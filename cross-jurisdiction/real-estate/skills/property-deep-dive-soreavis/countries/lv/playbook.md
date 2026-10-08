# Latvia (LV) — Property Due-Diligence Playbook

**Status**: ✅ fully populated as of 2026-04-26
**Currency**: EUR (eurozone since 1 Jan 2014 — joined a year before LT)
**Lang**: Latvian; English available at top 4 banks + Lursoft commercial gateway

---

## Country profile

Latvia is the middle Baltic state (~1.85M pop). **Cadastre and Land Book are SEPARATE registers** (unlike Lithuania's unified Registrų centras) — VZD = physical/fiscal description; Zemesgrāmata = legal title. Both must be checked. Riga apartment €/m² is structurally lower than Vilnius (~€865 standard segment vs ~€2,930 est. Vilnius) — slower post-2008 recovery + supply mix dominated by Soviet "khrushchyovkas". Critical Latvia-specific gotcha: **compulsory land lease (dalītais īpašums)** — many Soviet-era blocks in Riga have apartments owned separately from underlying land (often pre-1940 owner via restitution). EU + eurozone + Schengen. Major 2025 reform (in force 1 Jan 2025, rates unchanged for 2026): PIT to 25.5%/33% + capital-income to 25.5% (was 20%).

---

## Section: `--price`

**Primary index**: **CSP (Central Statistical Bureau)** — Eurostat-aligned HPI quarterly
- https://www.csp.gov.lv/ + EN https://stat.gov.lv/en
- **Q4 2025 LV HPI**: 224.02 (Trading Economics from CSP); +8.4% YoY through Q3 2025

**Latvijas Banka**: https://www.bank.lv/ — Real Estate Market Surveillance Reports (annual + quarterly)

**BIS / FRED**: https://fred.stlouisfed.org/series/QLVN628BIS

**Verified figures (early 2026)**:
- **Riga standard-type apartments**: ~€865/m² (lower segment, Soviet-era)
- **Riga central premium**: €2,900–€7,000/m²
- **Jūrmala / coastal premium**: significant uplift, wooden-architecture protected
- Source: https://www.globalpropertyguide.com/europe/latvia/price-history

**Listings**:

| Portal | URL | Notes |
|---|---|---|
| SS.lv / SS.com | https://www.ss.lv/ + https://www.ss.com/ | #1, all classifieds, RE dominant |
| City24 | https://www.city24.lv/ | Pan-Baltic agency listings |
| Varianti | https://www.varianti.lv/ | Latvian agency portal |
| Realto | https://www.realto.lv/ | Aggregator |

**Verdict bands**:
- 🟢 within ±10% of CSP/local-segment €/m²
- 🟡 ±20%, possibly compulsory-land-lease (dalītais īpašums) discount
- 🟠 ±30%, investigate land-ownership / encumbrance
- 🔴 >±30% — likely a Latvia-specific structural issue

---

## Section: `--traffic`

**Sources**:
- **Latvijas Valsts ceļi (LVC)**: https://lvceli.lv/
- **Riga real-time** via Mobills.lv / Waze
- **OSM Overpass** for road class + maxspeed (universal)

---

## Section: `--tax`

### Stamp duty (transfer tax) — Zemesgrāmata registration

- **Individual buyer**: **1.5%** of the higher of (purchase price OR cadastral value), capped at **€50,000**
- **Legal entity buyer**: **2%**, same cap
- Plus €15 clerk fee + €7 ownership-certificate fee to Land Book
- **Notary fee** for purchase contract: **€117–€272** (modest — far cheaper than LT's % notary fee)

**Total round-trip cost**: ~1.7–2.2% individual buyer

Source: https://taxsummaries.pwc.com/latvia/corporate/other-taxes

### Annual immovable property tax (NĪN — Nekustamā īpašuma nodoklis)

- **Land**: 1.5% of cadastral value (flat)
- **Residential buildings**: progressive **0.2% / 0.4% / 0.6%** of cadastral value
  - Typical thresholds: 0.2% up to ~€56,915, 0.4% next bracket, 0.6% above ~€106,715
  - Municipalities have flexibility 0.2%–3.0% within statutory band
- Local councils set actual rates in binding regulations. Riga uses progressive 0.2/0.4/0.6 on residential

**2025 cadastral value reform**: Two cadastral values now exist — **fiscal** (used for NĪN, frozen at 2012-13 market basis) and **universal** (closer to current market). Tax still uses fiscal value, so NĪN remains low relative to actual prices.

Sources:
- https://www.vid.gov.lv/en/immovable-property-tax
- https://www.fm.gov.lv/en/tax-rates-2

### Capital gains on property sale (LV individuals)

- **Standard rate 25.5%** from 1 Jan 2025 (2025 data, source VID) — 20% applies in 2025-2027 only to gains on capital-asset deals initiated by 31 Dec 2024 but not completed by then, with a capital-gains declaration filed
- **From 2025 onwards**: **25.5%** capital-gains rate (2025 PIT reform; unchanged on the VID rates page updated 30 Dec 2025)
- **Exemption**: held **≥60 months (5 years)** AND registered as primary residence **≥12 months** within that 60-month window → fully exempt (BOTH conditions, not OR)

Source: https://taxsummaries.pwc.com/latvia/individual/income-determination

### Rental income (individual)

- **10% PIT flat** after deductions if registered as "performer of economic activity without forming a business" — cleanest route for landlords
- OR full progressive **PIT (Iedzīvotāju ienākuma nodoklis, IIN)** 25.5% up to €105,300 / 33% above + additional **3% surcharge above €200,000** total annual income (2025 PIT reform, in force 1 Jan 2025; 2026 data, source VID)

### VAT new-build

- **Standard 21%**
- **New build (first sale within 1 year of completion or non-occupied)**: 21% VAT
- Resale of "used" buildings: VAT-exempt (B2B opt-in available)
- 12% reduced rate does NOT apply to property

---

## Section: `--rental`

### Long-term rental
- 10% PIT flat (deduction-allowed) is dominant route
- Standard expense deduction allowed
- 2025 platform-reporting amendments require Airbnb/Booking to report incomes to VID (DAC7-aligned)

### STR / Airbnb

**Apr 2026 state**: **No national STR registration system in force yet.** Riga has no city-wide ban, no licensing limit, no zoning prohibition. Operators must register economic activity with VID and pay applicable PIT.

**Reform incoming**: Ministry of Economics drafting national STR register per EU Regulation 2024/1028 (mandatory by **May 2026**). Trigger event: 2021 Merķeļa iela 8 fire in unlicensed hostel.
- https://www.em.gov.lv/en/article/latvia-along-other-eu-countries-there-plan-establish-short-term-rental-regulations-reduce-shadow-economy

**Tourist tax** (Riga): **€1/night per guest** (max €10/stay; children <18 exempt) since **January 2023** — rising to **€2/night from 1 Jan 2027** (agreement 19 May 2026 between Riga City Council and tourism industry). Compare Vilnius (already €2/night). (2026-05-27 verified, source riga.lv)

---

## Section: `--work=<profession>`

Riga financial-services hub (post-2018 ABLV scandal still recovering); Daugavpils/Rēzekne (Latgale) lower demand; Liepāja/Ventspils ports + manufacturing. Remote/hybrid common.

---

## Section: `--risks`

### Flood
- **LVĢMC (Latvian Environment, Geology and Meteorology Centre)**: https://www.lvgmc.lv/
- Flood Risk Information System: https://videscentrs.lvgmc.lv/iebuvets/pludu-riska-informacijas-sistema
- Three Riga flood drivers:
  1. Storm-surge in Gulf of Riga (S/SW storms)
  2. Daugava spring snowmelt discharge maxima
  3. Urban pluvial (densely-populated low-lying districts)
- **Coast**: SW/W/N storm surges can raise Baltic sea level **+1.7 to +2 m** locally — Jūrmala, Engure, Salacgrīva, Ventspils

### Seismic
- Negligible (Baltic Shield craton). Same as LT.

### Forest fire
- Lower than LT (more deciduous + bog mix); inland sandy pinelands of Latgale + parts of Vidzeme have moderate exposure
- **Gap**: no national fire-risk model comparable to LT's ASIO

### Mandatory diagnostics

- **Energy Performance Certificate (Ēkas energosertifikāts)** — mandatory for sale, rental, new construction, reconstruction, renovation
  - Two types: **Temporary** (new builds / post-reconstruction → 3-year validity); **Permanent** (≥1 year occupied → 10-year validity)
  - Public registry: https://bis.gov.lv/bisp/lv/epc_documents
  - Reform: **New methodology effective 15 Aug 2025** under regulation 322436. https://likumi.lv/ta/id/322436
- **Radon**: national reference level **200 Bq/m³** (regulatory threshold). Reported household-survey readings — median ~52 Bq/m³ (~95.6% est. below the reference), with **Rauna municipality** an est. high ~352 Bq/m³ (Vidzeme uplands hot-spot) — are est. and **unverified to a named survey** (confirm against the LVĢMC / SPKC radon survey before relying on the figures). **No mandatory pre-sale radon test**
- **Asbestos**: no mandatory pre-sale survey. Soviet-era blocks common; assume risk in 1960s-80s buildings

---

## Section: `--mains`

### Cadastre + Land Book — SEPARATE INSTITUTIONS

- **Cadastre (VZD — Valsts zemes dienests)**: https://www.vzd.gov.lv/ + EN https://www.vzd.gov.lv/en
  - Public cadastre interface: https://www.kadastrs.lv/
- **Land Book (Zemesgrāmata)** — separate institution under Ministry of Justice
  - https://www.zemesgramata.lv/ + EN https://www.zemesgramata.lv/?lang=en
  - **Encumbrances live in the Land Book** — must check both
- **Spatial portal**: https://geolatvija.lv/
- **Lursoft commercial gateway**: https://www.lursoft.lv/en/land-register — paid extracts in EN

### District heating

Dominant in cities (Riga, Daugavpils, Liepāja, Jelgava). **Rīgas siltums (RS)**: https://www.rs.lv/

**EIB programme**: 4-year €135M rehabilitation of Riga DH network (€47M EIB finance). https://www.eib.org/en/projects/all/20240344

**Riga DH split**: Left bank + Vecmīlgrāvis = self-produced by RS; **Right bank (2/3 of Riga heat consumption) = bought from Latvenergo and others** — explains tariff complexity.

**2025 tariff**: After regulator review, heating tariff +11.9% from autumn 2025 (final ~€83/MWh). Original 22% increase request was reduced. https://eng.lsm.lv/article/economy/economy/28.08.2025-riga-heating-tariff-rise-will-be-less-than-initially-suggested.a612119/

**Apr 2026 audit**: State Audit Office found Riga heating could be organized "better and cheaper" — political/governance reform pressure ongoing.

### Electricity / Water
- **Latvenergo** (SOE generation + retail), **Sadales tīkls** (DSO)
- **Rīgas ūdens** (Riga); separate municipal utilities elsewhere. Rural well + septic common
- **Same BRELL exit**: Latvia synced with Continental European grid 8 Feb 2025 alongside LT and EE

---

## Section: `--crime`

See `shared/crime-sources.md`. Latvia uses:
- **Iekšlietu ministrija (MoI) — State Police**: https://www.vp.gov.lv/
- **CSP crime tables**

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
| Riga apt €/m² (standard segment) | ~€865 |
| Riga central premium | €2,900–€7,000/m² |
| Stamp duty (individual) | 1.5% of price (cap €50k) |
| Notary fee | €117–€272 |
| Total acquisition costs | ~1.7–2.2% |
| Annual NĪN (residential) | 0.2–0.6% of cadastral value (Riga) |
| EPC certificate | ~€280+ |

---

## Active fiscal incentives

- **5-year + 12-month primary residence CGT exemption**
- **10% PIT flat for rental** (registered economic activity without forming business)
- **NĪN uses frozen 2012-13 fiscal cadastral value** — much lower than current market

---

## Foreign-buyer rules

- **EU/EEA**: free to buy buildings + urban land. **Rural / agricultural / forest land**: must meet Land Law criteria — operating farm, qualified ag education, or specific use intent
- **Non-EU**: **Cannot acquire land directly**; can buy buildings, but underlying land typically requires workaround (long lease or municipality permit). Rural land needs **municipal head's consent**
- **CRITICAL — Russian/Belarusian nationals (post-2022 sanctions)**:
  - **New real estate acquisitions broadly prohibited**, with limited exceptions (existing PR holders acquiring single dwelling)
  - Existing properties retainable but disposal scrutinized
  - Cross-reference: https://www.mfa.gov.lv/en/sanctions
  - LV has explicit purchase prohibitions in force (harder than LT, which relies on residency/AML chokepoints)
- **Border-zone**: properties in border zones / national-defense areas need MoD or local authority permit. Affects Latgale (E border with RU/BY) and parts of Baltic coast
- **Investor residence permit (Golden Visa equivalent)** — **Active programme (2026)**: RE investment ≥€250,000 + 5% state-budget contribution, NOT counting agricultural/forest land. 5-year hold; annual ID-card renewal; no minimum physical presence. **~201 approvals in 2025 (up from ~149 in 2024, ≈+35% YoY — est. from PMLP figures; counts not sourced to a named PMLP statistics report)** — no 2026 suspension. Governed by **Imigrācijas likums**. Russian/Belarusian-applicant restriction the only narrowing. Verify current criteria and the exact approval counts in the PMLP statistics report: https://www.pmlp.gov.lv/ (2026-05-27 verified)

---

## Country-specific quirks

- **Compulsory land lease (`dalītais īpašums`)** — Iconic LV problem: many Soviet-era apartment blocks in Riga sit on land owned by **a different party** (often pre-1940 owner via restitution). Residents own the apartment but **pay forced ground rent** to land owner. **Reform: phased buyout law** in force since 1 Jan 2023 (2026-05-27 — verify exact statute citation at https://likumi.lv) — apartment owners can compel land purchase at cadastral price. **Verify on EVERY Riga deal.** No LT equivalent.
- **Restitution legacy**: 1990s land reform restored property to pre-1940 owners or heirs (citizens AND citizenship-eligible heirs from emigration — broader than LT). 30-year reform formally completed 2020; residual claims continue to surface, especially in Riga urban land
- **Riga Old Town (Vecrīga) UNESCO 1997**: strict heritage rules. Heritage Inspection (NKMP) approval for any external change
- **Latgale (E Latvia)**: border zone (RU + BY), Russian-speaking-majority; lower prices, but **post-2022 RU/BY buyer ban + border permit requirements** are most relevant here. Latgale rural land cheap but harder to liquidate
- **Jūrmala**: premium coastal market (Riga Beach). Wooden architecture protected. Heritage demolition controls; flood/storm surge exposure
- **Latvian banking — non-EU pain point**: Following 2018 ABLV scandal + ongoing AML enforcement, opening LV bank accounts as non-EU non-resident is **very difficult**; cross-border purchase often routed via EU bank

---

## Verification authorities

| Item | Authority | URL |
|---|---|---|
| Cadastre | VZD | https://www.vzd.gov.lv/ |
| Land Book | Zemesgrāmata | https://www.zemesgramata.lv/ |
| Tax | VID (State Revenue Service) | https://www.vid.gov.lv/en/ |
| Min of Finance | FM | https://www.fm.gov.lv/en/ |
| Min of Economics | EM | https://www.em.gov.lv/en/ |
| Flood / weather | LVĢMC | https://www.lvgmc.lv/ |
| EPC public registry | BIS | https://bis.gov.lv/bisp/lv/epc_documents |
| Migration | PMLP | https://www.pmlp.gov.lv/en |

---

## Source URL templates

| Field | Template |
|---|---|
| Cadastre lookup | https://www.kadastrs.lv/ |
| Land Book | https://www.zemesgramata.lv/?lang=en |
| HPI / RPPI | https://www.csp.gov.lv/ + https://stat.gov.lv/en |
| NĪN rules | https://www.vid.gov.lv/en/immovable-property-tax |
| EPC reform 2025 | https://likumi.lv/ta/id/322436 |
| Flood maps | https://videscentrs.lvgmc.lv/iebuvets/pludu-riska-informacijas-sistema |
| MFA sanctions | https://www.mfa.gov.lv/en/sanctions |

---

## Status

**Confidence**: HIGH on stamp-duty 1.5%/2% with €50k cap, 2025 PIT reform 25.5%/33% (VID verified), cadastre + Land Book separation, compulsory land lease quirk (academic + legal sources). MEDIUM on per-municipality NĪN rates (Riga regulation specific lookup needed), 2025 cadastral fiscal/universal split (reform recent). LOW on per-locality rental yield benchmarks. Tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

**Update history**:
- 2026-04-26: full population (Batch 3 of skill expansion)

---

## Extension TODOs

- Riga municipal NĪN brackets exact 2025 lookup
- National STR register — track EU 2024/1028 May 2026 implementation
- Compulsory-land-lease (dalītais īpašums) buyout calculator pattern
- LV/LT/EE Baltic comparison primer
