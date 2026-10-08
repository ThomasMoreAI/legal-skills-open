# Moldova (MD) — Property Due-Diligence Playbook

ISO2: `md`. Status: ✅ Fully populated (researched 2026-04 / 2026-05).

## Country profile

- **Population**: ~2.5 million (2024 BNS estimate, **excluding Transnistria**); Chișinău (capital) ~660k, Bălți ~150k, Tiraspol ~125k (Transnistria — out of cadastral scope, see §Country-specific quirks)
- **GDP per capita**: ~US$6,650 (2024 World Bank / BNS); real GDP −0.7% 2022 (war shock), +0.7% 2023, +2.5% 2024 (BNS preliminary)
- **Currency**: **MDL** (Moldovan leu). 1 EUR ≈ 19.2–19.7 MDL, 1 USD ≈ 17.6–18.1 MDL (Q1 2026 BNM reference; managed-float — see `--currency`)
- **Languages**: **Romanian** (official; Constitutional Court Decision No. 36 of 5 Dec 2013 confirmed `Romanian` as state language per the Declaration of Independence over the older constitutional `Moldovan` formulation); Russian widely used in business + Chișinău/Bălți; **Gagauz** co-official in UTA Găgăuzia; **Ukrainian** in northern districts
- **EU status**: **Candidate country since 23 June 2022** (European Council); **accession negotiations formally opened 25 June 2024** ([Council conclusions](https://www.consilium.europa.eu/en/press/press-releases/2024/06/25/intergovernmental-conferences-with-the-republic-of-moldova-and-ukraine-the-european-union-opens-accession-negotiations/)); **Constitutional reform Oct 2024** referendum + parliament enshrined EU-integration objective in Constitution Art. 140¹
- **Postcode**: 4 digits, optional `MD-` prefix (e.g., Chișinău centre `MD-2001`–`MD-2075`; Bălți `MD-3100`–`MD-3128`)
- **Admin levels**: 32 raioane (districts) + 3 municipalities (Chișinău, Bălți, Bender) + 1 autonomous territorial unit (UTA Găgăuzia) + Stânga Nistrului (Transnistria — disputed; **Moldovan ASP cadastre does NOT issue valid extracts here**)
- **Cadastre**: **Agenția Servicii Publice (ASP)** — `cadastru.md` is the unified registry of immovable property + cadastral plans (since 2012 ASP merger consolidated former Cadastrul Bunurilor Imobile + Camera Înregistrării de Stat)
- **Identifier**: cadastral number (`numărul cadastral`) format `XXXX XXX XXX XX` (locality.zone.block.parcel) per Law No. 1543 of 25 Feb 1998 (Cadastru Law)
- **Foreign-buyer rule**: **residential freehold OPEN to foreigners** (no restriction since 2002 Civil Code modernisation); **agricultural + forest land BANNED** for foreign individuals + foreign legal entities (including Moldovan SRLs with foreign capital, even minority) under the **new Land Code in force 1 April 2025** (superseding Law No. 828-XII of 25 Dec 1991; 2026-05-27 verified, source jarniascyril.com guide + gov.md press archives) — only Moldovan citizens, Moldovan legal entities (with Moldovan ownership), the State, and local public authorities may own ag/forest land. Inherited / court-judgment / mortgage acquisitions trigger **mandatory divestment within 1 year**. The SRL-with-Moldovan-citizen-co-owners workaround is **more legally fragile under the new Code's explicit treatment of foreign-capital SRLs** (see `--visa` + Caveats)
- **Visa**: **90/180-day visa-free** for EU/EEA, UK, US, CA, AU, NZ, JP, KR, IL, GCC states (Law No. 200 of 16 Jul 2010 on regime of foreigners + Government Decision 384/2014 visa list); investor residence under same law for ≥ €250,000 economy investment

---

## Section: `--price`

### Primary sources

- **BNS (Biroul Național de Statistică)** — `https://statistica.gov.md/`
  - Quarterly **Indicele Prețurilor Imobiliare (IPLR)** — Real Estate Price Index, base 2018 = 100
  - Q4 2024 IPLR: ~144 (BNS press release Mar 2025) → +6.8% YoY total residential, Chișinău dominant
  - Sub-indices: secondary (resale) vs primary (new-build); urban vs rural
- **ASP cadastre** (paid extract): `https://cadastru.md/` — full title + ownership extract via e-Cadastru self-service or any ASP territorial office (~150–300 MDL standard, ~500–800 MDL urgent — verify current ASP tariff)
- **BNM (Banca Națională a Moldovei) Financial Stability Report**: `https://www.bnm.md/en/content/financial-stability-report-2024` — mortgage debt stock + bank-side property-market commentary
- **CNPF (Comisia Națională a Pieței Financiare)**: `https://www.cnpf.md/` — non-bank lending oversight, mortgage notarisation context
- **Cadastrul Bunurilor Imobile geoportal**: `https://www.asp.gov.md/en` — INSPIRE-aligned parcel viewer (public, no auth) — useful first cross-check before a paid ASP extract

### Price benchmarks (2024–2025 reference)

| Locality | New-build avg €/m² | Resale avg €/m² | Source |
|---|---:|---:|---|
| Chișinău (Centru, Buiucani, Râșcani prime) | ~€1,200–€1,800 | ~€900–€1,400 | 999.md aggregate Q4 2024; Lara.md market review 2024 |
| Chișinău (Botanica, Ciocana, Telecentru middle) | ~€800–€1,100 | ~€650–€900 | 999.md aggregate Q4 2024 |
| Chișinău (Sculeni, suburb commuter) | ~€600–€900 | ~€450–€700 | Makler.md 2024-Q4 |
| Bălți | ~€500–€750 | ~€350–€550 | Makler.md 2024-Q4 |
| Cahul (Prut border) | ~€450–€650 | ~€300–€500 | Makler.md 2024-Q4 |
| Orhei / Ungheni (district centres) | ~€400–€600 | ~€250–€450 | 999.md aggregate Q4 2024 |
| Rural village houses (case la sat) | n/a | ~€8,000–€35,000 outright | 999.md village-house segment |

> All €/m² are **est.** (calibration: cross-checked against BNS IPLR direction + ≥ 2 listing aggregators; primary-source €/m² not published by BNS — IPLR is index-only). Most listings priced in **EUR or USD** despite contracts denominated in **MDL** at BNM reference rate on signing day; verify exact figure on the day per BNM `https://www.bnm.md/en/content/official-exchange-rates`.

### Listing platforms

- **999.md** (largest classifieds, all categories incl. real estate): `https://999.md/ro/real-estate` *(per listing — verify with cadastre / on visit)*
- **Makler.md** (long-running real-estate-specific): `https://makler.md/` *(per listing — verify with cadastre / on visit)*
- **Lara.md** (real-estate portal with English UI): `https://lara.md/` *(per listing — verify with cadastre / on visit)*
- **Imobil.md** (newer aggregator, agency-heavy): `https://imobil.md/` *(per listing — verify with cadastre / on visit)*
- **Logos-Press / Bursa Imobiliară** (newspaper classifieds, niche but used by older sellers)
- Facebook groups (`Imobile Chișinău`, `Apartamente Chișinău`, etc.) — high volume, never authoritative

### Verdict bands (residential €/m², Chișinău reference)

- 🟢 within ±10% of district segment median (per 999.md / Lara.md, ≥ 5 comparables same street + condition)
- 🟡 ±20%
- 🟠 ±30% — investigate: pre-1990 panelka? Heat-network connection? Restitution status? Currency-mispricing?
- 🔴 >±30% — significant red flag

### Compute

1. €/m² = EUR listing ÷ m² advertised. **Trap**: Soviet-era convention often advertised "general" m² including walls + balcony; modern listings split "totală vs locuibilă vs utilă" — confirm which figure
2. Compare to BNS IPLR YoY direction for Chișinău
3. **Trap**: "preț negociabil" + EUR pricing — actual deal often 5–15% below ask after first cadastre check
4. **Trap**: "case la sat" (village houses, often 30–80 km from Chișinău) priced as bargain often have NO mains drains + NO mains water (see `--mains`); budget +€8,000–€20,000 for habitability uplift
5. **Trap**: "Pe roșu / la roșu" = bare-shell new-build (brick + roof + utilities-stubbed but no finishing); finishing budget typically +€150–€350/m² (est. — verify per quote)

---

## Section: `--traffic`

### Primary sources

- **Administrația de Stat a Drumurilor (ASD)** — state roads authority: `https://asd.md/` — annual traffic counts on national + regional roads (PDF reports)
- **Ministerul Infrastructurii și Dezvoltării Regionale**: `https://midr.gov.md/` — sectoral plans, road master plans
- **Primăria Chișinău (Direcția Generală Transport Public și Căi de Comunicație)**: `https://www.chisinau.md/` — Chișinău traffic + public transport
- **OSM Overpass** — universal fallback (see `shared/amenities-osm.md`)

### Key term

**AADT** equivalent in Romanian: `media zilnică anuală a traficului` (often abbreviated MZA or just "intensitatea medie")

### Verdict bands (residential noise impact)

- 🟢 < 1,000 v/d (rural side road, side street)
- 🟡 1,000–5,000 v/d (small municipal road, urban side street)
- 🟠 5,000–20,000 v/d (urban arterial, M-route national highway)
- 🔴 > 20,000 v/d (Chișinău inner ring — Bd. Ștefan cel Mare, Bd. Decebal, Bd. Dacia; M1 Chișinău–Leușeni; M3 Chișinău–Giurgiulești)

### Notes

- M14 / M21 / M2 = national routes; **R-prefix** = regional; **L-prefix** = local
- Chișinău private-vehicle fleet roughly doubled 2010 → 2024 per BNS transport stats; congestion now severe on Bd. Ștefan cel Mare, Bd. Negruzzi, Bd. Dacia, Calea Ieșilor
- Chișinău has no metro; **ring-road bypass (centura)** under reconstruction with EU/EBRD funding (2024–2027 phase) — properties along new bypass corridor will see noise+ during works
- **Trap**: rural properties advertised "5 min de la șosea" usually mean **on** a slip road or unpaved access — verify setback + paved access on visit

---

## Section: `--tax`

### Currency note

MDL, EUR/MDL ≈ 19.2–19.7 (Q1 2026 BNM, managed-float). Not in eurozone; no firm target. EU candidate but no ERM-II commitment (see `--currency`).

### Annual property tax — Impozit pe bunurile imobiliare (Tax Code Title VI, Art. 276–287)

Governed by [Codul Fiscal Republica Moldova](https://www.fisc.md/) Title VI; **rate set by each Local Council within statutory caps** (Art. 280):

**Residential immovables (apartments + houses)**:
- Statutory range: **0.05% – 0.4%** of cadastral value (rate set annually by each Local Council)
- Chișinău Sectorul Centru 2025 indicative: **0.3% of cadastral value** (per Decizia CMC No. 22/2 of 28 Nov 2024 — verify current at chisinau.md)
- Chișinău outer sectors (Botanica, Ciocana, Râșcani, Buiucani, Sculeni): **0.05–0.2%** typically
- "Cadastral value" maintained by ASP — **typically materially below market** (~30–60% of market price for resale apartments per BNM Financial Stability Report 2024 commentary)

**Land (terenuri)** — Art. 281 + Annex:
- Agricultural land: per-hectare fixed rates, e.g., arable Class I ~30 MDL/ha; Class V ~6 MDL/ha (Tax Code Annex; verify annual indexation per Tax Code Art. 280)
- Non-agricultural land (residential plot under house): 0.1%–1.5% of cadastral value (rate set by Local Council; Chișinău residential plots typically 0.3% per CMC decision)

### Example calculation

A €120,000 (≈ 2,316,000 MDL at 19.30 MDL/EUR) Chișinău Centru 2-bed apartment, ASP cadastral value ~€72,000 (≈ 1,389,000 MDL ≈ 60% of market):
- Annual property tax = 0.3% × 1,389,000 MDL ≈ **4,170 MDL/yr (~€216 / ~US$235)**

Same flat in Botanica, sectorul rate 0.1%, cadastral value 1,200,000 MDL:
- Annual property tax = 0.1% × 1,200,000 MDL = **1,200 MDL/yr (~€62)**

> Property tax in Moldova is materially low in absolute MDL terms; the mechanic is straightforward but cadastral-value deviation from market value is the dominant variable — verify per ASP extract.

### Transaction taxes (one-time at purchase)

- **VAT (TVA)** — Tax Code Title III:
  - **Standard rate 20%** (Art. 96)
  - **Reduced rate 8%** on residential dwellings sold by VAT-registered developer (Art. 96 lit. b — confirm scope in current Tax Code text); resale between individuals **exempt** (Art. 103)
- **Notary fee** (Lege 1453/2002 + Notarial Chamber tariff) — sliding scale:
  - up to 30,000 MDL value: ~600 MDL fixed
  - 30,000–100,000: 0.5% of value
  - 100,000–500,000: ~500 MDL + 0.3% on amount above 100,000
  - 500,000–1,000,000: ~1,700 MDL + 0.2% on amount above 500,000
  - >1,000,000 MDL: ~2,700 MDL + 0.1% on amount above 1,000,000 (cap effectively low — verify current tariff at notariat.md)
- **State duty (taxă de stat)** — Lege 1216/1992: **0.5–2%** of contract value sliding by transaction class (residential resale typically the lower band)
- **ASP cadastral registration fee**: ~150–300 MDL standard, ~500–800 MDL urgent (verify ASP tariff)
- **Total transaction cost** (buyer side, individual–individual resale): typically **1.5–3% of price** before agent commission

### Capital gains tax — individual sale (Tax Code Art. 18, 20, plus standard 12 % PIT under Art. 15; 2026-05-27 verified, sources PwC Tax Summaries Moldova (last reviewed 14 Jan 2026) + globalpropertyguide.com + intelcont.md)

- **There is no separate CGT rate in Moldova.** The capital gain on real-estate sale by an individual is **50 % included in gross income** (effective 1 Jan 2020; pre-2020 inclusion was 20 %) and taxed at the standard **12 % PIT** under Art. 15 → **effective burden ≈ 6 % of the gross gain**. The prior playbook framing of a "6 % flat CGT" was structurally misleading — the 6 % effective rate is coincidental, not a standalone tax line.
- **Primary-residence exemption** (Tax Code Art. 20): the gain on sale of a dwelling **owned for ≥ 3 years AND used as the taxpayer's domicile during the 3 years immediately prior to sale** is **fully non-taxable**. The exemption is **3 + 3 years, NOT 5 years** (the prior playbook 5-year figure was wrong — affects resale-timing decisions).
- Withheld by notary or self-declared on annual form CET18.

### Wealth / luxury tax on high-value residential (Tax Code Title VI¹ — "Impozit pe avere"; 2026-05-27 verified, sources PwC Tax Summaries Moldova other-taxes + logos-pres.md + intelcont.md)

Moldova has a **0.8 % wealth tax on high-value residential real estate** since 2016 (the playbook previously asserted "no wealth tax" — this was wrong):

- **Rate**: 0.8 % of cadastral value of the **building** (land excluded)
- **Threshold (both must be met)**: (a) dwelling total estimated value ≥ **200 × average forecast monthly economy wage** AND (b) **floor area ≥ 120 m²**
- **2025 threshold (value test)**: ~**3.22 million MDL** (~€163k–€168k at current BNM rates)
- **Payment**: notified by the territorial tax office based on a 1 November snapshot; due by **25 December** of the reporting year

This is a meaningful annual cost for any foreign buyer targeting a 130 m²+ Chișinău Centru flat priced above ~€170k.

### Rental income tax (Tax Code Art. 88¹)

- **7% withholding** at source on gross rental income paid to individuals — final tax (one-time, no further declaration) when withheld by tenant who is a legal entity, OR by individual landlord registering the contract with the tax authority (SFS — Serviciul Fiscal de Stat)
- **Alternative**: include rental in personal income declaration at standard **12% PIT** (Art. 18 lit. d) — but the 7% one-time route is usually preferred
- **Contract registration with SFS mandatory** within 7 days of signing — failure exposes both parties to fines + retroactive 12% PIT

### Personal income tax — general

- **12% flat PIT** for natural persons (Tax Code Art. 15) since 2018 reform (replacing prior 7%/18% bracketed system)
- **Corporate income tax (CIT)**: 12% (Art. 15.1)
- **Dividend WHT**: 6% (Art. 91)

### AML / cash limits

- Cash payments by legal entities to individuals: cap **MDL 100,000** per transaction per Law No. 308/2017 on AML/CTF
- Bank-to-bank wire is the standard channel for any transaction > MDL 100,000
- Notaries are AML "obligated entities" — must verify source of funds; politically exposed person (PEP) check mandatory
- BNM + SPCSB (Serviciul Prevenirea și Combaterea Spălării Banilor) coordinate enforcement

### Future risk

- **January 2027 cadastral revaluation** (2026-05-27 verified, source EuropaLibera Moldova reporting + government press): scheduled reset of the cadastral-value base across ~6 million immovables, **officially projected to raise effective property-tax bills by ~150–190 %** without any rate change. A €120k Chișinău Centru flat paying ~€216/yr today would move to ~€540–€620/yr post-revaluation — re-verify after the October 2026 approval round and recompute TCO. Single largest 2026–2027 buyer-decision signal for MD purchases in the next 18 months.
- **EU candidate status (Jun 2022) + accession opening (Jun 2024)**: harmonisation pressure on transfer-tax + AML alignment; expect tightening of beneficial-ownership transparency over 2026–2030 horizon
- **2024 Constitutional reform** enshrined EU-integration objective — irreversible direction without further constitutional change
- **Tax Code amendments** announced annually via November budget law; monitor `https://www.fisc.md/` + `https://www.parlament.md/`

---

## Section: `--rental`

### Long-term residential

- **Individual landlord, 7% one-time WHT** on gross rent if contract registered with SFS (Tax Code Art. 88¹) — final tax, no expense deductions
- **Alternative**: 12% PIT on net (with documented expenses) via annual CET18 declaration
- Mandatory contract registration with SFS within 7 days
- No rent-control regime nationally; private-law contracts (Civil Code Art. 1252+) govern

### Short-term rentals (STR / Airbnb / Booking)

#### Regulatory framework

- **2018 Law on Tourism Activity (Law No. 352/2006)** + **2023 amendments** introduced mandatory registration of accommodation establishments with **ANTRIM (Agenția de Investiții)** — `https://invest.gov.md/` (formerly Agenția Turismului)
- Hosts must classify accommodation (`structuri de cazare`) → register, obtain `Certificat de clasificare` from Ministerul Culturii / ANTRIM (1, 2, 3, 4, 5 stars or "casă de oaspeți" / guesthouse band)
- **Chișinău municipal layer**: 2024 Decizia CMC introduced supplementary STR registration at primarie sector level (verify current at chisinau.md)
- Tourist tax (`taxa pentru servicii turistice`): levied locally, typically **1–2% of accommodation tariff** per Local Council decision

#### Tax classification

- **Individual host (PFA equivalent — `persoană fizică care desfășoară activitate independentă`)**: register at SFS, file annual; effective tax 7% one-time on gross OR 12% PIT on net
- **Above MDL 1,200,000 annual turnover**: must register as **SRL** (Societate cu Răspundere Limitată) or as `întreprinzător individual (ÎI)`; CIT 12% on profit + dividend WHT 6%
- **VAT (TVA)**: registration mandatory if turnover > MDL 1,200,000/12 months (Tax Code Art. 112) — STR over the threshold falls under the 8% reduced rate for accommodation services (verify Art. 96 current scope)

#### Practical (2025–2026)

- Enforcement of STR registration is **patchy outside Chișinău Centru**; ANTRIM 2024 sweep audited ~340 platforms-listed flats and reported ~70% non-registered (per ANTRIM annual report — verify specific figures)
- **Trap**: HOA (`asociație de coproprietari`) bylaws often restrict STR in Chișinău newer developments — check before buying
- **Trap**: pre-1991 panelka building entrance security + concierge typically NOT compatible with self-check-in; expect tenant-mix friction

### Strategic notes

- **Chișinău Centru (Centru, Buiucani-1)**: highest year-round STR yield; conference + business + diplomatic demand; estimated gross yield 6–10% on €/m² basis
- **Old Town / Sfatul Țării heritage area**: thin STR pool but high rate per night; heritage-listing restrictions on renovation
- **Long-term residential Chișinău**: gross yields commonly cited **5–8%** (Lara.md / Imobil.md 2024 — verify against your specific listing); mid-2024 supply uptick from Ukrainian-displaced inventory churn

---

## Section: `--work=<profession>`

### Job platforms

- **Rabota.md** — largest job board: `https://www.rabota.md/`
- **Delucru.md** — long-running general: `https://www.delucru.md/`
- **999.md/work** — classifieds-style
- **LinkedIn Moldova** — active in IT, BPO, NGO, finance
- **ANOFM (Agenția Națională pentru Ocuparea Forței de Muncă)**: `https://anofm.md/` — official labour portal, vacancy register

### Self-employment regimes (foreigners eligible with valid residence)

- **Întreprinzător individual (ÎI)**: register at ASP in 1–3 days, ~165 MDL fee; default 12% PIT on net
- **Patenta de întreprinzător** (sole-trader patent): for low-turnover micro-business, fixed monthly fee — limited categories; foreign-individual eligibility constrained, verify per category
- **SRL (Societate cu Răspundere Limitată)**: 1-day ASP registration; minimum capital MDL 5,400; 12% CIT on profit + 6% dividend WHT
- **Tax residency**: 183+ days in any 12-month period OR vital-interests centre in Moldova (Tax Code Art. 5(2)–(3))

### IT-specific incentive — Moldova Innovation Technology Park (MITP)

- **MITP virtual park** (Law No. 77/2016): qualifying IT residents pay a single **7% of revenue** unique tax in lieu of CIT + PIT + social contributions + property tax for IT activity (verify current rate per `https://moldovaitpark.md/`)
- Park membership open to foreign-owned IT firms with substance in Moldova; very competitive vs neighbouring Romania flat-12% IT regime

### Salaried benchmarks

- Average monthly nominal wage 2024 Q4 (BNS): **~13,800 MDL gross** (~€720) — economy-wide
- IT/finance Chișinău: ~25,000–60,000 MDL/month for mid-level (Rabota.md market reports 2024)
- **Minimum wage**: **MDL 5,000/month** (set by Government Decision; revised periodically — verify at gov.md); apparent low base masks high informality in some sectors

### Catchment heuristics

- Within 30 min of Chișinău central districts: full salaried opportunity (IT, BPO, finance, NGO, diplomatic)
- Bălți: regional manufacturing + retail jobs; 30-min catchment limited
- Cahul (Free Economic Zone) + Comrat (Gagauzia): regional industrial / agro
- Rural raions: agriculture + remittance economy + remote-work; very thin local salaried market

### Visa / residence pathway for working foreigners

- **90/180-day visa-free** for Western passports (above) — covers business-trip / scoping
- **Work + residence permit** via the [Inspectoratul General pentru Migrație (IGM)](https://igm.gov.md/) (the former Biroul Migrație și Azil / BMA): tied to employer or business; processing ~30 days
- **Investor residence permit** (Law 200/2010 Art. 50): minimum **€250,000** investment in the Moldovan economy → 5-year permit, renewable; pathway to naturalisation after 8 years' continuous residence (Law No. 1024/2000 on Citizenship Art. 17)
- **Romanian-citizenship path** (Law No. 21/1991 Romania): Moldovans of Romanian descent (very large pool, both pre-1940 + Bessarabian heritage) eligible for **EU Romanian passport via descent** — material indirectly because dual-citizen Moldovan-Romanian buyers face NO foreign-buyer restriction in Romania for residential AND already have full EU access from a Moldovan address

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Inspectoratul General pentru Situații de Urgență (IGSU)** | `https://www.igsu.gov.md/` | Operational hazard data, flood/fire response |
| **Serviciul Hidrometeorologic de Stat (SHS)** | `https://www.meteo.md/` | Weather, flood warnings, climate baseline |
| **Institutul de Geologie și Seismologie (IGS / AȘM)** | `https://igs.asm.md/` | Seismic monitoring, fault maps, earthquake history |
| **Ministerul Mediului** | `https://mediu.gov.md/` | Environmental risk reports, climate strategy |
| **ANRE (Agenția Națională pentru Reglementare în Energetică)** | `https://www.anre.md/` | Energy/utility safety, fuel-storage zoning |
| **ANRCETI** | `https://www.anrceti.md/` | Telecoms; only tangential to property risk |

### Seismicity — material concern

- Moldova sits adjacent to the **Vrancea seismic zone** (Romania) — same intermediate-depth fault system that defines Bucharest seismic risk
- **Major historical events felt strongly in Chișinău**:
  - **1940-11-10 Vrancea Mw ~7.4**, hypocenter ~120 km depth — significant damage in Chișinău + Bălți
  - **1977-03-04 Vrancea Mw 7.5**, hypocenter ~94 km — Chișinău MSK VII–VIII; substantial damage to old building stock
  - **1986-08-30 Vrancea Mw 7.2**, hypocenter ~130 km — Chișinău MSK VI–VII
  - **1990-05-30/31 Vrancea Mw 6.9 + 6.4** — minor damage Chișinău
- Chișinău designated **MSK seismic intensity zone 7** (some peri-urban zones 8); design PGA ~0.20–0.25g per NCM E.04.02 (Moldovan seismic code aligned with Romanian P100-1)
- **Pre-1991 Soviet panelka stock** (`khrushchyovka` / `seria 102 / 143 / 135`): retrofit status uneven; no national consolidation programme equivalent to Bucharest AMCCRS — **independent structural survey strongly advised** before purchase of pre-1990 multi-storey

### Flood

- **Dniester (Nistru)** + **Prut** are the two main rivers; both border + transboundary
- **Major flood events**: 2008 (Prut + Nistru) widespread Cantemir/Cahul; 2010 Prut Cahul-Giurgiulești; 2020 minor
- **Flood hazard maps**: SHS + IGSU publish at locality level; **EU PEGASO project** (2020–2024) assisted Moldova in developing INSPIRE-aligned flood-risk maps under EU Floods Directive 2007/60/EC alignment (verify map availability at `https://www.meteo.md/` + `https://www.igsu.gov.md/`)
- **Verification path**: maps are commune/locality-level, not parcel-level. For parcel-grade hazard certification, request from SHS or commission private hydrological assessment (~€500–€1,500)

### Landslide / soil instability

- **Codrii region** (Călărași, Strășeni, Nisporeni, Ungheni raioane): central Moldova hilly forested zone — significant landslide susceptibility, particularly post-rainfall
- **Cricova / Goian / Chișinău northern slopes**: known landslide-prone zones (some properties on former vineyard terraces)
- **Verification**: IGS landslide registry (IGS public maps Romanian-only) + commune-level Plan Urbanistic General (PUG) — request from primarie

### Drought

- Eastern + southern Moldova (Cahul, Cantemir, Ștefan Vodă) increasingly drought-prone; viticulture stress
- Moldova UNFCCC 4th National Communication 2024: ~+1.2°C warming since 1961; +1.8–4.5°C projected by 2080 (RCP4.5 / RCP8.5)

### War-spillover risk

- **Russia–Ukraine war (Feb 2022 →)** has caused intermittent missile-debris incidents in northern Moldova (Briceni, Edineț, Soroca, Dondușeni raioane) 2022–2024; air-defence integration with EU partners ongoing
- **Transnistria (Stânga Nistrului) frozen conflict** since 1992 — see Caveats; baseline risk has not escalated to active hostilities since the 1992 ceasefire
- **EU/Russia geopolitical exposure**: insurance underwriters apply elevated political-risk loading for Moldovan property post-2022 — monitor

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1918 (Tsarist)** | Soft-fired brick + lime mortar; lead paint likely; weak seismic performance; some heritage-listed (Chișinău Centru) |
| **1918–1940 (Romanian inter-war)** | "Stalinist precursor" + Romanian inter-war styles; thicker walls; asbestos roofing some |
| **1940–1991 (Soviet)** | Khrushchyovka 5-storey + 9 + 16-storey panelka (seria 102, 143, 135); asbestos joints common; aging utility risers; uneven seismic retrofit |
| **1991–2003 (post-independence collapse)** | Often unpermitted ("self-build"); legalised in waves under 2007 + 2014 amnesties — verify ASP recordation |
| **2003–2014 (boom)** | Building boom Chișinău; quality varies; 2010 Construction Law overhaul (Law 721/1996 amendments) tightened standards |
| **2014–present** | Modern code; energy-efficiency requirements (Law 128/2014 transposing EU EPBD); EPC mandatory for new build + transfer (verify enforcement) |

**Asbestos**: pre-2005 likely in roofing + insulation; no national mandatory removal regime — buyer due diligence required.

### Mandatory documents at sale

| Document | Required because | Notes |
|---|---|---|
| **ASP extract (`extras din registrul bunurilor imobile`)** | All sales | Verify owner + cadastral number + encumbrances (`gaj` / mortgage, `sechestru` / seizure) |
| **Sale-purchase contract** | All sales | Notarised; in Romanian; ASP recordation within 30 days |
| **Cadastral plan** | All sales | Issued by ASP; ensure matches building footprint |
| **Energy Performance Certificate (Certificat de performanță energetică)** | New build + transfer (Law 128/2014) | Validity 10 yrs; enforcement uneven on resale — **request and check** |
| **Building completion certificate (`act de dare în exploatare`)** | New builds + extensions | Confirms construction completed legally; often missing for pre-2007 self-built — affects future renovation/extension permits |
| **No-debt certificate** (utilities, building management fees) | Apartments in managed buildings | From asociația de coproprietari (HOA) — ensure no fund-debts attached to flat |
| **Heritage listing check** | Old Town Chișinău + heritage zones | Ministerul Culturii Register: `https://mc.gov.md/` — listing imposes severe renovation restrictions |

### Climate change projections (Moldova UNFCCC 4th National Communication 2024)

- Mean annual temperature: +1.2°C since 1961; +1.8–4.5°C projected by 2080 (RCP4.5 / RCP8.5)
- Annual precipitation: regional shift — south drier, north wetter; +/− 10–15% by 2080
- Drought frequency: doubling by 2050 in southern raions; viticulture region (Cricova, Mileștii Mici, Purcari) under stress
- Heatwaves: Chișinău summer days > 35°C projected to triple by 2050 (SHS scenario report 2024)
- Flood frequency: +20–40% by 2080 along Prut + Nistru floodplains
- **Climate Adaptation Strategy 2030** (Government Decision approved 2023; verify current at mediu.gov.md)

---

## Section: `--mains`

### National database

- **ANRE (Agenția Națională pentru Reglementare în Energetică)**: `https://www.anre.md/` — utility tariffs (electricity, gas, district heating, water + sewer where regulated)
- **ApăCanal Chișinău**: `https://acc.md/` — Chișinău city water + sewer operator (~660k served)
- **Moldova-Apă (Asociația "Moldova Apă-Canal")**: `https://amac.md/` — federation of regional water utilities (~32 raioane)
- **Termoelectrica**: `https://termoelectrica.md/` — Chișinău district heating + power generation (~80% of Chișinău apartments connected)
- **CET-Nord** (Bălți): `https://cet-nord.md/` — Bălți cogeneration + DH
- **Moldovagaz**: `https://www.moldovagaz.md/` — gas distribution (post-2022 supply diversification — see Caveats)
- **Premier Energy / RED-Nord**: electricity distribution Chișinău south + north respectively

### Verification

1. Listing language:
   - "termoficare centrală" / "agent termic centralizat" = Termoelectrica DH connection
   - "centrală pe gaz" / "centrală autonomă" = individual gas boiler (often retrofitted in panelka)
   - "apeduct + canalizare centrală" = full mains water + sewer
   - "fântână" / "puț" = own well; verify potability + permit
   - "haznă" / "fosă septică" = no mains sewer
2. **Chișinău urban core**: mains water + sewer assumed; **verify with ApăCanal Chișinău before signing** (rare patches of unconnected legacy stock exist on city periphery)
3. **Bălți + raional centres**: mostly mains; verify with operator
4. **Villages and dachas**: often water-only or seasonal water; sewer rare; many rely on cesspits

### Costs

| Scenario | Cost (EUR, est.) |
|---|---:|
| Connection to existing nearby mains (urban) | ~€300–€1,500 |
| Mains drain extension (parcel where trunk line exists nearby) | ~€1,000–€4,000 |
| Borehole drilling (50–80 m) | ~€2,000–€6,000 |
| Septic tank install (typical residential) | ~€1,000–€3,000 |
| Modern WWTP (BIO compliance) | ~€3,500–€10,000 |
| Gas connection from street main | ~€500–€2,500 |

> All EUR ranges are **est.** based on Chișinău + Bălți 2024–2025 contractor quotes aggregated from 999.md trade-services classifieds + ApăCanal Chișinău + Moldovagaz published connection-charge schedules. Verify with 2+ quotes per project.

### Utility tariffs (2025–2026, regulated by ANRE)

| Utility | Tariff (residential, indicative) |
|---|---|
| **Electricity (Premier Energy ≤ 100 kWh/month)** | ~2.34 MDL/kWh (~€0.12) — verify current ANRE schedule |
| **Electricity (>100 kWh/month band)** | ~2.50 MDL/kWh |
| **Natural gas (Moldovagaz residential)** | ~12.5–14.0 MDL/m³ — substantially elevated post-2022 supply reform |
| **Water (ApăCanal Chișinău)** | ~9.30 MDL/m³ + ~12.50 MDL/m³ sewer = ~21.80 MDL/m³ combined |
| **District heating (Termoelectrica)** | ~1,540–1,700 MDL/Gcal — verify current ANRE schedule |

(Tariffs verified against anre.md + termoelectrica.md 2025 published schedules — confirm current rates; gas + DH tariffs particularly volatile post-2022 supply diversification.)

### Energy supply post-2022 reform

⚠️ **Pre-2022**: Moldova received ~100% of natural gas via Gazprom; ~80% of electricity via Cuciurgan thermal plant in Transnistria (gas-fired, Russian-operated). **Post-2022**: gas supply diversified via Romania interconnector + EU LNG; electricity grid synchronised with **ENTSO-E (continental Europe)** in **March 2022**; Cuciurgan exposure materially reduced 2022–2024 (winter 2022–23 partial outages; managed thereafter). Property buyers should expect ongoing tariff volatility 2025–2027 as transition completes.

---

## Section: `--crime`

### Primary sources

- **Inspectoratul General al Poliției (IGP)**: `https://politia.md/` — national crime statistics, district-level
- **BNS criminal-statistics annual yearbook** (Anuarul Statistic al Republicii Moldova, Capitolul Justiție): `https://statistica.gov.md/`
- **Procuratura Generală**: `https://procuratura.md/` — prosecutorial statistics

### Headline (2024 IGP + BNS annual data)

- **Total registered crimes 2024**: ~31,400 (vs ~33,800 in 2020 — declining trend)
- **Property-related crimes** (theft, burglary, fraud): ~52% of total registered
- **Chișinău municipality**: ~38% of national total registered crimes (population share ~26% — urban-density effect)
- **Homicide rate 2023**: ~3.6 per 100k (BNS) — moderate by regional standard, declining since 2014

### Verdict bands (parcel-level inference)

🟢 Chișinău residential sectors (Buiucani, Râșcani, Sculeni residential interiors); Bălți residential; rural raioane low-density villages
🟡 Chișinău Centru tourist zones (pickpocketing, scam exposure); Bălți Centru; raional centres
🟠 Specific high-incidence localities (CMC notes "zone cu risc sporit" updated annually) — verify per address
🔴 No specific routinely-flagged 🔴 zones in Chișinău; Transnistria has separate policing (out of scope)

### Verification

For parcel-level: request the local police sector ("sector de poliție") incident summary; informal but standard. IGP doesn't publish parcel-grade open data.

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`. Moldova is well-mapped on OpenStreetMap (Chișinău dense; villages thinner). Romanian + Russian + occasional Ukrainian name tags; query with `name:ro` preferred.

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`. National source: Serviciul Hidrometeorologic de Stat (`https://www.meteo.md/`) + Moldova UNFCCC 4th National Communication 2024 (Ministerul Mediului). Key projections: +1.8–4.5°C by 2080; drought intensifies south, precipitation +/-10-15%; viticulture-belt stress.

---

## Section: `--finance`

### Mortgage market

- **Regulator**: [BNM — Banca Națională a Moldovei](https://www.bnm.md/) — sets prudential rules, monetary-policy rate (5.0% Q1 2026 BNM monetary-policy decision — verify), loan-classification rules
- **Major banks** (BNM 2024 supervisory list): **Maib** (ex Moldova-Agroindbank, largest), **MICB** (Moldindconbank), **OTP Bank Moldova**, **Victoriabank** (Banca Transilvania group), **EuroCreditBank**, **EXIMBANK**, **ProCredit Bank**, **FinComBank**, **Energbank**, **BCR Chișinău**, **Comerțbank** — 11 licensed banks in 2025
- **LTV caps (residential, 2024–2025 BNM prudential guidance)**:

| Borrower | Max LTV |
|---|---:|
| Resident first-home buyer | typically **80%** |
| Resident second-home / investment | **60–70%** |
| Non-resident foreign buyer | typically **50%** if accepted at all (case-by-case) |

- **DTI / DSTI**: BNM Regulation 109/2018 caps debt-service at typically **40%** of net income; income evidence required (tax return + employment contract)
- **Rate structure (2024–2026)**:
  - **MDL-denominated mortgages**: typical 7–12% nominal; tied to BNM rate + bank margin
  - **EUR-denominated mortgages**: typical 5–8% but **strict eligibility** (income in EUR or hedge demonstration); BNM tightened FX-loan rules post-2014 banking crisis (Reg. 109/2018)
  - 20–25-year tenors standard; 30-year rare
- **Foreigner mortgages**: extremely limited; most Moldovan banks require resident status + Moldovan tax residency + 24+ months income history. **Cash purchase is the standard foreign-buyer route.**

### Banking access

- Account opening: **passport + IDNP (national ID number, issued by ASP for foreigners on residence)** + proof of address + AML KYC (source-of-funds declaration)
- Non-resident accounts increasingly available at Maib + OTP for EU-passport holders (post-2022 normalisation); Russia/Belarus-passport holders face heightened scrutiny under EU sanctions alignment

⚠️ **2014 banking crisis legacy**: ~US$1B disappeared from BC, BS, Unibank in 2013–2014 ("Theft of the Century"); BNM resolution + EU/IMF support since. Sector now tightly supervised; concentration in Maib + MICB + OTP + Victoriabank > 80% of system assets.

---

## Section: `--currency`

### MDL — Moldovan leu

- **Code**: MDL; subdivided into 100 bani; banknotes 1, 5, 10, 20, 50, 100, 200, 500, 1000 MDL
- **Regime**: managed-float since 1998; BNM intervenes to smooth volatility but does not target a fixed rate
- **Issuer**: [Banca Națională a Moldovei (BNM)](https://www.bnm.md/) — sole issuer; reference rate published daily on `https://www.bnm.md/en/content/official-exchange-rates`

### Recent volatility (2022–2026)

- 2022 war shock: MDL depreciated ~10% vs EUR Mar–Sep 2022; BNM hiked policy rate to 21.5% (Sep 2022)
- 2023: rate cut cycle to 4.5% by Dec 2023; MDL stabilised at 19.0–19.7 EUR/MDL
- 2024–2026: range-bound 19.0–19.8 EUR/MDL; BNM policy rate 4.0–6.0% range
- USD/MDL: 17.5–18.5 range Q1 2026

### What this means for buyers

- **EUR buyers**: 5–8% annualised volatility realised 2020–2025; significant depreciation risk during macro-shocks (2022 demonstrated)
- **USD buyers**: similar; MDL is a small-economy currency without hard peg
- **MDL-priced contract** is the legal requirement (Civil Code) — you negotiate in EUR but **sign in MDL at BNM rate of signing day**; price-creep risk between offer + signing for EUR-budgeted buyers
- **Hedging**: thin FX-forward market; bank-side hedging available at Maib + OTP for amounts > €100k but spreads wide (50–150 bps for 90-day forward)
- **Capital controls**: no formal capital controls 2025; BNM has reserve power to impose under Law 232/2016 in crisis

### EU candidate trajectory

- EU accession negotiations opened Jun 2024; ERM-II + euro adoption is a 10–15 year horizon at minimum (post-accession)
- **Constitutional reform Oct 2024** enshrined EU-integration objective — currency-substitution (euroisation in private contracts) likely to grow; full euro adoption requires ERM-II minimum 2 years post-accession

### Tail risks

⚠️ Moldova is a small open economy with elevated geopolitical exposure (Russia–Ukraine war proximity); MDL has experienced > 15% one-year depreciation events (2014, 2022). Position-size foreign-currency-denominated buyers accordingly.

---

## Section: `--visa`

### Property-linked / investor schemes

| Scheme | Threshold | Visa | PR/citizenship path |
|---|---|---|---|
| **Investor residence** (Law 200/2010 Art. 50) | ≥ €250,000 economy investment | 5-yr renewable | Naturalisation after 8 yrs continuous |
| **Skilled worker / employer-sponsored** | Employment contract | 1-yr renewable | Naturalisation after 8 yrs |
| **Family reunification** | Spouse/parent of MD citizen/PR | 1-yr renewable | Standard naturalisation timeline |
| **Visa-free 90/180** | EU/EEA/UK/US/CA/AU/NZ/JP/KR/IL/GCC + ~50 more | 90 days/180 days | n/a |

### CBI / golden-visa status

- **Programul Cetățenia pentru Investiții (Moldovan CBI)**: launched 2018 (Law No. 1024/2000 amended); required ~€100k contribution to Public Investment Fund + property + due-diligence fees → Moldovan citizenship
- **STATUS: ENDED** — programme suspended **June 2018** (within months of launch) under EU + OECD pressure; formally repealed 2020 by Law No. 100 of 16 May 2020 amending Law 1024/2000
- **No active CBI in Moldova as of 2026**; verify before any historical-program reference (see `shared/visa-programs.md` ENDED registry)

### Pathway specifically for property buyers

- **Property purchase alone does NOT confer residence** — Moldova has no real-estate-linked golden visa equivalent to Portugal-D7 / Spain-DNV / Greece pre-2024
- Foreign buyer typically holds property as **non-resident** with no residence rights from the property; physical presence governed by visa-free 90/180 rule for Western passports
- **Investor residence Law 200/2010 Art. 50 €250k threshold**: real estate investment may qualify but typically requires productive-economy criteria — verify with the [Inspectoratul General pentru Migrație (IGM)](https://igm.gov.md/) (the former BMA) before relying

### Romanian-citizenship adjacency

- Moldovans of Romanian descent (very large pool) eligible for **Romanian citizenship via Law No. 21/1991** (descent recovery) → full **EU passport**
- This is an INDIRECT property-decision factor: a Romanian-citizen Moldovan resident has full Schengen mobility + freedom of establishment in any EU member state, materially altering exit-optionality for Moldovan property holders

---

## Section: `--insurance`

### Mandatory

- **No nationally mandatory home-insurance scheme** for owner-occupiers (unlike Romania's PAID); private market voluntary
- **Mortgage lenders mandate fire + structure cover** for any mortgaged property (standard practice; verify per bank)
- **Third-party liability** typically embedded in fire/contents bundle

### Optional (standard market, 2024–2026)

| Cover | Typical premium (EUR/yr, indicative) |
|---|---:|
| Building structure (Chișinău 2-bed, sum insured ~€80k) | €100–€220 |
| Home contents (typical 2-bed) | €40–€120 |
| Earthquake | usually included up to small sub-limit; full earthquake top-up +€30–€80/yr |
| Flood (riverine) | included in major bundles, sub-limit applies; verify Prut/Nistru zone |
| Liability (3rd-party) | usually bundled |

### Major insurers (CNPF supervised)

- **Moldasig** (largest non-life, Maib group)
- **Donaris** (state-owned, public-sector default)
- **Asito** (long-running, broad book)
- **Klassikabank Sigorta** (regional)
- **Grawe Carat Asigurări** (Austrian Grawe group)
- **General Asigurări** (boutique non-life)
- Compare via CNPF supervisory list: `https://www.cnpf.md/` + Moldsigur.md aggregator

### Climate trajectory note

⚠️ Moldovan insurers raising premiums 4–8%/yr 2023–2026 driven by 2020+2022 flood claims + 2022 war-spillover political-risk loading; flood sub-limits tightening for Prut/Nistru floodplain properties; check policy schedule before signing.

---

## Section: `--notary`

### Conveyancing process

Moldova is **civil-law**; **notar** mandatory for any immovable-property transfer per **Civil Code Art. 213** (sale-purchase, donation, exchange, mortgage). Notary contract validated + transferred to ASP (cadastre) for recordation. Notary licensed under Law No. 246/2018 on Notarial Activity, supervised by Camera Notarială.

### Standard timeline

| Step | Day | What happens |
|---|---|---|
| 1. Pre-contract / promise of sale (`antecontract` / `promisiune de vânzare`) | D0 | Buyer pays earnest deposit (`avans` typically 10%); not strictly required but standard |
| 2. ASP extract pulled | D0–D7 | Buyer's notary or lawyer obtains current `extras din registrul bunurilor imobile` |
| 3. AML / source-of-funds review | D0–D14 | Notary verifies; bank channel for any payment > MDL 100k |
| 4. Notary sale-purchase deed signed | D14–D30 | Both parties present; original deed in Romanian; certified translation if buyer non-Romanian-speaking |
| 5. ASP recordation | D14–D44 | Within 30 days of deed; ASP issues updated extract reflecting new ownership |

### Costs

| Item | Typical |
|---|---|
| **Notary fee** (sliding, see `--tax` section) | ~0.1–1.5% of contract value (front-loaded for low-value transactions) |
| **State duty (taxă de stat)** | 0.5–2% of contract value |
| **ASP recordation fee** | ~150–300 MDL (€8–€16) |
| **Translator (if required)** | ~€100–€300 |
| **Lawyer (optional)** | €300–€1,500 typically for foreign-buyer transactions |
| **Total transaction cost (buyer side, residential)** | **~1.5–3% of price** |

### Notary selection

- Camera Notarială register: `https://cnm.md/lista-notarilor/` — ~280+ notaries, mostly Chișinău
- **Buyer should engage independent notary** (not seller's) — common practice but not statutorily required

### Foreign buyer practical

- **Non-Romanian-speaker**: certified translator must be present at deed signing OR full bilingual deed + sworn translation
- **Power of Attorney**: foreign buyer can authorise Moldovan-based representative via apostilled PoA (from country of residence) — common workaround if buyer not present in MD on signing day
- **AML / source-of-funds**: notary required to obtain bank statements + source-of-funds under Law 308/2017; PEP screening mandatory

---

## Section: `--compare`

### Moldova vs regional neighbours (residential investment lens, Q1–Q2 2026)

| Country | Foreign-buyer rule | Acquisition cost (typical) | Annual recurring | Yield (2024) | Currency |
|---|---|---:|---:|---:|---|
| **🇲🇩 Moldova** | Open (residential); ag/forest banned for foreign individuals | 1.5–3% | 0.05–0.4% × cadastral value | ~5–8% Chișinău | MDL managed-float |
| **🇷🇴 Romania** | EU/EEA full; non-EU buildings only (no land) | ~2–3% | ~0.1–0.3% × cadastral (rising 2026 reform) | ~5–7% Bucharest | RON managed-float |
| **🇺🇦 Ukraine** | War conditions — DD highly disrupted | n/a (war) | n/a | n/a | UAH war regime |
| **🇧🇬 Bulgaria** | EU/EEA full; non-EU residential OK; ag land restricted | ~3–5% | low | ~4–6% Sofia | BGN currency-board to EUR |
| **🇬🇪 Georgia** | Open (residential); ag banned post-2017 | 0.1–0.5% | 0–1% × market (income-threshold) | ~6–10% Tbilisi | GEL managed-float |

### Moldova's distinctive position

- **Lower property-acquisition tax than Romania/Bulgaria** (1.5–3% vs Romania 2–3% post-2026 reform; Bulgaria 3–5% — though Georgia lower still at 0.1–0.5%, see table above)
- **EU candidate (Jun 2022) + accession negotiations open (Jun 2024)** — accession path active; multi-year horizon; pricing today reflects "EU candidate discount" (BNS IPLR materially below regional EU peer per-€/m² comparison)
- **Currency risk**: MDL managed-float more volatile than BGN (currency-board) or RON (managed); position-size accordingly
- **Romania-citizenship adjacency**: large eligible-by-descent pool gives structural exit-optionality
- **War-spillover risk premium**: 2022 demonstrated meaningful tail risk; insurance + cash-purchase prevalence reflect

### Comparative reference

For Moldova vs Romania pre-2007-EU-accession parallels see `countries/ro/playbook.md`. For EU-candidate-discount peer see `countries/me/playbook.md` (Montenegro) and `countries/al/playbook.md` (Albania). For small-economy managed-float currency parallels see `countries/ge/playbook.md` (Georgia).

---

## Section: `--retirement`

### Retirement to Moldova scenario

Moldova is a **niche** retirement destination — primarily for diaspora-return + Romanian-passport holders + retirees seeking Black Sea proximity at sub-EU cost. Not a Lisbon/Valencia/Mexico-tier retirement market.

### Cost-of-living for retirees (Chișinău 2-bed apartment, conservative profile)

- Median 2-bed apt rental Q1 2026: ~€350–€700/month outside prime
- Public healthcare via Compania Națională de Asigurări în Medicină (CNAM): ~€250/yr voluntary contribution for non-employed; free at point-of-care for registered insured (limited coverage)
- Private health insurance for 65+: ~€600–€1,800/yr typical
- Public transport Chișinău: 6 MDL/ride (~€0.31); senior concession via municipal transport card
- Utilities (2-bed apt): ~€80–€180/month winter peak; ~€40–€80 summer

### Tax position for retirees

- **Foreign-source pension income**: typically taxed at **12% PIT** if MD-resident (Tax Code Art. 18); **double-tax treaties** (Romania, Germany, Italy, France, UK, US, Russia, Israel — verify per source country) may credit/exempt
- **CGT exemption** on residential sale where the dwelling was **owned ≥ 3 years AND used as the seller's domicile for the 3 years up to sale** (Tax Code Art. 20; 2026-05-27 verified, source PwC). Otherwise the gain is 50 %-included → 12 % PIT → ≈ 6 % effective
- **Moldova DOES levy a 0.8 % wealth tax** on residential buildings simultaneously meeting (a) value ≥ 200 × average forecast monthly economy wage (~3.22M MDL in 2025) AND (b) floor area ≥ 120 m² — see §`--tax` Luxury/wealth tax (2026-05-27 verified, source PwC). **No inheritance tax** — Moldova doesn't levy estate/inheritance tax (intra-family donations exempt under Art. 20)

### Healthcare access

- **CNAM** public system: 88 hospitals + ~1,200 primary-care centres; quality variable; tertiary in Chișinău (Spitalul Republican, Institutul Mamei și Copilului)
- **Major private**: Medpark (largest private hospital network), Genesis, Promed, MicroMed; all in Chișinău
- ⚠️ Specialist + advanced-oncology often referred to Romania (Iași, Bucharest, Cluj) or Turkey under bilateral agreements

### Verdict for retirement-first buyers

🟡 **Watch** — viable for diaspora returnees + Romanian-passport-eligible retirees + budget-conscious EU pensioners willing to bridge to Romania for tertiary healthcare; questionable for retirees prioritising mature healthcare market or large expat community. Best fit: Romanian-speaking retirees + Bessarabian-heritage diaspora + remote-working semi-retirees with private health insurance.

---

## Section: `--digital-nomad`

### Visa pathway

- **No formal "digital nomad visa"** as of 2026 (compared to PT-D8 / ES-DNV / EE-DNV)
- Practical pathways:
  1. **Visa-free 90/180** for Western passports — covers short-term remote stays
  2. **Investor residence Law 200/2010** at €250k threshold — overkill for typical DN
  3. **Employer-sponsored work residence** — only if MD-employer-tied
  4. **MITP (Moldova IT Park) status** for IT professionals registering substance — if turnover and activity criteria met (`https://moldovaitpark.md/`)

### Connectivity

- **Internet**: Moldova consistently ranks **top-10 globally** for fixed-broadband speed (Speedtest Global Index — verify current ranking); Moldtelecom + StarNet + Sun Communications + Orange Moldova offer 1-Gbps fibre at €10–€20/month residential (one of cheapest globally)
- **Mobile**: Orange + Moldcell + Unite — 5G launched 2024 in Chișinău; ~€10/month for 50+ GB
- **Co-working Chișinău**: Tekwill (USAID-supported, IT focus), iHub Chișinău, MITP-affiliated spaces; €80–€200/month hot desk
- **Time zone**: UTC+2 (UTC+3 DST) — favours EU + Middle East asynchronous work; 7-9 hr gap to US Pacific

### Cost-of-living for remote worker (Q1 2026)

- Studio short-let Chișinău Centru: €350–€700/month
- 1-bed apt long-term: €300–€600/month outside prime
- Single-meal mid-range: €5–€15
- Monthly transport: €5–€15

### Tax position

- **PIT 12% flat** if MD tax resident (183+ days)
- **MITP 7% unique tax** for IT professionals registering activity in the park (if eligibility met)
- Foreign-employer remote work: technically subject to MD PIT once tax-resident; double-tax treaty network covers most Western source countries

### Verdict for digital-nomad-first buyers

🟢 **Strong fit** for budget-conscious DNs prioritising cheap fast internet + low CoL + Schengen-adjacent + EU candidate trajectory. **Best fit**: Romanian-speaking DNs (passport adjacency), IT-sector DNs (MITP 7% incentive), Eastern-Europe-cycle nomads. **Friction**: no formal DN visa = either 90/180 churn or formal residence; thin MD-resident remote-employer infrastructure.

---

## Section: `--macro`

### Headline 2024–2026

- **GDP growth 2022**: −0.7% (war + energy shock)
- **GDP growth 2023**: +0.7% (BNS revised)
- **GDP growth 2024**: +2.5% (BNS preliminary)
- **GDP growth 2025**: +2.8–3.5% IMF Article IV / EBRD forecast range
- **GDP per capita 2024**: ~US$6,650 (World Bank)
- **Inflation 2025**: ~4.0–5.5% headline (BNM target 5%±1.5%)
- **Unemployment 2024 Q4**: ~3.0% (BNS) — low headline masks high informal-economy participation
- **Public debt / GDP**: ~35% (Ministerul Finanțelor) — moderate by regional standard
- **BNM policy rate Q1 2026**: 5.0% (verify current at bnm.md)

### Trend drivers (2024–2026)

- **EU accession negotiations** (Jun 2024) — material structural anchor; conditionality drives reforms 2024–2030
- **Constitutional reform Oct 2024** enshrined EU integration
- **Energy diversification post-2022**: Romania interconnector + EU LNG → reduced Gazprom dependency materially
- **Remittance economy**: ~12–14% of GDP (Bessarabian diaspora in Romania, Italy, Russia, Israel, Germany)
- **Russia-Ukraine war proximity**: ongoing political-risk premium; partially offset by EU support (Macro-Financial Assistance, EBRD, IMF EFF)

### IMF Article IV (latest)

[IMF 2024 Article IV (June 2024)](https://www.imf.org/en/Publications/CR/Issues/2024/06/24/Republic-of-Moldova-2024-Article-IV-Consultation-Press-Release-Staff-Report-and-Statement-by-the-550601) flags: war-spillover risk, energy-security transition, EU-conditionality reform pace, banking-sector consolidation, demographic decline (emigration). Property-market: subdued 2022–2023 trough; Chișinău recovery 2024 onward; structural EU-candidate discount narrowing slowly.

---

## Section: `--demographics`

### Population structure (2024 BNS estimate, **excluding Transnistria**)

- **Total**: ~2.50 million (vs ~2.99M in 1989 census peak — material decline)
- **Median age 2024**: ~38.6 years (rising)
- **Age 0–14**: ~17%
- **Age 15–64**: ~67%
- **Age 65+**: ~16% (rising — projected ~24% by 2050 per BNS projections)
- **Total fertility rate 2024**: ~1.8 (BNS)
- **Net migration**: persistently negative since 1991; ~–10k to –30k/yr typical (post-2022 mixed: emigration to EU + return migration of some Moldovan-Romanian dual citizens)
- **Diaspora**: ~1.0–1.2M Moldovans living abroad (Romania, Italy, Russia, Israel, Germany) — material remittance base

### Geographic distribution

- Chișinău municipality: ~660k (26.4% of population)
- Bălți municipality: ~150k (6.0%)
- Other urban: ~600k (24%)
- Rural: ~1.09M (43.6%)
- UTA Găgăuzia: ~155k

### Households

- ~1.0M domestic households (2024 BNS)
- Average household size: 2.6 persons (declining)
- Owner-occupier rate: **~93–95%** (legacy of post-Soviet apartment privatisation)
- Renter market thin outside Chișinău

### Implication for property

- **Demand floor 2025–2030**: emigration + ageing depress secondary-city demand; Chișinău relative resilience driven by capital-city function + diaspora-return purchases
- **Supply pipeline**: Chișinău new-build pipeline thin; pre-1990 panelka stock dominant resale segment
- **Discount opportunity**: secondary-city resale (Bălți, Cahul, Orhei) priced at material discount to Chișinău; rural village houses widely available <€20k but with severe utility + amenity constraints

---

## Section: `--esg`

### Climate-transition exposure

- **Climate Adaptation Strategy 2030** (Government Decision approved 2023; verify current at mediu.gov.md)
- **NDC under Paris Agreement**: 70% reduction in GHG by 2030 vs 1990 base (Updated NDC submitted 2020) — policy frameworks aligning with EU
- **Buildings sector**: ~40% of national CO₂; primary lever is heating-fuel switch + insulation retrofit
- **EPBD-aligned EPC mandatory** for new build + transfer (Law 128/2014 transposing EU EPBD); enforcement uneven on resale — request EPC and verify

### Property-level ESG considerations

- **Pre-1990 panelka stock**: typically EPC class **E–G**; major retrofit opportunity (insulation, window replacement, individual gas boiler) — €40–€120/m² typical retrofit budget for thermal-envelope upgrade
- **Heat-network connected (Termoelectrica)**: lower per-flat retrofit option (heat-network upgrades centrally) but higher tariff exposure to gas-price volatility
- **EU MFA-funded efficiency grants**: periodic Government + EU Energy Efficiency Fund schemes for HOA-led building retrofit (verify current at `https://www.fee.md/`)

### Climate-physical risk (cross-section to `--climate` + `--risks`)

- Drought stress in southern viticulture belt
- Vrancea seismic exposure for Chișinău pre-1990 panelka
- Prut/Nistru flood exposure for low-elevation parcels in border raioane
- Hotter Chișinău summers → cooling-load growth in stock built without AC provision

### Social / governance factors

- Owner-association governance (`asociație de coproprietari`) under Law 913/2000 — minority-protection mechanisms via court; HOA collective-action problem material in panelka stock
- Anti-corruption: Moldova's CNA (Centrul Național Anticorupție — `https://cna.md/`) materially strengthened post-2021 reform; ASP cadastre + notary chain considered substantially clean post-2018 e-services overhaul

### Verdict (ESG lens for typical Chișinău apt)

🟡 **Watch** — pre-1990 panelka stock represents the dominant retrofit-debt exposure; new-build (post-2014) materially better but priced higher; heat-network connection is a cost-vs-resilience tradeoff; EU candidate accession pressure will tighten EPBD enforcement 2026–2030.

---

## Section: `--exit`

### Resale market liquidity

- **Average days on market 2024**: ~60–150 days Chișinău mid-tier; 90–240 days Bălți / raional centres; rural village houses can sit 1–3+ years
- **Cyclical sensitivity**: Moldovan secondary market is **thin overall** — annual transactions nationally ~25–35k (BNS) vs ~3M registered immovables; turnover ratio < 1.5%/yr
- **2022 trough**: war shock + interest rate hike depressed transactions ~30% YoY; 2024 recovered to pre-war levels in Chișinău; secondary cities still subdued

### Exit-cost stack (seller side)

| Item | Cost |
|---|---|
| Estate agent commission | typically **2–4%** of sale price (often paid by seller; sometimes split) |
| Notary fee (seller side typically) | 0.1–1.5% of contract value (sliding) |
| **Capital gain on residential sale**: 50 % included in gross income, taxed at standard 12 % PIT under Art. 15 → ≈ 6 % effective on the gross gain (2026-05-27 verified, source PwC Tax Summaries Moldova). No separate CGT rate |
| **Primary-residence exemption**: dwelling **owned ≥ 3 years AND used as domicile for the 3 years up to sale** → fully non-taxable (Art. 20; **3 + 3 years, NOT 5**) |
| Mortgage early-discharge fee | typically 1–2% of outstanding balance, capped per loan agreement |
| Total exit cost | **typically 3–6 % of sale price** when primary-residence 3+3 exemption applies; 5–10 % for investment property where the 50 %-inclusion → 12 % PIT chain applies on the gain |

### Liquidity by sub-segment (qualitative, 2026)

| Segment | Liquidity | Notes |
|---|---|---|
| Chișinău Centru new-build (€1,200–€1,800/m²) | 🟡 selective | Diaspora-return + EU candidate uplift demand; 60–120 days typical |
| Chișinău outer sectors (Botanica, Ciocana, Râșcani) | 🟢 strong | Largest stock, perpetual buyer pool; 30–90 days typical |
| Chișinău Old Town heritage | 🟠 thin | Renovation restrictions + small buyer pool |
| Bălți + Cahul + Orhei mid-tier | 🟡 selective | Population decline; 90–240 days |
| Rural village houses | 🟠 niche | Diaspora-buy / hobby-property only; 1–3+ yr typical |
| Pre-1990 panelka without retrofit | 🟡 watch | EPC + retrofit-debt depressing pricing trajectory |

### Verdict for exit risk

🟡 for Chișinău mid-tier; 🟢 for in-demand outer-sector commuter stock; 🟠 for rural + secondary-city + heritage. **Pre-2022 buyers**: 2022 trough has materially recovered for Chișinău; full recovery elsewhere lagging. **EU accession trajectory** is the key 2026–2030 valuation tailwind; reverses materially if accession process stalls.

---

## Cost benchmarks (MD 2025–2026)

| Item | Cost (EUR or MDL, est.) |
|---|---:|
| ASP extract (standard) | ~€8–€16 (150–300 MDL) |
| ASP extract (urgent) | ~€26–€42 (500–800 MDL) |
| Notary fee (residential resale, sliding) | ~0.1–1.5% of value |
| State duty | 0.5–2% of value |
| Real-estate agent (paid by seller normally) | 2–4% |
| Translator (deed signing, foreign buyer) | €100–€300 |
| Building inspector (independent structural survey) | €200–€600 |
| Asbestos test (single sample) | €30–€80 |
| Radon test (3-month kit) | €40–€120 |
| Bare-shell ("la roșu") → finished apartment fit-out | €150–€350 / m² |
| Roof replacement (terracotta, 200 m²) | €5,000–€14,000 |
| Full apartment renovation (Chișinău mid-range, 80 m²) | €12,000–€30,000 |
| Septic to mains connection | €1,000–€4,000 |
| Annual property tax (Chișinău Centru, market €120k flat) | ~€60–€220 (cadastral × Local Council rate) |
| **Total transaction cost (buyer side, residential resale)** | **~1.5–3% of price** |

## Active fiscal incentives (2025–2026)

- **MITP Moldova IT Park** — 7% unique tax for qualifying IT residents (replaces CIT + PIT + social + property tax for IT activity)
- **Primary-residence CGT exemption** under Tax Code Art. 20: dwelling **owned ≥ 3 years AND used as domicile for the 3 years up to sale** is fully non-taxable (3 + 3, not the previously quoted 5-yr threshold; 2026-05-27 verified, source PwC). Outside the exemption: 50 %-inclusion → 12 % PIT → ≈ 6 % effective
- **Reduced 8% VAT** on residential dwellings sold by VAT-registered developer (Tax Code Art. 96 lit. b — verify scope)
- **Free Economic Zones** (Bălți, Cahul, Ungheni, Tvardița, Otaci, Vulcănești, Taraclia) — exemption from CIT, VAT, customs duty for in-zone activity
- **EU-supported energy-efficiency retrofit grants** via FEE (Fondul pentru Eficiență Energetică) — variable annual budget for HOA-led building retrofits

## Common listing platforms

- **999.md** (largest classifieds): `https://999.md/ro/real-estate` *(per listing — verify with cadastre / on visit)*
- **Makler.md**: `https://makler.md/` *(per listing — verify with cadastre / on visit)*
- **Lara.md** (English UI option): `https://lara.md/` *(per listing — verify with cadastre / on visit)*
- **Imobil.md**: `https://imobil.md/` *(per listing — verify with cadastre / on visit)*
- Facebook groups + Telegram channels (high volume; never authoritative)

## Caveats unique to MD

- **Foreigners CAN buy residential freehold without restriction** (since 2002 Civil Code) — among the most permissive in the region
- **Foreigners CANNOT own agricultural OR forest land** (new Land Code in force 1 April 2025, superseding Law 828-XII of 1991; 2026-05-27 verified). The new Code explicitly catches Moldovan SRLs with foreign capital (even minority) and triggers **mandatory 1-year divestment** on inherited / court-judgment / mortgage acquisitions; the Moldovan-citizen-co-owned SRL workaround is **more legally fragile** than under the old regime
- **Transnistria (Stânga Nistrului) — OUT OF SCOPE for normal DD**: separatist authorities issue parallel cadastral documents that the **Moldovan ASP does NOT recognise**. Properties physically east of the Dniester (Tiraspol, Bender, Râbnița, Slobozia, Camenca, Dubăsari, Grigoriopol) carry severe title-validity risk for any future EU-aligned property regime. **Moldovan banks generally do not finance Transnistria property.** Treat any listing in Stânga Nistrului as outside this skill's scope until UN/EU-recognised reintegration occurs
- **EU candidate (Jun 2022) + accession negotiations open (Jun 2024)** — material structural tailwind 2024–2030
- **2014 banking-crisis legacy**: BNM tightly supervises sector post-2014 "Theft of the Century"; current concentration in Maib + MICB + OTP + Victoriabank
- **Currency**: most listings priced in **EUR** but contracts denominated in **MDL** at BNM reference rate on signing day — exchange-rate exposure 2–3 weeks pre-signing
- **Soviet-era panelka** (1955–1991): asbestos + uneven seismic retrofit; pre-1990 stock dominant in Chișinău + Bălți; commission independent structural survey
- **Self-built (pre-2007) legalisation history**: 2007 + 2014 amnesties; verify ASP recordation matches building footprint
- **Notarised contract MANDATORY** (Civil Code Art. 213) — no DIY conveyancing
- **AML cash limit MDL 100,000** per transaction (Law 308/2017); bank-wire standard above
- **Romanian-citizenship adjacency**: large eligible pool gives full EU passport access — material exit-optionality factor for property holders
- **Russia-Ukraine war proximity** (since Feb 2022): tail political-risk premium; insurance loading; cash-purchase prevalence
- **Energy supply post-2022 reform**: gas + electricity diversified away from Russia/Transnistria; tariff volatility 2025–2027 expected as transition completes
- **No active CBI 2026** (programme ended 2018, formally repealed 2020) — beware historical references to "Moldovan citizenship by investment" in older sources

## Reddit / forum sources

- **r/moldova** — general (mixed quality on property; Romanian + English)
- **r/Chisinau** — city-specific, smaller but active
- **r/moldovaIT** — IT/MITP discussion, includes remote-worker housing
- Facebook: "Imobile Chișinău", "Chișinău Apartamente de Vânzare", "Expats in Chișinău", "Moldova Property"
- Telegram: `t.me/imobilchisinau` (high volume; classifieds; never authoritative)
- Diaspora forums: "Moldoveni în Italia", "Moldoveni în Romania" — material because diaspora-return is a non-trivial buyer segment
- Lara.md blog + Makler.md analytics — local market commentary

## Verification authorities

| Authority | When to call / visit |
|---|---|
| **ASP (Agenția Servicii Publice)** | Title extract, encumbrances, cadastral verification — any ASP territorial office |
| **Cadastrul Bunurilor Imobile geoportal** | Public parcel viewer (free first cross-check before paid extract) |
| **SFS (Serviciul Fiscal de Stat) — fisc.md** | Tax residency, contract registration, VAT registration |
| **IGM (Inspectoratul General pentru Migrație)** | Residence permit, investor visa Law 200/2010 |
| **BNM (Banca Națională a Moldovei)** | Reference exchange rate, bank supervisory list |
| **CNPF** | Insurance company supervisory list |
| **Camera Notarială** | Notary register, complaints, tariff |
| **Ministerul Culturii** | Heritage-listed building check |
| **Local Council (Consiliul Local / Primăria)** | Local property-tax rates, zoning, building permits |
| **ApăCanal Chișinău / Moldova-Apă-Canal / regional ops** | Mains water + sewer connection verification |
| **Premier Energy / RED-Nord (electricity), Moldovagaz (gas), Termoelectrica (DH)** | Utility connection + tariff |
| **SHS (Serviciul Hidrometeorologic de Stat)** | Flood + climate baseline data |
| **IGS (Institutul de Geologie și Seismologie)** | Seismic + landslide hazard data |
| **IGSU (Inspectoratul General pentru Situații de Urgență)** | Emergency response, hazard maps |
| **CNA (Centrul Național Anticorupție)** | If anomaly suspected in cadastre or notary chain |

## Quirks to know

- **Cadastral number format `XXXX XXX XXX XX`** (locality.zone.block.parcel) — every property has one; ask for it before any other paperwork
- **Romanian + Russian bilingual context**: Russian still widely used in business + older notaries; verify deed language preference; certified translation cheap and standard
- **"Italian courtyard" / "casă în interior"**: traditional Chișinău Old Town courtyard houses; charming but typically pre-1940, weak seismic performance, complex shared-wall + access rights
- **Heat-network "termoficare" connection**: Chișinău ~80% panelka stock connected to Termoelectrica; tariff exposure to gas-price volatility; individual gas boilers ("centrală autonomă") increasingly retrofitted — preference depends on price scenario
- **VAT trap on new-build**: confirm "TVA inclus" vs "TVA neinclus"; 8% reduced rate qualifying scope is narrow — verify
- **Romanian citizenship pathway**: large eligible pool; ~700k+ Moldovans estimated to hold dual MD+RO citizenship; material for exit + mobility planning
- **Transnistria zone**: any address east of the Dniester (Stânga Nistrului) — treat as out-of-scope for ASP-validated DD until reintegration
- **Diaspora-buy pattern**: many pre-1990 panelka apartments held by emigrant owners (Italy, Russia, Israel) and managed by local relatives — verify owner is signing personally OR via apostilled PoA
- **2014 banking-crisis discount**: certain pre-2015 mortgage-collateral properties may have residual title-chain complexity from BC/BS/Unibank resolution — verify carefully via ASP

## Source URL templates

| Source | URL pattern |
|---|---|
| ASP cadastre | `https://cadastru.md/` |
| Cadastrul Bunurilor Imobile geoportal | `https://www.asp.gov.md/en` |
| IPCBI — Instituția Publică Cadastrul Bunurilor Imobile (cadastre authority; e-Cadastru portal) | `https://www.ipcbi.gov.md/ro` — portal `https://www.cadastru.md/ecadastru/f?p=100:1::::::` (⚠️ `cadastru.md` geo-blocks non-Moldovan IPs) · online ordering via ASP e-services `https://eservicii.gov.md/asp/cadastru/cerere` |
| SFS Tax Service | `https://www.fisc.md/` |
| IGM — migration authority | `https://igm.gov.md/` |
| BNM National Bank | `https://www.bnm.md/` |
| BNM exchange rates | `https://www.bnm.md/en/content/official-exchange-rates` |
| BNS Statistics | `https://statistica.gov.md/` |
| CNPF Financial Markets | `https://www.cnpf.md/` |
| Notarial Chamber | `https://cnm.md/lista-notarilor/` |
| ANRE Energy Regulator | `https://www.anre.md/` |
| ApăCanal Chișinău | `https://acc.md/` |
| Termoelectrica | `https://termoelectrica.md/` |
| Moldovagaz | `https://www.moldovagaz.md/` |
| Premier Energy | `https://premierenergy.md/` |
| ANTRIM Investment Agency | `https://invest.gov.md/` |
| MITP Moldova IT Park | `https://moldovaitpark.md/` |
| 999.md classifieds | `https://999.md/ro/real-estate` |
| Makler.md | `https://makler.md/` |
| Lara.md (EN) | `https://lara.md/` |
| State Roads Authority | `https://asd.md/` |
| Hydromet Service | `https://www.meteo.md/` |
| IGSU emergency | `https://www.igsu.gov.md/` |
| Geology + Seismology | `https://igs.asm.md/` |
| Ministry of Environment | `https://mediu.gov.md/` |
| Ministry of Culture (heritage) | `https://mc.gov.md/` |
| IGP Police statistics | `https://politia.md/` |
| Anti-Corruption Centre | `https://cna.md/` |
| Energy Efficiency Fund | `https://www.fee.md/` |
| Chișinău Municipality | `https://www.chisinau.md/` |

## Status

**Confidence**: MEDIUM — HIGH on foundational legal/fiscal framework (new Land Code in force 1 April 2025 superseding Law 828-XII of 1991 with 1-yr divestment trigger for inheritance/court/mortgage acquisitions; CGT mechanic = 50% capital-gain inclusion in gross income (eff. 1 Jan 2020, pre-2020 was 20%) → taxed at standard 12% PIT under Art. 15 → ≈ 6% effective on gross gain; primary-residence exemption 3 yrs owned + 3 yrs domicile (NOT 5 yrs); 0.8% wealth tax on high-value residential under Tax Code Title VI¹ since 2016 — threshold both value ≥ 200 × average forecast monthly wage AND floor area ≥ 120 m², 1 November snapshot, due 25 December; January 2027 cadastral revaluation projected ~150–190% effective property-tax bill uplift). MEDIUM on property-tax statutory range upper bound (0.05–0.3% vs 0.05–0.4% vs 0.05–0.8% — weak sourcing on top of band; verify at fisc.md), SRL workaround legal fragility under new Land Code (foreign-capital SRL treatment evolving), and rental 7% monthly self-pay vs tenant withholding mechanic. LOW on listing-platform 999.md current price granularity (verify with attorney + cadastre per deal).

**Last verified**: 2026-05-27

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: Primary sources verified — ASP cadastre + Tax Code Art. 15/18/20/96/280-281 + Title VI¹ (effective ≈ 6 % on residential gains via 50 %-inclusion → 12 % PIT, **primary-residence exemption 3 yrs owned + 3 yrs domicile** per PwC 2026-01-14, VAT 8 % reduced + 20 % standard, property-tax 0.05–0.4 % bands, **0.8 % wealth tax on residential ≥ 120 m² AND ≥ 200× avg wage value** since 2016), Civil Code Art. 213 (mandatory notary), **new Land Code in force 1 April 2025 (superseding Law 828-XII of 1991)** retaining foreign ag/forest-land ban + 1-yr divestment trigger, Law 200/2010 Art. 50 (€250k investor residence), CBI ENDED 2018 (formally repealed Law 100/2020), MITP 7% unique tax (Law 77/2016), BNM exchange-rate regime, EU candidate status (23 Jun 2022) + accession opened (25 Jun 2024) + Constitutional reform Oct 2024. **January 2027 cadastral revaluation projected to raise effective property-tax bills ~150–190 %** (2026-05-27 verified, source EuropaLibera Moldova). **Transnistria (Stânga Nistrului) explicitly OUT OF SCOPE**: properties east of the Dniester carry parallel-cadastre title-validity risk; Moldovan ASP does not register, Moldovan banks generally do not finance, and any future EU-aligned regime treatment is uncertain — flagged in Caveats and Country profile. **Re-verify each annual budget law (November)** for Tax Code amendments, Local Council property-tax rates (each Decizia CMC December), ANRE tariff adjustments, BNM policy rate. **Watch list 2026**: any reintroduction of CBI (politically unlikely given EU conditionality), MITP rate changes, CGT primary-residence threshold tweaks, accession-driven tax/AML harmonisation milestones, Romanian-citizenship-by-descent procedural changes (RO law side).

## Extension TODOs (deepen on first real run)

- [ ] Per-Chișinău-sector property-tax coefficient extraction (Decizia CMC per year, all 5 sectors)
- [ ] ASP cadastral-value vs market-value calibration database (60% baseline currently inferred from BNM commentary; verify per-segment)
- [ ] EPC enforcement-rate audit (Law 128/2014 transposition — request data from Agenția pentru Eficiență Energetică)
- [ ] FEE (Fondul pentru Eficiență Energetică) HOA-grant cycle tracker
- [ ] Romanian-citizenship pathway procedural detail (RO ANC processing time + document requirements)
- [ ] BNM mortgage rate + LTV time-series automation
- [ ] Diaspora-buyer due diligence checklist (apostilled PoA + remote-signing workflow)
- [ ] Transnistria-zone parcel-flag automation (cadastral-number locality codes east of Dniester)
- [ ] Heritage-listed building cadastral-code lookup workflow (Ministerul Culturii register)
- [ ] Free Economic Zone tax-incentive eligibility checklist (per zone: Bălți, Cahul, Ungheni, etc.)
