# Georgia 🇬🇪 — Property Due-Diligence Playbook

ISO2: `ge`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

## Country profile

- **Population**: ~3.7 million (2024 Geostat estimate); Tbilisi ~1.2 million, Batumi ~170k, Kutaisi ~135k
- **GDP per capita**: ~US$8,800 (2024 World Bank / Geostat); real GDP +9.4 % 2023, +9.5 % 2024 (Geostat)
- **Currency**: GEL (Georgian Lari). 1 EUR ≈ 2.95–3.05 GEL, 1 USD ≈ 2.65–2.75 GEL (NBG reference, ~2026-05 — rates float, verify at nbg.gov.ge; managed-float with NBG intervention)
- **Languages**: Georgian (official, ქართული); Abkhaz official in Abkhazia; Russian widely understood; English common in Tbilisi/Batumi tourist zones
- **EU status**: Candidate country since **December 2023** (European Council); accession process effectively paused mid-2024 after the "foreign agents" law and contested 2024 election (per EU Council conclusions Dec 2024)
- **Postcode**: 4 digits (e.g., Tbilisi `0100`–`0199`, Batumi `6000`–`6010`)
- **Admin levels**: 9 mkhares (regions) + 2 autonomous republics (Adjara, Abkhazia) + Tbilisi (capital) → 64 municipalities → ~3,700 settlements
- **Cadastre**: **NAPR** (National Agency of Public Registry, საჯარო რეესტრის ეროვნული სააგენტო) — public viewer FREE for owner-only data via napr.gov.ge
- **Identifier**: cadastral code (საკადასტრო კოდი) format `XX.XX.XX.XXX` (region.district.block.parcel)
- **Foreign-buyer rule**: residential **freehold** open to all foreigners since 1996 Civil Code. **Agricultural land**: foreign ownership banned by 2018 constitutional amendment Art. 19 (only Georgian citizens, Georgian state, or local self-governments may own ag land); pre-2017 foreign-acquired ag land grandfathered
- **Visa**: 365-day visa-free entry for **~95 nationalities** (USA, EU/EEA, UK, Canada, AU, NZ, Japan, S. Korea, GCC, Israel, etc.) per **Government of Georgia Ordinance №255 of 5 June 2015** (list of visa-free countries; latest amendments **№98 of 2 April 2025** and **№80 of 24 February 2026**, the latter extending the stay right of Ukrainian citizens who entered before 24 Feb 2025 to 24 Feb 2027). Separately, **Ordinance №256 of 5 June 2015** (holders of listed countries' visas / residence permits may enter visa-free) was amended by **Ordinance №122 of 17 April 2025** (published 22 Apr 2025, matsne.gov.ge/en/document/view/2867377): nationals of 17 countries (Afghanistan, Bangladesh, Ghana, Ethiopia, Eritrea, Yemen, Cameroon, Côte d'Ivoire, DRC, Morocco, Nigeria, Pakistan, Somalia, Syria, Sudan, Tanzania, Uganda) keep the Gulf-state visa / residence-permit route only with a multiple-entry visa or residence permit valid ≥ 1 year on the day of entry (substance per Ministry of Internal Affairs statement as reported by immigration advisers, secondary — consolidated text walled 2026-09-24) *(2026-05-27 verified, source matsne.gov.ge/en/document/view/2867361)*

## Section: `--price`

### Primary sources

- **NAPR public e-extract** (FREE, owner-only): `https://www.napr.gov.ge/`
  - Search by cadastral code or address; English UI available
  - Returns: owner name, area, encumbrances (იპოთეკა/mortgage, ყადაღა/seizure)
  - Full extract (`amonatsereb`) issued at NAPR offices or via PSDA (Public Service Hall) for ~5 GEL same-day / 14 GEL express
- **Geostat real-estate price index**: `https://www.geostat.ge/en/modules/categories/214/real-estate-price-statistics`
  - Quarterly Residential Property Price Index (RPPI), base 2018 = 100
  - Tbilisi-only sub-index published separately
  - 2024 RPPI: ~165 (Q4 2024 Geostat) → +8 % YoY — index may have moved since; check current Geostat RPPI
- **TBC Capital / Galt & Taggart / Colliers Georgia** — investment-bank quarterly market reviews (secondary, but methodology disclosed)
- **NBG financial stability reports**: `https://nbg.gov.ge/en/page/financial-stability-report` — incl. mortgage debt + house-price overheating indicators

### Price benchmarks (2024–2025 reference)

| Locality | New-build avg US$/m² | Resale avg US$/m² | Source |
|---|---:|---:|---|
| Tbilisi (Vake, Saburtalo, Mtatsminda prime) | ~1,700–2,500 | ~1,400–2,000 | TBC Capital Q4 2024 review |
| Tbilisi (Gldani, Isani, Samgori middle) | ~900–1,200 | ~700–950 | TBC Capital Q4 2024 |
| Tbilisi (Old Town listed buildings) | ~1,500–3,000 | ~1,200–2,500 | Colliers 2024 |
| Batumi (seafront new-build) | ~1,200–2,200 | ~900–1,600 | Galt & Taggart 2024 H2 |
| Batumi (off-seafront) | ~700–1,100 | ~500–850 | Galt & Taggart 2024 H2 |
| Kutaisi | ~500–800 | ~350–600 | MyHome.ge aggregate, 2025-Q1 |
| Telavi / Sighnaghi (Kakheti) | ~400–700 | ~300–550 | MyHome.ge aggregate, 2025-Q1 |
| Bakuriani / Gudauri (ski) | ~1,500–2,800 (apt-hotel) | ~1,000–1,800 | Colliers 2024 |

> All US$/m² are **est.** (calibration: cross-checked against ≥ 2 secondary aggregators + Geostat RPPI direction). Listing-platform medians vary widely by district; verify with 5+ comparables on the same street.

### Listing platforms

- **MyHome.ge** — largest portal: `https://www.myhome.ge/en/` *(per listing — verify with cadastre / on visit)*
  - Filters: city → district → micro-district; sale/rent; new build vs resale; surface m²
- **SS.ge** — long-running classifieds incl. real estate: `https://home.ss.ge/en` *(per listing — verify with cadastre / on visit)*
- **Place.ge**, **Livo.ge** — smaller portals, sometimes earlier listings *(per listing — verify with cadastre / on visit)*
- **Korter.ge** — new-build aggregator with developer-direct prices *(per listing — verify with cadastre / on visit)*
- **Facebook Marketplace + Telegram channels** (e.g., `t.me/tbilisirent`) — heavily used; high volume but unverified

### Compute

1. Listing price/m² = listing US$ ÷ m². Most Tbilisi/Batumi listings priced in **US$**, converted to GEL at signing
2. Compare to Geostat RPPI level for Tbilisi vs your district benchmark
3. **Trap**: "white frame" (თეთრი კარკასი / ნახევრად მოპირკეთებული) = bare-shell new-build with no internal finishing; finishing typically adds US$200–US$400/m² (est., from Colliers 2024 fit-out survey — verify per quote)
4. **Trap**: "green frame" (მწვანე კარკასი) = unfinished without windows/utilities — even cheaper but +US$300–US$500/m² to reach habitable
5. **Trap**: balcony/terrace included in advertised m²? Georgian convention typically includes them at 100 % — confirm with developer
6. **Trap**: parking is rarely included in apartment price; expect US$8,000–US$25,000 for an underground space in central Tbilisi/Batumi (est. — verify per development)

---

## Section: `--traffic`

### Primary source

- **Roads Department of Georgia (საქართველოს საავტომობილო გზების დეპარტამენტი)**: `https://www.georoad.ge/`
  - Statistics page (Georgian) lists annual traffic surveys ("მოძრაობის ინტენსივობა") on international + state roads
  - Historical AADT counts published as PDFs by road segment
- **Ministry of Regional Development & Infrastructure**: `https://www.mrdi.gov.ge/en` — sectoral data, road master plans
- **Tbilisi City Hall transport planning**: `https://tbilisi.gov.ge/` (Georgian); 2030 Sustainable Urban Mobility Plan published 2022

### Key term

**AADT** equivalent in Georgian: საშუალო წლიური დღიური ინტენსივობა (sashualo ts'liuri dghiuri intensivoba)

### Verdict bands (residential noise impact)

- 🟢 < 1,000 v/d (rural side road, village street)
- 🟡 1,000–5,000 v/d (small municipal road, urban side street)
- 🟠 5,000–20,000 v/d (urban arterial, secondary highway)
- 🔴 > 20,000 v/d (primary international highway S1/S2/S3/S4, Tbilisi inner ring, Rustaveli/Agmashenebeli)

### Coarse fallback

OSM `highway` class → road class:
- motorway/trunk = international highway (S-routes)
- primary = state route (Sh-routes)
- secondary = municipal main
- tertiary = local connector
- residential = village/settlement street

### Notes

- Tbilisi private-vehicle fleet roughly doubled 2010 → 2023 per Geostat transport stats; congestion now severe on Heroes' Square, Vake-Saburtalo axis, Vazha-Pshavela
- East-West Highway (S1) Tbilisi → Batumi: ongoing widening to 4 lanes (continuous since 2014); completion past Rikoti pass 2024
- **Trap**: properties advertised "5 min from highway" usually mean **on** a slip road — check actual setback and noise barrier presence

---

## Section: `--tax`

### Annual property tax — ქონების გადასახადი (Property Tax)

Governed by Tax Code of Georgia Title VIII (Article 201–207); **set by each municipality within statutory caps**.

**For natural persons** (Art. 201):
- Applies only if **household annual income > 40,000 GEL** (~US$14,800 / ~€13,600) (2025 threshold per Tax Code Art. 201.2). Where prior-year household income does **not exceed 40,000 GEL**, no property tax is due **other than land tax** — this gate is a national Tax Code rule (per Revenue Service), not a municipal act *(2026-08-07 verified, source Revenue Service)*
- Rate band: **0.05 %–1.0 %** of market value, on a sliding scale by income
  - Income 40,000–100,000 GEL → 0.05–0.2 %
  - Income > 100,000 GEL → 0.8–1.0 %
- Tbilisi schedule — set by **Tbilisi Sakrebulo Ordinance №20-90 of 30 Dec 2014** (reg. 200130000.35.101.016108), last amended by **Ordinance №6-19 of 26 Dec 2025** (published 30 Dec 2025, retroactive to 1 Jan 2025), which left individual rates untouched. The previously cited "Decision #14-69, Dec 2024" is **not** the governing instrument:
  - Prior-year household income **under 100,000 GEL**: **0.2 %** of market value
  - Prior-year household income **at or above 100,000 GEL**: **0.8 %** of market value
  - Late-December annual revisions expected — re-check each January against the consolidated text at `https://matsne.gov.ge/ka/document/view/6734892` / tbilisi.gov.ge *(2026-08-07 verified, source Tbilisi Sakrebulo Ordinance №20-90 as amended by №6-19 + Revenue Service)*
- "Market value" assessment: declared by taxpayer; revenue service may challenge
- Annual filing on form 100 by **1 November**, payment by **15 November**

**For legal entities** (Art. 202):
- 1 % of average annual book value of immovable property (rate set by municipality, cap 1 %)
- **Tbilisi keeps the 1 % default for resident enterprises.** Ordinance №6-19 of 26 Dec 2025 cut the rate to **0.001 %** only for sports activities and regulated municipal passenger transport (M3 buses, metro, Rike–Narikala / Chavchavadze–Turtle Lake / University–Bagebi cable cars), for obligations arising 1 Jan 2025 to 1 Jan 2028 — the carve-out does not reach a residential property-holding company, which stays on the 1 % default *(2026-08-07 verified, source Tbilisi Sakrebulo Ordinance №6-19)*

### Land tax — მიწის გადასახადი

- **Agricultural land**: per-hectare fixed rate by zone (e.g., Tbilisi peri-urban 1st zone: ~28 GEL/ha, 5th zone: ~5 GEL/ha) — Tax Code Art. 204
- **Non-agricultural land** (residential plot under house): municipality-set per-m² rate × zone coefficient × area
  - Tbilisi: **0.24 GEL/m² base rate × district territorial coefficient**, per Tbilisi Sakrebulo Ordinance №20-90 as amended by №6-19 of 26 Dec 2025; the previously stated "zone coefficient (1.0–1.5)" range was **not confirmed** on re-verification — read the coefficient for your district off the ordinance schedule at `https://matsne.gov.ge/ka/document/view/6734892` *(2026-08-07 verified, source Tbilisi Sakrebulo Ordinance №20-90)*

### Example calculation

A US$150,000 (≈ 405,000 GEL at 2.70 GEL/USD) Tbilisi 2-bed apartment, owner household income > 100k GEL:
- Annual property tax = 0.8 % × 405,000 GEL = **3,240 GEL/yr (~US$1,200 / ~€1,100)**

Same flat, owner household income ≤ 40k GEL:
- Annual property tax = **0 GEL on the dwelling** (below the national Tax Code gate) — the gate exempts every property tax **except land tax**, so a separately-titled plot still attracts it *(2026-08-07 verified, source Revenue Service)*

> Property tax in Georgia is materially lower than W. Europe in absolute GEL terms but the income-threshold + market-value-declared mechanism means many foreign owners with modest local income pay nothing on their main home.

### Transaction taxes (one-time at purchase)

- **Transfer tax / stamp duty**: **NONE** for typical resale (no property transfer tax in Georgia per Tax Code)
- **VAT (DDS, დღგ)**: **18 %** on new-build sale by VAT-registered developer (Tax Code Art. 165 sets rate; Art. 160 defines taxable supply; Art. 168/176 carry the resale-by-individual exemption); usually included in advertised price — verify "DDS-iani" (with VAT) vs "DDS-is gareshe" (without VAT)
- **NAPR registration fee**: ~50 GEL standard, 200 GEL same-day, 500 GEL 1-hour express (Public Service Hall tariff 2024)
- **Notary**: registration of sale-purchase contract is **NOT mandatory** (NAPR registration suffices); notarised contract optional, fee ~0.05–0.5 % of contract value (Notarial Chamber tariff)
- **Real estate agent**: usually **3–5 %** paid by seller; foreign buyers sometimes asked to pay buyer-side commission — negotiate
- **Total transaction cost** (buyer side, resale): typically **0.1–0.5 % of price** — among the lowest in the world

### Capital gains / income tax on sale

- **Personal sale of residential immovable** held **> 2 years**: **EXEMPT** from PIT (Tax Code Art. 82.1.b)
- Held **≤ 2 years** by individual: **5 % flat** on gain (not on gross — on profit) per Art. 82
- Sale by legal entity: profit included in 15 % corporate income tax (CIT) base; Estonia-model deferral applies — CIT only on distribution (since 2017 reform)

### Future risk

- **EU candidate status (Dec 2023)**: accession de facto halted since 27 Jun 2024 (European Council) and at a standstill per Council Presidency conclusions of 16 Dec 2025 — EU-harmonisation pressure on transfer tax is not a planning basis; no concrete bill 2025
- 2024–2025 political turbulence: tax-code amendments unpredictable; monitor Revenue Service circulars at `https://www.rs.ge/`
- Discussion of a national real-estate registry of beneficial ownership for AML — no statute yet

---

## Section: `--rental`

### Long-term residential

**Income tax on rental** — Tax Code Art. 81:
- **Individual landlord, residential lease to natural person**: **5 % flat** on gross rental income (Art. 81.2) — no expense deductions, no social contributions
  - Filed on form 200 quarterly OR annual form 100 by 1 April year+1
- **Individual landlord, lease to legal entity** or **non-residential lease**: **20 % PIT** on net (gross minus documented expenses)
- **Legal entity (LLC/JSC)**: rental in CIT base; Estonia model (only on distribution since 2017)

**Small Business Status** — for sole proprietors only (Tax Code Art. 84):
- Annual revenue **≤ 500,000 GEL**: **1 % flat** on **turnover**
- Income > 500,000 in any year → **3 % rate on the excess** above GEL 500k for that year; status revoked from 1 January of year+2 if breached in **two consecutive** years *(2026-05-27 verified, source Andersen + rs.ge + Tax Code Art. 88-95)*
- Excluded activities (Decree #415 of 2010 as amended): consulting, finance, gambling, currency exchange — **residential rental IS allowed** under SBS for individual entrepreneurs registered as IE
- Foreign nationals **can register as individual entrepreneur** with Georgian tax residency; SBS application via rs.ge

> The 1 % SBS rate is the headline foreigner-attraction fact, but it requires being a registered Individual Entrepreneur (IE) **and** meeting tax residency — not automatic for a non-resident foreigner letting one apartment. For a non-resident landlord using PIT 5 % on residential lease to natural persons, the effective rate is already very low.

> **Labour-migration overlay (from 1 March 2026)**: the amendments adopted 26 June 2025 (**Law №862**) require a **right to labour activity** — plus a labour residence permit or D1 visa — for **self-employed foreigners and entrepreneurs** beyond the visa-free year; those whose labour-migrant database registration was active on **1 March 2026** must hold work authorisation + residence permit by **1 January 2027**, else **GEL 2,000** on the worker or self-employed foreigner (and **GEL 2,000** on an employer per worker), doubled on repeat. Work done **fully remotely for a foreign employer** is out of scope (**Law №1509 of 15 April 2026**) — **confirm with PSDA whether letting via IE/SBS brings you in scope before relying on the 1 % rate** *(2026-08-07 verified, source Parliament of Georgia + `https://matsne.gov.ge/ka/document/view/2806732`)*

### Short-term rentals (Airbnb / Booking)

**Status**: largely unregulated at national level as of 2025-2026.

#### Current obligations (2025)

- **Tax classification**: STR to natural persons → 5 % PIT for individual; 1 % under SBS for IE
- **VAT**: 18 % if landlord turnover > 100,000 GEL/12 months from STR (Tax Code Art. 157) — STR specifically counted as "hotel-like" service
- **Hotel tax / tourist fee**: **NONE national**; **Tbilisi has no city tourist tax 2025**; Batumi (Adjara) introduced a **2 GEL/night municipal tourist fee** for accommodation (Adjara Supreme Council 2024 — verify current rate at adjara.gov.ge)
- **Guest registration**: hosts of foreign guests must file PMC (Patrol Police) notification within 3 working days for stays > 24h — enforced patchily for STR; mandatory for licensed hotels
- **Building management association** (ამხანაგობა / amkhanagoba) approval: not required by law but increasingly required by amkhanagoba bylaws in newer Tbilisi/Batumi developments — check before buying

#### Tbilisi-specific (most regulatory pressure)

- 2023–2024 City Hall debate on Old Town STR cap (modelled on Lisbon/Barcelona); no statute passed as of 2025
- Some Old Town heritage-listed buildings: STR de facto restricted by Cultural Heritage Agency conservation conditions
- **Trap**: "ცენტრალური აპარტამენტი" (central apartment) listings in old buildings — heritage status may block STR-grade renovations

#### Batumi-specific

- Adjara 2 GEL/night tourist fee applies (above)
- "Aparthotel" developments (Wyndham, Orbi, Alliance, Next Iveria etc.) often have built-in management agreements with revenue-share; read terms — operator share ~30–45 % (est., from published Batumi aparthotel contracts — verify per development)
- Seasonal demand: Jun–Sep peak (~80 % occupancy in waterfront), Oct–May ~25–35 % (est., from Colliers 2024 Batumi review — verify)

### Strategic notes

- **Tbilisi (Vake/Vera/Mtatsminda/Old Town)**: highest year-round STR yield; 5 % PIT or 1 % SBS makes net-of-tax materially higher than EU comparables
- **Batumi seafront**: highest peak-season yield but ~6-month low season; aparthotel revenue-share dilutes gross
- **Bakuriani / Gudauri (ski)**: Dec–Mar peak only; summer hiking shoulder; ~120-day usable rental window
- **Long-term residential**: Tbilisi gross yields commonly cited at **6–10 %** by Colliers/TBC 2024 — verify against your specific listing

---

## Section: `--work=<profession>`

### Job platforms

- **HR.ge** — largest job board: `https://www.hr.ge/`
- **Jobs.ge** — long-running general: `https://jobs.ge/`
- **MyJobs.ge**, **SuperJob.ge**
- **LinkedIn Georgia** — active in IT, finance, BPO, NGO sectors
- **Ministry of Internally Displaced Persons, Labour, Health & Social Affairs** (Worknet, official labour portal): `https://worknet.gov.ge/`

### Self-employment regimes (foreigners eligible)

- **Individual Entrepreneur (IE / ინდივიდუალური მეწარმე)**: register at PSDA in 1 day, ~20 GEL fee
  - Default tax: PIT 20 % on net
- **Small Business Status** (annual turnover ≤ 500,000 GEL): **1 % on turnover**, registered via Revenue Service form
- **Micro Business Status** (annual turnover ≤ 30,000 GEL): **0 % income tax**, only excluded activities apply
- **LLC (შპს / SPS)**: Estonia-model CIT — 0 % until profit distribution, then 15 % on dividend
- **Tax residency**: 183+ days in any 12-month rolling period OR "high-net-worth individual" status (assets > 3 million GEL)

> **Registering a regime is not a right to work.** From **1 March 2026** (labour-migration amendments, adopted 26 June 2025, **Law №862**) self-employed foreigners and entrepreneurs need a **right to labour activity** — plus a labour residence permit or D1 visa — beyond the visa-free year; work done **fully remotely for a foreign employer** is out of scope (**Law №1509 of 15 April 2026**). See *Visa / residence pathway for working foreigners* below *(2026-08-07 verified, source Parliament of Georgia + `https://matsne.gov.ge/ka/document/view/2806732`)*

### Salaried benchmarks

- Average monthly nominal wage 2024 Q4 (Geostat): **~2,030 GEL** (~US$750) — economy-wide
- IT/finance sector Tbilisi: ~3,500–8,000 GEL/month for mid-level (HR.ge market reports 2024)
- **Minimum wage**: only **20 GEL/month** statutory (1999 figure, never updated — symbolic); effective market floor in Tbilisi ~800–1,200 GEL for low-skill (est., HR.ge low-skill postings 2024 — verify)

### Catchment heuristics

- Within 30 min of Tbilisi central districts: full salaried opportunity
- Batumi: regional jobs (tourism, port, BPO); 30-min catchment limited
- Kutaisi: industrial/logistics jobs; Hualing FIZ + airport BPO cluster
- Mountainous regions (Svaneti, Kazbegi, Tusheti): seasonal tourism only; no full-year salaried market

### Visa / residence pathway for working foreigners

- **365-day visa-free** entry covers digital nomad / remote work for ~95 nationalities
- **Work residence permit** (eMigration via PSDA): for those needing > 1 year continuous presence; tied to employer or business. **From 1 March 2026** the labour-migration amendments (adopted 26 June 2025, **Law №862**) require a **right to labour activity** for foreign workers engaged by a **local employer** and for **self-employed foreigners and entrepreneurs** beyond the visa-free year — lawful work needs an **employment contract + right to labour activity + labour residence permit or D1 visa**. Labour immigrants whose database registration was active on **1 March 2026** must obtain work authorisation + residence permit by **1 January 2027**, else **GEL 2,000 on the employer per worker AND GEL 2,000 on the worker or self-employed foreigner** (doubled on repeat). Labour-market test waived for **International Company** and innovative-startup-status employers, or where the posted vacancy *simultaneously* pays **over GEL 15,000 gross/month** AND requires a relevant higher-education degree (Government Resolution **№70 of 20 Feb 2026**). Art. 60 temporary-stay-right exemption added by **Law №1815 of 25 June 2026** (commencement 1 September 2026); holders of a valid **investment residence permit** are also outside the labour-migration law (Art. 1(4)(f)) *(2026-08-07 verified, source Parliament of Georgia + `https://matsne.gov.ge/ka/document/view/2806732`)*
- **"Remotely from Georgia"** programme: launched 2020; currently OPEN per geoconsul.gov.ge (income proof US$2,000/mo or US$24k savings + foreign employment + travel medical insurance; 360-day non-renewable). **2026-03-01 reform, scope narrowed 15 April 2026**: the labour-migration amendments require a right to labour activity for **self-employed foreigners and entrepreneurs** beyond the visa-free year, but **Law №1509 of 15 April 2026** (in force on publication) took OUT of scope work done **fully remotely for a local employer** that needs no entry into Georgia, and work or services for a **non-resident** tied to that non-resident's activity outside Georgia — so **remote work for a foreign employer is NOT caught**. Also out of scope: short-term professional activity, public-institution work, category 1-3 directorships, heritage-restoration work — verify current status at sda.gov.ge / mfa.gov.ge *(2026-08-07 verified, source geoconsul.gov.ge + Parliament of Georgia + `https://matsne.gov.ge/ka/document/view/2806732`)*
- **Real-estate residence permits** (Law on Legal Status of Aliens and Stateless Persons Art. 15-16): **short-term residence permit** for non-agricultural real estate valued by an accredited appraiser **above USD 150,000** GEL-equivalent (US$100,000 before 1 March 2026) → 1-year permit, renewed 1 year at a time, no re-valuation while the same property is kept (Art. 15(j)); **investment residence permit** for real estate **above USD 300,000** or a USD 300,000 investment → 5-year permit (Art. 15(h), unchanged); valid investment-permit holders are outside the Law on Labour Migration (Art. 1(4)(f)) — apply at PSDA Public Service Halls (sda.gov.ge); issuance authority is **PMMG / Ministry of Justice**; verify current thresholds at sda.gov.ge AND mfa.gov.ge *(2026-09-24 verified, source Law №2045-IIს consolidated text `https://matsne.gov.ge/ka/document/view/2278806` + Law on Labour Migration `https://matsne.gov.ge/ka/document/view/2806732`; 50 % uplift eff 2026-03-01 per Law №863 Art. 2(2))*

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **National Environmental Agency (NEA / გარემოს ეროვნული სააგენტო)** | `https://nea.gov.ge/En` | Hazard maps: flood, landslide, mudflow, drought |
| **NEA hazard atlas (geohazards portal)** | `http://drm.cenn.org/` (CENN — Caucasus Environmental NGO Network, NEA partner) | Multi-hazard interactive map |
| **Ministry of Environmental Protection & Agriculture** | `https://mepa.gov.ge/En/` | Environmental impact assessments, climate strategy |
| **Institute of Earth Sciences, Ilia State University** | `https://iliauni.edu.ge/en/iliauni/institutebi-451/dedamicis-shemstsavlel-metsnierebata-instituti` | Seismic monitoring, fault maps |
| **Institute of Earth Sciences & National Seismic Monitoring Centre (Ilia State University)** | `https://ies.iliauni.edu.ge/` | Real-time seismicity feed, seismic + GNSS station data (Georgian-language site) |
| **GeoSurvey (LEPL National Environmental Agency, Geological Service)** | `https://nea.gov.ge/En/Departments/Geology` | Geological maps, landslide registry |
| **Nuclear & radiation safety (Georgia)** | data not publicly available — verify with the [Ministry of Environmental Protection and Agriculture of Georgia](https://mepa.gov.ge/En/) | Radiation context only; no radon mapping product located |

### Flood / landslide / mudflow zones

- Georgia is one of the most landslide-prone countries in Europe — ~70 % of the territory has some landslide / mudflow susceptibility per CENN/NEA atlas
- **High-risk zones**: Adjara coastal escarpment, Imereti gorges, Racha-Lechkhumi, Mtskheta-Mtianeti, Kakheti foothills, Greater Caucasus southern slope
- **Tbilisi specific**: 2015 June flash flood (Vere river) killed 23 — Saburtalo / Vake riverside still has Q100 flood exposure; CENN atlas shows zone
- **Mudflow (selevye / ღვარცოფი)**: distinct from river flood; small mountain catchments hit hard during summer storms — common in Adjara, Kazbegi, Mestia

> **Verification path**: NEA + CENN maps are commune/district-level, not parcel-level. For a specific cadastral code, request a hazard certification from NEA Geological Service (fee-based, ~2–4 weeks).

### Seismicity

- Georgia sits on the **Lesser/Greater Caucasus collision zone** — moderate-to-high seismicity (Mw 6–7 historically possible)
- **Major historical events**: Racha 1991 (Mw 7.0, ~270 deaths), Tbilisi 2002 (Mw 4.5 with structural damage), Spitak 1988 (Armenia, Mw 6.8 — felt severely in southern Georgia)
- Building code: Georgian seismic norms (PN 01.01-09 / PN 01.07-09), aligned with Russian SNiP and partly Eurocode 8; **Tbilisi designated seismic zone 8 (MSK)** — design PGA ~0.2g
- **Pre-1991 Soviet panel-block buildings** (`khrushchyovka` / `panelka` / Lilo, Gldani, Varketili series): retrofit status uneven; some demolished, many in service — independent structural survey strongly advised before purchase

### Radon

- **No national radon map published as of 2025** (NACEC/NRSA confirms no parcel-grade dataset)
- Geological substrate of Georgia (granitic intrusions in Greater + Lesser Caucasus) is consistent with elevated radon potential, but no public verification grid
- **Verification path**: independent radon measurement (3-month alpha-track detector, cost ~US$50–US$200 for the kit, available via private labs in Tbilisi)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1921 (Tsarist)** | Soft-fired brick + lime mortar; many heritage-listed; weak seismic performance; lead paint likely |
| **1921–1955 (early Soviet, Stalinist)** | "Stalinka" buildings; thicker walls, better than later panel; asbestos in some roofing |
| **1955–1991 (Khrushchyov + Brezhnev panels)** | Khrushchyovka (5-storey), 9-storey + 16-storey panel; asbestos in joints common; aging utility risers; some seismic retrofits ongoing |
| **1991–2003 (post-Soviet collapse)** | Often unpermitted ("self-build"); hazardous; legalised in waves under "Self-built Object Legalisation" laws — verify NAPR recordation |
| **2003–2012 (Saakashvili boom)** | Building boom Tbilisi/Batumi; quality varies; 2012 Construction Code overhaul tightened standards |
| **2012–present** | Modern code (Order #41 of MoE 2016 + amendments); seismic + fire stricter; energy-efficiency requirements added 2020 (NZEB by 2025 deferred to 2030) |

**Asbestos**: pre-2005 likely in roofing + insulation; no national mandatory removal regime (unlike EU) — buyer due diligence required.

### Mandatory documents at sale

| Document | Required because | Notes |
|---|---|---|
| **NAPR ამონაწერი (extract)** | All sales | Verify owner + cadastral code + encumbrances (იპოთეკა, ყადაღა) |
| **Sale-purchase contract** | All sales | Bilingual Georgian + (often) English; must be registered at NAPR within 1 month |
| **Cadastral plan** | All sales | Issued by NAPR; ensure matches building footprint |
| **Technical inventory passport** (ტექნიკური ინვენტარი) | Older buildings | Confirms surface, layout — historically issued by Sakgeografia/BTI; not always current |
| **Building usage permit (ექსპლუატაციაში მიღება)** | New builds | Confirms construction completed legally — often **missing** for self-built or grandfathered objects → NAPR may have registered title without it; renovation/extension permits hinge on this |
| **No-debt certificate** (utilities, building management fees) | Apartments in managed buildings | From amkhanagoba (HOA equivalent) — ensure no fond-debts attached to flat |
| **Heritage listing check** | Old Town buildings | Cultural Heritage Agency register: `https://heritagesites.ge/` — listing imposes severe renovation restrictions |

### Climate change projections (NEA + national communications to UNFCCC)

- 2024 6th National Communication: +1.5–4.0 °C by 2100 (depending on RCP); Mtskheta-Tbilisi axis warming faster than Black Sea coast
- Black Sea coastal erosion: +20–60 cm sea-level rise by 2100 (RCP4.5 / RCP8.5) — Adjara coast (Kobuleti, Ureki, Anaklia) at risk
- Glacier loss: Greater Caucasus has lost ~30 % glacier mass since 1960; further 50–70 % loss by 2050 → glacier-fed flow decline (Enguri, Rioni)
- Drought: eastern Georgia (Kakheti) projected drier; viticulture under stress
- Increased extreme rainfall + mudflow frequency in Greater Caucasus southern slope
- Heat: Tbilisi summer days > 35 °C projected to double by 2050 (NEA 2024 report)

---

## Section: `--mains`

### National database

- **GNERC (Georgian National Energy and Water Supply Regulatory Commission)**: `https://gnerc.org/en/` — utility tariffs + licensed operator registry
- **United Water Supply Company of Georgia (UWSCG / გაერთიანებული წყალმომარაგების კომპანია)**: `https://water.gov.ge/` — operates water + sewerage in **most regional cities** (excluding Tbilisi, Mtskheta-Mtianeti, Adjara)
- **Georgian Water and Power (GWP)**: `https://gwp.ge/en` — Tbilisi + Mtskheta + Rustavi water/sewer (private, BR Group)
- **Adjara**: water is run by the **municipal** utilities, not a single regional company — for Batumi this is **შპს ბათუმის წყალი / LLC Batumi Water** ([batumi.gov.ge/companies/14](https://batumi.gov.ge/companies/14)); for other Adjara municipalities identify the local operator. National operator elsewhere: **United Water Supply Company of Georgia** ([water.gov.ge](https://water.gov.ge/)) (2026 data, source batumi.gov.ge + water.gov.ge; 2026-09-18 verified)

### Major operators

| Operator | Coverage |
|---|---|
| **Georgian Water & Power (GWP)** | Tbilisi, Rustavi, Mtskheta — ~1.5 million people |
| **United Water Supply Company (UWSCG)** | Most other regional centres (Kutaisi, Telavi, Gori, Zugdidi, Akhaltsikhe, etc.) |
| **Adjara Water (აჭარისწყალი)** | Batumi + Adjara |
| Numerous small municipal/village systems | Rural settlements; many lack sewer |

### Verification

1. Check **municipality website** for water/sewer service maps; many small munis only publish service in tariff schedules
2. Listing language:
   - "ცენტრალური წყალი + კანალიზაცია" (centralised water + sewer) = full mains
   - "ჭაბურღილი" (chaburghili / borehole) = own well; verify potability + permit
   - "სანიტარული ჭა" / "ციფრო" (cesspit) = no mains sewer
3. **Tbilisi + Batumi + Kutaisi urban core**: full mains assumed; **verify with operator before signing**
4. **Villages and dachas in mtas (mountain settlements)**: often water-only or seasonal water; sewer rare

### Costs

| Scenario | Cost (US$) |
|---|---:|
| Connection to existing nearby mains (urban) | ~500–2,000 |
| Mains drain extension (parcel where trunk line exists nearby) | ~1,500–6,000 |
| Borehole drilling (50–100 m, common depth) | ~3,000–10,000 |
| Septic tank install (typical residential) | ~1,500–4,000 |
| Modern WWTP (BIO compliance) | ~5,000–15,000 |

> All US$ ranges are **est.** based on Tbilisi/Batumi 2024–2025 contractor quotes aggregated from MyHome.ge contractor classifieds + GWP connection-charge schedule. Verify with 2+ quotes per project.

### Utility tariffs (2025, regulated by GNERC)

| Utility | Tariff |
|---|---|
| **Electricity (Telasi/Energo-Pro residential, ≤101 kWh)** | ~0.15 GEL/kWh (~US$0.055) |
| **Electricity (101–301 kWh)** | ~0.18 GEL/kWh |
| **Electricity (>301 kWh)** | ~0.22 GEL/kWh |
| **Natural gas (residential, 5–500 m³)** | ~0.50–0.65 GEL/m³ depending on supplier (Wissol, SOCAR, Tbilisi Energy) |
| **Water (GWP Tbilisi)** | ~0.35 GEL/m³ (without meter: ~3.15 GEL/person/month) |
| **District heating** | Phased out post-Soviet; most apartments now individual gas boilers or electric |

(Tariffs verified against gnerc.org 2025 published schedules — confirm current rates.)

---

## Cost benchmarks (GE 2025–2026)

| Work | Cost (US$) |
|---|---:|
| NAPR extract (same-day) | ~2 |
| NAPR registration of sale | ~20–80 |
| Notarisation (optional) | 0.05–0.5 % of price |
| Real-estate agent (paid by seller normally) | 3–5 % |
| Building inspector (independent structural survey) | 200–800 |
| Asbestos test (single sample) | 50–150 |
| Radon test (3-month kit) | 50–200 |
| White-frame → finished apartment fit-out | 200–400 / m² |
| Roof replacement (terracotta, 200 m²) | 8,000–18,000 |
| Full apartment renovation (Tbilisi mid-range, 80 m²) | 15,000–35,000 |
| Septic to mains connection | 1,500–6,000 |
| Annual property tax (residential, Tbilisi, owner prior-year household income under 100k GEL) | 0.2 % × declared value |
| Annual property tax (residential, Tbilisi, owner prior-year household income ≥ 100k GEL) | 0.8 % × declared value |
| **Total transaction cost (buyer side, resale)** | **~0.1–0.5 % of price** |

> All contractor-cost ranges (roof, full renovation, building inspector, fit-out) are **est.** from 2024–2025 Tbilisi/Batumi contractor quotes — get 2+ quotes per job.

## Active fiscal incentives (2025)

- **Small Business Status (1 % on turnover)** — for IEs with turnover ≤ 500k GEL/yr
- **Micro Business Status (0 % income tax)** — for IEs with turnover ≤ 30k GEL/yr
- **Estonia-model CIT** — 0 % corporate tax until profit distribution (since 2017)
- **International Company status** (since 2020): 5 % CIT + 0 % dividend WHT for qualifying IT/maritime firms with substance in Georgia (Decree #619)
- **Free Industrial Zones (FIZ)**: Poti, Kutaisi (Hualing), Tbilisi — exemption from CIT, VAT, property tax for in-zone activity
- **Tourism Zones** (Anaklia, parts of Adjara): tax incentives + investment guarantees per region — verify per project
- **Short-term residence permit on real estate** at US$150k (US$100k before 1 March 2026); the separate 5-year investment residence permit needs US$300k
- **Renovation grants for heritage buildings (Tbilisi Old Town)**: Tbilisi City Hall "Tbilisi Loves You" programme — variable annual budget; co-financing for façade restoration

## Common listing platforms

- **MyHome.ge** — full extraction, largest portal *(per listing — verify with cadastre / on visit)*
- **SS.ge** — long-running classifieds *(per listing — verify with cadastre / on visit)*
- **Place.ge**, **Livo.ge**, **Korter.ge** *(per listing — verify with cadastre / on visit)*
- **Facebook Marketplace** + Telegram channels (`tbilisirent`, `batumirealestate`) — high volume, unverified
- **Aparthotel developer portals** (Wyndham, Orbi, Alliance, Next, Iveria) for Batumi seafront

## Caveats unique to GE

- **Foreigners CAN buy residential freehold without restriction** (since 1996) — among the most permissive globally
- **Foreigners CANNOT own agricultural land** (2018 constitutional ban Art. 19); pre-2017 foreign ag-land grandfathered
- **Transaction costs ~0.1–0.5 %** — among the world's lowest (no transfer tax, NAPR fee nominal)
- **No CGT after 2-year holding period** for individuals selling residential property
- **5 % flat PIT on residential rental** to natural persons (or 1 % under SBS for IE) — very low effective tax
- **NAPR cadastre is fast + cheap + bilingual GE/EN** — full title transfer can complete in 1 day at PSDA
- **"White frame" trap**: many new-builds sold as bare shells; budget +US$200–US$400/m² for finishing
- **Self-built (TPN) legalisation history**: pre-2007 unpermitted construction was waved through several legalisation rounds; some titles look clean but have no original building permit — affects future renovation
- **Soviet-era panel buildings** (1955–1991): asbestos + uneven seismic retrofit; commission independent structural survey
- **Heritage listing in Tbilisi Old Town** severely restricts renovation — check Cultural Heritage Agency register before signing
- **Currency**: most listings priced in **US$** but contracts denominated in **GEL** at NBG reference rate on signing day — exchange-rate exposure
- **2024 political situation**: EU accession effectively paused; "foreign agents" law in force; monitor before relying on EU-harmonisation expectations
- **Real-estate short-term residence permit threshold US$150k (US$100k before 1 March 2026)** is one of the lowest in the world — but permit doesn't grant tax residency automatically
- **Property tax (other than land tax) owed only if household income > 40,000 GEL/yr** (~US$14,800) — the 40k gate is a national Tax Code rule (per Revenue Service), not a municipal act, and exempts every property tax except land tax; many foreign owners on remote-work income outside the Georgian tax net pay 0 GEL on the dwelling. Above the gate, **Tbilisi** charges **0.2 %** of market value where prior-year household income is under 100k GEL and **0.8 %** at or above 100k GEL (Sakrebulo Ordinance №20-90 as amended by №6-19 of 26 Dec 2025) *(2026-08-07 verified, source Revenue Service + `https://matsne.gov.ge/ka/document/view/6734892`)*
- **Adjara 2 GEL/night tourist fee** for accommodation hosts (Batumi area) — verify current rate
- **Foreign Agents Registration Act (effective 31 May 2025)** — criminal-liability "foreign-principal" registration regime; **does NOT restrict private foreign property purchase**, but its registration duty reaches any person, companies and advisers included, acting for a foreign principal in political activities, as PR or political consultant, or as fund-raiser (Art. 1); breach carries a fine up to GEL 10,000 or up to 5 yr imprisonment (Art. 8 + Criminal Code Art. 355²), and since 4 Mar 2026 receiving a foreign grant without the required consent is a crime punishable by up to 6 yr (Criminal Code Art. 319¹); verify your transaction-stack counsel is not impaired *(2026-09-24 verified, source `https://matsne.gov.ge/en/document/view/6461578` + `https://matsne.gov.ge/ka/document/view/16426`)*
- **Mandatory travel medical insurance (effective 1 Jan 2026)** — Government Decree #602 of 26 Dec 2025 requires all foreign entrants to hold travel medical insurance with min **GEL 30,000** coverage for stay duration; cost typically US$10–US$40 per trip — verify carrier list at mfa.gov.ge *(2026-05-27 verified, source matsne.gov.ge)*
- **Labour-activity permit for working foreigners (effective 1 Mar 2026)** — labour-migration amendments (adopted 26 Jun 2025, **Law №862**) require a **right to labour activity** + labour residence permit or D1 visa for foreign workers engaged by a **local employer** and for **self-employed foreigners and entrepreneurs** beyond the visa-free year; registrations active on 1 Mar 2026 have until **1 Jan 2027** (**GEL 2,000** on the employer per worker AND **GEL 2,000** on the worker/self-employed foreigner, doubled on repeat). **Remote work for a foreign employer is NOT caught** (Law №1509 of 15 Apr 2026); Art. 60 temporary-stay-right exemption in force 1 Sep 2026 *(2026-08-07 verified, source Parliament of Georgia + `https://matsne.gov.ge/ka/document/view/2806732`)*

## Reddit / forum sources

- **r/Sakartvelo** (Georgia general, Georgian-English mix)
- **r/tbilisi**, **r/Batumi** (city-specific)
- **r/georgiarepublic**, **r/expatsingeorgia**
- **Facebook**: "Expats in Tbilisi", "Foreigners in Georgia", "Tbilisi Apartments for Rent", "Batumi Real Estate"
- **Telegram**: `t.me/tbilisirent`, `t.me/batumi_real_estate` (high volume; classifieds; never authoritative)
- Expat blogs: **EmergingEuropeRealEstate**, **InvestInGeorgia.org** (think-tank)

## Verification authorities

| Authority | When to call / visit |
|---|---|
| **NAPR (National Agency of Public Registry)** | Title extract, encumbrances, cadastral verification — visit any PSDA Public Service Hall |
| **PSDA (Public Service Development Agency / სახელმწიფო სერვისების განვითარების სააგენტო)** | One-stop hall for NAPR + civil registry + visa + IE registration |
| **Revenue Service (rs.ge)** | Tax residency, SBS application, VAT registration |
| **Notarial Chamber of Georgia** | Notarisation of contracts (optional) |
| **Heritage Agency (heritagesites.ge)** | Heritage-listed building check (Old Town Tbilisi, Sighnaghi, Mestia) |
| **Tbilisi / Batumi / Kutaisi Sakrebulo** | Local property-tax rates, zoning, building permits |
| **GWP (Tbilisi) / UWSCG (regions) / Adjara Water (Batumi)** | Mains water + sewer connection verification |
| **Telasi / Energo-Pro Georgia** | Electricity connection + tariff |
| **National Environmental Agency (NEA)** | Geohazard certification (parcel-level on request) |
| **Cultural Heritage Agency** | Old Town building restrictions |
| **MFA (mfa.gov.ge)** | Visa-free eligibility, residence permit pathway |

## Quirks to know

- **Cadastral code format `XX.XX.XX.XXX`** (region.district.block.parcel) — every property has one; ask for it before any other paperwork
- **PSDA same-day NAPR transfer**: title transfer can legally complete in **1 hour** for express fee — among the world's fastest cadastres
- **"Amkhanagoba" (ამხანაგობა)**: Georgian equivalent of HOA/condo association — bylaws can restrict STR, alterations, pet ownership; obtain bylaws before signing
- **Tbilisi addresses sometimes use district + micro-district + street** (e.g., "Saburtalo, IV მკრ., კოსტავა 27") — confirm the cadastral code, not just the street address
- **"Italiuri ezo" (Italian courtyard)**: traditional Tbilisi balcony-courtyard apartment block; charming but typically pre-1921, weak seismic performance, tricky shared-wall rules
- **VAT trap on new-build**: confirm "DDS-iani" (with VAT included) vs "DDS-is gareshe" (without) — 18 % swing on advertised price
- **Khinkali test**: any seller insisting "we don't need a NAPR extract, trust me" — walk away; NAPR is free and 1-day

## Source URL templates

| Source | URL pattern |
|---|---|
| NAPR public viewer | `https://www.napr.gov.ge/` |
| SDA service hall (Public Service Development Agency, ex-PSDA) | `https://sda.gov.ge/en/` |
| Revenue Service | `https://www.rs.ge/` |
| Geostat real estate stats | `https://www.geostat.ge/en/modules/categories/214/real-estate-price-statistics` |
| NBG financial stability | `https://nbg.gov.ge/en/page/financial-stability-report` |
| MyHome.ge search | `https://www.myhome.ge/en/s/<city>` |
| SS.ge real estate | `https://home.ss.ge/en/real-estate/l/<city>` |
| Korter.ge new build | `https://korter.ge/<city>` |
| Roads Department | `https://www.georoad.ge/` |
| NEA hazard portal | `https://nea.gov.ge/En` |
| CENN geohazard atlas | `http://drm.cenn.org/` |
| Institute of Earth Sciences & National Seismic Monitoring Centre (Ilia State Uni) | `https://ies.iliauni.edu.ge/` |
| Cultural Heritage Agency | `https://heritagesites.ge/` |
| GNERC tariffs | `https://gnerc.org/en/` |
| GWP Tbilisi water | `https://gwp.ge/en` |
| UWSCG regional water | `https://water.gov.ge/` |
| Adjara water (municipal) | Batumi: `https://batumi.gov.ge/companies/14` · national operator: `https://water.gov.ge/` |
| MFA visa info | `https://mfa.gov.ge/en/visa-information` |
| eMigration / residence | `https://sda.gov.ge/` |
| Tbilisi City Hall | `https://tbilisi.gov.ge/` |

## Status

✅ **Fully populated** as of 2026-05-01.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats. Foreign-buyer rules + visa pathways verified against MFA + Civil Code references.
**Confidence**: HIGH for cadastre + tax + foreign-buyer rules (NAPR + Tax Code + Constitution Art. 19 are primary statutory sources, multi-source corroborated). MEDIUM for short-let regulation (no national STR statute as of 2025; Tbilisi/Batumi rules in flux) and for parcel-level geohazard data (NEA + CENN are commune/district-level — parcel certification requires NEA Geological Service request).
**Last verified**: 2026-08-07 (`--tax` only: Tbilisi property-tax schedule re-verified against Sakrebulo Ordinance №20-90 of 30 Dec 2014 as amended by Ordinance №6-19 of 26 Dec 2025 — instrument mis-citation and the under-100k rate corrected; all other sections last verified 2026-05-27; seismic, Adjara water and service-hall authority names corrected 2026-09-18 per ies.iliauni.edu.ge + batumi.gov.ge + sda.gov.ge). Visa-free instruments (Ordinances №255 / №256 and the №122 amendment) re-checked 2026-09-24 in the October regwatch wave; Gulf-permit rule substance secondary only. 2026-09-24: Foreign Agents Registration Act line re-verified against the consolidated FARA text (matsne 6461578, Arts. 1, 8, Law №1292 amendment) and Criminal Code Arts. 355² and 319¹ (matsne 16426); the JV-specific claim was removed as unsupported by the Act's text (November regwatch wave, run early). Finance / visa tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

## Extension TODOs (deepen on first real run)

- [ ] Per-Tbilisi-district property-tax coefficient extraction (Sakrebulo decisions per year)
- [ ] Adjara tourist-fee current rate confirmation + Tbilisi Sakrebulo STR draft tracking
- [ ] Heritage Agency listed-building cadastral-code lookup workflow
- [ ] Aparthotel revenue-share contract review template (Batumi)
- [ ] Foreign-ownership ag-land grandfathering audit (pre-2017 acquired plots)
- [ ] Self-built legalisation status check (TPN waves) for pre-2007 buildings
- [ ] Real-estate short-term-residence-permit transition confirmation (who may still apply at US$100k after 1 March 2026 — PSDA / sda.gov.ge; US$150k threshold itself confirmed in Law Art. 15(j))
- [ ] NEA parcel-level geohazard certification request walkthrough
