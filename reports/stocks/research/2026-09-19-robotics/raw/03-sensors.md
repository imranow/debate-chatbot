# Humanoid / General-Purpose Robot SENSOR Supply Chain — Equity Research Note
**Date:** 19 Sep 2026. **Method:** ~30 web searches (search budget exhausted); WebFetch to all target news/finance domains was blocked by the egress proxy, so every figure below is from search-result snippets and is cited by URL. Figures not found are flagged "n/f".

---

## (a) Summary table

| Component | Top-3 suppliers (evidence-weighted) | Moat rating | Investable ticker(s) | Value / bottleneck status |
|---|---|---|---|---|
| CMOS image sensors | 1. Sony Semiconductor 2. OmniVision/Will Semi 3. onsemi | Sony: **High** (>50% CIS share; sensor inside the Semco Optimus module). OmniVision: Med. onsemi: Med-Low for humanoids | 6758.T, 603501.SS, ON | High-volume but the sensor die is commoditised at humanoid volumes; value accrues to Sony via share, not humanoid-specific pricing |
| Camera modules (RGB + depth, integrated) | 1. LG Innotek (Figure, Boston Dynamics; mass production 2026) 2. Samsung Electro-Mechanics (Optimus) 3. Sunny Optical (Chinese OEMs) | Med (module assembly is contestable; wins are customer-specific, not IP) | 011070.KS, 009150.KS, 2382.HK | Currently **design-win bottleneck** (only 2 Korean firms qualified for US majors); will commoditise as Sunny/Luxshare/Cowell qualify |
| 3D depth cameras | 1. Orbbec (>70% share in Chinese service-robot 3D vision) 2. RealSense (claims 60% of AMRs/humanoids) 3. Sunny/LG Innotek integrated depth | Orbbec: Med-High in China; RealSense: Med (installed base, but private) | 688322.SS (RealSense private) | Orbbec is the purest public play but revenue growth stalled to +0.5% in H1'26 |
| Robot lidar | 1. Hesai (No.1 China humanoid/quadruped lidar; 50+ embodied-AI customers) 2. RoboSense (No.1 global robotics lidar 2025 by units) 3. Ouster (REV8 colour lidar + StereoLabs) | Hesai/RoboSense: **High** (scale, cost, ASIC-based) | HSAI, 2498.HK, OUST | High volume, rapidly falling ASP; duopoly economics in China |
| Event cameras | 1. Prophesee (Sony IMX636 co-developed) | Low-Med (niche, pivoting to drone detection) | Private (Sony 6758.T indirect) | Not on any production humanoid; research-only |
| 6-axis force/torque | 1. ATI/Novanta (global incumbent) 2. Keli Sensing (wrist/ankle series; Optimus alt-supplier) 3. Kunwei / Hypersen / Bota (private) | ATI: High in industrial, Med in humanoid; Keli: Med (cost position) | NOVT, 603662.SS | **High-value & still bottlenecked** (RMB32k/set avg 2022; humanoid needs 4/robot at ~RMB2-5k to scale) — biggest cost-down battleground |
| Joint torque sensing / encoders | 1. Renishaw/RLS (AksIM/Orbis) 2. Heidenhain (private, KCI 120 Dplus dual encoder) 3. Allegro / Broadcom / ams OSRAM / onsemi (chip-level magnetic & inductive) | Renishaw/Heidenhain: Med-High (precision); chip vendors: Low-Med (commoditising fast) | RSW.L, ALGM, AVGO, AMS.SW, ON, 002333.SZ | Highest unit count per robot (2 per joint, 56+ per Optimus) but $20-100 each → **commoditising** |
| Tactile / e-skin | 1. Luxshare (reported exclusive Optimus Gen3 fingertip MEMS tactile) 2. Fulai New Material (30k units to LinkerBot) 3. GelSight/Meta, Xela, Hanwei | Low-Med (no standard, many entrants; Luxshare win is the only volume win reported) | 002475.SZ, 605488.SS, 300007.SZ | Emerging, high-value per hand but pre-standard; **most speculative** |
| IMU | 1. TDK InvenSense 2. Bosch Sensortec 3. STMicro | Low (consumer MEMS oligopoly; ~$1-10 parts) | 6762.T, STM (Bosch private) | Fully commoditised; no humanoid-specific pricing power |
| Microphones/audio | Goertek (ASR front-end), TDK MEMS mics | Low | 002241.SZ, 6762.T | Commoditised; not investable on humanoids |

**Bottom line for a robotics-sensor basket:** best risk/reward on evidence found = **Hesai (HSAI)** and **RoboSense (2498.HK)** (verifiable humanoid orders + GAAP numbers), **LG Innotek (011070.KS)** (only supplier with confirmed mass production for a US humanoid major), **Sony (6758.T)** (indirect, low-beta). **Keli (603662.SS)** and **Orbbec (688322.SS)** carry the purest humanoid exposure but at valuations (~55x trailing earnings; ~50x annualised sales respectively) that already price mass production.

---

## (b) Per-component detail

### 1. Vision

**Who supplies camera modules on the majors (best available evidence):**
- **Tesla Optimus:** Samsung Electro-Mechanics (Semco) reported (Aug 2025) to supply camera modules combining **Sony image sensors** with Semco lenses/drive units; quantity and value "not yet determined" ([Investing.com](https://www.investing.com/news/stock-market-news/samsung-to-supply-camera-modules-for-teslas-optimus-bots--report-93CH-4166994), [Digitimes](https://www.digitimes.com/news/a20250805PD219/samsung-tesla-semco-optimus-hardware.html)). Optimus uses an eight-camera setup ([jparcvue Substack](https://jparcvue.substack.com/p/sony-6758-giving-ai-eyes-sonys-image)). Aug 2026: Tesla also picked Samsung and LG for Cybercab cameras ([SammyFans](https://www.sammyfans.com/2026/08/04/tesla-picks-samsung-and-lg-for-cameras-in-driverless-cars/)).
- **Figure:** LG Innotek agreed to supply camera modules to Figure AI (June 2025, [TrendForce](https://www.trendforce.com/news/2025/06/19/news-lg-innotek-reportedly-deepens-robotics-push-with-camera-module-supply-to-figure-ai/)). LG Innotek began mass production at its Paju plant for "a North American humanoid manufacturer" — tens of thousands of units, **5-8 camera modules per robot** (head + hands) ([BigGo](https://finance.biggo.com/news/cc81dee8-3389-4598-891a-d9af95ce5eaa)). Figure does not disclose the sensor vendor; Figure 03 has 2x frame rate, 1/4 latency, 60% wider FOV per camera and a palm camera in each hand ([Figure](https://www.figure.ai/news/introducing-figure-03)).
- **Boston Dynamics Atlas:** LG Innotek agreement (May 2025) to build an integrated vision unit (RGB cameras + 3D sensing modules) ([PR Newswire](https://www.prnewswire.com/news-releases/lg-innotek-and-boston-dynamics-to-create-the-next-generation-robot-vision-system-302452249.html)); BD also evaluating Korean lidar maker SOS Lab and Hyundai Mobis actuators ([Korea Herald](https://www.koreaherald.com/article/10791707)).
- **Unitree G1:** Intel RealSense D435i depth camera + DJI Livox Mid-360 lidar in the head ([robotsguide](https://robotsguide.com/robots/unitree-g1)); Hesai XT16 optional on Go2; Hesai lists Unitree as a JT128 customer (see lidar).
- **UBTech Walker S2:** binocular stereo vision + lidar; force & tactile sensors at wrists/fingertips; dual IMUs ([RoboZaps](https://blog.robozaps.com/b/ubtech-walker-s-review)). Sensor vendors not disclosed.
- **HONOR humanoid (MWC 2026):** Orbbec Gemini 330 stereo camera ([Orbbec](https://www.orbbec.com/news/honor-debuts-its-first-humanoid-robot-featuring-orbbecs-stereo-vision-3d-camera/)).
- Agility, Apptronik, 1X, Agibot, Fourier: **no vendor disclosure found** (n/f).

**Sony Semiconductor (6758.T)** — What: CIS (IMX series), also IMX636 event sensor with Prophesee. Moat: >50% global CIS share; sensor inside the Semco Optimus module. Financials: I&SS profit +37% in FY2025; FY26 I&SS forecast raised by ¥40bn to sales **¥2,110bn** and OI to **¥420bn**; group Q1 FY26 OI ¥476.5bn (+40% YoY) ([Investing.com](https://www.investing.com/news/company-news/sony-q1-fy2026-slides-operating-income-surges-40-on-gaming-sensors-93CH-4827007), [PetaPixel](https://petapixel.com/2026/08/06/sonys-image-sensor-division-is-booming/)). Sony guides a slight YoY decline in mobile sensor sales for FY26. Valuation: n/f. Risk: humanoids are immaterial to a ¥2tn segment; smartphone cycle dominates.

**OmniVision / Will Semiconductor (603501.SS)** — H1 2026 profit fell sharply on consumer/auto weakness, but machine vision/robotics/edge-AI revenue **+71%** ([Digitimes, 25 Aug 2026](https://www.digitimes.com/news/a20260825VL209/omnivision-technologies-cis-robotics-business-revenue.html)). Global-shutter sensors on NVIDIA Jetson/Holoscan ([OVT](https://www.ovt.com/press-releases/omnivision-high-performance-global-shutter-image-sensor-and-processor-now-available-on-nvidia-holoscan-and-nvidia-jetson-platforms/)). Absolute robotics revenue and valuation n/f. Risk: core CIS margin pressure; robotics still a small base.

**onsemi (ON)** — More relevant as **inductive position sensing** (NCS32100) for humanoid joints than as CIS; demoed humanoid position sensing at Embedded World 2026 ([onsemi](https://www.onsemi.com/company/events/embedded-world-2026)). Financials/valuation n/f.

**LG Innotek (011070.KS)** — CEO (CES 2026): humanoid sensing components in mass production 2026, "tens of billions of won" revenue ([Korea Times](https://www.koreatimes.co.kr/business/tech-science/20260210/lg-innotek-accelerates-camera-sensor-biz-for-humanoid-robots)). Competes head-to-head with Semco for "robot eye" modules ([BigGo](https://finance.biggo.com/news/1ff1e1c2-49a5-4c3b-a570-ffec444156f2)). Risk: Apple concentration; humanoid revenue <1% of group.

**Sunny Optical (2382.HK)** — H1 2026 revenue **RMB21.91bn (+11.5%)**, NP **RMB1.81bn (+9.9%)**; robotics vision has "stable shipments to leading customers", moving from modules to systems; strategy to extend to humanoids ([Investing.com](https://www.investing.com/news/company-news/sunny-optical-h1-2026-slides-paniot-surge-drives-diversification-93CH-4878303)). No humanoid customer named. Cowell: n/f.

**Orbbec (688322.SS)** — 3D structured-light/stereo/ToF cameras (Gemini 330); >70% share in Chinese service-robot 3D vision ([Orbbec](https://www.orbbec.com/company/)). Q1 2026 revenue RMB203m, net profit ex-items +531% YoY; but **H1 2026 revenue +0.5% to RMB437.6m** vs +104% in H1 2025 ([Bamboo Works](https://thebambooworks.com/orbbecs-booming-robotic-eye-sales-fail-to-wake-up-its-bottom-line/)). Market cap **RMB45.1bn (17 Aug 2026)** ([StockAnalysis](https://stockanalysis.com/quote/sha/688322/market-cap/)) → roughly 50x annualised sales. Risk: valuation vs. stalled growth; RealSense and integrated modules (LG Innotek) compete.

**RealSense (private)** — Spun out of Intel July 2025 with $50m Series A (Intel Capital, MediaTek); claims tech in **60% of AMRs and humanoids**; NVIDIA collaboration Oct 2025 ([BusinessWire](https://www.businesswire.com/news/home/20251008178223/en/RealSense-Spins-Out-from-Intel-Secures-$50-Million-and-Announces-Strategic-Collaboration-With-NVIDIA-to-Accelerate-Physical-AI-and-Robotics), [CNBC](https://www.cnbc.com/2025/07/11/intel-ai-robotics-realsense.html)). Design win: Unitree G1. Not investable directly.

**Prophesee (private)** — €20m raise June 2026 led by Critical Path Ventures; launched Mantara (drone detection) ([Image Sensors World](http://image-sensors-world.blogspot.com/2026/07/prophesee-raises-20-million.html)). EVK4 used in humanoid teleop research only ([arXiv](https://arxiv.org/abs/2607.29227)). Sony's IMX636 event sensor used in Sony AI's "Ace" robot ([Sony](https://www.sony-semicon.com/en/info/2026/2026042301.html)). Verdict: no production humanoid win; small raise signals limited traction.

**Lidar**
- **Hesai (HSAI):** Q2 2026 revenue **RMB860.8m (+21.9%)**, net income **RMB71m (+60%)**, 5th straight GAAP-profitable quarter; robotics lidar **142,371 units (+193%)**; FY26 robotics >500k units (vs ~240k in 2025); JT128 adopted by 50+ embodied-AI companies (Unitree, Robbyant, Galbot, Galaxea, Dexmal); humanoid orders from Galbot after July 2026 prototypes, revenue from Q3; Q3 guide RMB1.1-1.15bn; No.1 in China humanoid/quadruped lidar ([Hesai IR](https://investor.hesaitech.com/news-releases/news-release-details/hesai-group-reports-second-quarter-2026-unaudited-financial), [Yahoo](https://finance.yahoo.com/markets/stocks/articles/hesai-group-hsai-q2-2026-190146772.html)). Valuation: StockAnalysis shows mkt cap $2.92bn, trailing P/E 35.3, forward 22.6 — **date unverified, looks stale** ([StockAnalysis](https://stockanalysis.com/stocks/hsai/statistics/)). Risk: ASP deflation (JT16 for lawnmowers), US listing/geopolitics.
- **RoboSense (2498.HK):** H1 2026 revenue **~RMB1.02bn (+30.2%)**; total lidar 719,200 units (+169.6%), **robotics 282,600 units (+510%)**; No.1 global robotics lidar share 2025; new "eye/skin/muscle" lines — first joint module has orders in the tens of thousands, batch delivery Q4 2026 ([PR Newswire](https://www.prnewswire.com/apac/news-releases/robosense-reports-2026-interim-results-with-robotics-lidar-sales-volume-up-510-4-year-over-year-302861468.html), [Gasgoo](https://autonews.gasgoo.com/articles/news/robosense-interim-results-robotics-business-accounts-for-nearly-half-three-new-product-categories-accelerate-transformation-2093354315363475456)). Profitability and valuation n/f. Risk: still loss-making (unverified), robotics units are low-ASP.
- **Ouster (OUST):** REV8 native colour lidar ([TechCrunch](https://techcrunch.com/2026/05/04/ousters-new-color-lidar-is-coming-to-replace-cameras/)); acquired StereoLabs Feb 2026 for $35m + 1.8m shares ([TechCrunch](https://techcrunch.com/2026/02/09/lidar-maker-ouster-buys-vision-company-stereolabs-as-sensor-consolidation-continues/)); FieldAI collaboration June 2026. No humanoid OEM win named.
- **Luminar:** bankrupt; MicroVision bought lidar assets for $33m ([TechCrunch](https://techcrunch.com/2026/02/09/lidar-maker-ouster-buys-vision-company-stereolabs-as-sensor-consolidation-continues/)). Not investable for this theme.

### 2. Six-axis force/torque sensors
- **Usage:** Optimus Gen 2 uses 6-axis F/T at **wrists and ankles** (4 per robot) ([optimusk](https://optimusk.blog/blog/tesla-optimus-hardware-specs/)); UBTech Walker S2 has force sensors at wrists ([RoboZaps](https://blog.robozaps.com/b/ubtech-walker-s-review)). Keli confirms product series for humanoid wrist and ankle ([Futu](https://news.futunn.com/en/post/51666084/keli-sensing-technology-603662-sh-six-dimensional-force-torque-sensors)).
- **Pricing/cost-down:** average 6-axis F/T price fell from **RMB46,000/set (2017) to RMB32,000/set (2022)** (Fangzheng Securities via [Futu](https://news.futunn.com/en/post/36742138/fangzheng-securities-the-torque-sensor-market-exceeds-40-billion-yuan)); third-party BOM guides put humanoid F/T at **$200-1,000 per sensor** ([Black Scarab](https://www.blackscarab.ai/insights/humanoid-robot-anatomy-components-suppliers-guide)). 2025-26 Chinese vendor price points n/f (search budget). Market: humanoid 6D torque sensors **$642m (2025) → $4.64bn (2032), 32.4% CAGR** ([Research and Markets](https://www.researchandmarkets.com/reports/6055700/six-dimensional-torque-sensor-humanoid-robots)).
- **ATI / Novanta (NOVT):** ATI acquired for $172m upfront (2021) ([Robotics 24/7](https://www.robotics247.com/article/novanta_acquires_sensor_tooling_maker_ati_industrial_automation_172m/news)). Q2 2026: revenue **$265.8m**, adj EPS **$0.89** (beat), organic +9%, adj EBITDA +16%; first servo-drive orders for "hundreds of humanoid robots" in customer test facilities but "not a significant part" of margin; FY26 guide >15% reported growth; Riverpoint Medical deal takes medical to 60% of revenue ([Yahoo](https://finance.yahoo.com/markets/stocks/articles/novanta-inc-novt-q2-2026-030413946.html), [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-novanta-beats-q2-2026-estimates-and-lifts-outlook-93CH-4842339)). Valuation n/f. Risk: humanoid is a rounding error; ATI's premium pricing is the target of Chinese cost-down.
- **Keli Sensing (603662.SS):** FY2025 revenue **RMB1.558bn (+20.3%)**, NP **RMB341m (+30.7%)** ([Futu](https://news.futunn.com/en/post/72241009/keli-sensing-603662-annual-report-shows-impressive-performance-with-over)); market cap **~CN¥18.8bn** ([Simply Wall St](https://simplywall.st/stocks/cn/capital-goods/xssc-603662/keli-sensing-technology-ningboltd-shares)) → ~55x trailing earnings. Listed as an alternative Optimus 6-axis supplier post sample verification ([optimusk](https://optimusk.blog/blog/tesla-optimus-suppliers/)). Tactile sensors in R&D. Risk: humanoid F/T still a small share of a weighing-sensor business; valuation.
- **Bota Systems (private, CH):** MiniONE fingertip, Rokubi for humanoid bimanual manipulation ([Bota](https://botasys.com/)). **Hypersen (private, CN):** UR+ certified 6-axis, humanoid application page ([Hypersen](https://en.hypersen.com/application/six-axis-force-torque-sensors-the-force-sensing-technology-for-humanoid-robots/)). **Kunwei (private, CN):** KWR75/82 models; presented at China's Embodied Intelligence conference Mar 2026 ([Kunwei](https://www.czkunweitech.com/)). **Sensodrive (private, DE):** SensoJoint torque-controlled drives ([Sensodrive](https://www.sensodrive.de/products/torque-technology-senso-joint.php)). Dongguan Guangbo, Sichuan Zhongjun, Anpei, Robotiq, OnRobot: **no humanoid-specific evidence found** (n/f).
- Sep 18, 2026: Chinese robotics suppliers rallied on reports Tesla teams were in China auditing suppliers and placing additional Optimus orders ([Bloomberg](https://www.bloomberg.com/news/articles/2026-09-18/chinese-robotics-suppliers-rise-on-tesla-optimus-audit-report)).

### 3. Joint torque sensing and encoders
- **Dual-encoder requirement:** Optimus uses input (motor) + output (joint) encoders per actuator; Gen 2 has 28 actuators → ~56 encoders body, plus hands; encoder cost **$20-100 each** ([Black Scarab](https://www.blackscarab.ai/insights/humanoid-robot-anatomy-components-suppliers-guide), [optimusk](https://optimusk.blog/blog/tesla-optimus-hardware-specs/)). Renishaw/RLS confirm reduction-gear elasticity requires both motor and joint position ([Renishaw](https://www.renishaw.com/en/pal-robotics-integrates-magnetic-encoder-technology-into-robots-to-achieve-balance--43036)). Heidenhain's KCI 120 Dplus is a two-in-one dual encoder rated 400/600 m/s² ([Heidenhain](https://www.heidenhain.us/resources-and-news/innovative-dual-encoder-for-robots/)), though Heidenhain itself notes reliability no longer mandates dual encoders for fault checking.
- **Renishaw (RSW.L):** 9M FY26 revenue **£571.6m (+9.5%)**, Q3 record £206.0m; growth in enclosed optical and inductive encoders; RLS AksIM/Orbis in PAL Robotics knees/wrists/elbows ([DirectorsTalk](https://www.directorstalkinterviews.com/renishaw-reports-record-q3-and-sustained-growth-in-9m-fy2026/4121250649)). Humanoid revenue not disclosed; valuation n/f. Risk: premium encoders displaced by $20 chip-level magnetic/inductive parts at volume.
- **Allegro (ALGM):** 16-bit stray-field-immune magnetic encoders "to replace high-cost encoder solutions" in large joints; TMR + inductive + 48V gate drivers marketed for humanoids ([Allegro](https://www.allegromicro.com/en/applications/industrial/robotics)). Note: Allegro is an independent listed company, not Broadcom-owned (a search snippet conflated them). **Broadcom (AVGO):** AEAT-9922 programmable magnetic encoder and hollow-shaft absolute encoders for robots ([Broadcom](https://docs.broadcom.com/docs/magnetic-encoder-robotics-wp)). **ams OSRAM (AMS.SW):** AS5715R inductive position sensor for robot joints ([ams OSRAM](https://ams-osram.com/products/sensor-solutions/position-sensors/ams-as5715r-inductive-motor-control-position-sensor)). **onsemi:** NCS32100 inductive. **TDK:** n/f for encoders. **Yuheng Optics (002333.SZ):** named in humanoid encoder market reports; no financials or design wins found ([Data Insights](https://www.datainsightsmarket.com/reports/humanoid-robot-encoder-60877)). Netzer, Hengstler, Ruike: n/f. ZeroErr (private, CN) sells integrated actuator + magnetic encoder ([ZeroErr](https://www.zeroerr.com/)).
- Verdict: highest unit count per robot but the lowest ASP; chip-level vendors (Allegro, ams OSRAM, onsemi, TDK) will take volume; Renishaw/Heidenhain keep high-precision niches.

### 4. Tactile / e-skin
- **Luxshare (002475.SZ):** reported exclusive supplier of MEMS flexible tactile sensors for Optimus Gen3 fingertips plus full dexterous-hand structural parts; orders for 20,000 hand assemblies; 20,000 sets/month capacity in Dongguan ([androidshow.com exhibition site](https://en.androidshow.com/list_72/195.html)) — **source is a trade-show page; treat as unverified**. Gen 3 hands have force-feedback fingertip sensors; production hands targeted Q2-Q3 2026 ([Basenor](https://www.basenor.com/blogs/news/tesla-optimus-gen-3-hands-22-dof-50-actuators-explained)).
- **Fulai New Material (605488.SS):** 2nd-gen flexible tactile sensor ("true flexibility + full curvature + triaxial force"); >30,000 sensors delivered to LinkerBot, >30% of order fulfilled ([Gasgoo](https://autonews.gasgoo.com/articles/news/fulai-new-material-delivers-over-30000-tactile-sensors-to-linkerbot-2095113803636490241)); opened US unit, stock limit-up ([Yicai](https://www.yicaiglobal.com/news/fulai-new-material-jumps-by-limit-after-opening-us-unit-to-advance-haptic-sensing-business)). Financials/valuation n/f.
- **Hanwei Electronics (300007.SZ):** flexible piezoresistive/piezoelectric arrays; partnerships with ~30 robot integrators; new line H2 2025 ([Futu/Shanxi Securities](https://news.futunn.com/en/post/65245925/shanxi-securities-electronic-skin-is-key-to-humanoid-robot-interaction)). Financials n/f.
- **GelSight/Meta (private):** Digit 360 ([Robot Report](https://www.therobotreport.com/gelsight-meta-ai-release-digit-360-tactile-sensor-for-robotic-fingers/)). **Xela (private):** uSkin 3-axis patches ([Xela](https://xelarobotics.com/)). **RoboSense** launching "skin". **Keli** tactile in R&D. Sanctuary AI, Contactile: n/f.
- Market: e-skin **$756m by 2030**; flexible tactile demand 1.5m m² / CNY27.4bn by 2030 ([Shanxi Securities via Webull](https://www.webull.com/news/13893672901436416)). Verdict: no standard, no public-company volume win verified except the Luxshare report; most speculative category.

### 5. IMUs
- Commoditised consumer-MEMS oligopoly (ST, TDK InvenSense, Bosch); consumer IMU market ~$838m in 2026 ([Yole](https://www.yolegroup.com/press-release/stmicroelectronics-tdk-invensense-and-bosch-sensortec-mems-imus-all-you-need-to-know-from-the-technological-choices-to-the-design-wins-with-big-smartphone-oems/)). **Bosch Sensortec:** BMI423 (±32g/±4000 dps, robotics, available Q3 2026) and BMI5 platform (BMI563 for robotics) at CES 2026 ([Bosch](https://www.bosch-sensortec.com/en/news/precision-sensing-for-the-always-on-era-bosch-sensortec-launches-bmi423-imu.html)). **TDK InvenSense:** ICM-42688-P in RoboKit ([TDK](https://invensense.tdk.com/technology/robotics/)). **ST:** ST-NVIDIA humanoid proof-of-concept at Sensors Converge 2026 ([Fierce Sensors](https://www.fiercesensors.com/sensors/heres-more-sensors-converge-2026-scoop-st-and-microchip)). UBTech Walker S2 uses dual IMUs. Honeywell, ADI, Murata, Safran/Sensonor: **no humanoid design wins found** (n/f). Verdict: not investable on the humanoid theme.

### 6. Audio / other
- Goertek ASR front-end multi-mic arrays (98% near-field / 97% far-field accuracy) at CES 2026 ([PR Newswire](https://www.prnewswire.com/news-releases/goertek-showcases-full-stack-innovations-in-acoustics-and-sensing-at-ces-2026-302656965.html)); TDK MEMS mics for robotics ([TDK](https://www.tdk.com/en/featured_stories/entry_005.html)). Knowles: n/f. Not notable for valuation.

### Cross-cutting BOM context
Sensors are ~5-10% of humanoid BOM; Optimus Gen 2 BOM est. ~$46k with Chinese suppliers vs ~$131k without ([Black Scarab](https://www.blackscarab.ai/insights/humanoid-robot-anatomy-components-suppliers-guide)); McKinsey on supply-chain constraints ([McKinsey](https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins)). Optimus Gen3 reportedly 70% Chinese hardware content ([androidshow](https://en.androidshow.com/list_72/195.html), unverified).

---

## (c) Unverified / weak claims (flagged)
1. Luxshare "exclusive" Optimus Gen3 tactile sensor supplier, 20k hand orders, 70% Chinese content — single trade-show source; no Tesla or Luxshare confirmation found.
2. RealSense "60% of AMRs and humanoids" — company claim.
3. Hesai market cap $2.92bn / P/E 35x — StockAnalysis figure of unknown date; likely stale given revenue scale.
4. Orbbec RMB45.1bn market cap is dated 17 Aug 2026; P/E n/f.
5. Keli listed as "alternative" Optimus F/T supplier — from a blog aggregator (optimusk.blog), not Tesla.
6. Encoder ($20-100) and F/T ($200-1,000) unit costs — analyst blog estimates, not supplier quotes; 2025-26 Chinese 6-axis price points (widely reported in Chinese media as trending toward RMB2-5k) could not be searched due to budget exhaustion.
7. "Broadcom's Allegro" in a search snippet is wrong — Allegro (ALGM) is independent.
8. Figure 03 camera sensor vendor, Agibot/Fourier/Agility/Apptronik/1X sensor vendors — not disclosed anywhere found.
9. Missing financials: Novanta, Renishaw, Sony, Sunny valuation multiples; RoboSense profit; OmniVision absolute robotics revenue; Fulai/Hanwei/Yuheng H1 2026 results; Bosch/Honeywell/ADI humanoid wins.

## (d) Sources
- https://www.investing.com/news/stock-market-news/samsung-to-supply-camera-modules-for-teslas-optimus-bots--report-93CH-4166994
- https://www.digitimes.com/news/a20250805PD219/samsung-tesla-semco-optimus-hardware.html
- https://www.sammyfans.com/2026/08/04/tesla-picks-samsung-and-lg-for-cameras-in-driverless-cars/
- https://www.trendforce.com/news/2025/06/19/news-lg-innotek-reportedly-deepens-robotics-push-with-camera-module-supply-to-figure-ai/
- https://finance.biggo.com/news/cc81dee8-3389-4598-891a-d9af95ce5eaa
- https://finance.biggo.com/news/1ff1e1c2-49a5-4c3b-a570-ffec444156f2
- https://www.koreatimes.co.kr/business/tech-science/20260210/lg-innotek-accelerates-camera-sensor-biz-for-humanoid-robots
- https://www.prnewswire.com/news-releases/lg-innotek-and-boston-dynamics-to-create-the-next-generation-robot-vision-system-302452249.html
- https://www.koreaherald.com/article/10791707
- https://www.figure.ai/news/introducing-figure-03
- https://robotsguide.com/robots/unitree-g1
- https://blog.robozaps.com/b/ubtech-walker-s-review
- https://www.orbbec.com/news/honor-debuts-its-first-humanoid-robot-featuring-orbbecs-stereo-vision-3d-camera/
- https://www.orbbec.com/company/
- https://thebambooworks.com/orbbecs-booming-robotic-eye-sales-fail-to-wake-up-its-bottom-line/
- https://stockanalysis.com/quote/sha/688322/market-cap/
- https://www.businesswire.com/news/home/20251008178223/en/RealSense-Spins-Out-from-Intel-Secures-$50-Million-and-Announces-Strategic-Collaboration-With-NVIDIA-to-Accelerate-Physical-AI-and-Robotics
- https://www.cnbc.com/2025/07/11/intel-ai-robotics-realsense.html
- http://image-sensors-world.blogspot.com/2026/07/prophesee-raises-20-million.html
- https://arxiv.org/abs/2607.29227
- https://www.sony-semicon.com/en/info/2026/2026042301.html
- https://jparcvue.substack.com/p/sony-6758-giving-ai-eyes-sonys-image
- https://www.investing.com/news/company-news/sony-q1-fy2026-slides-operating-income-surges-40-on-gaming-sensors-93CH-4827007
- https://petapixel.com/2026/08/06/sonys-image-sensor-division-is-booming/
- https://www.digitimes.com/news/a20260825VL209/omnivision-technologies-cis-robotics-business-revenue.html
- https://www.ovt.com/press-releases/omnivision-high-performance-global-shutter-image-sensor-and-processor-now-available-on-nvidia-holoscan-and-nvidia-jetson-platforms/
- https://www.onsemi.com/company/events/embedded-world-2026
- https://www.investing.com/news/company-news/sunny-optical-h1-2026-slides-paniot-surge-drives-diversification-93CH-4878303
- https://investor.hesaitech.com/news-releases/news-release-details/hesai-group-reports-second-quarter-2026-unaudited-financial
- https://finance.yahoo.com/markets/stocks/articles/hesai-group-hsai-q2-2026-190146772.html
- https://stockanalysis.com/stocks/hsai/statistics/
- https://www.prnewswire.com/apac/news-releases/robosense-reports-2026-interim-results-with-robotics-lidar-sales-volume-up-510-4-year-over-year-302861468.html
- https://autonews.gasgoo.com/articles/news/robosense-interim-results-robotics-business-accounts-for-nearly-half-three-new-product-categories-accelerate-transformation-2093354315363475456
- https://techcrunch.com/2026/05/04/ousters-new-color-lidar-is-coming-to-replace-cameras/
- https://techcrunch.com/2026/02/09/lidar-maker-ouster-buys-vision-company-stereolabs-as-sensor-consolidation-continues/
- https://www.robotics247.com/article/novanta_acquires_sensor_tooling_maker_ati_industrial_automation_172m/news
- https://finance.yahoo.com/markets/stocks/articles/novanta-inc-novt-q2-2026-030413946.html
- https://www.investing.com/news/transcripts/earnings-call-transcript-novanta-beats-q2-2026-estimates-and-lifts-outlook-93CH-4842339
- https://news.futunn.com/en/post/36742138/fangzheng-securities-the-torque-sensor-market-exceeds-40-billion-yuan
- https://www.researchandmarkets.com/reports/6055700/six-dimensional-torque-sensor-humanoid-robots
- https://news.futunn.com/en/post/51666084/keli-sensing-technology-603662-sh-six-dimensional-force-torque-sensors
- https://news.futunn.com/en/post/72241009/keli-sensing-603662-annual-report-shows-impressive-performance-with-over
- https://simplywall.st/stocks/cn/capital-goods/xssc-603662/keli-sensing-technology-ningboltd-shares
- https://optimusk.blog/blog/tesla-optimus-suppliers/
- https://optimusk.blog/blog/tesla-optimus-hardware-specs/
- https://www.bloomberg.com/news/articles/2026-09-18/chinese-robotics-suppliers-rise-on-tesla-optimus-audit-report
- https://botasys.com/
- https://en.hypersen.com/application/six-axis-force-torque-sensors-the-force-sensing-technology-for-humanoid-robots/
- https://www.czkunweitech.com/
- https://www.sensodrive.de/products/torque-technology-senso-joint.php
- https://www.renishaw.com/en/pal-robotics-integrates-magnetic-encoder-technology-into-robots-to-achieve-balance--43036
- https://www.heidenhain.us/resources-and-news/innovative-dual-encoder-for-robots/
- https://www.directorstalkinterviews.com/renishaw-reports-record-q3-and-sustained-growth-in-9m-fy2026/4121250649
- https://www.allegromicro.com/en/applications/industrial/robotics
- https://docs.broadcom.com/docs/magnetic-encoder-robotics-wp
- https://ams-osram.com/products/sensor-solutions/position-sensors/ams-as5715r-inductive-motor-control-position-sensor
- https://www.datainsightsmarket.com/reports/humanoid-robot-encoder-60877
- https://www.zeroerr.com/
- https://en.androidshow.com/list_72/195.html
- https://www.basenor.com/blogs/news/tesla-optimus-gen-3-hands-22-dof-50-actuators-explained
- https://autonews.gasgoo.com/articles/news/fulai-new-material-delivers-over-30000-tactile-sensors-to-linkerbot-2095113803636490241
- https://www.yicaiglobal.com/news/fulai-new-material-jumps-by-limit-after-opening-us-unit-to-advance-haptic-sensing-business
- https://news.futunn.com/en/post/65245925/shanxi-securities-electronic-skin-is-key-to-humanoid-robot-interaction
- https://www.webull.com/news/13893672901436416
- https://www.therobotreport.com/gelsight-meta-ai-release-digit-360-tactile-sensor-for-robotic-fingers/
- https://xelarobotics.com/
- https://www.yolegroup.com/press-release/stmicroelectronics-tdk-invensense-and-bosch-sensortec-mems-imus-all-you-need-to-know-from-the-technological-choices-to-the-design-wins-with-big-smartphone-oems/
- https://www.bosch-sensortec.com/en/news/precision-sensing-for-the-always-on-era-bosch-sensortec-launches-bmi423-imu.html
- https://invensense.tdk.com/technology/robotics/
- https://www.fiercesensors.com/sensors/heres-more-sensors-converge-2026-scoop-st-and-microchip
- https://www.prnewswire.com/news-releases/goertek-showcases-full-stack-innovations-in-acoustics-and-sensing-at-ces-2026-302656965.html
- https://www.tdk.com/en/featured_stories/entry_005.html
- https://www.blackscarab.ai/insights/humanoid-robot-anatomy-components-suppliers-guide
- https://www.mckinsey.com/industries/industrials/our-insights/turning-humanoid-supply-chain-constraints-into-billion-dollar-wins
