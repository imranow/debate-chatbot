import os
from dataclasses import dataclass
from typing import Optional


def _load_dotenv_if_available() -> None:
    # Local dev convenience. In production, prefer real environment variables.
    try:
        from dotenv import load_dotenv  # type: ignore
    except Exception:
        return
    load_dotenv()


_load_dotenv_if_available()


@dataclass(frozen=True)
class Settings:
    pinecone_api_key: str
    pinecone_index_name: str
    pinecone_namespace: str
    pinecone_cloud: str
    pinecone_region: str
    pinecone_index_host: Optional[str]
    pinecone_embed_model: str
    pinecone_embed_field: str
    anthropic_api_key: str
    anthropic_model: str
    top_k: int
    max_context_chars: int


def _require(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise RuntimeError("Missing required environment variable: %s" % name)
    return v


def _get_int(name: str, default: int) -> int:
    v = os.getenv(name)
    if not v:
        return default
    try:
        return int(v)
    except ValueError as e:
        raise RuntimeError("Invalid int for %s: %r" % (name, v)) from e


def get_settings() -> Settings:
    return Settings(
        pinecone_api_key=_require("PINECONE_API_KEY"),
        pinecone_index_name=os.getenv("PINECONE_INDEX_NAME", "dem-debates-transcripts"),
        pinecone_namespace=os.getenv("PINECONE_NAMESPACE", "debates"),
        pinecone_cloud=os.getenv("PINECONE_CLOUD", "aws"),
        pinecone_region=os.getenv("PINECONE_REGION", "us-east-1"),
        pinecone_index_host=os.getenv("PINECONE_INDEX_HOST") or None,
        pinecone_embed_model=os.getenv("PINECONE_EMBED_MODEL", "multilingual-e5-large"),
        pinecone_embed_field=os.getenv("PINECONE_EMBED_FIELD", "chunk_text"),
        anthropic_api_key=_require("ANTHROPIC_API_KEY"),
        anthropic_model=os.getenv("ANTHROPIC_MODEL", "claude-sonnet-4-20250514"),
        top_k=_get_int("TOP_K", 8),
        max_context_chars=_get_int("MAX_CONTEXT_CHARS", 12000),
    )

