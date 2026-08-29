"""Compare two running deployments question by question.

The DeepEval suite judges answer quality, which is the right tool for asking
"is this RAG system any good". It is the wrong tool for asking "did the
migration change anything", because the judge is an LLM and its scores move
by a few points between runs on identical inputs.

Retrieval, by contrast, is deterministic: the same question against the same
Pinecone index returns the same chunk IDs in the same order. So the sharp test
for a migration is whether the retrieved citation IDs are identical. If they
are, retrieval is provably unchanged and any difference in wording is just the
language model's sampling.

Usage:
    python -m evals.compare_deployments \
        --baseline  https://old-service.example \
        --candidate https://new-service.example \
        --out evals/parity.json

Note on the answer cache: backend/rag/rag.py holds a per-process LRU cache
keyed on (question, top_k). Asking one deployment the same question twice
measures the cache, not the pipeline, so this script asks each question once
per deployment. The two deployments have independent caches, which is what
makes the comparison meaningful.

Neither URL needs credentials from this script: each service uses its own
configured keys. Set API_KEY if the services require the X-API-Key header.
"""

import argparse
import json
import os
import statistics
import time
import urllib.request
from typing import Any, Dict, List, Optional

from evals.eval_dataset import EVAL_QUESTIONS


def ask(base_url: str, question: str, timeout: float = 180.0) -> Dict[str, Any]:
    headers = {"content-type": "application/json"}
    api_key = os.getenv("API_KEY")
    if api_key:
        headers["X-API-Key"] = api_key

    req = urllib.request.Request(
        base_url.rstrip("/") + "/chat",
        data=json.dumps({"question": question}).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    started = time.time()
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        body = json.loads(resp.read().decode("utf-8"))
    elapsed = time.time() - started

    citations = body.get("citations") or []
    return {
        "latency_s": round(elapsed, 3),
        "citation_ids": [c.get("id") for c in citations],
        "citation_scores": [c.get("score") for c in citations],
        "answer": body.get("answer", ""),
        "sources_metadata": body.get("sources_metadata"),
    }


def compare(baseline_url: str, candidate_url: str) -> Dict[str, Any]:
    rows: List[Dict[str, Any]] = []

    for case in EVAL_QUESTIONS:
        question = case["question"]
        base = ask(baseline_url, question)
        cand = ask(candidate_url, question)

        base_ids = base["citation_ids"]
        cand_ids = cand["citation_ids"]
        overlap = len(set(base_ids) & set(cand_ids))
        denom = max(len(set(base_ids) | set(cand_ids)), 1)

        rows.append(
            {
                "question": question,
                "identical_order": base_ids == cand_ids,
                "identical_set": set(base_ids) == set(cand_ids),
                "jaccard": round(overlap / denom, 4),
                "baseline": base,
                "candidate": cand,
            }
        )
        status = "OK " if rows[-1]["identical_order"] else "DIFF"
        print(
            "%s  %-58s  baseline %5.2fs  candidate %5.2fs  jaccard %.2f"
            % (status, question[:58], base["latency_s"], cand["latency_s"], rows[-1]["jaccard"])
        )

    identical_order = sum(1 for r in rows if r["identical_order"])
    identical_set = sum(1 for r in rows if r["identical_set"])

    summary = {
        "questions": len(rows),
        "identical_citation_order": identical_order,
        "identical_citation_set": identical_set,
        "mean_jaccard": round(statistics.mean(r["jaccard"] for r in rows), 4),
        "baseline_median_latency_s": round(
            statistics.median(r["baseline"]["latency_s"] for r in rows), 3
        ),
        "candidate_median_latency_s": round(
            statistics.median(r["candidate"]["latency_s"] for r in rows), 3
        ),
        "baseline_url": baseline_url,
        "candidate_url": candidate_url,
    }
    return {"summary": summary, "rows": rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, help="URL of the existing deployment")
    parser.add_argument("--candidate", required=True, help="URL of the new deployment")
    parser.add_argument("--out", default="evals/parity.json", help="where to write the report")
    args = parser.parse_args()

    report = compare(args.baseline, args.candidate)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, sort_keys=True)

    s = report["summary"]
    print("\n%d/%d questions returned identical citations in identical order."
          % (s["identical_citation_order"], s["questions"]))
    print("%d/%d returned the same citation set (order aside)."
          % (s["identical_citation_set"], s["questions"]))
    print("Median latency: baseline %.2fs, candidate %.2fs"
          % (s["baseline_median_latency_s"], s["candidate_median_latency_s"]))
    print("Report written to %s" % args.out)

    return 0 if s["identical_citation_set"] == s["questions"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
