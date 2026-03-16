import pytest
from deepeval import assert_test
from deepeval.metrics import (
    AnswerRelevancyMetric,
    ContextualRelevancyMetric,
    FaithfulnessMetric,
)
from deepeval.test_case import LLMTestCase

from backend.config import get_settings
from backend.rag.anthropic_client import make_anthropic
from backend.rag.pinecone_client import make_pinecone
from backend.rag.rag import answer_question

from evals.eval_dataset import EVAL_QUESTIONS
from evals.judge import AnthropicJudge


# --- Shared fixtures ---


@pytest.fixture(scope="session")
def rag_clients():
    """Initialize Pinecone index and Anthropic client once per test session."""
    settings = get_settings()
    _pc, index = make_pinecone(settings)
    anthropic_client = make_anthropic(settings)
    return settings, index, anthropic_client


@pytest.fixture(scope="session")
def judge():
    return AnthropicJudge()


# --- Helper ---


def run_rag_pipeline(question, settings, index, anthropic_client):
    """Call the live RAG pipeline. Returns (answer, retrieval_context_list)."""
    answer, citations = answer_question(
        index=index,
        anthropic_client=anthropic_client,
        settings=settings,
        question=question,
    )
    retrieval_context = [c["text"] for c in citations if c.get("text")]
    return answer, retrieval_context


# --- Parametrized test ---


@pytest.mark.parametrize(
    "eval_case",
    EVAL_QUESTIONS,
    ids=[q["question"][:60] for q in EVAL_QUESTIONS],
)
def test_rag_eval(eval_case, rag_clients, judge):
    settings, index, anthropic_client = rag_clients

    question = eval_case["question"]
    expected_answer = eval_case.get("expected_answer")

    actual_output, retrieval_context = run_rag_pipeline(
        question, settings, index, anthropic_client
    )

    test_case = LLMTestCase(
        input=question,
        actual_output=actual_output,
        retrieval_context=retrieval_context,
        expected_output=expected_answer,
    )

    metrics = [
        FaithfulnessMetric(threshold=0.7, model=judge),
        AnswerRelevancyMetric(threshold=0.7, model=judge),
        ContextualRelevancyMetric(threshold=0.5, model=judge),
    ]

    assert_test(test_case, metrics)
