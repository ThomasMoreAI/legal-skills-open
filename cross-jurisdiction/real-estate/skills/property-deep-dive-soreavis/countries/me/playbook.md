# Montenegro 🇲🇪 — Property Due-Diligence Playbook

ISO2: `me`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`81000` Podgorica, `85320` Tivat, `85330` Kotor, `85310` Budva, `81250` Cetinje)
- **Admin levels**: 25 opštine (municipalities); no provinces
- **Currency**: **EUR (€)** — informally adopted **2002**, no central-bank issuance — UNIQUE in Europe
- **Languages**: Montenegrin (official); Serbian, Bosnian, Albanian, Croatian (regional minorities)
- **Cadastre**: **Uprava za nekretnine (UzN)** — `https://www.gov.me/en/uzn`
  - **eKatastar**: `https://ekatastar.me` — covers ~98% of registered properties (Sept 2025)
  - **Geoportal CG**: `https://geoportal.co.me/`
- **Identifier**: parcela + KO (katastarska opština)
- **Key document**: **list nepokretnosti** (property sheet/extract)
- **EU accession negotiations active** — 19 chapters open, 14 provisionally closed (April 2026); target close 2026-2027, membership 2028

## Section: `--price`

### Primary sources

- **MONSTAT (Statistical Office)**: `https://www.monstat.org/` — quarterly residential price index
- **CBCG (Central Bank Montenegro)**: `https://www.cbcg.me/` — Financial Stability Reports

### Listing platforms

- **Realitica**: `https://www.realitica.com/`
- **Property Finder Montenegro**, **MontenegroProspects**, **Realting.com/montenegro**
- High **English-language coverage** (Russian + EU buyers)
- Major developments: **Porto Montenegro (Tivat)**, **Lustica Bay**, **Dukley Gardens (Budva)**

### 2025-2026 price benchmarks

Coastal-average row is MONSTAT Q3 2025 (residential price index). All per-city / per-development EUR/m² ranges below are `~est.` from Realitica / listing aggregators — verify with cadastre transactions; MONSTAT does not publish per-development ranges.

| Region | EUR/m² (avg) | Notes |
|---|---:|---|
| **Coastal cities avg** | 2,458 | **+23.2% YoY** (MONSTAT Q3 2025) |
| **Tivat (Porto Montenegro)** | ~5,000–12,000 | Premium luxury (est.) |
| **Tivat (general)** | ~2,450 (avg) | High (est.) |
| **Kotor Old Town (UNESCO)** | ~4,000–8,000 | Premium (est.) |
| **Kotor general** | ~2,000–3,500 | High (est.) |
| **Budva luxury** (Sveti Stefan, Dukley) | ~4,000–10,000+ | Resort premium (est.) |
| **Budva general** | ~2,500–5,000 | High (est.) |
| **Herceg Novi** | ~2,000–3,500 | Coastal mid (est.) |
| **Bar** | ~1,500–2,500 | Coastal value (est.) |
| **Ulcinj** | ~1,200–2,500 | South coast (est.) |
| **Podgorica (capital)** | ~2,150 (avg) | Inland (est.) |
| **Cetinje (royal capital)** | ~800–1,500 | Inland heritage (est.) |
| **Mountain (Žabljak, Kolašin)** | ~800–1,800 | Ski + summer (est.) |

### Compute

1. EUR/m² = price / **uporabna površina** (usable area)
2. **Currency**: EUR informally adopted = no FX risk for EUR holders
3. **Coastal vs mountain divergence**: 5-10× multiplier (Tivat luxury vs interior)
4. **UNESCO** premium: Kotor Old Town strict construction = scarcity premium

### Key terms

- UzN = Uprava za nekretnine
- KO = katastarska opština
- List nepokretnosti = property sheet
- Notarska isprava = notarial deed
- Energetski pasoš = energy passport

---

## Section: `--traffic`

### Sources

- **JP Putevi Crne Gore**: `https://www.putevi.me/`
- City traffic data Podgorica, Budva

### Key term

**PGDS (Prosječni godišnji dnevni saobraćaj)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural, mountain)
- 🟡 1,500–10,000 v/d (regional roads, coastal off-season)
- 🟠 10,000–25,000 v/d (Adriatic coastal road peak, Podgorica arterials)
- 🔴 > 25,000 v/d (Adriatic coastal Jul-Aug peak, Sozina tunnel)

---

## Section: `--tax`

### Annual property tax — Porez na nepokretnost

- **0.25–1.0% of market value** (set per opština/municipality)
- Coastal premium properties typically 0.5-1.0%
- Inland Podgorica: 0.25-0.5%
- Annual or quarterly payment

### Transaction taxes — PROGRESSIVE since 1 Jan 2024

**MAJOR CORRECTION**: previously flat 3%; now progressive **marginal** RETT — EUR 4,500 + 5% on the part above EUR 150k; EUR 22,000 + 6% on the part above EUR 500k (bands below are marginal, not whole-price slabs; 6% band + 1 Jan 2024 date per secondary quotes of art. 11 — verify enacted text at Službeni list CG / Poreska uprava):

| Property value (EUR) | Rate |
|---|---:|
| Up to **150,000** | **3%** |
| **150,001–500,000** | **5%** |
| Above **500,000** | **6%** |

- **15-day payment deadline** post-contract; 0.03%/day late interest
- **Buyer pays** transfer tax

### VAT (PDV)

- **21% standard**; first-sale residential subject to 21% VAT in lieu of RETT (NOT a reduced rate)
- **15% reduced bracket** (eff **1 Jan 2025**) for hotel/resort accommodation, restaurant food + non-alcoholic non-sugary drinks (excl. coffee), and books/serial publications — **material for short-let yield modelling** *(2026-05-27 verified, source KPMG ME Tax Alert Oct 2024 + Eurofast Tax Card 2025)*
- **7% reduced** narrowed to essentials (basic food, medicines, drinking water, baby diapers, menstrual products, textbooks); **0%** export carve-out
- New build: 21% VAT included in price
- Resale: subject to RETT, not VAT

### Personal income tax (PIT) — Porez na dohodak fizičkih lica

Salary (gross/month) brackets effective since 1 Jan 2022 (Europe Now I), unchanged through 2026:

| Salary | Rate |
|---|---:|
| Up to €700 | **0%** |
| €700.01–€1,000 | **9%** |
| Above €1,000 | **15%** |

Plus **municipal surtax (prirez)** ~13% of PIT due → effective top rate ~17%. Passive personal income (rental, dividends, royalties, capital gains) → flat **15% PIT**. *(2026-05-27 verified, source PwC Tax Summaries ME)*

### Capital gains

- **15% PIT** on real-estate appreciation
- **Primary residence exempt** under specific conditions

### Total transaction cost (buyer side)

- Resale ≤€150k: ~4-5% (3% RETT + 0.5-1% notary + 0.5% other)
- Resale €150-500k: est. ~4.0-5.9% (RETT effective 3.0% at €150k to 4.4% at €500k = €4,500 + 5% of the excess over €150k, plus ~1-1.5% notary/other per the line above)
- Resale >€500k: est. ~5.4-7.1% up to €2M, rising towards ~7.5% above (RETT effective 4.4% at €500k, 5.2% at €1M, 5.6% at €2M = €22,000 + 6% of the excess over €500k, plus ~1-1.5% notary/other)
- New build: 21% VAT in price + ~2-3% other costs

### Future risk

- EU accession (2026-2028) likely to bring tax harmonization
- New 2026 investor residency program (€150k threshold — see below)

---

## Section: `--rental`

### Long-term residential

- **Zakon o stanovanju**
- Tenant protection moderate
- Standard 1-3 yr contracts; coastal seasonal common

### Short-let (Airbnb)

**MANDATORY before any platform listing**:
- **Municipal registration** (Opština)
- **Classification certificate**
- **Tourism tax certificate** from Ministry of Tourism

#### Tourist tax

- **€0.10–€1.00/day/adult guest**
- Varies by region/category
- **24-hour guest registration** mandatory via government portal

#### Rental income tax

- **15% net PIT**
- Penalty: **€1,200–€16,000** (2-20× minimum wage; Europe Now 2 minimum wage €600 low-qualification / €800 high-qualification, eff 1 October 2024 — verify statutory base for penalty multiplier)

### Tax on rental

- 15% PIT on net rental income
- Tourist tax collected from guest

---

## Section: `--work=<profession>`

### Sources

- **ZZZCG (Zavod za zapošljavanje)**: `https://www.zzzcg.me/`
- **Posao.me**, **LinkedIn ME**, **CGposao**

### Self-employment

- **DOO** (limited): low capital
- **Preduzetnik** (sole trader)
- **PDV** registration: from EUR 30,000 turnover

### Salary benchmarks (2025)

- Median monthly gross:
  - Podgorica: ~EUR 750–1,200
  - Tivat (tourism + luxury): ~EUR 700–1,300
  - Smaller cities: ~EUR 500–800
- **Minimum wage**: EUR 600 (low qualification) / EUR 800 (high qualification) — Europe Now 2, eff 1 October 2024 (see Active fiscal incentives section). **Pending**: Government "Euro model" law package adopted at the 17 Sep 2026 Government session would set minimum NET wages of EUR 1,000 / 1,250 / 1,400 (basic / secondary / higher education) from January 2027 — parliamentary adoption not confirmed, verify at skupstina.me (2026 data, source gov.me)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Seizmološki zavod CG** | — | Seismic monitoring |
| **ZHMS / IHMS Montenegro** (hydromet) | — | Floods, climate |
| **CBR / MUP civilna zaštita** | — | Wildfire/karst |

### Specific risks

#### Earthquake

- **1979 M6.9 Adriatic earthquake** catastrophic (~100 dead, major coastal damage)
- Coast remains seismic
- **Bay of Kotor** historic damage zone
- Modern EC8-compliant builds + retrofit

#### Wildfires

- **Mediterranean coastal critical** Jul-Aug
- Karst pinewood = high fire intensity
- 2017, 2022, 2024 active seasons

#### Karst hazards

- **Durmitor, Lovćen, Orjen** — sinkholes, drainage
- **Coastal hinterland**: cave systems
- Construction requires soil study

#### Floods

- **Bojana river**, mountain torrents
- Coastal flash flooding

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, asbestos cement starts |
| **Pre-1979 quake** | Non-modern seismic; many destroyed/damaged |
| **Post-1979 reconstruction** | Yugoslav-era reconstruction code |
| **Post-2008** | Modern EC8 |
| **Post-2010 luxury developments** | Premium standards |

### Mandatory at sale

| Document | Required because |
|---|---|
| **Energetski pasoš** | Mandatory for sale/lease |
| **Notarska isprava** (notarial deed) | Mandatory; transaction void without |
| **List nepokretnosti** | Cadastre extract (NOT "Izvod iz katastra" colloquially) |

---

## Section: `--mains`

### Sources

- **ViK (Vodovod i kanalizacija)** per municipality:
  - Tivat ViK, Kotor ViK, Herceg Novi ViK, Podgorica ViK
- **Coastal**: aging Soviet-era infrastructure
- **Inland Lim valley + mountain**: limited mains coverage; **septic + cisterne** dominant

### Costs

`~est.` contractor/regional ranges — get a quote.

| Scenario | Cost (EUR) |
|---|---:|
| ViK connection (coastal) | ~1,500–4,500 |
| Septic + cisterna (mountain) | ~2,500–8,000 |
| Bored well (interior) | ~3,500–10,000 |

---

## Cost benchmarks (ME 2026)

| Work | Cost (EUR) |
|---|---:|
| Energetski pasoš | 100–300 |
| Notar fees | 0.5–1.5% |
| RETT (progressive 3/5/6%) | varies |
| **Total transaction cost (≤€150k)** | **~4–5%** of price |
| **Total transaction cost (€150-500k)** | **~6–7%** |
| **Total transaction cost (>€500k)** | **~7–8%** |
| Roof renovation | ~4,000–12,000 |
| Earthquake retrofit | ~15,000–60,000 |
| Energy retrofit | ~8,000–25,000 |
| Solar PV (5kW) | ~4,500–8,000 |

Renovation/retrofit rows are `~est.` from regional contractor ranges — get a quote.

## Active fiscal incentives + visa programs (2025-2026)

### Investor residency (effective 17 January 2026)

- **Replaces abolished CBI Programme** (CBI ended **31 Dec 2022** — historical only)
- **€150k minimum tax-assessed property value** — Art 56 sets the floor at the local tax authority's transfer-tax base per *rješenje o porezu na promet nepokretnosti*, **NOT** the contract/purchase price (low amounts shown on the title deed do not count) (amendments to Zakon o strancima adopted by Parliament on the final day of 2025; entered into force **17 January 2026**)
- **EU/EEA/CH exemption**: the €150k threshold does NOT apply to nationals of EU member states, Iceland, Liechtenstein, Norway or Switzerland
- **50% minimum ownership share**: applicant must hold ≥50% of the property (co-owners each need ≥50% or none qualify)
- Grandfathering: foreigners holding property-based residency before 17 Jan 2026 retain rights without meeting the €150k threshold
- Path: 1-year temp permit (annually renewable) → permanent after 5 years → citizenship after 10 years (5 years temporary + 5 years permanent) *(2026-07-02 verified, source IMI Daily; statute: Zakon o izmjenama i dopunama Zakona o strancima, Sl. list CG br. 003/26, publ. 9 Jan 2026, in force 17 Jan 2026)*

### Other

- **EU accession funds** for energy retrofit
- **Bay of Kotor restoration** programs (UNESCO)
- **Tourism Master Plan** + coastal restrictions

## Common listing platforms

- **Realitica** — biggest English-language
- **Property Finder Montenegro**, **MontenegroProspects**, **Realting.com/montenegro**

## Caveats unique to ME

- **EUR informally adopted 2002** — no central-bank issues currency; UNIQUE in Europe; **no FX risk** for EUR holders
- **CBI Programme ABOLISHED 31 Dec 2022** (was EUR 250k+ minimum) — major historical reference
- **NEW investor residency (effective 17 January 2026)** (€150k property → 5 years to permanent → 10 to citizenship)
- **Progressive RETT since 1 Jan 2024**: 3% / 5% / 6% marginal bands — €4,500 + 5% above €150k, €22,000 + 6% above €500k (not flat 3% as previously)
- **VAT restructure (eff 1 Jan 2025)**: new **15% bracket** added (hotels/restaurants/books); 21% standard; 7% essentials-only; 21% on first-sale residential remains in lieu of RETT
- **Europe Now 2 (eff 1 October 2024)**: minimum wage raised to **€600** (low qualification) / **€800** (high qualification); employee pension-and-disability contribution cut 15% → 10%; employer pension-and-disability contribution eliminated (was 5.5%). **Pending "Euro model"** (Government session 17 Sep 2026, to apply from January 2027): minimum NET wages EUR 1,000 / 1,250 / 1,400 + a further labour-tax cut announced — not yet enacted as read on 2026-09-24, verify at skupstina.me (2026 data, source gov.me)
- **Foreign-buyer rules** (Zakon o svojinsko-pravnim odnosima): foreign natural persons CANNOT own agricultural land, forests, or forest land. **Exception**: up to **5,000 m²** of such restricted land may be acquired if a residential building is on it and the transfer agreement covers residence + adjoining land. **Workaround**: incorporate a Montenegrin **d.o.o.** (domestic legal entity faces no restriction) — the dominant vehicle for agricultural/coastal portfolio buyers *(2026-05-27 verified, source Chambers Real Estate 2025 ME)*
- **Russian buyer concentration post-2022** + EU buyer surge
- **Coastal vs mountain divergence**: Adriatic 5-10× inland prices
- **UNESCO Old Towns** (Kotor, Cetinje) — strict construction, premium scarcity
- **1979 Adriatic earthquake** as historical reference
- **Bay of Kotor restoration** (UNESCO) constraints
- **Tivat Porto Montenegro / Lustica Bay** = ultra-luxury markets €5-12k/m²+
- **Coastal wildfires** Jul-Aug
- **Karst hazards** (Durmitor, Lovćen, Orjen)
- **15-day payment deadline** post-contract for RETT (0.03%/day late interest)

## Reddit / forum sources

- **r/montenegro**, **r/balkans**
- **Total Montenegro News** (English)
- **CdM (Crnogorski monitor)**, **Vijesti**

## Verification authorities

| Authority | When to call |
|---|---|
| **UzN (Uprava za nekretnine)** | Title verification |
| **Notar** | Mandatory closing |
| **Opština** | Property tax + permits |
| **Poreska uprava** | Tax compliance |
| **Ministarstvo turizma** | If short-let |
| **Ministarstvo unutrašnjih poslova** | Investor residency |

## Source URL templates

| Source | URL pattern |
|---|---|
| UzN (cadastre) | `https://www.gov.me/en/uzn` |
| eKatastar | `https://ekatastar.me/` |
| Geoportal CG | `https://geoportal.co.me/` |
| MONSTAT | `https://www.monstat.org/` |
| CBCG | `https://www.cbcg.me/` |
| Realitica | `https://www.realitica.com/` |
| Property Finder ME | `https://www.propertyfindermontenegro.com/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Montenegro portal (e.g. nekretnine.me) |
| Putevi Crne Gore | `https://www.putevi.me/` |
| ZZZCG | `https://www.zzzcg.me/` |
| Poreska uprava CG | `https://www.gov.me/poreskauprava` |

## Statutes

| Statute | Topic |
|---|---|
| **Zakon o svojinsko-pravnim odnosima** | Ownership, etažna svojina, hipoteka, foreign-buyer agricultural-land restriction |
| **Zakon o državnom premjeru i katastru nepokretnosti** | Cadastre / list nepokretnosti / UzN |
| **Zakon o porezu na promet nepokretnosti** | RETT — progressive 3/5/6% since 1 Jan 2024 |
| **Zakon o porezu na nepokretnosti** | Annual property tax 0.25–1.0% (municipal) |
| **Zakon o porezu na dohodak fizičkih lica** | PIT — Europe Now I (Jan 2022) + Europe Now 2 (Oct 2024) |
| **Zakon o porezu na dodatu vrijednost** | VAT — Jan 2025 restructure (21/15/7/0) |
| **Zakon o strancima** | Foreigner law — investor residency 17 Jan 2026 €150k tax-assessed (Sl. list CG br. 003/26, publ. 9 Jan 2026) |
| **Zakon o crnogorskom državljanstvu** | CBI program (abolished 31 Dec 2022) |
| **Zakon o turizmu i ugostiteljstvu** | Short-let classification + municipal registration |

(Sl. list CG issue numbers omitted pending primary-statute lookup — verify before quoting in transaction documents.)

## Status

✅ **Fully populated** as of 2026-04-26. **Last verified**: 2026-05-27. Tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (MONSTAT Q3 2025 + CBCG + Realitica), traffic (Putevi PGDS), tax (porez na nepokretnost 0.25-1.0% + progressive RETT 3/5/6% since Jan 2024 + 21% VAT first-sale + 15% CGT), rental (Opština license + tourist tax + 15% PIT), work (ZZZCG), risks (1979 Adriatic M6.9 + Mediterranean wildfire + karst), mains (ViK per municipality).
**Confidence**: HIGH for EUR informal adoption 2002 (no central-bank issuance UNIQUE); HIGH for progressive RETT 3/5/6% effective 1 Jan 2024; HIGH for CBI abolition 31 Dec 2022 + NEW Jan 2026 investor residency €150k; HIGH for cadastre URLs (gov.me/uzn + ekatastar.me); MEDIUM for MerkaturNekretnine listing platform (could not independently verify); MEDIUM for 21% VAT first-sale framing (in lieu of RETT, not reduced rate).

## Extension TODOs

- [ ] Per-opština property tax rates (25 municipalities)
- [ ] Progressive RETT scenarios (€150k threshold + €500k threshold)
- [ ] CBI abolition transition + NEW Jan 2026 investor residency
- [ ] Bay of Kotor UNESCO construction limits
- [ ] Porto Montenegro / Lustica Bay HOA rules
- [ ] Coastal wildfire vulnerability per opština
- [ ] Karst hazard zoning (Durmitor, Lovćen, Orjen)
- [ ] Russian buyer concentration tracking
- [ ] EU accession reforms 2026-2027
- [ ] 1979 quake-affected coastal zone overlay
