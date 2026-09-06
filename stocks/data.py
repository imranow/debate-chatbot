"""Price data providers.

All providers return a `PriceData` with two wide DataFrames indexed by date:
`close` (split/dividend-adjusted) and `volume`, one column per ticker.

Providers:
- YFinanceProvider: default, batch download via yfinance (no API key).
- StooqProvider: per-ticker CSV from stooq.com, used as a fallback.
- CsvCacheProvider: read a previously saved snapshot (offline / tests).

Every live fetch is written to the cache so the screener can be rerun
offline and so daily history accumulates for later back-testing.
"""

from __future__ import annotations

import io
import logging
import os
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Protocol, Sequence

import pandas as pd
import requests

logger = logging.getLogger(__name__)

CACHE_DIR = Path(os.getenv("STOCKS_CACHE_DIR", ".cache/stocks"))
DEFAULT_LOOKBACK = "14mo"  # 12-month momentum + 1 month skip + buffer


@dataclass
class PriceData:
    close: pd.DataFrame
    volume: pd.DataFrame

    def tickers(self) -> list[str]:
        return [str(c) for c in self.close.columns]

    def save(self, cache_dir: Path = CACHE_DIR, as_of: date | None = None) -> Path:
        """Persist as two CSVs under cache_dir/prices_<date>/."""
        as_of = as_of or date.today()
        out = cache_dir / f"prices_{as_of.isoformat()}"
        out.mkdir(parents=True, exist_ok=True)
        self.close.to_csv(out / "close.csv")
        self.volume.to_csv(out / "volume.csv")
        return out

    @classmethod
    def load(cls, folder: Path) -> "PriceData":
        close = pd.read_csv(folder / "close.csv", index_col=0, parse_dates=True)
        volume = pd.read_csv(folder / "volume.csv", index_col=0, parse_dates=True)
        return cls(close=close, volume=volume)


class PriceProvider(Protocol):
    name: str

    def fetch(self, tickers: Sequence[str], lookback: str = DEFAULT_LOOKBACK) -> PriceData: ...


def _clean(close: pd.DataFrame, volume: pd.DataFrame) -> PriceData:
    """Drop columns with no data, sort, forward-fill short gaps."""
    close = close.sort_index()
    volume = volume.reindex(close.index).sort_index()
    close = close.dropna(axis=1, how="all")
    volume = volume[close.columns]
    close = close.ffill(limit=3)
    volume = volume.fillna(0)
    return PriceData(close=close, volume=volume)


class YFinanceProvider:
    """Batch download from Yahoo Finance via yfinance."""

    name = "yfinance"

    def __init__(self, batch_size: int = 200) -> None:
        self.batch_size = batch_size

    def fetch(self, tickers: Sequence[str], lookback: str = DEFAULT_LOOKBACK) -> PriceData:
        import yfinance as yf  # imported lazily: optional dependency

        closes: list[pd.DataFrame] = []
        volumes: list[pd.DataFrame] = []
        tickers = list(dict.fromkeys(tickers))
        for i in range(0, len(tickers), self.batch_size):
            batch = tickers[i : i + self.batch_size]
            logger.info("yfinance: downloading %d tickers (%d/%d)", len(batch), i, len(tickers))
            raw = yf.download(
                batch,
                period=lookback,
                interval="1d",
                auto_adjust=True,
                group_by="column",
                threads=True,
                progress=False,
            )
            if raw.empty:
                continue
            if isinstance(raw.columns, pd.MultiIndex):
                closes.append(raw["Close"])
                volumes.append(raw["Volume"])
            else:  # single ticker returns flat columns
                closes.append(raw[["Close"]].rename(columns={"Close": batch[0]}))
                volumes.append(raw[["Volume"]].rename(columns={"Volume": batch[0]}))
        if not closes:
            raise RuntimeError("yfinance returned no data for any ticker")
        close = pd.concat(closes, axis=1)
        volume = pd.concat(volumes, axis=1)
        return _clean(close, volume)


class StooqProvider:
    """Per-ticker daily CSV from stooq.com (no key; US tickers use the .us suffix)."""

    name = "stooq"
    URL = "https://stooq.com/q/d/l/?s={symbol}&i=d"

    def __init__(self, timeout: int = 20, session: requests.Session | None = None) -> None:
        self.timeout = timeout
        self.session = session or requests.Session()

    def fetch(self, tickers: Sequence[str], lookback: str = DEFAULT_LOOKBACK) -> PriceData:
        months = int(lookback.rstrip("mo")) if lookback.endswith("mo") else 14
        start = pd.Timestamp.today().normalize() - pd.DateOffset(months=months)
        closes: dict[str, pd.Series] = {}
        volumes: dict[str, pd.Series] = {}
        for t in dict.fromkeys(tickers):
            sym = f"{t.lower().replace('-', '.')}.us"
            try:
                r = self.session.get(self.URL.format(symbol=sym), timeout=self.timeout)
                r.raise_for_status()
                df = pd.read_csv(io.StringIO(r.text), parse_dates=["Date"]).set_index("Date")
            except Exception as exc:
                logger.warning("stooq: %s failed: %s", t, exc)
                continue
            if "Close" not in df or df.empty:
                continue
            df = df[df.index >= start]
            closes[t] = df["Close"]
            volumes[t] = df.get("Volume", pd.Series(0, index=df.index))
        if not closes:
            raise RuntimeError("stooq returned no data for any ticker")
        return _clean(pd.DataFrame(closes), pd.DataFrame(volumes))


class CsvCacheProvider:
    """Load the most recent (or a specific) cached snapshot. Works offline."""

    name = "cache"

    def __init__(self, cache_dir: Path = CACHE_DIR, folder: Path | None = None) -> None:
        self.cache_dir = cache_dir
        self.folder = folder

    def latest_folder(self) -> Path:
        if self.folder is not None:
            return self.folder
        candidates = sorted(self.cache_dir.glob("prices_*"))
        if not candidates:
            raise FileNotFoundError(f"No cached prices under {self.cache_dir}")
        return candidates[-1]

    def fetch(self, tickers: Sequence[str], lookback: str = DEFAULT_LOOKBACK) -> PriceData:
        data = PriceData.load(self.latest_folder())
        keep = [t for t in tickers if t in data.close.columns]
        return PriceData(close=data.close[keep], volume=data.volume[keep])


def fetch_with_fallback(
    tickers: Sequence[str],
    providers: Sequence[PriceProvider],
    lookback: str = DEFAULT_LOOKBACK,
    cache_dir: Path = CACHE_DIR,
    min_coverage: float = 0.8,
) -> tuple[PriceData, str]:
    """Try providers in order; accept the first with adequate ticker coverage.

    Live results are saved to the cache. Returns (data, provider_name).
    """
    errors: list[str] = []
    for provider in providers:
        try:
            data = provider.fetch(tickers, lookback=lookback)
        except Exception as exc:
            errors.append(f"{provider.name}: {exc}")
            logger.warning("provider %s failed: %s", provider.name, exc)
            continue
        coverage = len(data.tickers()) / max(len(tickers), 1)
        if coverage < min_coverage and provider.name != "cache":
            errors.append(f"{provider.name}: coverage {coverage:.0%} < {min_coverage:.0%}")
            logger.warning("provider %s: low coverage %.0f%%", provider.name, coverage * 100)
            continue
        if provider.name != "cache":
            data.save(cache_dir)
        return data, provider.name
    raise RuntimeError("All price providers failed:\n  " + "\n  ".join(errors))
