# GLP-1 / Incretin Pen and Autoinjector Supply Chain: Sell-Side Research Note (as of 2026-09-22)

**Method and limits.** I ran about 40 WebSearch queries before the session's search budget ran out. Every WebFetch attempt was blocked by the egress proxy: sec.gov, ypsomed.com, pharmiweb, prnewswire. So all figures below come from search snippets, with the URL cited. Items tagged **[memory]** or **[calc]** are my own recollection or arithmetic and are not verified.

---

## (a) Summary table

| Component / layer | Top 3 suppliers (GLP-1 relevant) | Moat rating | Ticker | Bottleneck or commoditised? |
|---|---|---|---|---|
| Originator multi-dose pens (FlexTouch, KwikPen) | Novo in-house; Lilly in-house plus Resilience (CMO, KwikPen from early 2027); component molders (undisclosed) | Very high, but captive (no listed pure play) | NVO, LLY; Resilience is private | Unit need is falling because the market is moving to multi-dose |
| Outsourced disposable autoinjector platforms (1 mL / 2.25 mL) | Ypsomed (YpsoMate), SHL Medical (Molly), BD (Intevia) / Stevanato–Owen Mumford (Aidaptus) | High. The device is locked into the drug's approval as part of the combination product, and switching means new bridging and human-factors work | YPSN.SW; private; BDX; STVN / EMBC | Tight for next-generation drugs (MariTide, CagriSema, Viking); capacity is being added heavily |
| Disposable variable or fixed-dose pens for generics and biosimilars | Ypsomed (UnoPen), Haselmeier/medmix (D-Flex), Stevanato (Alina); also Nemera, Phillips-Medisize (Envoi), Chinese OEMs | Medium, falling toward low | YPSN.SW, MEDX.SW, STVN | Commoditising. Buyers dual-source, and Chinese OEMs sell white-label pens |
| Primary containers (cartridges, prefilled syringes) | BD (Neopak), Stevanato (Nexa / EZ-fill), Gerresheimer (Schott is also relevant but was not researched) | Medium-high, from regulatory qualification | BDX, STVN, GXI.DE | Balanced now. Was a contributor in 2022–24 |
| Fill-finish (the root cause of the 2022–25 shortages) | Novo (ex-Catalent sites), Lilly (Concord NC and others), CMOs (Resilience, Jabil-Pii) | High | NVO, LLY, JBL | Was THE bottleneck. Easing from 2026 |
| Device contract manufacturing / EMS | Jabil, Phillips-Medisize (Molex/Koch), Flex; also Sanner | Medium | JBL, private, FLEX | Capacity being added. Jabil opens a new GLP-1 site in FY27 |
| Assembly automation | ATS (ATS.TO), Mikron (MIKN.SW), Syntegon (private); also teamtechnik (Dürr), IMA | Medium, cyclical | ATS.TO, MIKN.SW | Past peak. Customers are digesting the 2024–25 order wave |
| Resins (POM, PC) | Celanese (Hostaform MT POM), Covestro (Makrolon LF PC), DuPont / BASF (Delrin, Ultraform; not verified) | Low-medium. Qualified grades with drug master files (DMFs) create switching friction, but volumes are small | CE, 1COV.DE, DD, BAS.DE | Commoditised; GLP-1 is a tiny share of volumes |
| Connected pens and add-ons | Novo (NovoPen 6 / Echo Plus; Biocorp Mallya), Medtronic InPen, Aptar | Low | NVO, MDT, ATR | Not a bottleneck. Adoption is small |

**Bottom line.** The scarce, pricing-power layer is the **outsourced autoinjector platform** for next-generation and third-party incretins. That means Ypsomed and SHL, and to a lesser degree BD and Stevanato. Generic pens and resins are commoditising. Automation is in a digestion phase. The shift to multi-dose KwikPen and FlexTouch cuts devices per patient-month from 4 to 1, but mostly inside Lilly's and Novo's own captive device chains.

---

## (b) Detail

### 1. Who makes Lilly's and Novo's pens

**Novo Nordisk: FlexTouch is essentially in-house (partly confirmed)**
- Hillerød, Denmark is the main fill-finish and pen site for global markets. Tianjin, China is being expanded for pen-injector assembly, and a $556M sterile-preparations expansion (1.4M sq ft) is due by 2027. ([pharmaceutical-technology](https://www.pharmaceutical-technology.com/uncategorized/novo-tianjin/), [BioSpace](https://www.biospace.com/novo-invests-556m-in-china-operations-to-boost-manufacturing-capacity), [formblends](https://formblends.com/articles/glp1-hub/where-is-ozempic-manufactured))
- One low-quality source says "every step" is in-house. That is **contradicted** by two facts:
  - Novo bought three Catalent fill-finish sites (Anagni, Brussels, Bloomington) for $11bn, inside Novo Holdings' $16.5bn Catalent deal, which closed in December 2024. ([Fierce](https://www.fiercepharma.com/pharma/novo-holdings-antes-165b-poach-catalent-selling-three-fill-finish-sites-novo-nordisk), [Yahoo](https://finance.yahoo.com/news/novo-holdings-completes-16-5-140830763.html))
  - Novo signed a long-term, Novo-co-funded supply deal with Ypsomed for YpsoMate autoinjectors in September 2023, covering 1 mL metabolic and "second-generation GLP-1" drugs. First capacity was due during 2025. ([Fierce](https://www.fiercebiotech.com/medtech/ypsomed-inks-deal-manufacture-glp-1-autoinjectors-novo-nordisk), [Ypsomed ad hoc](https://www.ypsomed.com/en/investors/ad-hoc-announcements/ad-hoc-detail-page/ypsomed-concludes-a-long-term-supply-agreement-for-large-quantities-of-autoinjectors))
- **Conclusion:** FlexTouch is Novo's own design and assembly. Next-generation autoinjectors are partly outsourced to Ypsomed.
- Multi-dose shift: an FDA-approved US Wegovy FlexTouch (9.6 mg/3 mL, four 2.4 mg doses) was reported as launching in August–September 2026. The source is a Substack, so treat it as low confidence. ([onthepen](https://onthepen.substack.com/p/exclusive-wegovy-flextouch-is-coming))
- Wegovy HD single-dose pen: US launch was expected in April 2026. The device supplier is not disclosed.

**Eli Lilly: in-house plus a CMO**
- Concord, NC ($2bn, opened June 2024) has a dedicated device-assembly building. High-speed robotic lines there assemble prefilled syringes into autoinjectors. ([pharmaceutical-technology](https://www.pharmaceutical-technology.com/projects/eli-lilly-parenteral-products-facility-concord/), [Fierce](https://www.fiercepharma.com/manufacturing/automation-robots-and-local-talent-guide-way-lillys-2b-north-carolina-injectables))
- On 30 July 2026 Lilly and Resilience announced a $750M expansion in West Chester, OH that adds **KwikPen production**. It creates at least 400 jobs and should be fully operational in early 2027. The partnership (since 2023) has already produced more than 150M doses. ([BusinessWire](https://www.businesswire.com/news/home/20260730073895/en/Resilience-and-Lilly-Invest-$750-Million-to-Increase-U.S.-Manufactured-Medicine-Supply))
- Zepbound KwikPen (four doses in one device) was FDA-approved on 23 February 2026, at $299/month for 2.5 mg. Mounjaro KwikPen already existed ex-US. ([CNBC](https://www.cnbc.com/2026/02/23/eli-lilly-launches-zepbound-obesity-drug-pen-one-month-doses.html), [Healio](https://www.healio.com/news/endocrinology/20260224/fda-approves-label-expansion-for-zepbound-to-be-used-with-eli-lillys-kwikpen))
- Lilly launched Zepbound vials via LillyDirect in August 2024. This bypasses the autoinjector completely. ([CNN](https://www.cnn.com/2024/08/27/health/zepbound-tirzepatide-new-vials))
- Component suppliers are **not disclosed**. Historically Rexam (later Berry Global, now Amcor **[memory]**) made insulin-pen sub-assemblies exclusively for Lilly in Europe from 2008. IDEO has been Lilly's design partner for about 40 years. ([outsourcing-pharma 2013](https://www.outsourcing-pharma.com/Article/2013/02/07/Lilly-drives-expansion-at-its-insulin-pen-manufacturing-plant), [IDEO](https://www.ideo.com/works/designing-pharmaceutical-excellence-with-eli-lilly))

### 2. Capacity constraints and root cause
- **Tirzepatide:** in shortage from 2022. FDA declared it resolved in October 2024 and reaffirmed that in a 19 December 2024 decision memo. ([FDA memo](https://www.fda.gov/media/184606/download), [Pharmacy Times](https://www.pharmacytimes.com/view/fda-affirms-tirzepatide-shortage-resolved-sets-transition-period-for-compounding))
- **Semaglutide:** declared resolved for all presentations on 21 February 2025. ([Pharmacy Times](https://www.pharmacytimes.com/view/fda-ends-semaglutide-shortage-listing-contributing-to-ongoing-legal-challenges), [BioSpace](https://www.biospace.com/business/novo-nearly-catches-up-to-lilly-clears-ozempic-and-wegovy-from-fda-drug-shortage-list))
- **Root cause:** a demand shock (semaglutide fills rose about 442%) running into **sterile fill-finish** as the binding constraint. Novo explicitly cited fill-finish when it bought the Catalent sites and expects filling capacity to rise gradually from 2026. ([labiotech](https://www.labiotech.eu/in-depth/novo-catalent-acquisition-trend/), [CNBC](https://www.cnbc.com/2024/02/05/novo-nordisk-parent-to-buy-catalent-to-expand-wegovy-supply.html))
- Device assembly was a secondary constraint. Syntegon said in marketing copy that "pens and autoinjectors are in greater demand than supply." ([Syntegon](https://www.syntegon.com/news/supporting-self-medication-with-cutting-edge-assembly-solutions/))
- No source was found tying the shortages to API supply. **2026 status: not on the FDA shortage list.**

### 3. Company detail

**Ypsomed (YPSN.SW): best-positioned listed pure play**
- **What it makes:** YpsoMate autoinjectors (1 mL, 2.25 mL Pro, 5.5 mL), UnoPen (disposable variable-dose pen), YpsoPen, YpsoFlow. Now a pure-play self-injection company after selling Diabetes Care to TecMed for about CHF 420M (~$517.7M). The sale was announced on 22 April 2025 and has since completed. ([MassDevice](https://www.massdevice.com/ypsomed-completes-diabetes-business-sale-tecmed/), [Fierce](https://www.fiercebiotech.com/medtech/ypsomed-carves-out-diabetes-business-512m-deal-focus-glp-1-self-injectors))
- **FY2025/26 (year to March 2026, reported 20 May 2026):**
  - Delivery Systems sales CHF 601.5M (+20%); EBIT CHF 195.5M (~33% margin).
  - Group sales CHF 731.0M; group EBIT CHF 246.1M, which includes the gain on the Diabetes Care sale.
  - Dividend CHF 4.40; net debt/EBITDA 0.8x.
  - Autoinjector sales +33.6%; a record 44 new projects won.
  - GLP-1s contributed about CHF 30–40M of the CHF 100M growth.
  - Sources: [Ypsomed](https://www.ypsomed.com/en/investors/ad-hoc-announcements/ad-hoc-detail-page/ypsomed-grows-20-in-core-business-and-wins-record-number-of-customer-projects), [Yahoo transcript](https://finance.yahoo.com/quote/YPSN.SW/earnings/YPSN.SW-H2-2026-earnings_call-417529.html)
- **Guidance:**
  - FY26/27: sales +12–15%; EBIT CHF 210–230M (at least 33% margin).
  - Mid-term: CHF 0.9–1.1bn sales and 30%+ margin by the end of the decade.
  - Q1 FY26/27: 14 new projects, led by large-volume autoinjectors. ([Ypsomed Q1](https://www.ypsomed.com/en/news-insights/news/press-releases/news-reader-detail-page/ypsomed-is-off-to-a-strong-start-in-2026-27))
- **Capacity:**
  - About CHF 1.5bn of capex over four years.
  - First high-capacity YpsoMate line being commissioned in Solothurn.
  - Schwerin II (construction from January 2025) doubles the German site.
  - Changzhou, China opened in June 2025.
  - Holly Springs, NC: CHF 200M (~$248M per Fierce), production from end-2027.
  - Sources: [Fierce](https://www.fiercepharma.com/manufacturing/swiss-auto-injector-specialist-ypsomed-invests-248m-build-facility-nc), [PlasticsToday](https://www.plasticstoday.com/medical/ypsomed-invests-200m-in-first-us-manufacturing-facility)
- **Unit volumes:** more than 100M UnoPens and more than 10M YpsoPens delivered cumulatively. ([Ypsomed blog](https://www.ypsomed.com/en/news-insights/blog/blog-detail-page/mastering-UnoPen-and-YpsoPen-success))
- **Valuation:**
  - CHF 344.60 on 19 June 2026; 52-week range 260.50–441.50.
  - Consensus target CHF 407 (9 analysts, range 309–475); TipRanks average CHF 373.67; 10 Buy / 1 Sell. ([Investing.com](https://www.investing.com/equities/ypsomed-holding-ag-consensus-estimates), [TipRanks](https://www.tipranks.com/stocks/ch:ypsn/statistics))
  - **[calc, memory]** About 13.6M shares gives roughly CHF 4.7bn market cap, or about 21–23x FY26/27 guided EBIT. The September 2026 price was not captured.
- **Moat:** platform lock-in through combination-product approvals, a Novo co-funded capacity deal, and a record project pipeline.
- **Biggest risk:** concentration on Novo, and next-generation launches (CagriSema etc.) slipping. Multi-dose pens and oral drugs cap the growth of 1 mL autoinjectors. Generic pen pricing pressures UnoPen.

**SHL Medical (private; Zug, Switzerland / Taiwan / US)**
- **What it makes:** Molly, Quanta and Reunite platforms, plus large-volume cartridge autoinjectors.
- **Capacity:** $220M, 360,000 sq ft automated plant in North Charleston, SC (opened around March–April 2025, 300+ jobs), for products including GLP-1 therapies. A Swiss site is coming. ([Fierce](https://www.fiercepharma.com/manufacturing/switzerlands-shl-medical-debuts-220m-autoinjector-plant-south-carolina), [Plant Services](https://www.plantservices.com/industry-news/news/55286085/shl-medical-invests-220m-to-open-autoinjector-manufacturing-facility-in-south-carolina))
- **Volumes:** six cardiometabolic combination products supported since 2015, and about 50M cardiometabolic devices delivered in 2023. ([SHL blog](https://www.shl-medical.com/news-insights/blog/navigating-global-self-injection-market-trends-regional-strategies))
- **Ownership and valuation:** founder Roger Samuelsson holds about 69%; EQT (via EQT Future) and Athos hold about 31%. Forbes put the value at about $2.1bn in 2020 and $3.4bn at end-2022. ([Wikipedia](https://en.wikipedia.org/wiki/SHL_Medical), [PE Hub](https://www.pehub.com/eqt-transfers-stake-in-shl-medical-to-eqt-future/))
- **Missing:** revenue, named GLP-1 customers, and any 2026 valuation.

**Nemera (private: Astorg / Montagu / LGT)**
- Makes pens and autoinjectors for GLP-1s. Built a custom reusable PenDURA AD pen for a generic GLP-1 maker.
- Bloomberg (28 August 2026): the owners are exploring a sale at about **€3bn ($3.5bn)**. The earlier Montagu-to-Astorg deal was about €1bn. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-08-28/astorg-montagu-said-to-eye-sale-of-glp-1-pen-maker-nemera), [Unquote](https://www.unquote.com/france/official-record/3012167/montagu-to-sell-nemera-in-eur1bn-sbo-deal))
- **Unverified:** one secondary source claims Nemera has "Wegovy and Zepbound" involvement, and that Novo and Lilly are customers.

**Haselmeier / medmix (MEDX.SW)**
- medmix H1 2026 (23 July 2026): revenue CHF 214.4M (−4.9%, −1.6% organic); adjusted EBITDA CHF 43.5M (20.3% margin). **Drug Delivery declined because a customer moved to dual sourcing.** FY26 guidance: flat to low-single-digit organic growth, about 20% margin. ([Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-medmix-posts-margin-gains-but-shares-fall-on-weak-h1-2026-sales-93CH-4807695), [StockTitan](https://www.stocktitan.net/news/MDMXF/medmix-strengthens-profitability-and-cash-flow-while-advancing-tvgsm2gmkajl.html))
- September 2026: D-Flex pen collaboration with Xeris. ([StockTitan](https://www.stocktitan.net/news/MDMXF/medmix-drug-delivery-haselmeier-to-support-the-development-of-xeris-u21wsh9noba2.html))
- This is direct evidence that disposable pens are commoditising.

**Owen Mumford, now part of Embecta (EMBC)**
- Embecta closed the deal on 15 May 2026 for up to $199.4–201M: $133M upfront plus a $66.4M earnout tied to Aidaptus sales.
- Owen Mumford's 2025 revenue was $92.3M. Stevanato is the exclusive manufacturing partner for Aidaptus.
- Embecta's B2B partners launched generic GLP-1s co-packaged with its pen needles in Canada and Brazil.
- Sources: [Fierce](https://www.fiercebiotech.com/medtech/embecta-buy-auto-injector-maker-owen-mumford-200m-diversify-beyond-insulin), [MedTech Dive](https://www.medtechdive.com/news/embecta-closes-owen-mumford-acquisition-for-up-to-201m/820489/)

**Stevanato (STVN)**
- Q2 2026: revenue €302M (+8%); adjusted EBITDA margin 26%. High-value solutions are 45% of revenue, and GLP-1-related products about 22–23%.
- Liraglutide products using its proprietary **Alina** pen won EU authorisations.
- FY26 guidance: €1.26–1.28bn revenue; EPS €0.53–0.55.
- Sources: [TipRanks](https://www.tipranks.com/news/company-announcements/stevanato-group-q2-2026-results-highlight-shift-to-high-value-drug-delivery-systems), [Simply Wall St](https://simplywall.st/stocks/us/pharmaceuticals-biotech/nyse-stvn/stevanato-group/news/how-q2-results-and-alina-glp-1-approvals-at-stevanato-group)
- **Risk:** generic pen pricing; syringe volume lost as the market moves to multi-dose cartridges.

**BD (BDX)**
- Targets a **$1bn GLP-1 drug-delivery business by 2030**.
- Won 19 of 23 new biologic prefilled-syringe approvals since 2023; holds more than 40 biosimilar agreements covering pens, autoinjectors and syringes.
- $110M Neopak prefilled-syringe line in Columbus, NE, with supply from mid-2026.
- Intevia is a 1 mL two-step autoinjector (up to 35 cP).
- Sources: [Fierce](https://www.fiercebiotech.com/medtech/bd-plans-surf-glp-1-wave-1b-drug-delivery-business-2030), [Contract Pharma](https://www.contractpharma.com/breaking-news/bd-to-invest-110m-to-expand-production-of-prefillable-syringes/)
- Segment financials and UltraSafe data were not captured.

**Gerresheimer (GXI.DE)**
- About $180M (€166M) expansion at Peachtree City, GA: more than 130,000 sq ft of cleanroom for inhalers and autoinjectors "for diabetes and obesity."
- Offers the Gx Inbeneo autoinjector.
- Its 2025 annual report showed "stable revenue in a challenging year." **2026 guidance was not found.**
- Sources: [Cleanroom Technology](https://cleanroomtechnology.com/drug-packaging-manufacturer-gerresheimer-expands-production-capacities-for), [Gerresheimer](https://www.gerresheimer.com/en/customer/company/news/detail/gerresheimer-publishes-2025-annual-and-consolidated-financial-statements-stable-revenue-in-a-challenging-financial-year)

**Contract manufacturers**
- **Jabil (JBL):** raised its FY26 revenue outlook to $34.0bn, citing GLP-1 drug-delivery strength. A new site dedicated to GLP-1 drug delivery starts in FY2027. Acquired the CDMO Pii (fill-finish) in February 2025. It says it delivers "hundreds of millions" of drug-delivery devices a year. GLP-1 revenue is not disclosed. ([Simply Wall St](https://simplywall.st/stocks/us/tech/nyse-jbl/jabil/news/how-jabils-higher-2026-revenue-outlook-and-glp1-exposure-at), [Jabil](https://www.jabil.com/industries/healthcare/pharmaceutical-solutions.html))
- **Flex (FLEX):** FY26 revenue $27.9bn (+8%), driven by AI and cloud. Health Solutions has no GLP-1 split. ([Flex ARS](https://www.sec.gov/Archives/edgar/data/0000866374/000130817926000368/flex015484-ars.pdf))
- **Phillips-Medisize (Koch/Molex, private):** Envoi pen (insulin and GLP-1), Aria smart autoinjector; more than 6,000 staff at 30 sites. ([Phillips-Medisize](https://phillipsmedisize.com/pharmaceutical/platforms/envoi-pen-injector/))
- **Sanner (private):** CDMO with the Springboard and Gilero design centres.
- **Credence (private):** announced a 2026 commercial supply agreement with an unnamed major pharma company. ([drug-dev](https://drug-dev.com/credence-medsystems-innovative-companion-safety-syringe-system-earns-multiple-industry-awards/))

**Assembly automation**
- **ATS (ATS.TO):**
  - FY26 (year to 31 March 2026): revenue C$2.97bn (+17.4%); net income C$71.7M.
  - Q4 bookings C$704M (−18.4%). Life-sciences bookings in Q4 came from areas *outside* GLP-1 autoinjector equipment.
  - Backlog C$1,958M (−8.5%). **GLP-1 is about 20% of the life-sciences backlog.**
  - Q1 FY27 (6 August 2026): revenue about C$694–698M (−5.2%); adjusted EPS C$0.35; net debt/EBITDA 2.9x; backlog about C$1.9bn.
  - In FY24, ATS said autoinjector revenue was a low-single-digit % of revenue and would rise toward high-single-digit %.
  - Sources: [BusinessWire Q4](https://www.businesswire.com/news/home/20260528259819/en/ATS-Reports-Fourth-Quarter-Fiscal-2026-Results), [StockTitan](https://www.stocktitan.net/sec-filings/ATS/6-k-ats-corp-ats-current-report-foreign-issuer-99549be45c73.html), [ATS FY24 MD&A](https://www.sec.gov/Archives/edgar/data/1394832/000162828024023696/ats-mdaxfy24q4.htm)
  - **Individual order figures and customer names were not found in snippets.**
- **Mikron (MIKN.SW):** H1 2026 sales −6% (−3.5% in constant currency). The CEO said the large GLP-1 and injection-device orders of 2024–25 are still being installed, which is delaying new orders. ([Investing.com](https://ca.investing.com/news/transcripts/earnings-call-transcript-mikron-posts-softer-h1-2026-sales-as-shares-slip-93CH-4739098))
- **Syntegon:** platforms run at 3–200 parts per minute. **No 2025–26 order data was found for teamtechnik or IMA.**

**Resins and connected devices**
- **Celanese Hostaform MT POM:** ISO 10993, drug master file, USP Class VI. **Covestro Makrolon M204/M402/M404 LF:** low-friction polycarbonate for autoinjector buttons. ([Celanese](https://www.celanese.com/products/medical-hostaform-pom-mt-acetal-copolymer), [Covestro](https://www.covestro.com/press/new-polycarbonates-meet-demands-for-drug-delivery-and-surgical-devices/))
- DuPont and BASF were not researched.
- **Novo bought Biocorp** (Mallya Bluetooth add-on, FDA-cleared December 2022) for €154M (~$165M). NovoPen 6 uses NFC. ([BioPharma Dive](https://www.biopharmadive.com/news/novo-nordisk-biocorp-smart-pen-diabetes-obesity/652167/))

### 4. Generics and new entrants: device implications
- **India:** launches on 21 March 2026.
  - Dr Reddy's Obeda, a prefilled disposable pen at about INR 4,200/month.
  - Alkem, disposable pen from INR 1,800.
  - Zydus, a *reusable* multi-dose pen.
  - Sun and Glenmark also launched.
  - ([Pearce IP](https://www.pearceip.law/2026/03/21/generic-semaglutide-launches-in-india-including-by-dr-reddys-zydus-alkem-sun-pharma-glenmark/))
- **Canada:**
  - Apotex's generic Ozempic approved 1 May 2026, launched 14 May.
  - Apotex's Sevmia, a generic Wegovy, approved 29–30 June.
  - Sandoz approved 18 September 2026 (2 mg and 4 mg pens).
  - ([Pearce IP](https://www.pearceip.law/2026/09/18/sandozs-generic-ozempic-semaglutide-approved-in-canada/), [Health Canada](https://www.canada.ca/en/health-canada/news/2026/06/canada-approves-first-generic-semaglutide-for-weight-loss.html))
- **China:** the semaglutide patent expired in March 2026, but data protection runs to April 2027, and Novo sees generics delayed until 2027. ([Bloomberg](https://www.bloomberg.com/news/articles/2026-05-06/novo-sees-generic-ozempic-delayed-in-china-until-next-year))
  - Liraglutide approvals: Tonghua Dongbao (December 2023, prefilled pen, 18 mg/3 mL), CTTQ (June 2024), Huadong.
  - White-label Chinese pen OEMs exist, e.g. Hangzhou Sunrise.
  - **The pen suppliers for these generics are not disclosed.** ([drugdu](http://media.drugdu.com/ddu-news/135-million-domestic-liraglutide-is-coming-fiercely.html))
- **Brazil:** only the Embecta co-pack mention was found.
- **Viking:** CordenPharma has committed to supply 100M autoinjectors a year plus 100M vial/syringe units for VK2735 (11 March 2025). The device OEM is undisclosed. ([Viking IR](https://ir.vikingtherapeutics.com/2025-03-11-Viking-Therapeutics-Signs-Broad-Manufacturing-Agreement-With-CordenPharma-to-Support-Commercialization-of-VK2735))
- **Amgen MariTide:** single-dose handheld autoinjector, monthly or less often. Supplier undisclosed.
- **Pfizer/Metsera (MET-097i / PF'3944):** 10 Phase 3 trials in 2026. Device undisclosed.
- **Retatrutide:** Lilly's device is undisclosed. Search results were dominated by grey-market "retatrutide pens," which points to a counterfeit and compounding risk.
- **Roche:** not researched.

### 5. Demand-side risks
- **Oral drugs:** the Wegovy pill was approved in December 2025 and launched in the US on 5 January 2026. Lilly's Foundayo (orforglipron) was approved on 1 April 2026, from $149/month self-pay. Early commentary says the pills are not taking much share from injectables. ([AJMC](https://www.ajmc.com/view/fda-approves-lilly-s-oral-glp-1-orforglipron-for-obesity), [MDDI](https://www.mddionline.com/drug-delivery/glp-1-pills-might-not-outperform-injectables-after-all))
- **Multi-dose pens:** Zepbound KwikPen and US Wegovy FlexTouch cut devices from 4 to 1 per patient-month. This is negative for single-dose autoinjector and prefilled-syringe volumes and positive for cartridges.

---

## (c) Unverified claims and missing data
- SHL is "on track to deliver 1.5 billion devices in 2025" (Plant Services snippet). This looks inconsistent with about 50M cardiometabolic devices in 2023. It may be cumulative, or a mis-snippet.
- "Novo does every step in-house" (formblends) is contradicted by the Catalent and Ypsomed deals.
- That Nemera's devices are used with Wegovy and Zepbound, and that Lilly is an SHL customer, comes only from secondary aggregators. Neither is confirmed by the companies.
- **ATS:** no individual large autoinjector order figures or customer names (e.g. Lilly) were found, even though the task said they were disclosed. The primary filings are needed.
- Owen Mumford deal value: $199.4M (Fierce) vs "up to $201M" (MedTech Dive).
- **[memory]** items: Ypsomed share count and the market-cap/multiple calculation; Rexam to Berry to Amcor lineage; DuPont Delrin ownership change; Pfizer's final Metsera price (about $10bn after the Novo bidding war; the initial offer was $4.9bn).
- **Not found:** Lilly autoinjector and KwikPen component suppliers; tooling lead times and precision-spring suppliers; Gerresheimer 2026 guidance; segment data for BD Pharmaceutical Systems, Flex Health and Jabil GLP-1; teamtechnik and IMA orders; Roche's device; Brazil generic launches; Medtronic InPen and Aptar data; SHL revenue.

## (d) Sources
- Ypsomed: [FY25/26](https://www.ypsomed.com/en/investors/ad-hoc-announcements/ad-hoc-detail-page/ypsomed-grows-20-in-core-business-and-wins-record-number-of-customer-projects) · [Q1 26/27](https://www.ypsomed.com/en/news-insights/news/press-releases/news-reader-detail-page/ypsomed-is-off-to-a-strong-start-in-2026-27) · [Call transcript](https://finance.yahoo.com/quote/YPSN.SW/earnings/YPSN.SW-H2-2026-earnings_call-417529.html) · [Novo deal](https://www.fiercebiotech.com/medtech/ypsomed-inks-deal-manufacture-glp-1-autoinjectors-novo-nordisk) · [TecMed](https://www.massdevice.com/ypsomed-completes-diabetes-business-sale-tecmed/) · [NC plant](https://www.fiercepharma.com/manufacturing/swiss-auto-injector-specialist-ypsomed-invests-248m-build-facility-nc) · [Consensus](https://www.investing.com/equities/ypsomed-holding-ag-consensus-estimates)
- SHL: [Fierce](https://www.fiercepharma.com/manufacturing/switzerlands-shl-medical-debuts-220m-autoinjector-plant-south-carolina) · [Wikipedia](https://en.wikipedia.org/wiki/SHL_Medical) · [SHL blog](https://www.shl-medical.com/news-insights/blog/navigating-global-self-injection-market-trends-regional-strategies)
- Nemera: [Bloomberg](https://www.bloomberg.com/news/articles/2026-08-28/astorg-montagu-said-to-eye-sale-of-glp-1-pen-maker-nemera)
- medmix: [Investing.com](https://www.investing.com/news/transcripts/earnings-call-transcript-medmix-posts-margin-gains-but-shares-fall-on-weak-h1-2026-sales-93CH-4807695)
- Embecta / Owen Mumford: [MedTech Dive](https://www.medtechdive.com/news/embecta-closes-owen-mumford-acquisition-for-up-to-201m/820489/)
- Stevanato: [TipRanks](https://www.tipranks.com/news/company-announcements/stevanato-group-q2-2026-results-highlight-shift-to-high-value-drug-delivery-systems)
- BD: [Fierce](https://www.fiercebiotech.com/medtech/bd-plans-surf-glp-1-wave-1b-drug-delivery-business-2030)
- Gerresheimer: [Cleanroom Technology](https://cleanroomtechnology.com/drug-packaging-manufacturer-gerresheimer-expands-production-capacities-for)
- Jabil: [Simply Wall St](https://simplywall.st/stocks/us/tech/nyse-jbl/jabil/news/how-jabils-higher-2026-revenue-outlook-and-glp1-exposure-at)
- ATS: [Q4 FY26](https://www.businesswire.com/news/home/20260528259819/en/ATS-Reports-Fourth-Quarter-Fiscal-2026-Results) · [FY24 MD&A](https://www.sec.gov/Archives/edgar/data/1394832/000162828024023696/ats-mdaxfy24q4.htm)
- Mikron: [Investing.com](https://ca.investing.com/news/transcripts/earnings-call-transcript-mikron-posts-softer-h1-2026-sales-as-shares-slip-93CH-4739098)
- Syntegon: [Syntegon](https://www.syntegon.com/news/supporting-self-medication-with-cutting-edge-assembly-solutions/)
- Lilly: [Concord NC](https://www.pharmaceutical-technology.com/projects/eli-lilly-parenteral-products-facility-concord/) · [Resilience KwikPen](https://www.businesswire.com/news/home/20260730073895/en/Resilience-and-Lilly-Invest-$750-Million-to-Increase-U.S.-Manufactured-Medicine-Supply) · [Zepbound KwikPen](https://www.cnbc.com/2026/02/23/eli-lilly-launches-zepbound-obesity-drug-pen-one-month-doses.html)
- Novo: [Catalent](https://www.fiercepharma.com/pharma/novo-holdings-antes-165b-poach-catalent-selling-three-fill-finish-sites-novo-nordisk) · [Tianjin](https://www.biospace.com/novo-invests-556m-in-china-operations-to-boost-manufacturing-capacity) · [Biocorp](https://www.biopharmadive.com/news/novo-nordisk-biocorp-smart-pen-diabetes-obesity/652167/) · [Wegovy FlexTouch US](https://onthepen.substack.com/p/exclusive-wegovy-flextouch-is-coming)
- FDA shortage status: [FDA memo](https://www.fda.gov/media/184606/download) · [Semaglutide](https://www.pharmacytimes.com/view/fda-ends-semaglutide-shortage-listing-contributing-to-ongoing-legal-challenges)
- Generics: [India](https://www.pearceip.law/2026/03/21/generic-semaglutide-launches-in-india-including-by-dr-reddys-zydus-alkem-sun-pharma-glenmark/) · [Canada Sandoz](https://www.pearceip.law/2026/09/18/sandozs-generic-ozempic-semaglutide-approved-in-canada/) · [Canada Apotex](https://www.apotex.com/global/news/news-release/2026/06/30/apotex-first-to-receive-health-canada-approval-for-sevmia-a-generic-semaglutide-for-chronic-weight-management) · [China](https://www.bloomberg.com/news/articles/2026-05-06/novo-sees-generic-ozempic-delayed-in-china-until-next-year)
- New entrants: [Viking](https://ir.vikingtherapeutics.com/2025-03-11-Viking-Therapeutics-Signs-Broad-Manufacturing-Agreement-With-CordenPharma-to-Support-Commercialization-of-VK2735) · [Pfizer/Metsera](https://www.fiercebiotech.com/biotech/pfizer-finalizes-metsera-buy-after-contentious-bidding-war-novo-nordisk)
- Oral drugs: [Foundayo](https://www.ajmc.com/view/fda-approves-lilly-s-oral-glp-1-orforglipron-for-obesity)
- Resins: [Celanese](https://www.celanese.com/products/medical-hostaform-pom-mt-acetal-copolymer) · [Covestro](https://www.covestro.com/press/new-polycarbonates-meet-demands-for-drug-delivery-and-surgical-devices/)
