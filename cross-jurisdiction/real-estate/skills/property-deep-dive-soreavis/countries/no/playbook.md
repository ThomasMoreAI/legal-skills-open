# Norway 🇳🇴 — Property Due-Diligence Playbook

ISO2: `no`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`0150` Oslo central, `5003` Bergen, `7012` Trondheim, `4012` Stavanger)
- **Admin levels**: **15 fylker** (counties — NO reverted from 11 to 15 on 1 Jan 2024, dissolving Viken / Vestfold og Telemark / Troms og Finnmark back to Akershus, Buskerud, Østfold, Vestfold, Telemark, Troms, Finnmark) + 357 kommuner (municipalities) (2026-05-27 verified, source: Kartverket / regjeringen.no — 2022 Storting vote undid the 2020 consolidation)
- **Currency**: **NOK** (Norwegian krone); 1 EUR ≈ 11–12 NOK (volatile, often 11.5)
- **Languages**: Norwegian (Bokmål 85% + Nynorsk 15%, both official); Sámi minority (north)
- **Cadastre**: **Kartverket** (Norwegian Mapping Authority) + **Matrikkelen** (national property register)
- **Identifier**: gnr/bnr (gårdsnummer/bruksnummer) + festenr (lease number) per kommune; format `<kommune>/<gnr>/<bnr>/<fnr>`
- Distinct ownership types:
  - **Selveier** (freehold, ~75% of housing stock)
  - **Borettslag** (housing cooperative — major form, ~17% of stock)
  - **Aksjeleilighet** (old-style share apartment, rare)
  - **Eierseksjon** (condominium / commonhold — most modern apartments)
- **Norway is NOT in EU** — but EEA member; some buyer restrictions apply

## Section: `--price`

### Primary sources

- **Kartverket Matrikkelen** (cadastre): `https://eiendomsregisteret.kartverket.no/`
- **Se Eiendom** (Kartverket consumer portal): `https://seeiendom.kartverket.no/`
  - FREE address lookup with parcel + ownership info
- **Eiendom Norge** (industry body) — monthly market reports: `https://eiendomnorge.no/`
- **SSB (Statistics Norway) Boligprisindeks**: `https://www.ssb.no/`
- **Norges Bank** financial stability reports
- **Realkredittforeningen** mortgage data

### Listing platforms

- **Finn.no** — DOMINANT (~95% market share): `https://www.finn.no/realestate`
  - URL: `https://www.finn.no/realestate/homes/search.html?location=<id>`
  - Includes both selveier + borettslag in one feed
- **DNB Eiendom**, **EiendomsMegler 1**, **Privatmegleren**, **Krogsveen**, **Aktiv** — agency networks
- **Hjem.no** (alternative)

### 2025 price benchmarks (Eiendom Norge + SSB)

| Region | NOK/m² (avg leiligheter) | Avg total villa |
|---|---:|---:|
| **Oslo** | 90,000–130,000 (centro 100,000–160,000) | 9,000,000–18,000,000+ |
| **Bærum + Asker** (Oslo suburb) | 80,000–115,000 | 9,000,000–15,000,000 |
| **Bergen** | 60,000–80,000 | 6,500,000–10,500,000 |
| **Trondheim** | 55,000–75,000 | 6,000,000–9,500,000 |
| **Stavanger / Sandnes** | 50,000–70,000 | 6,000,000–9,000,000 |
| **Tromsø** | 55,000–75,000 | 6,500,000–9,500,000 |
| **Drammen, Sandefjord** | 45,000–60,000 | 5,500,000–8,000,000 |
| **Smaller cities** | 30,000–50,000 | 4,000,000–6,500,000 |
| **Rural / hytte** | varies massively | from NOK 1,500,000 (mountain cabin) to NOK 20,000,000+ (coastal/luxury) |

### Compute

1. Listing NOK/m² = price / **BRA (bruksareal)** standard surface measure
2. **Trap**: BRA = usable area; **P-rom (primærrom)** = primary rooms only (excl. storage); **S-rom (sekundærrom)** = secondary
3. **Borettslag math**: listing price = **innskudd** (down payment) + share of **fellesgjeld** (cooperative shared debt). The TRUE total cost = innskudd + fellesgjeld + felleskostnader future stream
4. **Eierseksjon math**: own apartment + share in common parts (sameie); separate sameieavgift

### Borettslag specific (CRITICAL)

For borettslag, always compute:
- **Innskudd** (your share value, like down payment) — what listing typically shows
- **Fellesgjeld** (cooperative shared building debt) — often **NOK 500,000–3,000,000 per apartment** for newer borettslag
- **Felleskostnader** (monthly common costs) — typically NOK 3,000–10,000+/mo
- **Total acquisition** = Innskudd + Fellesgjeld
- **Forretningsfører** + årsmøte protokoller for due-diligence

---

## Section: `--traffic`

### Primary sources

- **Statens vegvesen** (Public Roads Administration): `https://www.vegvesen.no/`
- **NVDB (Nasjonal vegdatabank)**: `https://nvdb.atlas.vegvesen.no/`
  - Open data, all road counts
- **Trafikkdata.no**: `https://trafikkdata.atlas.vegvesen.no/` — interactive

### Key term

**ÅDT (årsdøgntrafikk)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (boligvei, lokalvei)
- 🟡 1,000–8,000 v/d (fylkesvei, urban arterial)
- 🟠 8,000–30,000 v/d (riksvei, urban core)
- 🔴 > 30,000 v/d (E6/E18/E39, central Oslo Ring)

---

## Section: `--tax`

### Annual property tax — Eiendomsskatt (OPTIONAL per kommune)

**325 of 357 kommuner** charge eiendomsskatt (only 32 do NOT — trend over last decade is more kommuner opting in, not out) (2026-05-27 verified, source: SSB 2025). Not nationwide.

- **Rates**: max **4 promille (0.4 %)** for bolig/fritidsbolig since 2020 (commercial higher, historic 7‰ general cap); first year max 1‰, max +1‰ per year (2026-05-27 verified, source: SSB / eskl. §§ 11-13)
- **Bunnfradrag** (basic deduction): kommune sets — typically NOK 200,000–1,500,000
- **Verdsettelsesrabatt** (valuation discount): typically 30 % off market value
- **Effectively low**: typical NOK 5,000–25,000/yr for residential
- **Bills**: 4× per year (quarterly)

**Major kommuner with eiendomsskatt**:
- Oslo: yes (introduced 2017)
- Bergen, Stavanger, Trondheim: yes
- Many smaller kommuner: yes
- Bærum, Asker (Oslo wealthy suburbs): NO (no eiendomsskatt)

### Transaction taxes — Dokumentavgift (MAJOR)

**2.5 % of purchase price** (2025, source: Skatteetaten / dokumentavgiftsloven) — significant! Buyer pays.

**CRITICAL EXEMPTION**: **Borettslag NOT subject to dokumentavgift** (only selveier + eierseksjon).
- This makes borettslag often €25,000–€100,000 cheaper to buy at same price point
- **Borettslag transfer**: only **NOK 585** (2025) flat fee (Tinglysningsgebyr)

**Tinglysningsgebyr** (registration fee): **NOK 585** (2025) per document for kjøp + skjøte; mortgage doc separately

### Other transaction costs

- **Megler** (broker): typically **1.5–3 %** paid by seller (or split in negotiation)
- **Legal/conveyancing**: most use megler + standard contracts; full lawyer rare
- **Boligkjøperforsikring** (buyer insurance): voluntary; ~NOK 5,000–15,000 — **highly recommended**

### Total transaction cost (buyer side)

- **Selveier / eierseksjon**: ~3–4 % of price (mostly dokumentavgift 2.5 %)
- **Borettslag**: ~0.5–1 % of price (no dokumentavgift)

### Capital gains

- **22 % flat** (resident individuals) (2025, source: Skatteetaten)
- **Primary residence exemption**: **12 months ownership + occupation in last 24 months** → fully exempt (source: Skatteetaten, skatteloven; 2025)
- Investment property: full 22 % on gain

### VAT (mva)

- 25 % standard
- 15 % reduced (food)
- 12 % reduced (transport, hotels, cinema, museums) (2025 rates, source: Skatteetaten — merverdiavgiftsloven; rates may have changed)
- Residential property sales: **VAT-exempt** (excl. specific commercial)

### Future risk

- Eiendomsskatt residential cap stable at **4‰ (0.4 %)** since 2020
- **Formueskatt (wealth tax) — 2025**: tax-free **NOK 1.76M single / NOK 3.52M couples**; standard band (≤NOK 20.7M) total 1.0 % (kommune 0.525 + state 0.475); high band (>NOK 20.7M) total 1.1 % (kommune 0.525 + state 0.575) (2026-05-27 verified, source: Skatteetaten / regjeringen.no Prop 1 LS 2024–2025). Boligverdsetting: primærbolig first NOK 10M @ 25% of MV / above @ 70%; sekundærbolig 100%; fritidsbolig separate lower regime. New ML-based national valuation model from 2026 income year.
- **Utflyttingsskatt (2024 exit-tax reform)**: from 20 Mar 2024 (dividend rules from 7 Oct 2024); 12-year cap on payment regardless of realisation; **NOK 3M basic allowance** (replaces prior NOK 500k); pay-immediate / 12-yr instalments / 12-yr deferral options (2026-05-27 verified, source: Skatteetaten / Prop 1 LS 2024–2025 § 10-70 skatteloven)
- **Borettslag exemption from dokumentavgift** — periodically debated but stable

---

## Section: `--rental`

### Long-term residential

- **Husleieloven** (Tenancy Act): tenant-protective
- Standard contract: **3-year minimum** (loose); **tidsbestemt** (fixed-term) common
- **Husleieloven** rent caps: limited (per CPI adjustments)
- **Boligbyggelagene** (BBL) cooperatives manage many borettslag

### Short-let (Airbnb / Booking)

**Skatteetaten rules** (significant):
- **Sekundærbolig** (secondary housing): **31-day rental cap** for short-let in some kommuner without commercial license
- **Oslo**: ongoing debate about 30/60/90-day caps
- **Borettslag approval** required typically (most ban or restrict short-let)
- **Eierseksjon** rules per sameie (homeowners' assoc)

### Tax on short-let

- **Skatteetaten**: rental income taxable as **kapitalinntekt** 22 % (2025, source: Skatteetaten)
- **Above NOK 10,000/yr** for primary residence rental: tax applies on amount above
- **Sekundærbolig**: full taxation
- **Hyttekultur** (cabin culture): ulikt regelverk per kommune
- **EU Regulation 2024/1028**: NO transposition pending (NOR is EEA, not EU but participates in single-market regs)

---

## Section: `--work=<profession>`

### Job platforms

- **Finn Jobb** — biggest: `https://www.finn.no/job`
- **NAV (Arbeids- og velferdsetaten)**: `https://www.nav.no/`
- **LinkedIn NO**, **Indeed.no**, **Karriereguiden**, **Jobb.no**
- **Statens lønnsstatistikk** for civil service salaries

### Self-employment

- **Enkeltpersonforetak (ENK)**: sole trader; no min capital
- **Aksjeselskap (AS)**: limited company, **min NOK 30,000** capital (source: Brønnøysundregistrene / aksjeloven; 2025)
- **NUF (Norwegian-registered foreign company)**: niche
- **Brønnøysundregistrene** (registration agency)
- **Folketrygd** + **Næringsdrivende** social contributions

### Salary benchmarks (2025)

- Median monthly gross:
  - Oslo: ~NOK 60,000-75,000
  - Bergen, Trondheim, Stavanger: ~NOK 55,000-65,000
  - Smaller cities: ~NOK 48,000-55,000
- **No statutory minimum wage** (set per industry by union agreement); allmenngjøring in some sectors

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **NVE (Norges vassdrags- og energidirektorat)** | `https://www.nve.no/` | Floods, landslides, dams |
| **Skrednett** (NVE landslide registry) | `https://skrednett.no/` | Detailed landslide + avalanche maps |
| **NVE Atlas** | `https://atlas.nve.no/` | Aggregated risk maps |
| **NGI (Norwegian Geotechnical Institute)** | `https://www.ngi.no/` | Quick clay + slope research |
| **Aktsomhetskart for flom** | per fylke variations | Flood awareness maps |
| **NGU (Norges geologiske undersøkelse)** | `https://www.ngu.no/` | Geology, radon, geohazards |
| **DSA (Direktoratet for strålevern og atomsikkerhet)** | `https://www.dsa.no/` | Radon — Norway has aggressive testing program |
| **MET (Meteorologisk institutt)** | `https://www.met.no/` | Climate, weather |
| **NORSAR** (seismic monitoring) | `https://www.norsar.no/` | Earthquakes |

### Specific risks

- **Skred (landslides + avalanches) — MAJOR risk**:
  - **Snøskred** (snow avalanche)
  - **Jordskred** (mud / earth slide)
  - **Steinskred** (rockfall)
  - **Kvikkleireskred** (quick clay slide) — devastating, can be triggered by rain or construction
  - Especially: **fjordmark + western Norway + Trøndelag + arctic regions**
  - **Gjerdrum 2020 disaster** (10 dead): kvikkleire reminder
- **Flom (flooding)**:
  - River plains: Glomma, Drammenselva, Otra
  - Fjord communities
  - Frequent post-snowmelt + autumn rain
- **Kystflom + havnivåstigning** (coastal flood + sea-level rise)
- **Radon — Norway recommends testing for ALL houses**:
  - One of highest indoor levels in Europe
  - Especially East Norway granite + parts of Vestlandet
- **Earthquake**: low-moderate (Norwegian Sea, west coast)
  - Bergen + Oslo region: M 5+ historical
  - North Sea: minor
- **Climate change**: rising precipitation (see sourced MET + NVE projections below); permafrost retreat in north; sea-level rise

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint, asbestos, no thermal envelope |
| **1960s–1980s panelhus + concrete** | Asbestos very common |
| **1990s–2000s** | Better insulation, modern wiring |
| **Post-2010 TEK10** | Low-energy standards |
| **Post-2017 TEK17** | Strict energy + accessibility |
| **Wood construction** | Common — fire risk + moisture; brannsmitte |
| **Asbestos** | Pre-1980s buildings likely; banned 1985 |

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energimerking** (energy label) | All sales since 2010 | 10 years |
| **Tilstandsrapport** (condition report) | **MANDATORY since 1 January 2022** for resale of bolig | Per case |
| **Egenerklæring** (seller's declaration) | All sales | At sale |
| **Egenmelding skadedyr** (pest declaration) | All sales | At sale |
| **Eierskifteforsikring** (seller's insurance) | Recommended — protects seller from buyer claims | Per case |
| **Boligsalgsrapport** (older format) | Replaced by tilstandsrapport for 2022+ | n/a for new |

### Tilstandsrapport (CRITICAL post-2022)

The **mandatory tilstandsrapport** dramatically reduced post-sale dispute risk:
- Conducted by **takstmann/bygningskyndig**
- Costs NOK 15,000-35,000 (seller pays)
- Visual + technical inspection
- Specifies **TG (tilstandsgrad) 0-3** for each building component
  - **TG2 / TG3** = significant defect; reduce price negotiation power
- **2022 reform** + new **avhendingsloven** strengthens buyer position post-sale

### Climate change projections (MET + NVE)

- +1.5–4.5 °C by 2050 (RCP scenarios)
- Precipitation +20-40 % (winter + autumn especially)
- Sea-level rise: +20-80 cm by 2100
- Permafrost retreat: arctic + alpine
- More flom + skred events
- Glacial retreat: significant (Folgefonna, Jostedalsbreen)

---

## Section: `--mains`

### Sources

- **Norsk Vann**: `https://www.norskvann.no/` — national water utility association
- Each kommune manages own vannverk + avløpssystem
- Major: **Oslo VAV**, **Bergen Bymiljøetaten Vann og avløp**, **Trondheim kommune**, **Stavanger Vann & avløp**

### Verification

- Most populated areas: kommunal mains universal
- **Hytter (cabins) + rural**: own **brønn** (well) + **slamavskiller** (septic)
- **Modne avløpsanlegg** (mature septic systems) being phased out — **kommunal upgrades ongoing**

### Costs

| Scenario | Cost (NOK) |
|---|---:|
| Tilkobling to mains | 50,000–150,000 |
| Mains-line extension via kommune | 100,000–500,000+ |
| Slamavskiller upgrade | 100,000–250,000 |
| Pre-renseanlegg / minirenseanlegg | 150,000–400,000 |
| Borebrønn (drilled well) | 80,000–150,000 |

---

## Cost benchmarks (NO 2026)

| Work | Cost (NOK) |
|---|---:|
| Energimerking | 5,000–12,000 |
| Tilstandsrapport | 15,000–35,000 |
| Megler (seller-paid typically) | 1.5–3 % of price |
| **Dokumentavgift (selveier only)** | **2.5 % of price** |
| Tinglysningsgebyr | 585 per doc |
| Boligkjøperforsikring (recommended) | 5,000–15,000 |
| **Total transaction cost (selveier)** | **~3–4 %** of price |
| **Total transaction cost (borettslag)** | **~0.5–1 %** of price |
| Slamavskiller upgrade | 100,000–250,000 |
| Roof (concrete tile, 150 m²) | 250,000–500,000 |
| Asbestos abatement (small house) | 100,000–400,000 |
| Energy retrofit (Class C → A) | 600,000–1,500,000 |
| Radon mitigation | 30,000–80,000 |
| Brann + lyd retrofit (apartment) | 50,000–200,000 |

## Active fiscal incentives (2025-2026)

- **Enova** energy retrofit grants: heat pumps, insulation, PV solar
- **Husbanken** loans for energy-efficient first-purchase
- **Boligsparing for ungdom (BSU)**: tax-deductible savings for first-time buyers (NOK 27,500/yr cap)
- **Renteinnbetaling fradrag**: mortgage interest tax-deductible (~22 %) — significant subsidy
- **Skattelov § 6-1 oppfyllelse** for retrofit

## Common listing platforms

- **Finn.no** — DOMINANT (~95 %), full extraction
- **DNB Eiendom, Krogsveen, Aktiv, EiendomsMegler 1, Privatmegleren** — agency networks
- **Hjem.no** — alternative
- **Næringseiendom.no** — commercial

## Caveats unique to NO

- **Dokumentavgift 2.5 %** is the major buyer-side cost — **borettslag avoids it** (huge structural advantage); affects whether to choose freehold or coop
- **Borettslag vs selveier vs eierseksjon** distinction CRUCIAL; borettslag has fellesgjeld (shared debt of building) often €50k–€300k+ tied to apartment
- **Tilstandsrapport mandatory since 2022** — one of the strongest buyer-protection regimes in Europe (avhendingsloven reform)
- **Kvikkleire (quick clay)** zones — Trøndelag, Oslo region — Gjerdrum 2020 disaster; NVE Skrednett verification ESSENTIAL for any new build or extension
- **Boligkjøperforsikring** strongly recommended — covers buyer post-sale claims
- **Konsesjon** — concession requirement for some agricultural / bolig in certain kommuner; **can block foreigners**
- **Bo- og driveplikt** in some rural areas (residence + cultivation duty for agricultural)
- **Allemannsretten** (right of public access) over uncultivated land — affects neighbouring privacy
- **Norway is NOT in EU but EEA** — buying allowed for EU/EEA citizens; non-EEA may face restrictions
- **Hyttekultur** — fjellhytte (mountain cabin) and sjøhytte (sea cabin) major secondary-home market
- **Strict building permits** in fjords + coast (50–100m setback)
- **Folketrygd** + **Skatteetaten** make tax for residents straightforward
- **Currency volatility**: NOK can swing 15-25 % vs EUR; affects foreign-buyer purchasing power
- **Petroleum wealth fund**: keeps NOK supported; long-term outlook depends on oil price
- **Allmenningsrett** (commons rights) for some forest properties

## Reddit / forum sources

- **r/Norge**, **r/Oslo**, **r/Bergen**, **r/Trondheim**
- **r/AskNorway**, **r/PersonalFinanceNorge**
- **r/Norwegen** (German-speaking expat angle)
- Expat: **The Local Norway**, **Life in Norway**

## Verification authorities

| Authority | When to call |
|---|---|
| **Kartverket** | Title verification, Matrikkelen lookup |
| **Kommune byggesak / planavdelingen** | Permits, reguleringsplan, byggesak history |
| **Skatteetaten** | Eiendomsskatt, capital gains |
| **Megler** | Final transfer, escrow |
| **Vannverk kommune** | Mains drains verification |
| **NVE / NGI** | Skred / kvikkleire / flom check |
| **DSA** | Radon |
| **Borettslag forretningsfører** | If borettslag: financials, fellesgjeld details |
| **Sameieforvaltning** | If eierseksjon: sameieavgift, planned projects |

## Quirks to know

- **Gnr/Bnr/Fnr** — Norwegian way to identify property
- **Matrikkelnummer** = combined identifier
- **Hjemmel** = legal title; **rettigheter** = rights/easements
- **Heftelser** (encumbrances) on title — read all sections
- **Borett** (right to occupancy) in borettslag — different from ownership
- **Sameievedtekter** + **borettslagsvedtekter** must be read pre-purchase
- **TG2/TG3** flags in tilstandsrapport reduce buyer power
- **Festetomt** (leasehold ground) — separate festeavgift; check remaining lease
- **Konsesjon-pliktig** parcels: agricultural + some coastal need approval
- **Kvikkleirefare-soner** (NVE Skrednett) — never build without geotechnical study
- **Strandsoneforbud**: 100m coastal setback for new construction (with exceptions)
- **Oppdragsmegler avtale** (broker engagement): typically 3-month exclusive

## Source URL templates

| Source | URL pattern |
|---|---|
| Kartverket Se Eiendom | `https://seeiendom.kartverket.no/` |
| Finn.no | `https://www.finn.no/realestate/homes/search.html?location=<id>` |
| Eiendom Norge market | `https://eiendomnorge.no/` |
| SSB Boligprisindeks | `https://www.ssb.no/priser-og-prisindekser/boligpriser-og-boligprisindekser/statistikk/prisindeks-for-brukte-boliger` |
| NVE Atlas | `https://atlas.nve.no/` |
| Skrednett | `https://skrednett.no/` |
| NGU geo | `https://www.ngu.no/` |
| DSA Radon | `https://www.dsa.no/` |
| Skatteetaten Eiendomsskatt | `https://www.skatteetaten.no/person/skatt/hjelp-til-riktig-skatt/bolig-og-eiendeler/bolig-eiendom-tomt/` |
| MET Klima | `https://www.met.no/` |
| NORSAR | `https://www.norsar.no/` |
| Husbanken | `https://www.husbanken.no/` |
| Enova | `https://www.enova.no/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (Kartverket + NVE + Skrednett + Finn.no all gold-standard); HIGH for tilstandsrapport mandate (2022-onwards). MEDIUM for short-let regulation (NO is EEA — EU 2024/1028 may apply via EEA agreement; transposition pending).

## Extension TODOs

- [ ] Per-kommune eiendomsskatt + bunnfradrag specifics
- [ ] Borettslag fellesgjeld red-flag detection (debt %, repair backlog)
- [ ] Kvikkleire zone parcel-level lookup via NVE
- [ ] Konsesjon requirements per kommune
- [ ] Finn.no extraction patterns + sold prices
- [ ] Radon zones (NGU + DSA) overlay
- [ ] Hytte vs bolig tax distinctions
- [ ] EEA buyer rules (Norway non-EU but EEA)
- [ ] Festetomt remaining lease length lookup
- [ ] Tilstandsrapport TG-grade severity heuristics
