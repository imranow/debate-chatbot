#!/usr/bin/env bash
#
# Phase 2: one-time GCP project setup for the Debate Chatbot on Cloud Run.
#
# Idempotent: safe to re-run. Creates nothing that already exists.
# Requires: gcloud authenticated, and a billing account already linked to
# the project (that step needs a card, so it is done by hand in the console).
#
set -euo pipefail

PROJECT_ID="${PROJECT_ID:?set PROJECT_ID, e.g. export PROJECT_ID=debate-chatbot}"
REGION="${REGION:-europe-west1}"
REPO="${REPO:-debate-chatbot}"
SA_NAME="${SA_NAME:-debate-chatbot-run}"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

echo "Project : ${PROJECT_ID}"
echo "Region  : ${REGION}"
echo

gcloud config set project "${PROJECT_ID}" >/dev/null

# Fail early and clearly if billing is not linked. Every API enable below
# fails with a much less obvious error otherwise.
if ! gcloud billing projects describe "${PROJECT_ID}" \
     --format='value(billingEnabled)' 2>/dev/null | grep -qi true; then
  echo "ERROR: no billing account is linked to ${PROJECT_ID}." >&2
  echo "Link one at https://console.cloud.google.com/billing then re-run." >&2
  exit 1
fi

echo "Enabling APIs..."
gcloud services enable \
  run.googleapis.com \
  artifactregistry.googleapis.com \
  secretmanager.googleapis.com \
  cloudbuild.googleapis.com

echo "Creating Artifact Registry repository (if absent)..."
gcloud artifacts repositories describe "${REPO}" --location="${REGION}" >/dev/null 2>&1 || \
gcloud artifacts repositories create "${REPO}" \
  --repository-format=docker \
  --location="${REGION}" \
  --description="Container images for the Debate Chatbot"

# A dedicated runtime identity. The default compute service account holds
# project-wide Editor, which is far more than a public demo should carry.
echo "Creating runtime service account (if absent)..."
gcloud iam service-accounts describe "${SA_EMAIL}" >/dev/null 2>&1 || \
gcloud iam service-accounts create "${SA_NAME}" \
  --display-name="Debate Chatbot Cloud Run runtime"

# Cloud Build needs to push into the repository we just made. Which identity it
# runs as depends on the organisation's settings: newer projects use the
# Compute Engine default service account, older ones the legacy Cloud Build
# account. Google's own docs say it "depends on your organization's settings"
# rather than naming one, so grant both and let the non-existent one fail
# quietly. Without this the first `gcloud builds submit` fails on the push,
# after the build has already succeeded, which is a confusing place to land.
PROJECT_NUMBER="$(gcloud projects describe "${PROJECT_ID}" --format='value(projectNumber)')"
echo "Granting Cloud Build permission to push images..."
for CB_SA in \
  "${PROJECT_NUMBER}@cloudbuild.gserviceaccount.com" \
  "${PROJECT_NUMBER}-compute@developer.gserviceaccount.com"
do
  if gcloud iam service-accounts describe "${CB_SA}" >/dev/null 2>&1; then
    gcloud artifacts repositories add-iam-policy-binding "${REPO}" \
      --location="${REGION}" \
      --member="serviceAccount:${CB_SA}" \
      --role=roles/artifactregistry.writer \
      --condition=None >/dev/null 2>&1 && echo "  artifactregistry.writer -> ${CB_SA}"
    # The Compute default account also needs to write build logs when it is
    # the build identity. Harmless if already held.
    gcloud projects add-iam-policy-binding "${PROJECT_ID}" \
      --member="serviceAccount:${CB_SA}" \
      --role=roles/logging.logWriter \
      --condition=None >/dev/null 2>&1 && echo "  logging.logWriter        -> ${CB_SA}"
  fi
done

echo
echo "Done."
echo "Service account: ${SA_EMAIL}"
echo "Registry       : ${REGION}-docker.pkg.dev/${PROJECT_ID}/${REPO}"
echo
echo "Next: deploy/create-secrets.sh (needs the real API key values)."
