# Uruguay 🇺🇾 — Property Due-Diligence Playbook

ISO2: `uy`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode (CP)**: 5 digits (e.g., `11000` Centro Montevideo, `11300` Pocitos, `11500` Carrasco, `20000` Maldonado, `20100` Punta del Este, `70000` Colonia)
  - Issued by Correo Uruguayo; first digit = región, next 2 = departamento/zone, last 2 = local
- **Admin levels**: 19 **departamentos** → ~125 **municipios** (Ley 19.272 third tier of government, since 2010 reform extending the 2009 Ley 18.567)
- **Currency**: **UYU** (peso uruguayo) for everyday + government contributions; **USD billete** dominant for property transactions (most coastal + premium urban sales priced + closed in USD; mortgages historically in **UI — Unidad Indexada** to CPI under Ley 17.761)
- **Languages**: Spanish (official); Portuñol along Brazilian frontier (Rivera, Artigas, Cerro Largo)
- **Cadastre**: **Dirección Nacional de Catastro (DNC)** — Ministerio de Economía y Finanzas; portal `http://sede.catastro.gub.uy/Sede/`
- **Property registry**: **Registro de la Propiedad — Sección Inmobiliaria**, under Dirección General de Registros (DGR), Ministerio de Educación y Cultura; one office per departamental capital
- **Identifier**: **padrón** (cadastral parcel number, unique per departamento) + **cédula catastral** (DNC valuation reference) + **matrícula** for titled units (PH apartments)
- **Notary**: **Escribano público** — mandatory; civil-law tradition; profession regulated by **Asociación de Escribanos del Uruguay (AEU)** (`https://www.aeu.org.uy/`); **buyer chooses** the escribano per custom (cost ~3% of price)
- **Ownership types**: dominio pleno (freehold), usufructo (very common for inheritance planning), nuda propiedad, condominio indiviso, propiedad horizontal under **Ley 10.751** (1946) and **Ley 14.261** (1974) for apartment regimens
- **Foreigner rights**: **No restrictions** on foreigners owning real estate (constitutional protection, Art. 32). No residency requirement. Same rights as nationals.

### Recent reforms (anchor — full timeline in `shared/regulatory-watch.md`)

- **Ley 20.446 (Presupuesto 2025-2029, en vigor 2026-01-01)** — **MAJOR overhaul of the foreign-attraction regime** (supersedes Ley 19.937 2021): (a) **raised the real-estate investment threshold for tax residency from UI 3.5M to UI 12,500,000** (~USD 2,000,000) + 60-day presence; (b) **restructured the headline holiday** — exemption window = year of acquiring tax residency + the **following 10 fiscal years**, then **5 years at preferential rate = 50% of standard IRPF (i.e., 12% × 50% = 6%)** on foreign passive income (replaces the prior "11-year OR 5-yr + 7%" elective). Decreto 138/020 + 153/020 pathway grandfathered for residency obtained before 2026-01-01. Alt pathway: USD 100k/yr × 11 yrs into a National Innovation Fund (2026-05-27 verified, source IMI Daily + Forvis Mazars + KPMG + Vialto).
- **Ley 19.937 (2021) — SUPERSEDED 2026-01-01** by Ley 20.446. Original regime granted 11-yr foreign-source-income exemption OR 5-yr exemption + 7% reduced rate; applied via the now-grandfathered UI 3.5M / 60-day path. Pre-2026 residents continue under Ley 19.937 (ENDED-style marker — see `shared/regulatory-watch.md`).
- **Ley 18.083 (2007)**: tax framework reform that introduced IRPF (income tax on natural persons), IRAE (corporates), IRNR (non-residents), and IP (Impuesto al Patrimonio) — the architecture still in force
- **Ley 16.906 (1998) — Ley de Inversiones**: COMAP-administered IRAE/IPAT exemptions for certified construction projects (still active; key for new-build off-plan investors)
- **Ley 19.210 (2014) — Inclusión Financiera, modified by LUC Ley 19.889 (9 Jul 2020)**: cash payments in real-estate transactions capped at **1,000,000 UI** (~USD 120,000 at 2026 UI value); amounts above must use banking channels (transferencia, cheque, débito). **The original 40,000 UI / Art. 39 rule was REPEALED by LUC** — playbook prior wording superseded (2026-05-27 verified, source Deloitte UY + Posadas + IMPO Ley 19.889).
- **Ley 20.352 (promulgada 19 Sept 2024, publicada D.O. 27 Sept 2024) — Régimen de actividades de alojamiento turístico** — **NATIONAL STR FRAMEWORK** (supersedes the prior Ley 19.253 + Decreto 384/2018 partial regime): mandatory **Registro de Operadores Turísticos** (Ministerio de Turismo) for owners/administrators/operators of vivienda turística; platforms (Airbnb, Booking) may only list properties present in the registry; scope = alojamiento transitorio up to 120 días; 180-day platform adaptation window; **reglamentary decree still a DRAFT** — Mintur presented the proyecto in late Nov 2025 and it did NOT apply during the 2025-2026 austral summer season, with no signed decree surfacing as of a 2026-09-24 check (pending; IMPO + Carmelo Portal 10 Sep 2026, secondary). Each property receives a public ID number that must appear in every offer (2026-07-02 verified, source IMPO Ley 20352 + gub.uy Mintur proyecto Nov 2025 + CIU Dec 2025).
- **Decreto 138/020 + 153/020 (2020)** — **GRANDFATHERED** for pre-2026 residency only. Set the prior UI 3,500,000 real-estate path + 60-day presence; superseded for new applicants by Ley 20.446 (UI 12.5M).

---

## Section: `--price`

### Primary sources

- **DNC valuation database** (`Valor Real Catastral` — VRC):
  - Portal: `http://sede.catastro.gub.uy/Sede/`
  - Returns DNC-assessed valor real per padrón (basis for Contribución Inmobiliaria, ITP, Patrimonio); typically **30–60% below market** for Montevideo + Punta del Este (DNC re-valuations are infrequent; last general re-aforo 2012 with annual ajustes)
  - Per-padrón lookup requires registered access for full record; consulta básica is free
- **INE (Instituto Nacional de Estadística)**:
  - Índice de Precios de Compraventa de Inmuebles (IPCV): `https://www.ine.gub.uy/inmuebles`
  - Quarterly index of registered transactions, broken down by Montevideo/Interior and tipo (terreno, vivienda)
  - **2024 IPCV** showed ~5–7% YoY USD-equivalent appreciation in Montevideo apartments (verify current quarter at INE)
- **BCU (Banco Central del Uruguay)**:
  - `https://www.bcu.gub.uy/` — UI valor del día, política monetaria, tipo de cambio referencia
  - UI value is the inflation-indexed unit used for legal thresholds (Ley 19.210, mortgage indexation)
- **Cámara Inmobiliaria Uruguaya (CIU)**: `https://www.ciu.com.uy/` — quarterly market reports
- **MVOTMA / MVOT (Ministerio de Vivienda y Ordenamiento Territorial)**: `https://www.gub.uy/ministerio-vivienda-ordenamiento-territorial/` — VIS (Vivienda de Interés Social) registry, social housing transactions

### Listing platforms

- **InfoCasas** — leading portal: `https://www.infocasas.com.uy/`
- **Mercado Libre Inmuebles UY**: `https://inmuebles.mercadolibre.com.uy/`
- **Gallito.com.uy**: `https://www.gallito.com.uy/inmuebles`
- **Properati**: `https://www.properati.com.uy/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **El País Clasificados**: `https://gallito.com.uy`
- **InmoUruguay** (specialized in coastal): `https://www.inmouruguay.com/`
- **Punta.com** (Punta del Este focus): `https://www.punta.com/`

**USD vs UYU**: Sale listings overwhelmingly in **USD billete** (especially Montevideo Carrasco/Pocitos/Punta Carretas + ALL of Maldonado/Punta del Este + Colonia coast). Long-term residential rentals usually in **UYU** but increasingly with UI/USD adjustment clauses. Listings priced in UYU are flagged "$U" and tend to be smaller interior properties.

### 2026 price benchmarks (USD/m², asking — InfoCasas + Reporte CIU + TheLatinvestor cross-checked, Q1 2026)

| Region | USD/m² (typical) | Notes |
|---|---:|---|
| **MVD Carrasco** (premium, embassy zone) | $3,000–$5,200 (avg ~$3,800) | luxury single-family + low-rise; rising |
| **MVD Punta Carretas** (premium urban) | $3,500–$5,000 | high-rise + remodelados |
| **MVD Pocitos / Pocitos Nuevo** | $3,000–$4,500 | dense apartments, strong demand |
| **MVD Punta Gorda** | $2,800–$4,200 | costa + view premium |
| **MVD Buceo / Puerto Buceo** | $2,500–$3,800 | World Trade Center axis, growing |
| **MVD Centro / Cordón / Tres Cruces** | $1,800–$3,000 | older stock, value tier |
| **MVD Malvín / Parque Batlle** | $2,200–$3,200 | mid-tier residential |
| **MVD Periferia / Ciudad Vieja** | $1,200–$2,200 | gentrifying historic |
| **Punta del Este — Brava beachfront** | $5,000–$10,000+ | super-premium torres, USD asking |
| **Punta del Este — Mansa / Playa Mansa** | $3,500–$6,500 | family-oriented luxury |
| **Punta del Este — La Barra / Manantiales** | $3,000–$5,500 | bohemian-lux |
| **José Ignacio (Maldonado)** | $5,000–$12,000+ | ultra-premium boutique |
| **Maldonado city (non-PdE)** | $1,500–$2,500 | year-round, value |
| **Piriápolis** | $1,500–$2,800 | classic balneario |
| **Colonia del Sacramento (UNESCO casco)** | $1,800–$3,500 | heritage premium |
| **Punta del Diablo / La Pedrera (Rocha)** | $1,800–$3,500 | boutique coastal, seasonal |
| **Atlántida / Costa de Oro** | $1,400–$2,400 | commuter coastal |
| **Salto / Paysandú** (interior cities) | $700–$1,500 | low-tier interior |
| **Rivera / Artigas** (Brazilian frontier) | $600–$1,300 | very low-tier |

(Q1 2026 data, sources: InfoCasas indexed listings + CIU quarterly + TheLatinvestor — rates/figures may have changed since; cross-check for the specific date of valuation.)

### Compute

1. USD/m² = USD asking / **superficie edificada** (built area, declared in escritura)
2. **Distinguish**: `superficie del terreno` vs `superficie edificada` vs `superficie construida` (sometimes incl. balcón); listings often blur these
3. **DNC VRC vs market**: official Valor Real typically 30–60% below market in MVD/PdE — use VRC only for tax estimation, never as market-value proxy
4. **Trap**: USD-billete (cash) vs USD wire — slight cash premium historically due to AML friction; verify currency-of-payment
5. **Trap**: PdE listings often quote price WITHOUT expensas (HOA) — torres can be USD 4–10/m²/month

### Key terms

- **Padrón** = parcel ID per departamento; **Matrícula** = title ID for PH units; **Cédula catastral** = DNC valuation reference
- **Escritura pública** = notarized deed (sole legal proof of transfer); **Boleto de reserva** = pre-escritura binding seña
- **VRC (Valor Real Catastral)** = DNC-assessed value (basis for Contribución, ITP, Patrimonio)
- **UI (Unidad Indexada)** = CPI-indexed unit (Ley 17.761, 2004) published daily by INE; ~UYU 6.7 as of 2026-05 (verify daily at DGI/BCU). USD conversion of UI thresholds requires *two* peg lookups (UI/UYU AND UYU/USD)

---

## Section: `--traffic`

### Sources

- **MTOP — Ministerio de Transporte y Obras Públicas**: `https://www.gub.uy/ministerio-transporte-obras-publicas/` (institutional landing)
- **MTOP Geoportal — DNV traffic-data product**: `https://geoportal.mtop.gub.uy/` (primary — interactive map + estación de aforo + TPDA data)
- **Sistema de relevamiento estadístico de tránsito (MTOP — Dirección Nacional de Vialidad)**: `https://geoportal.mtop.gub.uy/-/sistema-de-relevamiento-estadistico-de-transito` — **per-station TPDA** (tránsito promedio diario anual) with the location of each *Puesto de Conteo de Vehículos*, served as a geoservice, so traffic can be read at a specific road segment rather than a regional rollup (2026 data, source MTOP geoportal; 2026-09-18 verified)
  - Publishes **TPDA (Tránsito Promedio Diario Anual)** — average annual daily traffic per estación de aforo on national routes (regional usage: TMDA)
  - Annual report; latest typically lags 1–2 years (verify latest at Geoportal MTOP) (2026-05-27 verified)
- **Intendencia de Montevideo — Movilidad**: `http://montevideo.gub.uy/tipo/area-tematica/movilidad`
  - Conteos vehiculares for capital arteries (Av. 18 de Julio, Rambla, Av. Italia, Av. 8 de Octubre, Bvar. Artigas)
- **Intendencia de Maldonado — Tránsito**: traffic data for Punta del Este corridor (Ruta 10, Ruta Interbalnearia)
- **Fallback**: OSM `highway` tag (motorway/trunk/primary/secondary/tertiary/residential)

### Key term

**TPDA (Tránsito Promedio Diario Anual)** — Average Annual Daily Traffic, measured per estación de aforo on national routes (regional ONDaT usage: TMDA; older docs may say TMD).

### Verdict bands

- 🟢 < 1,000 v/d (rural ruta secundaria, calle barrial)
- 🟡 1,000–5,000 v/d (avenida barrial, ruta nacional baja-densidad)
- 🟠 5,000–20,000 v/d (avenida urbana principal, Ruta Interbalnearia tramos rurales)
- 🔴 > 20,000 v/d (Rambla MVD, Av. Italia, Av. 8 de Octubre, Ruta 1 metropolitana, Ruta Interbalnearia high-season)

### Coarse fallback

OSM `highway` class:
- motorway/trunk = autopista (Ruta 1 / 5 / 9 selected stretches), Ruta Interbalnearia
- primary = ruta nacional principal (Ruta 1, 5, 8, 9)
- secondary = ruta nacional secundaria, avenida urbana
- tertiary = camino vecinal, calle de barrio
- residential = calle interior

### Notes

- **Punta del Este Ruta 10 + La Barra–José Ignacio**: traffic is **wildly seasonal** — Jan–Feb 2025 peaks reportedly 5–10× off-season levels per Intendencia Maldonado; verify with on-site visit during target season
- **Montevideo Rambla**: weekend/summer 2× weekday flow; noise + jogger activity major
- **Ruta Interbalnearia (IB)**: peak summer Friday-Sunday + Carnival traffic significantly degrades drive time MVD → PdE (normal 90 min; peak can be 3+ hours)

---

## Section: `--tax`

### Annual property tax — Contribución Inmobiliaria

**Levied by Intendencia (departamental government)** — rates and brackets vary by departamento. Basis: **VRC (Valor Real Catastral)** per padrón.

| Departamento | Rate range (% of VRC) | Notes |
|---|---|---|
| **Montevideo** | **0.18%–1.80%** (progresivo, 6 brackets; Decreto Departamental 38.156, eff. 2024-01-01) | Entry bracket 0.18% covers ~70% of properties (VRC < ~UYU 2.48M, 2024 ref); top bracket 1.80%; retirees may access 50–100% exemption. Brackets re-set annually by IM (`https://montevideo.gub.uy/`) (2026-05-27 verified) |
| **Maldonado** | 0.30%–1.20% (progresivo) | Premium PdE typically 0.8–1.2% effective (verify Intendencia de Maldonado annual ordenanza) |
| **Canelones** | 0.30%–1.10% | Costa de Oro tier varies |
| **Colonia** | 0.30%–1.00% | Colonia del Sacramento heritage subject to caps |
| **Interior departamentos** (Salto, Paysandú, Rivera, Tacuarembó, etc.) | 0.25%–0.80% typical | Lower brackets, lower VRC base |

(2025 ordenanzas, verify current year at each Intendencia; LOW–MEDIUM confidence on bracket exactness — these vary annually.)

### Surcharges + adjacent taxes

- **Adicional para MIDES** (Ministerio de Desarrollo Social) — surcharge on certain Contribución brackets in some departamentos (variable; verify per Intendencia)
- **Impuesto a la Educación Primaria** (school tax, national):
  - Levied on padrón holders; rate scales with VRC
  - Typical ~0.15% of VRC for residential; capped categories
  - Source: ANEP / DGI, see `https://www.dgi.gub.uy/`
- **Impuesto al Patrimonio (IP)** — wealth tax under Ley 18.083:
  - For natural persons resident in UY: levied on net worldwide assets (with exemptions for housing, vehicles, household goods up to thresholds)
  - 2025 minimum non-imponible (per persona física): ~UYU 6,500,000 (verify current at DGI; ~USD 165,000 at 2026 FX)
  - Rates: progressive 0.1%–0.6% for residents, 1.5% flat for non-residents holding UY assets via certain structures
  - **Trap**: Foreign individual owners of property in UY may face IP if structured through SA/SRL — natural-person ownership generally avoids if VRC + assets below threshold

### Transaction taxes — one-time at purchase

- **ITP (Impuesto a las Transmisiones Patrimoniales)** — Title 19 of Texto Ordenado DGI:
  - **Total 4% of VRC** (NOT market price — major saving for buyers since VRC is typically 30–60% below market)
  - Customarily split: **2% buyer + 2% seller** (negotiable but standard)
  - Source: DGI `https://www.dgi.gub.uy/`
- **Aportes a BPS (Banco de Previsión Social)** — for sellers selling new construction or recently-completed properties: contributions on labor used in construction (rare for second-hand)
- **Inscripción en el Registro de la Propiedad** — registration fee:
  - ~0.55% of VRC (verify current arancel at Dirección General de Registros: `https://www.gub.uy/ministerio-educacion-cultura/politicas-y-gestion/direccion-general-registros`)
- **Honorarios del escribano** (notary fee):
  - Customarily ~3% of price, paid by buyer (negotiable — large transactions often closer to 1.5–2%)
  - Per AEU arancel suggested + colegiado practice
- **Comisión inmobiliaria** (broker):
  - 3% + IVA (22%) buyer + 3% + IVA seller customary
  - Negotiable on premium PdE / large deals (often 2% + IVA each)

### Capital gains / IRPF

- Sale of real estate by natural-person resident: **IRPF Cat I — 12% on indexed gain** (real gain after CPI indexation under UI mechanism)
- Non-residents: **IRNR 12%** flat on indexed gain
- **Primary residence exemption**: no automatic exemption like FR/UK, but if proceeds reinvested into new primary residence under specific conditions, deferral possible (consult escribano)
- Source: DGI, `https://www.dgi.gub.uy/normativa-1/normativa-1`

### Inheritance / succession

- **No inheritance tax in Uruguay** since 1976 (one of major tax-relocation attractions)
- However: **ITP applies to inheritances** at reduced rates (typically 3% for direct ancestors/descendants, 4% for siblings)
- Source: DGI Texto Ordenado, see `https://www.dgi.gub.uy/`

### Example calculation — Carrasco apartment, USD 500,000 market, VRC USD 250,000 equivalent

```
Market price (asking):              USD 500,000
VRC (estimated 50% of market):      USD 250,000  ← basis for ITP, IP, Contribución
ITP (4%, split 2+2):                USD 10,000 total (USD 5k buyer)
Contribución (~0.9% of VRC):        USD 2,250 / year
Imp. a Primaria (~0.15% VRC):       USD 375 / year
Notary (3% of price):               USD 15,000
Inscripción (0.55% VRC):            USD 1,375
Comisión 3% + IVA each side:        ~USD 18,300 buyer-side
─────────────────────────────────────────────
Total buyer transaction cost:       ~USD 39,675 (~7.9% of price)
Annual recurring tax:               ~USD 2,625
```

(Computed example, inputs listed inline. Real VRC must be looked up per padrón at DNC.)

### Future risk

- Periodic talk of re-aforo catastral nacional (general re-valuation) — would raise VRC closer to market and significantly increase ongoing taxes; last major re-valuation 2012; **monitor MEF + DNC announcements**
- Tax-residency real-estate threshold (now **UI 12,500,000** per Ley 20.446, eff. 2026-01-01; prior UI 3.5M grandfathered for pre-2026 residency) is policy-mutable — has been changed before; could be raised or lowered
- **EU "list of non-cooperative jurisdictions" pressure**: Uruguay was on/off the EU grey list 2017–2020; full alignment with OECD BEPS could affect corporate-structure taxation of property holdings

---

## Section: `--rental`

### Long-term residential

**Statutory framework**: **Ley 14.219 (1974)** — Ley de Arrendamientos Urbanos + **DL 14.461 (1975)** + **Ley 16.471** modifications. Strong tenant protections — Uruguay is **distinctly tenant-friendly** by regional standards.

#### Standard contract structure
- **Plazo mínimo**: **2 años** for vivienda (residential); 1 year for non-residential casual
- **Garantía** required: typically **garantía solidaria (cosigner)**, **fianza** (deposit), **seguro de fianza** (Banco República FIANZA — popular), or **garantía bancaria**
- **Reajuste de alquiler**: indexed annually to **IPC (CPI)** or **UR (Unidad Reajustable)** — agreed in contract; default IPC since 2008 reform
- **Desalojo** (eviction) processes: judicially driven, can take 6–18 months; non-payment + abandono are faster routes
- **Subarriendo** (subletting): generally prohibited unless contract explicitly permits

#### Income tax on rental

| Status | Regime | Rate |
|---|---|---|
| **Resident natural person** | IRPF Cat I (rendimientos del capital inmobiliario) — Decreto 148/007 | **12% annual** on taxable rent; **10.5% monthly withholding** by retention agent (e.g. immobiliaria), creditable; deductible expenses: Contribución Inmobiliaria, Imp. a Primaria, BPS aportes (rural). Tenant of permanent residence may claim **6% credit** vs own IRPF (2026-05-27 verified, source DGI Resol. 662/007 + Decreto 148/007) |
| **Non-resident** | IRNR | **12% statutory** on Uruguayan-source rental income; in practice **10.5% monthly retención** by tenant/immobiliaria operates as final tax (no DJ obligation if fully retained). Verify per-transaction with contador |
| **Corporate (SA/SRL)** | IRAE | 25% on net + IP if applicable |

Source: DGI Texto Ordenado Cap. IV (IRPF) + Cap. VI (IRNR), see `https://www.dgi.gub.uy/`

### Short-term rentals (alquiler por temporada / Airbnb)

#### Statutory classification
- **Ley 20.352 (promulgada 19 Sept 2024, publicada D.O. 27 Sept 2024) — NATIONAL STR FRAMEWORK** creates the mandatory **Registro de Operadores Turísticos** (Ministerio de Turismo) for vivienda turística owners/administrators/operators; the **inscription number must appear in every offer** through any channel, physical or electronic (Ley 20.352 text, IMPO), and platforms (Airbnb, Booking) may only list registered properties. Scope = **alojamiento transitorio up to 120 días** (gub.uy Mintur). The **reglamentary decree is still a DRAFT** — Mintur presented the proyecto in **late Nov 2025** with a **180-day platform adaptation window**; it did **NOT apply during the 2025-2026 austral summer season** and no signed/gazetted decree had surfaced as of a 2026-09-24 check (IMPO consolidated text carries no reglamentación note; Carmelo Portal 10 Sep 2026, secondary, reports the Executive still completing it with no entry-into-force date), so the regime **remains pending** (status MEDIUM — evidence of absence). Guest identity must be reported periodically to the **Ministerio del Interior** (Ley 20.352 art. 4 d, IMPO). A **>5 lets/año** trigger is cited by news-tier CIU/Ámbito but appears in neither the Ley 20.352 text nor the Mintur 24 Nov 2025 release — data not publicly available, verify at gub.uy/ministerio-turismo once the decree is signed. Supersedes the partial Ley 19.253 + Decreto 384/2018 regime (2026-07-02 verified, source IMPO Ley 20352 + gub.uy Mintur proyecto Nov 2025 + CIU Dec 2025).
- Temporada contracts: <1 año, no Ley 14.219 protections, simpler termination, but require formal contract
- Ley 14.219 long-term protections do NOT apply to temporada contracts

#### Maldonado (Punta del Este)
- **No separate municipal STR registry** — Maldonado STR falls under the **national Ley 20.352 regime** (above), not an Intendencia "Operador Receptivo" requirement (the *operador receptivo* label is the distinct inbound tour-agency category, not an STR-landlord obligation)
- The **Intendencia de Maldonado's role is limited to reinforcing control over informal supply** in high-demand zones (Punta del Este, Piriápolis) for fair competition with traditional hotelería (per Alda, 2025-10-27 — secondary source, verify with Intendencia) (`https://www.maldonado.gub.uy/`)

#### Montevideo
- No general STR registry as of 2026 Q1; commercial accommodation businesses register under Ministerio de Turismo
- **Ministerio de Turismo Registro Único de Operadores Turísticos (RUOT)** — required for certain hospitality services (`https://www.gub.uy/ministerio-turismo/`)

#### Tax regime for STR
- Same IRPF Cat I (12%) for residents OR IRNR (12%) for non-residents (resident STR rental is ordinary IRPF Cat I rental — see rental tax table above; the 6% preferential rate is the Ley 20.446 foreign-passive-income rate, not an STR rate)
- If letting becomes "habitual + organized" → may be re-classified by DGI as **IRAE actividad empresarial** (25% on net + IP + BPS aportes); threshold judgment-based; consult contador
- **IVA**: STR rentals for vivienda exempt; if treated as hotelero (con servicios accesorios = limpieza diaria, recepción, cocina) may attract IVA (currently 22%, with reduced rates for tourism services in some seasons)

### Strategic notes

- **MVD long-term**: tenant-protection tilt + 2-yr minimum + slow eviction process means buy-to-let landlords face holding-period friction; cash-flow yields ~4–6% gross before tax in Pocitos/Punta Carretas (2025 CIU data), 5–8% in lower-tier
- **Punta del Este STR**: huge January peak (often single-month income = 50%+ of annual), Feb decent, Mar–Apr shoulder, **May–Nov occupancy collapses** (~5–15% off-season) — annual yields 4–8% gross net of expensas / mantenimiento
- **Colonia + Punta del Diablo / La Pedrera**: weekend + summer demand from Buenos Aires (Argentina day-trippers via Buquebus / Colonia Express) + Brazilian visitors; year-round modest
- **Tenant-side**: IRPF deductibility of rent paid (under specific conditions) — relevant for rental decisions for residents

---

## Section: `--work=<profession>`

### Job platforms

- **Buscojobs.com.uy**: `https://www.buscojobs.com.uy/`
- **Computrabajo Uruguay**: `https://www.computrabajo.com.uy/`
- **LinkedIn Uruguay** — strong in IT, financial services, MNCs (Zonamerica + Aguada Park concentrations)
- **Mercado Libre Empleos**: `https://empleos.mercadolibre.com.uy/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **El Gallito Empleos**: `https://www.gallito.com.uy/empleos`
- **El País Clasificados Empleos**: `https://trabajo.gallito.com.uy/`

### Self-employment / unipersonal

- **Unipersonal (sole trader)** — registers at DGI + BPS:
  - **Monotributo** simplified regime: capped activities + revenue (~UYU 686,000/year 2025 ceiling for Monotributo, verify at BPS); single combined contribution covering jubilación + salud + IRPF
  - **Unipersonal IRAE/IVA** general regime: full IVA + IRAE if activities/revenue exceed Monotributo caps
- **Sociedad Anónima (SA)**: traditional corporate; bearer-share reform under Ley 18.930 — registry now nominal
- **SRL**: simpler corporate, common for SMEs
- **SAS (Sociedad por Acciones Simplificada)** — Ley 19.820 (2019): simplified one-person corporate; lower friction

### Foreign worker permit

- **Dirección Nacional de Migración (DNM)** — Ministerio del Interior: `https://www.gub.uy/ministerio-interior/politicas-y-gestion/acerca-direccion-nacional-migracion`
  - **MERCOSUR nationals** (AR, BR, PY, BO, CL, CO, EC, PE, VE — full + associated): expedited residencia permanente or temporaria
  - **Other nationals**: residencia temporaria (1+1 years) → residencia permanente
- **Permiso de trabajo** generally tied to residencia status; not a separate permit for residents
- **Tax residency** (separate from migratory residency): granted under DGI rules at:
  - **183+ days physical presence** in calendar year, OR
  - **Centro de intereses vitales** (family + economic) in UY, OR
  - **Real-estate investment** ≥ **UI 12,500,000 (~USD 2,000,000)** + 60-day presence per Ley 20.446 (eff. 2026-01-01); pre-2026 UI 3,500,000 path grandfathered for residency obtained before 2026-01-01, OR
  - **Business investment** ≥ UI 15,000,000 + 15 direct jobs created
  - Source: DGI Resolución 543/008 + Decreto 138/020 + 153/020

### Salaried benchmarks (2025 — INE Encuesta Continua de Hogares)

- Median monthly gross (private sector): ~UYU 50,000–65,000 (~USD 1,250–1,650 at 2026 FX)
- IT senior dev (Zonamerica/Aguada Park MNC): ~USD 3,000–6,000+ (often paid USD)
- Doctor (médico generalista MSP): ~USD 1,500–2,500
- Médico especialista (private mutual): ~USD 3,000–5,000
- Salario mínimo nacional 2025: UYU 22,268/month (~USD 565)

### Catchment heuristics

- **MVD Centro / Pocitos / Punta Carretas / Carrasco**: full national labor market access (MNCs, gov, finance, MercoPress)
- **Maldonado / Punta del Este year-round**: limited skilled labor outside hospitality + construction + retail; IT remote OK
- **Colonia, Salto, Paysandú**: regional capitals — local civil service, agribusiness, light industry
- **Interior rural**: very thin labor markets; agropecuario + tourism + remote-work only

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **DINAGUA — Dirección Nacional de Aguas** (MA) | `https://www.gub.uy/ministerio-ambiente/politicas-y-gestion/agua` | Water management, flood basins, river-network data |
| **INUMET — Instituto Uruguayo de Meteorología** | `https://www.inumet.gub.uy/` | Climate data, alertas meteorológicas, wind/rain history |
| **SINAE — Sistema Nacional de Emergencias** | `https://www.gub.uy/sistema-nacional-emergencias/` | Emergency management, historic flood/storm events |
| **Instituto SARANDÍ / Geológico (DINAMIGE)** | `https://www.gub.uy/ministerio-industria-energia-mineria/tematica/mineria-geologia` | Geology, low-seismicity assessment |
| **Sistema de Información Ambiental (SIA — MA)** | `https://www.ambiente.gub.uy/sia/` | Environmental data layers |
| **MVOTMA / DINAMA flood-risk maps** (where available) | regional via MVOT | Coastal + fluvial flood zones |

### Flood + coastal risk

- **River basins**: **Río Uruguay** (western frontier — Salto, Paysandú, Mercedes, Fray Bentos), **Río Negro** (central), **Río de la Plata** (southern coast); historic events:
  - **2010 Mercedes flood** (Río Negro): 18,000 evacuated, major damage in Soriano
  - **2015 + 2017 Río Uruguay floods**: Bella Unión, Salto, Paysandú repeatedly affected
  - Recurrent low-grade flooding in Treinta y Tres (Río Olimar) + Durazno (Río Yí)
- **Coastal SLR (sea-level rise)**:
  - IPCC AR6 projects ~30–60 cm by 2100 (SSP2-4.5); Río de la Plata estuary already shows accelerated subsidence + storm surge in some segments
  - **Punta del Este** beachfront: SLR + erosion concern for ground-floor units 2050–2100; Brava + Mansa beaches actively monitored
  - **Atlántida / Costa de Oro**: similar exposure
  - **Colonia historic casco**: some riverfront historic buildings vulnerable
- **Tornadoes**: Uruguay is in the South-American tornado corridor (less intense than US Tornado Alley but real); historic event **2016 Dolores tornado** (Soriano, EF3) — 5 deaths, town devastated; SINAE issues warnings during austral spring/summer
- **Sudestadas**: SE wind storms drive Río de la Plata water levels up; can flood low-lying MVD Rambla + Ciudad Vieja periodically

### Seismicity

- **Very low — Uruguay sits on stable South American Platform** (Cratón del Río de la Plata)
- Historical record: a handful of M >4 events in 200 years; 1888 Colonia M~5 reported (uncertain magnitude); 2016 Río de la Plata estuary M 4.0 (offshore, no damage)
- **Building codes** do not require seismic-resistant design (vs Chile/Peru); standard reinforcing concrete construction applies
- For most properties, seismicity is **🟢 negligible**

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1940 (casco histórico, Ciudad Vieja, Colonia)** | Lead paint, lead pipes, weak foundations, possible asbestos in roofing repairs |
| **1940–1970 art deco + early modern** | Asbestos in cement-fibre roofing + tank insulation; lead pipes |
| **1970–1990** | Vivienda económica boom (BHU); variable build quality, asbestos use peaked early 80s; lead in some plumbing |
| **1990–2010** | Modern materials; condominio horizontal Ley 10.751 + Ley 14.261 governance applies; energy efficiency variable |
| **Post-2010 (Promoción de Inversiones era)** | Modern build standards; many incentivized constructions (Ley 16.906 COMAP) — verify habilitación final |
| **Post-2018 NB-Norma de Eficiencia Energética** | Some new builds rated under voluntary labelling; mandatory in some projects |

**Asbestos**: pre-1995 use widespread; **regulation since 2003 (Decreto 154/002)** restricts new use; removal not as strictly mandated as EU; verify on inspection if roof/insulation contains amianto.

### Mandatory diagnostics + due-diligence at sale

| Document | Required because | Source |
|---|---|---|
| **Estudio de títulos (30-yr chain)** | Verify 30-year title chain — standard escribano practice | Escribano público (mandatory) |
| **Plano de mensura registrado** | Cadastral plan registered at DNC | DNC `http://sede.catastro.gub.uy/Sede/` |
| **Cédula catastral informada** | DNC valuation reference | DNC |
| **Certificado único de DGI Inmuebles** | Confirms no IRPF/IRAE/Patrimonio debts on the padrón | DGI `https://www.dgi.gub.uy/` |
| **Certificado común de BPS** | Confirms no labor + social-security debts (relevant for new construction) | BPS `https://www.bps.gub.uy/` |
| **Certificado de OSE** | Confirms no water utility debts | OSE `https://www.ose.com.uy/` |
| **Certificado de UTE** | Confirms no electric utility debts | UTE `https://portal.ute.com.uy/` |
| **Certificado urbanístico de la Intendencia** | Confirms zoning, no outstanding municipal infractions, habilitación al día | Intendencia (variable URL per departamento) |
| **Constancia de pago de Contribución Inmobiliaria** | No outstanding municipal property tax | Intendencia |
| **Reglamento de copropiedad + acta de asamblea** | If PH: verify governance, expensas debts, fund balance | Administración del edificio |
| **Habilitación de bomberos** (commercial) | Required for commercial uses | DNB (Bomberos) |
| **Plano de instalación sanitaria + eléctrica aprobados** | Verify habilitación municipal | Intendencia |

**Critical**: The escribano públicamente conducts the **estudio de títulos (30-year chain)** — this is THE central diligence step. Buyer pays escribano fees (~3% customary). Foreign buyers should ensure escribano is reputable (verify membership at AEU `https://www.aeu.org.uy/`).

### Climate change projections (INUMET + IPCC AR6 + WB Climate Knowledge Portal)

- **+1.0 to +2.5 °C** by 2050 vs 1981–2010 baseline (depending on SSP)
- **More intense rainfall events**: Río Uruguay + Río Negro basin floods projected to increase frequency
- **Drought severity** rising in central + northern UY (Salto, Paysandú, Tacuarembó) — agricultural impact + groundwater stress
- **Coastal SLR**: 20–40 cm by 2050, 50–80 cm by 2100 (SSP2-4.5); higher under SSP5-8.5
- **Heat waves**: more frequent + intense; +5–8 days/year >32°C in Montevideo by 2050 (INUMET projections)
- **Sudestada intensification** likely; storm-surge events on Río de la Plata may worsen

---

## Section: `--mains`

### National operator

- **OSE — Obras Sanitarias del Estado**: `https://www.ose.com.uy/`
  - State-owned national water + sanitation utility
  - **Coverage** (per OSE 2024 annual report, verify current):
    - Drinking water: ~99% urban, ~85% nationwide population
    - Sewer / saneamiento: ~60% nationwide; **MVD ~95%+** in central; **interior coverage variable** (often <60% in small interior cities)
- **Intendencia de Montevideo — Saneamiento**: shared responsibility for sewer in capital; OSE provides agua potable, IM operates sewer in MVD via Plan de Saneamiento Urbano (PSU) (`http://montevideo.gub.uy/tipo/area-tematica/ambiente/agua-y-saneamiento/agua-y-saneamiento`)

### Regional / municipal

- **Punta del Este + Maldonado urban**: OSE coverage near-100% (saneamiento full)
- **La Barra / José Ignacio / interior PdE**: mixed — pozo + pozo negro / fosa séptica still common in older lots; verify per-padrón
- **Colonia del Sacramento urban**: OSE full coverage
- **Costa de Oro (Atlántida, Las Toscas, Salinas)**: water full; sewer expanding but **NOT universal** — many lots still on **pozo + pozo negro**; verify before buying
- **Rural** (campo / chacras): typically pozo (well) + pozo negro / fosa séptica; no mains

### Verification

1. Check **OSE Mapa de Saneamiento** (where published) or call OSE Atención al Cliente: 1881
2. Listing language:
   - "saneamiento OSE" / "saneamiento por OSE" / "alcantarillado" = mains drains
   - "pozo negro" / "fosa séptica" / "cámara séptica" = septic tank / cesspit (no mains sewer)
   - "pozo + bomba" = own well + pump (no mains water)
3. Request **certificado de OSE** as part of pre-escritura (mandatory diligence)

### Costs (2026 USD est. — verify with installer)

| Scenario | Cost |
|---|---:|
| OSE connection where saneamiento available | USD 800–2,500 (conexión + tasa + obra civil) |
| Saneamiento extension to new lot (if street has trunk) | USD 2,000–5,000 |
| New fosa séptica + pozo de infiltración (lot off-grid) | USD 3,000–7,000 |
| Pozo de agua perforado + bomba | USD 2,000–5,000 |
| Replace pozo negro with séptica + biofiltro modern | USD 4,000–10,000 |

(2026 estimates from informal contractor surveys + InfoCasas-listed services — verify with 2-3 quotes.)

---

## Cost benchmarks (UY 2026)

| Work | Cost |
|---|---:|
| **ITP total (4% of VRC, split 2+2)** | ~2% of VRC each side |
| **Notary (escribano) — buyer side** | ~3% of price (negotiable, often 1.5–2% on large deals) |
| **Inscripción registral** | ~0.55% of VRC |
| **Comisión inmobiliaria** | 3% + IVA buyer + 3% + IVA seller (negotiable) |
| **Plano de mensura** (new survey) | USD 500–2,000 |
| **Estudio de títulos** (included in escribano fee) | (folded into 3%) — standalone USD 500–1,500 |
| **Certificados (DGI, BPS, OSE, UTE, IM)** | USD 100–300 total |
| **Tasación independiente** (independent valuation) | USD 200–500 |
| **Inspección técnica** (independent surveyor) | USD 300–800 |
| **Contribución Inmobiliaria (annual, residential MVD avg)** | USD 800–3,000 typical for PH; higher for casas en Carrasco |
| **Imp. Primaria (annual)** | USD 100–500 typical |
| **Expensas comunes (PH MVD premium)** | USD 80–250/month |
| **Expensas torres premium PdE** | USD 200–1,500/month |
| **Total transaction cost (buyer side)** | ~6–9% of price |

(2026 estimates; computed using customary % rates above. ITP saving from VRC-vs-market gap is the major reason actual cash cost is below the headline 4%.)

## Active fiscal incentives (2025–2026)

- **Ley 16.906 / COMAP — Promoción de Inversiones**:
  - IRAE / IPAT / IVA exemptions for certified construction projects (residential + commercial)
  - Off-plan investors in COMAP-certified developments often inherit IP exemption on the unit for several years
  - Source: COMAP `https://www.gub.uy/ministerio-economia-finanzas/comap`
- **VIS — Vivienda de Interés Social** (under MVOT):
  - IRAE/IRPF/IP exemptions for developers building VIS-classified apartments (size + price caps)
  - Buyers of VIS units may access subsidized credit via Banco Hipotecario del Uruguay (BHU) or ANV
  - Source: ANV `https://www.anv.gub.uy/`
- **Tax-residency foreign-source-income holiday (Ley 20.446, en vigor 2026-01-01 — supersedes Ley 19.937)**:
  - **THE headline foreign attraction** — restructured for 2026 onwards
  - Exemption window = **year of acquiring tax residency + the following 10 fiscal years**, then **5 years at preferential rate = 50% of standard IRPF (i.e., 6%)** on foreign passive income (replaces the prior "11-year OR 5-yr + 7%" elective)
  - Alt pathway: USD 100k/yr × 11 yrs into a National Innovation Fund
  - Real-estate pathway: invest ≥ **UI 12,500,000** (~USD 2,000,000 at 2026 UI) + **60+ days presence** in calendar year
  - Pre-2026 residents stay under Ley 19.937 (grandfathered)
  - Source: Ley 20.446 (IMPO) + DGI Resolución 543/008 + Decreto 138/020 + 153/020 (2026-05-27 verified)
- **Free Zones (Zonas Francas)**: e.g., Zonamerica, Aguada Park, Parque de las Ciencias — corporate IRAE exemption + IP exemption for businesses; not directly for property investment, but residents working there may qualify
- **BHU mortgages**: state-backed housing finance for residents — UI-indexed loans up to 30 years, rates ~3.5–5.5% real (above UI inflation) for VIS; 5–7% real for non-VIS

## Common listing platforms

- **InfoCasas** — leading: `https://www.infocasas.com.uy/`
- **Mercado Libre Inmuebles UY**: `https://inmuebles.mercadolibre.com.uy/`
- **Gallito.com.uy**: `https://www.gallito.com.uy/inmuebles`
- **Properati**: `https://www.properati.com.uy/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **El País Clasificados**: `https://gallito.com.uy`
- **Punta.com** (PdE focus): `https://www.punta.com/`
- **InmoUruguay** (coastal): `https://www.inmouruguay.com/`
- **Sotheby's UY, Engel & Völkers UY, Christie's** (premium / luxury — Carrasco + PdE + José Ignacio)

## Caveats unique to UY

- **Tax-residency foreign-income holiday** (acquisition year + 10 fiscal years, then 5 yrs at 6% per Ley 20.446, eff. 2026-01-01 — supersedes the prior flat 11-year exemption) is THE headline foreign attraction — Uruguay has been a wealth-relocation destination from Argentina + Brazil since the 2000s and the 2020 reform doubled-down on this
- **VRC-vs-market gap** typically 30–60% means **ITP cash cost is lower than the headline 4% suggests** — but Contribución Inmobiliaria (annual) also taxed on VRC, so it cuts both ways
- **USD-pricing convention** for sales — verify whether USD billete or USD wire (slight cash premium); rentals usually UYU with UI/USD adjustment
- **ITP customarily split 2% + 2%** but negotiable — premium PdE deals sometimes shift split
- **Strong tenant protection** (Ley 14.219) — long-term residential buy-to-let has 2-yr minimum + slow eviction; STR often more attractive financially but seasonal (PdE) and subject to the **national Ley 20.352 STR registry** (reglamentary decree still draft — pending mid-2026)
- **Punta del Este seasonality**: Jan–Feb peak, Apr–Nov occupancy collapses (~5–15%) → STR yields concentrated in 2–3 months
- **Estudio de títulos (30-yr chain)** is mandatory escribano practice — do NOT skip; non-Uruguayan buyers especially should verify escribano is AEU-registered
- **Certificados (DGI, BPS, OSE, UTE, Intendencia)** required pre-escritura — ensures no hidden debts attached to padrón
- **UI vs UYU vs USD pricing** means inflation translation matters — long-term comparisons require deflating to UI or USD
- **Ley 19.210 (financial inclusion, modified by LUC Ley 19.889 of 9 Jul 2020)**: real-estate cash payments capped at **1,000,000 UI** (~USD 120,000 at 2026 UI) — amounts above MUST use banking channels (transferencia, cheque, débito); the original 40,000 UI / Art. 39 rule was REPEALED by LUC; AML compliance
- **National STR registry (Ley 20.352)**: STR owners/operators must register in the Mintur **Registro de Operadores Turísticos** once in force; reglamentary decree still draft (proyecto late Nov 2025), not yet enforced mid-2026 — Maldonado's role limited to reinforcing informal-supply control in Punta del Este/Piriápolis
- **Foreign owners may face IP (Patrimonio)** if structured via SA/SRL holding — natural-person ownership often avoids; consult contador
- **No inheritance tax** since 1976 — major succession-planning attraction
- **Bearer shares abolished** (Ley 18.930) — corporate transparency; identifying real owners now mandatory at AGESIC + DGI

## Reddit / forum sources

- **r/uruguay** — general; some real-estate threads; bilingual ES/EN
- **r/CapitalDelMar** (Punta del Este focus, smaller community)
- **r/ArgentinaBenderEnUY** — Argentine relocation perspective
- **expat.uy** — local expat forum (some real-estate Q&A)
- **ExpatFocus Uruguay** — international expat aggregator with UY-specific subforum
- **InternationalLiving.com Uruguay** — heavily marketing-driven; cross-check
- **Facebook**: "Argentinos en Uruguay", "Brasileiros no Uruguai", "Expats in Uruguay" (large Argentinian/Brazilian relocation cohorts)

## Verification authorities

| Authority | When to call |
|---|---|
| **DNC (Dirección Nacional de Catastro)** | Padrón verification, VRC, plano de mensura |
| **Registro de la Propiedad — Sección Inmobiliaria** | Title chain, inscripción, gravámenes |
| **MEF (Ministerio de Economía y Finanzas)** | Tax framework, COMAP, investment certifications |
| **DGI (Dirección General Impositiva)** | IRPF / IRNR / IP / ITP, certificados |
| **BPS (Banco de Previsión Social)** | Labor/social-security certificate (esp. for new construction) |
| **OSE** | Water/sewer certificate + connection status |
| **UTE** | Electric utility certificate |
| **Intendencia (Departamental gov)** | Contribución, certificado urbanístico, habilitación |
| **Dirección Nacional de Migración (DNM)** | Residencia status |
| **Asociación de Escribanos del Uruguay (AEU)** | Verify escribano credential + history |
| **MVOT / ANV** | VIS, social housing financing |

## Quirks to know

- **Padrón vs cédula catastral**: padrón = parcel ID, cédula catastral = DNC valuation reference doc — both quoted in escritura
- **VRC re-aforo lag**: last general re-valuation 2012; current VRCs annually adjusted but typically 30–60% below market — major re-valuation is a long-discussed risk
- **2% + 2% ITP customary split**: but negotiable; verify on contract
- **Condominio horizontal Ley 14.261**: governs PH; reglamento de copropiedad must be reviewed; expensas can be steep in premium torres
- **Usufructo for inheritance planning**: very common — parents transfer nuda propiedad to children, retain usufructo for life; tax-efficient given no inheritance tax already
- **LATU certifications**: Laboratorio Tecnológico del Uruguay handles materials testing — relevant for new construction quality verification
- **Ley 19.210 (financial inclusion, as modified by LUC Ley 19.889/2020)**: cash payment cap now **1,000,000 UI** — non-bank-channeled cash above the cap invalidates contract for tax/escribano purposes — full transactions go through banking system; AML verification on funds origin (especially large foreign inflows); the prior 40,000 UI rule was repealed
- **BHU vs ANV**: BHU lends UI-indexed mortgages; ANV oversees VIS programs + housing policy
- **Bearer shares ended** (Ley 18.930) + AGESIC beneficiario final registry — corporate ownership now nominal; foreign ownership via SA still possible but transparent
- **MERCOSUR residencia fast-track**: AR/BR/PY citizens (and associated countries) get expedited residencia — relevant for cross-border investors
- **Free Zones (Zonamerica + Aguada Park)** — corporate IRAE exemption; foreign professionals working from FZ may have specific tax + immigration treatment
- **Punta del Este "seña" custom**: USD cash seña (5–10% of price) common at boleto stage — handle via escribano escrow given Ley 19.210

## Source URL templates

| Source | URL pattern |
|---|---|
| DNC Catastro | `http://sede.catastro.gub.uy/Sede/` |
| Registro de la Propiedad (DGR) | `https://www.gub.uy/ministerio-educacion-cultura/politicas-y-gestion/direccion-general-registros` |
| MEF | `https://www.gub.uy/ministerio-economia-finanzas/` |
| DGI | `https://www.dgi.gub.uy/` |
| BPS | `https://www.bps.gub.uy/` |
| BCU (UI value, FX) | `https://www.bcu.gub.uy/` |
| INE Estadísticas Inmobiliarias | `https://www.ine.gub.uy/inmuebles` |
| OSE | `https://www.ose.com.uy/` |
| UTE | `https://portal.ute.com.uy/` |
| MTOP DNV (vialidad nacional, institutional) | `https://www.gub.uy/ministerio-transporte-obras-publicas/` |
| MTOP Geoportal (TPDA + estaciones) | `https://geoportal.mtop.gub.uy/` |
| MTOP — Sistema de relevamiento estadístico de tránsito (per-station TPDA) | `https://geoportal.mtop.gub.uy/-/sistema-de-relevamiento-estadistico-de-transito` |
| Intendencia de Montevideo | `https://montevideo.gub.uy/` |
| Intendencia de Maldonado | `https://www.maldonado.gub.uy/` |
| MVOT (vivienda) | `https://www.gub.uy/ministerio-vivienda-ordenamiento-territorial/` |
| ANV | `https://www.anv.gub.uy/` |
| COMAP | `https://www.gub.uy/ministerio-economia-finanzas/comap` |
| AEU (escribanos) | `https://www.aeu.org.uy/` |
| DNM (migración) | `https://www.gub.uy/ministerio-interior/politicas-y-gestion/acerca-direccion-nacional-migracion` |
| INUMET | `https://www.inumet.gub.uy/` |
| DINAGUA | `https://www.gub.uy/ministerio-ambiente/politicas-y-gestion/agua` |
| SINAE | `https://www.gub.uy/sistema-nacional-emergencias/` |
| InfoCasas | `https://www.infocasas.com.uy/` |
| Mercado Libre Inmuebles UY | `https://inmuebles.mercadolibre.com.uy/` |
| Gallito | `https://www.gallito.com.uy/inmuebles` |
| Properati UY | `https://www.properati.com.uy/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row |
| Cámara Inmobiliaria UY | `https://www.ciu.com.uy/` |

## Status

✅ **Fully populated** as of 2026-05-01.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: **HIGH** for tax-residency / ITP / cadastre / notary / OSE / DGI source paths (all primary state agencies, multi-source corroborated). **MEDIUM** for current Intendencia-by-Intendencia Contribución Inmobiliaria bracket exactness (varies annually + per departamento — must verify per ordenanza current year). **MEDIUM** for STR regulation (national Ley 20.352 reglamentary decree still draft — pending mid-2026, revisit before the 2026-27 summer season).
**Last verified**: 2026-05-27 (traffic source (per-station TPDA) corrected 2026-09-18 per MTOP geoportal). Ley 20.352 STR registry text re-read at IMPO 2026-09-24 in the October regwatch wave; decree still a draft per IMPO (no reglamentación note) + Carmelo Portal 10 Sep 2026 (secondary); '>5 lets/año' trigger not found in the law text.

## Extension TODOs (deepen on first real run)

- [ ] Per-departamento Contribución Inmobiliaria bracket scraping (top 5: MVD, Maldonado, Canelones, Colonia, Salto)
- [ ] Ley 20.352 reglamentary decree tracking (national STR regime — draft pending mid-2026; revisit before 2026-27 summer season)
- [ ] OSE Mapa de Saneamiento per-padrón coverage extraction
- [ ] Ley 19.937 sunset/renewal monitoring (2031 watershed: first cohort exits 11-yr exemption)
- [ ] Re-aforo catastral nacional risk monitor (MEF + DNC announcements)
