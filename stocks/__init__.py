"""Stock screener: ranks a universe of equities by performance and momentum.

Pipeline: universe -> prices -> per-ticker metrics -> composite scores ->
Top-100 leaderboard + "breakout watchlist" -> markdown/JSON reports.
Nothing here is investment advice; it is a systematic, reproducible screen.
"""

__all__ = ["universe", "data", "metrics", "screener", "report"]
