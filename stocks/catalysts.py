"""Automated catalyst scan: Claude + web search hunting for "next boom" setups.

The price screener (stocks.screener) catches stocks that have *started* moving.
This module looks for the signatures that precede the move, using the same
playbook that would have flagged SanDisk / Micron / Moderna early:

1. "sold out" / "fully allocated" / "lead times extended" in small and mid caps
2. second-tier suppliers raising guidance after a sector leader
3. announced contract price increases
4. dated binary events (trial readouts, FDA decisions, launches) on washed-out charts
5. cluster insider buying

Each theme is one Claude request with the server-side web search tool. Claude
writes a markdown section and a fenced JSON block of candidates; we collect the
candidates, cross-reference them with the latest price screen, and write
reports/stocks/catalysts/latest.md plus a dated copy.

Run: python -m stocks.catalysts --out reports/stocks
Needs ANTHROPIC_API_KEY (or an `ant auth login` profile).
"""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

MODEL = "claude-opus-5"
MAX_SEARCHES_PER_THEME = 12
MAX_CONTINUATIONS = 4  # pause_turn resumes

SYSTEM_PROMPT = """You are a buy-side equity research analyst hunting for stocks that could \
re-rate sharply in the next 3 to 12 months. The historical pattern: a supply-constrained input \
(memory chips, hard drives, transformers) meets a demand shock, prices spike, earnings explode, \
and the multiple re-rates on top. Or a binary event (trial readout, contract award) lands on a \
washed-out stock. Your job is to find the *next* ones before the market reprices them.

Rules:
- Search the web for recent, primary evidence: earnings calls, press releases, trade press, \
regulatory filings. Prefer the last 30 days.
- Name specific listed companies with tickers. Prefer names that have NOT already tripled.
- For each candidate give: ticker, exchange, one-sentence thesis, the concrete evidence with \
a URL, what would confirm the thesis, what would kill it, and how far the stock has already run \
if the sources say.
- Be sceptical: distinguish confirmed facts from rumours, and say when a claim comes from a \
promotional source.
- Never present this as investment advice; it is a research screen.

Output format:
1. A markdown section with a short summary paragraph and a table of candidates.
2. Then a fenced ```json block containing a list of objects with keys: \
ticker, name, exchange, theme, thesis, evidence_url, confirms, kills, already_run (string), \
confidence (low/medium/high). Nothing after the JSON block."""

THEMES: list[dict[str, str]] = [
    {
        "key": "sold_out",
        "title": "Sold-out capacity and stretched lead times",
        "prompt": (
            "Find listed companies (especially small and mid caps) whose latest earnings call or "
            "press release says capacity is sold out, fully allocated, or booked through 2027, or "
            "that lead times have lengthened sharply. Focus on suppliers to AI data centers "
            "(memory, storage, packaging, optics, transformers, switchgear, cooling, power "
            "generation, enrichment) and on industrial bottlenecks generally."
        ),
    },
    {
        "key": "second_tier",
        "title": "Second-tier suppliers raising guidance after the leader",
        "prompt": (
            "Sector leaders like SanDisk, Micron, GE Vernova, and TSMC have already re-rated. "
            "Find the second- and third-tier suppliers in the same supply chains that raised "
            "guidance or reported accelerating revenue in the last quarter but whose shares have "
            "not yet followed: controllers, test equipment, substrates, OSATs, specialty memory, "
            "lasers, transformer and switchgear makers, EMS and ODM names."
        ),
    },
    {
        "key": "price_hikes",
        "title": "Announced contract price increases",
        "prompt": (
            "Find recent announcements of contract or list price increases by listed "
            "manufacturers: memory, NOR flash, hard drives, storage arrays, transformers, "
            "generators, copper and other metals, specialty chemicals, shipping. Identify which "
            "listed companies capture the pricing and whether analysts have raised estimates yet."
        ),
    },
    {
        "key": "binary_events",
        "title": "Dated binary events in the next 120 days",
        "prompt": (
            "List dated binary catalysts in the next 120 days: Phase 3 readouts, PDUFA dates, "
            "pivotal data, first launches, major contract decisions. For each give the company, "
            "ticker, date, what is being decided, the estimated probability of success if any "
            "source gives one, the stock's distance from its 52-week high, and short interest "
            "if reported. Prioritise events where the stock is far below its highs."
        ),
    },
    {
        "key": "insider_buying",
        "title": "Cluster insider buying",
        "prompt": (
            "Find stocks with cluster insider buying (three or more insiders buying on the open "
            "market) or unusually large single insider purchases in the last 30 days, using "
            "sources like OpenInsider, SEC Form 4 coverage, and financial press. Prioritise "
            "companies in bottleneck industries or with upcoming catalysts."
        ),
    },
]

WEB_SEARCH_TOOL = {
    "type": "web_search_20260209",
    "name": "web_search",
    "max_uses": MAX_SEARCHES_PER_THEME,
}


@dataclass
class ThemeResult:
    key: str
    title: str
    text: str
    candidates: list[dict[str, Any]]
    sources: list[str]
    stop_reason: str
    error: str | None = None
    usage: dict[str, int] = field(default_factory=dict)


def build_client():
    """Anthropic client; credentials resolve from env or an `ant auth login` profile."""
    import anthropic  # lazy: optional dependency for the price screener

    return anthropic.Anthropic()


JSON_FENCE = re.compile(r"```json\s*(.*?)```", re.DOTALL | re.IGNORECASE)


def extract_candidates(text: str) -> tuple[str, list[dict[str, Any]]]:
    """Split Claude's answer into prose and the parsed JSON candidate list.

    Tolerates a missing or malformed block (returns an empty list) so one bad
    theme never sinks the whole report.
    """
    m = None
    for m in JSON_FENCE.finditer(text):
        pass  # keep the last fenced block
    if m is None:
        return text.strip(), []
    prose = (text[: m.start()] + text[m.end():]).strip()
    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as exc:
        logger.warning("could not parse candidates JSON: %s", exc)
        return prose, []
    if isinstance(data, dict):
        data = data.get("candidates", [])
    out = []
    for item in data if isinstance(data, list) else []:
        if isinstance(item, dict) and item.get("ticker"):
            item["ticker"] = str(item["ticker"]).upper().strip()
            out.append(item)
    return prose, out


def _collect(message) -> tuple[str, list[str]]:
    """Pull text and cited/search URLs out of a message's content blocks."""
    texts: list[str] = []
    urls: list[str] = []
    for block in message.content:
        btype = getattr(block, "type", None)
        if btype == "text":
            texts.append(block.text)
            for c in getattr(block, "citations", None) or []:
                url = getattr(c, "url", None)
                if url:
                    urls.append(url)
        elif btype == "web_search_tool_result":
            content = block.content
            if isinstance(content, list):  # success: list of web_search_result
                for r in content:
                    url = getattr(r, "url", None)
                    if url:
                        urls.append(url)
            else:  # error object, e.g. max_uses_exceeded
                logger.warning("web search error: %s", getattr(content, "error_code", content))
    return "\n".join(texts), list(dict.fromkeys(urls))


def scan_theme(client, theme: dict[str, str], model: str = MODEL) -> ThemeResult:
    """Run one theme: stream a web-search-enabled request, resuming on pause_turn."""
    user_prompt = f"{theme['prompt']}\n\nToday is {date.today().isoformat()}."
    messages: list[dict[str, Any]] = [{"role": "user", "content": user_prompt}]
    all_text: list[str] = []
    all_urls: list[str] = []
    usage: dict[str, int] = {"input_tokens": 0, "output_tokens": 0}
    stop_reason = ""
    for attempt in range(MAX_CONTINUATIONS + 1):
        with client.beta.messages.stream(
            model=model,
            max_tokens=64000,
            system=[{"type": "text", "text": SYSTEM_PROMPT, "cache_control": {"type": "ephemeral"}}],
            messages=messages,
            tools=[WEB_SEARCH_TOOL],
            output_config={"effort": "high"},
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
        ) as stream:
            message = stream.get_final_message()
        text, urls = _collect(message)
        all_text.append(text)
        all_urls.extend(urls)
        u = getattr(message, "usage", None)
        if u is not None:
            usage["input_tokens"] += getattr(u, "input_tokens", 0) or 0
            usage["output_tokens"] += getattr(u, "output_tokens", 0) or 0
        stop_reason = message.stop_reason or ""
        if stop_reason == "refusal":
            details = getattr(message, "stop_details", None)
            why = getattr(details, "explanation", None) or "no explanation"
            return ThemeResult(theme["key"], theme["title"], "", [], all_urls, stop_reason,
                               error=f"model declined: {why}", usage=usage)
        if stop_reason != "pause_turn":
            break
        # Server-side tool loop paused: resend with the assistant turn appended.
        messages = messages + [{"role": "assistant", "content": message.content}]
        logger.info("theme %s: pause_turn, resuming (%d)", theme["key"], attempt + 1)
    else:
        logger.warning("theme %s: still paused after %d resumes", theme["key"], MAX_CONTINUATIONS)

    prose, candidates = extract_candidates("\n".join(all_text))
    for c in candidates:
        c.setdefault("theme", theme["key"])
    return ThemeResult(theme["key"], theme["title"], prose, candidates,
                       list(dict.fromkeys(all_urls)), stop_reason, usage=usage)


def cross_reference(candidates: list[dict[str, Any]], screen_json: Path) -> None:
    """Annotate candidates with their status in the latest price screen, if present."""
    if not screen_json.exists():
        return
    try:
        payload = json.loads(screen_json.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return
    top = set(payload.get("leaderboard_symbols", []))
    breakout = set(payload.get("breakout_symbols", []))
    for c in candidates:
        t = c["ticker"].replace(".", "-")
        flags = []
        if t in breakout:
            flags.append("on breakout watchlist")
        if t in top:
            flags.append("in Top 100")
        c["screen_status"] = ", ".join(flags) if flags else "not yet moving in screen"


def render_markdown(results: list[ThemeResult], as_of: str, model: str) -> str:
    all_cands = [c for r in results for c in r.candidates]
    lines = [
        f"# Catalyst scan — {as_of}",
        "",
        f"Automated web research by {model} across {len(results)} themes. "
        "Research screen, not advice. Verify every claim at the linked source before acting.",
        "",
    ]
    if all_cands:
        lines += ["## All candidates", "",
                  "| Ticker | Name | Theme | Confidence | Screen status | Thesis |",
                  "|---|---|---|---|---|---|"]
        order = {"high": 0, "medium": 1, "low": 2}
        for c in sorted(all_cands, key=lambda c: order.get(str(c.get("confidence", "")).lower(), 3)):
            thesis = str(c.get("thesis", "")).replace("|", "/").replace("\n", " ")
            url = c.get("evidence_url")
            if url:
                thesis += f" ([source]({url}))"
            lines.append(
                f"| {c['ticker']} | {c.get('name', '')} | {c.get('theme', '')} | "
                f"{c.get('confidence', '')} | {c.get('screen_status', '')} | {thesis} |"
            )
        lines.append("")
    for r in results:
        lines += [f"## {r.title}", ""]
        if r.error:
            lines += [f"_Scan failed: {r.error}_", ""]
            continue
        lines += [r.text, ""]
        if r.sources:
            lines += ["Sources consulted:", ""] + [f"- {u}" for u in r.sources[:25]] + [""]
    total_in = sum(r.usage.get("input_tokens", 0) for r in results)
    total_out = sum(r.usage.get("output_tokens", 0) for r in results)
    lines += ["---", f"_Tokens: {total_in:,} in / {total_out:,} out._", ""]
    return "\n".join(lines)


def run_scan(out_dir: Path, client=None, model: str = MODEL,
             theme_keys: list[str] | None = None) -> tuple[Path, Path]:
    client = client or build_client()
    themes = [t for t in THEMES if not theme_keys or t["key"] in theme_keys]
    results: list[ThemeResult] = []
    for theme in themes:
        logger.info("scanning theme: %s", theme["key"])
        try:
            results.append(scan_theme(client, theme, model=model))
        except Exception as exc:  # one failed theme must not sink the run
            logger.exception("theme %s failed", theme["key"])
            results.append(ThemeResult(theme["key"], theme["title"], "", [], [], "error", error=str(exc)))

    all_cands = [c for r in results for c in r.candidates]
    cross_reference(all_cands, out_dir / "latest.json")

    as_of = date.today().isoformat()
    cat_dir = out_dir / "catalysts"
    cat_dir.mkdir(parents=True, exist_ok=True)
    md = render_markdown(results, as_of, model)
    latest = cat_dir / "latest.md"
    dated = cat_dir / f"{as_of}.md"
    latest.write_text(md, encoding="utf-8")
    dated.write_text(md, encoding="utf-8")
    (cat_dir / "latest.json").write_text(
        json.dumps({"as_of": as_of, "model": model, "candidates": all_cands,
                    "errors": {r.key: r.error for r in results if r.error}}, indent=2),
        encoding="utf-8",
    )
    return latest, dated


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="Claude web-search catalyst scan")
    p.add_argument("--out", default="reports/stocks")
    p.add_argument("--model", default=MODEL)
    p.add_argument("--themes", default="", help="comma-separated theme keys (default: all)")
    p.add_argument("-v", "--verbose", action="store_true")
    args = p.parse_args(argv)
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING,
                        format="%(levelname)s %(name)s: %(message)s")
    keys = [k for k in args.themes.split(",") if k.strip()] or None
    latest, dated = run_scan(Path(args.out), model=args.model, theme_keys=keys)
    print(f"Wrote {latest} and {dated}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
