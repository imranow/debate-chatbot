import json
import os
import pathlib
import threading

import pytest
from dotenv import load_dotenv

# Ensure .env is loaded before any backend imports.
# override=True is needed in case empty env vars shadow .env values.
load_dotenv(override=True)


_results = []
_lock = threading.Lock()


@pytest.fixture(scope="session")
def record_eval_result():
    def _record(row):
        with _lock:
            _results.append(row)

    return _record


@pytest.fixture(scope="session", autouse=True)
def write_eval_report():
    """Write every measured score to JSON so runs can be diffed.

    Path is overridable with EVAL_REPORT_PATH so an ECS baseline and a Cloud
    Run run land in separate files.
    """
    yield
    if not _results:
        return
    out = pathlib.Path(os.getenv("EVAL_REPORT_PATH", "evals/results.json"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(_results, indent=2, sort_keys=True))
    print("\nEval scores written to %s (%d cases)" % (out, len(_results)))
