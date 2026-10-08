# Lithuania (LT) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: EUR (eurozone since 1 Jan 2015)
**Lang**: Lithuanian; English broadly available in major banks/legal firms

---

## Country profile

Lithuania is a small Baltic state (~2.8M pop) with a unified land/cadastre system (Registrų centras) — making title checks materially simpler than in Latvia. EU + eurozone + Schengen. Most foreign buyers transact in Vilnius (~€2,930/m² apt avg, +10.7% YoY Dec 2025); secondary cities (Kaunas, Klaipėda) trail. Major 2026 reforms: progressive PIT (20/25/32%) + new immovable-property tax structure for non-main residences. Lithuania exited the BRELL (RU/BY) electricity grid 8 Feb 2025 and synchronized with Continental European Network — energy-security upgrade, a macro context relevant to utility-cost stability (see `--mains`).

---

## Section: `--price`

**Primary index**: **Ober-Haus Apartment Price Index (OHBI)** — the most-cited monthly series; covers 5 largest cities. Quasi-official.
- Page: https://www.ober-haus.lt/en/rinkos_apzvalgos/lithuanian-price-index/
- Annual Market Report PDF: https://www.ober-haus.lt/wp-content/uploads/Ober-Haus-Market-Report-Lithuania-2025.pdf
- **Dec 2025 Vilnius**: €2,930/m² apt avg, +1.0% MoM, **+10.7% YoY**

**Eurostat-aligned HPI**:
- **Statistics Lithuania (OSP)**: https://osp.stat.gov.lt/ (bot-blocked on HEAD, browser-OK)
- **Bank of Lithuania**: https://www.lb.lt/ (bot-blocked, browser-OK) — Real Estate Market Review + stress indicators
- **BIS / FRED**: https://fred.stlouisfed.org/series/QLTN628BIS — quarterly residential property price index

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| Aruodas | https://www.aruodas.lt/ | #1 marketplace, all property types, EN toggle |
| Domoplius | https://www.domoplius.lt/ | #2, agency-heavy |
| Skelbiu | https://www.skelbiu.lt/ | classifieds incl. RE |
| Kampas | https://www.kampas.lt/ | new-build focused |
| Ober-Haus | https://www.ober-haus.lt/ | premium agency + market reports |

**Verdict bands** (cmd: `--price`):
- 🟢 within ±10% of OHBI city avg for comparable district + condition
- 🟡 within ±20%
- 🟠 within ±30%
- 🔴 >±30% — investigate (could be: deferred maintenance, restitution flag, encumbrance, or genuine bargain — verify with Registrų centras extract)

**⚠️ Caveat**: Ober-Haus publishes nominal apt €/m² level for 5 cities (level series); Eurostat HPI is a quality-adjusted index (base=100). **Use whichever fits the question; don't compare growth rates across the two.**

---

## Section: `--traffic`

**Sources**:
- **AB „Via Lietuva"** — the state road authority (the former Lietuvos automobilių kelių direkcija / LAKD; `lakd.lt` now redirects here): https://vialietuva.lt/ — publishes traffic volumes (*eismo intensyvumas*) (2026-09-18 verified)
- **Trafi.lt** real-time congestion (Vilnius): https://www.trafi.com/vilnius-app
- **OSM Overpass** for road class + maxspeed (universal — see `shared/preflight.md`)

**Output**: road class (A1-A18 magistrales / krašto / rajoninis), maxspeed, AADT if available from Via Lietuva, noise translation (dB(A) inferred from OSM `highway=*` tag + maxspeed).

---

## Section: `--tax`

### Transfer / acquisition costs (individual buyer)

**No transfer tax / stamp duty.** Lithuania is unusually clean here.

| Item | Amount |
|---|---|
| Notary fee | 0.45% of price (set by Notary Chamber tariff), capped at ~€5,800 for high-value deals |
| Registrų centras registration | ~€50–€200 standard (~0.03–0.5% of value) |
| **Total round-trip cost** | **~1.0–1.5% buyer side** |

Source: https://www.notarurumai.lt/en/

### Annual immovable property tax (NTM) — **MAJOR REFORM 1 Jan 2026**

**Pre-2026 (now historical)**: residents tax-exempt up to €150,000 total residential value (€200k for families w/ 3+ children); above that 0.5–2% municipal. Most owner-occupiers paid €0.

**From 1 Jan 2026** (NTMĮ art. 6, as published by VMI), marginal bands on the **total** taxable value of an individual's **non-main** residential (plus garages, gardens and other listed non-commercial) property:
- 0% up to €50,000
- 0.2% €50k–€200k
- 0.4% €200k–€400k
- 0.6% €400k–€600k
- 0.8% €600k–€1,000,000
- 1% above €1,000,000 (2026 data, source VMI NTM page)

**Main dwelling**: municipal-set rate 0.1–1% on portion above municipal threshold (min €450,000); per-person or large-family credits: data not publicly available on the VMI NTM page — verify at https://www.vmi.lt/evmi/nekilnojamojo-turto-mokestis2. Main dwelling = the property where the owner has declared residence on the last day of the calendar month (VMI).

Sources:
- Ministry of Finance: https://finmin.lrv.lt/en/news/amendments-to-tax-laws-adopted-by-the-seimas/
- KPMG: https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2025/12/tnf-lithuania-dec-4-2025.pdf

### Capital gains on property sale — GPM (Gyventojų pajamų mokestis)

**2025 schedule (pre-reform — now historical from 1 Jan 2026)**:
- **15% standard** (with two key exemptions):
  - **Owned ≥10 years** → fully exempt (pre-2011 acquisition wrinkle: historical PwC summaries noted a 10-year clock combined with pre-2011 acquisition; re-verify the current 2026 rule at https://taxsummaries.pwc.com/lithuania/individual/income-determination — 2026-05-27)
  - **Declared primary residence ≥2 years** → exempt; OR proceeds reinvested in another residence (within 1 year before / 1 year after sale)
- Above €253,065 (2025 threshold) → **20%**

**2026 reform** (effective 1 Jan 2026): progressive GPM **20% / 25% / 32%** bands on aggregated income live. (2026-05-27 verified — confirm exact thresholds at vmi.lt + KPMG LT 2026 tax card)

Source: https://taxsummaries.pwc.com/lithuania/individual/income-determination

### Rental income — GPM

- **2025**: 15% on amounts up to €253,065/yr; above → 20% (pre-reform)
- **2026**: progressive 20/25/32% bands apply
- **Or** flat **5% via "individual activity certificate"** for short-term lets / **business certificate** for personal-use properties (limits apply)
- **Bank of Lithuania (Lietuvos bankas) macroprudential** Responsible Lending Regulations: **LTV ≤85%** (primary residence), **DSTI ≤40%** of net monthly income, **max maturity 30 years** (effective since 2011, recalibrated 2017 + 2022). Source: https://www.lb.lt/ (2026-05-27 verified)

### VAT new-build

- Standard 21%
- **New build sold within 24 months of completion → 21%**; resale of older buildings → exempt (seller can opt to charge VAT B2B)

---

## Section: `--rental`

### Long-term rental
- 15% PIT or 5% via individual-activity certificate (cleanest route for landlords)
- Standard expense deduction allowed under PIT route

### STR / Airbnb

**Vilnius city tax**: **€2 per person per night** from 1 Jan 2024 (was €1 since 1 Jul 2018); stays of 30+ days exempt (2026 data, source Go Vilnius). Airbnb collects and remits it automatically — Vilnius was the first Baltic city with an Airbnb auto-collection deal, from 1 Feb 2020 (per BNS via Delfi, 15 Jan 2020 — secondary).
- https://www.govilnius.lt/plan-your-trip/city-tax
- https://www.airbnb.com/help/article/2702

**Hosts must hold either**:
- **Individual activity certificate** (5% PIT, full bookkeeping), OR
- **Business certificate (verslo liudijimas)** (fixed-fee, geographically limited, capacity caps)

**All rental income taxable — no exemption threshold.**

**2025-2026 reform watch**:
- EU Regulation 2024/1028 on STR data collection enters mandatory enforcement **May 2026** → Lithuania will introduce a national STR registration number requirement (regulation number + enforcement date verify against the EUR-Lex primary text — the source below is a secondary aggregator)
- No Vilnius-wide cap or zoning ban announced as of Apr 2026 (unlike Lisbon/Barcelona)

Source: https://etias.com/articles/eu-short-term-rental-regulations

---

## Section: `--work=<profession>`

Standard universal `--work=<profession>` resolution. Strongest demand: tech (Vilnius hub, fintech post-Brexit migration), bio-tech (Kaunas, Vilnius), logistics (Klaipėda free port), shared-services (Vilnius). Remote/hybrid common.

---

## Section: `--risks`

### Flood
- **Aplinkos apsaugos agentūra (EPA) Flood Risk Information System**: https://potvyniai.aplinka.lt/ + http://vanduo.gamta.lt/info/potvyniai.aplinka.lt
- 54 Significant Flood Areas (PFRA 2011-2018)
- Highest exposure: **Nemunas Delta** (Šilutė, Rusnė), **Klaipėda coast** (storm-surge + Curonian Lagoon), Telšiai/Tauragė/Kėdainiai/Panevėžys/Kaunas districts
- ThinkHazard rating: https://thinkhazard.org/en/report/147-lithuania/FL

### Coastal
- Klaipėda + Curonian Spit (Neringa) — sea-level rise + storm surge; compound coastal-river risk documented (MDPI Water 2022)

### Seismic
- Negligible. Baltic Shield craton — peak ground acceleration ~<0.04g est. for 475-year return (European seismic hazard maps — verify at ESHM); **no building seismic code requirement**

### Forest fire
- Highest in **Dzūkija** (SE LT — Varėna, Alytus, Lazdijai, Druskininkai districts) — Scots pine on infertile sandy soils + Čepkeliai peatland
- Source: https://www.mdpi.com/2073-445X/11/2/260

### Geoportal layers
- https://www.geoportal.lt/ — overlay flood, environmental, protected, cadastre

### Mandatory diagnostics

- **Energy Performance Certificate (Pastato energinio naudingumo sertifikatas)**: mandatory for sale, rental, new construction. Classes A++ to G (9 classes). Validity 10 years. STR 2.01.02:2016 governs.
  - https://www.namupridavimas.lt/en/services/certification-of-the-energy-performance/
- **Radon**: national avg ~55 Bq/m³ (well below EU action 300 Bq/m³). **Karst region in N Lithuania (Biržai, Pasvalys, Pakruojis)** averages ~125 Bq/m³ with localized hot-spots. **No statutory pre-sale radon test required.** https://radonas.lt/
- **Asbestos**: no mandatory pre-sale survey for residential. Soviet-era apartment blocks (1960s–80s) commonly contain asbestos (slate roofing, pipe insulation, wall panels) — material risk on retrofits

---

## Section: `--mains`

### Cadastre / Land Registry — UNIFIED

**VĮ Registrų centras** (State Enterprise Centre of Registers):
- https://www.registrucentras.lt/ + https://www.registrucentras.lt/en/
- Single national register: cadastre + Real Property Register + addresses + legal persons
- Search by cadastral number, address, or unique ID
- Public: anyone can request paid extracts (~€3-€8 online); no residency required
- **Encumbrances/mortgages NOT visible online for free** — must buy the extract

**Spatial portal**: https://www.geoportal.lt/ (INSPIRE-compliant national SDI)

### District heating

Soviet-built; substantially modernized. Network heat losses dropped from **33% → 15%** post-EU accession.
- **LSTA stats**: https://lsta.lt/en/about-dh-sector/ (browser-OK)
- **IEA Lithuania 2025 review**: https://iea.blob.core.windows.net/assets/0f37fbed-856d-4fde-8f2b-4db10d9bfd2a/Lithuania2025.pdf
- Vilnius/Kaunas/Klaipėda DH largely biofuel/biomass-powered (~70%+)

**Soviet-era multi-apartment quirk**: Many old blocks have **single-pipe vertical heating risers** — no per-apartment metering or shut-off; bills allocated by m². "Renovated" (apkainotas) blocks have horizontal distribution + individual meters.

### Water/sewage
- Municipal utilities: Vilniaus vandenys, Kauno vandenys, etc.
- Rural areas: well + septic (~60% of rural households — est., re-verify with osp.stat.gov.lt household water-supply census)
- No nationwide single registry — check connection per-property via the municipal utility

### Electricity
- **ESO (Energijos skirstymo operatorius)** — sole DSO
- **Lithuania exited BRELL grid 8 Feb 2025** and synchronized with Continental European Network — landmark energy-security event; post-synchronization, wholesale electricity prices appear to have stabilized vs the 2022-23 spike (verify current tariffs at ESO / Litgrid)

---

## Section: `--crime`

See `shared/crime-sources.md` for the per-country contract. Lithuania uses:
- **Informacinės technologijos ir komunikacijos departamentas (ITKD) — Police**: https://www.ird.lt/
- **Statistics Lithuania crime tables**

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
| Vilnius apt €/m² avg | €2,930 (OHBI Dec 2025) |
| Kaunas / Klaipėda | secondary cities trail Vilnius by ~25–35% |
| Notary fee | 0.45% of price, capped ~€5,800 |
| Registration fee | ~€50–€200 |
| Total acquisition costs | ~1.0–1.5% |
| Annual property tax (main, ≤€450k) | typically €0 |
| EPC certificate | ~€150–€400 |

---

## Active fiscal incentives

- **No transfer tax** — already a structural incentive
- **Primary residence ≥2yr CGT exemption** OR ≥10yr full exemption
- **Reinvestment relief** within 1 year before/after primary-residence sale
- **5% individual-activity flat tax** for STR if registered

---

## Foreign-buyer rules

- **EU/EEA citizens**: free to buy residential, commercial. Agricultural / forest land requires 3 years' agricultural activity in LT (Art. 47 Constitution, transitional rules post-EU accession)
- **Non-EU**: can buy residential and commercial urban property freely; **CANNOT buy agricultural / forest land** unless holding LT residency permit + meeting activity criteria. https://www.elra.eu/contact-point-contribution/lithuania/limitations-to-foreigners-10/
- **Border-zone**: no general statutory ban; some specific national-security parcels excluded
- **Russian/Belarusian nationals (post-2022)**: residence permits heavily restricted → indirectly blocks land/agricultural purchases requiring residency. Bank account opening (KYC) and notarial AML checks now near-blocking even for residential

---

## Country-specific quirks

- **Vilnius land readjustment**: Soviet-era blocks often sit on land never properly cadastralized at parcel-by-parcel level. Many condominiums have **shared/undivided parcel** (bendrojo naudojimo žemės sklypas) — affects renovation, easements, additions. Confirm cadastral parcel matches building footprint via Registrų centras
- **Klaipėda Free Economic Zone** (412 ha): 0% real estate tax inside the zone, 0% corporate tax 10 years. Industrial only — not residential. https://www.fez.lt/
- **Denationalization legacy**: 1991 restitution applied **only to LT citizens at time of nationalization**, excluding most diaspora. Largely concluded; **no restitution exists yet for heirless Jewish property**. Some urban plots in Vilnius/Kaunas have unresolved historic-claim flags — pull "Ownership history" in Registrų centras extract
- **Curonian Spit (Neringa) UNESCO**: strict heritage rules; new construction effectively banned in protected zone. Buy resale only; expect renovation permit complexity
- **Old Town Vilnius (UNESCO 1994)**: demolition forbidden, exterior changes need Heritage Commission consent
- **Banking**: 3 Scandinavian banks dominate (Swedbank, SEB, Luminor). Mortgage to non-residents possible but typically requires LT income source or a larger deposit (non-resident LTVs commonly capped well below the 85% resident ceiling at `--tax` — verify with the specific bank)

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre + title | Registrų centras | https://www.registrucentras.lt/ |
| Tax | VMI (State Tax Inspectorate) | https://www.vmi.lt/ |
| Notary | Lithuanian Notary Chamber | https://www.notarurumai.lt/en/ |
| Flood | EPA / Aplinka | https://potvyniai.aplinka.lt/ |
| Radon | Radiation Protection Centre | https://radonas.lt/ |
| Foreign land purchase | Migration Department | https://www.migration.lt/ |

---

## Source URL templates

| Field | Template |
|---|---|
| Cadastral extract | https://www.registrucentras.lt/p/1094 |
| Tax rules (PIT/CGT) | https://taxsummaries.pwc.com/lithuania/individual/income-determination |
| Property tax 2026 | https://kpmg.com/kpmg-us/content/dam/kpmg/taxnewsflash/pdf/2025/12/tnf-lithuania-dec-4-2025.pdf |
| Flood map | https://potvyniai.aplinka.lt/ |
| Radon | https://radonas.lt/ |
| Vilnius city tax | https://www.govilnius.lt/plan-your-trip/city-tax |

---

## Status

**Confidence**: HIGH on transfer-tax (none), Vilnius price index (Ober-Haus Dec 2025 verified), 2026 NTM brackets (VMI NTM page, primary), STR Vilnius city tax (€2 from 1 Jan 2024, Go Vilnius; re-verified 2026-09-24). MEDIUM on per-municipality 2026 NTM rates (some not yet published), STR national registration number (EU 2024/1028 pending May 2026 implementation). LOW on per-locality rental yield benchmarks (no STATEC-grade source). Tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)

---

## Extension TODOs

- Per-municipality 2026 NTM rate table once Vilnius/Kaunas/Klaipėda councils publish
- Specific per-district Vilnius €/m² rents (currently only sale prices)
- LV/LT/EE Baltic comparison primer for cross-border investors
