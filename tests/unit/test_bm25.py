"""Unit tests for BM25Index: tokenizer, search, ID lookup, and save/load roundtrip."""

import io
import os
import pickle
import tempfile

import pytest

from backend.rag.bm25_index import BM25Index, BM25Document, _tokenize


class TestTokenize:

    def test_basic_tokenization(self):
        assert _tokenize("Hello, World!") == ["hello", "world"]

    def test_numbers_included(self):
        assert "2020" in _tokenize("debate in 2020")

    def test_empty_string(self):
        assert _tokenize("") == []

    def test_whitespace_only(self):
        assert _tokenize("   ") == []

    def test_punctuation_stripped(self):
        tokens = _tokenize("it's a test.")
        assert "it" in tokens
        assert "s" in tokens
        assert "a" in tokens
        assert "test" in tokens
        # punctuation characters should not appear
        assert "." not in tokens
        assert "'" not in tokens

    def test_unicode_letters_lowercased(self):
        tokens = _tokenize("BIDEN spoke")
        assert "biden" in tokens
        assert "spoke" in tokens


class TestBM25IndexSearch:

    def _build_index(self):
        docs = [
            BM25Document(id="row-1", tokens=_tokenize("healthcare insurance policy"), fields={"speech": "healthcare insurance policy"}),
            BM25Document(id="row-2", tokens=_tokenize("immigration border wall"), fields={"speech": "immigration border wall"}),
            BM25Document(id="row-3", tokens=_tokenize("climate change energy"), fields={"speech": "climate change energy"}),
        ]
        return BM25Index(docs)

    def test_relevant_doc_scores_highest(self):
        index = self._build_index()
        results = index.search("healthcare policy", top_k=3)
        assert results[0].id == "row-1"

    def test_top_k_limits_results(self):
        index = self._build_index()
        results = index.search("healthcare immigration climate", top_k=2)
        assert len(results) <= 2

    def test_scores_normalized_to_01(self):
        index = self._build_index()
        results = index.search("healthcare", top_k=3)
        for r in results:
            assert 0.0 <= r.score <= 1.0

    def test_top_result_has_score_1(self):
        index = self._build_index()
        results = index.search("healthcare", top_k=3)
        assert results[0].score == pytest.approx(1.0)

    def test_empty_query_returns_empty(self):
        index = self._build_index()
        assert index.search("", top_k=5) == []

    def test_zero_scoring_docs_excluded(self):
        """Docs with no matching tokens should not appear in results."""
        index = self._build_index()
        results = index.search("healthcare", top_k=3)
        ids = [r.id for r in results]
        # immigration and climate docs have no overlap with "healthcare"
        assert "row-2" not in ids
        assert "row-3" not in ids

    def test_fields_preserved_in_results(self):
        index = self._build_index()
        results = index.search("healthcare", top_k=1)
        assert results[0].fields["speech"] == "healthcare insurance policy"


class TestGetDocumentById:

    def test_existing_id_returns_document(self):
        doc = BM25Document(id="row-42", tokens=["test"], fields={"speech": "test"})
        index = BM25Index([doc])
        result = index.get_document_by_id("row-42")
        assert result is not None
        assert result.id == "row-42"

    def test_missing_id_returns_none(self):
        doc = BM25Document(id="row-1", tokens=["test"], fields={})
        index = BM25Index([doc])
        assert index.get_document_by_id("nonexistent") is None


class TestSaveLoadRoundtrip:

    def test_roundtrip_preserves_search_results(self):
        docs = [
            BM25Document(id="row-1", tokens=_tokenize("healthcare policy"), fields={"speech": "healthcare policy"}),
            BM25Document(id="row-2", tokens=_tokenize("climate energy"), fields={"speech": "climate energy"}),
        ]
        original = BM25Index(docs)

        with tempfile.NamedTemporaryFile(suffix=".pkl", delete=False) as f:
            path = f.name
        try:
            original.save(path)
            loaded = BM25Index.load(path)

            original_results = original.search("healthcare", top_k=2)
            loaded_results = loaded.search("healthcare", top_k=2)

            assert [r.id for r in original_results] == [r.id for r in loaded_results]
            assert loaded.num_documents == original.num_documents
        finally:
            os.unlink(path)

    def test_save_creates_missing_directories(self):
        docs = [BM25Document(id="row-1", tokens=["test"], fields={})]
        index = BM25Index(docs)

        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "nested", "dir", "index.pkl")
            index.save(path)
            assert os.path.exists(path)
