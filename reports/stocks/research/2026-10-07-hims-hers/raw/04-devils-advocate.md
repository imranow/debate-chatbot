# Devil's advocate: Hims & Hers note (7 Oct 2026)

*Stream 04. Target: `hims-hers-analysis.md` and raw streams 01–03. I ran `raw/01-valuation_model.py` with `python3 -I`. It reproduces the note exactly. I stressed it with a separate script that imports the model read-only (`scratchpad/stress.py`, `scratchpad/extra.py`). I made 8 web searches. All web facts are search-snippet level. "(estimate)" marks my own numbers. Not investment advice.*

---

## (a) Verdict on the note's conclusion

**About right on the call ("not cheap enough"), but the base-case number is too generous. The note also hides a right skew that the bull can fairly use.**

- The model's arithmetic is correct. Its mechanics flatter the base case. It values EBITDA *before* stock pay at 14x. It assumes $1.2B of free cash flow by 2030, about 49% of cumulative EBITDA. That compares with 18% in 2025 and negative cash flow in H1 2026.
- Treat stock pay at 4% of revenue as a cost and the base falls from $38.26 (+6.4% a year) to about $28 (−1.2%). Add realistic cash flow and dilution fixes and it falls to about $25.6 (−3.2%).
- Subscriber growth is weaker than the headline. Hims' own "$90 without Eucalyptus" disclosure implies Eucalyptus brought in roughly 0.12–0.35M subscribers. Organic growth was then about +8% to +11%, not +19% (estimate).
- On the other side, the note judges the stock on the base case alone. Weight the published scenarios 25/50/25 and the expected value is about $45.5, or about 11% a year. Even the regulatory stream's own 30/50/20 odds give about 8%. The skew is real, but the fixes above shrink it. Applied to all three scenarios, 25/50/25 gives about 4% a year and 30/50/20 about 1%.
- Net: an honest central return is about 0–5% a year, below the note's 6%. "Not cheap enough" holds. The note should say plainly that the base is pre-stock-pay. It should also show the probability-weighted figure.

---

## (b) The 5 strongest bull counter-arguments

**B1. The base-case revenue is below what is already in hand.**
- Evidence: the August guide implies Q4 2026 revenue of about $949M, a $3.8B run-rate. Consensus 2027 revenue is about $4.0B. The base case's 2030 revenue is $5.18B. That is only 8% a year from the Q4 run-rate and 12.8% from the 2026 midpoint. Revenue guidance was raised three times in 2026.
- Model effect: $6.0B of 2030 revenue at 14% gives **$43.95, +10.0% a year**, up from +6.4%. That is the note's own 10% hurdle.
- Weakness: most of the 2026 raises are Eucalyptus (see R5).

**B2. Revenue and gross profit per subscriber are rising, and Q2 may be the margin trough.**
- Evidence: monthly revenue per subscriber without Eucalyptus was $90, against $76 a year earlier (+18%, company figure via 10-Q snippet). Gross profit dollars grew 16% in Q2 ($482M vs $414M) even as margin fell 12 points. Gross profit after marketing grew 12% ($220M vs $196M).
- The Q3 guide implies about $96–99 a month per subscriber (estimate). That is already above the base case's $1,150 a year ($95.8 a month). The Q3 EBITDA guide midpoint is 9.6%, up from 8.0% in Q2.
- Model effect: $1,190 per subscriber gives **+7.2%** (+0.8 pts). A 15% margin gives **+8.1%**.

**B3. The scenario spread is skewed up, and the note reports only the middle.**
- Evidence: bear $7, base $38, bull $99. The downside is capped at −$29 a share. The upside is +$69.
- Model effect: 25/50/25 weights give **$45.5, +10.9% a year**. The regulatory stream's 30/50/20 gives **$41.0, +8.2%**. 40/40/20 gives $37.8, +6.1%.
- Weakness: once stock pay is charged in every scenario, these fall to +4.2%, +1.2% and −0.8%.

**B4. Pills, the Lilly channel and marketing leverage could lift the 2030 margin.**
- Evidence: marketing fell from 46.0% of revenue (2024) to 39.2% (2025) and 34.8% (Q2 2026). The Wegovy pill has passed 3M prescriptions since January. It is about 35% of Wegovy prescriptions (our GLP-1 pen note). On the note's own table it earns about 45% gross margin against about 27% for the injection. Lilly prescriptions filled by LillyDirect carry no pass-through drug revenue, so they are fee-only and high-margin. Canada generic semaglutide (from C$149 a month since 21 May 2026) is a legal own-made product.
- Model effect: the note's breakeven says a 16.2% margin gives 10% a year. With 4.8M subscribers, $1,200, 15% and 15x, the base gives **$49.12, +12.9%**.

**B5. A 14x exit multiple is below where the stock trades today.**
- Evidence: the stock is on about 25x 2026 and 18x 2027 adjusted EBITDA. A low-teens grower with net cash in 2030 (base) can plausibly hold 16x.
- Model effect: 16x gives **$43.36, +9.6%**. 18x with management's plan gives +28%.
- Weakness: 14x adjusted EBITDA already equals about 24x EBITDA after stock pay (14 × 14% / 8.2%). That is not low.

**Bull points that do not hold up:**
- **Short squeeze.** Short interest is 26–29%, but days to cover is only 3.2–3.7 and the borrow fee is about 0.3% (early Sep). The stock is easy to borrow, so this is a weak squeeze setup and not a valuation input.
- **Buybacks.** About $225M of authorisation is left, 3.3% of market cap. But H1 cash flow was negative. About $284M of Eucalyptus cash is due within 18 months, and $1B of notes is due in May 2030. There is little real capacity.
- **2032 capped call.** The model ignores it, but it is worth only **+$0.44 a share** in the base and +$0.95 in the bull.

---

## (c) The 5 strongest bear counter-arguments

**R1. The model values EBITDA before stock pay.**
- Evidence: stock pay was $135.2M in 2025, 5.8% of revenue. The model applies 14x to adjusted EBITDA, which excludes it. Its 2%-a-year dilution input covers stock pay only to 2030, not after.
- Model effect (14% adjusted margin less stock pay, 14x): at 5.8% → **$23.15, −5.5%**; at 4.0% → **$27.97, −1.2%**; at 3.0% → $30.60, +1.0%. Management's plan with 4% stock pay falls from +21.3% to +15.4%. The bull falls from +33% to +27%.

**R2. Organic subscriber growth is about half the headline, and FTC/Visa fixes may raise churn.**
- Evidence: Hims says Q2 revenue per subscriber would be $90 without Eucalyptus, against $92 with it. Backing out gives Eucalyptus average subscribers of 58–117k (estimate). That implies an end-June count of about 0.12–0.35M, depending on how Hims averages. Organic end-Q2 subscribers are then about 2.63–2.72M, **+8% to +11% y/y**. Organic Q2 net adds are about 44–132k. Marketing per organic net add is then about $2,000–5,900, not $874. Hims does not disclose churn.
- The FTC alleges cancel friction and charging before a real consult. Visa reportedly requires disputes below 1.5% of transactions for three straight months. Card acceptance is the payment rail of a cash-pay model.
- Model effect: 4.0M subscribers in 2030 gives **$34.29, +3.7%**.

**R3. The cash assumptions are rich, and some debt-like items are missing.**
- Evidence: FY2025 free cash flow was $57.4M on $318M EBITDA (18%). Q2 2026 was −$68.2M. The base needs $1.2B from H2 2026 to 2030. On a plausible EBITDA path ($180M H2-26, $407M 2027, rising to $725M in 2030) that is 49% conversion.
- The model leaves out the $400M JPMorgan receivables facility signed 1 July 2026. It is uncommitted and runs 364 days. Its balance will first show in the Q3 10-Q. The 2030 notes ($1B) mature in May 2030. In the bear case cash is about $557M, so refinancing is needed.
- Model effect: cash flow of $400M gives **+4.5%**. $0 gives +3.5%. The facility fully drawn takes the base to +5.5% and the bear to **−32.5%**.

**R4. Drug price deflation and direct channels undercut the $149 membership.**
- Evidence:
  - NovoCare: Wegovy pen $199 for the first two fills (to 31 Dec 2026), then $349. The pill runs $149–299 by dose.
  - Novo's own multi-month subscription runs down to $249 a month on 12-month plans for both pill and injection.
  - Novo cuts US list prices by up to 50% from 1 Jan 2027.
  - LillyDirect Zepbound is from $299. Amazon offers $149 pills and $299 injections, plus insurance.
  - Hims' $149 membership roughly doubles the patient's cost on a $149 pill.
- Revenue per subscriber and margin are linked in the model but entered as independent inputs. If drug revenue is booked gross, deflation cuts revenue per subscriber, not gross profit dollars.
- Model effect: $1,050 per subscriber gives **$35.15, +4.3%**. A 12x multiple gives **$33.15, +2.9%**.

**R5. The guidance record and governance weaken the 2030 plan.**
- Evidence: the EBITDA guide midpoint fell twice: $337.5M → $312.5M → $300M. Meanwhile the 2030 $1.3B target was "reaffirmed with increasing conviction". It needs about 44% a year.
- The May→August revenue raise of $300M is mostly seven months of Eucalyptus (about $280M at $40M a month). The May guide excluded Eucalyptus. So the organic guide barely moved. Eucalyptus cost about $968.5M (fair value) and appears to add roughly no 2026 EBITDA.
- Other weights: the DOJ referral is still open; Novo's dismissal was without prejudice; two securities suits are pending; the CEO holds about 87% of votes; the chief accounting officer is changing.
- Model effect: a "bear-adjusted base" (4% stock pay as cost, $600M cash flow, Eucalyptus stock at $25, +10M award shares) gives **$24.58, −4.1%**. With the $400M facility drawn it gives $23.17, −5.5%.

---

## (d) Model audit

**Reproduction.** Output matches the note and raw 01 exactly: bear $7.01 / −28.8%, base $38.26 / +6.4%, bull $98.62 / +33.1%, management plan $66.64 / +21.3%. My re-implementation matches `value()` to 1e-6 before any fix.

**Checks that pass:**
- Horizon: 7 Oct 2026 → 31 Dec 2030 = 4.233 years. Correct.
- Shares: 224.94M Class A (Form 144, 16 Sep) + 8.38M Class V (proxy, April) = 233.3M. Fine. If a Eucalyptus stock instalment was paid before 16 Sep, it is double-counted, up to about 2.4M shares. That is small.
- Base worked example: EV $10,143M + net cash $717M = $10,860M ÷ 283.9M shares = $38.26. Correct.
- The convert test is correct and continuous at the $29.53 threshold, because the debt equals the conversion shares × the conversion price.
- The note's "10% a year only below roughly $25": solved entry price is **$25.33**. Correct.
- The note's "about 18.6M Eucalyptus shares" and "27.8M convert shares" are correct.

**Errors and gaps (each is the change in base value per share or return):**

| # | Issue | Fix tested | Base result |
|---|---|---|---|
| 1 | Stock pay excluded from the capitalised EBITDA | Margin less 4.0% / 5.8% of revenue | $27.97 (−1.2%) / $23.15 (−5.5%) |
| 2 | Cumulative cash flow of $1.2B = 49% conversion vs 18% in 2025 | $800M / $400M / $0 | +5.5% / +4.5% / +3.5% |
| 3 | 2032 capped call ignored (offsets dilution to $50.15) | Add capped-call value | $38.70 (+6.7%); bull $99.57 |
| 4 | Eucalyptus stock priced at $29.40 in every scenario | Bear at $10 / $15; bull at $40 | Bear $6.37 / $6.68; bull $100.29 |
| 5 | Earn-out $100M in base vs 10-Q fair value $59.6M | $59.6M | $38.43 (+6.5%) |
| 6 | $400M receivables facility not in net debt | Treat as debt if drawn | $36.85 (+5.5%); bear $5.57 (−32.5%) |
| 7 | No existing RSU/option overhang (size not found) | +10M / +20M shares | $36.96 / $35.74 |
| 8 | The management case reuses the base's $1.2B cash flow, though its EBITDA is higher | — | Understates the management case slightly |
| 9 | Revenue per subscriber and margin entered as independent inputs, though pass-through links them | — | Can double-count deflation in the bear |
| 10 | Exit multiple applied to trailing 2030 EBITDA | — | Mildly conservative for a grower |

**Recomputed base cases:**
- **Fully fixed base** (4% stock pay, capped call, Eucalyptus stock at $31, $800M cash flow, +10M award shares): **$25.63, −3.2% a year**.
- Bear-adjusted base: $24.58 (−4.1%).
- Bull-adjusted base (4.8M, $1,200, 15%, 15x, capped call): $49.12 (+12.9%).
- At the latest price of about $29.79: base +6.1%.

**Two errors in the note's text:**
1. The cost-per-add claim runs the wrong way. "Net adds understate gross adds" makes $874 an upper bound per *gross* add. But "some of the 300,000 may be Eucalyptus customers" makes it a *lower* bound per organic add. The two effects point in opposite directions.
2. The margin sensitivity is understated. On the grid, 8%→11% moves the return 7.0 points, 11%→14% moves it 5.4, 14%→17% moves 4.7, and 17%→20% moves 4.1. "4–5 points" should read "4–7 points, larger on the downside".

---

## (e) Specific text changes to the note

1. "It gives about $38 a share, or about 6% a year." → "It gives about $38 a share, or about 6% a year, before stock pay. Charging stock pay at 4% of revenue as a cost gives about $28, or about −1% a year."
2. "Revenue guidance went up by $300M between May and August while the profit guide did not. That says the extra revenue earns roughly nothing in 2026." → "Revenue guidance went up by $300M between May and August. About $280M of that is seven months of Eucalyptus, which the May guide excluded. The EBITDA midpoint fell by $12.5M. So the organic guide barely moved, and Eucalyptus adds roughly no 2026 EBITDA."
3. "| Subscribers | 2.891M (+19%; includes part of June from Eucalyptus, not split out) |" → "| Subscribers | 2.891M (+19%; includes Eucalyptus from June. Our estimate from Hims' $90 ex-Eucalyptus figure: Eucalyptus about 0.12–0.35M, organic growth about +8% to +11%) |"
4. "That is an upper bound: net adds understate gross adds, and some of the 300,000 may be Eucalyptus customers." → "Per gross add it is an upper bound, because net adds understate gross adds. Per organic add it is a lower bound, because the 300,000 includes Eucalyptus customers. Excluding them, marketing per organic net add is about $2,000–5,900 (estimate)."
5. "**The margin is the swing factor**: each 3 points of 2030 margin moves the base-case return by about 4–5 points a year." → "**The margin is the swing factor**: each 3 points of 2030 margin moves the base-case return by about 4–7 points a year, more on the downside."
6. "The return compares that value with $29.40 over 4.23 years. All inputs are our assumptions." → "The return compares that value with $29.40 over 4.23 years. All inputs are our assumptions. The multiple is applied to EBITDA before stock pay. The base assumes $1.2B of free cash flow from mid-2026 to 2030, about half of cumulative EBITDA, against 18% in 2025."
7. "**Eucalyptus deferred payments:** about $710M over 18 months, plus an earn-out of up to $200M. About 60% can be paid in stock." → "**Eucalyptus deferred payments:** about $710M nominal ($683.9M fair value in the Q2 10-Q) over 18 months, plus an earn-out of up to $200M (fair value $59.6M). The 10-K said about 60% can be paid in stock; the Q2 10-Q says 'a significant majority'."
8. "| Enterprise value (EV: market cap plus debt minus cash) | about $7.42B, or about $8.13B including Eucalyptus payments |" → append "; excludes any draw on the $400M JPMorgan receivables facility (signed 1 Jul 2026; balance first visible in the Q3 10-Q)".
9. "| Short interest | about 27% of shares (31 Jul 2026; dated) |" → "| Short interest | about 26–29% (late Jul 2026; dated); 3.2–3.7 days to cover; borrow fee about 0.3%, so easy to borrow and squeeze risk is low |"
10. "This matches our earlier GLP-1 note: the drug makers keep most of the value." → "Our earlier GLP-1 note found drug makers keep most of the device and fill value against their suppliers. It did not study telehealth, but the channel data here point the same way."
11. "The chief accounting officer leaves on 9 October 2026, and two directors were not renominated." → "The chief accounting officer leaves on 9 October 2026. Jon Franklin (ex-Rivian) was named successor on 7 October. Two directors were not renominated."
12. "| 9 Oct 2026 | Chief accounting officer departs | Finance-team continuity before Q3 |" → "| 9 Oct 2026 | CAO handover to Jon Franklin (named 7 Oct) | Finance-team continuity before Q3 |"
13. "| Branded Wegovy injection (since March 2026) | Novo (Hims must sell at Novo's self-pay price) | about $349 drug + $149 membership | about 27% (estimate) |" → "| Branded Wegovy injection (since March 2026) | Novo (Hims must sell at Novo's self-pay price) | $199 (first two fills, to end-2026) to $349 drug, or $249–329 on Novo's multi-month plans, + $149 membership | about 27% (estimate; assumes gross booking. Raw 02 says maker pharmacies fill some scripts, which would mean fee-only revenue) |"
14. Section 1, after "**Verdict: not cheap enough for the risks.**" → add: "Weighting our bear, base and bull cases 30/50/20 gives about 8% a year. With stock pay charged as a cost, that falls to about 1%."
15. Section 7 bearish signals → add: "A material draw on the $400M receivables facility, or Eucalyptus instalments settled mainly in stock at prices below $29.53."

---

## (f) New facts found

1. **New chief accounting officer.** Jon Franklin was named CAO on 7 Oct 2026. He is a CPA with 20 years' experience, formerly at Rivian, and reports to CFO Yemi Okupe. The note says only that the old CAO leaves. [Investing.com]
2. **Latest price.** About $29.79 (tracker), down about 8% year to date from $32.45. The stock rose about 3% on 5 Oct. [MarketBeat; tradersunion]
3. **Q3 date.** Not yet announced. The estimate is 9 Nov 2026 (a Monday after the close). Hims usually announces the date in mid-October (13 Oct 2025 for 3 Nov 2025). [Business Wire 2025; quantisnow]
4. **Eucalyptus accounting (Q2 10-Q via snippets).** Purchase price $968.5M: $225.0M upfront, $683.9M deferred (six quarterly instalments), and $59.6M contingent fair value. The 10-Q says "a significant majority" is stock-settleable, against "approximately 60%" in the 10-K. Eucalyptus was about 5% of Q2 revenue and about 15% pro forma. Revenue per subscriber without it was $90. No instalment or share issuance was found for Sep 2026. [10-Q; beancount.io]
5. **$400M receivables facility.** XeCare and Apostrophe Pharmacy signed a Master Receivables Purchase Agreement with JPMorgan on 1 Jul 2026. It is uncommitted and runs 364 days, with extensions. It was enabled by Amendment No. 4 to the revolver (26 Jun). At 30 Jun the revolver had $162.4M available and $12.6M of letters of credit. The drawn balance is unknown. [sahmcapital; stocktwits; 10-Q]
6. **Novo pricing.** Novo launched a multi-month Wegovy subscription on 31 Mar 2026: injection $329 / $299 / $249 a month on 3/6/12-month plans; pill $289 / $269 / $249 after a $149 start. Hims was listed as "coming soon". NovoCare in Sep 2026: pill $149–299 by dose; pen $199 for two fills to 31 Dec 2026, then $349; Wegovy 7.2mg $399. US list prices are cut by up to 50% from 1 Jan 2027. [PR Newswire; FierceHealthcare; CNBC]
7. **No new DOJ or FDA action found.** Nothing found for Aug–Oct 2026. The 10-Q risk factor says official statements "may lead to investigations". [sherwood.news; 10-Q]
8. **No 2026 short-seller report found.** Short interest was 26.4% of shares outstanding (Equibles, 19 Jul 2026). [equibles]
9. **Not in the note (unverified).** A YourBio Health acquisition was mentioned ahead of Q2 (Capital.com, Aug 2026). Regional chief medical officers were named for the UK/EMEA and Australia (5 Oct). The CFO sold 2,000 shares on 1 Oct 2026 under a pre-set 10b5-1 trading plan (raw 03).

**Sources**
- [Investing.com: Hims appoints Jon Franklin as CAO](https://za.investing.com/news/stock-market-news/hims--hers-appoints-jon-franklin-as-chief-accounting-officer-93CH-4494515)
- [MarketBeat HIMS](https://www.marketbeat.com/stocks/NYSE/HIMS/); [tradersunion](https://tradersunion.com/news/stocks/show/3670899-hims-and-hers-health-rises); [Yahoo: regional CMOs](https://finance.yahoo.com/healthcare/articles/investors-may-respond-hims-hers-140826626.html)
- [Business Wire: Q3 2025 date notice](https://www.businesswire.com/news/home/20251013956129/en/Hims-Hers-to-Announce-Third-Quarter-2025-Financial-Results-on-November-3-2025/); [quantisnow HIMS earnings](https://www.quantisnow.com/earnings/HIMS)
- [Hims Q2 2026 10-Q](https://www.sec.gov/Archives/edgar/data/0001773751/000177375126000163/hims-20260630.htm); [beancount.io Q2 2026 analysis](https://beancount.io/blog/2026/09/26/hims-hers-q2-2026-earnings-analysis)
- [Sahm Capital: $400M receivables facility](https://www.sahmcapital.com/news/content/hims-hers-signs-usd-400-million-receivables-purchase-facility-with-jpmorgan-chase-2026-07-02); [Stocktwits](https://stocktwits.com/news-articles/markets/equity/hims-2026-high-400m-jp-morgan-retail-less-bearish/cZme2EPR71N)
- [PR Newswire: Novo Wegovy subscription](https://www.prnewswire.com/news-releases/novo-nordisk-launches-first-and-only-multi-month-subscription-program-for-fda-approved-wegovy-offering-savings-of-up-to-1-200year-302729943.html); [FierceHealthcare](https://www.fiercehealthcare.com/telehealth/novo-nordisk-launches-first-and-only-wegovy-subscription-program); [CNBC: list price cuts](https://www.cnbc.com/2026/02/24/novo-nordisk-to-slash-wegovy-ozempic-us-list-prices-by-up-to-50percent.html); [glpchart Wegovy cost](https://glpchart.com/wegovy-cost/)
- [Sherwood: HHS DOJ referral](https://sherwood.news/markets/fda-says-it-will-take-decisive-steps-against-glp-1-compounders-reuters/)
- [Equibles HIMS](https://equibles.com/stocks/hims); [Capital.com 5 Aug 2026](https://capital.com/en-gb/market-updates/hims-and-hers-share-price-05-08-2026)
- [GlobeNewswire: class action deadline](https://www.globenewswire.com/news-release/2026/10/05/3374685/1020/en/kaplan-fox-advises-hims-hers-health-inc-nyse-hims-investors-of-a-securities-class-action-deadline-on-november-2-2026.html)
