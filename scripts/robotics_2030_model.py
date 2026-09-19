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


# Base financials from the 19-Sep-2026 research streams and the follow-up data pull.
# Where a figure was NOT FOUND it is marked est. and set conservatively.
ASSUMPTIONS: list[Co] = [
    Co("Lynas", "LYC.AX", "AUD", 14_500, 978, 222, 0.10, 0.25, "all", 0, 0, 0, 22,
       "Robots modelled via HRE volumes, see text; here base business only + HRE premium in growth"),
    Co("MP Materials", "MP", "USD", 9_700, 350, -60, 0.40, 0.20, "all", 3.5 * 120, 0.30, 0.25, 25,
       "3.5 kg NdFeB per robot at $120/kg finished magnet; MP takes 30% of ex-China robot magnets (10X 10kt cap)"),
    Co("Nvidia", "NVDA", "USD", 5_370_000, 300_000, 165_000, 0.20, 0.55, "western", 2_000, 0.85, 0.55, 28,
       "Jetson class $2k per Western robot at 85% share; excludes sim/cloud upsell (immaterial at this scale)"),
    Co("Hengli Hydraulic", "601100.SS", "CNY", 95_000, 12_500, 2_600, 0.08, 0.20, "all", 14 * 150, 0.25, 0.20, 22,
       "14 roller screws per robot at $150 (2030 Chinese price) and 25% share"),
    Co("Schaeffler", "SHA.DE", "EUR", 5_500, 24_000, 200, 0.02, 0.02, "western", 25 * 250, 0.20, 0.10, 12,
       "25 actuator-grade parts per Western robot at $250, 20% share; group margin stays thin"),
    Co("Huachen Precision", "300809.SZ", "CNY", 12_000, 700, 60, 0.15, 0.12, "all", 4.0, 0.25, 0.15, 25,
       "Grinder capex: ~$4 of grinder per robot-year of capacity (28 parts / 50k parts per $1.5M grinder over 7 yrs)"),
    Co("LG Innotek", "011070.KS", "KRW", 4_500_000, 20_000_000, 250_000, 0.03, 0.02, "western", 6 * 40, 0.50, 0.08, 10,
       "6 camera modules at $40 per Western robot, 50% share"),
    Co("Hesai", "HSAI", "USD", 3_500, 480, 40, 0.20, 0.12, "embodied", 120, 0.35, 0.15, 22,
       "One robotics lidar at $120 into the broader embodied pool, 35% share"),
    Co("LG Energy Solution", "373220.KS", "KRW", 95_000_000, 24_000_000, 400_000, 0.08, 0.03, "western", 2.5 * 110, 0.45, 0.06, 15,
       "2.5 kWh pack at $110/kWh cell cost per Western robot, 45% share"),
    Co("Harmonic Drive Systems", "6324.T", "JPY", 548_000, 74_500, 4_500, 0.06, 0.07, "western", 14 * 180, 0.45, 0.15, 25,
       "14 harmonics per Western robot at $180 premium price, 45% share"),
    Co("Tuopu", "601689.SS", "CNY", 108_000, 30_000, 3_300, 0.10, 0.11, "tesla", 28 * 220, 0.60, 0.12, 20,
       "28 actuator assemblies per Tesla robot at $220, 60% share (reported exclusivity)"),
    Co("Leaderdrive", "688017.SS", "CNY", 51_300, 571, 150, 0.15, 0.26, "chinese", 14 * 85, 0.50, 0.28, 30,
       "14 harmonics per Chinese-chain robot at $85 (CNY 600), 50% share"),
    Co("Nabtesco", "6268.T", "JPY", 480_000, 344_000, 20_000, 0.04, 0.06, "all", 2 * 200, 0.25, 0.12, 18,
       "2 mini-RV per robot (hip/waist) at $200, 25% share"),
    Co("Keli Sensing", "603662.SS", "CNY", 18_800, 1_558, 341, 0.12, 0.22, "chinese", 4 * 420, 0.25, 0.20, 25,
       "4 six-axis F/T per Chinese-chain robot at $420 (CNY 3k), 25% share"),
    Co("Allegro", "ALGM", "USD", 6_500, 890, 40, 0.10, 0.12, "all", 100, 0.30, 0.20, 25,
       "$100 of encoders, current sensors and gate drivers per robot, 30% share"),
]


def run(md_path: str | None = None) -> None:
    rows = {s: [c.project(SCENARIOS[s]) for c in ASSUMPTIONS] for s in SCENARIOS}
    lines = ["| Company | Mkt cap $M | Base: 2030 rev $M | Base: robot rev $M | Base: robot % | Base: NI $M | Today's P/E on 2030 NI | Base: implied CAGR | Bear CAGR | Bull CAGR |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(ASSUMPTIONS):
        b, be, bu = rows["base"][i], rows["bear"][i], rows["bull"][i]
        pe = f"{b['pe_today_on_2030']:.0f}x" if b['pe_today_on_2030'] == b['pe_today_on_2030'] else "n/m"
        f = lambda r: f"{r['cagr']*100:+.0f}%" if r['cagr'] == r['cagr'] else "n/m"
        lines.append(f"| {c.name} ({c.ticker}) | {b['mcap_usd_m']:,} | {b['rev_2030']:,} | {b['robo_rev_2030']:,} | {b['robo_share']*100:.0f}% | {b['ni_2030']:,} | {pe} | {f(b)} | {f(be)} | {f(bu)} |")
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
