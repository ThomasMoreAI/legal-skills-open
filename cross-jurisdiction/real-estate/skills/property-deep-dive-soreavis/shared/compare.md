# Universal `--compare` Mode

Side-by-side multi-country comparison for relocation, investment, and "where should I move/buy?" decisions. Leverages all 87 country playbooks at once.

**Snapshot**: May 2026 (Tier-5 additions).

## When to use

Trigger `--compare` when the user is **not committing to a single address** but instead asking:
- "Where should I move from FR?" — compare candidate countries
- "Spain or Portugal for golden-visa replacement?" — compare 2-5 countries head-to-head
- "Cheapest entry market in EU for €200k?" — compare on a metric
- "Where can I retire on €2,500/mo?" — compare with `--retirement` overlay

## Invocation

```
/property-deep-dive --compare=es,pt,it [--criteria=<list>] [--journey=<type>] [--budget=<amount>]
/property-deep-dive --compare=eu --top=10 --criteria=tax,price,visa
/property-deep-dive --compare --rank=tax-friendly --rank=climate-stable
```

## Universal contract

For each country in the comparison set, return:
1. **One row per country** with the requested criteria
2. **Highlighted leaders/laggards** per criterion (best 🟢 / worst 🔴)
3. **Overall verdict per user-stated objective**
4. **Ranked shortlist** (top 3 by composite score)
5. **Anti-hallucination disclaimer**: comparison is structural, not predictive

## Output template

```markdown
## Multi-Country Comparison

**Comparison set**: <ISO2 list>
**Criteria**: <list>
**Date**: <YYYY-MM-DD>

### Headline metrics

| Metric | <C1> | <C2> | <C3> | … |
|---|---|---|---|---|
| Capital city €/m² (segment-typical) | … | … | … | … |
| Annual property tax (% / formula) | … | … | … | … |
| Transfer tax / acquisition cost | … | … | … | … |
| CGT regime | … | … | … | … |
| Foreign-buyer access | … | … | … | … |
| Mortgage LTV (non-resident) | … | … | … | … |
| Currency / FX volatility | … | … | … | … |
| Visa pathway (RBI/CBI status) | … | … | … | … |
| Climate trajectory (RCP4.5 to 2050) | … | … | … | … |
| Notary / closing-cost % | … | … | … | … |
| Time offer→deed (days) | … | … | … | … |

### Per-criterion leader

| Criterion | Best | Worst |
|---|---|---|
| Lowest acquisition cost | <C> | <C> |
| Lowest annual carry | <C> | <C> |
| Strongest CGT exemption | <C> | <C> |
| Most foreign-buyer-friendly | <C> | <C> |
| Most stable currency | <C> | <C> |
| Most accessible visa | <C> | <C> |
| Best climate (cooler / less drought / less wildfire) | <C> | <C> |
| Fastest closing | <C> | <C> |

### Composite ranking

🥇 1. <C> — <one-line rationale>
🥈 2. <C> — <one-line rationale>
🥉 3. <C> — <one-line rationale>

### Decision-context overlay

<if --journey=retiree, --journey=foreign-buyer, --journey=investor — apply that filter>

### Confidence
<HIGH | MEDIUM | LOW> — <one-sentence justification>
```

## Available criteria flags

| Flag | What it pulls |
|---|---|
| `--criteria=tax` | Annual + transfer + CGT + rental income tax + VAT |
| `--criteria=price` | Capital + secondary city €/m², HPI YoY |
| `--criteria=visa` | RBI/CBI status, property thresholds, language requirement |
| `--criteria=finance` | LTV non-resident, 10-yr fixed rate, FX-loan rules |
| `--criteria=climate` | Temperature trajectory, sea-level rise, drought, wildfire risk |
| `--criteria=foreign-buyer` | Restrictions, permits, surcharges, RU/BY rules |
| `--criteria=str` | Short-term rental regime, registration, taxes |
| `--criteria=closing` | Notary requirement, closing cost %, days offer→deed |
| `--criteria=insurance` | Cat-risk scheme, mortgage-mandatory, premium % |
| `--criteria=process` | Cadastre access, foreigner-self-serve, language requirement |
| `--criteria=cost-of-living` | Net-of-tax, working-age-profile, **country-level** living-cost position (OECD Taxing Wages ÷ Eurostat PLI / World Bank ICP) — city-vs-home capped to US BEA RPP; sourcing + the hard city-level cap in `shared/macro.md` § Cost-of-living |
| `--criteria=all` | All of the above |

## Comparison set shortcuts

| Shortcut | Resolves to |
|---|---|
| `eu` | All 27 EU members in skill |
| `eea` | EU + IS, NO, LI |
| `eurozone` | All 21 eurozone members |
| `western-balkans` | RS, ME, BA, MK, AL |
| `latam` | MX, BR, AR, CR, PA, DO, CO, UY, CL, PE, EC, PY |
| `anglo-non-eu` | CA, AU, NZ, US |
| `mediterranean` | ES, PT, IT, GR, CY, MT, FR, HR, SI, MA, IL, EG, TR, TN |
| `nordic` | SE, FI, NO, DK, IS |
| `dach` | DE, AT, CH |
| `gcc-mena` | AE, IL, MA, EG, TR, QA, SA, TN, JO, OM, BH, KW, LB |
| `gulf-cooperation-council` | AE, QA, SA, OM, BH, KW (skill-supported GCC; all 6 GCC members covered) |
| `southeast-asia` | TH, ID, MY, VN, PH, JP |
| `east-asia` | JP, KR, TW, HK, MO, SG |
| `south-asia` | IN |
| `microstates` | LI, MC, AD, MT, MO, SG (city-state), BH (city-state) |
| `caucasus` | GE, AM, AZ |
| `caucasus-eu-adjacent` | GE, TR, AM, AZ |
| `north-africa` | MA, EG, TN |
| `levant` | IL, JO, LB |
| `sub-saharan-africa` | NG, KE, ZA |
| `east-africa` | KE |
| `west-africa` | NG |
| `andean` | CO, EC, PE, CL |
| `southern-cone` | AR, UY, CL, PY |
| `eu-candidate` | MD, ME, RS, BA, MK, AL (Western Balkans + Moldova) |
| `top-10-foreign-buyer-friendly` | precomputed list (see below) |

## Precomputed verdict shortcuts (Apr 2026 snapshot)

These are computed from the per-country playbooks and refreshed on `--update`. They are commentary, not authoritative — use as a starting point.

### Most foreign-buyer-friendly (no AIP/permit beyond standard)
1. PT (open, NIF only)
2. ES (open, NIE only)
3. LU (no nationality restriction, same 7%)
4. IT (Codice Fiscale only)
5. FR (no permit, simple notarial)
6. GE (open, registration <1 day, no permit)
7. US (open, ITIN/SSN only; FIRPTA on resale)
8. TR (open subject to reciprocity + military-zone clearance)
9. KR (open to most foreigners; Foreigner's Land Acquisition Act notification only)
10. TW (open subject to reciprocity per BOCA list — verify nationality eligibility)
11. MD (open, foreigners can own buildings + non-agricultural land freely)
12. AM (open to foreigners; equal property rights for non-citizens per Land Code Art. 4 — exceptions on agricultural and protected land)
13. AZ (open subject to TRP / Strategic Investor Visa; agricultural and border-zone restricted)
14. PY (open; foreigners equal rights for urban land; some border-zone restrictions per Ley 2532/2005 within 50km of borders)
15. LB (open to most foreigners; ≤3,000 m² aggregate Beirut / ≤10,000 m² aggregate Mount Lebanon / ≤coastal limits; Council-of-Ministers approval for >limits; Lebanese-descent buyers exempt)
16. KE (open to foreigners; freehold for residential — but **agricultural land restricted to citizens** per Constitution Art. 65; 99-yr leasehold cap on non-citizen freehold-equivalents)

### Highest acquisition friction (permit / restriction-heavy)
1. CA (foreign-buyer ban through 1 Jan 2027)
2. AU (established-homes ban 1 Apr 2025–31 Mar 2027)
3. NZ (most existing homes banned since 2018)
4. TH (no land freehold for foreigners; condo 49% quota)
5. PH (no land for foreigners; condo 40% quota)
6. VN (no land; 50-yr leasehold + 30%-per-building / 250-houses-per-ward quotas — 2024 Land Law)
7. ID (no Hak Milik freehold for foreigners; Hak Pakai leasehold only)
8. CH (Lex Koller cantonal permit)
9. DK (non-EU + 5y residence requirement)
10. AE (foreign ownership restricted to designated freehold zones)
11. EG (max 2 properties × 4,000 m² total; Sinai/Suez excluded)
12. SG (foreign Restricted Residential Property Act — foreigners barred from landed homes; condo-style strata only without SLA approval; ABSD 60% non-resident)
13. HK (open but **BSD 15% + AVD up to 4.25%** non-PR surcharges; verified via IRD post-2024 cooling-measure rollback partial — verify per IRD)
14. MO (open but post-2007 Investment Residence suspended — no residence pathway via property; foreign buyer pool thin)
15. LI (Lex Koller-equivalent + EEA-only freehold; quota residency limits buyer pool)
16. MC (open but Sûreté Publique residence verification + €500k bank deposit gates qualifying buyer pool)
17. AD (open since 2012 reform; foreigners must register at Govern d'Andorra; **STR Llei 26/2024 + parish quotas** narrow short-let economics)
18. TW (reciprocity-list-based; nationality determines eligibility — verify BOCA list)
19. SA (Mecca/Medina constitutional Muslim-only ownership; Real-Estate-Owner Premium Residency requires SAR 4M; verify with Premium Residency Center / Real Estate General Authority)
20. QA (foreigners limited to designated freehold zones — Pearl-Qatar / West Bay Lagoon / Lusail; rest leasehold; verify with MoJ Real Estate Registration)
21. PE (border 50km Andean restriction per Constitution Art. 71 — foreigners need Supreme Decree authorization for border zones)
22. EC (open generally but **2024 Internal Armed Conflict Declaration** requires extra title-due-diligence in conflict-affected provinces — Guayaquil/Esmeraldas/Manta)
23. TN (open via Investor Residence Permit ≥TND 1M; Office des Changes documentation required for FX import — see MA-style repatriation friction)
24. IN (foreign-buyer ban for non-NRI/non-OCI residential — Foreign Exchange Management Regulations 2018 Sch.I; **NRIs + OCIs only**, no residential land for non-Indian-origin foreign nationals; agricultural / plantation / farmhouse land barred even for NRIs/OCIs)
25. NG (open to foreigners but **Land Use Act 1978 — all land vested in state Governor** — only Statutory Right of Occupancy 99-yr leasehold for foreign / non-citizen buyers; Governor's consent required for transfers; security risk requires private security + gated communities)
26. JO (open to foreigners subject to **Council-of-Ministers approval** for properties >Greater Amman threshold; ≤4,000 m² agricultural barred; reciprocity required for some nationalities — verify Jordan Department of Lands and Survey)
27. OM (foreigners limited to **Integrated Tourism Complexes (ITC)** designated zones — Royal Decree 12/2006 / 89/2021; rest barred or leasehold-only; Mecca/Medina-equivalent restrictions on certain national-heritage zones)
28. BH (open to foreigners in **designated freehold zones** — Diyar Al Muharraq / Amwaj Islands / Durrat Al Bahrain / Reef Island / Bahrain Bay / Seef / Manama Diplomatic Area; rest barred without Royal Decree)
29. KW (**foreigners CANNOT own real estate freehold** — only via 5-yr leasehold via Iqama-employer-sponsored arrangements; Decree-Law 74/1979 / 8/2008 amendments; among the most restrictive globally)

### Lowest acquisition cost (% of price)
1. GE (~0.1-0.5% — lowest tracked globally; Public Service Hall registration GEL 50-200)
2. EE (~1-2% no transfer tax)
3. LT (~1-1.5% no transfer tax)
4. CZ (~2-4% transfer tax abolished 2020)
5. SK (~2-4% no transfer tax since 2005)
6. NO (~3-4% dokumentavgift 2.5%)
7. CL (~3-4% notarial + Conservador de Bienes Raíces)
8. VN (~3-5% registration + notary)
9. US (~3-6% varies by state — CA escrow vs NY mansion-tax extremes)
10. MD (~2-4% — 1% notary + 0.5% State Registration Chamber + agent + ~5% only on > 500k MDL register-value transactions; verify CCRF)
11. AD (~3-5% — ITP 4% + notari + Govern registration; STR-zoned higher)
12. PY (~3-5% — ITBI ~1.5% + notarial + State Registration; among lowest LatAm)
13. AM (~3-5% — State Registry + notary + agent; lower than RU/EU)

### Highest acquisition cost (% of price)
1. ID (~17-19% combined BPHTB 5% + PPh 2.5% + PPN 11% on new-build via PMA)
2. BE (~12-17% Brussels/Wallonia)
3. ES (~10-13% existing)
4. PH (~10% — CGT 6% gross + DST 1.5% + transfer + LTT)
5. IL (~6-10% Mas Rechisha tiered + non-resident surcharge)
6. AT (~10-12%)
7. GR (~10-12%; watch — ANNOUNCED, NOT LEGISLATED (90th TIF, Sep 2026): FMA 3.09% → 15.45% for non-EU/EEA natural-person home buyers who are not ομογενείς or long-term residents, intended from 1 Jul 2027 — see GR playbook)
8. UK (~10-15% with SDLT non-res surcharge)
9. UY (~7-9%)
10. ZA (~7-9% transfer duty tiered)
11. DO (~7-8% — 3% transfer + 1% IPI + notary + registry)
12. AE (~6-8% — DLD 4% + agent + NOC + housing-fee 5% annual)
13. TR (~6-8% — 4% tapu + notary + agent)
14. JP (~6-7% — registration + acquisition tax + agent up to 3% + 6万円)
15. SG (BSD 1-6% + ABSD 60% non-resident + agent + legal — non-resident total can reach **65-70%+** vs ~3-7% citizen)
16. HK (AVD up to 4.25% + BSD 15% non-PR + Special Stamp Duty if <3 yrs — non-PR surcharges material; partial cooling-measure rollback Oct 2023-2024 — verify IRD)
17. KR (~6-8% — acquisition tax 1-3% sliding by price + 0.2% local + agent ~0.4-0.9% + reg fee 0.6-1.5%)
18. TW (~6-8% — deed tax 6% + agent 1-2% + reg + Land Value Increment Tax buyer-side rare)
19. MC (~10-12% — 4.5% droits d'enregistrement + notary 1.5% + agent 3% + 20% TVA on agent fee — verify Direction des Services Fiscaux)
20. LI (~5-7% — Handänderungssteuer ~2% + commune + Grundbuchamt registration; CH-aligned)
21. QA (~6-9% — ~0.25% transfer + notary + agent + freehold-zone-only restriction + verify with MoJ Real Estate Registration)
22. SA (~5-8% — 5% transfer tax (Real Estate Disposal Tax / RETT 5%) + notary + agent; Premium Residency real-estate-owner SAR 4M minimum)
23. TN (~10-15% — 5% droits d'enregistrement + 1% conservation foncière + agent + Office des Changes friction; non-resident slightly higher)
24. EC (~7-10% — alcabala 1% + registry + notary + agent + IVA 15% on services where applicable)
25. PE (~7-10% — alcabala 3% + notary + Registros Públicos + agent)

### Lowest annual carry (no/minimal annual property tax)
1. MT (no annual property tax)
2. AE (no annual property tax; only 5% housing fee on rentals via DEWA)
3. VN (no recurring residential property tax — non-agri land-use fee only)
4. CY (national IPT abolished 2017; municipal small)
5. LU (impôt foncier near-trivial currently — reform 2030)
6. GE (income-gated annual tax — 1% only above GEL 40k household income threshold)
7. IE (LPT modest, 0.0906% base rate)
8. LT (NTM from 2026: main dwelling exempt up to a municipal threshold of at least €450k / other non-commercial property 0% up to €50k total value, then 0.2–1% marginal bands — 2026 data, source VMI)
9. DO (1% IPI only on portion above DOP 9.86M, ~USD 165k)
10. MC (no annual property tax for owner-occupiers; small registration fees only)
11. MO (no annual property tax for residential; rental income subject to Property Tax 6-10% on rental net only)
12. SG (Property Tax 0-32% progressive on Annual Value, owner-occupied 0-23% — modest effective % vs price for owner-occupiers; non-residential and investment higher)
13. QA (no annual property tax for residential owner-occupiers; service charges per Pearl/Lusail master-plan only; verify with MME / MoJ)
14. SA (no annual property tax for owner-occupiers; **White Land + Vacant Property Fees up to 10%/yr, banded 10/7.5/5/2.5/nil by urban-development priority zone, on undeveloped urban plots ≥5,000 m²** (Royal Decree M/4 1437 AH as amended 2025; executive regulation 22 Aug 2025))
15. PY (very low annual immobiliario; flat ~1% on register-value but register-value typically ~10-30% market — effective <0.3%)
16. AM (low annual property tax — sliding 0-1% on cadastre value, exempt under AMD 3M threshold; verify SRC)

### Highest annual carry
1. FR (taxe foncière + redevance audiovisuelle, dependent on commune)
2. UK (council tax bands)
3. US (state-by-state; 0.5-2.5%, NJ/NH/IL on the heavy end, HI/AL on the light)
4. JP (1.4% kotei-shisan-zei + 0.3% toshi-keikaku-zei on assessed value)
5. ZA (Municipal Rates 0.6-1% — Cape Town/Joburg)
6. CH (cantonal Eigenmietwert until 2028 + cantonal property tax)
7. DK (boligskat 2024-reform unified ejendomsværdiskat + grundskyld)
8. UY (Contribución Inmobiliaria 0.25-1.4% + ITP 2% on transactions)
9. CL (Contribuciones ~0.98% above UF 49.5M exemption)
10. KR (재산세 jaesanse 0.1-0.4% + comprehensive real estate tax 종부세 0.5-5% on multi-home owners — among most progressive regimes globally; verify NTS)
11. TW (House Tax 1.5-3.6% by use + Land Value Tax 1-5.5% — verify County Government)
12. HK (Rates ~5% on Rateable Value urban + Property Tax 15% on rental income for owners)

### Most stable currency / lowest FX risk for €-buyers
1. **Eurozone** (21 countries — no FX risk)
2. BG (just joined 1 Jan 2026)
3. HR (joined 2023)
4. DK (DKK ERM-II ±2.25%)
5. BA (currency board 1.95583)
6. **MC** (EUR via Monetary Treaty — no FX risk)
7. **AD** (EUR via Monetary Treaty 2011 — no FX risk; not Eurozone-member)
8. **LI** (CHF currency union with CH — stable but EUR-CHF cycle exposure)
9. **HK** (HKD pegged to USD via LERS 7.75-7.85, HKMA Convertibility Undertaking — stable vs USD; EUR-HKD exposure via USD/EUR)
10. **MO** (MOP-HKD-USD double peg — same USD/EUR exposure layered through HKD)
11. **SG** (SGD MAS-managed-float against undisclosed basket — among the most stable EM currencies; modest EUR/SGD volatility)
12. **QA** (QAR pegged to USD 3.64 since Jul 2001 — stable vs USD; EUR-buyer carries USD/EUR risk)
13. **SA** (SAR pegged to USD 3.75 since Jun 1986 — stable vs USD; EUR-buyer carries USD/EUR risk)
14. **OM** (OMR pegged to USD 0.385 / USD = OMR 0.385 since 1986 — stable vs USD; EUR-buyer carries USD/EUR risk)
15. **BH** (BHD pegged to USD 0.376 since 1980 — stable vs USD; EUR-buyer carries USD/EUR risk)
16. **JO** (JOD pegged to USD 0.708 since Oct 1995 — stable vs USD; EUR-buyer carries USD/EUR risk)

### Highest FX risk for €-buyers
1. AR (managed band 1,000–1,400 ARS/USD; capital controls history)
2. EG (EGP devaluation cycles; March 2024 float halved value vs USD; Form 4 repatriation gate)
3. TR (TRY chronic high inflation; 2021-2025 cumulative loss vs EUR >70%)
4. UY (USD-parallel pricing for property — UYU not used at scale; FX exposure is USD/EUR)
5. ZA (ZAR EM-volatility; load-shedding-correlated swings)
6. CL (UF-indexed property contracts mute FX risk *internally* but UF→EUR conversion still volatile)
7. HU (HUF most volatile EU currency)
8. IS (small market, 10%+ annual range typical)
9. UK (GBP political-uncertainty premium)
10. CH (CHF safe-haven appreciation 2024-26 — actually a *gain* for buyers but unhedged exit risk)
11. AE (AED pegged to USD 3.6725 — stable vs USD, but EUR-buyers carry USD/EUR risk)
12. KR (KRW free-float; USD/KRW range 1,200-1,450 typical 2023-2026; EUR exposure layered)
13. TW (TWD managed-float CBC; USD/TWD ~30-33 typical 2023-2026)
14. MD (MDL float, NBM-managed; gradual depreciation trend; one of the smaller emerging-market currencies in Europe)
15. PE (PEN BCRP-managed float; USD-correlated economy; USD-pricing common in Lima Miraflores prime — FX exposure US/EUR layered through USD)
16. EC (USD-dollarized since 2000 — no native currency; FX risk = USD/EUR for European buyers; political-economy risk overlaid via 2024 Internal Armed Conflict Declaration)
17. PY (PYG BCP-managed float; relatively stable but small-market liquidity; USD widely accepted in Asunción)
18. AM (AMD CBA-managed; **strong appreciation 2022-23 from Russian-relocant capital inflow ~50% peak**; reversion risk material)
19. AZ (AZN CBA-managed peg-to-USD effective; oil-revenue stabilized via SOFAZ sovereign fund; modest but present FX risk)
20. TN (TND BCT-managed float; gradual depreciation 2014-2024; **IMF EFF program SUSPENDED Mar 2024** is structural FX overhang)
21. **IN** (INR RBI-managed float; gradual depreciation 70-90 INR/USD 2020-2026; **LRS USD 250k/yr cap on outbound remittance**; NRO/NRE bank-account split material; Tier-1 metro USD-pricing common foreign-buyer)
22. **NG** (NGN devaluation cycle 2023-24 catastrophic — ~70% loss vs USD post-Tinubu reforms; managed-float regime evolving; Form A documentation for FX repatriation; oil-revenue dependent)
23. **KE** (KES BCK-managed float; relatively stable but small-market liquidity; M-PESA mobile-money rails reduce some FX friction; modest depreciation 2020-2026)
24. **KW** (KWD highest-valued currency globally — pegged to undisclosed basket weighted toward USD by CBK; among the most stable EM currencies; KWD 0.30-0.31/USD typical)
25. **LB** (**LBP catastrophic collapse 2019-2026** — official rate vs Sayrafa rate vs parallel rate triple-tier; banking-sector restrictions on USD withdrawals + transfers; **post-2019 banking collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war** structural overhang; **dual-pricing USD ↔ LBP** in property contracts)

### Most golden-visa-friendly (Apr 2026, post-ES/IE/MT closures)
1. GR (€800k/€400k tiers, property-linked)
2. AE Golden Visa (AED 2M / ~USD 545k property — 10-year, renewable)
3. TR CBI (USD 400k property — citizenship, retain 3y)
4. GE Investor Residency (USD 300k property — 5-yr, path to permanent)
5. DO Investor Residency (USD 200k minimum via company / incentive-regime investment per DGM; direct property purchase not listed as a route — verify with DGM; CONFOTUR zones can shave taxes)
6. PH SRRV (USD 10-50k deposit depending on age — retiree visa, not strictly RBI)
7. TH LTR — 4 categories (no fixed property threshold; passive-income or wealth route)
8. MY MM2H (post-2024 reform: tiers USD 150k / 500k / 1M deposit + compulsory residence ≥ RM 600k / 1M / 2M)
9. CY (€300k PR — distinct from ended CBI)
10. MT MPRP (€375k lease/€750k purchase + fees)
11. PA (Friendly Nations $200k / Qualified Investor $300k)
12. LV (€250k Riga radius, built only)
13. ID 2nd Home Visa (IDR 2B funds, 5-10 yr; not strictly property-tied)
14. EG (PM Decree 3099/2019 investor routes — state real-estate tier USD 500,000 per GAFI form vs USD 300,000 per US State Dept 2025 ICS; outcome citizenship vs permanent residency unreconciled)
15. CO Migratorio M (350× SMLMV ≈ USD 195k property route at 2026 SMLMV + TRM 3,144.14)
16. UY (no formal RBI; tax-residency 11-yr exemption is the actual draw)
17. CL (no formal RBI; investor-visa via Sociedad)
18. **HK CIES reactivated Mar 2024** — HK$30M total + ≤HK$10M residential (Investments Office, ImmD)
19. **AD Residència Passiva** — ~€600k OR €350k + €50k AFA deposit (passive ≥90d/yr)
20. **MC carte de séjour** — ~€500k bank deposit + property/rental practitioner (Sûreté Publique)
21. **MD Investor Residency Law 200/2010** — €250k 5yr → naturalisation eligibility 8yr; CBI ENDED via Law 100/2020
22. **KR F-2 Investor** — ₩600M property/business via designated route, 5yr → F-5 PR
23. **TW Gold Card** — no investment, high-skill 8-category route, 4-yr work + residency → APRC 5yr
24. SG / MO / LI — **NO golden-visa via real estate**; SG via GIP (S$10M/S$25M/S$200M), MO Investment Residence SUSPENDED since 2007, LI quota-only
25. **QA Investor Residency Law 21/2018** — ≥QAR 730k → 5yr renewable; PR Law 10/2018 ≥QAR 1M (capped ~100/yr); **NO citizenship-by-investment** (Law 38/2005 prohibits)
26. **SA Premium Residency Vision 2030** — SAR 800k one-time / SAR 100k/yr renewable / Real-Estate-Owner SAR 4M; verify with Premium Residency Center
27. **AM Investor Residency** — AMD 50M (~USD 130k) deposit OR property → 5yr renewable; **Citizenship by descent (Diaspora) Art. 13 streamlined** for global Armenian diaspora (~7M)
28. **AZ TRP via real estate** — ≥AZN 100k (~USD 60k) → 1yr renewable to 5+; PR after 8yr continuous TRP; Strategic Investor Visa AZN 540k priority sectors
29. **PY Resolución SET 1186/2023 reformed PR** — formerly cheapest formal RBI (~USD 5,200) → now USD 70k SUACE business invest OR active SET RUC; citizenship 3yr continuous PR
30. **PE Investor Visa** — USD 30k BUSINESS activity (NOT real-estate exclusively) / **Rentista USD 1,500/mo passive**; PR after 3yr; passport after 2yr PR
31. **EC Investor Visa** — USD 42,500 (~100×SBU 2026 SBU USD 470/mo) / **Pensioner Visa USD 1,500/mo**; PR after 21mo Temporary; naturalization 3yr PR
32. **TN Investor Residence Permit** — ≥TND 1M (~USD 320k); **Tunisia Investor Visa drafted 2024 NOT gazetted** — verify gazette status
33. **IN — NO golden-visa via real estate (UNIQUE absence)**; OCI lifetime multi-entry for Indian-origin descendants only; foreign-buyer residential ban for non-NRI/non-OCI per FEMA 2018 Sch.I
34. **NG — NO golden-visa via real estate**; STR-1 Investor visa USD 100k business is the practical pathway; naturalization 15+yr + Nigerian language + dual NOT allowed for native-born
35. **KE — NO golden-visa via real estate (UNIQUE absence in EAC)**; Class A1 Investor USD 100k business / **Class K Resident KES 200k+/yr passive** / PR 7yr / Citizenship 7yr + Swahili
36. **JO CBI Jordan since 2018** — JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport (~50 visa-free destinations — WEAK passport for mobility); **Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable)**; Aqaba ASEZ separate framework
37. **OM Investor Residency Royal Decree 89/2021** — 5-yr ≥OMR 250k (~USD 650k) ITC freehold / 10-yr ≥OMR 500k (~USD 1.3M) ITC; **Long-term Retiree ≥OMR 4,000/mo pension (~USD 10,400)**; NO citizenship-by-investment
38. **BH Bahrain Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k) → 10-yr renewable Self-Sponsored Residence Permit**; **Golden Residency Decree 16/2022** 10-yr renewable for property owners ≥BHD 200k OR investors / talented / retirees (BHD 4k/mo); NO CBI
39. **KW — NO golden-visa via real estate (UNIQUE absence in GCC)**; residency entirely via employment Iqama (Decree-Law 17/1959); foreigners CANNOT own real estate freehold (Decree-Law 74/1979); citizenship effectively impossible (Decree-Law 15/1959)
40. **LB Investor Residency ≥USD 50k Lebanese business (1-yr renewable)**; property ownership ≥USD 200k can support but not automatic; **Lebanese descent streamlined naturalization** for ~13M global Mahjar diaspora; dual citizenship since 2007

### Cleanest 2026 tax reforms (helpful for buyers)
1. CY (Comprehensive Tax Reform 1 Jan 2026 — CGT exemptions raised, SDC abolished)
2. LU (Bëllegen Akt €40k credit per person made permanent)
3. MT (UCA / vacant 0% on first €750k Jan 2025–Dec 2026)
4. PT (IFICI replaced NHR — narrower but operational)
5. LT (NTM 2026 progressive on non-main with main-dwelling threshold ≥€450k)

### Steepest 2026 tax reforms (less helpful for buyers)
1. RO (VAT 19→21% Aug 2025; local property tax baseline +79% Jan 2026)
2. NL (Box 3 forfait 6% 2026)
3. UK (SDLT thresholds reverted 1 Apr 2025)
4. CH (Eigenmietwert abolition 2028 — net depending on profile)

## Cross-cutting red-flag flags

When comparing, surface country-level structural flags:
- 🚩 BA: dual-entity (FBiH/RS-entity) — buyer must understand
- 🚩 CY: TRNC north title risk
- 🚩 LV: compulsory land lease (`dalītais īpašums`) Riga gotcha
- 🚩 MX: fideicomiso restricted zone (50km coast/100km border)
- 🚩 RO: AMCCRS pre-1977 Bucharest Rs I class — insurance/mortgage refusal
- 🚩 PA: 10km border restriction (constitutional)
- 🚩 GR: Golden Visa thresholds vary by zone; "where" matters more than "how much"
- 🚩 BG: non-EU cannot own ANY land directly
- 🚩 RO: non-EU cannot own land (buildings only)
- 🚩 IT: non-resident purchase tax 9% vs resident 2% (cadastral)
- 🚩 TH: condo 49% foreign-quota cap per building — title verification at Land Office mandatory
- 🚩 PH: condo 40% foreign-quota cap per project — Master Deed must show available foreign allocation
- 🚩 VN: 50-yr leasehold + 30%-units-per-building / 250-houses-per-ward foreign quotas (2024 Land Law)
- 🚩 ID: Hak Milik freehold not available to foreigners — Hak Pakai or PMA structures only; nominee arrangements legally void
- 🚩 MY: state-level minimum thresholds for foreigners (MYR 500k-2M depending on state and tier — see my/playbook.md) + foreigner MOT stamp duty flat 8% from 1 Jan 2026 (Budget 2026, per my/playbook.md — verify at LHDN)
- 🚩 IL: ~93% land is state-owned (RMI / Israel Land Authority) — most "purchases" are 49/98-yr capitalised leaseholds, not freehold
- 🚩 IL: war-zone insurance via Karnit (state-backed compensation fund) — privates not always reachable for missile-impact zones
- 🚩 TR: military-restricted-zone clearance required — title transfer can be blocked even after deposit
- 🚩 TR: reciprocity list — buyer's nationality determines eligibility (some nationalities barred)
- 🚩 AE: foreign ownership only in designated freehold zones (Dubai/Abu Dhabi-specific lists); leaseholds elsewhere
- 🚩 AE: no annual property tax but 5% Dubai housing fee on rental value via DEWA bills
- 🚩 EG: Sinai + Suez Canal zones excluded for foreigners; max 2 properties × 4,000 m² total nationally
- 🚩 EG: Form 4 (or successor regulation) — currency-repatriation evidence at time of sale, retain bank import certificate
- 🚩 MA: only `titré` (registered) properties safely transferable to foreigners; `melkia`/`habous` titles risk-prone; agricultural land barred without permit
- 🚩 ZA: 50% LTV typical cap for non-resident mortgage; SARB approval may be required for capital introduction
- 🚩 GE: ultra-fast registration (<1 day Public Service Hall) — but title-search depth shallow vs EU; commission independent lawyer pre-signing
- 🚩 JP: foreign mortgage extremely limited (Shinsei/SBI only; large down-payment); cash-buy is the norm
- 🚩 JP: shakkan / akiya (vacant-house) stock can carry undisclosed cleanup/demolition liabilities — pre-1981 builds also fail current seismic code
- 🚩 DO: CONFOTUR (tourism-zone) properties can waive transfer + IPI taxes for 15 yr — verify project's CONFOTUR registration before closing
- 🚩 CO: predial varies by municipio + estrato (socio-economic strata 1-6); dual cadastre (catastro multipropósito) rollout mid-2026
- 🚩 UY: property contracts often denominated in USD, not UYU — confirm currency clause and parallel-rate mechanism
- 🚩 CL: PE/BO/AR border 10-km restriction (Decree 1939/1977 + DL 1.939); foreigners need presidential authorisation
- 🚩 US: FIRPTA — non-resident sellers face 15% withholding on gross sale price (not gain) at closing; refund via 1040-NR
- 🚩 US: state-by-state divergence is the dominant variable — TX no income tax + 2.5% property tax vs CA 1% Prop-13 cap + 13.3% income tax
- 🚩 SG: **ABSD (Additional Buyer's Stamp Duty) 60% non-resident** — among the highest globally; foreigners barred from landed homes (Restricted Residential Property Act); strata/condo only without SLA approval — verify with IRAS
- 🚩 HK: **BSD 15% non-PR + AVD up to 4.25%** + Special Stamp Duty if <3 yrs — partial cooling-measure rollback Oct 2023-2024 (verify per IRD); Article 23 (NSL) Mar 2024 sentiment factor for some buyers
- 🚩 KR: **jeonse rental-deposit system** unique risk (post-2022 HUG fraud-crisis reforms); comprehensive real estate tax 종부세 0.5-5% on multi-home owners — among most progressive globally
- 🚩 TW: 2024 Hualien M7.4 earthquake — seismic disclosure increasingly priced in; reciprocity-list-based foreign-buyer eligibility (verify BOCA list)
- 🚩 MO: Investment Residence SUSPENDED since 2007 — no residency pathway via property; tourism + casino-economy ~50% GDP creates high cyclicality; concessões 2022 renewed 10yr
- 🚩 AD: **Llei 26/2024** STR regulation + parish quotas narrow short-let economics; **20yr to naturalisation** (longest in Western Europe); CASS social-security mandatory for residents
- 🚩 MC: residence pathway requires Sûreté Publique due-diligence + ~€500k bank deposit + property purchase or rental practitioner; **NO PIT** is the principal draw (except FR nationals via 1963 Convention)
- 🚩 LI: quota-based residency (~28 EEA + ~17 third-country/year by lottery) — Lex-Koller-equivalent narrows buyer pool; Personal Residence Programme rare petition only
- 🚩 MD: **Transnistria scope excluded** from any due-diligence on titles east of Dniester; CBI ENDED via Law 100/2020; Investor Residency Law 200/2010 (€250k) is the practical track; Romanian-citizenship-by-descent → EU passport path commonly used in parallel
- 🚩 QA: foreigners limited to **designated freehold zones** (Pearl-Qatar / West Bay Lagoon / Lusail); rest leasehold; **NO citizenship-by-investment** (Law 38/2005); 88% expat population creates dependency-on-residency dynamics; **2018/2021/2024 Doha storm-surge floods + extreme heat 45°C+ + sandstorms** material to disclosure
- 🚩 SA: **Mecca/Medina Muslim-only ownership** constitutional restriction — non-Muslim foreigners barred from Holy Cities real estate entirely; **Vision 2030 mega-projects (NEOM, Qiddiya, Diriyah, Red Sea, AlUla, Roshn)** drive employment but creates concentration risk; Premium Residency Real-Estate-Owner threshold SAR 4M; **2009/2011 Jeddah catastrophic floods + 50°C+ summer + sandstorms + drought + groundwater depletion**
- 🚩 PE: **border 50km Andean restriction (Constitution Art. 71)** — foreigners need Supreme Decree authorization for border-zone property; **Pacific Ring of Fire HIGH seismic + tsunami coastal + 2017/2023 El Niño catastrophic floods + huaicos + volcanic Misti/Ubinas/Sabancaya south**; Lima STR Decree 001-2023 + Lima Miraflores/Barranco regs
- 🚩 EC: **2024 Internal Armed Conflict Declaration** — violent crime peaks Guayaquil/Esmeraldas/Manta (Quito/Cuenca relatively safer); **Pacific Ring seismic (2016 Pedernales M7.8) + Cotopaxi volcano active 2024 + Galapagos rising sea-temp**; **USD-dollarized since 2000** (no native currency — political-economy reversion-risk overhang); STR Decreto 042-2020 Quito
- 🚩 PY: **Resolución SET 1186/2023 reformed PR** — formerly cheapest RBI (~USD 5,200) now USD 70k SUACE business invest; **Río Paraguay flooding catastrophic 2014-15/2018/2019/2024 + Cerrado/Chaco wildfires 2019-20/2024 + drought**; **Itaipú/Yacyretá #2 net electricity exporter** (cheap energy attracts data centers but also water-rights tensions); border 50km restriction Ley 2532/2005
- 🚩 AM: **HIGH SEISMIC 1988 Spitak M6.8 baseline (~25,000 deaths) + Yerevan/Gyumri/Vanadzor microzoning**; **post-2020/2023 Karabakh war + ~120k displaced Sep 2023 + CSTO suspension Feb 2024 + Russian-relocant wave 2022-24 (~50% peak Yerevan appreciation)** — reversion risk material; agricultural land barred for foreigners; STR Decision 1158-N (2018)
- 🚩 AZ: **2020+2023 Karabakh + East Zangezur reintegration** — ANAMA de-mining certification required for newly-reintegrated zones + AZ-citizen-priority subsidized housing exclusionary for foreigners; **dual citizenship LIMITED exceptions** (must renounce in many cases); **Caspian seismic + Caspian sea-level falling 2010-24 ~1m + Absheron mud volcanoes (unique)**; STR Decree 1146 (2017); very low crime; oil-revenue stabilized via SOFAZ
- 🚩 TN: **post-2021 constitutional revisions + 2024 elections** political-economy overhang; **IMF EFF program SUSPENDED Mar 2024** structural FX risk; **Office des Changes mandatory for FX repatriation** — without proper documentation foreign-seller proceeds locked in TND (similar to MA Office des Changes friction); **2018 Cap Bon catastrophic floods + 2023-24 record drought (reservoirs <30%) + APAL coastal erosion**; STR Décret 2018-417; Tunisia Investor Visa drafted 2024 NOT gazetted
- 🚩 IN: **NO golden-visa via real estate (UNIQUE absence)** — India does NOT offer property-pegged residency or citizenship; **foreign-buyer residential ban for non-NRI/non-OCI** (FEMA 2018 Sch.I); **agricultural / plantation / farmhouse land barred even for NRIs/OCIs**; **LRS USD 250k/yr cap on outbound remittance**; OCI lifetime multi-entry for Indian-origin descendants is the practical pathway; NRO/NRE bank-account split material for NRIs; English in business + legal + healthcare; Mumbai/Delhi NCR/Bengaluru densely populated; Jio/Airtel/Vi 5G rapid 2024-26 rollout; PMJAY public + extensive private (Apollo / Fortis / Max / Manipal — JCI-accredited)
- 🚩 NG: **Land Use Act 1978 — all land vested in state Governor** — only Statutory Right of Occupancy 99-yr leasehold for foreigners; Governor's consent required for transfers; **NO golden-visa via real estate** — STR-1 Investor visa USD 100k business is the pathway; **security risk requires private security + gated communities**; energy autonomy mandatory (generators + solar) — Lagos VI/Ikoyi/Lekki standard; 2024-25 cost-of-living protests + Tinubu reforms ongoing; English official + Yoruba/Igbo/Hausa + Pidgin universal; Lagos 22M largest African city; expat hubs Lagos VI/Ikoyi/Lekki + Abuja Maitama/Asokoro
- 🚩 KE: **NO golden-visa via real estate (UNIQUE absence in EAC)**; agricultural land restricted to citizens per Constitution Art. 65; 99-yr leasehold cap on non-citizen freehold-equivalents; **Class K Resident Permit KES 200k+/yr passive income** is the practical retiree pathway; SGR Mombasa-Nairobi-Naivasha-Kisumu drives corridor RE; Safaricom 5G + **M-PESA mobile-money universal in admin (unique to KE)**; Aga Khan University Hospital Nairobi flagship; English + Kiswahili official; expat hubs Karen/Lavington/Westlands/Runda/Muthaiga/Kitisuru
- 🚩 JO: **CBI Jordan since 2018** (JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport, ~50 visa-free destinations — WEAK passport for mobility plays, rational mainly for diaspora reconnection / GCC business utility); Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable); Aqaba ASEZ separate framework; Council-of-Ministers approval for >threshold properties; ≤4,000 m² agricultural barred; **among most water-poor globally per FAO + Disi aquifer depletion + Dead Sea shrinking ~1m/yr**; large Iraqi+Syrian+Palestinian diaspora; Arabic + English in business/medical
- 🚩 OM: **Investor Residency Royal Decree 89/2021** — 5-yr ≥OMR 250k (~USD 650k) ITC freehold / 10-yr ≥OMR 500k (~USD 1.3M) ITC; foreigners limited to **Integrated Tourism Complexes (ITC)** designated zones — Royal Decree 12/2006 / 89/2021; **Long-term Retiree Residence ≥OMR 4,000/mo pension (~USD 10,400)**; **NO citizenship-by-investment** (Omani nationality strict); **CYCLONE EXPOSURE HIGH** — Gonu 2007/Phet 2010/Mekunu 2018/Shaheen 2021/Tej 2023 catastrophic Muscat coast (insurance underwriting baseline); Vision 2040; quieter than UAE — appeals to retirees
- 🚩 BH: **Bahrain Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k) → 10-yr renewable Self-Sponsored Residence Permit** (incl. spouse + children); **Golden Residency Decree 16/2022** 10-yr renewable for property owners ≥BHD 200k OR investors / talented / retirees (BHD 4k/mo); foreigners limited to **designated freehold zones** — Diyar Al Muharraq / Amwaj Islands / Durrat Al Bahrain / Reef Island / Bahrain Bay / Seef / Manama Diplomatic Area; NO CBI; Saudi Causeway integration drives weekend medical-tourism flow; banking + financial services hub historically; Arabic + English business + everyday widely
- 🚩 KW: **NO golden-visa via real estate (UNIQUE absence in GCC)** — residency entirely via employment Iqama (Decree-Law 17/1959); **foreigners CANNOT own real estate freehold** — only 5-yr leasehold via Iqama-employer-sponsored arrangements (Decree-Law 74/1979 / 8/2008 amendments); citizenship effectively impossible (Decree-Law 15/1959); **Bedoon stateless population pressing issue**; ~70% expat (largest IN/EG/BD/PH/SY); **Vision 2035**; periodic political deadlock (parliament dissolved 2024); among the most restrictive globally on foreign property ownership
- 🚩 LB: NO golden-visa via real estate; **Investor Residency ≥USD 50k Lebanese business (1-yr renewable)**; property ownership ≥USD 200k can support residency application but not automatic; **post-2019 banking-sector collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war Sep-Nov 2024**; foreign-buyer cohort dominated by ~13M Lebanese diaspora returnees (US/CA/AU/FR/BR/AR Mahjar dominant); ≤3,000 m² aggregate Beirut / ≤10,000 m² Mount Lebanon / coastal limits; Council-of-Ministers approval for >limits; Lebanese-descent buyers exempt; Touch + Alfa 4G ageing — **NO 5G yet**; Arabic + French + English trilingual; healthcare collapse since 2019 — historical AUB/Hôtel-Dieu de France standard; Cedars ski-zone unique to Middle East

## Anti-hallucination

- **Only compare countries already in the skill** (`countries/<iso2>/playbook.md` exists). Refuse to compare unsupported countries.
- **Use the playbook values as authoritative** — do not retrieve fresh data per-country during a `--compare` run; trust the latest playbook refresh
- **Date-stamp every cell** — comparison output must show "as of <playbook last-update>" per row
- **Surface playbook confidence** — if any country has LOW confidence, flag it in the row

## Reverse mode (`--match`)

`--match` is `--compare` pointed **backwards**: instead of naming the countries and comparing them, the user states their **constraints** (cohort + budget + criteria) and the skill returns a **ranked shortlist of best-fit countries** from the supported corpus. It is an address-less **discovery mode**, not a per-address section — most buyers know their constraints, not their candidate countries.

It reuses this file's precomputed verdict shortcuts + `config/_visa-programs.json` + the per-playbook values as the authoritative data layer — it never invents a score.

### Invocation

```
/property-deep-dive --match --cohort=<type> [--budget=<amount>] --criteria=<list> [--top=N] [--region=<shortcut>] [--exclude=<iso2,...>] [--must=<hard-filter,...>]
```

Examples:

- `--match --cohort=retiree --budget=300k --criteria=tax,climate,healthcare,visa --top=5`
- `--match --cohort=investor --criteria=yield,acquisition-cost,annual-carry --region=eu --must=foreign-buyer-open`
- `--match --cohort=digital-nomad --budget=150k --criteria=connectivity,visa,tax,cost-of-living`

`--top` defaults to **5**. `--region` reuses the comparison-set shortcuts above. The Skip-list (sanctions/conflict states etc.) is always excluded.

### Cohorts + default weight vectors

Cohorts map to existing overlays (no new data). Weights are the cohort default when the user doesn't override; **always shown in the output** (the weighting is the most opinion-laden part — never hide it).

| Cohort | Default weights (sum 100) |
|---|---|
| `retiree` | health 25 · tax 20 · climate 20 · cost-of-living 15 · visa 15 · safety 5 |
| `digital-nomad` | visa 25 · connectivity 20 · tax 20 · cost-of-living 20 · health 15 |
| `investor` | yield 35 · acquisition-cost 20 · annual-carry 15 · exit/CGT 15 · fx 15 |
| `family` | schools 30 · safety 25 · health 20 · cost-of-living 15 · climate 10 |
| `foreign-buyer` | foreign-buyer-access 25 · acquisition-cost 20 · closing/remote 20 · cost-of-living 15 · climate 10 · visa 10 |
| `lifestyle` | climate 30 · cost-of-living 25 · safety 20 · connectivity 15 · health 10 |

### Criteria → data source

| Criterion | Pre-ranked here? | Source |
|---|---|---|
| acquisition-cost | ✅ | § lowest/highest acquisition cost (also the budget hard-filter) |
| annual-carry | ✅ | § lowest/highest annual carry |
| tax | ✅ (partial) | § cleanest/steepest 2026 tax reforms + playbook `--tax` |
| foreign-buyer | ✅ | § most-friendly / highest-friction (also a hard filter) |
| fx | ✅ | § most/least FX-stable for €-buyers |
| visa | ✅ | `config/_visa-programs.json` (also a `--must` hard filter) |
| healthcare | ⚠️ curated | enrollment-timeline tiers (`digital-nomad-healthcare.md` → `config/_match-extracted.json`, ~10 countries) — MEDIUM |
| yield · climate · schools · safety · connectivity · cost-of-living | ❌ no stored value | **LOW / data-not-available** — no per-country value exists in the repo (computed live per-query). Only score a country if its playbook holds a *discrete, citable value*; descriptive prose is NOT a value — see the No-data rule below |

### Execution

1. **Resolve** the candidate set (`--region` shortcut or all supported countries) minus `--exclude` and the Skip-list.
2. **Hard-filter (eliminate)** — drop candidates that fail a pass/fail gate: foreign-buyer access, budget feasibility (entry = segment-typical €/m² × ~60 m²; a hard floor only with `--must=budget`, else a soft signal), and any `--must=` gate (visa availability via `_visa-programs.json`, FX, residency).
3. **Score** each survivor per criterion. Rank-based band: with `K` ranked countries, rank `r` → `band = round(100 × (K − r + 1) / K)` (#1 = 100). Graded hard-derived signals map to `{open 100 / restricted 60 / barred 0}`.
4. **Composite** = `Σ(wᵢ × bandᵢ) / Σ(wᵢ for criteria with data)`. A criterion with no grounded value for a country is **dropped from both numerator and denominator** — missing data must neither help nor penalise; footnote the drop.
5. **Render** the top-N shortlist + per-criterion breakdown + why each ranked where + confidence + a CTA to `--compare` the shortlist.

**No-data rule (grounding gate).** A criterion is *grounded* only by a named list position in this file or a **discrete, dated playbook value** (a stated tier, statistic, or rank) — **never** by descriptive prose ("mild climate", "good schools"). For a `pending`/live criterion, if the playbook holds no discrete value, render the cell `—` and **drop the criterion from that country's composite** (step 4). Never convert adjectives into a band or score. The generator never fabricates a pending criterion — the runtime extractor must not either. A `—` cell is the correct, expected output, not a failure.

### Output template

```markdown
## Country Match — <cohort>, budget <amount>, criteria <list>

**Candidates**: <N supported>   **After hard filters**: <M>   **Date**: <YYYY-MM-DD> (playbook last-refresh)

### Hard filters (eliminations)
- foreign-buyer-open → dropped CA, AU, NZ, TH(land), KW…
- budget ≥ entry → dropped MC, CH, SG(non-res)…

### Ranked shortlist (top N)
🥇 1. PT — 84/100 · open (NIF only), low carry, IFICI tax, D7 visa  [climate/health: no data → dropped]
🥈 2. GR — 80/100 · €800k/€400k golden visa; 🚩 zone-dependent thresholds
🥉 3. ES — 78/100 · open (NIE), deep market; ⚠️ acquisition cost ~10-13%

### Per-criterion breakdown
| Country | Tax | Climate | Health | Visa | Acq.cost | Composite |
|---|---|---|---|---|---|---|
| PT | 🟢 | — | — | 🟢 | 🟡 | 84 |

`—` = no grounded value → dropped from the composite (No-data rule); never a guessed band. (PT's climate + healthcare are `pending-extraction`, so they render `—`, not 🟢.)

### Weighting & confidence
- Weights: <cohort default | user-set> — shown in full
- Confidence: <HIGH/MEDIUM/LOW>. **If a country's grounded criteria sum to <50% of its cohort weight, mark its composite `LOW — partial` + show the surviving-weight %** — e.g. a `family` query leans on schools + safety (both unstored), so most weight drops and the composite is low-trust. Healthcare runs MEDIUM (curated, ~10 countries); the other five pending criteria are LOW / data-not-available.
- Dropped (no data): <country:criterion …> — list every `—` cell.

### Next step
→ Deep-compare:  /property-deep-dive --compare=pt,gr,es,cy,it --tax --climate --retirement
→ Full brief:    /property-deep-dive <PT address> --all
```

### Anti-hallucination (inherits the four rules above + 3 additions)

The four `--compare` rules apply verbatim (supported countries only · playbook/precomputed values are authoritative, no fresh per-country fetch · date-stamp · surface LOW confidence). Plus:

5. **No fabricated composite scores** — every band traces to a named list position (§ above) or a dated playbook value; show the inputs. A criterion with no grounded source for a country is excluded from that country's composite, never guessed.
6. **Structural shortlist, not advice** — `--match` ranks *documented attributes against stated constraints*. It is not financial / immigration / tax advice; weights are inherently subjective. See `DISCLAIMER.md`.
7. **Show the weighting** — the cohort default (or user) weights are always printed; the user must be able to see why #1 beat #2.

If hard filters eliminate everything, say so and suggest relaxing a `--must=`. If fewer than 3 survive, return them but flag the thin set.

### Worked example — retiree, €300k, criteria tax+climate+healthcare+visa

Illustrative (numbers are from individual playbooks at last refresh — check each `**Last verified**:` before quoting):

- **Hard filters**: foreign-buyer-open (drops CA / AU / NZ established-home bans); budget ≥ entry (€300k clears PT/GR/ES/CY/IT; drops MC/CH).
- **Result**: a PT-led Mediterranean shortlist — PT (open + IFICI + D7), GR (golden-visa + climate), ES (deep market, higher acquisition cost ~10-13%), CY (low carry, 🚩 north-title), IT (2%-resident vs 9%-non-resident cadastral 🚩). Each row carries its per-criterion band + the playbook date; tax/fx/acquisition-cost/foreign-buyer/visa are HIGH (pre-ranked), climate/healthcare run MEDIUM until the Phase-2 index.

### Phase 2 — `config/_match-index.json` (built)

`config/_match-index.json` precomputes, **per country, the rank/band + `src` provenance** for the criteria this file already ranks (acquisition-cost, annual-carry, fx, foreign-buyer, visa, tax) plus the three hard-filter booleans (`foreign-buyer-open`, `no-fx-risk`, `property-residency-route`). It is **generated deterministically** from this file's ranked lists + `config/_visa-programs.json` by `scripts/render-match-index.py` (regenerate on change; CI `--check` in `.github/workflows/match-index-audit.yml` keeps it in sync; `scripts/render-match-index-test.py` covers it). **Reverse mode consumes it**: read each survivor's band + hard-filter from the index when present; a country absent from the index (the lists don't cover all 126) or a criterion marked `pending-extraction` is resolved live **only from a discrete playbook value** (No-data rule) — absent that it renders `—` (LOW / data-not-available), never a MEDIUM band from prose.

Of the seven judgement-heavy criteria, **only `healthcare` has a stored, citable per-country signal** (public-system enrollment timeline in `digital-nomad-healthcare.md`). It is curated into `config/_match-extracted.json` (~10 countries — each with source + verbatim evidence + tier) and merged into the index at MEDIUM confidence. The other six — yield, climate, safety, connectivity, schools, cost-of-living — have **no stored per-country value**: the skill computes them live/per-query from primary sources *by design* (so they never go stale), so pre-baking them into a static index would decay or fabricate. They stay `{"status": "pending-extraction"}`: at query time each is scored **only if the playbook holds a discrete value** (No-data rule) — otherwise rendered `—` and dropped, never a MEDIUM band invented from prose. The generator **never fabricates** a pending criterion. Full design + the feasibility finding: `_local/scope-match-section.md`.

## Worked-example comparisons (new-country trios)

These illustrate how the matrix is used. Numbers are from individual playbooks at last refresh; check each playbook's `**Last verified**:` stamp before quoting.

### Example A — JP vs TH vs PH for retirement (Pacific-rim retiree)

| Metric | JP | TH | PH |
|---|---|---|---|
| Foreign access to land | Yes (freehold) | NO (condo 49% quota only) | NO (condo 40% quota only) |
| Total acquisition cost | ~6-7% | ~6-8% | ~10% |
| Annual carry | 1.4% + 0.3% on assessed | 0.01-0.7% L+B | RPT munisipal — modest |
| Retiree visa | None RBI; "Investor" requires active business | LTR (4 cat — passive-income route) | SRRV (USD 10-50k deposit by age) |
| English usability | LOW outside Tokyo/Osaka | MEDIUM (tourist zones) | HIGH (lingua-franca) |
| Currency stability | JPY weak vs USD/EUR 2024-26 — buyer tailwind | THB managed | PHP EM-volatile |
| Climate trajectory | Rising heat + typhoon north-shift | Rising heat + flood (BKK) | Typhoon-belt + sea-rise |

🥇 **PH** for English-fluent retiree on USD income who accepts condo-only ownership and tropical-storm risk
🥈 **TH** for retiree who wants LTR-tier tax structure and is comfortable with leasehold-house workaround (30-yr renewable)
🥉 **JP** for retiree wanting freehold ownership + rule-of-law, with capital base willing to absorb low rental yield + ageing-society demographic headwind

**Confidence**: MEDIUM — visa thresholds + tax rates verified per individual playbooks Q2 2026; long-term retirement viability is a 20-year bet that no playbook can fully de-risk.

### Example B — AE vs IL vs CY for tax-residence pivot

| Metric | AE | IL | CY |
|---|---|---|---|
| Personal income tax | 0% (corporate 9% above AED 375k) | Progressive to 47% + 3% surtax | Progressive to 35%; SDC abolished 1 Jan 2026 |
| CGT on resale | 0% | 25-50% Mas Shevach (NR uplift) | Exempt above raised thresholds (2026 reform) |
| Property tax annual | None (5% housing fee on rental only) | Arnona muni | Municipal small (national IPT abolished 2017) |
| Foreign ownership | Designated freehold zones only | de-facto leasehold (RMI 93% state land) | Full freehold |
| Visa pathway | Golden Visa AED 2M property, 10y | Aliyah (Jewish-only) — closed pathway for non-Jews | PR €300k property |
| Geopolitical risk | Regional but low-impact internally | High (war + missile risk) | Cyprus problem: TRNC north title trap |

🥇 **CY** for clean tax-residence pivot with EU-passport upside (after long stay) + post-2026 reform clarity
🥈 **AE** for fast-track 10-yr Golden Visa + zero income tax — at cost of EU access and lower liquidity in resale
🥉 **IL** only for Jewish applicants (Aliyah-eligible) willing to accept war-zone insurance via Karnit + leasehold dominant tenure

**Confidence**: MEDIUM — CY 2026 tax-reform details still being clarified by Inland Revenue; AE Golden Visa thresholds stable since 2022; IL war-risk is dynamic.

### Example C — CO vs MX vs PA for LATAM digital-nomad/investor

| Metric | CO | MX | PA |
|---|---|---|---|
| Foreign-buyer access | Open | Fideicomiso required in 50km coast / 100km border | Open except 10km border (constitutional) |
| Total acquisition cost | ~5-6% | ~6-8% (incl. fideicomiso setup) | ~5-6% |
| Annual carry | Predial municipio + estrato | Predial municipio | IBI escalating brackets |
| CGT | 15% ganancia ocasional | 25-35% on gain (or 25% gross option) | 3% + 10% capital gains structure |
| Digital-nomad/RBI route | Migratorio M (350× SMLMV) | RNE / Temporary Resident | Friendly Nations USD 200k / Qualified Investor USD 300k |
| Climate | Andean mild | Coastal hurricane belt (Pacific + Caribbean) | Caribbean+Pacific dual-coast hurricane fringe |
| FX risk | COP EM-volatile | MXN EM-volatile | USD-denominated economy (no FX risk for USD buyers) |

🥇 **PA** for USD-base investor wanting simplest visa + zero FX risk + Friendly Nations or Qualified Investor pathway
🥈 **CO** for cheaper entry, moderate climate, but 2026 catastro-multipropósito rollout creates assessed-value uncertainty
🥉 **MX** for buyer accepting fideicomiso friction in exchange for deeper market and proximity to US

**Confidence**: MEDIUM — PA Qualified Investor program threshold verified Q1 2026; CO catastro reform cadence per municipio is uneven.

### Example D — GE vs PT vs CY for EU-adjacent low-tax base

| Metric | GE | PT | CY |
|---|---|---|---|
| EU member? | NO (EU-adjacent / candidate) | YES | YES |
| Foreign-buyer access | Open, fastest registration globally (<1 day) | Open (NIF only) | Open |
| Acquisition cost | ~0.1-0.5% | ~7-8% (IMT + stamp + notary) | ~8-10% |
| Annual property tax | Income-gated (only above GEL 40k household income) | IMI 0.3-0.45% | Municipal small |
| CGT | None after 2-yr hold | 28% non-residents (50% inclusion residents) | Exempt above raised 2026 thresholds |
| Tax residency draw | Territorial — 1% small-business / 20% personal | IFICI replaced NHR (narrower) 2024+ | 60-day rule + non-dom 17 years |
| Visa | Investor USD 300k property | D7/D8 (income-based, not property) | PR €300k property |
| Risk | Russia border + currency exposure (GEL) | EU stability | TRNC title trap; banking-sector overhang |

🥇 **CY** for EU-passport-track tax-residence with strongest 2026 reform tailwind
🥈 **PT** for EU base prioritising rule-of-law over tax minimisation (post-NHR closure)
🥉 **GE** for ultra-fast non-EU base with lowest acquisition friction and territorial-tax structure — at cost of EU access and proximity to active conflict zone

**Confidence**: MEDIUM — GE political stability and visa-program continuity carry higher-than-EU uncertainty; PT IFICI implementation still settling; CY 2026 reform clarifications ongoing.

### Example E — SG vs HK vs MO for East-Asian financial-hub base

| Metric | SG | HK | MO |
|---|---|---|---|
| EU member? | NO (city-state) | NO (HK SAR China) | NO (MO SAR China) |
| Foreign-buyer access | Strata only without SLA approval; **ABSD 60% non-resident** | Open + **BSD 15% non-PR + AVD up to 4.25%** | Open but Investment Residence SUSPENDED 2007 |
| Total acquisition cost | **65-70%+ for non-residents** (BSD + ABSD + agent + legal); **3-7% citizen** | ~20-25% non-PR (AVD + BSD 15%); ~5-10% PR | ~5-8% (post-stamp duty + agent) |
| Annual property tax | Property Tax 0-23% on AV (owner-occupier) / up to 32% non-occupied | Rates ~5% on Rateable Value + Property Tax 15% on rental | None on residential; 6-10% Property Tax on rental net |
| CGT | NONE | NONE for individuals (Profits Tax doesn't apply to personal capital gains) | NONE on personal property gain |
| Personal income tax | Resident 0-22% progressive; foreign-source generally NOT taxed in SG | Salaries Tax 2-17% progressive / 15% standard; territorial — HK-source only | Macao Professional Tax territorial — MO-source only |
| Currency | SGD MAS-managed-float | HKD-USD peg LERS 7.75-7.85 (HKMA) | MOP-HKD-USD double peg |
| Visa pathway via property | None (GIP S$10M/S$25M/S$200M only) | **CIES reactivated Mar 2024** HK$30M + ≤HK$10M residential | **SUSPENDED 2007** — Talent Programme NOT property-linked |
| Climate | Equatorial 24-32°C year-round (Changi best-in-world airport) | Subtropical 14-33°C; typhoon season Jul-Oct | Subtropical 14-32°C; typhoon + post-Hato 2017 storm-surge reforms |

🥇 **HK** for high-net-worth wanting investment-track residency via property (CIES reactivated Mar 2024); accept Article 23 (NSL) sentiment factor and partial post-2020 expat outflow recovery
🥈 **SG** for highest-quality administrative environment + best-in-world airport + lowest CGT/PIT structure for foreign-source income — at cost of **ABSD 60% non-resident** which restructures any property-purchase economics into citizen-class transaction
🥉 **MO** only for those with a non-property residence pathway (Talent Programme, family-unification) — Investment Residence has been SUSPENDED since 2007

**Confidence**: MEDIUM — HK CIES revival details still being clarified by ImmD post-Mar 2024; SG ABSD 60% verified at IRAS but all-in stamp-duty stack drift on cooling-measure cycles; MO Talent Programme 2024 scope still being defined by IPIM. Verify all thresholds at issuing authority.

### Example F — KR vs TW for East-Asian remote-work base

| Metric | KR | TW |
|---|---|---|
| Foreign-buyer access | Open (Foreigner's Land Acquisition Act notification only) | Reciprocity-list-based — verify BOCA list per nationality |
| Total acquisition cost | ~6-8% (acquisition tax 1-3% sliding by price + 0.2% local + agent + reg fee) | ~6-8% (deed tax 6% + agent 1-2% + reg) |
| Annual carry | jaesanse 0.1-0.4% + comprehensive real estate tax 종부세 0.5-5% on multi-home owners | House Tax 1.5-3.6% by use + Land Value Tax 1-5.5% |
| CGT | Separate 6-45% + multi-home top rate up to 75% | AMT regime on foreign-source >NT$7M; 6% surtax on certain investment income |
| Personal income tax | Worldwide for residents (>183 days); progressive 6-45%; **5/10-yr foreign-source exemption** for newly-resident foreign workers (PIT Act Art. 18-2) | Worldwide for residents (>183 days); progressive 5-40% |
| Visa pathway | **F-2 Investor (₩600M, 5yr) → F-5 PR**; F-4 Korean diaspora; **Workation Visa F-1-D (Jan 2024)** | **Gold Card** 4-yr work + residency (no investment); APRC after 5yr; Plum Blossom long-stay |
| Climate | Cold continental — Seoul -5/+3°C winter, 26-31°C summer; aging society | Tropical-subtropical; Taipei 14-20°C winter, 28-32°C summer; **2024 Hualien M7.4 earthquake** |
| Internet | Gigabit fiber norm (KT/SK/LG); ranked top globally on most digital metrics | Gigabit FTTH norm (Chunghwa, Taiwan Mobile) |

🥇 **TW** for remote-worker via **Gold Card** (no investment threshold) — 8 high-skill categories + 4-yr residency leading to APRC; lower COL than KR for English-medium services
🥈 **KR** for those targeting F-2/F-5 PR via investment OR for Korean-diaspora F-4 holders; multi-home tax (종부세 0.5-5%) is material structural drag for portfolio buyers

**Confidence**: MEDIUM — KR Workation Visa F-1-D launched Jan 2024 (verify HiKorea); TW Gold Card category list updates periodically (verify NIA/BOCA); TW 2024 Hualien M7.4 disclosure rules still settling.

### Example G — AD vs MC vs LI for European-microstate residence

| Metric | AD | MC | LI |
|---|---|---|---|
| EU member? | NO (Monetary Treaty 2011, EUR) | NO (Monetary Treaty, EUR) | NO (EEA member; CHF currency union with CH) |
| Schengen | NO | YES (Schengen via FR) | YES (via 2011 extension) |
| Personal income tax | IRPF 0/5/10% — **lowest in Western Europe** | **NONE** (except FR nationals via 1963 Convention) | ~2.5-22.4% combined federal + commune (among lowest CH-area) |
| CGT | 10% within IRPF | NONE | Within personal-tax regime |
| Acquisition cost | ~3-5% (ITP 4% + notari + Govern registration) | ~10-12% (4.5% droits + notary + agent + 20% TVA on agent) | ~5-7% (Handänderungssteuer ~2% + commune + Grundbuchamt) |
| Visa pathway | **Residència Passiva ~€600k** OR €350k + €50k AFA; passive ≥90d/yr | **Carte temporaire** ~€500k bank deposit + property practitioner | **Quota-based lottery** (~28 EEA + ~17 third-country/year); Personal Residence Programme rare petition only |
| Naturalisation | 20 yrs (longest in Western Europe) | 10 yrs after privilégiée; rare in practice | 10 yrs (after surrendering prior citizenship — verify with Ausländer- und Passamt) |
| Population | ~85k (~75% non-Andorran) | ~38k (~70% non-Monégasque) | ~40k |
| Climate | Alpine 0-8°C winter, 18-25°C summer | Mediterranean 8-15°C winter, 24-29°C summer (mildest of three) | Alpine 0-5°C winter, 18-24°C summer |
| Healthcare | CASS mandatory; cross-border to FR/ES | Caisses Sociales + CHPG; cross-border to FR/IT | KVG-equivalent; cross-border to CH |

🥇 **MC** for ultra-high-net-worth wanting **NO PIT/CGT** + Mediterranean climate + Schengen access — at cost of highest COL globally and strict Sûreté Publique due-diligence
🥈 **AD** for HNWI accepting alpine isolation in exchange for IRPF 0/5/10% (lowest in Western Europe) and lowest acquisition cost of the three; **20yr naturalisation** is the long-game catch
🥉 **LI** only for lottery-winning EEA candidates or rare Personal Residence Programme petitioners; CH-integrated practice for healthcare/banking

**Confidence**: MEDIUM — AD Llei 26/2024 STR + parish quotas still rolling out per parròquia; MC Sûreté Publique due-diligence threshold drift on FX cycles; LI quota allocation publicly disclosed annually but qualifying-criteria opaque. Verify all thresholds at issuing authority.

### Example H — MD vs UA-adjacent EU-candidates for low-COL Eastern European base

| Metric | MD | (cross-reference: GE / RS / ME) |
|---|---|---|
| EU candidate? | YES (Jun 2022) | GE Dec 2023 (accession de facto halted Jun 2024); RS/ME accession negotiations open |
| COL | **Lowest in Europe** (Numbeo 2024-2026) | GE/RS/ME mid-low |
| Personal income tax | Flat 12% (one of lowest in Europe) | GE territorial-leaning; RS 10-25% progressive; ME 9-15% progressive |
| Acquisition cost | ~2-4% (notary + State Registration Chamber) | GE 0.1-0.5% (lowest globally); RS 5-7%; ME 5-7% |
| Foreign-buyer access | Open for buildings + non-agricultural land | All three open |
| Visa pathway | **Investor Residency Law 200/2010** — €250k 5yr → naturalisation 8yr | GE Investor Residency USD 300k; RS/ME standard residence |
| Romanian-citizenship-by-descent → EU passport | YES (widely used) | NO equivalent |
| Schengen | NO | NO (all three) |
| Currency | MDL float | GEL float; RSD managed; EUR (ME) |
| Internet | Gigabit fiber Moldtelecom + Orange MD + StarNet (one of fastest fiber penetrations in Eastern Europe) | GE Magticom/Silknet good; RS strong; ME variable |
| Transnistria | **Excluded from due-diligence scope** | N/A |

🥇 **MD** for cheapest Europe COL + flat 12% PIT + Romanian-citizenship-by-descent EU-passport optionality + gigabit fiber norm — at cost of: NO Schengen, NO formal Digital Nomad Visa as of 2026, geographic isolation, Russian-language-spillover political-risk overlay
- Cross-reference GE for similar low-COL Eurasian base with faster registration but EU accession de facto halted since Jun 2024 (candidate since Dec 2023)
- Cross-reference RS/ME for EU-candidate Western Balkans alternatives with broader expat networks

**Confidence**: MEDIUM — MD CBI ended via Law 100/2020 (verified at SFS/Govt portal); Investor Residency Law 200/2010 thresholds verified per Investment Agency Moldova. Romanian-citizenship-by-descent path is widely used but ANC processing times have stretched 2022-2026. Transnistria-scope exclusion is a hard rule for any due-diligence on real-estate east of Dniester.

### Example I — QA vs SA vs AE for GCC tax-residence base

| Metric | QA | SA | AE |
|---|---|---|---|
| Personal income tax | **NONE** for individuals (corporate ~10%) | **NONE** for individuals (Saudi Zakat 2.5% / corporate 20% non-Saudi) | **NONE** for individuals (corporate 9% above AED 375k) |
| CGT on resale | NONE | NONE | NONE |
| Foreign-buyer access | Designated freehold zones only (Pearl-Qatar / West Bay Lagoon / Lusail) | Mecca/Medina constitutional Muslim-only; Premium Residency Real-Estate-Owner SAR 4M minimum | Designated freehold zones only (Dubai Designated Areas + Abu Dhabi investment zones) |
| Visa pathway | **Investor Residency Law 21/2018 ≥QAR 730k → 5yr renewable**; PR Law 10/2018 ≥QAR 1M (capped ~100/yr); **NO CBI** | **Premium Residency Vision 2030** SAR 800k one-time / SAR 100k/yr / SAR 4M Real-Estate-Owner | **Golden Visa AED 2M property → 10yr renewable** |
| Population | ~3.05M (12% Qatari + 88% expat) | ~36.4M (63% Saudi + 37% expat) | ~10.2M (~88% expat) |
| Currency | QAR pegged USD 3.64 since Jul 2001 | SAR pegged USD 3.75 since Jun 1986 | AED pegged USD 3.6725 |
| Climate | 18-42°C; **summer 45°C+ + sandstorms + 2018/2021/2024 Doha storm-surge floods** | 12-45°C interior; **50°C+ summer + sandstorms + 2009/2011 Jeddah catastrophic floods + drought** | 18-42°C; **summer 45°C+ near-uninhabitable May-Sep** |
| Healthcare | HMC public + private (Aspetar / Sidra / Doha Clinic) | MOH + mandatory CCHI for expats + private (JCI-accredited) | Mandatory private DHA / DOH |
| Mega-project pull | FIFA World Cup 2022 legacy + Lusail | Vision 2030: NEOM / Qiddiya / Diriyah / Red Sea / AlUla / Roshn | Established freehold zones + Expo 2020 legacy |

🥇 **AE** for fastest visa pathway (Golden Visa AED 2M → 10yr) + most established freehold-zone economics + best diversification
🥈 **QA** for cleaner cap on foreign population pressure + Investor Residency floor lower (QAR 730k) than SA / AE Golden Visa + sustainable 5yr renewable
🥉 **SA** only for Vision 2030 mega-project economic-pull (NEOM / Red Sea) — but Real-Estate-Owner SAR 4M threshold is the steepest of the three, and Mecca/Medina Muslim-only restriction matters for non-Muslim retirees

**Confidence**: MEDIUM — QA Investor Residency thresholds verified Q1 2026 at MoI; SA Premium Residency Vision 2030 tiers actively being refined by Premium Residency Center; AE Golden Visa stable since 2022. Verify all three with issuing authority before action.

### Example J — AM vs AZ for Caucasus base + Russian-relocant wave dynamics

| Metric | AM | AZ |
|---|---|---|
| EU member? | NO (CSTO suspension Feb 2024 — geopolitical pivot in flight) | NO |
| Foreign-buyer access | Open (equal rights non-citizens per Land Code Art. 4); agricultural and protected land restricted | Open subject to TRP / Strategic Investor; agricultural and border-zone restricted |
| Total acquisition cost | ~3-5% (State Registry + notary + agent) | ~5-8% (registration + notary + agent) |
| Annual carry | Sliding 0-1% on cadastre value, AMD 3M threshold exempt | Modest property tax sliding by region |
| CGT | Within personal-tax regime (flat 21% PIT 2026 on residents) | Within progressive 14-25% PIT |
| Visa pathway | **Investor Residency AMD 50M (~USD 130k) deposit OR property → 5yr renewable**; **Citizenship by descent (Diaspora) Art. 13 streamlined**; naturalization 3yr + dual since 2007 | **TRP via real estate ≥AZN 100k (~USD 60k) → 1yr renewable to 5+**; PR after 8yr; Strategic Investor AZN 540k; **dual citizenship LIMITED** |
| Climate | Continental Yerevan -3 to +3°C / 28-35°C; **HIGH SEISMIC 1988 Spitak M6.8 baseline** | Caspian-moderate Baku 4-10°C / 27-33°C; **Caucasus + Caspian seismic + Absheron mud volcanoes (unique)** |
| Geopolitics | **Post-2020/2023 Karabakh war + ~120k displaced Sep 2023 + CSTO suspension Feb 2024**; Russian-relocant wave 2022-24 (~50% peak Yerevan appreciation) | **2020+2023 Karabakh + East Zangezur reintegration** (ANAMA de-mining required); oil-revenue stabilized via SOFAZ |
| Diaspora | ~7M global (US ~1M, RU ~2M, FR/AR/LB/IR) — Art. 13 descent path | Smaller diaspora; closer to TR economically |
| Internet | Beeline / VivaCell / Ucom fiber gigabit Yerevan | Azercell / Bakcell / Nar 5G Baku |

🥇 **AM** for Armenian-diaspora applicants (Art. 13 descent streamlined; dual since 2007) or for Yerevan-tech base accepting Russian-relocant-wave reversion-risk; appreciation 2022-24 has materially reset price floor higher than pre-war base
🥈 **AZ** for foreign investor accepting **dual-citizenship LIMITED** caveat in exchange for very-low-crime + oil-revenue economic stability + lower cost of living than AM Yerevan post-2022

**Confidence**: MEDIUM — AM Land Code Art. 4 verified; AM Russian-relocant wave 2022-24 documented by NSS / CBA but reversion timing uncertain; AZ Strategic Investor Visa AZN 540k threshold verified at State Migration Service; East Zangezur ANAMA de-mining cert + AZ-citizen-priority housing in newly-reintegrated zones still being clarified.

### Example K — PE vs EC vs PY for Andean / Cono-Sur low-COL base

| Metric | PE | EC | PY |
|---|---|---|---|
| Foreign-buyer access | Open; **border 50km Andean restriction (Constitution Art. 71)** — Supreme Decree for border zones | Open generally but **2024 Internal Armed Conflict Declaration** requires extra title-DD in Guayaquil/Esmeraldas/Manta | Open; border 50km restriction Ley 2532/2005 |
| Total acquisition cost | ~7-10% (alcabala 3% + notary + Registros Públicos + agent) | ~7-10% (alcabala 1% + registry + notary + IVA 15% on services) | ~3-5% (ITBI ~1.5% + notarial + registration; among lowest LatAm) |
| Annual carry | Sliding municipal predial | Sliding municipal predial | Very low ~1% on register-value (effective <0.3%) |
| Pension tax | Worldwide for residents (>183 days); progressive 8-30%; foreign-source pre-arrival potentially exempt Art. 6 LIR | Worldwide for residents (>183 days); progressive 5-37%; potentially exempt Art. 9 LRTI if treaty | **Territorial PIT** — foreign-source NOT subject to PY IRP; flat 8/9/10% on PY-source only |
| Visa pathway | **Investor Visa USD 30k BUSINESS** (NOT real-estate exclusively) / **Rentista USD 1,500/mo passive** | **Pensioner Visa USD 1,500/mo** / **Investor Visa USD 42,500** (~100×SBU 2026 SBU USD 470/mo) | **SET 1186/2023 reformed PR** — formerly USD 5,200 → now USD 70k SUACE business OR active SET RUC |
| Path to citizenship | PR 3yr → passport 2yr PR | Naturalization 3yr PR | Citizenship 3yr continuous PR |
| Currency | PEN BCRP-managed; USD-pricing common Lima Miraflores | **USD-dollarized since 2000** — no native currency | PYG BCP-managed; USD widely accepted Asunción |
| Climate | Lima 16-26°C year-round (Pacific cool current); **HIGH seismic + tsunami + 2017/2023 El Niño** | Quito/Cuenca altitude-moderated 10-22°C; **Pacific Ring + Cotopaxi 2024 active** | Asunción humid subtropical 14-34°C; **Río Paraguay floods 2014-15/2018/2019/2024 + Cerrado wildfires** |
| Expat hub | Lima Miraflores/Barranco/San Isidro | **Cuenca top US/CA expat retiree hub globally** (verify International Living rank) | Asunción Carmelitas/Villa Morra growing AR/BR/RU/EU |
| Energy | Standard | Standard | **Itaipú/Yacyretá #2 net electricity exporter** — cheap energy attracts data centers |

🥇 **PY** for **territorial PIT + lowest acquisition cost + cheap energy** (Itaipú/Yacyretá) + USD 70k SUACE pathway; accept PYG FX volatility + flood/drought climate risk
🥈 **EC** for **Pensioner USD 1,500/mo** (lowest threshold of three) + **Cuenca established US/CA retiree hub** + USD-dollarized FX simplicity; accept 2024 Internal Armed Conflict Declaration overhang on coastal cities
🥉 **PE** for **Lima Miraflores/Barranco established expat infrastructure** + Investor Visa USD 30k BUSINESS pathway; accept seismic + 2017/2023 El Niño climate risk + worldwide-income progressive PIT

**Confidence**: MEDIUM — PY Resolución SET 1186/2023 reform verified at SET; EC Internal Armed Conflict Declaration political-economy overhang dynamic 2024-2026; PE Constitution Art. 71 border-zone restriction stable; all three SBU/SUACE/MIGRACIONES thresholds drift annually — verify at issuing authority.

### Example L — TN vs MA vs EG for North African / Mediterranean retirement

| Metric | TN | MA | EG |
|---|---|---|---|
| Foreign-buyer access | Open via Investor Residence Permit ≥TND 1M; Office des Changes documentation | Only `titré` (registered) properties safely transferable to foreigners; agricultural barred | Max 2 properties × 4,000 m² total; Sinai/Suez excluded |
| Total acquisition cost | ~10-15% (5% droits + 1% conservation foncière + agent) | ~5-8% (cleaner stack) | ~5-7% formal but most properties unregistered |
| Pension tax | Worldwide resident progressive 0-35%; **80% abatement on foreign pension transferred permanently in TND** (Art. 36 Code IRPP — verify) | Foreign pensions: **80% abatement if transferred permanently in DH** (Art. 76 CGI) | Foreign-source pension generally not taxed by EG (territorial application varies) |
| Visa pathway | Investor Residence Permit ≥TND 1M (~USD 320k); **Tunisia Investor Visa drafted 2024 NOT gazetted** | Carte de Séjour (long-stay) standard residence permit | **PM Decree 3099/2019** USD 250k non-refundable Treasury contribution — outcome unreconciled (GAFI: citizenship / US State Dept 2025 ICS: permanent residency) |
| Citizenship | 5yr continuous PR + Arabic; dual since 2014 | 5yr continuous PR | PM Decree 3099/2019 investor routes (outcome unreconciled — verify with the Citizenship Applications Assessment Unit) |
| Population | ~12.07M (Tunis Metro ~2.7M, Sfax ~1M, Sousse ~290k, Djerba ~165k) | ~37M | ~110M |
| Climate | Tunis Mediterranean 11-32°C; **2018 Cap Bon floods + 2023-24 record drought + APAL coastal erosion** | Marrakech 18-22°C winter; Atlantic coast cooler | Hurghada/Sahel 18-35°C; very dry; summer extreme |
| Expat density | Moderate FR/IT/DE/UK (FR cultural ties strong) | FR retirees dominant; UK/DE growing | RU/UA/DE/UK; **EGP currency volatility material** post-2024 devaluation |
| Healthcare | CNAM + private (French-system); **medical-tourism destination** | AMO (2024-2026 expansion) + private (French-system) | New Universal Health Insurance (2018 phased); medivac for serious cases |
| FX repatriation | Office des Changes documentation required (similar MA-style friction) | Office des Changes mandatory for repatriation | Form 4 mandatory for USD repatriation — without it, EGP-only exit during devaluation |
| Macro | **IMF EFF program SUSPENDED Mar 2024** | Stable | EGP devaluation cycles 2022-2024 |

🥇 **MA** for cleanest acquisition stack + 80% abatement on foreign pension + established FR/UK/DE retiree communities (Marrakech / Essaouira / Tangier / Agadir); accept agricultural-land bar + `titré`-only-safely-transferable rule
🥈 **TN** for **medical-tourism healthcare quality + French-system standards** + 80% abatement on foreign pension under Art. 36 Code IRPP (verify); accept IMF EFF Mar 2024 suspension overhang + post-2021 constitutional revision political-economy risk
🥉 **EG** only with **Form 4 documented at purchase** for clean USD repatriation — without it, EGP-only exit during devaluation = catastrophic; **Sinai/Suez excluded** for foreigners; max 2 properties × 4,000 m² total

**Confidence**: MEDIUM — TN Code IRPP Art. 36 80% abatement structure parallels MA Art. 76 CGI but verify with Direction Générale des Impôts; TN IMF EFF Mar 2024 suspension is structural FX overhang; MA Art. 76 CGI verified; EG Decree-3099/2019 thresholds unreconciled between GAFI form and US State Dept 2025 ICS but Form 4 + currency-control risks remain material.

### Example M — OM vs BH vs KW vs JO for non-AE/QA/SA GCC + Levant residency-by-property

| Metric | OM | BH | KW | JO |
|---|---|---|---|---|
| Personal income tax | **NONE** for individuals (OM individual income-tax law drafted 2022 NOT enacted) | **NONE** for individuals | **NONE** for individuals | Worldwide for residents progressive 5-30% + 1% national-contribution |
| CGT on resale | NONE | NONE | NONE | Within personal-tax regime |
| Foreign-buyer access | **ITC (Integrated Tourism Complexes) designated zones only** per RD 12/2006 / 89/2021 | **Designated freehold zones only** (Diyar Al Muharraq / Amwaj Islands / Durrat Al Bahrain / Reef Island / Bahrain Bay / Seef / Manama Diplomatic Area) | **Foreigners CANNOT own real estate freehold** — only 5-yr leasehold via Iqama-employer (Decree-Law 74/1979) | Open subject to Council-of-Ministers approval >threshold; ≤4,000 m² agricultural barred |
| Visa pathway via property | **Royal Decree 89/2021** 5-yr ≥OMR 250k (~USD 650k) ITC / 10-yr ≥OMR 500k (~USD 1.3M); Long-term Retiree ≥OMR 4,000/mo pension (~USD 10,400) | **Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k) → 10-yr renewable**; **Golden Residency Decree 16/2022** 10-yr | **NO golden-visa via real estate (UNIQUE absence in GCC)** — Iqama via employment only | **CBI Jordan since 2018** (JOD 750k bond OR JOD 1M private investment OR JOD 250k SME → Jordanian passport, ~50 visa-free); **Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable)** |
| Citizenship | NO CBI (Omani nationality strict) | NO CBI | Effectively impossible (Decree-Law 15/1959) | **CBI since 2018** — Jordanian passport (~50 visa-free destinations — WEAK for mobility) |
| Population | ~5.0M (Muscat Metro 1.7M, ~38% expat) | ~1.49M (~52% Bahraini + 48% expat) | ~4.85M (~30% Kuwaiti + 70% expat) | ~11.4M (Amman Metro 4.5M; large Iraqi+Syrian+Palestinian diaspora) |
| Currency | OMR pegged USD 0.385 since 1986 | BHD pegged USD 0.376 since 1980 | KWD pegged to undisclosed basket weighted USD (highest-valued currency globally) | JOD pegged USD 0.708 since Oct 1995 |
| Climate | 17-42°C; **Salalah unique Khareef Jun-Sep**; **CYCLONE EXPOSURE HIGH** Gonu/Mekunu/Shaheen/Tej | 14-39°C; **40°C+ summer + sandstorms + 2008/2009 Manama flooding** | 8-49°C **among hottest inhabited capitals**; **50°C+ summer + sandstorms (Toz/shamal)** | Amman semi-arid altitude 4-32°C; **among most water-poor globally** |
| Healthcare | MoH + mandatory private (Dhamani 2025 phased) + Royal Hospital Muscat / SQU Hospital / Burjeel Muscat | SEHATI + private (King Hamad University Hospital / American Mission Hospital / Bahrain Specialist) | MoH + mandatory private (Afya 2016+) + Al Salam International / Hadi Clinic / New Mowasat | RMS + private (King Hussein Cancer Center / Specialty Hospital / Istishari / Al-Khalidi) — **medical-tourism hub for GCC + Iraq + Syria refugee population** |

🥇 **BH** for **Bahrain Property Visa BHD 200k (~USD 530k) 10-yr renewable + Golden Residency Decree 16/2022** + lowest property-visa threshold among GCC + Saudi Causeway integration drives weekend foot-traffic; quieter than UAE, accessible commercial scale
🥈 **OM** for **Vision 2040 + Royal Decree 89/2021 5-yr/10-yr ITC residency + Long-term Retiree (OMR 4,000/mo)** + cheaper than UAE/QA — at cost of ITC-zone-only constraint and HIGH cyclone exposure
🥉 **JO** for **CBI Jordan since 2018** (JOD 750k bond → passport — but WEAK passport for mobility plays, rational mainly for diaspora reconnection / GCC business utility); **Investor Residence ≥JOD 200k Greater Amman** alternative; medical-tourism hub
4️⃣ **KW** only for those willing to accept **NO real estate ownership for foreigners** — residency entirely via employment Iqama, citizenship effectively impossible; among the most restrictive globally

**Confidence**: MEDIUM — OM RD 89/2021 ITC tier thresholds verified at MoCIIP; BH Decree 6/2017 + 16/2022 verified at NPRA; KW restrictive regime stable since Decree-Law 74/1979; JO CBI 2018 program tiers verified at Investment Commission. Verify all four with issuing authority before action.

### Example N — IN vs NG vs KE for largest non-OECD-OECD-rule-of-law markets (population × economic depth)

| Metric | IN | NG | KE |
|---|---|---|---|
| Population | ~1.428B (Mumbai 21M / Delhi NCR 33M / Bengaluru 13M) | ~218M (Lagos 22M largest African city) | ~55M (Nairobi Metro 5M, Mombasa 1.4M) |
| Foreign-buyer access | **Foreign-buyer residential ban for non-NRI/non-OCI per FEMA 2018 Sch.I**; agricultural / plantation / farmhouse barred even for NRIs/OCIs | **Land Use Act 1978 — all land vested in state Governor** — only Statutory Right of Occupancy 99-yr leasehold; Governor's consent required for transfers | Open to foreigners (residential freehold); **agricultural land restricted to citizens per Constitution Art. 65**; 99-yr leasehold cap on non-citizen freehold-equivalents |
| Total acquisition cost | ~7-12% (stamp duty 5-8% state-varied + registration 1% + GST 5-12% on under-construction + brokerage 1-2%) | ~10-15% (stamp duty + Governor's consent fee + agent + legal — varies by state) | ~7-12% (4% stamp duty + 0.1% LRA + agent 1.5-3% + legal 1-2%) |
| Personal income tax | Worldwide for residents (>182 days); progressive 0-30% + surcharge + 4% cess; **LRS USD 250k/yr outbound cap** | Worldwide for residents (>183 days); progressive 7-24% + 2.5% NHF | Worldwide for residents (>183 days OR ≥122d × 3yr); progressive 10-35% PIT |
| CGT on resale | Long-term (>24 months) 20% with indexation OR 12.5% without; short-term per slab | CGT: the flat 10% charge was repealed by the Nigeria Tax Act 2025 — chargeable gains taxed as income from 1 Jan 2026 | CGT 15% flat (post-2023 reform; verify KRA) |
| Visa pathway | **NO golden-visa via real estate (UNIQUE absence)** — OCI lifetime multi-entry for Indian-origin descendants only | **NO golden-visa via real estate** — STR-1 Investor visa USD 100k business is the pathway | **NO golden-visa via real estate (UNIQUE absence in EAC)** — **Class K Resident KES 200k+/yr passive** is the practical retiree pathway |
| Path to citizenship | Naturalization 11+yr (very strict); **dual citizenship NOT allowed** | Naturalization 15+yr + Nigerian language + dual NOT allowed for native-born | Citizenship 7yr + Swahili (dual allowed since 2010) |
| English | Official + universal in business + legal + healthcare | Official + Pidgin universal + Yoruba/Igbo/Hausa | Co-official with Kiswahili |
| Internet | Jio / Airtel / Vi 5G rapid 2024-26 rollout to top 100 cities; Bengaluru / Mumbai / Hyderabad gigabit fiber growing | MTN / Glo / Airtel / 9mobile 5G limited Lagos/Abuja; **energy autonomy mandatory** (generators + solar) | Safaricom 5G + Airtel + Telkom; **M-PESA universal in admin (unique to KE)**; Nairobi fibre via JTL/Zuku |
| Healthcare | PMJAY public + extensive private (Apollo / Fortis / Max / Manipal — JCI flagship Bangalore/Hyderabad/Mumbai); **medical-tourism destination** | NHIA limited + mandatory private for expats (Reddington / Lagoon / LUTH / First Cardiology — Lagos VI/Ikoyi); medivac to ZA/UK/UAE | NHIF + SHIF (2024-25 reform) + private (Aga Khan University Hospital / Karen / Nairobi / MP Shah); medivac to ZA/UK |
| Climate | Mumbai 18-33°C / Delhi NCR 7-43°C + PM2.5 / Bengaluru altitude-moderated / Kerala monsoon | Lagos tropical-humid 22-32°C + flooding / Abuja FCT savanna 18-31°C / Kano Sahel 13-39°C | Nairobi altitude-moderated 11-26°C "City in the Sun" / Mombasa coastal 22-32°C |
| Coworking | **Bengaluru densest coworking ecosystem in South Asia (100+)** + Mumbai / Delhi NCR / Hyderabad / Pune | Lagos VI/Ikoyi 25-40 (Workstation / Capital Square / Workbench) + Abuja growing | Nairobi 30-50 (iHub / Nailab / Workstyle / The Mint Hub — Westlands / Karen / Kilimani) |
| Currency | INR RBI-managed float (gradual depreciation 70-90 INR/USD 2020-2026) | NGN devaluation cycle 2023-24 catastrophic ~70% loss vs USD post-Tinubu reforms | KES BCK-managed float (relatively stable; M-PESA reduces some FX friction) |

🥇 **IN** for **English-fluent + tech-deep market** (Bengaluru / Hyderabad / Pune SAAS hub) + medical-tourism + densest coworking ecosystem in South Asia; accept: NO golden-visa, foreign-buyer residential ban for non-NRI/non-OCI, LRS USD 250k/yr cap, naturalization 11+yr strict + dual citizenship NOT allowed
🥈 **KE** for **Nairobi expat infrastructure** (Karen British-cultural roots + Aga Khan University Hospital flagship) + altitude-moderated climate + M-PESA universal + Class K Resident permit (KES 200k+/yr passive); accept: NO golden-visa via property, agricultural land citizen-only constitutional restriction
🥉 **NG** only for **diaspora-engagement or specific business pull** (Lagos 22M largest African city + tech ecosystem Yaba / Ikeja) — accept: Land Use Act 1978 leasehold-only structure, NGN devaluation 2023-24 catastrophic, security risk requires private security + gated communities + energy autonomy mandatory

**Confidence**: MEDIUM — IN FEMA 2018 Sch.I verified at RBI; NG Land Use Act 1978 stable; KE Constitution Art. 65 agricultural-land restriction verified; cgt rates and pathway thresholds drift annually — verify at issuing authority.

### Example O — JO vs LB for Levant residency (CBI vs collapse-recovery)

| Metric | JO | LB |
|---|---|---|
| Foreign-buyer access | Open subject to Council-of-Ministers approval >threshold; ≤4,000 m² agricultural barred | Open to most foreigners; ≤3,000 m² aggregate Beirut / ≤10,000 m² Mount Lebanon / coastal limits; Council-of-Ministers approval for >limits; Lebanese-descent buyers exempt |
| Personal income tax | Worldwide for residents progressive 5-30% + 1% national-contribution | Worldwide for residents progressive 4-25% PIT |
| Visa pathway | **CBI Jordan since 2018** — JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport (~50 visa-free — WEAK passport for mobility); **Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable)**; Aqaba ASEZ separate framework | NO golden-visa via real estate; **Investor Residency ≥USD 50k Lebanese business (1-yr renewable)**; property ownership ≥USD 200k can support residency application but not automatic; **Lebanese descent streamlined naturalization** (~13M Mahjar diaspora); dual citizenship since 2007 |
| Currency | JOD pegged USD 0.708 since Oct 1995 (stable vs USD) | **LBP catastrophic collapse 2019-2026** — official vs Sayrafa vs parallel rate triple-tier; banking-sector restrictions on USD withdrawals + transfers |
| Geopolitics | Stable monarchy; large Iraqi+Syrian+Palestinian diaspora; among most water-poor globally | **Post-2019 banking collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war Sep-Nov 2024**; healthcare collapse; Touch + Alfa 4G ageing — **NO 5G yet** |
| Healthcare | RMS + private (KHCC / Specialty / Istishari / Al-Khalidi) — **medical-tourism hub for GCC + Iraq + Syria** | Historically AUB Medical Center / Hôtel-Dieu de France / Clemenceau / Saint George — **post-2019 collapse** + currency dual-pricing; medivac to CY/IT/FR for fresh-USD-paying patients |
| Population | ~11.4M (Amman Metro 4.5M, Zarqa 1.5M, Irbid 1.9M, Aqaba 200k) | ~5.5M (incl ~1.5M Syrian + ~470k Palestinian refugees) — Beirut Metro 2.4M; ~13M global Mahjar diaspora dwarfs domestic |
| Climate | Amman semi-arid altitude (~750m) 4-32°C; Aqaba Red Sea / Dead Sea -430m unique | Beirut Mediterranean 11-30°C / Mount Lebanon altitude-cooler / Cedars ski-zone 1,800-3,000m **only Middle Eastern country with skiing** |
| Languages | Arabic + English business/tourism/medical (English-medium hospitals) + French educated diaspora | Arabic + French de facto + English in tech/business/healthcare + Armenian Bourj Hammoud — historically trilingual |

🥇 **JO** for **stable JOD-USD peg + CBI 2018 (JOD 750k bond → passport for diaspora reconnection / GCC business utility — accept WEAK passport for mobility plays) + medical-tourism hub for GCC + Iraq + Syria + Investor Residence ≥JOD 200k Greater Amman alternative**; among most water-poor globally — material long-term risk
🥈 **LB** ONLY for **Lebanese-descent applicants** wanting streamlined naturalization (~13M Mahjar diaspora) OR **fresh-USD earners** willing to navigate post-2019 banking collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war + USD-LBP dual-pricing + healthcare collapse since 2019; foreign-buyer cohort dominated by Lebanese diaspora returnees (US/CA/AU/FR/BR/AR Mahjar dominant)

**Confidence**: MEDIUM — JO CBI 2018 thresholds verified at Investment Commission; LB regulatory environment dynamic post-2024 war + ongoing IMF discussions; banking collapse 2019-2026 still unresolved as of May 2026.

## Limitations

- **Not predictive**: comparison is current-state, not 5-year-forward
- **Not personalized**: doesn't know user's age, citizenship, financial profile — those go via `--journey=<type>` overlay
- **Doesn't replace local advice**: every shortlist needs a local notary/lawyer/tax adviser before committing
- **No scored "livability index"**: the skill deliberately does NOT emit a single composite livability / quality-of-life score — subjective criterion-weighting is false precision (English-friendliness, for one, is only an EF-EPI country-tier). For day-to-day fit, run a **no-composite side-by-side** instead: `--compare <countries> --criteria=climate,crime,amenities,connectivity`, add `--demographics` § Integration environment for the sourced policy-level signal, and use `--match` when you want a cohort-weighted ranking where *you* set the weights.

## Status

Last refreshed: 2026-05-01 (Tier-5 additions — 87 countries total; Tier-5 added: IN, NG, KE, JO, OM, BH, KW, LB).
