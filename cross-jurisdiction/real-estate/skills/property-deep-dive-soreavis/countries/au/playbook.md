# Australia 🇦🇺 — Property Due-Diligence Playbook

ISO2: `au`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`2000` Sydney CBD, `3000` Melbourne CBD, `4000` Brisbane, `6000` Perth)
- **Admin levels**: 6 states + 2 territories + 537 LGAs (Local Government Areas)
- **Currency**: **AUD** (Australian dollar); 1 EUR ≈ 1.55–1.70 AUD
- **Languages**: English (de facto)
- **Cadastre**: **Torrens system** — state-administered (no national portal)
  - **NSW**: NSW Land Registry Services `https://www.nswlrs.com.au` (Vol/Folio)
  - **VIC**: Landata `https://www.landata.vic.gov.au`
  - **QLD**: Titles Queensland `https://www.titlesqld.com.au`
  - **WA**: Landgate `https://www.landgate.wa.gov.au`
  - **SA**: SAILIS `https://sailis.lssa.com.au`
  - **TAS**: LIST `https://www.thelist.tas.gov.au`
- **Identifier**: Title reference (Vol/Folio); paid lookup ~$15-30/title
- **Ownership types**: freehold (Torrens), strata (apt), community title, **old-system title** (pre-Torrens, tiny pockets NSW)
- **Foreign-buyer ban**: established dwellings **1 Apr 2025 – 30 Jun 2029** (FIRB — extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset; 2026-07-03 verified, source ATO / foreigninvestment.gov.au)

## Section: `--price`

### Primary sources

- **CoreLogic (Cotality) Indices**: `https://www.corelogic.com.au/our-data/corelogic-indices` — daily HPI per region
- **ABS Residential Property Price Indexes** (cat 6432.0): `https://www.abs.gov.au/`
- **Domain HPI**: quarterly + monthly
- **REIA Real Estate Market Facts**: `https://www.reia.com.au/`
- **CMP (CoreLogic Property Reports)** — paid

### Listing platforms

- **realestate.com.au** — DOMINANT (REA Group, ~4.4M monthly): `https://www.realestate.com.au`
- **Domain.com.au** — #2 (Nine Entertainment): `https://www.domain.com.au`
- Coverage near-universal across both

### 2026 price benchmarks (CoreLogic/Cotality + ABS, early 2026 — STALE, refresh pending)

*(YoY column is stale: May 2026 Cotality HVI has national values flat at 0.0% MoM — Sydney -0.9% / Melbourne -0.8% MoM, 2.1% / 3.2% below their Nov-2025 peaks; annual growth spread Perth +25.8% vs Melbourne +0.5%. Combined-dwelling medians (May 2026, Cotality HVI): Sydney $1.28M, Melbourne $813k, Brisbane $1.13M, Perth $1.05M — house/unit split medians below need a dedicated `--price` refresh from a Cotality house/unit source. 2026-07-03 verified, source [Cotality HVI May 2026](https://discover.cotality.com/hubfs/Article-Reports/COTALITY%20HVI%20JUNE%202026%20FINAL.pdf))*

| Region | House median | Unit median | YoY |
|---|---:|---:|---:|
| **Sydney** | $1.41M | $865k | +3.2% |
| **Melbourne** | $977k | $603k | -0.6% |
| **Brisbane** | $1.18M | $845k | +6.5% |
| **Adelaide** | $830k | $552k | +5.0% |
| **Perth** | $880k | $540k | +18.3% |
| **Hobart** | $710k | $545k | +1.5% |
| **Darwin** | $620k | $440k | +1.0% |
| **Canberra** | $1.04M | $635k | -1.0% |
| **Combined regional** | $635k | — | +5.5% |

### Compute

1. AUD/sqm = price / **internal area sqm** (or per sq ft in some markets)
2. Cross-check **CoreLogic** sold-price + Domain HPI
3. **Strata levies** for units add ~$3-15k/yr (read sinking fund + admin fund)
4. Foreign buyer surcharge ~+8% (state stamp duty)

### Key terms

- Torrens title = freehold, registered
- Strata = apt complex with body corporate
- Community title = master-planned estate
- BMC = Building Management Committee (mixed-use)
- Off-the-plan = pre-construction purchase

---

## Section: `--traffic`

### Sources

- **State DOT traffic counts**:
  - NSW: **TfNSW Traffic Volume Viewer** `https://www.transport.nsw.gov.au/`
  - VIC: **VicRoads Open Data**
  - QLD: **TMR Open Data**
  - WA: **Main Roads WA Open Data**
- **City open-data portals**: Sydney, Melbourne, Brisbane all have AADT layers

### Key term

**AADT** — same as US/UK.

### Verdict bands

- 🟢 < 1,500 v/d (residential)
- 🟡 1,500–10,000 v/d (collector road, suburban)
- 🟠 10,000–35,000 v/d (urban arterial)
- 🔴 > 35,000 v/d (motorway, M-roads, urban core)

---

## Section: `--tax`

### Annual property tax — Land Tax (state-based)

Land tax = **rate × land value** above threshold.

| State | 2026 threshold | Rate (above threshold) |
|---|---:|---|
| NSW | $1,075,000 (frozen 2025-26 budget) | 1.6% (+ premium 2% over **$6,571,000** — premium threshold also frozen since 2025-26 budget) (2026-05-27 verified, source [Revenue NSW thresholds and rates](https://www.revenue.nsw.gov.au/taxes-duties-levies-royalties/land-tax/understanding-land-tax/thresholds-and-rates) — prior $7,067k figure was incorrect) |
| VIC | **$50,000** (temp. COVID-debt threshold cut from $300k, 2024–2033) | ~0.3–2.65% sliding (+ fixed levy component) (2026-07-03 verified, source [SRO VIC current rates](https://www.sro.vic.gov.au/land-tax-current-rates)) |
| QLD | $600k | 1.0% sliding to 2.75% |
| WA | $300k | 0.25-2.67% sliding |
| SA | $668k | 0.5-2.4% sliding |
| TAS | $99,999 | 0.55-1.5% |

**Principal place of residence (PPR)**: typically exempt.

### Council rates

Per LGA — est. **~0.2-0.4%** of land value annually + waste/water/services (set per-LGA and varies; verify with the relevant council's current rates notice).

### Transaction taxes (Stamp Duty)

State-based, varies hugely:

#### NSW (sliding to 5.5%)

- Up to $14,000: 1.25%
- ... up to top tier: 5.5% over $1M
- **FHB Assistance Scheme (FHBAS)**: full exemption up to $800k, concessional up to $1M — **in place since 1 July 2023**; no public Revenue NSW statement that thresholds are annually indexed — verify at [Revenue NSW FHBAS guide](https://www.revenue.nsw.gov.au/property-professionals-resource-centre/duties-guides/first-home-buyers-assistance-scheme-guide) (2026-05-27 verified)

#### VIC (sliding to 6.5%)

- Up to $25k: 1.4%
- ... top tier 6.5% over $2M
- **Off-the-plan apt < $1M**: stamp duty abolished
- **Vacant Residential Land Tax (VRLT)**: progressive 1% → 2% → 3% based on consecutive vacant years; **statewide from 1 Jan 2025**; metro Melbourne unimproved land subject **from 1 Jan 2026**
- **VIC Short-Stay Levy 7.5%** (from 1 Jan 2025) on STR revenue

#### QLD (sliding to 5.75%)

- FHB exemption to $700k

### Foreign owner surcharges (state)

| State | Foreign buyer surcharge |
|---|---:|
| NSW | **+9%** |
| VIC | **+8%** + 4% absentee owner land tax |
| QLD | **+8%** |
| WA | +7% |
| SA | +7% |

### FIRB approval (federal)

**Foreign Investment Review Board** — required for foreign buyers:
- **Established dwelling ban: 1 Apr 2025 – 30 Jun 2029** (cannot buy resale homes; extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset; 2026-07-03 verified, source ATO / foreigninvestment.gov.au)
- **New dwelling / vacant land**: allowed with FIRB approval + fees
- **Fees scaled by value** (`https://foreigninvestment.gov.au/guidance/general/fees` — schedule re-indexed each 1 Jul; FY2026-27 schedule applies to applications 1 Jul 2026 – 30 Jun 2027; 2026-07-03 verified)
- **Vacancy fee**: 2× application fee (annual, if dwelling vacant >6 months)

### Capital gains tax

- Marginal income tax + **50% discount** for >12-month hold
- **Main residence exemption** — full exemption owner-occupied
- **Foreign residents**: **lost main residence exemption** since 30 Jun 2020

### GST

10% on new builds (margin scheme common).

### Total transaction cost (buyer side)

- NSW domestic ($1M): ~5-6% (stamp duty + legal + LMI if applicable)
- VIC domestic ($1M): ~6% (stamp duty + legal)
- VIC foreign ($1M): ~14% (8% surcharge added)
- NSW foreign ($1M): ~15% (9% surcharge)

### Future risk

- FIRB ban extended to 30 Jun 2029 (realised — announced 2026-27 Federal Budget, from the original 31 Mar 2027 sunset; 2026-07-03 verified)
- VIC VRLT scope expanding through 2026 (metro Melbourne unimproved land)
- State stamp duty reform proposals (NSW First Home Buyer Choice repealed 2023; replaced by FHBAS)

---

## Section: `--rental`

### Long-term residential

- **State Residential Tenancies Acts** govern (RTA NSW, RTA VIC, RTA QLD, etc.)
- **Tenant protections strengthening** (no-fault eviction abolished VIC, NSW reform)
- **Rent caps**: limited (CPI-linked in some states)
- **Bond board**: state-administered (RTBA, etc.)

### Short-let (Airbnb)

#### NSW

- 180-night cap unhosted Greater Sydney
- STRA Property ID via NSW Planning Portal ($65 first 12 months)
- **Byron Shire 60 nights** from 23 Sep 2024 (tighter than statewide)

#### VIC

- 7.5% Short-Stay Levy from 1 Jan 2025
- 180-night statewide cap (from 2025)
- Mornington Peninsula moving to 90 nights

#### QLD

- Council-by-council (Brisbane, Gold Coast, Sunshine Coast register required)

### Tax on rental

- Marginal income tax on net rental
- **Negative gearing**: deductible against other income (UNIQUE in AU/NZ)
- BTL mortgage interest fully deductible
- Capital gains 50% discount + foreign-resident exemption loss

---

## Section: `--work=<profession>`

### Sources

- **JobActive / Workforce Australia**: `https://www.workforceaustralia.gov.au/`
- **Seek.com.au** — biggest: `https://www.seek.com.au/`
- **Indeed.com.au**, **LinkedIn AU**, **CareerOne**, **Adzuna**
- **AHPRA** for healthcare, **Engineers Australia** for engineering, etc.

### Self-employment

- **Sole trader**: ABN registration via ABR
- **Pty Ltd**: ASIC; min $1 capital
- **GST**: register at $75,000 turnover
- **PAYG instalments**: ATO collects

### Salary benchmarks (2025)

- Median annual gross:
  - Sydney: ~$95,000–$130,000
  - Melbourne: ~$85,000–$115,000
  - Brisbane / Perth: ~$75,000–$100,000
  - Smaller cities: ~$65,000–$85,000
- **Federal minimum wage**: $26.44/hr ($1,004.90/38-hr week) from 1 Jul 2026 — FWC *Annual Wage Review 2026* **[2026] FWCFB 3500** (2 Jun 2026): **modern award minimum wages +4.75%**, with a structural adjustment that lifts the lowest ongoing-employment award rate to the same $1,004.90 / $26.44 and the six-month entry-level rate to **$978.10/wk ($25.74/hr)**; the NMW figure is set to maintain alignment with the C13 classification rate rather than by a stated percentage (2026 data, source [FWC decision [2026] FWCFB 3500](https://www.fwc.gov.au/documents/decisionssigned/pdf/2026fwcfb3500.pdf) + [Fair Work Ombudsman](https://www.fairwork.gov.au/about-us/workplace-laws/annual-wage-review/annual-wage-review-2026); 2026-09-18 verified)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Bureau of Meteorology (BoM)** | `https://www.bom.gov.au` | Fire Danger Ratings, flood maps, climate |
| **Geoscience Australia** | `https://www.ga.gov.au` | Australian Flood Risk Information Portal (AFRIP), earthquake catalogue |
| **NSW Rural Fire Service** | `https://www.rfs.nsw.gov.au` | Bush Fire Prone Land mapping (mandatory disclosure trigger) |
| **Climate Council Climate Risk Map** | `https://www.climatecouncil.org.au/resources/climate-risk-map/` | Six hazards by suburb |
| **AFAC Seasonal Bushfire Outlook** | `https://www.afac.com.au/seasonal-outlook` | Pre-season risk forecast |
| **CSIRO National Bushfire Intelligence Capability** | `https://research.csiro.au/nbic` | Research + projections |
| **ARPANSA** | `https://www.arpansa.gov.au/` | Radon (lower than EU; not a major issue) |

### Specific risks

- **Bushfire** — extreme + increasing:
  - Black Saturday 2009 (173 dead, VIC)
  - Black Summer 2019-20 (33 dead, 18.6M ha burned)
  - **NSW Bush Fire Prone Land** mapping triggers building/disclosure rules (BAL-12.5 to FZ ratings)
  - Insurance premiums rising for high BAL ratings
- **Flood** — major risk:
  - **NSW + QLD 2022** floods (Lismore, Brisbane)
  - **Tropical North**: cyclone-driven
  - **Murray-Darling basin**: river flooding
- **Cyclone**: QLD + WA tropical north (Cyclone Tracy 1974, Yasi 2011)
- **Drought**: severe + long-duration (Millennium Drought 2001-2009)
- **Earthquake**: low-moderate; Newcastle 1989 (M5.6, 13 dead); Adelaide hill faults
- **Storm surge** + sea-level rise: coastal communities (Gold Coast, Sunshine Coast)
- **Heatwaves**: increasing; Melbourne 46.4°C, Sydney 47.3°C records
- **Coastal erosion**: NSW, Gold Coast

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | Lead paint, lead pipes |
| **1920s–1980s** | Asbestos very common (white asbestos used until 1987, blue/brown until 1985) |
| **1980s–1990s** | Some asbestos in renos |
| **2000s+** | Modern code; energy improvements |
| **AAC blocks (post-2000)** | Performance issues some buildings |
| **Aluminium composite cladding (post-Grenfell)** | Some buildings flagged |

### Mandatory at sale

| Document | State | Required because |
|---|---|---|
| **Section 32 / Vendor Statement** | VIC | Sale of Land Act 1962 mandatory |
| **Contract for Sale + s.10.7 zoning cert + drainage diagram + title** | NSW | Conveyancing Act |
| **Form 2 (Seller Disclosure Statement)** under Property Law Act 2023 (Qld) (effective 1 Aug 2025) | QLD | Replaces old contract warranties (2026-05-27 verified, source [Holding Redlich on Property Law Act 2023](https://www.holdingredlich.com/queensland-s-property-law-act-new-seller-disclosure-requirements-from-1-august-2025) — prior "Form 1" reference was wrong) |
| **Strata report** | NSW | Strata Schemes Management Act |
| **Owners Corporation cert (s.151)** | VIC | Owners Corporation Act |
| **Pool safety certificate** | QLD | Mandatory pre-sale |
| **Smoke alarm compliance** | QLD | From 1 Jan 2022 |

### Climate change projections

- **Sydney/Melbourne**: +2.0–3.5°C by 2050; +3-6 hot days >35°C
- **Sea-level rise**: +20–80 cm by 2100
- **Bushfire**: significant elevation (FFDI +20-50% by 2050)
- **Drought**: increasing in MDB
- **Cyclone**: poleward shift; Brisbane increasingly cyclone-vulnerable

---

## Section: `--mains`

### Sources

- **Sydney Water**, **Hunter Water**, **Yarra Valley Water (Melbourne)**, **Melbourne Water**, **Urban Utilities (QLD)**, **SA Water**, **Water Corporation (WA)**
- Universal in metro areas; rural may have rainwater tanks + septic

### Costs

| Scenario | Cost (AUD) |
|---|---:|
| Mains connection | $5,000–$15,000 |
| Septic upgrade | $15,000–$35,000 |
| Rainwater tank | $2,000–$8,000 |
| Bored well | $10,000–$30,000 |

---

## Cost benchmarks (AU 2026)

| Work | Cost (AUD) |
|---|---:|
| Building + pest inspection | $500–$1,000 |
| Strata report | $300–$500 |
| Conveyancer / solicitor | $1,500–$3,000 |
| Stamp duty (varies massively) | see above |
| LMI (if <20% deposit) | $5,000–$30,000 |
| **Total transaction cost (NSW $1M)** | **~$50–55k (5%)** |
| **Total transaction cost (VIC $1M)** | **~$60k (6%)** |
| **Total transaction cost (foreign NSW $1M)** | **~$140k (14%)** |
| Roof restoration | $5,000–$15,000 |
| Re-paint | $5,000–$15,000 |
| Bushfire-resilient retrofit | $10,000–$50,000 |
| Asbestos abatement | $3,000–$30,000 |
| Solar PV (5kW) | $4,000–$8,000 (with rebates) |
| Battery storage | $8,000–$15,000 |

## Active fiscal incentives (2025-2026)

- **First Home Buyer Assistance Scheme (FHBAS)**: NSW exempt up to $800k (no public Revenue NSW statement confirming annual indexation — verify at Revenue NSW FHBAS guide)
- **Help to Buy Scheme**: federal (2024+) — equity contribution up to 40% (new) / 30% (existing)
- **First Home Owner Grant (FHOG)**: $10-15k per state (variable)
- **First Home Super Saver (FHSS)**: $50k withdrawal from super for first home
- **Stamp duty concessions**: state-specific (VIC off-the-plan abolished, etc.)
- **Solar/Battery rebates**: federal STCs + state schemes

## Common listing platforms

- **realestate.com.au** — biggest
- **Domain.com.au** — second
- **Allhomes.com.au** (ACT focus)
- **Property.com.au**, **Homely**

## Caveats unique to AU

- **Foreign-buyer established-dwelling ban 1 Apr 2025 – 30 Jun 2029** (FIRB — extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset; 2026-07-03 verified)
- **State-by-state divergence is extreme** — stamp duty, land tax, foreign surcharges, RTA all differ massively
- **Foreign owner surcharges**: NSW 9%, VIC 8%, QLD 8%, WA 7%, SA 7%
- **VIC VRLT statewide from 1 Jan 2025** + metro Melbourne unimproved land from 2026
- **VIC Short-Stay Levy 7.5%** from 1 Jan 2025
- **NSW FHBAS** (annual indexation not confirmed by Revenue NSW — verify) (was First Home Buyer Choice 2022, repealed 2023)
- **FIRB fees + vacancy fee** for foreign-owned dwellings
- **Negative gearing** + **CGT 50% discount** are unique investor features
- **Bushfire BAL ratings** drive insurance + building code; high-BAL means $50k+ retrofit
- **Pool safety certificate** mandatory pre-sale QLD
- **NSW Bush Fire Prone Land** triggers special construction
- **Section 32 (VIC)** + **Form 2 Seller Disclosure Statement (QLD, new 1 Aug 2025)** + **Contract for Sale (NSW)** — mandatory pre-sale disclosures
- **Strata vs community title vs old-system title** — title quality varies
- **Aluminium composite cladding (post-Grenfell)** — some buildings flagged for remediation
- **Negative gearing** — deductible against other income
- **AHPRA + ABS data** drive professional registration verification

## Reddit / forum sources

- **r/AusFinance** — biggest community
- **r/AusProperty**, **r/AustralianRealEstate**
- **r/sydney**, **r/melbourne**, **r/brisbane**
- **PropertyChat** forums
- **Domain Newsletter**, **realestate.com.au Insights**

## Verification authorities

| Authority | When to call |
|---|---|
| **State Land Registry / Titles Office** | Title verification |
| **State Revenue Office (SRO)** | Stamp duty + land tax |
| **Local Council** | Rates + zoning + permits |
| **Owner Corporation / Strata** | If apartment |
| **FIRB** | Foreign-buyer eligibility |
| **NSW RFS / VIC CFA** | Bushfire risk |
| **State conveyancer/solicitor** | Final closing |

## Source URL templates

| Source | URL pattern |
|---|---|
| realestate.com.au | `https://www.realestate.com.au/<region>` |
| Domain | `https://www.domain.com.au/` |
| CoreLogic | `https://www.corelogic.com.au/our-data/corelogic-indices` |
| ABS RPPI | `https://www.abs.gov.au/statistics/economy/price-indexes-and-inflation/residential-property-price-indexes-eight-capital-cities/` |
| FIRB | `https://foreigninvestment.gov.au` |
| BoM | `https://www.bom.gov.au/` |
| Geoscience Australia | `https://www.ga.gov.au/` |
| NSW RFS BFP Land | `https://www.rfs.nsw.gov.au/plan-and-prepare/building-in-a-bush-fire-area` |
| Climate Council | `https://www.climatecouncil.org.au/resources/climate-risk-map/` |
| ATO | `https://www.ato.gov.au/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Coverage check**: pricing (CoreLogic + ABS), traffic, tax (extreme state divergence), rental (state RTA), work, risks (bushfire + flood + cyclone + earthquake), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for CoreLogic Mar 2026 indices + foreign-buyer ban (1 Apr 2025 - 30 Jun 2029 confirmed — extended in the 2026-27 Federal Budget from the original 31 Mar 2027 sunset) + foreign owner surcharges (NSW 9%, VIC 8%, QLD 8% confirmed) + VIC VRLT + Short-Stay Levy 7.5% + QLD Form 2 Seller Disclosure Statement (1 Aug 2025); MEDIUM for the FY2026-27 FIRB fee amounts (verify the current Schedule of Fees PDF on the FIRB fees page) and for market medians beyond the April 2026 Cotality print.
**Last verified**: 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; the federal-minimum-wage line was fully re-verified and re-stamped 2026-09-18 against the FWC Annual Wage Review 2026 decision [2026] FWCFB 3500 — the rest of the playbook keeps the 2026-07-03 date)

## Extension TODOs

- [ ] Per-LGA council rates table
- [ ] State-by-state stamp duty calculator
- [ ] State-by-state foreign surcharge specifics
- [ ] BAL bushfire rating verification flow
- [ ] Strata vs Owners Corp regulations per state
- [ ] FIRB application flow (new dwelling vs vacant land)
- [ ] Negative gearing optimization decision tree
- [ ] CGT main residence + foreign-resident transition
- [ ] State-by-state RTA tenant protections
- [ ] Bushfire BAL retrofit cost estimator
