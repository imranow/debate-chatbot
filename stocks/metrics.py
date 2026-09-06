"""Per-ticker performance and momentum metrics from daily closes and volume.

Everything is a pure function of the price history so it is easy to unit
test and to back-test later. Windows are in trading days (21 ~ 1 month).
"""

from __future__ import annotations

import math

import numpy as np
import pandas as pd

TRADING_DAYS = {"1m": 21, "3m": 63, "6m": 126, "12m": 252}


def _ret(close: pd.Series, days: int) -> float:
    """Simple return over the last `days` trading days (NaN if not enough data)."""
    if len(close) <= days:
        return float("nan")
    start = close.iloc[-days - 1]
    end = close.iloc[-1]
    if not (start > 0):
        return float("nan")
    return float(end / start - 1.0)


def rsi(close: pd.Series, period: int = 14) -> float:
    """Wilder's RSI on the last value of the series."""
    if len(close) < period + 1:
        return float("nan")
    delta = close.diff().dropna()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.ewm(alpha=1 / period, adjust=False).mean().iloc[-1]
    avg_loss = loss.ewm(alpha=1 / period, adjust=False).mean().iloc[-1]
    if avg_loss == 0:
        return 100.0
    rs = avg_gain / avg_loss
    return float(100 - 100 / (1 + rs))


def max_drawdown(close: pd.Series) -> float:
    """Worst peak-to-trough decline over the series (negative number)."""
    if close.empty:
        return float("nan")
    peak = close.cummax()
    dd = close / peak - 1.0
    return float(dd.min())


def ytd_return(close: pd.Series) -> float:
    last_date = close.index[-1]
    prior_year = close[close.index.year < last_date.year]
    if prior_year.empty:
        return float("nan")
    base = prior_year.iloc[-1]
    return float(close.iloc[-1] / base - 1.0) if base > 0 else float("nan")


def compute_metrics(close: pd.Series, volume: pd.Series | None = None) -> dict[str, float]:
    """Compute the metric dictionary for one ticker.

    Returns NaN for anything the history cannot support; the screener treats
    tickers with too little history as ineligible.
    """
    close = close.dropna()
    close = close[close > 0]
    n = len(close)
    out: dict[str, float] = {"days_of_history": float(n)}
    if n < 30:
        return out

    last = float(close.iloc[-1])
    out["last_close"] = last
    for label, days in TRADING_DAYS.items():
        out[f"ret_{label}"] = _ret(close, days)
    out["ret_ytd"] = ytd_return(close)

    # Classic 12-1 momentum: 12-month return excluding the most recent month.
    if n > 252:
        p_12 = close.iloc[-253]
        p_1 = close.iloc[-22]
        out["mom_12_1"] = float(p_1 / p_12 - 1.0) if p_12 > 0 else float("nan")
    else:
        out["mom_12_1"] = float("nan")

    window_52w = close.iloc[-252:]
    high_52w = float(window_52w.max())
    low_52w = float(window_52w.min())
    out["high_52w"] = high_52w
    out["pct_from_52w_high"] = last / high_52w - 1.0 if high_52w > 0 else float("nan")
    out["pct_above_52w_low"] = last / low_52w - 1.0 if low_52w > 0 else float("nan")
    # New 52-week high within the last 5 sessions?
    recent = close.iloc[-5:]
    prior = close.iloc[-252:-5]
    out["new_52w_high"] = float(bool(len(prior) and recent.max() >= prior.max()))

    sma50 = close.rolling(50).mean()
    sma200 = close.rolling(200).mean()
    out["sma50"] = float(sma50.iloc[-1]) if n >= 50 else float("nan")
    out["sma200"] = float(sma200.iloc[-1]) if n >= 200 else float("nan")
    out["above_sma50"] = float(last > out["sma50"]) if n >= 50 else float("nan")
    out["above_sma200"] = float(last > out["sma200"]) if n >= 200 else float("nan")
    out["sma50_gt_sma200"] = (
        float(out["sma50"] > out["sma200"]) if n >= 200 else float("nan")
    )
    # Golden cross within the last 20 sessions: 50dma crossed above 200dma.
    if n >= 220:
        diff = (sma50 - sma200).iloc[-21:]
        out["golden_cross_recent"] = float(bool(diff.iloc[0] <= 0 and diff.iloc[-1] > 0))
    else:
        out["golden_cross_recent"] = float("nan")

    daily = close.pct_change().dropna()
    vol_window = daily.iloc[-126:]
    out["vol_ann"] = float(vol_window.std() * math.sqrt(252)) if len(vol_window) > 20 else float("nan")
    r6 = out.get("ret_6m", float("nan"))
    out["risk_adj_6m"] = (
        r6 / out["vol_ann"] if out["vol_ann"] and not math.isnan(out["vol_ann"]) and out["vol_ann"] > 0 else float("nan")
    )
    out["max_dd_6m"] = max_drawdown(close.iloc[-126:])
    out["rsi_14"] = rsi(close)

    # Acceleration: is the last month running hotter than the 6-month trend?
    r1 = out.get("ret_1m", float("nan"))
    if not (math.isnan(r1) or math.isnan(r6)):
        monthly_trend = (1 + r6) ** (1 / 6) - 1 if r6 > -1 else float("nan")
        out["accel_1m_vs_6m"] = r1 - monthly_trend
    else:
        out["accel_1m_vs_6m"] = float("nan")

    if volume is not None:
        volume = volume.reindex(close.index).fillna(0)
        v10 = float(volume.iloc[-10:].mean())
        v60 = float(volume.iloc[-70:-10].mean()) if n >= 70 else float("nan")
        out["volume_ratio_10_60"] = v10 / v60 if v60 and v60 > 0 else float("nan")
        out["avg_dollar_volume_20d"] = float((close.iloc[-20:] * volume.iloc[-20:]).mean())
    return out


def metrics_table(close: pd.DataFrame, volume: pd.DataFrame | None = None) -> pd.DataFrame:
    """Compute metrics for every column; index = ticker."""
    rows = {}
    for t in close.columns:
        vol = volume[t] if volume is not None and t in volume.columns else None
        rows[t] = compute_metrics(close[t], vol)
    df = pd.DataFrame.from_dict(rows, orient="index")
    df.index.name = "symbol"
    return df.replace([np.inf, -np.inf], np.nan)
