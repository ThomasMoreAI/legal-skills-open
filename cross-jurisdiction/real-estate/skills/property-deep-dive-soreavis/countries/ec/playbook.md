# Ecuador 🇪🇨 — Property Due-Diligence Playbook

ISO2: `ec`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode (Código Postal)**: 6 digits (DPA-coded), e.g. **170150** Quito centre, **090150** Guayaquil centro, **010150** Cuenca centro. first 2 digits = provincia, next 2 = cantón, last 2 = parroquia / sector. **Correos del Ecuador EP (CDE EP) is in liquidation**: Decreto Ejecutivo No. 1244 ordered its escisión and the transfer of the Servicio Postal Universal to **Servicios Postales del Ecuador (SPE EP)** — verify the current operator with [MINTEL](https://www.telecomunicaciones.gob.ec/comunicado-oficial-correos-del-ecuador) (source MINTEL official communiqué; 2026-09-18 verified). The DPA code structure itself is unaffected by the operator change
- **Admin levels**: 24 **provincias** → 221 **cantones** → ~1,500 **parroquias** (urbanas + rurales) → barrios / ciudadelas / recintos. Galápagos (provincia 20) governed under [Ley Orgánica de Régimen Especial de Galápagos (LOREG)](https://www.gob.ec/) — distinct land-tenure regime
- **Currency**: **USD (US dollar)** — dollarization adopted **9 January 2000** ([BCE — 25 años de dolarización](https://www.bce.fin.ec/25/index.html)); formalized by the Ley para la Transformación Económica del Ecuador (Ley Trolebús, Mar 2000), replacing sucre at 25,000:1 after the 1999 banking crisis. **Banco Central del Ecuador (BCE)** issues only **centavos** coins; USD banknotes are Federal Reserve issuance. **No FX risk for USD holders** — UNIQUE selling point in LATAM
- **Languages**: **Spanish** (official, [Constitución 2008 art. 2](https://www.gob.ec/)); **Kichwa** + **Shuar** co-official within their territories; English in Cuenca expat zones, tourist areas (Quito Mariscal, Guayaquil Las Peñas, Salinas, Manta, Galápagos)
- **Population**: ~17.7 M (2024 [INEC](https://www.ecuadorencifras.gob.ec/) mid-year est.) — Quito ~2.0 M (DMQ 2.8 M metro), Guayaquil ~2.7 M (3.4 M metro), Cuenca ~600 k, Santo Domingo ~470 k, Machala ~290 k, Manta ~270 k, Ambato ~200 k
- **Cadastre**: **Decentralized at municipal (cantón) level** — there is **NO single national cadastre**. Each **GAD Municipal** ([Gobiernos Autónomos Descentralizados](https://www.gob.ec/)) maintains its own *catastro urbano + rural*. Major cities expose web portals: [Catastro Quito (DMQ)](https://www.quito.gob.ec/), [Catastro Guayaquil](https://www.guayaquil.gob.ec/), [Catastro Cuenca](https://www.cuenca.gob.ec/). National coordination via **SENPLADES** (national planning) + GeoCatastro initiatives but no unified portal as of 2026
- **Land registry**: **Registro de la Propiedad** per cantón (separate from Catastro Municipal); supervised nationally by [DINARP — Dirección Nacional de Registros Públicos](https://www.gob.ec/dinarp) (formerly DINARDAP, Dirección Nacional de Registro de Datos Públicos) since the 2010 reform (2026 data, source gob.ec/dinarp; 2026-09-18 verified)
- **Identifier**: parcel-level **Clave Catastral** (per Municipio) + **Predio Number** + **Inscripción del Registro de la Propiedad** (legal title). Both required for clean diligence
- **Foreign-buyer regime** (CRITICAL): **OPEN** — Ecuador imposes no general prohibition on foreign ownership of residential/urban property; foreigners buy freely in Quito, Guayaquil, Cuenca, Manta, Salinas, Ambato, Loja core urban areas. **RESTRICTED zones**: [Constitución art. 405](https://votoenelexterior.cne.gob.ec/wp-content/uploads/2026/01/CONSTITUCION-DE-LA-REPUBLICA-DEL-ECUADOR.pdf) bars foreign natural/legal persons from acquiring land or concessions *"en las áreas de seguridad nacional ni en áreas protegidas"*, so the 50 km international-border strip + Galápagos + protected/national-security areas require prior **autorización de SECOB / Comando Conjunto de las Fuerzas Armadas** under [Ley de Seguridad Pública y del Estado](https://www.gob.ec/)

## Section: `--price`

### Primary sources

- **INEC — Índice de Precios de la Vivienda (IPV)** + **Índice de Precios al Consumidor (IPC)**: [`https://www.ecuadorencifras.gob.ec/`](https://www.ecuadorencifras.gob.ec/) — quarterly housing price index (national + Quito + Guayaquil + Cuenca)
- **BCE — Banco Central del Ecuador**: [`https://www.bce.fin.ec/`](https://www.bce.fin.ec/) — *Estadísticas del Sector Inmobiliario* + mortgage-stock series + construction GDP
- **CAMICON — Cámara de la Industria de la Construcción**: [`https://www.camicon.ec/`](https://www.camicon.ec/) — bi-annual *Boletín Inmobiliario* with Quito/Guayaquil/Cuenca asking-price benchmarks
- **MIDUVI — Ministerio de Desarrollo Urbano y Vivienda**: [`https://www.habitatyvivienda.gob.ec/`](https://www.habitatyvivienda.gob.ec/) — VIS (vivienda de interés social) + VIP (interés público) certified-housing prices
- **Catastro Municipal** (per cantón) — **avalúo catastral** as fiscal-tax base (typically 50–80% of comercial)

### Listing platforms

- **Plusvalía**: [`https://www.plusvalia.com/`](https://www.plusvalia.com/) — DOMINANT national portal (Navent group)
- **Properati Ecuador**: [`https://www.properati.com.ec/`](https://www.properati.com.ec/) — aggregator + price index
- **OLX Ecuador**: [`https://www.olx.com.ec/inmuebles_c367`](https://www.olx.com.ec/inmuebles_c367) ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — private sellers, mixed quality
- **Mercado Libre Ecuador Inmuebles**, **Vivanuncios.com.ec**, **Inmobiliaria.com.ec**
- **Engel & Völkers Ecuador**, **RE/MAX Ecuador**, **Coldwell Banker Ecuador** — premium / international
- ⚠️ Most listings tagged in **m² de construcción** (built area); confirm vs **m² útil** (usable / privative) on visit *(per listing — verify with cadastre / on visit)*

### Price benchmarks (2024-2025 IPV + listing scrape, est.)

| Zone | USD/m² resale (≈ 2026 est.) | Notes |
|---|---:|---|
| **Quito — Cumbayá / Tumbaco** (valle expat) | 1,400–2,400 | DMQ premium; embassies + expat |
| **Quito — La Carolina / González Suárez / La Floresta** | 1,300–2,200 | Centro-norte, mid-to-high |
| **Quito — Centro Histórico** (UNESCO) | 800–1,800 | Heritage constraints; mixed |
| **Quito — Sur (Solanda, Quitumbe)** | 600–1,100 | Working-class |
| **Guayaquil — Samborondón / La Puntilla** | 1,500–2,800 | Premier expat + financial |
| **Guayaquil — Urdesa / Kennedy / Los Ceibos** | 900–1,600 | Mid-tier traditional |
| **Guayaquil — Centro / Norte (centro)** | 700–1,400 | Mixed; security concerns 2024+ |
| **Cuenca — Centro Histórico** (UNESCO) | 1,000–2,000 | Expat hub; heritage |
| **Cuenca — Ordoñez Lasso / Challuabamba** | 800–1,500 | New-build expat ring |
| **Manta / Salinas / Olón** (coastal) | 1,000–2,500 | Beach; security 2024+ caveat |
| **Galápagos** (Santa Cruz / San Cristóbal) | 1,800–4,000+ | LOREG-restricted; thin market |
| **Loja / Ambato / Riobamba** (Sierra mid-tier) | 600–1,200 | Local-buyer market |

⚠️ **2024 price freeze signal**: nominal price growth has stalled or contracted in Guayaquil + coastal cantones (Manta, Esmeraldas, Durán) under the 2024 *internal armed conflict* security shock (Decreto Ejecutivo 110, Jan 2024). Quito + Cuenca more resilient. *Verify per-cantón at INEC IPV + CAMICON quarterly bulletins*. Treat the bands above as wide indicative ranges — every parcel needs the local Catastro Municipal *avalúo* + at least two agencias inmobiliarias.

### Compute

1. USD/m² = price / **superficie de construcción** (built area as registered at Catastro Municipal); confirm vs *área útil* on the *escritura pública*
2. Ecuador-specific premium drivers: **Sierra altitude + climate** (Quito 2,850 m, Cuenca 2,500 m — temperate, year-round spring), **expat clusters** (Cuenca + Cumbayá + Salinas + Vilcabamba), **gated/cerrada urbanizaciones** with private security
3. Discount drivers: **2024 security situation** (coastal Guayaquil + Esmeraldas + Manabí violent-crime spike); pre-1990 unreinforced builds in seismic zones; *avalúo catastral* well below comercial in some cantones (under-collected predial)

### Key terms

- IPV = Índice de Precios de la Vivienda (INEC) · IPC = Índice de Precios al Consumidor
- Escritura pública = notarized deed · Predio = parcel · Avalúo catastral = fiscal value
- VIS = Vivienda de Interés Social (subsidized) · VIP = Vivienda de Interés Público
- Alícuota = HOA fee (in régimen de propiedad horizontal)

---

## Section: `--traffic`

### Sources

- **Ministerio de Infraestructura y Tecnología (MIT)** — successor to MTOP: [`https://www.mit.gob.ec`](https://www.mit.gob.ec); road-network and public-works data run through **SITOP (Sistema de Información de Transporte y Obras Públicas)**. The *Inventario de la Red Vial Estatal* and TPDA counts are not published on the ministry's current homepage — data not publicly located; verify at MIT / SITOP (2026 data, source mit.gob.ec; 2026-09-18 verified)
- **ANT — Agencia Nacional de Tránsito**: [`https://www.ant.gob.ec/`](https://www.ant.gob.ec/) — vehicular registration + accident statistics
- **AMT — Agencia Metropolitana de Tránsito Quito**: [`https://www.amt.gob.ec/`](https://www.amt.gob.ec/) + **ATM Guayaquil** + **EMOV-EP Cuenca** — city aforos vehiculares + Pico y Placa schemes

### Key term

**TPDA (Tráfico Promedio Diario Anual)** = AADT-equivalent. Reported by MIT (ex-MTOP) for the *Red Vial Estatal* (E1–E50 corridors) — **the TPDA series is not published on the ministry's current site (2026-09-18); verify at MIT / SITOP** + by GAD Provincial for *vías secundarias*.

### Verdict bands

- 🟢 < 1,500 v/d (rural recintos, parroquia lanes, mountain spurs)
- 🟡 1,500–10,000 v/d (cabecera cantonal, suburban collector)
- 🟠 10,000–35,000 v/d (urban arterial — Av. 6 de Diciembre / Av. Naciones Unidas Quito; Av. 9 de Octubre / Av. Francisco de Orellana Guayaquil; Av. España / Av. Solano Cuenca)
- 🔴 > 35,000 v/d (autopistas + ring roads — Panamericana E35 Quito-Sur, Av. Simón Bolívar Quito perimetral, Vía a Daule Guayaquil, Av. de las Américas Guayaquil)

⚠️ **Pico y Placa** (license-plate restriction) operates in Quito (peak hours, since 2010) and Cuenca (2024 implementation); affects daily *patterns*, not annual totals. **Galápagos** has near-zero motorized traffic but strict vehicle quota under LOREG.

---

## Section: `--tax`

### Annual taxes (municipal — GAD)

- **Impuesto Predial Urbano** ([COOTAD — Código Orgánico de Organización Territorial, Autonomía y Descentralización](https://www.defensa.gob.ec/wp-content/uploads/downloads/2016/01/dic15_CODIGO-ORGANICO-DE-ORGANIZACION-TERRITORIAL-COOTAD.pdf) art. 504-512): progressive **0.25–5 ‰** (per mil) on *avalúo catastral*; each Municipio sets its own ordenanza tributaria within the COOTAD bands
- **Impuesto Predial Rural** (COOTAD art. 514-520): 0.25–3 ‰ on rural *avalúo*; lower than urban
- **Contribución Especial de Mejoras (CEM)**: levied when public works increase parcel value — varies per obra + cantón
- Verify exact rates at target [GAD Municipal Quito](https://www.quito.gob.ec/), [Guayaquil](https://www.guayaquil.gob.ec/), [Cuenca](https://www.cuenca.gob.ec/) tax portal

### Transaction taxes (one-time at purchase)

| Item | Rate | Source |
|---|---|---|
| **Alcabala** (municipal transfer tax) | **1 %** of escritura value | COOTAD art. 527-537; Municipio |
| **Notario** | fixed **múltiplos de SBU** per value bracket (arancel notarial, Resolución 005-2023): 0.20 SBU ≤ $10k → 5.00 SBU at $1M, capped 20 SBU + 0.001 excedente — ~0.2–1 % effective (est.; overstates at high value, ~0.24 % at $1M) | [Consejo de la Judicatura — Notarías](https://www.funcionjudicial.gob.ec/) (verify arancel) |
| **Registro de la Propiedad** | **0.2–0.5 %** of price (per cantón table) | DINARP / Registrador Cantonal |
| **Lawyer (abogado patrocinador)** | 0.5–1.5 % typical | Private market |
| **Total buyer-side closing cost** | **~2.5–4 %** of price | sum of above |

### IVA (Impuesto al Valor Agregado)

- **Standard 15 %** since **1 Apr 2024** (raised from 12 % under [Decreto Ejecutivo 198/2024](https://www.sri.gob.ec/impuesto-al-valor-agregado-iva) + [Ley Orgánica para Enfrentar el Conflicto Armado Interno](https://www.sri.gob.ec/impuesto-al-valor-agregado-iva), Mar 2024 — security funding) *(2026-07-11 verified, source SRI)*
- **Residential resale** → exempt from IVA (Alcabala instead)
- **New-build first sale** → **0 % IVA** if MIDUVI-certified VIS / VIP; otherwise **15 % IVA** applies on new-build first sale of non-VIS
- ⚠️ The 2024 IVA hike from 12 → 15 % (Decreto Ejecutivo 198/2024, eff 1 Apr 2024) was emergency-funding for the *internal armed conflict* declaration; not reverted: Decreto Ejecutivo 470 kept 15 % for 2025 and SRI Circular NAC-DGECCGC25-00000006 (26 Dec 2025) confirms 15 % stays in force until a new decree; LRTI art. 65 band is 13–15 %, so a decree can cut only to 13 % (2025 data, source SRI) — check for a new decree at [SRI — Servicio de Rentas Internas](https://www.sri.gob.ec/)

### Capital gains (Plusvalía / IR aplicable)

- **0 %** if held **>1 year** — UNIQUE LATAM exemption for natural persons selling habitual residence ([LRTI — Ley de Régimen Tributario Interno](https://www.sri.gob.ec/) art. 8 + reglamento, as amended by Ley Orgánica de Reforma Tributaria) *(2026-05-27 verified, source SRI + Ley Orgánica Reforma Tributaria)*
- **<1 year**: gain folded into ordinary IR (PIT) at progressive scale up to 37 % residents / **flat 25 % non-residents** on Ecuador-source
- **Plusvalía Municipal** (separate, COOTAD art. 556-561): up to **5 %** on price increase between sales — but **suspended/derogated** under reforms since 2018; verify current at target Municipio

### Income tax — IR (resident) / Retención (non-resident)

- **IR (resident)** 2026 (per [SRI tabla](https://www.sri.gob.ec/)) progressive: **0 %** up to ~USD 11,902 / **5 % → 37 %** top bracket above ~USD 100,000
- **IR (non-resident)**: flat **25 %** withholding on Ecuador-source income (incl. rental); some DTAs reduce
- **ISD — Impuesto a la Salida de Divisas**: **5 %** on outbound transfers ([Ley Reformatoria para la Equidad Tributaria 2007 + reforms](https://www.sri.gob.ec/)) — material for non-resident repatriation; certain exemptions for capital-import-traceable funds

### Wealth + inheritance

- **No annual wealth tax**
- **Impuesto a Herencias, Legados y Donaciones** (LRTI art. 36): progressive **0–35 %** above ~USD 80,000 base (verify 2026 brackets at SRI); spousal + direct-descendant exemptions partial

### Future risk

- **2024 IVA 15 %** (Decreto Ejecutivo 198/2024, raised from 12 %, eff 1 Apr 2024) kept for 2025 by Decreto Ejecutivo 470 and in force for 2026 per SRI Circular NAC-DGECCGC25-00000006 (26 Dec 2025); LRTI art. 65 band 13–15 %, so a decree can lower it only to 13 %, not 12 %
- Noboa government **2025–26 fiscal reforms** (pending Asamblea) — possible Alcabala / predial rebalancing + VIS-housing incentive expansion
- Galápagos LOREG amendments under review (residency + property restrictions tightening)

---

## Section: `--rental`

### Long-term residential

- **Ley de Inquilinato** ([codificación 2000 + reforms](https://www.gob.ec/)) — tenant-protective: 2-year minimum default term, indexation capped to *salario básico* movement or IPC, security deposit 1–2 months
- Rental income taxed within IR (resident progressive 0–37 %) / **25 % retención** non-resident (LRTI art. 39)

### Short-let (Airbnb / Booking)

- **MINTUR — Ministerio de Turismo** — STR licensing portal at [gob.ec](https://www.gob.ec/) (former turismo.gob.ec ❌ DEPRECATED — domain now misrouted to an unrelated agency) under [Decreto Ejecutivo 1411 (2020)](https://www.gob.ec/) + a **2023 STR reform** (decree/acuerdo number requires verification at the Registro Oficial — the previously cited "Decreto 803" is a 2020 economic decree, not the STR reform): mandatory **Registro de Catastro Turístico** + LUAF (Licencia Única Anual de Funcionamiento) per Municipio
- **Quito DMQ — Decreto Metropolitano 042-2020**: STR-specific rules + community-vote requirement in régimen de propiedad horizontal (similar to AD/CO trend)
- **Tasa turística** + **IVA 15 %** + **ICE** (servicios turísticos, where applicable)
- ⚠️ Pre-2020 informal Airbnb listings now non-compliant — request **Catastro Turístico número** + LUAF before any STR pricing model
- ⚠️ **Galápagos**: STR effectively closed to non-residents under LOREG; only certified residents may operate

### Rental yields (est., 2026)

- Long-term gross yield: Quito Cumbayá ~**5–7 %**, Guayaquil Samborondón ~**6–8 %**, Cuenca centro expat ~**4–6 %**
- Short-let gross yield (compliant tourist zones): Cuenca centro ~**7–11 %**, Salinas / Manta beach ~**6–10 %** (seasonality), Quito Mariscal ~**5–8 %**
- **Net drag**: predial low (typical < 0.3 % avalúo), HOA *alícuota* moderate, **2024 security overhang** depressing coastal occupancy materially

---

## Section: `--work=<profession>`

### Job platforms

- **Multitrabajos**: [`https://www.multitrabajos.com/`](https://www.multitrabajos.com/) — DOMINANT national portal
- **Computrabajo Ecuador**: [`https://www.computrabajo.com.ec/`](https://www.computrabajo.com.ec/)
- **Ministerio del Trabajo Red Socio Empleo**: [`https://www.trabajo.gob.ec/`](https://www.trabajo.gob.ec/) — public jobs portal
- **LinkedIn Ecuador** — strong in Quito + Guayaquil for tech, banking, BPO
- **OpcionEmpleo**, **Bumeran Ecuador**

### Foreign-worker permit

- **Visa de Trabajo (categoría profesional)** via [Ministerio de Relaciones Exteriores y Movilidad Humana — Cancillería](https://www.cancilleria.gob.ec/) under [Ley Orgánica de Movilidad Humana 2017](https://www.gob.ec/) — employer-sponsored; 2-year temporary residency renewable
- **Self-employment**: requires either Inversionista, Profesional, or Rentista visa (see `--visa`)

### Self-employment + entities

- **RUC — Registro Único de Contribuyentes** at [SRI](https://www.sri.gob.ec/) — mandatory for any economic activity; ~1 day online
- **RIMPE — Régimen Simplificado para Emprendedores y Negocios Populares** ([Ley de Desarrollo Económico 2021](https://www.sri.gob.ec/)) — single integrated tax for revenues < USD 300k (Emprendedor) / < USD 20k (Popular); rates 0–2 % on revenue
- **Régimen general**: standard IR (PIT/CIT 25 %) + IVA 15 % if applicable
- **IESS (Instituto Ecuatoriano de Seguridad Social)**: [`https://www.iess.gob.ec/documents/13718/54965/Tasasdeaportacion.pdf`](https://www.iess.gob.ec/) — mandatory; ~**11.15 % employer + 9.45 % worker** (employed); self-employed on declared base
- **Sociedades**: SAS (Sociedad por Acciones Simplificada, since 2020) most common for foreign-buyer property holding; min capital ~USD 1; corporate tax 25 % standard

### Salary benchmarks (2026)

- **Salario Básico Unificado (SBU)** **2026: USD 482/mes** (+USD 12 vs 2025's USD 470; set by tripartite consensus per [Ministerio del Trabajo](https://www.trabajo.gob.ec/despues-de-casi-una-decada-hay-consenso-gobierno-empleadores-y-trabajadores-acuerdan-fijar-el-salario-basico-unificado-de-2026-en-usd-482-no-hay-imposicion/), Dec 2025 — verify annual decree)
- Mean monthly formal wage Q4 2024 (per INEC ENEMDU): ~**USD 700–900**
- Quito banking / finance / tech: ~USD 1,500–4,000
- Guayaquil shipping / agroindustry / finance: ~USD 1,200–3,500
- BPO / English-fluent professionals (Quito + Cuenca hubs): ~USD 800–2,500
- **Informalidad** (unregistered work) ~**52 %** nationally per INEC ENEMDU 2024 — material headline drag

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SGR — Servicio Nacional de Gestión de Riesgos y Emergencias** | [`https://www.gestionderiesgos.gob.ec/`](https://www.gestionderiesgos.gob.ec/) | National risk plans, alertas, emergency declarations |
| **IGEPN — Instituto Geofísico EPN** | [`https://www.igepn.edu.ec/`](https://www.igepn.edu.ec/) | Seismic + volcanic monitoring (1 of LATAM's best-equipped) |
| **INAMHI — Instituto Nacional de Meteorología e Hidrología** | [`https://www.inamhi.gob.ec/`](https://www.inamhi.gob.ec/) | Hydromet, El Niño, flood forecasting |
| **INOCAR — Instituto Oceanográfico de la Armada** | [`https://www.inocar.mil.ec/`](https://www.inocar.mil.ec/) | Tsunami warning Pacific + Galápagos |
| **MAE / MAATE — Ministerio del Ambiente** | [`https://rncc.ambiente.gob.ec/`](https://rncc.ambiente.gob.ec/) (❌ `www.ambiente.gob.ec` DEPRECATED — 301s to an unrelated agency) | Wildfire, biodiversity, climate adaptation |
| **GAD Municipal — Plan de Uso y Gestión del Suelo (PUGS)** | per cantón | Hazard zoning at parcel level |

### Specific risks

- **Seismic** (PRINCIPAL): **Pacific Ring of Fire** — Nazca plate subducting beneath South American plate. **Subduction-zone megathrust** capable of M8+; historical M7.8 **Pedernales 16 Apr 2016** killed ≥676 (Manabí + Esmeraldas), 1797 Riobamba M8.3, 1906 Esmeraldas M8.8 (one of the largest ever recorded). [NEC-15 — Norma Ecuatoriana de la Construcción 2015](https://www.habitatyvivienda.gob.ec/) (❌ DEPRECATED — habitatyvivienda.gob.ec now redirects to an unrelated agency; verify NEC-15 at Registro Oficial / current housing authority) + amendments define design accelerations; *microzonificación sísmica* per major city (Quito, Guayaquil, Cuenca, Manta)
- **Volcanic**: ~**12 active volcanoes** monitored by IGEPN. Highest-risk inhabited: **Cotopaxi** (~50 km N of Quito; major ashfall + lahar exposure for valles Latacunga / Salcedo / Cumbayá / Chillos; in active phase 2024–2026, vigilance), **Tungurahua** (Baños evacuation history), **Reventador** (Quito ashfall events incl. 2002), **Sangay** (Sierra-Oriente boundary, near-continuous activity), **Pichincha** (Quito west; 1999 ashfall), **Sumaco**, **Antisana**, **Cayambe**
- **Tsunami**: full Pacific coast (Esmeraldas, Manabí, Santa Elena, Guayas, El Oro) + Galápagos; INOCAR tsunami-warning system. Coastal evacuation routes mapped post-2016
- **Flooding (inundación)**: catastrophic during **El Niño** events (2023 + 2024 coastal floods, 1997-98 historical); **Andean rivers** flash-flood; Guayas basin lowlands recurring
- **Landslides (deslizamientos / movimientos en masa)**: ubiquitous Andean Sierra; Quito's Pichincha slopes (laderas) have major slide history (La Comuna, La Gasca + 2022 Quito slide event); also Cuenca + Loja steep parcels
- **Crime + security** (CRITICAL 2024–2026 context): **Decreto Ejecutivo 110 (8 Jan 2024)** declared the **estado de excepción** for grave conmoción interna — it was **Decreto Ejecutivo 111 (9 Jan 2024)** that amended 110 to recognise the **internal armed conflict (conflicto armado interno)** against narco-gangs ("grupos delictivos organizados — GDO"): *"Refórmese el Decreto Ejecutivo No. 110 de 08 de enero de 2024, al reconocer la existencia de un conflicto armado interno"* ([Suplemento al Registro Oficial No. 474, 10 Jan 2024](https://www.registroficial.gob.ec/suplemento-al-registro-oficial-no-474)). From Apr 2024 the states of exception instead cite **Decreto Ejecutivo 218 of 7 Apr 2024** as the decree contemplating the conflicto armado interno ([Sexto Suplemento al Registro Oficial No. 716](https://www.registroficial.gob.ec/sexto-suplemento-al-registro-oficial-no-716)) — cite **111** for the January 2024 declaration, **218** for anything dated after 7 Apr 2024. Acute violent-crime spikes in **Guayaquil**, **Esmeraldas**, **Manta**, **Quevedo**, **Durán**, **Machala**; comparatively safer: Cuenca, Quito (most barrios), Loja, sierra centro. **Plan Fénix** (not "Plan Phoenix") + military-police joint operations ongoing; situation evolving — *verify current state* at [Ministerio del Interior — Noticias](https://www.ministeriodelinterior.gob.ec/category/noticias/) + travel advisories (US Dept of State, UK FCDO) before any coastal purchase. The Plan Fénix page cited here previously is [Boletín N° 006 of 13 Dec 2023](https://www.ministeriodelinterior.gob.ec/plan-fenix-se-ejecuta-en-el-ecuador/) — it predates both decrees and is not a current-state source (2026-08-08 re-verified against registroficial.gob.ec)
- **Climate change** (per [INAMHI](https://www.inamhi.gob.ec/) + IPCC AR6): +1.5–3.0 °C by 2100; intensifying El Niño / La Niña amplitude; **Galápagos** rising sea-temperature stressing endemic biodiversity + coral; **glacier retreat** (Cotopaxi, Antisana, Cayambe, Chimborazo glaciers losing mass — water-supply implications for Quito + Sierra cities)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1977** | No seismic-design code; high collapse risk in M>7 events; asbestos-cement (eternit), lead pipes |
| **1977–2000** (CEC era) | First seismic norm Código Ecuatoriano de la Construcción (CEC-77/80/2000); compliance variable |
| **2000–2014** | NEC-2001 + revisions; modern principles but enforcement uneven |
| **2014–2015 NEC-15** | Current code mandatory ([NEC-15](https://www.habitatyvivienda.gob.ec/)); microzonificación per major city; substantially upgraded post-Pedernales 2016 lessons |
| **Post-2016** | Stricter enforcement post-Pedernales tragedy; many coastal builds reinforced |

### Mandatory diagnostics at sale

| Document | Required because | Where to get |
|---|---|---|
| **Certificado de Gravámenes** | Title chain + charges (≥15-yr) | Registro de la Propiedad (cantón) |
| **Certificado Catastral / Avalúo** | Fiscal ID + value | Catastro Municipal (cantón) |
| **Pago de Predio (paz y salvo predial)** | No predial debt | GAD Municipal — Tesorería |
| **Certificado de no adeudar al Municipio** | No CEM / patente / municipal arrears | GAD Municipal |
| **Declaración Juramentada** (seller) | Status + family / patrimony | Notario |
| **Certificado de la EERSA / EP** + **EPMAPS / Interagua / ETAPA** | Utility no-debt | Per utility provider |
| **Reglamento de Propiedad Horizontal + acta asamblea** + alícuota status | If condo | Administrador edificio |
| **Plano Aprobado + Permiso de Construcción** | Build legality | Municipio Planificación |
| **Certificado de Uso del Suelo** | Use compliance per PUGS | Municipio Planificación |

⚠️ **Cadena de propietarios trap**: must show **clean ≥15-year chain**; rural + coastal cantones still have **derecho de posesión** parcels (not titled freehold) — these are harder to mortgage and transact. Always verify on the *certificado de gravámenes* + cross-check with cadastral plano.

---

## Section: `--mains`

### Sources + operators

- **EPMAPS — Empresa Pública Metropolitana de Agua Potable y Saneamiento Quito**: [`https://www.aguaquito.gob.ec/`](https://www.aguaquito.gob.ec/)
- **Interagua Guayaquil** (concesión privada): [`https://www.interagua.com.ec/`](https://www.interagua.com.ec/)
- **ETAPA EP Cuenca** (multi-utility: water + telecom + sewer): [`https://www.etapa.net.ec/`](https://www.etapa.net.ec/)
- **CNEL EP** (Corporación Nacional de Electricidad — coastal + amazónica): [`https://www.cnelep.gob.ec/`](https://www.cnelep.gob.ec/)
- **Empresa Eléctrica Quito (EEQ)**, **CENTROSUR Cuenca**, **Eléctrica de Guayaquil (CNEL Guayaquil)** — distribution
- **CNT — Corporación Nacional de Telecomunicaciones**: [`https://www.cnt.gob.ec/`](https://www.cnt.gob.ec/) — fibre + fixed-line; private competitors (Netlife, Claro, Tuenti)
- **ARCA — Agencia de Regulación y Control del Agua**: [`https://www.regulacionagua.gob.ec/`](https://www.regulacionagua.gob.ec/) — sector regulator
- **No piped natural gas network** (national); **GLP cilindros** distributed by Petroecuador subsidized + LPG

### Coverage

- **Urban (cabecera cantonal Quito + Guayaquil + Cuenca + Ambato + Machala + Loja)**: water + sewer near-universal (>95 % per INEC ENEMDU); **drinking-water quality** strong in Cuenca (ETAPA gold standard) + Quito; weaker in coastal Guayaquil (Interagua intermittent in some sectores)
- **Rural (recintos)**: variable; many rely on *junta de agua potable comunitaria* + pozo séptico
- **2024 power crisis**: severe drought caused nationwide **rolling blackouts in 2024** — CELEC EP: *"las recientes sequías … provocaron apagones en 2024"* ([Plan de Descarbonización CELEC EP, 2025](https://www.celec.gob.ec/wp-content/uploads/2025/10/BEI-PATH-Plan-de-Descarbonizacion-para-CELEC-ESP-1.pdf)); blackouts ran ~8–14 hr/day Sep–Dec 2024 (est.; duration not stated in the CELEC source); partial recovery 2025 with thermal-import contingency. Property buyers should budget for backup (generator / inverter / solar) particularly in Sierra hydro-dependent zones. *Verify current generation status at* [CENACE](https://www.cenace.gob.ec/)

### Costs (est., USD 2026)

| Scenario | Cost |
|---|---:|
| Mains water connection (urban parcel) | 200–800 |
| Mains sewer connection | 400–1,500 |
| Septic tank + cisterna (rural / coastal no mains) | 1,500–5,000 |
| Electricity new connection (EEQ / CNEL) | 100–500 standard tariff |
| Solar PV residential 5 kWp (with batteries post-2024 blackouts) | 6,000–14,000 |
| Backup generator (3–5 kVA inverter / portable) | 600–2,500 |
| Fibre activation (CNT / Netlife) | 0–80 (often promo) |

---

## Section: `--crime`

### Primary source

- **Ministerio del Interior + Policía Nacional**: [`https://www.ministeriodelinterior.gob.ec/`](https://www.ministeriodelinterior.gob.ec/) — annual *Informes de Seguridad Ciudadana* + monthly homicide stats
- **INEC — Estadísticas de Seguridad y Justicia**: [`https://www.ecuadorencifras.gob.ec/`](https://www.ecuadorencifras.gob.ec/) series

### Headline (2023–2025)

- **National homicide rate — the historic peak is 2025, NOT 2023**: **9,216 intentional homicides in 2025 → ~50.9 per 100,000**, the highest in the country's recorded history. Count from the Ministerio del Interior; rate computed by [Primicias](https://www.primicias.ec/seguridad/ecuador-homicidios-asesinatos-violencia-crimen-organizado-2025-114304) on the INEC 2025 population projection of 18,103,660. The PADF observatory [OECO](https://oeco.padf.org/homicidios2025) publishes **50.1** on a different denominator — the 9,216 count is corroborated by both plus [CNN Español](https://cnnespanol.cnn.com/2026/01/21/latinoamerica/ecuador-2025-anio-mas-violento-homicidios-orix) citing the same ministry report, so the count is firm and the rate moves with the population projection used. Same series: **2023: 47.25** (the prior peak — supersedes the unsourced ~46.5 carried here before) · **2024: 38.80**, the partial cooling under the Decreto 111 measures now fully reversed; 2017 pre-crisis baseline <6 (est. — not re-verified this pass). ⚠️ These are **secondary sources**: the Ministerio del Interior publishes the counts but **does not tabulate the rate** on its public pages — verify at [Min Interior](https://www.ministeriodelinterior.gob.ec/) / INEC before relying on the rate (2026-08-08 verified)
- **Hotspots 2024**: Esmeraldas (~80–100/100k), Manta (~70), Durán (~60), Guayaquil (~50), Quevedo (~45)
- **Lower zones**: Cuenca (~5–10), Loja (~5), Quito Mariscal/Cumbayá ~10–20 (varies sub-barrio), Galápagos near-zero
- **Internal armed conflict** (Decreto Ejecutivo 111, 9 Jan 2024, amending DE 110 of 8 Jan 2024) escalated military involvement; 22 grupos delictivos organizados (GDO) declared *terroristas* — ongoing operations

### Verdict bands

- 🟢 < 50 % national rate (Cuenca, Loja, sierra centro, Galápagos, most Quito residential barrios)
- 🟡 50–110 % (typical Quito, Ambato, Riobamba)
- 🟠 110–200 % (Guayaquil core, Manta non-tourist)
- 🔴 > 200 % (Esmeraldas, Durán, Quevedo, parts of Guayaquil + Manabí — multiple-category elevated)

⚠️ Crime data 2024–2026 in flux — *verify current* per cantón at Min Interior + travel advisories before any coastal acquisition.

---

## Section: `--amenities`

Universal OSM Overpass logic per `shared/amenities-osm.md`. Ecuador-specific brand-chain conventions:

- **Supermarket**: **Supermaxi / Megamaxi / AKÍ** (Corporación Favorita — dominant), **Mi Comisariato / Hipermarket** (El Rosado group — Guayaquil-strong), **Tía** (mid-tier / popular), **Santa María**, **Coral Hipermercados** (Cuenca + sierra)
- **Convenience**: **OXXO Ecuador** (FEMSA, growing 2022+), **Listo!** (Petrocomercial fuel-station), traditional **tiendas de barrio**
- **Pharmacy**: **Fybeca**, **Pharmacys**, **Sana Sana**, **Cruz Azul**, **Difare** chains (`amenity=pharmacy`); high density urban
- **Hospital + clinic**: public via **MSP — Ministerio de Salud Pública** ([`https://www.salud.gob.ec/`](https://www.salud.gob.ec/)) + **IESS** networks. Private: Hospital Metropolitano + Hospital de los Valles (Quito), Hospital Kennedy + Clínica Kennedy + Hospital Alcívar (Guayaquil), Hospital del Río + Hospital Monte Sinaí (Cuenca)
- **Public transport**: **Metro de Quito** (line 1 operational since Dec 2023 — 22 km, 15 stations), **Trolebús + Ecovía + corredores BRT** (Quito), **Metrovía Guayaquil** (BRT), **Tranvía Cuenca** (operational since 2020). Inter-city via **terminales terrestres** (Cooperativa de Transporte network) — no national rail (Tren Ecuador tourist-only since 2020 financial crisis)
- **Schools**: trilingual options in expat zones — Colegio Alemán, Liceo Francés, British, Cotopaxi Academy, plus public *unidades educativas* under MINEDUC

### Verdict bands

- 🟢 < 800 m walk to supermarket/farmacia/centro de salud: typical urban (Quito centro-norte, Cuenca centro, Cumbayá, Samborondón)
- 🟡 800 m–3 km: peri-urban / suburbano
- 🟠 3–10 km: rural cabecera + coastal villages
- 🔴 > 10 km: very rural recintos + páramo; access dependent on private vehicle

---

## Section: `--climate`

Universal logic per `shared/climate-projections.md`. Ecuador-specific:

- **Köppen-Geiger**: highly varied due to Andes + equator: **Aw / Am** (Costa, Amazonía tropical), **Cfb / Cwb** (Sierra mid-altitude — Quito, Cuenca *eternal spring*), **ET** (páramo > 3,500 m), **BSh** (dry valleys + Galápagos arid coast)
- **Reference**: [INAMHI](https://www.inamhi.gob.ec/) 1981–2010 baseline + IPCC AR6 + downscaled CIIFEN/MAATE projections
- **Key projections**:
  - Annual mean temperature **+1.5–3.0 °C** by 2100 (national); **Andean amplification** ~1.2× lowland
  - **Glacier retreat** Cotopaxi/Antisana/Chimborazo/Cayambe — material for Sierra water supply (Quito EPMAPS sources at risk)
  - **El Niño / La Niña** intensification: 2023 + 2024 *El Niño costero* caused catastrophic flooding in Manabí + Guayas + El Oro
  - **Sea-level rise**: +30–60 cm by 2100 — coastal Manabí + Esmeraldas + Galápagos exposed
  - **Galápagos** rising sea-temperature: coral bleaching, marine endemic stress
- **Acute-event flags**:
  - 🔴 coastal property < 5 m elevation in Esmeraldas + Manabí + Guayas (SLR + tsunami + El Niño compound)
  - 🔴 Cotopaxi lahar corridor (Latacunga / Salcedo / valles Chillos / Cumbayá) — IGEPN evacuation maps
  - 🟠 Andean slope > 30 ° gradient (deslizamientos)
  - 🟡 sierra mid-altitude urban (Quito centro-norte, Cuenca) — generally resilient; cooling-load growth modest
  - 🟢 sierra mid-altitude (1,800–2,800 m, south-facing, no slope risk) — among most climate-resilient zones globally

### Climate verdict (typical mid-altitude Quito / Cuenca apt)

🟢 **Resilient — with watch caveats** for Cotopaxi lahar / glacier-fed water supply. Coastal exposure is materially worse — separate verdict per zone.

### Confidence

HIGH for IGEPN + INAMHI + INOCAR projection envelopes (Ecuador has among the best volcano + tsunami monitoring in Latin America); MEDIUM for parcel-level hazard zoning (PUGS coverage variable across the 221 cantones).

---

## Section: `--finance`

### Mortgage market

- **Banking system**: dominant private banks **Banco Pichincha**, **Banco Pacífico** (state-owned 2009–present), **Produbanco**, **Banco Internacional**, **Banco Guayaquil**, **Banco Bolivariano**; cooperatives (Coopnacional, JEP, Jardín Azuayo)
- **BIESS — Banco del Instituto Ecuatoriano de Seguridad Social**: [`https://www.biess.fin.ec/`](https://www.biess.fin.ec/) — state pension-fund mortgage bank; **only for IESS affiliates** (Ecuadorian-employed); subsidized rates
- Regulator: **Superintendencia de Bancos** [`https://www.superbancos.gob.ec/`](https://www.superbancos.gob.ec/)
- **LTV caps** (typical):

| Buyer profile | Max LTV |
|---|---:|
| **IESS-affiliate via BIESS** | up to **100 %** (subsidized; only for affiliates) |
| **Resident (private bank)** | **70–80 %** |
| **Non-resident** (visa holder) | typically **50–60 %** |
| **Non-resident pre-residency** | rarely available; cash-based |

- **Term**: typically 15–25 years; BIESS up to 25 years
- **Rate structure (2026)**: **BIESS ~7–9.5 %** (subsidized to affiliates), **private bank residential USD ~8–12 %**, fixed dominant in USD economy. **No FX mismatch risk** — all loans + revenue in USD
- **Stress test**: BCE + Superbancos macroprudential expectations; banks apply DSR caps typically 30–40 % gross income

### Banking access

- **Account opening**: passport + visa (or constancia de movilidad humana) + comprobante de domicilio + RUC if business; typically 1–3 weeks for non-resident with proper documentation; FATCA + CRS reporting standard
- **ISD 5 %** on outbound transfers — material for non-resident repatriation; structure via traceable capital-import declarations to claim exemption

### Confidence

HIGH for BIESS framework + private-bank LTV ranges; MEDIUM for non-resident product availability (case-by-case post-2024 KYC tightening).

---

## Section: `--currency`

### Currency status

- **USD (US Dollar)** — dollarization adopted **9 January 2000** ([BCE — 25 años de dolarización](https://www.bce.fin.ec/25/index.html)); formalized by the Ley para la Transformación Económica del Ecuador (Mar 2000), replacing sucre at 25,000:1 after the 1999 banking + currency crisis
- **BCE — Banco Central del Ecuador** retains regulatory + reserve role but does **NOT issue banknotes** — only mints sub-unit *centavos* coins (1, 5, 10, 25, 50)
- US Federal Reserve banknotes circulate as legal tender; no exchange controls on USD
- **Status comparison**: Ecuador's full dollarization is **distinct from Panama** (USD via Monetary Convention 1904 + balboa parity) and El Salvador (post-2001 dollarization); shares family with Timor-Leste and several Pacific microstates

### What this means for buyers

- **USD-denominated buyers** (US, dollarized economies): **near-zero FX risk** for purchase + ongoing payments — UNIQUE LATAM advantage
- **EUR / GBP / non-USD buyers**: full USD/home-currency exposure — use forwards for transaction lock-in if material
- **No capital controls** on USD inflows; **ISD 5 %** on outbound transfers (Ley 2007 + reforms) — exemption available for traceable capital-import returns
- AML reporting under [Ley Orgánica de Prevención de Lavado de Activos](https://www.gob.ec/) aligned with FATF + GAFILAT

### Stability credibility

- Dollarization is **politically central** — every government since 2000 has reaffirmed it; abandonment would require constitutional + economic disruption far exceeding any plausible 2026–30 scenario. Correa government (2007–17) attempted partial monetary tools (electronic *dinero electrónico*, 2014–18) without de-dollarizing; programme withdrawn
- Currency-risk scenario for property: **near-nil** for USD holders over typical 5–10y horizon

---

## Section: `--visa`

Universal logic per `shared/visa-programs.md`. Ecuador-specific routes (under [Ley Orgánica de Movilidad Humana 2017](https://www.gob.ec/) + reglamento):

### Visa de Inversionista (Investor Visa) — Real Estate

- **Investment minimum**: **USD 47,000** (= **100 × SBU** at SBU 2026 USD 470/mo = 100 × 470; verify current SBU multiple at Cancillería) in Ecuadorian real estate (or fixed-term productive activity) *(2026-05-27 verified, source decreto Ministerio del Trabajo Dec 2025)*
- **Permit**: 2-year **Residencia Temporal**; renewable; **Residencia Permanente** after 21 cumulative months physical residence
- **Most common foreign-buyer route**

### Visa de Rentista (Pensioner / Annuitant)

- Stable **monthly fixed income ≥ USD 1,500** (pension, annuity, dividend, rental) + USD 250/dependent
- 2-year Temporal → Permanent after 21 cumulative months
- **Popular Cuenca expat route**

### Visa Profesional / Trabajo (Professional / Work)

- Recognized degree (apostilled, SENESCYT-validated) + employer sponsorship for Trabajo
- 2-year Temporal → Permanent after 21 cumulative months

### Other categories

- **Estudiante**, **Voluntario**, **Convención Mercosur** (for Mercosur-aligned nationals; reduced threshold), **Familia de Ecuatoriano** (family reunification)

### NOT a citizenship-by-investment jurisdiction

- ⚠️ **No CBI / golden-passport**. Naturalization requires **3+ years' permanent residency** (relatively short by international standards, but residency must be earned via the visa categories above) plus civics + Spanish exam. Not investment-direct
- Dual nationality recognized (Constitución 2008 art. 6) — Ecuador allows it

### Confidence

HIGH for Investor + Rentista frameworks (Ley Movilidad Humana 2017 stable); MEDIUM for current USD threshold quantum (linked to SBU which adjusts annually — *verify at* [Cancillería](https://www.cancilleria.gob.ec/) before application).

---

## Section: `--insurance`

### Mandatory

- **Mortgage lender requirement**: **seguro de incendio + desgravamen** (fire + life-of-borrower); premium typically **0.05–0.20 % of sum insured** (incendio) + 0.04–0.08 % (desgravamen)
- **Sum insured = rebuild cost** (not market price) — typically **USD 500–1,000/m² built** for standard concrete-frame construction in Sierra; coastal coastal-resistant +20–40 %

### Optional but standard

| Cover | Typical premium (2026 est.) |
|---|---:|
| **Home contents** (typical 100 m² apt) | USD 100–350/yr |
| **Liability** (responsabilidad civil) | usually bundled |
| **Earthquake (sismo)** | INCLUDED in most multi-peril policies (mandatory consideration post-Pedernales 2016); **verify sub-limit** carefully — many policies cap at 50–80 % of sum insured |
| **Volcanic ashfall + lahar** (Cotopaxi/Tungurahua/Reventador zones) | usually included; verify language on *erupción volcánica* explicitly |
| **Tsunami** | typically separate rider for coastal Pacific |
| **Flood** (El Niño) | usually included for *inundación*; verify *El Niño costero* |

### Major insurers

- **Seguros Equinoccial**, **Mapfre Atlas**, **Sucre**, **Hispana**, **Liberty Seguros Ecuador**, **AIG Ecuador**, **Latina Seguros** — regulated by [Superintendencia de Compañías, Valores y Seguros](https://www.supercias.gob.ec/)

### Climate + risk trajectory

- ⚠️ Premiums in **coastal Manabí + Esmeraldas + Galápagos** trending upward 2023–26 from El Niño + tsunami risk re-pricing; **post-2024 security crisis** has tightened underwriting in Guayaquil + Durán + Quevedo (theft + property damage)
- ⚠️ Cotopaxi lahar corridor (valles Chillos / Cumbayá / Latacunga) — verify policy explicitly covers *flujo piroclástico + lahar* (some policies exclude)

### Confidence

MEDIUM — Ecuadorian insurance market modest in scale; figures *est. from Supercias bulletins + insurer product sheets — verify per parcel*.

---

## Section: `--notary`

### Process

- **Civil-law notario** mandatory for all RE transfers per [Ley Notarial](https://www.funcionjudicial.gob.ec/) — Ecuador has notarías numbered per cantón under *Consejo de la Judicatura*
- *Notario* role: drafts the **escritura pública**, identifies parties (cédula or apostilled passport for non-residents), verifies title + charges via *certificado de gravámenes del Registro de la Propiedad*, withholds taxes, files inscription

### Standard timeline (typical residential resale)

| Step | Day | What happens |
|---|---|---|
| 1. Promesa de compraventa | D0 | Buyer pays **arras ~10 %**; private contract drawn (often by abogado, not notario yet) |
| 2. Due diligence + financing | D7–D45 | Certificado de Gravámenes, paz y salvo predial, paz y salvo servicios, planos aprobados; if mortgage: bank avalúo + carta de aprobación |
| 3. Foreign-buyer Border-Zone authorization (if applicable) | D14–D60 | Only for parcels within 50 km frontier or Galápagos — SECOB/Comando Conjunto |
| 4. Pago de Alcabala (1 %) at Municipio | D40–D55 | Buyer pays Alcabala receipt before notario |
| 5. Escrituración (deed signing) at notario | D45–D70 | Buyer pays balance; notario witnesses |
| 6. Inscripción en Registro de la Propiedad | D70–D90 | Notario files; title perfected |

⚠️ **Border Zone gating**: Pacific coast frontier-zone parcels + Galápagos require 4–8 weeks for SECOB authorization before escrituración; build into closing schedule.

### Costs

| Item | Typical |
|---|---|
| **Notario fee** | regulated arancel; ~0.4–1.0 % of price (caps for high-value) |
| **Alcabala** (Municipio) | **1 %** of price |
| **Registro de la Propiedad** | ~0.2–0.5 % of price (per cantón table) |
| **Lawyer (abogado patrocinador)** | 0.5–1.5 % of price (recommended for non-residents) |
| **IVA 15 %** (new-build first sale, non-VIS only) | 15 % of price |
| **Total transaction cost (resale, buyer side)** | **~2.5–4 %** of price |
| **Total transaction cost (new-build first sale, non-VIS)** | **~17.5–19 %** of price (incl. IVA) |

### Foreign buyer practical

- **Power of attorney**: notario accepts apostilled + Spanish-translated PoA for absent buyers
- **Source-of-funds**: bank + notario apply AML/KYC under Ley de Prevención de Lavado de Activos; bank statements + tax returns + capital-import declaration (key for ISD exemption)
- **RUC obtention**: required if buying via SAS or for rental income

---

## Section: `--compare`

### Ecuador vs LATAM neighbours (residential investment lens, Q1–Q2 2026)

| Country | Foreign-buyer rule | Acquisition cost (typical) | Annual recurring | Yield (mid-tier) | Currency |
|---|---|---:|---:|---:|---|
| **🇪🇨 Ecuador** | OPEN; Border Zone authorization (50 km + Galápagos) | 2.5–4 % resale / 17.5–19 % new-build non-VIS (incl. IVA 15 %) | Predial 0.25–5 ‰ avalúo + low alícuota | 4–8 % | **USD** (full dollarization 2000) |
| **🇨🇴 Colombia** | Open; foreigners equal | 2–4 % | Predial 5–16 ‰ | 4–7 % | COP (volatile) |
| **🇵🇦 Panama** | Open; 10 km border restriction; comarcas off-limits | 3–4 % | Inmuebles 0–1 % | 5–9 % | **USD** + balboa |
| **🇵🇪 Peru** | Open; restricted within 50 km of frontier | 4–5 % | Predial low | 4–7 % | PEN |
| **🇨🇱 Chile** | Open | 4–6 % | Contribuciones moderate | 4–6 % | CLP |
| **🇺🇾 Uruguay** | Open | 7–10 % | Contribución low | 4–6 % | UYU |

### Ecuador's distinctive position

- **Full USD economy** (since 2000) — UNIQUE in South America (Panama is Central America); **near-zero FX risk** for USD holders
- **Tax-attractive holding**: predial typically <0.3 % avalúo; **0 % CGT after 1-year hold** (UNIQUE LATAM exemption — Ley Orgánica Reforma Tributaria); **no annual wealth tax**
- **Visa pathway** USD ~47,000 (= 100 × SBU 470) (Inversionista) is among the lowest investment-residency thresholds globally
- **Counter-balanced by**: 2024+ security situation (coastal cantones especially); 2024 IVA hike to 15 % (Decreto Ejecutivo 198/2024); ISD 5 % outbound; smaller + thinner RE market than CO/MX/CL/AR; power-grid uncertainty post-2024 drought
- **Best fit**: USD-holding retirees + remote workers + Cuenca / Quito-Cumbayá / sierra mid-altitude buyers; HNW seeking dollar-denominated property without US-tax exposure
- **Worse fit**: pure coastal speculation in 2024–26 security overhang; non-USD buyers without FX hedge framework

For comparable South American profile see `countries/co/playbook.md` (Colombia neighbour) + `countries/pa/playbook.md` (USD analog) + `countries/uy/playbook.md` + `countries/cl/playbook.md`.

---

## Section: `--retirement`

Ecuador is among the **most popular retirement-first destinations in LATAM** for North American retirees, anchored by Cuenca's expat community.

### Pathways

1. **Visa de Rentista** (USD 1,500/mo pension or annuity) — most common retirement route
2. **Visa de Inversionista** (USD ~47,000 (100×SBU 470) in real estate) — combine with property purchase
3. **Convención Mercosur** for relevant nationals — simplified path
4. **Tercera Edad benefits** (post-65): tax + transport + utility discounts under [Ley del Anciano](https://www.gob.ec/sites/default/files/regulations/2018-10/Documento_Ley-Anciano-Reglamento.pdf) — IVA refund, transport 50 %, utility tariff reductions

### Cost-of-living for retirees (2026 est.)

- Median 2-bed rental Cuenca centro: **USD 500–1,000/mo**; Quito Cumbayá **USD 700–1,400/mo**; Salinas / coast **USD 500–1,200/mo**
- IESS public healthcare: ~**17.6 %** affiliate contribution (including pension) — voluntary affiliation available for non-employed; private cover USD 80–250/mo for 65+
- Hospital: HCAM (Quito), Hospital Carlos Andrade Marín (Quito), Hospital Teodoro Maldonado Carbo (Guayaquil), Hospital del Río (Cuenca); private Metropolitano + Kennedy + Monte Sinaí; major specialists US/CO 2–4 hr by air
- Utilities: USD 50–150/mo typical (electricity tariff subsidized residential)

### Tax position for retirees

- **Foreign pension income**: Ecuador-resident IR (progressive 0–37 %); DTAs limited (Spain, Italy, Germany among them; **no Ecuador-US DTA** — material for US retirees)
- **0 % CGT after 1-year hold** on habitual residence (Ley Orgánica Reforma Tributaria); **no wealth tax**
- Inheritance: progressive 0–35 % above ~USD 80k; spousal + descendant partial exemptions

### Verdict for retirement-first buyers

🟢 **Go** for USD-holding retirees seeking sierra-altitude (Cuenca, Quito-Cumbayá, Loja, Vilcabamba) low-tax base with strong expat community; 🟡 **Watch** for coastal (Manta, Salinas, Olón) buyers — climate + security risks more material 2024–26.

---

## Section: `--digital-nomad`

### Visa pathway

- **No formal digital-nomad visa** as of 2026; usable pathways:
  1. **Visa de Rentista** (USD 1,500/mo from foreign source — viable for SaaS founders + remote employees with stable income)
  2. **Visa Profesional** + remote employment (gray area; verify with Cancillería)
  3. **Tourist entry** up to 90 days (extendable +90 days once per calendar year via Movilidad Humana office)
- A **Nómada Digital visa** has been periodically discussed in Asamblea Nacional (2024–25) but not enacted as of verification date; *track* [Cancillería](https://www.cancilleria.gob.ec/)

### Connectivity

- **FTTH coverage** strong in Quito + Cuenca + Guayaquil + Loja (CNT, Netlife, Claro, Tuenti); fibre = **88.3 % of all fixed-internet connections** at end-2024 — a technology-share-of-accounts metric, not household coverage; fixed internet itself reaches only ~17.5 % of the population (2024 data, source [ARCOTEL Boletín cierre 2024](https://www.arcotel.gob.ec/wp-content/uploads/2015/01/Boletin-cierre-2024_compressed-1.pdf))
- Gigabit fibre USD 25–60/mo; 5G mobile launching 2024–26 (Claro, Movistar)
- ⚠️ **2024 power-grid blackouts** (Sep–Dec, 8–14 hr/day) materially disrupted remote-work reliability; budget for UPS + inverter + solar backup; situation improved 2025 but residual risk persists during La Niña drought years
- Co-working: **Impaqto Quito**, **Selina Cuenca / Selina Cumbayá** (chain), **Hub UDLA**, **Comuna Coworking**, **Cuenca Coworking** — USD 100–300/mo hot desk
- Time zone: UTC-5 year-round (no DST); favours US Eastern + EU async

### Cost-of-living for remote worker (2026 est.)

- Studio short-let (compliant): USD 400–900/mo; long-let 1-bed: USD 350–800/mo
- Eating-out: USD 3–6 *almuerzo del día* / USD 12–25 mid-range
- Resident remote-worker IR: progressive 0–37 % on declared worldwide income post-residency (Ecuador taxes on worldwide income for residents); pre-residency tourist stay = no Ecuador IR liability

### Verdict for digital-nomad-first buyers

🟡 **Watch** — strong infrastructure (post-2024 caveat), low CoL, sierra-altitude lifestyle quality, but no formal DNV + 2024–26 security overhang on coast + power-grid uncertainty. Best fit: HN remote-workers committing to Rentista visa + sierra altitude (Quito-Cumbayá, Cuenca, Loja).

---

## Section: `--macro`

### Headline 2024–2026 ([BCE](https://www.bce.fin.ec/) + [INEC](https://www.ecuadorencifras.gob.ec/) + [IMF Article IV 2024](https://www.imf.org/en/Countries/ECU))

- GDP growth: 2023 ~+2.4 % / 2024 ~**-1.5 to 0 %** (recession driven by armed-conflict shock + drought + power crisis) / 2025 fcst +1.0–2.0 % recovery
- GDP per capita 2024: ~**USD 6,500** (lower-middle income)
- Inflation: 2024 ~**3.0–3.5 %** (raised by IVA 15 % + fuel-subsidy phase-out); 2025 ~2.0–2.8 % — moderate by LATAM standards (USD-anchored)
- Unemployment 2024 (INEC ENEMDU): ~**4.3 %** open + **20 %** *empleo inadecuado* (under-employment) + ~52 % informal — material structural drag
- Public debt / GDP: ~57 % 2024; IMF Extended Fund Facility USD 4 bn approved May 2024 — fiscal-tightening conditionalities (subsidy phase-out + tax reforms)

### Trend drivers (2024–2026)

- **Internal armed conflict** (Decreto Ejecutivo 111, 9 Jan 2024) — ongoing security operations; tourism + real estate volume hit hard in coastal cantones; sierra cities + Cuenca more resilient
- **2024 power crisis** (worst drought in 60 yr) — material productivity drag Sep–Dec 2024; thermal-import contingency 2025
- **Noboa government** (2023–): fiscal-reform agenda + IMF programme; **Asamblea fragmentation** elevates legislative risk
- **2025 elections** + post-election regulatory continuity question
- **Oil + remittances**: Ecuador is OPEC ex-member (departed 2020); oil ~**USD 13 bn** export annual; remittances ~**USD 5–6 bn**/yr (mostly from US + Spain); both primary FX-sources sustaining dollarization
- **Drug-economy spillover**: Pacific coast as transit corridor for Colombian + Peruvian cocaine to US/EU — root of 2024 security crisis

[IMF 2024 Article IV](https://www.imf.org/en/Countries/ECU) flags fiscal sustainability + dollarization pressure (no monetary lever) + security situation + fuel-subsidy reform as primary watch items.

---

## Section: `--demographics`

### Population structure (2024 INEC ENEMDU + Censo 2022 series)

- **Total**: ~17.7 M (2024 mid-year est.); **Censo 2022 final**: 16.9 M (lower than projection — material revision)
- **By region**: Costa ~50 % / Sierra ~42 % / Amazonía ~5 % / Galápagos ~0.2 %
- **Median age**: ~28 (relatively young vs aged AD/IT/JP); age 65+: ~9 % rising
- **Net migration**: 2022–24 net **negative** (Venezuelan migrant departure + Ecuadorian emigration to US/Spain accelerated post-2023); ~150–200 k Ecuadorian out-migrants/yr 2023–24
- **TFR**: ~1.9–2.0 (declining; below replacement)
- **Geographic concentration**: Quito + Guayaquil + Cuenca account for ~38 % of population
- **Households**: ~5.0 M; avg size ~3.4; owner-occupier ~64 %, rental ~25 %, otros ~11 % (informal occupancy + propiedad colectiva indígena)
- **Indigenous population**: ~7 % self-identifying (Censo 2022) — Kichwa nationalities largest; collective land tenure under [CODENPE / CONAIE](https://www.gob.ec/) frameworks

### Implication for property

- **2024 emigration spike** has dampened mid-tier rental demand in coastal cantones; sierra cities (Cuenca expat-driven) more stable
- Supply: new-build pipeline slow 2024–25 (CAMICON construction GDP -3 % 2024); 2025–26 modest recovery
- Long-term demand floor: low TFR + ageing baseline = future demographic drag, partially offset by Venezuelan + Colombian inflows pre-2022 (now reversed)

---

## Section: `--esg`

### Climate-transition exposure

- **NDC under Paris Agreement**: **Second NDC 2026–2035** now operative — unconditional **8,800 kt CO₂-eq (7 %)** + conditional **10,600 kt CO₂-eq (8 %)** with international support, implementation budget and unconditional / conditional split not quoted from the RNCC page — verify there ([MAATE — RNCC](https://rncc.ambiente.gob.ec/rncc/news/segunda-contribucion-determinada-a-nivel-nacional-de-ecuador-2026-2035)) *(2026 data, source MAATE/RNCC; 2026-09-18 verified)*. First NDC (2019) target was 9 % unconditional / 20.9 % conditional by 2025 vs BAU (superseded; ⚠️ secondary sources — IEA policy database / Climate Analytics — not re-read on the RNCC page). ❌ `ambiente.gob.ec` DEPRECATED — 301s to an unrelated agency; use the `rncc.ambiente.gob.ec` subdomain
- Power generation ~**85 % hydro** (high renewable share but hydrology-vulnerable; 2024 drought exposed grid fragility); thermal import contingency 2024–25
- **Yasuní-ITT 2023 referendum**: Ecuadorians voted to halt Block 43 oil extraction — landmark climate-policy event; ongoing implementation
- **Fuel subsidy phase-out**: gradual 2024–25 (Noboa government, IMF programme); diesel + gasoline subsidies historic political flashpoint (Oct 2019, Jun 2022 protests)

### Property-level ESG

- **Energy efficiency**: no mandatory pre-sale energy certificate as of 2026 (unlike EU); voluntary green-build certifications (LEED, EDGE) gaining among premium developers
- **Solar PV** residential: net-metering in place since [Resolución ARCONEL 003/18](https://www.controlrecursosyenergia.gob.ec/) ❌ DEPRECATED — primary source removed (domain now serves a default web-server test page); verify Resolución ARCONEL 003/18 at ARCONEL / Registro Oficial; typical 5 kWp system ~USD 6,000–14,000 (est., market) — payback 6–10 yr at residential tariff
- **Heat-pump retrofit**: minimal demand (Sierra altitude moderate, no winter heating culture); coastal A/C dominant
- **Water resilience**: glacier retreat affects EPMAPS Quito long-term water security; private cisternas common
- **Volcanic + seismic resilience**: post-2016 Pedernales codes (NEC-15) substantially improved coastal new-build; pre-2000 stock commands retrofit overhang
- **Sea-level rise + coastal erosion**: material 2050+ for Manabí + Esmeraldas + Galápagos low-lying parcels

### Verdict (ESG lens for typical mid-altitude EC apt)

🟢 **Resilient** for sierra-altitude (Quito Cumbayá, Cuenca, Loja) properties — high-renewable grid + low climate exposure; 🟡 **Watch** for coastal cantones + Galápagos with rising SLR + insurance trajectory; 🟠 **Adapt** for pre-2000 unreinforced builds in seismic + Cotopaxi-lahar zones.

---

## Section: `--exit`

### Resale market liquidity

- **Average days on market 2025** ([CAMICON](https://www.camicon.ec/) bulletins): **mid-tier Quito + Cuenca apt 90–180 days**; Guayaquil mid-tier 120–240 days (2024 security drag); coastal premium 180–365+ days
- 2024 transaction volume contracted **-15 to -25 %** in coastal cantones; sierra near-flat per CAMICON; 2025 partial recovery
- INEC IPV quarterly: 2024–25 nominal flat-to-slightly-positive in sierra; coastal sub-flat

### Exit-cost stack (seller side)

- Estate agent commission: **3–5 %** + IVA 15 % on commission
- Notario fee (seller portion of regulated arancel): smaller share
- **CGT (IR aplicable)**: **0 %** if held >1 yr (UNIQUE LATAM exemption, Ley Orgánica Reforma Tributaria); progressive PIT scale otherwise
- Mortgage early-discharge: USD 200–800 admin
- ISD 5 % on outbound USD repatriation (with capital-import-traceable exemptions)
- **Total exit cost**: typically **3.5–6 %** of price + CGT/ISD if applicable

### Liquidity by sub-segment (qualitative, 2026)

| Segment | Liquidity | Notes |
|---|---|---|
| Mid-tier USD 80–200k Quito Cumbayá / Centro-Norte | 🟢 strong | expat + local-family demand |
| Mid-tier USD 60–150k Cuenca Centro / Ordoñez Lasso | 🟢 strong | expat-driven |
| Premium USD 250–600k Samborondón Guayaquil | 🟡 selective | HNW + 2024 security drag mixed |
| Coastal Salinas / Manta / Olón | 🟠 thin | climate + security combined drag 2024–26 |
| Galápagos | 🔴 very thin | LOREG-restricted; cash-only foreign-buyer rare |
| Pre-1990 sierra heritage | 🟡 niche | renovation-cost overhang; Centro Histórico Quito + Cuenca UNESCO constraints |
| Rural derecho de posesión | 🟠 weak | non-titled; harder to mortgage + transact |

### Verdict for exit risk

🟢 sierra mid-tier (Quito Cumbayá, Cuenca centro); 🟡 Guayaquil Samborondón (HNW pool resilient); 🟠 coastal speculation segment + pre-1990 unreinforced; 🔴 Galápagos + rural derecho de posesión. **2024 security crisis + power-grid drought combined have chilled coastal exit demand materially** — material for seller exit-liquidity modelling.

---

## Cost benchmarks (EC 2026)

| Item | Cost (USD) |
|---|---:|
| Notario fee (regulated arancel) | 0.4–1.0 % of price |
| Registro de la Propiedad | 0.2–0.5 % of price |
| Estate agent commission (each side) | 3–5 % of price |
| Alcabala (Municipio) | 1 % of price |
| IVA 15 % (new build first sale, non-VIS only) | 15 % of price |
| Lawyer (abogado patrocinador) | 0.5–1.5 % of price |
| Annual Predial Urbano | 0.025–0.5 % of *avalúo catastral* (0.25–5 ‰ COOTAD bands) |
| Alícuota / community fees (mid-tier apt) | 30–150/month |
| Fire insurance + home contents (100 m² apt) | 200–600/year combined |
| Renovation (basic refresh / full retrofit, 100 m² apt) | 8k–25k / 30k–80k |
| Solar PV 5 kWp + batteries (post-2024 backup) | 6,000–14,000 |
| Seismic retrofit (pre-1990 build) | 50–200 USD/m² built |
| **Total transaction cost (resale, buyer side)** | **~2.5–4 %** of price |
| **Total transaction cost (new-build first sale, non-VIS)** | **~17.5–19 %** of price (incl. IVA 15 %) |

## Active fiscal incentives (2025–26)

- **VIS / VIP housing** (MIDUVI-certified) — **0 % IVA** on first sale + reduced Alcabala in some cantones; subsidies via [Casa para Todos](https://www.habitatyvivienda.gob.ec/)
- **Tercera Edad benefits** (post-65): IVA refund, transport + utility discounts ([Ley del Anciano](https://www.gob.ec/))
- **IESS BIESS mortgages** (affiliates only): subsidized 7–9.5 % USD; up to 100 % LTV
- **Solar net-metering** ([ARCONEL Resolución 003/18](https://www.controlrecursosyenergia.gob.ec/)) — viable solar PV residential
- **Capital-import traceable funds**: ISD 5 % exemption on repatriation if traceable inbound declaration on file
- ⚠️ Most incentive frameworks under **Noboa fiscal reform** review 2025–26; verify before underwriting

## Common listing platforms

- **Plusvalía** — DOMINANT national portal
- **Properati Ecuador**, **OLX Ecuador**, **Mercado Libre Inmuebles**
- **Engel & Völkers Ecuador**, **RE/MAX Ecuador**, **Coldwell Banker Ecuador** — premium / international
- **Vivanuncios.com.ec**, **Inmobiliaria.com.ec**, **CasaClub** (Quito-focused)
- ⚠️ Many listings dual-agent or agency-mirrored — cross-check by *clave catastral* or address before assuming uniqueness

## Caveats unique to EC

- **Full USD economy** since Sep 2000 — UNIQUE in South America, near-zero FX risk for USD holders
- **Border Zone restriction** (50 km from international frontiers + Galápagos) requires SECOB authorization for foreigners; otherwise foreigners have full equality (Constitución art. 405-406)
- **Galápagos LOREG** — distinct land-tenure regime; effectively closed to non-resident purchase
- **Cadastre is municipal** (no national portal); every check via target GAD Municipal
- **Notario + Catastro Municipal + Registro de la Propiedad + Municipio Tesorería + SRI** all involved in any transaction — coordinate via lawyer + notario
- **2024 IVA 15 %** (Decreto Ejecutivo 198/2024, raised from 12 %, security funding, eff 1 Apr 2024) — kept for 2025 (DE 470) and in force for 2026 until a new decree (SRI Circular NAC-DGECCGC25-00000006, 26 Dec 2025); decree floor 13 %
- **0 % CGT after 1-year hold** (UNIQUE LATAM exemption for habitual residence, Ley Orgánica Reforma Tributaria)
- **ISD 5 %** on outbound transfers — material for non-resident repatriation
- **2024 internal armed conflict** (Decreto Ejecutivo 111) — coastal security crisis material for Esmeraldas / Manabí / Guayas / El Oro / Los Ríos cantones; sierra centro relatively safer
- **2024 power-grid drought crisis** — backup capacity (solar + inverter) advisable in Sierra
- **Cotopaxi active-phase 2024–26** — verify lahar-corridor zoning for valles Latacunga / Salcedo / Chillos / Cumbayá
- **NEC-15 seismic code** mandatory; pre-2000 stock requires retrofit assessment
- **Visa de Inversionista** USD ~47,000 (= 100×SBU 470) is among lowest investment-residency thresholds globally
- **No CBI / golden-passport**; naturalization requires 3+ years' permanent residency + civics + Spanish exam
- **Listing m²**: convention is *m² de construcción* (built); confirm vs *área útil* on visit *(per listing — verify with cadastre / on visit)*

## Reddit / forum sources

- **r/ecuador** — bilingual; expat + local mix
- **r/Cuenca** — strong Cuenca expat community
- **r/Quito**, **r/Guayaquil**
- **GringoTree Cuenca** + **CuencaHighLife** + **Expats in Ecuador** + **InternationalLiving Ecuador** — expat blogs (treat as 🟡 anecdotal; advisory only, not primary)
- **El Comercio** + **El Universo** + **El Telégrafo** + **Primicias** + **GK** — local journalism
- **Cuenca Real Estate Insider** + **Live in Ecuador** — relocation-advisory blogs (🟡)

## Verification authorities

| Authority | When to call |
|---|---|
| **GAD Municipal** (target cantón) | Catastro extract, clave catastral, predial, paz y salvo, PUGS hazard zoning |
| **Registro de la Propiedad** (cantón) | Title verification, *certificado de gravámenes*, escritura inscription |
| **Notaría** (per cantón) | Mandatory closing, IVA/Alcabala withholding |
| **SRI — Servicio de Rentas Internas** | RUC, IR/IVA/RIMPE, AML source-of-funds |
| **Superintendencia de Bancos** | Banking + BIESS mortgage |
| **Cancillería + Servicio de Migración** | Visa applications |
| **MINTUR — Ministerio de Turismo** | STR Catastro Turístico + LUAF |
| **IESS** | Social-security registration |
| **SGR + IGEPN + INAMHI + INOCAR** | Risk: seismic + volcanic + hydromet + tsunami |
| **MIDUVI** | VIS/VIP certification + housing policy |
| **DINARP** | Public-registry oversight |
| **SECOB / Comando Conjunto** | Border-Zone foreign-buyer authorization (50 km + Galápagos) |

## Source URL templates

| Source | URL |
|---|---|
| Gobierno (portal único) | `https://www.gob.ec/` |
| BCE — Banco Central del Ecuador | `https://www.bce.fin.ec/` |
| INEC — Ecuador en Cifras | `https://www.ecuadorencifras.gob.ec/` |
| SRI — Servicio de Rentas Internas | `https://www.sri.gob.ec/` |
| MIDUVI — Hábitat y Vivienda | `https://www.habitatyvivienda.gob.ec/` |
| MINTUR — Turismo | `https://www.turismo.gob.ec/` |
| MAATE — Ambiente | `https://rncc.ambiente.gob.ec/` (❌ `www.ambiente.gob.ec` DEPRECATED) |
| Cancillería — Movilidad Humana | `https://www.cancilleria.gob.ec/` |
| Ministerio del Trabajo | `https://www.trabajo.gob.ec/` |
| Ministerio del Interior | `https://www.ministeriodelinterior.gob.ec/` |
| MIT — Ministerio de Infraestructura y Tecnología (ex-MTOP) | `https://www.mit.gob.ec` |
| ANT — Tránsito | `https://www.ant.gob.ec/` |
| SGR — Gestión de Riesgos | `https://www.gestionderiesgos.gob.ec/` |
| IGEPN — Geofísico EPN | `https://www.igepn.edu.ec/` |
| INAMHI — Meteorología | `https://www.inamhi.gob.ec/` |
| INOCAR — Oceanográfico Armada | `https://www.inocar.mil.ec/` |
| MSP — Salud Pública | `https://www.salud.gob.ec/` |
| IESS — Seguridad Social | `https://www.iess.gob.ec/` |
| BIESS — IESS Bank | `https://www.biess.fin.ec/` |
| Superbancos | `https://www.superbancos.gob.ec/` |
| Supercias — Compañías + Seguros | `https://www.supercias.gob.ec/` |
| DINARP — Dirección Nacional de Registros Públicos | `https://www.gob.ec/dinarp` |
| Funcion Judicial / Notarías | `https://www.funcionjudicial.gob.ec/` |
| ARCOTEL — Telecom | `https://www.arcotel.gob.ec/` |
| ARCA — Agua | `https://www.regulacionagua.gob.ec/` |
| ARCONEL — Energía | `https://www.controlrecursosyenergia.gob.ec/` |
| CENACE — Operación Eléctrica | `https://www.cenace.gob.ec/` |
| CELEC EP / CNEL EP / EPMAPS / Interagua / ETAPA / EEQ / CNT | `https://www.celec.gob.ec/` · `https://www.cnelep.gob.ec/` · `https://www.aguaquito.gob.ec/` · `https://www.interagua.com.ec/` · `https://www.etapa.net.ec/` · `https://www.eeq.com.ec/` · `https://www.cnt.gob.ec/` |
| GAD Municipal Quito / Guayaquil / Cuenca | `https://www.quito.gob.ec/` · `https://www.guayaquil.gob.ec/` · `https://www.cuenca.gob.ec/` |
| CAMICON — Cámara Construcción | `https://www.camicon.ec/` |
| Plusvalía / Properati EC / OLX EC | `https://www.plusvalia.com/` · `https://www.properati.com.ec/` · `https://www.olx.com.ec/inmuebles_c367` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row |

## Status

**Confidence**: MEDIUM — HIGH on foundational legal/fiscal framework (IVA 15% per Decreto Ejecutivo 198/2024 + Ley Orgánica Reforma Tributaria; CGT short-term test reduced 5y → 1y; Visa de Inversionista USD 47,000 (100×SBU 470); USD-dollarised currency since 2000; SRI tax-residency tests; Visa 10-II + Visa 11-VI investor / pensionado routes). MEDIUM on parcel-level municipal predial assessment values, current blackout duration (national hydropower-deficit-driven, oscillating 8–14 hr through 2025–2026 dry seasons — verify with CENACE at point of analysis), and STR municipal-level rules (no national statute; Quito + Cuenca + Galápagos varying). LOW on residential price benchmarks (no national HPI; aggregator listings + Numbeo + Properstar with broker bias).

**Last verified**: 2026-08-08 (crime + security section only — armed-conflict decree corrected to DE 111 of 9 Jan 2024 against Suplemento al Registro Oficial No. 474, DE 218 of 7 Apr 2024 added as the post-April basis, homicide series re-based to the 2025 peak; balance of the 2026-05-27 pass unchanged); NDC target corrected 2026-09-18 per MAATE/RNCC — Second NDC 2026–2035 supersedes the 2019 first NDC (registry name corrected 2026-09-18 per gob.ec/dinarp). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Locked-in via primary government sources: foreign-buyer constitutional equality (Constitución 2008 art. 405-406 + Border-Zone 50 km SECOB authorization), USD dollarization since 9 Sep 2000 (Ley para la Transformación Económica del Ecuador, BCE confirmation), IVA 15 % since 1 Apr 2024 (Decreto Ejecutivo 198/2024 + Ley Orgánica para Enfrentar el Conflicto Armado Interno, SRI confirmation — *a decree can lower the general rate only to the 13 % floor (LRTI art. 65); SRI Circular NAC-DGECCGC25-00000006 keeps 15 % until a new decree*), Alcabala 1 % + COOTAD predial 0.25–5 ‰ bands (COOTAD art. 504-561 BOE), 0 % CGT after 1-year hold (LRTI art. 8 + reglamento, as amended by Ley Orgánica Reforma Tributaria), ISD 5 % outbound (Ley Reformatoria para la Equidad Tributaria 2007), Visa de Inversionista 100×SBU (= USD 47,000 at 2026 SBU 470/mo) + Rentista USD 1,500/mo (Ley Orgánica de Movilidad Humana 2017 + reglamento — *verify current SBU multiple at Cancillería*), NEC-15 seismic code mandatory (MIDUVI), MINTUR Catastro Turístico STR licensing under Decreto 1411/2020 + Decreto 803/2023, Decreto Ejecutivo 111/2024 internal-armed-conflict declaration (9 Jan 2024, amending the DE 110 estado de excepción; Min Interior). Galápagos LOREG and parish-level Catastro Municipal split confirmed via the DINARP (ex-DINARDAP) framework. **Re-verify each annual fiscal cycle** for IVA rate, SBU adjustment (Dec decreto MoT), Alcabala-per-cantón ordenanzas, predial bands per Municipio, and Border-Zone perimeter updates. **Watch list 2026**: Noboa fiscal reform package + Asamblea ratification; potential IVA 15 → 13 cut by decree (LRTI art. 65 floor 13 %) vs sustained 15 % (already at peak; further escalation politically improbable); internal-armed-conflict decree (DE 111 / DE 218) periodic renewal + security-situation evolution per cantón; 2025 election outcome regulatory continuity; Cotopaxi volcanic activity + IGEPN alert level; Galápagos LOREG residency-and-property reforms; power-grid generation status (CENACE) post-drought; ISD rate calibration (historic 0–5 % oscillation).

## Extension TODOs (deepen on first real run)

- [ ] Per-cantón predial table (Quito, Guayaquil, Cuenca, Manta, Salinas, Loja, Ambato, Riobamba) with each ordenanza tributaria year + bands
- [ ] Cotopaxi lahar-corridor parcel overlay (valles Chillos + Cumbayá + Latacunga + Salcedo) from IGEPN
- [ ] Border-Zone 50 km perimeter map + SECOB authorization workflow
- [ ] Galápagos LOREG residency + property restrictions full mapping
- [ ] STR Decreto 042-2020 Quito DMQ + Cuenca centro implementation status
- [ ] BIESS vs private-bank mortgage product comparison for residents
- [ ] 2024 security-crisis homicide-rate-per-cantón quarterly tracker
- [ ] Microzonificación sísmica overlay (NEC-15 anexo) for Quito + Guayaquil + Cuenca + Manta
- [ ] SAS property-holding structure walkthrough for foreign buyers
- [ ] Cuenca expat-cluster barrio-level price + alícuota database
