# Universal `--digital-nomad` Section

Digital-nomad-specific filter: digital nomad visa (DNV) availability, internet quality, coworking density, time-zone overlap with major work hubs.

**Snapshot**: May 2026 (Tier-5 additions — 87 countries total).

## Universal contract

For the property's country, return:
1. **DNV available?** + thresholds + duration
2. **Internet quality** (Speedtest median, fibre coverage, 4G/5G mobile)
3. **Coworking density** (in city of interest)
4. **Time-zone overlap** with major work hubs (US-East/PT/UK/CET/IST)
5. **Tax residency trigger** (typical 183-day rule + special cases)
6. **Cost of living for nomad lifestyle** (city + restaurants + transit)
7. **Tax-treaty status** (with major source countries)

## Output template

```markdown
## Digital Nomad Profile

**Country**: <ISO2>
**DNV available**: <yes / no>
**Threshold**: <income/month or savings>
**Duration**: <max years>
**Internet (Speedtest median)**: <Mbps fixed / mobile>
**Coworking density**: <high | medium | low + count>
**Time-zone overlap (US-East / EU)**: <hours/day>
**Tax residency trigger**: <183 days standard / special>
**Cost of living tier**: <see compare table>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## DNV (Digital Nomad Visa) availability — Apr 2026 snapshot

### Active DNVs in skill-supported countries

| Country | Program | Threshold | Duration | Notes |
|---|---|---|---|---|
| **EE** | Digital Nomad Visa | €4,500 net monthly | 1-yr; no PR | Estonia first to launch (2020) |
| **HR** | Digital Nomad Visa | €3,622.50/mo (Jan 2026; 2.5× avg net) OR €43,470 lump | 18 months max, **NOT consecutively renewable** (6-mo cooldown) | Tax-exempt foreign income |
| **PT** | Digital Nomad Visa (D8) | €3,480/mo (4× SMN) | 1-yr renewable; PR after 5 yrs | Replaces tourist-visa workaround |
| **ES** | Digital Nomad Visa (Beckham-style) | €2,762/mo (200% min wage) | 1-yr→3-yr; flat 24% on Spanish income for 5 yrs | Active program, but property purchases NOT a route to citizenship after Apr 2025 GV repeal |
| **IS** | Long-Term Visa for Remote Work | ISK 1,000,000/mo (~€7,300) | 6 months (not extendable) | Short-stay only; NOT residency |
| **IT** | Digital Nomad Visa | €28,000/yr (~€2,333/mo) | 1-yr renewable | Tax residency trigger 183 days |
| **GR** | Digital Nomad Visa | €3,500/mo | 1-yr renewable; PR pathway 5 yrs | 50% tax discount first 7 yrs |
| **HU** | White Card | €2,000/mo | 1-yr renewable; max 2 years | Strict — no PR pathway |
| **CZ** | Zivnostenský (entrepreneur visa) | ~110,000 CZK savings + plan | annual renewal; PR 5 yrs | Not formally a DNV but used as one |
| **MT** | Nomad Residence Permit | €2,700/mo (€32,400/yr) | 1-yr renewable up to 4 yrs | Apply via Residency Malta Agency |
| **CY** | Digital Nomad Visa | €3,500/mo | 1-yr renewable up to 3 yrs | Tax residency trigger 183 days |
| **RO** | Digital Nomad Visa | ~3× avg gross salary (~€3,000/mo) | 1-yr renewable | |
| **MX** | Temporary residency (income-solvency proxy) | ~US$4,400/mo income OR ~US$74k savings | Renewable 4 yrs → PR | Not formally a DNV but used as one |
| **CR** | Rentista | US$2,500/mo (24 months) OR US$60k bank deposit | 2-yr renewable; PR 3 yrs | |
| **BR** | VITEM XIV — Digital Nomad | US$1,500/mo OR US$18,000 savings | 1-yr renewable once (max 2 yrs) | |
| **AL** | Unique Permit (Digital Nomad / Self-Employed) | 32,000 ALL/mo (~€385) OR 300,000 ALL (~€3,614) deposit | 1-yr renewable up to 5× (max 6 yrs) | Law 79/2021 |
| **JP** | Digital Nomad Visa | JPY 10M/yr income proof (~US$65k) | 6 months (NOT renewable in-country; not residency) | Launched Apr 2024; treaty-country nationals only |
| **TH** | DTV (Destination Thailand Visa) | THB 500k savings (~US$14k) + remote-employer / freelance proof | 5-yr multi-entry; 180 days/stay (extendable +180) | Launched mid-2024; replaces tourist-visa workarounds |
| **CO** | Migrante V — Visitante remote-worker | COP 5.25M ≈ US$1,671/mo (3× the 2026 SMMLV COP 1,750,905 at TRM 3,144.14 — computed) | 2 yrs (renewable) | Decreto 1209/2022 |
| **UY** | Digital Nomad Visa (Decreto 162/023) | ~US$1,500/mo income claim (declarative) | Initial 6 months → 1-yr extension | Live since 2023 |
| **CL** | Visa de Residencia Temporaria (DN sub-category) | No fixed threshold; remote-work contract required | 1-yr renewable | Used as DNV in practice |
| **ZA** | Remote Work Visitor Visa | ZAR 1M/yr (~US$54k) from foreign employer | 3-yr | Launched May 2024; Govt Gazette 50714 |
| **GE** | Remotely from Georgia | US$24k/yr OR US$2k/mo income | 360-day visa-free stay (most nationalities anyway) | Aug 2020; updated 2024 — informal in practice |
| **MY** | DE Rantau Nomad Pass | MYR 24k/mo (~US$5k) | 3-mo to 12-mo (renewable 12-mo) | Launched Oct 2022 |
| **KR** | Workation Visa (F-1-D) | ≥2× KR GNI per capita (~₩84M/yr 2026 — verify current GNI at HiKorea) | 1-yr renewable +1 | Launched Jan 2024; treaty-country nationals; not residency by itself |

### No specific DNV (use entrepreneur / business visa)

**FR, DE, BE, NL, LU, AT, CH, IE, UK** — alternative paths (Talent Passport, Freiberufler, DAFT for US, etc.). See `--visa` for details.

**SE, FI, NO, DK** — entrepreneur permits + remote work generally not DNV-classified.

**SK, SI, PL, BG, LT, LV, EE** — most have entrepreneur tracks; only EE has formal DNV.

**RS, ME, BA, MK, AL** — visa-free 90 days for many nationalities; longer needs business permit.

**CA, AU, NZ** — no DNV; ETA/work visa system; CA explicitly considering 2026.

**PA** — visa-free 180 days for 50+ nationalities is a de-facto nomad-friendly policy.

**US** — NO formal DNV; B-1/B-2 visitor (90-180 days) used as workaround for foreign-employer remote work; ESTA visa-waiver covers 90 days for VWP nationals. Remote-work-on-tourist-status is a grey area (USCIS has not formally blessed it).

**TR** — NO formal DNV (proposal floated 2024, not enacted as of Apr 2026); short-term residency permit (kısa dönem ikamet) for property owners is the practical route. Digital nomads informally use 90-day visa-free → residency renewal.

**AE** — Dubai **Virtual Working Programme** (1-yr, US$5k/mo income proof) and federal **Green Visa** for freelancers (5-yr, AED 360k income for 2 prior years) are the de-facto DNV equivalents. Not labelled "digital nomad" but functionally equivalent.

**DO, ID, VN, PH, IL, MA, EG** — NO formal DNV as of Apr 2026:
- **DO**: tourist 30-90 days; nomads use stay-extension workarounds
- **ID**: B211A visa (60-day, multi-extend up to 6 mo); a 5-yr DNV was proposed 2022 but not enacted
- **VN**: proposals tabled 2024-2025, none enacted; e-visa 90-day is the workaround
- **PH**: SRRV (Special Resident Retiree Visa, US$10k-50k deposit) used as nomad alternative; DNV proposed 2024
- **IL**: B/2 tourist (3-mo, extendable); NO DNV
- **MA**: Carte de Séjour (long-stay, 1-yr renewable) for nomads with 3-mo+ stay; DNV proposed 2024
- **EG**: tourist 30-90 days only; no formal DNV proposed yet

**QA, SA, PE, EC, PY, AM, AZ, TN** — DNV / remote-work pathways for Tier-4:
- **QA**: NO formal DNV; **Investor Residency Law 21/2018 ≥QAR 730k → 5yr renewable** is the practical longer-term route; tourist 30-day visa-free / e-visa for ~95 nationalities — verify with MoI / Hayya
- **SA**: NO formal DNV; **Premium Residency Vision 2030** (SAR 800k one-time / SAR 100k/yr renewable / Real-Estate-Owner SAR 4M) is the route; tourist e-visa 90 days for ~57 nationalities — verify with Premium Residency Center / Visit Saudi
- **PE**: NO formal DNV; tourist 90-180 days for many nationalities; **Rentista Visa USD 1,500/mo** is the practical remote-work route; verify with MIGRACIONES Peru
- **EC**: NO formal DNV; **Pensioner Visa USD 1,500/mo** + **Investor Visa USD 42,500** (~100×SBU 2026 SBU USD 470/mo) are the remote-work routes; tourist 90 days for many nationalities — verify with Cancillería Ecuador
- **PY**: NO formal DNV; **Resolución SET 1186/2023 reformed PR** — formerly cheapest formal RBI (~USD 5,200) → now USD 70k SUACE business invest OR active SET RUC; tourist 90 days for many — verify with DGM
- **AM**: NO formal DNV; visa-free 180d for ~92 nationalities (one of the most generous globally); **Investor Residency AMD 50M (~USD 130k) deposit OR property → 5yr renewable** is the longer-term route; **Citizenship by descent (Diaspora) Art. 13 streamlined** widely used by diaspora nomads — verify with Migration Service
- **AZ**: NO formal DNV; visa-free 90d for ~70 nationalities + ASAN eVisa; **TRP via real estate ≥AZN 100k (~USD 60k) → 1yr renewable to 5+** is the practical route — verify with State Migration Service
- **TN**: NO formal DNV (**Tunisia Investor Visa drafted 2024 NOT gazetted** — verify gazette status); visa-free 90d for ~80 nationalities; **Investor Residence Permit ≥TND 1M (~USD 320k)** is the longer-term route — verify with Ministère de l'Intérieur

**SG, HK, KR, TW, LI, MO, AD, MC, MD** — NO formal DNV as of May 2026:
- **SG**: NO formal DNV; **ONE Pass (S$30k/mo)** + **Tech.Pass** are the practical high-skill remote routes; tourist 30-90 days; remote-work-on-tourist-status not formally blessed by ICA
- **HK**: NO DNV; **Top Talent Pass / QMAS / IANG** are the routes for talent-class workers; tourist 90 days for many nationalities — verify with ImmD
- **KR**: **Workation Visa (F-1-D)** launched Jan 2024 — 1-yr (extendable +1 yr) for remote workers earning ≥2× KR GNI per capita (~₩84M/yr in 2026 — verify current GNI); also **Hi-Korea Digital Nomad** track via H-1 / Smart Card Workation pilot — verify with HiKorea
- **TW**: **Gold Card** (4-yr work + residency, no investment, high-skill applicants — 8 categories) is the practical DN-equivalent for qualifying skill-sets; standard visitor visa otherwise — verify with NIA / BOCA
- **LI**: NO DNV; quota-based residency only (~28 EEA + ~17 third-country/year); short-stay via Schengen extension 2011 for ≤90 days
- **MO**: NO DNV; tourist 30-90 days for many nationalities; Talent Programme 2024 NOT remote-work-targeted
- **AD**: NO formal DNV; **Residència Passiva** (~€600k OR €350k + €50k AFA) used as remote-base by some nomads; passive ≥90d/yr / active ≥183d/yr
- **MC**: NO DNV; carte de séjour (~€500k bank deposit) is the residency route; visitor 90 days for Schengen-eligible nationalities
- **MD**: NO formal DNV as of 2026 (proposals raised 2023-2024 but not enacted as of May 2026); tourist 90 days visa-free for many; Investor Residency Law 200/2010 (€250k 5yr) is the practical longer-term route

**IN, NG, KE, JO, OM, BH, KW, LB** — DNV / remote-work pathways for Tier-5:
- **IN**: NO formal DNV (proposals raised 2024 but not enacted as of May 2026); tourist e-visa 30/90/180-day for ~169 nationalities; **NO golden-visa via real estate (UNIQUE absence)** — India does NOT offer property-pegged residency or citizenship; **OCI lifetime multi-entry for Indian-origin descendants** is the practical longer-term route; LRS USD 250k/yr cap on outbound remittance — verify with MHA / Bureau of Immigration
- **NG**: NO formal DNV; tourist 90-day visa for many nationalities; **STR-1 Investor visa USD 100k business** is the longer-term pathway; nomads informally use 90-day tourist + extension; **security risk requires private security + gated communities + energy autonomy mandatory** — verify with NIS (Nigeria Immigration Service)
- **KE**: NO formal DNV (proposals raised 2024 but not enacted as of May 2026); tourist e-visa 90 days for ~150 nationalities; **NO golden-visa via real estate (UNIQUE absence in EAC)**; **Class K Resident Permit KES 200k+/yr passive income** is the practical longer-term pathway; **M-PESA mobile-money universal in admin (unique to KE)** — verify with Department of Immigration Services
- **JO**: NO formal DNV; tourist 30-day visa-on-arrival for ~118 nationalities; **CBI Jordan since 2018** (JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport, ~50 visa-free destinations — WEAK passport for mobility plays); **Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable)**; Aqaba ASEZ separate framework — verify with Ministry of Interior / Investment Commission
- **OM**: NO formal DNV; tourist e-visa 30 days for ~103 nationalities; **Investor Residency Royal Decree 89/2021** — 5-yr ≥OMR 250k (~USD 650k) ITC freehold / 10-yr ≥OMR 500k (~USD 1.3M) ITC; **Long-term Retiree Residence ≥OMR 4,000/mo pension (~USD 10,400)**; cyclone exposure HIGH baseline (Gonu/Mekunu/Shaheen) — verify with MoCIIP / ROP
- **BH**: NO formal DNV; tourist e-visa 14-day for ~115 nationalities; **Bahrain Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k) → 10-yr renewable Self-Sponsored Residence Permit**; **Golden Residency Decree 16/2022** 10-yr renewable for property owners ≥BHD 200k OR investors / talented / retirees (BHD 4k/mo); Saudi Causeway integration drives weekend medical-tourism flow — verify with Nationality, Passports & Residence Affairs
- **KW**: **NO golden-visa via real estate (UNIQUE absence in GCC)** — residency entirely via employment Iqama (Decree-Law 17/1959); citizenship effectively impossible (Decree-Law 15/1959); tourist e-visa 90 days for ~52 nationalities; remote-work-on-tourist-status not formally blessed; periodic political deadlock (parliament dissolved 2024) — verify with Public Authority for Civil Information / MoI
- **LB**: NO formal DNV; tourist 90-day on arrival for ~83 nationalities; **Investor Residency ≥USD 50k Lebanese business (1-yr renewable)**; property ownership ≥USD 200k can support residency application but not automatic; **post-2019 banking collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war Sep-Nov 2024** material to nomad cadence; Lebanese descent streamlined naturalization widely used by ~13M global Mahjar diaspora — verify with Direction Générale de la Sûreté Générale

## Internet quality (Apr 2026 best-available)

Speedtest Global Index country medians (Apr 2026 snapshot — verify https://www.speedtest.net/global-index for current).

### Tier 1 — fixed median ≥150 Mbps + 5G ubiquitous
🇸🇬 SG (consistently top-3 globally on Speedtest fixed + mobile per Ookla 2024-2026) · 🇰🇷 KR (gigabit fiber norm, KT/SK/LG) · 🇺🇸 US · 🇨🇭 CH · 🇫🇷 FR · 🇪🇸 ES · 🇸🇪 SE · 🇩🇰 DK · 🇳🇱 NL · 🇳🇴 NO · 🇳🇿 NZ · 🇨🇦 CA · 🇦🇺 AU · 🇯🇵 JP (1Gbps fibre standard urban) · 🇦🇪 AE (Dubai/Abu Dhabi etisalat/du fibre) · 🇭🇰 HK (gigabit FTTH ubiquitous urban) · 🇹🇼 TW (gigabit FTTH norm, Chunghwa/Taiwan Mobile) · 🇲🇨 MC (Monaco Telecom 5G) · 🇲🇩 MD (gigabit fiber Moldtelecom + Orange MD + StarNet — one of the highest fiber-penetrations in Eastern Europe per Ookla 2024-2026) · 🇶🇦 QA (Ooredoo / Vodafone Qatar 5G ubiquitous Doha)

### Tier 2 — fixed median 80-150 Mbps + 5G in cities
🇩🇪 DE · 🇬🇧 UK · 🇮🇪 IE · 🇧🇪 BE · 🇮🇹 IT · 🇵🇹 PT · 🇪🇪 EE · 🇱🇹 LT · 🇱🇻 LV · 🇨🇿 CZ · 🇸🇰 SK · 🇫🇮 FI · 🇮🇸 IS · 🇱🇺 LU · 🇲🇹 MT · 🇹🇭 TH (Bangkok/Chiang Mai AIS/3BB) · 🇮🇱 IL (Bezeq/Hot fibre) · 🇲🇴 MO (CTM + MTel + Smartone fibre + 5G urban) · 🇦🇩 AD (4G/5G via Andorra Telecom state monopoly; fibre Vaduz-style coverage urban) · 🇱🇮 LI (FL1 + Telecom Liechtenstein gigabit, Vaduz) · 🇸🇦 SA (STC / Mobily / Zain 5G Riyadh / Jeddah / Dammam) · 🇦🇲 AM (Beeline / VivaCell / Ucom fiber gigabit Yerevan) · 🇧🇭 BH (Batelco / Stc / Zain Bahrain 5G Manama ubiquitous) · 🇰🇼 KW (Zain / STC Kuwait / Ooredoo 5G Kuwait City) · 🇴🇲 OM (Omantel / Ooredoo Oman 5G Muscat)

### Tier 3 — fixed median 40-80 Mbps + 5G in capital
🇨🇾 CY · 🇬🇷 GR · 🇵🇱 PL · 🇭🇺 HU · 🇸🇮 SI · 🇭🇷 HR · 🇧🇬 BG · 🇷🇴 RO · 🇦🇹 AT · 🇲🇽 MX (CDMX/Monterrey) · 🇧🇷 BR (SP/Rio) · 🇨🇷 CR (San José) · 🇵🇦 PA (Panama City) · 🇹🇷 TR (Istanbul/Ankara Türknet/Turkcell) · 🇲🇾 MY (KL TM Unifi) · 🇨🇱 CL (Santiago Movistar/VTR) · 🇨🇴 CO (Bogotá/Medellín Movistar) · 🇿🇦 ZA (Cape Town/JHB Vodacom/MTN fibre) · 🇦🇿 AZ (Azercell / Bakcell / Nar 5G Baku) · 🇹🇳 TN (Tunisie Telecom / Ooredoo / Orange 4G/5G Tunis) · 🇪🇨 EC (Claro / Movistar / CNT fiber Quito / Cuenca) · 🇮🇳 IN (Jio / Airtel / Vi 5G — rapid 2024-26 rollout to top 100 cities; Bengaluru / Mumbai / Hyderabad gigabit fiber growing) · 🇯🇴 JO (Zain / Orange / Umniah 5G Amman; fiber Greater Amman growing)

### Tier 4 — variable, urban-centric
🇷🇸 RS · 🇲🇪 ME · 🇧🇦 BA · 🇲🇰 MK · 🇦🇱 AL · 🇦🇷 AR · 🇬🇪 GE (Tbilisi Magticom/Silknet) · 🇺🇾 UY (Montevideo Antel) · 🇩🇴 DO (Santo Domingo Claro/Altice) · 🇮🇩 ID (Jakarta/Bali Telkomsel/Indihome) · 🇻🇳 VN (HCMC/Hanoi Viettel/VNPT) · 🇵🇭 PH (Manila PLDT/Globe — speeds rising 2024-25) · 🇲🇦 MA (Casablanca/Rabat Maroc Telecom fibre) · 🇪🇬 EG (New Capital + Cairo/Alex Telecom Egypt fibre) · 🇵🇪 PE (Movistar / Claro / Entel — 5G Lima only) · 🇵🇾 PY (Tigo / Personal / Claro 4G/5G Asunción) · 🇰🇪 KE (Safaricom 5G dominant + Airtel + Telkom; **M-PESA mobile-money universal**; Nairobi fibre via JTL/Zuku) · 🇳🇬 NG (MTN / Glo / Airtel / 9mobile 5G limited Lagos / Abuja; **energy autonomy mandatory** — fibre via MainOne/IHS/Spectranet) · 🇱🇧 LB (Touch + Alfa 4G ageing — **NO 5G yet**; fibre via Ogero / IDM rebuilding post-2019 collapse)

**Reality check for nomads**: median speed often quoted is fibre-to-the-home in urban centers. Rural / coastal-village can drop to 4G / 30 Mbps. Always check the **specific address** before committing — many country playbooks include this in `--mains` (utilities) or `--amenities`.

## Coworking density (top nomad cities Apr 2026)

| City | Country | Coworking spaces (approx, NomadList) |
|---|---|---|
| Lisbon | PT | 80+ |
| Berlin | DE | 100+ |
| Madrid | ES | 70+ |
| Barcelona | ES | 90+ |
| Mexico City | MX | 60+ |
| Buenos Aires | AR | 50+ |
| Belgrade | RS | 30+ |
| Tbilisi | GE | 40+ |
| Tallinn | EE | 25+ |
| Tirana | AL | 15+ |
| Split | HR | 20+ |
| Athens | GR | 35+ |
| Valletta/Sliema | MT | 15+ |
| Bucharest | RO | 30+ |
| Bangkok | TH | 80+ |
| Chiang Mai | TH | 60+ (DN hotspot since pre-2020) |
| Bali (Canggu/Ubud) | ID | 60+ |
| Tokyo | JP | 80+ (WeWork strong; many cafés double as workspaces) |
| Dubai | AE | 70+ |
| Istanbul | TR | 50+ |
| Mexico City | MX | 60+ (also a TZ/LatAm hub for nomads) |
| Medellín | CO | 50+ (Laureles/Poblado) |
| Cape Town | ZA | 35+ (DN hub Q4-Q1 ZAF summer) |
| Buenos Aires | AR | 50+ |
| Montevideo | UY | 15+ |
| Santiago | CL | 30+ |
| Tel Aviv | IL | 45+ |
| Marrakech / Casablanca | MA | 20+ combined |
| Cairo | EG | 15+ |
| Kuala Lumpur | MY | 50+ |
| HCMC / Hanoi | VN | 40+ combined |
| Manila / Cebu | PH | 30+ combined |
| Singapore | SG | 100+ (WeWork, JustCo, The Working Capitol — among densest globally) |
| Hong Kong | HK | 80+ (Central / Wan Chai / Causeway Bay — Cyberport + Naked Hub) |
| Seoul | KR | 70+ (Gangnam / Hannam-dong / Pangyo — WeWork strong + FastFive + SparkPlus) |
| Taipei | TW | 50+ (Da'an / Xinyi / Neihu — CLBC + The Hive + Fab Cafe) |
| Macao | MO | 5-10 (small market; tourism + casino-economy dominant) |
| Andorra la Vella | AD | 3-5 (small ecosystem; ski-season nomad uplift in Encamp/La Massana) |
| Monaco | MC | 5-10 (boutique only; Riviera coworkers cross to Nice/Menton) |
| Vaduz | LI | 1-3 (tiny market; CH cross-border to Buchs/Sargans common) |
| Chișinău | MD | 10+ (growing ecosystem; iHUB + Castel Mimi-style + Generator co-led) |
| Doha | QA | 5-10 (small market; The Park Qatar / Astrolabs Doha minimal) |
| Riyadh | SA | 15-30 (growing; The Hub / Astrolabs Riyadh; Vision 2030 expansion) |
| Lima | PE | 50+ (Comunal / WeWork / Selina Lima Miraflores/Barranco) |
| Quito / Cuenca | EC | 15-25 combined (Selina / IMPAQTO Quito + Cuenca) |
| Asunción | PY | 5-10 (Loffice / CoLabora Asunción) |
| Yerevan | AM | 15-25 (IT-based hubs Tumo + Impact Hub Yerevan) |
| Baku | AZ | 5-10 (ABB Innovation Center / SOCAR business; oil-revenue stabilized economy + low crime) |
| Tunis | TN | 15-25 (Cogite / Wikistage Tunis; medical-tourism + tech overlap) |
| Bengaluru | IN | 100+ (WeWork / Awfis / 91springboard / Smartworks — **densest coworking ecosystem in South Asia**) |
| Mumbai | IN | 80+ (BKC / Powai / Lower Parel — WeWork / Awfis / Smartworks) |
| Delhi NCR (Gurgaon/Noida) | IN | 80+ (Cyber City / Cyber Hub Gurgaon — WeWork / Awfis / 91springboard) |
| Hyderabad | IN | 50+ (HITEC City / Gachibowli — IKeva / WeWork) |
| Pune | IN | 30+ (Koregaon Park / Hinjewadi — Awfis / Smartworks) |
| Lagos | NG | 25-40 (Workstation / Capital Square / Workbench / Regus VI/Ikoyi) |
| Abuja | NG | 10-20 (Cobloom / Capital Hub Abuja growing) |
| Nairobi | KE | 30-50 (iHub / Nailab / Workstyle / The Mint Hub — Westlands / Karen / Kilimani) |
| Amman | JO | 15-25 (ZINC / Beit Al Bawadi / Centro Connect Amman) |
| Muscat | OM | 5-15 (Ihroz / Oman Tech Fund / Spaces Muscat) |
| Manama | BH | 5-15 (Bru Coffee / Brinc / CoLab Manama) |
| Kuwait City | KW | 5-15 (Spaces / Sirdab / 360 MALL coworking) |
| Beirut | LB | 10-20 (Antwork / Coworking + Co / JoiBox / Cloud9 — operating with USD-LBP dual-pricing post-2019 collapse) |

For property-DD purposes: a coworking space within 15-min walk is a strong Tier-1 nomad signal.

## Time-zone overlap with major work hubs

For remote work, time-zone overlap with the team is critical. Hours per day in overlap (assuming 9am-6pm working hours).

| Country | TZ | US-East (ET) overlap | UK (GMT) overlap | CET overlap |
|---|---|---|---|---|
| US East/CA-East | ET | 9 hrs | 4-5 hrs | 3-4 hrs |
| US West/CA-West | PT | 5 hrs | 1-2 hrs | 0-1 hrs |
| MX, CR, PA | CT | 8 hrs | 3 hrs | 2 hrs |
| BR (SP) | BRT (-3) | 7 hrs | 3-4 hrs | 2-3 hrs |
| AR, UY, CL (winter), DO | -3 / -4 | 6-7 hrs | 3-4 hrs | 2-3 hrs |
| CO, EC, PE | COT/ECT/PET (-5) | 9 hrs | 4 hrs | 3 hrs |
| PY | PYT (-3 DST / -4) | 6-7 hrs | 3-4 hrs | 2-3 hrs |
| UK, IE, IS, PT | GMT/UTC | 5 hrs | 9 hrs | 8 hrs |
| MA | WET (UTC+1 perm. since 2018) | 4 hrs | 8 hrs | 9 hrs |
| EU (most) | CET | 4 hrs | 8 hrs | 9 hrs |
| FI, EE, LV, LT, GR, BG, RO, CY, MT (Eastern Europe) | EET | 3 hrs | 7 hrs | 8 hrs |
| ZA, EG, IL | UTC+2 / UTC+3 (no DST in ZA/EG; IL has DST) | 2-3 hrs | 7 hrs | 8 hrs |
| TN | CET (UTC+1, no DST) | 4 hrs | 8 hrs | 9 hrs |
| TR, QA, SA | UTC+3 (perm., no DST) | 2 hrs | 6 hrs | 7 hrs |
| GE, AE, AM, AZ, OM | UTC+4 | 1-2 hrs | 5 hrs | 6 hrs |
| IN | IST UTC+5:30 (no DST; unique half-hour offset) | 0-1 hrs | 3-4 hrs | 4-5 hrs |
| NG | WAT UTC+1 (no DST) | 4 hrs | 8 hrs | 9 hrs (same as CET) |
| KE, JO, BH, KW | UTC+3 (no DST except JO/LB) | 2 hrs | 6 hrs | 7 hrs |
| LB | EET UTC+2 / EEST UTC+3 DST | 2-3 hrs | 7 hrs | 8 hrs |
| TH, VN, ID (Jakarta WIB) | UTC+7 | 0 hrs | 2 hrs | 3 hrs |
| MY, PH, ID (Bali WITA UTC+8), SG, HK, TW, MO | UTC+8 | -1 hrs | 1 hrs | 2 hrs |
| JP, KR | UTC+9 (JST/KST, no DST) | -2 hrs | 0 hrs | 1 hrs |
| MD | EET (UTC+2, DST) | 3 hrs | 7 hrs | 8 hrs |
| AD, MC, LI | CET (UTC+1, DST) | 4 hrs | 8 hrs | 9 hrs |
| AU East | AEDT (+10/+11) | -2 hrs | -10 hrs | -8 hrs |
| NZ | NZDT (+12/+13) | -4 hrs | -11 hrs | -10 hrs |

**Best for US-team nomads**: LatAm (especially MX/CR/PA same TZ as US-Central; CO/DO same as US-East) > EU coastal-west (PT/ES) > rest of EU > MA (1-hr CET shift, 4-hr ET overlap) > ZA/IL/EG > GE/AE > AU/NZ/JP/SE-Asia (effectively next-day).

**Best for EU-team nomads**: Anywhere in EU (CET/EET) > UK > Iberian coast (PT/ES) > MA/ZA/EG/IL/TR (1-2 hrs offset, full overlap) > GE/AE (1-2 hrs ahead) > TH/VN/ID-W (3-hr ahead, half-day overlap) > MY/PH/JP (limited overlap) > LatAm (afternoon-evening overlap only).

## Tax residency trigger

Standard rule across most skill-supported countries:
- **183 days in 12 months → tax resident**
- Some countries also use "centre of vital interests" or "habitual abode" tests

**Special / shorter triggers (be careful)**:
- 🇨🇦 CA: ties to Canada (home, family, dependents) can trigger residency at <183 days
- 🇺🇸 US: substantial presence test (weighted 3-year) + citizenship-based
- 🇦🇺 AU: domicile + ordinarily-resident + 183 days + Commonwealth Superannuation tests
- 🇨🇭 CH: 30/90-day rule (lower than 183) — be careful for short stays

**Special / favorable**:
- 🇪🇪 EE: digital nomad / e-Residency does NOT confer tax residency by itself
- 🇲🇪 ME: 183-day rule but generally lenient enforcement
- 🇲🇽 MX: territorial-ish for residents abroad; 183 days triggers full tax-residency
- 🇦🇪 AE: 0% personal income tax; tax-residency cert available after 90/183 days (depending on type) — verify with FTA
- 🇬🇪 GE: 183 days OR "high-net-worth status" — territorial-ish; foreign-source income often exempt for non-resident-of-source treaty cases
- 🇹🇭 TH: 180 days = resident; **2024 reform** taxes foreign-source income brought into TH in same/later year (was previously exempt if remitted in next year) — verify with Revenue Department
- 🇲🇾 MY: 182 days = resident; foreign-source income exemption extended to 2036 for individuals (per Budget 2024)
- 🇺🇾 UY: **tax holiday** — new tax-residents can elect 11-yr exemption on foreign-source income (or 7% rate option)
- 🇿🇦 ZA: 183 days + continuous-91 test; worldwide-income basis once resident
- 🇺🇸 US: substantial presence test + citizenship-based — see top of section
- 🇯🇵 JP: 1 yr + "domicile" test → resident; foreign-source income exempted for first 5 yrs as "non-permanent resident" if not remitted to JP
- 🇸🇬 SG: 183 days = resident; **foreign-source income generally NOT taxed** for individuals received in SG; CGT NONE; verify with IRAS
- 🇭🇰 HK: territorial — only HK-source income taxable; no concept of worldwide PIT for individuals; physical-presence test for some Salaries Tax claims; verify with IRD
- 🇰🇷 KR: 183 days = resident; worldwide income; **foreign-source exemption first 5 of 10 yrs** for newly-resident foreign workers (PIT Act Art. 18-2); verify with NTS
- 🇹🇼 TW: 183 days = resident; **AMT regime** may apply on foreign-source >NT$7M; 6% surtax on certain investment income; verify with NTBT
- 🇲🇴 MO: territorial — Macao Professional Tax on MO-source only; foreign-source income generally NOT taxed; verify with DSF
- 🇦🇩 AD: 183 days OR centre of economic interest = resident; IRPF 0/5/10% lowest in Western Europe; verify with Departament de Tributs i Fronteres
- 🇲🇨 MC: residency confers **NO PIT** (except French nationals via 1963 Convention); NO CGT — tax-residence is the principal draw
- 🇱🇮 LI: 183 days OR habitual abode = resident; combined federal + commune ~2.5-22.4%; verify with Steuerverwaltung FL
- 🇲🇩 MD: 183 days = resident; flat 12% PIT on worldwide income (one of lowest in Europe); verify with SFS
- 🇶🇦 QA: 183 days = resident; **NO PIT** for individuals — corporate ~10% only; foreign-source pension/income NOT subject to QA personal taxation; verify with GAT (General Authority of Customs)
- 🇸🇦 SA: 183 days = resident; **NO PIT** for individuals (Saudi PIT regime is GCC-citizen Zakat 2.5% + corporate 20% non-Saudi); foreign-source income NOT subject to SA personal taxation; verify with ZATCA
- 🇵🇪 PE: 183 days = resident; worldwide income at progressive 8-30%; foreign-source income earned BEFORE arrival potentially non-taxable per Art. 6 LIR — verify with SUNAT
- 🇪🇨 EC: 183 days = resident; worldwide income at progressive 5-37%; foreign pension may be exempt under Art. 9 LRTI if double-tax treaty + source already taxed — verify with SRI
- 🇵🇾 PY: **Territorial PIT** — foreign-source income NOT subject to PY IRP; flat 8/9/10% on PY-source only; verify with SET
- 🇦🇲 AM: 183 days = resident; worldwide income at flat 21% PIT (2026 — verify SRC)
- 🇦🇿 AZ: 182 days = resident; worldwide income at progressive 14-25% (2026 — verify Min. Tax)
- 🇹🇳 TN: 183 days = resident; worldwide income at progressive 0-35% (2026 — verify Direction Générale des Impôts); 80% abatement on foreign pension under Art. 36 Code IRPP — verify
- 🇮🇳 IN: 182 days = resident (60-day shorter rule for Indian citizens with India-sourced income); worldwide income for residents at progressive 0-30% + surcharge + 4% cess; **LRS USD 250k/yr cap on outbound remittance**; treaty relief under DTAA — verify CBDT
- 🇳🇬 NG: 183 days = resident; worldwide income for residents at progressive 7-24% + 2.5% NHF (2026 — verify NRS, the Nigeria Revenue Service, formerly FIRS); minimal treaty network
- 🇰🇪 KE: 183 days OR ≥122 days/yr × 3 yrs = resident; worldwide income at progressive 10-35% PIT (2026 — verify KRA)
- 🇯🇴 JO: 183 days = resident; worldwide income at progressive 5-30% + 1% national-contribution PIT (2026 — verify ISTD / Income & Sales Tax Dept)
- 🇴🇲 OM: 183 days = resident (per Royal Decree 28/2009 / Tax Authority practice); **NO PIT for individuals** (Oman individual income-tax law drafted 2022 NOT enacted as of May 2026 — verify Tax Authority); foreign pension/income NOT subject to OM personal taxation
- 🇧🇭 BH: 183 days = resident; **NO PIT for individuals** — foreign pension/income NOT subject to BH personal taxation
- 🇰🇼 KW: 183 days = resident; **NO PIT for individuals** — foreign pension/income NOT subject to KW personal taxation; but **residency entirely via employment Iqama** (Decree-Law 17/1959)
- 🇱🇧 LB: 183 days = resident; worldwide income at progressive 4-25% PIT (2026 — verify MoF); **post-2019 banking collapse + currency dual-pricing (USD ↔ LBP)** material to tax-residency reasoning

## Cost of living for nomad lifestyle (1-bedroom + restaurants + transit)

### Cheap (<€1,500/mo)
🇦🇱 Tirana · 🇧🇦 Sarajevo · 🇲🇰 Skopje · 🇲🇪 Podgorica · 🇷🇸 Belgrade · 🇧🇬 Sofia · 🇷🇴 Bucharest · 🇲🇽 Mexico City (off-Polanco) · 🇦🇷 Buenos Aires (post-Milei) · 🇬🇪 Tbilisi · 🇪🇬 Cairo · 🇻🇳 HCMC / Hanoi · 🇵🇭 Manila / Cebu · 🇮🇩 Jakarta (off-Menteng) / Yogyakarta · 🇲🇦 Casablanca / Marrakech (off-Medina rentals) · 🇹🇭 Chiang Mai · 🇹🇷 Istanbul (post-2023 lira slide; verify in TRY at point of search) · 🇨🇴 Medellín / Bogotá · 🇩🇴 Santo Domingo (off-zona-colonial) · 🇲🇩 Chișinău (lowest COL in Europe — Numbeo 2024-2026) · 🇵🇾 Asunción (very low COL) · 🇪🇨 Cuenca / Quito (Cuenca lower than Lima/Bogotá per Numbeo) · 🇦🇲 Yerevan (moderate; appreciation 2022-24 from Russian-relocant wave) · 🇦🇿 Baku (off-Yasamal/Nasimi) · 🇹🇳 Tunis La Marsa / Sousse / Djerba (very low outside Tunis prime) · 🇮🇳 Bengaluru / Hyderabad / Pune / Chennai (Tier-1 metros; very wide COL band — Tier-3 cities much lower) · 🇳🇬 Lagos (off-VI/Ikoyi/Lekki) / Abuja (off-Maitama) · 🇰🇪 Nairobi (off-Karen/Lavington/Westlands/Runda) · 🇱🇧 Beirut (locals collapsed-wealth COL — fresh-USD COL inverts in expat zones)

### Mid (€1,500-2,500)
🇵🇹 Porto / Setúbal · 🇪🇸 Valencia / Malaga · 🇮🇹 Bari / Catania · 🇬🇷 Athens · 🇨🇿 Brno · 🇭🇺 Budapest · 🇵🇱 Warsaw · 🇨🇷 San José · 🇵🇦 Panama City · 🇲🇽 Guadalajara · 🇲🇾 Kuala Lumpur · 🇹🇭 Bangkok · 🇮🇩 Bali (Canggu/Ubud) · 🇿🇦 Cape Town (off-Atlantic-seaboard) / JHB · 🇨🇱 Santiago · 🇺🇾 Montevideo · 🇵🇪 Lima Miraflores / Barranco / San Isidro · 🇹🇳 Tunis (prime La Marsa / Sidi Bou Said) · 🇮🇳 Mumbai BKC / Bandra · 🇰🇪 Nairobi Westlands / Kilimani · 🇯🇴 Amman Abdoun / Sweifieh / Khalda

### Mid-high (€2,500-3,500)
🇵🇹 Lisbon · 🇪🇸 Madrid / Barcelona · 🇮🇹 Milan / Rome · 🇩🇪 Berlin / Hamburg · 🇫🇷 Lyon · 🇳🇱 Rotterdam · 🇮🇪 Galway · 🇲🇹 Sliema · 🇨🇾 Limassol · 🇪🇪 Tallinn · 🇧🇷 São Paulo · 🇮🇱 Tel Aviv (off-center) · 🇯🇵 Tokyo (off-23-ku) / Osaka · 🇰🇷 Seoul (off-Gangnam) · 🇹🇼 Taipei (off-Da'an / Xinyi) · 🇲🇴 Macao (residential off-Cotai) · 🇦🇩 Andorra la Vella · 🇴🇲 Muscat (Al Mouj / The Wave) · 🇧🇭 Manama (Seef / Diplomatic Area / Juffair) · 🇱🇧 Beirut Achrafieh / Verdun (fresh-USD)

### Expensive (€3,500+)
🇨🇭 Zurich · 🇳🇴 Oslo · 🇮🇸 Reykjavik · 🇱🇺 Luxembourg · 🇬🇧 London · 🇮🇪 Dublin · 🇸🇪 Stockholm · 🇩🇰 Copenhagen · 🇨🇭 Geneva · 🇫🇷 Paris · 🇳🇱 Amsterdam · 🇩🇪 Munich · 🇨🇦 Toronto/Vancouver · 🇦🇺 Sydney/Melbourne · 🇳🇿 Auckland · 🇺🇸 NYC / SF / LA / Boston · 🇦🇪 Dubai (Marina/DIFC) · 🇮🇱 Tel Aviv (center) · 🇯🇵 Tokyo (central 23-ku premium) · 🇸🇬 Singapore (consistently top-3 globally COL/rent — Numbeo 2024-2026) · 🇭🇰 Hong Kong (top-5 globally rent — Numbeo 2024-2026; lower than SG on housing per Knight Frank Q1 2025) · 🇲🇨 Monaco (Monte-Carlo — among the highest globally per Knight Frank Wealth Report) · 🇱🇮 Vaduz (CH-aligned, very high) · 🇶🇦 Doha (West Bay / The Pearl / Lusail — very-high COL) · 🇸🇦 Riyadh (DQ prime / Vision 2030 zones) · 🇰🇼 Kuwait City (Salmiya / Bayan / Mishref / Salwa prime)

## Tax-treaty cross-references

**Most tax treaties between OECD countries** prevent double taxation but require careful navigation:
- **183-day test in treaty article** — usually shifts tax residency
- **Tie-breaker rules** — residence > permanent home > centre of vital interests > habitual abode > nationality
- **Pension articles** vary — see `--retirement` for details

For US citizens specifically: **citizenship-based taxation** means worldwide income is taxed regardless of residency. **FBAR + FATCA** disclosure required for foreign accounts >US$10k. Tax treaty doesn't fully solve this; foreign-tax credit + foreign-earned-income exclusion (~US$130k 2026) help.

## Anti-hallucination

- **DNV thresholds change** — verify with the destination country's immigration portal
- **Speedtest median is national** — your specific address may be much slower (rural fibre lag)
- **Time zone overlap** changes around DST shifts — refine for your specific work-hour schedule
- **Tax residency rules** are stricter than 183 days in many countries (CH 30-day, CA ties test)
- **Coworking counts** are NomadList-style approximations — not exhaustive

## Status

Last refreshed: 2026-05-01 (Tier-5 additions — 87 countries total; Tier-5 added: IN, NG, KE, JO, OM, BH, KW, LB).

**Confidence**: MEDIUM — DNV thresholds and tax-residency cutoffs verified against destination immigration / tax authorities as of May 2026, but several reforms are in flight (TH 2024 foreign-source remittance change, JP DNV launched Apr 2024, ZA Remote-Work Visa launched May 2024, KR Workation Visa launched Jan 2024, UY tax-holiday election, MY foreign-source exemption to 2036, HK CIES reactivated Mar 2024, PY SET 1186/2023 reformed RBI, TN Investor Visa drafted 2024 NOT gazetted, SA Vision 2030 Premium Residency tiers, OM Investor Residency Royal Decree 89/2021, BH Property Visa Decree 6/2017 + Golden Residency Decree 16/2022, JO CBI since 2018, IN proposals 2024 NOT enacted as of May 2026, KE proposals 2024 NOT enacted, OM individual income-tax law drafted 2022 NOT enacted). Speedtest tier placements are urban-centric — rural fibre lags significantly in TH, ID, VN, PH, MA, EG, ZA, MX, BR, PE, EC, PY, TN, AZ, IN (Tier-3 cities), NG (outside Lagos/Abuja), KE (outside Nairobi/Mombasa); SG/HK/KR/TW/MD/QA/BH/KW/OM report exceptional fixed-line median speeds in their primary metros; LB has NO 5G yet (Touch + Alfa 4G ageing). Always verify the **specific address** via `--mains` / `--amenities`. Cost-of-living tiers compress under FX volatility (TR / EG / NG / LB especially — LB unique USD-LBP dual-pricing post-2019 collapse) — bands are EUR-equivalent at ~May 2026 rates.
