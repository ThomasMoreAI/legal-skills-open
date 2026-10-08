# Spain 🇪🇸 — Property Due-Diligence Playbook

ISO2: `es`. Status: ✅ Fully populated (researched 2026-04; Tier-A quarterly refresh 2026-07-03).

## Country profile

- **Postcode (CP)**: 5 digits (`28013` Madrid centro, `08001` Barcelona, `46001` Valencia)
- **Admin levels**: 17 CCAA (Comunidades Autónomas) + 2 ciudades autónomas (Ceuta, Melilla) + 50 provincias + 8,131 municipios
- **Currency**: EUR (€)
- **Languages**: Castilian (official); co-official: Català (Cataluña, Balears, Valencia), Galego (Galicia), Euskera (País Vasco, Navarra)
- **Cadastre**: **Catastro Nacional** (Ministerio de Hacienda) — FREE public viewer
- **Identifier**: Referencia Catastral (14-char alphanumeric) + Registro de la Propiedad (separate)
- **CRITICAL**: 17 CCAA mean **massive variation** in tax (ITP, ISD, wealth, VTV) across regions
- Distinct ownership types: pleno dominio (freehold), usufructo (usufruct), nuda propiedad (bare ownership), división horizontal (commonhold)

## Section: `--price`

### Primary sources

- **Catastro Sede Electrónica** (FREE consultation): `https://www.sedecatastro.gob.es/`
  - Search by Referencia Catastral, calle + número, or coordinates
  - Returns: valor catastral (cadastral value), surface, year built, use
- **Registro de la Propiedad Online** (paid notas simples): `https://www.registradores.org/`

### Listing platforms

- **Idealista** (largest by far): `https://www.idealista.com/<provincia>/<municipio>/`
- **Fotocasa**: `https://www.fotocasa.es/`
- **Habitaclia**: `https://www.habitaclia.com/`
- **Pisos.com**: `https://www.pisos.com/`
- **Wallapop, Milanuncios** — privates
- **Tinsa, Sociedad de Tasación, ST Tasaciones**: appraisal indices

### Price benchmarks (2025-2026)

- **INE Índice de Precios de Vivienda (IPV)**: `https://www.ine.es/`
- **Fomento estadística vivienda libre + protegida**: `https://www.mitma.gob.es/`
- **Idealista Informe de Precios** quarterly
- **Tinsa IMIE**
- **INE IPV national YoY: +12.9 %** (Q1 2026, published 2026-06-08; segunda mano +13.5 %, nueva +9.1 %; rebased to base-2025). Regional spread +10.3 % (País Vasco) to +15.6 % (Aragón/Murcia). Source [INE IPV1T26](https://www.ine.es/dyngs/Prensa/IPV1T26.htm) — €/m² ranges below are 2024-2025 vintage and now run low; re-check Idealista zonal.

| Region/City | Resale €/m² (2024-2025 vintage — figure current to Q1 2026) |
|---|---:|
| **Madrid (Comunidad)** | 4,000–6,500 (centro 7,000–10,000) |
| **Barcelona (provincia)** | 3,500–5,500 (Eixample/Gràcia 5,500–8,500) |
| **País Vasco (San Sebastián)** | 5,000–7,500 |
| **Bilbao** | 3,500–4,500 |
| **Costa del Sol (Marbella)** | 4,500–8,000 (luxury 10k+) |
| **Costa Brava** | 3,000–5,500 |
| **Mallorca** | 4,500–7,500 |
| **Valencia** | 2,500–4,000 |
| **Sevilla** | 2,500–3,500 |
| **Zaragoza** | 1,800–2,500 |
| Rural Castilla / Extremadura / Aragón | 600–1,500 |

### Compute

1. Listing €/m² = price / superficie útil (usable) or construida (built — includes walls)
2. **Trap**: Cataluña + Valencia + Andalucía coast often inflate by including terraza, ático
3. **Trap**: pueblos rurales sometimes price by **superficie construida** + sometimes **m² escritura** (deed-quoted) — can differ
4. Compare to Idealista zonal (per barrio) for accurate market view
5. Valor catastral (~50 % of market) for tax base

---

## Section: `--traffic`

### Sources

- **Ministerio de Transportes y Movilidad Sostenible**: `https://www.mitma.es/`
- **DGT (Dirección General de Tráfico)**: `https://www.dgt.es/`
- **Provincial road services** (Diputaciones)
- CCAA-level (Cataluña, Madrid, Andalucía have own systems)

### Key term

**IMD (Intensidad Media Diaria)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (calle vecinal, carretera local)
- 🟡 1,000–8,000 v/d (carretera autonómica, calle urbana)
- 🟠 8,000–30,000 v/d (N-road, avenida, ronda urbana)
- 🔴 > 30,000 v/d (autovía/autopista, urban core)

---

## Section: `--tax`

> **⚠️ "100 % non-EU buyer gravamen" — NOT in force (verified 2026-05-27).** The widely-reported January 2025 government announcement of a 100 % gravamen on non-EU non-resident property buyers was formalised by the Grupo Parlamentario Socialista as **[Proposición de Ley 122/000196](https://www.congreso.es/es/proyectos-de-ley?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=122/000196)** (BOCG B-229-1, 30/05/2025). The bill has been **stalled in the "Pleno toma en consideración" queue since 5 September 2025** — never reached a floor vote, never assigned to a committee, no amendments process. It was **quietly dropped from the government's January 2026 housing package**, and per Reuters parliamentary documents on 27 March 2026 there is no realistic path to passage (Junts withdrew government support; Podemos opposes from the left for being insufficient). **No BOE-published Ley exists.** Do NOT factor a 100 % gravamen into TCO models or buyer briefs as if enacted. Tracked at `shared/regulatory-watch.md` § Spain 122/000196. Original proposal scope (NOT law): 100 % on catastral reference value, second-hand residential only (new builds excluded under IVA), non-EU non-residents, foral PV+Navarra exempt, ITP deductible — flagged by PwC + multiple legal analyses as TFEU Art. 63 (free movement of capital) risk if enacted. (2026-05-27 verified, sources [Congreso 122/000196](https://www.congreso.es/es/proyectos-de-ley?p_p_id=iniciativas&p_p_lifecycle=0&p_p_state=normal&p_p_mode=view&_iniciativas_mode=mostrarDetalle&_iniciativas_legislatura=XV&_iniciativas_id=122/000196) + [BOCG B-229-1 PDF](https://www.congreso.es/public_oficiales/L15/CONG/BOCG/B/BOCG-15-B-229-1.PDF) + [Reuters via US News 2026-03-27](https://www.usnews.com/news/world/articles/2026-03-27/spains-100-non-eu-property-tax-stalls-in-congress) + [PwC Periscopio Fiscal Jun 2025](https://periscopiofiscalylegal.pwc.es/nuevo-impuesto-sobre-la-transmision-de-muebles-a-no-residentes-en-la-ue/))

### Annual property tax — IBI (Impuesto sobre Bienes Inmuebles)

- Set by **ayuntamiento** (municipality)
- **Urbano**: **0.4–1.1 %** of valor catastral (statutory band; ~0.5–0.7 % est. central tendency — verify per-municipio at the ayuntamiento *ordenanza fiscal*)
- **Rústico**: 0.3–0.9 %
- **Características especiales**: 0.4–1.3 %
- Bills annually, often Q3-Q4
- Some bonificaciones available (large families, energy efficient, etc.)

### Other annual taxes

- **Tasa de basura**: ~€100–€300/yr per municipality
- **IIVTNU (plusvalía municipal)**: paid on sale (capital-gain-like, on land value)
- **Wealth tax (Impuesto sobre el Patrimonio)**: regional — varies massively:
  - **Madrid, Andalucía**: 100 % bonificación regional (effectively ZERO at CCAA level)
  - **Cataluña**: 0.21–2.75 % progressive on wealth >€500k
  - **Comunidad Valenciana**: 0.25–3.5 %
- **ITSGF (Impuesto Temporal de Solidaridad de las Grandes Fortunas)**: federal top-up, **1.7–3.5 % progressive on net wealth >€3M**, made indefinite by RD-Ley 8/2023 (27 Dec 2023; original Ley 38/2022). Deducts what was paid under regional Patrimonio → neutralises the Madrid/Andalucía 100 % bonificación for HNW. (2026-05-27 verified; source [BOE Ley 38/2022](https://www.boe.es/buscar/doc.php?id=BOE-A-2022-22684) + [AEAT ITSGF page](https://sede.agenciatributaria.gob.es/Sede/declaraciones-informativas-otros-impuestos-tasas/impuesto-temporal-solidaridad-grandes-fortunas.html))

### Transaction taxes — ITP (Impuesto sobre Transmisiones Patrimoniales)

**MAJOR REFORM 2025**: Catalonia steepened its already-progressive ITP scale (from 10 % ≤€1M + 11 % above, to four brackets topping at 13 % >€1.5M) for taxable events from 27 Jun 2025 (2025 data, source ATC Guia ITP + tarifes-tipus page)

| CCAA | ITP rate (resale) |
|---|---:|
| **Madrid** | **6.0 %** (lowest) |
| **Navarra** | 6.0 % |
| **País Vasco** | 4.0–7.0 % (varies by province) |
| **Andalucía** | 7.0 % |
| **Aragón** | 8.0 % |
| **Asturias, Cantabria** | 8.0 % |
| **Castilla y León** | 8.0–10.0 % |
| **Castilla-La Mancha** | 9.0 % |
| **Galicia** | 8.0 % |
| **Murcia** | 8.0 % |
| **Comunidad Valenciana** | **9.0 %** general (≤€1M) · **11 %** >€1M (pre-existing band, retained) — general rate cut 10 %→9 % by Ley 5/2025 (BOE-A-2025-11959), eff. 1 Jun 2026; AJD 1.5 %→1.4 % same date (2026-07-03 verified) |
| **Baleares** | 8.0–11.5 % progressive |
| **Cataluña** (Decret-llei 5/2025, eff. 27 Jun 2025) | **10 %** ≤€600k · **11 %** €600k–€900k · **12 %** €900k–€1.5M · **13 %** >€1.5M · **20 %** flat for grans tenidors (large holders) · 5 % reduced rate for buyers under 35 (2026-05-27 verified; source [ATC](https://atc.gencat.cat/es/agencia/noticies/detall-noticia/20250627-mesures-fiscals-2025-itpajd-isd)) |
| **Canarias** | 6.5 % |
| **Extremadura** | 8.0 % |
| **La Rioja** | 7.0 % |
| **Ceuta, Melilla** | 6.0 % |

### New build taxes

For obra nueva (new build, vendida by impresa):
- **IVA**: 10 % (residential) or 4 % (VPO subsidized)
- **AJD (Actos Jurídicos Documentados)**: 0.5–2.0 % per CCAA
- No ITP on new builds

### Notario + Registro

- Notario: ~0.1–0.5 % (regulated by arancel)
- Registro de la Propiedad: ~0.1–0.4 %
- Combined: ~0.5–1.5 %

### Plusvalía municipal (capital gains-like)

- Reformed after 2021 Constitutional Court ruling
- Two methods (taxpayer chooses lower):
  1. Real-gain method
  2. Cadastral-coefficient method
- Set per ayuntamiento; varies wildly

### Total transaction cost (buyer side)

- Resale: **8–14 %** typical (heavy)
- New build: **11–13 %**

### IRNR for non-residents

- **19 %** for EU/EEA residents on rental income
- **24 %** for non-EU/EEA on rental income
- 19 % on capital gains for any non-resident
- (IRNR rates — verify current year against AEAT before relying)

### Future risk

- Wealth tax political flux — depends on CCAA government changes
- Plusvalía in legal evolution post-2021
- Catalonia's 2025 steeper ITP scale (13 % top bracket >€1.5M) may inspire other CCAA

---

## Section: `--rental`

### Long-term residential

- Marco regulado: **LAU (Ley de Arrendamientos Urbanos)**
- Tenant protection moderate; eviction takes 6-18 months
- **Mais Habitação-style controls**: rent caps in declared "zonas tensionadas" (Cataluña, Valencia, Bilbao introducing)
- IRPF on rental income: 60 % deduction for long-term residential rent

### Short-let — VTV / VFT (Vivienda de Uso Turístico)

**Regional licensing (varies hugely)**:

| CCAA | Status |
|---|---|
| **Cataluña** | Strict; HUTV / HUT licenses; many municipios moratorium incl. Barcelona (BCN: all 10,101 HUT (2024 data, source Ajuntament de Barcelona Mesura de Govern 2024-2027) lose their habilitation in November 2028 under the Generalitat's Decret llei 3/2023 DT2 — no calendar day is sourced; on 21 Jun 2024 the Ajuntament announced it will grant no llicència urbanística (a municipal announcement, not a municipal decree); DT2.2 allows one owner-requested extension of up to five years) |
| **Baleares** | Mallorca + Ibiza near impossible to obtain new licenses |
| **Canarias** | Strict in Tenerife, Gran Canaria |
| **Madrid** | License + community approval; pressure from city hall |
| **Andalucía (Costa del Sol)** | License via VFT registration |
| **Comunidad Valenciana** | Easier than Cataluña; VTV registration |

**Tax**:
- **IRPF resident**: progressive on net rental income
- **IRNR non-resident**: 19 % (EU/EEA) or 24 % (non-EEA) on **gross** rental (verify current year against AEAT before relying)
- **IVA** if hotel-style services (cleaning, food): 10 % VAT applies, treated as commercial
- **Tasa turística — Cataluña (IEET: tarifa autonómica + recargo municipal)**: tariff schedule **REPLACED** by **Llei 2/2026 de 6 de març** (DOGC 9621, 10 Mar 2026), in force **1 Apr 2026** — all pre-2026 figures superseded. **Barcelona city totals per person per night, 1 Apr 2026–31 Mar 2027** (general tariff + €5.00 Ajuntament recàrrec): 5★/gran luxe €12.00 · 4★ €8.40 · habitatge d'ús turístic (HUT) €9.50 · albergs de joventut €6.00 · other establishments €7.00 · cruise call >12 h €9.00 / ≤12 h €11.00. **Rest of Cataluña, 1 Apr 2026–31 Mar 2027** (no municipal recàrrec yet): 5★ €4.50 · 4★ €1.80 · HUT €1.75 · albergs €0.80 · other €0.90 — scheduled step-up from 1 Apr 2027 to 5★ €6.00 · 4★ €2.40 · HUT €2.50 · albergs €1.00 · other €1.20. Barcelona recàrrec statutory ceiling **€8/night** (art. 34 bis); non-Barcelona municipios may add up to **€4/night** but only for stays from **1 Oct 2026** and only with a fiscal ordinance + an ATC conveni. Cap **7 stay-units per person**; persons aged **16 or under exempt** (2026 data, 2026-08-07 verified; source [ATC Quota tributària i tarifes](https://atc.gencat.cat/ca/tributs/ieet/quota-tributaria))
- **Tasa turística — Baleares**: €1-7/night (pre-2026 figure, not re-verified this cycle — confirm the current tourist-tax schedule with the Balearic CCAA tax authority before relying)

### Strategic notes

- **Mais Habitación / Ley de Vivienda 2023** declared zonas tensionadas allow rent caps
- **Cataluña + Baleares** = highest barriers; **Madrid** moderate; **Canarias** + **Andalucía** easier
- **Plusvalía + ITP at sale** eats long-term gains
- Wealth tax matters for high-value assets in Cataluña

---

## Section: `--work=<profession>`

### Job platforms

- **InfoJobs** (largest)
- **LinkedIn ES, Indeed.es, Tecnoempleo** (IT-focused)
- **SEPE (Servicio Público de Empleo Estatal)**: `https://www.sepe.es/`
- Profession-specific colegios profesionales (architects, doctors, lawyers)

### Self-employment

- **Autónomo regime**: monthly Seguridad Social minimum cuota **~€200–590** by income tramo (15 brackets, net ≤€670/mo → >€6,000/mo; 2023-reform table held unchanged into 2026, MEI 0.8%→0.9%) — voluntary higher bases allowed, so actual cuota can exceed €590 (2026 data, source Seg. Social RETA via Infoautónomos — confirm at the importass simulator)
- **Tarifa plana** (€80/mo first year reduced)
- **Sociedad Limitada (SL)**: min **€1 capital** since Ley 18/2022 "Crea y Crece" (in force Oct 2022; was €3,000 pre-reform). Creditor-protection conditions: 20 % of annual profits to legal reserve until reserve + capital reaches €3,000; shareholders jointly liable up to €3,000 in liquidation. (2026-05-27 verified; source [BOE Ley 18/2022](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-15818))
- **Trabajador por cuenta propia** straightforward

### Salary benchmarks (2025)

- Median monthly gross:
  - Madrid, Barcelona: ~€2,400-3,200
  - Bilbao, Sevilla, Valencia: ~€1,900-2,500
  - Smaller cities: ~€1,600-2,000
- **SMI (Salario Mínimo Interprofesional) 2026**: €1,221/mo (14 payments) = €17,094/yr (RD 126/2026, BOE-A-2026-3815, 18 Feb 2026; +3.1 % vs 2025; 2026-07-03 verified)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SNCZI / SNZI Sistema Nacional de Cartografía de Zonas Inundables** | `https://sig.mapama.es/snczi/` | Flood hazard maps Q10/Q100/Q500 |
| **MITECO Riesgos Naturales** | `https://www.miteco.gob.es/` | Aggregated environmental risks |
| **IGN (Instituto Geográfico Nacional) Sismicidad** | `https://www.ign.es/web/ign/portal/sis-area-sismicidad` | Earthquake hazard, real-time |
| **CSN (Consejo de Seguridad Nuclear) radón** | `https://www.csn.es/radon` | Radon maps |
| **AEMET** (national meteorology): `https://www.aemet.es/` | Climate + storm |
| **CCAA cartas de riesgos naturales** | per CCAA | Flood + landslide + fire |
| **CASIAS / Suelos Contaminados** | per CCAA | Brownfield contamination |
| **DGSCM (Protección Civil)** | `https://www.proteccioncivil.es/` | Emergency planning |

### Specific risks

- **Inundación / DANA (gota fría)**: Mediterranean coast, Costa del Sol, Valencia (2024 disaster), Barcelona; increasing flash floods
- **Incendios forestales**: huge concern Galicia, Asturias, Cataluña, Castilla-La Mancha, Andalucía interior
- **Sismo**: moderate-high Andalucía + Murcia (Lorca 2011 M 5.1 reminder); Cordillera Bética; Pirineos minor
- **Sequía**: Mediterranean Cataluña + Andalucía + Castilla — water restrictions
- **Aluminosis** (Spain-specific concrete failure): 1960s-1970s buildings esp. Cataluña/Tarragona — catastrophic
- **Costas**: 100m strip restriction (Ley de Costas 1988)
- **Volcán** (volcanic risk): Canarias only — La Palma 2021 Cumbre Vieja eruption

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1957** | Lead pipes, asbestos, weak structures |
| **1957–1981 ASCE pre-NCSE** | No seismic standards; AlumiNOSIS major risk in CAT/Tarragona |
| **1981–2003** | Improved standards; some asbestos |
| **2003–2007** | NCSE-02 + CTE (Código Técnico de Edificación 2006) |
| **Post-2007** | Modern energy + seismic; CTE 2019 nZEB |

**Aluminosis crisis**: Cataluña had massive failures in 1960s-70s buildings due to high-alumina cement (cemento aluminoso); structural collapse risk. **Specific to verify in Tarragona, Barcelona, Lleida properties pre-1980**.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Cédula de Habitabilidad** | All sales (varies by CCAA strictness) | 5–25 years per CCAA |
| **Certificado Energético (CEE)** | All sales | 10 years; penalty €300-€6,000 (statutory sanction band — verify current regime before relying) |
| **ITE (Inspección Técnica de Edificios)** | Buildings >50 yrs in many CCAA (45-50 in Cataluña, Madrid, Valencia) | 10 yrs |
| **Nota simple Registro de la Propiedad** | All sales | At sale |
| **Recibo IBI** + **certificado de ayuntamiento** | At sale | At sale |
| **Estatutos de comunidad de propietarios** | If condo | At sale |
| **Liquidación de gastos** (community fees) | If condo | At sale |

### Climate change projections (AEMET / CCAA)

- +1.5–4.5 °C by 2050 (RCP scenarios)
- Drought intensifying (south + east)
- Heat waves: longer, more lethal
- Extreme rainfall: DANA events more frequent
- Wildfires: Iberian peninsula at major risk
- Sea-level rise: Mediterranean + Cantábrico coasts

---

## Section: `--mains`

### Sources

- Each ayuntamiento or mancomunidad runs water + sewer
- Major: **Canal de Isabel II** (Madrid), **Aigües de Barcelona**, **Hidráulica de Cantabria**, **EMASESA** (Sevilla), **EMVISESA**, **EMASA Málaga**
- Universal in cities; rural Galicia, Aragón, Castilla often on pozo + fosa séptica

### Costs (est. ranges — get local quotes)

| Scenario | Cost (€) |
|---|---:|
| Acometida (mains connection) | 1,500–4,000 |
| Septic to mains | 5,000–15,000 |
| Fosa séptica (modern) | 4,000–10,000 |
| Pozo de agua (well drill) | 3,000–8,000 |

---

## Cost benchmarks (ES 2026)

| Work | Cost (€) |
|---|---:|
| Cédula de habitabilidad | 100–300 |
| Certificado Energético | 100–250 |
| ITE | 300–800 |
| Notario | 600–1,500 |
| Registro de la Propiedad | 200–800 |
| **Total transaction cost (resale)** | **8–14 %** of price |
| **Total transaction cost (new build)** | **11–13 %** |
| Aluminosis remediation (small house) | 30,000–100,000 |
| Septic to mains | 5,000–15,000 |
| Roof tile (200 m² teja árabe) | 8,000–18,000 |
| Energy retrofit (Class C → A) | 25,000–60,000 |
| Antiseismic retrofit | 20,000–60,000 |

## Active fiscal incentives (2026)

- **Plan Reno** energy retrofit: up to 60 % grants (Next Generation EU funds)
- **Deducciones IRPF for retrofit**: 20-60 % rebate over 5 yrs depending on energy class jump
- **MOVES Plan III**: heat pump + renewable heating
- **Ley de Vivienda 2023**: incentives in zonas tensionadas (long-let)
- **Plan Estatal de Vivienda 2026-2030** (RD 326/2026, de 22 de abril, BOE-A-2026-8872): active state housing-aid framework (grants/rebates), first state plan under Ley 12/2023; 40 % of allocation to CCAA for public/affordable rental supply (2026-07-03 verified)

## Common listing platforms

- **Idealista** — biggest, full extraction
- **Fotocasa, Habitaclia, Pisos.com** — standard
- **Engel & Völkers, Sotheby's, Lucas Fox** — premium
- **Wallapop, Milanuncios** — privates

## Caveats unique to ES

- **Aluminosis** (Cataluña 1960s-70s): catastrophic concrete failure risk — verify with structural engineer
- **Costas Law 100m strip**: coastal restrictions on building/extending
- **Plusvalía municipal** still in legal evolution post-2021 ruling
- **Wealth tax** depends massively on CCAA — Madrid/Andalucía effectively zero, Cataluña/Valencia high
- **Cataluña ITP scale steepened 27 Jun 2025** (was already 10 %/11 % two-bracket) — affects high-value Barcelona purchases; top bracket 13 % >€1.5M + 20 % flat for grans tenidors (Decret-llei 5/2025)
- **Golden Visa abolished** by Ley Orgánica 1/2025 (3 Apr 2025) — the Ley 14/2013 art. 63 real-estate residency route is closed to new applicants (2026-05-27 verified; cross-ref `shared/visa-programs.md` ENDED registry)
- **VPO (vivienda protegida)** — subsidized housing, restrictions on resale
- **Cooperative housing (cooperativas)** — common form, specific rules
- **NIE/NIF** required for non-residents to buy
- **Pueblos rurales depopulating** — resale liquidity weak
- **Cédula de Habitabilidad** without it some purchases blocked (Cataluña strict)
- **Gota fría / DANA** (cold drop) flood events Mediterranean coast
- **Catastro vs Registro** mismatch common — verify both before buying
- **Cooperativa de viviendas** + **comunidad de propietarios** require diligence on financial state

## Reddit / forum sources

- **r/Spain**, **r/AskSpain**, **r/Madrid**, **r/Barcelona**, **r/Valencia**
- **r/SpainAuxiliares** (expat teaching)
- **InvertirEnLaBolsa** + **Rankia** (financial)
- **Idealista news** + comments
- **Real Estate Spain Telegram groups**
- Expat: **The Local Spain**, **Sur in English**, **Olive Press**

## Verification authorities

| Authority | When to call |
|---|---|
| **Catastro Sede Electrónica** | Cadastral verification — FREE |
| **Registro de la Propiedad** | Title verification (paid) |
| **Ayuntamiento Urbanismo** | Permits, planning, plusvalía |
| **Notario** | Final transfer, escrow |
| **Suministros** (gas/agua/luz) | Contracts after purchase |
| **Comunidad de propietarios** | If condo: gastos, deudas, derramas |
| **AEAT (Agencia Tributaria)** | IRPF/IRNR rules |

## Source URL templates

| Source | URL pattern |
|---|---|
| Catastro Sede Electrónica | `https://www.sedecatastro.gob.es/` |
| Idealista | `https://www.idealista.com/<provincia>/<municipio>/` |
| INE Vivienda | `https://www.ine.es/dynt3/inebase/es/index.htm?padre=2942` |
| SNCZI flood | `https://sig.mapama.es/snczi/` |
| IGN seismic | `https://www.ign.es/web/ign/portal/sis-area-sismicidad` |
| CSN radón | `https://www.csn.es/radon` |
| AEMET clima | `https://www.aemet.es/` |
| Registradores | `https://www.registradores.org/` |
| AEAT | `https://www.agenciatributaria.es/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-08-07 (Cataluña IEET tourist-tax tariff schedule re-verified against ATC — Llei 2/2026 rates in force 1 Apr 2026; prior Tier-A quarterly refresh 2026-07-03 — fast-moving claims re-verified; structural sections unchanged). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (Catastro free + comprehensive; SNCZI maintained). MEDIUM for short-let regulation (CCAA-specific, evolving — Cataluña tightening, Madrid moderate). HIGH for Cataluña 2025 ITP reform (27 Jun 2025 effective, Decret llei 5/2025).

## Extension TODOs

- [ ] Per-CCAA wealth tax + ITP rate tables (deeper)
- [ ] Per-municipio plusvalía methodology
- [ ] VTV/VFT per CCAA licensing decision tree
- [ ] Aluminosis detection workflow (Cataluña/Tarragona pre-1980)
- [ ] Costas 100m strip parcel-level lookup
- [ ] Zonas tensionadas tracking (Mais Habitação areas)
- [ ] La Palma volcanic zone (Canarias) overlay
- [ ] Cooperativa housing red-flag detection
