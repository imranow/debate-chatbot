# Hims & Hers (HIMS): From Drug Maker to Drug Store

*Research date 7 October 2026. Three research streams: financials and valuation (with a 2030 model, `raw/01-valuation_model.py`); GLP-1, compounding rules and legal risk; and competition, strategy and governance. Raw reports with sources are in `raw/`. The sandbox blocked every primary filing (sec.gov, investors.hims.com). So every figure comes from search snippets that quote Hims' releases, filings and calls. Figures seen in several snippets are treated as reported; single-source figures are marked unverified. Our own estimates are marked as estimates. Revised the same day after a devil's-advocate review (`raw/04-devils-advocate.md`; summary in section 7) and a QA review (`raw/05-qa-review.md`). Not investment advice.*

*Glossary. **GLP-1**: the class of weight-loss drugs that includes semaglutide (Wegovy, Ozempic) and tirzepatide (Zepbound, Mounjaro). **Compounding**: a pharmacy making its own version of a drug. **Convertible notes ("converts")**: debt that can turn into shares above a set price. **10-Q / 10-K / 8-K**: quarterly, annual and event filings with the US securities regulator. **Earn-out**: extra purchase price paid only if targets are met. **Fair value**: the accounting estimate of what a future payment is worth today. **Pass-through revenue**: revenue that is mostly someone else's price passing through the books.*

---

## 1. The answer first

Hims is growing fast again, but it has turned into a lower-margin business, and the stock prices in real doubt about its 2030 plan. Three facts matter most.

1. **It lost its highest-margin product.** Until March 2026, Hims made its own copies of the weight-loss drug semaglutide (Novo Nordisk's Ozempic and Wegovy) from cheap ingredients. On our estimate it kept about 80% of the price as gross profit. After a February crackdown by FDA and a Novo patent lawsuit, Hims settled with Novo on 9 March 2026. It now sells Novo's branded drugs at Novo's own cash prices and, on our reading, keeps mainly a service fee (terms not disclosed). The CEO said in February 2026 that only a small minority of subscribers used compounded GLP-1s. Gross margin fell from 76% to 64% in a year.
2. **Growth is back, but it is lower quality.** Second-quarter 2026 revenue rose 38% to $753.2M, and full-year guidance was raised to $3.1–3.3B. But US revenue grew only 16%. The rest came from international, which rose from $7.5M to $131.4M, mostly through acquisitions (Zava in July 2025; Eucalyptus in June 2026, about $40M in the quarter). Pass-through drug revenue inflates sales without adding much profit. Revenue guidance went up by $300M between May and August. About $280M of that is seven months of Eucalyptus at its June rate (estimate), which the May guide excluded. The profit guide midpoint fell by $12.5M. So the organic guide barely moved, and Eucalyptus appears to add roughly no 2026 profit (our inference).
3. **At about $29.40, the stock needs a margin recovery to pay well.** Our base case is 4.5 million subscribers and a 14% adjusted EBITDA margin (profit before interest, tax, depreciation and stock pay) in 2030, against 2.89 million and 8% today. It gives about $38 a share, or about 6% a year, before stock pay. Charging stock pay at 4% of revenue as a cost gives about $28, or about −1% a year. Management's own 2030 plan ($6.5B of revenue at a 20% margin) gives about 21% a year, or about 15% with stock pay charged. Our bear case (3.5 million subscribers, today's 8% margin, a 10x multiple) gives about $7 a share, or about −29% a year, because about $2.1B of convertible debt and deferred acquisition payments sit ahead of shareholders. An 8% margin with base-case subscribers gives about −6% a year.

**Verdict: not cheap enough for the risks.** The business is real and the brand is strong. But the moat is shallow, the legal docket is crowded, and the CEO controls about 87% of the votes. Our central estimate is about −1% to +6% a year: +6% before stock pay, about −1% with stock pay charged at 4% of revenue, and about −3% with all the reviewer's fixes. In our base case the stock earns about 10% a year only below roughly $25 before stock pay, or about $18–19 after it. Those are model outputs, not price targets. The case is skewed upward: if the regulatory stream's odds (30/50/20) are borrowed as weights for our bear, base and bull cases, the result is about 8% a year, or about 1% with stock pay charged as a cost. The things that would change our mind are listed in section 8.

---

## 2. How Hims makes money, from first principles

Hims is a website and app that connects patients to doctors who can prescribe, then ships the medicine by subscription. It started with hair loss and erectile dysfunction pills. Those are cheap generic drugs that cost cents to a few dollars a month. Hims charges for the visit and the convenience, so gross margins on those lines are likely 85–90% (our estimate).

A simple way to see what changed in weight loss: Hims used to cook the dish and sell it; now it resells someone else's packaged meal and charges a delivery fee.

| Product | Who sets the drug price | Illustrative monthly price | Illustrative gross margin |
|---|---|---|---|
| Compounded semaglutide (before March 2026) | Hims (it bought the ingredient and made the vials) | about $199 | about 80% (estimate: (199 − 40) / 199) |
| Branded Wegovy injection (since March 2026) | Novo (Hims must sell at Novo's self-pay price) | $199 (first two fills, to end-2026) to $349 drug, or $249–329 on Novo's multi-month plans, + $149 membership | about 27% at $349, about 38% at $199 (estimate; assumes gross booking. If the maker's pharmacy fills the script, Hims books only its fee) |
| Branded Wegovy pill | Novo | about $149 drug + $149 membership | about 45% (estimate) |
| Hair, sexual health, skin generics | Hims | varies | about 85–90% (estimate) |

The branded figures assume Hims books the drug price as its own revenue. Hims has not said whether it does, and its purchase price from Novo is not disclosed. Retail prices come from consumer guides and conflict ($149–$299 for the pill). Treat the table as an illustration of direction, not a measurement.

The result is that **each patient who moves from compounded to branded raises revenue per subscriber but cuts the margin percentage.** That is exactly what Q2 showed. Monthly revenue per subscriber rose from $76 to $92 while gross margin fell from 76% to 64%.

---

## 3. The numbers

| Metric | Q2 2026 | Q2 2025 | FY2025 |
|---|---|---|---|
| Revenue | $753.2M (+38%) | $544.8M | $2,347.6M (+59%) |
| of which US | $621.8M (+16%) | about $537.3M | — |
| of which international | $131.4M (about $40M from one month of Eucalyptus) | $7.5M | — |
| Subscribers | 2.891M (+19%; includes Eucalyptus from June. Our estimate from Hims' $90 ex-Eucalyptus revenue per subscriber (one snippet, unverified): Eucalyptus about 0.17–0.26M (rounding range 0.12–0.35M), so organic growth about +8% to +12% (range +4% to +14%)) | 2.439M | 2.511M |
| Monthly revenue per subscriber | $92 | $76 | — |
| Gross margin | 64% | 76% | — |
| Marketing / revenue | 34.8% | 40.0% | 39.2% |
| Adjusted EBITDA (operating profit before interest, tax, depreciation and stock pay) | $60.3M (8.0%) | $82.2M (15.1%) | $318M (13.5%) |
| Net income | −$86.3M (includes a $47.5M FTC legal accrual) | $42.5M | $128M |
| Free cash flow | −$68.2M (blamed on working capital for branded drugs) | — | $57.4M |

**Guidance for 2026** has moved in opposite directions:

| Date | Revenue | Adjusted EBITDA |
|---|---|---|
| 23 Feb 2026 | $2.7–2.9B | $300–375M |
| 11 May 2026 | $2.8–3.0B | $275–350M |
| 10 Aug 2026 | $3.1–3.3B (includes Eucalyptus) | $275–325M |

At the midpoint that is about 36% revenue growth but a 9.4% margin, down from 13.5% in 2025. The **2030 target** is at least $6.5B of revenue and $1.3B of adjusted EBITDA (20%). From the 2026 midpoint, that needs about 19% revenue growth and 44% profit growth a year.

**What Hims does not disclose.** It gives no revenue by category, no split between compounded and branded weight loss, no churn rate and no cost per new customer. A 2025 guide implied weight loss was about 31% of 2025 revenue ($725M). One secondary source says GLP-1s were 24% of Q4 2025 revenue (unverified). The latest disclosed figure is over 1.6M subscribers on personalised treatments in Q4 2025, about two-thirds of subscribers (one source).

**Cost to win a customer (estimate).** Q2 marketing of $262.2M ÷ about 300,000 net new subscribers = about $874 per net add. Per gross add it is an upper bound, because net adds understate gross adds. Per organic add it is a lower bound, because the 300,000 includes Eucalyptus customers. Excluding them, marketing per organic net add is about $2,000–5,900 (estimate). At $92 a month and a 64% gross margin, $874 pays back in about 15 months; at $2,000–5,900 per organic add, payback is about 34–100 months (estimate).

---

## 4. Regulation and legal risk

**How the compounding window closed.** Pharmacies may make ("compound") copies of an approved drug only in narrow cases. One is a declared shortage. Another is a genuine per-patient change, which Hims called "personalization". FDA declared the semaglutide shortage over on 21 February 2025. Novo ended its first partnership with Hims on 23 June 2025, alleging "mass sales of compounded drugs under the false guise of personalization" (Novo's allegation; no court ruled on it). The stock fell about 30–35% that day.

**February 2026 was the turning point.**
- 5 Feb: Hims launched a compounded semaglutide pill at $49 for the first month.
- 6 Feb: FDA named Hims in a statement on restricting GLP-1 ingredients. HHS's general counsel said HHS had referred Hims to the Department of Justice. That is a referral, not a charge, and no later DOJ action was found.
- 7 Feb: Hims withdrew the pill.
- 9 Feb: Novo sued Hims for patent infringement.
- 9 Mar: settlement. Novo dropped the suit "without prejudice", so it can refile. Hims sells branded Ozempic and Wegovy (injection and pill) at Novo's self-pay prices and stopped advertising compounded versions. It keeps them only on a "limited scale". No payment terms were found.

**Lilly.** Since late April 2026, Hims doctors can reportedly prescribe Lilly's Zepbound, Mounjaro and Foundayo, filled by Lilly's own pharmacy (FierceHealthcare and a Hims news post). Hims says this "does not imply a partnership or affiliation" with Lilly. Hims prescribes; Lilly's pharmacy dispenses and sells the drug, so Hims likely earns only its membership fee on these (fee terms not disclosed). Lilly has said it has no affiliation with Hims.

**The open legal items:**

| Item | Status | Why it matters |
|---|---|---|
| FTC v. Hims (with Utah and Los Angeles County), filed 29 Jul 2026 | Allegations: sharing health data with Meta, Snap and others through tracking pixels, and charging and enrolling patients before a real consultation, with a hard-to-cancel flow. Hims disputes them | Hims accrued $47.5M in Q2 but warns the final cost could be "materially higher". A consent order could add friction to sign-up and raise churn |
| DOJ referral (Feb 2026) | No action found | Tail risk; could revive if Hims grows compounding again |
| Novo patent suit | Dismissed without prejudice | Can be refiled |
| FDA 503B proposal (30 Apr / 1 May 2026) | Proposed, not final | Would stop large-batch compounders making semaglutide, tirzepatide and liraglutide. Small direct effect: Hims says it uses only traditional 503A pharmacies (state-licensed, compounding per patient prescription; 503B "outsourcing facilities" make large batches under FDA rules) for GLP-1s |
| Securities class actions | One from 2025 (Novo relationship); one from 2026 tied to the FTC suit, lead-plaintiff deadline 2 Nov 2026 | Legal cost and distraction |
| Consumer privacy class action (Doe v. Hims) | Pending | Statutory damages risk |
| Visa monitoring | Enrolled in August 2026 over excess card disputes in weight loss (Bloomberg, 21 Aug) | Must cut disputes; a sign of billing friction |
| DEA telehealth waivers for controlled drugs | Expire 31 Dec 2026 unless extended | Matters for any true testosterone (a Schedule III controlled drug); Hims' low-T line launched with enclomiphene, which we believe is not a controlled drug (to check), and branded oral testosterone was only planned; size unknown |
| FDA rule on TV drug ads | Proposed rule targeted for Dec 2026 | Could limit Hims' heavy advertising; scope unclear |

The regulatory stream's rough odds over 12–24 months (its own estimates): bear 30%, base 50%, bull 20%. The base case is a 503B rule with little effect, an FTC settlement in 2027 that Hims can absorb, and another DEA extension.

---

## 5. Competition and moat

**The moat is shallow.** The competition stream scores each possible advantage:

| Moat source | Strength | Why |
|---|---|---|
| Brand awareness | B (real but copyable) | Super Bowl ads in 2025 and 2026; but the FTC suit and Visa monitoring erode trust |
| Customer acquisition cost | C (weak) | Marketing still about 35% of revenue; rivals bid for the same customers |
| Own pharmacies, lab, peptide plant | B | Useful for generics and labs, but branded GLP-1s cannot be made in-house |
| Personalisation and data | C | The compounded "personalised" combos drew FDA criticism and Novo's allegations; no court ruled |
| Subscription lock-in | C | The same branded drug is available elsewhere |
| Licences and drug-maker access | B | Novo access is non-exclusive and can be withdrawn |
| Many categories in one account | B | New lines (menopause, testosterone, labs) have no disclosed revenue |
| International scale | B | Zava (UK and Europe), Eucalyptus (Australia), Canada; integration risk |

**Everyone sells the same drug now.** Ro, LifeMD, WeightWatchers' clinic, Costco with Sesame, Amazon One Medical (from 21 April 2026) and the drug makers' own direct channels all sell branded GLP-1s. The makers' channels are large. About 35% of new Zepbound prescriptions went through LillyDirect in Q2 2025 (latest found; over a year old). About 39% of US injectable Wegovy prescriptions were self-pay in mid-July 2026; that figure includes telehealth sellers such as Hims, so it measures cash-pay demand, not Novo's own channel. Novo also runs its own multi-month Wegovy plans from $249 a month, and cuts US list prices by up to 50% from 1 January 2027. No source gives measured 2026 market shares for telehealth. Our earlier GLP-1 note found that drug makers keep most of the device and fill value against their suppliers. It did not study telehealth, but the channel data here point the same way.

**What has worked:** the fast switch to branded Wegovy, which brought back growth, and international expansion by acquisition. International is now about 17% of revenue.

**What has not:** the compounded strategy, which ended two Novo relationships and drew an FDA rebuke, plus FDA warning letters to Hims (September 2025) and to its 503B facility (December 2025). Margins have also fallen. New categories have no disclosed numbers.

**Governance.** CEO Andrew Dudum chairs the board. Class V shares carry 175 votes each. On proxy share counts, Class V plus his Class A shares give him about 87–88% of the votes. Outside shareholders cannot replace management. He sold heavily in 2025 under a pre-set trading plan. No open-market sale by him was found in 2026; the CFO sold small amounts under a pre-set plan in August and October 2026. The chief accounting officer leaves on 9 October 2026. Jon Franklin (ex-Rivian) was named successor on 7 October (8-K). Two directors were not renominated.

---

## 6. Balance sheet and valuation

**Capital (30 June 2026):**
- **Cash and short-term investments:** $841M.
- **0% convertible notes, $1,402.5M in total:**
  - $1.0B due May 2030, converting at about $70.67 a share.
  - $402.5M due 2032, converting at $29.53, which is about today's price. A capped call (a hedge Hims bought that pays out in shares if the stock rises) offsets dilution up to $50.15.
- **Eucalyptus deferred payments:** about $710M nominal ($683.9M fair value in the Q2 10-Q) over 18 months, plus an earn-out of up to $200M (fair value $59.6M). Deal terms (Feb 2026) said about 60% can be paid in stock; the Q2 10-Q says "a significant majority".
- **Receivables facility:** a $400M uncommitted, 364-day facility with JPMorgan, signed 1 July 2026. The drawn balance is not known until the Q3 10-Q.
- **Shares:** about 233.3M basic. The notes could add about 27.8M shares (11.9%). Eucalyptus stock payments could add up to about 18.6M at today's price (estimate).

**Market price (about 6 October 2026, snippet data):**

| Item | Value |
|---|---|
| Share price | about $29.40 |
| Market cap | about $6.86B |
| Enterprise value (EV: market cap plus debt minus cash) | about $7.42B, or about $8.13B including Eucalyptus payments; excludes any draw on the $400M receivables facility |
| EV / 2026 sales | about 2.3x |
| EV / adjusted EBITDA | about 25x 2026 (guide midpoint), about 18x 2027 (one consensus source, unverified) |
| 52-week range | $13.74 – $65.30 |
| Short interest | about 26–29% (late Jul 2026; dated); 3.2–3.7 days to cover; borrow fee about 0.3%, so the stock is easy to borrow and squeeze risk is low |
| Teladoc and LifeMD EV / sales | about 0.55x (unverified) |

Adjusted EBITDA excludes stock pay, which was 5.8% of revenue in 2025. After stock pay, 2026 EBITDA would be only about $114M (estimate); EV is about 65 times that.

**Our 2030 model.** The model builds the 2030 equity value step by step:
1. Subscribers × annual revenue per subscriber = revenue.
2. Revenue × margin = adjusted EBITDA.
3. EBITDA × exit multiple = enterprise value.
4. Subtract net debt, then divide by diluted shares.

The return compares that value with $29.40 over 4.23 years. All inputs are our assumptions. The multiple is applied to EBITDA before stock pay. The base assumes $1.2B of free cash flow from mid-2026 to 2030, about half of cumulative EBITDA, against 18% in 2025.

| Scenario | 2030 subscribers | Revenue per subscriber | EBITDA margin | Exit multiple | Value per share | Return a year |
|---|---|---|---|---|---|---|
| Bear | 3.5M | $1,000 | 8% | 10x | about $7 | −29% |
| Base | 4.5M | $1,150 | 14% | 14x | about $38 | +6% |
| Bull | 5.8M | $1,250 | 20% | 18x | about $99 | +33% |
| Management plan ($6.5B, 20%) | — | — | 20% | 14x | about $67 | +21% |

In the base case, today's price breaks even (0% a year) at about 3.4M subscribers, or at a 10.5% margin with 4.5M subscribers. A 10% annual return needs about 5.2M subscribers or a 16% margin. **The margin is the swing factor**: each 3 points of 2030 margin moves the base-case return by about 4–7 points a year, more on the downside.

The bear case is so severe because of leverage. A $2.8B enterprise value leaves little after $1.4B of converts and the Eucalyptus payments. In that case the $1B of 2030 notes would need refinancing.

**What the banks say.** No big-bank Buy rating was found. Bank of America is Neutral with a target of about $36–37 (set around July, before Q2 results; dated). Morgan Stanley is Equal Weight at $28 (11 August). Canaccord is Buy at $40 (undated, about mid-2026). The average target is about $29–31 across 13–16 analysts. No JPMorgan or Goldman rating was found. Both have a lending tie: JPMorgan arranged Hims' $400M working-capital facility and Goldman is a lender. All snippet-level.

---

## 7. Devil's-advocate review

A separate reviewer attacked this note from both sides and stress-tested the model (`raw/04-devils-advocate.md`). Its verdict: the call ("not cheap enough") is about right, but the base-case number is too generous.

**Where the base case is too generous:**
- **Stock pay.** The model values profit before stock-based pay, which was 5.8% of revenue in 2025. Charging it at 4% of revenue as a cost cuts the base from about $38 (+6% a year) to about $28 (−1%). At 5.8% it falls to about $23 (−5.5%).
- **Cash flow.** The base needs $1.2B of free cash flow from mid-2026 to 2030, about 49% of cumulative EBITDA. That compares with 18% in 2025 and negative cash flow in the first half of 2026. At $400M the base return falls to about 4.5% a year.
- **Organic growth.** Hims says revenue per subscriber would be $90 without Eucalyptus. That implies Eucalyptus brought in roughly 0.17–0.26M subscribers (0.12–0.35M allowing for rounding), so organic growth was about +8% to +12%, not +19% (estimate).
- **Missing debt.** The $400M JPMorgan receivables facility is not in the model. Fully drawn, it takes the base to about +5.5% and the bear to about −32.5% a year.
- The reviewer's fully fixed base (4% stock pay, $800M of cash flow, the 2032 capped call, Eucalyptus stock at $31 and 10M extra award shares) is about $25.60, or about −3% a year.

**Where the note is too bearish:**
- **Upside skew.** Bear $7, base $38, bull $99: the bear case loses about $22 a share (and no more than $29.40 can be lost), while the bull case gains about $69. Weighting 25/50/25 gives about $45.50, or 11% a year. Weighting by the regulatory stream's 30/50/20 odds gives about 8%. With stock pay charged in every scenario, these fall to about 4% and 1%.
- **Base revenue looks low.** The August guide implies a Q4 2026 revenue run-rate of about $3.8B. The base case's $5.18B in 2030 is only about 8% a year above that. $6.0B at a 14% margin gives about 10% a year.
- **Revenue per subscriber is rising.** Gross profit dollars grew 16% in Q2 even as the margin fell 12 points. The Q3 guide implies about $96–99 a month per subscriber (estimate), above the base case's $96.
- **Exit multiple.** A 16x multiple gives about 9.6% a year. But 14x adjusted EBITDA is already about 20–24x EBITDA after stock pay (at 4–5.8% of revenue).

**Net:** a central return is about −1% to +5% a year, below the 6% pre-stock-pay headline. "Not cheap enough for the risks" holds.

## 8. What would change the view

**Bullish signals:**
- Adjusted EBITDA margin rising back toward 14% while revenue keeps growing. Our model says this matters more than anything else.
- Organic US subscriber growth (excluding acquisitions) above 10%, with a disclosed weight-loss subscriber count.
- An FTC settlement that is cheap and does not slow sign-ups.
- A paid, formal relationship with Novo or Lilly (fees or exclusive products).

**Bearish signals:**
- Gross margin below 60%, or 2026 EBITDA at the bottom of the guide.
- Rising card disputes or churn after the billing fixes the FTC and Visa are forcing.
- Any DOJ action, a Novo refiling, or FDA action against "personalized" 503A compounding.
- A material draw on the $400M receivables facility.
- Eucalyptus instalments settled mainly in stock below $29.53, which dilutes holders.

## 9. Dated signals to watch

| Date | Event | What it tells you |
|---|---|---|
| 9 Oct 2026 | Chief accounting officer handover to Jon Franklin (named 7 Oct) | Finance-team continuity before Q3 |
| 2 Nov 2026 | Lead-plaintiff deadline, 2026 securities class action | Legal docket |
| About 9 Nov 2026 (estimate; date not yet announced) | Q3 results; guide was revenue $880–900M and adjusted EBITDA $75–95M | Whether margin is recovering; Eucalyptus payments and share issuance |
| Late 2026 (estimate) | Hims' response to the FTC complaint | Settlement path |
| Dec 2026 (agency target) | Proposed FDA rule on TV drug ads | Marketing model risk |
| 31 Dec 2026 | DEA telehealth waivers expire unless extended | Testosterone business |
| Any time | FDA final 503B decision; DOJ referral outcome; Novo refiling | Compounding tail risks |
| Feb 2027 | Super Bowl; Hims advertised in 2025 and 2026 | FDA reaction to telehealth drug ads |
| Through end-2027 | Eucalyptus deferred payments (six quarterly instalments) | Cash versus stock settlement |

## 10. Gaps

- No primary filing was read. The Q2 2026 10-Q should be checked first for debt terms, Eucalyptus accounting, diluted shares and legal accruals.
- No revenue by category, no compounded versus branded split, no churn, no cost per gross new customer.
- Whether Hims books branded drug sales gross or net, and whether Novo or Lilly pays it any fee.
- Whether the 2030 notes have a capped call (one snippet says yes, conflicting with other information).
- 2025 buybacks: $65M (10-K note) versus $90M (cash-flow statement), not reconciled.
- 2027 EPS consensus: $0.42 versus $1.11 depending on the source.
- No 2026 market-share data for GLP-1 telehealth, and no 2026 numbers for Ro.
- Short-seller reports, state corporate-practice-of-medicine rules and foreign regulators were not researched.

*This note is research for discussion, not investment advice or a recommendation to buy or sell any security. All figures come from unverified web-search snippets and our own estimates. Verify against primary filings before acting.*
