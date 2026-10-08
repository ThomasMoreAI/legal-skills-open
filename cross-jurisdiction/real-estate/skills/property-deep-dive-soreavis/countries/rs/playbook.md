# Serbia 🇷🇸 — Property Due-Diligence Playbook

ISO2: `rs`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`11000` Belgrade, `21000` Novi Sad, `18000` Niš, `34000` Kragujevac)
- **Admin levels**: 3 statistical regions + 25 districts + 145 municipalities + Belgrade (capital, special status) + Vojvodina autonomous province + Kosovo (disputed)
- **Currency**: **RSD** (Serbian dinar); 1 EUR ≈ 117 RSD (managed float)
- **Languages**: Serbian (official); Hungarian (Vojvodina), Albanian, Bosnian, Romanian, Croatian (regional minorities)
- **Cadastre**:
  - **RGZ (Republički Geodetski Zavod)**: `https://www.rgz.gov.rs/`
  - **eKatastar public portal**: `https://katastar.rgz.gov.rs/eKatastarPublic/PublicAccess.aspx`
- **Identifier**: parcela + KO (cadastral municipality)
- **Ownership types**: pravo svojine (full ownership); etažna svojina (condominium for apartments); pravo zakupa (lease)
- **EU candidate** since 2012 (negotiations ongoing)

## Section: `--price`

### Primary sources

- **NBS (National Bank of Serbia)**: `https://www.nbs.rs/en/indeks/index.html` — real estate price index
- **RZS (Republički Zavod za Statistiku)**: `https://www.stat.gov.rs/`
- **FRED QRSN628BIS** for Serbia residential property
- **Investropa, Global Property Guide** — secondary aggregators

### Listing platforms

- **HaloOglasi** — DOMINANT: `https://www.halooglasi.com/`
- **Nekretnine.rs**: `https://www.nekretnine.rs/`
- **4zida.rs**, **Sasomange**: alternatives
- **BeoBuild** for Belgrade specialist

### 2025-2026 price benchmarks (NBS + Investropa Q3-Q4 2025)

| Region | EUR/m² (avg) | YoY |
|---|---:|---:|
| **Belgrade Vračar** | 3,359 (range 1,887–7,212) | +6% |
| **Belgrade Stari Grad** | 3,669 (range 1,500–6,154) | +6% |
| **Belgrade Novi Beograd** | 2,500–3,500 | +5-7% |
| **Belgrade waterfront premium** | 4,000–8,000+ | +8-12% |
| **Novi Sad** | 1,800–2,400 | +5-6% |
| **Niš** | 900–1,400 | +3-5% |
| **Kragujevac** | 700–1,100 | +3-5% |
| **National YoY** | — | **+5.78% Q2 2025 / +6% Sept 2025** |

**NBS price index** real: 117.798 (2010=100) Sept 2025

### Compute

1. EUR/m² = price / **korisna površina** (usable area)
2. **Currency**: residential typically transacted in RSD or EUR-equivalent; commercial often EUR-denominated
3. **Belgrade Waterfront** ongoing development — premium tier
4. Cross-check **NBS index** + **HaloOglasi** asking prices

### Key terms

- Pravo svojine = ownership right
- Etažna svojina = condominium (apartment)
- KO = katastarska opština (cadastral municipality)
- Energetski pasoš = energy passport
- List nepokretnosti = property sheet (cadastre extract)

---

## Section: `--traffic`

### Sources

- **JP Putevi Srbije**: `https://www.putevi-srbije.rs/`
- **Sekretarijat za saobraćaj Belgrade**: city traffic data

### Key term

**PGDS (Prosečan godišnji dnevni saobraćaj)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban side streets)
- 🟠 10,000–35,000 v/d (Belgrade arterials, državne ceste)
- 🔴 > 35,000 v/d (autoput E70/E75, Belgrade ring, Boulevard Vojvode Stepe)

---

## Section: `--tax`

### Annual property tax — Porez na imovinu (2025 rates — verify current local-self-government tariff)

**Local self-government (progressive)**:

| Property value | Rate (max) |
|---|---:|
| Up to RSD 10M (~€85k) | **0.4%** |
| RSD 10–25M | **0.6%** |
| RSD 25–50M | **0.8%** |
| > RSD 50M | **2.0%** |

- **Threshold**: RSD 400,000 (no tax below)
- **50% reduction** for owner-occupied (max RSD 20,000 reduction)
- **Quarterly payment**: Feb/May/Aug/Nov 15

### Transaction taxes

- **Porez na prenos apsolutnih prava** (transfer): **2.5%** on resale. **Seller is statutorily liable**; contracts routinely shift to buyer — read the ugovor carefully *(2026-05-27 verified, source PwC Tax Summaries + CMS)*
- **First-apartment exemption** (transfer tax): adult RS citizen with permanent residence, first apartment ≤40 m² → exempt from 2.5 % transfer tax; +15 m² per qualifying family member who hasn't owned since 1 July 2006. Above the cap, tax due on excess area only.
- **PDV (VAT)**: **20%** standard; **10% on first-sale residential** (replaces transfer tax). Refund mechanism: first-time buyer up to 40 m² + 15 m² per family member who hasn't owned since 1 July 2006.
- **Notary fees**: ~0.5–1.0% of price
- **Cadastre registration**: ~0.3%

### Personal income tax (PIT) framework

- **Employment income**: 10% flat (after monthly non-taxable cap RSD 34,221 for 2025).
- **Annual PIT top-up (synthetic on global net)**: **10% up to RSD 9,749,016** (~6× average annual salary); **15% above** that threshold. Filing threshold 2025 net: RSD 5,439,096.
- **Other categories** flat 10–20% (royalties 20%, capital gains 15%, rental 20% gross or 15% effective after 25% normative deduction). Young taxpayers <40 receive an extra allowance of RSD 5,439,096. *(2026-05-27 verified, source KPMG RS Annual PIT alert Feb 2026 + PwC Tax Summaries)*

### Capital gains

- **15% PIT** on real-estate appreciation (long-standing rate per Zakon o porezu na dohodak građana — Sl. glasnik RS; no 2024 rate change verified)
- **Exempt after 10-year holding** (CRITICAL)
- **Also exempt**: sale of primary residence; reinvestment of proceeds in housing within 90 days; inheritance, spousal transfer, first-line blood-relative transfer, divorce *(2026-05-27 verified, source PwC Tax Summaries + taxadvisorserbia)*

### Total transaction cost (buyer side)

- Resale: ~3-4% (2.5% transfer + 0.5-1% notary + 0.3% cadastre)
- New build: 10% VAT included + ~2-3% other costs

### Future risk

- EU candidate accession reforms continuing
- NBS key rate 5.75% since Oct 2024 (held)
- Belgrade Waterfront ongoing

---

## Section: `--rental`

### Long-term residential

- **Zakon o stanovanju i održavanju zgrada**
- Tenant protection moderate
- Standard 1-3 yr contracts

### Short-let (Airbnb)

- **Tourist tax (boravišna taksa)**: ~RSD 159/person/night Belgrade (~€1.30); 50% reduction ages 7-15
- **License**: registration with municipal authority required; display reg number on listings
- **Belgrade tightening 2024-2025**

### Tax on rental

- Resident: **effective 15% on gross rental** after the 25% normative-cost deduction (20% × 75% = 15%)
- Non-resident: 20% withholding

---

## Section: `--work=<profession>`

### Sources

- **NSZ (Nacionalna služba za zapošljavanje)**: `https://www.nsz.gov.rs/`
- **Poslovi.infostud.com**, **HelloWorld.rs**, **LinkedIn RS**

### Self-employment

- **Preduzetnik** (sole trader)
- **DOO** (limited): min RSD 100 capital
- **Paušalna obaveza** (flat rate) for small business
- **PDV** registration: from RSD 8M turnover

### Salary benchmarks (2025)

- Median monthly gross:
  - Belgrade: ~RSD 110,000–180,000 (~€940–€1,540)
  - Novi Sad: ~RSD 95,000–150,000
  - Smaller cities: ~RSD 70,000–110,000
- **Minimalna zarada**: RSD 47,154/month gross (2025) ~€403

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Seizmološki zavod Srbije** | `https://www.seismo.gov.rs/` | Seismic monitoring |
| **RHMZ (Republički Hidrometeorološki Zavod)** | `https://www.hidmet.gov.rs/` | Weather, hydrology, floods |
| **Ministarstvo unutrašnjih poslova** | — | Civil protection |

### Specific risks

#### Earthquake — moderate

- **2010 Kraljevo M5.5** (est. €100M+ damage, est. 16k structures damaged — verify with Seizmološki zavod / RHMZ)
- **1922 Lazarevac M6.0**, **1927 Rudnik M5.9**, **1980 Kopaonik M5.8**, **1998 Mionica M5.7**
- Belgrade MM IV during Kraljevo
- **Vlasinsko / Pirot** zone elevated; Belgrade lower

#### Floods

- **2014 catastrophic floods**: Sava + **Bosna** rivers (NOT Drava — common confusion)
- Belgrade outskirts inundated, Savski Nasip embankment held at 6,500 m³/s threshold
- Climate change increasing extreme rainfall

#### Air quality

- **Belgrade records severe winter PM2.5** — verify current ranking with IQAir / EEA
- Coal-heating + diesel cars contributors

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **Yugoslav era 1945-1990** | Asbestos common, panel buildings (paneli) |
| **Post-2008** | Modern codes (post-Skopje + Banja Luka reforms) |
| **Belgrade Waterfront 2014+** | Premium new-build standards |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Energetski pasoš** | Mandatory since 2013 |
| **Notar + ugovor o kupoprodaji** | Mandatory |
| **Geodetski snimak** (survey) | Cadastre |
| **List nepokretnosti** | Title verification |

---

## Section: `--mains`

### Sources

- **JKP Beogradski vodovod i kanalizacija** (Belgrade)
- Per-municipality elsewhere
- Sava + Danube water sources; aging infrastructure

### Costs

| Scenario | Cost (EUR) |
|---|---:|
| Mains connection | 1,500–4,000 |
| Septic upgrade | 2,500–6,000 |
| Bored well | 3,000–8,000 |

---

## Cost benchmarks (RS 2026)

| Work | Cost (EUR) |
|---|---:|
| Energetski pasoš | 100–250 |
| Notar fees | 0.5–1.0% |
| Transfer tax | 2.5% |
| **Total transaction cost (buyer)** | **~3–4%** of price |
| Roof renovation | 4,000–12,000 |
| Energy retrofit | 8,000–25,000 |
| Heat pump | 5,000–10,000 |
| Solar PV (5kW) | 3,500–7,000 |

## Active fiscal incentives (2025-2026)

- **NBS subsidized mortgage program** for first-home buyers
- **EU pre-accession funding** for energy retrofit
- **Vučić government** infrastructure spend continues

## Common listing platforms

- **HaloOglasi** — DOMINANT
- **Nekretnine.rs**, **4zida.rs**, **Sasomange**
- **BeoBuild** Belgrade specialist

## Caveats unique to RS

- **EU candidate since 2012** — accession negotiations ongoing
- **Foreign-buyer reciprocity rules** — non-EU/non-OECD buyers may need Ministry of Justice approval (est. RSD 1,990, ~15 days — verify current fee/timeline with Ministarstvo pravde)
- **Reciprocity reportedly recognised** for US, UK, CA, AU, most EU, Japan, Switzerland — verify the current list with Ministarstvo pravde (see Extension TODO)
- **EUR-denominated commercial** market; residential typically RSD or EUR-equivalent
- **2014 floods** = Sava + Bosna (NOT Drava — common confusion)
- **Capital gains 10-year exemption** — CRITICAL planning point
- **Belgrade Waterfront** controversial mega-project; ongoing
- **Belgrade records elevated winter PM2.5** — verify current ranking with IQAir / EEA
- **NBS key rate 5.75%** since Oct 2024
- **Currency RSD** managed float vs EUR
- **Vojvodina autonomous province** has separate provincial regulations
- **Kosovo property** disputed — separate jurisdictional issues
- **Zakon o posebnim uslovima za evidentiranje i upis prava na nepokretnostima** ("Svoj na svome", in force **24 October 2025**) — one-time legalizacija framework for ~2M unpermitted buildings (houses, apartments, commercial, extensions, garages). **MAIN FILING WINDOW IS NOW CLOSED** — it ran **8 December 2025 → 8 February 2026 24.00** (extended past the statutory ~60-day cut-off by government notice of 4 February 2026 after platform overload). Late filing is possible ONLY on proof of an objective impediment and ONLY until **24 October 2026** — later legalizacija can no longer be assumed at purchase. Authority: Agencija za prostorno planiranje i urbanizam RS → certifikat → RGZ priority registration. Cost €100–€1,000 (2025 figure — not re-verified 2026-08; confirm with the Agency). **Post-24-Oct-2025 illegal construction is NOT eligible** — hard enforcement shift. Buyers of older non-cadastre-conform property inherit any failure to file within the window *(2026-08-07 verified, source CT Legal + Lexology + VMT Attorneys + Tasić & Partners + `https://svojnasvome.gov.rs`)*
- **RGZ digital-only filings** since 4 November 2023 — all cadastre applications routed via professional users (attorneys + licensed geodetic organisations); direct walk-in no longer possible *(2026-05-27 verified, source law-firm.rs + RGZ)*

## Reddit / forum sources

- **r/serbia**, **r/Belgrade**
- **B92** (Belgrade English news)
- **N1 Serbia**, **Balkan Insight**
- **Forum.krstarica.com**

## Verification authorities

| Authority | When to call |
|---|---|
| **RGZ + eKatastar** | Title verification |
| **Notar** | Mandatory closing |
| **Lokalna samouprava** | Property tax + permits |
| **Poreska uprava** | Tax compliance |
| **Ministarstvo pravde** | Foreign-buyer reciprocity approval |

## Source URL templates

| Source | URL pattern |
|---|---|
| RGZ | `https://www.rgz.gov.rs/` |
| eKatastar | `https://katastar.rgz.gov.rs/eKatastarPublic/PublicAccess.aspx` |
| NBS price index | `https://www.nbs.rs/en/indeks/index.html` |
| RZS | `https://www.stat.gov.rs/` |
| HaloOglasi | `https://www.halooglasi.com/` |
| Seizmološki zavod | `https://www.seismo.gov.rs/` |
| RHMZ | `https://www.hidmet.gov.rs/` |
| Poreska uprava | `https://www.purs.gov.rs/` |

## Status

✅ **Fully populated** as of 2026-04-26. **Last verified**: 2026-08-07 (Svoj na svome legalizacija window re-verified — main filing window closed 8 Feb 2026, late filing only on proof of objective impediment until 24 Oct 2026; balance of the 2026-05-27 verification unchanged).
**Coverage check**: pricing (NBS + RZS + Investropa Q3-Q4 2025), traffic (JP Putevi PGDS), tax (porez na imovinu progressive 0.4-2% + 2.5% transfer + 20% VAT (10% first-sale residential) + 15% CGT 10-year exemption), rental (boravišna taksa + license), work (NSZ + Paušalna), risks (Kraljevo 2010 + 2014 Sava+Bosna floods + Belgrade winter PM2.5), mains (Belgrade vodovod + per-municipality).
**Confidence**: HIGH for tax structure (PwC + Investropa confirm); HIGH for 2014 flood factual correction (Sava+Bosna not Drava); HIGH for 10-year CGT exemption; HIGH for foreign-buyer reciprocity rules; MEDIUM for "Vlasinsko zemljotres" zone naming (could not verify as official feature).

## Extension TODOs

- [ ] Per-municipality property tax rates table
- [ ] Foreign-buyer reciprocity country list (verified)
- [ ] Belgrade Waterfront premium zone
- [ ] CGT 10-year holding clock optimization
- [ ] Energetski pasoš class verification flow
- [ ] Vojvodina autonomous province specific rules
- [ ] Belgrade winter PM2.5 mitigation
- [ ] EU pre-accession funding eligibility
- [ ] CHF/EUR mortgage scandal (post-2015 reforms)
- [ ] Kraljevo 2010 + 2014 flood-affected zones
