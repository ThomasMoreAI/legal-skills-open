# Malaysia 🇲🇾 — Property Due-Diligence Playbook

ISO2: `my`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

> **🇲🇾 LEAD WARNING — read before any other section.** Malaysia is a **moderately restricted** market. Foreigners CAN own freehold residential property in their own name, BUT subject to: (a) a **state-set minimum purchase price** (varies MYR 500,000 – MYR 2,000,000 by state and tier in the table below; Penang landed floors not publicly available), (b) **state authority consent** (Land Office / Menteri Besar / EPU depending on the state and price band), and (c) hard exclusions on **Malay Reserved Land (Tanah Rizab Melayu)**, **Bumiputera-quota lots**, **low/medium-cost housing**, and **agricultural smallholder land**. Land is administered by the 13 states under the **National Land Code 1965 (Act 56)** for Peninsular Malaysia and **separate** Sabah Land Ordinance / Sarawak Land Code regimes for the East Malaysian states. **State variation is the booby-trap**: a Selangor Zone 1–2 threshold (MYR 2,000,000, strata only) is double Kuala Lumpur (MYR 1,000,000) for the same year. Always verify the threshold + consent process at the destination **state Land Office (Pejabat Tanah)** before signing any SPA.

## Country profile

- **Postcode (Poskod)**: 5 digits, format `NNNNN` (e.g., `50450` Kuala Lumpur KLCC, `10250` George Town, `47500` Subang Jaya).
  - First 2 digits ≈ state cluster (`50`–`60` = WP Kuala Lumpur / Putrajaya / Selangor; `10`–`14` = Penang; `40`–`48` = Selangor; `80`–`86` = Johor; `93`–`98` = Sarawak; `88`–`91` = Sabah).
  - Source: Pos Malaysia `https://www.pos.com.my/postal-services/quick-access/?postcode-finder` (verify at official lookup).
- **Admin levels**: 13 negeri (states) + 3 wilayah persekutuan (federal territories: Kuala Lumpur, Putrajaya, Labuan) → 160 daerah (districts) → mukim (subdistricts) → kampung (villages, rural).
  - Source: Department of Statistics Malaysia (DOSM) `https://www.dosm.gov.my/`
- **Currency**: MYR (Malaysian ringgit, RM). 1 USD ≈ 4.4–4.7 MYR; 1 EUR ≈ 4.8–5.1 MYR (Apr 2026 BNM reference; FX volatile, verify at `https://www.bnm.gov.my/exchange-rates`).
- **Languages**: Bahasa Malaysia (official); English widely used in property law, SPA contracts, professional services and developer marketing; Mandarin, Tamil and many Chinese dialects in commerce. **Most title documents (geran) are in Bahasa Malaysia** — sworn translation may be needed for foreign buyers.
- **Cadastre / land registry**: state level via Land and Mines Offices (Pejabat Pengarah Tanah dan Galian Negeri, PTG) and District Land Offices (Pejabat Tanah Daerah, PTD). Federal coordinator **JKPTG** — `https://www.jkptg.gov.my/`. Survey & mapping **JUPEM** — `https://www.jupem.gov.my/`. Online land searches: state **e-Tanah** portals (Selangor `https://etanah.selangor.gov.my/` ⚠️ resolves but refused both probe egresses on 2026-09-18 — treat as unverified, not dead); for the **Federal Territories**, **MyLAND — Sistem Pengurusan Tanah Persekutuan dan Pembahagian Pusaka**, run by **JKPTG** (Kementerian Sumber Asli dan Kelestarian Alam), `https://myland.gov.my/` — **title search requires a registered account**; only eSemakan and ePayment are public. Sabah and Sarawak run independent systems.
- **Title types** (CRITICAL — only freehold and leasehold under registered title are safely transferable to foreigners):

| Code / Term | Description | Foreign use | Notes |
|---|---|---|---|
| **Hakmilik kekal** (Freehold) | Permanent ownership, no expiry | ✅ acceptable | Vast majority of urban residential; price premium 10–30 % vs leasehold |
| **Pajakan negeri** (Leasehold, State Lease) | 30 / 60 / 99-year lease from state, renewable | ✅ acceptable | 99-year is the common form; renewal is by application with premium ≥ 25 % of state market value (varies) |
| **Geran (Mukim / Daerah / FT)** | Title instruments under National Land Code 1965 | ✅ acceptable | Mukim title (rural) and Daerah/FT title (urban); both transferable subject to state consent |
| **Tanah Rizab Melayu** (Malay Reserved Land) | Reserved by the state for Malay nationals | ❌ never | Cannot be transferred to non-Malays even via Thai-style structures; no exceptions |
| **Hakmilik bumiputera** (Bumiputera-quota lot) | Reserved unit within a development for Bumiputera buyers | ❌ never | Even after the quota release deadline, conversion to "non-bumi" requires state consent and a release fee |
| **Tanah pertanian / smallholder** | Agricultural land < 5 ekar held under specific schemes | ❌ avoid | Multiple consent layers; some schemes (FELDA, FELCRA) have outright bans |

- **Major reforms / regulatory landscape** (date-stamped detail in `shared/regulatory-watch.md`):
  - **National Land Code 1965 (Act 56)**, recodified 2020 — `https://lom.agc.gov.my/`
  - **MM2H relaunch** — June 2024, Silver / Gold / Platinum + SEZ/SFZ categories under MOTAC — `https://www.mm2h.gov.my/`
  - **RPGT revised schedule 2022** under Finance Act 2021; current rates in Schedule 5 of RPGTA 1976 — `https://www.hasil.gov.my/`
  - **Stamp duty foreigner surcharge** — Stamp Act 1949 + Finance Act amendments. **Budget 2026 doubled the foreigner residential MOT stamp duty 4 % → 8 % flat, effective 1 January 2026** (PR exempt — PR pays citizen progressive 1–4 %; foreign-owned companies included). Pre-2026 transactions stamped at 4 % flat (2026-05-27 verified, source: Budget 2026 / KPMG MY TaxLetter / propcashflow.my). Verify Stamp Act amendment gazette at LHDN `https://www.hasil.gov.my/`.
  - **SST reform 2024** — services SST raised to 8 % from 1 March 2024 (impacts agency, legal fees) — `https://mysst.customs.gov.my/`

---

## 🇲🇾 LEAD SECTION: Foreign buyer eligibility

### Bottom line

Foreigners can purchase residential property in their own name (freehold or leasehold), with state-level consent and subject to a state-set minimum purchase price. The structure is generally cleaner and safer than Thailand's, but the **state variation** is the critical trap: thresholds, consent process, and excluded categories all vary by state. Get the threshold + consent process in writing from the destination **state Land Office (Pejabat Tanah)** before signing the Sale and Purchase Agreement (SPA).

### Minimum purchase price by state (2025 reference)

> ⚠️ **Verification required**: state-set thresholds change by Executive Council (EXCO) decision; a single Selangor or Penang threshold revision can move the floor by MYR 500k overnight. Verify at the destination state EXCO / Land Office circular before quoting.

| State / Federal Territory | Minimum purchase price (residential, foreigner) | Authority | Source |
|---|---|---|---|
| **WP Kuala Lumpur** | **MYR 1,000,000** | Federal Territory Land & Mines Office | Federal Territories Ministry — verify at `https://www.kpkt.gov.my/` |
| **WP Putrajaya** | **MYR 1,000,000** | Federal Territory Land & Mines Office | KPKT |
| **WP Labuan** | **MYR 1,000,000** | Labuan Corporation | Labuan land office |
| **Selangor** | **MYR 2,000,000** Zone 1 (Petaling / Gombak / Hulu Langat / Sepang / Klang) + Zone 2 (Kuala Selangor / Kuala Langat); **MYR 1,000,000** Zone 3 (Hulu Selangor / Sabak Bernam); **strata incl. landed strata only — non-strata landed residential not permitted** (Pekeliling PTG Selangor 1/2014, in force 1 Sep 2014; 2016 data, source Dewan Negeri Selangor written answer — rates/figures may have changed since; PTG Selangor portal still names 1/2014 as the approval basis) | Selangor State Authority | Pekeliling PTG Selangor 1/2014 — `https://ptg.selangor.gov.my/index.php/pages/view/268` + Dewan Negeri Selangor answer `https://dewan.selangor.gov.my/question/pemilikan-hartanah-oleh-warga-asing` |
| **Johor** | **MYR 1,000,000–2,000,000** depending on tier and zone (Iskandar Malaysia zones use higher floors; landed strata vary) | Johor State Authority | Johor EXCO — verify Johor State Government circular and Iskandar Regional Development Authority `https://www.irda.com.my/` |
| **Penang (Pulau Pinang)** | **Island strata: MYR 1,000,000**; **Seberang Perai strata: MYR 500,000** — restored after the 2020–2024 HOC campaign (which cut Seberang Perai strata to MYR 400,000) ended Dec 2024 (2026 data, source Penang housing EXCO quoted by Utusan Malaysia, May 2026 — secondary); landed floors: data not publicly available — verify at PTG Pulau Pinang `https://ptg.penang.gov.my/` | Penang State Authority | Penang EXCO — verify `https://www.penang.gov.my/` |
| **Negeri Sembilan** | **MYR 1,000,000** (residential) | NS State Authority | State Land Office |
| **Melaka** | **MYR 1,000,000** (residential, post-2020 EXCO; verify current per Melaka government) | Melaka State Authority | State Land Office |
| **Perak** | **MYR 1,000,000** (residential, est. — verify at Perak Land Office); historically lower (MYR 350,000) pre-2014 | Perak State Authority | State Land Office |
| **Kedah** | **MYR 600,000** (residential, est.); higher in Langkawi free-zone | Kedah State Authority | State Land Office |
| **Pulau Langkawi (within Kedah)** | **MYR 1,000,000** (residential) | Kedah / LADA | Langkawi Development Authority |
| **Perlis** | **MYR 500,000** (residential, est.) | Perlis State Authority | State Land Office |
| **Pahang** | **MYR 1,000,000** (residential, post-2020 EXCO); some hill-resort exceptions | Pahang State Authority | State Land Office |
| **Terengganu** | **MYR 1,000,000** (residential, est.) | Terengganu State Authority | State Land Office |
| **Kelantan** | **MYR 1,000,000** (residential, est.) | Kelantan State Authority | State Land Office |
| **Sabah** | **MYR 600,000** (residential, current EXCO); separate Sabah Land Ordinance regime | Sabah State Authority | Sabah Lands & Surveys Dept `https://jtu.sabah.gov.my` |
| **Sarawak** | **MYR 600,000–1,000,000** depending on division and category; separate Sarawak Land Code regime | Sarawak State Authority | Sarawak Lands & Survey Dept `https://landsurvey.sarawak.gov.my/` |

> Where a band shows "est." or "verify", the state EXCO circular is the only citable source — these numbers shift after each state budget cycle. **Always treat the table as the floor for triage; the SPA-binding number must come from the state circular as of the offer date.**

### Excluded categories (cannot be purchased by foreigners — any state)

1. **Tanah Rizab Melayu** (Malay Reserved Land) — NLC §3 + state-specific Malay Reservation Enactments. Hard ban; no consent route.
2. **Bumiputera-quota lots** — typically 30 % of new launches; release to non-Bumi requires state consent + release fee (3–8 % of market value).
3. **Low-cost / medium-low-cost housing** (rumah kos rendah) — excluded by category.
4. **Smallholder agricultural land** under FELDA / FELCRA / RISDA schemes.
5. **Properties below the state minimum purchase price**.
6. **Strata units in projects with unresolved Bumi quota** — verify *pelepasan* (release) before transfer.

### State authority consent (Section 433B / state equivalents)

- **Legal basis**: NLC 1965 §433B (Peninsular) requires state authority consent for *every* foreign acquisition unless pre-exempted for that price band.
- **Practical process**: most states with thresholds ≥ MYR 1,000,000 grant **general consent** for purchases above the floor — issued as part of the standard transfer. Below the threshold, no consent route exists.
- **Application step**: lawyer files §433B with the transfer at the state Land Office; processing 4–12 weeks.
- **Ministry of Economy** (the department that publishes the former **EPU — Economic Planning Unit** Guidelines; `epu.gov.my` no longer resolves, the portal is `https://ekonomi.gov.my/`) — approval historically required for large commercial / industrial / agricultural acquisitions. **For residential purchases above the state foreigner threshold, approval is generally NOT required** under the revised Guideline on the Acquisition of Properties. EPU still applies to property-company equity transfers and commercial/industrial > MYR 20M.
- **Sabah and Sarawak**: separate consent regimes under Sabah Land Ordinance (Cap. 68) / Sarawak Land Code (Cap. 81); engage locally admitted lawyer.

### MM2H (Malaysia My Second Home) — relaunched June 2024

- **Tier structure** (verify current version at `https://www.mm2h.gov.my/`):

| Tier | Fixed deposit (USD) | Visa duration | Property purchase right |
|---|---|---|---|
| **Silver** | 150,000 | 5 years renewable | Property purchase ≥ MYR 600,000 (subject to state min) |
| **Gold** | 500,000 | 15 years renewable | Property purchase ≥ MYR 1,000,000 |
| **Platinum** | 1,000,000 | 20 years renewable | Property purchase ≥ MYR 2,000,000 |

- **Current MOTAC framework (2026-05-27 verified)**: fixed-deposit tiers are denominated in **USD** (Silver USD 150k / Gold USD 500k / Platinum USD 1M), plus a 4th **SEZ/SFZ** category (FD USD 65k age 21-49 / USD 32k age 50+, compulsory Forest City, Johor property). **No monthly-income requirement** under the current published framework (the earlier MYR 50,000/mo offshore-income line was part of a 2021–2023 iteration and is no longer in force). Property must be acquired within 12 months of visa approval; 10-year property lock-in applies. Pre-2024 thresholds were lower and grandfathered. Source: MOTAC `https://www.mm2h.gov.my/` + applymm2h.com.my (updated Feb 2026). Politically volatile — verify each year.
- **Sarawak MM2H (S-MM2H)** — separate state variant, lower thresholds. `https://smm2h.sarawak.gov.my/`
- **MM2H is residence only**, not a PR path; no work rights in Silver/Gold/SEZ-SFZ (separate EP needed) — Platinum lists career + business as 'Permissible'. Renewable every 5 yrs after the tier term (2026 data, source MOTAC).
- **PR3M / Resident Pass** — older Ministry of Home Affairs program for high-skilled / HNWI; verify at `https://www.imi.gov.my/`.

### Real Property Gains Tax (RPGT) — exit-side cost

> Source: Real Property Gains Tax Act 1976, Schedule 5 (current rates), administered by LHDN — `https://www.hasil.gov.my/en/ckht/`

| Holding period | RPGT (foreigner / non-citizen non-PR) | RPGT (citizen / PR) | RPGT (Malaysian company) |
|---|---|---|---|
| Within 3 years | **30 %** | 30 % | 30 % |
| 4th year | **30 %** | 20 % | 20 % |
| 5th year | **30 %** | 15 % | 15 % |
| 6th year onwards | **10 %** | 0 % (since Jan 2022) | 10 % |

- RPGT base = chargeable gain (disposal price − acquisition price − allowable expenses).
- Foreigners therefore face a permanent 10 % exit tax even after 5+ years; this is the single largest gap vs citizen treatment.
- One-time RPGT exemption for citizens on a residential property disposal (Schedule 4 of RPGTA) — does NOT apply to foreigners.

### Confidence

**HIGH** — National Land Code 1965, RPGT Act 1976, Stamp Act 1949, Condominium Act framework, MM2H official tier structure (post-June-2024 MOTAC), and Sabah/Sarawak land codes are all primary statutes published in the Federal Gazette / state gazettes. **MEDIUM** for current state minimum purchase prices in any specific state — these are EXCO-circular driven and shift between state budget cycles; the table above is a triage reference, NOT an SPA-binding source. Verify the floor with the destination state Land Office at offer date.

---

## Section: `--price`

### Primary sources

- **NAPIC (Pusat Maklumat Harta Tanah Negara)** — JPPH/MoF. Quarterly MHPI (2010=100) + Property Market Report per state/area. `https://napic.jpph.gov.my/`
- **JPPH (Valuation & Property Services)** — `https://www.jpph.gov.my/`
- **DOSM** — Residential Property Price Index (RPPI). `https://www.dosm.gov.my/`
- **BNM** — Quarterly Financial Stability Review residential commentary. `https://www.bnm.gov.my/publications/qb`
- **State e-Tanah portals** — per-parcel title search + transfer history.

### Listing platforms (secondary, listings = seller-controlled)

- **PropertyGuru** `https://www.propertyguru.com.my/` · **iProperty** `https://www.iproperty.com.my/` (PropertyGuru group)
- **EdgeProp** `https://www.edgeprop.my/` — price-trend + transaction tools
- **Brickz** `https://www.brickz.my/transactions/` — transaction-price tracker (sold prices)
- **Mudah.my Property** `https://www.mudah.my/malaysia/properties-for-sale` · **StarProperty** `https://www.starproperty.my/`

### Price benchmarks (Q4 2025 / Q1 2026 reference)

> Source warning: NAPIC quarterly MHPI is the most reliable national/state reference. Listing platforms are seller-controlled and can run 5–15 % above realized prices. Use NAPIC + Brickz transactions for verdict, listings for comp shopping.

| Locality | Segment | MYR/sqft range | USD/sqft est. (4.5 MYR/USD) | Source |
|---|---|---|---|---|
| **KL central** (KLCC, Bukit Bintang, Mont Kiara, Bangsar) | High-end condo | MYR 1,000–2,500/sqft | ≈ $222–$555/sqft | NAPIC + EdgeProp Q1 2026 [verify per project] |
| **KL central** | Mid-tier condo | MYR 700–1,200/sqft | ≈ $156–$267/sqft | NAPIC + PropertyGuru Q1 2026 |
| **KL fringe** (Cheras, Kepong, Setapak, Ampang) | Condo / serviced apt | MYR 400–800/sqft | ≈ $89–$178/sqft | NAPIC + EdgeProp |
| **Petaling Jaya / Subang Jaya / Damansara (Selangor)** | Mid-tier landed/condo | MYR 600–1,500/sqft | ≈ $133–$333/sqft | NAPIC + Brickz Q1 2026 |
| **Cyberjaya / Putrajaya** | Condo / SOHO | MYR 400–700/sqft | ≈ $89–$156/sqft | NAPIC |
| **Penang Island** (George Town, Tanjung Bungah, Batu Ferringhi) | Condo / heritage | MYR 600–1,400/sqft | ≈ $133–$311/sqft | NAPIC + EdgeProp |
| **Penang Mainland** (Seberang Perai) | Landed / condo | MYR 300–600/sqft | ≈ $67–$133/sqft | NAPIC |
| **Iskandar Johor** (Johor Bahru, Iskandar Puteri, Medini) | Condo / landed | MYR 400–900/sqft | ≈ $89–$200/sqft | NAPIC + IRDA |
| **Melaka** | Condo / heritage | MYR 350–700/sqft | ≈ $78–$156/sqft | NAPIC |
| **Kota Kinabalu (Sabah)** | Condo / waterfront | MYR 500–1,200/sqft | ≈ $111–$267/sqft | Sabah Lands + EdgeProp |
| **Kuching (Sarawak)** | Condo / landed | MYR 400–800/sqft | ≈ $89–$178/sqft | Sarawak Lands + EdgeProp |
| **Langkawi** | Resort condo / landed | MYR 500–1,500/sqft | ≈ $111–$333/sqft | LADA + listings |

> Ranges are listing-derived; verify realized vs listing using NAPIC quarterly Property Market Report and Brickz transaction tracker.

### Compute

1. Listing price/sqft = MYR ÷ saleable built-up area. **Trap**: listings often quote *gross* built-up (incl. balcony, A/C ledge, sometimes parking) — verify against *strata title carpet area*.
2. Compare to NAPIC MHPI for the same district + Brickz transactions same building / past 12 months.
3. **Trap (foreigner premium)**: occasional 5–15 % uplift on "foreigner-friendly" towers vs equivalent local-Malaysian unit; check same-floor same-layout local price.
4. **Trap (leasehold discount)**: leasehold with < 50 years remaining typically transacts at 20–40 % discount to freehold; banks reduce LTV on short leases. Verify lease balance at e-Tanah.
5. **Trap (Bumi release pricing)**: a "released" Bumi unit may carry a release-fee history that some lenders flag — verify *pelepasan* completed before transfer.

### Confidence

**HIGH** for KL Klang Valley + Penang ranges (NAPIC + multiple listing platforms + Brickz agree within ±10 %). **MEDIUM** for Iskandar Johor (developer overhang + cross-border Singapore demand cycles produce volatile price signals). **LOW** for Sabah/Sarawak rural areas (limited NAPIC granularity; Sabah/Sarawak land codes produce different transaction-disclosure patterns).

---

## Section: `--traffic`

### Primary sources

- **JKR (Public Works, Jabatan Kerja Raya)** — federal-road authority. `https://www.jkr.gov.my/` ⚠️ **the traffic-count dataset was not located on JKR's reachable pages** — annual daily traffic (ADT) figures: data not publicly available at this source — verify with JKR's road-statistics publication or the Ministry of Works. (Host refuses EU/US egresses; reachable via a Malaysian route.)
- **LLM (Highway Authority)** — toll expressway traffic. `https://www.llm.gov.my/`
- **PLUS Malaysia** (NSE concessionaire) — annual traffic in financial reports. `https://www.plus.com.my/`
- **DBKL** — KL-specific traffic dashboard. `https://www.dbkl.gov.my/`
- **OSM** — fallback for road class.

### Verdict bands (vehicles per day)

- 🟢 < 2,000 v/d: residential lane (lorong / jalan kampung), housing-estate road
- 🟡 2,000–10,000 v/d: minor urban road (jalan), small inter-town
- 🟠 10,000–40,000 v/d: state road / federal road / urban arterial
- 🔴 > 40,000 v/d: tolled expressway / Federal Route 1 / KL urban core arterial

### Coarse fallback (OSM `highway` tag)

- `motorway` / `trunk` = lebuhraya bertol (PLUS, ELITE, NSE, SPRINT, KESAS, NKVE, etc.)
- `primary` = jalan persekutuan (Federal Routes — FT 1, FT 2 etc.)
- `secondary` = jalan negeri (state roads)
- `tertiary` = jalan daerah / inter-mukim
- `residential` = lorong, jalan taman (housing estate)

### Klang Valley + Penang quirks

- Klang Valley traffic chronic; AADT understates noise/pollution exposure on stop-and-go arterials (MRR2, Federal Highway, LDP). Elevated tolled expressways (AKLEH, DUKE, SUKE) over residential areas = 24/7 noise + particulates — flag any property within 100 m of an expressway pillar.
- MRT/LRT proximity premium: 500 m to active station ≈ ~10–20 % uplift (est. from NAPIC MHPI + Brickz transaction comps, 2025) — verify per building and *walking* distance.
- Penang Bridge (FT 36) and Second Penang Bridge (FT 37): Island↔Mainland congestion peaks weekday morning/evening. George Town heritage zone has narrow one-way streets, lower AADT but high tourist scooter density.

### Confidence

**MEDIUM** — JKR federal-road ADT coverage uneven; toll-road numbers (PLUS, LLM) HIGH; urban arterial AADT MEDIUM (DBKL data partial).

---

## Section: `--tax`

### Annual property tax — Cukai Pintu / Cukai Tanah (assessment + quit rent)

Malaysian property carries TWO recurring annual taxes, both LOW vs Western European standards:

| Tax | What | Authority | Typical residential range |
|---|---|---|---|
| **Cukai Pintu (Assessment)** | Local council assessment tax on built property | City / district council (DBKL, MBPJ, MPSJ, MBPP, etc.) | MYR 200–2,000/yr typical for residential; based on annual rental value × council rate (3–10 %) |
| **Cukai Tanah (Quit Rent)** | State land tax on land parcel | State Land Office | MYR 30–500/yr typical; based on land area × state rate (per sqft / per acre) |

- **Cukai Pintu** is biannual (semi-annual) in most councils; due February + August.
- **Cukai Tanah** is annual; due 31 May (most states).
- Sabah uses different terminology (Cukai Tanah administered under Sabah Land Ordinance).

> Source: Local council websites (e.g., DBKL `https://www.dbkl.gov.my/`, MBPP Penang Island `https://www.mbpp.gov.my/`), state Land Offices (quit rent).

### Example calculation — KL condo, 1,200 sqft, AV MYR 30,000/yr

- Cukai Pintu (DBKL rate ≈ 4 %): 30,000 × 4 % = **MYR 1,200/yr** (≈ USD 270)
- Cukai Tanah (KL strata, low — strata is per-share of land): **~MYR 50–100/yr**
- **Total annual property tax**: ~MYR 1,300/yr (≈ USD 290) — very low vs UK/FR/IT.

### Transaction taxes (one-time at purchase)

#### Stamp duty — Memorandum of Transfer (MOT)

> Source: **Stamp Act 1949, First Schedule** (the ad-valorem MOT scale) + Finance Act amendments, administered by LHDN — overview at `https://www.hasil.gov.my/en/duti-setem/` (⚠️ the LHDN landing page states only that "the rate of duty varies according to the nature of the instruments and the consideration"; the band percentages come from the Act's First Schedule, not from this page — 2026-09-18 verified) · e-stamping `https://stamps.hasil.gov.my/stamps/`

**Citizen / PR rates** (progressive, on consideration / market value, whichever higher):

| Bracket (MYR) | Rate |
|---|---|
| 0 – 100,000 | 1 % |
| 100,001 – 500,000 | 2 % |
| 500,001 – 1,000,000 | 3 % |
| Above 1,000,000 | 4 % |

**Foreigner / foreign-owned-company rates** (current 2025; verify at LHDN — there is a flat surcharge):

- **Foreign individual / foreign-incorporated company**: **flat 4 %** on the entire MOT value (no progressive bracket benefit). This is materially higher than the citizen progressive rate for properties under MYR 1 million.
- For a MYR 1,500,000 KL condo:
  - Citizen: 1,000 + 8,000 + 15,000 + 20,000 = **MYR 44,000** (~USD 9,800)
  - Foreigner: 1,500,000 × 4 % = **MYR 60,000** (~USD 13,300)
  - Gap = **MYR 16,000** (~USD 3,500) — foreigner pays ~36 % more in MOT stamp duty

#### Stamp duty — Sale and Purchase Agreement (SPA)

- **MYR 10 flat** on the SPA itself (not on the MOT). Negligible.

#### Stamp duty — Loan Agreement

- **0.5 %** on the loan principal (if buyer takes a Malaysian mortgage). Foreign-buyer mortgages capped LTV ≤ 70 % typically; verify with BNM credit guidelines.

#### Legal fees — SPA + MOT

- **Solicitors' Remuneration Order 2023** (Bar Council Malaysia) sets statutory scale:

| Property value (MYR) | Scale fee |
|---|---|
| First 500,000 | 1.25 % (subject to min MYR 500) |
| Next 500,000 | 1.0 % |
| Next 2,000,000 | 0.7 % |
| Next 2,000,000 | 0.6 % |
| Next 2,500,000 | 0.5 % |
| Above 7,500,000 | Negotiable (≤ 0.5 %) |

- For MYR 1,500,000 condo: 6,250 + 5,000 + 3,500 = **MYR 14,750** (~USD 3,300) — both SPA and MOT typically borne by buyer.
- Source: Bar Council Malaysia `https://www.malaysianbar.org.my/`

#### Real estate agent commission

- **Maximum 3 %** of selling price under the Malaysian Institute of Estate Agents (MIEA) / Board of Valuers, Appraisers, Estate Agents and Property Managers (BOVAEP) regulation. Typically paid by **seller**.
- Source: BOVAEP `https://lppeh.gov.my/`

#### SST on services (post-Mar 2024)

- 8 % SST on legal fees, agent fees, valuation services. Effective 1 March 2024.
- Source: Royal Malaysian Customs `https://mysst.customs.gov.my/`

### Total transaction cost (foreign buyer, MYR 1,500,000 KL condo)

| Item | MYR | % |
|---|---|---|
| MOT stamp duty (foreigner flat 4 %) | 60,000 | 4.00 % |
| Loan agreement stamp duty (70 % LTV) | 5,250 | 0.35 % |
| Legal fees (SPA + MOT) + SST 8 % | 15,930 | 1.06 % |
| Valuation + §433B consent | 2,500–4,000 | 0.20 % |
| **Total** | **≈ 83,000–85,000** | **≈ 5.5 %** |

> Compare: ES ~10 %, IT ~10–13 %, FR ~7–8 %, CZ ~1–2 %. Malaysia foreign buyer ~5–6 % is mid-range.

### Future risk

- Stamp duty foreigner surcharge has been mooted for further tightening (Budget 2024 / 2025 discussions); verify current rate at Budget Speech transcripts before quoting.
- Property tax revaluation: KL last city-wide revaluation 2013 — overdue; expect significant assessment uplift on next revaluation (could double bills for older properties).

---

## Section: `--rental`

### Long-term residential rental

> Source: Income Tax Act 1967 §4(d) (rental income), administered by LHDN — `https://www.hasil.gov.my/en/individu/kadar-cukai/`

#### Tax treatment

- **Resident individual** (citizen, PR, or foreigner ≥ 182 days physical presence): rental aggregated with other income at progressive PIT scale (Schedule 1 ITA 1967, 2025 brackets — 0 % up to MYR 5k; 1 % to 20k; 3 % to 35k; 6 % to 50k; 11 % to 70k; 19 % to 100k; 25 % to 400k; 26 % to 600k; 28 % to 2M; **30 % above 2M**).
- **Non-resident individual** (foreigner < 182 days/year): flat **30 %** with no personal relief.
- Allowable deductions: assessment, quit rent, mortgage interest, repairs (not improvements), agent fees, insurance.
- File via e-Filing: `https://mytax.hasil.gov.my/`

#### Typical gross yields (Q1 2026 reference)

| Locality | Segment | Gross yield range | Source |
|---|---|---|---|
| **KL central** (KLCC, Mont Kiara, Bangsar) | Condo | 3–5 % | NAPIC + EdgeProp + listings |
| **KL fringe / mid-tier** | Condo | 4–6 % | NAPIC + listings |
| **PJ / Subang / Damansara** | Landed / condo | 3–5 % | NAPIC + listings |
| **Penang Island** (George Town) | Heritage / condo | 3–5 % | NAPIC + listings |
| **Iskandar Johor** | Condo (cross-border SG demand) | 3–6 % (volatile) | IRDA + NAPIC |
| **Cyberjaya / Putrajaya** | SOHO / condo | 4–7 % | NAPIC |

> Yield = (annual rental × 12) / purchase price. Net yields after assessment + quit rent + management + vacancy allowance typically **1.5–2.0 % below gross**.

### Short-term rentals (STR / Airbnb)

- **Federal**: no single STR licensing law as of May 2026; sits between Tourism Industry Act 1992, Strata Management Act 2013 (KPKT), and local council by-laws.
- **Strata properties**: under SMA 2013, the JMB / MC can prohibit short lets via house rules. Many KL/Penang condo MCs have explicit Airbnb bans — verify by-laws BEFORE buying for STR investment.
- **Penang**: the operative instrument is the Penang State Government *Garis Panduan Pengoperasian Tempat Inap Persendirian (TIP) di Skim Hartanah Berstrata*, **in force 1 April 2023** (MMK 07/2023), **full implementation 1 March 2024** — this supersedes the older "2020 MBPP circular" framing, and the test is a **property-class whitelist, not tourism zoning**. Under **MBPP (Penang Island)** only **Pangsapuri Perkhidmatan / SoHo / SoFo / SoVo / office suite / office duplex** are whitelisted, so ordinary residential strata on the Island is **effectively barred** from STR; **MBSP (mainland Seberang Perai)** additionally allows **apartments, condominiums, townhouses and landed strata**. Conditions: the premises **owner and operator must be Malaysian citizens only** (cl. 5.1.1 — a foreign owner cannot run TIP on any Penang strata unit, Island or mainland); max **180 days per year** (extension only by a further three-quarters special resolution) and **3 days per rental transaction within one week**; a **three-quarters JMB or MC special resolution** under Strata Management Act 2013 **ss. 32(3) and 70(2)**; **low-cost / RM300,000-and-below affordable / PPR units barred**. A **parallel state guideline licenses landed-home TIP**. (2023–2024 instruments, MBPP primary source; 2026-08-07 verified.) Verify `https://www.mbpp.gov.my/images/sumber/perancangan/l.u.2_-_gp_pengoperasian_tip_di_skim_hartanah_berstrata_di_pulau_pinang.pdf` and `https://www.mbpp.gov.my/`.
- **Kuala Lumpur**: DBKL publishes an **STR SOP for developers, JMB and MC**; enforcement varies; some Bukit Bintang towers operate as serviced apartments under Tourism Industry Act licensing. **MC by-laws remain the decisive final layer in KL** (2026-08-07 verified).
- **Petaling Jaya (Selangor)**: MBPJ **licenses** STR as **Rumah Penginapan** under the MBPJ guideline **in force 1 January 2020** (MBPJ Hotel By-Laws 2007) — a licensable activity, not a blanket ban; **MC by-laws remain the decisive final layer in PJ** (2026-08-07 verified).
- **Tourist-zoned** (Langkawi, Penang outer, Sabah coast): more permissive, still subject to MC by-laws + Tourism Ministry registration.
- **Tax**: STR income under §4(d) ITA 1967, or §4(a) (business) if scale + service intensity = "trade" — may trigger SST registration > MYR 500k turnover. Tourism tax MYR 10/room/night for registered accommodation under Tourism Tax Act 2017.

### Strategic notes

- Tourist-zoned areas viable for STR; verify MC by-laws first.
- KL/PJ condos increasingly STR-restricted — assume long-term unless MC explicitly allows.
- Iskandar Johor: cross-border Singapore demand → mid-term rental (3–12 month) viable; RTS Link 2026 catalyst.
- Foreign owner management: appoint Malaysian property manager; income through Malaysian bank; annual LHDN filing.

### Confidence

**HIGH** on tax framework (LHDN primary). **MEDIUM** on STR regulation (state + council variable; in flux). **MEDIUM** on yield benchmarks (NAPIC quarterly + listing-derived).

---

## Section: `--work=<profession>`

### Job platforms

- **JobStreet Malaysia**: `https://www.jobstreet.com.my/` — largest by volume
- **LinkedIn MY**: very active in IT, finance, oil&gas, MNCs
- **Maukerja, Ricebowl, Hiredly, JobsCentral** — secondary
- **MyFutureJobs (PERKESO official)**: `https://www.myfuturejobs.gov.my/` — official (linked to EIS / SOCSO)
- **Federal job portal SPA**: `https://www.spa.gov.my/` — civil service

### Self-employment / business regimes

- **Sole proprietor (Pemilik Tunggal)**: registered with **SSM (Suruhanjaya Syarikat Malaysia, Companies Commission of Malaysia)** — `https://www.ssm.com.my/`. Annual fee MYR 30 + tax filing under personal income tax.
- **Sdn Bhd (private limited company)**: minimum 1 director ordinarily resident in Malaysia; 1 shareholder; minimum paid-up capital MYR 1; corporate tax 17 %/24 % (SME tiered) or 24 % flat (large).
- **Foreign-owned Sdn Bhd** for residential property holding: **NOT recommended** as a workaround for state thresholds (the threshold applies regardless of buyer entity); legitimate uses are commercial property and operating businesses.

### Foreign work rights

- **Employment Pass (EP)**: most common skilled-worker visa. Three categories:
  - **EP Cat I** (≥ MYR 10,000/month salary; up to 5-yr pass)
  - **EP Cat II** (MYR 5,000–9,999/month; up to 2-yr pass)
  - **EP Cat III** (MYR 3,000–4,999/month; up to 12-month pass)
  - Source: Immigration Department of Malaysia (JIM, ESD portal) `https://esd.imi.gov.my/`
- **DE Rantau (Digital Nomad Pass)** — launched October 2022 by MDEC; for tech / digital professionals; 12-month renewable; min income USD 24,000/yr.
  - Source: `https://mdec.my/derantau/`
- **MM2H pass holders**: no work rights in Silver / Gold / SEZ-SFZ — apply separately for an EP; Platinum lists career opportunities as 'Permissible' (2026 data, source MOTAC).
- **Sarawak**: separate Sarawak Immigration regime — must obtain Sarawak-specific work pass (not federal EP) to work *in Sarawak* even if you hold federal EP for elsewhere. Source: Sarawak Immigration `https://genesis.sarawak.gov.my/EXPRT/employment-pass`

### Salaried benchmarks (MYR/month, 2025 reference)

- **Minimum wage**: **MYR 1,700/month nationwide** under the **Minimum Wages Order 2024 [P.U. (A) 376]**, gazetted 4 Dec 2024 — in force **1 Feb 2025** for employers with five or more employees and for MASCO professional-activity employers of any size, and **1 Aug 2025 for all employers** with no headcount exception; **domestic servants are excluded**. There is no Peninsular / Sabah / Sarawak split (2025 data, source Minimum Wages Order 2024 P.U. (A) 376; 2026-09-18 verified) — [gazette PDF](https://gajiminimum.mohr.gov.my/wp-content/uploads/PUA%20376.pdf) · ministry (now branded **KESUMA**) `https://www.mohr.gov.my/`
- **DOSM Salaries & Wages Survey 2024** median monthly: ~MYR 2,700 nationally; KL ~MYR 3,800
- **est. market bands (not DOSM categories — verify)**: skilled professional KL ~MYR 6,000–12,000; MNC mid-management ~MYR 12,000–25,000; C-suite ~MYR 25,000+
- Source: DOSM Salaries & Wages Report `https://www.dosm.gov.my/`

### Catchment heuristics

- Within 30 min of KL CBD: full salaried + freelance opportunity (Klang Valley conurbation ~8 million)
- Within 60 min of George Town: Penang Island IT/manufacturing belt
- Within 30 min of Johor Bahru CBD: Iskandar + cross-border Singapore commute (RTS Link 2026)
- Sabah Kota Kinabalu / Sarawak Kuching: thinner skilled labour markets; tourism + oil&gas concentrations

---

## Section: `--risks`

### Primary national sources

| Source | URL | Gives |
|---|---|---|
| **MetMalaysia** | `https://www.met.gov.my/` | Weather warnings, monsoon, seismology |
| **DID / InfoBanjir** | `https://publicinfobanjir.water.gov.my/`, `https://publicinfobanjir.water.gov.my/` | Flood levels + national hazard maps |
| **NADMA** | `https://www.nadma.gov.my/` | Disaster declarations, evacuation |
| **JMG (Geoscience)** | `https://www.jmg.gov.my/en` | Landslide hazard, geological substrate |
| **DOE / APIMS** | `https://apims.doe.gov.my/` | Air quality (API real-time), water quality |
| **MyGeoportal** | `https://www.mygeoportal.gov.my/` | National geospatial portal |

### Flood risk

- **NE monsoon (Nov–Feb)**: Peninsular East Coast (Kelantan, Terengganu, Pahang, East Johor) + Sabah/Sarawak flood most years. Dec 2014, Jan 2017, Dec 2021–Jan 2022 floods caused billions MYR damage.
- **Klang Valley flash flooding**: increasing frequency 2021–2024; SMART Tunnel + Klang River drainage insufficient under extreme rainfall. Hot zones: Taman Sri Muda (Shah Alam), Pantai Dalam, Cheras Batu 9.
- **Penang flash flooding**: Tanjung Bungah / Pulau Tikus areas (hill development + drainage).
- **Verification**: pull JPS PIB hazard map for parcel district; check NADMA disaster declarations; ask seller about 10-year flood history.

### Landslide + earthquake risk

- **Hill landslide hot zones**: Bukit Antarabangsa (KL — 2008 event killed 5), Cameron Highlands, Genting Highlands, Penang Hills, Bukit Lanjan. Source: JMG landslide hazard map. Pre-2008 construction on slopes > 15° = high attention.
- **Peninsular Malaysia**: low seismicity, but Sumatra felt-tremors (Aceh 2004 M 9.1, Padang 2009 M 7.6) reach Penang + Klang Valley high-rises.
- **Sabah**: moderate seismicity — **Ranau M 6.0 (5 Jun 2015)** killed 18 climbers. **Sarawak**: low.
- **Building Code**: Eurocode 8 Malaysian NA (MS EN 1998-1:2015) introduced seismic design for Sabah + Peninsular high-risk zones; pre-2015 high-rises may have weaker compliance.

### Haze / air quality

- **Trans-boundary haze** from Sumatra/Borneo peat fires: severe episodes 1997, 2005, 2013, 2015, 2019; API hit "Hazardous" (>300) in worst.
- **Most exposed**: Klang Valley + Penang + Sarawak Kuching; East Coast less.
- **Mitigation**: HEPA HVAC + sealed windows + air purifiers — est. MYR 15,000–50,000 install for a ~200 sqm condo (installer-quote dependent; verify).

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1957** (colonial) | Lead paint, asbestos roofing; heritage status (George Town / Melaka UNESCO) constrains restoration |
| **1957–1983** | Lead paint, asbestos sheet + cement piping, weak by-law compliance |
| **1984–2000** (UBBL post-1984) | Asbestos in older flats; some 1980s aluminium wiring; pre-2008 hill development = weak landslide compliance |
| **2000–2015** | Modern UBBL; pre-2015 weaker seismic for Sabah high-rises |
| **Post-2015** | Eurocode-aligned seismic; better fire safety; voluntary Green Building Index |

### Mandatory diagnostics at sale

| Document | Required because | Notes |
|---|---|---|
| **Geran (title) issued copy** | All sales | Verify owner + encumbrances at e-Tanah |
| **Cukai Pintu / Cukai Tanah receipts** | All sales | Proof of no arrears at signing |
| **Land Search (Carian Rasmi)** | All transfers | Done by lawyer pre-SPA |
| **Strata Management Statement** | Apartment / condo | Maintenance fee, sinking fund, no arrears |
| **CCC** (Cert of Completion & Compliance) | Buildings post-2007 | Replaces CFO; mandatory for occupation |
| **Bumi quota release (pelepasan)** | If Bumi-quota unit | Non-released unit cannot transfer to non-Bumi |
| **EIA / Slope stability report** | Hill / slope properties post-2008 | Local council requirement |

> No general EPC equivalent (vs EU PENB); Green Building Index (GBI) is voluntary marketing.

### Climate change projections (MetMalaysia + IPCC AR6)

- Mean temperature already +1.0–1.4 °C vs 1961–1990; projected +1.5–2.5 °C by 2050 (RCP4.5).
- Sea-level rise: +25–35 cm by 2050, +60–80 cm by 2100 (RCP8.5) — coastal Penang, KK, JB, Klang exposed.
- Monsoon intensification: heavier short-duration rainfall; flash flood frequency rising.
- Heat stress: more TX ≥ 35 °C days; UHI intensifying in KL/Penang/JB.
- Source: MetMalaysia "Future Climate Change Projection for Malaysia 2010–2099" via `https://www.met.gov.my/`

---

## Section: `--mains`

### National database

- Federal level: **National Water Services Commission (SPAN, Suruhanjaya Perkhidmatan Air Negara)** regulates water + sewerage operators. `https://www.span.gov.my/`
- Sewerage: **Indah Water Konsortium (IWK)** — national sewerage operator (Peninsular). `https://www.iwk.com.my/`
- Drinking water: state-licensed operators (varies by state).

### Major operators (state water)

| Operator | Coverage |
|---|---|
| **Air Selangor** | Selangor + KL + Putrajaya |
| **PBA Pulau Pinang** | Penang |
| **Ranhill SAJ** | Johor |
| **AKSB / PAAB / SADA / SAINS / LAP / others** | Kelantan / Kedah / Perlis / Negeri Sembilan / Perak / regional |
| **Sabah Water Dept / Ranhill Sabah** | Sabah (water + sewerage) |
| **Kuching Water Board / LAKU / SIBU WB** | Sarawak (multiple boards) |
| **IWK** | Sewerage Peninsular national (except parts of Johor / Sabah / Sarawak) |

### Verification

1. Check the state water operator website for connection status.
2. Listing language: "Bekalan air paip / Mains water" = mains water; "Pembetungan IWK / Mains sewerage" = mains drains; "Sistem septik" = septic; "Telaga / Well" = no mains.
3. Most urban areas have mains water + sewerage; rural kampung typically mains water + septic-tank sewage; Sabah/Sarawak rural significant areas without mains water.

### Costs

| Scenario | Cost (MYR) |
|---|---|
| Connection (mains water available, urban) | 1,000–5,000 (one-time) |
| Sewerage connection (IWK, urban) | 500–2,500 (one-time) |
| Septic tank install (rural) | 3,000–15,000 |
| Septic to mains conversion (where mains arrives later) | 5,000–20,000 |
| Borehole / well (rural without mains) | 8,000–30,000 |

### Annual utility fees (2025 reference, residential)

| Item | MYR/month |
|---|---|
| Mains water (Air Selangor, low/high usage) | 8–80 |
| IWK sewerage (residential flat) | 8–12 |
| Cukai Pintu (assessment, averaged) | 20–200 |

---

## Cost benchmarks (MY 2026, residential foreign buyer)

| Work | Cost (MYR) |
|---|---|
| Land Search (Carian Rasmi) | 50–200 |
| SPA legal fees (typical, scale-based) | 0.5–1.25 % of price |
| MOT legal fees | 0.5–1.25 % of price |
| MOT stamp duty (foreigner flat 4 %) | 4 % of price |
| Loan Agreement stamp duty | 0.5 % of loan |
| Valuation report (independent) | 1,500–5,000 |
| State consent application (Section 433B) | 500–2,000 |
| Sworn translation (geran, if needed) | 200–800 |
| Building inspection (independent) | 2,000–8,000 |
| Annual Cukai Pintu (assessment) | 200–2,000 |
| Annual Cukai Tanah (quit rent) | 30–500 |
| Annual sinking fund + management (strata) | 2,400–24,000 |
| **Total transaction cost (foreign buyer)** | **≈ 5–6 % of price** |

## Active fiscal incentives (2025)

- **MM2H** (Silver / Gold / Platinum + SEZ/SFZ) — see foreign-buyer section
- **Sarawak MM2H (S-MM2H)** — lower thresholds
- **Resident Pass (Talent Corp)** — high-skilled professionals `https://www.talentcorp.com.my/`
- **MIDA** (manufacturing / services / R&D, business-only): `https://www.mida.gov.my/`
- **Iskandar / IRDA zones** (Johor): tax incentives for qualifying activities (not residential): `https://www.irda.com.my/`
- **MM2H foreign-source income remittance**: specific LHDN orders apply — verify current public rulings.
- **GBI-certified properties**: marginal stamp duty reductions historically; verify Budget annually.

## Common listing platforms

- **PropertyGuru** (largest) · **iProperty** (PG group) · **EdgeProp** (sale + rental + tx tools) · **Brickz** (sold-price tracker) · **Mudah.my Property** (classifieds) · **StarProperty** · **Speedhome** (rental) · **Imoney / Loanstreet** (mortgage comparison)

## Caveats unique to MY

- **State variation is the booby-trap**: Selangor MYR 2,000,000 vs WP-KL MYR 1,000,000 for the same year — the Klang Valley region alone has a 2× threshold gap depending on which side of a federal-state border the property sits. Always verify.
- **Bumiputera quota release (pelepasan)** — non-released units cannot transfer to non-Bumi (foreigner = non-Bumi); critical to verify before signing.
- **Malay Reserved Land (Tanah Rizab Melayu)** — hard ban on foreign acquisition; no consent route, no exceptions.
- **Sabah / Sarawak separate land regimes** — Sabah Land Ordinance (Cap. 68) and Sarawak Land Code (Cap. 81) operate independently from Peninsular National Land Code 1965; engage local-admitted lawyer.
- **MM2H volatility** — program suspended 2020, reopened with stricter terms 2021, restructured June 2024; the political cycle around MM2H means tier numbers can shift between budgets.
- **Foreigner stamp duty surcharge (8 % flat MOT eff 1 Jan 2026 under Budget 2026; was 4 % flat 2024–2025)** — materially increases acquisition cost vs progressive citizen rates (1–4 %); PR exempt (pay citizen progressive); foreign-owned companies included (2026-05-27 verified).
- **RPGT 10 % permanent for foreigners** beyond year 5 — citizens drop to 0 %; this is a permanent foreign-buyer disadvantage at exit.
- **STR (Airbnb) regulation in flux** — on **Penang Island (MBPP)** the state TIP strata guideline (in force 1 Apr 2023, MMK 07/2023; full implementation 1 Mar 2024) whitelists only Pangsapuri Perkhidmatan / SoHo / SoFo / SoVo / office suite / office duplex, so ordinary residential strata is effectively barred, while **mainland MBSP** additionally allows apartments, condominiums, townhouses and landed strata (Malaysian-citizen owner and operator only; 180 days/yr + 3 days per rental transaction within one week caps; three-quarters JMB/MC special resolution under SMA 2013 ss. 32(3) + 70(2); low-cost / RM300,000-and-below affordable / PPR units barred). **PJ licenses STR as Rumah Penginapan** (MBPJ guideline in force 1 Jan 2020) and **DBKL publishes an STR SOP** for KL — in both, **MC by-laws are the decisive final layer**. Verify *before* signing for STR investment thesis (2026-08-07 verified).
- **Cross-border Singapore demand** drives Iskandar Johor prices; RTS Link opening 2026 is the key catalyst.
- **Tropical climate hazards**: NE monsoon flooding (East Coast), Klang Valley flash flooding, Sabah seismicity (Ranau M 6.0 2015), trans-boundary haze (Sumatra peat fires).
- **No general EPC equivalent** (vs EU); GBI is voluntary marketing.
- **Foreign-source income (FSI) remittance**: **Budget 2026 extended the FSI exemption for resident individuals to 31 December 2036** (10-year extension from the prior 31 Dec 2026 sunset); for companies/LLPs/cooperatives/trusts (dividends + capital gains), extended to 31 Dec 2030. LHDN PR 12/2022 + Income Tax (Exemption) Orders 2022–2026; declaration in the annual return + supporting docs still required (2026-05-27 verified, source: Budget 2026 / MoF).

## Reddit / forum sources

- **r/malaysia**, **r/MalaysianPF** (personal finance + property), **r/Kualalumpur**, **r/Penang**, **r/Johor**, **r/Bolehland**
- **Lowyat.NET property forum**: `https://forum.lowyat.net/PropertyTalk`
- **iProperty Insider** + **EdgeProp news** — semi-editorial market commentary
- ⚠️ Forum-quality caveat: legal exposure (Bumi quota, MRL, state thresholds) shifts after each state EXCO meeting — treat older threads as outdated.

## Verification authorities

| Authority | When to call | URL |
|---|---|---|
| **State Land Office (Pejabat Tanah)** | Title verification, transfer, §433B consent | per state via `https://www.jkptg.gov.my/` |
| **JUPEM** | Cadastral plan | `https://www.jupem.gov.my/` |
| **LHDN** | RPGT, stamp duty, rental income tax | `https://www.hasil.gov.my/` |
| **Kastam** | SST on services, tourism tax | `https://mysst.customs.gov.my/` |
| **JIM (Immigration)** | EP, MM2H, DE Rantau | `https://www.imi.gov.my/` |
| **MOTAC** | MM2H program | `https://www.mm2h.gov.my/` |
| **Sarawak Immigration / S-MM2H** | Sarawak work pass + S-MM2H | `https://genesis.sarawak.gov.my/EXPRT/employment-pass` |
| **Sabah Lands & Surveys** | Sabah transactions (Cap. 68) | `https://jtu.sabah.gov.my` |
| **Sarawak Lands & Survey** | Sarawak transactions (Cap. 81) | `https://landsurvey.sarawak.gov.my/` |
| **BNM** | FX, mortgage credit | `https://www.bnm.gov.my/` |
| **EPU** | Commercial / industrial / equity | `https://ekonomi.gov.my/` |
| **MIDA / IRDA** | Investment incentives, Iskandar | `https://www.mida.gov.my/`, `https://www.irda.com.my/` |
| **NAPIC / JPPH** | Market data, valuation | `https://napic.jpph.gov.my/` |
| **BOVAEP / Bar Council** | Agent + lawyer fee scales | `https://lppeh.gov.my/`, `https://www.malaysianbar.org.my/` |
| **Local council** (DBKL/MBPP/MBPJ/MPSJ etc.) | Cukai Pintu, permits, zoning | per council |
| **SPAN / IWK** | Water + sewerage | `https://www.span.gov.my/`, `https://www.iwk.com.my/` |
| **DID InfoBanjir / NADMA** | Flood + disaster | `https://publicinfobanjir.water.gov.my/`, `https://www.nadma.gov.my/` |
| **MetMalaysia / JMG / DOE** | Climate, geology, air quality | `https://www.met.gov.my/`, `https://www.jmg.gov.my/`, `https://apims.doe.gov.my/` |

## Quirks to know

- **Geran types**: Geran Mukim (rural), Geran Daerah / FT (urban) — both transferable with state consent; Pajakan Negeri (state lease) = leasehold variant.
- **Bumi quota release (pelepasan)**: separate state-authority application BEFORE foreign transfer; verify on paper, not orally.
- **Strata Title vs Master Title**: must have individual Strata Title issued for unit-by-unit transfer; Master-Title-only transfers via SPA assignment carry higher risk.
- **CCC vs CF**: Certificate of Completion & Compliance (post-2007) replaced CF; occupation without CCC is illegal.
- **§433B consent**: required for every foreign acquisition (Peninsular); 4–12 weeks; lawyer files with transfer.
- **Sabah / Sarawak**: separate land regimes (Cap. 68 / Cap. 81); engage locally admitted lawyer (Sabah Bar / Sarawak Advocates).
- **Penang George Town UNESCO Core Zone**: restoration constraints; verify with Think City + GTWHI + Penang Heritage Trust.
- **Iskandar Malaysia zones (A–E)**: activity-based incentives are commercial; residential uses standard Johor foreigner threshold.
- **99-year leasehold renewal**: premium typically ≥ 25 % of state market value at renewal; budget for sub-50-year leases.
- **Foreign mortgages**: Malaysian banks typically cap LTV at 60–70 % (vs 80–90 % for citizens); MM2H Gold/Platinum sometimes marginally better.
- **Selling as foreigner**: RPGT 10 % flat above year 5; FX repatriation generally unrestricted with proper documentation per BNM rules.

## Source URL templates

| Source | URL |
|---|---|
| JKPTG / JUPEM | `https://www.jkptg.gov.my/`, `https://www.jupem.gov.my/` |
| e-Tanah (Selangor) / MyLAND (Federal Territories, JKPTG — account required) | `https://etanah.selangor.gov.my/`, `https://myland.gov.my/` |
| KPKT | `https://www.kpkt.gov.my/` |
| Laws of Malaysia online | `https://lom.agc.gov.my/` |
| Sabah / Sarawak Lands | `https://jtu.sabah.gov.my`, `https://landsurvey.sarawak.gov.my/` |
| LHDN (main / RPGT / Stamp / e-filing) | `https://www.hasil.gov.my/`, `https://mytax.hasil.gov.my/` |
| Kastam SST | `https://mysst.customs.gov.my/` |
| BNM (main / FX) | `https://www.bnm.gov.my/`, `https://www.bnm.gov.my/exchange-rates` |
| DOSM | `https://www.dosm.gov.my/` |
| NAPIC / JPPH | `https://napic.jpph.gov.my/`, `https://www.jpph.gov.my/` |
| JIM / MM2H / S-MM2H / DE Rantau | `https://www.imi.gov.my/`, `https://www.mm2h.gov.my/`, `https://smm2h.sarawak.gov.my/`, `https://mdec.my/derantau/` |
| Sarawak Immigration | `https://genesis.sarawak.gov.my/EXPRT/employment-pass` |
| MIDA / IRDA / EPU | `https://www.mida.gov.my/`, `https://www.irda.com.my/`, `https://ekonomi.gov.my/` |
| BOVAEP / Bar Council | `https://lppeh.gov.my/`, `https://www.malaysianbar.org.my/` |
| SPAN / IWK | `https://www.span.gov.my/`, `https://www.iwk.com.my/` |
| Water (Air Selangor / PBA) | `https://www.airselangor.com/`, `https://pba.com.my/` |
| DID InfoBanjir / NADMA | `https://publicinfobanjir.water.gov.my/`, `https://www.nadma.gov.my/` |
| MetMalaysia / JMG / DOE-APIMS / MyGeoportal | `https://www.met.gov.my/`, `https://www.jmg.gov.my/en`, `https://apims.doe.gov.my/`, `https://www.mygeoportal.gov.my/` |
| JKR / LLM / PLUS / DBKL / MBPP | `https://www.jkr.gov.my/`, `https://www.llm.gov.my/`, `https://www.plus.com.my/`, `https://www.dbkl.gov.my/`, `https://www.mbpp.gov.my/` |
| PropertyGuru / iProperty / EdgeProp / Brickz / Mudah | `https://www.propertyguru.com.my/`, `https://www.iproperty.com.my/`, `https://www.edgeprop.my/`, `https://www.brickz.my/transactions/`, `https://www.mudah.my/malaysia/properties-for-sale` |

---

## Status

✅ **Fully populated** as of 2026-05-01.

**Coverage check**: foreign-buyer eligibility (LEAD), price, traffic, tax, rental, work, risks, mains all sourced to primary government / regulated entity URLs + cost benchmarks + caveats.

**Confidence**:
- **HIGH** — National Land Code 1965 framework, RPGT Act 1976 schedule, Stamp Act 1949, Solicitors' Remuneration Order 2023, MM2H tier framework (post-June-2024 MOTAC), Sabah / Sarawak land code separation, Section 433B state consent process, BOVAEP agent commission cap, NAPIC quarterly MHPI methodology.
- **MEDIUM** — current state-by-state minimum purchase prices (state EXCO circulars shift between budget cycles; the table above is triage, not SPA-binding); STR (Airbnb) enforcement intensity (state + council variable); MM2H program stability (politically volatile — verify current tier structure each year); foreign-source income remittance taxation (LHDN public rulings ongoing); current foreigner MOT stamp duty surcharge (verify latest Budget speech).
- **LOW** for none — every section has primary sources.

**Reform watch items** (track in `shared/regulatory-watch.md`):
1. **MM2H tier structure** — politically volatile; revised June 2024; verify each year.
2. **State minimum purchase price thresholds** — EXCO-driven; revise per state budget cycle.
3. **Foreigner stamp duty surcharge** — Budget 2024/2025 discussions floated further tightening; verify annual Budget.
4. **STR / Airbnb licensing** — federal framework not yet enacted; state + council patchwork in flux.
5. **Foreign-source income remittance taxation** — LHDN public ruling clarifications ongoing post-2022.
6. **Property tax revaluation (Cukai Pintu)** — KL last city-wide revaluation 2013; next revaluation overdue.
7. **RTS Link Johor–Singapore opening 2026** — Iskandar property demand catalyst.
8. **Sabah seismic code review** — post-Ranau 2015 + post-Myanmar 2025 quakes; verify current MS EN 1998-1 National Annex.

**Last verified**: 2026-08-07 (`--rental` STR patch from `shared/regulatory-watch.md` — Penang TIP strata guideline in force 1 Apr 2023 / full implementation 1 Mar 2024, MBPP island whitelist vs MBSP mainland wider scope, 180-day/yr + 3-days-per-rental-transaction-within-one-week caps — cap wording corrected 2026-09-24; three-quarters JMB/MC resolution under SMA 2013 ss. 32(3)+70(2); MBPJ Rumah Penginapan licensing; DBKL STR SOP). Prior sweep 2026-05-27 (Foreigner MOT 8% eff. 1 Jan 2026 (Budget 2026); MM2H USD tiers restated (Silver 150k/Gold 500k/Platinum 1M); FSI individuals extended to 31 Dec 2036; minimum wage corrected 2026-09-18 per Minimum Wages Order 2024 P.U. (A) 376). MM2H tiers, compulsory residence purchase and work rights re-verified 2026-09-24 against the MOTAC category pages in the October regwatch wave. Foreign-buyer / rental tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
