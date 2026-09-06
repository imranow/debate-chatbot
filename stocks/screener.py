"""Scoring and ranking.

Two outputs:

1. **Top 100 leaderboard** — the best *performing* stocks, ranked by a
   composite of multi-horizon returns and risk-adjusted return, with a
   penalty for names that have already broken down from their highs.

2. **Breakout watchlist** ("stocks that look like they could boom") —
   names showing momentum *acceleration* plus confirming signals: new
   52-week highs, volume expansion, price above rising moving averages,
   a fresh golden cross. Momentum has historically persisted for months
   (Jegadeesh & Titman 1993), but this is a probabilistic screen, not a
   forecast.

Scores use cross-sectional percentile ranks (0..1) so a single extreme
outlier cannot dominate and the score is comparable across runs.
"""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np
import pandas as pd

MIN_HISTORY_DAYS = 200
MIN_DOLLAR_VOLUME = 5_000_000  # avoid illiquid names

LEADERBOARD_WEIGHTS = {
    "ret_3m": 0.20,
    "ret_6m": 0.25,
    "mom_12_1": 0.25,
    "risk_adj_6m": 0.20,
    "pct_from_52w_high": 0.10,  # closer to high = better
}

BREAKOUT_WEIGHTS = {
    "ret_1m": 0.25,
    "accel_1m_vs_6m": 0.25,
    "volume_ratio_10_60": 0.15,
    "pct_from_52w_high": 0.15,
    "ret_3m": 0.10,
    "risk_adj_6m": 0.10,
}


@dataclass
class ScreenResult:
    as_of: str
    provider: str
    universe_size: int
    eligible: int
    table: pd.DataFrame            # all eligible tickers, scored
    leaderboard: pd.DataFrame      # top N by perf_score
    breakouts: pd.DataFrame        # top M by breakout_score with signals
    notes: list[str] = field(default_factory=list)


def _pct_rank(s: pd.Series) -> pd.Series:
    return s.rank(pct=True, na_option="keep")


def _weighted_score(df: pd.DataFrame, weights: dict[str, float]) -> pd.Series:
    """Weighted mean of percentile ranks; missing metrics reweight the rest."""
    parts = []
    wts = []
    for col, w in weights.items():
        if col in df.columns:
            parts.append(_pct_rank(df[col]) * w)
            wts.append(df[col].notna() * w)
    num = pd.concat(parts, axis=1).sum(axis=1, min_count=1)
    den = pd.concat(wts, axis=1).sum(axis=1)
    return (num / den.replace(0, np.nan)) * 100.0


def eligible_mask(m: pd.DataFrame) -> pd.Series:
    mask = m["days_of_history"] >= MIN_HISTORY_DAYS
    if "avg_dollar_volume_20d" in m.columns:
        mask &= m["avg_dollar_volume_20d"].fillna(0) >= MIN_DOLLAR_VOLUME
    if "ret_6m" in m.columns:
        mask &= m["ret_6m"].notna()
    return mask


def breakout_signals(row: pd.Series) -> list[str]:
    """Human-readable confirming signals for one ticker."""
    sig = []
    if row.get("new_52w_high", 0) == 1:
        sig.append("new 52w high")
    elif row.get("pct_from_52w_high", -1) >= -0.03:
        sig.append("within 3% of 52w high")
    if row.get("volume_ratio_10_60", 0) >= 1.5:
        sig.append(f"volume x{row['volume_ratio_10_60']:.1f}")
    if row.get("golden_cross_recent", 0) == 1:
        sig.append("golden cross")
    if row.get("above_sma50", 0) == 1 and row.get("above_sma200", 0) == 1:
        sig.append("above 50/200dma")
    if row.get("accel_1m_vs_6m", 0) > 0.05:
        sig.append("momentum accelerating")
    r = row.get("rsi_14", float("nan"))
    if r == r:
        if r >= 80:
            sig.append(f"RSI {r:.0f} (overbought)")
        elif r >= 60:
            sig.append(f"RSI {r:.0f}")
    return sig


def run_screen(
    metrics: pd.DataFrame,
    meta: pd.DataFrame | None = None,
    as_of: str = "",
    provider: str = "",
    top_n: int = 100,
    breakout_n: int = 25,
) -> ScreenResult:
    """Score the metrics table and produce leaderboard + breakout watchlist.

    meta: optional DataFrame indexed by symbol with name/sector columns.
    """
    m = metrics.copy()
    notes: list[str] = []
    mask = eligible_mask(m)
    dropped = int((~mask).sum())
    if dropped:
        notes.append(
            f"{dropped} tickers excluded (history < {MIN_HISTORY_DAYS} days, "
            f"avg dollar volume < ${MIN_DOLLAR_VOLUME:,}, or missing returns)."
        )
    m = m[mask].copy()
    if m.empty:
        raise ValueError("No eligible tickers after filtering")

    m["perf_score"] = _weighted_score(m, LEADERBOARD_WEIGHTS)
    m["breakout_score"] = _weighted_score(m, BREAKOUT_WEIGHTS)

    # Trend confirmation bonus/penalty for the breakout score.
    trend_ok = (m.get("above_sma50", 0) == 1) & (m.get("above_sma200", 0) == 1)
    m.loc[trend_ok, "breakout_score"] += 5
    m.loc[m.get("new_52w_high", 0) == 1, "breakout_score"] += 5
    m.loc[m.get("golden_cross_recent", 0) == 1, "breakout_score"] += 3
    m.loc[m.get("rsi_14", 0) >= 85, "breakout_score"] -= 5  # parabolic, mean-reversion risk
    m["breakout_score"] = m["breakout_score"].clip(0, 100)

    if meta is not None:
        m = m.join(meta.reindex(m.index), how="left")

    m["perf_rank"] = m["perf_score"].rank(ascending=False, method="first").astype(int)
    m["breakout_rank"] = m["breakout_score"].rank(ascending=False, method="first").astype(int)
    m["signals"] = [breakout_signals(r) for _, r in m.iterrows()]

    leaderboard = m.sort_values("perf_score", ascending=False).head(top_n)
    breakouts = m.sort_values("breakout_score", ascending=False).head(breakout_n)

    return ScreenResult(
        as_of=as_of,
        provider=provider,
        universe_size=len(metrics),
        eligible=len(m),
        table=m,
        leaderboard=leaderboard,
        breakouts=breakouts,
        notes=notes,
    )


def diff_runs(current: list[str], previous: list[str] | None) -> dict[str, list[str]]:
    """New entrants / dropouts between two ranked symbol lists."""
    if not previous:
        return {"entered": [], "exited": []}
    cur, prev = set(current), set(previous)
    return {
        "entered": [s for s in current if s not in prev],
        "exited": [s for s in previous if s not in cur],
    }
