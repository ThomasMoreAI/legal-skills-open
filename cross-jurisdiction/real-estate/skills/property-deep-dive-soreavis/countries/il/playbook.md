# Israel 🇮🇱 — Property Due-Diligence Playbook

ISO2: `il`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

> **🇮🇱 LEAD WARNING — read before any other section.** Israel is a **de facto restricted** market. **~93% of land in Israel is state-owned** and managed by the Israel Land Authority (Reshut Mekarkei Yisrael / RMI / רשות מקרקעי ישראל) on behalf of the State of Israel, the Jewish National Fund (KKL / קק״ל), and the Development Authority. **JNF (KKL) parcels are restricted by charter to Jewish lessees** (subject to ongoing litigation; non-Jewish lessees access KKL-equivalent state parcels via swap). Foreigners can buy private land + non-JNF state-leased land but pay a **non-resident purchase-tax surcharge**. **Active war footing** (Israel-Hamas Oct 2023, under a fragile US-brokered Oct 2025 Gaza ceasefire — the "Yellow Line" — as of July 2026; Israel-Hezbollah ceasefire Nov 2024; plus two Israel-Iran wars — the Jun 2025 "12-Day War" and a 2026 Iran war, ceasefire announced 7 Apr 2026 — whose Iranian ballistic-missile strikes drove the bulk of war-damage claims) — missile/rocket damage is partially covered by the **Property Tax Compensation Fund** (Israel Tax Authority; state-funded), but insurance markets are disrupted and land devaluation is not compensated. Six- to seven-figure decisions in Israel demand a licensed Israeli **עורך דין מקרקעין** (real-estate attorney) and a **שמאי מקרקעין** (licensed appraiser) — non-negotiable. Verify Tabu (Land Registry) AND RMI lease status — Israel runs a **dual title system** and a parcel can be missing from one register while present in the other.

## Country profile

- **Postcode (מיקוד / mikud)**: 7 digits since 2013 (was 5 digits pre-reform). Format `NNNNNNN`. Source: Israel Postal Company `https://www.israelpost.co.il/zip.nsf/demozip` (verify postcode lookup; 7-digit format mandatory for mail since 1 February 2013).
- **Admin levels**: 6 mehozot (מחוזות, districts) → 15 nafot (נפות, sub-districts) → 257 municipalities (רשויות מקומיות / reshuyot mekomiyot — including 77 ערים/cities, 124 מועצות מקומיות/local councils, 54 מועצות אזוריות/regional councils, plus contested-status municipalities in East Jerusalem and the Golan). Counts per CBS Local Authorities table 2024. Source: Central Bureau of Statistics (CBS / הלמ"ס) `https://www.cbs.gov.il/he/publications/Pages/2024/Local-Authorities-in-Israel-2022.aspx`.
- **Population**: ~10.0 million (CBS estimate end-2025; verify at `https://www.cbs.gov.il/he/Pages/default.aspx`). Jewish ~73%, Arab ~21%, Other ~6% (CBS classification).
- **Currency**: ILS (Israeli new shekel, ₪). 1 USD ≈ 3.6–3.8 ILS; 1 EUR ≈ 3.9–4.1 ILS (May 2026 BoI representative rate; FX volatile during wartime — verify at `https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/`). Free-floating; Bank of Israel intervenes only in extreme moves; no capital controls on residents/non-residents for property transactions but FET-equivalent KYC applies under the Anti-Money Laundering Order 5761-2000.
- **Languages**: Hebrew + Arabic (both official in practice; Hebrew dominant in Tabu/RMI/tax filings). English widely used in Tel Aviv and among Anglo Olim; **all registered title documents are in Hebrew** — sworn translation required for non-Hebrew-reading buyers. Source: Basic Law: Israel as the Nation-State of the Jewish People (5778-2018) §4 (sets Hebrew as state language; Arabic as "special status").
- **Cadastre / land registry**: **dual system** —
- **Tabu / Land Registry (לשכת רישום מקרקעין)** — Ministry of Justice; tracks freehold (`חופשי`) and registered leases. Portal: `https://www.gov.il/he/departments/land_registration_and_settlement_of_rights_department` and online inquiries at `https://www.gov.il/he/service/land_registration_extract`. Nesach Tabu (נסח טאבו / title abstract) is ordered online at [gov.il — הפקת נסח טאבו](https://www.gov.il/he/service/land_registration_extract) → [מקרקעין ברשת](https://mekarkein-online.justice.gov.il/voucher/main); **the fee is not published on the authority's page** — it is charged "לפי המחיר המעודכן באתר התשלומים הממשלתי". Tariffs were re-indexed with effect from 1 Jan 2026 under הודעת המקרקעין (אגרות), התשפ"ו-2025 — data not publicly available on the landing page; verify the current amount at the Israeli government payments site / the Authority for Land Registration and Settlement of Rights (2026-09-18 verified).
- **Israel Land Authority / RMI (רשות מקרקעי ישראל)** — administers state-owned land leases (חכירה / hachira). Portal: `https://www.gov.il/he/departments/israel_land_authority`. RMI online services: `https://www.gov.il/he/departments/israel_land_authority`.
- For ~93% of land, BOTH registers must be checked: Tabu shows the registered lease/owner, RMI shows lease terms, capitalization status, and Heskem Hadash conversion eligibility.
- **Title types** (CRITICAL distinction for foreign buyers):

| Type (Hebrew) | English | Foreign use | Notes |
|---|---|---|---|
| **חופשי / chofshi** | Freehold (private land, "Mukdam" / non-RMI parcels) | ✅ acceptable | ~7% of land; concentrated in pre-1948 properties + post-2009 Heskem Hadash conversions in built-up areas |
| **חכירה / hachira** (RMI state-owned) | Long lease, typically 49+49 years | ✅ acceptable (non-JNF parcels) | Capitalized lease fee paid up-front or annually; transferable subject to RMI consent |
| **חכירה JNF/KKL** | JNF / Keren Kayemeth lease | ⚠️ legally restricted to Jewish lessees | Non-Jewish citizens have accessed via state-parcel swap arrangements; ongoing litigation; see Foreign-buyer section below |
| **Heskem Hadash freehold conversion** | "New Agreement" (post-2009 reform) | ✅ acceptable | Converts state-leased built-up plot to chofshi for capitalization fee (חיוב היוון); applies in many residential zones |
| **East Jerusalem / Area C / Golan / Settlement parcels** | Disputed jurisdiction | 🔴 deed status varies; see Quirks | Some parcels registered under Jordanian/Ottoman pre-1967 systems; international-law status contested; do NOT buy without specialist counsel |

- **Major reforms / regulatory landscape** (verify date-stamps in `shared/regulatory-watch.md`):
- **Heskem Hadash (Decision 1185 / החלטה 1185)** — ILA Council Decision 2009 enabling lessees to convert built-up state-leased land to freehold for a capitalization fee. Source: **מאגר החלטות מועצת מקרקעי ישראל** — [apps.land.gov.il/CouncilDecisions](https://apps.land.gov.il/CouncilDecisions/#/main) (search "החלטה 1185" there; the old ILA SharePoint search form has been retired). Subsequent updates via decisions 1370, 1456 etc. — verify currency at [gov.il — רשות מקרקעי ישראל](https://www.gov.il/he/departments/israel_land_authority) (2026-09-18 verified).
- **Land Taxation (Appreciation and Purchase) Law 5723-1963** — חוק מיסוי מקרקעין; Mas Rechisha (purchase tax) + Mas Shevach (appreciation/capital gains tax). Source: Israel Tax Authority `https://www.gov.il/he/departments/topics/real_estate_taxation`.
- **Buyer's tax brackets — non-resident scale** — annual update by Tax Authority (typically 16 January each year, indexed to CBS housing index). Verify current brackets at `https://www.gov.il/he/departments/dynamiccollectors/tax-rates-real-estate-purchase` (page often updated mid-January).
- **Olim 7-year purchase-tax incentive** — Section 12 of the Land Taxation Regulations, anchored in the Aliyah & Integration framework. Source: Ministry of Aliyah & Integration `https://www.gov.il/he/departments/ministry_of_aliyah_and_integration` and Tax Authority guidance.
- **Property Tax Compensation Fund (Israel Tax Authority)** — Property Tax and Compensation Fund Law 5721-1961 (מס רכוש וקרן פיצויים); pays for direct war/missile damage to property (structures + contents up to caps). Source: `https://www.gov.il/en/departments/topics/compensation_fund` and `https://www.gov.il/he/service/online-direct-damage-claim` (Tax Authority portal).
- **Wartime tax measures (2023–2026)**: temporary purchase-tax bracket adjustments under Order 5784; Compensation Fund claim deadlines extended for evacuee zones (Otef Aza, Northern border). Verify currency at Tax Authority and Knesset legislation database `https://main.knesset.gov.il/Activity/Legislation/Pages/default.aspx`.
- **Proposed reforms NOT enacted as of May 2026**: foreign-buyer outright restriction (proposed several times since 2010s, never passed); raising non-resident Mas Rechisha further (in periodic political discussion).

---

## 🇮🇱 LEAD SECTION: Foreign buyer eligibility

### Bottom line

Foreign nationals **may legally purchase residential property in Israel** subject to: (a) the parcel is on private (chofshi) land OR non-JNF state-leased land, (b) higher non-resident purchase-tax brackets apply (no Olim discount), (c) standard AML/KYC source-of-funds documentation, (d) RMI consent if the underlying parcel is state-leased. The de facto restriction is structural — **~93% of land is state-owned and a sub-portion of that is JNF-restricted by charter**. There is no nominee-style workaround: the land is registered to the lessee and RMI/Tabu vet the registration directly.

### State-land monopoly (~93%)

- **Land ownership composition** (per RMI public communications and KKL annual reports — verify currency at `https://www.gov.il/he/departments/israel_land_authority` and `https://www.kkl.org.il/`):
- **State of Israel**: ~70% of total land area
- **Jewish National Fund (JNF / KKL)**: ~12–13%
- **Development Authority (רשות הפיתוח)**: ~10%
- **Combined RMI-managed**: ~93%
- **Private (chofshi)**: ~7%
- **Implication**: when buying residential property in Israel, the contract is overwhelmingly likely to involve a *registered lease on state-owned land* (managed by RMI) rather than a freehold purchase. The owner-of-record on Tabu is the **lessee**, not the underlying landowner.

### Lease structure (חכירה / hachira)

- **Standard term**: 49 years + 49-year renewal option (פרק שני). Capitalized lease (חכירה מהוונת) is the most common modern form — the lessee pays a one-time capitalization fee (~91% of land value as of pre-2009 framework) covering the full 49+49 term.
- **Renewal at end of term**: lessees historically face renegotiation at end-of-term. Pre-2009 the fee structure was opaque; post-2009 framework standardized.
- **Heskem Hadash (New Agreement) — Decision 1185 (2009) and successor decisions**: enables lessees of built-up urban residential parcels to **convert lease to freehold (chofshi) for a capitalization fee**. Eligibility depends on zoning, building density, and parcel type. Verify per-parcel eligibility at RMI office or via authorized appraiser. Source: **מאגר החלטות מועצת מקרקעי ישראל** — [apps.land.gov.il/CouncilDecisions](https://apps.land.gov.il/CouncilDecisions/#/main).
- **Rural / agricultural / non-built-up parcels**: typically NOT eligible for Heskem Hadash conversion; remain on the 49+49 lease framework.

### JNF (KKL) parcels — Jewish-lessee restriction

- **Legal basis**: KKL Charter (Memorandum and Articles of Association of Keren Kayemeth LeIsrael, registered as a charitable corporation in 1907 in the UK; transferred to Israel under the Keren Kayemet LeIsrael Law 5714-1953). Charter specifies land is held "for the benefit of the Jewish People."
- **Practical effect**: KKL-titled parcels are leased only to Jewish lessees. RMI manages KKL land jointly with state-owned land but enforces the charter.
- **Litigation**: HCJ 9205/04 *Adalah v ILA* (2004) and successor cases challenged the JNF restriction as discriminatory. The compromise reached: when a non-Jewish buyer wins a tender on a JNF parcel, RMI swaps that parcel for an equivalent state-owned (non-JNF) parcel from its inventory, allowing the non-Jewish buyer to receive a non-restricted lease while KKL retains an equivalent area. Source: Israeli Supreme Court database `https://supreme.court.gov.il/`.
- **For foreign buyers**: the JNF restriction primarily affects Israeli Arab citizens. Foreign non-Jewish buyers face the same legal swap mechanism in theory but in practice rarely encounter raw JNF parcels in residential markets — most listed urban property is either chofshi or non-JNF state lease.
- **Verification step**: ask the seller's attorney for a Nesach Tabu (`נסח טאבו`) AND a RMI lease extract (`פלט חכירה / pelet hachira`); the document will identify whether the underlying land is State, JNF (KKL), or Development Authority.

### Non-resident purchase-tax surcharge (Mas Rechisha)

- **Foreign / non-resident buyers do NOT get the Israeli-resident or Olim discounted brackets**. They pay the **investor / second-home scale** — the highest applicable bracket structure.
- **Bracket structure (effective from January 2026, indexed annually; verify current brackets at Tax Authority)**:

| Bracket | Threshold (ILS) | Rate (non-resident / investor scale) |
|---|---|---:|
| 1 | 0 – ~6,055,070 | 8% |
| 2 | ~6,055,070+ | 10% |

- **Olim (new immigrants) discount — Section 12 of the Real Estate Taxation Regulations**: a one-time, 7-year window (from 1 year before to 7 years after Aliyah date) reduced rate. **Restructured 12 August 2024** by Section 12 amendment — post-amendment regime (Olim arriving on/after 12 Aug 2024) (2026-05-27 verified, source: Nefesh B'Nefesh + Gornitzky GNY):

| Bracket | Threshold (ILS) | Rate (Olim, post-12-Aug-2024) |
|---|---|---:|
| 1 | 0 – ~1,978,745 | **0%** (full exemption) |
| 2 | ~1,978,745 – ~6,055,070 | **0.5%** |
| 3 | ~6,055,070 – ~20,183,565 | **8%** |
| 4 | above ~20,183,565 | benefit DENIED — full standard rates |

- Benefit now applies **only to single-residency purchases**; Olim purchasing investment / additional properties pay standard rates
- Benefit capped at properties ≤ ~ILS 20,183,565
- **Grandfathering**: Olim who made Aliyah **before 12 Aug 2024** may elect old (0.5% / 5%) OR new (0% / 0.5% / 8%) rates for subsequent purchases; post-12-Aug-2024 Olim must use the new schedule only
- 7-year window (1 year before to 7 years after Aliyah) unchanged

- **Israeli-resident "single home" buyer**: progressive 0% / 3.5% / 5% / 8% / 10% scale up to ~ILS 6,055,070 (verify) — *not* available to non-residents.
- **Bracket indexation FROZEN 2025-2027**: normally indexed annually on 16 January to the CBS housing price index, but indexation is **frozen for tax years 2025, 2026, 2027** under the Economic Efficiency Law / 2025 budget directives; January-2024 brackets remain fixed in nominal shekels through 15 January 2028 — restart planned thereafter, no backfill (2026-05-27 verified per Economic Efficiency Law late-2024 budget package; previously indexed source: Tax Authority circular page `https://www.gov.il/he/departments/dynamiccollectors/tax-rates-real-estate-purchase`).
- **CRITICAL**: the bracket numbers above are 2026 reference points; verify current values at the Tax Authority page before signing — they shift every year and have been adjusted mid-year by emergency wartime orders since October 2023.

### Property Tax Compensation Fund (Israel Tax Authority) — wartime damage cover

- **Legal basis**: Property Tax and Compensation Fund Law 5721-1961 (חוק מס רכוש וקרן פיצויים).
- **What it covers**: direct physical war/missile/terror damage to:
- **Buildings (structures)** — repair or replacement up to fund caps tied to the property's tax-assessed value
- **Contents (movables)** — capped per-claim
- **Indirect damages** (loss of business income for evacuee zones) — tighter rules; partial coverage
- **What it does NOT cover**:
- **Land devaluation** caused by proximity to active conflict (e.g., Otef Aza / Northern border post-October 2023) — owners cannot recover lost market value
- Property-tax assessed value gap when a property's market value exceeds the assessed cap — the gap is uncovered
- Damage from internal causes (fire, earthquake) — those go to private insurance / Mavat Ra'ash (national earthquake fund framework, separate)
- **Funding**: state-funded (treasury allocation), supplemented historically by a property-tax surcharge. The fund has paid out an **est. tens of billions of ILS** since October 2023 for war damage in Otef Aza, Northern Israel, and central-Israel rocket-impact incidents (order-of-magnitude estimate — verify current figures at Compensation Fund publications). Documented claim volumes: **~1M cumulative war-damage claims across all fronts by April 2026** (Bloomberg, 2026-04-17); the 2026 Iran-war fighting alone logged **10,946 claims** by 15 March 2026 — 7,648 for structures, 1,179 for contents/equipment, 1,945 for vehicles, 174 other (Israel Tax Authority Compensation Fund update, `https://www.gov.il/en/pages/sa150326-1`).
- **Claim process**: **direct** property damage is filed via the Tax Authority Compensation Fund portal `https://www.gov.il/he/service/online-direct-damage-claim`. **Indirect (economic) damage** runs on separate, dated tracks indexed at [gov.il — מסלולי פיצויים בגין נזק עקיף](https://www.gov.il/he/Departments/DynamicCollectors/compensation-tracks); as at 2026-09-18 that index listed 66 tracks, including the May–June 2026 eligibility period for operation **שאגת הארי** with a filing deadline of **30 December 2026**. Deadlines are set per track and extended for active-conflict zones by emergency order — check the index for the period that applies (2026 data, source Israel Tax Authority; 2026-09-18 verified).
- **Implication for foreign buyers**: the Compensation Fund substantially de-risks war-damage to the structure but does NOT compensate land-value loss — a property in or near an evacuated zone may retain Compensation Fund coverage for damage but suffer material market-value loss with no compensation pathway. (Magnitude of the value loss is not publicly indexed during the active-conflict period — verify against Tax Authority transaction data for the specific locality.)

### War footing — current status (as of July 2026)

- **Israel-Hamas (Gaza) war**: started 7 October 2023; a **fragile US-brokered ceasefire (the "Yellow Line")** has held since October 2025, though the IDF continued expanding control beyond the Yellow Line as of July 2026 (Democracy Now, 2026-07-01); Otef Aza (Gaza envelope, ~30 km radius) communities partially repopulated, partial reconstruction.
- **Israel-Hezbollah (Lebanon)**: hostilities September–November 2024; ceasefire 27 November 2024 (verify currency at Israeli Ministry of Foreign Affairs `https://www.gov.il/he/departments/ministry_of_foreign_affairs`); the ceasefire held until hostilities with Hezbollah resumed during the 2026 Iran war (Britannica); Northern border evacuees gradually returning.
- **Israel-Iran wars**: two direct wars — the **June 2025 "12-Day War"** (Israel struck Iranian nuclear/military sites from 13 June 2025; Al Jazeera) and a **2026 Iran war** (Feb–Apr 2026 escalation; two-week ceasefire announced 7 April 2026; Wikipedia). Iranian **ballistic-missile strikes caused heavy damage to Israeli residential property** (e.g. Kiryat Ata near Haifa; Bloomberg) and are the **dominant driver of war-damage claims** — nearly 10,000 property-damage claims by the second day of the June 2025 war, and 9,115 missile-damage claims after 11 days of the 2026 fighting (Globes, 2026-03-10).
- **Houthi (Yemen) missile/UAV strikes**: intermittent strikes against central Israel through 2024–2026; air defense generally effective; occasional impacts.
- **Insurance market**: many private insurers reduced or excluded war-coverage riders; **Compensation Fund central** for war-damage compensation; private insurance covers theft, fire, earthquake (separate framework), water damage. **Verify with the [Capital Market, Insurance and Savings Authority (רשות שוק ההון, ביטוח וחיסכון)](https://www.gov.il/he/departments/capital_market_authority/govil-landing-page)** — the regulator, which publishes the home-insurance comparison tooling — and with your private carrier. Note that **war-damage** cover is the Property Tax Compensation Fund's, not any private insurer's (see the Compensation Fund rows above).

### Mortgage / financing for non-residents

- **Bank of Israel limits** (Banking Supervision Department, Proper Conduct of Banking Business Directive 329):
- **Non-resident foreign buyer**: maximum LTV typically **50%** (varies by bank; some go to 60% with strong credit). Source: BoI directive page `https://www.boi.org.il/en/`.
- **Israeli first home**: up to 75% LTV
- **Israeli second home / investor**: up to 50% LTV
- **Currency**: most non-resident mortgages offered in ILS; some banks offer USD/EUR-denominated mortgages with FX conversion at drawdown — discuss with the lender.
- **Documentation**: source-of-funds (under AML Order); tax-residency declaration (FATCA/CRS); often Israeli attorney's confirmation of clean title.

### Buyer due diligence — minimum checklist

1. **Nesach Tabu (טאבו abstract)** — verify ownership, encumbrances (`עיקולים`/garnishments, `משכנתאות`/mortgages, `הערות אזהרה`/warning notices). Nesach Tabu (נסח טאבו / title abstract) is ordered online at [gov.il — הפקת נסח טאבו](https://www.gov.il/he/service/land_registration_extract) → [מקרקעין ברשת](https://mekarkein-online.justice.gov.il/voucher/main); **the fee is not published on the authority's page** — it is charged "לפי המחיר המעודכן באתר התשלומים הממשלתי". Tariffs were re-indexed with effect from 1 Jan 2026 under הודעת המקרקעין (אגרות), התשפ"ו-2025 — data not publicly available on the landing page; verify the current amount at the Israeli government payments site / the Authority for Land Registration and Settlement of Rights (2026-09-18 verified).
2. **RMI lease extract (פלט חכירה)** — verify lease term, capitalization status, JNF vs State vs Development Authority, Heskem Hadash eligibility. Order at RMI office or via attorney.
3. **Rishum Mekarkein** — alternate registry for some pre-1969 unsettled parcels (`רישום מקרקעין לא מוסדרים`); attorney must check both.
4. **Building permit + completion certificate (היתר בנייה + טופס 4)** — issued by the local municipality; verifies the structure was legally built and inhabitable. Unauthorized additions (חריגות בנייה) are extremely common and **not always visible at viewing** — request the hetter and Form 4 directly from municipality.
5. **Tabu rights map (תשריט)** + RMI parcel map — surveyed boundaries; commission a licensed surveyor (`מודד מוסמך`) for boundary verification on rural parcels.
6. **War-damage history** — for properties in or near border zones (Otef Aza, Galilee, Golan), check claim history with the seller and request a Compensation Fund clearance. Damage history affects market value and future insurability.
7. **Va'ad Bayit / building committee balance** — for apartments under condominium (Bait Meshutaf / בית משותף) regime, request statement of arrears and reserve fund (קרן שיקום).
8. **Licensed Israeli real-estate attorney (עורך דין מקרקעין)** — the buyer's attorney is legally responsible for verifying clean title and registering the transfer; standard fee 0.5–2% + VAT (currently 18% as of January 2025; verify at Tax Authority).
9. **Licensed appraiser (שמאי מקרקעין)** — independent valuation, especially for non-residents; ~ILS 3,000–8,000 typical.

### Confidence

**HIGH** for legal framework (Land Taxation Law, RMI structure, Compensation Fund framework, mortgage LTV limits — all primary statutes published in Reshumot / `https://www.gov.il/`). **MEDIUM** for current bracket numbers (annual indexation; verify at signing). **MEDIUM** for war-zone insurability (private market disrupted post-Oct 2023; conditions evolving).

---

## Section: `--price`

### Primary sources

- **CBS (Central Bureau of Statistics, הלשכה המרכזית לסטטיסטיקה)** — official dwelling price index and rental price index, monthly.
- Dwelling Price Index portal: `https://www.cbs.gov.il/he/subjects/Pages/מחירי-דירות.aspx`
- Monthly Consumer Price Index page: `https://www.cbs.gov.il/he/Pages/default.aspx`
- Index methodology: hedonic regression on transactions reported to the Tax Authority.
- **Israel Tax Authority — Real Estate Transactions Database (מאגר עסקאות נדל"ן)**:
- Public portal: `https://www.gov.il/he/departments/dynamiccollectors/realestate_purchase_data` (search by address — actual recorded sale prices)
- This is the **single most important benchmark source** for foreign buyers: shows realized prices, not listing asking prices.
- **Bank of Israel residential property data**:
- Financial Stability Report `https://www.boi.org.il/en/communication-and-publications/regular-publications/financial-stability/`
- Statistical bulletin (real estate section) `https://www.boi.org.il/en/economic-roles/statistics/`
- **Ministry of Construction & Housing (משרד הבינוי והשיכון)** — tender prices for state-land plots; useful as a lower bound. `https://www.gov.il/he/departments/ministry_of_construction_and_housing`

### Listing platforms (secondary, listings = seller-controlled)

- **Yad2 (יד2)** — largest aggregator (apartments, houses, land, commercial). `https://www.yad2.co.il/realestate/forsale`
- **Madlan (מדלן)** — strong on Tel Aviv and Gush Dan; combines listings + neighborhood analytics + transaction overlay (uses Tax Authority data). `https://www.madlan.co.il/`
- **OnMap** — map-first, English+Hebrew, foreign-buyer-friendly. `https://www.onmap.co.il/`
- **Komo (קומו)** — Tel Aviv–focused premium listings. `https://www.komo.co.il/`
- **Homeless** — `https://www.homeless.co.il/` (Israeli-language; sometimes lower-priced inventory)
- **WinWin (וין-וין)** — `https://www.winwin.co.il/` (broader real estate platform)
- **Anglo-List** — `https://www.anglo-list.com/` (English-language Anglo Olim and foreign-buyer focused)

### Price benchmarks (Q1 2026 reference — verify on Tax Authority transaction database for the specific neighborhood)

> **Source warning**: Yad2/Madlan/OnMap are listing-platforms (asking prices). Use the **Tax Authority transaction database** at `https://www.gov.il/he/departments/dynamiccollectors/realestate_purchase_data` for the specific street to see realized prices. CBS index gives macro trend.

| Locality | Segment | ILS/sqm range | USD/sqm est. (3.7 ILS/USD) | Source |
|---|---|---|---|---|
| **Tel Aviv** (central, Lev Ha'ir, Florentin, north city) | Resale apartment | 50,000–110,000 | ≈ $13,500–$29,700 | Madlan + Yad2 + Tax Authority transactions Q1 2026 |
| **Tel Aviv** (luxury — Rothschild, Neve Tzedek, Tel Aviv Port) | New / luxury apartment | 80,000–200,000+ | ≈ $21,600–$54,000+ | Madlan + Komo Q1 2026 |
| **Jerusalem** (central, Rehavia, German Colony, Talbieh) | Apartment | 35,000–75,000 | ≈ $9,500–$20,300 | Yad2 + Tax Authority Q1 2026 |
| **Jerusalem** (Anglo-heavy: Baka, Old Katamon, Arnona) | Apartment | 40,000–85,000 | ≈ $10,800–$23,000 | Yad2 + Anglo-List Q1 2026 |
| **Haifa** (Carmel, Hadar, German Colony) | Apartment | 18,000–40,000 | ≈ $4,860–$10,800 | Yad2 + Tax Authority Q1 2026 |
| **Netanya / Herzliya / Ra'anana** | Apartment | 30,000–70,000 | ≈ $8,100–$18,900 | Yad2 + Madlan Q1 2026 |
| **Beersheba (Be'er Sheva)** | Apartment | 12,000–25,000 | ≈ $3,240–$6,750 | Yad2 + Tax Authority |
| **Eilat** | Apartment | 20,000–45,000 | ≈ $5,400–$12,160 | Yad2 |
| **Tiberias / Tzfat / Galilee periphery** | Apartment / house | 12,000–30,000 | ≈ $3,240–$8,100 | Yad2 (data thin in some communities) |
| **Otef Aza / Gaza envelope (post-Oct 2023 zone)** | Variable | data not publicly indexed in normal CBS series during active-conflict period | — | Verify at Tax Authority transaction database; many transactions paused; specialist counsel mandatory |

> Ranges are listing-derived where Tax Authority data isn't aggregated; verify realized prices for the specific street/building via the Tax Authority transactions database before any offer.

### Compute

1. **Price/sqm** = listing ILS ÷ usable area (`שטח עיקרי` / shetach ikari). **Trap**: many Israeli listings advertise total area (`שטח כולל`) including balconies (`מרפסת`), service areas (`שטח שירות`), and storage (`מחסן`) — clarify which area metric.
2. **Compare to Tax Authority transactions** for the same street + recent 12 months. This is the **realized-price benchmark**.
3. **Compare to CBS index** for the macro trend in the city.
4. **Pull Madlan neighborhood overlay** for transaction comps + price-per-sqm distribution.
5. **Trap (lease vs freehold pricing)**: chofshi (freehold) parcels typically command a **5–15% premium** over equivalent state-leased (chachira) units. The premium reflects RMI consent risk + lease-renewal exposure.
6. **Trap (parking + storage)**: in Tel Aviv, dedicated parking (חניה) adds ILS 250,000–500,000+ per spot; storage (מחסן) adds ILS 50,000–150,000. Verify whether the listing price includes them.

### Confidence

**HIGH** for Tel Aviv, Jerusalem, Haifa pricing (CBS index + Tax Authority transactions + multiple listing platforms agree). **MEDIUM** for periphery (Galilee, Negev) — thinner transaction sample. **LOW** for Otef Aza / Northern-border evacuee zones during active-conflict reporting period.

---

## Section: `--traffic`

### Primary sources

- **Netivei Israel (נתיבי ישראל / National Roads Company)** — traffic counts on inter-urban roads.
- Portal: `https://www.iroads.co.il/`
- Traffic data publication: search "סקרי תנועה" / "נפח תנועה" via the site
- **Ministry of Transport (משרד התחבורה)** — annual traffic statistics; `https://www.gov.il/he/departments/ministry_of_transport_and_road_safety`
- **CBS Transport Statistics** — `https://www.cbs.gov.il/he/subjects/Pages/תחבורה.aspx`
- **Local municipality traffic department** — for urban arterial counts (Tel Aviv, Jerusalem, Haifa publish their own counts intermittently)
- **OpenStreetMap (OSM)** — fallback for road class

### Verdict bands (vehicles per day, AADT-equivalent)

- 🟢 < 2,000 v/d: rural agricultural road, kibbutz access, side street
- 🟡 2,000–10,000 v/d: small inter-urban, urban side street
- 🟠 10,000–40,000 v/d: regional trunk, urban arterial
- 🔴 > 40,000 v/d: national highway (Kvish 1, 2, 4, 6 toll), urban core arterial

### Coarse fallback (OSM `highway` tag)

- `motorway` = Kvish 6 (Highway 6 / Trans-Israel Toll), parts of Kvish 1, 2, 4, 20
- `trunk` = primary inter-urban (Kvish 90, 40, 65)
- `primary` = regional (3-digit national roads)
- `secondary` = inter-village
- `tertiary` = urban collector
- `residential` = neighborhood / shchunah

### Quirks

- **Kvish 6 (Trans-Israel Toll Highway)**: tolled, electronic-tolled (no booths), national north-south route. Traffic data published by toll operator Derech Eretz and Netivei Israel.
- **Tel Aviv arterials (Ayalon / איילון, Ibn Gabirol, Allenby, Begin)**: heavy congestion at peak; AADT understates noise/pollution due to stop-and-go.
- **Jerusalem Light Rail (הרכבת הקלה)**: Red, Green (under construction/opened 2025), Blue lines reshape arterial flow; properties on light-rail corridor see noise + value uplift simultaneously.
- **Border roads (Kvish 90 along Jordan Valley, Kvish 232 in Otef Aza)**: traffic data may be intermittent during security operations.

### Confidence

**MEDIUM** — Netivei Israel publishes counts on national network but coverage is less granular than EU equivalents. For urban arterials, municipality data is patchy. Use OSM road-class as a baseline and verify with on-site visit for borderline properties.

---

## Section: `--tax`

### Annual property tax — Arnona (ארנונה)

**Israel does NOT have a national annual property tax**. Each of the 257 local authorities levies a **municipal property tax called Arnona** (legal basis: Local Authorities (Property Taxes Exemption) Law 5727-1967, plus annual local budget orders).

- **Computed**: by built area (`שטח בנוי` in m²) × per-m² rate set in the municipality's annual ordinance (`חוק עזר ארנונה`). Rates vary by:
- Property classification (residential, commercial, industrial, vacant)
- Neighborhood (`איזור ארנונה`) — most municipalities define 2–6 zones with different rates
- Building age (some municipalities discount for older / preserved buildings)
- **Annual indexation**: Ministry of Interior caps the year-on-year increase (typically published October/November for the coming calendar year). Source: `https://www.gov.il/he/departments/ministry_of_interior`.
- **Discounts** (`הנחות ארנונה`): standard discounts for olim (up to 90% in first year), pensioners, single-parent, disabled, large families — typically the buyer cannot inherit the seller's discount.
- **Range** (residential, 2026):
- **Tel Aviv-Yafo** (Zone A): ~ILS 75–110/m²/year (verify current at `https://www.tel-aviv.gov.il/`)
- **Jerusalem**: ~ILS 60–90/m²/year (verify at `https://www.jerusalem.muni.il/`)
- **Haifa**: ~ILS 50–75/m²/year
- **Periphery / smaller towns**: ~ILS 30–60/m²/year
- **Kibbutzim / regional councils**: variable, often lower (special arrangements)
- **Example calculation**:
- 90 m² apartment in central Tel Aviv at ~ILS 92/m²/year → ~ILS 8,280/year (~$2,240/year est. at 3.7 ILS/USD)
- 100 m² apartment in central Jerusalem at ~ILS 78/m²/year → ~ILS 7,800/year (~$2,110/year est.)
- **Verify exact rate on the seller's last Arnona bill (חשבון ארנונה)** — the most reliable source.

### Transaction tax — Mas Rechisha (מס רכישה)

**Mas Rechisha is the buyer's purchase tax.** Brackets normally indexed annually on **16 January** to CBS housing index, but indexation is **FROZEN for tax years 2025-2027** under the Economic Efficiency Law / 2025 budget directives; January-2024 brackets remain fixed in nominal shekels through 15 January 2028 (2026-05-27 verified per late-2024 budget package). Verify current values at `https://www.gov.il/he/departments/dynamiccollectors/tax-rates-real-estate-purchase`.

#### 2026 reference brackets (verify before signing — these change every January)

**Israeli resident, single residential home (zakaut le-dira yechida — זכאות לדירה יחידה)**:

| Bracket | Threshold (ILS) | Rate |
|---|---|---:|
| 1 | 0 – ~1,978,745 | 0% |
| 2 | ~1,978,745 – ~2,347,040 | 3.5% |
| 3 | ~2,347,040 – ~6,055,070 | 5% |
| 4 | ~6,055,070 – ~20,183,565 | 8% |
| 5 | ~20,183,565+ | 10% |

**Israeli resident, second home / investor (mashka'ot — משקיעים)**:

| Bracket | Threshold (ILS) | Rate |
|---|---|---:|
| 1 | 0 – ~6,055,070 | 8% |
| 2 | ~6,055,070+ | 10% |

**Non-resident / foreign buyer**: same as Israeli investor scale — **8% / 10%** (no discount).

**Olim (within 7-year window — Section 12 of regulations, post-12-Aug-2024 reform)** (2026-05-27 verified, source: Nefesh B'Nefesh + Gornitzky GNY):

| Bracket | Threshold (ILS) | Rate (Olim, post-12-Aug-2024) |
|---|---|---:|
| 1 | 0 – ~1,978,745 | **0%** (full exemption) |
| 2 | ~1,978,745 – ~6,055,070 | **0.5%** |
| 3 | ~6,055,070 – ~20,183,565 | **8%** |
| 4 | above ~20,183,565 | benefit DENIED |

- Single-residency only; investment / additional purchases get standard rates
- Olim who made Aliyah pre-12-Aug-2024 may elect old (0.5% / 5%) OR new (0% / 0.5% / 8%) scale

#### Worked examples

- **Foreign buyer, ILS 4,000,000 apartment**: 4,000,000 × 8% = **ILS 320,000 Mas Rechisha** (~$86,500 est.)
- **Foreign buyer, ILS 8,000,000 apartment**: (6,055,070 × 8%) + (1,944,930 × 10%) = 484,406 + 194,493 = **~ILS 678,899** (~$183,500 est.)
- **Oleh, ILS 4,000,000 apartment within 7-year window (post-12-Aug-2024 regime)**: (1,978,745 × 0%) + (2,021,255 × 0.5%) = 0 + 10,106 = **~ILS 10,106** (~$2,730 est.) (2026-05-27 verified — formerly ~ILS 113,230 under pre-amendment 0.5%/5% scale; grandfathered Olim may still elect that)
- **Foreign vs Oleh on same ILS 4M apartment**: foreign pays ILS 320,000; Oleh (post-12-Aug-2024 single-residency) pays ILS 10,106 — **the Olim discount saves ~ILS 309,894 (~$83,800 est.)** on this transaction; the prior 0.5%/5% regime saved ~ILS 206,770.

### Capital gains — Mas Shevach (מס שבח)

- **Legal basis**: Land Taxation (Appreciation and Purchase) Law 5723-1963, Chapter Three.
- **Standard rate**: 25% on the real (CPI-indexed) capital gain for individuals; 23% for corporations (matching corporate tax rate).
- **Linear formula**: gain accrued before 7 November 2001 is taxed at the marginal income-tax rate of the seller (up to 50%); gain accrued from 7 November 2001 onward is taxed at the flat 25%. Sellers compute via the official Mas Shevach Linear Calculator at the Tax Authority site.
- **Primary residence exemption (פטור מדירה יחידה)**: Israeli-resident sellers who own a single residential dwelling and have held it ≥ 18 months may claim a full Mas Shevach exemption (subject to ownership-history conditions). Source: Tax Authority `https://www.gov.il/he/departments/topics/real_estate_taxation`.
- **Non-resident sellers**: typically pay 25% on the post-2001 gain; primary-residence exemption rarely applies (requires Israeli residency conditions).
- **Withholding at sale**: buyer's attorney withholds an interim Mas Shevach (`ניכוי במקור`) at closing and remits to Tax Authority; final assessment within 4 years.

### Other transaction-related taxes / fees

- **VAT (מע"מ)**: 18% (effective 1 January 2025, raised from 17%; verify at `https://www.gov.il/he/departments/topics/vat_information`). Applies to **new-build sales by developers**, not to second-hand sales between individuals. New-build advertised prices may include or exclude VAT — clarify per listing.
- **Heitel Hashbacha (היטל השבחה / betterment levy)**: 50% of the valuation uplift from a planning-permission upgrade (rezoning, density increase). **Seller pays** at sale. Verify with municipality whether any TBA (תב"ע) plan affects the parcel.
- **Mas Mechira (מס מכירה)**: ABOLISHED 1 August 2007 for individuals (still applies in some corporate contexts; check with Tax Authority).
- **Tabu registration fee**: variable, modest — `est.` ILS 1,500–3,000 for a standard apartment registration, **uncited**: the Land Registry service page `https://www.gov.il/he/service/land_registration_extract` states no registration-fee range, and tariffs were re-indexed with effect 1 Jan 2026 under הודעת המקרקעין (אגרות), התשפ"ו-2025 — verify the current amount at the Israeli government payments site / the Authority for Land Registration and Settlement of Rights (2026-09-18).
- **RMI consent / capitalization fee** (if state-leased): variable; ranges from negligible (pre-paid lease) to several percent of land value (Heskem Hadash conversion).
- **Buyer attorney**: 0.5–2.0% + VAT (18%) typical; standardized minimum fees published by Israel Bar Association `https://www.israelbar.org.il/`.
- **Real estate broker (תיווך)**: typical 2% + VAT each side (buyer + seller pay 2% each); regulated under the Real Estate Brokers Law 5756-1996 — broker must be licensed (`רישיון מתווך`).

### Future risk

- **Annual bracket indexation in mid-January** can shift thresholds materially.
- **Wartime emergency tax orders** since October 2023 have included temporary purchase-tax adjustments and Compensation Fund-funding surcharges; verify currency at signing.
- **Periodic political proposals** to raise non-resident Mas Rechisha (most recently discussed 2024) — not enacted as of May 2026.
- **Heitel Hashbacha enforcement** strengthening — many municipalities catching up on uncollected betterment levies.

---

## Section: `--rental`

### Long-term residential

- **Tax regime — choice of three** (legal basis: Income Tax Ordinance §122 + 122A):
- **Full exemption track** (קו פטור): if monthly rental income from all residential properties ≤ ILS 5,654 (2026 threshold; verify currency at Tax Authority) — fully exempt from income tax. Useful for small landlords.
- **10% flat-rate track** (קו 10%): pay 10% flat tax on gross rental income; no expense deductions; no abatement; mandatory advance-payment by 30 January following tax year. Most common for small-to-mid landlords.
- **Standard income tax track** (מסלול רגיל): rental income added to other income; taxed at marginal bracket (10–50% range); deduct actual expenses (depreciation, mortgage interest, repairs, agent fees). Best for high-cost / high-leverage scenarios.
- **Non-residents**: typically 10% track or standard track; no exemption-track for non-Israeli-resident landlords (§122 limits exemption to Israeli residents).
- **Tenant-protection law**: Tenancy Law 5731-1971 (חוק השכירות והשאילה); reformed substantially 2017 (Fair Rent Law / חוק שכירות הוגנת) — sets minimum standards (working appliances, safety, mold-free), restrictions on landlord termination during tenancy, deposit caps (max 3 months' rent or 1/3 of lease value).
- **Standard contract**: 12 months with renewal option; termination requires 60–90 days notice depending on lease term.

### Short-term rentals (Airbnb / Booking)

- **Status**: legal but increasingly regulated. National framework still evolving (proposed STR registration law debated 2023–2025; as of May 2026 verify current status at Knesset).
- **Tel Aviv-Yafo**: most stringent — Tel Aviv has discussed mandating short-let registration, building-association consent, and per-unit caps. Verify at `https://www.tel-aviv.gov.il/`.
- **Tax**: short-term rental income generally classified as **business income** (not §122 residential rental) when:
- Property is offered for short-let (< 6 months at a time)
- Active management / marketing (Airbnb / Booking listings)
- Multiple turnovers per year
- **VAT trigger**: if annual short-let revenue > ILS ~120,000 (2026 osek patur threshold; verify), VAT registration becomes mandatory at 18%.
- **Building-association (Va'ad Bayit) consent**: under Land Law 5729-1969 §59A and amendments, condominium owners cannot run a "hotel-like" operation without by-law amendment from the building's general assembly (`אסיפה כללית`). Many Tel Aviv buildings have passed by-laws prohibiting Airbnb.
- **Local accommodation tax**: some municipalities (Tel Aviv, Jerusalem, Eilat) collect a guest tax (`מס תיירים` / accommodation levy) on short-let stays — verify per municipality.
- **Eilat special status**: VAT-exempt zone (Eilat Free Zone Law 5745-1985); short-let rates for Eilat differ from rest of Israel.

### Strategic notes

- **Tel Aviv + Jerusalem central + Eilat + Tiberias** — strongest short-let demand but highest regulatory pressure.
- **Coastal cities (Netanya, Bat Yam, Ashdod, Herzliya)** — moderate demand, less regulation.
- **Periphery (Galilee, Negev, Otef Aza)** — limited demand outside specific tourism niches; war-zone risk for Northern + Southern border properties.
- **Anglo-Olim long-let market**: strong rental demand from English-speaking olim in Jerusalem (Baka, Old Katamon, German Colony), Ra'anana, Modi'in — premium rents possible.

---

## Section: `--work=<profession>`

### Job platforms

- **AllJobs (אול-ג'ובס)**: `https://www.alljobs.co.il/` — largest Israeli platform
- **Drushim (דרושים)**: `https://www.drushim.co.il/`
- **JobMaster**: `https://www.jobmaster.co.il/`
- **LinkedIn IL** — extremely active in tech, finance, Anglo-Olim networks
- **Israemploy** — `https://www.israemploy.net/` ❌ DEPRECATED — link dead (verified 2026-06-13); verify with a current Israel job board (Israemploy ceased 2021) (Anglo-Olim focused, English)
- **Nefesh B'Nefesh** — `https://www.nbn.org.il/` (Aliyah + employment for Anglo Olim)
- **Government job portal** — `https://www.gov.il/he/departments/dynamiccollectors/jobs_for_civil_service_employees` (state employment)

### Self-employment regimes

- **Osek Patur (עוסק פטור)**: VAT-exempt micro-business; 2026 turnover ceiling **ILS ~120,000/year** (verify at Tax Authority, indexed annually). Files annual income tax; no VAT; bituach leumi (national insurance) + bituach bri'ut (health insurance) on net income.
- **Osek Murshe (עוסק מורשה)**: standard VAT-registered self-employed; charges 18% VAT (effective Jan 2025); files bi-monthly VAT returns; annual income tax; full bituach leumi.
- **Hevra Ba'am (חברה בע"מ / Ltd company)**: corporate tax 23% (2026); useful above ~ILS 600k profit or for specific structures.
- **Bituach Leumi (national insurance + health)**: combined ~12–17% on self-employed income up to a cap; pays for state pension, disability, healthcare.

### Salaried benchmarks (CBS data, 2025; verify at `https://www.cbs.gov.il/he/subjects/Pages/שכר-ותעסוקה.aspx`)

- **Average monthly gross 2025**: ~ILS 13,500 (verify CBS current; pre-tax)
- **Tel Aviv tech sector**: ~ILS 25,000–50,000/month (senior engineer / mid-level PM)
- **Periphery / non-tech**: ~ILS 8,000–15,000/month
- **Minimum wage 2026**: ~ILS 5,880/month (verify; updated periodically; current at `https://www.gov.il/he/departments/ministry_of_economy_and_industry`)

### Anglo-Olim profession quirks

- **Licensed professions** (medicine, law, accounting, psychology, dentistry, pharmacy, engineering, teaching): require Israeli license — many Anglo Olim require local exams + Hebrew proficiency; **Misrad HaBriut** (Health Ministry), **Lishkat HaDin** (Bar Association), **Lishkat HaRoeh Heshbon** (Accountants).
- **Tech (high-tech / hi-tech / היי-טק)**: English-language work environment dominant in Tel Aviv; Anglo Olim hire easily without Hebrew; competitive global salaries.
- **Remote / international work** (consulting, content, online teaching, etc.): widely viable; tax-residency complexity (likely Israeli tax resident if >183 days; foreign tax credit per treaty).
- **Real-estate brokerage**: requires Israeli license (`רישיון מתווך`) under Real Estate Brokers Law 5756-1996; Hebrew proficiency typically expected.

### Catchment heuristics

- Within Tel Aviv metro / Gush Dan: full salaried + freelance opportunity
- Within Jerusalem corridor (Modi'in, Beit Shemesh): commutable to Tel Aviv (60–90 min) + Jerusalem (30–45 min)
- Periphery (Galilee, Negev, Eilat): thinner labor markets; remote / tourism / agriculture / specific industries (chemicals in Mitzpe Ramon; tech in Yokne'am, Caesarea)
- Border / evacuee zones (Otef Aza, Northern border post-Oct 2023): labor markets disrupted; verify current employment status before relocating

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Home Front Command (פיקוד העורף, Pikud HaOref)** | `https://www.oref.org.il/` | Missile/rocket alert zones, shelter (Mamad / ממ"ד / Merhav Mugan Dirati) requirements, war-zone designations |
| **Property Tax Compensation Fund (Israel Tax Authority)** | `https://www.gov.il/en/departments/topics/compensation_fund` + `https://www.gov.il/he/service/online-direct-damage-claim` | War-damage compensation; published claim volumes |
| **Geological Survey of Israel (GSI / מכון הסקר הגיאולוגי)** | `https://www.gsi.gov.il/` | Earthquake hazard maps, landslide registry, geology |
| **Israel Building Code SI 413 + Standards Institute** | `https://www.sii.org.il/` | Earthquake-resistant building standards |
| **Ministry of Environmental Protection (המשרד להגנת הסביבה)** | `https://www.gov.il/he/departments/ministry_of_environmental_protection` | Air quality, contamination, environmental hazards |
| **Israel Water Authority (רשות המים)** — hydrological observations + GIS | obs/forecast: `https://hydro.water.gov.il/` · national water GIS: `https://govextra.gov.il/water-authority/water-authority/home/` · authority: `https://www.gov.il/he/departments/water_authority` | Flood / wadi flood hazard data; arid-region flash-flood risk (2026 data, source gov.il Water Authority; 2026-09-18 verified) |
| **Israel Meteorological Service (השירות המטאורולוגי)** | `https://ims.gov.il/` | Climate baseline + extreme weather |
| **TAMA 38 / TAMA 70 plans (תמ"א 38 / 70)** | `https://www.gov.il/he/departments/topics/tama_38` | Earthquake-retrofit national outline plans (TAMA 38 sunset 1 Oct 2022 — replaced by TAMA 70 / local outline plans) |

### Earthquake risk

- **Israel sits on the Dead Sea Transform fault** — left-lateral fault running Aqaba → Dead Sea → Jordan Valley → Hula Valley → Lebanon. Historical major events: 1927 Jericho M 6.2; 1837 Galilee M 6.5–7.0; 1759 Galilee–Lebanon M 7.4.
- **Standard SI 413** mandates earthquake-resistant design for new buildings since 1975 (revised 1995, 2004, 2013, 2020). Pre-1980 buildings frequently NOT compliant.
- **TAMA 38** (National Outline Plan 38, in force 2005–2022): incentivized seismic-retrofit of pre-1980 buildings via density bonuses. **Sunset 1 October 2022**; replaced by local outline plans (תוכניות מתאר מקומיות) and TAMA 70. Many Tel Aviv buildings underwent or are awaiting TAMA 38 retrofit.
- **Risk ranking**: 🟠–🔴 in Jordan Valley / Beit She'an Valley / Galilee fault belt; 🟡 along central coast and Tel Aviv; 🟢 most Negev (lower fault density).
- **Insurance**: standard homeowner policies (`ביטוח דירה`) typically include earthquake cover but verify per policy.

### Missile / rocket / war-damage risk

- **Compensation Fund-covered** (state-funded compensation for direct property damage) — see Foreign-buyer section above.
- **Mamad (מ.מ.ד / shelter room)**: mandatory in all new residential construction since 1992 (Civil Defense Law 5711-1951 amendment). Pre-1992 buildings have public shelters (`מקלט ציבורי`) within 90 seconds run.
- **Otef Aza (Gaza envelope)**: ~30 km radius around Gaza Strip; active rocket/missile/UAV threat from October 2023 until the fragile US-brokered October 2025 Gaza ceasefire (the "Yellow Line"); IDF operations continued past the Yellow Line as of July 2026 (Democracy Now, 2026-07-01). Compensation Fund claim volumes have run into tens of billions ILS since Oct 2023.
- **Northern border (Galilee + Golan)**: Hezbollah hostilities Sep–Nov 2024; ceasefire Nov 2024 (held until hostilities resumed during the 2026 Iran war — Britannica); partial repopulation as of July 2026.
- **Iranian ballistic-missile strikes**: two Israel-Iran wars — the June 2025 "12-Day War" and a 2026 Iran war (ceasefire 7 April 2026) — hit Israeli residential property directly and are the dominant driver of war-damage claims (nearly 10,000 claims by day two of the June 2025 war; 9,115 after 11 days of the 2026 fighting — Globes, 2026-03-10; ~1M cumulative war-damage claims across all fronts by April 2026 — Bloomberg, 2026-04-17). Heavy damage documented at Kiryat Ata near Haifa (Bloomberg).
- **Central Israel** (Tel Aviv–Gush Dan, Jerusalem corridor): Houthi (Yemen) UAV/missile strikes intermittent through 2024–2026; Iron Dome / Arrow / David's Sling intercept rates high but not 100%.

### Flood / wadi / flash-flood risk

- **Coastal cities**: storm-surge + drainage flooding (Tel Aviv, Bat Yam, Netanya periodically). Verify flood-zone status with municipality and the Israel Water Authority.
- **Negev / Arava / Dead Sea**: arid, but **flash floods** (`שיטפון`) in wadis after rare heavy rain — extremely dangerous; check wadi-channel proximity before buying rural southern property.
- **Galilee / Northern**: winter rain + steep terrain → localized flooding; routine engineering controls.

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1948** (Ottoman / British Mandate) | Pre-Mamad; pre-SI 413; lead, asbestos in roofing common; weak foundations; frequent unauthorized additions |
| **1948–1967** (early state, "shikun" social housing — `שיכון`) | Pre-SI 413 (1975); asbestos in roofing/insulation common; weak earthquake resilience; aging plumbing |
| **1968–1991** | SI 413 from 1975 partial; asbestos in older sections; Mamad NOT mandatory |
| **1992+ (post-Mamad mandate)** | Mamad mandatory; SI 413 revised; modern standards |
| **Post-2005 TAMA 38 era** | Many pre-1980 buildings retrofitted seismically |
| **Post-2020 SI 413 revision** | Strongest earthquake standards |

- **Asbestos**: pre-1990 buildings frequently contain asbestos (roofs, pipe insulation, wall panels). Removal regulated by Asbestos Hazards Prevention Law 5771-2011; mandatory licensed contractor for friable asbestos. Source: `https://www.gov.il/he/departments/topics/asbestos_dust_pollution`.

### Mandatory diagnostics at sale

| Document | Required because | Notes |
|---|---|---|
| **Nesach Tabu (טאבו abstract)** | All sales | Ordered online via `https://www.gov.il/he/service/land_registration_extract` → `https://mekarkein-online.justice.gov.il/voucher/main`; **fee not published on the authority's page — data not publicly available; verify the current amount at the government payments site** (tariffs re-indexed 1 Jan 2026 under הודעת המקרקעין (אגרות), התשפ"ו-2025; 2026-09-18 verified) |
| **RMI lease extract (פלט חכירה)** | If state-leased | At RMI office or via attorney |
| **Building permit + Form 4 (היתר בנייה + טופס 4)** | All sales | From local municipality |
| **Architectural drawings (תוכנית אדריכלית)** | Recommended | Verify built area matches permit |
| **Va'ad Bayit clearance** | If apartment under Bait Meshutaf | Statement of arrears + reserve fund (קרן שיקום) |
| **Heitel Hashbacha clearance** | All sales | Confirms no outstanding betterment levy |
| **Arnona clearance (אישור היעדר חובות ארנונה)** | All sales | Required for Tabu registration |
| **Energy rating (דירוג אנרגטי)** | New construction since 2017 | Mandatory for new builds |

### Climate change projections (IMS / Israel Meteorological Service + IPCC AR6)

- +1.5–3.5 °C by 2050 vs 1981–2010 baseline (depending on SSP)
- Increased heat-wave frequency + duration (esp. Jordan Valley, Negev, Beit She'an)
- Drying summers + wetter winters projected
- Sea-level rise: ~30–60 cm by 2100 (RCP 4.5–8.5) along Mediterranean coast → coastal Tel Aviv–Bat Yam–Ashkelon assets need long-horizon assessment
- Wildfires: rising in Carmel, Jerusalem corridor forests
- Water-table stress in coastal aquifer (saltwater intrusion)

---

## Section: `--mains`

### Water + sewer service

Israel has **near-universal mains water + sewer in urban areas** but verification is necessary in rural / kibbutzim / moshavim / Bedouin villages / Arab villages with informal infrastructure.

### Operators

- **Mei Avivim (מי אביבים)** — Tel Aviv-Yafo + Bat Yam; subsidiary structure
- **Hagihon (הגיחון)** — Jerusalem
- **Mei Carmel (מי כרמל)** — Haifa region
- **Mei Sharon (מי השרון)** — Sharon coastal corridor
- **Mei Avot (מי אבות)** — Petah Tikva, Rishon LeZion area
- **Many regional/municipal water corporations** — each major city has its own corporate utility under the Water Companies Law 5701-2001
- **Mekorot (מקורות)** — national water carrier (wholesale; not consumer-facing usually)
- **Water Authority (רשות המים)** — regulator; `https://www.gov.il/he/departments/water_authority`

### Verification

1. Listing language:
   - "מחובר למים ולביוב" / "tap-water + sewer connected" = urban mains
   - "מים מהמקור הישוב" / "boer יישוב" = village/kibbutz water (verify quality + reliability)
   - "ביוב פרטי" / "septic" = private septic — common in older periphery houses
2. Check **municipality website** under "מים וביוב" / "water and sewer" — most publish coverage
3. Most populated municipalities (>5,000 residents) have full mains coverage
4. **Bedouin unrecognized villages (Negev)**: many lack formal water/sewer + electricity infrastructure → specialist due diligence
5. **Settlement-area properties (Area C / Golan / disputed jurisdictions)**: utility provider may differ; verify operator + legal status

### Costs

| Scenario | Cost (ILS) |
|---|---:|
| Connection where available | 5,000–25,000 |
| Sewer connection construction | 30,000–100,000 |
| Septic to mains conversion | 50,000–150,000 |
| Modern compliant septic install | 60,000–180,000 |
| Water meter installation | nominal (covered by utility) |

---

## Cost benchmarks (IL 2026)

| Work | Cost (ILS) |
|---|---:|
| Buyer attorney (סדר רכישה) | 0.5–2.0% of price + VAT (18%) |
| Real-estate broker (תיווך) | 2% + VAT (each side) |
| Licensed appraiser (שמאי מקרקעין) | 3,000–8,000 |
| Tabu registration fee | `est.` 1,500–3,000 — uncited; fee range not published (verify) |
| Nesach Tabu (online abstract) | fee not published on the authority's page — verify at the government payments site |
| RMI lease extract / consent | 200–2,000 (varies) |
| Heskem Hadash conversion (capitalization) | varies — % of land value (verify per parcel) |
| **Mas Rechisha (foreign buyer)** | 8–10% of purchase price |
| **Annual Arnona (90 m² Tel Aviv)** | ~6,500–10,000 |
| Asbestos removal (200 m² roof) | 30,000–80,000 |
| TAMA 38 / TAMA 70 retrofit cost (per unit, paid by developer in exchange for density bonus) | typically nil to owner; structured as construction-financed deal |
| Mamad retrofit (adding shelter to existing apt) | 60,000–200,000 (often impractical) |
| Earthquake retrofit (general structural strengthening) | 100,000–500,000+ |
| Energy retrofit | 50,000–250,000 |
| Building inspection (independent בדיקה) | 1,500–4,000 |
| **Total transaction cost (foreign buyer side)** | ~10–13% of price (driven by Mas Rechisha + attorney + broker + VAT on services) |

## Active fiscal incentives (2026)

- **Olim 7-year purchase-tax discount** (Section 12) — see Foreign-buyer section above
- **Olim Arnona discount** — up to 90% in first year, decreasing in years 2–4 (verify per municipality)
- **Misrad HaKlita / Aliyah grants** — `https://www.gov.il/he/departments/ministry_of_aliyah_and_integration` — financial absorption package for Olim
- **Periphery / Development Zone (אזור פיתוח א'/ב')** — tax incentives for businesses in designated peripheral zones; some affect personal income tax for residents
- **Mas Hachnasa pension contributions** — tax-deductible contributions to קרן השתלמות + קופת גמל
- **TAMA 38 / TAMA 70** — earthquake retrofit programs (developer-financed in exchange for density bonus); homeowner gets seismic upgrade + sometimes additional unit/floor/balcony
- **Energy efficiency grants** — Ministry of Energy grants for solar PV, heat pumps, building envelope upgrades; verify currency at `https://www.gov.il/he/departments/ministry_of_energy`
- **Bituach Leumi grants** — Mavtach LeNaghim (mortgage assistance for olim, large families, etc.)

## Common listing platforms

- **Yad2** — largest aggregator, full Israel coverage
- **Madlan** — Tel Aviv + Gush Dan; combines listings + Tax Authority transaction overlay (gold standard for Tel Aviv comps)
- **OnMap** — map-first, English+Hebrew, foreign-friendly
- **Komo** — Tel Aviv premium/luxury
- **Homeless** — Hebrew-focused
- **WinWin** — broader real estate platform
- **Anglo-List** — English-language, Anglo Olim + foreign-buyer focus
- **Bnei Brith / specific community listings** — for niche religious-community housing (Bnei Brak, Ramat Beit Shemesh, etc.)

## Caveats unique to IL

- **State-land monopoly (~93%)**: most "sales" are technically lease transfers (with or without Heskem Hadash conversion). Always verify Tabu + RMI lease status.
- **JNF restriction litigation**: ongoing legal contestation; non-Jewish buyers face the swap mechanism; watch HCJ rulings.
- **Compensation Fund caps**: war-damage compensation has caps tied to property tax-assessed value, NOT market value — coverage gap can be material on premium properties.
- **Land devaluation NOT compensated**: Otef Aza / Northern border properties may retain Compensation Fund cover for damage but suffer material market-value loss (magnitude not publicly indexed) with no compensation pathway.
- **Settlement / Area C / East Jerusalem / Golan deeds**: international-law status disputed; some parcels registered under Jordanian or Ottoman pre-1967 systems; specialist counsel mandatory; foreign-buyer reputational risk consideration (some EU jurisdictions caution against settlement-area transactions).
- **Bedouin unrecognized villages (Negev)**: ~30–50 villages lack formal recognition + infrastructure + Tabu titles — extreme caution.
- **Tabu vs RMI dual system**: parcel must be verified in BOTH; pre-1969 unsettled parcels (`לא מוסדר`) need attorney verification.
- **Unauthorized additions (חריגות בנייה)**: extremely common; sometimes municipality has no current record of as-built; verify against the original heter.
- **VAT 18% on new-build (raised from 17% on 1 January 2025)**: clarify whether listing is gross or net of VAT.
- **TAMA 38 sunset 2022**: existing pipeline projects continue under transitional rules; new earthquake retrofit under local outline plans + TAMA 70.
- **Bituach Leumi (national insurance)**: foreign property owners renting out to Israeli tenants may incur bituach leumi exposure if classified as business activity — verify with Israeli accountant.
- **AML / source-of-funds**: Anti-Money Laundering Order 5761-2000 mandates KYC by attorneys + banks; non-resident buyers should expect comprehensive source-of-funds documentation requests.
- **Wartime emergency tax orders**: temporary purchase-tax + Compensation Fund-funding adjustments since October 2023; verify at signing.

## Reddit / forum sources

- **r/Israel**, **r/IsraelPalestine** (Reddit; English-language; Anglo-Olim-heavy)
- **Nefesh B'Nefesh community forums** — `https://www.nbn.org.il/` — Anglo-Olim Aliyah + housing
- **Anglo-List forums** — `https://www.anglo-list.com/`
- **Janglo** — `https://www.janglo.net/` — Anglo-Olim community in Jerusalem; classifieds + housing
- **Tapuz Anash** — `https://www.tapuz.co.il/` — Israeli-language community forums (real estate threads)
- **Calcalist (כלכליסט) realestate section** — `https://www.calcalist.co.il/real-estate` — financial press, market commentary
- **TheMarker realestate** — `https://www.themarker.com/realestate` — financial press
- **Globes realestate** — `https://en.globes.co.il/en/realestate.tag` — financial press

## Verification authorities

| Authority | When to call |
|---|---|
| **Tabu / Land Registry (לשכת רישום מקרקעין)** | Title abstract (Nesach), encumbrance check, registration |
| **RMI / Israel Land Authority (רשות מקרקעי ישראל)** | State-lease verification, Heskem Hadash eligibility, lease consent |
| **Local municipality (עיריה / מועצה)** | Building permit (heter), Form 4, Arnona clearance, Heitel Hashbacha clearance, TBA (תב"ע) plans, Mamad status, unauthorized additions |
| **Israel Tax Authority (רשות המסים)** | Mas Rechisha brackets, Mas Shevach calculation, transaction registration, real estate transactions database |
| **Property Tax Compensation Fund (Israel Tax Authority)** | War-damage history check on property; future claim guidance |
| **Bank of Israel (בנק ישראל)** | FX, mortgage LTV regulations, financial stability |
| **CBS (Central Bureau of Statistics)** | Dwelling price index, rental index, neighborhood statistics |
| **Home Front Command (פיקוד העורף)** | Missile-zone designation, Mamad requirements |
| **Geological Survey of Israel** | Earthquake hazard, fault proximity |
| **Israel Water Authority (רשות המים)** | Flood / wadi-flood zoning |
| **Misrad HaKlita / Aliyah** | Olim status verification + benefits |
| **Israeli Bar Association (לשכת עורכי הדין)** | Verify attorney licensure |
| **Israel Real Estate Brokers Federation** | Verify broker licensure under Real Estate Brokers Law 5756-1996 |
| **Va'ad Bayit (ועד בית)** | Building-association arrears, by-laws (incl. STR restrictions) |

## Quirks to know

- **Tabu vs RMI dual-system**: ~93% of land touches both registers; pre-1969 unsettled parcels are tracked at the older Land Registry under different procedures.
- **Bait Meshutaf (בית משותף — condominium law)**: under Land Law 5729-1969 §52–77; condominium register kept separately at Tabu; building must have a ratified `תקנון` (by-laws) and a `נציגות הבית המשותף` (representative) registered.
- **East Jerusalem / Area C / Golan / settlement-area deeds**: international-law status contested; some parcels registered under Jordanian (pre-1967), Ottoman (pre-1917), British Mandate, or military-administration regimes; specialist counsel mandatory.
- **Bedouin unrecognized villages (Negev)**: ~30–50 villages without formal recognition; no Tabu titles; extreme due diligence.
- **Heskem Hadash eligibility varies parcel-by-parcel**: not all state-leased parcels qualify; verify with RMI before banking on a freehold conversion.
- **Mamad (shelter room) mandatory in new builds since 1992**: verify presence + functional status; older buildings rely on stairwell or public shelters.
- **Energy rating (דירוג אנרגטי) mandatory for new builds since 2017**: verify rating certificate.
- **Asbestos pre-1990 likely**: licensed removal under Asbestos Hazards Prevention Law 5771-2011.
- **Bituach Dira (apartment insurance)**: typically covers structure + contents + earthquake (verify rider); war-damage routes through the Property Tax Compensation Fund instead.
- **Non-resident bank-account opening**: Israeli banks comply with FATCA + CRS; expect detailed source-of-funds documentation; allow weeks for account setup.
- **VAT 18% on services** (effective 1 January 2025): attorney + broker + appraiser fees all subject to VAT.
- **Vacation home / second-home rules**: a property declared as the buyer's "single home" (`דירה יחידה`) gets the discounted Israeli-resident purchase-tax scale — non-residents cannot claim this; foreign buyers always pay the investor scale.

## Source URL templates

| Source | URL pattern |
|---|---|
| Tabu Land Registry | `https://www.gov.il/he/service/land_registration_extract` |
| Land Registry main page | `https://www.gov.il/he/departments/land_registration_and_settlement_of_rights_department` |
| RMI / Israel Land Authority | `https://www.gov.il/he/departments/israel_land_authority` |
| Tax Authority real estate | `https://www.gov.il/he/departments/topics/real_estate_taxation` |
| Mas Rechisha brackets | `https://www.gov.il/he/departments/dynamiccollectors/tax-rates-real-estate-purchase` |
| Tax Authority transactions database | `https://www.gov.il/he/departments/dynamiccollectors/realestate_purchase_data` |
| CBS dwelling price index | `https://www.cbs.gov.il/he/subjects/Pages/מחירי-דירות.aspx` |
| Bank of Israel financial stability | `https://www.boi.org.il/en/communication-and-publications/regular-publications/financial-stability/` |
| Bank of Israel FX | `https://www.boi.org.il/en/economic-roles/financial-markets/exchange-rates/` |
| Property Tax Compensation Fund | `https://www.gov.il/en/departments/topics/compensation_fund` |
| Misim Compensation Fund portal | `https://www.gov.il/he/service/online-direct-damage-claim` |
| Aliyah & Integration | `https://www.gov.il/he/departments/ministry_of_aliyah_and_integration` |
| Construction & Housing | `https://www.gov.il/he/departments/ministry_of_construction_and_housing` |
| Home Front Command | `https://www.oref.org.il/` |
| Geological Survey of Israel | `https://www.gsi.gov.il/` |
| Israel Water Authority — hydrological observations | `https://hydro.water.gov.il/` |
| IMS meteorology | `https://ims.gov.il/` |
| Yad2 search | `https://www.yad2.co.il/realestate/forsale` |
| Madlan | `https://www.madlan.co.il/` |
| OnMap | `https://www.onmap.co.il/` |
| Komo | `https://www.komo.co.il/` |
| Anglo-List | `https://www.anglo-list.com/` |
| Israeli Bar Association | `https://www.israelbar.org.il/` |
| Reshumot (Official Gazette) | `https://www.gov.il/he/departments/publications/reports/official-gazette` |
| Knesset legislation | `https://main.knesset.gov.il/Activity/Legislation/Pages/default.aspx` |

## Status

✅ **Fully populated** as of 2026-05-01.
**Coverage check**: foreign-buyer eligibility, pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for legal framework (Land Code via Reshumot; RMI structure via gov.il; Property Tax Compensation Fund via primary statute; Mas Rechisha brackets via Tax Authority — all primary state agencies). MEDIUM for current bracket numerical values (annual indexation 16 January; verify at signing). MEDIUM for war-zone insurability and Otef Aza / Northern-border pricing (active conflict period; data thin). LOW for settlement-area / disputed-jurisdiction deeds (specialist counsel mandatory; not commodity due-diligence).

**Last verified**: 2026-07-02 (insurance regulator, ILA decisions database and hydrological-source attribution corrected 2026-09-18 per gov.il Capital Market Authority + apps.land.gov.il + Water Authority)

## Extension TODOs (deepen on first real run)

- [ ] Per-municipality Arnona rate scrape (top 50 cities — each publishes annual `חוק עזר ארנונה`)
- [ ] Tax Authority real-estate transactions database walkthrough — automate per-street comp pulls
- [ ] Heskem Hadash eligibility heatmap by RMI district
- [ ] Compensation Fund claim-volume timeseries since Oct 2023 (from official publications)
- [ ] TAMA 38 / TAMA 70 successor-plan tracking by city
- [ ] Bedouin unrecognized villages registry + due-diligence workflow
- [ ] East Jerusalem / Golan / settlement deed-system primer
- [ ] Va'ad Bayit by-law screening tool for STR-restricted buildings
- [ ] Asbestos detection workflow for pre-1990 shikun buildings
- [ ] Mamad / shelter-room compliance check (pre-1992 buildings)
