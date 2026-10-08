# Argentina 🇦🇷 — Property Due-Diligence Playbook

ISO2: `ar`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (CPA)**: 4 digits + letter prefix + 3 chars (`C1414BFE` Buenos Aires, `M5500AAB` Mendoza, `R8400CBO` Bariloche)
- **Admin levels**: 23 provincias + CABA (Ciudad Autónoma de Buenos Aires) + 2,259 municipalities
- **Currency**: **ARS** (Argentine peso) + **USD billete** (real-estate market is USD-denominated)
- **Languages**: Spanish (de facto)
- **Cadastre — provincial fragmentation**:
  - **Registro de la Propiedad Inmueble** per province (CABA + 23 provinces)
  - **Catastro** also provincial (e.g., **ARBA** in PBA, **ATM** Mendoza)
  - **ARCA (ex-AFIP) — Agencia de Recaudación y Control Aduanero** (renamed by **Decreto 953/2024**, B.O. 2024-10-25, effective 2024-11-05; legal successor inheriting AFIP competencies + personnel + functions) — federal tax integration via CDI/CUIT for foreigners. URL `afip.gob.ar` redirects/coexists with `arca.gob.ar` (2026-05-27 verified).
- **Identifier**: matrícula (per provincial registry)
- **Escribano público (notary)** — buyer-chosen and **mandatory**; pulls certificado de dominio + inhibiciones
- **Ownership types**: dominio pleno (freehold); usufructo; condominio; PH (propiedad horizontal — apartments)

## Section: `--price`

### Primary sources

- **INDEC** (national stats): `https://www.indec.gob.ar/` — limited housing detail due to currency volatility
- **Reporte Inmobiliario** monthly market reports
- **Banco Nación + BCRA** for new mortgage data (mortgages restarted 2024)
- **TheLatinvestor** aggregated data

### Listing platforms

- **Zonaprop** — DOMINANT national portal: `https://www.zonaprop.com.ar`
- **Argenprop**: `https://www.argenprop.com`
- **MercadoLibre Inmuebles**: `https://inmuebles.mercadolibre.com.ar`
- **Inmoclick** (regional): `https://www.inmoclick.com.ar`
- **Reporteinmobiliario.com** — market data

**USD vs ARS**: Sale listings overwhelmingly in **USD billete**; rentals in ARS but with USD/CER/UVA adjustment clauses now allowed post-DNU.

### 2026 price benchmarks (Reporte Inmobiliario / TheLatinvestor)

| Region | USD/m² (typical) | Trend |
|---|---:|---|
| **CABA Puerto Madero** | $3,200–$7,000 (avg $6,100) | luxury |
| **CABA Palermo** | $2,800–$3,900 (avg $3,400) | +6% USD H1 2026 |
| **CABA Recoleta** | $3,000–$4,500 | rising |
| **CABA Belgrano** | $2,500–$3,500 | rising |
| **CABA Caballito** | $1,800–$2,800 | flat |
| **Pilar/Nordelta** (suburbs) | $1,500–$3,000 | rising |
| **Mendoza city** | $1,500–$3,000 | +5-7% USD |
| **Córdoba city** | $1,200–$2,000 | +5% USD |
| **Bariloche premium** (Arelauquen, Lago Moreno, Cerro Catedral) | $2,800–$5,100 | +5-9% YoY USD |
| **Bariloche value** (Ñireco, Las Victorias) | $1,600–$2,800 | +5-9% |
| **Bariloche avg property** | ~$250k blended | +5-9% |
| **Mar del Plata** | $1,200–$2,500 | +3-5% |

### Compute

1. USD/m² = price / **superficie cubierta** (covered area)
2. **USD-denominated**: most listings + transactions in USD billete
3. Cross-check **Zonaprop asking** + **Reporte Inmobiliario** monthly data
4. **CABA premium**: Puerto Madero > Palermo > Recoleta > Belgrano

### Key terms

- Matrícula = title identifier
- Escribano público = notary (mandatory + buyer-chosen)
- Certificado de dominio = title certificate
- Inhibiciones = encumbrances
- Boleto de compraventa = pre-escritura agreement
- COTI = **ARCA (ex-AFIP)** listing declaration

---

## Section: `--traffic`

### Sources

- **DNV (Dirección Nacional de Vialidad)**: `https://www.argentina.gob.ar/transporte/vialidad-nacional/`
- **DPV provincial vialidad** (Vialidad Buenos Aires, etc.)
- **CABA Movilidad**: `https://buenosaires.gob.ar/movilidad`

### Key term

**TMDA (Tránsito Medio Diario Anual)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural Patagonia)
- 🟡 1,500–10,000 v/d (suburban arterial, provincial roads)
- 🟠 10,000–35,000 v/d (Buenos Aires arterials, RP-2, autopistas)
- 🔴 > 35,000 v/d (General Paz, Panamericana, 9 de Julio, Riccheri)

---

## Section: `--tax`

### Annual property tax — Impuesto Inmobiliario

**Provincial — varies by province:**

| Province | Rate (annual on fiscal value) |
|---|---:|
| CABA (ABL) | ~0.6–1.2% |
| PBA | ~0.5–1.5% |
| Mendoza | ~0.5–1.0% |
| Córdoba | ~0.5–1.5% |

- Fiscal value typically below market (similar to LatAm)
- Annual or quarterly installments

### Transaction taxes

#### Sellos (stamp duty) — provincial

| Province | Rate |
|---|---:|
| CABA | ~3.5% |
| PBA | ~3.6% |
| Mendoza | ~3.0% |
| Córdoba | varies |

#### ITI (Impuesto a la Transferencia de Inmuebles) — **DEROGATED 2024-07-08**

- **REPEALED by Ley 27.743 (Medidas Fiscales Paliativas y Relevantes), Título IV art. 67**, in force from B.O. publication **8 Jul 2024**. The 1.5% transfer tax **no longer applies** to any property transfer regardless of acquisition date (2026-05-27 verified, source ARCA novedad 3808 + Colegio Escribanos PBA Ficha #01 2024-09-16 + argentina.gob.ar).
- **Capital gains 15% (cedular Impuesto a las Ganancias)** for inmuebles acquired from 2018-01-01 onward **continues to apply** — NOT derogated. Pre-2018 acquisitions transferred after 2024-07-08 are now effectively **untaxed at the federal level on transfer** (primary residence still exempt).
- COTI (Código de Oferta de Transferencia de Inmuebles) now administered by **ARCA (ex-AFIP)**.

### Bienes Personales (wealth tax) — current 2026 schedule (Ley 27.743 + IPC-indexed thresholds)

**Per ARCA Resolución FY 2025 declared 2026** (IPC-adjusted; verify each año):
- **Mínimo no imponible (non-taxable threshold)**: **ARS 384,702,388.90** (~USD 320k at MEP)
- **Casa-habitación exemption (primary residence)**: **ARS 1,346,458,361.17** (~USD 1.12M at MEP)
- **Rate schedule (FY 2025 declared 2026)** — multi-tramo with cumplidor (compliant-taxpayer) discounts:
  - First tramo (up to ARS 52,660,771.80 over the mínimo): **0.50%** general / **0%** cumplidores
  - Second tramo (52.66M–114.10M over mínimo): **0.75%** general / **0.25%** cumplidores
  - **Top bracket steps down every fiscal year** under **Ley 27.743 art. 63** (B.O. 2024-07-08), which rewrote art. 25 of Ley 23.966: FY2023 **0.50–1.50%** → FY2024 **0.50–1.25%** → FY2025 **0.50–1.00%** → FY2026 **0.50–0.75%** → flat **0.25%** from FY2027. The FY2025 scale declared in 2026 therefore tops out at **1.00%** (2026-08-07 verified, source [Ley 27.743 texto](https://biblioteca.afip.gob.ar/dcp/LEY_C_027743_2024_06_27)).
- **Foreign-asset surcharge eliminated retroactively to FY 2023** by Ley 27.743 (sanctioned June 2024) — unified schedule for foreign + domestic assets
- **REIBP optional prepayment** scheme exists (Ley 27.743 Régimen Especial); rates negotiated under the régimen

(2026-05-27 verified, source [ARCA alícuotas](https://www.afip.gob.ar/gananciasYBienes/bienes-personales/conceptos-basicos/alicuotas.asp) + iprofesional 2026 escalas + Errepar mínimos 2025.)

### Capital gains

- **15%** on real-estate appreciation (foreigners typically **13.5%** via withholding)

### Capital-gains rate for non-residents

- ~**13.5% effective** for non-residents on real-estate appreciation (15% × 90% presumed gain, via ARCA withholding RG) — verify per transaction with notario/escribano.

### COTI

**ARCA (ex-AFIP) COTI (Código de Oferta de Transferencia de Inmuebles)** must be obtained pre-listing if price > threshold.

### Total transaction cost (buyer side) — post-ITI repeal

- CABA: **~4.5-6.5%** (3.5% sellos + ~1-2% escribano + 0.5-1% other; ITI 1.5% no longer applies after 2024-07-08)
- PBA: **~4.5-6.5%**
- Mendoza: **~3.5-5.5%**

---

## Section: `--rental`

### Long-term residential — DNU 70/2023 LIBERALIZED

**MAJOR REFORM**:
- **DNU 70/2023 (Milei, B.O. 2023-12-21, in force from 2023-12-29)** repealed Ley 27.551
- **Consolidated by Ley Bases (Ley 27.742, sanctioned 2024-06-27, promulgated + B.O. 2024-07-08)** — now PERMANENT LAW, not at-risk decree
- New contracts: **free duration, free currency** (USD/UVA/CER/IPC), **free deposit**
- **Pre-existing Ley 27.551 contracts** continue under Ley 27.551 — only new contracts post-DNU use the new liberalized regime (grandfathering) (2026-05-27 verified).

### Short-let

- **CABA**: Registry with Ente de Turismo (Ley 4631 + 6255); short-let licence + ABL surcharge
- **DNU + Ley Bases** liberalized rental market — landlord-favorable

### Tax on rental

- Residents: progressive income tax
- Non-residents: 21% withholding
- Currency: ARS or USD (depending on contract)

---

## Section: `--work=<profession>`

### Sources

- **Bumeran** — biggest job board: `https://www.bumeran.com.ar`
- **ZonaJobs**, **Computrabajo**, **LinkedIn AR**, **Indeed.com.ar**
- **Ministerio de Trabajo (MTSS)**: `https://www.argentina.gob.ar/trabajo`

### Self-employment

- **Monotributo** simplified regime — 2026 cap (category K, highest) **ARS 108,357,084.05/year** (~ARS 108M) per Feb 2026 re-indexation (+14.29% IPC); category A floor ARS 10,277,988.13 (semestral indexation by ARCA)
- **Responsable Inscripto** for higher revenue + IVA registration
- **IIBB** provincial gross-receipts tax

### Salary benchmarks (2026)

- Median monthly gross:
  - CABA: ~ARS 1,000,000–1,800,000 (~USD 850–1,500 at MEP)
  - Córdoba/Mendoza: ~ARS 800,000–1,400,000
  - Smaller cities: ~ARS 600,000–1,000,000
- **Salario Mínimo Vital y Móvil**: **ARS 357,800/month** (April 2026, Resolución 9/2025 del Ministerio de Capital Humano) — cronograma: Marzo ARS 352,400, Abril ARS 357,800, Mayo ARS 363,000, Agosto ARS 376,600 (2026-05-27 verified).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **INPRES (Instituto Nacional de Prevención Sísmica)** | `https://www.inpres.gob.ar/` | Seismic monitoring + INPRES-CIRSOC 103 building code |
| **SEGEMAR** | `https://www.segemar.gov.ar/` | Geology + cross-border volcanic |
| **OVDAS Chile** (cross-border Patagonia) | — | Volcanic monitoring |
| **SMN (Servicio Meteorológico Nacional)** | `https://www.smn.gob.ar/` | Weather, climate |
| **INA (Instituto Nacional del Agua)** | `https://www.ina.gob.ar/` | Hydrology, flood |

### Specific risks

#### Earthquake — significant

- **INPRES seismic zones** 0-4 (4 highest)
- **Cuyo (Mendoza, San Juan, La Rioja)**: Zone 4 — highest hazard
- **Patagonia, NW**: Zone 1-3 moderate
- **CABA + Pampas**: Zone 0-1 (low)
- **INPRES-CIRSOC 103** building code applies to seismic zones

#### Volcanic

- **Andes Patagonia**: Lanín, Llaima, Villarrica (Chile-side affecting AR)
- **Mendoza area**: Maipo, Tupungato
- **2008 Chaitén** ash affected Bariloche

#### Other

- **Flood**: Buenos Aires province, Tigre delta (chronic)
- **Climate**: Pampas mega-drought 2018-2023 receding
- **Patagonia warming** + glacier retreat
- **Wildfire**: Patagonia + Cuyo summer

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **1900–1980 (modernist boom)** | Asbestos common, dated wiring |
| **1980–2010** | Improved standards, post-Caracas/Mexico quake reforms |
| **Post-2010** | EC8-equivalent + INPRES-CIRSOC 103 |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Escritura pública + escribano** | Mandatory closing |
| **Certificado de dominio + inhibiciones** | ≤15 days valid |
| **Plano de mensura registered** | Cadastre |
| **Libre deuda municipal/ABL + provincial + AySA/EDENOR** | No-debts certificates |
| **ARCA (ex-AFIP) COTI + retentions** | Tax compliance |

### Climate change projections

- **est. ~+2.0–3.5°C** by 2100 (scenario-dependent; verify against IPCC AR6 / SMN national climate communication)
- **Patagonia warming faster** + glacier retreat
- **Pampas drought intensification**
- **Andes snowpack decline** affecting hydropower

---

## Section: `--mains`

### Sources

- **AySA** (CABA + 26 PBA municipalities): `https://www.aysa.com.ar/`
- **ABSA** (rest of PBA): `https://www.aguasbonaerenses.com.ar/`
- **Aguas Cordobesas, AYSAM (Mendoza), Aguas Rionegrinas** etc.
- Rural Patagonia + Cuyo: cisterns + pozos negros / cámara séptica + lecho nitrificante

### Costs

| Scenario | Cost (USD) |
|---|---:|
| Mains connection | $2,000–$5,000 |
| Septic + cámara | $3,000–$8,000 |
| Pozo negro | $1,000–$3,000 |
| Bored well (Patagonia) | $4,000–$10,000 |

---

## Cost benchmarks (AR 2026)

| Work | Cost (USD typical) |
|---|---:|
| Inspection (relevamiento) | $300–$700 |
| Escribano fees | 1.5–2.5% of price |
| Sellos provincial | 3–3.6% |
| ITI federal | REPEALED 2024-07-08 (Ley 27.743 art. 67) — no longer applies |
| Realtor commission | 3-4% per side typical |
| **Total transaction cost (buyer CABA)** | **~6–8%** of price |
| Roof renovation | $5,000–$15,000 |
| Asbestos abatement | $3,000–$10,000 |
| Earthquake retrofit (Cuyo) | $20,000–$80,000 |
| Energy retrofit | $10,000–$40,000 |
| Solar PV (5kW) | $5,000–$10,000 |

## Active fiscal incentives (2025-2026)

- **Mortgage market reopening 2024-2025**: 30+ banks offering UVA loans + USD-linked
- **Cepo cambiario partial lift effective 2025-04-14** (BCRA Phase 3, announced 2025-04-11): natural persons can buy USD officially (USD 200/mo cap eliminated; cross-restriction lifted); exchange-rate **band ARS 1,000–1,400/USD** floating within band, adjusting ±1% monthly; IMF EFF USD 20bn supports the program. Legacy dividend stocks pre-2025 + pre-2023-12 commercial debt still routed via BOPREAL (2026-05-27 verified, source BCRA news).
- **PROCREAR** still active (state housing program)
- **Zonas Francas** for commercial

## Common listing platforms

- **Zonaprop** — DOMINANT
- **Argenprop**, **MercadoLibre Inmuebles**, **Inmoclick**
- **Reporteinmobiliario.com** — market data

## Caveats unique to AR

- **USD-denominated market** — listings + transactions in USD billete, NOT pesos
- **Currency controls (cepo cambiario)** — partially lifted April 2025; restrictions on companies remain
- **Currency arbitrage** (oficial / blue / MEP / CCL) historically — gap narrowing since 2024
- **High inflation** (peso depreciation) makes ARS-denominated investments meaningless
- **Capital gains** unusual: 15% on real-estate gains (was 0% pre-2018)
- **Bienes Personales** wealth tax — major issue for foreigners; reformed by **Ley 27.743 art. 63** (B.O. 2024-07-08) into a single scale over Argentine + foreign assets whose top bracket drops each year: FY2024 0.50–1.25% → FY2025 0.50–1.00% → FY2026 0.50–0.75% → flat **0.25%** from FY2027 (2026-08-07 verified)
- **DNU 70/2023 + Ley Bases (Ley 27.742)** — rental market liberalization NOW PERMANENT
- **Boleto de compraventa** pre-escritura common
- **Foreigners cannot buy rural land >1,000 ha** in the core Pampas zone (Ley 26.737 — **still in force**; equivalent-productive-area limits apply elsewhere); also **15% provincial cap** (foreigners may not own >15% of provincial rural land) and **30% same-nationality sub-cap** within that 15%; water-body adjacency + border-security-zone prohibitions are separate. **Milei's DNU 70/2023 attempted to repeal Ley 26.737 but that specific provision is frozen pending Supreme Court / Congressional review** (2026-05-27 verified).
- **Border-zone restrictions** (150 km Andes/Patagonia border) — INTRA federal approval required
- **ARCA (ex-AFIP) COTI** declaration mandatory pre-listing
- **Escribano público mandatory + buyer-chooses** — UNIQUE
- **23 provincias + CABA different sellos rates**
- **Mortgage market restarted 2024** after long hiatus
- **Cepo lift April 2025** — can now hold USD officially as natural person
- **Bariloche** USD-denominated tourism + lifestyle premium

## Reddit / forum sources

- **r/argentina** — biggest community
- **r/BuenosAires**, **r/PERSONAL_FINANCE_AR**
- **r/Bariloche**, **r/Mendoza**, **r/Cordoba**
- **Buenos Aires Times** (English)
- **Reporte Inmobiliario** monthly newsletters
- **TheLatinvestor** market analysis

## Verification authorities

| Authority | When to call |
|---|---|
| **Registro de la Propiedad Inmueble (provincial)** | Title verification |
| **Catastro provincial** | ARBA / ATM cadastre |
| **Escribano público** (buyer-chosen) | Mandatory closing |
| **ARCA (ex-AFIP)** | Federal taxes + COTI + CDI (Decreto 953/2024, eff. 2024-11-05) |
| **INTRA** | Border-zone foreign approval (Patagonia/Andes) |
| **Municipal** | ABL + permits |
| **PRT (Ente de Turismo CABA)** | If short-let |
| **INPRES** | Seismic risk |

## Source URL templates

| Source | URL pattern |
|---|---|
| Zonaprop | `https://www.zonaprop.com.ar/` |
| Argenprop | `https://www.argenprop.com/` |
| MercadoLibre Inmuebles | `https://inmuebles.mercadolibre.com.ar/` |
| Reporte Inmobiliario | `https://www.reporteinmobiliario.com/` |
| INDEC | `https://www.indec.gob.ar/` |
| BCRA | `https://www.bcra.gob.ar/` |
| ARCA (ex-AFIP) | `https://www.arca.gob.ar/` (legacy `https://www.afip.gob.ar/` also resolves) |
| INPRES seismic | `https://www.inpres.gob.ar/` |
| SEGEMAR | `https://www.segemar.gov.ar/` |
| SMN | `https://www.smn.gob.ar/` |
| AySA (CABA water) | `https://www.aysa.com.ar/` |
| ARBA (PBA cadastre) | `https://www.arba.gov.ar/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Last verified**: 2026-08-07.
**Coverage check**: pricing (Reporte Inmobiliario + Zonaprop + TheLatinvestor 2026), traffic (DNV TMDA), tax (provincial inmobiliario + sellos + **ITI federal REPEALED 2024-07-08** by Ley 27.743 art. 67 + Bienes Personales reformed by Ley 27.743 art. 63 (single scale over Argentine + foreign assets, top bracket stepping down FY2025 1.00% → FY2026 0.75% → flat 0.25% from FY2027) with IPC-indexed 2026 thresholds + 15% CGT post-2018 + **AFIP→ARCA** rename Decreto 953/2024), rental (DNU 70 + Ley Bases liberalized), work (Monotributo K cap ARS 108M; SMVM ARS 357,800 Abr 2026), risks (INPRES Cuyo Zone 4 + Patagonia volcanic + flood Tigre; Ley 26.737 still in force, frozen DNU 70 repeal), mains (AySA + ABSA + provincial), cepo (Phase 3 lift 2025-04-14 with band ARS 1,000-1,400/USD).
**Confidence**: HIGH for Bienes Personales reform schedule (Ley 27.743) + DNU 70/2023 + Ley Bases consolidation June 2024 + cepo partial lift April 2025; HIGH for Zonaprop + Reporte Inmobiliario market data; MEDIUM for provincial registry URL stability (varies); MEDIUM for further Milei tax-cut announcements (March 2026 unenacted as of writing).

## Extension TODOs

- [ ] Per-province registry URL + lookup flow
- [ ] Per-province sellos rates table
- [ ] Bienes Personales calculator with the Ley 27.743 art. 63 step-down scale (FY2025 0.50–1.00% / FY2026 0.50–0.75% / flat 0.25% from FY2027)
- [ ] Cepo cambiario lift impact on transactions
- [ ] Mortgage product comparison (UVA vs USD-linked)
- [ ] DNU 70 / Ley Bases rental contract templates
- [ ] Border-zone INTRA approval flow (Patagonia/Andes 150km)
- [ ] CABA Airbnb registry tracker (Ley 4631+6255)
- [ ] Bariloche USD-denominated market specifics
- [ ] CABA neighborhood premium tracker (Puerto Madero/Palermo/Recoleta)
