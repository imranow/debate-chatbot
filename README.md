# Debate Chatbot (RAG)

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

## Deploy To AWS (App Runner)

This repo includes a `Dockerfile` that runs `uvicorn` on `0.0.0.0:$PORT` (default `8080`).

### 1) Push Image To ECR (zsh-safe)

```bash
REGION=us-east-1
REPO=debate-chatbot

aws sts get-caller-identity
aws ecr create-repository --repository-name "$REPO" --region "$REGION" 2>/dev/null || true

ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REGISTRY="${ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com"
aws ecr get-login-password --region "$REGION" | docker login --username AWS --password-stdin "$REGISTRY"

IMAGE_URI="${REGISTRY}/${REPO}:latest"
docker buildx build --platform linux/amd64 -t "$IMAGE_URI" --push .
echo "$IMAGE_URI"
```

### 2) Create App Runner Service

In the AWS Console:

1. App Runner → Create service → Source: **ECR**
2. Select your image (`…/debate-chatbot:latest`)
3. Set:
   - Port: `8080`
   - Health check path: `/health`
4. Add environment variables:
   - `PINECONE_API_KEY`
   - `ANTHROPIC_API_KEY`
   - Optional but recommended: `PINECONE_INDEX_HOST`
   - Optional: `ANTHROPIC_MODEL` — leave unset to use the code default
     (`claude-sonnet-4-6`). If you set it here, this value **overrides** the
     code default, so keep it current: a retired model ID (e.g. the old
     `claude-sonnet-4-20250514`) makes every `/chat` request fail with a 502.
     Update it here when you change models, not just in code.
5. Deploy and open the App Runner URL.

## Security / Cost Notes

- Do **not** commit API keys. If you pasted a key into chat or a public place, rotate it.
- This service is effectively “pay-per-request” (Anthropic + Pinecone usage). Add auth/rate limiting before making it publicly accessible.

