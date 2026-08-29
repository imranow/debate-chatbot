# Deploying to Cloud Run

Four scripts, run in order. Everything is idempotent and safe to re-run.

```bash
export PROJECT_ID=your-project-id
export REGION=europe-west1

./deploy/setup-gcp.sh        # APIs, Artifact Registry, runtime service account
./deploy/create-secrets.sh   # you run this: it prompts for the two API keys
./deploy/deploy.sh           # Cloud Build, then deploy with explicit runtime config
./deploy/set-budget.sh       # 5 GBP budget alert at 50/90/100%
```

## Prerequisites you have to do by hand

A billing account linked to the project. Cloud Run needs one even when usage
sits entirely inside the free tier, and linking it takes a card. Nothing else
in these scripts requires the console.

## Region

Default is `europe-west1` (Belgium), not `europe-west2` (London). Both are
close enough to Manchester that the difference is a few milliseconds, but
`europe-west1` is a Tier 1 Cloud Run region and `europe-west2` is Tier 2, so
Tier 2 charges more per vCPU-second once past the free tier. Set
`REGION=europe-west2` if you would rather have the data in the UK; at this
traffic level the cost difference is zero either way.

Worth knowing: the Pinecone index is in `us-east-1` and Anthropic is
US-hosted, so every request makes two transatlantic hops regardless. Hosting
in Europe helps the browser connection, not the backend path.

## Secrets

`create-secrets.sh` reads each key with `read -rsp`, so the value is never
echoed, never written to a file, and never enters shell history. It goes
straight into Secret Manager and the runtime service account is granted
`secretAccessor` on those two secrets only.

On ECS these keys were plain environment variables in the task definition,
visible to anyone with console read access. Rotate both after the AWS
teardown: they have lived in two places.

## Verifying a deploy

```bash
# Same 12 questions to both deployments; compares retrieved citation IDs.
python -m evals.compare_deployments \
  --baseline  https://<old-ecs-url> \
  --candidate https://<new-run-url>

# Judged quality scores against a running service.
EVAL_TARGET_URL=https://<url> EVAL_REPORT_PATH=evals/run.json \
  pytest evals/ -q
```

The parity harness is the sharper of the two for a migration. An LLM judge
moves a few points between runs on identical input; retrieval does not. If the
citation IDs match across both deployments, retrieval is provably unchanged.

## A note on the budget currency

`set-budget.sh` leaves `CURRENCY` empty by default, so the budget uses the
billing account's own currency. The API rejects a budget whose currency differs
from the billing account's, so only set `CURRENCY=GBP` once you know the
account is in sterling.

## Flags

Every gcloud flag in these scripts was checked against the current reference
rather than written from memory. Two things that are easy to get wrong:
`--filter-projects` takes `projects/{project_id}`, not the project number, and
threshold percentages are 1.0-based, so `percent=0.50` means fifty percent.
