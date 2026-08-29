# Follow-ups

Work found during the Cloud Run migration and deliberately not done as part of
it. Mixing infrastructure and behaviour changes makes a regression impossible
to attribute, so these are written down rather than folded in.

Ordered by what they cost you if left alone.

---

## 1. BM25 is not running in production

**Status:** live defect. The deployed service has never done hybrid retrieval.

### What happens

`Settings.bm25_index_path` defaults to `data/bm25_index.pkl`. The Dockerfile
copies `backend`, `scripts` and `README.md`, and no `data/` directory exists in
the repository. The transcript CSV is excluded by both `.gitignore` and
`.dockerignore`. So in the lifespan handler:

```python
if os.path.exists(settings.bm25_index_path):      # false, no pickle in image
    ...
elif os.path.exists(settings.csv_path):           # false, CSV excluded
    ...
except Exception as e:
    logger.warning("BM25 index not available: %s", e)
```

Neither branch fires. `bm25_index` stays `None`, and `hybrid_search` takes its
early return:

```python
if bm25_index is None:
    return (await search_pinecone_records(index, settings, question, fetch_k))[:top_k]
```

Dense-only retrieval, no RRF, no keyword matching, and nothing louder than a
warning in the logs to say so.

### Why it matters beyond the code

`CLAUDE.md`, the README architecture section and the CV all describe hybrid
BM25 plus Pinecone merged via Reciprocal Rank Fusion. The code implements that
correctly and 60 unit tests cover it. It has simply never had an index to run
against in a container. That is a gap between what the project claims and what
it does, which is worth closing before an interview rather than during one.

The practical loss is keyword recall. Dense retrieval on `multilingual-e5-large`
handles paraphrase well and exact terms poorly. Questions turning on a specific
name, figure or phrase ("stop and frisk", "$15 minimum wage", "2 cents") are
exactly where BM25 earns its place, and exactly what people ask a debate
transcript bot.

### One thing that is already correct

The document IDs line up. `scripts/ingest.py` and `backend/rag/bm25_index.py`
both number rows with an identical increment-then-skip loop:

```python
row_id = 0
for row in reader:
    row_id += 1
    speech = (row.get("speech") or "").strip()
    if not speech:
        continue
    ...  "_id": "row-%d" % row_id
```

So `row-N` means the same chunk in Pinecone and in BM25, and RRF will merge and
deduplicate correctly rather than silently fusing two different ID spaces. This
was worth checking, because if the numbering had diverged the fix would have
made retrieval worse while appearing to work.

Both files carry their own copy of `_open_csv_with_guess`. That duplication is
what guarantees the alignment today and what would quietly break it tomorrow.
Worth extracting to one place as part of this fix.

### Measure before choosing an approach

The right packaging depends on three numbers nobody has yet:

```bash
python scripts/build_bm25.py            # prints document count, build time, pickle size
python - <<'PY'
import time
from backend.rag.bm25_index import BM25Index
t = time.time(); ix = BM25Index.load("data/bm25_index.pkl")
print("load: %.2fs, %d docs" % (time.time() - t, ix.num_documents))
PY
```

Then:

| Pickle size | Load time | Approach |
|---|---|---|
| under ~25 MB | under ~1s | Commit the artifact, `COPY data/ /app/data/`. Simplest thing that works. |
| 25 to 200 MB | 1 to 3s | Build it in a Docker builder stage from a committed CSV, copy only the artifact into the final image. Keeps git history clean. |
| over 200 MB | over 3s | Lazy-load on first `/chat` rather than in the lifespan handler, so cold starts stay fast and the first query pays once. |

Do not rebuild from CSV in the lifespan handler. That puts the whole corpus
tokenisation on the critical path of every cold start, which is precisely the
thing `min-instances 0` makes expensive.

### A note on pickle

`BM25Index.load` calls `pickle.load` on a file. That is fine for an artifact you
built and baked into your own image, and not fine if the path ever becomes
configurable from outside. It is also brittle: the pickle embeds the class and
will break across `rank_bm25` or Python version bumps, failing at startup with
a warning that currently gets swallowed. If this is being touched anyway,
serialising the token lists and metadata as JSON or npz and reconstructing
`BM25Okapi` at load is a small amount of work for a meaningful gain in
robustness.

### Verification

The parity harness already built for the migration is the right tool. Run the
evaluation set against dense-only and hybrid deployments, and expect the
citation IDs to differ. That difference is the point. Compare judged scores
with `EVAL_TARGET_URL` to confirm the change is an improvement rather than
merely a change.

Also worth fixing while in there: make the BM25 loading failure loud. A demo
that silently degrades from hybrid to dense is how this went unnoticed for six
months. If `ENABLE_BM25` is set and the index cannot be loaded, the service
should refuse to start rather than quietly serve worse answers.

---

## 2. The answer cache does not survive scale to zero

**Status:** accepted trade, not a defect. Documented so it is a choice rather
than a surprise.

### What happens

`backend/rag/rag.py` holds a module-level LRU keyed on `(question, top_k)`,
capped at 256 entries. It is per-process and in memory.

On ECS a single task ran continuously, so the cache filled and stayed warm
indefinitely. Measured against the live ECS service: a fresh question took
8.6s, the same question immediately after took 0.2s.

On Cloud Run at `min-instances 0` the process is torn down when traffic stops,
and the cache goes with it. It is also not shared between the up-to-three
instances. So a repeat question after an idle period costs a cold start plus a
full pipeline run.

### Why this was left alone

The cache was mostly serving the same visitor within one session, which still
works: instances live for minutes after a request, so a follow-up question from
the same person still hits a warm process. What is lost is the cross-visitor,
cross-day case, which for a demo answering open-ended questions was rare
anyway.

Solving it properly means paying for an always-warm instance, which is the
thing this migration existed to stop.

### If it is worth revisiting

Ranked by effort against benefit.

**Anthropic prompt caching.** Costs nothing to try and helps a different part
of the problem: the system prompt and retrieved sources are large and stable
within a conversation. This reduces token spend and time-to-first-token on the
generation step without touching the retrieval path or the deployment. Start
here.

**Firestore-backed cache.** Key on a hash of `(question, top_k)` and store the
answer and citations. Free tier covers 50,000 reads and 20,000 writes a day,
which this service will not approach. Survives scale to zero and is shared
across instances. Adds a network round trip on the read path, so it only pays
off if hit rates are genuinely non-trivial, which is worth measuring before
building.

**Do not use Memorystore.** Redis on GCP has an hourly instance charge with no
scale to zero, so it reintroduces exactly the always-on baseline cost that this
migration removed. It would be a more expensive version of the problem.

### Worth measuring first

There is currently no logging of cache hits or misses, so the hit rate is
unknown and any work here would be speculative. `CLAUDE.md` already lists "no
query/response logging or latency tracking" as tech debt. Counting hits and
misses is a few lines and turns this from a guess into a decision.

---

## 3. `/chat` is open to the internet

**Status:** pre-existing, unchanged by the migration, worth a decision.

`API_KEY` is unset in both deployments, so `require_api_key` logs a warning and
waves every request through. Anyone who finds the URL can spend your Anthropic
and Pinecone quota, and the demo URL is on a public portfolio.

`--max-instances 3` bounds compute cost. It does nothing about token spend,
which is the part that actually costs money here.

This is a genuine tension: the demo has to be usable by a recruiter who clicks
a link, so an API key in a header is not an option. Realistic mitigations are
rate limiting by IP, a small per-day request budget enforced in the app, or
accepting the risk on the grounds that the URL is not interesting enough to
attack. The Anthropic account's own spend limit is the real backstop and is
worth confirming is set.

---

## 4. Log retention is unset

Every CloudWatch log group in the AWS account is set to "Never expire",
including two orphaned from services that no longer exist. It costs nothing
today because the volume sits inside the 5 GB free tier, and it will keep
costing nothing at this rate. Listed for completeness rather than urgency, and
covered in `deploy/aws-teardown.md`.

Cloud Logging has its own 30-day default retention, so this does not carry over
to the new deployment.
