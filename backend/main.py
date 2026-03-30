import logging
import os
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any, Dict, List, Optional

from fastapi import Depends, FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field

from backend.config import Settings, get_settings
from backend.rag.anthropic_client import make_anthropic
from backend.rag.auth import require_api_key
from backend.rag.exceptions import LLMError, RetrievalError
from backend.rag.pinecone_client import make_pinecone
from backend.rag.rag import answer_question

logger = logging.getLogger(__name__)


class ChatRequest(BaseModel):
    question: str = Field(..., min_length=1, max_length=4000)
    top_k: Optional[int] = Field(None, ge=1, le=50)


class Citation(BaseModel):
    id: str
    score: float
    date: Optional[str] = None
    debate_name: Optional[str] = None
    debate_section: Optional[str] = None
    speaker: Optional[str] = None
    text: str


class SourcesMeta(BaseModel):
    total_sources: int
    included_sources: int
    excluded_sources: int
    chars_used: int
    chars_budget: int


class ChatResponse(BaseModel):
    answer: str
    citations: List[Citation]
    sources_metadata: Optional[SourcesMeta] = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    _pc, index = make_pinecone(settings)
    anthropic_client = make_anthropic(settings)

    # Load BM25 index (pickle or build from CSV)
    bm25_index = None
    try:
        if os.path.exists(settings.bm25_index_path):
            from backend.rag.bm25_index import BM25Index
            bm25_index = BM25Index.load(settings.bm25_index_path)
            logger.info("Loaded BM25 index (%d docs)", bm25_index.num_documents)
        elif os.path.exists(settings.csv_path):
            from backend.rag.bm25_index import BM25Index
            bm25_index = BM25Index.from_csv(settings.csv_path)
            logger.info("Built BM25 index from CSV (%d docs)", bm25_index.num_documents)
            bm25_index.save(settings.bm25_index_path)
            logger.info("Saved BM25 index to %s", settings.bm25_index_path)
    except Exception as e:
        logger.warning("BM25 index not available: %s", e)

    # Load knowledge graph
    knowledge_graph = None
    if settings.enable_knowledge_graph:
        try:
            if os.path.exists(settings.knowledge_graph_path):
                from backend.rag.knowledge_graph import KnowledgeGraph
                knowledge_graph = KnowledgeGraph.load(settings.knowledge_graph_path)
                logger.info("Loaded knowledge graph (%d nodes, %d edges)",
                            knowledge_graph.num_nodes, knowledge_graph.num_edges)
        except Exception as e:
            logger.warning("Knowledge graph not available: %s", e)

    app.state.settings = settings
    app.state.index = index
    app.state.anthropic_client = anthropic_client
    app.state.bm25_index = bm25_index
    app.state.knowledge_graph = knowledge_graph
    yield


app = FastAPI(title="Debate Chatbot", lifespan=lifespan)

WEB_DIR = Path(__file__).resolve().parent / "web"
INDEX_HTML = WEB_DIR / "index.html"
app.mount("/static", StaticFiles(directory=str(WEB_DIR)), name="static")


@app.get("/")
def index() -> FileResponse:
    return FileResponse(str(INDEX_HTML))


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.post("/chat", response_model=ChatResponse, dependencies=[Depends(require_api_key)])
async def chat(req: ChatRequest) -> Dict[str, Any]:
    try:
        settings: Settings = app.state.settings
        answer, citations, sources_metadata = await answer_question(
            index=app.state.index,
            anthropic_client=app.state.anthropic_client,
            settings=settings,
            question=req.question,
            top_k=req.top_k,
            bm25_index=app.state.bm25_index,
            knowledge_graph=app.state.knowledge_graph,
        )
        return {
            "answer": answer,
            "citations": citations,
            "sources_metadata": {
                "total_sources": sources_metadata.total_sources,
                "included_sources": sources_metadata.included_sources,
                "excluded_sources": sources_metadata.excluded_sources,
                "chars_used": sources_metadata.chars_used,
                "chars_budget": sources_metadata.chars_budget,
            },
        }
    except RetrievalError:
        raise HTTPException(
            status_code=502,
            detail="Unable to retrieve relevant sources. Please try again later.",
        )
    except LLMError:
        raise HTTPException(
            status_code=502,
            detail="Language model is temporarily unavailable. Please try again later.",
        )
    except HTTPException:
        raise
    except Exception:
        logger.exception("Unexpected error in /chat")
        raise HTTPException(
            status_code=500,
            detail="An unexpected error occurred. Please try again later.",
        )
