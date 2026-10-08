# United States 🇺🇸 — Property Due-Diligence Playbook (Federal Overview)

ISO2: `us`. Status: ✅ Federal overview populated (researched 2026-05).

> ⚠️ **Federal overview only.** The US has no national cadastre, no national property tax, no national transfer tax, and no national mandatory disclosure regime beyond the federal Lead-Based Paint Disclosure (Title X 1992). State property tax, transfer / recording / closing fees, conveyance procedure, mandatory disclosures, zoning, landlord-tenant law, short-term-rental rules, and homestead exemptions all vary materially by state, county, and municipality. This playbook covers **federal-level constants** + the **verification path** to find state/county-specific resources. Per-state playbooks (when added) inherit federal here and overlay state specifics.

## Country profile

- **ZIP code**: 5-digit (`NNNNN`) optionally extended `NNNNN-NNNN` (ZIP+4). Issued by USPS; not a legal admin boundary.
- **Admin levels**: Federal → 50 states + DC + 5 territories → 3,143 counties (or parishes/boroughs) → ~19,500 incorporated municipalities + ~16,000 townships. Census-defined places (CDPs) are statistical, not legal.
- **Currency**: USD (US dollar)
- **Languages**: No federal official language; English de facto. Spanish substantial in border / urban areas. State-level: HI recognises Hawaiian; many states recognise English.
- **Cadastre**: ❌ **No national cadastre.** Property records are maintained by **county recorders / clerks / registries of deeds** (~3,143 separate offices). Title is established through **title insurance + abstract / title search** (recording-act system), not a unified central register. A handful of counties (~12 nationwide, mostly Hawaii, Minnesota, Massachusetts, Illinois, Ohio) operate **Torrens title** systems for some parcels (residual; not expanding) (source: [American Bar Association Real Property](https://www.americanbar.org/groups/real_property_trust_estate/)).
- **Identifier scheme**: **Assessor's Parcel Number (APN)** or **Parcel Identification Number (PIN)** — county-specific format (e.g., `123-456-789` in CA; `1234567890` in IL). Always paired with county + state. Some states use **Property Index Number (PIN)** or **Tax Map Number (TMN)** instead.
- **Federal foreign-buyer regime**:
  - **No nation-wide ban** on foreign individual ownership of residential real estate.
  - **CFIUS jurisdiction** under [31 CFR Part 802](https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII/part-802) covers foreign-person purchases / leases within **1 mile** of Part 1 military installations and within **100 miles** of Part 2 installations. Final rule [89 FR 88128 (7 Nov 2024)](https://www.federalregister.gov/documents/2024/11/07/2024-25773/definition-of-military-installation-and-the-list-of-military-installations-in-the-regulations) added **59 new sites** to the appendix and moved eight from part 1 to part 2, effective **9 Dec 2024** (2024 data, source 89 FR 88128 — [govinfo PDF](https://www.govinfo.gov/content/pkg/FR-2024-11-07/pdf/2024-25773.pdf)).
  - **State-level restrictions multiplying** (see Caveats § state foreign-buyer laws below).
- **AFIDA (Agricultural Foreign Investment Disclosure Act)**: 7 USC 3501 — foreign acquirers of agricultural land must report to USDA on Form FSA-153 within 90 days. Civil penalty up to 25 % of fair-market value if missed.

## Section: `--price`

### Federal aggregate price sources (national / metro level)

| Source | Coverage | URL |
|---|---|---|
| **FHFA House Price Index (HPI)** | National + state + MSA + ZIP3; repeat-sales | `https://www.fhfa.gov/data/hpi` |
| **S&P CoreLogic Case-Shiller HPI** | National + 20 metro composite | `https://www.spglobal.com/spdji/en/index-family/indicators/sp-corelogic-case-shiller/` |
| **NAR Existing Home Sales** | National median + 4 regions, monthly | `https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales` |
| **U.S. Census Median Sales Price of New Homes** | New-construction only, monthly | `https://www.census.gov/construction/nrs/index.html` |
| **HUD User – State of the Cities** | MSA-level housing market data | `https://www.huduser.gov/portal/datasets/socds.html` |
| **Zillow Research / ZHVI** | ZIP-level home value index | `https://www.zillow.com/research/data/` |
| **Redfin Data Center** | Metro / ZIP / neighborhood, weekly | `https://www.redfin.com/news/data-center/` |
| **Realtor.com Research** | Metro listing data | `https://www.realtor.com/research/data/` |

### National benchmarks (current)

- **NAR existing-home median sale price**: **$429,300 (May 2026)** — highest price ever recorded for the month of May; +1.3 % YoY (vs $423,700 May 2025), 35th consecutive month of YoY increases; SAAR 4.17M (+3.2 % YoY); 4.5-month inventory (source: [NAR May 2026 release](https://www.nar.realtor/newsroom/nar-existing-home-sales-report-shows-3-2-increase-in-may))
- **FHFA HPI**: +2.0 % YoY (Apr 2025 → Apr 2026); −0.1 % MoM Apr 2026 (source: [FHFA HPI Apr 2026, pub. 30 Jun 2026](https://www.fhfa.gov/news/news-release/fhfa-house-price-index-down-0.1-percent-in-april-up-2.0-percent-from-last-year)) — next release 28 Jul 2026 (May data)
- **NAR 2026 forecast**: downgraded amid lackluster spring 2026 buying season — verify current with NAR

### Local price discovery — verification path

There is no national MLS public price search. To get a parcel-level / neighborhood comparable:

1. **County assessor website** — search by APN or address; returns **assessed value** (≠ market value in 90 % of states; assessment ratios + Prop-13-style caps vary)
2. **County recorder / register of deeds** — search recent deeds for sale-price stamps (where transfer tax exists) or full purchase price (where required)
3. **MLS comparables** — request through a NAR-affiliated broker (MLS data is **NOT public**; access gated by license + dues)
4. **Zillow / Redfin / Realtor.com** — listing platform medians; treat as **secondary** (seller-controlled, often outdated, ZHVI is modeled estimate not transaction)
5. **States with non-disclosure**: AK, ID, KS, LA, MS, MO, MT, NM, ND, TX, UT, WY — sale prices are **not publicly recorded**; rely on broker-provided MLS comps only

### Compute

1. List price ÷ surface (sqft) = price/sqft (US convention; multiply by 10.764 for €/m²)
2. Compare to ZHVI for the same ZIP (Zillow) and Redfin median for the metro
3. Cross-check assessed value (county assessor) — **assessed ≠ market** (typical assessment ratio 25–100 % varies by state; CA Prop-13 freezes at last-sale value + 2 % cap)
4. **Trap**: listing surface often includes garage / basement / unfinished sqft inconsistently — verify via county appraisal record or independent appraisal
5. **Trap**: HOA / condo-fee separately disclosed, sometimes after offer — request HOA disclosure package before contract

**Confidence**: HIGH for federal aggregate sources (FHFA, NAR, Census = primary federal). MEDIUM for local price discovery (depends on state disclosure regime + MLS access).

---

## Section: `--traffic`

### Federal source

- **FHWA Traffic Volume Trends (monthly report)**: `https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm`
  - 2024 cumulative US travel: **3,279.1 billion vehicle-miles** (+1.0 % YoY) (source: [FHWA TVT Dec 2024](https://www.fhwa.dot.gov/policyinformation/travel_monitoring/24dectvt/))
  - Apr 2025: **277.3 billion VMT** (+1.5 % YoY) (source: [FHWA TVT Apr 2025](https://www.fhwa.dot.gov/policyinformation/travel_monitoring/25aprtvt/))
  - Underlying data from ~5,000 continuous count stations (state DOTs + FHWA TMAS)
- **FHWA Highway Statistics**: `https://www.fhwa.dot.gov/policyinformation/statistics.cfm` — annual; AADT by route, state-level
- **National Highway System (NHS)** classification: `https://www.fhwa.dot.gov/planning/national_highway_system/`

### State / parcel-level traffic

- **State DOT traffic-count viewers** (one per state — search "<state> DOT traffic count map"):
  - Examples: CA Caltrans Traffic Census, FL DOT Florida Traffic Online, NY DOT Traffic Data Viewer, TX DOT Statewide Traffic Map
  - Returns AADT (annual average daily traffic) per segment, often updated 1–3 yr lag
- **MPO (Metropolitan Planning Organization)** counts for urbanized areas
- **OSM `highway` class** as coarse fallback

### Verdict bands (US AADT, two-way unless noted)

- 🟢 < 1,000 AADT (rural local / county road)
- 🟡 1,000–5,000 (collector, rural minor arterial)
- 🟠 5,000–25,000 (urban arterial, suburban collector)
- 🔴 > 25,000 AADT (interstate, major arterial, freeway feeder)

**Confidence**: HIGH for FHWA federal aggregate. State DOT data quality varies; date-stamp every AADT figure (often 2–3 yr old at publication).

---

## Section: `--tax`

> ⚠️ **State property tax + state transfer tax + recording fees are SET AT STATE / COUNTY / MUNICIPAL LEVEL.** This section covers **federal tax constants only** — the income-tax side that touches real estate (deductions, exclusions, withholding, estate tax). For state property tax: use the verification path at the bottom of this section.

### Federal income tax — homeowner constants (2025-2026)

| Provision | 2025-2026 status | Source |
|---|---|---|
| **§ 121 capital gains exclusion (primary residence)** | **$250,000 single / $500,000 MFJ** — must own + use as principal residence ≥ 2 of last 5 yrs; usable once per 2 yrs. **NOT indexed to inflation since 1997.** | [26 USC 121](https://www.law.cornell.edu/uscode/text/26/121); [IRS Pub 523 (2025)](https://www.irs.gov/publications/p523) |
| **Mortgage interest deduction (MID) cap** | **$750,000 acquisition debt** for loans originated after 15 Dec 2017. **Made permanent by OBBBA (PL 119-21, 4 Jul 2025)** — sunset to $1M was eliminated. | [IRS One Big Beautiful Bill Provisions](https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions) |
| **SALT (state & local tax) deduction cap** | **$40,000 (2025); $40,400 (2026, indexed +1 %/yr through 2029)** — raised from $10,000 by OBBBA; phases down at 30¢ per $ of MAGI over $500,000 (threshold also indexed — $505,000 for 2026 per Rev. Proc. 2025-32 as reported; MFS gets half: $20,000 cap / $250,000 threshold / $5,000 floor); floor $10,000. **Reverts to $10,000 in 2030.** | [IRS OBBBA Provisions](https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions); [IRS 2026 inflation adjustments](https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2026-including-amendments-from-the-one-big-beautiful-bill) |
| **§ 25C Energy Efficient Home Improvement Credit** | Up to $1,200/yr (or $2,000 for heat pumps) — **TERMINATED for property placed in service after 31 Dec 2025** by OBBBA | [IRS FAQs OBBB §§ 25C 25D etc.](https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb) |
| **§ 25D Residential Clean Energy Credit (solar / geothermal etc.)** | 30 % — **TERMINATED for expenditures after 31 Dec 2025** by OBBBA | (same source) |
| **§ 45L New Energy Efficient Home Credit** | Builder-side, modified by OBBBA — verify current | [IRS OBBBA Provisions](https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions) |
| **Property tax (federal deduction)** | Itemize; subject to SALT cap above | (same) |

### FIRPTA — withholding on foreign-seller dispositions

**Foreign Investment in Real Property Tax Act**, codified at [26 USC 1445](https://www.law.cornell.edu/uscode/text/26/1445); IRS overview: [FIRPTA withholding](https://www.irs.gov/individuals/international-taxpayers/firpta-withholding):

| Scenario | Rate | Source |
|---|---:|---|
| Standard foreign-seller disposition | **15 %** of gross amount realized | 26 USC 1445(a); PATH Act 2015 increased from 10 % |
| Buyer-occupied residence ≤ $300,000 | 0 % (exempt) | 26 USC 1445(b)(5) |
| Buyer-occupied residence $300,001–$1,000,000 | **10 %** | (same) |
| Buyer-occupied residence > $1,000,000 | 15 % | (default) |

- Buyer is the **withholding agent** (personally liable if not remitted via IRS Form 8288 + 8288-A within 20 days of closing).
- Foreign seller files Form 1040-NR after year-end; actual tax = capital-gains rate × gain; refund typical for long-held appreciated property.
- "Foreign person" = anyone not a US citizen / resident alien (substantial-presence test) / domestic entity.

### Federal estate / gift tax — non-domiciliary alien (huge exposure)

| Person | 2026 estate-tax exemption | 2026 gift-tax exemption |
|---|---:|---:|
| **US citizen / domiciliary** | **$15,000,000** per person (raised by OBBBA from prior ~$13.99M; effective 1 Jan 2026) | $15M (unified credit) |
| **Non-domiciliary alien (NRA)** | **$60,000** — **NOT indexed since 1976** | **$0 (none)** for US-situs property; $19,000/yr present-interest exclusion to non-spouse done |

Sources: [IRS One Big Beautiful Bill Provisions](https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions); [2026 Estate & Gift Tax Chart for NRAs (Skatoff law)](https://skatoff.com/florida-estate-planning-attorney/updated-for-2026-estate-and-gift-tax-chart-for-non-us-persons-greencard-holders-and-nras/).

**Critical**: A foreign individual buying a $1M US property in their personal name dies → estate tax computed on $1M − $60,000 = $940,000 at graduated rates (top 40 %). **Mitigation**: hold via foreign blocker corporation, foreign trust, or use a US-Country estate-tax treaty (15 treaties exist — UK, FR, DE, DK, AT, AU, CA, FI, GR, IE, IT, JP, NL, NO, ZA). Consult cross-border tax counsel before closing.

### State property tax — find your county rate

There is no national rate. Effective rate range nationally (2025): **0.33 % (HI) to 1.84 % (IL)** — source [ATTOM 2025 Property Tax Report](https://www.attomdata.com/news/market-trends/home-sales-prices/2025-annual-tax-report/).

Top 5 lowest effective rates 2025: HI 0.33 %, ID 0.39 %, WY 0.40 %, AZ 0.43 %, AL 0.43 %.
Top 5 highest: IL 1.84 %, NJ 1.58 %, VT 1.40 %, CT 1.36 %, OH 1.32 %.

**National average effective rate 2025: 0.90 %** (up from 0.86 % in 2024).

To find your specific rate:

1. **State Department of Revenue (DOR) / Tax Commission** — search "<state> property tax rate" — most publish median + per-county rates
2. **County assessor** — APN-level assessed value + tax rate (mill rate) lookup
3. **County treasurer / tax collector** — actual prior-year tax bill (request from seller)
4. **NAR Field Guide to Property Taxes**: `https://www.nar.realtor/property-taxes`
5. **Tax Foundation per-state property-tax data**: `https://taxfoundation.org/data/all/state/property-taxes-by-state-county/`

### State / county transfer + recording fees — find by state

Federal transfer tax: **none.** State + county + municipal vary widely:

- **No real-estate transfer tax**: AK, ID, IN, KS, LA, MS, MO, MT, NM, ND, OR (most counties), TX, UT, WY (12 states + DC outliers — verify each)
- **Highest combined**: DC ~2.2 %, DE 4 %, NY (NYC mansion tax stacks to 4.65 %+), CT 1.25–2.75 %, NJ 1 %+
- **Recording fees**: typically $20–$300 per document, county-set
- Verification: state DOR + county recorder fee schedule + use a settlement-agent (escrow officer / closing attorney) estimate before signing

### Future federal tax-policy uncertainty (watch items)

- **OBBBA (4 Jul 2025) reshaped landscape**: SALT cap raised to $40k (sunset 2030); MID $750k made permanent; 25C/25D terminated 31 Dec 2025; estate exemption raised to $15M (2026); QBI made permanent. Verify current status as of date of read — Treasury / IRS continues releasing implementing guidance through 2026.
- **NRA $60k estate exemption** has not moved since 1976 — political risk: low (no constituency).
- Carry-over CFIUS expansion (Nov 2024 final rule) likely to grow further — watch for 2026 supplemental rule on energy-grid proximity.

⚠️ Verification: request seller's most recent **county property tax bill** + **HOA assessment statement** (if applicable) before signing. Federal income-tax impact requires CPA review.

**Confidence**: HIGH for federal income-tax provisions (IRS primary). HIGH for FIRPTA (statute + IRS guidance). MEDIUM for state-tax range (ATTOM 2025 secondary aggregator; verify current via state DOR).

---

## Section: `--rental`

### Federal income-tax framework

| Activity | Reporting | Source |
|---|---|---|
| **Long-term residential rental** (≥ 30-day average stays, no significant services) | **Schedule E** (Form 1040), Part I — passive activity | [IRS Pub 527 (2025)](https://www.irs.gov/publications/p527) |
| **Short-term rental ≤ 7-day average stay** (Airbnb / VRBO typical) | **Schedule E IF rental activity** OR **Schedule C IF substantial services** (housekeeping mid-stay, meals, concierge) | [IRS Pub 925 (2025)](https://www.irs.gov/publications/p925) |
| **STR with material participation** | Loss can be **non-passive** if ≥ 1 of 7 material-participation tests met (most common: > 100 hrs AND more than anyone else; or > 500 hrs) | [Form 8582 instructions (2025)](https://www.irs.gov/instructions/i8582) |
| **STR with substantial services + material participation** | **Schedule C**; subject to 15.3 % SE tax on net | [Sched C Instructions (2025)](https://www.irs.gov/businesses/small-businesses-self-employed/self-employment-tax-social-security-and-medicare-taxes) |

### "Short-term rental loophole" (IRS-recognised)

- Average customer use ≤ 7 days = **NOT a rental activity** under § 469
- If owner materially participates → losses are **non-passive** → can offset W-2 / ordinary income
- Frequently combined with **cost segregation + bonus depreciation** for large year-1 deductions
- **Documentation requirement**: contemporaneous time logs; courts reject "standardized allocations that ignore actual facts" (source: [Mitchell Tax Law analysis](https://irstaxtrouble.com/short-term-vacation-rentals-and-material-participation/))

### Passive activity loss (PAL) rules

- **§ 469**: passive losses deductible only against passive income
- **$25,000 special allowance**: rental real-estate losses for active participants with MAGI ≤ $100,000 (phases out by $150,000)
- **Real estate professional** (§ 469(c)(7)): > 750 hrs + > 50 % personal-services time in real-estate trade → rental losses non-passive

### Federal short-term-rental regulation

- **No federal STR ban or registry.** STR regulation is state / county / municipal.
- **CDC / federal eviction moratorium expired** August 2021 (post-CARES Act); no current federal moratorium.
- **Lead Disclosure Rule** ([24 CFR Part 35 Subpart A](https://www.ecfr.gov/current/title-24/subtitle-A/part-35/subpart-A) + [40 CFR 745](https://www.epa.gov/lead/lead-based-paint-disclosure-rule-section-1018-title-x)) applies to **target housing built before 1978** — sellers + lessors must disclose known LBP, provide EPA pamphlet, give 10-day inspection opportunity. Enforced jointly by EPA + HUD.
- **Fair Housing Act** (42 USC 3601-3619) prohibits discrimination by race, color, religion, sex, national origin, disability, familial status — applies to most rental listings.
- **ADA** Title III applies to short-term lodging "places of public accommodation" with > 5 rooms — most single-family STRs exempt; verify if scaled.

### Verification path for state / city STR rules

1. **City clerk / planning department**: STR registration / permit required?
2. **State DOR / hotel-occupancy-tax authority**: lodging tax registration?
3. **HOA / condo bylaws**: many prohibit < 30-day rentals
4. **Zoning code**: residential-only vs mixed-use; some cities (e.g., NYC, NOLA, SF, Boston) have hard caps + primary-residence requirements

### Strategic notes

- **Tax benefit asymmetry**: STR with material participation > LTR for high-income investors; LTR > STR for passive investors / retirees
- **Regulatory risk** is highest in major coastal / tourist cities (NYC, LA, SF, Boston, NOLA, Miami, Honolulu, Seattle) — restrictive permit caps; STR market values discounted vs LTR comps
- **Rural / suburban**: usually permissive but verify HOA + zoning

**Confidence**: HIGH for federal tax framework (IRS primary). MEDIUM for state-by-state STR rules (verification required per locality).

---

## Section: `--work=<profession>`

### Federal job platforms

| Platform | Best for |
|---|---|
| **USAJOBS** (`https://www.usajobs.gov/`) | All federal civilian positions — official portal |
| **Indeed** (`https://www.indeed.com/`) | Largest aggregator (private + public) |
| **LinkedIn Jobs** | Mid-senior corporate, professional services |
| **ZipRecruiter**, **Glassdoor**, **Monster** | General private-sector |
| **Handshake** | Recent grads + university recruiting |
| **Dice** | Tech / engineering specifically |
| **Idealist** | Nonprofit |

### State / local employment

- **State workforce agency** (varies by state; e.g., CA EDD, NY DOL, TX TWC) — UI claims, state job postings
- **Bureau of Labor Statistics OEWS** (`https://www.bls.gov/oes/`) — wage data by occupation × MSA
- **BLS Occupational Outlook Handbook** (`https://www.bls.gov/ooh/`) — projection + median wage per occupation

### Immigration / work-authorization landscape (federal)

| Visa | Use | Cap |
|---|---|---|
| **H-1B** | Specialty occupation; requires bachelor's + sponsoring employer | 65,000 + 20,000 advanced-degree (annual; lottery) |
| **L-1A/L-1B** | Intracompany transferee (manager / specialized knowledge) | None |
| **E-2 Treaty Investor** | Substantial investment from treaty country | None; 50+ treaty countries |
| **EB-5 Immigrant Investor** | $800,000 (TEA) / $1,050,000 (standard) investment + 10 jobs (Regional Center vs Direct) — 2022 EB-5 RIA thresholds, inflation-adjusted; verify current with USCIS | ~10,000/yr (split per country) |
| **O-1** | Extraordinary ability | None |
| **TN (USMCA)** | Canadian / Mexican professional, listed occupations | None |

Source: [USCIS Visa Categories](https://www.uscis.gov/working-in-the-united-states). Real-estate purchase **does not** create immigration status; there is no "golden visa" by property purchase (EB-5 is investment-into-a-business, not house).

### Self-employment regimes (federal)

- **Sole proprietor**: report on **Schedule C** (Form 1040); pay **SE tax 15.3 %** (12.4 % SS up to $184,500 in 2026 + 2.9 % Medicare uncapped) on 92.35 % of net earnings ([Schedule SE 2025](https://ourtaxpartner.com/schedule-se-2025-guide/))
- **Single-member LLC**: default disregarded entity → Schedule C; can elect S-Corp via Form 2553 (potentially reduces SE tax via reasonable-salary structure)
- **S-Corporation / C-Corporation**: separate entity; payroll required for owner-employees
- **Retirement plans available to self-employed**:
  - **SEP-IRA**: contribute up to 25 % of net SE earnings, max **$70,000 (2025) / $72,000 (2026)** ([Fidelity SEP-IRA limits](https://www.fidelity.com/learning-center/smart-money/sep-ira-contribution-limits))
  - **Solo 401(k)**: 2026 employee deferral $24,000 + employer 25 % of compensation; combined cap matches SEP-IRA
  - **SIMPLE IRA**: lower contribution; suits very small business with employees
- **State licensure** for many professions (real-estate broker, contractor, attorney, doctor, accountant) varies — verify with **state licensing board**

### Catchment heuristics

- **Within 30 min commute** of an MSA principal city → strong employment market
- **Within 60 min** of an MSA → typical suburban / exurban catchment
- **> 90 min** from any MSA → rural; remote-work or self-employment dominant
- **Right-to-work states** (~28 as of 2026 — verify current with NCSL) vs union-friendly: affects unionised trades

**Confidence**: HIGH for federal tax / SE / visa frameworks (IRS + USCIS primary). MEDIUM for state-licensure specifics (verification per state required).

---

## Section: `--risks`

### Federal risk-mapping primary sources

| Hazard | Source | URL |
|---|---|---|
| **Flood** | **FEMA Flood Map Service Center** (FIRMs / NFHL) | `https://msc.fema.gov/portal/home` |
| **Flood insurance pricing** | **NFIP Risk Rating 2.0** (FEMA) | `https://www.fema.gov/flood-insurance/risk-rating` |
| **Earthquake** | **USGS National Seismic Hazard Map (2023 update)** | `https://www.usgs.gov/programs/earthquake-hazards/science/2023-50-state-national-seismic-hazard-model` |
| **Wildfire (community exposure)** | **USFS Fireshed Registry** + **Wildfire Risk to Communities** | `https://research.fs.usda.gov/rmrs/projects/firesheds` + `https://wildfirerisk.org/` |
| **Hurricane** | **NOAA HURDAT2 / Atlantic Best Track** + **National Hurricane Center** | `https://www.nhc.noaa.gov/data/hurdat/` + `https://www.nhc.noaa.gov/` |
| **Tornado** | **NOAA Storm Prediction Center** climatology | `https://www.spc.noaa.gov/wcm/` |
| **Radon** | **EPA Map of Radon Zones** (1993; state supplementals) | `https://www.epa.gov/radon/epa-map-radon-zones` |
| **Lead-based paint** | **EPA / HUD Title X disclosure** (pre-1978) | `https://www.epa.gov/lead` |
| **Asbestos** | **EPA / OSHA** rules; pre-1980s common | `https://www.epa.gov/asbestos` |
| **Climate projections** | **NCA5 (Fifth National Climate Assessment, Nov 2023)** | `https://repository.library.noaa.gov/view/noaa/61592` |
| **Air quality** | **EPA AirNow** / NAAQS attainment | `https://www.airnow.gov/` |

> **Don't rely on listing-portal climate badges.** From late 2025 Zillow de-emphasised the First Street climate-risk scores on its listings after a California Regional MLS accuracy dispute (numerical scores off the listing page, module links out to First Street, map layer kept — [Zillow explainer](https://www.zillow.com/news/climate-risk-product-update/), byline 6 Dec 2025 as read via proxy on 17 Sep 2026 — the change was first reported in Nov 2025; [CNN 2 Dec 2025](https://www.cnn.com/2025/12/02/climate/zillow-climate-data-extreme-weather-first-street-redfin); still the case on 17 Sep 2026). Redfin still displays First Street data; Realtor.com and Homes.com not verified at listing level. MSCI completed its acquisition of First Street on 3 Aug 2026 and RiskFactor.com now redirects to [firststreet.org](https://firststreet.org/) behind an MSCI terms-of-use gate, with a paid tier above the free reports — verify free access before relying on it. Pull hazard data from the primary government sources above plus First Street and the state NHD report directly, not from a portal badge.

### Flood — FEMA + NFIP framework

- **FIRM (Flood Insurance Rate Map)** zones:
  - **A / AE / AH / AO / AR / A99**: 1 %-annual-chance flood zone (100-yr); mortgage requires NFIP if federally backed
  - **V / VE**: coastal high-hazard with wave action
  - **X (shaded)**: 0.2 %-annual-chance (500-yr)
  - **X (unshaded)**: minimal hazard
  - **D**: undetermined
- **NFIP Risk Rating 2.0**: **rolled out 1 Oct 2021** for new policies; existing policies transitioned **1 Apr 2022**; **fully implemented 1 Apr 2023**. Pricing now per-property based on multiple factors (replacement cost, flood frequency, distance to source) — replaces flat-zone pricing. (Source: [FEMA NFIP Risk Rating 2.0 fact sheet Apr 2025](https://www.fema.gov/sites/default/files/documents/fema_rr-2.0_04-2025.pdf))
- **Verification path**:
  1. FEMA Flood Map Service Center → enter address → download FIRMette
  2. Order **Elevation Certificate** if property is in A / V zone (lender will require)
  3. Get NFIP quote OR private flood insurance quote (Wright, Neptune, FloodFlash, Lloyd's etc.)
  4. State CRS (Community Rating System) discount may apply

### Earthquake — USGS NSHM

- **2023 50-state update** to National Seismic Hazard Model published Jan 2024 (source: [USGS NSHM 2023](https://www.usgs.gov/news/national-news-release/new-usgs-map-shows-where-damaging-earthquakes-are-most-likely-occur-us))
- Key finding: **~75 % of US could experience damaging earthquake shaking**. Increased hazard along Atlantic Coast (DC, Philadelphia, NY, Boston) vs prior maps; CA + AK + HI elevated.
- Building-code adoption (IBC / state amendments) drives seismic detailing; pre-1980 unreinforced masonry (URM) is highest residential risk in CA / WA / OR / UT / SC.
- **Earthquake insurance is separate** from standard homeowner's; CEA in California (offered via insurers); private market elsewhere. Deductibles 5–25 % typical.

### Wildfire — Fireshed Registry + WUI

- **Fireshed Registry**: ~250,000-acre accounting units; maps source-of-risk transmission to communities (source: [USFS Fireshed Registry](https://www.fs.usda.gov/rmrs/datasets/fireshed-registry-fireshed-and-project-area-boundaries-continental-united-states); 2024 update uses 2023 FSim outputs representing 2020 conditions)
- **Wildland-Urban Interface (WUI)**: community-level mapping at `https://wildfirerisk.org/`
- Insurance market crisis: CA, OR, CO, NM, TX have seen carrier withdrawals from high-WUI ZIPs since 2022; verify availability before closing — see [California FAIR Plan](https://www.cfpnet.com/) as residual-market backstop
- **Defensible space** required by state law in CA, NV, OR (zone 0 ember-resistant 0–5 ft, zone 1 lean clean & green 5–30 ft, zone 2 reduce fuel 30–100 ft)

### Hurricane — NOAA HURDAT2

- **Atlantic basin**: HURDAT2 covers 1851-present; National Hurricane Center provides probabilistic landfall + storm-surge inundation maps
- **Pacific basin**: separate dataset; affects HI + CA + Pacific territories
- Highest residential risk: FL, LA, TX Gulf Coast, NC Outer Banks, SC Lowcountry — windstorm + storm surge
- **Windstorm insurance** often separately purchased (not in standard HO-3) in coastal counties; state windpools / FAIR plans backstop

### Tornado climatology

- **Tornado Alley** (TX panhandle → OK → KS → NE) + **Dixie Alley** (AR / TN / MS / AL / LA) — highest annual incidence
- ~1,200 tornadoes/yr nationally; EF-rating scale (EF0-EF5)
- Standard HO-3 covers wind / hail incl. tornado; deductibles can be 1–5 % of dwelling

### Radon — EPA

- **Zone 1 (red)**: predicted average indoor > 4 pCi/L (action level) — highest potential
- **Zone 2 (orange)**: 2–4 pCi/L
- **Zone 3 (yellow)**: < 2 pCi/L
- **EPA action level**: 4 pCi/L. Mitigation est. $800–$2,500 (sub-slab depressurization) — verify with a local contractor quote.
- **Map dates from 1993** — county-level only; **EPA strongly recommends testing every home regardless of zone** (source: [EPA Map of Radon Zones](https://www.epa.gov/radon/epa-map-radon-zones))
- High-zone states: PA, OH, IA, ND, MN, KY, TN, WV, NM, CO, MT (much of mountain west + Appalachia + upper Midwest)

### Build-era hazards (US construction history)

| Era | Hazards |
|---|---|
| **Pre-1900** | Knob-and-tube wiring, balloon framing (fire spread), brick foundations, lead service lines, lead paint |
| **1900–1940** | Lead paint, lead pipes, asbestos insulation, knob-and-tube |
| **1940s–1978** | Lead paint (banned for residential 1978), asbestos popcorn ceilings + floor tile + pipe wrap + siding (regulated 1989+) |
| **1978–1995** | **Polybutylene plumbing** (gray flexible PB pipe; class-action 1995; replaced with PEX/copper) |
| **1980s** | **FRT (fire-retardant treated) lumber** roof sheathing — failed widely in southeast; class-action 1990s |
| **1980s–early 1990s** | **EIFS (synthetic stucco)** with no drainage plane → moisture intrusion; reformed 1996+ |
| **1990s–2000s** | LP Inner Seal siding / OSB-based exterior cladding swelling; Chinese drywall (2001-2007 imports → corrosion + odor) |
| **2010s+** | Composite decking flammability (some recalls); spray foam off-gassing if mixed wrong |

### Mandatory federal disclosure (only one)

| Disclosure | Trigger | Authority |
|---|---|---|
| **Lead-Based Paint Disclosure** | Residential "target housing" built **before 1978** | EPA + HUD; [24 CFR 35 Subpart A](https://www.ecfr.gov/current/title-24/subtitle-A/part-35/subpart-A) + [40 CFR 745](https://www.epa.gov/lead/lead-based-paint-disclosure-rule-section-1018-title-x); 10-day risk-assessment opportunity for buyer; EPA pamphlet must be provided |

**Everything else** (asbestos disclosure, radon disclosure, flood disclosure, earthquake disclosure, megan's-law disclosure, mold disclosure, prior-death disclosure, structural defects, latent defects) is **state-specific**. Some states (e.g., CA, TX) have ~20-page Transfer Disclosure Statements; others (e.g., MA caveat-emptor with limited carve-outs) have minimal mandatory disclosure.

**Archetypal state hazard disclosure — California NHD** (verified 2026-05-28): the Natural Hazard Disclosure Statement (NHDS) under [Civ. Code §§ 1103–1103.15](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1103.2.) (statutory form at § 1103.2) obliges seller + agent to disclose whether the parcel sits in any of **6 mapped hazard zones** — 2 seismic (Alquist-Priolo earthquake-fault + seismic-hazard/landslide), 2 fire (state-responsibility-area + very-high fire-hazard-severity), 2 flood (FEMA Special Flood Hazard Area + dam-inundation). All parties sign before close of escrow; a third-party NHD report (RiskFactor/JCP/FANHD-style) typically satisfies it. Many other states have narrower analogues — verify per state.

### Climate to 2050 — NCA5

[Fifth National Climate Assessment (Nov 2023)](https://repository.library.noaa.gov/view/noaa/61592) — congressionally-mandated US Government report, ~500 authors:

- **Temperature**: US warmed ~1.1 °C since 1900; projected +2 °C by 2050 under intermediate scenario (SSP2-4.5), +2.5–3 °C under high (SSP3-7.0)
- **Precipitation**: increasing in NE / Midwest; decreasing in SW
- **Sea level rise**: US-coastal 25–30 cm by 2050 (above 2000 baseline) — varies by region (highest GoM and mid-Atlantic due to subsidence; lowest Alaska due to glacial isostatic rebound)
- **Wildfire**: western US burn area trending up; expected to continue
- **Extreme heat days**: > 100 °F days projected to double in many southern states
- **Drought**: SW (CO River basin) increasingly stressed; chronic drought already documented

### Pre-purchase risk checklist (federal)

1. ☐ FEMA Flood Map (FIRM) for parcel — if A / V → quote NFIP + private
2. ☐ USGS NSHM seismic zone — if high-hazard, confirm code-conforming construction year
3. ☐ Fireshed / WUI lookup — if WUI, verify insurance availability + defensible space compliance
4. ☐ EPA Radon Zone (county) + radon test (regardless of zone)
5. ☐ Pre-1978 → demand federal Lead Disclosure + consider XRF inspection
6. ☐ Pre-1980 → ask about asbestos (popcorn ceilings, pipe wrap, siding); pre-1985 → vermiculite insulation (Zonolite from Libby MT — high-risk asbestos)
7. ☐ 1978-1995 → check for polybutylene plumbing
8. ☐ Coastal → windstorm insurance availability + storm-surge map
9. ☐ State-mandated disclosures (varies — get from listing agent)
10. ☐ Pull title insurance commitment + review for easements / encroachments / boundary disputes

**Confidence**: HIGH for FEMA, USGS, NOAA, EPA federal sources (all primary government). MEDIUM for state mandatory-disclosure overlay (must verify per state).

---

## Section: `--mains`

### Federal regulatory framework

- **Safe Drinking Water Act (SDWA)** (42 USC 300f et seq.) — federal primary drinking-water standards (NPDWRs) set by EPA; **state primacy** for enforcement (49 states + tribes have primacy; only WY + DC do not)
- **Clean Water Act (CWA)** §§ 402 (NPDES wastewater discharge permits) + 404 (wetlands fill — USACE jurisdiction)
- **EPA**: ~152,000 public water systems regulated; private wells (serving < 25 ppl or < 15 connections) **NOT federally regulated** — well water testing is owner responsibility

### Lead and Copper Rule status (2026)

- **Lead and Copper Rule (LCR)** 1991 — original
- **Lead and Copper Rule Revisions (LCRR)** finalized Dec 2021 — required initial Service Line Inventory submission by **16 Oct 2024**
- **Lead and Copper Rule Improvements (LCRI)** finalized **Oct 2024** — mandates **full replacement of all lead service lines within 10 years (by ~2037)**, lowers lead action level to **10 ppb** (down from 15), requires Tier 1 public notification within 24 hrs of exceedance. **Compliance date: 1 Nov 2027.** Sources: [EPA LCRI](https://www.epa.gov/ground-water-and-drinking-water/lead-and-copper-rule-improvements); [BDLaw analysis](https://www.bdlaw.com/publications/epa-issues-final-lead-and-copper-rule-improvements-with-far-reaching-lead-pipe-replacement-mandates/).

### Wetlands / Section 404

- **Sackett v. EPA (May 2023)** narrowed CWA jurisdiction to wetlands with continuous surface connection to "Waters of the US" — many isolated wetlands no longer federally regulated; state regulation may still apply
- USACE jurisdictional determination required if filling near a wetland — verify before purchase if rural acreage with wet ground

### Verification path — is this property on mains?

There is **no national database** of household water/sewer connections. To verify:

1. **Local water utility / municipal water department** — call with address, ask: connected? service-line material (lead / copper / galvanized / PEX)? meter size? backflow preventer required?
2. **County health department** — if private well: does well permit / water test exist?
3. **County sewer / sanitation district** — connected to sewer? if no, septic permit history?
4. **EPA Envirofacts** (`https://enviro.epa.gov/`) — confirms which public water system serves the area + violations history
5. **EPA Safe Drinking Water Information System (SDWIS)** (`https://sdwis.epa.gov/ords/sfdw_pub/r/sfdw/sdwis_fed_reports_public/`) — system-level compliance data
6. **EPA ECHO** (Enforcement Compliance History Online) (`https://echo.epa.gov/`) — utility compliance + violations
7. Listing language tells:
   - "Public water + sewer" / "city water + sewer" → mains both
   - "Well + septic" → both private
   - "Public water, septic" → mains in, private out (suburban-fringe common)
   - "Cistern" → rainwater capture (rural, often no mains)

### Cost ranges (federal-aggregate — verify locally)

| Scenario | Cost (USD) |
|---|---:|
| Tap fee to connect to municipal water (where main exists at street) | $1,500–$15,000 |
| Tap fee to connect to municipal sewer | $2,000–$20,000 |
| Lateral install from house to street main | $2,000–$10,000 |
| Drill new well (residential, 200–400 ft) | $5,000–$30,000 |
| Septic system new install (conventional) | $5,000–$15,000 |
| Septic with engineered drainfield (high water table / clay) | $15,000–$50,000+ |
| Lead service-line replacement | $2,500–$8,000 (often utility-funded post-LCRI) |
| Annual private-well water test | $50–$200 |

**Confidence**: HIGH for federal SDWA / LCR framework (EPA primary). MEDIUM for cost ranges (national aggregate; verify local plumber + utility quotes).

---

## Cost benchmarks (US 2026)

> **Federal-only constants in USD.** State + county + city overlays vary materially.

| Item | Cost (USD) | Notes |
|---|---:|---|
| **Home inspection** | $300–$700 | InterNACHI / ASHI inspector; 2,000-3,000 sqft typical |
| **Wood-destroying organism (WDO) / termite inspection** | $50–$150 | Often required by VA / FHA loans |
| **Sewer scope inspection** | $150–$400 | Recommended for older / large-tree-lined lots |
| **Survey (boundary)** | $500–$2,000 | Required by some states / lenders |
| **Appraisal** | $400–$700 (residential); $2,000+ (complex) | Lender-ordered |
| **Owner's title insurance** | ~0.4–1.0 % of price (one-time) | Varies by state; CA / TX / NY higher; sometimes seller-paid |
| **Lender's title insurance** | ~0.1–1.0 % of loan amount | Required by lender |
| **Title-insurance avg national (Fannie Mae sample)** | est. ~0.42 % of price | est. ~$1,337 avg on a $318k sample average price — sample average predates 2026 and is below this playbook's current NAR median; verify current with Fannie Mae title-cost data |
| **Settlement / closing fee** | $300–$1,500 | Settlement agent / title company / closing attorney |
| **Recording fee** | $20–$300 per document | County-set |
| **State / county transfer tax** | 0–2.5 % of price | None in 12 states; highest DC + DE + NY + CT |
| **Escrow setup** | $200–$1,000 | Where used |
| **HOA disclosure / transfer fee** | $200–$1,000 | If applicable |
| **FIRPTA withholding (foreign seller)** | 15 % gross (or 10 % / 0 % per buyer-occupancy + price) | Buyer-remitted to IRS |
| **Mortgage origination fee** | 0.5–1.5 % of loan | Lender-set |
| **Discount points (optional)** | 1 % of loan per point | Buys down rate |
| **PMI (Private Mortgage Insurance)** | 0.3–1.5 % of loan annually | If down payment < 20 % conventional |
| **MIP (FHA Mortgage Insurance Premium)** | 1.75 % upfront + 0.55–0.75 % annual | FHA loans |
| **Total buyer closing costs (federal-overlay average)** | **2–5 % of price** | Excludes down payment + state transfer tax |

## Active federal fiscal incentives (2025-2026)

> ⚠️ **Major OBBBA reset** (PL 119-21, 4 Jul 2025). The IRA-era residential-energy credits **terminate 31 Dec 2025** (placed-in-service / expenditure cliff). Verify current status as of date of read.

| Incentive | 2025-2026 status | Source |
|---|---|---|
| **§ 25C Energy Efficient Home Improvement Credit** | Up to $1,200/yr ($2,000 heat pumps); **TERMINATED 31 Dec 2025** by OBBBA | [IRS OBBBA Provisions](https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions) |
| **§ 25D Residential Clean Energy Credit (solar PV / geothermal / SWH / batteries / wind)** | 30 %; **TERMINATED 31 Dec 2025** by OBBBA | (same) |
| **§ 45L New Energy Efficient Home Credit (builder)** | Modified by OBBBA — verify current amount + termination | (same) |
| **HUD § 203(k) renovation loans** | FHA-insured purchase + rehab one-loan | `https://www.hud.gov/program_offices/housing/sfh/203k` |
| **HUD § 203(b) FHA standard** | Low-down-payment FHA; current MIP rates | `https://www.hud.gov/hud-partners/single-family-sfh203b` |
| **VA Loan** | 0 %-down, no PMI, for eligible veterans | `https://www.va.gov/housing-assistance/home-loans/` |
| **USDA Rural Development Loan (Section 502 Direct + Guaranteed)** | 0 %-down for eligible rural areas | `https://www.rd.usda.gov/programs-services/single-family-housing-programs` |
| **Good Neighbor Next Door (HUD)** | 50 %-off list for teachers / first responders / EMTs in revitalization areas | `https://www.hud.gov/program_offices/housing/sfh/reo/goodn/gnndabot` |
| **First-time-buyer down-payment assistance (DPA)** | State / local — varies; HUD aggregator: `https://www.hud.gov/buying/loans` |
| **§ 121 home-sale exclusion** | $250k / $500k (see Tax section) | (statute) |

## Common listing platforms

| Platform | Strength |
|---|---|
| **Zillow** (`https://www.zillow.com/`) | Widest reach; ZHVI estimate; Zestimate |
| **Redfin** (`https://www.redfin.com/`) | Brokerage + data center; daily refresh |
| **Realtor.com** (`https://www.realtor.com/`) | NAR-affiliated; MLS-direct feeds |
| **Trulia** | Owned by Zillow; neighborhood data |
| **Homes.com** | NewsCorp-owned; agent-centric |
| **Compass** (`https://www.compass.com/`) | Brokerage-direct |
| **MLS via NAR-affiliated broker** | Authoritative; public sees only IDX-licensed feeds |
| **Roofstock** (`https://www.roofstock.com/`) | Single-family-rental investor marketplace |
| **LoopNet** (`https://www.loopnet.com/`) | Commercial real estate |
| **Crexi** (`https://www.crexi.com/`) | Commercial + auction |
| **Auction.com**, **Hubzu**, **Xome** | REO + foreclosure auction |
| **HomePath** (Fannie Mae REO), **HomeSteps** (Freddie Mac) | GSE-owned REO |

## Caveats unique to US

- **No national cadastre** — title chain proven via title insurance + abstract; ~3,143 county recorders are authoritative
- **No federal property tax** — all state / county / municipal; effective rate spans 0.33 % (HI) to 1.84 % (IL) in 2025
- **Federal mandatory disclosure: LBP only** — everything else is state-specific (CA + TX have extensive forms; MA caveat-emptor)
- **FIRPTA exposure for foreign sellers**: 15 % gross-proceeds withholding (or 10 % / 0 % per occupancy + price); buyer is withholding agent
- **$60,000 federal estate exemption for non-domiciliary aliens** (vs $15M for citizens, 2026) — major risk for foreign individual ownership; mitigate via foreign blocker corp / trust / treaty
- **State foreign-buyer restrictions multiplying — no single authoritative count**: **~29 states** have enacted foreign-ownership restrictions on *agricultural land* ([Nat'l Ag Law Center FAQ](https://nationalaglawcenter.org/foreign-investments-in-ag/), 2026), while **38 states** saw broader foreign-adversary property bans introduced/advanced in 2025, of which **15 enacted** ([MultiState, Jan 2026](https://www.multistate.us/insider/2026/1/26/foreign-adversary-property-bans-advanced-across-38-states-in-2025)) — the spread is a scope difference (ag-land-only vs all real property; enacted vs advanced), not a factual conflict. Texas SB 17 (signed 20 Jun 2025, eff 1 Sep 2025) prohibits direct + indirect ownership + leases ≥ 1 yr by foreign adversaries; Florida SB 264 (eff 1 Jul 2023) bans agricultural land + within 10 mi of military for "foreign countries of concern" (CN, RU, IR, KP, CU, VE-Maduro, SY); **2025**: AZ / KY / TX / WV enacted new restrictions; AR / GA / ID / NE / TN / UT amended (NALC). **2026 session**: 7 more states enacted new/amended laws — IN SB 256; LA SB 200/466 + HB 192/816; MS SB 2341; OK HB 3431; SD SB 40 (eff 1 Jul 2026); TN SB 2233/2424; UT HB 291 — with 25 states considering bills (per NALC FAQ — verify current there before relying).
- **CFIUS Part 802** (Treasury) — foreign-person purchases within 1 mile (or 100 mi for Part 2) of 200+ military installations subject to review; expanded **9 Dec 2024** to add 59 sites
- **NFIP Risk Rating 2.0** fully implemented **1 Apr 2023**: flood premiums now per-property risk-priced; some properties saw substantial increases (capped at 18 %/yr by statute) — verify quote before closing
- **OBBBA (4 Jul 2025) overhaul**: SALT $40k cap (sunset 2030), MID $750k permanent, 25C/25D terminated 31 Dec 2025, estate exemption $15M (2026) — verify all federal-tax claims as of date of read
- **HOA prevalence in newer construction** (post-1990s subdivisions, condo, townhouse): monthly dues + special assessments + use restrictions; FL + AZ + CA + TX + NV + GA see most
- **Special assessment districts** — Mello-Roos (CA), MUDs (TX), CDDs (FL) — added annual property-tax burden NOT in standard tax-rate quote; review tax bill carefully
- **State non-disclosure of sale price**: AK / ID / KS / LA / MS / MO / MT / NM / ND / TX / UT / WY — comparable analysis must rely on MLS broker access (not public records)
- **Community-property states** (AZ / CA / ID / LA / NV / NM / TX / WA / WI + AK opt-in): both spouses have title rights regardless of name on deed
- **Homestead exemption** wildly variable: TX + FL unlimited (against creditors); some states limit to small dollar amount; affects bankruptcy + creditor claims
- **Insurance market disruption**: FL, CA, LA, CO have seen carrier withdrawals + non-renewals in high-risk ZIPs since 2022; verify availability **before** offer
- **Mortgage interest deductibility limited to $750k** acquisition debt + capped by SALT — high-cost areas (Bay Area, NYC, Boston, DC, LA) see deductibility erosion
- **Property tax basis variance**: CA Prop 13 freezes assessed value at last sale + 2 %/yr cap → reset on sale; most other states reassess annually or on a cycle

## Reddit / forum sources

- **r/RealEstate** — general buyer / seller / agent discussion
- **r/FirstTimeHomeBuyer** — process Q&A; lender / inspection horror stories
- **r/PersonalFinance** (housing flair) — affordability, math, compare-vs-rent
- **r/realestateinvesting** — landlord, BRRRR, syndication
- **BiggerPockets forum** (`https://www.biggerpockets.com/forums`) — investor-heavy, deep landlord knowledge
- **r/Mortgages** — rate / loan-product discussion
- **r/Landlord** — operations, eviction, screening
- **NAR member forums** (gated, REALTOR.com network)
- **r/<state>** subreddits — state-specific tax / disclosure / regulation chatter

## Verification authorities

| Authority | Level | When to call |
|---|---|---|
| **IRS** | Federal | FIRPTA, § 121, MID, SALT, estate-tax for NRA |
| **HUD** | Federal | LBP disclosure, FHA loans, 203(k), DPA |
| **FEMA** | Federal | FIRM lookup, NFIP quotes, Elevation Cert |
| **EPA** | Federal | Lead, radon, SDWA, asbestos, wetland 404 |
| **USGS** | Federal | Seismic hazard, geological hazards |
| **NOAA** | Federal | Hurricane track / storm surge / climate |
| **USFS** | Federal | Fireshed / wildfire risk |
| **USDA** | Federal | AFIDA foreign-ag-land filing, Rural Dev. loans |
| **CFIUS** (Treasury) | Federal | Foreign-buyer review near military |
| **Bureau of Indian Affairs (BIA)** | Federal | Tribal / Indian Country land — separate jurisdiction, federal consent often required |
| **NAR** | Trade | Member directory, state association lookup |
| **State Department of Revenue (DOR)** | State | Property + transfer tax rates |
| **State Insurance Commissioner** | State | Carrier complaints + market-of-last-resort (FAIR plan) |
| **State Real Estate Commission** | State | Broker / agent licensing; complaints |
| **State Attorney General** | State | Consumer protection, unfair-practice complaints |
| **County Recorder / Register of Deeds** | County | Title chain, lien search, deed lookup |
| **County Assessor** | County | APN, assessed value, tax-rate calculator |
| **County Treasurer / Tax Collector** | County | Actual tax bill, delinquency status |
| **County Building / Planning Department** | County | Permit history, zoning, code-enforcement record |
| **County Health Department** | County | Septic / well permits, food-service if STR |
| **Local Water / Sewer Utility** | Municipal | Mains connection, service-line material |
| **Local Fire Marshal** | Municipal | Defensible-space + smoke-alarm + WUI compliance |
| **HOA / Condo Association** | Private | Bylaws, special assessments, reserve fund |
| **Title Insurance Underwriter** | Private | Title commitment, exceptions, insurable defects |

## Quirks to know (US-specific)

- **Title insurance vs cadastre / Torrens**: US relies on private title-insurance market (most-litigated insurance line) instead of state-guaranteed land register. Owner's policy is one-time premium; covers historical defects through closing date. Lender's policy is separate. ~12 counties (HI / MN / MA / IL / OH residual) operate Torrens — sale + transfer have different procedure.
- **Recording-act priority**: Most states are **race-notice** (first-to-record-without-notice wins) or **notice** (last-to-take-without-notice wins); a few (LA / NC) are **race**. Failure to record a deed promptly can lose priority to subsequent BFP.
- **Closing process variance**:
  - **Escrow states** (CA, AZ, OR, WA): neutral escrow company holds funds + docs
  - **Attorney states** (NY, MA, GA, SC, NC, others): closing attorney mandatory
  - **Title-company states**: title company runs settlement
- **Buyer agent commission** (verified 2026-07-02): post-NAR settlement (practice changes eff 17 Aug 2024), buyer-agent compensation is **removed from the MLS** and **must be negotiated separately**; buyers sign a **written buyer-broker agreement before touring** ([NAR practice changes](https://www.nar.realtor/news/real-estate-news/nar-practice-changes-to-take-effect-august-17)). Commissions did **not** fall — Redfin buyer-side 2.42 % (Q3-2025, up from 2.36 % a year earlier); total both agents combined still mid-5 % per agent surveys. States are **codifying** the settlement: **California AB 2992** (Chapter 516, Statutes of 2024, signed 24 Sep 2024; eff **1 Jan 2025**) requires a written buyer-broker representation agreement as soon as practicable and no later than the buyer's offer (the pre-tour timing is the NAR practice rule, not the statute), covering compensation, services, when compensation is due and contract termination, max 3 months from execution, void and unenforceable if the duration/renewal limits are breached ([CA DRE Licensee Advisory 14 Nov 2024](https://dre.ca.gov/Licensees/Advisories/Advisory_2024_11_14_Changes_to_Buyer_Representation.html)) ([leginfo](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202320240AB2992)). The **DOJ antitrust probe is separate** from the private settlement and remains **open** (Participation Rule + Clear Cooperation Policy; SCOTUS denied NAR's cert petition 13 Jan 2025) — further rule changes remain possible. Verify current state contract forms with a broker.
- **Earnest money deposit (EMD)**: 1-3 % of price typical; held in escrow; subject to forfeiture if buyer defaults outside contingencies.
- **Contingencies**: financing, inspection, appraisal, title, sale-of-current-home — each must be in writing + waived in writing.
- **FIRPTA blocker structures**: foreign individual + US LLC (default disregarded) → FIRPTA still applies. Foreign corp owning US RPI → no FIRPTA on share sale (treaty-permitting), but corporate income tax + branch profits.
- **Mello-Roos (CA Community Facilities District)** + **MUD (TX Municipal Utility District)** + **CDD (FL Community Development District)**: special assessments funding infrastructure; can add 0.3-1.5 %/yr on top of regular property tax for 20-40 yrs; disclosure required but easy to miss.
- **Homestead exemption** vs **homestead protection**: two different concepts. Tax homestead = exemption from assessed value. Homestead protection = protection from creditors / forced sale. Variance huge by state.
- **Community property** (9 + AK opt-in states): both spouses own marital property regardless of title; affects divorce + estate.
- **Indian Country / tribal land**: separate federal jurisdiction; trust land cannot be alienated without BIA approval; many parcels appear on county maps but are not subject to county tax / law.
- **Right of first refusal (ROFR)**: common in HOAs, condos, family land — affects marketability; must clear pre-closing.
- **Adverse possession**: state-specific; typical 7-20 yrs continuous + open + notorious + adverse + exclusive use can vest title; survey + title commitment surface most issues.
- **Mineral / oil-gas / water rights**: severable from surface in most states (esp. western); confirm what's conveyed in deed.

## Source URL templates

| Source | URL |
|---|---|
| **IRS FIRPTA** | `https://www.irs.gov/individuals/international-taxpayers/firpta-withholding` |
| **IRS Pub 523 (sale of home)** | `https://www.irs.gov/publications/p523` |
| **IRS Pub 527 (rental property)** | `https://www.irs.gov/publications/p527` |
| **IRS Pub 925 (PAL rules)** | `https://www.irs.gov/publications/p925` |
| **IRS OBBBA Provisions** | `https://www.irs.gov/newsroom/one-big-beautiful-bill-provisions` |
| **IRS § 25C/25D OBBB FAQs** | `https://www.irs.gov/newsroom/faqs-for-modification-of-sections-25c-25d-25e-30c-30d-45l-45w-and-179d-under-public-law-119-21-139-stat-72-july-4-2025-commonly-known-as-the-one-big-beautiful-bill-obbb` |
| **FEMA Flood Map Service Center** | `https://msc.fema.gov/portal/home` |
| **FEMA NFIP Risk Rating 2.0** | `https://www.fema.gov/flood-insurance/risk-rating` |
| **FEMA Map of Federal Disaster Declarations** | `https://www.fema.gov/disaster/declarations` |
| **USGS NSHM 2023** | `https://www.usgs.gov/programs/earthquake-hazards/science/2023-50-state-national-seismic-hazard-model` |
| **USGS Earthquake Hazards Program** | `https://earthquake.usgs.gov/` |
| **NOAA NHC** | `https://www.nhc.noaa.gov/` |
| **NOAA HURDAT2** | `https://www.nhc.noaa.gov/data/hurdat/` |
| **NOAA NCEI Storm Events Database** | `https://www.ncdc.noaa.gov/stormevents/` |
| **EPA Lead** | `https://www.epa.gov/lead` |
| **EPA Map of Radon Zones** | `https://www.epa.gov/radon/epa-map-radon-zones` |
| **EPA Envirofacts** | `https://enviro.epa.gov/` |
| **EPA SDWIS** | `https://sdwis.epa.gov/` |
| **EPA AirNow** | `https://www.airnow.gov/` |
| **EPA Lead and Copper Rule Improvements** | `https://www.epa.gov/ground-water-and-drinking-water/lead-and-copper-rule-improvements` |
| **USFS Fireshed Registry** | `https://www.fs.usda.gov/rmrs/datasets/fireshed-registry-fireshed-and-project-area-boundaries-continental-united-states` |
| **Wildfire Risk to Communities (USFS)** | `https://wildfirerisk.org/` |
| **HUD § 203(k)** | `https://www.hud.gov/program_offices/housing/sfh/203k` |
| **HUD User datasets** | `https://www.huduser.gov/portal/datasets.html` |
| **VA home loans** | `https://www.va.gov/housing-assistance/home-loans/` |
| **USDA Rural Development** | `https://www.rd.usda.gov/programs-services/single-family-housing-programs` |
| **CFIUS Part 802** | `https://home.treasury.gov/policy-issues/international/the-committee-on-foreign-investment-in-the-united-states-cfius/cfius-real-estate-instructions-part-802` |
| **31 CFR Part 802 (eCFR)** | `https://www.ecfr.gov/current/title-31/subtitle-B/chapter-VIII/part-802` |
| **AFIDA / USDA FSA** | `https://www.fsa.usda.gov/programs-and-services/economic-and-policy-analysis/afida` |
| **FHFA House Price Index** | `https://www.fhfa.gov/data/hpi` |
| **NAR Existing Home Sales** | `https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales` |
| **Census Median New Home Sales** | `https://www.census.gov/construction/nrs/index.html` |
| **FHWA Traffic Volume Trends** | `https://www.fhwa.dot.gov/policyinformation/travel_monitoring/tvt.cfm` |
| **FHWA Highway Statistics** | `https://www.fhwa.dot.gov/policyinformation/statistics.cfm` |
| **BLS OEWS (wages)** | `https://www.bls.gov/oes/` |
| **BLS Occupational Outlook** | `https://www.bls.gov/ooh/` |
| **USAJOBS (federal jobs)** | `https://www.usajobs.gov/` |
| **USCIS Visa Categories** | `https://www.uscis.gov/working-in-the-united-states` |
| **Zillow Research** | `https://www.zillow.com/research/data/` |
| **Redfin Data Center** | `https://www.redfin.com/news/data-center/` |
| **Realtor.com Research** | `https://www.realtor.com/research/data/` |
| **Tax Foundation State Property Tax** | `https://taxfoundation.org/data/all/state/property-taxes-by-state-county/` |
| **NCA5 (climate)** | `https://repository.library.noaa.gov/view/noaa/61592` |
| **National Ag Law Center (foreign-ownership compilations)** | `https://nationalaglawcenter.org/state-compilations/aglandownership/` |

## Status

✅ **Federal overview fully populated** (initially populated 2026-05-01).

**Coverage check**: federal-level constants for tax (FIRPTA + § 121 + MID + SALT + NRA estate), risk (FEMA + USGS + USFS + NOAA + EPA), mains (SDWA + LCRI), rental (Schedule E/C + § 469), and disclosure (Title X LBP) — all with primary government sources and date-stamped figures. State / county verification paths provided for property tax, transfer tax, sale-price disclosure, mandatory disclosures, STR regulation, mains connection, and licensing.

**Confidence**: **HIGH** for federal tax / risk / disclosure / mains constants (all sourced to IRS / FEMA / USGS / USFS / EPA / Treasury primary government with citations and 2025-2026 dates). **MEDIUM** for state-by-state aggregates (range only — e.g., effective property tax rate 0.33 %–1.84 %; verify locally). **MEDIUM** for state foreign-buyer regime (rapidly evolving — 9 new state laws in 2025 alone).

**Last verified**: 2026-09-17 (NFIP authorization date corrected to 11 Dec 2026 per Public Law 119-103; portal climate-badge paragraph updated for the MSCI / First Street consolidation; balance unchanged) · previously 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged). Insurance / mains / rental / risks / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).

**2026 watch items** (revisit each ≤ 6 months):

- **OBBBA implementation guidance** — Treasury / IRS continues releasing rules through 2026 on §§ 25C/25D termination mechanics, SALT-cap MAGI phaseout, estate-tax $15M base, MID permanence
- **State foreign-buyer expansions** — multiple state legislatures considering 2026 sessions; National Ag Law Center tracker is canonical
- **CFIUS Part 802** — supplemental rules likely on energy-grid + critical-mineral proximity
- **NFIP reauthorization** — authorization now runs to **11 Dec 2026**: H.R. 6500, the Continuing Appropriations and Extensions Act, 2027, became Public Law 119-103 on 2 Sep 2026 and substituted 11 Dec 2026 for the 30 Sep 2026 date set by Public Law 119-75 (3 Feb 2026); CRS IN10835 (11 Sep 2026) counts it as the 36th short-term reauthorization since FY2017. Appropriations and NFIP authority now expire on the same day — Congress must reauthorize by 11 Dec 2026 or FEMA stops selling and renewing policies (in-force contracts run to the end of their one-year term). FEMA's own reauthorization page still showed 30 Sep 2026 on 17 Sep 2026 — check congress.gov / CRS, not FEMA, for the live date. NFIP endured its **longest-ever lapse (43 days)** during the Oct–Nov 2025 shutdown (restored retroactively to 1 Oct 2025 by HR 5371). Buyers needing NFIP for a federally-backed-mortgage closing must confirm the program is authorized on the closing date.
- **LCRI compliance ramp** — utilities ramping up for 1 Nov 2027 deadline; may surface lead-service-line replacement costs to homeowners
- **Insurance market** — FL / CA / LA / CO carrier exits continuing; FAIR-plan capacity stretched
- **NAR settlement (Aug 2024) follow-on** — buyer-agent commission practice still settling; DOJ antitrust probe (Participation Rule + Clear Cooperation Policy) is **separate + still open** (SCOTUS denied NAR cert 13 Jan 2025); states codifying (CA AB 2992 eff 1 Jan 2025); verify current state contract forms

## Extension TODOs

- [ ] Per-state child playbooks (50 states + DC) for property tax, transfer tax, mandatory disclosure, STR rules, foreign-buyer specifics
- [ ] CA / TX / FL / NY / IL / WA priority states (highest transaction volume)
- [ ] HOA / Mello-Roos / MUD / CDD lookup workflow
- [ ] Lead-service-line inventory check via state-utility public dashboards (per LCRR Oct 2024 inventory)
- [ ] Wildfire-insurance availability lookup per ZIP (FAIR plan + private market)
- [ ] FIRPTA withholding calculator with treaty-table integration (15 estate-tax treaties)
- [ ] State non-disclosure-of-sale-price workaround pathways
