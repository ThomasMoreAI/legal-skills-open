# Paraguay 🇵🇾 — Property Due-Diligence Playbook

ISO2: `py`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode (Código Postal)**: 4-digit historic system + 5-digit modern format issued by **Dirección Nacional de Correos del Paraguay (DINACOPA)** (`https://www.correoparaguayo.gov.py/`). Asunción ranges roughly `1101`–`1925`; Ciudad del Este ~`7000`–`7400`; Encarnación ~`6000`. Postcodes weakly enforced — many addresses still rely on barrio + manzana + cuenta corriente catastral references rather than CP.
- **Admin levels**: 17 **departamentos** + Asunción **Distrito Capital** → ~250 **distritos / municipios** → barrios / compañías (rural) / manzanas (urban) → fincas (parcels) (Ley 3.966/2010 Orgánica Municipal + Constitución 1992 art. 156).
- **Currency**: **PYG — guaraní paraguayo** (ISO 4217 PYG, ₲). Régimen de **flotación administrada**; **BCP — Banco Central del Paraguay** (`https://www.bcp.gov.py/`) intervenes selectively. **No capital controls** at retail level. **USD widely used** for higher-value RE pricing (especially Asunción premium + cross-border Ciudad del Este). Modest inflation (~3–5 % typical post-2000s; BCP target 4 % ± 2 %).
- **Languages**: **Spanish + Guaraní** (both official, Constitución art. 140); Portuguese widely spoken near BR border (Ciudad del Este, Pedro Juan Caballero, Salto del Guairá); **Plautdietsch / German** in Mennonite colonies (Filadelfia, Loma Plata, Neuland — Chaco Central).
- **Cadastre**:
  - **SNC — Servicio Nacional de Catastro** under MEF (Ministerio de Economía y Finanzas) — `https://www.catastro.gov.py/` — assesses **valor fiscal** (cadastral base) per finca, issues **cuenta corriente catastral (CCC)**.
  - **DGRP — Dirección General de los Registros Públicos** under Corte Suprema de Justicia — `https://www.pj.gov.py/contenido/144-direccion-general-de-los-registros-publicos/144` — **Registro Inmobiliario** holds title/dominio chain per **finca + matrícula**.
  - **Identifier**: every parcel has both **finca número** (DGRP legal title) and **cuenta corriente catastral** (SNC fiscal). Both quoted in escritura pública.
- **Notary**: **Escribano público** — civil-law tradition; titles and authorisations from Corte Suprema; profession regulated by **Colegio de Escribanos del Paraguay** (`http://www.cep.org.py/`). Notary is **mandatory** for transfer of real property (Código Civil art. 700 inc. a, Ley 879/1981 Código de Organización Judicial). Buyer typically chooses the escribano.
- **Foreign ownership**:
  - **General rule**: **OPEN** — foreigners hold property rights equal to nationals (Constitución 1992 art. 109 + 109bis).
  - **Border-zone restriction** — **Ley 2.532/2005** art. 2 (as amended by Ley 2.647/2005) restricts ownership of rural land within the 50 km security zone to **foreign nationals of BORDERING COUNTRIES (Argentina, Bolivia, Brazil)** — or legal entities majority-controlled by such nationals. **Non-bordering nationals (US/EU/UK/Asian/African passports) are NOT subject to this restriction** and may acquire rural land in the zone, subject to standard cadastre + INDERT verification. Decreto 7525/2011 provides a public-interest executive-waiver pathway for bordering nationals (12-18 months). **Urban parcels** in border cities (Ciudad del Este, Encarnación, Pedro Juan Caballero, Salto del Guairá) remain available to all foreigners. (2026-05-27 verified, source [catastro.gov.py Ley 2532 PDF](https://www.catastro.gov.py/public/439bc5_ley%202532-05%20seguridad%20fronteriza.pdf) + BACN Ley 2647 + MEF Dictamen Jurídico 49/2025 — supersedes prior wording that incorrectly extended the restriction to all foreigners.)
  - Indigenous territories (tierras de comunidades indígenas) under Ley 904/1981 + INDI oversight — collective title, not transferable to foreigners.
- **Recent reforms (anchor — full timeline in `shared/regulatory-watch.md`)**:
  - **Ley 7143/2023** (sanctioned 2023-07, effective 2024-01) — **fused SET (Subsecretaría de Estado de Tributación) + DNA (Aduanas)** into the new **DNIT — Dirección Nacional de Ingresos Tributarios**, autonomous decentralised entity. SET no longer exists as an institution; URL `set.gov.py` redirects to **[dnit.gov.py](https://www.dnit.gov.py/)**. SET references throughout this playbook should be read as DNIT (ex-SET). (2026-05-27 verified, source Ferrere + DNIT institutional portal.)
  - **Ley 6.380/2019** — "Ley de Modernización y Simplificación del Sistema Tributario Nacional" — consolidated IRP, IRE, IDU, IVA. Effective 2020. **IRP rate clarification**: **rentas de servicios personales** = **progressive 8 % / 9 % / 10 %** by tramo de renta neta; **IRGC (ganancia de capital + rentas pasivas — including real-estate sale gains + rental income)** = **8 % flat**. (2026-05-27 verified, source DNIT IRP Cartilla 2024-07-30.) **IVA**: 10 % standard / **5 % reducido** — the 5 % reducido **applies to enajenación de bienes inmuebles (sale of immovables by IVA contributors, e.g., developers of new-build) AND to arrendamiento de inmuebles destinados a la vivienda** (residential rental by IVA contributor), per Ley 6380/2019 art. 90; vivienda rental by non-IVA-contributor (personal lessor) remains exento. (2026-05-27 verified, source DNIT IVA Tasas.)
  - **Ley 6984/2022 — Nueva Ley de Migraciones** (promulgated 17 Oct 2022) — **fully repealed Ley 978/1996**. Current residency categories (temporaria + permanente + espontánea + repatriados + Mercosur tracks) flow from Ley 6984/22 + reglamentación, administered by **Dirección Nacional de Migraciones (DNM)** (renamed from "General"). Decreto 18.295/1997 reglamento no longer in force. (2026-05-27 verified, source [migraciones.gov.py Ley 6984/22 portal](https://migraciones.gov.py/ley-n-6984-22-de-migraciones/).)
  - **Paraguay Investor Pass (launched May 2026)** — MIC + Migraciones express RBI pathway granting **direct permanent residency** for: **USD 200,000 invested in paraguayan securities market OR real-estate projects** (no job-creation obligation), OR **USD 150,000 in tourism sector**. Validity "definitive" with 10-year card renewal. This materially supplements the "no real-estate-only visa" pre-2026 framing — **USD 200k+ in qualifying inmobiliario projects DOES now qualify** for permanent residency. (2026-05-27 verified, source [MIC Paraguay Investor Pass launch](https://www.mic.gov.py/mic-y-migraciones-lanzan-el-paraguay-investor-pass-para-facilitar-la-residencia-permanente-a-inversionistas-extranjeros/) + ABC Color 2026-05-21.)
  - **Resolución SET 1186/2023** (now administered by DNIT) — tightened **Permanent Residency** requirements via legacy SUACE route: USD 70,000 investment via SUACE OR active RUC + economic activity. Investor Pass is the newer parallel route (2026).
  - **Impuesto Inmobiliario rural smallholder rate**: **0.50 %** (not 1.0 %) for **rural fincas <5 ha dedicated exclusively to agricultural activity** held as the owner's sole property — Ley 125/1991 art. 60 + Ley 5513/2015 amendment. Valor fiscal 2026 adjusted +4.1 % per Executive Decree end-Dec 2025. (2026-05-27 verified, source BACN + ABC Color.)
  - **Ley 5.811/2017** — Marco regulatorio de la construcción (Construction Code).
  - **Mercosur 2024** common-customs deepening; Itaipú Treaty Annex C renegotiation 2023–2024 (energy revenue + tariff impact).

---

## Section: `--price`

### Primary sources

| Source | Type | URL | What it gives |
|---|---|---|---|
| **SNC valor fiscal** | Cadastre | `https://www.catastro.gov.py/` | Per-finca **valor fiscal** (basis of Impuesto Inmobiliario). Typically **far below** market (often 10–30 % of market in Asunción). |
| **DGRP búsqueda registral** | Registry | `https://www.pj.gov.py/contenido/144-direccion-general-de-los-registros-publicos/144` | Title chain, gravámenes, prior transfers per finca (paid consulta) |
| **INE — Instituto Nacional de Estadística** | National stats | `https://www.ine.gov.py/` | Population, vivienda census, ECPV; no dedicated RE price index |
| **BCP estadísticas** | Central bank | `https://www.bcp.gov.py/` | FX, monetary, sector financiero (mortgage stocks); no dedicated price index |
| **CAPADEI / Cámara Paraguaya de Desarrolladores** | Trade body | `https://capadei.org.py/` | Asunción + suburbs developer-side market sense (limited free data) |
| **MUVH — Ministerio de Urbanismo, Vivienda y Hábitat** | Housing | `https://www.muvh.gov.py/` | Social housing programs (FONAVIS/AVI), price benchmarks for VIS |

⚠️ **No equivalent of DANE IPVN (CO) or INE IPCV (UY)** — Paraguay lacks a national transactional RE price index. Price discovery relies heavily on **listing platforms** + private brokers + CAPADEI bulletins.

### Listing platforms

| Platform | URL | Notes |
|---|---|---|
| **InfoCasas Paraguay** | `https://www.infocasas.com.py/` | Largest portal; agency + private; Asunción + Ciudad del Este coverage strong |
| **Clasipar** | `https://clasipar.paraguay.com/` | National classifieds incl. inmuebles |
| **MercadoLibre Inmuebles PY** | `https://inmuebles.mercadolibre.com.py/` | Wide coverage |
| **Properati Paraguay** | `https://www.properati.com.py/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Paraguay portal (Properati does not operate in PY) | Aggregator |
| **Remax Paraguay**, **Century 21 PY**, **Coldwell Banker PY** | various | Premium brokerages, Asunción + suburbs |
| **Inmobiliaria del Este** (CDE focus) | regional | Ciudad del Este + Alto Paraná |

### Currency convention

- **USD pricing dominant** for Asunción premium (Las Carmelitas, Villa Morra, Manorá, Carmelitas, Mariscal López corridor) + Ciudad del Este commercial + Encarnación waterfront premium.
- **PYG pricing** typical for sub-USD-100k properties, interior cities (Pedro Juan Caballero, Coronel Oviedo, Caaguazú), and lots/chacras.
- Rentals: **PYG-denominated short-term, USD common for premium long-term + corporate**.

### 2026 price benchmarks (USD/m², asking — InfoCasas + Properati + Remax PY listings cross-checked, Q1 2026)

| Region | USD/m² (typical) | Notes |
|---|---:|---|
| **Asunción — Carmelitas / Villa Morra / Mariscal López corridor** | $1,800–$3,200 | premium torres, embassy zone, modern stock |
| **Asunción — Manorá / Las Carmelitas** | $1,600–$2,800 | premium residential, low-rise + new towers |
| **Asunción — Centro / Sajonia / Trinidad** | $900–$1,800 | mixed older + new builds, value tier |
| **Asunción — Mburucuyá / Recoleta / Las Mercedes** | $1,400–$2,400 | mid-tier residential |
| **Asunción — Bañado Sur / Tacumbú** | $300–$700 | informal-formal interface; flood exposure |
| **Lambaré / San Lorenzo / Fernando de la Mora** (metro) | $700–$1,400 | commuter, mid-tier |
| **Luque / Capiatá / Limpio** (metro outer) | $500–$1,100 | growing commuter + airport corridor |
| **Mariano Roque Alonso / Villa Elisa / Ñemby** (metro) | $600–$1,200 | suburban |
| **Ciudad del Este — Centro comercial** | $1,000–$2,200 | retail-heavy, BR cross-border demand |
| **Ciudad del Este — Km 7 / Km 8 / Km 12 residencial** | $700–$1,400 | residential outer |
| **Encarnación — Costanera / centro** | $900–$1,800 | tourism + BR/AR cross-border |
| **San Bernardino — lakefront Ypacaraí** | $1,200–$2,500 | weekend / vacation home market |
| **Pedro Juan Caballero — centro** | $600–$1,300 | BR border, illicit-economy stigma — buyer caution |
| **Filadelfia / Loma Plata** (Chaco Mennonite) | $400–$1,000 | semi-autonomous communities, often closed market |
| **Interior tier-2** (Coronel Oviedo, Caaguazú, Pilar, Concepción) | $300–$700 | thin liquidity |

(Q1 2026 estimates, sources: InfoCasas indexed listings + Properati + selected Remax PY scrapes. **No primary-government price index exists**; figures are aggregated **listing asks**, not transacted — actual sale prices typically 5–15 % below asking. Rates/figures may have changed since.)

### Compute

1. USD/m² = USD asking / **superficie cubierta** (built area, declared in escritura) — distinguish from **superficie del terreno** (lot)
2. **SNC valor fiscal vs market**: Paraguayan valor fiscal is **dramatically below** market (often 10–30 %) — last general re-evaluation cadastral lagging. Use valor fiscal **only for tax estimation**, never as market proxy.
3. **Trap**: USD-billete (cash) vs USD wire — slight cash premium near border zones (Ciudad del Este, Pedro Juan Caballero) tied to AML/UIF friction.
4. **Trap**: listings often quote price WITHOUT expensas / cuota condominial — Asunción premium torres can be USD 3–8/m²/mes.
5. **Trap**: rural lots advertised "hectáreas con casa" — listing area conflates lot + built; clarify before computing USD/m².

### Key terms

- **Finca** = parcel ID at DGRP (legal title); **Matrícula** = title number on registro
- **Cuenta corriente catastral (CCC)** = SNC fiscal reference; basis for Impuesto Inmobiliario
- **Valor fiscal** = SNC-assessed value (basis for property tax + transfer tax base, though declared price wins if higher)
- **Escritura pública** = notarized deed (sole legal proof of transfer)
- **Boleto de compraventa** = pre-escritura binding pact (often with seña 10–30 %)
- **Hectárea** (ha) = 10,000 m² — standard rural unit

---

## Section: `--traffic`

### Primary sources

| Source | URL | What it gives |
|---|---|---|
| **MOPC — Ministerio de Obras Públicas y Comunicaciones** | `https://www.mopc.gov.py/` | Red vial nacional inventory + selected aforos vehiculares (irregular publication) |
| **DINATRAN — Dirección Nacional de Transporte** | `https://www.dinatran.gov.py/` | Public transport (buses interurbanos), commercial freight |
| **Municipalidad de Asunción — Tránsito** | `https://www.asuncion.gov.py/` | Capital traffic management, conteos selectos en arterias |
| **PMT — Policía Municipal de Tránsito** (Asunción + Lambaré + San Lorenzo etc.) | per municipio | Local traffic enforcement, occasional aforos |
| **OSM fallback** | `https://overpass-turbo.eu/` | `highway=` class — coarse band |

⚠️ **Traffic count availability is LOW** in Paraguay vs FR/DE/ES: MOPC aforos vehiculares are **published irregularly** and many segments lack public TPDA (Tránsito Promedio Diario Anual) data. For most properties, **OSM `highway=` class is the working fallback**.

### Key term

**TPDA (Tránsito Promedio Diario Anual)** — Paraguayan equivalent of TMJA (FR) / AADT (UK). Published selectively by MOPC for **rutas nacionales primarias**.

### Verdict bands (TPDA)

- 🟢 < 1,000 v/d (rural ruta departamental, calle barrial)
- 🟡 1,000–5,000 v/d (avenida secundaria, ruta nacional baja-densidad)
- 🟠 5,000–20,000 v/d (avenida arterial Asunción, Ruta PY01/PY02 tramos rurales)
- 🔴 > 20,000 v/d (Avda. Mariscal López, Avda. España, Avda. Eusebio Ayala, Ruta PY01 metro Asunción, Ruta Internacional CDE-Foz)

### Coarse fallback (OSM `highway` class)

- `motorway/trunk` ≈ Ruta PY01 (Asunción–CDE) + PY02 (Asunción–Encarnación) selected segments — note: very few true motorway segments in PY
- `primary` ≈ Ruta nacional principal (PY01, PY02, PY03 Asunción–Concepción, PY07 CDE–Pedro Juan)
- `secondary` ≈ Ruta departamental, avenida urbana
- `tertiary` ≈ camino vecinal
- `residential` ≈ calle interior

### Notes

- **Asunción Microcentro + arteries** (Avda. Mariscal López, Avda. España, Avda. Eusebio Ayala, Avda. Artigas, Avda. Madame Lynch): peak congestion 07:00–09:00 + 17:30–19:30; Ruta PY01 km 5–km 25 corridor saturated rush hour.
- **Ruta PY02 Asunción → Encarnación**: peak in summer (Dec–Feb) for beach/lake traffic to San Bernardino + Areguá; bus + truck heavy year-round.
- **Ruta PY07 + Puente de la Amistad (CDE → Foz do Iguaçu BR)**: extreme cross-border traffic, especially weekends + Brazilian shopping rushes; congestion + queue minutes-to-hours typical.
- **Bypass Asunción (Ñemby–Limpio bypass)** under construction phases; consult MOPC vialidad updates.
- **Buses + camiones**: high heavy-vehicle share on rutas nacionales; noise + air quality consideration for properties on PY01 corridor.

---

## Section: `--tax`

### Annual property tax — Impuesto Inmobiliario

**Levied by Municipalidad** (Ley 125/1991 + Ley 620/1976 + Ley 6.380/2019 ratification). Basis: **valor fiscal** per CCC at SNC.

#### National rate

- **General**: **1.0 %** of valor fiscal (Ley 125/1991 art. 60).
- **Edificado (built)**: full 1.0 % rate.
- **Baldío (vacant urban lot)**: surcharge possible per municipal ordenanza (some municipios apply +0.5 %).

#### Impuesto Inmobiliario Adicional Rural — Latifundios

- For **rural fincas** > 10,000 ha: **additional 0.5–1.0 %** under Ley 125/1991 + amendments (anti-latifundio surcharge). Triggers progressive scale.
- For most residential / urban / small rural buyers — **does NOT apply**.

#### Surcharges + adjacent municipal taxes

- **Tasa especial de servicios (limpieza, alumbrado, recolección de basura)** per Municipalidad — varies; Asunción typically PYG 200,000–800,000/year (~USD 30–115) for residential per ordenanza tributaria.
- **Tasa de pavimentación** (one-time, per obra) when streets paved — per ordenanza.

(Ley 125/1991 + Ley 6.380/2019; verify current ordenanza tributaria at each Municipalidad — Asunción `https://www.asuncion.gov.py/`)

### Transaction taxes — one-time at purchase

| Item | Rate | Source |
|---|---|---|
| **Notarial fees (escribano)** | ~0.5–2.0 % sliding (Ley 1.190/1985 arancel notarial — verify current actualización per Colegio de Escribanos) | `http://www.cep.org.py/` |
| **DGRP — Inscripción registral** | PYG ~200,000–500,000 fijo + small ad valorem (escala TUPA DGRP) | `https://www.pj.gov.py/contenido/144` |
| **IVA on professional services** | 10 % on notary fees + comisión inmobiliaria | SET — Subsecretaría de Estado de Tributación |
| **Comisión inmobiliaria** | 3–5 % + IVA, customarily seller-side; sometimes split | mercado |
| **Estudio de títulos (abogado)** | USD 300–1,500 fijo o 0.3–1.0 % | privado |
| **Total buyer-side closing costs** | ~**1.5–4 %** of price | sum of above (lower than UY/CO due to low notarial scale + no general transfer tax) |

⚠️ **Key Paraguay distinction**: **NO general property transfer tax** equivalent to UY ITP (4 %) or CO Impuesto de Registro (0.5–1 %). The transfer is taxed via **IRP/IRE/IDU on capital gain** (see below) instead — total cash cost at closing is typically **lower than LATAM peers**.

### Capital gains on resale

- **Individuals (residentes domiciliados)**: gains from sale of **non-habitual** real estate fall under **IRP — Impuesto a la Renta Personal** (Ley 6.380/2019 + Decreto 3.184/2019 + 2.787/2019):
  - **Tax base**: 30 % of net gain treated as taxable income (Decreto 3.184/2019 art. 60).
  - **Rate**: **8 % flat** on the taxable portion (effective ~2.4 % of gross gain after 30 % proxy).
  - **Primary residence exemption**: **Decreto 9.371/2018** + Ley 6.380/2019 — sale of vivienda habitual after **2+ years continuous use** as principal residence may be **exempt** (verify with contador).
- **Entities (sociedades)**: under **IRE — Impuesto a la Renta Empresarial**: **10 % flat** on net gain (Ley 6.380/2019).
- **IDU — Impuesto a Dividendos y Utilidades**: 8 % on distributions to individuals + 15 % to non-residents (when entity holds property).
- **Non-resident individuals**: subject to **IR** retención at notary on **gross sale price** (rate per Ley 6.380/2019 + reglamento — typically 4.5 % effective on gross, verify current SET resolution).

(Source: Ley 6.380/2019 + Decretos reglamentarios + SET — `https://www.set.gov.py/`)

### Inheritance / herencia

- **No general inheritance tax** in Paraguay (under Ley 6.380/2019 framework, the legacy "impuesto a herencias y legados" is not a separate active tax).
- However: notarial + judicial sucesión costs apply (~1–3 % of patrimonial value depending on complexity).
- Ganancia ocasional / IRP on subsequent sale of inherited property follows standard rules (cost basis = valor fiscal at inheritance OR declared market value).

### Example calculation — Asunción Villa Morra apartment, USD 200,000 market, valor fiscal USD 30,000 equivalent

```
Market price (declared in escritura):    USD 200,000
Valor fiscal (SNC, ~15 % of market):     USD  30,000  ← basis for Impuesto Inmobiliario
Impuesto Inmobiliario (1.0 % of VF):     USD     300 / year
Tasa especial servicios (Asunción):      USD  30–115 / year
Notario (~1.0 % of price):               USD   2,000 (negotiable)
DGRP inscripción (fijo + ad valorem):    USD     ~80
Estudio títulos (abogado):               USD     500–1,000
Comisión inmobiliaria 4 % seller-side:   USD   8,000 (paid by seller customarily)
─────────────────────────────────────────────
Total buyer transaction cost:            ~USD 2,580–3,180 (~1.3–1.6 % of price)
Annual recurring tax:                    ~USD 330–415
```

(Computed example, inputs listed inline. **Real valor fiscal must be looked up per finca at SNC** — `https://www.catastro.gov.py/`. Comisión inmobiliaria customarily seller-side; some markets split.)

### Future risk

- **General re-valuation cadastral**: valor fiscal lag is dramatic — discussions of nationwide revaluación periodically surface. Would significantly raise Impuesto Inmobiliario if implemented (potentially 3–5×); monitor MEF + SNC announcements.
- **Mercosur tax harmonisation 2024–** discussions could revise IRP/IRE rates.
- **Latifundio surcharge** scope (>10,000 ha threshold) periodically debated; monitor Congreso reform cycles.
- **Itaipú revenue impact** (post-2024 Treaty Annex C renegotiation) — fiscal-space implications for municipal budgets, possibly pushing higher local levies.

---

## Section: `--rental`

### Long-term residential

**Statutory framework**: **Ley 1.183/1985 — Código Civil Paraguayo** (Libro III, Tít. VII — Locación) + **Ley 125/1991 art. 75–80** (tax aspects). Less rigid tenant-protection tilt than Uruguay/Argentina; more flexible than EU norms.

#### Standard contract structure

- **Plazo**: típicamente **1–2 años**; renewal by mutual agreement.
- **Garantía**: depósito **1–2 meses** + sometimes garante personal (cosigner with title or income proof).
- **Reajuste**: free to agree — IPC-indexed (BCP IPC `https://www.bcp.gov.py/` indices) or USD-pegged clauses common; PYG-denominated rents typically reviewed annually.
- **Desalojo (eviction)**: judicial process; non-payment + abandono are faster grounds (~3–8 months); contractual breaches longer.
- **Subarriendo**: requires landlord consent unless contract permits.

#### Income tax on rental

| Status | Regime | Rate |
|---|---|---|
| **Resident natural person** | **IRP — Renta de la prestación de servicios + arrendamientos** under Ley 6.380/2019 | **8 % flat** on net taxable rent (with 50 % presumption deduction or actual expenses, per Decreto 3.184/2019) |
| **Non-resident** | IRP-NR retención by tenant or property manager | retención per SET resolución vigente (verify) — typically 4.5 % effective on gross |
| **Corporate (SA/SRL/EAS)** | **IRE** | 10 % on net rental income |
| **IVA on residential rental** | **0 %** (exempt) for vivienda; **10 %** if commercial / amueblado short-term hotelero | Ley 6.380/2019 |

⚠️ **IRP threshold**: Paraguayan IRP only applies above ~36 monthly minimum wages (~PYG 90 M/year ≈ USD 12,500/year at 2026 FX) accumulated income — **most small landlords below threshold pay nothing**; verify with contador as threshold updates.

(Source: Ley 6.380/2019 + Decreto 3.184/2019 + SET — `https://www.set.gov.py/`)

### Short-term rentals (alquiler temporal / Airbnb)

#### Statutory classification

- **SENATUR — Secretaría Nacional de Turismo**: `https://www.senatur.gov.py/` — registers turismo establishments under **Ley 1.388/1998** (Ley Orgánica de Turismo) + **Decreto 8.771/2017** (reglamentación de prestadores de servicios turísticos).
- **STR Airbnb-style**: technically falls under "alojamiento turístico" if commercial; **SENATUR registry recommended** for properties offered habitually + commercially.
- **Enforcement**: variable. Asunción + Encarnación + San Bernardino lakeside seeing growing SENATUR / DNVS sweeps 2024–2026.

#### Asunción — municipal layer

- **Ordenanza Municipal de Asunción**: standard commercial-activity registration if STR is professional/recurring; tasa habilitación local applies.
- **No dedicated STR-specific municipal regime** comparable to Colombia's national RNT regime (the often-cited Bogotá 'Decreto 538/2024' is unverified) — STR remains lightly regulated formally as of 2026 Q1.

#### Encarnación + San Bernardino lakeside

- Growing tourism market — Encarnación Costanera + Carnaval Encarnaceno + Itapúa Jesuit ruins drive seasonal demand.
- San Bernardino + Areguá (Lago Ypacaraí): traditional summer-home market (Dec–Feb peak); STR Airbnb listings expanding.
- SENATUR registration intermittently enforced; municipal tasas habilitación apply.

#### Tax regime for STR

- Same **IRP 8 %** flat for residents (above income threshold); **IRP-NR retención** for non-residents.
- **IVA**: hotelero commercial (con servicios accesorios — limpieza diaria, recepción) attracts **10 % IVA**; pure room rental for vivienda **exento**.
- If letting habitual + organized commercially → may be classified as **IRE actividad empresarial** (10 % on net + IDU + IVA + SENATUR registration).

### Strategic notes

- **Asunción long-term residential**: yields ~5–8 % gross typical (Villa Morra/Carmelitas premium 4–6 %; mid-tier Sajonia/Trinidad 6–9 %); USD-pegged premium rentals more stable in real terms.
- **Asunción STR**: thinner business-traveler driven; corporate furnished apartments dominant in Carmelitas + Mariscal López; classic Airbnb tourist demand shallow vs LATAM peers.
- **Encarnación + San Bernardino**: highly seasonal — Dec–Feb peak (3–4 months), Apr–Oct shoulder/low; annual yields 4–7 % gross.
- **Ciudad del Este**: cross-border + commercial demand; thin classic-tourist STR; corporate furnished demand around free-zone / Itaipu projects.
- **Mennonite Chaco** (Filadelfia, Loma Plata): **largely closed-market**, semi-autonomous economy via **Cooperativa Chortitzer / Fernheim / Neuland**; outside investor tractor-trade limited; verify locally.

---

## Section: `--work=<profession>`

### Job platforms

- **Computrabajo Paraguay**: `https://www.computrabajo.com.py/`
- **Konzerta Paraguay**: `https://www.konzerta.com/`
- **Trabajos.com.py**: `https://trabajos.com.py/`
- **OCC Mundial Paraguay** (selectivo)
- **LinkedIn Paraguay** — strong for IT, finance, MNCs in Asunción + free-zone Ciudad del Este
- **Clasipar Empleos**: `https://clasipar.paraguay.com/` — classifieds
- **Servicio de Empleo MTESS**: `https://www.mtess.gov.py/` — Ministerio de Trabajo, Empleo y Seguridad Social

### Self-employment / business regimes

- **RUC** (Registro Único del Contribuyente) at SET — mandatory for any economic activity (`https://www.set.gov.py/`).
- **IRP — Impuesto a la Renta Personal**: 8 % flat above ~36 SM mínimo accumulated yearly — Ley 6.380/2019.
- **IRE — Impuesto a la Renta Empresarial**: 10 % flat on net (Ley 6.380/2019); applies to SA/SRL/EAS (Empresa por Acciones Simplificada).
- **IDU — Impuesto a Dividendos y Utilidades**: 8 % residents / 15 % non-residents on distributions.
- **IVA**: 10 % standard / 5 % reducido (alimentos básicos, salud, educación, vivienda VIS).
- **EAS — Empresa por Acciones Simplificada** (Ley 6.480/2020): simplified one-person corporation; ~1 week setup via SUACE.
- **SUACE — Sistema Unificado de Apertura y Cierre de Empresas** (`https://www.suace.gov.py/`): one-stop business registration.
- **IPS — Instituto de Previsión Social**: social security; ~9 % worker + 16.5 % employer on payroll.

### Foreign worker / residency permits

- **Dirección Nacional de Migraciones (DNM, ex-DGM)** under Ministerio del Interior: `https://www.migraciones.gov.py/`
- **Permanent Residency (RUE — Residente)**:
  - **Pre-2023 regime**: USD ~5,200 BNF (Banco Nacional de Fomento) deposit was sufficient — Paraguay was historically **one of the world's cheapest formal residency-by-investment** paths.
  - **Post-2023 (Resolución SET 1186/2023)**: tightened — applicant must demonstrate **either** (a) active SET RUC + economic activity in PY, OR (b) **investment ≥ USD 70,000** in business via SUACE with business plan + commitment.
  - Even post-tightening, Paraguay remains **among the cheapest formal RBI in South America**.
- **Mercosur visa**: nacionales AR/BO/BR/CL/CO/EC/PE/UY (+ asociados) → expedited residencia temporaria → permanente.
- **Investor SUACE Visa**: ≥ USD 70,000 invest + business plan + RUC.
- **Naturalisation**: 3 years continuous PR + Spanish OR Guaraní + integración + sin antecedentes → **Paraguayan passport** (Constitución art. 148).

### Salaried benchmarks (2025–2026)

- **Salario mínimo nacional 2025**: **PYG 2,798,309/mes** (~USD 380 at PYG 7,400/USD; verify current at MTESS + Decreto Salario Mínimo annual). 2026 update typically Q1.
- **Median formal monthly wage** (DGEEC/INE EPH 2024): ~PYG 3.5–5 M (~USD 470–680).
- **IT senior dev (Asunción MNC / free zone)**: ~USD 1,500–4,000/mes (often paid USD).
- **Médico generalista (sector público — IPS / MSPBS)**: ~USD 1,000–2,000.
- **Médico especialista (privado — Sanatorio Migone, IPS, Hospital Bautista)**: ~USD 2,500–5,000.

### Catchment heuristics

- **Asunción Metropolitan Area** (~3.0 M): full national labor market; MNCs (Itaipú, ANDE, Banco Itaú PY, Continental, Atlas, Familiar, MNCs Asunción), gov, finance, agribusiness HQ, IT growing.
- **Ciudad del Este metro** (~600k): commerce + Itaipú + free-zone industrial + cross-border BR services.
- **Encarnación** (~130k): regional services, university (UNAE), tourism, BR/AR cross-border.
- **Pedro Juan Caballero** (~120k): BR border commerce + agribusiness; security stigma.
- **Filadelfia / Loma Plata Chaco** (~50k combined): Mennonite-cooperative economy (cattle, dairy — Lácteos Trébol, agribusiness); semi-closed labor market.
- **Interior tier-2** (Coronel Oviedo, Caaguazú, Pilar, Concepción): thin formal labor; agropecuario + small commerce + remote-work + civil service.

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SEN — Secretaría de Emergencia Nacional** | `https://www.sen.gov.py/` | Emergency management; historic flood + drought + wildfire events; alertas |
| **DINAC — Dirección Nacional de Aeronáutica Civil** (meteorología) | `https://www.dinac.gov.py/` | Climate data, alertas meteorológicas, wind/rain history |
| **MADES — Ministerio del Ambiente y Desarrollo Sostenible** | `https://www.mades.gov.py/` | Environmental risk, deforestation, water-quality |
| **INFONA — Instituto Forestal Nacional** | `https://www.infona.gov.py/` | Forest fire data, deforestation Chaco / Cerrado |
| **DGEEC / INE Atlas Vivienda** | `https://www.ine.gov.py/` | Census-based vivienda indicators (riesgo zonas) |
| **ERSSAN — Ente Regulador de Servicios Sanitarios** | `https://www.erssan.gov.py/` | Water + sanitation regulation |

⚠️ **No address-level risk database** equivalent to FR Géorisques / DE Hochwasserkarte. Risk assessment requires triangulation across SEN historic events + topography + INFONA + commune-level visual maps.

### Flood + river risk

- **River basins**: **Río Paraguay** (western frontier with AR + BO + BR), **Río Paraná** (eastern frontier with AR + BR), **Río Pilcomayo** (Chaco frontier with AR), **Río Tebicuary** + **Río Manduvirá** (interior).
- **Asunción Bañados** (Bañado Sur + Bañado Norte): informal settlements on **Río Paraguay floodplain** — recurrent catastrophic flooding (2014, 2015, 2018, 2019, 2024). Bañado parcels carry **HIGH flood exposure**; SEN evacuation events repeatedly affect 50,000–100,000+ residents.
- **Pilar (Ñeembucú)**: historically the most flood-prone significant town in PY — 1983, 1992, 1997–98, 2014, 2015–16, 2018–19 events.
- **Encarnación Costanera**: post-Yacyretá reservoir (1994 filling completed 2011) — riverfront refurbished + protected, but downstream Ayolas + Itá Ibaté carry residual exposure.
- **Concepción + Pedro Juan Caballero**: smaller-river flood risk seasonal (Oct–Mar wet season).

### Drought + wildfire

- **Chaco Central + Boreal** (Filadelfia, Mariscal Estigarribia): **severe drought zones**; 2019–2020 + 2022 + 2024 prolonged dry seasons → wildfire outbreaks across **Cerrado + Chaco** vegetation.
- **2019–2020 fires**: catastrophic — Chaco + Cerrado saw multi-million-hectare burns; Pantanal frontier border BR/PY/BO.
- **2024 fires**: renewed catastrophic events; ongoing climate-amplified trend.
- **Wildfire-urban interface** for properties on Chaco edge + Cerrado-adjacent — verify INFONA hot-spot history per zona.

### Seismicity

- **Very low — intra-plate continental setting**. South American Platform / Brazilian Shield — minimal seismic hazard.
- Historical record: occasional M < 4 events; **no significant damaging earthquakes in modern record**.
- **Building codes do NOT require seismic-resistant design**; standard reinforced concrete + masonry construction applies.
- For most properties, seismicity is **🟢 negligible**.

### Crime + security

- **Asunción**: moderate-low; declining post-2018 with national security reforms; premium distritos (Carmelitas, Villa Morra, Mariscal López, Las Mercedes) safer; informal periferia + Bañados higher-risk.
- **Ciudad del Este**: cross-border smuggling + counterfeiting hub historically; commercial centro busy + watched; residential outer zones mixed.
- **Pedro Juan Caballero**: BR border, **drug-trafficking presence** (PCC + CV factions, narcomenudeo, occasional spillover violence) — buyer caution; foreign RE buyers should engage local lawyer + verify finca chain extra-carefully.
- **Salto del Guairá**: similar BR-border cross-flow; smaller scale.
- **Interior rural**: generally low crime; aislado abigeato (cattle theft) seasonal in Chaco.
- **Source**: Policía Nacional `https://www.policianacional.gov.py/` + Ministerio del Interior + occasional INE studies.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1950 (casco histórico Asunción + Areguá + Concepción)** | Lead paint, lead pipes, weak foundations possible, asbestos in roof reparaciones |
| **1950–1980** (Stroessner-era expansion) | Asbestos cement-fibre roofing (eternit equiv.) common; lead pipes in older barrios |
| **1980–2000** | Modernization wave; variable build quality; some asbestos persistence early 80s |
| **2000–2015** | Modern materials standard; condominio horizontal Ley 677/1960 + Ley 3.966/2010 governance applies |
| **Post-2017 (Ley 5.811/2017 Construction Code)** | Modern build standards enforced; verify habilitación final municipal |

⚠️ **Asbestos**: Paraguay regulates but did not fully ban — verify eternit roofs on inspection. Lead in older plumbing checked via simple test kits.

### Mandatory diagnostics + due-diligence at sale

| Document | Required because | Source |
|---|---|---|
| **Estudio de títulos (chain ≥ 30 yrs typical)** | Verify 30-year title chain — escribano + abogado practice | DGRP `https://www.pj.gov.py/contenido/144` |
| **Certificado de Condiciones de Dominio (CCD) / Informe Registral** | Confirms current title + gravámenes (hipotecas, embargos) | DGRP — paid consulta |
| **CCC + valor fiscal SNC** | Cadastral reference + tax base | SNC `https://www.catastro.gov.py/` |
| **Certificado de no adeudo Impuesto Inmobiliario** | No outstanding municipal property tax | Municipalidad |
| **Certificado de no adeudo ESSAP** (water) | No water utility debts | ESSAP `https://www.essap.com.py/` (or per-municipio operator) |
| **Certificado de no adeudo ANDE** (electricity) | No electric utility debts | ANDE `https://www.ande.gov.py/` |
| **Certificado de no adeudo tasas municipales** | Limpieza, alumbrado, recolección | Municipalidad |
| **Reglamento de copropiedad + acta de asamblea (PH)** | If condominio horizontal: verify governance, expensas debts, fund balance | Administración del edificio |
| **Habilitación Bomberos (commercial)** | Required for commercial uses | Cuerpo de Bomberos |
| **Plano de obra aprobado + final de obra** | Verify habilitación municipal of construction | Municipalidad — Dirección de Obras |
| **Ley 2.532/2005 verificación zona de frontera** (foreign buyer + rural finca) | Confirms property is NOT in 50 km border-zone-rural restriction | DGRP + INDERT |
| **Certificado INDERT (rural)** | No agrarian-reform claim or pendencia | INDERT `https://www.indert.gov.py/` |

**Critical**: The **escribano público** conducts the **estudio de títulos** with a **collaborating abogado**. Buyer should engage **independent abogado** for parallel review (not the seller's). Foreign buyers should verify escribano membership at **Colegio de Escribanos del Paraguay** (`http://www.cep.org.py/`).

### Climate change projections (DINAC + IPCC AR6 + WB Climate Knowledge Portal)

- **+1.5 to +3.0 °C** by 2050 vs 1981–2010 baseline (depending on SSP) — Paraguay is one of the more strongly-warming inland zones globally.
- **Drought severity rising**: Chaco + western departamentos projected to see longer dry spells + reduced predictability.
- **Heavy precipitation events**: Río Paraguay + Río Paraná basin floods projected to increase in frequency + intensity.
- **Heat waves**: Asunción + central PY — +10–20 days/year >35°C by 2050 (DINAC + IPCC projections).
- **Wildfire frequency**: Chaco + Cerrado fire-weather-index trending up substantially; 2019–2020 + 2024 events foreshadow.
- **Hydroelectric dependence**: Itaipú + Yacyretá hydropower output sensitive to Paraná-Paraguay basin flows; long-term drought risk to national energy mix.

---

## Section: `--mains`

### National + regional operators

- **ESSAP — Empresa de Servicios Sanitarios del Paraguay**: `https://www.essap.com.py/` — state-owned national water + sanitation utility (urban Asunción + selected cities).
- **SENASA — Servicio Nacional de Saneamiento Ambiental**: `https://www.senasa.gov.py/` — rural + small-town water systems (Juntas de Saneamiento, community-managed).
- **ERSSAN — Ente Regulador de Servicios Sanitarios** (`https://www.erssan.gov.py/`): regulator for water + sanitation operators.
- **Aguatería privadas**: in some interior cities + suburbs, private aguaterías hold concessions (regulated by ERSSAN).

### Coverage (per ERSSAN + ESSAP 2023–2024 reports)

- **Drinking water**: ~85 % nationwide population (urban ~95 %, rural ~75 %).
- **Sewer / saneamiento**: **dramatic gap** — only ~15 % nationwide population on collective sewer (ESSAP/ERSSAN data). **Asunción ~50 %** in central + premium distritos; **interior cities <30 %** typical; **rural <5 %**. Most properties rely on **pozo ciego / cámara séptica + pozo absorbente** for sewage.

### Regional / municipal

- **Asunción central + Carmelitas + Villa Morra + Mariscal López + Las Mercedes + Sajonia + Trinidad**: ESSAP water near-universal; sewer collective in central distritos, expanding to Las Mercedes / Villa Morra; **older + outlying distritos still on cámara séptica**.
- **Lambaré, San Lorenzo, Fernando de la Mora, Luque, Capiatá**: ESSAP water yes; sewer **partial** — many lots still cámara séptica.
- **Ciudad del Este**: ESSAP water + selected sewer; outer Km zones rely on pozo + cámara séptica.
- **Encarnación**: ESSAP water + central sewer; outer barrios mixed.
- **Filadelfia + Loma Plata** (Mennonite Chaco): **own cooperativa-managed water + sanitation** (Cooperativa Chortitzer / Fernheim infrastructure); separate from ESSAP.
- **Interior tier-2 + rural**: SENASA Juntas de Saneamiento + private wells (pozo + bomba) common.

### Verification

1. Check **ESSAP cobertura por zona** + ERSSAN operator registry per municipio.
2. Listing language:
   - "agua corriente ESSAP" / "agua de red" / "saneamiento ESSAP" / "alcantarillado sanitario" = mains
   - "pozo + bomba" / "pozo artesiano" = own well + pump (no mains water)
   - "cámara séptica" / "pozo ciego" / "pozo absorbente" / "fosa séptica" = septic / cesspit (no mains sewer — extremely common)
3. Request **certificado de no adeudo ESSAP** as part of pre-escritura (mandatory diligence).
4. **Municipalidad de Asunción Dirección de Saneamiento** + per-municipio Obras Públicas can confirm collector existence in street.

### Costs (2026 USD est. — verify with installer)

| Scenario | Cost |
|---|---:|
| ESSAP connection (water + sewer) where available | USD 500–2,500 (conexión + tasa + obra civil) |
| Saneamiento extension to lot (if collector exists in street) | USD 1,500–5,000 |
| New cámara séptica + pozo absorbente (lot off-grid for sewer) | USD 1,500–4,000 |
| Pozo de agua perforado + bomba + tanque elevado | USD 1,500–4,500 |
| Replace pozo ciego + cámara séptica with biofiltro modern | USD 3,000–8,000 |

(2026 estimates from informal contractor + InfoCasas-listed services — verify with 2–3 quotes.)

---

## Section: `--crime`

### Primary sources

- **Policía Nacional del Paraguay**: `https://www.policianacional.gov.py/` — institutional reports; statistics published intermittently.
- **Ministerio del Interior — Estadísticas**: `https://www.mdi.gov.py/` — national security data.
- **Observatorio de Seguridad Pública** (Min Interior): selected studies, Asunción metro focus.
- **INE / DGEEC ECPV** (Encuesta de Calidad de Vida): occasional victimization indicators.

⚠️ **Crime data granularity is LOW** — Paraguay does not publish parcel/barrio-level rates equivalent to UY Sistema de Información Criminal or CO Indicadores Operativos. Rely on **departamento-level data** + **qualitative neighborhood reputation** + **journalistic coverage** (ABC Color, Última Hora, La Nación PY).

### Verdict bands (qualitative — calibrated to LATAM peers)

- 🟢 Asunción premium distritos (Carmelitas, Villa Morra, Mariscal López, Las Mercedes, Manorá), Filadelfia/Loma Plata, San Bernardino, Areguá
- 🟡 Asunción mid-tier (Sajonia, Trinidad, Recoleta), Lambaré, San Lorenzo central, Encarnación centro, Asunción premium apartments overall
- 🟠 Asunción outlying (Tacumbú, Bañado Sur edges), CDE outer zones, Pedro Juan Caballero centro, Salto del Guairá
- 🔴 Pedro Juan Caballero outer / cross-border zones (drug-trafficking corridors), Bañado Sur informal (also high flood risk), CDE specific high-counterfeit zones

### Walking-around safety

Asunción premium zones safe daytime + most evening hours; standard urban-LATAM situational awareness recommended. Border cities (CDE, PJC, Salto) require additional caution — avoid cross-border outer zones at night.

### Confidence

**MEDIUM** — official statistics infrequent; reliance on qualitative + journalistic sources elevates uncertainty. Trends 2018–2026 generally improving in Asunción metro per Min Interior; mixed in border zones.

---

## Section: `--amenities`

Universal OSM Overpass logic (`shared/amenities-osm.md`) applies. Country-specific notes:

- **Brand recognition (supermarkets)**: **Stock**, **Real**, **Superseis**, **Salemma**, **Casa Rica**, **Areté Supermercados**, **Biggie** (24h chain — Asunción ubiquitous), **Fortis** (premium small-format).
- **DIY / hardware**: **Sodimac Constructor Paraguay**, **Easy Paraguay** (Cencosud), **Codipar**, **Industria Park** (industrial).
- **Pharmacy**: **Punto Farma**, **Catedral**, **Salutaria**, **Sanatorio Migone Pharmacy**; small-town **boticas independientes** common.
- **Hospital network**:
  - **Public**: **MSPBS — Ministerio de Salud Pública y Bienestar Social** hospitals + **IPS — Instituto de Previsión Social** (workers' insurance hospital network; Hospital Central IPS Asunción flagship).
  - **Private**: **Sanatorio Migone**, **Hospital Bautista**, **Sanatorio La Costa**, **Hospital Italiano Asunción**, **Hospital Privado del Sur** (Encarnación).
- **Schools**: public **MEC — Ministerio de Educación y Ciencias** schools; private dominant in Asunción premium (Colegio Internacional, Colegio del Sol, ASA — American School of Asunción, Goethe-Schule, Lycée Marcel Pagnol).
- **Public transport**: **bus** dominant (no metro/tram in Asunción as of 2026; **Metrobús** corridor partially built — verify status); **DINATRAN** regulates intercity.
- **Airports**: **Silvio Pettirossi (Asunción ASU)** — main international; **Guaraní (Ciudad del Este AGT)** — secondary international; **Capitán Carmelo Peralta (Encarnación)** — domestic.

⚠️ OSM coverage in Paraguay is **patchier than EU**; cross-check rural results via Google Maps + Waze before signing.

---

## Section: `--climate`

Universal Copernicus / IPCC AR6 logic (`shared/climate-projections.md`) applies. Country-specific notes:

- **Köppen-Geiger zones**: most of Paraguay = **Cfa** (humid subtropical), Chaco western = **BSh** (semi-arid hot steppe) transitioning to **Aw** (tropical savanna) in northern Chaco.
- **Coastal**: Paraguay is **fully landlocked** → no SLR exposure; flood/drought are dominant climate stressors instead.
- **Reference**: 1981–2010 baseline → 2050 / 2100 (DINAC + WB CKP).

### Temperature trajectory (Asunción central, est.)

| Metric | Baseline | 2050 SSP2-4.5 | 2050 SSP5-8.5 | 2100 SSP5-8.5 |
|---|---|---|---|---|
| Annual mean | ~22 °C | +1.5 °C | +2.0 °C | +4.0 °C |
| Days TX≥35°C | ~30/yr | +10–15/yr | +15–25/yr | +50–80/yr |
| Tropical nights TN≥20°C | ~150/yr | +20/yr | +30/yr | +60/yr |

### Drought / wildfire / degree-days

- **SPEI** (Standardized Precipitation-Evapotranspiration Index): trending negative in Chaco + western PY → drying.
- **FWI** (Fire Weather Index): +20–40 % by 2050 in Chaco / Cerrado regions.
- **CDD shift** (cooling degree-days): +30–60 % by 2050 → A/C demand surge implications for energy bills.
- **HDD**: minimal (PY heating demand low; modest winter Jun–Aug).

### Verdict (default Asunción metro)

🟡 **Watch** — meaningful warming + wildfire/drought trends, but no acute coastal/seismic exposure; A/C costs + heat resilience are primary planning items.

🟠 **Adapt** for Chaco / Filadelfia / Loma Plata + Pilar floodplain — drought + heat + flood compound exposure.

### Confidence

**MEDIUM** — DINAC + IPCC AR6 frame solid; per-finca downscaling not available.

---

## Section: `--finance`

### Mortgage market (resident vs non-resident)

**Major lenders** (regulados por **Superintendencia de Bancos del BCP** — `https://www.bcp.gov.py/superintendencia-de-bancos/`):
- **Banco Nacional de Fomento (BNF)** — state — `https://www.bnf.gov.py/`
- **Banco Itaú Paraguay** — `https://www.itau.com.py/`
- **Banco Continental** — `https://www.bancontinental.com.py/`
- **Banco Atlas** — `https://www.bancoatlas.com.py/`
- **Banco Familiar** — `https://www.familiar.com.py/`
- **Sudameris Bank** — `https://www.sudameris.com.py/`
- **Visión Banco**, **Regional**, **GNB Paraguay**, **Banco Río** — others.

### Tasas hipotecarias típicas (2026)

- **PYG (guaraní)**: ~**8–15 %** anual (variable o fija — verify daily at BCP Superintendencia de Bancos publicaciones).
- **USD**: ~**6–9 %** anual.
- **EUR**: available at selected banks (Itaú, Continental) — ~5–8 %.
- **Plazo**: hasta **20–25 años** resident; **10–15 años** non-resident.

### LTV típico

- **Resident paraguayo / extranjero con cédula RUE permanente**: **70 %** standard; up to 80 % at BNF for vivienda primera (programs FONAVIS/AVI eligible).
- **Non-resident extranjero**: **50 %** typical; require depósito en banco PY + estados de cuenta + carta no-adeudo de banco origen + verificación AML/UIF.

### Multi-currency

- **Itaú PY + Continental + Atlas** offer **PYG / USD / EUR** mortgage products — match-currency-to-income recommended.
- **Conversion clauses**: some PYG mortgages have USD-conversion options (rate caps + spreads); verify reglamento.

### Programs (resident-focused)

- **FONAVIS — Fondo Nacional de la Vivienda Social**: subsidio MUVH for vivienda VIS — `https://www.muvh.gov.py/`.
- **AVI — Programa Asistencia para la Vivienda Individual**: subsidio MUVH for first-time buyers (verify income tope + 2026 cuota).
- **BNF Crédito Hipotecario**: state-backed, longer plazo + reduced rates for vivienda primera + clase media.

### Trampas

- **PYG depreciation risk if mortgage USD + income PYG**: managed-float guaraní stable historically (3–5 % annual depreciation typical) but mismatch elevates real cost.
- **Seguro desgravamen + seguro vivienda**: obligatorio con hipoteca; ~0.05–0.15 % monthly on saldo.
- **Tasa fija vs variable**: BCP policy rate driver — historic peaks 2022 (8.5 %) → cuts toward 6.0 % 2024–2025.

### Cost benchmark (Asunción Villa Morra apartment 100 m² @ USD 1,800/m² = USD 180,000)

- **Down 30 %**: USD 54,000
- **Préstamo USD 126,000 @ 7.5 % a 20 años**: cuota ~USD 1,015/mes
- **Cuota PYG @ 11 % a 20 años (eligibles BNF)**: PYG ~PYG 9–10 M/mes (verify simulador BNF/Itaú)

**Confidence**: HIGH for BCP-regulated framework + lender list. MEDIUM for current 2026 tasas (verify daily BCP Superintendencia).

---

## Section: `--currency`

### Currency baseline

- **PYG — guaraní paraguayo** (símbolo ₲, ISO 4217 PYG). One of South America's longest-running stable currencies post-1990s.
- **Régimen cambiario**: **flotación administrada**; BCP intervenes selectively at Mesa de Cambios; no fixed peg.
- **Capital controls**: **none significantly** at retail level; inbound/outbound transfers free in either currency.
- **Reporting**: **SEPRELAD — Secretaría de Prevención de Lavado de Dinero o Bienes** (`https://www.seprelad.gov.py/`) + SET reporte for transactions >USD 10,000 inflow/outflow (Ley 1.015/1997 + Ley 6.452/2019 amendments). Banks ROS automatic.

### USD usage

- **Pricing**: ~30–50 % of Asunción premium + Ciudad del Este commercial RE listings priced in **USD**. Lower-tier + provincial in PYG dominantly.
- **Notarial escritura**: can be denominated in either USD or PYG; conversion at BCP tipo de cambio publicado on day of escritura for tax base.
- **Banks**: dual-currency accounts standard at all major banks; ATM dispense in both PYG + USD.
- **Origen**: legacy of 1980s–90s regional inflationary dynamics + cross-border trade with Brazil (Real) + Argentina (Peso) — guaraní + USD parallel pricing entrenched.

### Rate history + outlook

- **PYG/USD 2020–2026 range**: ~6,500 (2020 floor) → ~7,800 (2024 peak) → ~7,200–7,500 (2025–2026 stabilizing) — verify current at BCP.
- **BCP policy rate**: ~6.00 % (Q1 2026 — verify monthly Programa Monetario `https://www.bcp.gov.py/`); peaked 8.50 % in 2022, sequential cuts 2023–2025.
- **Inflation target**: **4 % ± 2 %** per BCP charter; 2024–2025 within band post-2022–23 spike.

### For property buyers

- **Match currency**: prefer PYG mortgage if income PYG; USD mortgage if foreign income.
- **Hedge tools**: forward FX + options available at Itaú/Continental/Atlas for >USD 50,000 transactions; spreads 0.5–1.5 %.
- **Inbound transfer**: SWIFT to PY bank account; SEPRELAD reporting >USD 10,000 — entirely legal but documented; AML KYC mandatory.
- **Outbound on resale**: no restriction; IRP/IRE settled at notary + cleared escritura → full USD repatriation legal.

### Mercosur context

- Paraguay is a **Mercosur founding member** (Tratado de Asunción 1991); regional currency harmonisation discussions periodic but **no Mercosur common currency** as of 2026.
- Cross-border (BR / AR) shopping flows from Ciudad del Este / Encarnación drive USD + Real + Peso dynamics in border RE.

**Confidence**: HIGH — BCP managed float + minimal capital controls is well-documented + stable framework since post-1990s reforms.

---

## Section: `--visa`

### Primary authority

- **DNM — Dirección Nacional de Migraciones (ex-DGM)** under Ministerio del Interior: `https://www.migraciones.gov.py/` — visa enforcement + RUE (Residente) issuance.
- **MRE — Ministerio de Relaciones Exteriores**: `https://www.mre.gov.py/` — visa application via consulados.
- **SUACE — Sistema Unificado de Apertura y Cierre de Empresas**: `https://www.suace.gov.py/` — investor track support.
- Legal basis: **Ley 6984/2022 — Nueva Ley de Migraciones** (repealed Ley 978/1996; Decreto 18.295/1997 reglamento no longer in force) + **Resolución SET 1186/2023** (now administered by DNIT, residency tightening 2023). See country profile reforms anchor.

### Major visa pathways

#### 1. RUE — Residencia Permanente (Permanent Residency)

**Pre-2023 regime** (now historic):
- USD ~5,200 deposit at BNF + DGM application + clean record → 90 days to RUE issuance.
- **One of the world's cheapest formal RBI** paths globally — hugely popular 2018–2022.

**Post-2023 (Resolución SET 1186/2023)** — current regime:
- Applicant must demonstrate **EITHER**:
  - **(a)** Active **SET RUC + economic activity** in PY (e.g., self-employed, consulting, remote-work sourced abroad with PY tax registration), OR
  - **(b)** **Investment ≥ USD 70,000** in business via SUACE with business plan + commitment.
- Plus: clean criminal record (apostille from country of origin), birth certificate apostille, health certificate.
- **Processing time**: ~3–9 months (variable per DGM workload).
- **Status**: still **among the cheapest formal RBI in South America**; tightened but remains accessible vs Portugal/Spain (USD 250k+ thresholds) and Uruguay (USD 525k RE pathway).

#### 2. SUACE Investor track

- ≥ USD 70,000 PY business investment (incorporación EAS/SA/SRL) + business plan.
- Faster track + investor visa label; renewable.

#### 3. Mercosur visa

- Convenio Mercosur (Resolución MERCOSUR/CMC/Dec 28/02 + complementarias) — nacionales **AR/BO/BR/CL/CO/EC/PE/UY** (+ asociados) → **Visa Temporaria Mercosur** with simplified docs → ruta a Permanente tras 24 meses.

#### 4. Family-link

- Cónyuge paraguayo + hijos: ruta directa con docs apostillados.

#### 5. Naturalisation → Paraguayan passport

- **3 años continuos de Residencia Permanente** + Spanish OR Guaraní + integración + sin antecedentes → naturalización (Constitución art. 148).
- Among the **fastest naturalisation paths globally** (vs UY 3y, AR 2y residency-only-time, but longer process; PT 5y; ES 10y).

### NO real-estate-only visa

⚠️ Historically Paraguay had **NO "golden visa" via residential RE alone** equivalent to PT/ES/UY 19.937 / GR / MT. As of May 2026 the **Paraguay Investor Pass** changes this — **USD 200,000 in qualifying real-estate projects now grants direct permanent residency** (see reforms anchor, line 24). The legacy RUE route still requires coupling RE with business activity / SUACE investment / RUC.

### Cédula de Identidad para Extranjeros

- Once RUE granted, **DGM issues Cédula de Identidad Paraguaya** (extranjero permanente).
- Permits opening RUC, contratación laboral, banking, conducir, voto en elecciones municipales (con condiciones).

**Confidence**: HIGH — Ley 6984/2022 (current migration law) + DGM/DNM framework + Resolución SET 1186/2023 (DNIT-administered) documented + multiple sources confirm. MEDIUM for processing time (varies per DGM/DNM workload + applicant nationality).

---

## Section: `--insurance`

### Regulator

- **Superintendencia de Seguros (SIS)** under BCP — `https://www.bcp.gov.py/superintendencia-de-seguros/`.
- **APCS — Asociación Paraguaya de Compañías de Seguros**: `https://apcs.org.py/` — gremio.

### Major insurers (RE-relevant)

- **Mapfre Paraguay** — `https://www.mapfre.com.py/`
- **La Consolidada** — `https://www.laconsolidada.com.py/`
- **Aseguradora Tajy**
- **Patria Seguros**
- **Aseguradora Yacyretá** (state-linked)
- **El Sol del Paraguay**

### Coverage required / typical

- **Seguro de Desgravamen** (mortgage life insurance): obligatorio con hipoteca; cubre saldo en caso fallecimiento titular. ~0.04–0.08 % monthly on saldo.
- **Seguro contra Todo Riesgo (incendio + daños + robo)**: typically required with hipoteca; voluntario without. ~0.10–0.30 % anual sobre valor asegurado.
- **Inundación**: not always included in standard policy; addable as rider — critical for **Pilar / Bañado Sur Asunción / floodplain Río Paraguay** properties.
- **Incendio Chaco / Cerrado wildfire**: not typically excluded but verify coverage for properties in fire-prone zones.
- **Sismo**: minimal relevance (low seismicity); typically not separately rated.

### Sin hipoteca

- Sin hipoteca, **el seguro vivienda NO es obligatorio** legalmente; voluntario. Penetración baja (<20 % viviendas formales aseguradas — APCS estimate).

### Trampas

- **Flood deducible**: revise el deducible para zonas inundables — Pilar / Bañado Sur con eventos recurrentes pueden exceder cobertura standard.
- **Pre-1980 builds**: aseguradoras pueden requerir certificación estructural o aplicar surcharge.
- **HOA-level seguro**: edificios bajo Ley 677/1960 + Ley 3.966/2010 (PH régimen) often have seguro for áreas comunes; verify reglamento + balance fund.

**Confidence**: HIGH for SIS regulatory framework. MEDIUM for tasas exactas (variable per perfil + zona).

---

## Section: `--notary`

### Notarial framework

- **Ley 879/1981 — Código de Organización Judicial** (Tít. IV, Cap. III — Escribanos).
- **Ley 1.190/1985 — Ley del Notariado** + arancel notarial reglamentario (verify current at Colegio).
- **Colegio de Escribanos del Paraguay** + Corte Suprema oversight.
- **Notario público**: profesional jurídico autorizado por la Corte Suprema, ejerce fe pública, custodio del archivo notarial. Numero limitado por circunscripción notarial.

### Process — typical RE purchase

1. **Preliminary acuerdo** (boleto de compraventa) — borrador escritura redactado por abogado / escribano; firmado entre partes con seña típica 10–30 % precio.
2. **Escribano revisa boleto + verifica documentos**:
   - Informe Registral DGRP (CCD per finca + matrícula)
   - Cuenta Corriente Catastral SNC + valor fiscal
   - Certificado no adeudo Impuesto Inmobiliario (Municipalidad)
   - Certificado no adeudo ESSAP + ANDE + tasas municipales
   - Cédula de identidad / pasaporte de las partes
   - Estatutos + acta de directorio si parte juridica
   - Reglamento de copropiedad + acta asamblea (PH)
3. **Verificación zona de frontera 50 km** (Ley 2.532/2005) si comprador extranjero + finca rural.
4. **SEPRELAD reporte** automático si transacción >USD 10,000 (Ley 1.015/1997 + 6.452/2019).
5. **Escritura pública** firmada en presencia escribano + testigos si requerido + funcionario fiscal eventual.
6. **Escribano presenta para inscripción a DGRP — Registro Inmobiliario**.
7. **DGRP califica** (5–30 días hábiles típicos); inscribe → emite anotación + matrícula actualizada.
8. **Escribano entrega copia legalizada de escritura + matrícula actualizada** al comprador.

### Costs

- **Honorarios notariales**: ~**0.5–2.0 %** del precio (escala notarial + complejidad).
- **DGRP — Inscripción registral**: ~PYG 200,000–500,000 fijo + small ad valorem.
- **IVA 10 %** sobre honorarios notariales + comisión.
- **Total notario + DGRP**: ~**1.0–2.5 %** del precio (lower than UY ITP 4 % or AR sellos 3.5 %).

### Trampas

- **Doble venta**: mitigated by DGRP bloqueo registral while matrícula in trámite + due diligence pre-firma con CCD fresco (mismo día firma).
- **Falsa identidad vendedor**: escribano verifica cédula contra **DRGP/RNV cross-check + biométrico cuando posible** — pero falsificación posible; pedir cédula física + cotejar.
- **Sustitución partes en boleto**: only firmar con boleto cargado al escribano directamente; no aceptar borradores externos cambiados a último minuto.
- **Border-zone (50 km) trampa**: foreign buyer + rural finca within 50 km of border = **transaction VOID under Ley 2.532/2005** — escribano must verify; some informal historical workarounds via PY-shell entities have been challenged in court 2018–2024.

**Confidence**: HIGH — Ley 879/1981 + Ley 1.190/1985 framework stable; DGRP electronic gradual reduces falsa-identidad risk vs pre-2010s.

---

## Section: `--compare`

### Mercosur + Andean comparison (PY / UY / AR / BR-region)

| Dimension | Paraguay | Uruguay | Argentina | Brazil |
|---|---|---|---|---|
| Foreign-buyer regime | Open with 50 km border-zone rural restriction (Ley 2.532/2005) | Fully open (no restrictions) | Open with security-zone restrictions Tierra del Fuego/border | Open + 25 km border-zone INCRA approval rural |
| Currency / inflation | PYG managed float; 3–5 % typical | UYU/USD pricing; 5–8 % | ARS very volatile; high inflation | BRL flotation; 4–6 % |
| Cadastre quality | DGRP + SNC mejorando, gap parcel-vs-fiscal | DNC mature, 30-60 % VRC gap | Catastros provinciales + RNRA mixed | INCRA + SREN gradual catastro |
| Property tax (annual) | Impuesto Inmobiliario 1.0 % of valor fiscal | Contribución 0.25–1.4 % of VRC | Inmobiliario provincial 0.5–2 % | IPTU municipal 0.3–1.5 % |
| Transfer tax / closing costs | ~1.5–4 % buyer side (no general transfer tax) | ~6–9 % buyer side (4 % ITP split) | ~4–6 % buyer side (sellos provinciales) | ~5–7 % buyer side (ITBI + cartório) |
| CGT (resident) | 8 % flat × 30 % presumption ≈ 2.4 % effective; primary residence 2y exempt | 12 % indexed gain | Renta financiera + cedular | IR ganho de capital 15–22.5 % progressive |
| Mortgage rates 2026 | 8–15 % PYG / 6–9 % USD | UI-indexed BHU 3.5–7 % real | ARS punitive; UVA programs evolving | SFH BR ~10–12 % nominal |
| STR regulation | SENATUR + municipal light | Decreto 384/2018 + Maldonado emerging | Buenos Aires evolving | Cidade-level (RJ + SP varies) |
| Investor visa | RUE post-2023 USD 70k SUACE; cheapest formal RBI region | Tax-residency UI 3.5M ≈ USD 525k + 60d | Various Argentine residency tracks | Fixed visa investor BRL 700k+ |
| Naturalisation timeline | 3y from PR → passport (Const. art. 148) | 3y residency → naturalisation | 2y residency → ciudadanía | 4y residency typical |

### Asunción vs other regional capitals

| Metric | Asunción PY | Montevideo UY | Buenos Aires AR | São Paulo BR |
|---|---:|---:|---:|---:|
| Premium $/m² (top distrito) | ~$2,500 (Carmelitas/Villa Morra) | ~$4,000 (Carrasco/Punta Carretas) | ~$2,500 (Recoleta/Palermo) | ~$3,500 (Jardins/Itaim) |
| Population metro | ~3.0 M | ~1.9 M | ~15.5 M | ~22.5 M |
| Seismic risk | 🟢 Negligible | 🟢 Negligible | 🟢 Low | 🟢 Low |
| Flood risk | 🟠 Bañado Sur + Pilar floodplains | 🟡 Río de la Plata estuary low-lying | 🟡 Riachuelo zones | 🟡 Tietê várzea |
| Climate | 🟡 Cfa subtropical, hot summers | 🟢 Cfa mild oceanic | 🟢 Pampas mild | 🟡 Tropical altitude |
| Cost-of-living anchor | LOW (cheapest of comparison) | MID-HIGH | MID (volatile) | HIGH |

---

## Section: `--retirement`

### RUE Permanente (post-2023)

(detailed in `--visa`): SET RUC + economic activity OR USD 70,000 SUACE business investment. After 3 years RUE → naturalisation eligibility.

### Cost-of-living anchor (Asunción Carmelitas/Villa Morra 2026, single retiree)

- Rent (1BR Carmelitas/Villa Morra): USD 600–1,200/mo
- Utilities + internet: USD 80–180/mo
- Groceries + dining: USD 350–700/mo
- Healthcare (private clinic seguro): USD 80–250/mo
- Transport: USD 50–150/mo (taxi / Uber / MUV; bus low cost)
- **Total estimate single Asunción**: **USD 1,200–2,500/mo**

Provincial cities (Encarnación, Ciudad del Este interior, San Bernardino): ~30–50 % cheaper than Asunción.

### Healthcare

- **MSPBS público**: free at point of use; quality variable; long waits in Tier-2 hospitals.
- **IPS — Instituto de Previsión Social**: contributory social insurance for workers; foreign retirees not eligible unless employed locally.
- **Private clinics Asunción**: Sanatorio Migone, Hospital Bautista, Sanatorio La Costa, Hospital Italiano, Hospital Privado del Sur (Encarnación), Hospital Adventista del Paraguay — mid-to-high quality; out-of-pocket or private seguro (Mapfre / Patria / La Consolidada planes USD 80–350/mo).
- **Medical tourism inflow** from BR border driven by lower-cost dental + general — quality acceptable in urban centers.

### Pension taxation

- **Foreign pension** received in PY by **non-residente fiscal** (<183 days + no domiciliación): NOT taxed in Paraguay (territorial-source IRP — Ley 6.380/2019 favors PY-source income).
- **Domiciliado fiscal** (>183 days + center of vital interests): foreign pension may be taxed if classified as PY-source under Ley 6.380/2019; **Paraguay's tax base remains essentially territorial** for individuals — foreign-pension passive income often **NOT taxed** in PY even for residents.
- **No CDIs** (convenios doble tributación) with major pension-source countries (US, EU, UK) — but territorial-source design typically prevents double taxation regardless. Verify with contador.

### Strategic notes

- Paraguay is **one of the cheapest formal retirement destinations in South America** post-2023 RUE tightening.
- **Health system**: lower-quality vs UY/CL; private insurance + premium clinic access compensates.
- **Climate**: hot subtropical — A/C important; Filadelfia / Chaco hotter still.
- **Language**: Spanish dominant; Guaraní cultural lingua franca; English limited outside premium Asunción + tourism.
- **Expat community**: small but growing — mostly business-investor + remote-worker driven; AR + BR cross-border retiree flow.

**Confidence**: HIGH for visa + pension territorial-source frame. MEDIUM for cost estimates (variable per lifestyle).

---

## Section: `--digital-nomad`

### No specific "digital nomad visa" framework

Paraguay as of 2026-05 has **no dedicated digital-nomad visa** comparable to PT D8 / ES DN / CR DN. Nomads typically use:

- **Visa de turista**: most nationalities can enter visa-free or with on-arrival stamp; typically up to 90 days, extendable to 180 days at DGM. Tolerated for remote-work for foreign employer in practice but no legal cover.
- **RUE Permanente** (post-2023): USD 70k SUACE business investment OR SET RUC + economic activity → full residency.
- **Mercosur visa** for AR/BO/BR/CL/CO/EC/PE/UY — easier residencia path.

### Key remote-work realities

- **Internet**: Asunción Carmelitas/Villa Morra/Mariscal López have high-quality fibre (**Tigo Star**, **Personal Flow**, **Vox**, **Copaco**) — 200 Mbps–1 Gbps PYG 250k–600k/mo (~USD 35–80). Provincial Tier-2 cities reasonable; Chaco rural patchy.
- **Coworking density**: Asunción Carmelitas/Villa Morra/Las Carmelitas highest — **Asuncion CoWork**, **DataLab Paraguay**, **The Office Paraguay**, **Workity**. Encarnación + CDE thinner.
- **Time zones**: PY = **GMT-4** (no DST since 2024 simplification) — aligned with US Eastern (winter) / overlap US/CA workdays.
- **Tax**: tourist visa <183 days = non-residente fiscal; foreign-source remote-work income NOT taxed in Paraguay (territorial-source design).
- **Itaipú/Yacyretá energy surplus** → Paraguay is among world's #2 net electricity exporters → low industrial electricity costs → **growing crypto-mining + server-farm cluster** in Ciudad del Este + Alto Paraná region (esp. post-2020 BTC wave). Potential remote-work / digital-asset demographic.

### Lifestyle hotspots

- **Asunción** (Carmelitas / Villa Morra / Manorá / Las Mercedes): coworking + safety + amenity dense.
- **Encarnación Costanera**: scenic riverfront + lower COL; tourism + university energy.
- **San Bernardino + Areguá** (Lago Ypacaraí): traditional weekend community; lakeside lifestyle.
- **Ciudad del Este**: cross-border BR/AR commerce + crypto/server-farm ecosystem.
- **Filadelfia (Chaco)**: distinctive German-Mennonite community; exotic but isolated.

**Confidence**: MEDIUM — no dedicated DN visa; tourist + RUE frameworks documented but DN-specific tax treatment ambiguous (defaults to favorable territorial-source).

---

## Section: `--macro`

### Macro indicators (BCP + INE)

- **GDP growth 2024**: ~3.8 % (BCP / INE) — recovery after 2022 drought-driven contraction.
- **GDP growth 2025 est.**: ~3.5–4.0 % (BCP Informe Económico — verify current `https://www.bcp.gov.py/`).
- **Inflation (IPC Asunción Metropolitana)**: ~3.5–4.5 % YoY 2025 (within BCP 4 % ± 2 % target).
- **BCP policy rate**: ~6.00 % (Q1 2026 — verify monthly Programa Monetario).
- **Unemployment (urbano)**: ~6–7 % INE EPH; informal employment ~64 %.
- **PYG/USD**: ~7,200–7,500 range Q1 2026.
- **Sovereign credit rating**: **BB+** (S&P), **Ba1** (Moody's), **BB+** (Fitch) — at investment-grade threshold; outlook stable to positive 2024–2026.
- **EMBI+ Paraguay**: ~150–250 bps over US Treasury.

### Long-term drivers

- **Hydropower exports**: Itaipú (PY/BR) + Yacyretá (PY/AR) → Paraguay is **world's #2 net electricity exporter** (after Norway-equivalent baseline); 2024 Itaipú Annex C renegotiation rebalances royalty distribution → fiscal-space upside.
- **Soya + cattle agribusiness**: Mato Grosso do Sul border + Mennonite Chaco cattle → ~15–20 % GDP + ~50 % exports. China + EU demand cycle key driver.
- **Maquila industria (free-zone manufacturing)**: Ciudad del Este + Asunción periphery; growing under Ley 1.064/1997 maquila regime.
- **Crypto-mining + server farms**: post-2020 driven by surplus hydroelectricity; controversial (energy-pricing debates) but growing.
- **Demographic**: median age ~28 (one of South America's youngest); rising urbanization but modest pace.

### Risks

- **Itaipú Treaty Annex C** (re-negotiated 2023–2024, effective 2024+): structural shift in energy revenue sharing; positive net for PY but uncertainty on long-term flows.
- **Drought sensitivity (ENSO)**: 2022–2023 drought cut soya yields + hydropower output; 2024–2026 conditions improved but climate amplification risk persists.
- **Mennonite vs national integration**: peripheral but recurrent debates on Cooperativa autonomy + fiscal contribution.
- **Border-zone illicit economy**: drug + counterfeit + cigarette trafficking PJC / CDE / Salto del Guairá — fiscal + reputational drag; Mercosur cooperation gradual.

**Confidence**: HIGH for BCP + INE macro data; MEDIUM for forward GDP estimates (verify current Informe Económico BCP).

---

## Section: `--demographics`

### Population (INE 2024 mid-year est., projection 2022 census base)

- **National**: ~7.4 M
- **Asunción Distrito Capital**: ~520k
- **Asunción Metropolitan Area** (Asunción + Lambaré + San Lorenzo + Luque + Capiatá + Limpio + Mariano Roque Alonso + Fernando de la Mora + Ñemby + Villa Elisa): ~3.0 M (~40 % of national)
- **Ciudad del Este metro** (Alto Paraná): ~600k
- **Encarnación** (Itapúa): ~130k
- **Pedro Juan Caballero** (Amambay): ~120k
- **Coronel Oviedo** (Caaguazú): ~100k
- **Filadelfia + Loma Plata** (Chaco Mennonite): ~50k combined

### Age structure

- Median age: ~28 years (one of region's youngest)
- Under 15: ~28 %
- 65+: ~7 % (rising; pension transition emerging)

### Migration

- **Internal**: rural → urban (Asunción metro absorbing internal migration 1980s–2020s); current trend slowing but Asunción still net-positive.
- **External in**: Brazilian (especially Mato Grosso do Sul / Paraná) + Argentine cross-border + Asian (Korean + Taiwanese in Ciudad del Este commerce) flows; recent Venezuelan secondary inflow modest vs Peru/Colombia/Chile.
- **Paraguayan diaspora**: ~700k abroad (AR primary destination, ES, BR, US).

### Languages + culture

- **Spanish + Guaraní official** (Constitución art. 140); Guaraní first-language for ~30–35 % rural population, second for most urban Paraguayans.
- **Portuguese** widely spoken near BR border (CDE, PJC, Salto del Guairá) — sometimes near-majority street-level.
- **Plautdietsch / German** in Mennonite Chaco colonies (Filadelfia, Loma Plata, Neuland).
- **Asian communities**: Korean + Taiwanese commerce-focused in CDE + Asunción Mercado 4.

### Education

- **Literacy**: ~94 % adult.
- **Tertiary education**: variable; UNA (Universidad Nacional de Asunción) + UCA (Católica) + UAA (Autónoma) + UPAP private + UNAE (Encarnación) + UNCA (Caaguazú).

### Religion

- **Catholic**: ~85 % per INE — declining; **evangélica** ~10 % rising; Mennonite + smaller Protestant niches.

---

## Section: `--esg`

### Climate policy

- **NDC**: Paraguay submitted updated NDC under Paris Agreement — 20 % unconditional + 10 % conditional GEI reduction by 2030 vs BAU (UNFCCC submission 2021–2022). MADES leads — `https://www.mades.gov.py/`.
- **Plan Nacional de Cambio Climático** (PNCC): adaptation + mitigation framework.
- **Política Nacional de Cambio Climático (Ley 5.875/2017)**: legal framework.

### Energy mix

- **Generación eléctrica**: ~**99 %+ hidroeléctrica** (Itaipú + Yacyretá + Acaray). Among world's cleanest generation mixes (essentially zero fossil-fuel power).
- **Net export status**: Paraguay is **#2 net electricity exporter** globally (~80 % of Itaipú output exports to BR, ~40 % of Yacyretá to AR per treaty allocations).
- **Domestic transmission losses + informal connections**: gradual ANDE upgrades; ~12 % network losses.
- **Itaipú Annex C 2024 renegotiation**: rebalances royalties + tariff (PY share rising); fiscal-space implications.

### Building energy efficiency

- **Ley 5.811/2017 Construction Code** + **Norma Paraguaya** (NP IRAM mirror) — modern envelope standards.
- **No mandatory energy certificate** at sale (unlike Chile CEV from 2024 or EU EPC).
- **Voluntary EDGE certification** (IFC) used by some Asunción premium developers.

### Water + sanitation

- **ESSAP + SENASA + Aguaterías privadas** — coverage strong urban water (~95 %), gap rural + critical sewer gap (~15 % nationwide on collective sewer).
- **Sewage treatment Asunción**: ~Bahía Asunción project + selected interceptors; large fraction still discharges raw to Río Paraguay.
- **River-pollution exposure**: Bañado Sur + Bahía Asunción receive informal effluents; downstream impact on Río Paraguay quality.

### Forest + biodiversity

- **INFONA Forest Code** + Cerrado/Chaco deforestation tracking.
- **Chaco deforestation rate**: among world's highest (per Global Forest Watch + INFONA) — soy + cattle expansion driver.
- **Reserva forestal + áreas protegidas**: SINASIP (Sistema Nacional de Áreas Silvestres Protegidas) under MADES.
- **Mennonite cooperativa land** holds vast hectares — sustainability + indigenous-land debates recurrent.

### ESG considerations for buyers

- **Asunción urban property**: low direct ESG-flag exposure; energy mix essentially fully green.
- **Chaco / rural properties**: deforestation + indigenous-land + water-rights complications elevated; diligence on INDERT + INDI (Instituto Paraguayo del Indígena) status critical.
- **Mining + extractives**: limited in PY (vs PE/CL/CO/BR); minimal ESG drag from sector.

---

## Section: `--exit`

### Sale process for foreign owner (Asunción Villa Morra apartment, USD 200,000)

1. **Engage abogado + corredor inmobiliario**. Typical commission **3–5 % + IVA** seller-side.
2. **Listing on InfoCasas + Properati + Remax PY**; estimated marketing 3–9 months Asunción premium depending on distrito + price-to-market.
3. **Pre-sale documents**:
   - Informe Registral DGRP fresh CCD
   - CCC + valor fiscal SNC
   - Certificado no adeudo Impuesto Inmobiliario + ESSAP + ANDE + tasas municipales
   - Estado de cuenta de mantenimiento (administrador edificio, PH)
   - Recibos servicios al día
4. **Buyer offer** → boleto de compraventa (seña típica 10–30 % precio).
5. **Escribano engaged** (often buyer-selected); minuta drafted; due diligence by buyer abogado.
6. **Buyer pays balance + closing costs** at notary firma.
7. **Escritura pública** firmada notario.
8. **Notario inscribe DGRP — Registro Inmobiliario** — matrícula actualizada en ~5–30 días hábiles.

### Tax obligations on sale

- **Resident individual non-habitual**: **IRP 8 %** on 30 % of net gain (effective ~2.4 % gross gain). Primary residence after 2 years continuous use **may be exempt** under Decreto 9.371/2018.
- **Resident habitual** (frequent flipper): may be re-classified as IRE actividad empresarial 10 % flat on net.
- **Non-resident individual**: **IR retención by notary on gross sale** per SET resolution vigente (typically 4.5 % effective gross — verify with notary).
- **Corporate (SA/SRL/EAS)**: IRE 10 % on net gain + IDU 8 %/15 % on subsequent distributions.

### Repatriation

- **No capital controls**: USD or PYG proceeds wire-transferable abroad freely from PY bank account.
- **AML reporting**: bank reports >USD 10,000 to SEPRELAD automatically (Ley 1.015/1997 + 6.452/2019); legal + documented.
- **Foreign-currency conversion**: at BCP daily tipo de cambio or bank spot; spread typically 0.5–1.5 %.

### Liquidity reality

- **Asunción Carmelitas / Villa Morra / Mariscal López**: liquidity reasonable; 4–9 months typical sale for fairly priced premium units.
- **Asunción mid-tier** (Sajonia, Trinidad, Recoleta): 6–12 months.
- **Provincial Tier-2** (CDE / Encarnación / San Bernardino): 9–18 months.
- **Border-zone rural** (50 km): foreign-owner exit constrained — buyer pool restricted to Paraguayans; verificar before purchase.
- **Mennonite Chaco**: thinly-traded, semi-closed market; verify locally.

### Costs to seller (typical)

- Comisión inmobiliaria: 3–5 % + IVA 10 %
- IRP/IRE on net gain: ~2.4 % effective (resident) or ~4.5 % gross retención (non-resident)
- Escribano + DGRP: often shared or buyer-paid by negotiation
- **Net to seller**: ~92–95 % of gross precio venta after commission + tax (varies).

**Confidence**: HIGH — framework documented + standard; provincial liquidity LOW for underwriting purposes.

---

## Cost benchmarks (PY 2026)

| Concepto | Costo (PYG / USD / %) | Fuente |
|---|---:|---|
| **Impuesto Inmobiliario (annual, residential)** | **1.0 %** of valor fiscal | Ley 125/1991 |
| Tasa especial servicios municipales (Asunción) | PYG 200,000–800,000/yr | Ordenanza Municipalidad |
| Notario (escritura, ad valorem) | **0.5–2.0 %** of price | Ley 1.190/1985 |
| DGRP inscripción registral | PYG 200,000–500,000 + small ad val | TUPA DGRP |
| IVA on professional services | **10 %** | Ley 6.380/2019 |
| Estudio de títulos (abogado) | USD 300–1,500 | privado |
| Tasación banco (si hipoteca) | USD 100–400 | bancos |
| Seguro desgravamen + vivienda | ~0.10–0.30 % anual sobre valor | aseguradoras SIS |
| Comisión inmobiliaria | **3–5 % + IVA** seller-side typical | mercado |
| **Total transaction cost (buyer side)** | **~1.5–4 % of price** | sum of above |
| Renovación cocina (60 m²) | USD 5,000–15,000 | mid-range |
| Renovación baño completo | USD 1,500–5,000 | per baño |
| Pintura interior (100 m²) | USD 400–1,200 | labor + materiales |
| New cámara séptica + pozo absorbente | USD 1,500–4,000 | per lot |
| Pozo de agua perforado + bomba | USD 1,500–4,500 | per lot |

(2026 estimates; computed from customary % rates above + InfoCasas/Properati listings cross-checked. **Lower headline transaction cost** than UY/CO/AR due to absence of general transfer tax — main cost is notarial 0.5–2 % + comisión inmobiliaria seller-side.)

## Active fiscal incentives & programs (2025–2026)

- **Ley 60/1990 — Régimen de Incentivos Fiscales para la Inversión**: IRE/IDU/IVA exemptions for certified investment projects (>USD 5M typically) — historically the central PY incentives instrument. Source: MIC / SUACE.
- **Ley 5.542/2015 — Garantías para Inversiones**: 20-year tax stability commitment for qualifying projects.
- **Ley 1.064/1997 — Maquila**: free-zone-style manufacturing regime; 1 % flat tax on value-added; CDE + Asunción periphery hubs.
- **FONAVIS — Fondo Nacional de la Vivienda Social** (MUVH `https://www.muvh.gov.py/`): subsidy for VIS — first-time buyers below income tope.
- **AVI — Asistencia Vivienda Individual** (MUVH): subsidy + technical assistance for individual VIS construction.
- **BNF Crédito Hipotecario** (state-backed): longer plazo + reduced rates for vivienda primera + clase media.
- **IVA 5 % reduced** on social housing (vivienda VIS) — Ley 6.380/2019.
- **Itaipú/Yacyretá royalty distribution** (post-2024 Annex C): potential indirect fiscal-space benefit for municipal investments + housing programs.

## Common listing platforms

- InfoCasas Paraguay, Clasipar, MercadoLibre Inmuebles PY, Properati Paraguay, Remax Paraguay, Century 21 Paraguay, Coldwell Banker Paraguay.

## Caveats unique to PY

- **50 km border-zone rural restriction (Ley 2.532/2005)**: foreign individuals + foreign-controlled entities **CANNOT acquire RURAL land within 50 km of national borders** — affects significant portions of Itapúa, Alto Paraná, Amambay, Canindeyú, Concepción, Chaco departments. **Urban parcels in border cities OK**. Verify finca cadastral position pre-purchase.
- **No general property transfer tax**: closing costs ~1.5–4 % buyer side — **lower than UY (6–9 %), CO (2–4 %), AR (4–6 %)**.
- **Valor fiscal vs market gap is dramatic** (often 10–30 %): means Impuesto Inmobiliario is cheap (~0.1–0.3 % of market effective) but a future re-valuación is a long-discussed risk.
- **CGT effective rate ~2.4 % via 30 % presumption × 8 % IRP** for non-habitual sellers — among lowest in region. Primary residence after 2 years exempt under Decreto 9.371/2018.
- **Territorial-source IRP** for individuals: foreign passive income often **not taxed** even for residents — critical for retirement / digital-nomad planning.
- **RUE post-2023 (Resolución SET 1186)**: USD 70k SUACE business OR SET RUC + activity. Still **among cheapest formal RBI in South America**; 3 years RUE → naturalisation eligibility.
- **Legacy RUE has no RE-only route** (must couple with business activity / SUACE / RUC), BUT the **May-2026 Paraguay Investor Pass grants permanent residency for USD 200k in qualifying RE projects** (see line 24).
- **Mennonite Chaco semi-closed market**: Filadelfia + Loma Plata + Neuland — Cooperativa Chortitzer / Fernheim / Neuland-managed; outside investor entry limited.
- **Itaipú/Yacyretá hydropower surplus**: world's #2 net electricity exporter; **crypto-mining + server-farm cluster** growing in CDE + Alto Paraná.
- **Mainly civil-law notarial system + DGRP electronic gradual**: solid title-chain due diligence required (30y minimum); DGRP digital improvements 2018–2024 reduce fraud risk.
- **Strong USD parallel pricing convention** in Asunción premium + CDE + Encarnación tourism — verify currency-of-payment + escrow protocol.
- **Drought + wildfire amplification in Chaco / Cerrado**: 2019–2020 + 2024 events; INFONA + SEN monitoring critical for rural / interface properties.
- **Bañado Sur / Pilar floodplain**: recurrent catastrophic flood events 2014/15/18/19/24 — verify finca elevation + flood history pre-purchase.
- **Border-zone illicit economy stigma** (PJC / CDE / Salto): drug-trafficking + counterfeit + smuggling history — buyer due-diligence elevated; verify chain + seller identity carefully.
- **SEPRELAD AML reporting** for >USD 10,000 transactions: standard but documented.
- **ESSAP sewer coverage gap**: ~85 % of population NOT on collective sewer — cámara séptica + pozo absorbente standard.

## Reddit / forum sources

- **r/Paraguay** — general; some real-estate threads; bilingual ES/EN
- **r/Asuncion** — capital focus
- **r/expats** + **expat.com/paraguay** — expat relocation perspective
- **NomadList Asunción + Ciudad del Este** — limited
- **InternationalLiving.com Paraguay** — heavily marketing-driven; cross-check
- **Facebook**: "Expats in Paraguay", "Argentinos en Paraguay", "Brasileiros no Paraguai" (cross-border cohorts)

## Verification authorities

| Authority | When to call |
|---|---|
| **DGRP — Registro Inmobiliario** | Title chain, gravámenes, matrícula |
| **SNC — Servicio Nacional de Catastro** | CCC verification, valor fiscal |
| **Municipalidad (Asunción + per-municipio)** | Impuesto Inmobiliario, ordenanzas, certificados |
| **SET — Subsecretaría de Estado de Tributación** | RUC, IRP/IRE/IDU, ITF, certificados |
| **MEF — Ministerio de Economía y Finanzas** | Tax framework, incentivos Ley 60/1990 |
| **BCP — Banco Central del Paraguay** | FX, monetary policy, Superintendencias Bancos + Seguros |
| **ESSAP** | Water/sewer certificate + connection status |
| **ANDE** | Electric utility certificate |
| **DNM — Dirección Nacional de Migraciones (ex-DGM)** | Residencia status, RUE |
| **MRE — Ministerio de Relaciones Exteriores** | Visa application abroad |
| **SUACE** | Investor business registration + RUE investor track |
| **MUVH** | VIS, FONAVIS/AVI housing subsidies |
| **Colegio de Escribanos del Paraguay** | Verify escribano credential |
| **MOPC** | Vialidad nacional, traffic |
| **SEN** | Emergency/risk historic events |
| **MADES + INFONA** | Environmental + forest |
| **INDERT** | Rural finca status (agrarian reform) |
| **INDI** | Indigenous-territory verification |
| **SENATUR** | STR / turismo prestador registry |
| **SEPRELAD** | AML reporting for large transactions |

## Quirks to know

- **Finca + matrícula vs CCC**: finca = DGRP legal ID, matrícula = title number, CCC = SNC fiscal ID — all three quoted in escritura.
- **Valor fiscal lag**: SNC re-valuación dramatic gap from market — major re-valuation is a long-discussed risk + structural reform candidate.
- **Notarial scale 0.5–2 %**: lower than UY (3 %), often negotiable on premium deals (closer to 0.5 % on >USD 200k).
- **PH régimen Ley 677/1960 + Ley 3.966/2010**: governs propiedad horizontal; reglamento de copropiedad must be reviewed; expensas can be steep in premium torres Asunción.
- **EAS — Empresa por Acciones Simplificada (Ley 6.480/2020)**: simplified one-person corporate; ~1 week setup via SUACE; common for foreign buyers seeking liability separation + RUE investor track.
- **SEPRELAD reporting threshold USD 10,000**: standard; document funds-origin for inbound transfers.
- **Mercosur visa fast-track**: AR/BO/BR/CL/CO/EC/PE/UY citizens get expedited residencia.
- **Foreign-source income territoriality**: PY individuals largely NOT taxed on foreign passive income — a key retirement/nomad attraction.
- **Crypto-mining cluster**: post-2020 hydropower surplus → server farms in CDE/Alto Paraná — affects industrial RE pricing.
- **Mennonite Cooperativa Chortitzer / Fernheim / Neuland**: separate banking, separate insurance, separate utilities in Chaco colonies — NOT integrated with national systems for RE due-diligence purposes.
- **Asunción Bañado Sur informal-formal interface**: lowest-priced "urban" parcels but highest flood + crime + tenure-uncertainty risk.
- **Postcode usage weak**: addresses often rely on barrio + manzana + finca number rather than CP — verify with cadastre + Google Maps + on visit.
- **Itaipú Annex C 2024**: structural energy-revenue rebalance — fiscal-space upside for PY 2025–2030.
- **Naturalisation 3 years**: among fastest globally (vs 5y PT, 10y ES) — passport access route attractive for foreign investors.

## Source URL templates

| Source | URL pattern |
|---|---|
| DGRP (Registro Inmobiliario) | `https://www.pj.gov.py/contenido/144-direccion-general-de-los-registros-publicos/144` |
| SNC (Catastro) | `https://www.catastro.gov.py/` |
| MEF | `https://www.mef.gov.py/` |
| SET (Tributación) | `https://www.set.gov.py/` |
| BCP | `https://www.bcp.gov.py/` |
| ESSAP | `https://www.essap.com.py/` |
| ANDE | `https://www.ande.gov.py/` |
| ERSSAN | `https://www.erssan.gov.py/` |
| SENASA | `https://www.senasa.gov.py/` |
| MOPC | `https://www.mopc.gov.py/` |
| Municipalidad Asunción | `https://www.asuncion.gov.py/` |
| MUVH | `https://www.muvh.gov.py/` |
| MTESS | `https://www.mtess.gov.py/` |
| DNM (Migraciones, ex-DGM) | `https://www.migraciones.gov.py/` |
| MRE | `https://www.mre.gov.py/` |
| SUACE | `https://www.suace.gov.py/` |
| Colegio de Escribanos PY | `http://www.cep.org.py/` |
| SENATUR | `https://www.senatur.gov.py/` |
| SEN (emergencia) | `https://www.sen.gov.py/` |
| DINAC (meteorología) | `https://www.dinac.gov.py/` |
| MADES | `https://www.mades.gov.py/` |
| INFONA | `https://www.infona.gov.py/` |
| INDERT | `https://www.indert.gov.py/` |
| INE / DGEEC | `https://www.ine.gov.py/` |
| Policía Nacional | `https://www.policianacional.gov.py/` |
| SEPRELAD | `https://www.seprelad.gov.py/` |
| BNF | `https://www.bnf.gov.py/` |
| Banco Itaú PY | `https://www.itau.com.py/` |
| Banco Continental | `https://www.bancontinental.com.py/` |
| InfoCasas PY | `https://www.infocasas.com.py/` |
| Clasipar | `https://clasipar.paraguay.com/` |
| MercadoLibre PY | `https://inmuebles.mercadolibre.com.py/` |
| Properati PY | `https://www.properati.com.py/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Paraguay portal (Properati does not operate in PY) |
| CAPADEI | `https://capadei.org.py/` |

## Status

**Confidence**: MEDIUM — HIGH for foundational legal/fiscal framework (Ley 2532/2005 border-zone, Ley 6380/2019 tax reform, Ley 6984/2022 migration, Ley 7143/2023 DNIT, Ley 5513/2015 smallholder rate, Paraguay Investor Pass 2026 USD 200k RE), BCP + INE macro datapoints, and territorial PIT/IRP framework; MEDIUM for fine-grained municipal IMI assessment values + listing-aggregator USD price benchmarks (no national HPI); LOW for parcel-level forward GDP forecasts (verify against current Informe Económico BCP).

**Last verified**: 2026-05-27

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Paraguay's framework is **well-documented at the national-government level** (DGRP, SNC, SET, BCP, DGM, MOPC, MADES, SEN all maintain primary .gov.py portals). HIGH confidence on visa regime (Ley 6984/2022 current migration law + Resolución SET 1186/2023 confirmed), notarial framework (Ley 1.190/1985), tax structure (Ley 6.380/2019 + Ley 125/1991), border-zone rural restriction (Ley 2.532/2005), foreign-buyer rights baseline (Constitución art. 109/109bis), territorial-source IRP design. MEDIUM on parcel-level price/m² (no national transactional RE index — listing-derived only), per-municipio Impuesto Inmobiliario surcharge brackets (vary by ordenanza annually), STR-specific enforcement (lightly regulated as of 2026 Q1 — SENATUR + municipal mosaic). LOW on traffic counts (MOPC TPDA published irregularly — OSM `highway` class is the working fallback), crime granularity (no parcel-level rates published — qualitative + journalistic reliance). Reform watch: (1) potential SNC re-valuación cadastral nacional — would significantly raise Impuesto Inmobiliario; (2) Itaipú Annex C 2024 fiscal-space rebalance impact 2025–2030; (3) further RUE Resolución SET tightening cycles; (4) drought / wildfire climate amplification 2025–2030 affecting Chaco property valuations; (5) potential Mercosur tax-harmonisation initiatives.
