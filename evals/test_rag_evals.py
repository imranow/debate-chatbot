import os

import pytest
from deepeval.metrics import (
    AnswerRelevancyMetric,
    ContextualRelevancyMetric,
    FaithfulnessMetric,
)
from deepeval.test_case import LLMTestCase

from backend.config import get_settings
from backend.rag.anthropic_client import make_anthropic
from backend.rag.pinecone_client import make_pinecone

from evals.eval_dataset import EVAL_QUESTIONS
from evals.judge import AnthropicJudge
from evals.target import run_rag_pipeline, target_label


# --- Shared fixtures ---


@pytest.fixture(scope="session")
def rag_clients():
    """Pinecone index and Anthropic client for the in-process target.

    Not built when EVAL_TARGET_URL is set: in HTTP mode the service under test
    owns those clients, and the suite needs no Pinecone credentials of its own.
    """
    if os.getenv("EVAL_TARGET_URL"):
        return None, None, None
    settings = get_settings()
    _pc, index = make_pinecone(settings)
    anthropic_client = make_anthropic(settings)
    return settings, index, anthropic_client


@pytest.fixture(scope="session")
def judge():
    return AnthropicJudge()


# --- Parametrized test ---


@pytest.mark.parametrize(
    "eval_case",
    EVAL_QUESTIONS,
    ids=[q["question"][:60] for q in EVAL_QUESTIONS],
)
def test_rag_eval(eval_case, rag_clients, judge, record_eval_result):
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

    # Measured explicitly rather than via assert_test so the scores can be
    # recorded and diffed across deployments, not just asserted against.
    scores = {}
    failures = []
    for metric in metrics:
        metric.measure(test_case)
        name = type(metric).__name__
        scores[name] = {
            "score": metric.score,
            "threshold": metric.threshold,
            "reason": metric.reason,
        }
        if metric.score is None or metric.score < metric.threshold:
            failures.append("%s scored %s, threshold %s" % (name, metric.score, metric.threshold))

    record_eval_result(
        {
            "target": target_label(),
            "question": question,
            "retrieved_chunks": len(retrieval_context),
            "answer_chars": len(actual_output),
            "metrics": scores,
        }
    )

    assert not failures, "; ".join(failures)
