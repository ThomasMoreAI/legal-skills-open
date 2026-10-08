# Andorra 🇦🇩 — Property Due-Diligence Playbook

ISO2: `ad`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode**: `AD` + 3 digits, parish-coded:
  - **AD500** Andorra la Vella, **AD700** Escaldes-Engordany, **AD200** Encamp + Pas de la Casa, **AD100** Canillo + El Tarter + Soldeu, **AD300** Ordino + La Massana (split AD400 La Massana / AD300 Ordino), **AD600** Sant Julià de Lòria
- **Admin levels**: 7 **parròquies** (parishes), each with its own **Comú** (parish council); no provinces; the Govern d'Andorra is the national executive
- **Currency**: **EUR (€)** — adopted via [Monetary Agreement with EU 2011](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A22011A1217%2801%29) (Andorra mints its own euro coins, Banc Central not member of Eurosystem; **NOT a Eurozone member, NOT EU member**)
- **Languages**: **Catalan** (sole official); Spanish, French, Portuguese widely used in commerce. ~50% native Andorran population are Spanish nationals
- **Population**: ~85,800 end-2024 ([Departament d'Estadística](https://www.estadistica.ad/) 2024 padró); ~50% non-Andorran resident
- **Cadastre**: **Decentralized at parish level (Comú)** — there is NO single national cadastre. Each Comú maintains its own *cadastre parroquial* (parcel layer + tax base)
- **Land registry**: **Registre de la Propietat** at the Justícia courts (Cort, Andorra la Vella) — separate from Comú cadastre
- **Identifier**: parish-level reference (parcel + Comú); Registre folio number on title
- **Key documents**: *escriptura pública* (notarial deed), *certificat del Comú* (parish certificate), *nota simple del Registre* (registry extract)
- **Foreign-investor regime** (CRITICAL): non-residents need prior **autorització d'inversió estrangera** from Govern under [Llei 10/2012 d'inversió estrangera](https://www.bopa.ad/Documents/Detall?doc=GD20120607_15_45_22) before any RE acquisition; **Llei 3/2024** added a new tax on non-resident RE investment (see `--tax`)

## Section: `--price`

### Primary sources

- **Departament d'Estadística**: `https://www.estadistica.ad/` — quarterly **Index de Preus de l'Habitatge (IPH)** + transaction volume series
- **Banc Central d'Andorra (AFA — Autoritat Financera Andorrana)**: `https://www.afa.ad/` — financial-stability + mortgage-stock context
- **Cambra de Comerç, Indústria i Serveis d'Andorra (CCIS)**: `https://www.ccis.ad/` — biennial RE market report
- **Cadastre Comú** (per parròquia, see Verification authorities for URLs) — surface (m²), parcel reference, *valor cadastral* used for parish property tax

### Listing platforms

- **Idealista Andorra**: `https://www.idealista.com/ca/andorra/` — strong coverage, Catalan/Spanish
- **Engel & Völkers Andorra**: `https://www.engelvoelkers.com/ca-ad/andorra/` — premium / international
- **Sotheby's International Realty Andorra**: `https://www.andorra-sothebysrealty.com/en`
- **Habitatclick.ad**, **Pisos.com Andorra**, **MM Andorra Real Estate**, **Cisa Inmobiliaria**
- **Naturland properties** (mountain / ski-corridor specialists)
- ⚠️ Most listings tagged in **m² construïts** (built area); confirm vs **m² útils** (usable) on visit *(per listing — verify with cadastre / on visit)*

### Price benchmarks (2024-2025 IPH + listing scrape, est.)

| Parròquia / area | EUR/m² resale (≈ 2025) | Notes |
|---|---:|---|
| **Andorra la Vella centre** | 5,500–8,500 | capital; commercial centre |
| **Escaldes-Engordany** | 5,000–8,000 | spa town adjacent capital; high demand |
| **La Massana** (Arinsal, Pal corridor) | 4,000–6,500 | ski + family residential |
| **Ordino** (village + ski hamlets) | 4,500–7,000 | UNESCO Biosphere; premium chalet stock |
| **Canillo** (incl. El Tarter, Soldeu, Grau Roig) | 4,500–8,500 | Grandvalira ski-in |
| **Encamp** + Pas de la Casa | 3,200–6,000 | Pas de la Casa ski-front, Encamp town value |
| **Sant Julià de Lòria** | 3,500–5,500 | south, lower altitude, frontier with ES |
| **Ultra-prime chalets** (new build, ski-in, valley views) | 8,000–15,000+ | Soldeu/Ordino; per E&V/Sotheby's listings |
| **Pas de la Casa older studios** (1970s ski-block) | 2,500–4,000 | aged stock, façade/heating issues |

⚠️ Andorra is small (~468 km², ~85k population) → **transaction volume is thin** (~1,500–2,500 RE transactions/year per Estadística). Comparable-sales data sparse outside the main parishes; price discovery slow. Treat the bands above as wide indicative ranges — every parcel needs an individual view from the local Comú + at least two estate agents.

### Compute

1. EUR/m² = price / **superfície construïda** (built area as registered at Comú); **superfície útil** also recorded but listing convention is "construïda"
2. Andorra-specific premium drivers: **ski-in/ski-out** (Grandvalira / Vallnord domains), **valley orientation** (south-facing slopes), **altitude** (sub-1,200m for year-round comfort)
3. Discount drivers: **Pas de la Casa pre-2000 ski-blocks** (heating/insulation legacy), **steep parcels** (avalanche / access), high HOA *despeses comunitàries* in older blocks

### Key terms

- IPH = Índex de Preus de l'Habitatge
- Comú = parish council
- Parròquia = parish (×7)
- Escriptura pública = notarial deed
- Despeses comunitàries = HOA / community fees

---

## Section: `--traffic`

### Sources

- **Govern d'Andorra — Mobilitat**: `https://www.mobilitat.ad/` — traffic counters on the trunk network (CG-1 to CG-6) + winter pass operations
- **Servei de Forces de Comunicacions (SFC)**: real-time road status, snow/avalanche closures
- **Departament d'Estadística** mobility series (annual)

### Key term

**IMD (Intensitat Mitjana Diària)** = AADT-equivalent. Reported on the *Carreteres Generals* (CG-1 to CG-6) and major *carreteres secundàries*.

### Verdict bands

- 🟢 < 2,000 v/d (parish lanes, residential carrers, mountain spurs)
- 🟡 2,000–10,000 v/d (Carretera General secondary, parish through-roads)
- 🟠 10,000–25,000 v/d (CG-1 / CG-2 outside Andorra la Vella, CG-3 valley)
- 🔴 > 25,000 v/d (Avinguda Meritxell + ronda Andorra la Vella; CG-2 Pas de la Casa peak ski weekends — Jan/Feb/Easter Sat-Sun)

⚠️ Andorra has **no rail and no airport** — every visitor and every truck passes through the same trunk network. Saturday turnover days in ski season + Pyrenean tunnel weekends create **acute peak loading** on CG-1 (FR border) + CG-2 (Pas de la Casa / Tunel d'Envalira) that doesn't appear in annual averages.

---

## Section: `--tax`

### Annual taxes (parish-level)

- **Impost sobre la propietat immobiliària edificada** (parish prop. tax, set per Comú): est. **~€0.30–€1.50/m² built/year** for residential, varies by Comú ordinació (verify current rate — see below)
- **Foc i Lloc** (residency tax): ~€100–200/person/year per Comú
- **Higiene** (waste/sanitation): ~€80–€300/dwelling/year per Comú
- Verify exact rate with target parish ([Comú Andorra la Vella](https://www.comuandorra.ad/), [Comú Escaldes-Engordany](https://www.e-e.ad/), etc.)

### Transaction taxes — ITP

- **~4% total** on resale, split per Llei 1229/2000 art. 8: **1% Govern (state, art. 8.1)** + **0.50–3% Comú (parish-set per ordinació comunal, art. 8.2)**. Most parishes have set 3%, so the typical headline total is **1% + 3% = 4%** — but **confirm with target Comú** (some parishes lower). (2026-05-27 verified, source [portaljuridicandorra.ad/L20001229B_11](https://portaljuridicandorra.ad/L20001229B_11).)
- Buyer pays ITP at *escripturació*. Ref: [Llei sobre l'Impost sobre Transmissions Patrimonials Immobiliàries del 29 desembre 2000](https://portaljuridicandorra.ad/L20001229B_11) — verify amendments before closing.

### IEI — Impost sobre l'inversió estrangera en immobles (Llei 3/2024 + Llei 5/2025 "Llei Òmnibus")

- **Llei 3/2024 del 29 de febrer** introduced an **additional RE tax** on non-residents. **Llei 5/2025 del 6 de març ("Llei Òmnibus", BOPA 26 March 2025, EIF 16 April 2025)** replaced the prior progressive scale with a **two-tier**:
  - **6%** for first property (single home / apartment / studio + permitted annexes per personal-use threshold)
  - **10%** for additional properties beyond the first
- **Foreign-investor property cap (Llei 5/2025)**: max **1 single-family home** OR **2 apartments/studios + 3 storage units + 3 parking spaces per unit** (or 6 parking + 1 commercial unit alternative). Exception for 10-year affordable-rental commitments.
- Combined ITP + IEI: **non-resident acquisition tax floor ~10%** on first property (4% ITP + 6% IEI); **~14% on each additional** (4% + 10%). Verify current rate at [tributs.ad](https://www.tributs.ad/) + Govern d'Andorra BOPA before any non-resident purchase. (2026-05-27 verified, source [Llei 5/2025 — leslleis](https://www.leslleis.com/L2025005) + Cases & Lacambra.)
- **Authorisation silence rule** (Llei 3/2024 disposició final quarta): the prior **positive silence** under Llei 10/2012 art. 18.3 became **negative silence** — if Govern fails to expressly resolve within 2 months (+ possible extension), the foreign-investment authorisation is **deemed DENIED**, not granted. Build hard timeline pads + escalation contact at Servei d'Immigració. (2026-05-27 verified, source Augé Legal & Fiscal.)
- **Llei 2/2026 del 22 de gener ("Omnibus 2")** further tightened residency parameters — verify current values at BOPA before relying.

### VAT — IGI (Impost General Indirecte)

- **Standard 4.5%** (lowest in Europe). Residential resale → ITP (NOT IGI). **New-build first sale → 4.5% IGI** (in lieu of ITP). Ref: [Llei 11/2012](https://www.bopa.ad/)

### Capital gains — Plusvàlua immobiliària (within IRPF framework)

- [Llei 21/2014 + Llei 5/2014](https://www.bopa.ad/) sliding scale by holding period: <1y ~15% / 1–2y ~13% / 2–10y gradient ~10%→~1% / **>10y exempt**
- **Primary-residence exemption** with reinvestment in another habitual AD residence — verify at [tributs.ad](https://www.tributs.ad/)

### Income tax — IRPF (resident) / IRNR (non-resident)

- **IRPF (resident)** [Llei 5/2014](https://www.bopa.ad/): **0%** ≤ €24,000 / **5%** €24k–€40k / **10%** > €40k
- **IRNR (non-resident)**: flat **10%** on Andorran-source income (incl. rental)

### Notary + Registre

- **Notari** mandatory; ~0.5–1.5% of price (regulated arancel, capped high-value)
- **Registre** filing: ~0.1–0.5%. Combined: ~1–2%

### Total transaction cost (buyer side)

- **Resale, resident**: ~**5.5–7%** (4% ITP + 1–2% notary/registry)
- **Resale, non-resident**: ~**8–14%+** (with Llei 3/2024 progressive surcharge)
- **New build (first sale)**: ~**6.5–8%** (4.5% IGI + notary/registry + parish levies)

### Wealth + inheritance

- **No wealth tax** (abolished); **no inheritance tax** between direct heirs per [Llei 21/2014](https://www.bopa.ad/); collateral inheritances may attract minor parish-level fees
- Central to Andorra's tax-residency appeal vs ES/FR

### Future risk

- **Llei 3/2024** politically sensitive — parameters may change in 2026 budget
- **OECD BEPS Pillar Two** — domestic minimum taxation implemented; corporate-vehicle structuring evolving
- **EU Association Agreement** ([Govern AA portal](https://andorraue.ad/ca/acord-d-associacio)) — Council of the EU approved the text **16 July 2026**; **signature set for 19 October 2026 in Brussels**, then European Parliament consent, ratification by all 27 EU member states (Coreper confirmed the text is a MIXED agreement, 15 Jul 2026), a **consultative referendum** and ratification by the Consell General before entry into force; per Eunews (secondary, 16 Jul 2026) the Council decision also covers **provisional application** — scope and start not verified against the Council release, check consilium.europa.eu after signature — tax-cooperation tightening on ratification (2026 data, source Govern d'Andorra Secretaria d'Estat per a les Relacions amb la UE; 2026-09-18 verified)

---

## Section: `--rental`

### Long-term residential

- **Llei 1/2024, de l'arrendament d'habitatge** ([BOPA Mar 2024](https://www.bopa.ad/)) — new tenancy law: **5-year minimum term**, tenant break clause from year 1, indexation capped to **IPC d'Andorra** (CPI, typically 2–4% recent), 1-month security deposit standard
- Rental income taxed within IRPF (resident, 0/5/10%) / **10% IRNR** (non-resident) — see `--tax`

### Short-let (Habitatge d'ús turístic / HUT)

- **Llei 26/2024** ([BOPA 2024](https://www.bopa.ad/)) — short-let regime now tight: mandatory **HUT registration** with [Departament de Turisme](https://www.turisme.ad/) + parish *autorització*, **community-of-owners vote** required in multi-unit buildings, **quotas / moratoria** in saturated parishes (**Andorra la Vella** restricted new HUT permits 2024), nightly *taxa turística* per guest
- ⚠️ Pre-2024 informal Airbnb listings now non-compliant — request **número de registre HUT** before any STR pricing model. Penalties €3,000–€30,000 for unregistered operation
- **IGI 4.5%** on rental revenue may apply if hotel-like services (verify with Departament de Turisme)

### Rental yields (est.)

- Long-term gross yield, mid-tier apt 2026 ≈ **3.5–5%**
- Short-let gross yield (compliant ski-front) ≈ **5–8%** but strong seasonality (Dec–Apr concentration)
- Net drag: parish prop. tax low, community fees in old ski-blocks high

---

## Section: `--work=<profession>`

### Job platforms

- **Servei d'Ocupació** (Govern d'Andorra Treball): `https://www.treball.ad/` — official jobs portal + work-permit info
- **InfoJobs Andorra**, **LinkedIn AD**, **Andorra Difusió jobs**, **Diari d'Andorra ofertes**
- **Cambra de Comerç (CCIS)** for SME hiring
- Profession-specific *col·legis professionals* for licensing (architects, doctors, lawyers, engineers — most require Andorran or EEA-recognised qualification + Catalan-language test)

### Work-permit gating

- **All non-residents** require an *autorització de treball + residència* before starting work; sponsored by employer who must prove Andorran-citizen vacancy was unfilled (preference-of-employment rule)
- **Quotes** (annual work-permit quotas) set by Govern, typically saturate during ski-season hiring (Oct-Nov) and summer hospitality
- *Residència activa* (work + reside) ≠ *Residència passiva* (residency without work — see `--visa`)
- **Self-employed** (*compte propi*): minimum capital + business plan; CASS social-security registration mandatory

### Self-employment + entities

- **CASS (Caixa Andorrana de Seguretat Social)**: `https://www.cass.ad/` — single social-security regime; ~**22% employer + 6.5% employee** contribution (employed); self-employed flat ~**21–22%** of base
- **Societat Limitada (SL)**: minimum capital **€3,000**; one-shareholder OK; corporate tax (IS) **10%** flat
- **Empresari individual** (sole trader): straightforward; CASS + IRPF liability

### Salary benchmarks (2024-2025, Estadística)

- **Salari mitjà** (mean monthly gross, all sectors) Q4 2024: ~**€2,400** (per Estadística salaris series)
- **Salari mínim** (minimum wage) 2026: **€1,525.33/month** (gross; €8.80/hr) — Decret 8/2026, del 14-1-2026 (BOPA núm. 3), in force from 1 Jan 2026; revised again 1 Jul 2026 (Decret 253/2026) — verify current amount at BOPA ([Govern circular salari mínim 2026](https://www.govern.ad/documents/d/guest/circular-informativa-salari-minim-2026?download=true))
- Hospitality / retail (ski-corridor seasonal): ~€1,500–€2,000
- Banking / finance (Andorran private banks: AndBank, MoraBanc, Crèdit Andorrà, BancSabadell d'Andorra): ~€2,800–€5,500
- Tech / digital (small market): ~€2,400–€4,500
- **No language gating in private sector legally** but **Catalan competence** decisive in practice for any client-facing role

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Departament de Medi Ambient** | `https://www.mediambient.ad/` | Environmental + landslide cartography |
| **Servei Meteorològic Nacional** | `https://www.meteo.ad/` | Snow/avalanche bulletins, climate baseline |
| **FORTA Servei de Forces de Comunicacions** | via [Mobilitat](https://www.mobilitat.ad/) | Avalanche-corridor warnings on roads |
| **Cos de Bombers** | `https://www.bombers.ad/` | Wildfire response + emergency planning |
| **Govern Protecció Civil** | `https://www.govern.ad/` | Civil-protection coordination |

### Specific risks

- **Avalanche (allau)**: principal natural hazard — Pyrenean alpine terrain, every commercial ski domain mapped. **Avalanche-corridor zoning** integrated into parish urban plans (*Pla d'Ordenació i Urbanisme Parroquial — POUP*); request parcel risk classification from target Comú. Historical fatal events on CG-3 (Vall d'Incles), CG-4 (La Massana corridor)
- **Landslide / rockfall**: steep slopes prone to *esllavissades* especially after heavy rain and freeze-thaw cycles; verify *POUP* hazard layer for parcels above 1,500m or on north-facing slopes
- **Flood**: limited but real — **riu Valira** (north + main confluence in Andorra la Vella) and tributaries (Valira d'Orient, Valira del Nord, Valira de Pal) flash flooding in extreme rainfall (2010-2020 events of record). Riverside parcels in Andorra la Vella + Sant Julià de Lòria deserve flood-zone check
- **Earthquake**: **LOW seismic hazard** — Pyrenean foreland; Andorra is in [seismic zone I](https://www.meteo.ad/) per CPC-2002 / EC8 implementation (PGA <0.04g typical); not a primary structural-design driver but modern builds use EC8 anyway
- **Snow loading + winter access**: persistent snow Dec–Apr above 1,500m; roof snow-load design critical (often 250–400 kg/m² in upper parishes); confirm structural capacity for any chalet purchase
- **Frost-jacking / freeze-thaw**: foundation + drainage detailing matters; pre-1980 stone constructions often have shallow footings → cracking, water ingress

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1960 stone "borda"/"casa de poble"** | Heritage, low insulation, lead pipes in some, asbestos cement in renovations 1950–80, shallow footings |
| **1960–1980 ski-boom (Pas de la Casa, Soldeu)** | Concrete-block walls, single-glazed, electric resistive heating, high *despeses comunitàries* now; some asbestos |
| **1980–2010** | Improving thermal codes; gradual EC1991/EC8 alignment; double-glazed standard mid-90s |
| **2010+** | EC-aligned + RITE-style energy code; modern thermal envelope; many new chalets pursuing high energy class |
| **Post-2018 Llei d'eficiència energètica** | Mandatory energy certification, façade retrofit incentives |

### Mandatory diagnostics at sale

| Document | Required because | Notes |
|---|---|---|
| **Certificat d'eficiència energètica (CEE)** | Mandatory at sale/lease per [Llei d'eficiència energètica 2018](https://www.bopa.ad/) | A–G scale |
| **Cèdula d'habitabilitat** (per Comú, varies) | Comú-level — required for occupancy / utility connection | confirm per parròquia |
| **Certificat del Comú** (no debts) | Mandatory pre-deed; certifies no parish-tax arrears | Comú issues; ~1-2 weeks |
| **Nota simple del Registre de la Propietat** | Mandatory pre-deed; confirms title + charges | Cort, Andorra la Vella |
| **Inspecció tècnica de l'edifici (ITE)** | Older multifamily blocks (parish-dependent) | check with Comú; not yet universal as in ES Cataluña |
| **Estatuts comunitat de propietaris + actes** | If condo | community fees + deudas + outstanding *derrames* (special levies) |

### Climate change projections (Servei Meteorològic + Pyrenees-OPCC)

- **+2 to +4°C** by 2050 vs 1990 baseline, mountain amplification ([OPCC Observatori Pirinenc del Canvi Climàtic](https://www.opcc-ctp.org/))
- **Snow-line rising ~150m / decade** — direct exposure for ski stations <2,000m base elevation (Pas de la Casa base ~2,100m; Vallnord-Pal ~1,780m; Vallnord-Arinsal ~1,550m at risk)
- **Glacial regression** in adjacent Pyrenean massifs (no glaciers within Andorra itself but hydrology affected)
- **Extreme rainfall** events: increasing intensity per OPCC; flash-flood risk in Valira basins
- **Wildfire**: low-altitude pinewoods (Sant Julià de Lòria) exposure rising

---

## Section: `--mains`

### Sources

- **FEDA (Forces Elèctriques d'Andorra)**: `https://www.feda.ad/` — sole electricity utility (national); also district heating in Andorra la Vella + EE services
- **Aigua + clavegueram**: managed by each **Comú** (parish-level water + sewer service)
- **GASNORD-PROANSA / butà bombona**: LPG bottle distribution (no piped gas network in Andorra)
- **Andorra Telecom (STA)**: `https://www.andorratelecom.ad/` — sole telecom + fibre operator (national monopoly); >95% FTTH coverage

### Costs (est., EUR, 2026)

| Scenario | Cost |
|---|---:|
| Mains water connection (typical urban parcel) | 800–2,500 |
| Mains sewer connection | 1,500–4,500 |
| Septic tank installation (rural, no mains) | 4,000–9,000 |
| FEDA electricity new connection | 500–2,000 (standard tariff) |
| FTTH activation (Andorra Telecom) | 0–150 (often promo) |
| District heating connection (Andorra la Vella, where available) | 2,000–6,000 |

⚠️ **No piped natural gas in Andorra** — heating is **electric resistive (cheap kWh post-2010)**, **heat pumps (rising)**, **wood / pellet** (rural), or **diesel / LPG bottles**. Verify heating system + annual cost before purchase: pre-2000 ski-blocks with electric resistive can run €2,500–€5,000/year heating alone for a 70 m² apartment at altitude.

---

## Section: `--crime`

### Primary source

- **Cos de Policia d'Andorra**: `https://www.policia.ad/` — annual *Memòria del Cos de Policia* with crime stats by parish + category
- **Departament d'Estadística**: `https://www.estadistica.ad/` — *justícia i seguretat* series

### Headline (2023-2024 Memòria del Cos de Policia)

- **Total recorded crimes 2023**: ~1,200 (per latest published Memòria)
- **Violent crime**: among the lowest in Europe per capita; near-zero homicide rate (0–2 cases/year)
- **Burglary**: low absolute numbers but seasonal spikes during ski-season (closed second-homes targeted in Pas de la Casa + Soldeu)
- **Petty theft + tourist-targeted scams**: concentrated in Andorra la Vella commercial axis (Avinguda Meritxell)
- **Drug-related**: small-scale; cross-border smuggling occasional (Andorra–France via tunnel + Andorra–Spain via N-145)

### Verdict bands

- 🟢 < 30% national rate (most rural villages, mid-altitude residential)
- 🟡 30–100% (typical urban parishes)
- 🟠 > 100% in 1–2 categories (Andorra la Vella commercial centre — petty theft elevated; Pas de la Casa winter — closed-property burglary)
- 🔴 multi-category > 200% — not observed; Andorra has no concentrated-crime blackspot

### Confidence

HIGH for headline national rate (Andorra is among the safest European jurisdictions per Eurostat / Numbeo aggregate); MEDIUM for parish-level granularity (Memòria does not always break out by sub-parish; some Comú-level reports supplement).

---

## Section: `--amenities`

Universal OSM Overpass logic per `shared/amenities-osm.md`. Andorra-specific brand-chain conventions:

- **Supermarket**: **Pyrénées Andorra** (Andorra la Vella flagship), **Hipermercat Carrefour** (Comú de la Vella), **Spar Andorra** (chain), **Mercadona** (cross-border presence Sant Julià / Andorra), **Lidl** has limited presence
- **Convenience / Pharmacy**: **Farmàcies** are tightly regulated — quota of ~58 nationally; tag `amenity=pharmacy`. Each parish has 24h on-call pharmacy rotation
- **GP / hospital**: single national hospital **Hospital Nostra Senyora de Meritxell (HNSM)** in Escaldes-Engordany ([servei sanitari](https://www.saas.ad/)); GP via *Centres d'Atenció Primària (CAP)* per parish
- **Public transport**: **Cooperativa Interurbana** bus network, **Línia 1** national axis (Pas de la Casa ↔ Sant Julià de Lòria); ski-shuttle services; **NO RAIL, NO AIRPORT** — closest connectivity points: Toulouse-Blagnac (180 km, 3h drive), Barcelona-El Prat (200 km, 3h), La Seu d'Urgell aerodrome (limited GA)
- **Schools**: trilingual choice — *Escola Andorrana* (Catalan), *Sistema Espanyol* (MEC-ES), *Sistema Francès* (AEFE-FR), British / international (Janer / Agora)

### Verdict bands

- 🟢 < 800m walk to supermarket/pharmacy/CAP: typical urban (Andorra la Vella, Escaldes-Engordany, parish town centres)
- 🟡 800m–3km: peri-urban / village outskirts
- 🟠 3–10km: mountain-corridor hamlets (Soldeu, Arinsal, El Tarter)
- 🔴 > 10km from any supermarket / pharmacy: very rural bordas; access dependent on private vehicle + winter snow-clearance

---

## Section: `--climate`

Universal logic per `shared/climate-projections.md`. Andorra-specific:

- **Köppen-Geiger**: dominant **Cfb** (oceanic mountain) + **Dfb / Dfc** at higher altitude + **ET** (alpine tundra) on summits
- **Reference baseline**: Servei Meteorològic 1990–2020 series; capital ~1,000m elevation; ski-corridor 1,800–2,500m
- **Key projections** (per [OPCC](https://www.opcc-ctp.org/) + Servei Meteorològic):
  - Annual mean temperature **+2 to +4°C** by 2050 vs 1990 baseline (Pyrenean amplification factor ~1.3× global mean)
  - **Snow-line rising ~150m/decade** — material for any property below 1,800m relying on ski-domain proximity for value
  - Heatwaves: rising number of *nits tropicals* (T-min > 20°C) at low altitudes; capital sees 5–15 such nights/year by 2050 (was rare in 1990s)
  - Extreme rainfall: hourly intensity +10–25%; Valira flash-flood signal
- **Acute-event flags**:
  - 🔴 ski-station base < 1,800m + heavy revenue dependence on snow (Pas de la Casa partially exposed; Vallnord-Arinsal base 1,550m exposed)
  - 🟠 valley-floor parcel < 100m from Valira channel — increased pluvial / fluvial flood probability
  - 🟡 mid-altitude main-valley urban (Andorra la Vella, Escaldes) — cooling-load growth; insurance trajectory upward
  - 🟢 mid-altitude (1,200–1,800m) south-facing year-round residential — generally resilient

### Climate verdict (typical mid-altitude urban Andorran apt 1,000–1,400m elevation)

🟡 **Watch** — material warming + cooling-load growth; ski-revenue exposure for the wider parish economy; insurance + building-envelope cost trajectory upward.

### Confidence

HIGH for OPCC + Servei Meteorològic projection envelopes (Pyrenees amongst best-monitored mountain ranges in Europe); MEDIUM for sub-parcel hazard zoning (POUP coverage variable across the 7 parishes).

---

## Section: `--finance`

### Mortgage market

- **Banking system**: 4 commercial banks (post-2015 BPA resolution + 2017 Vall Banc absorption): **Andbank**, **Crèdit Andorrà**, **MoraBanc**, **BancSabadell d'Andorra**
- Regulator: **AFA (Autoritat Financera Andorrana)**: `https://www.afa.ad/`
- **LTV caps** (typical, per AFA macroprudential expectations + bank product sheets):

| Buyer profile | Max LTV |
|---|---:|
| **Resident, primary residence** | **80%** |
| **Resident, second home / investment** | 60–70% |
| **Non-resident** | typically **50–60%** |
| **Non-resident pre-residency-application** | 40–50% (case-by-case; banks tighter post-2018 KYC reforms) |

- **Term**: typically 25–30 years, residential
- **Rate structure**: variable (Euribor + spread 1.5–3.0%) dominant; some banks offer fixed (mostly 5–10y); long fixed (>15y) rare. Q1 2026 effective mortgage rate ≈ **3.5–4.5%** all-in (Euribor 12M ≈ 2.3–2.8% + spread)
- **Stress test**: AFA expectations include +200bps stress; banks apply own DSR (debt-service ratio) caps typically **35–40% gross income**
- **Foreign-buyer mortgages**: available but tighter — most retail banks require:
  - Proof of foreign-investment authorisation already issued (Llei 10/2012)
  - Andorran bank account (open with passport + proof of foreign residence + tax declaration)
  - 50–60% LTV ceiling
  - Income evidence + 2 years' tax returns from home country
  - Some banks restrict to existing private-bank clients

### Banking access

- All 4 banks operate as private + retail; non-resident account opening subject to **CRS / FATCA** + **AML/KYC** under [Llei 14/2017 prevenció blanqueig](https://www.bopa.ad/) — typically 4–8 weeks; minimum balances vary (€10k–€100k+ for private-bank tier)
- Andorran banks' international transfer infrastructure routes via Spanish / French correspondents; SEPA member since 2016

### Confidence

HIGH for system-level figures (AFA reports + bank product sheets); MEDIUM for non-resident LTV ceilings (case-by-case; product sheets vary 2024–2026).

---

## Section: `--currency`

### Currency status

- **EUR (€)** adopted by [Monetary Agreement between EU and Andorra signed 30 Jun 2011](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A22011A1217%2801%29), entered into force 1 Apr 2012
- Andorra mints its own euro coins (since 2014) under the agreement; banknotes are ECB issuance
- **NOT** a Eurozone member; Banc Central not part of Eurosystem; AFA is the prudential regulator
- For reference: same regime category as **Monaco, San Marino, Vatican City** — small-state monetary agreements with EU (post-millennium pattern); **distinct** from Montenegro/Kosovo informal adoption (ME has no agreement, AD has)

### What this means for buyers

- **EUR-denominated buyers** (EU/EEA): **near-zero FX risk** for purchase + ongoing payments
- **GBP / USD / CHF / non-EUR buyers**: full EUR/home-currency exposure — use forward contracts for transaction lock-in if material; depth available via Andorran banks routing through Spanish / French counterparties
- No capital controls on EUR movements; AML reporting thresholds align with EU 4MLD/5MLD/6MLD as transposed by Andorra

### Peg credibility

- The Monetary Agreement is **legal-treaty-based**, not market-pegged; revocation requires bilateral action. No realistic re-redenomination scenario short of a country-wide political rupture
- Cross-border transfers benefit from SEPA membership (2016) — no FX intermediation cost for EUR transfers in/out

---

## Section: `--visa`

Universal logic per `shared/visa-programs.md`. Andorra-specific:

### Residència Passiva (sense activitat lucrativa)

- [Llei 9/2012 d'inversions estrangeres + Reglament](https://www.bopa.ad/), reformed 2022 + 2024 + **Llei 5/2025 ("Llei Òmnibus", eff. 16 April 2025)** + **Llei 2/2026 del 22 de gener ("Omnibus 2")**.
- **Investment required**: **€600,000 (pre-2025)** → **€800,000 (Llei 5/2025, eff. 16 April 2025)** → **possibly €1,000,000 (Llei 2/2026, eff. early 2026)** in Andorran assets (RE, public debt, shares, deposits, life insurance); within that, qualifying share can be in Andorran RE — remainder diversified into local financial assets. *Verify current floor at [immigracio.ad](https://www.immigracio.ad/) before relying.* (2026-05-27 verified, source carlotapastora + Cases & Lacambra + Advantia on Omnibus 2.)
- **AFA deposit restructure (post-Llei 5/2025)**: principal-holder portion split into **€30,000 NON-REIMBURSABLE state contribution + €20,000 AFA deposit (refundable)**. Each dependant: **€6,000 non-reimbursable + €6,000 refundable**. The non-refundable portion is sunk cost — model as such in retirement / digital-nomad NPV. (2026-05-27 verified, source Altaveu + carlotapastora.)
- Permit: 1-year initial → 3 + 3 + 7y renewals
- **Residency obligation**: ≥**90 days/year** physical presence (passive — no work)
- Tax-residence triggered separately at >183 days physical presence

### Residència Activa

- Work + reside permit; quota-bound; employer-sponsored (see `--work=`)
- **Self-employed**: SL min capital €3,000 + CCIS + CASS registration + business plan + AFA deposit ~€15,000 (verify current)
- Residency obligation: >**183 days/year**

### NOT a citizenship-by-investment jurisdiction

- ⚠️ **Andorran nationality RESERVED**: naturalisation requires **20 years' continuous residence** (no investment route). Andorra has never run a CBI / golden-passport scheme (cf. shared `visa-programs.md` ENDED registry)
- **Dual nationality not recognized** — most foreign residents stay on residency permits indefinitely

### Confidence

HIGH for Llei 9/2012 + 10/2012 framework + 20-year naturalisation rule (constitutional, multi-decade stable). MEDIUM-HIGH for current quantum (€800k floor per Llei 5/2025 — up from superseded pre-2025 €600k, possibly €1m per Llei 2/2026; + AFA deposits) — *verify exact current quantum at AFA + BOPA before application*.

---

## Section: `--insurance`

### Mandatory

- **Mortgage lender requirement**: **Assegurança d'incendis** (fire / multi-peril) on the dwelling structure, premium typically **0.04–0.15% of sum insured**
- **Sum insured = rebuild cost** (not market price) — typically **€1,200–€2,500/m² built** for standard concrete frame chalet/apt
- **Multi-unit blocks**: *comunitat de propietaris* often holds block policy; individual owners pay pro-rata via *despeses* — verify before duplicating

### Optional but standard

| Cover | Typical premium (2026 est.) |
|---|---:|
| **Home contents** (typical 70 m² apt) | €120–€450/yr |
| **Liability + community** (responsabilitat civil) | usually bundled in home policy |
| **Avalanche / landslide rider** (mountain corridor) | €100–€400/yr supplement; check cover for *allau* explicitly |
| **Pipe-freeze damage** (high altitude) | usually included; verify |
| **Earthquake** | typically included up to small sub-limit (low risk) |

### Major insurers

- **Assegurances Generals d'Andorra (AGA)**, **MoraBanc Assegurances**, **Crèdit Assegurances**, **Atlàntida Assegurances**, **Mapfre Andorra**, **Allianz Andorra** (cross-border presence)

### Climate trajectory

- ⚠️ Premiums in mountain corridors (Pas de la Casa, Soldeu, Arinsal) trending **+5–10%/year** 2023–2026 driven by avalanche-corridor risk re-pricing + extreme-rainfall flash-flood claims; underwriters tightening sub-limits on slope-side parcels and pre-1980 stock

### Confidence

MEDIUM — Andorran insurance market is small + relatively opaque on aggregate premiums; figures above are *est. from CCIS reports + insurer product sheets — verify quotes per parcel*.

---

## Section: `--notary`

### Process

- **Civil-law notary** (*notari*) mandatory for all RE transfers per [Llei del notariat](https://www.bopa.ad/) — Andorra has ~6–8 notaris nationally (small jurisdiction)
- *Notari* role: drafts the *escriptura pública*, confirms identity (incl. apostilled passport for non-residents), confirms title + charges via *nota simple del Registre*, withholds and remits taxes (ITP + Llei 3/2024 surcharge if applicable), files registration

### Standard timeline (typical residential resale)

| Step | Day | What happens |
|---|---|---|
| 1. Reserva / contracte privat | D0 | Buyer pays **deposit ~10%**; private contract drawn |
| 2. Foreign-investor authorisation (Llei 10/2012) | D7–D45 | If non-resident: file with Govern → **typical 2–4 weeks** for residential |
| 3. Mortgage approval (if applicable) | D14–D45 | Bank valuation + offer letter |
| 4. *Certificat del Comú* (no-debt) + *nota simple del Registre* | D30–D50 | Notari requests both pre-deed |
| 5. Escripturació (deed signing) at notari | D45–D75 | Buyer pays balance; notari withholds ITP + non-resident surcharge if applicable |
| 6. Registration at Registre de la Propietat | D75–D90 | Notari files; title perfected |

⚠️ **Foreign-investor authorisation gating**: non-resident buyers cannot complete escripturació without the prior Govern *autorització d'inversió estrangera*; build the 2–4 week wait into any closing schedule. Some sellers will accept conditional reservations subject to authorisation; standard practice in Andorran agency contracts.

### Costs

| Item | Typical |
|---|---|
| **Notari fee** | regulated arancel; ~0.5–1.5% of price (caps for high-value) |
| **Registre de la Propietat** | ~0.1–0.5% of price |
| **ITP** (resale, resident-buyer) | ~4% of price (1% Govern + 0.50–3% Comú, most parishes 3% — per Llei 1229/2000 art. 8) |
| **Llei 3/2024 surcharge** (non-resident) | progressive, up to ~10% (verify current bands) |
| **Foreign-investment file fee** | ~€500–€2,000 admin |
| **IGI** (new build first sale) | 4.5% of price (in lieu of ITP) |
| **Total transaction cost (buyer side, resident, resale)** | **~5.5–7%** of price |
| **Total transaction cost (buyer side, non-resident, resale)** | **~8–14%+** of price (rises with non-resident progressive surcharge) |

### Foreign buyer practical

- **Power of attorney** acceptable: notari accepts apostilled PoA for absent buyers; identity verification via passport copy + sworn declaration before consul or local notary in home jurisdiction
- **Source-of-funds**: notari + bank both apply AML/CRS reviews under [Llei 14/2017](https://www.bopa.ad/); bank statements + tax returns + source narrative standard
- **Beneficial-ownership disclosure**: corporate buyers register UBO with [Govern Direcció de Tributs i de Fronteres](https://www.tributs.ad/)

---

## Section: `--compare`

### Andorra vs neighbours (residential investment lens, Q1–Q2 2026)

| Country | Foreign-buyer rule | Acquisition cost (typical, resident) | Annual recurring | Yield (mid-tier) | Currency |
|---|---|---:|---:|---:|---|
| **🇦🇩 Andorra** | Authorisation required (Llei 10/2012) + non-resident progressive surcharge to ~10% | 5.5–7% (resident) / 8–14%+ (non-resident) | Parish prop. tax low + Foc i Lloc + community fees | 3.5–5% | EUR (Mon. Agreement 2011) |
| **🇪🇸 Spain** | Open; **NIE** required; some regional AJD | 8–14% | IBI 0.4–1.1% catastral | 3–5% (varies CCAA) | EUR (Eurozone) |
| **🇫🇷 France** | Open; *fiscale* + notary process | 7–9% | Taxe foncière + Taxe d'habitation | 2.5–4.5% | EUR (Eurozone) |
| **🇲🇨 Monaco** | Open but supply-constrained; max-CoL | ~8–12% | minimal recurring; no income tax (resident regime) | 1.5–3% | EUR (Mon. Agreement) |

### Andorra's distinctive position

- **Lowest IGI/VAT in Europe** (4.5%) + **0%/5%/10% IRPF** + **no wealth tax** + **no inheritance tax** (direct heirs) → headline tax-residency value-prop
- **Counter-balanced by**: small + thin RE market, foreign-buyer authorisation friction, Llei 3/2024 non-resident surcharge raising acquisition cost materially, no CBI/golden-passport route, 20-year naturalisation
- **Best fit**: tax-residency seekers willing to spend ≥183 days/yr (or ≥90 for passive route), high-net-worth professionals + retirees + remote workers compatible with mountain location
- **Worse fit**: pure non-resident investment-only buyers (post Llei 3/2024 surcharge, IRR squeezed); short-flip strategies (sliding CGT scale 0–15% on holding period)

### Comparative reference

For Andorra vs Monaco / Liechtenstein / San Marino micro-state monetary-agreement parallels see `countries/mc/playbook.md` (when populated) + `countries/li/playbook.md` (when populated). For tax-residency comparison vs Spain/France high-net-worth flight see `countries/es/playbook.md` + `countries/fr/playbook.md`.

---

## Section: `--retirement`

Andorra is a **viable retirement-first destination** for HNW retirees seeking low income tax + EU-proximity healthcare + mountain lifestyle.

### Pathways

1. **Residència passiva** (€800k investment per Llei 5/2025, eff. 16 April 2025 — up from superseded pre-2025 €600k, possibly €1m per Llei 2/2026; + AFA deposit; ≥90 days/yr) — most common retirement route
2. **Family reunification** (sponsored by AD-resident family)
3. **Pre-existing residency** transitioned

### Cost-of-living for retirees (2026 est.)

- Median 2-bed rental Q1 2026: **€1,000–€1,800/month** (capital prime €1,500–€3,000+)
- CASS public healthcare: **75% reimbursement** for residents; private cover €120–€350/month typical for 65+
- Hospital: HNSM (Escaldes-Engordany); Spanish/French specialists 2–3h drive (Toulouse, Barcelona)
- Utilities at altitude: **€200–€500/month** winter heating-driven

### Tax position for retirees

- **No wealth tax, no inheritance tax (direct heirs)** — headline appeal
- Foreign pension income: Andorran-resident IRPF (0/5/10%); DTAs with ES (2016) + FR (2014) eliminate most overlap
- **No CGT after 10-year hold**; sliding 0–15% below

### Verdict for retirement-first buyers

🟢 **Go** for HNW retirees (€800k+ liquid per Llei 5/2025, EUR-denominated, Spanish/Catalan competence) seeking low-tax mountain base with EU-proximity healthcare; 🟡 **Watch** for moderate-wealth (sub-€800k investible) — passive-residency floor + CoL above Portugal/Spain/Greece equivalents on lifestyle-per-euro.

---

## Section: `--digital-nomad`

### Visa pathway

- **No formal digital-nomad visa**. Workable pathways: (1) **Residència passiva** + foreign-employer remote-work — gray area (verify with Servei d'Immigració); (2) **Residència activa self-employed** via SL — clean route but full tax-residency + CASS + IS exposure; (3) Visitor entry (Andorra is NOT in Schengen but external-perimeter aligned) up to 90/180 days. ⚠️ Sustained "working from Andorra" without residency permit case-by-case risk

### Connectivity

- **>95% FTTH** via Andorra Telecom (sole telco) — gigabit fibre standard in all parishes; €30–€50/mo for 1-Gbps; 5G mobile €20–€60/mo
- **Co-working**: L'Hub (Andorra la Vella), HUMAN ID (Escaldes), Andorra Coworking + parish *centres d'innovació*; €150–€400/mo hot desk
- Time zone: UTC+1 (CEST summer); favours EU + East Coast US async; 6h gap to US Pacific

### Cost-of-living for remote worker (2026 est.)

- Studio short-let (HUT-compliant): €700–€1,500/mo; long-let 1-bed: €700–€1,400/mo
- Eating-out: €10–€20 *menú del dia* / €25–€60 mid-range
- Resident remote-worker: **IRPF 0/5/10%** on worldwide income post-residence; SL self-employed = **IS 10%** + IRPF on draws

### Verdict for digital-nomad-first buyers

🟡 **Watch** — strong infrastructure + low CoL + 4.5% IGI / 0–10% IRPF, but tight visa framework (no DNV, gray area sub-residency). Best fit: HN remote-workers committing to ≥183 days active or ≥90 days passive (and €800k investment per Llei 5/2025).

---

## Section: `--macro`

### Headline 2024–2026 ([Estadística](https://www.estadistica.ad/) + [IMF Article IV 2024](https://www.imf.org/en/Countries/AND))

- GDP growth: 2023 ~+1.4% / 2024 ~+1.6% / 2025 fcst +1.5–2.0%
- GDP per capita 2024: ~**€41–44k** (top quartile EU per-capita)
- Inflation: 2024 ~3.5% headline (cooling from 2022 peak ~7%); 2025 ~2.5–3% — tracks ES + FR
- Unemployment 2024: ~1.5–2.5% (bottleneck is work-permit quotas, not demand)
- Public debt / GDP: ~40% stable; IMF positive on fiscal space

### Trend drivers (2024–2026)

- **EU Association Agreement** (text approved by the Council of the EU 16 Jul 2026, signature scheduled 19 Oct 2026, not in force) — single-market spillover scenario if ratified
- **Tax-residency inflows** from ES (Catalonia 2025 wealth-tax + progressive ITP) + FR (IFI flight)
- Tourism: 8–9M visits/year (≥100× population) — Llei 26/2024 tightening STR supply
- IPH 2018–2024 nominal +5–8%/yr; cooling 2024–2025 with rate-cycle peak

[IMF 2024 Article IV](https://www.imf.org/en/Countries/AND) flags external dependence (ES + FR macro), banking-sector concentration (4 banks), and labour-quota tightness as structural watch items.

---

## Section: `--demographics`

### Population structure (end-2024, [Padró aggregated by Estadística](https://www.estadistica.ad/))

- **Total**: ~85,800
- **By nationality** (~2024 padró): Andorran ~48% / Spanish ~24% / Portuguese ~11% / French ~4–5% / other ~12%
- **Median age**: ~46 (ageing; similar to ES, IT); age 65+: ~20% rising
- **Net migration**: ~+800–1,500/yr (talent + family reunification)
- **TFR**: ~1.0–1.1 (very low)
- **Geographic**: Andorra la Vella + Escaldes-Engordany ~50% (metropolitan core); Encamp + Sant Julià ~25%; La Massana + Ordino + Canillo ~25%
- **Households**: ~33,000; avg size ~2.6; owner-occupier ~58%, rental ~42% (high vs rural ES/FR — transient + foreign-resident population)

### Implication for property

- Demand floor 2025–2030: net-positive migration supports mid-tier rental + ownership; foreign-buyer demand absorbed Llei 3/2024 surcharge with some absorption-test signs in 2024–2025
- Supply pipeline: limited new-build capacity (mountain terrain + POUP constraints) → supply-side rigidity supports prices
- Ageing risk: pre-2000 ski-block stock (Pas de la Casa) underperforms as second-home owners age out — opportunity for retrofit-savvy buyers

---

## Section: `--esg`

### Climate-transition exposure

- **Estratègia Energètica i de Lluita contra el Canvi Climàtic** (Llei 21/2018) + **Estratègia 2050**: net-zero by 2050 ([Govern d'Andorra — La Litecc](https://www.govern.ad/ca/ministeris-i-secretaries-d-estat/ministeri-de-medi-ambient-agricultura-i-ramaderia/convenis-i-normativa/la-litecc); law as published at [BOPA 30/57](https://www.bopa.ad/bopa/030057/Pagines/CGL20180928_13_54_03.aspx)) (Llei 21/2018 verified 2026-09-18, source Govern d'Andorra; the net-zero-by-2050 target is not evidenced on the cited pages — verify at govern.ad)
- FEDA decarbonising electricity (hydro + EU import mix); thermal-envelope + heat-pump shift accelerating
- **CEE (Certificat d'Eficiència Energètica)** A–G mandatory at sale/lease per Llei d'eficiència energètica 2018

### Property-level ESG

- CEE A/B: growing in 2020+ chalet stock; CEE F/G typical for pre-1990 ski-blocks → retrofit ~€500–€1,500/m² for thermal + HVAC modernisation
- Heat-pump retrofit incentives via [Servei d'Energia](https://www.energia.ad/) — verify current scheme
- Green mortgages nascent — Crèdit Andorrà, MoraBanc, BancSabadell d'Andorra advertise concessions for high-CEE properties
- Avalanche-corridor + flash-flood basin properties carry rising insurance + resilience cost
- Ski-station base-elevation risk: Pas de la Casa partial (~2,100m base resilient); Vallnord-Arinsal (~1,550m) more exposed → resort-economy spillover

### Verdict (ESG lens for typical mid-altitude AD apt)

🟡 **Watch** — pre-2000 stock progressively below market expectation by 2030; mid-tier retrofit (envelope, heat-pump) becomes mandatory cost; CEE A/B + retrofit stock carries resilience premium.

---

## Section: `--exit`

### Resale market liquidity

- **Average days on market 2025**: ~90–180 days mid-tier apt; ~120–360 days for chalets >€1M
- Cyclical: moderate in upcycle (2018–2022 strong); thin in downcycle (2024–2025 cooling post-Llei 3/2024)
- Estadística IPH quarterly leading indicator; 2025 nominal flat-to-slightly-positive YoY

### Exit-cost stack (seller side)

- Estate agent commission: ~**3–5%** + IGI 4.5% on commission
- Notari fee (seller portion of regulated arancel): smaller share
- **Plusvàlua / CGT**: sliding 0–15% by holding period; **10y+ exempt**; primary-residence exemption with reinvestment
- Mortgage early-discharge: ~€500–€2,000 admin + bank clawback
- **Total exit cost**: typically **3.5–6%** + CGT if any

### Liquidity by sub-segment (qualitative, 2026)

| Segment | Liquidity | Notes |
|---|---|---|
| Mid-tier €350–€800k Andorra la Vella + Escaldes | 🟢 strong | Foreign-resident + local family demand |
| Premium chalet €1–€3M Ordino / La Massana / Canillo | 🟡 selective | HNW relocation flow |
| Ultra-luxe €3M+ Soldeu/Grau Roig ski-front | 🟠 thin | <50 tx/yr; slow price discovery |
| Pas de la Casa pre-2000 ski-blocks | 🟠 weak | Retrofit-cost overhang |
| New-build first-hand (developer release) | 🟢 promo | Resale 6–24mo later sometimes discount-to-launch |
| Borda / heritage rural | 🟡 niche | Cultural-protection layer; local-buyer market |

### Verdict for exit risk

🟢 mid-tier capital-axis apt; 🟡 premium chalet (resilient HNW pool); 🟠 ultra-luxe + Pas de la Casa older stock. Llei 3/2024 surcharge has **chilled non-resident exit demand** for mid-tier non-trophy properties in 2024–2025 — material for seller exit-liquidity modelling.

---

## Cost benchmarks (AD 2026)

| Item | Cost (EUR) |
|---|---:|
| Notari fee (regulated arancel) | 0.5–1.5% of price |
| Registre de la Propietat fee | 0.1–0.5% of price |
| Estate agent commission (each side) | 3–5% of price |
| ITP resale, resident | ~4% (1% Govern + 0.50–3% Comú, most parishes 3% — Llei 1229/2000 art. 8) |
| Llei 3/2024 non-resident surcharge | progressive, est. up to ~10% |
| IGI (new build first sale) | 4.5% of price |
| Foreign-investment file (Llei 10/2012) | 500–2,000 admin |
| Cèdula d'habitabilitat / CEE | 150–500 each |
| Annual property tax (parish, residential) | €0.30–€1.50 per m² built |
| Foc i Lloc + Higiene (parish levies) | 100–500/year combined |
| Community fees (mid-tier apt / old Pas de la Casa block) | 80–250 / 200–500+ /month |
| Fire insurance + home contents (70 m² apt) | 320–1,150/year combined |
| Renovation (basic refresh / full retrofit, 70 m² apt) | 30k–80k / 100k–300k |
| Avalanche-corridor structural reinforcement | 20,000–80,000 |
| **Total transaction cost (resident, resale)** | **~5.5–7%** of price |
| **Total transaction cost (non-resident, resale)** | **~8–14%+** of price |
| **Total transaction cost (new build first sale)** | **~6.5–8%** of price |

## Active fiscal incentives (2025–26)

- **Heat-pump + thermal-envelope retrofit grants** via [Servei d'Energia](https://www.energia.ad/) — verify current scheme + budget-cycle availability
- **Solar PV residential incentive** (limited-quota; renewed annually)
- **No first-time-buyer ITP discount** as standard, but parish-level *bonificacions* exist (e.g., young-family programmes in some Comús)
- **CASS health-coverage transitions** for new residents (gap-cover periods; verify with CASS)
- **Llei 9/2012 passive residency** route still open; investment floor now **€800k (Llei 5/2025, eff. 16 April 2025)** — €600k is superseded (pre-2025), possibly rising to €1m (Llei 2/2026); subject to AFA quantum verification

## Common listing platforms

- **Idealista AD** — biggest Catalan/Spanish-language pool
- **Engel & Völkers AD**, **Sotheby's International Realty AD** — premium / international
- **Habitatclick.ad**, **MM Andorra Real Estate**, **Cisa Inmobiliaria**, **Naturland**
- ⚠️ Many listings are dual-agent (E&V + boutique), often **same property at different prices** across platforms — cross-check by reference + agent code

## Caveats unique to AD

- **Foreign-investor authorisation (Llei 10/2012)**: non-residents need prior Govern authorisation (~2–4 weeks residential) before any RE acquisition
- **Llei 3/2024 non-resident surcharge** (≈ up to 10% est. ceiling): layered on 4% ITP — *verify exact current bands at tributs.ad*
- **Cadastre is parish-level**: every check goes to the target Comú; no single national portal
- **Notari + Registre + Comú + Govern all involved** in any transaction — coordinate via the notari from day 1
- **Currency = EUR by Monetary Agreement (2011)**, NOT Eurozone member; SEPA member since 2016
- **No CBI / golden-passport**, **20-year naturalisation**, dual-nationality not recognized
- **No piped natural gas**: heating is electric / heat-pump / wood / LPG; legacy resistive in pre-2000 ski-blocks expensive
- **Ski-corridor base-elevation risk**: climate trajectory pressuring sub-1,800m resorts (Vallnord-Arinsal exposed)
- **Llei 26/2024 STR**: HUT registration + community vote + parish quota (Andorra la Vella restricted)
- **Llei 1/2024 long-let**: 5-year min term, IPC-capped indexation
- **No CGT after 10y hold** (sliding 0–15% below); **no wealth tax, no inheritance tax** (direct heirs)
- **Top IRPF 10%, IS 10%, IGI 4.5%** — among Western Europe's lowest
- **Avalanche-corridor zoning** in POUP — request parcel hazard layer from Comú before any chalet >1,500m
- **Banking concentration** (4 banks) + Llei 14/2017 AML — non-resident account opening 4–8 weeks
- **Catastre (parish) vs Registre (national)** split — must reconcile both pre-deed
- **EU Association Agreement** — text approved by the Council of the EU 16 Jul 2026, signature scheduled 19 Oct 2026, not in force; single-market spillover scenario if ratified
- **Listing m²**: convention is *m² construïts* (built); confirm vs *m² útils* on visit *(per listing — verify with cadastre / on visit)*

## Reddit / forum sources

- **r/andorra** — small but active; bilingual (Catalan/Spanish/English)
- **r/europe** + **r/IWantOut** — relocation threads
- **Diari d'Andorra** + **El Periòdic d'Andorra** + **Andorra Difusió** — local news (Catalan)
- **Bondia** + **Altaveu** — local news
- **Andorra Living** + **Confluence Tax Andorra** — tax-residency / relocation blogs (advisory, treat with `🟡 anecdotal` ranking)
- **Andorra Insiders** — relocation guidance (advisory)

## Verification authorities

| Authority | When to call |
|---|---|
| **Comú (target parròquia)** | Cadastre extract, parcel ref, parish prop. tax, *certificat de no-deute*, POUP, hazard zoning |
| **Registre de la Propietat (Cort)** | Title verification, *nota simple*, charges + servituds |
| **Notari** | Mandatory closing, ITP/IGI withholding, Llei 3/2024 surcharge calc |
| **Tributs i de Fronteres** | IRPF/IS/IGI/ITP guidance, AML source-of-funds |
| **AFA** | Banking + investor-residency deposit |
| **Servei d'Immigració** | Foreign-investment authorisation (Llei 10/2012), residency permits |
| **Departament de Turisme** | HUT registration + tourist tax |
| **CASS** | Social-security registration (employed + self-employed) |
| **Cos de Policia / Bombers / Servei Meteorològic** | Crime stats / wildfire response / avalanche+snow+climate baseline |
| **FEDA / Andorra Telecom / CCIS** | Electricity+district heating / fibre / RE market reports + SL setup |

## Source URL templates

| Source | URL |
|---|---|
| Govern d'Andorra | `https://www.govern.ad/` |
| BOPA (Butlletí Oficial) | `https://www.bopa.ad/` |
| Departament d'Estadística | `https://www.estadistica.ad/` |
| AFA (Autoritat Financera Andorrana) | `https://www.afa.ad/` |
| Tributs i Fronteres / Tràmits / Immigració | `https://www.tributs.ad/` · `https://www.tramits.ad/` · `https://www.immigracio.ad/` |
| Turisme / Mobilitat / Meteo / Medi Ambient / Energia | `https://www.turisme.ad/` · `https://www.mobilitat.ad/` · `https://www.meteo.ad/` · `https://www.mediambient.ad/` · `https://www.energia.ad/` |
| FEDA / Andorra Telecom / CASS / Policia / Bombers / SAAS / CCIS | `https://www.feda.ad/` · `https://www.andorratelecom.ad/` · `https://www.cass.ad/` · `https://www.policia.ad/` · `https://www.bombers.ad/` · `https://www.saas.ad/` · `https://www.ccis.ad/` |
| Comú Andorra la Vella / Escaldes-Engordany / Encamp / Canillo | `https://www.comuandorra.ad/` · `https://www.e-e.ad/` · `https://www.comuencamp.ad/` · `https://www.canillo.ad/` |
| Comú Ordino / La Massana / Sant Julià de Lòria | `https://www.ordino.ad/` · `https://www.lamassana.ad/` · `https://www.santjulia.ad/` |
| Idealista AD / Engel & Völkers AD / Sotheby's AD | `https://www.idealista.com/ca/andorra/` · `https://www.engelvoelkers.com/ca-ad/andorra/` · `https://www.andorra-sothebysrealty.com/en` |
| OPCC Pyrenees Climate Observatory | `https://www.opcc-ctp.org/` |

## Status

**Confidence**: MEDIUM — HIGH for the foundational legal/fiscal framework (ITP split 1% Govern + 0.50–3% Comú per Llei 1229/2000 art. 8.1+8.2, IEI two-tier 6%/10% post-Llei 5/2025, Llei 5/2025 "Llei Òmnibus" foreign-investor cap, negative-silence rule per Llei 3/2024, AFA deposit split, Passive-residency tier ladder €600k → €800k → possible €1m), bopa.ad primary statutes, and Comú-level transfer tax confirmation. MEDIUM for parcel-level Comú variation within the 0.50–3% ITP band (verify per parcel with Comú treasurer), Llei 2/2026 forward-flag detail, and 2026 minimum-wage / IRPF effective-rate parentheticals (verify at gov.ad). MEDIUM for residential price benchmarks (no national HPI; aggregator listing data with foreign-buyer bias).

**Last verified**: 2026-05-27 (EU Association Agreement status corrected 2026-09-18 and 2026-09-24 per Govern d'Andorra AA portal)

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Locked-in via primary government sources: foreign-investor authorisation regime (Llei 10/2012 BOPA + Servei d'Immigració), Llei 3/2024 non-resident RE surcharge (BOPA Feb 2024 — *exact progressive bands have been adjusted multiple times in 2024 and remain politically sensitive; verify current rate at tributs.ad before any non-resident purchase*), ITP ~4% split 1% Govern + 0.50–3% Comú (most parishes 3%) per Llei 1229/2000 art. 8.1+8.2 (BOPA + Comú confirmation), IGI 4.5% (Llei 11/2012), IRPF 0/5/10 + IS 10 (Llei 5/2014), residency-by-investment quantum €800k current (Llei 5/2025; €600k superseded pre-2025, possibly €1m per Llei 2/2026) + AFA deposit (Llei 9/2012 — verify current AFA deposit at afa.ad), Llei 1/2024 long-let + Llei 26/2024 short-let HUT (BOPA 2024), EUR Monetary Agreement (EU/Andorra 2011 OJ), parish cadastre split (Comú-by-Comú, no national portal), Cos de Policia annual Memòria for crime, Servei Meteorològic + OPCC for climate. **Re-verify each annual budget law (Llei de Pressupostos)** for any ITP/IGI/IRPF adjustment, the Llei 3/2024 surcharge bands, AFA deposit quantum, and the salari mínim decree. **Watch list 2026**: EU Association Agreement ratification (2024–2026 negotiation; signing slipped past 2025 — major regulatory-spillover event if ratified); Llei 3/2024 surcharge potential adjustment with pre-2027 budget cycle; any Pas de la Casa ski-station refurbishment + altitude-base climate-adaptation programme; new POUP cycles per parish (avalanche zoning + new-build limits).

## Extension TODOs (deepen on first real run)

- [ ] Per-parròquia property-tax rate matrix (7 Comús × residential band)
- [ ] Llei 3/2024 progressive-band table once stable (post-2026 budget)
- [ ] Avalanche-corridor + landslide POUP layer extraction (per parish)
- [ ] HUT registry quota tracking by parish (Llei 26/2024 implementation)
- [ ] Pas de la Casa pre-2000 ski-block retrofit cost benchmark
- [ ] 4-bank non-resident mortgage product comparison
- [ ] EU Association Agreement single-market spillover scenario modelling
- [ ] Snow-line-rising impact map per ski-domain base elevation
