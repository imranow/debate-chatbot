from typing import Any, Tuple

from backend.config import Settings


def make_pinecone(settings: Settings) -> Tuple[Any, Any]:
    """
    Returns (pc, index). We keep typing loose because the Pinecone SDK has
    multiple optional transports and releases.
    """
    from pinecone import Pinecone  # type: ignore

    pc = Pinecone(api_key=settings.pinecone_api_key)
    if settings.pinecone_index_host:
        index = pc.Index(host=settings.pinecone_index_host)
    else:
        index = pc.Index(settings.pinecone_index_name)
    return pc, index

