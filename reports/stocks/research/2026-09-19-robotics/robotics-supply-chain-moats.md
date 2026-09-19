# Who Owns the Robot Supply Chain? Moat Map for State-of-the-Art Humanoids

*Research date: 19 September 2026. Six parallel research streams (actuators and gears; motors, magnets and batteries; sensors; compute and AI models; structure, hands and machine tools; OEMs and demand). Raw stream reports with full source lists are in `raw/`. All figures come from web-search snippets because finance sites are blocked from this sandbox; verify against filings before acting. Not investment advice.*

---

## 1. The one-paragraph answer

A state-of-the-art humanoid is roughly 28 to 40 actuators, two dexterous hands, a compute module, a 2 to 3 kWh battery, and 5 to 8 cameras wrapped in a die-cast frame. About half the bill of materials is actuators. The supply chain has three genuine scarcity moats today, in this order: **heavy rare earths** (dysprosium and terbium, where Lynas is the only ex-China producer at tonne scale and China's April 2025 licensing regime has never been lifted), **precision thread grinding for planetary roller screws** (the Swiss pair GSA/Rollvis holds over half the world market, Chinese yields are about 60% versus 85% in Switzerland, and the grinder makers Reishauer and Kapp Niles are private), and **Nvidia's full-stack lock-in** on robot compute and simulation (Jetson Thor plus Isaac, Cosmos and GR00T). Everything else, including harmonic reducers, motors, die-castings, connectors, IMUs, contract assembly and, notably, the robot foundation models themselves, is either already commoditising in China or is a relationship moat that lasts only as long as a single customer's ramp.

---

## 2. First principles: why moats form where they do

Think of the humanoid the way the market learned to think about the AI data centre in 2024 to 2026. The GPU got the headlines, but the durable picks-and-shovels moats were the parts where **physics plus tooling plus yield** capped supply: high-bandwidth memory, advanced packaging, transformers. The robot equivalents are:

| Data-centre analogue | Robot analogue | Why it is scarce |
|---|---|---|
| HBM memory oligopoly | Heavy rare earths (Dy/Tb) for joint-motor magnets | Joint motors run hot, so magnets need Dy/Tb to hold field; China controls ~99% of Dy/Tb output and licenses exports; ex-China prices are 4 to 5x China's |
| CoWoS packaging bottleneck | Thread and profile grinders for roller screws and flexsplines | Micron tolerances, heat-treat and metrology know-how; a handful of private machine-tool makers; high-end grinder delivery quoted at about 12 months |
| Transformers and switchgear | Harmonic reducers and roller screws themselves | Real bottleneck in 2023 to 2025 (26-week lead times), but Chinese capacity of 3 to 5 million screws per year and over 2 million reducers per year lands in 2026 to 2027 |
| Nvidia CUDA lock-in | Nvidia Jetson Thor plus Isaac Sim plus Cosmos plus GR00T | Robots developed in Isaac Sim deploy natively on Jetson; every Western tier-1 humanoid ships on it |
| Dell / Supermicro assemblers | Tuopu, Sanhua, Jabil, Foxconn | Volume beneficiaries with thin margins and customer-concentration risk |

The rule that falls out: **a moat is durable when the constraint is a scarce capability (yield, tooling, geology, ecosystem), and temporary when the constraint is merely capacity that money can build.** Reducers are the second kind. Grinders and heavy rare earths are the first kind.

---

## 3. Demand reality check (so the sizing is honest)

| Item | Figure | Source stream |
|---|---|---|
| 2025 global humanoid shipments | 13k to 20k units, over 80% Chinese | OEM stream (Goldman, Morgan Stanley, SAG) |
| 1H 2026 shipments | 19,100 units, +272% y/y; AgiBot 44%, Unitree 31% | SAG via OEM stream |
| 2026 forecasts | Goldman 75k; BofA 90k; Morgan Stanley China-only 50k | OEM stream |
| 2035 forecast | Goldman raised to 6.5M units (from 1.4M) in Sep 2026 | OEM stream |
| Tesla Optimus | V3 reveal slipped again; Musk declined to give a 2026 unit target; Fremont line converted; Tesla audit teams at Sanhua and Tuopu on 16 to 17 Sep 2026 with a reported ~5,000-unit order | OEM and actuator streams |
| Western pure-plays | Figure ~3k/yr run-rate in April 2026 at a $39B private valuation; Agility going public via SPAC at $2.5B with >$300M contracted orders; 1X had no verified customer delivery as of July 2026 | OEM stream |
| Unitree (688836.SS) | Listed 19 Aug 2026, +460% day one to roughly $50B; 2025 revenue CNY 1.7B, 60% gross margin, in-house actuators | Compute and OEM streams |

Implication: 2026 volume is 55k to 90k units and roughly 80% Chinese. That means the moats that pay in the next two years are the ones **inside the Chinese chain** or the ones **China cannot substitute** (heavy rare earths, Nvidia, Swiss screws). The Western OEM ramp (Tesla, Figure, Agility) is a 2027 to 2028 story and its suppliers are priced as if it were already here.

Bill of materials at a blended $30k unit (industrial-grade; Chinese units are $6k to $15k, Western $40k to $60k):

| Subsystem | Share of BOM | Market at 100k units | at 1M units |
|---|---|---|---|
| Rotary actuators (motor + harmonic + encoder + driver) | 28% | $0.8B | $8.4B |
| Linear actuators (motor + roller/ball screw) | 20% | $0.6B | $6.0B |
| Dexterous hands | 15% | $0.45B | $4.5B |
| Structure, thermal, harness | 10% | $0.3B | $3.0B |
| Sensors | 8% | $0.24B | $2.4B |
| Compute | 7% | $0.21B | $2.1B |
| Bearings, encoders, misc | 7% | $0.21B | $2.1B |
| Battery and BMS | 5% | $0.15B | $1.5B |

Morgan Stanley's Optimus Gen-2 teardown ($50k to $60k) puts legs at 39% and hands at 17%. Unitree G1's teardown is about $5.8k with 23 joint modules at 66% of BOM.

---

## 4. Moat map by subsystem

Moat ratings: **A** = scarce capability, durable; **B** = design-win or relationship moat, durable only while the customer ramps; **C** = commoditising or contestable.

### 4.1 Heavy rare earths and magnets: moat A (ex-China), C (China NdPr grades)

- **Lynas (LYC.AX)** is the only producer of dysprosium and terbium outside China at tonne scale (8 to 9 t per quarter). FY26 revenue A$978M (+76%), NPAT A$222M. Risk: heavy-rare-earth capex escalation flagged at results.
- **MP Materials (MP)** has a 10-year US$110/kg NdPr floor and 100% offtake of its 10X magnet plant from the Department of Defense, plus GM and Apple deals. Q2 2026 revenue $108.5M (+89%), still loss-making; 10X commissions about 2028. It has no heavy rare earths of its own.
- **Energy Fuels (UUUU)** produces Dy/Tb in kilograms at pilot scale, with commercial circuits at end-2027, and has an announced $1.9B agreement to buy Vacuumschmelze (single source; confirm via filings).
- **JL MAG (300748.SZ / 6680.HK)** is the world's largest NdFeB maker (40 kt to 60 kt by 2027); H1 2026 revenue CNY 4.7B (+33%), robot and servo revenue +90%. It is a scale play, not a scarcity play, and it is exposed to export licensing.
- **USA Rare Earth (USAR)** is pre-revenue on magnets (Q2 2026 revenue $5.8M, all alloy) despite a $1.6B federal package; it sold off on its Q2 miss.

Magnet content per robot is 2 to 4.5 kg, about twice an electric vehicle. The near-term catalyst is 10 November 2026, when China's one-year suspension of its October 2025 package expires; the April 2025 Dy/Tb licences are still in force. Tesla said in April 2025 that Optimus production was affected by these controls and has not publicly confirmed resolution.

### 4.2 Planetary roller screws and precision grinding: moat A

- The Swiss **GSA and Rollvis** (Ziegler Group, private) hold over half the world market and run near capacity; Optimus Gen-3 reportedly uses 14 screws sourced mainly from GSA (single source).
- **Hengli Hydraulic (601100.SS)** has the largest Chinese capacity: 2.6M sets per year at home plus 0.8M in Thailand, Tesla-validated samples in small-batch delivery, a target of over 5,000 units per month. H1 2026 revenue CNY 6.83B (+32%), net profit flat on FX. Screw revenue is a broker projection (~CNY 2B in 2026 at 40% gross margin), not guidance.
- **Wuzhou Xinchun (603667.SS)** is reported as Tesla's designated inverted-roller-screw supplier for legs and waist and miniature ball screws for hands (over 30 screws per robot); capacity to 980k sets. It rose 183% in 2025 and was among the biggest fallers in the 27 May 2026 humanoid sell-off.
- **Schaeffler (SHA.DE)** owns Ewellix (roller screws, strain-wave gear with integrated torque sensor), counts about 45 humanoid engagements and targets a humanoid order book in the three-digit millions of euros by 2030. It also announced a new strain-wave manufacturing process in August 2026 with mass production from 2027, which could de-bottleneck harmonic gears. Humanoid is immaterial to a leveraged auto supplier today, so this is cheap optionality.
- **The grinder layer** is where the moat is strongest and least investable. Reishauer and Kapp Niles are private. Chinese listed proxies are **Huachen Precision (300809.SZ)**, **Qinchuan Machine Tool (000837.SZ)** and **Haomai (002595.SZ)**; **Klingelnberg (KLIN.SW)** covers harmonic-gear tooling. Chinese screw makers are visibly buying grinders. The single most important missing datapoint in this research is a 2026 delivery lead time for a Reishauer or Kapp Niles thread grinder; none was found.

### 4.3 Harmonic reducers: moat B, sliding to C in China

- **Harmonic Drive Systems (6324.T)**: June-quarter orders +56% y/y, FY3/27 guidance raised to revenue ¥74.5B and operating profit ¥8.5B. Market cap ¥548B, about 186x trailing earnings. No large Japanese greenfield expansion; Beverly MA is adding 33% by December 2026.
- **Leaderdrive / Green Harmonic (688017.SS)**: China's number one with 27.5% domestic share and a claimed 80 to 90% share among Chinese humanoids that use harmonics; FY2025 revenue CNY 571M (+47%), 425k units shipped (+73%), capacity heading to 120k per month by end-2026 and 2M units in 2027; guided to about CNY 1B revenue in 2026. Market cap CNY 51B, about 364x trailing earnings and roughly 50x 2026 sales.
- **Laifual (3952.HK)**: number two in China, listed June 2026; it is the price-war instigator (ASP CNY 802 in 2023 to CNY 573 in 2025) and lost money in 2025.
- Average Chinese harmonic ASP fell about 42% from 2017 to 2024. With over 30 domestic makers, this is the "transformer" of the robot chain: real shortage, capacity coming, margins compressing. The Japanese incumbent keeps the premium industrial tier; the Chinese leader keeps the humanoid volume but at valuations that leave no room for a slip.

### 4.4 Cycloidal reducers and bearings: moat B (industrial), C (humanoid)

- **Nabtesco (6268.T)** has about 60% of the global RV-reducer market for industrial robots but only about 28% of the nascent humanoid mini-RV segment; H1 FY12/26 operating profit +72%, Changzhou plant at 100% utilisation, doubling capacity to 2M units by 2026; about 27x earnings. It is an industrial-robot cyclical more than a humanoid play.
- Cross-roller bearings: **IKO / Nippon Thompson (6480.T)** estimates 14 to 20 per humanoid; **THK (6481.T)**, NSK, Schaeffler and SKF compete. Not reported as bottlenecked anywhere.

### 4.5 Motors and drives: moat C

Motors are the most in-housed part of the joint (Tesla designs its own; Unitree builds its own and says vertical integration is the source of its 60% gross margin; Figure designs everything in-house). Chinese frameless motor volume is 2 to 3 million units per year (Inovance, Leadshine). Western names (**Regal Rexnord / Kollmorgen RRX**, Allient, Maxon, TQ RoboDrive) have know-how but immaterial humanoid revenue; Regal fell 14% on its Q2 print. **Moog (MOG.A)** is being priced as a humanoid supplier without evidence. Power semiconductors are about US$500 of content per robot across Infineon, TI, onsemi, ST and Allegro, multi-sourced and commoditised; **Allegro (ALGM)** is the one with a disclosed robotics revenue line growing over 2x from a small base.

### 4.6 Actuator integrators holding the Tesla purchase orders: moat B

- **Tuopu (601689.SS)**: reported exclusive supplier of lower-limb linear actuators and hand drive modules, first-batch orders CNY 1.5B, two actuator lines of 300k sets per year, Mexico and Thailand plants; market cap about $15B, +33% year to date.
- **Sanhua (002050.SZ)**: joint modules and actuator liquid cooling, a CNY 3.8B Hangzhou base sized for 1M actuators per year; the widely reported CNY 5B Tesla order was denied by the company.
- Both hold a relationship moat and a tariff-proof footprint. Both are hostage to Optimus timing, which has slipped twice in 2026. The 16 to 17 September audits are the confirming signal; the reported 2026 plan of about 50,000 units would be an order of magnitude above what secondary sources expect Tesla to actually build.

### 4.7 Sensors: moat B in three places, C elsewhere

- **Camera modules**: **LG Innotek (011070.KS)** is the only supplier with confirmed mass production for a US humanoid major (5 to 8 modules per robot for Figure; integrated vision unit for Boston Dynamics Atlas). Samsung Electro-Mechanics with **Sony (6758.T)** sensors reportedly supplies Optimus. Module assembly will commoditise as Sunny Optical and Luxshare qualify.
- **Lidar**: **Hesai (HSAI)** shipped 142k robotics lidars in Q2 2026 (+193%), fifth straight GAAP-profitable quarter, JT128 adopted by over 50 embodied-AI companies including Unitree and Galbot. **RoboSense (2498.HK)** robotics units +510% in H1 2026 and is launching joint modules. A duopoly with falling ASPs.
- **Six-axis force/torque**: the cost-down battleground. Average price fell from CNY 46k (2017) to CNY 32k (2022) and humanoids need about four at CNY 2k to 5k to scale. **ATI / Novanta (NOVT)** is the incumbent; **Keli Sensing (603662.SS)** is the Chinese challenger at about 55x earnings.
- **Encoders**: highest unit count (56+ per Optimus) but $20 to $100 each; chip vendors (Allegro, ams OSRAM, onsemi, Broadcom) will take volume from Renishaw and Heidenhain. Commoditising.
- **Tactile skin**: pre-standard and speculative; Luxshare is reported as the exclusive Optimus fingertip-sensor supplier (trade-show source only).
- **IMUs**: fully commoditised.

### 4.8 Compute, simulation and models: moat A (Nvidia), C (models)

- **Nvidia (NVDA)**: Jetson Thor at $2,999 per module is the standard on Figure, Agility, Boston Dynamics and 1X; Isaac Sim, Cosmos 3 and GR00T are used by 1X, Agibot, Agility, Boston Dynamics, Figure, Neura and Skild. Robotics is under 2% of revenue, so this is a free option inside a $5.4T company, and a $3k compute BOM is too expensive for sub-$20k robots.
- **Rockchip (603893.SS)** is the default brain in Chinese entry humanoids (Unitree G1, Agibot X2); H1 2026 revenue +41%, net profit +62%. **Qualcomm (QCOM)** IQ10 is the first credible second source, with Figure and Neura as named wins.
- **Tesla AI5** is dual-sourced at Samsung 2nm (Taylor, trial wafers 15 Sep 2026) and TSMC 3nm; the foundry read-through is the investable angle.
- **Foundation models are the most contestable layer.** At least eight well-funded competitors (Nvidia GR00T, Google Gemini Robotics 2, Physical Intelligence at a reported $11B, Skild at $14B on roughly $30M revenue, Figure Helix, Generalist, Genesis, OpenAI) chase a layer where the two largest incumbents give the model away to sell chips and cloud. No public pure-play exists, and that is the right outcome.

### 4.9 Batteries: moat B (LG Energy Solution), not a supply bottleneck

**LG Energy Solution (373220.KS)** has named humanoid contracts with Tesla, Boston Dynamics and Figure. **Samsung SDI (006400.KS)** targets 500 Wh/kg solid-state humanoid cells in mass production H2 2027. **CATL** powers Galbot; **EVE (300014.SZ)** ships 300 Wh/kg semi-solid cells. Energy density (2 to 4 hour runtimes) is a product constraint, not a supply one; the US solid-state names (QS, SLDP, SES) have no robot contracts.

### 4.10 Structure, hands, materials and assembly: moat C with two exceptions

Die-casting (Tuopu, Xusheng for Figure's magnesium shells, Wencan), connectors (TE, Hirose, Molex hybrid joint connectors), tendon fibre (Avient Dyneema, grams per hand) and contract assembly (Foxconn, Jabil for Apptronik) are relationship-driven and thin-margin. The exceptions: **PEEK polymer** (**Victrex VCT.L** over 50% of global capacity; **Zhongyan 688716.SS** largest in China) faces a plausible capacity squeeze if volumes reach 1M units (about 11 kt), and **micro-drive / coreless-motor makers for hands** (Zhaowei 003021.SZ, Portescap within RRX) have know-how, though Zhaowei's 2025 robotics revenue was only CNY 24M against a valuation that assumes Tesla volume.

---

## 5. Ranked list: where a moat exists and what it costs

| Rank | Company | Ticker | Moat | Why | What is wrong with it |
|---|---|---|---|---|---|
| 1 | Lynas | LYC.AX | A | Only ex-China Dy/Tb at tonne scale; profitable; FY26 revenue +76% | Heavy-rare-earth capex creep; Malaysian politics; stock fell 6% on results |
| 2 | Nvidia | NVDA | A | Full-stack compute + sim + model lock-in on every Western humanoid | Robotics <2% of revenue; already the world's largest company |
| 3 | MP Materials | MP | A (policy) | DoD price floor and 100% offtake; only US mine-to-magnet chain | Loss-making; 10X plant is 2028; no heavy rare earths |
| 4 | Hengli Hydraulic | 601100.SS | A/B | Largest Chinese roller-screw capacity, Tesla-validated, profitable hydraulics base | Screw revenue is a broker forecast; Tesla timing |
| 5 | Schaeffler | SHA.DE | A/B | Ewellix screws, integrated strain-wave gear, new 2027 harmonic process; cheap optionality | Immaterial to group; leveraged auto supplier |
| 6 | Huachen Precision / Qinchuan | 300809.SZ / 000837.SZ | A (tooling) | Chinese thread-grinder proxies while Reishauer and Kapp Niles stay private | Quality gap for sub-5 micron work; no lead-time data found |
| 7 | LG Innotek | 011070.KS | B | Only confirmed mass-production camera supplier to a US humanoid major (Figure, Boston Dynamics) | Humanoid <1% of group; Apple concentration |
| 8 | Hesai | HSAI | B | Number one robotics lidar in China, GAAP profitable, +193% robotics units | ASP deflation; US-listing geopolitics; stale valuation data |
| 9 | LG Energy Solution | 373220.KS | B | Named cells for Tesla, Boston Dynamics, Figure | Cell format undisclosed; EV cycle dominates |
| 10 | Harmonic Drive Systems | 6324.T | B | Premium tier incumbent, orders +56% | 186x earnings; Chinese share gains; Schaeffler process 2027 |
| 11 | Tuopu | 601689.SS | B | Holds the reported Tesla actuator purchase orders, tariff-proof plants | Tesla V3 has slipped twice; unconfirmed order claims |
| 12 | Leaderdrive | 688017.SS | B | 80 to 90% of Chinese humanoid harmonics, 2M-unit 2027 capacity | 364x earnings; Laifual price war |
| 13 | Nabtesco | 6268.T | B | 60% of industrial RV, 27x earnings, capacity doubling | Only 28% of humanoid mini-RV; humanoids moving to harmonic + screw |
| 14 | Keli Sensing | 603662.SS | B | Chinese six-axis F/T challenger, wrist and ankle series | 55x earnings; F/T still a small share of revenue |
| 15 | Allegro | ALGM | C+ | Only chip vendor with a disclosed robotics revenue line (2x) | Encoders and drivers commoditise |

Names the market treats as humanoid plays where the evidence does not support a moat: **Moog** (aerospace actuation mispriced as humanoid), **Zhaowei** (CNY 24M robotics revenue), **Orbbec** (about 50x sales with H1 2026 revenue growth of 0.5%), **Laifual** (loss-making price-war instigator), **USA Rare Earth** (pre-revenue on magnets), **Navitas, QuantumScape, Solid Power, SES** (no robot contracts), and **Unitree** at roughly $50B (a fine company at an extreme price).

---

## 6. How to hold it (framework, not advice)

- **Core, scarcity-based (2 to 3% each for a risk-aware investor)**: Lynas, MP Materials, Nvidia (already held by most portfolios), Schaeffler as the cheap way in.
- **Sleeve, relationship-based (1 to 1.5%)**: Hengli, LG Innotek, Hesai, LG Energy Solution. Stage entries around the confirming events below.
- **Tooling sleeve (0.5 to 1%, speculative)**: Huachen and Qinchuan as the only listed proxies for the grinder bottleneck.
- **Trade, not hold**: Harmonic Drive, Leaderdrive, Tuopu, Sanhua, Keli. These are momentum vehicles on Tesla headlines with triple-digit multiples; the 27 May 2026 sell-off showed the downside.
- **Avoid at current prices**: the list at the end of section 5.

## 7. Dated signals that confirm or kill the thesis

| Date | Event | What it tells you |
|---|---|---|
| Late Sep to Oct 2026 | Outcome of Tesla's Zhejiang supplier audits; any Tesla-confirmed supplier or order | Converts Tuopu/Sanhua/Hengli/Wuzhou from rumour to disclosure |
| 10 Nov 2026 | Expiry of China's one-year suspension of its October 2025 rare-earth package | Renewal or lapse sets the ex-China Dy/Tb premium for 2027 |
| H2 2026 | Tesla Optimus V3 reveal and first Fremont output; 2026 target still undisclosed | Any hard unit number re-rates the entire Chinese Tesla chain |
| By YE 2026 | Agility SPAC close (AGLT); Unitree H1 2026 results (guided +36 to 45%) | First public Western pure-play and the Chinese profitability benchmark |
| Dec 2026 | Harmonic Drive Beverly MA +33% capacity; Leaderdrive 120k per month run-rate | Tests whether reducer pricing holds as capacity lands |
| 2027 | Schaeffler strain-wave mass production; Samsung SDI 500 Wh/kg solid-state; Hyundai 30k-unit plant build toward 2028 | De-bottlenecking of harmonics; battery step change; Western volume |
| Ongoing | Publication of a Reishauer or Kapp Niles thread-grinder lead time | The single datapoint that would confirm the grinder as the true bottleneck |

## 8. Gaps in this research

Finance sites were blocked, so valuation multiples are missing for most Japanese, Korean and Chinese names and stale for Hesai. No source gave a 2026 thread-grinder lead time. Tesla supplier claims are all from Chinese media and broker notes, not from Tesla. The Energy Fuels acquisition of Vacuumschmelze rests on a single source. Policy and ETF sections in the OEM stream were written from background knowledge and are unverified. Each raw stream report lists its own unverified claims.
