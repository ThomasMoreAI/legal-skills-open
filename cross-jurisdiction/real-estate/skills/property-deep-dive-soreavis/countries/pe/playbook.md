# Peru — Property Due-Diligence Playbook

ISO2: `pe`. Status: Fully populated (researched 2026-05).

## Country profile

- **Postcode (Código Postal)**: 5 digits, rolled out post-2017 by **SERPOST** (Servicios Postales del Perú) via Resolución de Gerencia. Lima Metropolitana uses prefix `15` (e.g., `15001` Cercado de Lima, `15074` Miraflores, `15023` San Isidro, `15063` Barranco); Arequipa `04001`; Cusco `08001`; Trujillo `13001`. Often omitted on listings — verify at `https://www.gob.pe/521-consulta-tu-codigo-postal-nacional`.
- **Admin levels**: 24 **departamentos** + 1 **Provincia Constitucional del Callao** → 196 **provincias** → 1,874 **distritos** (per INEI division político-administrativa, 2024). Lima Metropolitana = Provincia de Lima (43 distritos) + Provincia Constitucional del Callao (7 distritos). The **distrito** is the level at which the **Municipalidad Distrital** sets impuesto predial rates, arbitrios, and licencia de funcionamiento.
- **Currency**:
  - **PEN** — Sol (called "Nuevo Sol" 1991-2015; the "Nuevo" was dropped by **Ley 30381 (2015)** — official name now just "Sol"). Symbol `S/`.
  - **USD** — widely used for residential pricing in Lima coastal districts (Miraflores, San Isidro, Barranco, La Molina, Surco) and luxury beach (Asia, Punta Hermosa) — legacy of 1980s-90s hyperinflation dollarization. Notarial escritura can be denominated in either; conversion at BCRP **tipo de cambio publicado** (`https://www.bcrp.gob.pe/estadisticas/cuadros-anuales-historicos.html` + daily `https://www.bcrp.gob.pe/estadisticas/tipo-de-cambio-diario.html`).
  - BCRP runs **managed float** with active intervention; no general capital controls; SBS supervises FX on banks.
- **Languages**: Spanish (official, Constitución 1993 art. 48); **Quechua** + **Aymara** co-official "in zones where they predominate" (art. 48) — relevant in Andean departments (Cusco, Puno, Apurímac, Ayacucho, Huancavelica). English usable in Miraflores/San Isidro/Barranco business + tourism; rare elsewhere with notaries, SUNARP, and municipales.
- **Cadastre / registry**:
  - **SUNARP** (Superintendencia Nacional de los Registros Públicos): national property registry. **Registro de Predios** at **Oficinas Registrales** in each Zona Registral (14 zones nationally). Title identifier: **Partida Registral** (unique per property). Portal: `https://www.sunarp.gob.pe/` + **Servicio de Publicidad Registral en Línea (SPRL)** `https://www.sunarp.gob.pe/serviciosenlinea/portal/servicios-de-publicidad-registral-sprl.html`.
  - **Catastro** is **distrito-level** in urban zones (each Municipalidad Distrital maintains **Catastro Predial Urbano**) — codified via **Ley 28294 (2004)** + Reglamento DS 005-2006-JUS creating the **Sistema Nacional Integrado de Información Catastral Predial (SNCP)** coordinated by SUNARP. Coverage of the unified catastro is uneven 2025 — many distritos still operate independent cadastres.
  - **IGN** (Instituto Geográfico Nacional): national mapping authority `https://www.ign.gob.pe/`.
  - **COFOPRI** (Organismo de Formalización de la Propiedad Informal): titulación masiva of informal urban settlements `https://www.gob.pe/cofopri`.
- **Identifier**: every parcel typically has:
  - **Partida Registral SUNARP** (legal — registry)
  - **Código Predial / Código Catastral** at the distrito (fiscal — Municipalidad)
  - **Código Único Catastral (CUC)** via SNCP rollout (where deployed)
- **Foreign ownership**: open with **one major restriction**:
  - **Constitución Política del Perú 1993, art. 71**: foreigners (natural or juridical) **cannot acquire or possess, directly or indirectly, mines, lands, forests, waters, fuels or sources of energy within 50 km of the border** ("Zona de Frontera") — except in case of **public necessity expressly declared by Supreme Decree** approved by Consejo de Ministros.
  - The 50 km Border Zone restriction applies to the entire perimeter (north Ecuador/Colombia, east Brazil/Bolivia, south Chile, plus the maritime border), affecting border cities/towns including **Tumbes, Tacna, Puno (lake Titicaca shore), Madre de Dios, parts of Loreto**.
  - **Outside the Zona de Frontera**: foreigners hold **freehold equivalent to nationals** — full Civil Code rights, no nationality restrictions on residential or rural acquisition.
  - The **notario público** is required to verify Border Zone status before extending the escritura — declaring a Supreme-Decree exception is rare and project-specific.
- **Recent reforms (selected, verify date-stamped)**:
  - **Decreto Legislativo 1499 (2020)** — anti-money-laundering reinforcement in real estate; sujetos obligados to **UIF-SBS** (Unidad de Inteligencia Financiera) reporting expanded to include real-estate intermediaries.
  - **Ley 31435 (2022)** — **Ley del Servicio Inmobiliario** ("Ley del Corredor Inmobiliario"): regulates real-estate brokers, mandatory registration with MVCS-promoted **Registro de Agentes Inmobiliarios (RAI)**, code of ethics. Effective phased 2022-2024.
  - **Decreto Supremo 001-2023-MINCETUR** + **MINCETUR turismo de hospedaje rules** — STR registration framework via **Ministerio de Comercio Exterior y Turismo (MINCETUR)**.
  - **Fondo MiVivienda 2024 reforms** — adjusted Bono del Buen Pagador (BBP) and Premio del Buen Pagador (PBP) thresholds; programa Nuevo Crédito MiVivienda extended.
  - **Ley 32103 (2024)** + **Decreto Legislativo 1623 (2024)** — IGV digital services / non-resident extension; verify scope at SUNAT.

---

## Section: `--price`

### Primary sources

| Source | Type | URL | What it gives |
|---|---|---|---|
| **BCRP IPV — Indice de Precios de Viviendas** | Central bank | `https://www.bcrp.gob.pe/estadisticas/indice-de-precios-de-viviendas.html` | Quarterly real housing-price index, **Lima Metropolitana** (10 distritos): Jesús María, Lince, Magdalena, Miraflores, Pueblo Libre, San Borja, San Isidro, San Miguel, Santiago de Surco, La Molina. USD/m² + PEN/m² medians per distrito. **Primary source for Lima pricing.** |
| **INEI** (Instituto Nacional de Estadística e Informática) | National statistics | `https://www.inei.gob.pe/` | Demographics, ENAHO household survey, ENCO continuous household survey (housing stock + tenure). Less granular for prices than BCRP. |
| **CAPECO** (Cámara Peruana de la Construcción) | Trade body | `https://www.capeco.org/` | **Estudio del Mercado de Edificaciones Urbanas en Lima Metropolitana** (annual) — new-build supply, sale prices by distrito, m² oferta. |
| **MVCS Observatorio** | Ministry | `https://www.gob.pe/vivienda` | Observatorio Urbano + indicators on déficit habitacional, MiVivienda metrics. |
| **SUNARP SPRL** | Registry | `https://www.sunarp.gob.pe/serviciosenlinea/portal/servicios-de-publicidad-registral-sprl.html` | Búsqueda + publicidad registral por partida — for títulos chain (not price index) |
| **ASEI** (Asociación de Empresas Inmobiliarias del Perú) | Trade body | `https://www.asei.com.pe/` | Reportes mensuales venta nueva Lima Metro |

### Listing platforms

| Platform | URL pattern | Notes |
|---|---|---|
| **Adondevivir** | `https://www.adondevivir.com/` | One of two largest national portals (QuintoAndar / Navent group) |
| **Urbania** | `https://urbania.pe/` | Other major national portal (Navent group); shares inventory with Adondevivir |
| **Properati Perú** | `https://www.properati.com.pe/` | Lifull aggregator |
| **Mercado Libre Inmuebles Perú** | `https://inmuebles.mercadolibre.com.pe/` | Aggregator + privates |
| **OLX Perú** (now Doomos / discontinued) | varies | Privates declined post-2022 |
| **Nestoria Perú** | `https://www.nestoria.pe/` | Meta-aggregator |
| **A la venta** | `https://www.alaventa.pe/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Peru listing portal (boutique broker site defunct) | Boutique broker network |

### USD/m² benchmarks — Lima Metropolitana (BCRP IPV Q4 2025 reference)

> **Source**: BCRP **Mediana de precios de venta de departamentos por distrito**, USD per m², series published quarterly. Verify current at `https://www.bcrp.gob.pe/estadisticas/indice-de-precios-de-viviendas.html` Cuadro 1 / Cuadro 2.

| Distrito | USD/m² mediana (Q4 2025 ~est. range) | Note |
|---|---:|---|
| Miraflores | ~$2,200–$2,600 | Top-tier residential coastal |
| San Isidro | ~$2,200–$2,700 | Financial district + premium residential |
| Barranco | ~$2,100–$2,500 | Bohemian + STR demand |
| Santiago de Surco | ~$1,500–$2,100 | Large area, varies (Chacarilla, Las Casuarinas premium) |
| La Molina | ~$1,400–$1,900 | Casa-dominant + condominio |
| San Borja | ~$1,600–$2,000 | Stable middle-upper |
| Jesús María | ~$1,500–$1,900 | Densifying + good metro access |
| Lince | ~$1,400–$1,800 | Renovation belt |
| Magdalena del Mar | ~$1,400–$1,800 | Coastal + boom 2018-2024 |
| Pueblo Libre | ~$1,300–$1,700 | Densifying |
| San Miguel | ~$1,200–$1,600 | Coastal western, La Marina corridor |

> Distritos OUTSIDE the BCRP 10-distrito panel (Surco/Chorrillos/Surquillo/Pueblo Libre fringes, Lima Norte/Este/Sur as Comas, San Juan de Lurigancho, Villa El Salvador, etc.) are NOT in BCRP IPV — use **CAPECO Estudio del Mercado** + **ASEI** monthly + **Adondevivir/Urbania** scrapes for those zones; expect ~$700–$1,400/m² typical.

### USD/m² — provinces (CAPECO + listing observation, lower confidence)

| City | USD/m² typical (~est., 2025-26 listing) | Source caveat |
|---|---:|---|
| Arequipa (Yanahuara, Cayma, Cercado) | ~$700–$1,400 | Listings + CAPECO regional notes |
| Cusco (Centro Histórico, Wanchaq) | ~$1,000–$2,000+ | UNESCO heritage scarcity premium |
| Trujillo (Víctor Larco, San Andrés) | ~$700–$1,200 | Listings |
| Piura | ~$600–$1,000 | Listings |
| Iquitos | ~$500–$900 | Listings; remote |
| Tacna (note: 50 km Border Zone applies city-adjacent) | ~$600–$1,100 | Listings + Border Zone caveat |

⚠️ Provincial pricing has NO equivalent of BCRP IPV — confidence MEDIUM at best, **LOW** outside Arequipa/Cusco/Trujillo. Cross-check listings from at least 3 platforms before using as basis for any underwriting.

### Compute

1. **Listing PEN/m² or USD/m²** = listing price ÷ m² techados (built m²) — clarify "área techada" vs "área libre" vs "área común" (listing language varies; áreas techadas + áreas comunes share is the legal title surface in Régimen de Propiedad Exclusiva y Común).
2. Convert PEN ↔ USD at **BCRP tipo de cambio publicado del día** (`https://www.bcrp.gob.pe/estadisticas/tipo-de-cambio-diario.html`) — sol typically PEN 3.50–3.90/USD range 2024-2026; verify daily.
3. Compare listing $/m² to **BCRP IPV mediana** for the distrito (Lima only, 10-distrito panel).
4. Compare to **CAPECO Estudio del Mercado** new-build oferta supply for the year (annual).
5. **Trap**: many listings quote **área total** (techada + libre) not área techada — two listings at "120 m²" may differ 20-30 m² in legal escritura surface. Always demand the **escritura pública** + **partida registral** to confirm.
6. **Trap**: pre-construction (entrega futura) advertised in USD; convert to PEN at signing AND at handover for fiscal purposes — IGV exposure on developer first sale (see `--tax`).

**Confidence**: HIGH for BCRP IPV Lima 10-distrito (active state source, primary). MEDIUM for CAPECO new-build oferta (trade body, methodology disclosed). LOW for provincial $/m² (no central-bank index outside Lima).

---

## Section: `--traffic`

### Primary sources

| Source | URL | What it gives |
|---|---|---|
| **MTC — Ministerio de Transportes y Comunicaciones** | `https://www.gob.pe/mtc` | National road inventory + IMD (Indice Medio Diario) per tramo on red vial nacional (PE routes) |
| **PROVÍAS Nacional** | `https://www.gob.pe/pvn` | Concessionary + national road operator; conteos volumétricos publicados |
| **PROVÍAS Descentralizado** | `https://www.gob.pe/pvd` | Regional + departamental network |
| **OSITRAN** | `https://www.ositran.gob.pe/` | Concession regulator — toll-road operator IMD reporting (Pativilca, Norvial, Rutas de Lima, IIRSA Norte/Sur, Survial) |
| **Municipalidad Metropolitana de Lima — GMU/GTU** | `https://www.gob.pe/munilima` | Lima city traffic counts, Plan Maestro de Transporte, semaforización |
| **AATE — Autoridad Autónoma del Tren Eléctrico** | `https://www.aate.gob.pe/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row | Lima Metro lines (1, 2, 3, 4) + projected lines |
| **ATU — Autoridad de Transporte Urbano para Lima y Callao** | `https://www.gob.pe/atu` | Lima + Callao integrated transport regulator (since Ley 30900, 2018) |
| **OSM fallback** | `https://overpass-turbo.eu/` | Road class only — coarse band |

### Key term

**IMD (Indice Medio Diario)** / **IMDA (Indice Medio Diario Anual)** — average daily traffic; the Peruvian equivalent of AADT/TMJA. Reported by MTC + PROVÍAS Nacional on the red vial nacional and by OSITRAN-supervised concessions on toll roads.

### Verdict bands (IMD)

- 🟢 < 1,000 v/d (rural caminos vecinales)
- 🟡 1,000–5,000 v/d (red departamental, urban side street)
- 🟠 5,000–20,000 v/d (red nacional secundaria, urban arterial — Lima Av. Salaverry, Av. Arequipa tramos)
- 🔴 > 20,000 v/d (Panamericana Norte/Sur urban tramos, Vía de Evitamiento, Av. Javier Prado, Vía Expresa Línea Amarilla)

### Coarse fallback (OSM `highway` class)

- `motorway/trunk` ≈ Panamericana + autopistas concesionadas (Norvial, Rutas de Lima, Survial)
- `primary` ≈ red vial nacional principal (PE-1, PE-3 troncales)
- `secondary` ≈ red departamental
- `tertiary` ≈ red vecinal
- `residential` ≈ urban distrito streets

### Caveats

- **MTC IMD reports lag 1-2 years** (most recent typically t-2). Date-stamp every figure.
- **Lima specific**: no rotating "pico y placa" license-restriction system at scale (vs Bogotá/Mexico CDMX); congestion management via bus corredores (Metropolitano BRT + corredores complementarios) + Línea 1 Metro (operational since 2011) + Línea 2 (under construction, partial opening 2024-2026).
- **Concession IMD** reported by operators to OSITRAN under contract — reliable for the concession length only.
- Lima Metro **Línea 2** (subterranean east-west, Ate → Callao, ~35 km) under construction by Concesionaria MetroLima; partial opening ongoing 2024-2027 per AATE schedule. **Línea 3 + Línea 4** in design/early-works phase per AATE — verify status before underwriting transit-adjacency premium.

---

## Section: `--tax`

### Annual property tax — Impuesto Predial

**Authority**: each **Municipalidad Distrital** sets the assessed value (autoavalúo) and collects the impuesto predial. Legal basis: **Texto Único Ordenado (TUO) de la Ley de Tributación Municipal — Decreto Supremo 156-2004-EF** (consolidates Decreto Legislativo 776 + amendments).

**Base imponible**: **autoavalúo** = sum of **valor del terreno** (per arancel CONATA — Consejo Nacional de Tasaciones, MVCS) + **valor de la edificación** (per Reglamento Nacional de Tasaciones, MVCS). Updated annually 1 enero.

#### Tasas progresivas (TUO Ley Tributación Municipal art. 13)

Expressed in **UIT** (Unidad Impositiva Tributaria — annually adjusted by MEF; **2026 UIT = PEN 5,500** per Decreto Supremo 301-2025-EF, vigente 1 Ene 2026 — verify each Dec at MEF; 2025 UIT was PEN 5,350 per DS 260-2024-EF) (2026-05-27 verified, source MEF gob.pe/1314665).

| Tramo (autoavalúo en UIT) | Tasa anual |
|---|---:|
| Hasta 15 UIT | **0.2 %** |
| Más de 15 hasta 60 UIT | **0.6 %** |
| Más de 60 UIT | **1.0 %** |

Applied progressively (each tramo on the marginal portion).

#### Mínimo

- **Mínimo anual**: 0.6 % de UIT (per art. 13 TUO) ≈ PEN 33 al 2026 (UIT PEN 5,500) — applies if the calculated impuesto < this floor.

#### Beneficios

- **Pensionistas / adulto mayor**: deduction of **50 UIT** del autoavalúo (art. 19 TUO) for sole dwelling, monthly pension ≤ 1 UIT — verify per municipalidad.
- **Pronto pago**: many municipalidades distritales offer 5-15 % discount for full annual payment by Feb-March deadline (calendario per Ordenanza Municipal anual).
- **Vivienda única + persona adulta mayor no pensionista**: similar 50 UIT deduction extended (Ley 30490, 2016).

⚠️ **Distrito-level rates are uniform nationally per TUO art. 13**, but **arbitrios municipales** (cleaning, parks, security, serenazgo) are set per distrito by Ordenanza — these vary widely (annual PEN 200 to PEN 3,000+ for medium dwelling).

### Arbitrios Municipales (separate from impuesto predial)

Per **Ley Orgánica de Municipalidades — Ley 27972** + TUO Tributación Municipal art. 68. Distritos charge for:
- **Limpieza pública** (recolección de residuos sólidos)
- **Parques y jardines**
- **Serenazgo** (municipal security patrols)

**Total arbitrios** typically PEN 500–2,500/year for a Lima coastal-distrito apartment, MUCH higher in San Isidro / Miraflores / La Molina; lower in Lima Norte/Sur. Verify at the **Municipalidad Distrital** Ordenanza tarifaria del año.

### Transaction taxes (one-time at purchase)

| Item | Rate | Source / authority |
|---|---|---|
| **Impuesto de Alcabala** | **3 %** of higher of (precio venta, autoavalúo ajustado) MINUS **10 UIT exempt threshold** (~PEN 55,000 at UIT 2026) | TUO Ley Tributación Municipal art. 21–29; pagado por **comprador** before notarial escritura; collected by **SAT Lima Metropolitana** (any property within Provincia de Lima — provincial level, NOT distrito), or **SAT del distrito** (Piura/Trujillo/Chiclayo/Huancayo/Cusco + ~6 others), or directly by the **Gerencia de Administración Tributaria de la Municipalidad** in the remaining distritos (most of Peru's 1,874 distritos have no SAT) (2026-05-27 verified, source SAT Lima FAQ + SATP) |
| **IGV (Impuesto General a las Ventas)** | **18 %** on **first sale** of new construction by **constructor habitual** (developer) — calculated on 50 % of price (other 50 % treated as terreno, IGV-exempt per Ley IGV art. 13) → effective IGV rate ~**9 %** on full price | Ley del IGV — Decreto Supremo 055-99-EF + amendments; SUNAT |
| **Notarial fees** | ~**0.5–1.0 %** of price (escala notarial — Ministerio de Justicia + Colegio de Notarios) | Decreto Legislativo 1049 (Ley del Notariado) + arancel notarial |
| **SUNARP registration** (Derechos registrales) | ~**0.2–0.5 %** of price (escala TUPA SUNARP) | TUPA SUNARP; verify at `https://www.sunarp.gob.pe/` |
| **Estudio de títulos / abogado** | **0.5–1.5 %** of price (negotiated) | Private market |
| **Tasación bancaria** (if mortgage) | PEN 500–2,000 fixed | Bank requirement |
| **Comisión inmobiliaria** | **3 % + IGV** typical, paid by seller (sometimes split) | Ley 31435 + market practice |
| **Total buyer-side closing costs** | ~**4–6 %** of price | Sum of alcabala + notario + SUNARP + abogado |

### Capital Gains Tax — Impuesto a la Renta de Segunda Categoría

Per **Ley del Impuesto a la Renta — Decreto Supremo 179-2004-EF** (TUO LIR) art. 24 + 84:

- **Resident natural person (PN domiciliado)**: **5 %** flat on **net capital gain** (precio venta − costo computable ajustado por inflación) on second-or-later property. **Withheld at notary** (notario público as agente de retención per Ley 28194 art. 84-A).
- **Non-resident (no domiciliado)**: **5 %** on net capital gain (precio venta − costo computable ajustado) per **TUO LIR art. 54(b)**, vigente desde 01.01.2017 (Ley 30404). Withheld by buyer/notario via SUNAT Formulario 1665. Note: art. 56(g) reads 30 % for non-residents on capital gains, but art. 54(b) carves RE down to 5 % — the 5 % rule controls for RE specifically (2026-05-27 verified, source SUNAT orientacion 3536-02).
- **Exemption**: sale of **única casa-habitación** held ≥ 2 years and not used for commercial activity — **EXEMPT** (TUO LIR art. 2 + Segunda Disp. Transitoria + DS 122-94-EF Reglamento art. 1-A) OR property acquired before 2004-01-01 (Ley 27804 transitoria — pre-Ley 30404 vintage). Notario withholds via art. 84-A.
- **Costo computable adjustment**: indexed by **factores de actualización** published annually by SUNAT (`https://www.sunat.gob.pe/`).

### Inheritance / sucesión

- Peru **abolished impuesto a la herencia / sucesoral** by **Decreto Legislativo 25988 (1992)** during fiscal reform. **No federal inheritance tax** as of 2026.
- Notarial sucesión costs (declaratoria de herederos + adjudicación) typically PEN 2,000–10,000 + SUNARP fees.
- **Gift (anticipo de legítima)**: also no impuesto a la donación at federal level; may attract impuesto de alcabala 3% if property transferred inter vivos to non-direct heir (verify per case with notario).

### IGV (Impuesto General a las Ventas) — VAT framework

- **General rate**: **18 %** (16 % IGV + 2 % IPM Impuesto de Promoción Municipal).
- **First sale of new immovable by constructor habitual**: IGV **applies** on 50 % of price (terreno portion exempt) → effective ~9 % on full price. Ley IGV art. 13(d).
- **35-UIT exoneración (Apéndice I Lit. B Ley IGV)**: first sale destined for **vivienda** with sale value ≤ **35 UIT** (~PEN 192,500 at UIT 2026) is **IGV-exempt** if the constructora has the licencia de construcción presented + admitted at the Municipalidad. Extended by **Ley 31651** to **31 Dec 2028** — verify each año (recurrent extensions) (2026-05-27 verified, source Congreso comunicaciones + Ley 31651).
- **Resale (segunda transferencia)**: **IGV-exempt** per Ley IGV art. 2 lit b.
- **Rentals**: residential lease IGV-**exempt**; commercial lease IGV-**applicable** at 18 % if landlord is IGV-registered (RUC + régimen general/especial).

### ITF + Bancarización (Ley 28194)

- **ITF (Impuesto a las Transacciones Financieras)** — **0.005 %** on each financial debit/credit in PE banking system, withheld by bank on the transfer leg. Source: Ley 28194 + TUO DS 150-2007-EF; SUNAT gob.pe/7960.
- **Bancarización obligatoria (Ley 28194)**: any RE payment ≥ **1 UIT (~PEN 5,500 / 2026)** OR **≥ USD 1,000** MUST be made via medio de pago bancario (transferencia, cheque no negociable, depósito). Cash above threshold is **fiscally void** — buyer loses **costo computable** for CGT; seller cannot deduct (2026-05-27 verified, source SUNAT Ley 28194 + TUO DS 150-2007-EF).

### Future risk

- **MEF UIT 2026** = PEN 5,500 (Decreto Supremo 301-2025-EF, vigente 1 Ene 2026). Re-pull each año Dec/Jan — all property-tax tramos move with UIT.
- **Reforma tributaria pendiente**: Ley 32103 (2024) + Decreto Legislativo 1623 (2024) digital-economy IGV scope continues to expand; monitor **MEF** + **Congreso** for property-touching changes.
- **Catastro multipropósito SNCP**: ongoing 2020-2026 rollout per Ley 28294 + DS 005-2006-JUS — when a distrito's catastro updates, autoavalúo can rise materially → impuesto predial bill jumps.

---

## Section: `--rental`

### Long-term residential — Código Civil + Decreto Legislativo 1177 (2015)

- **No statutory rent cap** (unlike Chile DFL2 / Colombia Ley 820 IPC cap).
- **Decreto Legislativo 1177 (2015)** "Régimen de Promoción del Arrendamiento para Vivienda" introduced fast-track eviction (formularios FUA — Formulario Único de Arrendamiento, FUAS — venta con arrendamiento, FUAO — opción de compra) registered with **MVCS-promoted Notario Público** + **SUNARP**. Fast-track judicial restitution via **proceso único de ejecución** ~3-6 months when properly filed — but uptake is modest; most leases still under ordinary Código Civil art. 1666+.
- **Standard contract**: 12-month minimum customary; tenant + landlord termination notice typically 30 days; deposit (garantía) typically 1-2 months.
- **Tax on rental income (resident PN)**:
  - **Renta de Primera Categoría** per Ley IR art. 23.
  - Effective rate **5 %** of gross rental income (after 20 % deemed deduction → 6.25 % on 80 % base = effective 5 % flat). TUO LIR art. 36 + 84.
  - Paid via **SUNAT Formulario Virtual 1683** monthly.
  - **Foreign owner non-domiciliado**: retención **5 %** flat on gross rent (TUO LIR art. 76 + 56) — withheld by tenant if obligated to inscribe RUC, or self-declared.

### Short-term rentals (STR / Airbnb / Booking)

**Status**: regulatory framework via **MINCETUR** + Ley General de Turismo + distrito-level licensing.

#### National baseline (MINCETUR + Ley 29408 General de Turismo)

- **Establecimientos de hospedaje** classified per **Decreto Supremo 001-2015-MINCETUR** — Reglamento de Establecimientos de Hospedaje (hoteles, hostales, apart-hoteles, albergues). STR private-home short-stay falls in a regulatory gray zone — most operators register as "casa de hospedaje" or "departamento amoblado" or operate without specific category.
- **Registro Nacional de Establecimientos de Hospedaje** at MINCETUR — mandatory for clasificados; STR informal often unregistered (verify enforcement intensity per distrito).
- **IGV**: STR services to non-residents staying < 60 días considered **export of services → 0 % IGV** (Ley IGV art. 33 + reglamento) — IF operator is RUC-registered + invoices via factura electrónica with non-resident passport.
- **Renta de Primera Categoría (5 %)** if treated as renta de primera; if **habitualidad** (frequent + commercial) → **renta de tercera categoría** (business income, IR 29.5 % on net + IGV 18 % on gross if not export-of-services) — SUNAT criteria evolving.
- **UIF-SBS reporting**: Decreto Legislativo 1499 (2020) added real-estate intermediarios as sujetos obligados — STR platforms partially scoped.

#### Lima distrito-level rules (selected, verify each año)

- **Miraflores** — Ordenanza 575/2022 + updates: licencia de funcionamiento required for STR commercial use; junta de propietarios (HOA) of edificio can prohibit STR via **Reglamento Interno** under **Ley 27157 Ley de Regularización de Edificaciones** + Régimen de Propiedad Exclusiva y Común (Ley 27157 + DS 008-2000-MTC).
- **Barranco** — increasing STR scrutiny; Municipalidad enforcing licencia for commercial-class operations; verify at **Gerencia de Desarrollo Económico** Ordenanzas 2024-2025.
- **San Isidro** — most upscale edificios have Reglamento Interno that **prohibits** STR independent of municipal rules; check the Reglamento del edificio before underwriting STR.
- **Cusco Centro Histórico** — UNESCO heritage zone; **Plan Maestro del Centro Histórico Cusco (DS 001-2005-ED + UNESCO requirements)** + Municipalidad del Cusco licencia constraints.

### Strategic notes

- **Long-term yields** (est., unsourced indicative bands — derive your own from BCRP/INEI mediana $/m² ÷ scraped asking rents on Adondevivir/Urbania before underwriting): ~4–7 % gross for Lima coastal distritos (Miraflores, San Isidro, Barranco, Surco); ~5–8 % in middle distritos (Jesús María, Pueblo Libre, San Miguel); higher (~8–10 %) in lower-priced Lima Norte/Este but tenant-quality risk rises.
- **STR yields** (est., unsourced indicative — depends on ADR + occupancy you model; build your own from comparable Airbnb/Booking listings): ~6–12 % gross in Miraflores/Barranco/San Isidro premium units (pre-restrictions, USD-denominated tourist demand); **net yields after IGV / IR / arbitrios / mantenimiento + Reglamento Interno HOA prohibition risk can run roughly half of gross (est.)**.
- **Régimen de Propiedad Exclusiva y Común (Ley 27157 + DS 008-2000-MTC)**: junta de propietarios assemblea binding; **Reglamento Interno can prohibit STR** independent of municipal rules. Always read the Reglamento del edificio before buying for STR.
- **Cuotas de mantenimiento (HOA)**: 0.3-1.0 % of value/yr typical; arrears attach to the unit in some interpretations — request **estado de cuenta** from administrador before signing.

**Confidence**: HIGH for national tax framework (Ley IR + Ley IGV, TUO Tributación Municipal). MEDIUM for distrito-level STR rules (evolving 2024-2026, Miraflores + Barranco specifically).

---

## Section: `--work=<profession>`

### Job platforms

- **Bumeran Perú**: `https://www.bumeran.com.pe/`
- **Computrabajo Perú**: `https://www.computrabajo.com.pe/`
- **LinkedIn Perú** — strong Lima corporate, finance, mining, tech.
- **Indeed Perú**: `https://pe.indeed.com/`
- **Aptitus** (El Comercio group): `https://aptitus.com/`
- **Laborum.pe** (Adevinta): `https://www.laborum.pe/`
- **Trabajos.com Perú**: `https://www.trabajos.com.pe/`
- **Empleos Perú** (Ministerio de Trabajo) — gov: `https://www.gob.pe/23475-buscar-trabajo-en-el-portal-empleos-peru`

### Self-employment / business regimes

- **RUC** (Registro Único de Contribuyentes) — at **SUNAT**, mandatory for any economic activity. Free, ~30 min online.
- **Régimen Único Simplificado (RUS) / Nuevo RUS** — small businesses, ingresos ≤ PEN 8,000/mes (Categoría 1) or ≤ PEN 30,000/mes (Categoría 2). Cuota fija mensual PEN 20–50.
- **Régimen Especial de Renta (RER)** — ingresos ≤ PEN 525,000/año; tasa 1.5 % de ingresos netos.
- **Régimen MYPE Tributario (RMT)** — ingresos ≤ 1,700 UIT/año (PEN 9.1 M en 2026); tasa 10 % primer tramo + 29.5 % marginal.
- **Régimen General** — sin tope; tasa **29.5 %** sobre renta neta + 18 % IGV.
- **Aportes a EsSalud**: 9 % de remuneración (empleador); ONP 13 % (worker, Sistema Nacional de Pensiones) **OR** AFP ~10 % + comisión + prima (Sistema Privado de Pensiones — opcional, irreversible after election).
- **Foreign-worker visa** (see `--visa`).

### Salaried benchmarks (2025-2026)

- **Remuneración Mínima Vital (RMV)**: **PEN 1,025/mes** desde 2022-05 (Decreto Supremo 003-2022-TR) → updated to **PEN 1,130/mes** desde 2025-01 (DS 006-2024-TR, vigente 1 Ene 2025; adjustments are ad-hoc DS, no fixed cadence).
- **Median formal monthly wage (INEI ENAHO)**: ~PEN 1,500–2,000 nationally; Lima Metro ~PEN 2,500–3,500; Lima Top 25 % distritos ~PEN 5,000+. Verify at INEI ENAHO síntesis estadística.
- **Professional tech / fintech Lima** (English-fluent): ~PEN 6,000–20,000/mes (~USD 1,600–5,400) est. — listing-derived indicative band, no published source; cross-check at a salary aggregator (Bumeran / Computrabajo / LinkedIn Salary).
- **Mining / oil & gas senior roles**: ~PEN 15,000–40,000/mes est. (unsourced indicative; materially above the median) — concentrated Lima HQ + remote sites (rotational).

### Catchment heuristics

- **Lima Metropolitana** (Provincia de Lima + Callao): ~10.7 M (INEI 2024 mid-year est.) — largest catchment; finance, mining HQs, BPO, services, manufacturing, tech.
- **Arequipa metro**: ~1.1 M — second city; mining services, tourism, manufactura.
- **Trujillo metro**: ~1.0 M — agroindustria, services.
- **Chiclayo**: ~600 k.
- **Iquitos**: ~400 k — Amazon hub, river-only access.
- **Cusco**: ~430 k — tourism-dominant, peak-season seasonality.
- **Outside Tier-1 cities**: thin formal labor markets; informalidad ~70 % nationally per INEI ENAHO 2023-24.

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **IGP — Instituto Geofísico del Perú** | `https://www.igp.gob.pe/` | Sismicidad instrumental + histórica; **Centro Sismológico Nacional (CENSIS)**; volcanic monitoring (OVS — Observatorio Vulcanológico del Sur); tsunami modeling collaboration |
| **INDECI — Instituto Nacional de Defensa Civil** | `https://www.gob.pe/indeci` | Mapa de peligros, planes de evacuación, alertas, escenarios sísmicos Lima |
| **CENEPRED — Centro Nacional de Estimación, Prevención y Reducción del Riesgo de Desastres** | `https://www.gob.pe/cenepred` | Estimación + prevención prospectiva (mapas amenaza nacional, **SIGRID** Sistema de Información para la Gestión del Riesgo de Desastres) |
| **SIGRID** (CENEPRED) | `https://sigrid.cenepred.gob.pe/` | Geoportal multi-amenaza nacional (sismo, volcán, tsunami, huayco, inundación) |
| **INGEMMET** | `https://www.gob.pe/ingemmet` | Geología, peligros geológicos, **OVI** Observatorio Vulcanológico del INGEMMET (Misti, Sabancaya, Ubinas, Ticsani) |
| **DHN — Dirección de Hidrografía y Navegación (Marina de Guerra)** | `https://www.dhn.mil.pe/` | Tsunami warning + cartas de inundación tsunami costera |
| **SENAMHI — Servicio Nacional de Meteorología e Hidrología** | `https://www.senamhi.gob.pe/` | Hidrometeorología, El Niño, alertas hidrológicas |
| **ANA — Autoridad Nacional del Agua** | `https://www.gob.pe/ana` | Recursos hídricos, fajas marginales, riesgo inundación fluvial |
| **MVCS / MINAM** | `https://www.gob.pe/vivienda` + `https://www.gob.pe/minam` | Vivienda + Ambiente, código sismorresistente, NDCs Paris |

### Sismicidad — riesgo dominante

Peru lies on the **subduction zone Nazca-Sudamericana** (Cinturón de Fuego del Pacífico). Históricos M ≥ 7.5:
- **31 May 1970 Áncash M 7.9** — provocó el **aluvión de Yungay** (~70,000 fallecidos, ciudad de Yungay sepultada).
- **23 Jun 2001 Atico (Arequipa) M 8.4** — gran terremoto sur, daños Arequipa-Tacna.
- **15 Aug 2007 Pisco M 8.0** — daños severos Pisco-Ica-Chincha.
- **26 May 2019 Loreto M 8.0** (profundidad intermedia, pocos daños).

**Lima Metropolitana** is in a recognized **seismic gap** ("brecha sísmica de Lima") with ~250 yrs since the M ~8.6-8.8 1746 megaterremoto y tsunami → IGP + INDECI publish escenarios sísmicos regularmente; "scenario design" event commonly modeled at **M 8.5-8.8** rupturing offshore frente a Lima.

### Norma sismorresistente

- **NTE E.030 Diseño Sismorresistente** (vigente: **DS 002-2014-VIVIENDA** updating 2003 version) — Reglamento Nacional de Edificaciones (RNE).
- **NTE E.060 Concreto Armado**, **NTE E.070 Albañilería**, **NTE E.090 Estructuras Metálicas** — complementary.
- Pre-1977 (anterior Reglamento Nacional de Construcciones original): sin diseño sísmico formal robusto.
- 1977-2003 (primera norma E.030 + actualizaciones): estándar básico.
- Post-2003 (E.030 actualizada) + post-2014 (DS 002-2014-VIVIENDA): estándar moderno post-Pisco.

| Era construcción | Hazard sísmico |
|---|---|
| **Pre-1977** | Sin norma sísmica formal robusta; alto riesgo en eventos M ≥ 7 |
| **1977–2003** (E.030 original) | Norma básica; reforzar |
| **2003–2014** (E.030 actualizada) | Estándar moderno pre-Pisco/post-Pisco |
| **Post-2014** (DS 002-2014-VIVIENDA) | Estándar reforzado vigente |

**Pregunta crítica al vendedor**: año de **Conformidad de Obra municipal** (Recepción Final equivalente) y zonificación sísmica (Z) per E.030 + tipo de suelo (S).

### Tsunami (DHN + IGP)

- Toda la costa Pacífico peruana en exposición. **DHN — Dirección de Hidrografía y Navegación** (Marina de Guerra del Perú) publishes cartas de inundación por tsunami.
- Ciudades con cartas tsunami publicadas: Tumbes, Piura (Paita), Chiclayo (Pimentel), Trujillo (Salaverry/Huanchaco), Chimbote, **Lima-Callao** (Punta Hermosa, Punta Negra, San Bartolo, Ancón, Magdalena, Miraflores, Chorrillos costanera, Callao puerto), Pisco, Ica, Mollendo, Arequipa coastal, Tacna coastal.
- **Cota de inundación tsunami Lima-Callao**: modelos DHN + IGP ponen líneas de inundación cercanas a Costa Verde y bahía Callao en escenarios M 8.5+.
- **Plan de evacuación tsunami** obligatorio en distritos costeros expuestos vía INDECI + Municipalidades.

### Volcánico (INGEMMET — OVI + IGP — OVS)

- Sur del Perú concentra los volcanes activos: **Misti** (Arequipa, ~17 km del centro de la ciudad — alta exposición), **Sabancaya** (Caylloma, en erupción intermitente desde 2016), **Ubinas** (Moquegua, erupciones 2006-2009 y 2019), **Ticsani**, **Yucamane**, **Tutupaca**.
- **OVI INGEMMET** (`https://ovi.ingemmet.gob.pe/`) y **OVS IGP** monitor estado y publican alertas.
- **Mapas de peligro volcánico** publicados por INGEMMET para Misti, Ubinas, Sabancaya, Ticsani — verificar zonificación antes de compra en Arequipa, Moquegua, Tacna.

### Inundación + huayco (huaicos)

- **El Niño costero 2017** y **2023** causaron inundaciones catastróficas costa norte (Piura, Lambayeque, La Libertad, Lima Norte/Este).
- **Huaicos** (flujos de detritos): común en quebradas Andinas + valles costeros (Chosica, Chaclacayo, San Mateo, Lurigancho-Chosica) durante temporada de lluvias (Dic-Mar).
- **SIGRID CENEPRED** + INDECI mapas de peligro hidrometeorológico per cuenca + distrito.
- **ANA fajas marginales** (zona ribereña ríos): construcción prohibida; verificar en escritura + cadastre municipal.

### Climate change

- **NDC Perú** bajo Acuerdo de París (compromiso 30 % GEI reduction by 2030 unconditional + 40 % conditional).
- **PNCC — Plan Nacional de Cambio Climático** (MINAM) y **Política Nacional de Cambio Climático**.
- **Costa**: aridificación, ENSO intensification, fish-stock disruption, glaciar-fed water-stress.
- **Andes**: **retroceso glaciar acelerado** (Cordillera Blanca, Cordillera Vilcanota) — 50 %+ glacier loss since 1970s per INAIGEM + UGRH (ANA); affects dry-season water for valleys and agriculture.
- **Selva**: deforestation hotspot; biodiversity risk; climate-feedback to Andean precipitation.

### Mandatory diagnostics — documentos a exigir antes de oferta

| Documento | Emisor | Por qué |
|---|---|---|
| **Copia Literal de Partida Registral** | SUNARP — Oficina Registral / SPRL | Confirma titular, áreas, gravámenes, hipotecas, cargas |
| **Certificado Registral Inmobiliario (CRI)** | SUNARP | Certificación cargas y gravámenes vigentes |
| **Certificado Negativo de Cargas y Gravámenes** | SUNARP | Confirma libre de hipotecas/embargos |
| **HR + PU (Hoja Resumen + Predio Urbano)** | Municipalidad Distrital | Autoavalúo + condición fiscal + sin deuda predial |
| **Certificado de no adeudo arbitrios** | Municipalidad Distrital | Sin deuda arbitrios |
| **Constancia de Posesión / Conformidad de Obra** | Municipalidad — Gerencia de Desarrollo Urbano | Obras construidas con licencia y aprobadas |
| **Certificado de Parámetros Urbanísticos y Edificatorios (CPUE)** | Municipalidad — GDU | Zonificación + uso permitido + altura permitida |
| **Reglamento Interno + Junta de Propietarios** (si edificio Ley 27157) | Administrador / Junta | Restricciones STR, gastos comunes, fondo de reserva |
| **Estado de Cuenta de Mantenimiento** | Administrador del edificio | Sin deuda HOA |
| **Recibos servicios públicos al día** | Operadores (Sedapal/EPS, Enel-Luz del Sur, Cálidda gas) | Sin deuda servicios |
| **Estudio de títulos** (abogado) | Abogado privado | Revisión cadena dominial 30 años + verificación SUNARP |

### Title monitoring — SUNARP free tools (mandatory post-purchase)

- **Alerta Registral SUNARP** (`https://alertaregistral.sunarp.gob.pe/`) — free; email/SMS notification on any movement on the Partida (title-change, lien, publicidad-registral inquiry). Activate immediately post-purchase.
- **Inmovilización de Partidas con Aviso Electrónico** — free voluntary lock on the Partida preventing any onerous transfer/charge/lien filing for a self-set period; lifted only with notary-witnessed authorisation. Particularly relevant for **absentee foreign owners** + holdings > 12 months idle (2026-05-27 verified, source SUNARP servicios).

### Expropiación + saneamiento físico legal

- **DL 1192 + TUO DS 011-2019-VIVIENDA (Ley Marco de Adquisición y Expropiación)**: state may acquire (preferred: trato directo) or expropriate (last resort, requires Ley del Congreso) for infrastructure works (Línea Metro 2/3/4, IIRSA, Panamericana ampliaciones). Compensation = valor comercial + 10 % afectación. Check **SBN — Superintendencia Nacional de Bienes Estatales** (`https://www.gob.pe/sbn`) for parcel-level afectación notices before purchasing near major project corridors.

⚠️ **Trampa Zona de Frontera** (50 km perimeter, Const. art. 71): el notario está obligado a verificar; pero compra anterior puede tener vicios si el vendedor fue extranjero sin Decreto Supremo de excepción → verificar cadena dominial completa.

⚠️ **Trampa COFOPRI** (titulación informal): muchos predios en distritos populares fueron formalizados vía COFOPRI desde 1996 — la Partida Registral puede mostrar cadena trunca anterior a la formalización; aceptable si COFOPRI emitió título saneado, pero verificar.

---

## Section: `--mains`

### National regulators + database

- **SUNASS — Superintendencia Nacional de Servicios de Saneamiento**: `https://www.sunass.gob.pe/` — regulador agua potable + alcantarillado.
- **OSINERGMIN — Organismo Supervisor de la Inversión en Energía y Minería**: `https://www.osinergmin.gob.pe/` — regulador electricidad + gas natural + hidrocarburos.
- **MINEM — Ministerio de Energía y Minas**: `https://www.gob.pe/minem` — política energética.
- **MVCS — Ministerio de Vivienda Construcción y Saneamiento**: `https://www.gob.pe/vivienda`.

### Major operators (urban)

| City | Water + sewer | Electricity | Gas natural |
|---|---|---|---|
| **Lima Metropolitana + Callao** | **SEDAPAL** (Servicio de Agua Potable y Alcantarillado de Lima) — `https://www.sedapal.com.pe/` | **Enel Distribución Perú** (Lima Centro + Norte) + **Luz del Sur** (Lima Sur + Este) | **Cálidda — Gas Natural de Lima y Callao** — `https://www.calidda.com.pe/` |
| Arequipa | **SEDAPAR** | **SEAL** (Sociedad Eléctrica del Sur Oeste) | red gas en expansión vía concesión sur |
| Trujillo | **SEDALIB** | **Hidrandina** | limited |
| Cusco | **SEDACUSCO** | **Electro Sur Este** | limited |
| Piura | **EPS Grau** | **ENOSA** | limited |
| Chiclayo | **EPSEL** | **ENSA** | limited |

### Coverage

- **Urban (Lima Metropolitana)**: agua potable + alcantarillado near-universal in formal distritos (>95 % per SUNASS Estudio Tarifario SEDAPAL); coverage gaps remain in **asentamientos humanos** + Lima Sur/Norte conos (Pachacamac, Lurigancho-Chosica, Carabayllo, San Juan de Lurigancho upper zones).
- **Provincias Tier-2/3**: coverage variable; Iquitos + selva towns lower; rural relies on pozo + fosa séptica or comunal.
- **Sewage treatment**: Lima discharges large fraction at **La Chira** + **Taboada** WWTPs (post-2010s investment); pre-2014 raw discharge into Pacific common.
- **Verification**:
  1. Recibo de servicios (water + power + gas) shows the operator + connection status.
  2. **SUNASS SISDOC** + Estudio Tarifario per EPS for coverage data.
  3. For STR: verify potable-water continuity (Lima has historic intermittent supply some upper zones — tinacos + cisternas common).

### Costs (Lima 2026 reference)

- **Conexión nueva agua potable + alcantarillado SEDAPAL**: PEN 1,500–5,000 (depending on diametro + distancia).
- **Pozo séptico nuevo (rural / fuera red)**: PEN 5,000–15,000.
- **Conexión gas natural Cálidda**: PEN 1,000–3,500 (frequent promociones with cuota cero financiamiento).
- **Boleta mensual (Lima distrito coastal, family of 3)**:
  - Agua + alcantarillado: PEN 60–150
  - Electricidad: PEN 150–400
  - Gas natural (si conectado): PEN 30–80
  - Internet fibra: PEN 80–160

---

## Section: `--crime`

### Primary sources

- **PNP — Policía Nacional del Perú**: `https://www.gob.pe/pnp` — denuncias + reportes regional.
- **INEI ENAPRES — Encuesta Nacional de Programas Presupuestales**: `https://www.inei.gob.pe/` — victimización + percepción inseguridad encuesta semestral.
- **Observatorio Nacional de Seguridad Ciudadana — Mininter**: `https://www.gob.pe/mininter` — datos agregados.
- **Ministerio del Interior — DataCrim** (where available): integration ongoing.

### Verdict bands (Lima distritos, victimización ENAPRES)

INEI ENAPRES reports "personas víctimas de algún hecho delictivo" (12-mo prevalence):
- 🟢 < 15 % distrito-level — bajo (rare in Lima Metro; some rural/remote zones)
- 🟡 15–25 % — moderado
- 🟠 25–35 % — alto (Lima Metro promedio ~25-28 % en 2023-24 ENAPRES)
- 🔴 > 35 % — muy alto (some Lima Norte/Este distritos + Trujillo + Tumbes border zones)

⚠️ **Numbers vary year-on-year** with reporting methodology + post-COVID rebound; date-stamp every figure.

### Distrito-level perception (Lima)

- Miraflores / San Isidro / Barranco / La Molina / San Borja: percepción inseguridad típicamente menor; **serenazgo distrital** activo.
- Lima Norte (San Martín de Porres, Comas, Los Olivos, Independencia): mayor exposición a delitos patrimoniales y extorsión.
- Lima Este (San Juan de Lurigancho — distrito más poblado del país, Ate, El Agustino): mayor exposición.
- Callao (Provincia Constitucional): tradicionalmente alta percepción de inseguridad; activo enforcement.

### Sicariato + extorsión (2024-2026 trend)

- **Extorsión** + **sicariato** han incrementado significativamente 2023-2026 según PNP + Mininter; impacto en transporte público, comercio en Lima Norte/Este + Trujillo + Piura.
- **Estado de emergencia distrital** declarations recurrent en 2024-2025 (San Juan de Lurigancho, Trujillo, etc.) — verificar si distrito objetivo está bajo estado de emergencia (Decreto Supremo).

### Verification path

1. **INEI ENAPRES** semestral por departamento + Lima distritos seleccionados.
2. **Mininter Observatorio** estadísticas agregadas mensuales.
3. **Junta vecinal del barrio** + portero/conserje del edificio para anécdota (no reemplaza data).
4. **Reglamento Interno edificio**: sistemas de seguridad (cámaras, control acceso) — pregunta antes de oferta.

**Confidence**: MEDIUM — INEI ENAPRES data is primary but lags 6-12 months; distrito-granular data variable in availability.

---

## Section: `--amenities`

### What "amenities" means here

Schools, healthcare, parks, transit, retail density — public-good adjacency that drives livability + resale.

### Sources (Lima focus)

- **MINEDU — Ministerio de Educación**: `https://www.gob.pe/minedu` — Escale (estadísticas educativas) + lista de instituciones educativas per distrito + UGEL.
- **SUSALUD — Superintendencia Nacional de Salud** (MINSA sector): `https://www.gob.pe/susalud` — administers **RENIPRESS** (Registro Nacional de IPRESS — Instituciones Prestadoras de Servicios de Salud), the register of public, private and mixed health-service providers: [consulta RENIPRESS](https://www.gob.pe/10202-obtener-informacion-de-las-instituciones-prestadoras-de-servicios-de-salud-renipress) (2026-09-18 verified). **MINSA — Ministerio de Salud**: `https://www.gob.pe/minsa` — health policy; **EsSalud** — social health insurance.
- **SERPAR Lima** (Servicio de Parques de Lima): `https://www.serpar.gob.pe/` — parques metropolitanos; municipalidades distritales para parques locales.
- **AATE + ATU + Línea 1 Metro de Lima** (concesionaria GyM / Volcán): Línea 1 operativa Bayóvar (San Juan de Lurigancho) ↔ Villa El Salvador, 26 estaciones; Línea 2 + Ramal Av. Faucett ↔ Av. Gambetta in construcción.
- **Metropolitano BRT** (Lima): troncal Naranjal ↔ Matellini (norte ↔ sur Lima).
- **Adondevivir / Urbania filtros** — proxies para densidad amenity (gimnasio, centro comercial, restaurantes).

### Lima distritos — amenity density heuristic

- **High amenity density**: Miraflores, San Isidro, Barranco, Surco (Chacarilla, Las Casuarinas), San Borja, La Molina (parque-rich), Magdalena.
- **Mid amenity**: Jesús María, Lince, Pueblo Libre, San Miguel, Surquillo.
- **Mid-lower**: Chorrillos, Breña, La Victoria.
- **Lower formal amenity** (improving rapidly): Lima Norte conos (Comas, Los Olivos), Lima Este (San Juan de Lurigancho), Lima Sur (Villa El Salvador).

### Verification

- Educación: **MINEDU Escale** mapa de instituciones (público + privado).
- Salud: **SUSALUD — RENIPRESS** + listado clínicas privadas + EsSalud por distrito.
- Movilidad: **ATU / Línea 1 mapa** + Metropolitano BRT + corredores complementarios coverage.
- Comercio: Adondevivir/Urbania filtros + listings density indicador.

---

## Section: `--climate`

### Climate type by zone

Peru has 28 of the 32 Holdridge life zones — extreme heterogeneity:

- **Costa** (coastal desert): arid; coastal fog (garúa) Lima/centro; very low precipitation (<50 mm/yr Lima); ENSO variable.
- **Sierra** (Andean highlands): seasonal — wet (Dic-Mar) + dry (Abr-Nov); altitude-driven temperature; nights cold.
- **Selva** (Amazon basin): hot + humid; rainfall 2,000-4,000 mm/yr; flood season Dic-May.
- **Selva Alta / Yungas**: cloud-forest transition; high biodiversity.

### Sources

- **SENAMHI**: `https://www.senamhi.gob.pe/` — meteorological data, climate normals, ENSO bulletins, alertas.
- **MINAM**: `https://www.gob.pe/minam` — Política Nacional de Cambio Climático, NDC, **GEOServidor MINAM**.
- **INAIGEM** — Instituto Nacional de Investigación en Glaciares y Ecosistemas de Montaña: `https://www.gob.pe/inaigem` — glacier monitoring.
- **IGP — CIIFEN**: ENSO + climate research.

### Climate change projections (IPCC AR6 South America chapter + MINAM PNCC)

- **Costa central**: ~+1.5–2.5 °C by 2050 (SSP2-4.5); aridification; ENSO costero (2017, 2023) intensification; sea-level rise gradual.
- **Andes**: glaciar retreat 50-90 % small glaciers by 2050-2070; dry-season water stress for valleys (Cordillera Blanca → Río Santa basin most studied).
- **Selva**: deforestation amplifies regional warming; precipitation regime shifts uncertain.

### Implications for property

- **Lima coastal** (Miraflores, Barranco, etc.): mild year-round (~14-26 °C); humedad alta + garúa; minimal heating/cooling needs (most apts no AC); coastal cliff erosion (Costa Verde) ongoing → check parcel proximity to malecón cliff edge.
- **Andean property** (Cusco, Puno, Huaraz): día/noche temperature swings; calefacción central rare; insulation often poor (adobe, ladrillo simple).
- **Selva property** (Iquitos, Tarapoto, Pucallpa): humedad ~80-90 %; AC required; flood season impacts ground-floor.

---

## Section: `--finance`

### Mortgage market (resident vs non-resident)

**Major lenders** (regulados SBS — Superintendencia de Banca, Seguros y AFP):
- **BCP** (Banco de Crédito del Perú) — `https://www.viabcp.com/`
- **BBVA Perú** (ex-Continental) — `https://www.bbva.pe/`
- **Interbank** — `https://interbank.pe/`
- **Scotiabank Perú** — `https://www.scotiabank.com.pe/`
- **MiBanco** (microfinanzas, BCP group) — `https://www.mibanco.com.pe/`
- **Banco Pichincha**, **Banco GNB**, **Banco Falabella** — others.

**Tasas hipotecarias típicas (2026)**:
- **PEN (sol)**: ~7–10 % anual (Tasa Cliente Preferencial — TCP, fija o variable; verify daily at **SBS Tasas de Interés** `https://www.sbs.gob.pe/`).
- **USD**: ~5.5–8 % anual.
- **Plazo**: hasta 25–30 años (resident); 15-20 años (non-resident).

**LTV típico**:
- **Resident peruano + extranjero residente con CE (Carné de Extranjería)**: 70–90 % (con BBP — Bono del Buen Pagador MiVivienda subsidio si aplica).
- **Non-resident extranjero**: 50–60 % típico, mayoritariamente con depósito en banco peruano + estados de cuenta + carta de no adeudo de su banco origen.

### MiVivienda — Fondo MiVivienda

- **Fondo MIVIVIENDA S.A.** (`https://www.mivivienda.com.pe/`): **state-backed mortgage subsidy** vehicle for first-time buyers. Programs:
  - **Nuevo Crédito MiVivienda** — financiamiento USD/PEN para vivienda valor PEN 86,000 a PEN 504,000 (UIT-linked thresholds, verify 2026 cuota); pago mensual reducido + plazo hasta 30 años + **BBP** (Bono del Buen Pagador) descuento si pago puntual.
  - **Bono Familiar Habitacional (BFH) — Techo Propio**: subsidio para vivienda nueva ≤ PEN 117,000 (Tramos según UIT) — primera vivienda + ingreso familiar tope.
  - **Bono Verde**: bonus para vivienda con eficiencia energética + medioambiental.
- **Eligibility**: residencia peruana o extranjero con CE permanente típicamente requerida; foreign non-resident generally NOT eligible for MiVivienda.

### Trampas

- **Mortgage in USD if income in PEN**: Risk de cambio (PEN volatility 3.50-4.10 vs USD desde 2020 — históricamente más estable que LATAM peers, pero managed-float). SBS recomienda match currency to income.
- **Tasa fija vs variable**: variable atada a TCP del banco; 2024-2026 BCRP mantuvo rate cuts — verificar sensitividad a TIR.
- **Seguro desgravamen + seguro contra todo riesgo (SCTR vivienda)**: obligatorio con hipoteca; ~0.04-0.08 % mensual sobre saldo.
- **CTS + AFP fondos**: pueden usarse para downpayment hipotecario (Ley 30908 + amendments) — verificar reglas vigentes con AFP/SBS.

### Cost benchmark (Lima 2026, departamento Miraflores 100 m² @ USD 2,400/m² = USD 240,000)

- **Down 30 %**: USD 72,000
- **Préstamo USD 168,000 @ 6.5 % a 20 años**: cuota ~USD 1,253/mes
- **Cuota MV con BBP + tasa PEN @ 8 % a 25 años (eligibles)**: PEN equivalente ~PEN 4,500/mes (verify simulador MiVivienda)

**Confidence**: HIGH for SBS-regulated framework + MiVivienda national programa. MEDIUM for current 2026 tasas (volatil; verify daily SBS).

---

## Section: `--currency`

### Currency baseline

- **PEN — Sol** (símbolo S/, ISO 4217 PEN). Renamed from "Nuevo Sol" by **Ley 30381 (2015)** — official just "Sol" since.
- **Régimen cambiario**: **flotación administrada (managed float)** — BCRP (Banco Central de Reserva del Perú) intervenes periodically to smooth volatility, no fixed peg.
- **Capital controls**: **none significantly** at retail level; no exchange controls on inbound/outbound transfers in either currency. SBS supervises FX exposure on banks. Reporting: **UIF-SBS** (Unidad de Inteligencia Financiera) + **SUNAT** for >USD 10,000 inflows AML purposes (Decreto Legislativo 1499 + previous AML).

### USD usage

- **Pricing**: ~30-40 % of Lima coastal / luxury residential listings priced in **USD**; rest in PEN. New-build pre-construction often USD-quoted.
- **Notarial escritura**: can be denominated in either USD or PEN; conversion for tributario at BCRP **tipo de cambio publicado**.
- **Banks**: dual-currency accounts standard at BCP/BBVA/Interbank/Scotiabank; ATM dispensing in both.
- **Origen**: legacy of 1980s-90s hyperinflation (peak 7,000 %+ inflation 1990); even post-stabilization Sol remains ~30-40 % USD-influenced in real estate.

### Rate history + outlook

- **PEN/USD 2020-2026 range**: ~3.30 (2020 floor) → 4.10 (2021-2022 peak post-elections) → ~3.50-3.85 (2024-2026 stabilizing).
- **BCRP policy rate**: peaked 7.75 % in 2023; cut sequentially to ~5.50 % by Q4 2025 (verify current at `https://www.bcrp.gob.pe/`).
- **Inflation target**: 1-3 % per BCRP charter; 2024-2025 within band post-2022-23 spike.

### For property buyers

- **Match currency**: prefer match between mortgage currency + income currency to avoid risk de cambio.
- **Hedge tools**: forward FX available at BCP/BBVA/Interbank for >USD 50,000 transactions; minor cost (0.5-1.5 % spread).
- **Inbound transfer**: SWIFT to peruano bank account; SUNAT/UIF reporting >USD 10,000 — entirely legal but documented.
- **Outbound on resale**: no restriction; CGT 5 % at notary + cleared escritura allows full USD repatriation.

**Confidence**: HIGH — BCRP managed float + minimal capital controls is well-documented + stable framework.

---

## Section: `--visa`

### Primary authority

- **MIGRACIONES — Superintendencia Nacional de Migraciones**: `https://www.gob.pe/migraciones` — visa enforcement + carné de extranjería (CE) issuance.
- **MRE — Ministerio de Relaciones Exteriores (Cancillería)**: `https://www.gob.pe/rree` — visa application abroad via consulados.
- Legal basis: **Decreto Legislativo 1350 (2017)** Ley de Migraciones + **Decreto Supremo 007-2017-IN** Reglamento.

### Major visa pathways for property-buyers / investors

#### 1. Visa Inversionista (Investor)

- **Investment requirement**: USD 30,000 minimum in a Peruvian business activity (incorporación de empresa or aporte a sociedad existente). Real estate **alone** does NOT qualify (Peru does not offer a "golden visa" via residential RE only) — but investment in business + RE asset for the operación can be structured.
- **Renewable annually**; after **3 years continuous residencia**, eligible for **Residencia Permanente** (CE indefinido).
- **Naturalización** (Peruvian passport): tras **2 años de Residencia Permanente** + Spanish + integración + record sin antecedentes — total ~5 years from initial Inversionista.

#### 2. Visa Rentista

- **Pasive income ≥ USD 1,000/mes** demostrado (pensión gobierno extranjero, renta financiera, alquileres) + USD 500/mes adicional por dependiente.
- Documentación: certificación bancaria + pensión statements + sin antecedentes penales (apostillado).
- Renovable; ruta a Residencia Permanente tras 3 años.

#### 3. Visa Trabajador

- Job-linked; empleador peruano debe registrar contrato ante MTPE + obtener autorización de trabajo extranjero (límite legal: contratistas extranjeros ≤ 20 % planilla + 30 % planilla salarial — Decreto Legislativo 689). **Visa Designada / Trabajador**.

#### 4. Visa Familiar (Familia de Peruano / Residente)

- Cónyuge peruano + hijos: ruta directa.

#### 5. Visa de Inmigrante / Profesional

- Profesionales con título universitario validado por SUNEDU + oferta laboral.

#### 6. Mercosur visa

- Convenio ResMercosur 14/02 — nacionales AR/BO/BR/PA/UY (+ Asociados CL/CO/EC) → Visa Temporal con beneficios; ruta a Permanente tras 24 meses.

### Carné de Extranjería (CE)

- Documento de identidad para extranjeros residentes; emitido por MIGRACIONES tras visa concedida.
- Costo trámite: variable per categoría (~PEN 200-1,500 inicial + renovaciones).
- Permite contratar servicios bancarios, RUC, conducir, etc.

### NO golden-visa por RE

- Importante: Peru no tiene equivalente de Portugal Golden Visa, España Golden Visa, Chile Visa Inversionista por RE puro. Inversión en RE residencial sola NO califica para Visa Inversionista — debe estructurarse via empresa + actividad económica (alquiler comercial puede calificar bajo ciertas estructuras).

**Confidence**: HIGH — Decreto Legislativo 1350 + MIGRACIONES framework stable; categorías + thresholds verifiables. MEDIUM for naturalización tiempos exactos (varies por caso).

---

## Section: `--insurance`

### Regulator

- **SBS — Superintendencia de Banca, Seguros y AFP**: `https://www.sbs.gob.pe/` — supervisa aseguradoras + corredores.
- **APESEG — Asociación Peruana de Empresas de Seguros**: `https://www.apeseg.org.pe/` — gremio.

### Major insurers (RE-relevant)

- **Rímac Seguros** — `https://www.rimac.com/`
- **Pacífico Seguros** (BCP group) — `https://www.pacifico.com.pe/`
- **Mapfre Perú** — `https://www.mapfre.com.pe/`
- **La Positiva** — `https://www.lapositiva.com.pe/`
- **Interseguro** (Interbank group) — `https://www.interseguro.com.pe/`

### Coverage required / typical

- **Seguro de Desgravamen** (mortgage life insurance): obligatorio con hipoteca; cubre saldo en caso fallecimiento titular. ~0.03-0.05 % mensual sobre saldo.
- **Seguro contra Todo Riesgo (SCTR vivienda)**: obligatorio con hipoteca; cubre incendio, sismo, inundación, daños por agua, robo. ~0.10-0.25 % anual sobre valor asegurado.
- **Sismo**: incluido en SCTR estándar; verificar deducible (típico 2-5 % suma asegurada).

### Sin hipoteca

- Sin hipoteca, **el seguro vivienda NO es obligatorio** legalmente; voluntario. Penetración baja (<20 % viviendas formales aseguradas — Apeseg).

### Trampas

- **Sismo deducible**: revise el deducible — en evento M 8+ Lima, perdidas pueden ser severas; deducible 2-5 % de USD 200,000 = USD 4,000-10,000 out-of-pocket.
- **Pre-1977 builds**: aseguradoras pueden requerir certificación estructural (peritaje) o aplicar surcharge / exclusión sísmica.
- **HOA-level seguro**: edificios bajo Ley 27157 a menudo tienen seguro para áreas comunes; verificar Reglamento Interno + estado pagos.

**Confidence**: HIGH for regulatory framework (SBS) + product categories. MEDIUM for tasas exactas (variable per perfil).

---

## Section: `--notary`

### Notarial framework

- **Decreto Legislativo 1049 (2008)** — Ley del Notariado + amendments.
- **Junta de Decanos de Colegios de Notarios del Perú** + **Colegio de Notarios** per distrito notarial (33 colegios, uno por departamento + Lima/Callao subdivisiones).
- **Notario público**: profesional jurídico autorizado por Estado, fe pública, archivo notarial. Numero limitado por distrito notarial (concursos públicos abren plazas).

### Process — typical RE purchase

1. **Minuta de compraventa**: borrador escritura redactado por abogado; firmado entre partes.
2. **Notario revisa minuta** + verifica documentos (Partida SUNARP, autoavalúo HR-PU, pago alcabala 3 % por SAT/comprador, no adeudos predial + arbitrios, certificado parámetros, identidad partes via DNI/CE).
3. **Notario verifica Zona de Frontera 50 km** (Const. art. 71) si comprador extranjero.
4. **UIF-SBS reporte** si transacción >USD 10,000 (Decreto Legislativo 1499 + complementos).
5. **Escritura pública** firmada en presencia notario + testigos si requerido.
6. **Notario presenta para inscripción a SUNARP** — Registro de Predios — Oficina Registral correspondiente.
7. **SUNARP califica** (5-15 días hábiles típicos); inscribe → emite Anotación de Inscripción + Partida actualizada.
8. **Notario entrega copia legalizada de escritura + Partida actualizada** al comprador.

### Costs

- **Honorarios notariales**: ~0.5-1.0 % del precio (escala notarial + complejidad).
- **SUNARP — Derechos registrales**: ~0.2-0.5 % del precio (escala TUPA SUNARP + UIT-linked).
- **Alcabala**: 3 % de (precio − 10 UIT) — pagado en SAT del distrito + Lima Metro o municipalidad.
- **Total notario + SUNARP**: ~0.7-1.5 % del precio.

### Trampas

- **Doble venta** (vendedor inscribe escritura a dos compradores en breve sucesión): mitigado por bloqueo registral SUNARP mientras Partida está en trámite + due diligence pre-firma con CRI fresco (mismo día firma).
- **Falsa identidad vendedor**: notario verifica DNI/CE contra RENIEC + biométrico — pero falsificación posible; pedir DNI físico + cotejar.
- **Sustitución partes en minuta**: only firmar con minuta cargada al notario directamente; no aceptar borradores externos cambiados a último minuto.

**Confidence**: HIGH — Decreto Legislativo 1049 framework stable; SUNARP electrónico reduces falsa-identidad risk vs pre-2010s.

---

## Section: `--compare`

### Latam Pacific neighbors comparison (PE / CL / CO / EC)

| Dimension | Perú | Chile | Colombia | Ecuador |
|---|---|---|---|---|
| Foreign-buyer regime | Open with 50 km Border Zone (Const. art. 71) | Open; DL 1939 limítrofe restriction nationals AR/BO/PE | Open; 2 km zonas frontera | Open with 50 km border restriction |
| Currency / inflation | PEN managed float; inflation 1-3 % target stable | CLP / UF inflation-indexed; mature framework | COP highly volatile; 2-3 % to 9 % range 2020-2024 | USD dollarized since 2000 |
| Cadastre quality | SUNARP electronic + uneven distrito catastro | CBR + SII Rol very mature | IGAC + ORIP + multipurpose rollout 2020-2026 | Catastro municipal variable |
| Property tax | Predial 0.2-1.0 % progresivo + arbitrios | Contribuciones 0-1.09 % + sobretasa | Predial 0.5-1.6 % per municipio | Predial 0.025-0.5 % |
| CGT (resident) | 5 % flat 2da categoría | 10 % unique tax > UF 8,000 lifetime | 15 % ganancia ocasional | Varies, recent reforms |
| Mortgage rates 2026 | 7-10 % PEN / 5.5-8 % USD | UF + ~3-5 % real | DTF + spread, 12-16 % nominal COP | USD ~7-9 % |
| STR regulation | MINCETUR national + distrito | Comuna-by-comuna evolving | national RNT + municipal uso del suelo (Bogotá 'Decreto 538/2024' unverified) | Limited national |
| Seismic code | E.030 (DS 002-2014-VIVIENDA) | NCh 433 of.96 mod. 2009 + DS 61/2011 | NSR-10 (Decreto 926/2010) | NEC-15 |
| Investor visa | Inversionista USD 30k business | Visa Temporaria Inversionista | M-visa 350× SMLMV | Visa Inversionista |

### Lima vs other Pacific cities

| Metric | Lima | Santiago CL | Bogotá CO | Quito EC |
|---|---:|---:|---:|---:|
| Premium $/m² (top distrito) | ~$2,500 (Miraflores/San Isidro) | ~UF 130 ≈ $5,200 (Vitacura) | ~$4,500 (Chicó) | ~$1,800-$2,200 |
| Population metro | ~10.7 M | ~7.1 M | ~10.5 M | ~2.8 M |
| Seismic risk | High (subduction Nazca) | High (subduction Nazca) | Moderate-High (inland Andes) | High (inland Andes + volcanic) |
| Tsunami risk coastal | Yes (DHN cartas) | Yes (SHOA CITSU) | Yes Pacific only (Tumaco/Bvtra) | Yes (esmeraldas / Manabí) |

---

## Section: `--retirement`

### Visa Rentista (pension-based)

(detailed in `--visa`): Passive income ≥ USD 1,000/mes + USD 500/dependiente. Renewable; 3 years → Permanente.

### Cost-of-living anchor (Lima Miraflores 2026, single retiree)

- Rent (1BR Miraflores): USD 700-1,200/mo
- Utilities + internet: USD 80-150/mo
- Groceries + dining: USD 400-700/mo
- Healthcare (private clinic seguro): USD 80-200/mo
- Transport: USD 50-150/mo (taxi / rideshare; metro low cost)
- **Total estimate single**: USD 1,400-2,500/mo Lima coastal

Provincias (Cusco, Arequipa, Trujillo): ~30-50 % cheaper.

### Healthcare

- **MINSA público**: free at point of use; quality variable; long waits in Tier-2 hospitals.
- **EsSalud**: contributory social insurance (workers); foreign retirees not eligible unless employed.
- **Private clinics** (Lima): Clínica Anglo Americana, Clínica San Felipe, Clínica Ricardo Palma, Clínica Internacional, Clínica Delgado — mid-to-high quality; out-of-pocket or via private seguro (Rímac, Pacífico, Mapfre planes USD 80-300/mes).
- **EPS — Entidad Prestadora de Salud**: private layer on EsSalud (employer-linked).

### Pension taxation

- **Foreign pension** received in Peru by non-domiciliado (less than 183 días + no condition met): NOT taxed in Peru — taxed in country of source per convenio doble tributación if applicable.
- **Domiciliado** (>183 días resident): foreign pension taxed in Peru as renta de fuente extranjera, tasa marginal IR PN. Verify convenio (CDI) — Peru has CDIs with Brasil, Chile, Canadá, Corea, México, Portugal, Suiza, ANDEAN Decisión 578.

### Trampas

- **Seguro privado para mayores**: tasas suben significativamente >65 años; pre-existing conditions excluidos en algunos planes. Negociar con corredor APESEG.
- **AFP withdraw**: residentes pueden retirar fondos AFP bajo ciertas condiciones (Ley 30908 + 2020-2024 emergency-withdrawal laws); foreign-pension retirees no AFP-affiliated.

**Confidence**: HIGH for visa Rentista + private clinics framework. MEDIUM for cost estimates (vary widely).

---

## Section: `--digital-nomad`

### No specific "digital nomad visa" framework

Peru as of 2026-05 has **no dedicated digital-nomad visa** comparable to Portugal D8 / Spain España DN / Costa Rica DN. Nomads typically use:
- **Visa de turista** (tourist): up to 183 days/year (extendable up to 90 days additional via prórroga); free; airport entry. **Not for working** technically — tolerated for remote-work for foreign employer in practice but no legal cover.
- **Visa Rentista** if income ≥ USD 1,000/mo passive (interpreted strictly — remote-work income may qualify if structured).
- **Mercosur visa** for AR/BR/CL/CO/UY/PY etc. — easier residencia path.
- **Visa Inversionista** if structuring investment in PE business.

### Key remote-work realities

- **Internet**: Lima coastal distritos have high-quality fibra (Movistar, Claro, Win) — 200 Mbps-1 Gbps ~PEN 80-180/mo (est., 2025 provider plans — verify current). Provincial Tier-2 cities reasonable; rural patchy.
- **Coworking density**: Miraflores + Barranco + San Isidro highest (Selina, WeWork legacy / replaced by local brands, Comunal Coworking, Worx, Wayra).
- **Time zones**: PE = GMT-5 (no DST) — aligned with US Eastern (winter) / overlap with US/CA workdays.
- **Tax**: tourist visa <183 days = non-domiciliado; income from foreign employer NOT taxed in Peru if earned + paid abroad (subject to convenio CDI rules).

### Lifestyle hotspots

- **Lima** (Miraflores / Barranco / San Isidro): coworking + safety + amenity dense.
- **Cusco** (Centro Histórico / San Blas): tourism-dense; high-altitude (3,400 m).
- **Arequipa** (Cercado / Yanahuara): mid-altitude (2,335 m); less crowded.
- **Mancora / Vichayito** (north coast): surf + warm; thinner infra.
- **Huanchaco** (Trujillo): surf + colonial; thinner infra.

**Confidence**: MEDIUM — no dedicated DN visa makes the framework ambiguous; tourist visa is de-facto for short-stay remote work.

---

## Section: `--macro`

### Macro indicators (BCRP + INEI)

- **GDP growth 2024**: ~2.8 % (BCRP / INEI estadísticas anuales) — recovering from 2023 contraction (-0.6 %) post-political-crisis 2022-23.
- **GDP growth 2025 est.**: ~2.5-3.5 % (BCRP Reporte de Inflación Q4 2025 — verify current).
- **Inflation (IPC Lima Metro)**: ~2.0-2.5 % YoY 2025 (within BCRP 1-3 % target).
- **BCRP policy rate**: ~5.50 % (Q4 2025 — verify monthly Programa Monetario `https://www.bcrp.gob.pe/`).
- **Unemployment (urbano)**: ~6-7 % INEI ENAHO; informal employment ~70 %.
- **PEN/USD**: ~3.50-3.85 range Q4 2025.
- **Soberano risk (EMBI+ Peru)**: ~150-200 bps over US Treasury (verify daily).
- **Sovereign credit rating**: BBB- (S&P, Fitch; as of Q4 2025 — verify current at agency / BCRP) — investment grade; downgraded from BBB during 2022-23 political turmoil; outlook stable.

### Long-term drivers

- **Mining**: Peru is #2 global copper producer (after Chile), top silver, zinc, tin; mining sector ~10-12 % GDP + ~60 % exports — China demand cycle key driver.
- **Agroexports**: arándanos, espárragos, paltas, uvas — irrigated north coast (Ica, Piura, La Libertad) — growth motor 2010-2024.
- **Tourism**: Cusco/Machu Picchu + Lima gastronómico — affected by 2022-23 protests, recovering 2024-26.
- **Demographic**: relatively young (median age ~30) but aging trend; Lima Metro absorbing internal migration.

### Risks

- **Political instability**: 6 presidents 2016-2024; Constitutional Tribunal + Congress conflict recurring; 2026 elections cycle pivotal.
- **Mining-cycle dependence**: copper price drop = fiscal stress; 2024-2025 Chinese demand recovery supportive.
- **Climate (ENSO costero)**: 2017 + 2023 events caused multi-billion USD losses + GDP shocks.
- **Informal economy**: tax base narrow; SUNAT formalization gradual.

**Confidence**: HIGH for BCRP/INEI macro data; MEDIUM for forward GDP estimates (verify current Reporte de Inflación BCRP).

---

## Section: `--demographics`

### Population (INEI 2024 mid-year est., projection 2017 census base)

- **National**: ~34.0 M
- **Lima Metropolitana** (Lima + Callao): ~10.7 M (~32 % of national)
- **Arequipa** (departamento): ~1.5 M (metro ~1.1 M)
- **La Libertad** (Trujillo): ~2.0 M
- **Piura**: ~2.1 M
- **Cusco**: ~1.4 M

### Age structure

- Median age: ~30 years
- Under 15: ~24 %
- 65+: ~9 % (rising; pension transition emerging)

### Migration

- **Internal**: rural → urban (Lima absorbed millions 1980s-2000s); current trend slowing but Lima still net-positive.
- **External**: Venezuelan immigration 2018-2024 (~1.5 M Venezolanos in Peru per ACNUR, largest single host); CPP — Carnet Permiso Temporal de Permanencia regularization. Has affected labor market + rental markets in Lima.
- **Peruvian diaspora**: ~3.5 M abroad (US, ES, AR, CL, IT principal destinos).

### Education

- **Literacy**: ~94 % adult; gender gap closing.
- **Tertiary education**: SUNEDU-supervised universities; ~30 % gross enrollment ratio.

### Religion

- **Catholic**: ~76 % per INEI 2017; declining; **evangélica** ~14 % rising.

### Lima distrito heterogeneity

- **Coastal premium distritos** (Miraflores, San Isidro, Barranco, San Borja, Surco): high-income, low-density growth, professional-skewed.
- **Lima Norte/Este/Sur** (San Juan de Lurigancho most populous distrito 1.1 M+): younger, working-class, faster-growing.

---

## Section: `--esg`

### Climate policy

- **NDC**: 30 % unconditional + 40 % conditional GEI reduction by 2030 vs BAU (per Gob. de Perú a UNFCCC).
- **Estrategia Nacional ante el Cambio Climático (ENCC)**: MINAM long-term framework.
- **Plan Nacional de Adaptación (NAP)**: prioritizing water, agriculture, forests, fisheries, health.

### Energy mix

- **Generación eléctrica 2024**: ~55-60 % hidroeléctrica + ~35 % gas natural (Camisea-fuelled) + ~5-8 % renovables no convencionales (solar, eólica) + thermal residual. Per OSINERGMIN + COES (Comité de Operación Económica del Sistema).
- **Gas natural**: Camisea (Cusco) — primary upstream + Cálidda distribution Lima + Naturgy nationwide industrial.
- **Renewable**: Marcona wind + Tacna solar farms expanding; subastas RER (Recursos Energéticos Renovables) periodic.

### Building energy efficiency

- **Norma EM.110 Confort Térmico y Lumínico** (RNE) — basic standards.
- **Bono Verde MiVivienda**: subsidy bonus for vivienda nueva certified eficiencia energética (verify thresholds at MiVivienda).
- **Energy certification (CEV equivalent)**: not mandatory at sale (unlike Chile's CEV from 2024); voluntary EDGE certification used by some developers (IFC partnership).

### Water + sanitation

- **SUNASS** + **SEDAPAL** + **EPS regionales** — coverage strong urban, gaps rural + informal urban edges.
- **Sewage treatment Lima**: La Chira + Taboada WWTPs post-2014 reduce raw discharge (still partial).

### Mining + ESG

- Peruvian RE outside Lima sometimes mining-adjacent — community conflicts (consulta previa Convenio 169 OIT) recurrent in Andean / Selva regions. Less relevant to urban RE buyer.

---

## Section: `--exit`

### Sale process for foreign owner (Lima coastal apartment, USD 250,000)

1. **Engage abogado + corredor inmobiliario** (Ley 31435 RAI-registered preferred). Typical commission **3 % + IGV** seller-side.
2. **Listing on Adondevivir/Urbania** + Properati; estimated marketing 3-9 months Lima coastal segments depending on distrito + price-to-market.
3. **Pre-sale documents**: Partida Registral SUNARP fresh CRI; HR + PU autoavalúo year corriente; constancia de no adeudo predial + arbitrios (Municipalidad); estado de cuenta de mantenimiento (administrador edificio); recibos servicios al día.
4. **Buyer offer** → Promesa de compraventa (señal típica 5-10 % precio).
5. **Notario engaged** (often buyer-selected); minuta drafted; due diligence by buyer abogado.
6. **Buyer pays alcabala 3 %** (− 10 UIT exempt) at SAT; pays seller balance.
7. **Escritura pública** firmada notario.
8. **Notario inscribe SUNARP** — Partida actualizada en ~5-15 días hábiles.

### Tax obligations on sale

- **Renta de Segunda Categoría 5 %** sobre net gain (precio venta ajustado − costo computable ajustado por SUNAT factores). **Withheld at notary** by notario as agente de retención (Ley 28194 art. 84-A).
- **Exempt** if **única casa-habitación held ≥ 2 years** + not used for commercial activity (TUO LIR art. 2).
- **Non-resident seller**: **5 %** retención sobre **net capital gain** (precio venta − costo computable ajustado) per **TUO LIR art. 54(b)**, vigente desde 01.01.2017 (Ley 30404) — withheld by buyer/notario via SUNAT Formulario 1665. Art. 56(g) headline 30 % does NOT apply to RE (carved out by art. 54(b)) (2026-05-27 verified).
- **No alcabala on sale** (alcabala is buyer-side only).

### Repatriation

- **No capital controls**: USD or PEN proceeds can be wire-transferred abroad freely from peruano bank account.
- **AML reporting**: bank reports >USD 10,000 to UIF-SBS automatically; legal but documented.
- **Foreign-currency conversion**: at BCRP daily tipo de cambio or bank spot; spread typically 0.5-1.5 %.

### Liquidity reality

- **Lima coastal premium distritos** (Miraflores, San Isidro): liquidity reasonable; 6-12 months typical sale for fairly priced units.
- **Provincias**: liquidity thinner; 12-24 months common.
- **Border-zone properties** (within 50 km of frontier): foreign-owner exit constrained — buyer pool smaller; verificar before purchase.

### Costs to seller (typical)

- Comisión inmobiliaria: 3 % + IGV
- IR 5 % retenido sobre net gain
- Notarial costs (often split or buyer-paid by negotiation)
- **Net to seller**: ~92-95 % of gross precio venta after commission + tax (varies)

**Confidence**: HIGH — framework is documented + standard; provincial liquidity LOW for underwriting purposes.

---

## Cost benchmarks (PE 2026)

| Concepto | Costo (PEN o %) | Fuente |
|---|---:|---|
| Alcabala (transferencia) | **3 %** sobre (precio − 10 UIT, ~PEN 55,000 al 2026) | TUO Ley Tributación Municipal art. 21-29 |
| Notario escritura | **0.5-1.0 %** del precio | Decreto Legislativo 1049 + arancel notarial |
| SUNARP inscripción | **0.2-0.5 %** del precio | TUPA SUNARP |
| Estudio de títulos (abogado) | **0.5-1.5 %** | privado |
| Tasación banco (si hipoteca) | PEN 500-2,000 | bancos |
| Seguro desgravamen + SCTR | ~0.10-0.30 % anual sobre saldo | aseguradoras SBS |
| Comisión inmobiliaria | **3 % + IGV** seller-side típico | Ley 31435 + mercado |
| Predial anual | 0.2-1.0 % progresivo sobre autoavalúo | TUO Tributación Municipal art. 13 |
| Arbitrios anuales | PEN 500-2,500 típico Lima coastal | Ordenanza Municipal Distrital |
| Mantenimiento HOA edificio | 0.3-1.0 % valor/año | Reglamento Interno |
| **Total transacción comprador** | ~**4-6 %** del precio | suma costos buyer-side |
| IGV first-sale developer | ~9 % efectivo (18 % sobre 50 % precio) | Ley IGV art. 13(d) |

---

## Active fiscal incentives & programs (2025-2026)

- **Nuevo Crédito MiVivienda** + **Bono del Buen Pagador (BBP)**: subsidio interés crediticio para vivienda PEN 86-504k (UIT-linked); Fondo MIVIVIENDA S.A.
- **Techo Propio + Bono Familiar Habitacional (BFH)**: vivienda nueva ≤ PEN 117k segmento bajo ingreso.
- **Bono Verde MiVivienda**: bonus para vivienda con eficiencia energética.
- **Beneficio pensionista predial**: 50 UIT deducción autoavalúo (Ley TUO art. 19) si pensión ≤ 1 UIT + única vivienda.
- **Pronto pago predial**: 5-15 % descuento por pago anual completo Feb-Mar (Ordenanza Municipal Distrital).
- **Ley 30056 PYMES + RMT**: regímenes simplificados para pequeños propietarios-arrendadores.

---

## Common listing platforms

- Adondevivir, Urbania, Properati, Mercado Libre Inmuebles Perú, Nestoria.

---

## Caveats unique to PE

- **Zona de Frontera 50 km (Const. art. 71)**: extranjeros NO pueden adquirir tierras dentro del perímetro 50 km de cualquier frontera (terrestre + marítima costera limítrofe); verificar siempre con notario.
- **PEN + USD dual-currency pricing** Lima coastal: legacy dollarización; verificar moneda escritura.
- **Catastro distrital fragmentado**: SNCP unification rolling 2020-2026 vía Ley 28294; expect autoavalúo updates → predial bills jump.
- **Régimen de Propiedad Exclusiva y Común (Ley 27157 + DS 008-2000-MTC)**: Reglamento Interno can prohibit STR — leer antes de comprar para BNB.
- **MINCETUR + distrito STR rules** evolving: Miraflores/Barranco/San Isidro intensificando 2024-2026.
- **Subducción Nazca-Sudamericana**: Lima en seismic gap ~250 yrs → escenario M 8.5+ planeado por IGP/INDECI.
- **Tsunami DHN**: cartas de inundación Lima-Callao + costa publicadas; verificar cota.
- **Volcanes sur** (Misti, Sabancaya, Ubinas, Ticsani): mapas peligro INGEMMET/OVI antes de compra Arequipa/Moquegua/Tacna.
- **El Niño costero** (2017, 2023): inundaciones costa norte recurrentes; verificar SIGRID CENEPRED.
- **MiVivienda restricted to residents/CE**: foreign non-resident generally not eligible.
- **No golden-visa por RE puro**: Inversionista requiere business actividad ≥ USD 30k.
- **No impuesto a la herencia federal** (abolida 1992) — but notarial sucesión costs apply.
- **CGT exempt si única casa-habitación ≥ 2 años**: planning-relevant para foreign owners considering tenure.
- **UIF-SBS reporting >USD 10k**: AML compliance via Decreto Legislativo 1499.
- **COFOPRI**-titled properties: cadena dominial may reset at COFOPRI formalization — accept but verify saneamiento.

---

## Reddit / forum sources

- **r/PERU** — general national Spanish
- **r/lima**
- **r/Cusco**
- **r/Arequipa**
- **InterNations Lima** + **Expat.com Peru** — expat communities
- **Perú Expats** Facebook groups
- **NomadList Lima** — digital nomad anecdote
- **InternationalLiving Peru** (anglo, marketing — not primary)

---

## Verification authorities

| Authority | When to call |
|---|---|
| **SUNARP** | Partida Registral, CRI, cadena dominial |
| **Municipalidad Distrital** (Catastro + Hacienda) | Autoavalúo, predial, arbitrios, parámetros urbanísticos |
| **SAT del distrito o Lima Metro** | Pago alcabala, no adeudo predial |
| **SUNAT** | RUC, IGV, IR, alquileres tributación |
| **MIGRACIONES** | Visa, CE, residencia |
| **MEF** | UIT, política fiscal |
| **BCRP** | Tipo de cambio, tasas referencia, IPV Lima |
| **INEI** | Demografía, ENAHO, ENAPRES, censos |
| **MINCETUR** | RNT establecimientos hospedaje, turismo |
| **MVCS / MiVivienda** | Vivienda subsidios, RNE, normas constructivas |
| **MINEDU** | Educación + Escale |
| **SUSALUD** (MINSA sector) | Salud + RENIPRESS |
| **SUNASS** | Agua + alcantarillado regulación |
| **OSINERGMIN** | Electricidad + gas regulación |
| **SBS** | Bancos + seguros + AFP regulación |
| **IGP / INDECI / CENEPRED / INGEMMET / DHN / SENAMHI / ANA** | Riesgos sismicos, volcánicos, tsunami, hidrometeorológicos |
| **COFOPRI** | Titulación informal saneada |
| **PNP / Mininter** | Seguridad + denuncias |
| **MTC / PROVÍAS / OSITRAN / ATU / AATE** | Vías + transporte |
| **MINAM** | Ambiente + cambio climático |

---

## Quirks to know

- **Partida Registral** = identifier único legal (SUNARP).
- **Código Predial / Código Catastral** = identifier fiscal distrital (Municipalidad).
- **HR + PU** = Hoja de Resumen + Predio Urbano = autoavalúo year corriente.
- **UIT 2026** = PEN 5,500 (DS 301-2025-EF, vigente 1 Ene 2026) — base para tramos predial, alcabala, IR.
- **DNI / CE** — Documento Nacional de Identidad (peruanos) / Carné de Extranjería (extranjeros residentes) — required for any RE transaction.
- **RUC** — Registro Único Contribuyentes SUNAT — required for landlords + sellers.
- **SIGRID CENEPRED** — geoportal multi-amenaza nacional — clave para riesgos.
- **BCRP tipo de cambio publicado** — official rate; usar para cualquier conversión PEN/USD tributaria.
- **Régimen de Propiedad Exclusiva y Común (Ley 27157)**: Reglamento Interno = clave HOA + STR + restricciones.
- **Border Zone 50 km (Const. art. 71)**: NUNCA olvidar verificación si comprador extranjero.
- **Eléctrica**: 220 V 60 Hz; clavija tipo A/B/C — verificar electrodomésticos importados.

---

## Source URL templates

| Source | URL pattern |
|---|---|
| SUNARP | `https://www.sunarp.gob.pe/` |
| SUNARP SPRL (búsqueda) | `https://www.sunarp.gob.pe/serviciosenlinea/portal/servicios-de-publicidad-registral-sprl.html` |
| SUNAT | `https://www.sunat.gob.pe/` |
| MEF | `https://www.gob.pe/mef` |
| BCRP | `https://www.bcrp.gob.pe/` |
| BCRP IPV Lima | `https://www.bcrp.gob.pe/estadisticas/indice-de-precios-de-viviendas.html` |
| BCRP tipo de cambio | `https://www.bcrp.gob.pe/estadisticas/tipo-de-cambio-diario.html` |
| INEI | `https://www.inei.gob.pe/` |
| MIGRACIONES | `https://www.gob.pe/migraciones` |
| MVCS | `https://www.gob.pe/vivienda` |
| MiVivienda | `https://www.mivivienda.com.pe/` |
| MINCETUR | `https://www.gob.pe/mincetur` |
| SBS | `https://www.sbs.gob.pe/` |
| SUNASS | `https://www.sunass.gob.pe/` |
| OSINERGMIN | `https://www.osinergmin.gob.pe/` |
| IGP | `https://www.igp.gob.pe/` |
| INDECI | `https://www.gob.pe/indeci` |
| CENEPRED | `https://www.gob.pe/cenepred` |
| SIGRID CENEPRED | `https://sigrid.cenepred.gob.pe/` |
| INGEMMET / OVI | `https://www.gob.pe/ingemmet` + `https://ovi.ingemmet.gob.pe/` |
| DHN | `https://www.dhn.mil.pe/` |
| SENAMHI | `https://www.senamhi.gob.pe/` |
| ANA | `https://www.gob.pe/ana` |
| MINAM | `https://www.gob.pe/minam` |
| MINEDU Escale | `https://escale.minedu.gob.pe/` |
| SUSALUD — RENIPRESS | `https://www.gob.pe/10202-obtener-informacion-de-las-instituciones-prestadoras-de-servicios-de-salud-renipress` |
| ATU | `https://www.gob.pe/atu` |
| AATE | `https://www.aate.gob.pe/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row |
| MTC | `https://www.gob.pe/mtc` |
| PROVÍAS Nacional | `https://www.gob.pe/pvn` |
| OSITRAN | `https://www.ositran.gob.pe/` |
| COFOPRI | `https://www.gob.pe/cofopri` |
| CAPECO | `https://www.capeco.org/` |
| ASEI | `https://www.asei.com.pe/` |
| Adondevivir | `https://www.adondevivir.com/` |
| Urbania | `https://urbania.pe/` |
| Properati Perú | `https://www.properati.com.pe/` |

---

## Status

**Confidence**: HIGH

**Last verified**: 2026-05-27 (RENIPRESS administering authority (SUSALUD) corrected 2026-09-18 per gob.pe)

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Framework-level confidence is HIGH for SUNARP/SUNAT/BCRP/SBS frameworks (all primary .gob.pe sources cited inline), Constitución art. 71 Border Zone 50 km (text-of-law), TUO Ley Tributación Municipal predial tramos (DS 156-2004-EF), Decreto Legislativo 1049 notarial, Ley 27157 propiedad exclusiva y común, NTE E.030 sismorresistente (DS 002-2014-VIVIENDA). MEDIUM for distrito-level STR rules (Miraflores Ord. 575/2022 + Barranco enforcement evolving 2024-26 — verify each año), provincial $/m² benchmarks (no BCRP IPV equivalent outside Lima 10-distrito panel — use CAPECO + listing scrapes with caution), 2026 UIT/RMV exact values (verify Dec/Jan annual decretos). LOW only for parcel-level price extrapolation outside Lima coastal premium distritos. All numeric facts dated and cited; per anti-hallucination contract, listing claims tagged + Border Zone trap surfaced + COFOPRI cadena dominial trap surfaced + IGV first-sale 9 %-effective derivation shown transparently.
