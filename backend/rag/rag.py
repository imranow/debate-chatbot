from typing import Any, Dict, List, Optional, Tuple

from backend.config import Settings
from backend.rag.anthropic_client import extract_text
from backend.rag.prompts import SYSTEM_PROMPT, build_user_prompt
from backend.rag.retrieval import render_sources, search_pinecone_records


def answer_question(
    *,
    index: Any,
    anthropic_client: Any,
    settings: Settings,
    question: str,
    top_k: Optional[int] = None,
) -> Tuple[str, List[Dict[str, Any]]]:
    k = int(top_k) if top_k is not None else settings.top_k
    if k < 1:
        k = 1
    if k > 50:
        k = 50

    chunks = search_pinecone_records(index=index, settings=settings, question=question, top_k=k)
    sources_text, citations = render_sources(chunks, settings=settings)

    if not sources_text.strip():
        return ("I don't know based on the provided transcripts.", [])

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

