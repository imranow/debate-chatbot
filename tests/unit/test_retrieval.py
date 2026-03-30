"""Unit tests for retrieval functions: RRF merge and render_sources."""

from backend.config import Settings
from backend.rag.retrieval import RetrievedChunk, merge_rrf, render_sources


def _make_settings(**overrides) -> Settings:
    defaults = dict(
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
    defaults.update(overrides)
    return Settings(**defaults)


def _chunk(id: str, score: float, speech: str = "test speech") -> RetrievedChunk:
    return RetrievedChunk(id=id, score=score, fields={"speech": speech, "speaker": "Alice", "date": "2020-01-01", "debate_name": "Debate 1", "debate_section": "Opening"})


class TestMergeRRF:

    def test_basic_merge(self):
        semantic = [_chunk("a", 0.9), _chunk("b", 0.7)]
        bm25 = [_chunk("b", 0.8), _chunk("c", 0.6)]
        merged = merge_rrf(semantic, bm25, top_k=3, k=60, alpha=0.5)

        ids = [c.id for c in merged]
        # "b" appears in both lists so should get the highest combined score
        assert ids[0] == "b"
        assert len(merged) == 3
        assert set(ids) == {"a", "b", "c"}

    def test_top_k_limits_output(self):
        semantic = [_chunk("a", 0.9), _chunk("b", 0.8), _chunk("c", 0.7)]
        bm25 = [_chunk("d", 0.9), _chunk("e", 0.8)]
        merged = merge_rrf(semantic, bm25, top_k=2, k=60, alpha=0.5)
        assert len(merged) == 2

    def test_alpha_weighting(self):
        semantic = [_chunk("a", 0.9)]
        bm25 = [_chunk("b", 0.9)]
        # alpha=1.0 means only semantic matters
        merged = merge_rrf(semantic, bm25, top_k=2, k=60, alpha=1.0)
        assert merged[0].id == "a"
        # alpha=0.0 means only BM25 matters
        merged = merge_rrf(semantic, bm25, top_k=2, k=60, alpha=0.0)
        assert merged[0].id == "b"

    def test_empty_inputs(self):
        assert merge_rrf([], [], top_k=5) == []
        semantic = [_chunk("a", 0.9)]
        merged = merge_rrf(semantic, [], top_k=5, alpha=0.5)
        assert len(merged) == 1
        assert merged[0].id == "a"

    def test_rrf_scores_are_positive(self):
        semantic = [_chunk("a", 0.9), _chunk("b", 0.5)]
        bm25 = [_chunk("c", 0.8)]
        merged = merge_rrf(semantic, bm25, top_k=3)
        for chunk in merged:
            assert chunk.score > 0

    def test_duplicate_ids_merged(self):
        """Same chunk in both lists should appear once with combined score."""
        semantic = [_chunk("a", 0.9)]
        bm25 = [_chunk("a", 0.8)]
        merged = merge_rrf(semantic, bm25, top_k=5, k=60, alpha=0.5)
        assert len(merged) == 1
        # Combined score should be higher than either individual RRF contribution
        individual_rrf = 1.0 / (60 + 0 + 1)
        assert merged[0].score > individual_rrf * 0.5


class TestRenderSourcesTruncation:

    def test_returns_metadata(self):
        chunks = [_chunk("a", 0.9), _chunk("b", 0.5)]
        settings = _make_settings(max_context_chars=12000)
        text, citations, meta = render_sources(chunks, settings)
        assert meta.total_sources == 2
        assert meta.included_sources == 2
        assert meta.excluded_sources == 0
        assert meta.chars_used > 0
        assert meta.chars_budget == 12000

    def test_ranked_by_score(self):
        """Chunks should be ordered by score descending in output."""
        low = _chunk("low", 0.1, speech="low score speech")
        high = _chunk("high", 0.9, speech="high score speech")
        settings = _make_settings(max_context_chars=12000)
        text, citations, meta = render_sources([low, high], settings)
        # The first citation should be the higher-scored chunk
        assert citations[0]["id"] == "high"
        assert citations[1]["id"] == "low"

    def test_truncation_excludes_sources(self):
        """With a very small budget, not all sources fit."""
        chunks = [_chunk(f"c{i}", 1.0 - i * 0.1, speech="x" * 200) for i in range(10)]
        settings = _make_settings(max_context_chars=1000)
        text, citations, meta = render_sources(chunks, settings)
        assert meta.total_sources == 10
        assert meta.included_sources < 10
        assert meta.excluded_sources == 10 - meta.included_sources
        assert meta.chars_used <= meta.chars_budget + 100  # small margin for rounding

    def test_empty_chunks(self):
        settings = _make_settings()
        text, citations, meta = render_sources([], settings)
        assert text == ""
        assert citations == []
        assert meta.total_sources == 0
        assert meta.included_sources == 0

    def test_per_source_truncation(self):
        """A single huge speech gets truncated to ~1200 chars."""
        huge = _chunk("big", 0.9, speech="a" * 5000)
        settings = _make_settings(max_context_chars=12000)
        _, citations, _ = render_sources([huge], settings)
        # The excerpt should be capped around 1200 chars + ellipsis
        assert len(citations[0]["text"]) <= 1201
