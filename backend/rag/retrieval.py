from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Sequence, Tuple

from backend.config import Settings


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
