"""Unit tests for _retrieve_chunks fallback chain in rag.py."""

import pytest
from unittest.mock import AsyncMock, MagicMock, patch

from backend.rag.exceptions import RetrievalError
from backend.rag.rag import _retrieve_chunks
from backend.rag.retrieval import RetrievedChunk


def _make_settings():
    from backend.config import Settings
    return Settings(
        pinecone_api_key="test",
        pinecone_index_name="test",
        pinecone_namespace="test",
        pinecone_cloud="aws",
        pinecone_region="us-east-1",
        pinecone_index_host=None,
        pinecone_embed_model="test",
        pinecone_embed_field="chunk_text",
        anthropic_api_key="test",
        anthropic_model="test",
        top_k=8,
        max_context_chars=12000,
        hybrid_alpha=0.5,
        enable_knowledge_graph=False,
        csv_path="test.csv",
        bm25_index_path="test.pkl",
        knowledge_graph_path="test.json",
        api_key=None,
        per_source_limit=1200,
        max_tokens=900,
        llm_temperature=0.2,
    )


def _chunk(id: str) -> RetrievedChunk:
    return RetrievedChunk(id=id, score=0.9, fields={"speech": "test"})


@pytest.mark.asyncio
async def test_hybrid_success_returns_immediately():
    """When hybrid search succeeds, return its result without trying fallbacks."""
    expected = [_chunk("a"), _chunk("b")]
    with patch("backend.rag.rag.hybrid_search", new=AsyncMock(return_value=expected)):
        with patch("backend.rag.rag.search_pinecone_records", new=AsyncMock()) as mock_semantic:
            result = await _retrieve_chunks(
                index=MagicMock(), settings=_make_settings(),
                question="test", k=5, bm25_index=MagicMock(),
            )
    assert result == expected
    mock_semantic.assert_not_called()


@pytest.mark.asyncio
async def test_hybrid_fails_falls_back_to_bm25():
    """When hybrid search raises, fall back to BM25-only search."""
    bm25_results = [_chunk("bm25-1")]
    bm25_index = MagicMock()
    bm25_index.search = MagicMock(return_value=bm25_results)

    with patch("backend.rag.rag.hybrid_search", new=AsyncMock(side_effect=Exception("pinecone down"))):
        result = await _retrieve_chunks(
            index=MagicMock(), settings=_make_settings(),
            question="test", k=5, bm25_index=bm25_index,
        )
    assert result == bm25_results


@pytest.mark.asyncio
async def test_hybrid_and_bm25_fail_falls_back_to_semantic():
    """When hybrid and BM25 both fail, fall back to semantic-only search."""
    semantic_results = [_chunk("semantic-1")]
    bm25_index = MagicMock()
    bm25_index.search = MagicMock(side_effect=Exception("bm25 broken"))

    with patch("backend.rag.rag.hybrid_search", new=AsyncMock(side_effect=Exception("pinecone down"))):
        with patch("backend.rag.rag.search_pinecone_records", new=AsyncMock(return_value=semantic_results)):
            result = await _retrieve_chunks(
                index=MagicMock(), settings=_make_settings(),
                question="test", k=5, bm25_index=bm25_index,
            )
    assert result == semantic_results


@pytest.mark.asyncio
async def test_no_bm25_index_skips_bm25_fallback():
    """When bm25_index is None, BM25 fallback is skipped; go straight to semantic."""
    semantic_results = [_chunk("sem-1")]

    with patch("backend.rag.rag.hybrid_search", new=AsyncMock(side_effect=Exception("down"))):
        with patch("backend.rag.rag.search_pinecone_records", new=AsyncMock(return_value=semantic_results)):
            result = await _retrieve_chunks(
                index=MagicMock(), settings=_make_settings(),
                question="test", k=5, bm25_index=None,
            )
    assert result == semantic_results


@pytest.mark.asyncio
async def test_all_methods_fail_raises_retrieval_error():
    """When all three retrieval methods fail, raise RetrievalError."""
    bm25_index = MagicMock()
    bm25_index.search = MagicMock(side_effect=Exception("bm25 broken"))

    with patch("backend.rag.rag.hybrid_search", new=AsyncMock(side_effect=Exception("down"))):
        with patch("backend.rag.rag.search_pinecone_records", new=AsyncMock(side_effect=Exception("semantic down"))):
            with pytest.raises(RetrievalError):
                await _retrieve_chunks(
                    index=MagicMock(), settings=_make_settings(),
                    question="test", k=5, bm25_index=bm25_index,
                )


@pytest.mark.asyncio
async def test_all_methods_fail_no_bm25_raises_retrieval_error():
    """RetrievalError raised when no BM25 and both remaining methods fail."""
    with patch("backend.rag.rag.hybrid_search", new=AsyncMock(side_effect=Exception("down"))):
        with patch("backend.rag.rag.search_pinecone_records", new=AsyncMock(side_effect=Exception("down"))):
            with pytest.raises(RetrievalError):
                await _retrieve_chunks(
                    index=MagicMock(), settings=_make_settings(),
                    question="test", k=5, bm25_index=None,
                )
