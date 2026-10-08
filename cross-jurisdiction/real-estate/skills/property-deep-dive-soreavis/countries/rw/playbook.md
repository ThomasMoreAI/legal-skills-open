# Rwanda 🇷🇼 — Property Due-Diligence Playbook

ISO2: `rw`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Population**: **13,246,394** as of August 2022 (NISR, 5th Rwanda Population and Housing Census — RPHC-5, fieldwork 16–30 Aug 2022). Tripled from 4.8 M (1978) to 13.2 M (2022). Growth rate ~2.3 %/yr. Source: NISR `https://www.statistics.gov.rw/data-sources/censuses/Population-and-Housing-Census/fifth-population-and-housing-census-2022`.
- **Capital**: **Kigali** (City of Kigali — `https://www.kigalicity.gov.rw/`). City population **1.745 M (2022 census)**, projected ~2.6 M by 2032 (NISR Subnational Projections 2023–2032). Three districts: **Nyarugenge** (CBD), **Gasabo** (largest, includes Kacyiru / Kibagabaga / Nyarutarama / Kimihurura), **Kicukiro** (south-east, includes Niboye / Kanombe / Gahanga).
- **Other markets** (much smaller): **Musanze** (Volcanoes National Park gateway, ~110k), **Rubavu** / Gisenyi (Lake Kivu, DRC border, ~150k), **Huye** / Butare (university town, ~110k), **Rusizi** / Cyangugu (Lake Kivu south).
- **Currency**: **RWF — Rwandan franc**, **managed float** (no fixed peg). Exchange rate references: BNR daily/weekly bulletin (`https://www.bnr.rw/avgexchangerate`). **8 Aug 2025**: 1 USD ≈ **1,448.54 RWF** (BNR Weekly Bulletin 11 Aug 2025). 2024 depreciation est. ~10 % vs USD (est. from BNR year-start vs year-end average rate — verify against BNR annual report); trajectory still depreciating but BNR-managed (Reserves cover ~4 months imports per IMF Article IV). **Verify spot rate at signing.**
- **Languages**: **Kinyarwanda** (universal national language), **English** (primary administrative + commercial language since 2008 switch from French), **French** (residual legal/older generation), **Swahili** (added as 4th official language 2017, used in EAC trade). Notarial deeds and the Land Registry operate in **English + Kinyarwanda**.
- **Legal system**: Civil law (Belgian/French-derived) overlaid with extensive post-2003 reforms drawing on common-law commercial practice. Property transfers governed by **Law N° 27/2021 of 10/06/2021 governing land** (replacing 2013 Land Law) + **Law N° 28/2021 of 10/06/2021 governing land use and development planning**.
- **Cadastre / land registry**: **Rwanda Land Management and Use Authority — RLMUA** (formerly RLMA — Rwanda Land Management Authority; rebranded 2021). Portal: `https://www.lands.rw/` (the former RLMA `rlma.rw` portal is defunct — superseded by RLMUA's lands.rw). Rwanda completed **systematic Land Tenure Regularisation (LTR) 2009–2013** under MINIRENA / DAI / DFID, demarcating **>10.4 M parcels** and issuing **8.8 M titles**. **Titling rate ~93 % (gender-equal)** — Rwanda is one of very few African countries with near-universal parcel-level digital cadastre. Land Administration Information System (LAIS, ESRI ArcGIS-based, version 4.0) operational; e-titles paperless from 2024.
- **Postcode**: Rwanda **does not have a national postal code system** — addresses are by Cell / Sector / District / Province + landmark. RDB / RRA correspondence uses PO Boxes.
- **Admin levels**: **5 provinces** (Kigali City + Eastern + Northern + Southern + Western) → **30 districts** → **416 sectors** → **2,148 cells** → **14,837 villages (umudugudu)** [NISR 2022 administrative inventory]. Each district has its own council that sets land-tax rates within RRA-prescribed bands.
- **EAC / regional**: Rwanda is a member of **EAC (East African Community)**, **COMESA**, **CEPGL** (with DRC + Burundi). EAC + COMESA citizens get reduced investor thresholds (USD 100k vs USD 250k for OECD nationals).

### Major reforms tracked (2022–2026)

- **Law N° 27/2021 (Land Law)** — extended **emphyteutic / leasehold term to 99 years** for both residential and investment use (previously 49 years for investment, 20 years for residential). Foreigners get **leasehold only**; freehold reserved for Rwandan citizens (subject to international convention reciprocity). Source: Official Gazette + RLMUA.
- **Law N° 027/2022 of 20/10/2022 establishing taxes on income** (amended by **Law N° 051/2023 of 05/09/2023** and **Law N° 014/2025 of 27/05/2025**) — replaced 2018 Income Tax Law; restructured PIT brackets (see `--tax`); **CGT 10 %** (Art. 36 as amended by Law N° 014/2025, Official Gazette n° Special of 29/05/2025 — Art. 36 as promulgated read 5 %, which was the statute for 20/10/2022 – 28/05/2025) on the **Art. 37 base of shares, licences, debt instruments, options, guarantees and similar assets — immovable property is NOT in the CGT base**; commercial-property gains fall into business profit (Art. 19) at **CIT 28 %** (Art. 48 as amended by Law N° 051/2023) or PIT progressive to 30 %; residential individual sales captured through the 2 % / 2.5 % sale levy (see `--tax`); preserved **rental income tax** progressive scale. *(2026-08-07 verified, source Law 014/2025 + Law 027/2022 + Law 051/2023 gazettes + RRA Tax Handbook + PwC Worldwide Tax Summaries)*
- **Law N° 006/2021 of 05/02/2021 on investment promotion and facilitation** (Investment Code 2021) — replaced 2015 Code; preferential CIT rates 3 / 15 / 25 %; **3 foreign-worker permits + residence permit for USD 250k+ registered investor**. Source: UNCTAD Investment Laws Navigator + RDB.
- **Property Tax Reform — Cabinet-approved 20 April 2023; enacted as Law N° 048/2023 of 05/09/2023 (repeals Law N° 75/2018), in force on gazettement 14 Sept 2023 per Art. 60 (Official Gazette n° Special of 14/09/2023)** — land-rate implementing instrument **Ministerial Order n° 002/23/10/TC of 24/11/2023**; first tax period under the new rates = **calendar 2024**, RRA opened the 2024 declaration **20 August 2024** after District Council + City of Kigali rate approval, **annual deadline 31 December**. Land Tax rate compressed from FRW 0–300/m² to **FRW 0–80/m²** band (varies by district + use, set annually by District Council / City of Kigali); **Building Tax**: 0.5 % residential / 0.3 % commercial / 0.1 % industrial-SME of combined building + plot market value, with **0.25 %** for a residential plot + building of **three floors** and **0.1 %** **above three floors**; **one owner-occupied family dwelling exempt** (its land remains taxable); **Sale levy**: 2 % registered seller / 2.5 % unregistered, levied on the sale value **after deducting the first FRW 5,000,000** — use-based applicability of the deduction is not specified in the source; verify residential treatment with RRA. Source: Law N° 048/2023 (Law on Sources of Revenue for Decentralized Entities) `https://www.rra.gov.rw/fileadmin/user_upload/Law_of_2023_about_the_sources_of_Revenues_and_property_for_decentralized_entitied.pdf` + gov.rw Cabinet press release 20 Apr 2023 + RRA 2024 declaration notice *(rates re-confirmed unchanged 2026-08-07 against RRA Basic Information version 2025 + RRA Tax Handbook 2025; no amending law — the May-2025 package did not touch Law 048/2023)*
- **Law N° 015/2025 of 27 May 2025 — 3 % Tourism Levy (effective 1 July 2025)** — unanimous Parliament vote 28 Apr 2025; 3 % tax on accommodation (Art. 2: "a service which consists of providing a room or place to sleep or rest" — hotels, motels, lodges, guest houses, **apartments and similar**), charged on the amount paid or payable **exclusive of VAT** (Art. 3); declared + paid within 15 days of month-end. Materially affects short-let / serviced-apartment yields *(2026-05-27 verified, source Law 015/2025 + allAfrica + travelnews.africa)*
- **e-Apostille launch (5 June 2024)** — MINAFFET + Irembo partnership; Rwanda became 126th HCCH Apostille Convention member (instrument of accession deposited 6 Oct 2023; entered into force 5 June 2024); first country to launch e-Apostille from day-one of accession; 1–3 day processing via `https://irembo.gov.rw/`. Material for foreign-buyer document chain (birth certificates, PoA, marriage certificates required for LAIS / RDB filings) *(2026-05-27 verified, source MINAFFET press release + Schmidt-Export accession tracker)*
- **Kigali Master Plan 2050 (KMP 2050)** — adopted 2020; portal: `https://bpmis.gov.rw/asset_uplds/kigali_master_plan/` and `https://www.kigalicity.gov.rw/`. Reduced commercial zones from 9 → 3, residential zones from 7 → 5; introduced overlay districts encouraging mixed-use along future BRT corridors. **Strict enforcement** — building permits checked against KMP 2050 zoning.
- **Electronic Land Title rollout (2024)** — all titles paperless via LAIS; physical printout fee FRW 5,000 abolished by default (charged only for special-print requests).

---

## Foreign buyer eligibility (READ FIRST)

Rwanda is **broadly permissive** for foreign property buyers in **leasehold**, but freehold is constitutionally restricted. The framework is unusually transparent for sub-Saharan Africa thanks to RLMUA's digital cadastre.

### What foreigners can and cannot buy

| Asset | Foreigner-buyable? | Notes |
|---|---|---|
| **Urban titled apartment / villa (Kigali)** | ✅ YES (leasehold 99 years) | Default safe — Nyarutarama, Kacyiru, Kimihurura, Kibagabaga, Gacuriro, Kiyovu. Confirm title via LAIS / RLMUA. |
| **Off-plan / new-build apartment in Kigali** | ✅ YES (with care) | Most reputable developers (e.g., Vision City, Kigali Heights) operate on certified leaseholds. Verify developer's Class A/B/C licence + construction permit + KMP 2050 zoning compliance. |
| **Lake Kivu / Rubavu / Karongi tourist property** | ✅ YES (leasehold) | Verify zoning (Lake Kivu has shoreline-protection bands); pollution risk monitored due to methane in Lake Kivu deeps. |
| **Volcanoes National Park gateway (Musanze) tourism property** | ✅ YES (leasehold) | Strict zoning around park buffer; volcanic risk material (see `--risks`). |
| **Agricultural / rural land outside urban plans** | ⚠️ CAUTION | Allowed via long-term lease, but rural Rwanda is **densely cultivated subsistence land**; consolidation / villagisation programmes can affect tenure. Verify with RLMUA + district authority. |
| **Freehold title (any asset)** | ❌ NO (foreigners) | Reserved for Rwandan citizens under **Constitution Article 29 (private property right)** + Land Law 2021. Only path: **bilateral reciprocity convention**. |
| **Marshlands, protected wetlands** | ❌ NO | Inalienable public domain (Land Law 2021 + REMA — Rwanda Environment Management Authority). |
| **Volcanoes / Akagera / Nyungwe National Park interiors** | ❌ NO | Protected; managed by RDB Tourism + RWCA (Rwanda Wildlife Conservation Authority). |

### Mandatory pre-purchase verification (foreigner)

1. **TIN** (Tax Identification Number) — foreigner obtains from RRA via `https://www.rra.gov.rw/` or RDB One-Stop Centre. Free.
2. **LAIS title check** — confirm seller is registered titleholder; verify leasehold term remaining; check for mortgage / caveat. RLMUA `https://www.lands.rw/`. Title certificate: **Certificate of Registration** (UPI = Unique Parcel Identifier).
3. **Land use plan check** — verify parcel's zoning under KMP 2050 (Kigali) or relevant district master plan. Portal: `https://bpmis.gov.rw/`.
4. **Sale and Purchase Agreement (notarised)** — registered with RLMUA within 30 days of signing.
5. **Land Sub-lease deed** (for foreigners) — registered against UPI; confirms 99-year emphyteutic lease.
6. **Building permit + Occupancy Certificate** (Habitable certificate) — issued by **City of Kigali / district** under KMP 2050 (Kigali Building Permit Management Information System — BPMIS, `https://bpmis.gov.rw/`).
7. **Tax clearance from RRA** — confirms no outstanding immovable property tax / rental income tax.
8. **AML / KYC**: BNR-supervised commercial banks must verify source of funds for transfers > **USD 10,000**.

### Currency / repatriation framework

- **No legal restrictions** on capital transfers in or out of Rwanda (US State Dept 2025 Investment Climate Statement, citing BNR + Investment Code 2021 Art. 19).
- **Authorised commercial banks only**: routine transfers via BCR, BK (Bank of Kigali), Equity Bank Rwanda, I&M Bank, Cogebanque, Access Bank, KCB Rwanda, Ecobank Rwanda.
- **Notification rule**: BNR notified of all individual transfers > **USD 10,000** (AML).
- **Repatriation right**: investors registered under Investment Code 2021 may repatriate capital, profits, dividends, debt service. Rental income from non-resident-owned property repatriable through bank channels after RRA tax clearance.
- **Keep forever**: bank-issued **declaration of foreign exchange entry** referencing the property purchase — basis for repatriation right at resale.
- **RWF is managed-float, not pegged**: budget for ~5–10 %/yr depreciation vs USD/EUR over recent years; verify spot rate at each transaction.

### Confidence

**HIGH** for the foreign-buyer leasehold framework, RLMUA digital cadastre, and Investment Code 2021 thresholds (multi-source: government law text + UNCTAD + US State Dept). **HIGH** for tax rates (RRA primary publication). **MEDIUM** for property-sale price benchmarks (no published RPPI; aggregated from listings + secondary press). **MEDIUM** for rural/peri-urban tenure transitions (consolidation programmes evolving district by district).

---

## Section: `--price`

### Primary sources

- **NISR — National Institute of Statistics of Rwanda** — `https://www.statistics.gov.rw/` — Construction Statistics, Establishment Census, GDP. **Does NOT publish a residential property price index** comparable to PT Confidencial Imobiliário or FR Notaires; Rwanda has no official RPPI.
- **BNR — National Bank of Rwanda — Financial Stability Reports + Monetary Policy Reports** — `https://www.bnr.rw/` — credit-to-real-estate aggregates, mortgage market depth.
- **RDB — Rwanda Development Board** — `https://rdb.rw/` — real-estate sector reports + investor briefs.
- **RLMUA — LAIS** — sale-deed registrations are paid per-search; not in open data.
- **RRA Immovable Property Tax matrix values** — fiscal-base values are valuation-roll-derived; typically **30–50 % below market** (use as floor only).

### Listing platforms (Kigali + national)

- **House in Rwanda** — `https://www.houseinrwanda.com/` — large national listing site
- **Rwandan Houses** — `https://rwandanhouses.com/` — agency network
- **Plut Properties** — `https://plutproperties.com/` — agency, residential + commercial
- **Kwanda Real Estate** — `https://kwandarealestate.com/` — foreign-investor-oriented platform
- **Kigali Inspectify** — `https://kigaliinspectify.com/` — inspection + listing
- **Property24 Rwanda** — `https://www.property24.co.rw/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Rwanda portal (Property24 is South Africa-only) — regional Property24 instance
- **Real Estate in Rwanda (REIR)** — `https://reir.rw/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with REIR association appears defunct — use RDB (rdb.rw) / RLMUA (lands.rw) for primary data — sector association

### Indicative price bands (2024–2025, Kigali — listing aggregation, est.)

> ⚠️ Rwanda has **no official RPPI**. Below is **est.** range from listing aggregation; transaction prices not systematically published. Assume listing/transaction gap 5–15 %. **Verify against LAIS sale records (paid per UPI search) or RDB sector reports.**

| Locality | Property type | Listing USD/m² (est., 2024–2025) | Notes |
|---|---|---:|---|
| **Nyarutarama, Kacyiru, Kimihurura** (premium Gasabo) | Luxury villa (leasehold) | ~$1,500–$2,500 | Diplomat / expat / NGO market; gated estates |
| **Nyarutarama, Kacyiru** | Premium apartment | ~$1,200–$2,000 | La Rubibi, Touch Africa, Vision City units; RWF 450M–600M = ~USD 310k–415k for 2-3BR (Kwanda 2024, ~RWF 1,448 / USD) |
| **Kibagabaga, Gacuriro, Gisozi** | Mid-market villa / townhouse | ~$700–$1,300 | Local-buyer-heavy; growing expat overflow |
| **Kiyovu, Nyarugenge CBD** | Older villa / converted residence | ~$900–$1,800 | Diplomatic enclave heritage; older stock |
| **Kicukiro, Niboye, Kanombe** (south Kicukiro, near airport) | Mid-range villa | ~$500–$1,000 | Suburban; growth zone post-airport relocation tracker |
| **Bumbogo, Kinyinya, Gatsata** (peri-urban Gasabo / Nyarugenge) | Affordable house / plot | ~$200–$600 | Local-buyer market; infrastructure expanding |
| **Musanze** (Volcanoes NP gateway) | Tourism-oriented house / lodge | ~$400–$900 | Gorilla-trekking-driven; high seasonality |
| **Rubavu / Gisenyi** (Lake Kivu) | Lake-view villa | ~$500–$1,200 | Tourism + DRC trade adjacency |
| **Huye / Butare** | University-town residence | ~$200–$500 | Modest market |

(Listing-derived ranges, Kwanda Real Estate / House in Rwanda / REIR aggregations, 2024–2025; **rates may have changed since** — verify on portal.)

### Indicative apartment-sale price points (Kigali, 2024)

- **1-bedroom apartment, mid-tier** (Kibagabaga / Gacuriro): from **~USD 70,000** (House in Rwanda 2024 listing aggregations).
- **2–3-bedroom apartment, mid-tier** (Kibagabaga / Gacuriro): from **~USD 100,000+**.
- **2–3-bedroom premium apartment** (Nyarutarama / Kacyiru — La Rubibi, Touch Africa): **RWF 450 M – 600 M (~USD 310k–415k at FRW 1,448/USD Aug 2025).**

### Compute

1. Listing USD/m² = (Listing price in USD) / (advertised m² built area). **Note**: Rwandan listings often quote **plot size + built area separately** in m² or sometimes ares (1 are = 100 m²). Confirm which figure you're dividing by.
2. Cross-check with seller's **Certificate of Registration** (UPI) for legal area.
3. For accurate transacted price: paid LAIS search per UPI via RLMUA.
4. **Trap**: listing prices for foreigners are sometimes 10–20 % higher than equivalent local-buyer transaction. Anecdotal but reported across multiple agency sources; best counter is hire local conveyancing lawyer and request RRA matrix value for benchmarking.
5. **Trap**: leasehold remaining term materially affects value. A 20-year-remaining 99-yr leasehold ≠ a fresh 99-yr leasehold. Verify start date on Certificate of Registration.

### Confidence

**MEDIUM** — no official RPPI; ranges are listing-derived from foreign-buyer-oriented portals; asymmetric price discovery typical.

---

## Section: `--traffic`

### Primary sources

- **RTDA — Rwanda Transport Development Agency** — `https://www.rtda.gov.rw/` — national road inventory, asphalt programmes; some traffic counts in annual reports (irregular publication; not parcel-level).
- **City of Kigali Transport Master Plan** — `https://www.kigalicity.gov.rw/` + KMP 2050 transport overlay (BRT corridors planned).
- **RURA — Rwanda Utilities Regulatory Authority** — public transport regulation: `https://rura.rw/`.
- **OSM** — Rwanda has **good OSM coverage** in Kigali (since the YouthMappers / Missing Maps work), thinner in rural areas. Use `highway` tag for class.

### Coarse fallback (OSM `highway` → vehicles/day est.)

- `motorway` = expressway (very limited in Rwanda; e.g., Kigali–Nyamata expressway under expansion) — **not a parcel-level concern in 2025**
- `trunk` = National Route NR (e.g., NR1 Kigali–Rusumo, NR3 Kigali–Musanze, NR4 Kigali–Cyanika) — est. **5,000–25,000 v/d** core sections
- `primary` = District / urban arterial (e.g., KG 9 Avenue, KN 5 Road) — est. **3,000–15,000 v/d** Kigali core
- `secondary` = collector — est. **1,000–5,000 v/d**
- `tertiary` = local connector — est. **300–2,000 v/d**
- `residential` = quiet street — est. **<500 v/d**

### Verdict bands

- 🟢 < 500 v/d (interior residential street)
- 🟡 500–3,000 v/d (urban side street, suburban arterial)
- 🟠 3,000–10,000 v/d (busy arterial, NR-class)
- 🔴 > 10,000 v/d (NR1 / NR3 core sections, urban CBD arterials)

**Caveat**: Rwanda does not publish open AADT counts at a parcel-level scale; bands are **OSM-class-derived estimates**, not measured. For decision-grade noise/traffic assessment, request from RTDA directly OR commission a 24-hour count.

**Kigali-specific note**: motorbike taxis (**moto-taxis** or "moto") dominate urban transport. They are heavy nightly users of arterials; expect higher noise floor near "moto stages" (informal pickup points). Visit at peak hours (07:00–08:30, 17:00–19:00) before signing.

---

## Section: `--tax`

### Stamp / transfer levy (one-time, buyer or per agreement)

- **Levy on sale of immovable property**: **2 %** of sale value (registered seller) / **2.5 %** (unregistered), levied **after deducting the first FRW 5,000,000** of the sale value — legal basis **Law N° 048/2023 of 05/09/2023**, in force on gazettement 14 Sept 2023 (Official Gazette n° Special of 14/09/2023); collected by RRA at registration. Use-based applicability of the FRW 5 M deduction is not specified in the source — verify residential treatment with RRA. Source: Law N° 048/2023 `https://www.rra.gov.rw/fileadmin/user_upload/Law_of_2023_about_the_sources_of_Revenues_and_property_for_decentralized_entitied.pdf` + RRA (prior secondary reporting: Kigali Times Finance Law 2024/2025) *(2026-08-07 verified)*

### Land Registration / RLMUA fees

- **Land transfer fee**: **FRW 20,000** residential / **FRW 30,000** commercial (RLMUA flat).
- **Land registration fee** (post-transfer): **0.5 %** of declared property value.
- **Title deed printout (electronic system 2024+)**: free by default; FRW 5,000 for special-print copy.
- **Notary fees**: regulated scale, typically **0.5–1 %** of sale value (anecdotal range; flat-rate component FRW 1,000–5,000 for simple deeds).
- Source: RLMUA `https://www.lands.rw/land-transactions` (One Step One Day Transfer page).

### Annual Immovable Property Tax (IPT) — RRA

**Source**: RRA Immovable Property Tax page `https://www.rra.gov.rw/index.php?id=64&L=27` + reform-package PDF `https://www.rra.gov.rw/fileadmin/user_upload/WEB_POPERTY_TAX__EN_Ok.pdf`.

**Reform — Law N° 048/2023 of 05/09/2023** (repeals Law N° 75/2018), in force on gazettement **14 Sept 2023** per Art. 60 (Official Gazette n° Special of 14/09/2023). Land rates are set by **Ministerial Order n° 002/23/10/TC of 24/11/2023**. First tax period under the new rates = **calendar 2024**; RRA opened the 2024 declaration **20 Aug 2024** after District Council + City of Kigali rate approval; **annual deadline 31 December**.

Rates in force:

#### Land Tax

- Range: **FRW 0–80/m²** (compressed from previous FRW 0–300/m²).
- Set annually by **District Council / City of Kigali** based on location + use.
- Cap: **FRW 80/m²**.

#### Building Tax (residential / commercial / industrial)

| Use | Rate (% of market value of building + plot) |
|---|---:|
| **Residential** | **0.5 %** |
| **Commercial** | **0.3 %** |
| **Industrial / micro & small business** | **0.1 %** |
| **Residential plot + building of three floors** | **0.25 %** |
| **Residential plot + building above three floors** | **0.1 %** |

Second residential house: **0.5 %** of combined market value.

#### Worked example — Kigali residential apartment, market value ~USD 200,000 (~FRW 290 M at FRW 1,448/USD)

- Building Tax: 0.5 % × FRW 290 M = **~FRW 1,450,000/yr (~USD 1,000/yr)**
- Land Tax: ~80 m² × FRW 80/m² = **FRW 6,400/yr (~USD 4/yr)**
- **Total annual IPT**: ~FRW 1,456,400 (~USD 1,005)

⚠️ This example applies the flat **0.5 %** residential rate. Law N° 048/2023 also sets **0.25 %** for a residential plot + building of **three floors** and **0.1 %** **above three floors** — the floor count of this apartment block is not stated, so if the building falls in either band the figure above is an over-estimate. Confirm the applicable band with RRA / the district council before relying on it.

**One owner-occupied family dwelling is exempt from Building Tax** (Law N° 048/2023) — **its land remains taxable** (Land Tax still due). Confirm your dwelling qualifies, and the applicable land rate, with the district council annually.

#### Transfer + Registration costs (one-time, buyer side, USD 200k purchase)

| Item | RWF | USD est. |
|---|---:|---:|
| Sale levy 2 % (registered; on RWF 290 M − RWF 5 M = RWF 285 M; the FRW 5 M deduction applies to the sale value, use-based applicability not specified in the source — verify residential treatment with RRA) | ~5,700,000 | ~$3,940 |
| Land registration 0.5 % | ~1,450,000 | ~$1,000 |
| Land transfer fee (residential flat) | 20,000 | ~$15 |
| Notary fees ~0.75 % (mid-range est.) | ~2,175,000 | ~$1,500 |
| Title printout / misc. | 5,000 | ~$4 |
| **Total transaction cost** | ~9,450,000 | **~$6,500 (~3.3 % of price)** |

(Law N° 048/2023 basis, first tax period calendar 2024; rates re-confirmed unchanged **2026-08-07** against RRA Basic Information version 2025 + RRA Tax Handbook 2025 — still verify current rates at RRA/RLMUA on day of transaction.)

### Capital Gains Tax (CGT)

- **CGT base** (Art. 37 of Law N° 027/2022, as amended): direct or indirect sale or transfer of **shares, licences, debt instruments, options, guarantees and similar assets**. **Immovable property is NOT in the CGT base.**
- **Rate**: **10 %** of the capital gain (acquisition value vs selling / transfer price). Legal basis: **Law N° 014/2025 of 27/05/2025** (Official Gazette n° Special of 29/05/2025, in force from gazettement) amending **Art. 36 of Law N° 027/2022** — "The capital gain tax rate is 10% of the capital gain". Art. 36 as promulgated read **five percent (5 %)**, so **5 % was the primary statute for 20/10/2022 – 28/05/2025**. Source: Law 014/2025 + Law 027/2022 gazettes + RRA Tax Handbook + PwC Worldwide Tax Summaries 2026.
- **Commercial immovable property**: **not CGT at all** — the gain falls into **business profit** (Art. 19 of Law N° 027/2022, "proceeds of sale of any business asset"), taxed at **CIT 28 %** (Art. 48 as amended by **Law N° 051/2023 of 05/09/2023**, which cut CIT 30 % → 28 %) or at **PIT progressive to 30 %** (Art. 14 top band), depending on the seller. There is **no 30 % CGT on commercial immovable property** — the earlier framing here was wrong.
- **Residential immovable property** (individual seller, non-business): **NOT a separate CGT** — gain is captured through the immovable-property sale levy (2 % registered / 2.5 % unregistered above the RWF 5 M exempt floor; see Transfer + Registration costs above). Verify your specific scenario with RRA — the residential-vs-commercial classification is fact-driven.
- **Declaration deadline**: 15th of the month following the transaction.
- Source: RRA Tax Handbook `https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdfhandbook/explanation-of-capital-gains-tax/` + PwC Rwanda Corporate Tax Summary 2026 `https://taxsummaries.pwc.com/rwanda/corporate/other-taxes` *(2026-08-07 re-verified — this corrects the note previously carried here: the "5 % flat" framing was **not** a pre-2022 confusion. Art. 36 of Law N° 027/2022 as promulgated read five percent (5 %), and Law N° 051/2023 amended only Arts. 9 + 48 (CIT 30 % → 28 %) without touching CGT, so 5 % was the primary statute for 20/10/2022 – 28/05/2025; the 10 % rate arrives only with Law N° 014/2025 of 27/05/2025)*

### Rental Income Tax (RIT) — for landlords

**Source**: RRA `https://www.rra.gov.rw/fileadmin/img/rental-income-tax.html` + Law 027/2022.

| Annual rental income (RWF) | Rate |
|---|---:|
| 1 – 180,000 | **0 %** |
| 180,001 – 1,000,000 | **20 %** |
| > 1,000,000 | **30 %** |

- **Taxable base**: Gross rental income − **50 % flat deduction** for maintenance + bank-loan interest deduction (loans for the rented property).
- Deadline: **31 January** following the income year.
- Penalty: **40 %** of tax due for late declaration / false information.
- Note: this is the **simple rental income tax** (regime for individuals not subject to CIT). If the landlord is a corporate entity or VAT-registered trader operating commercial lodging, **CIT 28 % + VAT 18 %** apply via standard regime. *(CIT 28 % per Art. 48 of Law N° 027/2022 as amended by Law N° 051/2023 of 05/09/2023 — the former 30 % is stale; 2026-08-07 verified)*

### Personal Income Tax (PIT) — context for resident earners

**Source**: Law N° 027/2022 of 20/10/2022.

PIT brackets (monthly employment income, post-Nov 2023):

| Monthly income (RWF) | Rate |
|---|---:|
| 0 – 60,000 | **0 %** |
| 60,001 – 100,000 | **10 %** |
| 100,001 – 200,000 | **20 %** |
| > 200,000 | **30 %** |

(2023 transition table — verify current brackets at RRA each year; rates may have changed since post-Nov 2023 release.)

### VAT

- **18 %** standard rate (one of the highest in EAC).
- New residential builds by VAT-registered developers: VAT applies on first sale; resale by individuals exempt.
- Source: RRA + PwC Tax Summaries Rwanda.

### Future risk

- **Property tax reform 2024 still bedding in** — district councils setting per-locality rates; some Kigali districts pushing toward upper end of building tax band.
- **Rental income reporting compliance push** — RRA actively cross-checking AirBnB / hospitality registrations against rental tax filings (verify status 2026 at RRA news).
- **Sale levy** — distinguishing 2 % vs 2.5 % depends on TIN registration status; foreigners typically pay 2 % once TIN issued.

⚠️ **Verification**: request seller's last RRA Immovable Property Tax + Rental Income Tax clearance certificates before signing.

---

## Section: `--rental`

### Long-term residential rentals

**Governing law**:
- Law N° 30/2018 of 02/06/2018 governing tenancy and tenants of residential premises (and amendments).
- Common-law-influenced lease principles; written contracts strongly recommended (RDB / RRA recommend registration of leases > 1 year).

**Key obligations**:
- Written lease standard for any term > 6 months.
- **Deposit**: typically **1–3 months' rent**, returnable at end of lease (less damages); no statutory escrow rules — hold via lawyer or escrow agent for safety.
- **Notice**: typically 1–3 months, per contract; 60 days standard for monthly tenancies.
- Eviction: court order required; commercial court (Kigali) handles disputes; relatively fast (<6 months typical).
- **Inspection**: joint at move-in / move-out best practice.

### Tax treatment (long-term let)

- Reported on **annual Rental Income Tax declaration** (deadline 31 Jan); see `--tax` for brackets.
- Deductible: **50 % flat** for maintenance + bank-loan interest on the rented property.
- Top marginal bracket: **30 %** above FRW 1 M annual.

### Short-term rentals (Airbnb / serviced apartments)

**Status**: legal but increasingly regulated.

- **RDB tourism licensing**: short-term rental as a commercial accommodation operator requires a **tourism business operating licence** issued via RDB (`https://rdb.rw/`); applies to rentals offered as hospitality service (not casual single-property landlords with long-term tenants).
- **Local district council registration**: required in Kigali; check City of Kigali Business Permit office at sector level.
- **Tax treatment**: if income > FRW 12 M/yr (~USD 8,300) AND the activity is "commercial accommodation provision," **CIT or PIT under business income rules** may apply (rather than Rental Income Tax) — consult RRA Tax Handbook before entering.
- **VAT**: registration mandatory for hospitality turnover ≥ **FRW 20 M/yr** (~USD 13,800).
- **Tourism Levy 3 %** (effective **1 July 2025** per **Law N° 015/2025 of 27 May 2025**): 3 % of the amount paid or payable for accommodation, **exclusive of VAT** (Law 015/2025 Art. 3), on hotels, motels, lodges, guest houses, **apartments and similar services**; declare + pay within 15 days of month-end. Net occupancy economics: a USD 100/night Airbnb listing now remits ~USD 3/night tourism levy + standard 18 % VAT (if registered) + business income tax — model net before underwriting short-let yield *(2026-05-27 verified, source Law 015/2025 + Parliament plenary 28 Apr 2025 + travelnews.africa)*
- Body Corporate / building rules: many Kigali condominium developments **prohibit short-term lets** in their by-laws — verify before purchase.

### Strategic notes

- **Kigali short-let demand**: business travel + diplomatic + NGO + Mountain Gorilla / Nyungwe tourist routing → robust occupancy in Kacyiru, Kimihurura, Nyarutarama, near Convention Centre.
- **Musanze**: gorilla-trekking peak (Jun–Sep, Dec–Jan); off-peak occupancy weak.
- **Rubavu**: domestic-tourism + DRC traders; weekly rhythms.
- **Yields**: 6–10 % gross typical Kigali (mid-market apartment); 4–7 % luxury Nyarutarama (price ceiling); 8–12 % gross peri-urban / mid-tier — **est., listing-derived**, not transaction-verified.
- **Currency hedge**: foreign owners often demand rent in USD; tenants pay USD-equivalent at month-of-payment FX (RWF depreciation risk borne by tenant if so structured) — verify legal enforceability with local lawyer.

---

## Section: `--work=<profession>`

### Job platforms

- **JobinRwanda** — `https://www.jobinrwanda.com/` (largest)
- **MyJobMag Rwanda** — `https://www.myjobmag.co.rw/` ❌ DEPRECATED — dead on 2026-09-18; verify with the authority named in this row
- **LinkedIn Rwanda** — strong in NGO, finance, tech, hospitality
- **Indeed Rwanda** — limited but growing
- **RDB job board** — `https://rdb.rw/careers/` (RDB-internal only)
- **UN, World Bank, IMF, AfDB** — Kigali hosts substantial multilateral presence
- **Foreign Embassies / Consulates** — diplomatic corps

### Self-employment / business structures

- **Sole proprietor**: simplest; PIT at progressive rates; no liability shield.
- **Limited liability company (Ltd)**: registered at **RDB Office of the Registrar General** via `https://org.rdb.rw/`; CIT **28 %** standard (Art. 48 of Law N° 027/2022 as amended by Law N° 051/2023 of 05/09/2023 — the former 30 % is stale) / 15–25 % preferential rates per Investment Code 2021 (export, energy, holding co's).
- **Investment certificate**: USD 250k+ investor → 3 work permits + residence permit + tax incentives via Investment Code 2021.
- **Tax registration**: TIN automatic with company registration; VAT registration if turnover ≥ FRW 20 M/yr.
- **Social security**: **RSSB** (Rwanda Social Security Board) — pension + medical insurance; combined ~13–17 % (est.) depending on employee/employer split — verify current statutory split against RSSB published contribution schedule.

### Foreign worker visas — Directorate General of Immigration & Emigration (DGIE)

**Source**: `https://www.migration.gov.rw/our-services/business-investor` + Business Procedures portal `https://businessprocedures.rdb.rw/menu/62?l=en`.

**Visa class structure** (Temporary Resident Permits):

| Class | Category |
|---|---|
| A | Mining / mineral sector — Investor / Entrepreneur |
| B | Agriculture & animal husbandry — Investor / Entrepreneur |
| C | Prescribed Professionals (incl. religious, artistic) |
| D | Diplomats |
| E | Government / Parastatal employee |
| F | Manufacturing & Processing — Investor / Entrepreneur |
| **G** | **Trade, Business & Services — EAC/CEPGL or Outside EAC/CEPGL** |
| H | Employment by employer (skilled / semi-skilled / journalists / org staff) |
| I | Religious activities |
| J | Hospitality industry — Investor / Entrepreneur |
| **K** | **Person with Assured Income (retiree-style)** |
| M | Dependent pass (family of permit holder) |
| N | Student / Trainee |
| P | Voluntary worker / Holiday worker |
| W | IT & related — Investor / Entrepreneur |
| X | Transport & logistics — Investor / Entrepreneur |
| Z | Other Investments — Investor / Entrepreneur |

**Permit fees (RDB Business Procedures Portal)**:
- New applicant (1-tier): **FRW 150,000** — validity up to **2 years**.
- Recurring applicant (3+ tier): **FRW 250,000** — validity up to **5 years**.

**Investor incentive (Law N° 006/2021 Art. 14)**:
- Registered investor with USD 250,000+ investment certificate → **residence permit + 3 foreign-worker permits without labour-market test**.
- Investors from **EAC / COMESA member states**: reduced threshold to **USD 100,000**.

**Mackrell International Golden Visa overview** + **IMI Daily** + **Kwanda RE summaries** mention a **USD 500,000 luxury property route** + **USD 250,000 RDB investor route** — **note: the USD 500k "luxury property" path is sometimes described as the practical residence-by-investment route but is NOT a clearly published primary-source RDB programme; verify directly with RDB One-Stop Centre** (`https://rdb.rw/one-stop-centre/`) before relying on it for a specific transaction. The **USD 250k registered-investor + 3-permit-grant route under Law N° 006/2021** is the primary-source-confirmed path.

### Salary benchmarks (2024–2025 Kigali, gross monthly RWF — listing/recruiter-aggregated, est.)

- Junior professional (entry, NGO/private sector): **FRW 400k–800k** (~USD 280–550)
- Mid-level (5+ yrs, urban): **FRW 1.0M–2.5M** (~USD 700–1,700)
- Senior / management: **FRW 2.5M–6.0M+** (~USD 1,700–4,100+)
- Skilled trades: **FRW 250k–800k**
- (NISR Labour Force Survey `https://www.statistics.gov.rw/` — releases biannual; absolute figures NOT systematically published per skill class; ranges above are aggregator estimates.)

⚠️ **Caveat**: Rwanda has no published wage statistics at the granularity of EU LFS; salary bands are recruiter-aggregator estimates.

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **MIDIMAR / MINEMA** (Ministry in Charge of Emergency Management) | `https://www.minema.gov.rw/` | National disaster risk reduction; flood / landslide / drought |
| **REMA — Rwanda Environment Management Authority** | `https://www.rema.gov.rw/` | Wetlands, marshlands, EIA, pollution registry |
| **MINIRENA / Ministry of Environment** | `https://www.environment.gov.rw/` | Climate / forestry / land |
| **Meteo Rwanda — Rwanda Meteorology Agency** | `https://www.meteorwanda.gov.rw/` | Climate / weather / drought |
| **RWCA — Rwanda Wildlife Conservation Authority / RDB Tourism** | `https://rdb.rw/investment-opportunities/invest-in-tourism/` | National Park boundaries; buffer zones |
| **RBC — Rwanda Biomedical Centre** | `https://www.rbc.gov.rw/` | Disease vectors (malaria; cholera in border zones) |
| **U.S. Geological Survey + Smithsonian Global Volcanism Programme** | `https://volcano.si.edu/` | Nyiragongo / Nyamuragira monitoring (Virunga, DRC side) |
| **Goma Volcano Observatory (OVG, DRC) + IGN-FI / SAVCO regional monitoring** | (DRC primary) | Real-time Virunga seismicity data |

### Region-specific recurring hazards

| Region | Hazard | Notes |
|---|---|---|
| **Rubavu / Gisenyi (NW border)** | **Volcanic + seismic — Nyiragongo (DRC, 20 km NW of Goma)** | **2021 Nyiragongo eruption** (22 May 2021) sent lava toward Goma; tremors felt in Gisenyi + as far as Kigali (90 km); ~8,000 Goma residents fled into Rwanda. **2002 eruption** more catastrophic — 450k temporary refuge in Rubavu/Musanze. **Active** — extreme-risk monitoring continuous. Properties on Rubavu lakefront NW also exposed to Lake Kivu methane risk (limnic eruption potential in deep waters). |
| **Musanze district + Volcanoes National Park gateway** | **Volcanic + seismic + landslide** | Within ~25 km of Karisimbi / Bisoke / Sabyinyo / Muhabura volcanoes (currently dormant); regional seismicity rift-related. Steep slopes → landslides during heavy rain (Mar–May, Oct–Dec). |
| **Northern Province (Burera / Gicumbi / Musanze)** | **Landslides** | Steep terraced terrain; episodic landslide casualties in heavy-rain seasons. MINEMA tracks. |
| **Western Province (Karongi / Rusizi / Rutsiro)** | **Lake Kivu methane + landslide + flood** | Lake Kivu has dissolved CH4 + CO2 → low (but real) limnic-eruption risk; methane extraction projects (KivuWatt) cap risk. Steep western slopes prone to landslide. |
| **Eastern Province (Kayonza / Kirehe / Bugesera)** | **Drought + flood** | Bugesera drought-prone (lower rainfall belt); Kirehe flood-prone in heavy rain. |
| **Kigali City** | **Flash flood (urban) + landslide on hilly slopes** | Kigali built on hills (1,500–1,800 m); flash floods in valley districts (Nyabugogo) in heavy rain; landslides on steep slopes (Kimisagara, Nyamirambo escarpments). Strict KMP 2050 building permit enforcement reduces newer-build risk. |
| **All districts** | **Malaria** | Decreasing thanks to RBC ITN + IRS programmes; still endemic in lower-altitude eastern + western provinces. Kigali (1,500m+) lower risk. |

### Seismicity

- Rwanda sits on the **Albertine Rift** (East African Rift western branch) → **moderate seismic risk**, especially in NW (Rubavu, Musanze, parts of Karongi).
- Felt earthquakes magnitude 4–5 occur regularly in NW; large events rare but possible (1948 / 2008 events).
- Source: USGS earthquake archive `https://earthquake.usgs.gov/earthquakes/map/`.

### Build-era hazards (Rwanda)

| Era | Hazards |
|---|---|
| **Pre-1994** | Pre-genocide-era stock; many properties have **historical-claims due-diligence** requirement (verify chain of title via LAIS — restitution issues legally resolved through Gacaca courts + post-2000 Land Commissions, but title cleanliness checks essential). Concrete + masonry quality variable. |
| **1995–2010** | Reconstruction-era; mid-quality concrete; minimal seismic detailing in private builds. |
| **Post-2010** | **Rwanda Building Code 2009 (revised)** + **Rwanda National Building Code 2019** — improved seismic detailing requirements, esp. NW provinces. Verify compliance certificate via City of Kigali / district. |
| **Kigali post-2020 (KMP 2050 era)** | Permits checked against zoning; quality rises. |

### Mandatory / strongly recommended diagnostics at sale (Rwanda)

| Document | When required | Authority |
|---|---|---|
| **Certificate of Registration (LAIS title)** | All sales | RLMUA — verify UPI online |
| **Land use plan compliance** | Kigali + districts with KMP 2050 / district plans | City of Kigali / district BPMIS |
| **Building permit + Occupancy Certificate** | All formal sales of buildings | City of Kigali / district |
| **Tax clearance certificate (RRA)** | All sales | RRA |
| **Sub-lease / leasehold deed** | Foreign buyers (always) | RLMUA |
| **Architectural + structural drawings** (post-2009 builds) | Strongly recommended | Seller |
| **Body corporate by-laws + financial statements** | Apartments / condominiums | Body corporate / managing agent |
| **Proof of clear historical title** (Pre-1994 stock especially) | Strongly recommended | Conveyancing lawyer |

### Climate change projections (Meteo Rwanda + IPCC AR6)

- **Temperature**: +1.0–2.0 °C by 2050 (RCP4.5/SSP2-4.5); +2.5–4.0 °C by 2100 (RCP8.5/SSP5-8.5) over 1981–2010 baseline. (IPCC AR6 East Africa regional assessment.)
- **Precipitation**: high uncertainty — most models suggest slight increase in mean annual rainfall but **higher variability + extreme events** (more intense short-rain bursts → flood risk).
- **Drought**: Eastern Province (Bugesera, Kirehe) increased drought stress; potential agricultural pressure on rural land values.
- **Landslide**: more intense rainfall → elevated landslide risk on already-steep slopes, esp. Northern + Western provinces.
- **Glacier-fed streamflow**: not relevant (no glaciers in Rwanda mountains).

Source: Meteo Rwanda Climate Atlas `https://www.meteorwanda.gov.rw/` + Rwanda's Updated NDC 2020 (UNFCCC) `https://unfccc.int/`.

---

## Section: `--mains`

### Coverage in Rwanda

Rwanda's mains-utility coverage in **urban Kigali is exceptional for sub-Saharan Africa** — verify per-parcel but the framework is robust.

- **Water + sanitation**: **WASAC — Water and Sanitation Corporation** (`https://www.wasac.rw/`) — national utility; near-universal piped-water coverage in Kigali urban districts; expanding in secondary cities.
- **Sewerage**: limited centralised sewerage even in Kigali — most properties (incl. premium villas) use **on-site septic systems / soak-pits**. Only specific corridors (CBD, some new developments) on centralised sewer. Verify per-property.
- **Electricity**: **REG / EUCL — Rwanda Energy Group / Energy Utility Corporation Limited** (`https://www.reg.rw/` + `https://www.reg.rw/about-us/subsidiaries/eucl/`); national grid covers ~75 % of households (NISR EICV-7); ~95 %+ urban Kigali. Combination of hydro (incl. Lake Kivu KivuWatt methane-to-power), peat, solar, grid imports.
- **Internet**: **fibre + 4G** widely available in Kigali; **MTN, Airtel, Liquid Intelligent Technologies**; Kigali fibre-to-home available in most premium districts.

### Verification

1. **Certificate of Registration / Sub-lease deed** confirms parcel identity (UPI).
2. **Most recent WASAC water bill + EUCL electricity bill** — confirm meter on the parcel.
3. **Septic / soakaway diagram** — request from seller; many properties pre-2015 lack formal documentation; ask conveyancer to do site verification.
4. **WASAC sewer map** — for premium developments with sewer connection, request connection certificate.
5. **Building permit + Occupancy Certificate** confirms site-services compliance at construction.
6. KMP 2050 zoning may indicate planned-sewer-corridor expansion — relevant for off-plan / new builds.

### Kigali-specific

- **Power**: load-shedding **rare since 2020** (excess capacity post-KivuWatt methane-power + grid expansion); occasional planned maintenance.
- **Water**: **occasional supply interruptions** in dry-season peaks (Jun–Sep) at high-elevation districts (Kacyiru, Nyarutarama hilltops); most premium properties have **header tanks** as standard.
- **Generators / backup**: standard for premium properties + most office buildings; budget USD 1,500–10,000 for residential 5–10 kVA inverter+battery+solar combo (verify 2025 prices via local installer).

### Costs (2024–2025 ranges, USD est.)

| Scenario | Cost (USD est.) |
|---|---:|
| WASAC water connection (urban Kigali, new) | $200–$800 |
| WASAC sewer connection where corridor exists | $500–$2,000 |
| Septic system (pre-cast, residential) | $1,500–$5,000 |
| Soak-away / french-drain | $300–$1,500 |
| EUCL grid connection (urban) | $200–$1,500 |
| Solar + inverter + battery (5 kVA / 5 kWh) | $3,500–$8,000 |
| Solar + inverter + battery (10 kVA / 10 kWh) | $8,000–$18,000 |
| Borehole drill (peri-urban, depth-dependent) | $3,000–$10,000 |

### Kigali utility advantage

- Kigali's **utility coverage + reliability + paved-road access + cellular + fibre** is genuinely exceptional for sub-Saharan Africa. Worth flagging — it is a structural advantage that does not show up in headline price-per-m² comparisons but materially de-risks buy-and-hold ownership.

---

## Section: `--crime`

### Primary sources

- **Rwanda National Police (RNP)** — `https://www.police.gov.rw/` — annual crime statistics in police reports (less granular than EU forces; commune/district level rare publicly).
- **NISR Establishment Census + Vital Statistics** — `https://www.statistics.gov.rw/`.
- **UN Office on Drugs and Crime (UNODC) Statistics** — `https://dataunodc.un.org/` — country aggregates.
- **WHO Global Health Observatory** — homicide rate as a stable cross-country metric.

### National benchmarks

- **Intentional homicide rate** (UNODC, 2020s): ~**2.0–2.5 per 100,000** — among the **lower** rates in sub-Saharan Africa.
- **Petty crime / theft** in Kigali: low by African capital standards; tourism-corridor pickpocketing exists but property crime against residential is comparatively rare (anecdotal — verify with neighbours / local policing district).

### Rwanda-specific note

- **High visible policing + curfew compliance + community policing structures (Inyangamugayo at cell level)** give Kigali a notably safer feel than most African capitals.
- **Walking-around safety** at night in Kigali central districts: generally very good; verify per-district.
- **Border zones (Rubavu / Gisenyi facing DRC; Cyangugu / Rusizi facing DRC)**: occasional cross-border-tension incidents (notably 2022–2024 M23 conflict spillover); residential property risk remains low but factor in for tourism-yield exposure to DRC instability.

### Verdict bands (Rwanda-specific calibration)

- 🟢 Kigali interior districts (Nyarutarama, Kacyiru, Kimihurura, Gacuriro): low risk — verified by visible policing + low rates.
- 🟡 Outer Kigali / Kicukiro suburban: low–moderate; verify with district police station.
- 🟠 Rubavu / Rusizi border zones: monitor regional security situation (DRC tensions).
- 🔴 N/A under normal conditions.

### Confidence

**MEDIUM** — homicide rate is well-documented at national level (UNODC); per-district granularity less publicly available than EU equivalents.

---

## Section: `--amenities`

### OSM coverage

Rwanda has **strong OSM coverage in Kigali** (YouthMappers + Missing Maps work since ~2014); thinner but improving in secondary cities and rural areas.

Use universal `shared/amenities-osm.md` Overpass queries.

### Brand-chain conventions (Kigali)

- **Supermarkets**: **Simba Supermarket** (largest local), **Sawa Citi**, **Carrefour** (Kigali Heights / Kigali City Tower), **Nakumatt-successor stores**, **Choppies** (entry/exit cycles tracked), **Kazana**, **Vision City Mall** food anchors.
- **Pharmacies**: pharmacies are well-distributed in Kigali (`amenity=pharmacy` reliable in OSM).
- **Hospitals**: **King Faisal Hospital** (premier private), **CHUK** (Centre Hospitalier Universitaire de Kigali, public referral), **Rwanda Military Hospital — Kanombe**, **Kibagabaga Hospital** (district), **Kanombe Hospital**. Network of district hospitals across all 30 districts.
- **Schools**: international schools cluster in Kacyiru / Kimihurura / Nyarutarama (Green Hills Academy, Kigali International Community School — KICS, Riviera High School, Lycée de Kigali, Ecole Belge).
- **Public transport**: **Kigali Bus Service (KBS)** + private operators (Royal Express, Volcano Express); **moto-taxis** dominate point-to-point.

### Verdict bands (universal)

- 🟢 < 1 km / < 12 min walk to main amenities (Kigali central districts typical)
- 🟡 1–3 km
- 🟠 3–10 km
- 🔴 > 10 km (rural / outer peri-urban)

⚠️ OSM caveat: cross-check rural results via Google Maps / local agency before signing.

---

## Section: `--climate`

### Climate basics

- **Köppen-Geiger**: most of Rwanda is **Cwb** (subtropical highland — warm summer, dry winter) or **Aw** (tropical savanna) at lower elevations.
- **Elevation**: Kigali ~1,500–1,800 m; Musanze ~1,800–2,500 m; Lake Kivu ~1,460 m; Eastern lowlands ~1,200–1,400 m.
- **Two rainy seasons**: long rains Mar–May; short rains Sep–Dec. Dry seasons Jun–Aug + Jan–Feb.
- **Temperature**: Kigali daytime 22–28 °C year-round; cool nights 12–18 °C; minimal seasonal swing.

### Reference sources

- **Meteo Rwanda Climate Atlas** — `https://www.meteorwanda.gov.rw/`
- **IPCC AR6 Atlas** (East Africa) — `https://interactive-atlas.ipcc.ch/`
- **Copernicus Climate Data Store (universal)** — `https://cds.climate.copernicus.eu/`
- **Rwanda Updated NDC 2020 (UNFCCC)** — `https://unfccc.int/`

### Trajectory

- **Temperature**: +1.0–2.0 °C by 2050 (SSP2-4.5); +2.5–4.0 °C by 2100 (SSP5-8.5).
- **Precipitation**: more intense extremes; mean uncertain.
- **Heat days**: Kigali's elevation insulates from extreme-heat events typical of lowland tropics; nights remain cool — air-conditioning rarely required (a structural cost-of-ownership advantage).
- **Drought**: Eastern Province (Bugesera, Kirehe) increased stress.
- **Sea-level rise**: N/A (landlocked).
- **Wildfire**: low (humid/dense agriculture); some grass-fire risk Eastern dry season.

### Verdict bands

- 🟢 Kigali highland properties (1,500m+): generally resilient — temperature buffered by elevation; no SLR; flood risk mitigated by hill topography (with hill-slope landslide flag below).
- 🟡 Eastern Province (drought-leaning): plan for water security.
- 🟠 NW border (Rubavu / Musanze): volcanic + seismic + landslide overlay; not a climate flag per se but a multi-hazard area.

### Confidence

**MEDIUM** — IPCC AR6 East Africa regional projections + Meteo Rwanda national-scale; finer-resolution downscaled models limited.

---

## Cost benchmarks (RW 2026)

| Work | Cost (USD est.) |
|---|---:|
| Sale levy 2 % (registered taxpayer) | 2 % of sale value after deducting the first FRW 5 M |
| Land registration 0.5 % | 0.5 % of price |
| Land transfer fee (residential flat) | ~$15 (FRW 20,000) |
| Notary fees (typical) | 0.5–1 % of price |
| Conveyancing lawyer (foreign-buyer-grade) | $1,000–$3,000 |
| Independent property inspection | $500–$1,500 |
| Title search (LAIS via RLMUA) | < $50 |
| Land surveyor (boundary verification) | $500–$2,000 |
| Building permit application (City of Kigali) | $500–$5,000 (depends on scope) |
| Architect (residential design) | $5,000–$30,000+ |
| Septic + soakaway install | $1,500–$5,000 |
| Standard 5 kWh inverter+battery+solar | $3,500–$8,000 |
| Building code structural assessment (post-2009) | $500–$2,000 |
| **Total transaction cost (buyer side, USD 200k purchase)** | ~3.0–4.5 % of price |

## Active fiscal incentives (Investment Code 2021 + 2024 reform)

- **Preferential CIT 15 %**: registered investors in energy generation (solar / hydro / biomass / wind / methane / peat / geothermal) + exporters with 50 %+ exports.
- **Preferential CIT 25 %**: registered exporters with 30–50 % exports.
- **Preferential CIT 3 %**: pure holding companies, investment SPVs, collective investment schemes, foreign-source-income IP companies (Kigali International Financial Centre route).
- **150 % tax deduction** for SME / emerging investor internationalisation expenditure.
- **Strategic Investment Project (SIP)** designation: bespoke incentive package available for nationally-significant projects.
- **Source**: `https://rdb.rw/invest` + Law N° 006/2021 of 05/02/2021.

## Common listing platforms

- **House in Rwanda** — `https://www.houseinrwanda.com/`
- **Rwandan Houses** — `https://rwandanhouses.com/`
- **Plut Properties** — `https://plutproperties.com/`
- **Kwanda Real Estate** — `https://kwandarealestate.com/`
- **Property24 Rwanda** — `https://www.property24.co.rw/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Rwanda portal (Property24 is South Africa-only)
- **Real Estate in Rwanda (REIR)** — `https://reir.rw/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with REIR association appears defunct — use RDB (rdb.rw) / RLMUA (lands.rw) for primary data
- **Kigali Inspectify** — `https://kigaliinspectify.com/`

## Caveats unique to RW

- **Foreigners cannot get freehold** — leasehold (99 yr) only, except via international convention reciprocity. Verify remaining lease term, not just "the property has a 99-year lease" (a 99-year lease started 1995 has 68 years left).
- **Pre-1994 chain-of-title due diligence** — historical-claims layer for properties owned/transferred during/before genocide; LAIS resolves most cases via post-2000 Land Commissions + Gacaca-related restitution programmes, but a foreign buyer should require an explicit conveyancing-lawyer chain-of-title certificate for pre-1994 properties. **HIGH structural integrity post-LTR 2009–2013 thanks to systematic re-registration**, but individual edge cases exist.
- **KMP 2050 + district master plans** are **strictly enforced** — building anything outside zoning will be denied permit; informal-construction risk lower in Kigali than in many emerging-market capitals.
- **Cadastre is unusually clean for the region** — Rwanda's LAIS is one of Africa's better digital land registries; titling rate ~93 % (gender-equal; LTR 2009–2013 + ongoing). Verify UPI and don't assume informal "ubukungu" / customary tenure suffices.
- **Tax compliance discipline is high** — RRA enforces aggressively; ensure all tax clearances current at transfer.
- **English is the practical legal language** — 2008 administrative shift from French; most contracts now in English (sometimes bilingual Kinyarwanda).
- **Rwf depreciation against USD** — ~5–10 %/yr typical recent. Foreign buyers should hedge or accept that USD-denominated returns trail RWF-denominated ones in the lease/rent stream.
- **BNR > USD 10k transfer notification** — bank notifies BNR; not a restriction but a reporting trigger; expect KYC documentation requests for larger transfers.
- **No national postcode** — addresses are by Cell / Sector / District + landmark; UPI is the unambiguous identifier.
- **Lake Kivu methane** (Karongi / Rubavu / Rusizi shoreline) — managed via methane extraction (KivuWatt); residual limnic-eruption risk is low but non-zero; for shoreline property factor in disaster awareness.
- **Volcanic + seismic NW Rwanda** — Nyiragongo (DRC, 20 km from Gisenyi) is one of world's most active volcanoes; Rubavu / Musanze + parts of Western/Northern provinces face material multi-hazard exposure. **2021 eruption tremors felt in Kigali (90 km).**
- **Investor visa "USD 500k luxury property" path** — appears in secondary-source aggregator articles (IMI Daily, Kwanda RE, Mackrell) but is **NOT a clearly-published primary RDB programme name**. The primary-source-confirmed path is the **Investment Code 2021 USD 250k registered-investor route** (Law N° 006/2021 Art. 14). **Verify with RDB One-Stop Centre** before relying on the property-only path.
- **Kigali utility reliability is exceptional for sub-Saharan Africa** — water, electricity, fibre, paved roads, cellular all near-EU-standard in central districts. Worth flagging as a structural advantage.

## Reddit / forum sources

- **r/Rwanda** — general; modest activity
- **r/Africa** — broader context
- **House in Rwanda blog** — `https://www.houseinrwanda.com/news/`
- **Kwanda Real Estate news** — `https://kwandarealestate.com/news` — investor-oriented commentary (secondary aggregator; cross-check claims)
- **The New Times** — `https://www.newtimes.co.rw/` (state-leaning national paper)
- **Kigali Times** — `https://www.kigalitimes.rw/`
- **Rwanda Today** — `https://rwandatoday.africa/`
- **Taarifa** — `https://taarifa.rw/`
- **Igihe** — `https://en.igihe.com/`

## Verification authorities

| Authority | When to call |
|---|---|
| **RLMUA** (Rwanda Land Management and Use Authority) | Title verification (LAIS); UPI lookup; sub-lease registration |
| **RDB** (Rwanda Development Board) | Investor certificate; One-Stop Centre; visa-by-investment |
| **RRA** (Rwanda Revenue Authority) | TIN; property tax / rental tax / CGT clearance |
| **City of Kigali — BPMIS** | Building permit; zoning compliance under KMP 2050 |
| **District authority** | Land tax rates; secondary city building permits |
| **DGIE — Directorate General of Immigration & Emigration** | Visa class verification; permit issue/renewal |
| **WASAC** | Water + sewer connection certificate |
| **REG / EUCL** | Electricity connection |
| **REMA** | Environmental compliance; wetland; EIA |
| **Notary (regulated)** | Sale-deed authentication |
| **Conveyancing lawyer (registered)** | Title due diligence; chain-of-title (pre-1994 esp.) |
| **MINEMA** | Hazard mapping (national level) |
| **Meteo Rwanda** | Climate baseline |
| **RNP** (Rwanda National Police) | District-level crime |
| **BNR** (National Bank of Rwanda) | FX framework; > USD 10k notification |

## Quirks to know

- **UPI is everything** — Unique Parcel Identifier in LAIS is the single source of truth for any property; insist on UPI in all documentation.
- **No paper titles since 2024** — all titles electronic; physical printout fee FRW 5,000 only for special copies.
- **One Step One Day Transfer** — RLMUA's flagship target: simple residential transfers can complete within **one working day** at full LTR-coverage parcels. Verify this for your property's location.
- **Foreigner buys leasehold; Rwandan citizen buys freehold** — same physical property may have different available tenure types depending on buyer nationality.
- **Investor-Certificate route is well-trodden** — RDB processes investor certificates within 2 working days once docs complete; the route is genuinely operational, not just nominal.
- **Tax handbook online** — `https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf` — primary RRA reference for all taxes; cite by section when computing.
- **Kigali Master Plan 2050 portal** — `https://bpmis.gov.rw/` — building permits checked here; foreign buyers should verify any planned-extension / planned-build complies BEFORE purchase.
- **Construction quality varies pre-2009 / post-2009** — the National Building Code 2009/2019 raised standards; pre-2009 stock often lacks formal seismic detailing.
- **Body corporate culture is nascent** — apartment / condominium body-corporate governance less mature than ZA / KE; demand bylaws + financials before buying in any building.
- **Volcanic risk discussion is often understated** — even Kigali-resident agents sometimes downplay the NW border seismic / volcanic exposure; pull USGS + Smithsonian primary data.
- **EAC / CEPGL passport benefits** — citizens of EAC / COMESA member states get reduced investor thresholds (USD 100k vs USD 250k for OECD nationals).
- **USD pricing parallel to RWF** — premium Kigali properties commonly listed in USD; ensure contract specifies which currency is the contract currency for default interpretation.

## Source URL templates

| Source | URL |
|---|---|
| RLMUA — Lands portal | `https://www.lands.rw/` |
| RLMUA — Rwanda Land Mgmt & Use Authority | `https://www.lands.rw/` |
| RDB — Rwanda Development Board | `https://rdb.rw/` |
| RDB Business Procedures | `https://businessprocedures.rdb.rw/` |
| RDB Investment Incentives | `https://rdb.rw/invest` |
| RRA — Rwanda Revenue Authority | `https://www.rra.gov.rw/` |
| RRA Tax Handbook | `https://www.rra.gov.rw/fileadmin/Folder_for_2025/RRA_Tax_Handbook_2025_Final.pdf` |
| RRA Immovable Property Tax page | `https://www.rra.gov.rw/index.php?id=64&L=27` |
| RRA Rental Income Tax page | `https://www.rra.gov.rw/fileadmin/img/rental-income-tax.html` |
| BNR — National Bank of Rwanda | `https://www.bnr.rw/` |
| BNR exchange rates | `https://www.bnr.rw/avgexchangerate` |
| NISR — Statistics | `https://www.statistics.gov.rw/` |
| RPHC-5 (2022 Census) | `https://www.statistics.gov.rw/data-sources/censuses/Population-and-Housing-Census/fifth-population-and-housing-census-2022` |
| City of Kigali | `https://www.kigalicity.gov.rw/` |
| KMP 2050 portal | `https://bpmis.gov.rw/` |
| Migration / DGIE | `https://www.migration.gov.rw/` |
| WASAC | `https://www.wasac.rw/` |
| REG / EUCL | `https://www.reg.rw/` |
| MINEMA | `https://www.minema.gov.rw/` |
| REMA | `https://www.rema.gov.rw/` |
| Meteo Rwanda | `https://www.meteorwanda.gov.rw/` |
| Rwanda National Police | `https://www.police.gov.rw/` |
| Investment Law 2021 (UNCTAD) | `https://investmentpolicy.unctad.org/investment-laws/laws/369/rwanda-investment-law-2021` |
| US State Dept 2025 ICS Rwanda | `https://www.state.gov/reports/2025-investment-climate-statements/rwanda` |

## Status

**Status**: ✅ fully populated as of 2026-05-07
**Confidence**: HIGH — primary government sources (RLMUA, RRA, RDB, NISR, BNR, Migration / DGIE) are unusually accessible for sub-Saharan Africa; Land Tenure Regularisation 2009–2013 + LAIS digital cadastre give parcel-level title verification at a quality rare for the region. MEDIUM for residential price benchmarks (no published RPPI; ranges are listing-aggregator est.). MEDIUM for the "USD 500k luxury-property residence-by-investment" claim (secondary-source repeated; primary RDB programme name not publicly confirmed — verify via RDB One-Stop Centre).
**Last verified**: 2026-08-07 (CGT re-verified — Law N° 014/2025 raised the Art. 36 rate 5 % → 10 % from 29/05/2025, immovable property confirmed outside the Art. 37 CGT base, standard CIT corrected 30 % → 28 %; prior full validation sweep 2026-05-27). Rental / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
