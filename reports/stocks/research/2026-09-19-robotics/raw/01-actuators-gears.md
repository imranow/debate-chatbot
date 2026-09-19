# Humanoid Actuator & Reduction-Gear Supply Chain — Sell-side Style Research Note
**Date:** 19 Sep 2026. **Method:** 32 web searches (search budget hit its 200/session cap; all WebFetch attempts to 36kr, Substack, Schaeffler IR, Barchart, BuzzHK were blocked by the egress proxy). Figures below are from search snippets only and should be re-verified against primary filings before use. Items I could not confirm are in section (c).

**Important naming note:** "Leaderdrive / Leader Harmonious Drive (688017.SS)" and "Green Harmonic (绿的谐波 / Suzhou Green Harmonic Drive)" are the **same company** — 688017.SS is 绿的谐波. Sources use both names. I treat them as one entity throughout.

---

## (a) Summary table

| Component | Top-3 suppliers (est. rank) | Moat rating | Investable ticker(s) | Bottlenecked or commoditising? |
|---|---|---|---|---|
| Strain-wave / harmonic gears | 1. Harmonic Drive Systems 2. Leaderdrive/Green Harmonic 3. Laifual (then Nidec DT, Shuanghuan/Huandong, CTKM) | HDS: **strong** (precision/brand, but eroding in China); Leaderdrive: **medium-strong** in China; Laifual: **weak-medium** (share-grab via price) | 6324.T, 688017.SS, 3952.HK, 002472.SZ, 6594.T (Nidec, small exposure) | **Commoditising fast in China** (ASPs down ~40% since 2017; >30 domestic makers); premium/industrial tier still tight (machine-tool lead times ~12 months) |
| Planetary roller screws (linear actuators) | 1. GSA + Rollvis (Ziegler Group, Swiss, private) 2. Ewellix/Schaeffler 3. Chinese cluster: Hengli, Wuzhou Xinchun, Beist, Xinjian/Seenpin (private, pre-IPO) | Swiss pair: **strong** (>50% global share, 85%+ yields vs ~60% China); Schaeffler: **medium**; Chinese: **weak today, improving** | SHA.DE, 601100.SS, 603667.SS, 603009.SS, 002472.SZ (indirect), 601689.SS/002050.SZ (actuator integrators) | **Genuinely bottlenecked** (McKinsey: more acute than harmonics; 26-week lead-time episode in 2023; thread-grinder scarcity; yields) — but Chinese capacity additions of 3–5m units/yr are coming in 2026–27 |
| Cycloidal / RV reducers | 1. Nabtesco 2. Sumitomo Heavy 3. Shuanghuan / Zhongda Leader | Nabtesco: **strong** (~60% global RV share, Morningstar wide-moat); SHI: **medium**; Chinese: **weak-medium** | 6268.T, 6302.T, 002472.SZ, 002896.SZ | Industrial RV tight (Changzhou plant at 100% utilisation); humanoid-specific miniature RV is nascent — Nabtesco only ~28% share there |
| Frameless torque motors / joint modules | 1. Kollmorgen (Regal Rexnord) / TQ RoboDrive / Maxon (West) 2. Inovance & Chinese cluster (Step, Leadshine, Dongjie) 3. In-house (Unitree, Tesla design) | Western: **medium** (know-how, but volumes leaving); Inovance: **medium**; in-housing is the norm at scale | RRX, ALNT, MOG.A, 6594.T, 300124.SZ, 688836.SS (Unitree, vertically integrated) | **Commoditising** — motors are the most in-housed part of the joint; value migrates to integrated actuator assemblers (Tuopu, Sanhua) |
| Cross-roller / thin-section bearings | 1. IKO (Nippon Thompson) 2. THK 3. Schaeffler / NSK / SKF-Kaydon; Chinese entrant Changsheng | Japanese: **medium-strong** (precision, 14–20 CRBs per humanoid); Chinese: **weak** | 6480.T, 6481.T, 6471.T, SHA.DE, SKF-B.ST, 300718.SZ | Not reported as bottlenecked; incumbents compete on lightweighting/sealing |

**Where the money is bottlenecked today:** planetary roller screws (precision thread grinding, heat treatment, yields) and — one level up — the **precision grinding machine tools** needed to make both screws and flexsplines (high-end machine-tool delivery reported at ~12 months). **Where it is commoditising:** harmonic reducers in China, frameless motors, and (increasingly) RV reducers below Nabtesco's quality tier.

---

## (b) Per-component detail

### 1. Strain-wave / harmonic gears

**Demand frame.** Tesla Optimus uses 28 actuators — 14 rotary (frameless motor + harmonic reducer + sensors) and 14 linear (frameless motor + planetary roller screw). Vendors cite ~14 harmonic reducers per humanoid. China's 2025 robotic harmonic reducer market was ~1.36–1.4m units; humanoids absorbed ~179k (~13%). CIC projects China volume to 20.7m units by 2030 (72% CAGR). Both Leaderdrive and Laifual say humanoids are ~30% of their business. TrendForce expects >50k global humanoid shipments in 2026 (+700% YoY).

**Harmonic Drive Systems (6324.T)** — inventor-lineage incumbent (Musser patent 1955; core patents long expired; a later "harmonic drive motor" patent expired 19 Feb 2025 — the patent estate is now about process/tooth-profile know-how, not exclusivity).
- Financials: FY3/2026 saw a V-shaped recovery (ordinary profit reported +1,555% YoY after an upward revision of +66.7% vs the August forecast). June-2026 quarter: sales ¥16.7bn (+24% YoY), OPM 11%, orders ¥24.1bn (+56% YoY, cited as +55.7% on semiconductor and AI-robot demand). FY3/2027 guidance raised to revenue ¥74.5bn (from ¥68bn) and OP ¥8.5bn (from ¥6.2bn), OPM 11.4%.
- Capacity: Beverly, MA (Harmonic Drive LLC) +13% completed Dec 2025 ($15.1m), further +33% by Dec 2026 ($8.45m). Hotaka/Ariake (Azumino, Nagano) capex ~$26m to Mar 2027, mostly maintenance/IT — i.e., **no large Japanese greenfield expansion found**.
- Valuation (12 Sep 2026): ¥5,790, mkt cap ¥548bn, P/E ~186x TTM, yield 0.35%. EV/sales not found (≈7x on FY3/27 guidance if EV ≈ mkt cap — my arithmetic, unverified).
- Biggest risk: Chinese price competition (Chinese domestic share of the harmonic market rose from ~15% in 2022 to ~38% by 1Q24; Leaderdrive claims 30–40% lower prices) plus Tesla/US humanoids sourcing from China.

**Leaderdrive / Green Harmonic (688017.SS)** — China's #1.
- FY2025: revenue RMB571m (+47.3%); harmonic reducer & metal parts revenue RMB476m (+46.4%); 425,158 reducers shipped (+72.5%); attributable net profit +121.4%. Domestic share 27.5% (2025); claimed 80–90% share among Chinese humanoids that use harmonics (up from ~70%). Management guided 2026 revenue approaching RMB1bn.
- Capacity: ~600–700k units end-2025; 70k/month May 2026, 80k/month June, target 120k/month by end-2026 (1.44m annualised) and ≥2m units in 2027. New Suzhou plant (500k units) starts 2026 — described as sufficient for Optimus' initial ramp. Reported as Tesla's primary Chinese harmonic supplier, targeting ~60% of Optimus reducer supply in 2026 at 30–40% below Japanese pricing (**unverified**). Operating cash flow weakened in 2025 on capex, inventory and supplier prepayments.
- Price trend: Bernstein data — ASP RMB1,900 (2017) → RMB1,100 (2024), i.e., ~-42%.
- Valuation: RMB279.8, mkt cap RMB51.3bn, P/E ~364x TTM (EPS RMB0.79), yield 0.07%. ≈50x 2026E sales on the RMB1bn guide (my arithmetic).
- Biggest risk: price war (Laifual explicitly cutting price to take share) and Tesla volumes slipping; a ~360x P/E leaves no room for either.

**Zhejiang Laifual Drive (3952.HK)** — China #2.
- Listed HK 30 Jun 2026 (priced HK$77–85.5, raised ~HK$1.15bn); mkt cap ~HK$6.7bn (~US$855m) in Aug 2026.
- 2025 revenue RMB261m (+142%); 2025 net loss ~RMB171m (36kr); 21.4% volume / 12.9% revenue share in China (CIC). ASP collapsed RMB802 (2023) → 724 (2024) → 573 (2025); company calls this a "strategic price adjustment to secure greater market share."
- H1 2026: revenue RMB142.2m (+80%), adj. EBITDA RMB12.4m, adj. net loss RMB4.1m (-63%).
- Biggest risk: it is the price-war instigator with thin/negative margins; humanoid volume must arrive before cash runs thin.

**Nidec Drive Technology (via 6594.T)** — FLEXWAVE and Smart-FLEXWAVE (built-in sensors, launched Dec 2024). Invested ~$80m to double Philippines reducer plant; had targeted ¥100bn reducer sales by 2025. **No humanoid share or 2026 capacity data found.** Immaterial to Nidec group valuation.

**Shuanghuan Driveline (002472.SZ)** — subsidiary Huandong Technology ships harmonics in small batches; RV reducers for hip/waist; new Suzhou base with 500k-set reducer capacity in 2026; Jan 2026 co-development with Xinjian Transmission on roller screws; enters Optimus chain indirectly via Tuopu/Sanhua; a subsidiary IPO is underway. Q1 2026: revenue and profit "grew modestly." Biggest risk: reducers remain a rounding error vs its EV gear business; humanoid halo priced in.

**Beijing CTKM** — named in market lists only; **no share, capacity or financial data found**.

**Lead times / allocation:** No hard 2026 lead-time figure found for harmonic reducers themselves; the constraint cited is upstream — high-end machine-tool deliveries stretched to ~12 months, so capacity adds are slower than announced targets suggest.

### 2. Planetary roller screws (linear actuators)

**Bottleneck evidence.** McKinsey flags PRS as potentially a more acute bottleneck than harmonic gearboxes (narrow supplier base, long lead times, few substitutes). Tolerances are micron-level; specialty steel, precision grinders and heat treatment cost "millions of dollars… years of expertise." A 2023 Optimus episode saw lead times balloon to 26 weeks; raw-material delays add 12–18 weeks. Chinese domestic yield ~60% vs 85%+ at Rollvis/GSA (gap: steel purity, thread-grinding precision, heat-treatment consistency, metrology); industry expects China to cross 80% by 2027–28. Qinchuan Machine Tool and Dingzhi are investing in domestic thread grinders. Hengli reportedly imported 25 high-precision thread grinders (Xueqiu post — **unverified**). **I found no specific data on Reishauer/Kapp Niles/Klingenberg lead times** — only the generic "high-end machine tool lead time ~12 months."

**Grinding vs rolling moat:** ground threads are required for the C3/C5-class accuracy and load rating in hip/knee joints; rolled/whirled threads are the cost-down route Chinese entrants are pursuing for hands and lower-load axes. Sources consistently describe grinding know-how + heat-treat + inspection as the moat; no source quantified cost delta.

**GSA AG + Rollvis SA (Ziegler Group, Swiss, private).** Same parent (thread grinding since 1932; GSA founded 1982, Rollvis added 2016). Together >50% global PRS share. Optimus Gen-3 reportedly uses 14 PRS sourced primarily from GSA (**unverified**). Operating near capacity on robotics + aerospace demand. Not investable.

**Ewellix / Schaeffler (SHA.DE).** Ewellix bought Jan 2023 for ~€582m + ~€120m net debt. Portfolio: ball and PRS assemblies, strain-wave gear with integrated torque sensor, bearings, and a new planetary-gear rotary actuator (CES 2026), all made in-house. Schaeffler cites 25–30 actuators per humanoid, ~45 humanoid engagements, humanoid market growth 53–88% CAGR 2025–35 (Feb 2026 deck), and targets a humanoid order book "in the three-digit millions of euros by 2030" assuming ≥1m units/yr industry output. Financials/valuation for the robotics line: **not found** (immaterial vs ~€20bn+ group sales). Biggest risk: humanoid is a rounding error for a leveraged auto supplier; upside is optionality only.

**Hengli Hydraulic (601100.SS).** Largest Chinese PRS capacity: 2.6m sets/yr (line completed end-2025, mass production 2026) + 800k sets Thailand = 3.4m sets. "Bestec/Hengli >5,000 units/month stable supply" cited as enabling 30–50% linear-actuator cost reduction. H1 2026 (corrected from snippet mis-scaling): revenue RMB6.83bn (+32.1%), Q2 RMB3.62bn (+31.8%), attributable NP RMB1.44bn (+0.5%; ~+38% ex-FX). Broker (CMBI/EastMoney note) expects 2026 screw revenue ~RMB2bn at ~40% GM, with ≥20k Optimus-equivalent orders (**aggressive, unverified**). Valuation not found. Biggest risk: hydraulics cycle dominates earnings; screw revenue ramp depends on Tesla volumes.

**Zhejiang Wuzhou Xinchun (603667.SS).** Reported Tesla mass-production designated supplier of inverted PRS for leg/waist and miniature ball screws for hands (>30 screws per robot). Capacity to 980k sets via private placement; Thailand plant 2026. Stock +183% in 2025; among the largest fallers in the 27 May 2026 humanoid sell-off. H1 2026 financials **not found** (search budget exhausted).

**Shanghai Beist / Beite Technology (603009.SS).** RMB1.85bn PRS base in Kunshan (Oct 2024); subsidiary Yuhua Precision completed samples, targeting batch supply 2026; auto customers BYD/Tesla/Li Auto. Broker NP forecasts RMB80m/110m/160m for 2024–26. Biggest risk: sub-scale, late entrant.

**Private Chinese PRS makers (pre-IPO):** Xinjian Transmission/NewSword ("Tier-1 T-chain supplier," co-developing with Shuanghuan); Seenpin Hangzhou (RMB2.6bn plant for 1m units/yr, Tesla-linked, IPO planned); Zhenyu Technology (linear actuator candidate). Nanjing Process and Jiangsu Leadmax: **no data found**.

**Actuator integrators (who actually holds the Tesla PO):**
- **Tuopu (601689.SS):** described as exclusive supplier of lower-limb linear actuators (hip/knee/ankle) and hand drive modules using self-developed PRS; also rotary actuators. 2024 revenue RMB26.5bn, NP RMB3.0bn. Two actuator lines (300k sets/yr) running early 2025; +200k/yr line Hangzhou Q1 2026; Thailand robotics plant (~150k m², up to RMB10bn output); Mexico plant ~200km from Giga Texas; RMB5bn robot-component base; goal ~60% of Optimus reducer supply by 2026 (**unverified**). +2.8% on 18 Sep 2026 audit report.
- **Sanhua (002050.SZ):** joint modules/actuators; reported RMB5bn (~$685m) Tesla linear-actuator order (enough for ~180k robots, deliveries from Q1 2026) — **company denied the report**; robotics revenue +320% YoY in H1 2025; plants in China/US/Mexico/Europe.
- Tesla audit: teams arrived in Zhejiang 16 Sep 2026, on-site audits from 17 Sep (Sanhua, Joyson, Tuopu; also Shanghai, Hangzhou, Ningbo, Xiamen); new ~5,000-unit order; 2026 plan ~50,000 Optimus units; Fremont line sized for 1m/yr; Chinese suppliers ~70% of hardware cost. V3 production start slated for summer 2026 at Fremont.

### 3. Cycloidal / RV reducers

**Nabtesco (6268.T).** ~60% global share of RV reducers for mid/large industrial robot joints (Morningstar wide-moat); only ~28% share (2024) in the nascent miniature-RV-for-humanoid segment. Launched RVmini and Monocrank compact series 2 Dec 2025 for cobots/humanoids. Capacity: doubling precision reduction gears to 2m units/yr by 2026 (~¥47bn investment; Hamamatsu plant completed Sept 2023); a Feb 2026 Tsuruga +30% expansion was cited by one source (**unverified**).
- H1 FY12/2026: revenue ¥167.4bn (+17%), OP ¥15.8bn (+72%), OPM 9.5%; PRG segment +¥4.8bn; Q2 orders +11% QoQ / +21% YoY; utilisation Tsu 85%, Changzhou 100%. FY guidance raised to revenue ¥344bn (+5%), OP ¥32.6bn (+18%).
- Valuation: P/E ~27–28x TTM. EV/sales not found.
- Biggest risk: humanoids are moving to harmonic + PRS architectures; RV content per humanoid is small (hip/waist only), so Nabtesco is more an industrial-robot cyclical than a humanoid play; Chinese RV (Shuanghuan, Zhongda) gaining in mid-tier.

**Sumitomo Heavy (6302.T).** FINE CYCLO zero-backlash line for robot joints. **No humanoid-specific wins, capacity or revenue data found.** Moat: medium (legacy Cyclo IP, #2 in cycloidal).

**Ningbo Zhongda Leader (002896.SZ).** RV + harmonic + gear motors. Publicly disclosed Unitree supplier (core joint reducer components, per Unitree IPO materials); named among Figure AI's reducer suppliers (**unverified**). **Financials not found.** Biggest risk: small, low-margin gear-motor business; price-taker.

### 4. Frameless torque motors and integrated joint modules

- **Kollmorgen (Regal Rexnord, RRX):** TBM2G frameless series (7 frame sizes × 3 stack lengths vs competitors' 3–5 sizes); sister brands Portescap (mini motors), Thomson (linear), Warner (brakes), Berg (gears); hosting humanoid forums at Automate 2026 and EMEA Humanoid Summit (Munich, 16–17 Jun 2026). Robot revenue share **not disclosed/found**.
- **Allient (ALNT):** ElectroFlux frameless torque motors; added 25mm/38mm sizes Aug 2026; slotless/axial-flux options. Robotics revenue split **not found**.
- **Moog (MOG.A):** ~$9.7bn mkt cap, +83% since KOID ETF inception; Seeking Alpha argues the market is mis-pricing it as a humanoid supplier (core is certified aerospace/defence actuation). Risk: de-rating when humanoid revenue fails to show.
- **Maxon (private), TQ RoboDrive (private, DLR-origin), Genesis Motion:** Maxon/TQ confirmed as humanoid/cobot frameless suppliers; **Genesis Motion — no data found**.
- **Hyundai Mobis:** agreement at CES 2026 to supply actuators for Boston Dynamics' next-gen Atlas (details not retrievable).
- **Inovance (300124.SZ):** low-voltage high-power drivers, frameless torque motors, joint modules moved to development stage; delivered samples of PRS-based linear modules; launches targeted end-2025. Chinese frameless peers: Step Electric, Dongjie Zhikong, Leadshine (CES 2026), Aerospace Electric, Haozhi, Micro Precision Motor. **Estun (002747.SZ): no humanoid data found.**
- **Unitree (688836.SS):** IPO priced ¥150.80 on 6 Aug 2026 (~$9bn), closed +460% on debut (~$50bn). Builds its own QDD actuators (6:1–9:1 ratios, rare-earth magnets); vertical integration cited as the source of ~60% gross margin; >90% domestic sourcing; disclosed suppliers include Changsheng Bearing (300718.SZ) and Zhongda Leader (002896.SZ).
- Take: motors are the most readily in-housed element (Tesla designs its own; Unitree builds its own); value accrues to actuator assemblers (Tuopu/Sanhua) and to the gear/screw makers, not to standalone motor vendors.

### 5. Cross-roller and thin-section bearings

- **IKO / Nippon Thompson (6480.T):** estimates 14–20 crossed-roller bearings per humanoid; launching ultra-lightweight LCRB series (Apr 2026). FY3/2026: needle roller & linear guide sales ¥56.5bn (+17.9%), production ¥52.4bn (+13.5%). Humanoid revenue share **not disclosed**.
- **THK (6481.T):** Cross-Roller Ring for compact robot joints (radial/axial/moment loads); also ball screws/linear actuators. Humanoid figures **not found**.
- **NSK (6471.T), Schaeffler (INA/FAG), SKF-Kaydon (thin-section "Reali-Slim"), Silverthin:** incumbents competing on lightweighting, sealed variants and rapid prototyping.
- **Chinese entrants:** Changsheng Bearing (300718.SZ, self-lubricating bearings for Unitree). Flexible bearings for harmonic reducers are increasingly localised; no share data found.
- Market: humanoid-robot bearings forecast at ~46.6% CAGR (openPR). Not described as a bottleneck anywhere in the sources.

---

## (c) Unverified claims (single-source, promotional, or internally inconsistent)
1. Green Harmonic/Leaderdrive "~60% of Optimus reducer supply in 2026 at 30–40% below Japanese prices" — supplier-blog sourced.
2. Tuopu "exclusive global supplier of lower-limb linear actuators" and "60% of Optimus reducer supply by 2026" — Chinese broker/promo sources; WSJ cited only as verifying Tuopu as one of two high-certainty suppliers.
3. Sanhua RMB5bn/$685m Tesla order — reported by 36kr/Teslarati, **denied by the company**.
4. Optimus Gen-3 sourcing 14 PRS "primarily from GSA" — single source (kggfa.com).
5. Laifual "70,000 reducers shipped in 2025" conflicts with its 21.4% volume share of a ~1.4m-unit market (~300k) — one figure is wrong.
6. Shuanghuan "Q1 2026 revenue 9.1B CNY" from Alpha Spread snippet — implausible for a single quarter (annual revenue is ~RMB9bn); likely TTM/annual.
7. Hengli "imported 25 high-precision thread grinders" — Xueqiu retail post.
8. Hengli 2026 screw revenue RMB2bn at 40% GM — broker projection, not company guidance.
9. Nabtesco Tsuruga +30% RV expansion (Feb 2026) — single Substack source; the confirmed program is the 2m-unit doubling via Hamamatsu.
10. "Precision grinding… concentrated among Nippon Thompson and Rollvis" — Nippon Thompson is a bearing/linear-guide maker, not a grinder OEM; treat as garbled.
11. Zhongda Leader named as Figure AI reducer supplier — Morgan Stanley Humanoid 100 list-derived; Figure has not confirmed.
12. HDS "harmonic reducer revenue of 114 million yuan in 2025" (36kr price-war article) — inconsistent with HDS' ¥60bn+ scale; probably refers to a different company.
13. Harmonic-drive patent expiry "19 Feb 2025" — refers to one US motor patent, not the core strain-wave patents (expired decades ago).
14. Market-size figures from paid-report vendors (QY, IntelMarket, Verified, dataintelo) vary by 3–5x and are not reconciled.

**Data not found (flag):** Reishauer/Kapp Niles/Klingelnberg lead times; Nidec DT humanoid share; CTKM anything; Estun humanoid; Genesis Motion; Sumitomo Heavy humanoid; Zhongda Leader and Wuzhou Xinchun H1 2026 financials; EV/sales for all names; P/E for Schaeffler, THK, IKO, NSK, RRX, ALNT, Tuopu, Sanhua, Hengli, Shuanghuan; harmonic reducer unit lead times in 2026; Boston Dynamics/Hyundai Mobis agreement details.

---

## (d) Sources
- https://finance.biggo.com/news/JP_6324.T_2026-08-07 (HDS Q1 FY3/27 call, guidance)
- https://note.com/mangawakaru/n/n06cd47063ffe?hl=en (HDS FY3/26 revision)
- https://www.investing.com/equities/harmonic-drive-systems-inc ; https://stockanalysis.com/quote/tyo/6324/statistics/ (HDS valuation)
- https://www.hdinresearch.com/news/1559 (HDS Beverly/Hotaka capex)
- https://404kresearch.substack.com/p/leader-harmonic-deep-dive-80-90-humanoid (Leaderdrive share/capacity)
- https://humanoid.guide/leaderdrive-harmonic-reducers-surge-as-humanoid-demand-lifts-shares/ (Leaderdrive FY2025)
- https://eu.36kr.com/en/p/3865401317309313 (price war; Green Harmonic 2025, Laifual loss)
- https://news.futunn.com/en/post/62706196/... (Leaderdrive broker forecasts)
- https://longbridge.com/quote/688017.SH/valuation ; https://www.investing.com/equities/leader-harmonious-drive-systems (688017 valuation)
- https://hk-official.cmbi.info/upload/e3ebe881-03e5-4d27-8045-d61823c4df93.pdf (CMBI Laifual initiation)
- https://autonews.gasgoo.com/articles/market-industry/laifual-drive-launches-ipo-plans-to-list-on-june-30-2069799357594185729 ; https://itbusinessnet.com/2026/08/laifual-03952-hk-announces-2026-interim-results/ (Laifual IPO, H1 2026)
- https://corematter.substack.com/p/china-humanoid-robot-deployments-wrc-2026 (Laifual mkt cap, humanoid share of reducer demand)
- https://www.nidec.com/en/products/news/2024/news1225-01/ ; https://www.eetimes.com/nidec-positions-precision-reducers-for-cobots-humanoids-and-automation/ (Nidec DT)
- https://www.patsnap.com/resources/blog/rd-blog/harmonic-drive-gearing-patent-landscape/ (patent landscape)
- https://eu.36kr.com/en/p/3780414717129481 ; https://eu.36kr.com/en/p/3728136166797832 (Optimus China supply chain)
- https://finance.biggo.com/news/gQPHv50BZk7xib5f4ox8 ; https://en.androidshow.com/list_72/195.html (70% China content, Wuzhou/Tuopu/Sanhua roles)
- https://ahr.so/teslas-secret-chinese-supplier-is-going-ipo-betting-on-a-million-robot/ (Seenpin)
- https://www.scmp.com/business/companies/article/3368053/tesla-auditing-chinese-suppliers-ahead-optimus-roll-out-sources ; https://www.bloomberg.com/news/articles/2026-09-18/chinese-robotics-suppliers-rise-on-tesla-optimus-audit-report ; https://eu.36kr.com/en/p/3987206969546624 (Sept 2026 audits, 5,000-unit order, 50k plan)
- https://eu.36kr.com/en/p/3510288514980998 ; https://www.teslarati.com/tesla-optimus-v3-design-finalized-china-rumors/ (Sanhua order report/denial)
- https://news.futunn.com/en/post/66803312/... ; https://robottoday.com/article/how-tuopu-became-a-core-player-in-tesla-s-emerging-humanoid-robot-ecosystem ; https://inf.news/en/economy/02c31e7b34e924f73dd77a76a21208ac.html (Tuopu)
- https://europecapitalnews.substack.com/p/the-bottleneck-behind-the-humanoid ; https://www.ignoretheconfusion.com/p/the-manufacturing-challenge-that ; https://www.fastcompany.com/91314612/this-tiny-screw-is-powering-the-humanoid-robot-revolution (PRS bottleneck, McKinsey)
- https://interestingengineering.com/ai-robotics/china-humanoid-robots-actuators ; https://www.thexpin.com/p/china-humanoid-robot-supply-chain (yields 60% vs 85%, Qinchuan/Dingzhi)
- https://www.kggfa.com/news/another-look-at-the-tesla-robot-the-planetary-roller-screw/ ; https://www.limonrobot.com/planetary-roller-lead-screws-powering-humanoid-robots-and-driving-chinas-breakthroughs (GSA/Rollvis, lead times)
- https://rollvis.com/about-us/ (Ziegler Group)
- https://www.schaeffler.com/en/media/press-releases/press-releases-detail.jsp?id=88156672 ; https://finance.yahoo.com/sectors/technology/articles/schaeffler-sees-humanoid-robotics-orders-112441111.html ; https://www.schaeffler.com/remotemedien/media/_shared_media_rwd/08_investor_relations/presentations/20260205_humanoids_at_schaeffler.pdf (Schaeffler)
- https://medicineandmarkets.substack.com/p/the-humanoid-robot-trade-may-not (Ewellix deal terms)
- https://eu.36kr.com/en/p/3636380217885702 ; https://news.qq.com/rain/a/20260827A07Z6D00 ; https://xueqiu.com/5558886703/351404594 ; https://pdf.dfcfw.com/pdf/H3_AP202608251828422871_1.pdf (Hengli capacity, H1 2026, grinders)
- https://www.itiger.com/news/2475595965 ; https://news.futunn.com/en/flash/18440972/... (Beist/Beite)
- https://inf.news/en/economy/6715abd81bd87f07956e409c471e57e3.html ; https://min.news/en/economy/dc20dede27a17965f31c3fef9d51180d.html (Wuzhou Xinchun, Xinjian)
- https://www.nabtesco.com/en/news/20251202-17329/ ; https://finance.biggo.com/news/ir_6268.T_20260806_a83095b6df94 ; https://www.morningstar.com/company-reports/1080595-... ; https://seisanzai-japan.com/article/p3206/ ; https://www.intelmarketresearch.com/miniature-rv-reducer-for-humanoid-robots-market-6266 ; https://www.investing.com/equities/nabtesco-corp-ratios (Nabtesco)
- https://us.sumitomodrive.com/en-us/industry/robotics (Sumitomo)
- https://kraneshares.com/a-complete-guide-to-unitree-robotics-2026-ipo-... ; https://www.techtimes.com/articles/325193/20260821/unitree-ipo-closes-460-... ; https://robotopian.com/blogs/news/unitree-robotics-ipo-2026-financials-valuation (Unitree, Zhongda/Changsheng disclosure)
- https://news.futunn.com/en/post/51736957/... ; https://news.futunn.com/en/post/63560437/... (Shuanghuan)
- https://www.kollmorgen.com/en-us/solutions/robotics/humanoid-robots ; https://www.kollmorgen.com/en-us/company/events/join-regal-rexnord-motion-brands-humanoid-robot-forum-automate-2026 (Kollmorgen)
- https://www.roboticstomorrow.com/news/2026/08/19/allient-inc-expands-electroflux-series-frameless-torque-motors-with-new-sizes/26971/ (Allient)
- https://seekingalpha.com/article/4941915-moog-market-is-confusing-it-for-a-humanoid-robotics-supplier ; https://kraneshares.com/humanoid-robotics-etf-top-performing-stocks-in-the-koid-portfolio/ (Moog)
- https://www.tq-group.com/en/products/tq-robodrive/torque-motors-humanoid-robots-whitepaper/ (TQ)
- https://www.barchart.com/story/news/36939666/hyundai-mobis-forms-strategic-collaboration-framework-with-boston-dynamics (Mobis/Atlas)
- https://roboticsandautomationnews.com/2025/09/25/inovance-technology-targets-humanoid-robot-components-... ; https://robotics.techbuzzchina.com/reports/actuators-motors.html ; https://www.honest-hls.com/frameless-torque-motor (Inovance, Chinese motor cluster)
- https://pmarketresearch.com/auto/humanoid-robot-crossed-roller-bearing-market/ ; https://ikont.com/rotary-bearings/crossed-roller-bearings/ ; https://www.thk.com/?q=us/node/5229 ; https://www.marketscreener.com/news/nippon-thompson-release-of-business-results-for-the-march-2026-term-ce7f5bd8df8ff72d ; https://www.skf.com/us/products/thin-section-bearings/industry-pages/solutions-for-robotics-industry ; https://pibsales.com/bearings/a-guide-to-robot-joint-bearing-design/ (bearings)
- https://www.trendforce.com/presscenter/news/20251209-12825.html (2026 humanoid shipments)
- https://www.qyresearch.com/reports/5499331/harmonic-drive ; https://reports.valuates.com/market-reports/QYRE-Auto-4V12992/global-harmonic-reducer-for-humanoid-robot ; https://www.persistencemarketresearch.com/market-research/roller-screw-market.asp (market sizing)

