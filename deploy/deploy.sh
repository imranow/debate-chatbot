#!/usr/bin/env bash
#
# Phase 4: build the image with Cloud Build and deploy it to Cloud Run.
#
# Cloud Build builds on x86-64, which sidesteps the Apple Silicon problem
# entirely: no local Docker, no --platform linux/amd64, no exec format error
# at runtime. The build runs in the same region as the registry and the
# service, so there is no cross-region image pull.
#
# Every runtime setting below is explicit. Defaults are what turn a portfolio
# demo into a surprise invoice.
#
set -euo pipefail

PROJECT_ID="${PROJECT_ID:?set PROJECT_ID}"
REGION="${REGION:-europe-west1}"
REPO="${REPO:-debate-chatbot}"
SERVICE="${SERVICE:-debate-chatbot}"
SA_NAME="${SA_NAME:-debate-chatbot-run}"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"
TAG="${TAG:-$(git rev-parse --short HEAD)}"
IMAGE="${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}/${SERVICE}:${TAG}"

# Not a secret, but worth setting: without it the Pinecone client makes a
# control-plane lookup during startup, putting a network round trip on the
# critical path of every cold start.
PINECONE_INDEX_HOST="${PINECONE_INDEX_HOST:-}"

gcloud config set project "${PROJECT_ID}" >/dev/null

echo "Building ${IMAGE}"
gcloud builds submit --region="${REGION}" --tag "${IMAGE}" .

ENV_VARS="PINECONE_INDEX_NAME=dem-debates-transcripts,PINECONE_NAMESPACE=debates"
if [ -n "${PINECONE_INDEX_HOST}" ]; then
  ENV_VARS="${ENV_VARS},PINECONE_INDEX_HOST=${PINECONE_INDEX_HOST}"
else
  echo "WARNING: PINECONE_INDEX_HOST is unset. Startup will make an extra"
  echo "         Pinecone control-plane call on every cold start."
fi

echo
echo "Deploying ${SERVICE} to ${REGION}"
gcloud run deploy "${SERVICE}" \
  --image="${IMAGE}" \
  --region="${REGION}" \
  --service-account="${SA_EMAIL}" \
  --set-env-vars="${ENV_VARS}" \
  --set-secrets="ANTHROPIC_API_KEY=anthropic-api-key:latest,PINECONE_API_KEY=pinecone-api-key:latest" \
  --min-instances=0 \
  --max-instances=3 \
  --cpu=1 \
  --memory=512Mi \
  --cpu-throttling \
  --cpu-boost \
  --concurrency=20 \
  --timeout=120 \
  --allow-unauthenticated \
  --port=8080

URL="$(gcloud run services describe "${SERVICE}" --region="${REGION}" --format='value(status.url)')"
echo
echo "Deployed: ${URL}"
echo
echo "Health check:"
curl -sS -o /dev/null -w "  %{http_code} in %{time_total}s\n" "${URL}/health"

# --- why each flag is set the way it is -------------------------------------
#
# --min-instances=0    Nothing runs when nobody is asking. This is the entire
#                      point: it is what takes the bill to zero.
#
# --max-instances=3    A public endpoint with no ceiling is how a demo becomes
#                      an invoice. Three is far above real demand and still
#                      bounds the worst case.
#
# --memory=512Mi       Measured, not guessed. Embeddings are computed by
#                      Pinecone, not in-process, so there is no model to load.
#                      The largest in-process structure is the 256-entry answer
#                      cache, roughly 2.5 MB.
#
# --cpu-throttling     CPU only during request handling. The app has no
#                      background tasks, no asyncio loops and no websockets, so
#                      there is nothing that needs CPU between requests. This is
#                      the cheaper of the two billing modes.
#
# --cpu-boost          Extra CPU during startup, at no additional cost. Free
#                      reduction in cold start latency.
#
# --concurrency=20     The app is genuinely async and IO-bound: it waits on
#                      Pinecone and Anthropic. More requests per instance means
#                      fewer instances and fewer billed vCPU-seconds. The
#                      ceiling worth knowing is anyio's default 40-thread pool,
#                      which the Pinecone calls use via asyncio.to_thread;
#                      20 leaves headroom under it.
#
# --timeout=120        Worst observed end-to-end latency on ECS was 10.3s, and
#                      max_tokens is 900 so answers are short. 120s is generous
#                      while still capping how long a hung request can hold a
#                      billed instance. The platform default of 300s is looser
#                      than this service needs.
