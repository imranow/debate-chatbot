# Robot Supply Chain: 2030 Projection

*Companion to `robotics-supply-chain-moats.md`. Model date 19 September 2026. All numbers come from `scripts/robotics_2030_model.py`; assumptions and the full output table are in `projection-2030-model-output.md`, base financials in `raw/07-financials-2026-09-19.md`. Market caps are snippet-sourced and some are undated. This is a scenario model, not a forecast, and not investment advice.*

---

## 1. The answer first

Run the supply chain forward to 2030 on Goldman's base case of about 900,000 humanoids a year (200,000 of them from Western OEMs, 120,000 from Tesla) and three things fall out.

1. **Robotics becomes a material business by 2030 for only six of the eighteen names.** Leaderdrive (74% of 2030 revenue), Keli Sensing (45%), Wuzhou Xinchun (29%), Harmonic Drive (26%), Huachen (23%) and Hengli (17%). For everyone else, including Nvidia, Lynas, MP Materials, LG Energy Solution, LG Innotek, Sanhua and Allegro, humanoids are under 5% of 2030 revenue. Their share prices will be set by their core businesses, not by robots.
2. **Even where robotics is material, today's price already discounts it.** On the base case, the model gives a positive four-year return only for Nvidia (+20%, driven by its data-centre business, not robots), Schaeffler (+5%), Keli (+5%) and Hesai (+2%). The pure-play reducer and screw names (Leaderdrive, Harmonic Drive, Wuzhou, Hengli) show negative base-case returns and need 1.6M to 3.3M units in 2030, roughly two to four times Goldman's number, just to be fairly priced today.
3. **The cheapest exposure to the robot volume story is where the market cap is small relative to the 2030 profit pool: Keli and Hesai.** Keli is fairly priced at 0.5M units and returns 10% a year at 1.4M. Hesai is fair at 0.2M humanoids because its lidar sells into quadrupeds and service robots too. Those are the only two names in the set with a margin of safety under the base case.

The rare-earth names are a different animal. Humanoids alone do not move Lynas or MP by 2030 (200,000 Western robots need about 21 tonnes of Dy/Tb, less than one year of Lynas output). Their case rests on the ex-China price regime, EV and defence demand and policy, not on robot volumes. Hold them for that reason or not at all.

---

## 2. How the model works (first principles)

A supplier's 2030 robotics revenue is the product of four things: how many robots are built, how many of them its customers build, how many dollars of its part each robot carries at 2030 prices, and its share of that content. Add the non-robot business grown at a conservative rate, apply a margin, apply an exit multiple, and compare with today's market cap. The compounding rate that reconciles the two is the implied annual return.

Three unit scenarios:

| Scenario | 2030 humanoids | of which Western OEMs | of which Tesla | Broader embodied multiplier (lidar, compute) |
|---|---|---|---|---|
| Bear | 300k | 60k | 30k | 3x |
| Base | 900k | 200k | 120k | 3x |
| Bull | 2.5M | 600k | 400k | 3.5x |

Base is Goldman's September 2026 number (890k). Bear is roughly where Morgan Stanley's China-only 446k plus a slow West lands. Bull assumes the Chinese cost curve (Unitree G1 at a $6k BOM) opens consumer and light-commercial demand. Tesla at 120k units in the base case is far below Musk's stated 1M-a-year Fremont capacity and far above the "low thousands" secondary sources expect in 2026.

Content prices are the 2030 cost-down prices, not today's: roller screws at $150 in the Chinese chain (from $1,350 to $2,700 today), harmonic reducers at $85 Chinese and $180 premium (from $800 to $1,500), six-axis force sensors at $420 (from about $4,500). This matters because the volume story and the price-deflation story fight each other. A supplier that keeps unit share can still see revenue per robot fall 80% over the period.

---

## 3. The 2030 table (base case)

| Company | Market cap $M | 2030 revenue $M | Robot revenue $M | Robot share | 2030 net income $M | Today's price / 2030 earnings | Implied CAGR base | bear | bull |
|---|---|---|---|---|---|---|---|---|---|
| Nvidia | 5,310,000 | 744,742 | 340 | 0% | 409,608 | 13x | +20% | +20% | +20% |
| Schaeffler | 7,513 | 29,806 | 250 | 1% | 912 | 8x | +5% | +4% | +6% |
| Keli Sensing | 2,800 | 647 | 294 | 45% | 136 | 21x | +5% | -3% | +19% |
| Hesai | 2,920 | 1,106 | 113 | 10% | 146 | 20x | +2% | 0% | +8% |
| Tuopu | 14,000 | 6,461 | 252 | 4% | 651 | 21x | -2% | -3% | +1% |
| Lynas | 7,194 | 990 | 22 | 2% | 250 | 29x | -6% | -7% | -5% |
| Hengli Hydraulic | 18,589 | 2,750 | 472 | 17% | 596 | 31x | -8% | -10% | -2% |
| MP Materials | 9,730 | 1,354 | 34 | 2% | 273 | 36x | -8% | -9% | -7% |
| Nabtesco | 4,097 | 2,578 | 90 | 3% | 160 | 26x | -8% | -9% | -5% |
| Sanhua | 27,656 | 6,514 | 252 | 4% | 844 | 33x | -11% | -12% | -9% |
| Leaderdrive | 7,459 | 561 | 416 | 74% | 154 | 48x | -11% | -24% | +9% |
| Huachen Precision | 896 | 155 | 36 | 23% | 20 | 45x | -13% | -17% | -5% |
| LG Innotek | 8,877 | 18,606 | 24 | 0% | 466 | 19x | -14% | -14% | -14% |
| Harmonic Drive Systems | 4,429 | 876 | 227 | 26% | 86 | 52x | -16% | -22% | -3% |
| Wuzhou Xinchun | 1,998 | 747 | 216 | 29% | 48 | 41x | -16% | -28% | +5% |
| Allegro | 10,980 | 1,361 | 27 | 2% | 192 | 57x | -18% | -18% | -17% |
| Qinchuan Machine Tool | 1,280 | 758 | 36 | 5% | 26 | 49x | -19% | -21% | -14% |
| LG Energy Solution | 69,094 | 23,989 | 25 | 0% | 960 | 72x | -31% | -31% | -31% |

Read the "today's price / 2030 earnings" column as the multiple you pay now for what the company earns four years out. Anything above about 25x needs either a higher exit multiple than the model gives it or a bull-case volume to work.

**How many robots does each name need?** The volume at which today's price is fair (0% return) and the volume for a 10% annual return:

| Company | Units for 0% | Units for +10% |
|---|---|---|
| Hesai | 0.2M | 3.7M |
| Keli Sensing | 0.5M | 1.4M |
| Leaderdrive | 1.6M | 2.6M |
| Wuzhou Xinchun | 2.3M | 3.7M |
| Tuopu | 2.4M | 12.8M |
| Hengli Hydraulic | 3.3M | 7.3M |
| Harmonic Drive Systems | 3.3M | 5.7M |
| Huachen Precision | 3.5M | 6.5M |
| Nabtesco | 6.5M | 16.0M |
| Qinchuan | 8.7M | 15.3M |
| Lynas, MP Materials | about 10M to 13M (robots alone cannot carry the price) | never |
| Sanhua, LG Innotek, LG Energy Solution, Allegro | never below 20M | never |
| Nvidia, Schaeffler | fair on the base business alone | Schaeffler needs 8.6M |

Goldman's 2035 number is 6.5M. So Leaderdrive, Wuzhou, Tuopu, Hengli and Harmonic Drive are priced today for roughly 2030 volumes that the most bullish Street house does not expect until 2032 to 2035.

---

## 4. What each business looks like in 2030

**Lynas.** About A$1B of revenue with 20 to 30% of it from heavy rare earths, still the only ex-China Dy/Tb source at scale unless Energy Fuels' White Mesa circuits (2027) and Iluka's Eneabba refinery ramp. Robots are a rounding error in its volumes. The stock is a bet on the two-tier price regime surviving. If China lifts the April 2025 licences, the premium collapses and the model's 25% margin is too high. If it tightens, the model is too low.

**MP Materials.** The 10X plant is running at 10,000 tonnes a year of magnets with the DoD taking output under the ten-year floor. Revenue around $1.3B to $1.5B, profitable for the first time. It looks like a defence-adjacent utility with a guaranteed price. Robots take perhaps 30% of ex-China magnet demand by then, but MP sells whatever it makes regardless.

**Nvidia.** Jetson Thor's successor sits in most Western humanoids, and Nvidia's physical-AI run-rate (about $10B today by its own account) plausibly reaches $30B to $50B including simulation, training and cloud. That is 4 to 7% of a $740B company. Nvidia is the strongest moat in the chain and the least sensitive stock to it.

**Hengli Hydraulic.** The largest roller-screw maker in China with 3M sets of capacity, selling into Tesla and the domestic chain at prices one-tenth of 2025's. Screw revenue around CNY 3.4B on a CNY 20B company: material, not transformative. Price deflation eats most of the volume growth. At 31x 2030 earnings today, the stock needs the bull case.

**Wuzhou Xinchun and Tuopu and Sanhua.** All three depend on one customer building 120,000 robots a year in the base case. Tuopu and Sanhua are large auto suppliers where the robot line is 4% of revenue, so a Tesla slip hurts sentiment more than earnings. Wuzhou is the leveraged version: 29% of revenue and a 41x multiple on 2030 earnings.

**Schaeffler.** Ewellix and the new strain-wave process give it a few hundred million euros of actuator revenue, exactly the "three-digit millions" management has guided. The investment case is the group margin recovering from zero to 3%, which the consensus EPS of EUR 0.88 already assumes. Robots are free.

**Harmonic Drive Systems.** Stuck between two forces: its premium tier keeps roughly 45% of Western humanoid harmonics, but at prices 40% below today's, and Schaeffler's 2027 process plus Chinese entrants cap the volume. Revenue about ¥130B, earnings margin single digit. The 52x multiple on 2030 earnings is the most demanding in the set outside the battery names.

**Leaderdrive.** The biggest transformation: from a CNY 571M company to a CNY 4B one, with harmonics at CNY 600 apiece and 50% of the Chinese chain. Net margin holds at 28% only if the Laifual price war ends; if it does not, margin halves and the stock is worth a third of today. This is the highest-beta name in the set on both sides.

**Keli Sensing.** Four six-axis sensors per robot at CNY 3,000 turns a CNY 1.6B weighing-sensor company into a CNY 4.6B one with 45% of revenue from robots. At 21x 2030 earnings today it is the best-priced pure play, provided ATI, Bota and the private Chinese entrants do not compress the price faster than the model's 90% decline already assumes.

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

- **Keep the moat ranking, change the sizing.** The moat map correctly identified where scarcity sits. The 2030 model says scarcity is priced in for the reducer and screw names and not priced in for Keli and Hesai.
- **Own Nvidia and Schaeffler for reasons other than robots** and treat the robot line as a free option.
- **Treat Lynas and MP as a policy trade** with 10 November 2026 as the next binary date, not as robot-volume plays.
- **Trade the reducer and screw names on drawdowns only.** Leaderdrive needs 1.6M units to be fair; buy it when a Tesla slip or a price-war headline takes 30 to 40% off, as happened on 27 May 2026, and sell it into audit-and-order headlines.
- **Re-run the model on 30 September 2026** (Micron results as a memory read-through), after Tesla's audit outcome, and after Unitree's first-half results, changing only the unit and price cells.

## 7. Limits of this model

Market caps for Hengli, Keli, MP and Qinchuan differ between sources by 10 to 40%; the lower figure was used. Leaderdrive's FY2025 net income is inferred from its price/earnings ratio. Nvidia's 2030 net income assumes 15% growth on FY27 consensus and a 55% margin, which is a data-centre call and not part of this analysis. No sell-side 2027 consensus was available for most Asian names, so base-business growth rates are the analyst's. Component price paths are the single largest source of error and are stated in section 2 so they can be changed.
