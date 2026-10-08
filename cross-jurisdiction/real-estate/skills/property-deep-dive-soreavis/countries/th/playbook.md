# Thailand 🇹🇭 — Property Due-Diligence Playbook

ISO2: `th`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

> **🇹🇭 LEAD WARNING — read before any other section.** Thailand is a **foreign-restricted** market. **Foreigners cannot own land freehold** under the Land Code BE 2497 (1954). The only clean foreign-ownership pathway is a **Chanote-titled condominium unit** within a project's 49% foreign quota. All other structures (lease, Thai company, marriage) carry legal/enforceability risk. Six- to seven-figure decisions in Thailand demand a Thai-licensed real-estate lawyer — non-negotiable. Skip the lawyer-fee line and you can lose the entire principal.

## Country profile

- **Postcode (รหัสไปรษณีย์)**: 5 digits.
  - Bangkok metropolitan: `10xxx` (e.g., `10110` Khlong Toei / Sukhumvit area, `10330` Pathumwan)
  - Chiang Mai: `50xxx` (e.g., `50200` Mueang Chiang Mai)
  - Phuket: `83xxx` (e.g., `83000` Mueang Phuket, `83110` Kathu/Patong, `83150` Cherng Talay)
  - Pattaya / Chonburi: `20xxx` (Pattaya `20150`)
  - Hua Hin / Prachuap Khiri Khan: `77xxx` (Hua Hin `77110`)
  - Koh Samui / Surat Thani: `84xxx` (Koh Samui `84320` Bo Phut)
  - Source: Thailand Post `https://www.thailandpost.co.th/`
- **Admin levels**: 76 จังหวัด (provinces) + Bangkok Metropolitan Administration (special — กรุงเทพมหานคร) → 928 อำเภอ (districts; in Bangkok = เขต / khet, 50 in BMA) → 7,255 ตำบล (subdistricts; in Bangkok = แขวง / khwaeng) → หมู่บ้าน (villages, rural)
  - Source: Department of Provincial Administration `https://www.dopa.go.th/` (counts per Thai Government open data; figures may shift on subdistrict reclassifications)
- **Currency**: THB (Thai baht, ฿). 1 USD ≈ 35–37 THB; 1 EUR ≈ 38–40 THB (Apr 2026 BoT reference; FX volatile, verify at `https://www.bot.or.th/`)
- **Languages**: Thai (official, ภาษาไทย); English widely used in condo sector, tourist hubs, premium developer brochures, and most title-related professional services. **All registered title documents are in Thai** — translation/sworn translator required for foreign buyers.
- **Cadastre / land registry**: **Department of Lands (กรมที่ดิน, DOL)** — `https://www.dol.go.th/`
  - DOL e-Service portal: `https://eservice.dol.go.th/`
  - LandsMaps web GIS (parcel viewer, FREE): `https://landsmaps.dol.go.th/`
  - Title searches must be done in person at the provincial DOL office (สำนักงานที่ดิน) for the parcel's location — many records still paper-original.
- **Title deed types** (CRITICAL — only Chanote and Nor Sor 3 Gor are safely transferable; foreigners should accept **Chanote only**):

| Code | Thai | Type | Boundary precision | Foreign use | Notes |
|---|---|---|---|---|---|
| **โฉนด** (Chanote) | Nor Sor 4 Jor (น.ส.4จ.) | Full title deed | GPS-surveyed | ✅ acceptable | Strongest title; freehold; transferable |
| **น.ส.3 ก.** | Nor Sor 3 Gor | Confirmed certificate of use | Aerial-photo surveyed | ⚠️ caution | Transferable but boundaries less precise; can be upgraded to Chanote |
| **น.ส.3** | Nor Sor 3 | Certificate of use | Hand-surveyed | ❌ avoid | Transferable but vague boundaries; many disputes |
| **ส.ค.1** | Sor Kor 1 | Notification of possession | None | ❌ avoid | Cannot be transferred; possession only |
| **ภ.บ.ท.5** | Por Bor Tor 5 | Tax payment receipt | None | ❌ never | Not a title; tax-payer record only; common scam involves selling these as "land" |

- **Major reforms / regulatory landscape** (see `shared/regulatory-watch.md` for date-stamped detail):
  - **Land and Building Tax Act BE 2562 (2019)** — first national property tax, effective 1 January 2020. Source: Royal Gazette `http://www.ratchakitcha.soc.go.th/` Vol 136 special part 30 ก.
  - **Thailand Privilege Card** restructure — September 2023 (formerly "Thailand Elite"). Source: `https://thailandprivilege.co.th/`
  - **Long-Term Resident (LTR) Visa** — launched 1 September 2022 by BoI. Source: `https://ltr.boi.go.th/`
  - **Destination Thailand Visa (DTV)** — launched mid-July 2024 by Ministry of Foreign Affairs. Source: `https://www.mfa.go.th/`
  - **Foreign Business Act BE 2542 (1999)** — ongoing enforcement; nominee-company crackdown stepped up 2024 (DBD warnings) under Land Code §96bis.
  - **Proposed reforms NOT enacted as of May 2026**: sap ing sit term extension from 30 to up to 99 years (Sap Ing Sit Act B.E. 2562 s.4; Cabinet discussion 2024); foreign condo quota raise from 49% to 75% (Ministry of Interior proposal 2024); current status not re-verified from a primary source (a Cabinet resolution of 18 Jun 2024 directed the Ministry of Interior to review both rules, secondary: BBC Thai) — verify at the Royal Gazette `https://ratchakitcha.soc.go.th/`. Verify via Cabinet Resolution database `https://resolution.soc.go.th/`.

---

## 🇹🇭 LEAD SECTION: Foreign buyer eligibility

### Bottom line

Foreigners **cannot own land freehold in Thailand**. The Land Code BE 2497 (1954) §86 is the general prohibition; §96 lists the narrow exceptions (BoI-promoted industrial land, treaty-based reciprocity for specific countries which Thailand does not currently exercise, inherited via Thai-spouse with court order to dispose within 1 year). For residential property, the practical paths are:

1. **Condominium unit, Chanote title, within 49% foreign quota** — the only clean legal freehold available to foreigners
2. **30-year registered lease** of land (with house owned separately) — renewable by contract but renewals not enforceable beyond original 30
3. **Thai limited company** holding land (foreigner ≤49% shares) — high legal risk under §96bis (anti-nominee)
4. **Marriage to Thai national** — Thai spouse owns the land, foreigner has no claim
5. **Usufruct (สิทธิเก็บกิน) / superficies (สิทธิเหนือพื้นดิน) / habitation right (สิทธิอาศัย)** — limited rights, registered at DOL, term capped at lifetime or 30 years

### Path 1: Condominium freehold (✅ recommended for most foreign buyers)

- Legal basis: **Condominium Act BE 2522 (1979)**, as amended (1991, 1999, 2008). Source text via Office of the Council of State `https://www.ocs.go.th/searchlaw`.
- **49% foreign quota**: foreigners may collectively own up to 49% of the **total saleable floor area** of any one condominium project. The quota is **per project, not per unit type**.
- **Quota verification** before purchase: ask the project's juristic person (นิติบุคคลอาคารชุด — condo management entity) for a written **Foreign Quota Certificate** stating current foreign-owned area % and confirming the unit you are buying is "in foreign quota". Without it, DOL will not transfer the unit to a foreign name.
- **FX rule (mandatory)**: purchase funds must be remitted **from abroad in foreign currency** and converted to THB inside Thailand. The receiving Thai bank issues a **Foreign Exchange Transaction Form (FET / formerly Tor Tor 3 / ธ.ต.3)** for any single inbound transfer ≥ USD 50,000 (or its equivalent). FET is mandatory evidence at DOL transfer; without it, the transfer cannot be registered. Source: Bank of Thailand FX regulation `https://www.bot.or.th/en/our-roles/financial-markets/foreign-exchange-regulations.html`
- **Resale vs new**: foreign quota is set per project at registration; new launches by reputable developers typically reserve foreign units up-front. Resale risk: a unit may have been sold to a Thai owner and now needs to slot back into foreign quota — verify with the juristic person *in writing*.

### Path 2: 30-year leasehold of land

- Legal basis: **Civil and Commercial Code §540 (lease cap 30 years)** and **§541 (renewal)**. Source via Krisdika `https://www.ocs.go.th/searchlaw`.
- A lease registered at DOL for a term > 3 years is enforceable against subsequent landowners; **maximum registrable term: 30 years**.
- **"30 + 30 + 30" / "90-year lease"**: marketed by developers as effectively perpetual. **Legal reality**: only the first 30-year term is enforceable as a registered right. The two renewals are *contractual options* — if the landowner refuses or transfers the land, Thai courts have held that successor owners are NOT bound by unregistered renewal options. Multiple Supreme Court (Dika) rulings (e.g., 2008/2557, 2015/2358) have nullified second-term claims.
- **Practical implication**: budget the property as a 30-year asset with optional (uncertain) extension. Discount the price accordingly vs freehold.
- **Proposed 99-year sap ing sit term (2024–2025)**: a Cabinet resolution of 18 Jun 2024 directed the Ministry of Interior to review extending the ทรัพย์อิงสิทธิ (sap ing sit) term under Sap Ing Sit Act B.E. 2562 s.4 from 30 to up to 99 years (secondary: BBC Thai); not enacted as of May 2026. Watch `https://resolution.soc.go.th/` and the Ministry of Interior.

### Path 3: Thai limited company structure (⚠️ high legal risk)

- Mechanism: a Thai limited company is incorporated, with the foreign buyer holding ≤49% (max permitted) of voting shares; ≥51% must be held by Thai nationals. The company buys the land freehold; the foreigner controls via director rights and preferential share class.
- **Risk under Land Code §96bis**: if the Thai shareholders are "nominees" (holding shares for the foreigner without contributing genuine capital), the structure is illegal. DOL has anti-nominee guidance and demands evidence of Thai shareholder source-of-funds at land transfer.
- **Enforcement intensity**: the Department of Business Development (DBD, กรมพัฒนาธุรกิจการค้า) has stepped up nominee investigations 2023–2024 (notably in Phuket and Koh Samui). Penalties: criminal fine + imprisonment up to 2 years + forced disposal of the land within 1 year.
- **Practical guidance**: most reputable Thai law firms will no longer set up a "thin" company purely for residential foreign holding. The structure is acceptable only if there is genuine Thai shareholder capital and a real operating purpose.

### Path 4: Marriage to a Thai national

- Thai spouse can own land in their sole name. The foreign spouse must sign a **declaration at DOL** confirming the funds are the *Thai spouse's separate property* (sin suan tua / สินส่วนตัว) — i.e., the foreigner relinquishes any community-property claim to that land.
- On divorce: Thai spouse keeps the land. Foreigner has no recoverable interest.
- On Thai spouse's death: foreigner inherits but must dispose within **1 year** (Land Code §93).

### Path 5: Limited rights (Usufruct / Superficies / Habitation)

- **Usufruct (สิทธิเก็บกิน)**: lifetime or up-to-30-year right to use and enjoy land owned by another (e.g., Thai spouse, family). Registered at DOL. Cannot be sold by usufructuary; survives transfer of the underlying land.
- **Superficies (สิทธิเหนือพื้นดิน)**: right to own buildings on someone else's land. Useful when foreigner builds a house on Thai-spouse-owned land — the building (but not the land) is registered to the foreigner. Up to 30 years or lifetime.
- **Habitation (สิทธิอาศัย)**: personal right to live in a dwelling. Lifetime or fixed term up to 30 years.

### Anti-nominee enforcement (read this before considering a company structure)

- Land Code §96bis (added 1999) prohibits any Thai national from holding land "as nominee" for a foreigner.
- DOL has a checklist of nominee-flag indicators: Thai shareholders with no relevant occupation, all shares paid via single foreign-source loan, sole Thai shareholder is the developer's secretary, etc.
- **2024 DBD circular** (verify current text at `https://www.dbd.go.th/`) instructed provincial offices to refer suspected nominee structures to the police.
- Penalty: criminal (up to 2 years prison + 20,000 THB fine for the foreigner; same for the Thai nominee) + forced sale within 1 year + civil voidance of the title.

### Foreign Business Act BE 2542 (1999)

- Restricts foreign majority ownership in many sectors. **Real-estate brokerage** (List 3 §22) is a restricted activity → foreigners cannot run a Thai real-estate agency without BoI/MoC approval.
- Source: Ministry of Commerce text `https://www.dbd.go.th`

### Confidence

**HIGH** — Land Code, Condominium Act, Civil and Commercial Code, FBA, FET rules are all primary statutes published in the Royal Gazette and on the Office of the Council of State website. Anti-nominee enforcement intensity (Path 3 risk) is MEDIUM-confidence — varies by province and political cycle.

---

## Section: `--price`

### Primary sources

- **REIC (Real Estate Information Center, ศูนย์ข้อมูลอสังหาริมทรัพย์)** — Government Housing Bank (GH Bank) subsidiary, semi-official data.
  - Portal: `https://www.reic.or.th/`
  - English summaries: `https://www.reic.or.th`
  - Quarterly transfer-price index, condo price index by zone, supply pipeline.
- **AREA (Agency for Real Estate Affairs, บริษัท เอเจนซี่ ฟอร์ เรียลเอสเตท แอฟแฟร์ส)** — semi-private, widely cited; market intelligence reports.
  - Portal: `https://www.area.co.th/`
- **Treasury Department (กรมธนารักษ์, Ministry of Finance)** — official **appraised values** (ราคาประเมิน) used as the tax base for transfer fee, SBT, withholding tax.
  - Portal: `https://www.treasury.go.th/`
  - Online appraisal lookup: `https://assessprice.treasury.go.th/`
  - Note: appraised value is typically **30–60% of market value** in Bangkok central districts — useful as a tax-base reference, not a price benchmark.
- **DOL transfer registers** — actual sale prices filed at transfer; not centrally published, accessible per-parcel at provincial DOL.
- **Bank of Thailand (ธนาคารแห่งประเทศไทย)** — quarterly real estate stability monitors. `https://www.bot.or.th/en/statistics/real-sector.html`

### Listing platforms (secondary, listings = seller-controlled)

- **DDProperty** (largest, English+Thai): `https://www.ddproperty.com/`
- **Hipflat**: `https://www.hipflat.co.th/` — strong on Bangkok condos with sold-price overlays (mix primary + listing)
- **FazWaz**: `https://www.fazwaz.com/` — foreign-buyer focused, Phuket/Pattaya/Bangkok
- **Thailand-Property.com**: `https://www.thailand-property.com/`
- **Lazudi**: `https://www.lazudi.com/`
- **Bangkok Post Property**: `https://property.bangkokpost.com/`
- **Hipflat 88, Livinginsider** (Thai-language, sometimes lower-priced listings)

### Price benchmarks (Q4 2025 / Q1 2026 reference)

> **Source warning**: REIC quarterly indexes are the most reliable Bangkok/national reference. Listing-platform averages are seller-controlled and can run 10–25% above realized prices. Use REIC for verdict, listings for comp shopping.

| Locality | Segment | THB/sqm range | USD/sqm est. (35 THB/USD) | Source |
|---|---|---|---|---|
| **Bangkok central** (Sukhumvit Asok–Ekkamai, Sathorn, Silom, Chidlom) | New condo, branded | 200,000–400,000 | ≈ $5,700–$11,400 | REIC + DDProperty Q1 2026 [verify per project] |
| **Bangkok central** | Resale condo 5–10 yr | 130,000–250,000 | ≈ $3,700–$7,150 | REIC + Hipflat Q1 2026 |
| **Bangkok mid-tier** (Ratchada, Ari, On Nut, Lat Phrao MRT) | New condo | 100,000–180,000 | ≈ $2,850–$5,150 | REIC + DDProperty |
| **Bangkok suburban** (Bang Na, Min Buri, Nonthaburi, Pak Kret) | Condo / townhouse | 50,000–100,000 | ≈ $1,430–$2,850 | REIC |
| **Phuket** (Patong, Kamala, Surin, Bang Tao, Layan) | Condo / villa freehold | 100,000–300,000 | ≈ $2,850–$8,570 | DDProperty + FazWaz Q1 2026 |
| **Phuket** beachfront / luxury villa | Villa with land (lease/company) | 250,000–800,000+ | ≈ $7,150–$22,860+ | FazWaz / Lazudi |
| **Pattaya / Jomtien** | Condo | 60,000–150,000 | ≈ $1,710–$4,290 | DDProperty Q1 2026 |
| **Hua Hin** | Condo / villa | 60,000–180,000 | ≈ $1,710–$5,140 | DDProperty + FazWaz |
| **Koh Samui** | Condo / villa lease | 80,000–250,000 | ≈ $2,290–$7,150 | FazWaz / Lazudi |
| **Chiang Mai** (Mueang + Nimman) | Condo | 60,000–120,000 | ≈ $1,710–$3,430 | REIC + DDProperty |

> Ranges are listing-derived; verify realized vs listing using REIC quarterly transfer-price index and the Treasury appraised value as a floor.

### Compute

1. Listing price/sqm = listing THB ÷ saleable area (พื้นที่ใช้สอย, internal floor area). **Trap**: some Thai listings advertise "land area + house area" combined or only land area — clarify which.
2. Compare to REIC index for the same district (Bangkok BTS/MRT-stop level granularity available; Phuket/Pattaya/Chiang Mai zone-level only).
3. Compare to nearest 3–5 same-building / same-soi (ซอย, side-street) listings on Hipflat or DDProperty.
4. Pull Treasury appraised value via `https://assessprice.treasury.go.th/` for the parcel — informs the tax base, not the market value.
5. **Trap (foreign quota premium)**: condo units sold within foreign quota often list 5–15% higher than the same-floor Thai-quota equivalent. Verify whether the listing is "foreign quota" or "Thai quota" — they are NOT interchangeable for foreign buyers.

### Confidence

**HIGH** for Bangkok ranges (REIC + multiple listing platforms agree within ±10%). **MEDIUM** for Phuket/Samui villas (data dominated by foreign-buyer listing platforms; less REIC granularity). **LOW** for pure-villa land+house pricing in rural Isan/Northern Thailand.

---

## Section: `--traffic`

### Primary sources

- **Department of Highways (กรมทางหลวง, DOH)** — AADT counts on national highways (ทางหลวงแผ่นดิน).
  - Portal: `https://www.doh.go.th/`
  - Traffic data: `https://bhs.doh.go.th/` (Bureau of Highway Safety) — annual AADT
- **Department of Rural Roads (กรมทางหลวงชนบท, DORR)** — provincial/rural road network counts. `https://www.drr.go.th/`
- **Bangkok Metropolitan Administration (BMA) Traffic & Transportation Department** — Bangkok-specific traffic + commuter modal data. `https://www.bangkok.go.th/traffic/`
- **Expressway Authority of Thailand (EXAT, การทางพิเศษแห่งประเทศไทย)** — toll-expressway traffic. `https://www.exat.co.th/`
- **OpenStreetMap (OSM)** — fallback for road class when official AADT not available

### Verdict bands (vehicles per day)

- 🟢 < 2,000 v/d: rural lane, soi, sub-district road
- 🟡 2,000–10,000 v/d: small provincial road, urban side street
- 🟠 10,000–40,000 v/d: provincial trunk, urban arterial
- 🔴 > 40,000 v/d: national highway / Bangkok arterial / expressway feeder

### Coarse fallback (OSM `highway` tag)

- `motorway` / `trunk` = expressway (มอเตอร์เวย์) / national highway 1-digit (ทางหลวงหมายเลข เช่น 1, 2, 4)
- `primary` = ทางหลวงแผ่นดิน 2-digit
- `secondary` = ทางหลวงชนบท major
- `tertiary` = ทางหลวงชนบท minor / urban collector
- `residential` = ซอย (soi) / housing-estate road

### Bangkok-specific quirks

- Bangkok traffic is severe and chronic; AADT alone understates noise/pollution exposure because of stop-and-go congestion. A "20,000 v/d" Bangkok arterial behaves worse than a 40,000 v/d expressway in flow terms.
- Elevated expressways (ทางด่วน) over residential sois generate **noise + particulate exposure 24/7** for adjacent buildings — flag any property within 100 m of an expressway pillar.
- BTS/MRT lines are quieter (electric, elevated) but stations generate foot-traffic and concentrated retail — different exposure profile.

### Confidence

**MEDIUM** — DOH publishes AADT for national highways but coverage is patchy on provincial+rural roads; Bangkok BMA data is fragmented across departments. For most non-highway roads, OSM-class fallback is the realistic baseline.

---

## Section: `--tax`

### Annual property tax — Land and Building Tax (ภาษีที่ดินและสิ่งปลูกสร้าง)

**Primary statute**: Land and Building Tax Act BE 2562 (2019), effective 1 January 2020. Royal Gazette Vol 136, Special Part 30 ก, 12 March 2019. Replaced the old House and Land Tax (1932) and Local Development Tax (1965). Administered by **local administrative organizations** (อปท. — municipalities/subdistrict councils) and the **Bangkok Metropolitan Administration** for BMA-area parcels.

**Tax base**: appraised value (ราคาประเมิน) per the Treasury Department, NOT market value (typically 30–60% of market in Bangkok). Lookup: `https://assessprice.treasury.go.th/`

**Rate ceilings under the Act** (the 2019 statute caps; actual rates set by Royal Decree, currently the rates below):

| Use class | Rate range | Notes |
|---|---|---|
| **Agricultural** (เกษตรกรรม) | 0.01–0.15 % | Owned by individual: first 50M THB exempt (until 2024); excess progressive 0.01–0.10% |
| **Residential — primary residence** (บ้านอยู่อาศัยหลังหลัก) | 0.02–0.10 % | First **50M THB exempt** if owner of land+building together, **10M THB exempt** if owner of building only on leased/another's land — applies only to the *single primary residence* (1 person, 1 unit) |
| **Residential — secondary** (บ้านอยู่อาศัยหลังอื่น / second home / investment condo) | 0.02–0.10 % | NO exemption threshold — first baht taxed |
| **Other (commercial, industrial)** | 0.30–0.70 % | Hotel, retail, office, warehouse |
| **Vacant / unused** (ที่ดินรกร้างว่างเปล่า) | 0.30–0.70 % | Increases by 0.30 percentage points every 3 years up to a 3% ceiling |

**Current effective rates (Royal Decree 2563/2020, extended; for 2026/BE 2569 NO across-the-board Royal Decree reduction was issued — full statutory rates apply; verify the 2027/BE 2570 decree via Royal Gazette)**:

| Appraised value bracket (residential primary, owner-occupied) | Rate |
|---|---|
| ≤ 50,000,000 THB | exempt |
| 50,000,001–75,000,000 | 0.03 % |
| 75,000,001–100,000,000 | 0.05 % |
| > 100,000,000 | 0.10 % |

| Appraised value bracket (residential secondary / investment) | Rate |
|---|---|
| ≤ 50,000,000 THB | 0.02 % |
| 50,000,001–75,000,000 | 0.03 % |
| 75,000,001–100,000,000 | 0.05 % |
| > 100,000,000 | 0.10 % |

**Temporary reductions**: the Cabinet has issued Royal Decrees reducing the effective rate for specific years, but these were **episodic, not an automatic annual renewal** (90% reduction 2020–2021 COVID; ~15% reduction 2023; **none for 2026/BE 2569** — the pandemic-era discounts have expired and full statutory rates apply). **As of 2026-07-02 no across-the-board Royal Decree reduction was issued for the 2026 tax year.** Verify any 2027/BE 2570 decree and the four-year rate/threshold-review Gazette notice due late 2026 at `https://resolution.soc.go.th/` and the Royal Gazette (2026-07-02 verified, source: LEX Bangkok / Dansiam Property / Thailand Law Online 2026).

**Filing**: bills are issued by the local authority (กทม. for Bangkok, municipal/SAO elsewhere) by April; pay by August (penalty 1 %/month after due). Source: Ministry of Interior `https://www.moi.go.th/` and Department of Local Administration (DOLA) `https://www.dla.go.th/`.

**Example calculation** (Bangkok, secondary residence, 8M THB appraised value):
- 8,000,000 × 0.0002 = **1,600 THB/yr** (~$45/yr) — modest by international standards.
- Same condo at 80M appraised: 50M × 0.0002 + 25M × 0.0003 + 5M × 0.0005 = 10,000 + 7,500 + 2,500 = **20,000 THB/yr** (~$570/yr).

### Transaction taxes (one-time at purchase, paid at DOL transfer)

| Tax | Rate | Base | Who pays |
|---|---|---|---|
| **Transfer fee** (ค่าธรรมเนียมการโอน) | 2 % | Treasury appraised value | Negotiable; often split 50/50 buyer/seller; foreign-buyer condo transfers often borne by buyer |
| **Specific Business Tax (SBT, ภาษีธุรกิจเฉพาะ)** | 3.3 % (incl 10 % municipal surtax) | Sale price OR appraised, whichever higher | Seller if held < 5 yrs OR seller is a corporate / developer |
| **Stamp duty** (อากรแสตมป์) | 0.5 % | Sale price OR appraised, whichever higher | Seller — only if SBT does NOT apply (mutually exclusive with SBT) |
| **Withholding tax** (ภาษีเงินได้หัก ณ ที่จ่าย) | Individual seller: progressive (per holding period & §50 formula); Corporate seller: 1 % of appraised | Sale price | Seller |

> **Cabinet stimulus measure (Royal Decree under MoI, 22 Apr 2025 – 30 Jun 2026)**: transfer fee 2 % → **0.01 %** and mortgage registration fee 1 % → **0.01 %** for residences ≤ **7,000,000 THB** (raised from the earlier 3M cap). **Applies to Thai nationals only** — **foreign buyers continue to pay the statutory 2 % transfer fee** and are excluded from this reduction (2026-05-27 verified, source: Royal Gazette + Forbes & Partners 2025/2026 guide). **Renewed 1 Jul 2026 – 30 Jun 2027**: two MoI notifications dated 30 Jun 2026, published in the Royal Gazette 1 Jul 2026 — same 0.01 % transfer + 0.01 % mortgage rates, sale price and appraised value ≤ 7,000,000 THB and mortgage ≤ 7,000,000 THB, individual Thai nationals only; WHT / SBT / stamp duty unchanged (2026 data, source Department of Lands `https://www.dol.go.th/kabinburi/press-release/news-1782960944`). Verify any renewal after 30 Jun 2027 at `https://www.dol.go.th/`.

**Worked example** — foreign buyer of a 10M THB Bangkok condo from a Thai individual seller (held 7 yrs, no SBT):
- Transfer fee: 10M × 2% = 200,000 THB (often split → 100,000 buyer + 100,000 seller)
- Stamp duty: 10M × 0.5% = 50,000 THB (seller)
- Withholding: ~varies, est. 100,000–300,000 THB (seller)
- **Buyer side total**: ~100,000 THB (1 % of price) + lawyer fees ~150,000 THB (~1.5%) = **~2.5 % of price**.

> If buyer agrees to pay all transfer fees (common in foreign-buyer transactions to make the deal happen): **~3.5 % all-in transaction cost** to the buyer.

### Inheritance & gift tax

- **Inheritance Tax Act BE 2558 (2015)**, effective 1 February 2016.
  - Threshold: **100M THB net estate** per beneficiary (cumulative)
  - Rate: **5 % for direct descendants/ascendants**, **10 % for others**
  - Source: Revenue Department `https://www.rd.go.th/english/`
- **Gift Tax** (amendment to Revenue Code 2015):
  - Direct family: 20M THB/yr/donor exempt; excess at 5 %
  - Other: 10M THB/yr/donor exempt; excess at 5 %

### Future risk

- **Land + Building Tax temporary reduction** is **episodic, not an automatic annual renewal** (90% 2020–2021; ~15% 2023; **none for 2026/BE 2569 — full statutory rates apply**); verify any 2027/BE 2570 Royal Decree.
- Periodic Cabinet discussions on raising the rate ceiling (currently 3% for vacant land); none enacted.
- Transfer-fee reduction (0.01% transfer + 0.01% mortgage for residences ≤ 7M THB, individual Thai nationals only) renewed 1 Jul 2026 – 30 Jun 2027 (2026 data, source Department of Lands) — verify any renewal after 30 Jun 2027.

### Confidence

**HIGH** for the statutory framework (Act + Royal Decrees + Revenue Code citations are authoritative). **MEDIUM** for current 2026 effective rates because of Cabinet temporary-reduction renewals; verify current Royal Gazette before quoting an exact rate to a buyer.

---

## Section: `--rental`

### Long-term residential rental income tax

**Personal income tax (PIT) — Revenue Code §40(5)** rental income:
- Thai-resident landlord: progressive PIT 0–35 % (2026 brackets, per Revenue Department):
  - 0–150,000 THB: exempt
  - 150,001–300,000: 5%
  - 300,001–500,000: 10%
  - 500,001–750,000: 15%
  - 750,001–1,000,000: 20%
  - 1,000,001–2,000,000: 25%
  - 2,000,001–5,000,000: 30%
  - > 5,000,000: 35%
- Non-resident landlord (foreigner not in TH ≥ 180 days/yr): also progressive but no personal allowances, or 15% withholding by tenant if treaty/regulation applies.
- **Expense deduction**: standard 30 % (ค่าใช้จ่ายเหมา) OR actual expenses (อัตราค่าใช้จ่ายตามจริง — needs receipts).
- **Filing forms**: ภ.ง.ด. 90 (resident with multiple income types) / ภ.ง.ด. 91 (resident salary-only — not for rental); deadline 31 March year +1; e-filing extended to 8 April. Source: `https://www.rd.go.th/`

**Withholding tax**:
- If tenant is a **corporate entity** (company renting for staff / office): tenant withholds **5 %** of rent and remits to Revenue Department. Landlord credits this against final PIT.
- If tenant is an **individual**: no withholding; landlord declares full income.

### Short-term rentals (Airbnb / Booking / Agoda)

**The headline rule**: under the **Hotel Act BE 2547 (2004)** §4 and Ministerial Regulations, **renting a place for stays of less than 30 nights without a hotel license is illegal**. **Ministerial Regulation BE 2566 (2023)** broadened the **non-hotel exemption to properties with ≤ 8 rooms / ≤ 30 guests** (raised from the earlier ≤ 4 rooms / ≤ 20 guests under BE 2551); hosts must notify the District Office and obtain a **Certificate of Non-Hotel Status / Certificate of Exemption** — does NOT override condo juristic-person bylaws which typically still forbid <30-day lets (2026-05-27 verified, source: DOPA Ministerial Regulation BE 2566). Source: `https://www.dopa.go.th/` (Department of Provincial Administration administers Hotel Act).

**Practical reality**:
- **Most condo juristic person regulations forbid daily/weekly letting**, regardless of Hotel Act. Verify the project's bylaws BEFORE buying with STR intent.
- **Hotel licensing is onerous**: requires building-code compliance for hotel use, fire/safety inspection, separate hotel-zoned land use; condos typically cannot be retrofitted.
- **Enforcement intensity varies**:
  - **Bangkok / Hua Hin / Krabi**: stricter; raids and fines reported 2023–2025; condo juristic persons actively monitor and report STR listings.
  - **Phuket / Pattaya / Koh Samui**: variable; some buildings tolerate STR; tourist-zone authorities sometimes look the other way until a complaint is filed.
  - **Chiang Mai**: mixed; condo-by-condo enforcement.
- **Penalties**: Hotel Act §59 — fine up to 20,000 THB + 10,000 THB/day continuing + imprisonment up to 1 year.
- **Workaround often advertised but legally fragile**: 30+ night minimums (genuine monthly let) are outside the Hotel Act and generally permitted; week-long lets are illegal absent a hotel license.

**2024–2026 watch**: two draft accommodation-reform bills are now under **Council of State public consultation** — a **Draft Accommodation Establishments Act** (would repeal and replace the Hotel Act entirely, and would let condominium units be legally used for short-term accommodation by registration, without a full hotel licence) and a **Draft Hotel & Non-Hotel Accommodation Act**. Both are **NOT enacted as of 2026-07** — the <30-night illegality above is unchanged. **Viral property-marketing claiming STR is 'already legalised' in condos is false** (the bills are draft/consultation only). Verify via `https://www.moi.go.th/` and Cabinet Resolution database (2026-07-02 verified, source: AMCHAM Thailand Feb 2026 + Formichella & Sritawat Jun 2026).

**Tax treatment if you do legally STR via hotel license / monthly lets**:
- Standard PIT §40(5) applies; 30 % deemed expense or actual.
- VAT (ภาษีมูลค่าเพิ่ม / VAT 7 %) applies if turnover > 1.8M THB/yr.
- Local hotel tax (ภาษีโรงแรม) may apply per provincial ordinance.

### Strategic notes

- **Bangkok central condos**: long-term yields ~3–5 % gross; STR explicitly forbidden by most premium-building juristic persons.
- **Phuket / Pattaya / Samui beachfront**: STR yields theoretically high (est. ~7–12 % gross in peak season — foreign-buyer listing-platform estimates, verify against realized REIC/Hipflat transfer data) but legal exposure and management complexity; many buyers use developer-managed rental pool with hotel license as the workaround.
- **Hua Hin**: long-term lets to Thai retirees / expats; ~4–6 % gross.
- **Chiang Mai**: digital-nomad demand strong; long-stay (1–3 month) lets dominant; condo juristic persons increasingly forbid sub-30-day.
- **Koh Phangan / Koh Tao**: irregular tourist economy; high seasonality.

### Confidence

**HIGH** for Hotel Act and PIT statutory framework. **MEDIUM** for STR enforcement intensity (varies by province/year/political climate). **MEDIUM** for current condo juristic person bylaw landscape (project-specific; verify each project's rules in writing).

---

## Section: `--work=<profession>`

### Job platforms

- **JobsDB Thailand**: `https://th.jobsdb.com/` (SEEK group, largest)
- **JobThai**: `https://www.jobthai.com/` (Thai-language dominant)
- **LinkedIn Thailand**: very active in tech, finance, multinationals, Bangkok-centric
- **Glassdoor Thailand**: `https://www.glassdoor.com/Job/thailand-jobs-SRCH_IL.0,8_IN211.htm`
- **ThaiJobsGov / กรมการจัดหางาน (Department of Employment)**: `https://www.doe.go.th/`
- **NationJobs, Jobtopgun, Adecco TH**

### Work permit & visa

**Foreign nationals working in Thailand require a work permit (ใบอนุญาตทำงาน)** issued by the Department of Employment, Ministry of Labour (`https://www.doe.go.th/`). Work permits are tied to:

1. A specific employer
2. A specific job description
3. A specific work location

**Restricted occupations**: under the **Emergency Decree on Managing the Work of Aliens B.E. 2560 (2017), as amended** (พระราชกำหนดการบริหารจัดการการทำงานของคนต่างด้าว พ.ศ. 2560 — this replaced the Alien Employment Act B.E. 2521 (1978)) and the Ministry of Labour notification on work prohibited to foreigners, **40 works are specified: 27 absolutely closed to foreigners and 13 open subject to conditions** (List 2 — accounting, engineering and architecture, only under an international agreement binding Thailand; List 3 — craft/semi-skilled work, employer required; List 4 — labouring and shop-sales work, employer required and entry under a government-to-government MOU). Absolutely closed works include wood carving, motor-vehicle driving (forklift driving excepted), auctioneering, **brokerage and agency work — which closes real-estate brokerage to foreigners**, tour-guiding, hairdressing/beautician work, Thai massage, Thai musical-instrument making, Buddha-image making and legal services (2026 data, source Ministry of Labour / Department of Employment; 2026-09-18 verified). Full list: `https://www.doe.go.th` (verify current list — periodically updated).

### Visa pathways relevant to property buyers

| Visa | Duration | Income/asset threshold | Tax benefit | Real-estate angle |
|---|---|---|---|---|
| **LTR — Wealthy Global Citizen** | 10 yr | USD 1M assets, USD 80k/yr income, USD 500k investment in TH (incl. real estate ≥ 5M THB or Thai government bonds) | Foreign-source income tax-exempt while LTR; flat 17% PIT for LTR-WHT employment | Direct: real estate counts toward the USD 500k investment requirement |
| **LTR — Wealthy Pensioner** | 10 yr | USD 80k/yr passive income (or USD 40k + 250k investment) age ≥ 50 | Same | Indirect |
| **LTR — Work-from-Thailand Professional** | 10 yr | USD 80k/yr employment income from foreign employer with USD 150M revenue (or 50M for some) | Same | Indirect |
| **LTR — Highly Skilled Professional** | 10 yr | USD 80k/yr employment + targeted-industry employer (BoI list) | Flat 17 % PIT | Indirect |
| **Thailand Privilege (formerly Elite)** | 5–20 yr depending on tier | 900,000 THB (Gold 5-yr) up to 5,000,000 THB (Reserve 20-yr) | NO direct tax benefit | Convenience visa; no work right; NOT a route to ownership |
| **DTV (Destination Thailand Visa)** | 5 yr multi-entry, 180 days/stay | 500,000 THB savings (≈ USD 14,300) | None | Aimed at digital nomads / freelancers; renewable; no work permit required |
| **Non-O Retirement** | 1 yr (renewable) | 65+; THB 800,000 in Thai bank OR THB 65,000/mo income | None | No work right; allows long-stay |
| **SMART Visa** | up to 4 yr | Tech / R&D specialist; income threshold; BoI-approval | Various | Targeted at tech sector |

- **LTR Visa portal**: `https://ltr.boi.go.th/`
- **Thailand Privilege**: `https://thailandprivilege.co.th/`
- **DTV**: applied via Royal Thai Embassies / e-Visa portal `https://www.thaievisa.go.th/`
- **Source for the rules**: Immigration Bureau `https://www.immigration.go.th/` and Royal Decrees per visa.

### Self-employment / freelance reality

- A freelance foreigner in Thailand still legally needs a work permit. The **DTV** allows long stays for "remote work for foreign employers/clients" — but enforcement of work-permit requirements for purely-remote work remains gray; recent (2024–2025) MoFA guidance has loosened this for DTV holders.
- **No simple "auto-entrepreneur" / Kleinunternehmer equivalent** exists in Thailand for foreigners. A foreigner running a Thai-incorporated business needs work permit + corporate tax compliance + capital adequacy (commonly 2M THB registered capital per work permit).

### Salary benchmarks (Bangkok 2025–2026)

| Role | Median monthly gross THB | USD est. (35 THB/USD) |
|---|---:|---:|
| Software engineer (mid-senior, MNC) | 80,000–180,000 | $2,300–$5,150 |
| English teacher (degree, certified) | 40,000–70,000 | $1,150–$2,000 |
| Hotel mgmt (mid) | 60,000–120,000 | $1,710–$3,430 |
| Bangkok median (all sectors) | ~25,000 | ~$715 |
| **Minimum wage 2026** (varies by province; Bangkok) | ~10,800/mo (363 THB/day × ~30) | ~$310 |

Sources: NSO Thailand `http://www.nso.go.th/`, Ministry of Labour, JobsDB salary surveys.

### Confidence

**HIGH** for visa thresholds and work permit framework (BoI / Immigration sources). **MEDIUM** for restricted-occupation list (regulations updated periodically — verify current text). **MEDIUM** for salary benchmarks (large MNC vs SME variance).

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **DDPM (กรมป้องกันและบรรเทาสาธารณภัย)** | `https://www.disaster.go.th/` | Hazard maps, disaster declarations, flood/landslide history |
| **TMD (กรมอุตุนิยมวิทยา)** | `https://www.tmd.go.th/` | Weather/climate, monsoon, tropical-cyclone tracking, climate-projection products |
| **GISTDA (สทอภ. — Geo-Informatics and Space Technology)** | `https://www.gistda.or.th/` | Satellite-based flood mapping, land-use, sea-level monitoring |
| **DMR (กรมทรัพยากรธรณี — Dept. of Mineral Resources)** | `https://www.dmr.go.th/` | Geology, landslide & earthquake hazard mapping |
| **Royal Irrigation Department (กรมชลประทาน)** | `https://www.rid.go.th/` | Floodplain & dam release data |
| **Pollution Control Department (กรมควบคุมมลพิษ)** | `https://www.pcd.go.th/` | Air quality, water quality, AQ index |
| **NDWC (National Disaster Warning Center)** | `https://ndwc.disaster.go.th/` | Tsunami warning + Andaman coast sirens |
| **Office of Natural Resources & Environmental Policy & Planning (ONEP)** | `https://www.onep.go.th/` | Climate-change adaptation strategy, EIA |

### Flood (น้ำท่วม)

- **Bangkok metropolitan**: legacy of 2011 floods (worst in 50 years; CBD partially flooded; estimated USD 46B economic losses — World Bank 2012). Subsequent BMA flood-defence investments (king's tunnels / Chao Phraya barrier upgrades) — partial mitigation only.
- **Annual monsoon floods**: October–November (Northeast monsoon retreat) — Chao Phraya basin, Northeast (Khorat plateau), Northern provinces (Chiang Rai 2024 flooded; Chiang Mai 2024 flooded).
- **Bangkok subsidence**: city sinks ~1–3 cm/yr in some districts (heavy groundwater abstraction historically + delta sediment compaction). Combined with sea-level rise 3–5 mm/yr, parts of inner Bangkok could be regularly inundated by mid-century. Source: GISTDA + Chulalongkorn University monitoring; ONEP National Adaptation Plan 2022.
- **Flood maps**: GISTDA flood-extent products (post-event mapping) at `https://disaster.gistda.or.th/flood`. DDPM hazard zones at provincial PAO (อบจ.) level.
- **Verdict bands**:
  - 🔴 Bangkok low-lying (Bang Khae, Min Buri, Lat Krabang east, Bang Phlat riverbank) + Lower Chao Phraya delta + central plain
  - 🟠 Bangkok inner-mid (Sukhumvit, Sathorn, Silom — protected by king's tunnels but 2011 flooding reached parts)
  - 🟡 Bangkok upper-elevation (Chatuchak, Lat Phrao, Ramkhamhaeng higher ground)
  - 🟢 Hilly upcountry (Chiang Mai elevated districts, Phuket interior, Hua Hin foothills)

### Tsunami (สึนามิ)

- **Andaman coast** (Phuket, Krabi, Phang Nga, Ranong, Trang, Satun) — 2004 Indian Ocean tsunami killed ~5,400 in Thailand; epicenter off Sumatra.
- Post-2004 mitigation: NDWC tsunami towers + sirens along Andaman coast; warning protocol DEWS.
- Property risk: any Andaman beachfront ≤ 10 m elevation within 500 m of shoreline = high tsunami risk. New construction post-2004 typically required higher first-floor habitable level for hotels but residential discretion varies.
- **Gulf of Thailand** (Pattaya, Hua Hin, Koh Samui): much lower tsunami risk because Sunda Trench source is shielded by Malay peninsula. Local microtsunami (storm surge + earthquake combination) theoretically possible but no historical major event.

### Seismicity (แผ่นดินไหว)

- Most of Thailand: low-to-moderate seismic risk.
- **Higher-risk fault zones** (per DMR active-fault map, `https://www.dmr.go.th/`):
  - **Mae Chan fault** (Chiang Rai): M 6.3 in 2014 (Mae Lao earthquake)
  - **Mae Tha / Mae Hong Son** Northern fault zones
  - **Three Pagodas fault** (Kanchanaburi border)
  - **Ranong fault** (Andaman onshore extension)
- Bangkok: low seismic source but **soft-soil amplification** — distant earthquakes (Myanmar 2025 Mandalay M 7.7 was felt strongly in Bangkok skyscrapers, prompting renewed scrutiny of high-rise compliance with EIT seismic code Mw 0027-50). Verify any Bangkok high-rise post-2007 was built to Engineering Institute of Thailand (EIT) seismic standard.
- **2025 reform watch**: post-Myanmar 2025 quake, Department of Public Works & Town Planning announced review of high-rise seismic code for Bangkok — verify current status at `https://www.dpt.go.th/`.

### Air quality (PM2.5)

- **Northern Thailand** (Chiang Mai, Chiang Rai, Mae Hong Son): severe seasonal smog Feb–Apr (crop-residue burning + Myanmar/Laos transboundary smoke). PM2.5 routinely 150–300+ µg/m³ — WHO 24-hr guideline 15 µg/m³.
- **Bangkok**: chronic PM2.5 from traffic + industrial; winter-inversion (Dec–Feb) episodes 80–150 µg/m³.
- Source: PCD AQ monitoring `http://air4thai.pcd.go.th/`

### Climate-change projections (TMD + IPCC AR6 + ONEP)

- **Temperature**: +1.5–3.0 °C by 2050 vs 1986–2005 baseline (RCP4.5 → RCP8.5). Source: TMD downscaled CMIP6, IPCC AR6 Atlas.
- **Sea-level rise**: +20–60 cm by 2100 (conservative SSP1-2.6 → high SSP5-8.5). Andaman + Gulf coasts both exposed; Bangkok delta combined with subsidence = compound risk.
- **Extreme rainfall**: Southern monsoon and tropical-cyclone-derived events expected to intensify; 2024 Phuket flash floods are early signal.
- **Drought**: NE Thailand dry-season severity increasing; affects rural land values.
- **Coral reef bleaching**: Andaman + Gulf — affects Phuket/Krabi/Samui tourism economy long-term, indirect impact on STR yields.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1992** (no modern building code consistently enforced) | Unreinforced masonry, asbestos in roofing/sheet, lead pipes, weak foundations on alluvial soil |
| **1992–2007** (Building Control Act 1979 + early reforms) | Variable quality; many small contractors; asbestos still permitted in some products |
| **Post-2007** (EIT seismic & wind code 0027-50, modernized fire code) | Better; high-rises in Bangkok post-2007 generally to seismic standard |
| **Post-2020** (ECON Energy code, BCG green-building incentives) | Modern energy + safety; rising green-building certifications (TREES, EDGE, LEED) |

### Mandatory pre-purchase diagnostics

| Document | Required because | Where |
|---|---|---|
| **Title deed verification** (Chanote / nor sor 3 gor) | All sales — verify chain of title, no encumbrances | DOL provincial office (in person, in Thai) |
| **Land office encumbrance search** (ภาระติดพัน) | Mortgages, leases, usufructs, court orders | DOL provincial office |
| **Construction permit (ใบอนุญาตก่อสร้าง)** | Verify the building was permitted | Local OBT / municipal office |
| **Occupancy permit (ใบรับรองการใช้อาคาร)** | Confirm legal occupancy | Local OBT |
| **Foreign Quota Certificate** (condo) | Confirm unit is in foreign 49% quota | Project's juristic person |
| **Juristic person debt clearance** (ใบปลอดหนี้) | No unpaid common-area fees / sinking fund | Juristic person |
| **House Registration (ทะเบียนบ้าน, blue book)** | Confirms address; not ownership | Amphoe / khet office |
| **FET / Tor Tor 3 (foreign buyer only)** | Mandatory for DOL transfer | Receiving Thai bank issues at remittance |
| **Land survey** (รังวัด) | Especially for villas / land — verify boundaries match Chanote | DOL surveyor or licensed private surveyor |

**Foreign buyers should commission a Thai-licensed real-estate lawyer for the title and encumbrance verification — DIY is not feasible because all DOL records are in Thai.**

### Confidence

**HIGH** for flood / tsunami / Bangkok subsidence (multiple primary sources). **MEDIUM** for seismic risk (post-2025-Myanmar code review pending). **MEDIUM** for build-era hazards (variable enforcement history).

---

## Section: `--mains`

### Water supply

- **MWA (Metropolitan Waterworks Authority, การประปานครหลวง)** — covers Bangkok, Nonthaburi, Samut Prakan only. `https://www.mwa.co.th/`
- **PWA (Provincial Waterworks Authority, การประปาส่วนภูมิภาค)** — covers all other provinces (74 of 77). `https://www.pwa.co.th/`
- **Local municipal waterworks** — small cities sometimes operate own systems
- **Rural**: many villages on shallow well + storage tank; quality variable

### Sewer / wastewater

**Thailand has limited mains-sewer coverage compared to OECD baselines.**

- **Bangkok**: BMA estimates ~50–60 % of generated wastewater is centrally collected and treated (BMA Drainage & Sewerage Dept, `https://dds.bangkok.go.th/`). Older / outer districts often on individual septic + soakaway.
- **Provincial cities**: coverage drops sharply outside provincial seats. Most condo developments use **on-site treatment** (อาคารบำบัดน้ำเสียในตัวอาคาร) per Building Control Act ministerial regulation requiring on-site treatment for buildings > 500 sqm.
- **Rural / villa areas (Phuket, Samui, Hua Hin, Chiang Mai outskirts)**: septic tank + soakaway is the norm. Modern villas typically have **3-stage septic + soakaway field**; older may have simple cesspit (บ่อเกรอะ).
- **Wastewater regulator**: Pollution Control Department `https://www.pcd.go.th/` and Office of Wastewater Management (provincial level).

### Verification path

1. Listing language scan:
   - "ระบบสุขาภิบาลส่วนกลาง" / "เชื่อมต่อท่อระบายน้ำ" = mains drainage
   - "ระบบบำบัดน้ำเสียในตัวอาคาร" = on-site building treatment (typical condo)
   - "บ่อเกรอะ" / "บ่อซึม" = septic tank + soakaway
2. **Bangkok**: call MWA (1125) for water; BMA Drainage Dept for sewer (specific to district).
3. **Province**: call PWA hotline (1662) for water; provincial municipal office or SAO for sewer.
4. **Phuket / Samui / Pattaya villas**: assume septic; confirm tank size + last desludge date with seller; verify soakaway not failing.

### Cost benchmarks

| Scenario | Cost (THB) |
|---|---:|
| Standard condo connection / monthly fee | 30–100 THB/sqm/month common-area incl. water+wastewater |
| Septic install (3-stage, modern, villa) | 80,000–250,000 |
| Septic upgrade / soakaway redo | 50,000–150,000 |
| Sewer-line connection (where mains available) | 30,000–100,000 + monthly fees |
| Mains water connection (PWA / MWA new) | 5,000–15,000 |

### Confidence

**HIGH** for the MWA/PWA institutional structure. **MEDIUM** for parcel-level coverage (sewer particularly variable; verification often requires telephone the local authority).

---

## Cost benchmarks (TH 2026)

| Item | Cost (THB) | USD est. |
|---|---:|---:|
| **Lawyer fees (foreign buyer condo)** | 50,000–200,000 (or 1–2 % of price) | $1,400–$5,700 |
| **Lawyer fees (foreign buyer villa, lease/company)** | 150,000–500,000+ (more complex structure) | $4,300–$14,300+ |
| **Title verification (Chanote search)** | 5,000–15,000 | $140–$430 |
| **Building inspector (condo)** | 5,000–20,000 | $140–$570 |
| **Building inspector (villa)** | 10,000–50,000 | $290–$1,430 |
| **Land surveyor (private licensed)** | 5,000–30,000 | $140–$860 |
| **DOL transfer fee** | 2 % of appraised | varies |
| **Stamp duty** | 0.5 % | varies |
| **SBT (if applicable)** | 3.3 % | varies |
| **Withholding tax (corp seller)** | 1 % appraised | varies |
| **Common-area fees (condo, mid-range)** | 30–100 THB/sqm/month | $1–$3/sqm/mo |
| **Common-area fees (luxury condo, Bangkok)** | 80–200 THB/sqm/month | $2–$6/sqm/mo |
| **Sinking fund (one-off, at handover)** | 500–1,000 THB/sqm | $14–$29/sqm |
| **Typical condo refurb (60 sqm full)** | 400,000–1,200,000 | $11,400–$34,300 |
| **Villa pool maintenance (incl. chemicals)** | 3,000–6,000 THB/mo | $86–$170/mo |
| **Annual property tax (residential, ≤ 50M appraised)** | 0–10,000 typical | $0–$285 |
| **Total transaction cost (foreign buyer, all-in)** | ~3–5 % of price | — |

---

## Active fiscal incentives (2026)

- **BOI (Board of Investment) — residential**: rare; only for ultra-high-net-worth or industrial-residential mixed projects. `https://www.boi.go.th/`
- **LTR Visa — tax incentives**:
  - Foreign-source income tax-exempt while LTR (for Wealthy Global Citizen / Pensioner / Work-from-Thailand categories)
  - Flat 17 % PIT for LTR Highly Skilled Professional (employment income only)
- **Thailand Privilege**: NO tax incentive; visa convenience only
- **BCG (Bio-Circular-Green) building incentives**: corporate tax deduction for green-certified construction; minor at the residential level
- **EV charger incentives**: VAT exemption + corporate tax credit for installing chargers (commercial / mixed-use); residential charger rebates limited
- **DTV holders**: no Thai-sourced tax exemption; **Por.161/2566 + Por.162/2566** (Revenue Department orders effective 1 Jan 2024) abolished the same-calendar-year remittance loophole — foreign-source income remitted to Thailand in any later year is taxable; **Por.162/2566 explicitly carves out** the new rule to apply ONLY to foreign-source income derived **on or after 1 January 2024** (pre-2024 foreign income remitted in 2024+ remains exempt). A 2025 draft 2-year relief proposal is being considered but is **not yet enacted** as of Jun 2026 — pending Cabinet approval + Council of State review + Royal Gazette publication (2026-07-02 re-verified, source: Rumavi + Acclime + Chambers 2026).

---

## Common listing platforms

- **DDProperty** — `https://www.ddproperty.com/` — largest, English+Thai, all segments
- **FazWaz** — `https://www.fazwaz.com/` — foreign-buyer focused, Phuket / Pattaya / Samui / Bangkok
- **Hipflat** — `https://www.hipflat.co.th/` — Bangkok condo specialist, sold-price overlays
- **Lazudi** — `https://www.lazudi.com/`
- **Thailand-Property.com** — `https://www.thailand-property.com/`
- **Bangkok Post Property** — `https://property.bangkokpost.com/`
- **Livinginsider** — `https://www.livinginsider.com/` (Thai-language)
- **PropertyHub88** — `https://www.propertyhub88.com/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Thai portal (propertyhub.in.th — verify)

---

## Caveats unique to TH

- **Foreign land ownership prohibition is strict and unmoving** — Land Code §86 has stood since 1954; the only freehold option is condominium within 49% quota.
- **"30 + 30 + 30" leases are not 90-year leases** — only the first 30 years is legally enforceable; renewals are contractual options that may be unenforceable against successor landowners.
- **Thai company nominee structures are actively prosecuted** — DBD/DOL crackdown 2023+; do not rely on this path for residential foreign holding.
- **Chanote (โฉนด) is the only safe title for foreign buyers** — Nor Sor 3, Sor Kor 1, Por Bor Tor 5 should be hard-rejected.
- **49 % foreign quota verification is non-negotiable** — get the Foreign Quota Certificate in writing before paying any deposit.
- **STR (Airbnb) is generally illegal under the Hotel Act** for stays < 30 nights; condo juristic persons typically forbid; enforcement varies by province but the legal exposure is real.
- **Bangkok subsidence + sea-level rise** = compound flood-risk for low-lying inner districts; insurance pricing is increasingly reflecting this.
- **Visa-linked property structures** (e.g., "buy a condo, get a visa") do NOT exist in Thailand as a real-estate-linked golden visa; LTR rewards a USD 500k investment that can include real estate but the visa is not parcel-linked.
- **FX requirement (FET/Tor Tor 3)** for foreign condo buyers is mandatory at DOL transfer — funds must be remitted from abroad in foreign currency and converted in Thailand.
- **All title documents are in Thai** — sworn translation + Thai-licensed lawyer are mandatory for foreign buyers; do not skip.
- **New condo from reputable developer is often cleaner than resale** because the foreign quota is set at registration and the developer reserves foreign units; resale requires verifying the unit is back in the foreign quota.
- **Bangkok high-rise seismic compliance** under post-2007 EIT code is good in principle; pre-2007 high-rises (esp. 1990s boom) may have variable compliance — relevant after the 2025 Myanmar quake felt strongly in Bangkok.

---

## Reddit / forum sources

- **r/Thailand** — active general
- **r/ThailandTourism**, **r/Bangkok**, **r/ChiangMai**, **r/Phuket**
- **r/ThaiVisa** — visa & long-stay focused
- **ThaiVisa.com forum** (now ASEAN Now): `https://aseannow.com/` — long-running expat forum, many real-estate threads
- **Bangkok Post Forum**: `https://www.bangkokpost.com/`
- **Thaiger forums**: `https://thethaiger.com/`
- **Pattaya forums** (PattayaUnplugged, Stickman) — older, anecdotal
- ⚠️ Forum-quality caveat: many anecdotes about "my friend bought via company structure and it was fine" — but the legal exposure has shifted significantly since 2023 enforcement; treat older forum threads as outdated.

---

## Verification authorities

| Authority | When to call | Contact |
|---|---|---|
| **Department of Lands (DOL) — provincial office** | Title verification, encumbrance search, transfer registration | Search by province at `https://www.dol.go.th/` |
| **Treasury Department (กรมธนารักษ์)** | Appraised value lookup | `https://assessprice.treasury.go.th/` |
| **Revenue Department (กรมสรรพากร)** | Tax filings, withholding, VAT | `https://www.rd.go.th/` |
| **Immigration Bureau (ตม.)** | Visa, 90-day reporting, residence | `https://www.immigration.go.th/` |
| **BoI Board of Investment** | LTR Visa, BoI promotions | `https://www.boi.go.th/`, LTR `https://ltr.boi.go.th/` |
| **Bank of Thailand (BOT)** | FX rules, FET form, capital flows | `https://www.bot.or.th/` |
| **Ministry of Interior (MoI)** | Hotel licensing, provincial governance | `https://www.moi.go.th/` |
| **Department of Provincial Administration (DOPA)** | House registration, ID, hotel act administration | `https://www.dopa.go.th/` |
| **Department of Business Development (DBD)** | Company registration, anti-nominee | `https://www.dbd.go.th/` |
| **Department of Public Works & Town Planning (DPT)** | Building code, zoning | `https://www.dpt.go.th/` |
| **DDPM (Disaster Prevention)** | Flood / hazard maps | `https://www.disaster.go.th/` |
| **TMD (Meteorology)** | Climate / monsoon | `https://www.tmd.go.th/` |
| **GISTDA** | Satellite flood / land-use | `https://www.gistda.or.th/` |
| **Pollution Control Dept (PCD)** | Air & water quality | `https://www.pcd.go.th/` |
| **Provincial appraisal office** | Local market context | per province |

---

## Quirks to know

- **Chanote vs Nor Sor**: never accept anything less than Chanote (Nor Sor 4 Jor) for foreign-buyer transactions; Nor Sor 3 Gor is acceptable only for Thai-nominee/spouse paths and only if upgrade to Chanote is feasible.
- **Foreign Quota Certificate** for condo: get it in writing, signed by the juristic person manager, BEFORE paying deposit. If the unit isn't in foreign quota, no DOL transfer will happen.
- **Juristic person (นิติบุคคลอาคารชุด)**: the condo's management entity, established under §35 Condominium Act. Manages common areas, fees, sinking fund, foreign quota tracking. AGM (annual general meeting) participation rights for owners.
- **Thai company nominee risk**: Land Code §96bis active enforcement; do not assume historical "everyone does it" still applies. As of 2024 DBD circular, anti-nominee referrals to police have intensified.
- **30-year lease registration at DOL is essential** — an unregistered lease > 3 years is unenforceable against subsequent landowners and not opposable to third parties; pay the est. ~1.1% registration fee + stamp duty est. ~0.1% on the lease value (verify current rates with DOL / Revenue Department before budgeting).
- **Stamp duty quirks**: SBT and stamp duty are mutually exclusive on a single sale (whichever applies); double-payment is a common error to avoid.
- **Usufruct (สิทธิเก็บกิน)** vs **superficies (สิทธิเหนือพื้นดิน)** vs **habitation (สิทธิอาศัย)**: three distinct registered rights at DOL; useful for foreign-spouse or family arrangements but NOT for arms-length purchase.
- **LTR vs Privilege vs DTV**: LTR = best tax + duration but high asset bar; Privilege = pure visa convenience, no tax benefit, mid-cost; DTV = cheapest, designed for digital nomads, no work-permit but 180-day stays.
- **House Registration (ทะเบียนบ้าน, blue book / yellow book for foreigners)**: not proof of ownership but required for many administrative services; foreigners get a yellow book (ทร.13) — separate from the property title.
- **Selling back as a foreigner**: capital gains via withholding (5% individual) on the sale + foreign-currency repatriation requires same FET evidence at outbound transfer; not automatic.
- **Bangkok BTS/MRT proximity premium**: properties within 500 m of a station have historically transacted at an est. ~15–30% premium (per REIC/Hipflat — band undated, verify current spread); verify with the station's actual walking distance (sometimes "near MRT" listings are 1.5 km away).
- **Soi (ซอย) numbering**: Sukhumvit sois have famous numbering quirks — even-numbered sois on south side, odd-numbered on north, and several "Soi 39/1, 39/2" branch sois. Verify exact soi via Google Maps Thai-script search.

---

## Source URL templates

| Source | URL pattern |
|---|---|
| DOL main | `https://www.dol.go.th/` |
| DOL e-Service | `https://eservice.dol.go.th/` |
| LandsMaps GIS viewer | `https://landsmaps.dol.go.th/` |
| Treasury appraised value | `https://assessprice.treasury.go.th/` |
| Treasury Department main | `https://www.treasury.go.th/` |
| Revenue Department | `https://www.rd.go.th/` |
| Royal Gazette (statutes) | `http://www.ratchakitcha.soc.go.th/` |
| Krisdika (Office of the Council of State, statute texts) | `https://www.ocs.go.th/searchlaw` |
| Cabinet Resolution database | `https://resolution.soc.go.th/` |
| Bank of Thailand FX rules | `https://www.bot.or.th/en/our-roles/financial-markets/foreign-exchange-regulations.html` |
| Immigration Bureau | `https://www.immigration.go.th/` |
| BoI main | `https://www.boi.go.th/` |
| LTR Visa portal | `https://ltr.boi.go.th/` |
| Thailand Privilege | `https://thailandprivilege.co.th/` |
| Thailand e-Visa (DTV) | `https://www.thaievisa.go.th/` |
| Department of Employment (work permit) | `https://www.doe.go.th/` |
| Department of Business Development (DBD) | `https://www.dbd.go.th/` |
| Ministry of Interior | `https://www.moi.go.th/` |
| Department of Provincial Administration (DOPA) | `https://www.dopa.go.th/` |
| Department of Public Works & Town Planning (DPT) | `https://www.dpt.go.th/` |
| MWA Bangkok water | `https://www.mwa.co.th/` |
| PWA provincial water | `https://www.pwa.co.th/` |
| BMA Drainage & Sewerage | `https://dds.bangkok.go.th/` |
| Pollution Control Dept (air, water) | `https://www.pcd.go.th/` |
| PCD AQ portal | `http://air4thai.pcd.go.th/` |
| DDPM (disaster) | `https://www.disaster.go.th/` |
| TMD (meteorology) | `https://www.tmd.go.th/` |
| GISTDA (geo / satellite) | `https://www.gistda.or.th/` |
| GISTDA flood viewer | `https://disaster.gistda.or.th/flood` |
| DMR (geology, faults) | `https://www.dmr.go.th/` |
| ONEP (climate adaptation) | `https://www.onep.go.th/` |
| Department of Highways AADT | `https://bhs.doh.go.th/` |
| EXAT (expressways) | `https://www.exat.co.th/` |
| REIC (real estate info) | `https://www.reic.or.th/` |
| AREA (real estate affairs) | `https://www.area.co.th/` |
| DDProperty | `https://www.ddproperty.com/` |
| FazWaz | `https://www.fazwaz.com/` |
| Hipflat | `https://www.hipflat.co.th/` |
| Lazudi | `https://www.lazudi.com/` |
| Thailand-Property | `https://www.thailand-property.com/` |
| Bangkok Post Property | `https://property.bangkokpost.com/` |

---

## Status

✅ **Fully populated** as of 2026-05-01.

**Coverage check**: foreign-buyer eligibility (LEAD), price, traffic, tax, rental, work, risks, mains all sourced to primary government / regulated entity URLs + cost benchmarks + caveats.

**Confidence**:
- **HIGH** — foreign-ownership rules (Land Code §86 + §96bis, Condominium Act §19), Chanote-only requirement, FX/FET requirement, LTR Visa thresholds (BoI primary), DTV (MoFA primary), Land + Building Tax 2019 statutory framework, Hotel Act §4 framing of STR illegality.
- **MEDIUM** — current 2026 transfer-fee rate (Cabinet Royal Decree on temporary reduction renewed annually; verify Royal Gazette before quoting); STR enforcement intensity (varies by province + political cycle); seismic high-rise compliance (post-2025-Myanmar code review pending); anti-nominee enforcement geography (Phuket/Samui higher than Isan).
- **LOW** for none — every section has primary sources.

**Reform watch items** (track in `shared/regulatory-watch.md`):
1. **Long-term lease 99-year extension** — Cabinet 2024 discussion; not enacted May 2026.
2. **Foreign condo quota raise to 75 %** — MoI 2024 proposal; not enacted May 2026; current status not re-verified from a primary source.
3. **Land + Building Tax temporary reduction** — episodic, not an automatic annual renewal (90% 2020–2021; ~15% 2023; none for 2026/BE 2569 — full statutory rates apply); verify any 2027/BE 2570 decree.
4. **STR licensing framework** — Draft Accommodation Establishments Act + Draft Hotel & Non-Hotel Accommodation Act under Council of State public consultation (would let condos register for STR without a full hotel licence); NOT enacted as of 2026-07.
5. **Bangkok high-rise seismic code review** — DPT post-Myanmar 2025; verify current text.
6. **Foreign-source income remittance taxation** — Revenue Department interpretation effective 2024 for non-LTR holders; ongoing clarifications.

**Last verified**: 2026-07-02 (regulatory re-verification — Land & Building Tax: no across-the-board Royal Decree reduction for 2026/BE 2569, full statutory rates apply; STR <30-night illegality under Hotel Act §4 unchanged, Draft Accommodation Establishments Act + Draft Hotel & Non-Hotel Accommodation Act under Council of State consultation but NOT enacted; foreign-source remittance Por.161/2566 + Por.162/2566 operative, 2025 draft 2-yr relief unenacted. Prior 2026-05-27 sweep: Royal Decree 22 Apr 2025–30 Jun 2026 0.01% Thai-only transfer-fee reduction; Hotel Act Ministerial Reg BE 2566 (≤8 rooms/≤30 guests exemption); Por.161 + Por.162 + 1 Jan 2024 cut-off; restricted-occupations statute and the 40/27/13 split corrected 2026-09-18 per Ministry of Labour notification). Transfer-fee renewal to 30 Jun 2027 re-verified 2026-09-24 against the Department of Lands in the October regwatch wave; rental and remittance tracker entries re-checked. Visa tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
