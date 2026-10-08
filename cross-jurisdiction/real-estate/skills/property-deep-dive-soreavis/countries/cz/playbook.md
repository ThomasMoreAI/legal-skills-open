# Czech Republic 🇨🇿 — Property Due-Diligence Playbook

ISO2: `cz`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **PSČ (postcode)**: 5 digits in `NNN NN` format (e.g., `110 00`, `602 00`)
  - First 3 digits: regional cluster
  - Last 2: local (no `0` after space typically)
- **Admin levels**: 14 kraje → 76 okresy → 6,254 obce (municipalities) → katastrální území
- **Currency**: CZK (Czech koruna). 1 EUR ≈ 24–25 CZK (variable)
- **Languages**: Czech (official); German/Polish/Slovak minority pockets
- **Cadastre**: **ČÚZK** (Český úřad zeměměřický a katastrální) — public viewer **FREE since 2014**
- **Identifier**: parcela číslo + katastrální území + obec (LV = list vlastnictví = title deed)
- **Major reform 2014**: New Civil Code (NOZ) merged building + land parcel; old separate registers consolidated.
- **CRITICAL 2020 change**: nabývací daň (transfer tax for buyers) **ABOLISHED** September 2020.

## Section: `--price`

### Primary sources

- **ČÚZK Nahlížení do KN** (FREE, official):
  - Portal: `https://nahlizenidokn.cuzk.gov.cz/`
  - Search by parcela / building / unit / address (fixed CAPTCHA for owner reveal without login)
  - Returns: short LV with vlastník, výměra, list vlastnictví číslo, zatížení (encumbrances)
  - Login via Identita občana for full LV
- **ČÚZK Dálkový přístup pro neregistrované**: `https://dpn.cuzk.gov.cz/`
- **Sister** (paid pro tier): `https://cuzk.gov.cz/aplikace-dp` — full extracts, planimetry

### Price benchmarks (Q4 2025 reference)

- **ČSÚ Indexy realizovaných cen bytů** (quarterly): `https://csu.gov.cz/produkty/indexy-realizovanych-cen-bytu-4-ctvrtleti-2025`
- **ČSÚ Indexy cen nemovitostí**: `https://csu.gov.cz/produkty/icn_cr`
- **ČNB residential property price data**: `https://www.cnb.cz/cs/financni-stabilita/`
- 2025 trend: Praha bytů +13.4 % YoY, mimo Prahu +16.6 % YoY (Q3 2025)

### Listing platforms

- **Sreality.cz** — largest, includes **Cenová mapa** (atlas of sold prices): `https://www.sreality.cz/cenova-mapa`
  - URL: `https://www.sreality.cz/hledani/prodej/byty/<region>` or `/<okres>` or `/<obec>`
  - Filters: cena, dispozice (1+kk to 6+1), výměra, lokalita
- **Bezrealitky.cz** — privates, no agency fees: `https://www.bezrealitky.cz/`
- **Reality.idnes.cz**, **Realityix**, **ULOV.realit**
- **REMAX, M&M, Sting** — agency networks

### Average €/m² benchmarks (Q4 2025)

| Region | Realized €/m² (avg byty) |
|---|---:|
| Praha (město) | ~115,500 CZK ≈ €4,700 |
| Brno-město | ~126,000 CZK ≈ €5,140 |
| Jihomoravský kraj (mimo Brno) | ~81,200 CZK ≈ €3,310 |
| Ostrava + Moravskoslezský | ~50,000–70,000 CZK ≈ €2,000–€2,860 |
| Ústecký, Karlovarský | ~30,000–50,000 CZK ≈ €1,225–€2,040 |
| Vysočina, Pardubický, Zlínský | ~50,000–80,000 CZK ≈ €2,040–€3,265 |
| Středočeský (mimo Praha) | ~70,000–100,000 CZK ≈ €2,860–€4,080 |

### Compute

1. Listing price/m² = listing CZK / m² (clarify: užitná plocha = Carrez-equivalent, vs zastavěná plocha for taxes)
2. Compare to ČSÚ realized price for the kraj
3. Compare to Sreality cenová mapa (more granular, by city district)
4. **Trap**: byty in Praha priced in CZK or EUR — clarify which currency on listing
5. **Trap**: některé novostavby exclude DPH (advertise net price); check if "cena bez DPH" or "vč. DPH"

---

## Section: `--traffic`

### Primary source

- **ŘSD Sčítání dopravy** (Ředitelství silnic a dálnic):
  - Portal: `https://scitani.rsd.cz/`
  - Most recent: **CSD2020** (data collected 07/2020–06/2021), published 2022
  - Coverage: 6,465 sčítací úseky (D + I + II + III třída)
  - Display: `https://scitani.rsd.cz/CSD_2020/pages/informations/default.aspx`
- **CDV — Centrum dopravního výzkumu**: `https://cdv.gov.cz/` (methodology + supplementary research)
- **Silniční databanka ŘSD + NDIC**: `https://www.rsd.cz/rsd/silnicni-databanka-a-ndic`

### Key term

**TGM (Roční průměrná denní intenzita dopravy)** — Average Daily Traffic over the year, similar to AADT.

### Verdict bands

- 🟢 < 1,000 v/d (rural III. třída)
- 🟡 1,000–5,000 v/d (small II. třída, urban side street)
- 🟠 5,000–20,000 v/d (busy II. třída, urban arterial, smaller I. třída)
- 🔴 > 20,000 v/d (D/dálnice, major I. třída, urban core)

### Coarse fallback

OSM `highway` class:
- motorway/trunk = D + R + I. třída major
- primary = I. třída
- secondary = II. třída
- tertiary = III. třída
- residential = obytná zóna

### CSD2020 highlights

- Total traffic +10 % vs CSD2010
- D-network +15 %, I+II+III +9 %
- Heavy vehicles +16 %, cars +9 %

---

## Section: `--tax`

### Annual property tax — Daň z nemovitých věcí

**Major 2024 reform** (Konsolidační balíček) increased rates ~1.8× from 2024.
**Major 2025 reform**: zrušení koeficientu 1.5; new local koeficient range 0.5–5.0.

**Formula**:
```
Daň = Plocha (m²) × Základní sazba × Základní koeficient × Místní koeficient × Inflační koeficient
```

| Item | Sazba 2025 |
|---|---|
| Obytné domy (rodinný dům, byt) | **2 Kč/m² zastavěné plochy** |
| Stavby pro rodinnou rekreaci | 6 Kč/m² |
| Garáže | 8 Kč/m² |
| Stavby pro podnikání | 10 Kč/m² |
| Pozemky (orná půda, zahrada, vinice, sad, chmelnice) | **1.35 % z ceny pozemku** (2025; raised from 0.75 % by konsolidační balíček Act 349/2023 Sb. effective 1 Jan 2024) |
| Trvalé travní porosty + lesy + rybníky s intenzivním chovem ryb | **0.45 % z ceny pozemku** (2025; raised from 0.25 % since 1 Jan 2024) |
| **Stavební pozemek** | 3.50 Kč/m² |
| **Inflační koeficient 2025** | **1.0** |

**Základní koeficient** by population:
- Obec ≤ 1,000 obyv: **1.0**
- 1,001–6,000: **1.4**
- 6,001–10,000: **1.6**
- 10,001–25,000: **2.0**
- 25,001–50,000: **2.5**
- > 50,000 + statutární města: **3.5**
- Praha: **4.5**

**Místní koeficient** (set by obec): 0.5–5.0; can apply only-up for stavby/stavební pozemky since 2025.

### Example calculation

A 100 m² rodinný dům in Praha:
- 100 × 2 Kč × 4.5 (Praha basic) × 1.0 (no local mult) × 1.0 (inflation) = **900 CZK/rok** (~€37/yr)

A 200 m² rodinný dům in obci 5,000 obyv:
- 200 × 2 Kč × 1.4 × 1.0 × 1.0 = **560 CZK/rok** (~€23/yr)

**Daň z nemovitých věcí is therefore very low compared to W. Europe** — typically €20–€200/yr for residential.

### Transaction taxes (one-time at purchase)

- **Daň z nabytí nemovitých věcí (transfer tax)**: **ABOLISHED 26 September 2020** by law 386/2020.
- **Buyer pays**: only notary/lawyer fees + cadastre registration fee (1,000 CZK) + survey
- **Seller pays**: daň z příjmů on capital gain (15 % / 23 %) if sold within **5 years** (acquisitions before 1 Jan 2021) or **10 years** (acquisitions from 1 Jan 2021 onwards — § 4 odst. 1 ZDP); primary-residence exemption after 2 yrs registered trvalé bydliště, or reinvestment-of-proceeds exemption (§ 4 odst. 1 písm. v ZDP) — verify with daňový poradce given strict 1-year reinvest-notification rule (2026-05-27 verified, source: Finanční správa; zákonyprolidi.cz Lei 586/1992 ZDP)

**Notary / advokát**: 0.5–1.5 % typical, negotiable
**Realitní makléř**: usually 3–5 % paid by seller
**Total transaction cost** (buyer side): ~1–2 % of price (vs ~10–13 % in IT)

### Future risk

- Increases discussed politically (multiple parties want to raise to W-Europe levels)
- Re-introduction of nabývací daň proposed periodically (currently rejected)

---

## Section: `--rental`

### Long-term residential

**Daň z příjmů z pronájmu (FO)** — § 9 Zákona o daních z příjmů:
- Two cost methods (must be uniform across all rentals):
  - **Skutečné výdaje** (actual expenses)
  - **Paušální výdaje 30 %** (max 600,000 CZK ceiling, i.e., max revenue 2 mil. CZK)
- Sazba 2025: **15 %** up to ZD 1,676,052 CZK; **23 %** above
- Reportable on daňové přiznání (DAP) annually
- No social/health insurance contributions (unlike OSVČ)
- Taxes paid by 1 April year +1

### Short-term rentals (krátkodobé ubytování / Airbnb / Booking)

**Status**: in transition. Rules tightening sharply 2025-2026.

#### Current obligations (2025)

- **Hostinská činnost živnost** required if >30 days/year revenue threshold met (debated; many treat all Airbnb as živnost)
- **DPH (VAT)**: 21 % if revenue > 2 mil. CZK/12 months — most professional Airbnb hits this
- **Daň z ubytování** (local accommodation tax): 21 CZK/night Praha, varies elsewhere; 50 CZK ceiling
- **Hlášení hostů na cizinecké policii** within 3 working days
- **eTurista** (national register): launches **1 July 2025** — replaces ad-hoc municipal registers

#### EU Regulation 2024/1028

- Mandatory short-term rental registration across EU
- Full application from **20 May 2026**
- Member states preparing IT systems 2024–2026

#### Praha-specific (most restrictive)

- Praha 1 referendum 2024 backed regulation
- City wants:
  - **Max 60 days/year** per byt for short-let
  - **SVJ (homeowners' association) approval** required
  - **Possibly ban** in worst-affected zones
- Currently legal limbo — pending parlamentární approval
- Some Pražské městské části: stricter local rules

#### Tax regime for Airbnb

- **If hostinská činnost (živnost)**: standard OSVČ regime — paušál 60 %, sociální + zdravotní pojištění + daň
- **If just nájem (under §9)**: but Praha and tax authority increasingly classify professional Airbnb as "podnikatelská činnost" → re-classified as živnost retroactively
- **Paušální daň for OSVČ 2025**: 7,498 CZK/měsíc all-in for I. pásmo (revenue ≤ 1 mil/yr)

### Strategic notes

- **Praha + Český Krumlov + Karlovy Vary + Brno + spa towns**: highest yields but biggest regulatory risk
- **South Bohemia, Šumava, Krkonoše**: tourist demand, less regulation
- **Wholly-rural / vesnice**: limited demand outside ski resorts
- **eTurista from 1 Jul 2025** — register early to avoid penalties
- **EU regulation 2026** — platforms must verify; unregistered listings will be removed

---

## Section: `--work=<profession>`

### Job platforms

- **Jobs.cz**, **Práce.cz**, **Profesia.cz**, **StartupJobs.cz**
- **LinkedIn CZ** (very active in IT, finance, big-corp)
- **Ústav práce ČR**: `https://www.uradprace.cz/` — official labor office
- **Hyperinzerce, Annonce** — older classifieds

### Self-employment regimes

- **OSVČ (osoba samostatně výdělečně činná)**: standard self-employed
  - Paušální výdaje 40 / 60 / 80 % depending on činnost
  - Sociální pojištění + zdravotní pojištění mandatory
- **Paušální daň** (2025):
  - I. pásmo (revenue < 1 mil): 7,498 CZK/měsíc all-in
  - II. pásmo (1–1.5 mil): 16,745 CZK/měsíc
  - III. pásmo (1.5–2 mil): 27,139 CZK/měsíc
- **Volná živnost** (free trade): no qualifications, register at Živnostenský úřad
- **Vázaná / koncesovaná živnost**: requires education / experience / license

### Salaried benchmarks

- Median monthly gross 2025 (CZK):
  - Praha: ~50,000
  - Velká města: ~40,000
  - Regiony: ~32,000–38,000
- **Minimální mzda 2025**: 20,800 CZK/měsíc

### Catchment heuristics

- Within 30 min of okresní město: decent catchment
- Within 60 min of kraj capital: full salaried opportunity
- Mountainous border regions (Šumava, Krušné hory, Jeseníky): thin labor markets, English-speaking expats common in tourism

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Záplavová území** (national flood map) | `https://voda.gov.cz/?page=zaplavova-uzemi-mapa` | Q5/Q20/Q100 flood zones |
| **Digitální povodňový plán ČR** | `https://webmap.dppcr.cz/dpp_cr/dppcr.dll?MU=001` | Flood plans, hlásné profily |
| **ČHMÚ Hlásná a předpovědní povodňová služba** | `https://hydro.chmi.cz/hppsoldv/` | Real-time hydrology |
| **MŽP povodňové nebezpečí Q100** | `https://cds.mzp.cz/mapy/?MAP=mpn_100` | Hazard zones |
| **ČAP (Česká asociace pojišťoven) povodňové mapy** | `https://www.cap.cz/povodnove-mapy` | Insurance-grade flood zones (1-4) |
| **EDPP.cz online povodňová mapa** | `https://www.edpp.cz/online-povodnova-mapa-cr/` | Aggregated commercial map |
| **ČGS Svahové nestability (landslides)** | `https://mapy.geology.cz/svahove_nestability/` | Landslide registry + susceptibility |
| **ČGS Geofond sesuvy** | `https://mapy.geology.cz/arcgis/rest/services/Geohazardy/sesuvy_Geofond/MapServer` | API access |
| **ČGS / SÚRO Radon mapa** | `http://www.geology.cz/demo/CD_RADON50/index/info.htm` + `https://www.suro.cz/cz/prirodnioz/radonove-mapy` | Radon index 1-3 of geological substrate |
| **GeoVědy radonová mapa** | `http://www.geologicke-mapy.cz/radon/` | Detailed online radon map |
| **Geofyzikální ústav AV ČR seismicita** | `https://www.ig.cas.cz/observatorie/ceska-regionalni-seismicka-sit/` | Earthquake monitoring |
| **SeismickaMapa.cz** | `https://seismickamapa.cz/` | Aggregated hazard map |
| **WEBNET West Bohemia swarms** | `https://www.ig.cas.cz/observatorie/lokalni-seismicka-sit-webnet/` | West-Bohemia microseism |

### Flood zones (záplavová zóna 1-4)

| Zóna | Riziko | Notes |
|---|---|---|
| **1** | Zanedbatelné | No restriction; insurance unaffected |
| **2** | Nízké | Possible insurance surcharge |
| **3** | Střední | Insurance can be expensive; new build restrictions |
| **4** | Vysoké | Often uninsurable; very limited new build allowed |

Source for parcel-level: ČAP map at `https://www.cap.cz/povodnove-mapy` (insurance-aligned).

### Radon zones (radonový index podloží)

- **Nízký** (low) — most of CZ
- **Přechodný** (transitional)
- **Vysoký** (high) — Vysočina, Krušné hory podhůří, Jižní Čechy granite belt, Krkonoše + Jizerské hory podhůří, Jeseníky
- **CZ is among the highest-radon countries in Europe** (est., reflecting the granite-substrate geology of the high-index zones above — verify radon-index data at suro.cz)
- New buildings since 1991: mandatory radon protective measures
- Older buildings (pre-1991): retrofit recommended in vysoký radon areas

**Mitigation cost**: est. 50,000–200,000 CZK (~€2,000–€8,000) (2026 contractor ranges — verify with quotes) — VMC, sealing, sub-floor ventilation

### Seismicity

- **Very low overall** — most of CZ in zone 1 (faible) per ČSN EN 1998-1
- **Active microseismic zones**:
  - **Western Bohemia / Vogtland** — Kraslicko, Nový Kostel: M 4.8 record (2008), regular swarms
  - **Hronovsko-poříčský zlom** (Královéhradecký kraj) — moderate
  - **Jeseníky** — minor
- For most properties, seismicity is **🟢 negligible**

### Build-era hazards

| Era | Hazards |
|---|---|
| **< 1948** (předválečné, válečné) | Lead, asbestos in roofing, weak foundations |
| **1948–1989 panelové domy** | Asbestos in joints + insulation, low-quality concrete (PVS issue), aging utility lines |
| **1948–1989 cihlové domy** | Better quality but asbestos + lead pipes likely |
| **1990–2000 "kvalitní privátní"** | DIY craftsmanship variability; possible no permit work |
| **2000–2008** | Building boom — uneven quality |
| **Post-2008** | Modern energy + fire standards (Vyhláška 268/2009) |
| **Post-2014 NOZ** | New civil code; older "anomalous" titles harmonized |

**Asbestos**: pre-1995 likely; obligatory removal if friabile; est. cost 1,500–4,000 CZK/m² roof (2026 ranges — verify with abatement quotes).

### Mandatory diagnostics at sale

| Document | Required because | Validity / penalty |
|---|---|---|
| **PENB (Průkaz energetické náročnosti budovy)** | All sales (with limited exceptions) | 10 yrs validity; **penalty 100k CZK FO / 200k CZK PO** if missing |
| **List vlastnictví aktuální** | All sales (verify owner + zatížení) | Free via Nahlížení |
| **Snímek z katastrální mapy** | All sales | Free via Nahlížení |
| **Bezdlužnost SVJ** | If apartment in SVJ | At signing |
| **Geometrický plán** | If parcel split / new build | Per-case |
| **BPEJ** (bonita půdy) | Agricultural land sales | Per-case |
| **Souhlas věřitele/banky** | If pre-existing zástava | At signing |

**PENB exceptions**:
- Chaty, chalupy < 4 měsíců používání
- Energy use < 25 % of typical
- Recreational evidence in cadastre
- Pre-1947 historical buildings unchanged
- Buildings < 50 m²

**From 2027**: PENB mandatory even for new rental contracts (currently only sales).

### Climate change projections (ČHMÚ)

- +1.5–3.0 °C by 2050 vs 1981–2010 baseline (depending on RCP)
- More droughts (esp. Southern Moravia)
- Warmer winters → less snow → ski-resort impact (Krkonoše, Jeseníky, Šumava lower altitudes)
- Heat waves: longer + more intense
- Extreme rain events: increasing frequency
- Wildfires: rising in Šumava, South Moravia, North Bohemia forests

---

## Section: `--mains`

### National database

- **SOVAK ČR** (Sdružení oboru vodovodů a kanalizací): `https://www.sovak.cz/`
- Statistical data per provider; not parcel-level

### Major operators

| Operator | Coverage |
|---|---|
| **PVK (Pražské vodovody a kanalizace)** | Praha (Veolia subsidiary; assets owned by hl. m. Prahy via PVS) |
| **SčVK (Severočeské vodovody a kanalizace)** | Ústecký + Liberecký kraj + Roztoky |
| **Středočeské vodárny** (Veolia) | Středočeský kraj parts |
| **Královéhradecká provozní** (Veolia) | Královéhradecký kraj |
| **Moravská vodárenská** (Veolia) | parts of Moravia |
| **VaK Brno**, **VaK Olomouc**, **VaK Ostrava** | regional/municipal |
| **Vodárna Plzeň**, **VaK Mladá Boleslav** | regional |
| Many obecní/místní | Smaller obce, often public ownership |

Veolia ČR group = largest operator (est. ~50% of total connections, based on the operator coverage list above — verify with SOVAK ČR operator statistics).

### Verification

1. Check **obec website** under "Životní prostředí > Vodovody a kanalizace"
2. Listing language:
   - "kanalizace" / "obecní kanalizace" = mains drains
   - "septik" / "domovní ČOV" / "žumpa" = individual / cesspit
   - "vodovod ano / kanalizace ne" = mains water but no mains sewer
3. **Most populated obce > 500 obyv have mains**; **vesnice < 200 obyv often lack mains sewer**

### Costs

*est. 2026 contractor ranges — verify with quotes.*

| Scenario | Cost |
|---|---:|
| Connection where available | est. 30,000–80,000 CZK |
| Mains drains construction (per parcel) if obec has trunk line | est. 50,000–150,000 CZK |
| Septik to mains conversion | est. 80,000–200,000 CZK |
| Domovní ČOV (modern compliant) install | est. 100,000–250,000 CZK |
| Žumpa replacement | est. 60,000–150,000 CZK |

---

## Cost benchmarks (CZ 2026)

| Work | Cost (CZK) |
|---|---:|
| PENB (rodinný dům) | 2,500–5,000 |
| PENB (bytový dům) | 5,000–15,000 |
| Notary / advokát | 0.5–1.5 % of price |
| Cadastre registration fee | 1,000 |
| **Daň z nemovitých věcí (annual, residential)** | 500–5,000 typical |
| Septik to mains | 80,000–200,000 |
| Roof (terracotta tile, 200 m²) | 250,000–500,000 |
| Asbestos removal (200 m² roof) | 200,000–500,000 |
| Energy retrofit (Class C → A) | 800,000–2,500,000 |
| Radon retrofit (VMC + sealing) | 50,000–200,000 |
| Building inspection (independent) | 8,000–25,000 |
| **Total transaction cost (buyer side)** | ~1–2 % of price |

## Active fiscal incentives (2025)

- **Nová zelená úsporám** (NZÚ) — energy retrofit grants for households (up to 50 % of eligible costs)
- **Kotlíkové dotace** — replace old solid-fuel boilers (až 95 % for low-income)
- **NZÚ Light** — quick small-scale subsidies for low-income
- **Fotovoltaika dotace** — solar PV
- **Heat pump grants** — incl. NZÚ + obec subsidies
- **Bezúročná půjčka modernizační fond** — for some retrofit packages
- **Sleva na dani 15 %** for certified retrofit projects (new from 2025)

## Common listing platforms

- **Sreality.cz** — full extraction, includes cenová mapa
- **Bezrealitky.cz** — privates, no agency
- **Reality.idnes.cz**, **ULOV.realit**, **Realityix**
- **REMAX, M&M, Sting, Century 21** — agency networks
- **Hyperinzerce, Annonce** — older classifieds, sometimes hidden gems

## Caveats unique to CZ

- **Nabývací daň abolished 2020** — buyer-side costs are very low (~1–2 %) compared to W. Europe (10–13 %)
- **Daň z nemovitých věcí 1.8× from 2024** + new local koeficient 0.5–5.0 from 2025 — bills changing significantly
- **Among the highest-radon countries in Europe** (est. — verify radon-index data at suro.cz) — test before buying granite-substrate areas
- **Krátkodobé ubytování (Airbnb) heavily restricted in Praha**; eTurista national register from 1 July 2025; EU reg 2024/1028 from 20 May 2026
- **Panelové domy** (1948–1989 socialistická panelová výstavba): variable quality; asbestos in joints common; check rekonstrukce status
- **NOZ 2014 reform** merged building+land registers; pre-2014 properties may have legal complexity
- **eTurista mandatory** for short-let from 1 July 2025
- **PENB mandatory at sale**, penalty up to 100k CZK
- **PIT capital gain 15 % / 23 %** if sold within **5 yrs** (pre-2021 acquisitions) or **10 yrs** (from 1 Jan 2021 onwards) — primary residence exempt after 2 yrs occupancy, or reinvestment-of-proceeds exemption (§ 4 odst. 1 písm. v ZDP) (2026-05-27 verified)
- **VAT 21 % on novostavby**; **12 % reduced rate** (since 1 Jan 2024 — konsolidační balíček 349/2023 Sb. merged former 10 % + 15 % reduced rates into a single 12 %) for sociální bydlení = family house ≤ 350 m² podlahové plochy / apartment ≤ 120 m² podlahové plochy (2026-05-27 verified, source: Finanční správa; § 48 zákona č. 235/2004 Sb. o DPH ve znění zák. 349/2023 Sb.)
- **Polození bytového domu** (basement / shelter requirements) — varies by obec
- **Foreign-buyer parity (since 1 May 2011)**: Czechia imposes **no nationality-based restrictions** on residential, commercial, or agricultural property purchase — EU, EEA, and non-EU citizens have equal rights as natural persons. Same ČÚZK katastr filing; no special permit, no surcharge, no pre-approval. Large-scale agricultural transactions may trigger SPÚ notification (not nationality-based); strategic-asset purchases (kritická infrastruktura) fall under FDI-screening zákon č. 34/2021 Sb. (2026-05-27 verified, source: Dostupný advokát; Finanční správa).
- **Skrytá vada — § 2129 občanského zákoníku (zákon 89/2012 Sb.)**: buyer of a building with permanent foundations must notify the seller of a hidden defect (skrytá vada present at transfer, manifested later) within **5 years** of acquisition or the court will not grant rights from defective performance if the seller objects (§ 2129 odst. 1). The 5-yr lhůta does NOT apply if the seller knew or should have known of the defect (§ 2129 odst. 2). For **consumer buyers (B2C)**, **§ 2161 OZ** establishes a **2-year presumption** that any defect manifesting within 2 years of risk transfer was present at transfer (rebuttable by nature of defect / opotřebení / stáří) (2026-05-27 verified, source: zákonyprolidi.cz 2012-89; dTest).
- **Beneficial-ownership registration (zákon č. 37/2021 Sb., succeeding the repealed 38/2020)**: if buying via Czech s.r.o. or other právnická osoba, **evidence skutečných majitelů** registration is **mandatory** at the rejstříkový soud — penalty up to **CZK 500,000** for non-registration. The advokátní tarif (vyhláška č. 177/1996 Sb.) governs the legal-services fee schedule (2026-05-27 verified, source: zákonyprolidi.cz 2021-37; esm.justice.cz).

## Reddit / forum sources

- **r/czech**, **r/Praha** (Czech-language, mixed)
- **r/PraguePeople**, **r/CzechRepublic**
- **Bezrealitky blog** (forum-style discussions)
- **Realityix blog**, **CenovaMapa.cz** community
- Expat: **InYourPocket Prague**, **Expats.cz** forums
- Facebook: "Bydlení v Praze", "Reality bez realitky"

## Verification authorities

| Authority | When to call |
|---|---|
| **ČÚZK / Katastrální úřad** | LV verification, parcela verification, vlastník/zatížení |
| **Obecní úřad / Stavební úřad** | Permit history (kolaudace), abuse check, územní plán |
| **Notář / advokát** | Final compravendita, smluvní jistota, escrow |
| **Provozovatel VaK** (operator) | Mains drains verification |
| **Krajský úřad — odbor životního prostředí** | Záplavová zóna confirmation |
| **Katastrální pracoviště** | Walk-in for full LV with all encumbrances |
| **SVJ** (apartment owners' assoc.) | Bezdlužnost, fond oprav stav, poplatky |
| **Bytové družstvo** (if cooperative) | Different ownership rules — check carefully |

## Quirks to know

- **Parcela vs jednotka**: bytová jednotka has separate LV from the building's parcela; verify both
- **Lhůta na nahlížení**: free LV view is shortened (no historical owners or pohledávky); for full info → Czech Point or paid extract
- **eTurista vs živnost vs nájem**: same activity might fall under 3 different regimes depending on professionalism — get expert advice
- **Praha 1**: extreme regulation pressure on Airbnb; pending change
- **BPEJ kód** for agricultural land — affects valuation + dotace
- **Plomba katastru**: red flag if "P" letter on LV — pending change
- **Územní plán** must allow intended use — verify at obec before any non-residential plans
- **Stavební uzávěra** rare but devastating — verify obec doesn't have one for the lokalita
- **2014 NOZ harmonization** — pre-2014 properties may still have separated building+land titles → unification recommended

## Source URL templates

| Source | URL pattern |
|---|---|
| ČÚZK Nahlížení | `https://nahlizenidokn.cuzk.gov.cz/` |
| ČÚZK DPN (unregistered) | `https://dpn.cuzk.gov.cz/` |
| ČÚZK Sister (paid) | `https://cuzk.gov.cz/aplikace-dp` |
| Sreality search | `https://www.sreality.cz/hledani/prodej/byty/<region>/<obec>` |
| Sreality cenová mapa | `https://www.sreality.cz/cenova-mapa<region>/<obec>` |
| Bezrealitky | `https://www.bezrealitky.cz/<region>/<obec>` |
| ČSÚ ceny bytů | `https://csu.gov.cz/produkty/indexy-realizovanych-cen-bytu-<X>-ctvrtleti-<year>` |
| ŘSD sčítání dopravy | `https://scitani.rsd.cz/CSD_2020/pages/informations/default.aspx` |
| Záplavová území | `https://voda.gov.cz/?page=zaplavova-uzemi-mapa` |
| ČHMÚ HPPS | `https://hydro.chmi.cz/hppsoldv/` |
| ČAP povodňové mapy | `https://www.cap.cz/povodnove-mapy` |
| ČGS svahové nestability | `https://mapy.geology.cz/svahove_nestability/` |
| ČGS radon | `http://www.geology.cz/demo/CD_RADON50/index/info.htm` |
| GeoVědy radonová mapa | `http://www.geologicke-mapy.cz/radon/` |
| SÚRO radonové mapy | `https://www.suro.cz/cz/prirodnioz/radonove-mapy` |
| Geofyzikální ústav seismika | `https://www.ig.cas.cz/observatorie/ceska-regionalni-seismicka-sit/` |
| eTurista (from 2025) | `https://eturista.gov.cz/` |
| Finanční správa daň z nemovitostí | `https://financnisprava.gov.cz/cs/dane/dane/dan-z-nemovitych-veci` |
| SOVAK (water operators) | `https://www.sovak.cz/` |
| MMR ČR (housing policy) | `https://mmr.gov.cz/` |
| MŽP (environment) | `https://mzp.gov.cz/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (all primary state agencies, multi-source corroborated). MEDIUM for short-let regulation (in transition: eTurista launch July 2025 + EU regulation May 2026 + Praha-specific rules pending).

## Extension TODOs (deepen on first real run)

- [ ] Per-kraj traffic data extraction (CSD2020 has regional sub-pages)
- [ ] Per-obec daň z nemovitých věcí místní koeficient (need scraping per ~6,254 obec — start with top 100)
- [ ] eTurista registration walkthrough once portal is live
- [ ] Praha městské části short-let rules (each MČ has own approach)
- [ ] BPEJ codes for agricultural land valuation
- [ ] Bytové družstvo vs SVJ distinction tooling
- [ ] Asbestos detection workflow for panelové domy (1948-1989)
