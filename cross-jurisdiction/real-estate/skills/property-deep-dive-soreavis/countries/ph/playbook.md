# Philippines 🇵🇭 — Property Due-Diligence Playbook

ISO2: `ph`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

> **🇵🇭 LEAD WARNING — read before any other section.** The Philippines is a **constitutionally foreign-restricted** market. Under **1987 Constitution Art. XII §7**, only Filipino citizens (or corporations ≥60% Filipino-owned) may own LAND. Foreigners may own **condominium units** within a project's 40% foreign equity cap (Republic Act 4726, Condominium Act of 1966) and **buildings/improvements** on land held under a long-term lease (Republic Act 7652, Investors' Lease Act of 1993, max 50 + 25 yrs). Nominee structures ("Filipino fronting for a foreigner") are criminalized under the **Anti-Dummy Law (Commonwealth Act 108, as amended)**: imprisonment 5–15 years + fine up to twice the value of the right transferred + forfeiture. Six- to seven-figure decisions in the Philippines demand a Philippine-licensed real-estate / property lawyer — non-negotiable.

## Country profile

- **Postcode (ZIP)**: 4 digits (PHLPost, 1978). Examples: Metro Manila `1000` Manila CBD/Ermita, `1200` Makati CBD, `1605` Pasig CBD, `1226` BGC/Taguig. Cebu City `6000`, Davao `8000`, Baguio `2600`, Iloilo `5000`, Tagaytay `4120`, Boracay/Malay (Aklan) `5608`. Directory: `https://phlpost.gov.ph/`.
- **Admin levels**: 17 administrative regions (NCR + 16 named, incl. BARMM, CAR) → 82 provinces → 149 cities + 1,489 municipalities → 42,046 barangays (PSA 2024 PSGC `https://psa.gov.ph/classification/psgc` — figures shift on barangay reclassifications).
- **Currency**: PHP (₱). Mid-Apr 2026 BSP reference: 1 USD ≈ 56–59 PHP; 1 EUR ≈ 60–64 PHP. Peso is **floating, not USD-pegged** despite long-tail US-policy correlation; daily at `https://www.bsp.gov.ph/SitePages/Statistics/ExchangeRate.aspx`.
- **Languages**: Filipino (Tagalog-based, official) + English (official, dominant in legal/commercial/title docs). All Torrens TCT/CCT/OCT, Deed of Absolute Sale, Contract to Sell are **drafted in English** — no sworn translation typically needed (rare among SE-Asian markets).
- **Cadastre / land registry**: **Land Registration Authority (LRA)** — `https://www.lra.gov.ph/`. Operates the **Torrens system** (Act 496 of 1903; now PD 1529, Property Registration Decree 1978). LRA oversees ~166 Registries of Deeds (RD), one per registration district. Public CTC request portal: `https://eserbisyo.lra.gov.ph/`. Most urban RDs computerised; rural districts partially on manual ledgers.
- **Title certificate types (Torrens)**:

| Code | Full name | Origin | Use |
|---|---|---|---|
| **OCT** | Original Certificate of Title | First registration of a parcel (decree of registration / patent) | Mother title — foundation of all subsequent transfers |
| **TCT** | Transfer Certificate of Title | Subsequent transfers of land + improvements | Standard land title — held by Filipino owner |
| **CCT** | Condominium Certificate of Title | Condominium unit + undivided interest in common areas | The only Torrens title a foreigner may hold (within 40% project quota) |

- **Major reforms / regulatory landscape** (see `shared/regulatory-watch.md` for date-stamped detail):
  - **RA 11534 (CREATE, 2021)** + **CREATE MORE (RA 12066, 11 Nov 2024)** — corporate income tax + investment incentives reform; affects PEZA / BOI enterprises.
  - **RA 11647 (2022)** Foreign Investments Act amendments — eased min paid-up capital for foreign-owned domestic corps to USD 100,000 in some cases; did NOT change the constitutional land bar.
  - **RA 11201 (2019) DHSUD Act** — created DHSUD, absorbing HUDCC housing + HLURB regulatory functions; now regulates condo / subdivision developers + issues Licences to Sell.
  - **RA 9856 REIT Act (2009)** — operational since 2020 (AREIT, DDMPR, FILRT, RCR listed on PSE).
  - **TRAIN (RA 10963, 2017)** + TRABAHO/CREATE adjustments — restructured PIT brackets; retained DST and CGT framework.
  - **RA 12001 Real Property Valuation Reform Act (Jun 2024)** — uniform valuation standard across LGUs. The statutory SMV-updating deadline of **5 Jul 2026** has **lapsed** (2026-08-07); certified Schedules of Market Values now roll out **per LGU** via BLGF/DOF review, with the first-year RPT increase capped at **6 %** of pre-RPVARA RPT per tax type (see `--tax`).
  - **Maharlika Investment Fund Act (RA 11954, 2023)** — sovereign wealth; tangential to property.
  - **Proposed but not enacted as of May 2026**: Charter Change to relax foreign land-ownership ban (perennially discussed; multiple Congresses failed). Do not assume liberalisation is imminent.

---

## 🇵🇭 LEAD SECTION: Foreign buyer eligibility

### Bottom line

The 1987 Constitution Art. XII §7 reserves **land** for Filipino citizens (or corps with ≥60% Filipino equity). The foreigner's clean ownership paths are narrow:

1. **Condominium unit (CCT)** within the project's 40% foreign equity cap — **the only freehold title a foreigner may hold in their own name**.
2. **Long-term lease of land + freehold ownership of the building** (Investors' Lease Act, RA 7652: 50 yr + 25 yr renewal).
3. **Inheritance** by hereditary succession (constitutional exception under Art. XII §7).
4. **Filipino spouse owns the land**, foreigner has no legal claim to that land (only to improvements built with conjugal funds — and even those are evidentiary).
5. **60/40 corporation** with the Filipino majority — legal in form but fraught: see Anti-Dummy Law below.

**Cannot**: own land freehold, own a "house and lot" with the lot as freehold, own agricultural land of any kind (additional bar under CARP / RA 6657), own through 100%-foreign or fronted Filipino corporations.

### Path 1: Condominium freehold (✅ recommended for most foreign buyers)

- **Statute**: RA 4726 (Condominium Act, 1966), amended by RA 7899 (1995) clarifying foreign-equity computation. Text: `https://www.officialgazette.gov.ph/1966/06/18/republic-act-no-4726/`.
- **40 % cap**: foreigners may collectively own up to 40 % of the total saleable interest in a project (by floor area or condo-corp share, per master deed). Breaching 40 % invalidates the condo corporation's capacity to hold land — title to common areas can be voided.
- **Two project structures** per master deed: (a) condo corp owns the land, foreigner owns CCT + shares (foreign shares ≤ 40 %); (b) owners hold land as undivided common interest (foreign undivided interest ≤ 40 %).
- **Verification before purchase**: request a **Foreign Ownership Certification** from the condo corp secretary confirming current foreign % and that the unit's transfer will not breach 40 %. Without it the RD may refuse annotation.
- **Pre-selling vs RFO**: pre-selling under **PD 957 (Subdivision and Condominium Buyers' Protective Decree, 1976)** + DHSUD Licence to Sell. Verify the developer holds a current LTS (`https://dhsud.gov.ph/`) before any reservation.
- **No FX form requirement**: unlike Thailand, no specific BSP foreign-exchange remittance form for condo purchase. BSP Manual of Regulations on FX Transactions governs inward-remittance reporting ≥ USD 50,000 — `https://www.bsp.gov.ph/Regulations/MORFXT/MORFXT.pdf`.

### Path 2: Long-term land lease + own the building

- **Statute**: RA 7652 (Investors' Lease Act, 1993) — foreign investors may lease private land up to **50 yrs + 25 yr renewal** (max 75). Source: `https://www.officialgazette.gov.ph/1993/06/04/republic-act-no-7652/`.
- **Building separately titled**: foreigner registers the building via a Tax Declaration in their name + a separate Deed of Sale of Improvement annotated on the parent land TCT at the RD. Improvements by Tax Declaration are weaker than Torrens titles — verify the annotation.
- **Practical use**: villa / house-and-lot in Cebu, Boracay, Palawan, Batangas, La Union often sold on this structure (Filipino lessor = developer SPV or family trust).
- **Renewal risk**: 25-yr renewal is NOT automatic — needs mutual agreement at renewal date. Enforceability against successor landowners requires the lease to be registered + annotated on the TCT.
- **PD 471 (1974)**: 50-yr cap (no renewal) for non-investor foreign lessees; RA 7652 +25-yr renewal applies only for **business purposes** registered with BOI/DTI. Pure residential leases by foreigners typically fall under Civil Code Art. 1643 (cap 99 yrs) with patchy litigation enforceability — consult counsel.

### Path 3: Filipino-majority corporation (⚠️ Anti-Dummy Law risk)

- **Mechanism**: PH domestic corp with ≥ 60 % voting capital held by Filipinos; foreigner ≤ 40 %. Corp owns the land freehold.
- **Anti-Dummy Law (CA 108, 1936, amended by PD 715, 1975) §2-A**: unlawful for a Filipino to "allow his name or citizenship to be used" to evade Filipino-ownership requirements. Penalty: imprisonment **5–15 yrs** + fine not exceeding value of right enjoyed + **property forfeiture** + perpetual disqualification from public office (for the Filipino dummy). Foreigner inducer is equally liable. Source: Senate `https://legacy.senate.gov.ph/`; DOJ `https://doj.gov.ph/`.
- **SEC enforcement**: SEC (`https://www.sec.gov.ph/`) can revoke corp registration of dummy structures. **Gamboa v. Teves** (G.R. 176579, 2013) clarified "capital" means **voting capital** — tightened scrutiny.
- **Practical**: reputable PH law firms decline 60/40 setups for purely residential foreign holding; acceptable only with genuine Filipino capital + real operating purpose (hotel / commercial).

### Path 4: Filipino spouse owns the land

- Filipino spouse owns land in their sole name; foreign spouse must execute a waiver/acknowledgment at transfer that funds are the Filipino spouse's separate property (or that the foreigner makes no claim).
- **Foreigner's death**: Filipino spouse keeps the land. **Filipino spouse's death**: foreigner inherits only by hereditary succession (Art. XII §7); no statutory disposal deadline (contrast Thailand). **Matthews v. Taylor** (G.R. 164584, 2009): foreigners cannot reclaim funds used to buy land titled to a Filipino spouse — buy at your own risk.
- **On divorce/annulment**: Filipino spouse keeps the land; no community-property claim by the foreign spouse.

### Path 5: Hereditary succession

- Constitutional exception (Art. XII §7): foreigner may acquire land by **hereditary succession** from a Filipino testator (intestate / forced heirship under the Civil Code; testamentary disposition to a non-heir foreigner is not protected). Practical reach is narrow — not a planning route for most buyers.

### SRRV (Special Resident Retiree's Visa) — Philippine Retirement Authority (PRA)

- **Legal basis**: Executive Order 1037 (1985) created the PRA; SRRV regulated under PRA Circulars. Source: `https://pra.gov.ph/srrv/`.
- **SRRV restructured effective 1 September 2025** (2026-05-27 verified, source: PRA SRRVisa page). Minimum age lowered from 50 to 40 (creating 40–49 and 50+ brackets); categories collapsed into **Classic** + **Courtesy** only (Smile, Human Touch, Expanded Courtesy retired); BI Clearance newly required for every applicant. **Current deposits** (verified at `https://pra.gov.ph/SRRVisa`):
  - **SRRV Classic, age 50+ with pension**: USD **15,000**
  - **SRRV Classic, age 50+ no pension**: USD **30,000**
  - **SRRV Classic, age 40–49 with pension**: USD **25,000**
  - **SRRV Classic, age 40–49 no pension**: USD **50,000**
  - **SRRV Courtesy** (ex-Filipinos / former Filipino citizens / foreign diplomats / int'l-org retirees), age 50+: USD **1,500** (with pension) / **3,000** (no pension); age 40–49: USD **3,000** (with pension) / **6,000** (no pension)
- **Historical (pre-1 Sept 2025) categories** retained for grandfathered holders only — Smile / Human Touch / Expanded Courtesy categories no longer issued. Pre-restructure table for reference:

| Category | Eligibility | Visa deposit (USD) | Notes |
|---|---|---:|---|
| **SRRV Smile** | Age 35+, healthy, no pension required | **20,000** | Deposit must remain in PRA-accredited bank; cannot be invested in real estate |
| **SRRV Classic** | Age 35–49, no pension | **50,000** | Convertible to active investment (incl. condo purchase ≥ USD 50,000) after 30 days |
| **SRRV Classic** | Age 50+, with pension (USD 800/mo single, USD 1,000/mo couple) | **10,000** | Convertible to real-estate investment |
| **SRRV Classic** | Age 50+, no pension | **20,000** | Convertible to real-estate investment |
| **SRRV Human Touch** | Age 35+, with medical needs | **10,000** | Plus USD 1,500/mo pension proof + health insurance |
| **SRRV Courtesy** | Age 50+, ex-Filipino or foreign diplomat / int'l org retiree | **1,500** | No bank deposit beyond the visa fee |

- **Real-estate conversion**: SRRV Classic deposits ≥ USD 50,000 may be converted to a condo purchase (Foreigner-eligible CCT only — same 40% rule applies) after 30 days from issuance; the property must be retained for the duration of SRRV status.
- **Indefinite stay**: SRRV holders enjoy multiple-entry indefinite-stay residence; not a path to citizenship (which requires Filipino blood or naturalization).
- **2020–2021 PRA reform**: SRRV deposit thresholds increased and "Tourism Smile" was tightened (former USD 20,000 deposit category for 35–49 with no pension was paused in 2020 then partially reinstated 2022; verify current text at `https://pra.gov.ph/`).

### SIRV (Special Investor's Resident Visa) — Board of Investments

- **Legal basis**: Executive Order 226 (Omnibus Investments Code, 1987) Book III; administered by the **Board of Investments (BOI)**. Source: `https://boi.gov.ph/special-investors-resident-visa/`.
- **Threshold**: minimum **USD 75,000** invested in a qualifying activity (BOI-registered enterprise, manufacturing, agribusiness, BOI Investment Priorities Plan sectors). **Direct purchase of a condominium does NOT qualify for SIRV** — SIRV requires equity in an operating enterprise, not passive real-estate.
- **Visa**: indefinite-stay; multiple-entry; spouse + minor children covered.
- **Tax**: SIRV does not confer income-tax exemption; standard PIT/CIT applies.

### Other foreign-investor visas (relevant to property ecosystem)

**9(g)** Pre-Arranged Employment (standard work visa) · **9(d)** Treaty Trader/Investor (US/Japan/Germany — substantial trade or investment) · **SVEG** (hires ≥ 10 Filipinos) · **47(a)(2)** PEZA-registered enterprise employees.

### Anti-Dummy Law enforcement (read before considering a corporation)

- CA 108 + PD 715: **criminal liability for both** the foreigner and the Filipino dummy. DOJ + SEC + DOLE enforce; criminal conviction rates historically modest but **property forfeiture** is the more common civil consequence.
- **Foreign Investment Negative List** (EO 65, 2018, last update EO 175, 2022, post-RA 11647 amendments): land ownership stays on List A (constitutional bar). Source: `https://boi.gov.ph/foreign-investments-negative-list/`.
- Recent SEC focus on retail-trade dummies (RA 8762, RA 11595 lowered foreign minimum to USD 250,000 paid-up capital for retail, 2022) signals 60/40 structures are monitored — do not assume non-enforcement.

### Confidence

**HIGH** — Constitution Art. XII §7, RA 4726, RA 7652, CA 108, RA 11647, EO 226, and SRRV/SIRV PRA/BOI primary sources are all on Official Gazette / agency websites with statutory text. **MEDIUM** for SRRV deposit category amounts (PRA periodically restructures categories — verify current text at PRA Apr 2026).

---

## Section: `--price`

### Primary sources

- **BSP Residential Property Price Index (RPPI)** — quarterly, Bangko Sentral ng Pilipinas, by region (NCR vs AONCR — Areas Outside NCR) and by property type (condo, single attached/detached, townhouse, duplex). **Successor to the discontinued RREPI series, replaced starting Q1 2025 release** (2026-05-27 verified). Source: `https://www.bsp.gov.ph/Media_And_Research/RPPI/`.
- **PSA — Construction Statistics from Approved Building Permits** — quarterly value/unit counts (proxy for new-build volume). `https://psa.gov.ph/statistics/construction`.
- **BIR Zonal Values** — per-square-meter values by location used as the **floor** for capital gains tax + DST. **Not a market value**, but the highest-of (zonal vs gross selling price) is the tax base. Lookup zonal value PDFs by RDO at `https://www.bir.gov.ph/index.php/zonal-values.html`.
- **Local Assessor's Office (City/Provincial Assessor)** — "fair market value" (FMV) and **assessed value** (a fraction of FMV) used for the local Real Property Tax (RPT) — typically lower than BIR zonal.
- **Colliers / JLL / Cushman & Wakefield / Leechiu Property Consultants** — quarterly market reports (secondary, professional). E.g., Colliers Philippines `https://www.colliers.com/en-ph` — quote with "secondary aggregator, verify against BSP RPPI (formerly RREPI; replaced Q1 2025)".

### Listing platforms (secondary, listings = seller-controlled)

- **Lamudi Philippines** — `https://www.lamudi.com.ph/`
- **MyProperty.ph** — `https://www.myproperty.ph/` (joined Lamudi group, still distinct front-end)
- **Property24 Philippines** — `https://www.property24.com.ph/`
- **Dot Property Philippines** — `https://www.dotproperty.com.ph/`
- **OnePropertee** — `https://www.onepropertee.com/`
- **PhilPropertyExpert / Hoppler / Carousell Property** — secondary sources.

### Price benchmarks (Q4 2025 / Q1 2026 reference)

> **Source warning**: BSP RPPI (formerly RREPI; replaced Q1 2025) gives the most reliable national/regional index. Listing-platform averages are seller-controlled and often run 10–25 % above realised prices. BIR zonal values are tax-floor figures, **not market price**. Use BSP for verdict, listings for comp shopping, BIR zonal for the tax estimate.

| Locality | Segment | PHP/sqm range | USD/sqm est. (57 PHP/USD) | Source |
|---|---|---|---|---|
| **Makati CBD** (Salcedo, Legaspi, Rockwell adj.) | New / branded condo | 250,000–450,000 | ≈ $4,400–$7,900 | Lamudi + Colliers Q1 2026 [verify per project] |
| **BGC / Taguig** (Bonifacio Global City) | New condo, prime | 280,000–500,000 | ≈ $4,900–$8,800 | Lamudi + Leechiu Q1 2026 |
| **Ortigas CBD** (Pasig / Mandaluyong) | New condo | 180,000–320,000 | ≈ $3,200–$5,600 | Lamudi Q1 2026 |
| **Manila — Ermita / Malate / Intramuros** | Resale condo | 90,000–180,000 | ≈ $1,580–$3,160 | MyProperty Q1 2026 |
| **Quezon City** (Eastwood, North EDSA, Diliman) | Condo | 100,000–220,000 | ≈ $1,750–$3,860 | Lamudi Q1 2026 |
| **Cebu City** (IT Park, Cebu Business Park, Mabolo) | Condo | 100,000–220,000 | ≈ $1,750–$3,860 | Lamudi + Property24 Q1 2026 |
| **Mactan / Lapu-Lapu** (Cebu beach) | Condo / villa | 80,000–200,000 | ≈ $1,400–$3,510 | Lamudi Q1 2026 |
| **Davao City** (Lanang, Matina, Ecoland) | Condo / townhouse | 70,000–140,000 | ≈ $1,230–$2,460 | Lamudi Q1 2026 |
| **Tagaytay** (cool-climate retreat) | Condo / lot+villa | 60,000–180,000 | ≈ $1,050–$3,160 | Property24 Q1 2026 |
| **Boracay (Malay, Aklan)** | Beachfront condo / villa lease | 200,000–500,000+ | ≈ $3,510–$8,770+ | Dot Property Q1 2026 |
| **El Nido / Coron (Palawan)** | Beachfront villa lease | 150,000–400,000 | ≈ $2,630–$7,020 | Dot Property Q1 2026 |
| **La Union (San Juan, Urbiztondo)** | Condo / villa lease | 80,000–200,000 | ≈ $1,400–$3,510 | OnePropertee Q1 2026 |

> Ranges are listing-derived; verify realised vs listing using BSP RPPI (formerly RREPI; replaced Q1 2025) quarterly (latest published Q4 2025 at time of writing — verify via `https://www.bsp.gov.ph/Pages/MediaAndResearch/PublicationsAndReports/regular_RREPI.aspx`).

### Compute

1. Listing price/sqm = listing PHP ÷ saleable area (floor area). **Trap**: many condo listings advertise the **gross saleable area** which includes proportional balcony + parking — ask whether the price includes parking (separately titled in many projects, often PHP 1.0–2.5M extra in Makati/BGC).
2. Compare to BSP RPPI (formerly RREPI; replaced Q1 2025) for the region.
3. Compare to nearest 3–5 same-tower / same-street listings on Lamudi or MyProperty.
4. Pull BIR zonal value via `https://www.bir.gov.ph/index.php/zonal-values.html` for the parcel's RDO — this informs the CGT/DST tax base, not the market value.
5. **Trap (foreign quota premium)**: condo units sold within the 40 % foreign quota sometimes list at a 5–10 % premium vs the Filipino-quota equivalent in the same building. Verify whether the unit is currently in foreign quota.
6. **Trap (pre-selling discount)**: pre-selling units are often 15–30 % cheaper than RFO equivalents but carry **completion risk** (developer financial distress, project cancellation) — see Caveats below.

### Confidence

**HIGH** for Metro Manila ranges (BSP RPPI (formerly RREPI; replaced Q1 2025) + multiple listing platforms agree within ±15 %). **MEDIUM** for Cebu / Davao (less granular RREPI). **LOW** for Boracay / Palawan beachfront (data dominated by foreign-buyer listing platforms; thin transaction sample).

---

## Section: `--traffic`

### Primary sources

- **DPWH** national highway AADT — `https://www.dpwh.gov.ph/` (Atlas of Roads; spotty digital availability).
- **MMDA** Metro Manila counts + EDSA corridor — `https://www.mmda.gov.ph/`.
- **DOTr** MRT/LRT modal + ridership — `https://dotr.gov.ph/`.
- **LTO** vehicle registration counts — `https://lto.gov.ph/`.
- **OSM** fallback when official AADT not available.

### Verdict bands (AADT, vehicles/day)

🟢 < 2,000 (barangay/rural) · 🟡 2,000–10,000 (provincial collector/urban side) · 🟠 10,000–40,000 (city arterial/national secondary) · 🔴 > 40,000 (national primary/Metro Manila arterial/expressway).

### Coarse fallback (OSM `highway` tag)

`motorway`/`trunk` = expressway (NLEX, SLEX, CALAX, Skyway, NAIAX) · `primary` = national highway (N1–N9 backbone) · `secondary` = national secondary/provincial trunk · `tertiary` = barangay collector · `residential` = subdivision/barangay road.

### Metro Manila quirks

- **Chronic congestion** — TomTom Traffic Index 2024 places Metro Manila in the world's top-10 most congested; average rush-hour speed on EDSA ~10–15 km/h (MMDA monitoring, 2024).
- **Number-coding** (UVVRP): private vehicles banned on specific weekdays by plate ending; verify current MMDA rules.
- **Elevated infra noise**: Skyway / NAIAX viaducts over residential areas generate noise + particulate exposure 24/7; flag any property within 100 m of an expressway pillar.
- **MRT/LRT proximity** within 500 m of a station (MRT-3 EDSA, LRT-1 Roxas, LRT-2 east-west) transacts at a premium per Colliers/Leechiu reports.

### Confidence

**MEDIUM** — DPWH AADT publication patchy; MMDA Metro Manila data fragmented. OSM-class fallback is the realistic baseline for non-highway roads.

---

## Section: `--tax`

### Annual property tax — Real Property Tax (RPT)

**Statute**: **RA 7160 (Local Government Code 1991)**, Book II Title II "Real Property Taxation" (§§ 197–283). Source: Official Gazette `https://www.officialgazette.gov.ph/1991/10/10/republic-act-no-7160/`; BLGF `https://blgf.gov.ph/`.

**Rate ceilings**: Provinces ≤ **1 %** of assessed; cities + Metro Manila municipalities ≤ **2 %** of assessed; **+1 %** mandatory **Special Education Fund (SEF)** under §235.

**Effective rates by jurisdiction** (Apr 2026 — verify current ordinance at the city/provincial treasurer):

| LGU (residential) | Basic | + SEF | Combined |
|---|---:|---:|---:|
| Quezon City | 1.50 % | 1.00 % | **2.50 %** of assessed |
| Makati / BGC-Taguig / Davao | 1.00 % | 1.00 % | **2.00 %** of assessed |
| City of Manila | 2.00 % | 1.00 % | **3.00 %** of assessed |
| Cebu City | 1.50 % | 1.00 % | **2.50 %** of assessed |
| Most provinces | 1.00 % | 1.00 % | **2.00 %** of assessed |

**Tax base (assessed value)**:

- **Assessed value** = Fair Market Value (per LGU Assessor's Schedule) × **assessment level** (statutory % per use class):
  - Residential: max **20 %** (§218 RA 7160)
  - Commercial: max **50 %**
  - Industrial: max **50 %**
  - Agricultural: max **40 %**
- The Schedule of Fair Market Values (SFMV) per assessor's office historically moved only by LGU ordinance; many LGUs are **decades behind market** (Manila SFMV last general revision pre-2010 in some districts) — actual RPT bills can be a small fraction of "what you'd expect at 2 % of market."
- **RA 12001 (RPVARA) changed that update route** (2026-08-07): a Schedule of Market Values (SMV) now clears a **BLGF regional 45-day → central 30-day review → DOF 30-day certification** chain, takes effect **15 days after publication**, and is then generally revised **every 3 years** (BLGF MC 001.2026, 6 Jan 2026). The statutory SMV-updating deadline of **5 Jul 2026** (IRR §41 of BLGF MC 001.2025) has **lapsed**, so a given LGU may still be on its old schedule — ask the assessor whether a **certified** SMV is in force before modelling the RPT base, and note the **6 % first-year cap** on the increase (§ Future risk below).

**Worked example** (Makati condo, market 12M PHP, assessor FMV 8M): assessed value = 8M × 20 % = 1.6M; basic RPT (1.0 %) = 16,000 + SEF (1.0 %) = 16,000 → **PHP 32,000/yr (~ USD 560)**.

**Discounts**: many LGUs grant 10–20 % prompt-payment discount for full annual by 31 March (per ordinance). **Filing**: bills issued by City/Municipal Treasurer; due quarterly (31 Mar / 30 Jun / 30 Sep / 31 Dec) or lump sum.

### Transaction taxes (one-time at purchase, paid at title transfer)

| Tax | Rate | Base | Who pays | Payable to |
|---|---|---|---|---|
| **Capital Gains Tax (CGT)** | **6 %** | Higher of: gross selling price, BIR zonal value, or assessor FMV | **Seller** (NIRC §24(D)) | BIR — within 30 days of sale, BIR Form 1706 |
| **Documentary Stamp Tax (DST)** | **1.5 %** | Higher of GSP, BIR zonal, or FMV | Convention: buyer (statutorily either party) | BIR — within 5 days of close of month, Form 2000-OT |
| **Local Transfer Tax** | **0.50 % (provinces)** / **0.75 % (cities + Metro Manila municipalities)** of the higher of GSP / FMV | Buyer (convention) | LGU Treasurer — within 60 days of execution |
| **Registration Fee (LRA / RD)** | Per LRA fee schedule — graduated, **~0.25 %** of value (commonly cited "PHP 8,796 + 0.0025 × (value − 1.7M)" type formula) | Buyer | RD with jurisdiction over the property |
| **IT/Notarial fees** (Deed of Absolute Sale notarisation) | **1–2 % of value** typical (negotiable; some lawyers flat-fee) | Buyer | Notary / law firm |
| **Broker's commission** | **3–5 %** typical (residential resale); 5–10 % on developer pre-selling | Seller | Licensed broker |

> **Source for CGT + DST**: National Internal Revenue Code (NIRC) of 1997 as amended by **TRAIN Law (RA 10963, 2017)** §6, §57 (CGT), §174–§201 (DST). Bureau of Internal Revenue: `https://www.bir.gov.ph/`.

> **Note on CGT terminology**: in Philippine tax law, the "Capital Gains Tax" on real property is a **flat 6 % on the GROSS** (selling price or zonal/FMV), **not** on the gain. It is a transaction tax in substance, despite its name.

**Worked example** — foreign buyer of a PHP 12M Makati condo (zonal 11M, FMV 8M); tax base = max = 12M:

- CGT (seller, 6 %) = 720,000 (sometimes negotiated to buyer)
- DST (buyer, 1.5 %) = 180,000 · LTT (Makati 0.75 %) = 90,000 · LRA registration ~0.25 % ≈ 30–35,000 · notarial 1.5 % ≈ 180,000 (often flat 30–60,000)
- **Buyer-side excl. CGT** ≈ 480,000 PHP (≈ 4.0 % of price). **If buyer absorbs CGT** ≈ 1,200,000 PHP (≈ 10 % all-in).

### VAT on real property (developer sales)

- **Sales by VAT-registered developers**: per **BIR RR 1-2024 effective 1 January 2024** (2026-05-27 verified), the residential-lot separate VAT exemption was **REMOVED** (residential lot now VAT-able regardless of price, subject to general VAT registration thresholds at PHP 3,000,000 turnover); house-and-lot / other residential dwellings are **VAT-exempt up to PHP 3,600,000 sale price** (raised from prior PHP 3,199,200 CPI-tracked floor) — dwellings **above PHP 3,600,000 are subject to 12 % VAT**. Source: BIR RR 1-2024 + NIRC §109(P) `https://www.bir.gov.ph/`.
- Pre-selling units typically include VAT in the quoted price (verify "VAT-inclusive" vs "VAT-exclusive" in the contract).

### Inheritance & donor's tax (TRAIN Law)

- **Estate Tax** (post-TRAIN): flat **6 %** on the net estate above PHP 5,000,000 standard deduction (per heir, with family-home deduction up to PHP 10,000,000). NIRC §84–§97 as amended.
- **Donor's Tax** (post-TRAIN): flat **6 %** on donations above PHP 250,000/yr per donor (regardless of relationship).

### Future risk

- **Real Property Valuation Reform Act (RA 12001, signed 13 Jun 2024)** — mandates a uniform valuation standard for the schedules of market values (SMVs) across LGUs, with a transitional revaluation programme run by DOF/BLGF. The statutory SMV-updating deadline was **5 Jul 2026** (IRR §41 of BLGF MC 001.2025) and has now **lapsed** (status as at 2026-08-07). Certified SMVs roll out via a **BLGF regional 45-day → central 30-day review → DOF 30-day certification** chain, take effect **15 days after publication**, and are then generally revised **every 3 years** (BLGF MC 001.2026, 6 Jan 2026).
  - **Bill shock is deferred and phased, not immediate**: the RPT increase in the **FIRST year** of an approved SMV is capped at **6 % of the pre-RPVARA RPT, per tax type** (RA 12001 Sec. 29 Transitory Guidelines), and the LGU **sanggunian may cap or phase later years by ordinance**. **RPT base recalibration** in long-stale jurisdictions (Manila, Cebu City) therefore arrives over several cycles rather than in one bill — verify the LGU's certified SMV and any phasing ordinance with the city/provincial assessor + treasurer.
  - The RA 12001 **RPT amnesty window closed 5 Jul 2026** — no longer available.
  - **Suspension pending (secondary sources)**: in Aug 2026 the President asked Congress to suspend RA 12001. On 23 Sep 2026 the Palace said he supports temporarily suspending real property valuation increases, that DOF is acting (action unspecified), and that Congress would need to act (GMA News + BusinessWorld, 2026-09-23). As of 2026-09-24 no suspension statute or DOF/BLGF issuance has been verified from a primary source. Check with the BLGF/DOF and the LGU assessor whether a new SMV is being applied or held.
  - Sources: RA 12001 full text `https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/97502` · BLGF `https://blgf.gov.ph/` · Official Gazette `https://www.officialgazette.gov.ph/`.
- **Ease of Paying Taxes Act (RA 11976, 2024)** — simplifies BIR filing/payment; no rate change.
- **CREATE MORE (RA 12066, 2024)** — investment incentives; tangential to residential.

### Confidence

**HIGH** for the statutory framework (RA 7160, NIRC, TRAIN, RA 12001 are authoritative) and for the RA 12001 rollout mechanics + 6 % first-year cap (re-verified 2026-08-07 against RA 12001 Sec. 29 Transitory Guidelines + BLGF MC 001.2026). **MEDIUM** for current effective RPT (city ordinances vary; verify per LGU). **MEDIUM** for the assessed-value impact of RA 12001 revaluation **in any specific LGU** — SMV certification is per-LGU and still rolling out after the 5 Jul 2026 deadline lapsed.

---

## Section: `--rental`

### Long-term residential rental income tax

**Personal income tax (PIT) — National Internal Revenue Code §24** rental income (post-TRAIN brackets, effective 2023 onwards):

| Annual taxable income (PHP) | Rate |
|---|---|
| ≤ 250,000 | exempt |
| 250,001–400,000 | 15 % of excess over 250,000 |
| 400,001–800,000 | 22,500 + 20 % of excess over 400,000 |
| 800,001–2,000,000 | 102,500 + 25 % of excess over 800,000 |
| 2,000,001–8,000,000 | 402,500 + 30 % of excess over 2,000,000 |
| > 8,000,000 | 2,202,500 + 35 % of excess over 8,000,000 |

- Source: NIRC §24(A) as amended by TRAIN (RA 10963, 2017) and adjusted by **TRAIN II / TRABAHO/CREATE** for the post-2022 brackets.
- **Non-resident foreigner** (NRA-NETB — non-resident alien not engaged in trade or business in PH): flat **25 %** on Philippine-sourced gross income (NIRC §25(B)). Rental income from PH property to a non-resident foreign owner is taxed at this flat 25 % unless reduced by tax treaty (e.g., US-PH treaty may apply for US persons — verify case-by-case).
- **Resident alien / NRA-ETB**: graduated PIT brackets above.
- **Withholding on rent paid by a corporate tenant**: **5 %** expanded withholding tax on rental payments to the lessor (BIR Form 1601-EQ); creditable against final PIT.
- **VAT on rent**: VAT-able if landlord's gross rentals exceed PHP 3,000,000/yr threshold (TRAIN-adjusted) **AND** the unit's monthly rent exceeds **PHP 15,000** (residential exemption threshold under RA 11534 / RR 9-2018; verify current BIR threshold). Below the threshold: VAT-exempt.

### Short-term rentals (Airbnb / Booking)

**Legal landscape**:

- **No national STR-specific statute** — STR is not directly prohibited at the national level, but layered constraints apply.
- **Condo project bylaws (House Rules)** are the most binding constraint in practice — many condo corps forbid daily/weekly letting via Master Deed + House Rules. Verify in writing before buying with STR intent.
- **Local ordinances** in Boracay/Malay (post-2018 rehab), Baguio, Tagaytay require LGU + DOT registration as accommodation establishments.
- **DOT accreditation**: properties offering STR to transient guests should be DOT-accredited (`https://www.tourism.gov.ph/`; DOT MC 2022-001 series).
- **BIR**: RMC 65-2012 and successors treat Airbnb-style income as taxable rental — PIT + VAT (> threshold) or 3 % percentage tax under §116 NIRC.

**Practical reality**: Metro Manila premium towers (Rockwell, Shang, Greenbelt, Park Triangle) forbid sub-30-day letting; mid-tier more permissive. Cebu/Mactan variable, beachfront caters to STR. Boracay post-2018 — DOT + LGU accreditation enforced; takedowns occur. Tagaytay/Batangas/La Union variable. El Nido/Coron extensive STR but 2023–2024 LGU enforcement stepped up.

**Tax if legally STR**: graduated PIT (resident) or 25 % flat (NRA-NETB); VAT 12 % if turnover > PHP 3M/yr threshold else 3 % percentage tax (§116 NIRC); LGU business permit required (STR is a lessor-of-real-property business under RA 7160).

### Strategic notes

- **Makati / BGC** long-term ~4–6 % gross (Colliers Q4 2025 condo report); premium-tower House Rules typically forbid STR.
- **Cebu IT Park / Mabolo** ~5–7 % gross (BPO long-stay); STR variable.
- **Mactan beach + Boracay/Palawan** ~7–15 % gross theoretical peak season; high seasonality + DOT-accreditation exposure; many foreign owners use developer-managed pool with hotel licence.
- **Tagaytay** Manila-driven Friday–Sunday demand; ~50 % realistic occupancy; ~5–8 % gross.

### Confidence

**HIGH** for PIT framework and condo House Rules authority (RA 4726 §9). **MEDIUM** for STR enforcement intensity (LGU + political cycle). **MEDIUM** for current BIR VAT thresholds (TRAIN-adjusted; verify).

---

## Section: `--work=<profession>`

### Job platforms

- **JobStreet Philippines** — `https://www.jobstreet.com.ph/` (SEEK group, largest)
- **LinkedIn Philippines** — strong in BPO, tech, finance, multinationals
- **Kalibrr** — `https://www.kalibrr.com/` (Manila-grown, tech-skewed)
- **Indeed Philippines** — `https://ph.indeed.com/`
- **OnlineJobs.ph** — Filipino virtual-assistant / outsourcing focused
- **DOLE PhilJobNet** — `https://philjobnet.gov.ph` (government-managed; SMEs)
- **Glassdoor Philippines** — pay benchmarks (small sample for niche roles)

### Work permit & visa

**Foreign nationals working in the Philippines require an Alien Employment Permit (AEP)** from **DOLE (Department of Labor and Employment)** + a corresponding work visa from the **Bureau of Immigration**. Source: DOLE Department Order 221-21 (`https://www.dole.gov.ph/`) and BI `https://immigration.gov.ph/`.

**Key visa categories for foreign workers/investors**:

| Visa | Statutory basis | When |
|---|---|---|
| **9(g) Pre-Arranged Employment** | Commonwealth Act 613 (Philippine Immigration Act, 1940) §9(g) | Standard work visa; AEP-linked; renewable |
| **9(d) Treaty Trader / Investor** | §9(d) | Nationals of countries with reciprocal trade treaty (US, Japan, Germany, etc.) — substantial trade or investment |
| **47(a)(2) Special Visa** | EO 226 + BOI rules | Employees of PEZA / BOI-registered enterprises |
| **SVEG** | Special Visa for Employment Generation | Foreigners employing ≥ 10 Filipinos |
| **SRRV** | EO 1037 (PRA) | Long-stay retiree; **no automatic work right** (separate AEP needed) |
| **SIRV** | EO 226 Book III | Investor in BOI-qualifying enterprise (≥ USD 75k); separate AEP for active work |

**Restricted occupations under Anti-Dummy Law CA 108 §2-A and Constitution**: practice of regulated professions (law, medicine, engineering, accountancy, architecture, etc.) is reserved for Filipino citizens with limited reciprocity exceptions. Source: PRC (Professional Regulation Commission) `https://www.prc.gov.ph/`.

**Mass media + advertising**: 100 % Filipino-owned (constitutional bar Art. XVI §11 for mass media; PD 1018 for advertising — though RA 11647 partially relaxed advertising).

**Retail trade**: **RA 11595 (2021)** lowered the foreign-equity threshold to allow 100 % foreign-owned retail enterprises with paid-up capital ≥ USD 250,000.

**Public utilities**: **RA 11659 (2022)** narrowed the constitutional definition of "public utility" — telcos, transportation networks, power distribution etc. opened up to foreign equity (subject to specific caps).

### Self-employment / freelance reality

- Foreigner doing freelance work for **foreign clients** while in PH on a long-stay visa operates in a grey zone — strictly an AEP is required for any "gainful employment," but enforcement against purely-remote-work-for-foreign-employers is limited.
- **Tax**: foreigner resident > 180 days/yr is taxed on **Philippine-sourced** income only (NRA-ETB / resident alien); foreign-source income generally **not taxed** in PH (territorial-leaning regime for individuals — verify case-by-case with a Philippine CPA; US/UK persons have separate home-country taxation).
- **No "auto-entrepreneur" simple regime**: registered PH business needs SEC/DTI + BIR + LGU permits + AEP.

### Salary benchmarks (Metro Manila 2025–2026)

| Role | Median monthly gross PHP | USD est. (57 PHP/USD) |
|---|---:|---:|
| Software engineer (mid-senior, MNC) | 80,000–200,000 | $1,400–$3,510 |
| BPO team lead / mid manager | 50,000–120,000 | $880–$2,100 |
| English ESL tutor (online) | 25,000–60,000 | $440–$1,050 |
| Hotel mgmt (mid) | 40,000–90,000 | $700–$1,580 |
| Metro Manila median (all sectors) | ~22,000 | ~$390 |
| **Minimum wage 2026 NCR (non-agri)** | ~17,440/mo (**PHP 695/day** × 25.08, per **RTWPB-NCR Wage Order 26, effective 18 Jul 2025** — agri/service-retail ≤15 + small manufacturing <10: PHP 658/day; 2026-05-27 verified) | ~$305 |

Sources: PSA Labor Force Survey `https://psa.gov.ph/`, JobStreet Salary Report 2024-2025, RTWPB Wage Orders (per regional Tripartite Wages and Productivity Board).

### Confidence

**HIGH** for visa and AEP framework (BI / DOLE / BOI primary). **HIGH** for restricted-profession list (Constitution + PRC + sector statutes). **MEDIUM** for salary benchmarks (large MNC vs SME variance; BPO-skewed national data).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **NDRRMC (National Disaster Risk Reduction and Management Council)** | `https://www.ndrrmc.gov.ph/` | Hazard situational reports, disaster history, advisories |
| **PHIVOLCS (Philippine Institute of Volcanology and Seismology)** | `https://www.phivolcs.dost.gov.ph/` | Earthquake & volcano hazard maps, active fault map, tsunami |
| **PAGASA (Philippine Atmospheric, Geophysical and Astronomical Services Administration)** | `https://www.pagasa.dost.gov.ph/` | Typhoon tracks, climate, monsoon, climate-projection products |
| **MGB (Mines and Geosciences Bureau)** | `https://www.mgb.gov.ph/` | Geo-hazard maps (landslides, ground subsidence) |
| **DENR (Dept of Environment & Natural Resources)** | `https://www.denr.gov.ph/` | Environmental clearances, ECC, protected areas |
| **DENR-EMB Air Quality Management** | `https://emb.gov.ph/` | Air-quality monitoring (Manila and major cities) |
| **HazardHunterPH** | `https://hazardhunter.georisk.gov.ph/` | DOST geo-portal — parcel-level hazard lookup (seismic, volcanic, hydromet) |
| **Project NOAH** (UP Resilience Institute, partial archive) | `https://noah.up.edu.ph/` | Flood & landslide mapping (university-led, archive maintained) |
| **CCC (Climate Change Commission)** | `https://climate.gov.ph/` | National Climate Change Action Plan, climate-vulnerability assessments |

### Typhoon / tropical cyclone (bagyo)

- **Most typhoon-exposed country in the world**: ~20 tropical cyclones enter the Philippine Area of Responsibility (PAR) annually; ~8–9 make landfall (PAGASA `https://www.pagasa.dost.gov.ph/`).
- **Major landfalls since 2010**: Yolanda/Haiyan 2013 (~6,300 deaths, USD 5.8B losses per NDRRMC + World Bank), Pablo/Bopha 2012, Lawin 2016, Ompong/Mangkhut 2018, Odette/Rai 2021 (Visayas + Palawan), Karding 2022, Kristine/Trami 2024.
- **Regional exposure**: 🔴 Eastern seaboard (E Samar, N Samar, Catanduanes, Camarines, Quezon, Aurora, Isabela, Cagayan) — direct Pacific landfall, peak Aug–Nov · 🟠 Visayas south + Bicol + Palawan — indirect tracks (Odette devastated Cebu/Bohol/Siargao/Palawan 2021) · 🟡 Metro Manila + Central Luzon — typhoon flooding (Ondoy 2009) + west-Sierra Madre landslide · 🟢 Davao + Mindanao south — mostly outside the typhoon belt.
- **Build-code response**: NSCP wind-load revised 2010 + 2015 (NSCP 2015) reflects post-Yolanda lessons. Pre-2010 light-construction housing is typically not Yolanda-resilient.

### Earthquake (lindol)

- PH sits on the **Pacific Ring of Fire**; multiple active faults + subduction zones.
- **Major active faults**: Philippine Fault Zone (Luzon → Leyte → Mindanao), Marikina Valley Fault System (the "**Big One**" — PHIVOLCS GMMA Risk Analysis projects M 7.2 worst case for Metro Manila), West Valley Fault, Lubang Fault.
- **Recent significant events**: M 7.0 Bohol 2013 (~220 deaths), M 6.5 Surigao 2017, M 6.7+6.5+6.6 Mindanao triple-quakes 2019, M 7.0 Luzon (Abra) 2022, M 6.9 Mindanao 2023.
- **Metro Manila high-rise scrutiny**: National Building Code (PD 1096, 1977) + NSCP 2015 seismic provisions. Pre-2000 buildings have variable compliance; post-2017 buildings designed to NSCP 2015 (more conservative). **Verify construction date + compliance cert for any high-rise.**
- Use **HazardHunterPH** (`https://hazardhunter.georisk.gov.ph/`) per-coordinate for seismic / volcanic / hydromet hazard.

### Volcanic, flood, landslide, storm surge

- **Volcanic** — 24 active volcanoes per PHIVOLCS. Key for buyers: **Taal** (Batangas; erupted Jan 2020 — Tagaytay ridge is downstream of any future eruption; PDZ 7 km), **Mayon** (Albay; PDZ 6 km — Legazpi in southern fan), **Pinatubo / Bulusan / Kanlaon / Hibok-Hibok** active with localised exclusion zones, **Apo / Banahaw** dormant but classified active.
- **Flood** — Metro Manila chronic urban flooding from monsoon (habagat) + typhoons; Pasig/Marikina/Tullahan basins regularly inundate Marikina, Pasig, Cainta, Taguig riverside, lower Manila. **Ondoy (2009)** reference event: 455 mm in 12 hr (PAGASA), ~700 deaths. Provincial: Cagayan Valley, Pampanga delta, Cotabato basin, Agusan basin seasonally inundated. Project NOAH archive: `https://noah.up.edu.ph/`.
- **Landslide** — high on Cordillera (Baguio, Benguet) and Eastern Samar/Leyte slopes after intense rainfall. Cherry Hills (Antipolo) 1999 reference event. MGB geo-hazard maps for landslide-prone barangays.
- **Storm surge** — post-Yolanda 2013 (5–7 m surge Tacloban Bay), PAGASA + NAMRIA + DOST mapped inundation zones for Pacific-facing coasts (HazardHunterPH lookup). 🔴 Coastal villas/condos in storm-surge zones: budget structural elevation + cyclone-rated openings.

### Build-era hazards

| Era | Hazards |
|---|---|
| Pre-1977 (no NBC) | Variable structural; informal additions; lead pipes; asbestos in roofing/cement sheets |
| 1977–1992 (NBC PD 1096 + initial NSCP) | Typhoon-resistance variable; many low-rise not engineered |
| 1992–2010 (NSCP 1992/2001) | Improved wind/seismic; pre-Yolanda cyclone classifications under-conservative |
| Post-2015 (NSCP 2015) | Stricter wind/seismic post-Yolanda; enforcement variable |
| Post-2020 (DHSUD Act) | DHSUD Licence to Sell for new condos — verify before buying pre-selling |

### Mandatory pre-purchase diagnostics

| Document | Required because | Where |
|---|---|---|
| **Certified True Copy of TCT/CCT** (current owner's title) | Verify the chain of title; encumbrances annotated on Memorandum of Encumbrances | RD via `https://eserbisyo.lra.gov.ph/` |
| **Tax Declaration** (real property + improvements) | Confirms LGU's view of FMV; needed for RPT history | City/Provincial Assessor's Office |
| **RPT clearance (latest)** | Confirms no unpaid Real Property Tax | City/Municipal Treasurer |
| **HOA / Condo dues clearance** | Confirms no unpaid condo / homeowner dues | Condo corp / HOA secretary |
| **Foreign Ownership Certification** (condo, foreign buyer) | Confirms unit is within the 40 % foreign quota | Condo corp secretary |
| **DHSUD Licence to Sell** (pre-selling unit) | Confirms developer is licensed; pre-selling without LTS is illegal under PD 957 | DHSUD or developer |
| **Building Permit + Occupancy Permit** | Confirms legal construction + occupancy | LGU Office of the Building Official |
| **Zoning Certificate** | Confirms permitted use (residential / commercial / mixed) | LGU Zoning Office |
| **HazardHunterPH report** | Per-parcel hazard assessment | `https://hazardhunter.georisk.gov.ph/` |
| **Tax Identification Number (TIN)** + BIR transfer documents | CGT/DST filing requires both parties' TINs | BIR RDO with jurisdiction |

**Foreign buyers should commission a Philippine real-estate lawyer for the title verification and BIR/RD transfer execution — DIY is feasible (English-language records) but procedural complexity at the BIR + RD warrants counsel.**

### Confidence

**HIGH** for typhoon + earthquake + volcanic exposure (PHIVOLCS + PAGASA + NDRRMC primary). **HIGH** for HazardHunterPH parcel-level lookup availability. **MEDIUM** for build-era enforcement (NSCP variable enforcement historically). **HIGH** for mandatory diagnostics (LRA + BIR + DHSUD framework codified).

---

## Section: `--mains`

### Water supply

- **Metro Manila**: **Manila Water** (East Zone — Makati, Pasig, BGC, Marikina, Eastern Manila) and **Maynilad Water Services** (West Zone — Quezon City western, Caloocan, Manila CBD west, Las Piñas, Cavite north). Concession agreements administered by **MWSS (Metropolitan Waterworks and Sewerage System Regulatory Office)** under the National Government. Sources: `https://www.manilawater.com/`, `https://www.mayniladwater.com.ph/`, `https://mwss.gov.ph/`.
- **Cebu**: **MCWD (Metro Cebu Water District)** — `https://www.mcwd.gov.ph/`.
- **Davao**: **DCWD (Davao City Water District)** — `https://www.davao-water.gov.ph/`.
- **Provincial cities + municipalities**: water districts under **LWUA (Local Water Utilities Administration)** — `https://www.lwua.gov.ph/`. ~890 water districts nationally (LWUA 2024 count, verify).
- **Rural barangays**: **Barangay Water and Sanitation Associations (BWSAs)** + **Rural Waterworks and Sanitation Associations (RWSAs)** + private deep wells; quality + reliability variable.

### Sewer / wastewater

**The Philippines has limited mains-sewer coverage compared to OECD baselines.**

- **Metro Manila**: per Manila Water + Maynilad Concession Agreement (extended to 2037 in 2009), the concessionaires committed to expanding sewerage coverage to ~100 % of customers by 2037. **As of 2024 sewerage coverage in Metro Manila is estimated ~25–35 %** (varying by district per MWSS annual report). The remainder uses **on-site sanitation** (septic tank + soakaway); concessionaires offer **periodic septage desludging** included in the water bill (Sanitation Charge, ~20 % of basic water bill).
- **Provincial cities (Cebu, Davao, Iloilo)**: even lower sewerage coverage; mostly on-site.
- **Modern condos**: under the **National Plumbing Code of the Philippines (RA 1378, 1955, latest revision 2020)** + LGU building codes, condos with > 30 units must have **on-site sewage treatment plants (STP)** — common in BGC, Makati, QC towers. The treated effluent discharges to the LGU drainage.
- **Standalone houses**: **septic tank + soakaway** (drain field) is the universal default. Older houses may have simple cesspits — non-compliant with RA 9275 (Clean Water Act 2004).
- **Wastewater regulator**: **DENR-EMB (Environmental Management Bureau)** under the Clean Water Act `https://emb.gov.ph/`. Effluent standards in DAO 2016-08.

### Verification path

1. **Listing language**: "connected to MWSS/Manila Water/Maynilad sewerage" = mains sewerage (rare) · "with STP / central sewage treatment plant" = on-site condo treatment · "with septic tank" = septic + soakaway · "deep well" = private well, not LWUA piped.
2. **Metro Manila**: call Manila Water (1627) or Maynilad (1626) for sewerage-area confirmation.
3. **Provincial city**: local water district (LWUA list `https://www.lwua.gov.ph/`) for water; LGU City Engineer / Office of the Building Official for sewerage.
4. **Standalone house**: assume septic; request Sanitary Permit + most recent desludging receipt from seller; verify soakaway is functional (no standing water, no smell).

### Cost benchmarks (est., PH 2026; contractor / installer quotes vary — verify per installer)

| Scenario | Cost (PHP) |
|---|---:|
| Standard condo connection / monthly fee (Manila Water / Maynilad water + sewerage) | 700–2,500/mo for typical 2BR usage |
| Condo association dues (incl. STP O&M) | 50–100 PHP/sqm/month |
| Septic tank install (3-stage modern, residential) | 80,000–200,000 |
| Septic desludging (Manila Water Sanitation Charge auto / standalone vacuum truck) | included in water bill (~20 %) / 3,000–7,000 standalone |
| Deep well install (60–100 m, residential) | 80,000–250,000 |
| Sewer-line connection (where mains sewerage available) | 10,000–40,000 + monthly sewerage charge |
| Mains water connection (new MWSS / LWUA) | 5,000–20,000 |

### Confidence

**HIGH** for Manila Water / Maynilad / MWSS + LWUA institutional structure. **MEDIUM** for parcel-level coverage (sewerage particularly variable; verification often requires telephone the local water district / city engineer).

---

## Cost benchmarks (PH 2026)

| Item | Cost (PHP) | USD est. (57 PHP/USD) |
|---|---:|---:|
| **Lawyer fees (foreign buyer condo)** | 50,000–150,000 (or 1–1.5 % of price) | $880–$2,630 |
| **Lawyer fees (foreign buyer villa, lease structure)** | 100,000–400,000 (more complex) | $1,750–$7,020 |
| **Title verification (LRA CTC + RD search)** | 1,500–5,000 | $26–$88 |
| **Building inspector (condo)** | 5,000–20,000 | $88–$350 |
| **Building inspector (villa)** | 15,000–60,000 | $260–$1,050 |
| **Capital Gains Tax (seller, often borne by buyer in foreign transactions)** | 6 % of higher of GSP / zonal / FMV | varies |
| **Documentary Stamp Tax** | 1.5 % | varies |
| **Local Transfer Tax (city)** | 0.75 % | varies |
| **Local Transfer Tax (province)** | 0.50 % | varies |
| **LRA registration fee** | est. ~0.25 % of value | varies |
| **Notarial fees** | 1–2 % typical (negotiable to flat) | varies |
| **Broker's commission (resale)** | 3–5 % (seller pays) | varies |
| **Broker's commission (developer pre-selling)** | 5–10 % (developer pays) | varies |
| **Condo dues (mid-range Makati/BGC)** | 50–100 PHP/sqm/month | $0.90–$1.75/sqm/mo |
| **Condo dues (luxury BGC tower)** | 100–200 PHP/sqm/month | $1.75–$3.50/sqm/mo |
| **Sinking fund (one-off, at handover)** | 500–2,000 PHP/sqm | $9–$35/sqm |
| **Annual RPT (Makati condo, 12M PHP value)** | ~30,000 PHP | ~$525 |
| **Typical 60-sqm condo full refurb** | 600,000–1,800,000 | $10,500–$31,600 |
| **Total transaction cost (foreign buyer, all-in if seller pays CGT)** | ~4–5 % of price | — |
| **Total transaction cost (foreign buyer, all-in if buyer absorbs CGT)** | ~10–11 % of price | — |

---

## Active fiscal incentives (2026)

- **PEZA (Philippine Economic Zone Authority)** — `https://www.peza.gov.ph/`. Foreign-owned export enterprises in PEZA-registered economic zones enjoy income tax holiday (4–7 yrs) → 5 % gross income tax in lieu of all national + local taxes (legacy regime; modified by CREATE/CREATE MORE). **Land in a PEZA zone is leased to the enterprise (not owned)** — typically PEZA-administered or private estate. Residential property is NOT eligible for PEZA incentives.
- **BOI (Board of Investments)** — `https://boi.gov.ph/`. Investment Priorities Plan (IPP) registration → income tax holiday + capex deductions. Residential real-estate generally NOT in the IPP (some mass-housing exceptions).
- **CREATE Act (RA 11534, 2021)** + **CREATE MORE (RA 12066, 2024)** — corporate income tax 25 % (or 20 % for SMEs), PEZA/BOI rationalized incentives. Source: `https://www.officialgazette.gov.ph/`.
- **REIT Act (RA 9856)**: REIT income distributed to shareholders is deductible at the REIT level → near-zero corporate tax on distributed income; minimum 90 % distribution required. Source: SEC + PSE.
- **SRRV Discounts**: PRA's accreditation network gives ~15 % discount on certain hotel / hospital / domestic-airline services (verify at PRA partners list).
- **No Philippine "golden visa" tied to a residential real-estate purchase** — SRRV is the closest but the deposit is held in PRA-accredited bank or convertible to property; SIRV requires equity in an operating enterprise.

---

## Common listing platforms

- **Lamudi Philippines** — `https://www.lamudi.com.ph/` — broad nationwide
- **MyProperty.ph** — `https://www.myproperty.ph/` (Lamudi group)
- **Property24 Philippines** — `https://www.property24.com.ph/`
- **Dot Property Philippines** — `https://www.dotproperty.com.ph/`
- **OnePropertee** — `https://www.onepropertee.com/`
- **Hoppler** — `https://www.hoppler.com.ph/` (Metro Manila premium)
- **Carousell Property** — `https://www.carousell.ph/`
- **Rent.ph / Pinoy Listings** — long-tail
- **Developer direct sites**: Ayala Land `https://www.ayalaland.com.ph/`, Megaworld `https://www.megaworldcorp.com/`, SMDC `https://smdc.com/`, DMCI Homes `https://dmcihomes.com/`, Robinsons Land `https://www.robinsonsland.com/`.

---

## Caveats unique to PH

- **Constitutional foreign-land bar is unmoving** — Art. XII §7 has stood since 1987; multiple Charter Change attempts (2003, 2006, 2014, 2018, 2024) failed. Do not assume liberalisation is imminent.
- **CCT within 40 % foreign quota is the only safe freehold** — get the Foreign Ownership Certification in writing BEFORE any deposit.
- **Residential land lease structurally weaker than RA 7652 investor lease** — RA 7652 50+25 yrs is for business investors; residential lease falls under Civil Code Art. 1643 (cap 99 yrs) with patchy enforceability.
- **Anti-Dummy Law is criminal, not just civil** — 60/40 corporation structures are prosecuted. Do not assume historical "everyone does it" still applies.
- **Pre-selling completion risk** — historically notable share of projects faced delayed handover or cancellation; verify developer track record + DHSUD Licence to Sell + escrow under PD 957.
- **Typhoon Aug–Nov + earthquake background** — combine with HazardHunterPH parcel report; budget typhoon-rated openings + NSCP 2015-compliant construction.
- **Volcanic PDZ** (Taal, Mayon, Kanlaon) — never buy within the Permanent Danger Zone regardless of view.
- **Metro Manila "Big One"** (Marikina Valley Fault) — prefer post-NSCP 2015 high-rises; verify compliance certification.
- **Storm-surge exposure** for coastal property post-Yolanda: structural elevation + cyclone-rated openings essential.
- **Sewerage coverage low** outside Metro Manila core; assume septic + budget desludging.
- **VAT on developer sales** above threshold — verify "VAT-inclusive" vs "VAT-exclusive": a "VAT-exclusive PHP 12M" condo is PHP 13.44M all-in.
- **RA 12001 RPT recalibration** — long-stale assessor schedules (Manila, Cebu City) likely to rise, but **phased**: the first year under an approved SMV is capped at **6 % of pre-RPVARA RPT per tax type** (RA 12001 Sec. 29) and the sanggunian may phase later years. The 5 Jul 2026 SMV-updating deadline has lapsed (2026-08-07) — check whether the LGU's SMV is DOF-certified yet, and whether the proposed RA 12001 suspension has been enacted (President's Aug 2026 request to Congress; Palace backing 23 Sep 2026 — secondary sources, no primary instrument verified as of 2026-09-24).
- **All transaction taxes stack** (unlike Thailand SBT vs stamp): 6 % CGT + 1.5 % DST + 0.5–0.75 % LTT + ~0.25 % registration + 1–2 % notarial all apply on the same sale.
- **English-language records** — title, Deed of Absolute Sale, BIR forms all English; no sworn translation needed.

---

## Reddit / forum sources

- **r/Philippines** — active general
- **r/PinoyProgrammer** — Manila tech / BPO context
- **r/Manila**, **r/Cebu**, **r/davao** — city-specific
- **r/expats** — cross-country comparisons; SRRV / SIRV threads
- **PinoyExchange.com** — long-running Filipino forum, real-estate sub-forum
- **Sulit.ph** (legacy property listings, now Carousell)
- **Living in the Philippines / Live in the Philippines forums**
- ⚠️ Forum-quality caveat: many anecdotes about "my friend bought through a 60/40 corporation and it was fine" — but the legal exposure has not changed; treat older posts with care. The Anti-Dummy Law is criminal-grade.

---

## Verification authorities

| Authority | When to call |
|---|---|
| **LRA + RD** | Title verification, CTC, encumbrances, transfer registration — `https://www.lra.gov.ph/`, `https://eserbisyo.lra.gov.ph/` |
| **BIR** | CGT/DST/VAT, zonal lookup, transfer tax payment — `https://www.bir.gov.ph/` |
| **City/Provincial Assessor + Treasurer** | Tax Declaration, FMV, RPT bill + clearance — per LGU |
| **DHSUD** | Pre-selling Licence to Sell, condo / subdivision regulation, HOA disputes — `https://dhsud.gov.ph/` |
| **PRA** | SRRV categories, deposit, real-estate conversion — `https://pra.gov.ph/` |
| **BOI** | SIRV + IPP + 47(a)(2) visa — `https://boi.gov.ph/` |
| **BI · DOLE · SEC · DOJ** | Visas + AEP + corp registration + Anti-Dummy enforcement — `https://immigration.gov.ph/`, `https://www.dole.gov.ph/`, `https://www.sec.gov.ph/`, `https://doj.gov.ph/` |
| **BSP** | Inward remittance, FX rules, RREPI — `https://www.bsp.gov.ph/` |
| **PHIVOLCS + HazardHunterPH** | Quake/volcano + parcel hazard — `https://www.phivolcs.dost.gov.ph/`, `https://hazardhunter.georisk.gov.ph/` |
| **PAGASA · NDRRMC · DENR-EMB · MGB** | Typhoon/climate, disaster history, environment, geo-hazard — `https://www.pagasa.dost.gov.ph/`, `https://www.ndrrmc.gov.ph/`, `https://emb.gov.ph/`, `https://www.mgb.gov.ph/` |
| **PSA** | Population, demographics, PSGC — `https://psa.gov.ph/` |

---

## Quirks to know

- **OCT → TCT → CCT chain**: TCT on land traces back to OCT (mother title). For any land purchase, request the full chain of TCTs back to the OCT + decree of registration / patent — gaps in the chain are the most common dummy-title scam vector. CCT applies only to condo units + undivided interest in common areas (the only Torrens title a foreigner may hold).
- **Mother title vs derivative title**: subdivision creates derivative TCTs partially cancelling the mother title — verify the derivative TCT references the correct parent + the subdivision plan was LRA-approved.
- **Tax Declaration ≠ title**: rural transactions often advertised on Tax Declaration alone — reject. Only Torrens (OCT/TCT) confers ownership.
- **CARP agrarian-reform notations** (RA 6657): agricultural land may bear DAR annotations prohibiting transfer to non-farmer-beneficiaries or capping at 5-ha retention. Foreigners cannot own agricultural land at all (conversion to non-agri required first).
- **Free Patent / Homestead Patent** (CA 141 Public Land Act): 5-yr prohibition on alienation + additional restrictions; verify before purchase.
- **Adverse possession**: registered Torrens land cannot be acquired by adverse possession (PD 1529 §47) — a key strength of the system. (Unregistered land can still be acquired by 30-yr possession.)
- **Condo corp governance** (RA 4726 §9): non-stock corp governed by by-laws; foreign owners have AGM voting rights (proportionate to floor area/share) but cannot serve as directors unless the master deed permits foreigner directors AND foreign equity ≤ 40 %.
- **HOA for subdivisions**: governed by RA 9904 (Magna Carta for Homeowners and HOAs, 2010); HOA dues + assessments enforceable against title.
- **BIR zonal vs assessor FMV vs market**: three different numbers, three uses. Zonal = CGT/DST tax-base floor (BIR). Assessor FMV × assessment level = RPT base (LGU). Market = what you pay.
- **Top-5 developers** (Ayala, Megaworld, SMDC, DMCI, Robinsons) dominate publicly listed developer space — pre-selling from a top-5 carries less completion risk than from a small unbranded developer.

---

## Source URL templates

| Source | URL |
|---|---|
| LRA + eSerbisyo CTC | `https://www.lra.gov.ph/` · `https://eserbisyo.lra.gov.ph/` |
| BIR + Zonal Values | `https://www.bir.gov.ph/` · `https://www.bir.gov.ph/index.php/zonal-values.html` |
| Official Gazette · Senate · SC e-Library | `https://www.officialgazette.gov.ph/` · `https://legacy.senate.gov.ph/` · `https://elibrary.judiciary.gov.ph/` |
| BSP · RREPI · FX rules | `https://www.bsp.gov.ph/` · RREPI `…/MediaAndResearch/RREPI.aspx` · FX `…/Pages/Regulations/FXRegulations.aspx` |
| PSA + PSGC | `https://psa.gov.ph/` · `https://psa.gov.ph/classification/psgc` |
| DHSUD · PRA SRRV · BOI · BOI SIRV · BOI FINL | `https://dhsud.gov.ph/` · `https://pra.gov.ph/srrv/` · `https://boi.gov.ph/` · `…/special-investors-resident-visa/` · `…/foreign-investments-negative-list/` |
| BI · DOLE · SEC · DOJ | `https://immigration.gov.ph/` · `https://www.dole.gov.ph/` · `https://www.sec.gov.ph/` · `https://doj.gov.ph/` |
| PHIVOLCS · HazardHunterPH · PAGASA · NDRRMC | `https://www.phivolcs.dost.gov.ph/` · `https://hazardhunter.georisk.gov.ph/` · `https://www.pagasa.dost.gov.ph/` · `https://www.ndrrmc.gov.ph/` |
| DENR-EMB · MGB · CCC · Project NOAH archive | `https://emb.gov.ph/` · `https://www.mgb.gov.ph/` · `https://climate.gov.ph/` · `https://noah.up.edu.ph/` |
| MWSS · Manila Water · Maynilad · LWUA · MCWD · DCWD | `https://mwss.gov.ph/` · `https://www.manilawater.com/` · `https://www.mayniladwater.com.ph/` · `https://www.lwua.gov.ph/` · `https://www.mcwd.gov.ph/` · `https://www.davao-water.gov.ph/` |
| MMDA · DPWH · DOTr · DOT · BLGF · PRC | `https://www.mmda.gov.ph/` · `https://www.dpwh.gov.ph/` · `https://dotr.gov.ph/` · `https://www.tourism.gov.ph/` · `https://blgf.gov.ph/` · `https://www.prc.gov.ph/` |
| Listing platforms | Lamudi `https://www.lamudi.com.ph/` · MyProperty `https://www.myproperty.ph/` · Property24 `https://www.property24.com.ph/` · Dot Property `https://www.dotproperty.com.ph/` · OnePropertee `https://www.onepropertee.com/` · Hoppler `https://www.hoppler.com.ph/` |
| Top developers | Ayala Land `https://www.ayalaland.com.ph/` · Megaworld `https://www.megaworldcorp.com/` · SMDC `https://smdc.com/` · DMCI `https://dmcihomes.com/` |

---

## Status

✅ **Fully populated** as of 2026-05-01.

**Coverage check**: foreign-buyer eligibility (LEAD), price, traffic, tax, rental, work, risks, mains all sourced to primary government / regulated entity URLs + cost benchmarks + caveats.

**Confidence**: HIGH — Constitution Art. XII §7, RA 4726 (Condominium Act), RA 7652 (Investors' Lease Act), CA 108 (Anti-Dummy Law), RA 7160 (LGC + RPT), NIRC + TRAIN (CGT/DST), PD 1529 (Property Registration Decree), RA 11534 + RA 12066 (CREATE / CREATE MORE), RA 12001 (Real Property Valuation Reform), PRA SRRV circulars, BOI SIRV (EO 226), PHIVOLCS + PAGASA + NDRRMC for hazards — all primary statute or agency sources. **MEDIUM** for SRRV deposit-category amounts (PRA periodically restructures; verify current text); STR LGU-specific enforcement intensity; current effective RPT post-RA 12001 revaluation in long-stale jurisdictions; condo project foreign-quota live status (project-specific; verify in writing per project).

**Reform watch items** (track in `shared/regulatory-watch.md`):
1. **Real Property Valuation Reform Act (RA 12001) implementation** — the 5 Jul 2026 SMV-updating deadline has lapsed (2026-08-07); certified SMVs are still rolling out per LGU through the BLGF/DOF review chain (BLGF MC 001.2026), with the first-year RPT increase capped at 6 % of pre-RPVARA RPT per tax type (Sec. 29). Track certification **per LGU**, not a national date. Also track the proposed **suspension** of RA 12001 (President's Aug 2026 request to Congress; Palace backing 23 Sep 2026, DOF acting, action unspecified — GMA News + BusinessWorld, secondary). No suspension statute or DOF/BLGF issuance has been verified from a primary source.
2. **Charter Change attempts to relax foreign-land bar** — perennial; verify current Congress before quoting any "imminent" change.
3. **CREATE MORE Act (RA 12066) implementing rules** — DOF/BIR Revenue Regulations rolling out 2025–2026.
4. **SRRV category restructuring** — PRA circulars; verify deposit thresholds before client-quote.
5. **Boracay STR licensing model** — whether DOT/LGU expand to other tourist islands.
6. **Bangko Sentral FX Manual updates** — BSP Circular series; affects foreign-buyer remittance documentation.

**Last verified**: 2026-08-07 (`--tax` RA 12001 RPVARA re-verification — 5 Jul 2026 SMV-updating deadline lapsed; BLGF/DOF certification chain + 15-day effectivity + 3-yr general revision per BLGF MC 001.2026; 6 % first-year RPT cap per RA 12001 Sec. 29; RPT amnesty closed 5 Jul 2026). Prior validation sweep 2026-05-27 (BSP RREPI → RPPI rename + URL; SRRV restructure 1 Sept 2025 (Classic+Courtesy USD deposits, age 40-49); VAT exemption PHP 3.6M (BIR RR 1-2024); NCR-26 PHP 695/day Wage Order eff. 18 Jul 2025). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
