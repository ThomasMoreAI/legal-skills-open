# Canada 🇨🇦 — Property Due-Diligence Playbook

ISO2: `ca`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: `A1A 1A1` (alphanumeric, 6 chars, space)
- **Admin levels**: 10 provinces + 3 territories; municipalities below
- **Currency**: **CAD** (Canadian dollar); 1 EUR ≈ 1.45–1.55 CAD
- **Languages**: English (official) + French (official); Quebec French-majority
- **Cadastre**: **fragmented by province** — no national portal
  - **Ontario**: Teranet OnLand `https://www.onland.ca` + ServiceOntario LRO
  - **British Columbia**: LTSA `https://ltsa.ca` + LOTR (free beneficial-owner search since Apr 2024)
  - **Alberta**: SPIN2 `https://spin.alt.alberta.ca`
  - **Quebec**: Registre foncier `https://www.registrefoncier.gouv.qc.ca` (only true cadastre system)
- **Identifier**:
  - ON: PIN (9 digits)
  - BC: PID (9 digits XXX-XXX-XXX)
  - AB: Linc (10 digits)
  - QC: cadastre lot number
- **Ownership types**:
  - **Freehold** — most houses
  - **Condo** (most provinces) / **Strata** (BC) / **Co-op** (rare ON/QC)
  - **Leasehold** — 99-year on Indigenous land (e.g., Musqueam, Squamish/Tsleil-Waututh leasehold lands, Vancouver)
- **Federal foreign-buyer ban**: extended to **1 Jan 2027** (Prohibition on the Purchase of Residential Property by Non-Canadians Act)

## Section: `--price`

### Primary sources

- **CREA MLS Home Price Index (HPI)**: `https://www.crea.ca/housing-market-stats/mls-home-price-index/` — national + regional benchmark
- **Teranet-NBC HPI**: `https://housepriceindex.ca` — repeat-sales index, monthly
- **CMHC Housing Market Information Portal**: `https://www03.cmhc-schl.gc.ca/hmip-pimh/`
- **Statistics Canada (StatCan)**: `https://www.statcan.gc.ca/en/subjects-start/housing` — house price index + rental
- **Provincial price boards**:
  - Toronto: TRREB `https://trreb.ca` (Toronto Regional Real Estate Board)
  - Vancouver: **Greater Vancouver REALTORS® (GVR)** — formerly the Real Estate Board of Greater Vancouver (REBGV) — `https://www.gvrealtors.ca/` (monthly benchmark price / HPI package under market intelligence) (2026 data, source GVR; 2026-09-18 verified)
  - Calgary: CREB `https://www.creb.com`
  - Montreal: APCIQ `https://apciq.ca`

### Listing platforms

- **Realtor.ca** — DOMINANT (CREA, ~95% MLS coverage): `https://www.realtor.ca`
- **Centris.ca** — Quebec only (QPAREB): `https://www.centris.ca`
- **Royal LePage**, **RE/MAX**, **Zolo** — agency networks

### 2026 price benchmarks (CREA MLS HPI March 2026)

| Region | HPI Composite (CAD) | YoY change |
|---|---:|---:|
| **National composite** | $664,400 | -4.7% |
| **Toronto (TRREB)** | $1,017,796 (avg) | -7.4% |
| **Vancouver (Greater Van)** | $1,104,300 | -6.8% |
| **Calgary** | $565,600 (HPI) / $641,844 (avg) | -4.2% |
| **Montreal (CMA)** | ~$590,000 | +0.5% |
| **Ottawa** | ~$648,000 | -1.2% |
| **Halifax** | ~$540,000 | +2.0% |
| **Edmonton** | ~$420,000 | +0.5% |
| **Winnipeg** | ~$370,000 | +1.5% |

### Compute

1. CAD/sq ft = price / **square footage** (sqft is dominant unit, not m²)
2. Cross-check **Realtor.ca** sold-price history + Teranet for closed sales
3. **HPI vs average**: HPI strips out luxury/distressed; average runs 5-15% higher
4. **Convert CAD to EUR/USD** at current FX

### Key terms

- PIN/PID/Linc = title identifier per province
- Strata (BC) = condo/townhouse with shared common property
- Co-op = corporate ownership, individual occupancy rights (rare)
- HPI = MLS Home Price Index (CREA)

---

## Section: `--traffic`

### Sources

- **Transport Canada national highway system**: `https://tc.canada.ca/`
- **Provincial DOT traffic counts**:
  - Ontario: **MTO Provincial Highways Traffic Volumes** — search the Ontario Open Data Catalogue (`data.ontario.ca`) for "provincial highways traffic volumes" (verify current dataset URL on the catalogue)
  - BC: **DriveBC Traffic** `https://www.drivebc.ca/`
  - Alberta: **Open Data Alberta** traffic
  - Quebec: **MTQ Traffic Volumes**
- **City open-data portals**: Toronto, Vancouver, Calgary all have AADT layers

### Key term

**AADT (Annual Average Daily Traffic)** — same as US/UK.

### Verdict bands

- 🟢 < 1,500 v/d (residential, suburban side streets)
- 🟡 1,500–10,000 v/d (urban arterial, suburban collector)
- 🟠 10,000–35,000 v/d (regional highway, urban core)
- 🔴 > 35,000 v/d (highway 401, ring roads, major arterials)

---

## Section: `--tax`

### Annual property tax — Provincial / Municipal

Property tax = **mill rate × assessed value** (assessed by provincial agency, e.g., MPAC ON, BC Assessment, MAA AB).

Mill rates below are est. magnitudes set annually by each municipality (verify the current year on the municipal tax bill / city budget — rates may have changed since):

| Province / City | Mill rate (est.) | Assessment basis |
|---|---:|---|
| Toronto | ~0.66% | MPAC (every 4 years; 2016 frozen) |
| Vancouver (City) | ~0.28% | BC Assessment annual |
| Calgary | ~0.74% | Annual |
| Montreal | ~0.60% | Annual |
| Ottawa | ~1.02% | MPAC |
| Halifax | ~0.95% | PVSC annual |
| Edmonton | ~0.91% | Annual |

**Education portion**: separately added (est. ~0.15-0.50% depending on province/board — verify on the municipal tax bill).

### Transaction taxes (LTT — Land Transfer Tax)

#### Ontario LTT

Tiered 0.5% to 2.5% — provincial:
- Up to $55,000: 0.5%
- $55-250k: 1.0%
- $250-400k: 1.5%
- $400k-$2M: 2.0%
- > $2M: 2.5%

**Toronto Municipal LTT (MLTT)**: graduated rates with **new high-value tier from 1 Apr 2026** (passed by Council 17 Dec 2025): **4.4%** ($3M–$4M), **5.45%** ($4M–$5M), **6.5%** ($5M–$10M), **7.5%** ($10M–$20M), **8.6%** (>$20M) — on top of base 0.5–2.5% (2026-05-27 verified, source: [toronto.ca — MLTT rates](https://www.toronto.ca/services-payments/property-taxes-utilities/municipal-land-transfer-tax-mltt/municipal-land-transfer-tax-mltt-rates-and-fees/)).

**FTB rebate**: up to $4,000 ON + $4,475 Toronto.

#### BC Property Transfer Tax (PTT)

Tiered:
- Up to $200k: 1%
- $200k–$2M: 2%
- $2M+: 3%
- **+2% over $3M** (additional)
- **Foreign buyer Additional Property Transfer Tax: 20%** in the specified Regional Districts: Capital (CRD), Fraser Valley, Metro Vancouver, Central Okanagan, Nanaimo (2026-05-27 verified, source: [gov.bc.ca — Additional Property Transfer Tax](https://www2.gov.bc.ca/gov/content/taxes/property-taxes/property-transfer-tax/additional-property-transfer-tax))

#### Alberta — Land Title Transfer Fee

Flat ~$50 + ~$2 per $5,000 of value (very low compared to ON/BC).

#### Quebec — Welcome Tax / Droit de mutation

Tiered 0.5–2.5% depending on municipality (Montreal 3% over $2.6M).

### Other taxes

- **Federal GST 5%** on new builds (PST 7% in BC, HST 13% ON, HST 15% Atlantic)
- **Underused Housing Tax (UHT)**: **REPEALED 26 Mar 2026** by Bill C-15 (no filing for 2025+; 2022-2024 obligations remain)
- **BC Speculation & Vacancy Tax (SVT)**: **rates DOUBLED for 2026**:
  - Foreign owners + satellite families: **3%** (was 2%)
  - BC residents: **1%** (was 0.5%)
  - Credit raised $2k → $4k
  - Filing due first business day of July
- **Vancouver Empty Homes Tax**: **3%** of assessed value (separate from BC SVT)
- **Toronto Vacant Home Tax**: **3%** (since 2024)
- **Foreign buyer ban**: extended to **1 Jan 2027**; review for post-2027 easing under way (per Dec 2025 reporting — flag as "in flux")

### Capital gains

- Federal: **50% inclusion rate** (2/3 inclusion proposal **CANCELLED 21 Mar 2025** by PM Carney announcement; the $250k/yr threshold was part of the cancelled package and also fell away) (2026-05-27 verified, source: [PM news release](https://www.pm.gc.ca/en/news/news-releases/2025/03/21/prime-minister-mark-carney-cancels-proposed-capital-gains-tax-increase))
- Marginal rates: ~25–53% combined federal+provincial
- **Principal residence exemption** — full exemption for years owner-occupied
- **Foreign residents**: lose principal residence exemption from 2026
- **Non-resident disposition — Section 116 clearance**: when a non-resident DISPOSES of Canadian real property, the buyer must withhold **25% of gross proceeds** (50% on depreciable / rental property) until CRA issues a Form T2062 certificate of compliance; CRA processing typically 8-16 weeks; 10-day notice requirement (2026-05-27 verified, source: [CRA IC72-17R6 — Section 116](https://www.canada.ca/en/revenue-agency/services/forms-publications/publications/ic72-17/ic72-17r6-procedures-concerning-disposition-taxable-canadian-property-non-residents-canada-section-116.html))

### Total transaction cost (buyer side)

- ON resale primary: ~3-4% (LTT + legal + title insurance)
- ON resale Toronto >$2M: ~6-8% (tiered LTT + MLTT)
- BC primary <$2M: ~2-3% (PTT + legal)
- BC foreign buyer: ~22-23% (PTT + 20% surcharge)
- AB: <1% (no LTT, just title fee)

### Future risk

- Foreign buyer ban review post-2027 (likely modified)
- BC SVT rates may rise further
- Federal capital-gains inclusion-rate 2/3 proposal **CANCELLED 21 Mar 2025** (no longer in policy pipeline)

---

## Section: `--rental`

### Long-term residential

- **Residential Tenancies Act** per province (RTA ON, RTB BC, RTDRS AB, Régie du logement QC)
- **Rent control** (varies):
  - ON: post-2018 builds exempt; pre-2018 capped at CPI
  - BC: capped at inflation (2.5% max 2024)
  - AB: no rent control (full market)
  - QC: ad-hoc indexed
- **Tenant protections strict** in ON/QC (tenant-favorable hearings)

### Short-let (Airbnb)

#### Vancouver

- **Principal-residence-only**
- BC provincial registry mandatory since **1 May 2025**
- Fees: $100/yr owner-occupied, $450/yr non-OO
- Fines up to $50k

#### Toronto

- Principal residence only
- 180-night cap on entire-home
- Registration **$375/yr** (raised Jan 2025)
- Fines up to $50k corp

#### Quebec / Montreal

- **CITQ registration** mandatory
- Numéro CITQ on listing required

### Tax on rental

- Rental income = federal+provincial marginal income tax
- Foreign owners: **25% withholding** at gross (or NR4/NR6 elections)
- Capital gains 50% inclusion at sale
- BTL mortgage interest fully deductible

---

## Section: `--work=<profession>`

### Sources

- **Job Bank Canada**: `https://www.jobbank.gc.ca/`
- **Indeed.ca**, **LinkedIn CA**, **Glassdoor**, **Workopolis**, **Eluta**
- **Provincial workers' compensation boards**: WSIB ON, WorkSafeBC, etc.

### Self-employment

- **Sole proprietorship**: register provincially (e.g., ServiceOntario)
- **Federal incorporation**: Industry Canada; min $1 capital
- **Provincial incorporation**: similar
- **GST/HST registration**: from $30,000 turnover
- **Professional bodies**: per profession (CA, MD, P.Eng, etc.)

### Salary benchmarks (2025)

- Median annual gross:
  - Toronto / Vancouver: ~$70,000–$95,000
  - Calgary / Montreal / Ottawa: ~$60,000–$80,000
  - Smaller cities: ~$50,000–$65,000
- Federal minimum wage: $17.30/hr (2025)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Earthquakes Canada (NRCan)** | `https://www.earthquakescanada.nrcan.gc.ca` | Seismic, RiskProfiler |
| **Public Safety Canada — National Risk Profile** | `https://www.publicsafety.gc.ca/cnt/mrgnc-mngmnt/ntnl-rsk-prfl/` | Top 3: earthquake, wildfire, flood |
| **GEO.CA flood polygons** | `https://geo.ca/emergency/` | Satellite-derived flood maps |
| **BC PreparedBC hazard map** | `https://www2.gov.bc.ca/gov/content/safety/emergency-management/preparedbc/know-your-hazards/hazard-map` | BC hazards |
| **ECCC weather/storm** | `https://climate.weather.gc.ca/` | Climate, weather data |
| **Canadian Wildland Fire Information System** | `https://cwfis.cfs.nrcan.gc.ca/` | Wildfire (FWI, hot spots) |
| **Health Canada radon** | `https://www.canada.ca/en/health-canada/services/health-risks-safety/radiation/radon.html` | Radon zones |

### Specific risks

- **Wildfire** — extreme + increasing:
  - BC, AB, ON (boreal), Atlantic
  - 2023 record fire season (~18.5M ha burned — verify with NRCan / CIFFC 2023 season summary)
  - Black summer 2023 evacuations Yellowknife, Kelowna, West Kelowna
  - **Increased home insurance exclusions** in WUI zones
- **Flood** — major risk:
  - **Toronto**: urban flash flooding (2013, 2024)
  - **Calgary**: 2013 disaster
  - **Atlantic Canada**: storm surge + sea-level
  - **Montreal/Quebec**: spring snowmelt
  - GEO.CA satellite-derived flood maps
- **Earthquake**:
  - **BC West Coast — Cascadia Subduction Zone**: M9 expected
  - **Eastern Canada**: Charlevoix-Kamouraska seismic zone (1925 M6.2)
  - Vancouver/Victoria: high seismic preparedness required
- **Permafrost**: Yukon + NWT + northern BC/AB; thaw-triggered building damage
- **Ice storms**: Eastern (Quebec 1998 ice storm)
- **Hurricane**: Atlantic Canada (Fiona 2022)
- **Tornado**: Prairie + Southern ON
- **Radon**: high in some BC/AB/SK areas (Saskatchewan, Manitoba, parts of Yukon)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1950** | Asbestos cement, lead paint, lead pipes, knob-and-tube wiring |
| **1950s–1970s** | Asbestos very common (banned 1990s); UFFI insulation 1977-1980 (banned) |
| **1980s–1990s** | Some asbestos in older renos; Poly-B plumbing (class-action) |
| **2000s+** | Modern code; energy improvements |
| **Vermiculite / Zonolite attic insulation** | Pre-1990 — contains asbestos; flag for testing |
| **Cladding fires** (post-Grenfell era): some buildings flagged |

### Mandatory at sale

| Document | Province | Notes |
|---|---|---|
| **Property Disclosure Statement (PDS)** | BC mandatory | Seller signs; buyer reviews |
| **SPIS (Sellers' Property Information Statement)** | ON voluntary | Optional but common |
| **Real Property Report (RPR) + compliance** | AB mandatory | Survey of structures |
| **Déclaration du vendeur** | QC standard | Seller declaration |
| **Title insurance** | ON near-universal | Replaces survey/expert opinion |
| **Strata documents (Form B/F)** | BC condos | HOA disclosure |
| **Status Certificate** | ON condos | Condo health snapshot |

### Climate change projections

- BC + AB + Prairies: **+3–5°C** by 2050 (est., scenario-dependent — verify with Canada in a Changing Climate / ECCC regional projections)
- Wildfire intensity: significant elevation
- Permafrost retreat: NWT, Yukon
- Atlantic sea-level rise: est. +30–80 cm by 2100 (scenario-dependent — verify with ECCC sea-level projections)
- Increased insurance premiums for wildfire/flood

---

## Section: `--mains`

### Sources

- Per-municipality water utilities (Toronto Water, Metro Vancouver, City of Calgary, Service de l'eau Montreal)
- Health Canada water quality
- Universal in urban; rural may have wells + septic

### Costs

Illustrative contractor estimates, not quoted figures — verify with local quotes:

| Scenario | Cost (CAD, est.) |
|---|---:|
| Water/sewer connection (urban) | $5,000–$15,000 |
| Mains-line extension | $20,000–$60,000+ |
| Septic replacement | $15,000–$35,000 |
| Bored well | $8,000–$20,000 |

---

## Cost benchmarks (CA 2026)

| Work | Cost (CAD) |
|---|---:|
| Home inspection | $400–$700 |
| Title insurance | $200–$700 |
| Real estate lawyer / notary | $1,500–$3,000 |
| Survey / RPR | $700–$2,500 |
| Land Transfer Tax (varies) | see above |
| **Total transaction cost (ON, $1M, FTB)** | **~$30k (3%)** |
| **Total transaction cost (BC, $1.5M)** | **~$35-45k (2.5-3%)** |
| **Total transaction cost (BC foreign, $1.5M)** | **~$345k (23%)** |
| Roof (asphalt shingle) | $8,000–$15,000 |
| Window replacement | $500–$1,200 each |
| Asbestos abatement | $5,000–$30,000+ |
| Vermiculite removal | $10,000–$40,000+ |
| Knob-and-tube re-wire | $8,000–$15,000 |
| Energy retrofit | $30,000–$80,000 |
| Heat pump installation | $8,000–$20,000 (with rebates) |

## Active fiscal incentives (2025-2026)

- **First-Time Home Buyer Incentive (FTHBI)**: federal shared-equity (5-10% of purchase) — being wound down
- **First Home Savings Account (FHSA)**: $40k lifetime contribution, tax-deductible + tax-free withdrawal for first home
- **HBP (Home Buyers' Plan)**: RRSP up to $60k withdrawal (raised 2024)
- **GST/HST New Housing Rebate**: rebate on portion of GST for new builds
- **Provincial FTB rebates**: ON up to $4k, BC up to $8k, etc.
- **Greener Homes Loan + Grant**: federal energy retrofit (up to $40k loan + $5k grant)
- **CMHC Multi-Unit Mortgage Loan Insurance**: lower down for purpose-built rentals

## Common listing platforms

- **Realtor.ca** — DOMINANT, ~95% MLS
- **Centris.ca** — Quebec only
- **Royal LePage, RE/MAX, Sotheby's, Engel & Völkers** — agency networks
- **Zolo** — alternative
- **Honest Door** — sold-price aggregator (BC/AB)

## Caveats unique to CA

- **Federal foreign-buyer ban** until **1 Jan 2027** (Prohibition Act in force 1 Jan 2023; repeal deferred to 1 Jan 2027 by Budget Implementation Act, 2024, No. 1, S.C. 2024, c. 17, s. 149)
- **Provincial fragmentation extreme** — each province has different cadastre, LTT, rent control, condo law
- **BC vs ON major divergence** — BC PTT 1-3%+2%+20% foreign; ON LTT 0.5-2.5% + Toronto MLTT
- **UHT REPEALED 26 Mar 2026** — no longer applies for 2025+ (file 2022-2024 obligations)
- **BC SVT rates DOUBLED 2026** — foreign 3%, BC 1%
- **Vancouver Empty Homes Tax 3%** + **Toronto Vacant Home Tax 3%**
- **BC LOTR (Land Owner Transparency Registry)** — free public beneficial-owner search since Apr 2024 (UNIQUE in Canada)
- **Vermiculite / Zonolite attic insulation** — pre-1990 — common asbestos hazard
- **Knob-and-tube wiring** — pre-1950s; insurance-blocking
- **Poly-B plumbing** (1978-1995) — class-action; flagged
- **Mortgage stress test** = OSFI minimum qualifying rate: **greater of contract rate + 2% or 5.25% floor**; from **21 Nov 2024** uninsured-mortgage renewals switching lenders are exempt from re-stress-testing if loan + amortization unchanged (2026-05-27 verified, source: [OSFI MQR for uninsured mortgages](https://www.osfi-bsif.gc.ca/en/supervision/financial-institutions/banks/minimum-qualifying-rate-uninsured-mortgages))
- **Cross-border tax** — US/CA dual citizens face FATCA + complex CGT
- **Strata depreciation reports** mandatory in BC (every 5 years)
- **Indigenous land** — leasehold-only on reserve land (e.g., Musqueam, Squamish/Tsleil-Waututh leasehold lands, Vancouver)
- **CMHC mortgage insurance** mandatory if down payment <20%
- **Toronto MLTT graduated high-value rates** from 1 Apr 2026

## Reddit / forum sources

- **r/RealEstateCanada**
- **r/PersonalFinanceCanada** — mortgage + tax discussion
- **r/canadahousing**, **r/TorontoRealEstate**, **r/VancouverRE**
- **Globe and Mail Real Estate**, **Financial Post Personal Finance**
- **Better Dwelling** (analysis)

## Verification authorities

| Authority | When to call |
|---|---|
| **Provincial Land Title Office** | Title verification |
| **Municipal property tax department** | Tax assessment + arrears |
| **MPAC (ON) / BC Assessment** | Assessed value |
| **Real estate lawyer** (mandatory in most provinces) | Final closing |
| **Strata/Condo board** | If apartment |
| **Health Canada Radon** | Testing |
| **CMHC** | Mortgage insurance + market data |

## Source URL templates

| Source | URL pattern |
|---|---|
| Realtor.ca | `https://www.realtor.ca/<region>` |
| Centris.ca (QC) | `https://www.centris.ca/` |
| Teranet OnLand (ON) | `https://www.onland.ca/` |
| BC LTSA + LOTR | `https://ltsa.ca/` + `https://landtransparency.ca/` |
| AB SPIN2 | `https://spin.alt.alberta.ca/` |
| QC Registre foncier | `https://www.registrefoncier.gouv.qc.ca/` |
| CREA HPI | `https://www.crea.ca/housing-market-stats/mls-home-price-index/` |
| Earthquakes Canada | `https://www.earthquakescanada.nrcan.gc.ca/` |
| Public Safety Canada | `https://www.publicsafety.gc.ca/` |
| Health Canada Radon | `https://www.canada.ca/en/health-canada/services/health-risks-safety/radiation/radon.html` |
| CRA tax | `https://www.canada.ca/en/revenue-agency.html` |

## Status

✅ **Fully populated** as of 2026-04-25 (Vancouver board name (Greater Vancouver REALTORS) corrected 2026-09-18 per gvrealtors.ca). Ownership tracker entries re-checked 2026-09-24 in the October regwatch wave (see shared/regulatory-watch.md).
**Coverage check**: pricing (CREA + provincial boards), traffic, tax (extreme provincial divergence), rental (RTA per province), work, risks (wildfire + flood + earthquake + permafrost + radon), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for CREA HPI Mar 2026 + UHT repeal (Bill C-15 Royal Assent confirmed) + BC SVT 2026 doubling + Toronto MLTT graduated tier (1 Apr 2026) + foreign buyer ban extension; MEDIUM for post-2027 foreign-buyer review (in flux); MEDIUM for capital-gains inclusion rate (2/3 proposal paused).

## Extension TODOs

- [ ] Per-municipality property tax mill rates table
- [ ] Per-province condo/strata law nuances
- [ ] BC LOTR beneficial-owner verification flow
- [ ] Indigenous land lease verification (Musqueam, Cowichan, etc.)
- [ ] Vermiculite/Zonolite testing decision tree
- [ ] Poly-B / Knob-and-tube remediation cost
- [ ] Stress test mortgage qualification calculator
- [ ] Cross-border US/CA tax decision tree
- [ ] Per-province RTA tenant protections summary
- [ ] BC SVT vs Vancouver EHT scenario optimization
