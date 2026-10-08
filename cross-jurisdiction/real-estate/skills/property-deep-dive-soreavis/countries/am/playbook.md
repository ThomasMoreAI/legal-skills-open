# Armenia (AM) — Property Due-Diligence Playbook

ISO2: `am`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

## Country profile

- **Population**: ~2.78 million (2024 ARMSTAT — Statistical Committee of the Republic of Armenia estimate); Yerevan (capital) ~1.08M, Gyumri ~120k, Vanadzor ~80k. Global Armenian diaspora ~7M (Russia ~2M, US ~1M, France, Argentina, Lebanon, Iran, Georgia) materially shapes property demand
- **GDP per capita**: ~US$8,000 (2024 World Bank / ARMSTAT preliminary); real GDP +12.6% 2022 (Russian-relocation shock), +8.3% 2023, +5.9% 2024 (ARMSTAT preliminary)
- **Currency**: **AMD** (Armenian dram). 1 USD ≈ **368 AMD** (2026-05-27 verified, source CBA reference rate); 1 EUR ≈ 395–410 AMD; managed-float — see `--currency`. AMD has strengthened materially through 2025–2026 vs the Q1 2026 ~385–400 band
- **Languages**: **Armenian** (official, Eastern Armenian standard, Armenian alphabet — Հայոց այբուբեն); **Russian** widely used (older generation, business, Russian-relocant cohort 2022–2024); **English** common in Yerevan tech + tourism + diaspora-return circles
- **EU status**: **NOT a candidate**. Armenia signed the EU **Comprehensive and Enhanced Partnership Agreement (CEPA)** in November 2017 (in force since 1 March 2021); EU candidacy pathway under public discussion 2024–2026 but **not formally lodged**. CSTO (Russia-led security alliance) participation **frozen February 2024** by PM Pashinyan — de facto suspension; formal exit pending
- **Postcode**: 4 digits (Yerevan `0001`–`0099` by district, e.g., Kentron `0001`–`0026`; Gyumri `3100`–`3199`; Vanadzor `2001`–`2078`)
- **Admin levels**: 11 marzes (provinces) including Yerevan as a separate marz-equivalent → 79 communities (`hamaynkner`) since 2021 enlarged-community reform → settlements
- **Cadastre**: **Cadastre Committee of the Republic of Armenia** (`Կադաստրի կոմիտե`) — `e-cadastre.am` is the unified online registry of immovable property + cadastral plans, supervised under the Government per Law on the State Registration of Rights to Property HO-295-N of 1999 and Law on Real Property of 1999. Title certificate (`Vkayakan` / Վկայական) issued post-registration
- **Identifier**: cadastral code (`kadastrayin tsats` / կադաստրային ծածկագիր) format `XX-XXX-XXXX-XXXX` (region.community.block.parcel) per Government Decision 822-N
- **Foreign-buyer rule**: **residential freehold OPEN to foreigners** (Civil Code Art. 184; Law on Real Property of 1999) — non-residents own same as citizens; **agricultural land BANNED** for foreign individuals + foreign legal entities under **Land Code Art. 4** — only Armenian citizens, Armenian legal entities (with Armenian ownership), the State, and communities may own ag land. LLC workaround with Armenian-citizen co-owners is common practice but title is contestable on enforcement (see Caveats)
- **Visa**: **180-day visa-free** within 1 year for ~92 nationalities (EU/EEA, UK, US, CA, AU, NZ, JP, KR, IL, GCC states + many CIS — verify per [MFA visa policy](https://www.mfa.am/en/visa/)) per Government Decision 1255-N of 2014 as amended; Armenia has one of the most permissive visa regimes globally for Western passports

---

## Section: `--price`

### Primary sources

- **ARMSTAT (Statistical Committee of the Republic of Armenia)** — `https://armstat.am/en/`
  - Quarterly **Real Estate Price Index** for Yerevan + national; published as separate Quarterly Bulletin "Prices in Real Estate Market of the RA"
  - Q4 2024 Yerevan apartment price index: ~+9% YoY (ARMSTAT bulletin Mar 2025); cumulative ~+50–60% nominal Yerevan since 2021 (Russian-relocation wave + IT-sector boom)
- **Cadastre Committee — e-cadastre.am**: `https://e-cadastre.am/` — full online title + ownership extract self-service (~AMD 10,000–15,000 standard, faster express options — verify current Cadastre tariff)
- **CBA (Central Bank of Armenia) Financial Stability Report**: `https://www.cba.am/en/Publication/` — mortgage debt stock + bank-side property-market commentary; CBA Macroprudential Reports
- **Yerevan Municipality Open Data**: `https://www.yerevan.am/` — selected market commentary, building-permit pipeline
- **e-register.am** (Government unified e-register portal): `https://www.e-register.am/` — entity + cadastre cross-check

### Price benchmarks (2024–2025 reference)

| Locality | New-build avg US$/m² | Resale avg US$/m² | Source |
|---|---:|---:|---|
| Yerevan (Kentron / Center, Northern Avenue, Cascade prime) | ~US$2,200–US$3,500 | ~US$1,800–US$2,800 | List.am aggregate Q4 2024; ARMSTAT bulletin |
| Yerevan (Arabkir, Kanaker-Zeytun, Davtashen middle) | ~US$1,500–US$2,200 | ~US$1,100–US$1,600 | List.am aggregate Q4 2024 |
| Yerevan (Erebuni, Malatia-Sebastia, Shengavit outer) | ~US$900–US$1,400 | ~US$700–US$1,000 | List.am aggregate Q4 2024 |
| Yerevan (Nor Nork, Avan, Nubarashen Soviet panelka periphery) | ~US$700–US$1,000 | ~US$550–US$800 | MyRealty.am 2024-Q4 |
| Gyumri | ~US$500–US$800 | ~US$300–US$550 | List.am aggregate 2025-Q1 |
| Vanadzor | ~US$450–US$700 | ~US$280–US$500 | List.am aggregate 2025-Q1 |
| Dilijan ("Armenian Switzerland", boutique) | ~US$1,000–US$1,800 | ~US$700–US$1,300 | List.am 2025-Q1 |
| Tsaghkadzor (ski) | ~US$1,200–US$2,500 (apt-hotel) | ~US$800–US$1,500 | Estate.am 2024 |
| Sevan (lakefront cottages) | n/a | ~US$400–US$900 | List.am 2025-Q1 |
| Rural village houses (Aragatsotn, Lori, Tavush, Vayots Dzor) | n/a | ~US$10,000–US$50,000 outright | List.am village segment |

> All US$/m² are **est.** (calibration: cross-checked against ARMSTAT price-index direction + ≥ 2 listing aggregators; primary-source US$/m² not published by ARMSTAT as headline — index-only). Most Yerevan listings priced in **US$** despite contracts denominated in **AMD** at CBA reference rate on signing day; verify exact figure on the day per CBA `https://www.cba.am/en/SitePages/Default.aspx`. **Yerevan saw ~50% peak nominal appreciation 2021–2023** driven by Russian relocant inflow + IT-sector growth; 2024–2025 plateau / mild correction depending on sub-segment.

### Listing platforms

- **List.am** (dominant general classifieds incl. real estate, the de facto monopolist): `https://www.list.am/en/category/60` *(per listing — verify with cadastre / on visit)*
- **MyRealty.am** (real-estate-specific portal with English UI): `https://www.myrealty.am/` *(per listing — verify with cadastre / on visit)*
- **Estate.am** (boutique agency network): `https://www.estate.am/` *(per listing — verify with cadastre / on visit)*
- **Yerevan.estate / Property.am** (newer aggregators) *(per listing — verify with cadastre / on visit)*
- **Realt.am** (long-running local) *(per listing — verify with cadastre / on visit)*
- Facebook groups (`Yerevan Apartments`, `Real Estate Armenia`, etc.) — high volume, never authoritative
- Telegram channels (`t.me/yerevanrealestate`, diaspora-return groups) — high volume, classifieds-grade

### Verdict bands (residential US$/m², Yerevan reference)

- 🟢 within ±10% of district segment median (per List.am / MyRealty.am, ≥ 5 comparables same street + condition)
- 🟡 ±20%
- 🟠 ±30% — investigate: pre-1988 panelka? Spitak-era retrofit status? Heat-network / individual-gas? Russian-seller exit-discount?
- 🔴 >±30% — significant red flag

### Compute

1. US$/m² = USD listing ÷ m² advertised. **Trap**: Soviet-era convention often advertised "general" m² including walls + balcony; modern Yerevan listings split "ընդհանուր / ընդհանուր օգտակար / բնակելի" (total / total usable / living) — confirm which figure
2. Compare to ARMSTAT Yerevan Real Estate Price Index YoY direction + sub-district segment benchmark
3. **Trap**: "preț negociabil" + USD pricing — actual deal often 5–15% below ask after first cadastre check, larger discount on Russian-relocant resale (2024–2026 cohort exits)
4. **Trap**: "գյուղական տուն" (village houses, often 30–120 km from Yerevan) priced as bargain often have NO mains drains + NO mains water (see `--mains`); budget +US$10,000–US$25,000 for habitability uplift
5. **Trap**: "կարկաս" (`karkas` = bare-shell new-build, brick + roof + utilities-stubbed but no finishing); finishing budget typically +US$200–US$400/m² (est. — verify per quote)
6. **Trap**: parking is rarely included in apartment price; expect US$10,000–US$30,000 for an underground space in central Yerevan (est. — verify per development)
7. **Trap**: balcony / "лоджия" included in advertised m²? Armenian convention typically includes them at 100% — confirm with developer

---

## Section: `--traffic`

### Primary sources

- **Ministry of Territorial Administration and Infrastructure (MTAI)**: `https://www.mtad.am/en/` — sectoral plans, road master plans, AADT-equivalent surveys on inter-state + republican roads
- **Armenian Roads Directorate (ARD, "Հայաստանի ավտոմոբիլային ճանապարհներ")**: subordinate to MTAI; annual traffic counts published as PDF reports — verify availability per current MTAI portal
- **Yerevan Municipality (Department of Transport)**: `https://www.yerevan.am/` — Yerevan traffic + public transport (metro single-line, bus, trolleybus)
- **OSM Overpass** — universal fallback (see `shared/amenities-osm.md`)

### Key term

**AADT** equivalent in Armenian: `միջին տարեկան օրական երթևեկության ինտենսիվություն` (mijin tarekan orakan ertevekuti'an intensivutyun) — often abbreviated `MTOEI` in survey reports

### Verdict bands (residential noise impact)

- 🟢 < 1,000 v/d (rural side road, side street)
- 🟡 1,000–5,000 v/d (small municipal road, urban side street)
- 🟠 5,000–20,000 v/d (urban arterial, M-route inter-state highway, secondary republican road)
- 🔴 > 20,000 v/d (Yerevan inner ring — Mashtots Ave, Tigran Mets Ave, Komitas Ave, Bagrevand St, Arshakunyats Ave; M1 Yerevan–Gyumri; M2 Yerevan–Goris–Iran border; M4 Yerevan–Sevan–Georgia border; M3 Yerevan–Vanadzor)

### Notes

- M-prefix = inter-state / republican highways; H-prefix = republican (state); local roads numbered per marz
- Yerevan private-vehicle fleet roughly tripled 2010 → 2024 per ARMSTAT transport stats; congestion now severe on Mashtots Ave, Tigran Mets, Komitas, Bagratunyats, Northern Avenue (pedestrianised core)
- **Yerevan Metro** (single line, 10 stations, opened 1981): runs Charbakh ↔ Davtashen-North; properties within ~600 m of metro station carry ~10–15% premium (est., per List.am district analysis 2024 — verify per listing)
- **Trap**: rural properties advertised "5 րոպե մայրուղուց" (5 minutes from highway) usually mean **on** a slip road or unpaved access — verify setback + paved access on visit
- **Trap**: Yerevan ring-road (`shrjanayin' chanaparh`) widening + bypass projects 2024–2027 EBRD/EU/ADB-funded; properties along corridor see noise+ during works phase

---

## Section: `--tax`

### Currency note

AMD, EUR/AMD ≈ 415–435 (Q1 2026 CBA, managed-float). Not in eurozone; no firm peg. CEPA-aligned but no ERM-II commitment (see `--currency`).

### Annual property tax — Real Estate Tax / Անշարժ գույքի հարկ (Tax Code Section 13, Articles 224–238 as amended)

Governed by [Tax Code of the Republic of Armenia](https://www.src.am/en/) Section 13 + **[Law HO-332-N, adopted 25 June 2020](https://www.arlis.am/hy/acts/143904)** (signed 30 June 2020, ՀՀՊՏ 2020.06.30/73(1628)) which introduced the major Real Estate Tax reform **in force 1 January 2021**, phased at 25 % of full rate for 2021, 30 % for 2022, 35 % for 2023, 50 % for 2024, 75 % for 2025 and 100 % from 2026 *(2026-09-18 verified, source ARLIS — Armenian Legal Information System)*. Rate **set as progressive AMD-bracket scale on cadastral value approaching market**, levied at **community level**:

**Residential apartments — 6 brackets (HO-332-N regime, Tax Code Art. 230; 2026-05-27 verified, source armenian-lawyer.com 2025 property-tax guide cross-checked vs src.am)**:

| Cadastral value bracket (AMD) | Rate |
|---|---|
| ≤ AMD 10M (~US$27k) | 0.05% |
| AMD 10M – 25M | AMD 5,000 + 0.1% on amount above 10M |
| AMD 25M – 47M | AMD 20,000 + 0.2% on amount above 25M |
| AMD 47M – 120M | AMD 64,000 + 0.4% on amount above 47M |
| AMD 120M – 200M | AMD 356,000 + 0.6% on amount above 120M |
| > AMD 200M (~US$545k) | AMD 836,000 + 1.0% on amount above 200M |

**Houses use a separate bracket schedule** (Tax Code Art. 230; 2026-05-27 verified, source armenian-lawyer.com): cut-offs at AMD 7M / 23M / 50M / 85M / 200M (not the apartment ones); confirm exact rate steps at src.am before final per-house computation. JAMnews-cited "1.5%" top rate conflates commercial schedule — residential cap is 1.0%.

**Phased implementation 2021–2026**: HO-332-N introduced a phase-in coefficient applied to the calculated tax — 25% in 2021, 30% in 2022, 35% in 2023, 50% in 2024, 75% in 2025, **100% from 2026 onward** (verify current schedule via src.am — the headline reform is fully phased in for tax year 2026).

**Cadastral value** maintained by Cadastre Committee on a market-approximation methodology since the HO-332-N reform — designed to converge to ~80–90% of market price for resale apartments (vs. pre-2021 nominal cadastral values often <30% of market). **Key 2026 effect**: full-rate first calendar year — many Yerevan owners will see materially higher property tax bills than 2024–2025 baselines.

**Land tax** — separate (Tax Code Art. 235):
- Agricultural land: per-hectare fixed rates by zone (cadastral category) — typically AMD 1,000–15,000/ha depending on irrigation + zone classification
- Non-agricultural land (residential plot under house): 1.0% of cadastral value (set by Land Code + Tax Code; verify via community tariff schedule)

### Example calculation

A US$200,000 (≈ AMD 73.6M at 368 AMD/USD, 2026-05-27 verified) Yerevan Kentron 2-bed apartment, Cadastre Committee cadastral value ~AMD 66M (~90% of market in HO-332-N regime):

- Apartment falls in **AMD 47M–120M bracket** (AMD 66M):
  - Calculated annual tax = AMD 64,000 + 0.4% × (66,000,000 – 47,000,000) = AMD 64,000 + AMD 76,000 = **AMD 140,000/yr**
  - **2026 fully phased in (100% coefficient)** → final bill ≈ **AMD 140,000 (~US$380 / ~€350)**
  - **2025 at 75% coefficient** → ≈ AMD 105,000 (~US$285)

A US$600,000 Yerevan Kentron premium apartment (AMD ~221M cadastral value):
- Falls in `> AMD 200M` bracket
- Calculated annual tax = AMD 836,000 + 1.0% × (221,000,000 – 200,000,000) = AMD 1,046,000 (~US$2,840 / ~€2,600) at full 2026 phase-in

> Property tax in Armenia under HO-332-N is materially higher than the pre-2021 regime but still moderate by W. European standard. **2026 first-full-year effect** is the dominant variable for prospective buyers — verify per Cadastre Committee extract before underwriting.

### Transaction taxes (one-time at purchase)

- **State duty (`petakan tursk` / պետական տուրք)** — Law on State Duty: **0.05% of purchase price** for cadastre registration of sale-purchase deed; nominal absolute amount even on US$500k transactions
- **Notary fee** — Law on Notary + Notarial Chamber tariff: **AMD 50,000–150,000 fixed** for typical sale-purchase deed (~US$130–US$390); sliding for high-value deeds — among the cheapest notarial regimes regionally
- **Cadastre Committee registration fee**: ~AMD 10,000–15,000 standard; faster express options (verify current tariff via cadastre.am)
- **VAT (DDS / ԱԱՀ)** — Tax Code Title 4:
  - **Standard rate 20%** (Art. 64)
  - **Residential dwelling first-sale by VAT-registered developer EXEMPT** under Tax Code Art. 64.2.1 (specific VAT exemption for residential)
  - Resale between individuals **exempt** (no VAT applies)
  - Construction services + materials remain at standard 20% VAT — feeds into developer cost stack
- **Total transaction cost** (buyer side, individual–individual resale): typically **0.1–0.5% of price** — **among the lowest in the world** alongside Georgia

### Capital gains tax — individual sale (Tax Code Art. 147(1)(16); 2026-05-27 verified, sources PwC Worldwide Tax Summaries Armenia + armenian-lawyer.com tax cheat sheet 2026 + GSL)

- **Individual-to-individual residential sale: EXEMPT from PIT** under Tax Code Art. 147(1)(16), **regardless of holding period or primary-residence status**. There is no statutory 1-year holding test — the prior playbook framing was wrong.
- **Sale by individual to a legal entity / sole-proprietor (acting as tax agent): 10% withholding tax** on transaction price for residential (20% on commercial), withheld and remitted by the buyer; this is a gross-price WHT, not a net-gain CGT
- **Recharacterisation risk**: if the individual habitually trades real estate in a business-like pattern, tax authorities may treat the activity as entrepreneurial → exemption is lost and standard regime applies
- **Sale by legal entity**: profit included in 18% Corporate Income Tax base (since 2020 reform)

### Personal income tax — general

- **20% flat PIT** for natural persons (Tax Code Art. 150) — adopted from 1 January 2020 transition, reaching final 20% flat rate from 2023 (vs prior 23%/26%/36% progressive). Effective 2024–2026.
- **Corporate income tax (CIT)**: 18%
- **Dividend WHT**: 5% (residents); 10% (non-residents)
- **VAT-registration threshold**: AMD 115M annual turnover (~US$300k)

### IT-sector-specific incentive — Law on State Support to IT Sector

⚠️ **MAJOR distinguishing fact for foreign buyers + remote workers**:

- **Law HO-105-N "On State Support to the Information Technology Sector"** (2014 original; multiple extensions; current extension to **31 December 2031** — verify current text via src.am): qualifying IT companies (incl. small startups + foreign-IT-employee individual entrepreneurs subject to size + activity caps) pay **1% turnover tax in lieu of CIT + VAT** for IT activity, **plus 10% PIT (vs standard 20%) on employee salaries** in the IT sector
- Eligible activities: software development, IT consulting, web design, IT services
- Headcount cap historically 30 employees (verify current statute scope)
- Material for property buyers because: (a) IT-relocant cohort is a dominant buyer segment in Yerevan 2022–2026; (b) foreign IT solo-founders can register IE substance in Armenia → 1% turnover regime → tax-residence pathway
- **Armenian IE / individual entrepreneur** (`anhat dzernarkat'irutyun`): register at State Revenue Committee (`Petakan Ekamutaneri Komite` / SRC) in 1–3 days; default 5% turnover tax for micro-revenue or 20% PIT on net depending on regime; IT-sector members opt into the HO-105-N 1% regime if eligible

### AML / cash limits

- Cash payments by legal entities to individuals: cap **AMD 500,000** per transaction per Law on Combating Legalization of Criminal Income (HO-80-N of 2008 as amended)
- Bank-to-bank wire is the standard channel for any transaction above the cash limit
- Notaries are AML "obligated entities" — must verify source of funds; politically exposed person (PEP) check mandatory
- **CBA Financial Monitoring Center** + Financial Action Task Force (FATF) Eurasian Group coordinate enforcement
- ⚠️ **Russia/Belarus-passport buyer scrutiny elevated 2022–2026** under EU + US secondary-sanctions concern; banks selective on opening accounts for Russian-citizen buyers despite Armenia not being EU/G7 sanction signatory

### Future risk

- **HO-332-N Real Estate Tax 2026 first-full-year effect**: many owners see materially higher bills than 2025 baseline; market-pricing impact still unfolding 2026
- **CEPA implementation deepening** (in force March 2021) drives EU-aligned reforms; expect tightening of beneficial-ownership transparency over 2026–2030 horizon
- **CSTO frozen February 2024** — geopolitical realignment may eventually impact foreign-buyer rules; no concrete bill 2026
- **Tax Code amendments** announced periodically via amendment laws; monitor `https://www.src.am/` + `https://www.parliament.am/` (National Assembly) + Government decisions

---

## Section: `--rental`

### Long-term residential

- **Individual landlord**: rental income taxed under PIT framework — standard 20% flat (Tax Code Art. 150) on net rental (gross minus documented expenses incl. property tax, repair, insurance, depreciation)
- **Simplified turnover tax option**: rental as IE under turnover tax can elect 5% turnover regime if total turnover < AMD 115M (~US$300k); contract registration with SRC standard
- No rent-control regime nationally; private-law contracts (Civil Code Art. 606+) govern
- Mandatory contract registration with SRC for tax compliance; failure exposes landlord to retroactive PIT + penalties

### Short-term rentals (STR / Airbnb / Booking)

#### Regulatory framework

- **Government Decision 1158-N of 2 August 2018** introduced registration framework for accommodation providers (`hyurnkalut'yan tsa'ratsutyun matuts'oghnerin grants'umy`) under the Tourism Committee (now under Ministry of Economy)
- Hosts must register accommodation and obtain classification certificate (1, 2, 3, 4, 5 stars or "guesthouse" / "apartment" tier) — enforcement uneven outside Yerevan Centre
- **Yerevan Municipal layer** (Decision of City Council, 2023–2024): supplementary STR registration at Yerevan Municipality level for properties advertised on platforms; verify current at `https://www.yerevan.am/`
- **Tourist tax** (`zbosashrtchakan tursk`): levied locally where adopted; Yerevan introduced ~AMD 200–500/night municipal tourist fee for accommodation establishments (verify current at yerevan.am — rate evolves)

#### Tax classification

- **Individual host**: register at SRC, file annual; effective tax 5% turnover (if elected and under AMD 115M cap) OR 20% PIT on net
- **Above AMD 115M annual turnover**: VAT registration mandatory (Tax Code Art. 60); STR over the threshold treated as accommodation services
- **CIT 18% if held via legal entity**; dividend WHT 5% on distribution

#### Practical (2025–2026)

- Enforcement of STR registration is **patchy outside Yerevan Kentron + Cascade**; estimated registration rate of platform-listed flats below 50% (per Tourism Committee inspection campaigns 2024 commentary — verify specific figures)
- **Trap**: HOA (`hama'ayns'eri kazmakerputyun`) bylaws often restrict STR in Yerevan newer developments (post-2015 stock especially) — check before buying
- **Trap**: pre-1988 panelka building entrance security + concierge typically NOT compatible with self-check-in; expect tenant-mix friction
- **Russian-relocant cohort 2022–2024 effect**: long-term rental supply expanded materially in Yerevan — gross rents 2024–2026 plateau / mild correction depending on sub-segment; STR market more resilient on tourism-demand side

### Strategic notes

- **Yerevan Kentron + Cascade + Northern Avenue**: highest year-round STR yield; tourism + business + diaspora-return + Russian-relocant tenant pool; estimated gross yield 6–10% on US$/m² basis (est., from Estate.am 2024 commentary — verify)
- **Dilijan + Tsaghkadzor + Sevan lakefront**: strong seasonal STR (May–Oct + ski Dec–Mar); shoulder-month occupancy thin
- **Long-term residential Yerevan**: gross yields commonly cited **5–8%** (List.am / Estate.am 2024 — verify against your specific listing); 2024–2026 yield compression from price appreciation 2021–2023 outpacing rent growth
- **Tourism 2022–2026 tailwind**: ARMSTAT recorded ~2.1M tourist arrivals 2023, ~2.3M 2024 (post-pandemic recovery + Russian-relocant + diaspora return + new direct flights); supports STR demand floor

---

## Section: `--work=<profession>`

### Job platforms

- **List.am/work** — classifieds-style, dominant general
- **Staff.am** — leading job board: `https://staff.am/`
- **MyJob.am** / **Job.am** — long-running general boards
- **HR.am**, **CareerCenter.am** — HR/recruiter-driven
- **LinkedIn Armenia** — active in IT, finance, BPO, NGO, diaspora-cross-border roles
- **Employment Agency of the Republic of Armenia (`Ashkhatank'i parteti petakan gortsakalut'yun`)**: `https://mlsa.am` — official labour portal, vacancy register

### Self-employment regimes (foreigners eligible with valid residence)

- **Individual Entrepreneur (`anhat dzernarkat`, IE)**: register at SRC in 1–3 days, ~AMD 5,000–15,000 fee; default 20% PIT on net OR 5% turnover regime if under AMD 115M cap
- **Patent regime** (fixed monthly fee): for low-turnover micro-business in narrow categories (taxi, hairdresser, etc.); foreign-individual eligibility constrained, verify per category
- **LLC (`sahmanapak pataskhanatvut'yamb dzernarkut'yun`, SAA)**: 1-day SRC e-registration; minimum capital AMD 50,000 (~US$130, nominal); 18% CIT on profit + 5% dividend WHT
- **Tax residency**: 183+ days in any 12-month period OR vital-interests centre in Armenia (Tax Code Art. 25)

### IT-specific incentive — Law HO-105-N "On State Support to IT Sector"

- **1% turnover tax** for qualifying IT residents in lieu of CIT + VAT for IT activity; **10% PIT** for IT employees (vs. standard 20%) — extended through **31 December 2031**; verify current scope via src.am
- Headcount caps + activity scope apply (historical 30-employee cap, software/web/IT services)
- Park membership of HighTech Park or equivalent science-park status grants additional incentives in some cases
- Materially competitive vs neighbouring Georgia (Virtual Zone 0% on export IT income) and Romania (12% IT-flat regime)

### Salaried benchmarks

- Average monthly nominal wage 2024 Q4 (ARMSTAT): **~AMD 290,000–310,000 gross** (~US$750–US$800) — economy-wide
- IT/finance Yerevan: ~AMD 600,000–1,500,000/month for mid-level (Staff.am market reports 2024) — IT premium pronounced post-2022 relocant inflow
- **Minimum wage**: **AMD 75,000/month** (set by Government Decision; revised periodically — verify at gov.am); apparent low headline masks substantial informal-economy participation in services sector

### Catchment heuristics

- Within 30 min of Yerevan central districts: full salaried opportunity (IT, BPO, finance, NGO, diplomatic, diaspora-cross-border)
- Gyumri: Tumo Center for Creative Technologies + emerging IT cluster + manufacturing; 30-min catchment limited
- Vanadzor: industrial / chemical legacy + IT ramp; thin
- Dilijan: UWC Dilijan (international school) + Central Bank Training Centre; very narrow professional niche
- Rural marzes (Tavush, Vayots Dzor, Syunik, Aragatsotn): agriculture + tourism + remittance economy; very thin local salaried market

### Visa / residence pathway for working foreigners

- **180-day visa-free** for ~92 nationalities (above) — covers business-trip / scoping / digital nomad stays
- **Temporary Residence Permit** (`zhamanakavor karuyts'`): 1-yr renewable, tied to employment / family / investment / property purchase / study; processing ~30 days via Migration Service of MoIA
- **Investor Residence** (Law on Foreigners Art. 18.4): **AMD 50M (~US$130k)** deposit OR property purchase of equivalent value → **5-year permit, renewable**
- **Special Residence Permit** (`Hatuk karuyts'`): **10-year** permit issued for ethnic Armenians (Diaspora) automatically + others case-by-case (cultural + scientific + economic significance) under Law on Foreigners Art. 21
- **Citizenship by descent**: streamlined for Armenian-heritage applicants (Law on Citizenship of the Republic of Armenia Art. 13) — no minimum residence required for ethnic-Armenian descent; document chain (genealogy, baptismal records, family certificates) is the practical hurdle
- **Naturalisation**: minimum **3 years** of permanent residence + Armenian-language test + Constitution test (Law on Citizenship Art. 13); **dual citizenship allowed** (since 2007 amendment) — Armenia is among the more permissive on dual citizenship

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Ministry of Internal Affairs — seismic risk reduction** | `https://mia.gov.am` | Seismic hazard maps / microzoning — **parcel-level microzoning data not publicly available at a live primary URL — verify with the Ministry of Internal Affairs (mia.gov.am)**; the former NSSP standalone site (`nssp-gov.am`) is retired and no successor body page was located (2026-09-18 verified) |
| **Ministry of Internal Affairs — Rescue Service** (`Ներքին գործերի նախարարություն — Փրկարար ծառայություն`) | `https://mia.gov.am` | Operational hazard data, evacuation, fire/flood/earthquake response — MIA created 30 Dec 2022 by force of law and absorbed the former Ministry of Emergency Situations' civil-protection, rescue and firefighting functions (2026 data, source MIA; 2026-09-18 verified) |
| **Hydromet Service** (under Ministry of Environment) | `https://www.armmonitoring.am/` | Weather, flood warnings, climate baseline |
| **Ministry of Environment** | `https://environment.gov.am/en/` | Environmental risk reports, NDC, climate strategy |
| **Geological Survey of Armenia** (under Ministry of Territorial Administration) | via mtad.am | Geological maps, landslide registry |
| **Public Services Regulatory Commission (PSRC)** | `https://www.psrc.am/` | Energy/utility safety regulation |
| **Yerevan Municipality (seismic-microzoning maps)** | `https://www.yerevan.am/` | Yerevan-specific microzoning per NSSP–municipal collaboration |

### Seismicity — material concern (the dominant Armenia property risk)

- Armenia sits on the **Lesser Caucasus collision zone** + Anatolian-Iranian plate boundary system — high seismicity (Mw 6–7+ historically possible)
- **1988 December 7 Spitak earthquake Mw 6.8**, surface rupture ~37 km, focal depth ~7 km — **~25,000+ deaths**, ~500,000 homeless; Spitak destroyed, Gyumri (then Leninakan) ~80% damaged, Vanadzor ~50% damaged. **Defines all current building-code calibration + retrofit policy.** Pre-1988 building stock is the dominant risk-bearing inventory
- **Other historical events**: 1840 Ararat Mw ~7.5; 1931 Zangezur Mw 6.4; 1968 Yerevan Mw ~5.8; ongoing Mw 4–5 swarms documented by NSSP
- Building code: **SNiP RA II-2.02-94** (Armenian seismic code, 1994 first post-Spitak codification, aligned with Russian SNiP and partly Eurocode 8) + **2020 update** (per MTAI / Urban Construction Committee) — **Yerevan designated seismic intensity zone 8–9 MSK**; design PGA ~0.30–0.40g per NSSP microzoning (verify per Yerevan-Gyumri-Vanadzor microzoning maps)
- **Pre-1988 Soviet panelka stock** (`khrushchyovka` / `seria 105 / II-29 / I-464A`): retrofit status uneven; some 1989–1995 demolition of unsafe Spitak-zone stock; many Yerevan/Gyumri/Vanadzor blocks remain in service. **Independent structural survey strongly advised** before purchase of pre-1988 multi-storey
- Yerevan + Gyumri + Vanadzor have published seismic-microzoning maps via NSSP collaboration with municipality — request from NSSP for parcel-level applicability

### Geopolitical risk — material concern (the dominant Armenia non-physical risk)

⚠️ **Nagorno-Karabakh (Artsakh) wars + Azerbaijan border tensions**:
- **Second Karabakh War September–November 2020**: Azerbaijan retook ~75% of pre-1994-status territory; ~6,500 deaths + ~90,000 displaced
- **Azerbaijan offensive 19–20 September 2023**: full Azerbaijani control over remaining Karabakh territory; **~120,000 ethnic Armenians displaced** to Armenia within weeks (one of fastest displacement events globally per UNHCR)
- **Armenia–Azerbaijan border**: ongoing tension along Tavush, Syunik, Vayots Dzor, Gegharkunik marz borders; sporadic ceasefire violations 2021–2024; "border-corridor" / "Zangezur corridor" demands by Azerbaijan unresolved
- **CSTO frozen February 2024** — Armenia de facto suspended participation in Russia-led security alliance; no formal exit yet
- **Property impact**: insurance underwriters apply elevated political-risk loading for Armenian property post-2020/2023; no widespread home-insurance war-exclusion shock yet but selective; Tavush + Syunik + Vayots Dzor border-area properties carry materially higher tail risk; Yerevan + Aragatsotn + Lori interior have been operationally normal throughout
- **Russia–Ukraine war (Feb 2022 →)**: indirect material impact via Russian-relocant capital + emigration inflows that drove Yerevan housing prices ~50% peak appreciation 2021–2023

### Flood

- Limited overall (semi-arid country); concentrated in spring snowmelt + summer convective storms
- **Rivers**: Aras (border with Iran/Turkey), Hrazdan (Yerevan), Debed (Lori), Vorotan (Syunik) — episodic flash-flood risk in narrow valleys
- **Major flood events**: 2010 Lori spring flood; 2015 Tavush flash flood; recurrent in low-lying areas of Hrazdan canyon
- **Verification path**: Hydromet Service flood-warning system; commune-level maps. For parcel-grade certification, request from Hydromet Service or commission private hydrological assessment

### Landslide / soil instability

- **Areni** (Vayots Dzor) — historical landslide register; **Tatev** (Syunik) — gorge-edge instability; **Lori marz** (post-1988 earthquake-triggered ground-instability legacy); **Dilijan** (Tavush) — forested-slope susceptibility
- **Verification**: Geological Survey of Armenia + commune-level master plans (`General Plans`) — request from community administration

### Drought

- **Hot semi-arid Yerevan basin + Ararat Plain + Vayots Dzor + Syunik**: increasingly drought-prone; agriculture stress (apricots, grapes, pomegranates)
- Armenia UNFCCC NDC + Fourth National Communication: ~+1.0–1.5°C warming since 1960; +1.5–4.5°C projected by 2080–2100 (RCP4.5 / RCP8.5)
- Ararat Plain irrigation-water-demand stress under increasing pressure 2025–2050

### Crime

- **Crime rate among the lowest in CIS region** + lower than EU mean for property + violent crime (per WHO mortality + UN Office on Drugs & Crime data)
- Yerevan walking-around safety high day + night; petty theft moderate in tourist zones; verify at commune-level via Police of Armenia statistics

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1920 (Tsarist + Russian Imperial)** | Soft-fired brick + lime mortar; many heritage-listed (Yerevan Kond + Old Quarter remnants); weak seismic performance; lead paint likely |
| **1920–1955 (early Soviet, Stalinist + reconstruction)** | "Stalinka" buildings; thicker walls, better than later panel; tuff-stone (volcanic) cladding common in Yerevan; asbestos in some roofing |
| **1955–1988 (Khrushchyov + Brezhnev panels, pre-Spitak)** | Khrushchyovka (5-storey), 9-storey + 16-storey panel (`seria 105 / II-29 / I-464A`); asbestos in joints common; aging utility risers; **uneven Spitak-era retrofit — dominant residual seismic risk inventory** |
| **1988–2000 (Spitak + post-Spitak crisis era)** | Reconstruction phase — new code SNiP RA II-2.02-94 enforced; mixed quality; Soviet-collapse + 1990s economic crisis impacted finishing standards |
| **2000–2010 (post-crisis recovery)** | Building boom Yerevan; quality varies; private-sector "narrow-front" infill common in Kentron — verify permits |
| **2010–2020 (mature recovery)** | Modern code; energy-efficiency requirements emerging |
| **2020–present (HO-332-N era + post-2020 Karabakh + Russian-relocant)** | Updated seismic code 2020 + EPC-equivalent emerging; HO-332-N RE-tax reform; relocant-driven new-build pipeline Yerevan Kentron + Davtashen + Achapnyak; quality strong on top-tier developers, mixed on mid-tier |

**Asbestos**: pre-2005 likely in roofing + insulation + heating-pipe insulation; no national mandatory removal regime — buyer due diligence required.

### Mandatory documents at sale

| Document | Required because | Notes |
|---|---|---|
| **Cadastre Committee extract (`Vkayakan` / Title Certificate)** | All sales | Verify owner + cadastral code + encumbrances (`grav` / mortgage, `arvets'um` / seizure) |
| **Sale-purchase contract** | All sales | Notarised; in Armenian; Cadastre Committee recordation within 30 days; contract may be bilingual Armenian + English with sworn translation |
| **Cadastral plan + technical passport** (`tekhnikakan andznagir`) | All sales | Issued by Cadastre Committee; ensure matches building footprint |
| **Energy efficiency declaration** | New build + transfer | Emerging requirement aligned with EU EPBD direction (CEPA-driven); enforcement uneven on resale — request and verify |
| **Building completion certificate (`shahagortsman'i handznelu act`)** | New builds + extensions | Confirms construction completed legally; often missing for pre-2007 self-built — affects future renovation/extension permits |
| **No-debt certificate** (utilities, building management fees) | Apartments in managed buildings | From building HOA — ensure no fund-debts attached to flat |
| **Heritage listing check** | Yerevan Kond + Old Quarter, Gyumri historic centre, regional historic towns | Ministry of Education, Science, Culture and Sports register — listing imposes severe renovation restrictions |

### Climate change projections (Armenia UNFCCC Fourth National Communication 2024)

- Mean annual temperature: +1.0–1.5°C since 1960; +1.5–4.5°C projected by 2080–2100 (RCP4.5 / RCP8.5)
- Annual precipitation: regional shift — Ararat Plain drier, mountain north slightly wetter; ±10–20% by 2080
- Drought frequency: doubling by 2050 in Ararat Plain + Vayots Dzor + Syunik; viticulture + horticulture stress
- Heatwaves: Yerevan summer days > 35°C projected to triple by 2050 (Hydromet Service scenario report 2024)
- Glacier loss: limited (Armenia has minimal glaciation); spring snowmelt timing shifting earlier
- **National Climate Adaptation Plan** + **Updated NDC** under Paris Agreement — verify current at mnp.am

---

## Section: `--mains`

### National database

- **PSRC (Public Services Regulatory Commission)**: `https://www.psrc.am/` — utility tariffs (electricity, gas, water + sewer where regulated)
- **Veolia Jur CJSC** (Veolia Group — **Unified Operator** under the trilateral lease contract of 21 Nov 2016, **15-year mandate running 1 Jan 2017 – end 2031**; target service coverage **~73% of Armenia's population**, consolidating the former Yerevan Djur, AWSC, Lori, Shirak and Nor Acounk service areas): `https://www.veolia.am/en` — water + sewer operator (2026 data, source Veolia Armenia; 2026-09-18 verified)
- **Electric Networks of Armenia (ENA)**: `https://www.ena.am/` — electricity distribution nationwide (single distributor, Tashir Group ownership post-2015)
- **Gazprom Armenia** (`Gazprom Armenia` / formerly ArmRosGazprom): `https://armenia-am.gazprom.com/` — gas distribution (Russia-owned, geopolitically scrutinised — see post-2022 caveats)
- **Yerevan Jermamatakararum** (district heating): limited residual DH service post-Soviet; most Yerevan apartments now individual gas boilers
- **High Voltage Electric Networks** (transmission): under Ministry of Territorial Administration

### Verification

1. Listing language:
   - "ջերմություն կենտրոնական" / `jermut'yun kentronakan` = central heating (residual; rare)
   - "ինքնավար" / `inknavar` = individual gas boiler (dominant in modern + retrofitted Yerevan)
   - "ջուր և կանալիզացիա կենտրոնական" / `jur ev kanalizats'ia kentronakan` = full mains water + sewer
   - "հոր" / `hor` = own well; verify potability + permit
   - "սանհան" / `sankhan` = no mains sewer (cesspit / septic)
2. **Yerevan urban core**: mains water + sewer assumed; **verify with Veolia Jur before signing** (rare patches of unconnected legacy stock exist on city periphery — Ajapnyak, Nubarashen)
3. **Gyumri + Vanadzor + marz centres**: mostly mains; verify with Veolia Jur regional operations
4. **Villages and dachas**: often water-only or seasonal water; sewer rare; many rely on cesspits

### Costs

| Scenario | Cost (US$, est.) |
|---|---:|
| Connection to existing nearby mains (urban) | ~US$300–US$1,500 |
| Mains drain extension (parcel where trunk line exists nearby) | ~US$1,500–US$5,000 |
| Borehole drilling (50–100 m, common depth) | ~US$2,500–US$8,000 |
| Septic tank install (typical residential) | ~US$1,200–US$3,500 |
| Modern WWTP (BIO compliance) | ~US$4,000–US$12,000 |
| Gas connection from street main | ~US$500–US$2,500 |

> All US$ ranges are **est.** based on Yerevan + Gyumri 2024–2025 contractor quotes aggregated from List.am trade-services classifieds + Veolia Jur + Gazprom Armenia published connection-charge schedules. Verify with 2+ quotes per project.

### Utility tariffs (2025–2026, regulated by PSRC)

| Utility | Tariff (residential, indicative) |
|---|---|
| **Electricity (ENA, ≤ 200 kWh/month)** | ~AMD 49–55/kWh (~US$0.13) — verify current PSRC schedule |
| **Electricity (> 200 kWh/month band)** | ~AMD 60–66/kWh (~US$0.16) |
| **Natural gas (Gazprom Armenia residential)** | ~AMD 161–165/m³ (~US$0.42) — subject to bilateral pricing reviews |
| **Water (Veolia Jur, Yerevan)** | ~AMD 180–230/m³ combined water + sewer |
| **District heating (residual Yerevan)** | thin / phased out; individual gas boiler dominant |

(Tariffs verified against psrc.am 2025 published schedules — confirm current rates; gas tariff particularly volatile due to bilateral Russia-Armenia supply pricing reviews.)

### Energy supply post-2022 context

⚠️ **Pre-2022 + post-2022 reality**: Armenia receives ~85% of natural gas via Gazprom (Russia) through the Iran–Armenia interconnector + Russia transit; ~85% of electricity via mix of nuclear (Metsamor NPP, ~30%) + thermal (Hrazdan, gas-fired) + hydro. **Russia–Ukraine war + CSTO suspension 2024** increase political-risk loading on energy supply chain; no immediate operational disruption but tariff + supply-chain volatility 2025–2027 expected as Armenia diversifies. Iran–Armenia gas-for-electricity barter remains backstop. Property buyers should expect ongoing tariff volatility 2025–2027 as energy diversification proceeds.

---

## Section: `--crime`

### Primary sources

- **Police of the Republic of Armenia** (`Hayastani Hanrapetut'yan Vostikanut'yun`): `https://www.police.am/` — national crime statistics, district-level
- **ARMSTAT criminal-statistics annual yearbook** (Statistical Yearbook, "Justice" chapter): `https://armstat.am/`
- **Prosecutor General's Office**: `https://prosecutor.am/` — prosecutorial statistics

### Headline (2024 Police of Armenia + ARMSTAT annual data)

- **Total registered crimes 2024**: ~32,000 (vs ~29,500 in 2020 — moderate uptick driven by reporting + post-Karabakh-displacement context)
- **Property-related crimes** (theft, burglary, fraud): ~50% of total registered
- **Yerevan municipality**: ~40% of national total registered crimes (population share ~39% — proportional)
- **Homicide rate 2023**: ~1.4 per 100k (Police of Armenia / ARMSTAT) — **among the lowest in CIS + below EU median**, declining trend since 2010

### Verdict bands (parcel-level inference)

🟢 Yerevan residential interiors (Arabkir, Kanaker-Zeytun, Davtashen, Achapnyak); Gyumri residential; Dilijan; rural marzes low-density villages
🟡 Yerevan Kentron tourist zones (pickpocketing, scam exposure); Erebuni + Shengavit + Malatia-Sebastia outer Yerevan; Gyumri Centre
🟠 Specific high-incidence localities flagged by police (verify per address) — limited
🔴 No specific routinely-flagged 🔴 zones in Yerevan; **border zones (Tavush, Syunik, Vayots Dzor)** flagged for political-tension tail risk rather than ordinary crime

### Verification

For parcel-level: request the local police precinct (`vostikanut'yan masnachyughy`) incident summary; informal but standard. Police of Armenia doesn't publish parcel-grade open data.

### Caveats

- Recorded vs actual: under-reporting moderate; tourist-zone pickpocketing under-reports
- Tourist destinations (Yerevan Kentron, Cascade) have inflated rates per inhabitant due to transient population denominator effect
- Border-marz crime statistics distort by military/security incidents — read separately

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`. Armenia is well-mapped on OpenStreetMap (Yerevan dense; villages thinner but improving via local mappers). Armenian + Russian + occasional English name tags; query with `name:hy` (Armenian) preferred, fallback `name:ru` + `name:en`.

**Brand-chain conventions**:
- **Supermarket chains**: SAS, Yerevan City, Carrefour (Yerevan + Gyumri), Nor Zovk, Evrika, Parma
- **Pharmacy chains**: Natali Pharm, Pharmacia, MedFarm
- **DIY / hardware**: Aiti-Asparez, Senset, Kotayk Hardware (Yerevan)
- **Bank ATM density**: Ameriabank, ACBA, Inecobank, Converse, Evocabank — universal urban; thin rural

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`. National source: Hydromet Service (`https://www.armmonitoring.am/`) + Ministry of Environment + Armenia UNFCCC Fourth National Communication 2024. Key projections: +1.5–4.5°C by 2080–2100; drought intensifies Ararat Plain + Syunik + Vayots Dzor; precipitation ±10–20%; viticulture + apricot belt stress; mountain snowmelt timing shifting earlier; minimal glaciation buffer.

---

## Section: `--finance`

### Mortgage market

- **Regulator**: [CBA — Central Bank of Armenia](https://www.cba.am/) — sets prudential rules, monetary-policy rate (CBA refinancing rate **6.5%** (2026-05-27 verified, source cba.am Monetary Policy Decisions log), down from the 2024 ~10% peak), loan-classification rules
- **Major banks** (CBA 2024 supervisory list, ~17 commercial banks): **Ameriabank** (largest; partial sale to Bank of Georgia 2023–2024), **ACBA Bank** (formerly ACBA-Crédit Agricole), **Inecobank**, **Converse Bank**, **Ardshinbank**, **VTB Armenia** (Russia-owned — sanction-watch sensitive), **Unibank**, **Evocabank** (digital-first), **AraratBank**, **Byblos Bank Armenia**, **Mellat Bank** (Iran-owned), **HSBC Armenia** (announced exit 2024–2026; Ameriabank acquisition completed)
- **LTV caps (residential, 2024–2026 CBA prudential guidance)**:

| Borrower | Max LTV |
|---|---:|
| Resident first-home buyer | typically **70–80%** |
| Resident second-home / investment | **50–70%** |
| Non-resident foreign buyer | typically **50%** if accepted at all (case-by-case) |

- **DTI / DSTI**: CBA caps debt-service at typically **40–50%** of net income; income evidence required (tax return + employment contract)
- **Rate structure (2024–2026)**:
  - **AMD-denominated mortgages**: typical 8–13% nominal; tied to CBA refinancing rate + bank margin
  - **USD/EUR-denominated mortgages**: typical 5–9% but **strict eligibility** (income in same currency or hedge demonstration); CBA tightened FX-loan rules post-2014 dram-volatility cycle
  - 15–25-year tenors standard; 30-year rare
- **Foreigner mortgages**: limited; most Armenian banks require resident status + Armenian tax residency + 12–24+ months income history. **Cash purchase is the standard foreign-buyer route.** Diaspora cohorts (US, French, Russian Armenian-passport holders) sometimes access lending via dual-citizenship status

### Banking access

- Account opening: **passport + Public Services Number (PSN, issued by SRC for foreigners on residence)** + proof of address + AML KYC (source-of-funds declaration)
- Non-resident accounts available at most banks for Western-passport holders; Russia/Belarus-passport holders face elevated CBA + bank-level scrutiny under EU + US secondary-sanctions concern post-2022 (Armenia not formal sanction signatory but bank correspondent risk material)

⚠️ **Armenian banking sector context**: well-supervised post-2014 dram-shock + 2018 Velvet-Revolution-era reforms; concentration in Ameriabank + ACBA + Inecobank + Converse + Ardshinbank + Unibank > 70% of system assets. **HSBC Armenia exit 2024–2026** reduces foreign-bank options materially; Bank of Georgia partial Ameriabank ownership 2023–2024 increased Caucasus regional integration.

---

## Section: `--currency`

### AMD — Armenian dram

- **Code**: AMD; subdivided into 100 luma; banknotes 1,000, 2,000, 5,000, 10,000, 20,000, 50,000, 100,000 AMD
- **Regime**: managed-float since 1993 (post-rouble exit); CBA intervenes to smooth volatility but does not target a fixed rate
- **Issuer**: [Central Bank of Armenia (CBA)](https://www.cba.am/) — sole issuer; reference rate published daily on `https://www.cba.am/en/SitePages/Default.aspx`

### Recent volatility (2022–2026)

- 2022 war shock + Russian-relocant inflow: AMD **appreciated materially ~25% vs USD** Mar 2022–Dec 2023 (atypical — most regional currencies depreciated); driven by ~US$3–5B+ Russian capital inflow + IT-sector expansion
- 2024–2025: range-bound 385–410 AMD/USD; mild AMD softening as relocant inflow stabilised + outflows on partial relocant departures
- **2026 to date**: AMD continued strengthening through H1; **~368 AMD/USD; ~395–410 AMD/EUR; CBA refinancing rate 6.5%** (2026-05-27 verified, source cba.am reference rates + Monetary Policy Decisions)

### What this means for buyers

- **USD buyers**: 2022–2024 saw **adverse FX move** (AMD strengthened) for USD-denominated buyers — property priced in USD became cheaper but contract-day AMD conversion was less favourable. Buyers who bought 2021 Q4 in USD effectively realised lower local-purchasing-power; 2024–2026 reversal partial
- **EUR buyers**: similar dynamic vs EUR; cross-rate volatility 2022 demonstrated 10–20% one-quarter swings
- **AMD-priced contract** is the legal requirement (Civil Code) — you negotiate in USD/EUR but **sign in AMD at CBA rate of signing day**; price-creep risk between offer + signing for foreign-currency-budgeted buyers (especially in volatile periods)
- **Hedging**: thin FX-forward market; bank-side hedging available at Ameriabank + ACBA for amounts > US$100k but spreads wide (50–150 bps for 90-day forward)
- **Capital controls**: minimal — no formal capital controls 2026; CBA has reserve power under monetary-policy law in crisis

### CEPA + EU integration trajectory

- CEPA in force March 2021; EU candidacy under public discussion 2024–2026 but not formally lodged
- **CSTO frozen February 2024** — geopolitical realignment; EU-aligned reforms accelerating
- ERM-II + euro adoption is **not on horizon**; Armenia's currency regime expected to remain managed-float through 2030+

### Tail risks

⚠️ Armenia is a small open economy with elevated geopolitical exposure (Russia–Ukraine war; Azerbaijan border tensions; CSTO suspension); AMD has experienced > 20% one-year moves in both directions (2014 depreciation; 2022 appreciation). **Russia-relocant capital is a major 2022–2026 dynamic** — inflows drove appreciation 2022–2023, partial outflows softening 2024–2026. Position-size foreign-currency-denominated buyers accordingly.

---

## Section: `--visa`

### Property-linked / investor schemes

| Scheme | Threshold | Visa | PR/citizenship path |
|---|---|---|---|
| **Investor Residence** (Law on Foreigners Art. 18.4) | ≥ AMD 50M (~US$130k) deposit OR property | 5-yr renewable | Naturalisation after 3 yrs continuous residence |
| **Special Residence Permit** (Law on Foreigners Art. 21) | Ethnic Armenian / cultural / scientific / economic significance | 10-yr | Auto for ethnic Armenian; case-by-case others |
| **Standard Temporary Residence** | Employment / family / study / property | 1-yr renewable | Naturalisation after 3 yrs |
| **Visa-free 180/365** | EU/EEA/UK/US/CA/AU/NZ/JP/KR/IL/GCC + many CIS (~92 nationalities) | 180 days/year | n/a |

### CBI / golden-visa status

- **No active CBI in Armenia as of 2026**. Armenia has never operated an investment-citizenship programme (unlike Moldova 2018, Cyprus pre-2020, Malta, etc.). **Citizenship pathway is via residence + naturalisation** (3 yrs PR) or **descent** (Armenian-heritage applicants) under Law on Citizenship Art. 13
- **Programme directly via property purchase**: Investor Residence Law on Foreigners Art. 18.4 — property purchase at AMD 50M (~US$130k) qualifies → 5-yr renewable residence (NOT citizenship directly)

### Pathway specifically for property buyers

- **Property purchase ≥ AMD 50M (~US$130k) confers Investor Residence eligibility** — 5-yr renewable; one of the lowest property-investor thresholds globally
- **Diaspora / ethnic Armenian buyers**: **Special Residence Permit (10-year)** issued automatically for ethnic Armenians under Law on Foreigners Art. 21 — material exit-optionality factor
- **Citizenship by descent**: streamlined for Armenian-heritage applicants under Law on Citizenship Art. 13; documentation chain (genealogy, baptismal records, family certificates) is the practical hurdle; no minimum residence required for descent applicants
- **Naturalisation**: 3 yrs PR + Armenian-language test + Constitution test; **dual citizenship allowed since 2007** — Armenia is among the more permissive on dual citizenship, attractive for diaspora returnees

### CSTO/CIS visa context

- CSTO frozen Feb 2024; CIS visa-free regime with Russia, Belarus, Kazakhstan, Kyrgyzstan operationally continues for now
- EU+US passport holders enjoy 180 days/yr visa-free — comparable to Georgia's 365 days/yr but materially more permissive than EU/Schengen 90/180

---

## Section: `--insurance`

### Mandatory

- **No nationally mandatory home-insurance scheme** for owner-occupiers; private market voluntary
- **Mortgage lenders mandate fire + structure cover** for any mortgaged property (standard practice; verify per bank)
- **Third-party liability** typically embedded in fire/contents bundle
- **MTPL** (motor) is the only universally mandatory insurance line

### Optional (standard market, 2024–2026)

| Cover | Typical premium (US$/yr, indicative) |
|---|---:|
| Building structure (Yerevan 2-bed, sum insured ~US$120k) | US$130–US$300 |
| Home contents (typical 2-bed) | US$50–US$150 |
| **Earthquake top-up** (material in Armenia given Spitak baseline) | +US$60–US$200/yr — verify sub-limit + deductible |
| Flood (riverine) | included in major bundles, sub-limit applies; verify Hrazdan/Aras zone |
| Liability (3rd-party) | usually bundled |

### Major insurers (CBA-supervised post-2008 insurance-supervision transfer)

- **Rosgosstrakh Armenia** (Russia-linked — sanction-watch sensitive)
- **Ingo Armenia** (largest non-life, broad book)
- **Sil Insurance**
- **Naïri Insurance**
- **RESO** (Russia-linked)
- **Armenia Insurance** (state-linked legacy)
- Compare via CBA supervisory list: `https://www.cba.am/en/Publication/`

### Climate + seismic + geopolitical loading

⚠️ Armenian insurers raising premiums 5–10%/yr 2023–2026 driven by 2020+2023 Karabakh political-risk re-pricing + 2020+2024 climate-event uptick + reinsurance market hardening; **earthquake sub-limits + deductibles tightening** for pre-1988 panelka stock; check policy schedule before signing. **War-exclusion clauses** to read carefully for Tavush/Syunik border-area properties — selectively excluded post-2020.

---

## Section: `--notary`

### Conveyancing process

Armenia is **civil-law**; **notary** (`notar`) mandatory for any immovable-property transfer per **Civil Code Art. 295 + Law on State Registration of Rights to Property HO-295-N of 1999**. Notary contract validated + transferred to Cadastre Committee for recordation. Notary licensed under Law on Notary HO-274-N of 2001, supervised by Notarial Chamber of the Republic of Armenia.

### Standard timeline

| Step | Day | What happens |
|---|---|---|
| 1. Pre-contract / preliminary agreement (`nakhnakan paymanagir`) | D0 | Buyer pays earnest deposit (`ardenagir` typically 5–10%); not strictly required but standard |
| 2. Cadastre extract pulled | D0–D7 | Buyer's notary or lawyer obtains current `Vkayakan` extract via e-cadastre.am |
| 3. AML / source-of-funds review | D0–D14 | Notary verifies; bank channel for any payment > AMD 500,000 cash-limit |
| 4. Notary sale-purchase deed signed | D7–D21 | Both parties present; original deed in Armenian; certified translation if buyer non-Armenian-speaking |
| 5. Cadastre Committee recordation | D7–D31 | Within 30 days of deed; Cadastre Committee issues updated `Vkayakan` reflecting new ownership |

### Costs

| Item | Typical |
|---|---|
| **Notary fee** (typical residential sale-purchase) | AMD 50,000–150,000 (~US$130–US$390 fixed; sliding for high-value deeds) |
| **State duty (`petakan tursk`)** | 0.05% of contract value |
| **Cadastre Committee recordation fee** | ~AMD 10,000–15,000 (~US$26–US$40) |
| **Translator (if required)** | ~US$80–US$300 |
| **Lawyer (optional)** | US$300–US$2,000 typically for foreign-buyer transactions |
| **Total transaction cost (buyer side, residential)** | **~0.1–0.5% of price** — among the lowest globally |

### Notary selection

- Notarial Chamber register: ~250+ notaries, mostly Yerevan
- **Buyer should engage independent notary** (not seller's) — common practice but not statutorily required

### Foreign buyer practical

- **Non-Armenian-speaker**: certified translator must be present at deed signing OR full bilingual deed + sworn translation
- **Power of Attorney**: foreign buyer can authorise Armenia-based representative via apostilled PoA (from country of residence) — common workaround if buyer not present in AM on signing day; **Russian-passport buyers** subject to enhanced source-of-funds scrutiny under bank correspondent risk post-2022
- **AML / source-of-funds**: notary required to obtain bank statements + source-of-funds; PEP screening mandatory; sanction-list screening expanded post-2022

---

## Section: `--compare`

### Armenia vs regional neighbours (residential investment lens, Q1–Q2 2026)

| Country | Foreign-buyer rule | Acquisition cost (typical) | Annual recurring | Yield (2024) | Currency |
|---|---|---:|---:|---:|---|
| **🇦🇲 Armenia** | Open (residential); ag banned for foreign individuals | 0.1–0.5% | 0.05–1.0% × cadastral value (HO-332-N progressive) | ~5–8% Yerevan | AMD managed-float |
| **🇬🇪 Georgia** | Open (residential); ag banned post-2017 | 0.1–0.5% | 0–1% × market (income-threshold) | ~6–10% Tbilisi | GEL managed-float |
| **🇦🇿 Azerbaijan** | Open w/ permit; ag banned for foreigners | 1–3% | low | ~5–7% Baku | AZN dollar-pegged |
| **🇹🇷 Türkiye** | Open w/ reciprocity; min purchase USD 200k for residence | ~5–8% | ~0.1–0.6% × market | ~5–8% Istanbul | TRY free-float (volatile) |
| **🇮🇷 Iran** | Restricted for non-residents | n/a (sanctions context) | n/a | n/a | IRR multi-tier |
| **🇲🇩 Moldova** | Open (residential); ag banned | 1.5–3% | 0.05–0.4% × cadastral | ~5–8% Chișinău | MDL managed-float |

### Armenia's distinctive position

- **Lowest property-acquisition tax of immediate region** (~0.1–0.5% vs Azerbaijan 1–3%, Türkiye 5–8%, Moldova 1.5–3%) — comparable only to Georgia
- **180-day visa-free for ~92 nationalities** — most permissive in the immediate region after Georgia (365 days)
- **Investor Residence at AMD 50M (~US$130k) property purchase** — among the lowest property-investor thresholds globally; comparable to Georgia (US$150k real-estate short-term residence permit since 1 Mar 2026; US$100k before) and materially below most EU programmes
- **Diaspora-citizenship pathway** (Law on Citizenship Art. 13) gives ethnic Armenian descent applicants direct citizenship route — unique structural advantage for diaspora property buyers
- **HO-332-N Real Estate Tax 2026 first-full-year effect**: materially raises annual carrying cost vs 2025 baseline; pricing impact still unfolding
- **War-spillover risk premium**: 2020 + 2023 Karabakh demonstrated meaningful tail risk; Azerbaijan border tension (Tavush/Syunik) and CSTO suspension elevate political-risk loading; insurance + cash-purchase prevalence reflect
- **IT-sector 1% turnover regime** (HO-105-N to 2031): unique in region for foreign IT-relocant property buyers; materially competitive vs Georgia Virtual Zone + Romania flat-12% IT
- **Russian-relocant 2022–2024 wave**: drove ~50% peak nominal Yerevan price appreciation 2021–2023; partial reversal 2024–2026; structural overhang on supply

### Comparative reference

For Armenia vs Georgia closest-analog comparison see `countries/ge/playbook.md`. For small-economy managed-float currency parallels see `countries/md/playbook.md` (Moldova). For high-seismic regional comparison see `countries/tr/playbook.md` (Türkiye, post-2023 Kahramanmaraş context).

---

## Section: `--retirement`

### Retirement to Armenia scenario

Armenia is a **niche** retirement destination — primarily for **diaspora-return** (ethnic Armenian heritage from US, France, Argentina, Lebanon, Iran, Russia) + **budget-conscious EU/US retirees** seeking sub-EU cost + cultural depth + favourable tax position. Not a Lisbon/Valencia/Mexico-tier mass-market retirement destination.

### Cost-of-living for retirees (Yerevan 2-bed apartment, conservative profile)

- Median 2-bed apt rental Q1 2026: ~US$500–US$1,000/month outside prime
- Public healthcare via Ministry of Health: limited coverage; out-of-pocket common; private insurance recommended
- Private health insurance for 65+: ~US$800–US$2,200/yr typical
- Public transport Yerevan: AMD 100/ride (~US$0.26); senior concession via Yerevan Card
- Utilities (2-bed apt): ~US$80–US$200/month winter peak; ~US$40–US$80 summer

### Tax position for retirees

- **Foreign-source pension income**: typically taxed at **20% PIT** if AM-resident (Tax Code Art. 150); **double-tax treaties** (Russia, Iran, Greece, Bulgaria, China, India, Romania, Cyprus, Germany, France, UK, US — verify per source country) may credit/exempt
- **Individual-to-individual residential sale: EXEMPT from PIT** under Tax Code Art. 147(1)(16) regardless of holding period (2026-05-27 verified, source PwC + armenian-lawyer.com); 10% WHT on price applies only when the buyer is a legal entity / sole-proprietor acting as tax agent
- **No wealth tax**, no inheritance tax — Armenia doesn't levy estate/inheritance tax (verify per Tax Code; intra-family transfers typically exempt)
- **HO-332-N Real Estate Tax** (annual property tax, fully phased in 2026) is the dominant carrying cost — material for high-value Yerevan Kentron retirees

### Healthcare access

- **Public** system: Ministry of Health hospitals + community clinics; quality variable; tertiary in Yerevan
- **Major private**: Erebouni Medical Center, Astghik Medical Center, Nairi Medical Center, Wigmore Clinic, Izmirlyan Medical Center — all Yerevan
- ⚠️ Specialist + advanced-oncology often referred to Russia, Türkiye, Israel, Germany, US under family-network arrangements; diaspora returnees typically retain home-country tertiary access

### Verdict for retirement-first buyers

🟡 **Watch** — viable for diaspora returnees + budget-conscious EU/US retirees willing to bridge to Türkiye/Russia/Israel/Germany for tertiary healthcare; strong fit for cultural-heritage + Armenian-Apostolic-Church-engaged retirees + Caucasus-cycle expat retirees. Best fit: diaspora returnees, Armenian-language/heritage retirees, semi-retired with private health insurance + flexible international medical access. Friction: thin specialist healthcare market, geopolitical tail risk (Azerbaijan border, CSTO suspension), HO-332-N RE-tax 2026 first-full-year cost increase.

---

## Section: `--digital-nomad`

### Visa pathway

- **No formal "digital nomad visa"** as of 2026 (compared to PT-D8 / ES-DNV / EE-DNV)
- Practical pathways:
  1. **Visa-free 180/365** for ~92 nationalities — covers significant remote-work stays (180 days/year is generous globally)
  2. **Investor Residence** at AMD 50M (~US$130k) property/deposit — overkill for typical DN
  3. **Employer-sponsored work residence** — only if AM-employer-tied
  4. **HO-105-N IT Sector status** for IT professionals registering substance — if turnover and activity criteria met (1% turnover tax)

### Connectivity

- **Internet**: Armenia ranks materially above regional median for fixed-broadband speed; UCom + Beeline (now Team) + Rostelecom-Armenia + Telecom Armenia offer 1-Gbps fibre at ~US$15–US$30/month residential — among cheapest globally
- **Mobile**: UCom + Team (Beeline) + Viva-MTS — 4G ubiquitous Yerevan + marz centres; 5G launched limited in Yerevan 2024; ~US$10/month for 50+ GB
- **Co-working Yerevan**: Impact Hub Yerevan, Loft Yerevan, Workshop Yerevan, FabLab + Tumo (programming-academy adjacent), Hyfen — US$80–US$250/month hot desk
- **Time zone**: UTC+4 (no DST since 2011) — favours Asia + Middle East asynchronous work; 9–11 hr gap to US Pacific; 2–3 hr gap to W. Europe

### Cost-of-living for remote worker (Q1 2026)

- Studio short-let Yerevan Kentron: US$500–US$1,000/month
- 1-bed apt long-term: US$450–US$900/month outside prime
- Single-meal mid-range: US$8–US$20
- Monthly transport: US$10–US$25

### Tax position

- **PIT 20% flat** if AM tax resident (183+ days)
- **HO-105-N IT Sector 1% turnover tax + 10% PIT for IT employees** (vs standard 20%) — material competitive advantage if eligible
- Foreign-employer remote work: technically subject to AM PIT once tax-resident; double-tax treaty network covers most Western source countries

### Verdict for digital-nomad-first buyers

🟢 **Strong fit** for budget-conscious DNs prioritising cheap fast internet + low CoL + 180-day visa-free + Caucasus-region access + IT-sector tax incentives. **Best fit**: IT-sector DNs (HO-105-N 1% turnover regime), Armenian-language/heritage DNs (citizenship by descent pathway), Caucasus-cycle nomads. **Friction**: no formal DN visa = either 180-day churn or formal residence; Russia-relocant cohort has saturated short-let market in Yerevan Kentron 2022–2024 (mild 2024–2026 reversal); geopolitical tail risk material.

---

## Section: `--macro`

### Headline 2024–2026

- **GDP growth 2022**: +12.6% (post-pandemic + Russian-relocant inflow shock)
- **GDP growth 2023**: +8.3% (ARMSTAT preliminary)
- **GDP growth 2024**: +5.9% (ARMSTAT preliminary)
- **GDP growth 2025**: +5.0–5.5% IMF Article IV / EBRD forecast range
- **GDP per capita 2024**: ~US$8,000 (World Bank)
- **Inflation 2025**: ~2.5–4.0% headline (CBA target 4%±1.5%)
- **Unemployment 2024 Q4**: ~12% (ARMSTAT) — moderate; informal-economy participation material
- **Public debt / GDP**: ~50% (Ministry of Finance) — moderate
- **CBA refinancing rate (2026-05-27 verified)**: **6.5%** (source cba.am Monetary Policy Decisions; cutting cycle from 2024 peak ~10%)

### Trend drivers (2024–2026)

- **Russian-relocant inflow 2022–2024** (~50,000+ Russian citizens to Yerevan; ~US$3–5B+ capital + IT-services contract migration) — material structural shock; partial reversal 2024–2026
- **CSTO suspension Feb 2024** — geopolitical realignment; EU-aligned reforms accelerating
- **2023 Karabakh displacement** (~120,000 displaced to Armenia) — humanitarian + housing-demand shock
- **CEPA implementation deepening** since March 2021
- **IT-sector growth** (HO-105-N regime through 2031) — material structural anchor; software services exports growing 15–25%/yr
- **Diaspora remittance economy**: ~10–14% of GDP (US, Russia, France, Argentina diaspora)

### IMF Article IV (latest)

[IMF 2024 Article IV](https://www.imf.org/en/Countries/ARM) flags: Russian-relocant-shock normalisation, EU-conditionality reform pace, Karabakh-displacement integration, geopolitical risks (Azerbaijan border, CSTO transition), banking-sector resilience post-Ameriabank/HSBC consolidation. Property-market: Yerevan 2021–2023 boom, 2024–2026 plateau / mild correction; structural HO-332-N tax-cost increase 2026 first-full-year.

---

## Section: `--demographics`

### Population structure (2024 ARMSTAT estimate)

- **Total**: ~2.78 million (vs ~3.55M peak ~1991 — material decline driven by emigration)
- **Median age 2024**: ~37.0 years (rising)
- **Age 0–14**: ~20%
- **Age 15–64**: ~67%
- **Age 65+**: ~13% (rising — projected ~20–22% by 2050 per ARMSTAT projections)
- **Total fertility rate 2024**: ~1.6 (ARMSTAT) — below replacement
- **Net migration**: persistently negative since 1991 except 2022–2023 (Russian-relocant + Karabakh-displaced inflow temporary reversal); structural negative trend resumes 2024–2026
- **Diaspora**: ~7M Armenians living abroad (Russia ~2M, US ~1M, France, Argentina, Lebanon, Iran, Georgia, Türkiye-historical) — **diaspora exceeds domestic population** materially; structural economic factor

### Geographic distribution

- Yerevan municipality: ~1.08M (39% of population) — single-city dominance
- Gyumri municipality: ~120k (4.3%)
- Vanadzor municipality: ~80k (2.9%)
- Other urban: ~600k (22%)
- Rural: ~900k (32%)

### Households

- ~775,000 domestic households (2024 ARMSTAT)
- Average household size: 3.6 persons (declining but among the highest in Europe)
- Owner-occupier rate: **~85–90%** (one of the highest in Europe — legacy of post-Soviet apartment privatisation 1991–1995)
- Renter market thin outside Yerevan + Gyumri; expanded materially in Yerevan 2022–2024 from Russian-relocant cohort

### Implication for property

- **Demand floor 2025–2030**: long-term emigration + ageing depress secondary-city demand; Yerevan relative resilience driven by capital-city function + diaspora-return + IT-sector clustering + post-2022 relocant inventory churn
- **Karabakh-displaced cohort 2023+** (~120k) added housing demand shock — partially absorbed via state housing programmes + own purchases
- **Supply pipeline**: Yerevan new-build pipeline strong 2022–2026 in Kentron + Davtashen + Achapnyak + Northern Avenue extensions; pre-1988 panelka stock dominant resale segment (Spitak-era retrofit-debt overhang)
- **Discount opportunity**: Gyumri + Vanadzor + marz centres priced at 40–70% discount to Yerevan; rural village houses widely available <US$30k but with severe utility + amenity + seismic-retrofit constraints

---

## Section: `--esg`

### Climate-transition exposure

- **Updated NDC under Paris Agreement** (latest submission 2021; verify current at mnp.am): 40% reduction in net GHG by 2030 vs 1990 base — policy frameworks aligning with EU CEPA direction
- **Buildings sector**: ~30% of national CO₂; primary lever is heating-fuel switch + insulation retrofit
- **Energy-efficiency requirements** emerging via EPBD-aligned legislation (CEPA implementation); enforcement uneven on resale — request EPC and verify when applicable

### Property-level ESG considerations

- **Pre-1988 panelka stock**: typically EPC-equivalent class **E–G**; major retrofit opportunity (insulation, window replacement, individual gas boiler, heating-system modernisation) — US$50–US$150/m² typical retrofit budget for thermal-envelope upgrade
- **Tuff-stone Yerevan stalinka stock**: thicker walls + better thermal mass than panelka; lower retrofit-debt
- **Gas-boiler retrofit dominance**: ~80% of Yerevan apartments now individual gas boilers post-2000s phase-out of Soviet district heating; tariff exposure to Gazprom Armenia bilateral pricing
- **Renewable energy + Metsamor NPP**: ~30% nuclear (Metsamor), ~10% hydro, ~5% solar — material low-carbon baseline; Metsamor reactor-life-extension (under IAEA review) determines 2030+ baseload
- **Solar PV growth**: residential rooftop solar accelerating 2022–2026 (PSRC net-metering scheme); typical 5 kW system US$4,000–US$8,000 installed

### Climate-physical risk (cross-section to `--climate` + `--risks`)

- Drought stress in Ararat Plain + Vayots Dzor + Syunik (viticulture, apricot, pomegranate)
- Lesser Caucasus seismic exposure for Yerevan + Gyumri pre-1988 panelka (dominant ESG-physical risk)
- Hrazdan + Aras + Debed flood exposure for low-elevation parcels
- Hotter Yerevan summers → cooling-load growth in stock built without AC provision

### Social / governance factors

- Owner-association governance under Law on Apartment Buildings — minority-protection mechanisms via court; HOA collective-action problem material in panelka stock
- Anti-corruption: post-2018 Velvet Revolution anti-corruption reforms materially strengthened cadastre + notary chain transparency; Cadastre Committee + e-cadastre.am considered substantially clean
- **2018 Velvet Revolution** + subsequent reforms underpin governance improvements; CEPA implementation drives further EU-aligned reforms

### Verdict (ESG lens for typical Yerevan apt)

🟡 **Watch** — pre-1988 panelka stock represents the dominant retrofit-debt + seismic-resilience exposure (Spitak baseline); new-build (post-2010) materially better but priced higher; gas-boiler dominance creates Gazprom-Armenia tariff-volatility exposure; CEPA-driven EPBD enforcement will tighten 2026–2030; geopolitical loading material.

---

## Section: `--exit`

### Resale market liquidity

- **Average days on market 2024**: ~45–120 days Yerevan mid-tier; 90–240 days Gyumri / Vanadzor; rural village houses can sit 1–3+ years
- **Cyclical sensitivity**: Armenian secondary market is **moderately liquid in Yerevan**, **thin elsewhere** — annual transactions nationally ~30–45k (Cadastre Committee) vs ~1.5M registered immovables; turnover ratio ~2–3%/yr
- **2021–2023 Russian-relocant boom**: drove ~50% peak nominal Yerevan appreciation; transactions volumes peaked 2022–2023
- **2024–2026 plateau / mild correction**: Russian-relocant outflow + supply-pipeline absorption + HO-332-N RE-tax 2026 first-full-year cost increase combined effect

### Exit-cost stack (seller side)

| Item | Cost |
|---|---|
| Estate agent commission | typically **2–4%** of sale price (often paid by seller; sometimes split) |
| Notary fee (seller side typically) | AMD 50,000–150,000 (~US$130–US$390 fixed; sliding for high-value) |
| **Individual-to-individual residential sale: PIT EXEMPT** (Tax Code Art. 147(1)(16); 2026-05-27 verified, source PwC + armenian-lawyer.com) — no holding-period test |
| **Sale to legal entity / sole-proprietor (tax agent)**: 10% withholding on transaction price (residential); 20% (commercial) |
| Mortgage early-discharge fee | typically 1–3% of outstanding balance, capped per loan agreement |
| Total exit cost | **typically 2–5% of sale price** for individual-to-individual residential resale; 12–22% effective stack when sale is to a legal entity (10% WHT on price + agent + notary) |

### Liquidity by sub-segment (qualitative, 2026)

| Segment | Liquidity | Notes |
|---|---|---|
| Yerevan Kentron new-build (US$2,200–US$3,500/m²) | 🟡 selective | Diaspora-return + IT-relocant + Russian-relocant exit + premium pool; 60–120 days typical |
| Yerevan Arabkir/Davtashen mid-tier | 🟢 strong | Largest stock, perpetual buyer pool incl. local upgraders; 30–90 days typical |
| Yerevan Erebuni/Malatia outer + panelka | 🟡 watch | Thin retrofit-debt; pre-1988 stock uneven; HO-332-N RE-tax progressive impact varies by cadastral value |
| Yerevan Old Quarter / Kond heritage | 🟠 thin | Renovation restrictions + small buyer pool |
| Gyumri + Vanadzor mid-tier | 🟡 selective | Population decline; 90–240 days |
| Tavush / Syunik / Vayots Dzor border-zone | 🟠 niche | Geopolitical risk premium; thin buyer pool |
| Rural village houses | 🟠 niche | Diaspora-buy / hobby-property only; 1–3+ yr typical |
| Pre-1988 panelka without retrofit | 🟡 watch | Spitak-era seismic + retrofit-debt depressing pricing trajectory |

### Verdict for exit risk

🟡 for Yerevan mid-tier; 🟢 for in-demand Arabkir/Davtashen commuter stock; 🟠 for rural + secondary-city + heritage + border-zone. **2022–2023 Russian-relocant buyers**: appreciation realised but exit liquidity cools 2024–2026 as cohort partial reversal proceeds. **HO-332-N 2026 first-full-year RE-tax increase** is the key carrying-cost variable; net-yield compression may motivate partial sell-down by yield-focused investors. **Geopolitical tailwind/headwind**: CSTO-suspension realignment + EU candidacy discussion 2024–2026 could materially reprice over multi-year horizon — both directions plausible.

---

## Cost benchmarks (AM 2025–2026)

| Item | Cost (US$ or AMD, est.) |
|---|---:|
| Cadastre extract (`Vkayakan` standard) | ~US$26–US$40 (AMD 10,000–15,000) |
| Cadastre extract (urgent) | ~US$40–US$80 |
| Notary fee (residential resale, fixed/sliding) | ~AMD 50,000–150,000 (~US$130–US$390) |
| State duty (cadastre registration) | 0.05% of value |
| Real-estate agent (paid by seller normally) | 2–4% |
| Translator (deed signing, foreign buyer) | US$80–US$300 |
| Building inspector (independent structural survey) | US$200–US$700 |
| Asbestos test (single sample) | US$40–US$100 |
| Radon test (3-month kit) | US$50–US$150 |
| Bare-shell ("karkas") → finished apartment fit-out | US$200–US$400 / m² |
| Roof replacement (terracotta, 200 m²) | US$6,000–US$16,000 |
| Full apartment renovation (Yerevan mid-range, 80 m²) | US$15,000–US$35,000 |
| Septic to mains connection | US$1,500–US$5,000 |
| Annual property tax (Yerevan Kentron, market US$200k flat, 2026 phased-in) | ~US$300–US$500 |
| Annual property tax (Yerevan Kentron, market US$600k flat, 2026 phased-in) | ~US$3,500–US$4,000 |
| **Total transaction cost (buyer side, residential resale)** | **~0.1–0.5% of price** — among the lowest globally |

## Active fiscal incentives (2025–2026)

- **HO-105-N IT Sector** — 1% turnover tax in lieu of CIT + VAT for qualifying IT residents; 10% PIT (vs standard 20%) for IT employees; **extended to 31 December 2031**
- **Individual-to-individual residential sale: PIT EXEMPT under Art. 147(1)(16)** regardless of holding period (2026-05-27 verified, source PwC + armenian-lawyer.com) — among the most generous CGT-free regimes globally
- **VAT residential first-sale exemption** by VAT-registered developer (Tax Code Art. 64.2.1)
- **Free Economic Zones** (Meridian, Alliance, Meghri, ECOS) — exemption from CIT, VAT, customs duty for in-zone activity
- **Investor Residence (AMD 50M / ~US$130k property purchase)** — 5-yr renewable residence permit
- **Special Residence (10-year) for ethnic Armenians** — automatic for Diaspora applicants
- **Citizenship by descent** for Armenian-heritage applicants — no minimum residence required

## Common listing platforms

- **List.am**: `https://www.list.am/en/category/60` *(per listing — verify with cadastre / on visit)*
- **MyRealty.am**: `https://www.myrealty.am/` *(per listing — verify with cadastre / on visit)*
- **Estate.am**: `https://www.estate.am/` *(per listing — verify with cadastre / on visit)*
- **Realt.am**: `https://www.realt.am/` *(per listing — verify with cadastre / on visit)*
- **Yerevan.estate / Property.am** *(per listing — verify with cadastre / on visit)*
- Facebook groups + Telegram channels (high volume; never authoritative)

## Caveats unique to AM

- **Foreigners CAN buy residential freehold without restriction** (Civil Code Art. 184 + Law on Real Property of 1999) — among the most permissive globally
- **Foreigners CANNOT own agricultural land** (Land Code Art. 4) — only Armenian citizens, Armenian legal entities, State, communities; LLC workaround common but title contestable
- **Transaction costs ~0.1–0.5%** — among the world's lowest (state duty 0.05% + nominal notary fee + cadastre fee)
- **HO-332-N Real Estate Tax 2026 first-full-year effect**: annual property tax materially higher than 2024–2025 baseline; verify per Cadastre Committee extract before underwriting
- **Individual-to-individual residential sale fully PIT-exempt under Art. 147(1)(16)** — no holding-period test (2026-05-27 verified, source PwC + armenian-lawyer.com); 10% WHT on price applies only when buyer is a legal entity / sole-proprietor acting as tax agent
- **20% flat PIT** since 2023 (vs prior progressive system)
- **HO-105-N IT Sector 1% turnover regime through 2031** — uniquely competitive in region for IT-relocant buyers
- **Cadastre Committee + e-cadastre.am**: post-2018 e-services overhaul; bilingual Armenian + English; substantially clean post-2018 reforms
- **Notarised contract MANDATORY** (Civil Code Art. 295) — no DIY conveyancing
- **AML cash limit AMD 500,000** per transaction (HO-80-N 2008); bank-wire standard above
- **Spitak 1988 baseline + pre-1988 panelka**: dominant residual seismic risk; commission independent structural survey for any pre-1988 multi-storey
- **Yerevan-Gyumri-Vanadzor seismic microzoning** — request from NSSP for parcel-level applicability
- **Geopolitical tail risk**: 2020 + 2023 Karabakh + ongoing Azerbaijan border (Tavush, Syunik, Vayots Dzor); CSTO frozen Feb 2024; EU candidacy discussion 2024–2026 — material multi-year repricing variable in both directions
- **Russian-relocant 2022–2024 wave**: drove ~50% peak nominal Yerevan price appreciation 2021–2023; partial reversal 2024–2026 — supply overhang material in some sub-segments
- **180-day visa-free** for ~92 nationalities — most permissive after Georgia (365)
- **Investor Residence at AMD 50M (~US$130k) property** — 5-yr renewable; among the lowest property-investor thresholds globally
- **Diaspora-citizenship pathway** (Law on Citizenship Art. 13): Armenian-heritage applicants direct citizenship route; no minimum residence
- **Dual citizenship allowed since 2007** — material for diaspora returnees + foreign retirees
- **Currency**: most listings priced in **US$** but contracts denominated in **AMD** at CBA reference rate on signing day — exchange-rate exposure 2–3 weeks pre-signing; AMD has experienced > 20% one-year moves (2014, 2022)
- **No active CBI** — citizenship via 3-yr naturalisation OR descent
- **Russia-passport buyer scrutiny** elevated 2022–2026 under EU + US secondary-sanctions concern; banks selective
- **HSBC Armenia exit 2024–2026** — reduces foreign-bank options; Bank of Georgia partial Ameriabank ownership 2023–2024 increased Caucasus integration

## Reddit / forum sources

- **r/armenia** — general (mixed quality on property; English + Armenian)
- **r/Yerevan** — city-specific, active English/Armenian/Russian
- **r/ArmenianITSector** — IT/HO-105-N discussion, includes remote-worker housing
- Facebook: "Yerevan Apartments", "Real Estate Armenia", "Expats in Yerevan", "Armenia Property"
- Telegram: `t.me/yerevanrealestate` (high volume; classifieds; never authoritative); diaspora-return groups
- Diaspora forums: "Russia-Armenian community Yerevan", "Hai Diaspora", AGBU + Hamazkayin local chapters — material because diaspora-buy is a non-trivial segment
- Estate.am blog + List.am analytics — local market commentary

## Verification authorities

| Authority | When to call / visit |
|---|---|
| **Cadastre Committee** | Title extract (`Vkayakan`), encumbrances, cadastral verification — any Cadastre Committee territorial office or e-cadastre.am |
| **e-cadastre.am self-service** | Online cadastral viewer + extract ordering |
| **e-register.am unified portal** | Entity + cadastre cross-check |
| **SRC (State Revenue Committee)** | Tax residency, contract registration, VAT registration, IE registration, HO-105-N IT-sector status |
| **Migration Service of MoIA** | Residence permit, investor visa Law on Foreigners Art. 18.4 + 21 |
| **CBA (Central Bank of Armenia)** | Reference exchange rate, bank supervisory list, insurance supervisory list |
| **Notarial Chamber** | Notary register, complaints, tariff |
| **Ministry of Education, Science, Culture and Sports** | Heritage-listed building check |
| **Yerevan Municipality** + community administration | Local property-tax rates, zoning, building permits |
| **Veolia Jur** | Mains water + sewer connection verification |
| **ENA (Electric Networks Armenia)** | Electricity connection + tariff |
| **Gazprom Armenia** | Gas connection + tariff |
| **Hydromet Service** | Flood + climate baseline data |
| **NSSP (National Survey for Seismic Protection)** | Seismic microzoning + parcel-level applicability |
| **Geological Survey** | Landslide + geological hazard data |
| **Ministry of Internal Affairs — Rescue Service** | Emergency response, hazard maps |
| **Police of Armenia** | Crime statistics, parcel-level precinct summary |

## Quirks to know

- **Cadastral code format `XX-XXX-XXXX-XXXX`** (region.community.block.parcel) — every property has one; ask for it before any other paperwork
- **Armenian + Russian + English bilingual context**: Russian still widely used in business + older notaries; verify deed language preference; certified translation cheap and standard
- **"Tuff-stone" Yerevan**: distinctive volcanic-rock cladding (pink/grey/black tuff) characteristic of Yerevan stalinka + post-Soviet stock; thermal-mass benefit + heritage character; tuff-cladding restoration cost premium for heritage listings
- **Heat-network "jermut'yun" residual**: thin remnant in some Soviet-era Yerevan blocks; individual gas boilers ("inknavar") dominant
- **Spitak earthquake 1988 baseline**: dominant residual seismic risk anchor; pre-1988 panelka stock requires structural survey
- **HO-332-N RE-tax progressive scale**: bracket sensitivity at boundaries (AMD 10M, 25M, 47M, 120M, 200M for apartments; separate 7M/23M/50M/85M/200M for houses per Tax Code Art. 230); 2026 first-full-year cost increase
- **Diaspora buyer pattern**: many Yerevan apartments held by emigrant owners (Russia, US, France, Argentina) and managed by local relatives — verify owner is signing personally OR via apostilled PoA
- **Russian-relocant 2022–2024 cohort**: drove price appreciation; partial 2024–2026 reversal; supply overhang in Yerevan Kentron premium segment
- **CSTO suspension Feb 2024**: geopolitical realignment ongoing; EU candidacy discussion 2024–2026
- **Karabakh displacement Sept 2023**: ~120k humanitarian inflow; integrated via state housing programmes + own purchases
- **Sanction-watch on Russian banks** (VTB Armenia, RESO insurance, Rosgosstrakh): verify status before engaging
- **Armenia–Türkiye border closed since 1993**: limits direct land-route to W. Europe; Georgia + Iran are the operational land borders

## Source URL templates

| Source | URL pattern |
|---|---|
| Cadastre Committee | `https://www.cadastre.am/` |
| e-cadastre online | `https://e-cadastre.am/` |
| e-register unified | `https://www.e-register.am/` |
| SRC State Revenue | `https://www.src.am/` |
| Migration Service MoIA | `https://www.mfa.am/en/visa/` (and immigration sub-pages) |
| CBA Central Bank | `https://www.cba.am/` |
| CBA exchange rates | `https://www.cba.am/en/SitePages/Default.aspx` |
| ARMSTAT Statistics | `https://armstat.am/en/` |
| Notarial Chamber | (verify current at justice.am) |
| PSRC Energy Regulator | `https://www.psrc.am/` |
| Veolia Jur | `https://www.veolia.am/en` |
| ENA Electric | `https://www.ena.am/` |
| Gazprom Armenia | `https://armenia-am.gazprom.com/` |
| Tourism / Investment | `https://invest.am/` |
| HighTech Park / IT Sector | (verify current at gov.am) |
| List.am classifieds | `https://www.list.am/en/category/60` |
| MyRealty.am | `https://www.myrealty.am/` |
| Estate.am | `https://www.estate.am/` |
| MTAI / State Roads | `https://www.mtad.am/en/` |
| Hydromet Service | `https://www.armmonitoring.am/` |
| Ministry of Internal Affairs — Rescue Service | `https://mia.gov.am` |
| Seismic protection (via Ministry of Internal Affairs) | `https://mia.gov.am` |
| Ministry of Environment | `https://environment.gov.am/en/` |
| Police statistics | `https://www.police.am/` |
| Yerevan Municipality | `https://www.yerevan.am/` |
| Government portal | `https://www.gov.am/` |
| National Assembly | `https://www.parliament.am/` |
| MFA visa info | `https://www.mfa.am/en/visa/` |

## Status

**Confidence**: MEDIUM — HIGH on foundational legal/fiscal framework (Tax Code Art. 147(1)(16) individual-to-individual residential PIT-exemption; 10% WHT on price when buyer is legal entity / sole-proprietor tax agent (residential), 20% commercial; Tax Code Art. 230 property-tax brackets — separate schedules for apartments vs houses; CBA refinancing rate 6.5% (2026-05-27, source cba.am) following cutting cycle from 2024 ~10% peak; AMD ~368/USD ~395-410/EUR May 2026 per CBA reference rate). MEDIUM on parcel-level cadastre exact apartment vs house classification (verify at src.am for any specific deal), 2026 CBA forward-rate path, and recharacterisation risk for business-pattern traders (individual sales with high frequency may be re-classified as entrepreneurial income). LOW on residential listing benchmarks (no national HPI; List.am + Spyur aggregator-grade with broker bias).

**Last verified**: 2026-05-27 (real-estate-tax reform law corrected 2026-09-18 — HO-332-N of 25 June 2020, not HO-185-N of 25 December 2020, per ARLIS; risks-authority rows (MIA Rescue Service) and Veolia Jur operator identity corrected 2026-09-18 per mia.gov.am + veolia.am). Cross-references corrected 2026-09-24 from the GE-537 tracker entry (November regwatch wave, run early).

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Primary sources verified — Civil Code Art. 184 + Art. 295 (residential foreign ownership open, mandatory notary), Land Code Art. 4 (foreign ag-land ban), Law on Real Property of 1999 + Law on State Registration HO-295-N (1999 Cadastre framework), Tax Code Art. 64 + 147 + 150 + 158 + Section 13 Articles 224–238 + Law HO-332-N of 25 June 2020 (Real Estate Tax progressive scale phased through 2026 to 100% coefficient), Law on Foreigners Art. 18.4 (Investor Residence AMD 50M ~US$130k) + Art. 21 (Special Residence 10-year for ethnic Armenians), Law on Citizenship Art. 13 (descent + 3-yr naturalisation; dual citizenship since 2007), Law HO-105-N "On State Support to IT Sector" (1% turnover regime extended to 31 December 2031), Law HO-80-N 2008 on AML (cash limit AMD 500,000), CEPA in force 1 March 2021, CSTO frozen February 2024, Spitak 1988 Mw 6.8 baseline + SNiP RA II-2.02-94 (1994) + 2020 update seismic code, NSSP microzoning Yerevan + Gyumri + Vanadzor. **Geopolitical context (2020 + 2023 Karabakh, ~120k displaced Sept 2023, Azerbaijan border tension Tavush/Syunik/Vayots Dzor, CSTO suspension Feb 2024, EU candidacy under discussion 2024–2026)** integrated as material risk + repricing variable; written non-partisan, factual. **Russian-relocant 2022–2024 wave** documented as drove ~50% peak nominal Yerevan appreciation 2021–2023 with 2024–2026 partial reversal. **HO-332-N first-full-year 2026 RE-tax effect** flagged repeatedly as dominant 2026 carrying-cost variable. **Re-verify each annual budget law amendment** for Tax Code (especially Art. 230 RE-tax brackets), CBA refinancing rate decisions, PSRC tariff schedules, Cadastre Committee tariffs, HO-105-N IT-sector eligibility scope. **Watch list 2026**: HO-332-N implementation actuals vs forecast tax bills, EU candidacy formalisation milestones (if any), Azerbaijan border status, CSTO formal exit progression, Russian-relocant cohort net-flow direction, HSBC Armenia exit completion + bank-sector consolidation. **Transnistria-equivalent zone**: none — Karabakh fully under Azerbaijani control post-Sept 2023 (out of Armenian cadastral scope by international consensus).

## Extension TODOs (deepen on first real run)

- [ ] Per-Yerevan-district HO-332-N cadastral-value calibration database (90% baseline currently inferred from Cadastre Committee methodology guidance; verify per-segment empirical samples)
- [ ] HO-332-N 2026 first-full-year actual tax-bill audit (collect Q1 2026 owner sample for calibration)
- [ ] HO-105-N IT-sector eligibility checklist for foreign IE-registered solo founders (2031 sunset risk planning)
- [ ] NSSP seismic-microzoning parcel-level certification request walkthrough for Yerevan + Gyumri + Vanadzor
- [ ] Diaspora-buyer due diligence checklist (apostilled PoA + Russia/US/France/Argentina source-of-funds patterns)
- [ ] Russian-relocant cohort exit-flow tracker (List.am turnover signals; Russian-language listing share)
- [ ] Karabakh-displaced housing-programme intersection with private market pricing (state housing scheme + private absorption)
- [ ] CBA mortgage rate + LTV time-series automation
- [ ] Heritage-listed building cadastral-code lookup workflow (Yerevan Kond + Old Quarter, Gyumri historic centre)
- [ ] Free Economic Zone tax-incentive eligibility checklist (Meridian, Alliance, Meghri, ECOS)
- [ ] Border-zone (Tavush, Syunik, Vayots Dzor) political-risk-premium pricing differential measurement
- [ ] Sanction-watch banking + insurance carrier matrix (VTB Armenia, RESO, Rosgosstrakh — operational status)
