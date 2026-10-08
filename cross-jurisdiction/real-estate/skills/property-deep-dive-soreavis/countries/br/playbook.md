# Brazil 🇧🇷 — Property Due-Diligence Playbook

ISO2: `br`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (CEP)**: 8 digits in `XXXXX-XXX` format (`01310-100` Avenida Paulista, `22070-000` Copacabana, `30130-000` BH centro)
- **Admin levels**: 26 states + DF (Brasília) + 5,570 municípios
- **Currency**: **BRL** (Brazilian real); 1 USD ≈ 5–6 BRL; 1 EUR ≈ 5.5–6.5 BRL
- **Languages**: Portuguese (official); regional indigenous languages
- **Cadastre — decentralized + transitioning to national**:
  - **Cartórios de Registro de Imóveis** (per-município; ownership only transfers when escritura registered)
  - **Matrícula** = unique property ID (life-of-property record)
  - **CIB (Cadastro Imobiliário Brasileiro) "CPF dos Imóveis"** — national single property identifier, 7 alphanumeric characters + check digit. Instituted by **IN RFB 2.030/2021**; Sinter under **Decreto 11.208/2022**; notarial/registry adoption under **IN RFB 2.275/2025**. **In force from Jan 2026** for federal administration, notarial/registry services and state capitals + DF (LC 214/2025 art. 266 I — 12-month deadline); **state administration + all remaining municipalities from Jan 2027** (art. 266 II — 24 months). Inscription is mandatory for all urban and rural properties and BICE (art. 265), but per the Receita Federal FAQ only urban properties in capitals/DF are obliged during 2026 — other municipalities from Jan 2027; all rural properties must already hold a CIB (via CNIR/Cafir). **Does NOT replace the cartórios** — deeds, land registration and certificate issuance stay with the cartórios, and cadastre upkeep stays with prefeituras (urban) / INCRA (rural); cartórios and municipalities must merely carry the CIB code in their documents (2026 data, 2026-08-07 verified, source: [Receita Federal CIB FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib) + Planalto LC 214/2025)
  - **SINTER** (Sistema Nacional de Gestão de Informações Territoriais)
  - **INCRA** (`https://www.gov.br/incra/pt-br`) — rural land registry
- **Identifier**: matrícula (per-cartório); CIB (national, rolling out)
- **Foreign buyer needs CPF** before any transaction
- **Ownership types**: pleno domínio (full); usufruct; multipropriedade (timeshare, Lei 13.777/2018)

## Section: `--price`

### Primary sources

- **FIPE-ZAP Index** (FGV/Fipe): `https://www.fipe.org.br/en-us/indexes-and-indicators/fipezap` — most-cited; 500k+ valid listings/month
- **IBGE Vivienda**: `https://www.ibge.gov.br/` — census + housing surveys
- **BCB (Banco Central) Real Estate Market Report**: `https://www.bcb.gov.br/`
- **CBIC (Câmara Brasileira da Indústria da Construção)**

### Listing platforms

- **ZAP Imóveis + VivaReal** — DOMINANT (merged under Grupo OLX/Adevinta): `https://www.zapimoveis.com.br`, `https://www.vivareal.com.br`
- **Imovelweb**, **OLX Imóveis**: `https://www.olx.com.br/imoveis`
- **Quinto Andar** (rental + sales innovator): `https://www.quintoandar.com.br`
- **DataZAP** for analytics
- **Loft** (urban resale, fintech-backed)

### 2026 price benchmarks (FIPE-ZAP Q1 2026)

| Region | BRL/m² (apt) | YoY |
|---|---:|---:|
| **São Paulo Vila Nova Conceição** | 20,000–38,000 | +6.11% (+0.55% real) |
| **São Paulo Jardins** | 17,000–35,000 | +6.11% |
| **São Paulo Itaim Bibi** | 19,400 | +6.11% |
| **São Paulo Pinheiros** | 18,400 | +6.11% |
| **São Paulo Butantã/Santana** | 5,500–9,000 | +6.11% |
| **Rio de Janeiro Ipanema/Leblon** | 25,000–40,000 | +4.62% (-0.87% real) |
| **Rio de Janeiro avg** | 12,000–15,000 | +4.62% |
| **Brasília avg** | 9,750 | +5.5% |
| **Brasília Plano Piloto** | 10,000–12,000 | +5.5% |
| **Belo Horizonte avg** | 10,850 | +5.0% |
| **Belo Horizonte Savassi** | 7,000–9,000 | +5.0% |
| **Curitiba** | 6,500–8,100 | +5.5% |
| **Florianópolis** | 10,000–15,000 (beach 15,000–30,000) | +12% |

### Compute

1. BRL/m² = price / **área privativa** (private area, NOT including common parts)
2. Cross-check **FIPE-ZAP** + **DataZAP** + recent matrícula transactions
3. **Valor venal vs market**: valor venal typically 30-60% below market (intentional)
4. **Convert BRL to USD/EUR** at current FX

### Key terms

- Matrícula = property "birth certificate" + life record
- Valor venal = municipal cadastral value (basis for IPTU + ITBI)
- Habite-se = occupancy permit
- Escritura pública = notarized deed
- Cartório de Registro de Imóveis = land registry (per-município)
- CIB = national property identifier, phased in Jan 2026 (federal administration + notarial/registry + state capitals & DF) → Jan 2027 (state administration + remaining municipalities)

---

## Section: `--traffic`

### Sources

- **DNIT (Departamento Nacional de Infraestrutura)**: `https://www.gov.br/dnit/pt-br` — federal highways (BR-roads)
- **DERSP (SP), DER-RJ, DER-MG, etc.** — state-level
- **CET-SP, RioCard** — city traffic data

### Key term

**VMD (Volume Médio Diário)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (collector, suburban)
- 🟠 10,000–35,000 v/d (urban arterial, BR-roads secondary)
- 🔴 > 35,000 v/d (Marginais SP, Ponte Rio-Niterói, BR-101 metropolitan)

---

## Section: `--tax`

### Annual property tax — IPTU

**Imposto Predial e Territorial Urbano** — annual; municipal.

| Município | Residential rate | Commercial/vacant |
|---|---:|---:|
| **São Paulo** | ~0.7–1.5% | ~1.1–1.9% |
| **Rio de Janeiro** | ~0.6–1.2% | ~1.0–1.5% |
| **Brasília** | ~0.3–1.0% | ~1.0–1.5% |
| **Belo Horizonte** | ~0.6–1.2% | ~1.0–1.5% |

- Rates above are **indicative ranges (est., c. 2025)** — verify the current rate against each município's IPTU legislation and annual reajuste decree (e.g. São Paulo via prefeitura.sp.gov.br)
- Base = **valor venal** (typically 30-60% below market)
- Annual or 10x monthly installments
- **Early payment 4-10% discount**

### Transaction taxes — ITBI

**Imposto sobre Transmissão de Bens Imóveis** — municipal:

| Município | ITBI rate |
|---|---:|
| **São Paulo** | **3%** (Lei Municipal SP 11.154/1991 Art. 10) of declared transaction value |
| **Rio de Janeiro** | **2%** (Lei Municipal RJ 1.364/1988); **0.5% MCMV-financed first acquisition** |
| Other municípios | 2–3% |

- **STJ Tema Repetitivo 1.113 (REsp 1.937.821/SP, Feb 2022)**: ITBI base = the **declared transaction value** (presumption of truth). The "valor venal de referência" (VVR) used unilaterally by São Paulo is unlawful as an automatic basis; municipality must challenge via administrative procedure. Buyers in SP routinely seek refunds where ITBI was paid on VVR rather than price (2026-05-27 verified, source: STJ Tema 1.113 / REsp 1.937.821/SP).

### Other taxes

- **ITR (Imposto Territorial Rural)**: rural; federal; INCRA-administered
- **ITCMD (Imposto sobre Transmissão Causa Mortis e Doação)** — state-level inheritance + lifetime-gift tax (separate from ITBI which is municipal + onerous-transfer-only). Constitutional ceiling **8%** (Resolução Senado Federal nº 9/1992). Indicative 2025 rates: SP 4% flat (Lei 10.705/2000); RJ 4–8% progressive (Lei 7.174/2015); MG 5% flat (Lei 14.941/2003); DF 4–6% progressive. **EC 132/2023 amended CF Art. 155 §1º VI to make ITCMD progressivity MANDATORY** (previously optional under STF RE 562.045/2013); EC 132/2023 Art. 23 III imposes a transitional immediate-implementation rule — many flat-rate states (SP, MG, ES, AL) have NOT yet legislated progressivity as of 2026-05, creating pending constitutional-incompatibility litigation risk (2026-05-27 verified, source: Senado Federal Resolução 9/1992 + EC 132/2023 text via Planalto + ConJur "Adesão dos estados às regras de ITCMD" May 2024).
- **IR (Imposto de Renda) ganho de capital**:
  - Residents AND non-residents: progressive **15% / 17.5% / 20% / 22.5%** at gains ≤ R$5M / R$5M–R$10M / R$10M–R$30M / > R$30M (Lei 13.259/2016 — progressivity extended to non-residents from 2017; "flat 15%" is the pre-2017 rule) (2026-05-27 verified, source: Planalto Lei 13.259/2016)
  - **R$35k small-sale exemption** applies to MOVEABLES (Lei 9.250/1995 Art. 22), NOT real estate
  - **R$440k "isenção do único imóvel"** (Lei 9.250/1995 Art. 23) — single residential property; seller must NOT have sold another residential property in last 5 years AND sale price ≤ R$440k
  - **180-day rollover (Lei 11.196/2005 Art. 39)** — sale of residential property exempt if proceeds reinvested in another residential property within 180 days; once per 5 years
- **IRPF 2026 filing window**: March 23 – May 29, 2026 (verify Instrução Normativa RFB defining 2026 window at receitafederal.gov.br)

### Cartório fees

- **Escritura**: ~0.5–2% of price (est. — set per-state; verify against the relevant tabela de emolumentos)
- **Registro**: ~0.5–1% of price (est. — set per-state; verify against the relevant tabela de emolumentos)
- **Combined**: ~1–2% mandatory closing

### Total transaction cost (buyer side)

- São Paulo standard: **~4–5%** (3% ITBI + 1-2% cartório)
- Rio standard: **~3–4%** (2% ITBI + 1-2% cartório)
- Plus optional valuation, lawyer, mortgage costs

### Future risk — REFORMA TRIBUTÁRIA

**Emenda Constitucional 132/2023** + **Lei Complementar 214/2025** (implementing statute, sanctioned January 2025) — major tax reform:
- **2026: TEST YEAR** — CBS **0.9%** + IBS **0.1%** = **1.0% combined test rate** (creditable against PIS/COFINS so net collection ≈ zero)
- **2027: CBS** goes live; CBS replaces **PIS + COFINS** (federal contributions) — **NOT IPI** (IPI is preserved with rates zeroed outside Zona Franca de Manaus under EC 132/2023 Art. 3º amending CF Art. 153 §3º)
- **2029: IBS** (state+municipal, replaces ICMS/ISS) phased in
- **2033: full system in place** — combined CBS+IBS standard rate ceiling ~26.5%
- **Real estate sector reductions (LC 214/2025 Art. 261)** (2026-05-27 verified, source: Planalto LC 214/2025):
  - **50% reduction** on standard rate for compra/venda + cessão de direitos sobre imóveis (effective ≈ 13.25%)
  - **70% reduction** for locação, cessão onerosa, arrendamento (effective ≈ 7.95%)
  - **40% reduction** for short-term rental < 90 days (treated as hotelaria)
- **Pessoa-física exemptions**: locação ≤ R$240k/year up to 3 properties; sale ≤ 3 imóveis/year
- **Redutor social on new residential sales**: R$100k (apartment/house) + R$30k (lot)
- **IPTU/ITBI/IR NOT directly changed** by reform — and the **CIB is an identifier layer, not a valuation authority**: cadastre upkeep stays with the prefeituras (urban) / INCRA (rural), and cartórios and municipalities merely carry the CIB code in their documents, so any IPTU/ITBI base movement still depends on each município updating its own outdated valor venal (2026-08-07 verified, source: [Receita Federal CIB FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib))

---

## Section: `--rental`

### Long-term residential

- **Lei do Inquilinato (Lei 8.245/1991)** — federal, governs all rental
- **Tenant protection moderate** (less strict than Argentina, more than US)
- 30-day notice tenant; 90-day notice landlord (or 30-day end-of-contract)
- **Fiador** (guarantor) common
- **Caução** (security deposit) up to 3 months

### Short-let (Airbnb)

- **Lei do Inquilinato** defines "locação por temporada" up to **90 days**
- Federally legal; **no national permit**
- **STJ ruling 2021**: condomínios CAN BAN STR entirely — dominant restriction
- **Rio de Janeiro**: municipal regulation in development (registration likely Copacabana/Ipanema)
- **Florianópolis**: ~40k active Airbnb listings; only Lei do Inquilinato + condomínio rules
- **No federal residency requirement**; secondary-home owners can legally STR

### Tax on rental

- **IR (income tax)** progressive on net rental
- Non-residents: 15% withholding
- IPTU paid by owner (tenant reimbursement common)

---

## Section: `--work=<profession>`

### Sources

- **MTE (Ministério do Trabalho)**: `https://www.gov.br/trabalho/`
- **Catho** — biggest job board: `https://www.catho.com.br/vagas`
- **Indeed.com.br**, **Vagas.com.br**, **InfoJobs**, **LinkedIn BR**
- **CRECI** for realtors; **CONFEA/CREA** for engineering

### Self-employment

- **MEI (Microempreendedor Individual)**: simplified, up to R$81k revenue
- **Simples Nacional**: small business, up to R$4.8M
- **CPF** required for foreigners
- **CNPJ** for business
- **PIS/COFINS** federal taxes (replaced by CBS in 2027)

### Salary benchmarks (2025)

- Median monthly gross:
  - São Paulo: ~R$5,000–R$10,000 (€900–€1,800)
  - Rio de Janeiro: ~R$4,500–R$9,000
  - Brasília (govt): ~R$6,000–R$12,000
  - Smaller cities: ~R$3,000–R$5,500
- **Salário mínimo**: **R$1.621/month (2026)** — reajuste 6,79% per INPC + PIB rule; Decreto nº 12.797 de 24-Dez-2025, in force 1-Jan-2026 (the R$1.518 figure was the 2025 value) (2026-05-27 verified, source: [Planalto Decreto 12.797/2025](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/d12797.htm))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **CEMADEN** | `https://www.cemaden.gov.br/` | Flood + landslide early warning (Decreto 7513/2011) |
| **CPRM (Serviço Geológico do Brasil)** | `https://www.cprm.gov.br/` | Geology, geological hazards |
| **INMET** | `https://portal.inmet.gov.br/` | Weather, climate |
| **IBAMA** | `https://www.ibama.gov.br/` | Environmental |
| **ANA (Agência Nacional de Águas)** | `https://www.ana.gov.br/` | Water management |

### Specific risks

- **Flooding + landslide** — major risk:
  - **Petrópolis Feb 2022**: 252.8mm in 3 hours, 231 fatalities — deadliest landslide on record in city
  - **Rio Grande do Sul May 2024 floods** — extensive damage, statewide emergency
  - **Feb 2026 Zona da Mata floods**: Juiz de Fora wettest month on record (4× monthly avg)
  - 17 rain gauges in Petrópolis since 2015 (CEMADEN)
- **Drought**: Northeast (sertão) — chronic
- **Rainforest fire**: Amazonas — increasing
- **Tropical storms**: northeast coast (Bahia, Ceará)
- **Earthquake risk LOW** (stable Brazilian shield)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990** | Asbestos common (banned 2017 nationally); lead paint |
| **Pre-1990 informal tenure** | Many favela properties without title |
| **1980s–2000s "casa-grande" reforma** | Variable construction quality |
| **Post-2000** | NBR codes tightened |
| **Post-2017 asbestos ban** | Modern materials |

### Mandatory at sale

| Document | Required because | Notes |
|---|---|---|
| **Certidão de matrícula atualizada** | Title (≤30 days) | Cartório de Registro de Imóveis |
| **Certidão negativa de ônus reais** | No-liens | Same |
| **Certidão negativa de débitos** | Federal (RFB), estadual, municipal (IPTU paid) | Multiple authorities |
| **Certidão de regularidade do condomínio** | No condo arrears | If apartment |
| **Habite-se** | Occupancy permit | Municipal |
| **IPTU + valor venal certificate** | Tax base | Municipal |
| **Personal certidões on seller** | CND federal, criminal, trabalhista, civil, tributária | Multiple |
| **Escritura pública** | At Tabelionato de Notas | Notary |
| **Registration at Cartório de Registro de Imóveis** | ONLY step that transfers ownership | CRITICAL |

### Climate change projections

- **~+2.0–4.0°C** by 2100 (est. — projection range; verify against IPCC AR6 / PBMC regional scenario for the relevant SSP/RCP pathway)
- **Amazon deforestation** + drying — global tipping point concern
- **Coastal sea-level rise**: **~+30–80 cm** by 2100 (Recife, Santos, Fortaleza vulnerable) (est. — projection range; verify against IPCC AR6 / PBMC regional scenario)
- **Drought intensification**: Northeast + Cerrado
- **Increased extreme rainfall** (Petrópolis 2022 type)

---

## Section: `--mains`

### Sources

- **SABESP** (SP): `https://www.sabesp.com.br/`
- **CEDAE** (Rio — partially privatized): `https://www.cedae.com.br/`
- **COPASA** (MG), **SANEPAR** (PR), state operators
- **ANA** federal regulator
- **Marco Legal do Saneamento (Lei 14.026/2020)**: universal access target 2033

### Verification

- **47% of population unassisted by sewage collection/treatment** (2020 data, most recent national — figures may have changed since)
- RJ ~15% unconnected; CEDAE-contracted municípios only 39.2% actually connected
- **SABESP committed R$47.4B 2024-28**; universalization target 2029
- **Favelas**: fossas (cesspits) common; informal connections widespread
- **Per-município coverage extremely uneven**

### Costs

| Scenario | Cost (BRL) |
|---|---:|
| Mains connection | 5,000–25,000 |
| Septic upgrade | 8,000–30,000 |
| Cisterna installation | 15,000–60,000 |
| Bored well | 25,000–80,000 |

---

## Cost benchmarks (BR 2026)

| Work | Cost (BRL) |
|---|---:|
| Vistoria (inspection) | 1,000–3,000 |
| Avaliação | 2,000–6,000 |
| Cartório fees (escritura + registro) | 1–2% of price |
| ITBI (SP) | 3% of higher-of price/valor venal |
| ITBI (Rio) | 2% |
| **Total transaction cost (buyer SP)** | **~4–5%** |
| **Total transaction cost (buyer Rio)** | **~3–4%** |
| Roof renovation | 30,000–100,000 |
| Asbestos abatement (post-2017 ban) | 20,000–80,000 |
| Earthquake retrofit | not standard (low risk) |
| Energy retrofit | 50,000–200,000 |
| Solar PV (5kW) | 25,000–45,000 |
| Reforma completa (apt) | 80,000–250,000 |

## Active fiscal incentives (2025-2026)

- **MCMV (Minha Casa Minha Vida) extension April 2026**:
  - **R$200B total / +R$20B Social Fund**
  - New ceiling: families up to **R$13k/month income** can finance up to **R$600k** properties
  - Mortgage tenor extended to **420 months (35 years)**
  - **Target: 3M units by end-2026** (election year)
- **CHF mortgage** — none specific to BR
- **Pró-Cotista FGTS** for FGTS-paying workers
- **Casa Verde Amarela** archived (replaced by MCMV)

## Common listing platforms

- **ZAP Imóveis + VivaReal** — DOMINANT (merged)
- **Imovelweb**, **OLX Imóveis**
- **Quinto Andar** (no-broker model)
- **DataZAP** analytics
- **Loft** (urban fintech)

## Caveats unique to BR

- **Cartório system**: decentralized + sometimes corrupt + expensive; ownership ONLY transfers on registration
- **Matrícula** = property "birth certificate" with full history
- **CIB ("CPF dos Imóveis") phased in Jan 2026 → Jan 2027** — in force Jan 2026 for federal administration, notarial/registry services and state capitals + DF; state administration + all remaining municipalities from Jan 2027 (LC 214/2025 art. 266 I / II); all rural properties must already hold a CIB (via CNIR/Cafir). It is a national *identifier* only — it does **NOT** replace the cartórios (deeds, land registration and certidões unchanged) and cadastre upkeep stays with prefeituras (urban) / INCRA (rural) (2026-08-07 verified, source: [Receita Federal CIB FAQ](https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib) + Planalto LC 214/2025)
- **Reforma Tributária** 2027 (CBS) → 2029 (IBS) → 2033 (full)
- **MCMV extension April 2026**: R$200B, R$13k/mo income, R$600k cap, 35-year term
- **Multipropriedade** (Brazilian timeshare) — large legal market (Lei 13.777/2018)
- **Foreign rural land caps** (statute: **Lei 5.709/1971** + Decreto 74.965/1974):
  - ≤25% of any município's rural land in foreign hands; ≤10% per single nationality (Art. 12)
  - **Módulo de Exploração Indefinida (MEI, Lei 5.709/1971 Art. 3º — NOT to be confused with Microempreendedor Individual)**: foreign natural persons can buy up to **3 MEIs** without INCRA authorization; per-município MEI size set by INCRA Normative Instructions (varies; upper bound often well above 100 ha in low-productivity ZTMs)
  - Foreign legal entities require INCRA + CNDR + national-security clearance for ANY acquisition (Art. 5º)
  - **Border strip 150 km** (Lei 6.634/1979 + CF Art. 20 II): presidential/congressional approval
  (2026-05-27 verified, source: Planalto Lei 5.709/1971)
- **Pre-1990 informal tenure**: many favela properties without title
- **Usucapião** (adverse possession) common path
- **Lei 6.815/80** repealed by **Lei de Migração 13.445/2017**
- **STJ 2021 ruling**: condomínios can ban STR — biggest practical Airbnb constraint
- **Petrópolis 2022 + RS 2024 + Juiz de Fora 2026**: recent flood disaster reference
- **47% of national population unassisted by sewage** — massive infrastructure gap
- **Asbestos banned 2017** nationally — earlier buildings likely contain it
- **Currency volatility** — BRL can swing 15-25% vs USD/EUR
- **Terreno de marinha / laudêmio / foro (CRITICAL for coastal buyers)** (2026-05-27 verified, source: Planalto Decreto-Lei 9.760/1946 + Lei 9.636/1998): **terreno de marinha** = coastal land within 33 m of the 1831 high-water line, titled to the **União** (federal government), administered by **SPU (Secretaria do Patrimônio da União)**. Holders have **enfiteuse (aforamento)** or **ocupação** — never full domínio pleno. Affected sweeps: Copacabana, Ipanema, Leblon, Botafogo, Flamengo, central Salvador, central Recife, Santos waterfront, much of Florianópolis. **Laudêmio = 5% on transfer value** payable to SPU on every sale of an aforado property (DL 9.760/1946 Art. 686 + Lei 9.636/1998); **foro = ~0.6%/yr ground-rent** to SPU. Verify via SPU portal `https://www.gov.br/spu/` or via Certidão Autorizativa de Transferência (CAT). **PEC 3/2022** (Câmara approved two-round vote Feb 2022; pending Senado CCJ since Aug 2023, pedido de vista Dec 2024 — no scheduled return as of 2026-05) seeks to revoke União ownership and transfer to current occupants — **laudêmio + foro REMAIN IN FORCE 2026-05**; do NOT pre-emptively assume PEC will pass.
- **Indivisão / condomínio pro indiviso**: heirs who never completed partilha leave property in fractional undivided shares; requires extrajudicial inventário (Lei 11.441/2007 + CPC 13.105/2015) before any sale.

## Reddit / forum sources

- **r/brasil** — biggest community
- **r/saopaulo**, **r/rio**, **r/Florianopolis**
- **r/PersonalFinanceBR**
- **InfoMoney**, **Valor Econômico Real Estate**
- **Exame Imóveis**, **G1 Economia**

## Verification authorities

| Authority | When to call |
|---|---|
| **Cartório de Registro de Imóveis** | Title verification, registration |
| **Tabelionato de Notas** | Escritura pública |
| **Município (Prefeitura)** | IPTU + Habite-se + valor venal |
| **Receita Federal (RFB)** | Federal taxes + CIB |
| **INCRA** | Rural land |
| **Estado (Secretaria da Fazenda)** | ICMS + state taxes |
| **Síndico do Condomínio** | If apartment |
| **CEMADEN** | Flood/landslide risk |

## Source URL templates

| Source | URL pattern |
|---|---|
| FIPE-ZAP HPI | `https://www.fipe.org.br/en-us/indexes-and-indicators/fipezap` |
| ZAP Imóveis | `https://www.zapimoveis.com.br/` |
| VivaReal | `https://www.vivareal.com.br/` |
| Quinto Andar | `https://www.quintoandar.com.br/` |
| BCB Real Estate | `https://www.bcb.gov.br/` |
| IBGE | `https://www.ibge.gov.br/` |
| CEMADEN | `https://www.cemaden.gov.br/` |
| CPRM | `https://www.cprm.gov.br/` |
| INMET | `https://portal.inmet.gov.br/` |
| ANA | `https://www.ana.gov.br/` |
| INCRA | `https://www.gov.br/incra/pt-br` |
| Receita Federal — CIB FAQ | `https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/perguntas-frequentes/cadastros/cib` |
| Receita Federal (CIB/SINTER) | `https://www.gov.br/receitafederal/` |
| ONR (cartório integration) | `https://www.onr.org.br/` |

## Status

✅ **Fully populated** as of 2026-04-26.
**Coverage check**: pricing (FIPE-ZAP Q1 2026), traffic (DNIT VMD), tax (IPTU + ITBI per município + IR + Reforma Tributária 2026-2033), rental (Lei do Inquilinato + STJ 2021 condo STR ban), work (MTE + MEI + Simples), risks (CEMADEN + Petrópolis 2022 + RS 2024 + Juiz de Fora 2026), mains (Marco Legal Saneamento 2033 target).
**Confidence**: HIGH for FIPE-ZAP Q1 2026 figures + Reforma Tributária timeline (Emenda 132/2023 confirmed) + MCMV extension April 2026 (R$200B + R$13k income + R$600k cap + 35yr); HIGH for STJ 2021 condo STR ban; HIGH for CIB phasing (Jan 2026 federal administration + notarial/registry + state capitals & DF; Jan 2027 state administration + remaining municipalities — LC 214/2025 art. 266; instituted by IN RFB 2.030/2021, notarial/registry adoption IN RFB 2.275/2025); MEDIUM for IBS/CBS final real-estate sector rates (pilot 2026, finalization pending).

**Last verified**: 2026-08-07 (CIB cadastre re-verified — LC 214/2025 art. 265/266 two-phase rollout, Jan 2026 federal administration + notarial/registry + capitals & DF → Jan 2027 state administration + remaining municipalities; CIB does not replace the cartórios; instituting instrument corrected to IN RFB 2.030/2021. Remainder of the playbook unchanged from the 2026-04-26 population date.)

## Extension TODOs

- [ ] CIB rollout tracker (Jan 2027 phase — state administration + all remaining municipalities, LC 214/2025 art. 266 II)
- [ ] Per-município IPTU rates table
- [ ] Per-município ITBI rates table
- [ ] Reforma Tributária real-estate sector rates 2027-2033
- [ ] MCMV eligibility decision tree (R$13k income, R$600k cap)
- [ ] Foreign rural land cap calculation per município (25% + 10% rules)
- [ ] Petrópolis + Rio Grande do Sul flood-zone overlay
- [ ] Favela property regularization (usucapião + REURB)
- [ ] STJ condomínio STR ban tracker
- [ ] Sewage connection per município (Marco Legal target 2033)
