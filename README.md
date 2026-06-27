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

## Deploy To AWS (ECS Express Mode)

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

