# 香港 / Hong Kong SAR 🇭🇰 — Property Due-Diligence Playbook

ISO2: `hk`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode**: **none** — Hong Kong has no postal code system. Address structure is District → Street → Building/Estate name → Floor/Flat (e.g., `Flat 12B, 25/F, Tower 3, Kornhill, 1 Hong Yue Street, Quarry Bay, Hong Kong`)
- **Population**: 7,510,800 (end-2025 provisional, [Census & Statistics Department](https://www.info.gov.hk/gia/general/202602/12/P2026021200283.htm)); +0.1% YoY; natural decrease of ~18,900 (births 31,100, deaths 50,000) offset by inbound talent migration
- **GDP per capita**: ≈ USD 46,583 (2025 constant 2015 prices, IMF/HKTDC); among world's top 25 by PPP
- **Currency**: **HKD (HK$)** — pegged USD via Linked Exchange Rate System since 17 Oct 1983; HKMA Convertibility Undertaking band **7.75–7.85 HKD/USD** ([HKMA LERS](https://www.hkma.gov.hk/eng/key-functions/money/linked-exchange-rate-system/))
- **Languages**: Chinese (Cantonese de facto spoken; Traditional 繁體 written) + English, both official under Basic Law Article 9. Government bilingual; conveyancing instruments dual-language
- **Admin levels**: 1 SAR → **3 areas** (Hong Kong Island / Kowloon / New Territories) → **18 districts** (4 HK Island, 5 Kowloon, 9 NT) administered by [Home Affairs Department](https://www.had.gov.hk/en/18_districts/my_map.htm) + District Councils
- **Cadastre**: **The Land Registry (土地註冊處)** under [Department of Justice](https://www.landreg.gov.hk/) operates the **Integrated Registration Information System (IRIS)** — title-by-deeds register (NOT Torrens; bills for Land Titles Ordinance Cap. 585 conversion paused since enactment 2004)
  - Online: `https://www.iris.gov.hk/` — fee HK$10 per Current Land Register search; HK$25 per full historical search ([IRIS fees](https://www2.iris.gov.hk/eservices/help/topic16.jsp))
  - **Lands Department (地政總署)**: `https://www.landsd.gov.hk/` — handles Crown leases, government rent, land disposal, lease modification (cadastral mapping function)
- **Identifier**: Lot number under **Demarcation District (DD)** for NT (e.g., `DD 6 Lot 123 in Sha Tin`) or **Inland Lot / Section / Subsection** for HK Island/Kowloon; modern subdivisions use **Subsection / Subsubsection** notation. Building-level: deed of mutual covenant (DMC) defines undivided shares
- **Title concept**: All land in Hong Kong is technically **leasehold from the Government** (legacy of Crown Lease) — there is NO freehold in HK except St John's Cathedral on Garden Road (granted in fee simple 1847)
  - Most pre-1997 leases were 50 / 75 / 99 / 999 years; after 1985 Sino-British Joint Declaration, new grants and renewals capped at 30 June 2047
  - **Resolved 2024**: [Extension of Government Leases Bill](https://www.devb.gov.hk/en/legco_matters/replies_to_legco_questions/index_id_9304.html) enacted; eligible commercial / residential / industrial leases auto-extend **50 years from 30 June 2047** without new premium (annual government rent at 3% rateable value continues post-renewal)
- **Foreign-buyer rule**: **NO restriction** on foreigners buying residential property; **NO BSD/SSD/NRSD since 28 Feb 2024** ([Government press release](https://www.info.gov.hk/gia/general/202402/28/P2024022800551.htm)); only Ad Valorem Duty Scale 2 applies. NT village houses (丁屋) under Small House Policy carry restrictions for indigenous male villagers only
- **Visa**: Top Talent Pass Scheme (TTPS) / Quality Migrant Admission Scheme (QMAS) / Immigration Arrangements for Non-local Graduates (IANG) / **New Capital Investment Entrant Scheme (CIES)** reactivated 1 Mar 2024 — HK$30M+ in permissible assets (residential property up to HK$10M counts as ancillary, NOT primary investment) ([New CIES Scheme Rules](https://www.newcies.gov.hk/media/jvkfl4uq/scheme-rule-en.pdf))
- **Recent reforms (2024–2026 watershed)**:
  - **28 Feb 2024**: BSD (Buyer's Stamp Duty 15%), SSD (Special Stamp Duty up to 20%), NRSD (New Residential Stamp Duty 7.5%) **all abolished**; mortgage stress test suspended ([HKMA 2024-02-28 circular](https://brdr.hkma.gov.hk/chi/doc-ldg/docId/getPdf/20240228-3-EN/20240228-3-EN.pdf))
  - **1 Mar 2024**: New CIES launched
  - **23 Mar 2024**: Safeguarding National Security Ordinance (Article 23 / SNSO) effective ([news.gov.hk 2024-03-19](https://www.news.gov.hk/eng/2024/03/20240319/20240319_191521_516.html)) — material to foreign-capital sentiment / cross-border data; not directly to property law
  - **16 Oct 2024**: HKMA unified the maximum LTV for all residential properties at a flat 70% regardless of value (the earlier tiered schedule no longer applies — see `--finance`) ([HKMA 2024-10-16](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2024/10/20241016-4/))
  - **2024 Extension of Government Leases Bill** — settled the 2047 question for the vast majority of land (auto 50-yr extension, no premium)

## Section: `--price`

### Primary sources

- **Rating and Valuation Department (差餉物業估價署 — RVD)**: `https://www.rvd.gov.hk/en/publications/property_market_statistics.html` — official **Hong Kong Property Price Index (HKPPI)** + **Hong Kong Property Rental Index** monthly + Hong Kong Property Review annual
  - 2026 release: [Hong Kong Property Review 2026 preliminary findings](https://www.rvd.gov.hk/doc/en/HKPR2026_Preliminary_Findings_Eng.pdf)
- **Centaline Property Centa-City Index (CCI)**: `https://hk.centanet.com/findproperty/en/centadata` — secondary-market private residential weekly index based on formal Sale & Purchase Agreement dates; Hong Kong's most-watched real-time price gauge (private sector but quoted by HKMA + government)
- **The Land Registry IRIS**: `https://www.iris.gov.hk/` — actual recorded transactions (Memorial of Assignment); each transaction filed with consideration; HK$10 per current title search
- **Census and Statistics Department (政府統計處)**: `https://www.censtatd.gov.hk/` — quarterly housing affordability series, rental + price-to-income series

### Listing platforms

- **Centaline / Centanet**: `https://hk.centanet.com/home/index.aspx` — largest agency by transaction count; agent-listed inventory + sold-price history
- **Midland Realty / Midland.com.hk**: `https://www.midland.com.hk/` — second largest agency
- **Squarefoot.com.hk** (Ricacorp): `https://www.squarefoot.com.hk/`
- **28Hse.com**: `https://www.28hse.com/` — buyer-direct + agency mixed
- **Spacious.hk**: `https://www.spacious.hk/` — English-language, expat-oriented
- **OKAY.com**: `https://www.okay.com/` — English, prime / mid-luxe
- **GoHome.com.hk** + **Property.hk**: aggregators

### Premium-area benchmarks (Q1–Q2 2026 reference, RVD HKPPI + Centa-City Index aggregates)

| Area | Type | HKD/sq ft (saleable) | est. EUR/m² |
|---|---|---:|---:|
| **The Peak** (Hong Kong Island) | luxury house / low-rise apt | 35,000–80,000+ | ≈ 41,000–94,000 |
| **Mid-Levels Central / Repulse Bay** | mid-to-high apt | 22,000–40,000 | ≈ 26,000–47,000 |
| **Central / Sheung Wan / Wan Chai** | apt | 18,000–30,000 | ≈ 21,000–35,000 |
| **Quarry Bay / North Point / Tai Koo** | apt | 14,000–22,000 | ≈ 16,000–26,000 |
| **Tsim Sha Tsui / Yau Ma Tei (Kowloon)** | apt | 14,000–24,000 | ≈ 16,000–28,000 |
| **Kowloon Tong / Ho Man Tin** | apt / townhouse | 18,000–32,000 | ≈ 21,000–37,000 |
| **Sha Tin / Tai Po / Ma On Shan (NT)** | apt | 10,000–16,000 | ≈ 12,000–19,000 |
| **Tuen Mun / Yuen Long / Tin Shui Wai (NT)** | apt | 8,000–13,000 | ≈ 9,400–15,000 |
| **NT village house (丁屋)** | 700 sqft 3-storey | HK$5–12M total typical | ≈ €590k–1.4M |

⚠️ Hong Kong quotes **saleable area (實用面積)** post-2013 mandatory disclosure under [Residential Properties (First-hand Sales) Ordinance Cap. 621](https://www.elegislation.gov.hk/hk/cap621). Pre-2013 listings often quoted **gross area (建築面積)** which includes ~20–30% common areas — direct €/m² conversion misleading on legacy stock. Always confirm 實用面積.

### Compute

1. **HKD/sq ft (saleable)** = listing price ÷ saleable area in sq ft
2. **EUR/m²** ≈ HKD/sq ft × 10.764 ÷ ~8.5 (HKD/EUR Q1 2026 indicative; HKD pegged USD so EUR rate moves with USD/EUR)
3. Compare to Centa-City Index (weekly) for the building's sub-index (CCL Mass / CCL Large unit)
4. Compare to last 6–12 months IRIS recorded transactions same building (search by lot number)
5. Compare to RVD HKPPI for the area (Class A–E by saleable area — A ≤ 40m², B 40–69.9m², C 70–99.9m², D 100–159.9m², E ≥ 160m²)
6. **Trap**: gross-area listings inflate area by 15–30% vs saleable; **Trap**: "efficiency ratio" of older buildings 70–80%, newer towers 75–85%
7. **Trap**: club-house, balcony, A/C platform, bay window historically counted into gross area but NOT saleable
8. **Trap**: free-of-management-fee period vs ongoing management fee + sinking fund — not in listing price

### Trend Q1 2022 → Q1 2026

- **Sustained decline**: HKPPI fell continuously **Feb 2022 → Aug 2025** (-~28% peak-to-trough cumulative; [BIS residential property price statistics Q2 2025](https://www.bis.org/statistics/pp_residential_2511.htm)); -8% YoY in real terms Q2 2025
- **Stabilizing late 2025 → 2026**: Oct 2025 HKPPI **+1.13% YoY** — second consecutive month of YoY increase after 42-month decline (RVD via [news.gov.hk archive](https://www.rvd.gov.hk/en/press_releases/press_release_318.html))
- **Drivers**: stamp-duty abolition Feb 2024 + LTV easing Oct 2024 + TTPS/CIES inbound migration + US Fed rate cut cycle (HKD interest rates track USD via peg)
- **Q1–Oct 2025 transaction volume**: 51,361 units (+20.3% YoY), HK$416.94B aggregate (+14.4% YoY) — momentum in volume preceded price recovery

---

## Section: `--traffic`

### Primary source

- **Transport Department (運輸署) — Annual Traffic Census**: `https://www.td.gov.hk/en/publications_and_press_releases/publications/free_publications/atci1/index.html` — annual traffic flow at ~1,300 count points across HK road network; volumes in PCU (Passenger Car Unit) and AADT-equivalent
- **HKeMobility / OpenAPI Traffic**: `https://www.hkemobility.gov.hk/` — real-time traffic + speed
- **Highways Department (路政署)**: `https://www.hyd.gov.hk/` — road classification + traffic studies

### Key term

**AADT (年平均日交通量)** — annual average daily traffic, measured at observation points by Transport Department.

### Verdict bands

- 🟢 < 5,000 v/d (residential street, NT village access)
- 🟡 5,000–25,000 v/d (district road, secondary corridor)
- 🟠 25,000–80,000 v/d (primary district artery, e.g., King's Road, Nathan Road)
- 🔴 > 80,000 v/d (Cross-Harbour Tunnel approaches, Tolo Highway, Tuen Mun Road, Eastern Corridor — saturation often >150,000)

### Coarse fallback (OSM `highway`)

- motorway = expressway / strategic route (e.g., Route 8, Route 9)
- trunk = principal distributor (e.g., Tolo Highway sections)
- primary = district distributor
- secondary = local distributor
- residential = local access road
- service = back-of-house / interior estate access

⚠️ Cross-check elevated structure noise — Hong Kong's flyover network (e.g., Eastern Corridor, West Kowloon Highway) creates **noise contour zones**; HKEPD publishes **Strategic Noise Maps** at `https://www.epd.gov.hk/epd/english/environmentinhk/noise/noise_maincontent.html` — request for any property within 100m of an elevated road or rail.

---

## Section: `--tax`

### Annual property charges — Rates + Government Rent

**Hong Kong has NO recurring "property tax" in the European sense; instead:**

| Charge | Rate | Base | Statute |
|---|---|---|---|
| **Rates (差餉)** | **5%** of rateable value (domestic ≤ HK$550,000 RV; progressive scale above — see below) | RV = annual rental value if let on open market on 1 Oct designated date | [Rating Ordinance Cap. 116](https://www.rvd.gov.hk/en/our_services/rates.html) |
| **Government Rent (地租)** | **3%** of rateable value | RV (same base) | [Government Rent (Assessment & Collection) Ordinance Cap. 515](https://www.rvd.gov.hk/en/our_services/government_rent.html) |
| **Property Tax (物業稅)** | **15%** flat × (rental income − 20% standard deduction) | Actual rental income | [Inland Revenue Ordinance Cap. 112](https://www.ird.gov.hk/eng/tax/ind_ppt.htm) — applies only if property is let; not for owner-occupied |

⚠️ **Government Rent applies to leases granted/extended after 27 May 1985** (per Joint Declaration) — most NT land + post-1985 HK Island/Kowloon grants. Some pre-1985 HK Island leases carry only nominal annual rent (HK$1,000 or under) and may be exempt — confirm via [Lands Department lease search](https://www.landsd.gov.hk/en/gov_rent/index.htm).

### Progressive Rates (domestic tenements, 2024-25 onwards per [RVD progressive rating system](https://www.rvd.gov.hk/en/progressive_rating_system.html))

| Rateable value band | Rates % |
|---|---:|
| ≤ HK$550,000 | 5% |
| HK$550,001 – HK$800,000 | 8% (on slice above 550k) |
| > HK$800,000 | 12% (on slice above 800k) |

Non-domestic tenements: flat 5% (no progression).

### Transaction taxes (one-time, post-28 Feb 2024 abolition)

**Only Ad Valorem Stamp Duty (AVD) at Scale 2 applies** ([IRD AVD FAQ](https://www.ird.gov.hk/eng/faq/avd.htm)):

| Consideration band | Scale 2 rate |
|---|---:|
| ≤ HK$3,000,000 | HK$100 (flat) → 1.5% (sliding by formula) |
| HK$3M – HK$3.528M | HK$100 + 10% × excess over HK$3M |
| > HK$3.528M – HK$4.5M | 1.5% |
| > HK$4.5M – HK$4.935M | HK$67,500 + 10% × excess over HK$4.5M |
| > HK$4.935M – HK$6M | 2.25% |
| > HK$6M – HK$6.72M | HK$135,000 + 10% × excess over HK$6M |
| > HK$6.72M – HK$20M | 3% |
| > HK$20M – HK$21,739,120 | HK$600,000 + 10% × excess over HK$20M |
| > HK$21,739,120 | **4.25%** flat on full consideration |

(Source: [GovHK Stamp Duty Rates IRSD123(E)](https://www.gov.hk/en/residents/taxes/docs/IRSD123(E).pdf))

⚠️ Same Scale 2 applies regardless of buyer status — HKPR, non-HKPR individual, corporate buyer all charged identically since 28 Feb 2024. Pre-28-Feb-2024 BSD 15% + AVD 7.5% + NRSD 15% layering is **historical only**; do not apply to any current transaction.

### Other transaction-side costs

| Item | Cost (HKD) |
|---|---:|
| Solicitor / law firm conveyancing | HK$7,000–HK$15,000 typical residential ([CLIC scale guidance](https://www.clic.org.hk/en/topics/saleAndPurchaseOfProperty/formal_sale_and_purchase_agreement/q9)) |
| Land Registry registration fee | sliding scale ~HK$210–HK$1,030 by consideration band |
| Estate agent commission | typically **1% of price from buyer side + 1% from seller side** (negotiable; cap not statutory but Estate Agents Authority [EAA Practice Direction](https://www.eaa.org.hk/) treats >2% combined as discloseable) |
| Mortgage stamp duty (Mortgage Deed) | HK$5 flat per HK$1,000 of mortgage amount, capped HK$500 typical |
| Building survey (optional pre-purchase) | HK$5,000–HK$25,000 depending on scope |

### Capital gains

- **NO Capital Gains Tax** in Hong Kong ([PwC HK Other Taxes](https://taxsummaries.pwc.com/hong-kong-sar/individual/other-taxes))
- **EXCEPTION**: if disposals are deemed **trading** (frequency, holding period, intent test under IRD's six badges of trade), gains may be assessed as **profits tax** (15% individual / 16.5% corporate)
- Pre-Feb-2024 SSD (Special Stamp Duty up to 20% if held <3 yrs) **abolished** — short-flip penalty no longer applies via stamp-duty channel; profits-tax trading recharacterization remains the operative deterrent

### Inheritance / Estate Duty

- **Estate Duty abolished 11 Feb 2006** by [Revenue (Abolition of Estate Duty) Ordinance 2005](https://www.ird.gov.hk/eng/tax/sdu.htm) — no estate / inheritance / gift tax in Hong Kong
- Probate via Probate Registry of the High Court ([Judiciary website](https://www.judiciary.hk/))

### Future risk

- Periodic discussion of CGT introduction tied to budget deficit (Feb 2025 budget speech ruled out short-term); monitor annual February budget speeches
- Rates concession (one-off rebate) is a near-annual budget feature — 2025/26 budget concession of HK$500 per quarter for Q1 + Q2 ([info.gov.hk 2025-03 budget](https://www.info.gov.hk/gia/general/202503/14/P2025031300515.htm))
- Article 23 SNSO does not amend tax law but tightens cross-border data + financial-disclosure environment; offshore-structuring complexity rising

---

## Section: `--rental`

### Long-term residential

- **Tenancy law**: [Landlord and Tenant (Consolidation) Ordinance Cap. 7](https://www.elegislation.gov.hk/hk/cap7) — tenant protection materially weaker than UK/JP; minimal statutory rent control on private market since Part IV repeal 1998
- **Standard tenancy structure**: 2-year fixed term with "**1+1 break clause**" (1 yr no break / 2nd yr either party 2-month notice); **2-month security deposit + 1-month advance** standard; **rates + government rent** typically borne by **landlord** in private agreements (negotiable but customary)
- **Property Tax** at flat 15% on net rent (after 20% standard deduction, no further itemized deductions except rates if landlord pays + irrecoverable rent) — file via IRD BIR57 / BIR60
- **Salary Tax / Profits Tax** alternative election: if owner has other HK income, may elect Personal Assessment to set rental losses against other income

### Yields (Q2 2025, [GlobalPropertyGuide via RVD HKPPI](https://www.globalpropertyguide.com/asia/hong-kong/rental-yields))

| Area | Gross yield (Q2 2025) |
|---|---:|
| Hong Kong (national avg) | 3.90% |
| Hong Kong Island | 3.61–4.35% (avg 3.9%) |
| Kowloon | 2.49–4.89% (avg 4.13%) |
| New Territories | 3.5–5.5% (varies widely) |
| Tai Koo / Quarry Bay (premium expat) | 3.0–3.6% |
| Sha Tin / Ma On Shan (mid-tier NT family) | 4.0–4.8% |
| Tuen Mun / Tin Shui Wai | 4.5–5.5% |

⚠️ Rental yields hit ~12.5-yr high mid-2024 due to talent-scheme inbound demand vs falling capital values ([SCMP 2024-09](https://www.scmp.com/business/article/3287897/hong-kong-rental-yields-hit-125-year-high-talent-scheme-influx-lower-rates)). 2025-26 stabilization expected.

### Short-term rentals (民宿 / serviced apartments / Airbnb)

⚠️ **CRITICAL: short-term letting < 28 consecutive days requires a licence under [Hotel and Guesthouse Accommodation Ordinance Cap. 349](https://www.elegislation.gov.hk/hk/cap349)**

| Stay duration | Regulation | Practical reality |
|---|---|---|
| **≥ 28 consecutive days** | Outside HAGAO scope — ordinary tenancy regime applies | Serviced-apartment market (e.g., Tai Koo Shing, Sky Tower, Citybase) operates legally |
| **< 28 consecutive days, unlicensed** | **ILLEGAL** — Cap. 349 § 5 offence; max fine HK$200,000 + 2 yrs imprisonment | Most Airbnb listings in HK private residential operate in violation; OLA (Office of Licensing Authority) sweeps regularly |
| **< 28 consecutive days, licensed** | Hotel Licence or Guesthouse Licence required from **Office of the Licensing Authority (HADLA)** under Home Affairs Department | Most residential buildings prohibit guesthouse use via DMC; licence application typically requires fire-safety + building-modification works and DMC consent |

- **Authority**: [HADLA — Hotel & Guesthouse Licensing Authority](https://www.hadla.gov.hk/en/hotels/index.html)
- **DMC restriction**: even if you obtain a Cap. 349 licence, the Deed of Mutual Covenant for most Hong Kong private residential buildings explicitly prohibits "hotel / guesthouse / boarding-house" use — Owners' Corporation can seek injunction
- **Airbnb host responsibility**: platform makes hosts solely responsible; HK has no platform-data-sharing arrangement comparable to EU 2024/1028 ([Airbnb HK responsible hosting](https://www.airbnb.com/help/article/1395))
- **Practical strategic conclusion**: a credible HK short-let strategy is **monthly+ serviced apartment** (≥ 28 days), NOT Airbnb-style nightly. Pursuing nightly without licence is enforcement-exposure that can compound into DMC injunction + criminal record.

### Tax on rental (Property Tax 15%)

- File annual tax return BIR57 (jointly-owned) / BIR58 (corporation) or in BIR60 personal return Schedule 5 (Property)
- Standard deduction: 20% of net rent (covers repair / outgoings)
- Rates paid by owner: deductible
- Mortgage interest: NOT deductible against Property Tax — only deductible if elected Personal Assessment AND property tax basis aggregated
- IRD enforcement: cross-checks AMC (estate management) + utility records; non-declaration penalty up to 3× tax + criminal action

---

## Section: `--work=<profession>`

### Job platforms

- **JobsDB Hong Kong**: `https://hk.jobsdb.com/` (SEEK-owned — broadest mid-market)
- **CTgoodjobs**: `https://www.ctgoodjobs.hk/`
- **LinkedIn Hong Kong**: strong for finance, tech, in-house counsel, expat roles
- **eFinancial Careers HK**: `https://www.efinancialcareers.hk/` (banking / asset management)
- **Glassdoor HK** + **Indeed HK**
- **Recruit / cpjobs**: `https://www.cpjobs.com/`
- **Government job board**: `https://www.csb.gov.hk/`

### Self-employment regimes

- **Sole proprietor / partnership**: register with [Inland Revenue Department Business Registration Office](https://www.ird.gov.hk/eng/pdf/brfee_table.pdf); BR fee HK$2,200 1-yr / HK$5,720 3-yr (2024-25 rate; subject to budget concession)
- **Profits Tax (个人独资业务)**: **two-tier rate** — first HK$2M of assessable profits at **7.5%** individual / 8.25% corporate; balance at 15% individual / 16.5% corporate ([IRD profits tax](https://www.ird.gov.hk/eng/tax/bus_pft.htm))
- **No GST / VAT** in Hong Kong
- **MPF (Mandatory Provident Fund)**: self-employed must contribute 5% of relevant income (capped HK$1,500/month) under Cap. 485
- **No social security (no NIS / NHS-equivalent)**: private medical insurance recommended

### Foreign worker visa interface (cross-section to `--visa`)

- **Top Talent Pass Scheme (TTPS)** — `https://www.immd.gov.hk/eng/services/visas/TTPS.html`
  - Cat A: HK$2.5M+ annual income previous year → 3-yr visa
  - Cat B: top-100-university grad with ≥3 yrs work experience → 2-yr visa
  - Cat C: top-100-university grad <3 yrs experience → 2-yr visa
- **Quality Migrant Admission Scheme (QMAS)**: 60-profession Talent List (2024 update); General Points Test or Achievement-Based Points Test
- **General Employment Policy (GEP)**: standard sponsored work visa; employer-tied
- **Immigration Arrangements for Non-local Graduates (IANG)**: 24-month post-graduation job-search visa
- **New CIES (Capital Investment Entrant Scheme)**: HK$30M+ permissible assets → unsponsored 2-yr visa, 7-yr to PR

PR after 7 years' continuous ordinary residence (immigration test + intent to stay test).

### Salaried benchmarks (median monthly gross 2024 [Census & Statistics Department Quarterly Report on General Household Survey](https://www.censtatd.gov.hk/))

- Hong Kong median monthly employment earnings 2024 Q4: **~HK$20,500** (all employed)
- Finance & insurance: median ~HK$36,000–HK$45,000
- Information & communications (IT): ~HK$32,000–HK$42,000
- Professional services (legal / accounting): senior ~HK$60,000–HK$120,000+
- Construction / hospitality / retail: HK$15,000–HK$22,000
- **Statutory minimum wage**: HK$42.10/hr (effective 1 May 2025 per [Labour Department](https://www.labour.gov.hk/eng/news/mwo.htm))

### Catchment heuristics

- HK Island Central catchment: 30-min commute reachable from all HK Island residential, most Kowloon, Tsuen Wan, Sha Tin via MTR
- Kowloon East (Kwun Tong / Kai Tak) emerging CBD2: Sai Kung, Tseung Kwan O, Kwun Tong residential most efficient
- North/NE NT (Sheung Shui, Fanling, Tai Po): 45–60 min to Central — viable for hybrid-remote
- Outlying islands (Lantau outside Tung Chung, Cheung Chau, Lamma): ferry-dependent — strict commute discipline

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Hong Kong Observatory (HKO 香港天文台)** | `https://www.hko.gov.hk/` | Tropical Cyclone Warning Signal (T1/T3/T8/T9/T10), Rainstorm Warning (Amber/Red/Black), Sea-level Rise projections |
| **Geotechnical Engineering Office (GEO 土力工程處)** under CEDD | `https://www.cedd.gov.hk/eng/about-us/organisation/geo/` | Slope inventory + Landslip Warning System |
| **Slope Information System (SIS)** | `https://hkss.cedd.gov.hk/hkss/en/slope-safety-in-hong-kong/slope-safety-system/overview/index.html` | Search any registered slope by number — current condition, last inspection |
| **Civil Engineering & Development Department (CEDD)** | `https://www.cedd.gov.hk/` | Coastal protection, sea-level rise studies (CCFISD reports) |
| **Drainage Services Department (DSD)** | `https://www.dsd.gov.hk/` | Flood-prone area maps |
| **Buildings Department (BD)** | `https://www.bd.gov.hk/` | Unauthorised Building Works (UBW) register, building safety |
| **Environmental Protection Department (EPD)** | `https://www.epd.gov.hk/` | Strategic noise maps + air-quality monitoring |

### Specific risks (HK)

- **Typhoons (颱風)**: 4–6 tropical cyclones/year affecting HK; T8 issued ~3–6× per season Jun–Oct; **T10** (hurricane signal) historically rare (~1 every 2–4 yrs) but rising frequency — Super Typhoon Mangkhut 2018, Super Typhoon Saola 2023, Super Typhoon Ragasa 2025 (T10 sustained), Typhoon Wipha 2025 (T10 then T8); HKO maintains [historical T10 list](https://www.hko.gov.hk/en/informtc/historical_tc/metinfo_wind.htm)
- **Landslides**: post-1972 Po Shan Road tragedy → systematic Slope Safety System; ~60,000 registered man-made slopes; **GEO Landslip Warning** issues alongside T8 + Amber/Red/Black rainstorm; high-risk neighbourhoods: Mid-Levels, Pok Fu Lam, Tai Hang, Wong Chuk Hang, Mid-Levels East slope corridor
- **Storm-surge / coastal flooding**: 2018 Mangkhut surge breached low-lying Heng Fa Chuen, Lei Yue Mun; CEDD Coastal Hazard Study identifies ~20 vulnerable shorelines
- **Fluvial / pluvial flooding**: Black rainstorm cumulative >70mm/hr; Sept 2023 record >158mm/hr Wong Tai Sin → MTR station inundation; DSD Flood-prone Area Map
- **Earthquake**: HK is on the **passive margin** of South China Block — historical earthquake risk LOW (no major historical event >M6 within 100km); modern code design level **MMI VII / PGA ~0.07g** ([HKO seismicity](https://www.hko.gov.hk/en/gts/equake/seismic_mon.htm)); not a primary structural-design driver
- **Subsidence**: limited; some legacy reclamation areas (West Kowloon, Tseung Kwan O, parts of Tung Chung) — confirm via Lands Department reclamation history layer
- **Subdivided units (劏房)**: not a hazard for buyers but ENV illegal alteration / fire-escape risk in older walk-up buildings — common in Sham Shui Po, To Kwa Wan, Yau Ma Tei

### Build-era hazards (the watershed)

| Era | Code basis | Hazard rating |
|---|---|---|
| **Pre-1955** | Pre-Buildings Ordinance modern era (1956 BO) | 🔴 Tong-lau (唐樓) walk-up; structural concerns + UBW + asbestos |
| **1956–1979** | 1956 Buildings Ordinance + 1973 first wind code | 🟠 Higher rebar risk; ageing facade tile spalling; 不適切 fire-escape; private estates of this era often awaiting **Mandatory Building Inspection Scheme (MBIS)** |
| **1980–2000** | Code of Practice on Wind Loading 1983; Concrete 1987 | 🟡 Sound modern; MBIS due at 30+ yrs (since 2012 mandatory after 30 yrs) |
| **2000+** | Code of Practice for Structural Use of Concrete 2004/2013; Wind Code 2004 | 🟢 Modern. High-rise tower stock |
| **2010+ post-Mong Kok 2010 fatality** | Strengthened façade-spalling regulation; Mandatory Window Inspection Scheme (MWIS) | 🟢 |

⚠️ **Mandatory Building Inspection Scheme (MBIS)** + **Mandatory Window Inspection Scheme (MWIS)** for buildings 30+ yrs ([BD MBIS portal](https://www.bd.gov.hk/en/safety-inspection/mbis/learn-more-about-MBIS/index.html)) — request the building's **MBIS notice + Owners' Corporation compliance status** before any pre-1996 building purchase. Non-compliance → BD Order to Repair → contractor procurement liability falls to Owners' Corporation (i.e., your future levy share).

### Mandatory disclosures (at sale)

| Document | Required because | Source |
|---|---|---|
| **Sale & Purchase Agreement** (provisional + formal) | Standard practice + Estate Agents Practice Regulation | drafted by buyer's solicitor |
| **Land Search (IRIS)** | Solicitor mandatory step | confirms title, mortgage charges, Memorial registrations |
| **Building search (BD)** | Standard | Occupation Permit, UBW register, Order to Repair status, MBIS notices |
| **Lands Department Government Rent + Lease conditions** | Crown Lease compliance | annual rent obligation + breach status |
| **Deed of Mutual Covenant (DMC)** | For multi-unit buildings | usage restrictions (e.g., no guesthouse), undivided share basis |
| **Sales brochure** (first-hand only) | [Residential Properties (First-hand Sales) Ordinance Cap. 621](https://www.elegislation.gov.hk/hk/cap621) | mandatory disclosure incl. saleable area, fittings, lease term, AVD scenarios |

### Climate change projections (HKO + IPCC AR6)

- **HKO Climate Change Projections** (under SSP2-4.5 / SSP5-8.5):
  - Annual mean temperature **+1.7 to +3.4°C** by 2100 vs 1995–2014 baseline
  - Hot nights (Tmin ≥ 28°C): currently ~50/yr → 100–150/yr by 2100 SSP5-8.5
  - Very hot days (Tmax ≥ 33°C): ~30/yr → 80–120/yr SSP5-8.5
  - **Sea-level rise**: **+0.37–0.82m by 2100 SSP2-4.5; +0.57–1.08m SSP5-8.5** ([HKO sea-level projections via gov.hk Climate Change page](https://www.gov.hk/en/residents/environment/global/climate.htm))
  - Extreme rainfall hourly: +20–50% intensity by 2100
  - Tropical cyclone frequency: stable count; intensity (Cat 4-5 super-typhoons) increasing
- Coastal vulnerability: Heng Fa Chuen, Lei Yue Mun, low-lying Tai O, Sai Kung waterfronts, parts of Tung Chung — flag for any property < 5m elevation
- Climate Action Plan 2050: 50% emission reduction by 2035 vs 2005, carbon neutrality before 2050 ([CAP2050 leaflet](https://cnsd.gov.hk/wp-content/uploads/pdf/CAP2050_leaflet_en.pdf))

---

## Section: `--mains`

### National framework

- **Water Supplies Department (WSD 水務署)**: `https://www.wsd.gov.hk/` — sole licensed water utility for the entire SAR
- **Drainage Services Department (DSD 渠務署)**: `https://www.dsd.gov.hk/` — sewerage + stormwater
- Coverage: **>99.9%** of HK population on mains water + sewer; Hong Kong is **fully reticulated** outside a handful of rural NT villages and outlying islands (e.g., parts of Lantau hinterland, Tap Mun, Po Toi)

### Operators

- 100% public: WSD (water) + DSD (sewer) — no private operators
- WSD imports ~70% of fresh water from Dongjiang (Guangdong) under [Dongjiang Water Supply Agreement](https://www.wsd.gov.hk/en/core-businesses/water-resources/dongjiang-water/index.html); ~30% local catchment

### Verification

1. Request **Form WWO46** (WSD water account confirmation) from seller
2. Confirm **DSD sewer connection** via Buildings Dept records or DSD enquiry hotline (2877 0418)
3. For NT village house / unauthorised structures — verify septic tank installation + EPD discharge licence (rural NT pre-1980s villages may discharge to nullah/stream pre-mains-extension)

### Costs (2026 typical)

| Scenario | Cost (HKD) |
|---|---:|
| WSD water account opening (existing connection) | HK$0 admin (deposit HK$1,000–HK$3,000) |
| Water connection + meter installation (new build / new account) | HK$2,000–HK$10,000 |
| Sewer connection (where mains available, NT village) | HK$15,000–HK$80,000 |
| Septic tank installation (rural NT, where no mains) | HK$50,000–HK$200,000 + EPD discharge licence |
| Quarterly water + sewer charges (typical 2-bed apt) | HK$300–HK$700/quarter |

---

## Section: `--crime`

### Primary source

- **Hong Kong Police Force Crime Statistics**: `https://www.police.gov.hk/ppp_en/09_statistics/csc.html`
- **DATA.GOV.HK** crime detail dataset: `https://data.gov.hk/en-data/dataset/hk-hkpf-stat-crm-stat-detail`

### Headline 2024 + 2025 (HKPF / [Security Bureau Law and Order](https://www.sb.gov.hk/eng/special/crime/law.html))

- **2024 total crimes**: 94,747 (+5.0% YoY); driven by deception cases (online fraud)
- **2025 total crimes**: ~89,150 (provisional, **-5.9% YoY** per [news.gov.hk 2026-02-11](https://www.news.gov.hk/eng/2026/02/20260211/20260211_170512_850.html)) — first decline since 2020
- **Robbery 2024**: 90 cases (-7.2% YoY; second-lowest on record); detection rate 92.2%
- **Burglary 2024**: second-lowest on record (figure ~1,300); detection 38%; **NT village houses** disproportionately affected (rural perimeter)
- **Violent crime per capita**: among the world's lowest by World Justice Project + Numbeo aggregate; 2024 homicide rate ~0.3 per 100,000 (one of the lowest globally)

### Verdict bands (HK-specific — vs HK national average)

- 🟢 < 50% national rate (most upmarket residential — Mid-Levels, Pok Fu Lam, Discovery Bay, Tung Chung)
- 🟡 50–110% national rate (typical urban residential — Sha Tin, Tai Po)
- 🟠 110–200% one+ category (Yau Ma Tei, Mong Kok, Sham Shui Po — pickpocketing + deception elevated)
- 🔴 > 200% national in multiple categories (concentrated dosshouse / illicit-activity blackspots — rare in HK; selected Sham Shui Po + Yau Ma Tei sub-blocks)

### Walking-around safety

Hong Kong is one of the safest major cities globally. **Personal-safety risk (street violence) is very low** even in late hours; primary risk to homeowners is **deception / phishing scams + occasional NT village burglary**. CCTV deployment expanding (615 sets installed by end-2024 across territory).

### Confidence

HIGH. HKPF maintains by-district + by-month breakdowns with 5+ year time series; methodology stable post-2020 protests data normalization.

---

## Section: `--amenities`

Universal OSM Overpass logic per `shared/amenities-osm.md`. HK-specific brand-chain conventions:

- **Supermarket**: ParknShop (百佳 — Watson group), Wellcome (惠康 — DCH), AEON, City'Super, Marketplace, Fusion (mid-tier), DON DON DONKI
- **Convenience**: 7-Eleven, Circle K (OK便利店), VanGO
- **Pharmacy**: Watsons (屈臣氏), Mannings (萬寧), big-pharm chains; tag `amenity=pharmacy`. Note: `shop=chemist` in HK is rare; Mannings/Watsons commonly tagged as pharmacy in OSM
- **Hospital**: dual public ([Hospital Authority HA](https://www.ha.org.hk/) — 43 public hospitals) + private (e.g., Hong Kong Sanatorium, Adventist, Matilda); tag `amenity=hospital`
- **Public transport** (HK-specific dense): MTR (`railway=subway`), KMB / Citybus / NWFB (`route=bus`), tram (`route=tram` — HK Island only), Star Ferry + interisland ferries (`amenity=ferry_terminal`), Light Rail (`railway=light_rail` — Tuen Mun / Yuen Long), Peak Tram (`railway=funicular`)

### Verdict bands (HK adjusted — density-shifted)

- 🟢 < 200m / < 3 min walk to MTR / supermarket: dense urban (most HK residential)
- 🟡 200m–800m / 3–10 min walk: typical
- 🟠 800m–2km: NT estate / Lantau remote
- 🔴 > 2km from any MTR or supermarket: outlying island / village (rare for any "private estate" listing)

⚠️ **Octopus card** + MTR proximity defines convenience more than walking-distance to supermarket — HK residents rely on MTR-mall integration. A property "10 min walk from MTR" is materially worse than "5 min walk from MTR" in resale + rental.

---

## Section: `--climate`

Universal logic per `shared/climate-projections.md`. HK-specific overrides:

- **Köppen-Geiger**: `Cwa` (humid subtropical, dry winter — actually marginal Cwa/Cfa)
- **Coastal exposure**: 100% of HK is < 30km from coast; ~60% of population lives in catchment within 5km of coast
- **Reference baseline**: HKO 1991–2020 normal series
- **Key projections** (HKO Climate Change Projections under SSP2-4.5 / SSP5-8.5):
  - Annual mean temperature +1.7 → +3.4°C by 2100
  - Sea-level rise +0.37 → +1.08m by 2100 (range across SSPs)
  - Hot nights frequency triples
  - Heavy-rain hourly intensity +20–50%
  - Tropical-cyclone Cat 4-5 frequency rising
- **Acute-event flags**:
  - 🔴 Coastal property < 5m elevation (Heng Fa Chuen, Lei Yue Mun, Tai O, parts of Sai Kung waterfront, low Tung Chung) under SSP5-8.5 → 🔴 verdict
  - 🟠 Ground-floor / podium-level units in flood-prone catchment (Wong Tai Sin Sept 2023 case study)
  - 🟢 High-rise upper-floor units typical urban — high resilience to sea-level rise; primary climate exposure is operating-cost (cooling + dehumidification)

### Climate verdict (typical urban HK high-rise apt > 30m elevation, > 200m from coast)

🟡 **Watch** — material cooling-load growth; insurance + maintenance cost trajectory upward; building envelope (curtain wall) salt-corrosion accelerates.

### Confidence

HIGH for HKO downscaled projections; MEDIUM for sub-2km sea-level inundation specificity (CCFISD studies ongoing 2024–2026).

---

## Section: `--finance`

### Mortgage market (post-Oct 2024 reform)

- **Regulator**: [HKMA — Hong Kong Monetary Authority](https://www.hkma.gov.hk/) — sets countercyclical macroprudential measures via [Banking (Capital) Rules](https://www.hkma.gov.hk/eng/news-and-media/press-releases/prudential-measures-and-other-mortgage-related-matters)
- **LTV caps (post 2024-10-16 [HKMA circular](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2024/10/20241016-4/))**:

| Property value / occupancy | Max LTV |
|---|---:|
| **All residential properties** (regardless of value, self-use or non-self-use) | **70 % (flat)** |
| Net-worth-based | 70 % (also unified) |

(2026-05-27 verified — correction from prior tiered table. Per [HKMA press release 2024-10-16](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2024/10/20241016-4/): *"The maximum loan-to-value (LTV) ratio for all residential properties will be set at 70%, regardless of the value of the property."* The prior tiered 70 % ≤30M / 60-70 % 30-35M / 60 % >35M schedule no longer applies post 16 Oct 2024.)

- **DSR (Debt Servicing Ratio)**: **standardised at 50 %** of monthly income for all residential AND non-residential properties, self-use AND non-self-use (HKMA 16 Oct 2024 unification); **stress test SUSPENDED 28 Feb 2024** (was +200 bps stress; HKMA still applies internal +100bps benchmark via [HKMA stress-test FAQ](https://www.hkma.gov.hk/media/eng/doc/other-information/FAQ_J1_Table_Eng.pdf))
- **Mortgage Insurance Programme (MIP)** via [HKMC Insurance Ltd](https://www.hkmc.com.hk/) — top-up to 80–90% LTV for properties ≤ HK$10M (first-time buyer); insurance premium 2–5% of mortgage amount
- **Rate structure**:
  - **H-Plan (HIBOR-linked)**: HIBOR 1M + 1.30–1.50% spread; capped at P-cap (cap rate near Prime); **dominant** product post-2008
  - **P-Plan (Prime-linked)**: Prime − 2.0–2.5% (Prime = 5.625% HSBC/Hang Seng/SCB or 5.875% BOCHK as of Q1 2026); secondary
  - 30-year amortization standard; fixed-rate residential mortgages rare
- **HIBOR cycle**: HKD pegged → tracks USD Fed; 1M HIBOR Q1 2026 ≈ 4.0–4.5% (down from peak ~5.5% in 2023). Effective mortgage rate Q1 2026: ≈ 3.5–4.0% all-in
- **Foreigner mortgages**: most HK retail banks offer to non-residents but typically demand:
  - HK bank account (open with passport + proof of address)
  - est. 50–60% LTV maximum (bank-by-bank policy, not an HKMA cap; more conservative than HKPR) — confirm with target bank
  - Income evidence + tax returns from home country
  - Major non-resident-friendly: HSBC, Standard Chartered, BOCHK, Hang Seng, DBS, Citibank

### Banking access

Account opening requires HKID for residents; for non-residents, in-person visit + W-8BEN/CRS forms; common entry: HSBC Premier (HK$1M+ TR), SCB Priority, Citi Priority. Online-only Mox / ZA Bank / WeLab — mostly HKID-only.

⚠️ **Foreigner non-resident bank accounts** have tightened post-2020 NSL + 2024 SNSO; account opening more selective for cross-border income earners — confirm via target bank in advance.

---

## Section: `--currency`

### Linked Exchange Rate System (LERS)

- **Peg**: HK$7.80 ± **HK$0.05** band (7.75–7.85) to USD since 17 Oct 1983; HKMA Convertibility Undertaking enforced via interbank intervention
- **Strong-side CU**: HKMA sells HKD at 7.75 when demand pushes HKD up
- **Weak-side CU**: HKMA buys HKD at 7.85 when supply pushes HKD down
- **Mechanism**: automatic interest-rate adjustment via Aggregate Balance — HK interest rates de facto track US Federal Funds Rate

### What this means for buyers

- **USD-denominated buyers** (US, Latin America with USD assets): **near-zero FX risk** for purchase + ongoing payments
- **EUR / GBP / JPY buyers**: HKD effectively a USD-tracking currency; FX exposure = your home-vs-USD exposure. Use forward contracts for transaction cost-base lock-in if material
- **CNY (RMB) buyers**: NOT pegged to RMB; HKD/CNY rate variable (Q1 2026 ≈ 0.92 HKD/CNY); cross-border capital flows from mainland subject to Stock Connect + Wealth Management Connect frameworks, NOT free convertibility
- **Hedging products**: deep FX-forward + options market via HK banks; typical 12-month USD/EUR forward bid-ask 5–15 bps for HK$ amounts >HK$10M

### Peg credibility

HKMA's [USD foreign reserves](https://www.hkma.gov.hk/eng/news-and-media/press-releases/2026/05/20260507-5/) = USD 442.1B at end-April 2026 (end-March 2026: USD 430.8B) — over 5× currency in circulation, ~38% of HKD M3 (2026 data, source HKMA press release 7 May 2026). Peg defended successfully through 1997 Asian crisis, 1998 GFC stress, 2018-2020 trade-war pressure, 2022-2024 USD-strength cycle (HKMA bought HKD at 7.85 weak-side multiple times Apr 2022 – Aug 2023; Jul 2025 again per [Xinhua 2025-07-03](https://english.news.cn/20250703/45563ff358854f1d95d7a72ba1924b74/c.html)). Periodic academic + policy debate on long-term sustainability ([Wharton 2025 working paper](https://fnce.wharton.upenn.edu/wp-content/uploads/2025/08/UrbanJermann2_12_25.pdf)) — not a near-term break risk.

⚠️ **Tail risk**: any sustained breakdown of LERS would re-rate HKD-denominated property substantially in foreign-currency terms. Position-size with this in mind for foreign-currency-denominated buyers.

---

## Section: `--visa`

### Talent + investor schemes (most relevant for property-acquisition decision)

| Scheme | Threshold | Visa | PR path |
|---|---|---|---|
| **TTPS Cat A** | HK$2.5M+ annual income previous year | 3-yr | 7 yrs ordinary residence |
| **TTPS Cat B** | top-100-uni grad + 3 yrs experience | 2-yr | 7 yrs |
| **TTPS Cat C** | top-100-uni grad < 3 yrs experience | 2-yr | 7 yrs |
| **QMAS** | General Points + Achievement-Based | 2-yr | 7 yrs |
| **GEP / ASMTP** | employer-sponsored skilled worker | usually 2-yr | 7 yrs |
| **IANG** | recent HK uni graduate | 24-mo job search | 7 yrs from arrival |
| **CIES (New)** | HK$30M+ in permissible assets | 2-yr extendable | 7 yrs |

### CIES asset rules ([New CIES portal](https://www.newcies.gov.hk/))

- Total HK$30M+ across:
  - **Listed equities + bonds + qualifying funds**: max-permissible allocation
  - **Hong Kong real estate** (post 17 Sept 2025 reform): minimum single-property transaction HK$30M (lowered from HK$50M); aggregate real-estate cap HK$15M of which residential ≤ HK$10M (non-residential can fill the additional HK$5M); only the capped amount counts toward the HK$30M, balance must be in financial assets ([newcies.gov.hk Investment Requirement](https://www.newcies.gov.hk/en/application-procedures/application-to-investhk/investment-requirement/)) — essentially an "ancillary" bucket, NOT primary qualifying investment
  - **Non-residential property**: case-by-case
  - **Capital Investment Entrant Scheme Investment Portfolio**: alternative pooled-fund route
- Net-worth threshold: HK$30M+ for 6 months preceding application

⚠️ Property-only CIES strategy does **NOT** qualify; property is genuinely ancillary. Most CIES applicants combine listed-securities portfolio with apartment.

### Permanent Residence

7 years' continuous ordinary residence + intent to make HK permanent home → apply for **Right of Abode** under [Immigration Ordinance Cap. 115 § 2(4)](https://www.elegislation.gov.hk/hk/cap115). Failure of intent test (e.g., never primary residence, no family ties, no employment) → application refused even at 7-year mark.

### Article 23 / SNSO consideration (cross-section)

23 Mar 2024 SNSO does not change immigration mechanics. Material to **dual-nationality holders**: HK does not formally recognize dual nationality for Chinese nationals; a Chinese-national HK PR who acquired foreign nationality and wishes to retain HK consular protection should declare nationality change to ImmD. SNSO + State Secrets provisions extra-territorial — review profession + employer compliance separately.

---

## Section: `--insurance`

### Mandatory

- **Fire Insurance**: required by every mortgage lender; covers building structure (NOT contents); typical premium **0.03–0.15% of sum insured** ([Generali HK 2024](https://www.generali.com.hk/EN_US/blog/insurance-knowledge/fireinsurance))
  - Sum insured = **rebuild cost** (not market price) — est. ~HK$3,000–HK$8,000 per saleable sq ft for standard concrete frame (market heuristic, not an insurer-published rate; confirm with a quantity surveyor / RICS HK rebuild-cost assessment)
  - Multi-unit DMC may stipulate **block-policy** purchased centrally by Owners' Corporation; individual unit owners pay pro-rata via management fee — confirm before duplicating
- **Third-party liability**: typically embedded in home-content / fire policy; statutory minimum HK$10M typical for Owners' Corporation block policy

### Optional but standard

| Cover | Typical premium (2026) |
|---|---:|
| **Home Contents Insurance** (typical 700 sq ft 2-bed) | HK$700–HK$3,000/yr ([Bowtie HK reviews](https://www.bowtie.com.hk/blog/en/insurance101/home-insurance/)) |
| **Typhoon / windstorm** | usually included in fire + contents bundle |
| **Flood** | included in major bundles (Generali, AXA, Bowtie); confirm sub-limit |
| **Earthquake** | usually included up to small sub-limit (HK low risk; not headline) |
| **Domestic helper insurance** (if hiring) | Mandatory under [Employees' Compensation Ordinance Cap. 282](https://www.labour.gov.hk/eng/public/ecd/Know_more_about_taking_out_ECI_eng.pdf) — HK$500–HK$1,500/yr per helper |

### Major insurers

AIA, AXA, Manulife, Prudential, Generali HK, Bowtie (digital-first), HSBC Insurance, MSIG, Zurich HK. Compare via [10Life](https://www.10life.com/) + [MoneyHero](https://www.moneyhero.com.hk/).

### Climate trajectory note

⚠️ HK insurance premiums rising 5–10%/yr 2023–2026 driven by Mangkhut/Saola/Ragasa typhoon claims load + black-rain Sept 2023 surge claims. Underwriters tightening sub-limits on ground-floor / B1 / B2 units in flood-prone catchments (Wong Tai Sin, low Tung Chung, parts of NT village).

---

## Section: `--notary`

### Conveyancing process

Hong Kong does NOT have a civil-law notary; **solicitors qualified under [Legal Practitioners Ordinance Cap. 159](https://www.elegislation.gov.hk/hk/cap159)** handle the entire transfer (drafting, execution, registration). Common-law conveyancing structure inherited from UK pre-1997.

### Standard timeline (typical residential, post-Feb 2024)

| Step | Day | What happens |
|---|---|---|
| 1. Provisional Sale & Purchase Agreement (臨時買賣合約) | D0 | Buyer pays **initial deposit 3–5% to seller's solicitor stakeholder account**; agent commission portion typically due |
| 2. Solicitor instructed | D0–D7 | Each side appoints solicitor; buyer's solicitor begins **Land Search (IRIS) + Building Search + Lease conditions check** |
| 3. Formal Sale & Purchase Agreement (正式買賣合約) | ~D14 | Further deposit (typically up to 10% cumulative); AVD payable within 30 days of Provisional |
| 4. Mortgage approval | D14–D45 | Bank valuation + offer letter; typical 3–6 weeks |
| 5. Completion | D60–D90 | Final 90% paid; **Memorial of Assignment registered at Land Registry within 1 month** |

### Costs

| Item | Typical |
|---|---|
| **Solicitor fee** (buyer side) | HK$7,000–HK$15,000 + disbursements (Land Registry fees, search fees, courier ~HK$2,000–HK$3,000) ([Hong Kong Lawyer Magazine — Conveyancing fees](https://www.hk-lawyer.org/content/conveyancing-fees-and-other-issues)) |
| **Solicitor fee (seller side)** | HK$5,000–HK$10,000 |
| **AVD Stamp Duty** | per Scale 2 (see `--tax`) |
| **Mortgage instrument stamp duty** | HK$5/HK$1,000 capped ~HK$500 |
| **Land Registry registration fee** | sliding HK$210–HK$1,030 |
| **Memorial filing fee** | HK$220 |
| **Total transaction cost (buyer side)** | **~3–6% of price** typical (much lower than UK 8–18% post-Oct-2024 reform) |

### Solicitor selection

Source: [Law Society of Hong Kong directory](https://www.hklawsoc.org.hk/) (~12,000+ solicitors). Typical good-fit firms for residential conveyancing: K. C. Ho & Fong, Chan & Co, Cheung & Liu, larger firms (Mayer Brown, Deacons, Mayer Brown JSM) for high-value or cross-border. ⚠️ The buyer should NOT use the seller's solicitor — independent representation strongly recommended (no statutory bar but Estate Agents Authority practice direction discourages dual representation).

### Foreign buyer practical

- **No need to be present in HK**: solicitor accepts Power of Attorney for execution; identity verification via apostilled passport copy + sworn declaration before solicitor in home jurisdiction
- **Beneficial ownership disclosure**: post-2018 Companies Ordinance Significant Controllers Register applies to corporate buyers; individual buyers identity verified at solicitor level
- **AML / source-of-funds**: solicitor required to obtain bank statements + source-of-funds declaration under [Drug Trafficking (Recovery of Proceeds) Ordinance Cap. 405](https://www.elegislation.gov.hk/hk/cap405) + AMLO Cap. 615

---

## Section: `--compare`

### Hong Kong vs APAC neighbours (residential investment lens, Q1–Q2 2026)

| Country | Foreign-buyer rule | Acquisition cost (typical) | Annual recurring | Yield (Q2 2025) | Currency risk |
|---|---|---:|---:|---:|---|
| **🇭🇰 Hong Kong** | Open since Feb 2024 (no BSD/SSD/NRSD); AVD Scale 2 only | 3–6% | Rates 5% RV + Gov Rent 3% RV + mgmt fee | **3.9%** | HKD pegged USD |
| **🇸🇬 Singapore** | ABSD 60% for foreigners (post Apr 2023) | 60–65%+ | Property tax progressive 0–32% | ~3.2% | SGD managed-float |
| **🇯🇵 Japan** | Open; no foreign-buyer surcharge | 6–10% | 固定資産税 1.4% + 都市計画税 0.3% | ~4.0% Tokyo central | JPY free-float |
| **🇰🇷 South Korea** | Open; case-by-case minor | 5–10% | Acquisition + property taxes | ~3.5% | KRW free-float |
| **🇹🇼 Taiwan** | Reciprocity rule; case-by-case | 6–8% | House tax + land value tax | ~2.0–3.0% | TWD managed-float |
| **🇹🇭 Thailand** | Foreigners cannot own land; condo OK ≤49% foreign quota | 6–8% | Property tax low | ~5.0–7.0% | THB free-float |

### Hong Kong's distinctive position

- **Lowest transaction cost of major APAC** (3–6% all-in) post-Feb-2024 abolition — significantly below UK 8–18%, Singapore 60%+ for foreigners, Japan 6–10%
- **No CGT, no inheritance tax, no GST/VAT** — simpler ongoing tax footprint than UK / EU / JP
- **Currency stability**: HKD-USD peg removes most FX risk for USD asset holders
- **Cyclically attractive entry 2024–2026**: 28% peak-to-trough decline Feb 2022–Aug 2025 + transaction-cost reform → entry-price discount + low all-in friction
- **Counter-balance risks**: post-2020 political environment; Article 23 SNSO; demographic stagnation (population net-flat 2025); ageing high-rise stock + MBIS levy exposure

### Comparative reference

For HK vs UK leasehold structure parallels see `countries/uk/playbook.md`. For HK vs JP transaction-cost benchmarks see `countries/jp/playbook.md`. For Singapore comparison: HK is the dominant lower-friction APAC alternative for foreign capital post-ABSD-60%.

---

## Section: `--retirement`

### Retirement to Hong Kong scenario

Hong Kong is **NOT** a retirement-first destination by international standards — high-CoL, dense, no specific retirement visa category. Most foreign retirees in HK arrive via:

1. **Dependent visa** (sponsored by HKPR / working spouse)
2. **CIES** (HK$30M+ assets)
3. **Right of Abode** earned via 7+ year prior residence
4. **Returning HKPR** (lifelong RoA via past residence)

### Cost-of-living for retirees

- Median 2-bed apt rental Q1 2026: HK$22,000–HK$45,000/month outside prime
- Public healthcare via Hospital Authority: HK$180/day general ward (HKID-holders); foreign-resident non-eligibles billed at full cost
- Private health insurance for 65+: HK$15,000–HK$50,000/yr typical
- MTR concession 60+: HK$2 flat senior fare (with valid Octopus card)
- Utilities (2-bed apt): HK$2,000–HK$4,000/month
- **MPF (Mandatory Provident Fund)**: members can withdraw at age 65 lump-sum or in instalments

### Tax position for retirees

- **No CGT, no estate duty, no wealth tax** → HK is a low-tax retirement jurisdiction in international comparison
- Foreign-source pension income generally NOT taxed (territorial system; pension is foreign-sourced if non-HK employer)
- Salaries Tax applies only if working post-retirement
- **Property Tax 15%** if letting other HK properties

### Healthcare access

[Hospital Authority](https://www.ha.org.hk/) operates 43 public hospitals + 72 specialist outpatient clinics; world-class quality; long wait times for non-urgent. Major private hospitals (Hong Kong Sanatorium, Adventist, Matilda International, St Paul's) — quoted in HK$ tens of thousands per stay.

### Verdict for retirement-first buyers

🟡 **Watch** — viable for high-net-worth retirees (HK$10M+ liquid + private health insurance) seeking APAC tax efficiency; questionable for moderate-net-worth retirees seeking lifestyle (Lisbon / Valencia / Chiang Mai dramatically cheaper). Best fit: returning Cantonese-speaking diaspora + CIES candidates seeking dual base.

---

## Section: `--digital-nomad`

### Visa pathway

Hong Kong has **NO formal "digital nomad visa"** comparable to Portugal D8 / Spain DNV / Estonia DNV. Workable pathways for remote-working visitors:

1. **Visitor (visa-free) entry** — varies by passport; up to 90 days (most Western); 180 days (UK); 14 days (some): ⚠️ **WORK is technically prohibited** even for foreign-employer remote work — ImmD enforces case-by-case. Short remote-stay tolerated; sustained "working from HK" without employment visa is non-compliant
2. **TTPS / QMAS** — valid for genuine high-income remote workers with employer sponsorship or proven income/qualification
3. **IANG** — for recent local-uni grads only
4. **Dependent visa** — if spouse holds working/PR visa

### Connectivity

- **Internet**: gigabit FTTB (HKBN, Netvigator/PCCW, China Mobile HK, SmartTone) widespread; HK$200–HK$400/month for 1-Gbps fibre
- **Mobile**: HK$100–HK$300/month for 5G unlimited; eSIM (3HK / China Mobile HK / Csl)
- **Co-working**: WeWork, The Hive, Garage Society, Naked Hub, Industrial Centre — HK$2,500–HK$8,000/month hot desk
- **Time zone**: UTC+8 — favours APAC + East Coast US asynchronous work; 12-13 hour gap to US Pacific / 7-8 hr to Europe

### Cost-of-living for remote worker (Q1 2026)

- Studio short-let: HK$15,000–HK$28,000/month (Sheung Wan, Kennedy Town, Sai Ying Pun, Tai Hang, Causeway Bay)
- Co-living (Weave, Dash Living, Hmlet): HK$10,000–HK$20,000/month
- Single-meal eating-out: HK$50–HK$150 cha chaan teng / HK$200–HK$500 mid-range / HK$800+ premium
- Monthly transport: HK$500–HK$1,500 Octopus typical

### Tax position

- **Salaries Tax** applies on income for services rendered IN Hong Kong (territorial source); a remote worker employed by foreign employer working FROM HK > 60 days/yr is technically on the hook for Salaries Tax on the HK-rendered portion — IRD has [60-day rule](https://www.ird.gov.hk/eng/pdf/dipn10.pdf) (DIPN 10) for visiting employees
- **No specific digital-nomad tax incentive** (cf. Portugal / Greece / Cyprus)
- Verify employer can hire/pay HK-tax-residents; many cannot without HK PE setup

### Verdict for digital-nomad-first buyers

🟠 **Adapt** — HK is great as an APAC base for established high-earners with employer support, but cost-of-living + visa friction make it suboptimal for "freelance digital nomad" buy-and-host pattern. If the goal is short-let income while abroad, the Cap. 349 < 28-day prohibition kills the standard Airbnb model — pivot to monthly+ corporate let.

---

## Section: `--macro`

### Headline 2024–2026

- **GDP growth 2024**: +2.5% (HKMA / Census & Statistics)
- **GDP growth 2025**: +2.3% (provisional)
- **GDP growth forecast 2026**: +2.0–3.0% (range across IMF Article IV / HKMA)
- **GDP per capita 2025**: ~USD 46,583 (constant 2015) / ~USD 53,000 (current)
- **Inflation 2025**: ~1.7% headline; ~1.3% underlying
- **Unemployment 2025 Q4**: ~3.2%
- **Public debt / GDP**: structurally low (~5%); fiscal reserves ~HK$700B
- **Population**: 7,510,800 end-2025; -0.7% net natural; +0.8% talent migration → +0.1% net

### Trend drivers (2024–2026)

- **Talent inflow surge**: TTPS approvals 2024 ~187,000 (cumulative); net positive migration 2024 + 2025 reversed pandemic-era outflow
- **Mainland integration**: GBA (Greater Bay Area) cross-border financial-product expansion (Wealth Management Connect 2.0 launched 2024)
- **US-China cycle exposure**: HKD-USD peg → HK monetary conditions tied to Fed; equity market sensitivity to mainland regulatory cycle
- **Real-estate-as-fiscal-anchor**: ~30% of government revenue historically from land + stamp-duty; Feb-2024 stamp-duty reform reduced this share — fiscal realignment ongoing

### Key 2024–2026 reforms (cross-section)

- **28 Feb 2024**: stamp-duty cooling measures fully abolished
- **1 Mar 2024**: New CIES launched
- **23 Mar 2024**: Article 23 SNSO effective
- **2024**: Extension of Government Leases Bill resolves 2047 question
- **16 Oct 2024**: HKMA LTV expanded
- **2025 Q4**: HKPPI YoY positive after 42-month decline

### IMF Article IV (latest)

[IMF 2025 Article IV](https://www.elibrary.imf.org/view/journals/002/2025/016/article-A003-en.xml) flags climate-transition exposure, ageing demographics, and continued political-uncertainty discount as primary structural risks. Property-market: cyclically near trough; structural tailwind from talent inflow + monetary easing 2025–2027.

---

## Section: `--demographics`

### Population structure (end-2025, [Census & Statistics 2026-02-12 release](https://www.info.gov.hk/gia/general/202602/12/P2026021200283.htm))

- **Total**: 7,510,800
- **Male / Female**: 3.34M / 4.07M (45.05% / 54.95%)
- **Median age**: 47.9 years (one of the world's oldest)
- **Age 0–14**: ~10%
- **Age 15–64**: ~67%
- **Age 65+**: ~23% (rising fast — projected to reach 36% by 2046 per Census C&SD projections)
- **Natural change 2025**: -18,900 (births 31,100, deaths 50,000)
- **Net migration 2025**: +29,100 (talent schemes + family reunification)
- **Total fertility rate**: ~0.7 (lowest globally with South Korea + Taiwan)

### Geographic distribution

- Hong Kong Island: ~1.25M (16.6%)
- Kowloon: ~2.18M (29.0%)
- New Territories: ~4.08M (54.4%) — most population growth concentrated here

### Households

- ~2.69M domestic households (2024)
- Average household size: 2.7 persons (declining)
- Owner-occupier rate: ~50% (incl. ~15% public-housing equivalent)
- Public housing (HOS / PRH): ~46% of population

### Implication for property

- **Demand floor 2025–2030**: net-positive talent migration > natural decrease — sustained inbound demand for mid-tier private rental (TTPS / CIES typical demographic: 30–50 yo professional family)
- **Supply pipeline**: ~107,000 first-hand units 2026–2030 in [Hong Kong Property Review 2026](https://www.rvd.gov.hk/doc/en/HKPR2026_Preliminary_Findings_Eng.pdf) — material absorption test
- **Ageing risk**: HOS resale market + older private estates (1980s-built) face demographic supply pressure as estate-planning unwinds — discount opportunity in 1980s-1990s mid-tier estates with full MTR connectivity

---

## Section: `--esg`

### Climate-transition exposure

- **Climate Action Plan 2050**: 50% emission reduction by 2035 (vs 2005), carbon neutrality before 2050 ([CNSD CAP2050](https://cnsd.gov.hk/en/climate-ready/climate-targets-of-hk/))
- **Buildings sector**: contributes ~60% of HK CO₂ emissions; **BEAM Plus** + **HKGBC (Hong Kong Green Building Council)** standards drive private-sector certification
- **Mandatory Energy Efficiency Labelling Scheme** for residential appliances ([EMSD MEELS](https://www.emsd.gov.hk/en/energy_efficiency/mandatory_energy_efficiency_labelling_scheme/))
- **Buildings Energy Efficiency Ordinance Cap. 610** — energy audit + retro-commissioning required for commercial buildings; residential exempt

### Property-level ESG considerations

- **BEAM Plus** certification (Provisional Gold / Platinum / Final): ~30% of new private residential 2020+; not standard pre-2015 stock
- **EE label**: kitchen + window AC + lighting energy class A-E mandatory disclosure on resale (per EMSD)
- **Green-mortgage loans**: HSBC + SCB + BOCHK + DBS HK offer 5–15bps rate reduction for BEAM-Plus Platinum/Gold properties (selective; verify with bank)
- **Solar PV / district cooling**: rare in residential; some new estates (e.g., Hung Hom Pacific Wave) have district cooling

### Climate-physical risk (cross-section to `--climate` + `--risks`)

- Sea-level rise + storm surge: low-elevation coastal stock progressively higher insurance + retrofit cost
- Cooling-load growth: 1.7–3.4°C warming + tropical-night frequency triple → operating-cost up + envelope-stress (curtain wall thermal cycling) up
- Building-envelope salt corrosion: HK's tropical-marine atmosphere + post-typhoon spray → 30+ yr stock requires escalating façade-maintenance; MBIS levy exposure rising

### Social / governance factors

- Hong Kong Stock Exchange [HKEX ESG Reporting Guide (Appendix C2)](https://en-rules.hkex.com.hk/rulebook/environmental-social-and-governance-reporting-guide-1) mandatory for listed companies; trickles to property developers (Sun Hung Kai, Henderson, CK Asset, New World) annual sustainability reporting
- Owners' Corporation governance under [Building Management Ordinance Cap. 344](https://www.elegislation.gov.hk/hk/cap344) — minority-protection mechanisms via Lands Tribunal

### Verdict (ESG lens for typical HK private apt)

🟡 **Watch** — non-BEAM-Plus pre-2015 stock progressively below market expectation by 2030; mid-tier retrofit (window upgrade, AC modernization, façade overhaul) becomes mandatory cost; BEAM-Plus stock + green-mortgage holders carry resilience premium.

---

## Section: `--exit`

### Resale market liquidity

- **Average days on market 2025 Q4**: ~60–120 days (mid-tier mass private); 90–180 days (luxury > HK$30M); 30–60 days (in-demand estates with MTR + school catchment)
- **Cyclical sensitivity**: HK secondary market is **highly liquid in upcycle** (2017 peak ~10,000+ private resale transactions/month) and **thin in downcycle** (2024 trough ~3,000–4,000/month)
- **Centa-City Index methodology**: weekly published index based on formal SPA dates → leading indicator of liquidity restoration

### Exit-cost stack (seller side, post-Feb-2024)

| Item | Cost |
|---|---|
| Estate agent commission (seller side) | typically **1% of sale price** + 5% gov AVD on commission |
| Solicitor fee (seller side) | HK$5,000–HK$10,000 |
| **NO Special Stamp Duty** since 28 Feb 2024 abolition (was up to 20% for sales <3 yrs from purchase) — short-flip penalty removed |
| Mortgage early-discharge fee | HK$2,000–HK$5,000 admin + clawback of any cash rebate received at origination (typically claw-back if held <2 yrs from drawdown) |
| **No CGT on capital appreciation** (unless trading-recharacterized — see `--tax`) |
| Total exit cost | **typically 1.5–3% of sale price** (vs 5–10% in many EU jurisdictions) |

### Trading-recharacterization risk (six badges of trade)

If IRD assesses sale as "trading" rather than capital disposal:
- **Frequency**: multiple flips within short period
- **Holding period**: very short hold (e.g., < 1 yr; especially if purchased off-plan)
- **Subject matter**: bulk purchase / multi-unit
- **Method of acquisition / disposal**: financed via short-term debt; reseller-style marketing
- **Modifications / improvements**: substantial reno → resale
- **Stated intent at acquisition**: documented investment-vs-flip intent

→ Profits Tax assessment 15% individual / 16.5% corporate on entire gain. Substantially worse outcome than the no-CGT default. Document genuine investment intent at purchase (lease-out track record, primary residence affidavit).

### Liquidity by sub-segment (qualitative, 2026)

| Segment | Liquidity | Notes |
|---|---|---|
| Mid-tier mass private (HK$5–15M) MTR + school | 🟢 strong | Sha Tin City One, Mei Foo Sun Chuen, Tai Koo Shing — perpetual ready buyer pool |
| Premium high-rise (HK$20–60M) | 🟡 selective | TTPS / CIES inbound demand 2024–2026 helping |
| Ultra-luxe (HK$100M+) The Peak / Repulse Bay | 🟠 thin | <50 transactions/yr; mainland-buyer cyclicality |
| New build first-hand (developer release) | 🟢 promo | Developer financing + cash rebates; resale ~6–24 months later typically discount-to-launch |
| HOS resale (subsidized) | 🟡 special regime | Restricted resale (Form A premium-paid only); separate ecosystem |
| NT village house | 🟠 niche | Indigenous-villager + 丁屋 framework; thin secondary market |

### Verdict for exit risk

🟢 for mid-tier MTR-served mass private; 🟡 for premium; 🟠 for ultra-luxe and NT village. Post-2024 stamp-duty abolition + LTV easing materially improved exit liquidity; CGT-free regime preserves capital appreciation.

---

## Cost benchmarks (HK 2026)

| Item | Cost (HKD) |
|---|---:|
| Solicitor (residential conveyancing, buyer side) | HK$7,000–HK$15,000 |
| Solicitor (residential conveyancing, seller side) | HK$5,000–HK$10,000 |
| Land Registry registration fee | HK$210–HK$1,030 (sliding) |
| Estate agent commission (each side) | ~1% of price |
| AVD Stamp Duty (Scale 2) | HK$100–4.25% per band |
| Mortgage instrument stamp | HK$5/HK$1,000 (cap ~HK$500) |
| Pre-purchase building survey | HK$5,000–HK$25,000 |
| Annual Rates (5% RV, typical 2-bed apt RV HK$300k) | ~HK$15,000/yr |
| Annual Government Rent (3% RV, same RV) | ~HK$9,000/yr |
| Management fee (2-bed apt mass private) | HK$2,500–HK$4,500/month |
| Sinking fund contribution | HK$200–HK$800/month |
| Fire insurance (HK$5M sum insured) | HK$1,500–HK$7,500/yr |
| Home contents (700 sqft 2-bed) | HK$700–HK$3,000/yr |
| Renovation (basic refresh, 2-bed apt) | HK$200,000–HK$500,000 |
| Renovation (full redo, 2-bed apt) | HK$600,000–HK$1,500,000 |
| **Total transaction cost (buyer side, residential)** | **~3–6% of price** |

## Active fiscal incentives (2025–26)

- **HKMC Mortgage Insurance Programme (MIP)** — top-up to 80–90% LTV for properties ≤HK$10M (first-time HKPR buyer); insurance premium 2–5% capitalised
- **Rates concession** (annual budget: 2025/26 HK$500/quarter Q1+Q2 per [info.gov.hk 2025-03 budget](https://www.info.gov.hk/gia/general/202503/14/P2025031300515.htm))
- **Home Ownership Scheme (HOS)** — subsidized resale for HKPR low/middle-income; quotas via Housing Authority
- **Green Form** subsidy schemes for transition from public rental to ownership
- **No first-time-buyer stamp-duty discount** (post-Feb-2024 reform — Scale 2 already low at ≤HK$3M consideration)
- **CIES property bucket** (post 17 Sept 2025 reform): minimum single-property transaction HK$30M (lowered from HK$50M); aggregate real-estate cap HK$15M (residential cap remains HK$10M; non-residential can fill the additional HK$5M); applies to purchases on/after 17 Sept 2025 (2026-05-27 verified, source [newcies.gov.hk Investment Requirement](https://www.newcies.gov.hk/en/application-procedures/application-to-investhk/investment-requirement/))
- **BEAM Plus green-mortgage rate concession** — 5–15bps via select banks

## Common listing platforms

- **Centaline / Centanet**: `https://hk.centanet.com/home/index.aspx`
- **Midland Realty**: `https://www.midland.com.hk/`
- **Squarefoot.com.hk** (Ricacorp): `https://www.squarefoot.com.hk/`
- **28Hse.com**: `https://www.28hse.com/`
- **Spacious.hk** (English-language): `https://www.spacious.hk/`
- **OKAY.com** (English / prime): `https://www.okay.com/`
- **GoHome.com.hk** + **Property.hk**

## Caveats unique to HK

- **All land is leasehold from Government** — no freehold; 2047 question resolved 2024 by [Extension of Government Leases Bill](https://www.devb.gov.hk/en/legco_matters/replies_to_legco_questions/index_id_9304.html) (auto 50-yr extension) but verify exact lease conditions of target lot via Lands Department lease search
- **Saleable area (實用面積) post-2013 mandatory** — pre-2013 listings may quote gross area inflating space 15–30%; always confirm 實用面積
- **Cap. 349 short-let prohibition < 28 consecutive days** — kills standard Airbnb-style short-let model; pivot to monthly+ serviced apartment
- **No CGT, no estate duty, no GST/VAT** — HK is structurally low-tax compared to UK/EU/JP; trading-recharacterization the main downside
- **Stamp duty Scale 2 only since 28 Feb 2024** — historical BSD/SSD/NRSD analyses are obsolete; verify current state in any 2024+ analysis
- **HKMA LTV unified at a flat 70%** for all residential properties regardless of value post 16 Oct 2024 (the earlier tiered HK$30M / HK$35M schedule no longer applies — see `--finance`) — verify with target bank
- **MBIS / MWIS levy exposure** for buildings >30 yrs — request Owners' Corporation compliance status
- **DMC restrictions**: hotel/guesthouse/short-let prohibition near-universal in private residential; verify before any STR strategy
- **Ten-year-plus old buildings** with cracking façades / structural concerns: BD Order to Repair → Owners' Corporation special levy unavoidable
- **HOS resale (Home Ownership Scheme)**: separate regulatory regime (Housing Authority Form A premium / Form B Green-Form); not interchangeable with private market
- **NT village house (丁屋) Small House Policy**: indigenous-villager-only acquisition right; thin secondary market
- **Article 23 SNSO 2024**: not directly to property law but cross-border data + financial-disclosure environment tightened — relevant for ultra-luxe / corporate-buyer structuring
- **HKD-USD peg**: zero FX risk for USD asset holders; tail-risk for non-USD-denominated buyers
- **Mortgage stress test suspended Feb 2024**, but DSR 50% binding constraint
- **Property Tax 15% on rental** — paid to IRD by owner; NOT deductible for mortgage interest under straight Property Tax basis (use Personal Assessment election to deduct)

## Reddit / forum sources

- **r/HongKong** — general (mixed quality on property)
- **r/HKproperty** — focused; small but active
- **r/HongKongPropInvest** — investor-focused
- **AsiaXPAT Hong Kong forums** — `https://www.asiaxpat.com/`
- **GeoExpat Hong Kong** — `https://geoexpat.com/forum/` — buyer/lawyer/mortgage threads
- **Bowtie HK Insurance blog** — `https://www.bowtie.com.hk/blog/en/`
- **Habitat Property news** — `https://www.habitat-property.com/news/` (luxury/midmarket commentary)
- **CBRE HK Insights** — `https://www.cbre.com.hk/insights`
- **Spacious blog** — `https://www.spacious.hk/en/blog`

## Verification authorities

| Authority | When to call |
|---|---|
| **Land Registry (土地註冊處)** | IRIS title search; Memorial of Assignment registration |
| **Lands Department (地政總署)** | Crown Lease conditions, Government Rent, lease modification |
| **Rating and Valuation Department (RVD 差餉物業估價署)** | Rateable value, Rates + Government Rent calculation |
| **Buildings Department (BD 屋宇署)** | Occupation Permit, UBW register, MBIS notices, Order to Repair |
| **Inland Revenue Department (IRD 稅務局)** | AVD assessment, Property Tax, Profits Tax, BR |
| **Hong Kong Monetary Authority (HKMA)** | Mortgage LTV/DSR rules, banking sector |
| **Office of the Licensing Authority (HADLA)** | Cap. 349 hotel/guesthouse licensing |
| **Estate Agents Authority (EAA 地產代理監管局)** | Agent licensing, complaint procedure |
| **Law Society of Hong Kong** | Solicitor verification + complaint |
| **Owners' Corporation / Building Manager** | DMC, sinking fund, MBIS compliance |
| **Companies Registry** | Corporate ownership chain (if buyer / seller is company) |
| **Hospital Authority** | Healthcare access verification (cross-section to retirement) |
| **Immigration Department (ImmD)** | Visa eligibility, RoA application |

## Source URL templates

| Source | URL |
|---|---|
| The Land Registry IRIS | `https://www.iris.gov.hk/` |
| Lands Department | `https://www.landsd.gov.hk/` |
| Rating and Valuation Department | `https://www.rvd.gov.hk/` |
| Inland Revenue Department | `https://www.ird.gov.hk/` |
| HKMA | `https://www.hkma.gov.hk/` |
| Hong Kong Observatory | `https://www.hko.gov.hk/` |
| Buildings Department MBIS | `https://www.bd.gov.hk/en/safety-inspection/mbis/learn-more-about-MBIS/index.html` |
| GEO Slope Information System | `https://hkss.cedd.gov.hk/hkss/en/slope-safety-in-hong-kong/slope-safety-system/overview/index.html` |
| Drainage Services Department | `https://www.dsd.gov.hk/` |
| Water Supplies Department | `https://www.wsd.gov.hk/` |
| EPD strategic noise maps | `https://www.epd.gov.hk/epd/english/environmentinhk/noise/noise_maincontent.html` |
| Hong Kong Police Force crime statistics | `https://www.police.gov.hk/ppp_en/09_statistics/csc.html` |
| DATA.GOV.HK | `https://data.gov.hk/` |
| Centa-City Index | `https://hk.centanet.com/findproperty/en/centadata` |
| Hong Kong Property Review (RVD) | `https://www.rvd.gov.hk/en/publications/property_market_statistics.html` |
| Census & Statistics Department | `https://www.censtatd.gov.hk/` |
| Climate Action Plan 2050 (CNSD) | `https://cnsd.gov.hk/` |
| ImmD New CIES portal | `https://www.newcies.gov.hk/` |
| ImmD Top Talent Pass Scheme | `https://www.immd.gov.hk/eng/services/visas/TTPS.html` |
| Estate Agents Authority | `https://www.eaa.org.hk/` |
| Law Society of Hong Kong | `https://www.hklawsoc.org.hk/` |
| eLegislation (statutory text) | `https://www.elegislation.gov.hk/` |
| Hospital Authority | `https://www.ha.org.hk/` |
| HK 18 Districts (Home Affairs Dept) | `https://www.had.gov.hk/en/18_districts/my_map.htm` |
| Centaline / Centanet listings | `https://hk.centanet.com/home/index.aspx` |
| Midland Realty | `https://www.midland.com.hk/` |
| Squarefoot listings | `https://www.squarefoot.com.hk/` |
| 28Hse listings | `https://www.28hse.com/` |
| Spacious (English) | `https://www.spacious.hk/` |

## Status

**Confidence**: HIGH

**Last verified**: 2026-05-27 (HKMA foreign-reserve level and coverage multiple corrected 2026-09-18 per the HKMA press release of 7 May 2026)

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Locked-in via primary government sources: stamp-duty regime (IRD + 28 Feb 2024 government press release), HKMA LTV (Oct 2024 circular), Rates + Government Rent (RVD + Cap. 116 / Cap. 515), CIES rules (newcies.gov.hk), TTPS thresholds (ImmD), property crime (HKPF + Security Bureau), HKO climate projections, RVD HKPPI quarterly trend, Cap. 349 STR prohibition, Land Registry / IRIS fee schedule. **Re-verify each annual February budget speech** for Rates concession, any AVD adjustment, any CIES tweak, MIP threshold; **2047 lease question** materially resolved by 2024 Extension of Government Leases Bill (auto 50-yr, no premium) but individual lots' lease conditions vary — confirm via Lands Department lease search per parcel. **Watch list 2026**: any reintroduction of CGT (recurring budget topic; ruled out Feb 2025 but cyclical revisit); HKMA LTV further easing/tightening with property-cycle turn; SNSO downstream effects on cross-border buyer KYC; first-hand sales pipeline 2026–2030 (RVD HKPR2026 forecasts ~107k units) absorption test.

## Extension TODOs (deepen on first real run)

- [ ] Per-district HKPPI sub-index extraction tooling (RVD publishes by Class A–E saleable-area band)
- [ ] CCI-CL / CCI-Mass / CCI-Large Centa sub-index automation
- [ ] Lands Department lease-condition PDF scraper (per-lot lease term + government rent rate)
- [ ] DMC text extraction for hotel/guesthouse-prohibition clause detection (key for any STR strategy)
- [ ] MBIS notice register cross-reference (BD publishes building-by-building compliance)
- [ ] BEAM Plus certified-property database scrape ([HKGBC project list](https://www.hkgbc.org.hk/eng/beam-plus/beam-plus.jsp))
- [ ] Strategic Noise Map polygon overlay for elevated-road / rail noise contour
- [ ] CCFISD coastal-flood inundation polygon for sub-5m elevation flag automation
- [ ] HOS resale-restriction lookup automation (Form A vs Form B status)
- [ ] NT village house (丁屋) Small House Policy carve-out detector
