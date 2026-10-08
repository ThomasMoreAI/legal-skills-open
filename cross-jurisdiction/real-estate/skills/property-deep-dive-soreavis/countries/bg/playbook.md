# Bulgaria (BG) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: **EUR (eurozone since 1 Jan 2026)** — 21st member; conversion rate locked at 1.95583 BGN/EUR
**Lang**: Bulgarian; English at top banks/legal firms; KAIS cadastre offers EN

---

## Country profile

Bulgaria (~6.4M pop) joined EU 2007 and **completed Schengen integration 1 Jan 2025** alongside Romania. **Bulgaria entered the eurozone 1 Jan 2026** — major event of the 2026 due-diligence cycle (BGN 1.95583/EUR conversion locked since 1999 currency board). Cadastre and Land Register are still **separately maintained** (AGCC vs Registry Agency). Black Sea coast is the country-defining foreign-buyer market — historically Russian-heavy (~5,298 Russian-owned properties in Burgas region alone as of 2023); post-2022 transactions tightening but no mass sell-off. **Toplofikatsiya Sofia in active financial crisis** — Sofia panel-block buyers face winter outage risk 2026-2028. **2024 worst-recorded wildfire season** (~600 wildfires); rural Pirin/Rhodope cheap properties carry elevated fire risk.

---

## Section: `--price`

**Primary index**: **NSI (Национален статистически институт)** — Eurostat-aligned HPI
- https://www.nsi.bg/ + methodology: https://www.nsi.bg/en/metadata/house-price-index-hpi-227
- **Q4 2025 HPI**: 256.71 (2015=100), up from 256.01 in Q3
- **Sofia Q3 2025**: +5.3% QoQ. Stara Zagora led at +7.2%, Varna +5.2%
- **Sofia €/m² level**: residential ~**EUR 1,500–1,900/m²**, new build sometimes >EUR 2,000/m²

**BNB (Bulgarian National Bank)**: https://www.bnb.bg/ — credit aggregates + macro stability

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| Imot.bg | https://www.imot.bg/ | #1 portal, sale + rent |
| Imoti.net | https://www.imoti.net/ | strong agency aggregator |
| Bazar.bg | https://www.bazar.bg/ | classifieds incl. property |
| Alo.bg | https://www.alo.bg/ | classifieds |
| Bulgarian Properties | https://www.bulgarianproperties.com/ | EN-language, foreign-buyer focused (Black Sea coast emphasis) |

**Verdict bands**:
- 🟢 within ±10% of NSI HPI segment for comparable district + condition
- 🟡 ±20%
- 🟠 ±30% — investigate: Black Sea complex maintenance fees? Title clarity in rural Pirin/Rhodope? Toplofikatsiya connection?
- 🔴 >±30%

---

## Section: `--traffic`

- **Agentsiya Patna Infrastruktura (API)** road authority
- Sofia real-time via Waze
- OSM Overpass universal

---

## Section: `--tax`

### Currency note (2026)

BGN no longer Bulgaria's currency. **EUR is legal tender from 1 Jan 2026** (Council Decision 8 July 2025). Conversion rate **1.95583** locked. Mandatory dual display through ~8 Aug 2026. Pre-2026 BGN obligations auto-converted at 1.95583 in deeds. All amounts below in EUR.

### Transfer / acquisition costs (individual buyer)

- **Local acquisition tax (данък при придобиване)**: Set by each of 265 municipalities **between 0.1% and 3.0%**. Applied to higher of declared price or **tax assessment value** (typically below market)
  - **Sofia, Plovdiv, Varna, Burgas, major resorts**: 3.0% typically
  - **Rural / small towns**: as low as 0.5%
- **Notary fee**: progressive (capped) per the regulated Notaries Act tariff. Roughly 0.1%–1.5% of value, max ~EUR 3,000 (regulated figure — verify current tariff, may change). **20% VAT applies on top** of notary fee (not on property price itself for resales)
- **Registration fee at Registry Agency**: 0.1% of price

**Total typical acquisition costs**: ~**2–5%** of price.

### Annual immovable property tax

- Municipal rate: **0.01% to 0.45%** of **tax-assessed value** (NOT market — typically 30–60% of market), per the Local Taxes and Fees Act statutory band. Sofia ~0.18–0.20% for residential (rate set annually per municipality — verify current year with sofia.bg / Local Taxes and Fees Act)
- Levied on land + buildings within development limits (urban + nucleated rural settlements)
- Paid in 2 instalments (30 June and 31 October). **5% prompt-pay discount** if full year paid by 30 April

**Tourist / waste tax (taxa za smet)**: separate municipal levy, often comparable to or larger than property tax itself, especially in resort areas.

### Capital Gains Tax (individuals)

- **Flat 10%** on gain
- **Exemptions** (BG residents and EU/EEA residents only):
  - **One residential property/year** exempt **if held >3 years**
  - **Up to 2 additional properties** exempt **if held >5 years**
- Non-EU residents: full 10% on gains, no holding-period exemption

### Rental income tax

- **10% flat** on net rental income (after 10% statutory deduction → effective 9% on gross). Same for residents and non-residents on BG-source income
- Health/social contributions can apply to residents

### VAT new-build

- **Standard 20%** applies to new buildings (sold by VAT-registered developer or building <5 years from "Akt 16")
- Resales of "old" residential (>5 years post-completion): VAT-exempt
- **No reduced rate for housing** (unlike RO, FR, ES)
- VAT registration trigger: **BGN 100,000 (~EUR 51,130)** over 12 rolling months — reverted from BGN 166,000 effective **1 April 2025** (BGN 166k was only effective 1 Jan – 31 Mar 2025). (2026-05-27 verified, source VATupdate / Taxually / EY)

---

## Section: `--rental`

### STR / Airbnb

- **Tourism Act**: STR must be registered as **Class "B" tourist accommodation** (категоризация) with the local municipality
- **Class A**: hotels, motels, family hotels — full categorization
- **Class B**: guesthouses, guest apartments — simpler regime, used by most Airbnb hosts
- **ESTI (Единна система за туристическа информация)** — registration online; **each guest stay must be reported on the day of check-in** with name, DOB, ID number
- **Tourist tax (such)**: BGN 0.20 to BGN 3.00 per overnight stay → EUR 0.10–1.53 per night post-eurozone, by municipality and class
- **Sofia / Sunny Beach / Varna**: same regime nationwide; resort municipalities (Nesebar, Sozopol, Pomorie, Varna, Burgas) enforce rigorously
- **VAT trigger**: STR turnover >**BGN 100,000 (~EUR 51,130)** over 12 rolling months → mandatory VAT registration → 20% VAT on stays. Reverted from BGN 166,000 on 1 Apr 2025 — steep cliff for full-time mid-scale operators. (2026-05-27 verified)
- **No Sofia-specific cap** on STR (unlike Barcelona, Amsterdam, Paris)

---

## Section: `--work=<profession>`

Sofia IT/services hub; Plovdiv automotive (PIB Trakia + Trakya zones); Varna/Burgas tourism; Bansko ski-season. Bulgaria has substantial IT outsourcing.

---

## Section: `--risks`

### Seismic

- **Main zones**: Sofia, Kresna (SW), Maritsa (Plovdiv area), Gorna Oryahovitsa, Shabla (Black Sea coast)
- Plovdiv has highest provincial seismic hazard ranking; a large share of Plovdiv residential buildings sit in the highest PEI category (specific percentage not publicly verified — confirm with NIGGG-BAS)
- Sofia: historical reference earthquake **18/30 September 1858, M6.5, MSK intensity 9-10** (Vitosha north-margin fault). Probabilistic max design earthquake M~6.5 PGA ~0.16-0.24g
- **NIGGG-BAS (National Institute of Geophysics, Geodesy & Geography)**: https://ndc.niggg.bas.bg/en/ — live seismic data, catalogue
- EFEHR European Seismic Hazard Map integrates Bulgaria

### Flood

- **Coastal**: Black Sea coast (Varna, Burgas, Pomorie) — surge + storm + sea-level rise. Dobruja (NE) flat plains: river flood (Danube tributaries)
- **River**: Maritsa, Iskar, Struma basins. 2014 Mishlitsa, 2017 floods reference events
- INSPIRE Bulgaria flood layers via https://inspire.egov.bg/en

### Forest fire (CRITICAL — 2024 worst recorded year)

- **2024: ~600 wildfires; among the EU's most fire-affected countries by burned area** (EU ranking not source-stamped here — verify with EFFIS / European Forest Fire Information System)
- Hot zones: **Rhodopes (south), Strandzha, Sakar, Pirin** (rural/mountain), Black Sea hinterland (Burgas province)
- 90%+ fires human-caused, but climate-prepared landscape (heatwave, drought) is the multiplier
- **Implication**: rural Pirin/Rhodope cheap properties (often advertised sub-EUR 30k) sit in elevated fire-risk zones with limited insurance availability

### Mandatory diagnostics

- **Energy Performance Certificate** (Сертификат за енергийни характеристики): mandatory for sale or rent. Issued by SEDA-licensed auditor. 10-year validity. Must be presented to buyer prior to deed
- **Akt 16 / Razreshenie za polzvane**: For new builds — Min of Regional Development issues "Akt 16" upon completion; legal certificate that building is fit for occupation. **Buying new-build before Akt 16 is high-risk** (developer can fail finalization). Verify Akt 16 number
- **No mandatory radon test, no mandatory seismic-risk class certificate** at sale (unlike Romania's de-facto Bucharest scrutiny). Asbestos / lead also not in mandatory diagnostic stack
- **Building book (домова книга)**: mandatory for condominium buildings — records of residents, common-area decisions. Verify is up to date

---

## Section: `--mains`

### Cadastre / Land Registry — TWO institutions

- **AGCC (Агенция по геодезия, картография и кадастър)**:
  - https://www.cadastre.bg/en/frontpage — institutional EN/BG
  - https://kais.cadastre.bg/en — **KAIS** (Cadastral Administrative Information System) — public, foreigner-accessible
  - Map browsing free; certified extracts paid (BGN 5–20 ≈ EUR 2.5–10; post-2026 in EUR)
  - Search by **identifikator** (17-digit cadastral, e.g., 68134.500.1234.5.6)
  - https://inspire.egov.bg/en — INSPIRE national geoportal
- **Registry Agency (Агенция по вписванията)**: https://www.registryagency.bg/ — separate, holds land register
- Cadastre and Land Register integration project incomplete countrywide. **Buyer needs both**

### Sofia district heating — major issue

- **Toplofikatsiya Sofia** (~70% of Sofia households connected — coverage share not source-stamped here; verify with Toplofikatsiya Sofia / Sofia municipality). Severe financial distress:
  - Liabilities expected to reach BGN 2.7 billion in 2025
  - >BGN 1 billion debt to natural gas supplier Bulgargaz
  - Gas supplier blocked Toplofikatsiya accounts late 2025
  - **December 2025–January 2026: 6,197 customers without heat/hot water for >48 hours**; mandatory compensation ordered
  - Sofia mayor (Vassil Terziev) requested World Bank/IFC review
- **Buying in a Sofia panel block on toplofikatsiya = real risk of winter outages 2026-2028**

### Other mains
- **Electricity**: Three regional distributors — **EVN** (south, Plovdiv), **Energo-Pro** (north), **ChEZ Razpredelenie / Elektrohold** (west, Sofia)
- **Gas**: **Bulgargaz** (state) wholesale; **Overgas** + regional DSOs retail. Domestic gas penetration low
- **Water**: Local "VIK" municipal companies. Sofia VIK serves capital. Tariffs among the lowest in the EU (ranking not source-stamped here — verify with EurEau / regulator KEVR for a dated tariff)
- **Black Sea coast resort complexes**: many gated complexes on **private water/sewage** maintained by complex management — annual fee EUR 300–1,500+. Not connected to public main. Verify before buying

---

## Section: `--crime`

See `shared/crime-sources.md`. Bulgaria uses:
- **MVR (Ministry of Interior)**: https://www.mvr.bg/
- **NSI criminality data**

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`.

---

## Cost benchmarks (Apr 2026)

| Item | Range / typical |
|---|---|
| Sofia €/m² (Q4 2025) | €1,500–€1,900; new build >€2,000 |
| Plovdiv / Varna / Burgas | €900–€1,400/m² |
| Black Sea complex (resale) | €600–€1,200/m² (varies by complex maintenance) |
| Rural Pirin/Rhodope | €10,000–€50,000 whole houses (fire-risk zone) |
| Local acquisition tax | 0.1–3.0% (Sofia 3.0%) |
| Notary fee | 0.1–1.5% (max ~€3,000) + 20% VAT on fee |
| Registration | 0.1% |
| Total acquisition costs | ~2–5% |

---

## Active fiscal incentives

- **3-year + 5-year residential CGT exemption** schedule (residents/EU/EEA)
- **10% PIT flat** on rental
- **Eurozone entry 1 Jan 2026** structurally reduces FX risk for foreign buyers

---

## Foreign-buyer rules

- **Buildings/apartments**: **All foreigners (EU and non-EU)** can buy buildings, apartments, condominium units freely as individuals
- **Land**:
  - **EU/EEA**: can buy non-agricultural urban land directly since ~2012; agricultural and forest land since 5-year derogation expired (1 Jan 2014); 5-year-residency rule on agricultural land was contested and largely overruled by EU Court for EU buyers
  - **Non-EU**: **CANNOT directly own ANY land** — including regulated urban plots. Standard workaround: register a Bulgarian **EOOD** (sole-owner LLC) or **OOD**; company can own land. Setup ~EUR 1,500–2,000, capital BGN 2 (EUR 1.02). 100% non-EU shareholder allowed for **building/regulated land**, **NOT for agricultural and forest land** (those require EU shareholding)
- **Russian buyers post-2022**:
  - Pre-2022: hundreds of thousands of Black Sea coast properties; Burgas region alone ~5,298 officially Russian-owned (2023)
  - Post-Feb 2022: BG banks closed/refused new accounts for Russian nationals; sales by Russians ~EUR 22M in 2022 — significant but no mass sell-off
  - Implication: complexes with high Russian-owner concentration may have under-maintained common areas, unpaid maintenance dues, distressed sellers — opportunity AND risk
  - Buyers should ask explicitly whether seller is on EU sanctions list; notaries are AML-obligated entities
- **Large transactions** (since 2025): additional source-of-funds checks for transactions >EUR 500,000 (threshold and effective date not source-stamped here — verify with notary / DANS under the Measures Against Money Laundering Act)

---

## Country-specific quirks

- **"Bearer share" exclusion for agricultural land**: Joint-stock companies (AD) with bearer shares cannot own farmland. Rules out many holding structures
- **Soviet-era panel apartments (panelki)**: Built 1960s-1980s, prefabricated concrete. Quality varies; many are cold, poorly insulated; renovation grants from EU funds (NRRP) available. Energy class often F-G. **CORRECTION**: Bulgarian panelki are **condominium-owned (NOT cooperatives)** — Law on Management of Condominium (2009). Each block has mandatory "association of co-owners". The cooperative form (TKZS) was an agricultural-collectivization legacy
- **Black Sea closed complexes (apart-hotels)**: hundreds of thousands of holiday units in Sunny Beach, Sveti Vlas, Pomorie. Typically: (a) historically Russian-owned; (b) over-supplied; (c) burdened with annual maintenance fees EUR 300-1,500+; (d) prices stagnant or falling 2014-2024 in real terms. Re-sale liquidity low outside summer
- **Pirin / Rhodope rural cheap properties**: Genuinely cheap (EUR 10–50k whole houses) but: limited services, fire risk (see §risks), depopulation, often no good road access in winter, traditional houses may have no formal building permit (zaverena regulatsia missing), and ownership chains can be confused (post-restitution sub-divisions among heirs)
- **Dobruja flood plain (NE)**: flat agricultural region; flood risk on Danube tributaries; agricultural land — non-EU buyers blocked from direct ownership
- **Land vs building on plot**: Legal in BG for the building to be owned by one party while the underlying land is owned by another (`pravo na stroezh` / superficies). Foreign individual non-EU can buy the building but the land may need separate BG-company structure
- **AML cash limit**: cash payments **>BGN 10,000 (~EUR 5,113)** in single transaction prohibited. Property deals settle by bank transfer; notary refuses cash above threshold
- **Currency switch transition (2026)**: minor friction during 2026 — POS, banks, utility billing migrating. Notarial deeds drawn after 1 Jan 2026 in EUR; pre-2026 BGN obligations auto-converted at 1.95583

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre (KAIS) | AGCC | https://kais.cadastre.bg/en |
| Land Register | Registry Agency | https://www.registryagency.bg/ |
| HPI | NSI | https://www.nsi.bg/ |
| National Bank | BNB | https://www.bnb.bg/ |
| Min of Finance | MOF | https://www.minfin.bg/ |
| Tax authority (national: PIT, VAT, CIT, CGT) | NRA (Национална агенция за приходите) | https://nra.bg/ |
| Municipal property tax / transfer / tourist tax | Local municipality directly (e.g. sofia.bg) | Administered DIRECTLY by each municipality since 2024 — no longer via NRA. (2026-05-27 verified, source Aidos Bulgaria) |
| Seismology | NIGGG-BAS | https://ndc.niggg.bas.bg/en/ |
| INSPIRE geoportal | egov | https://inspire.egov.bg/en |

---

## Source URL templates

| Field | Template |
|---|---|
| Cadastre lookup | https://kais.cadastre.bg/en |
| HPI | https://www.nsi.bg/en/metadata/house-price-index-hpi-227 |
| Tax / CGT | https://taxsummaries.pwc.com/bulgaria/individual/income-determination |
| Foreign-buyer rules (ELRA) | https://www.elra.eu/contact-point-contribution/bulgaria/limitations-to-foreigners/ |
| Eurozone 2026 entry | https://www.consilium.europa.eu/en/press/press-releases/2025/07/08/ |
| Toplofikatsiya Sofia crisis | https://www.novinite.com/articles/228658/ |

---

## Status

**Confidence**: HIGH on eurozone entry 1 Jan 2026 (multiple verified sources), VAT 20% no reduced rate for housing, CGT 10% with 3yr/5yr exemption schedule, KAIS cadastre + Registry Agency dual-system, non-EU "cannot own land directly" rule, Toplofikatsiya Sofia crisis (2025 documented). MEDIUM on per-municipality acquisition tax rates (265 municipalities; verify per locality), Russian-buyer post-2022 secondary effects (anecdote-heavy). LOW on Black Sea complex maintenance fees per-development (varies; verify per-complex).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)

---

## Extension TODOs

- BGN→EUR transition tracker through ~Aug 2026 dual-display deadline
- Black Sea complex liquidity scoring per-development (Sunny Beach / Sveti Vlas / Pomorie / Sozopol)
- Pirin/Rhodope fire-zone overlay for rural cheap-property scanning
- Toplofikatsiya Sofia connected-block lookup by address
