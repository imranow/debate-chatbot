# QA review: Hims & Hers note (7 Oct 2026)

*Stream 05. Target: `hims-hers-analysis.md` at HEAD (commit 6c41ade, "Apply devil's-advocate review"). The working copy matched HEAD throughout. Sources checked: raw 01–04, `01-valuation_model.py`, the GLP-1 pen note (2026-09-22) and the bank-views raw file 02. I ran the model with `python3 -I` and rebuilt every derived figure in scratch scripts (`scratchpad/qa_check.py`, `qa_check2.py`). I made 3 web searches to settle conflicts between raw files. Every quote in table (b) was string-matched against the note: each appears exactly once. In rows #19, #28 and #39, "\|" is only a markdown escape. The note has a plain "|" there.*

---

## (a) Verdict

**PASS WITH FIXES.**

- The model reproduces exactly. Almost every number traces to a raw file. Most caveats survived the revision.
- But the revision added errors in the headline and in section 7:
  - The "0–6%" central range does not match the note's own stock-pay figure (−1%) or the reviewer's range (0–5%).
  - The organic-subscriber range is internally inconsistent.
  - The 30/50/20 weights are regulatory odds presented as "our" valuation odds.
  - The −3% "all fixes" figure is described with the wrong set of fixes.
  - The 39% Wegovy self-pay share is misread as a drug-maker channel share.
  - "A repeat of 8% margin gives large losses" overstates what an 8% margin alone does.
- None of these changes the call ("not cheap enough for the risks"). All are fixable with text edits. No critical defect found.

---

## (b) Defect table

| # | Sev. | Location + exact quote | Problem | Evidence | Exact replacement text |
|---|---|---|---|---|---|
| 1 | major | §1 verdict: "Our honest central estimate is about 0–6% a year, depending on whether stock pay is treated as a cost." | With stock pay charged, the note's own base is −1% (§1 point 3, §7), not 0%. The reviewer's fully fixed base is −3%. Raw 04 said "0–5%". "Honest" implies the other figures are not. | Model: base at 4% stock pay = $27.97, −1.2%. Raw 04 (a): "about 0–5% a year". | "Our central estimate is about −1% to +6% a year: +6% before stock pay, about −1% with stock pay charged at 4% of revenue, and about −3% with all the reviewer's fixes." |
| 2 | major | §7: "**Net:** an honest central return is about 0–6% a year, below the 6% headline." | Self-contradictory: a range topping out at 6% is not "below" 6%. Misquotes raw 04 ("0–5%"). Same issue as #1. | Raw 04 (a), last bullet. | "**Net:** a central return is about −1% to +5% a year, below the 6% pre-stock-pay headline." |
| 3 | major | §1 point 3: "A repeat of today's 8% margin gives large losses, because about $2.1B of convertible debt and deferred acquisition payments sit ahead of shareholders." | At 8% margin with base subscribers and multiple, the return is about −6% a year ($22.6), not "large losses". The −29% bear also assumes 3.5M subs, $1,000 per sub and 10x. | Model grid row 4.5M, 8% column: −6.0%. Bear inputs in raw 01 §6. | "Our bear case (3.5 million subscribers, today's 8% margin, a 10x multiple) gives about $7 a share, or about −29% a year, because about $2.1B of convertible debt and deferred acquisition payments sit ahead of shareholders. An 8% margin with base-case subscribers gives about −6% a year." |
| 4 | major | §1 point 2: "But US revenue grew only 16%. Much of the rest came from buying Eucalyptus in Australia." | Eucalyptus (~$40M) is about 19% of the $208M revenue growth and about a third of the $124M international growth. The rest of international growth (about $84M) is not Eucalyptus. | Raw 01 §1.1: US +$84.5M, international +$123.9M, Eucalyptus ~$40M. | "But US revenue grew only 16%. The rest came from international, which rose from $7.5M to $131.4M, mostly through acquisitions (Zava in July 2025; Eucalyptus in June 2026, about $40M in the quarter)." |
| 5 | major | §3 table: "Eucalyptus about 0.12–0.35M, so organic growth about +8% to +11%)" | The range and the growth figure don't match. 0.12–0.35M gives organic growth of +4% to +14%. +8% to +11% matches only the central values, 0.17–0.26M. At 0.35M, organic net adds in Q2 would be negative. | Recomputed: Eucalyptus average subs 58–117k (rounding range), point estimate 88k → end count 0.175M (half-quarter basis) or 0.26M (one-month-in-three basis). Organic end 2.63–2.72M = +7.9% to +11.6% vs 2.439M. | "Eucalyptus about 0.17–0.26M (rounding range 0.12–0.35M), so organic growth about +8% to +12% (range +4% to +14%))" |
| 6 | major | §7: "That implies Eucalyptus brought in roughly 0.12–0.35M subscribers, so organic growth was about +8% to +11%, not +19% (estimate)." | Same mismatch as #5. | As #5. | "That implies Eucalyptus brought in roughly 0.17–0.26M subscribers (0.12–0.35M allowing for rounding), so organic growth was about +8% to +12%, not +19% (estimate)." |
| 7 | major | §1 verdict: "The case is skewed upward: weighting our bear, base and bull cases 30/50/20 gives about 8% a year, or about 1% with stock pay charged as a cost." | The 30/50/20 weights are raw 02's odds for *regulatory* scenarios over 12–24 months. They are not probabilities for the valuation cases. The note calls them "our" weights. The arithmetic is right (8.2% / 1.1%). | Raw 02 (b); raw 04 (a) "the regulatory stream's own 30/50/20 odds". | "The case is skewed upward: if the regulatory stream's odds (30/50/20) are borrowed as weights for our bear, base and bull cases, the result is about 8% a year, or about 1% with stock pay charged as a cost." |
| 8 | minor | §7: "Weighting 30/50/20 gives about 8%." | Same attribution gap as #7. | Raw 04 B3. | "Weighting by the regulatory stream's 30/50/20 odds gives about 8%." |
| 9 | major | §7: "- With all of these fixes applied together, the reviewer's base is about $25.60, or about −3% a year." | Not "all of these". The $25.63 case uses 4% stock pay, $800M cash flow (not $400M), the 2032 capped call, Eucalyptus stock at $31 and +10M award shares. It excludes the receivables facility and any change to subscribers. | Raw 04 (d) "Fully fixed base". Reproduced: $25.63, −3.2%. | "- The reviewer's fully fixed base (4% stock pay, $800M of cash flow, the 2032 capped call, Eucalyptus stock at $31 and 10M extra award shares) is about $25.60, or about −3% a year." |
| 10 | major | §5: "About 39% of US injectable Wegovy prescriptions were self-pay in mid-July 2026." | It is offered as proof that "the makers' channels are large". But the 39% self-pay share covers retail and NovoCare, *including telehealth*, so it includes Hims' own volume. | Raw 03 §2.8: "self-pay channel (retail and NovoCare, including telehealth)". | "About 39% of US injectable Wegovy prescriptions were self-pay in mid-July 2026; that figure includes telehealth sellers such as Hims, so it measures cash-pay demand, not Novo's own channel." |
| 11 | minor | §6: "After stock pay, 2026 EBITDA would be only about $114M (estimate), about 65 times EV." | The ratio is inverted. EV is about 65 times EBITDA, not the reverse. | 7,421 / 114.4 = 64.9. | "After stock pay, 2026 EBITDA would be only about $114M (estimate); EV is about 65 times that." |
| 12 | minor | §6: "JPMorgan arranged Hims' $400M working-capital facility and Goldman is a lender, so neither has an independent rating found here." | False cause. The bank file says only that no rating was found. It does not say lending is the reason. | Bank-views raw 02 table B: "nf" for GS and JPM. | "No JPMorgan or Goldman rating was found. Both have a lending tie: JPMorgan arranged Hims' $400M working-capital facility and Goldman is a lender." |
| 13 | minor | §6: "Bank of America is Neutral with a target of about $36–37 (around July). Morgan Stanley is Equal Weight at $28 (11 August). Canaccord is Buy at $40." | Staleness. BofA's $36 dates from about 1 Jul and $37 is undated but before Q2. Canaccord is "~mid-2026", undated. The latest entry in the bank file is Stifel (11 Sep), which the note omits. | Bank-views raw 02, rows for HIMS; (c) "order is not clear". | "Bank of America is Neutral with a target of about $36–37 (set around July, before Q2 results; dated). Morgan Stanley is Equal Weight at $28 (11 August). Canaccord is Buy at $40 (undated, about mid-2026)." |
| 14 | minor | §7: "the downside is capped at about −$29 a share and the upside is about +$69." | The bear case loses about $22 a share ($7.01 vs $29.40). −$29 is the most you can lose at any value (a price of zero), not the bear case. | 7.01 − 29.40 = −22.39; 98.62 − 29.40 = +69.22. | "the bear case loses about $22 a share (and no more than $29.40 can be lost), while the bull case gains about $69." |
| 15 | minor | §6: "In the base case, today's price is fair (0% a year)" | "Fair" sounds like a valuation verdict. A 0% return is a breakeven. | Raw 01 §6 "What the model says". | "In the base case, today's price breaks even (0% a year)" |
| 16 | minor | §1 verdict: "or about $19 after it." | The $25 hurdle comes from a full solve (Eucalyptus shares move with the price): $25.33. The same method gives $17.99 with stock pay, not $19. A simple discount gives $18.69. | Scratch solve. | "or about $18–19 after it." |
| 17 | minor | §3: "At $92 a month and a 64% gross margin, $874 pays back in about 15 months." | Gives payback only for the flattering figure. The note's own organic cost of $2,000–5,900 per add pays back in about 34–100 months. | 874 / 58.9 = 14.8; 2,000 / 58.9 = 34; 5,900 / 58.9 = 100. | "At $92 a month and a 64% gross margin, $874 pays back in about 15 months; at $2,000–5,900 per organic add, payback is about 34–100 months (estimate)." |
| 18 | minor | §3: "One secondary source says 24% (unverified)." | Misquote. The 24% is the GLP-1 share of Q4 2025 revenue, not of 2025 revenue. | Raw 01 §2: "41% of revenue in Q4 2024 to 24% in Q4 2025". | "One secondary source says GLP-1s were 24% of Q4 2025 revenue (unverified)." |
| 19 | minor | §2 table: "$199 (first two fills, to end-2026) to $349 drug, or $249–329 on Novo's multi-month plans, + $149 membership \| about 27% (estimate;" | The 27% was computed at $349 only. At $199 it is about 38%; at $249 about 34%. | Raw 01 §3.5: (498 − 364) / 498. | "$199 (first two fills, to end-2026) to $349 drug, or $249–329 on Novo's multi-month plans, + $149 membership \| about 27% at $349, about 38% at $199 (estimate;" |
| 20 | minor | §6: "The 10-K said about 60% can be paid in stock" | The raw files conflict on the source. Raw 01 ties "~60%" to the deal terms / 8-K. Raw 04 says the 10-K. | Raw 01 (b): "8-K vs 10-Q wording"; raw 04 (f)4. | "Deal terms (Feb 2026) said about 60% can be paid in stock" |
| 21 | minor | §4: "saying Hims was selling mass copies "under the false guise of personalization"" | Novo's statement is an allegation (raw 02 tags it). The narrator voice ("Hims was selling mass copies") states it as fact. | Raw 02 §1 and §2.6: "(allegation)". | "alleging "mass sales of compounded drugs under the false guise of personalization" (Novo's allegation; no court ruled on it)" |
| 22 | minor | §4: "One stream could not confirm Hims sells Zepbound, so treat this as reported, not confirmed." | Mis-resolves the conflict. The streams agree once "prescribe" and "sell" are kept apart. Hims prescribes; LillyDirect dispenses and sells the drug. Web check: a third-party guide dates the change to 23 Apr 2026; Lilly said in 2025 it has "no affiliation" with Hims. | Raw 02 §1 and §3.2; raw 01 §2; raw 03 (c). Web: Lilly statement; Fierce; TheRxIndex. | "Hims prescribes; Lilly's pharmacy dispenses and sells the drug, so Hims likely earns only its membership fee on these (fee terms not disclosed). Lilly has said it has no affiliation with Hims." |
| 23 | minor | §4 table: "Matters for testosterone (a Schedule III drug); size of that business unknown" | Hims' low-T launch was enclomiphene (raw 03 §2.11). As far as I know, enclomiphene is not a controlled drug. Branded oral testosterone was only planned. The DEA exposure may be smaller than implied. | Raw 03 §2.11, §3; raw 02 §4.5. Scheduling of enclomiphene is background knowledge; check it. | "Matters for any true testosterone (a Schedule III drug); Hims' low-T line launched with enclomiphene, and branded oral testosterone was only planned; size unknown" |
| 24 | minor | §1 point 2: "About $280M of that is seven months of Eucalyptus, which the May guide excluded. The profit guide midpoint fell by $12.5M. So the organic guide barely moved, and Eucalyptus adds roughly no 2026 profit." | $280M scales one month (~$40M) to seven. "Adds roughly no profit" is an inference: the guide does not split Eucalyptus EBITDA. Neither is tagged. | Raw 01 §2 (Eucalyptus run-rate "estimate"); raw 04 R5. | "About $280M of that is seven months of Eucalyptus at its June rate (estimate), which the May guide excluded. The profit guide midpoint fell by $12.5M. So the organic guide barely moved, and Eucalyptus appears to add roughly no 2026 profit (our inference)." |
| 25 | minor | §3 table: "Our estimate from Hims' $90 ex-Eucalyptus revenue per subscriber" | The $90 figure comes from one 10-Q snippet via raw 04 and is not tagged. | Raw 04 (f)4 [10-Q; beancount.io]. | "Our estimate from Hims' $90 ex-Eucalyptus revenue per subscriber (one snippet, unverified)" |
| 26 | minor | §7: "The Q3 guide implies about $96–99 a month per subscriber, above the base case's $96." | Our own estimate, not tagged. It depends on assumed Q3 subscribers (a range of $95–102 for 2.95–3.10M). | Recomputed. | "The Q3 guide implies about $96–99 a month per subscriber (estimate), above the base case's $96." |
| 27 | minor | §7: "But 14x adjusted EBITDA is already about 24x EBITDA after stock pay." | Uses stock pay at 5.8%. At the 4% used elsewhere in the note it is about 20x. | 14 × 14 / 8.2 = 23.9; 14 × 14 / 10 = 19.6. | "But 14x adjusted EBITDA is already about 20–24x EBITDA after stock pay (at 4–5.8% of revenue)." |
| 28 | minor | §6 table: "\| EV / adjusted EBITDA \| about 25x 2026, about 18x 2027 \|" | 2027 uses a single-source consensus ($407M, StocksGuide). | Raw 01 §5. | "\| EV / adjusted EBITDA \| about 25x 2026 (guide midpoint), about 18x 2027 (one consensus source, unverified) \|" |
| 29 | minor | §3: "The latest disclosed personalised share is 65% of subscribers, about 1.6M people, in Q4 2025." | Single source (raw 03 [S3]). Raw 01 could not find it. Web check: the company figure is "over 1.6M"; 65% is a third-party calculation (about 64% of 2.511M). | Raw 01 §3.4 vs raw 03 §1.4. Web: Fintool / 247wallst summaries. | "The latest disclosed figure is over 1.6M subscribers on personalised treatments in Q4 2025, about two-thirds of subscribers (one source)." |
| 30 | minor | §1 point 1: "It now sells Novo's branded drugs at Novo's own cash prices and keeps only a service fee." | "Keeps only a service fee" is raw 02's own reading. Fee terms and gross/net booking are undisclosed (§10 says so). | Raw 02 §3.2, §3.4 ("my read"). | "It now sells Novo's branded drugs at Novo's own cash prices and, on our reading, keeps mainly a service fee (terms not disclosed)." |
| 31 | minor | §1 point 3: "Our base case is 4.5 million subscribers and a 14% profit margin in 2030, against 2.89 million and 8% today." | "Profit margin" reads as net margin (net income was negative in Q2). It is the adjusted EBITDA margin. | Raw 01 §6. | "Our base case is 4.5 million subscribers and a 14% adjusted EBITDA margin (profit before interest, tax, depreciation and stock pay) in 2030, against 2.89 million and 8% today." |
| 32 | minor | §1 point 3: "Management's own 2030 plan ($6.5B of revenue at a 20% margin) gives about 21% a year." | The base and verdict are shown both before and after stock pay; this figure is not. | Model with 4% stock pay: $53.82, +15.4% (matches raw 04 R1). | "Management's own 2030 plan ($6.5B of revenue at a 20% margin) gives about 21% a year, or about 15% with stock pay charged." |
| 33 | minor | §1 point 1: "**It lost its best product.**" | Missing balancing fact. The CEO said in Feb 2026 that "only a small minority of our subscribers use compounded GLP-1s". | Raw 01 §2 [S27]. | "**It lost its highest-margin product.**" and add after the first sentence of point 1: "The CEO said in February 2026 that only a small minority of subscribers used compounded GLP-1s." |
| 34 | minor | §5: "About 35% of new Zepbound prescriptions went through LillyDirect in Q2 2025." | Stale (more than a year old) but used as current evidence. | Raw 03 §2.8. | "About 35% of new Zepbound prescriptions went through LillyDirect in Q2 2025 (latest found; over a year old)." |
| 35 | minor | §5: "**What has not:** the compounded strategy, which ended two Novo relationships and drew an FDA rebuke." | Understates the FDA record. Material facts left out: an FDA warning letter to Hims (9 Sep 2025) and one to its 503B facility (Dec 2025). | Raw 02 §1, §4.1. | "**What has not:** the compounded strategy, which ended two Novo relationships and drew an FDA rebuke, plus FDA warning letters to Hims (September 2025) and to its 503B facility (December 2025)." |
| 36 | minor | §5: "He sold heavily in 2025 under a pre-set trading plan. No open-market sale by him was found in 2026." | Leaves out 2026 insider sales by the CFO under a 10b5-1 plan (19 Aug and 1 Oct 2026). | Raw 01 §4.3; raw 03 §5.3. | "He sold heavily in 2025 under a pre-set trading plan. No open-market sale by him was found in 2026; the CFO sold small amounts under a pre-set plan in August and October 2026." |
| 37 | minor | §6: "A capped call offsets dilution up to $50.15." | Jargon not explained. | — | "A capped call (a hedge Hims bought that pays out in shares if the stock rises) offsets dilution up to $50.15." |
| 38 | minor | §4 table: "Hims says it uses only traditional 503A pharmacies for GLP-1s" | 503A and 503B are not explained. | Raw 02 §2.2–2.3. | "Hims says it uses only traditional 503A pharmacies (state-licensed, compounding per patient prescription; 503B 'outsourcing facilities' make large batches under FDA rules) for GLP-1s" |
| 39 | minor | §5 table: "\| Personalisation and data \| C \| The compounded "personalised" combos are what regulators attacked \|" | "Regulators attacked" is broader than the record. FDA's letter targeted the "same active ingredient" claim, and "personalization" was Novo's allegation; no court ruled. | Raw 02 §2.6. | "\| Personalisation and data \| C \| The compounded "personalised" combos drew FDA criticism and Novo's allegations; no court ruled \|" |

**Readability: other jargon not explained on first use.** GLP-1 (first used in the header line), convertible notes / "converts", 0% coupon, 10-Q / 10-K, earn-out, fair value, pass-through and gross booking, "uncommitted, 364-day" facility, days to cover / borrow fee / squeeze, exit multiple, net debt, diluted shares, Class V, consent order, lead-plaintiff deadline, Schedule III. ROSCA does not appear in the note. EV and EBITDA are defined on first use (§6 and §3 tables). Suggest a five-line glossary under the header.

**Settled conflicts (web checks).**
- **CAO successor.** Raw 03 said the CFO would cover in the interim. Raw 04 said Jon Franklin was named. A Hims 8-K dated 7 Oct 2026 confirms Franklin becomes principal accounting officer from 9 Oct 2026. The note is right. Cite the 8-K. ([SEC 8-K](https://www.sec.gov/Archives/edgar/data/0001773751/000177375126000220/hims-20261007.htm))
- **Zepbound.** Hims providers send prescriptions to LillyDirect at Lilly's self-pay prices (a third-party guide gives 23 Apr 2026). Hims does not dispense or sell the drug. Lilly said in 2025 it has no affiliation with Hims. See #22. ([Lilly statement](https://investor.lilly.com/news-releases/news-release-details/statement-lilly-has-no-affiliation-hims-hers); [FierceHealthcare](https://www.fiercehealthcare.com/digital-health/dtc-obesity-med-market-heats-eli-lilly-taps-knownwell-hims-hers-adds-new-weight-loss); [TheRxIndex](https://therxindex.com/guides/does-hims-offer-tirzepatide/))
- **Personalised share.** The company figure is "over 1.6M". 65% is a third-party calculation. See #29. ([Fintool Q4 2025](https://fintool.com/app/research/companies/HIMS/earnings/Q4%202025); [247wallst](https://247wallst.com/companies/hims/earnings/2025/Q4))
- **Eucalyptus price and stock share.** Not searched. The note handles this correctly: $710M nominal / $683.9M fair value, "about 60%" vs "a significant majority". Only the source attribution needs fixing (#20). The upfront payment ($225M vs $240M) does not appear in the note.

**Traceability: items with no raw source.** None found apart from those above. Every other number traces to raw 01–04 or the bank file. The 3.2-day short-interest figure traces only to raw 04. Raw 01 has 3.7 days.

**Staleness.** Dated but presented as current: BofA and Canaccord targets (#13); LillyDirect 35% from Q2 2025 (#34); short interest from late July (already labelled). Personalised share (Q4 2025) and the weight-loss share (Feb 2025 guide) are labelled with their dates. Everything else is August 2026 or later.

**Balance.** The verdict is fair given the evidence. Two facts in raw 04 are missing from the bear side: Novo's US list-price cut of up to 50% from 1 Jan 2027, and Novo's own multi-month plans undercutting Hims' membership. Consider one line in §5. Wording that leans toward advice: "pay well" and "today's price is fair" (#15). The "$25 / $19" hurdle prices are flagged as "not price targets", which is adequate.

---

## (c) Arithmetic and model table

Model run: `python3 -I raw/01-valuation_model.py` reproduces raw 01 and the note exactly. "Note" = what the note says; "Recomputed" = my result.

| Item | Note | Recomputed | OK? |
|---|---|---|---|
| Q2 revenue growth | +38% | 753.2 / 544.8 = +38.3% | Yes |
| US growth | +16% | 621.8 / 537.3 = +15.7% | Yes |
| International share | ~17% | 131.4 / 753.2 = 17.4% | Yes |
| Subscriber growth | +19% | 2,891 / 2,439 = +18.5% | Yes |
| Marketing / revenue | 34.8% / 40.0% / 39.2% | 34.8% / 40.0% / 39.2% | Yes |
| Adj. EBITDA margins | 8.0% / 15.1% / 13.5% | 8.0% / 15.1% / 13.5% | Yes |
| 2026 guide growth, margin | 36%, 9.4% | 36.3%, 9.375% | Yes |
| 2030 growth needed | 19% / 44% | 19.4% / 44.3% | Yes |
| Guide raise / Eucalyptus / EBITDA change | +$300M / ~$280M / −$12.5M | 3.2 − 2.9 = 0.3B; 40 × 7 = 280; 300 − 312.5 | Yes (280 is an estimate, #24) |
| Cost per net add | $874 | 262.2 / 0.300 = 874 | Yes |
| Payback | ~15 months | 874 / (92 × 0.64) = 14.8 | Yes (organic: 34–100 months, #17) |
| Per organic add | $2,000–5,900 | 262.2 / 0.132 to / 0.044 = 1,986–5,959 | Yes |
| Eucalyptus subs / organic growth | 0.12–0.35M / +8% to +11% | 0.17–0.26M central → +7.9% to +11.6%; 0.12–0.35M → +4.2% to +13.6% | **No (#5, #6)** |
| Gross margin compounded / injection / pill | 80% / 27% / 45% | 79.9% / 26.9% (at $349) / 45.0% | Yes (injection only at $349, #19) |
| Market cap / EV / EV incl. Eucalyptus | $6.86B / $7.42B / $8.13B | 6,860 / 7,421 / 8,131 | Yes |
| EV / 2026 sales | 2.3x | 2.32x | Yes |
| EV / EBITDA 2026, 2027 | 25x, 18x | 24.7x, 18.2x | Yes |
| EBITDA after stock pay; EV multiple | $114M; "65 times" | 300 − 0.058 × 3,200 = 114.4; 7,421 / 114.4 = 64.9 | Number yes; wording inverted (#11) |
| Convert dilution | 27.8M, 11.9% | 14.15 + 13.63 = 27.78M; 11.9% | Yes |
| Eucalyptus stock shares | up to 18.6M | 0.6 × 910 / 29.40 = 18.57M | Yes |
| Debt + deferred | ~$2.1B | 1,402.5 + 710 = 2,112.5 | Yes |
| CEO votes | 87–88% | Class V only 86.8%; plus 15.39M Class A 87.7% | Yes |
| Bear / base / bull / management plan | $7, −29% / $38, +6% / $99, +33% / $67, +21% | $7.01, −28.8% / $38.26, +6.4% / $98.62, +33.1% / $66.64, +21.3% | Yes |
| Breakevens | 3.4M subs or 10.5% for 0%; 5.2M or 16% for 10% | 3.39M, 10.5%, 5.22M, 16.2% | Yes |
| Margin sensitivity | 4–7 points per 3 points | 7.0 / 5.4 / 4.7 / 4.1 | Yes |
| Stock pay 4% / 5.8% | $28, −1% / $23, −5.5% | $27.97, −1.2% / $23.15, −5.5% | Yes |
| Management plan with 4% stock pay | not stated | $53.82, +15.4% | Missing (#32) |
| 10% hurdle price, before / after stock pay | ~$25 / ~$19 | $25.33 / $17.99 (simple discount: $25.56 / $18.69) | $19 slightly high (#16) |
| 25/50/25 weighting | $45.50, 11% | $45.54, +10.9% | Yes |
| 30/50/20 weighting | ~8% | $40.96, +8.2% | Yes (weights mis-attributed, #7) |
| Weighted with 4% stock pay | ~4% and ~1% | +4.0% / +1.1% | Yes |
| Free cash flow share of EBITDA | ~49%, "about half" | 1,200 / 2,444 = 49.1% | Yes |
| FCF $400M | ~4.5% | $35.44, +4.5% | Yes |
| $400M facility drawn | base +5.5%, bear −32.5% | $36.85, +5.5%; $5.57, −32.5% | Yes |
| Fully fixed base | $25.60, −3% | $25.63, −3.2% | Number yes; description wrong (#9) |
| Q4 run-rate; base vs run-rate | $3.8B; ~8% a year | 949 × 4 = 3,795; (5,175 / 3,795)^(1/4) = +8.1% | Yes |
| $6.0B revenue at 14% | ~10% | $43.95, +10.0% | Yes |
| 16x multiple | ~9.6% | $43.36, +9.6% | Yes |
| Gross profit growth | +16% | 482.0 / 414.0 = +16.4% | Yes |
| 14x adjusted = 24x after stock pay | 24x | 23.9x at 5.8%; 19.6x at 4% | Basis unstated (#27) |
| Bear downside / bull upside | −$29 / +$69 | −$22.39 / +$69.22 | Downside wrong framing (#14) |
| 8% margin with base other inputs | "large losses" | $22.61, −6.0% | **No (#3)** |
| Eucalyptus share of revenue growth | "much of the rest" | 40 / 208.4 = 19% of total; 32% of non-US growth | **No (#4)** |

---

## (d) Claims needing an "(unverified)" or "(estimate)" tag

1. "About $280M of that is seven months of Eucalyptus" → (estimate). See #24.
2. "Eucalyptus adds roughly no 2026 profit" → (our inference). See #24.
3. "Hims' $90 ex-Eucalyptus revenue per subscriber" → (one snippet, unverified). See #25.
4. "The Q3 guide implies about $96–99 a month per subscriber" → (estimate). See #26.
5. "about 18x 2027" EV/EBITDA → (one consensus source, unverified). See #28.
6. "65% of subscribers, about 1.6M people, in Q4 2025" → (one source; 65% is a calculation). See #29.
7. "keeps only a service fee" → (our reading; terms not disclosed). See #30.
8. "Jon Franklin (ex-Rivian) was named successor on 7 October" → the 8-K confirms it; cite the 8-K instead of tagging.
9. "Since late April 2026, Hims doctors can reportedly prescribe Lilly's Zepbound…" → already hedged; add that the date comes from one third-party guide.
10. "3.2–3.7 days to cover" → 3.2 days traces only to raw 04 (unverified).
11. "He sold heavily in 2025" → the dollar sizes in raw 01 are unverified. The wording is acceptable without figures.
12. "Gross profit dollars grew 16% in Q2" → (estimate; from rounded margins).
13. "Visa ... must cut disputes" → the 1.5% threshold is from one report (raw 03). The note does not cite the threshold, so no tag needed unless it is added.
14. Section 2 "Illustrative" prices: the Wegovy pen $199/$349 and the multi-month $249–329 come from third-party guides and raw 04 web snippets → mark (unverified, third-party price guides).

*QA only. Not investment advice.*
