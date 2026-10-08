# Universal Section Contract

Every country playbook implements these ten core + one regulatory sections with a consistent interface. The data sources differ; the interface and output structure don't.

Three core sections are **fully universal** (no country-specific implementation needed):
- `--amenities` (OSM Overpass — see `shared/amenities-osm.md`)
- `--climate` (Copernicus + IPCC — see `shared/climate-projections.md`)
- `--crime` (universal output, country-specific URLs — see `shared/crime-sources.md`)

The regulatory and transaction-buyer sections are also **fully universal** (single canonical doc with regional patterns + per-country tables):
- `--permits` (building-works permit thresholds, heritage overlays, conformity-at-completion — see `shared/permits.md`)
- `--agent` (buyer-side agency landscape: commission, licensing, MLS, dual-agency, EBA — see `shared/agent.md`)
- `--scams` (country-specific transaction-fraud register: BEC, deed forgery, off-plan disappearance, nominee structures, golden-visa price-inflation — see `shared/scams.md`)
- `--language` (foreign-buyer deed-language rule + sworn-translator mandate + Hague Apostille / POA chain + diagnostic-doc language + sworn-translation cost bands — see `shared/language.md`)
- `--connectivity` (broadband: address-level fibre availability checker, dominant ISPs, tariff bands, FTTH coverage, rural fallback, Starlink licence registry, strata trap — see `shared/connectivity.md`)
- `--home-tax` (buyer-nationality tax overlay: tax-residence trigger, worldwide-income reach, foreign-asset disclosure, CGT on disposal, annual wealth on overseas RE, estate/inheritance, exit-tax events, special inbound regimes — see `shared/home-tax.md`)
- `--cross-border` (opt-in cross-border-residency / cross-border-business framework: dual-jurisdiction tax-residence tie-breaker pointer per OECD MTC Art. 4(2), POEM/PE flag for company owners per Art. 4(3) + Art. 5, origin-country deregistration entry points across 4 parallel registers, EU/EEA/CH free-movement clarification — framework + linkage only, never per-country numerics — see `shared/cross-border.md`)
- `--remote` (foreign-buyer remote-execution: POA + apostille + RON + e-conveyancing + eIDAS QES + mortgage-bank residual wet-ink + Hawarden v ENS BEC trap — see `shared/remote.md`)
- `--relocation` (foreign-buyer 90-day post-completion onboarding: pets + DL exchange + vehicle import + utility setup + healthcare gap; FAVN-rabies-titer 7-month flow; CDC dog import 1 Aug 2024; AU EDR removed; LEZ landscape; foreign-buyer Catch-22 — see `shared/relocation.md`)

## Section: `--price`

**Goal**: Is the asking price fair vs the local market?

**Interface contract** — country playbook must provide:
- 1+ data source for local €/m² (or local currency/m²) average
- Range of prices for the locality (min/max)
- Trend indicator if available (up / flat / down over recent years)
- Method to find 3–5 comparable listings on the same locality
- Confidence note (high/medium/low — based on transaction sample)

**Output structure**:
```markdown
## Price Assessment

**Listing**: <price> (<currency>), <surface>, built <year> → **<price/area>**
**Local average**: <avg> (<range>) per <unit>, source: <source>
**Position**: <%> below/above average — **Verdict**: bargain | fair | aggressive | overpriced

| Comp | Surface | Price/area | Condition |
|---|---|---|---|

**Confidence**: <high/medium/low>
**Walk-away price**: <amount> if inspection reveals significant work
```

---

## Section: `--traffic`

**Goal**: How busy is the road? Noise/safety implications?

**Interface contract**:
- Method to identify the road's official designation (D-road, B-Straße, A-road, etc.)
- 1+ official traffic count source (national/regional government)
- Fallback: OSM `highway` class → coarse band

**Output structure**:
```markdown
## Traffic Profile

**Road**: <name> (<class>: <ref>, <highway>, maxspeed <maxspeed>)

| Road | Where | TMJA / AADT / DTV | % heavy vehicles |
|---|---|---:|---:|

**This property's road**: ~<X> v/d (estimated/measured)
- ≈ <Y> cars/hour daylight
- ≈ <Z> cars/hour at night

**Comparison**: <relative to nearby roads or country averages>

**Noise verdict**: 🟢 silent / 🟡 light / 🟠 audible / 🔴 nuisance
```

Country-specific data terms:
- **FR**: TMJA (Trafic Moyen Journalier Annuel) — Conseil Départemental
- **DE**: DTV (Durchschnittlicher täglicher Verkehr) — Bundesländer
- **UK**: AADT — Department for Transport
- **IT**: TGM (Traffico Giornaliero Medio) — ANAS / Regione
- **ES**: IMD (Intensidad Media Diaria) — Ministerio de Transportes / CCAA

---

## Section: `--tax`

**Goal**: Annual property tax + one-time purchase costs

**Interface contract**:
- Communal/local tax rate(s) for residential property
- Transaction tax rate (stamp duty / DMTO / Grunderwerbsteuer / IBI / etc.)
- Notary/legal fee structure
- Future revaluation/reform risk if any

**Output structure**:
```markdown
## Tax Estimate

**Local rates**: <table of rates>
**Estimated assessment base**: <local taxable value formula>

| Scenario | Annual tax |
|---|---:|
| Primary residence | <range> |
| Secondary residence | <range> |

**One-time at purchase**: ≈ <amount> in transaction taxes + legal fees

**Future risk**: <upcoming reform impact>

⚠️ Verification: request seller's last property tax bill.
```

Country-specific tax terms:
- **FR**: Taxe foncière, Taxe d'habitation RS, frais de notaire, DMTO 5.81%
- **DE**: Grundsteuer (post-2025 reform), Grunderwerbsteuer (3.5–6.5%), Notarkosten 1.5–2%
- **UK**: Council Tax band, Stamp Duty Land Tax (SDLT), legal fees ~£1–2k
- **IT**: IMU (seconda casa), TASI, imposta di registro 2–9%
- **ES**: IBI, ITP/AJD 6–11%, notario+registro 1–2.5%
- **NL**: OZB (gemeentelijk), overdrachtsbelasting 2–10.4%
- **BE**: Précompte immobilier, droits d'enregistrement 6–12.5%
- **CH**: Impôt foncier (cantonal), valeur locative imputed
- **AT**: Grundsteuer, Grunderwerbsteuer 3.5%
- **PT**: IMI, IMT progressive

---

## Section: `--rental`

**Goal**: Realistic short-let / vacation rental income + tax-optimised net

**Interface contract**:
- Local existing competition (3–8 nearest comparable units)
- Country-typical occupancy rates (rural / urban / coastal)
- Country tax regime for short lets (with thresholds and abatements)
- Classification benefits if any (e.g., FR meublé classé, IT CIR, ES VTV)

**Output structure**:
```markdown
## Rental Income Analysis

**Existing competition** (locality): <N> short-lets

| Unit | Sleeps | Weekly tariff |
|---|---:|---:|

### Realistic configurations

| Option | Year-3 gross | Net (low tax bracket) | Net (high tax bracket) |
|---|---:|---:|---:|

### Tax regime
- **Best regime**: <name + decision>
- Thresholds: <country-specific>
- Special status to claim: <e.g. classement, CIR, VTV>

### Strategic notes
- <pool / view / wifi differentiators>
- <regulatory traps: zone tendue, mandatory registration>
```

Country-specific regimes:
- **FR**: Micro-BIC classé/non-classé, URSSAF 6%/21.2%, plafonds 15k/83.6k
- **DE**: Vermietung & Verpachtung Einkommensteuer; commercial threshold; gewerbesteuer if hotel-style
- **UK**: Furnished Holiday Let (FHL) rules + new abolition 2025; income tax + property income allowance £1,000
- **IT**: Cedolare secca 21% short-let; CIR registration mandatory
- **ES**: VTV/VFT regional license; IRNR 19/24% for non-residents
- **NL**: Box 3 imputed; B&B regulated by gemeente
- **BE**: Régional licence (Brussels strict, Wallonia/Flanders moderate); IPP barème
- **CH**: Cantonal patente; valeur locative impacts taxe
- **AT**: Gewerbeschein if professional; ESt-Pauschalierung option
- **PT**: AL (Alojamento Local) registration; IRS Cat. F or B

---

## Section: `--work=<profession>`

**Goal**: Can the user earn a living locally with their profession?

**Interface contract**:
- Catchment population within 30 / 60 minute drive
- Country-specific employment platforms (Pôle Emploi, Bundesagentur, Job Centre Plus, etc.)
- Profession-specific licensing/certification requirements
- Country self-employment regime options (auto-entrepreneur, Kleinunternehmer, sole trader, autónomo, partita IVA, ZZP, etc.)

**Output structure**:
```markdown
## Local Work Options for <Profession>

### Catchment
| Place | Distance | Population | Notes |
|---|---|---:|---|

### Competition
| Player | Offer | Pricing |
|---|---|---:|

### Revenue options ranked
1. <Salaried at local institution>
2. <Independent>
3. <Online/hybrid>

### Legal status
| Status | When | Tax | Social charges |
|---|---|---|---|

### Realistic year-3 net
| Scenario | Net annual |
|---|---:|

### How to build it in 12 months
1. Month 0–1: ...
2. Month 1–2: ...
```

---

## Section: `--risks`

**Goal**: Every officially declared + climate + property-specific risk

**Interface contract**:
- 1+ official risk register (DICRIM / Hochwasserkarte / Risk register / Carta del Rischio)
- Address-level risk lookup if available (ERRIAL / equivalent)
- Climate projections to 2050 (DRIAS or country equivalent)
- Build-year hazards based on national construction-era patterns
- Mandatory diagnostics matrix at sale

**Output structure**:
```markdown
## Risk Map

### Officially declared
| Risk | Severity | Specific to property |
|---|---|---|

### High-attention items
🔴 **<Risk 1>** — explanation, mitigation cost, action
🟠 **<Risk 2>** — ...
🟡 **<Risk 3>** — ...

### Climate to 2050
- <temp change>
- <drought / flood / wildfire trends>

### Build-era mandatory diagnostics
| Diagnostic | Required because | Validity |
|---|---|---|

### Risk dashboard
| Class | Severity | Action priority |
|---|---|---|

### Pre-purchase checklist
1. ...
2. ...
```

---

## Section: `--mains`

**Goal**: Is the property on mains drains/sewer? Cost implications.

**Interface contract**:
- 1+ national/regional registry confirming sewer service exists for the locality
- Method to identify likely connection status (zoning plan / cadastre overlay / listing language)
- Verification path (which authority to call)
- Cost ranges for both connected and non-connected scenarios

**Output structure**:
```markdown
## Mains Drains Verification

### What the records confirm
- Locality has collective sewer: yes/no
- Operator: <name>
- Property location: bourg / outlying / hamlet / urban core

### Likely connection status
**Probability connected**: <%>

### Why probably yes
- <signal 1>

### Why uncertain
- <gap 1>

### Verification path (must do)
1. Call <authority>: <phone>
2. Ask: <country-specific question>
3. Request from seller: <country-specific document>

### Cost implications
| Scenario | Cost |
|---|---:|
| On collective, conform | <annual fee> |
| On collective, non-conform | <upgrade cost> |
| Outside collective, septic | <full system cost> |
```

Country-specific authorities:
- **FR**: Mairie / SPANC (commune-level)
- **DE**: Stadtwerke / Abwasserzweckverband
- **UK**: Water company (Thames Water / Severn Trent / etc.)
- **IT**: Comune / gestore idrico
- **ES**: Ayuntamiento / mancomunidad
- **NL**: Gemeente / waterschap
- **BE**: Commune / société wallonne/flamande des eaux
- **CH**: Commune / SIG / IWB
- **AT**: Gemeinde / Verband
- **PT**: Câmara Municipal / Águas de Portugal

---

## Section: `--crime`

**Goal**: Commune-level crime rate + national/regional comparison + trend.

**Universal contract**:
- Use the **per-country crime data source registry** in `shared/crime-sources.md`
- Pull latest year published by national police statistics or stat office
- Compute rate per 1,000 (or 100k) inhabitants
- Compare vs national + regional average
- Note 5-year trend if available
- Surface methodology breaks (e.g., FR CSI 2022, DE PKS revision)

**Output structure** (full template in `shared/crime-sources.md`):
```markdown
## Crime & Safety

**Locality**: <name>, <region>
**Population**: <pop>
**Data year**: <YYYY> (latest)
**Source**: <national police / stat office>

| Metric | Locality | National | Regional | 5-yr trend |
|---|---:|---:|---:|---|

### Verdict
🟢/🟡/🟠/🔴 — one-line justification

### Walking-around safety
<one-line qualitative note>

### Confidence
<HIGH/MEDIUM/LOW> — <reason>
```

**Verdict bands**:
- 🟢 < 50 % national average across all categories
- 🟡 50–110 % of national average
- 🟠 110–200 % for one+ category
- 🔴 > 200 % national average; multiple categories elevated

**Caveats to surface every time**:
- Recorded vs actual (under-reporting varies)
- Tourist destinations have inflated rates (transient population)
- Small communes: absolute numbers volatile; statistical noise
- Methodology changes: 2022-2023 reforms (esp. FR CSI, DE PKS) make 5-year comparisons tricky

---

## Section: `--amenities`

**Goal**: Distance to nearest essential services from the property.

**Universal logic** (works in every country): full OSM Overpass query patterns in `shared/amenities-osm.md`.

**What to look up** (single combined Overpass call):
- Supermarket / grocery (`shop=supermarket|convenience|grocery`)
- DIY / hardware / brico (`shop=hardware|doityourself|trade|garden_centre`)
- Pharmacy (`amenity=pharmacy`)
- General Practitioner (`amenity=doctors`, `healthcare=doctor|general_practitioner`)
- Hospital (`amenity=hospital`)
- Schools (`amenity=school|kindergarten`)
- Public transport (bus, train, tram, metro)

**Compute per amenity**:
- Closest by Haversine distance
- Walking time @ 5 km/hr
- Driving time @ 25/50/80 km/hr (urban / rural / motorway)

**Output structure**:
```markdown
## Local Amenities

| Service | Closest | Distance | Walk | Drive |
|---|---|---:|---:|---:|
| Supermarket | <name> | <km> | <min> | <min> |
| DIY / hardware | <name> | <km> | <min> | <min> |
| Pharmacy | <name> | <km> | <min> | <min> |
| General Practitioner | <name> | <km> | <min> | <min> |
| Hospital | <name> | <km> | <min> | <min> |
| Primary school | <name> | <km> | <min> | <min> |
| Bus stop | <name> | <km> | <min> | — |
| Train station | <name> | <km> | <min> | <min> |

### Verdict
🟢/🟡/🟠/🔴 — convenience band

### Walkability score
<X / 10>

### Medical access
🟢/🟡/🟠/🔴 — <one-line>

⚠️ OSM caveat: cross-check rural results via Google Maps before signing.
```

**Verdict bands**:
- 🟢 < 1 km / < 12 min walk: convenient urban
- 🟡 1–3 km / 12–36 min walk: suburban
- 🟠 3–10 km: transport-dependent
- 🔴 > 10 km: very rural; bulk-shopping concerns; medical access flag

**Country-specific quirks** (full table in `shared/amenities-osm.md`):
- DE: `shop=chemist` (Drogerie like dm/Rossmann) is NOT a pharmacy
- IT: tabacchi sometimes function as mini-marts
- FR: tabacs double as small convenience
- Each country has dominant brand chains worth recognizing

---

## Section: `--permits`

**Goal**: Can the buyer legally do the works the listing implies? What unauthorised works might already exist? What is the post-purchase enforcement risk?

**Universal logic** (works in every country): full implementation in `shared/permits.md`. Single canonical doc with regional patterns + per-country tables for all 126 supported countries — country playbook does NOT need a separate permits section.

**Disambiguation**: `--permits` ≠ `--work=<profession>`. The latter is local employment for a profession at the address. The former is permits for **building works** on the property.

**What to look up** (universal):
- Permit hierarchy: which works require nothing / declaration / full permit (country-specific 2-tier or 3-tier system)
- Numeric thresholds (m² creation, m² extension, height, façade modification) where statute defines them
- Listed-building / heritage overlay (separate parallel consent regime)
- Indicative timeline (declaration vs full permit, weeks/months)
- Conformity certificate at completion (DAACT FR / SCAGI IT / licencia de primera ocupación ES / autorização de utilização PT / Schlussabnahme DE / etc.)
- Retention / amnesty / regularization path for unauthorised existing works
- Post-purchase enforcement risk (limitation period for prior-owner unauthorised works)

**Output structure** (full template in `shared/permits.md`):
```markdown
## Permits & Building-Works Regime

**Country**: <ISO2>
**Permit hierarchy**: <none → declaration → full permit>
**Key thresholds**: <new build / extension / façade / internal-only / demolition / pool>
**Heritage overlay**: <authority + separate consent>
**Timeline (typical)**: declaration <weeks>; full permit <weeks/months>
**Conformity at completion**: <required / optional / not used>
**Retention / amnesty path**: <country-specific>
**Post-purchase enforcement risk**: <limitation period>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Cross-cutting traps to surface every time** (from `shared/permits.md`):
- The "tolerated" extension trap — passage of time does NOT legalise unauthorised structures in most civil-law jurisdictions
- Heritage overlay invisibility — Listed Buildings (UK), Monuments Historiques + ABF (FR), vincolo paesaggistico (IT), BIC (ES), Denkmalschutz (DE/AT) often unsignaled in listings
- Conformity-at-completion gap — properties sold without DAACT / agibilità / licencia de primera ocupación carry hidden time bombs
- Amnesty / condono windows close — historic regularization paths are rarely re-opened

---

## Section: `--scams`

**Goal**: Country-specific transaction-fraud register — what documented buyer-side scams target this country's market in 2024-2026, with regulator advisories, prosecutions, or investigative-journalism evidence.

**Universal logic** (works in every country): full implementation in `shared/scams.md`. Single canonical doc with 7 cross-cutting traps + regional patterns + per-country one-liners for all 126 supported countries — country playbook does NOT need a separate scams section.

**Disambiguation**: `--scams` ≠ `--integrity` ≠ `--risks`. `--scams` = country-specific **transaction-fraud** patterns targeting buyers (deed forgery, wire fraud, off-plan disappearance, nominee structures, golden-visa inflation). `--integrity` = data-honesty checks on the listing/cadastre output itself. `--risks` = natural + technological hazards.

**What to look up** (universal):
- Top 3-5 scam patterns documented for the country in 2022-2026
- Per pattern: scheme name (with native term), mechanism, victim profile, documented evidence (regulator advisory / prosecution / embassy / investigative-journalism URL), mitigation (which authority/registry to verify with)
- Confidence per pattern: HIGH (regulator advisory + prosecution) / MEDIUM (multi-source forum + practitioner) / LOW (anecdotal)

**Output structure** (full template in `shared/scams.md`):
```markdown
## Transaction Fraud Register

**Country**: <ISO2>
**Headline patterns** (top 3-5 by buyer-loss evidence):

### <Scheme name>
**Mechanism**: <one sentence>
**Victim profile**: <demographic>
**Evidence**: <regulator URL / prosecution case>
**Mitigation**: <verification path>
**Confidence**: <HIGH/MEDIUM/LOW>

### Universal mitigations
1. Voice-verify wire instructions on independently-sourced number
2. Pull cadastre/registry document yourself the day of signing
3. Engage independent buyer's lawyer (not seller's)
4. Verify agent license at country's registry
5. For foreign-restricted zones: pre-clear eligibility before signing
```

**Cross-cutting traps to surface every time** (from `shared/scams.md`):
- Wire-fraud at closing (BEC) — biggest by $ volume universally; voice-verify IBAN on independently-sourced number
- Title fraud / deed forgery / impersonated owner — UK HMLR Property Alert + ON LTAF backstop are the model defenses
- Off-plan developer disappearance — bank-guaranteed escrow only; existing-stock preference for non-residents
- Foreign-restricted-zone confusion / nominee structure — illegal in TH/ID/MX/MA/KW; courts unwind consistently
- Golden-visa / RBI price-inflation — independent statutory-licensed appraisal; ENDED programs cannot be "still available"
- Customary-tenure / restitution-lien — chain-of-title back to pre-disruption baseline (PL 1939, RO 1947/1989, BA pre-conflict)
- Concession-vs-freehold tourism-zone — zone-status verification BEFORE deposit (CR ZMT, BR marinha, BS Crown, CV ZDTI)

---

## Section: `--language`

**Goal**: Foreign-buyer language requirements — what language must the deed be in, when is a sworn translator mandatory at signing, what's the apostille / POA chain, what does sworn translation cost.

**Universal logic** (works in every country): full implementation in `shared/language.md`. Single canonical doc with 7 cross-cutting traps + regional patterns + per-country one-liners for all 126 supported countries — country playbook does NOT need a separate language section.

**Disambiguation**: `--language` ≠ `--notary` ≠ `--visa`. `--language` = deed-language rule + sworn-translator regime + POA-translation chain. `--notary` = transaction-completion process. `--visa` = residency programs.

**What to look up** (universal):
- Closing-deed language; bilingual permitted; which version controls
- Sworn interpreter at signing: mandatory / on demand / not used
- POA / apostille chain: Hague Apostille member status; chain from foreign-language POA → apostille / consular legalisation → sworn translation → notary acceptance
- Mandatory diagnostic / disclosure document language (DPE/APE/CEE/Energieausweis/EPC/BER/PEA — local-language-only or bilingual)
- Sworn-translation cost band (industry-reported or statutory tariff)
- Confidence: HIGH / MEDIUM / LOW

**Output structure** (full template in `shared/language.md`):
```markdown
## Language & Sworn-Translation Profile

**Country**: <ISO2>
**Closing-deed language**: <local language(s); which version controls if bilingual>
**Sworn interpreter at signing**: <mandatory / on demand / not used>
**POA chain**: <Hague Apostille y/n → apostille or consular legalisation → sworn translation → notary acceptance>
**Diagnostic docs language**: <local-only / bilingual standard>
**Sworn-translation cost**: <range, industry-reported or statutory>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Cross-cutting traps to surface every time** (from `shared/language.md`):
- Hague Apostille membership confusion — non-members (AE, EG, JO, KW, LB, QA, NG, KE, GH, TW, KH, LK, MV, MY, TH-until-late-2026, VN-until-Sept-2026) require full consular legalisation chain (4-8 weeks)
- "Sworn translator" means three different regimes — statutory profession (FR/DE/ES/IT/...), court-admitted (ZA/JP/KR/IN), or notary-public-certified (IL/US/UK/IE/AU/NZ + most common-law)
- Bilingual deeds — local-language version always controls (IT, DE, ID, MX, HU)
- Diagnostic documents universally local-language-only — buyer pays own translation
- State / regional variation breaks single-country assumptions — CA Quebec Bill 96, US CA Civ. Code § 1632, CH cantonal, BE language regions, IN state language, ES regional
- Consular POA bypass — civil-law consulates abroad can draft local-language POA directly, bypassing both apostille and sworn-translation steps
- Sworn-translator cost varies 10× across region — US/UK/AU/NZ ~$50-150/page market vs NO statutory NOK 1,200-2,500/page (~€100-220) vs full POA chain $1,500-3,500 in non-Hague jurisdictions

---

## Section: `--connectivity`

**Goal**: Foreign-buyer broadband / fixed-internet profile — official address-level fibre availability checker, dominant ISPs, tariff bands (entry / mid / gigabit) with currency + EUR/USD equivalent, FTTH urban coverage, rural fallback (5G FWA / Starlink / fixed-wireless), Starlink licence status, build-era / strata trap, country-specific quirk.

**Universal logic** (works in every country): full implementation in `shared/connectivity.md`. Single canonical doc with 7 cross-cutting traps + regional patterns + per-country one-liners for all 126 supported countries — country playbook does NOT need a separate connectivity section.

**Disambiguation**: `--connectivity` ≠ `--digital-nomad` ≠ `--mains`. `--connectivity` = address-level broadband verification (checker, ISPs, tariff bands, rural fallback, Starlink, strata trap) for property buyers. `--digital-nomad` = nomad-specific filter (national Speedtest tier, coworking density, time-zone overlap, DNV availability) — uses national medians, not address-level data. `--mains` = utility verification (sewer / water / gas / electricity), occasionally references the dominant ISP.

**What to look up** (universal):
- Broadband-checker URL — official primary-source address-level fibre availability map (regulator or state portal)
- Dominant ISPs (3-5 named carriers with FTTH product line + market position; wholesale-retail split flagged where it exists)
- Tariff bands (date-stamped 2025-2026): entry (~50-100 Mbps) / mid (~300-500 Mbps) / gigabit, local currency + EUR/USD equivalent, internet-only or bundle, install fee + contract length
- FTTH urban coverage % + rural fallback (DSL/VDSL, 5G FWA, Starlink, fixed-wireless, satellite)
- Starlink licence status (calendar-actionable registry): licensed / pending / banned / grey-market / not-yet-on-coverage-map
- Build-era / strata trap (HOA / SVJ / borettslag / talohyhtiö / consorcio / asamblea / kat malikleri kurulu / 小区 / mahalla approval; gated estate anchor-ISP exclusivity)
- Country-specific quirk (load-shedding ZA, EDL outages LB, GFW + IPLC CN, FX volatility AR/TR/EG, FUP capping LK/EG, etc.)
- Confidence: HIGH / MEDIUM / LOW

**Output structure** (full template in `shared/connectivity.md`):
```markdown
## Broadband & Connectivity Profile

**Country**: <ISO2>
**Address-level checker**: <regulator URL or "no national checker — carrier direct">
**Dominant ISPs**: <3-5 carriers with positioning>
**Tariffs (May 2026)**: entry <local + EUR/USD>, mid <local + EUR/USD>, gigabit <local + EUR/USD>; <internet-only / bundle>; install <fee>; <12mo / 24mo / no-contract>
**FTTH urban + rural fallback**: <urban %; rural option>
**Starlink**: <licensed YYYY-MM-DD / pending / banned / grey>
**Build trap**: <strata / HOA / riser / heritage>
**Quirk**: <country-specific>
**Confidence**: HIGH / MEDIUM / LOW
```

**Cross-cutting traps to surface every time** (from `shared/connectivity.md`):
- "Fibre available" on the listing ≠ active line at this unit — verify regulator address-checker + ask seller for active line ID before signing
- National FTTH percentages mask rural/urban gaps — ES 92% national vs 79% rural; UK 74% national but 90%+ urban with isolated rural gaps; BR 70% national but tier-1-skewed; AU mixes FTTP/FTTC/FTTN/HFC/FW/Sky Muster
- Starlink legality varies and changes — banned (CN/IR/SY/RU/BY/AF/CU/KP), pending (SA/MA/EG/BH/KW/AM/AZ/GE/UZ/IL-security/IN/KR), grey (ZA-30%-BEE), not-licensed (BA-major-EU-absence, JM, TR), recently licensed (AE Aug 2026, JO Feb 2026, CO Apr 2024); status moves fast
- 5G FWA does not replace fibre for upload-heavy work — symmetric-gigabit FTTH (IS Reykjavík Fibre, KR/JP/SG/HK/TW urban, CH FR symmetric add-ons) required for video conferencing at scale
- Strata / HOA / riser approval — strong individual right-to-fibre laws (FR Loi Pintat, IT D.Lgs. 259/2003 + Law 12/2019, PT DL 123/2009, ES Ley 9/2014); assembly approval routinely required (DE Mietshaus, AT WEG, NL VvE, BE syndic, CH Stockwerkeigentum, SE BRF, FI taloyhtiö, CZ panelák SVJ, IL board, IN society/RWA, ZA body corp, AU Owners Corp, JP マンション 管理組合, KR 아파트 단지)
- Microstate / state monopolies — MC, AD, LI, SM, MV, UY, EC, CV, MO, LB, CN, EG, BZ have single licensed operators or near-monopolies; expect 10-30% premium and longer install-windows
- Contract length traps + bundle pricing — 24mo locks EU-norm; UK anti-CPI-rise post-Ofcom 2024; ES Digi / PT Digi / UK altnets often no-permanencia; promo "first-12-months" tariffs nearly double at month 13 — read steady-state price

---

## Section: `--home-tax`

**Goal**: Buyer-nationality home-country tax overlay — what the buyer's home tax authority does to them annually, at disposal, at death, and at emigration because they own foreign property. Indexed by the **buyer's tax-residence country** (NOT the property country — uniquely orthogonal to all other sections).

**Universal logic** (works for any buyer cohort): full implementation in `shared/home-tax.md`. Single canonical doc with 7 cross-cutting traps + 20+ buyer-cohort patterns covering US/UK/CA/AU/NZ + DE/FR/IT/ES/NL + Nordics (SE/NO/DK/FI) + CH + JP/KR/SG/HK/CN + IL + emerging markets (IN/BR/MX/ZA/AE/SA/GCC). Country playbook does NOT need a separate home-tax section — the canonical doc is keyed by buyer residence, not property location.

**Disambiguation**: `--home-tax` ≠ `--tax` ≠ `--finance` ≠ `--notary`. `--home-tax` = buyer-residence-side (what the buyer's home tax authority does). `--tax` = property-country-side (local property tax, transaction tax, future revaluations). `--finance` = mortgage availability for non-resident buyers in the property country. `--notary` = transaction-completion process. Tax due in BOTH countries is the norm, with bilateral relief via DTT (credit method or exemption-with-progression).

**What to look up** (universal):
- Tax-residence trigger (days-test + domicile/centre-of-life test + treaty tie-breaker)
- Worldwide-income reach (form/schedule for foreign rental)
- Foreign-asset disclosure (FBAR + Form 8938 / T1135 / Modelo 720 / Quadro RW / Schedule FA / Form 3916 / Anlage AUS / Form 5060 / Bens no Exterior + CBE)
- CGT on disposal (rate, holding-period exemptions, treaty allocation, principal-residence relief)
- Annual wealth/property tax on overseas RE (IFI, Patrimonio + ITSGF, Formueskatt, Box 3, IVIE, Vermögenssteuer, Ejendomsværdiskat)
- Estate/inheritance exposure (worldwide for resident decedent/heir; treaty network US 16 / UK ~10 / DE 5 / FR ~7 / IT ~7 / ES ~3)
- Departure/exit-tax (does emigration trigger deemed disposition on foreign RE? US/CA/AU/IL/ZA YES; DE/FR/JP/KR shareholdings only)
- Special inbound regimes (Beckham, 24-bis, FIG, Olim, RNOR, 30%-ruling)
- Confidence: HIGH / MEDIUM / LOW

**Output structure** (full template in `shared/home-tax.md`):
```markdown
## Home-Country Tax Overlay (buyer's residence: <ISO2>)

**Tax-residence trigger**: <days / domicile / centre-of-life test>
**Worldwide income**: <yes/no/territorial>
**Foreign rental reporting**: <form / schedule>
**Foreign-asset disclosure**: <form name + threshold + penalty>
**CGT on foreign disposal**: <rate, holding-period, principal-residence relief>
**Annual wealth/property on foreign RE**: <name / rate / threshold>
**Estate/inheritance worldwide**: <yes/no + treaty count>
**Exit tax on foreign RE**: <yes/no + statute>
**Special inbound regimes**: <Beckham / 24-bis / FIG / Olim / RNOR>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Cross-cutting traps to surface every time** (from `shared/home-tax.md`):
- Phantom currency-gain on foreign mortgage payoff — IRC § 988 ordinary gain (US) / Div 775 FRE 4 (AU) / § 39(2) (CA) / § 57-3 (JP); anchor case *Quijano v. United States*; integrated systems (UK *Bentley v Pike* / DE / FR / IT) avoid bifurcation
- PFIC trap on foreign collective-investment vehicles (US-only) — § 1297; Spanish SOCIMI / French SCPI / German Offene Immobilienfonds / UK REIT / AU LIT-MIT all PFIC for US individual holders; § 1291 punitive default vs § 1295 QEF vs § 1296 mark-to-market
- Wealth tax overlap on overseas property — most DTTs do NOT cover wealth tax; FR resident + ES property = IFI worldwide AND Patrimonio Spanish-situs (no relief)
- Estate/inheritance-tax patchwork — US 16 treaties; UK ~10; DE 5; FR ~7; IT ~7; ES ~3 — most foreign property gets DOUBLE-taxed on death
- Exit-tax events on direct foreign RE — YES in US (§ 877A) / CA (§ 128.1) / AU (CGT event I1) / IL (§ 100A) / ZA (§ 9H); NO in DE (§ 6 AStG shareholdings only) / FR (Art. 167 bis) / JP (§ 60-2) / KR (Art. 118-9)
- Special-inbound-regime lock-in — IT 24-bis €100k/€200k 15y / IT 24-ter 7% pensioners / ES Beckham 24% / UK FIG 4y / IL Olim 10y + 2026 reporting reform / NL 30%-ruling → 27% from 2027
- Treaty FTC vs treaty exemption — exemption-with-progression (DE/AT/FR/CH most EU treaties) vs credit method (US/UK/CA/AU/JP/IN); DE-ES DTT 2013 atypically uses credit; verify per-treaty Article 24 method

---

## Section: `--remote`

**Goal**: Foreign-buyer remote-execution mechanisms — can a buyer execute a property purchase WITHOUT physically being present? Five distinct mechanisms covered: POA to local representative + apostille / consular legalisation, remote video-conference signing at notary, eIDAS QES / equivalent, digital land-register filing, mortgage-bank residual wet-ink.

**Universal logic** (works for any property country): full implementation in `shared/remote.md`. Single canonical doc with 7 cross-cutting traps + ~80-country regional patterns + cross-jurisdictional reform calendar covering all 126 supported countries — country playbook does NOT need a separate remote section. Pairs strongly with `--language` (apostille / sworn-translator / POA-translation chain).

**Disambiguation**: `--remote` ≠ `--language` ≠ `--notary` ≠ `--scams`. `--remote` = execution-side (POA + RON + e-conveyancing + eIDAS QES + mortgage residual). `--language` = language-side (deed-language + sworn-translator + POA-translation chain). `--notary` = process-side (days from offer to deed, closing costs, notary vs solicitor regime). `--scams` = fraud register (BEC at closing — *Hawarden v ENS* SCA 10 Jun 2024 affirms buyer bears BEC risk).

**What to look up** (universal):
- POA mechanism — local term + statutory anchor + form requirement (private vs notarial vs apostilled chain) + consulate-bypass availability
- Remote video-witnessed deed at notary — available y/n + scope (property in / excluded) + statute + platform + effective date
- eIDAS / equivalent QES — accepted at deed-signing y/n + format constraints + national-eID or cross-border-recognised
- Digital ID for foreign buyers — what's accepted; whether non-residents can practically obtain it
- Land-register electronic filing — system name + notary / attorney direct-filing y/n
- Mortgage residual wet-ink — bank-side practice, separate from notary side
- 2024-2026 reform — date-stamped, with effective date
- Confidence: HIGH / MEDIUM / LOW

**Output structure** (full template in `shared/remote.md`):
```markdown
## Remote-Execution Profile

**Country**: <ISO2>
**POA mechanism**: <local term + statute + form (private / notarial / apostilled chain) + consulate bypass y/n>
**Remote video-deed**: <available y/n + scope (property in/excluded) + platform + effective date>
**eIDAS / QES at deed**: <accepted y/n + format constraints>
**Digital ID for foreign buyers**: <obtainable y/n + which system>
**Land-register e-filing**: <system + notary direct y/n>
**Mortgage residual wet-ink**: <bank typical practice>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Cross-cutting traps to surface every time** (from `shared/remote.md`):
- eIDAS recognition asymmetry — QES is EU-mutual, deed-validity is national; DE Auflassung / AT § 31 GBG / IT rogito / NL transportakte / ES compraventa all still require physical presence even with eIDAS-2 EUDI Wallet rolling out 2026-2027
- Mortgage-bank residual wet-ink — RON-eligible note ≠ RON-eligible loan; Fannie/Freddie accept RON since 31 Mar 2020 + manufactured homes 7 Aug 2024 but originator + warehouse + recorder all gate
- Time-zone collision on real-time video signing — default to apostilled-POA chain rather than RON for buyers > 6 hours offset from destination
- State / canton / province fragmentation — US ~46 states + DC + PR have permanent RON; **CA SB 696 effective 1 Jan 2030 backstop** (regulations pending); AU PEXA + Sympli interoperability **suspended** 2024; CH 26 cantons each own Notariatsgesetz
- Identity-verification infrastructure incompatibility — Catch-22 for foreign buyers without local eID; pass-through via solicitor / consulate / RON credential-analysis fallback (FL § 117.295 expressly permits foreign-passport credential analysis)
- Apostille / consular legalisation chain still required for foreign POA — non-Hague: AE / EG / JO / KW / LB / QA / NG / KE / GH / TW / KH / LK / MV / MY / TH (deposited 30 Jun 2026; in force 28 Feb 2027); VN is Hague since 11 Sep 2026 except vs DE / AT / CZ (Art. 12(2) objections)
- AML/KYC gatekeepers — *Hawarden v ENS* [2024] ZASCA 90 BUYER bears BEC risk; FinCEN Residential Real Estate Reporting Rule effective 1 Mar 2026; EU AMLR/AMLA 19 Jun 2024 applies 10 Jul 2027

---

## Section: `--relocation`

**Goal**: Foreign-buyer 90-day post-completion relocation logistics — pets, driving licence, vehicle import, utility setup, healthcare gap. The "surprise cost / surprise timeline" patterns that turn a clean purchase into a scrambled move-in.

**Universal logic** (works for any property country): full implementation in `shared/relocation.md`. Single canonical doc with 7 cross-cutting traps + per-country detail for all 126 supported countries — country playbook does NOT need a separate relocation section. Pairs strongly with `--language` (apostille / sworn-translator), `--remote` (deed execution), `--home-tax` (tax-residence considerations on emigration).

**Disambiguation**: `--relocation` ≠ `--mains` ≠ `--connectivity` ≠ `--remote`. `--relocation` = buyer's account-holder logistics (pet entry + DL exchange + vehicle import + utility account opening + healthcare gap). `--mains` = parcel infrastructure (sewer / water / electricity / gas presence; pre-purchase). `--connectivity` = broadband layer (address-level fibre + Starlink registry). `--remote` = deed-execution mechanisms (POA / RON / e-conveyancing). `--relocation` is post-completion; `--remote` is pre-/at-closing.

**What to look up** (universal):
- Pets: entry rules + ISO microchip + rabies vaccinations + FAVN/RFFIT titer (where applicable) + waiting period + quarantine + banned breeds
- Driving licence: recognition / exchange / re-test + grace period + IDP + senior re-test thresholds + bilateral exchange list
- Vehicle import: emissions + age cap + RHD/LHD + tax stack + LEZ
- Utility setup: DSO + suppliers + ID requirements + deposits + foreign-buyer onboarding friction
- Healthcare: public-system enrolment timeline + private travel-insurance gap exposure
- 2024-2026 reforms — date-stamped
- Confidence: HIGH / MEDIUM / LOW

**Output structure** (full template in `shared/relocation.md`):
```markdown
## Relocation Profile

**Country**: <ISO2>
**Pets**: <microchip + rabies + FAVN waiting + quarantine + banned breeds>
**Driving licence**: <foreign DL grace + IDP + bilateral exchange list + re-test threshold>
**Vehicle import**: <emissions + age cap + LHD/RHD + tax stack + LEZ>
**Utility setup**: <DSO + suppliers + ID requirements + deposit + lead time>
**Healthcare**: <public-system enrolment timeline + gap insurance need>
**Confidence**: <HIGH/MEDIUM/LOW>
```

**Cross-cutting traps to surface every time** (from `shared/relocation.md`):
- Pet rabies titer waiting period — 6-7 month flow for AU / NZ / JP / SG (Schedule III) / MY; FAVN ≥ 0.5 IU/ml + 180-day wait
- EU pet passport vs Animal Health Certificate (AHC) — post-Brexit chain + EU Reg 2016/429 transition 22 Apr 2026 (UK pet passports invalidated for EU travel)
- Driving licence exchange — bilateral patchwork; EU 4DLD Dir 2025/2205 in force 25 Nov 2025; AU EDR removed Apr 2025-Feb 2026 (binary recognised vs full re-test)
- Vehicle import — emissions + age + LHD/RHD trifecta; KSA/QA/KW 5-year cap; KE 2026-01-01 KEBS RHD ≥2019; EG one-vehicle-per-5-years from 26 Dec 2024
- LEZ urban driving cost — UK ULEZ Greater London 29 Aug 2023; FR ZFE-m Crit'Air 3 ban 1 Jan 2025; PL Warsaw SCT Stage 2 + Kraków LEZ 1 Jan 2026; SE Stockholm Klass 3 EV-only 31 Dec 2024; NL zero-emission zones 1 Jan 2025
- Utility setup — foreign-buyer onboarding friction (the 30-day delay trap); Catch-22 chain DE/NL/FR/ES/IT
- Healthcare registration — the parallel 90-day cliff; DE Krankenversicherung mandatory day 1 (failure = €1,000+ backdated); FR Carte Vitale 3-mo residence

---

## Section: `--climate`

**Goal**: Long-term climate-change projections specific to the property's coordinates — temperature, sea-level rise, heatwaves, drought, wildfire, degree-day shift.

**Universal logic** (works in every country): full implementation in `shared/climate-projections.md`. Pulls from Copernicus Climate Data Store (CDS), IPCC AR6 Interactive Atlas, Climate Central Coastal Risk Screening Tool (coastal only), and national downscaled models where available (DRIAS FR, DKRZ DE, NCCS CH, SMHI SE, KNMI NL, etc.).

**What to look up** (universal):
- Köppen-Geiger climate classification (current baseline)
- Distance to coast (via Overpass `natural=coastline`)
- Temperature trajectory: now → 2050 → 2100 (SSP2-4.5 + SSP5-8.5)
- Hot days (TX≥30°C / TX≥35°C / TX≥40°C) per year
- Tropical nights (TN≥20°C) per year
- Sea-level rise (cm by 2050, 2100) — coastal only
- Drought / SPEI projection
- Wildfire FWI projection
- HDD / CDD shift (heating vs cooling degree-days)
- Precipitation pattern (winter wetter / summer drier typical for EU)

**Output structure**:
```markdown
## Climate & Long-term Resilience

**Coordinates**: <lat>, <lon>
**Climate zone**: <Köppen-Geiger code>
**Coastal**: <yes — distance X km / no>
**Elevation**: <m a.s.l.>
**Reference**: 1981–2010 baseline → 2050 / 2100

### Temperature trajectory
| Metric | Baseline | 2050 SSP2-4.5 | 2050 SSP5-8.5 | 2100 SSP5-8.5 |

### Sea-level rise (coastal)
| Year | RCP4.5 | RCP8.5 | High-end |

### Drought / wildfire / degree-days
- SPEI: <↑↓→>
- FWI: <% change>
- HDD shift: <X → Y> · CDD shift: <X → Y>

### Verdict
🟢/🟡/🟠/🔴 — <one-line>

### Confidence
<HIGH | MEDIUM | LOW>
```

**Verdict bands** (full criteria in `shared/climate-projections.md`):
- 🟢 Resilient — minimal impact, low exposure to acute climate events
- 🟡 Watch — moderate warming, some adaptation needed
- 🟠 Adapt — meaningful long-term cost or risk
- 🔴 Avoid or fortify — high exposure to multiple acute events

**Acute-event flags** (red flags):
- Coastal property < 5m elevation + SLR > 80 cm by 2100
- Wildland-urban interface (within 100 m of forest/scrub) in fire zone
- Within 100 m of river floodplain with flood multiplier > 2x by 2050
- Permafrost zone with thaw projected during ownership horizon
- Glacial outburst flood (jökulhlaup) zone

**Country-specific override** (when finer-resolution model exists):
- 🇫🇷 DRIAS · 🇩🇪 DKRZ + DWD Klimaatlas · 🇨🇭 NCCS · 🇸🇪 SMHI Klimatscenarier · 🇫🇮 Climateguide.fi · 🇳🇴 Klimaservicesenter · 🇩🇰 DMI Klimaatlas · 🇳🇱 KNMI Klimaatscenario's

---

## Implementation guidelines for country playbooks

When you write `countries/<iso2>/playbook.md`:

1. Implement the 7 country-specific sections (price, traffic, tax, rental, work, risks, mains). The 3 universal sections (crime, amenities, climate) inherit from `shared/`.
2. For each section, list:
   - Specific data source URLs (with patterns)
   - Extraction quirks (PDF size, OCR needed, login walls)
   - Compute formulas (specific to the country's tax/cost structure)
   - Country-specific output template (extending the universal one above)
3. For `--crime`: country-specific portal URLs go in the country playbook OR can be inherited from `shared/crime-sources.md`
4. For `--amenities`: the universal OSM logic in `shared/amenities-osm.md` applies; country playbook only needs to note brand-chain conventions
5. For `--climate`: universal Copernicus/IPCC always available; if country has finer-resolution model (DRIAS, DKRZ, etc.), country playbook should reference it as an override
6. Add a "Cost benchmarks" section with renovation costs typical to that country.
7. Add a "Mandatory diagnostics" section with the country's required-at-sale documents.
8. Reference the country's most-used real estate platforms for listing extraction.

## Cross-cutting layers (apply on top of section output)

When `--integrity`, `--journey=<type>`, or `--type=<kind>` is requested, additional cross-cutting analysis is layered onto the standard section output. See:
- `shared/integrity-checks.md` — 4 data-honesty checks
- `shared/journeys.md` — 7 buyer-journey templates
- `shared/property-types.md` — 11 specialized property-type templates

If a section is genuinely not applicable for a country (e.g., `--mains` in a country where mains drains are universal in the urban areas), still produce the section but say "universal in <country> — no individual verification needed unless rural/remote."
