# From AI Application Engineer to Machine Learning Engineer

A personalized roadmap, grounded in an assessment of this repository (August 2026).

---

## Part 1 — Where You Are Today

This assessment is based on evidence in this codebase, not self-reporting.

### Demonstrated strengths

**Production Python (mid-level, genuinely solid).**
- Correct async engineering: `asyncio.gather` to run Pinecone (network I/O) and BM25
  (CPU) concurrently, `asyncio.to_thread` for CPU-bound work inside an async app
  (`backend/rag/retrieval.py`), lifespan-managed resources in FastAPI.
- Clean structure: dataclasses, type hints with `TYPE_CHECKING` imports, typed
  exceptions (`RetrievalError`, `LLMError`), Pydantic request/response contracts with
  field constraints.
- Defensive engineering: a three-stage retrieval fallback chain, a hand-rolled LRU
  cache with correct eviction order, per-source and total context budgets.

**Information-retrieval fundamentals.**
- You implemented Reciprocal Rank Fusion from the algorithm (not a library call),
  with a weighted alpha blend and sensible over-fetching (`fetch_k = 3 * top_k`).
- Score-ranked truncation so the best chunks survive the context budget, with
  metadata (`sources_excluded`, `chars_used`) surfaced through the API — that's
  observability thinking.

**Evaluation culture (rare at this stage, and a real differentiator).**
- A DeepEval harness with faithfulness / relevancy / contextual metrics, plus a
  custom `AnthropicJudge` implementing `DeepEvalBaseLLM` with structured-output
  handling. Most people building RAG apps never measure them.
- ~680 lines of unit tests covering RRF, truncation, BM25, the graph, and auth.

**Shipping.** Dockerized, health-checked, deployed to AWS ECS, with real-world
fixes in the history (retired model ID, CSV encoding detection in `ingest.py`).

### Honest gaps (relative to an ML engineer role)

1. **No trained models anywhere.** Every model in this system is someone else's,
   called over an API (Pinecone's embedder, Claude). An MLE's core loop —
   data → train → evaluate → deploy → monitor — doesn't appear in the repo.
   This is the single biggest gap.
2. **No deep-learning framework evidence.** No PyTorch, no training loops, no
   GPU work.
3. **No demonstrated ML/statistics foundations.** Nothing here shows (or
   disproves) comfort with linear algebra, probability, optimization,
   bias/variance, or proper cross-validation. Interviews will probe this hard.
4. **No MLOps tooling.** No CI/CD (no `.github/workflows`), no experiment
   tracking, no data versioning, no model registry, no drift monitoring. The
   BM25 index is an in-memory pickle; the eval dataset lives in a Python file.
5. **Scale.** One CSV, one process. No SQL/warehouse, pipeline, or
   distributed-data evidence.

### Verdict

You are operating as a **capable AI application engineer** — roughly a solid
junior-to-mid software engineer with strong LLM-application instincts and an
unusually good testing/eval habit. You are **not yet** an ML engineer, because
you haven't yet trained, evaluated, and shipped models of your own. The good
news: your gap is narrower than most career-changers' — you already have the
software engineering half, which is the half most ML learners lack. The plan
below fills the modeling half and deliberately reuses this repo as your lab.

---

## Part 2 — The Plan (~9 months at 10–15 hrs/week)

Each phase has a **learning track** and a **build track**. The build track is
where hiring signal comes from — never do a course without a project attached.
Compress the timeline if you can put in more hours; the order matters more than
the pace.

### Phase 0 — Setup and quick wins (Weeks 1–2)

- Add **GitHub Actions CI** to this repo: lint (ruff), typecheck (mypy), and
  `pytest tests/unit` on every PR. This closes an embarrassing gap cheaply and
  you'll extend this pipeline in Phase 4.
- Take a math self-diagnostic. Watch 3Blue1Brown's *Essence of Linear Algebra*
  and *Essence of Calculus*; if most of it feels familiar, your foundations are
  fine and Phase 1's math track is review, not study.
- Set up a Python ML environment: `uv` or conda, Jupyter, NumPy, pandas,
  scikit-learn, matplotlib.

### Phase 1 — ML foundations (Months 1–2)

**Learn:**
- Andrew Ng's *Machine Learning Specialization* (Coursera) **or** *An
  Introduction to Statistical Learning* (ISLR, free PDF + labs) — pick one,
  finish it. ISLR if you prefer reading and rigor; Ng if you prefer video.
- StatQuest (YouTube) for intuition on anything that doesn't click.
- Core concepts you must be able to explain on a whiteboard by the end:
  bias–variance tradeoff, regularization (L1/L2), cross-validation done
  correctly (no leakage), precision/recall/ROC-AUC and when each matters,
  gradient descent, feature scaling, tree ensembles vs. linear models.

**Build:**
- Two end-to-end tabular projects with scikit-learn (a Kaggle competition works
  well). The deliverable is not the leaderboard score — it's a notebook that
  shows a proper split strategy, an honest baseline, error analysis, and a
  written "what I'd try next."
- **Repo tie-in:** build a small query classifier for this chatbot (e.g.,
  "candidate-position question vs. factual-recall vs. out-of-scope") using
  TF-IDF + logistic regression. Label ~200 queries yourself. This teaches
  labeling pain, class imbalance, and evaluation on a problem you own.

### Phase 2 — Deep learning with PyTorch (Months 3–4)

**Learn:**
- Andrej Karpathy's *Neural Networks: Zero to Hero* — do every notebook by
  hand, including micrograd and makemore. This is the single highest-value
  resource for you: it builds training-loop fluency, which is exactly what you
  lack.
- Supplement with *Dive into Deep Learning* (d2l.ai) or fast.ai part 1 for
  breadth (CNNs, RNNs, attention).
- Learn to read a loss curve, diagnose over/underfitting, and use a GPU
  (Colab/Kaggle free tiers are enough; Lambda/RunPod when you need more).

**Build — the bridging project (this is the centerpiece of your portfolio):**
- **Fine-tune an embedding model on your debate data.** Generate synthetic
  (question, relevant-chunk) pairs with Claude, fine-tune a
  `sentence-transformers` model with contrastive loss, and swap it into this
  repo's retrieval path.
- **Train a cross-encoder reranker** and add it as a stage after RRF.
- Prove the lift with the eval harness you already built: retrieval
  recall@k and DeepEval metrics, before vs. after, in a results table in the
  README. "I fine-tuned a retriever and reranker and improved faithfulness by
  X% on my own eval set" is an interview story almost no AI-app engineer can
  tell.

### Phase 3 — NLP and LLM depth (Months 5–6)

**Learn:**
- Hugging Face ecosystem: `transformers`, `datasets`, `peft`, `trl`.
- Karpathy's *nanoGPT* / "Let's build GPT" video to understand transformer
  internals — you will be asked how attention works.
- Fine-tuning techniques: LoRA/QLoRA, when SFT vs. prompting vs. RAG is the
  right tool.

**Build (both directly close "Known Issues" in this repo):**
- **Replace the naive knowledge-graph entity matching** (substring, 3+ chars)
  with a real NER model — start with spaCy, then fine-tune a small transformer
  on debate-domain entities. Measure entity precision/recall against a
  hand-labeled sample.
- **Build the citation validator** the repo admits it lacks: an NLI-style
  classifier (start from a pretrained NLI model, fine-tune if needed) that
  checks whether each cited source actually supports the sentence citing it.
  Wire it into `/chat` as a post-hoc validation step with a confidence field.
- Optional stretch: QLoRA-fine-tune a small open model (e.g., Llama-class 8B)
  on debate-style Q&A and compare it honestly against the Claude pipeline on
  cost, latency, and eval scores.

### Phase 4 — MLOps and ML systems (Months 7–8)

**Learn:**
- *Designing Machine Learning Systems* (Chip Huyen) — read it cover to cover;
  it is the interview canon for ML system design.
- Experiment tracking (Weights & Biases or MLflow), data versioning (DVC),
  model registries, serving (ONNX export, TorchServe, or vLLM for LLMs),
  monitoring and drift detection (Evidently).
- SQL to a solid intermediate level if you're not there already.

**Build — MLOps-ify this repo:**
- Every training script from Phases 2–3 gets experiment tracking and a
  versioned dataset.
- CI gains an **eval gate**: PRs that touch retrieval or prompts must run the
  offline eval suite and fail on metric regression. (You already have the
  harness — automating it is the MLOps skill.)
- Add query/response logging and latency percentiles (another admitted gap),
  then a simple drift check on incoming query distributions.
- Serve the Phase 2 reranker as its own containerized service with batching,
  and load-test it. Deploy to the ECS setup you already have.

### Phase 5 — Specialization and job search (Month 9+)

- Your natural lane is **LLM/applied-NLP ML engineering** — retrieval,
  fine-tuning, evaluation. It builds directly on everything above and demand
  is strong. Keep classical ML sharp for interviews, but market yourself here.
- Interview prep, in order of weight for MLE roles: (1) ML fundamentals
  (Phase 1 whiteboard list), (2) ML system design ("design a
  search/recommendation/RAG system" — you'll have literally built one),
  (3) coding (LeetCode mediums; your Python is already fine), (4) deep
  dives on your projects — know every number in your results tables.
- Write 2–3 technical blog posts from the build tracks (the
  embedding-fine-tuning one especially). Posts convert projects into inbound
  interest and prove communication skill.
- Target roles: "ML Engineer (NLP/LLM)", "Applied Scientist (engineering-
  leaning)", "AI Engineer" at companies where it means training models, not
  just calling them.

---

## Part 3 — Portfolio checklist (what "done" looks like)

By the end you should be able to point to:

- [ ] This repo, upgraded: fine-tuned retriever + trained reranker + NER-based
      graph + citation validator, each with before/after eval numbers
- [ ] CI with an automated eval gate; experiment tracking on every model
- [ ] Two clean classical-ML projects with honest error analysis
- [ ] One from-scratch training artifact (Karpathy notebooks / nanoGPT run)
- [ ] One fine-tuned open LLM with a cost/latency/quality comparison
- [ ] 2–3 blog posts; README results tables everywhere
- [ ] Fluent answers to the Phase 1 whiteboard list and one rehearsed
      ML-system-design walkthrough (use this system)

## Weekly cadence that works at 10–15 hrs/week

- 2 sessions × 2h: course/book (learn track)
- 2 sessions × 2–3h: project (build track)
- 1 session × 1h: review — write down what you learned; this becomes blog material
- Never let the learn track run more than a week ahead of the build track.

---

*Principle behind the whole plan: you already know how to ship software. Every
phase therefore converts "consume ML content" into "ship an ML artifact into a
system you run" as fast as possible — because trained-and-shipped models are
the only credential that separates an MLE from an AI-app engineer.*
