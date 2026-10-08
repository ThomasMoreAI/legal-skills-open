# Faroe Islands 🇫🇴 — Property Due-Diligence Playbook

ISO2: `fo`. Status: ✅ Standalone playbook (Denmark autonomous territory under Self-Government Act 1948 / Home Rule 2005). Faroe is NOT part of the EU (excluded from Denmark's EU accession via Protocol 2); it IS in the Nordic Council, Schengen by Nordic Passport Union, and EFTA-adjacent via fisheries agreements. Currency: Danish Krone (DKK) — Faroese Króna (FOK) banknotes are issued by Landsbanki Føroya as DKK-equivalent notes (not a separate currency; 1:1 with DKK, no FX risk).

## Country profile

- Postcode pattern: 3 digits (`XXX`) — Tórshavn 100, Klaksvík 700, Tvøroyri 800, Vágar 380
- Municipality (kommuna): 29 municipalities post-2017 merger; codes used in cadastre (verify on government.fo)
- Geocode: [`https://kortal.fo/`](https://kortal.fo/) (Faroese national geo-portal) — address search + cadastre overlay
- Currency: DKK (Danish Krone); Faroese Króna (FOK) banknotes = DKK 1:1, no FX risk for DKK-area buyers
- Language: Faroese (official); Danish (universal); English widely spoken in Tórshavn but Faroese dominates legal docs
- Cadastre: [matrikkulin.fo](https://www.us.fo/matrikul/) — Faroese cadastre under Umhvørvisstovan (Environment Agency)
- Land registry: Tinglýsingin under the Sorinskrivarin (Office of the Court Clerk / Bailiff); head of government is the **Løgmaður** (Prime Minister)
- Time zone: WET / WEST (Western European, UTC+0 / UTC+1 DST)

## Section: `--price`

**Data sources** (priority order — primary first):

1. **Hagstova Føroya (Statistics Faroe Islands) — authoritative quarterly house price index**:
   - [hagstova.fo/en/economy/prices/number-sold-houses-and-prices](https://hagstova.fo/en/economy/prices/number-sold-houses-and-prices) — number of sales + average prices, broken down Tórshavn / towns / villages
   - News releases: [hagstova.fo/en/news](https://hagstova.fo/en/news) (filter "house prices")
   - Data sourced from public registration figures (tinglýsing) — includes ALL house sales, not a sample
2. **Bank-published quarterly indices** (cross-check):
   - Betri Banki house-price report (quarterly) — DKK-denominated; dissemination via Hagstova news bulletin
3. **Listing platforms** (live asks, not closed transactions):
   - [bugv.fo](https://bugv.fo/en) — primary Faroese listing portal (Faroese + EN UI)
   - [skyn.fo](https://www.skyn.fo/) — real-estate agency
   - [meklarin.fo](https://www.meklarin.fo/) — broker network
   - [Betri Heim](https://www.betriheim.fo/) — brokerage of the Betri group (Betri Banki), formerly betri-fastogn.fo
4. **WebSearch fallback**: `"<bygd or kommuna>" hús til sølu` (Faroese) or `"Faroe Islands" house for sale <area>` (English)

**Anchor values** (2022 data, Hagstova news bulletin "House sales decline as prices shoot up across the country"; verify against newest bulletin):

- Tórshavn average dwelling house: **DKK 3.9 million** (2022)
- Towns (Klaksvík, Runavík, Tvøroyri, Vágar, etc.): **DKK 2.2 million** (2022)
- Villages (bygdir): **DKK 1.8 million** (2022)
- **271 total dwelling-house sales** in 2022 — lowest in 10 years; segment split: Tórshavn 82, towns 90, villages 99

**Price growth — long window (15 years, 2007 → 2022)** — Hagstova 2023-03-30 bulletin headline figures:

- Tórshavn: **+70%** (DKK 2.3M → DKK 3.9M)
- Towns / small cities: **+81%** (DKK 1.2M → DKK 2.2M)
- Villages: **+75%** (DKK 1.0M → DKK 1.8M)

**Price growth — short window (~10 years, ~2010 → ~2020)** — separately cited Hagstova figure, narrower window:

- Tórshavn: **+35%**
- Towns: **+15%**
- Villages: **+16%**
- *Window given as ~2010–2020 in the source bulletin (exact decade boundaries not stated); verify against the specific Hagstova news release referenced.*

Data excludes **apartment buildings** (Hagstova caveat) — apartment-only sales not in this index.

Source: [hagstova.fo news bulletin (2022)](https://hagstova.fo/en/news/house-sales-decline-prices-shoot-across-country) and [capitals-house-prices-continue-soar](https://hagstova.fo/en/news/capitals-house-prices-continue-soar) — figures may have changed since; verify newest at hagstova.fo/en/news.

**Compute**:

- Price/m² = listing ask / surface m² (cadastral surface from matrikkulin.fo, NOT listing surface for primary calc)
- Tórshavn central price/m² inferred range: ~DKK 25,000–40,000/m² for ~100–150 m² typical detached; sparse public data — use listing comp set of 5+ recent sales for any specific district (Argir, Hoyvík, Hvítanes etc.)
- Walk-away price = listing × (1 − reasonable_discount). Faroese market is thin (200–400 transactions/yr nationally) — discount room highly seller-dependent; 3–8% typical from ask, less in Tórshavn central

**Caveats**:

- Hagstova averages are annual; quarterly granularity less reliable due to small sample (<100 sales/quarter in many segments)
- Tórshavn vs "towns" vs "villages" is the official Hagstova segmentation — there is no commune-level price index per kommuna
- Listing surface includes outbuildings (skúr, kjallari) in non-standard ways — verify Bruttoetageareal (BTA) per cadastre
- Very thin market: many properties sell "off-market" via family / neighbour networks before listing publicly

---

## Section: `--traffic`

**Data sources**:

- [Landsverk](https://www.landsverk.fo/) — Faroese national road authority (Public Roads & Tunnels); publishes traffic counts on main arterial roads + tunnels
- Tunnel-specific counts (Eysturoyartunnilin, Sandoyartunnilin, Vágatunnilin) reported in annual reports
- OSM Overpass for road class + `ref` + `maxspeed`

**Compute / context**:

- Total Faroese road network is ~960 km; main spine via subsea tunnels + ferry to remote islands
- TMJA on most rural Faroese roads is very low: <500 v/d on most non-tunnel routes
- Subsea tunnels are tolled (Eysturoyar / Sandoyar / Vága); toll = ~DKK 105–150 per car (verify at [tunnil.fo](https://www.tunnil.fo/))
- Sheep on roads: common rural hazard; not a traffic-volume issue but a driving-condition signal

**Verdict bands for rural FO** (calibrate to Faroese baseline):

- 🟢 < 100 v/d
- 🟡 100–500 v/d
- 🟠 500–2,000 v/d
- 🔴 > 2,000 v/d (Tórshavn ring / tunnel approaches only)

---

## Section: `--tax`

⚠️ **Limited English primary sources.** Many figures below cite [taks.fo](https://www.taks.fo/) Faroese pages where the English mirror is incomplete. Where the EN page is silent, the verification path is the Faroese page or direct call to TAKS.

**Data sources** (primary first):

1. **TAKS (Faroese Tax Administration)** — [taks.fo](https://www.taks.fo/) — tax authority; English mirror at [taks.fo/en/](https://www.taks.fo/en/individuals/tax/taxation-in-the-faroe-islands)
2. **Norden / Info Norden** — [norden.org/en/info-norden/tax-faroe-islands](https://www.norden.org/en/info-norden/tax-faroe-islands) — Nordic Council reference (cross-check)
3. **Nordisk eTax** — [nordisketax.net/pages/en-GB/faroe-islands/](https://nordisketax.net/pages/en-GB/faroe-islands/) — Nordic tax cooperation portal
4. **EURAXESS Faroe** — [euraxess.fo/faroe-islands/information-assistance/taxation](https://www.euraxess.fo/faroe-islands/information-assistance/taxation) — researcher-oriented (good EN summary)
5. **Global Expansion 2019 country guide** (PDF) — secondary aggregator referencing TAKS structure; used as cross-check

### Income tax

**Two-tier structure**: national tax (progressive) + municipal tax (**kommunalskattur**, flat, varies per kommuna).

**National progressive bands** (per [EURAXESS Faroe Taxation](https://www.euraxess.fo/faroe-islands/information-assistance/taxation); cross-checked Wikipedia / Norden):

- **DKK 0 – 65,000**: 0% (personal allowance)
- **Mid-band**: progressive tax rate increasing — **two same-tier sources disagree on the floor**:
  - **EURAXESS Faroe**: increasing **from 13% to 30%** on income above DKK 65,000
  - **Global Expansion 2019 PDF**: increasing **from 15% to 30%** on the remaining income
  - *(both secondary; ceiling 30% agrees; floor 13% vs 15% gap — `verify at taks.fo for 2026 rates` or call TAKS direct)*
- **DKK 330,000+**: fixed DKK 44,500 on the first DKK 330,000 + 25% on the remainder up to DKK 800,000 (both sources agree)
- **Above DKK 800,000**: top marginal applies (verify exact rate with TAKS — historical Wikipedia ref "20% on incomes up to DKK 500,000" is OUT-OF-DATE; EURAXESS supersedes)
- Verify current 2026 bands at [taks.fo](https://www.taks.fo/) (Faroese) or call TAKS +298 35 26 00

**Municipal tax (kommunalskattur)** (flat, per kommuna) — **two same-tier sources disagree on the ceiling**:

- **EURAXESS / Norden (2024–2025 data, per draft research)**: **16–23%**
- **Global Expansion 2019 PDF**: **16–22%**
- The 23% upper bound likely reflects a 2024–2025 kommuna rate increase relative to the 2019 figure; the specific ceiling-raising kommuna is not named in EN aggregator sources. `verify highest-rate kommuna at taks.fo for 2026 rates`.

**Church tax** (for members of the Fólkakirkjan / National Church): **0.6–0.9%** of income exceeding DKK 30,000 (EURAXESS, 2024–2025 data — verify at taks.fo for 2026 rates)

**Child deductions**:

- National: DKK 9,200 (child under 7), DKK 6,500 (child 7–18)
- Municipal: DKK 4,500–10,000 (per kommuna)
- (EURAXESS, 2024–2025 data — verify at taks.fo for 2026 figures)

**Combined marginal rate** (national + municipal, top): inferred **~46–53%** at top bands (= ~30% national + 16–23% municipal); verify at TAKS

### Capital gains on property

- **Primary residence**: structural framework suggests primary-residence exemption (mirrors DK "parcelhusreglen" pattern), but exact Faroese rule + holding-period threshold: `data not publicly available in English — verify at taks.fo (Faroese) or TAKS direct` **(LOW confidence — see Status)**
- **Investment property / second home**: capital gains generally taxable as ordinary income; verify holding-period rules and any indexation at TAKS **(LOW confidence)**
- Source framework: cross-referenced via [Nordisk eTax — Faroe Islands](https://nordisketax.net/pages/en-GB/faroe-islands/) and EURAXESS Faroe; EN-language detail is thin — this is one of the most important fields to verify directly with TAKS before any investment transaction

### Property / wealth taxes

- **Property tax (grunnskattur (FO) / grundskat (DK form sometimes used in EN aggregators) / kommunal property charge)**: Faroese kommunas levy a property charge on the land/buildings — rate set by each kommuna. Reported range **0.2–0.5%** of registered value (secondary source — Norden / aggregator only; verify with specific kommuna) **(LOW confidence on specific rate — see Status)**
- **No national property value tax** (differs from DK ejendomsværdiskat which does NOT apply in FO)
- **No wealth tax** in the Faroe Islands (matches DK position)

### Transfer / stamp duty

- **Tinglýsingargjald (registration fee on deed)**: structural fee on registering the deed (skøde) at the Tinglýsing — exact 2026 rate: `data not publicly available in English`; reported as a percentage-of-value fee plus a fixed administrative element. Verify at [tinglysing.fo](https://www.tinglysing.fo/) or via the lóggildur advokátur handling the transaction **(LOW confidence on specific rate — see Status)**
- **No separate state transfer tax** beyond the tinglýsingargjald (verify at Sorinskrivarin)

### VAT (MVG / meirvirðisgjald)

- **Standard rate: 25%** (TAKS primary — [taks.fo/en/business/vat/general-about-vat](https://www.taks.fo/en/business/vat/general-about-vat); matches DK rate; applies broadly to new build, materials, professional services)
- **No reduced rate** for residential construction in standard scenarios — verify at taks.fo MVG section

### Inheritance / gift tax

- Faroese rule diverges from DK in places — verify at taks.fo Faroese page or via Faroese solicitor
- Bullet detail: data not publicly available in English — `verify at taks.fo (Faroese) or Sorinskrivarin`

**Compute** (worked example, ~DKK 3.0M Tórshavn detached):

- Purchase price: DKK 3,000,000 (illustrative)
- Tinglýsing fee: ~DKK est. — verify rate at Sorinskrivarin
- Solicitor (lóggildur advokátur): ~DKK 15,000–30,000 (est. — verify quote)
- Annual municipal tax (kommunalskattur) on income: 16–23% on assessed income (not on property)
- Annual property charge (kommuna): ~DKK 6,000–15,000 (est. = 0.2–0.5% × DKK 3.0M; verify with specific kommuna)
- VAT (MVG) on any new-build / contractor invoices: 25%

**Caveats**:

- All numeric rates above marked `est.` REQUIRE verification with TAKS or the kommuna before transaction
- Faroese tax law is independently legislated from Danish — do NOT assume DK rates apply
- 2026 rates: verify Q1 2026 publication on taks.fo (Faroese pages often more current than English mirror)

---

## Section: `--rental`

⚠️ **Thin rental data.** Faroe is not a major STR market by global standards; tourism is real but seasonal (May–September dominant).

**Data sources**:

- [visitfaroeislands.com](https://www.visitfaroeislands.com/) — official tourism board (Visit Faroe Islands)
- [airbnb.com/s/Faroe-Islands](https://www.airbnb.com/s/Faroe-Islands) — listing inventory
- [hagstova.fo/en/business/tourism](https://hagstova.fo/en/business/i-accommodation-and-food-service-activities/accommodation) — overnight stays statistics
- Faroese rental law: Lóggáva um leigu (rental act) — administered via [logir.fo](https://logir.fo/) (legal database)

**Long-term rental regime**:

- Tenant protection moderate — Faroese rental law mirrors Nordic security-of-tenure principles but with own statute
- Rent control: not standard; market-rate negotiation typical
- Verify current statute via logir.fo search "leiga" or via Faroese solicitor

**Short-term let (STR)**:

- Tourist accommodation tax / regulation: Visit Faroe Islands publishes operator registration guidance — verify current at visitfaroeislands.com/professionals
- Sustainable-tourism cap: Faroe runs periodic "closed-for-maintenance" volunteer campaigns; STR licensing tightened post-2022 in Tórshavn area — verify with Tórshavn kommuna
- Peak season (June–August): ~80–90% occupancy typical Tórshavn; off-season (Nov–Feb): <30% (anecdotal aggregator data — `verify with operator returns`)

**Tax**:

- STR income taxed as ordinary income (municipal + national); see `--tax`
- Operator must register for MVG (VAT) above DKK 50,000 turnover (Faroese threshold — verify at taks.fo)

**Caveats**:

- Faroese tourism is weather-dependent + capacity-constrained (limited daily flights, ferry seats)
- Many "Faroese rentals" listed on Airbnb are operated by Tórshavn/Klaksvík residents informally — formalisation expected as regulation tightens

---

## Section: `--work`

**Sectors with real foreign-worker demand**:

- **Salmon farming / aquaculture**: Bakkafrost, Hiddenfjord, MOWI Faroes — engineers, biologists, technicians
- **Fisheries / processing**: Faroe Origin, Pelagos, P/F Vón — operations + maintenance
- **Telecoms / IT**: Føroya Tele, Hey, P/F Vatnsføroya — software + network engineers
- **Tourism / hospitality**: seasonal + permanent in Tórshavn / Vágar (airport)
- **Healthcare**: Landssjúkrahúsið (national hospital, Tórshavn) — recruits internationally
- **Maritime**: Faroese fleet + offshore service (Atlantic Petroleum legacy)

**Job boards**:

- [job.fo](https://www.als.fo/storv/) — main Faroese job board
- [ALS — Arbeiðsloysisskipanin](https://www.als.fo/storv/) — statutory unemployment-insurance body; runs the public job-placement service (*arbeiðsávísingin*) and the job board at [starv.fo](https://starv.fo/). Successor to Arbeiðsstovan (2026 data, source als.fo; 2026-09-18 verified)
- LinkedIn (Faroe Islands filter)
- [setur.fo](https://www.setur.fo/) — University of the Faroe Islands (academic jobs)

**Work permits**:

- Faroe is NOT in EU — EU/EEA free movement does NOT apply automatically
- Nordic Passport Union: Nordic citizens (DK / IS / NO / SE / FI) can live + work without permit
- Non-Nordic citizens: residence + work permit via Útlendingastovan (Faroese Immigration) — verify at [us.fo](https://www.us.fo/) and [government.fo](https://www.utlendingastovan.fo/en/home)
- Bakkafrost + major employers commonly sponsor permits

**Salary benchmarks** (data not publicly aggregated in EN):

- Verify at Hagstova labour statistics: [hagstova.fo/en/society/labour-market](https://hagstova.fo/en/society/labour/unemployment)

---

## Section: `--risks`

**Data sources** (primary first):

1. **Jarðfeingi (Faroese Earth & Energy Directorate)**: [jardfeingi.fo](https://www.jardfeingi.fo/) — geological survey; landslide + bedrock data
2. **Landsverk** (national infrastructure): road, rockfall, tunnel safety
3. **Veðurstovan (Faroese Met Office)**: [vedur.fo](https://www.vedur.fo/) — weather, storm warnings, sea state
4. **Umhvørvisstovan (Environment Agency)**: [us.fo](https://www.us.fo/) — coastal, water, air quality

**Risk categories**:

| Hazard | Severity profile |
|---|---|
| **Atlantic storms / wind** | 🔴 SEVERE — winds 30+ m/s common Oct–Mar; gusts >50 m/s documented; building envelope standards must meet Faroese wind code |
| **Fog** | 🟠 — sea fog very common, especially Vágar airport area; driving hazard year-round |
| **Coastal erosion** | 🟡 — basalt cliffs are resistant; sandy coastline limited (Sandur on Sandoy, parts of Tórshavn harbour) |
| **Coastal flooding / storm surge** | 🟡 — harbours and low-lying settlements (Vestmanna, Sørvágur) at storm-surge risk |
| **Pluvial flooding** | 🟡 — heavy rainfall + steep terrain → flash drainage issues in valleys (parcel-level: verify with kommuna planning) |
| **Landslide / rockfall** | 🟠 — steep basalt slopes; documented historical events (Skælingsfjall, Hattarvík). Parcel-level verification via Jarðfeingi |
| **Seismic** | 🟢 — very low; not a credible risk |
| **Radon** | 🟡 — basalt geology generally low; no national radon map equivalent to UK/IRL. `data not publicly available — verify at us.fo (Faroese)` |
| **Volcanic / tsunami** | 🟢 — geological lifespan extinct; no historical tsunami events recorded |
| **Snow / ice** | 🟡 — winter snow brief and rare at sea level; ice on tunnel approaches more relevant |

**Build-era hazards**:

- Pre-1970: wood frame + tarred-felt roofs (turf in older traditional houses); often poor insulation
- 1970–1990: concrete + steel construction common in Tórshavn / Klaksvík expansion
- Post-2000: modern envelope to Faroese building code; high wind-load standards
- Asbestos: present in 1960s–1990s builds; mandatory survey for pre-1990 demolition / major refit (verify with Umhvørvisstovan)

**Climate change projection**:

- Wind regime: storm frequency rising (Nordic Met cooperation projections); building code updated 2018 to reflect
- Precipitation: +5–15% wetter winters projected 2030–2050 (Faroese Met Office / Nordic CC outlook)
- Sea level: +0.3–0.6 m by 2100 (regional Nordic projection; verify with Veðurstovan)

---

## Section: `--mains`

**Data sources**:

- [SEV (Strong á Føroyum)](https://www.sev.fo/) — national electricity utility (publicly owned)
- Water utility per kommuna — Tórshavn: [torshavn.fo](https://www.torshavn.fo/), Klaksvík via Klaksvíkar kommuna
- Sewerage: kommunal responsibility — verify with relevant kommuna
- Telecoms: [Føroya Tele](https://www.ft.fo/) and [Nema](https://www.nema.fo/) (formerly Hey) — fibre rollout near-universal in Tórshavn + town centres; village coverage variable (2026 data, source ft.fo + nema.fo; 2026-09-18 verified)

**Electricity**:

- SEV is sole grid operator; ~50% renewable (wind + hydro) as of 2024 reporting; target 100% renewable electricity 2030
- Standard supply: 230 V / 50 Hz; Schuko-compatible plugs (Type F)
- Connection cost: data not publicly available — `verify with SEV`

**Heating**:

- District heating (fjarhitaveita) in Tórshavn central + parts of Klaksvík (verify coverage with kommuna)
- Outside DH zones: electric / oil / heat-pump (heat pumps increasingly common new-build)
- Oil heating: declining (decarbonisation policy); new oil installs restricted (verify current policy)

**Water**:

- Surface-water sourced from reservoirs (e.g. Eiðisvatn for Eysturoy + Streymoy network); generally soft, high quality
- Per-property charge: kommunal — verify with kommuna invoice

**Sewerage**:

- Tórshavn and major towns: collective sewer to harbour/coastal discharge (some with treatment, varying by kommuna)
- Bygdir (villages): individual septic or kommunal small-system common; verify with kommuna

**Telecom**:

- Føroya Tele incumbent; fibre near-universal Tórshavn / Klaksvík; villages variable
- Mobile: Hey, Vodafone, Føroya Tele (Tele) — 4G coverage extensive; 5G in capital + tunnels expanding

---

## Section: `--crime`

- **Overall**: extremely low; Faroese society small (~54,000 pop), strong social cohesion
- **Data source**: [Føroya Politi](https://politi.fo/) (Faroese Police; formerly logreglan.fo) — annual statistics page not located; Hagstova may not have a comparable EN report
- No meaningful violent crime rate at parcel level; property crime rare

---

## Section: `--amenities`

- Tórshavn (capital, pop ~22,000): full urban amenities — supermarkets (Bónus, Føroya Keypsfelag, FK, Miklagarður), hospital, university, theatre, sports halls, harbour
- Klaksvík (pop ~5,000): regional hub northern islands
- Smaller towns + villages: reduced services; ferry / tunnel connection critical
- Tunnel network: subsea tunnels Streymoy↔Vágar (Vágatunnilin, 2002), Streymoy↔Eysturoy (Eysturoyartunnilin, 2020), Streymoy↔Sandoy (Sandoyartunnilin, 2023) — connect ~85% of population to Tórshavn within 60 min

---

## Foreign-buyer rules (CRITICAL SECTION)

**Legal basis**: **Løgtingslóg um at keypa fastogn í Føroyum** ("Parliamentary Act on Purchase of Real Estate in the Faroe Islands"), enacted as [Løgtingslóg nr. 158 frá 10. desember 2021](https://logir.fo/Logtingslog/158-fra-10-12-2021-um-at-keypa-fastogn-i-Foroyum) — published 13 Dec 2021, in force the day after publication (§ 13 stk. 1); § 13 stk. 2 applies it to transfers lodged for registration after commencement (2021 statute, source logir.fo).

**Rule** (per the act as reported):

- **Permit-free purchase**:
  - Persons currently resident in the Faroe Islands
  - Persons who previously resided in the Faroe Islands for at least 5 years
  - Danish citizens resident elsewhere in the Kingdom of Denmark for at least 5 years
  - Companies or other legal persons with their head office (høvuðssæti) in the Faroe Islands (§ 1 stk. 2)
- **Permit required from the landsstýrismaður** (§ 2; logir.fo lists Løgmansskrivstovan as the responsible authority; delegable under § 11; no permit needed for inheritance, undivided estate, division of joint property or gifts in direct line, § 3; apply within 6 months of the final agreement, § 4) for all other foreign buyers, including:
  - EU/EEA citizens (Faroe is NOT in EU — no free-movement override)
  - Nordic citizens (DK/IS/NO/SE/FI) other than under the 5-year DK-resident rule
  - Holiday-home purchases by non-residents

**Permit criteria**: not exhaustively listed in published EN summaries — historical guidance suggests:

- Demonstrable connection to the Faroe Islands (family, employment, longstanding visits)
- Use case (primary residence > investment > pure holiday let)
- `verify at government.fo (Faroese pages) or via Faroese solicitor before transaction`

**Process** (per published Faroese practitioner guidance):

1. Sign conditional purchase agreement (subject to permit)
2. Solicitor files permit application with the relevant ministry
3. Permit issued OR refused — refusal forfeits the transaction; deposit treatment per contract
4. On permit: complete via tinglýsing of skøde at the local Sorinskrivari

**Sanctions for breach**: if a permit is refused or not applied for, the landsstýrismaður orders the owner to sell within 6 months to 1 year (§ 9); failing to apply in time or to obey the order is punishable by fine, and the court may set weekly coercive fines (§ 12).

**Comparison context**:

- This is STRICTER than EU norms but LESS strict than Greenland (Greenland passed similar legislation more recently — see `gl/playbook.md` when published)
- Pre-2021: Faroe was effectively open to all DK citizens without restriction; the December 2021 Løgtingslóg closed the holiday-home loophole

**Sources**:

- [local.fo coverage](https://local.fo/parliament-passes-legislation-to-restrict-foreign-ownership-of-real-estate-in-the-faroe-islands/)
- [local.fo regulatory expectations](https://local.fo/regulations-on-foreign-ownership-of-real-estate-in-faroe-expected-to-be-mild-rather-than-tough/)
- Primary statute: [Løgtingslóg nr. 158/2021 on logir.fo](https://logir.fo/Logtingslog/158-fra-10-12-2021-um-at-keypa-fastogn-i-Foroyum) — Faroese only
- Verification path: [government.fo](https://www.government.fo/en/) → Løgmansskrivstovan (responsible authority per logir.fo)

---

## Section: `--notary` / transaction process

**Roles**:

- **Lóggildur advokátur** (licensed Faroese advokat): handles purchase contract drafting, permit application (if foreign buyer), tinglýsing filing, escrow of purchase funds. Equivalent to a DK advokat — Faroese-trained or Danish-trained-with-Faroese-licence
- **Sorinskrivarin** (Office of the Court Clerk / Bailiff): operates the **Tinglýsingin** (Land Title Registry); registers the deed (skøde) and any mortgage charges
- **Real estate agent (ognarmeklari)**: not strictly required but common; commission typically 1.5–3% (verify current market practice — agent fee usually paid by seller)

**Process** (typical residential transaction):

1. **Offer + acceptance** (often via agent or directly)
2. **Conditional purchase agreement (keypssáttmáli)** — drafted by advokat; deposit typically 5–10% to escrow
3. **Foreign-buyer permit** (if applicable) — apply at this stage
4. **Financing condition** — bank approval (typical 30–60 day window)
5. **Diagnostic / inspection** (less formalised than EU norms — see `--mains` and `--risks` for areas to inspect)
6. **Completion + payment** of balance via solicitor escrow
7. **Tinglýsing** — advokat files the skøde at the Sorinskrivari; registration fee (tinglýsingargjald) payable
8. **Possession** — keys typically handed over on tinglýsing confirmation

**Document language**: Faroese standard. Buyers without Faroese should require certified Danish or English translation of key documents (skøde, keypssáttmáli, any mortgage charge) — verify cost with solicitor.

**Timeline**: 60–120 days from offer to completion typical; foreign-buyer permit adds 30–90 days.

---

## Section: `--finance` (mortgage / banking)

**Regulator**: **Finansieringseftirlitið** (Financial Supervisory Authority of the Faroe Islands) — [finansieringseftirlitid.fo](https://www.tryggingareftirlitid.fo/fo/english/about-us)

**Banks active in Faroe mortgage market**:

- **BankNordik** — largest; Faroese + Greenland + DK ops; full mortgage product line
- **Eik Banki** — Faroese-focused commercial + retail
- **Norðoya Sparikassi** — northern islands savings bank
- **Suðuroyar Sparikassi** — southern island savings bank
- **Betri Banki** — Faroese full-service (consumer + business)

**Foreign-buyer mortgage availability** — limited. Practical reality:

- Most Faroese banks require Faroese residency + Faroese-source income for residential mortgages
- Cross-border lending from DK banks possible but reduced product set
- Cash + 50%+ equity typical for foreign-buyer transactions; 80% LTV reserved for resident borrowers
- `verify with bank directly — foreign-buyer mortgage policy varies bank-by-bank`

**Rates** (typical 2025–2026 — verify current):

- Variable rate residential: ~4–6% (mirrors Nordic / DK rate environment)
- Fixed rate 5-yr: ~5–7%
- Source: Faroese banks publish rate sheets on their respective websites

**Mortgage tax / stamp on mortgage charge**:

- Registration of pant (mortgage charge) at Tinglýsing: fee structure mirrors deed registration; `verify at Sorinskrivari`

---

## Section: `--insurance`

- **Mandatory**: building insurance (brandtrygging) required by mortgage lenders; market-standard
- **Operators**: Trygd, Tryggingarfelag Føroya (TF), Føroya Lívstrygging — verify quotes locally
- **Wind / storm cover**: ESSENTIAL given Faroese wind regime; verify policy explicitly covers high-wind events
- **Flood**: typically included in standard building cover but verify storm-surge exclusion
- **Contents**: separate policy; not bundled

---

## Section: `--connectivity`

- **International air**: Vágar Airport (FAE) — only commercial airport. Atlantic Airways (Faroese flag carrier) + SAS seasonal; routes to Copenhagen (daily), Edinburgh / Reykjavík / Bergen / Paris / Barcelona (varies seasonally)
- **Ferry**: Smyril Line — Tórshavn ↔ Hirtshals (DK) ↔ Seyðisfjörður (IS), passenger + vehicle ro-ro
- **Domestic ferry**: Strandfaraskip Landsins (SSL) — inter-island routes to Sandoy / Suðuroy / Mykines etc.
- **Tunnels**: subsea tunnel network connects Streymoy + Vágar + Eysturoy + Sandoy
- **Roads**: well-maintained main spine; rural roads narrow + single-lane in places; sheep on roads ordinary

---

## Section: `--language`

- **Official language**: Faroese (Føroyskt) — North Germanic; closest living relative is Icelandic
- **Working language**: Danish universal (taught from primary school); English widely spoken in Tórshavn / tourism / business sectors; less so in rural bygdir
- **Legal documents**: Faroese only by default; translation to Danish or English available via certified translator
- **Apostille**: Faroe Islands fall under the Danish Hague Apostille framework — DK apostille issued via Danish MFA covers Faroe (verify with [um.dk](https://um.dk/) apostille service)

---

## Section: `--digital-nomad`

- **No dedicated digital-nomad visa**: Faroe Islands have no DNV programme
- **Nordic citizens**: can move + work via Nordic Passport Union with no visa
- **Non-Nordic EU/EEA**: require residence permit (no free-movement override — Faroe excluded from EU)
- **Long-stay**: Skammtíðarvistarlondi (short-term residence) up to 90 days visa-free for Schengen-eligible passports; longer requires permit via Útlendingastovan ([us.fo](https://www.us.fo/))
- **Connectivity**: fibre near-universal Tórshavn / Klaksvík; remote-work-friendly bandwidth
- **Cost of living**: high — Tórshavn rents ~DKK 8,000–15,000/mo for 2-bed; groceries +20–30% vs DK mainland (Hagstova / Numbeo cross-check)

---

## Country-specific quirks

- **DKK + FOK**: Faroese banknotes are legal tender in Faroe but NOT in mainland Denmark (must exchange at par at Faroese banks before traveling); coin set is shared DKK
- **No EU rules**: Faroe is outside EU customs union — imports from DK mainland subject to MVG + duty in some cases; impacts construction-material pricing
- **Sheep**: ~70,000 sheep on the islands (more than people); right-of-way disputes around grazing/parcel boundaries are real
- **Land below 700 m elevation**: most habitable parcels; above is grazing or uninhabitable
- **Common land (almenningur)**: many parcels border or include shares of common grazing land — historical Faroese tenure pattern; verify at matrikkulin.fo
- **Sunday closures**: most retail closed Sundays; legal/professional services Mon–Fri only
- **Faroese-only documents**: prepare for full translation cost; budget DKK 5,000–15,000 for full transaction document package

---

## Source URL templates table

| Topic | URL | Authority |
|---|---|---|
| Tax (TAKS) | [taks.fo/en](https://www.taks.fo/en/individuals/tax/taxation-in-the-faroe-islands) | Faroese Tax Authority |
| Cadastre | [matrikkulin.fo](https://www.us.fo/matrikul/) | Umhvørvisstovan |
| Land title | [tinglysing.fo](https://www.tinglysing.fo/) | Sorinskrivarin |
| Statistics | [hagstova.fo/en](https://hagstova.fo/en) | Statistics Faroe Islands |
| Government portal | [government.fo/en](https://www.government.fo/en/) | Faroese Government |
| Financial regulator | [finansieringseftirlitid.fo](https://www.tryggingareftirlitid.fo/fo/english/about-us) | FSA Faroe Islands |
| Met Office | [vedur.fo](https://www.vedur.fo/) | Veðurstovan |
| Geology / earth sciences | [jardfeingi.fo](https://www.jardfeingi.fo/) | Jarðfeingi |
| Environment / cadastre admin | [us.fo](https://www.us.fo/) | Umhvørvisstovan |
| Roads + tunnels | [landsverk.fo](https://www.landsverk.fo/) | Landsverk |
| Electricity utility | [sev.fo](https://www.sev.fo/) | SEV |
| Immigration | [us.fo](https://www.us.fo/) (and [government.fo/en/foreign-relations](https://www.utlendingastovan.fo/en/home)) | Útlendingastovan / Government |
| Legal database | [logir.fo](https://logir.fo/) | Government legal portal |
| Listings (main) | [bugv.fo](https://bugv.fo/en) | private |
| Tourism board | [visitfaroeislands.com](https://www.visitfaroeislands.com/) | Visit Faroe Islands |
| Police | [Føroya Politi](https://politi.fo/) | Faroese Police |
| Nordic tax portal | [nordisketax.net/faroe-islands](https://nordisketax.net/pages/en-GB/faroe-islands/) | Nordic Council |
| Info Norden | [norden.org/info-norden/tax-faroe-islands](https://www.norden.org/en/info-norden/tax-faroe-islands) | Nordic Council |

---

## Listing platforms summary

- **bugv.fo** — primary; EN UI available
- **skyn.fo, meklarin.fo, betriheim.fo** — agency portals
- **rightmove.co.uk/overseas-property/in-Faroe-Islands** — UK aggregator (sparse coverage)
- **Off-market via family/neighbour networks** — significant share of village transactions

---

## Reddit / forum sources for operator stories

- r/faroeislands — small but active (`community signal limited — Faroese community is small`)
- r/NordicCountries — broader Nordic context
- Visit Faroe Islands forum (visitfaroeislands.com community)
- Faroe Islands expat Facebook groups (private — search "Faroe Islands expats")
- Local.fo news + comment sections (English-language Faroese news)

---

## Caveats unique to FO

- **Anti-hallucination warning**: many primary sources (taks.fo, logir.fo, government.fo) have INCOMPLETE English mirrors — Faroese-language verification is often required for the final figure. EN tertiary sources (norden.org, ARAB MLS, Numbeo) are useful for orientation but MUST be verified against Faroese primary before transaction
- **Small-sample data**: ~200–400 property transactions/yr nationally → most "averages" have meaningful sampling error
- **Bank-by-bank policy** on foreign mortgages varies; do not assume Nordic norms transfer
- **MVG (VAT) on construction**: at 25%, materially affects renovation costs vs EU jurisdictions with reduced rates
- **Wind code**: Faroese building wind-load standard is among Europe's strictest; pre-2010 builds may NOT meet current code (verify with building inspector)
- **Common land (almenningur)**: historical tenure complications around hill / grazing parcel boundaries — engage local solicitor for any rural parcel
- **No EU recourse**: consumer protection + cross-border legal mechanisms (e.g., ECC-Net) do NOT apply; remedies are Faroese-court only

---

## Verification authorities

- **TAKS** (tax) — +298 35 25 00 / [taks.fo](https://www.taks.fo/)
- **Sorinskrivarin** (land registry) — verify via [tinglysing.fo](https://www.tinglysing.fo/)
- **Kommuna of property** — annual tax + connection confirmation
- **Faroese solicitor (lóggildur advokátur)** — transaction + permit handling
- **Útlendingastovan** (immigration) if non-Nordic buyer — residence-permit interaction with purchase permit

---

## Status

✅ **Standalone playbook populated** as of 2026-05-27.

**Confidence**: **LOW-MEDIUM** overall.

- **HIGH** for: foreign-buyer rule architecture (multi-source — local.fo English coverage + multiple confirming aggregators); Hagstova property-price anchors (2022 official statistics, Tavily-verified); VAT/MVG rate 25% (TAKS primary source verified).
- **MEDIUM** for: municipal tax (kommunalskattur) range (EURAXESS / Norden 16–23% vs Global Expansion 2019 16–22% — same-tier aggregator disagreement, specific kommuna ceiling not verified); national progressive band floor (EURAXESS 13→30% vs Global Expansion 2019 15→30% — same-tier disagreement).
- **LOW** for: capital gains on property holding-period rules (no English primary source); tinglýsingargjald specific rate (English source unavailable; DK reference rate 1.25% from 1 Jan 2026 likely NOT applicable as Faroe legislates independently); property tax / kommunal property charge specific rate (only secondary aggregator estimate 0.2–0.5% — verify with kommuna).

**Last verified**: 2026-05-27 (employment-service body and telecom operator list corrected 2026-09-18 per als.fo + ft.fo + nema.fo). Ownership tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

### Regulatory-watch follow-up (on PR merge)

On promotion out of `_local/`, the following entries must be added to `shared/regulatory-watch.md`:

1. **Faroe Islands — Løgtingslóg on real-estate purchase**: country `FO`, topic "foreign-buyer purchase permit", statute [Løgtingslóg nr. 158 frá 10. desember 2021 um at keypa fastogn í Føroyum](https://logir.fo/Logtingslog/158-fra-10-12-2021-um-at-keypa-fastogn-i-Foroyum) (Løgtingið vote 7 Dec 2021 · signed 10 Dec 2021 · published 13 Dec 2021 · in force 14 Dec 2021 per § 13 stk. 1; § 13 stk. 2 grandfathers pre-14-Dec-2021 transactions in flight), source logir.fo primary + kvf.fo + dagur.fo cross-confirmation, verified date 2026-05-27, revisit-cadence "annual", impact tier 2, affected sections: foreign-buyer / `--notary` / `--finance`.
2. **Faroe Islands — Faroe NOT in EU (re-affirmation)**: country `FO`, topic "EU jurisdiction exclusion", source government.fo Home Rule Act + OECD 2023 Global Forum + US State.gov 2025 Investment Climate, verified date 2026-05-27, revisit-cadence "5-year (stable)", impact tier 3, affected sections: foreign-buyer / `--work` / `--digital-nomad`.

## ⚠️ Run quality notes

During the research run for this playbook:

- **TAKS English mirror** ([taks.fo/en](https://www.taks.fo/en/individuals/tax/general-information-about-income-tax-in-the-faroe-islands)) does not publish current-year progressive band thresholds in detail; EURAXESS Faroe taxation page provided the most specific EN breakdown (DKK 65,000 allowance, 13→30% progressive, DKK 44,500 fixed + 25% above DKK 330,000). The Global Expansion 2019 PDF disagrees on the floor (15%, not 13%) and on the municipal ceiling (22%, not 23%); both are same-tier secondary sources. Verification path is the Faroese TAKS page or direct TAKS call (+298 35 26 00).
- **Hagstova fetch** of `/economy/prices/number-sold-houses-and-prices` returned a dynamically-loaded table (data not in raw HTML); the DKK 3.9M / 2.2M / 1.8M anchor was verified via the news bulletin "[House sales decline as prices shoot up across the country](https://hagstova.fo/en/news/house-sales-decline-prices-shoot-across-country)" (2022 data, validator Tavily-confirmed verbatim). The 15-yr (+70/+81/+75%) and 10-yr (+35/+15/+16%) windows are now labelled separately; the 10-yr figure is sourced to a separate Hagstova bulletin reference — verify exact decade boundaries against the original release. The Hagstova StatBank ([statbank.hagstova.fo](https://statbank.hagstova.fo/pxweb/en/H2/)) is the verification path for newer figures.
- **Foreign-buyer law verified 2026-05-27**: [Løgtingslóg nr. 158 frá 10. desember 2021 um at keypa fastogn í Føroyum](https://logir.fo/Logtingslog/158-fra-10-12-2021-um-at-keypa-fastogn-i-Foroyum) — Løgtingið passed it on **7 December 2021** (per kvf.fo + dagur.fo), statute dated **10 December 2021**, published (kunngjørd) **13 December 2021**, entered into force **14 December 2021** per § 13 stk. 1 ("Henda løgtingslóg kemur í gildi dagin eftir, at hon er kunngjørd"). § 13 stk. 2 grandfathers pre-14-Dec-2021 transactions tendered for registration. The earlier "13 December 2021" wording referred to the publication date, not the statute date. Buyers should still request the current consolidated text via their Faroese solicitor in case of post-2021 amendments — re-verify at the logir.fo URL.
- **Wikipedia tax page** quotes "20% government tax on incomes up to DKK 500,000" — this contradicts EURAXESS's DKK 65,000 / 13–30% progressive bands. EURAXESS is more recent and more granular; Wikipedia appears stale and was not used.
- **Tinglýsingargjald** specific 2026 rate: no English primary source located. Do NOT assume Danish 1.25% (from 1 Jan 2026) applies — Faroe legislates independently. Verify with Sorinskrivari or via the Faroese advokat handling the transaction.
- **Reddit** was not run during validation (budget + thin-signal — Faroese community is small). Future maintenance run may use the `reddit-fetch` skill; not blocking for promotion.
- **`guidetofaroeislands.fo`** foreign-buyer process page returned 404 during this run.

---

## ⚠️ Verification responsibilities

This report aggregates publicly accessible data and clearly-labelled estimates. **Before signing**, the buyer must independently verify:

1. **Foreign-buyer permit requirement** — confirm with Faroese solicitor and Løgmansskrivstovan (responsible authority per logir.fo); the 2021 law requires permits for non-resident, non-Nordic-DK-5-year-resident buyers
2. **Tax figures** — request the seller's most recent annual tax bill; confirm specific kommuna municipal rate (kommunalskattur) at taks.fo; resolve the EURAXESS-vs-Global-Expansion floor/ceiling gap against TAKS direct
3. **Risk disclosures** — pull parcel-level geological/landslide data from Jarðfeingi; confirm wind / flood / storm-surge profile with Veðurstovan and the kommuna
4. **Mains connections** — telephone the kommuna for parcel-level water + sewer status; confirm electricity capacity with SEV
5. **Building condition** — commission an independent surveyor for any pre-2000 build; wind-code compliance is parcel-critical in Faroe
6. **Listing claims** — anything from the seller's listing (surface, year, energy rating, condition) must be re-verified with matrikkulin.fo cadastre and a physical visit
7. **Mortgage availability** — confirm with bank IN ADVANCE; foreign-buyer mortgage products are bank-by-bank policy

**This report is decision-support, not legal/tax advice.** AI-assisted aggregations contain risk of error. Critical figures must be confirmed with primary sources or qualified professionals.

---

*Generated by `/property-deep-dive` on 2026-05-27. Confidence levels per section above.*
