# Robot Supply Chain: 2030 Projection

*Companion to `robotics-supply-chain-moats.md`. Model date 19 September 2026, revised 22 September 2026. All numbers come from `scripts/robotics_2030_model.py`; assumptions and the full output table are in `projection-2030-model-output.md`, base financials in `raw/07-financials-2026-09-19.md`. Market caps are snippet-sourced and some are undated. This is a scenario model, not a forecast, and not investment advice.*

---

## 1. The answer first

> **Revised 22 September 2026, twice.** First, a devil's-advocate audit (`raw/08-devils-advocate-2026-09-22.md`) led to these changes:
> - One arithmetic error was fixed: grinder cost per robot is $160, not $270.
> - One market cap was brought into line with the "use the lower figure" rule (Harmonic Drive ¥548B).
> - Content pools now count only the robots whose design uses each part. Quasi-direct-drive Chinese robots such as Unitree's use no harmonic reducers or roller screws.
> - Keli's force-sensor content was cut to two sensors in 40% of Chinese robots.
> - Hesai's double-counted non-humanoid lidar was removed.
> - A 150k-unit crash case was added.
>
> Second, a QA review (`raw/09-qa-review.md`) led to these changes:
> - Lynas's market cap was re-based to A$16.5B, because the A$10.9B quote was in US dollars. This moves Lynas from -6% to -15% a year.
> - Nvidia and LG Innotek now sell only into non-Tesla Western robots.
> - Grinder demand now counts the 50% of Chinese robots that use screws or harmonics.
> - Stale first-version text in sections 4 to 6 was replaced.
>
> First-version figures are available on request.

Run the supply chain forward to 2030 on Goldman's 890k 2030 forecast (rounded to 900,000; the split of 200,000 Western and 120,000 Tesla units is our assumption). Three things fall out.

1. **Robotics becomes a material business by 2030 for only four or five of the eighteen names.** The four clear cases are Leaderdrive (59% of 2030 revenue), Wuzhou Xinchun (29%), Harmonic Drive (26%) and Keli Sensing (14%). Huachen sits right at 10% and Hengli at 8% once only the robots that use screws or harmonics are counted. For Nvidia, Lynas, MP Materials, LG Energy Solution, LG Innotek, Sanhua, Hesai and Allegro, humanoids are under 5% of 2030 revenue.
2. **No robot-exposed name offers a positive base-case return.** The only positive four-year returns are Nvidia (+20% a year, entirely a data-centre call: robots are 0.02% of its modelled revenue) and Schaeffler (+5%, an auto-margin recovery call). Hesai is roughly flat. Every pure play is negative. The reducer and screw names need 2.3M to 7.9M units in 2030 just to be fairly priced, 2.6 to 9 times Goldman's number.
3. **The "margin of safety" found in the first version disappears.** Keli moves from +5% to -5% a year once its force-sensor content is limited to what a Chinese robot's sensor budget can hold. It now needs 2.6M units to break even. Hesai needs 0.8M, but its market cap is undated and probably stale (section 7). There is no listed name that is cheap relative to a 900k-unit 2030.

The rare-earth names are a different animal. Humanoids alone do not move Lynas or MP by 2030. 200,000 Western robots need about 21 tonnes of Dy/Tb, less than one year of Lynas output. Their case rests on the ex-China price regime, which is a live bargaining chip at the 23 to 25 September 2026 Trump-Xi summit and the 10 November 2026 deadline.

## 2. How the model works (first principles)

A supplier's 2030 robotics revenue is the product of four things:
- how many robots are built;
- how many of them its customers build;
- how many dollars of its part each robot carries at 2030 prices;
- its share of that content.

Add the non-robot business grown at a conservative rate, apply a margin, apply an exit multiple, and compare with today's market cap. The compounding rate that reconciles the two is the implied annual return.

Four unit scenarios:

| Scenario | 2030 humanoids | of which Western OEMs | of which Tesla |
|---|---|---|---|
| Crash (added after audit) | 150k | 30k | 15k |
| Bear | 300k | 60k | 30k |
| Base | 900k | 200k | 120k |
| Bull | 2.5M | 600k | 400k |

The base case is Goldman's 890k, rounded. The bear case (300k) is below Morgan Stanley's China-only 446k. Morgan Stanley plus a slow West would sit between bear and base. The bull case assumes the Chinese cost curve (Unitree G1 at a $6k BOM) opens consumer and light-commercial demand. Tesla at 120k units in the base case is far below Musk's stated 1M-a-year Fremont capacity. It is far above the "low thousands" that secondary sources expect in 2026.

Content prices are the 2030 cost-down prices, not today's:

| Part | 2030 price in the model | Price today |
|---|---|---|
| Roller screws (Chinese chain) | $150 | $1,350 to $2,700 |
| Harmonic reducers, Chinese | $85 | CNY 573 to 1,100, about $80 to $155 |
| Harmonic reducers, premium | $180 | $800 to $1,500 (high-end quotes) |
| Six-axis force sensors | $420 | CNY 32k, about $4,500, in 2022 |

This matters because the volume story and the price-deflation story fight each other. A supplier that keeps unit share can still see revenue per robot fall 80% over the period. Chinese harmonics are the exception: they are already close to the model's 2030 price.

---

## 3. The 2030 table (base case, corrected)

| Company | Market cap $M | 2030 revenue $M | Robot revenue $M | Robot share | 2030 net income $M | Today's price / 2030 earnings | Implied CAGR base | crash | bear | bull |
|---|---|---|---|---|---|---|---|---|---|---|
| Nvidia | 5,310,000 | 744,538 | 136 | 0% | 409,496 | 13x | +20% | +20% | +20% | +20% |
| Schaeffler | 7,513 | 29,806 | 250 | 1% | 912 | 8x | +5% | +4% | +4% | +6% |
| Hesai | 2,920 | 1,022 | 29 | 3% | 133 | 22x | 0% | -1% | 0% | +1% |
| Tuopu | 14,000 | 6,461 | 252 | 4% | 651 | 21x | -2% | -3% | -3% | +1% |
| Keli Sensing | 2,800 | 412 | 59 | 14% | 89 | 31x | -5% | -8% | -7% | -1% |
| MP Materials | 9,730 | 1,354 | 34 | 2% | 273 | 36x | -8% | -9% | -9% | -7% |
| Nabtesco | 4,097 | 2,578 | 90 | 3% | 160 | 26x | -8% | -9% | -9% | -5% |
| Hengli Hydraulic | 18,589 | 2,474 | 197 | 8% | 540 | 34x | -10% | -11% | -11% | -7% |
| Sanhua | 27,656 | 6,514 | 252 | 4% | 844 | 33x | -11% | -12% | -12% | -9% |
| Harmonic Drive Systems | 3,726 | 876 | 227 | 26% | 86 | 43x | -12% | -20% | -19% | +1% |
| LG Innotek | 8,877 | 18,592 | 10 | 0% | 465 | 19x | -14% | -14% | -14% | -14% |
| Lynas | 10,890 | 990 | 22 | 2% | 250 | 44x | -15% | -15% | -15% | -14% |
| Wuzhou Xinchun | 1,998 | 747 | 216 | 29% | 48 | 41x | -16% | -32% | -28% | +5% |
| Huachen Precision | 896 | 132 | 13 | 10% | 16 | 55x | -17% | -19% | -19% | -13% |
| Allegro | 10,980 | 1,361 | 27 | 2% | 192 | 57x | -18% | -18% | -18% | -17% |
| Leaderdrive | 7,459 | 353 | 208 | 59% | 96 | 78x | -20% | -32% | -29% | -5% |
| Qinchuan Machine Tool | 1,280 | 735 | 13 | 2% | 23 | 55x | -21% | -22% | -22% | -19% |
| LG Energy Solution | 69,094 | 23,989 | 25 | 0% | 960 | 72x | -31% | -31% | -31% | -31% |

Read the "today's price / 2030 earnings" column as the multiple you pay now for what the company earns four years out. Anything above about 25x needs either a higher exit multiple than the model gives it or a bull-case volume to work.

**How many robots does each name need?** The table gives the volume at which today's price is fair (0% return) and the volume for a 10% annual return:

| Company | Units for 0% | Units for +10% |
|---|---|---|
| Hesai | 0.8M | 14.3M |
| Wuzhou Xinchun | 2.3M | 3.7M |
| Tuopu | 2.4M | 12.8M |
| Harmonic Drive Systems | 2.6M | 4.5M |
| Keli Sensing | 2.6M | 6.9M |
| Leaderdrive | 3.3M | 5.2M |
| Nabtesco | 6.5M | 16.0M |
| Hengli Hydraulic | 7.9M | 17.5M |
| Huachen Precision | 9.8M | 17.9M |
| MP Materials | 13.4M (robots alone cannot carry the price) | never below 20M |
| Sanhua | 16.9M | never below 20M |
| Lynas, Qinchuan, LG Innotek, LG Energy Solution, Allegro | never below 20M | never below 20M |
| Nvidia, Schaeffler | fair on the base business alone | Nvidia fair on its base business; Schaeffler needs 8.6M |

Goldman's 2035 number is 6.5M. Every robot pure play is priced today for a 2030 volume that Goldman does not expect until the early-to-mid 2030s, if at all.

**Further downside the corrected model still does not include.** These come from the audit and were not adopted as base assumptions because they are judgement calls:
- Component prices are held fixed across scenarios, even though overcapacity should push them lower in the bear case.
- Exit multiples are 25 to 30x for parts the moat map itself rates as commoditising. Halving them takes Leaderdrive's bear case to about -40% a year.
- Leaderdrive's 28% robot net margin at an $85 selling price is contradicted by its loss-making peer Laifual. At 17% and 20x, Leaderdrive's base case is about -32%.
- Schaeffler's 2030 margin is 3%. At 2% it turns to about -5%.
- No share dilution is modelled.

## 4. What each business looks like in 2030

**Lynas.** About A$1.5B (US$1.0B) of 2030 revenue. The heavy-rare-earth share is an analyst assumption. Lynas stays the only ex-China Dy/Tb source at scale unless Energy Fuels' White Mesa circuits (2027) and Iluka's Eneabba refinery ramp. Robots are a rounding error in its volumes. After the currency fix, the stock trades at 44x the model's 2030 earnings. It is a bet on the two-tier price regime surviving, and even that bet needs a higher margin than the model's 25%. If China lifts the April 2025 licences, the premium collapses and 25% is too high. If China tightens, the model is too low.

**MP Materials.** The 10X plant is planned at 10,000 tonnes a year of magnets, with the DoD taking output under the ten-year floor. Revenue reaches around $1.3B to $1.5B and the company returns to profit (it last earned a profit in 2022, by reviewer knowledge; not in the raw files). It looks like a defence-adjacent utility with a guaranteed price. Robots are a small share of ex-China magnet demand, about 700 tonnes at 200k Western units. MP sells whatever it makes regardless.

**Nvidia.** Jetson Thor's successor is standard on most non-Tesla Western humanoids (Figure, Agility, Boston Dynamics, 1X). Tesla uses its own AI5. Nvidia says its physical-AI run-rate is about $10B today, per a secondary source. That run-rate plausibly reaches $30B to $50B including simulation, training and cloud. That is 4 to 7% of a $745B-revenue company. Nvidia is the strongest moat in the chain and the stock least sensitive to it.

**Hengli Hydraulic.** It is the largest roller-screw maker in China, with 3.4M sets of capacity, selling into Tesla and the domestic chain at prices one-tenth of 2025's. Screw revenue is around CNY 1.4B on a CNY 18B company (8%): material, not transformative. Price deflation eats most of the volume growth. At 34x 2030 earnings, even the bull case (-7% a year) does not justify today's price.

**Wuzhou Xinchun and Tuopu and Sanhua.** All three depend on one customer building 120,000 robots a year in the base case. Tuopu and Sanhua are large auto suppliers where the robot line is 4% of revenue, so a Tesla slip hurts sentiment more than earnings. Wuzhou is the leveraged version: 29% of revenue and a 41x multiple on 2030 earnings.

**Schaeffler.** Ewellix and the reported new strain-wave process (single blog source) give it a few hundred million euros of actuator revenue. That is consistent with management's target of a three-digit-million-euro humanoid order book by 2030, which assumes at least 1M industry units. The investment case is the group margin recovering from a trailing loss to 3%, which the consensus EPS of EUR 0.88 already assumes. Robots are free.

**Harmonic Drive Systems.** It is stuck between two forces. Its premium tier keeps roughly 45% of Western humanoid harmonics, but at prices roughly 80% below today's premium quotes ($180 vs $800 to $1,500). Schaeffler's 2027 process and Chinese entrants cap the volume. Revenue is about ¥129B, with a single-digit earnings margin. The 43x multiple on 2030 earnings is demanding, but below Leaderdrive, Huachen, Qinchuan and Allegro.

**Leaderdrive.** It is the biggest transformation: from a CNY 571M company to a CNY 2.5B one, with harmonics at about CNY 600 apiece and 50% of the Chinese chain. Even on the base case, the 2030 value is about 40% of today's market cap. If the Laifual price war halves robot margin, it is about a quarter. The model gives Leaderdrive no Tesla volume; reported Optimus supply (unverified) would be upside. This is the highest-beta name in the set on both sides.

**Keli Sensing.** The first version put four six-axis sensors in every Chinese robot. That alone exceeded the whole sensor budget of a $10k robot. Corrected to two wrist sensors in the 40% of Chinese robots that carry them, robots are 14% of Keli's 2030 revenue. The stock is 31x 2030 earnings and needs 2.6M units to be fair. It is no longer a margin-of-safety name.

**Hesai.** Its revenue reaches about $1.0B by 2030. Humanoids are about 3% of that. All robotics lidar (quadrupeds, mowers, AMRs) is perhaps 10%, by our estimate, and sits inside the base growth rate. The model's 18% base growth is below the 2027 consensus path. The market already prices the robot line cheaply because it is bundled with automotive lidar. The verdict rests on an undated market cap (section 7).

**Nabtesco, LG Innotek, LG Energy Solution, Allegro, Sanhua.** Humanoids stay under 5% of revenue in the base case, and under 12% even in the bull case. Own them for their core businesses or not at all. The robot narrative adds nothing to the 2030 earnings that the market is not already paying a full price for.

**Huachen and Qinchuan.** The grinder pool is real but small: about $88M a year of grinder capex at 900k robots. That counts only Western robots and the half of Chinese robots that use screws or harmonics. The Chinese makers' share of the sub-5-micron tier is unproven. They are option tickets, not investments, at 55x 2030 earnings each.

---

## 5. Sensitivities that matter most

| Assumption | Base value | What changes if it moves |
|---|---|---|
| 2030 unit volume | 900k | Each doubling adds about 9 to 11 points of CAGR to Wuzhou and Leaderdrive, about 7 to Harmonic Drive, about 3 to Keli and Huachen, and under 2 to everyone else |
| 2030 component prices | Screws $150, harmonics $85 to $180, F/T $420 | If deflation is slower (prices 2x the model), Leaderdrive improves to about -11% and Keli to about -2%; Harmonic Drive and Wuzhou to about -5%. None turns positive. If faster, all fall further |
| Tesla 2030 volume | 120k | At 30k units Tuopu and Sanhua robot revenue falls to 1% of sales; at 400k it reaches 12%, still not a re-rating driver for auto-parts multiples |
| Exit multiples | 10x to 30x | For names at 20x to 30x, 5 more turns of exit multiple are worth about 3 to 5 points of CAGR. For the 10x names (Schaeffler, LG Innotek), 5 turns are worth about 9 to 11 points |
| Ex-China Dy/Tb premium | $1,500/kg blended | Irrelevant to robot volumes but central to the Lynas case; a return to China parity ($220/kg) cuts Lynas's heavy-rare-earth revenue by 85% |

---

## 6. What to do with this

These verdicts match section 9 of the moat map.

- **Keep the heavy-rare-earth and Nvidia moats. Downgrade the rest.** Roller screws, grinders and harmonics (moat map sections 4.2 and 4.3) are capacity moats being competed away. The corrected 2030 model says scarcity is priced in for every robot pure play. None offers a margin of safety at 900k units.
- **Own Nvidia and Schaeffler only for reasons other than robots.** Treat the robot line as a free option.
- **Treat Lynas as a policy trade.** Its next binary dates are the 24 September summit and 10 November 2026. It is not a robot-volume play, and after the currency fix it is not cheap even on the base business.
- **Put Tuopu, Hengli, Nabtesco and Keli on a watchlist for a big drawdown.** Leaderdrive needs 3.3M units to be fair, 3.7 times Goldman's 2030 number. Along with Harmonic Drive, Wuzhou, Sanhua, MP, Huachen, Qinchuan, LG Innotek, LG Energy Solution and Allegro, the review rates it "avoid as a robotics play".
- **Re-run the model on 30 September 2026** (Micron results as a memory read-through), after Tesla's audit outcome, and after Unitree's first-half results. Change only the unit and price cells, and re-source the Hesai market cap first.

## 7. Limits of this model

- **Market caps conflict between sources.** Caps for Hengli, Keli, MP and Qinchuan differ by 10 to 40%. The lower figure was used, with three exceptions:
  - Keli is CNY 20.0B, between CNY 18.8B and 22.5B.
  - Leaderdrive is CNY 53.3B, the latest dated figure; raw/01 shows 51.3B, which would give about -19% and 3.1M units to break even.
  - Lynas is US$10.9B (stockanalysis, about A$16.5B at the model's 0.66 rate), consistent with A$15.54 × 1.01B shares. The earlier A$10.9B tag was a currency error.
- **Hesai's cap is undated and likely stale.** The Hesai figure of $2.92B must be re-checked against a dated cap before the verdict is used. A cap 1.5 times higher gives about -9%.
- **Several inputs are stale or undated.** The Sanhua and LG Energy Solution caps date from March and April 2026. All caps pre-date the 20 September 2026 reports that China is slowing humanoid IPOs.
- **Some profit inputs are inferred or assumed.** Leaderdrive's FY2025 net income is inferred from its price/earnings ratio. Base-business 2030 income is an assumed margin on grown revenue and is not linked to current profits.
- **Compounding is uniform.** All bases are compounded 4.25 years, whether they are FY2025 actuals or FY2026/27 forecasts. That is worth about ±1 point of CAGR.
- **FX rates are assumed, not sourced.** CAGRs do not depend on them; robot share of revenue does.
- **Nvidia is a data-centre call.** Its 2030 net income assumes 15% growth on FY27 consensus and a 55% margin, which is not part of this analysis.
- **Growth rates for Asian names are ours.** No sell-side 2027 consensus was available for most of them, so base-business growth rates are the analyst's.
- **Unit splits and prices are assumptions.** The Western and Tesla unit splits are ours. Component price paths are the single largest source of error and are stated in section 2 so they can be changed.
