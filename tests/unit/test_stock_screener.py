"""Unit tests for stocks.screener scoring/ranking and stocks.report writers."""

import json

import numpy as np
import pandas as pd
import pytest

from stocks.data import CsvCacheProvider, PriceData, fetch_with_fallback
from stocks.metrics import metrics_table
from stocks.report import write_reports
from stocks.screener import breakout_signals, diff_runs, eligible_mask, run_screen
from stocks.universe import _parse_constituents, build_universe


def _synthetic_prices(n_tickers=40, days=300, seed=1):
    rng = np.random.default_rng(seed)
    idx = pd.bdate_range("2025-06-02", periods=days)
    close, vol = {}, {}
    for i in range(n_tickers):
        r = rng.normal(0.0003, 0.015, size=days)
        if i == 0:  # engineered breakout: last month +1%/day and 3x volume
            r[-21:] += 0.01
        if i == 1:  # engineered loser
            r -= 0.003
        close[f"T{i}"] = 100 * np.cumprod(1 + r)
        v = np.full(days, 2_000_000.0)
        if i == 0:
            v[-10:] *= 3
        if i == 2:  # illiquid
            v[:] = 1_000.0
        vol[f"T{i}"] = v
    return PriceData(pd.DataFrame(close, index=idx), pd.DataFrame(vol, index=idx))


@pytest.fixture
def screened():
    data = _synthetic_prices()
    m = metrics_table(data.close, data.volume)
    meta = pd.DataFrame({"name": m.index, "sector": "Tech"}, index=m.index)
    return run_screen(m, meta=meta, as_of="2026-01-01", provider="test", top_n=10, breakout_n=5)


def test_illiquid_and_short_history_excluded():
    data = _synthetic_prices()
    m = metrics_table(data.close, data.volume)
    mask = eligible_mask(m)
    assert not mask["T2"]  # illiquid
    assert mask["T0"]
    m.loc["T3", "days_of_history"] = 50
    assert not eligible_mask(m)["T3"]


def test_breakout_detects_engineered_surge(screened):
    assert "T0" in screened.breakouts.index[:3]
    sig = screened.breakouts.loc["T0", "signals"]
    assert any(s.startswith("volume x") for s in sig)
    assert "momentum accelerating" in sig


def test_loser_not_on_leaderboard(screened):
    assert "T1" not in screened.leaderboard.index
    assert len(screened.leaderboard) == 10
    assert screened.leaderboard["perf_score"].is_monotonic_decreasing
    assert screened.breakouts["breakout_score"].between(0, 100).all()


def test_scores_are_percentile_based(screened):
    t = screened.table
    assert t["perf_score"].max() <= 100 and t["perf_score"].min() >= 0
    assert t["perf_rank"].min() == 1 and t["perf_rank"].max() == len(t)


def test_breakout_signals_text():
    row = pd.Series({
        "new_52w_high": 1, "pct_from_52w_high": 0.0, "volume_ratio_10_60": 2.0,
        "golden_cross_recent": 1, "above_sma50": 1, "above_sma200": 1,
        "accel_1m_vs_6m": 0.1, "rsi_14": 88.0,
    })
    sig = breakout_signals(row)
    assert sig[0] == "new 52w high"
    assert "volume x2.0" in sig and "golden cross" in sig
    assert sig[-1] == "RSI 88 (overbought)"


def test_diff_runs():
    assert diff_runs(["A", "B"], None) == {"entered": [], "exited": []}
    assert diff_runs(["A", "C"], ["A", "B"]) == {"entered": ["C"], "exited": ["B"]}


def test_reports_written_with_history_diff(tmp_path, screened):
    md, js, hist = write_reports(screened, tmp_path)
    assert md.exists() and js.exists() and hist.name == "2026-01-01.json"
    payload = json.loads(js.read_text())
    assert payload["changes"]["previous_as_of"] is None
    assert len(payload["leaderboard"]) == 10
    text = md.read_text()
    assert "## Top 10 performers" in text and "Breakout watchlist" in text

    # Second run: the previous run becomes the baseline for change detection.
    screened.as_of = "2026-01-08"
    screened.leaderboard = screened.leaderboard.iloc[1:]
    write_reports(screened, tmp_path)
    payload2 = json.loads((tmp_path / "latest.json").read_text())
    assert payload2["changes"]["previous_as_of"] == "2026-01-01"
    assert len(payload2["changes"]["leaderboard"]["exited"]) == 1
    assert "## Changes since 2026-01-01" in (tmp_path / "latest.md").read_text()


def test_cache_provider_roundtrip(tmp_path):
    data = _synthetic_prices(n_tickers=3, days=40)
    data.save(tmp_path)
    got, name = fetch_with_fallback(["T0", "T1", "ZZZ"], [CsvCacheProvider(tmp_path)])
    assert name == "cache"
    assert list(got.close.columns) == ["T0", "T1"]
    assert got.close.iloc[-1, 0] == pytest.approx(data.close.iloc[-1, 0])


def test_fallback_skips_failing_and_low_coverage_provider(tmp_path):
    class Boom:
        name = "boom"
        def fetch(self, tickers, lookback="14mo"):
            raise RuntimeError("down")

    class Sparse:
        name = "sparse"
        def fetch(self, tickers, lookback="14mo"):
            d = _synthetic_prices(n_tickers=1, days=40)
            return d

    good = _synthetic_prices(n_tickers=3, days=40)
    good.save(tmp_path)
    got, name = fetch_with_fallback(["T0", "T1", "T2"], [Boom(), Sparse(), CsvCacheProvider(tmp_path)], cache_dir=tmp_path)
    assert name == "cache"
    with pytest.raises(RuntimeError, match="All price providers failed"):
        fetch_with_fallback(["T0"], [Boom()], cache_dir=tmp_path)


def test_universe_parsing_and_extras(tmp_path, monkeypatch):
    csv = "Symbol,Security,GICS Sector,GICS Sub-Industry\nBRK.B,Berkshire,Financials,Multi\nAAPL,Apple,IT,Hardware\n"
    secs = _parse_constituents(csv)
    assert secs[0].symbol == "BRK-B" and secs[1].sector == "IT"
    monkeypatch.setattr("stocks.universe.load_sp500", lambda cache_dir: list(secs))
    u = build_universe("sp500", extra=["tsla", "AAPL"], exclude=["brk.b"], cache_dir=tmp_path)
    assert [s.symbol for s in u] == ["AAPL", "TSLA"]
    assert [s.symbol for s in build_universe("none", extra=["PLTR"])] == ["PLTR"]
