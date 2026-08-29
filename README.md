# Debate Chatbot (RAG)

Link: https://de-fafa3ceb88a24b38b241702b67d9b091.ecs.us-east-1.on.aws/

Grounded Q&A over the 2019-2020 U.S. Democratic primary debate transcripts using:

- **FastAPI** for the API + a minimal web UI
- **Pinecone** as the vector database (integrated embeddings index)
- **Anthropic (Claude)** for answer generation

The app retrieves relevant transcript snippets at query time and asks Claude to answer **using only the retrieved sources**, returning citations.

## Features

- Web chat UI at `/`
- API endpoint at `POST /chat`
- Source citations included in responses
- One-command ingestion into Pinecone (`scripts/ingest.py`)

## Architecture

1. **Ingest** transcripts into Pinecone as “records” with metadata (speaker/date/debate info).
2. At query time: **embed question** → **retrieve top_k** relevant records from Pinecone.
3. Inject retrieved sources into a prompt and ask **Claude** to answer with citations.

## Requirements

- Python 3.9+ (local dev)
- A Pinecone account + API key
- An Anthropic API key

## Quickstart (Local)

1. Install dependencies:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

2. Configure environment variables:

```bash
cp .env.example .env
```

Edit `.env` and set at least:

- `PINECONE_API_KEY`
- `ANTHROPIC_API_KEY`

3. Add the dataset:

This repo intentionally does **not** commit the transcript CSV. Place it at:

- `debate_transcripts_v3_2020-02-26.csv`

4. Ingest into Pinecone (creates the index if missing):

```bash
python3 scripts/ingest.py
```

5. Run the API:

```bash
uvicorn backend.main:app --reload --host 127.0.0.1 --port 8001
```

Open:

- Web UI: `http://127.0.0.1:8001/`
- Health: `http://127.0.0.1:8001/health`

## API

### `GET /health`

Returns:

```json
{ "status": "ok" }
```

### `POST /chat`

Request body:

```json
{
  "question": "What did candidates say about Medicare for All?",
  "top_k": 8
}
```

Response:

- `answer`: Markdown-formatted answer with citations like `[1]`
- `citations`: list of the retrieved transcript snippets (speaker/date/debate metadata + excerpt)

Example:

```bash
curl -sS http://127.0.0.1:8001/chat \
  -H 'content-type: application/json' \
  -d '{"question":"What did Bernie Sanders say about billionaires?","top_k":6}'
```

## Configuration (Environment Variables)

Minimum:

- `PINECONE_API_KEY`
- `ANTHROPIC_API_KEY`

Common:

- `PINECONE_INDEX_NAME` (default: `dem-debates-transcripts`)
- `PINECONE_NAMESPACE` (default: `debates`)
- `PINECONE_INDEX_HOST` (recommended if you already know it; avoids a control-plane lookup at startup)
- `PINECONE_EMBED_MODEL` (default: `multilingual-e5-large`)
- `PINECONE_EMBED_FIELD` (default: `chunk_text`)
- `ANTHROPIC_MODEL` (default: `claude-sonnet-4-6`)
- `TOP_K` (default: `8`)
- `MAX_CONTEXT_CHARS` (default: `12000`)

Notes:

- `PINECONE_EMBED_MODEL` only matters when **creating** a new integrated-embeddings index.
- If you change embedding models, create a new index name (or delete and recreate the existing index).

## Project Layout

- `backend/main.py`: FastAPI app (`/`, `/health`, `/chat`)
- `backend/rag/`: retrieval + prompting + Anthropic client
- `backend/web/`: static web UI (HTML/CSS/JS)
- `scripts/ingest.py`: ingest CSV into Pinecone as records

## Migration: AWS ECS to Google Cloud Run

The service ran on AWS ECS Express Mode from February 2026. It moved to Cloud
Run in August 2026. This section records why, what had to change, and what the
move cost in latency.

### Why it moved

The bill, not the technology. Two months of AWS charges, pre-tax USD:

| Line item | July | August (projected) | What it is |
|---|---:|---:|---|
| ECS Fargate (1 vCPU, 2 GB) | 36.73 | 35.31 | the container |
| VPC public IPv4 addresses | 26.06 | 25.05 | scaffolding |
| Application Load Balancer | 16.75 | 16.10 | scaffolding |
| App Runner (retired mid-July) | 2.59 | 0.00 | previous deployment |
| ECR image storage | 0.09 | 0.08 | images |
| CloudWatch, data transfer | 0.00 | 0.00 | inside free tier |
| **Total pre-tax** | **82.22** | **76.54** | |

The interesting split is not AWS against GCP. It is compute against
scaffolding. Only 46% of the August bill was the container. The other 54% was
the cost of being reachable:

```
Amazon Virtual Private Cloud Public IPv4 Addresses
  $0.005 per In-use public IPv4 address per hour   4,685.662 Hrs   USD 23.43
```

4,686 address-hours across 29 days is 6.7 addresses held continuously, against
one cluster, one service, one running task. ECS Express Mode places an
internet-facing load balancer in every availability zone in the region, and
us-east-1 has six. Six ALB nodes, each holding a public IP, plus the task
network interface. Nobody chose that; it is what the managed abstraction does
on your behalf.

So the service was paying roughly 25 dollars a month in address rent and a
further 16 in load balancer hours, of which one cent was actual traffic
(0.798 LCU-hours across the whole month). A demo that is hit a handful of
times a week was buying availability infrastructure sized for continuous
production load.

There is no NAT Gateway in this account, which is the usual suspect for a VPC
line item of that size. It really was just addresses.

Cloud Run does not shrink the scaffolding cost. It removes the category.
Ingress, TLS termination and routing are bundled into the per-request price,
and at this traffic level the per-request price sits inside the free tier
(2 million requests, 180,000 vCPU-seconds and 360,000 GiB-seconds per month).
There is no address to rent when nothing is running.

**Cost before: about 77 USD per month pre-tax, roughly 92 with tax.
Cost after: 0.**

Anthropic and Pinecone spend is unaffected by the move. Those bills follow
usage, not hosting.

### What had to change in the container

Three things, none of which touched application behaviour.

**The PORT contract.** Cloud Run injects a `PORT` environment variable and
expects the container to listen on it. The entrypoint already read `${PORT}`,
but with no default, so the image depended on the platform setting it. Now
`${PORT:-8080}`, which also makes a bare `docker run` work.

**Signal handling.** The entrypoint was `sh -c "uvicorn ..."`, which leaves the
shell as PID 1. The shell swallows `SIGTERM`, so the container would ignore the
shutdown signal and wait out the platform kill timeout on every scale to zero.
Now `sh -c "exec uvicorn ..."`, so uvicorn is PID 1 and exits promptly. This
never mattered on ECS because the task never stopped. Scale to zero is what
turns a latent bug into a real one.

**The amd64 build.** Cloud Run runs x86-64, and building on Apple Silicon
without `--platform linux/amd64` produces an image that fails at runtime with
an exec format error. Rather than remembering the flag, the build moved to
Cloud Build, which builds on x86-64 by definition and in the same region as
the registry and the service. The problem is removed rather than worked
around.

**Image size.** `deepeval` was in `requirements.txt`, so an evaluation
dependency was shipping in the production image, and dragging in the OpenAI
SDK, posthog telemetry, pytest, rich, typer and pyfiglet with it. Splitting it
into `requirements-dev.txt` took site-packages from 302 MB to 184 MB, measured.
No runtime code path ever imported any of it.

### Runtime configuration

Every setting is passed explicitly in `deploy/deploy.sh`. The defaults are what
turn a portfolio demo into a surprise invoice.

`--min-instances 0` is the entire point: nothing runs when nobody is asking.
`--max-instances 3` bounds the worst case, because a public endpoint with no
ceiling is an open invitation.

`--memory 512Mi` is measured rather than guessed. Embeddings are computed by
Pinecone through its integrated-embeddings index, not by a local
sentence-transformer, so there is no model to load and no reason to reserve a
gigabyte for one. The largest in-process structure is the answer cache at
roughly 2.5 MB.

`--concurrency 20` because the app is genuinely async and IO-bound: it spends
its time waiting on Pinecone and Anthropic. More requests per instance means
fewer instances and fewer billed vCPU-seconds. The ceiling worth knowing is
anyio's default 40-thread pool, which the Pinecone calls borrow through
`asyncio.to_thread`. Twenty leaves headroom under it.

`--cpu-throttling` because there is no background work to fund. There are no
asyncio loops, no scheduled tasks and no websockets, so nothing needs CPU
between requests.

`--timeout 120` against a worst observed end-to-end latency of 10.3s on ECS.
Generous, while still capping how long a hung request can hold a billed
instance. The platform default of 300s is looser than this service needs.

### Cold start, and the trade that was accepted

Startup work is close to nothing. Timed from process start to the first 200 on
`/health` with the production dependency set: 0.88 to 1.18s across five runs
with a warm page cache, and 4.40s on the first run after a fresh checkout with
nothing cached.

The cold figure is the honest one for Cloud Run. Every cold start there begins
with freshly pulled layers and an empty page cache, so 4s is the number to
expect and 1s is the number you get once an instance is warm. Measuring only
the warm case is how a cold start estimate ends up three or four times too
optimistic.
There is no embedding model to load, and the BM25 index is absent from the
image (see Known limitations), so the lifespan handler does almost no work.
`PINECONE_INDEX_HOST` is set in the deployment, which keeps the Pinecone client
from making a control-plane lookup on the startup path.

<!-- FILL IN AFTER CUTOVER -->
Measured Cloud Run cold start, first request after 20 minutes idle: TBD
Measured warm request latency: TBD
Median latency comparison against the ECS baseline: TBD, see evals/parity.json

**The real trade is not cold start. It is the answer cache.**

`backend/rag/rag.py` holds a per-process LRU cache keyed on
`(question, top_k)`. On ECS one task ran forever, so the cache filled and
stayed warm indefinitely: a repeat question returned in 0.2s against 8 to 10
seconds for a fresh one. On Cloud Run at `min-instances 0` the process dies
whenever traffic stops, and the cache dies with it. It is also not shared
across instances.

So a repeat question that used to cost 0.2s now costs a cold start plus a full
pipeline run. Scale to zero and an in-memory cache are the same trade made
twice, and the second one is easy to miss because nothing in the container
configuration mentions it.

That was accepted rather than solved. For a demo that is hit occasionally by
different people asking different questions, the cache was rarely being hit by
anyone but the same visitor anyway, and the alternative is paying for an
always-warm instance, which is the thing this migration existed to stop.

### Verifying that retrieval did not change

An LLM judge moves by a few points between runs on identical input, so a small
DeepEval score movement proves nothing either way. Retrieval does not move:
the same question against the same Pinecone index returns the same chunk IDs
with the same scores.

`evals/compare_deployments.py` sends the evaluation set to both deployments and
compares retrieved citation IDs. Identical IDs in identical order means
retrieval is provably unchanged, and any difference in wording is the language
model sampling at temperature 0.2.

### Known limitations found during the migration

Neither was introduced by the move, and neither was fixed during it, on the
principle that mixing infrastructure and behaviour changes makes a regression
impossible to attribute.

**BM25 is not running in production.** `bm25_index_path` defaults to
`data/bm25_index.pkl`. The Dockerfile does not copy a `data/` directory, and
the transcript CSV is excluded by both `.gitignore` and `.dockerignore`. So
neither branch of the loader in the lifespan handler fires, `bm25_index` stays
`None`, the failure is swallowed as a warning, and `hybrid_search` silently
returns dense-only results. The hybrid retrieval and RRF code is correct and
tested; it has simply never had an index to work with in a deployed container.

**The eval suite could not run.** `evals/test_rag_evals.py` called the async
`answer_question` without awaiting it and then unpacked the coroutine, so it
failed on the first case with a `TypeError`. It had therefore never produced a
score, and there was no historical baseline to migrate against. It also called
the pipeline in-process rather than over HTTP, which made it blind to the
deployment: it would have returned the same result whichever service was live.
Both are fixed, and `EVAL_TARGET_URL` now switches it to run against a running
service.

## Deploy to Google Cloud Run

Four scripts in `deploy/`, run in order. See `deploy/README.md` for the detail.

```bash
export PROJECT_ID=your-project-id
export REGION=europe-west1

./deploy/setup-gcp.sh        # APIs, Artifact Registry, runtime service account
./deploy/create-secrets.sh   # prompts for the two API keys, never echoes them
./deploy/deploy.sh           # Cloud Build, then deploy with explicit runtime config
./deploy/set-budget.sh       # GBP 5 budget alert
```

`deploy/aws-teardown.md` lists every AWS resource with its cost and whether it
should be deleted or kept.

## Deploy To AWS (ECS Express Mode, superseded)

> Kept deliberately. The service no longer runs here, but these are the working
> instructions for the deployment it ran on from February to August 2026, and
> the notes below on the IAM role that the CLI cannot create are the kind of
> thing that is painful to rediscover. The ECS task definitions are also still
> in the AWS account for the same reason.


The live deployment runs on [Amazon ECS Express Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/express-service-overview.html),
which turns a single container image into a Fargate service with an Application Load
Balancer (HTTPS), auto-scaling, and a public `*.ecs.<region>.on.aws` URL. The repo's
`Dockerfile` runs `uvicorn` on `0.0.0.0:$PORT` (default `8080`).

> **Keep everything in one region.** Build/push the image **and** create the service in
> the same region (this project uses `us-east-1`). A service in one region can't pull an
> image from another without extra cross-region setup.

### 1) Build & push the image to ECR

```bash
REGION=us-east-1
REPO=debate-chatbot

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGISTRY="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
aws ecr create-repository --repository-name "$REPO" --region "$REGION" 2>/dev/null || true
aws ecr get-login-password --region "$REGION" | docker login --username AWS --password-stdin "$REGISTRY"

# Run from the repo root (where the Dockerfile is). --platform matters on Apple Silicon.
docker buildx build --platform linux/amd64 -t "${REGISTRY}/${REPO}:latest" --push .
```

### 2) Create the service (first time: use the Console)

The CLI (`aws ecs create-express-gateway-service`) needs an
`ecsInfrastructureRoleForExpressServices` IAM role that does **not** exist on a fresh
account — calling it first returns `Cannot assume role`. The **ECS Console → Create →
Express** flow creates that role for you, so use the Console for the first service:

- **Container image:** the ECR URI from step 1 (`…/debate-chatbot:latest`)
- **Port:** `8080`
- **Health check path:** `/health`
- **Environment variables:**
  - `PINECONE_API_KEY`, `PINECONE_INDEX_HOST`, `PINECONE_INDEX_NAME`, `PINECONE_NAMESPACE`
  - `ANTHROPIC_API_KEY`
  - `ANTHROPIC_MODEL` — **optional**. The image already defaults to `claude-sonnet-4-6`,
    so leaving this unset avoids a hand-typed value. If you do set it, use the **exact**
    hyphenated ID `claude-sonnet-4-6`. A typo (`claude_sonnet_4-6`) or a retired ID makes
    Anthropic return 404, and every `/chat` request then fails with a 502
    (`"Language model is temporarily unavailable"`).

Once that first service (and its IAM role) exists, later deploys can use the CLI.

### 3) Redeploy / update env vars (CLI)

Put the container config in a file to avoid shell-quoting issues, then update by service ARN:

```bash
cat > container.json <<'JSON'
{
  "image": "<ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/debate-chatbot:latest",
  "containerPort": 8080,
  "environment": [
    {"name": "ANTHROPIC_API_KEY", "value": "<key>"},
    {"name": "PINECONE_API_KEY", "value": "<key>"},
    {"name": "PINECONE_INDEX_HOST", "value": "<host>"},
    {"name": "PINECONE_INDEX_NAME", "value": "dem-debates-transcripts"},
    {"name": "PINECONE_NAMESPACE", "value": "debates"}
  ]
}
JSON

aws ecs update-express-gateway-service \
  --region us-east-1 \
  --service-arn <your-service-arn> \
  --primary-container file://container.json
```

Updating the container triggers a new deployment. Watch it roll out, then verify:

```bash
# wait until one deployment shows rollout COMPLETED, running == desired, none IN_PROGRESS
aws ecs describe-services --cluster default --services <service-name> --region us-east-1 \
  --query "services[0].deployments[].{rollout:rolloutState,running:runningCount,desired:desiredCount}"

curl -s -X POST "https://<your-service-url>/chat" \
  -H 'content-type: application/json' \
  -d '{"question":"What did candidates say about healthcare?"}'
```

A JSON `answer` with `[n]` citations means it's live. Per-request errors that don't crash
the container are logged to CloudWatch (`/aws/ecs/default/<service>`); the app also returns
a specific `detail` (retrieval vs. language-model failure) in the 502 body.

## Security / Cost Notes

- Do **not** commit API keys. If you pasted a key into chat or a public place, rotate it.
- Set keys as service environment variables (or AWS Secrets Manager), never in the image.
- ECS Express has a baseline cost: the Fargate task runs continuously and the shared
  Application Load Balancer is billed even when idle — it is **not** purely pay-per-request.
  On top of that you pay per-use for Anthropic + Pinecone. Add auth/rate limiting before
  exposing it publicly, and delete the service when you're done to stop the baseline charges.

