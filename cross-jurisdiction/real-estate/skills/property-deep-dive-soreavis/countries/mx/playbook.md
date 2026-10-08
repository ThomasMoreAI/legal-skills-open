# Mexico 🇲🇽 — Property Due-Diligence Playbook

ISO2: `mx`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (Código Postal)**: 5 digits (`06000` CDMX Centro, `64000` Monterrey, `44100` Guadalajara, `77780` Tulum, `37700` San Miguel de Allende)
- **Admin levels**: 32 federal entities (31 states + Mexico City) + 2,469 municipios
- **Currency**: **MXN** (Mexican peso); 1 USD ≈ 17–20 MXN; 1 EUR ≈ 19–22 MXN
- **Languages**: Spanish (de facto); 68 indigenous languages recognized (Náhuatl, Yucateco, Zapoteco)
- **Cadastre — fragmented per state (no national portal)**:
  - **RPP (Registro Público de la Propiedad)**: state-level (32 separate registries)
  - **Catastro**: municipal-level, separate from RPP, holds cadastral value
  - **RAN (Registro Agrario Nacional)** for ejido land: `https://www.gob.mx/ran`
- **Identifier**: **folio real** (per state) + **cuenta catastral** (municipal)
- **Ownership types**:
  - **Propiedad privada** (private freehold)
  - **Ejido** (collective; ~50% of MX territory; cannot be sold to foreigners; "regularización" path to private title via ejido assembly + RAN release)
  - **Fideicomiso** (bank trust mandatory for foreigners in Restricted Zone)
- **CRITICAL: Foreign-buyer Restricted Zone**: 50 km coast / 100 km border — fideicomiso required

## Section: `--price`

### Primary sources

- **SHF (Sociedad Hipotecaria Federal) HPI**: `https://www.gob.mx/shf` — quarterly, mortgage-financed homes only
- **INEGI Vivienda**: `https://www.inegi.org.mx/temas/viviendasat/` — census + cadastral
- **Banxico** financial system reports
- **Lamudi MX quarterly market reports** (free PDFs)

### Listing platforms

- **Inmuebles24** — DOMINANT (OLX-owned): `https://www.inmuebles24.com`
- **Vivanuncios**: `https://www.vivanuncios.com.mx` (eBay heritage)
- **Lamudi MX**: `https://www.lamudi.com.mx`
- **Propiedades.com**: `https://www.propiedades.com`
- **Mexlist / Point2Homes** for English-speaking foreign buyers (Baja, Quintana Roo)
- **MLS systems** regional (AMPI national, CCIQR Quintana Roo) — patchy coverage

### 2025-2026 price benchmarks (SHF + Lamudi Q4 2025)

| Region | MXN/m² (typical) | USD-equivalent | YoY |
|---|---:|---:|---:|
| **CDMX (Polanco/Roma/Condesa)** | 60,000–110,000 | $3,300–$6,000 | +4.6% |
| **CDMX (suburbs)** | 30,000–50,000 | $1,650–$2,750 | +4.0% |
| **Monterrey** | 60,000–90,000 (premium) | $3,300–$5,000 | +9-12% (nearshoring) |
| **Guadalajara** | 35,000–55,000 | $1,925–$3,025 | +7-9% (tech) |
| **Puebla** | 25,000–40,000 | $1,375–$2,200 | +5% |
| **Tulum / Playa del Carmen** | 50,000–90,000 | $2,750–$5,000 | **+14-15%** |
| **Los Cabos** | 60,000–150,000+ | $3,300–$8,250+ | +14-15% |
| **San Miguel de Allende** | 40,000–80,000 | $2,200–$4,400 | +6% |
| **Mérida** | 25,000–40,000 | $1,375–$2,200 | +6% |

### Compute

1. MXN/m² = price / **superficie construida** (built area)
2. Cross-check **SHF HPI** + **Lamudi quarterly** + **Inmuebles24** asking prices
3. **Cadastral value typically 30-60% below market** (intentionally) — affects predial calc, NOT market value
4. **USD-denominated listings** common in Restricted Zone (Tulum, Cabo, Vallarta)

### Key terms

- Folio real = state RPP title identifier
- Cuenta catastral = municipal cadastre identifier
- Predial = annual property tax
- Fideicomiso = bank trust (foreign in Restricted Zone)
- Ejido = collective rural land
- Notario público = mandatory closing notary

---

## Section: `--traffic`

### Sources

- **SCT (Secretaría de Comunicaciones y Transportes)** + **SICT** (rebranded) — federal highways
- **CAPUFE** for toll roads
- City open-data: CDMX (`https://datos.cdmx.gob.mx/`), Monterrey, Guadalajara

### Key term

**TPDA (Tránsito Promedio Diario Anual)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (collector, suburban)
- 🟠 10,000–35,000 v/d (urban arterial, libramiento)
- 🔴 > 35,000 v/d (Periférico, Anillo Vial, autopistas)

---

## Section: `--tax`

### Annual property tax — Predial

**Municipal — varies massively per state/municipio.**

- Rate: **0.05–0.3%** of cadastral value (residential); commercial up to 1.2%
- **Cadastral value typically 30-60% below market**
- Typical CDMX residential bill: **MXN 3,000–20,000/yr** (USD 170–1,100)
- Early-payment discount up to **25% Jan–Feb**
- **CDMX progressive rates** for high-value properties

### Transaction taxes — ISAI / ISABI

**Per state — varies massively** (Impuesto Sobre Adquisición de Inmuebles):

| State | ISAI/ISABI rate |
|---|---:|
| CDMX | progressive 4–6.5% (up to 8.7% high-end) |
| Quintana Roo | 2% |
| Jalisco | 2–3% |
| Baja California Sur | 3% |
| Tijuana | 1.8–4% |

### Other taxes

- **ISR (Impuesto Sobre la Renta) capital gains**: up to **35%** marginal
- **Principal residence exemption (Mexican tax residents only)**: up to **700,000 UDIs** (~MXN 5–6M ≈ USD 280–350k at 2025 UDI fixing — UDI ≠ MXN, it is an inflation-indexed unit); requires RFC + utility/voter-ID proof of residence; land ≤ 3× construction area; usable once per 3 years. Double exemption with co-titled resident spouse. **Non-residents do NOT qualify** — must elect 25% withholding on gross OR 35% on net gain (the latter requires Mexican legal representative or notarized public deed) (2026-05-27 verified, source: Connell & Associates; PwC Tax Summaries — Mexico)
- **IVA**: 16% on commercial; residential generally exempt
- **Notario público**: **0.75–2.5%** (varies by state; 2026 — see Cost benchmarks table)
- **Registration**: 0.5–1% (2026 — see Cost benchmarks table)
- **Avalúo (appraisal)**: ~MXN 5,000–15,000 (2026 — see Cost benchmarks table)

### Foreign-buyer fideicomiso (CRITICAL)

**Restricted Zone**: 50 km coast / 100 km border. **Statute chain**: Constitución Art. 27 → **Ley de Inversión Extranjera 1993 Arts. 10–11** (SRE-permitted fideicomiso; 50-yr renewable) → Reglamento LIE (2026-05-27 verified, source: [Cámara de Diputados — Ley de Inversión Extranjera official PDF](https://www.diputados.gob.mx/LeyesBiblio/pdf/LIE.pdf)).

- **Fideicomiso required** for foreigners — bank trust 50-year renewable
- **Setup cost**: ~USD 2,000–3,000 (est. — per-bank fee comparison pending, see Extension TODOs)
- **Annual maintenance**: ~USD 350–1,000 (est. — per-bank fee comparison pending, see Extension TODOs)
- **SRE (Secretaría de Relaciones Exteriores)** permit required
- **Outside Restricted Zone**: foreigners can buy directly

### Total transaction cost (buyer side)

- Outside Restricted Zone: **5–8%** of price
- Inside Restricted Zone (with fideicomiso): **7–12%** of price
- **Notario público is biggest line item** (4–7%)

### Future risk

- Sheinbaum administration housing initiatives (affordable housing focus)
- Increased predial collection in CDMX, Monterrey
- Restricted Zone rules unchanged (no fideicomiso reform proposals advancing 2026)

---

## Section: `--rental`

### Long-term residential

- Per-state Civil Code governs lease
- Tenant protections **moderate** (less strict than EU)
- 1-2 year contracts standard
- **Aval** (guarantor) common requirement

### Short-let (Airbnb)

#### CDMX (Mexico City)

- **Mexico City Airbnb Law Oct 2024**: mandatory **Host Registry** (Padrón de Anfitriones) + **Technology Platform Registry** (Padrón de Plataformas) under amended Tourism Law (April 2024) — **registries went LIVE via Gaceta Oficial CDMX 22 May 2026** (accelerated ahead of the FIFA World Cup); registration opened 21 May 2026 with a 30-day window, but on 19 Aug 2026 Gobierno CDMX **extended the host-registration deadline to December 2026** (secondary — La Jornada 19 Aug 2026 + Gobierno CDMX social post; exact cutoff not confirmed from a primary page — verify at `https://estanciaeventual.cdmx.gob.mx`) (registry launch 2026-07-02 verified, sources: Jefatura de Gobierno CDMX 22 May 2026 + Ibarra, Del Paso y Gallego + Expansión Política)
- **50 % annual occupancy cap** (Art 61 Sexies — max 50 % of the year's nights) adopted by April 2024 amendment to CDMX Tourism Law; sanction if exceeded = non-renewal of registration + 1-year re-registration bar — **cap enforcement legally in flux pending amparo litigation**: Airbnb filed an amparo (Jan 2025) and individual hosts have too, with **suspensión definitiva granted in some cases** so the cap is not applied to those litigants pending trial; a Tribunal Colegiado has ordered a merits/constitutionality ruling (2026-07-02 verified, sources: El País 9 Jul 2025; Airbnb Newsroom Jan 2025; SMPS Legal)
- Sheinbaum (former mayor, now president) reversed her earlier UNESCO/Airbnb partnership

#### Quintana Roo (Tulum, Cancún, Playa del Carmen)

- **RETUR-Q law**: state-level Registro Estatal de Turismo mandatory
- **6% Lodging Tax (ISH)** on private departments / houses / villas let by an Anfitrión or platform (Ley del Impuesto al Hospedaje art. 8 para 2, in force 1 Apr 2023); 5% general rate for other lodging (art. 8 para 1) — (2025 data, source Congreso Q-Roo ISH consolidation POE 16-12-2025)
- Foreign hosts must hold **legal residency + RFC**
- Municipalities now empowered to ban platforms locally

#### Jalisco / Puerto Vallarta

- State-level less strict
- **HOA bans rising** in resort condos

### Tax on rental

- Marginal income tax (up to 35% MXN-resident)
- **Foreign owners**: **25% withholding** at gross
- IVA 16% on furnished short-let services

---

## Section: `--work=<profession>`

### Sources

- **OCC Mundial** — biggest job board: `https://www.occ.com.mx/`
- **LinkedIn MX**, **Computrabajo**, **Indeed.com.mx**, **Bumeran**
- **STPS (Secretaría del Trabajo)**: `https://www.gob.mx/stps`

### Self-employment

- **Persona física con actividad empresarial**: SAT registration
- **RFC (Registro Federal de Contribuyentes)** mandatory
- **Régimen Simplificado de Confianza (RESICO)** preferential rates for small business
- **IVA**: 16% standard

### Salary benchmarks (2025)

- Median monthly gross:
  - CDMX: ~MXN 18,000–35,000 (€900–€1,750)
  - Monterrey: ~MXN 20,000–40,000 (nearshoring premium)
  - Guadalajara: ~MXN 18,000–30,000
- **Salario mínimo (2026)**: **MXN 315.04/day general; MXN 440.87/day Northern Border Free Zone** (CONASAMI decree 3 Dec 2025; +13% general; +5% frontier; effective 2026-01-01) — Northern Border Free Zone covers BC, Sonora, Chihuahua, Coahuila, NL, Tamaulipas (2026-05-27 verified, source: Littler "Mexico Increases the Minimum Wage for 2026"; Ogletree; Mexperience)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SSN (Servicio Sismológico Nacional)** | `https://www.ssn.unam.mx/` | Real-time seismicity |
| **CENAPRED** | `https://www.gob.mx/cenapred` | National risk atlas, seismic zones A-D |
| **CONAGUA** | `https://www.gob.mx/conagua` | Flood, drought, hurricane |
| **Protección Civil federal** | `https://www.gob.mx/sspc/acciones-y-programas/coordinacion-nacional-de-proteccion-civil-357857` | Emergency response |
| **CFE Sismo** | building code zones |

### Specific risks

#### Earthquake — CRITICAL

- **Pacific subduction zone** = highest hazard (CFE seismic Zone D)
- **Pacific southwest (Oaxaca/Chiapas/Guerrero)** = highest hazard
- **CDMX 350km from subduction zone** but **lake-bed amplification**:
  - **1985 M8.0** (10,000+ dead)
  - **2017 M7.1** (centered Puebla, 369 dead)
- **Volcanic risk**:
  - **Popocatépetl** (50km from CDMX) — active
  - **Colima**, **Pico de Orizaba** also active

#### Hurricane

- **Quintana Roo** (Riviera Maya, Cancún, Tulum) — Atlantic hurricanes
- **Pacific** (Baja California, Sinaloa) — Pacific hurricanes
- **Tabasco, Yucatán** — flooding
- Hurricane **Ian, Otis 2023, Beryl 2024** as recent reference

#### Other

- **Landslide + flooding**: CDMX hillsides, Tabasco
- **Drought**: CDMX water crisis — Cutzamala system ~**97 % capacity early 2026** (highest in 5 years; recovered from 2024 historic low of ~26 %); structural drought risk remains but short-term supply secured ~2 years (2026-05-27 verified, source: Mexico News Daily; Mexico Business News "Cutzamala Reaches 95.5%")
- **Wildfire**: increasing northern + central
- **Cenotes / collapses**: Yucatán karst

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1985 (pre-Mexico City quake)** | Non-seismic standards — DANGEROUS in CDMX zones |
| **Post-1985** | Reformed seismic code |
| **Post-2017** | Stricter post-Puebla quake reforms |
| **Asbestos** | pre-2000 buildings likely; less regulated than EU |
| **Lead** | water pipes, paint pre-2000 |

### Mandatory at sale

| Document | Required because | Notes |
|---|---|---|
| **Cédula catastral** | Municipal cadastre | Catastro |
| **Constancia de no adeudo** | No-debts (predial + water) | Municipal |
| **Avalúo** | Appraisal for tax basis | Perito SHF certified |
| **Certificado de libertad de gravamen** | No-liens | RPP |
| **Boleta predial** | Property tax paid | Annual |
| **Notario público** | MANDATORY + EXPENSIVE | 4-7% of price total closing |
| **Fideicomiso permit (SRE)** | Restricted Zone foreign | Foreigners only |

---

## Section: `--mains`

### Sources

- **CONAGUA** federal regulator
- **SACMEX** (CDMX water + drainage)
- Per-state: AGUAH (Hidalgo), JAPAY (Yucatán), etc.

### Verification

- **CDMX water crisis ongoing**: cisterns + tinacos universal even with mains
- **Cutzamala system ~97% capacity early 2026** (recovered from 2024 historic low of ~26 %; ~95.5 % by Oct 2025; one of the wettest years since 1982) (2026-05-27 verified, source: Mexico News Daily; Mexico Business News)
- **Rural**: cisterns + septic standard; **12-15% of rural housing lacks mains drainage**

### Costs

| Scenario | Cost (MXN) |
|---|---:|
| Mains connection | 15,000–50,000 |
| Septic upgrade | 30,000–80,000 |
| Cisterna installation (10,000L) | 20,000–50,000 |
| Tinaco rooftop tank | 5,000–15,000 |

---

## Cost benchmarks (MX 2026)

| Work | Cost (MXN) |
|---|---:|
| Avalúo (perito SHF) | 5,000–15,000 |
| Notario público (varies by state) | 0.75–2.5% of price |
| Registration (RPP) | 0.5–1% |
| Fideicomiso setup (foreign Restricted Zone) | USD 2,000–3,000 |
| Fideicomiso annual fee | USD 350–1,000 |
| **Total transaction cost (outside Restricted Zone)** | **~5–8%** of price |
| **Total transaction cost (Restricted Zone foreign)** | **~7–12%** |
| Roof renovation | 80,000–200,000 |
| Asbestos abatement | 30,000–150,000 |
| Energy retrofit | 100,000–400,000 |
| Earthquake retrofit (older builds) | 200,000–800,000+ |
| Tinaco + cisterna combo | 25,000–65,000 |

## Active fiscal incentives (2025-2026)

- **Sheinbaum Vivienda para el Bienestar**: 1.1-1.2M homes target over 6-year term
- **INFONAVIT zero-interest 30-year mortgages** for workers earning ≤ 2× minimum wage
- **2025: 390,983 starts (101% of 386k target)**
- **INFONAVIT regulatory reform 2025**: institute can buy land + build social housing directly (first time in 30 years)
- **915k of 4.8M unpayable loans relieved**; 500k via "Paga lo Justo"

## Common listing platforms

- **Inmuebles24** — DOMINANT
- **Vivanuncios**, **Lamudi MX**, **Propiedades.com**
- **Mexlist / Point2Homes** — English-language for foreign buyers

## Caveats unique to MX

- **Fideicomiso for foreigners in Restricted Zone (50 km coast / 100 km border)** — mandatory bank trust; constitutional Article 27
- **Ejido land** (~50% of MX territory) — cannot be sold to foreigners; "regularización" complex multi-step process
- **Notario público EXPENSIVE** — 4-7% of total closing; single biggest line item
- **Cadastral value 30-60% below market** — intentionally; affects predial only
- **State-by-state divergence extreme** — RPP, ISAI, predial, registration all differ per state
- **CDMX water crisis** — Cutzamala system stress; "Day Zero" fears
- **Earthquake risk**: 1985 + 2017 reference events; lake-bed amplification CDMX-specific
- **Popocatépetl** active volcano 50km from CDMX
- **CDMX Airbnb Law Oct 2024** — host + platform registries (Padrón de Anfitriones + Plataformas) went LIVE via Gaceta Oficial CDMX 22 May 2026, original ~20-21 Jun 2026 folio deadline extended to December 2026 for hosts (announced 19 Aug 2026, secondary — verify at estanciaeventual.cdmx.gob.mx); 50 % annual occupancy cap (April 2024 amendment) contested — Airbnb + host amparos, suspensión definitiva in some cases so cap not applied pending trial (verified 2026-07-02)
- **Quintana Roo RETUR-Q** + 6% ISH lodging tax
- **Sheinbaum housing initiatives** — INFONAVIT zero-interest 30-year mortgages
- **USD-denominated listings** common in Restricted Zone (Tulum, Cabo, Vallarta)
- **Mérida + Yucatán** — tourism + retiree market; cenote risk
- **Hurricane belts** affect Quintana Roo (Atlantic) + Baja/Pacific separately

## Reddit / forum sources

- **r/mexico**, **r/MexicoCity**
- **r/expats**, **r/expatsmexico**
- **r/MoveToMexico**
- **El Universal Inmobiliario**, **El Financiero Real Estate**

## Verification authorities

| Authority | When to call |
|---|---|
| **RPP estatal** | Title verification |
| **Catastro municipal** | Cadastral value + cuenta |
| **RAN** | If ejido land |
| **SRE** | Fideicomiso permit (foreign Restricted Zone) |
| **Notario público** | Mandatory closing |
| **SAT** | Tax compliance |
| **Banco fiduciario** | If fideicomiso |
| **Catastro federal CENAPRED** | Risk maps |

## Source URL templates

| Source | URL pattern |
|---|---|
| SHF HPI | `https://www.gob.mx/shf` |
| INEGI Vivienda | `https://www.inegi.org.mx/temas/viviendasat/` |
| RPP CDMX | `https://rppyc.cdmx.gob.mx/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with the CDMX Consejería Jurídica RPPyC successor https://data.consejeria.cdmx.gob.mx/index.php/rppyc (search-confirmed live; fetch-verify from an unblocked network) |
| Catastro CDMX | `https://datos.cdmx.gob.mx/` |
| RAN (ejido) | `https://www.gob.mx/ran` |
| SSN seismic | `https://www.ssn.unam.mx/` |
| CENAPRED | `https://www.gob.mx/cenapred` |
| CONAGUA | `https://www.gob.mx/conagua` |
| SAT (tax) | `https://www.sat.gob.mx/` |
| SRE (foreign) | `https://www.gob.mx/sre` |
| Inmuebles24 | `https://www.inmuebles24.com` |
| Lamudi MX | `https://www.lamudi.com.mx` |

## Status

✅ **Fully populated** as of 2026-04-26. Rental tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (SHF + Lamudi Q4 2025), traffic (SCT + city portals), tax (predial + ISAI per state + ISR + IVA + fideicomiso), rental (CDMX Airbnb Law Oct 2024 + Quintana Roo RETUR-Q), work (OCC + RFC + INFONAVIT), risks (SSN + CENAPRED + CONAGUA + 1985+2017 quakes + Popocatépetl + hurricane), mains (CDMX water crisis context).
**Confidence**: HIGH for SHF Q4 2025 figures + Sheinbaum Vivienda program 2025 starts + fideicomiso Restricted Zone constitutional rule + CDMX Airbnb Law Oct 2024; MEDIUM for state-by-state ISAI table (only popular destinations confirmed); MEDIUM for CDMX 50 % Airbnb occupancy cap (adopted April 2024 amendment; registries live via Gaceta 22 May 2026 but cap enforcement in flux pending Airbnb + host amparo litigation as of 2026-07-02).

## Extension TODOs

- [ ] Per-state ISAI rates table (32 states)
- [ ] Per-municipio predial rates
- [ ] Fideicomiso bank fee comparison (Banamex, Banorte, BBVA, Santander)
- [ ] Ejido regularización flow (assembly → parcelization → RAN → RPP)
- [ ] Earthquake zone overlay (CFE Zones A-D)
- [ ] Restricted Zone perimeter map
- [ ] Notario público fee comparison per state
- [ ] CDMX Airbnb cap amparo-litigation tracker (Tribunal Colegiado merits/constitutionality ruling pending; registry live 22 May 2026)
- [ ] Cadastral vs market value reconciliation tool
- [ ] CDMX water crisis impact per delegación
