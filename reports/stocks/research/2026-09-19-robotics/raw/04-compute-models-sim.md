# Humanoid / General-Purpose Robot Stack: Compute, Models, Simulation & Data
**Sell-side style equity research note — as of 19 Sep 2026**
*Method: 24 web searches (session cap reached); WebFetch to finance sites blocked, so figures come from search snippets and are cited by URL. Items I could not verify are in section (c). Note: several attempted searches (Mercor, Sanctuary, Formant, Unity financials, Agibot compute, Jetson install base, Gemini Robotics partner list, Genesis AI, AMD Versal, Scale AI physical-AI revenue) were blocked by the search cap — flagged as MISSING below.*

---

## (a) Summary table — layer → top vendors → moat → investable ticker

| Layer | Top 3 vendors (in order) | Moat rating | Investable ticker(s) | One-line thesis |
|---|---|---|---|---|
| **On-robot compute (high-end)** | 1. Nvidia Jetson Thor/Orin  2. Tesla AI5 (captive)  3. Qualcomm Dragonwing IQ10 | **Strong** (Nvidia); Qualcomm = challenger | NVDA, QCOM, (TSLA captive; Samsung 005930.KS / TSMC as foundries) | Every Western tier-1 humanoid (Figure, Agility, BD Atlas, 1X NEO) ships on Jetson; Thor at $2,999/module (1k qty) is the de-facto standard. Qualcomm IQ10 (700 TOPS, GA Sep-2026) is the first credible second source. |
| **On-robot compute (China / low-cost)** | 1. Rockchip RK3588  2. Horizon Robotics RDK S100  3. Nvidia Orin (grey/legacy) | Medium (cost, sovereignty) | 603893.SS, 9660.HK | Unitree G1, EngineAI, Galbot, Agibot X2, LimX ship RK3588; Rockchip H1-26 rev +40.6%, NP +61.7%. Horizon is still an ADAS company (2.2M chips shipped H1-26) with a robotics option. |
| **Mid-tier / niche compute** | 1. Ambarella CV72/CV75/CV8  2. Renesas RZ/V2H  3. Hailo (private) | Weak–Medium | AMBA, 6723.T | AMBA: ~15 robot design wins, ~$100M pipeline; 2nm CV8 first revenue FY28. Hailo pivoting to robotics but laying off ~10%. Mobileye (MBLY/INTC) bought Mentee for ~$900M — a robot-maker bet, not a chip win. |
| **Memory** | 1. SK hynix  2. Samsung  3. Micron | **Strong (oligopoly)** but robot share of demand tiny today | 000660.KS, 005930.KS, MU | Jetson Thor = 128GB; Tesla AI5 reportedly SK hynix + Samsung LPDDR5X. 60k humanoids in 2026 × ~128GB ≈ 7.7 PB — a rounding error vs HBM. Real robot memory upside is 2028+. |
| **Foundation models (robot brains)** | 1. Nvidia GR00T N1.7/N2  2. Google DeepMind Gemini Robotics 2  3. Physical Intelligence / Skild AI | **Most contestable** | NVDA, GOOGL (indirect); no public pure-play | ≥8 well-funded competing models (GR00T, Gemini, π0, Skild Brain, Helix 02, Redwood, Generalist Gen 1.5, Genesis, TRI LBM, Amazon, OpenAI). Open weights (GR00T, Gemini on-device) push pricing toward zero; value accrues to compute + data. |
| **Simulation / synthetic data** | 1. Nvidia Omniverse/Isaac Sim/Cosmos 3  2. Unity  3. Epic Unreal (private) | Strong (Nvidia); Weak (Unity/Epic in robotics) | NVDA, U | Cosmos 3 + Isaac Lab used by 1X, Agibot, Agility, BD, Figure, Hexagon, Neura, Skild, FieldAI. Synthetic 10k clips ≈ $10–15k vs ≥$500k real. Unity has no disclosed humanoid wins. |
| **Real-world data / teleop / labor** | 1. Scale AI (Meta-affiliated)  2. In-house (Tesla helmet rigs, Agibot exoskeletons, Apptronik Robot Park)  3. Long-tail teleop specialists | Weak (labor-intensive, commoditising) | None (SCALE private; META indirect) | Physical Intelligence appears on Scale's customer list. Leading labs are internalising data collection — bearish for third-party vendors. Mercor/Sanctuary: MISSING. |
| **Middleware / OS** | 1. ROS 2 (OSRF; Intrinsic→Google)  2. Foxglove  3. Formant / PickNik | Weak (open source) | GOOGL (indirect only) | Intrinsic folded into Google (Feb-2026) to work with DeepMind. Foxglove $40M Series B (Nov-2025; Bessemer). No investable pure-play. |
| **Cloud training capex** | 1. Nvidia (GPU)  2. CoreWeave  3. Nebius | Medium (contract lock-in) | NVDA, CRWV, NBIS | Both neo-clouds launched dedicated Physical-AI offerings (CRWV Field Engineering; NBIS + Nvidia end-to-end robotics platform, RoboForce customer). No disclosed Figure/PI/Skild contracts. |
| **Connectivity** | 1. Qualcomm  2. MediaTek  3. Broadcom | Weak / undifferentiated | QCOM, 2454.TW, AVGO | Wi-Fi 7 + 5G + UWB combo modules; MediaTek MT8893 (4nm, 48 TOPS NPU, Wi-Fi 7) is a robot-relevant SoC. Not a thesis driver. |

**Strongest moat:** On-robot compute + simulation, both owned by **Nvidia** (Jetson Thor + Isaac Sim/Lab + Cosmos + GR00T + Omniverse = full-stack lock-in; robots developed in Isaac Sim deploy natively on Jetson). Secondary: memory oligopoly (pricing power, but robot volumes immaterial until ~2028–30).
**Most contestable:** Robot foundation models. ~$25B+ of private valuation (PI ~$11B, Skild ~$14–15B, Generalist $3B, Genesis ~$3B pre) is chasing a layer where the two largest incumbents (Nvidia, Google) give models away or price them as loss-leaders for compute/cloud. Also contestable: teleop/human-data labor (internalised by the labs) and middleware (open source).

---

## (b) Detail with sourced figures

### 1. On-robot compute

**Nvidia (NVDA) — Jetson Thor / Orin**
- Role: SoC/module vendor + full software stack (JetPack, Isaac ROS, GR00T runtime).
- Product: Jetson AGX Thor — Blackwell GPU, 14-core Arm CPU, 128GB memory, up to 2,070 FP4 TFLOPS. GA announced Aug-2025. Pricing: **$2,999 per T5000 module (1,000-unit qty), $3,499 dev kit** (DCD; Nvidia newsroom).
- Design wins / moat evidence: early adopters Agility, Amazon Robotics, Boston Dynamics, Caterpillar, Figure, Hexagon, Medtronic, Meta; 1X, John Deere, OpenAI, Physical Intelligence "evaluating" (DCD). Confirmed on-robot: Boston Dynamics production Atlas "runs Jetson Thor onboard" (Engadget/Automate, CES Jan-2026); 1X NEO "powered by Jetson Thor" (1X/TNW); Agility Gen-6 Digit integrating Thor; Figure 02 used Orin, Figure 03 uses a "custom onboard inference chip developed in collaboration with Nvidia's Jetson platform" (RoboZaps — see unverified). Nvidia/Unitree open humanoid reference design (H2 Plus + Sharpa hands + Jetson Thor + GR00T) adopted by Ai2, ETH Zurich, Stanford, UCSD (Nvidia newsroom, May/Jun-2026).
- Financials: Q2 FY27 (qtr ended 26 Jul 2026): revenue **$96.2B** (+18% q/q, +106% y/y); Data Center $89.0B (+117% y/y); GAAP & non-GAAP GM 75.0%; GAAP EPS $2.46 / non-GAAP $2.22 (Nvidia newsroom, 26 Aug 2026). Huang guided ~70% FY28 revenue growth (CNBC). **Robotics/automotive segment figure not surfaced — MISSING.**
- Valuation: market cap ~**$5.37T** (Sep-2026, Capital.com). Forward P/E reported as 48.3 (valueinvesting.io, 13 Sep) vs 18.2–24.5 on other sites — inconsistent; treat as ~20–25x NTM on street numbers, higher on trailing.
- Biggest risk: robotics is <2% of revenue; Thor's $3k BOM is too expensive for sub-$20k consumer humanoids (Chinese OEMs already default to $100-class RK3588); Tesla, Figure and Chinese OEMs going custom.

**Tesla (TSLA) — AI5 (captive)**
- Taped out **15 Apr 2026**; dual-sourced — **Samsung 2nm (SF2T) at Taylor, TX** (trial wafer production started **15 Sep 2026**, ~2 months early) and **TSMC 3nm** (Electrek 13 Jul 2026; Tom's Hardware; autoevolution). Musk claims 3x Blackwell power efficiency at <10% cost (unverified). TrendForce (16 Apr 2026): AI5 reportedly uses SK hynix memory + Samsung LPDDR5X.
- Optimus status: Fremont Model S/X line converted to Optimus mid-2026, target 1M units/yr eventual capacity; ~1,000–1,200 units deployed internally as of mid-2026; **zero external sales**; Q2-26 call (5 Aug): production "soon"; B2B late-2026, consumer end-2027 targets (optimusk.blog / IIoT World — secondary sources).
- Investable angle: Samsung Foundry (005930.KS) and TSMC (2330.TW/TSM) as foundry beneficiaries; Samsung Taylor validation is the more incremental datapoint.
- Risk: repeated timeline slips; AI5 volume until 2027+.

**Qualcomm (QCOM) — Dragonwing IQ10 / RB series**
- IQ10: 18 Oryon cores, up to **700 TOPS**, announced CES Jan-2026; Robotics Reference Design (RRD) at Computex Jun-2026; early access Jun-2026, **commercial availability Sep-2026** (Qualcomm OnQ; embodiedglobal). Thundercomm TurboX IRB10 board. Legacy RB2/RB3 Gen2/RB5 platforms.
- Wins named: Advantech, APLUX, AutoCore, **Booster, Figure**, Kuka, Robotec.ai, **Neura Robotics** (4NE-1 humanoid, TechCrunch Mar-2026), VinMotion (Gadgeteer; Qualcomm). Qualcomm Ventures is a Figure Series C investor.
- Financials: FQ3-26 revenue **$9.95B** (-4% y/y, beat ~$9.67B est.); QCT Automotive record $1.59B (+61%); IoT $1.83B (+9%); handsets -20% (KuCoin/Futurum/Investing.com). Market cap ~**$188B** (TradingEconomics, Sep-2026).
- Moat: power efficiency + integrated 5G/Wi-Fi; weakness = no CUDA/Isaac ecosystem. Risk: handset decline dominates the P&L; robotics immaterial for years.

**Rockchip (603893.SS)**
- RK3588/RK3588S is the default brain in Chinese entry humanoids: **Unitree G1**, Agibot (Zhiyuan) Lingxi X2, LimX Oli, Gaoqing Pi (36Kr; arXiv Unitree G1 report). Also robot dogs, AGVs, cleaning/companion robots.
- H1-26: revenue **CNY 2.88B (+40.6%)**, net profit **CNY 859M (+61.7%)** (Digitimes 18 Aug 2026; Futu). Valuation: MISSING (not surfaced).
- Risk: smartphone-derived silicon (~6 TOPS class) caps it at "basic tasks"; upgrade cycle could go to Horizon/Nvidia/custom.

**Horizon Robotics (9660.HK)**
- Primarily ADAS; RDK S100 (100–128 TOPS) used in some domestic humanoids (36Kr). H1-26: revenue **RMB 2.055B (+32.9%)**, GM 66%, ~2.2M chips shipped, adj. net loss **RMB 1.67B**; breakeven targeted ~2028; mgmt raised medium-term revenue CAGR guide 50%→60% (Investing.com; Gasgoo, 31 Aug 2026). Market cap ~**HK$72.4B** (stockanalysis, late Aug). Risk: cash burn; robotics is optional upside, not core.

**Ambarella (AMBA)**
- FQ2-27 (reported 3 Sep 2026): revenue **$108.1M (+13.2%)**, non-GAAP GM 59.3%, EPS $0.18; FY27 guide +10–15%. **~15 robot design wins, ~$100M pipeline**, mostly on 5nm CV72/CV75; 2nm CV8 semi-custom first revenue FY28; showed CV72 quadruped (Motley Fool transcript; Seeking Alpha). Memory supply flagged as risk. Valuation: MISSING.

**Renesas (6723.T)** — RZ/V2H (DRP-AI3, 4×A55 + 2×R8) marketed for humanoid real-time control (Renesas site); no disclosed humanoid wins found. Low-relevance peripheral MCU supplier.

**Hailo (private)** — $344M raised; unicorn; refocusing on robotics/physical AI while cutting ~10% of staff; raising a new round (CTech). No humanoid wins found.

**Intel / Mobileye (INTC / MBLY)** — Mobileye to acquire humanoid startup **Mentee Robotics for ~$900M**; Intel spun out RealSense (depth cameras) into robotics; Intel retains ~23% of Mobileye (MarketScreener; Yahoo). This is a robot-maker bet, not a compute win. **AMD Versal: no robotics evidence found — MISSING.**

**Memory (MU, 000660.KS, 005930.KS)**
- Content: Jetson Thor carries **128GB**; AI5 uses SK hynix + Samsung LPDDR5X (TrendForce). Micron-bull piece argues humanoids need ~10x a self-driving car's memory (24/7 Wall St, 11 Aug 2026 — precise GB/robot figure MISSING).
- Volumes: humanoid shipments **19,100 units H1-26 (+272% y/y)**, ~60k FY26, 500k by 2030 (same source). Even at 128GB, 60k units ≈ 7.7 PB — immaterial vs. AI-server DRAM.
- Financials: SK hynix Q2-26 revenue **KRW 79.32T (+257% y/y)**, OP **KRW 60.54T**, **76% operating margin** (SK hynix newsroom). Micron FQ3-26 revenue **$41.46B** (vs $9.30B y/y); FY26 consensus ~$129.7B; FQ4 reports 30 Sep 2026 (Micron IR; Motley Fool). Samsung LPDDR5X-PIM (Hot Chips 2026) 3x inference speed/8x bandwidth — relevant to on-robot inference. Risk: robot demand is a 2028+ story; memory cycle dominated by HBM.

### 2. Foundation models

| Vendor | Model / status | Adoption evidence | Valuation / funding | Risk |
|---|---|---|---|---|
| **Nvidia** | GR00T N1.7 (commercial license); **N2** (world-action model, DreamZero-based, >2x success on novel tasks vs VLAs) due by end-2026 | N1.7 licensees: Agibot, Humanoid, LG Electronics, Neura, Noble Machines; reference humanoid used by Ai2/ETH/Stanford/UCSD | n/a (loss-leader for Jetson/DGX) | Models are open → no direct revenue |
| **Google DeepMind (GOOGL)** | **Gemini Robotics 2** (30 Jul 2026): VLA + ER 2 (public via Gemini API/AI Studio) + **On-Device 2** (adapts to new bodies in hours) | Apptronik Apollo 2 whole-body demo; Apptronik "Robot Park" data facility with DeepMind (Jul-2026); Boston Dynamics Atlas fleet shipping to DeepMind; Intrinsic merged into Google | Alphabet also owns CapitalG stake in Physical Intelligence | Partner OEMs may prefer vendor-neutral models |
| **Physical Intelligence (private)** | π0 / π0.5 VLA | Customer of Scale AI; evaluating Jetson Thor | Series B **$600M at $5.6B** (Nov-2025, CapitalG-led; Sequoia, OpenAI, Lux, NVDA, T. Rowe); **~$1B at ~$11B reported Mar-2026, unconfirmed** (Dealroom; The Elec) | No disclosed revenue |
| **Skild AI (private)** | Skild Brain ("omni-bodied") | Uses Nvidia Cosmos for data gen; investors incl. Samsung, LG, Schneider, Salesforce | **$1.4B Series C at >$14B** (14 Jan 2026, SoftBank-led; NVentures, Bezos) — some sources say $15B/Mar-2026; ~$30M 2025 revenue (Sacra, unaudited) | 470x trailing revenue |
| **Figure (private)** | Helix 02 (Jan-2026): single network for locomotion + manipulation; retired Figure 02 fleet | BMW Spartanburg pilot | Series C **>$1B at $39B post** (Sep-2025; Parkway, Brookfield, NVDA, Intel Capital, Qualcomm Ventures) | See unverified BMW claims |
| **Tesla** | Optimus in-house VLA on AI4/AI5; data via multi-camera helmet rigs (moved off VR teleop) | Internal only | n/a | Zero external revenue |
| **1X (private)** | Redwood — 160M-param VLM at ~5 Hz on-robot (Jun-2025) | NEO: $20k or $499/mo; >10k pre-orders; 10k/yr Hayward capacity; no verified customer delivery as of 16 Jul 2026 | $100M raised; OpenAI Startup Fund | Delivery slippage |
| **Generalist AI (private)** | Gen 1.5 — learns tasks from 3–12s video demos | Nvidia-backed | $400M Series B at $2B (Jun-2026, Radical) + ~$200M extension at **$3B** (Aug-2026, 8VC) (TechCrunch) | Early |
| **Genesis AI (private)** | Model + physics sim | — | In talks for ~$500M at ~$3B pre (aibusinessweekly) | Unconfirmed |
| **OpenAI** | Confirmed building own humanoid + control model (Altman, Sep-2026); robotics division re-staffing after Kalinowski's Mar-2026 exit (Forbes 3 Sep 2026) | — | — | Late entrant |
| **Amazon (AMZN)** | DeepFleet (fleet coordination, +10% travel efficiency; 1M robots deployed); agentic FM for Proteus; Covariant team/IP licensed | Internal | — | Captive, not sold |
| **Toyota Research Institute** | Large Behavior Models (~80% less data); LBM on Boston Dynamics Atlas | BD/Hyundai | — | Research |

**Where value accrues:** to the owners of (i) the deployment hardware (Nvidia Jetson), (ii) proprietary embodied data at scale (Tesla, Figure, Amazon, Apptronik/DeepMind), and (iii) training compute. **No public pure-play model vendor exists**; the closest listed exposure is NVDA (open models sold via silicon) and GOOGL (Gemini API + CapitalG stake in PI + DeepMind/Intrinsic).

### 3. Simulation & synthetic data
- **Nvidia**: Cosmos 3 (GTC Mar-2026) unifies world generation, vision reasoning, action simulation; Physical AI Data Factory Blueprint (Cosmos Curator/Transfer/Reason + OSMO). Users: 1X, Agibot, Agility, Agile Robots, Boston Dynamics, Figure, Hexagon, Humanoid, Mentee, Neura (Isaac Sim/Lab + Cosmos); FieldAI and Skild build brains on Cosmos (Nvidia newsroom; TrendForce). Cost datapoint: 10k synthetic clips ≈ **$10–15k GPU-hours vs ≥$500k** real collection (Spheron). Moat: Isaac Sim → Jetson deployment path + OpenUSD; this is Nvidia's second-strongest lock-in.
- **Unity (U)**: positioned as mature rendering ecosystem for robotics/AV training environments but requires commercial licensing; no humanoid design wins surfaced; Q2-26 financials MISSING (search cap).
- **Epic Unreal (private)**: no robotics-specific evidence surfaced.
- **Real-world data / labor**: Scale AI runs demonstration-capture programs; Physical Intelligence on customer list (Troveo/Teahose). Teleop yields 5–50 episodes/hr; Agibot uses exoskeleton capture; Tesla uses helmet camera rigs; Apptronik built "Robot Park" with DeepMind. Trend: labs internalise data → weak moat for third-party vendors. **Mercor, Sanctuary AI: MISSING.**

### 4. Middleware / OS
- ROS 2: OSRF retains ROS/Gazebo; Intrinsic bought OSRC (Dec-2022) and **joined Google in Feb-2026**, working with DeepMind/Gemini/Cloud (TechCrunch 25 Feb 2026). Investable only via GOOGL, immaterially.
- **Foxglove**: $40M Series B (Nov-2025, Bessemer; Eclipse, Amplify); customers Nvidia, Amazon, Anduril, Wayve, Dexterity. Private.
- **Formant, PickNik (MoveIt Pro)**: private; funding MISSING. Verdict: no investable middleware pure-play; open-source economics.

### 5. Cloud training capex
- **CoreWeave (CRWV)**: Physical AI page (policy training, synthetic data, sim-to-real); new Physical AI Field Engineering service; "doubling down" per Yahoo (Sep-2026; SiliconANGLE 18 Sep). Named robotics customers: none surfaced.
- **Nebius (NBIS)**: Nvidia collaboration for end-to-end robotics cloud; customer **RoboForce** (70% faster pipeline setup on Blackwell). No Figure/PI/Skild disclosure.
- Hyperscalers: Google Cloud (Intrinsic/DeepMind), AWS (Amazon Robotics internal). **No disclosed robotics-lab contract values — MISSING.**

### 6. Connectivity
- Industry moving to Wi-Fi 7 + 5G + UWB combo modules for humanoids (RoboticsTomorrow, Aug-2026). MediaTek MT8893 (4nm, 48 TOPS NPU, 5G, Wi-Fi 7); MediaTek showing 6G-for-humanoids test platform (Computex 2026). Qualcomm embeds connectivity in IQ10. Broadcom: only generic Wi-Fi 7 M.2 modules. Verdict: no robot-specific moat; QCOM is the only vendor bundling compute + radio.

---

## (c) Unverified / conflicting claims (do not cite without confirmation)
1. **Figure "Q1 2026 earnings call", 120 Figure 03 units at BMW, -73% inventory errors, +18% throughput** — from an AI-content blog (artificialintelligenceherald); Figure is private and does not hold earnings calls. Treat as fabricated until confirmed.
2. **Figure 03 "custom inference chip with Nvidia"** — RoboZaps blog only.
3. **Physical Intelligence ~$11B / $11.2B** — reported (Dealroom, The Elec), not confirmed by the company; last confirmed is $5.6B (Nov-2025).
4. **Skild AI: $14B (Jan-2026 BusinessWire) vs $15B (Mar-2026)**; "~$30M 2025 revenue" (Sacra estimate).
5. **Tesla AI5 "3x Blackwell efficiency at <10% cost"** — Musk claim, no benchmark.
6. **Optimus 1,000–1,200 units deployed; 1M/yr Fremont capacity** — fan-site aggregation (optimusk.blog, IIoT World).
7. **Nvidia forward P/E** — sources range 18x–48x; not reconciled.
8. **Unitree day-one move: +460% (Yahoo) vs +629% (valueaddvc)**; ~$50B post-debut cap based on the 845 yuan close.
9. **Humanoid shipments 19,100 H1-26 / 60k FY26 / 500k 2030** — single secondary source (24/7 Wall St citing an unnamed tracker).
10. **Genesis AI $500M at ~$3B** — "in talks" only.
11. **Horizon market cap HK$72.4B** — date-stamped "as of today" on stockanalysis; may be stale.
12. **Rockchip valuation, Ambarella market cap, Unity Q2-26, Mercor/Sanctuary/Formant status, AMD Versal robotics, Nvidia robotics-segment revenue, Micron GB-per-robot** — MISSING (search budget exhausted).

## Bonus datapoint — Unitree (688836.SS) as the listed OEM read-through
Priced at CNY 150.8 (≈CNY 61B cap), listed 19 Aug 2026 on STAR; 2025 revenue **CNY 1.699B**, adj. NP **CNY 590M**, GM 60.1%; humanoids = CNY 868M (51.8% of revenue); H1-26 revenue guide CNY 1.05–1.13B (+36–45%); raised ~CNY 6.1B; DeepSeek a cornerstone investor (SSE; Caixin; KraneShares). Uses Rockchip RK3588 (G1) and Jetson Thor (H2 Plus reference design) — the clearest public proof that both chip tiers coexist.

---

## (d) Sources
**Compute**
- https://www.datacenterdynamics.com/en/news/nvidia-launches-jetson-thor-compute-modules-for-humanoid-robots/
- https://nvidianews.nvidia.com/news/nvidia-blackwell-powered-jetson-thor-now-available-accelerating-the-age-of-general-robotics
- https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world
- https://nvidianews.nvidia.com/news/nvidia-open-humanoid-robot-reference-design
- https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-second-quarter-fiscal-2027
- https://www.cnbc.com/2026/08/26/nvidia-nvda-earnings-report-q2-2027-live-updates.html
- https://capital.com/en-int/markets/shares/nvidia-corp-share-price/market-cap
- https://valueinvesting.io/NVDA/metric/forward-pe
- https://electrek.co/2026/07/13/samsung-taylor-fab-tesla-ai5-chip-2nm/
- https://www.tomshardware.com/tech-industry/artificial-intelligence/teslas-ai5-with-2nm-class-node-tapes-out-at-samsung-foundry-production-starts-soon-months-after-tsmc-tape-out
- https://www.autoevolution.com/news/tesla-s-ai5-chip-enters-trial-production-as-samsung-gets-the-taylor-fab-running-275799.html
- https://www.trendforce.com/news/2026/04/16/news-tesla-ai5-reportedly-uses-sk-hynix-memory-samsung-lpddr5x-samsung-sf2t-process-applied-ahead-of-ai6/
- https://optimusk.blog/blog/tesla-q2-2026-earnings-optimus-update/
- https://www.iiot-world.com/smart-manufacturing/tesla-optimus-manufacturing-2026/
- https://www.qualcomm.com/news/onq/2026/06/dragonwing-iq10-robotics-reference-design
- https://www.automate.org/robotics/news/ces-2026-qualcomm-targets-nvidia-jetson-with-new-robotics-developer-platform
- https://techcrunch.com/2026/03/09/qualcomms-partnership-with-neura-robotics-is-just-the-beginning
- https://the-gadgeteer.com/2026/06/01/qualcomm-computex-snapdragon-c-dragonwing-iq10-robotics/
- https://www.kucoin.com/blog/qualcomm-q3-2026-earnings
- https://futurumgroup.com/insights/qualcomm-q3-fy-2026-automotive-growth-offsets-handset-weakness/
- https://tradingeconomics.com/qcom:us:market-capitalization
- https://eu.36kr.com/en/p/3473485924538759
- https://arxiv.org/html/2509.14096v1
- https://www.digitimes.com/news/a20260818VL215/rockchip-profit-chips-revenue-2026.html
- https://news.futunn.com/en/post/77785424/rockchip-603893-sh-announced-its-semi-annual-results-with-net
- https://www.investing.com/news/transcripts/earnings-call-transcript-horizon-robotics-posts-strong-h1-2026-growth-as-losses-continue-93CH-4882954
- https://autonews.gasgoo.com/articles/icv/horizon-robotics-2026-interim-report-gross-margin-maintains-high-of-66-2095039844043800577
- https://stockanalysis.com/quote/hkg/9660/market-cap/
- https://www.fool.com/earnings/call-transcripts/2026/09/09/ambarella-amba-q2-2027-earnings-call-transcript/
- https://seekingalpha.com/news/4558382-ambarella-targets-10-percentminus-15-percent-revenue-growth-in-fiscal-2027-as-edge-ai
- https://www.renesas.com/en/applications/industrial/robotics/humanoid-robots
- https://www.calcalistech.com/ctechnews/article/hyzk11etvwx
- https://www.marketscreener.com/news/mobileye-to-acquire-humanoid-robotics-startup-mentee-for-900-million-ce7e59dfde89f023
- https://247wallst.com/investing/2026/08/11/humanoid-robots-need-10x-the-memory-of-a-self-driving-car-micron-is-positioned-to-win/
- https://news.skhynix.com/en/q2-2026-business-results/
- https://www.fool.com/investing/2026/09/18/micron-is-poised-to-surge-after-its-fiscal-year-en/
- https://investors.micron.com/news/press-release/2026/Micron-Technology-to-Report-Fiscal-Fourth-Quarter-Results-on-September-30-2026/default.aspx
- https://www.tomshardware.com/pc-components/dram/hot-chips-2026-samsung-makes-lpddr5x-smart-with-logic-unit-in-memory-lpddr5x-pim-is-3-01x-faster-than-lpddr5x-in-ai-inference-with-8x-the-bandwidth
- https://www.forbes.com/sites/jonmarkman/2026/05/19/the-nvidia-arm-chip-stack-winning-the-humanoid-robot-boom/

**Models**
- https://github.com/Nvidia/Isaac-GR00T
- https://robocloud-dashboard.vercel.app/learn/blog/gr00t-world-action-models-2026
- https://deepmind.google/blog/gemini-robotics-2-brings-whole-body-intelligence-to-robots/
- https://www.therobotreport.com/google-deepmind-says-gemini-robotics-2-enables-full-body-control/
- https://roboticsandautomationnews.com/2026/07/06/apptronik-launches-robot-park-to-train-apollo-humanoid-robots-with-google-deepmind/
- https://app.dealroom.co/news/feed/physical-intelligence-raises-1-6b-across-two-rounds-valuation-hits-11-2b
- https://www.teahose.com/guides/physical-intelligence-valuation
- https://www.businesswire.com/news/home/20260114335623/en/Skild-AI-Raises-$1.4B-Now-Valued-Over-$14B
- https://www.techcrunch.com/2026/01/14/robotic-software-maker-skild-ai-hits-14b-valuation/
- https://sacra.com/c/skild-ai/
- https://www.roboticscenter.ai/companies/figure-ai
- https://blog.robozaps.com/b/figure-03-review
- https://artificialintelligenceherald.com/robotics/figure-ai-humanoid-robots-2026-capabilities-pricing-future
- https://thenextweb.com/news/1x-neo-humanoid-factory-hayward-10000-home-robots
- https://blog.robozaps.com/b/1x-neo-review
- https://techcrunch.com/2026/08/25/robotics-startup-generalist-reaches-3b-valuation-sources-say/
- https://siliconangle.com/2026/06/04/generalist-ai-raises-400m-2b-valuation-build-general-intelligence-real-world/
- https://aibusinessweekly.net/p/genesis-ai-500-million-robotics-funding
- https://www.forbes.com/sites/johnkoetsier/2026/09/03/openai-is-making-a-humanoid-robot-everyone-should-have-one/
- https://www.aboutamazon.com/news/operations/amazon-million-robots-ai-foundation-model
- https://www.tri.global/our-work/large-behavior-models
- https://pressroom.toyota.com/ai-powered-robot-by-boston-dynamics-and-toyota-research-institute-takes-a-key-step-towards-general-purpose-humanoids/

**Simulation / data / middleware / cloud / connectivity / OEM**
- https://www.trendforce.com/news/2026/03/19/insights-nvidia-expands-robotics-ecosystem-at-gtc-as-physical-ai-moves-toward-large-scale-deployment/
- https://www.spheron.network/blog/deploy-nvidia-cosmos-gpu-cloud-synthetic-data/
- https://blogs.nvidia.com/blog/gtc-2026-virtual-worlds-physical-ai/
- https://www.blackcoffeerobotics.com/blog/which-robot-simulation-software-to-use
- https://www.troveo.ai/resources/robotics-training-data-companies
- https://www.teahose.com/guides/robotics-training-data
- https://www.shaip.com/blog/robot-training-data-strategy/
- https://techcrunch.com/2026/02/25/alphabet-owned-robotics-software-company-intrinsic-joins-google
- https://www.therobotreport.com/foxglove-raises-40m-scale-data-platform-roboticists/
- https://www.coreweave.com/industries/physical-ai
- https://siliconangle.com/2026/09/18/cloud-platform-coreweave-ai-thecube-fullyconnected/
- https://nebius.com/newsroom/nebius-teams-with-nvidia-to-build-cloud-for-robotics-and-physical-ai
- https://www.roboticstomorrow.com/article/2026/08/the-invisible-nervous-system-wireless-connectivity-for-physical-ai-and-humanoids/26947
- https://www.mediatek.com/iot/modem-based-iot/mt8893
- https://www.mediatek.com/computex2026
- https://www.engadget.com/big-tech/boston-dynamics-unveils-production-ready-version-of-atlas-robot-at-ces-2026-234047882.html
- https://www.automate.org/robotics/industry-insights/boston-dynamics-to-begin-production-on-redesigned-atlas-humanoid-in-2026
- https://english.sse.com.cn/news/newsrelease/voice/c/c_20260806_10828128.shtml
- https://www.caixinglobal.com/2026-08-18/unitree-to-debut-at-61-billion-yuan-valuation-in-closely-watched-shanghai-ipo-102475173.html
- https://finance.yahoo.com/markets/stocks/articles/unitree-robotics-stock-soars-460-111514463.html
- http://www.china.org.cn/2026-06/03/content_118529304.shtml

