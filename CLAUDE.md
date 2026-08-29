# Debate Chatbot — Claude Working Memory

## Project Overview
AI-powered Q&A chatbot grounded in **2019-2020 Democratic primary debate transcripts**.
Built with a production-grade RAG pipeline: hybrid search (BM25 + Pinecone semantic) merged via RRF, optional knowledge graph enrichment, and Claude as the LLM.

## Stack
- **Backend**: FastAPI + Uvicorn (async)
- **Retrieval**: Pinecone (semantic/vector) + BM25 (keyword), merged via Reciprocal Rank Fusion
- **Knowledge graph**: NetworkX (optional, JSON-persisted)
- **LLM**: Anthropic Claude
- **Frontend**: Static HTML/CSS/JS (`backend/web/`)
- **Evals**: DeepEval + Anthropic judge
- **Docker**: slim Python 3.11 image, health check at `/health`

## Key Files
| File | Purpose |
|---|---|
| `backend/main.py` | FastAPI app, routes, error handling |
| `backend/config.py` | `Settings` dataclass, env var mapping |
| `backend/rag/rag.py` | `answer_question()` — main RAG orchestration |
| `backend/rag/retrieval.py` | Hybrid search, RRF merge, ranked context truncation |
| `backend/rag/bm25_index.py` | BM25 index (pickle-serializable) |
| `backend/rag/knowledge_graph.py` | Entity linking + 1-hop graph traversal |
| `backend/rag/pinecone_client.py` | Pinecone adapter |
| `backend/rag/anthropic_client.py` | Anthropic adapter |
| `backend/rag/exceptions.py` | Typed exceptions: `RetrievalError`, `LLMError` |
| `backend/web/app.js` | Frontend chat logic, citation rendering, loading states |
| `evals/test_rag_evals.py` | DeepEval integration tests |
| `tests/unit/` | Unit tests for RRF, truncation, graph enrichment |

## Architecture Decisions
- **Hybrid alpha = 0.5** (configurable): balances semantic vs keyword retrieval
- **Ranked truncation**: sources sorted by score before char-limit truncation; metadata returned (`sources_excluded`, `context_chars_used`)
- **Fallback chain**: Pinecone fail → BM25-only → semantic-only → graceful error message
- **Knowledge graph**: substring entity matching (3+ chars), 1-hop traversal — known limitation: naive matching
- **Citations**: Claude generates `[1]`, `[2]` refs; no post-hoc validation yet (known gap)

## Recent Changes (PR #1)
- Multi-stage loading indicator with elapsed time in UI
- Clickable example questions for onboarding
- Relevance score badges on citations (green/amber/gray)
- Truncation indicators on cut-off source excerpts
- Typed exceptions + fallback chain in RAG pipeline
- 21 unit tests added in that PR; the suite is now 60 and all pass

## Testing
- Unit tests: `python -m pytest tests/unit/ -v` (60 passing)
- Evals in-process: `pytest evals/ -q` (needs live Pinecone and Anthropic)
- Evals against a deployment: `EVAL_TARGET_URL=https://... pytest evals/ -q`
- Deployment parity: `python -m evals.compare_deployments --baseline URL --candidate URL`

## Known Issues / Tech Debt

See `FOLLOW_UPS.md` for the two that matter, with root cause and fix options.

- **BM25 is not running in production.** The pickle is not in the image and the
  CSV is dockerignored, so `bm25_index` is always `None` and `hybrid_search`
  silently returns dense-only results. The hybrid/RRF code is correct and
  tested; it has never had an index to work with in a container.
- **The answer cache does not survive scale to zero.** It is a per-process LRU,
  so on Cloud Run at `min-instances 0` it dies with the instance. Accepted
  trade, not a defect.
- Knowledge graph entity matching is naive (substring, no NER/lemmatization)
- No citation accuracy validation (Claude could hallucinate citation indices)
- BM25 index is in-memory/pickled — not suitable for >1M docs
- No query/response logging or latency tracking, so the answer cache hit rate is unknown

## Conventions
- Type hints throughout; Pydantic models for API contracts
- Environment variables for all config (see `backend/config.py`)
- Tests live in `tests/unit/` — run with `python -m pytest tests/unit/ -v`
- Evals require live Pinecone + Anthropic — run separately from unit tests
