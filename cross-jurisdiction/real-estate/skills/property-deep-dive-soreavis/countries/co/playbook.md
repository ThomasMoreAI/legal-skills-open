# Colombia 🇨🇴 — Property Due-Diligence Playbook

ISO2: `co`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode (Código Postal)**: 6 digits managed by **4-72** (Servicios Postales Nacionales). First 2 digits = departamento; next 2 = ZIP zone; last 2 = local sector. Example: `110111` (Bogotá D.C., centre).
- **Admin levels**: 32 **departamentos** + 1 **Distrito Capital** (Bogotá D.C.) → 1,103 **municipios** (incl. distritos especiales: Cartagena, Santa Marta, Barranquilla, Buenaventura, Tumaco, Riohacha) → veredas / corregimientos (rural) and barrios / comunas / localidades (urban).
- **Currency**: COP (peso colombiano). Highly volatile vs USD; BanRep policy rate 9.25 % at Apr 2026 monetary meeting (per BanRep release; verify at next Junta meeting). 2024-25 cuts as inflation eased toward the 3 % target.
- **Languages**: Spanish (official, Constitución 1991 art. 10); 65 indigenous languages co-official in their territories; English common in El Poblado (Medellín), Chicó/Usaquén (Bogotá), and Cartagena tourism zones — elsewhere expect Spanish-only with notaries, ORIP, and municipal offices.
- **Cadastre**:
  - **IGAC** (Instituto Geográfico Agustín Codazzi) — national cadastre + map authority: `https://www.igac.gov.co/`
  - **Catastro multipropósito** rests on **Ley 1955/2019 (PND 2018-22) arts. 79-82** plus **Decreto 1983 of 2019** + **Decreto 148 of 2020**, compiled into **Decreto 1170 of 2015** (IGAC + DNP normatividad portal). ⚠️ **Decreto 1339 of 2020 is NOT part of this chain** — it is MinAmbiente's Páramo Las Hermosas legal-representative designation of 8 Oct 2020 and has nothing to do with cadastre; the citation is common in secondary write-ups and is wrong (`https://www.minambiente.gov.co/documento-normativa/decreto-1339-de-2020`) (2026-08-07 verified). Goal: parcel-level fiscal + legal + ecological data, replacing the 2010s-era avalúo gap (historically commercial value 2-3× catastral). Coverage as of 2025 still uneven — verify in IGAC's cobertura tracker.
  - **Bogotá D.C.**: own cadastre via **UAECD** (Unidad Administrativa Especial de Catastro Distrital).
  - **Medellín**: **Subsecretaría de Catastro** within Secretaría de Gestión y Control Territorial.
  - **Cali**: Subdirección de Catastro Municipal.
- **Identifier**: every parcel has both:
  - **Cédula catastral** (fiscal — IGAC/UAECD/local catastro)
  - **Folio de Matrícula Inmobiliaria (FMI)** (legal — Oficina de Registro de Instrumentos Públicos / ORIP, supervised by **SNR**)
- **Foreign ownership**: foreigners hold **freehold equivalent to nationals** (Código Civil; Ley 9 de 1989; **no nationality restrictions on residential**). Restricted only in: zonas de frontera (Decreto-Ley 2535/1993 + Ley 191/1995 — 2 km strip generally); reserves indígenas/comunidades negras (collective titles, Ley 70/1993, Ley 21/1991).
- **Recent reforms (selected)**:
  - **Ley 2010/2019** "Ley de Crecimiento" — tax reform.
  - **Ley 2155/2021** "Ley de Inversión Social" — social investment + tax adjustments.
  - **Ley 2277/2022** ("Reforma Tributaria" of the Petro government) — wealth tax reintroduced; ganancia ocasional rate raised from 10 % to 15 %; predial-base adjustments per municipality.
  - **Decreto 538 of 2024 (Bogotá)** — 10 % impuesto al consumo (lodging tax) on STR + obligations *(claim per second-tier sources — "Decreto 538/2024" reference NOT verifiable in alcaldiabogota.gov.co/sisjur as of 2026-07; a fresh sisjur re-check finds only Decreto 538/2021 (bienestar animal) and Decreto 538/2025 (Sec. Movilidad), no 2024 STR/lodging decree; national impuesto al consumo on lodging is 8 % under Estatuto Tributario art. 512-9 — verify before relying)*.
  - **Catastro multipropósito** ongoing rollout (2020 → 2025+).
  - **M-visa investment thresholds** (**Resolución 5477/2022 art. 79**, within Decreto 1067/2015): **real-estate route ≥ 350× SMLMV**; **FDI route > 650× SMLMV**. Both routes accumulate 5 years toward **Visa R** (art. 90 as replaced by **Resolución 10434/2023 art. 76**) — the R grant is **not automatic** (Parágrafo 3). At the **2026 SMLMV of COP 1,750,905/mes** (+23 %, Decreto 1469/2025; the Consejo de Estado suspended it on 12 Feb 2026 and **Decreto 0159 of 19-Feb-2026** re-fixed the same figure transitorily — secondary reports state an auto of 9 Jul 2026 revoked the suspension, restoring Decreto 1469/2025 and leaving 0159 without effect, with the nullity action on the merits still pending (primary auto not read — verify at consejodeestado.gov.co, Rad. 11001-03-25-000-2026-00004-00)): 350× = **COP 612.8 M ≈ USD 195 k**; 650× = **COP 1,138.1 M ≈ USD 362 k** at TRM 3,144.14 (BanRep, 2026-08-03). Re-prices **every 1 Jan** with the SMLMV and **daily** in USD terms with the TRM — the widely-quoted ~USD 125 k figure was the 2025 wage at a ~4,100 TRM *(superseded)*. Verify current Resolución at Cancillería (2026-08-07 verification).

---

## Section: `--price`

### Primary sources

| Source | Type | URL | What it gives |
|---|---|---|---|
| **DANE IPVN** (Índice de Precios de Vivienda Nueva) | National statistics | `https://www.dane.gov.co/index.php/estadisticas-por-tema/construccion/indice-de-precios-de-vivienda-nueva-ipvn` | Quarterly price index, new dwellings, 23 metro areas |
| **DANE IEAC / IEAH** | National statistics | `https://www.dane.gov.co/index.php/estadisticas-por-tema/construccion` | Construction costs + housing stock |
| **BanRep IPVN/IPVU** | Central bank | `https://www.banrep.gov.co/es/estadisticas/indice-precios-vivienda-nueva-usada` | Used-home price index (BanRep computes IPVU from mortgage records) |
| **IGAC Geoportal / SIGOT** | Cadastre | `https://geoportal.igac.gov.co/` | Parcel viewer (where multipurpose cadastre rolled out) |
| **UAECD Mapas Bogotá** | City cadastre | `https://www.catastrobogota.gov.co/` and `https://mapas.bogota.gov.co/` | Bogotá parcel + avalúo catastral |
| **Catastro Medellín** | City cadastre | `https://www.medellin.gov.co/es/secretaria-gestion-y-control-territorial` | Medellín parcel + avalúo |
| **Lonja de Propiedad Raíz Bogotá** | Trade body | `https://www.lonjadebogota.org.co/` | Quarterly market reports |
| **Lonja de Propiedad Raíz Medellín** | Trade body | `https://lonjadecolombia.com.co/` | Quarterly market reports + Antioquia |
| **Galería Inmobiliaria** | Private aggregator | `https://galeriainmobiliaria.com.co/` | Sales data, paid pro tier |

### Listing platforms

| Platform | URL pattern | Notes |
|---|---|---|
| **Metrocuadrado** (El Tiempo group) | `https://www.metrocuadrado.com/<tipo>/<ciudad>/` | Largest national portal; aggregator of agencies |
| **Finca Raíz** | `https://www.fincaraiz.com.co/` | Wide coverage; mix agency + private |
| **Properati Colombia** (Lifull) | `https://www.properati.com.co/` | Aggregator + price index |
| **CienCuadras** (BVC group) | `https://www.ciencuadras.com/` | Banked transactions, more curated |
| **OLX Colombia** | `https://www.olx.com.co/inmuebles_c1503` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row | Private sellers, varies in quality |
| **Habi** | `https://www.habi.co/` | iBuyer, Bogotá/Medellín/Cali used apartments |

### Avalúo catastral vs avalúo comercial — the core gap

- **Avalúo catastral** = municipal fiscal value (basis of impuesto predial).
- **Avalúo comercial** = market value (basis of mortgage, sale).
- Historical gap: catastral typically 30–60 % of comercial pre-multipurpose-cadastre rollout (DANE/IGAC reports 2018-2020). Some municipios still at 30 %, others (Bogotá UAECD post-2024 actualización) approaching 80–90 %.
- **Trap**: low avalúo catastral makes predial bill cheap today, and an actualización catastral raises the base — but the widely repeated **2–3× bill jump is OVERSTATED**. Statutory annual ceilings cap the bill at **IPC + 8pp** where the predio is actualizado / **max 50 %** where it is not (**Ley 1995/2019 art. 2**), **max 2×** (**Ley 44/1990 art. 6**), and **100 % of IPC** for estratos 1-2 up to 135 SMMLV; IGAC also states the avalúo jump is **not automatic and not proportional to the tax**. The caps do **NOT** cover lotes urbanizables no urbanizados, predios bajo autoavalúo, or a changed destino económico / área / construcción — larger jumps are lawful there (2026-08-07 verified). Always check UAECD/IGAC actualisation date for the cédula catastral.

### Price benchmarks (Q4 2025 / Q1 2026 reference)

> All figures sourced **directly from DANE IPVN release notes** + **Galería Inmobiliaria** + **Lonja de Bogotá quarterly bulletins**. Per-barrio numbers vary widely; numbers below are **city-average asking-price/m² for new + used apartments in mid-tier estratos 4-5** unless noted.

| City / zone | COP/m² (~2026) | USD/m² @ 4,000 COP/USD | Source |
|---|---:|---:|---|
| Bogotá D.C. average | ~6.5–8.5 M | ~$1,625–$2,125 | DANE IPVN Q4 2025; Lonja Bogotá |
| Bogotá Chicó / Chapinero Alto / Usaquén (estrato 5-6) | ~10–18 M | ~$2,500–$4,500 | Lonja Bogotá; Metrocuadrado scrapes |
| Bogotá sur (Bosa, Kennedy, estratos 1-3) | ~3–5 M | ~$750–$1,250 | DANE IPVN |
| Medellín average | ~6–8 M | ~$1,500–$2,000 | Lonja Medellín; DANE IPVN |
| Medellín El Poblado (estrato 6) | ~10–17 M | ~$2,500–$4,250 | Lonja Medellín; Galería Inmobiliaria |
| Medellín Laureles / Envigado | ~7–11 M | ~$1,750–$2,750 | Lonja Medellín |
| Cartagena Bocagrande / Centro Histórico | ~12–25+ M | ~$3,000–$6,250+ | Galería Inmobiliaria; listing scrapes |
| Cali (Sur, Pance, estrato 5-6) | ~5–9 M | ~$1,250–$2,250 | DANE IPVN |
| Barranquilla (Norte) | ~5–8 M | ~$1,250–$2,000 | DANE IPVN |
| Santa Marta (Rodadero) | ~7–14 M | ~$1,750–$3,500 | Galería Inmobiliaria |

⚠️ **USD conversion volatile**: 2022-2026 the COP/USD has swung between ~3,800 and ~4,900. Always re-quote at the day's BanRep TRM (`https://www.banrep.gov.co/es/estadisticas/trm`).

### Compute

1. Listing COP/m² = listing COP / m² (clarify: área construida vs área privada vs área útil — listing language varies).
2. Compare to DANE IPVN for the city (national).
3. Compare to Lonja regional bulletin (city/zone specific).
4. Cross-check with Metrocuadrado / Finca Raíz comparable sales for the **same barrio + estrato**.
5. **Trap**: many listings quote "área construida" including walls + common-area share; "área privada" is the legal title surface (used for predial + administración charges). Always ask for the **escritura pública** to confirm.
6. **Trap**: new builds (preventa / sobre planos) advertised in UVR (Unidad de Valor Real) or USD — convert to COP at signing for comparability.

---

## Section: `--traffic`

### Primary sources

| Source | URL | What it gives |
|---|---|---|
| **INVÍAS** (Instituto Nacional de Vías) | `https://www.invias.gov.co/` | National road inventory + Tránsito Promedio Diario (TPD) for non-concessioned national roads; "Volúmenes de Tránsito" annual reports |
| **ANI** (Agencia Nacional de Infraestructura) | `https://www.ani.gov.co/` | Concessioned highways (4G program) — TPD per concesión |
| **Secretaría Distrital de Movilidad — Bogotá** | `https://www.movilidadbogota.gov.co/` | City vehicle counts, pico y placa, TransMilenio data |
| **Secretaría de Movilidad — Medellín** | `https://www.medellin.gov.co/es/secretaria-de-movilidad/` | Aforos vehiculares + Encuesta Origen-Destino |
| **Secretaría de Movilidad — Cali** | `https://www.cali.gov.co/movilidad/` | Aforos vehiculares Cali |
| **OSM fallback** | `https://overpass-turbo.eu/` | Road class only — coarse band |

### Key term

**TPD (Tránsito Promedio Diario)** — average daily traffic; the Colombian equivalent of AADT/TMJA. Reported by INVÍAS for the troncal network and by ANI for concesiones.

### Verdict bands (TPD)

- 🟢 < 1,000 v/d (rural terciaria, vereda)
- 🟡 1,000–5,000 v/d (secundaria, urban side street)
- 🟠 5,000–20,000 v/d (busy primaria/secundaria, urban arterial)
- 🔴 > 20,000 v/d (autopista, ring road, urban core arterial — Calle 80, Av. Boyacá, Av. Las Américas Bogotá; Av. Las Vegas Medellín)

### Coarse fallback (OSM `highway` class)

- `motorway/trunk` ≈ INVÍAS Primaria + 4G concesiones
- `primary` ≈ INVÍAS Primaria
- `secondary` ≈ INVÍAS Secundaria (departmental)
- `tertiary` ≈ Terciaria (municipal/veredal)
- `residential` ≈ urban barrio

### Caveats

- **Pico y placa** (license-plate restriction) operates in Bogotá, Medellín, Cali on rotating schemes — affects daily traffic *patterns*, not totals.
- INVÍAS TPD reports lag 1–2 years (latest published typically t-2). Date-stamp every figure.
- Concesiones report TPD to ANI under contract — those are reliable but only for the concession length.

---

## Section: `--tax`

### Annual property tax — Impuesto Predial Unificado (IPU)

**Base**: avalúo catastral (per the city/IGAC catastro). Authority: each municipio sets its own rates within national bounds (Ley 44/1990 + Ley 1450/2011 + Ley 1955/2019). Rates expressed in **por mil (‰)**.

#### National bounds (Ley 1450/2011 art. 23, Ley 44/1990)

- **Mínimo**: 5 ‰ (0.5 %)
- **Máximo general**: 16 ‰ (1.6 %)
- **Predios urbanos no edificados**: hasta 33 ‰ (3.3 %)
- Special discounted rates for predios de uso social, vivienda de interés social (VIS).

#### Bogotá D.C. (per Acuerdo 648/2016 + UAECD updates 2025)

> Actual rates per Acuerdo Distrital and yearly UAECD adjustments — verify at `https://www.haciendabogota.gov.co/` for the assessment year. Bogotá uses a **self-declaration** system with **bands by avalúo**.

Indicative residential rates (verify current Acuerdo):
- Estrato 1-2 (avalúo bajo): **2-5 ‰**
- Estrato 3-4: **5-8.5 ‰**
- Estrato 5-6: **8.5-9.5 ‰**
- Vivienda no residencial / lotes: higher tiers

**Beneficio por pronto pago**: typically 10 % discount if paid by April deadline (verify each year's calendario tributario at SHD Bogotá).

#### Medellín (per Acuerdos Municipales)

- Residencial estrato 1-2: ~3-4 ‰
- Estrato 3-4: ~5.5-7.5 ‰
- Estrato 5-6: ~8.5-10 ‰
- Verify at `https://www.medellin.gov.co/es/secretaria-de-hacienda/` for current Estatuto Tributario Municipal.

> All city-specific rates dated and per-municipio Acuerdo — **verify at the city Secretaría de Hacienda before quoting**. Multipurpose cadastre rollouts do raise avalúos on the 2024-2026 cycle, but the **2-3× predial-bill figure repeated in secondary sources is OVERSTATED**: per IGAC an avalúo rise is neither automatic nor proportional to the tax, and the annual bill is capped at **IPC + 8pp** (predio actualizado) or **max 50 %** (not actualizado) under **Ley 1995/2019 art. 2**, **max 2×** under **Ley 44/1990 art. 6**, and **100 % of IPC** for estratos 1-2 up to 135 SMMLV. Caps do **not** cover lotes urbanizables no urbanizados, autoavalúo predios, or changes of destino económico / área / construcción (2026-08-07 verified).

### Transaction taxes (one-time at purchase)

| Item | Rate | Source |
|---|---|---|
| **Gastos notariales (notary fee)** | **~0.3 % per side (~0.54 % total)** of escritura value; buyer + seller each pay 0.27 %–0.3 % by custom | **Decreto 0188/2017** + SNR Resolución 2026-000964-6 (Feb 2026); verify current Resolución (2026-05-27 verified) |
| **Impuesto de Beneficencia** (Bogotá / Cundinamarca) | **1.0 %** of escritura value | Ley 223/1995; Decreto 352/2002 (Bogotá D.C. 30 % / Cundinamarca 70 %) — **MISSING from prior table; material understatement of buyer-side cost** (2026-05-27 verified) |
| **Impuesto de Registro** (departmental) | **0.3 % (Bogotá inmuebles)** / **0.5–1.0 %** other depts | Ley 223/1995 art. 226+; each departamento Ordenanza sets the rate |
| **Derechos de Registro** (ORIP fee) | tarifa per UVT (Unidad de Valor Tributario) | SNR Resolución de tarifas anual |
| **Retención en la fuente** (when seller is **persona natural** selling activo fijo) | **1 %** of price withheld by notary | **Estatuto Tributario art. 398**; reduced by 10 % per year of holding for vivienda de habitación (Decreto 1625/2016 art. 1.2.4.5.1) — note: applies to natural persons, NOT sociedades (corrected from prior playbook framing) (2026-05-27 verified) |
| **Lawyer / estudio de títulos** | **~1–2 %** | private market |
| **Total buyer-side closing costs (Bogotá)** | ~**2.6–4 %** of price (1 % benef + 0.3 % registro + ~0.27 % notarial + 1 % retención + lawyer + ORIP) | sum of above |

### Plusvalía / capital gains on resale

Two distinct concepts (don't confuse):

1. **Ganancia Ocasional (income tax on capital gain on sale)** — Estatuto Tributario art. 300+:
   - Rate: **15 %** for natural persons (raised from 10 % by **Ley 2277/2022**, eff. 2023).
   - Long-term holding: cost basis indexed via UVT (no inflation discount but adjusted for *renta líquida ocasional*).
   - **Exemption**: first **5,000 UVT** (~COP 249 M @ 2025 UVT) of gain on sole dwelling held ≥ 2 years — reduced from 7,500 UVT by **Ley 2277/2022 art. 31** (eff. 2023), reglamentado por **Decreto 1920/2023** (Estatuto Tributario art. 311-1; ceiling adjusted yearly) — re-quote at 2026 UVT once DIAN Resolución cited (2026-05-27 verified, source DIAN normograma).
2. **Plusvalía urbanística** (Ley 388/1997 art. 73-90) — municipal capture of gain from rezoning / norm-density increase / public infrastructure benefit. Triggered when the POT or a Plan Parcial uplifts what your land may be developed into. Rate 30–50 % of the uplift, captured at next building permit / sale. **Verify with city Secretaría de Planeación** before buying redevelopment plays.

### Wealth tax (Impuesto al Patrimonio)

- Reintroduced by **Ley 2277/2022** for residents (and non-residents on Colombian property) with patrimonio líquido > 72,000 UVT (~COP 3,389 M @ 2025 UVT, ~USD 850 k @ 4,000 COP — re-quote at 2026 UVT once DIAN Resolución cited).
- Rates progressive 0.5 % → 1.5 % above 239,000 UVT.
- **Property is taxed at avalúo catastral or self-declared, whichever is higher** — multipurpose cadastre rollouts are pushing some owners into bracket.

### Inheritance / herencia

- **Ganancia Ocasional 15 %** on the inherited value above exemption (Estatuto Tributario art. 302+).
- Plus notarial costs of sucesión.
- Régimen de gananciales (community of property) and nudo propiedad / usufructo splits common in planning.

### Future risk

- **Multipurpose cadastre rollout** continues 2026+ — predial bills rise when your municipio re-actualizes, but within the Ley 1995/2019 art. 2 / Ley 44/1990 art. 6 topes set out above.
- **Ley 2294/2023 art. 49 one-off rezago adjustment** — **IGAC Resolución 2057 of 30 Dec 2025** reajusta rural avalúos formed or updated before 2018 across **527 municipios** with effect from **1 Jan 2026**; IGAC reported **520 municipios adjusted** as at 23 Feb 2026 and states the avalúo jump is **not automatic or proportional to the tax**. Check whether the municipio of the predio is on IGAC's list before underwriting a rural predial line (2026-08-07 verified).
- **PL 188/2025C + 291/2025C ("Ley Predial Justo")** — would tighten the topes; not law. Cámara ficha lists first-debate ponencias negativa (Gaceta 248/2026) and positiva (Gaceta 378/2026) and a Segundo Debate Cámara ponente assigned 26 Aug 2026, while its Estado still reads Debate de Comisión — first-debate vote date not shown; verify at `https://www.camara.gov.co/ley-predial-justo-175`.
- **Tax-reform cycle**: each Petro / Duque government cycle proposes changes; track Cámara de Representantes + DIAN drafts.
- **Wealth-tax recalibration** politically active.
- **Bogotá Decreto Distrital 639/2025** unifies prior tributary decretos (predial + ICA + impuesto al consumo) into a single codified regime — verify at haciendabogota.gov.co for any changes affecting your year of assessment (2026-05-27 verified).

---

## Section: `--rental`

### Long-term residential — Ley 820 de 2003

- **Annual rent increase capped to IPC** (Índice de Precios al Consumidor) of prior year — **Ley 820/2003 art. 20**. Landlord must notify formally; tenant can refuse non-IPC increases.
- Standard contract minimum 1 year; tenant has right to terminate with 3 months' notice + indemnización; landlord termination grounds limited (Ley 820 art. 22).
- **Garantía**: traditional codeudor or póliza de arrendamiento (insured guarantee, ~3 % of annual rent/year).
- **Tax on rental income** (IRP — natural person, residential):
  - Declaración de renta annual via **DIAN** (Dirección de Impuestos y Aduanas Nacionales).
  - UVT-based progressive brackets; first ~1,090 UVT (~COP 51 M @ 2025 UVT) generally exempt for cédula no laboral; above — progressive 19 %, 28 %, 33 %, 35 %, 37 %, 39 %.
  - Permitted deductions: 25 % renta exenta (cap 790 UVT) + actual costs (administración, predial, intereses crédito hipotecario).
- **Foreign owner without residencia fiscal**: subject to retención en la fuente by tenant/intermediary; **rate 15 %** for arrendamientos pagados a no residentes (Estatuto Tributario art. 408 — verify current rate). Many foreign owners structure via **SAS (Sociedad por Acciones Simplificada)** to align with Régimen Simple de Tributación and limit liability — engage a local **contador público** before signing.

### Short-term rentals (Airbnb / Booking)

**Status**: tightening sharply 2024-2026; varies by city.

#### National baseline (MinCIT + MITUR)

- **Registro Nacional de Turismo (RNT)** — mandatory for any prestador de servicios turísticos including STR (Ley 300/1996 + Ley 1101/2006 + Ley 2068/2020). Register at `https://rnt.confecamaras.co/` via Cámara de Comercio. Renewal annual. **Pending**: MinCIT published a proyecto de decreto on 1 Jul 2026 (comments 2-11 Jul 2026) partially substituting Decreto 1074/2015 Libro 2 Parte 2 Título 4 on the RNT and digital-platform operator obligations; per press *(news-tier — verify)* it would require an individual RNT per vivienda turística unit. No signed decree located as of 2026-09-24 (source [MinCIT proyectos de decreto 2026](https://www.mincit.gov.co/normatividad/proyectos-de-normatividad/proyectos-de-decreto-2026)).
- **Contribución parafiscal de turismo** 2.5 ‰ on revenue (Ley 1101/2006; some exemptions).
- **IVA 19 %** on lodging services (some short-stay below thresholds may apply RST exemption).
- **Régimen de Propiedad Horizontal** (Ley 675/2001) — the **assamblea de copropietarios** can prohibit STR in the reglamento; many luxury edificios (El Poblado, Chicó, Bocagrande) have done so 2023-2025.

#### Bogotá D.C. — **Decreto 538 of 2024** *(claim per second-tier sources — reference NOT verifiable in alcaldiabogota.gov.co/sisjur as of 2026-07; genuine sisjur hits are Decreto 538/2021 bienestar animal + Decreto 538/2025 Sec. Movilidad; verify before relying)*

- **10 % impuesto al consumo** on STR services (lodging tax) effective via the decreto — verify scope at `https://www.haciendabogota.gov.co/`. **Note**: the **national** impuesto al consumo on lodging is **8 %** (Estatuto Tributario art. 512-9); a 10 % distrital rate would be an unusual structure (impuestos al consumo are typically national).
- RNT registration enforcement intensified.
- Operators must declare ICA (Industria y Comercio) and present libros contables.

#### Medellín — El Poblado controversies + 2024-25 rules

- **STR legal basis**: the **national RNT** (Ley 300/1996 + Ley 2068/2020 + Decreto 1836/2021) plus **municipal uso del suelo** under the **POT — Acuerdo 48 de 2014, art. 255**, which governs whether a dwelling may host alojamiento turístico (per EAFIT análisis, cross-checked vs medellin.gov.co uso-del-suelo / Mapgis references). Second-tier sources widely cite an **"Acuerdo 056 de 2024"** as tightening STR in El Poblado, Laureles, Provenza, but that reference is **NOT verifiable in concejodemedellin.gov.co as of 2026-07** — treat POT Acuerdo 48/2014 as the real municipal basis. Many PH régimens have also *de facto* banned STR via reglamento de propiedad horizontal updates.
- **Enforcement active + intensifying into 2026**: the Alcaldía de Medellín identified **1,700+ casas/apartamentos** operating without uso-del-suelo / matrícula documentation (medellin.gov.co, 2024); RNT stock stood at **8,951 alojamientos inscritos as of May 2026** (medellin.gov.co — Secretaría de Turismo). Per the Alcaldía (medellin.gov.co, Secretaría de Gestión y Control Territorial, 24 Mar 2026), the preceding 6 months saw **93 informes técnicos** consolidated (Laureles 21, San Cristóbal 19, El Poblado 16, La Candelaria 13), with **34** of the places found operating without licencia; earlier the Alcaldía reported **8 establecimientos temporarily suspended** in 2025 (to 14 Jul 2025) and **2,000+ RNT anulación requests** for viviendas in baja-mixtura residential zones (medellin.gov.co, 14 Jul 2025).
- Increased Migración Colombia + DIAN inspections 2024-25 driven by housing-affordability backlash.
- The **mediano-plazo POT revision was filed at the Concejo as Proyecto de Acuerdo 104 de 2026 on 19 Aug 2026** (concejodemedellin.gov.co; the Concejo has 90 days to study it) *(pending — not enacted as of 2026-09-24)*; per press (El Colombiano, secondary) it would concentrate viviendas turísticas in alta-mixtura zones and áreas de vocación near metro stations. **Verify current state** at Concejo de Medellín + Secretaría de Turismo / Gestión y Control Territorial before underwriting STR yield.

#### Cartagena

- Centro Histórico under stricter UNESCO + IPCC heritage rules; STR allowed but with PEMP (Plan Especial de Manejo y Protección) constraints.
- Bocagrande / Manga: PH régimen rules vary; many newer towers prohibit.

### Strategic notes

- **Yields**: STR gross yields ~6–12 % est. for well-located premium units in Medellín El Poblado (pre-restrictions); Cartagena ~5–10 % est.; Bogotá Chapinero/Chicó ~4–7 % est. — unsourced ranges; compute as gross STR rent ÷ asking price for the specific unit and verify against listing comps; **net yields after IVA + impuesto al consumo + 2.5 ‰ contribución + administración + predial + IRP est. roughly half of gross**.
- Long-term rental yields (LTR) typically 4–7 % gross national average per Lonja reports.
- **Régimen de propiedad horizontal**: always read the **reglamento** before buying for STR — a reglamento prohibition is binding regardless of municipal STR rules.
- **HOA arrears (estado de cuentas administración)**: critical pre-purchase doc — overdue cuotas attach to the unit, not the prior owner.

---

## Section: `--work=<profession>`

### Job platforms

- **Computrabajo Colombia**: `https://co.computrabajo.com/`
- **elempleo.com**: `https://www.elempleo.com/`
- **Indeed Colombia**: `https://co.indeed.com/`
- **LinkedIn Colombia** — strong in Bogotá / Medellín / Cali for tech, finance, BPO.
- **Magneto** (Magneto365): `https://www.magneto365.com/`
- **Servicio Público de Empleo** (gov): `https://www.serviciodeempleo.gov.co/`
- **Bumeran**, **Konzerta**: regional aggregators.

### Self-employment / business regimes

- **RUT** (Registro Único Tributario) at DIAN — mandatory for any economic activity, ~1 day online via `https://www.dian.gov.co/`.
- **Régimen Simple de Tributación (RST)** — Ley 1943/2018 + Ley 2010/2019 — single integrated tax replacing renta + ICA + INC + complementarios for individuals & sociedades meeting thresholds (revenues < 100,000 UVT). Rate progressive 1.2 %–5.4 % depending on actividad.
- **Régimen Ordinario** — standard income tax + ICA municipal + IVA if applicable.
- **Aportes a Seguridad Social** (statutory rates — confirm governing norm + current rate at MinTrabajo / MinSalud / UGPP before relying): **salud (12.5 %, employer 8.5 % + worker 4 %)** + **pensión (16 %, employer 12 % + worker 4 %)** + **ARL** (work risk, employer-paid 0.522–6.96 %) + cajas de compensación 4 % + ICBF 3 % + SENA 2 % (the last 3 mostly for payroll above 10 SMLMV). Self-employed must remit on Ingreso Base de Cotización (40 % of monthly income, floor SMLMV).
- **Foreign-worker permit**: via **Migración Colombia** — typical paths: M-visa for skilled workers (M-Trabajador with offer), V-visa for short-term, R-visa (residente) after qualifying tenure.
- **Digital nomad visa**: V-visa Nómada Digital introduced 2023 — minimum monthly income ~3× SMLMV (**verify at Cancillería `https://www.cancilleria.gov.co/`**), max 2 years.

### Salaried benchmarks (2025-26)

- **Salario mínimo (SMLMV) 2026**: **COP 1,750,905/mes** (+23 % on 2025; Decreto 1469/2025; the Consejo de Estado suspended it on 12 Feb 2026 and **Decreto 0159 of 19-Feb-2026** re-fixed the same figure transitorily — secondary reports state an auto of 9 Jul 2026 revoked the suspension, restoring Decreto 1469/2025 and leaving 0159 without effect, with the nullity action on the merits still pending (primary auto not read — verify at consejodeestado.gov.co, Rad. 11001-03-25-000-2026-00004-00) — 2026-08-07 verification; suspension-revocation limb added 2026-09-24 from secondary reports). **2025**: COP 1,423,500/mes + auxilio de transporte COP 200,000 (for those earning ≤ 2 SMLMV) — 2026 auxilio de transporte not verified here. 2027 SMLMV: verify at MinTrabajo decreto end of December (typically announced 30 Dec).
- **Median formal monthly wage (DANE GEIH)**: ~COP 1.6–1.8 M nationally; Bogotá ~COP 2.5–3.5 M; Medellín ~COP 2.0–3.0 M (verify at DANE GEIH boletín técnico).
- **English-fluent professionals** in BPO / tech: ~COP 4–10 M/mes (Bogotá, Medellín hubs).

### Catchment heuristics

- **Bogotá metro area**: ~10.5 M (Sabana de Bogotá including Soacha, Chía, Cota, Cajicá) — large catchment all sectors.
- **Medellín metro (Aburrá Valley)**: ~4.0 M — strong tech, fashion, services.
- **Cali metro**: ~2.7 M.
- **Barranquilla metro**: ~2.3 M.
- **Outside major cities**: thinner labor markets; informalidad high (DANE: ~55 % nationally — as-of year not stated; verify current rate at DANE GEIH boletín técnico de empleo informal).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **IDEAM** (Instituto de Hidrología, Meteorología y Estudios Ambientales) | `https://www.ideam.gov.co/` | Hydrology, flood (inundación), drought, climate baseline + projections, IDEAM-Sistema de Alerta Temprana |
| **SGC** (Servicio Geológico Colombiano) | `https://www.sgc.gov.co/` | Seismic, volcanic, landslide (movimientos en masa) hazard maps; SISMOS app |
| **UNGRD** (Unidad Nacional para la Gestión del Riesgo de Desastres) | `https://portal.gestiondelriesgo.gov.co/` | National risk plans, emergency declarations |
| **SNIGRD** | `https://snigrd.gestiondelriesgo.gov.co/` | National Risk Information System; aggregates IDEAM + SGC + municipal |
| **POT / POMCA municipal** | each municipio's Secretaría de Planeación | Plan de Ordenamiento Territorial — defines amenazas natural mapped to urban polygons |
| **DAGRD Medellín** | `https://www.medellin.gov.co/es/dagrd/` | Antioquia geo-risk |
| **IDIGER Bogotá** | `https://www.idiger.gov.co/` | Bogotá D.C. risk maps (sismo, remoción en masa, inundación, incendio forestal) |

### Hazard summary (Colombia)

- **Seismic**: Colombia sits on Nazca-Caribbean-Sudamericana plate junction — **high seismic hazard** along Andean cordilleras. Historical M7.5+ events (1999 Quindío M6.2 was devastating, 1979 Tumaco M8.1, 1983 Popayán M5.5). NSR-10 microzonificación maps (Bogotá, Medellín, Cali, Manizales etc.) define design accelerations.
- **Volcanic**: 13 active volcanoes monitored by SGC. Highest-risk inhabited areas: **Nevado del Ruiz** (Manizales, Caldas — 1985 Armero tragedy), **Galeras** (Pasto), **Nevado del Huila**, **Cerro Machín** (Tolima), **Puracé** (Cauca). Lahar and ash-fall zones mapped; check SGC volcanic atlas.
- **Movimientos en masa (landslide)**: very common Andean slopes; SGC inventario nacional. Major events: Mocoa (2017), Salgar (2015), Útica recurrent. Build-era: cut-and-fill on hillsides + pre-NSR-98 informal construction = highest exposure.
- **Inundación (flood)**: Magdalena / Cauca basins (La Mojana, Mompós, Magangué); Pacific coast (Chocó); periodic ENSO-El Niño/La Niña amplification.
- **Coastal SLR + tropical cyclone**: Caribbean (Cartagena, Santa Marta, Barranquilla, San Andrés) — SLR ongoing per IDEAM/IPCC; San Andrés took direct hits Eta + Iota 2020.
- **Wildfire**: Sabana cundiboyacense + Cauca dry season; intensifying.
- **Tsunami**: Pacific coast (Tumaco, Buenaventura) — historical M8.1+ subduction-zone events.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1984** | No seismic-design code; high collapse risk in M>6 zones. Asbestos-cement (eternit) roofing common; lead pipes in older barrios. |
| **1984–1998** (CCCSR-84 era, post-Popayán '83) | First seismic norm (Decreto 1400/1984); compliance variable. |
| **1998–2010** (NSR-98) | Post-Quindío 1999 quake reform; modern seismic design. Adopted via **Ley 400/1997 + Decreto 33/1998**. |
| **2010+ (NSR-10)** | Current code — **Decreto 926/2010 + Decreto 005/2010** + updates. Mandatory; municipal building permits enforce. Microzonificación per major city (Bogotá, Medellín, etc.). |
| **Régimen de Propiedad Horizontal** | Ley 675/2001 — governs apartments + condos: assemblies, fondo de imprevistos, reglamento, administración. |

### Mandatory diagnostics at sale (estudio de títulos)

| Document | Required because | Where to get |
|---|---|---|
| **Certificado de Tradición y Libertad (CTL)** | Title chain — last 30 yrs minimum | ORIP (Oficina de Registro de Instrumentos Públicos) — `https://www.supernotariado.gov.co/` (SNR portal); ~COP 25,000–60,000, online |
| **Folio de Matrícula Inmobiliaria (FMI)** number | Property identifier | Same — visible on CTL |
| **Cédula Catastral** | Fiscal identifier | IGAC / UAECD / city catastro |
| **Paz y Salvo Predial** | No outstanding predial debt | City Secretaría de Hacienda |
| **Paz y Salvo Valorización** | No outstanding contribución de valorización | City Instituto de Desarrollo Urbano (IDU Bogotá; equivalents elsewhere) |
| **Paz y Salvo Servicios Públicos** | No utility arrears | each operator (acueducto, energía, gas, aseo) |
| **Estado de Cuenta Administración** + acta de asamblea + reglamento (PH) | HOA solvency + STR rules + special assessments | administrador del edificio |
| **Certificado de Uso de Suelo** | Allowed use per POT | Curaduría Urbana / Secretaría de Planeación municipal |
| **Estudio de títulos** | Lawyer review of CTL chain | private abogado, COP 500 k – 2 M |
| **Promesa de compraventa** | Pre-contract (binding) | private abogado, then escritura at notaría |
| **Avalúo comercial** (if mortgage) | Bank requirement | perito de la lonja, COP 500 k – 2 M |

⚠️ **CTL trap**: must show **clean 30-year chain** without rupturas (e.g., falsa tradición — owner registered as "poseedor" not "propietario"; very common in some rural/coastal regions). False-owner fraud also recurrent — verify cédula of seller against Registraduría.

---

## Section: `--mains`

### National regulator + database

- **SSPD** (Superintendencia de Servicios Públicos Domiciliarios): `https://www.superservicios.gov.co/` — supervises water, sewer, electricity, gas, waste; **SUI** (Sistema Único de Información) database for operator-level KPIs.
- **MinVivienda** (Ministerio de Vivienda, Ciudad y Territorio): `https://www.minvivienda.gov.co/` — water + housing policy.

### Major operators (urban)

| City | Water + sewer operator | Electricity | Gas |
|---|---|---|---|
| Bogotá | **EAAB** (Empresa de Acueducto y Alcantarillado de Bogotá) — `https://www.acueducto.com.co/` | Enel-Codensa | Vanti |
| Medellín | **EPM** (Empresas Públicas de Medellín — multi-utility: water + power + gas) — `https://www.epm.com.co/` | EPM | EPM |
| Cali | **EMCALI** — `https://www.emcali.com.co/` | EMCALI | Gases de Occidente |
| Barranquilla | **Triple A** (Sociedad de Acueducto, Alcantarillado y Aseo) — `https://www.aaa.com.co/` | Air-e | Gases del Caribe |
| Cartagena | **Aguas de Cartagena (Acuacar)** — `https://www.acuacar.com/` | Afinia | Surtigas |

### Coverage

- **Urban (cabecera municipal)**: water + sewer near-universal in Tier-1 cities (Bogotá, Medellín, Cali, Barranquilla, Bucaramanga, Manizales, Pereira, Cartagena coverage > 95 % per SSPD SUI 2023-24). Sewage treatment lags coverage — many cities still discharge partially untreated.
- **Rural (resto)**: variable; many veredas rely on acueducto veredal (community-managed) + pozo séptico.
- **Verification path**:
  1. Check the **estado de servicios públicos** cert from each operator.
  2. Cross-check at **SSPD SUI** for the operator's coverage in the barrio.
  3. For STR: confirm potable-water capacity (some Cartagena historic centro buildings have intermittent supply requiring tinacos / rebombeo).

### Costs

- **Connection fee** (where mains exists): COP 1–5 M typical urban.
- **Septic-to-mains conversion**: COP 5–20 M depending on distance.
- **Pozo séptico new build (rural)**: COP 5–15 M.
- **Monthly bill (urban estrato 4-5, family of 3)**: water ~COP 80–150 k, electricity ~COP 150–400 k, gas ~COP 30–80 k — **estrato cross-subsidy hugely amplifies bills for estrato 5-6**.

---

## Cost benchmarks (CO 2026)

| Item | Cost (COP) | Notes |
|---|---:|---|
| Gastos notariales | 0.27 % of escritura | Decreto 0188/2017; verify current Resolución SNR |
| Impuesto de Registro (departmental) | 0.5–1.0 % | per Ordenanza departamental |
| Retención en la fuente | 1.0 % | when seller is persona natural selling activo fijo (Estatuto Tributario art. 398) — NOT sociedades; see --tax row |
| Estudio de títulos (lawyer) | 500 k – 2 M | per 30-yr CTL review |
| Building inspection (peritaje técnico) | 1 M – 3 M | rare in CO; recommend insist for pre-2010 builds |
| Avalúo comercial (mortgage) | 500 k – 2 M | perito de la Lonja |
| **Predial Unificado (annual)** | varies — COP 200 k – 30 M+ | function of avalúo × tasa por mil; estrato 5-6 high end |
| Administración (HOA) | **0.5–1.5 % of value/yr** | estrato 5-6 luxury edificio higher; varies wildly |
| **Total transaction cost (buyer side)** | **~2–4 % of price** | sum of above |
| Renovación cocina (60 m²) | 25 M – 80 M | mid-range |
| Renovación baño completo | 8 M – 25 M | per baño |
| Pintura interior (100 m²) | 1.5 M – 4 M | labor + materiales |
| Reforzamiento estructural (post-NSR-10 retrofit) | 100 k – 500 k / m² built | depending on tipología |

## Active fiscal incentives (2025-2026)

- **Mi Casa Ya** — MinVivienda subsidy for first-time VIS buyers (down-payment cover + interest-rate subsidy via **FRECH-Banca**) — verify current cupos at `https://www.minvivienda.gov.co/viceministerio-de-vivienda/mi-casa-ya/subsidio-familiar-de-vivienda-nueva-cloned`
- **FRECH (Fondo de Reserva para la Estabilización de la Cartera Hipotecaria)** — BanRep + MinVivienda interest-rate subsidies for new-build (VIS + VIP).
- **VAT exemption** on construction VIS up to 135 SMLMV (Ley 1607/2012 + updates).
- **Ley 1715/2014 + Ley 2099/2021** — renewable energy retrofit tax credits (50 % deduction over 15 years for solar PV, eficiencia energética).
- **Renta exenta vivienda nueva** — historical incentive periods; verify current via DIAN.

## Common listing platforms

- Metrocuadrado, Finca Raíz, Properati, CienCuadras, OLX Colombia, Habi (iBuyer Bogotá/Medellín/Cali), Mercado Libre Inmuebles.

## Caveats unique to CO

- **Estrato system (1-6)** controls utility tariffs, predial bands, plusvalía calculation, and many services — estrato 6 can pay 5× the per-kWh / per-m³ of estrato 1 (Ley 142/1994 cross-subsidy regime). Always **check the estrato of the dwelling** (visible on any utility bill) before underwriting cost-of-ownership.
- **Multipurpose cadastre rollout** is mid-flight 2020-2026 — actualisation raises the avalúo, but the **2-3× predial-bill claim is OVERSTATED**: annual bills are capped at IPC + 8pp (actualizado) / max 50 % (not actualizado) per **Ley 1995/2019 art. 2** and max 2× per **Ley 44/1990 art. 6** (100 % of IPC for estratos 1-2 up to 135 SMMLV). Caps do not cover lotes urbanizables no urbanizados, autoavalúo predios or a changed destino económico / área / construcción, where bigger jumps are lawful (2026-08-07 verified).
- **CTL must show clean 30-year chain** — false-tradition (poseedor not propietario), missing inheritances, false owners are recurrent in coastal + rural regions.
- **STR Bogotá: Decreto 538/2024** *(reference NOT verifiable in alcaldiabogota.gov.co/sisjur as of 2026-07)* + **Medellín El Poblado restrictions 2024-26** — real municipal basis is **POT Acuerdo 48 de 2014 (art. 255) uso del suelo**, not the widely-cited **"Acuerdo 056/2024"** *(056 NOT verifiable in concejodemedellin.gov.co)*; PH régimen reglamento can also prohibit independent of city rules — read it before underwriting STR yield.
- **Plusvalía urbanística (Ley 388/1997)** can capture 30-50 % of rezoning gain.
- **Andean seismic risk + NSR-10** — pre-1998 builds in active microzones carry significant retrofit / collapse risk; insist on peritaje técnico.
- **Volcanic-risk towns**: Manizales, Pasto, Popayán, Ibagué — require reading SGC zonificación.
- **Coastal heat + humidity + sargazo**: Cartagena/Santa Marta historic centro maintenance burden high.
- **Currency volatility**: COP swung 3,800-4,900 vs USD 2022-2026; dollarizing the deal pre-signing protects USD-denominated savings but is non-standard for Colombian sellers.
- **Régimen de propiedad horizontal (Ley 675/2001)**: assamblea decisions binding; check past actas + fondo de imprevistos status.
- **SAS structure** common for foreign buyers seeking liability separation + ICA optimisation; consult contador público.
- **Patrimonios autónomos (fiducia)** used in pre-construction (preventa) contracts — escrow funds in fiduciaria until handover. Verify the fiduciaria's vigilancia by SuperFinanciera.

## Reddit / forum sources

- **r/Colombia**, **r/medellin**, **r/bogota**, **r/cali_colombia**, **r/cartagena**
- **r/digitalnomad** (Medellín, Bogotá threads)
- **NomadList Medellín / Bogotá**
- **Expat.com Colombia forum**
- **InternationalLiving Colombia** (anglo, treat as marketing — not primary)

## Verification authorities

| Authority | When to call |
|---|---|
| **IGAC** | National cadastre — parcel info outside Bogotá/Medellín/Cali |
| **UAECD Bogotá** | Bogotá parcel + avalúo |
| **Catastro Medellín / Cali** | city parcel + avalúo |
| **ORIP (city-specific)** | CTL request + register of escritura |
| **SNR** (Superintendencia de Notariado y Registro) | National notary + register oversight; tarifa schedules |
| **SSPD** | Utility-operator KPIs |
| **MinVivienda** | Mi Casa Ya + FRECH + housing policy |
| **BanRep** | TRM, IPVU, monetary policy |
| **DANE** | IPVN, GEIH, ECV, demographics |
| **DIAN** | RUT, declaración de renta, retención |
| **MITUR / MinCIT** | RNT for STR |
| **Migración Colombia** | Visa enforcement |
| **Cancillería** | Visa application |
| **Curaduría Urbana / Planeación municipal** | Use of soil + building permits + POT consultation |
| **Cámara de Comercio** | RNT registration + SAS constitution |

## Quirks to know

- **Estrato lookup**: visible on every utility bill; published by city catastro. Critical for cost-of-ownership.
- **Folio de matrícula vs cédula catastral**: legal vs fiscal IDs — both required for clean estudio de títulos.
- **Multipurpose cadastre rollout status**: check **IGAC cobertura tracker** for the municipio — un-actualised areas show 30-60 % undervaluation; once actualised, predial jumps.
- **SAS for foreign buyers**: Sociedad por Acciones Simplificada — set up in ~1 week via Cámara de Comercio; ~COP 1-3 M total cost. Allows RST (régimen simple) optimisation; consult contador.
- **Renta presuntiva**: derogada para 2022 en adelante (Ley 2010/2019 art. 90 + Ley 2155/2021), but historical declarations may show artefacts.
- **Régimen de propiedad horizontal (Ley 675/2001)**: assamblea ordinaria annual; coeficiente de copropiedad governs voting + cuotas. Always ask for **últimas 3 actas** + **fondo de imprevistos** balance + **reglamento PH**.
- **Patrimonios autónomos (fiducia mercantil)**: pre-construction escrow under fiduciaria vigilada by SuperFinanciera — protects buyer if developer defaults pre-handover.
- **TRM**: Tasa Representativa del Mercado — daily official COP/USD published by SuperFinanciera + BanRep; used for any USD-denominated obligation.
- **UVT**: Unidad de Valor Tributario — annually adjusted (DANE-IPC), used as base for all tax thresholds. **2025 UVT = COP 49,799** per Resolución DIAN; verify 2026 UVT at DIAN.
- **Notary rotation**: notarías numbered per circuito; choose by jurisdiction (typically the notaría closest to where the inmueble is registered).
- **Pico y placa inmobiliario**: nope — only for vehicles. But rotating water-restriction (racionamiento) recently in Bogotá (2024-25 Niño-related) can affect day-to-day.

## Source URL templates

| Source | URL pattern |
|---|---|
| IGAC (cadastre) | `https://www.igac.gov.co/` |
| IGAC Geoportal | `https://geoportal.igac.gov.co/` |
| UAECD Bogotá (catastro) | `https://www.catastrobogota.gov.co/` |
| Catastro Bogotá mapas | `https://mapas.bogota.gov.co/` |
| SNR (Superintendencia Notariado y Registro) | `https://www.supernotariado.gov.co/` |
| SSPD | `https://www.superservicios.gov.co/` |
| BanRep | `https://www.banrep.gov.co/` |
| BanRep TRM | `https://www.banrep.gov.co/es/estadisticas/trm` |
| BanRep IPVU | `https://www.banrep.gov.co/es/estadisticas/indice-precios-vivienda-nueva-usada` |
| DANE IPVN | `https://www.dane.gov.co/index.php/estadisticas-por-tema/construccion/indice-de-precios-de-vivienda-nueva-ipvn` |
| DANE GEIH | `https://www.dane.gov.co/index.php/estadisticas-por-tema/mercado-laboral/empleo-y-desempleo` |
| DIAN | `https://www.dian.gov.co/` |
| MinVivienda | `https://www.minvivienda.gov.co/` |
| MinCIT | `https://www.mincit.gov.co/` |
| RNT (Registro Nacional de Turismo) | `https://rnt.confecamaras.co/` |
| Migración Colombia | `https://www.migracioncolombia.gov.co/` |
| Cancillería (visas) | `https://www.cancilleria.gov.co/tramites_servicios/visa` |
| IDEAM | `https://www.ideam.gov.co/` |
| SGC (Servicio Geológico Colombiano) | `https://www.sgc.gov.co/` |
| UNGRD | `https://portal.gestiondelriesgo.gov.co/` |
| SNIGRD | `https://snigrd.gestiondelriesgo.gov.co/` |
| IDIGER Bogotá | `https://www.idiger.gov.co/` |
| DAGRD Medellín | `https://www.medellin.gov.co/es/dagrd/` |
| Hacienda Bogotá (predial + ICA) | `https://www.haciendabogota.gov.co/` |
| Hacienda Medellín | `https://www.medellin.gov.co/es/secretaria-de-hacienda/` |
| Metrocuadrado | `https://www.metrocuadrado.com/` |
| Finca Raíz | `https://www.fincaraiz.com.co/` |
| Properati | `https://www.properati.com.co/` |
| CienCuadras | `https://www.ciencuadras.com/` |
| Habi | `https://www.habi.co/` |
| Galería Inmobiliaria | `https://galeriainmobiliaria.com.co/` |
| Lonja Bogotá | `https://www.lonjadebogota.org.co/` |
| Lonja Medellín | `https://lonjadecolombia.com.co/` |
| INVÍAS | `https://www.invias.gov.co/` |
| ANI | `https://www.ani.gov.co/` |
| Servicio Público de Empleo | `https://www.serviciodeempleo.gov.co/` |

## Status

✅ **Fully populated** as of 2026-05-01.

**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government / regulated-entity sources + cost benchmarks + caveats.

**Confidence**: **HIGH** for visa structure (Cancillería + Decreto 1067/2015 + Resolución 5477/2022 art. 79 + Resolución 10434/2023 art. 76), notary + cadastre + ORIP framework (SNR + IGAC), tax structure at the national level (Estatuto Tributario + Ley 2277/2022 + Ley 1450/2011 + Ley 388/1997), Ley 820/2003 LTR cap, NSR-10 seismic code, Ley 675/2001 PH régimen.

**MEDIUM** for: per-municipio predial rates (vary by Acuerdo, evolving with multipurpose-cadastre rollout — verify each year per city); STR rules (city-by-city, 2024-26 reforms ongoing — the widely-cited Bogotá "Decreto 538/2024" + Medellín "Acuerdo 056/2024" are NOT verifiable in official sources; real bases are the national RNT + municipal uso del suelo, POT Acuerdo 48/2014); current SMLMV (verify each Dec 30 MinTrabajo decreto); current UVT (verify each year DIAN Resolución).

**LOW** for: parcel-level price/m² (use only as zone-average context — must cross-check Lonja + Metrocuadrado comparables for the specific barrio + estrato).

**Last verified**: 2026-08-07 (`--tax` / `--price` catastro-multipropósito legal basis + predial-cap correction; `--visa` M-visa investment thresholds re-verified — Resolución 5477/2022 art. 79 real-estate ≥ 350× / FDI > 650× SMLMV, Visa R accumulation via Resolución 10434/2023 art. 76, 2026 SMLMV COP 1,750,905; other sections 2026-05-27). RNT pending MinCIT proyecto de decreto added 2026-09-24 in the October regwatch wave. `--rental` Medellín STR block re-verified 2026-09-24 against Alcaldía releases (1,700+ Mar 2024; 8 suspensions + 2,000+ RNT anulación requests Jul 2025; 93 informes / 34 sin licencia Mar 2026; 8,951 RNT May 2026), the POT Acuerdo 48/2014 art. 255 text, and the Concejo's 19 Aug 2026 filing of Proyecto de Acuerdo 104 de 2026; the '8 viviendas selladas across comunas 10/11/14/16' figure was not found and was replaced (November regwatch wave, run early). Finance / visa tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

**Reform watch (next 12 mo)**:
1. **Catastro multipropósito + Ley 2294/2023 art. 49 rezago adjustment** — track IGAC cobertura updates per municipio and the **Resolución 2057 of 30 Dec 2025** rural reajuste (527 municipios from 1 Jan 2026; 520 adjusted at 23 Feb 2026); plus **PL 188/2025C + 291/2025C ("Ley Predial Justo")**, which would tighten the predial topes — Cámara ficha lists first-debate ponencias negativa (Gaceta 248/2026) and positiva (Gaceta 378/2026) and a Segundo Debate Cámara ponente assigned 26 Aug 2026 (Estado still reads Debate de Comisión; vote date not shown — verify at camara.gov.co).
2. **Bogotá 'Decreto 538/2024'** (unverified — not found in sisjur) / MinCIT RNT proyecto de decreto STR enforcement + possible widening to other consumo categories.
3. **Medellín Concejo — POT Proyecto de Acuerdo 104 de 2026** (radicado 19 Aug 2026, 90-day Concejo study window) — would re-zone where vivienda turística may operate (per press, secondary: alta mixtura + áreas de vocación); track debates + adoption at concejodemedellin.gov.co.
4. **Cancillería visa schedule** — M-visa thresholds (350× / 650× SMLMV) re-price **every 1 Jan** with the SMLMV and **daily** in USD terms with the TRM; the 2026 SMLMV (**COP 1,750,905**, +23 %, **Decreto 1469/2025**; suspended by the Consejo de Estado 12 Feb 2026 and re-fixed transitorily by **Decreto 0159 of 19-Feb-2026** — `https://dapre.presidencia.gov.co/normativa/normativa/DECRETO%20No.%200159%20DEL%2019%20DE%20FEBRERO%20DE%202026.pdf` — until, per secondary reports, an auto of 9 Jul 2026 revoked the suspension and left 0159 without effect; primary auto not read, verify at consejodeestado.gov.co Rad. 11001-03-25-000-2026-00004-00) already moved them to **COP 612.8 M / COP 1,138.1 M**. The nullity ruling on the merits is still outstanding per the same secondary reports — re-confirm the SMLMV base at Presidencia / MinTrabajo before relying on the COP figures.
5. **DIAN UVT 2026** — recalibrates all tax thresholds (predial bands, ganancia ocasional exemption, wealth-tax floor).
6. **Reforma tributaria pendiente** — Petro government second-term tax adjustments under discussion in Congreso 2026.

## Extension TODOs (deepen on first real run)

- [ ] Per-city predial sazón table (Bogotá, Medellín, Cali, Cartagena, Barranquilla, Bucaramanga, Pereira) with each Acuerdo Municipal year + bands
- [ ] Per-municipio multipurpose cadastre actualización status from IGAC tracker
- [ ] STR PH-régimen reglamento prohibition database (top edificios in El Poblado, Chicó, Bocagrande)
- [ ] Microzonificación seismic maps per major city (NSR-10 anexos)
- [ ] FRECH cupos + MCY allocation tracker (MinVivienda monthly)
- [ ] Patrimonios autónomos (fiducia) due-diligence checklist for preventa
- [ ] Foreign-buyer SAS setup walkthrough (Cámara de Comercio + DIAN RUT + cuenta bancaria + RUE)
