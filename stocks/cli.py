"""CLI: python -m stocks.cli [--out reports/stocks] [--extra TSLA,PLTR] [--offline]"""

from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

import pandas as pd

from .data import CsvCacheProvider, PriceProvider, StooqProvider, YFinanceProvider, fetch_with_fallback
from .metrics import metrics_table
from .report import write_reports
from .screener import run_screen
from .universe import build_universe


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Top-100 stock performance + breakout screener")
    p.add_argument("--out", default="reports/stocks", help="output directory")
    p.add_argument("--universe", default="sp500", choices=["sp500", "none"])
    p.add_argument("--extra", default="", help="comma-separated extra tickers")
    p.add_argument("--exclude", default="", help="comma-separated tickers to skip")
    p.add_argument("--top", type=int, default=100)
    p.add_argument("--breakouts", type=int, default=25)
    p.add_argument("--lookback", default="14mo")
    p.add_argument("--offline", action="store_true", help="use cached prices only")
    p.add_argument("--provider", default="auto", choices=["auto", "yfinance", "stooq", "cache"])
    p.add_argument("-v", "--verbose", action="store_true")
    return p.parse_args(argv)


def providers_for(choice: str, offline: bool) -> list[PriceProvider]:
    if offline or choice == "cache":
        return [CsvCacheProvider()]
    if choice == "yfinance":
        return [YFinanceProvider(), CsvCacheProvider()]
    if choice == "stooq":
        return [StooqProvider(), CsvCacheProvider()]
    return [YFinanceProvider(), StooqProvider(), CsvCacheProvider()]


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format="%(levelname)s %(name)s: %(message)s",
    )
    extra = [t for t in args.extra.split(",") if t.strip()]
    exclude = [t for t in args.exclude.split(",") if t.strip()]

    universe = build_universe(base=args.universe, extra=extra, exclude=exclude)
    tickers = [s.symbol for s in universe]
    meta = pd.DataFrame(
        {"name": [s.name for s in universe], "sector": [s.sector for s in universe]},
        index=pd.Index(tickers, name="symbol"),
    )
    print(f"Universe: {len(tickers)} tickers", file=sys.stderr)

    data, provider = fetch_with_fallback(tickers, providers_for(args.provider, args.offline), args.lookback)
    as_of = data.close.index[-1].date().isoformat()
    print(f"Prices: {len(data.tickers())} tickers via {provider}, as of {as_of}", file=sys.stderr)

    metrics = metrics_table(data.close, data.volume)
    result = run_screen(metrics, meta=meta, as_of=as_of, provider=provider,
                        top_n=args.top, breakout_n=args.breakouts)
    md, js, hist = write_reports(result, Path(args.out))
    print(f"Wrote {md}, {js}, {hist}", file=sys.stderr)

    top10 = result.leaderboard.head(10)
    print("\nTop 10 performers:")
    for sym, r in top10.iterrows():
        print(f"  {int(r['perf_rank']):3d}. {sym:<6} 6m {r['ret_6m']*100:+6.1f}%  12m {r.get('ret_12m', float('nan'))*100:+6.1f}%  score {r['perf_score']:.0f}")
    print("\nBreakout watchlist (top 10):")
    for sym, r in result.breakouts.head(10).iterrows():
        print(f"  {int(r['breakout_rank']):3d}. {sym:<6} 1m {r['ret_1m']*100:+6.1f}%  score {r['breakout_score']:.0f}  [{', '.join(r['signals'])}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
