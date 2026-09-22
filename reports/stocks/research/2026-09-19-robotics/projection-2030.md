# Robot Supply Chain: 2030 Projection

*Companion to `robotics-supply-chain-moats.md`. Model date 19 September 2026. All numbers come from `scripts/robotics_2030_model.py`; assumptions and the full output table are in `projection-2030-model-output.md`, base financials in `raw/07-financials-2026-09-19.md`. Market caps are snippet-sourced and some are undated. This is a scenario model, not a forecast, and not investment advice.*

---

## 1. The answer first

> **Revised 22 September 2026** after a devil's-advocate audit of the model (`raw/08-devils-advocate-2026-09-22.md`). One arithmetic error was fixed (grinder cost per robot is $160, not $270), one market cap was brought into line with the "use the lower figure" rule (Harmonic Drive ¥548B), content pools now count only the robots whose design actually uses each part (quasi-direct-drive Chinese robots such as Unitree's use no harmonic reducers or roller screws), Keli's force-sensor content was cut to two sensors in 40% of Chinese robots, Hesai's double-counted non-humanoid lidar was removed, and a 150k-unit crash case was added. The conclusions below reflect the corrected model; the first version's numbers are in git history.

Run the supply chain forward to 2030 on Goldman's base case of about 900,000 humanoids a year (200,000 of them from Western OEMs, 120,000 from Tesla) and three things fall out.

1. **Robotics becomes a material business by 2030 for only four of the eighteen names.** Leaderdrive (59% of 2030 revenue), Wuzhou Xinchun (29%), Harmonic Drive (26%) and Keli Sensing (14%). Hengli (8%) and Huachen (7%) drop below 10% once only the robots that use roller screws are counted. For Nvidia, Lynas, MP Materials, LG Energy Solution, LG Innotek, Sanhua, Hesai and Allegro, humanoids are under 5% of 2030 revenue.
2. **No robot-exposed name offers a positive base-case return.** The only positive four-year returns are Nvidia (+20% a year, entirely a data-centre call: robots are 0.05% of its modelled revenue) and Schaeffler (+5%, an auto-margin recovery call). Hesai is roughly flat. Every pure play is negative, and the reducer and screw names need 2.3M to 7.9M units in 2030 just to be fairly priced, three to nine times Goldman's number.
3. **The "margin of safety" found in the first version disappears.** Keli moves from +5% to -5% a year once its force-sensor content is limited to what a Chinese robot's sensor budget can hold, and it now needs 2.6M units to break even. Hesai needs 0.8M. There is no listed name that is cheap relative to a 900k-unit 2030.

The rare-earth names are a different animal. Humanoids alone do not move Lynas or MP by 2030 (200,000 Western robots need about 21 tonnes of Dy/Tb, less than one year of Lynas output). Their case rests on the ex-China price regime, which is a live bargaining chip at the 23 to 25 September 2026 Trump-Xi summit and the 10 November 2026 deadline.

## 2. How the model works (first principles)

A supplier's 2030 robotics revenue is the product of four things: how many robots are built, how many of them its customers build, how many dollars of its part each robot carries at 2030 prices, and its share of that content. Add the non-robot business grown at a conservative rate, apply a margin, apply an exit multiple, and compare with today's market cap. The compounding rate that reconciles the two is the implied annual return.

Three unit scenarios:

| Scenario | 2030 humanoids | of which Western OEMs | of which Tesla | Broader embodied multiplier (lidar, compute) |
|---|---|---|---|---|
| Crash (added after audit) | 150k | 30k | 15k | 3x |
| Bear | 300k | 60k | 30k | 3x |
| Base | 900k | 200k | 120k | 3x |
| Bull | 2.5M | 600k | 400k | 3.5x |

Base is Goldman's September 2026 number (890k). Bear is roughly where Morgan Stanley's China-only 446k plus a slow West lands. Bull assumes the Chinese cost curve (Unitree G1 at a $6k BOM) opens consumer and light-commercial demand. Tesla at 120k units in the base case is far below Musk's stated 1M-a-year Fremont capacity and far above the "low thousands" secondary sources expect in 2026.

Content prices are the 2030 cost-down prices, not today's: roller screws at $150 in the Chinese chain (from $1,350 to $2,700 today), harmonic reducers at $85 Chinese and $180 premium (from $800 to $1,500), six-axis force sensors at $420 (from about $4,500). This matters because the volume story and the price-deflation story fight each other. A supplier that keeps unit share can still see revenue per robot fall 80% over the period.

---

## 3. The 2030 table (base case, corrected)

| Company | Market cap $M | 2030 revenue $M | Robot revenue $M | Robot share | 2030 net income $M | Today's price / 2030 earnings | Implied CAGR base | crash | bear | bull |
|---|---|---|---|---|---|---|---|---|---|---|
| Nvidia | 5,310,000 | 744,742 | 340 | 0% | 409,608 | 13x | +20% | +20% | +20% | +20% |
| Schaeffler | 7,513 | 29,806 | 250 | 1% | 912 | 8x | +5% | +4% | +4% | +6% |
| Hesai | 2,920 | 1,022 | 29 | 3% | 133 | 22x | 0% | -1% | 0% | +1% |
| Tuopu | 14,000 | 6,461 | 252 | 4% | 651 | 21x | -2% | -3% | -3% | +1% |
| Keli Sensing | 2,800 | 412 | 59 | 14% | 89 | 31x | -5% | -8% | -7% | -1% |
| Lynas | 7,194 | 990 | 22 | 2% | 250 | 29x | -6% | -7% | -7% | -5% |
| MP Materials | 9,730 | 1,354 | 34 | 2% | 273 | 36x | -8% | -9% | -9% | -7% |
| Nabtesco | 4,097 | 2,578 | 90 | 3% | 160 | 26x | -8% | -9% | -9% | -5% |
| Hengli Hydraulic | 18,589 | 2,474 | 197 | 8% | 540 | 34x | -10% | -11% | -11% | -7% |
| Sanhua | 27,656 | 6,514 | 252 | 4% | 844 | 33x | -11% | -12% | -12% | -9% |
| Harmonic Drive Systems | 3,726 | 876 | 227 | 26% | 86 | 43x | -12% | -20% | -19% | +1% |
| LG Innotek | 8,877 | 18,606 | 24 | 0% | 466 | 19x | -14% | -14% | -14% | -14% |
| Wuzhou Xinchun | 1,998 | 747 | 216 | 29% | 48 | 41x | -16% | -32% | -28% | +5% |
| Huachen Precision | 896 | 128 | 9 | 7% | 16 | 57x | -18% | -19% | -19% | -15% |
| Allegro | 10,980 | 1,361 | 27 | 2% | 192 | 57x | -18% | -18% | -18% | -17% |
| Leaderdrive | 7,459 | 353 | 208 | 59% | 96 | 78x | -20% | -32% | -29% | -5% |
| Qinchuan Machine Tool | 1,280 | 731 | 9 | 1% | 23 | 56x | -22% | -22% | -22% | -20% |
| LG Energy Solution | 69,094 | 23,989 | 25 | 0% | 960 | 72x | -31% | -31% | -31% | -31% |

Read the "today's price / 2030 earnings" column as the multiple you pay now for what the company earns four years out. Anything above about 25x needs either a higher exit multiple than the model gives it or a bull-case volume to work.

**How many robots does each name need?** The volume at which today's price is fair (0% return) and the volume for a 10% annual return:

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
| Lynas, MP Materials | about 10M to 13M (robots alone cannot carry the price) | never |
| Huachen Precision | 14.4M | never below 20M |
| Sanhua, Qinchuan, LG Innotek, LG Energy Solution, Allegro | never below 20M | never |
| Nvidia, Schaeffler | fair on the base business alone | Schaeffler needs 8.6M |

Goldman's 2035 number is 6.5M. Every robot pure play is priced today for a 2030 volume the most bullish Street house does not expect until the early-to-mid 2030s, if at all.

**Further downside the corrected model still does not include** (from the audit, not adopted as base assumptions because they are judgement calls): component prices held fixed across scenarios even though overcapacity should push them lower in the bear case; exit multiples of 25 to 30x for parts the moat map itself rates as commoditising (halving them takes Leaderdrive's bear case to about -35% a year); Leaderdrive's 28% robot net margin at an $85 selling price, which its loss-making peer Laifual contradicts (at 17% and 20x, Leaderdrive's base case is about -35%); Schaeffler's 3% 2030 margin (at 2% it turns to about -5%); and no share dilution.

## 4. What each business looks like in 2030

**Lynas.** About A$1B of revenue with 20 to 30% of it from heavy rare earths, still the only ex-China Dy/Tb source at scale unless Energy Fuels' White Mesa circuits (2027) and Iluka's Eneabba refinery ramp. Robots are a rounding error in its volumes. The stock is a bet on the two-tier price regime surviving. If China lifts the April 2025 licences, the premium collapses and the model's 25% margin is too high. If it tightens, the model is too low.

**MP Materials.** The 10X plant is running at 10,000 tonnes a year of magnets with the DoD taking output under the ten-year floor. Revenue around $1.3B to $1.5B, profitable for the first time. It looks like a defence-adjacent utility with a guaranteed price. Robots take perhaps 30% of ex-China magnet demand by then, but MP sells whatever it makes regardless.

**Nvidia.** Jetson Thor's successor sits in most Western humanoids, and Nvidia's physical-AI run-rate (about $10B today by its own account) plausibly reaches $30B to $50B including simulation, training and cloud. That is 4 to 7% of a $740B company. Nvidia is the strongest moat in the chain and the least sensitive stock to it.

**Hengli Hydraulic.** The largest roller-screw maker in China with 3M sets of capacity, selling into Tesla and the domestic chain at prices one-tenth of 2025's. Screw revenue around CNY 3.4B on a CNY 20B company: material, not transformative. Price deflation eats most of the volume growth. At 31x 2030 earnings today, the stock needs the bull case.

**Wuzhou Xinchun and Tuopu and Sanhua.** All three depend on one customer building 120,000 robots a year in the base case. Tuopu and Sanhua are large auto suppliers where the robot line is 4% of revenue, so a Tesla slip hurts sentiment more than earnings. Wuzhou is the leveraged version: 29% of revenue and a 41x multiple on 2030 earnings.

**Schaeffler.** Ewellix and the new strain-wave process give it a few hundred million euros of actuator revenue, exactly the "three-digit millions" management has guided. The investment case is the group margin recovering from zero to 3%, which the consensus EPS of EUR 0.88 already assumes. Robots are free.

**Harmonic Drive Systems.** Stuck between two forces: its premium tier keeps roughly 45% of Western humanoid harmonics, but at prices 40% below today's, and Schaeffler's 2027 process plus Chinese entrants cap the volume. Revenue about ¥130B, earnings margin single digit. The 52x multiple on 2030 earnings is the most demanding in the set outside the battery names.

**Leaderdrive.** The biggest transformation: from a CNY 571M company to a CNY 4B one, with harmonics at CNY 600 apiece and 50% of the Chinese chain. Net margin holds at 28% only if the Laifual price war ends; if it does not, margin halves and the stock is worth a third of today. This is the highest-beta name in the set on both sides.

**Keli Sensing.** The first version put four six-axis sensors in every Chinese robot, which alone exceeded the whole sensor budget of a $10k robot. Corrected to two wrist sensors in the 40% of Chinese robots that carry them, robots are 14% of Keli's 2030 revenue, the stock is 31x 2030 earnings and it needs 2.6M units to be fair. It is no longer a margin-of-safety name.

**Hesai.** Robotics lidar is about 10% of a $1.1B revenue base by 2030, sold into several million quadrupeds, mowers, AMRs and humanoids. The model's 18% base growth is below the 2027 consensus path. It is the one name where the market already prices the robot line cheaply because it is bundled with automotive lidar.

**Nabtesco, LG Innotek, LG Energy Solution, Allegro, Sanhua.** Humanoids stay under 5% of revenue in every scenario. Own them for their core businesses or not at all; the robot narrative adds nothing to the 2030 earnings that the market is not already paying a full price for.

**Huachen and Qinchuan.** The grinder pool is real (about $240M a year of precision-grinder capex at 900k robots) but small, and the Chinese makers' share of the sub-5-micron tier is unproven. They are option tickets, not investments, at 45x and 49x 2030 earnings.

---

## 5. Sensitivities that matter most

| Assumption | Base value | What changes if it moves |
|---|---|---|
| 2030 unit volume | 900k | Each doubling adds roughly 8 to 12 points of CAGR to Leaderdrive, Keli, Wuzhou and Harmonic Drive, and under 2 points to everyone else |
| 2030 component prices | Screws $150, harmonics $85 to $180, F/T $420 | If deflation is slower (prices 2x the model), Leaderdrive and Keli move to +15% and +18% base-case CAGR; if faster, both go negative |
| Tesla 2030 volume | 120k | At 30k units Tuopu and Sanhua robot revenue falls to 1% of sales; at 400k it reaches 12%, still not a re-rating driver for auto-parts multiples |
| Exit multiples | 20x to 30x | Every 5 turns of exit multiple is worth about 5 points of CAGR over four years; the model already gives the pure plays 25x to 30x |
| Ex-China Dy/Tb premium | $1,500/kg blended | Irrelevant to robot volumes but the whole Lynas case; a return to China parity ($220/kg) cuts Lynas's heavy-rare-earth revenue by 85% |

---

## 6. What to do with this

- **Keep the moat ranking, change the sizing.** The moat map correctly identified where scarcity sits. The corrected 2030 model says scarcity is priced in for every robot pure play; none offers a margin of safety at 900k units.
- **Own Nvidia and Schaeffler for reasons other than robots** and treat the robot line as a free option.
- **Treat Lynas and MP as a policy trade** with 10 November 2026 as the next binary date, not as robot-volume plays.
- **Trade the reducer and screw names on drawdowns only.** Leaderdrive needs 1.6M units to be fair; buy it when a Tesla slip or a price-war headline takes 30 to 40% off, as happened on 27 May 2026, and sell it into audit-and-order headlines.
- **Re-run the model on 30 September 2026** (Micron results as a memory read-through), after Tesla's audit outcome, and after Unitree's first-half results, changing only the unit and price cells.

## 7. Limits of this model

Market caps for Hengli, Keli, MP and Qinchuan differ between sources by 10 to 40%; the lower figure was used, except Keli (CNY 20.0B, midpoint of CNY 18.8B to 22.5B) and Lynas (A\$10.9B, the only dated figure; an unconfirmed estimate of A\$14 to 15B would take its base case to about -14%). All caps pre-date the 20 September 2026 reports of a Chinese humanoid IPO freeze. Leaderdrive's FY2025 net income is inferred from its price/earnings ratio. Nvidia's 2030 net income assumes 15% growth on FY27 consensus and a 55% margin, which is a data-centre call and not part of this analysis. No sell-side 2027 consensus was available for most Asian names, so base-business growth rates are the analyst's. Component price paths are the single largest source of error and are stated in section 2 so they can be changed.
