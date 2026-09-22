# QA Review: `glp1-pen-bottlenecks.md` (package 2026-09-22-glp1-pens)

I edited no files. I read all six files in full and used 5 of the 8 permitted web searches.

## (a) Verdict: PASS WITH FIXES (defects #1 to #4 block release)

The main thesis is well supported by the raw files: the bottleneck has moved, the winning formats need fewer devices, most of the value is captive, and West has the best moat but is expensive. Most numbers trace back correctly. The device model and the devil's-advocate (DA) arithmetic recompute to within rounding.

The note should still not go to the client as written:
- **Medicare statement is wrong.** Section 1 says the $50 Medicare programme covers only the Zepbound KwikPen. Medicare.gov says it also covers Wegovy (injection or pill) and Foundayo. This sentence supports a headline argument.
- **Device table is mislabelled.** The "four-dose pens" row includes daily liraglutide pens, which overstates four-dose pens by 42% in 2026. The "devices per patient-year" row counts vials and leaves out needles, but the table has no vials row, so a reader cannot rebuild 26.5 / 19.1 / 12.7.
- **"First principles" sentence has an arithmetic error.** It says "removes 39 million autoinjectors"; the correct figure is 52 million removed, 39 million net fewer devices. The error is copied from raw 04.
- **Ownership is wrong.** Owen Mumford has belonged to Embecta since 15 May 2026, not Stevanato.
- **One dated catalyst is wrong.** Pfizer's first Phase 3 readouts are late 2027, not early 2027.
- **Estimates are stated as fact.** Several derived or single-source figures carry no caveat, including the $2 to 2.5bn supplier pool (its own itemisation adds up to only about $1.45bn) and the 18 to 30 month requalification time.
- **Some verdicts go beyond the evidence or skip the DA.** "Cleanest exposure is Lilly" has no Lilly valuation anywhere in the package. Calling Schott a "format winner" ignores the DA's view that Schott's 1 mL syringe business is among the hardest hit.

All fixes are text edits; none needs new research.

## (b) Defect list

| # | Sev | Location / quote | Problem | Evidence | Suggested fix text |
|---|---|---|---|---|---|
| 1 | Critical | §1 pt 2: "the Medicare $50 program covers only the Zepbound four-dose KwikPen" | Wrong. The Bridge also covers Wegovy (injection or tablet) and Foundayo; "only KwikPen" applies to Zepbound formats alone. Wegovy's US injection is currently a single-dose pen, so the Bridge does not "structurally" force 13 devices a year. Raw 04 §(c)1 and DA "Why these assumptions…" repeat the error. | Raw 04: "The Medicare Bridge covers only the Zepbound KwikPen. The single-dose pen and the vial are excluded…" (source lilly.com). Medicare.gov / AARP: "Wegovy® (injection or tablet), Zepbound® (KwikPen® only), and Foundayo®… doesn't cover single-dose Zepbound® vials or pens." | "…the Medicare $50 Bridge covers Wegovy (injection or pill) and Foundayo, but for Zepbound only the four-dose KwikPen, not the single-dose pen or vial…" |
| 2 | Critical | §3 table row "Four-dose pens / cartridges 271M / 475M / 280M" | Totals include daily liraglutide pens (80M / 56M / 20M). Four-dose pens alone are 191M / 419M / 260M, so the 2026 figure is overstated by 42%. The needles row likewise includes liraglutide needles (730M / 511M / 183M). | Raw 04 2026 table: "191.1M pens/cartridges" (4-dose) plus "80.0M pens" (daily) = 271M; 2030: 418.6M + 56M. DA worst case includes "daily 1%". | Rename the row "Pens / cartridges (four-dose weekly pens plus daily liraglutide pens)". Add a footnote: "Four-dose pens alone: 191M / 419M / 260M." Rename the needles row "Pen needles (weekly and daily pens)". |
| 3 | Critical | §3 row "Devices per patient-year 26.5 / 19.1 / about 12.7" | These are (autoinjectors + pens + vials) ÷ patient-years. Vials are not in the table and needles are excluded. Summing the rows shown gives (463+271+1,494)/31 = 72, not 26.5. The metric is undefined for the reader. | Raw 04: "Delivery units per patient-year fall from 26.5 to 19.1"; DA: "All delivery units (autoinjectors + pens + vials) 816M / 1,335M / ~633M". | Add row "Vials: 82M / 107M / ~57M". Rename the row "Delivery units per patient-year (autoinjectors + pens + vials; excludes needles and loose syringes)". |
| 4 | Major | §3: "each million patients who move from a weekly single-dose autoinjector to a four-dose pen removes 39 million autoinjectors and adds 13 million pens and 52 million needles" | Arithmetic error: 52 autoinjectors are removed, 13 pens added, so 39M is the net device reduction. Same error in raw 04 §(b) and DA attack 1. | 52 × 1M = 52M autoinjectors removed; 52 − 13 = 39 net. | "…removes 52 million autoinjectors and adds 13 million pens (39 million fewer devices in net) plus 52 million pen needles." |
| 5 | Major | §2 autoinjector row: "Stevanato/Owen Mumford" | Ownership wrong. Embecta closed its acquisition of Owen Mumford (and its Aidaptus autoinjector) on 15 May 2026; Stevanato is only the exclusive contract manufacturer. The note never mentions that Embecta now has an autoinjector business. | Raw 02: "Owen Mumford, now part of Embecta (EMBC). Embecta closed the deal on 15 May 2026… Stevanato is the exclusive manufacturing partner for Aidaptus." Raw 01 agrees. Embecta IR confirms the 15 May 2026 close (£100M upfront, up to £50M earn-out). | "…BD, Embecta (Owen Mumford's Aidaptus, made by Stevanato), Nemera (private)". In §4 Embecta row, exposure: "Generic co-packs; US decline; Aidaptus autoinjector (acquired May 2026)". |
| 6 | Major | §6: "Early 2027 \| MariTide Phase 3; Pfizer monthly GLP-1" | No raw file supports an early-2027 Pfizer readout. Raw 04 says Pfizer/Metsera timing was not researched; the DA only has a trial registration (19 May 2026, low-quality source). Pfizer guides first Phase 3 readouts to late 2027. | Raw 04: "Pfizer/Metsera monthly assets are not researched (a gap)." Web: Pfizer "10 Phase 3 trials… first readouts late 2027, first approvals targeted 2028". | Split the row: "Early 2027 \| MariTide Phase 3 (MARITIME-1/-2)" and "Late 2027 \| First Pfizer monthly GLP-1 (PF'3944) Phase 3 readouts". |
| 7 | Major | §1 pt 3 / §4 Lilly row: "Listed suppliers share roughly $2 to 2.5bn a year of GLP-1 revenue, about 2 to 3% of the drug market's value" | This is the DA's own rough estimate, stated as fact. Its itemised inputs add up to about $1.45bn (see c). The inputs mix a current run-rate (West), a 2023 IPO contract figure (Schott), a former CEO's 2025 target (Gerresheimer; raw 01 gives a different €350M target) and a 2033 target (Embecta). The denominator (~$95bn current incretin sales) is not stated. Raw 04 also has a different "Goldman $95B by 2030" figure, which invites confusion. | DA: "By my rough estimate… about $2–2.5bn… about 2–3% of the roughly $95bn incretin drug market [derived]"; DA "Unverified or derived: My estimates: the listed-supplier GLP-1 revenue pool". | "By our rough estimate, listed suppliers earn about $1.5 to 2.5bn a year from GLP-1 work, roughly 2 to 3% of current annualised incretin drug sales of about $95bn. The figure mixes reported sales with company targets and is indicative only." |
| 8 | Major | §1 pt 1: "Lilly and Novo solved it by building and buying their own plants (Novo's $11bn purchase of three Catalent fill sites; Lilly's $50bn+ of US plants)" | The cause-and-effect does not fit the dates. The Catalent deal closed 18 Dec 2024 with capacity guided "from 2026"; FDA had already declared tirzepatide resolved in Oct 2024. The $50bn+ is commitments since 2020, including API sites (Lebanon $9bn, Houston $6.5bn, Huntsville $6bn, Goochland $5bn), and Lehigh Valley is not operational until 2031. | Raw 03: "Novo Holdings closed the Catalent deal on 18 Dec 2024… Capacity was guided to rise gradually 'from 2026'"; "Total: more than $50bn in US commitments since 2020"; "Lehigh Valley… operational 2031". Raw 02: tirzepatide "resolved in October 2024 and reaffirmed… 19 December 2024". | "…FDA declared the tirzepatide shortage resolved in October 2024 (reaffirmed December 2024) and semaglutide in February 2025, as existing lines ramped. Lilly and Novo are now locking in the next wave in-house: Novo bought three Catalent fill sites for $11bn (capacity from 2026), and Lilly has committed more than $50bn to US plants, including API sites and a device plant due in 2031." |
| 9 | Major | §2 machines row: "No. Orders falling: ATS bookings -18%, Stevanato Engineering -31%, Mikron -6%" | (a) Only ATS is an order figure; Stevanato Engineering −31% is Q1 2026 revenue and Mikron −6% is H1 2026 sales. (b) It contradicts raw 03 for aseptic filling machines: Syntegon has a record backlog and book-to-bill above 1. The downturn is in assembly automation. | Raw 03: "Stevanato Engineering revenue –31% (Q1 2026)"; "Syntegon backlog record €1.3bn (H1 2026)… book-to-bill 1.09, Pharma +14%". Raw 02: "Mikron: H1 2026 sales −6%". | "No for assembly lines: ATS Q4 FY26 bookings −18%, Stevanato Engineering Q1 revenue −31%, Mikron H1 sales −6%. Aseptic filling machines are still strong (Syntegon record €1.3bn backlog, book-to-bill 1.09)." |
| 10 | Major | §4 Schott row "cartridge mix winner"; §5 "Schott Pharma and Nipro benefit as the US moves from single-dose autoinjectors to four-dose pens" | Contradicts the DA without explanation. DA attack 1 lists Schott (1 mL syringes) among those hit hardest by the format shift. Schott's current GLP-1 upswing is glass syringes, which the note's own §2 says are heading to oversupply. | DA: "Hits hardest: Ypsomed, SHL, BD, Stevanato and Schott (1 mL syringes)…" Raw 01: "DDS €123.2M… recovering on GLP-1 glass syringes"; raw 03: guidance raised "citing sustained demand for GLP-1 glass syringes". | §5: "Schott Pharma gains from cartridges but its recent GLP-1 growth is in 1 mL syringes, which lose from the same shift; Nipro is the cleaner cartridge exposure but data are thin. Buy either only on weakness." §4 Schott exposure: "Cartridges (winner) and 1 mL syringes (loser); about €1bn of contracts to 2030 disclosed at the 2023 IPO". |
| 11 | Major | §5: "the cleanest exposure is Lilly…"; §4: "own the drug maker, not the supplier" | A recommendation with no supporting work. There is no Lilly valuation in any raw file. The DA puts Lilly and Novo "outside the supplier thesis" and offers no buy view. This is overconfident for a client note. | DA §(e): "Novo (NVO) and Lilly (LLY): outside the supplier thesis." No LLY price, multiple or risk work in raw 01 to 05. | "If you believe the volume thesis, Lilly captures more of it than any supplier… We have not assessed Lilly's valuation in this work; treat this as a direction for further work, not a recommendation." |
| 12 | Major | §2 plungers row: "Strong (18 to 30 months to requalify)" | Single secondary source, flagged unverified in raw, stated as fact. | Raw 01: "Requalifying a stopper supplier reportedly takes 18 to 30 months (secondary source, unverified)." | "Strong (requalification reportedly 18 to 30 months, unverified)" |
| 13 | Minor | §3 row "Single-dose autoinjectors (and the syringes inside) 463M / 753M / 296M" | The 2030 figures include monthly devices (25.2M base, 36M worst). Weekly single-dose autoinjectors alone are 728M / 260M. | Raw 04: "Monthly… 25.2M AI/PFS"; DA: "Autoinjectors / prefilled syringes (weekly + monthly)". | Rename "Autoinjectors and prefilled syringes (weekly single-dose plus monthly)". |
| 14 | Minor | §1: "US obesity prescriptions are up 78% a year" | This is one quarter's year-on-year figure, not an annual growth rate. | Raw 04: "+78% year on year… Q2 2026". | "US obesity prescriptions were up 78% year on year in Q2 2026" |
| 15 | Minor | §1 pt 1: "FDA declared the tirzepatide shortage over in December 2024" | Imprecise. FDA declared it resolved in October 2024 and reaffirmed on 19 Dec 2024. | Raw 02 (quoted in #8). | Covered by the #8 fix. |
| 16 | Minor | §1 pt 1: "The scarce layer in 2026 is peptide drug substance for generics and biotechs, not pens" | Leaves out "CDMO fill slots" from raw 03 and conflicts with the note's own §2, which says autoinjectors are "Tight for next-generation drugs". | Raw 03: "Generics and biotechs: peptide API plus CDMO fill slots". | "…is peptide drug substance and outsourced fill-finish slots for generics and biotechs, not originator pens." |
| 17 | Minor | §2 syringes row: "No, heading to oversupply" | Stronger than the evidence. | Raw 01: "possibly heading to oversupply". | "No; possibly heading to oversupply in 2027-28…" |
| 18 | Minor | §2 fill-finish row: "overbuild risk by 2028" | This is the analyst's own estimate in raw 03, stated without a label. | Raw 03: "2028 (my estimate)". | "…overbuild risk by 2028 (our estimate)" |
| 19 | Minor | §2 cartridges row: "Tight for sterile ready-to-fill cartridges" | The tightness claim rests on secondary sources. Raw calls them "ready-to-use". | Raw 01 §(c): "cartridge 'shortages [are] expected for at least two years'… come from secondary sources." | "Reportedly tight near term for sterile ready-to-use cartridges (secondary sources)…" |
| 20 | Minor | §2 peptide row: "PolyPeptide (being bought by Samsung Biologics)" | The deal is a pending tender offer, not a completed or certain sale. | Raw 03: "Announced 20 Jul 2026, close around end-2026, 66⅔% minimum acceptance". | "PolyPeptide (subject to a pending Samsung Biologics tender at CHF 44.31, expected to close around end-2026)" |
| 21 | Minor | §2 resins row: "Celanese, Covestro, DuPont, BASF" | DuPont and BASF were not researched. The note that Delrin changed ownership comes from memory. | Raw 02: "DuPont / BASF (Delrin, Ultraform; not verified)"; "[memory] DuPont Delrin ownership change". | "Celanese, Covestro (DuPont/Delrin and BASF not verified)" |
| 22 | Minor | §4 Gerresheimer row: "Pen bodies for Novo and Lilly" | A supplier-to-drug link stated as fact, while §7 says such links are "market lore". | Raw 01 (snippet); DA attack 5. | "Pen bodies, reportedly for Novo and Lilly" |
| 23 | Minor | §4 Embecta row: "2.8x earnings" | Derived figure; raw flags Embecta's P/E as conflicting between sources. The price date is not given. | Raw 01: "about 2.8x forward EPS (derived)"; §(c): "Several market-data figures conflict… Embecta P/E". | "about 3x forward EPS (derived; sources conflict)" |
| 24 | Minor | §4 Nipro / Bachem / Embecta: "Only on a drawdown" | The DA verdict is "only on a big drawdown". The DA's caveat on Nipro is also dropped. | DA §(e): Nipro "only on a big drawdown. There was not enough data…". | "Only on a big drawdown" for all three; Nipro: add "limited data". |
| 25 | Minor | §4 Schott row: "into a year flattered by a €15M one-off" | FY26 ends 30 Sep 2026 and the one-off is booked in Q4 FY26, so the year is not yet closed. The "€1bn of contracts to 2030" is a 2023 IPO disclosure and is stale. | Raw 01: "one-off contribution of about €15M in Q4 FY26"; "disclosed at the 2023 IPO". | "…into a fiscal year (ending September 2026) that will include a €15M one-off"; "About €1bn of contracts to 2030 (2023 IPO disclosure)". |
| 26 | Minor | §5: "as it did after COVID: West fell 56% and Stevanato 44% from their post-COVID peaks" | West's figure is peak (Sep 2021) to trough (Jul 2025). Stevanato's is peak (Aug 2023) to today's price, so it is still open and includes the post-Q2 2026 fall. | DA attack 9. | "…West fell 56% from its 2021 peak to its July 2025 low, and Stevanato is still 44% below its August 2023 peak." |
| 27 | Minor | §3 last sentence: "every current US pricing and channel signal points toward fewer devices per patient" | Overstated. The Bridge covers Wegovy injections (#1). More than 80% of Wegovy-pill patients are new to GLP-1s. Raw 02 notes pills "are not taking much share from injectables". | Raw 04 §(c)2; raw 02 §5. | "…and most US pricing and channel signals (KwikPen price parity, multi-dose Wegovy FlexTouch, pills) point toward fewer devices per patient." |
| 28 | Minor | §6 dated signals | Missing near-term events: Gerresheimer's ~€870M notes must be refinanced by 30 Sep 2026 (8 days away). The US Wegovy FlexTouch launch is the key format swing for Ypsomed; Novo itself guides H2 2026 (web), so it is no longer Substack-only. Retatrutide "Q1 2027" filing and West "late Oct" date need caveats. | Raw 01 (Gerresheimer); DA kill-shot table (West date "exact date unverified"; Ypsomed trigger); raw 04 #6 (retatrutide non-primary). | Add "30 Sep 2026 \| Gerresheimer ~€870M note refinancing deadline" and "H2 2026 \| US Wegovy four-dose FlexTouch launch \| Direct hit to single-dose autoinjector volume (Ypsomed)". Amend: "Late Oct 2026 (date unconfirmed)"; "Q1 2027 (secondary source) \| Retatrutide filing". |
| 29 | Minor | Header: "All figures are from web-search snippets" / only one "Not investment advice" | Many figures are the team's own derivations (multiples, target prices, supplier pool, whole bear model). The disclaimer does not appear near the buy levels in §4/§5. | DA and raw 01 "derived" tags. | Header: "…All figures are from web-search snippets or our own arithmetic on them (marked as estimates)…". Add at the end of §5: "Price levels are illustrative multiples, not price targets. Not investment advice." |
| 30 | Minor (raw only) | Raw 02 Stevanato: "FY26 guidance… EPS €0.53–0.55" | Conflicts with raw 01 (€0.60–0.62), which the DA's 28x uses. The web check confirms €0.60–0.62 (narrowed in Aug 2026 from €0.59–0.63). The note is correct; raw 02 is wrong or stale. | Stevanato Q2 2026 release (web). | Note: no change. Raw 02: annotate as superseded. |

## (c) Arithmetic check

| Item | Note value | Recomputed | OK / WRONG |
|---|---|---|---|
| 2026 patient-years | 31M | 8.9+14.7+2.0+1.2+1.5+2.5 = 30.8M | OK |
| 2026 oral share | 8% | 2.5/30.8 = 8.1% | OK |
| US tirzepatide (raw) | 6.5M | $9.7bn / ($500×3) = 6.47M; also 3.2+1.5+0.6+1.2 = 6.5 | OK |
| 2026 autoinjectors | 463M | 8.9×52 = 462.8M | OK |
| 2026 pens/cartridges | 271M | 14.7×13 = 191.1 + 2.0×40 = 80 → 271.1M (includes daily pens) | Arithmetic OK; label WRONG (#2) |
| 2026 needles | 1.49bn | 14.7×52 = 764.4 + 2.0×365 = 730 → 1,494M | OK (includes daily) |
| 2030 base mix | 100% / 70M | 25+3+4+2+20+46 = 100%; 17.5+2.1+2.8+1.4+14+32.2 = 70 | OK |
| 2030 autoinjectors | 753M | 14×52 = 728 + 2.1×12 = 25.2 → 753.2M | OK |
| 2030 pens | 475M | 32.2×13 = 418.6 + 1.4×40 = 56 → 474.6M | OK |
| 2030 needles | 2.19bn | 32.2×52 = 1,674.4 + 1.4×365 = 511 → 2,185M | OK |
| 2030 vials (raw) | 107M | 1.8×52 + 1.0×13 = 106.6M | OK |
| Worst case mix (DA) | 50M | 40+6+10+40+3+1 = 100% | OK |
| Worst autoinjectors | 296M | 5×52 = 260 + 3×12 = 36 → 296M | OK |
| Worst pens | 280M | 20×13 = 260 + 0.5×40 = 20 → 280M | OK |
| Worst needles | 1.22bn | 20×52 = 1,040 + 0.5×365 = 182.5 → 1,222.5M | OK |
| Worst vials (DA) | ~57M | 1.5M × (106.6/2.8 = 38.1) = 57.1M | OK |
| Devices per patient-year 2026 | 26.5 | (462.8+271.1+81.9)/30.8 = 815.8/30.8 = 26.49 | OK (definition missing, #3) |
| Devices per patient-year 2030 base | 19.1 | (753.2+474.6+106.6)/70 = 19.06 | OK |
| Devices per patient-year worst | ~12.7 | (296+280+57)/50 = 12.66 | OK |
| Fall by 2030 | −28% | 19.06/26.49 − 1 = −28.0% | OK |
| "36% below today" | −36% | 296/463 − 1 = −36.1% | OK |
| DA: −61% vs base; pens −41%; needles −44%/−18%; all units −53%/−22% | as stated | 296/753 = −60.7%; 280/475 = −41.1%; 1,223/2,185 = −44.0%, 1,223/1,494 = −18.1%; 633/1,335 = −52.6%, 633/816 = −22.4% | OK |
| DA moderate bear 473 / 352 / 1,529 | as stated | 8.4×52+3×12 = 472.8; 25.2×13+0.6×40 = 351.6; 25.2×52+0.6×365 = 1,529.4 | OK |
| DA: patients "grow 60%" | +60% | 50/30.8 = +62% | OK |
| Raw 04 CAGRs 23/13/15/10/7% | as stated | 2.273^¼ = 1.228; 1.626^¼ = 1.129; 1.751^¼ = 1.150; 1.463^¼ = 1.100; 1.30^¼ = 1.068 | OK |
| Raw 04 format bear 613 / 393 / 1,858 | as stated | 10.5×52+5.6×12 = 613.2; 25.9×13+56 = 392.7; 25.9×52+511 = 1,857.8. Shares add to 98%; the missing 2% is daily pens | OK (shares not shown adding to 100%) |
| Weekly autoinjector → four-dose pen | "removes 39M autoinjectors" | Removes 52M autoinjectors, adds 13M pens: −39M net | WRONG (#4) |
| Weekly → monthly | removes 40M | 52 − 12 = 40 | OK |
| 52/13 | 13 instead of 52 | 52/4 = 13 | OK |
| Monthly cut "4.3×" (raw) | 4.3× | 52/12 = 4.33 | OK |
| Wegovy pill API per week | ~73× | 25 mg × 7 = 175 mg; 175/2.4 = 72.9 | OK |
| West multiple | ~42x | $373.56 / $8.95 = 41.7x | OK |
| West at 25x / 30x | $224 / $268 | 25×8.95 = $223.75; 30×8.95 = $268.50 (−40.1% / −28.1%) | OK |
| West FY26 EPS midpoint | $8.95 | ($8.85+9.05)/2 = 8.95 | OK |
| West GLP-1 revenue (DA) | ~$605M | 18% × $3.36bn = $604.8M | OK |
| Schott rally | +87% | 23.65/12.62 = +87.4% | OK |
| Schott P/E (raw 01/DA) | ~22x | 16.6 × 23.65/17.46 = 22.5x | OK |
| DA: Schott back at 16.6x ≈ €17.8 | (DA only) | 16.6 × (23.65/22.48) = €17.46 (the July price itself); €17.8 is a rounding artefact | Minor WRONG (DA only) |
| Stevanato multiple | ~28x | 0.61 × 1.16 = $0.708; 19.67/0.708 = 27.8x. The EPS guidance is confirmed on the web | OK |
| Stevanato GLP-1 revenue (DA) | ~€285M | 22.5% × €1.27bn = €285.8M | OK |
| Embecta P/E | 2.8x | $5.19 / $1.85 = 2.81x | OK (derived; sources conflict) |
| Supplier pool | $2–2.5bn | West 605 + Stevanato €285M×1.16 = 331 + Schott €140M×1.16 = 162 + Gerresheimer €200M×1.16 = 232 + Datwyler ~15–25 + Embecta 100 (a 2033 target) ≈ **$1.45bn**. Anything above that needs unitemised names (Ypsomed, BD, Aptar, Nipro, Bachem, ATS, Mikron, medmix) | Not reproducible; overstated or unsupported (#7) |
| "2 to 3% of drug market" | 2–3% | 2.0/95 = 2.1%; 2.5/95 = 2.6%; the itemised $1.45bn/95 = 1.5%. Denominator: Lilly (9.9+4.9)×4 = $59.2bn plus Novo semaglutide ≈ $35bn ≈ $95bn, plausible | OK only on the unsupported pool (#7) |
| DA: $2.70 per delivery unit | (DA only) | $2.2bn / 816M = $2.70 | OK |
| Novo sites 11 → 14 | +3 | 3 ex-Catalent sites | OK |

## (d) Claims that must carry an "unverified" or "estimate" caveat

1. The $2 to 2.5bn listed-supplier pool and "2 to 3% of the drug market" (DA "my estimates"; itemised inputs add up to about $1.45bn).
2. "18 to 30 months to requalify" elastomers (secondary source, flagged unverified in raw 01).
3. West's ~70% elastomer share (the note already caveats this; keep it).
4. Cartridge tightness, "tight for sterile ready-to-fill cartridges" (secondary sources, raw 01 §(c)).
5. "Overbuild risk by 2028" for fill-finish (raw 03 "my estimate").
6. Gerresheimer "pen bodies for Novo and Lilly", and generally any supplier-to-drug link (raw 01 §(c); DA attack 5).
7. Retatrutide filing "Q1 2027" (non-primary source, raw 04 unverified #6).
8. West Q3 "late Oct 2026" (DA: "exact date unverified").
9. Embecta "2.8x earnings" (derived; raw 01 lists Embecta P/E among conflicting figures).
10. The 42x, 28x and 22x multiples and the $224 to $268 levels are the team's derivations, not quotes or targets.
11. Stevanato "22 to 23% of revenue" (raw 04: "Call summary; verify").
12. The worst plausible case (12.7 devices per patient-year, −36% autoinjectors) is the DA's assumption set (§7 says this; §1 should say "the skeptic's assumed worst case").
13. The 31M and 70M patient-years and all format splits are estimates derived from revenue at assumed net prices (§7 covers this; add "estimate" in §1 and §3).
14. Schott "about €1bn of contracts to 2030" is a 2023 IPO disclosure and needs a date caveat.
15. DuPont/BASF as resin suppliers (not researched; Delrin ownership from memory).
16. Datwyler's "one customer" ("leading GLP-1", unnamed and unconfirmed).

**Web adjudication (5 of 8 searches used):**
- **Medicare Bridge coverage:** the raw files and the note are wrong; the Bridge also covers Wegovy and Foundayo ([Medicare.gov fact sheet](https://www.medicare.gov/publications/12234-medicare-glp-1-bridge-glp-1-drugs-for-50-a-month.pdf), [AARP](https://www.aarp.org/medicare/glp1-weight-loss-copay-program/)). The 31 Dec 2027 end date is consistent with CMS extending the Bridge by a year.
- **Stevanato FY26 adjusted EPS €0.60 to 0.62:** confirmed, so raw 02 is wrong ([Stevanato IR](https://ir.stevanatogroup.com/news-events/press-releases/detail/183/stevanato-group-delivers-8-revenue-growth-for-the-second)).
- **US Wegovy FlexTouch:** FDA-approved, and Novo expects to launch it in H2 2026, so it is no longer resting on a Substack alone ([Novo 6-K](https://www.sec.gov/Archives/edgar/data/0000353278/000035327826000023/caq22026.htm)).
- **Embecta owns Owen Mumford:** confirmed, closed 15 May 2026 ([Embecta IR](https://investors.embecta.com/news-releases/news-release-details/embecta-completes-acquisition-owen-mumford-holdings-limited)).
- **Pfizer monthly GLP-1:** first Phase 3 readouts are late 2027 ([Fierce Biotech](https://www.fiercebiotech.com/biotech/pfizers-10b-monthly-glp-1-bet-generates-competitive-weight-loss-phase-2b)).

Files reviewed:
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-glp1-pens/glp1-pen-bottlenecks.md`
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-glp1-pens/raw/01-primary-containers-needles.md`
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-glp1-pens/raw/02-pens-autoinjectors-devices.md`
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-glp1-pens/raw/03-fill-finish-equipment-api.md`
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-glp1-pens/raw/04-demand-device-count.md`
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-glp1-pens/raw/05-devils-advocate.md`
