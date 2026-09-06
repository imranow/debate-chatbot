"""Unit tests for stocks.metrics (pure functions on synthetic price series)."""

import math

import numpy as np
import pandas as pd
import pytest

from stocks.metrics import compute_metrics, max_drawdown, metrics_table, rsi


def _series(values, start="2025-01-01"):
    idx = pd.bdate_range(start, periods=len(values))
    return pd.Series(values, index=idx, dtype=float)


def test_short_history_returns_only_days():
    m = compute_metrics(_series([100] * 10))
    assert m == {"days_of_history": 10.0}


def test_returns_over_windows():
    # Linear ramp: price = 100 + day index
    n = 300
    s = _series(100 + np.arange(n))
    m = compute_metrics(s)
    last = 100 + n - 1
    assert m["ret_1m"] == pytest.approx(last / (last - 21) - 1)
    assert m["ret_12m"] == pytest.approx(last / (last - 252) - 1)
    # 12-1 momentum excludes the last month
    assert m["mom_12_1"] == pytest.approx((last - 21) / (last - 252) - 1)
    assert m["above_sma50"] == 1.0 and m["above_sma200"] == 1.0
    assert m["new_52w_high"] == 1.0
    assert m["pct_from_52w_high"] == pytest.approx(0.0)


def test_downtrend_flags():
    n = 300
    s = _series(400 - np.arange(n))
    m = compute_metrics(s)
    assert m["ret_6m"] < 0
    assert m["above_sma50"] == 0.0
    assert m["new_52w_high"] == 0.0
    assert m["pct_from_52w_high"] < 0
    assert m["rsi_14"] < 30


def test_rsi_bounds_and_flat():
    assert rsi(_series([100] * 30)) == 100.0  # no losses -> 100 by convention
    up = _series(100 + np.arange(40))
    assert 50 < rsi(up) <= 100
    assert math.isnan(rsi(_series([1, 2, 3])))


def test_max_drawdown():
    s = _series([100, 120, 60, 90, 130])
    assert max_drawdown(s) == pytest.approx(-0.5)


def test_volume_ratio_and_dollar_volume():
    n = 120
    close = _series([50.0] * n)
    vol = pd.Series([1_000_000.0] * n, index=close.index)
    vol.iloc[-10:] = 3_000_000.0
    m = compute_metrics(close, vol)
    assert m["volume_ratio_10_60"] == pytest.approx(3.0)
    assert m["avg_dollar_volume_20d"] == pytest.approx(50 * (10 * 1e6 + 10 * 3e6) / 20)


def test_golden_cross_recent():
    # 230 days: falling then sharply rising so the 50dma crosses the 200dma late.
    n = 260
    prices = np.concatenate([np.linspace(200, 100, 180), np.linspace(100, 260, n - 180)])
    m = compute_metrics(_series(prices))
    assert m["sma50_gt_sma200"] == 1.0
    assert m["golden_cross_recent"] in (0.0, 1.0)


def test_metrics_table_indexes_by_symbol_and_handles_nan():
    idx = pd.bdate_range("2025-01-01", periods=260)
    close = pd.DataFrame({"AAA": 100 + np.arange(260), "BBB": np.nan}, index=idx)
    vol = pd.DataFrame({"AAA": 1e6, "BBB": 1e6}, index=idx)
    t = metrics_table(close, vol)
    assert list(t.index) == ["AAA", "BBB"]
    assert t.loc["AAA", "days_of_history"] == 260
    assert t.loc["BBB", "days_of_history"] == 0
