# Universal `--demographics` Section

Population, aging, schools, family-friendly metrics across 87 supported countries (44 original + 10 Tier-1 + 8 Tier-2 + 9 Tier-3 + 8 Tier-4 + 8 Tier-5). Useful for relocation/family decisions and long-term valuation outlook.

**Snapshot**: May 2026 (Tier-5 additions).

## Universal contract

For the property's country, return:
1. **Population** (latest official; trend last 5 years)
2. **Median age + dependency ratio**
3. **Net migration rate** (per 1k pop)
4. **Fertility rate** (TFR, latest)
5. **PISA / school-system rank** (last assessment)
6. **English proficiency (EF EPI)** (where applicable)
7. **Family-friendliness composite** (parental leave, childcare cost, school quality)

## Output template

```markdown
## Demographics Profile

**Country**: <ISO2>
**Population**: <X> (trend: ↑↓→)
**Median age**: <X> yrs
**Net migration rate (per 1k)**: <X>
**Fertility rate (TFR)**: <X>
**PISA reading/math/science rank (latest)**: <X>
**EF EPI English proficiency rank**: <X>
**Family-friendliness composite**: <verdict>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## Authoritative sources

- **Eurostat demography**: https://ec.europa.eu/eurostat/web/population-demography
- **OECD population stats**: https://data.oecd.org/pop/population.htm
- **World Bank Open Data**: https://data.worldbank.org/
- **UN World Population Prospects**: https://population.un.org/wpp/
- **PISA**: https://www.oecd.org/pisa/ (last cycle: 2022, published Dec 2023; next: 2025 results late 2026)
- **EF EPI English Proficiency Index**: https://www.ef.com/wwen/epi/

## Per-country snapshot (Apr 2026)

### Western Europe

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| FR | 68.4 | 42.0 | 1.79 | 474 | Moderate | Strong (free public childcare from age 3, generous parental leave) |
| IT | 58.8 | 47.3 | 1.20 | 482 | Moderate | Mid (childcare costs vary; Mezzogiorno underfunded) |
| ES | 48.5 | 44.5 | 1.16 | 474 | Moderate | Mid (free public schools, weak childcare 0-3) |
| PT | 10.5 | 46.0 | 1.43 | 477 | High | Mid (rising costs in Lisbon) |
| DE | 84.7 | 45.0 | 1.46 | 480 | Very High | Strong (Elterngeld, Kita expansion ongoing) |
| AT | 9.1 | 43.8 | 1.32 | 480 | Very High | Strong (Karenzgeld, kindergarten universal) |
| CH | 8.9 | 42.7 | 1.39 | 483 | Very High | Mid (school OK; childcare expensive) |
| NL | 17.9 | 42.3 | 1.49 | 459 (down) | Very High | Strong (kinderbijslag, kraamzorg, English-friendly) |
| BE | 11.8 | 41.9 | 1.55 | 467 | Very High | Strong (free childcare, language matters region-by-region) |
| LU | 0.66 | 39.7 | 1.30 | 465 | Very High | Strong (multilingual schools; high costs) |
| IE | 5.3 | 38.6 | 1.54 | 516 (top tier) | Native | Strong (English, strong public schools) |
| UK | 67.5 | 40.7 | 1.49 | 494 | Native | Strong public schools, expensive childcare |

### Iberia/Mediterranean

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| GR | 10.4 | 46.0 | 1.32 | 438 | High | Mid (crisis-impacted public schools) |
| MT | 0.55 | 41.4 | 1.13 | 448 | Very High | Mid (small system; English-medium top schools) |
| CY | 0.92 | 38.4 | 1.40 | 442 | High | Mid (private school dominant for English) |

### Northern Europe / Baltics

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| SE | 10.6 | 41.1 | 1.45 | 487 | Very High | Excellent (1+1yr parental leave, free childcare) |
| FI | 5.6 | 43.5 | 1.32 | 488 | Very High | Excellent (Finnish school model) |
| NO | 5.6 | 39.8 | 1.40 | 477 | Very High | Excellent (kontantstøtte, foreldrepermisjon) |
| DK | 5.96 | 42.1 | 1.50 | 489 | Very High | Excellent (barselsdagpenge, vuggestue universal) |
| IS | 0.39 | 37.8 | 1.59 | 460 | Very High | Excellent (highest TFR in Nordic; small population) |
| EE | 1.37 | 43.4 | 1.31 | 511 (top) | Very High | Strong (digital-native schools; vanemahüvitis) |
| LV | 1.85 | 44.5 | 1.36 | 475 | High | Mid (compulsory land lease + restitution affect family planning) |
| LT | 2.83 | 45.0 | 1.27 | 472 | High | Mid (declining pop; Vilnius growing) |

### CEE

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| PL | 38.2 | 42.0 | 1.16 | 489 | Moderate | Mid (500+ child benefit, Czyste Powietrze housing) |
| CZ | 10.6 | 43.4 | 1.71 | 492 | Moderate | Strong (3yr parental leave, mateřská) |
| SK | 5.4 | 41.7 | 1.61 | 466 | Moderate | Mid (rodičovský príspevok) |
| SI | 2.1 | 44.7 | 1.60 | 469 | High | Strong (porodniški dopust 1yr, free state preschool from age 1) |
| HR | 3.85 | 44.3 | 1.46 | 475 | High | Mid (declining pop esp. in interior) |
| HU | 9.6 | 43.4 | 1.59 | 473 | Moderate | Strong (CSOK Plusz, large-family bonuses) |
| RO | 19.0 | 43.6 | 1.81 | 428 | Moderate | Mid (rural schools weak; Bucharest/Cluj/Iași strong) |
| BG | 6.4 | 45.4 | 1.65 | 404 | Moderate | Mid (pop declining; Black Sea coast inflated by tourism) |

### Western Balkans

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| RS | 6.6 | 44.4 | 1.49 | 440 | Moderate | Mid |
| ME | 0.62 | 39.9 | 1.69 | 405 | Moderate | Mid (coast premium) |
| BA | 3.2 | 43.9 | 1.30 | 403 | Moderate | Mid (entity-level differences) |
| MK | 1.83 | 41.0 | 1.45 | 358 | Moderate | Lower (PISA bottom of EU candidate region) |
| AL | 2.7 | 36.9 | 1.32 | 358 | Lower | Lower (improving since 2020) |

### Anglo non-EU

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| US | 333 (2024 Census Bureau est.) | 38.9 (2023 ACS) | 1.66 (2023 NCHS, provisional) | 504 (PISA 2022) / math 465 | Native | Mid (no federal paid parental leave; childcare ~22% of median household income — Treasury 2023) |
| CA | 40.6 | 41.9 | 1.30 | 507 | Native | Strong (CCB, parental leave, universal healthcare) |
| AU | 26.7 | 38.0 | 1.50 | 498 | Native | Strong (paid parental leave, universal healthcare) |
| NZ | 5.3 | 38.0 | 1.52 | 501 | Native | Strong (universal early-childhood, paid leave) |

### Latin America

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| MX | 130.6 | 30.5 | 1.81 | 415 | Moderate | Mid (informal sector dominant; INFONAVIT housing benefits) |
| BR | 215.3 | 33.5 | 1.62 | 410 | Moderate | Mid (public schools weak; private dominant) |
| AR | 46.0 | 32.7 | 1.50 | 401 | High | Mid (post-Milei austerity affecting public services) |
| CR | 5.2 | 35.6 | 1.49 | 415 | Moderate | Strong public schools relative to LatAm; bilingual private exists |
| PA | 4.5 | 31.4 | 2.18 | 392 | Moderate | Mid (US-influenced bilingual private schools strong) |
| DO | ~11.3 (2024 ONE est.) | ~28 | 2.3 (2023 World Bank) | not in PISA — UNESCO LLECE 2019: below LatAm avg | Lower-Moderate | Mid (private bilingual schools dominant in Santo Domingo/Punta Cana; public underfunded) |
| CO | ~52.3 (2024 DANE) | ~31 | 1.7 (2023 DANE) | 409 reading (PISA 2022) | Moderate | Mid (public schools variable; Bogotá/Medellín private strong) |
| UY | ~3.4 (2024 INE) | ~36 | 1.5 (2023 MSP) | 430 reading (PISA 2022) | High | Strong (Plan Ceibal 1-laptop-per-child, free public university, 14-week paid maternity leave) |
| CL | ~19.6 (2024 INE) | ~36 | 1.5 (2023 INE, record-low) | 448 reading (PISA 2022, top in LatAm) | Moderate | Mid (school-quality gap public vs private severe; 24-week postnatal leave) |
| PE | ~34 (2024 INEI mid-year) | ~30 (2024 INEI) | ~2.2 est. (2023 INEI, declining toward replacement) | 408 reading (PISA 2022) | Moderate | Mid (98-day maternity leave; Spanish + Quechua/Aymara public; private bilingual concentrated in Lima Miraflores/Barranco/San Isidro) |
| EC | ~17.7 (2024 INEC mid-year est. — Censo 2022 final 16.9M) | ~29 (2024 INEC) | ~2.0 est. (2023 INEC, near replacement) | 411 reading (PISA 2022) | Moderate | Mid (12-week maternity leave; Spanish + Kichwa/Shuar public; 2024 violent crime peak Guayaquil/Esmeraldas/Manta affecting family relocation; emigration acceleration since 2022) |
| PY | ~7.4 (2024 INE) | ~27 (2024 INE, youngest in S. America after Bolivia) | ~2.4 est. (2023 INE, above replacement) | not in PISA — ERCE 2019: below LatAm avg | Moderate | Mid (18-week maternity leave; Spanish + Guaraní co-official; bilingual schooling routine; demographic dividend window through ~2040) |

### Caucasus

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| GE | ~3.7 (2024 Geostat) | ~38 | 1.7 (2023 Geostat, declining from 2.0 in 2019) | 374 reading (PISA 2022) | Moderate | Mid (730-day maternity leave on paper, low cash value; emigration steady — net migration negative since 2010s per Geostat) |
| AM | ~2.78 (2024 ARMSTAT) | ~37 (2024 ARMSTAT) | ~1.6 est. (2023 ARMSTAT, declining) | not in PISA — TIMSS 2019: mid-band | High (Russian + English business; IT-driven) | Mid (140-day maternity leave; Armenian Eastern official; ~7M global diaspora structural FX/talent inflow; Yerevan IT-sector concentrating talent) |
| AZ | ~10.16 (2024 SSC) | ~33 (2024 SSC) | ~1.7 est. (2023 SSC, declining) | not in PISA — TIMSS 2019: below international median | Moderate (Azerbaijani Latin + Russian widely + English business + Turkish) | Mid (126-day maternity leave; ASAN Service efficient governance; SOFAZ buffer → fiscal stability for family policy; private bilingual concentrated Baku) |

### Middle East / Levant / Gulf

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| TR | ~85.4 (2024 TÜİK) | ~33.5 (2023 TÜİK) | 1.51 (2023 TÜİK, record-low) | 456 reading (PISA 2022) | Lower | Mid (16-week maternity leave; declining TFR; private bilingual schools dominate top tier) |
| AE | ~10.2 (2024 FCSC est.) | ~33 (skewed by ~88% expat workforce, FCSC 2022) | 1.4 (2023 World Bank, Emirati TFR higher ~3) | 417 reading (PISA 2022) | Moderate | Mid (private international schools dominant — 60%+ of students per KHDA Dubai; childcare market-rate; positive net migration) |
| IL | ~9.84 (2024 CBS) | ~30.5 (2023 CBS) | 2.89 (2023 CBS, highest in OECD) | 474 reading (PISA 2022) | Very High | Strong (15-week paid maternity leave; ultra-Orthodox/Haredi TFR ~6.5 drives aggregate; Hebrew/Arabic public; English-medium private) |
| QA | ~3.05 (2024 PSA) | ~33 (skewed by ~88% expat workforce, PSA 2024) | ~1.8 est. (2023 PSA — Qatari TFR higher ~2.7, expat lower) | not in PISA — Qatar participated 2018 (407 reading); 2022 cycle data not published nationally | Moderate (Arabic + English business widely) | Mid (50-day maternity leave for nationals + 60-day for expats; private international schools dominant for expat family pattern; positive net migration) |
| SA | ~36.4 (2024 GASTAT) | ~31 (2024 GASTAT) | ~2.4 est. (2023 GASTAT, declining from 3.5 in 2010) | 419 reading (PISA 2022) | Moderate (Arabic + English business widely under Vision 2030) | Mid (10-week maternity leave; gender-segregated public schools historically; private international schools growing in Riyadh + Jeddah; Vision 2030 reforming workforce participation) |
| JO | ~11.4 (2024 DOS, including refugees) | ~24 (2024 DOS, young) | ~2.6 est. (2023 DOS, declining from 3.5 in 2010) | 342 reading (PISA 2022) | Moderate (Arabic + English business widely) | Mid (10-week maternity leave; public schools strained by Syrian refugee influx; private international + IB schools growing in Amman west — Abdoun, Sweifieh) |
| OM | ~5.0 (NCSI 2024) | ~30 (skewed by ~46% expat workforce, NCSI 2024) | ~2.5 est. (2023 NCSI — Omani TFR higher, expat lower) | not in PISA — Oman last participated 2015 (373 reading) | Moderate (Arabic + English business widely under Vision 2040) | Mid (50-day maternity leave; gender-segregated public schools historically; private international schools growing in Muscat — Madinat Sultan Qaboos, Qurum, Shatti Al Qurum; Vision 2040 reforming) |
| BH | ~1.49 (iGA 2024) | ~33 (skewed by ~55% expat workforce, iGA 2024) | ~1.8 est. (2023 iGA — Bahraini TFR ~2.5, expat lower) | not in PISA — Bahrain participated 2022 (414 reading) | Moderate (Arabic + English business widely) | Mid (60-day maternity leave; mixed-gender public schools at primary; private international schools dominant for expat family pattern in Manama / Saar / Janabiya / Riffa) |
| KW | ~4.85 (2024 PACI) | ~30 (skewed by ~70% expat workforce, PACI 2024) | ~2.0 est. (2023 PACI — Kuwaiti TFR higher ~2.5, expat lower) | not in PISA — Kuwait participated 2022 (363 reading) | Moderate (Arabic + English business widely) | Mid (70-day maternity leave for nationals; gender-segregated public schools; private international schools dominant for expat family pattern in Salwa, Mishref, Bayan, Salmiya) |
| LB | ~5.5 (CAS estimate, incl ~1.5M Syrian + ~470k Palestinian refugees) | ~33 (CAS estimate) | ~2.0 est. (CAS — declining; emigration accelerated post-2019) | not in PISA — Lebanon participated 2022 (353 reading) | High (Arabic + French + English trilingual elite) | Lower (10-week maternity leave; public schools severely strained — 2019 economic collapse + 2024 Israel-Hezbollah war + 2020 Beirut Port explosion; private French/American schools dominant — IC International College Ras Beirut, ACS, LAU, AUB feeders) |

### MENA — North Africa

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| MA | ~37.9 (2024 HCP census) | ~30 (2024 HCP) | 2.1 (2023 HCP, declining from 2.5 in 2010) | 339 reading (PISA 2022, near-bottom of participants) | Lower | Mid (14-week maternity leave; French/Arabic public schools; private French/American dominant in Casablanca/Rabat) |
| EG | ~110 (2024 CAPMAS) | ~25 (2024 CAPMAS) | 2.85 (2023 CAPMAS, declining from 3.5 peak 2014) | not in PISA — TIMSS 2019: below international median | Lower | Lower (4-month maternity leave; public schools severely under-resourced; private/IGCSE/American schools dominant in Cairo elite) |
| TN | ~12.07 (2024 INS) | ~33 (2024 INS) | ~2.0 est. (2023 INS, near replacement) | 365 reading (PISA 2022) | Lower (Arabic + French in business/legal) | Mid (30-day maternity leave — short by region; French-Arabic bilingual public; Tunis private French/American schools dominant for elite; IMF EFF SUSPENDED Mar 2024 affecting public-sector funding) |

### Sub-Saharan Africa

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| ZA | ~62.0 (2024 Stats SA mid-year est.) | ~28 (2024 Stats SA) | 2.3 (2023 Stats SA) | not in PISA — TIMSS 2019: bottom quartile | Moderate | Mid (4-month maternity leave at UIF rate; public schools highly variable, top quintile-5 strong; HIV-affected adult mortality skews age structure per Stats SA) |
| NG | ~227 (UN 2024 proj — 2006 was last full census) | ~17 (UN 2024 proj, youngest among major countries) | ~5.0 est. (2023 UN, declining from 6+ in 2010) | not in PISA — TIMSS not participated; UNESCO TLO data limited | Moderate (English official + 500+ languages + Pidgin universal) | Lower (12-week maternity leave; public schools severely under-resourced + insurgency-affected NE; private international schools dominant in Lagos VI/Ikoyi/Lekki — Greensprings, BIS, AISL, ALC; Boko Haram NE/ISWAP Lake Chad/IPOB SE/banditry NW affect family relocation) |
| KE | ~55 (KNBS 2024 — 2019 census 47.6M) | ~20 (KNBS 2024) | ~3.3 est. (2023 KNBS, declining from 4 in 2010) | not in PISA — TIMSS not participated; SACMEQ data limited | High (English official + Kiswahili) | Mid (3-month maternity leave; public schools variable — CBC reform ongoing; private international + IB schools growing in Nairobi Westlands/Karen/Kilimani — Braeburn, Hillcrest, ISK, Brookhouse; al-Shabaab cross-border NE Kenya — Garissa/Mandera/Wajir affect family relocation; M-PESA mobile money 95%+ adoption) |

### East Asia

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| JP | ~123.8 (2024 Stat Bureau) | 49.4 (2024 Stat Bureau, oldest globally) | 1.20 (2024 MHLW, record-low) | 516 reading (PISA 2022, top tier) | Lower | Strong (1-yr paid parental leave; universal childcare expanding under Kishida policy; population declining ~600k/year per MHLW) |
| KR | ~51.7 (2024 KOSTAT) | ~45 (2024 KOSTAT) | 0.72 (2024 KOSTAT, lowest globally) | 515 reading (PISA 2022, top tier) | High | Strong on paper (1-yr paid leave + childcare subsidies; Yoon-era population emergency framework) but TFR collapse signals mismatch — work culture + housing cost in Seoul/Pangyo/Gangnam structural |
| TW | ~23.4 (2024 DGBAS) | ~44 (2024 DGBAS) | 0.87 (2023 MOI, well below replacement) | 515 reading (PISA 2022, top tier) | High | Mid (8-week maternity leave + parental allowance; aging fast; Taipei international-school tier strong; geopolitical-risk premium for relocation decisions) |
| HK | ~7.5 (2024 C&SD) | ~46 (2024 C&SD) | 0.75 (2023 C&SD, near-lowest globally) | 535 reading (PISA 2022 — Hong Kong is separate jurisdiction at PISA, top-tier) | Very High | Mid (14-week maternity leave; aging fast; English co-official; international-school tier strong but expensive; Article 23 NSL Mar 2024 sentiment factor for foreign families) |
| MO | ~0.673 (2024 DSEC) | ~42 (2024 DSEC) | 0.7 est. (2023 DSEC, near-lowest in region) | not in PISA — DSEC Education indicators only | High | Mid (Cantonese majority + Portuguese co-official + Mandarin growing; small system; international tier limited; gaming-economy structures family work patterns) |

### South-East Asia

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| TH | ~71.7 (2024 NSO) | ~40 (2024 NSO) | 1.3 (2023 NSO, well below replacement) | 379 reading (PISA 2022) | Lower | Mid (98-day maternity leave; aging fastest in SE Asia; rural public schools weak, Bangkok international tier strong) |
| ID | ~281 (2024 BPS) | ~30 (2024 BPS) | 2.1 (2023 BPS, at replacement) | 359 reading (PISA 2022) | Lower | Mid (3-month maternity leave; demographic dividend window through ~2030 per BPS; quality gap urban-rural severe) |
| MY | ~34.1 (2024 DOSM) | ~30 (2024 DOSM) | 1.6 (2023 DOSM, declining) | 388 reading (PISA 2022) | High | Mid (60-day maternity leave; multi-ethnic system Malay/Chinese/Tamil-medium public; private international tier strong in KL/Penang) |
| VN | ~100.3 (2024 GSO) | ~33 (2024 GSO) | 1.95 (2023 GSO, declining toward replacement) | 462 reading (PISA 2022, strong relative to peers) | Lower | Mid (6-month paid maternity leave — generous regionally; aging from a young base, "old before rich" risk per GSO) |
| PH | ~115 (2024 PSA) | ~25.7 (2024 PSA, youngest in SE Asia) | 2.7 (2023 PSA) | 347 reading (PISA 2022) | High | Mid (105-day paid maternity leave; English-medium public schools but quality variable; OFW remittances structure family economics) |
| SG | ~5.94 (2024 Singstat) | ~42.8 (2024 Singstat) | 0.97 (2023 Singstat, record-low) | 543 reading (PISA 2022, #1 globally) | Very High (English working language) | Strong (16-week paid maternity + 4-week paternity; MOE schools top-tier globally; childcare subsidies + Baby Bonus scheme; aging fast — citizen TFR ~0.97 below replacement long-term per Singstat) |

### South Asia

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| IN | ~1,428 (UN 2024 proj — 2011 last full census, 2021 census deferred to 2025-26) | ~28 (UN 2024 proj) | ~2.0 (2021 NFHS-5, at replacement; declining from 2.7 in 2005) | not in PISA — India withdrew after 2009; ASER + NAS national alternatives | High (English official + Hindi + 21 other scheduled languages; English-medium schooling routine for elite + middle class) | Mid (26-week maternity leave under Maternity Benefit Amendment Act 2017 — generous regionally; public schools severely variable; private CBSE/ICSE/IB/Cambridge schools dominant for elite in Bengaluru/Mumbai/Delhi-Gurgaon-Noida; demographic dividend window through ~2050 per UN; India Stack Aadhaar + UPI + DigiLocker + ONDC digital infrastructure) |

### European microstates / non-EU enclaves (Tier-3)

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| LI | ~0.040 (2024 Statistik Liechtenstein) | ~44 (2024 SL) | ~1.4 est. (2023 SL) | not in PISA — SL Education indicators only | Very High (German + English) | Strong (CHF-bound, generous family allowances; small system; German Alemannic dialect official; cross-border CH/AT schooling routine) |
| AD | ~0.085 (2024 Estadística d'Andorra) | ~44 (2024 EA) | ~1.1 est. (2023 EA) | not in PISA — three school systems (Andorran, French, Spanish) | High | Mid (Catalan official; tri-system schooling; small economy ski + retail + finance; family-friendly relative to size) |
| MC | ~0.038 (2024 IMSEE) | ~55 est. (2024 IMSEE — among oldest globally; HNW-skewed) | ~1.5 est. (2023 IMSEE) | not in PISA — small system | Very High (French + English) | Mid (French official; private/international schools dominant for expat HNW families; ultra-HNW property structure) |

### Eastern Europe non-EU (Tier-3)

| Country | Pop (M) | Median age | TFR | PISA reading | EF EPI tier | Family-friendly |
|---|---:|---:|---:|---:|---|---|
| MD | ~2.5 (2024 BNS, excl. Transnistria) | ~38 (2024 BNS) | 1.7 (2023 BNS) | 411 reading (PISA 2022) | Moderate | Mid (24-month parental leave; Russian + Romanian-medium public schools split; emigration sustained — net migration negative since 1990s; EU candidate Jun 2022 → accession negotiations Jun 2024 may reverse) |

## Aging & dependency cliffs

Countries already past the demographic peak (population declining), highest concern:
- 🇯🇵 JP (49.4, 1.20) — oldest median globally; ~600k pop loss/year (2024 MHLW)
- 🇰🇷 KR (~45, 0.72) — TFR lowest globally (2024 KOSTAT); structural population decline since 2020
- 🇭🇰 HK (~46, 0.75) — TFR among lowest globally (2023 C&SD); aging fast
- 🇲🇴 MO (~42, 0.7 est.) — TFR near-lowest in region (2023 DSEC)
- 🇹🇼 TW (~44, 0.87) — TFR well below replacement (2023 MOI); aging fast
- 🇸🇬 SG (~42.8, 0.97) — TFR record-low (2023 Singstat); aging fast
- 🇮🇹 IT (median 47.3, TFR 1.20) — accelerating decline
- 🇧🇬 BG (45.4, 1.65) — emigration overlay
- 🇭🇷 HR (44.3, 1.46)
- 🇵🇹 PT (46.0) — rural depopulation severe
- 🇱🇻 LV (44.5) — emigration to Western EU
- 🇱🇹 LT (45.0) — emigration to Western EU
- 🇷🇸 RS (44.4) — emigration
- 🇲🇩 MD (~38, 1.7) — emigration sustained since 1990s (2024 BNS)
- 🇹🇭 TH (~40, 1.3) — fastest-aging in SE Asia; record-low TFR (2023 NSO)
- 🇬🇪 GE (~38, 1.7) — emigration sustained (2024 Geostat)

Countries with stable / growing demographics:
- 🇮🇱 IL (30.5, 2.89) — highest TFR in OECD (2023 CBS)
- 🇪🇬 EG (~25, 2.85) — high TFR but declining (2023 CAPMAS)
- 🇵🇭 PH (25.7, 2.7) — youngest median in skill (2024 PSA)
- 🇩🇴 DO (~28, 2.3) — replacement-plus
- 🇿🇦 ZA (~28, 2.3) — high TFR but HIV-affected adult mortality (2024 Stats SA)
- 🇲🇦 MA (~30, 2.1) — at replacement
- 🇮🇩 ID (~30, 2.1) — demographic dividend window through ~2030 (2024 BPS)
- 🇻🇳 VN (~33, 1.95) — declining toward replacement
- 🇮🇪 IE (38.6, 1.54) — strong inbound migration + native growth
- 🇮🇸 IS (37.8, 1.59) — youngest median in skill
- 🇨🇭 CH (42.7, 1.39) — net migration positive
- 🇱🇺 LU (39.7, 1.30) — cross-border + EU staff inflow
- 🇲🇽 MX (30.5, 1.81) — youngest in skill (LatAm)
- 🇵🇦 PA (31.4, 2.18) — TFR above replacement!
- 🇨🇦 CA (41.9, 1.30) — large immigration uplift
- 🇺🇸 US (38.9, 1.66) — net migration positive (2024 Census Bureau)
- 🇦🇪 AE (~33, 1.4) — expat-driven, ~88% non-citizen workforce (2022 FCSC)
- 🇶🇦 QA (~33, 1.8) — expat-driven, ~88% non-citizen workforce (2024 PSA)
- 🇸🇦 SA (~31, 2.4) — Vision 2030 demographic dividend; declining TFR but still above replacement
- 🇵🇪 PE (~30, 2.2) — declining toward replacement
- 🇪🇨 EC (~29, 2.0) — at replacement
- 🇵🇾 PY (~27, 2.4) — youngest among Tier-4; demographic dividend through ~2040
- 🇦🇲 AM (~37, 1.6) — declining; ~7M diaspora overlay structural
- 🇦🇿 AZ (~33, 1.7) — declining
- 🇹🇳 TN (~33, 2.0) — at replacement; declining
- 🇮🇳 IN (~28, 2.0) — at replacement (NFHS-5 2021); demographic dividend window through ~2050 per UN; world's most populous since 2023
- 🇳🇬 NG (~17, 5.0) — youngest median in skill (UN 2024 proj); high-growth despite declining TFR
- 🇰🇪 KE (~20, 3.3) — young; replacement-plus
- 🇯🇴 JO (~24, 2.6) — young; refugees-driven (Syrian + Palestinian)
- 🇴🇲 OM (~30, 2.5) — Omani TFR replacement-plus, expat-driven aggregate
- 🇧🇭 BH (~33, 1.8) — expat-driven (~55%)
- 🇰🇼 KW (~30, 2.0) — Kuwaiti TFR replacement-plus, expat-driven (~70%) aggregate
- 🇱🇧 LB (~33, 2.0) — declining; emigration accelerated post-2019 economic collapse + 2024 war

## English-proficiency tiers (EF EPI 2025 cycle — non-government, treat as relative ranking)

- **Native**: UK, IE, AU, NZ, CA, US
- **Very High**: NL, AT, BE, FI, SE, NO, DK, DE, LU, IE, EE, MT, IL, SG (English working language), LI, MC
- **High**: PT, GR, CY, SI, HR, LT, LV, AR, MY, PH, UY, KR, TW, HK, MO, AD, AM (IT-driven), KE, IN, LB (FR/EN trilingual elite)
- **Moderate**: FR, IT, ES, PL, CZ, SK, HU, RO, RS, ME, BA, MK, MX, BR, CR, PA, GE, AE, ZA, CO, CL, MD, QA, SA, PE, EC, PY, AZ, JO, OM, BH, KW, NG
- **Lower-Moderate**: DO
- **Lower**: AL, BG (improving), MK (lower), TR, MA, EG, TH, ID, VN, TN

## PISA rank distinction (2022 results published Dec 2023; 2025 cycle results expected late 2026)

Top tier (>500 reading):
- 🇸🇬 SG (543, #1 globally), 🇭🇰 HK (535), 🇮🇪 IE (516), 🇯🇵 JP (516), 🇰🇷 KR (515), 🇹🇼 TW (515), 🇪🇪 EE (511), 🇨🇦 CA (507), 🇺🇸 US (504), 🇳🇿 NZ (501)

Strong tier (480-500):
- Most Nordic + DE/AT/CH/UK

Mid (440-480):
- Most other EU + Anglo non-EU + 🇮🇱 IL (474), 🇻🇳 VN (462), 🇹🇷 TR (456), 🇨🇱 CL (448)

Lower-mid (400-440):
- 🇮🇹 IT, 🇪🇸 ES, 🇬🇷 GR, 🇨🇾 CY, 🇲🇹 MT (small systems), 🇧🇬 BG, 🇷🇴 RO, all Balkans except SI, 🇺🇾 UY (430), 🇲🇩 MD (411), 🇦🇪 AE (417), 🇨🇴 CO (409), 🇸🇦 SA (419), 🇪🇨 EC (411), 🇵🇪 PE (408), 🇶🇦 QA (407 — 2018 cycle, 2022 not published nationally), 🇧🇭 BH (414, PISA 2022)

Lower (<400):
- 🇲🇾 MY (388), 🇹🇭 TH (379), 🇬🇪 GE (374), 🇹🇳 TN (365), 🇰🇼 KW (363, PISA 2022), 🇮🇩 ID (359), 🇱🇧 LB (353, PISA 2022), 🇵🇭 PH (347), 🇯🇴 JO (342, PISA 2022), 🇲🇦 MA (339)
- Not in PISA: 🇩🇴 DO, 🇿🇦 ZA, 🇪🇬 EG, 🇲🇴 MO, 🇱🇮 LI, 🇦🇩 AD, 🇲🇨 MC, 🇵🇾 PY, 🇦🇲 AM, 🇦🇿 AZ, 🇮🇳 IN (withdrew after 2009 — ASER/NAS alternatives), 🇳🇬 NG, 🇰🇪 KE, 🇴🇲 OM (last 2015, 373 reading) — national-level indicators, TIMSS / SACMEQ / national alternatives only

## Family-friendliness composite signals

Strongest (parental leave, free childcare, school quality, work-life balance):
- 🇸🇪 SE, 🇫🇮 FI, 🇩🇰 DK, 🇳🇴 NO, 🇮🇸 IS — Nordic model
- 🇩🇪 DE, 🇦🇹 AT, 🇧🇪 BE, 🇳🇱 NL, 🇫🇷 FR — Continental Europe strong
- 🇮🇪 IE, 🇨🇦 CA, 🇦🇺 AU, 🇳🇿 NZ — Anglo-sphere with social-democratic streak
- 🇸🇮 SI, 🇨🇿 CZ — Surprising Eastern strength
- 🇯🇵 JP — top-tier school quality + recent parental-leave expansion (Kishida policy)
- 🇮🇱 IL — strong family infrastructure + highest TFR in OECD
- 🇻🇳 VN — 6-month paid maternity leave (regionally generous)
- 🇸🇬 SG — top-tier MOE schools (#1 PISA 2022) + 16-week maternity + Baby Bonus, but TFR collapse signals housing-cost / work-culture mismatch
- 🇰🇷 KR — generous on paper (1-yr leave + childcare subsidies + Yoon population emergency framework) but TFR 0.72 lowest globally per KOSTAT 2024 — policy/practice gap severe
- 🇱🇮 LI — CHF-bound generous family allowances (small system)

Mid-tier:
- 🇺🇸 US — strong universities + suburban schools, weak federal family policy (no paid leave; childcare ~22% household income, 2023 Treasury)
- 🇦🇪 AE, 🇲🇾 MY, 🇹🇭 TH — strong international/private school options, public quality variable
- 🇺🇾 UY, 🇨🇱 CL — top in LatAm by school metrics; UY notable for Plan Ceibal
- 🇭🇰 HK, 🇹🇼 TW, 🇲🇴 MO — top-tier school quality but high cost / Article-23 NSL sentiment factor (HK) / geopolitical premium (TW); aging fast
- 🇦🇩 AD — Catalan official, tri-system schooling (Andorran/French/Spanish), small economy
- 🇲🇨 MC — French official, private/international schools dominant for HNW expat families
- 🇶🇦 QA, 🇸🇦 SA — Vision 2030 reforming, private international schools dominant for expat family pattern; Arabic + English working in Doha/Riyadh/Jeddah elite
- 🇵🇪 PE, 🇪🇨 EC — public Spanish + Quechua/Aymara (PE) / Kichwa/Shuar (EC); private bilingual in Lima (Miraflores/Barranco/San Isidro) / Quito / Cuenca; 2024 Ecuador security situation affecting family relocation
- 🇵🇾 PY — Spanish + Guaraní co-official, bilingual schooling routine; demographic dividend through ~2040
- 🇦🇲 AM — IT-sector + diaspora schools, Yerevan-concentrated
- 🇦🇿 AZ — ASAN Service efficient governance; private bilingual concentrated Baku
- 🇮🇳 IN — 26-week maternity leave (regionally generous); private CBSE/ICSE/IB/Cambridge schools dominant for elite (Bengaluru/Mumbai/Delhi-Gurgaon-Noida); demographic dividend through ~2050; English-medium routine for elite + middle class
- 🇯🇴 JO — public schools strained by Syrian refugee influx; private international + IB schools growing in Amman west (Abdoun, Sweifieh)
- 🇴🇲 OM, 🇧🇭 BH, 🇰🇼 KW — Vision 2040 (OM) / NSS 2050 (BH) / Vision 2035 (KW) reforming; private international schools dominant for expat family pattern in Muscat / Manama-Saar-Janabiya / Salwa-Mishref-Bayan-Salmiya

Weakest:
- LatAm informal urban (excluding strong middle-class enclaves)
- Western Balkans (improving)
- 🇪🇬 EG, 🇲🇦 MA, 🇵🇭 PH, 🇮🇩 ID, 🇩🇴 DO — public schools severely under-resourced; quality concentrated in private/international tier
- 🇲🇩 MD — emigration sustained since 1990s, public schools split Russian/Romanian-medium, EU candidate status (Jun 2022 → accession Jun 2024) may reverse trajectory
- 🇹🇳 TN — short maternity (30 days); IMF EFF SUSPENDED Mar 2024 affecting public-sector funding; quality concentrated in Tunis private French/American
- 🇳🇬 NG — public schools severely under-resourced + insurgency-affected NE; private international tier dominant in Lagos VI/Ikoyi/Lekki for elite
- 🇱🇧 LB — public schools severely strained — 2019 economic collapse + 2024 Israel-Hezbollah war + 2020 Beirut Port explosion; emigration accelerated post-2019; quality concentrated in private French/American/IB

## Integration environment (policy + lived-outcome gap)

For a mover asking "how welcoming is this country, structurally?", two primary signals are sourceable at the **country level** — and one widely-cited one is not. Report the two sourced rows, each date-stamped; fence off the third.

- **Integration POLICY (the legal framework on the books)** — [MIPEX](https://www.mipex.eu/what-is-mipex) (Migrant Integration Policy Index, Migration Policy Group): 58 indicators × 8 policy areas (Labour Market Mobility · Family Reunion · Education · Health · Political Participation · Permanent Residence · Access to Nationality · Anti-discrimination), expert legal coding 0–100 — **country-level POLICY, not lived outcome**. ⚠️ **Vintage trap**: the **MIPEX 2025** refresh covers **only the 27 EU members + Canada** (policy period 2020–2023/24); for every other country the latest is still **MIPEX 2020** (2014–2019 snapshot) — date-stamp accordingly. Report the overall band + the most decision-relevant of {Access to Nationality, Permanent Residence, Labour Market Mobility}.
- **Lived OUTCOME gap (how immigrants actually fare vs natives)** — [OECD/EU *Indicators of Immigrant Integration — Settling In* (2023)](https://www.oecd.org/content/dam/oecd/en/publications/support-materials/2023/06/indicators-of-immigrant-integration-2023_70d202c4/indicators-of-immigrant-integration-settling-in-main-indicators-2023-brochure.pdf): 83 outcome indicators; the most decision-relevant is the **immigrant-vs-native employment-rate gap** (foreign-born unemployment exceeds native-born in ~4 of 5 countries, ~2× across the EU; reference data 2010–2021 — vintage-stamp it). Country-level, not address-level.
- 🚫 **Loneliness / belonging / "expat happiness" / churn** — **NOT a primary-sourceable metric.** The most-cited ranking, **InterNations Expat Insider** (2025: 10,085 **self-selected** members, 46 destinations), is a non-probability convenience survey — anecdotal, must **not** drive a verdict. Community fit is a visit-and-trial-rental question (cross-ref `--integrity` § Why lifestyle moves END), not a dataset.

**Net**: report the MIPEX policy band + the OECD employment-outcome gap, each date-stamped and country-level; refuse a "this place is friendly / lonely" score. Companion to the English-proficiency tiers + family-friendliness signals above.

## Childcare cost + the second-earner trap

For a working-age family mover, childcare is both a top-line budget item and a hidden **second-earner disincentive** — distinct from the K-12 / international-school landscape in `--schools`. Two primary-sourced, **country-level** signals:

- **Net childcare cost** — [OECD Tax-Benefit "Net childcare costs"](https://taxben.oecd.org/tax-ben-resources/Calculating-Net-Childcare-Costs-Guidelines-for-Experts.pdf) (model: a couple with two children aged 2 & 3 in full-time centre-based care; **net** = gross fee − childcare benefits / fee discounts − tax reductions + other-benefit changes, as a % of the average wage). OECD average ≈ **14%** of average earnings; lowest **DE ~1% / EE ~0%**; highest in the English-speaking OECD + CH / NZ. Quote a country's exact value **only with the stated metric (% of average wage vs % of disposable income — they differ) + vintage** (values move; NZ's high figure is 2018-vintage; some economies are missing in some years). The national systems behind the number: FR *crèche* / CAF + free *école maternelle* from age 3 · DE *Kita-Gebühren* (set by Land) · NL *kinderopvangtoeslag* · UK 30-hours + Tax-Free Childcare.
- **The second-earner trap** — [OECD *Taxing Wages* 2024](https://www.oecd.org/tax/taxing-wages-20725124.htm) ("Tax and Gender through the Lens of the Second Earner"): a second earner entering work at 67% of the average wage faces a **34.0% tax wedge** (vs 31.0% for a single worker), **higher still with children** (lost child benefits stack), and **larger where tax is assessed at the household level**. **>75% of second earners are women** across most OECD countries — so the childcare-cost-plus-clawback is often what actually decides whether the trailing spouse works at all (cross-ref `--work` § spouse work-rights + `--cost-of-living`).

**Honest tail**: country-level only — this does **not** compute a household's net childcare bill, eligibility for CMG / *kinderopvangtoeslag* / Tax-Free Childcare / 30-hours, or a "should the spouse work" verdict (those turn on exact incomes, hours, child ages, residence). Per-city availability / waitlists are not uniformly published — verify locally.

## Anti-hallucination

- **Cite Eurostat / OECD / World Bank / UN DESA** as primary; date-stamp data
- **National stats offices** (Census Bureau US, TÜİK TR, FCSC AE, Stat Bureau JP, NSO TH, ONE DO, DANE CO, INE UY/CL/PY, Stats SA, Geostat GE, BPS ID, DOSM MY, GSO VN, PSA PH, CBS IL, HCP MA, CAPMAS EG, Singstat SG, C&SD HK, KOSTAT KR, DGBAS TW, Statistik Liechtenstein LI, DSEC MO, Estadística d'Andorra AD, IMSEE MC, BNS MD, PSA Qatar QA, GASTAT SA, INEI PE, INEC EC, ARMSTAT AM, SSC AZ, INS TN, NSO India / MoSPI IN, NBS NG, KNBS KE, DOS JO, NCSI OM, iGA BH, PACI/CSB KW, CAS LB) are primary for in-country data
- **PISA cycle is 3-year**; 2022 results are still authoritative until late 2026 (next cycle 2025 results expected late 2026)
- **PISA participation is voluntary** — DO, ZA, EG, MO, LI, AD, MC do not participate at country level; use TIMSS / UNESCO LLECE / national alternatives, do NOT extrapolate. SG and HK participate as separate jurisdictions
- **Population projections** are uncertain — use UN WPP medium variant
- **TFR varies substantially by year** — use latest single-year data, not multi-year; flag record-lows (KR 2024 0.72 globally lowest, JP 2024, HK 2023, TW 2023, SG 2023, TR 2023, CL 2023, TH 2023)
- **EF EPI** is non-government and methodology-disputed — use as a relative ranking, not absolute
- **Expat-skewed populations** (AE: ~88% expat per 2022 FCSC; QA: ~88% expat per 2024 PSA; KW: ~70% expat per 2024 PACI; BH: ~55% expat per 2024 iGA; OM: ~46% expat per 2024 NCSI; MC: ~9.5k Monégasques + ~28.5k others per IMSEE; SG: ~70% citizen + 30% PR/work-pass per Singstat) — citizen and aggregate metrics can diverge sharply; quote both when relevant
- **Israel TFR** is heavily driven by ultra-Orthodox/Haredi sub-population (~6.5 vs secular ~2.0 per 2023 CBS) — aggregate masks composition
- **Moldova population**: BNS official figures exclude Transnistria (~360k claimed by separatist administration but not in BNS series) — always state which scope is used
- **India population**: 2011 was last full census; 2021 census deferred to 2025-26 — UN 2024 medium-variant projection ~1.428B is currently the most-cited reference
- **Nigeria population**: 2006 was last full census; UN 2024 medium-variant projection ~227M is currently the most-cited reference (NPC contested counts post-2006)
- **Lebanon population**: no full census since 1932; CAS estimate ~5.5M includes ~1.5M Syrian + ~470k Palestinian refugees — always state which scope is used
- **Jordan population**: 2024 DOS estimate ~11.4M including refugees (Palestinian + Syrian); Jordanian-citizen-only count materially smaller

## Status

Last refreshed: 2026-05-01 (Tier-5 expansion: +8 countries — IN, NG, KE, JO, OM, BH, KW, LB; cumulative 87 countries: 44 original + 10 Tier-1 + 8 Tier-2 + 9 Tier-3 + 8 Tier-4 + 8 Tier-5).
**Confidence**: MEDIUM-HIGH overall — primary national stats office citations for population/TFR; PISA 2022 cycle for school benchmarks where countries/jurisdictions participate; TIMSS/SACMEQ/LLECE/ERCE/ASER/NAS/national-only alternatives flagged for non-PISA participants. Re-verify TFRs annually given record-low volatility in KR/HK/TW/SG/JP/TR/TH/CL. India + Nigeria + Lebanon population figures are projections / estimates pending overdue censuses.
