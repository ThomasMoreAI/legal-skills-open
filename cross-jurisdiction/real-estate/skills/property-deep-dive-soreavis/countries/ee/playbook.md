# Estonia 🇪🇪 — Property Due-Diligence Playbook

ISO2: `ee`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 5 digits (`10115` Tallinn central, `50050` Tartu, `80010` Pärnu)
- **Admin levels**: 15 maakond (counties) + 79 omavalitsus (municipalities)
- **Currency**: **EUR (€)** — adopted 1 Jan 2011
- **Languages**: Estonian (official); Russian minority (Northeast); English widely used in business
- **Cadastre**: **Maa-amet** + **e-Kinnistusraamat** (RIK e-Land Register)
  - Geoportaal: `https://geoportaal.maaamet.ee/eng/services/cadastral-register-query-p302.html`
  - e-Land Register: `https://www.rik.ee/en/e-land-register/e-land-register-portal`
- **Identifier**: `kinnistu number` (registered immovable number) + cadastral parcel code
- **Ownership types**:
  - **Kinnisasja omandi** (full ownership)
  - **Hoonestusõigus** (right of superficies)
  - **Korteri-omand** (apartment ownership with land share)
- **e-Notar**: digital notarisation with biometric AI verification — **UNIQUE globally**
- **EU member since 2004 + eurozone since 2011**

## Section: `--price`

### Primary sources

- **Statistikaamet (Statistics Estonia)**: `https://stat.ee/en/` — official housing price + transactions
- **Maa-amet transactions register**: `https://geoportaal.maaamet.ee/` — public per-transaction data
- **e-Kinnistusraamat (RIK)**: `https://www.rik.ee/en/e-land-register/e-land-register-portal` — title + owner (with eID)
- **Eesti Pank** (central bank) housing market reports

### Listing platforms

- **KV.ee** — DOMINANT (~80–85% market share, BCG): `https://www.kv.ee/en/`
- **City24.ee** — #2 (also BCG): `https://www.city24.ee/`
- **Maa365.ee** — rural/land-focused
- Agency networks: **Pindi Kinnisvara**, **Domus Kinnisvara**, **Uus Maa**

### 2025 price benchmarks (Statistikaamet + KV.ee)

| Region | Avg €/m² (apt secondary) | Avg €/m² (apt primary/new) |
|---|---:|---:|
| **Tallinn (Põhja-Tallinn, Kesklinn)** | 3,700 (+5.4% YoY) | 4,540 (+6.7% YoY) |
| **Tartu** | 2,443 (-6.8% YoY) | ~3,200 |
| **Pärnu (coastal)** | 2,331 (+13.7% YoY) | ~3,100 |
| **Narva** | 950 | — |
| **Kuressaare (Saaremaa)** | 1,400 | — |
| **Tartu maakond rural** | 800–1,200 | — |

### Compute

1. €/m² = price / **kasulik pind** (usable area)
2. Cross-check **Maa-amet transactions** (free public) + **KV.ee asking prices**
3. **Tallinn districts vary**: Kesklinn premium 4,500+, suburbs 2,800-3,500
4. **Tartu softening 2025** (-6.8% YoY) reflects general slowdown; Tallinn + Pärnu still rising

### Key terms

- Kinnistu = registered immovable
- Korteriomand = apartment ownership
- Korteriühistu = apartment association (HOA)
- Maamaks = land tax
- Energiamärgis = energy certificate

---

## Section: `--traffic`

### Sources

- **Maanteeamet (Estonian Transport Administration)**: `https://www.transpordiamet.ee/` (formerly Maanteeamet)
- **Liiklusloendus** (traffic counts) — annual published
- Estonian Open Data Portal: `https://avaandmed.eesti.ee/`

### Key term

**ÖKL (Ööpäevane keskmine liiklus)** = AADT-equivalent.

### Verdict bands

- 🟢 < 1,500 v/d (residential, rural)
- 🟡 1,500–10,000 v/d (regional roads, urban arterial)
- 🟠 10,000–25,000 v/d (Tallinn arterials, T1, T2)
- 🔴 > 25,000 v/d (Pärnu mnt, Narva mnt, ring road)

---

## Section: `--tax`

### Annual property tax — Maamaks (LAND ONLY — UNIQUE)

**Estonia has NO annual property tax on buildings — only on LAND.**

#### Maamaks reform 2024-2026

- **2024**: max +10% increase per cadastral unit, or +€5 floor
- **2025**: max +50% increase or +€20 floor
- **2026**: limit set by **each local government** at 10–100%; €5 floor; **homeowner exemption €0–1,000** (also municipality-set)

#### Rate ranges (set per municipality)

| Land type | Rate range |
|---|---|
| Residential / yard land | 0.1–1% |
| Profit-yielding land | 0.1–0.5% |
| Other land | 0.1–2% |

#### Typical bills

- Tallinn 100m² apt with land share: **~€100–€500/yr** (est. — depends on municipality rate within the 0.1–1% band above × assessed land value; confirm on the EMTA maamaks notice)
- Tartu single-family with 1,000m² plot: **~€200–€600/yr** (est.)
- Pärnu coastal villa with 2,000m² plot: **~€500–€1,500/yr** (est.)

### Transaction taxes

- **NO transfer tax** (UNIQUE in EU)
- **Notary fee scale**: ~€100–€500 depending on price (est. range — confirm exact fee against the statutory notary tariff at the e-Notar / notary quote stage)
- **Land Register fee**: ~€20–€80 (est. — confirm against current statutory land-register fee)
- **e-Notar digital signing**: same fee scale

### VAT (käibemaks)

- **22% standard** (raised from 20% on 1 Jan 2024)
- **24% from 1 July 2025** (Security Tax Act; raised from 22 %; **made permanent April-May 2026** — VAT will NOT revert to 22 % from 2029) — Käibemaksuseadus (KMS) / EMTA. (2026-05-27 verified, source KPMG + Eesti Kaubandus-Tööstuskoda)
- **Accommodation-services reduced VAT** (hotel-classified short-let): **9 % → 13 % from 1 Jan 2025** (separate from standard rate; applies where the host provides hotel-like services)
- New builds + significantly renovated buildings + building land: **VAT applies**
- Resale: generally **VAT-exempt**

### Capital gains — Tulumaks (Tulumaksuseadus)

- **Tulumaks 22 % from 1 Jan 2025 and still 22 % in 2026** (EMTA tax-rates page, 2026 block: "The rate of withheld income tax is 22%"; corporate distributed profit 22/78; CGT integrated into general Tulumaks). (2026 data, source [EMTA — Tax rates](https://www.emta.ee/en/private-client/taxes-and-payment/declaration-income/tax-rates))
- **Primary residence exempt** (>2-year ownership rule simplified)

### Total transaction cost (buyer side)

- Resale primary: ~**0.5–1%** of price (notary + land register only)
- New build: 24% VAT in price + ~1% other costs

### Future risk

- Maamaks rates rising 2024-2026 (municipality discretion)
- VAT may rise further in 2026 budget
- E-government efficiency continues — record-time transactions

---

## Section: `--rental`

### Long-term residential

- **Võlaõigusseadus § 271 ff** (Law of Obligations Act § 271+) governs lease
- **Tenant protection moderate** (less strict than DE/AT)
- **Indekseerimine** allowed (CPI-linked)

### Short-let

**EU Reg (EU) 2024/1028** (STR data-collection) applies EU-wide **from 20 May 2026** — now in force — introducing a mandatory per-listing registration number + platform data-sharing/verification obligations; it does **not** harmonise substantive limits (local night-caps stay national). (2026-07-02 verified, source EUR-Lex Reg (EU) 2024/1028 + Bird & Bird)

Estonia has **NO national mandatory STR-registration regime** in force. The Ministry of Economic Affairs (**MKM**) is only *proposing* clearer Tourism Act rules as of June 2026, targeted to take effect **2027-2028** (source ERR News 2026-06-25); market participants want a nationwide accommodation database "but the Ministry of Economic Affairs and Communications is not listening" (ERR opinion, 2026-02) — i.e. no such requirement exists yet. In Sep 2026 MKM said it sees **no need for new national STR limits** despite a European Commission proposal letting local governments restrict short-term rentals; the government is still developing its position (source ERR News 2026-09-13, secondary — verify with MKM).

- **Tulumaks** (income tax) 22 % on rental earnings (2025 and 2026 — EMTA tax-rates page) (Tulumaksuseadus)
- **VAT registration required if revenue > €40,000/year** (then 24% VAT on bookings)
- **No Tallinn citywide night-cap** as of early 2026; an **Old Town (Vanalinn)** cap is only *proposed* under the City of Tallinn 2025-2035 Old Town development plan — not enacted (source Investropa 2026)
- Guest-registration to **Politsei- ja Piirivalveamet (PPA)** within 24h — *unverified for Estonia* (guest data historically routes to Statistikaamet, not PPA; verify with PPA before relying)

### Tax on rental

- Residential rental: 22% income tax
- **No accelerated depreciation** (unlike some other EU)
- Mortgage interest deductible

---

## Section: `--work=<profession>`

### Sources

- **Töötukassa (Estonian Unemployment Insurance Fund)**: `https://www.tootukassa.ee/`
- **CV-Online.ee, MeMa, CV.ee, LinkedIn EE**
- **Riigi Tugiteenuste Keskus** for state jobs

### Self-employment

- **FIE (Füüsilisest isikust ettevõtja)** = sole trader
- **OÜ (Osaühing)** = limited; **min €2,500 capital** (statutory — verify current threshold in Äriseadustik) but pay-when-distributed
- **Käibemaksu** registration: from €40,000 turnover (statutory threshold — verify current value with EMTA / Käibemaksuseadus)
- **e-Residency** program for non-residents

### Salary benchmarks (2025)

- Median monthly gross:
  - Tallinn: ~€2,200–€3,000
  - Tartu: ~€1,800–€2,500
  - Smaller cities: ~€1,500–€2,200
- **Minimum wage**: €820/month (2025)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Keskkonnaagentuur (Environment Agency)** | `https://www.ilmateenistus.ee/` | Climate, weather, hydrology |
| **Keskkonnaportaal** | `https://keskkonnaportaal.ee/en/` | Environmental hazard maps |
| **Maa-amet flood map** | `https://keskkonnaportaal.ee/en/topics/remote-sensing/flood-map` | Sentinel-1 satellite-derived (operational) |
| **EGT (Eesti Geoloogiateenistus)** | `https://www.egt.ee/en` | Geology, **radon**, geohazards |
| **Päästeamet (Rescue Board)** | `https://www.rescue.ee/` | Emergency response |

### Specific risks

- **Flood**: Pärnu (storm surge worst-case), coastal Hiiumaa/Saaremaa
  - **Sentinel-1 flood map** for operational satellite data
- **Storms**: Baltic winter storms (Gudrun 2005 type)
- **Radon**: limestone hotspots — **north coast, Viimsi, Harjumaa, Lääne-Viru**
  - EGT radon map per region
  - Higher risk than NL/UK; lower than CZ/SK
- **Climate**: warming + Baltic sea-level rise; permafrost not relevant
- **Earthquake**: very low (Fennoscandian shield)
- **Wildfire**: low-moderate (peat bog + boreal forest)

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1990 (Soviet era)** | Asbestos common, lead paint, dated heating |
| **Khrushchyovka + Brezhnev panel** | Energy-inefficient, asbestos |
| **1990s–2000s** | Improving insulation |
| **Post-2008** | Modern energy code |
| **Post-2020 LEED/BREEAM** | Some commercial; growing residential |

### Mandatory at sale

| Document | Required because | Validity |
|---|---|---|
| **Energiamärgis** (energy certificate) | Mandatory at sale + lease | 10 years |
| **e-Notar contract** | All sales | At sale |
| **Kinnistusraamat extract** | Title verification | At sale |

### Climate change projections

- **est. +2.0–3.5°C** by 2100 (climate-model projection — verify against Keskkonnaagentuur climate scenarios / IPCC RCP figures, source list above)
- **Baltic sea-level rise**: est. +20–50 cm by 2100 (Pärnu, Saaremaa, Hiiumaa) (climate-model projection — verify against Keskkonnaagentuur / IPCC scenarios)
- **Increased winter rainfall** + reduced winter snow
- **More extreme storms**

---

## Section: `--mains`

### Sources

- **Tallinna Vesi**: `https://www.tallinnavesi.ee/` (Tallinn water/sewer)
- **Per-omavalitsus** (municipality) utilities: AS Tartu Veevärk (Tartu), AS Pärnu Veevärk (Pärnu)
- Universal in cities; rural **kogumiskaev** (cesspits) common

### Costs

Indicative installer/connection ranges (est. — confirm with a current utility tariff or installer quote):

| Scenario | Cost (€) |
|---|---:|
| Mains connection (Tallinn) | ~€3,000–€8,000 (est.) |
| Septic / individual treatment | ~€4,000–€10,000 (est.) |
| Bored well | ~€5,000–€12,000 (est.) |

---

## Cost benchmarks (EE 2026)

Statutory fees as noted; all construction/retrofit figures are **est. indicative ranges** (contractor quote bands — verify on quote):

| Work | Cost (€) |
|---|---:|
| Energiamärgis | 150–400 |
| Notary fee (e-Notar) | 100–500 |
| Land Register fee | 20–80 |
| **Total transaction cost (buyer)** | **~0.5–1%** of price (lowest in EU) |
| Roof renovation | 8,000–20,000 |
| Asbestos abatement | 2,000–10,000 |
| Energy retrofit (Class E → A) | 25,000–60,000 |
| Insulation upgrade | 5,000–15,000 |
| Heat pump | 8,000–18,000 |
| Solar PV (5kW) | 5,000–10,000 |

## Active fiscal incentives (2025-2026)

- **KredEx** energy retrofit grants (KredEx korterelamute toetus)
- **First-time buyer**: no specific scheme but low transaction costs help
- **Solar PV grants**: regional + national
- **District heating connection** subsidies in Tallinn

## Common listing platforms

- **KV.ee** — biggest (~80-85% market share)
- **City24.ee** — better UX, expat-friendly
- **Maa365.ee** — rural

## Caveats unique to EE

- **e-government / e-Notar digital property contracts** — UNIQUE globally; sign with Estonian eID, mobile-ID, or Smart-ID
- **NO annual tax on buildings** — only land (maamaks) — UNIQUE in EU
- **NO transfer tax** — only notary + land register fee — UNIQUE
- **Maamaks reform 2024-2026** — rates rising, municipality discretion expanded
- **VAT 20% → 22% (1 Jan 2024) → 24% (1 Jul 2025, permanent from 2026)** — major rise (2026-05-27 verified)
- **Tulumaks (income tax + CGT integrated) 22 % from 1 Jan 2025, unchanged in 2026** (2026 data, source EMTA tax-rates page)
- **Currency: EUR since 2011** (no FX risk for eurozone buyers)
- **Tallinn + Pärnu rising 2025** while Tartu softening (-6.8% YoY)
- **Soviet-era panel buildings**: Khrushchyovka + Brezhnev — many in Tallinn Lasnamäe, Mustamäe, Õismäe — energy-inefficient + asbestos
- **No national short-let registration regime yet** — EU Reg (EU) 2024/1028 (per-listing ID + platform data-sharing) applies from 20 May 2026; MKM Tourism Act rules only proposed (targeted 2027-2028)
- **e-Residency**: foreign nationals can register Estonian companies remotely
- **Bordering Russia (Ida-Virumaa)**: geopolitical tail risk; Narva primarily Russian-speaking
- **Korteriühistu** financial health critical for apt purchase
- **Pärnu coastal market**: tourist-driven + EU-buyer demand growing

## Reddit / forum sources

- **r/Estonia** — biggest community
- **r/Tallinn**
- **e-Estonia.com** (gov info)
- **Estonian World** (English news)
- **The Baltic Times**

## Verification authorities

| Authority | When to call |
|---|---|
| **Maa-amet** | Cadastre verification |
| **e-Kinnistusraamat (RIK)** | Title + owner verification |
| **e-Notar** | Sale process |
| **EMTA (tax authority)** | Maamaks + VAT |
| **Local omavalitsus** | Local maamaks rate + permits |
| **Korteriühistu** | If apartment |
| **EGT** | Radon |

## Source URL templates

| Source | URL pattern |
|---|---|
| Maa-amet Geoportaal | `https://geoportaal.maaamet.ee/` |
| e-Kinnistusraamat (RIK) | `https://www.rik.ee/en/e-land-register/e-land-register-portal` |
| Statistikaamet | `https://stat.ee/en/` |
| KV.ee | `https://www.kv.ee/en/` |
| EMTA (tax) | `https://www.emta.ee/en/` |
| Keskkonnaportaal | `https://keskkonnaportaal.ee/en/` |
| EGT (geology + radon) | `https://www.egt.ee/en` |
| Maanteeamet traffic | `https://www.transpordiamet.ee/` |
| Eesti Pank | `https://www.eestipank.ee/en/` |

## Status

✅ **Fully populated** as of 2026-04-25. Rental: Sep 2026 MKM STR position added 2026-09-24 in the October regwatch wave from ERR News (secondary); EU Reg 2024/1028 date and Tallinn Old Town status not re-read. Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing (Statistikaamet + Maa-amet + KV.ee), traffic (Maanteeamet), tax (maamaks reform 2024-2026 + VAT 22%→24% + 22% CGT), rental (EU Reg 2024/1028 from 20 May 2026; no national STR reg yet), work, risks (flood + radon + Baltic storms), mains all have primary government sources + cost benchmarks.
**Confidence**: HIGH for maamaks reform timeline (2024 +10%, 2025 +50%, 2026 municipality-set 10-100%); HIGH for VAT 24% from 1 Jul 2025 (corrected from earlier "1 Jan 2025" data point; made permanent April-May 2026); HIGH for Tulumaks 22 % from 1 Jan 2025, still 22 % in 2026 (EMTA); HIGH for e-government sources (Maa-amet + RIK gold-standard); MEDIUM for short-let reg specifics (2026-07-02 verified — no national regime yet; EU Reg 2024/1028 in force 20 May 2026, MKM Tourism Act reform only proposed for 2027-2028).

## Extension TODOs

- [ ] Per-omavalitsus maamaks rates table
- [ ] Korteriühistu financial health rubric
- [ ] e-Notar digital signing flow for non-residents
- [ ] e-Residency property purchase flow
- [ ] Soviet-era panel building inventory (Lasnamäe, Mustamäe)
- [ ] Pärnu coastal market vs inland comparison
- [ ] Radon zone overlay (EGT) per parish
- [ ] Geopolitical risk assessment (Ida-Virumaa)
- [ ] District heating connection availability
- [ ] KredEx grant eligibility decision tree
