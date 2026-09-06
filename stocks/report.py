"""Report writers: JSON (machine-readable, kept as history) and Markdown."""

from __future__ import annotations

import json
import math
from datetime import date
from pathlib import Path
from typing import Any

import pandas as pd

from .screener import ScreenResult, diff_runs

LEADERBOARD_COLS = [
    "perf_rank", "symbol", "name", "sector", "last_close", "ret_1m", "ret_3m",
    "ret_6m", "ret_12m", "ret_ytd", "pct_from_52w_high", "vol_ann", "perf_score",
]
BREAKOUT_COLS = [
    "breakout_rank", "symbol", "name", "sector", "last_close", "ret_1m", "ret_3m",
    "volume_ratio_10_60", "pct_from_52w_high", "rsi_14", "breakout_score", "signals",
]
PCT_COLS = {"ret_1m", "ret_3m", "ret_6m", "ret_12m", "ret_ytd", "pct_from_52w_high", "vol_ann"}


def _fmt(col: str, v: Any) -> str:
    if isinstance(v, list):
        return ", ".join(v) if v else "-"
    if v is None or (isinstance(v, float) and math.isnan(v)):
        return "-"
    if col in PCT_COLS:
        return f"{v * 100:+.1f}%"
    if col in {"perf_score", "breakout_score", "rsi_14"}:
        return f"{v:.0f}"
    if col == "volume_ratio_10_60":
        return f"x{v:.2f}"
    if col == "last_close":
        return f"{v:,.2f}"
    if isinstance(v, float):
        return f"{v:.2f}"
    return str(v)


def _md_table(df: pd.DataFrame, cols: list[str]) -> str:
    df = df.reset_index()
    cols = [c for c in cols if c in df.columns]
    header = "| " + " | ".join(cols) + " |"
    sep = "|" + "|".join(["---"] * len(cols)) + "|"
    lines = [header, sep]
    for _, r in df.iterrows():
        lines.append("| " + " | ".join(_fmt(c, r[c]) for c in cols) + " |")
    return "\n".join(lines)


def _records(df: pd.DataFrame, cols: list[str]) -> list[dict[str, Any]]:
    df = df.reset_index()
    cols = [c for c in cols if c in df.columns]
    out = []
    for _, r in df.iterrows():
        rec = {}
        for c in cols:
            v = r[c]
            if isinstance(v, float) and math.isnan(v):
                v = None
            elif hasattr(v, "item"):
                v = v.item()
            rec[c] = v
        out.append(rec)
    return out


def load_previous(history_dir: Path) -> dict[str, Any] | None:
    files = sorted(history_dir.glob("*.json"))
    if not files:
        return None
    with files[-1].open(encoding="utf-8") as fh:
        return json.load(fh)


def to_json(result: ScreenResult, previous: dict[str, Any] | None) -> dict[str, Any]:
    lb_syms = [str(s) for s in result.leaderboard.index]
    bo_syms = [str(s) for s in result.breakouts.index]
    prev_lb = previous.get("leaderboard_symbols") if previous else None
    prev_bo = previous.get("breakout_symbols") if previous else None
    return {
        "as_of": result.as_of,
        "generated": date.today().isoformat(),
        "provider": result.provider,
        "universe_size": result.universe_size,
        "eligible": result.eligible,
        "notes": result.notes,
        "leaderboard_symbols": lb_syms,
        "breakout_symbols": bo_syms,
        "changes": {
            "leaderboard": diff_runs(lb_syms, prev_lb),
            "breakouts": diff_runs(bo_syms, prev_bo),
            "previous_as_of": previous.get("as_of") if previous else None,
        },
        "leaderboard": _records(result.leaderboard, LEADERBOARD_COLS),
        "breakouts": _records(result.breakouts, BREAKOUT_COLS),
    }


def to_markdown(payload: dict[str, Any], result: ScreenResult) -> str:
    ch = payload["changes"]
    lines = [
        f"# Stock Screener — {payload['as_of']}",
        "",
        f"Universe: {payload['universe_size']} tickers · eligible: {payload['eligible']} · "
        f"data: {payload['provider']} · generated {payload['generated']}",
        "",
        "> Systematic screen of price action only. Not investment advice. "
        "Momentum tends to persist for 3-12 months but reverses sharply at turns; "
        "size positions accordingly.",
        "",
    ]
    if ch.get("previous_as_of"):
        lines += [
            f"## Changes since {ch['previous_as_of']}",
            "",
            f"- **New in Top 100:** {', '.join(ch['leaderboard']['entered']) or 'none'}",
            f"- **Dropped from Top 100:** {', '.join(ch['leaderboard']['exited']) or 'none'}",
            f"- **New on breakout watchlist:** {', '.join(ch['breakouts']['entered']) or 'none'}",
            f"- **Off breakout watchlist:** {', '.join(ch['breakouts']['exited']) or 'none'}",
            "",
        ]
    lines += [
        f"## Breakout watchlist (top {len(result.breakouts)})",
        "",
        "Momentum acceleration + confirming signals (new highs, volume, trend). "
        "Score 0-100 is a cross-sectional percentile composite.",
        "",
        _md_table(result.breakouts, BREAKOUT_COLS),
        "",
        f"## Top {len(result.leaderboard)} performers",
        "",
        "Ranked by composite of 3m / 6m / 12-1 momentum, risk-adjusted 6m return, "
        "and proximity to 52-week high.",
        "",
        _md_table(result.leaderboard, LEADERBOARD_COLS),
        "",
    ]
    if result.table is not None and "sector" in result.table.columns:
        sec = (
            result.leaderboard.groupby("sector").size().sort_values(ascending=False)
            if "sector" in result.leaderboard.columns else None
        )
        if sec is not None and len(sec):
            lines += ["## Top-100 sector mix", ""]
            lines += [f"- {k or 'Unknown'}: {v}" for k, v in sec.items()]
            lines.append("")
    if payload["notes"]:
        lines += ["## Notes", ""] + [f"- {n}" for n in payload["notes"]] + [""]
    lines += [
        "## Method",
        "",
        "- **Performance score** = weighted percentile ranks of 3m return (20%), 6m return (25%), "
        "12-1 month momentum (25%), 6m return / annualised volatility (20%), distance from 52w high (10%).",
        "- **Breakout score** = weighted percentile ranks of 1m return, 1m-vs-6m acceleration, "
        "10d/60d volume ratio, distance from 52w high, 3m return, risk-adjusted 6m return; "
        "+5 above 50/200dma, +5 new 52w high, +3 fresh golden cross, -5 if RSI ≥ 85.",
        "- Eligibility: ≥200 trading days of history and ≥$5M average daily dollar volume.",
        "",
    ]
    return "\n".join(lines)


def write_reports(result: ScreenResult, out_dir: Path) -> tuple[Path, Path, Path]:
    out_dir.mkdir(parents=True, exist_ok=True)
    history = out_dir / "history"
    history.mkdir(exist_ok=True)
    previous = load_previous(history)
    payload = to_json(result, previous)
    md = to_markdown(payload, result)

    latest_json = out_dir / "latest.json"
    latest_md = out_dir / "latest.md"
    hist_file = history / f"{result.as_of}.json"
    latest_json.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    hist_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    latest_md.write_text(md, encoding="utf-8")
    return latest_md, latest_json, hist_file
