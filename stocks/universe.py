"""Ticker universes for the screener.

The default universe is the S&P 500, pulled from the open-data constituents
CSV maintained on GitHub (no API key needed). Results are cached locally so
offline reruns still work. Extra tickers can be appended via CLI/env.
"""

from __future__ import annotations

import csv
import io
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import requests

SP500_CSV_URL = (
    "https://raw.githubusercontent.com/datasets/s-and-p-500-companies/"
    "main/data/constituents.csv"
)
CACHE_DIR = Path(os.getenv("STOCKS_CACHE_DIR", ".cache/stocks"))


@dataclass(frozen=True)
class Security:
    symbol: str
    name: str
    sector: str = ""
    sub_industry: str = ""


def _normalise_symbol(symbol: str) -> str:
    """Yahoo uses '-' where the S&P list uses '.' (e.g. BRK.B -> BRK-B)."""
    return symbol.strip().upper().replace(".", "-")


def _parse_constituents(text: str) -> list[Security]:
    rows = list(csv.DictReader(io.StringIO(text)))
    out: list[Security] = []
    for r in rows:
        sym = r.get("Symbol") or r.get("symbol")
        if not sym:
            continue
        out.append(
            Security(
                symbol=_normalise_symbol(sym),
                name=(r.get("Security") or r.get("Name") or "").strip(),
                sector=(r.get("GICS Sector") or r.get("Sector") or "").strip(),
                sub_industry=(r.get("GICS Sub-Industry") or "").strip(),
            )
        )
    return out


def load_sp500(cache_dir: Path = CACHE_DIR, timeout: int = 30) -> list[Security]:
    """Fetch the S&P 500 constituents; fall back to the cached copy on failure."""
    cache_dir.mkdir(parents=True, exist_ok=True)
    cache_file = cache_dir / "sp500_constituents.csv"
    try:
        resp = requests.get(SP500_CSV_URL, timeout=timeout)
        resp.raise_for_status()
        text = resp.text
        cache_file.write_text(text, encoding="utf-8")
    except Exception as exc:  # network blocked / offline
        if not cache_file.exists():
            raise RuntimeError(
                f"Could not download S&P 500 list ({exc}) and no cache at {cache_file}"
            ) from exc
        text = cache_file.read_text(encoding="utf-8")
    securities = _parse_constituents(text)
    if len(securities) < 400:
        raise RuntimeError(f"S&P 500 list looks wrong: only {len(securities)} rows")
    return securities


def build_universe(
    base: str = "sp500",
    extra: Iterable[str] = (),
    exclude: Iterable[str] = (),
    cache_dir: Path = CACHE_DIR,
) -> list[Security]:
    """Return the deduplicated screening universe.

    base: "sp500" (default) or "none" (only the extra tickers).
    extra: additional symbols, e.g. high-growth names outside the index.
    """
    if base == "sp500":
        securities = load_sp500(cache_dir=cache_dir)
    elif base == "none":
        securities = []
    else:
        raise ValueError(f"Unknown base universe: {base}")

    seen = {s.symbol for s in securities}
    for sym in extra:
        sym = _normalise_symbol(sym)
        if sym and sym not in seen:
            securities.append(Security(symbol=sym, name=sym))
            seen.add(sym)

    excluded = {_normalise_symbol(s) for s in exclude}
    return [s for s in securities if s.symbol not in excluded]
