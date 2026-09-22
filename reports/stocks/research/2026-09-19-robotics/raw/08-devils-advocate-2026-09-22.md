# Devil's advocate: "Humanoid supply-chain moats will be big winners"
*Date: 22 Sep 2026. I read every file in `reports/stocks/research/2026-09-19-robotics/` (the moat map, the projection, the model output and raw/01-07) and re-ran `scripts/robotics_2030_model.py` with changed inputs. I used 15 web searches; all of them worked. Anything I state from memory, and anything that is my own reasoning, is labelled.*

---

## (a) The strongest bear argument

The 2030 base case of 900k units rests on Chinese shipments. Chinese regulators are now questioning that revenue themselves. Reuters (20 Sep 2026) reports they have informally frozen humanoid IPOs and are scrutinising revenue from state-backed data-collection centres and local-government JVs, where the government puts up 80-90% of the money. Mech-Mind's CEO says stripping out that revenue could cut some valuations by 60-70%. Unitree is down 55% from its peak a month after listing.

Meanwhile the bottleneck parts are capacity moats that China is already competing away. Four to five suppliers are chasing each part, at 40-60% of Japanese prices. The #2 humanoid maker by volume (Unitree) uses quasi-direct-drive planetary joints that need neither harmonic reducers nor roller screws. The one real scarcity, Dy/Tb, is a policy variable on the table at the Xi-Trump summit (23-25 Sep 2026) and at the 10 Nov 2026 deadline.

The team's own model already shows negative base-case returns for every pure play. Once I fix its architecture-blind content pools, even the two "margin of safety" names (Keli, Hesai) turn negative. The names that survive (Nvidia, Schaeffler) survive for reasons that have nothing to do with robots.

---

## (b) Ranked attacks

| # | Claim | Evidence (sourced) | Severity | Hit hardest |
|---|---|---|---|---|
| 1 | **Chinese demand is partly policy-manufactured.** The 80%+ Chinese share is propped up by data-collection centres and state procurement. | Reuters 20 Sep 2026: window guidance on humanoid IPOs; regulators question revenue from "data collection centers, related-party deals and other unsustainable arrangements"; stripping it out "could cut some valuations by 60% to 70%". Unitree down 55% from peak. Local-government JVs fund 80-90% of initial investment. UBTech won an $18M Guangxi tender to supply a *training* facility (Bloomberg, 27-31 Aug 2026). A search snippet says one Hangzhou maker's subsidies were ~42% of its net profit (the page behind it is unconfirmed; UNVERIFIED). | **High** | Leaderdrive, Keli, Hengli, Huachen, Qinchuan (all modelled on the "chinese" or "all" pools) |
| 2 | **Robots are not yet doing useful work at scale.** | Musk admitted in Jan 2026 that zero Optimus units were doing useful factory work, and Tesla missed its 10k 2025 goal (team raw/06, Electrek). AP (Jul 2026): Tesla and Figure "each shipped a few hundred or less" in 2025. BMW told Fortune (2025) that only one Figure robot worked at Spartanburg at any time; Figure threatened to sue. Chinese teleop trainers get one usable movement per 300 attempts as novices and one per 50 when experienced (Bloomberg, Aug 2026). "Deployments in 2026 are real but narrow: totes, bins, parts" (cervo-tech). Unitree's CEO said in Aug 2025 that humanoids still lack the AI (Bloomberg). | **High** | Everything volume-driven; worst for Wuzhou, Tuopu, Sanhua (Tesla) and Leaderdrive, Keli (China) |
| 3 | **Capacity moats are already being competed away.** Screw and reducer capacity exceeds demand several times over. | Chinese roller-screw capacity: Hengli 3.4M sets, Wuzhou 0.98M, Seenpin 1M plant (team raw/01). Global 2026 demand is at most ~0.84M screws, even if all ~60k robots used 14 each (my arithmetic). That is about 6x overcapacity before counting that most Chinese robots use no roller screws. Harmonics: Leaderdrive alone is heading to 1.44M/yr by end-2026 and ≥2M in 2027, plus Shuanghuan 500k, against 179k humanoid harmonics in China in 2025 (raw/01). "Four or five suppliers chasing the same harmonic reducer or roller screw"; mid-to-high-teens margins projected (aiproem substack, mid-2026). Laifual cut its ASP from CNY 802 to CNY 573 and lost ~CNY 171M in 2025 (raw/01). | **High** | Leaderdrive, HDS, Hengli, Wuzhou, and then the grinder makers |
| 4 | **Architecture risk: the winning design may drop the bottleneck part.** | Unitree builds QDD actuators at 6:1-9:1 ratios in-house (raw/01). Planetary reducers cost about 1/5 of harmonics and can be hobbed on standard equipment (corematter / zanerobotics substack). Tesla Gen 2 already used some low-ratio joints (<20:1). Unitree's ASP fell from ¥593k (2023) to ¥168k (9M25) per its prospectus via corematter, which shows the cost-down route runs through simpler joints. Tesla's hand moves actuators into the forearm with tendons (raw/05). | **High** | Leaderdrive, HDS, Hengli, Wuzhou, Huachen, Qinchuan, Nabtesco |
| 5 | **The rare-earth premium is a bargaining chip, not geology.** | The April 2025 Dy/Tb licences are still in force. The Oct 2025 package is suspended to 10 Nov 2026 (Clark Hill, CSIS). Trump-Xi summit 23-25 Sep 2026, with rare earths central; USTR Greer says Beijing is "still holding out" on mineral exports (chinastrategy.org, 21 Sep 2026). Grain-boundary diffusion cuts Dy/Tb 50-70%, and Zhenghai pushes HRE-free grades (raw/02). By the team's own maths, robots are 2% of Lynas's 2030 revenue. | **High** (binary, near-term) | Lynas, MP (sentiment), Energy Fuels |
| 6 | **US-China decoupling was missed entirely by the team.** | FCC banned imports of *new* foreign-made humanoid and quadruped models on 28-29 Jul 2026 (AP/PBS/NBC/Al Jazeera). The Pentagon designated Unitree a 1260H Chinese military company on 8 Jun 2026 (AP). The Section 232 robotics review explicitly covers parts; no decision yet, and action can come any time (strtrade, FDD). None of this appears in any team file (I grepped). | **High** | Hengli, Wuzhou, Tuopu, Sanhua, Leaderdrive (Tesla chain, 70% China content); Hesai (US listing) |
| 7 | **Tesla concentration on unconfirmed orders.** | V3 unveil slipped from Feb/Mar 2026 to "later this year"; production moved to "late July/Aug" (Q1 call; notateslaapp, tesery). No 2026 unit target. The Sanhua CNY 5B order was denied by the company. All supplier claims come from Chinese media or brokers (raw/01, raw/06). The reported audit order is about 5,000 units against a reported 50k plan. The model puts 29% of Wuzhou's 2030 revenue on Tesla. | **High** for Wuzhou; **Med** for Tuopu, Sanhua (robots are 4% of revenue) | Wuzhou, Tuopu, Sanhua, Hengli |
| 8 | **Price already discounts the story; the team's own model says so.** | Base-case CAGRs: 14 of 18 names are negative. Pure plays need 1.6-3.3M units in 2030 just to break even (projection-2030.md §3). Robot revenue across all 18 names in 2030 is $3.1B, and robot net income is about $0.67B. Capitalised at 25x, that is ~$17B, or about 8% of the $200B combined market cap excluding Nvidia (my computation from the model). | **High** | All pure plays |
| 9 | **Base rates for picks-and-shovels after the hype peak are brutal.** | 3D Systems fell >92% and Stratasys >86% from Jan 2014 (Motley Fool). Lithium carbonate fell 80% in 2023. The LIT ETF's maximum drawdown was 65.9% (Apr 2025), and Albemarle is at $111 (18 Sep 2026), about 50% below its 52-week range high and further below its 2022 peak. Polysilicon went from $39/kg (2022) to <$4.50/kg (end-2024); Tongwei lost CNY 7.04B in 2024 (Caixin, pv-tech). Cobots are the closest analogue: Universal Robots revenue went $326M (2022) → $304M → $293M (2024), Teradyne Robotics revenue fell 17.9% in 9M25, and Teradyne made 10% and 14% layoffs (SEC 10-Q, Robot Report). From memory, UNVERIFIED this session: Segway sold ~30k units in 6 years against a claimed 10k/week; Lilium and Volocopter both went insolvent in 2024-25. | **Medium** (history, not proof) | Chinese A-share components, grinders |
| 10 | **The AI and data problem may take a decade.** | Waymo, from memory (UNVERIFIED this session): the Google project started in 2009 and ran its first public driverless rides in Oct 2020, 11 years later, in one metro area, for a far easier task. Foundation models are "the most contestable layer", with at least 8 rivals and open weights (raw/04). Teleop yields 5-50 episodes per hour (raw/04). Nvidia is pitching GR00T N2 because current VLAs fail on novel tasks (raw/04: ">2x success on novel tasks vs VLAs"). | **Medium-High** | All; this is the upstream cause of #2 |

---

## (c) Model audit (`robotics_2030_model.py`, `projection-2030.md`)

I re-ran the model. Reproduction scripts are in the scratchpad (`audit.py`, `audit2.py`).

1. **Content pools ignore architecture (the biggest error).**
   - What the model assumes:
     - Hengli: 14 roller screws in **all** 900k robots.
     - Leaderdrive: 14 harmonics in **all** 700k Chinese robots.
     - Keli: four 6-axis force/torque sensors in **all** Chinese robots.
   - Why that is implausible: the pre-share content pools add up to **$6,010 per Chinese robot**, and Hengli plus Leaderdrive plus Keli alone come to **$4,970**. A Chinese BOM is $6-15k. The team's own BOM table puts all sensors at 8%, which is $800 on a $10k robot, yet Keli's F/T pool alone is $1,680. Unitree (31% of 1H26 volume) uses QDD, not harmonics or roller screws.
   - Corrected base case (pool fix only):

   | Name | Fix | Base CAGR | Breakeven units |
   |---|---|---|---|
   | Hengli | Western robots + 25% of Chinese | −8% → **−10%** | 3.3M → **7.9M** |
   | Leaderdrive | 50% of Chinese robots | −11% → **−20%** | 1.6M → **3.3M** |
   | Keli | 2 sensors in 40% of Chinese robots | +5% → **−5%** | 0.5M → **2.6M** |

   For Keli, +10% a year then needs **6.9M units**, not 1.4M. Keli stops being a margin-of-safety name.

2. **Nvidia's +20% is 100% a data-centre call.** Robotics is **0.046%** of modelled 2030 revenue. Setting robotics to zero leaves the CAGR at +20%. The +20% itself rests on 15% growth, a 55% net margin and a 28x exit on FY27 consensus.
   - Exit at 22x: **+13%**.
   - 8% growth, 45% margin, 22x: **+1%**.

   Nvidia should be taken out of a robotics ranking. The projection's headline ("positive only for Nvidia...") dresses up a GPU-cycle view as a robot finding.

3. **Market caps contradict the note's "lower figure used" rule.**
   - HDS uses ¥651.3B (July), but raw/01 has **¥548B on 12 Sep**. Corrected: −16% → **−12%**. This one helps the bull.
   - Keli uses CNY 20.0B against sources of 18.8B and 22.5B. The CAGR range is **+2% to +6%**.
   - Lynas uses A$10.9B, but raw/02 has the share at A$15.54 and estimates the cap at A$14-15B. At A$15.5B (my estimate; share count unconfirmed): −6% → **−14%**.
   - Every cap pre-dates the Unitree −55% and the IPO freeze, so the A-share names may now be cheaper (UNVERIFIED).

4. **Exit multiples stay the same in every scenario.** The model applies 25-30x to parts the team itself rates C or "sliding to C". That is inconsistent in my view; commoditised Chinese component makers look more like 15-20x (my reasoning). If the bear case also halves the multiple:

   | Name | Bear CAGR now | With half exit P/E |
   |---|---|---|
   | Leaderdrive | −24% | **−35%** |
   | Wuzhou | −28% | **−39%** |
   | HDS | −22% | **−34%** |
   | Keli | −3% | **−18%** |

5. **Leaderdrive's 28% robot net margin at an $85 ASP is contradicted by the team's own data.** Laifual's 2025 ASP of CNY 573 (about $80) came with a net loss. With a 17% margin, a 20x exit and the pool fix: base **−35%**, breakeven **8.9M units**, which is above Goldman's 2035 figure of 6.5M.

6. **Prices do not respond to volume.** 2030 component prices are held fixed across the bear, base and bull cases. In the bear case, overcapacity should push prices lower still. In the bull case, scale should also cut prices. So the breakeven solver's unit numbers are too low, and the bear-case downside is understated.

7. **The grinder pool is mis-specified.**
   - The note's own inputs give a $160 steady-state replacement cost per robot, not $270: 28 parts × ($1.2M / 30k parts) / 7-year life.
   - Grinder demand depends on how fast *capacity is added*, not on unit output. Chinese screw capacity is already about 6x 2026 demand (attack #3), so grinder orders could peak in 2025-27 and be lower by 2030. That is the equipment-maker pattern of 2021-24.
   - Huachen with the pool cut to 40% and an 18x exit: −13% → **−23%**.

8. **Double counting and an aggressive share stack.**
   - Hesai's base revenue already includes robotics lidar (>500k units in FY26), and the model adds a 2.7M-unit "embodied" pool on top. Removing the overlap takes the base case from +2% to **0%**. Most Western humanoids (Tesla, Figure) are camera-only, so the lidar pool is not humanoid-driven.
   - Leaderdrive's base revenue also already includes ~30% humanoid sales (minor).
   - Per Tesla robot, the 18 names capture **$11,468**, which is 38-57% of Tesla's $20-30k target BOM.
   - GSA/Rollvis, today's main roller-screw source, gets 0%, while Wuzhou gets 50% and Hengli 25%.

9. **Scenario design.**
   - The "bear" case of 300k units is itself optimistic.
   - At **150k** (my crash case): Leaderdrive **−29%**, Wuzhou **−33%**, HDS **−23%**, Keli **−6%**, Hengli −11%.
   - The Western share is fixed at 22% even though the FCC ban and 1260H now fragment the market.
   - The note compares 2030 breakevens with Goldman's *2035* 6.5M figure as if it were a near target.

10. **Unused field and inconsistent base years.**
    - `base_ni_lc` is never used. 2030 base net income is an assumed margin that has no link to today's profits: Schaeffler is at TTM EPS −$0.47 yet assumed at 3%. At 2%, Schaeffler goes +5% → **−5%**.
    - `YEARS = 4.25` compounds FY2025 actuals (Tuopu, Sanhua, Wuzhou, Leaderdrive, Keli) and *forward* bases (HDS FY3/27 guide, Nvidia FY27 consensus, MP 2026 consensus) by the same amount. Forward bases are over-compounded by ~0.25-0.5 years (about 1 point of CAGR); trailing ones are under-compounded.

11. **No dilution.** Wuzhou's private placement to reach 980k capacity, MP's DoD preferred (~15% diluted, raw/02) and the stream of Chinese IPOs are all ignored, so returns are overstated.

---

## (d) Kill-shot table

| Company | What makes it a bad investment | Observable signal and date |
|---|---|---|
| Lynas | Its premium is China policy; robots are 2% of revenue; the correct market cap makes the base case −14% | Summit outcome **23-25 Sep 2026**; renewal or general licences by **10 Nov 2026**; ex-China Dy quote converging from $575-2,500/kg toward China's ~$215; HRE ASP in the Oct 2026 quarterly |
| MP Materials | 36x 2030 earnings, loss-making, 10X plant not until 2028, no heavy rare earths; robots irrelevant | Q3 results (early Nov 2026); any 10X slip |
| Nvidia | Robots are 0.05% of revenue; the return depends on data-centre capex | Hyperscaler 2027 capex guides (late Oct 2026); Q3 FY27 against the $108B guide (late Nov 2026) |
| Hengli | Screw price deflation (to 1/10 of 2025 prices in the model); most Chinese robots use no roller screws; 232 parts exposure | Q3 report (late Oct 2026): does it disclose screw revenue at all; Tesla audit outcome (Oct 2026) |
| Wuzhou Xinchun | Leveraged single-customer bet; 3% base margin; model −16% base, −33% at 150k | Tesla Q3 call (~late Oct 2026) with no Optimus unit number; V3 unveil slipping into 2027 |
| Schaeffler | Robots are 1% of revenue; this is an auto-margin bet | Q3 margin (Nov 2026); net-debt covenant headlines |
| Huachen / Qinchuan | Grinder demand is a derivative of screw capacity additions that are already overbuilt | Screw makers cutting capex in H1 2027; Q3 2026 order backlogs |
| Harmonic Drive | 52x 2030 earnings; Chinese price competition; Schaeffler's new process from 2027 | Q2 FY3/27 orders (early Nov 2026) slowing from +56% to under +20% |
| Leaderdrive | 364x trailing earnings on a deflating, over-supplied part; its customers face an IPO freeze | Q3 2026 gross margin and ASP; 120k/month reached **Dec 2026** with falling prices; AgiBot IPO delay |
| Tuopu / Sanhua | Robots are 4% of revenue; unconfirmed Tesla POs, one of them denied | Tesla-confirmed supplier list (or silence) by YE 2026; any Section 232 parts action |
| LG Innotek | Robots are 0% of revenue; it depends on Apple | iPhone cycle; robots do not matter |
| Hesai | Humanoids mostly don't use lidar; ASP deflation; US-listed Chinese issuer after the FCC ban | Q3 2026 ASP; any FCC or 1260H action on lidar (from memory, Hesai was already put on the 1260H list in Jan 2024; UNVERIFIED this session) |
| LG Energy Solution | 0.5 GWh of robot demand against a >400 GWh base (my estimate); it is an EV-cycle stock | EV demand and IRA-credit headlines |
| Nabtesco | Humanoids are moving away from RV reducers; it is an industrial-robot cyclical | Q3 orders (Nov 2026) |
| Keli | The F/T content per robot is 2x a Chinese robot's entire sensor budget; the corrected base case is −5% | Chinese 6-axis quotes below CNY 2k; F/T revenue line in the FY2026 annual report (Apr 2027) |
| Allegro | Robots are 2% of revenue; GAAP loss in FY26 | Auto and industrial semiconductor cycle |

---

## (e) What the bull case gets right

- Volume is real and compounding from a small base: 19.1k units in 1H26, +272% y/y (SAG). The Chinese cost curve (Unitree G1 BOM about $5.8k) makes eventual mass adoption plausible.
- The Dy/Tb two-tier market is real. Ex-China prices are 4-5x China's, the April 2025 licences were never lifted, and Lynas is the only tonne-scale ex-China source.
- Nvidia's stack (Jetson Thor, Isaac, Cosmos) is the default on Western humanoids.
- The team's own analysis is honest: it already finds robots immaterial for most names and pure plays priced for 2-4x Goldman's volumes. The bear case largely extends the team's own conclusions.
- Precision grinding and heat treatment are genuine know-how gaps today, with Chinese roller-screw yields of ~60% against 85% in Switzerland.

---

## (f) Verdict per company

- **Lynas**: only on a big drawdown, and only after the summit and 10 Nov outcome. It is a policy trade, not a robot trade.
- **MP Materials**: avoid as a robotics play. The DoD floor makes it a defence utility at 36x 2030 earnings.
- **Nvidia**: survives the attack, but for data-centre reasons; the robot thesis adds nothing.
- **Hengli**: only on a big drawdown. The hydraulics base (~23% net margin) is real, and screws are optional upside.
- **Wuzhou Xinchun**: avoid.
- **Schaeffler**: survives as a cheap auto-recovery option (8x 2030 earnings). Robots are free, but so is the margin risk.
- **Huachen**: avoid.
- **Qinchuan**: avoid.
- **LG Innotek**: avoid as a robotics play.
- **Hesai**: survives best of the robot-exposed names, because it is priced on auto lidar and already profitable. It needs no humanoids, and US-listing risk remains.
- **LG Energy Solution**: avoid as a robotics play.
- **Harmonic Drive**: avoid.
- **Tuopu**: only on a big drawdown. It is an auto supplier at a fair price; the Tesla option costs little.
- **Sanhua**: avoid as a robotics play.
- **Leaderdrive**: avoid.
- **Nabtesco**: only on a big drawdown, as an industrial-robot cyclical.
- **Keli**: only on a big drawdown. The model's "margin of safety" disappears once content is corrected.
- **Allegro**: avoid as a robotics play.

---

## (g) Sources

**Web, this session**
- Reuters via RTE / investing.com / TheNextWeb, "China slows humanoid robot IPO rush" (20-21 Sep 2026): https://www.rte.ie/news/business/2026/0921/1592325-china-slows-humanoid-robot-ipo-rush/ ; https://www.investing.com/news/stock-market-news/china-slows-humanoid-robot-ipo-rush-as-hype-outruns-reality-4908236 ; https://thenextweb.com/news/china-slows-humanoid-robot-ipos-unitree
- Bloomberg via Insurance Journal / Japan Times, "China's humanoid robots aren't smart enough..." (27-31 Aug 2026): https://www.insurancejournal.com/news/international/2026/08/31/883381.htm ; https://www.japantimes.co.jp/business/2026/08/27/tech/china-humanoid-robots-job/
- CNBC, 21 Aug 2026: https://www.cnbc.com/2026/08/21/chinese-humanoid-robots-face-challenge-of-their-own-capabilities.html
- Rest of World, data factories: https://restofworld.org/2026/china-robots-training-centers-workers/
- Cervo-tech statistics: https://cervo-tech.com/blog/humanoid-robot-market-statistics-2026.html
- EdgeX, 97% China share: https://pro.edgex.exchange/en-US/news/article/china-ships-97-percent-humanoid-robots-h1-2026
- The "Hangzhou subsidies = 42% of profit" figure is UNVERIFIED (search snippet; source page unconfirmed).
- FCC humanoid import ban and Unitree 1260H (AP via ABC/PBS/NBC, Al Jazeera, 28-29 Jul 2026): https://www.pbs.org/newshour/world/u-s-bans-foreign-made-humanoid-robots-targeting-china-over-national-security ; https://www.aljazeera.com/economy/2026/7/29/us-bans-imports-of-new-chinese-robots-over-security-concerns ; https://www.nbcnews.com/tech/tech-news/us-bans-foreign-made-humanoid-robots-targeting-china-national-security-rcna589777
- Section 232 robotics: https://www.strtrade.com/trade-news-resources/tariff-actions-resources/section-232-investigation-robotics-industrial-machinery ; https://www.fdd.org/analysis/2025/10/17/section-232-national-security-investigation-of-imports-of-robotics-and-industrial-machinery/
- Rare earths and the summit: https://www.chinastrategy.org/2026/09/21/rare-earths-friction-threatens-to-stall-trade-truce-extension-ahead-of-xi-trump-summit/ ; https://rareearthexchanges.com/news/trump-xi-summit-rare-earth-trade/ ; https://www.clarkhill.com/news-events/news/china-hits-pause-on-rare-earth-export-controls-and-what-it-means-for-supply-chains/ ; https://www.csis.org/analysis/rare-earth-export-restrictions-one-year-later
- Tesla Optimus delays: https://www.notateslaapp.com/news/3884/tesla-delays-optimus-gen-3-unveil-for-finishing-touches ; https://www.tesery.com/blogs/news/tesla-optimus-production-timeline-update-2026 ; https://optimusk.blog/blog/tesla-optimus-delay/
- Figure and BMW (Fortune dispute): https://mikekalil.com/blog/figure-ai-vs-fortune/ ; https://www.humanoidsdaily.com/news/figure-ais-bmw-partnership-reports-detail-cautious-first-steps-for-humanoid-robots-in-manufacturing
- QDD and Unitree ASP: https://corematter.substack.com/p/humanoid-robot-actuators-torque-economics ; https://zanerobotics.substack.com/p/quasi-direct-drive-joints-the-engineering ; https://robotics.techbuzzchina.com/reports/actuators-motors.html
- Overcapacity and margins: https://aiproem.substack.com/p/bodies-are-cheap-data-is-not-a-mid ; https://eu.36kr.com/en/p/3780414717129481 ; https://www.thexpin.com/p/china-humanoid-robot-supply-chain
- Base rates:
  - 3D printing: https://www.fool.com/investing/2016/08/23/3-beaten-up-3d-printing-stocks-are-they-bargains.aspx ; https://time.com/3916323/3d-printer-stocks/
  - Lithium: https://www.tikr.com/blog/albemarle-fell-10-this-week-heres-where-the-stock-could-go-in-2026 ; https://portfolioslab.com/symbol/LIT
  - Polysilicon: https://www.pv-tech.org/polysilicon-prices-remained-depressed-throughout-2024-when-will-they-rebound/ ; https://www.caixinglobal.com/2025-05-16/chinas-polysilicon-industry-slashes-output-to-record-lows-as-prices-collapse-102320054.html
  - Cobots (Teradyne): https://www.sec.gov/Archives/edgar/data/97210/000119312525258477/ter-20250928.htm ; https://www.therobotreport.com/teradyne-robotics-lays-off-another-14-of-workforce/
- Unitree CEO on AI: https://www.bloomberg.com/news/articles/2025-08-09/humanoid-robots-still-lack-ai-technology-unitree-ceo-says

**Team files (all figures there are snippet-sourced):** `robotics-supply-chain-moats.md`, `projection-2030.md`, `projection-2030-model-output.md`, `raw/01`-`raw/07` under `/home/user/debate-chatbot/reports/stocks/research/2026-09-19-robotics/`.

**UNVERIFIED, from memory:**
- Segway sales against its 10k/week claim.
- Lilium and Volocopter insolvencies (2024-25).
- Waymo timeline (2009 start → Oct 2020 driverless rides).
- Hesai on the 1260H list (Jan 2024).
- Albemarle's 2022 peak of ~$334.
- Lynas share count of ~1.0B, which drives the A$15.5B cap.

Reproduction scripts (scratchpad, not in the repo): `/tmp/claude-0/-home-user-debate-chatbot/7d77e5a7-be3d-5eeb-89ce-9125f9e0b7ad/scratchpad/audit.py` and `audit2.py`. Model under audit: `/home/user/debate-chatbot/scripts/robotics_2030_model.py`.

---

## Errata (QA review, 22 Sep 2026)

- The Lynas "about -14% at A$14-15B" estimate is superseded. The QA review found the base cap was in US dollars; the corrected model gives -14% at A$15.64B (1.0065B shares x A$15.54).
- Reuters (20 Sep 2026) describes window guidance that slows humanoid IPOs, not a freeze. The 60-70% valuation cut is Mech-Mind's CEO's estimate.
