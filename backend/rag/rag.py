from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple, TYPE_CHECKING

from backend.config import Settings
from backend.rag.anthropic_client import extract_text
from backend.rag.prompts import SYSTEM_PROMPT, build_user_prompt
from backend.rag.retrieval import enrich_with_graph, hybrid_search, render_sources

if TYPE_CHECKING:
    from backend.rag.bm25_index import BM25Index
    from backend.rag.knowledge_graph import KnowledgeGraph


def answer_question(
    *,
    index: Any,
    anthropic_client: Any,
    settings: Settings,
    question: str,
    top_k: Optional[int] = None,
    bm25_index: Optional[BM25Index] = None,
    knowledge_graph: Optional[KnowledgeGraph] = None,
) -> Tuple[str, List[Dict[str, Any]]]:
    k = int(top_k) if top_k is not None else settings.top_k
    if k < 1:
        k = 1
    if k > 50:
        k = 50

    # Hybrid search: semantic + BM25 with RRF merge
    chunks = hybrid_search(index, settings, question, k, bm25_index=bm25_index)

    # Knowledge graph enrichment
    graph_context = None
    if knowledge_graph is not None:
        chunks, graph_context = enrich_with_graph(
            chunks, knowledge_graph, bm25_index, question,
        )

    sources_text, citations = render_sources(chunks, settings=settings)

    if not sources_text.strip():
        return ("I don't know based on the provided transcripts.", [])

    # Prepend graph context if available
    if graph_context:
        sources_text = "GRAPH CONTEXT:\n" + graph_context + "\n\n" + sources_text

    user_prompt = build_user_prompt(question=question, sources_text=sources_text)

    msg = anthropic_client.messages.create(
        model=settings.anthropic_model,
        max_tokens=900,
        temperature=0.2,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_prompt}],
    )
    answer = extract_text(msg)
    if not answer:
        answer = "I don't know based on the provided transcripts."
    return answer, citations
