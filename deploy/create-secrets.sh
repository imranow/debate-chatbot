#!/usr/bin/env bash
#
# Phase 3: put the two API keys into Secret Manager and grant the runtime
# service account read access to those two secrets only.
#
# Run this yourself. It prompts for the key values and never echoes them,
# never writes them to a file, and never puts them in your shell history.
#
# On ECS these keys were plain environment variables in the task definition,
# readable by anyone with console access. After this, they are versioned
# secrets and the service reads them at start.
#
set -euo pipefail

PROJECT_ID="${PROJECT_ID:?set PROJECT_ID}"
SA_NAME="${SA_NAME:-debate-chatbot-run}"
SA_EMAIL="${SA_NAME}@${PROJECT_ID}.iam.gserviceaccount.com"

gcloud config set project "${PROJECT_ID}" >/dev/null

put_secret () {
  local name="$1" prompt="$2" value

  # -s suppresses the echo, so the key never appears on screen.
  read -rsp "${prompt}: " value
  echo

  if [ -z "${value}" ]; then
    echo "  skipped (empty input)"
    return
  fi

  if gcloud secrets describe "${name}" >/dev/null 2>&1; then
    printf '%s' "${value}" | gcloud secrets versions add "${name}" --data-file=-
    echo "  added a new version of ${name}"
  else
    printf '%s' "${value}" | gcloud secrets create "${name}" \
      --replication-policy=automatic --data-file=-
    echo "  created ${name}"
  fi
  unset value

  gcloud secrets add-iam-policy-binding "${name}" \
    --member="serviceAccount:${SA_EMAIL}" \
    --role=roles/secretmanager.secretAccessor \
    --condition=None >/dev/null
  echo "  granted accessor on ${name} to ${SA_NAME}"
}

echo "Values are read silently and are not echoed or stored locally."
echo
put_secret anthropic-api-key "Anthropic API key"
put_secret pinecone-api-key  "Pinecone API key"

echo
echo "Secrets in this project:"
gcloud secrets list --format='table(name)'
echo
echo "Rotate both keys after the AWS teardown: they have lived in two places."
