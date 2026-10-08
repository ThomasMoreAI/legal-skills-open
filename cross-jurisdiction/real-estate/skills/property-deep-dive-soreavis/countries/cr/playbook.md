# Costa Rica 🇨🇷 — Property Due-Diligence Playbook

ISO2: `cr`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`10101` San José, `40101` Alajuela, `50101` Cartago, `60101` Heredia)
- **Admin levels**: 7 provinces + 84 cantones + 488 distritos
- **Currency**: **CRC** (Costa Rican colón); 1 USD ≈ 510–540 CRC; 1 EUR ≈ 555–585 CRC (as of early 2026 — rates fluctuate, check BCCR *tipo de cambio*)
- **Languages**: Spanish (de facto); English widely used in tourist + expat zones
- **Cadastre — CENTRALIZED (strongest digital infra in LatAm)**:
  - **Registro Nacional**: `https://www.rnpdigital.com/`
  - **SIRI** (Sistema de Información del Registro Inmobiliario) — online property study
  - **Ventanilla Digital** — document e-filing
  - Certificación literal + plano catastrado online
- **Identifier**: **Folio Real** (provincia-finca-derecho format) + **plano catastrado** (CL-XXXXXX-YYYY)
- **Ownership types**: dominio pleno (freehold); usufructo; servidumbre; **concesión marítimo-terrestre** (Maritime Zone, **Ley 6043 / 1977**)

## Section: `--price`

### Primary sources

- **BCCR (Banco Central de Costa Rica)**: `https://www.bccr.fi.cr/` — quarterly real-estate price index
- **INEC**: `https://www.inec.cr/` — Encuesta Nacional de Hogares housing data
- **CCSS housing surveys**

### Listing platforms

- **Encuentra24** — DOMINANT: `https://www.encuentra24.com/costa-rica`
- **MLS Costa Rica**: `https://www.mlscostarica.com/`
- **CRPropertyExpert**, **Properties in Costa Rica**, **Coldwell Banker CR**
- High **English-language presence** (expat-driven market)

### Price benchmarks (as of early 2026, BCCR index + Coldwell Banker CR aggregate — figures may have changed since)

| Region | USD/m² (typical) | Notes |
|---|---:|---|
| **Escazú/Santa Ana houses** | $1,110–$1,180 | Premium Central Valley |
| **Escazú/Santa Ana condos** | $1,724–$2,343 | Premium condos >$2,500 |
| **San José central** | mixed (older stock) | $800–$1,500 |
| **Tamarindo / Nosara / Coco condos** | $1,400–$3,154 | Pacific coast premium |
| **Tamarindo / Nosara / Coco houses** | $550k–$1.7M | varies hugely |
| **Jacó / Manuel Antonio** | $1,500–$2,500 (houses) | Pacific |
| **Atenas / Grecia hills** | ~$170–$180/m² (raw land, per listing — verify with plano catastrado + comparable transactions) | Inland mountain |
| **Liberia / Guanacaste interior** | $700–$1,200 | Lower coast |
| **Limón Caribbean** | $400–$900 | Underdeveloped |

**2026 outlook**: est. +7-12% in premium areas (inference, not a sourced forecast — verify against BCCR index trend).

### Compute

1. USD/m² = price / **área de construcción** (built area)
2. Cross-check **SIRI literal certificate** + **MLS Costa Rica** asking
3. **Maritime Zone properties**: confirm titulado vs concesión (HUGE difference)

### Key terms

- Folio Real = title identifier (provincia-finca-derecho)
- Plano catastrado = registered cadastre plan
- Zona Marítimo-Terrestre = Maritime Zone (50m public + 150m concession)
- Pensionado / Rentista / Inversionista = residency programs
- Sociedad Anónima (SA) = corporación commonly used to hold property
- Pura vida = "pure life" (national motto + lifestyle)

---

## Section: `--traffic`

### Sources

- **MOPT (Ministerio de Obras Públicas y Transportes)**: `https://www.mopt.go.cr/`
- **CONAVI** (Consejo Nacional de Vialidad)
- **Lanamme UCR** for road counting + research

### Key term

**TPDA (Tránsito Promedio Diario Anual)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (collector, suburban)
- 🟠 10,000–35,000 v/d (urban arterial, Carretera Interamericana segments)
- 🔴 > 35,000 v/d (San José Circunvalación, Ruta 27 Próspero Fernández, Ruta 1)

---

## Section: `--tax`

### Annual property tax — Impuesto sobre Bienes Inmuebles (**Ley 7509, 1995**)

- **0.25% of registered value** (paid quarterly to municipalidad)
- **VERY LOW** (one of lowest in Americas)
- Exemptions for low-value primary residences
- Municipalities administer collection; property-owner declarations filed every 5 years
- Source: Procuraduría General SCIJ — Ley 7509 (Ley de Impuesto sobre Bienes Inmuebles) (2026-05-27 verified)

### Transaction taxes

- **Impuesto de Traspaso**: **1.5%** on transfer (typically buyer pays)
- **Notary stamps** (timbres): ~0.55%
- **Registry duty**: ~0.25%
- **Notary fees** (escritura): 1.0–2.0%
- **Total mandatory**: **~3.5-4%**

### Other taxes

- **IVA 13%** on **new builds** + commercial rent — introduced by **Ley 9635 (Fortalecimiento de las Finanzas Públicas, publicada 4 dic 2018; effective 1 Jul 2019)** (2026-05-27 verified, source Procuraduría General SCIJ + Deloitte CR + Grupo Camacho).
- **Impuesto Solidario** (luxury home tax) — **2026 threshold CRC 143M** per **Decreto Ejecutivo 45358-H (publicado 19 dic 2025)**; bracket-progressive schedule:
  - ≤ CRC 359M: 0.25%
  - CRC 359M – 720M: 0.30%
  - CRC 720M – 1,082M: 0.35%
  - CRC 1,082M – 1,442M: 0.40%
  - CRC 1,442M – 1,802M: 0.45%
  - CRC 1,802M – 2,162M: 0.50%
  - > CRC 2,162M: 0.55%
  - Filing deadline 15 January each year (2026-05-27 verified, source AG Legal + Tico Times + ICS.cr).

### Capital gains (Ley 9635, CGT 15% effective 1 Jul 2019)

- **CGT rate: 15%** on the net gain (introduced by Ley 9635, eff. 1 Jul 2019).
- **Primary-residence exemption (vivienda habitual)**: sale of the habitual residence is EXEMPT, provided this can be evidenced.
- **Pre-1 Jul 2019 properties** — seller may elect either 15% on net gain OR **2.25% on the full sale price** (one-time election, made at closing, irrevocable).
- **Habitual trader** (real-estate business activity) — gain taxed at **30% corporate income tax**, NOT 15% CGT.
- **Non-domiciled seller** — buyer must **withhold 2.5%** of the sale price for tax compliance before registration.

(2026-05-27 verified, source PwC Tax Summaries CR + Bluezone Legal + Latin Counsel. Prior playbook framing inverted the rule — sporadic individual sellers pay 15% CGT; only the vivienda habitual is exempt; traders pay 30%, not the other way around.)

### Total transaction cost (buyer side)

- Resale primary: **~3-4%** (1.5% traspaso + 0.5% timbres + 0.3% registro + 1-2% notary + 0.5% lawyer)
- New build: 13% IVA in price + ~3% other costs

### Future risk

- **Investor visa threshold reduced from USD 200k to USD 150k by Ley 9996 (2021)** (post-COVID inversion-promotion law); threshold stable through 2026 ($100k forestry) — corrected from prior "(2025)" date stamp; the threshold did NOT change in 2025 (2026-05-27 verified).
- **CGT framework stable** (Ley 9635 reform retained — primary residence exempt, 15% on other gains, 30% if habitual trader).

---

## Section: `--rental`

### Long-term residential

- **Ley General de Arrendamientos Urbanos y Suburbanos**
- **Tenant protection moderate**
- Standard 3-year contracts (renewable)

### Short-let

- **ICT (Instituto Costarricense de Turismo)** registration recommended: `https://www.ict.go.cr/`
- Some HOAs prohibit
- **Tax**: 13% IVA + income tax (15% non-resident withholding or progressive resident)

### Tax on rental

- **Residents**: progressive income tax (up to 25%)
- **Non-residents**: 15% withholding
- **IVA 13%** on platform listings

---

## Section: `--work=<profession>`

### Sources

- **MTSS (Ministerio de Trabajo y Seguridad Social)**: `https://www.mtss.go.cr/`
- **Encuentra24 Empleos**, **Computrabajo CR**, **LinkedIn CR**, **Elempleo.com**

### Self-employment

- **Régimen Tradicional / Simplificado** for tax
- **CCSS** social security mandatory
- **Profesión Liberal** for licensed professionals

### Salary benchmarks (2025)

- Median monthly gross:
  - San José: ~$700–$1,200 (USD)
  - Escazú / Heredia: ~$900–$1,500
  - Coastal tourist zones: ~$500–$1,000
- **Salario Mínimo**: varies by profession (~CRC 360,000-450,000/month, 2025 — published MTSS *salario mínimo* decree number, not an estimate; verify exact figure against the current semester decree)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **OVSICORI-UNA** (Volcanic Observatory) | `https://www.ovsicori.una.ac.cr/` | Volcanic monitoring |
| **RSN (Red Sismológica Nacional)** UCR/ICE | `https://rsn.ucr.ac.cr/` | Seismic |
| **CNE (Comisión Nacional de Emergencias)** | `https://www.cne.go.cr/` | Hazard management |
| **IMN (Instituto Meteorológico Nacional)** | `https://www.imn.ac.cr/` | Weather, climate |
| **MINAE (Ambiente y Energía)** | `https://www.minae.go.cr/` | Environment |

### Specific risks

#### Earthquake — CRITICAL

- **Cocos plate subducts NE beneath the Caribbean plate at the Middle America Trench (~7–9 cm/yr)**
- **2022 Seismic Hazard Model** — current reference standard
- **Recent significant events**:
  - **Cinchona 2009 M6.1**
  - **Nicoya 2012 M7.6** (Cocos-Caribbean subduction, Middle America Trench, Nicoya Peninsula)
  - **Limón 1991 M7.7** (Caribbean)

#### Volcanic

- **Arenal** — active 1968-2010, currently dormant but monitored
- **Poás** — active (2017 eruption)
- **Turrialba** — active (recurring eruptions 2010s+)
- **Rincón de la Vieja** — active
- **Irazú** — dormant but watched (**Cartago province, ~30 km E of San José; last major eruption 1963–65**)

#### Flooding + landslide

- **Rainy season May-November** — critical
- **Caribbean coast (Limón)**: chronic flooding
- **Tropical-storm bands** (e.g., Otto 2016, Nate 2017)

#### Climate

- Costa Rica is **tropical wet/dry** — climate change driving rainfall variability

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990** | Asbestos common; older systems |
| **1990s–2000s** | Improving codes |
| **Post-2010** | Modern seismic codes (after Cinchona 2009 + Nicoya 2012 reforms) |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Estudio de Registro** | Title study by lawyer/notary |
| **Plano catastrado** | Registered cadastre plan, must match Folio Real |
| **Certificación literal del Registro Nacional** | Title certificate |
| **No-debt certificates** | CCSS, ARESEP/ICE, AyA/ASADA, Municipalidad |
| **Notario** | Mandatory closing |

### Climate change projections

- **+1.5–3.0°C** by 2100
- **Pacific drying** + Caribbean wetting
- **Sea-level rise**: +20–50 cm by 2100 (coastal property risk)
- **Increased extreme rainfall events**

---

## Section: `--mains`

### Sources

- **AyA (Acueductos y Alcantarillados)**: `https://www.aya.go.cr/`
- **ASADAS** rural community water (~1,500 systems)
- **ESPH** Heredia-area private operator

### Verification

- Universal in cities; rural pozos + tanque séptico standard
- **ARESEP** regulatory authority

### Costs

| Scenario | Cost (USD, est.) |
|---|---:|
| Mains connection | ~$500–$2,000 |
| Pozo + bomba | ~$2,500–$8,000 |
| Tanque séptico | ~$2,000–$6,000 |

*Est. ranges (AyA connection + local contractor quotes) — verify on quote.*

---

## Cost benchmarks (CR 2026)

| Work | Cost (USD) |
|---|---:|
| Estudio de Registro (title study) | est. $300–$700 |
| Notary + escritura | 1.0–2.0% of price |
| Traspaso + timbres + registro | ~2.3% |
| **Total transaction cost (buyer)** | **~3–4%** of price |
| Roof renovation | est. $3,000–$10,000 |
| Anti-seismic retrofit | est. $15,000–$60,000 (depends on structure/size — verify with structural engineer quote) |
| Energy retrofit | est. $5,000–$25,000 |
| Solar PV (5kW) | est. $4,000–$8,000 |

*Works/professional-service rows above are est. ranges from contractor/notary quotes — verify per quote. Traspaso/timbres/notary % rows are anchored to the sourced `--tax` section.*

## Active fiscal incentives + visa programs (2025-2026)

### Residency programs

- **Pensionado**: USD 1,000/month income (lifetime pension) + dependents +$250/mo
- **Rentista**: USD 2,500/month for 24 months OR USD 60k bank deposit
- **Inversionista (Investor Visa)**: **threshold USD 150k** (reduced from USD 200k by **Ley 9996, 2021**; threshold stable through 2026); USD 100k for forestry; investment in **personal name** (not corporate) required for visa (2026-05-27 verified, source IMI Daily + CitizenX + Fragomen)
- **2-year temp residency → 3 yrs to permanent → 7 yrs to citizenship eligibility**
- **Al menos una entrada anual** (at least one entry into CR per year) to maintain temporary residency (per DGME statutory wording)

### Tax incentives

- **No CGT for individuals (non-habitual)**
- **No worldwide income tax** for territorial residents
- Various municipal exemptions

## Common listing platforms

- **Encuentra24** — DOMINANT
- **MLS Costa Rica**
- **CRPropertyExpert, Properties in Costa Rica, Coldwell Banker CR**
- High English-language coverage

## Caveats unique to CR

- **Strongest digital cadastre infra in LatAm** — Registro Nacional + SIRI + Ventanilla Digital online
- **Hold via corporación SA** common (estate planning + liability) — but **investor visa now requires personal-name title**
- **No CGT for individuals** — UNIQUE in region (non-habitual)
- **Maritime Zone Law 6043** (CRITICAL):
  - **First 50m public** — no construction (Zona Pública)
  - **Next 150m restricted** — concession-only (5–20-yr leases)
  - **51% must be Tico-owned**
  - **Foreigners max 49%**
  - **2.5% annual fee** on appraised value (in lieu of property tax)
  - **Many advertised "beachfront" titles are CONCESSION, not titled** — critical diligence point
- **10km international border zone** restrictions (less famous than Panama's)
- **ARESEP / ICE / AyA** state-utility monopoly
- **Pensionado USD 1,000/mo** = generous LatAm threshold
- **Investor visa $150k (Ley 9996, 2021; stable through 2026)** — most accessible in region
- **Earthquake risk CRITICAL** — Cocos subduction + Nicoya 2012 reference
- **4 active volcanoes** (Arenal, Poás, Turrialba, Rincón de la Vieja)
- **Tropical climate** — rainy May-Nov; landslide + flooding risk
- **Limón Caribbean** = different climate + higher flood
- **English-language market** — expat-driven, particularly Pacific coast
- **Pura vida** lifestyle marketing premium

## Reddit / forum sources

- **r/CostaRica** — biggest community
- **r/expats**, **r/expatsincosta**
- **r/MoveToCostaRica**
- **The Tico Times** (English)
- **A.M. Costa Rica**
- **Q Costa Rica**

## Verification authorities

| Authority | When to call |
|---|---|
| **Registro Nacional** | Title verification (online via SIRI) |
| **Catastro Nacional** | Cadastre verification |
| **Notario público** | Mandatory closing |
| **Municipalidad** | Property tax + permits |
| **CCSS / ARESEP / ICE / AyA** | No-debt certificates |
| **ICT** | If short-let |
| **DGME (Migración)** | Residency visa |
| **OVSICORI / RSN / CNE** | Hazard zone status |

## Source URL templates

| Source | URL pattern |
|---|---|
| Registro Nacional | `https://www.rnpdigital.com/` |
| BCCR | `https://www.bccr.fi.cr/` |
| INEC | `https://www.inec.cr/` |
| Encuentra24 CR | `https://www.encuentra24.com/costa-rica` |
| MLS Costa Rica | `https://www.mlscostarica.com/` |
| OVSICORI volcanic | `https://www.ovsicori.una.ac.cr/` |
| RSN seismic | `https://rsn.ucr.ac.cr/` |
| CNE emergencies | `https://www.cne.go.cr/` |
| IMN weather | `https://www.imn.ac.cr/` |
| AyA water | `https://www.aya.go.cr/` |
| ICT tourism | `https://www.ict.go.cr/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (BCCR + Encuentra24 + MLS Costa Rica 2026), traffic (MOPT TPDA), tax (Bienes Inmuebles 0.25% + Traspaso 1.5% + IVA 13% new + No CGT individuals + Solidario luxury), rental (ICT + 13% IVA), work (MTSS + CCSS), risks (Cocos subduction + Nicoya 2012 + 4 active volcanoes), mains (AyA + ASADAS).
**Confidence**: HIGH for Registro Nacional (gold-standard digital cadastre); HIGH for tax structure (PwC + Coldwell Banker confirm; **Ley 7509** property tax, **Ley 9635** IVA+CGT, **Ley 6043** Maritime Zone, **Ley 9996** investor visa); HIGH for visa thresholds (Investor $150k via Ley 9996/2021 confirmed); HIGH for Maritime Zone Law 6043 (well-documented); HIGH for Impuesto Solidario 2026 (CRC 143M Decreto 45358-H); MEDIUM for 2026 price benchmarks (regional aggregator data).
**Last verified**: 2026-05-27.

## Extension TODOs

- [ ] Per-canton property tax rates
- [ ] SA holding structure for property + tax implications
- [ ] Maritime Zone concession verification flow (titulado vs concesión)
- [ ] 10km border zone overlay
- [ ] Investor visa $150k personal-name compliance
- [ ] Pensionado/Rentista comparison decision tree
- [ ] Volcanic hazard overlay per canton (4 active volcanoes)
- [ ] Cocos subduction earthquake retrofit cost estimator
- [ ] AyA vs ASADAS rural water verification
- [ ] CCSS/ICE no-debt certificate flow
