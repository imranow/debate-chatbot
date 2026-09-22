# Meta-QA review: robotics QA report (2026-09-22)

No repo files were edited. My scratch scripts are `mq_recompute.py` and `mq_tablecheck.py` in the scratchpad. Both model versions reproduce their committed output files byte for byte. I used 4 web searches.

## Verdicts

- **QA report: RELIABLE WITH CORRECTIONS.** All 45 defects exist in the pre-fix files. Every model number the QA claims recomputes, to 0.1 pt. The problems are in some fixes, not in the findings:
  - The Lynas input it chose (A$16.5B) is off by about 5%.
  - Fix 14 on MP's profit history is factually wrong.
  - Its Hesai "likely stale" call leans the wrong way.
  - It told the author to put "QA web check (verify)" and "reviewer knowledge" into client text.
  - Several process/traceability items are over-rated as major.
- **Post-fix package fit to release: YES WITH FIXES.** Every number in projection §1-7 and moat-map §6/§9 matches `model_post.py`. The model-output file matches the script. §5's verdict column matches §9. Five things must change before release:
  1. The MP profit sentence.
  2. Re-base Lynas to about A$15.6B, which gives -14% and 41x.
  3. Remove the internal QA/"verify" wording.
  4. Correct the Hesai-cap caveat.
  5. Quantify how conservative the Hesai base is.

## (a) Rulings on the 45 QA defects

| # | Ruling | Reason | Corrected fix (if any) |
|---|---|---|---|
| 1 | CONFIRMED (fix PARTLY) | Web check: stockanalysis gives US$10.9B, a US$10.87 price and 1.0065B shares. A$15.54 × 0.70 = US$10.88, so the source implies AUD/USD of about 0.70, not the script's 0.66. | Use A$15,640M (1.0065B × A$15.54, from raw/02 plus the web share count). That gives -14% base, 41x, "never below 20M". A$16.5B applies the model's FX to a USD quote and overstates the cap by 5.5%. It also breaks the note's "lower figure" rule, since A$14.07B was also found. |
| 2 | CONFIRMED | Text is identical to v1 (11061f3 line 117). Recompute: -10.6% / -2.4%. | – |
| 3 | CONFIRMED | Pre §6 put "Avoid" names in 2-3% Core and 1-1.5% sleeves. | – |
| 4 | CONFIRMED | Breakeven is 3.26M. The v1 text is in 11061f3 line 129. | – |
| 5 | CONFIRMED | Contradicts M §9. | – |
| 6 | CONFIRMED | CNY 1.41B robot revenue on CNY 17.7B, 34.4x, bull -7.2%. raw/01 has 2.6M + 0.8M = 3.4M. | – |
| 7 | CONFIRMED | 43.4x. $180 vs $800-1,500 is 78-88% below. | The fix drops the fact that LGES (72x) is also higher. Post-fix, Lynas (44x) is higher too. |
| 8 | CONFIRMED | CNY 2.52B. Value/cap is 0.386, or 0.269 at a 14% robot margin. | – |
| 9 | CONFIRMED | 375k units × $160 = $60M. P/E 57.3x / 56.3x. | Fix 39 then moved it to $88M and 55x, which the post-fix text reflects. |
| 10 | CONFIRMED | Sanhua breaks even at 16.9M. | – |
| 11 | CONFIRMED | Bull robot shares: Sanhua 11.8%, Nabtesco 9.1%, Allegro 5.3%. | – |
| 12 | CONFIRMED | Deltas: +10.8 / +9.45 / +7.17 / +2.80. Others ≤1.62. | – |
| 13 | CONFIRMED | US$990M ÷ 0.66 = A$1.5B. No HRE-share source in raw/02. | – |
| 14 | PARTLY (fix WRONG) | "Profitable for the first time" is false. But MP also earned $24.3M in FY2023 (MP Q4/FY2023 release, via web). "Last earned a profit in 2022" is wrong, and "reviewer knowledge" is not client-safe. | "...returns to profit (it last reported a full-year net profit in 2023)." |
| 15 | CONFIRMED | 200k × 3.5 kg = 700 t. Small misread: raw/02 says 10X brings total US capacity to about 10,000 tpa, not 10X alone. | – |
| 16 | CONFIRMED | Bear case is 300k total, below MS's China-only 446k (raw/07). | – |
| 17 | CONFIRMED | raw/06 gives only the 890k total. | Severity should be minor. |
| 18 | CONFIRMED | No pool used "embodied". | Minor, not major: it has no numeric effect. |
| 19 | PARTLY | The traceability gap is real. The 1.5x-cap case gives -9.0%. But the conflicting ~$21B figure looks like an artefact of Hesai's 8-for-1 split (ADS ratio 1→8, 10 Jul 2026, ADS count unchanged; Nasdaq ECA2026-479). Morningstar showed $2.97B on 4 Sep 2026. | "Undated in our sources; a 4 Sep 2026 quote of $2.97B is consistent. Sites showing about $21B appear to apply the July 2026 8-for-1 split to an unchanged ADS count. Re-check before use." |
| 20 | CONFIRMED | Immateriality verified: Nvidia moves ≤0.03 pt, LG Innotek ≤0.17 pt. | – |
| 21 | CONFIRMED | Trailing P/E from the model inputs: Tuopu 36x, Sanhua 49x, Keli 55-59x. | – |
| 22 | CONFIRMED | The field is unused. Schaeffler's TTM is a loss. | Severity should be minor. The -444 value is USD placed in a EUR field; it should be about -404. |
| 23 | CONFIRMED | raw/01 Ewellix: an order book assuming ≥1M units a year. | – |
| 24 | CONFIRMED | raw/01: Laifual CNY 573 (2025), Bernstein CNY 1,100 (2024). raw/03: CNY 32k (2022). | – |
| 25 | CONFIRMED | The midpoint is 20.6. | raw/07 also has CNY 18.30B (Sep 2025), so the true lower figure is 18.3B, not 18.8B. |
| 26 | CONFIRMED | Disclosure gap. | Severity should be minor. |
| 27 | CONFIRMED | raw/08 line 8 wrote "frozen". The QA's web check says "slow". | – |
| 28 | CONFIRMED | – | Only applied to §5. The M §3 table still says "$50B". |
| 29 | CONFIRMED | 2.6x-8.9x. | – |
| 30 | CONFIRMED | -39.8% / -31.9%. | – |
| 31 | CONFIRMED | For 20-30x names: +2.95 to +5.3 pts. | – |
| 32 | CONFIRMED | raw/07: BofA 10M by 2035. | – |
| 33 | CONFIRMED | – | – |
| 34 | CONFIRMED | $1,022M revenue, 2.9% humanoid share. | The fix adds a new unsourced "perhaps 10%". |
| 35 | CONFIRMED | – | – |
| 36 | CONFIRMED | – | – |
| 37 | CONFIRMED | – | – |
| 38 | CONFIRMED | – | Also: raw/02 plus the web imply AUD ≈ 0.70, not 0.66. |
| 39 | CONFIRMED | – | Its effect is larger than "minor": Huachen's breakeven goes from 14.4M to 9.8M and its robot share from 7% to 10%. |
| 40 | CONFIRMED | – | – |
| 41 | CONFIRMED | raw/02: ASSB, Longquan II. | – |
| 42 | CONFIRMED | raw/02: "as of March 2026". | – |
| 43 | PARTLY | Web-only claims. The fix pushed unverified sanctions-list claims into client text with "(verify)". | Cite the DoD 1260H list (8 Jun 2026) directly, or leave them out. |
| 44 | CONFIRMED | – | – |
| 45 | CONFIRMED | – | – |

Critical items: 1, 2 and 3 are all real. Items 4-9 and 12 are real stale v1 text. Every one of them is found verbatim in commit 11061f3.

## (b) Recompute on the pre-fix model

| Claim | QA | Mine | OK? |
|---|---|---|---|
| Lynas at A$14.07B | -11.6%, 37x, never | -11.62%, 37.2x, never | OK |
| Lynas at A$16.5B / US$10.9B | -14.9%, 44x | -14.87%, 43.6x | OK |
| Lynas at A$15.64B (raw-sourced) | not run | -13.8%, 41.3x, never | QA missed this; it is the better input |
| Leaderdrive / Keli at 2x prices | -10.6% / -2.4% | -10.62% / -2.36% (HDS -5.0, Wuzhou -4.9) | OK |
| Doubling deltas | Wuzhou 10.8, Leaderdrive 9.4, HDS 7.2, Keli 2.8, others ≤1.6 | 10.82 / 9.45 / 7.17 / 2.80; max other 1.62 (Huachen) | OK |
| Exit +5 turns | 3.0-4.5 | Leaderdrive 2.95, HDS 3.85, Keli 4.16, Wuzhou 4.54; Tuopu 5.30, Nabtesco 5.47; the 10x names 8.6-10.5 | OK |
| Sanhua breakeven | 16.9M | 16.93M | OK |
| Bull robot shares | 11.8 / 9.1 / 5.3 | 11.8 / 9.1 / 5.3 | OK |
| Hengli | CNY 1.4B / 17.7B / 34x / bull -7% | 1,407 / 17,671 / 34.4x / -7.24% | OK |
| HDS | 43.4x, ¥128.8B | 43.36x, ¥128,824M | OK |
| Leaderdrive | CNY 2.52B, 0.39, 0.27 | 2,521, 0.386, 0.269 | OK |
| Leaderdrive at 51.3B | -19%, 3.1M | -19.36%, 3.11M | OK |
| Huachen / Qinchuan | 375k × $160 = $60M; 57x / 56x | 375,000, $60M; 57.3x / 56.3x | OK |
| Hesai at 1.5x cap | -9% | -8.99% | OK |
| Audit sensitivities | -39.8 / -31.9 / -4.6 | -39.77 / -31.86 / -4.56 | OK |
| Nvidia robot share; $30-50B vs revenue | 0.046%; 4.0-6.7% | 0.0457%; 4.03-6.71% | OK |
| Tesla 30k / 400k | 1.0% / 11.9% | Tuopu 1.0 / 11.9, Sanhua 1.0 / 11.8 | OK |

No QA arithmetic errors. The only error of this kind is the choice of Lynas input, covered in the next section.

## (c) Bad fixes

1. **Lynas A$16.5B is not the right input.** It converts the US$ quote back at the model's assumed 0.66. The source's own price, US$10.87 against A$15.54, implies 0.70. Price × shares gives A$15.64B, which is -14% and 41x, not -15% and 44x. The note's phrase "consistent with A$15.54 × 1.01B shares" is false at 0.66, because that product is A$15.7B. The verdict ("policy trade") is unchanged.
2. **Fix 14 is not safe to assert.** MP had net income of $24.3M in FY2023, so "last earned a profit in 2022" is wrong. The parenthetical "by reviewer knowledge; not in the raw files" was pasted into client text.
3. **The Nvidia and LG Innotek move to a non-Tesla pool is immaterial.** Verified: at most 0.03 pt and 0.17 pt of CAGR. It is correct in direction.
4. **Fix 19 ("likely stale") points the wrong way.** The web evidence supports roughly $2.6-3.0B. See the ruling on #19.
5. **Fix 43 and fix 34 add unsourced claims.** Fix 43 adds sanctions-list claims tagged "(verify)". Fix 34 adds "perhaps 10%".
6. **Fix 22 has a unit error.** Schaeffler `base_ni_lc = -444` is a USD figure (-$0.47 × 945M) in a EUR field. It should be about -404. The field is unused, so there is no numeric impact.
7. **Fix 25 misses the lower Keli figure.** raw/07 has Keli at CNY 18.30B, which is lower than 18.8B.

## (d) Fix application

- **Model code is correct:**
  - `western_ex_tesla` = (west − tesla) × use_west, which gives 80k base and 200k bull.
  - The `embodied` pool and `embodied_mult` are fully removed, and the breakeven scaler is simplified correctly.
  - The grinder `use_cn` is now 0.50 for both Huachen and Qinchuan.
  - The formatter prints "0%" when the value rounds to 0, and never "-0%".
  - The dead `share_mult` is removed, and the docstring and path are fixed.
  - There is no guard for tesla > west, but no current scenario hits that.
- **Numbers match the model:**
  - The P §3 table matches all 18 rows × 10 columns (script check).
  - The breakeven table matches.
  - §1: 0.02%, 2.6-9x, Huachen 10%.
  - §4: CNY 1.4B / 18B / 34x, ¥129B, 43x, CNY 2.5B, 40% and a quarter, $88M, 55x.
  - §5 matches except the one item in the table below.
  - The §6 figure of 3.7x matches.
  - M §6: 2.4M-7.9M matches. M §9: 8x matches.
- **§5 verdict column vs §9:** they match, apart from wording on Huachen/Qinchuan (row 5 below).

| # | Location / quote | Problem | Corrected text |
|---|---|---|---|
| 1 | P §5 "about 3 to Keli and Huachen" | Huachen's delta is +2.28 | "about 3 to Keli, about 2 to Huachen" |
| 2 | P §4 Nvidia "(Figure, Agility, Boston Dynamics, 1X)" | Conflicts with post-fix M §4.8, "Figure 03 may use a custom chip" | "(Agility, Boston Dynamics, 1X; Figure 03 may use a custom chip)" |
| 3 | M §3 table "+460% day one to roughly $50B" | Fix 28 not applied here | "...to roughly $50B at its debut (down about 55% from peak by 20 Sep)" |
| 4 | M §9 "which change the risk picture more than the moat ranking" | Contradicts the §1 update box and the rewritten §6 | "which change both the risk picture and the moat ranking" |
| 5 | M §5 Huachen/Qinchuan verdict "Avoid" | §9 says "Avoid as robotics plays" | "Avoid as robotics plays" |
| 6 | M §6 "-15% a year on the base business" | It is the base case, and it should be -14% (see c1) | "-14% a year in the base case" |
| 7 | Lynas -15% / 44x / A$16.5B in P §1 banner, §3, §4, §6, §7; M §5, §6, §9; S; raw errata | Wrong input (c1) | Cap A$15,640M: $10,322M, 41x, -14% / -14% / -14% / -13%, still "never below 20M" |

## (e) Missed defects in the post-fix notes

| Sev | Location + quote | Problem | Evidence | Replacement text |
|---|---|---|---|---|
| major | P §4 MP "(it last earned a profit in 2022, by reviewer knowledge; not in the raw files)" | Factually wrong, and internal wording | MP FY2023 net income $24.3M (MP Q4/FY2023 release) | "...and the company returns to profit (it last reported a full-year net profit in 2023)." |
| major | P §4 Hesai "The model's 18% base growth is below the 2027 consensus path" | Not quantified, and it changes the "least-bad" verdict. The base is TTM $491M, while raw/07 has 2026 consensus at $698M and 2027 at $987M. The model's 2030 revenue ($1,022M) implies about 1% a year after 2027. | Recompute: on the 2027 consensus path then 18%, base case +12% (14x). From 2026 consensus, +8.5%. | "The base is conservative: on 2027 consensus revenue ($987M) growing 18% afterwards, Hesai's base case is about +12% a year, the only robot-exposed name that could be positive." |
| major | P §1 "probably stale", P §7 "likely stale"; M §5/§6 re-check | Wrong direction (see #19) | Nasdaq ECA2026-479 (8-for-1, ADS 1→8, 10 Jul 2026); Morningstar $2.97B (4 Sep 2026) | "Hesai's $2.92B cap is undated in our sources. A 4 Sep 2026 quote of $2.97B is consistent. Sites showing about $21B appear to apply the July 2026 8-for-1 split to an unchanged ADS count. Re-check before use." |
| major | M §4.7 "per a QA web check ... (verify)"; M §4.9 "a QA web check indicates ... (verify)" | Unverified sanctions claims and review language in a client note | Nothing in raw | Cite the DoD 1260H list (8 Jun 2026) for RoboSense and EVE and drop "QA web check (verify)". Otherwise delete. |
| minor | P §4 HDS "Schaeffler's 2027 process"; M §5 "new 2027 harmonic process"; M §7 "2027 Schaeffler strain-wave mass production" | Unhedged, while P §4 Schaeffler and M §4.2 now say single source | QA (d)5 | "Schaeffler's reported 2027 process (single source)" |
| minor | M §5 Hengli "Tesla-validated" | Unhedged, while §4.2 now says "reportedly" | – | "reportedly Tesla-validated" |
| minor | P §4 HDS "below Leaderdrive, Huachen, Qinchuan and Allegro" | LGES (72x) and Lynas (44x) are also higher | Model | "only Leaderdrive, LG Energy Solution, Allegro, Huachen, Qinchuan and Lynas are higher" |
| minor | P §7 / S comment "Keli is CNY 20.0B, between CNY 18.8B and 22.5B" | raw/07's lower figure is 18.30B (Sep 2025) | raw/07 | "between CNY 18.3B (Sep 2025) and 22.5B" |
| minor | S `FX["AUD"]=0.66` | The source implies 0.70. This affects robot share and the Lynas re-basing. | A$15.54 ↔ US$10.87 | Set 0.70, or state "assumed" with a date |
| minor | S Schaeffler `-444` | USD figure in a EUR field | -0.47 × 945 ÷ 1.10 | `-404` |
| minor | M §4.8 "Robotics is under 2% of revenue" vs P §4 "$10B physical-AI run-rate" | $10B is 2.4% of the FY27 $411B | raw/07 | "Robotics is a low-single-digit share of revenue" |

## (f) Severity calibration

- The three criticals are right. Lynas could arguably be major, because the verdict does not change, but a currency error in a client note justifies critical.
- These are over-rated as major; they are process or traceability items with no effect on client conclusions: 17, 18, 22, 26. Items 10 and 16 are also minor.
- These are under-rated:
  - 39 (minor): it moved Huachen's breakeven by 4.6M units.
  - 43 (minor): sanctions-list claims matter to clients.
  - The Hesai base-growth issue was missed entirely, and it is verdict-relevant.

## (g) Systematic QA weaknesses

- It chose fix inputs by convenience: the model's FX, and ignoring its own "lower figure" rule. It did not re-derive them from the raw price × shares.
- It relied on reviewer memory for a historical fact (MP) without checking it.
- It left a web conflict (Hesai) unresolved, even though its own search had found the explanation (the ADS ratio change).
- Its fix wording was pasted into client prose, including "QA web check", "(verify)" and "reviewer knowledge".
- It checked stale text against the model but did not check how conservative the inputs are, such as a TTM base against consensus.
- Its severity inflates hygiene items to major.

Sources: [stockanalysis LYC](https://stockanalysis.com/quote/asx/LYC/market-cap/), [MP FY2023 results](https://www.businesswire.com/news/home/20240222345443/en/MP-Materials-Reports-Fourth-Quarter-and-Full-Year-2023-Results), [Morningstar HSAI](https://www.morningstar.com/stocks/xnas/hsai/quote), [Nasdaq ECA2026-479 Hesai ratio change](https://www.nasdaqtrader.com/TraderNews.aspx?id=ECA2026-479), [TipRanks Hesai 8-for-1 split](https://www.tipranks.com/news/company-announcements/hesai-group-plans-eight-for-one-share-split-and-change-in-board-lot-size).

Files reviewed: `/home/user/debate-chatbot/reports/stocks/research/2026-09-19-robotics/{robotics-supply-chain-moats.md, projection-2030.md, projection-2030-model-output.md, raw/01-09}` and `/home/user/debate-chatbot/scripts/robotics_2030_model.py`, at 2981a54 and 17c0f63.
