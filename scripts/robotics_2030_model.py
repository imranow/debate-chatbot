"""2030 projection model for the robot supply-chain moat map.

Every assumption lives in ASSUMPTIONS below. The model is deliberately simple:

    robotics_revenue_2030 = units_2030 * addressable_share * content_per_robot * company_share
    total_revenue_2030    = base_revenue_2030 + robotics_revenue_2030
    net_income_2030       = base_net_income_2030 + robotics_revenue_2030 * robotics_net_margin
    value_2030            = net_income_2030 * exit_pe
    implied_cagr          = (value_2030 / market_cap_today) ** (1 / years) - 1

Three unit scenarios are run. All money in USD millions unless noted. FX used for
conversion is fixed in FX. Run:  python scripts/robotics_2030_model.py [--md OUT.md]
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict

YEARS = 4.25  # Sep 2026 -> end 2030

# 2030 humanoid units, plus a "broader embodied" multiplier for sensors/compute that
# also sell into quadrupeds, AMRs and service robots.
SCENARIOS = {
    "bear": {"units": 300_000, "western_units": 60_000, "tesla_units": 30_000, "embodied_mult": 3.0},
    "base": {"units": 900_000, "western_units": 200_000, "tesla_units": 120_000, "embodied_mult": 3.0},
    "bull": {"units": 2_500_000, "western_units": 600_000, "tesla_units": 400_000, "embodied_mult": 3.5},
}

FX = {"USD": 1.0, "CNY": 0.14, "JPY": 0.0068, "AUD": 0.66, "EUR": 1.10, "KRW": 0.00073}


@dataclass
class Co:
    name: str
    ticker: str
    ccy: str
    market_cap_lc: float          # local currency, millions
    base_rev_lc: float            # latest FY/TTM revenue, local millions
    base_ni_lc: float             # latest FY/TTM net income, local millions
    base_growth: float            # CAGR of the non-robot business to 2030
    base_margin_2030: float       # net margin of the non-robot business in 2030
    pool: str                     # which unit pool the content is sold into
    content_usd: float            # $ content per robot at 2030 prices
    share: float                  # company share of that content in 2030 (base case)
    robot_margin: float           # net margin on robotics revenue
    exit_pe: float                # multiple on 2030 earnings
    note: str

    def units(self, s: dict) -> float:
        if self.pool == "all":
            return s["units"]
        if self.pool == "western":
            return s["western_units"]
        if self.pool == "tesla":
            return s["tesla_units"]
        if self.pool == "embodied":
            return s["units"] * s["embodied_mult"]
        if self.pool == "chinese":
            return s["units"] - s["western_units"]
        raise ValueError(self.pool)

    def project(self, s: dict, share_mult: float = 1.0) -> dict:
        fx = FX[self.ccy]
        mcap = self.market_cap_lc * fx
        base_rev = self.base_rev_lc * fx * (1 + self.base_growth) ** YEARS
        base_ni = base_rev * self.base_margin_2030
        robo_rev = self.units(s) * self.content_usd * min(1.0, self.share * share_mult) / 1e6
        robo_ni = robo_rev * self.robot_margin
        ni = base_ni + robo_ni
        value = ni * self.exit_pe
        cagr = (value / mcap) ** (1 / YEARS) - 1 if mcap > 0 and value > 0 else float("nan")
        return {
            "name": self.name, "ticker": self.ticker,
            "mcap_usd_m": round(mcap), "rev_2030": round(base_rev + robo_rev),
            "robo_rev_2030": round(robo_rev), "robo_share": robo_rev / (base_rev + robo_rev),
            "ni_2030": round(ni), "value_2030": round(value), "pe_today_on_2030": mcap / ni if ni > 0 else float("nan"),
            "cagr": cagr,
        }


# Base financials: market caps and latest-year figures from the 19-Sep-2026 data pull
# (stockanalysis, companiesmarketcap, PitchBook, company releases; see raw/07-financials.md).
# Local-currency millions. Where two sites conflicted the lower figure is used.
ASSUMPTIONS: list[Co] = [
    Co("Lynas", "LYC.AX", "AUD", 10_900, 978, 222, 0.10, 0.25, "western", 0.105 * 1_500, 0.70, 0.35, 22,
       "0.105 kg Dy/Tb per robot (3% of a 3.5 kg magnet set) at $1,500/kg ex-China; 70% of ex-China robot HRE"),
    Co("MP Materials", "MP", "USD", 9_730, 433, -65, 0.30, 0.20, "western", 3.5 * 120, 0.40, 0.25, 25,
       "Base = 2026 consensus revenue $433M growing 30% as 10X ramps; 3.5 kg NdFeB at $120/kg, 40% of ex-China robot magnets"),
    Co("Nvidia", "NVDA", "USD", 5_310_000, 411_000, 226_000, 0.15, 0.55, "western", 2_000, 0.85, 0.55, 28,
       "Base = FY27 consensus $411B growing 15%; Jetson-class $2k per Western robot at 85% share (physical-AI cloud upsell excluded)"),
    Co("Hengli Hydraulic", "601100.SS", "CNY", 132_780, 11_730, 2_770, 0.08, 0.22, "all", 14 * 150, 0.25, 0.20, 22,
       "14 roller screws per robot at $150 (2030 Chinese price), 25% global share"),
    Co("Wuzhou Xinchun", "603667.SS", "CNY", 14_270, 3_343, 91, 0.03, 0.03, "tesla", 30 * 120, 0.50, 0.15, 20,
       "30 screws (leg inverted PRS + hand ball screws) per Tesla robot at $120, 50% share"),
    Co("Schaeffler", "SHA.DE", "EUR", 6_830, 24_700, 0, 0.02, 0.03, "western", 25 * 250, 0.20, 0.10, 10,
       "25 actuator-grade parts per Western robot at $250, 20% share; group margin recovers to 3% (consensus EPS EUR0.88)"),
    Co("Huachen Precision", "300809.SZ", "CNY", 6_400, 525, 60, 0.12, 0.12, "all", 270, 0.15, 0.15, 25,
       "Grinder capex ~$270 per robot-year (28 parts / 30k parts per $1.2M grinder, 7-yr life); 15% share"),
    Co("Qinchuan Machine Tool", "000837.SZ", "CNY", 9_140, 4_190, 50, 0.05, 0.03, "all", 270, 0.15, 0.12, 20,
       "Same grinder-capex pool, 15% share; base business is low-margin machine tools"),
    Co("LG Innotek", "011070.KS", "KRW", 12_160_000, 22_450_000, 485_000, 0.03, 0.025, "western", 6 * 40, 0.50, 0.08, 10,
       "6 camera modules at $40 per Western robot, 50% share"),
    Co("Hesai", "HSAI", "USD", 2_920, 491, 73, 0.18, 0.13, "embodied", 120, 0.35, 0.15, 22,
       "Base grows 18% (2027 consensus $987M); one robotics lidar at $120 into the broader embodied pool, 35% share"),
    Co("LG Energy Solution", "373220.KS", "KRW", 94_650_000, 23_670_000, -1_073_000, 0.08, 0.04, "western", 2.5 * 110, 0.45, 0.06, 15,
       "2.5 kWh pack at $110/kWh per Western robot, 45% share; base margin recovers to 4%"),
    Co("Harmonic Drive Systems", "6324.T", "JPY", 651_300, 74_500, 5_900, 0.06, 0.08, "western", 14 * 180, 0.45, 0.15, 25,
       "Base = FY3/27 guide; 14 harmonics per Western robot at $180 premium price, 45% share"),
    Co("Tuopu", "601689.SS", "CNY", 100_000, 29_580, 2_780, 0.10, 0.10, "tesla", 14 * 250, 0.60, 0.12, 20,
       "14 linear actuator assemblies per Tesla robot at $250, 60% share (reported exclusivity)"),
    Co("Sanhua", "002050.SZ", "CNY", 197_540, 31_010, 4_060, 0.09, 0.13, "tesla", 14 * 250, 0.60, 0.12, 20,
       "14 rotary joint modules per Tesla robot at $250, 60% share (reported)"),
    Co("Leaderdrive", "688017.SS", "CNY", 53_280, 571, 141, 0.15, 0.26, "chinese", 14 * 85, 0.50, 0.28, 30,
       "14 harmonics per Chinese-chain robot at $85, 50% share"),
    Co("Nabtesco", "6268.T", "JPY", 602_490, 309_700, 18_440, 0.04, 0.06, "all", 2 * 200, 0.25, 0.12, 18,
       "2 mini-RV per robot (hip/waist) at $200, 25% share"),
    Co("Keli Sensing", "603662.SS", "CNY", 20_000, 1_558, 341, 0.12, 0.22, "chinese", 4 * 420, 0.25, 0.20, 25,
       "4 six-axis F/T per Chinese-chain robot at $420, 25% share"),
    Co("Allegro", "ALGM", "USD", 10_980, 890, 100, 0.10, 0.14, "all", 100, 0.30, 0.20, 25,
       "$100 of encoders, current sensors and gate drivers per robot, 30% share; base NI = non-GAAP"),
]


def breakeven_units(c: Co, target_cagr: float = 0.0) -> float | None:
    """2030 humanoid units (all pools scaled from the base scenario) at which the
    implied CAGR equals target_cagr. None if no volume up to 20M units gets there."""
    base = SCENARIOS["base"]
    lo, hi = 0.0, 20_000_000.0
    def cagr_at(u: float) -> float:
        k = u / base["units"]
        sc = {kk: (v * k if kk != "embodied_mult" else v) for kk, v in base.items()}
        r = c.project(sc)["cagr"]
        return r if r == r else -1.0
    if cagr_at(hi) < target_cagr:
        return None
    if cagr_at(lo) >= target_cagr:
        return 0.0
    for _ in range(60):
        mid = (lo + hi) / 2
        if cagr_at(mid) < target_cagr:
            lo = mid
        else:
            hi = mid
    return hi


def run(md_path: str | None = None) -> None:
    rows = {s: [c.project(SCENARIOS[s]) for c in ASSUMPTIONS] for s in SCENARIOS}
    lines = ["| Company | Mkt cap $M | Base: 2030 rev $M | Base: robot rev $M | Base: robot % | Base: NI $M | Today's P/E on 2030 NI | Base: implied CAGR | Bear CAGR | Bull CAGR |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(ASSUMPTIONS):
        b, be, bu = rows["base"][i], rows["bear"][i], rows["bull"][i]
        pe = f"{b['pe_today_on_2030']:.0f}x" if b['pe_today_on_2030'] == b['pe_today_on_2030'] else "n/m"
        f = lambda r: f"{r['cagr']*100:+.0f}%" if r['cagr'] == r['cagr'] else "n/m"
        lines.append(f"| {c.name} ({c.ticker}) | {b['mcap_usd_m']:,} | {b['rev_2030']:,} | {b['robo_rev_2030']:,} | {b['robo_share']*100:.0f}% | {b['ni_2030']:,} | {pe} | {f(b)} | {f(be)} | {f(bu)} |")
    lines.append("")
    lines.append("| Company | 2030 units needed for 0% CAGR at today's price | for +10% CAGR |")
    lines.append("|---|---|---|")
    for c in ASSUMPTIONS:
        b0, b10 = breakeven_units(c, 0.0), breakeven_units(c, 0.10)
        fmt = lambda u: "n/a (base business alone)" if u == 0 else ("never below 20M" if u is None else f"{u/1e6:.1f}M")
        lines.append(f"| {c.name} | {fmt(b0)} | {fmt(b10)} |")
    out = "\n".join(lines)
    print(out)
    if md_path:
        with open(md_path, "w") as fh:
            fh.write(out + "\n\n## Assumptions\n\n| Company | Pool | Content/robot $ | Share | Robot net margin | Base growth | Base margin 2030 | Exit P/E | Note |\n|---|---|---|---|---|---|---|---|---|\n")
            for c in ASSUMPTIONS:
                fh.write(f"| {c.name} | {c.pool} | {c.content_usd:,.0f} | {c.share*100:.0f}% | {c.robot_margin*100:.0f}% | {c.base_growth*100:.0f}% | {c.base_margin_2030*100:.0f}% | {c.exit_pe:.0f}x | {c.note} |\n")
            fh.write("\n## Scenarios\n\n" + json.dumps(SCENARIOS, indent=2) + "\n")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--md")
    run(ap.parse_args().md)
