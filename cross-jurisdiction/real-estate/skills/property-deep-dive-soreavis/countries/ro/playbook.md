# Romania (RO) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: RON (free-floating; ~4.97 EUR/RON Apr 2026; **not in eurozone**, no firm target — fiscal deficit blocks ERM-II entry)
**Lang**: Romanian; English at top banks/legal firms; AMCCRS Bucharest seismic data Romanian-only

---

## Country profile

Romania (~19M pop) joined EU 2007 and **completed full Schengen integration 1 Jan 2025** (air/sea was 31 Mar 2024). Major 2025-26 reforms hit hard: **VAT 19% → 21% (1 Aug 2025)**, local property tax baseline +79% (1 Jan 2026, Lege 239/2025), special tax on luxury 0.3% → 0.9% (1 Jan 2026). **Bucharest seismic risk is the country-defining due-diligence concern** — Vrancea zone generates intermediate-depth M6.5–7.5 events; ~350 buildings classed Rs I (highest collapse risk). District heating crisis (Termoenergetica, was RADET — bankrupt 2019) affects most Bucharest panel-block buyers.

---

## Section: `--price`

**Primary index**: **INS (Institutul Național de Statistică)** — quarterly HPI (IPL)
- https://www.insse.ro/ (**permanent** JavaScript browser-verification wall — returns HTTP 503 with a "Verifying your browser" proof-of-work body to every non-JS client, on http and https; the site is alive, this is not an outage — allowlist `insse.ro` in the URL-liveness workflow rather than re-chasing it each cycle. 2026-09-18 verified)
- **Q4 2025 HPI**: 168.99 (2015=100); up from 166.14 in Q3

**Bucharest market value (Dec 2025)**: ~**€2,204/m²** average, **+16.6% YoY** (Imobiliare.ro/GlobalPropertyGuide aggregation; INS doesn't publish €/m² directly)

**BNR (Banca Națională a României)**: https://www.bnr.ro/ — Quarterly Financial Stability Report

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| Imobiliare.ro | https://www.imobiliare.ro/ | Largest, RON pricing, has its own "Indicele Imobiliare.ro" |
| Storia.ro | https://www.storia.ro/ | OLX Group / Adevinta; aggregates many agencies |
| OLX Imobiliare | https://www.olx.ro/imobiliare/ | Strong on private-seller listings |

**Verdict bands**:
- 🟢 within ±10% of Imobiliare.ro segment for comparable district + condition + seismic class
- 🟡 ±20%
- 🟠 ±30% — investigate: Bucharest Rs class? Restitution? Informal-build? Termoenergetica connection?
- 🔴 >±30% — significant red flag

**Critical Bucharest cross-check**: Pre-1977 building? Check **AMCCRS list** for Rs I/II/III/IV class before any offer. https://amccrs-pmb.ro/

---

## Section: `--traffic`

**Sources**:
- **Compania Națională de Administrare a Infrastructurii Rutiere (CNAIR)** road authority
- **Bucharest real-time** via Waze
- **OSM Overpass** universal

---

## Section: `--tax`

### Currency note
RON, EUR/RON ≈ 4.97 (Apr 2026, floating). Not in eurozone. No firm target.

### Major 2025-2026 reforms

- **VAT**: Standard rate raised **19% → 21% (1 Aug 2025)**. User assumption "VAT 19%" is now outdated.
- **Reduced VAT**: former 5% and 9% rates merged to single **11% reduced rate** from 1 Aug 2025
- **New-build housing transitional 9%**: between 1 Aug 2025 and **30 Sep 2026 inclusive** (window extended from 31 Jul 2026 by Legea 161/2026 of 4 Aug 2026, M.Of. 642 per juridice.ro, secondary; 2026 data, source ANAF DGRFP Cluj notice CJR_DEC 15671/24.08.2026), qualifies for 9% VAT only if: useful area ≤ 120 m², value (incl. land, ex-VAT) ≤ RON 600,000, buyer is individual, no prior reduced-VAT purchase since 1 Jan 2023, advance contract by 1 Aug 2025 with a 20% advance (ex-VAT) paid in full by 31 Jul 2025 + delivery by 30 Sep 2026. Buyers who paid the standard rate on one qualifying home purchased 1-7 Aug 2026 may claim the difference back from 1 Oct 2026. **After 30 Sep 2026 the 9% concession EXPIRES** unless extended again — verify at ANAF
- **Local property tax — major reform 1 Jan 2026** (Lege 239/2025, M.Of. 15 Dec 2025; 2026-05-27 verified, source ProTV / Europa Libera / juridice.ro — scope note: only the concrete/brick basis description, the O.G. 16/2022 repeal and the O.U.G. 9/2026 age cuts stated below carry the later 2026-08-07 re-verification, source Ministerul Finanțelor https://mfinante.gov.ro/static/10/Mfp/transparenta/EMproiectlegeredresareficientizareRP_28082025.pdf; every other figure in this bullet still carries the 2026-05-27 stamp): Taxable value baseline (residential, concrete/brick frame + full utilities) raised from **RON 1,492/m² → RON 2,677/m² (+79%)**. The notarial market-study basis (O.G. 16/2022) is **REPEALED** — the Ministerul Finanțelor explanatory memo projects that the mass-valuation IT system could supply values in 2026 for the 2027 tax base (a projection, not a confirmed switch — verify the 2027 basis at Ministerul Finanțelor / the local primărie). Reductions for buildings >30 years (10%) and >50 years (30%) were eliminated by Lege 239/2025, but **O.U.G. 9/2026 restores age cuts of 15% (50–100 yrs) and 25% (100+ yrs)** (2026 verified — no in-force date given in the source entry; confirm the applicable tax year with the local primărie). Buildings >4 floors reduction **eliminated**. Severe-disability exemption **removed**. Statutory cota per Codul Fiscal art. 457–458: **0.08–0.2% residential / 0.2–1.3% non-residential** (set by hotărâre de consiliu local). Apartment owners typically see local tax up **70–80%**, in Bucharest Sector 1 close to doubled — not adjusted for the O.U.G. 9/2026 age-cut restoration; no revised impact figure is published in the source entry.
- **Special tax on high-value properties**: 0.3% → **0.9%** for residential >RON 2,500,000 and vehicles >RON 375,000 (1 Jan 2026)
- **Full market-value taxation**: Scheduled for **2027** under PNRR commitments
- **Securities/crypto/gold CGT**: 10% → 16% (1 Jan 2026) — *not* real estate

### Transfer / acquisition costs (individual buyer)

- **Notary fee**: progressive grid (Camera Notarilor Publici). Above RON 600,001: ~RON 6,405 fixed + 0.6% on amount above 600,001
- **Land Registry intabulation (carte funciară)**: ~0.15% of transaction value
- **Minimum reference value**: Notaries use published "studii de piață privind valorile minime imobiliare" (formerly grilele notariale) per locality. If declared sale price < grid minimum, taxes computed on grid minimum. Annual: https://www.cnpb.ro/studiile-de-piata-privind-valorile-minime-imobiliare

### Capital gains tax — individual sale

- **3%** on taxable amount if held **≤3 years**
- **1%** if held **>3 years**
- Withheld by notary at deed signature
- Computed on higher of declared price or grid minimum value
- **No primary-residence exemption** — RO does NOT exempt main home, unlike many EU peers
- **Note**: 16% rate (2026) applies to securities/financial-instrument capital gains, NOT real estate

### Rental income tax

- **10% flat** on net rental income (after 20% lump-sum deductible expense allowance, effective ~8% gross)
- **CASS health-insurance contribution** of 10% if total annual non-salary income exceeds 6×, 12×, or 24× the minimum wage thresholds
- Hosts on Airbnb/Booking: ANAF in 2025 identified ~22,000 undeclared operators; only ~20% compliant. Enforcement sharply tightening

### AML / cash limits (Law 70/2015)

- Cash payments between professional entities and individuals: daily threshold RON 10,000
- Cash payments by professional entities: RON 5,000/day per person
- Mandatory ONPCSB reporting of any cash transaction ≥ EUR 10,000 equivalent
- Real estate developers (NACE 4110) are AML "obligated entities"

---

## Section: `--rental`

### STR / Airbnb

- **Mandatory**: "Certificat de clasificare" from Ministerul Economiei, Antreprenoriatului și Turismului. Free, application by email/post. Must be displayed in entrance and kitchen
- **Cash register obligation (2025)**: Airbnb hosts must issue receipts and use cash register for in-person payments
- **Bucharest**: no specific Bucharest license layer beyond national classification; sectorial control by ANAF + Direcția de Control Turism (phone 0372 570 602 must be displayed)
- **2025 enforcement**: Fines RON 10,000–40,000 (~EUR 2,000–8,000) for unlicensed operation; ANAF March 2025 sweep recovered tax on RON 260M of undeclared 2023-2024 income
- **Tourist tax**: levied locally; e.g., Bucharest 1% of accommodation tariff per night
- **Tax regime**: From 2024, individuals letting >5 properties OR using digital platforms must register as PFA or company. Below threshold: flat 10% on net

---

## Section: `--work=<profession>`

Bucharest IT/services hub; Cluj tech hub ("Silicon Valley of Eastern Europe"); Timișoara, Iași, Sibiu/Brașov regional centers. Romania has substantial IT outsourcing and shared-services economy.

---

## Section: `--risks`

### Seismic — CRITICAL for Bucharest

- **Vrancea zone** generates intermediate-depth (60-180 km) M6.5–7.5 events
- INFP statistical recurrence: M≥6 every ~10 years, M≥7 every ~33 years, M≥7.5 every ~80 years
- **Last major: 4 Mar 1977, M7.5, hypocenter 85 km depth; 1,578 dead (1,424 in Bucharest), 32,900 buildings destroyed/damaged**
- **AMCCRS (Bucharest seismic consolidation administration)**: https://amccrs-pmb.ro/
- Building classes: **Rs I** (high collapse risk in design earthquake), Rs II (major structural damage), Rs III (moderate), Rs IV (no significant damage)
- Per latest published lists: ~350 Rs I, ~363 Rs II, ~112 Rs III in Bucharest. ~350 Rs I + ~363 Rs II = ~713 in classes I–II
- **Citizen map (community-built)**: https://www.hartablocuri.ro/ — crowdsourced map by year of construction; widely used by buyers
- **Class Rs I buildings cannot be insured by most insurers and banks may refuse mortgages**

### Flood

- **Apele Române**: https://rowater.ro/
- 526 designated Areas of Potential Significant Flood Risk (APSFR)
- New flood hazard + risk maps (2024 release, World Bank–supported) cover all APSFRs at multiple return periods (1:10, 1:100, 1:1000-year + climate-change scenario)
- Annual expected damage: ~EUR 1.7 billion; ~150,000 citizens annually exposed (per the 2024 World Bank–supported flood maps above — verify the underlying study at Apele Române)
- INSPIRE EU dataset record: https://inspire-geoportal.ec.europa.eu/srv/api/records/b275eed0-198b-11e5-b939-0800200c9a66
- World Bank dataset mirror: https://www.inundatii.ro/

### Forest fires
- Less affected than Mediterranean peers but Carpathian/Apuseni dry seasons rising
- AFM (Administrația Fondului pentru Mediu): https://www.afm.ro/ (intermittent 503)

### Government risk hub
- https://inundatii.ro/ (browser-check; HEAD filtering)

### Mandatory diagnostics

- **Energy Performance Certificate (Certificat de Performanță Energetică)**: mandatory under Law 372/2005. Validity 10 years. Sale-purchase contract concluded **without the EPC is voidable** (relative nullity, contestable in court). Original transmitted to buyer at deed; copy to local fiscal authority
- **Seismic risk class**: NOT mandatory disclosure at sale legally, BUT Bucharest pre-1977 buildings publicly listed by AMCCRS in classes Rs I–IV. **Class Rs I buildings cannot be insured by most insurers and banks may refuse mortgages.** Single largest "gotcha" in Bucharest property — always check pre-1977 buildings against AMCCRS list before any offer
- **Radon**: Order No. 153/2023 (effective Aug 2023) implements EU 2013/59/EURATOM; reference 300 Bq/m³. Mandatory testing in workplaces in radon-prone areas. **NOT yet mandatory for residential sale**, but advisable in Cluj/Bihor/Alba/Bistrița/Sibiu
- **No mandatory termite/asbestos/lead-paint diagnostic** at sale — Romania has no French-style DDT bundle. Buyer-beware regime

---

## Section: `--mains`

### Cadastre / Land Registry (eTerra3)

**ANCPI — Agenția Națională de Cadastru și Publicitate Imobiliară**:
- https://www.ancpi.ro/ — institutional (RO + EN)
- https://geoportal.ancpi.ro/ ❌ OFFLINE — ANCPI's public Geoportal is among the platforms (with RTI, MyEterra, Registrul proprietarilor, Titluri de proprietate) that ANCPI states will be brought back "etapizat" after the August 2026 e-Terra outage (11–19 Aug 2026; payment-link function restored 20 Aug 2026) — verify at ANCPI https://www.ancpi.ro/ and the county OCPI. When restored: INSPIRE-compliant national geoportal; parcel viewer at `/geoportal/imobile/Harta.html`. Public. (2026 data, source ANCPI; 2026-09-18 verified)
- https://eterra3.ancpi.ro/ ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — eTerra3, integrated cadastre + land book. **Auth-only** (notaries, lawyers, executors get credentials)
- https://myeterra.ancpi.ro/ ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row — citizen self-service portal. **Auth via ROeID** — foreign buyer without ROeID **cannot self-serve**; must instruct RO notary or lawyer to pull `extras de carte funciară` (~RON 25–40 electronic, RON 100+ paper sealed)
- **CF (carte funciară) is the canonical identifier** for any parcel
- eTerra3 = production system (replaced legacy eTerra). All county OCPI offices route through it

### Bucharest district heating — major pain point

- **RADET went bankrupt in 2019**; municipal company **Termoenergetica** took over (DO NOT use "RADET" in 2026 docs)
- Serves >8,000 apartment blocks (~90% of city heating)
- Pipe network corroded — reported losses of est. >2,000 tons of hot water/hour in worst sections (press-sourced figure — verify with Termoenergetica)
- Termoenergetica's debt to ELCEN (generator) reached ~RON 1.18 billion (~EUR 236M) late 2025
- Bucharest mayor + EU funding (~EUR 260M) commenced rehabilitation of 210 km primary network (4-year programme)
- **Buyers in Bucharest district-heated blocks should expect periodic winter outages, scheduled 2026-2029 disruptions for pipe replacement, and ongoing tariff uncertainty.**

### Other mains
- **Other cities**: Cluj, Timișoara, Iași, Constanța — DH similarly aged but smaller-scale. Apartments with **centrală proprie** (individual gas boiler) vs **conectare la termoficare** is a major valuation differentiator
- **Gas**: Distrigaz Sud (Engie) for Bucharest/south, E.ON Gaz for north
- **Electricity**: Hidroelectrica + Nuclearelectrica generation; distribution by E.Distribuție (Enel), DEER (PPC), Electrica
- **Water/sewage**: Apa Nova (Veolia subsidiary) for Bucharest; municipal RAJA companies elsewhere. Rural areas: high % unconnected to mains sewage

---

## Section: `--crime`

See `shared/crime-sources.md`. Romania uses:
- **Inspectoratul General al Poliției Române (IGPR)**: https://www.politiaromana.ro/
- **INS criminality data**

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`.

---

## Cost benchmarks (Apr 2026)

| Item | Range / typical |
|---|---|
| Bucharest €/m² avg (Dec 2025) | ~€2,204 (+16.6% YoY) |
| Cluj-Napoca | ~€2,400–€2,800/m² (est., Imobiliare.ro segment, Apr 2026) |
| Timișoara / Iași / Brașov | ~€1,600–€2,200/m² (est., Imobiliare.ro segment, Apr 2026) |
| VAT new-build (qualifying) | 9% (until 30 Sep 2026, Legea 161/2026) → 11% / 21% |
| CGT (>3 years held) | 1% |
| Local property tax baseline (1 Jan 2026) | RON 2,677/m² × adjustments + municipal rate |
| Total acquisition costs | ~2–3% buyer side |

---

## Active fiscal incentives (Apr 2026)

- **9% VAT new-build for qualifying first-home** until 30 Sep 2026 (cliff; extended from 31 Jul 2026 by Legea 161/2026)
- **1% CGT after 3 years** (vs 3% under)
- **Schengen full integration 1 Jan 2025** — EU buyer access uplift

---

## Foreign-buyer rules

- **EU/EEA citizens**: full equality with Romanian citizens since **1 January 2014** (end of 7-year derogation post-2007 accession). Includes agricultural land and forests
- **Non-EU/EEA individuals**: **Cannot own land directly** (Constitution Art. 44). They CAN own buildings/apartments, just not the underlying land plot. Workaround: buy a building only (`drept de superficie`) or set up a Romanian SRL
- **Reciprocity treaty**: some non-EU nationalities can own land if their state has a reciprocity agreement with RO — case-by-case via lawyer
- **Agricultural land**: right of preemption applies (co-owners, lessees, neighbors, young farmers, ANAF, RO state) — Law 17/2014. Foreigners face same preemption stack + ministry approval for plots >30 ha

---

## Country-specific quirks

- **Restitution Laws 18/1991, 1/2000, 10/2001, 247/2005, 165/2013**: Communist-era confiscated agricultural land (18/1991), forests (1/2000), and urban properties (10/2001) restituted in rem where possible, otherwise compensated. **Key risk**: if a property has unresolved restitution claim (uncommon now but possible for buildings sold without good-faith DD in 1990s/2000s), title can be voided years later. **Always demand `extras de carte funciară` showing clean title chain back to pre-1945 or to a clear post-restitution adjudication**
- **Informal/illegal builds**: 1990s saw widespread construction without permits, especially rural. "Carte funciară" must show building registered (intabulat) — if only land registered and structure isn't, it's an unauthorized build. Common around Bucharest commuter belt (Ilfov: Voluntari, Popești, Berceni). Legalization possible via court (Law 50/1991 amendments) but expensive and slow
- **Brașov/Sibiu/Sighișoara German Saxon heritage**: pre-1945 ethnic-German Saxon population largely emigrated post-1989 (Aussiedler). Old town Sibiu (UNESCO buffer) and Brașov have heritage protection — major renovations require Direcția Județeană pentru Cultură approval. Some properties restituted to Saxon heirs in Germany; chains of title sometimes complex
- **Rural land consolidation**: parcels micro-fragmented (post-1991 restitution divided land back to pre-collectivization owners' heirs). Buying a "10 ha plot" can mean assembling 30+ titles. Ministerial pre-emption stack (Law 17/2014) bites
- **Anti-mafia / source-of-funds**: Cash limit RON 10,000 daily. Notaries demand documented source of funds for transactions >EUR 15,000 under AML rules; bank-to-bank wire is standard above the cash threshold
- **Constitutional non-resident land ban**: Non-EU individuals cannot own land directly. SRL workaround standard

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre + title | ANCPI / OCPI | https://www.ancpi.ro/ |
| Tax authority | ANAF | https://www.anaf.ro/ |
| National Bank | BNR | https://www.bnr.ro/ |
| Notary minimum-value studies | CNPB | https://www.cnpb.ro/studiile-de-piata-privind-valorile-minime-imobiliare |
| Bucharest seismic | AMCCRS | https://amccrs-pmb.ro/ |
| Citizen seismic map | hartablocuri.ro | https://www.hartablocuri.ro/ |
| Floods | Apele Române | https://rowater.ro/ |
| Risk maps hub | Gov risk | https://inundatii.ro/ |
| Nuclear / radon | CNCAN | https://www.cncan.ro/ |

---

## Source URL templates

| Field | Template |
|---|---|
| Cadastral extract (myeTerra) | https://myeterra.ancpi.ro/ ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row |
| Cadastre map | https://geoportal.ancpi.ro/ ❌ OFFLINE — ANCPI's public Geoportal is among the platforms (with RTI, MyEterra, Registrul proprietarilor, Titluri de proprietate) that ANCPI states will be brought back "etapizat" after the August 2026 e-Terra outage (11–19 Aug 2026; payment-link function restored 20 Aug 2026) — verify at ANCPI https://www.ancpi.ro/ and the county OCPI (2026 data, source ANCPI; 2026-09-18 verified) |
| HPI quarterly | https://www.insse.ro/ |
| Bucharest seismic class | https://amccrs-pmb.ro/ |
| Property-tax CGT | https://taxsummaries.pwc.com/romania/individual/income-determination |
| Flood maps | https://rowater.ro/ |

---

## Status

**Confidence**: HIGH on VAT 19→21% (1 Aug 2025, multiple sources), local property tax 2026 reform (RON 2,677/m² baseline), CGT 1%/3% individual rates, Bucharest Termoenergetica/RADET debt, AMCCRS seismic class methodology. MEDIUM on per-municipality 2026 tax rates (varies), 9% VAT cliff 30 Sep 2026 (Legea 161/2026 extension) implementation details. LOW on AMCCRS list completeness (community-augmented at hartablocuri.ro). Cadastre / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)
- 2026-08-07: `--tax` local property tax — O.U.G. 9/2026 restores building-age cuts (15% for 50–100 yrs, 25% for 100+ yrs); O.G. 16/2022 notarial market-study basis repealed, market values deferred to the 2027 base; source re-pointed to Ministerul Finanțelor (regulatory-watch RO entry, verified 2026-08-07)

---

## Extension TODOs

- AMCCRS Rs I/II/III/IV list integration — expose as a Bucharest-specific cross-check inside `--integrity`
- Termoenergetica connection check by address (currently address → block → registry must be done manually)
- 2027 full market-value property-tax transition tracker (PNRR commitment)
- Restitution-claim red-flag scanner enhancement
