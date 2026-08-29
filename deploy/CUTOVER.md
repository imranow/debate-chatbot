# Cutover runbook

Ordered steps from "billing is linked" to "AWS is switched off". Everything
before this point is done; everything here needs the service to exist.

## 1. Deploy

```bash
export PROJECT_ID=your-project-id
export REGION=europe-west1
export PINECONE_INDEX_HOST=https://...   # from the ECS task definition

./deploy/setup-gcp.sh
./deploy/create-secrets.sh    # prompts for the two keys
./deploy/deploy.sh
```

`deploy.sh` prints the service URL and a health check at the end. If the health
check does not return 200, stop here and read the logs:

```bash
gcloud run services logs read debate-chatbot --region="${REGION}" --limit=50
```

## 2. Smoke test

```bash
RUN_URL=$(gcloud run services describe debate-chatbot --region="${REGION}" --format='value(status.url)')

curl -sS -X POST "${RUN_URL}/chat" \
  -H 'content-type: application/json' \
  -d '{"question":"What did Bernie Sanders say about billionaires?"}' | head -c 600
```

Expect a JSON `answer` containing `[n]` citation markers and a `citations`
array. A 502 with "Unable to retrieve relevant sources" means Pinecone; a 502
with "Language model is temporarily unavailable" means Anthropic. Both point at
the secrets rather than at Cloud Run.

## 3. Measure cold start

This is the number the README asks for, and it needs a genuinely cold
instance. Wait out the idle period rather than guessing.

```bash
echo "waiting 20 minutes for the instance to be reclaimed..."
sleep 1200

curl -s -o /dev/null -w "cold start to first byte: %{time_starttransfer}s\n" "${RUN_URL}/health"
curl -s -o /dev/null -w "warm:                     %{time_starttransfer}s\n" "${RUN_URL}/health"
```

The ECS baseline for a warm `/health` was 0.24 to 0.51s. Local process startup
with the production dependency set was 0.94 to 1.30s, so a cold start much
above about 3s means image pull is dominating and the image is worth another
look. Above 10s, go back and cut image size or move startup work to lazy
initialisation, as the brief says.

## 4. Prove retrieval did not change

```bash
python -m evals.compare_deployments \
  --baseline  https://de-fafa3ceb88a24b38b241702b67d9b091.ecs.us-east-1.on.aws \
  --candidate "${RUN_URL}" \
  --out evals/parity.json
```

Exit code 0 means every question returned the same citation set. Anything else
is a blocker, not a curiosity: both deployments read the same Pinecone index
with the same code, so a difference means something is genuinely wrong with the
new deployment rather than that the model felt different today.

Note the harness asks each question once per deployment on purpose. The answer
cache in `backend/rag/rag.py` is keyed on the question, so asking twice measures
the cache rather than the pipeline.

Optionally, judged scores:

```bash
EVAL_TARGET_URL="${RUN_URL}" EVAL_REPORT_PATH=evals/cloudrun.json pytest evals/ -q
```

That spends Anthropic tokens: 12 questions through the pipeline plus three
judged metrics each.

## 5. Fill in the README

`README.md` has three placeholders marked `<!-- FILL IN AFTER CUTOVER -->`.
Fill them from steps 3 and 4:

- measured cold start, first request after 20 minutes idle
- measured warm request latency
- median latency comparison, from `evals/parity.json`

## 6. Update every reference to the URL

Four places, and it is worth doing all of them in one sitting because the last
two URL changes were missed:

| Where | What |
|---|---|
| `README.md` line 3 | the `Link:` line |
| `Portfolio/public/index.html` | the `Live` button on the project card |
| `Portfolio/public/projects/debate-chatbot/index.html` | the `Live` button |
| `cv-tailor` skill, line 137 | the `[Live Demo]` link |

The Portfolio repo deploys from `main` through GitHub Pages, so pushing a
branch is not enough. Merge it.

While in the `cv-tailor` skill, line 52's Cloud & Deployment list should gain
GCP: `AWS (ECS Fargate, ECR), GCP (Cloud Run, Artifact Registry, Secret
Manager)`. That is the version worth having on a CV, because it is the part of
this work an interviewer will ask about.

Also regenerate `Portfolio/public/assets/imran-tanbir-cv.docx`, which is older
than the current pipeline output.

## 7. Run both for 48 hours

Leave ECS up. It costs about 2.50 USD a day, which is a cheap rollback.

## 8. Tear down

Follow `deploy/aws-teardown.md`. Delete the ECS Express service first and
confirm the load balancer and the public IPv4 charges stop, since those are
75 of the 77 dollars.

## 9. Rotate the keys

Both have lived in an ECS task definition as plain environment variables and in
GCP Secret Manager. Rotate in Pinecone and Anthropic, then:

```bash
./deploy/create-secrets.sh     # adds a new version of each secret
gcloud run services update debate-chatbot --region="${REGION}"   # picks up :latest
```

## 10. Set the budget

```bash
./deploy/set-budget.sh
```

Left until last deliberately: it needs the billing account to have been used at
least once for the currency to resolve cleanly.
