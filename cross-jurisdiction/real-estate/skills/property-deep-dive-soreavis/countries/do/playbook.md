# República Dominicana 🇩🇴 — Property Due-Diligence Playbook

ISO2: `do`. Status: ✅ Fully populated (researched 2026-05-01).

## Country profile

- **Postcode**: 5 digits, limited everyday use (e.g., `10101` Santo Domingo Distrito Nacional, `23000` La Romana, `45000` Santiago, `33000` Punta Cana / Higüey area). Most addresses rely on `calle, sector, municipio, provincia` rather than CP.
- **Admin levels**: **32 provincias + 1 Distrito Nacional** → **158 municipios** → **distritos municipales** → **secciones / parajes** (rural). Tourist-relevant provinces: La Altagracia (Punta Cana / Bávaro / Cap Cana), Samaná (Las Terrenas / Las Galeras), Puerto Plata (Cabarete / Sosúa / Cofresí), La Romana (Casa de Campo / Bayahibe).
- **Currency**: **DOP** (Peso dominicano). 1 USD ≈ 60–63 DOP (2025 BCRD reference range — verify daily). **USD parallel pricing universal** in resort/tourist property; high-end Punta Cana, Cap Cana, Las Terrenas, Casa de Campo deals are USD-denominated. Non-tourist housing (Santo Domingo middle market, Santiago, San Cristóbal) typically priced in DOP.
- **Languages**: Spanish (official). English widely used in Punta Cana, Las Terrenas, Sosúa, Cabarete, Cap Cana resort sectors. French + Italian common in Las Terrenas (large expat colony).
- **Cadastre / land registry**:
  - **Jurisdicción Inmobiliaria** (Land Registration Jurisdiction, est. by **Ley 108-05** of 2005, in force 2007): `https://ji.gob.do/`
  - **Tribunal Superior de Tierras (TST)**: appellate court for title; sits in 4 regional jurisdictions (Norte, Central, Departamento Este, Departamento Noreste)
  - **Registro de Títulos**: per-jurisdiction title office issuing `Certificado de Título`
  - **Dirección Nacional de Mensuras Catastrales (DNMC)** — surveyor-side cadastre: `https://indomet.gob.do/`
- **Identifier**: `Designación Catastral` (e.g., `parcela X, distrito catastral Y, municipio Z`) + `Matrícula` (modern post-saneamiento) OR legacy `Certificado de Título` numbering. After **saneamiento** (registration purification), title is held under a **Matrícula** in the unified Registry.
- **Ownership types**: **Dominio pleno** (freehold; foreigners on equal footing per Constitución art. 51 + **Ley 195-69**); **Condominio** (**Ley 5038-58**); **SA / SRL** corporate holding (estate-planning, anonymity); **Fideicomiso inmobiliario** (Ley 189-11; common for development trusts + CONFOTUR); **Concesión** for state coastal bands — first 60 m from high-tide line is public (**Ley 305-68 Zona Marítima Terrestre**), all beachfront subject to setback rules.
- **Recent reforms**: **Ley 108-05** Registro Inmobiliario (in force 2007 — Torrens-style title); **Ley 158-01 + 195-13** CONFOTUR; **Ley 155-17** AML (beneficial-owner + sworn source-of-funds); **Ley 189-11** trust law (fideicomiso); **Ley 358-05** General Consumer Protection Law (Pro Consumidor enforcement for developer-to-consumer purchases — new construction, off-plan); **DGII Norma 06-2017** digital IPI/transfer filing; annual DGII Resolución indexes IPI threshold (**DOP 10,695,494 for 2026** per DGII Resolución DG-AR1-2026-00001 — verify current year at filing) (2026-05-27 verified).

---

## Section: `--price`

### Primary sources

- **BCRD**: `https://www.bancentral.gov.do/` — mortgage-portfolio aggregates + FX. **No official residential price index parcel-level**.
- **ONE (Oficina Nacional de Estadística)**: `https://www.one.gob.do/` — Censo 2022 housing stock by provincia/municipio.
- **DGII**: `https://www.dgii.gov.do/` — `Avalúo Catastral` not publicly searchable per parcel; indexed thresholds published annually.
- **MITUR**: `https://mitur.gob.do/` — CONFOTUR-registered project list (verify resolution number before pricing incentives).

### Listing platforms

- **SuperCasas** (DOMINANT generic): `https://www.supercasas.com/`
- **Inmobiliaria.com.do**, **A2 Inmuebles**, **Remax DR**, **Coldwell Banker DR**, **Century 21 DR**, **Keller Williams DR**
- Resort developer direct: Cap Cana Heritage, Casa de Campo, Punta Cana Resort & Club, Tropicalia Samaná
- Foreign-buyer-targeted: **PointTwo Homes**, **DR Sotheby's**, **Punta Cana Real Estate**

### 2025-2026 price benchmarks

> All figures `est.` from listing-platform aggregation + Global Property Guide (Q4 2024) + Coldwell Banker DR market reports — secondary-tier; cross-check with **3+ live SuperCasas comparables** for the specific sector before relying.

| Sector | USD/m² (typical, condo) | Notes |
|---|---:|---|
| **Cap Cana (oceanfront / beachfront)** | $4,000–$8,000+ | Premium gated; CONFOTUR projects common |
| **Punta Cana / Bávaro (resort condo)** | $1,800–$3,500 | High volume; CONFOTUR widespread |
| **Las Terrenas (Samaná)** | $2,000–$3,800 | French/Italian expat premium |
| **Casa de Campo (La Romana)** | $3,000–$6,500 | Luxury gated, golf |
| **Sosúa / Cabarete (Puerto Plata)** | $1,500–$2,800 | Mature expat market |
| **Santo Domingo — Piantini / Naco** | $2,200–$3,500 | DOP-priced typical; convertible |
| **Santo Domingo — Bella Vista / Mirador Sur** | $1,500–$2,400 | Upper-mid |
| **Santiago — centro / Cerros de Gurabo** | $900–$1,600 | Second city |
| **Inland (San Cristóbal, La Vega rural)** | $400–$900 | Local-market pricing in DOP |

**Trend**: **+5 to +8 % YoY nominal in USD-denominated tourist zones** through 2024 (Global Property Guide H2-2024 — secondary source; verify with BCRD when published). DOP-priced inland housing tracks DOP inflation (BCRD CPI ~3–4 % 2024).

### Compute

1. USD/m² = price ÷ **m² construcción** (built area; clarify if listing reports `área de construcción` vs `área total / solar`).
2. Compare to ≥ 3 active SuperCasas comparables in the same `sector` + project (HOA discipline matters more than municipio average).
3. **CONFOTUR vs non-CONFOTUR delta**: identical-spec units in CONFOTUR-registered projects can carry ~5-10 % price premium that buyers recoup via 15-yr IPI + transfer-tax exemption — verify project's CONFOTUR resolution number with MITUR.
4. **Trap — currency**: confirm whether price is **USD firme**, **DOP**, or DOP "al cambio" (FX-linked). Closing FX shifts can move the deal by 2-3 % over a 60-day escrow.
5. **Trap — area definitions**: `m² construcción cerrada`, `m² construcción total` (incl. terrazas), `m² solar`. Listings often quote the largest of these without flagging.

### Key terms

- **Certificado de Título** (legacy) / **Matrícula** (post-saneamiento) — title evidence
- **Designación Catastral** — `parcela X, DC Y, municipio Z`
- **Saneamiento** — Torrens-style title quieting (judicial)
- **Constancia Anotada** — historical document, **NOT a clean title** (precursor to Matrícula); verify if Constancia has been converted via saneamiento
- **Acta de Mensura** — boundary survey signed by `agrimensor` registered with DNMC
- **CONFOTUR** — Consejo de Fomento Turístico (Ley 158-01 + 195-13)
- **Solar** — land plot
- **Sector** — neighbourhood (sub-municipal)

---

## Section: `--traffic`

### Sources

- **DIGECITRAN** (Dirección General de Tránsito Terrestre) under Instituto Nacional de Tránsito y Transporte Terrestre **INTRANT**: `https://intrant.gob.do/`
- **MOPC (Ministerio de Obras Públicas y Comunicaciones)**: `https://mopc.gob.do/` — road inventory + some `Tránsito Promedio Diario Anual (TPDA)` counts published in tender / feasibility documents (not a public live portal).
- **OSM** fallback via Overpass — `highway` tag class.

### Key term

**TPDA (Tránsito Promedio Diario Anual)** = AADT-equivalent. Public TPDA coverage is sparse outside MOPC feasibility studies for the autopistas (DR-1 / Autopista Duarte, DR-3 / Las Américas, DR-5 / del Coral, DR-7 / Punta Cana–Bávaro toll). For most secondary roads, **rely on OSM road class + on-ground observation**.

### Verdict bands (heuristic; calibrate with on-site visit)

- 🟢 < 1,500 v/d (residential `calle interior`, gated subdivisión interior)
- 🟡 1,500–10,000 v/d (`avenida secundaria`, suburban arterial)
- 🟠 10,000–35,000 v/d (urban arterial, Bulevar Turístico del Este, secondary autopista feeders)
- 🔴 > 35,000 v/d (Autopista Las Américas DR-3, Autopista Duarte DR-1, 27 de Febrero / Núñez de Cáceres in Santo Domingo, Bulevar 1ro de Noviembre Punta Cana peak)

### Coarse OSM fallback

| OSM `highway` | DR road class | Typical v/d |
|---|---|---|
| `motorway` | Autopista (DR-1/3/5/7) | 20,000–80,000 |
| `trunk` | Carretera nacional principal | 8,000–30,000 |
| `primary` | Carretera principal | 3,000–15,000 |
| `secondary` | Carretera secundaria | 1,000–5,000 |
| `tertiary` / `residential` | Calle / camino vecinal | < 1,500 |

### Caveats

- **Motoconchos (motorcycle taxis)** dominate noise profile in many secondary towns — counts under-represent acoustic nuisance.
- **Resort access roads** (Bulevar Turístico Punta Cana, Coral Highway) carry seasonal peaks (high season Dec–Apr, Semana Santa).

---

## Section: `--tax`

### Annual property tax — IPI (Impuesto al Patrimonio Inmobiliario)

Governed by **Ley 18-88** (as amended) + **DGII Norma 06-2017** + annual indexation Resolution.

- **Rate**: **1 %** on the portion of the **aggregate registered value of all real estate held by an individual** that **exceeds the exemption threshold**.
- **Exemption threshold (2026)**: **DOP 10,695,494** per individual owner aggregate (DGII Resolución **DG-AR1-2026-00001**, annual indexation per Ley 18-88 art. 2 as amended by Ley 253-12 art. 14 — verify current-year figure at `https://www.dgii.gov.do/` under "IPI"). Approx. **USD 182,206** at Jan-2026 FX. (Prior 2025 threshold was DOP 9,860,649) (2026-05-27 verified, source DGII Resolución DG-AR1-2026-00001).
- **Tax base**: DGII appraisal value (`Avalúo Catastral`), **NOT market price**. Avalúo lags market ~30-50 % in prime tourist zones (est., based on observed DGII appraisal-vs-listing spreads — verify per parcel by requesting the seller's Avalúo Catastral); updated periodically per DGII resolution (commonly 5-yr cycle, but cycle variable — verify).
- **Filed annually**, paid in **two semestres** (typically **11 March + 11 September** per DGII annual calendar — verify exact year-specific date at https://dgii.gov.do/).
- **Primary residence**: same threshold applies; no separate primary-residence exemption beyond the DOP 10.7M floor, BUT individuals **65+ owning a single property held ≥ 15 years** receive total IPI exemption (Ley 18-88 art. 2).
- **Held in SA / SRL**: **1 % on full value (no threshold)** — the per-individual threshold doesn't transfer to corporate holders; this changes the math significantly above the threshold.

### CONFOTUR exemption

For property in a CONFOTUR-registered project under **Ley 158-01 + 195-13**:

- **100 % IPI exemption** for **15 years** from CONFOTUR resolution date
- **100 % transfer-tax exemption** on the first transfer from the developer
- **ITBIS exemption** on materials + services during construction (developer-side, but reflected in price)
- **Verification**: MITUR maintains CONFOTUR resolution registry — request `Resolución CONFOTUR` number from seller/developer; **never rely on marketing claim alone**.

### Transfer tax (one-time at purchase) — Impuesto de Transferencia Inmobiliaria

- **Rate**: **3 %** on the higher of (a) contract price or (b) DGII appraisal (`Avalúo`).
- **Form**: DGII `IR-17` (currently `Formulario IR-17` or successor — verify on DGII).
- **Buyer pays by custom**, but legally either party can be designated.

### Closing-cost stack

| Item | Rate / amount | Who pays (custom) |
|---|---|---|
| Transfer tax (DGII) | **3 %** of higher of price/appraisal | Buyer |
| Notary `acta auténtica` + legalisations | **0.25–1 %** (capped sliding scale per **Tarifa Notarial**, custom 1 % typical) | Buyer |
| Lawyer (`abogado`) + title due-diligence | **1.0–1.5 %** | Buyer |
| Registry fee (`Registro de Títulos`) | **~0.5 %** (sliding) | Buyer |
| **Subtotal (non-CONFOTUR resale)** | **~5.5–6 % of price** | Buyer |
| **Subtotal (CONFOTUR new)** | **~1.5–2.5 %** (transfer waived) | Buyer |

### ITBIS (VAT)

- **18 %** on **new construction sold by developer** as part of habitual activity. **Not on resales between individuals**.
- ITBIS may apply to short-let services (see `--rental`).

### Capital gains — Ganancia de capital

- Treated as ordinary income under **Código Tributario art. 289**.
- **Resident individuals**: progressive PIT (currently up to **25 %** above DOP ~867k bracket — annual indexation).
- **Resident corporations**: **27 %** flat.
- **Non-residents selling DR property**: buyer (or notary) **withholds 1 % of sale price** as advance payment; final liability reconciled on filing — withholding is a credit, not a final tax.
- **Cost basis**: original acquisition price + documented improvements + inflation adjustment per DGII published indexes.

### Inheritance / estate tax — Sucesiones

- **3 % flat** on the net taxable estate (after deductions). Among the **lowest in the Americas** — material for estate planning. (Ley 2569 + Ley 288-04.)

### Summary

| Cost item | Ballpark |
|---|---:|
| Annual IPI (above threshold, individual) | 1 % of avalúo above DOP 10.7M (2026 threshold DOP 10,695,494; DGII Resolución DG-AR1-2026-00001) |
| Annual IPI (CONFOTUR project, first 15 yrs) | **0** |
| Transfer + notary + legal + registry (non-CONFOTUR) | **~6 % of price** |
| Transfer + notary + legal + registry (CONFOTUR new) | **~1.5–2.5 %** |
| ITBIS on new construction | 18 % (in developer price; explicit on invoice) |
| Capital gains (resident individual) | up to 25 % progressive |
| Capital gains (non-resident) | 1 % withholding + final reconciliation |
| Estate / inheritance | **3 %** |

⚠️ Verification: request seller's last **IPI receipt** (`recibo de pago IPI`) AND their **DGII Avalúo Catastral**. Confirm CONFOTUR resolution number directly with MITUR if claimed.

---

## Section: `--rental`

### Long-term residential rentals

Governed by **Ley 4314 + Ley 17-88** + **Reglamento del Inquilinato**. Standard 1-2 yr contracts; **security deposit held by Banco Agrícola** (mandatory state escrow under Ley 4314) — 2 months typical. Tenant protection moderate; **eviction (`desahucio`) is judicial and slow — ~6-18 months is commonly reported by DR practitioners (est.; verify with a local abogado for the specific tribunal)**.

### Long-term rental tax (resident landlord)

- **Individual**: progressive PIT up to **25 %** on net rental income (gross minus 30 % standard deduction per **Código Tributario art. 314** OR documented expenses).
- **Corporate (SA/SRL)**: **27 %** flat on net.
- **Non-resident landlord**: **27 % withholding on gross rents** (no deduction allowed at withholding stage; deductions claimed only via DGII filing).
- **ITBIS 18 %**: long-term residential rentals **exempt**; commercial rentals + short-term hotel-like rentals **subject**.

### Short-term rentals (Airbnb / `vivienda vacacional`)

Regulatory status (verified 2026-04):

- **MITUR** classifies tourism accommodation under **Ley 541-69** + reglamentos. Categorías: `Hotel`, `Apart-hotel`, `Vivienda vacacional / turística` — last requires MITUR registration (`Registro Nacional de Prestadores de Servicios Turísticos`) when operated commercially.
- **Permits**: MITUR registration + municipal `Uso de Suelo` + Bombero / Defensa Civil safety permit (if >4 rooms).
- **HOA reality**: in Cap Cana, Casa de Campo, Punta Cana Resort & Club, Roco Ki, etc., **HOA `reglamento interno` is the binding constraint** — many forbid <30-day rentals or require central rental-pool participation. Read before pricing a yield model.
- **Tax**: income same as long-term (progressive / 27 % corp / 27 % non-resident WHT). **ITBIS 18 %** applicable to lodging services + historical **10 % `Impuesto al Hospedaje`** on hotel-style services (enforcement variable per municipio; consult lawyer).
- **Punta Cana / Bávaro** = broadly tolerated, HOA-by-HOA. **Las Terrenas** = mature STR, MITUR registration spotty in practice. **2024-2026 trend**: enforcement tightening, formalisation pressure rising.

### Strategic notes

- Best STR yields: **Punta Cana / Bávaro / Cap Cana** (resort access, year-round inventory turnover, branded rental pools). Net yields commonly cited at 5-9 % — **secondary aggregator data; verify per-project**.
- **Las Terrenas** has high seasonality (Euro winter peak Dec-Apr); summer demand thinner.
- **Cabarete / Sosúa** kitesurf-driven seasonality (Dec-Apr + Jun-Aug peaks).
- **Santo Domingo** STR nascent; mostly business-traveller corporate.
- **CONFOTUR + MITUR registration + HOA approval** = the three boxes to tick before pricing a yield model.

---

## Section: `--work=<profession>`

### Job platforms

- **Empleos.com.do**, **Computrabajo DR**, **LinkedIn DR** (active in finance/tech/tourism), **Indeed DR**, **Multitrabajos**
- **Ministerio de Trabajo**: `https://mt.gob.do/`

### Self-employment / business

**RNC (Registro Nacional de Contribuyentes)** required for invoicing (via DGII). **Régimen Simplificado (RST)** for small taxpayers below DGII threshold. **SA** or **SRL** common (Ley 479-08; minimum capital nominal). **Profesión liberal** roles need colegio profesional registration; foreign-degree `exequátur` via Ministerio de Educación Superior.

### Foreign worker

**Migración**: `https://migracion.gob.do/` — work-related residency under **Ley 285-04**. Categories: **Residencia por Inversión** (DGM minimum USD 200,000 contributed as foreign capital to a DR company / free-zone / incentive-regime company (2026 data, source DGM service page on gob.do); direct real-estate purchase not listed as a route and naturalization period not stated on the MIP page — verify at DGM + MIP); **Pensionado** (USD 1,500/mo lifetime pension); **Rentista** (USD 2,000/mo stable income, both with 50 % discount on most domestic taxes for 5 years per Ley 171-07); **Empleo asalariado** (employer-sponsored).

### Salary benchmarks (2024-2025)

> Source: ONE + Ministerio de Trabajo wage tables; verify current year via `https://mt.gob.do/` "Salarios Mínimos".

- **Salario Mínimo Nacional Privado** (no-zona-franca, sectorial) 2025: **DOP 17,200 – 28,500 / month** by company size (CNS Resolución 02/2024).
- **Median private-sector gross 2024**: ~DOP 25,000–35,000 (~USD 400–560) — ONE Encuesta Continua de Empleo.
- **Punta Cana hospitality**: tipped roles multiply base via service charge.
- **Banca / corporate / tech (Santo Domingo)**: USD 1,200–4,000/mo professional roles est.

### Catchment heuristics

- Within 30 min of **Santo Domingo**, **Santiago**, **Punta Cana** = full job market.
- Within 30 min of **Puerto Plata**, **La Romana**: mid-market + tourism.
- **Las Terrenas, Cabarete, Bayahibe, Samaná town**: thin local salaried market; expat self-employment + remote work dominant.
- **Inland rural** (Cordillera Central, Línea Noroeste): subsistence + agriculture; very thin formal employment.

---

## Section: `--risks`

### Primary national hazard sources

| Source | URL | What it gives |
|---|---|---|
| **ONAMET (Oficina Nacional de Meteorología)** | `https://onamet.gob.do/` | Tropical cyclones, rainfall, drought |
| **COE (Centro de Operaciones de Emergencias)** | `https://coe.gob.do/` | Plan Nacional de Riesgos, evacuation, alerts |
| **CNE (Comisión Nacional de Emergencias)** | `https://cne.gob.do/` | Civil protection coordination |
| **SGN (Servicio Geológico Nacional)** | `https://sgn.gob.do/` | Seismic hazard, landslides, geological maps |
| **INDRHI (Instituto Nacional de Recursos Hidráulicos)** | `https://indrhi.gob.do/` | Hydrology, flood basins, dam status |
| **Ministerio de Medio Ambiente** | `https://ambiente.gob.do/` | Forestry, coastal, ecosystem |
| **MIVHED CDCRD** (Código de Construcción de la RD, Vol. I; wind loads per ASCE 7-22, Título 2) + legacy **MOPC R-001 / R-007** | building code (seismic + wind) | CDCRD oficializado by MIVHED Resolución 007-2026 (Apr 2026, one-year transition — secondary press reports; verify at mivhed.gob.do); R-001 2011 / R-007 2008 for earlier projects |

### Hurricane (Atlantic basin)

- **Season**: **Jun 1 – Nov 30**, peak **Aug-Oct**.
- **Historical reference**: **David 1979** (catastrophic, baseline for code revisions); **Georges 1998** (full-island traverse, drove tightening); **Jeanne 2004** (north-coast flooding); **Maria 2017** (passed N, rainfall + surge); **Fiona 2022** (Cat 1 landfall east coast Sep-2022, tested resort infrastructure).
- **Implication**: post-2008 resort-grade builds meet stronger code; pre-2000 non-resort builds often do not.
- **Insurance**: hurricane peril bundled with all-risk fire; CAT deductibles ~2-5 % of sum insured (est., market-typical — verify in the specific carrier's póliza); rates ~0.25-0.6 % of insured value/yr est. (Superintendencia de Seguros `https://superseguros.gob.do/`).

### Flood

- **High-risk basins**: **Yuna** (Samaná Bay drainage), **Yaque del Norte** (Cibao), **Yaque del Sur** (Barahona / Azua), **Ozama-Isabela** (Santo Domingo metro).
- **Urban Santo Domingo**: combined-sewer flash flooding common in `Los Tres Brazos`, `Capotillo`, `Villa Mella` after heavy rain.
- **Coastal surge**: Bayahibe, Boca Chica, Juan Dolio low-lying; Punta Cana itself relatively elevated but Bávaro beach back-of-resort flat.
- **INDRHI** publishes basin-level flood maps (PDF / GIS) but **no consolidated public parcel-level flood-zone web viewer** equivalent to FEMA / Géorisques. **Verification path**: request from INDRHI per-parcel review OR municipal `Plan de Ordenamiento Territorial` (POT).

### Seismic

- **Active structures**: **Septentrional Fault** (E–W across northern DR — Puerto Plata, Cibao; >M7 capability; SGN paleoseismic studies suggest ~800-1,200 yr return); **Enriquillo–Plantain Garden Fault** (south — drove **Haiti 2010 M7.0**, eastern segment crosses DR south); **Muertos Trough** offshore subduction south (tsunamigenic); **North Hispaniola subduction** offshore north.
- **Major historical**: Santiago 1842 (~M7.5), Samaná 1946 (M8.0 + tsunami), Mona Passage 1918, Puerto Plata 2003 M6.5.
- **Hazard zoning**: **MOPC R-001** seismic zones 1-4; Santiago / Cibao = highest. Post-2011 R-001-compliant builds materially safer; pre-1979 builds particularly weak.

### Landslide / mass movement

- **Cordillera Central** (Constanza, Jarabacoa, San José de Ocoa) + **Cordillera Septentrional** (Puerto Plata hinterland) — chronic landslide risk during hurricane / tropical-storm rains.
- **SGN** maintains susceptibility maps; municipal `POT` is the binding planning document.

### Climate change projections (2050 horizon)

- **Hurricane intensity** trending up (more Cat 4-5 share) — IPCC AR6 + NOAA Atlantic basin assessments.
- **Sea-level rise**: +20-50 cm by 2100 (RCP4.5–8.5 range); **acute exposure in Punta Cana east-facing beaches, Bávaro back-shore, Boca Chica, Samaná town malecón** — IPCC AR6 + Climate Central Coastal Risk Screening Tool.
- **Drought**: South-west (Barahona, Pedernales, Azua) + Línea Noroeste increasingly arid; reservoirs (Sabaneta, Sabana Yegua, Tavera) under pressure.
- **Coral / marine ecosystem stress** affecting beach sand replenishment + coastal-protection economics.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1979 (David)** | No seismic code; weak masonry; lead paint; asbestos in roofing common |
| **1979–2000** | Patchwork code; Georges 1998 exposed weaknesses; asbestos likely |
| **2000–2008** | Modernising; **R-007 (hurricane / wind)** tightened post-Georges |
| **2008–2011** | R-007 in force; transition to R-001 |
| **Post-2011** | **R-001 + R-007 enforced** — modern seismic + wind; resort-grade typically exceeds with international engineering |
| **Post-2022 (Fiona)** | Some resort developments retroactively reinforcing roofing + glazing |

### MANDATORY title / due-diligence diagnostics

| Document | Source | Why critical |
|---|---|---|
| **Certificado de Título / Matrícula** (current) | Registro de Títulos | Sole legal title evidence |
| **Estado Jurídico del Inmueble** | Registro de Títulos | Lists encumbrances, mortgages, liens, oposiciones |
| **Constancia Anotada review** (if pre-saneamiento title) | Lawyer + Registro | Verify saneamiento has happened — otherwise title is not Torrens-clean |
| **Acta de Mensura** + **Plano** | Agrimensor + DNMC | Boundary survey; must match Registro |
| **Certificación de No Acreedores** | Registro de Títulos | Confirms no creditor claims at moment X |
| **IPI receipts (last 4 yrs)** | DGII | Confirms no tax arrears (DGII can lien) |
| **CAASD/INAPA/EDESUR/EDENORTE/EDEESTE no-debt** | Utility | Utilities can encumber |
| **HOA `Estado de Cuenta`** | HOA | Outstanding HOA fees follow the unit |
| **Permisos de Construcción + Uso de Suelo** | Ayuntamiento | Verifies legal construction + permitted use |
| **Sworn declaration source of funds** (Ley 155-17) | Buyer notarised | AML compliance — non-resident buyers |

### Risk dashboard — typical resort condo (Punta Cana / Bávaro)

| Class | Severity | Action priority |
|---|---|---|
| Hurricane | 🟠 | Confirm post-2011 build + insurance + impact glazing |
| Flood (storm surge) | 🟡-🟠 | Verify elevation + project drainage |
| Seismic | 🟡 | R-001 compliance in build-era |
| Landslide | 🟢 | Coastal flat — generally not applicable |
| Title | 🟠-🔴 | **Single biggest DR-specific risk** — full lawyer due-diligence non-negotiable |
| Climate / SLR (long-term) | 🟠 | 2050+ exposure if oceanfront < 5 m AMSL |

---

## Section: `--mains`

### Water + sewer operators

| Operator | Coverage |
|---|---|
| **CAASD (Corporación de Acueducto y Alcantarillado de Santo Domingo)** | Distrito Nacional + Santo Domingo provincia |
| **CORAASAN** | Santiago |
| **CORAAPLATA** | Puerto Plata |
| **CORAAMOCA** | Moca / Espaillat |
| **CORAAROM** | La Romana |
| **CORAABO** | Boca Chica / San Cristóbal corridor (per recent reorg) |
| **INAPA (Instituto Nacional de Aguas Potables y Alcantarillados)** | All other municipios + rural |

URL hubs: `https://caasd.gob.do/`, `https://www.coraasan.gob.do/`, `https://inapa.gob.do/`.

### Sewer reality

- **Urban Distrito Nacional + central Santiago / Santo Domingo**: combined/separate sewer; coverage variable by sector — Piantini / Naco / Bella Vista mostly served, peripheral barrios variable.
- **Resort communities** (Cap Cana, Casa de Campo, Punta Cana Resort & Club, Las Terrenas central): project-internal water + sewer (private package plants + bulk supply), typically fully reticulated.
- **Outlying / rural**: **septic (`pozo séptico`) + cistern (`cisterna`) is standard**, not mains. Cistern fed by truck (`camión cisterna`) or shallow well + pump.
- **Listing clue**: "cisterna y pozo séptico" = no mains; "conectado a alcantarillado" = mains (verify with operator).
- **Potability**: even where mains exist, **not assumed potable** — bottled/filtered drinking water near-universal across DR.

### Power

**Distributors**: **EDESUR** (south), **EDENORTE** (north), **EDEESTE** (east incl. Punta Cana / La Romana). Regulator: **SIE (Superintendencia de Electricidad)**. Reliability historically poor (`apagones` frequent) — **`planta eléctrica` + `inversor + baterías` standard for any resort property and most middle-class urban housing**. Resort developments have project-level backup; standalone villas need their own kit.

### Costs

| Scenario | Cost (USD est.) |
|---|---:|
| Mains water connection (urban, where line exists) | $200–$700 |
| Septic tank install (3-bedroom equivalent) | $1,500–$5,000 |
| Cisterna 1,000-2,000 gal install | $1,500–$4,000 |
| Pump + pressurisation | $400–$1,200 |
| Planta eléctrica diesel 8-15 kVA | $3,000–$8,000 |
| Inversor + bank of batteries (lithium 5-10 kWh) | $4,000–$12,000 |
| Solar PV 5 kW + inverter | $7,000–$14,000 |

---

## Cost benchmarks (DO 2026)

| Item | Cost |
|---|---:|
| Lawyer + title due-diligence | **1.0–1.5 %** of price |
| Notary `acta auténtica` | **0.25–1 %** (typical 1 %) |
| DGII transfer tax (non-CONFOTUR) | **3 %** |
| Registro de Títulos fee | **~0.5 %** |
| Acta de Mensura / boundary survey (where required) | **USD 1,500–5,000** |
| Title study (`estudio de título`) | **USD 800–2,500** included in lawyer fee |
| Independent inspector (estructural) | **USD 500–1,500** |
| **Total transaction cost (non-CONFOTUR)** | **~5.5–6 %** of price |
| **Total transaction cost (CONFOTUR new)** | **~1.5–2.5 %** |
| Annual IPI (above threshold, individual) | 1 % of avalúo above DOP 10.7M (2026 threshold DOP 10,695,494; DGII Resolución DG-AR1-2026-00001) |
| HOA fees (Punta Cana / Cap Cana / Las Terrenas resort condos) | USD **200–2,000 / month** |
| Hurricane + all-risk insurance | 0.25–0.6 % of insured value/yr est. |
| Planta + inverter + battery package | USD **3,000–15,000** |
| Roof retrofit (concrete, post-Fiona reinforcement) | USD **8,000–25,000** |

## Active fiscal incentives + visa programs (2025-2026)

### Tax-incentive regimes

- **CONFOTUR** (Ley 158-01 + 195-13) — **15-yr 100 % IPI + transfer-tax exemption + ITBIS construction-side relief** for property in registered tourism-development projects. Geographic scope: Punta Cana, Bávaro, Cap Cana, Bayahibe, La Romana / Casa de Campo, Las Terrenas, Las Galeras, Samaná, Puerto Plata, Sosúa, Cabarete, Río San Juan, plus designated mountain (Jarabacoa, Constanza) + colonial (Santo Domingo Zona Colonial) sub-zones. **Always verify project's CONFOTUR resolution number with MITUR.**
- **Ley 28-01** Border Development — 100 % income / IPI / ITBIS exemption for qualifying activities in 7 border provinces (Pedernales, Independencia, Elías Piña, Dajabón, Montecristi, Santiago Rodríguez, Bahoruco) — niche for property buyers; mostly industrial.
- **Ley 57-07 Renewable Energy** — incentives for solar PV / wind installations (some applicable to residential).
- **Ley 171-07 Pensionados y Rentistas** — pensioners + rentistas: 50 % discount on transfer tax + IPI exemption (for primary residence) + customs exemptions on household items + tax-exempt remittances of pension/rentista income. Real-estate transfer of `casa única` capped exemption.

### Residency / citizenship

- **Residencia por Inversión** (Ley 285-04 migration framework + reglamento Migración; Ley 171-07 supplies the 50 % domestic-tax-discount overlay) — minimum **USD 200,000** (2026 data, source DGM service page on gob.do) contributed as foreign capital to a DR company registered with CEI-RD (Ley 16-95), a free-zone company, or an incentive-regime company (Ley 84-99 / 8-90 / 158-01 / 28-01 — no minimum where foreign capital is present); direct real-estate purchase is not listed as a route on that page and the naturalization period is not stated on the MIP naturalización page — data not publicly available, verify at DGM (`https://migracion.gob.do/`) and MIP (`https://mip.gob.do/`).
- **Pensionado**: USD **1,500/month** lifetime pension → residency.
- **Rentista**: USD **2,000/month** stable income from non-DR sources → residency.
- **One-day-per-year physical presence** sufficient to maintain residency once granted.

## Common listing platforms

- **SuperCasas** — DOMINANT generic
- **Inmobiliaria.com.do**
- **A2 Inmuebles**
- **Remax DR**, **Coldwell Banker DR**, **Century 21 DR**, **Keller Williams DR**
- **Sotheby's International Realty DR** (Casa de Campo, Cap Cana high-end)
- **PointTwo Homes**, **Punta Cana Real Estate**, **Tropicalia Samaná** — foreign-buyer-targeted
- **Resort developers direct**: Cap Cana Heritage, Punta Cana Resort & Club, Casa de Campo, Roco Ki, Tropicalia, Cap Cana Marina

## Caveats unique to DO

- **Title chain is the single biggest risk in DR**. Pre-2007 (pre-Ley 108-05) titles can have parallel claims, missing saneamiento, cadastral mismatches. **Constancia Anotada is NOT a clean Torrens title** — buyer must verify saneamiento has been completed and a Matrícula issued.
- **Mandatory lawyer (`abogado`) — not just notary**. The notary authenticates signatures; **title due-diligence is a lawyer-only function** in DR practice. Never close on notary alone.
- **CONFOTUR vs non-CONFOTUR delta is huge** — 15 yrs IPI + transfer waiver. Always verify the project's CONFOTUR resolution number directly with MITUR before pricing the deal.
- **USD vs DOP pricing** — confirm `USD firme` vs `DOP al cambio` in the contract; FX shifts during escrow can move final wire by 2-3 %.
- **Hurricane insurance**: bundled with all-risk fire, but post-Fiona 2022 some carriers tightened terms in Punta Cana / Bávaro. Verify carrier still writes the geography + sublimits for windstorm.
- **HOA fee transparency in resort communities** is uneven. Insist on **3 yrs HOA financials + reserve-fund statement**; special assessments (post-hurricane roof retrofit, beach replenishment) are common and material.
- **Power reliability + planta cost**: budget USD 3-15k for generator/inverter even on a "modern" property unless a resort with project-grade backup.
- **Servidumbres (rights of way)** on rural / hillside land — verify in `Acta de Mensura` and Registry; informal access tracks across neighbours' parcels are widespread and create disputes.
- **Squatter / `acción reivindicatoria` / posesión**: vacant land buyers must verify possession history; **prescripción adquisitiva** can convert long-term occupants into legal owners. Walk the boundary; talk to neighbours; check for fence-lines that disagree with your survey.
- **Sociedad inmobiliaria / SA / SRL holdings**: very common; affects beneficial-owner disclosure (Ley 155-17), CONFOTUR transferability, and the 1-%-with-no-threshold IPI on corporate holders.
- **Beachfront 60-m public band (Ley 305-68)**: no private construction within 60 m of high-tide line; beachfront houses sit behind this band. Verify setback compliance with municipal `Uso de Suelo`.
- **AML — Ley 155-17**: non-resident buyers must execute a **sworn declaration of source of funds** at notary; bank accounts opened to wire purchase price subject to KYC + UAF review.
- **Drug-trafficking-adjacent provinces** (parts of border belt + some northern coast pockets) carry reputational + insurance flags — diligence on neighbourhood + sector matters.

## Reddit / forum sources

- **r/Dominican** — biggest DR-resident community
- **r/dominicanrepublic** — mixed expat + tourist
- **r/expatfin**, **r/expats** (DR threads)
- **DR1 Forum** (`https://www.dr1.com/forums/`) — long-running expat forum, deep historical Q&A
- **Punta Cana Living** (`https://puntacanaliving.com/`) — Punta Cana-specific
- **Samaná en Línea** / **Las Terrenas News** — local expat coverage
- **The Dominican Today** (English news)

## Verification authorities

| Authority | When to call |
|---|---|
| **Tribunal Superior de Tierras (TST) / Jurisdicción Inmobiliaria** | Title disputes, saneamiento status |
| **Registro de Títulos** (per jurisdiction) | Certificado / Matrícula / Estado Jurídico |
| **DNMC (Dirección Nacional de Mensuras Catastrales)** | Acta de Mensura, plano cadastral |
| **DGII** | IPI + transfer tax + Avalúo + RNC + AML compliance |
| **MITUR (Ministerio de Turismo)** | CONFOTUR resolution verification |
| **Migración (DGM)** | Residency by investment / pensionado / rentista |
| **ONAMET / COE / CNE / SGN / INDRHI** | Hazard zone confirmation |
| **MOPC** | R-001/R-007 code compliance |
| **Ayuntamiento (municipio)** | Uso de Suelo + Permiso de Construcción + IPI municipal |
| **Superintendencia de Seguros** | Insurance carrier solvency / market |
| **CAASD / CORAASAN / CORAAPLATA / INAPA** | Water + sewer service confirmation |
| **EDESUR / EDENORTE / EDEESTE** | Power-account standing + connection |

## Quirks to know

- **Certificado de Título** is the only legal title evidence; physical document numbering matters; modern **Matrícula** is the post-saneamiento equivalent.
- **Constancia Anotada vs Certificado / Matrícula distinction**: a Constancia is a derivative document, NOT title; verify saneamiento completion.
- **Saneamiento** is a judicial Torrens-style process; **vacant rural land** without saneamiento can have multiple claimants — adversarial proceedings can run 2-7 years.
- **Acta de Mensura** must be done by a **DNMC-registered agrimensor**; older surveys may not match modern georeferencing.
- **Sociedad Anónima ownership** is common — buyer should confirm SA's `nómina de accionistas`, that the SA has no other liabilities, AML disclosure of beneficial owner (Ley 155-17).
- **Non-resident sworn declaration of source of funds** under Ley 155-17 + UAF (Unidad de Análisis Financiero) — wire transfers from offshore banks subject to enhanced review.
- **Notario público** authenticates only; the **abogado** (lawyer) does the legal due-diligence and represents the buyer.
- **Cooperativa inmobiliaria / fideicomiso** structures common in newer developments under Ley 189-11 (trust law).
- **`Cuota Litis`**: lawyer-engagement letter often specifies fees; common to bundle title-DD + closing for 1-1.5 %.
- **`Discharge` / `cancelación de hipoteca`** — verify any prior mortgage is fully cancelled at the Registro before closing.

## Source URL templates

| Source | URL pattern |
|---|---|
| Jurisdicción Inmobiliaria | `https://ji.gob.do/` |
| Registro de Títulos (per jurisdicción) | via JI portal |
| DNMC catastro | `https://indomet.gob.do/` |
| DGII (IPI + transfer + RNC) | `https://www.dgii.gov.do/` |
| MITUR + CONFOTUR | `https://mitur.gob.do/` |
| Migración | `https://migracion.gob.do/` |
| ONAMET (weather/hurricane) | `https://onamet.gob.do/` |
| COE (emergencies) | `https://coe.gob.do/` |
| CNE | `https://cne.gob.do/` |
| SGN (seismic/geological) | `https://sgn.gob.do/` |
| INDRHI (hydrology) | `https://indrhi.gob.do/` |
| MOPC (codes + roads) | `https://mopc.gob.do/` |
| INTRANT (transit) | `https://intrant.gob.do/` |
| BCRD (central bank, FX, mortgage stats) | `https://www.bancentral.gov.do/` |
| ONE (statistics, census) | `https://www.one.gob.do/` |
| SuperCasas (listings) | `https://www.supercasas.com/` |
| Inmobiliaria.com.do | `https://www.inmobiliaria.com.do/` |
| A2 Inmuebles | `https://www.a2inmuebles.com/` |
| Remax DR | `https://www.remax.com.do/` |
| CAASD water (SD) | `https://caasd.gob.do/` |
| INAPA water (national) | `https://inapa.gob.do/` |
| Superintendencia de Seguros | `https://superseguros.gob.do/` |
| Superintendencia de Electricidad | `https://sie.gob.do/` |
| Ministerio de Trabajo (salaries) | `https://mt.gob.do/` |

## Status

✅ **Fully populated** as of 2026-05-01.
**Coverage check**: pricing (BCRD + ONE + SuperCasas + Coldwell Banker DR 2025-2026), traffic (INTRANT + MOPC TPDA where available + OSM fallback), tax (IPI 1% above DOP 10.7M 2026 threshold per DGII Resolución DG-AR1-2026-00001 + 3% transfer + CONFOTUR 15-yr exemption + 27% non-resident WHT + 3% sucesiones), rental (Ley 4314 + MITUR vivienda vacacional + HOA reality), work (MT + DGII RNC + Migración 200k investor visa), risks (ONAMET + COE + SGN + INDRHI + R-001/R-007 + Fiona 2022 lessons), mains (CAASD + INAPA + EDE distributors + planta reality).
**Confidence**:
- **HIGH** for legal/tax structure (Ley 108-05 + Ley 18-88 + Ley 158-01/195-13 + Ley 155-17 + Ley 305-68 — all primary statutes verified).
- **HIGH** for CONFOTUR mechanics (15-yr IPI + transfer-tax exemption + MITUR resolution requirement) and for residency thresholds (USD 200k inversionista minimum, USD 1,500 pensionado, USD 2,000 rentista); **LOW** for an inversionista real-estate route and the citizenship timeline (not stated on DGM / MIP pages).
- **HIGH** for hazard sources (ONAMET, COE, SGN, INDRHI, MOPC R-001/R-007 all primary government).
- **MEDIUM** for current resort-community service pricing — HOA fees, planta install, hurricane insurance — vary widely by development; figures are aggregator + market-survey est.
- **MEDIUM** for 2025-2026 USD/m² benchmarks — secondary aggregator data; cross-check live SuperCasas + 3+ comparables before relying.
- **LOW** for some rural municipal-level data (Permiso de Uso de Suelo, parcel-level flood plain in non-Yuna/Yaque basins) — limited online presence; verification requires on-site municipal request.
**Last verified**: 2026-05-27. Risks: MIVHED CDCRD building-code row added 2026-09-24 in the October regwatch wave (Resolución 007-2026 from secondary press only); build-era rows citing R-001 / R-007 not re-verified. Visa tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

## Extension TODOs

- [ ] Per-provincia avalúo cycle calendar (DGII publishes irregularly)
- [ ] CONFOTUR resolution registry mirror — verify project list updates quarterly with MITUR
- [ ] MIVHED CDCRD (Resolución 007-2026, Apr 2026) — read the resolution text, confirm the transition end date, then update the build-era table and hazard rows that cite MOPC R-001 / R-007
- [ ] AML Ley 155-17 beneficial-owner disclosure — track UAF enforcement evolution
- [ ] Fideicomiso Ley 189-11 cost benchmarks for medium-value transactions
- [ ] Per-municipio Plan de Ordenamiento Territorial (POT) catalogue for flood + setback zones
- [ ] Investor-residency citizenship timeline — not stated on MIP naturalización page; locate the residency period in the naturalization law text
- [ ] Hurricane-insurance carrier registry post-Fiona — Superintendencia de Seguros market update
- [ ] Border-belt Ley 28-01 incentives — rare but worth a residential-buyer note
- [ ] Resort HOA reglamento templates (Cap Cana / Casa de Campo / Punta Cana Resort & Club / Las Terrenas major condos) — STR + reserve-fund disclosure norms
