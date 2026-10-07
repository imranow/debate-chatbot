"""
HIMS 2030 first-principles valuation model (stream 01).

As of 7 Oct 2026. All scenario inputs are ESTIMATES unless noted as reported.
Chain: subscribers x annual revenue per subscriber -> revenue
       x adj. EBITDA margin -> EBITDA
       x exit EV/EBITDA -> enterprise value (end-2030)
       - net debt (end-2030) -> equity value
       / diluted shares -> value per share
       -> implied annual return from today's price.

Run: python3 01-valuation_model.py
"""
from dataclasses import dataclass, replace

# ---------------------------------------------------------------- starting point
PRICE_NOW = 29.40          # ~6 Oct 2026 snapshot, Yahoo/StockAnalysis $29.28-29.47 (unverified, snippet)
VAL_DATE_YEARS = 4.23      # 7 Oct 2026 -> 31 Dec 2030 = 4 years + 85 days (estimate of horizon)
SHARES_NOW = 224.94 + 8.38  # M; Class A 224,935,790 (Form 144, 16 Sep 2026) + Class V 8,377,623 (proxy, Apr 2026)
CASH_NOW = 841.0           # $M cash + ST investments, 30 Jun 2026 (reported, snippet)
NOTES_2030 = 1000.0        # $M 0% converts due 15 May 2030, conv. price $70.67 (reported)
CONV_2030 = 70.67
NOTES_2032 = 402.5         # $M 0% converts due 2032, conv. price $29.53 (reported)
CONV_2032 = 29.53
EUCA_DEFERRED = 710.0      # $M Eucalyptus deferred consideration, 6 quarterly installments (reported terms)
EUCA_STOCK_SHARE = 0.60    # ~60% of deferred + earn-out settleable in stock at Hims' option (reported)
SUBS_NOW = 2.891           # M, 30 Jun 2026 (reported)
ARPS_NOW = 92 * 12         # $/yr, Q2 2026 monthly revenue per avg subscriber $92 (reported) -> $1,104


@dataclass
class Scenario:
    name: str
    subs_2030: float        # M subscribers at end-2030
    arps_2030: float        # $ annual revenue per average subscriber
    ebitda_margin: float    # adj. EBITDA margin
    exit_multiple: float    # EV / adj. EBITDA at end-2030
    cum_fcf: float          # $M cumulative FCF, H2 2026 - 2030
    sbc_dilution: float     # net annual share growth from SBC after buybacks
    earnout_paid: float     # $M of the up-to-$200M Eucalyptus earn-out


SCENARIOS = [
    Scenario("bear", 3.5, 1000, 0.08, 10.0, 0.0, 0.030, 0.0),
    Scenario("base", 4.5, 1150, 0.14, 14.0, 1200.0, 0.020, 100.0),
    Scenario("bull", 5.8, 1250, 0.20, 18.0, 2500.0, 0.015, 200.0),
]


def value(s: Scenario) -> dict:
    revenue = s.subs_2030 * s.arps_2030           # $M (M subs x $ = $M)
    ebitda = revenue * s.ebitda_margin
    ev = ebitda * s.exit_multiple

    # Eucalyptus: stock-settled part adds shares at today's price, cash part is a debt-like outflow
    euca_total = EUCA_DEFERRED + s.earnout_paid
    euca_cash = euca_total * (1 - EUCA_STOCK_SHARE)
    euca_shares = euca_total * EUCA_STOCK_SHARE / PRICE_NOW

    base_shares = SHARES_NOW * (1 + s.sbc_dilution) ** VAL_DATE_YEARS + euca_shares

    # Converts: if-converted test. Iterate because per-share value depends on conversion.
    cash_2030 = CASH_NOW + s.cum_fcf - euca_cash
    debt = NOTES_2030 + NOTES_2032
    shares = base_shares
    vps = (ev + cash_2030 - debt) / shares
    for _ in range(5):
        debt, shares = 0.0, base_shares
        if vps > CONV_2030:
            shares += NOTES_2030 / CONV_2030
        else:
            debt += NOTES_2030
        if vps > CONV_2032:
            shares += NOTES_2032 / CONV_2032
        else:
            debt += NOTES_2032
        vps = (ev + cash_2030 - debt) / shares
    net_debt = debt - cash_2030
    irr = (vps / PRICE_NOW) ** (1 / VAL_DATE_YEARS) - 1 if vps > 0 else -1.0
    return dict(revenue=revenue, ebitda=ebitda, ev=ev, net_debt=net_debt,
                equity=ev - net_debt, shares=shares, vps=vps, irr=irr)


def solve(s: Scenario, field: str, target_irr: float, lo: float, hi: float) -> float:
    """Bisection: value of `field` that gives target_irr, other inputs fixed."""
    for _ in range(100):
        mid = (lo + hi) / 2
        if value(replace(s, **{field: mid}))["irr"] < target_irr:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2


def main() -> None:
    mcap = SHARES_NOW * PRICE_NOW
    ev_now = mcap + NOTES_2030 + NOTES_2032 - CASH_NOW
    print(f"Today: price ${PRICE_NOW:.2f}, basic shares {SHARES_NOW:.1f}M, mkt cap ${mcap:,.0f}M")
    print(f"EV (converts at face, ex-Eucalyptus deferred) = {mcap:,.0f} + {NOTES_2030+NOTES_2032:,.1f} - {CASH_NOW:,.0f}"
          f" = ${ev_now:,.0f}M; incl. ${EUCA_DEFERRED:.0f}M Eucalyptus deferred = ${ev_now+EUCA_DEFERRED:,.0f}M")
    print(f"Today: {SUBS_NOW:.3f}M subs x ${ARPS_NOW:,}/yr = ${SUBS_NOW*ARPS_NOW:,.0f}M revenue run-rate\n")

    hdr = f"{'scenario':<6} {'subs M':>6} {'$/sub':>6} {'rev $M':>7} {'margin':>6} {'EBITDA':>7} {'mult':>5} " \
          f"{'EV $M':>7} {'netdebt':>8} {'shares':>7} {'$/sh':>7} {'IRR/yr':>7}"
    print(hdr)
    print("-" * len(hdr))
    for s in SCENARIOS:
        r = value(s)
        print(f"{s.name:<6} {s.subs_2030:>6.2f} {s.arps_2030:>6.0f} {r['revenue']:>7,.0f} {s.ebitda_margin:>6.0%} "
              f"{r['ebitda']:>7,.0f} {s.exit_multiple:>5.1f} {r['ev']:>7,.0f} {r['net_debt']:>8,.0f} "
              f"{r['shares']:>7.1f} {r['vps']:>7.2f} {r['irr']:>7.1%}")

    # Management 2030 target check: >= $6.5B revenue, $1.3B adj. EBITDA (20%)
    mgmt = replace(SCENARIOS[1], name="mgmt", subs_2030=6500 / 1150, ebitda_margin=0.20)
    r = value(mgmt)
    print(f"\nMgmt target ($6.5B rev, 20% margin) with base multiple 14x / base other inputs: "
          f"${r['vps']:.2f}/sh, IRR {r['irr']:.1%}")
    for m in (10, 18):
        r = value(replace(mgmt, exit_multiple=m))
        print(f"  ... at {m}x exit: ${r['vps']:.2f}/sh, IRR {r['irr']:.1%}")

    print("\nBreakeven table (other inputs held at scenario values)")
    print(f"{'scenario':<6} {'subs for 0%':>12} {'subs for 10%':>13} {'margin 0%':>10} {'margin 10%':>11} {'mult 0%':>8} {'mult 10%':>9}")
    for s in SCENARIOS:
        row = [solve(s, "subs_2030", t, 0.1, 30) for t in (0.0, 0.10)]
        row += [solve(s, "ebitda_margin", t, 0.0, 0.6) for t in (0.0, 0.10)]
        row += [solve(s, "exit_multiple", t, 0.5, 60) for t in (0.0, 0.10)]
        print(f"{s.name:<6} {row[0]:>11.2f}M {row[1]:>12.2f}M {row[2]:>10.1%} {row[3]:>11.1%} {row[4]:>7.1f}x {row[5]:>8.1f}x")

    print("\nIRR grid, base case: subscribers (rows) x EBITDA margin (cols)")
    margins = [0.08, 0.11, 0.14, 0.17, 0.20]
    print(f"{'subs M':>7} " + " ".join(f"{m:>7.0%}" for m in margins))
    for subs in (3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0):
        cells = [value(replace(SCENARIOS[1], subs_2030=subs, ebitda_margin=m))["irr"] for m in margins]
        print(f"{subs:>7.1f} " + " ".join(f"{c:>7.1%}" for c in cells))


if __name__ == "__main__":
    main()
