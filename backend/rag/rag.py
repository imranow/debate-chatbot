from __future__ import annotations

import logging
from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING

from backend.config import Settings
from backend.rag.anthropic_client import extract_text
from backend.rag.exceptions import LLMError, RetrievalError
from backend.rag.prompts import SYSTEM_PROMPT, build_user_prompt
from backend.rag.retrieval import (
    enrich_with_graph,
    hybrid_search,
    render_sources,
    search_pinecone_records,
    SourcesMetadata,
)

if TYPE_CHECKING:
    from backend.rag.bm25_index import BM25Index
    from backend.rag.knowledge_graph import KnowledgeGraph

logger = logging.getLogger(__name__)


async def _retrieve_chunks(
    *,
    index: Any,
    settings: Settings,
    question: str,
    k: int,
    bm25_index: Optional[BM25Index],
) -> list:
    """Try hybrid search with fallbacks: hybrid -> BM25-only -> semantic-only."""
    try:
        return await hybrid_search(index, settings, question, k, bm25_index=bm25_index)
    except Exception as exc:
        logger.warning("Hybrid/Pinecone search failed, trying BM25-only: %s", exc)

    # Fallback 1: BM25-only
    if bm25_index is not None:
        try:
            import asyncio
            return await asyncio.to_thread(bm25_index.search, question, top_k=k)
        except Exception as exc:
            logger.warning("BM25 fallback failed, trying semantic-only: %s", exc)

    # Fallback 2: semantic-only (no BM25 merge)
    try:
        return await search_pinecone_records(index, settings, question, k)
    except Exception as exc:
        logger.error("All retrieval methods failed: %s", exc)
        raise RetrievalError("All retrieval methods failed") from exc


async def answer_question(
    *,
    index: Any,
    anthropic_client: Any,
    settings: Settings,
    question: str,
    top_k: Optional[int] = None,
    bm25_index: Optional[BM25Index] = None,
    knowledge_graph: Optional[KnowledgeGraph] = None,
) -> Tuple[str, List[Dict[str, Any]], SourcesMetadata]:
    k = int(top_k) if top_k is not None else settings.top_k
    if k < 1:
        k = 1
    if k > 50:
        k = 50

    # Retrieval with fallback chain
    chunks = await _retrieve_chunks(
        index=index, settings=settings, question=question, k=k,
        bm25_index=bm25_index,
    )

    # Knowledge graph enrichment
    graph_context = None
    if knowledge_graph is not None:
        chunks, graph_context = await enrich_with_graph(
            chunks, knowledge_graph, bm25_index, question,
        )

    sources_text, citations, metadata = render_sources(chunks, settings=settings)

    if not sources_text.strip():
        return ("I don't know based on the provided transcripts.", [], metadata)

    # Prepend graph context if available
    if graph_context:
        sources_text = "GRAPH CONTEXT:\n" + graph_context + "\n\n" + sources_text

    user_prompt = build_user_prompt(question=question, sources_text=sources_text)

    try:
        msg = await anthropic_client.messages.create(
            model=settings.anthropic_model,
            max_tokens=900,
            temperature=0.2,
            system=SYSTEM_PROMPT,
            messages=[{"role": "user", "content": user_prompt}],
        )
    except Exception as exc:
        raise LLMError("LLM call failed: %s" % exc) from exc

    answer = extract_text(msg)
    if not answer:
        answer = "I don't know based on the provided transcripts."
    return answer, citations, metadata
