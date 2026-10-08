# Azerbaijan (AZ) — Property Due-Diligence Playbook

ISO2: `az`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Population**: ~10.16 million (2024 SSC State Statistical Committee estimate); Baku (capital) ~2.4M, Sumqayit ~340k, Ganja ~330k, Mingachevir ~110k, Shirvan ~90k
- **GDP per capita**: ~US$7,800 (2024 World Bank / SSC); real GDP +1.4 % 2023, +4.1 % 2024 (SSC preliminary; non-oil sector +6.3 % vs oil −2.4 %)
- **Currency**: **AZN** (Azerbaijani manat). 1 USD ≈ **1.70 AZN** (de-facto peg held since 2017 by CBAR — Central Bank of Azerbaijan Republic; see `--currency`); 1 EUR ≈ 1.78–1.85 AZN floating with USD/EUR cross
- **Languages**: **Azerbaijani** (official, Azərbaycan dili — Latin script since 2001 transition from Cyrillic); Russian widely understood in Baku + business + over-40s; English in Baku CBD + tourism + IT; Turkish broadly mutually intelligible (Oghuz cluster); Persian in southern districts (Lankaran, Astara)
- **EU/CIS status**: Member of CIS (founder); Eastern Partnership member (EU); **no EU candidate status**; bilateral PCA + Strategic Partnership negotiation since 2017; OSCE + Council of Europe member
- **Postcode**: 4 digits with `AZ` prefix per Azərpoçt scheme (e.g., Baku centre `AZ1010`, Yasamal `AZ1100`, Khatai/Khatayi `AZ1003`–`AZ1078`, Sumqayit `AZ5000`–`AZ5018`, Ganja `AZ2000`)
- **Admin levels**: 11 economic regions → 66 rayons (districts/raions) + 11 cities of republican subordination + 1 autonomous republic (Naxçıvan/Nakhchivan, exclave) → ~4,500 municipalities + settlements. Karabakh + East Zangezur economic regions reintegrated 2020–2023 (see Caveats)
- **Cadastre**: **State Service on Property Issues (SCSI)** under Ministry of Economy — `https://emlak.gov.az/` operates the State Register of Real Estate (Daşınmaz əmlakın dövlət reyestri); citizen interface via **e-emlak.gov.az** + **e-gov.az** (single sign-on) + **ASAN Service** one-stop offices nationwide
- **Identifier**: Real Estate Cadastral Number (`Daşınmaz əmlakın kadastr nömrəsi`) format `XX-XXX-XX-XXXX-XXX` (region.district.block.parcel.unit) per Law on Real Estate State Register No. 270-IIIQ of 2004
- **Foreign-buyer rule** (2026-05-27 verified, sources Land Code Art. 48.3 + Art. 49, AZ MFA New Delhi reference document, emze.az, vlolawfirm.com, norma.az): **foreigners may own buildings / apartments / individual houses** as full freehold structures, with same registration/rights as AZ citizens (Constitution Art. 13 + Civil Code Art. 152). **Foreigners CANNOT own LAND of any class** — agricultural, forest, residential plot, urban — per **Land Code Art. 48.3** (foreigners lease only) **+ Art. 49** (ag/forest/border ownership ban). For an apartment in a multi-unit building, this is moot (land is collective/state). For a **standalone house with plot**, the foreigner owns the structure but the land must be held under a long lease (up to 99 years) from the State or AZ private landowner. **Border zones + strategic-security areas** require case-by-case approval (often denied) per Cabinet Decree on Border Regime. Foreigners must register acquired property at SCSI within **1 month** of deed signing.
- **Visa**: **Visa-free 30–90 day** entry for ~70 nationalities (Russia, Türkiye, GCC, Israel, Belarus, CIS); **e-visa via ASAN Visa** (`https://evisa.gov.az/`) for ~100 nationalities incl. EU, UK, US, CA, AU, NZ, JP, KR — 3-day processing, ~US$25 fee; visa-on-arrival NOT generally available

---

## Section: `--price`

### Primary sources

- **SSC (State Statistical Committee — Dövlət Statistika Komitəsi)**: `https://www.stat.gov.az/`
  - Quarterly **Real Estate Statistics** (Daşınmaz əmlakın statistikası) — average per-m² for new + secondary residential by city + region
  - Annual House Price Index (since 2018; base 2015 = 100); Q4 2024 nationwide index ~178 → +9.2 % YoY (per SSC release Mar 2025 — verify)
  - Sub-indices: Baku vs regional cities; primary (new build) vs secondary (resale)
- **CBAR (Central Bank of Azerbaijan Republic)**: `https://www.cbar.az/` — quarterly Financial Stability Report includes mortgage debt + house-price commentary
- **SCSI cadastre extracts** (paid): `https://e-services.economy.gov.az/` — full title + ownership + cadastral plan via e-gov.az auth or any ASAN Service centre (~AZN 5–20 standard, AZN 30–60 urgent — verify current SCSI tariff)
- **İpoteka və Kredit Zəmanət Fondu (İKZF — Mortgage and Credit Guarantee Fund)**: `https://mcgf.gov.az/` — publishes subsidised-mortgage loan counts and volumes and rent-to-own unit counts (59,970 loans / AZN 4,087,056,037 / 10,092 rent-to-own units as at 2026-09-18). **An average per-m² price for qualifying inventory is not published here — verify with the State Statistical Committee (stat.gov.az) if a per-m² cross-check is needed** (2026 data, source İKZF; 2026-09-18 verified)

### Price benchmarks (2024–2025 reference)

| Locality | New-build avg AZN/m² | Resale avg AZN/m² | USD/m² (≈) | Source |
|---|---:|---:|---:|---|
| Baku Sahil/Yasamal/Nəsimi prime CBD | ~AZN 3,200–5,500 | ~AZN 2,400–4,200 | ~$1,900–3,200 (new) / $1,400–2,500 (resale) | Bina.az + Tap.az aggregate Q4 2024; Colliers Baku 2024 review |
| Baku Nərimanov/Xətai middle | ~AZN 2,200–3,000 | ~AZN 1,500–2,200 | ~$1,300–1,800 / $880–1,300 | Bina.az aggregate Q4 2024 |
| Baku Sabunçu/Suraxani/Bilgəh outer | ~AZN 1,200–1,800 | ~AZN 800–1,400 | ~$700–1,060 / $470–820 | Tap.az 2024-Q4 |
| Sumqayit | ~AZN 900–1,500 | ~AZN 600–1,000 | ~$530–880 / $350–590 | Bina.az aggregate Q4 2024 |
| Ganja (Gəncə) | ~AZN 700–1,200 | ~AZN 450–800 | ~$410–700 / $260–470 | Tap.az 2024-Q4 |
| Quba / Qəbələ (resort/ski) | ~AZN 1,500–3,500 (apt-hotel) | ~AZN 900–2,000 | ~$880–2,060 / $530–1,180 | Lalafo.az + Bina.az resort segment |
| Lankaran / Astara (south) | ~AZN 500–900 | ~AZN 350–600 | ~$290–530 / $200–350 | Tap.az regional 2024 |
| Naxçıvan (exclave) | ~AZN 800–1,400 | ~AZN 500–900 | ~$470–820 / $290–530 | Bina.az aggregate (thin sample) |

> All AZN/m² are **est.** (calibration: cross-checked against SSC quarterly average + ≥ 2 listing aggregators). Listing platform medians vary widely by sub-district; verify with 5+ comparables on the same street + same building era. USD figures use 1.70 AZN/USD CBAR peg.

### Listing platforms

- **Bina.az** — largest real-estate portal: `https://bina.az/` *(per listing — verify with cadastre / on visit)*
  - Filters: city → rayon → metro/landmark; sale/rent; new build vs resale; m²; floor/total; renovation grade
- **Tap.az** — long-running classifieds incl. real estate: `https://tap.az/elanlar/dasinmaz-emlak` *(per listing — verify with cadastre / on visit)*
- **Lalafo.az** — broader classifieds with active RE category: `https://lalafo.az/azerbaijan/nedvizhimost` *(per listing — verify with cadastre / on visit)*
- **EvDe.az**, **Yeniemlak.az**, **Birja.az** — smaller real-estate portals *(per listing — verify with cadastre / on visit)*
- **Facebook + Telegram channels** (e.g., `t.me/baki_emlak`) — high volume, unverified
- Developer-direct portals (Pasha Construction, Akkord, Baku White City, Crescent Bay) for new-build aggregation

### Verdict bands (residential AZN/m², Baku reference)

- 🟢 within ±10 % of district segment median (per Bina.az / Tap.az, ≥ 5 comparables same street + condition)
- 🟡 ±20 %
- 🟠 ±30 % — investigate: pre-1990 panel? District heating connection? Self-built (kustar) status? Border-zone restriction?
- 🔴 > ±30 % — significant red flag

### Compute

1. AZN/m² = listing AZN ÷ m² advertised. Many Baku high-end listings priced in **USD** (because of historical TRY/RUB volatility insurance) but contracts denominated in **AZN** at CBAR reference rate on signing day
2. Compare to SSC quarterly bulletin for Baku rayon
3. **Trap**: Soviet-era "ümumi sahə" (general area) typically includes walls + balcony at 100 % — confirm vs "yaşayış sahəsi" (living area) on listing
4. **Trap**: "təmirsiz" / "bare frame" (kustar bina) new-build = no internal finishing — finishing typically adds AZN 350–700/m² (est., from Baku contractor classifieds 2024 — verify per quote)
5. **Trap**: "Stalinka" pre-1955 buildings priced as heritage in Baku Sahil/İçəri Şəhər — heritage register restrictions may block STR-grade renovation (check with Ministry of Culture)
6. **Trap**: parking is rarely included in apartment price; expect AZN 15,000–45,000 for an underground space in central Baku (est. — verify per development)
7. **Trap**: "Ağ ev" (White City) Bibiheybət regeneration zone — premium pricing for redevelopment-zone certificates

---

## Section: `--traffic`

### Primary sources

- **State Highway Agency (Azərbaycan Avtomobil Yolları Dövlət Agentliyi — AAYDA)**: `https://aayda.gov.az/` — annual traffic counts on M-prefix (republic) + R-prefix (regional) roads
- **Ministry of Digital Development and Transport** (`https://mincom.gov.az/`) — sectoral plans, road master plans, port + rail context
- **AYNA — Azərbaycan Yerüstü Nəqliyyat Agentliyi** (Azerbaijan Land Transport Agency; successor to the Baku Transport Agency / *Bakı Nəqliyyat Agentliyi*, BNA): `https://ayna.gov.az/` — Baku bus routing and stops, taxi regulation, freight, coach stations and the city's 5 paid-parking zones. **Baku Metro is operated separately by Bakı Metropoliteni — AYNA is ground transport only** (2026 data, source AYNA; 2026-09-18 verified)
- **Baku Metropoliten** (`https://metro.gov.az/`) — Baku metro (3 lines, 27 stations as of 2025; expansion ongoing)
- **Yandex Maps + Google Traffic** — only commercial-grade real-time fallback in AZ (Yandex is dominant locally)

### Key term

**AADT** equivalent in Azerbaijani: `orta gündəlik illik nəqliyyat axını` (often abbreviated OGİNA) or simply `gündəlik trafik intensivliyi`

### Verdict bands (residential noise impact)

- 🟢 < 1,000 v/d (rural side road, village street)
- 🟡 1,000–5,000 v/d (small municipal road, urban side street)
- 🟠 5,000–20,000 v/d (urban arterial, M-route republic highway)
- 🔴 > 20,000 v/d (Baku inner ring — Heydər Əliyev pr., Neftçilər pr., 28 May küç.; M1 Baku–Russia border; M2 Baku–Georgia border; M3 Baku–Iran border)

### Coarse fallback (OSM `highway` class)

- `motorway` = M-prefix republic highway
- `trunk`/`primary` = R-prefix regional road
- `secondary` = il/rayon road
- `tertiary` = local connector
- `residential` = mahalla/küçə (neighbourhood street)

### Notes

- **Baku metro** (3 lines, Red/Green/Purple) is the dominant rapid-transit + reduces traffic exposure for properties near stations; expansion to Khojasan + Air Port lines underway
- Baku private-vehicle fleet roughly tripled 2010 → 2024 per SSC transport stats; congestion now severe on Heydər Əliyev pr., Neftçilər pr., 28 May küç., Tbilisi pr., Bibiheybət axis
- **M1 Baku–Russia border** widening + **M2 Baku–Georgia border** four-laning ongoing under EU-Asia Trans-Caucasus Corridor (Middle Corridor) — properties along corridor see noise+ during works; long-term port Baku/Alat freight uplift
- **Trap**: properties advertised "5 dəq metroya" (5 min to metro) — confirm walking distance vs marshrutka shuttle; outer-Baku stations have wide catchment with mixed-quality access
- **Trap**: rural properties advertised "yola yaxın" (close to road) — usually mean **on** a slip road or unpaved access — verify setback + paved access on visit

---

## Section: `--tax`

### Currency note

AZN, USD/AZN ≈ 1.70 (CBAR de-facto peg since 2017). All tax computations in AZN; foreign-currency cash payments restricted by 2016 Cabinet Decision (see `--currency`).

### Annual property tax — Əmlak vergisi (Tax Code Art. 196–202)

Governed by [Tax Code of the Republic of Azerbaijan](https://www.taxes.gov.az/) Title VIII; rates set centrally by Tax Code with municipal collection.

**Residential immovables (apartments + houses) — natural persons** (Art. 198; 2026-05-27 verified, sources PwC Worldwide Tax Summaries Azerbaijan + Tax Code Art. 198):

The tax is **AZN-per-m² of inventory area** (NOT a percentage of cadastral value), with a value-based 0.6 % uplift only above the 120 m² band:
- up to 30 m² inventory area: **0 %** (exempt floor)
- 30–120 m² portion: **AZN 0.4/m² base rate** in Baku; AZN 0.3/m² in Sumqayit / Ganja / Absheron / other republican-subordination cities; AZN 0.2/m² in other cities; AZN 0.1/m² in rural settlements
- 120 m²+ portion: same per-m² base **plus** 0.6 % of inventory value attributable to the area above 120 m²

**Baku district (rayon) coefficient** (2026-05-27 verified, source PwC + Wikipedia Taxation in Azerbaijan): the Baku base AZN 0.4/m² is multiplied by a **location coefficient of 0.7 to 1.5** depending on rayon, so effective Baku per-m² rates range AZN 0.28–0.60/m² before the above-120 m² 0.6 % component triggers. Confirm rayon coefficient via the rayon municipal tariff or e-gov.az before final computation.

**Property of legal entities** (Art. 199):
- 1 % of average annual book value of fixed-asset immovable property; collected by State Tax Service

**Land tax — Torpaq vergisi** (Tax Code Art. 206–209):
- Agricultural land: per-hectare fixed rates by zone (Annex 2 to Tax Code) — typically AZN 0.06–0.30/ha for arable
- Non-agricultural land (residential plot under house): per-m² rates by city zone — Baku 1st zone ~AZN 0.6/m²/yr; rural ~AZN 0.1/m²/yr (verify Annex 2)

### Example calculation

A AZN 200,000 (≈ US$118k) Baku Yasamal 100 m² apartment, owner natural person:
- 30 m² exempt → 70 m² taxable at AZN 0.4/m² = **AZN 28/yr (~US$16)**
- (Cadastral value < 120 m² band, no % component triggered)

Same apartment in Ganja (regional city), 100 m²:
- 30 m² exempt → 70 m² × AZN 0.3/m² = **AZN 21/yr (~US$12)**

A 200 m² Baku Sahil flat, AZN 1.2 million market value, cadastral value AZN 800,000:
- 30 m² exempt; 30–120 m² band = 90 m² × AZN 0.4 = AZN 36; above 120 m² = AZN 36 + 0.6 % × (cadastral value attributable to 80 m² above 120 band) → estimated AZN 36 + ~AZN 1,920 = **~AZN 1,956/yr (~US$1,150)**

> Property tax in AZ is **materially low** in absolute AZN terms compared to Western Europe; the m²-based mechanic + 30 m² exempt floor means most modest Baku flats (60–90 m²) pay AZN 12–36/yr. The 0.6 % component triggers only above 120 m². Verify per ASCİ/SCSI cadastral inventory record.

### Transaction taxes (one-time at purchase)

- **VAT (ƏDV — əlavə dəyər vergisi)** — Tax Code Title XI:
  - Standard rate **18 %** (Art. 173)
  - **First sale of residential immovable by licensed developer**: **0 % VAT** (Art. 164.1.5 — accommodation/residence VAT exemption + housing-specific construction VAT regime as amended 2019)
  - **Resale between individuals**: VAT exempt (Art. 164.1)
- **Notary fee** (Law on Notary No. 560-IQ of 1999 + Cabinet Decree on Notarial Tariffs):
  - Sliding 0.5–1.0 % of contract value (capped) — typical residential resale ~0.5 %
  - Notarisation **mandatory** for any immovable property transfer (Civil Code Art. 152 + Notary Law)
- **State duty (dövlət rüsumu)** — Law on State Duty No. 223-IIQ of 2001:
  - Real estate registration **AZN 50–500** fixed (varies by category); apartment registration typically AZN 50–100
- **Stamp duty / contract registration**: typically **0.1–0.5 %** of contract value (Tax Code Art. 84 stamp duty; sliding by transaction class — verify current rates)
- **SCSI cadastral registration fee**: ~AZN 10–30 standard, ~AZN 50–100 urgent (verify SCSI tariff)
- **Total transaction cost** (buyer side, individual–individual resale): typically **1–2 % of price** before agent commission

### Capital gains tax on residential property — individual sellers (2026-05-27 verified, source Caspian Legal Center "Taxation of capital gains in Azerbaijan")

- Individual-seller property gains are **NOT** taxed on net gain at the general PIT rate. A **simplified property-transfer tax is withheld by the notary** (notary acts as the seller's tax agent) at deed signing, calculated as **per-m² unit price × statutory coefficient** under the Art. 220-series simplified-tax schedule. The proceeds are then **excluded from the seller's annual taxable income**.
- The prior playbook claim of a "3-year primary-residence exemption under Art. 102.1.18" is **NOT corroborated** by PwC, Caspian Legal Center, or current taxes.gov.az text (appears transposed from CZ/RU/SK analogs); **treat as fabricated pending direct Tax Code verification** at taxes.gov.az. Do not rely on it for buyer/seller planning.
- **Non-resident individual**: 10 % WHT on gross transaction value of AZ-located immovable is widely cited but the article anchor needs re-verification against current Tax Code text (data not publicly verified — verify at taxes.gov.az).
- **Legal-entity seller**: gain included in 20 % CIT base.

### Personal income tax — general (Tax Code Art. 101; 2026-05-27 verified, sources Wikipedia Taxation-in-Azerbaijan + QuickBooks Global Tax Tables + Caspian Legal Center 2025/2026 amendment summaries)

- **PIT is progressive, NOT a 14 % flat rate** (the prior playbook framing conflated the general regime with the non-oil employee incentive). Standard bands (Art. 101):
  - Monthly income up to **AZN 2,500**: **14 %**
  - Monthly income above AZN 2,500: **AZN 350 + 25 %** on the excess
- The **0 % up to AZN 8,000 / 14 % above** band is a **separate 7-year incentive** for non-oil non-government **employees** of private-sector employers (Law of 1 Jan 2019, originally sunset 2026). From **1 Jan 2026** the non-oil private-sector employee scheme transitions to a graduated structure (2026 budget package, first reading; cross-check final text at meclis.gov.az): up to AZN 2,500 → **3 %** (rising 5 % in 2027, 7 % in 2028); 2,500–8,000 → AZN 75 + 10 % over 2,500; >8,000 → AZN 625 + 14 % over 8,000.
- **Rental income from residential property paid to individuals**: **14 %** for 2024–2025; **reduced to 10 %** from **1 Jan 2026** (APA 2026-budget-package reporting; Caspian Legal Center 2026 amendments — cross-check final text). Notary or tax-agent withholds at source.
- **Corporate income tax (CIT)**: 20 % (Tax Code Art. 105)
- **Dividend WHT**: 10 % (Art. 122)

### AML / cash limits

- Cash payments by legal entities: capped per Cabinet Decision on Cash Discipline; **AZN 30,000** per transaction is the residential-resale practical ceiling (Decree on Cash Operations 2016 — verify current cap)
- Bank-to-bank wire is the standard channel for any transaction > AZN 10,000
- Notaries are AML "obligated entities" under **Law on Prevention of Money Laundering and Financing of Terrorism No. 767-IIIQ of 2009** — must verify source of funds; PEP screening mandatory
- **Financial Monitoring Service (FMS / FIU-Azerbaijan)** — a **standalone public legal entity since Presidential Decree No. 95 of 25 May 2018** (it sat under the Central Bank only from its creation by Decree No. 66 of 23 Feb 2009, and under the Financial Markets Supervision Authority from 3 Feb 2016): `https://fiu.gov.az/` — AML/CFT supervision, national risk assessment, red flags and reports. **CBAR** (`https://www.cbar.az/`) is the separate banking regulator (2026 data, source FMS; 2026-09-18 verified)

### Future risk

- **Tax Code amendments** typically announced annually via Milli Məclis budget law (December); monitor `https://www.taxes.gov.az/` + `https://meclis.gov.az/`
- **2018 Tax Reform** (PIT 14 % flat + 0 % non-oil 7-year incentive): non-oil private-sector incentive originally sunset 2026 — extension/modification likely; verify
- **EU Eastern Partnership** alignment: indirect tightening of beneficial-ownership transparency (no concrete bill 2025–2026)
- **Karabakh + East Zangezur reconstruction zones**: special tax incentives for investment 2024–2030 (Presidential Decree on State Programme for Restoration; verify zones at karabakh.gov.az)

---

## Section: `--rental`

### Long-term residential

- **Individual landlord**: residential rental income taxed at **14 %** (2024–2025) → **reduced to 10 % from 1 Jan 2026** (Tax Code Art. 101; APA 2026-budget-package reporting / Caspian Legal Center 2026 amendments — cross-check final text). PIT is progressive in general (see `--tax`); this is the residential-rental-specific rate. Declared annually via personal income return at State Tax Service (Vergilər Nazirliyi)
- **Tenant-side withholding**: if tenant is a legal entity, **14 % WHT at source** is the standard practice (Art. 124); no further declaration if WHT applied
- **Foreign / non-resident landlord**: same 14 % flat PIT; foreign-source-of-funds declaration may be required for AML
- **Contract registration**: not strictly mandatory for residential leases but increasingly enforced via SCSI for tax compliance — verify per case
- No rent-control regime nationally; private-law contracts (Civil Code Art. 700+) govern; standard 1-year tenancies with one-month notice

### Short-term rentals (STR / Airbnb / Booking)

#### Regulatory framework

- **Law on Tourism No. 674-IQ of 1999** (as amended) + **Cabinet Decree No. 1146 of 11 Aug 2017** on Classification of Hotel-type Accommodation Establishments — created mandatory classification + registration regime
- **State Tourism Agency (Azərbaycan Turizm Bürosu)**: `https://tourism.gov.az/` (formerly Ministry of Culture & Tourism) — issues classification certificates
- **STR-specific rules**: hosts of "qonaq evi" (guest house) / "günlük kirayə" (daily rental) must register accommodation activity, obtain `təsnifat sertifikatı` (classification certificate) per Decree 1146 + Tourism Law amendments 2018
- **Municipal layer**: Baku municipality (BBİ) requires additional registration for short-term rental in tourist zones (Sahil, Fountains Square, İçəri Şəhər) — verify current at baku-ih.gov.az

#### Tax classification

- **Individual host operating informally**: 14 % PIT on net rental + risk of being reclassified as "sahibkarlıq fəaliyyəti" (entrepreneurial activity) → triggers IE registration
- **Sole proprietor / IE (`fərdi sahibkar`)** with STR activity: simplified tax regime available — **2 % flat on turnover** under Tax Code Art. 218–222 (Simplified Tax for individuals/SMEs) for activity in Baku; **2 % outside Baku** (verify current rate per Art. 220)
- **Above AZN 200,000 annual turnover**: must transition to standard CIT regime (20 % CIT on profit + 10 % dividend WHT) and register VAT mükellefi (Art. 154)
- **VAT (ƏDV)**: 18 % if STR turnover > AZN 200,000/12 months — accommodation services are within VAT scope
- **Tourist tax / accommodation tax**: no national tourist tax 2025; some Baku area resorts apply municipal levies — verify per locality

#### Practical (2025–2026)

- Enforcement of classification has tightened post-2017 Decree 1146 + post-2024 Tourism Strategy 2025–2030; informal STRs face fines AZN 200–800 per platform listing
- **Trap**: HOA (`mənzil-tikinti kooperativi` / MTK or `mənzil mülkiyyətçilərinin alyansı`) bylaws may restrict STR in newer Baku developments — check before buying
- **Trap**: pre-1991 panel buildings (Khrushchovka 5-storey + 9/16-storey panels — sometimes called "Lenin layihəsi") have entrance security + concierge ("liftçi") incompatible with self-check-in; tenant-mix friction common

### Strategic notes

- **Baku Sahil/İçəri Şəhər/Fountains Square/Yasamal**: highest year-round STR yield; Eurovision 2012 + Formula 1 European Grand Prix (2017–) + Caspian Tourism + post-2017 visa liberalisation drive demand
- **İçəri Şəhər (UNESCO Walled City) heritage zone**: high nightly rate but heritage-listing restrictions on renovation; verify with Ministry of Culture before purchase
- **Quba/Qəbələ resort zones**: seasonal demand (May–Oct peak); ski-shoulder Dec–Mar at Shahdağ resort
- **Baku LTR (long-term residential)**: gross yields commonly cited **5–8 %** (Bina.az / Colliers 2024 — verify against your specific listing)

---

## Section: `--work=<profession>`

### Job platforms

- **Job boards** (commercial, ⚠️ not primary): `https://www.hellojob.az` · `https://boss.az` · `https://jobsearch.az` — listed as examples only; **no ranking or market-share claim is sourceable**. For labour-market figures use the **State Statistical Committee (stat.gov.az)** or the State Employment Agency
- **Jobsearch.az** — long-running general: `https://jobsearch.az/`
- **Boss.az** — IT + finance focus: `https://boss.az/`
- **Offer.az** — broader classifieds + jobs: `https://offer.az/`
- **LinkedIn Azerbaijan** — active in IT, finance, oil/gas, BPO
- **DOST Agency for Sustainable and Operational Social Provision** (`https://dost.gov.az/`) — public employment service + labour stats

### Self-employment regimes (foreigners eligible with valid work permit / residence)

- **Individual Entrepreneur (Fərdi sahibkar — FS)**: register at State Tax Service in 1–3 days; default Simplified Tax 2 % on turnover (residential STR + small services qualify)
- **MMC (Məhdud Məsuliyyətli Cəmiyyət — LLC)**: 1-day ASAN/MOJ registration; minimum capital AZN 10; 20 % CIT on profit + 10 % dividend WHT
- **Tax residency**: 183+ days in any 12-month period OR centre of vital interests in AZ (Tax Code Art. 13)

### Tech / IT-specific incentive

- **High Technology Park (Yüksək Texnologiyalar Parkı — YTP)** at AZ-Tech Park / Pirallahi (Law on High Technology Park 2012 + Presidential Decree 2018): residents pay reduced taxes on qualifying IT activity — typically 0 % CIT + 0 % VAT + 0 % property tax for first 7–10 years (verify current eligibility at `https://ytp.az/`)
- **IDDA / İRİA — İnnovasiya və Rəqəmsal İnkişaf Agentliyi** (Innovation and Digital Development Agency; successor to the Innovation Agency): `https://idda.az/` — startup support and grants (750+ startups supported, 190+ companies holding non-technopark residency status), plus the Azerbaijan Cybersecurity Centre, Holberton School Azerbaijan and the **mygov ID** national digital identity (2026 data, source IDDA; 2026-09-18 verified)

### Salaried benchmarks

- Average monthly nominal wage 2024 Q4 (SSC): **~AZN 1,050 gross** (~US$620) — economy-wide; non-oil private sector ~AZN 870
- IT/finance Baku: ~AZN 2,500–6,500/month for mid-level (HH.az market reports 2024)
- Oil & gas (SOCAR + BP + TPAO): ~AZN 3,500–12,000/month senior technical (industry sources)
- **Minimum wage 2025**: **AZN 400/month** (set by Presidential Decree; revised periodically — last raised 2022; verify at gov.az); apparent low base masks high-density informal-economy participation in non-oil services

### Catchment heuristics

- Within 30 min of Baku central rayons: full salaried opportunity (oil & gas, finance, IT, BPO, government, diplomatic)
- Sumqayit: regional industrial + chemical + petrochemical + Baku commute (~30 min)
- Ganja: regional industrial + agro + Trans-Caucasus rail/road logistics; thinner labour market
- Mingachevir: hydropower + textile; thin
- Naxçıvan exclave: regional administrative + cross-border (Iran/Türkiye) trade; isolated labour market
- Karabakh + East Zangezur reconstruction zones: rapid 2024–2030 buildout (construction, public-sector, displaced-return support); structural demand

### Visa / residence pathway for working foreigners

- **Visa-free 30–90 days** for ~70 nationalities (CIS, Türkiye, Israel, GCC) + e-visa for ~100 (EU, UK, US, CA, AU) — covers business-trip + scoping
- **Temporary Residence Permit (TRP — müvəqqəti yaşamaq icazəsi)**: tied to employer, business activity, real-estate threshold (≥ AZN 100,000 ≈ US$60k purchase qualifies — see `--visa`), study, or family reunification → 1-year renewable; renewals to 5+ years
- **Work Permit (iş icazəsi)**: required for foreign employment via [State Migration Service](https://migration.gov.az/); employer-sponsored; quota system (typically 1 foreign worker per 5 AZ-citizen workers in same employer)
- **Permanent Residence (daimi yaşamaq icazəsi)**: after **8 years continuous TRP** (Law on Migration No. 713-IVQ of 2013)
- **Naturalisation**: after **5 years PR** + Azerbaijani-language proficiency + renunciation of prior citizenship (dual citizenship NOT generally permitted; very limited Presidential discretion)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Republic Seismological Survey Center (RSSC — Respublika Seysmoloji Xidmət Mərkəzi)** | `https://seismology.az/en` | Real-time + historic seismicity, fault maps, intensity scenarios |
| **Ministry of Emergency Situations (FHN — Fövqəladə Hallar Nazirliyi)** | `https://fhn.gov.az/` | Operational hazard data, flood/fire response, civil protection |
| **National Hydrometeorology Department (Milli Hidrometeorologiya Departamenti)** | `https://www.eco.gov.az/` (under MENR) | Weather, flood warnings, climate baseline |
| **Ministry of Ecology & Natural Resources (MENR — Ekologiya və Təbii Sərvətlər Nazirliyi)** | `https://eco.gov.az/` | Environmental risk reports, climate strategy, geo-hazards |
| **Geological Service (GSC — Milli Geoloji Kəşfiyyat Xidməti)** | (under MENR) `https://eco.gov.az/` | Geological maps, mud-volcano + landslide registry |
| **State Service on Property Issues (SCSI)** | `https://emlak.gov.az/` | Cadastre + zoning + restricted-zone flag (border / strategic) |
| **Caspian Sea Sustainable Development monitoring** | (Tehran Convention regional) | Sea-level + ecosystem monitoring |

### Seismicity — material concern

- AZ sits on the **Greater + Lesser Caucasus collision zone** + Caspian foredeep — moderate-to-high seismicity (Mw 6–7 historically possible)
- **Major historical events**:
  - **2000-11-25 Baku Mw 6.8** (Caspian offshore epicentre, ~25 km depth) — ~30 deaths, significant Baku building damage; widely cited reference event
  - **2012-05-07 Zaqatala Mw 5.7** — northern AZ, minor structural damage; reminder of Greater Caucasus active faulting
  - **2019 + 2023 Shamakhi/Şamaxı district minor swarms** — Mw 4–5 range, no casualties; ongoing seismicity
- AZ designated **MSK seismic intensity zone 7–8** (Baku coastal 8; inland 7); design PGA ~0.20–0.30 g per **AzDTN 2.4-1 (Azerbaijan Construction Norms 2010, seismic-resistant design)** + revisions 2015/2018 (aligned with Russian SNiP + partial Eurocode 8)
- **Pre-1991 Soviet panel-block stock** (Khrushchovka 5-storey, 9/16-storey panels — Lenin / 1-464 / 1-468 / 105 series): retrofit status uneven; some demolished + rebuilt under Baku Master Plan; many in service — **independent structural survey strongly advised** before purchase

### Mud volcanoes — Absheron Peninsula unique hazard

- AZ has the **world's highest concentration of mud volcanoes** (~400 of ~1,000 globally), concentrated on Absheron Peninsula (Baku surroundings) + Garadagh + offshore Caspian
- Most are **dormant cones with intermittent activity**; major eruptions episodic (Lokbatan 2001/2018; Bozdag 2021; Dashgil + Otman Bozdag periodic)
- Hazard: methane release + cone instability → **building setback + zoning restrictions** in known mud-volcano zones (Lokbatan, Şıxov, Otman Bozdag, Qobustan)
- Verification: **Geological Service of MENR** publishes mud-volcano register (Russian/Azerbaijani only); commune-level zoning via SCSI
- Trap: outer-Baku peripheral developments occasionally encroach on dormant cones — verify on-site + check geo-zone designation

### Flood

- Major rivers: **Kura (Kür)** + **Araz/Aras** + smaller Caucasus tributaries
- **Major flood events**: 2010 Kura/Araz widespread (60k+ displaced); 2016 Imishli/Saatli; 2021 Greater Caucasus southern slope flash floods
- **Flood hazard maps**: FHN + MENR publish at locality level; **EU + UN-supported flood-risk assessment** under Tehran Convention partnership (verify map availability at `https://www.fhn.gov.az/`)
- **Caspian sea-level dynamics**: historical rising 1978–1995 (+2.5 m), then **falling** ~1m 2010–2024 per Caspian monitoring (Tehran Convention reports); **coastal flooding risk evolving** — receding shorelines also expose infrastructure mismatches; verify per coastal locality

### Landslide / soil instability

- **Greater Caucasus southern slope** (Quba, Qusar, Şamaxı, Qəbələ, Qəbələ-Zaqatala axis): significant landslide susceptibility, particularly post-rainfall
- **Lesser Caucasus** (Karabakh, Kalbajar, Lachin reintegrated zones): post-conflict + post-displacement reconstruction underway; geological surveys ongoing 2024–2030 → uncertainty on reconstructed-property risk profile
- **Verification**: GSC landslide registry (Azerbaijani-only) + commune-level urban-planning records via SCSI

### Geopolitical risk — Karabakh + East Zangezur context

- **2020 Karabakh War (Sept–Nov 2020)** + **Sept 2023 Karabakh anti-terrorism operation** restored AZ full sovereignty over former Nagorno-Karabakh + adjacent districts
- **Reintegration timeline 2024–2030**: massive de-mining + reconstruction programme (Karabakh + East Zangezur economic regions); cities renamed (e.g., Khankendi formerly Stepanakert; Lachin Corridor reopened May 2023; Khojaly returned)
- **Property-buyer relevance**:
  - Reintegrated zones offer **special tax incentives + subsidised mortgages** for displaced returnees (mostly Azerbaijani citizens) and qualifying investors (Presidential Decree on State Programme for Restoration)
  - **Pre-1992 Armenian-occupied property records**: AZ does NOT recognise documents issued by former de-facto Karabakh authorities; reconstruction proceeds under AZ State Register
  - **De-mining unfinished as of 2026**: ANAMA + international partners progressing but extensive UXO contamination — buyers in reintegrated zones must verify ANAMA clearance certificate
  - Foreign-buyer caution: many reintegrated areas remain restricted-access pending reconstruction
- **Iran border tensions (Nakhchivan + southern AZ)**: periodic; baseline risk modest; Western Zangezur Corridor negotiations ongoing
- **CIS / Russia / Türkiye** triangle: AZ maintains balanced multi-vector foreign policy; minimal direct tail risk
- **Crime**: AZ is **one of the lowest-crime countries in CIS** (UNODC + IGP — IGP equivalent: Daxili İşlər Nazirliyi); Baku tourist-zone safety high

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1918 (Tsarist + 1st Republic)** | Soft-fired brick + lime mortar; lead paint likely; weak seismic performance; many heritage-listed (İçəri Şəhər UNESCO + Sahil district) |
| **1918–1955 (early Soviet, Stalinist)** | "Stalinka" buildings; thicker walls + better seismic than later panels; asbestos in some roofing; oil-boom Baku architectural heritage |
| **1955–1991 (Khrushchyov + Brezhnev panels)** | Khrushchovka 5-storey + 9 + 16-storey panels (1-464, 1-468, 105 series); asbestos joints common; aging utility risers; some seismic retrofits ongoing |
| **1991–2003 (post-Soviet collapse)** | Often unpermitted ("kustar" / self-build); legalised in waves under amnesty laws — verify SCSI recordation |
| **2003–2014 (oil-boom Baku)** | Building boom; quality varies; 2010 AzDTN 2.4-1 seismic code overhaul tightened standards; "Flame Towers" + Crystal Hall + White City completed |
| **2014–present** | Modern code (AzDTN 2.4-1 with 2015/2018 amendments); seismic + fire stricter; energy-efficiency requirements 2020+ (verify current at MENR + Ministry of Economy) |

**Asbestos**: pre-2005 likely in roofing + insulation; no national mandatory removal regime — buyer due diligence required.

### Mandatory documents at sale

| Document | Required because | Notes |
|---|---|---|
| **SCSI extract (Çıxarış)** | All sales | Verify owner + cadastral number + encumbrances (`girov` / mortgage, `həbs` / seizure) |
| **Notarised sale-purchase contract** | All sales (Civil Code Art. 152) | Mandatory; in Azerbaijani; SCSI recordation within 1 month |
| **Cadastral plan** | All sales | Issued by SCSI; ensure matches building footprint |
| **Technical passport (texniki pasport)** | Older buildings | Confirms surface, layout — historically issued by ATEM (Azərbaycan Texniki Sənədlərin Mərkəzi); not always current |
| **Building completion / commissioning certificate (istismara qəbul aktı)** | New builds + extensions | Confirms construction completed legally; pre-2007 self-built ("kustar") may lack — affects future renovation/extension permits |
| **No-debt certificate** (utilities, building management fees) | Apartments in managed buildings | From MTK / mənzil mülkiyyətçilərinin alyansı (HOA) — ensure no fond-debts attached to flat |
| **Heritage listing check** | İçəri Şəhər + Sahil + Fountains Square + Old Baku heritage zones | Ministry of Culture register: `https://mct.gov.az/` — listing imposes severe renovation restrictions |
| **Border-zone / strategic-area clearance** | Properties near borders + strategic infrastructure | SCSI flags; foreigners often denied; verify before any deposit |
| **Mine clearance certificate (ANAMA)** | Karabakh + East Zangezur reintegrated zones | Mandatory for any title transfer in reintegrated zones |

### Climate change projections (MENR 4th National Communication 2024)

- Mean annual temperature: +1.0–1.5 °C since 1961; +1.5–4.0 °C projected by 2100 (RCP4.5 / RCP8.5); Mil-Mughan + Kura-Aras lowlands warming faster
- Annual precipitation: regional shift — south + east drier (Salyan, Imishli, Mil-Mughan), Greater Caucasus wetter + flood-prone
- Drought: eastern + central AZ (Aran economic region) projected drier; cotton + wheat agriculture under stress
- Caspian sea-level: 2010–2024 declining ~1m → coastal infrastructure mismatch (port silting, beach loss, sewer outfalls); long-run trajectory uncertain
- Heat: Baku summer days > 35 °C projected to triple by 2050 (MENR 2024); urban heat island Baku CBD pronounced
- **Climate Resilience Strategy 2024** (Cabinet Decision; verify current at eco.gov.az)
- AZ NDC: 35 % GHG reduction by 2030 vs 1990; LT-LEDS 2050 net-zero ambition (announced COP29 Baku 2024)

---

## Section: `--mains`

### National database + operators

- **Tariff Council (Tarif Şurası)**: `https://www.tariffcouncil.gov.az/` — sets utility tariffs (electricity, gas, water, heating)
- **Azərsu OJSC**: `https://www.azersu.az/` — national water + sewer operator (most cities outside Baku Old Town); covers ~85 % of urban population
- **Bakı Su Kanal** (under Azərsu): Baku city water + sewer
- **Azərişıq OJSC**: `https://www.azerishiq.az/` — national electricity distribution (post-2014 consolidation; Baku managed via Bakı Elektrik Şəbəkəsi subsidiary)
- **SOCAR Distribution / Azəriqaz**: `https://www.socar.az/` + `https://www.azeriqaz.az/` — gas distribution (SOCAR upstream + downstream dominant)
- **Azərenerji**: `https://www.azerenerji.gov.az/` — generation + transmission
- **Baku Heat Network (Bakı İstilik Təchizatı)** + regional MMK heat networks — district heating where retained (Sumqayit, Mingachevir; Baku largely individual gas boilers post-Soviet retrofit)

### Verification

1. Listing language:
   - "mərkəzi su + kanalizasiya" = mains water + mains sewer
   - "kombi (qaz)" / "fərdi qaz qazanı" = individual gas boiler (most Baku flats post-1995 retrofit)
   - "mərkəzi istilik" = district heating (rare in modern Baku; common Sumqayit + regional)
   - "quyu" = own well; verify potability + permit
   - "septik" / "lokal kanalizasiya" = no mains sewer; cesspit
2. **Baku urban core + Sumqayit + Ganja**: full mains assumed; **verify with Azərsu before signing** (rare patches of unconnected legacy stock exist on city periphery + outer Absheron)
3. **Rural settlements + dachas (bağ evi)**: often water-only or seasonal water; sewer rare; many rely on cesspits

### Costs

| Scenario | Cost (AZN, est.) |
|---|---:|
| Connection to existing nearby mains (urban) | ~AZN 500–2,500 |
| Mains drain extension (parcel where trunk line exists nearby) | ~AZN 1,500–6,000 |
| Borehole drilling (50–100 m) | ~AZN 3,000–10,000 |
| Septic tank install (typical residential) | ~AZN 1,500–4,000 |
| Modern WWTP (BIO compliance, single-house) | ~AZN 5,000–15,000 |
| Gas connection from street main | ~AZN 800–3,000 |

> All AZN ranges are **est.** based on Baku + Sumqayit 2024–2025 contractor quotes aggregated from Tap.az + Bina.az service classifieds + Azərsu/Azəriqaz published connection schedules. Verify with 2+ quotes per project.

### Utility tariffs (2025–2026, regulated by Tariff Council)

| Utility | Tariff (residential, indicative) |
|---|---|
| **Electricity (Azərişıq, ≤ 200 kWh/month)** | ~0.07 AZN/kWh (~US$0.041) — verify current Tariff Council schedule |
| **Electricity (200–300 kWh/month band)** | ~0.11 AZN/kWh |
| **Electricity (> 300 kWh/month)** | ~0.13 AZN/kWh |
| **Natural gas (Azəriqaz, residential ≤ 1,500 m³/yr)** | ~0.10 AZN/m³ |
| **Natural gas (residential > 1,500 m³/yr)** | ~0.20 AZN/m³ |
| **Water + sewer (Azərsu Baku)** | ~0.35–0.50 AZN/m³ residential |
| **District heating (Baku İstilik / regional)** | varies by network; subsidised; verify Tariff Council schedule |

(Tariffs verified against tariffcouncil.gov.az + azersu.az + azerishiq.az 2025 published schedules — confirm current rates; AZ utility tariffs are heavily subsidised vs cost — adjustment risk over 2026–2030 horizon.)

### Energy supply context

- AZ is a **net energy exporter** (Caspian oil + gas via BTC, BTE, TANAP, TAP pipelines); domestic supply secure with multiple generation sources
- Renewables push 2024–2030: **30 % renewables in installed capacity by 2030** (Strategy 2030 Cabinet Decision); large solar + wind tenders Absheron + Caspian offshore
- COP29 (Baku, Nov 2024) reinforced LT-LEDS net-zero 2050 ambition; reconstruction zones (Karabakh + East Zangezur) being built as "Green Energy Zone" pilot

---

## Section: `--crime`

### Primary sources

- **Ministry of Internal Affairs (Daxili İşlər Nazirliyi — DİN)**: `https://mia.gov.az/` — national crime statistics (limited public granularity)
- **State Statistical Committee (SSC) annual yearbook**: `https://www.stat.gov.az/` — Justice chapter
- **General Prosecutor's Office (Baş Prokurorluq)**: `https://genprosecutor.gov.az/` — prosecutorial statistics
- **UNODC + Numbeo cross-reference** for international comparison

### Headline (2024 DİN + SSC annual data)

- AZ has **one of the lowest registered-crime rates in the CIS region** (UNODC + Numbeo Q1 2026 indices)
- **Total registered crimes 2024**: ~25,000–28,000 nationally (declining trend since 2015)
- **Property-related crimes** (theft, burglary, fraud): ~45 % of total registered
- **Baku municipality**: ~40 % of national total (population share ~24 % — urban-density effect)
- **Homicide rate 2023**: ~2.0 per 100k (SSC) — low by regional standard, declining since 2010
- **Tourist-zone safety**: very high; Baku Sahil + Fountains Square + İçəri Şəhər well-policed

### Verdict bands (parcel-level inference)

🟢 Baku residential rayons (Yasamal, Nəsimi, Nərimanov interiors); Sumqayit + Ganja residential cores; rural rayons low-density villages
🟡 Baku Centre tourist hotspots (rare petty pickpocketing, scam exposure); regional bus-station perimeters
🟠 Specific high-incidence localities (DİN does not publish parcel-grade open data — verify per address with sector inspector)
🔴 No specific routinely-flagged 🔴 zones in Baku; Karabakh + East Zangezur reintegrated zones flagged for UXO/de-mining (separate from civil crime)

### Verification

For parcel-level: visit local police precinct ("rayon polis idarəsi") for informal incident summary; DİN does not publish parcel-grade open data.

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`. AZ is well-mapped on OpenStreetMap (Baku dense + colour-tagged in Latin script `name:az` + Russian `name:ru`; regional cities thinner; Karabakh + East Zangezur mapping rapidly evolving 2024–2026 as reconstruction proceeds). Query with `name:az` preferred; older data may use Cyrillic Azerbaijani (pre-2001) — confirm transliteration.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`. National source: National Hydrometeorology Department (under MENR `https://eco.gov.az/`) + AZ UNFCCC 4th National Communication 2024. Key projections: +1.5–4.0 °C by 2100; drought intensifies south-east (Aran), wetter Greater Caucasus; Caspian sea-level uncertain (2010–2024 declining ~1m); urban heat island Baku CBD pronounced; LT-LEDS 2050 net-zero ambition (announced COP29 Baku Nov 2024).

---

## Section: `--finance`

### Mortgage market

- **Regulator**: [CBAR — Central Bank of Azerbaijan Republic](https://www.cbar.az/) — sets prudential rules, monetary-policy rate (refinancing rate 7.25 % Q1 2026 — verify), loan-classification rules
- **Major banks** (CBAR 2024 supervisory list — 26 licensed banks):
  - **Kapital Bank** (largest retail; PASHA Holding)
  - **PASHA Bank** (corporate + retail; PASHA Holding)
  - **International Bank of Azerbaijan (IBA — Beynəlxalq Bank)** (state-owned, partial-privatisation underway)
  - **Bank Respublika**
  - **Bank ABB** (Azerbaijan Beynəlxalq Bankı successor segment)
  - **Unibank**
  - **Yelo Bank**
  - **Rabitabank**, **Bank BTB**, **TuranBank**, **AccessBank**, **Xalq Bank**
- **LTV caps (residential, 2024–2026 CBAR + AMF guidance)**:

| Borrower | Max LTV |
|---|---:|
| Resident first-home buyer (AMF subsidised) | up to **85 %** |
| Resident second-home / investment | typically **70 %** |
| Non-resident foreign buyer | typically **50 %** if accepted at all (case-by-case) |

- **DTI / DSTI**: CBAR Regulation caps debt-service at typically **40–50 %** of net income; income evidence required (tax return + employment contract)
- **Rate structure (2024–2026)**:
  - **Standard AZN-denominated mortgages**: typical 8–15 % nominal (commercial)
  - **AMF (Azerbaijan Mortgage and Credit Guarantee Fund) subsidised programme**: **5–9 % rates** for AZ-citizen first-time buyers meeting income + property-cap criteria — `https://mcgf.gov.az/`
  - **Social mortgage**: even lower rates for state employees + young families + IDPs/displaced from Karabakh — verify AMF current programme
  - 15–25-year tenors standard; 30-year rare
- **Foreigner mortgages**: limited; most AZ banks require resident status + AZ tax residency + 24+ months income history. **Cash purchase is the standard foreign-buyer route.**

### Banking access

- Account opening: **passport + AZ FİN-code (tax ID)** + proof of address + AML KYC (source-of-funds declaration)
- Non-resident accounts available at Kapital Bank, PASHA Bank, IBA, Yelo for EU/US/UK passport holders; Russia/Belarus passport holders face heightened scrutiny under partial international sanctions alignment
- **CBAR strategy 2024**: digital-first banking push + open-banking framework (verify current at cbar.az)

⚠️ **2015–2017 banking crisis legacy**: AZN devalued ~50 % across Feb 2015 + Dec 2015 (oil price shock); IBA recapitalisation + several smaller bank licence revocations; sector now tightly supervised + concentrated in PASHA + Kapital + IBA (>60 % system assets).

---

## Section: `--currency`

### AZN — Azerbaijani manat

- **Code**: AZN; subdivided into 100 qəpik; banknotes 1, 5, 10, 20, 50, 100, 200 AZN
- **Regime**: **de-facto USD peg at 1.70 AZN/USD** maintained by CBAR since **2017 stabilisation** (post-2015–16 dual devaluation)
- **Issuer**: [Central Bank of Azerbaijan Republic (CBAR)](https://www.cbar.az/) — sole issuer; reference rate published daily on `https://www.cbar.az/currency`

### Recent volatility (2015–2026)

- 2015 Feb: managed-devaluation +33 % (1.05 → 1.55 AZN/USD) — oil shock
- 2015 Dec: free-float move +47 % (1.55 → 1.80 AZN/USD)
- 2016 Jan: peak 1.81; CBAR tightened
- 2017–present: **de-facto peg 1.70 AZN/USD** — stable for 9+ years (longest stability period in AZN history)
- EUR/AZN: floats with USD/EUR cross; ~1.78–1.85 range Q1 2026

### What this means for buyers

- **USD buyers**: minimal AZN/USD volatility under peg — but peg is policy-maintained, NOT institutional (no formal currency board); 2015-style devaluation tail risk exists if oil shock recurs without adequate FX reserves
- **EUR buyers**: indirect AZN/EUR volatility via USD/EUR cross; ~5–8 % annualised fluctuation realised 2020–2025
- **AZN-priced contract** is the legal requirement (CBAR + Cabinet Decree on Foreign Currency Operations 2016 — most domestic transactions must be settled in AZN); foreign-currency cash on deposit + foreign-currency settlement increasingly restricted under 2016 Cabinet Decree
- **Hedging**: thin local FX-forward market; minimal capital controls 2025; CBAR + State Customs jointly supervise currency export/import (declarations required > USD 10,000 cash)

### CBAR FX reserves + oil-revenue stabilisation

- **State Oil Fund (SOFAZ — Dövlət Neft Fondu)**: `https://www.oilfund.az/` — sovereign-wealth fund holding ~US$60bn (Q1 2026), dominant FX-buffer
- CBAR + SOFAZ: combined FX reserves ~US$75bn, providing peg-defence capacity for cyclical oil-price pressure (verify current at cbar.az + oilfund.az)
- Policy implication: AZN peg is robust under "ordinary" oil-price cycles; sustained sub-$50 oil for 12+ months would test it (last test 2015–16 → forced devaluation)

### Tail risks

⚠️ AZ is an oil-export-dependent economy (~40 % of GDP, ~85 % of export earnings from hydrocarbons in 2024); diversification programme ("non-oil" target) progressing slowly. Major oil-price shock + SOFAZ drawdown could force peg revaluation similar to 2015–16. Position-size foreign-currency-denominated buyers accordingly. Karabakh reconstruction (~AZN 30bn estimated 2024–2030) pulls SOFAZ disbursements upward.

---

## Section: `--visa`

### Property-linked / investor schemes

| Scheme | Threshold | Visa | PR/citizenship path |
|---|---|---|---|
| **Real-estate-linked TRP (Temporary Residence Permit)** | Real-estate purchase ≥ **AZN 100,000** (~US$60k) | 1-yr renewable | After 8 yrs continuous TRP → PR; +5 yrs → naturalisation |
| **Strategic Investor Visa / Investor TRP** | **AZN 540,000** (~US$320k) investment in priority sectors (Cabinet Decree thresholds) | TRP path | Same path; faster eligibility under priority programmes |
| **Skilled worker / employer-sponsored** | Employment contract + work permit | 1-yr renewable | Standard 8 yrs to PR + 5 yrs to citizenship |
| **Family reunification** | Spouse/parent of AZ citizen/PR | 1-yr renewable | Standard timeline |
| **Visa-free 30–90** | ~70 nationalities (CIS, Türkiye, Israel, GCC) | 30–90 days/180 days | n/a |
| **e-visa via ASAN Visa** | EU, UK, US, CA, AU, NZ, JP, KR + ~100 nationalities | 30 days single/multi | n/a |

### CBI / golden-visa status

- **No CBI (Citizenship by Investment) programme exists in Azerbaijan** as of 2026
- **Naturalisation path**: only via residence (5+ yrs PR after 8+ yrs TRP) + Azerbaijani-language proficiency + renunciation of prior citizenship
- **Dual citizenship NOT generally permitted** (Constitution Art. 53; Law on Citizenship No. 527-IQ of 1998 as amended) — limited Presidential discretion exceptions

### Pathway specifically for property buyers

- **AZN 100,000 real-estate threshold = 1-yr TRP**: among lowest in the region, comparable to Georgia (US$150k short-term residence permit since 1 Mar 2026; US$100k before) and Türkiye (was $200k, ended for property → CBI only at $400k); verify current threshold + procedural requirements at [State Migration Service (Dövlət Miqrasiya Xidməti)](https://www.migration.gov.az/en/useful/8?page=3) before relying
- **Property purchase + TRP → 8 years continuous → PR**: long horizon; requires demonstrable physical presence + tax compliance
- **No real-estate-linked golden visa equivalent to Portugal D7 / Spain DNV / Greece pre-2024**: AZ's real-estate-linked TRP is materially shorter (1-yr) and requires actual residence, not virtual presence

### Karabakh + East Zangezur reintegration zones

- **Special tax + residence incentives** for displaced returnees (Azerbaijani citizens) and qualifying investors per Presidential Decree on State Programme for Restoration
- Foreign-investor pathway evolving 2024–2030; verify current programme at karabakh.gov.az + ministry of economy

---

## Section: `--insurance`

### Mandatory

- **No nationally mandatory home-insurance scheme** for owner-occupiers; private market voluntary
- **Mortgage lenders mandate fire + structure cover** for any mortgaged property (CBAR + AMF guidance; standard practice — verify per bank)
- **Compulsory Property Insurance Law** (Compulsory Insurance Law No. 165-IIIQ of 2011): introduced compulsory insurance for residential property in seismic + flood-prone regions but enforcement on individual residential buyers remains uneven; HOA-level coverage growing — verify per locality
- **Earthquake + natural-disaster cover**: typically embedded in standard homeowner package; sub-limit varies

### Optional (standard market, 2024–2026)

| Cover | Typical premium (AZN/yr, indicative) |
|---|---:|
| Building structure (Baku 2-bed, sum insured ~AZN 200k) | AZN 200–500 |
| Home contents (typical 2-bed) | AZN 100–250 |
| Earthquake top-up | usually +AZN 50–150 if not bundled |
| Flood (riverine) | included in major bundles, sub-limit applies |
| Liability (3rd-party) | usually bundled |

### Major insurers (Financial Market Supervisory Authority + CBAR insurance supervision)

- **PASHA Insurance** (largest non-life; PASHA Holding)
- **Atəşgah Sığorta** (long-running, broad book)
- **AzSığorta** (state segment / public-sector default)
- **Qala Sığorta**, **Azərbaycan Sənaye Sığorta**, **Mega Sığorta**, **Xalq Sığorta** — mid-tier
- Compare via Insurers' Association of Azerbaijan (`https://asa.az/`) + CBAR insurance supervision pages

### Climate trajectory note

⚠️ AZ insurers raising premiums 3–6 %/yr 2023–2026 driven by 2010–2021 flood claims + Caspian sea-level fluctuation + post-2020 reintegration-zone reinsurance rebuild; flood + earthquake sub-limits tightening for Greater Caucasus southern slope + outer Absheron. Check policy schedule + sub-limits before signing.

---

## Section: `--notary`

### Conveyancing process

AZ is **civil-law**; **notar (notarius)** mandatory for any immovable-property transfer per **Civil Code Art. 152 + Law on Notary No. 560-IQ of 1999**. Notarised contract is then submitted to SCSI (State Service on Property Issues) for cadastral recordation. Notaries supervised by **Ministry of Justice (Ədliyyə Nazirliyi)** + Notarial Chamber.

### Standard timeline

| Step | Day | What happens |
|---|---|---|
| 1. Pre-contract / promise of sale (`alqı-satqı vədi müqaviləsi`) | D0 | Buyer pays earnest deposit (`beh` typically 10 %); not strictly required but standard |
| 2. SCSI extract pulled | D0–D5 | Buyer's notary or lawyer obtains current `çıxarış` (e-emlak.gov.az or ASAN Service) |
| 3. AML / source-of-funds review | D0–D14 | Notary verifies; bank channel for any payment > AZN 10,000 |
| 4. Notary sale-purchase deed signed | D7–D21 | Both parties present; deed in Azerbaijani; certified translation if buyer non-Azerbaijani-speaking |
| 5. SCSI recordation | D7–D30 | Within 1 month of deed; SCSI issues updated extract reflecting new ownership |
| 6. Foreigner mandatory registration | D7–D30 | Within 1 month, foreign buyer registers ownership via ASAN Service / e-gov.az |

### Costs

| Item | Typical |
|---|---|
| **Notary fee** (sliding 0.5–1.0 % of contract value) | ~0.5 % residential resale typical |
| **Stamp duty / state duty** | 0.1–0.5 % of contract value (sliding) |
| **SCSI recordation fee** | ~AZN 50–100 (~US$30–60) |
| **Translator (if required)** | ~AZN 100–300 |
| **Lawyer (optional but recommended for foreign buyer)** | AZN 500–2,500 typically |
| **Total transaction cost (buyer side, residential)** | **~1–2 % of price** |

### Notary selection

- Ministry of Justice notary register: `https://justice.gov.az/` — notaries by district (rayon)
- **Buyer should engage independent notary** (not seller's) — common practice but not statutorily required

### Foreign buyer practical

- **Non-Azerbaijani speaker**: certified translator must be present at deed signing OR full bilingual deed + sworn translation
- **Power of Attorney**: foreign buyer can authorise AZ-based representative via apostilled PoA (from country of residence) — common workaround if buyer not present in AZ on signing day; AZ joined Hague Apostille Convention 2004
- **AML / source-of-funds**: notary required to obtain bank statements + source-of-funds under Law 767-IIIQ/2009; PEP screening mandatory; FMS (Financial Monitoring Service) supervision
- **FİN-code (tax ID)** mandatory before any cadastral registration — issued same-day at any tax office or ASAN Service with passport
- **1-month registration deadline**: foreign buyer must complete SCSI recordation within 1 month of notarised deed — late registration triggers penalty + procedural complication

---

## Section: `--compare`

### Azerbaijan vs regional neighbours (residential investment lens, Q1–Q2 2026)

| Country | Foreign-buyer rule | Acquisition cost (typical) | Annual recurring | Yield (2024) | Currency |
|---|---|---:|---:|---:|---|
| **🇦🇿 Azerbaijan** | Open (residential); ag/border banned for foreign individuals | 1–2 % | AZN 0.1–0.4/m² + 0.6 % above 120 m² | ~5–8 % Baku | AZN de-facto USD peg |
| **🇬🇪 Georgia** | Open (residential); ag banned post-2017 | 0.1–0.5 % | 0–1 % × market (income-threshold) | ~6–10 % Tbilisi | GEL managed-float |
| **🇦🇲 Armenia** | Open (residential); ag restricted | ~1–2 % | 0.05–1 % cadastral | ~6–9 % Yerevan | AMD managed-float |
| **🇹🇷 Türkiye** | Open + CBI at $400k | ~5–8 % | 0.1–0.6 % rayiç bedel | 5–8 % İstanbul (FX-distorted by hyperinflation) | TRY hyperinflation |
| **🇮🇷 Iran** | Highly restricted for foreigners | n/a | n/a | n/a | sanctions context |

### Azerbaijan's distinctive position

- **Lowest property-acquisition tax in the immediate region** (1–2 % vs Türkiye 5–8 %)
- **Currency stability under de-facto USD peg** since 2017 — among the most stable regional currencies for USD-denominated buyers (vs GEL/AMD floats and TRY hyperinflation)
- **AZN 100,000 real-estate-linked TRP** comparable to Georgia US$150k (US$100k before 1 Mar 2026); lowest in Caucasus + Caspian region
- **Oil + gas economy** provides macro buffer (SOFAZ ~US$60bn) but creates concentrated commodity-price tail risk
- **Karabakh + East Zangezur reintegration zones** (2024–2030 reconstruction) create subsidised investment opportunities for qualified investors
- **No CBI** unlike Türkiye + Caribbean peers — naturalisation requires actual residence + language + dual-citizenship renunciation
- **Restricted dual citizenship + ag/border bans** narrow long-term-resident foreign buyers

### Comparative reference

For neighbour-context see `countries/ge/playbook.md` (Georgia — closest regional peer with similar permissive residential foreign-buyer regime). For cultural/economic peer see `countries/tr/playbook.md` (Türkiye — Oghuz language family + Caspian/Mediterranean trade overlap). For CIS managed-currency context see `countries/md/playbook.md` (Moldova).

---

## Section: `--retirement`

### Retirement to Azerbaijan scenario

AZ is a **niche** retirement destination — primarily for diaspora-return + Russian/CIS retirees seeking Caspian climate at sub-EU cost + Türkiye-cycle retirees. Not a Lisbon/Valencia/Mexico-tier mature retirement market.

### Cost-of-living for retirees (Baku 2-bed apartment, conservative profile)

- Median 2-bed apt rental Q1 2026: ~AZN 600–1,200/month outside prime; AZN 1,500–3,500 prime Sahil/Yasamal
- Public healthcare via **State Agency on Mandatory Medical Insurance (TƏBİB)**: phased rollout under Compulsory Medical Insurance Law 2007 + accelerated 2020+ — universal coverage transitioning; verify current contribution + entitlement scope
- Private health insurance for 65+: ~AZN 1,500–4,500/yr typical
- Public transport Baku: AZN 0.40/ride (BakıKart); senior concession; metro AZN 0.40
- Utilities (2-bed apt): ~AZN 80–200/month winter peak; ~AZN 40–80 summer (subsidised tariffs)

### Tax position for retirees

- **Foreign-source pension income**: typically taxed at **14 % flat PIT** if AZ-resident (Tax Code Art. 101); double-tax treaties (with Türkiye, Russia, Germany, Italy, France, UK, Netherlands, Switzerland, China, Japan, S. Korea — verify per source country) may credit/exempt
- **Individual-seller property gains** are settled via a notary-withheld per-m² simplified property-transfer tax, **not** a CGT-on-gain. The previously claimed 3-yr primary-residence exemption under Art. 102.1.18 is **NOT corroborated — data not publicly verified** (treat as fabricated pending direct Tax Code check; see `--tax`) — verify at taxes.gov.az
- **No wealth tax**; **no inheritance tax** (Tax Code does not levy estate/inheritance tax — verify intra-family donation treatment)

### Healthcare access

- **TƏBİB** public system: hospitals + primary-care under universal-coverage transition; quality variable; tertiary in Baku (Mərkəzi Klinika, Bona Dea, Modern Hospital)
- **Major private**: Bona Dea International Hospital, Liv Bona Dea, Memorial Hospital Baku, Baku Medical Plaza, Central Hospital Baku — all in Baku CBD
- ⚠️ Specialist + advanced-oncology often referred to Türkiye (İstanbul, Ankara) or Israel under bilateral agreements; verify under-treaty access

### Verdict for retirement-first buyers

🟡 **Watch** — viable for diaspora returnees + CIS retirees + budget-conscious Türkiye-circuit retirees willing to bridge to Türkiye/Israel for tertiary healthcare; questionable for retirees prioritising mature healthcare market or large expat community (smaller than Türkiye/Georgia foreign-resident pools). Best fit: Russian/CIS + Türk-speaking retirees + Caspian-coast attached + remote-working semi-retirees with private health insurance.

---

## Section: `--digital-nomad`

### Visa pathway

- **No formal "digital nomad visa"** as of 2026 (compared to PT-D8 / ES-DNV / EE-DNV / GE remote-work)
- Practical pathways:
  1. **Visa-free 30 days** (Türkiye/CIS/Israel/GCC) or **e-visa 30 days extendable** for Western passports — covers short-term remote stays
  2. **Real-estate-linked TRP at AZN 100,000 (~US$60k) → 1-yr renewable** — among the lowest barriers in the region
  3. **High Technology Park (YTP) status** for IT professionals registering substance — corporate-tax incentives (verify current at ytp.az)
  4. **Employer-sponsored work residence** — only if AZ-employer-tied
  5. **Investor TRP at AZN 540,000 (~US$320k)** — for high-net-worth nomads

### Connectivity

- **Internet**: AZ ranks moderately on global broadband (Speedtest Global Index — verify current); Aztelekom + Bakcell + Azerfon + Azercell offer up to 1-Gbps fibre at AZN 30–50/month residential in Baku
- **Mobile**: Azercell + Bakcell + Nar — 5G launched 2024 in Baku; ~AZN 15–25/month for 30+ GB
- **Co-working Baku**: Pasha Holding's Crown Plaza, Zive Coworking, Bric Center, Park Bulvar Mall co-work spaces; AZN 200–500/month hot desk
- **Time zone**: UTC+4 (no DST since 2016) — favours EU + Middle East asynchronous work; 9-hr gap to US Pacific; 4-hr gap to Singapore

### Cost-of-living for remote worker (Q1 2026)

- Studio short-let Baku Centre: AZN 800–1,800/month
- 1-bed apt long-term: AZN 600–1,200/month outside prime
- Single-meal mid-range: AZN 12–30
- Monthly transport: AZN 30–60

### Tax position

- **PIT progressive**: 14 % up to AZN 2,500/month, then AZN 350 + 25 % above (Tax Code Art. 101; see `--tax`) if AZ tax resident (183+ days)
- **Simplified Tax 2 %** on turnover for sole proprietors with qualifying activity
- **YTP residents**: significant CIT/VAT incentives if eligibility met
- Foreign-employer remote work: technically subject to AZ PIT once tax-resident; double-tax treaty network covers most Western source countries

### Verdict for digital-nomad-first buyers

🟡 **Selective fit** — AZ offers low CoL + AZN/USD peg-stability + low-threshold TRP at AZN 100k property purchase + COP29 host-city profile + emerging tech ecosystem. **Friction**: no formal DN visa programme; thin English-speaking infrastructure outside Baku CBD; Azerbaijani+Russian dominate over English; oil-dependence macro tail risk. **Best fit**: Russian-speaking DNs (cyrillic/CIS adjacency), Türk-speaking DNs (Oghuz mutual intelligibility), IT-sector DNs targeting YTP incentive, Caspian/Caucasus-cycle nomads.

---

## Section: `--macro`

### Headline 2024–2026

- **GDP growth 2022**: +4.6 % (oil + gas price tailwind)
- **GDP growth 2023**: +1.4 %
- **GDP growth 2024**: +4.1 % (SSC preliminary; non-oil +6.3 % vs oil −2.4 %)
- **GDP growth 2025**: +3.0–3.5 % IMF Article IV / EBRD forecast range
- **GDP per capita 2024**: ~US$7,800 (World Bank)
- **Inflation 2025**: ~3.0–4.5 % headline (CBAR target ~4 %)
- **Unemployment 2024 Q4**: ~5.5 % (SSC) — masked by high informal-economy participation
- **Public debt / GDP**: ~18 % (Ministry of Finance) — low by regional standard, oil-revenue-buffered
- **CBAR refinancing rate Q1 2026**: 7.25 % (verify current at cbar.az)
- **SOFAZ assets (Q1 2026)**: ~US$60bn

### Trend drivers (2024–2030)

- **Oil + gas economy**: ~40 % of GDP; ~85 % of export earnings; SOCAR + BP-led BTC pipeline + TANAP + TAP gas-export to EU
- **Non-oil diversification**: tech (YTP), tourism, agro-export — growing but slow
- **Karabakh + East Zangezur reconstruction**: ~AZN 30bn (~US$18bn) committed 2024–2030; major infrastructure + housing pipeline
- **COP29 (Baku, Nov 2024)**: signalled climate-finance + green-investment positioning; LT-LEDS 2050 net-zero
- **Middle Corridor / Trans-Caspian transit**: post-2022 EU-Asia logistics shift increases AZ corridor volume → port + rail + road infrastructure tailwind
- **CBAR + SOFAZ buffer**: combined FX reserves ~US$75bn — robust cyclical defence

### IMF Article IV (latest)

[IMF 2024 Article IV](https://www.imf.org/en/Countries/AZE) flags: oil-revenue concentration, demographic ageing, non-oil productivity, banking-sector consolidation. Property-market: subdued 2015–2017 trough post-devaluation; Baku recovery 2018+; structural pricing supported by AZN/USD peg and oil-revenue-funded mortgage subsidies.

---

## Section: `--demographics`

### Population structure (2024 SSC estimate)

- **Total**: ~10.16 million (vs ~7.0M in 1989 census — +45 % growth)
- **Median age 2024**: ~33.6 years (rising)
- **Age 0–14**: ~22 %
- **Age 15–64**: ~70 %
- **Age 65+**: ~8 % (rising — projected ~14 % by 2050 per SSC projections)
- **Total fertility rate 2024**: ~1.7 (SSC; below replacement; declining)
- **Net migration**: modestly negative since 1991; ~–5k to –20k/yr typical (recent return migration from Russia partly offsets historical CIS outflow)
- **Diaspora**: ~3M Azerbaijanis living abroad (Russia, Türkiye, Iran, Germany, US, Ukraine) — material remittance + return-migration base

### Geographic distribution

- Baku municipality (Greater Baku): ~2.4M (24 % of population)
- Sumqayit municipality: ~340k (3.3 %)
- Ganja municipality: ~330k (3.2 %)
- Other urban: ~3.0M (30 %)
- Rural: ~4.1M (40 %)
- Naxçıvan AR: ~460k (exclave)

### Households

- ~2.7M domestic households (2024 SSC)
- Average household size: 3.7 persons (declining; among highest in Caucasus)
- Owner-occupier rate: **~85–90 %** (legacy of post-Soviet apartment privatisation)
- Renter market thin outside Baku; growing in Baku CBD post-2017 tourism uplift

### Implication for property

- **Demand floor 2025–2030**: rising-population + young-age structure → structural housing demand (vs declining-population peers Moldova, Bulgaria); Baku continues capital-city pull
- **Karabakh + East Zangezur returns**: ~700k IDPs/displaced from 1990s + early 2020s — reintegration over 2024–2035 creates structural housing demand in reintegrated zones
- **Discount opportunity**: regional cities (Sumqayit, Ganja, Mingachevir) priced at material discount to Baku; rural village houses (kənd evi) widely available <AZN 30k but with severe utility + amenity constraints + isolation

---

## Section: `--esg`

### Climate-transition exposure

- **Climate Resilience Strategy 2024** (Cabinet Decision; verify current at eco.gov.az)
- **NDC under Paris Agreement**: 35 % GHG reduction by 2030 vs 1990 base
- **LT-LEDS 2050 net-zero ambition** announced **COP29 Baku (Nov 2024)** — major signalling moment for AZ as host
- **Renewables target 30 % installed capacity by 2030** (Strategy 2030); large solar + wind tenders Absheron + Caspian offshore (Masdar, ACWA, BP — multi-GW pipeline)
- **Buildings sector**: ~25 % of national CO₂; primary lever is heating-fuel switch + insulation retrofit + cooling-load efficiency

### Property-level ESG considerations

- **Pre-1990 panel stock**: typically poor thermal envelope; major retrofit opportunity (insulation, window replacement, individual gas boiler) — AZN 50–150/m² typical retrofit budget for thermal-envelope upgrade
- **Subsidised gas + electricity tariffs**: dampens economic case for energy-efficiency investment but tariff adjustment risk over 2026–2030
- **Karabakh + East Zangezur "Green Energy Zone"**: pilot for net-zero new-build standards in reintegrated zones — high-spec construction floor; verify per development

### Climate-physical risk (cross-section to `--climate` + `--risks`)

- Drought stress in Aran (south-east) viticulture + cotton belt
- Greater Caucasus seismic + flood exposure for northern + western rayons
- Caspian sea-level uncertainty for outer-Absheron coastal property
- Hotter Baku summers → cooling-load growth in stock built without modern AC provision
- Mud-volcano hazard zones (Absheron Peninsula) require setback compliance

### Social / governance factors

- HOA governance (`mənzil mülkiyyətçilərinin alyansı` / MTK) under Housing Code 2009; minority-protection mechanisms via court; HOA collective-action problem material in panel stock
- Anti-corruption: AZ has tightened SCSI cadastre + notary supervision via e-gov.az single sign-on; ASAN Service one-stop model is regional best-practice for citizen interface; ranking improving on Transparency International CPI but baseline modest
- COP29 host year (2024) elevated AZ ESG profile internationally; reporting/disclosure pressure rising on listed entities + larger developers

### Verdict (ESG lens for typical Baku apt)

🟡 **Watch** — pre-1990 panel stock represents the dominant retrofit-debt exposure; new-build (post-2014) materially better but priced higher; subsidised utility tariffs distort investment economics; tariff adjustment risk + COP29-signalled green-finance pressure tightens 2026–2030. Karabakh reintegration zones leapfrog as "green pilots."

---

## Section: `--exit`

### Resale market liquidity

- **Average days on market 2024**: ~45–120 days Baku mid-tier; 90–240 days Sumqayit/Ganja/regional centres; rural village houses can sit 1–3+ years
- **Cyclical sensitivity**: AZ secondary market is **moderately liquid in Baku, thin elsewhere** — annual transactions nationally ~80–110k (SSC) vs ~3.5M registered immovables; turnover ratio ~2.5–3 %/yr
- **2015–2016 trough**: dual devaluation depressed transactions ~35–40 % YoY; recovered to pre-shock levels by 2018; 2020 COVID + 2020 Karabakh war minor secondary impact

### Exit-cost stack (seller side)

| Item | Cost |
|---|---|
| Estate agent commission | typically **2–4 %** of sale price (often paid by seller; sometimes split) |
| Notary fee (seller side typically partial) | 0.5–1.0 % of contract value (sliding) |
| **Notary-withheld simplified property-transfer tax** (per-m² × statutory coefficient under Art. 220-series; 2026-05-27 verified, source Caspian Legal Center) — replaces a CGT-on-gain; proceeds excluded from seller annual income |
| **Non-resident gross-value WHT (~10 %)** widely cited but article anchor needs re-verification — data not publicly verified — verify at taxes.gov.az |
| Mortgage early-discharge fee | typically 1–2 % of outstanding balance, capped per loan agreement |
| Total exit cost | **typically 3–6 % of sale price** for resident individual residential sale (notary tax + agent + notary fee); higher for non-resident or commercial/legal-entity sales |

### Liquidity by sub-segment (qualitative, 2026)

| Segment | Liquidity | Notes |
|---|---|---|
| Baku Sahil/Yasamal/Nəsimi prime CBD | 🟢 strong | Diaspora-return + business + diplomatic pool; 30–90 days typical |
| Baku Nərimanov/Xətai middle | 🟢 strong | Largest stock, perpetual buyer pool; 45–120 days typical |
| Baku Sabunçu/Suraxani/Bilgəh outer | 🟡 selective | Commute-quality dependent; 90–240 days |
| Baku İçəri Şəhər heritage | 🟠 thin | Renovation restrictions + small buyer pool |
| Sumqayit + Ganja + Mingachevir mid-tier | 🟡 selective | Population stable; 90–240 days |
| Quba / Qəbələ resort | 🟡 selective | Seasonal + thin foreign-resident pool |
| Karabakh + East Zangezur reintegrated | 🔴 thin (special regime) | New regime; subsidised but reconstruction-phase liquidity uncertain; AZ-citizen-priority |
| Rural village houses | 🟠 niche | Diaspora-buy / hobby-property only; 1–3+ yr typical |

### Verdict for exit risk

🟢 for Baku CBD + middle-tier; 🟡 for outer Baku + Sumqayit + regional centres; 🟠 for rural + heritage + reintegrated zones (special regime). **Pre-2015 buyers**: 2015–16 devaluation trough has materially recovered; full recovery elsewhere achieved by 2018–2019. **AZN/USD peg stability** is the key valuation anchor; reverses materially if peg revalues following sustained oil shock.

---

## Cost benchmarks (AZ 2025–2026)

| Item | Cost (AZN, est.) |
|---|---:|
| SCSI extract (standard) | ~AZN 5–20 (~US$3–12) |
| SCSI extract (urgent) | ~AZN 30–60 (~US$18–35) |
| Notary fee (residential resale, 0.5–1.0 %) | ~AZN 500–2,000 on AZN 200k flat |
| Stamp duty / state duty | 0.1–0.5 % of value |
| Real-estate agent (paid by seller normally) | 2–4 % |
| Translator (deed signing, foreign buyer) | AZN 100–300 |
| Building inspector (independent structural survey) | AZN 300–800 |
| Asbestos test (single sample) | AZN 80–200 |
| Radon test (3-month kit) | AZN 80–250 |
| Bare-shell ("təmirsiz") → finished apartment fit-out | AZN 350–700 / m² |
| Roof replacement (terracotta, 200 m²) | AZN 8,000–20,000 |
| Full apartment renovation (Baku mid-range, 80 m²) | AZN 18,000–45,000 |
| Septic to mains connection | AZN 1,500–6,000 |
| Annual property tax (Baku 100 m² flat) | ~AZN 28 (m²-based after 30 m² exempt floor) |
| Annual property tax (Baku 200 m² Sahil flat, AZN 800k cadastral) | ~AZN 1,956 (m² + 0.6 % above 120 m² band) |
| **Total transaction cost (buyer side, residential resale)** | **~1–2 % of price** |

## Active fiscal incentives (2025–2026)

- **0 % VAT on first sale of residential by licensed developer** (Tax Code Art. 164.1.5)
- **Simplified Tax 2 %** on turnover for individual entrepreneurs in qualifying activities (Tax Code Art. 218–222)
- **Non-oil private-sector employee PIT** — 0 % up to AZN 8,000/month under the 7-year scheme through 2025; **transitions to graduated 3 % / 10 % / 14 % bands from 1 Jan 2026** (2026-05-27 verified, sources APA + Caspian Legal Center 2026 amendments)
- **Residential rental income paid to individuals**: 14 % (2024–2025) → **10 % from 1 Jan 2026** (2026-05-27 verified, source APA 2026-budget-package reporting)
- **Individual seller property transfer**: notary-withheld per-m²-based simplified tax under Art. 220-series (no separate CGT on net gain; the previously claimed "3-year primary-residence exemption under Art. 102.1.18" is unverified — data not publicly verified — verify at taxes.gov.az)
- **AMF state-subsidised mortgage** at 5–9 % rates for AZ-citizen first-time buyers (`https://mcgf.gov.az/`)
- **Karabakh + East Zangezur reconstruction zones**: special tax incentives + subsidised mortgages for displaced returnees + qualifying investors (Presidential Decree on State Programme for Restoration)
- **High Technology Park (YTP)**: significant CIT/VAT incentives for resident IT firms
- **Real-estate-linked TRP at AZN 100,000** purchase threshold → 1-yr renewable

## Common listing platforms

- **Bina.az** (largest real-estate portal): `https://bina.az/` *(per listing — verify with cadastre / on visit)*
- **Tap.az**: `https://tap.az/elanlar/dasinmaz-emlak` *(per listing — verify with cadastre / on visit)*
- **Lalafo.az**: `https://lalafo.az/azerbaijan/nedvizhimost` *(per listing — verify with cadastre / on visit)*
- **EvDe.az**, **Yeniemlak.az**, **Birja.az** smaller portals *(per listing — verify with cadastre / on visit)*
- **Facebook + Telegram channels** (`t.me/baki_emlak`, `t.me/bakuhomes`) — high volume; never authoritative
- Developer-direct portals: Pasha Construction, Akkord, Baku White City, Crescent Bay, Port Baku Towers

## Caveats unique to AZ

- **Foreigners CAN own buildings, apartments, and individual house structures as full freehold** (Constitution Art. 13 + Civil Code Art. 152; 2026-05-27 verified, sources AZ MFA New Delhi + Land Code Art. 48.3 / 49). For apartments this is operationally identical to citizen ownership (land is collective/state). For **standalone houses** the structure is owned freehold but the **plot underneath must be held under a long lease (up to 99 years)** — foreigners cannot own land of any class
- **Foreigners CANNOT own LAND of any class — agricultural, forest, urban, residential plot** (Land Code Art. 48.3 lease-only + Art. 49 ownership ban for ag/forest/border); ag + border + strategic = banned outright
- **1-month registration deadline** for foreign buyers post-deed at SCSI — late registration triggers penalty + procedural complication
- **AZN/USD de-facto peg at 1.70** since 2017 — among the most stable regional currencies for USD buyers; tail risk on sustained oil shock
- **Soviet-era panel stock** (1955–1991): asbestos + uneven seismic retrofit; pre-1990 dominant in Baku/Sumqayit/Ganja resale; commission independent structural survey
- **Mud volcanoes** (Absheron Peninsula) — verify zoning for outer-Baku properties (Lokbatan, Şıxov, Otman Bozdag)
- **Notarised contract MANDATORY** (Civil Code Art. 152) — no DIY conveyancing
- **Dual citizenship NOT generally permitted** (Constitution Art. 53) — naturalisation requires renunciation; affects long-term-resident foreign buyers
- **AZ joined Hague Apostille Convention 2004** — simplifies foreign-document acceptance for foreign buyers
- **No CBI** (golden citizenship by investment) — only residence-based naturalisation
- **AML cash limit AZN 10,000** practical bank-channel threshold (Law 767-IIIQ/2009); FMS supervision
- **Karabakh + East Zangezur reintegrated zones** (post-2020 + post-2023): UXO/de-mining ongoing; ANAMA clearance certificate mandatory; AZ State Register only (former de-facto authority documents not recognised)
- **2015–16 dual devaluation legacy**: AZN-denominated mortgages on pre-2015 properties may have residual collateral-chain complexity from IBA recapitalisation + bank licence revocations — verify carefully
- **COP29 Baku (Nov 2024) host year** signalled climate-finance + green-investment positioning; LT-LEDS 2050 net-zero ambition
- **Subsidised gas + electricity tariffs**: dampen energy-efficiency investment economics; tariff-adjustment risk over 2026–2030
- **Iran border tensions** (Nakhchivan + southern AZ): periodic; baseline risk modest; verify per locality near border

## Reddit / forum sources

- **r/azerbaijan** — general (mixed quality on property; English + Azerbaijani + Russian)
- **r/baku** — city-specific
- **r/AzerbaijaniLearners** — language learners; useful for Latin-script + Cyrillic-legacy questions
- Facebook: "Expats in Baku", "Baku Apartments for Rent", "Foreigners in Azerbaijan"
- Telegram: `t.me/baki_emlak`, `t.me/bakuhomes` (high volume; classifieds; never authoritative)
- Diaspora forums (Russia, Türkiye, Germany, US): material because diaspora-return is non-trivial buyer segment
- Bina.az + Tap.az analytics → local market commentary

## Verification authorities

| Authority | When to call / visit |
|---|---|
| **SCSI (State Service on Property Issues — emdk.gov.az)** | Title extract, encumbrances, cadastral verification — any ASAN Service centre or SCSI office |
| **e-emlak.gov.az / e-gov.az** | Online cadastral self-service (e-extract) |
| **ASAN Service** | One-stop government services hub (cadastre, civil registry, FİN-code, residence) |
| **State Tax Service (Vergilər Nazirliyi — taxes.gov.az)** | Tax residency, FİN-code, Simplified Tax registration, VAT registration |
| **State Migration Service (migration.gov.az)** | TRP, work permit, investor visa, real-estate-linked residence |
| **CBAR (Central Bank — cbar.az)** | Reference exchange rate, bank supervisory list, mortgage prudential |
| **AMF (Mortgage and Credit Guarantee Fund — amcgf.gov.az)** | Subsidised mortgage programme |
| **Notarial Chamber + Ministry of Justice (justice.gov.az)** | Notary register, complaints, tariff |
| **Ministry of Culture (mct.gov.az)** | Heritage-listed building check (İçəri Şəhər + Sahil + Old Baku) |
| **Local rayon municipality (icra hakimiyyəti)** | Local zoning, building permits, MTK/HOA registration |
| **Azərsu (azersu.az)** | Mains water + sewer connection verification |
| **Azərişıq (azerishiq.az), Azəriqaz (azeriqaz.az)** | Electricity + gas connection + tariff |
| **MENR (eco.gov.az) — Ministry of Ecology & Natural Resources** | Geo-hazard, mud-volcano + landslide zoning, EIA, climate strategy |
| **RSSC (rssc.az) — Republic Seismological Survey Center** | Seismic hazard data |
| **FHN (fhn.gov.az) — Ministry of Emergency Situations** | Emergency response, hazard maps |
| **ANAMA (anama.gov.az)** — Mine Action Agency | Karabakh + East Zangezur de-mining clearance certificates |
| **FMS (fms.gov.az)** — Financial Monitoring Service | AML if anomaly suspected in cadastre/notary chain |
| **Tariff Council (tariffcouncil.gov.az)** | Utility tariff verification |
| **State Tourism Agency (tourism.gov.az)** | STR classification certificate |
| **SOFAZ (oilfund.az)** | Oil-revenue stabilisation context |
| **State Customs (customs.gov.az)** | FX-cash declaration > USD 10,000 |

## Quirks to know

- **Cadastral number format `XX-XXX-XX-XXXX-XXX`** (region.district.block.parcel.unit) — every property has one; ask for it before any other paperwork
- **Latin-script Azerbaijani since 2001**: older deeds + technical passports may be in Cyrillic Azerbaijani; certified transliteration cheap and standard
- **Russian + Azerbaijani bilingual context**: Russian still widely used in business + older notaries; verify deed language preference
- **"Qonaq evi" (guest house) / "günlük kirayə" (daily rental)** are the regulated STR categories — Decree 1146 + Tourism Law
- **Baku panel-block series identification**: 1-464, 1-468, 105 series (5-storey Khrushchovkas); 9- + 16-storey Brezhnev panels — informs structural-survey scope + seismic retrofit history
- **VAT trap on new-build**: confirm "ƏDV daxil" (VAT included) — first-sale residential by licensed developer is **0 % VAT** but resale by intermediary may flip to 18 % VAT scope; verify
- **Mud-volcano zoning (Absheron)**: outer-Baku peripheral developments occasionally encroach on dormant cones — verify on-site + check geo-zone designation with MENR Geological Service
- **ASAN Service one-stop model**: cadastral, civil registry, FİN-code, residence permit all available same-day at one window — regional best-practice
- **e-gov.az single sign-on**: with FİN-code + ASAN signature, foreign residents can access most cadastral + tax services online
- **FİN-code (tax ID)** mandatory for any property purchase + utility account + bank account — issued same-day at any tax office or ASAN Service with passport
- **Diaspora-buy pattern**: many pre-1990 panel apartments held by emigrant owners (Russia, Türkiye, Germany, US, Israel) and managed by local relatives — verify owner is signing personally OR via apostilled PoA
- **Karabakh + East Zangezur cadastral codes**: post-2020/2023 reintegration; AZ State Register issuing new SCSI codes; former de-facto authority documents not recognised; ANAMA certificate mandatory before transfer
- **"Bağ evi" (dacha)**: traditional Caspian/Absheron summer-house segment; cheap (often <AZN 30k) but typically off-grid — water/sewer/mains absent; verify
- **2015–2016 devaluation discount**: certain pre-2015 mortgage-collateral properties in IBA-resolution chain may have residual title-chain complexity — verify carefully via SCSI

## Source URL templates

| Source | URL pattern |
|---|---|
| SCSI cadastre / property issues | `https://emlak.gov.az/` |
| SCSI e-extract self-service | `https://e-services.economy.gov.az/` |
| e-Gov single sign-on | `https://www.e-gov.az/` |
| ASAN Service one-stop | `https://asan.gov.az/` |
| State Tax Service | `https://www.taxes.gov.az/` |
| State Migration Service | `https://migration.gov.az/` |
| CBAR Central Bank | `https://www.cbar.az/` |
| CBAR exchange rates | `https://www.cbar.az/currency` |
| State Statistical Committee | `https://www.stat.gov.az/` |
| Ministry of Justice (notary register) | `https://justice.gov.az/` |
| Tariff Council | `https://www.tariffcouncil.gov.az/` |
| AMF Mortgage Fund | `https://mcgf.gov.az/` |
| MENR Ministry of Ecology | `https://eco.gov.az/` |
| RSSC Seismology | `https://seismology.az/en` |
| FHN Emergency Situations | `https://fhn.gov.az/` |
| ANAMA Mine Action | `https://anama.gov.az/` |
| Ministry of Culture | `https://mct.gov.az/` |
| Tourism Agency | `https://tourism.gov.az/` |
| Azərsu (water + sewer) | `https://www.azersu.az/` |
| Azərişıq (electricity) | `https://www.azerishiq.az/` |
| Azəriqaz (gas) | `https://www.azeriqaz.az/` |
| SOCAR | `https://www.socar.az/` |
| SOFAZ State Oil Fund | `https://www.oilfund.az/` |
| Bina.az classifieds | `https://bina.az/` |
| Tap.az classifieds | `https://tap.az/elanlar/dasinmaz-emlak` |
| Lalafo.az classifieds | `https://lalafo.az/azerbaijan/nedvizhimost` |
| State Highway Agency | `https://aayda.gov.az/` |
| AYNA — Azərbaycan Yerüstü Nəqliyyat Agentliyi (ex-BNA) | `https://ayna.gov.az/` |
| Baku Metropoliten | `https://metro.gov.az/` |
| ASAN Visa (e-visa) | `https://evisa.gov.az/` |
| YTP High Technology Park | `https://ytp.az/` |
| FMS Financial Monitoring | `https://fiu.gov.az/` |
| Insurers' Association | `https://asa.az/` |

## Status

**Confidence**: MEDIUM — HIGH on foundational legal/fiscal framework (Land Code Art. 48.3 + 49 — foreigners may freehold-own buildings / apartments / individual house structures but cannot own LAND of any class; standalone-house plots held under up-to-99-yr lease; property-tax AZN-per-m² mechanic with Baku district coefficient AZN 0.4/m² base × 0.7–1.5 → effective AZN 0.28–0.60/m²; PIT progressive 14% up to AZN 2,500/month, AZN 350 + 25% above per Tax Code Art. 101; rental 14% → 10% from 1 Jan 2026 residential rentals paid to individuals; AZN-USD peg ~1.7 since 2017). MEDIUM on simplified property-transfer-tax exact notary-withheld coefficient (verify at notary per deal); the "3-yr primary-residence exemption under Art. 102.1.18" framing remains unverified vs PwC + taxes.gov.az and is currently tagged `data not publicly verified — verify at taxes.gov.az`. MEDIUM on parcel-level rayon coefficient assignment within Baku (verify at relevant Bələdiyyə). LOW on residential price benchmarks (no national HPI; Bina.az / Tap.az aggregator-grade).

**Last verified**: 2026-05-27 (traffic, AML and innovation authority identities corrected 2026-09-18 per ayna.gov.az + fiu.gov.az + idda.az). Cross-references corrected 2026-09-24 from the GE-537 tracker entry (November regwatch wave, run early).

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Primary sources verified — SCSI cadastre + Land Code Art. 47–48 (foreign ag/border ban), Civil Code Art. 152 (mandatory notary), Tax Code Art. 101 (14 % flat PIT), Art. 102 (CGT — 3-yr primary-residence exemption claim UNVERIFIED, see `--tax`), Art. 164.1.5 (0 % VAT first-sale residential), Art. 173 (18 % standard VAT), Art. 196–202 (m²-based property tax with 30 m² exempt floor + AZN 0.4/m² Baku band + 0.6 % above 120 m²), Art. 218–222 (Simplified Tax 2 % turnover), Constitution Art. 13 + 53 (foreign rights + dual-citizenship restriction), CBAR de-facto USD peg at 1.70 since 2017, AMF subsidised mortgage 5–9 %, real-estate-linked TRP at AZN 100,000, Cabinet Decree 1146/2017 (STR classification), Law 767-IIIQ/2009 (AML), Law 270-IIIQ/2004 (Real Estate State Register), AzDTN 2.4-1 seismic code 2010, Hague Apostille (AZ joined 2004). **Karabakh + East Zangezur reintegrated zones explicitly OUT-OF-SCOPE for ordinary foreign-buyer DD as of 2026**: ANAMA de-mining ongoing, special tax/residence regime, AZ-citizen-priority subsidies, former de-facto authority documents not recognised — flagged in Caveats and Visa/Risks sections. **No CBI exists** (verify against ENDED registry — never had one). **Re-verify each annual budget law (December)** for Tax Code amendments, Tariff Council utility-rate adjustments, CBAR refinancing rate, AMF mortgage programme caps. **Watch list 2026**: non-oil PIT 0 % up to AZN 8k/month 7-year incentive sunset (originally 2026), AZN/USD peg under sustained oil-price stress, Karabakh reconstruction-zone foreign-investor rules evolution, COP29-signalled green-investment incentive rollout, Western Zangezur Corridor outcome, Iran border tensions, EU Eastern Partnership AML harmonisation milestones.

## Extension TODOs (deepen on first real run)

- [ ] Per-Baku-rayon m²-based property-tax calibration (verify rates per rayon municipal collection)
- [ ] SCSI cadastral-value vs market-value calibration database (fraction varies by build era + district)
- [ ] AMF subsidised-mortgage programme eligibility tree (citizen-only filter, income caps, property caps)
- [ ] Karabakh + East Zangezur reconstruction zone foreign-investor pathway documentation (evolving 2024–2030)
- [ ] Mud-volcano zone parcel-flag automation (Absheron geological registry integration)
- [ ] STR classification certificate process walkthrough (Decree 1146 implementation)
- [ ] Heritage-listed building cadastral-code lookup workflow (Ministry of Culture register)
- [ ] YTP residence + tax-incentive eligibility checklist (IT activity definitions)
- [ ] Border-zone + strategic-area restricted-list (Cabinet Decree on Border Regime — periodic updates)
- [ ] Diaspora-buyer due diligence checklist (apostilled PoA + remote-signing workflow Türkiye/Russia/Germany pathways)
- [ ] Dual-citizenship Presidential-discretion exception case-law tracking
- [ ] CBAR + SOFAZ FX-buffer time-series automation for peg-stress monitoring
