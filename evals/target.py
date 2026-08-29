"""Where the eval suite sends its questions.

By default the suite calls the RAG pipeline in-process, exactly as it always
has. That mode exercises the code but is blind to the deployment: it talks
straight to Pinecone and Anthropic, so it returns the same result whichever
service is live, and therefore cannot detect a deployment regression.

Setting EVAL_TARGET_URL switches the suite to POST /chat against a running
service instead, which is what makes a before/after comparison across a
migration mean anything.
"""

import asyncio
import os
from typing import Any, List, Optional, Tuple


def target_label() -> str:
    return os.getenv("EVAL_TARGET_URL") or "in-process"


def _run_in_process(question: str, settings, index, anthropic_client) -> Tuple[str, List[str]]:
    from backend.rag.rag import answer_question

    answer, citations, _ = asyncio.run(
        answer_question(
            index=index,
            anthropic_client=anthropic_client,
            settings=settings,
            question=question,
        )
    )
    return answer, [c["text"] for c in citations if c.get("text")]


def _run_over_http(question: str, base_url: str) -> Tuple[str, List[str]]:
    import json
    import urllib.request

    headers = {"content-type": "application/json"}
    api_key = os.getenv("API_KEY")
    if api_key:
        headers["X-API-Key"] = api_key

    timeout = float(os.getenv("EVAL_HTTP_TIMEOUT", "120"))
    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat",
        data=json.dumps({"question": question}).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read().decode("utf-8"))

    citations = body.get("citations") or []
    return body.get("answer", ""), [c["text"] for c in citations if c.get("text")]


def run_rag_pipeline(
    question: str,
    settings: Any = None,
    index: Any = None,
    anthropic_client: Any = None,
) -> Tuple[str, List[str]]:
    """Return (answer, retrieval_context) from whichever target is configured."""
    base_url: Optional[str] = os.getenv("EVAL_TARGET_URL")
    if base_url:
        return _run_over_http(question, base_url)
    return _run_in_process(question, settings, index, anthropic_client)
