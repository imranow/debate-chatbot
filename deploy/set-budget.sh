#!/usr/bin/env bash
#
# Phase 8: a billing budget with an alert, so an unexpected bill announces
# itself rather than arriving at the end of the month.
#
# The Cloud Run free tier (2M requests, 180,000 vCPU-seconds and 360,000
# GiB-seconds per month, request-based billing) is far beyond what a portfolio
# demo uses, so the expected steady state is zero. Any alert here means
# something is wrong, not that traffic grew.
#
set -euo pipefail

PROJECT_ID="${PROJECT_ID:?set PROJECT_ID}"
AMOUNT="${AMOUNT:-5}"
CURRENCY="${CURRENCY:-GBP}"

BILLING_ACCOUNT="${BILLING_ACCOUNT:-$(gcloud beta billing projects describe "${PROJECT_ID}" \
  --format='value(billingAccountName)' | sed 's|billingAccounts/||')}"

if [ -z "${BILLING_ACCOUNT}" ]; then
  echo "ERROR: could not determine the billing account for ${PROJECT_ID}." >&2
  exit 1
fi

echo "Creating a ${AMOUNT} ${CURRENCY} budget on project ${PROJECT_ID}"

gcloud beta billing budgets create \
  --billing-account="${BILLING_ACCOUNT}" \
  --display-name="Debate Chatbot monthly cap" \
  --budget-amount="${AMOUNT}${CURRENCY}" \
  --filter-projects="projects/$(gcloud projects describe "${PROJECT_ID}" --format='value(projectNumber)')" \
  --threshold-rule=percent=0.5 \
  --threshold-rule=percent=0.9 \
  --threshold-rule=percent=1.0

echo
echo "Budgets on this billing account:"
gcloud beta billing budgets list --billing-account="${BILLING_ACCOUNT}" \
  --format='table(displayName, amount.specifiedAmount.units, amount.specifiedAmount.currencyCode)'
echo
echo "Note: a budget alerts, it does not cap. It cannot stop spend on its own."
echo "The hard guard is --max-instances on the service."
