import argparse
import csv
import json
import os
import sys
import time
from typing import Any, Dict, List, Optional, Tuple

import networkx as nx  # type: ignore


EXTRACTION_PROMPT = """Extract entities and relationships from these debate speech excerpts.

Return a JSON object with two arrays:
- "entities": objects with "name" (canonical lowercase), "type" (one of: person, topic, position, organization)
- "relationships": objects with "source" (entity name), "target" (entity name), "type" (one of: argues_for, argues_against, mentions, responds_to), "row_id" (the Row ID of the speech)

Rules:
- Use canonical lowercase names (e.g., "bernie sanders", "medicare for all", "climate change")
- Speaker names are always type "person"
- Policy positions, bills, and concepts are type "topic"
- Specific stances are type "position"
- Only extract clear, explicit relationships from the text
- Keep entity names short and consistent

Speeches:
{speeches}

Return ONLY the JSON object, no other text."""


def _open_csv_with_guess(path: str) -> Tuple[Any, str]:
    encodings = ["utf-8-sig", "utf-8", "cp1252", "latin-1"]
    for enc in encodings:
        try:
            f = open(path, "r", encoding=enc, newline="")
            f.read(4096)
            f.seek(0)
            return f, enc
        except UnicodeDecodeError:
            continue
    f = open(path, "r", encoding="utf-8", errors="replace", newline="")
    return f, "utf-8(replace)"


def _read_speeches(csv_path: str) -> List[Dict[str, Any]]:
    speeches = []
    f, _enc = _open_csv_with_guess(csv_path)
    with f:
        reader = csv.DictReader(f)
        row_id = 0
        for row in reader:
            row_id += 1
            speech = (row.get("speech") or "").strip()
            if not speech:
                continue
            speeches.append({
                "row_id": "row-%d" % row_id,
                "speaker": (row.get("speaker") or "").strip(),
                "speech": speech[:500],  # truncate long speeches for extraction
                "date": (row.get("date") or "").strip(),
                "debate_name": (row.get("debate_name") or "").strip(),
            })
    return speeches


def _batch(items: list, size: int) -> List[list]:
    return [items[i:i + size] for i in range(0, len(items), size)]


def _extract_batch(client: Any, model: str, batch: List[Dict]) -> Dict:
    speeches_text = "\n\n".join(
        "Row ID: %s\nSpeaker: %s\nDate: %s\nSpeech: %s" % (
            s["row_id"], s["speaker"], s["date"], s["speech"]
        )
        for s in batch
    )
    prompt = EXTRACTION_PROMPT.format(speeches=speeches_text)

    msg = client.messages.create(
        model=model,
        max_tokens=4096,
        temperature=0.0,
        messages=[{"role": "user", "content": prompt}],
    )
    text = msg.content[0].text.strip()

    # Try to extract JSON from the response
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Try extracting from code blocks
        for block in text.split("```"):
            block = block.strip()
            if block.startswith("json"):
                block = block[4:].strip()
            try:
                return json.loads(block)
            except json.JSONDecodeError:
                continue
    return {"entities": [], "relationships": []}


def _normalize_name(name: str) -> str:
    return name.lower().strip()


def build_graph(
    csv_path: str,
    client: Any,
    model: str,
    batch_size: int = 5,
    resume_path: Optional[str] = None,
) -> nx.DiGraph:
    speeches = _read_speeches(csv_path)
    print("Read %d speeches from CSV" % len(speeches))

    # Load progress if resuming
    processed_row_ids = set()
    all_entities: List[Dict] = []
    all_relationships: List[Dict] = []

    if resume_path and os.path.exists(resume_path):
        with open(resume_path, "r") as f:
            progress = json.load(f)
        processed_row_ids = set(progress.get("processed_row_ids", []))
        all_entities = progress.get("entities", [])
        all_relationships = progress.get("relationships", [])
        print("Resuming from %d processed rows" % len(processed_row_ids))

    # Filter out already processed speeches
    remaining = [s for s in speeches if s["row_id"] not in processed_row_ids]
    batches = _batch(remaining, batch_size)
    print("Processing %d remaining speeches in %d batches..." % (len(remaining), len(batches)))

    for i, batch in enumerate(batches):
        try:
            result = _extract_batch(client, model, batch)
            all_entities.extend(result.get("entities", []))
            all_relationships.extend(result.get("relationships", []))
            for s in batch:
                processed_row_ids.add(s["row_id"])
        except Exception as e:
            print("  Error on batch %d: %s" % (i + 1, e))

        if (i + 1) % 10 == 0:
            print("  Processed %d/%d batches" % (i + 1, len(batches)))
            # Save progress
            if resume_path:
                with open(resume_path, "w") as f:
                    json.dump({
                        "processed_row_ids": list(processed_row_ids),
                        "entities": all_entities,
                        "relationships": all_relationships,
                    }, f)

    # Also ensure all speakers are person nodes
    speaker_names = set()
    for s in speeches:
        if s["speaker"]:
            speaker_names.add(_normalize_name(s["speaker"]))

    # Build NetworkX graph
    graph = nx.DiGraph()

    # Add speaker nodes
    for name in speaker_names:
        graph.add_node(name, name=name, type="person")

    # Add extracted entities
    for entity in all_entities:
        name = _normalize_name(entity.get("name", ""))
        if not name:
            continue
        etype = entity.get("type", "topic")
        if name in graph:
            # Merge: keep existing type if already set
            pass
        else:
            graph.add_node(name, name=name, type=etype)

    # Add relationships
    for rel in all_relationships:
        src = _normalize_name(rel.get("source", ""))
        dst = _normalize_name(rel.get("target", ""))
        rel_type = rel.get("type", "mentions")
        row_id = rel.get("row_id", "")

        if not src or not dst:
            continue
        # Ensure both nodes exist
        if src not in graph:
            graph.add_node(src, name=src, type="topic")
        if dst not in graph:
            graph.add_node(dst, name=dst, type="topic")

        # Add or update edge
        if graph.has_edge(src, dst):
            edge_data = graph[src][dst]
            if edge_data.get("type") != rel_type:
                # Different relationship type - add as separate edge (use multigraph fallback: append row_ids)
                edge_data.setdefault("source_row_ids", []).append(row_id)
            else:
                edge_data.setdefault("source_row_ids", []).append(row_id)
        else:
            graph.add_edge(src, dst, type=rel_type, source_row_ids=[row_id] if row_id else [])

    return graph


def main(argv: Optional[List[str]] = None) -> int:
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv(override=True)
    except Exception:
        pass

    parser = argparse.ArgumentParser(description="Build knowledge graph from debate CSV using Claude.")
    parser.add_argument(
        "--csv",
        default="debate_transcripts_v3_2020-02-26.csv",
        help="Path to the transcripts CSV (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default="data/knowledge_graph.json",
        help="Output JSON path (default: %(default)s)",
    )
    parser.add_argument(
        "--model",
        default=os.getenv("ANTHROPIC_MODEL", "claude-haiku-4-5-20251001"),
        help="Anthropic model for extraction (default: %(default)s)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=5,
        help="Speeches per Claude API call (default: %(default)s)",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Resume from previous progress (uses data/graph_progress.json)",
    )
    args = parser.parse_args(argv)

    if not os.path.exists(args.csv):
        print("CSV not found: %s" % args.csv)
        return 1

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not set")
        return 1

    import anthropic  # type: ignore
    client = anthropic.Anthropic(api_key=api_key)

    resume_path = "data/graph_progress.json" if args.resume else None

    t0 = time.time()
    graph = build_graph(args.csv, client, args.model, args.batch_size, resume_path)
    dt = time.time() - t0

    print("Graph built: %d nodes, %d edges (%.0fs)" % (
        graph.number_of_nodes(), graph.number_of_edges(), dt))

    # Save using KnowledgeGraph wrapper
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    from backend.rag.knowledge_graph import KnowledgeGraph
    kg = KnowledgeGraph(graph)
    kg.save(args.output)
    print("Saved to %s" % args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
