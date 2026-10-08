# Poland 🇵🇱 — Property Due-Diligence Playbook

ISO2: `pl`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits in `XX-XXX` format (`00-001` Warsaw centro, `30-001` Kraków, `80-001` Gdańsk, `50-001` Wrocław)
- **Admin levels**: 16 województwa (voivodeships) + 380 powiaty + 2,477 gminy
- **Currency**: **PLN (Polish złoty)** — 1 EUR ≈ 4.30–4.60 PLN (volatile)
- **Languages**: Polish (official); Kashubian, German, Belarusian (regional minorities)
- **Cadastre**:
  - **EKW (Elektroniczne Księgi Wieczyste, electronic land register)**: `https://ekw.ms.gov.pl/`
  - **Geoportal2** (national geoportal): `https://www.geoportal.gov.pl/`
  - **EGiB (Ewidencja Gruntów i Budynków)**: cadastre, accessed via gmina/powiat geoportals
  - **ZSIN (Zintegrowany System Informacji o Nieruchomościach)**: integrates EKW + EGiB
- **Identifier**: numer KW (e.g., `WA1M/12345678/9` — court code + sequence + check digit)
- **Ownership types**:
  - **Własność** (full ownership)
  - **Użytkowanie wieczyste** (perpetual usufruct, gradually being abolished — converted to ownership for housing since 2019)
  - **Spółdzielcze prawo własnościowe / lokatorskie** (cooperative ownership)
  - **Najem** (rental)
- **EU member since 2004**; not in eurozone (PLN remains)

## Section: `--price`

### Primary sources

- **NBP BaRN database** (since Q3 2006): `https://nbp.pl/publikacje/cykliczne-materialy-analityczne-nbp/rynek-nieruchomosci/informacja-kwartalna/`
  - Quarterly residential price reports — National Bank of Poland authoritative data
- **AMRON-SARFiN** (Polish Banking Association): `https://amron.pl/raporty/`
  - Bank valuation + transaction + mortgage finance data; quarterly
- **GUS (Główny Urząd Statystyczny)**: `https://stat.gov.pl/` — national statistics
- **Otodom Analytics**: `https://analytics.otodom.pl/en` — combines NBP/GUS/BIK/AMRON-SARFiN; gated for agents/developers
- **EKW** for individual title lookup (read-only by KW number, paid certified outprints)
- **Geoportal2** for parcel maps + zoning

### Listing platforms

- **Otodom** (OLX Group) — DOMINANT (~6.7M users): `https://www.otodom.pl/`
- **Morizon Group** (Morizon + Gratka + Noweinwestycje.pl): `https://www.morizon.pl/`
- **Nieruchomosci-online**: `https://nieruchomosci-online.pl/`
- **Domiporta**: `https://www.domiporta.pl/`
- **OLX Nieruchomości** within OLX Group: `https://www.olx.pl/nieruchomosci/`

### 2025 price benchmarks (NBP BaRN + AMRON)

| Region | Avg PLN/m² (apt) | Avg total (single-family) |
|---|---:|---:|
| **Warszawa centrum** | 17,000–25,000+ | 1,800,000–4,500,000+ |
| **Warszawa periphery** | 12,000–17,000 | 1,200,000–2,200,000 |
| **Kraków centrum** | 14,000–20,000 | 1,400,000–2,800,000 |
| **Kraków periphery** | 10,000–14,000 | 1,000,000–1,800,000 |
| **Wrocław** | 11,000–15,000 | 1,000,000–1,800,000 |
| **Gdańsk / Gdynia / Sopot** | 12,000–18,000 | 1,100,000–2,200,000 |
| **Poznań** | 10,000–14,000 | 950,000–1,600,000 |
| **Łódź** | 7,500–11,000 | 700,000–1,200,000 |
| **Smaller cities** | 6,000–9,500 | 550,000–1,000,000 |
| **Rural eastern PL** | 3,000–5,500 | 250,000–550,000 |

### Compute

1. PLN/m² = price / **powierzchnia użytkowa** (usable area, PN-ISO 9836)
2. **Sprawdź KW** — read all 4 sections of land register (I-O property, I-Sp rights, II ownership, III encumbrances, IV mortgage)
3. **Convert to EUR** at current FX (PLN volatile)
4. **Real Estate Reports** from NBP quarterly for area trend

### Key terms

- KW (Księga wieczysta) = land register
- Własność = ownership
- Użytkowanie wieczyste = perpetual usufruct (legacy)
- Spółdzielnia mieszkaniowa = housing cooperative
- Wspólnota mieszkaniowa = HOA for apartment building
- Świadectwo CEN = energy certificate

---

## Section: `--traffic`

### Sources

- **GDDKiA** (Generalna Dyrekcja Dróg Krajowych i Autostrad): `https://www.gov.pl/web/gddkia` — national roads
- **GPR (Generalny Pomiar Ruchu)** — every 5 years, complete national count
- **Per-województwo road authority** for regional roads
- **Per-gmina** for local

### Key term

**SDR (Średni Dobowy Ruch)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (rural roads, residential streets)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (urban arterial, voivodeship roads)
- 🔴 > 35,000 v/d (motorway, expressway, Warsaw arterials)

---

## Section: `--tax`

### Annual property tax — Podatek od nieruchomości (PoN)

#### 2025 reform (CONFIRMED)

**Effective 1 January 2025**: new statutory definitions of *budynek* (building) vs *budowla* (structure) in Annex 4 (28 categories) to *Ustawa o podatkach i opłatach lokalnych*.
- Triggered by Constitutional Court ruling 4 July 2023 (existing definitions unconstitutional, 18-month deadline to fix)
- Decoupled from Building Law — both require "construction works" basis
- Sources: Wolters Kluwer, EY, TPA, Grant Thornton confirm

#### 2026 max rates (Ministry of Finance Obwieszczenie 1 August 2025, +4.5% indexation)

| Category | Max rate |
|---|---:|
| **Residential building** | **1.25 PLN/m²/yr** |
| **Land under residential** | **0.77 PLN/m²/yr** |
| **Business-use building** | **35.53 PLN/m²/yr** |
| **Business-use land** | **1.45 PLN/m²/yr** |
| **Other building** | 11.92 PLN/m²/yr |

- Each gmina sets its actual rate by uchwała before year-end
- Typical residential: **~150–500 PLN/yr** for apartment, **~600–2,000 PLN/yr** for single-family

### Transaction taxes

- **PCC (Podatek od czynności cywilnoprawnych)**: **2%** on resale (paid by buyer)
- **PCC 6% bulk-buyer rate (od 1.01.2024)**: 6% PCC on the **6th+ lokal mieszkalny on the same nieruchomość gruntowa** purchased from a developer (joint-ownership counts toward threshold; rate **stacks with VAT** — exception to no-PCC-with-VAT rule). Source: Ustawa z 26.05.2023, **Dz.U. 2023 poz. 1463** (2026-05-27 verified)
- **First-home exemption since 31 August 2023** (secondary market only):
  - Single-family house or flat
  - <50% inherited share allowed
  - Spouses both qualify
  - No prior ownership ≥50% in any property
- **VAT (new build)**: **8%** residential ≤150 m² flat / ≤300 m² house; 23% above; 23% other RE
- **Notariusz** fees: ~1.0–2.0% of price (graduated scale + VAT)
- **Sąd (court) fees**: KW entry ~200 PLN

### Total transaction cost (buyer side)

- **First-home (primary, exempt)**: ~3–4% (notary + court + lawyer)
- **Resale, second home / BTL**: ~6–8% (2% PCC + 1-2% notary + others)
- **New build (developer)**: 8% VAT included; ~3% other costs

### Capital gains

- **PIT 19%** if sold within **5 years** from end of acquisition year
- **Exempt after 5 years**
- **Exempt** if proceeds reinvested in own housing within 3 years
- Inheritance + gifting: separate scale (Group I close family up to ~PLN 36,120 exempt — est., indexed/periodically revised; verify current amount at podatki.gov.pl / Ustawa o podatku od spadków i darowizn before relying on it)

### Future risk

- **PoN reform definitions** still being litigated case-by-case
- **Użytkowanie wieczyste conversion** ongoing for residential
- **EU 2024/1028 short-let** transposition slipping to 15 Oct 2026

---

## Section: `--rental`

### Long-term residential

- **Najem instytucjonalny** (institutional lease) — landlord-friendly form (since 2017)
- **Najem okazjonalny** (occasional lease) — limited-term, notarial
- **Najem standardowy** (standard) — Civil Code; tenant-protected
- Caps on rent increase: CPI-based for some forms

### Short-let (Najem krótkoterminowy)

**EU 2024/1028 transposition status (as of April 2026)**:
- NOT yet enacted in Poland
- Government draft + Polska 2050 draft submitted to Sejm 14 Apr 2026
- Central registry under **Ministerstwo Sportu i Turystyki**
- **Deadline pushed to 15 Oct 2026** for gmina implementation
- **Penalties up to 50,000 PLN**
- Platforms (Airbnb/Booking) banned from listing without ID

#### Local rules

- **Kraków + Warsaw**: operator registration required
- **Kraków uchwała krajobrazowa** (advertising/landscape ordinance) — broader than STR-specific
- **Sopot, Gdańsk, Wrocław**: tightening rules

### Tax on rental

- **Najem prywatny (since 1 stycznia 2023)**: ryczałt is the **only allowed form** — **8.5%** up to PLN 100,000/yr (single) or PLN 200,000/yr (spouses jointly); **12.5%** above; **no deduction of costs** and no tax-free amount (2026-05-27 verified, source: podatki.gov.pl / Ustawa o zryczałtowanym podatku dochodowym). PIT progressive scale **NO LONGER available** for najem prywatny — only if rental conducted as działalność gospodarcza (separate ZUS + accounting).
- **Kasa fiskalna** required if turnover >20,000 PLN/yr (some thresholds)
- **VAT 8%** on short-let services if registered (above €40k turnover ~ 200,000 PLN)

---

## Section: `--work=<profession>`

### Sources

- **Pracuj.pl** — biggest job board: `https://www.pracuj.pl/`
- **OLX Praca**, **Indeed.pl**, **LinkedIn PL**
- **Urząd Pracy** (employment office) per powiat

### Self-employment

- **JDG (Jednoosobowa działalność gospodarcza)** — sole trader
  - **Składki ZUS** (~1,485 PLN/mo full, less for small business "Mały ZUS")
  - **PIT 12%/32%** progressive OR **podatek liniowy 19%** OR **ryczałt** (flat-rate by category)
- **Sp. z o.o.** (limited): min 5,000 PLN capital
- **VAT registration**: from 200,000 PLN turnover (some sectors mandatory)

### Salary benchmarks (2025)

- Median monthly gross:
  - Warszawa: ~PLN 8,500–13,000
  - Kraków, Wrocław, Gdańsk: ~PLN 7,500–11,000
  - Smaller cities: ~PLN 6,000–8,500
- **Minimum wage (płaca minimalna)**: PLN 4,666 gross monthly (2026)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Wody Polskie** (waters management) | `https://www.gov.pl/web/wody-polskie` | Flood + water management |
| **ISOK flood maps** | `https://wody.isok.gov.pl/` | Flood hazard maps |
| **IMGW** (meteorology + hydrology) | `https://www.imgw.pl/` | Weather, climate |
| **PIG-PIB** (Geological Institute) | `https://www.pgi.gov.pl/` | Geology, mining subsidence |
| **PAA (Państwowa Agencja Atomistyki)** | `https://monitoring.paa.gov.pl/maps-portal/` | Radon |
| **Państwowa Inspekcja Sanitarna** (Sanepid) — radon zone monitoring |
| **GIOŚ** (env protection) | `https://www.gov.pl/web/gios` | Air, water, soil quality |
| **Polski Alarm Smogowy** | `https://polskialarmsmogowy.pl/` | Air quality monitoring |
| **Airly** | `https://airly.org/map/` | Live PM2.5 data |
| **Czyste Powietrze** | `https://czystepowietrze.gov.pl/` | Anti-smog programme |
| **Baza Azbestowa** | `https://bazaazbestowa.gov.pl/` | Asbestos legacy register |

### Specific risks

- **Floods** — major risk:
  - **Wisła (Vistula), Odra (Oder), Warta** river basins
  - **Storm Boris September 2024**: catastrophic flooding in Kłodzko, Nysa, Opolskie, Dolnośląskie, Śląskie, Małopolskie
    - 9 dead, 57k affected, 6.5k evacuated
    - State of natural disaster declared 16 Sep 2024
  - 1997 "Powódź tysiąclecia" + 2010 events as historic references
- **Smog / PM2.5** — major Polish issue:
  - PM10 +7% in 2024 vs 2023 (reversal of improvement)
  - Worst: Łódzkie, Śląsk, Małopolska
  - **~2.5M legacy "kopciuchy" boilers** ≈ est. ~86% national PM2.5 (annually-shifting; cite Polski Alarm Smogowy / GIOŚ + year before relying on it)
  - **Małopolska anti-smog uchwała** XXXV/527/17 (2017):
    - Kraków solid-fuel ban since 1 Sep 2019
    - Rest of Małopolska — non-compliant boilers banned end of April 2024
    - Class 3/4 boilers banned end of 2026
    - Fireplaces must hit ecodesign or 80% efficiency since 1 May 2024
- **Mining subsidence (szkody górnicze)**:
  - **Górnośląski Zagłębie Węglowe (USCB)** — ~1,000 tremors/yr ML≥1.5; >56,000 since 1974
  - **Bełchatów lignite** — ~60 tremors/yr; max ML 4.6 (29 Nov 1980)
  - **KGHM copper** Polkowice/Rudna/Lubin in Dolnośląskie
  - Regulated under Prawo geologiczne i górnicze
- **Radon**:
  - **PAA radiation map**: `https://monitoring.paa.gov.pl/maps-portal/`
  - **Radon-specific**: `https://www.gov.pl/web/poznajradon/mapy-radonowe2`
  - **Hotspots**: Karkonosze + Strzegom granites, Izerskie/Kaczawa metamorphics, Kłodzko Basin, Suwalszczyzna (NE)
- **Earthquake**: low (Polish Plate); historical induced seismicity from coal mining
- **Heatwaves + drought**: increasing climate risk
- **Storm damage**: increasing frequency in NE + central PL

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1939 kamienica** | Lead paint, lead pipes, no DPC, damp, structural settlement |
| **PRL Wielka Płyta (1957–1990)** | ~8M residents in panel blocks; thermal bridges, slab-joint leaks, acoustic, **50yr design life** |
| **Eternit/asbestos roofing** | National program 2002, removal deadline **31 Dec 2032** |
| **1990s–2000s** | Improved insulation; some asbestos remains |
| **Post-2017 WT** | Modern energy + acoustic standards |
| **Post-2021** | NZEB-equivalent (energy class C minimum) |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Świadectwo charakterystyki energetycznej (CEN)** | Mandatory at sale/rent since **28 April 2023** (Ustawa o charakterystyce energetycznej amendment) | 10 years |
| **KW outprint (odpis z księgi wieczystej)** | Title verification | Current |
| **Zaświadczenie o wymeldowaniu** | Confirms no one registered at address | ≤2-3 days old |
| **Wypis z rejestru gruntów + kartoteki lokali** | Cadastre extract | Current |
| **Podstawa nabycia** | Acquisition basis (prior deed) | Per case |
| **Zaświadczenie o braku zaległości czynszowych** | If apartment | Current |
| **Penalty for missing CEN** | up to **5,000 PLN**; recorded in akt notarialny | n/a |

### Climate change projections

- +2.5–4.0 °C by 2100
- Reduced summer precipitation, increased winter
- More extreme rainfall (Boris 2024 type)
- More frequent heatwaves
- Shorter winters, less snow

---

## Section: `--mains`

### Sources

- **WPK (Wodociągi i Kanalizacja)** per gmina (Miejskie/Gminne Przedsiębiorstwo Wodociągów i Kanalizacji)
- **Cesspits emptying** ~40 PLN/m³ (vs ~10 PLN/m³ on mains) — economic disincentive
- **Eastern + southern rural areas** worst-served

### Verification

- **Major cities**: universal mains
- **Rural sewerage coverage** historically lower (~42% rural per 2017-2019 academic data)
- **Suburbs**: mixed; check gmina **Krajowy Program Oczyszczania Ścieków Komunalnych (KPOŚK)** for upgrade plans
- **Szambo** (cesspit) common in rural east + south

### Costs

| Scenario | Cost (PLN) |
|---|---:|
| Przyłącze do sieci wodociągowej | 5,000–15,000 |
| Przyłącze do kanalizacji | 8,000–25,000 |
| Szambo to mains | 12,000–35,000 |
| Przydomowa oczyszczalnia ścieków | 10,000–25,000 |
| Studnia głębinowa | 8,000–20,000 |

---

## Cost benchmarks (PL 2026)

| Work | Cost (PLN) |
|---|---:|
| Świadectwo CEN | 600–1,500 |
| Notariusz | 1.0–2.0% of price |
| KW + sąd fees | 200–500 |
| PCC (resale, non-FTB) | 2% |
| Realtor | 2-3% per side |
| **Total transaction cost (FTB exempt)** | **~3–4%** |
| **Total transaction cost (resale, second home)** | **~6–8%** |
| **Total transaction cost (new build, 8% VAT included)** | **~3–4%** |
| Asbestos eternit removal | 4,000–15,000 |
| Wielka Płyta refurbishment | 30,000–80,000 |
| Roof renovation | 15,000–50,000 |
| Energy retrofit (Class E → A) | 60,000–150,000 |
| Boiler upgrade (kotła ekodesignowy) | 12,000–30,000 |
| Heat pump | 35,000–70,000 |
| Solar PV | 25,000–60,000 |

## Active fiscal incentives (2025-2026)

- **Czyste Powietrze**: max **PLN 136,200** (priority); air-quality-driven retrofit
  - **31 March 2025 reform**: gas/oil/fossil boilers no longer eligible (per EPBD)
  - Pellet boilers without emergency grate only
  - Pivot to heat pumps + PV
  - Separate gas-boiler subsidy window reopened **15 July 2025** for legacy 2024 investments (3-month)
- **Mój Prąd** (PV): up to PLN 7,000 grant
- **Stop Smog**: low-income retrofit
- **Mieszkanie bez wkładu własnego**: state-guaranteed mortgage for first home
- **Bezpieczny Kredyt 2%**: launched 1 lipca 2023; **applications closed early January 2024** (budget exhausted) — subsidy continues for already-approved borrowers through 10-yr subsidy period (2026-05-27 verified, source: BGK / Ministerstwo Rozwoju)
- **Kredyt #naStart / Mieszkanie na Start**: planned successor (project 8.04.2024); **withdrawn end of 2024**, funds redirected to powódź Boris relief
- **Pierwsze Klucze**: latest mooted replacement (MRiT, 2025); **NOT enacted as of May 2026**; legislative limbo
- **Rodzinny dom** scheme: families with 3+ kids

## Common listing platforms

- **Otodom** — biggest
- **Morizon Group** (incl. Gratka, Noweinwestycje.pl)
- **Nieruchomosci-online**, **Domiporta**, **OLX Nieruchomości**

## Caveats unique to PL

- **PoN 2025 reform**: new "budynek" vs "budowla" definitions effective 1 Jan 2025; case-by-case litigation expected
- **PCC first-home exemption since 31 Aug 2023** — secondary market only
- **8% VAT on small new residential** (≤150 m² flat / ≤300 m² house)
- **Currency risk** (PLN volatile vs EUR)
- **CHF mortgage scandal** — 2002-2008 vintage; ongoing court battles; SN judgment November 2024 set "frankowicze" precedent
- **Użytkowanie wieczyste**: legacy form — converted to ownership for housing 2019; commercial still in use
- **Spółdzielcze własnościowe prawo do lokalu** — cooperative ownership (separate from KW); convert to full ownership recommended
- **Wspólnota mieszkaniowa** (HOA): arises automatically from sale of first lokal (art. 6 UWL); **"duża wspólnota" = ≥ 4 lokali (since 1.01.2020 UWL nowelizacja)** with mandatory zarząd; mała wspólnota (≤ 3 lokale) operates under Kodeks cywilny współwłasność rules (2026-05-27 verified, source: Ustawa o własności lokali ISAP)
- **Foreign-buyer regime — Ustawa z 24.03.1920 o nabywaniu nieruchomości przez cudzoziemców**: non-EU/EEA/Swiss buyers need **MSWiA permit** (zezwolenie ministra właściwego ds. wewnętrznych) for property acquisition; EU/EEA/Swiss exempt since 1 May 2004 for residential (agricultural restrictions lifted 1 May 2016 but Ustawa o kształtowaniu ustroju rolnego still applies). Non-EU buying standalone **lokal mieszkalny**: no permit required (2017 amendment); buying **house+land or agricultural**: permit required, discretionary 2-6 months (2026-05-27 verified, source: gov.pl/web/mswia / ISAP).
- **Okres ochronny (1 listopada – 31 marca)**: seasonal moratorium on eviction execution under art. 16 ust. o ochronie praw lokatorów (Ustawa z 21.06.2001); does NOT apply to najem okazjonalny + najem instytucjonalny — which is precisely why these forms exist.
- **Świadectwo CEN mandatory since 28 Apr 2023**
- **Storm Boris 2024** = recent reform-driver event
- **Małopolska anti-smog**: most restrictive in Poland; Kraków zero-emission since 2019
- **Eternit removal deadline 31 Dec 2032** — major remaining stock
- **Wielka Płyta** refurbishment ongoing; designed for 50-year life, mostly past that now
- **EU 2024/1028 STR transposition slipping** to 15 Oct 2026
- **Czyste Powietrze 31 March 2025**: gas boilers no longer eligible — pivot to heat pumps
- **Mining subsidence** documented + compensable in USCB + Bełchatów + Polkowice areas
- **Radon hotspots**: Karkonosze, Sudety, Kłodzko, Suwalszczyzna
- **CHF "frankowicze"** mortgage holders — major civil case backlog
- **Income from rental**: ryczałt 8.5%/12.5% best for most landlords

## Reddit / forum sources

- **r/poland** — biggest community
- **r/Polska** (Polish-language)
- **r/Warsaw**, **r/krakow**, **r/wroclaw**, **r/Gdansk**
- **r/PolskaPolityka** — political/regulatory discussions
- **Bankier.pl** forums — financial
- **Notes from Poland** (English news)
- **DomPlus.pl**, **Murator.pl** — building/renovation

## Verification authorities

| Authority | When to call |
|---|---|
| **Sąd Rejonowy (KW department)** | Title verification |
| **Geoportal2 / EGiB** | Cadastre extract |
| **Notariusz** (mandatory for sale) | Final transfer |
| **Urząd Skarbowy** | PCC, PIT, capital gains |
| **Gmina** | PoN, planning, permits |
| **Wody Polskie** | Flood risk |
| **PAA** | Radon |
| **Wspólnota mieszkaniowa** / **Spółdzielnia** | If apartment |
| **Sanepid** | Radon, water quality |
| **GIOŚ** | Air quality |

## Source URL templates

| Source | URL pattern |
|---|---|
| EKW | `https://ekw.ms.gov.pl/` |
| Geoportal2 | `https://www.geoportal.gov.pl/` |
| NBP BaRN | `https://nbp.pl/publikacje/cykliczne-materialy-analityczne-nbp/rynek-nieruchomosci/` |
| AMRON | `https://amron.pl/raporty/` |
| Otodom | `https://www.otodom.pl/` |
| Wody Polskie | `https://www.gov.pl/web/wody-polskie` |
| ISOK floods | `https://wody.isok.gov.pl/` |
| PAA radon | `https://monitoring.paa.gov.pl/maps-portal/` |
| Czyste Powietrze | `https://czystepowietrze.gov.pl/` |
| Baza Azbestowa | `https://bazaazbestowa.gov.pl/` |
| Polski Alarm Smogowy | `https://polskialarmsmogowy.pl/` |
| GUS | `https://stat.gov.pl/` |
| GDDKiA traffic | `https://www.gov.pl/web/gddkia` |
| GIOŚ | `https://www.gov.pl/web/gios` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing (NBP + AMRON + Otodom), traffic (GDDKiA SDR), tax (PoN 2025 reform + 2026 max rates from Aug 2025 Obwieszczenie), rental (najem types + STR transposition), work, risks (smog + Boris 2024 + radon + mining), mains all have primary government sources + cost benchmarks.
**Confidence**: HIGH for PoN 2025 reform (Wolters Kluwer + EY + TPA + Grant Thornton confirm new budynek/budowla definitions); HIGH for PCC first-home exemption (31 Aug 2023); HIGH for 2026 max rates (MF Obwieszczenie 1 Aug 2025); HIGH for świadectwo CEN mandate (28 Apr 2023); HIGH for Storm Boris 2024 + Małopolska anti-smog; MEDIUM for STR transposition (in flux, dates slipping); MEDIUM for rural sewerage % (older academic figure, fresh GUS table needed).

## Extension TODOs

- [ ] Per-gmina PoN rates (uchwały)
- [ ] PoN 2025 reform case law tracker (budynek vs budowla disputes)
- [ ] Małopolska anti-smog implementation deadline tracker
- [ ] Storm Boris 2024 affected zone overlay
- [ ] Wielka Płyta block inventory by city
- [ ] Eternit removal progress per gmina (2032 deadline)
- [ ] Mining subsidence zones overlay (USCB + Bełchatów + Polkowice)
- [ ] Radon zone overlay per powiat
- [ ] EU 2024/1028 STR transposition tracker
- [ ] CHF "frankowicze" case law summary
- [ ] Czyste Powietrze 31 Mar 2025 gas-boiler transition
- [ ] First-home PCC exemption decision tree
