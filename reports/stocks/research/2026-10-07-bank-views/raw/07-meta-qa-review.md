# Meta-QA review: bank views QA (7 Oct 2026)

Scope: `raw/06-qa-review.md` (34 defects, PASS WITH FIXES), checked against the pre-fix note (`2e1e5e3`), the post-fix note (`d338827`), raw files 01–05, and the sister notes named in section 7 of the note. Every line reference in the QA was opened. All arithmetic was rerun in Python. Four web searches were used, only on facts the QA brought in from its own searches. No repo file was changed except this one.

## (f) Verdicts

- **QA report: RELIABLE WITH CORRECTIONS.** All 34 quotes are really in the pre-fix note. Every cited raw line says what the QA says it does. Its arithmetic is all correct. But four of its replacement texts add new errors or unsupported claims. Four of its 34 defects (#5, #6, #14, #34) are only partly right; the other 30 are confirmed. Its "Agree?" judgements in section 7 are uneven.
- **Post-fix note: YES WITH FIXES.** Every QA fix was applied, nearly word for word. No critical errors remain. But the note should not go out until the 7 major items below are fixed: F1 to F6 and M1.

## Web checks on facts the QA brought in

| QA fact | Result |
|---|---|
| UBS 21 Aug target is from UBS Global Wealth Management (Reuters) | **Confirmed.** Reuters copies on Zawya and Lufkin Daily News carry that headline, with 8,100 year-end, 8,400 mid-2027, EPS $350 / $400 and about 6% upside from 7,641.16. One article giving "from 7,500" looks like an older story. That may also be where CNBC's 8,900 comes from. |
| Goldman "close to the current 21" is from the May note | **Confirmed.** The 26 May note raised the target to 8,000 from 7,600 and said the multiple stays "close to the current 21" (Yahoo Finance; Invezz). |
| 10-year "briefly passed 5.3% on 30 September, its highest since 2002" | **Not confirmed.** Reports through 25 Sep put the 10-year at about 5.1–5.2%, "the highest since 2007". The 30-year was about 5.48%, its highest since 2004. No source found gives 5.3% on 30 Sep or "highest since 2002". The QA's own 247 Wall St source has the headline "broke its 2007 peak". |
| "2 October jobs report" (added to the note's §4 and §9) | **Confirmed but not in any raw file.** It was released 2 Oct: +29,000 payrolls against about 90,000 expected, unemployment 4.2%, and October hold odds of about 77% afterwards (First Trust, Fox Business). |

Sources: [Zawya (Reuters)](https://www.zawya.com/en/capital-markets/corporate-earnings/ubs-global-wealth-management-lifts-sp-500-year-end-target-to-8100-463458); [Lufkin Daily News (Reuters)](https://lufkindailynews.com/news_reuters/business/ubs-global-wealth-management-lifts-s-p-500-year-end-target-to-8-100/article_f5a9c808-82f9-5124-a2df-593acdb2850b.html); [Yahoo Finance, Goldman](https://finance.yahoo.com/markets/stocks/articles/goldman-sachs-hikes-p-500-084300964.html); [Invezz, 27 May](https://invezz.com/sg/news/2026/05/27/sandampp-500-could-hit-8000-by-end-2026-goldman-sachs-says/); [Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield/news/586699); [Crypto Briefing, highest since 2007](https://cryptobriefing.com/10-year-treasury-yield-highest-since-2007/); [First Trust, payrolls](https://www.ftportfolios.com/Commentary/EconomicResearch/2026/10/2/nonfarm-payrolls-increased-29,000-in-september); [Fox Business](https://www.foxbusiness.com/economy/us-jobs-report-september-2026.amp).

## (a) Ruling on each QA defect

Quote check: all 34 quotes match the pre-fix note exactly. Line references: all checked and correct.

| # | QA sev. | Ruling | Note |
|---|---|---|---|
| 1 | major | CONFIRMED | Wilson said "consolidation" (01 l.50). The yield context is real, but the replacement adds "highest since 2002", which is unconfirmed (see F1). |
| 2 | major | CONFIRMED | 4.80% is an 8 Sep aggregator close (03 l.74). The 0.8-point gap is right on 5.2%. |
| 3 | major | CONFIRMED | Web confirms UBS GWM. The severity is closer to minor. |
| 4 | major | CONFIRMED | 1 point = 400; the gap is 550–700. Real, but minor: a derived aside. |
| 5 | major | PARTLY | Dropped caveats and mixed scopes: real. "Almost 2 times" is loose rounding (1.75x; 2.1x against the older $95bn), not a hard error. The replacement adds new problems (F3, F4). |
| 6 | major | PARTLY | MS part is right (China 446k in 2030, 24.4m by 2036; 05 l.38–39). The Citi part is wrong: the 1.3bn by 2035 counts all "AI robots", not humanoids (05 l.174). For humanoids, Citi's only figure is for 2050. |
| 7 | major | CONFIRMED | Raw 02 l.136–150 gives "nf" for the reasons. The note made up the reasons. |
| 8 | major | CONFIRMED | Units mixed up (04 l.150–162; 03 l.111, 120). |
| 9 | major | CONFIRMED | Stale and undated; BofA's −3% is absolute, not relative. |
| 10 | major | CONFIRMED | Global AI capex vs hyperscaler capex; caveat dropped. |
| 11 | major | CONFIRMED | Goldman points tagged unverified (03 l.68–69). |
| 12 | major | CONFIRMED | Problem real. The fix is still too generous to us (F7). |
| 13 | minor | CONFIRMED | |
| 14 | minor | PARTLY | The table already said implied P/E is "our arithmetic", so the labelling point is weak. Adding Goldman's own figures is useful. The replacement's last sentence is unsupported (F10). |
| 15 | minor | CONFIRMED | MS +23% (unverified) is outside 24–35%. |
| 16 | minor | CONFIRMED | |
| 17 | minor | CONFIRMED | Range recomputed: −0.2% to +12.5%. |
| 18 | minor | CONFIRMED | |
| 19 | minor | CONFIRMED | |
| 20 | minor | CONFIRMED | |
| 21 | minor | CONFIRMED | The replacement drops the $21 figure the QA itself mentions (F15). |
| 22 | minor | CONFIRMED | |
| 23 | minor | CONFIRMED | |
| 24 | minor | CONFIRMED | |
| 25 | minor | CONFIRMED | |
| 26 | minor | CONFIRMED | |
| 27 | minor | CONFIRMED | |
| 28 | minor | CONFIRMED | |
| 29 | minor | CONFIRMED | Problem real. The replacement adds an unsupported claim (F5). |
| 30 | minor | CONFIRMED | Added a second Buy but left "Partly agree" (F8). |
| 31 | minor | CONFIRMED | Accurate against the Hims note at `d338827`. That note was "pre-review" and has since been revised (F6). |
| 32 | minor | CONFIRMED | |
| 33 | minor | CONFIRMED | Trivial. |
| 34 | minor | PARTLY | The UBS and 10-year gaps are fine. The jobs-report line is not in the raw files and clashes with Hatzius's early-October view (F2). |

Other QA errors:
- Its verdict says "the bank-by-bank target table is correct", but #3 and #24 are table defects.
- #8 says the UBS line "is a currency view, not a regional one", but its fix leaves it in the Regions row (F11).
- 12 "major" is inflated. #3 and #4 are minor.

## (c) Recompute table

Python, S&P 500 = 7,818.93.

| Item | Stated | Recomputed | OK? |
|---|---|---|---|
| Median YE target | 8,000 | 8,000 | yes |
| Index vs median | 2.3% below | 2.26% below; 2.32% upside | yes |
| Mean target (QA) | 7,960 / +1.8% | 7,960 / +1.80% | yes |
| Band ex-BofA | 150 | 150 | yes |
| P/E GS / JPM / Citi / UBS / WF / Barc / DB | 20.8 / 19.0 / 20.3 / 20.3 / 20.4 / 19.2 / 19.0 | 20.78 / 19.05 / 20.25 / 20.25 / 20.38 / 19.20 / 19.05 | yes |
| HSBC P/E 2026 | 22.5x | 22.50 | yes |
| JPM recipe | ≈8,000 | 7,980 | yes |
| One point of multiple | 400, about 5% | 400; 5.0% | yes |
| Post-fix "1.5 points (600) = gap to median" | 1.5 | 600/400 = 1.50 | yes |
| GS vs JPM/DB 2027 EPS | $35 | 35 | yes |
| 2027 EPS growth | 12–17% | GS 13.2, JPM 15.1, Citi/UBS 14.3, WF 14.7, Barc 13.4, DB 17.3, BofA/MS 12 | yes |
| 2026 EPS growth (post-fix) | 23–35% | MS 23 (unverified), GS 24, DB 28, BofA/HSBC 33, JPM 35 | yes |
| 12m / 2027 targets vs spot | 0% to +12.5% | BofA −0.24, MS +6.15, UBS +7.43, GS +11.27, Barc +12.55 | yes |
| UBS 8,900 (if used) | — | +13.8% | not used; fine |
| Raw 01 median 2027 EPS | QA: $400, 19.55x | 7 banks, $400, 19.55x | yes (QA right; raw wrong) |
| GLP-1 JPM / GS | about 1.75x | 1.754 | yes |
| GLP-1 like-for-like (not stated) | — | JPM vs UBS (both incl. diabetes) 1.54x; GS vs UBS obesity 1.43x | see F4 |
| Humanoid raise 2030 / 2035 | 3.48x / 4.70x | 3.48 / 4.70 (6.48/1.38) | yes |
| MS power gap | 38; 57 | 68−15−15 = 38; 97−21−19 = 57 | yes |
| Hesai GS upside | +93% | +93.4% | yes |
| FICO cut | −50% | −50% | yes |
| LLY Citi vs HSBC | 70% | 70.2% | yes |
| NVO MS vs price | −7.5% | −7.5% | yes |
| GS 10-year vs spot | 0.8pp | 5.2 − 4.4 = 0.8 (0.9 on 5.3) | yes |
| GS capex growth (QA: raw +54%/+12% vs +50%/+17%) | +50% / +17% | +50.0% / +16.7% | yes |
| JPM debt share (not stated) | — | 4.1/5.5 = 75% | consistent |
| GS "AI ≈ half of 2026 growth" vs "11 points" | about half | 11/24 = 46% | consistent |
| JPM target path | four changes | 7,200 → 7,600 → 7,800 → 8,000 | yes |
| UBS upside (raw 01) | 6% / 10% from 7,641 | 6.0% / 9.9% | yes |

No arithmetic errors were found in the QA or in sections 1–4 of the post-fix note.

## (d) Fix-application problems

Every QA fix and every staleness item was applied. No fix was skipped. The problems below come from the replacement texts themselves, or from how they sit next to text that was not changed.

| # | Sev. | Location + exact quote | Problem | Exact replacement |
|---|---|---|---|---|
| F1 | major | §1 item 4: "Secondary reports say the 10-year briefly passed 5.3% on 30 September, its highest since 2002, then eased to about 5.2% on 2 October (unverified)." §4 10-year row: "Secondary reports put it near 5.3% on 30 September" | "Highest since 2002" is unconfirmed. Reports say about 5.1–5.2%, the highest since 2007. §1 says "passed 5.3%" and §4 says "near 5.3%": the two places disagree. | §1: "Secondary reports say the 10-year passed 5% in mid-September and reached about 5.2–5.3% in late September, its highest since about 2007, then eased to about 5.2% on 2 October (unverified; check a live quote)." §4: "Secondary reports put it at about 5.2–5.3% in late September and about 5.2% on 2 October (unverified)." |
| F2 | major | §4 Fed row: "...but in early October Hatzius said markets over-price further hikes (unverified)... All of these predate the 2 October jobs report". §9: "The Fed calls predate the 2 October jobs report." | Contradiction in the same cell: Hatzius's early-October remark has no exact date (03 l.69) and may come after 2 Oct. The jobs report is in no raw file. It is real (web): +29,000, unemployment 4.2%. | §4: "Except perhaps Hatzius's early-October comment, these calls predate the weak September jobs report (2 October: +29,000 payrolls, unemployment 4.2%; secondary reports, unverified), which cut the odds of an October hike." §9: "Most Fed calls predate the 2 October jobs report; check for updates." |
| F3 | major | §4 GLP-1 row: "Morgan Stanley's base case is about $190bn at peak, on a 2035 horizon." | The scope and the caveat were both dropped: raw 05 l.44 says "(obesity plus diabetes)" and "(unverified date)". It is also a 2035 figure in a "2030" row. MS's 2030 figures conflict: $105bn (about 2024; 05 l.45) and $54bn (02 l.203). | "Morgan Stanley gives no clean 2030 figure (older notes say $105bn, one says $54bn); its latest base case is about $190bn at peak for obesity plus diabetes, on a 2035 horizon (date not confirmed)." |
| F4 | major | §4 GLP-1 row: "The scopes differ, so the headline gap (JPMorgan about 1.75 times Goldman) overstates the real disagreement" | Only half true. Like-for-like gaps are still large: JPMorgan $200bn vs UBS $130bn (both include diabetes) is 1.54x. Goldman $114bn vs UBS $80bn (obesity only) is 1.43x. | "The scopes differ, so JPMorgan's $200bn against Goldman's $114bn (1.75x) is not like for like. But like-for-like gaps are still wide: about 1.5x for the whole market (JPMorgan vs UBS) and about 1.4x for obesity alone (Goldman vs UBS)" |
| F5 | major | §7 Hesai, Agree cell: "Partly agree: both rank it best of the group, but Goldman's target implies about +93% and our base case is flat" | No source says Goldman ranks Hesai best among robot names. Goldman also rates Harmonic Drive and MP Buy (02 l.136, 147). | "Partly agree: Goldman is Buy and we rate it the least-bad robot name, but Goldman's target implies about +93% and our base case is flat" |
| F6 | major | §7 Hims, research cell: "Not cheap enough for the risks: base case about $38, about 6% a year from about $29.40 (separate note, 7 Oct)" | Correct for the Hims note at `d338827`, which was pre-review. The revised Hims note in the working tree now gives a central estimate of about 0–6% a year: about $38 (+6%) before stock pay and about $28 (−1%) after it. | "Not cheap enough for the risks: central estimate about 0–6% a year from about $29.40 (about $38 before stock pay, about $28 after; separate note, 7 Oct)". Re-check against the final Hims note before publishing. |
| F7 | minor | §7 West, Agree cell: "Agree with Morgan Stanley; most of the Street is more positive than we are" | MS's $365 is about the $374 price, so MS calls it roughly fair. We would buy only at $224–268, 28–40% lower. | "Closest to Morgan Stanley's Equal Weight, but we are more negative (we would buy only at $224–268); most of the Street is more positive" |
| F8 | minor | §7 Stevanato: "...Wells Fargo Overweight $35 (date not found); all older \| Avoid \| Partly agree" | The new Wells Fargo Buy makes two Buys against our Avoid. "Partly agree" is now too generous. | Agree cell: "Mostly disagree: Citi and Wells Fargo rate it Buy; only Morgan Stanley's Equal Weight is near our Avoid (all older)" |
| F9 | minor | §1 item 1: "**The banks are bullish, but they have run out of room.**" followed by the new "...imply about 0% to +12.5% from here." | The added sentence contradicts the heading. | Heading: "**The banks are bullish, but little room is left this year.**" |
| F10 | minor | §2: "These two Goldman figures are from different dates and measure different things." | "Measure different things" is unsupported. Both are described as forward P/E (01 l.24; 03 l.14). | "These two Goldman figures are four months apart, and our sources do not say which earnings each uses." |
| F11 | minor | §4 Regions: "UBS wealth CIO: trim the dollar into strength, hold gold" | The QA called this a currency view, not a regional one, but left it in Regions. | Delete it from Regions. If kept, add a row: "\| Dollar and gold \| UBS wealth CIO: trim the dollar into strength, hold gold as a hedge. Morgan Stanley economists: stronger dollar. Hartnett: stay risk-off until the dollar peaks (secondary) \|" |
| F12 | minor | §7 MP: "Goldman Buy $70–80 (May; sources conflict)" | "(May)" only fits the $80 figure. The $70 one is undated (02 l.136, 248). | "Goldman Buy $80 (8 May; another source shows $70, undated)" |
| F13 | minor | §2 UBS row: "8,400 by mid-2027 (one July report said 8,900; conflicting)" | Web checks suggest the "from 7,500" story is an older report. The 8,900 likely comes from the same story. | "8,400 by mid-2027 (a CNBC report dated 21 Jul gives 8,900; probably an older story)" |
| F14 | low | §2 UBS row "name not found", while §5 names Mark Haefele as UBS's wealth CIO | Readers may think the two disagree. | Strategist cell: "CIO office (CIO Mark Haefele; strategist not named)" |
| F15 | low | §8: "...reported at $32, $30, $25, $36 and $37 within months (order not fully confirmed)." | Drops the $21 figure the QA itself cites (02 l.249). | "...reported at $21, $25, $30, $32, $36 and $37 within months (order not confirmed)." |
| F16 | low | §1 item 5: "...Europe (8.5%) and emerging markets (7.2%; unverified)." | Raw 04 l.170 tags both the Europe and EM figures unverified. The LTCMA horizon is 10–15 years. | "...give US large caps 6.7% a year over 10–15 years, below Europe (8.5%) and emerging markets (7.2%) (both unverified)." |

## (e) Material defects both the QA and the fixes missed

| # | Sev. | Location + exact quote | Problem | Evidence | Exact replacement |
|---|---|---|---|---|---|
| M1 | major | §1 item 4: "On those figures his trigger has already been crossed." §4: "and Wilson's 5% trigger has already been crossed" | This implies Wilson's correction call has fired. But his own latest comments, after yields passed 5%, put drawdown risk at only 5–10%, and he planned to add risk-on names in October. Meanwhile the index closed at a record on 6 Oct. The note leaves this out. | 05 l.57; 01 l.12 | Append to §1 item 4: "Even so, Wilson's latest comments (about 2 October; unverified) put drawdown risk at 5–10% and he planned to add risk-on names in October, and the index closed at a record on 6 October." |
| M2 | minor | §7 Progyny: "JPMorgan Neutral $30 (21 Aug); Wells Fargo Buy $37 (20 Aug) \| Only on a big drawdown, as a benefits business \| Broadly agree with JPMorgan" | Same flaw the QA fixed for West. JPMorgan's $30 is about 11% above the roughly $27 price. We would buy only at $16–20, 26–41% lower. Wells Fargo, Citizens and the consensus are Buy or Overweight. | Egg-freezing note l.41, 71; 02 l.152–154, 173 | Banks cell: add "; Citizens Buy $33 (8 Sep); consensus Overweight". Agree cell: "Closer to JPMorgan's Neutral than to the Buys, but we are more negative: we would buy only at $16–20" |
| M3 | minor | §4 Humanoid: "Goldman 890k units in 2030 and about 6.5m in 2035" | A dropped caveat: raw files say it is unclear whether 6.5m is annual or cumulative. Our robotics note compares it with annual volumes. | 02 l.190, 253 | "...about 6.5m in 2035 (unclear whether annual or cumulative)..." |
| M4 | minor | §1 item 1: "Nine of ten big banks expect the S&P 500 to end 2026 between 7,950 and 8,100." | After the UBS fix, one of the ten is a wealth-arm call, not a sell-side strategist. §1 does not say so. | §2 note under the table | "Nine of ten big banks (one, UBS, through its wealth arm) expect..." |
| M5 | minor | §3: "Bank of America, Barclays, Wells Fargo, Morgan Stanley and HSBC all name some version of it." | HSBC calls fears of Fed hikes "overdone". It flags inflation prints, not the Fed. | 01 l.113 | "...and HSBC all name some version of it (HSBC flags inflation prints but calls Fed-hike fears 'overdone')." |

No other material defects were found in the post-fix note. Sections 3, 5, 6 and 8 trace cleanly to the raw files.

## Systematic QA weaknesses

- **Web facts went into the note with less care than raw facts.** "Highest since 2002" was not checked. The jobs-report fact was added to the note but not to any raw file or source list.
- **Replacement texts break the QA's own rules.** It demanded caveats everywhere, then dropped "(obesity plus diabetes)" and "(unverified date)" from its own Morgan Stanley addition. It added "both rank it best" and "measure different things" without a source.
- **Uneven judgement on the "Agree?" column.** It fixed West, but left Progyny and Stevanato, which have the same flaw. It added a bank Buy to Stevanato without revising the verdict.
- **It did not check that its new text fits the cells around it.** Examples: "All of these predate" sits next to an early-October Hatzius view, and the §1 heading no longer matches the sentence it added.
- **Severity inflation and small self-contradictions.** 12 "major" defects include minor ones. It called the target table "correct" while fixing two of its cells.
- **It cited a note it had not reviewed, and that note was mid-revision** (Hims). Section 7 rows need to be re-checked against the final sister notes.
