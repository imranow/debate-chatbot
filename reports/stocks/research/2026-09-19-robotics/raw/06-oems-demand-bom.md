# Humanoid / General-Purpose Robot Demand Side & OEM Landscape — as of 19 Sep 2026

**Research constraints (read first):** 16 web searches completed before the session hit its hard search cap (200/200); every WebFetch/curl attempt was blocked by the egress proxy (electrek, CNBC, Goldman, Hyundai, Agility, KraneShares, 36kr, etc.). Sections 1–2 and the demand forecasts are sourced from search snippets (URLs in section f). **Sections 3 (incumbents), 4 (policy) and 5 (investor vehicles) could not be searched at all** — those are written from analyst background knowledge current to ~mid-2026 and are explicitly marked UNVERIFIED; treat every number there as a hypothesis to be checked. No YTD stock performance could be retrieved.

---

## (a) OEM status table (Sept 2026)

| OEM | Product / gen | Status Sep-2026 | Volumes | Funding / valuation | Disclosed suppliers & partners | Source |
|---|---|---|---|---|---|---|
| **Tesla** | Optimus V3 (Gen 3); Gen 4 planned for Giga Texas | V3 reveal pushed "later this year" again (Electrek, 22 Apr 2026); Fremont Model S/X line converted; Musk previously said production "late July/Aug 2026". Electrek (7 Sep 2026) headline: "Tesla Optimus stalls" as XPeng starts line. Musk **declined to give any 2026 unit target**; admitted Jan-2026 that zero Optimus were doing useful factory work; missed the 10k-unit 2025 goal entirely. | 2025: ~0 useful units. 2026 realistic: "low thousands" (secondary sources). Stated capacity: 1M/yr Fremont "by late 2026"; 10M/yr Giga Texas from ~summer 2027 | Internal (TSLA) | Chinese press/broker reports (not Tesla disclosures): Sanhua (joint modules; reported $685M order Oct-2025, Mexico plant 2026), Tuopu (Tier-0.5 actuator assembly, Mexico, 300k-set capacity target Q2-26), Leaderdrive/"Green Harmonic" (harmonic reducers), Wuzhou Xinchun (planetary roller screws, Thailand plant 2026). Tesla audit teams in Zhejiang at Sanhua/Tuopu on **16 Sep 2026**. Claimed ~70% China content. | electrek.co, teslarati, 36kr, kantan.news, BigGo |
| **Figure AI** | Figure 03 (Helix VLA) | BotQ ramp: few units/mo (2025) → ~60 (Feb-26) → ~240 (Apr-26); "one robot/day to one/hour in <120 days". Figure 03 at BMW Spartanburg: 40 units (Figure 02 previously ran 11 months, 90k parts, 30k X3s). | Run-rate ~3k/yr in Apr-26; BotQ capacity plan 12k → 100k/yr | $39B post-money (Sep-2025); >$1.9B raised; IPO speculation | Vertically integrated (in-house actuators, BotQ). No public supplier list. | sacra.com, iiot-world, humanoidanalytics, axis-intelligence |
| **Agility Robotics** | Digit 5 (unveiled 17 Sep 2026) | Going public via Churchill Capital XI SPAC at $2.5B (announced 24 Jun 2026; ticker AGLT, close by YE-2026). >$300M multi-year contracted Digit v5 orders. Customers: GXO (Flowery Branch: 100k totes, ~98% accuracy), Schaeffler, Toyota Motor Mfg Canada, Mercado Libre; >65k field hours. | RoboFab (Salem, OR, 70k sq ft) capacity 10k/yr at peak; actual fleet: tens-to-low-hundreds (not disclosed — flag) | >$390M private raised; SPAC gross ~$620M incl. **$200M Foxconn-led PIPE** | Schaeffler (strategic investor + motion components + customer), Foxconn (PIPE lead — likely contract mfg; unconfirmed) | geekwire, businesswire, roboticsandautomationnews (17 Sep 2026) |
| **Apptronik** | Apollo | Pilots at Mercedes-Benz, GXO, Jabil; "commercial quantities by 2027" | Not disclosed (pilot fleets) | $520M Series A-X (11 Feb 2026) → Series A >$935M, total ~$1B, **~$5B valuation**; investors: Google, Mercedes, B Capital, PEAK6, John Deere, AT&T Ventures, QIA | **Jabil** (contract manufacturer + customer), Google DeepMind (Gemini Robotics), Mercedes | cnbc.com (11 Feb 2026), apptronik.com |
| **1X** | NEO (home) | Pre-orders: $20,000 or $499/mo, $200 deposit; deliveries US/Canada 2H-2026, expand 2027. **As of 16 Jul 2026 no verified customer delivery.** Teleop-assisted caveat. | Nil shipped as of mid-2026 (flag) | (funding not retrieved) | Not disclosed | therobotreport, robotics247, notebookcheck |
| **Boston Dynamics (Hyundai)** | Atlas (production version, CES 5 Jan 2026) | First production run shipping 2026 to Hyundai and Google DeepMind. Hyundai plant use: parts sequencing 2028, assembly 2030. Hyundai $26B US investment incl. **30,000 units/yr humanoid factory targeted 2028**. | 2026: initial production run (count not disclosed) | Hyundai-owned | Google DeepMind (Gemini Robotics on Atlas); Hyundai Mobis/Glovis ecosystem (flag) | engadget, automate.org, bostondynamics.com, hyundainews.com/releases/4664 |
| **Unitree** | R1 ($4,900), G1 ($13,500), H2 ($29,900), H2 Plus ($100,000) | **IPO on STAR Market (688836)**: priced RMB150.8 → RMB6.1B raised (~$904M), $9B pre-listing valuation (6 Aug 2026); +460% day one, ~RMB342B (~$50B) mkt cap. | 2025: 5,500+ humanoids; revenue RMB1.70B (from 393M), net profit RMB278M; humanoids 52% of 9M-25 revenue. 1H26: ~31% of 19.1k global = ~5.9k | Listed; ~$50B cap post-pop | Teardown (China Post Securities, Mar-2026): in-house actuators; DJI (cameras), Intel, Longsys; TV-class SoC (Rockchip RK3588 — flag); Nvidia Jetson on EDU | cnbc.com (6 Aug 2026), yahoo, kraneshares, eeworld |
| **UBTech (9880.HK)** | Walker S2 (industrial, hot-swap battery); U1 (home) | Walker S2 orders >RMB800M (Nov-2025); RMB250M single contract; RMB159M Zigong data-collection centre; target 500 S2 delivered in 2025; **capacity target 5,000 (2026) → 10,000 (2027)**; U1 home units shipping Sept-2026; "13,000 reserved" for new bionic line (The Standard — flag) | 2025: several hundred S2; 2026 guide 5k capacity | Listed HKEX Dec-2023 | Not disclosed | prnewswire, chinadaily, thestandard.com.hk, humanoid.guide |
| **AgiBot (Zhiyuan)** | A2/G1/X2 lines | 10,000th unit Mar-2026; 15,000th in 1H26; **#1 globally 1H26 at 44% share (~8.4k units)** (SAG); Omdia ranked #1 for 2025. HK IPO targeted Q3-2026 at HK$40–50B ($5.1–6.4B). | 1H26 ~8.4k | >RMB15B valuation; investors LG Electronics, BYD, Hillhouse, Mirae | LG (strategic), BYD | smartanalyticsglobal, techtimes, agibot.com, capital.com |
| **Galbot** | Wheeled humanoids (G1) | #3 globally 1H26 ~900 units; RMB2.5B round Mar-2026 (highest-valued unlisted China humanoid) | ~900 (1H26) | RMB2.5B raise Mar-26 | n/a | humanoidsdaily |
| **Fourier** | GR-3 (care/rehab) | >RMB1B Series C; clinical install base | n/d | >RMB1B Series C | n/a | robozaps |
| **XPeng** | IRON (76 DoF, 21/hand) | **Automated production line commissioned ~7 Sep 2026** (>80% automated); mass production by YE-2026 into own stores/campuses; external sales 2027; target >1,000/month, 1M/yr by 2030. XPeng Robotics raised **$900M at $6.3B** (24 Aug 2026). | 2026: hundreds–low thousands internal | $6.3B (robotics sub) | In-house Turing chip, VLA 2.0 | xpeng.com, cnevpost, electrek (24 Aug & 7 Sep 2026) |
| **Xiaomi** | "Tieda" (WRC Aug-2026; 1.70m, 66kg, 66 DoF) | Factory trials at EV plant since Mar-2026 (nut install 90.2% → 98% after 4 months); "large numbers" deployed within 5 years | Trial fleet | Internal | n/a | technode, scmp, cnbc (4 Mar 2026), BigGo |
| **Neura Robotics** | 4NE-1 | Series C **up to $1.4B, ~$7B valuation** (10–12 Jun 2026; Tether, Nvidia, Amazon, Qualcomm, Bosch; milestone-contingent). **Zero verified customer deployments/pilots as of 15 Aug 2026.** | ~0 | ~$7B | Bosch (investor) | cnbc (10 Jun 2026), neura-robotics.com, theresarobotforthat |
| **Sanctuary AI** | Phoenix | Undisclosed funding May-2026; no 2026 deployment data found — **missing** | n/d | n/d | n/d | tracxn (indirect) |

---

## (b) Bill of materials

**Morgan Stanley teardown of Optimus Gen-2 (BOM $50–60k):** legs ~$21k (38.6%), hands $9.5k (17.2%), waist/pelvis $7.8k (14.2%), feet $6.7k (12.2%), elbows $2.6k (4.7%), forearms $2.2k (3.9%), head $2.1k (3.8%), upper arms $1.1k (2.0%). Planetary roller screws $1,350–2,700 each. Actuators+reducers ≈ half of BOM at scale. (Source: robozaps economics page, corematter substack summarising MS.)

**Unitree G1 (China Post Securities teardown, Mar-2026):** BOM RMB41.6k (~$5.8k) on an RMB85k retail → 40.7% GM (EDU up to 66.7%); 23 joint modules = RMB27.5k (66% of BOM; 14 small @RMB1k, 9 large @RMB1.5k); plastics/aluminium structure, steel only in shin. A Japanese teardown puts G1 BOM at **$6,144** (X/teortaxes). G1 retail now $13.5k (was $16k). "Chinese cost cliff": Western BOM ~$131k vs China cited by patentailab (unverified).

**Targets:** Tesla $20–30k/unit at scale (Musk); Goldman (2024) high-spec BOM fell to ~$35k from $50–250k; Unitree G1 <$6.2k BOM already.

### Subsystem table (synthesised; blended $30k BOM assumed for a full-size industrial humanoid — Chinese units are ~$6–15k, Western $40–60k; shares are analyst-consensus ranges, not a single published table)

| Subsystem | % BOM | Units / robot | $/robot @ $30k | 2027 mkt @100k | @1M | @10M |
|---|---|---|---|---|---|---|
| Rotary actuator modules (frameless motor + harmonic reducer + encoder + driver) | 28% | ~14 | $8,400 | $0.84B | $8.4B | $84B |
| Linear actuators (motor + planetary roller/ball screw) | 20% | ~14 | $6,000 | $0.60B | $6.0B | $60B |
| — of which harmonic reducers | (8%) | 12–14 | $2,400 | $0.24B | $2.4B | $24B |
| — of which planetary roller screws | (8%) | 12–14 | $2,400 | $0.24B | $2.4B | $24B |
| Dexterous hands (micro-motors, tendons/screws, tactile) | 15% | 2 (22 DoF Optimus; 21/hand IRON) | $4,500 | $0.45B | $4.5B | $45B |
| Sensors (cameras, IMU, F/T, tactile skin, optional lidar) | 8% | 3–8 cams, 1–2 IMU, 6+ F/T | $2,400 | $0.24B | $2.4B | $24B |
| Compute (SoC/FSD-class + boards) | 7% | 1–2 | $2,100 | $0.21B | $2.1B | $21B |
| Battery pack + BMS (2–3 kWh) | 5% | 1 | $1,500 | $0.15B | $1.5B | $15B |
| Structure / frame / skin / thermal / harness | 10% | — | $3,000 | $0.30B | $3.0B | $30B |
| Bearings, encoders, misc. electronics | 7% | 50–100 bearings | $2,100 | $0.21B | $2.1B | $21B |
| **Total** | 100% | | **$30,000** | **$3.0B** | **$30B** | **$300B** |

Sensitivity: at a China-style $10k BOM, divide by 3; at a Western $50k BOM, multiply by 1.67. Legs/hands dominate under MS methodology (~56% combined), consistent with the actuator-heavy split above.

---

## (c) Demand forecasts (with sources)

| Metric | Figure | Source |
|---|---|---|
| 2025 global shipments (actual) | 13k–18k; Goldman 15–20k; MS ~16k with >80% China; SAG 5.1k in 1H25 | robozaps, cnbc/MS (24 Jun 2026), SAG |
| 1H-2026 global shipments | **19,100 (+272% YoY)**; AgiBot 44%, Unitree 31%, Galbot #3 (~900) | smartanalyticsglobal.com; humanoidsdaily |
| 2026 forecasts | Goldman 75k (raised from 51k); **BofA 90k**; MS China 50k (from 28k, 24 Jun 2026); TrendForce >50k global, China output +94% | cnbc, 247wallst, kraneshares |
| 2027 | Omdia (Jul-2024, superseded) >10k; UBTech 10k capacity; Agility 10k RoboFab; XPeng 1k/mo run-rate; Hyundai 30k/yr plant (2028) | omdia, prnewswire |
| 2030 | Goldman 890k (raised from 256k, Sep-2026); Omdia (2024) 38k; XPeng 1M/yr ambition | 247wallst (14 Sep 2026), omdia |
| 2035 | Goldman **6.5M units** (raised 5x from 1.4M, Sep-2026); Goldman $38B market (Feb-2024 note — likely raised) | 247wallst, goldmansachs.com |
| 2050 TAM | Morgan Stanley $5T; Citi $7T | robozaps, streetwisereports |
| Tesla-specific | Musk: 1M/yr Fremont late-2026, 10M/yr Texas 2027; secondary estimates "low thousands" in 2026 | electrek, robotnewstoday |
| **Missing** | IDC and Omdia 2026 refreshed numbers; Citi 2030 unit count; MS global (non-China) unit forecast | — |

House view for sizing: 2026E ~55–90k global (Chinese OEMs ≈75–85%); 2027E 150–250k if AgiBot/Unitree/UBTech/XPeng capacity is used, plus 5–20k Western (Figure, Agility, Apptronik, BD, Tesla). The 100k case in the BOM table is a 2027 bear/base; 1M is a 2029–30 bull; 10M is Musk-narrative only.

---

## (d) Disclosed suppliers by OEM (buys from whom)

- **Tesla**: Sanhua (joint/actuator modules, Mexico), Tuopu (actuator assembly, Mexico, 300k sets Q2-26 target), Leaderdrive/Green Harmonic (harmonic reducers, "exclusive"), Wuzhou Xinchun (roller screws, Thailand). All from Chinese media/broker channels, **none confirmed by Tesla**. Tesla audit visit Zhejiang 16 Sep 2026 suggests V3 sourcing is being finalised.
- **Figure**: vertically integrated (BotQ); no external actuator supplier disclosed.
- **Agility**: Schaeffler (investor + motion components + customer); Foxconn (PIPE lead; manufacturing role unconfirmed).
- **Apptronik**: Jabil (EMS partner + customer); Google DeepMind (AI); Mercedes (customer/investor); Deere (investor).
- **Boston Dynamics**: Hyundai group (owner, factory 2028); Google DeepMind (Gemini Robotics).
- **Unitree**: in-house joint motors; DJI cameras, Intel, Longsys, Rockchip-class SoC; Nvidia Jetson (EDU).
- **AgiBot**: LG Electronics, BYD (investors/strategic); component suppliers not disclosed.
- **XPeng**: in-house line; own Turing SoC.
- **Neura**: Bosch (investor; possible manufacturing).
- **UBTech / 1X / Xiaomi / Galbot / Fourier / Sanctuary**: no supplier disclosure found.

---

## (3) Incumbents, (4) Policy, (5) Investor vehicles — UNVERIFIED (no search capacity remained; background knowledge to ~mid-2026, verify before use)

**Incumbents:** ABB agreed (Oct-2025) to sell ABB Robotics to SoftBank for ~$5.4B instead of the planned spin-off, closing targeted mid/late-2026 — status as of Sep-2026 unverified. Fanuc/Yaskawa: no humanoid products; Yaskawa (servo motors, MOTOMAN NEXT) and Fanuc are seen as component/servo suppliers rather than humanoid OEMs; Harmonic Drive Systems (6324.T) and Nabtesco (6268.T) are the Japanese reducer incumbents being displaced by Leaderdrive/Shuanghuan in Chinese humanoids. KUKA (Midea) — Midea has shown humanoid prototypes using KUKA capability. Teradyne (UR/MiR) — cobot demand soft in 2025; Nvidia collaboration; no humanoid product. Estun (002747.SZ) and Siasun (300024.SZ) have humanoid programmes. Samsung controls Rainbow Robotics (35%, RB-Y1 wheeled humanoid); LG invested in AgiBot and Bear Robotics; Toyota uses Digit (TMMC) and partners TRI with Boston Dynamics on large behaviour models; Honda — no active humanoid product (flag). Hyundai: 30k/yr humanoid plant 2028 (verified above).

**Policy:** China — MIIT humanoid guidelines (target: mass production 2025, world-leading 2027); "embodied intelligence" in the 2025 Government Work Report and in the 15th Five-Year Plan (2026–30) as a future industry; RMB1T national venture guidance fund; municipal funds (Beijing RMB100B robotics fund, Shanghai/Shenzhen embodied-AI subsidies); state/SOE procurement (e.g., UBTech's Zigong data-centre contract) — this policy stack explains why >80% of 2025 units were Chinese and favours domestic reducer/screw/motor suppliers. US — Commerce Section 232 investigation into robotics/industrial machinery imports (opened Sept-2025); China tariffs; reshoring push (Sanhua/Tuopu Mexico plants and Wuzhou Xinchun Thailand plant are direct tariff-avoidance responses; Hyundai's $26B US plan and Agility RoboFab are the US-build cases). Reports of a US robotics executive order — **could not verify**. EU — AI Act and Machinery Regulation (2027) compliance costs; Neura ($1.4B) is the flagship EU champion.

**Investor vehicles:** BOTZ (Global X), ROBO (ROBO Global), ARKQ (ARK), KOID (KraneShares Global Humanoid & Embodied Intelligence, launched 2025; holds Unitree post-IPO per KraneShares article), HUMN (Roundhill Humanoid Robotics). **KROP is KraneShares' agriculture ETF, not robotics.** Morgan Stanley "Humanoid 100" (Feb-2025): 100 listed names across Brain (semis/software: Nvidia, Alphabet, Tesla…), Body (actuators/sensors/batteries: Sanhua, Tuopu, Leaderdrive, Shuanghuan, Harmonic Drive, Regal Rexnord, Hengli, Nidec, THK, NSK…) and Integrators (Tesla, UBTech, Xiaomi, XPeng, Hyundai, Toyota…); Asia dominates the Body list (~73%), China ~56% of it (recollection — verify). Market-treated "humanoid plays": Sanhua (002050.SZ/2050.HK), Tuopu (601689.SS), Leaderdrive (688017.SS), Shuanghuan Driveline (002472.SZ), Wuzhou Xinchun (603667.SS), Hengli Hydraulic (601100.SS), Best Precision (300580.SZ), Zhaowei (003021.SZ), Harmonic Drive (6324.T), Regal Rexnord (RRX), Teradyne (TER), UBTech (9880.HK), Unitree (688836.SS). **YTD 2026 performance: not retrievable in this session.**

---

## (e) Unverified / conflicting claims to flag

1. Tesla supplier names and the "$685M Sanhua order" / "300k Tuopu sets" — Chinese-media sourced, not Tesla-confirmed.
2. "Tesla Optimus stalls" (Electrek 7 Sep 2026) — headline only; underlying unit count unknown. Musk's 1M/yr "late 2026" is not a forecast anyone models.
3. Figure BotQ "240/month in April" and 12k→100k capacity — from secondary aggregators (Sacra/Axis), not Figure filings.
4. UBTech "13,000 units reserved" for "million-dollar bionic humanoids" (The Standard) — likely reservations, not orders.
5. Unitree G1 BOM: $5.8k (China Post) vs $6,144 (Japanese teardown) — consistent; Unitree 1H26 unit count is inferred from 31% share.
6. SAG's 19.1k 1H26 figure may include wheeled humanoids (Galbot) — definitional risk when comparing with Goldman/MS.
7. Omdia's 2027 (10k) and 2030 (38k) forecasts are from July 2024 and already exceeded; no refreshed Omdia/IDC numbers found.
8. Hyundai "30,000 units/yr by 2028" — from Hyundai CES release via secondary sources; may be total robots not humanoids.
9. Everything in the Incumbents / Policy / ETF sections (see above).
10. Sanctuary AI: only "undisclosed funding May 2026" — status effectively unknown.

---

## (f) Sources (URLs)

Tesla: https://electrek.co/2026/04/22/tesla-optimus-production-fremont-model-sx-line/ ; https://robotnewstoday.com/reports/tesla-optimus-gen3-production-2026/ ; https://www.tesery.com/blogs/news/elon-musk-reveals-aggressive-production-timeline-for-tesla-optimus-3 ; https://electrek.co/2026/09/07/xpeng-iron-humanoid-robot-production-line/ ; https://eu.36kr.com/en/p/3780414717129481 ; https://www.teslarati.com/tesla-optimus-v3-design-finalized-china-rumors/ ; https://kantan.news/news/tesla-begins-auditing-chinese-suppliers-for-optimus-production ; https://finance.biggo.com/news/gQPHv50BZk7xib5f4ox8
Figure: https://sacra.com/c/figure-ai/ ; https://www.iiot-world.com/artificial-intelligence-ml/robotics/physical-ai-deployment-roi-humanoid-robots/ ; https://humanoidanalytics.com/2026/06/15/figure-ais-39-billion-valuation-tests-humanoid-robotics-expectations/ ; https://axis-intelligence.com/figure-ai-statistics/
Agility: https://www.geekwire.com/2026/digit-maker-agility-robotics-to-go-public-in-2-5b-deal-heres-what-the-filings-say-about-its-finances/ ; https://www.businesswire.com/news/home/20260624555633/en/ ; https://roboticsandautomationnews.com/2026/09/17/agility-unveils-digit-5-humanoid-as-orders-exceed-300-million-ahead-of-public-listing/104857/ ; https://www.agilityrobotics.com/content/agility-robotics-announces-strategic-investment-and-agreement-with-motion-technology-company-schaeffler-group
Apptronik: https://www.cnbc.com/2026/02/11/apptronik-raises-520-million-at-5-billion-valuation-for-apollo-robot.html ; https://apptronik.com/news-collection/apptronik-closes-over-935-million-series-a
1X: https://www.therobotreport.com/1x-announces-pre-order-launch-neo-humanoid-robot/ ; https://theplanettools.ai/blog/1x-neo-first-consumer-humanoid-dated-priced-teleop-caveat-may-2026 ; https://blog.robozaps.com/b/1x-neo-review
Unitree: https://www.cnbc.com/2026/08/06/chinese-humanoid-robot-maker-unitree-prices-ipo-at-9-billion-valuation.html ; https://finance.yahoo.com/markets/stocks/articles/unitree-robotics-stock-soars-460-111514463.html ; https://kraneshares.com/a-complete-guide-to-unitree-robotics-2026-ipo-why-it-matters-for-star-market-etf-kstr-humanoid-robotics-etf-koid/ ; https://en.eeworld.com.cn/news/robot/eic733333.html ; https://longbridge.com/en/news/281283080 ; https://x.com/teortaxesTex/status/2081099254001553812
Boston Dynamics/Hyundai: https://www.engadget.com/big-tech/boston-dynamics-unveils-production-ready-version-of-atlas-robot-at-ces-2026-234047882.html ; https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026 ; https://www.hyundainews.com/releases/4664 ; https://bostondynamics.com/blog/boston-dynamics-google-deepmind-form-new-ai-partnership/
UBTech: https://www.prnewswire.com/news-releases/ubtech-humanoid-robot-walker-s2-begins-mass-production-and-delivery-with-orders-exceeding-800-million-yuan-302616924.html ; https://global.chinadaily.com.cn/a/202509/09/WS68bf7e39a3108622abc9f971.html ; https://www.thestandard.com.hk/innovation/article/336083/ ; https://humanoid.guide/ubtech-lines-up-september-deliveries-for-u1-home-humanoids/
AgiBot/Galbot/Fourier: https://smartanalyticsglobal.com/global-humanoid-robot-shipments-2026-agibot-unitree/ ; https://www.humanoidsdaily.com/news/global-humanoid-shipments-surge-272-in-1h-2026-as-agibot-overtakes-unitree ; https://www.techtimes.com/articles/317632/20260602/ ; https://capital.com/en-int/learn/ipo/agibot-ipo ; https://www.agibot.com/article/231/detail/33.html
XPeng/Xiaomi: https://www.xpeng.com/news/01a080371029a057bc8e8a02a2c6012b ; https://cnevpost.com/2026/09/08/xpeng-opens-iron-humanoid-robot-production-line/ ; https://electrek.co/2026/08/24/xpeng-robotics-900m-iron-humanoid-robot-valuation/ ; https://www.humanoidsdaily.com/news/xpeng-ceo-targets-late-2026-for-massive-iron-deployment ; https://technode.com/2026/03/03/xiaomi-says-humanoid-robots-begin-factory-trials-targets-large-scale-deployment-within-five-years/ ; https://www.cnbc.com/2026/03/04/xiaomi-humanoid-robots-ev-factory-.html ; https://finance.biggo.com/news/ba425dbf-72e3-42cf-bada-583533e1057e
Neura/Sanctuary: https://www.cnbc.com/2026/06/10/neura-robotics-funding-ai-humanoid-robots.html ; https://neura-robotics.com/record-series-c/ ; https://theresarobotforthat.com/blog/neura-robotics/ ; https://tracxn.com/d/companies/neura-robotics/
Forecasts: https://247wallst.com/investing/2026/09/14/goldman-sachs-just-supercharged-its-humanoid-robot-prediction-5x-to-6-5-million-by-2035/ ; https://www.goldmansachs.com/insights/articles/the-global-market-for-robots-could-reach-38-billion-by-2035 ; https://www.cnbc.com/2026/06/24/morgan-stanley-china-humanoid-robot-market-forecast.html ; https://www.cnbc.com/video/2025/11/28/humanoid-robot-orders-and-shipments-could-multiply-2026-goldman-sachs.html ; https://omdia.tech.informa.com/pr/2024/jul/omdia-global-humanoid-robot-shipments-to-exceed-10000-units-by-2027-and-reach-38000-units-in-2030 ; https://cervo-tech.com/blog/humanoid-robot-market-statistics-2026.html ; https://blog.robozaps.com/b/market-size-for-humanoid-robots ; https://www.streetwisereports.com/article/2026/09/16/
BOM: https://blog.robozaps.com/b/economics-of-humanoid-robot-production ; https://corematter.substack.com/p/humanoid-robot-actuator-cost-bom-analysis ; https://www.grabarobot.com/blog/humanoid-robot-bill-of-materials-cost-2026/ ; https://en.eeworld.com.cn/news/robot/eic720187.html ; https://patentailab.com/tesla-vs-china-robot-patent-war/

**Recommended follow-ups (need search budget):** (1) confirm ABB→SoftBank close and Fanuc/Yaskawa humanoid component wins; (2) pull KOID/HUMN/BOTZ holdings and YTD for the Sanhua/Tuopu/Leaderdrive/Shuanghuan/HDS/RRX/TER basket; (3) verify Goldman Sept-2026 note's 2026/2027 unit path and BOM curve; (4) get Figure's H1-2026 unit disclosure and Agility S-4 unit/revenue data; (5) China 15th FYP embodied-AI clauses and US robotics EO/232 outcome.
