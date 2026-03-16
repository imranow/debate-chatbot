from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, TYPE_CHECKING

from backend.config import Settings

if TYPE_CHECKING:
    from backend.rag.bm25_index import BM25Index
    from backend.rag.knowledge_graph import KnowledgeGraph


@dataclass
class RetrievedChunk:
    id: str
    score: float
    fields: Dict[str, Any]


def _coerce_hits(resp: Any) -> List[Dict[str, Any]]:
    # Pinecone SDKs have returned a few shapes over time; handle the common ones.
    if resp is None:
        return []
    if isinstance(resp, dict):
        if isinstance(resp.get("result"), dict) and isinstance(resp["result"].get("hits"), list):
            return resp["result"]["hits"]
        if isinstance(resp.get("hits"), list):
            return resp["hits"]
        if isinstance(resp.get("matches"), list):
            return resp["matches"]
        return []
    # Some SDK versions return an object with .result.hits
    result = getattr(resp, "result", None)
    hits = getattr(result, "hits", None)
    if isinstance(hits, list):
        return hits
    return []


def search_pinecone_records(index: Any, settings: Settings, question: str, top_k: int) -> List[RetrievedChunk]:
    fields = [
        settings.pinecone_embed_field,
        "speech",
        "speaker",
        "date",
        "debate_name",
        "debate_section",
        "speaking_time_seconds",
    ]
    query = {"inputs": {"text": question}, "top_k": top_k}

    # Newer Pinecone SDK: index.search(namespace=..., query=..., fields=[...])
    try:
        if hasattr(index, "search"):
            resp = index.search(namespace=settings.pinecone_namespace, query=query, fields=fields)
        elif hasattr(index, "search_records"):
            resp = index.search_records(namespace=settings.pinecone_namespace, query=query, fields=fields)
        else:
            raise AttributeError("Pinecone Index is missing search/search_records (SDK too old?)")
    except TypeError:
        # Older signature: (namespace, query, fields)
        if hasattr(index, "search"):
            resp = index.search(settings.pinecone_namespace, query, fields)
        else:
            resp = index.search_records(settings.pinecone_namespace, query, fields)

    chunks: List[RetrievedChunk] = []
    for h in _coerce_hits(resp):
        rid = h.get("_id") or h.get("id") or ""
        score = h.get("_score") or h.get("score") or 0.0
        try:
            score_f = float(score)
        except Exception:
            score_f = 0.0
        f = h.get("fields") or h.get("metadata") or {}
        if not isinstance(f, dict):
            f = {}
        chunks.append(RetrievedChunk(id=str(rid), score=score_f, fields=f))
    return chunks


def merge_rrf(
    semantic_chunks: List[RetrievedChunk],
    bm25_chunks: List[RetrievedChunk],
    top_k: int,
    k: int = 60,
    alpha: float = 0.5,
) -> List[RetrievedChunk]:
    """Reciprocal Rank Fusion: combine semantic and BM25 rankings."""
    scores: Dict[str, float] = {}
    chunk_map: Dict[str, RetrievedChunk] = {}

    for rank, chunk in enumerate(semantic_chunks):
        rrf = 1.0 / (k + rank + 1)
        scores[chunk.id] = scores.get(chunk.id, 0.0) + alpha * rrf
        # Prefer semantic chunk (has Pinecone fields)
        chunk_map[chunk.id] = chunk

    for rank, chunk in enumerate(bm25_chunks):
        rrf = 1.0 / (k + rank + 1)
        scores[chunk.id] = scores.get(chunk.id, 0.0) + (1 - alpha) * rrf
        if chunk.id not in chunk_map:
            chunk_map[chunk.id] = chunk

    sorted_ids = sorted(scores, key=lambda cid: scores[cid], reverse=True)[:top_k]
    return [
        RetrievedChunk(id=cid, score=scores[cid], fields=chunk_map[cid].fields)
        for cid in sorted_ids
    ]


def hybrid_search(
    index: Any,
    settings: Settings,
    question: str,
    top_k: int,
    bm25_index: Optional[BM25Index] = None,
) -> List[RetrievedChunk]:
    """Run semantic + optional BM25 search, merge with RRF."""
    fetch_k = min(top_k * 3, 50)

    semantic_chunks = search_pinecone_records(index, settings, question, fetch_k)

    if bm25_index is None:
        return semantic_chunks[:top_k]

    bm25_chunks = bm25_index.search(question, top_k=fetch_k)
    return merge_rrf(
        semantic_chunks, bm25_chunks,
        top_k=top_k, alpha=settings.hybrid_alpha,
    )


def enrich_with_graph(
    chunks: List[RetrievedChunk],
    knowledge_graph: Optional[KnowledgeGraph],
    bm25_index: Optional[BM25Index],
    query: str,
    max_graph_additions: int = 3,
) -> Tuple[List[RetrievedChunk], Optional[str]]:
    """Add graph-derived related chunks and return graph context text."""
    if knowledge_graph is None:
        return chunks, None

    graph_context = knowledge_graph.format_graph_context(query)

    # Find related row IDs from graph
    row_ids = knowledge_graph.get_enrichment_row_ids(query, max_results=max_graph_additions)
    existing_ids: Set[str] = {c.id for c in chunks}
    new_ids = [rid for rid in row_ids if rid not in existing_ids]

    if new_ids and bm25_index is not None:
        for rid in new_ids:
            doc = bm25_index.get_document_by_id(rid)
            if doc is not None:
                chunks.append(RetrievedChunk(
                    id=doc.id,
                    score=0.0,
                    fields=dict(doc.fields),
                ))

    return chunks, graph_context


def render_sources(chunks: Sequence[RetrievedChunk], settings: Settings) -> Tuple[str, List[Dict[str, Any]]]:
    """
    Returns (sources_text_for_prompt, citations_json).
    """
    remaining = max(1000, settings.max_context_chars)
    lines: List[str] = []
    citations: List[Dict[str, Any]] = []

    for i, c in enumerate(chunks, start=1):
        f = c.fields
        date = (f.get("date") or "").strip() if isinstance(f.get("date"), str) else str(f.get("date") or "")
        debate_name = (f.get("debate_name") or "").strip() if isinstance(f.get("debate_name"), str) else str(f.get("debate_name") or "")
        debate_section = (f.get("debate_section") or "").strip() if isinstance(f.get("debate_section"), str) else str(f.get("debate_section") or "")
        speaker = (f.get("speaker") or "").strip() if isinstance(f.get("speaker"), str) else str(f.get("speaker") or "")

        # Prefer the raw speech for quoting; fall back to the embedded field.
        raw_text = f.get("speech")
        if not raw_text:
            raw_text = f.get(settings.pinecone_embed_field)
        if raw_text is None:
            raw_text = ""
        if not isinstance(raw_text, str):
            raw_text = str(raw_text)
        raw_text = raw_text.strip()

        # Per-source truncation so one huge turn doesn't crowd out everything.
        per_source_limit = 1200
        excerpt = raw_text[:per_source_limit]
        if len(raw_text) > per_source_limit:
            excerpt = excerpt.rstrip() + "…"

        header = "[%d] %s | %s | %s | %s" % (i, date, debate_name, debate_section, speaker)
        block = header + "\n" + excerpt + "\n"

        if len(block) > remaining:
            block = block[:remaining].rstrip() + "\n"
        remaining -= len(block)
        lines.append(block)

        citations.append(
            {
                "id": c.id,
                "score": c.score,
                "date": date or None,
                "debate_name": debate_name or None,
                "debate_section": debate_section or None,
                "speaker": speaker or None,
                "text": excerpt,
            }
        )

        if remaining <= 0:
            break

    return ("\n".join(lines).strip(), citations)
