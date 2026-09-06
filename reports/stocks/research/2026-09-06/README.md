# Research run: 2026-09-06

Workflow-generated research behind the Notion page "Next Boom Stocks: Catalyst Hunt (Sep 2026)".

- `dossiers.json` — per-name dossiers (`stocks-dossiers` workflow). Entries with `dossier: null` are pending re-run.
- `sweep_round1_candidates.json` — candidates from the four finder agents of the verification sweep that completed
  before a usage-limit interruption (memory second tier, storage, packaging/test, optics). Unverified leads.
- `notion/` — Notion-flavored markdown rendered by `scripts/render_notion_dossiers.py --split`: `main.md` plus one
  file per tier.

Regenerate: `python scripts/render_notion_dossiers.py --split dossiers.json - notion/framework.md notion/`
