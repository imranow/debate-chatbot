import sys, copy, re
sys.path.insert(0, "/home/user/debate-chatbot/scripts")
import robotics_2030_model as m
from dataclasses import replace
S = m.SCENARIOS
A = {c.name: c for c in m.ASSUMPTIONS}
def P(c, s="base"): return c.project(S[s] if isinstance(s,str) else s)
def pct(x): return f"{x*100:+.1f}%"
# 1. note table vs script
note = open("/home/user/debate-chatbot/reports/stocks/research/2026-09-19-robotics/projection-2030.md").read()
rows = [l for l in note.splitlines() if l.startswith("| ") and "|---" not in l]
print("== note table check ==")
for l in rows:
    cells = [x.strip() for x in l.strip("|").split("|")]
    if cells[0] in A and len(cells) == 11:
        c = A[cells[0]]; b = P(c); cr, be, bu = P(c,"crash"), P(c,"bear"), P(c,"bull")
        f = lambda r: f"{r['cagr']*100:+.0f}%"
        exp = [f"{b['mcap_usd_m']:,}", f"{b['rev_2030']:,}", f"{b['robo_rev_2030']:,}", f"{b['robo_share']*100:.0f}%", f"{b['ni_2030']:,}", f"{b['pe_today_on_2030']:.0f}x", f(b), f(cr), f(be), f(bu)]
        diffs = [(i, cells[i+1], e) for i, e in enumerate(exp) if cells[i+1] != e]
        print(cells[0], "OK" if not diffs else diffs)
print("\n== bull robot share (claim: <5% in every scenario) ==")
for n in ["Nabtesco","LG Innotek","LG Energy Solution","Allegro","Sanhua","Tuopu"]:
    print(n, {s: f"{P(A[n],s)['robo_share']*100:.1f}%" for s in S})
print("\n== doubling units 900k->1.8M, CAGR delta (pts) ==")
dbl = {k:(v*2 if k!="embodied_mult" else v) for k,v in S["base"].items()}
for c in m.ASSUMPTIONS:
    print(f"{c.name:24s} {100*(P(c,dbl)['cagr']-P(c)['cagr']):+.1f}")
print("\n== prices 2x (content_usd x2) base CAGR ==")
for n in ["Leaderdrive","Keli Sensing"]:
    print(n, pct(replace(A[n], content_usd=A[n].content_usd*2).project(S["base"])["cagr"]))
print("\n== Tesla 30k / 400k robot share ==")
for t in [30_000, 400_000]:
    sc = dict(S["base"]); sc["tesla_units"] = t
    for n in ["Tuopu","Sanhua"]:
        print(t, n, f"{P(A[n],sc)['robo_share']*100:.1f}%")
print("\n== exit multiple +5 turns effect ==")
for n in ["Leaderdrive","Keli Sensing","Harmonic Drive Systems","Wuzhou Xinchun"]:
    c=A[n]; print(n, c.exit_pe, pct(P(c)['cagr']), "->+5x", pct(replace(c, exit_pe=c.exit_pe+5).project(S['base'])['cagr']))
print("\n== audit sensitivities ==")
L=A["Leaderdrive"]
print("Leaderdrive bear half P/E", pct(replace(L, exit_pe=L.exit_pe/2).project(S["bear"])["cagr"]))
print("Leaderdrive 17%/20x base", pct(replace(L, robot_margin=0.17, exit_pe=20).project(S["base"])["cagr"]))
print("Schaeffler 2% margin", pct(replace(A["Schaeffler"], base_margin_2030=0.02).project(S["base"])["cagr"]))
for cap in [14_000, 14_500, 15_000, 15_540, 15_700]:
    print("Lynas cap A$", cap, pct(replace(A["Lynas"], market_cap_lc=cap).project(S["base"])["cagr"]))
print("Keli at 18.8B", pct(replace(A["Keli Sensing"], market_cap_lc=18_800).project(S["base"])["cagr"]), "at 22.466B", pct(replace(A["Keli Sensing"], market_cap_lc=22_466).project(S["base"])["cagr"]), "at 18.3B", pct(replace(A["Keli Sensing"], market_cap_lc=18_300).project(S["base"])["cagr"]))
print("Leaderdrive at 51.3B", pct(replace(L, market_cap_lc=51_300).project(S["base"])["cagr"]), m.breakeven_units(replace(L, market_cap_lc=51_300)))
print("HDS at 651.3B", pct(replace(A["Harmonic Drive Systems"], market_cap_lc=651_300).project(S["base"])["cagr"]))
print("\n== Nvidia/LG Innotek pools excluding Tesla (Tesla uses AI5 / Semco) ==")
for n in ["Nvidia","LG Innotek"]:
    c=A[n]; b=P(c); print(n, "robot rev", b["robo_rev_2030"], "max possible share of non-Tesla Western", (200_000-120_000)/200_000)
print("\n== grinder pool $ at base ==")
c=A["Huachen Precision"]; print("units", c.units(S["base"]), "pool $M", c.units(S["base"])*c.content_usd/1e6, "all 900k", 900_000*160/1e6, "at $270", 900_000*270/1e6)
print("\n== section 4 text checks ==")
for n in ["Hengli Hydraulic","Harmonic Drive Systems","Leaderdrive","Huachen Precision","Qinchuan Machine Tool","Hesai","Lynas"]:
    c=A[n]; b=P(c); fx=m.FX[c.ccy]
    print(f"{n:24s} rev_lc {b['rev_2030']/fx:,.0f} robo_lc {b['robo_rev_2030']/fx:,.0f} P/E {b['pe_today_on_2030']:.1f} robo% {b['robo_share']*100:.1f}")
print("Nvidia robo%", P(A["Nvidia"])["robo_rev_2030"]/P(A["Nvidia"])["rev_2030"]*100)
print("\n== breakevens ==")
for c in m.ASSUMPTIONS:
    print(f"{c.name:24s}", m.breakeven_units(c,0.0), m.breakeven_units(c,0.10))
print("\n== aggregate robot rev / NI (audit claim $3.1B / $0.67B) ==")
tr = sum(c.project(S['base'])['robo_rev_2030'] for c in m.ASSUMPTIONS)
tn = sum(c.units(S['base'])*c.content_usd*c.share/1e6*c.robot_margin for c in m.ASSUMPTIONS)
print(tr, round(tn))
print("sum mcap ex NVDA", sum(P(c)['mcap_usd_m'] for c in m.ASSUMPTIONS if c.name!='Nvidia'))
print("per Tesla robot $ captured", sum(c.content_usd*c.share for c in m.ASSUMPTIONS if c.pool in ('tesla','western','all')))
