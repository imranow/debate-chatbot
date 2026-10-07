# Meta-QA review: Hims & Hers QA (7 Oct 2026)

*Stream 06. I checked the QA report `raw/05-qa-review.md`, which gave "PASS WITH FIXES" with 39 defects. Pre-fix note: commit 6c41ade. Post-fix note: commit 2f09e1c. The raw files are unchanged since 2f09e1c, and the working tree is clean. I string-matched every QA quote against the pre-fix note and every replacement against the post-fix note. All 39 quotes appear exactly once in the pre-fix note. I ran `python3 -I raw/01-valuation_model.py` and recomputed every number in scratch scripts (`scratchpad/mq_quotes.py`, `mq_recompute.py`). I made 4 web searches, only to check facts the QA brought in. No repo file was edited except this report.*

---

## (f) Verdicts

**QA report: RELIABLE WITH CORRECTIONS.**
- 29 of 39 defects are confirmed, 8 are partly right and 2 are overstated. None is wrong.
- Every quote matches. The model and nearly all the QA arithmetic reproduce.
- But several replacement texts added new errors:
  - The headline range now contradicts §7 and its own −3% figure.
  - "Highest-margin" contradicts the note's §2 table.
  - An undated 2025 Lilly statement is presented as if it were current.
  - "(to check)" was left in published text.
  - An organic-growth bound has rounding drift.
  - A false causal claim about leverage was carried over into the bear-case rewrite.

**Post-fix note fit to publish: YES WITH FIXES.**
- The call ("not cheap enough for the risks") holds on every recompute.
- Before it is published, fix:
  - the central-range contradiction between §1 and §7, which is also synced into the bank-views note;
  - the bear-case "because of leverage" claim in §1 and §6;
  - "highest-margin";
  - the Lilly and DEA rows.
- All are text edits.

---

## (a) Ruling on the 39 QA defects

Quote check: all 39 QA quotes are in the pre-fix note exactly once. Rulings judge whether the problem is real. Where a replacement text added a new error, the ruling says so and points to table (d).

| # | Ruling | Note |
|---|---|---|
| 1 | CONFIRMED | "0–6%" did not match the −1% stock-pay base or raw 04's "0–5%". But the new range leaves out the −3% figure it quotes, and it disagrees with #2 (see F1). |
| 2 | CONFIRMED | Self-contradiction is real. But the replacement ("−1% to +5%") disagrees with #1 ("−1% to +6%") (see F1–F2). |
| 3 | PARTLY | Base subscribers at an 8% margin give −6.0% a year (grid), about −23% in total. So "large losses" is loose, not false. The rewrite keeps a false cause ("because about $2.1B … sit ahead") and drops the "before stock pay" basis (see F4, M1). |
| 4 | CONFIRMED | Eucalyptus $40M is 19.2% of the $208.4M growth and 32.3% of the international growth. "Mostly through acquisitions" is an untagged inference (F10). |
| 5 | PARTLY | The mismatch is real. But the central range recomputes to +7.8% to +11.4%, so the original "+8% to +11%" was right. The QA's "+12%" comes from using 0.17M rather than 0.175M (F9). |
| 6 | PARTLY | As #5. |
| 7 | CONFIRMED | Raw 02 (b): the 30/50/20 odds are for regulatory scenarios. Arithmetic: $40.96, +8.15%. |
| 8 | CONFIRMED | As #7. |
| 9 | CONFIRMED | Raw 04 (d) "Fully fixed base". Reproduced: $25.63, −3.20%. |
| 10 | CONFIRMED | Raw 03 §2.8: "retail and NovoCare, including telehealth". The fix leaves "The makers' channels are large" resting on one 2025 data point (F7). |
| 11 | CONFIRMED | 7,421 / 114.4 = 64.9. |
| 12 | CONFIRMED | Bank raw 02: GS and JPM "nf". Lending is not given as the reason. |
| 13 | CONFIRMED | BofA "$37 undated, before Q2 results". Canaccord "~mid-2026". The Stifel point does not matter: the bank file gives no Stifel rating to add. |
| 14 | PARTLY | "Capped at −$29" is true (the most anyone can lose is the $29.40 price), but it was set against bear and bull values. The fix is fine: 7.01 − 29.40 = −22.39. |
| 15 | CONFIRMED | A 0% return is breakeven, not "fair". |
| 16 | CONFIRMED | Full solve: $25.33 / $17.99. Simple discount: $25.56 / $18.69. "$18–19" is right. |
| 17 | CONFIRMED | 874 / 58.88 = 14.8 months. 2,000 / 58.88 = 34. 5,900 / 58.88 = 100. |
| 18 | CONFIRMED | Raw 01 §2: "24% in Q4 2025". |
| 19 | CONFIRMED | $349: 26.9%. $249: 33.7%. $199: 38.5%. |
| 20 | CONFIRMED | Raw 01 (b) says "8-K vs 10-Q wording". Raw 04 (f)4 says 10-K. "Deal terms (Feb 2026)" is a safe neutral wording. |
| 21 | OVERSTATED | "Novo … saying Hims was selling…" already attributed the claim to Novo. The replacement quote is still more accurate (raw 02 §1). |
| 22 | PARTLY | The prescribe-versus-sell split is right for 2026. Web check: Hims routes prescriptions to LillyDirect from 23 Apr 2026. But the QA ignored raw 02's 2025 entry (Hims listed Zepbound at about $1,899 a month). It also imported Lilly's statement of **1 Apr 2025** without a date, which duplicates Hims' own disclaimer (F5). |
| 23 | PARTLY | Enclomiphene is non-controlled (bulk listings, web). But "branded oral testosterone was only planned" goes beyond raw 03 ("launch not confirmed"). Kyzatrex is Schedule III and Hims has a Kyzatrex drug page. The fix also left "(to check)" in the published text (F6). |
| 24 | CONFIRMED | Raw 04 R5. |
| 25 | CONFIRMED | Raw 04 (f)4 [10-Q; beancount.io]. §7 still states the $90 figure untagged (F11). |
| 26 | CONFIRMED | Raw 04 B2 marks it "(estimate)". |
| 27 | CONFIRMED | 14 × 14 / 10 = 19.6x. 14 × 14 / 8.2 = 23.9x. |
| 28 | CONFIRMED | Raw 01 §5: $407M from StocksGuide only. |
| 29 | PARTLY | Raw 03 [S3] attributes the 65% / 1.6M to the company. I did not re-check the QA's web claim that 65% is a third-party figure. 1.6 / 2.511 = 64%, so the fix is harmless either way. |
| 30 | CONFIRMED | Raw 02 §3.4 says "My read". |
| 31 | CONFIRMED | Raw 01 §6: the margin is adjusted EBITDA. |
| 32 | CONFIRMED | $53.82, +15.37%. |
| 33 | PARTLY | The balancing CEO quote is real (raw 01 §2 [S27]). But "highest-margin" contradicts §2, where generics earn 85–90% against about 80% for compounded semaglutide (F3). |
| 34 | CONFIRMED | Raw 03 §2.8 [S51]: Q2 2025. |
| 35 | CONFIRMED | Raw 02 §1 and §4.1. |
| 36 | CONFIRMED | Raw 01 §4.3: 19 Aug, 4,938 shares. Raw 03 §5.3: 1 Oct, 2,000 shares. |
| 37 | CONFIRMED | Jargon. The gloss is acceptable. |
| 38 | CONFIRMED | Jargon. The gloss matches raw 02 §2.2–2.3. |
| 39 | OVERSTATED | Raw 02 (a)3 says "Novo, FDA and HHS all attacked that". The original wording was supported. The fix is harmless. |

Tally: 29 CONFIRMED, 8 PARTLY, 2 OVERSTATED, 0 WRONG.

**QA web facts.**
- Jon Franklin 8-K: confirmed. A Hims 8-K dated 7 Oct 2026 names Franklin principal accounting officer from 9 Oct 2026; he was a Rivian VP and Corporate Controller. The note's "(8-K)" is correct.
- Zepbound dispensed by LillyDirect: confirmed for 2026. The routing was announced 23 Apr 2026. Hims' own release lists only Zepbound and Foundayo; Mounjaro appears only in FierceHealthcare.
- Lilly "no affiliation": the statement exists, but it is dated **1 Apr 2025** and was about Hims' earlier Zepbound listing. It is not about the 2026 arrangement.
- "Over 1.6M" personalised: not re-checked (budget). Harmless either way.

---

## (c) Recompute table

The model output matches raw 01 exactly. "Note" means the post-fix note.

| Item | Note | Recomputed | OK? |
|---|---|---|---|
| Bear / base / bull | $7, −29% / $38, +6% / $99, +33% | $7.01, −28.8% / $38.26, +6.4% / $98.62, +33.1% | Yes |
| Management plan | $67, +21%; +15% after stock pay | $66.64, +21.3%; $53.82, +15.4% (margin 16%) | Yes |
| Base after stock pay, 4% / 5.8% | $28, −1% / $23, −5.5% | $27.97, −1.17% / $23.15, −5.50% | Yes |
| 10% hurdle price, before / after stock pay | ~$25 / ~$18–19 | $25.33 / $17.99 (full solve); $25.56 / $18.69 (simple discount) | Yes |
| 30/50/20 weighting | ~8%; ~1% with stock pay | $40.96, +8.15%; $30.77, +1.08% | Yes |
| 25/50/25 weighting | $45.50, 11%; ~4% with stock pay | $45.54, +10.9%; $34.71, +4.0% | Yes |
| Base subscribers at 8% margin | −6% | $22.61, −6.0% before stock pay; $11.89, **−19.3%** after 4% stock pay | Number yes; basis missing (F4) |
| Bear "because $2.1B sits ahead" | $2.1B | Gross 1,402.5 + 710 = 2,112.5. But the bear's model net debt is **$846M**. With zero net debt the bear is still $10.04 (−22.4% a year). | **No (F4, M1)** |
| Fully fixed base | $25.60, −3% | $25.63, −3.20%; capped call alone +$0.44 | Yes |
| $400M free cash flow / facility drawn | 4.5% / base +5.5%, bear −32.5% | +4.52% / +5.48%, −32.51% | Yes |
| $6.0B revenue at 14%; 16x multiple | ~10%; ~9.6% | +9.97%; +9.62% | Yes |
| Breakevens | 3.4M or 10.5%; 5.2M or 16% | 3.39M, 10.5%, 5.22M, 16.2% | Yes |
| Eucalyptus subscribers (central) | 0.17–0.26M | Average 88k → 0.175M (begin/end average) or 0.263M (one month in three) | Yes |
| Organic growth (central) | +8% to +12% | **+7.8% to +11.4%** | **Upper bound should be +11% (F9)** |
| Organic growth (rounding range) | +4% to +14% | +4.1% to +13.8% (0.116–0.351M) | Yes |
| Cost per organic net add | $2,000–5,900 | $1,986–6,029 (central range only; negative adds at 0.35M) | Yes |
| Payback | 15; 34–100 months | 14.8; 34; 100 | Yes |
| Injection gross margin | 27% at $349; 38% at $199 | 26.9%; 38.5% | Yes |
| Pill / compounded margin | 45% / 80% | 45.0% / 79.9% | Yes |
| Market cap / EV / EV incl. Eucalyptus | $6.86B / $7.42B / $8.13B | 6,860 / 7,421 / 8,131 | Yes |
| EV / 2026 sales | 2.3x | 2.32x | Yes |
| EV / EBITDA 2026, 2027 | 25x, 18x | 24.7x, 18.2x (27.1x, 20.0x on the $8.13B EV) | Yes (basis, M2) |
| EBITDA after stock pay; EV multiple | $114M; 65x | 114.4; 64.9x | Yes |
| 14x adjusted → after stock pay | 20–24x | 19.6x / 23.9x | Yes |
| Growth: revenue / US / subscribers / international share | 38% / 16% / 19% / 17% | 38.3% / 15.7% / 18.5% / 17.4% | Yes |
| Gross profit growth; Q4 run-rate; base vs run-rate | 16%; $3.8B; ~8% | 16.4%; 3,795; 8.1% | Yes |
| Free cash flow share of EBITDA | ~49% | 1,200 / 2,444 = 49.1% | Yes |

---

## (d) Fix-application problems

| # | Location + exact quote (post-fix) | Problem | Exact replacement |
|---|---|---|---|
| F1 | §1 Verdict: "Our central estimate is about −1% to +6% a year: +6% before stock pay, about −1% with stock pay charged at 4% of revenue, and about −3% with all the reviewer's fixes." | −3% falls outside its own range. The range also disagrees with §7 ("−1% to +5%"). The bank-views row was synced to "−1% to +6%". | "Our central estimate is about −1% a year, with stock pay charged at 4% of revenue. The range is about −3% (all the reviewer's fixes) to +6% (before stock pay)." Also change the bank-views Hims row "central estimate about −1% to +6% a year from about $29.40" → "central estimate about −1% a year (range −3% to +6%) from about $29.40". |
| F2 | §7: "**Net:** a central return is about −1% to +5% a year, below the 6% pre-stock-pay headline." | Contradicts §1 (+5% vs +6%), and the range leaves out −3%. | "**Net:** with stock pay charged, a central return is about −1% a year (range about −3% to +6%), below the 6% pre-stock-pay headline." |
| F3 | §1 point 1: "**It lost its highest-margin product.**" | §2 shows generics at 85–90% gross margin, against about 80% for compounded semaglutide. | "**It lost its most distinctive product.**" |
| F4 | §1 point 3: "Our bear case (3.5 million subscribers, today's 8% margin, a 10x multiple) gives about $7 a share, or about −29% a year, because about $2.1B of convertible debt and deferred acquisition payments sit ahead of shareholders. An 8% margin with base-case subscribers gives about −6% a year." | False cause. The model's bear net debt is $846M: cash offsets the debt and 60% of Eucalyptus is paid in stock. With zero net debt the bear is still about $10 (−22% a year). The main driver is EV falling to $2.8B. Both figures are also before stock pay, unlike the base and plan figures beside them. | "Our bear case (3.5 million subscribers, today's 8% margin, a 10x multiple) gives about $7 a share, or about −29% a year, before stock pay. Most of the fall comes from a $2.8B enterprise value; net debt of about $0.85B takes about $3 a share more. An 8% margin with base-case subscribers gives about −6% a year before stock pay, and about −19% with it." |
| F5 | §4 Lilly: "Hims prescribes; Lilly's pharmacy dispenses and sells the drug, so Hims likely earns only its membership fee on these (fee terms not disclosed). Lilly has said it has no affiliation with Hims." | Lilly's statement is dated 1 Apr 2025 and concerned Hims' earlier Zepbound listing at about $1,899 a month (raw 02 §1). With no date, it reads as a comment on 2026. It also repeats Hims' disclaimer from the sentence before. | "Hims prescribes; LillyDirect dispenses and sells the drug, so Hims likely earns only its membership fee ($39 first month, then $149; single source). Any fee from Lilly is not disclosed. (In April 2025, when Hims first listed Zepbound at about $1,899 a month, Lilly said it had no affiliation with Hims.)" |
| F6 | §4 DEA row: "Matters for any true testosterone (a Schedule III controlled drug); Hims' low-T line launched with enclomiphene, which we believe is not a controlled drug (to check), and branded oral testosterone was only planned; size unknown" | "(to check)" is a work note in published text. "Only planned" goes beyond raw 03 ("launch not confirmed"). Kyzatrex is Schedule III, and Hims has a Kyzatrex drug page. | "Matters for any true testosterone (a Schedule III controlled drug). Hims' low-T line launched in September 2025 with enclomiphene, which is not a controlled drug (background knowledge). Its branded oral testosterone (Kyzatrex, Schedule III) was announced, but launch is not confirmed. Size unknown" |
| F7 | §5: "The makers' channels are large." | After fix #10, the only support left is LillyDirect's 35% from Q2 2025. | "The makers' own channels look large, but the data are thin." |
| F8 | §5: "Novo also runs its own multi-month Wegovy plans from $249 a month, and cuts US list prices by up to 50% from 1 January 2027." | §2 lists these plans as a Hims price option, and raw 04 (f)6 says Hims was listed as "coming soon" on them. A list-price cut is not a cash-price cut. | "Novo also sells its own multi-month Wegovy plans from $249 a month (Hims was listed as "coming soon" on them), and plans to cut US list prices by up to 50% from 1 January 2027 (effect on cash prices not known)." |
| F9 | §3 table: "so organic growth about +8% to +12% (range +4% to +14%)"; §7: "so organic growth was about +8% to +12%, not +19% (estimate)." | The central range recomputes to +7.8% to +11.4%. +12% is rounding drift in the QA. | §3: "so organic growth about +8% to +11% (range +4% to +14%)". §7: "so organic growth was about +8% to +11%, not +19% (estimate)." |
| F10 | §1 point 2: "mostly through acquisitions (Zava in July 2025; Eucalyptus in June 2026, about $40M in the quarter)." | Zava's revenue is in no raw file. This is an inference with no tag. | "mostly through acquisitions (our inference; Zava, bought July 2025, does not disclose revenue; Eucalyptus, June 2026, about $40M in the quarter)." |
| F11 | §7: "Hims says revenue per subscriber would be $90 without Eucalyptus." | Tagged in §3 but not here. | "Hims says revenue per subscriber would be $90 without Eucalyptus (one snippet, unverified)." |

Checked and fine: the glossary (accurate enough at this level); the 503A/503B gloss; the capped-call gloss; the CFO sales; the FDA warning letters; "(8-K)" for Franklin; the bank-ratings rewrite; the EV-multiple inversion fix; $18–19; +15%.

---

## (e) Missed defects (both the QA and the fixes)

| Sev. | Location + exact quote | Problem | Evidence | Exact replacement |
|---|---|---|---|---|
| major | §6: "The bear case is so severe because of leverage. A $2.8B enterprise value leaves little after $1.4B of converts and the Eucalyptus payments." | Wrong cause. Bear equity is $1.95B, 70% of EV. Leverage costs about $3 of the roughly $22 drop. The driver is EBITDA of $280M × 10x = $2.8B EV, against $7.4B today. (The same claim in §1 is F4.) | Model: bear net debt 846; EV 2,800; shares 278.9 (+45.6M); unlevered value $10.04. | "The bear case is severe mainly because EBITDA falls to $280M and the multiple to 10x, so EV drops to $2.8B from about $7.4B today. Net debt of about $0.85B and about 46M more shares take it the rest of the way. In that case the $1B of 2030 notes would need refinancing." |
| minor | §6 table: "\| EV / adjusted EBITDA \| about 25x 2026 (guide midpoint), about 18x 2027 (one consensus source, unverified) \|" | Basis mismatch. The 2026 guide includes Eucalyptus EBITDA, but this EV leaves out the $710M Eucalyptus payments. | Raw 01 §5: 27.1x / 20.0x on $8.13B. | "\| EV / adjusted EBITDA \| about 25x 2026 (guide midpoint) and about 18x 2027 (one consensus source, unverified); about 27x and 20x if the Eucalyptus payments are counted in EV \|" |
| minor | §4 Lilly: "Hims doctors can reportedly prescribe Lilly's Zepbound, Mounjaro and Foundayo" | Hims' own release lists only Zepbound and Foundayo. Mounjaro comes from FierceHealthcare only. | Web check; raw 02 §1 cites both sources. | "Hims doctors can reportedly prescribe Lilly's Zepbound and Foundayo (one report adds Mounjaro)" |
| minor | §6 table: "3.2–3.7 days to cover"; §7: "Gross profit dollars grew 16% in Q2" | QA (d) items 10 and 12 were never applied. 3.2 days traces only to raw 04, and 16% is computed from rounded margins. | Raw 01 §5 (3.7 days); 482.0 / 414.0. | "3.2–3.7 days to cover (3.2 from one source)"; "Gross profit dollars grew about 16% in Q2 (estimate)" |

No other material defect found. Everything else in the post-fix note traces to raw 01–04 or the bank file.

---

## Systematic QA weaknesses

- Replacements were written row by row and not read together. #1 and #2 give different ranges, and the #1 range leaves out its own −3%.
- Replacements were not checked against the note's own tables. "Highest-margin" conflicts with §2.
- The QA fixed numbers but kept the note's causal claims. It never tested how much of the bear case is leverage.
- Web facts came in without dates or reconciliation. The 2025 Lilly statement was used for 2026, and raw 02's 2025 Zepbound entry was ignored.
- Its own recompute has small rounding drift (+11.6% against +11.4%), which produced a new bound.
- Two defects were overstated (#21, #39), where the raw files supported the original wording.
- A background-knowledge point was handed on with "(to check)" in place of a resolved, tagged statement.

*Sources for web checks: [Hims 8-K, 7 Oct 2026](https://www.sec.gov/Archives/edgar/data/0001773751/000177375126000220/hims-20261007.htm); [Lilly statement (1 Apr 2025)](https://investor.lilly.com/news-releases/news-release-details/statement-lilly-has-no-affiliation-hims-hers); [Sherwood on Lilly statement](https://sherwood.news/business/eli-lilly-says-it-has-no-affiliation-with-hims-and-hers-after-market); [Hims newsroom: FDA-approved GLP-1s](https://news.hims.com/newsroom/full-range-of-fda-approved-glp-1s-available-on-hims-hers); [FierceHealthcare](https://www.fiercehealthcare.com/telehealth/telehealth-provider-him-hers-adds-all-fda-approved-glp-1s-platform); [Marius–Hims Kyzatrex (CIII)](https://www.biospace.com/press-releases/marius-pharmaceuticals-and-hims-hers-collaborate-to-expand-access-to-kyzatrex-testosterone-undecanoate-ciii-capsules-the-first-fda-approved-oral-testosterone-therapy-offered-on-the-hims-hers-platform); [Hims Kyzatrex page](https://www.hims.com/drugs/info/kyzatrex); [enclomiphene bulk listing](https://hellopharmacist.com/ndc/73377-0320-02). QA only. Not investment advice.*
