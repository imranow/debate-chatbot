"""Render workflow research output (dossiers + verification sweep) into Notion-flavored markdown.

Usage: python scripts/render_notion_dossiers.py dossiers.json [sweep.json] > page.md
"""
from __future__ import annotations

import json
import re
import sys
from collections import OrderedDict

TIERS = OrderedDict([
    ("Tier 1: sold-out bottlenecks (the SanDisk / Micron pattern)",
     ["SIMO", "2344", "2337", "2408", "AMKR", "ASX", "HPS.A", "POWL", "LEU", "MOD", "NVT", "CAT", "LITE", "BE"]),
    ("Tier 2: volume beneficiaries and pricing-power laggards (the Dell pattern)",
     ["CLS", "JBL", "NTAP", "PSTG", "CLSK", "CORZ", "APLD", "BTDR"]),
    ("Tier 3: dated binary events (the Moderna pattern)",
     ["GOSS", "INO", "CYBN", "RKLB", "ASTS", "RGNX"]),
    ("Tier 4: commodity and materials squeezes",
     ["SCCO", "TECK", "HBM", "ERO", "HL", "PAAS", "AG", "CDE", "MP", "USAR", "UUUU", "CCJ"]),
])
EXCHANGE_PREFIX = {"TWSE": "TWSE:", "TSX": "TSX:"}


def esc(s) -> str:
    if s is None:
        return ""
    s = str(s)
    return re.sub(r"([\\*~`$\[\]<>{}|^])", r"\\\1", s)


def trim(text, n: int) -> str:
    """Cut long agent prose at a sentence boundary near n chars."""
    if text is None:
        return ""
    t = str(text).strip()
    if len(t) <= n:
        return t
    cut = t[:n]
    for sep in (". ", "; ", ", "):
        i = cut.rfind(sep)
        if i > n * 0.5:
            return cut[: i + 1].rstrip(",;") + (" …" if sep != ". " else "")
    return cut.rstrip() + " …"

LIMITS = {"business": 450, "why_now": 900, "analogue": 450, "guidance": 400, "valuation": 500,
          "price_action": 400, "balance_sheet": 400, "bull_case": 700, "bear_case": 700,
          "what_confirms": 350, "what_kills": 350, "how_far_run_note": 300, "market_cap": 160,
          "summary": 500, "priced_in": 500, "durability": 500, "evidence_quality": 500, "one_line": 250}


def T(d: dict, key: str) -> str:
    return trim((d or {}).get(key, ""), LIMITS.get(key, 500))


def link(url: str, text: str | None = None) -> str:
    url = str(url).strip()
    if not url.startswith("http"):
        return esc(url)
    t = esc(text) if text else esc(url.replace("https://", "").replace("http://", "")[:70])
    return f"[{t}]({url})"


def display_ticker(d: dict, inp: dict) -> str:
    t = str(inp.get("ticker") or d.get("ticker") or "").upper()
    t = re.sub(r"\.(TW|TWO|T|KS|KQ|TO|HK|L|DE|PA|AS)$", "", t)
    ex = str(inp.get("exchange") or d.get("exchange") or "")
    for k, p in EXCHANGE_PREFIX.items():
        if ex.upper().startswith(k):
            return p + t
    return t


def table(headers, rows, fit=True):
    out = [f'<table fit-page-width="{"true" if fit else "false"}" header-row="true">']
    out.append("\t<tr>" + "".join(f"<td>{esc(h)}</td>" for h in headers) + "</tr>")
    for r in rows:
        out.append("\t<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>")
    out.append("</table>")
    return "\n".join(out)


def bullet(label, text):
    text = esc(text).strip()
    return f"- **{esc(label)}:** {text}" if text else ""


def render_dossier(entry: dict, sweep_index: dict) -> str:
    inp, d, s = entry.get("input", {}), entry.get("dossier"), entry.get("skeptic")
    tick = display_ticker(d or {}, inp)
    name = (d or {}).get("name") or inp.get("name", "")
    lines = []
    if not d:
        lines.append(f"### {esc(name)} ({esc(tick)})")
        lines.append(f"_Full dossier in progress (re-running after the usage-limit reset). Working thesis: {esc(inp.get('thesis', ''))}_")
        return "\n".join(lines)

    verdict = (s or {}).get("verdict", "no skeptic pass")
    colour = {"compelling": "green_bg", "interesting": "blue_bg", "weak": "yellow_bg", "avoid": "red_bg"}.get(verdict, "gray_bg")
    run = d.get("how_far_run", "unknown")
    lines.append(f"### {esc(name)} ({esc(tick)}) {{toggle=\"true\"}}")
    hdr = (f"\t<callout icon=\"📌\" color=\"{colour}\">\n"
           f"\t\t**Skeptic verdict: {esc(verdict)}.** {esc(T(s, 'one_line'))}\n"
           f"\t\t**How far it has run:** {esc(run)}. {esc(T(d, 'how_far_run_note'))}\n"
           f"\t\t**Risk:** {esc(d.get('risk_rating', ''))} · **Sizing:** {esc(d.get('suggested_sizing', ''))} · "
           f"**Analyst confidence:** {esc(d.get('confidence', ''))}\n"
           f"\t</callout>")
    lines.append(hdr)
    facts = [
        ("Exchange / market cap", f"{esc(inp.get('exchange') or d.get('exchange', ''))} · {esc(T(d, 'market_cap'))}"),
        ("Business", esc(T(d, "business"))),
        ("Why now", esc(T(d, "why_now"))),
        ("2026 analogue", esc(T(d, "analogue"))),
        ("Guidance", esc(T(d, "guidance"))),
        ("Valuation", esc(T(d, "valuation"))),
        ("Price action", esc(T(d, "price_action"))),
        ("Balance sheet", esc(T(d, "balance_sheet"))),
    ]
    for label, txt in facts:
        if txt.strip(" ·"):
            lines.append(f"\t- **{label}:** {txt}")
    nums = (d.get("latest_numbers") or [])[:10]
    if nums:
        lines.append("\t**Latest numbers**")
        rows = []
        for n in nums:
            src = n.get("source_url")
            rows.append([esc(trim(n.get("metric"), 60)), esc(trim(n.get("value"), 170)), esc(trim(n.get("period"), 60)),
                         link(src, "source") if src and str(src).startswith("http") else ""])
        lines.append("\t" + table(["Metric", "Value", "Period", "Source"], rows).replace("\n", "\n\t"))
    cats = (d.get("catalysts") or [])[:8]
    if cats:
        lines.append("\t**Dated catalysts**")
        rows = []
        for c in cats:
            src = c.get("source_url")
            rows.append([esc(trim(c.get("date"), 40)), esc(trim(c.get("event"), 200)),
                         link(src, "source") if src and str(src).startswith("http") else ""])
        lines.append("\t" + table(["Date", "Event", "Source"], rows).replace("\n", "\n\t"))
    lines.append(f"\t- **Bull case:** {esc(T(d, 'bull_case'))}")
    lines.append(f"\t- **Bear case:** {esc(T(d, 'bear_case'))}")
    lines.append(f"\t- **What confirms:** {esc(T(d, 'what_confirms'))}")
    lines.append(f"\t- **What kills it:** {esc(T(d, 'what_kills'))}")
    if s:
        lines.append("\t**Skeptic's review**")
        lines.append(f"\t- **Priced in?** {esc(T(s, 'priced_in'))}")
        lines.append(f"\t- **Durable?** {esc(T(s, 'durability'))}")
        lines.append(f"\t- **Evidence quality:** {esc(T(s, 'evidence_quality'))}")
        for c in s.get("corrections") or []:
            lines.append(f"\t- <span color=\"orange\">Correction:</span> {esc(trim(c, 250))}")
    sw = sweep_index.get(str(d.get("ticker") or inp.get("ticker")).upper())
    if sw:
        status = "survived" if sw.get("survives") else "REFUTED"
        lines.append(f"\t**Independent 3-lens verification ({status})**")
        for v in sw.get("votes") or []:
            lines.append(f"\t- {esc(v.get('lens'))}: {'refuted' if v.get('refuted') else 'held'}. {esc(trim(v.get('reason', ''), 300))}")
    unv = d.get("unverified_claims") or []
    if unv:
        lines.append("\t<details>\n\t<summary>Unverified claims</summary>")
        for u in unv[:5]:
            lines.append(f"\t- {esc(trim(u, 200))}")
        lines.append("\t</details>")
    srcs = list(dict.fromkeys((d.get("sources") or []) + ((s or {}).get("sources") or [])))
    if srcs:
        lines.append("\t<details>\n\t<summary>Sources</summary>")
        for u in srcs[:10]:
            lines.append(f"\t- {link(u)}")
        lines.append("\t</details>")
    return "\n".join(l for l in lines if l is not None)


def render_calendar(dossiers):
    rows = []
    for e in dossiers:
        d = e.get("dossier")
        if not d:
            continue
        tick = display_ticker(d, e.get("input", {}))
        for c in d.get("catalysts") or []:
            rows.append((str(c.get("date", ""))[:40], tick, esc(trim(c.get("event", ""), 160)), c.get("source_url")))
    rows.sort(key=lambda r: r[0])
    return table(["Date", "Ticker", "Event", "Source"],
                 [[esc(r[0]), esc(r[1]), r[2], link(r[3], "source") if r[3] and str(r[3]).startswith("http") else ""] for r in rows])


def render_miners(ms):
    if not ms or not ms.get("miners"):
        return "_Miner screen unavailable._"
    rows = []
    for m in ms["miners"]:
        rows.append([esc(m.get("ticker")), esc(m.get("name")), esc(m.get("total_mw")), esc(m.get("contracted_mw")),
                     esc(m.get("uncontracted_mw")), esc(m.get("market_cap", "")), esc(m.get("ev_per_mw", "")),
                     esc(m.get("notes")),
                     link(m.get("source_url"), "source") if m.get("source_url") and str(m.get("source_url")).startswith("http") else ""])
    out = [table(["Ticker", "Name", "Total MW", "Contracted MW", "Uncontracted MW", "Mkt cap", "EV/MW", "Notes", "Src"], rows)]
    if ms.get("method"):
        out.append(f"_Method: {esc(ms['method'])}_")
    return "\n".join(out)


def render_sweep_sections(sweep):
    if not sweep:
        return ""
    lines = []
    st = sweep.get("stats") or {}
    lines.append("## Independent verification sweep")
    lines.append(esc(f"18 finder agents (plus {st.get('finders_round2', 0)} critic-proposed angles) surfaced "
                     f"{st.get('unique_candidates', '?')} unique candidates; {st.get('excluded_already_boomed', 0)} already-boomed "
                     f"names were excluded; each remaining candidate was deep-read and attacked by three refuters "
                     f"(priced-in, durability, evidence). {st.get('survivors', '?')} survived, {st.get('rejected', '?')} were rejected."))
    picks = sweep.get("top_picks") or []
    if picks:
        lines.append("**Top picks from the sweep**")
        lines.append(table(["Ticker", "Tier", "Why"], [[esc(p.get("ticker")), esc(p.get("tier")), esc(p.get("one_line"))] for p in picks]))
    surv = sweep.get("survivors") or []
    if surv:
        lines.append("### Survivors not in the dossier set {toggle=\"true\"}")
        rows = []
        for s_ in surv:
            deep = s_.get("deep") or {}
            rows.append([esc(s_.get("ticker")), esc(s_.get("name")), esc(", ".join(s_.get("themes") or [])),
                         esc(T(deep, "summary")), esc(deep.get("ytd_move", "")), esc(deep.get("next_catalyst", ""))])
        lines.append("\t" + table(["Ticker", "Name", "Themes", "Summary", "Move", "Next catalyst"], rows).replace("\n", "\n\t"))
    rej = sweep.get("rejected") or []
    if rej:
        lines.append("### Rejected by the refuters, and why {toggle=\"true\"}")
        rows = []
        for r in rej:
            reasons = [f"{v.get('lens')}: {v.get('reason')}" for v in (r.get("votes") or []) if v.get("refuted")]
            rows.append([esc(r.get("ticker")), esc(r.get("name")), esc(" / ".join(reasons)[:600] or r.get("note", ""))])
        lines.append("\t" + table(["Ticker", "Name", "Refutation"], rows).replace("\n", "\n\t"))
    if sweep.get("report_markdown"):
        lines.append("### Sweep synthesis note (verbatim) {toggle=\"true\"}")
        for l in str(sweep["report_markdown"]).splitlines():
            conv = convert_md_line(l) if l.strip() else ""
            if conv.strip():
                lines.append("\t" + conv)
    return "\n".join(lines)


def convert_md_line(l: str) -> str:
    """Best-effort: keep headings/bullets, escape the rest, drop pipe tables into plain text."""
    if l.startswith("|"):
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        if all(re.match(r"^:?-+:?$", c) for c in cells if c):
            return ""
        return "- " + " · ".join(esc_keep_links(c) for c in cells if c)
    m = re.match(r"^(#{1,4})\s+(.*)", l)
    if m:
        return "**" + esc(m.group(2)) + "**"
    m = re.match(r"^(\s*)[-*]\s+(.*)", l)
    if m:
        return "- " + esc_keep_links(m.group(2))
    m = re.match(r"^(\s*)(\d+)\.\s+(.*)", l)
    if m:
        return f"{m.group(2)}. " + esc_keep_links(m.group(3))
    return esc_keep_links(l)


def esc_keep_links(s: str) -> str:
    parts = re.split(r"(\[[^\]]*\]\((https?://[^)]*)\))", s)
    out = []
    i = 0
    while i < len(parts):
        p = parts[i]
        if re.match(r"^\[[^\]]*\]\(https?://[^)]*\)$", p):
            m = re.match(r"^\[([^\]]*)\]\((https?://[^)]*)\)$", p)
            out.append(f"[{esc(m.group(1))}]({m.group(2)})")
            i += 2  # skip the captured url group
        else:
            out.append(re.sub(r"([\\~`$\[\]<>{}|^])", r"\\\1", p))  # keep * for bold
            i += 1
    return "".join(out)


def summary_table(entries, sweep_index):
    rows = []
    for tier, ticks in TIERS.items():
        short = tier.split(":")[0]
        for t in ticks:
            e = next((x for x in entries if str(x.get("input", {}).get("ticker", "")).upper() == t), None)
            if not e:
                continue
            d, s_ = e.get("dossier"), e.get("skeptic")
            tick = display_ticker(d or {}, e.get("input", {}))
            if not d:
                rows.append([esc(tick), esc(e["input"].get("name", "")), esc(short), "in progress", "", "", ""])
                continue
            verdict = (s_ or {}).get("verdict", "pending")
            one = T(s_, "one_line") if s_ else trim(d.get("how_far_run_note", ""), 220)
            rows.append([esc(tick), esc(d.get("name") or e["input"].get("name", "")), esc(short), esc(verdict),
                         esc(d.get("how_far_run", "")), esc(d.get("risk_rating", "")) + " · " + esc(trim(d.get("suggested_sizing", ""), 60)), esc(one)])
    return table(["Ticker", "Name", "Tier", "Skeptic", "How far run", "Risk · sizing", "One line"], rows)


def render_split(entries, sweep, framework, outdir, extra_main=""):
    """Write main.md plus tier1..4.md so each Notion page stays a readable size."""
    import os
    os.makedirs(outdir, exist_ok=True)
    sweep_index = {}
    if sweep:
        for s_ in (sweep.get("survivors") or []):
            sweep_index[str(s_.get("ticker")).upper()] = dict(s_, survives=True)
        for r in (sweep.get("rejected") or []):
            sweep_index[str(r.get("ticker")).upper()] = dict(r, survives=False)
    by_ticker = {str(e.get("input", {}).get("ticker", "")).upper(): e for e in entries}
    main = [framework.rstrip(), "## Summary of all names", summary_table(entries, sweep_index),
            "## Binary-event calendar (all dossiers)", render_calendar(entries),
            "## Full dossiers by tier", "{{TIER_LINKS}}"]
    if sweep:
        covered = set(by_ticker)
        sw = dict(sweep)
        sw["survivors"] = [s_ for s_ in (sweep.get("survivors") or []) if str(s_.get("ticker")).upper() not in covered]
        main.append(render_sweep_sections(sw))
    if extra_main:
        main.append(extra_main)
    open(os.path.join(outdir, "main.md"), "w").write("\n".join(m for m in main if m))
    for i, (tier, ticks) in enumerate(TIERS.items(), 1):
        out = [f"*{esc(tier)}. Open each toggle for the full dossier. Back to the main page for the summary table and calendar.*"]
        for t in ticks:
            e = by_ticker.get(t)
            if e:
                out.append(render_dossier(e, sweep_index))
        if tier.startswith("Tier 2"):
            out.append("### Next miner to sign: uncontracted-megawatt screen {toggle=\"true\"}")
            out.append("\t" + render_miners((sweep or {}).get("miner_screen") or MINERS_HOLDER.get("miner_screen")).replace("\n", "\n\t"))
        open(os.path.join(outdir, f"tier{i}.md"), "w").write("\n".join(out))
        print(f"tier{i}.md: {sum(len(x) for x in out)} chars", file=sys.stderr)


MINERS_HOLDER = {}


def main():
    if sys.argv[1] == "--split":
        dossiers = json.load(open(sys.argv[2]))
        MINERS_HOLDER["miner_screen"] = dossiers.get("miner_screen")
        sweep = json.load(open(sys.argv[3])) if sys.argv[3] not in ("", "-", "/dev/null") else None
        framework = open(sys.argv[4]).read()
        extra = open(sys.argv[6]).read() if len(sys.argv) > 6 else ""
        render_split(dossiers.get("dossiers") or [], sweep, framework, sys.argv[5], extra)
        return
    dossiers = json.load(open(sys.argv[1]))
    sweep = json.load(open(sys.argv[2])) if len(sys.argv) > 2 and sys.argv[2] not in ("", "-", "/dev/null") else None
    framework = open(sys.argv[3]).read() if len(sys.argv) > 3 else ""
    entries = dossiers.get("dossiers") or []
    by_ticker = {str(e.get("input", {}).get("ticker", "")).upper(): e for e in entries}
    sweep_index = {}
    if sweep:
        for s_ in (sweep.get("survivors") or []):
            sweep_index[str(s_.get("ticker")).upper()] = dict(s_, survives=True)
        for r in (sweep.get("rejected") or []):
            sweep_index[str(r.get("ticker")).upper()] = dict(r, survives=False)

    out = []
    out.append(framework.rstrip())
    out.append("## Binary-event calendar (all dossiers)")
    out.append(render_calendar(entries))
    for tier, ticks in TIERS.items():
        out.append(f"## {esc(tier)}")
        for t in ticks:
            e = by_ticker.get(t)
            if e:
                out.append(render_dossier(e, sweep_index))
        if tier.startswith("Tier 2"):
            out.append("### Next miner to sign: uncontracted-megawatt screen {toggle=\"true\"}")
            out.append("\t" + render_miners(dossiers.get("miner_screen")).replace("\n", "\n\t"))
    covered = set(by_ticker)
    for t, e in by_ticker.items():
        if not any(t in v for v in TIERS.values()):
            out.append(render_dossier(e, sweep_index))
    if sweep:
        # remove dossier-covered tickers from the survivors table to avoid duplication
        sweep = dict(sweep)
        sweep["survivors"] = [s_ for s_ in (sweep.get("survivors") or []) if str(s_.get("ticker")).upper() not in covered]
        out.append(render_sweep_sections(sweep))
    print("\n".join(o for o in out if o))


if __name__ == "__main__":
    main()
