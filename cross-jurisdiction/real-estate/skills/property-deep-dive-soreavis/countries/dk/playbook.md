# Denmark 🇩🇰 — Property Due-Diligence Playbook

ISO2: `dk`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1050` København K, `2000` Frederiksberg, `8000` Aarhus C, `5000` Odense, `9000` Aalborg)
- **Admin levels**: 5 regioner + 98 kommuner (post-2007 reform)
- **Currency**: **DKK** (Danish krone) — pegged to EUR via ERM II at **7.46038 ± 2.25%**; effectively stable
- **Languages**: Danish (official); German minority (Sønderjylland)
- **Cadastre**: **Geodatastyrelsen / Styrelsen for Dataforsyning og Effektivisering** (matriculation) + **Tinglysning.dk** (national land register, fully digital since 2009)
- **Identifier**: matrikelnummer + ejerlavskode (`12a, Roskilde Markjorder`)
- **Ownership types**:
  - **Ejerbolig** (freehold, ~63% of stock)
  - **Andelsbolig** (cooperative — major form, ~7-8% national, up to 35% in København) — you own a share, not the unit
  - **Almene boliger** (social housing, ~20%)
  - **Lejeboliger** (rental, ~10%)

## Section: `--price`

### Primary sources

- **Vurderingsstyrelsen** (Property Assessment Agency): `https://vurdst.dk/` — official assessments
  - **Vurderingsportalen**: `https://www.vurderingsportalen.dk/` — consumer access
- **OIS (Offentlig Information om Salg)**: `https://www.ois.dk/` — sales register, FREE; every sale recorded
- **BBR (Bygnings- og Boligregistret)**: `https://bbr.dk/forside` — all buildings + dwellings register
- **Tinglysning.dk**: `https://www.tinglysning.dk/` — land register; FREE viewer, paid certified extracts
- **Boliga**: `https://www.boliga.dk/` — sold prices map + listings (combines OIS + listings)
- **Boligsiden**: `https://www.boligsiden.dk/` — major listings
- **Danmarks Statistik (DST)** — Boligprisindeks: `https://www.dst.dk/`
- **Danmarks Nationalbank** — financial stability
- **Realkreditrådet** mortgage data

### Listing platforms

- **Boligsiden** — biggest aggregator: `https://www.boligsiden.dk/`
- **Boliga** — sold-price map specialty: `https://www.boliga.dk/`
- **Home.dk**, **EDC.dk**, **RealMaegler**, **Nybolig**, **DanBolig**, **Estate Mæglerne** — agency networks
- **Lokalbolig.dk** — alternative

### 2025 price benchmarks (DST + Boliga)

| Region | Avg DKK/m² (apt) | Avg total (parcelhus, single-family) |
|---|---:|---:|
| **København K (centro)** | 50,000–75,000+ | 8,000,000–18,000,000+ |
| **Greater København** | 35,000–55,000 | 5,500,000–9,500,000 |
| **Frederiksberg** | 50,000–75,000 | 7,000,000–14,000,000 |
| **Aarhus** | 30,000–48,000 | 4,000,000–7,500,000 |
| **Odense** | 22,000–35,000 | 3,200,000–5,500,000 |
| **Aalborg** | 18,000–30,000 | 2,800,000–4,800,000 |
| **Smaller cities** | 14,000–22,000 | 2,200,000–4,000,000 |
| **Rural Jylland / Fyn** | 8,000–18,000 | 1,500,000–3,500,000 |
| **Sommerhuse coastal** | varies | 1,500,000–8,000,000+ |

### Compute

1. DKK/m² = price / **boligareal** (BBR-registered area)
2. **OIS sale prices** = official, post-completion
3. **Andelsbolig math**: andel pris (share value) ≠ market value; capped by association rules
4. **Energimærke** A-G: A is best; F-G near unmortgageable
5. Cross-check sold prices via Boliga + Vurderingsportalen

### Andelsbolig specific (CRITICAL)

For andelsbolig, you must check:
- **Andelskrone** (share value per square meter) — the price ceiling per association
- **Generalforsamlingsreferat** (general assembly minutes) — financial health
- **Årsregnskab** + **vedligeholdelsesplan** — backlog repairs
- **Foreningens gæld** (cooperative debt) — high debt = repair backlog risk
- **Andelsforeningens vedtægter** — what you can/can't do
- **Belåningsgrad** (ratio of debt to value) — high = restructuring risk

### Key terms

- Ejerbolig = freehold
- Andelsbolig = cooperative
- Sommerhuse = summer cottage (different zone + tax)
- BBR-meddelelse = building register notice
- Boligskat = combined property tax
- Tinglysning = registration

---

## Section: `--traffic`

### Sources

- **Vejdirektoratet**: `https://www.vejdirektoratet.dk/` — road agency
- **Vejman.dk** — traffic counts platform
- **Mastra (Mastrabasen)** — traffic count database, open

### Key term

**ÅDT (Årsdøgntrafik)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (boligvej, residential street)
- 🟡 1,500–10,000 v/d (kommunal vej, urban arterial)
- 🟠 10,000–30,000 v/d (statsvej, motortrafikvej)
- 🔴 > 30,000 v/d (motorvej, urban core E-vej)

---

## Section: `--tax`

### Annual property tax — Boligskat (MAJOR REFORM 2024)

**1 January 2024 reform** combined two old taxes into single **boligskat**:

#### Components

1. **Grundskyld** (land tax):
   - Base: 80% of grundværdi (precautionary 20% deduction)
   - Rate: **0.51%** below skattegrænse / **1.4%** above (2026)
   - Progressionsgrænse: **DKK 9,200,000 (2024 base, indexed annually under Personskattelovens §20)** (2026-05-27 verified, source: vurderingsportalen.dk; 2024 boligskat reform halved pre-reform 0.92%/3.0% rates and added a 20% precautionary deduction)
   - **Kommunale promille**: 16-26‰ varying per kommune for grundskyld
2. **Ejendomsværdiskat** (property value tax):
   - Base: 80% of ejendomsværdi (full property value, also 20% reduction)
   - Rate: **0.51%** below threshold / **1.4%** above
   - Applies to ejerbolig + sommerhus only

#### Collection (NEW since 2024)

- Both collected via **statskat** (state tax) — pulled from your **forskudsopgørelse** (preliminary tax return)
- No longer kommune-direct
- 2025 + 2026 use **preliminary 2024 valuation**; final adjustment retroactive

#### Stigningsbegrænsning (transitional cap)

- 2024-2026: cap on year-on-year increase to soften reform impact
- Phase-out by ~2030

### Transaction taxes

- **Tinglysningsafgift** (registration fee): **0.6% + DKK 1,850 flat** for property purchase (2025); **1.45% + flat** for mortgage
- **No general transfer tax** beyond tinglysning — **lowest in W. Europe**
- **Mæglersalær** (broker): typically **1.5–3%** paid by seller (negotiable)
- **Notar fees**: not mandatory in DK (advokat optional)

### Total transaction cost (buyer side)

- Resale primary residence: **~1–2.5%** of price (very low compared to W. Europe)
- Mortgage adds 1.45% tinglysning of mortgage amount

### Capital gains

- **Ejerbolig (Ejendomsavancebeskatningsloven §8 'parcelhusreglen', LBK nr 132 af 25/01/2019)**: capital gain on primary residence often **EXEMPT** if owner-occupied + plot ≤1,400 m² (or subdivision impossible per kommune); sommerhus → §8 stk. 2 (2026-05-27 verified, source [retsinformation.dk](https://www.retsinformation.dk/eli/lta/2019/132))
- **Sommerhus (sommerhusreglen)**: similar exemption if for personal use during ownership
- **Investment property**: progressive income tax up to **52.07%** (or 22% selskab if held in company)

### VAT (moms)

- 25% standard
- Real estate transactions exempt (excl. specific commercial)
- New build sale by trader: 25% moms (developer-paid)

### Future risk

- **Boligskat continues to phase in** (transitional cap)
- **Stigningsbegrænsning** ends gradually toward 2030
- **Andelsbolig taxation** debated periodically

---

## Section: `--rental`

### Long-term residential

- **Lejeloven** (Tenancy Act): tenant-protective; particularly strict in older buildings (pre-1992)
- **Boligreguleringsloven**: rent control in cities >40k inhabitants — **repealed 1 July 2022** (2026-05-27 verified, source: elov.dk / gorrissenfederspiel.com; consolidated into new Lejeloven + Lov om boligforhold) — existing tenants in regulated kommuner protected via transitional rules
- **Andelsbolig rules**: members of housing association; specific share-purchase rules
- **Tidsbegrænsede aftaler** common
- **Indekslejekontrakt** (index-linked rent): **caps tightened** since 2022 amid inflation

### Short-let (Airbnb / udlejning)

- **Airbnb-aftalen** (Denmark's Airbnb agreement 2018, updated 2023):
  - **70 nights/year cap** København + Frederiksberg (primary residence)
  - **30 nights/year cap** elsewhere (primary residence) without commercial license
- **Mandatory CVR-registration** for >DKK 70,000 yearly turnover
- **Sommerhuse** (summer cottages): **max 70 nights/year** for non-resident owners; primary residents unlimited
- Income reported via Skat **eIndkomst**

### Tax on rental

- **Skattefri bundgrænse**: DKK 31,200 (2025) on Airbnb if hosted via verified platform (auto-reporting)
- **Above bundgrænse**: standard income tax on net rental
- **Kapitalindkomst** if pure investment property

---

## Section: `--work=<profession>`

### Sources

- **Jobnet.dk** (state job platform): `https://www.jobnet.dk/`
- **Jobindex.dk**, **OfferOgEfterspørgsel.dk**, **LinkedIn DK**, **Workindenmark.dk**
- **Brancheforeninger** for profession bodies

### Self-employment

- **Enkeltmandsvirksomhed** (sole trader): no min capital
- **ApS** (Anpartsselskab): limited company, **min DKK 40,000 capital**
- **A/S** (Aktieselskab): public limited, min DKK 400,000
- **CVR registration** mandatory
- **Moms** (VAT): from DKK 50,000 turnover
- **AM-bidrag** 8% + progressive income tax 37–55.9%

### Salary benchmarks (2025)

- Median monthly gross:
  - København: ~DKK 50,000–65,000
  - Aarhus, Odense, Aalborg: ~DKK 42,000–55,000
  - Rural: ~DKK 35,000–45,000
- **Ingen statsligt mindsteløn** (no statutory minimum); sectoral via union agreements

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **DMI (Danmarks Meteorologiske Institut)** | `https://www.dmi.dk/` | Weather, climate |
| **Naturstyrelsen** | `https://naturstyrelsen.dk/` | Nature management |
| **Kystdirektoratet** | `https://kyst.dk/` | Coastal erosion + storm surge |
| **Klimatilpasning.dk** | `https://klimatilpasning.dk/` | Climate adaptation portal — kommune plans |
| **GEUS (Geological Survey)** | `https://www.geus.dk/` | Geology, radon |
| **Sundhedsstyrelsen radon** | `https://www.sst.dk/` | Radon program |
| **DCE (Aarhus Univ. environment)** | `https://dce.au.dk/` | Pollution |
| **HOFOR + provincial floodmaps** | per kommune | Local flood |

### Specific risks

- **Stormflod** (storm surge) — coastal regions, major + increasing:
  - **Stormflodsråd** payment scheme — public insurance for storm surge events
  - Ole 1825, 1872, 1981, **20 Oct 2023 record event** (Lolland, Falster, Sønderjylland)
  - **Stormrådet** assesses ratings A-D for properties; A means insurable, D means uninsurable
- **Oversvømmelse** (river/precipitation flooding) — primarily flat lowlands, river basins (Vidåen, Skjernåen)
- **Kysterosion** — west coast Vesterhavet retreating up to **8 m/yr** in some areas; Skagen, Lønstrup
- **Earthquake**: very low — Denmark on stable Fennoscandian shield; max ML 3.5 historic
- **Radon**: significant in Bornholm + parts of Sjælland + Jylland; **all properties recommended for testing**; **Sundhedsstyrelsen 100 Bq/m³ reference level**
- **Skogsbrand** (wildfire): increasing in heath + dry summers (Vestjylland, Hedeområde)
- **Saltvandsindtrængning** (saltwater intrusion) — coastal wells, Sjælland
- **Skred (landslides)**: low; some clay-cliff slumps Stevns Klint, Møns Klint

### Insurance

- **Stormrådet** runs national storm surge compensation scheme
- **Stormflodsforsikring** integrated into property insurance
- **Force majeure naturskader** — regulated via Stormrådet
- **Kommunal støtte** for property buyback in unviable coastal locations (e.g., Mårup Kirke buyback)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, weak insulation, asbestos cement starts, lead |
| **1900–1960** | Lead paint, asbestos, weak insulation |
| **1960s–1980s "betonbyggeri"** | Asbestos very common, energy-inefficient, **PCB in fugemasse 1950–1977** (banned) |
| **1980s–2010** | Improving insulation, modern wiring |
| **Post-2010 BR15/BR18** | Strict |
| **Post-2020 BR18** | Near-zero-energy required |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energimærke** | Required since 2013 for all sales | 10 years |
| **Tilstandsrapport** (condition report) | Strongly recommended; usually buyer pays — relieves seller of liability | Per case |
| **Elinstallationsrapport** (electrical) | Recommended; pairs with tilstandsrapport for insurance | Per case |
| **BBR-meddelelse** | Building register notice | At sale |
| **Tinglysningsudskrift** | Land register extract | At sale |
| **Servitutter** (easements) review | Per case | At sale |

### Climate change projections (DMI)

- +1.5–4.0 °C by 2100
- Sea-level rise: +30–80 cm by 2100
- Precipitation +20–30% winter
- Increased storm surges (esp. Baltic Sea entry)
- More extreme rainfall events

---

## Section: `--mains`

### Sources

- **Danva** (national water utility assoc): `https://www.danva.dk/`
- **HOFOR** (København): `https://www.hofor.dk/`
- **Aarhus Vand**, **Aalborg Forsyning**, **VandCenter Syd** (Odense)
- Universal in urban; sommerhuse + rural may be on individual systems

### Verification

- Most populated areas: kommunal mains universal
- **Sommerhusområder**: many on **slamafskillere** (septic) + **nedsivning**
- **Tank tømning** (sludge collection): scheduled per kommune

### Costs

| Scenario | Cost (DKK), est. |
|---|---:|
| Tilkobling to mains | est. 80,000–250,000 |
| Mains-line extension | est. 200,000–800,000 |
| Slamafskiller upgrade | est. 80,000–150,000 |
| Mini-renseanlæg | est. 100,000–250,000 |
| Borebrønd (drilled well) | est. 60,000–120,000 |

_Ranges are order-of-magnitude estimates (not tied to a published tariff); actual cost depends on distance to mains, kommune VVS schedule, and ground conditions — confirm with a kloakmester quote + your kommune's tilslutningsbidrag tariff._

---

## Cost benchmarks (DK 2026)

| Work | Cost (DKK) |
|---|---:|
| Energimærke | 4,000–10,000 |
| Tilstandsrapport | 8,000–18,000 |
| Elinstallationsrapport | 4,000–8,000 |
| Tinglysningsafgift (kjøp) | 0.6% + 1,850 flat |
| Tinglysningsafgift (mortgage) | 1.45% + 1,850 flat |
| Mæglersalær | 1.5–3% of price (seller) |
| **Total transaction cost (buyer)** | **~1.5–3%** of price |
| Septik to mains | est. 80,000–250,000 |
| Roof (slate, 150 m²) | est. 200,000–400,000 |
| Energy retrofit (Class C → A) | est. 500,000–1,200,000 |
| Asbestos abatement | est. 100,000–400,000 |
| Radon mitigation | est. 30,000–80,000 |
| PCB removal (fugemasse, apartment) | est. 200,000–500,000+ |

_Renovation/abatement ranges are order-of-magnitude estimates (not from a published price book); calibrate against a Bolius/Molio price book or contractor quotes for the specific property._

## Active fiscal incentives (2025-2026)

- **Bygningspuljen**: insulation grants (up to ~DKK 50,000, est. — verify current cap at sparenergi.dk)
- **Skrotningsordning**: oil furnace replacement
- **Varmepumpepuljen**: heat pump grants
- **Renteindbetaling fradrag**: mortgage interest tax-deductible (~25.6%) — significant subsidy
- **Boligjobordning** (handyman deduction): up to ~DKK 17,500/yr per person, est. — verify current cap at skat.dk
- **Boliglån** for first-time buyers (kommune-specific in some cases)

## Common listing platforms

- **Boligsiden** — biggest, most listings
- **Boliga** — sold-price specialty
- **Home.dk, EDC.dk, RealMaegler, Nybolig, DanBolig** — agency networks

## Caveats unique to DK

- **Andelsbolig** (cooperative) is a major form, especially København (~35%); you own **shares** in a housing association, not the apartment
  - Andelskrone caps share price; foreningens gæld = main risk
  - **Andelsforeningens financial health** audit critical before buying
  - **Bopælspligt** in some andelsforeninger — must live there
- **Boligskat reform 2024** combined ejendomsværdiskat + grundskyld; 2025-2026 use preliminary 2024 valuations with retroactive adjustment
- **Stigningsbegrænsning** caps tax increase impact through ~2030
- **Parcelhusreglen** (primary-residence capital gain exemption) is generous — plot ≤1,400 m² + owner-occupied
- **Sommerhus rules** distinct: own zone, max 70 nights non-resident rental
- **Airbnb caps**: 70 nights København / 30 elsewhere for primary residence
- **Storm surge stormflodsråd** insurance scheme — properties get A-D rating; D = uninsurable
- **20 Oct 2023 storm surge** = recent reference event for southern coasts
- **Bornholm radon** distinct hotspot
- **PCB in fugemasse 1950–1977** — banned but still in many older buildings
- **NemID/MitID** required for tinglysning + tax + Skat services
- **Tinglysning fully digital since 2009** — fast registration
- **Boligreguleringsloven repealed 1 July 2022** (consolidated into new Lejeloven + Lov om boligforhold); existing tenants protected via transitional rules
- **Foreign-buyer regime — Lov om erhvervelse af fast ejendom (Erhvervelsesloven)** (2026-05-27 verified, source: civilstyrelsen.dk): non-resident buyers without 5+ years prior DK residency need **Civilstyrelsens tilladelse** (permission moved Justitsmin → Civilstyrelsen 9 Jul 2018). **EU/EEA + Nordic** citizens exempt for year-round (helårsbolig). **Sommerhus**: even EU/EEA need Civilstyrelsen permission absent "special connection" (close DK family, professional/cultural/economic ties) — preserved under Edinburgh Agreement 1992 / Amsterdam Treaty Protocol No. 32 sommerhusprotokol
- **Sønderjylland German minority** — bilingual context

## Reddit / forum sources

- **r/Denmark** (active, English-friendly)
- **r/Aarhus**, **r/Copenhagen**
- **r/dkfinance** — mortgage + tax discussion
- **MyHusum.dk** forums
- Expat: **The Local Denmark**, **Wonderful Copenhagen**

## Verification authorities

| Authority | When to call |
|---|---|
| **Vurderingsstyrelsen** | Boligskat assessment, valuation |
| **Tinglysningsretten** | Title verification |
| **Kommune** | Permits, planning, BBR |
| **Skat** | Tax calculations, capital gains |
| **Stormrådet** | Storm surge rating |
| **Sundhedsstyrelsen** | Radon |
| **Andelsforeningens bestyrelse** | If andelsbolig |
| **Mægler / advokat** | Sale process |

## Source URL templates

| Source | URL pattern |
|---|---|
| OIS (sales register) | `https://www.ois.dk/` |
| Boliga | `https://www.boliga.dk/` |
| Boligsiden | `https://www.boligsiden.dk/` |
| Vurderingsstyrelsen | `https://vurdst.dk/` |
| Vurderingsportalen | `https://www.vurderingsportalen.dk/` |
| Tinglysning | `https://www.tinglysning.dk/` |
| BBR | `https://bbr.dk/forside` |
| Vejdirektoratet | `https://www.vejdirektoratet.dk/` |
| Klimatilpasning | `https://klimatilpasning.dk/` |
| Skat (tax) | `https://www.skat.dk/` |
| GEUS | `https://www.geus.dk/` |
| Stormrådet | `https://www.stormraadet.dk/` |
| Kystdirektoratet | `https://kyst.dk/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax (with 2024 boligskat reform), rental, work, risks (incl. storm surge ratings + 20 Oct 2023 reference event), mains all have primary government sources.
**Confidence**: HIGH for boligskat 2024 reform (Vurderingsportalen + Bolius confirm rates 0.51%/1.4% + 20% deduction); HIGH for tinglysning (1 unified register since 2009); HIGH for andelsbolig structure (DK-specific). MEDIUM for Boligreguleringsloven post-1 July 2022 transition specifics (rapidly changing).

## Extension TODOs

- [ ] Per-kommune grundskyld promille (2024-2028 schedule per Vurderingsportalen)
- [ ] Andelsbolig financial health red-flag detection (foreningens gæld %, repair backlog)
- [ ] Sommerhus zone parcel-level lookup
- [ ] Coastal erosion projection per kommune
- [ ] Bornholm radon zone overlay
- [ ] Stormrådet A-D rating overlay
- [ ] Boligreguleringsloven post-1 July 2022 transition rules
- [ ] PCB legacy building inventory
- [ ] Kommune VVS / kloak connection database
- [ ] Pendlerfradrag + boligjobordning eligibility
