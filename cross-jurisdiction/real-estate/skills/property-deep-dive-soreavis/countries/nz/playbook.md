# New Zealand 🇳🇿 — Property Due-Diligence Playbook

ISO2: `nz`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1010` Auckland CBD, `6011` Wellington CBD, `8013` Christchurch)
- **Admin levels**: Central government + 16 regions + 67 territorial authorities
- **Currency**: **NZD** (New Zealand dollar); 1 EUR ≈ 1.75–1.90 NZD
- **Languages**: English (de facto) + Te Reo Māori (official)
- **Cadastre**: **Toitū Te Whenua / LINZ (Land Information NZ)** — fully unified national system
  - **Landonline**: `https://www.linz.govt.nz/` (lawyers/surveyors, paid)
  - **Public Land Record Search**: `https://lrs.linz.govt.nz/search/` — **$8 per record**
- **Identifier**: Record of Title (RT) reference (e.g. `WN12A/345`); supersedes older Certificate of Title
- **Ownership types**:
  - **Freehold (fee simple)** — most common
  - **Leasehold** — Cornwall Park (Auckland), Glasgow Crescent, Cashmere Hills; **99-year leases common on Māori land** under Te Ture Whenua Māori Act 1993
  - **Cross-lease** — ~10% of Auckland; clunky shared ownership of section + flat plan
  - **Unit title** — apartments, body corporate
- **Foreign-buyer ban**: Overseas Investment Amendment Act 2018; AU + SG resident citizens exempt; new builds + apartments off-the-plan partly exempt. **Modified 19 Dec 2025** (Royal Assent — Overseas Investment (National Interest Test and Other Matters) Amendment Act): Active Investor Plus (AIP) + Investor 1 + Investor 2 visa holders can now obtain OIO consent to buy ONE residential property valued (land + build) **over NZ$5,000,000**; fast-track ~5 working day OIO process; fees NZ$2,040 (existing >$5M) / NZ$3,500 (new build). Order in Council expected early 2026 (2026-05-27 verified, source: [Bell Gully OIA update](https://www.bellgully.com/insights/overseas-investment-act-update-door-opens-for-investor-visa-holders-buying-residential-land/))

## Section: `--price`

### Primary sources

- **REINZ (Real Estate Institute of New Zealand) HPI**: `https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx` — monthly, authoritative
- **Quotable Value (QV) / Cotality NZ**: `https://www.qv.co.nz/price-index/` — local government valuation; rates basis
- **Stats NZ**: `https://www.stats.govt.nz/` — house price + rental indices
- **OneRoof Property Report**: `https://www.oneroof.co.nz/` (NZ Herald)

### Listing platforms

- **Trade Me Property**: `https://www.trademe.co.nz/property` — ~39k listings
- **realestate.co.nz**: `https://www.realestate.co.nz` — industry-owned, ~35k listings
- **OneRoof** (NZ Herald) — secondary
- **Homes.co.nz** — sold-price specialty

### 2026 price benchmarks (REINZ + QV March 2026)

| Region | Median (NZD) | YoY |
|---|---:|---:|
| **National median** | $788,000 | 0.0% (HPI) |
| **Auckland (Tāmaki Makaurau)** | $1,040,000 | -1.1% |
| **Wellington City** | $908,000 (avg QV) | **-5.1%** (hit hardest) |
| **Christchurch (Ōtautahi)** | $735,000 | record |
| **Canterbury HPI** | — | +3.2% |
| **Hamilton** | $755,000 | -1.0% |
| **Tauranga** | $880,000 | +0.5% |
| **Dunedin** | $625,000 | -2.0% |
| **Queenstown Lakes** | $1,500,000+ | +2.0% |

### Compute

1. NZD/sqm = price / **floor area** (sqm dominant unit)
2. Cross-check **REINZ HPI** + **QV** + **Trade Me sold-price**
3. **HPI vs median**: HPI strips luxury/distressed; median runs 5-10% higher
4. **Wellington ~-26% est.** from Oct 2021 peak (worst-affected city — verify peak-to-current against QV House Price Index)
5. **Convert NZD to EUR/USD** at current FX

### Key terms

- RT (Record of Title) = land title
- Cross-lease = shared title with flat plan (Auckland-specific quirk)
- Body Corporate = HOA for unit title
- LIM = Land Information Memorandum (council report)
- Bright-line = capital gains test

---

## Section: `--traffic`

### Sources

- **NZTA (Waka Kotahi) Traffic Counts**: `https://www.nzta.govt.nz/resources/state-highway-traffic-volumes`
- **AADT data + heavy-vehicle proportion** by road
- **Council traffic data** for local roads

### Key term

**AADT** — same as US/UK.

### Verdict bands

- 🟢 < 1,000 v/d (residential, rural)
- 🟡 1,000–8,000 v/d (suburban arterial)
- 🟠 8,000–25,000 v/d (urban arterial, SH-routes)
- 🔴 > 25,000 v/d (motorways: SH1, SH16, SH20)

---

## Section: `--tax`

### Annual property tax — Council Rates

Rates = **general rate × Capital Value (CV) or Land Value (LV)** + targeted rates.

**No central property tax** — rates are local-authority-only.

| City | Annual rates (~2024-2025 est., typical) |
|---|---:|
| Auckland Council | ~0.30% of CV (median ~$3,500) |
| Wellington | ~0.65% of CV (median ~$4,500) |
| Christchurch | ~0.60% (median ~$3,800) |
| Queenstown Lakes | ~0.45% (median ~$5,500) |

Figures are estimates — confirm the current year's rates demand against each council's rates schedule (Auckland Council / Wellington City Council / Christchurch City Council / Queenstown Lakes District Council).

**Rates frozen** in some councils 2024-2025 due to crisis politics.

**Auckland — short-term letting shifts the rating category**: peer-to-peer STR moves the property onto a graduated business-rating share of general rates + CATTR once it is let 29+ nights in the 1 Jul – 30 Jun year; the Accommodation Provider Targeted Rate (APTR) itself has been suspended since 2020 and is NOT reinstated for 2026/2027. Bands and deadlines in `--rental` § Auckland (2026-08-07 verified, source: [Auckland Council — Accommodation Provider Targeted Rate](https://www.aucklandcouncil.govt.nz/en/property-rates-valuations/accommodation-provider-targeted-rate.html))

### Transaction taxes

- **NO STAMP DUTY** (abolished 1999) — UNIQUE in OECD
- Legal fees: $1,500–$3,000
- LIM report: $300–$500
- Building report: $500–$1,000

### Capital gains tax — BRIGHT-LINE TEST

**No general CGT in NZ.** But the **bright-line test** taxes residential property gains as ordinary income IF sold within the bright-line period:

| Bright-line period | When applicable |
|---|---|
| **2 years** | From 1 Jul 2024 (current; was 5/10) |
| 5 years | Acquired 29 Mar 2018 – 26 Mar 2021, sold before 1 Jul 2024 (2024 data, source IRD) |
| 10 years (5 for qualifying new builds) | Acquired on/after 27 Mar 2021, sold before 1 Jul 2024 (2024 data, source IRD) |
| 2 years | Earlier regime for acquisitions before 29 Mar 2018 — start date not verified; verify at https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test/property-sold-before-1-july-2024 |

- "Bright-line start date" varies (settlement, contract date)
- Main home exemption applies but tightened
- Inheritance + relationship transfers exempt

### GST

- **15%** on new builds; resale exempt
- From **1 Apr 2024**: GST collected by online STR marketplaces (8.5% passed to non-GST-registered hosts)

### Interest deductibility (BTL)

**Fully restored 100% from 1 Apr 2025** (tax year ending 31 Mar 2026 onwards) — major reversal of 2021 phase-out.

### Foreign-buyer regime

**Overseas Investment Amendment Act 2018** — foreign nationals **cannot buy** existing residential property except:
- AU + SG resident citizens (treaty exemption)
- Existing residence permit holders
- New builds + apartments off-the-plan (with conditions)

### Total transaction cost (buyer side)

- Resale primary: ~$3,000–$5,000 fixed (legal + searches + LIM) — **lowest in OECD**
- New build with GST: 15% + ~$3,000 fees

### Future risk

- Bright-line expansion possible if government changes
- Foreign-buyer ban likely to remain
- Interest deductibility could be re-tightened

---

## Section: `--rental`

### Long-term residential

- **Residential Tenancies Act 1986** (RTA) — tenant-protective
- **No-cause 90-day termination RESTORED 30 Jan 2025** by Residential Tenancies Amendment Act 2024 (passed 17 Dec 2024), reversing the 11 Feb 2021 abolition; also adds 42-day notice for owner/family occupation or sale-with-vacant-possession, and 21-day tenant termination; pet-related changes effective 1 Dec 2025 (2026-05-27 verified, source: [HUD — RTA Amendment Act 2024](https://www.hud.govt.nz/our-work/residential-tenancies-amendment-act-2024))
- **Rent increases** capped at every 12 months
- **Rental loss ring-fencing** — losses ring-fenced per IRD
- **Healthy Homes Standards** mandatory for rentals (insulation, heating, ventilation, moisture, draught)

### Short-let (Airbnb, Bachcare)

#### Queenstown Lakes

- **Residential Visitor Accommodation registration** required
- **Night cap is zone-specific**: e.g. Lower Density Suburban Residential allows a cumulative 90 nights/yr from initial registration (PDP ch.7 std 7.5.18.1, Jun 2023 Decisions Version); operating beyond your zone's standards needs a resource consent - check the parcel's zone on QLDC ePlan (2026 data, source [QLDC STVA](https://www.qldc.govt.nz/services/rates-property/short-term-visitor-accommodation))
- **Rates**: no change if available to short-term guests for up to 28 days/yr cumulative; under 180 days = rated Mixed Use (+25-35%); 181-365 days = rated Accommodation (+50-80%); a Homestay = Mixed Use (+25-35%); changes apply from the next rating year beginning 1 Jul (2026 data, source [QLDC STVA](https://www.qldc.govt.nz/services/rates-property/short-term-visitor-accommodation))

#### Auckland

- Unitary Plan visitor accommodation rules
- **APTR (Accommodation Provider Targeted Rate) suspended since 2020 — NOT reinstated for 2026/2027.** The live cost is a **graduated general-rates + CATTR business uplift** on peer-to-peer STR, nights counted **1 Jul – 30 Jun** (2026-08-07 verified, source: [Auckland Council — Accommodation Provider Targeted Rate](https://www.aucklandcouncil.govt.nz/en/property-rates-valuations/accommodation-provider-targeted-rate.html))

| Nights let (1 Jul – 30 Jun) | Rating split |
|---|---|
| **up to 28** | stays 100% residential |
| **29–135** | 75% residential / 25% business |
| **136–180** | 50% residential / 50% business |
| **more than 180** | 100% business |

- **Declare before 1 Jul** to land on the first instalment bill; **remove the listing before 30 Jun** to stay residential
- Supreme Court upheld the original 2017/18–2018/19 APTR on **12 May 2023** ([2023] NZSC 53)

#### Other councils

- Wellington, Christchurch tightening discussions

### Tax on rental

- Marginal income tax on net rental
- BTL interest fully deductible (from 1 Apr 2025)
- Bright-line test on sale
- **GST $60k threshold** (online STR platforms collect for non-registered hosts)
- **Rental loss ring-fencing** — losses cannot offset other income

---

## Section: `--work=<profession>`

### Sources

- **Work and Income (WINZ)**: `https://www.workandincome.govt.nz/`
- **Trade Me Jobs**: `https://www.trademe.co.nz/jobs`
- **Seek.co.nz** — biggest: `https://www.seek.co.nz/`
- **MyJobSpace, JobAve, Indeed.co.nz, LinkedIn NZ**
- **MIQ + Work Visa** for migrants

### Self-employment

- **Sole trader**: IRD + GST (above $60k turnover)
- **Limited company**: Companies Office; min $1 capital
- **Working for Families** tax credits

### Salary benchmarks (2025)

- Median annual gross:
  - Auckland: ~$80,000–$110,000
  - Wellington (govt): ~$85,000–$120,000
  - Christchurch / Hamilton / Tauranga: ~$70,000–$95,000
  - Smaller cities: ~$60,000–$80,000
- **Minimum wage**: **$23.95/hr from 1 Apr 2026** (previously $23.50, +45c) (2026-05-27 verified, source: [MBIE — Minimum wage set for 2026](https://www.mbie.govt.nz/about/news/minimum-wage-set-for-2026))

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **GeoNet** | `https://www.geonet.org.nz` | Earthquake / volcano / tsunami real-time |
| **GNS Science / Earth Sciences NZ** | `https://www.gns.cri.nz` | National Seismic Hazard Model (2022 update raised hazard ~50% nationally) |
| **Natural Hazards Commission Toka Tū Ake** (formerly EQC) | `https://www.naturalhazards.govt.nz` | NHCover up to **$300,000 +GST** residential building cap |
| **NIWA** | `https://www.niwa.co.nz` | Climate, flood, drought |
| **Council hazard registers** | per council | Auckland Hazard Viewer, Wellington Hazards Mapper |

### Specific risks

#### Earthquake — EXTREME

- **NZ sits on Pacific Ring of Fire / plate boundary**
- **National Seismic Hazard Model 2022**: raised hazard estimates ~50% nationally
- **Historical major events**:
  - **Christchurch (Canterbury) 2010-11** (M7.1 + M6.3 — 185 dead, ~$40B damage est. — verify cost with Treasury / Toka Tū Ake)
  - **Kaikoura 2016** (M7.8 — fault rupture, tsunami, port damage)
  - **Hawkes Bay 1931** (M7.8 — 256 dead)
- **Wellington fault**: high probability of major event in coming decades
- **Auckland**: lower risk (volcanic field replaces tectonic faults)
- **NHCover** mandatory natural-disaster insurance via property insurance — covers up to **$300,000 +GST** building damage

#### Volcanic

- **Taupo Volcanic Zone** (largest known supervolcano)
- **Mount Ruapehu**: active stratovolcano (Whakapapa ski field)
- **Auckland Volcanic Field**: 53 cones; Rangitoto last erupted ~600 yrs ago
- **Whakaari/White Island 2019** eruption (22 dead — tourists)

#### Tsunami

- Pacific Ocean origin; Kaikoura 2016 generated local tsunami
- Risk: East Coast, Cook Strait, Bay of Plenty
- Council tsunami evacuation zones mandatory

#### Flood + landslip

- Auckland 2023 floods (state of emergency, ~$2B insured losses est. — verify with ICNZ)
- Cyclone Gabrielle 2023 (Hawkes Bay, Tairāwhiti)
- Sub-tropical climate: heavy rainfall events increasing
- Steep terrain landslip risk (Kaikoura, Wellington)

#### Coastal erosion + sea-level rise

- +20-80 cm by 2100 (NIWA SLR)
- Coastal Hazards Susceptibility (per council mapping)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | Lead paint, lead pipes |
| **1920s–1980s** | Asbestos very common (banned 1990) |
| **1990s–2000s** | **Leaky homes crisis** — monolithic-clad homes pre-2003: water ingress + rot (~$11B+ damage est. — verify with PwC / Dept of Building & Housing estimate) |
| **Post-2003 H1** | Tightened weathertightness rules |
| **Post-2018** | Updated insulation + Healthy Homes |
| **Cross-lease titles** | ~10% Auckland — shared ownership complications |

### Mandatory at sale

| Document | Notes |
|---|---|
| **LIM (Land Information Memorandum)** | From council; ~$300-500; mandatory in practice |
| **Project Information Memorandum (PIM)** | For consents (build/extension) |
| **Body Corporate disclosure** | Unit title only |
| **Vendor warranty re weathertightness** | Leaky-building disclosure expected |
| **Healthy Homes Compliance Statement** | If letting out |

### Climate change projections

- **+1.5–4.0°C** by 2100
- **Sea-level rise**: +20–80 cm by 2100
- **Heavy rainfall**: ~+20-30% est. by 2100 (verify against NIWA / MfE projection scenario)
- **Drought**: increasing eastern regions
- **Insurance premiums rising** for high-risk zones

---

## Section: `--mains`

### Sources

- **Watercare** (Auckland): `https://www.watercare.co.nz/`
- **Wellington Water**: `https://www.wellingtonwater.co.nz/`
- **Christchurch City Council Water**, **DCC Water (Dunedin)**
- Universal in cities; rural may have rainwater tanks + septic

### Costs

| Scenario | Cost (NZD) |
|---|---:|
| Mains connection | $5,000–$15,000 |
| Septic upgrade | $15,000–$30,000 |
| Rainwater tank | $3,000–$8,000 |
| Bored well | $10,000–$25,000 |

---

## Cost benchmarks (NZ 2026)

| Work | Cost (NZD) |
|---|---:|
| Building report | $500–$1,000 |
| LIM report | $300–$500 |
| Solicitor / conveyancer | $1,500–$3,000 |
| Body Corporate disclosure | $300–$700 |
| **Total transaction cost (buyer)** | **~$3,000–$5,000 (lowest in OECD)** |
| Roof restoration | $5,000–$15,000 |
| Earthquake strengthening (older builds) | $30,000–$200,000+ |
| Asbestos abatement | $5,000–$30,000 |
| Leaky home remediation | $100,000–$500,000+ |
| Insulation upgrade | $5,000–$15,000 |
| Heat pump | $2,500–$5,000 |
| Solar PV (5kW) | $10,000–$15,000 |

## Active fiscal incentives (2025-2026)

- **First Home Loan**: 5% deposit via Kāinga Ora
- **First Home Grant**: $5-10k for FHB (KiwiBuild + Kāinga Ora)
- **KiwiSaver First Home Withdrawal**: full balance for first home
- **Healthy Homes incentives**: insulation grants
- **Warmer Kiwi Homes**: Energy retrofit subsidy

## Common listing platforms

- **Trade Me Property** — biggest
- **realestate.co.nz** — industry-owned
- **OneRoof** (NZ Herald)
- **Homes.co.nz** — sold-prices

## Caveats unique to NZ

- **NO STAMP DUTY** (abolished 1999) — UNIQUE in OECD; transaction cost ~$3-5k
- **NO general CGT** but **bright-line test 2 years** (from 1 Jul 2024) — sells within 2 years = ordinary income
- **Foreign-buyer ban (2018)** — AU + SG resident citizens exempt; new builds partly exempt
- **NHCover (Toka Tū Ake)**: mandatory $300k+GST natural-disaster insurance via property insurance — UNIQUE coverage
- **Earthquake risk extreme** — NSHM 2022 raised hazard ~50%; Christchurch + Wellington high
- **Wellington ~-26% est.** from Oct 2021 peak (hit hardest by recent rate cycle — verify against QV House Price Index)
- **Cross-lease titles** (~10% Auckland) — shared ownership of section, flat plan; clunky for renovations
- **Leaky homes crisis** (1990s-early 2000s) — monolithic cladding pre-2003 vulnerable
- **Healthy Homes Standards** mandatory for rentals
- **Interest deductibility 100% restored 1 Apr 2025** for residential investment
- **GST on STR via platforms** since 1 Apr 2024
- **Cyclone Gabrielle 2023** + Auckland floods 2023 — major recent reform drivers
- **NHCover building cap $300k+GST** — high-value houses need top-up insurance
- **LIM report ~$300-500** mandatory in practice
- **Māori land** (Te Ture Whenua Māori Act 1993) — unique constraints, often 99-year leases
- **Rating valuations** (CV/LV) every 3 years per council; not market value
- **Rental loss ring-fencing** — cannot offset other income

## Reddit / forum sources

- **r/PersonalFinanceNZ** — biggest community
- **r/auckland**, **r/wellington**, **r/chch**
- **r/newzealand**
- **PropertyTalk forums**
- **Stuff Property** (news)

## Verification authorities

| Authority | When to call |
|---|---|
| **LINZ Toitū Te Whenua** | Title verification |
| **Local council** | LIM report, rates, zoning |
| **GNS Science / GeoNet** | Hazard zone status |
| **Toka Tū Ake (NHC)** | Natural-disaster cover specifics |
| **REINZ** | Market data |
| **Body Corporate** | If unit title |
| **Solicitor** (mandatory) | Final closing |

## Source URL templates

| Source | URL pattern |
|---|---|
| LINZ Public Land Record Search | `https://lrs.linz.govt.nz/search/` |
| Trade Me Property | `https://www.trademe.co.nz/property/` |
| realestate.co.nz | `https://www.realestate.co.nz/` |
| REINZ HPI | `https://www.reinz.co.nz/Web/Web/Data-and-Products/REINZ-HPI-Report.aspx` |
| QV / Cotality NZ | `https://www.qv.co.nz/price-index/` |
| GeoNet | `https://www.geonet.org.nz/` |
| GNS Science NSHM | `https://www.gns.cri.nz/` |
| Toka Tū Ake (Natural Hazards Commission) | `https://www.naturalhazards.govt.nz/` |
| NIWA | `https://www.niwa.co.nz/` |
| NZTA Traffic Counts | `https://www.nzta.govt.nz/resources/state-highway-traffic-volumes` |
| IRD (**Te Tari Taake**) | `https://www.ird.govt.nz/` (2026-05-27 verified bilingual masthead) |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing (REINZ HPI + QV + Trade Me), traffic, tax (rates + bright-line + GST + zero stamp duty), rental (RTA + Healthy Homes), work, risks (NSHM 2022 + Cyclone Gabrielle 2023 + leaky homes), mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for REINZ + QV March 2026 medians + bright-line 2-yr from 1 Jul 2024 + interest deductibility 100% from 1 Apr 2025 + foreign-buyer ban (AU+SG exempt) + NHCover $300k+GST cap + STR GST collection from 1 Apr 2024; MEDIUM for council rate forecasts (frozen in some councils 2024-2025).
**Last verified**: 2026-08-07 (Auckland APTR suspension since 2020 + graduated general-rates/CATTR STR business uplift re-verified against Auckland Council; other sections unchanged). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).

## Extension TODOs

- [ ] Per-council rates table
- [ ] Per-council STR rules detail
- [ ] Cross-lease conversion to fee simple flow
- [ ] Leaky-home identification + remediation decision tree
- [ ] Earthquake strengthening NSEC rating verification
- [ ] Bright-line transition rules per acquisition date
- [ ] Healthy Homes Standards compliance checklist
- [ ] Māori land (Te Ture Whenua) constraint check
- [ ] NHCover top-up insurance for high-value homes
- [ ] AU/SG resident exemption verification flow
