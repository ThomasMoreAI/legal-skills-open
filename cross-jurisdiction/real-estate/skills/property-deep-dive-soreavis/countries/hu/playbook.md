# Hungary 🇭🇺 — Property Due-Diligence Playbook

ISO2: `hu`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1011` Budapest I, `1051` Budapest V Belváros, `4024` Debrecen, `6720` Szeged)
- **Admin levels**: 19 megye (counties) + Budapest (capital) + 23 districts in Budapest + 3,176 települések (settlements)
- **Currency**: **HUF** (Hungarian forint); 1 EUR ≈ 380–410 HUF (volatile)
- **Languages**: Hungarian (official); German, Slovak (regional minorities)
- **Cadastre**: **Földhivatal Online** (citizen) + **TAKARNET** (B2B professional)
  - Földhivatal Online: `https://www.foldhivatal.hu/` — citizen access via ügyfélkapu
  - TAKARNET: `https://www.takarnet.hu/` — banks, lawyers, notaries (since 2003)
- **Identifier**: **helyrajzi szám (HRSZ)** — topographical lot number; unique parcel ID
- **Tulajdoni lap** = title deed extract (the document buyers/lawyers always pull)
- **Unified cadastre + legal data since 1971** (egységes ingatlan-nyilvántartási rendszer)
- **Ownership types**: tulajdon (full), közös tulajdon (co-ownership), albérlet (sublet)
- **EU member since 2004**; **HUF currency** (NOT in eurozone)

## Section: `--price`

### Primary sources

- **KSH (Központi Statisztikai Hivatal)**: `https://www.ksh.hu/` — official price index
- **Ingatlan.com aggregated data** widely cited in KSH commentary
- **MNB (Magyar Nemzeti Bank)** Housing Market Report: `https://www.mnb.hu/`
- **Pannonland, Investropa** — secondary aggregators

### Listing platforms

- **Ingatlan.com** — DOMINANT (primary source for benchmarks)
- **Otthonterkep.hu** — significant secondary
- **Otthonajánló**, **Ingatlannet** — niche

### 2025 price benchmarks (KSH Q4 2025 / Nov 2025)

| Region | HUF/m² (resale apt) | EUR-equivalent (~395 HUF/EUR) |
|---|---:|---:|
| **Budapest avg (resale apt)** | 1,490,000 | ~€3,800 |
| **Buda Hills (II, XII, III)** | 1,500,000+ | ~€3,800+ |
| **Other Buda (XI, XXII)** | 1,300,000 | ~€3,300 |
| **Budapest VI (Terézváros)** | 1,200,000–1,500,000 | €3,000–€3,800 |
| **Pest inner districts (V, VI, VII, VIII, IX)** | 1,100,000–1,400,000 | €2,800–€3,500 |
| **Debrecen** | 998,000 (resale) / 1,070,000 (brick) | €2,500–€2,700 |
| **Szeged** | 900,000–950,000 | €2,300–€2,400 |
| **Győr** | 850,000 | €2,150 |
| **Pécs** | 750,000 | €1,900 |
| **National avg** | 539,000 (resale) / 1,261,000 (new) | €1,360 / €3,200 |

### Compute

1. HUF/m² = price / **lakóterület** (residential area)
2. **Convert HUF to EUR** at current FX (HUF volatile)
3. **Cross-check** Ingatlan.com asking prices + KSH transaction data
4. **Buda Hills premium** factor 1.5-2× over outer Pest districts

### Key terms

- HRSZ = helyrajzi szám (topographical lot number)
- Tulajdoni lap = title deed extract
- Társasház = condominium / multi-unit residential
- Kataszter = cadastre
- Energetikai tanúsítvány = energy certificate

---

## Section: `--traffic`

### Sources

- **Magyar Közút (NIF Zrt.)**: `https://kozut.hu/` — state roads
- **Önkormányzati közlekedési adatok**: per local authority
- **BKK** (Budapest transit)

### Key term

**ÁNF (Átlagos napi forgalom)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–30,000 v/d (Budapest arterials, M-roads)
- 🔴 > 30,000 v/d (M0 ring, Üllői út, Hungária körút)

---

## Section: `--tax`

### Annual property taxes — local

#### Építményadó (Building tax)

- **Local — set per municipality**
- Maximum 2025: **~2,950 HUF/m²**
- Budapest XIII district 2024: 2,508 HUF/m²
- Many districts charge **0 for primary residences**

#### Telekadó (Land tax)

- **Local — set per municipality**
- Budapest XIII 2025: **536 HUF/m²** (per local önkormányzati rendelet — verify with Budapest XIII önkormányzat)
- Max 2026: **556 HUF/m²** (statutory max — verify with local önkormányzat)
- Wide variance by district / municipality

#### Typical annual tax bills

| Property | Annual (HUF) | EUR |
|---|---:|---:|
| Budapest XI 80m² primary residence | 0 (exempt) | 0 |
| Budapest XIII 80m² rental (építményadó 2,508) | ~200,640 | ~€510 |
| Budapest 80m² + 250m² plot (XIII building + land) | 200,640 + 134,000 = 334,640 | ~€850 |
| Debrecen 100m² | 80,000–150,000 | €200–€380 |

### Transaction taxes

#### Visszterhes vagyonátruházási illeték (transfer tax)

- **4%** of market value (standard)
- **2%** above HUF 1bn threshold (luxury reduction)
- Capped: HUF **200M per property**
- **First-home reduction**: under-35 buyers get **50% discount** if total value ≤ HUF 15M
- *(2026-05-27 verified, source: NAV illeték / PwC Tax Summary)*

### VAT (ÁFA)

- **27% standard** (highest in EU)
- **Reduced 5% on new homes** (≤150 m² flat / ≤300 m² house) — **extended to end of 2026**, possibly 2030 with permit by end of 2026

### Capital gains (PIT)

- **15%** flat
- **5-year holding exemption** (full exemption after 5 years; sliding scale years 1-5 per NAV SZJA információs füzet — residential schedule): Year 1: 100%; Year 2: 90%; Year 3: 60%; Year 4: 30%; Year 5+: 0% (some secondary sources publish 100/90/70/50/30/0 for non-residential — confirm with NAV booklet per transaction) (2026-05-27 verified, source: NAV / PwC Tax Summary)

### Rental income — private accommodation (STR)

- **Fizetővendéglátó tételes átalányadó** (Szja tv. 57/A. § (4)): **HUF 150,000/habitable room/yr** in Budapest — the only settlement over the 2m guest-night trigger — and **HUF 38,400/room/yr** in every other settlement; raised from 38,400 on 1 Jan 2025, both rates unchanged for tax year 2026. Full conditions + NAV list timing in `--rental` (2026-08-07 verified, source: NAV)

### Total transaction cost (buyer side)

- Standard resale: ~5-6% (4% transfer + 1-2% legal/lawyer)
- First-home (under-35, ≤15M HUF): ~3-4% (2% transfer + others)
- New build: 5% VAT included + ~2% other costs

### Future risk

- VAT 5% reduction extended to 2026 (may extend to 2030)
- Currency volatility (HUF can swing 10-20% vs EUR)

---

## Section: `--rental`

### Long-term residential

- **Lakástörvény** (Housing Act) — moderate tenant protection
- Standard 1-3 yr contracts
- **Bérleti szerződés** must be notarized for >1 year if applicable

### Short-let (Airbnb, Booking)

- **Kataregisztráció** (lump-sum tax category) — STR operators register with NAV
- **Budapest VI District (Terézváros)**: **BAN on STRs from 1 January 2026** (online referendum 2024 → 54% for ban → Supreme Court greenlit Nov 2025) — enforcement live since Jan 2026 (Terézváros + police + NAV inspections; fines up to several million HUF); only hotels, guesthouses, and community accommodations may operate legally
- **Budapest VII District (Erzsébetváros)** — stage 1: building decree **33/2025 (IX.24)** (amends 25/2018 XII.21), in force **25 Sept 2025**, caps NEW commercial accommodation at **10% of a building's residential floor area**, ground-floor only, min room sizes + en-suite bath per room, guesthouses ≥6 rooms; existing registered permits exempt
- **Budapest VII District** — stage 2: decree **46/2025 (XII.10)** sets STR usable days/yr to **ZERO from 1 Jan 2026** unless a **társasház** (condominium) agreement exists (then 365) — units registered by 31 Dec 2025 must file the agreement by 31 Dec 2026 (same zero-day mechanism as District VI, with a condo-consent carve-out)
- **Budapest city-wide STR/NTAK registration moratorium 1 Jan 2025 – 31 Dec 2026** (city-wide, not national) — no new NTAK registration numbers issued; hosts registered by 31 Dec 2024 exempt; **expires 31 Dec 2026, extension uncertain — watch**
- Other Budapest districts (e.g. V) reportedly considering similar moves
- STR stock grew **+80% Budapest 2020-2024**; **>hotel rooms** in city
- **Tax**: kata regime up to HUF 18M revenue (preferential)
- **Fizetővendéglátó tételes átalányadó** (itemised flat-rate tax on private accommodation, Szja tv. 57/A. § (4)) — **HUF 150,000 per habitable room per year** in settlements whose guest-nights exceeded **2 million in the second year before the tax year**; **HUF 38,400/room/yr everywhere else**. **Budapest is the only settlement on that list** (guest-nights above 2m in both 2023 and 2024). Rate rose 38,400 → 150,000 on **1 Jan 2025** (+290.6%) — NOT a 2024 change (NAV's 2024 information booklet still stated a flat HUF 38,400/room nationwide); both rates unchanged for tax year 2026. NAV republishes the qualifying-settlement list **by 31 January each year** — check it before assuming the low rate (2026-08-07 verified, source: NAV information booklet 10 published 2026-02-03 + NAV notice 2025-01-17, `https://nav.gov.hu/ado/szja/A_fizetovendeglatokat_erinto_valtozasok`)
- *Short-let rules re-verified 2026-07-02 (Airbnb Hungary Help Center; Erzsébetváros decrees 33/2025 & 46/2025 via net.jogtar.hu); fizetővendéglátó tételes átalányadó re-verified 2026-08-07 (NAV)*

---

## Section: `--work=<profession>`

### Sources

- **NFSZ (Nemzeti Foglalkoztatási Szolgálat)**: `https://nfsz.munka.hu/`
- **Profession.hu** — biggest: `https://www.profession.hu/`
- **Jobline.hu**, **Karrier.hu**, **LinkedIn HU**

### Self-employment

- **EV (Egyéni vállalkozó)** = sole trader
- **Kft. (Korlátolt felelősségű társaság)** = limited; **min HUF 3M capital**
- **ÁFA** registration (alanyi adómentesség threshold): from **HUF 18M turnover** (raised from HUF 12M on 1 Jan 2025) (2026-05-27 verified, source: NAV / WTS Klient)
- **Kata** preferential regime: 50,000 HUF/month flat tax (up to 18M revenue, only specific occupations since 2022)

### Salary benchmarks (2025)

- Median monthly gross:
  - Budapest: ~HUF 700,000–950,000 (€1,800–€2,400)
  - Debrecen / Győr / Szeged: ~HUF 550,000–750,000
  - Smaller cities: ~HUF 450,000–600,000
- **Minimum wage (minimálbér, 2026)**: **HUF 322,800/month gross** (+11% vs 2025; ~€815 at 396 HUF/EUR); guaranteed minimum wage (garantált bérminimum, skilled/diploma): **HUF 373,200/month gross** (~€944) (2026-05-27 verified, source: Forvis Mazars / RSM Hungary / Leinonen)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **OMSZ (Országos Meteorológiai Szolgálat)** | `https://www.met.hu/` | Weather, climate |
| **OVF (Országos Vízügyi Főigazgatóság)** | `https://www.ovf.hu/` | Water management, **flood maps** |
| **SZTFH Földtani Szolgálat** (successor to MBFSZ / MFGI / ELGI / MÁFI) | `https://sztfh.hu/tevekenysegek/foldtani-tevekenyseg` · maps: `https://map.hugeo.hu` | Geology, geophysics, hydrogeology; GeoBank borehole database (2026 data, source sztfh.hu; 2026-09-18 verified) |
| **VÁTI** | varies | Spatial planning |

### Specific risks

- **Flood** — major risk:
  - **~25% of national territory on floodplain** (per OVF — verify flood maps at ovf.hu)
  - **Tisza + Duna + Tisza-Maros** primary
  - "Icy flood" (early spring) + "green flood" (early summer)
  - **4,200 km of dykes**
  - Tisza 2000 catastrophic flood; Duna 2013 (Budapest)
- **Drought**: Great Plain (Alföld) — rising frequency under climate change
- **Heat waves**: increasing
- **Earthquake**: low-moderate; central HU + Komárom area; not catastrophic
- **Storm**: derecho 2022 (Budapest)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead paint, asbestos cement starts |
| **1900–1990 (Soviet/communist era)** | Asbestos common; dated heating; panel buildings (panelház) |
| **Panelház 1960s–1980s** | ~800k units; energy-inefficient; gradual refurbishment |
| **1990s–2000s** | Improving insulation |
| **Post-2008** | Modern energy code |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energetikai tanúsítvány** (energy certificate) | Mandatory since 2012 | 10 years |
| **Tulajdoni lap** | Title deed extract | Current |
| **Notarial / lawyer-witnessed contract** (ügyvédi ellenjegyzés) | Mandatory | At sale |

### Climate change projections

- **+2.5–4.0°C** by 2100
- **Reduced summer precipitation** (Pannonian basin drying)
- **More frequent heatwaves** in Budapest + Alföld
- **Tisza valley**: increasing flood frequency
- **Continental climate intensification**

---

## Section: `--mains`

### Sources

- **Vízművek** per önkormányzat (e.g., **Fővárosi Vízművek** Budapest, **Debreceni Vízmű**)
- Sewer connection rates: **70-80%** nationally; lower in villages
- Rural: **szippantós (cesspit)** common

### Costs

| Scenario | Cost (HUF) |
|---|---:|
| Mains connection | 800,000–2,500,000 |
| Septic upgrade | 1,500,000–4,000,000 |
| Bored well | 1,500,000–3,500,000 |

---

## Cost benchmarks (HU 2026)

| Work | Cost (HUF) |
|---|---:|
| Energetikai tanúsítvány | 50,000–150,000 |
| Lawyer (ügyvéd) | 0.5–1% of price |
| Visszterhes illeték (transfer tax) | 4% (2% above 1bn) |
| Realtor commission | 3% (~paid by seller) |
| **Total transaction cost (buyer)** | **~5–6%** of price |
| Roof renovation | 3,000,000–8,000,000 |
| Asbestos abatement | 500,000–3,000,000 |
| Energy retrofit (Class E → A) | 8,000,000–20,000,000 |
| Panelház refurbishment | 5,000,000–12,000,000 (per unit) |
| Heat pump | 2,500,000–5,000,000 |
| Solar PV (5kW) | 1,800,000–3,500,000 |

## Active fiscal incentives (2025-2026)

- **Otthon Start Program** (1 Sep 2025): **3% fixed-rate mortgage**, up to HUF 50M, 25-year max term, 10% down minimum, must be **first-time owner + 2 years Hungarian social-security history**
- **CSOK Plusz** (family home benefit): up to HUF 50M loan + non-refundable subsidies
- **5% VAT on new homes** extended to end-2026 (to 2030 with permit by Dec 2026)
- **Rezsicsökkentés** (utility cost cap): below-market gas + electricity — being phased
- Bankmonitor forecasts 15-20% price rise in 2026 driven by Otthon Start

## Common listing platforms

- **Ingatlan.com** — DOMINANT
- **Otthonterkep.hu** — secondary
- **Otthonajánló**, **Ingatlannet** — niche

## Caveats unique to HU

- **Currency: HUF** (volatile vs EUR; can swing 10-20%) — material for non-HUF buyers
- **27% VAT** (highest in EU) — but new homes 5% reduced through 2026 (potentially 2030)
- **Otthon Start Program** (1 Sep 2025) — 3% fixed mortgage causing market distortion; sub-€100k stock affected
- **Terézváros (Budapest VI) STR ban from 1 Jan 2026** — first major Hungarian STR ban
- **Other Budapest districts (e.g. V)** considering similar bans (District VII has already enacted rules — see `--rental`)
- **Földforgalmi törvény** (Land Transfer Act):
  - Non-EU citizens essentially **prohibited** from acquiring agricultural land
  - EU citizens limited to 1 hectare with farmer status (3-year farming history + 5-year self-cultivation pledge)
- **Panelház** (~800k units) energy-inefficient Soviet-era panel buildings
- **Tisza + Duna flood risk** — 25% of national territory on floodplain
- **Capital gains 15% PIT** with 5-year holding exemption (sliding scale years 1-5)
- **First-home reduction**: under-35 + property ≤15M HUF = 50% transfer tax discount
- **Visszterhes illeték cap**: HUF 200M per property
- **Társasház** (condominium) financial health critical
- **Földforgalmi törvény** amendment 24 Dec 2025: broader scope for agricultural land lease structures
- **Otthon Start excludes prior-owner applicants** — strong distortion expected on sub-HUF 50M stock
- **Buda Hills (II, XII)** premium 1.5-2× over outer Pest

## Reddit / forum sources

- **r/hungary** — biggest community
- **r/budapest**
- **r/PersonalFinanceHU** (smaller)
- **Hungarian Conservative**, **Daily News Hungary**, **Hungary Today** (English)
- **Portfolio.hu** (financial)

## Verification authorities

| Authority | When to call |
|---|---|
| **Földhivatal Online** | Cadastre verification |
| **TAKARNET** (via lawyer) | Title verification |
| **NAV (tax authority)** | Transfer tax + PIT |
| **Local önkormányzat** | Építményadó + telekadó rates + permits |
| **Ügyvéd** (lawyer, mandatory for sale) | Closing process |
| **Társasházi képviselő** | If apartment |
| **OVF** | Flood risk |

## Source URL templates

| Source | URL pattern |
|---|---|
| Földhivatal Online | `https://www.foldhivatal.hu/` |
| TAKARNET | `https://www.takarnet.hu/` |
| KSH | `https://www.ksh.hu/` |
| Ingatlan.com | `https://www.ingatlan.com/` |
| MNB | `https://www.mnb.hu/` |
| OMSZ | `https://www.met.hu/` |
| OVF | `https://www.ovf.hu/` |
| SZTFH Földtani Szolgálat (ex-MBFSZ) | `https://sztfh.hu/tevekenysegek/foldtani-tevekenyseg` |
| NAV (tax) | `https://nav.gov.hu/` |
| Magyar Közút (traffic) | `https://kozut.hu/` |

## Status

✅ **Fully populated** as of 2026-04-25 (geological-survey body (SZTFH Foldtani Szolgalat) corrected 2026-09-18 per sztfh.hu).
**Coverage check**: pricing (KSH + Ingatlan.com + MNB), traffic (Magyar Közút), tax (építményadó + telekadó local + 4% transfer + 27% VAT (5% new) + 15% CGT 5-yr exempt + fizetővendéglátó tételes átalányadó), rental (Terézváros STR ban from 1 Jan 2026), work, risks (flood 25% territory + drought + Soviet-era panelház), mains all have primary government sources.
**Confidence**: HIGH for Otthon Start (1 Sep 2025) + Terézváros STR ban (1 Jan 2026 confirmed) + 4% transfer tax + 5% VAT extension to 2026; HIGH for Földforgalmi törvény amendment (24 Dec 2025) — agricultural lease structures broader; MEDIUM for HUF FX volatility forecasts (rapidly changing).

## Extension TODOs

- [ ] Per-district építményadó + telekadó rates table
- [ ] Otthon Start eligibility decision tree (first-time owner + SSN history)
- [ ] CSOK Plusz family home benefit eligibility
- [ ] Panelház refurbishment subsidy availability per district
- [ ] Föld Forgalmi Act non-EU agri-land prohibition flow
- [ ] Tisza + Duna flood zone overlay
- [ ] Társasház financial health rubric
- [ ] HUF FX hedging recommendation for non-HUF buyers
- [ ] Budapest district-by-district STR rules tracker (V, VI banned; others?)
- [ ] Buda Hills vs Pest premium multiplier history
