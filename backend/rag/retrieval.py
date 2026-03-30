from __future__ import annotations

import asyncio
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple, TYPE_CHECKING

from backend.config import Settings

# RRF damping constant — algorithm parameter, not a deployment tuning knob.
_RRF_K = 60

if TYPE_CHECKING:
    from backend.rag.bm25_index import BM25Index
    from backend.rag.knowledge_graph import KnowledgeGraph


@dataclass
class RetrievedChunk:
    id: str
    score: float
    fields: Dict[str, Any]


@dataclass
class SourcesMetadata:
    total_sources: int
    included_sources: int
    excluded_sources: int
    chars_used: int
    chars_budget: int


async def search_pinecone_records(index: Any, settings: Settings, question: str, top_k: int) -> List[RetrievedChunk]:
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

    resp = await asyncio.to_thread(
        index.search,
        namespace=settings.pinecone_namespace,
        query=query,
        fields=fields,
    )

    chunks: List[RetrievedChunk] = []
    for hit in resp.result.hits:
        rid = getattr(hit, "_id", "") or ""
        score = getattr(hit, "_score", 0.0) or 0.0
        try:
            score_f = float(score)
        except Exception:
            score_f = 0.0
        f = getattr(hit, "fields", {}) or {}
        if not isinstance(f, dict):
            f = {}
        chunks.append(RetrievedChunk(id=str(rid), score=score_f, fields=f))
    return chunks


def _coerce_str(val: Any) -> str:
    """Coerce a metadata field value to a clean string."""
    if isinstance(val, str):
        return val.strip()
    return str(val) if val is not None else ""


def merge_rrf(
    semantic_chunks: List[RetrievedChunk],
    bm25_chunks: List[RetrievedChunk],
    top_k: int,
    k: int = _RRF_K,
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


async def hybrid_search(
    index: Any,
    settings: Settings,
    question: str,
    top_k: int,
    bm25_index: Optional[BM25Index] = None,
) -> List[RetrievedChunk]:
    """Run semantic + optional BM25 search, merge with RRF."""
    fetch_k = min(top_k * 3, 50)

    if bm25_index is None:
        return (await search_pinecone_records(index, settings, question, fetch_k))[:top_k]

    # Run Pinecone (network I/O) and BM25 (CPU) concurrently — they are independent.
    semantic_chunks, bm25_chunks = await asyncio.gather(
        search_pinecone_records(index, settings, question, fetch_k),
        asyncio.to_thread(bm25_index.search, question, top_k=fetch_k),
    )
    return merge_rrf(
        semantic_chunks, bm25_chunks,
        top_k=top_k, alpha=settings.hybrid_alpha,
    )


async def enrich_with_graph(
    chunks: List[RetrievedChunk],
    knowledge_graph: Optional[KnowledgeGraph],
    bm25_index: Optional[BM25Index],
    query: str,
    max_graph_additions: int = 3,
) -> Tuple[List[RetrievedChunk], Optional[str]]:
    """Add graph-derived related chunks and return graph context text."""
    if knowledge_graph is None:
        return chunks, None

    # Single find_entities pass for both context and row IDs.
    graph_context, row_ids = knowledge_graph.get_context_and_row_ids(
        query, max_results=max_graph_additions,
    )
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


def render_sources(
    chunks: Sequence[RetrievedChunk], settings: Settings,
) -> Tuple[str, List[Dict[str, Any]], SourcesMetadata]:
    """
    Rank chunks by score (highest first), then truncate to fit the context budget.
    Returns (sources_text_for_prompt, citations_json, metadata).
    """
    # Sort by score descending so the best chunks survive truncation.
    ranked = sorted(chunks, key=lambda c: c.score, reverse=True)

    budget = max(1000, settings.max_context_chars)
    remaining = budget
    lines: List[str] = []
    citations: List[Dict[str, Any]] = []
    included = 0

    per_source_limit = settings.per_source_limit

    for i, c in enumerate(ranked, start=1):
        f = c.fields
        date = _coerce_str(f.get("date"))
        debate_name = _coerce_str(f.get("debate_name"))
        debate_section = _coerce_str(f.get("debate_section"))
        speaker = _coerce_str(f.get("speaker"))

        # Prefer the raw speech for quoting; fall back to the embedded field.
        raw_text = f.get("speech") or f.get(settings.pinecone_embed_field) or ""
        if not isinstance(raw_text, str):
            raw_text = str(raw_text)
        raw_text = raw_text.strip()

        # Per-source truncation so one huge turn doesn't crowd out everything.
        excerpt = raw_text[:per_source_limit]
        if len(raw_text) > per_source_limit:
            excerpt = excerpt.rstrip() + "\u2026"

        header = "[%d] %s | %s | %s | %s" % (i, date, debate_name, debate_section, speaker)
        block = header + "\n" + excerpt + "\n"

        # Only include this source if its full block fits in the remaining budget.
        # A partially-truncated source would diverge from what the LLM actually sees.
        if len(block) > remaining:
            break
        remaining -= len(block)
        lines.append(block)
        included += 1

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

    metadata = SourcesMetadata(
        total_sources=len(ranked),
        included_sources=included,
        excluded_sources=len(ranked) - included,
        chars_used=budget - remaining,
        chars_budget=budget,
    )

    return ("\n".join(lines).strip(), citations, metadata)
