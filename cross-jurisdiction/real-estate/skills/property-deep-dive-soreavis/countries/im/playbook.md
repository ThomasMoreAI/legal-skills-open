# Isle of Man 🇮🇲 — Property Due-Diligence Playbook

ISO2: `im`. Status: ✅ Fully populated. **Crown Dependency** — self-governing British Isles nation under the Crown; **not part of the UK**, **not part of the EU**, has its own Parliament (**Tynwald**, world's oldest continuous), legal system (Manx common law, derived from English common law), tax authority (Treasury — Income Tax Division), and land registry. UK governs only defence + international representation.

## Country profile

- Postcode pattern: `IM<n> <n><AA>` (UK-format prefix, all begin `IM1–IM9`)
- Currency: GBP (£) — Manx pound (Isle of Man Government issues notes/coins at parity with sterling; sterling circulates interchangeably)
- Language: English (Manx Gaelic revived on signage/schools; rarely encountered in conveyancing)
- Customs/VAT shared with UK under the **Final Expenditure Revenue Sharing Arrangement (FERSA)** — 1979 Agreement framework; **current FERSA re-signed 11 April 2025** (supersedes the 2020 provisional agreement); IoM share for YE 31 Mar 2025 = **£439.2M** (86.51% VAT / 13.49% other duties). Sources: [gov.im — FERSA](https://www.gov.im/about-the-government/departments/the-treasury/final-expenditure-revenue-sharing-arrangements-fersa) + [gov.uk — HMRC IoM Account YE 31 Mar 2025](https://www.gov.uk/government/publications). **VAT rates mirror UK.**
- Land registry: [Land Registry, General Registry, Government Offices, Douglas](https://www.gov.im/landregistry) — **Land Registration Act 1982** (compulsory registration on sale since 1 Dec 2009)
- Legal system: Manx law; conveyancing done by **advocates** (members of [Isle of Man Law Society / Manx Bar Council](https://iomlawsociety.co.im/)) — distinct from English solicitors
- Population: ~84,500 (2021 census, Cabinet Office)
- 17 local authorities + 4 Sheading parishes; rates collected by Treasury for all except Douglas Borough, Onchan District + Braddan Parish (self-collecting)

---

## Section: `--foreign-buyer-rules`

**No restriction on foreign ownership.** Any non-resident — EU, US, Asian, GCC — may freely buy freehold or leasehold property in the Isle of Man. There is no "approval" step, no nationality test on the title, and no "open / qualified" market split (contrast with Jersey or Guernsey). ([Locate IoM — buying property](https://www.locate.im/relocating/uk/working-in-the-isle-of-man/work-permit-exemptions); IoM Government — no restriction codified.) Locate Isle of Man (regulated entity, government promotional body) states explicitly: *"There are no restrictions on purchasing property in the Isle of Man, no stamp duty and no inheritance tax."*

The cleavage is **living + working ≠ buying**:

| Activity | Restriction |
|---|---|
| Owning property | None (any nationality, any value) |
| Visiting | Standard UK Common Travel Area (CTA) rules for British/Irish; visa rules per nationality otherwise |
| Residing > 6 months | Residence permit required for non-British/non-Irish nationals not under CTA |
| Working / self-employed | **Work permit required** unless exempt — **Control of Employment Act 2014**; British and Irish citizens are exempt by CTA; post-Brexit EEA citizens generally NOT exempt unless pre-settled |
| Tax residence | > 183 days in tax year, OR > 90-day rolling average over 4 yrs |

**⚠️ Unverified aggregator claim — primary-source check required**: aggregator pages (jarniascyril.com, arabmls.org, isleofmancompanyformation.com) repeat a claim that "government approval is required for purchases of undeveloped land or properties valued over £750,000, via DEFA application." **This was searched against gov.im and legislation.gov.im and not located on any primary government page** in this research pass (2026-05-27). The DLA Piper REALWORLD Ownership Restrictions atlas does **not** list IoM among jurisdictions with foreign-buyer approval regimes. The Land, Deeds & Probate Registries Fees & Duties Order 2023 (**SD 2023/0077** — primary source, confirmed) operates as a tiered duty by buyer category, NOT an approval-gated regime. Two possibilities: (a) the aggregator claim is stale/incorrect; (b) it refers to a sub-regime (Control of Employment + planning + work permit composite) not Land-Registry-level. **Verify with a Manx advocate before treating the £750k figure as an actual buyer-approval threshold.** Tier: 🔴 Model inference / 🟡 aggregator-only. **As of 2026-05-27 this gate is unverified at the primary source; treat as aggregator artefact unless an advocate produces the operative SD/statute.**

**Confidence**: HIGH for "no nationality restriction on ownership"; MEDIUM on the £750k approval claim (only aggregator-sourced, not confirmed at gov.im).

---

## Section: `--tax`

**Data sources** (priority — primary first):

1. **Treasury Income Tax Division** — [gov.im/incometax](https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/) (primary government); operative statute: **Income Tax Act 1970**
2. **Land, Deeds & Probate Registries Fees & Duties Order 2023 (SD 2023/0077)** — effective 1 May 2023 — [centralregistry.gov.im](https://centralregistry.gov.im/)
3. **PwC Tax Matters 2025/26** — [pwc.com/im — Tax Matters](https://www.pwc.com/im/en/services/tax/assets/Tax-Matters-2025-26.pdf) (regulated entity, cross-check)
4. **KPMG IoM Budget 2025/26 commentary** — [kpmg.com — IoM tax measures 2025/26](https://kpmg.com/dp/en/services/tax/family-office-private-client/tax-in-the-isle-of-man.html)

### Income tax (2025/26) — Income Tax Act 1970

| Band | Single | Married/Jointly assessed |
|---|---|---|
| Personal allowance | £17,000 | £34,000 |
| Standard rate (10 %) | next £6,500 | next £13,000 |
| Higher rate (21 %) | balance | balance |

(Sources cross-corroborated: [PwC IoM Tax Summaries — Taxes on personal income](https://taxsummaries.pwc.com/isle-of-man/individual/taxes-on-personal-income); [Locate Isle of Man — Income Tax](https://www.locate.im/relocating/uk/tax-and-ni/income-tax). 2025/26 tax year data — verify at [gov.im rates and allowances](https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/tax-practitioners-and-technical-information/rates-and-allowances/) before relying for transactional decisions. The higher rate dropped from 22% → 21% effective 2025/26.)

Personal allowance phase-out: reduced £1 for every £2 of income over £100,000 single / £200,000 jointly.

### Tax cap election (HNW) — Income Tax Act 1970 §§2ZA–2ZC

- £220,000/yr cap for individuals (2025/26 — raised from £200,000 effective 2025/26) ([Locate IoM — Tax Cap](https://www.locate.im/hnwi/tax-cap-election))
- £440,000/yr cap for jointly assessed couples
- Election made under **Income Tax Act 1970 §§2ZA–2ZC** (form **R264**); binds for **5 or 10 consecutive tax years**
- Break-even ~ £1,048,000 income at 2025/26 rates (Locate IoM)

### No transactional-property taxes — **but** Land Registry duty applies

The Isle of Man **does not levy UK-style Stamp Duty Land Tax** ([Katz & Co Land Duty primer](https://www.katzand.co/isle-of-man-land-duty-registration/)). **However**, the **Land, Deeds & Probate Registries Fees & Duties Order 2023 (SD 2023/0077)** (effective 1 May 2023) introduced a **tiered Land Registry duty** that operates as a transaction tax in practice ([Livingstone Surveyors duty calc](https://www.livingstone.im/mortgagecalculator/landregistryfees/)):

| Buyer category | Duty band | Rate |
|---|---|---|
| **Owner Occupier** (sole worldwide residence, under £1M) | £0 – £230,000 | £0 per £1,000 |
| | £230,001 – £500,000 | £10 per £1,000 (1 %) |
| | over £500,000 | £20 per £1,000 (2 %) |
| **Resident Non-Owner Occupier** (resident with other property / investor) | up to £3,000,000 | £20 per £1,000 (2 %) |
| | over £3,000,000 | £25 per £1,000 (2.5 %) |
| **Non-Resident** (outside IoM tax residence) | up to £3,000,000 | £40 per £1,000 (4 %) |
| | over £3,000,000 | £45 per £1,000 (4.5 %) |

**Worked example — £500,000 property**:
- Owner Occupier: £2,700 (= 0 + 270 × £10)
- Resident Non-Owner: £10,000 (= 500 × £20)
- Non-Resident: £20,000 (= 500 × £40)

(Exemptions: spouse/civil-partner transfers, charities, government bodies, certain probate transfers — verify with conveyancing advocate.)

### No annual property tax (CGT/IHT/Wealth) — confirmed absent

| Tax | Status | Source |
|---|---|---|
| Capital Gains Tax | **None** | PwC IoM 2025/26; gov.im (Income Tax Act 1970 silent on CGT) |
| Inheritance Tax / Estate Duty / Gift Tax | **None** | PwC IoM — "no death duties, estate duties, or gift taxes" |
| Wealth tax | **None** | PwC IoM |
| Annual Tax on Enveloped Dwellings (ATED) | **None** | (UK-only; does not apply IoM) |
| Annual property holding tax (national) | **None — but** see local Rates below | gov.im |

### Income tax on land transactions — **20 % company rate (anti-speculation)**

**Companies** deriving rental, development, or dealing-in-land income from Isle of Man land/property sources are taxed at **20 %** (since 6 April 2015 per gov.im **Company Income Tax Return Guide GN 58**). For **individuals**, dealing-in-land income remains within the personal 10%/21% scale unless held inside a company structure — but **HMRC-style "badges of trade" classification applies** (Income Tax Commissioners decision **CD 1/11**), so frequent flips / development trades can be re-characterised as trading rather than passive. Verify activity classification with a Manx tax adviser if the buyer's intent involves resale or development. ([PwC IoM Tax Matters 2025/26 — land transactions](https://www.pwc.com/im/en/services/tax/assets/Tax-Matters-2025-26.pdf); gov.im GN 58 Company Income Tax Return Guide.)

### Rental income tax

- **IoM resident landlord**: taxed as ordinary income at 10 %/21 % bands after personal allowance
- **Non-resident landlord (Isle of Man source income)**: **flat 21 %** on total taxable IoM income, **no personal allowance, no 10 % band** (PwC IoM 2025/26). Mandatory IoM tax return; return due 6 October following 6 April year-end; £100 fixed penalty for late filing ([gov.im — Non-resident IoM source income](https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/individuals/non-residents/receiving-isle-of-man-source-income/))
- **Homestay scheme** (live-in lodgers): £2,500 TT-period tax-free allowance (2026/27 Budget) — narrow scope ([iomtoday — Homestay TT 2026](https://www.iomtoday.co.im/news/residents-encouraged-to-register-for-homestay-ahead-of-isle-of-man-tt-2026-884436))

### VAT — Common Purse / FERSA with UK

- Standard rate **20 %**; reduced **5 %** (domestic energy, certain repairs); zero rate (food, books, public transport, **new-build residential**) ([PwC IoM 2025/26](https://taxsummaries.pwc.com/isle-of-man/individual/other-taxes))
- Registration threshold: turnover > **£90,000** (2025/26)
- **Implication for property**: residential sales = exempt (no VAT); residential rents = exempt; commercial property + new-build commercial = standard 20 %; option-to-tax mechanism mirrors UK
- VAT remitted via [IoM Customs & Excise](https://www.gov.im/categories/tax-vat-and-your-money/customs-and-excise/) under FERSA revenue-sharing arrangement with HM Revenue & Customs (UK); **FERSA re-signed 11 April 2025** with revised splits (86.51 % VAT / 13.49 % other duties); IoM share for YE 31 Mar 2025 = £439.2M

### Local rates (annual property tax)

Two-part bill, calculated from the **1969-baseline rateable value** × pence-in-the-pound rate set annually:

| Component | Set by | Notes |
|---|---|---|
| Local authority rate | Each of 17 local authorities (parish commissioners / town commissioners / Douglas Borough) | varies — Douglas typically highest |
| Water + sewerage rate | **Manx Utilities** | island-wide flat per rateable value band |

Rates 2025/26: 19 local authorities announced increases ([iomtoday — Rates 2025/26](https://www.iomtoday.co.im/news/isle-of-man-local-authority-rates-202526-how-much-youll-pay-from-april-as-19-areas-announce-increases-766271)). **Verification path**: look up parcel's rateable value via the [Treasury Rates Payments portal](https://services.gov.im/rates-payments/make-a-payment) (or seller's recent rates bill) and apply the current p/£ multiplier from the local authority's site (e.g., [michael.gov.im — Rates 2025-2026](https://michael.gov.im/news/rates-2025-2026-889118/)).

Typical annual rates bill: a single-family home with rateable value £200 × Douglas rate (e.g., £4.50 / £) ≈ **£900/yr** for local + ~£300–500 water/sewerage = est. **£1,200–£1,600/yr** total. (Indicative — varies materially by parish; **verify with seller's recent bill**.)

**Confidence**: HIGH on income/VAT/CGT/IHT/registry duty structure (multi-source primary + regulated); MEDIUM on annual rates worked example (parcel-specific rateable value not in this run).

---

## Section: `--price`

**Data sources**:

1. **Isle of Man Planning — sold-price statistics** (open data community project): [isle-of-man-planning.github.io/iom-planning-stats](https://isle-of-man-planning.github.io/iom-planning-stats/2026/03/31/isle-of-man-house-prices.html) — derived from Land Registry; useful for time-series
2. **Land Registry document search** (per-property deeds): [services.gov.im/deeds-probate-land-registry-document-search](https://services.gov.im/deeds-probate-land-registry-document-search/) — small fee per search; canonical actuals
3. **Listing aggregators**: [chrystals.co.im](https://www.chrystals.co.im), [dandara.com](https://www.dandara.com), [rightmove.co.uk (filter to IM)](https://www.rightmove.co.uk/property-for-sale/Isle-of-Man.html), [zoopla.co.uk (IM filter)](https://www.zoopla.co.uk/for-sale/property/isle-of-man/), [iomestateagents.com](https://www.iomestateagents.com)
4. **Locate Isle of Man relocation guide** for high-level market framing

**Compute**:
- Price/sq ft (UK convention used locally) = listing £ / floor area
- Cross-check against Land Registry actuals over last 2 yrs for nearest postcode
- Discount/premium = (postcode median – listing) / postcode median

**Caveats**:
- IoM property market is small (≤ ~800–1,200 transactions/yr depending on year) — postcode-level medians can be statistically thin (Reddit signal r/IsleofMan `1l80wjt` / `1b9opbf` corroborates extreme thinness, particularly on the rental side)
- "Sea view" + Douglas/Onchan corridor properties carry significant premium; Foxdale / rural west materially cheaper
- Listing surfaces are seller-stated — **verify against architect drawings / valuation report**

---

## Section: `--rental` (residential + short-let)

**Long-term residential**:

- **No rent control**; market-priced
- **Landlord Registration Act 2018** (in force): all residential landlords must register with the [Department of Infrastructure Housing Division](https://www.gov.im/landlordregistration/) (or successor; verify name at gov.im before filing — Cabinet Office reorganisations move this around)
- **Eviction**: under Landlord & Tenant Acts (Manx) — process via Manx courts, **not** UK Section 21/Section 8 procedure
- Standard tenancy: Assured Shorthold style by convention but governed by Manx statute
- **Market thinness**: Reddit signal (r/IsleofMan `1l80wjt`, mid-2025: "Only 26 properties for rent") corroborates an extremely thin rental supply — landlord-favourable for letting velocity, tenant-hostile

**Short-let / holiday-let / self-catering**:

- **Tourism Act 1975** + amendments — all self-catering / tourist accommodation must register with the **Department for Enterprise (Visit Isle of Man)** ([visitisleofman.com](https://www.visitisleofman.com))
- Income classed as **trading income** (not passive rent) — taxed at 10 %/21 % bands for resident individuals (flat 21 % no PA for non-residents; 20 % company rate if held in a company)
- Inspection/quality grading available (optional but a sales lever for premium positioning)
- **TT fortnight** (late May–early June) is the single dominant short-let revenue spike; year-round occupancy outside TT is materially lower
- **Homestay scheme 2026/27**: £2,500 TT-period tax-free allowance for live-in hosts (announced Budget 2025/26)

**Compute**:
1. TT-period gross: 14 nights × premium rate (£200–600/night for 2–4 bed depending on proximity to Glencrutchery Road / Mountain Course)
2. Non-TT shoulder + season: 8–14 weeks × off-peak rate
3. Operating costs: 30–40 % (cleaning, linen, agent commission)
4. Tax: trading income at 21 % over personal allowance (resident); 21 % flat (non-resident); 20 % (company)

**Confidence**: HIGH on regulatory framework; MEDIUM on TT rate ranges (peer-listing observational; verify via [airbnb.co.uk — Isle of Man](https://www.airbnb.com/isle-of-man/stays) or Booking.com TT-period sweep).

---

## Section: `--work=<profession>` (work permit + employment)

**Work permit regime** ([Control of Employment Act 2014](https://legislation.gov.im); [Locate IoM — work permit exemptions](https://www.locate.im/relocating/uk/working-in-the-isle-of-man/work-permit-exemptions)):

| Status | Permit required? |
|---|---|
| Manx-born | No (Isle of Man Worker) |
| 5+ yrs IoM resident | No (Isle of Man Worker) |
| Spouse of IoM Worker, cohabiting | No |
| British / Irish citizen, recent arrival | **Yes — permit required** unless other exemption applies |
| EEA citizen post-Brexit | Yes |
| Other nationalities | Yes (+ separate UK Visas immigration route via CTA) |

**Key sectors hiring (eGov / Locate IoM 2025)**: financial services, ICT/eGaming, fintech, biomedical, aerospace/engineering, Maritime — typically have lower friction for skilled-worker permits.

**Self-employment**: separate self-employment permit; sole-trader sets up via Income Tax Division registration + Manx Industrial Relations Service guidance.

**Confidence**: HIGH on regime structure; MEDIUM on sector hiring claims (depends on year + government promotion).

---

## Section: `--risks`

**Data sources** (parcel-level + commune-level):

1. **IOM Flood Hub** (primary government) — [iomfloodhub.im](https://iomfloodhub.im/) — interactive coastal + river flood maps; updated 2025 ([gov.im news — Updated flood maps May 2025](https://www.gov.im/news/2025/may/15/updated-flood-maps-designed-to-increase-resilience/))
2. **National Strategy on Sea Defences, Flooding and Coastal Erosion 2026–2036** — published 2025/26 by Department of Infrastructure (DoI)
3. **DEFA — Department of Environment, Food and Agriculture**: [gov.im/defa](https://www.gov.im/defa)
4. **Planning portal**: [gov.im/planningapplications](https://www.gov.im/planningapplications) — adjacent application risk
5. **Listing language** for flood/coastal flags

**Key risks**:

| Risk | Geography | Notes |
|---|---|---|
| **River flood** | Sulby (Ramsey area), Neb (Peel area), Glass (Douglas), Dhoo | Check IOM Flood Hub overlay |
| **Coastal flood + erosion** | West coast (Peel → Niarbyl), parts of east (Laxey), south coastal villages | National Strategy 2026–2036 maps |
| **Seismic** | **Negligible** — IoM is intraplate; no historical damaging quakes |
| **Radon** | Low compared to Cornwall/Devon; localised hotspots possible but no national high-risk classification — **verify with [UKHSA radon map](https://www.ukradon.org/) IoM postcode lookup** |
| **Wind / storm** | Notable — exposed Irish Sea position; design-wind loads in IoM Building Regs are higher than UK lowland equivalents |
| **Subsidence (mining legacy)** | Foxdale, Laxey, Snaefell, Bradda Head — historical lead/zinc/silver mining; **always request a coal-equivalent mining search via advocate before buying in former mining parishes** |
| **Argillaceous shrink-swell (clay)** | Low — geology is predominantly Manx Group slate; isolated clay pockets only |

**Build-era hazards** (English construction conventions broadly apply):
- Pre-1900 stone cottages (common in Castletown, Peel, Ramsey old town): solid walls, no DPC, slate roofs, lime mortar, lead paint
- 1900–1980: asbestos likely (Artex ceilings, AIB panels, cement roof sheets, vinyl floors) — Asbestos at Work Regs 2007 apply
- Pre-1970s: lead plumbing/paint
- 1980s–2000s: often timber-frame; cavity-wall standard
- Post-2010: largely meet IoM Building Regulations 2014 (modernised)

**Confidence**: HIGH on flood/coastal framework + mining legacy regions; MEDIUM on radon (parcel-level needs UKHSA lookup).

---

## Section: `--mains` (utilities)

**Operators**:

- **Manx Utilities** ([manxutilities.im](https://www.manxutilities.im)) — combined electricity + water + sewerage; single bill; statutory undertaker
- **Manx Gas** — natural gas (mains gas LIMITED — Douglas, Onchan, Ramsey, Peel, Castletown only; rural homes typically oil/LPG/electric/heat-pump)
- **Sure** / **Manx Telecom** — telecoms (broadband fibre rollout via the Manx Telecom Fibre Broadband Programme; 4G/5G via Sure + Manx Telecom)

**Verification path**:
1. Ask seller for last 12 mo Manx Utilities bill (water + electric + sewerage)
2. Check listing wording for sewer type: "mains drainage" = on collective; "septic tank" / "cesspit" = off-grid
3. For rural / hill homes: confirm mains water vs private borehole; mains drainage vs septic
4. Call **Manx Utilities customer services +44 1624 687687** for parcel-level connection confirmation
5. Mains gas availability: lookup at [Manx Gas postcode checker](https://www.manxgas.com) ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row (if outside reach, factor £3,000–7,000 oil tank install OR £8,000–15,000 air-source heat pump retrofit)

**Cost ranges (2025/26, indicative — verify with installer quotes)**:

| Work | Cost |
|---|---:|
| Septic tank replacement | £6,000–£14,000 |
| Connection to mains sewer (where available) | £3,000–£10,000 |
| Air-source heat pump retrofit | £8,000–£15,000 |
| Oil-fired boiler + tank replacement | £4,000–£8,000 |
| Borehole + treatment (private water) | £8,000–£20,000 |

---

## Section: `--notary` (advocate-led conveyancing)

**Process** (single-jurisdiction, English-common-law-derived):

1. **Offer accepted** (subject to contract) — not legally binding
2. **Buyer's advocate** instructed; seller's advocate prepares contract pack + draft transfer
3. **Searches**: Land Registry, Planning, Environmental (**DEFA**), Drainage (**Manx Utilities**), Local Authority — mining-area buyers add a mining-history search
4. **Survey**: independent surveyor (RICS-equivalent on IoM = **MIVS / Manx Institute of Surveyors**) — Homebuyer or Building Survey
5. **Mortgage offer** issued (if borrowing) — **IOMFSA**-regulated lender or UK lender with IoM lending license
6. **Exchange of contracts** — buyer's 10 % deposit committed; both bound; completion date set
7. **Completion** — purchase monies transferred via advocate; **Deed of Conveyance** signed and dated (legacy unregistered land) OR Land Registry transfer form completed (registered land — 1 Dec 2009+)
8. **Registration** at [Land Registry](https://www.gov.im/landregistry) within statutory window — **Land Registration Act 1982**; ALL first-registration applications require an Advocate's certificate
9. **Land Registry duty paid** to Treasury (per tiered scale, above) — duty regime under **SD 2023/0077**

**Advocate**: must be on the [IoM Law Society roll](https://iomlawsociety.co.im/) — UK solicitors / English solicitors **cannot** conduct Manx conveyancing without dual qualification. Conveyancing fees regulated under the [Advocates (Conveyancing Fees) Regulations 2000](https://iomlawsociety.co.im/wp-content/uploads/2019/09/8.5-Advocates-Conveyancing-Fees-Regulations-2000.pdf) (statutory scale; in practice many advocates quote fixed fees).

**Typical buyer-side cost stack** (residential, £400k Owner Occupier purchase):

| Item | Cost |
|---|---:|
| Advocate fees | £1,500–£3,500 |
| Searches | £150–£400 |
| Survey (Homebuyer) | £500–£900 |
| Mortgage product/admin fee | £0–£1,500 (lender-dependent) |
| Land Registry duty (Owner Occupier on £400k) | £1,700 (= £170k × £10 / £1k) |
| Land Registry registration fee | £200–£600 (per fee schedule) |
| **Total buyer fees** | **~£4,000–£7,000** (excl. duty + deposit) |

**Confidence**: HIGH on process structure; MEDIUM on cost ranges (varies by advocate firm + property complexity — verify with 2–3 advocate quotes).

---

## Section: `--finance` (banking + mortgage)

**Regulator**: [**Isle of Man Financial Services Authority (IOMFSA)**](https://www.iomfsa.im/) — supervises banks, insurers, fund managers, fiduciaries, and lending.

**Resident-style retail banks** (handle current accounts, mortgages):

- [Isle of Man Bank / NatWest Group](https://www.iombank.com)
- [Lloyds Bank International (Isle of Man)](https://www.lloydsbank.com/international)
- [HSBC Expat / HSBC Isle of Man](https://www.expat.hsbc.com)
- [Barclays Isle of Man](https://international.barclays.com)
- [Santander International](https://www.santanderinternational.co.uk)
- [Conister Bank](https://www.conisterbank.im) — Manx-incorporated SME lender (Manx Financial Group); incorporated under **Companies Act 1931**
- [Capital International Bank](https://www.capital-iom.com) — newer entrant (2020 licence)

**Note**: "RL360" mentioned in brief = an **insurance company** (international life assurance, formed from Royal London International), **not a bank** — useful for offshore-bond wrappers, not mortgages.

**Mortgages**:
- Available to residents and non-residents; non-resident LTVs typically capped at 60–70 %
- Stress-tested per IOMFSA macro-prudential guidance
- BoE base rate followed informally (Manx Treasury does not set policy rate); pricing tracks Sterling money-market
- Brokerage common — verify lender is **IOMFSA**-licensed; UK-only-licensed lenders cannot lend on IoM security without additional permission

**Confidence**: HIGH on regulator + main banks; MEDIUM on LTV figures (year + bank dependent).

---

## Section: `--property-types`

| Form | Status | Notes |
|---|---|---|
| **Freehold** | Standard | "Fee simple" equivalent; most residential |
| **Leasehold (long)** | Rare for residential; common for commercial | Lease > 21 yrs requires Land Registry registration |
| **Commonhold** | Not used | (Unlike UK 2002 reform; IoM did not adopt commonhold legislation in equivalent form) |
| **Quarterland / Intack** | Historical | Old Manx land categories; modernised under **Land Registration Act 1982** — irrelevant for typical modern conveyance, but mentioned on old title deeds |
| **Corporate-vehicle holding** | Common for HNW / commercial | Vehicles formed under **Companies Act 1931** (legacy) or **Companies Act 2006** (modern, 1A licence holder required) |

---

## Status

✅ **Fully populated** as of 2026-05-27.

**Confidence**: MEDIUM — Tax/registry-duty/conveyancing/banking/flood data from primary gov.im + regulated entities (PwC, KPMG, IoM Law Society) and is HIGH-confidence. However, several content cells (£750k foreign-buyer-approval claim, parcel-specific rates examples, mortgage LTV figures, build-cost ranges) are MEDIUM and need cross-check with a Manx advocate or the seller's specific bills before any high-stakes decision.

**Last verified**: 2026-05-27.

**Verification authorities**:
- Isle of Man Treasury — Income Tax Division ([gov.im/incometax](https://www.gov.im/categories/tax-vat-and-your-money/income-tax-and-national-insurance/))
- Isle of Man Land Registry ([gov.im/landregistry](https://www.gov.im/landregistry); enquiries by phone)
- **IOMFSA** ([iomfsa.im](https://www.iomfsa.im))
- IoM Law Society ([iomlawsociety.co.im](https://iomlawsociety.co.im))
- **Manx Utilities** ([manxutilities.im](https://www.manxutilities.im))
- IOM Flood Hub ([iomfloodhub.im](https://iomfloodhub.im))
- **DEFA**, Department of Infrastructure, Cabinet Office, **Tynwald** (gov.im directories)

**Quirks unique to IoM**:
- VAT shared with UK under FERSA (1979 framework; **re-signed 11 April 2025**, supersedes 2020 agreement; IoM YE 31 Mar 2025 share £439.2M) — VAT rules identical to UK; revenue shared
- No CGT, no IHT, no SDLT — but Land Registry duty (SD 2023/0077, May 2023) operates economically as a transaction tax with a 4× non-resident multiplier
- 1969-baseline rateable values still in use for local rates (vs UK England now using 1991/2003 bands)
- Tax cap election (£220k / £440k joint) for HNW — 5- or 10-year binding under Income Tax Act 1970 §§2ZA–2ZC
- Manx Gaelic mandated bilingual signage in newer developments — has no legal effect on title docs
- Mining-area subsidence searches are a parcel-level extra in Foxdale / Laxey / Snaefell / Bradda
- 20% company income tax rate applies to IoM land/property-source income (since 6 April 2015) — individuals taxed under 10%/21% personal scale unless re-characterised as trading

---

**📋 On PR merge — `regulatory-watch.md` follow-ups required**:

Add initial Isle of Man entries to `skills/property-deep-dive/shared/regulatory-watch.md`:

1. **SD 2023/0077** — Land, Deeds & Probate Registries Fees & Duties Order 2023, effective **1 May 2023** — non-resident 4-4.5% duty introduced as 4× owner-occupier rate. Tier 2. Affected sections: `--tax --foreign-buyer-rules --notary`. Source: Tynwald + centralregistry.gov.im. Revisit: 2027-05-01.

2. **FERSA re-signed 11 April 2025** — Final Expenditure Revenue Sharing Arrangement between IoM and UK; supersedes the 2020 provisional agreement; new splits 86.51% VAT / 13.49% other duties; IoM share YE 31 Mar 2025 = £439.2M. Tier 2. Affected sections: `--tax` (VAT subsection). Source: gov.im FERSA page + gov.uk HMRC IoM Account YE 31 Mar 2025. Revisit: 2027-04-11.

No `config/_visa-programs.json` update needed — IoM has no tracked visa programme (ACTIVE or ENDED) as of 2026-05-27.
