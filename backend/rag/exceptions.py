"""Typed exceptions for the RAG pipeline."""


class RAGError(Exception):
    """Base exception for RAG pipeline errors."""


class RetrievalError(RAGError):
    """Raised when retrieval (Pinecone or BM25) fails."""


class LLMError(RAGError):
    """Raised when the LLM call fails."""
