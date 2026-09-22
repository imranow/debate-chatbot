# QA review: 2026-09-19-robotics package (reviewed 22 Sep 2026)

No files were edited. I ran the model script, and my recomputation script is in the scratchpad at `/tmp/claude-0/-home-user-debate-chatbot/7d77e5a7-be3d-5eeb-89ce-9125f9e0b7ad/scratchpad/qa.py`. I used 7 of the 8 allowed web searches.

## (a) Verdict: FAIL

The model's tables are reproduced exactly. `projection-2030-model-output.md` matches the script output byte for byte. The section 3 table in `projection-2030.md` matches too, apart from Hesai's "0%" (the script prints "+0%" and "-0%"). The package still cannot go to the client, for three reasons:

1. **Wrong-currency Lynas market cap.** The Lynas cap in the model is in the wrong currency. The web check shows stockanalysis' 10.9B is **US$** (1.01B shares), not A$. Lynas' base case is therefore about -12% to -15%, not -6%, and it never breaks even below 20M units.
2. **Stale first-version text in the projection note.** Sections 4, 5 and 6 of `projection-2030.md` still carry text from the first version (confirmed against commit 11061f3). Those numbers contradict the corrected tables in the same note, and one row claims +15% and +18% returns where the model now gives -11% and -2%.
3. **Moat-map positioning contradicts section 9.** Sections 5 and 6 of the moat map still say to hold 2-3% "core" positions and 0.5-1.5% "sleeve" positions in names that section 9 now rates "Avoid" (MP, Huachen, Qinchuan, LG Innotek, LGES, Harmonic Drive, Leaderdrive, Sanhua).

On top of these there are several claims that are false or unsupported: MP "profitable for the first time", robots taking "30% of ex-China magnet demand", "every Western humanoid" running on Nvidia, and "triple-digit multiples" for Tuopu, Sanhua and Keli. There are also traceability gaps on Hesai's stale market cap and on base-income inputs. Most fixes are text edits plus one model input change (Lynas).

## (b) Defect table

P = `projection-2030.md`, M = `robotics-supply-chain-moats.md`, S = `scripts/robotics_2030_model.py`, O = `projection-2030-model-output.md`.

| # | Sev | Location (file, section, quote) | Problem | Evidence | Suggested fix |
|---|---|---|---|---|---|
| 1 | critical | S line 93 `Co("Lynas","LYC.AX","AUD",10_900,...)`; P §7 "Lynas (A\$10.9B, the only dated figure; an unconfirmed estimate of A\$14 to 15B would take its base case to about -14%)" | The market cap is in USD but tagged AUD, so the cap is understated by about 35%. | raw/07: "10.9B (stockanalysis ASX page; site convention = AUD)". raw/02: share price A\$15.54, cap about A\$14-15B. Web (stockanalysis/companiesmarketcap): "$10.9 billion with 1.01 billion shares. This figure is in USD"; AUD cap A\$14.07-16.5B. Recomputed: A\$14.07B gives -11.6% and 37x; US\$10.9B gives -14.9% and 44x; 0% breakeven becomes "never below 20M". | Set `market_cap_lc=16_500` (or put 10_900 in a USD row) and re-run all tables. Replace the §7 text with: "Lynas: US\$10.9B (stockanalysis, 10 Sep 2026; about A\$16.5B at 0.66), consistent with A\$15.54 x 1.01B shares." Update the P §1 and §3 rows, the breakeven table ("Lynas, MP ... about 10M to 13M"), and raw/08's -14% note. |
| 2 | critical | P §5 row "If deflation is slower (prices 2x the model), Leaderdrive and Keli move to +15% and +18% base-case CAGR" | First-version number. At 2x content prices the corrected model gives Leaderdrive -10.6% and Keli -2.4%. | Recomputed by doubling `content_usd`. Commit 11061f3 line 117 has the identical sentence. | "If deflation is slower (prices 2x the model), Leaderdrive improves to about -11% and Keli to about -2%; neither turns positive." |
| 3 | critical | M §6 "How to hold it" (whole section) and §5 ranking | Written before the review; contradicts §9's verdicts (see item 4 below for the full list). | M §9 table vs §6 bullets | Put a banner at the top of §5 and §6: "Superseded 22 Sep 2026: rankings and position buckets below pre-date the devil's-advocate review. Where they conflict, section 9's verdicts and the corrected `projection-2030.md` govern." Better: rewrite §6 as in item 4. |
| 4 | major | P §6 "Leaderdrive needs 1.6M units to be fair; buy it when ... takes 30 to 40% off" | Stale; the model says 3.3M. It also contradicts M §9, which rates Leaderdrive "Avoid". | Script breakeven 3.26M; v1 was 1.6M | "Leaderdrive needs 3.3M units to be fair, 3.7x Goldman's 2030 number; the review rates it 'avoid as a robotics play'." Drop the "buy it when" advice. |
| 5 | major | P §6 "Keep the moat ranking, change the sizing." | Contradicts M §9: "the moats in sections 4.2 and 4.3 are capacity moats being competed away faster than the original note allowed". | M §9 | "Keep the heavy-rare-earth and Nvidia moats; downgrade roller screws, grinders and harmonics (sections 4.2-4.3) to capacity moats being competed away, per section 9." |
| 6 | major | P §4 Hengli: "Screw revenue around CNY 3.4B on a CNY 20B company ... At 31x 2030 earnings today, the stock needs the bull case." | Stale v1. The model gives robot revenue CNY 1.4B on CNY 17.7B total, and 34x. The bull case is still -7%. Capacity is "3M sets" in P but 3.4M in raw/01. | Script: robo 197 USD M, rev 2,474, P/E 34.4x, bull -7.2% | "The largest roller-screw maker in China with 3.4M sets of capacity ... Screw revenue around CNY 1.4B on a CNY 18B company (8%) ... At 34x 2030 earnings, even the bull case (-7% a year) does not justify today's price." |
| 7 | major | P §4 Harmonic Drive: "prices 40% below today's ... The 52x multiple on 2030 earnings is the most demanding in the set outside the battery names." | 52x is v1; the model says 43x. Leaderdrive (78x), Huachen (57x), Allegro (57x) and Qinchuan (56x) are all higher. "40% below" conflicts with P §2, where $180 against $800-1,500 is 78-88% below. | Script P/E 43.4x | "...at prices roughly 80% below today's premium quotes ($180 vs \$800-1,500) ... The 43x multiple on 2030 earnings is demanding but below Leaderdrive, Huachen, Qinchuan and Allegro." |
| 8 | major | P §4 Leaderdrive: "from a CNY 571M company to a CNY 4B one ... if it does not, margin halves and the stock is worth a third of today" | Stale v1. The model gives 2030 revenue CNY 2.5B. On the base case the 2030 value is already 39% of today's cap; with margin halved it is 27%. | Script rev 353 USD M = CNY 2.52B; value/mcap 0.39 (base) and 0.27 (robot margin 14%) | "...to a CNY 2.5B one ... Even on the base case the 2030 value is about 40% of today's market cap; if the price war halves robot margin, about a quarter." |
| 9 | major | P §4 Huachen/Qinchuan: "about \$240M a year of precision-grinder capex at 900k robots ... at 45x and 49x 2030 earnings" | Stale v1: \$240M is 900k x the old \$270. Corrected pool is 375k addressable units x \$160 = \$60M. P/E is 57x and 56x. | Script units 375,000 x 160 = \$60M | "...(about \$60M a year of grinder capex at 900k robots, since only Western and a quarter of Chinese robots use screws) ... at 57x and 56x 2030 earnings." |
| 10 | major | P §3 breakeven table: "Sanhua, Qinchuan, LG Innotek, LG Energy Solution, Allegro \| never below 20M \| never" | Sanhua reaches breakeven at 16.9M units. | Script/O line 37 "Sanhua \| 16.9M \| never below 20M" | Add a row "Sanhua \| 16.9M \| never below 20M" and remove Sanhua from the grouped row. Also change "never" to "never below 20M" throughout. |
| 11 | major | P §4 "Nabtesco, LG Innotek, LG Energy Solution, Allegro, Sanhua. Humanoids stay under 5% of revenue in every scenario." | False in the bull case: Sanhua 11.8%, Nabtesco 9.1%, Allegro 5.3%. P §5 itself says Sanhua reaches 12% at 400k Tesla units. | Recomputed bull robo_share | "...Humanoids stay under 5% of revenue in the base case (under 12% even in the bull case)..." |
| 12 | major | P §5 "Each doubling adds roughly 8 to 12 points of CAGR to Leaderdrive, Keli, Wuzhou and Harmonic Drive" | Stale v1. Doubling 900k to 1.8M adds Wuzhou +10.8, Leaderdrive +9.4, HDS +7.2, Keli only +2.8 points. The others get <=1.6 points, so that part is correct. | Recomputed | "Each doubling adds about 9 to 11 points to Wuzhou and Leaderdrive, about 7 to Harmonic Drive, about 3 to Keli, and under 2 to everyone else." |
| 13 | major | P §4 Lynas "About A\$1B of revenue with 20 to 30% of it from heavy rare earths" | The model's 2030 revenue is US\$990M, about A\$1.5B. The 20-30% HRE share has no source. | Script rev 990 USD M / 0.66 = A\$1,500M | "About A\$1.5B (US\$1.0B) of 2030 revenue; the heavy-rare-earth share is an analyst assumption..." |
| 14 | major | P §4 MP: "Revenue around \$1.3B to \$1.5B, profitable for the first time." | MP reported net profits in 2021 and 2022 (reviewer knowledge; not in the raw files). | raw/02 gives only 2026 losses | "...returning to profit (it last earned a profit in 2022)." |
| 15 | major | P §4 MP: "Robots take perhaps 30% of ex-China magnet demand by then" | No source, and it contradicts the model: 200k robots x 3.5 kg = 700 t, while MP's 10X alone is about 10,000 tpa (raw/02). MP's robot revenue is \$34M (2%). | Model inputs; raw/02 | Delete the sentence, or replace with: "Robots are a small share of ex-China magnet demand (about 700 t at 200k Western units)." |
| 16 | major | P §2 "Bear is roughly where Morgan Stanley's China-only 446k plus a slow West lands." | The bear case is 300k in total (240k Chinese), below MS's China-only 446k. MS plus a slow West falls between bear and base. | P §2 table; raw/07 MS 446k | "Bear (300k) is below Morgan Stanley's China-only 446k; MS plus a slow West would sit between bear and base." |
| 17 | major | P §1 "on Goldman's base case of about 900,000 humanoids a year (200,000 of them from Western OEMs, 120,000 from Tesla)" | The Western/Tesla split is the analyst's assumption; Goldman gives only 890k (raw/06, via 247wallst). | raw/06 | "...on Goldman's 890k 2030 forecast (the 200k Western / 120k Tesla split is our assumption)..." |
| 18 | major | P §2 table column "Broader embodied multiplier (lidar, compute)"; S `embodied` pool | No company uses pool "embodied" after the Hesai fix, so `embodied_mult` has no effect. The column implies it drives lidar and compute. | S lines 64-65; every ASSUMPTIONS `pool` value | Delete the column (or add "(not used after 22-Sep correction)"), and remove `embodied_mult` from SCENARIOS. |
| 19 | major | P §7 caveats; P §3 Hesai row; M §9 "Hesai \| Least-bad robot-exposed name" | Hesai's \$2.92B cap is undated and flagged "looks stale" in raw/03 and raw/07. P never says so, yet Hesai is the "least-bad" call. At a cap 1.5x higher, the base case is -9%. | raw/03 (c)3; web search returned a conflicting ~21.3B figure (currency unclear) and an ADS ratio change to 1:8 | Add to §7: "Hesai's \$2.92B cap is undated and likely stale; the Hesai verdict must be re-checked against a dated cap before use." |
| 20 | major | M §2 "every Western tier-1 humanoid ships on it"; M §5 Nvidia "lock-in on every Western humanoid"; P §4 "Jetson Thor's successor sits in most Western humanoids"; S Nvidia `pool="western"` at 85% share | Tesla Optimus uses Tesla AI5 (M §4.8, raw/04), and Tesla is 120k of the model's 200k Western units. The same applies to LG Innotek at 50% share: Samsung Electro-Mechanics supplies Optimus (raw/03). | raw/04 table: "Tesla AI5 (captive)"; the non-Tesla Western pool caps share at 40% | "Standard on most non-Tesla Western humanoids (Figure, Agility, Boston Dynamics, 1X); Tesla uses its own AI5." In the model, use a non-Tesla pool (western minus tesla) for Nvidia and LG Innotek. Immaterial to their CAGRs. |
| 21 | major | M §6 "Trade, not hold: Harmonic Drive, Leaderdrive, Tuopu, Sanhua, Keli. These are momentum vehicles ... with triple-digit multiples" | Only HDS (186x) and Leaderdrive (364x) have triple-digit multiples. Tuopu is about 36x, Sanhua about 49x, Keli about 55x. | raw/07 cap and NI; raw/03 Keli 55x | "...HDS and Leaderdrive trade on triple-digit trailing multiples; Tuopu, Sanhua and Keli on 35-55x." |
| 22 | major | S line 41 `base_ni_lc` (never used); ASSUMPTIONS Schaeffler NI `0`, Nvidia `226_000`, HDS `5_900`, Huachen `60`, Allegro `100` | These base NI inputs are not in any raw file, or contradict it. Schaeffler's TTM is a loss (EPS -\$0.47, about -\$444M on 945M shares). The field feeds nothing: 2030 base NI = revenue x assumed margin. | raw/07: Schaeffler NI "NOT FOUND (TTM EPS -\$0.47)"; HDS FY3/26 NI ¥1,608M; Huachen NI "NOT FOUND"; no NVDA NI | Delete `base_ni_lc`, or label each entry "(est.)". Fix the docstring. Add to P §7: "Base-business 2030 income is an assumed margin, not linked to current profits." |
| 23 | major | P §4 Schaeffler "exactly the 'three-digit millions' management has guided. The investment case is the group margin recovering from zero to 3%" | Management guided an **order book** of three-digit millions of euros by 2030, assuming at least 1M units a year of industry output (raw/01), not revenue. The group is loss-making on a TTM basis, not at zero. | raw/01 Ewellix para; raw/07 | "...consistent with management's target of a three-digit-million-euro humanoid order book by 2030 (which assumes ≥1M industry units). The case is the group margin recovering from a TTM loss to 3%..." |
| 24 | major | P §2 "harmonic reducers at \$85 Chinese and \$180 premium (from \$800 to \$1,500)"; "six-axis force sensors at \$420 (from about \$4,500)" | \$800-1,500 is the high-end quote. The Chinese ASP is already CNY 573-1,100 (about \$80-155; raw/01 Laifual and Bernstein), so \$85 implies little further deflation. \$4,500 is the **2022** F/T average (CNY 32k). | raw/01; raw/03 | "...harmonics at \$85 Chinese (today CNY 573-1,100, about \$80-155) and \$180 premium (today \$800-1,500); force sensors at \$420 (CNY 32k, about \$4,500, in 2022)." |
| 25 | major | P §7 "the lower figure was used, except Keli (CNY 20.0B, midpoint of CNY 18.8B to 22.5B)" | The midpoint of 18.8 and 22.466 is 20.6, not 20.0. Leaderdrive is also an unlisted exception: the model uses CNY 53.28B (16 Sep), but raw/01 has 51.3B, and the NI of 141 is inferred from 51.3B/364x. | raw/01, raw/03, raw/07. Leaderdrive at 51.3B: -19% base, 3.1M breakeven | "...Keli (CNY 20.0B, between CNY 18.8B and 22.5B) and Leaderdrive (CNY 53.3B, the latest dated figure; raw/01 shows 51.3B)..." |
| 26 | major | S line 20 `YEARS = 4.25`, applied to all bases; P "four-year return" | Forward bases (Nvidia FY27, MP 2026 consensus, HDS FY3/27 guidance) are over-compounded, and FY2025 bases under-compounded. The audit flagged this (raw/08 §c10); it is still unfixed and undisclosed. | S; raw/08 | Add to P §7: "All bases are compounded 4.25 years whether trailing or forward (about ±1pt CAGR)." Optionally add a per-company `years` field. |
| 27 | major | M §9 "Chinese regulators have informally frozen humanoid IPOs"; "Stripping that revenue out could cut some valuations by 60 to 70%" | Reuters says regulators used window guidance to "hold back some listings" (a slowdown, not a freeze). The 60-70% figure is Mech-Mind's CEO (raw/08), not Reuters or regulators. | Web: Reuters 20 Sep 2026 "China slows humanoid robot IPO rush"; raw/08 line 8 | "...have used informal window guidance to slow humanoid IPOs ... Mech-Mind's CEO said stripping that revenue out could cut some valuations by 60 to 70%." |
| 28 | minor | M §3 and §5 "Unitree ... roughly \$50B" | Stale against §9 "down about 55% from its post-IPO peak". | M §9; web (Reuters) | Add "(at the Aug 2026 debut; down about 55% from peak by 20 Sep)". |
| 29 | minor | P §1 pt 2 "three to nine times Goldman's number" | 2.3M/0.89M = 2.6x and 7.9M/0.89M = 8.9x. | Arithmetic | "2.6 to 9 times". |
| 30 | minor | P §3 "halving them takes Leaderdrive's bear case to about -35% ... at 17% and 20x, Leaderdrive's base case is about -35%" | These figures come from the audit's intermediate model. The corrected model gives -40% and -32%. | Recomputed | "about -40%" and "about -32%". |
| 31 | minor | P §5 "Every 5 turns of exit multiple is worth about 5 points of CAGR" | At 20-30x, 5 turns is worth 3-5 points (Leaderdrive +3.0, HDS +3.9, Keli +4.2, Wuzhou +4.5). | Recomputed | "about 3 to 5 points". |
| 32 | minor | P §3 "the most bullish Street house does not expect until the early-to-mid 2030s" | BofA's 10M by 2035 (raw/07) is more bullish than Goldman's 6.5M. | raw/07 | "...a volume Goldman does not expect until the early-to-mid 2030s". |
| 33 | minor | P §3 Hesai row "0% \| ... \| 0%" | The script prints "+0%" and "-0%"; the "-0%" is a formatting artefact. | O line 12 | Keep "0%" but fix the script formatter so it never prints "-0%". |
| 34 | minor | P §4 Hesai "Robotics lidar is about 10% of a \$1.1B revenue base by 2030" | Model revenue is \$1.02B and humanoid lidar is 3%. The 10% is not modelled. | Script | "...about \$1.0B of 2030 revenue; humanoids are about 3%, all robotics lidar perhaps 10% (our estimate, inside the base growth rate)". |
| 35 | minor | P header "Model date 19 September 2026"; P §1 "the first version's numbers are in git history" | Revision date is inconsistent, and a client note should not point to git. | P §1 banner | "Model date 19 Sep 2026, revised 22 Sep 2026"; "first-version figures available on request". |
| 36 | minor | M §9 "all seven research streams" vs M header "Six parallel research streams" | Inconsistent count: raw/07 is a data pull, not a stream. | M header | "all six research streams and the financial data pull". |
| 37 | minor | S lines 89-91 comment "see raw/07-financials.md"; S `share_mult` parameter | Wrong filename; dead parameter. | S | "raw/07-financials-2026-09-19.md"; remove `share_mult`. |
| 38 | minor | S line 31 `FX` | Unsourced and undated. Raw-implied rates differ: CNY about 0.15 from the Dy quotes in raw/07; KRW about 0.00078 from the LGES pair. CAGRs are FX-invariant, but robot share of revenue is not. | raw/07 | Add a source and date for FX, or label it "assumed". |
| 39 | minor | S Huachen/Qinchuan `use_cn=0.25` vs Leaderdrive `use_cn=0.50` | The note says grinders serve robots using screws **or** harmonics, so the Chinese share should be at least 50%. The current value is conservative. | S notes | Use 0.50, or explain why 0.25. |
| 40 | minor | S Leaderdrive `pool="chinese"`; HDS `pool="western"` at 45% | raw/01 and raw/06 report Leaderdrive as Tesla's primary Chinese harmonic supplier ("~60% of Optimus reducer supply", unverified). The model gives Tesla harmonics to HDS and none to Leaderdrive. | raw/01 §1 | Document it as a deliberate choice, or split the Tesla pool. |
| 41 | minor | M §4.9 "EVE ... ships 300 Wh/kg semi-solid cells" | raw/02 says all-solid-state (ASSB) Longquan II. | raw/02 | "300 Wh/kg all-solid-state cells". |
| 42 | minor | M §4.1 "Tesla ... has not publicly confirmed resolution" | raw/02 dates this "as of March 2026", six months stale. | raw/02 | Add "(as of March 2026)". |
| 43 | minor | M §4.7 and §9 "US-listed Hesai"; M §4.7 RoboSense; M §4.9 EVE | Web: Hesai also listed in Hong Kong in Sep 2025. RoboSense and EVE Energy were added to the DoD 1260H list in June 2026 alongside Unitree. None of this is in the raw files. | Web (WilmerHale/MoFo/TNW 1260H update; Barchart on Hesai HK) | Add "(also HK-listed)" for Hesai; add a 1260H caveat for RoboSense and EVE after verifying. |
| 44 | minor | M §6 "Core ... 2 to 3% each"; "Sleeve 1 to 1.5%" | Specific position sizes read as advice, despite "framework, not advice". | M §6 | Remove the percentages, or add "illustrative only; not a recommendation". |
| 45 | minor | M §4.8 "\$5.4T company" vs model \$5.31T | Two sources with no date. | raw/04 \$5.37T; raw/07 \$5.31T (18 Sep) | "\$5.3T (18 Sep 2026)". |

**Internal-consistency list for check 4 (section 5/6 against section 9 and the corrected projection):**
- MP: §5 ranks it #3, moat "A (policy)"; §6 puts it in Core at 2-3%. §9 says "Avoid as robotics play".
- Lynas: §5 ranks it #1; §6 Core at 2-3%. §9 says "Policy trade only; wait for summit and 10 Nov".
- Hengli: §5 ranks it #4, A/B; §6 Sleeve. §9 says "Only on a big drawdown".
- LG Innotek and LGES: §6 Sleeve. §9 says Avoid.
- Huachen and Qinchuan: §5 #6 "A (tooling)"; §6 Tooling sleeve. §9 says Avoid.
- HDS, Leaderdrive, Sanhua: §6 "Trade, not hold". §9 says Avoid.
- Tuopu and Keli: §6 "Trade". §9 says "only on a big drawdown".
- §6 "Avoid at current prices: the list at the end of section 5". That list omits the ten names §9 now rates Avoid.
- §1 and §2 call precision grinding a "genuine"/"durable" moat, and the §4.2 heading says "moat A". §9 says the 4.2/4.3 moats "are capacity moats being competed away".
- §9 opening says the findings "change the risk picture more than the moat ranking". The verdicts that follow overturn most of §6.
- P §6 "Trade the reducer and screw names on drawdowns" contradicts M §9's Avoid for HDS and Leaderdrive.

**Minimal fix:** (1) Put the superseded banner from item 3 at the top of M §1, §5 and §6. (2) Rewrite M §6 to mirror §9:
- Core policy/data-centre: Nvidia, Schaeffler.
- Policy trade after 24 Sep / 10 Nov: Lynas.
- Big-drawdown watchlist: Tuopu, Hengli, Nabtesco, Keli.
- Avoid as robotics plays: MP, Wuzhou, Huachen, Qinchuan, HDS, Leaderdrive, Sanhua, LG Innotek, LGES, Allegro.

(3) Add a "22-Sep verdict" column to the §5 table.

## (c) Model check table

| Item | Note value | Script value | OK/WRONG |
|---|---|---|---|
| O (whole file) vs script stdout | table + breakevens | identical | OK |
| P §3: mcap, 2030 rev, robot rev, robot %, NI, P/E, base/crash/bear/bull CAGR, 17 names | as printed | identical | OK |
| P §3 Hesai base / bear | 0% / 0% | +0% / -0% | OK (format) |
| Hand recompute: Lynas | 7,194 / 990 / 22 / 250 / -6% | 7,194 / 989.9 / 22.05 / 249.7 / -6.15% | OK (but see item 1: wrong input) |
| Hand recompute: Keli | 2,800 / 412 / 59 / 89 / 31x / -5% | 2,800 / 411.9 / 58.8 / 89.4 / 31.3x / -5.2% | OK |
| Hand recompute: Harmonic Drive | 3,726 / 876 / 227 / 86 / 43x / -12% | 3,726 / 875.8 / 226.8 / 85.9 / 43.4x / -12.2% | OK |
| Breakevens: 16 names in P §3 | as printed | match | OK |
| Breakeven: Sanhua | "never below 20M" | 16.9M / never | WRONG |
| Breakeven: Lynas, MP | "about 10M to 13M" / "never" | 9.9M, 13.4M / never below 20M | OK (Lynas becomes "never" after the item 1 fix) |
| P §1 material names | 4 of 18; Leaderdrive 59, Wuzhou 29, HDS 26, Keli 14; Hengli 8, Huachen 7 | same | OK |
| P §1 Nvidia robot share | 0.05% | 0.046% | OK |
| P §1 units range and multiple | 2.3M-7.9M; "three to nine times" | 2.3-7.9M; 2.6-8.9x | minor |
| P §1 Dy/Tb tonnes | 21 t | 200k x 0.105 kg = 21 t | OK |
| P §4 Hengli | CNY 3.4B / CNY 20B / 31x | CNY 1.4B / 17.7B / 34x | WRONG |
| P §4 HDS | ¥130B / 52x | ¥128.8B / 43x | rev OK, P/E WRONG |
| P §4 Leaderdrive | CNY 4B; ASP CNY 600 | CNY 2.5B; \$85 = CNY 607 | WRONG / OK |
| P §4 Wuzhou | 29%, 41x | 29%, 41x | OK |
| P §4 Tuopu/Sanhua | 4% | 3.9% | OK |
| P §4 Keli | 14%, 31x, 2.6M | same | OK |
| P §4 Hesai | 10% of \$1.1B | 3% of \$1.02B | WRONG |
| P §4 Lynas revenue | A\$1B | US\$990M = A\$1.5B | WRONG |
| P §4 grinder pool / P/Es | \$240M; 45x, 49x | \$60M; 57x, 56x | WRONG |
| P §4 Nvidia physical AI \$30-50B | 4-7% of \$740B | 4.0-6.7% of \$745B | OK |
| P §5 doubling | 8-12 pts for 4 names; <2 others | 10.8 / 9.4 / 7.2 / 2.8; others <=1.6 | WRONG (Keli, HDS) |
| P §5 prices 2x | Leaderdrive +15%, Keli +18% | -10.6%, -2.4% | WRONG |
| P §5 Tesla 30k / 400k | 1% / 12% | 1.0% / 11.9% | OK |
| P §5 5 turns of exit multiple | ~5 pts | 3.0-4.5 pts | minor |
| P §5 Dy/Tb parity cut | 85% | 1 - 220/1500 = 85.3% | OK |
| P §3 audit sensitivities | Leaderdrive half-P/E bear -35%; 17%/20x -35%; Schaeffler 2% -5% | -39.8%; -31.9%; -4.6% | WRONG / WRONG / OK |
| P §7 Lynas at A\$14-15B | about -14% | -11.5% to -12.9% (at US\$10.9B: -14.9%) | WRONG |
| P §6 Leaderdrive breakeven | 1.6M | 3.3M | WRONG |
| M §9 Schaeffler | about 8x 2030 earnings | 8.2x | OK |

**Code review (S):**
- Unit pools, `use_west`/`use_cn` and the bisection are correct. The bisection runs 60 iterations, is monotone in units, and scales western and tesla units proportionally.
- NaN handling maps to -1.0. The 'n/a' label (breakeven = 0) and 'never' label (None) are correct.
- Bugs and design issues, all detailed in the defect table: unused `base_ni_lc` (22); unused `embodied` pool and `embodied_mult` (18); dead `share_mult` (37); uniform YEARS compounding (26); Nvidia and LG Innotek Western pools include Tesla (20); unsourced FX (38); the `-0%` formatter (33).

## (d) Claims that must carry an "unverified" caveat

1. Tuopu is Tesla's "exclusive" linear-actuator supplier, with 60% of Optimus reducers and CNY 1.5B first orders. This comes from Chinese brokers and media (raw/01 (c)2, raw/05 (c)2). M §4.6 and the S note state it as "(reported exclusivity)". It needs a clear caveat.
2. Wuzhou is Tesla's "designated" roller-screw supplier (over 30 screws per robot); Hengli's "Tesla-validated samples" (36kr); Leaderdrive as Tesla's primary harmonic supplier. None is confirmed by Tesla (M §8 says so, but §4.2 states it as fact).
3. Tesla audit "~5,000-unit order" and "2026 plan of about 50,000 units".
4. Optimus Gen-3 uses 14 PRS mainly from GSA (single source, kggfa).
5. Schaeffler's August 2026 strain-wave manufacturing process with mass production from 2027 (single blog, jamesm.blog). M §4.2, §5 and §7 and P §4 state it as fact.
6. Jetson Thor as "the standard on Figure" (Figure 03 uses a custom chip per a RoboZaps blog) and "every Western tier-1 humanoid ships on it".
7. Nvidia's physical-AI run-rate "about \$10B today by its own account": the source is secondary, not an Nvidia filing.
8. Musk's 1M-a-year Fremont capacity and 1,000-1,200 units deployed (fan-site aggregation, raw/04 (c)6).
9. Figure's ~3k/yr run-rate in April 2026 (Sacra/Axis aggregators, raw/06 (e)3).
10. 1H26 shipments of 19,100 and AgiBot 44% / Unitree 31% (single tracker; may include wheeled robots).
11. Goldman's 890k (2030) and 6.5M (2035): seen only via 247wallst; the note was not read.
12. Hyundai's "30,000-unit" plant: this may be all robots, not humanoids only (raw/06 (e)8).
13. Keli as an "alternative Optimus F/T supplier" (optimusk.blog), and the S assumption that 40% of Chinese robots carry F/T sensors (analyst estimate).
14. Chinese roller-screw capacity "about six times 2026 demand": this is the devil's advocate's own upper-bound arithmetic.
15. PEEK "about 11 kt at 1M units" (vendor blog).
16. Market caps: Hesai (undated and likely stale; web gave a conflicting figure); Hengli, Wuzhou, Qinchuan, Tuopu, LG Innotek (undated); Sanhua (2 Mar 2026) and LGES (2 Apr 2026), both stale; Keli (midpoint of undated or Sep-2025 figures). Also Leaderdrive's FY2025 net income (inferred).
17. Schaeffler's €0.88 consensus EPS (year not stated); Hesai's 2027 consensus EPS (currency suspect).
18. Unitree's day-one move of +460% (a conflicting +629% figure exists, raw/04 (c)8).
19. Moog "mispriced as humanoid" (a single Seeking Alpha opinion).

Already correctly caveated: Energy Fuels-VAC, Luxshare, Sanhua's CNY 5B order (denied), and screw revenue as a broker forecast.

**Web adjudication, 7 of 8 searches used:**
- Lynas: stockanalysis' 10.9B is US\$, so item 1 is confirmed.
- FCC ban on new foreign humanoid and quadruped models, 28 Jul 2026: confirmed.
- Unitree on the 1260H list: confirmed. The DoD list is dated 8 Jun 2026 and was published about 10 Jun; RoboSense and EVE were added at the same time.
- Reuters, 20 Sep 2026: confirmed, but it describes a "slowdown/window guidance", not a freeze.
- Trump-Xi state visit 23-25 Sep 2026 (summit on 24 Sep) with the 10 Nov deadline: confirmed.
- Hesai market cap: unresolved. It conflicts with a \$21.3B snippet of unclear currency and an ADS ratio change to 1:8, so it must be re-sourced.

Sources: [stockanalysis LYC](https://stockanalysis.com/quote/asx/LYC/market-cap/), [companiesmarketcap Lynas AUD](https://companiesmarketcap.com/aud/lynas/marketcap/), [PBS on the FCC ban](https://www.pbs.org/newshour/world/u-s-bans-foreign-made-humanoid-robots-targeting-china-over-national-security), [Forbes on the FCC ban](https://www.forbes.com/sites/johnkoetsier/2026/07/28/united-states-bans-chinese-humanoid--quadruped-robots-citing-national-security/), [BusinessWorld/Reuters on the IPO slowdown](https://bworldonline.com/technology/2026/09/21/780046/china-slows-humanoid-robot-ipo-rush-as-hype-outruns-reality/), [US News on the summit](https://www.usnews.com/news/national-news/articles/2026-09-21/trump-and-xi-meet-in-washington-under-shadow-of-ai-trade-and-rare-earth-tensions), [WilmerHale on the 1260H update](https://www.wilmerhale.com/en/insights/client-alerts/20260611-pentagon-adds-65-new-entities-to-the-1260h-list-of-chinese-military-companies), [DoD 1260H list PDF](https://media.defense.gov/2026/Jun/08/2003945537/-1/-1/1/ENTITIES-IDENTIFIED-AS-CHINESE-MILITARY-COMPANIES-OPERATING-IN-THE-UNITED-STATES-IN-ACCORDANCE-WITH-SECTION-1260H.PDF), [stockanalysis HSAI](https://stockanalysis.com/stocks/hsai/market-cap/), [Simply Wall St HSAI](https://simplywall.st/stocks/us/automobiles/nasdaq-hsai/hesai-group).

**Files reviewed:** `/home/user/debate-chatbot/reports/stocks/research/2026-09-19-robotics/{robotics-supply-chain-moats.md, projection-2030.md, projection-2030-model-output.md, raw/01-08}` and `/home/user/debate-chatbot/scripts/robotics_2030_model.py`.
