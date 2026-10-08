# Slovakia 🇸🇰 — Property Due-Diligence Playbook

ISO2: `sk`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **PSČ (postcode)**: 5 digits in `NNN NN` format (e.g., `811 01` Bratislava, `040 01` Košice)
- **Admin levels**: 8 kraje → 79 okresy → 2,890 obce + 138 mestá
- **Currency**: **EUR (€)** — adopted 1 January 2009 (no FX risk vs CZ which still uses CZK)
- **Languages**: Slovak (official); Hungarian minority (south, ~9 % of population), small Rusyn / Ukrainian / Roma
- **Cadastre**: **ÚGKK SR** (Úrad geodézie, kartografie a katastra Slovenskej republiky)
- **Identifier**: parcela číslo + katastrálne územie + obec; LV (list vlastníctva) = title deed
- **CRITICAL note**: **No transfer tax (nadobúdacia daň) since 2005** — buyer-side costs very low like CZ
- **Civil code**: based on the older Czechoslovak Občiansky zákonník; reformed but no NOZ-style overhaul like CZ 2014
- **Bratislava-centric market**: prices in BA are 1.5–2.5× higher than the rest of the country

## Section: `--price`

### Primary sources (cadastre + price)

- **ÚGKK SR ZBGIS Mapa** (FREE, official map application):
  - Portal: `https://zbgis.skgeodesy.sk/mapka/sk/kataster`
  - Search parcels + buildings directly on the map
  - Layer toggling for cadastral data
- **CICA Portal** (informative LV viewing, free):
  - `https://kataster.vugk.sk` — the standard Public Cadastre System
  - For quick check of LV / parcela / building data
- **eSKN Portal** (electronic LV for legal proceedings):
  - `https://kataster.skgeodesy.sk/eskn-portal/`
  - Login via Slovensko.sk (eID)
- **Katasterportal.sk** (free informative LV download):
  - `https://www.katasterportal.com/`
  - Free LV PDF; not legally binding

**CRITICAL distinction**: CICA viewing is **informative only**. For mortgage, court, or notary purposes you need the **official electronic LV from eSKN** (paid via slovensko.sk eID).

### Price benchmarks (mid-2025)

- **Realitný barometer** (Realitná únia) — monthly market index: `https://www.realitnaunia.sk/realitny-barometer`
- **Realitymap.sk** — cenová mapa SK: `https://realitymap.sk`
- **NBS (Národná banka Slovenska)** — Residential property prices by region: `https://nbs.sk/en/statistics/selected-macroeconomics-indicators/residential-property-prices/residential-property-prices-by-regions/`
- **trh.sk štatistiky cien**: per okres breakdowns
- **Reality Radar cenová mapa**: `https://realityradar.eu/cenova-mapa-slovenska`

### 2025 average price benchmarks (byty)

(City averages per Realitná únia / Realitymap.sk / Reality Radar cenová mapa, 2025 — sources listed above; rates/figures may have changed since. Top three rows are reported city averages; rows prefixed `~` are estimates.)

| Mesto | Avg cena bytu | Avg plocha | €/m² (byty) |
|---|---:|---:|---:|
| **Bratislava** | €223,721 | 72 m² | **3,107 €/m²** |
| **Košice** | €135,922 | 71 m² | **1,914 €/m²** |
| **Žilina** | €130,203 | 77 m² | **1,691 €/m²** |
| Trnava (BA satellite) | ~€180k | ~70 m² | ~2,500–2,800 €/m² |
| Banská Bystrica | ~€110k | ~70 m² | ~1,500–1,700 €/m² |
| Prešov | ~€100k | ~70 m² | ~1,400–1,600 €/m² |
| Trenčín | ~€115k | ~70 m² | ~1,600–1,800 €/m² |
| Nitra | ~€110k | ~70 m² | ~1,500–1,700 €/m² |
| Rural / smaller towns | varies wildly | varies | 600–1,500 €/m² |

### 2025 trend

- May 2025 Realitný barometer: **3,070 €/m²** Bratislava / capital-region avg (per Realitná únia barometer; YoY +13.2 %) — note this is a capital-region figure, NOT a national mean (the national average is far lower given BA is 1.5–2.5× the rest of the country)
- Q4 2025 expected to close with double-digit YoY growth nationally

### Listing platforms

- **Nehnutelnosti.sk** — largest, full coverage: `https://www.nehnutelnosti.sk/`
- **Reality.sk**: `https://www.reality.sk/`
- **Topreality.sk**: `https://www.topreality.sk/`
- **Bazoš.sk** — privates, no agency: `https://reality.bazos.sk/`
- **Zoznam Realit**, **Realtbilliard**
- Agency networks: Bond Reality, M&M Reality, Lexxus Reality, RE/MAX SK

### Compute

1. Listing €/m² = listing price / úžitková plocha (or zastavaná plocha for non-byt)
2. Compare to NBS regional benchmark for the kraj
3. Compare to Realitná únia barometer monthly value
4. **Trap**: úžitková plocha (usable) vs zastavaná plocha (built-up footprint) vs podlahová plocha (floor area) — clarify which the listing uses
5. **Trap**: novostavby often advertise **bez DPH** (without VAT); the 5 % DPH rate on building supply is a retained pre-2025 rate limited to state-supported rental-housing projects — not a first-time-buyer rate (Finančná správa); verify the DPH applicable with the developer

---

## Section: `--traffic`

### Primary sources

- **SSC Celoštátne sčítanie dopravy 2022-2023**: `https://www.ssc.sk/sk/cinnosti/rozvoj-cestnej-siete/dopravne-inzinierstvo/celostatne-scitanie-dopravy-v-roku-2022-a-2023.ssc`
  - 2,757 sčítacích miest covered
  - Traffic increased +14 % since 2015 census across all road types
- **Open data ArcGIS Hub**: `https://hub.arcgis.com/datasets/3fce14460a694592b06641d67d83d6c3`
- **CDB (Cestná databanka)**: `https://www.cdb.sk/sk/Vystupy-CDB/Mapy-cestnej-siete-SR.alej`
  - Maps by správca (D + I + II + III triedy)
- **NDS (Národná diaľničná spoločnosť)** — autostrade live + counts: `https://ndsas.sk/`
- **Pan-European E-Road Census** (UN ECE / Eurostat) — Slovakia participant since 1980; conducted every 5 years (years ending in 0, 5)

### Key terms

- **TGM (Priemerná denná intenzita dopravy)** — Average Daily Traffic — same as Czech TGM
- Road categories: D (diaľnice), R (rýchlostné cesty), I/II/III triedy (state roads), miestne komunikácie

### Verdict bands

- 🟢 < 1,000 v/d (rural III. triedy, miestna komunikácia)
- 🟡 1,000–5,000 v/d (II. triedy, peripheral urban)
- 🟠 5,000–20,000 v/d (busy II/I. triedy, urban arterial)
- 🔴 > 20,000 v/d (D, R, urban core, major I. triedy)

### Bratislava extreme

- Bypass section between Gagarinova–Galvaniho intersections: **>100,000 vehicles/day** (per SSC Celoštátne sčítanie dopravy 2022-2023, listed above — among the busiest counted segments in SK)
- Bratislava ring D1/D2: 50,000–80,000 v/d typical
- City centre: heavy congestion at peak hours

### CSD 2022-2023 highlights

- +14 % vs 2015 across all road types
- D-network growth most pronounced
- Heavy vehicles +16 %, cars +13 %

---

## Section: `--tax`

### Annual property tax — Daň z nehnuteľností

**Set by each obec via VZN (Všeobecne záväzné nariadenie)** — extreme variation between obce.

Three components:

#### 1. Daň z pozemkov (land tax)

```
Daň = (hodnota pozemku za 1 m² × výmera pozemku v m²) × ročná sadzba
```

- Hodnota pozemku za m² stanovená vo VZN obce (or by znalecký posudok if applicable)
- Sadzba zvyčajne 0.25 % – 1.5 % (varies hugely by obec)

#### 2. Daň zo stavieb (building tax)

```
Daň = ročná sadzba/m² × výmera zastavanej plochy/m²
```

- Sadzby per m² per VZN obce (typical):
  - Stavby na bývanie (rodinný dom): **0.10 – 1.00 €/m²/rok**
  - Stavby na poľnohospodársku produkciu: 0.05 – 0.20 €/m²/rok
  - Záhradné chaty / chaty na rekreáciu: 0.30 – 2.00 €/m²/rok
  - Garáže: 0.50 – 3.00 €/m²/rok
  - Priemyselné stavby: 1.00 – 7.00 €/m²/rok
  - Bratislava (premium MČ): higher end of ranges

#### 3. Daň z bytov a nebytových priestorov

```
Daň = ročná sadzba/m² × výmera bytu/m²
```

- Sadzba zvyčajne 0.20 – 1.50 €/m²/rok
- Bratislava centrum: vyššie

### Example (Bratislava 100 m² byt at typical 0.50 €/m²/rok)

- 100 × 0.50 = **50 €/rok** (very low)

### Example (small obec 150 m² rodinný dom + 600 m² pozemok)

- Stavba: 150 × 0.20 = 30 €/rok
- Pozemok (e.g., 5 €/m² hodnota × 0.25 % sadzba): 600 × 5 × 0.0025 = 7.50 €/rok
- **Total: ~37 €/rok**

→ **Daň z nehnuteľností in Slovakia is among the lowest in Europe** — typically €30–€300/year for residential.

### Transaction taxes (one-time at purchase)

- **Nadobúdacia daň: ABOLISHED 2005** — buyer pays no transfer tax
- Buyer pays:
  - **Notár / advokát**: typically 0.5–1.5 % of price
  - **Kataster registration fee**: €66 (urgent: €266)
  - **Znalecký posudok** (appraisal, often required by bank): €100–€300
- Seller may pay **daň z príjmu na kapitálový zisk** (§ 8 ZDP) at **19 % / 25 %** brackets if sold within **5 years** of acquisition; exempt after 5 years. **Primary residence exempt** if (a) trvalý pobyt ≥ 2 years immediately before sale, AND (b) not used for business in the 5 years prior, AND (c) never registered as obchodný majetok (§ 9 ods. 1 ZDP). (2026-05-27 verified, source PwC SK + Accace 2025)
- **Realitný maklér**: usually 3–5 % paid by seller

### Total transaction cost

- **Buyer side: ~1–2 % of price** (similar to CZ; far cheaper than IT/DE/UK)

### DPH (VAT) on new builds

**MAJOR 2025 reform** (konsolidačný balíček; effective 1 Jan 2025, source Zákon 222/2004 § amend + Grant Thornton SK + financnasprava.sk, 2026-05-27 verified):
- **23 %** standard rate (up from 20 %)
- **19 %** reduced — NEW from 2025, replaces old 10 % bracket (food non-basic, electricity, restaurant non-alcoholic beverages)
- **5 %** super-reduced applies to **accommodation services (ubytovanie)**, restaurant food services, fitness centres, sports events, books — NEW from 2025; plus basic foodstuffs, medicines, medical devices, and pre-existing state-supported social housing (Zákon 222/2004 Z. z. §85). **Not** a new first-time-buyer bracket.
- Old rules: 20 % standard, no special accommodation rate

### Future risk

- VZN changes by obec are common (annual review possible)
- **Konsolidačný balíček 2025** raised DPH significantly; further increases discussed
- Re-introduction of nadobúdacia daň occasionally proposed (currently rejected)

---

## Section: `--rental`

### Long-term residential

**Daň z príjmu z prenájmu (FO)**:
- Income from prenájom is "iný príjem" (other income) under § 6 ods. 3 ZDP
- **Paušálne výdavky 60 %** allowed (max €20,000/yr)
- Tax brackets 2025 (pre 1 Jan 2026 progressivity reform; source ZDP § 15 + financnasprava.sk + podnikajte.sk, 2026-05-27 verified):
  - **15 %** (mikrodaňovník) for príjem ≤ €100,000/yr
  - **19 %** standard up to **€48,441.43** ZD (176.8× životné minimum, raised from €60,000 EUR in 2024)
  - **25 %** above €48,441.43
  - Future: **30 % + 35 % progressivity brackets** added from 1 Jan 2026 per konsolidačný balíček (verify final thresholds at financnasprava.sk)
- Reportable annually (DAP fyzickej osoby)
- No social/health insurance contributions (unless registered as živnostník)

### Short-term rentals (krátkodobý prenájom / Airbnb / Booking)

**Status**: rapidly tightening 2025-2026.

#### EU Regulation 2024/1028 → SK national law

- Mandatory short-term rental **register** being created (per EU mandate)
- Public register fields: address, unit type, # of beds, registration number
- Penalties: **€100–€1,500 per FO violation** plus larger brackets for businesses and platforms (per MCRŠ návrh)
- **EU base reg 2024/1028: applies 20 May 2026** across EU for data-sharing infrastructure
- **SK transposition timeline** (per MCRŠ návrh, pending NR SR final reading at 2026-05-27): existing hosts active on online platforms by **31 Dec 2026** must register by **28 Feb 2027**; from **1 March 2027** registration is a precondition for offering STR via online platforms (verify final text in Zbierka zákonov)

#### Hostinská činnosť živnosť

Short-term rental WITH ancillary services (cleaning, breakfast, key handover, etc.) → **živnostenské oprávnenie** required.
- Without proper živnosť, fine up to **€1,659**
- Most professional Airbnb operations qualify as živnosť

#### DPH thresholds 2025

- **€50,000** revenue/yr → register as DPH platiteľ (kicks in next year)
- **€62,500** revenue/yr → immediate DPH platiteľ status
- DPH rate for ubytovanie: **5 %** (reduced rate for accommodation services from 2025 — significant change)

#### Daň za ubytovanie (accommodation tax)

- Local tax set by obec
- Bratislava: ~€1.70–€3.00/night (varies by MČ)
- Other tourist destinations: €0.50–€2.00/night
- Collected from guest, paid to obec quarterly

#### Bratislava-specific

- Pressure for caps similar to Praha (60 days/yr proposed)
- Some MČ stricter than others
- New register from 2026 will enable enforcement

### Strategic notes

- **Bratislava + Vysoké Tatry + spa towns (Piešťany, Bardejov)**: highest yields but biggest regulatory pressure
- **Eastern Slovakia (Košice + okolie)**: lower yields, less regulation
- **High Tatras** seasonal — winter ski + summer hiking; year-round demand
- **eTuristic-like register from 2026** — register early
- **5 % DPH for accommodation from 2025** — significant tax win for accommodation operators

---

## Section: `--work=<profession>`

### Job platforms

- **Profesia.sk** — largest SK job board: `https://www.profesia.sk/`
- **Kariera.sk**
- **Indeed.sk**, **LinkedIn SK** (active in IT, finance, automotive)
- **Slovenský úrad práce**: `https://www.upsvr.gov.sk/` — official labor office

### Self-employment regimes

- **SZČO (samostatne zárobkovo činná osoba)**: standard self-employed (similar to CZ OSVČ)
- **Paušálne výdavky 60 %** (same as for prenájom; limit €20,000/yr)
- Mandatory **sociálne poistenie** + **zdravotné poistenie**:
  - Min. odvody 2025: ~€216/mo zdravotné + ~€217/mo sociálne (after first year)
  - First year exempt from sociálne (as new SZČO)
- **Voľná živnosť** (free trade): no qualifications, register at Živnostenský úrad
- **Viazaná / koncesovaná živnosť**: requires education / experience / license

### Salaried benchmarks (2025)

- Median monthly gross:
  - Bratislava: ~€1,800
  - Košice / Žilina: ~€1,400
  - Smaller towns: ~€1,100–€1,300
- **Minimálna mzda 2025**: €816/mo gross (≈ €188/wk; NV SR / financnasprava.sk)
- 13. + 14. plat traditions vary by employer

### Catchment heuristics

- Within 30 min of okresné mesto: decent catchment
- Within 60 min of kraj capital: full salaried opportunity
- Eastern Slovakia (Prešov, Košice areas): lower wages but lower cost of living
- High Tatras + Liptov + Orava: thin labor markets, tourism-driven

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **SVP MPO/MPR** (Mapy povodňového ohrozenia + rizika) | `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/` | Q10/Q100/Q1000 flood hazard + risk maps for all SK rivers |
| **SVP MP-T portál** | `https://mpt.svp.sk/svp_vmapportal/` | Map portal supplementary |
| **SHMÚ Hydro stupne aktivity** | `https://www.shmu.sk/sk/?page=1&id=hydro_stpa` | Real-time flood activity stages 1-3 |
| **Minzp.sk povodňové mapy** | `https://www.minzp.sk/voda/ochrana-pred-povodnami/manazment-povodnovych-rizik/povodnove-mapy.html` | Ministry environment flood policy + maps |
| **ŠGÚDŠ Geofyzikálne mapy radon** | `https://apl.geology.sk/radio/` | Radon natural radioactivity maps 1:50k–1:500k |
| **ŠGÚDŠ map portal** | `https://www.geology.sk/maps-and-data/mapovy-portal/geophysical-maps/maps-of-natural-radioactivity/?lang=en` | Direct access to scaled radon maps |
| **Geoportal.gov.sk radon** | `https://geoportal.gov.sk/articles/radonove-riziko` | Aggregated radon risk |
| **GFÚ SAV (Geofyzikálny ústav SAV) seizmicita** | `https://www.seismology.sk/Maps/` | Seismic hazard map (475-yr return period PGA) |
| **Ústav vied o Zemi SAV** | `https://geo.sav.sk/` | Earthquake research + recent activity |
| **Geoportal KSK povodne** | `https://www.geoportalksk.sk/home/povodnove-ohrozenie-uzemia-ksk/` | Košický kraj specific |

### Flood zones (záplavové územia)

SVP publishes maps for 3 probability levels:
- **Q10**: high probability (every 10 yrs) — frequent flooding, major restrictions
- **Q100**: medium probability (every 100 yrs) — insurance / building restrictions
- **Q1000**: low probability (every 1,000 yrs) — extreme event reference

Verify parcel-level via SVP's flood-hazard and flood-risk maps (MPO/MPR, scale **1:10,000**, prepared under Directive 2007/60/EC) — `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/`. **The page has no municipality or parcel search; open the linked *Mapový portál* and locate the parcel on the map** (2026-09-18 verified).

### Radon zones (radónové riziko)

ŠGÚDŠ classifies into:
- **Nízke** (low) — most of lowland Slovakia
- **Stredné** (medium) — transitional zones
- **Vysoké** (high) — primary problem areas:
  - **Strážovské vrchy** (Trenčiansky kraj)
  - **Považský Inovec** (Trenčín / Nitra)
  - **Malá Fatra** (Žilinský kraj)
  - **Spišsko-gemerské rudohorie** parts (Košický + Prešovský kraje)
  - **Hornádska kotlina** (Spiš region)
  - **Veporské vrchy** (granite belt central SK)

**Slovakia has elevated radon overall** (similar pattern to CZ), but slightly less severe than CZ on average. Granite-substrate areas always require **measurement** before purchase.

**Mitigation cost**: €1,500–€7,000 — VMC, sealing, sub-floor ventilation

### Seismicity

Slovakia is **more seismically active than CZ** — five recognized active zones:

| Zone | Notable events |
|---|---|
| **Dobrá Voda (Malé Karpaty, north)** | Ongoing microseismicity |
| **Komárno** | **1763 M 6.5** — historical major; 1783 aftershocks |
| **Žilina** | **1858 M 5.7** — recent reminder |
| **Stredné Slovensko (B. Bystrica)** | Ongoing low-level |
| **Východné Slovensko (Vihorlat / Humenné / Vranov / Michalovce)** | Recent Zemplín 2023 quake |

For most properties: 🟡 LOW–MEDIUM (zone-dependent). For Komárno + Vihorlat areas: 🟠 MEDIUM concern; for the rest: 🟢 negligible.

Map: `https://www.seismology.sk/Maps/` (475-year return period PGA map, 2012 GFÚ SAV).

### Build-era hazards

| Era | Hazards |
|---|---|
| **< 1948** | Lead, asbestos in roofing, weak foundations |
| **1948–1989 panelové domy** | Asbestos in joints + insulation, low-quality concrete (similar to CZ panelák problem) |
| **1948–1989 cihlové domy** | Better quality but asbestos + lead pipes likely |
| **1990–2000 "kvalitná privátna výstavba"** | DIY craftsmanship variability; possible no-permit work |
| **2000–2008** | Building boom — uneven quality |
| **Post-2008** | Modern energy + fire standards |
| **Post-2013 nZEB** | Energy efficiency standards tightening |

**Asbestos**: pre-1995 likely; obligatory remediation if friabile; cost €30–€80/m² roof.

### Mandatory diagnostics at sale

| Document | Required because | Penalty |
|---|---|---|
| **Energetický certifikát budovy (EC)** | All sales (with limited exceptions) | Up to **€2,000** |
| **List vlastníctva aktuálny** | All sales (verify owner + ťarchy) | Free via katasterportal |
| **Snímok z katastrálnej mapy** | All sales | Free via ZBGIS |
| **Geometrický plán** | If parcela split / new build | Per-case |
| **Znalecký posudok** | Often required by bank for mortgage | €100–€300 |
| **Potvrdenie SVB o nedoplatkoch** | If apartment in SVB | At signing |
| **PPV (potvrdenie o platených úhradách)** | If apartment | At signing |

**EC platnosť**: 10 years.
**EC obligation at sale / lease since 2013** under Zákon 555/2005 Z. z. § 7, § 8 (not 1 April 2025 — that date is the new Stavebný zákon 201/2022 effective date; see below). Pokuta **€500–€3,000** under § 12. (2026-05-27 verified, source SIEA)

**Stavebný zákon transition (1 April 2025)**: Zákon 50/1976 Zb. zrušený; replaced by **Zákon 201/2022 Z. z. o výstavbe** and **Zákon 200/2022 Z. z. o územnom plánovaní** (effective 1 April 2025). Late-2024 bridge novela Zákon 46/2024. Source: Úrad pre územné plánovanie a výstavbu SR `https://uupv.sk/`.

### Climate change projections (SHMÚ)

- +1.5–3.0 °C by 2050 vs 1981–2010 baseline (RCP scenario)
- More droughts (esp. Žitný ostrov, lowland SK)
- Vysoké Tatry snow → less reliable lower altitudes
- Heat waves: longer + more intense
- Extreme rain events: more frequent
- Wildfires: rising in Tatras + East SK forests

---

## Section: `--mains`

### Major water operators (regional)

| Operator | Coverage |
|---|---|
| **BVS (Bratislavská vodárenská spoločnosť)** | Bratislavský kraj |
| **TAVOS (Trnavská vodárenská spoločnosť)** | Trnava + okolie |
| **ZsVS (Západoslovenská vodárenská spoločnosť)** | Nitriansky kraj parts: Dunajská Streda, Galanta, Šaľa, Levice, Nové Zámky, Nitra, Zlaté Moravce, Topoľčany, Bánovce nad Bebravou, Partizánske |
| **StVS / StVPS (Stredoslovenská vodárenská spoločnosť / prevádzková)** | Banskobystrický kraj |
| **SEVAK (Severoslovenské vodárne a kanalizácie)** | Žilinský kraj |
| **VVS (Východoslovenská vodárenská spoločnosť)** | Košický + Prešovský kraje (>2,000 employees) |
| Smaller obecné/mestské | Some smaller obce on local water utilities |

### Verification

- ZsVS-style coverage portal: `https://www.zsvs.sk/sluzby/zivotna-situacia/pripojenie-na-verejny-vodovod-a-kanalizaciu`
- Or directly via obec website
- **Most populated obce > 1,000 obyv have mains**; **vesnice < 500 obyv often lack mains sewer**
- Listing language:
  - "verejný vodovod" / "obecný vodovod" = mains water
  - "verejná kanalizácia" / "obecná kanalizácia" = mains sewer
  - "studňa" = own well (groundwater)
  - "žumpa" = cesspit / vault (no treatment)
  - "domová ČOV" = domestic wastewater treatment
  - "septik" = septic tank

### Costs

| Scenario | Cost |
|---|---:|
| Connection where available | €1,000–€3,000 |
| Mains drains construction (per parcel) if obec has trunk line | €2,000–€8,000 |
| Septik to mains conversion | €4,000–€10,000 |
| Domová ČOV (modern compliant) install | €4,000–€10,000 |
| Žumpa replacement | €2,000–€6,000 |
| Vŕtaná studňa (well) | €3,000–€8,000 |

---

## Cost benchmarks (SK 2026)

| Work | Cost (€) |
|---|---:|
| Energetický certifikát (rodinný dom) | €150–€350 |
| Energetický certifikát (bytový dom) | €300–€800 |
| Notár / advokát | 0.5–1.5 % of price |
| Cadastre registration fee (Kataster) | €66 (urgent €266) |
| Znalecký posudok | €100–€300 |
| **Daň z nehnuteľností (annual, residential)** | €30–€300 typical |
| Septik to mains | €4,000–€10,000 |
| Roof (terracotta tile, 200 m²) | €8,000–€18,000 |
| Asbestos removal (200 m² roof) | €4,000–€12,000 |
| Energy retrofit (Class C → A) | €25,000–€80,000 |
| Radon retrofit (VMC + sealing) | €1,500–€7,000 |
| Building inspection (independent) | €300–€800 |
| **Total transaction cost (buyer side)** | **~1–2 %** of price |

## Active fiscal incentives (2025)

- **Zelená domácnostiam** — solar PV, heat pumps, wind, biomass: up to 60 % subsidy (renewed 2024-2030)
- **Plyn-out** kotlíkové dotácie — replace gas boilers
- **Obnov dom** — comprehensive home retrofit grants (up to €19,000 on RH)
- **Refundácia DPH** — for first-time buyers (limited, conditions apply)
- **5 % DPH** for accommodation services (FROM 2025) — major win for short-let
- **Obnova budov programu** Plán obnovy a odolnosti — €630M over 2024-2026

## Common listing platforms

- **Nehnutelnosti.sk** — full extraction, largest market share
- **Reality.sk** — standard
- **Topreality.sk** — standard
- **Bazoš.sk** — privates, lowest commission (no agency)
- **Zoznam Realit, Realtbilliard** — secondary
- **Bondreality, M&M, RE/MAX SK, Lexxus** — agency networks
- **Realitymap.sk + Realitný barometer** — for benchmarking, not listings

## Caveats unique to SK

- **No nadobúdacia daň since 2005** — buyer-side costs very low (~1–2 %); the cheapest-to-buy of the V4 + Western European countries
- **Daň z nehnuteľností very low** — typically €30–€300/yr (similar to CZ but EUR-denominated)
- **DPH reform 2025**: standard rate 20 % → 23 %, reduced rates 19 % and 5 % (2025 data, source Finančná správa); the 5 % rate on supply of buildings is a RETAINED pre-2025 rate limited to projects of state-supported rental housing (štátom podporované nájomné bývanie) — it is not a general housing rate, so verify the DPH applicable to a new-build purchase with the developer / Finančná správa
- **No NOZ-style major civil reform** — older Občiansky zákonník still applies; some "predkupné právo" surprises possible
- **Bratislava market is 1.5–2.5× the rest of SK** — extreme price gradient
- **Eastern Slovakia (Prešovský/Košický)** — much cheaper but lower liquidity + higher emigration
- **Tatry chaty** — special restrictions (TANAP National Park rules)
- **Energetický certifikát mandatory at sale**, penalty up to €2,000 — easier than CZ's 100k CZK penalty
- **Bratislava + Komárno + Žilina seismicity** — higher than CZ; verify zone before buying older buildings
- **Hungarian-speaking south Slovakia** — listings often in Hungarian on local platforms
- **Panelové domy 1948–1989**: same hazards as CZ — asbestos in joints, low-quality concrete

## Reddit / forum sources

- **r/Slovakia** (English-friendly), **r/Bratislava**
- Slovak: **/r/Slovensko** equivalent forums
- **Refresher.sk**, **Profesia.sk komunita**
- Facebook: "Bývanie na Slovensku", "Reality bez realitky SK"
- **InYourPocket Bratislava, Slovakia.travel** — expat info
- **Spectator.sme.sk** — English-language SK news incl. property

## Verification authorities

| Authority | When to call |
|---|---|
| **Kataster** (Okresný úrad — odbor katastrálny) | LV verification, parcela verification, vlastník/ťarchy |
| **Obec / mesto / mestská časť** | Územný plán, daň z nehnuteľností (sadzby per VZN), kolaudácia |
| **Notár / advokát** | Final compravendita, escrow, ťarchy check |
| **Provozovateľ vodovodu** (regional water co.) | Mains drains verification |
| **Okresný úrad — odbor životného prostredia** | Záplavové územia, povolenia |
| **SHMÚ** | Hydrology + meteorology |
| **ŠGÚDŠ** | Geological / radon information |
| **GFÚ SAV** | Seismic information |
| **SVB** (apartment owners' assoc.) | Bezdlžnosť, fond opráv stav |
| **Bytové družstvo** (if cooperative) | Different ownership rules |

## Quirks to know

- **Parcela registra "C" vs "E"**: registra C = current state, registra E = original (pre-collectivization). Some properties only on E — may need Registračné konanie to harmonize
- **CICA viewing free + informative**; eSKN = legally binding (paid via slovensko.sk)
- **Predkupné právo**: pre-emption rights common in inherited / cooperative properties — verify before signing
- **Susedské vzťahy** (neighbour rights / disputes) — CZ-similar legal framework
- **Vyznámenie zákazu zaťaženia** (encumbrance freeze) on LV = red flag
- **Ťarcha B**: building / restriction; **ťarcha C**: ownership-related encumbrance — both must be verified
- **Geodet vs notár roles**: geodet creates GP (geometric plan), notár handles transfer — both needed for parcela split
- **Land vs building**: still legally separable in some pre-1990 properties (unlike post-NOZ CZ)
- **Žitný ostrov** groundwater protection zone — restrictions on industrial use
- **TANAP / NAPANT / Slovenský raj** national parks — strict construction limits

## Source URL templates

| Source | URL pattern |
|---|---|
| ÚGKK CICA (informative LV) | `https://kataster.vugk.sk` |
| ÚGKK eSKN (electronic LV, login) | `https://kataster.skgeodesy.sk/eskn-portal/` |
| ÚGKK ZBGIS map | `https://zbgis.skgeodesy.sk/mapka/sk/kataster` |
| Katasterportal (free download) | `https://www.katasterportal.com/` |
| Nehnutelnosti search | `https://www.nehnutelnosti.sk/<region>/<okres>/<obec>/` |
| Reality.sk | `https://www.reality.sk/byty-na-predaj/<region>/<obec>/` |
| Realitný barometer | `https://www.realitnaunia.sk/realitny-barometer` |
| NBS prices by region | `https://nbs.sk/en/statistics/selected-macroeconomics-indicators/residential-property-prices/residential-property-prices-by-regions/` |
| SSC sčítanie dopravy | `https://www.ssc.sk/sk/cinnosti/rozvoj-cestnej-siete/dopravne-inzinierstvo/celostatne-scitanie-dopravy-v-roku-2022-a-2023.ssc` |
| SVP povodňové mapy | `https://www.svp.sk/sk/uvodna-stranka/povodne/mpo-a-mpr-sr/` |
| SHMÚ povodne aktivita | `https://www.shmu.sk/sk/?page=1&id=hydro_stpa` |
| ŠGÚDŠ radon mapy | `https://apl.geology.sk/radio/` |
| Geoportal radon | `https://geoportal.gov.sk/articles/radonove-riziko` |
| GFÚ SAV seismika | `https://www.seismology.sk/Maps/` |
| Slovensko.sk daň pozemkov | `https://www.slovensko.sk/sk/zivotne-situacie/zivotna-situacia/_dan-z-pozemkov/` |
| Finančná správa SR | `https://www.financnasprava.sk/` |
| ZsVS (water W. SK) | `https://www.zsvs.sk/` |
| BVS (water Bratislava) | `https://www.bvsas.sk/` |
| VVS (water E. SK) | `https://www.vodarne.eu/` |

## Leaving Slovakia — origin-country deregistration entry points

For SK-resident buyers moving abroad. **Doorway only** — see [`shared/cross-border.md`](../../shared/cross-border.md) for the framework + [`shared/home-tax.md`](../../shared/home-tax.md) for tax detail. Mandatory call-out: engage cross-border tax counsel in BOTH jurisdictions before moving the centre of vital interests.

| Register | Action | Authority | URL |
|---|---|---|---|
| Tax residence | Final-year daňové priznanie with foreign address per [Zákon 595/2003 Z. z.](https://www.slov-lex.sk/) o dani z príjmov § 2 písm. d); verify DTA tie-breaker if dual residence claimed by destination | Finančná správa SR | [financnasprava.sk](https://www.financnasprava.sk/) |
| Civil register (trvalý pobyt) | **Odhlásenie z trvalého pobytu** via municipal *ohlasovňa pobytu* per [Zákon 253/1998 Z. z. § 6](https://www.slov-lex.sk/) — required if no longer resident in SR | Obecný / mestský úrad | [minv.sk — ohlasovne pobytu](https://portal.minv.sk/wps/wcm/connect/sk/site/main/zivotne-situacie/Cudzinci/Hlasenie-pobytu-cudzincov) |
| Health insurance | Terminate verejné zdravotné poistenie per [Zákon 580/2004 Z. z.](https://www.slov-lex.sk/) — VšZP / Dôvera / Union; **Union and Dôvera are merging: the purchase agreement was signed 14 Jul 2026 and takes effect once the required institutional approvals are obtained, with Union's insureds transferring automatically to Dôvera from 1 January 2027 unless they file a change-of-insurer application by 30 September** (2026-09-18 verified); if EU/EEA/CH destination, S1 form bridges coverage | All-payor framework (**two payors from 1 Jan 2027 if the merger completes**) | [vszp.sk](https://www.vszp.sk/) · [dovera.sk](https://www.dovera.sk/) · [union.sk](https://www.union.sk/) |
| Social security | Sociálna poisťovňa coordination via S1 if EU/EEA/CH destination per [Reg 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883); bilateral totalisation outside coordination zone | Sociálna poisťovňa | [socpoist.sk](https://www.socpoist.sk/) |
| **s.r.o. owner-manager** | If owner-manager moving abroad — **POEM / PE risk** under destination DTA Art. 4(3) + Art. 5; effective-management migration can make the s.r.o. treaty-resident in destination → destination corporate tax + SK exit-tax event. Engage **corporate-tax counsel BEFORE move**. | Slovenská komora daňových poradcov + destination tax counsel | [skdp.sk](https://www.skdp.sk/) |
| Slovakia-treaty register (DTA lookup) | Find the relevant SK-destination ZZDP + tie-breaker article + MLI matches | Ministerstvo financií SR — Zmluvy o zamedzení dvojitého zdanenia | [mfsr.sk — ZZDP](https://www.mfsr.sk/sk/dane-cla-uctovnictvo/priame-dane/dane-z-prijmu/zmluvy-zamedzeni-dvojiteho-zdanenia/zmluvy-zamedzeni-dvojiteho-zdanenia/) |

**Cross-link**: invoke `--cross-border` for the framework (DTA tie-breaker pointer + POEM/PE check + EU/EEA/CH free-movement clarification per [AFMP](https://www.fedlex.admin.ch/eli/cc/2002/243/en) / [EEA](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:21994A0103(01)) / [Dir 2004/38/EC](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004L0038)) and `--home-tax` for Slovakia-side detail.

## Status

✅ **Fully populated** as of 2026-04-25 (health-insurance payor row corrected 2026-09-18 — the Union / Dôvera merger is conditional on approvals and has not completed; the Zákon 580/2004 and S1 limbs were not re-verified). Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + cadastre + risk sources (all primary state agencies, multi-source corroborated). MEDIUM for short-let regulation (in transition: EU 2024/1028 SK transposition + 5 % DPH adjustment 2025 + Bratislava-specific rules pending).

## Extension TODOs (deepen on first real run)

- [ ] Per-obec daň z nehnuteľností sadzby from VZN (need scraping per ~2,890 obec — start with top 50 mestá)
- [ ] CSD2022-2023 ArcGIS Hub data extraction workflow
- [ ] EU 2024/1028 SK national register walkthrough once portal launches
- [ ] Bratislava MČ Airbnb / krátkodobý prenájom rules per MČ
- [ ] Asbestos detection workflow for panelové domy (1948-1989)
- [ ] Predkupné právo + susedské vzťahy detection from LV
- [ ] Žitný ostrov + národné parky construction limits
- [ ] Hungarian-language listings (south Slovakia) — bilingual extraction
