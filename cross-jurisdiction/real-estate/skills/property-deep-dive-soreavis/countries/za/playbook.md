# South Africa 🇿🇦 — Property Due-Diligence Playbook

ISO2: `za`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode**: 4 digits (e.g., `8001` Cape Town CBD, `2196` Sandton, `2193` Rosebank, `4001` Durban CBD, `0002` Pretoria CBD)
  - First digit: rough provincial cluster (0xxx Gauteng/Limpopo, 1xxx North-West, 2xxx Gauteng/NW, 3xxx KZN, 4xxx KZN, 5xxx Eastern Cape, 6xxx Eastern Cape/W. Cape inland, 7xxx Western Cape, 8xxx Western Cape coastal, 9xxx Free State/Northern Cape)
- **Admin levels**: 9 provinces → 8 metropolitan munis (Cape Town, Johannesburg, Ekurhuleni, Tshwane, eThekwini, Nelson Mandela Bay, Buffalo City, Mangaung) + 44 district + 205 local munis (per CoGTA / Municipal Demarcation Board)
- **Currency**: ZAR (South African Rand); volatile vs USD/EUR (1 USD ≈ R18–R19 typical 2025; 1 EUR ≈ R20 — verify on day of conversion)
- **Languages**: 11 official (English, Afrikaans, isiZulu, isiXhosa, Sesotho, Sepedi, Setswana, Xitsonga, siSwati, Tshivenda, isiNdebele); **English dominates commerce, contracts, and conveyancing**
- **Cadastre**: **Deeds Registry** (Deeds Office, one per major city — Cape Town, Pretoria, Johannesburg, Pietermaritzburg, Bloemfontein, Kimberley, King William's Town, Mthatha, Vryburg, Nelspruit, Polokwane) + **Surveyor-General** (per province) for diagrams
  - Deeds Registration portal: `https://www.deeds.gov.za/` (an entity of the Department of Land Reform and Rural Development, `https://www.dlrrd.gov.za/`)
  - DeedsWeb (subscription): `https://www.deeds.gov.za/`
- **Identifier**: **Title Deed number** (e.g., `T12345/2020`) + **Surveyor-General (SG) diagram** + **Erf/Stand/Portion number** (residential) or **Sectional Title** scheme + unit number for apartments
- **Recent reforms**:
  - **Expropriation Act 13 of 2024** (assented **20 Dec 2024**, published in *Government Gazette* No. 51964 on 24 Jan 2025) — replaces 1975 Act; introduces "expropriation without compensation" in narrow listed circumstances, but is **NOT in force as at 2026-09-24**: s31 requires a presidential proclamation and gov.za records commencement as "To be proclaimed"; **constitutional challenges pending** — the consolidated DA / AfriForum / IRR Legal / Vaderland Stigting review opened in the **Western Cape High Court** on 3 Aug 2026 and was **postponed part-heard** on 7 Aug 2026 (three respondents + three amici and the applicants' replies outstanding, per applicant AfriForum's 7 Aug 2026 statement); no resumption date published in the sources read, so argument has not concluded
  - **Property Practitioners Act 22 of 2019** (in force Feb 2022) — replaced Estate Agency Affairs Act; created PPRA (Property Practitioners Regulatory Authority)
  - **Sectional Titles Schemes Management Act 8 of 2011** + **Community Schemes Ombud Service Act 9 of 2011** — body corporate governance + CSOS dispute forum
  - **Spatial Planning and Land Use Management Act 16 of 2013 (SPLUMA)** — municipal planning framework
  - **FICA (Financial Intelligence Centre Act 38 of 2001)** — AML; conveyancers must verify source of funds

## Section: `--price`

### Primary sources

- **SARB Quarterly Bulletin** (residential property price index): `https://www.resbank.co.za/en/home/publications/quarterly-bulletin1`
- **FNB House Price Index** (monthly, free release): `https://www.fnb.co.za/economics-commentary/property-barometer.html`
- **Lightstone Property** (paid pro tier; deeds-based actual sales): `https://www.lightstoneproperty.co.za/`
- **PayProp Rental Index** (quarterly, free PDF): `https://www.payprop.co.za/rental-index`
- **Stats SA Residential Property Price Index** (RPPI): `https://www.statssa.gov.za/?page_id=1854&PPN=P0151` (release lag 6–9 months — verify latest)
- **Deeds Office** (paid per-search; sole authoritative record of sale price): walk-in or via conveyancer

### Listing platforms

- **Property24** — largest portal: `https://www.property24.com/`
- **Private Property** — second-largest: `https://www.privateproperty.co.za/`
- **Pam Golding** — premium agency: `https://www.pamgolding.co.za/`
- **Seeff** — national agency: `https://www.seeff.com/`
- **Lew Geffen Sotheby's International Realty** — luxury: `https://www.sothebysrealty.co.za/`
- **Remax SA** — `https://www.remax.co.za/`
- **Gumtree Property** — classifieds, more downmarket: `https://www.gumtree.co.za/s-property-for-sale/v1c8398p1`

### Price benchmarks (R/m², 2025 data — rates may have changed since)

Listing-derived ranges, cross-checked against FNB HPI (Q4 2024 / Q1 2025 releases). **Listing-trust caveat**: asking ≠ realised; Deeds Office search per erf gives true sale.

| Location | Listing R/m² (premium) | Source basis |
|---|---:|---|
| Clifton / Bantry Bay / Camps Bay (Atlantic Seaboard, Cape Town) | R60,000–R150,000+ | Property24 + Pam Golding listings, Q1 2025 |
| Sea Point / Green Point | R40,000–R80,000 | Property24 listings, Q1 2025 |
| Cape Town CBD / De Waterkant | R35,000–R60,000 | Property24 listings, Q1 2025 |
| Constantia / Bishopscourt (Southern Suburbs) | R30,000–R70,000 | Pam Golding, Q1 2025 |
| Stellenbosch town | R25,000–R55,000 | Property24, Q1 2025 |
| Sandton / Bryanston / Hyde Park (JHB) | R20,000–R60,000 | Property24, Q1 2025 |
| Houghton / Rosebank / Melrose (JHB) | R18,000–R45,000 | Property24, Q1 2025 |
| Johannesburg CBD / Maboneng | R8,000–R18,000 | Property24, Q1 2025 |
| Umhlanga / Ballito (KZN coastal) | R20,000–R45,000 | Property24, Q1 2025 |
| Durban North / Berea | R12,000–R25,000 | Property24, Q1 2025 |
| Durban CBD | R6,000–R14,000 | Property24, Q1 2025 |
| Pretoria East / Waterkloof / Brooklyn | R12,000–R28,000 | Property24, Q1 2025 |

### Compute

1. Listing R/m² = listing price / advertised m² (clarify: floor area vs erf size — listings often quote both; **erf = land plot, floor area = built**)
2. Cross-check FNB HPI YoY for the metro (FNB releases monthly area indices)
3. For accurate transacted price: paid Lightstone or Deeds Office search per erf
4. **Trap**: sectional title listings sometimes exclude "exclusive use areas" (parking, garden) from the section's m² — verify against sectional title plan
5. **Trap**: foreigners purchasing for speculative letting now sometimes face seller "non-resident pricing premium" — anecdotal

---

## Section: `--traffic`

### Primary sources

- **SANRAL** (South African National Roads Agency Ltd) — national routes (N-routes, R-routes managed nationally): `https://www.nra.co.za/` (open-data traffic counts limited; ITS sites publish monthly)
- **Provincial DOTs** — regional roads:
  - Western Cape: `https://www.westerncape.gov.za/mobility`
  - Gauteng: `https://www.gauteng.gov.za/`
  - KZN: `https://www.kzntransport.gov.za/`
- **Municipal traffic depts** for urban: City of Cape Town TDA (Transport Directorate); City of Johannesburg JRA (Johannesburg Roads Agency); eThekwini ETA
- **OSM fallback**: `highway` tag for class (motorway, trunk, primary, secondary, tertiary, residential)

### Coarse fallback (OSM `highway`)

- `motorway` = N-route (e.g., N1, N2, N3) — 30,000–150,000 vehicles/day typical
- `trunk` = major R-route (R21, R24) — 15,000–50,000 v/d
- `primary` = secondary R-route — 5,000–20,000 v/d
- `secondary` = arterial suburban — 2,000–10,000 v/d
- `tertiary` = local connector — 500–3,000 v/d
- `residential` = quiet street — < 500 v/d

### Verdict bands

- 🟢 < 1,000 v/d (suburban residential)
- 🟡 1,000–5,000 v/d (urban side street, suburban arterial)
- 🟠 5,000–20,000 v/d (busy R-route, urban main road)
- 🔴 > 20,000 v/d (N-route, major urban arterial)

**Caveat**: SANRAL parcel-level AADT not in a single open dataset; for premium/decision-grade, request from provincial DOT directly. OSM class is reliable for tier; absolute volumes are estimates.

---

## Section: `--tax`

### Transfer Duty (one-time, buyer pays) — SARS Schedule 8

**Source**: SARS Transfer Duty: `https://www.sars.gov.za/types-of-tax/transfer-duty/` — verify current brackets at filing.

**2025/26 tax year brackets** (effective **1 April 2025**, per SARS — 2026-05-27 verified, source: SARS Latest News "New Transfer Duty rates effective 1 April 2025"):

| Property value (ZAR) | Rate |
|---|---|
| R0 – R1,210,000 | **0 %** |
| R1,210,001 – R1,663,800 | 3 % of value above R1,210,000 |
| R1,663,801 – R2,329,300 | R13,614 + 6 % above R1,663,800 |
| R2,329,301 – R2,994,800 | R53,544 + 8 % above R2,329,300 |
| R2,994,801 – R13,310,000 | R106,784 + 11 % above R2,994,800 |
| R13,310,001 + | R1,241,456 + 13 % above R13,310,000 |

(Source: SARS Transfer Duty 2025/26 Budget — verify at https://www.sars.gov.za/types-of-tax/transfer-duty/)

### VAT 15 %

- If seller is a **VAT vendor** (e.g., developer of new property), price is **VAT-inclusive at 15 %**, AND **no Transfer Duty** is payable (one or the other, not both)
- If seller is private (most resales), Transfer Duty applies, no VAT
- **2025 Budget proposed VAT rise 15 % → 15.5 % from 1 May 2025; withdrawn 24 Apr 2025**, VAT remained at 15 %. Contracts signed Mar–Apr 2025 with VAT rate-change clauses should be reviewed (2026-05-27 verified, source: National Treasury Media Statement 24 Apr 2025).

### Municipal Rates (annual, owner pays) — per municipality, set by tariff resolution each July

**Source**: each municipality publishes annual Tariffs document. Verify on city's official site each year.

| Municipality | Residential rate (cents/Rand of valuation) | Source |
|---|---:|---|
| **City of Cape Town** | ~0.6055 c/R (2024/25) | `https://www.capetown.gov.za/Family%20and%20home/Residential-utility-services/Residential-property-rates-and-valuations` |
| **City of Johannesburg** | ~0.7 c/R (2024/25) | `https://joburg.org.za/services_/Pages/City%20Services/Rates%20and%20Taxes/Rates-and-Tax.aspx` |
| **eThekwini (Durban)** | ~0.95–1.0 c/R (2024/25) | `https://www.durban.gov.za/uploads/0000/6/2025/09/22/ethekwini-municipality-property-rates-policy-2025-2026.pdf` |
| **City of Tshwane (Pretoria)** | ~0.93 c/R (2024/25) | `https://www.tshwane.gov.za/?page_id=6924` |
| **Ekurhuleni** | ~0.85 c/R (2024/25) | `https://www.ekurhuleni.gov.za/` |

(2024/25 data — **rates may have changed since July 2025 tariff cycle**; verify current at each municipality's tariff page.)

**Computation**: each municipality applies an **impermissible value** threshold (first ~R350,000 typically exempt for primary residence in Cape Town; ~R200,000 est. in JHB — verify JHB rates policy) before the rate. The Municipal Property Rates Act 6 of 2004 governs the framework.

**Example** — R5,000,000 home in Cape Town (2024/25):
- Taxable value: R5,000,000 − R350,000 = R4,650,000
- Annual rates: R4,650,000 × 0.006055 = **~R28,156/yr (~R2,346/month)**
- Plus refuse + sewer + water utility tariffs (separate)

### Capital Gains Tax (CGT) — seller, on disposal

- 40 % inclusion rate × marginal income tax rate (max 45 %) → **max effective CGT 18 %**
- **Primary residence exclusion**: first **R2,000,000** of gain excluded (per SARS) — applies only if used as primary residence
- Source: SARS CGT: `https://www.sars.gov.za/types-of-tax/capital-gains-tax/`

### Section 35A — Non-resident seller withholding

- For sales where the price is **R2,000,000 or more** to non-resident sellers (i.e., ≥ R2m, applies to the **full purchase price** — not only the portion above R2m), conveyancer must withhold (rates per SARS s35A, amended 22 Feb 2017; 2026-05-27 verified):
  - **7.5 %** if seller is natural person
  - **10 %** if seller is company
  - **15 %** if seller is trust
- Withheld amount paid to SARS within **14 days** if purchaser is resident, **28 days** if purchaser is non-resident; offset against final CGT on assessment.
- Seller may apply to SARS for a **directive** for a reduced or zero rate (e.g., exempt, low income, disposal at a loss) under the Tax Administration Act 28 of 2011 (TAA).
- Source: SARS s35A guide IT-PP-02-G01 + Non-resident sellers page: `https://www.sars.gov.za/types-of-tax/capital-gains-tax/non-resident-sellers-of-immovable-property/`

### Estate Duty

- 20 % above R3,500,000 abatement; 25 % on portion above R30,000,000
- Surviving-spouse abatement: any unused portion rolls over (effective abatement R7,000,000 for second-dying spouse if first-dying used none)
- Source: SARS Estate Duty: `https://www.sars.gov.za/types-of-tax/estate-duty/`

### Conveyancer / attorney fees (recommended Law Society guideline tariff — not statutory)

For R2M–R5M property: typically **R20,000–R50,000** (excluding VAT, Deeds Office reg, and bond reg)

### Total transaction cost (buyer side, 2025/26)

For an R3,000,000 cash purchase (no bond), Cape Town:
- Transfer Duty (R3M): R106,784 + 11 % × (R3,000,000 − R2,994,800) = **R107,356** (R3,000,000 falls in the R2,994,801–R13,310,000 bracket)
- Conveyancer transfer fees: ~R28,000 + VAT
- Deeds Office reg: ~R1,000
- FICA / disbursements: ~R2,000
- **Total: ~R140,000 (~4.7 % of price)**

For same R3M with 80 % bond:
- Above + bond registration attorney: ~R28,000 + VAT
- Bank initiation fee: ~R6,000
- Bond registration Deeds Office: ~R1,500
- **Total: ~R180,000 (~6.0 %)**

---

## Section: `--rental`

### Long-term residential rentals

**Governing law**:
- **Rental Housing Act 50 of 1999** (national framework + Provincial Rental Housing Tribunals for disputes)
- **Consumer Protection Act 68 of 2008** (consumer-facing tenants)
- **Common law** (lease principles)

**Key obligations**:
- Written lease required if either party requests
- **Deposit**: must be held in **interest-bearing trust account** (interest accrues to tenant on return); refund within 7 days if no claims, or 14 days with itemised deductions
- **Inspection**: joint at move-in AND move-out, written report
- Notice: typically 1 calendar month for both parties
- Eviction: PIE Act 19 of 1998 (Prevention of Illegal Eviction) — court order required, lengthy

**Tax treatment**:
- Rental income reported on **ITR12** (annual return) and **IRP6** (provisional tax twice yearly)
- Deductible expenses: rates, levies, insurance, repairs (not improvements), bond interest, agent commission, water/electricity if owner-paid
- Net rental income added to taxable income at marginal rate (max 45 % for 2025/26 above ~R1,817,000 — top-bracket threshold est., verify SARS personal income-tax brackets table)
- Source: SARS Rental Income: `https://www.sars.gov.za/individuals/i-am-a-property-investor/`

### Short-term rentals (STR / Airbnb)

**Status**: in regulatory transition.

- **STR regulatory state of play (2026-05-27 verified)**: the **2019 Tourism Amendment Bill** (Hanekom) has been **shelved**; the successor instrument is the **Draft Code of Good Practice for Short-Term Rentals** gazetted by Tourism Minister Patricia de Lille in **March 2026** (60-day public comment closed **12 May 2026**) — currently **non-binding** but signals registration is the direction of travel under the Tourism Act 3 of 2014; a new **Tourism Amendment Bill** is estimated to reach **Cabinet during the 2026/27 financial year** (per Dept of Tourism briefing to the Portfolio Committee on Tourism, PMG `https://pmg.org.za/committee-meeting/42612`, 2026-07-02). Aug 2023 MoU between Airbnb + Dept of Tourism on a national STR database remains operative. **TOMSA Levy** (1 % voluntary, on accommodation tariff excl. VAT) managed by TBCSA; not a statutory tax. **No national statutory tourism tax exists** as of May 2026. Verify at `https://www.tourism.gov.za/`. Source: dearsouthafrica bill tracker; Lexology critical overview; Financial Mail 2026-04-09.
- **City of Cape Town (2026-07-02 verified)**: the **Municipal Planning By-Law (MPBL 2015 + amendments) already permits short-term letting**, so a zoning change is generally **not** required (a temporary departure from land-use rights / consent-use application may still apply in specific zones — treat as a per-erf caveat, not the default). The active 2026 levers are **rates + registration**: (1) a **2026/27 Rates Policy amendment** (tabled in Council **31 Mar 2026**, public comment to **30 Apr 2026** as part of the draft City budget; **approved by Special Council 29 Jun 2026** (SPC 04/06/26; 2026/27 Rates Policy Annexure 5 — threshold measured on room nights = bedrooms x 365 over any 365-day period incl. future listed availability; business rates ratio 1:2.41), policy year **from 1 Jul 2026**) **reclassifies any property available for STR >50% of any 365-day period as commercial** rather than residential for rating (stays commercial until availability falls below 50% within a 365-day period); commercial reclassification of identified properties is **foreseen only from 1 Jul 2027** after a grace period. (2) a **mandatory STR registration system** (City-issued registration number for every property listed on an online booking platform) to be legislated via a **Short-Term Letting By-Law later in 2026**. Source: City of Cape Town Short-Term Letting FAQs `https://resource.capetown.gov.za/cityassets/Media%20Centre%20Assets/CCT-short-term-letting-FAQs.pdf`.
- **Body Corporate / HOA** (sectional title or estate): often **forbid STR** in the rules / conduct rules — verify sectional title management rules + conduct rules BEFORE buying for STR purpose
- **CSOS dispute forum**: residents can complain to Community Schemes Ombud Service if neighbour STR violates scheme rules

**Tax treatment for STR**:
- If casual / occasional → standard rental treatment (ITR12)
- If full-time professional → may be classified as "trade" → taxed as business income; consider PTY Ltd structure
- VAT registration mandatory if turnover > R1,000,000/12 months (compulsory) — verify SARS VAT thresholds

**Strategic notes**:
- Cape Town summer (Dec–Feb) peak; Atlantic Seaboard yields highest in country
- Garden Route (Knysna, Plett), KZN North Coast (Ballito, Umhlanga) seasonal
- Body Corporate consent the silent killer — many sectional title schemes ban STR via rule changes (CSOS-validated)
- Crime / safety perception affects demand — security infrastructure (alarms, electric fence, armed response) listed as features

---

## Section: `--work=<profession>`

### Job platforms

- **Pnet**: `https://www.pnet.co.za/` (largest)
- **Careers24**: `https://www.careers24.com/`
- **LinkedIn ZA** — very active in finance, IT, mining, professional services
- **Indeed ZA**: `https://za.indeed.com/`
- **Bizcommunity**: `https://www.bizcommunity.com/Jobs.aspx` (marketing, media, comms)
- **CareerJunction**: `https://www.careerjunction.co.za/`

### Self-employment / business structures

- **Sole proprietor**: simplest; report income on ITR12 personal return; no separation of liability
- **PTY Ltd** (Private Company): registered at CIPC (`https://www.cipc.co.za/`); separate legal person; subject to corporate tax 27 % (2025/26) + dividends tax 20 % on distributions
- **Provisional Tax (IRP6)** — twice yearly (Aug, Feb) for non-PAYE income earners
- **UIF** (Unemployment Insurance Fund): 1 % employer + 1 % employee on remuneration (cap)
- **COIDA** (Compensation for Occupational Injuries and Diseases Act): annual return + assessment

### Foreign worker visas — Department of Home Affairs

- **General Work Visa**: requires Department of Employment & Labour confirmation no SA citizen available
- **Critical Skills Work Visa**: per gazetted Critical Skills List (most recent: 2022 — verify at `https://www.dha.gov.za/`)
- **Intra-Company Transfer Visa**: max 4 years
- **Business Visa**: requires R5,000,000 investment minimum (waivable for some sectors)
- **Permanent Residence**: various paths (5-yr work visa + critical skills, spouse, retired person with R37,000/month income)
- **Retired Person's Visa**: requires income/assets ≥ R37,000/month for life

Source: Department of Home Affairs: `https://www.dha.gov.za/index.php/immigration-services/types-of-visas`

### Salary benchmarks (2025, gross monthly, ZAR)

- Junior professional (entry, JHB/CT): ~R15,000–R30,000 (est.)
- Mid-level (5+ yrs, urban): ~R35,000–R70,000 (est.)
- Senior / management (urban): ~R80,000–R200,000+ (est.)
- Skilled trades (electrician, plumber): ~R20,000–R45,000 (est.)
- Bands are model/market estimates — the Stats SA QLFS (P0211) measures employment/unemployment levels, NOT per-occupation pay; verify against a current recruiter/salary-survey release (e.g. Stats SA QES earnings data or a PE/CareerJunction salary survey).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Council for Geoscience (CGS)** — sinkhole/dolomite + seismic | `https://www.geoscience.org.za/` | Dolomite stability + seismic hazard maps |
| **South African Weather Service (SAWS)** | `https://www.weathersa.co.za/` | Storm/flood/wind warnings; long-term climate data |
| **Working on Fire / DFFE wildfire** | `https://www.workingonfire.org/` + `https://www.dffe.gov.za/` | Wildfire registry + alerts |
| **Provincial Disaster Management Centres (DMCs)** | per province (e.g., `https://www.westerncape.gov.za/local-government/disaster-management`) | Local hazard maps + response |
| **Department of Water and Sanitation** | `https://www.dws.gov.za/` | Floodlines, dam levels |
| **City of Cape Town water dashboard** | `https://www.capetown.gov.za/Family%20and%20home/Residential-utility-services/Residential-water-and-sanitation-services` | Dam levels, restriction levels |
| **SAPS Crime Statistics** (quarterly) | `https://www.saps.gov.za/services/crimestats.php` | Per-station crime stats |

### Region-specific recurring hazards

| Region | Hazard | Notes |
|---|---|---|
| **Cape Town + Western Cape** | Drought (Day Zero 2017–2018 residual; aquifer + desal capacity since improved) | Verify current dam levels at City dashboard each season |
| **Cape Peninsula + Cape winelands** | **Wildfire** (FOS) | Annual summer (Dec–Mar); peri-urban interface high risk in Hout Bay, Llandudno, Constantia, Stellenbosch fynbos belt |
| **KZN coast (Durban + N. Coast + S. Coast)** | **Flooding** (April 2022 catastrophic; April 2024 repeat); **storm surge** | Insurance loaded; check eThekwini DMC floodlines |
| **JHB West Rand + Centurion + parts of Pretoria** | **Sinkholes / dolomite instability** | CGS dolomite stability map ESSENTIAL pre-purchase; build-restriction zones |
| **Highveld (JHB, Pretoria)** | Hailstorms (Oct–Mar); lightning | Insurance standard; vehicle hail-cover common |
| **Mpumalanga + Limpopo escarpment** | Wildfire + landslide | Lower density of formal mapping |
| **Eastern Cape coastal** | **Coastal erosion** + storm | DFFE coastal management |

### Seismicity

- South Africa is **seismically low-to-moderate** (intraplate); most properties **🟢 negligible** risk
- **Exception**: induced seismicity in **Klerksdorp / Welkom / Carletonville mining belt** (gold mining-induced tremors, occasional M3–M5)
- CGS seismic hazard map: `https://www.geoscience.org.za/index.php/services/seismology`

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1980** | Asbestos cement (Everite) very common in roofing; lead paint; lead pipes; minimal SANS compliance |
| **1980–2008** | SANS 10400 in force from 1990; energy efficiency NOT mandatory; mid-quality concrete |
| **Post-2008** | **SANS 10400-XA energy efficiency** mandatory (insulation, glazing, hot-water minimums) |
| **Post-2011** | Sectional Titles Schemes Management Act enforced; better body corporate governance expected |
| **Coastal (any era)** | **Beetle borer** (Hylotrupes, Coptotermes) endemic Western Cape + KZN coastal — Beetle Free Cert mandatory at sale |

**Asbestos**: Asbestos Abatement Regulations 2020 require licensed contractor for removal; cost est. R150–R400/m² (verify via licensed contractor — `https://www.labour.gov.za/`).

### Mandatory diagnostics at sale

| Document | When required | Validity / penalty |
|---|---|---|
| **Title Deed verification** | All sales | Free via Deeds Office walk-in / paid via DeedsWeb / done by conveyancer |
| **Rates Clearance Certificate** | All sales | Issued by municipality; **transfer cannot register without it**; valid 60 days typical |
| **Beetle Free Certificate** (Coastal — W. Cape, KZN, E. Cape, Garden Route) | All sales | Required by lender + most contracts; valid ~3 months |
| **Electrical Compliance Certificate (CoC)** | All sales (national, per Occupational Health and Safety Act / Electrical Installation Regs 2009) | Valid 2 years |
| **Plumbing Certificate** | Cape Town (since 2010 by-law); JHB requires certain works | Per municipality; verify locally |
| **Gas Compliance Certificate** | If gas appliance present (national, per OHSA gas regs) | Valid 5 years (or per re-installation) |
| **Electric Fence System Compliance Certificate** | If electric fence present | One-off; transferable |
| **Body Corporate Levy Clearance / Section 15B(3) Certificate** | Sectional title only | At signing |
| **HOA Levy Clearance** | Estate / freehold-in-HOA only | At signing |
| **SG diagram** | All sales | Free / nominal; via SG office |

### Climate change projections (DFFE / NCCRP)

- **+1.5–3.5 °C by 2050** vs 1986–2005 baseline (CSIR Green Book; depends on RCP)
- **Western Cape**: drier (winter rainfall reduction projected); fire-weather days +20–40 %
- **Eastern half**: more intense convective storms + flooding
- **Coastal SLR**: 0.4–0.8 m by 2100 likely (IPCC AR6 + DFFE coastal climate)
- KZN coastal flooding events (2022, 2024) consistent with increased rainfall extremes

Source: CSIR Green Book climate atlas: `https://greenbook.co.za/`

---

## Section: `--mains`

### National / municipal water + sanitation

- **City of Cape Town Water & Sanitation**: `https://www.capetown.gov.za/Family%20and%20home/Residential-utility-services/Residential-water-and-sanitation-services`
- **Joburg Water (City of Johannesburg)**: `https://www.johannesburgwater.co.za/`
- **eThekwini Water and Sanitation**: `https://www.durban.gov.za/page/water-and-sanitation-services`
- **City of Tshwane**: `https://www.tshwane.gov.za/?page_id=6924`
- **Ekurhuleni Water**: `https://www.ekurhuleni.gov.za/`
- **Department of Water and Sanitation**: `https://www.dws.gov.za/`

### Verification

1. Check property's municipal account / rates statement — names water + sanitation service line
2. Listing language:
   - "municipal water + sewer" = mains both
   - "borehole + septic" = none on mains
   - "borehole + sewer" = mains sewer only (rural-urban edge)
3. **Most urban erfs in metro municipalities have full mains** (water + sewer); peri-urban smallholdings often borehole + septic; rural farms usually borehole + septic + own electricity arrangements

### Eskom load-shedding

- **Status (2026-08-07 verified)**: **no national loadshedding since 16 May 2025** — Eskom recorded **441 consecutive loadshedding-free days as at 31 Jul 2026**, the first full loadshedding-free year since Sept 2018 having been reached at 00:01 on 16 May 2026; the Winter Outlook published 22 Apr 2026 projects no loadshedding to 31 Aug 2026, and demand was met 100 % of the time FY-to-date (1 Apr–30 Jul 2026), on the Generation Recovery Plan + Operation Vulindlela reforms and private generation. Verify current at `https://www.eskom.co.za/distribution/loadshedding/` or EskomSePush app. Source: Eskom `https://www.eskom.co.za/eskom-sustains-strong-system-performance-eaf-reaches-highest-daily-level-82-04-since-2017-and-unplanned-outages-recorded-at-lowest-daily-level-in-eight-years`
- **Residual localised risk is load reduction, NOT loadshedding** — peak-hour switch-offs on high-theft or overloaded feeders; ~6.9 % of Eskom's 7.2m customers still affected (down from a 23.5 % peak), six provinces load-reduction-free, nationwide eradication targeted 2027. **Check the specific feeder / suburb**, not the national headline (2026-08-07 verified)
- **Next trigger**: Eskom Q2 FY2027 coal shutdown / repowering decision due 1 Jul–30 Sep 2026
- **Solar / inverter / battery backup** still common upgrade despite improved supply; cost R80,000–R300,000 typical install (5–10 kWh battery + inverter ± solar PV)
- **Section 12B / 12BA tax allowance** for renewable energy (business) — verify with SARS

### Costs

| Scenario | Cost (ZAR) |
|---|---:|
| Municipal new connection (water) | R5,000–R20,000 |
| Municipal sewer connection where available | R10,000–R40,000 |
| Septic tank install (rural) | R30,000–R80,000 |
| Borehole drill + pump install | R60,000–R150,000 |
| Solar + inverter + battery (5 kWh) | R80,000–R150,000 |
| Solar + inverter + battery (10 kWh + PV) | R200,000–R350,000 |

---

## Cost benchmarks (ZA 2026)

| Work | Cost (ZAR) |
|---|---:|
| **Transfer Duty** | per SARS Schedule 8 (see --tax above) |
| Conveyancer transfer fees (R2M–R5M) | R20,000–R50,000 + VAT (Law Society guideline) |
| Deeds Office registration | ~R1,000–R2,000 |
| Bond registration attorney | R20,000–R50,000 + VAT |
| Bank bond initiation fee | ~R6,000 |
| Bond registration at Deeds Office | ~R1,500 |
| Beetle Free Certificate | R500–R2,000 (inspection) + R3,000–R15,000 (treatment if found) |
| Electrical CoC | R1,500–R5,000 (inspection) + remedial cost if non-compliant |
| Plumbing Certificate (Cape Town) | R1,500–R5,000 |
| Gas CoC | R1,000–R3,000 |
| Independent building inspection | R3,000–R10,000 |
| Valuation | R2,000–R5,000 |
| Sectional title monthly levy (typical) | R500–R5,000/month (premium estates higher) |
| Body Corporate special levy (when needed) | varies (can be R10,000–R200,000+ once-off) |
| **Total transaction cost (buyer side, R3M cash)** | ~4.5–6 % of price |

## Active fiscal incentives (2025/26)

- **Section 13sex tax allowance** — 5 % p.a. straight-line write-down for new/unused **5+ residential units** owned for letting (income-tax deduction); confirm conditions at SARS: `https://www.sars.gov.za/`
- **Section 12L** — energy-efficiency savings tax allowance (claim per kWh saved per certified baseline); SANEDI managed: `https://www.sanedi.org.za/`
- **Section 12B / 12BA** — standard s12B renewable-energy allowance continues (50 %/30 %/20 % over 3 yrs, or 100 % accelerated for small-scale renewables ≤1 MW); **s12BA 125 % enhanced allowance lapsed 28 Feb 2025** (applied to PV + storage placed in service 1 Mar 2023 – 28 Feb 2025); verify any new incentive at SARS Budget 2026 (2026-05-27 verified)
- **Solar PV individual rebate** (announced Budget 2023): up to R15,000 individual income tax rebate for solar PV panels installed between 1 March 2023 and **expired 29 February 2024** — **NOT extended in 2025 or 2026/27 Budget** (no successor residential solar PV incentive enacted; verify at `https://www.sars.gov.za/types-of-tax/personal-income-tax/filing-season/solar-tax-rebate/` and 2026/27 Budget Review) (2026-07-02 verified)
- **First-Time Home Buyers**: no specific national grant; some lenders offer first-time-buyer rates (FNB, Absa, Standard Bank, Nedbank); FLISP (Finance Linked Individual Subsidy Programme) for income R3,501–R22,000/month — DHS: `https://www.dhs.gov.za/`

## Common listing platforms

- **Property24** — `https://www.property24.com/` (largest)
- **Private Property** — `https://www.privateproperty.co.za/`
- **Pam Golding** — `https://www.pamgolding.co.za/` (premium)
- **Seeff** — `https://www.seeff.com/`
- **Lew Geffen Sotheby's** — `https://www.sothebysrealty.co.za/` (luxury)
- **Remax SA** — `https://www.remax.co.za/`
- **Gumtree Property** — `https://www.gumtree.co.za/s-property-for-sale/v1c8398p1` (downmarket / privates)

## Caveats unique to ZA

- **BEC risk (Hawarden v ENS, [2024] ZASCA 90, 10 Jun 2024)** — Supreme Court of Appeal held conveyancers owe **no duty of care** to non-client buyers to warn of business email compromise; buyer bears the wire-fraud risk. Ms Hawarden lost ZAR 5.5m to a fraudster-substituted bank-detail letter. **Before any wire to a conveyancer trust account, phone-verify bank details against an independently-sourced number** (firm's switchboard listed on the Legal Practice Council roll, not the email signature). Foreign buyers wiring from offshore particularly exposed. ConCourt application pending. Source: SAFLII `https://www.saflii.org/za/cases/ZASCA/2024/90.html` (2026-05-27 verified).
- **CIPC Beneficial Ownership filing regime** (General Laws Amendment Act 22 of 2022) — any company/CC holding the property must file BO with CIPC within 30 days of anniversary alongside annual return; from **1 Jul 2024 CIPC hard-stops annual returns without BO compliance**; anyone with **>5 % beneficial interest** must be disclosed; non-compliance blocks annual returns and risks deregistration → cloud on title. Final reminder issued 21 Jul 2025. Verify at `https://www.cipc.co.za/?p=20495` (2026-05-27 verified).
- **Crime / safety per-suburb** verification critical — never rely on metro-level stats; pull SAPS quarterly per police station + walk the area at night before buying. ADT / Fidelity / Chubb armed-response coverage near-mandatory in JHB / parts of Cape Town
- **Load-shedding + backup power costs** — **no national loadshedding since 16 May 2025** (441 loadshedding-free days as at 31 Jul 2026, Eskom); the live residual is **load reduction** on high-theft / overloaded feeders (~6.9 % of Eskom's 7.2m customers), so check the specific feeder / suburb rather than the national headline. Backup power (inverter / PV) is still commonly retained as a legacy install — market practice, not sourced; verify per property. Budget est. R100k–R300k for solar/inverter/battery if working from home is critical (2026-08-07 verified)
- **Body Corporate health (sectional title)** — request 3 years of Annual General Meeting minutes + audited financials + reserve fund (10 yr Maintenance Plan mandatory under STSMA s. 3); special-levy risk if reserve under-funded
- **FICA proof of source of funds** — conveyancer will require bank statements, tax clearance, ID / passport copies; non-residents need apostilled docs + foreign bank statements
- **Non-resident 7.5 % S35A withholding** on sale > R2M (10 % company / 15 % trust) — paid to SARS by conveyancer; offset on assessment
- **Conveyancer mandatory** — only an admitted attorney with conveyancing certificate can lodge transfer at Deeds Office; buyer chooses but seller often prescribes
- **Beetle / Electrical / Plumbing CoCs at sale** — non-negotiable for lender finance; budget remediation
- **Expropriation Act 13 of 2024** — **not in force as at 2026-09-24**: s31 requires a presidential proclamation and gov.za records commencement as "To be proclaimed". The consolidated DA / AfriForum / IRR Legal / Vaderland Stigting constitutional review opened in the **Western Cape High Court** (not the Constitutional Court) on 3 Aug 2026, with Ramaphosa, DPWI, the NA Speaker and the NCOP Chairperson as respondents, and was **postponed part-heard** on 7 Aug 2026 after five hearing days — per applicant AfriForum's 7 Aug 2026 statement, three respondents and three friends of the court had still to argue and the applicants' replies were outstanding; no resumption date published in the sources read — verify resumption + judgment on SAFLII. The Minister of Public Works and Infrastructure confirmed in NCOP written reply 18 (CW18E) of 26 Feb 2026 that the Act is "the subject of multiple constitutional legal challenge by various applicants". **Practical urban residential risk remains very low while the Act is unproclaimed** (Act narrowly targets unused land, derelict properties, agrarian reform), but theoretical risk for residential land should be disclosed to foreign buyers; full text: `https://www.parliament.gov.za/storage/app/media/Acts/2024/Act_13_of_2024_Expropriation_Act_2024.pdf`; commencement status: `https://www.gov.za/documents/acts` (2026-08-07 verified)
- **Coastal Beetle borer** — endemic W. Cape + KZN; treatment cost can run R20,000–R100,000+ for full-roof fumigation
- **Cape water security** — improved post-Day-Zero (2018) via desal, aquifer extraction, demand management; on-watch in extended droughts
- **Sinkhole / dolomite zones** (JHB West Rand, Centurion, parts of Pretoria) — CGS Dolomite Stability Map essential pre-purchase; in worst zones building permits restricted
- **KZN April flood pattern** — 2022 + 2024 events catastrophic; insurance now loaded for floodplain properties

## Reddit / forum sources

- **r/southafrica** — general
- **r/capetown** — Cape-specific (active property threads)
- **r/johannesburg** — JHB-specific (load-shedding, security debate-heavy)
- **r/PersonalFinanceZA** — bond + tax discussions
- **MyBroadband forums** — `https://mybroadband.co.za/forum/` (active property + tech threads)
- **BizNews** — `https://www.biznews.com/` (financial commentary)
- **Daily Maverick** — `https://www.dailymaverick.co.za/` (investigative + property/policy)
- Facebook: "Property in South Africa", "Cape Town Real Estate" groups (anecdotal)

## Verification authorities

| Authority | When to call |
|---|---|
| **Deeds Office** (per city) | Title Deed verification; full property history; encumbrances |
| **DLRRD** (Dept of Land Reform & Rural Development) | National cadastre policy; Deeds Registration Trading Entity |
| **Department of Agriculture** (`nda.gov.za`) | Veterinary import permits (pet relocation) |
| **Surveyor-General** (per province) | SG diagram; erf boundary verification |
| **SARS** | Transfer Duty calculation; CGT; rental tax queries |
| **Municipality** (rates, valuations, planning, CoCs) | Rates clearance, building plans approval, zoning, valuation roll |
| **CSOS** (Community Schemes Ombud Service) | Sectional title / HOA disputes; scheme rules verification |
| **Eskom + private utilities** | Load-shedding stages (none nationally since 16 May 2025); **load-reduction status for the specific feeder / suburb**; connection costs |
| **SAPS Crime Stats** | Per-station crime data quarterly |
| **CGS** (Council for Geoscience) | Dolomite stability map; seismic; geotechnical |
| **SAWS** (SA Weather Service) | Climate / storm history |
| **DFFE** (Forestry, Fisheries & Environment) | Coastal management; wildfire registry |
| **Body Corporate / Managing Agent** (sectional title) | Levy clearance; AGM minutes; reserve fund; rules |
| **HOA** (estate / freehold) | Levy clearance; conduct rules; aesthetic rules |

## Quirks to know

- **Title Deed is sole evidence of ownership** — there is NO title insurance market in ZA (unlike US); Deeds Registry is state-guaranteed
- **SG diagram link**: every erf has a SG diagram registered separately — verify boundary matches what seller claims
- **Body Corporate vs HOA**: sectional title schemes have a Body Corporate (statutory under STSMA); estates / share-block schemes typically HOA (contractual under Articles); different governance + dispute paths
- **Special Levies clause**: review last 3 yrs AGM minutes for hints of impending special levy (roof, lift, painting cycles)
- **Beetle / electrical / plumbing CoCs** mandatory at sale — see Risks section
- **CSOS dispute forum**: cheaper / faster than High Court for body corporate / HOA disputes; both parties bound by adjudication
- **FICA enforcement**: South Africa was on FATF "grey list" 2023; FICA enforcement intensified — expect lengthy KYC for non-residents
- **Expropriation Act 13 of 2024** is **not yet in force** — awaiting the s31 presidential proclamation (gov.za commencement: "To be proclaimed") as at 2026-09-24; the consolidated DA / AfriForum / IRR Legal / Vaderland Stigting constitutional review opened in the **Western Cape High Court**, not the Constitutional Court, on 3 Aug 2026 and was **postponed part-heard** on 7 Aug 2026 with argument unfinished (per applicant AfriForum's 7 Aug 2026 statement; no resumption date published in the sources read); practical urban residential expropriation extremely rare; theoretical risk should be disclosed
- **SARS S35A non-resident withholding** — the 7.5 / 10 / 15 % is INTERIM; final CGT liability assessed on tax return; reclaim possible if over-withheld
- **Loadshedding language**: "Stages" (1–8) refer to MW shed; "Stage 4" ≈ 4–8 hr/day cuts in 2 hr blocks per area schedule — but **no stage has been declared nationally since 16 May 2025**. Do not conflate loadshedding with **load reduction** (peak-hour switch-offs on high-theft or overloaded feeders), which is the only outage regime still running on some feeders (2026-08-07 verified)
- **Ekurhuleni includes OR Tambo Airport** — may impact noise / flight-path properties
- **Foreign buyer mortgage cap**: typically **50 % LTV for non-resident foreigners** without SA work visa; **70–90 % LTV** for resident foreigners with valid visa (varies by lender — verify with FNB / Standard Bank / Absa / Nedbank / Investec; offshore-funds verification adds 4–8 weeks)

## Source URL templates

| Source | URL |
|---|---|
| Deeds Office (Deeds Registration) | `https://www.deeds.gov.za/` |
| DeedsWeb (subscription portal) | `https://www.deeds.gov.za/` |
| SARS Transfer Duty | `https://www.sars.gov.za/types-of-tax/transfer-duty/` |
| SARS CGT | `https://www.sars.gov.za/types-of-tax/capital-gains-tax/` |
| SARS Rental Income | `https://www.sars.gov.za/individuals/i-am-a-property-investor/` |
| SARS Estate Duty | `https://www.sars.gov.za/types-of-tax/estate-duty/` |
| SARB Quarterly Bulletin | `https://www.resbank.co.za/en/home/publications/quarterly-bulletin1` |
| FNB Property Barometer | `https://www.fnb.co.za/economics-commentary/property-barometer.html` |
| Stats SA RPPI | `https://www.statssa.gov.za/?page_id=1854&PPN=P0151` |
| Property24 | `https://www.property24.com/` |
| Private Property | `https://www.privateproperty.co.za/` |
| Pam Golding | `https://www.pamgolding.co.za/` |
| Lightstone | `https://www.lightstoneproperty.co.za/` |
| Cape Town rates / valuations | `https://www.capetown.gov.za/Family%20and%20home/Residential-utility-services/Residential-property-rates-and-valuations` |
| JHB property rates | `https://joburg.org.za/services_/Pages/City%20Services/Rates%20and%20Taxes/Rates-and-Tax.aspx` |
| eThekwini property tax | `https://www.durban.gov.za/uploads/0000/6/2025/09/22/ethekwini-municipality-property-rates-policy-2025-2026.pdf` |
| Tshwane | `https://www.tshwane.gov.za/?page_id=6924` |
| CSOS | `https://www.csos.org.za/` |
| CGS (geoscience / dolomite / seismic) | `https://www.geoscience.org.za/` |
| SAWS (weather / climate) | `https://www.weathersa.co.za/` |
| Eskom load-shedding | `https://www.eskom.co.za/distribution/loadshedding/` |
| SAPS Crime Stats | `https://www.saps.gov.za/services/crimestats.php` |
| Department of Home Affairs (visas) | `https://www.dha.gov.za/index.php/immigration-services/types-of-visas` |
| CSIR Green Book (climate atlas) | `https://greenbook.co.za/` |
| PPRA (Property Practitioners Regulatory Authority) | `https://www.theppra.org.za/` |
| Acts of Parliament | `https://www.gov.za/documents/acts` |

## Status

✅ **Fully populated** as of 2026-05-01.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government / regulated-entity sources + cost benchmarks + caveats.
**Confidence**: **HIGH** for cadastre / Transfer Duty / CGT / conveyancer requirements / FICA (all primary state / SARS / DHA sources). **MEDIUM** for municipal rates per-city (annual tariff cycle each July; verify current). **MEDIUM** for short-term rental rules (Tourism Amendment Bill in flux; municipal STR regulation evolving; verify Cape Town MPBL current state). **MEDIUM** for Expropriation Act 13 of 2024 implementation (Act unproclaimed / not in force as at 2026-08-07; Western Cape High Court constitutional review postponed part-heard on 7 Aug 2026 after five hearing days, argument unfinished and no resumption date published in the sources read; practical residential urban risk currently very low).
**Last verified**: 2026-08-07 (`--finance` and `--risks` re-verified — Expropriation Act 13 of 2024: assent 20 Dec 2024, *Government Gazette* No. 51964 of 24 Jan 2025, still unproclaimed under s31, Western Cape High Court review heard 3–7 Aug 2026 and postponed part-heard on 7 Aug (corrected 2026-09-24); and Eskom load-shedding, which has been at zero rather than merely "declining" since 16 May 2025). Prior sweep 2026-05-27 (Transfer Duty bracket date 1 Apr 2025; Tourism Bill shelved + Mar 2026 Code + TOMSA; Hawarden v ENS [2024] ZASCA 90; CIPC BO regime; s35A rates 7.5/10/15; s12BA lapsed 28 Feb 2025; VAT 15.5% withdrawn 24 Apr 2025). ZA departmental split + Deeds Registration ownership re-verified 2026-09-18 (authority / URL only). Cape Town 2026/27 Rates Policy STR limb re-verified 2026-09-24 in the October regwatch wave; Tourism Bill, STL By-law status and FAQ grace date not re-checked. Finance tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

## Extension TODOs (deepen on first real run)

- [ ] Per-suburb SAPS crime station pull (manual quarterly download)
- [ ] Per-municipality annual tariff scrape (Cape Town, JHB, eThekwini, Tshwane, Ekurhuleni each July)
- [ ] CGS Dolomite Stability Map per-erf overlay (JHB West Rand + Centurion essential)
- [ ] eThekwini floodlines per-erf (April 2022 / 2024 reference)
- [ ] Critical Skills List 2022 → next gazette (DHA) revisit cadence quarterly
- [ ] Tourism Amendment Bill enactment tracker
- [ ] Expropriation Act 13 of 2024 — Western Cape High Court resumption + judgment tracker (part-heard; postponed 7 Aug 2026 after 3–7 Aug hearing days) + s31 presidential proclamation watch
- [ ] FICA non-resident KYC walk-through (typical 4–8 weeks)
- [x] Solar PV individual rebate — confirmed NOT extended in 2025 or 2026/27 Budget (2026-07-02)
