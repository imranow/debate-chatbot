# QA review: Single Women and Egg Freezing (2026-09-22 package)

Files reviewed (none edited):
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-egg-freezing/egg-freezing-thesis.md`
- `/home/user/debate-chatbot/reports/stocks/research/2026-09-22-egg-freezing/raw/01-demand-demographics.md` … `04-devils-advocate.md`

Web searches used: 8 of 8. The budget is now spent. They went on: SART 2024 (2 searches), the Xu Zaozao ruling, Sun/Organon, Kitazato results and ticker, the Richter ticker (2 searches), and Merck FY2025 fertility.

---

## (a) Verdict: PASS WITH FIXES (it should not go out as it stands)

Almost every number in the note traces to a raw file, and the key arithmetic checks out. That covers the $33.5k customer value and its 72/16/7/5 split, the $620M market, the 23% CAGR, +2.1%, +1.4%, most of the exposure percentages and the $4.4k tax figure. The note also makes the right choices on two of the disputed facts: it uses 7 Aug 2024 for the Xu Zaozao ruling (confirmed by search) and compares 38,930 with 38,126, a SART-to-SART comparison.

It still needs text fixes before it can go to the client:
- **One critical defect.** The headline claim that growth "just stalled" rests on a single snippet (SART 2024 preliminary, 38,930 cycles). Three of the four research streams could not retrieve that number, and I could not confirm it in two searches. The note presents it as fact and never says which 2023 base it compares against.
- **Several major defects:**
  - The note gives three different answers to "which listed name is the best exposure", and it reframes Progyny as the elective-freezing play, which contradicts raw/04 without saying why.
  - The Merck "84% US price cut" is misleading.
  - Kitazato is called "dominant" even though its US share is unknown and its risks are left out.
  - "Fastest-growing part of IVF" has no source.
  - Kindbody's "$400M" is undated and reported as a possibility, but the note states it as fact.
  - The 20% return rate in the model is an assumption, not a finding.
  - The note tells readers what to buy with only a one-line disclaimer.

None of this means redoing the research. The note also sends clients to `raw/`, so the raw-file errors listed after the defect table (R1-R8) should be fixed or annotated before release.

---

## (b) Defect table

| # | Sev | Location and quote | Problem | Evidence | Suggested fix text |
|---|---|---|---|---|---|
| 1 | **Critical** | §1.2 "SART's preliminary 2024 report shows 38,930 cycles, only about 2% growth"; §1.2 heading "growth just stalled"; §4 "US (+2%)" | Rests on one source that could not be checked, and the base year is not named. Only raw/04 has 38,930. Raw/01 says "egg freezing line not retrieved"; raw/02 (c) lists "SART 2024 egg-freezing data" as missing. Against raw/01's 39,269 the change is **-0.9%**, not +2%. The note uses 38,126 for 2023 without saying so. Preliminary and final counts are also different vintages. | raw/04 l.6: "38,930 … against 38,126 in the final 2023 report. That is +2.1% … Against the team's 39,269 … -0.9%". raw/01 l.60: "egg freezing line not retrieved". My 2 searches did not surface 38,930. | §1.2: "SART's preliminary 2024 report, as seen in one search snippet we could not check against the SART site, shows 38,930 cycles. That is about 2% more than SART's final 2023 figure of 38,126, and about 1% less than the 39,269 some sources give for 2023. Either way, growth appears to have stalled, pending SART's final 2024 data." Change the heading to "growth appears to have stalled". |
| 2 | Major | §1 "The best listed exposure is Kitazato" vs §1.3 "only Progyny (about 5 to 11%) … and Kitazato (about 3 to 9%)" vs §5 "[Progyny] is the only listed name with meaningful elective exposure" | Three different answers to the same question. By exposure, Progyny ranks above Kitazato, so "best exposure" can only mean best quality. | raw/04 (c): Progyny is "The **only** listed name that plausibly clears 5%"; Kitazato is "The best-quality exposure". | §1: "The best-quality listed exposure is Kitazato (368A.T)…". §5: "Progyny has the largest estimated elective exposure of any listed name (about 5 to 11%, undisclosed); Kitazato's is about 3 to 9%." |
| 3 | Major | §5 "Wait for Progyny to get cheap. It is the only listed name with meaningful elective exposure…" | Contradicts raw/04's verdict and gives no reason. Raw/04 says to buy it only as a cheap benefits manager, "not as an egg-freezing bet". | raw/04 (f): "**Only on a big drawdown** (near the 52-week low of $16-20), and as a cheap fertility benefits manager, not as an egg-freezing bet" | "Wait for Progyny to get cheap, and treat it as a fertility-benefits business, not an egg-freezing play. Its egg-freezing share is undisclosed, and its use per member is falling…" |
| 4 | Major | §3 Merck row "84% US price cut under the TrumpRx deal" | Overstated. The 84% is the company's "up to" figure, and it applies only to cash purchases on TrumpRx when all three drugs are used. The raw files' own dollar figures work out to about 40-55% off. §4 of the note correctly says "up to 84%", so the note contradicts itself. | raw/01 l.157: "The company claims up to 84% savings if a patient uses all three". raw/02: "up to $2,200 saved per cycle". raw/03: $3,500-6,000 at list vs $1,500-3,500 on TrumpRx. | "Fertility flat to down; TrumpRx cash price up to 84% below list for the three-drug regimen (company claim; about $2,200 saved per cycle)" |
| 5 | Major | §1 "It is a real chokepoint … a reported 70% share in Europe, 80% in China and 85% in India"; §5 "the only listed company with a dominant, high-margin position in freezing itself" | (i) The share figures come from an investor write-up, but that is said only in §7. (ii) Kitazato's **US share is unknown**, yet the US is the market the note sizes. (iii) China, with its 80% share, has zero elective demand. (iv) The top pick gets no risk list. | raw/03 l.105: "from an MOI Global/Latticework writeup, not the company". raw/03 l.107: "**Missing:** US share". Risks at raw/03 l.109 and raw/04 (d): small cap, founder legacy, currency, one US distributor (DeviMed), Genea Gavi automation, IVM. | §1: "…a 70% share in Europe, 80% in China and 85% in India, according to an investor write-up rather than the company (its US share is not known)…". Add after it: "Risks: small cap; currency; dependence on one new US distributor; automated vitrification (Genea Gavi) or in-vitro maturation could change lab workflow." §5: "dominant outside the US". |
| 6 | Major | §5 "all frozen cycles (egg and embryo), which are the fastest-growing part of IVF" | No raw file supports this. The nearest is raw/01's "Egg and embryo freezing were 17% of all cycles in 2024" (UK), which is a share, not a growth rate. | Not found in raw/01-04 | Delete "which are the fastest-growing part of IVF", or replace it with "which are a large and rising share of IVF cycles (17% of UK cycles in 2024)". |
| 7 | Major | §4 "Kindbody fell from a $1.8bn valuation to about $400M." | Stated as fact. The source says "reportedly possibly as low as" and the item is undated. | raw/02 l.94: "targeted $600M pre-money raise, and reportedly possibly as low as about $400M"; raw/02 (c): "the $400M valuation … undated" | "Kindbody's valuation has reportedly fallen from $1.8bn to a targeted $600M, and possibly as low as about $400M (undated reports)." |
| 8 | Major | §2 table "Thaw… (only about 20% return)"; prose "only 6% (US, 5 to 7 years) to 28% (Australia and New Zealand, 10 years) of women ever come back" | The base case is a US woman, but the model's 20% return rate is about 3.5 times the observed US rate (5.7%). The note does not say 20% is an assumption. "Ever" is also wrong: these are return rates within each study's follow-up period. The conclusion still holds, since a lower rate makes later IVF even smaller. | raw/01 (c): US 5.7% at 5-7 yrs; Extend about 9%; ANZ 27.9% at 10+ yrs. The worked example assumes 20%, 1.5 cycles and 95% storage retention (raw/01 (f): "my assumptions"). | Table: "(assumes 20% return over 10 years, above the 6-9% seen in US studies so far)". Prose: "…because only 6% (US, after 5 to 7 years) to 28% (Australia and New Zealand, after 10 or more years) of women have come back for their eggs." Add under the table: "Assumptions: 1.5 cycles, $750 a year storage with 95% annual retention, 20% return; FertilityIQ reports an average of 2 cycles." |
| 9 | Major | Whole note: "Own it", "Own the chokepoint", "Wait for Progyny… buying near its 52-week low", "size small" | The note gives directives with price levels, but its only caveat is one italic line in the header. It has no risk section and no statement of positions or conflicts. | Header only: "Not investment advice." | Add at the end: "**Important:** This note is research for discussion, not investment advice or a recommendation to buy or sell any security. All figures come from unverified web-search snippets and estimates. Company exposure figures are our assumptions. Verify against primary filings. The authors hold no positions [confirm]." Soften "Own it" to "The case for owning it is…". |
| 10 | Minor | §4 "Total US IVF cycles grew only 1.4%" | The note does not say which 2023 total it uses. The raw files give three: 415,953, 425,869 and ~432k. Against ~432k, 2024 is -0.2%. These are also ART cycles, not IVF cycles. The TFR of 1.57 is for 2025, while the cycle comparison is for 2024. | raw/04 l.152 lists the conflict; raw/02 l.104: 415,953; raw/03 l.9: 425,869; raw/01 l.59: ~432k. Search snippets show 415,953 and 432,641 in secondary sources. | "Total US ART cycles were 431,746 in SART's preliminary 2024 report, 1.4% above the final 2023 figure of 425,869 (other sources give 415,953 to about 432,000 for 2023), even as the fertility rate hit a record low of 1.57 in 2025." |
| 11 | Minor | §7 "US 2023 egg-freezing counts differ across sources (38,126 to about 40,000)" | Does not say which figure the note uses. It also leaves out the total-cycle conflict, the single-source status of the 2024 figure, and the Xu Zaozao date conflict with raw/01. | See #1 and #10 | "The note uses SART's final 2023 count of 38,126 for comparisons. Other sources give 39,269 and about 40,000. Total 2023 ART cycles also differ (415,953 / 425,869 / ~432k). The 2024 figures (38,930; 431,746) come from one snippet each. Raw/01's October 2025 date for the Xu Zaozao ruling is wrong: the final appeal was rejected on 7 Aug 2024." |
| 12 | Minor | §7 "Merck KGaA's 2025 fertility growth differs between sources (+0.4% vs +2.4% organic)" | This can be settled. Merck's FY2025 release gives +0.4% and Gonal-f -6.7%. The +2.4% and -7.7% in raw/04 are Q3 2025 quarterly figures (raw/03 l.60 has "Q3 2025 was +2.4%"). | Search: Merck FY2025 results say "organic growth of 0.4%", Gonal-f "declined organically by 6.7%", and a 7.7% Gonal-f decline in Q3. | Replace with: "Merck KGaA fertility grew +0.4% organic in FY2025 (Gonal-f -6.7%). The +2.4% figure seen elsewhere is Q3 2025 only." Correct raw/04 l.8 and l.36 to match. |
| 13 | Minor | §3 Cooper row "About 0.2 to 0.5%" | Carries over an arithmetic slip from raw/04. The raw inputs give $6-9m on $4.24bn of revenue, which is 0.13-0.22%. | See (c) | "About 0.1 to 0.2%" |
| 14 | Minor | §1 and §4 "a 53% operating margin and a price of about 13 times earnings" | 5.86/10.95 = 53.5%, so "53%" understates it. Search confirms FY3/26 net profit of ¥3.90bn; on raw/03's ¥55bn market cap, P/E is 14.1x. The 13.4x in raw/03 implies a cap of about ¥52bn. Search also shows FY3/26 operating profit up only +1.3% against sales +6.3%, so the margin compressed. The raw files don't report this. | raw/03 l.103-104; TipRanks/BigGo FY3/26 results | "an operating margin of about 54% and a price of about 13 to 14 times earnings (aggregator data)" |
| 15 | Minor | §4 "about $4,400 of extra tax on a $20,000 benefit" | Leaves out the income assumption. $4,400 is exactly 22% × $20k, which is federal income tax only, excluding FICA (about $1,530) and state tax. | raw/01 l.162: "a woman earning $80k owes about $4.4k more tax (CNBC)" | "about $4,400 of extra federal income tax on a $20,000 benefit for a woman earning $80,000 (CNBC; payroll and state taxes would add more)" |
| 16 | Minor | §4 "The federal 'excepted fertility benefit' rule … target[s] medical infertility" | It is a *proposed* rule, and the raw file says elective freezing is "probably excluded (the rule text needs checking)". | raw/01 l.158-161 | "The proposed federal 'excepted fertility benefits' rule (May 2026) appears to cover medical infertility only (rule text not checked)…" |
| 17 | Minor | §4 "Employer egg-freezing coverage rose only from 16% (2024) to 18% (2026)" | The 18% figure for 2026 comes from a secondary site (doesinsurancecover.com), not IFEBP directly. Mercer's figure (21% of large employers) also conflicts and is not mentioned. | raw/04 (g) l.137; raw/01 l.151-152 | "…to 18% in 2026 (IFEBP, via a secondary source; Mercer puts large-employer coverage at 21%)" |
| 18 | Minor | §3 Organon "It is a fixed $14 cash takeover by Sun Pharma" | Leaves out the status and timing. Search confirms: agreement 26 Apr 2026, $14 cash, EV $11.75bn, shareholder approval 23 Jul 2026, closing expected early 2027. | raw/03 l.84; search (Organon PR, 10-Q) | "Avoid. Pending $14-a-share cash takeover by Sun Pharma (shareholders approved 23 Jul 2026; closing expected early 2027)." Add "Early 2027: Sun/Organon close" to §6. |
| 19 | Minor | §3 Monash "takeover interest gone" | Rests on one raw/04 phrase ("cancelled"). Raw/02 says only that the board rejected the bids, and the consortium still holds 19.6%. | raw/02 l.141; raw/04 l.39 | "The Genesis Capital/Soul Patts bid was rejected and has reportedly lapsed; the consortium still holds 19.6%." |
| 20 | Minor | §5 "Public investors can only reach them through IPOs, and the first one (Indira IVF) is an exit by its owners" | Indira is not a US chain with owned storage, and it is not "the first" IPO: raw/02 records a 2026 Gaudium IVF IPO (unverified). Monash and Jinxin are already listed. | raw/02 l.162 | "…through IPOs, and the most prominent one in the pipeline (Indira IVF, India) is a full exit by EQT and the founders." |
| 21 | Minor | §4 "Low-cost clinics charge $6,000 to $7,600" | Mixes pricing bases: Kindbody's $6k excludes drugs, while CNY's $7,594 is all-in. | raw/01 l.110 | "Low-cost clinics charge from $6,000 before drugs (Kindbody) to $7,600 all-in (CNY Fertility)" |
| 22 | Minor | §3 Vitrolife "Avoid as a thesis vehicle" vs §5 "points back to Kitazato and, on a large drawdown, Vitrolife" | The table and the prose disagree. | raw/04 (f): "only on a big drawdown as a bet on IVF cycles recovering" | Table: "Avoid as a thesis vehicle; only on a big drawdown as a bet on IVF recovery." |
| 23 | Minor | §3 "Only on a big drawdown ($16 to 20)" vs §5 "near its 52-week low" | The 52-week low is $16.10; $16-20 is a band. "Client losses" (plural) overstates it: one client (Amazon) is identified, it left on 1 Jan 2025, and management says retention risks are "largely addressed". | raw/02 l.59-62, l.70 | §5: "…the loss of Amazon to Maven (effective Jan 2025) argue for buying only well below today's ~$27 (52-week low $16.10)." |
| 24 | Minor | §4 "Progyny trades at about $27." | Presented as evidence of a poor track record, but with no comparison it shows nothing. Raw/04's comparison (2021 peak of about $60+) is marked unverified. | raw/04 l.42, l.149 | Delete it, or write "Progyny trades at about $27, well below its 2021 peak (reported at about $60+, unverified)." |
| 25 | Minor | §1.1 "Unmarried US women aged 15 and over have outnumbered married women since around 2010"; "has stopped moving" | The year is unconfirmed, and the margin is 50.1% vs 49.9%. "Stopped moving" is based on all adults (Pew). Raw/01 found "no 2024-25 figure for share of women married". | raw/01 l.19, l.43, l.196 | "…have slightly outnumbered married women (49.9% married, PRB, probably 2009-10 data; year unconfirmed). Among all US adults, Pew shows the trend stalling…" |
| 26 | Minor | §4 "Gameto's Fertilo shortens hormone stimulation from about two weeks to 2 to 3 days" | This is a company claim, not a trial result, and it is presented as fact. | raw/04 l.43 quotes company language | "Gameto says its Fertilo shortens…" |
| 27 | Minor | §1.2 "about $620M of revenue a year, of which about two thirds is elective" | The $620M is retrieval spend only (storage adds about $60m, a raw/01 estimate). The two-thirds ratio is from 2021 cycles and is applied to 2024. | raw/01 l.146; raw/04 l.35 | "…about $620M of retrieval spend a year (2024 volumes; storage adds roughly $60M by our estimate), of which about two thirds (the 2021 elective share) is elective, or about $415M." |
| 28 | Minor | §2 table "Clinic about $11,000 per cycle" | The raw files conflict: raw/01 has $11k (FertilityIQ), while raw/03's cost stack has a clinic midpoint of $8k plus $0.9k anaesthesia. | raw/01 l.109; raw/03 l.36-38 | "Clinic about $9,000 to $11,000 per cycle (sources differ)" |
| 29 | Minor | §2 "Storage is the best annuity … specimens rarely move once frozen" vs §4 "Offsite storage at $200 to $500 a year undercuts clinic storage" | Undercutting only matters if specimens do move. The annuity is also small (about $60m a year in the US, raw/01) and the note never sizes it. | raw/01 l.146; raw/02 l.190 | Add: "It is small, though: roughly $60M a year of US storage revenue on our estimate, and cheaper offsite storage is a competitive threat." |
| 30 | Minor | §3 Kitazato "About 3 to 9% direct" | Raw/04 applies a 50-67% elective share, which is the US ratio, to a company whose reported strongholds are China (elective freezing banned) and India. The range is likely an upper bound. | raw/04 (c) l.52, l.58; raw/03 l.105 | "About 3 to 9% direct (probably an upper bound given its China and India mix)" |
| 31 | Minor | §6 "Before 1 Jan 2027 — Final federal excepted fertility benefit rule" | The date is inferred from the proposed start date for plan years; the raw files give no confirmed date for a final rule. | raw/01 l.160 | "Expected before 1 Jan 2027 (timing not confirmed)" |
| 32 | Minor | §3 Gedeon Richter "RICHT.BD" | The raw files disagree (raw/02 has RICHTER.BD). The Budapest exchange ticker is **RICHTER**; Yahoo shows both RICHT.BD and RICHTER.BD. | Search: bse.hu, stockanalysis "BUD:RICHTER", Yahoo | "RICHTER (Budapest)" |
| 33 | Minor | Staleness: §6 "Nov 2026 — Kitazato H1 FY3/27" | Kitazato already reported Q1 FY3/27 on about 3 Aug 2026 (search: net profit +35.1%, sales ¥3.02bn, overseas ratio 67.1% "led by US and European markets"). The raw files missed it. | BigGo search result | Add: "Q1 FY3/27 (Aug 2026) reportedly showed net profit +35.1% and US-led overseas growth (not verified against the filing)." |
| 34 | Minor | Jargon throughout | Terms a non-expert won't know are left unexplained: ART, SART, HFEA, vitrification, EBITDA ("earnings (EBITDA)" is inaccurate), P/E, organic growth, covered lives, excepted benefit, TrumpRx, Phase 3 interim readout, H1 FY3/27, Two Sessions, EQT, IPO, 52-week low. | — | Add a short glossary. Change "11 to 15 times earnings (EBITDA)" to "11 to 15 times EBITDA (operating profit before depreciation and amortisation)". Change "H1 FY3/27" to "first-half results for the year to March 2027". Change "Two Sessions" to "China's annual parliamentary meetings". |
| 35 | Minor | §4 "Organon fertility fell 9% excluding currency." | No period is given. | raw/03 l.83: Q1 2026 | "…fell 9% excluding currency in Q1 2026" |

**Raw-file defects.** The note sends clients to `raw/`, so these should be fixed or annotated before release:
- R1. raw/01 l.179: "A Beijing court upheld the ban in October 2025 (Xu Zaozao case)" is **wrong**. The Third Intermediate People's Court in Beijing rejected her final appeal on **7 Aug 2024** (HKFP, France24, Sixth Tone). The note is correct.
- R2. raw/01 l.140: "at US return rates of 6-28%". The 28% figure is Australia/NZ, not the US.
- R3. raw/01 table: the 2021 growth shown as "+31%" works out to +46% (24,558 vs 16,786). The 2023 growth shown as "+39.2%" works out to +31.8% (39,269 vs 29,803) or +27.9% (38,126 vs 29,803). Raw/02 repeats "+39%".
- R4. raw/04 l.8 and l.36: the "+2.4% / -7.7%" attributed to the annual report are Q3 2025 figures. FY2025 was +0.4% / -6.7%, as raw/03 says (confirmed by search).
- R5. raw/04 (c): the Cooper arithmetic gives 0.13-0.22%, not "~0.2-0.5%".
- R6. raw/02 l.197 says "extra $1B buyback"; raw/03 l.123 says "$3bn buyback authorisation". Not reconciled.
- R7. raw/02 has RICHTER.BD and raw/03 has RICHT.BD (see #32).
- R8. Gameto conflicts between the raw files: raw/03 says 15 US sites, raw/04 says "up to 20". The lists of countries where it is cleared also differ (Argentina/Paraguay vs India/Singapore).

**Items that are correct:**
- Kitazato ticker 368A.T (confirmed on Yahoo).
- FY3/26 sales ¥10.95bn and operating profit ¥5.86bn (confirmed).
- Hamilton Thorne was taken private by Astorg, not Patient Square (raw/03).
- MVE was sold by Chart to Cryoport in Oct 2020 (raw/03; the note's "Cryoport (MVE)" is right).
- Sun/Organon: $14 cash, EV $11.75bn (confirmed).
- The other tickers: PGNY, VITR.ST, COO, MRK.DE, OGN, MVF.AX, 1951.HK, CYRX.

---

## (c) Arithmetic check

| Item | Note value | Recomputed | Result |
|---|---|---|---|
| Retrieval | $24,000 | 1.5 × $16,000 = $24,000 | OK |
| Storage | $5,300 | $750 × Σ0.95^k for k=1..9 (= 7.026) = $5,270 | OK (rounded) |
| Thaw/transfer | $2,400 | 20% × $12,000 = $2,400 | OK (20% is an assumption, see #8) |
| Fresh IVF | $1,800 | 20% × 40% × $23,000 = $1,840 | OK |
| 10-year total | $33,500 | $33,510 | OK |
| Split 72/16/7/5 | 72/16/7/5 | 71.6 / 15.7 / 7.2 / 5.5 | OK |
| US market size | ~$620M | 38,930 × $16,000 = $622.9M (retrieval only) | OK (see #27) |
| Two thirds elective | ~2/3 | 16,436 / 24,558 = 66.9% (2021); 2014: 4,153 / 6,100 = 68% | OK (dated ratio) |
| Elective $ (implied) | not stated | 0.669 × $623M ≈ $417M | OK vs raw/04's $415M |
| CAGR 2014-23 | ~23% | 6,100 → 39,269: 23.0%; 6,090 → 38,126: 22.6%; 6,100 → 38,000: 22.5% | OK |
| 2024 growth | ~2% | 38,930 / 38,126 = +2.1%; vs 39,269 = **-0.9%** | OK on the SART-final base; the base must be stated (#1) |
| Total ART growth | +1.4% | 431,746 / 425,869 = +1.38%; vs 432,641 = -0.2%; vs 415,953 = +3.8% | OK on the 425,869 base, which is unstated (#10) |
| Egg freezing share of ART (raw/04) | — | 38,930 / 431,746 = 9.0% | OK |
| Progyny cycles vs lives | +0.4% / +6.6% | 16,998 / 16,938 = +0.35%; 7.185 / 6.743 = +6.55% | OK |
| Progyny exposure | 5-11% | 10% × 0.6 × 0.8 = 4.8%; 15% × 0.8 × 0.9 = 10.8%; × $1.3725bn = $66-148m | OK |
| Kitazato exposure | 3-9% | 65% × 10% × 0.5 = 3.25%; 65% × 20% × 0.67 = 8.7%; ¥0.36-0.95bn ≈ $2.4-6.4m | OK (likely an upper bound, #30) |
| Kitazato vitrification sales | ~65% | ¥10.95bn × 65% = ¥7.1bn | OK (the 65% is unverified) |
| Kitazato operating margin | 53% | 5.86 / 10.95 = 53.5% | Minor rounding: say ~54% or 53.5% |
| Kitazato P/E | ~13x | ¥55bn / ¥3.90bn net profit (confirmed by search) = 14.1x; raw/03 has 13.4x | Approximately OK; better as "13-14x" |
| Vitrolife | 0.5-1% | 358/857 = 41.8%; 5% × 0.4-0.6 × 0.67 = 1.34-2.01% of consumables → 0.56-0.84% | OK (the 1% top end is generous) |
| Cooper | 0.2-0.5% | $560m × 5% × 0.3-0.5 × 0.67 = $5.6-9.4m ÷ $4.24bn = **0.13-0.22%** | **WRONG** (overstated; conclusion of under 1% unchanged) |
| Merck KGaA | ~0.2% | €1.4bn / €21.0bn = 6.6%; 25% × 6% + 75% × 2% = 3.0%; product 0.20% (€42m) | OK |
| Organon | ~0.3% | ($264m + $101m) / $6.2bn = 5.9% × 5% = 0.29% | OK ($6.2bn revenue is from memory, unverified) |
| Monash | 3-5% | 6,460 / 100k = 6.5% × 0.75 × 0.6 = 2.9%, plus storage | OK (100k total is unverified) |
| Jinxin | 2-4% | 25-35% × 10-15% × 0.8 = 2.0-4.2% | OK (HRC share is unverified) |
| Richter / Cryoport | <0.1% / <1% | ≤5% × 2% = ≤0.1%; ≤10% × 5-10% = ≤0.5-1% | OK |
| Indira offer size | 100% secondary | ₹29bn + 3 × ₹2bn = ₹35bn = ₹3,500cr | OK |
| China marriages | +10.8% | 6.76 / 6.1 = +10.8% | OK |
| Tax example | $4,400 on $20k | 22% federal marginal rate × $20k = $4,400 (an $80k earner stays in the 22% bracket); FICA adds about $1,530 | OK, but the assumptions must be stated (#15) |
| TrumpRx discount | "84% cut" / "up to 84%" | Raw dollar figures: $3.5-6k list → $1.5-3.5k, about 40-57% off; "$2,200 saved" on "typically $5,000" = 44% | "84%" is only the maximum company claim (#4) |

---

## (d) Claims that must carry an "unverified" caveat

1. **SART 2024 preliminary: 38,930 egg-freezing cycles and 431,746 total.** One snippet, found only by raw/04. Not retrieved by the other streams, and not confirmed in 2 QA searches.
2. **The 2023 baselines** (38,126 / 39,269 / ~40,000 egg-freezing cycles; 415,953 / 425,869 / ~432k total). Unresolved conflict; the note must name the one it uses.
3. **PRB 49.9% of women married, "since around 2010".** The year is unconfirmed.
4. **Kitazato's regional shares** (Japan 60%, Europe 70%, China 80%, India 85%) and possibly the 65% vitrification share. From an MOI Global/Latticework investor write-up. US share unknown.
5. **Kitazato's market cap and P/E (about ¥55bn, 13.4x), Vitrolife's multiples, and Progyny's $26.86 price and -14.3% move.** Aggregator data from a single source each.
6. **Kindbody's valuation "as low as about $400M"** and the sale/bridge reports. Undated, reported as a possibility.
7. **IFEBP employer egg-freezing coverage of 18% in 2026.** From a secondary website.
8. **The excepted-benefits rule "excludes elective freezing".** Raw/01 says "probably", and the rule text was not checked. It is a proposed rule.
9. **Every per-company elective-exposure %** in §1 and §3. These are analyst assumptions. Specific inputs are unverified: Organon revenue of about $6.2bn (from memory), Jinxin's US unit at 25-35% of revenue, ANZ total cycles of about 100k, and Cooper's Generate Life Sciences exposure.
10. **Lab consumables of $300-800 per cycle** and the drug-maker take of $2,500-4,500. Analyst estimates.
11. **The unit-economics model inputs:** 1.5 cycles per woman, 95% annual storage retention, 20% return rate, $12k thaw path, 40% thaw failure. All assumptions.
12. **TrumpRx "up to 84%".** A company claim, applying to cash purchases of the full three-drug protocol.
13. **Gameto Fertilo cutting stimulation to 2-3 days and a late-2026 interim readout.** Company claims and guidance.
14. **Monash's takeover "gone" or "cancelled".** One snippet in raw/04; raw/02 differs.
15. **Indira IVF "not yet listed".** True as of the latest results found, but not checked for 22 Sep 2026.
16. **PE clinic multiples (6-14x, previously 11-15x).** From M&A-adviser guides.
17. **"Egg and embryo freezing are the fastest-growing part of IVF".** No source at all; delete it or source it.
18. **Kitazato Q1 FY3/27 results** (if added per #33). From one search snippet.

Resolved by QA searches, so no caveat is needed once the text is corrected:
- Xu Zaozao's final appeal was rejected on 7 Aug 2024.
- Merck FY2025 fertility grew +0.4% organic, with Gonal-f -6.7%.
- Sun/Organon: $14 cash, agreed 26 Apr 2026, shareholders approved 23 Jul 2026, closing expected early 2027.
- The Kitazato ticker 368A.T and its FY3/26 sales and operating profit.
- Richter's exchange ticker is RICHTER.

