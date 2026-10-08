# Sweden 🇸🇪 — Property Due-Diligence Playbook

ISO2: `se`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits with space `NNN NN` (e.g., `111 29` Stockholm centro, `411 18` Göteborg, `211 22` Malmö)
- **Admin levels**: 21 län (counties) + 290 kommuner (municipalities) + ~2,500 församlingar (parishes, mostly historical)
- **Currency**: **SEK** (Swedish krona); 1 EUR ≈ 11–12 SEK (variable, often weakening)
- **Languages**: Swedish (official); Sami / Meänkieli / Finnish / Yiddish / Romani are recognized minorities
- **Cadastre**: **Lantmäteriet** (national land survey + registration agency)
- **Identifier**: fastighetsbeteckning (e.g., `Stockholm Vasastaden 1:1` = `<kommun> <traktnamn> <blocknr:enhetsnr>`)
- Distinct ownership types: **äganderätt** (freehold villa/townhouse), **bostadsrätt** (cooperative apartment — most apartments), **hyresrätt** (rental apartment, regulated), **tomträtt** (leasehold ground from kommun, common in older Stockholm/Göteborg)

## Section: `--price`

### Primary sources

- **Lantmäteriet "Min fastighet"**: `https://www.lantmateriet.se/sv/fastighet-och-mark/information-om-fastigheter/Min-fastighet/` — own-property full extracts, requires BankID
- **Lantmäteriet open data**: `https://geotorget.lantmateriet.se/`
- **SCB (Statistiska centralbyrån) Fastighetspriser**: `https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/fastigheter/fastighetspriser-och-lagfarter/`
- **Mäklarstatistik**: `https://www.maklarstatistik.se/` — agency-aggregated price index
- **Värderingsdata** + **Booli Pris** valuation tools

### Listing platforms

- **Hemnet** — dominant, ~90% market share: `https://www.hemnet.se/`
  - Includes "Salda objekt" (sold prices) searchable per kommun + område
  - URL: `https://www.hemnet.se/bostader?location_ids[]=<id>&item_types[]=bostadsratt|villa|...`
- **Booli** (Schibsted): `https://www.booli.se/` — sold prices map + valuation
- **Blocket Bostad**: `https://www.blocket.se/bostad`
- Agency networks: **Fastighetsbyrån** (largest), **Svensk Fastighetsförmedling**, **Mäklarhuset**, **Notar** (Stockholm premium), **Skandia Mäklarna**

### 2025 price benchmarks (Hemnet + SCB)

| Region | Bostadsrätt SEK/m² | Villa avg total |
|---|---:|---:|
| **Stockholm City (central)** | 85,000–120,000 | 7,000,000–15,000,000+ |
| Stockholm suburbs | 50,000–75,000 | 4,500,000–8,000,000 |
| **Göteborg** | 55,000–75,000 | 5,500,000–8,000,000 |
| **Malmö** | 45,000–65,000 | 4,000,000–6,500,000 |
| Uppsala, Lund | 50,000–75,000 | 5,000,000–7,500,000 |
| Linköping, Västerås, Örebro | 30,000–45,000 | 3,500,000–5,500,000 |
| Smaller cities | 20,000–35,000 | 2,500,000–4,000,000 |
| Norrland (rural) | 8,000–18,000 | 1,000,000–2,500,000 |
| Sommarstuga | varies massively | 800,000–4,000,000 |

### Compute

1. Listing SEK/m² = price / **boarea (BOA)**, the legal living area definition
2. **Trap**: BOA + biarea (BIA: basement, garage, attic) = useful total but not for €/m² comparison
3. **Trap**: Bostadsrätt has **andelstal** (share %) determining BRF voting rights + monthly avgift portion
4. **Bostadsrätt math**: monthly **avgift** (€100–€800/mo typical) covers BRF mortgage + maintenance — affects "true" cost
5. Tomträtt apartments: separate **tomträttsavgäld** (ground rent, increases periodically)

---

## Section: `--traffic`

### Primary sources

- **Trafikverket**: `https://www.trafikverket.se/` — federal road authority
- **NVDB (Nationell vägdatabas)**: `https://nvdb.trafikverket.se/` — open data, all road counts
- City traffic: Stockholm `https://www.stockholm.se/`, Göteborg, Malmö city portals

### Key term

**ÅDT (årsdygnstrafik)** = AADT-equivalent; sometimes "**ÅMDT**" (årsmedeldygnstrafik) — daily-average for the year

### Verdict bands (SE coastal/urban-typical)

- 🟢 < 1,000 v/d (residential gata, lokal väg)
- 🟡 1,000–8,000 v/d (länsväg, urban arterial)
- 🟠 8,000–30,000 v/d (motorväg/E-road, inner ring)
- 🔴 > 30,000 v/d (E4/E6/E18, central Stockholm/Göteborg/Malmö)

---

## Section: `--tax`

### Annual property charge — Fastighetsavgift (CAPPED)

**Sweden has a unique CAP-based property charge** (replaced traditional property tax for residential in 2008):

**Småhus (villa, 2025)**:
- 0.75 % of taxeringsvärde (assessed value, ~75% of market)
- **Cap: SEK 10,074/year (2025) / SEK 10,425/year (2026)** — index-linked to inkomstbasbelopp annually (2026-05-27 verified, source: Skatteverket)
- New builds exempt for 15 years (gradually decreasing)

**Bostadsrätt** (apartment in BRF):
- BRF pays 0.3 % of taxeringsvärde, capped at **~SEK 1,510 per apartment** (2025)
- **Included in monthly avgift** to BRF
- Individual owner doesn't pay separately

**Hyreshus** (apartment building):
- 0.3 % of taxeringsvärde, capped at SEK 1,562/yr per residential unit (2025, source: Skatteverket)

**Effectively very low** — for a SEK 5M villa, taxeringsvärde ~SEK 3.75M × 0.75% = ~SEK 28,125, capped at SEK 10,074/yr (2025) — so you pay the cap (~€840), regardless of value. A capped charge rather than an ad-valorem tax, so high-value homes pay far less proportionally than under classical property tax.

### Transaction taxes

- **Stämpelskatt** (stamp duty on lagfart, canonical Lantmäteriet/Skatteverket term): **1.5 % of price for privatpersoner / bostadsrättsföreningar / kommuner; 4.25 % for juridiska personer** (AB, HB, ekonomiska föreningar) + **expeditionsavgift SEK 825** (lagfart application fee, separate from stamp duty) (2026-05-27 verified, source: Lantmäteriet)
  - For real estate (fastighet)
  - For bostadsrätt: NOT lagfart, but BRF transfer fee (often SEK 0–10,000 negotiable)
- **Pantbrev** (mortgage deed): **2 % of mortgage amount** + SEK 375 (only on new pantbrev; existing transfer) (2026, source: Lantmäteriet)
- **No general transfer tax** beyond lagfart
- **Mäklare** (broker): **2–4 %** typical, paid by seller; negotiable

### Capital gains

- **Reavinstskatt 22 %** on profit (gain) — effective rate = 30 % capital-income tax on 22/30 of the gain for a privatbostad (2026, source: Skatteverket)
- **Uppskov** (deferral): can defer if buying replacement primary residence; **interest-free since 1 Jan 2021** (uppskovsränta abolished) — no annual cost beyond eventual 22% CGT when realised (2026-05-27 verified, source: Skatteverket)
- **Undersökningsplikt — Jordabalken 4 kap. 19 § andra stycket** (canonical caveat-emptor anchor): buyer loses right to price reduction / rescission for any defect they should have detected through ordinary inspection — duty is *långtgående* (far-reaching) per SE doctrine + case law. Besiktning is the only practical defence (source: riksdagen.se / lagen.nu).
- **Privatbostad** (primary residence) deduction methods + reno tracking

### VAT (moms)

- 25 % standard
- 12 % reduced (food + hotels)
- 6 % super-reduced (books, transport)
- Residential property sales: VAT-exempt
- Commercial: 25 %

### Future risk

- Periodic political debate about reintroducing classical property tax (would hit Stockholm/Göteborg homeowners hard)
- Pantbrev system stable
- No transfer tax changes pending

---

## Section: `--rental`

### Long-term residential

- **Hyresreglering** (rent control) — STRICT especially in major cities
- **Bruksvärdesystem**: rent set by negotiation between Hyresgästföreningen + Fastighetsägarna
- **First-hand contract (förstahandskontrakt)** in regulated rental: hard to obtain, often years of queue
- **Andrahandsuthyrning** (subletting your own bostadsrätt): requires BRF approval; max 1-2 yrs typical
- **Privatuthyrningslagen**: looser rules for renting your own house/villa

### Short-let (Airbnb, Booking)

- **Hemförsäkring** disclosure required
- **BRF approval** typically required for cooperative apartments — most BRFs ban or strictly limit short-let
- **Stockholm + Göteborg**: no city-level cap yet but BRF rules + tax authority tightening
- **EU Regulation 2024/1028**: SE transposition pending May 2026 deadline
- Income tax: **SEK 40,000/yr threshold** below which small-scale rental is tax-exempt (own home); above = standard income tax (2025, source: Skatteverket)

### Tax on rental

- Above SEK 40,000/yr: 30 % flat tax on rental income (capital income) (2025, source: Skatteverket)
- Standard 50,000 SEK schablonavdrag (lump-sum deduction) (2025, source: Skatteverket)
- Residential commercial-style rental: subject to standard tax + sometimes moms

---

## Section: `--work=<profession>`

### Job platforms

- **Arbetsförmedlingen Platsbanken** (state): `https://arbetsformedlingen.se/`
- **LinkedIn SE**, **Indeed.se**, **Monster.se**
- **Saco lönesök** (graduate union salary lookup)
- Profession unions (SACO, LO, TCO confederations)

### Self-employment regimes

- **Enskild firma** (sole trader): simplest, no min capital
- **Aktiebolag (AB)**: min SEK 25,000 capital (since 2020 reform)
- **F-skattsedel** registration via Skatteverket
- **Egenavgifter** (self-employed social): ~28.97 % up to certain ceiling
- **A-kassa** unemployment fund (voluntary)

### Salary benchmarks (2025)

- Median monthly gross:
  - Stockholm: ~SEK 45,000-55,000
  - Göteborg/Malmö: ~SEK 38,000-45,000
  - Smaller cities: ~SEK 32,000-38,000
- **Mindre cities + rural**: SEK 28,000-35,000
- No statutory minimum wage (set per industry by union agreement)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SMHI** (meteorology + hydrology) | `https://www.smhi.se/` | Real-time + forecasts + hist. floods |
| **MSB (Myndigheten för samhällsskydd och beredskap)** | `https://www.msb.se/` | Risk maps, civil protection |
| **MSB Översvämningskartor** | `https://www.msb.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/` | Flood hazard maps |
| **SGU (Sveriges geologiska undersökning)** | `https://www.sgu.se/` | Geology, radon, sinkhole maps |
| **SSM (Strålsäkerhetsmyndigheten)** | `https://www.stralsakerhetsmyndigheten.se/` | Radon program |
| **Boverket** | `https://www.boverket.se/` | Building regulations, BBR/BEN |
| **Klimatanpassning (SMHI)** | `https://www.klimatanpassning.se/` | Climate adaptation portal |
| **SGI (Statens geotekniska institut)** | `https://www.sgi.se/` | Landslide + slope stability |

### Specific risks

- **Skred (landslides)** — Vänern + Vättern shores, **Göta älv valley** (severe quick-clay zones, similar to Norway), west coast
- **Översvämning (flooding)** — coastal + lake-shore + river plains; Mälaren risk for Stockholm
- **Stigande havsnivå** (sea-level rise) — south + west coast (Skåne, Halland, Bohuslän)
- **Skogsbrand (forest fire)** — increasing climate risk; Sala 2014, Ljusdal 2018 disasters
- **Radon** — significant in granite areas (Småland, Bergslagen, Uppland, Stockholm bedrock); Sweden's measurement program is comprehensive
- **Earthquake** — very low (Sweden on stable Baltic Shield)
- **Storm/strong wind** — Atlantic depressions Skåne, Halland; Storm Hans (2023), Storm Eowyn (2025) reminders
- **Strandskyddszon** (shoreline protection): 100m default, can be 300m sensitive — restricts construction near waters
- **Saltvattensinträngning** (saltwater intrusion) — coastal wells affected

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960s** | Lead paint, asbestos, weak insulation |
| **1965–1974 "miljonprogrammet"** | Panel concrete, asbestos in joints, energy-inefficient — major retrofit cost |
| **1974–1989** | Asbestos still common, improving insulation |
| **1989–2000** | Better insulation, modern wiring; some PCB issues in fugemassa (sealants) |
| **Post-2008** | BBR + BEN energy standards; BBR 2020 stricter |
| **Post-2017 nZEB** | Low-energy required for new builds |

**Asbestos**: pre-1992 likely; **PCB in fugemassa** (caulking, expansion joints) banned 1973 but present in 1955-1973 builds.

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energideklaration** (energy declaration) | All sales since 2009 | 10 years; penalty up to SEK 10,000 |
| **Lagfartsbevis** | Title verification | At sale |
| **Fastighetsutdrag** (property extract) | All sales | At sale |
| **Besiktning** (independent survey) | NOT mandatory but strongly recommended | Per case |
| **Stadgar + årsredovisning + senaste årsmöte protokoll** (BRF) | If bostadsrätt | At sale |
| **Underhållsplan** (maintenance plan, BRF) | If bostadsrätt | At sale |

### BRF financial health (CRITICAL for bostadsrätt buyers)

Before buying any bostadsrätt, demand:
1. **Senaste tre årsredovisningar** (last 3 annual reports)
2. **Underhållsplan** with cost projections
3. **Belåningsgrad** (BRF mortgage % of property value) — high = risk
4. **Skuldkvot** + **låneförhållande** trends
5. **Avgift per m² historisk** (avgift trend)
6. **Stora kommande projekt** (planned major repairs — stamb, fasad, tak)

**Red flags**: BRF debt > 70 % of property value, deferred maintenance, multi-year avgift increases, < 10 % own capital.

### Climate change projections (SMHI)

- +1.5–4.5 °C by 2050 (RCP scenarios)
- More precipitation: winter floods, summer drought
- Sea-level rise affecting south + west coasts (+30-70 cm by 2100)
- Heat waves: Skåne + central SE more frequent
- Forest fire risk rising sharply
- Permafrost retreat: Norrland

---

## Section: `--mains`

### Sources

- **Svenskt Vatten** (national association): `https://www.svensktvatten.se/`
- Each kommun manages own water + sewer
- Major: **Stockholm Vatten och Avfall**, **Göteborg Kretslopp och Vatten**, **NSVA** (Nordvästra Skånes Vatten och Avlopp), **VA SYD** (Malmö-Lund)

### Verification

- Most populated areas: kommunal mains universal
- **Glesbygd (rural) + sommarstugor**: often **enskilt avlopp** (BDT + 3-chamber tank + filter)
- **EU Urban Wastewater Directive 2026** may tighten rural requirements

### Costs

| Scenario | Cost (SEK) |
|---|---:|
| Anslutning to mains | 30,000–80,000 |
| Mains-line extension via kommun | 50,000–250,000+ |
| Enskilt avlopp 3-chamber + filter | 80,000–250,000 |
| Markbädd renovation | 60,000–150,000 |
| Borrad brunn (drilled well) | 80,000–150,000 |

---

## Cost benchmarks (SE 2026)

| Work | Cost (SEK) |
|---|---:|
| Energideklaration | 4,000–10,000 |
| Mäklare (seller-paid typically) | 2–4 % of price |
| **Lagfartsavgift (buyer)** | **1.5 % + 825** |
| Pantbrev (new mortgage) | 2 % of mortgage + 375 |
| Besiktning | 5,000–15,000 |
| **Total transaction cost (buyer, with new mortgage at 70 % LTV)** | **~3 %** of price |
| **Total transaction cost (cash buyer)** | **~2 %** of price |
| Enskilt avlopp installation | 80,000–250,000 |
| Roof concrete tile (150 m²) | 250,000–500,000 |
| Energy retrofit (Class C → A) | 600,000–1,500,000 |
| Asbestos abatement (small house) | 100,000–400,000 |
| BRF stamb-renovation per apartment | 100,000–300,000 |

## Active fiscal incentives (2025-2026)

- **ROT-avdrag**: tax deduction for renovation labour (50 % deductible up to SEK 50,000/yr/person)
- **RUT-avdrag**: cleaning + household services (50 % deductible up to SEK 75,000/yr/person)
- **Solcellsbidrag**: PV solar grants (up to 60 %)
- **Boverket Klimatpremie**: low-energy retrofit grants
- **Bank green-mortgage discounts**: many banks offer 0.1-0.3 % discount for energy class A/B

## Common listing platforms

- **Hemnet** — dominant (~90 % market share); full extraction
- **Booli** — sold prices + valuation
- **Blocket Bostad** — secondary
- **Fastighetsbyrån, Svensk Fastighetsförmedling, Mäklarhuset** — agency networks
- **Lansförsäkringar Fastighetsförmedling** — bank-affiliated

## Caveats unique to SE

- **Bostadsrätt vs äganderätt**: bostadsrätt is share in BRF housing cooperative; ~60 % of urban dwellings in major cities
- **BRF financial health audit MANDATORY** — bad BRF can wipe out apartment value
- **BRF stamb-renovation cycle** ~50 years — buildings approaching this can have €25-50k assessment per apartment
- **Hyresreglering** kills long-let yield in major cities
- **Strandskydd** (shoreline protection) 100-300m: severe restrictions on new construction near water
- **Tomträtt** apartments (Stockholm, Göteborg older areas): separate ground rent that increases
- **Belåningstak 85 %** (LTV cap) since 2010; **amorteringskrav** mortgage amortization rules
- **Sommarstuga** (summer cottage) often has different regime + utilities + strandskydd
- **Fjällstugor** (mountain cabins): even stricter restrictions + reindeer-husbandry concerns (Sami)
- **Hög radon** especially Stockholm + Småland — measurement before buying recommended
- **Quick clay (kvicklera)** along Göta älv valley + west coast — Skredkommissionen
- **Andelsboende** rare; common is BRF cooperative
- **Tax-free first-time buyer schemes** — none currently
- **Fastighetsskatt vs Fastighetsavgift**: skatt is for non-residential; avgift for residential (the cap-based one)
- **Deklaration K6/K10 forms** — capital gains computation mandatory at sale

## Reddit / forum sources

- **r/sweden**, **r/svenskpolitik**, **r/SwedishPersonalFinance**
- **Hemnet community + blog**, **Fastighet-bidrag forum**
- **Bostadsrätterna** consumer association resources
- Expat: **r/sweden** + **The Local Sweden**

## Verification authorities

| Authority | When to call |
|---|---|
| **Lantmäteriet** | Title verification, lagfart, fastighetsutdrag |
| **Kommun byggnadsnämnd** | Permits, detaljplan, strandskydd |
| **Kronofogden** | Pending lawsuits, encumbrances |
| **Skatteverket** | Lagfartsskatt, capital gains |
| **BRF styrelse + förvaltning** | If bostadsrätt: financial state, assessments |
| **VA-bolag (kommunalt)** | Mains drains verification |
| **Länsstyrelse** | Strandskydd, naturreservat |
| **SGU** | Radon mapping |

## Quirks to know

- **Andelstal vs insats vs månadsavgift** distinctions in BRF
- **Pantbrev** can be reused but must be transferred properly
- **Tomträtt** ground rent often re-negotiated periodically — surprise increases possible
- **Servitut** (easements) common in tomträttsavtal
- **Förenade Hyresgäster** + **Hyresgästföreningen** for tenant disputes
- **Rotavdrag** paperwork via tradesperson, not buyer
- **Klimatdeklaration** for new buildings since 2022 (BBR 28)
- **SBC (Specialfastigheter)** + **Riksbyggen** + **HSB** are major BRF management orgs
- **Bostadsmarknad i Norden tax differential**: SE much lower property tax than DK/FI/NO

## Source URL templates

| Source | URL pattern |
|---|---|
| Lantmäteriet | `https://www.lantmateriet.se/` |
| Hemnet | `https://www.hemnet.se/bostader?location_ids[]=<id>` |
| Booli | `https://www.booli.se/` |
| SCB Fastighetspriser | `https://www.scb.se/hitta-statistik/statistik-efter-amne/boende-bebyggelse-och-mark/fastigheter/fastighetspriser-och-lagfarter/` |
| Mäklarstatistik | `https://www.maklarstatistik.se/` |
| Skatteverket Fastighetsskatt | `https://www.skatteverket.se/privat/fastigheterochbostad/fastighetsavgiftochfastighetsskatt.html` |
| MSB Översvämningskartor | `https://www.msb.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/` |
| SGU Radonkarta | `https://www.sgu.se/produkter-och-tjanster/kartor/kartvisaren/` |
| Boverket | `https://www.boverket.se/` |
| Trafikverket | `https://www.trafikverket.se/` |
| Klimatanpassning | `https://www.klimatanpassning.se/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (Lantmäteriet + SCB + Hemnet all gold-standard); HIGH for fastighetsavgift cap (annual update by Skatteverket). MEDIUM for short-let regulation (EU 2024/1028 SE transposition deadline May 2026).

## Extension TODOs

- [ ] Per-kommun strandskyddsmättning (some kommuner extend default 100m to 300m)
- [ ] BRF financial health red-flag detection (belåningsgrad, underhållsplan, etc.)
- [ ] Tomträtt remaining lease length lookup
- [ ] Quick clay (kvicklera) zone overlay along Göta älv
- [ ] Per-kommun avgiftsuttag (ROT-eligible) tracking
- [ ] Sommarstuga vs permanentbostad distinction patterns
- [ ] Hemnet API extraction patterns (limited)
- [ ] Booli sold-prices API
