#!/usr/bin/env bash
#
# Phase 8: a billing budget with alerts, so an unexpected bill announces
# itself rather than arriving at the end of the month.
#
# The Cloud Run free tier (2M requests, 180,000 vCPU-seconds and 360,000
# GiB-seconds per month on request-based billing) is far beyond what a
# portfolio demo uses, so the expected steady state is zero. An alert here
# means something is wrong, not that traffic grew.
#
set -euo pipefail

PROJECT_ID="${PROJECT_ID:?set PROJECT_ID}"
AMOUNT="${AMOUNT:-5}"

# Leave CURRENCY empty to use the billing account's own currency. Passing a
# currency that differs from the billing account's is rejected by the API, so
# only set this if you know they match.
CURRENCY="${CURRENCY:-}"

BILLING_ACCOUNT="${BILLING_ACCOUNT:-$(gcloud billing projects describe "${PROJECT_ID}" \
  --format='value(billingAccountName)' 2>/dev/null | sed 's|billingAccounts/||')}"

if [ -z "${BILLING_ACCOUNT}" ]; then
  echo "ERROR: no billing account found for ${PROJECT_ID}." >&2
  echo "Link one at https://console.cloud.google.com/billing then re-run." >&2
  exit 1
fi

echo "Creating a ${AMOUNT}${CURRENCY:+ ${CURRENCY}} budget on project ${PROJECT_ID}"
echo "Billing account: ${BILLING_ACCOUNT}"

# --filter-projects takes projects/{project_id}, not the project number.
# Threshold percentages are 1.0-based: 0.5 is 50 percent.
gcloud billing budgets create \
  --billing-account="${BILLING_ACCOUNT}" \
  --display-name="Debate Chatbot monthly cap" \
  --budget-amount="${AMOUNT}${CURRENCY}" \
  --filter-projects="projects/${PROJECT_ID}" \
  --threshold-rule=percent=0.50 \
  --threshold-rule=percent=0.90 \
  --threshold-rule=percent=1.00

echo
echo "Budgets on this billing account:"
gcloud billing budgets list --billing-account="${BILLING_ACCOUNT}" \
  --format='table(displayName, amount.specifiedAmount.units, amount.specifiedAmount.currencyCode)'
echo
echo "Note: a budget alerts, it does not cap. It cannot stop spend on its own."
echo "The hard guard is --max-instances on the service."
