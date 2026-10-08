# United Arab Emirates 🇦🇪 — Property Due-Diligence Playbook

ISO2: `ae`. Status: ✅ Fully populated (researched 2026-04 / verified 2026-07-03 — Tier-A quarterly refresh).

> **Critical framing**: The UAE is a **foreign-buyer-restricted market**. Non-GCC nationals can only acquire **freehold** in **designated freehold / investment zones** that vary by emirate. Outside those zones the maximum interest is leasehold or 99-year usufruct (Sharjah). Always confirm zone status with the relevant cadastre (DLD / ADREC / Sharjah Real Estate Reg.) **before** signing any reservation form. Currency risk vs USD is structurally zero — AED is pegged at **3.6725 to the USD since 1997** (Central Bank of the UAE).

## Country profile

- **Postal code system**: Traditionally none. Modern parcel-level identifiers:
  - **Makani** (Dubai) — 10-digit unique address code maintained by Dubai Municipality (`https://www.dm.gov.ae/open-data2/open-data-for-makani`)
  - **Onwani** (Abu Dhabi) — physical street-naming + addressing system maintained by the Department of Municipalities and Transport
  - **Plot number + community** is the cadastral identifier on Title Deeds
- **Admin levels**: Federation of **7 emirates** → municipalities → communities (sub-divisions)
- **Currency**: AED (UAE Dirham). Pegged USD 1 = AED 3.6725 since 1997 (Central Bank of UAE)
- **Languages**: Arabic (official, all formal contracts and Title Deeds in Arabic — bilingual EN/AR is universal in property sector); English is the de-facto business language
- **Cadastre** (per emirate — there is **no federal cadastre**):
  - **Dubai**: Dubai Land Department (DLD) — `https://dubailand.gov.ae/` + Dubai REST app
  - **Abu Dhabi**: Abu Dhabi Real Estate Centre (ADREC, formerly DMT-DGE) — `https://adrec.gov.ae/`
  - **Sharjah**: Sharjah Real Estate Registration Department — `https://www.shjrerd.gov.ae/`
  - **Ras Al Khaimah**: RAK Municipality / RAK Department of Economic Development for property — `https://mun.rak.ae/`
  - **Ajman**: Ajman Municipality and Planning Department — `https://www.ajman.ae/en/servicecatalog/service_categories/municipality-planning-department`
  - **Fujairah / Umm Al Quwain**: Municipal offices
- **Identifier(s)**:
  - **Title Deed (Sanad Mulkiyya)** — issued by relevant emirate cadastre at completion / handover
  - **Oqood** (عقد) — interim registration certificate for off-plan sales (Dubai), recorded in DLD's Oqood system, replaced by Title Deed at handover
  - **Initial Sale Contract (ISC)** — equivalent to oqood in Abu Dhabi / other emirates
- **Recent reforms** (12-month watchlist):
  - **Abu Dhabi Law 13/2019** (effective 16 Apr 2019, amending Abu Dhabi Law 19/2005) — non-GCC freehold ownership in Abu Dhabi designated investment areas (NB: there is no Federal Decree-Law 21/2021 on this topic; the reform is an emirate-level Abu Dhabi law, not federal) (2026-05-27 verified, source Al Tamimi & Co + Library of Congress Global Legal Monitor)
  - **Dubai 2040 Urban Master Plan** (effective 2021–2040) — zoning + density evolution
  - **Golden Visa expansions** Oct 2022 + further easing 2024 (mortgage financing portion now counted)
  - **VAT** introduced 1 Jan 2018 at 5%; first-sale residential 0%-rated; subsequent residential exempt; commercial standard-rated
  - **Federal Corporate Tax** introduced for periods starting **1 June 2023** at 9% above AED 375k taxable profit. Personal income from real estate held in own name is **excluded** (CT applies only to business activity); juridical non-residents earning UAE immovable-property income create a nexus
  - **Dubai Smart Rental Index** revamped Jan 2025 — every residential building rated **1–5 stars** by AI (~60 criteria: condition, finishes, maintenance, amenities, FM quality, location); star rating influences allowed rent increases at renewal (NOT A/B/C/D) (2026-05-27 verified, source DLD Smart Rental Index portal + Driven Properties + Kaizen AMS)
  - **Dubai Tasreef stormwater plan** (AED ~30 bn / USD 8 bn) approved post-Apr 2024 floods; phased to 2033
  - **Dubai Law No. 2 of 2025** — DIFC Courts Enforcement Judge has jurisdiction over enforcement of DIFC-registered non-Muslim wills inside or outside the DIFC (Art. 31(5)); for assets outside the DIFC (e.g. DLD-registered property) execution still runs through the Dubai Courts Enforcement Judge (Art. 32), which the DIFC Courts Wills FAQ calls a standard formality (2025 law, source DIFC Courts)

---

## 🇦🇪 Foreign buyer eligibility (READ FIRST)

This section determines whether a transaction is even legally possible. Confirm zone status BEFORE assessing price.

### Dubai

**Designated Freehold Areas** (DLD-maintained list — areas where non-GCC may own freehold):
- Dubai Marina, Downtown Dubai, Palm Jumeirah, Business Bay, Jumeirah Lake Towers (JLT), Jumeirah Village Circle (JVC), Jumeirah Beach Residence (JBR), Arabian Ranches, Damac Hills, Dubai Hills Estate, Emirates Hills, Meydan, MBR City, The Greens / The Views, Dubai Sports City, Dubai Silicon Oasis, International City, Discovery Gardens, Al Furjan, Town Square, Tilal Al Ghaf, Bluewaters Island, City Walk, Dubai Creek Harbour, and ~30+ more zones.
- Authoritative list: DLD eServices portal → "Designated Areas" lookup or Dubai REST app.
- **Outside designated areas**: non-GCC may obtain **leasehold up to 99 years** in some non-freehold districts (less common for residential investment).
- **2025 freehold-zone expansion**: DLD amended Art. 3 of Regulation 3/2006 (announced Jan 2025) to let private plot owners in **Sheikh Zayed Road** (Trade Centre Roundabout → Water Canal, 128 plots) and **Al Jaddaf** (329 plots) convert leasehold → freehold, open to **all nationalities**. Conversion fee = **30% of DLD valuation** (on Gross Floor Area); common-area fees / service charges then set per RERA guidelines. Verify eligibility per-plot on Dubai REST. (2026-07-03 verified, source DLD news release + BSA Law for the instrument)

### Abu Dhabi

**Investment Zones for non-GCC freehold** (ADREC):
- **Saadiyat Island**, **Yas Island**, **Al Reem Island**, **Al Raha Beach**, **Al Reef**, **Masdar City**, **Hidd Al Saadiyat**, **Mohammed Bin Zayed City** (selected zones), **Lulu Island** (selected), **Jubail Island**, **Ghantoot**.
- **Abu Dhabi Law 13/2019** (amending Abu Dhabi Law 19/2005) grants non-GCC the right to **freehold land + buildings** within designated investment areas; prior to Apr 2019 non-GCC were limited to musataha / usufruct / 99-yr lease. (NB: prior playbook attribution to "Federal Decree-Law 21/2021" was incorrect — that federal decree exists but covers a different subject; the real-estate ownership extension is emirate-level only.) (2026-05-27 verified, source Al Tamimi + Addleshaw Goddard 2021)
- Verify zone via ADREC's **Tamleek** lookup.

### Sharjah

- **Non-GCC nationals** (incl. non-Arab): freehold available **in designated zones only** per **Sharjah Law 2/2022 + Executive Council Decision 30/2022** (Aljada, Maryam Island, Al Mamsha and other approved projects). Outside designated zones, 100-year usufruct (intifa') is the maximum interest, renewable. (2026-05-27 verified, source Afridi & Angell + Lexology)
- **Arab nationals** (non-GCC, but holding Arab country passport): freehold permitted in selected designated zones.
- **GCC nationals**: freehold across most of the emirate.
- **June 2025 update**: SRERD dropped the **residency-visa prerequisite** for non-UAE nationals purchasing in designated zones (procedural relaxation under Decision 30/2022 framework); underlying ownership statute itself dates to Sharjah Law 2/2022.

### Other Northern Emirates

- **RAK**: Freehold for non-GCC in **Al Marjan Island**, **Al Hamra Village**, **Mina Al Arab**, **Dafan Al Nakheel** (RAK Municipality / RAK Properties communities).
- **Ajman**: Freehold for non-GCC in selected developments — **Ajman Corniche Residences**, **Emirates City**, **Al Ameera Village**, etc.
- **Fujairah / UAQ**: Limited freehold — verify per development with the local Municipality.

### Golden Visa property route (federal — applies UAE-wide)

| Item | Threshold |
|---|---|
| **Long-term Golden Visa (10 yr)** | Property worth ≥ AED 2,000,000 (single or aggregate properties, your name) |
| **2-year Property Investor Visa** | **Sole owners**: no minimum property value (completed property + registered title deed); **joint owners**: ≥ AED 400,000 each (DLD reform 29 Apr 2026 — the prior AED 750k floor was **abolished**) (2026-05-27 verified, source VisaHQ + LuxHabitat Journal + DLD announcement 29 Apr 2026) |
| **Mortgage financing allowed** | Yes — bank financing up to 50% counts toward the AED 2 M threshold; equity portion must reach AED 2 M; bank NOC required (per ICP) |
| **Off-plan eligible** | Not stated on the GDRFA golden-residence page (route 'includes all types of properties'; no off-plan or escrow terms) — verify off-plan eligibility with DLD before relying |
| **Family inclusion** | Spouse + children (no age cap for unmarried daughters; sons up to 25); domestic workers covered |
| **Authority** | ICP (Federal Authority for Identity, Citizenship, Customs and Port Security) — `https://icp.gov.ae/` + GDRFA Dubai for Dubai applications |

**Retirement Visa (5 yr)** — age ≥ 55 + 15 years' work history:
- Property ≥ AED 1,000,000 + savings ≥ AED 1,000,000, **OR**
- Annual income ≥ AED 180,000 (federal floor; Dubai's "Retire in Dubai" accepts AED 15k/month).

### Compliance / AML

- Federal AML rules (UAE Anti-Money-Laundering and Counter-Terrorism Financing Law — Federal Decree-Law 20/2018) require **source-of-funds documentation** for every property transaction; DLD trustee offices enforce this at sale registration.
- Cash transactions > AED 55,000 trigger reporting under FATF-aligned thresholds (per Ministry of Economy Real Estate Regulator guidelines 2022+).

**Verification path**:
1. Confirm property is in a designated zone for your nationality (DLD/ADREC/SRERD lookup).
2. Pull the seller's current Title Deed extract (DLD trustee office) to verify ownership + encumbrances.
3. If off-plan → verify project on DLD project register + escrow account active.

---

## Section: `--price`

### Primary sources

- **DLD Open Data Portal** (Dubai): `https://dubailand.gov.ae/en/open-data/` — transaction-level sales data, downloadable
- **DLD Smart Rental Index** (rentals): `https://dubailand.gov.ae/en/eservices/rental-index/`
- **ADREC** open data: `https://adrec.gov.ae/`
- **Property Monitor** (consultancy aggregator using DLD data): `https://propertymonitor.com/`
- **Bayut Index**: `https://www.bayut.com/index/` — apartment + villa quarterly updates
- **Property Finder** market reports: `https://www.propertyfinder.ae/blog/`
- **REIDIN** Residential Market Sales Price Index: tracks Dubai monthly

### Listing platforms

- **Bayut**: `https://www.bayut.com/`
- **Property Finder**: `https://www.propertyfinder.ae/`
- **Dubizzle Property**: `https://www.dubizzle.com/property-for-sale/`
- **Houza**: `https://www.houza.com/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **Luxhabitat**, **LuxuryProperty.com** (high-end)

### Dubai citywide benchmarks (verified 2026-07-03)

- **Citywide weighted-avg residential (ready)**: **AED ~1,691 / sqft (~USD 460)** as of Q1 2026 — **+5.62% YoY** (ValuStrat Q1 2026, via Global Property Guide). Off-plan ran hotter: AED 2,030/sqft, +12.22% YoY. Growth has cooled sharply from the +19.8% YoY printed for Dec 2025 — note that figure was REIDIN/Property Monitor, a different index, so read the deceleration as directional (corroborated: REIDIN +10.79% YoY Feb 2026): the price *level* held while momentum normalised. (2026-07-03 verified) — cross-check current month on DLD Open Data / REIDIN.
- **Q1 2026 residential transaction value**: **AED ~137–143 bn (+19–22% YoY)** across ~45k residential deals (Property Monitor: AED 143.1 bn, +22.2% YoY, 44,743 units; REIDIN: AED 137.3 bn / 45,221 transactions, off-plan AED 103.4 bn of that). All-property incl. land/commercial ~AED 176.5 bn per DXBinteract (aggregator social post — verify on dxbinteract.com). (2026-07-03 verified — quarterly figure, re-pull each quarter.)
- **Villas outperformed apartments**: villas **+15.16%** vs apartments **+12.52%** YoY in REIDIN index (Dec 2025); the villa/apartment gap widened into 2026 as apartment momentum cooled faster (Property Monitor Q1 2026)

### Premium-zone benchmarks (Q4 2025 / latest cited)

| Zone | Type | AED/sqft (avg) | Notes |
|---|---|---:|---|
| **Dubai Marina** | apartment | ~AED 2,188 (range 1,800–2,900 by tier) | Bayut Index 2025 — verify current month |
| **Downtown Dubai** | apartment | ~AED 2,900 (recent transactions) | Burj Khalifa premium pulls avg up |
| **Business Bay** | apartment | ~AED 2,307 | Bayut Index 2025 |
| **Palm Jumeirah** | villa | ~AED 6,160 | Bayut Index — beachfront premium |
| **Palm Jumeirah** | apartment | ~AED 3,500–5,500 | Tier-dependent (Shoreline vs branded) |
| **Emirates Hills / Dubai Hills** | villa | ~AED 2,200–3,500 | High-end suburban |
| **JVC / Damac Hills 2** | apartment | ~AED 1,200–1,500 | Mid-market freehold |
| **International City / Dubai Silicon Oasis** | apartment | ~AED 700–1,000 | Entry-level freehold |

(Sources: Bayut Index `https://www.bayut.com/index/`, Property Monitor monthly reports — *2025 data; figures may have shifted; cross-check current month on DLD Open Data*)

### Abu Dhabi benchmarks

[ADREC (Abu Dhabi Real Estate Centre)](https://adrec.gov.ae/) is the primary regulator and publishes interactive dashboards at [adrec.gov.ae/en/property_and_index/adrec-dashboard](https://adrec.gov.ae/en/property_and_index/adrec-dashboard) (transaction volumes + price indices — interactive, no static export; manual dashboard visit required for definitive transactional values). Most reliable per-zone AED/sqft figures are aggregated by [Knight Frank H1 2025](https://www.knightfrank.ae/newsroom/article/2025/8/abu-dhabi-residential-market-review-h1-2025) and [Bayut FY 2025 / H1 2025 reports](https://www.bayut.com/mybayut/abu-dhabi-sales-market-report-2025/). ADREC's 2025 annual report (released 27 Feb 2026) confirms direction: **+19% apartments, +13% villas YoY 2024 → 2025**. Per [ADREC's H1 2025 Market Report](https://adrec.gov.ae/-/media/adrec/home/abu-dhabi-real-estate-market-report-2025-h1.pdf), H1 2025 residential unit sales hit a record **AED 25 Bn**, with ~82% of sales value concentrated in 8 key districts — Al Saadiyat Island led at ~33% of sales value (~AED 8.25B of the AED 25 Bn) and Yas Island ~15% (~AED 3.75B). (2025 data, source ADREC H1 2025 Market Report)

| Zone | Type | AED/sqft | Source · period | YoY |
|---|---|---:|---|---:|
| **Saadiyat Island** | villa (luxury slice — HIDD Al Saadiyat, Mamsha, beachfront) | ~AED 2,061 | Bayut FY 2025 report | +12.9% |
| **Saadiyat Island** | villa (whole-island incl. Reserve/Lagoons) | ~AED 1,631 | Bayut Index Apr 2026 | −6.0% |
| **Saadiyat Island** | apartment (luxury) | ~AED 2,932 | Bayut FY 2025 report | +27.0% |
| **Saadiyat Island** | apartment (whole-island) | ~AED 3,344 | Bayut Index Apr 2026 | +4.6% |
| **Yas Island** | villa | ~AED 1,528 | Bayut FY 2025 report | +10.9% |
| **Yas Island** | apartment | ~AED 1,818 | Bayut FY 2025 report | +24.3% |
| **Yas Island** | apartment (live index — branded/waterfront uplift) | ~AED 2,370 | Bayut Index Apr 2026 | +27.7% |
| **Al Reem Island** | apartment (mid-tier — Reem is overwhelmingly apartment stock) | ~AED 1,352 | Bayut FY 2025 report | +18.9% |
| **Al Reem Island** | apartment (live index) | ~AED 1,767 | Bayut Index Apr 2026 | +26.9% |
| **Abu Dhabi citywide** | apartment | ~AED 1,296 | Knight Frank Q2 2025 | +17.3% |
| **Abu Dhabi citywide** | villa | ~AED 1,103 | Knight Frank Q2 2025 | (+42.3% since Q1 2020) |
| **Abu Dhabi citywide** | blended (all stock, hedonic index) | ~AED 1,005 | ValuStrat Q3 2025 | +9.0% |

**Abu Dhabi citywide (Q1 2026, ValuStrat via Global Property Guide):** ready homes ~AED 1,507/sqft (~USD 410) — **+25.06% YoY**; off-plan ~AED 2,191/sqft (~USD 597), +17.99% YoY. AD momentum now outpaces Dubai. Pair with the Jun 2026 ADREC rent freeze (see `--rental`), which caps AD rental growth for any yield read-across. (2026-07-03 verified)

**Rental yields (Bayut FY 2025 — ROI on listed prices, gross):** Saadiyat villa 4.47% · Saadiyat apt 4.05% · Yas villa 5.43% · Yas apt 7.07% · Al Reem apt **7.49%** (the highest mid-tier yield in Abu Dhabi).

**Methodology notes:** (a) Knight Frank uses transaction-weighted close prices; ValuStrat uses a hedonic index across all stock — the AED 1,005 vs AED 1,296 citywide spread is methodology, not error. (b) Bayut "luxury segment" carves out the top tier; the live Bayut Index is the whole-zone median including mid-tier sub-communities — for Saadiyat this pulls villa median below the luxury slice (AED 1,631 vs AED 2,061). (c) ADREC per-zone AED/sqft is **not** exposed in static press releases. (d) Off-plan list price ≠ ready market — apply 5–15% off-plan-to-handover discount.

*— 2025–April 2026 data; rates/figures may have shifted; cross-check current month on Bayut Index, Knight Frank quarterly review, or the ADREC dashboard. (2026-05-27 verified, sources [Knight Frank H1 2025](https://www.knightfrank.ae/newsroom/article/2025/8/abu-dhabi-residential-market-review-h1-2025) + [Bayut FY 2025](https://www.bayut.com/mybayut/abu-dhabi-sales-market-report-2025/) + [ADREC 2025 annual report](https://www.zawya.com/en/press-release/research-and-studies/adrec-releases-abu-dhabi-real-estate-market-report-2025-n8imcrtw))*

### Compute

1. Listing AED/sqft = listing AED ÷ BUA sqft (BUA = Built-Up Area; some listings show sellable area instead of BUA — clarify which)
2. Cross-check with Bayut Index for the same community + property type
3. Cross-check with **DLD transaction history** for the same building (DLD Dubai REST app shows recent sold prices building-by-building)
4. **Trap**: Off-plan list price ≠ ready market — apply 5–15% off-plan-to-handover discount when comparing
5. **Trap**: Branded residences (Bulgari, Armani, Atlantis The Royal) carry 50–150% premiums vs peer non-branded — don't average them in
6. **Trap**: Service-charge-included vs net rent for rental yield calcs — verify

---

## Section: `--traffic`

### Primary sources

- **RTA Dubai** (Roads and Transport Authority): `https://www.rta.ae/` — open data portal `https://www.rta.ae/wps/portal/rta/ae/home/open-data`
- **Department of Municipalities and Transport — Abu Dhabi (DMT)**: `https://www.tamm.abudhabi/` (TAMM is the unified Abu Dhabi services platform; transport open data via DMT)
- **Federal Ministry of Energy and Infrastructure** (federal road network): `https://moei.gov.ae/`

### Coarse fallback

OSM `highway` class:
- motorway = Sheikh Zayed Road (E11), E311 Mohammed Bin Zayed Road, E611 Emirates Road
- trunk = major Dubai-Sharjah-Abu Dhabi arterials
- primary = intra-emirate boulevards
- residential = community internal roads

### Verdict bands (for UAE highway context)

- 🟢 < 5,000 v/d (community internal road)
- 🟡 5,000–25,000 v/d (urban arterial)
- 🟠 25,000–80,000 v/d (busy arterial / E-route side)
- 🔴 > 80,000 v/d (Sheikh Zayed Road, E311 mainlanes — chronic congestion)

### Notes

- Dubai-side Sheikh Zayed Road carries 200,000+ v/d at peak in central segments (RTA data). Adjacency = guaranteed noise + congestion.
- Salik (Dubai toll) gantries: presence near a property often signals a major arterial.
- Metro Red + Green lines (RTA) and forthcoming Blue Line (target opening 2029) materially affect catchment + price for stations within ~800 m.

---

## Section: `--tax`

### Annual property tax

**There is NO annual real-estate property tax in the UAE** — neither federal nor (for residential held in personal name) emirate-level.

What residents do pay annually:

| Item | Rate / amount | Authority |
|---|---|---|
| **Dubai Municipality Housing Fee** | **5% of annual rental value**, billed monthly via DEWA in 12 instalments | Dubai Municipality (collected via DEWA) |
| Owner-occupier housing fee equivalent (Dubai) | 5% of RERA-assessed average rental value of comparable property | Dubai Municipality |
| Abu Dhabi rental fee (tenants only, expats) | 3% of annual rent (added to Tawtheeq registration; municipal levy) | Abu Dhabi Municipality |
| **UAE nationals** | Exempt from housing fee on owner-occupied property | — |
| **Service charges** (HOA equivalent — mandatory) | **AED 3–70 / sqft / yr** depending on community/tier | DLD Mollak system regulates Dubai |
| **Chiller / district cooling** (often separate) | AED 10–18 / sqft / yr (residential, district cooling) OR AED 400–1,000 / month flat | Empower / Tabreed / Emicool (provider-dependent) |

(Sources: Dubai Municipality / DEWA; DLD Service Charge Index `https://dubailand.gov.ae/`; Empower / Tabreed tariffs)

### Service-charge tier reference (Dubai 2026)

| Tier | AED/sqft/yr | Examples |
|---|---:|---|
| **Entry** | 3–10 | International City, Discovery Gardens |
| **Mid** | 10–20 | JVC, JLT mid-tier, Dubai Hills mid |
| **Premium** | 20–35 | Marina, Downtown standard, Business Bay |
| **Luxury** | 35–55 | Palm Jumeirah Shoreline, Emirates Hills |
| **Ultra-luxury / branded** | 55–70+ | Bulgari Residences, Atlantis The Royal, One Za'abeel |

(Source: DLD Service Charge Index Dubai 2026 + LuxHabitat 2026 guide — verify current per Mollak per building)

### Transaction taxes (one-time at purchase)

| Item | Amount | Notes |
|---|---|---|
| **DLD Transfer Fee — Dubai** | **4% of purchase price** | Statutory split 2%+2% buyer/seller; market practice = buyer pays full 4% (verify in MOU) |
| **ADREC Transfer Fee — Abu Dhabi** | **2% of purchase price** | Lower than Dubai |
| **Sharjah / RAK / Ajman fees** | 2–4% (varies — confirm with local cadastre) | — |
| **DLD Title Deed issuance fee** | AED 580 (residential ready); AED 250 (off-plan oqood) | DLD fixed |
| **DLD Knowledge + Innovation fees** | AED 20 + 10 | DLD fixed |
| **Trustee office fee** (mandatory for secondary-market Dubai transfers) | AED 4,000 (price > AED 500k) / AED 2,000 (price < AED 500k) + 5% VAT | Per DLD trustee |
| **Mortgage registration** (if mortgaged) | **0.25% of mortgage amount + AED 290** | DLD |
| **Bank mortgage processing fee** | 0.5–1% of loan | Per bank |
| **Property valuation** (mortgaged) | AED 2,500–3,500 | Bank-appointed valuer |
| **Conveyancer / lawyer** (optional) | AED 5,000–15,000 typical | UAE has no notary system for property — DLD Trustee + lawyers handle conveyancing |
| **Real estate agent commission** | 2% of price + 5% VAT (typical Dubai) | Buyer-side or seller-side, negotiable |
| **VAT** | First sale of new residential **0%-rated**; subsequent residential **exempt**; commercial property **5%** standard-rated | Federal Tax Authority |

(Sources: DLD fees portal `https://dubailand.gov.ae/en/eservices/`; FTA VAT Public Clarification VATP002 on real estate)

### Federal Corporate Tax 2023+ — when it touches property

- **Personal income** from real estate (rentals, capital gains on sale) held in **own name** by a **natural person** is **OUT OF SCOPE** of CT — explicit FTA guidance.
- **Natural persons conducting business**: CT applies only if annual turnover > **AED 1 million** AND the activity qualifies as a business — pure passive rental income from properties held in own name is generally excluded.
- **Property held in a UAE company / juridical person**: 9% CT on profits above AED 375,000 threshold.
- **Non-resident juridical persons**: earning income from UAE immovable property creates a nexus → 9% CT applies (Cabinet Decision 56/2023).

(Source: FTA `https://tax.gov.ae/`, MoF Corporate Tax pages `https://mof.gov.ae/`)

### Inheritance

- **Non-Muslim expats**: since 2020 federal reforms + Dubai Law 2/2025, **DIFC Wills** and **ADGM Wills** allow English-law-style testamentary freedom over UAE assets — overrides Sharia default.
  - DIFC Will registration: **AED 10,000** single-will (Standard Will) — DIFC Courts Wills Service Centre.
  - ADGM Wills: equivalent framework in Abu Dhabi.
  - Dubai Law 2/2025 gives the DIFC Courts Enforcement Judge jurisdiction over DIFC-registered wills inside or outside the DIFC (Art. 31(5)); outside the DIFC the writ is executed via the Dubai Courts Enforcement Judge (Art. 32) — a standard formality per the DIFC Courts Wills FAQ, not a bypass (2025 law, source DIFC Courts).
- **Muslims**: Sharia inheritance applies as default; can be modified within Sharia limits (1/3 testamentary share max).
- **No federal inheritance tax** in either case.

### Future risk

- 5% VAT review periodically discussed (no concrete change as of 2026-05) — federal scope.
- Potential extension of corporate tax to passive real estate income for individuals above thresholds — speculative (no announcement).
- Dubai service charge cap discussion has surfaced periodically; no statutory cap yet.

---

## Section: `--rental`

### Long-term residential

- **Mandatory tenancy registration**:
  - **Dubai**: **Ejari** (RERA's tenancy registration system) — tenant or landlord registers contract; AED 220 typical fee. Required for DEWA connection, school enrolment, visa renewals.
  - **Abu Dhabi**: **Tawtheeq** — equivalent system run by DMT.
  - **Sharjah**: registered with the Sharjah Municipality Tenancy Contract section.
- **Rent increase cap (Dubai)** — RERA Smart Rental Index 2025 brackets:

| Current rent vs market index | Max increase allowed |
|---|---:|
| Within 10% of market | **0%** |
| 11–20% below | **5%** |
| 21–30% below | **10%** |
| 31–40% below | **15%** |
| > 40% below | **20%** |

- 2025 reform: **Smart Rental Index** assigns a **1–5 star rating** per residential building (DLD/RERA, Jan 2025) that feeds into the index value used for the Decree 43/2013 rent-increase brackets (DLD Smart Rental Index portal `https://dubailand.gov.ae/en/eservices/rental-index/`) (2026-05-27 verified).
- 90-day notice prior to renewal required for rent increases (**Dubai Law 26/2007 as amended by Law 33/2008** for renewal notice; rent-increase brackets per **Dubai Decree 43/2013** — Determining Rent Increase for Real Property). (Prior playbook reference to "Decree 26/2013" was incorrect — Decree 26/2013 established the Rental Disputes Settlement Centre, a different instrument.) (2026-05-27 verified, source Al Tamimi + DLP Dubai legislation portal)
- **Abu Dhabi rent freeze (Jun 2026)**: ADREC suspended all rent increases on renewals and new lettings (residential / commercial / industrial) **until further notice** — benchmark = rental rate in the property's last registered Tawtheeq contract; cap cut from 5% to 0% (2026 data, source ADREC press release 03 Jun 2026). Tamleek benchmark + ADGM carve-out per law-firm notes only (secondary) — verify at adrec.gov.ae. Model AD rental yields flat until lifted. (source ADREC press release 03 Jun 2026, adrec.gov.ae/en/news/press-release-26---rental-freeze-update — confirm current status on adrec.gov.ae)

### Short-term rentals (holiday homes)

- **Dubai**: **DET (Department of Economy and Tourism)** Holiday Home Permit — formerly called DTCM Holiday Home licence.
  - Property must be furnished + inspected; building NOC required (some OAs / towers prohibit short-let).
  - **Initial registration fee**: AED 1,520 (incl. AED 10 Knowledge + AED 10 Innovation); **Annual permit fee**: from AED 370 per unit (size-dependent for larger units) (2026-05-27 verified, source DET portal + Houst + KeyOne 2025/2026 schedules — prior AED 3,720 figure was stale).
  - **Tourism Dirham**: AED 10/bedroom/night (collected from guest, remitted to DET).
  - **Municipality fee**: 10% of booking revenue (separate from Tourism Dirham).
  - **Guest registration**: every guest must be registered on DTCM portal within 3 hours of check-in.
  - **VAT**: 5% applies to short-term rental revenue if total taxable supplies > AED 375k/yr (FTA mandatory registration threshold).
  - **Penalties**: AED 10,000–50,000+ for unlicensed operation; OTAs (Airbnb, Booking) audited by DET.
  - Owners may hold permits directly for up to **8 properties**; beyond that requires a licensed operator.
- **Abu Dhabi**: **DCT Abu Dhabi** Holiday Home licence (Department of Culture and Tourism).
- **Sharjah / RAK / Ajman**: per-emirate tourism authority; less-developed STR market outside RAK Marjan Island.

### Yield benchmarks (per listing platforms — verify per building)

| Zone | Long-let gross yield | Short-let gross yield (high season) |
|---|---:|---:|
| Dubai Marina apartments | ~6–8% | ~10–14% |
| Palm Jumeirah | ~5–7% | ~9–12% (premium) |
| JVC / Damac Hills 2 | ~7–9% | ~9–12% |
| Downtown | ~5–7% | ~10–13% |
| Saadiyat (Abu Dhabi) | ~5–7% | ~7–10% |

(Source: Bayut + Property Finder yield indices; verify current month — *yields gross of service charge, chiller, OA fees, vacancy*)

### Strategic notes

- **Service charge + chiller = 25–40% of gross yield** in many high-end towers — model NET yield, not gross
- **Building OA approval** for STR is the single biggest gate — confirm BEFORE buying if STR is the strategy
- **VAT on commercial leases (5%)** but residential is exempt
- **PIT = 0%** federally (no income tax) — but US/UK/EU tax residents will face their own home-country tax on UAE rental income (treaty network limited)

---

## Section: `--work=<profession>`

### Job platforms

- **Bayt.com** — `https://www.bayt.com/` (largest MENA job board)
- **GulfTalent** — `https://www.gulftalent.com/`
- **LinkedIn UAE** — extremely active, especially for white-collar / tech / finance
- **Naukrigulf** — `https://www.naukrigulf.com/` (strong for South Asian diaspora networks)
- **Indeed UAE**, **Monster Gulf**, **Dubizzle Jobs**

### Visa routes for working

| Visa | Eligibility | Authority |
|---|---|---|
| **Standard Work Permit** | Employment offer from UAE entity | MOHRE (Ministry of Human Resources & Emiratisation) |
| **Green Visa (5 yr)** | Skilled employee, freelancer, or self-employed (Bachelor's + AED 15k/month income, or relevant freelance permit) | ICP / GDRFA |
| **Golden Visa (10 yr)** | Property AED 2 M, OR investor/entrepreneur, OR specialised talent / scientist / doctor / outstanding student | ICP |
| **Freelance Permit** | Specific free zones (DMCC, TECOM, twofour54, Fujairah Creative City, etc.) | Per free zone authority |

### Free Zone vs Mainland

- **Mainland company** (DED licence) — can trade UAE-wide; historically required local 51% sponsor — **abolished for most activities since 1 June 2021** (Federal Decree-Law 26/2020); now 100% foreign ownership for ~1,000+ activities.
- **Free Zone company** — 100% foreign ownership, 0% personal income tax, easier setup, but limited mainland trade (must use mainland distributor or open mainland branch).
- 9% Corporate Tax applies to free zone entities EXCEPT "Qualifying Free Zone Persons" earning "Qualifying Income" (FTA Decision 100/2023) — narrow conditions.

### Catchment heuristics

- Within 30 min drive of Sheikh Zayed Road / Downtown / DIFC: full white-collar opportunity
- Sharjah residents commuting to Dubai: 60–90 min peak — common but tiring
- Abu Dhabi: separate labour market from Dubai (90 min between centres, light commute population)
- Northern Emirates (RAK / Fujairah): thin mainland labour markets; remote work + property as Golden Visa anchor more typical

### Income benchmarks

- Median expatriate professional salary 2025–2026: AED 15,000–35,000/month (white-collar mainland) — varies massively by sector
- Tech / finance / law senior roles in DIFC / ADGM: AED 40,000–120,000/month + bonuses
- Free zone freelancers: variable; common AED 8,000–25,000/month equivalent invoicing

(Sources: Bayt.com salary guides, GulfTalent annual reports — verify current year)

---

## Section: `--risks`

### Officially declared risks

| Risk | Severity (UAE-wide) | Authority |
|---|---|---|
| **Sandstorms** | Recurrent (esp. shamal winds Mar-Aug) | NCM (National Center of Meteorology) `https://www.ncm.gov.ae/` |
| **Extreme heat (TX > 45°C)** | Increasing — annual occurrence Jun-Sep | NCM + IPCC AR6 Persian Gulf projections |
| **Flash floods / drainage failure** | Documented Apr 2024 record event | Dubai Municipality + NCM |
| **Seismicity** | Generally low; northern emirates closer to active Iranian Zagros fault zone | NCESI (National Centre of Earthquake Studies and Information — under NCM) |
| **Coastal SLR exposure** | Long-term (decades) for low-lying reclaimed islands | NCCS not formally federal; IPCC AR6 + Climate Central |
| **Subsidence** | Some reclaimed/coastal areas anecdotal | No federal cadastre — confirm geotechnical with developer / consultant |

### April 2024 flood event — what changed

- **Apr 16, 2024**: 254 mm of rain in 48 hrs in parts of UAE — **heaviest rainfall in 75 years of records** (NCM); record loss-of-life event with at least 4 deaths in UAE + 19 in Oman.
- **Cause** (per Met Office + Newcastle U research, Nature 2025): mesoscale convective system; climate-change attribution increases likelihood ~10–40%.
- **Reform — Dubai "Tasreef" stormwater plan**: ~AED 30 bn (USD 8 bn), approved Jun 2024 by Sheikh Mohammed bin Rashid; phased to **2033**.
- **Neighbourhood project (not emirate-wide)**: AED 277 m sewerage + rainwater drainage network in Nad Al Sheba 3 completed Jun 2025 (2025 data, source Dubai Media Office) — 24 km sewerage + 31 km gravity rainwater network; Dubai Municipality frames it within the Tasreef and sewerage programmes.
- **Implication for buyers**: low-lying communities (some Mirdif, Al Quoz, Sharjah border areas, IMPZ) experienced multi-day water-logging — verify drainage history with OA + developer.

### Build-quality / fire risk

- **Cladding fires** historical: Marina Torch (2015), Address Downtown (2015), Sulafa Tower (2016), 23 Marina (2017) — non-compliant ACP cladding.
- **UAE Fire & Life Safety Code 2017** (UAE Civil Defence) tightened cladding rules; **2018 update** mandated retrofits for non-compliant towers (multiple emirates).
- Verify cladding certification + fire NOC (Civil Defence) for towers built 2000–2017.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-2000** | Older Sharjah / Dubai Bur Dubai stock — variable quality, occasional asbestos roofing |
| **2000–2008 boom** | Rapid construction phase — uneven quality, cladding risk (see above) |
| **2008–2014 GFC stalled** | Many off-plan projects cancelled or delayed years; verify Title Deed transferred + project completed |
| **2014–2020** | Modernised codes; better quality |
| **Post-2020** | UAE Sustainable Building Code + tightened fire/structural standards |

### Climate to 2050 (IPCC AR6 Persian Gulf)

- +1.5–3.0 °C by 2050 vs 1981–2010 baseline (SSP scenarios)
- Wet-bulb temperatures projected to approach **35°C survivability threshold** in Persian Gulf summers by 2070+ under high-emissions scenarios (Pal & Eltahir 2015 + IPCC AR6 AR6 WG1)
- More extreme rain events (April 2024 type) — drainage capacity planning is now policy priority
- Sea-level rise: ~30 cm by 2050 (median) → exposure for Palm Jumeirah outer fronds, Yas low-lying, Saadiyat coastal villas — verify elevation vs SLR projection at parcel level

### Mandatory diagnostics at sale

| Document | Required because | Issuing authority |
|---|---|---|
| **Title Deed (current)** | Verify owner + encumbrances | DLD / ADREC / etc. |
| **Mortgage Discharge Letter** (if mortgaged) | Bank confirms loan paid off | Lending bank |
| **NOC from Developer / OA** | Confirms service charges paid up + permits transfer | Master developer / OA |
| **Service charge clearance certificate (Mollak)** | Dubai — confirms no outstanding fees | Mollak via OA |
| **Affection Plan** | Cadastral plot info | Dubai Municipality / equivalent |
| **Building Completion Certificate** (off-plan completion) | Project legally complete | Master developer |
| **Fire NOC / Civil Defence certificate** | Cladding + fire compliance | Dubai Civil Defence / MoI General Command of Civil Defence |
| **DEWA / ADDC clearance** | No outstanding utility bills | DEWA / ADDC |

(Note: The UAE has no mandatory energy performance certificate equivalent for resale yet; sustainability ratings exist for new builds (DM Green Building, Estidama Pearl) but are not retroactive.)

### Risk dashboard (UAE 2026)

| Class | Severity | Action priority |
|---|---|---|
| **Heat stress + cooling cost** | 🟠 increasing | Verify chiller economics; assume worsening to 2050 |
| **Cladding (towers 2000–2017)** | 🟠 era-dependent | Demand Civil Defence NOC + certification |
| **Flash flood (low-lying communities)** | 🟡 → 🟠 post-2024 | Check drainage history + Tasreef coverage |
| **Off-plan completion risk** | 🟠 always | Verify RERA project status + escrow + developer track record |
| **Service charge inflation** | 🟡 | Pull 5-year history + check Mollak |
| **Cyclone / coastal storm** | 🟢 (low frequency, increasing concern long-term) | — |
| **Earthquake** | 🟢 most of UAE; 🟡 in northern emirates near Zagros | Standard structural review |

---

## Section: `--mains`

### Universal in serviced areas

UAE urban property is essentially **always on mains** for water + electricity + sewer + cooling — the question is which provider and how the bills are structured.

| Emirate | Provider |
|---|---|
| **Dubai** | **DEWA** (Dubai Electricity & Water Authority) `https://www.dewa.gov.ae/` |
| **Abu Dhabi** | **ADDC** (Abu Dhabi Distribution Company) `https://www.addc.ae/` |
| **Al Ain** | **AADC** (Al Ain Distribution Company) |
| **Sharjah** | **SEWA** (Sharjah Electricity, Water & Gas Authority) `https://www.sewa.gov.ae/` |
| **Northern Emirates** (Ajman, RAK, UAQ, Fujairah) | **EtihadWE** (Etihad Water and Electricity — established 2020 by Federal Law No. 31 of 2020, replacing FEWA) `https://etihadwe.ae/en/Pages/default.aspx` |
| **District cooling** | **Empower** (Dubai dominant), **Tabreed** (UAE-wide), **Emicool** (Dubai) — separate bill |

### Verification

1. Pull existing **DEWA / ADDC / SEWA / EtihadWE** account info from seller — confirms active mains + no overdue
2. Off-plan: confirm developer has utility connection on the master plan (verify NOC at handover)
3. Some compounds use **TSE (treated sewage effluent)** for landscape irrigation — separate cost line
4. Rural / undeveloped Northern Emirates plots: may not yet have utility connection; verify with EtihadWE + master developer

### Tariffs (residential indicative)

- **DEWA**: tiered; first 2,000 kWh/month at AED 0.23/kWh; > 6,000 kWh at AED 0.38/kWh + fuel surcharge (~5–7 fils/kWh) — verify current rate at `https://www.dewa.gov.ae/`
- **District cooling** (Empower / Tabreed): split into **capacity charge** (fixed, based on contracted RT) + **consumption charge** — typical residential AED 10–18/sqft/year all-in
- **Housing fee (Dubai)**: 5% of annual rent or RERA rental-equivalent value, billed via DEWA monthly

### Costs

| Scenario | Cost |
|---|---:|
| Connection (already serviced area) | AED 1,000–3,000 (deposit + activation) |
| Off-plan handover utility activation | Often included; verify with developer |
| Chiller "freeze" between tenants (capacity charge continues) | AED 400–1,500/month |
| Disconnection / clearance certificate | AED 100–300 |

---

## Cost benchmarks (UAE 2026)

| Item | Cost |
|---|---:|
| **DLD transfer fee (Dubai)** | **4% of price** |
| **ADREC transfer fee (Abu Dhabi)** | **2% of price** |
| **Title Deed issuance** | AED 580 |
| **Trustee office fee** | AED 4,000 (price > AED 500k) + 5% VAT |
| **Mortgage registration (DLD)** | 0.25% of mortgage + AED 290 |
| **Bank mortgage processing** | 0.5–1% of loan |
| **Property valuation (mortgage)** | AED 2,500–3,500 |
| **Real estate agent commission** | 2% + 5% VAT (typical) |
| **Conveyancer / lawyer** (optional) | AED 5,000–15,000 |
| **DIFC Will registration** (single) | AED 10,000 |
| **Holiday Home Permit (DET)** | initial registration AED 1,520; annual permit from ~AED 370/unit |
| **Service charges (annual)** | AED 3–70 / sqft / yr (tier-dependent) |
| **District cooling (annual)** | AED 10–18 / sqft / yr (residential) |
| **Annual housing fee (Dubai)** | 5% of annual rental value (via DEWA) |
| **Annual property tax** | **None** |
| **Total transaction cost (buyer side, Dubai cash secondary)** | **~6–8% of price** (4% DLD + ~2% agent + trustee + AED 1k DLD admin + lawyer) |
| **Total transaction cost (Dubai with mortgage)** | ~8–10% of price |

## Active fiscal incentives (2026)

- **Golden Visa (10-year)**: property ≥ AED 2 M (single or aggregate)
- **Investor Visa (2-year)**: sole owners — no minimum property value; joint owners — ≥ AED 400,000 each (prior AED 750k floor abolished, DLD 29 Apr 2026)
- **Retirement Visa (5-year, age ≥ 55)**: property ≥ AED 1 M + savings AED 1 M, OR AED 180k/yr income
- **Green Visa (5-year)**: skilled workers / freelancers
- **0% personal income tax** on rental income (federal — but check home-country tax residency obligations)
- **0% VAT first sale of new residential**; subsequent residential exempt
- **0% capital gains tax** on individual property sales (not within scope of CT for natural persons)
- **Free Zone "Qualifying Income"** 0% CT (narrow conditions)

## Common listing platforms

- **Bayut** (largest by listings) — `https://www.bayut.com/`
- **Property Finder** (UAE-wide, strong analytics) — `https://www.propertyfinder.ae/`
- **Dubizzle Property** — `https://www.dubizzle.com/property-for-sale/`
- **Houza** — `https://www.houza.com/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **LuxHabitat** + **LuxuryProperty.com** + **Sotheby's UAE** (high-end)
- **JustProperty.com** (Sharjah / Northern Emirates strong)
- Developer direct portals (Emaar, Damac, Aldar, Nakheel, Sobha) for off-plan

## Caveats unique to UAE

- **Freehold-zone-only restriction crucial** — non-GCC outside designated freehold zones cannot acquire freehold title; verify zone status before any reservation
- **Off-plan completion risk** — RERA escrow + Project Status register protects buyer funds, but **delays of 12–36+ months** are common; verify developer track record (Emaar / Aldar / Nakheel / Damac historically reliable; smaller developers higher variance)
- **Service charges + chiller can be 25–40% of gross rental yield** in high-end towers — model NET, never gross
- **Building OA short-term-rental policy is the single biggest STR gate** — verify BEFORE buying if STR is the strategy
- **No income tax personally; 9% corporate tax from Jun 2023** for property held in a juridical person above AED 375k profit
- **DIFC / ADGM Wills are critical for non-Muslim foreign owners** — without one, Sharia inheritance rules apply by default to your UAE assets
- **Apr 2024 floods exposed drainage limits** — verify drainage history of low-lying communities; Tasreef plan phased to 2033
- **Cladding (towers 2000–2017)**: demand Civil Defence Fire NOC; multiple historical cladding fires
- **Federal AML rules require source-of-funds documentation** — bank statements, employment records, prior asset sale proof; cash transactions > AED 55k trigger reporting
- **Currency**: AED pegged to USD at 3.6725 — **no FX risk vs USD**; meaningful FX risk vs EUR / GBP / other floating currencies
- **No federal cadastre** — each emirate has its own register; cross-emirate portfolio requires multi-cadastre lookup
- **VAT 5% on commercial property** (and STR if turnover > AED 375k/yr) — easy to forget for foreign investors

## Reddit / forum sources

- **r/dubai** (largest active expat community)
- **r/UAE**
- **r/ADXfinance** (Abu Dhabi finance/investment)
- **Bayut Blog** (`https://www.bayut.com/mybayut/`) — community-style guides
- **ExpatWoman.com** forums — practical expat property + service-charge discussions
- **Dubizzle community pages**

## Verification authorities

| Authority | When to call |
|---|---|
| **Dubai Land Department (DLD)** | Title Deed verification; designated freehold zone confirmation; transfer registration |
| **DLD Trustee Offices** (RERA-licensed) | Mandatory venue for Dubai secondary-market transfers |
| **RERA** (under DLD) | Off-plan project status, escrow status, broker licence verification |
| **ADREC** | Abu Dhabi cadastre + Tamleek zone confirmation |
| **Sharjah Real Estate Registration Department** | Sharjah cadastre |
| **ICP** (Federal Authority for Identity, Citizenship, Customs and Port Security) | Golden Visa, Green Visa, Retirement Visa applications |
| **GDRFA Dubai** | Dubai-specific residency processing |
| **Federal Tax Authority (FTA)** | VAT clarifications, Corporate Tax registration |
| **MOEC** (Ministry of Economy — Real Estate Regulator) | Federal-level consumer protection in real estate, AML enforcement |
| **Dubai Police** | Off-plan / real estate fraud reports |
| **DIFC Wills Service Centre** | Non-Muslim wills (Dubai/UAE assets) |
| **ADGM Wills Service** | Non-Muslim wills (Abu Dhabi-anchored) |
| **Dubai Civil Defence / MoI General Command of Civil Defence** | Fire NOC, cladding compliance |
| **Dubai Municipality** | Makani address, building permits, drainage history |

## Quirks to know

- **Makani number** (Dubai) — 10-digit address code; required for utility setup, deliveries, emergency response
- **Title Deed (Sanad Mulkiyya)** issued in Arabic — bilingual EN/AR is standard but the Arabic prevails legally
- **Oqood** (off-plan) ≠ Title Deed — only the Title Deed at handover gives full ownership rights
- **Initial Sale Contract / SPA** — pre-handover binding agreement
- **Post-handover payment plans** common for off-plan (e.g., 50/50, 60/40, 80/20 over 2–5 years post-handover) — model the IRR carefully; effectively developer financing
- **Secondary-market freehold transfers** in Dubai must be done at a **DLD-registered Trustee Office** (not lawyer-only)
- **Mollak system** — DLD's centralised service-charge regulation portal (since 2018); each tower has a registered annual budget
- **Service-charge "owner committee"** — buyers should attend AGMs to influence budgets
- **Cooling provider lock-in** — district cooling contracts are often 25–30 years between developer and provider; tenants/owners cannot switch
- **Off-plan handover defects** — most contracts give 1-year defects liability period (developer warranty) + 10-year structural warranty (federal)
- **Courts**: civil disputes over property typically heard in **Rental Disputes Centre** (Dubai) for tenancy matters; Real Estate Court for ownership; DIFC Courts for opt-in English-law contracts; Dubai Courts for default

## Source URL templates

| Source | URL |
|---|---|
| DLD home | `https://dubailand.gov.ae/en/` |
| DLD eServices (transfer / oqood / etc.) | `https://dubailand.gov.ae/en/eservices/` |
| DLD Smart Rental Index | `https://dubailand.gov.ae/en/eservices/rental-index/` |
| DLD Open Data | `https://dubailand.gov.ae/en/open-data/` |
| Dubai REST app (mobile) | `https://dubailand.gov.ae/en/eservices/dubai-rest/` |
| ADREC | `https://adrec.gov.ae/` |
| Sharjah Real Estate Registration | `https://www.shjrerd.gov.ae/` |
| ICP (Federal — visas) | `https://icp.gov.ae/` |
| GDRFA Dubai | `https://www.gdrfad.gov.ae/` |
| Federal Tax Authority | `https://tax.gov.ae/` |
| Ministry of Finance (Corporate Tax) | `https://mof.gov.ae/` |
| MOEC (consumer protection / real estate regulator) | `https://www.moec.gov.ae/` |
| NCM (weather / climate) | `https://www.ncm.gov.ae/` |
| DEWA | `https://www.dewa.gov.ae/` |
| ADDC | `https://www.addc.ae/` |
| SEWA | `https://www.sewa.gov.ae/` |
| EtihadWE (formerly FEWA) | `https://etihadwe.ae/en/Pages/default.aspx` |
| Dubai Municipality | `https://www.dm.gov.ae/` |
| Makani (Dubai address) | `https://www.dm.gov.ae/open-data2/open-data-for-makani` |
| TAMM (Abu Dhabi unified services) | `https://www.tamm.abudhabi/` |
| RTA Dubai | `https://www.rta.ae/` |
| Dubai Civil Defence (emirate-level; UAE federal body is the MoI General Command of Civil Defence) | `https://www.dcd.gov.ae/` ⚠️ reachable from the UAE only |
| DIFC Courts Wills Service | `https://www.difccourts.ae/difc-courts-wills/` |
| ADGM | `https://www.adgm.com/` |
| DET (holiday home permits, Dubai) | `https://www.dubaidet.gov.ae/` |
| Bayut Index | `https://www.bayut.com/index/` |
| Property Finder | `https://www.propertyfinder.ae/` |
| Property Monitor | `https://propertymonitor.com/` |

## Status

✅ **Fully populated** (initially populated 2026-05-01).

**Coverage check**: foreign-buyer eligibility, price, traffic, tax, rental, work, risks, mains all have primary government / regulated entity sources + cost benchmarks + caveats; Golden Visa + Retirement Visa thresholds verified vs ICP guidance; DLD fees verified vs DLD eServices.

**Confidence**: **HIGH** for federal-level rules (Golden Visa / Retirement Visa thresholds, VAT regime, Corporate Tax, AED peg, AML), Dubai DLD transfer fee + service-charge framework + Smart Rental Index brackets + DET holiday-home permit, ADREC 2% + Abu Dhabi Law 13/2019 (amending Law 19/2005) framework, DIFC/ADGM Wills + Dubai Law 2/2025, Apr 2024 flood event + Tasreef response. **MEDIUM** for emirate-by-emirate detail outside Dubai/Abu Dhabi (RAK/Ajman/Fujairah/UAQ less standardised — designated zones verified per source but precise transfer fee schedules vary and need per-deal confirmation with the relevant municipality), Abu Dhabi citywide pricing benchmarks (less granular open data than Dubai), Sharjah usufruct vs freehold-for-Arabs distinction (verify with SRERD per nationality).

**Last verified**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; Northern Emirates utility (EtihadWE) corrected 2026-09-18 per u.ae). Connectivity / finance / rental / risks / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).

## Extension TODOs (deepen on first real run)

- [ ] Per-emirate transfer fee + trustee fee schedule (Northern Emirates beyond Dubai/AD)
- [ ] Abu Dhabi citywide AED/sqft per-zone benchmarks comparable to Dubai's Bayut Index granularity
- [ ] Mollak per-building service-charge history extraction workflow
- [ ] DET Holiday Home Permit per-building NOC compatibility list (which towers permit STR)
- [ ] Tasreef rollout schedule per community (which neighbourhoods upgrade first 2025–2033)
- [ ] Cladding compliance lookup for towers built 2000–2017 (Civil Defence database)
- [ ] Free Zone vs mainland Corporate Tax decision tree for property-holding SPVs
- [ ] Sharjah / RAK / Ajman per-development freehold zone master list
- [ ] Branded residence premium calibration (Bulgari / Armani / Atlantis / etc.) per sqft
- [ ] DIFC vs ADGM Will choice decision tree for foreign owners
