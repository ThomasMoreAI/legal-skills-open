# Universal `--retirement` Section

Retiree-specific filter overlay: pension taxation, healthcare access, climate, expat communities. Combines with `--all` or `--compare` to surface retirement-relevant facets.

**Snapshot**: May 2026 (Tier-5 additions — 87 countries total).

## Universal contract

For the property's country, return:
1. **Pension taxation** (foreign-source pension treatment)
2. **Healthcare access** (EU EHIC vs S1 form vs private)
3. **Climate suitability** (heatwaves, mild winters, humidity)
4. **Expat retiree community size** (English-speaking density)
5. **Cost of living** (relative to base country)
6. **Language barrier** (English availability in healthcare/admin)
7. **Special retirement programs** (where they exist)

## Output template

```markdown
## Retirement Profile

**Country**: <ISO2>
**Pension taxation (foreign-source)**: <regime>
**Healthcare access**: <EU S1 / private / dual / state>
**Climate suitability**: <evaluation>
**Expat retiree community**: <size>
**Cost of living vs <base>**: <ratio>
**English in healthcare/admin**: <high | mixed | low>
**Special programs**: <list>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## Pension-taxation regimes

### Most favourable (low/no tax on foreign-source pension)

| Country | Regime | Threshold / conditions |
|---|---|---|
| **PT** | **IFICI / NHR 2.0** (replaced classic NHR, closed to new entrants 1 Jan 2024 by Lei 82/2023) — research/innovation only; **pensions NO LONGER exempt under IFICI** (must pay PT progressive PIT) | EQF L6+ degree, scientific research / certified tech startup / export co only |
| **GR** | **Foreign Pensioner Tax Regime** — 7% flat on foreign-source income for 15 years for new tax residents who haven't been GR tax resident in 5 of last 6 years | Application via AADE; 7% covers worldwide income |
| **IT** | **Southern Italy 7% regime** — flat 7% for 9 years on foreign-source income for retirees moving to municipalities <20,000 pop in S Italy | First-time tax residency in IT in last 5 years |
| **CY** | **17-year non-dom regime** — exempt SDC; foreign pension may be taxed at 5% flat (over €3,420 pa) OR Cyprus marginal rate | Choose annually |
| **MT** | **MPRP residency** + flat 15% on foreign-remitted income (Maltese non-dom rule) | Min stay requirements |
| **PA** | **Pensionado program** (most generous LatAm) — US$1,000/mo lifetime pension qualifies; no PA tax on foreign-source income (territorial system) | |
| **MX** | **Temporary/Permanent residency** — no foreign-source pension tax under territorial principles for non-residents-tax (be cautious — verify per-program) | |
| **CR** | **Rentista visa** — US$2,500/mo income; CR doesn't tax foreign-source income for non-residents | |
| **AE** | **Retirement Visa (5-yr renewable)** — NO income/pension tax; territorial system; Federal Decree-Law 47/2022 introduced 9% corporate tax but personal income (incl. foreign pensions) remains untaxed | Age 55+; AED 1M property OR AED 1M savings OR AED 20k/mo income (verify 2026 thresholds at GDRFA) |
| **TH** | **LTR Wealthy Pensioner** — flat 17% on assessable income (most categories); foreign-source income remitted to TH may be taxable post-2024 reform — verify with Revenue Dept | Age 50+; USD 80k/yr passive income OR USD 40-80k + USD 250k investment |
| **PH** | **SRRV (Special Resident Retiree's Visa)** — foreign pension NOT taxed by PH; territorial-style for non-resident-source income | Age 35+ (some classes); USD 10k–50k deposit depending on age/pension status |
| **MY** | **MM2H (Malaysia My Second Home)** — foreign-source income exempt under territorial principle (post-2022 amendments narrowed for residents — verify) | Silver/Gold/Platinum + SEZ/SFZ; FD USD 150k–1M (SEZ/SFZ USD 32k–65k) + compulsory residence purchase (2026 data, source MOTAC) |
| **DO** | **Investor/Pensionado visa** — foreign pension exempt from DO tax; territorial system; 50% discount on transfer tax + property tax under retirement law | USD 1.5k/mo pension OR USD 200k investment route |
| **UY** | **Tax residency** — 11-yr exemption on foreign-source interest+dividends (Ley 19.937); pension itself not exempt but progressive PIT modest; territorial-leaning | Investment OR 60-day physical presence routes |
| **GE** | **Visa-free 1-year** for ~95 nationalities; territorial tax — foreign-source income not taxed | No formal retirement visa needed for most |
| **EG** | **PM Decree 3099/2019 investor route** (outcome unreconciled: GAFI citizenship / US State Dept 2025 ICS permanent residency) — foreign-source pension generally not taxed by EG (territorial application varies) | USD 250k non-refundable Treasury contribution (GAFI form) |
| **HK** | **Salaries Tax territorial — HK-source income only**; foreign pension generally NOT taxed; no global PIT regime | Tax residency by physical presence; pension articles in DTA network |
| **SG** | **Foreign-source income generally NOT taxed** for individuals (received in SG); IRAS NOR scheme for qualifying tax-residents (~0% on certain inbound foreign income) | NOR replaced for new applicants 2020+ — verify with IRAS; resident PIT 0-22% progressive |
| **MO** | **Macao Professional Tax territorial** — foreign pension NOT subject to MO PIT under territorial principle | DSF (Direcção dos Serviços de Finanças) — verify per-case |
| **MC** | **NO personal income tax** (Monaco residents — except French nationals via 1963 Convention); NO CGT | Carte de séjour required; ~€500k bank deposit + property/rental practitioner standard (verify at Sûreté Publique) |
| **AD** | **IRPF 0/5/10%** — lowest in Western Europe; foreign pension taxed at AD-resident progressive but max 10% | Tax residency 183d/yr or centre of economic interest (passive ≥90d/yr but tax-resident threshold higher — verify Departament de Tributs) |
| **LI** | **Foreign-pension taxation** at LI personal-tax rates (combined federal + commune ~2.5-22.4% — among lowest CH-area); double-tax treaty with most OECD | Steuerverwaltung FL — verify per-case; quota-based residency makes program rare |
| **MD** | **Worldwide income for residents** (>183 days); foreign pension taxable at flat 12% PIT (one of lowest in Europe); territorial-leaning for non-residents | SFS (Serviciul Fiscal de Stat) — verify; treaty network with major OECD |
| **TW** | **Worldwide income for tax residents** (>183 days); foreign pension taxable at progressive 5-40%; **AMT regime** may apply on foreign-source >NT$7M; 6% surtax on certain investment income | NTBT (National Taxation Bureau) — verify with treaty article for pension |
| **KR** | **Worldwide income for tax residents** (>183 days); foreign pension taxable at progressive 6-45%; foreign-source income exemption for first 5 of 10 yrs for "newly-resident" foreign workers (KR PIT Act Art. 18-2) | NTS (National Tax Service) — Naver/Kakao tax-blogs not authoritative; verify Art. 18-2 eligibility |
| **QA** | **NO personal income tax** for individuals (Qatar PIT regime is corporate-only, ~10% rate); foreign pension NOT subject to QA PIT; pension taxation deferred to source-country | Investor Residency Law 21/2018 ≥QAR 730k → 5yr renewable; PR Law 10/2018 ≥QAR 1M (capped ~100/yr); verify with MoI / GAT |
| **SA** | **NO personal income tax** for individuals (Saudi PIT regime is GCC-citizen Zakat 2.5% + corporate 20% non-Saudi); foreign pension NOT subject to SA PIT | Premium Residency Vision 2030: SAR 800k one-time / SAR 100k/yr renewable / Real-Estate-Owner SAR 4M; verify with ZATCA / Premium Residency Center |
| **AE** | **NO income/pension tax** (already listed above — repeated for tier-4 cross-reference) | (see AE Retirement Visa row) |
| **PE** | **Worldwide income for tax residents** (>183 days); foreign pension taxable at progressive PIT (2026: 8-30%); but foreign-source income earned BEFORE arrival can be claimed as non-taxable per Art. 6 LIR — verify with SUNAT | Investor Visa USD 30k BUSINESS activity (NOT real-estate exclusively); Rentista USD 1,500/mo passive; PR after 3yr continuous; passport after 2yr PR |
| **EC** | **Worldwide income for tax residents** (>183 days); foreign pension taxable at progressive PIT (2026: 5-37%) but foreign pension may be exempt under Art. 9 LRTI if double-tax treaty + source-country pension already taxed; verify with SRI | Pensioner Visa USD 1,500/mo; Investor Visa USD 42,500 (~100×SBU 2026 SBU USD 470/mo); PR after 21mo Temporary; naturalization 3yr PR |
| **PY** | **Territorial PIT** — foreign-source pension NOT subject to PY IRP (Impuesto a la Renta Personal) for non-PY-source income; flat 8/9/10% PIT regime on PY-source only | Resolución SET 1186/2023 reformed PR — USD 70k SUACE business invest OR active SET RUC; citizenship 3yr continuous PR |
| **AM** | **Worldwide income for tax residents** (>183 days); foreign pension taxable at flat 21% PIT (2026 — verify SRC); diaspora-repatriation incentives via Law on Foreign Investment | Investor Residency AMD 50M (~USD 130k) deposit OR property → 5yr renewable; Citizenship by descent (Diaspora) Art. 13 streamlined / naturalization 3yr PR + dual since 2007 |
| **AZ** | **Worldwide income for tax residents** (>182 days); foreign pension taxable at progressive 14-25% PIT (2026 — verify Min. Tax) | TRP via real estate ≥AZN 100k (~USD 60k) → 1yr renewable; PR after 8yr continuous TRP; Strategic Investor Visa AZN 540k priority sectors; naturalization 5yr PR + Azeri language; dual citizenship LIMITED |
| **TN** | **Worldwide income for tax residents** (>183 days); foreign pension taxable at progressive 0-35% PIT (2026 — verify with Direction Générale des Impôts); 80% abatement on foreign pension transferred permanently to TN in TND under similar logic to MA (verify Code IRPP Art. 36) | Investor Residence Permit ≥TND 1M (~USD 320k); citizenship 5yr continuous PR + Arabic + dual since 2014; Tunisia Investor Visa drafted 2024 NOT gazetted |
| **OM** | **NO personal income tax** for individuals (Oman individual income-tax law drafted 2022 NOT enacted as of May 2026 — verify with Tax Authority); foreign pension NOT subject to OM PIT — verify | Investor Residency Royal Decree 89/2021 — 5-yr ≥OMR 250k (~USD 650k) ITC freehold / 10-yr ≥OMR 500k (~USD 1.3M) ITC; Long-term Retiree Residence ≥OMR 4,000/mo pension (~USD 10,400); NO citizenship-by-investment (Omani nationality strict) |
| **BH** | **NO personal income tax** for individuals; foreign pension NOT subject to BH PIT | Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k) → 10-yr renewable; Golden Residency Decree 16/2022 — 10-yr renewable for property owners ≥BHD 200k OR investors / talented / retirees (BHD 4k/mo); NO CBI; verify with Nationality, Passports & Residence Affairs |
| **KW** | **NO personal income tax** for individuals; foreign pension NOT subject to KW PIT — but residency entirely via employment Iqama (Decree-Law 17/1959); citizenship effectively impossible (Decree-Law 15/1959) | NO golden-visa via real estate (UNIQUE absence in GCC); 5+yr to PR claim rarely granted; verify with Public Authority for Civil Information / MoI |

### Less favourable (foreign pension taxed at marginal/progressive)

| Country | Regime |
|---|---|
| FR | Worldwide income; tax-treaty avoids double taxation but progressive rates apply |
| ES | Worldwide; pensions taxed at general scale (post-Beckham Law sunset) |
| DE | Worldwide; pensions partially taxable (rising portion until 100% by 2058) |
| UK | Worldwide for tax residents; double-tax treaty with most |
| US | Citizenship-based taxation — worldwide regardless of residency (unique) |
| CA | Worldwide for residents |
| TR | Worldwide for tax residents; pensions taxed at progressive PIT (2026: 15%-40%); treaty network mitigates double-tax |
| JP | Worldwide for residents; foreign pension taxable but treaty-relief (US-JP, UK-JP, etc.) common; "non-permanent resident" 5-year carve-out for non-Japan-source income not remitted |
| CO | Worldwide for tax residents (>183 days); pensionado visa holders pay CO PIT; UVT-based progressive rates |
| CL | Worldwide post-3-yr (3-year exemption for new residents on foreign-source income — Art. 3 DL 824); pensions taxable thereafter at progressive PIT (2026: up to 40%) |
| ZA | Worldwide for tax residents; foreign pension may be exempt under s10(1)(gC) ITA if for services rendered abroad — verify per-case |
| ID | Worldwide for residents (>183 days); foreign pension taxable at progressive PIT; some treaty relief |
| VN | Worldwide for residents (>183 days); foreign pension taxable at progressive PIT (2026: up to 35%) |
| IL | Worldwide for residents BUT new immigrants (Olim) get **10-year tax holiday** on foreign-source income+capital gains (Amendment 168, 2008) |
| MA | Foreign-source pensions: **80% abatement** if transferred permanently to MA in DH (Art. 76 CGI); effective rate dramatically reduced |
| IN | Worldwide for tax residents (>182 days); foreign pension taxable at progressive 0-30% + surcharge + 4% cess (2026 — verify CBDT); LRS USD 250k/yr cap on outbound remittance; foreign pension may receive treaty relief under DTAA (US/UK/CA — verify Income Tax Act s.90); **NRO/NRE bank-account split** material; **NO golden-visa via real estate** (UNIQUE absence — India does not offer property-pegged residency) |
| NG | Worldwide for tax residents (>183 days); foreign pension taxable at progressive 7-24% + 2.5% NHF (2026 — verify NRS, formerly FIRS); minimal treaty network; **NO golden-visa via real estate** — STR-1 Investor visa USD 100k business is the longer-term pathway |
| KE | Worldwide for tax residents (>183 days OR ≥122 days/yr × 3 yrs); foreign pension taxable at progressive 10-35% PIT (2026 — verify KRA); **NO golden-visa via real estate** (UNIQUE absence in EAC); Class K Resident Permit KES 200k+/yr passive income is the practical retiree route |
| JO | Worldwide for tax residents (>183 days); foreign pension taxable at progressive 5-30% + 1% national-contribution PIT (2026 — verify ISTD / Income & Sales Tax Dept); **CBI Jordan since 2018** (JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport, ~50 visa-free destinations — WEAK passport for mobility plays, rational mainly for diaspora reconnection / GCC business utility) |
| LB | Worldwide for tax residents (>183 days); foreign pension taxable at progressive 4-25% PIT (2026 — verify MoF); **post-2019 banking-sector collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war Sep-Nov 2024** structural overlay; NO golden-visa via real estate; Investor Residency ≥USD 50k Lebanese business (1-yr renewable); property ownership ≥USD 200k can support residency application but not automatic |

### Pension tax special cases

- **CY 5% pension regime**: optional alternative — flat 5% on foreign pension income above €3,420 (effectively a 5% marginal once threshold passed)
- **DK borgerservice**: tax law treats foreign pensions as taxable but with credit for foreign tax paid
- **NL Box 1 pension treatment**: foreign pensions usually taxed at progressive rates; treaty-based exemption case-by-case

## Healthcare access

### EU/EEA (S1 form for retirees from another EU country)
S1 form lets you access host-country state healthcare while it's billed back to your home country. Available throughout EU+EEA+CH for state-pension recipients.

| Country | Public healthcare quality (2025 ranking-style) | Notes |
|---|---|---|
| FR | Excellent (universal Sécu) | English in major cities limited |
| ES | Excellent (SNS) | English coastal/expat areas |
| PT | Good (SNS); waiting lists | English coastal/Algarve |
| IT | Good (SSN) regional variation | English Tuscany/major cities |
| GR | Mid (EOPYY) — private gap-cover common | English in tourist areas |
| MT | Good (state hospitals); English-speaking | English everywhere |
| CY | Good (GeSY 2019); English-speaking | English everywhere |
| LU | Excellent (CNS) | French/German/Lëtzebuergesch |
| DE | Excellent (multi-payer GKV/PKV) | German required for admin |
| AT | Excellent (ÖGK) | German required |
| CH | Excellent (LAMal mandatory private) | Multilingual incl. English in cities |
| NL | Excellent (Zvw) | English widely spoken |
| BE | Excellent (mutuelles/ziekenfonds) | French/Dutch/German |
| DK | Excellent (universal) | Danish required |
| SE | Excellent (universal) | English widely spoken |
| FI | Excellent (Kela) | English widely spoken |
| NO | Excellent (HELFO) | English widely spoken |
| IS | Excellent (state) | English widely spoken |
| IE | Mixed (HSE waiting lists; private gap) | English |
| LI | Excellent (KVG mandatory private — closely modelled on CH LAMal) | German required for admin; Swiss-system standard |
| AD | Good (CASS mandatory) | Catalan/Spanish/French — admin multilingual; English limited in clinics |
| MC | Excellent (CHPG state hospital + French-system network); Caisses Sociales de Monaco | French dominant; English in private clinics |

### Non-EU
- **UK NHS**: free for residents; non-resident must pay or use private; post-Brexit S1 still available for some pre-2021 retirees
- **AU Medicare**: residents/PR; reciprocal agreements with UK/IE/NL/SE/FI/NO/IT/MT/SI/BE
- **NZ**: residents; reciprocal with UK/AU
- **CA**: provincial residency required (typically 3-month waiting period)
- **US**: Medicare available at 65 if 10+ years payroll contributions; resident-only; ACA marketplace alternative for under-65 retirees; state-level variation (TX/FL no state income tax; CA/NY high)
- **MX/BR/AR/CR/PA**: state healthcare exists but expat retirees commonly use private (much cheaper than US, comparable to EU)
- **TR**: SGK universal scheme available to residents (incl. expat retirees with residence permit); private network strong (Acibadem, Memorial); cost ~30-50% of UK private
- **AE**: NO universal public system for expats; mandatory private health insurance via DHA (Dubai) / DOH (Abu Dhabi); high quality, premium pricing for retirees age 60+
- **JP**: National Health Insurance (NHI / Kokuho) covers all residents incl. expats; 30% co-pay; quality high but **language barrier severe**; English-speaking clinics concentrated in Tokyo/Yokohama/Osaka
- **TH**: Universal Coverage Scheme for citizens; expats use private (Bumrungrad, Bangkok Hospital — internationally accredited); LTR visa requires USD 50k health insurance OR USD 100k deposit
- **DO**: SeNaSa public + private SDSS; expats overwhelmingly use private (Hospiten, CEDIMAT); Medicare-style coordination with US insurance limited
- **CO**: EPS contributory system (residents pay ~12% income); private (Sanitas, Colsanitas) strong; Medellín/Bogotá quality compares to US private at fraction of cost
- **UY**: Mutualistas (private cooperatives) excellent — most expats join (~USD 80-150/mo); FONASA public for residents
- **CL**: Dual system — FONASA (public) OR Isapres (private); retirees often Isapres but premiums rise sharply with age (post-2023 Constitutional Court ruling reshaping pricing)
- **ZA**: Public healthcare overstretched; expats universally use private (Discovery Health, Bonitas) + medical aid scheme; quality-cost ratio strong but ZAR volatility risk
- **GE**: Universal Healthcare Program (state) for citizens/residents; private clinics (Mediclub, Medi) growing; Tbilisi quality fair but expats often medivac for serious conditions
- **ID**: BPJS Kesehatan (universal) for residents incl. KITAS/KITAP holders; quality variable; expats in Bali commonly use private (BIMC, Siloam); medivac to SG common for serious cases
- **MY**: Universal public system + strong private (Sunway, Pantai, Gleneagles); Penang/KL hospitals internationally accredited; **medical-tourism destination**
- **VN**: Universal Health Insurance for residents; expats use private (Vinmec, FV Hospital); Saigon/Hanoi quality fair-good but evac to TH/SG for complex cases
- **PH**: PhilHealth universal for residents; private (St. Luke's, Makati Med) strong in Metro Manila; provincial quality patchy
- **IL**: Universal via 4 Sick Funds (Kupot Holim — Clalit, Maccabi, Meuhedet, Leumit); excellent quality; **Olim entitled from arrival**; English support varies
- **MA**: AMO universal scheme being expanded (2024-2026 reform); expats use private (Cliniques Akdital, Cheikh Zaid); French-system standards
- **EG**: New Universal Health Insurance (2018 law, phased rollout); expats use private (Cleopatra, As-Salam International); Cairo quality fair; **medivac for serious cases recommended**
- **SG**: MediShield Life (universal for citizens/PRs) + MediSave/MediFund 3M structure; non-resident expats use private (Mount Elizabeth, Raffles, Gleneagles — JCI-accredited); among the highest-quality systems globally per WHO 2023 indicators; English universal in healthcare admin
- **HK**: HA (Hospital Authority) public network — eligible-persons subsidy for HKID holders; expats commonly mix HA + private (Matilda, Hong Kong Adventist, Canossa); English universal; HKD-pegged-to-USD currency stability for retirees
- **KR**: NHIS (National Health Insurance Service) universal — mandatory enrolment for foreign residents 6+ months; quality high (Samsung Medical, Asan, Severance JCI-accredited); **Korean dominant in admin** outside Itaewon/Gangnam English-medium clinics
- **TW**: NHI (National Health Insurance) universal — mandatory enrolment for ARC/APRC holders after 6 months; consistently top-ranked globally on accessibility/cost (NHIA reports); English in major Taipei hospitals (NTUH, Taipei Medical, Cathay General); Chinese dominant elsewhere
- **MO**: SSM (Serviços de Saúde de Macau) public + Hong Kong-style private gap-cover common; resident card holders entitled; Cantonese + Portuguese dominant; English in tourism-zone clinics only
- **AD**: CASS (Caixa Andorrana de Seguretat Social) — mandatory for residents; covers Andorran network + cross-border to FR/ES per agreement; private gap-cover common; Catalan/Spanish admin
- **MC**: Caisses Sociales de Monaco for residents/employees; CHPG (Centre Hospitalier Princesse Grace) state hospital; cross-border to FR/IT for specialised cases; private clinics English-friendly
- **LI**: KVG-equivalent compulsory health insurance (Krankenversicherung) — closely modelled on CH LAMal; Vaduz hospital + cross-border to CH (St. Gallen, Zurich) standard; German-system standard
- **MD**: CNAM (Compania Națională de Asigurări în Medicină) mandatory; expats commonly use private (Medpark, Repromed); **emigration of medical staff to RO/EU is structural concern**; Romanian + Russian dominant
- **QA**: HMC (Hamad Medical Corporation) public network — eligibility-gated for Qatari + sponsored residents; expats use private (Aspetar, Sidra Medicine, Doha Clinic); high quality, premium pricing for retirees age 60+; Arabic + English in healthcare admin
- **SA**: MOH (Ministry of Health) public network for Saudi citizens; expats mandatory private health insurance (CCHI); private (Saudi German Hospital, Dr. Sulaiman Al Habib, King Faisal Specialist Hospital — JCI-accredited); Vision 2030 healthcare expansion via Roshn / Red Sea / NEOM medical clusters; Arabic + English in major centres
- **PE**: EsSalud (social security, contributory) for residents + SIS (subsidized public, low-income); expats use private (Clínica Anglo Americana, Clínica Ricardo Palma, Auna network); Lima quality fair-good but evac to US/MX for serious cases common; Spanish dominant + English in expat-clinic enclaves Miraflores/San Isidro
- **EC**: IESS (Instituto Ecuatoriano de Seguridad Social) for residents + private; expats use private (Hospital Metropolitano, Hospital Vozandes — Quito; Hospital Monte Sinaí — Cuenca); Cuenca ranks well on retiree healthcare per International Living indices but verify; Spanish dominant + English in Cuenca expat zone
- **PY**: IPS (Instituto de Previsión Social) public scheme; expats commonly use private (Sanatorio Migone, Sanatorio Adventista, Hospital Bautista — Asunción); PY healthcare quality lags PE/EC; medivac to BR/AR for complex cases; Spanish + Guaraní co-official
- **AM**: state Healthcare Universal Programme + private; **CMC and Erebouni Medical Center are flagship Yerevan hospitals**; expats commonly mix state + private; medivac to TR/RU/EU historically common; Armenian + Russian dominant; English in private clinics
- **AZ**: AzMedSv (state) + private; mandatory CMI (Compulsory Medical Insurance) phased in 2020-2024; expats use private (Memorial Bahcelievler — Baku, Bona Dea International Hospital, MediClub Hospital); Azerbaijani + Russian dominant; English in business/expat zones; medivac to TR
- **TN**: CNAM (Caisse Nationale d'Assurance Maladie) public + private; **French-system standards**; expats use private (Clinique Hannibal, Clinique Taoufik, Clinique El Manar — Tunis); Arabic + French in healthcare admin; medical-tourism destination (cosmetic surgery, dental, IVF) for FR/IT/MT clientele
- **IN**: PMJAY (Pradhan Mantri Jan Arogya Yojana) public for low-income citizens (~500M beneficiaries) + extensive private; expats use private (Apollo, Fortis, Max, Manipal, Medanta — JCI-accredited flagship hospitals Bangalore/Hyderabad/Mumbai/Delhi NCR); **medical-tourism destination** at fraction of Western costs; English universal in private hospitals + medical admin; medivac rarely needed
- **NG**: NHIA (National Health Insurance Authority — replaces NHIS since 2022) limited rollout; expats use private (Reddington Hospital, Lagoon Hospital, Lagos University Teaching Hospital, First Cardiology — Lagos VI/Ikoyi) **mandatory private insurance for expats**; medivac to ZA/UK/UAE common for serious cases; English official + Yoruba/Igbo/Hausa + Pidgin universal
- **KE**: NHIF (National Hospital Insurance Fund) public + Social Health Insurance Fund (SHIF — phased 2024-25 reform — verify); private flagship Aga Khan University Hospital Nairobi + Karen Hospital + Nairobi Hospital + MP Shah Hospital; medivac to ZA/UK for complex; English + Kiswahili official; M-PESA mobile-money universal in admin (unique to KE)
- **JO**: Royal Medical Services (RMS — military-affiliated; serves civilians via referral) + private (King Hussein Cancer Center, Specialty Hospital, Istishari Hospital, Al-Khalidi Medical Center — Amman); **medical-tourism hub for GCC + Iraq + Syria refugee population**; English-medium private hospitals; Arabic + English in healthcare admin
- **OM**: MoH (Ministry of Health) public network for Omani citizens + sponsored expats; mandatory private health insurance for expats (Dhamani 2025 phased rollout per RD 89/2021 healthcare provisions); private (Royal Hospital Muscat, Sultan Qaboos University Hospital, Burjeel Muscat); medivac to UAE common; **cyclone exposure HIGH** — Gonu 2007/Mekunu 2018/Shaheen 2021 catastrophic Muscat (insurance underwriting baseline); Arabic + English in healthcare admin
- **BH**: SEHATI (mandatory contributory + supplemental) + MoH public + private (King Hamad University Hospital, American Mission Hospital, Bahrain Specialist Hospital, Al Salam Specialist Hospital); Saudi Causeway integration drives weekend medical-tourism flow; Arabic + English in healthcare admin; everyday English widely
- **KW**: MoH public network for Kuwaiti citizens + mandatory private health insurance for expats (Afya health-card system 2016+); private (Al Salam International Hospital, Hadi Clinic, New Mowasat, Dar Al Shifa); medivac to UAE/UK historically common; Arabic + English in healthcare admin; mandatory KD 50/yr healthcare-fee for expat residents
- **LB**: **Healthcare collapse since 2019 financial crisis + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war** — private clinics + hospitals operating with import-shortages + currency-collapse fee dual-pricing (USD ↔ LBP); historically excellent French-system standards (American University of Beirut Medical Center, Hôtel-Dieu de France, Clemenceau Medical Center, Saint George Hospital University Medical Center); medivac to CY/IT/FR for fresh-USD-paying patients; Arabic + French + English in healthcare admin (Lebanon traditionally trilingual)

## Climate suitability for retirement

### Mild winters + manageable summers (preferred)
1. **PT (Algarve, Lisbon, Madeira)** — 18-23°C winter days; coastal cooling
2. **ES (Costa del Sol, Costa Blanca, Canarias)** — 17-22°C winter
3. **GR (Crete, Cyprus, southern Peloponnese)** — 15-20°C winter
4. **IT (Sicily, Calabria, Puglia)** — 12-18°C winter; rising heatwave concern
5. **MT, CY** — 14-20°C winter; **water scarcity rising** (CY 2025 worst drought)
6. **TR (Aegean coast — Bodrum, Antalya, Fethiye)** — 14-19°C winter; summer heatwaves rising
7. **MA (Marrakech, Essaouira, Tangier)** — 18-22°C winter; Atlantic coast cooler than interior
8. **CL (Coquimbo, Ñuble coast)** — 12-18°C winter; Mediterranean climate; arid trend (drought)
9. **UY (Punta del Este, Montevideo)** — 12-16°C winter; humid subtropical
10. **ZA (Cape Town, Garden Route)** — 12-18°C winter; Mediterranean climate; **water-scarcity overlay (Day Zero risk)**
11. **CO (Medellín "City of Eternal Spring")** — 18-22°C year-round; altitude-moderated
12. **MX (already listed)** — verify
13. **US (FL/AZ/TX/CA-S)** — 15-25°C winter; FL hurricane season + AZ extreme summer heat trade-offs
14. **EC (Quito, Cuenca)** — 10-22°C year-round altitude-moderated (Cuenca ~2,560m, Quito ~2,850m); **Cotopaxi volcano active 2024 + Pacific Ring seismic (2016 Pedernales M7.8) + tsunami coastal**
15. **PE (Lima coastal)** — 16-26°C year-round (Pacific cool current); inland Andes higher; **Pacific Ring of Fire HIGH seismic + 2017/2023 El Niño catastrophic floods + huaicos + volcanic Misti/Ubinas/Sabancaya south**
16. **PY (Asunción)** — humid subtropical 14-34°C; **Río Paraguay floods catastrophic 2014-15/2018/2019/2024 + Cerrado/Chaco wildfires 2019-20/2024 + drought**; minimal seismic

### Subtropical / temperate Asian
- **HK**: Humid subtropical 14-19°C winter, 28-33°C humid summer (Jun-Sep); typhoon season Jul-Oct; Article 23 (Mar 2024) sentiment factor for some retirees
- **SG**: Equatorial 24-32°C year-round; minimal seasonal variation; very high humidity; Changi best-in-world airport for medical travel
- **TW**: Tropical-subtropical; Taipei 14-20°C winter, 28-32°C summer; **2024 Hualien M7.4 earthquake** material to seismic disclosure
- **MO**: Humid subtropical 14-20°C winter, 28-32°C summer; typhoon season; **post-Hato 2017 storm-surge resilience reforms** (verify with DSAMA)

### Cold-continental / Eastern Europe
- **MD**: Cold continental — Chișinău -3 to +1°C winter, 22-28°C summer; lowest COL in Europe

### Tropical / hot year-round
- **TH (Phuket, Chiang Mai, Hua Hin)** — 22-32°C; Chiang Mai cool-season Nov-Feb; **PM2.5 burning season Feb-Apr severe in N**
- **PH (Cebu, Bohol, Davao)** — 25-32°C; typhoon season Jun-Nov (Davao less typhoon-exposed)
- **MY (Penang, KL, Johor)** — 25-32°C year-round; humid; minimal seasonal variation
- **ID (Bali, Lombok)** — 26-30°C; wet/dry seasons; volcanic risk
- **VN (Da Nang, Hoi An, Saigon)** — 22-32°C; Da Nang/Hoi An typhoon Sep-Nov
- **DO (Las Terrenas, Punta Cana)** — 24-31°C; hurricane season Jun-Nov
- **EG (Hurghada, Sahel, Sharm)** — 18-35°C; very dry; summer extreme
- **AE (Dubai, Abu Dhabi)** — 18-42°C; **summer 45°C+ near-uninhabitable outdoors May-Sep**
- **QA (Doha)** — 18-42°C; **summer 45°C+ + sandstorms + 2018/2021/2024 Doha storm-surge floods**; FIFA World Cup 2022 legacy infra (Lusail metro)
- **SA (Riyadh, Jeddah, Mecca, Medina, NEOM, Red Sea, AlUla)** — 12-45°C; **interior 50°C+ summer + sandstorms + 2009/2011 Jeddah catastrophic floods + drought + groundwater depletion**; Mecca/Medina constitutional Muslim-only; Riyadh Metro Phase 1 Dec 2024
- **TN (Tunis, Sousse, Sfax, Djerba)** — 11-32°C; Mediterranean coast milder; **2018 Cap Bon catastrophic floods + 2023-24 record drought (reservoirs <30%) + APAL coastal erosion**
- **IN (Mumbai, Delhi NCR, Bengaluru, Goa, Kerala, Pondicherry)** — Mumbai 18-33°C / Delhi NCR 7-43°C / Bengaluru 16-33°C altitude-moderated / Kerala 23-31°C; **Indian monsoon Jun-Sep critical (Mumbai/Kerala flooding); Delhi PM2.5 crisis Oct-Feb annual; Bengaluru water-scarcity 2024+ acute; Joshimath subsidence 2023 + Himalayan flash floods**; cyclone exposure E coast (Chennai/Vizag); Bengaluru/Pune/Goa most retiree-amenable
- **NG (Lagos, Abuja, Kano)** — Lagos 22-32°C tropical humid + flooding rainy season Apr-Oct / Abuja FCT 18-31°C savanna milder altitude / Kano 13-39°C Sahel hot-arid; **Lagos coastal flooding chronic + Atlantic surge events + Niger-delta climate stress + Sahel drought**
- **KE (Nairobi, Mombasa, Diani, Naivasha)** — Nairobi altitude-moderated 11-26°C year-round (~1,795m) "City in the Sun"; Mombasa coastal 22-32°C tropical-humid; **Rift Valley seismic baseline + Mt Kenya / Kilimanjaro snow-loss climate marker + 2018+ locust crises + drought NE/Turkana**
- **JO (Amman, Aqaba, Dead Sea, Petra)** — Amman semi-arid altitude-moderated (~750m) 4-32°C; Aqaba Red Sea 12-39°C / Dead Sea 14-39°C below sea level (-430m); **among most water-poor globally per FAO + Disi aquifer depletion + Dead Sea shrinking ~1m/yr**
- **OM (Muscat, Salalah, Nizwa, Sohar)** — Muscat 17-42°C; **Salalah unique Khareef monsoon Jun-Sep (Indian Ocean SW monsoon) — only verdant zone in Arabian Peninsula**; Nizwa interior 8-44°C; **CYCLONE EXPOSURE HIGH** — Gonu 2007/Phet 2010/Mekunu 2018/Shaheen 2021/Tej 2023 catastrophic Muscat coast; Indian Ocean SST warming intensifying (insurance underwriting baseline)
- **BH (Manama, Muharraq, Riffa, Hamad Town)** — 14-39°C; **summer 40°C+ + sandstorms + sea-level rise + 2008/2009 Manama flooding + groundwater depletion + Saudi Causeway integration**; humid coastal vs UAE/Qatar
- **KW (Kuwait City, Hawalli, Salmiya)** — 8-49°C among hottest inhabited capitals; **summer 50°C+ near-uninhabitable May-Sep + sandstorms (Toz / shamal) + 2018 Kuwait flooding + groundwater depletion + 2003 Kuwait fires legacy + oil-fired heat-island effect**; Arabian Gulf coastal humid
- **LB (Beirut, Tripoli, Byblos, Mount Lebanon, Cedars)** — Beirut Mediterranean 11-30°C / Mount Lebanon altitude-moderated cooler / Cedars ski-zone 1,800-3,000m **only Middle Eastern country with skiing**; **2024 Israel-Hezbollah war Sep-Nov 2024 + 2020 Beirut Port explosion legacy + post-2019 banking-collapse + Litani River + drought**

### Cold but stable (added)
- **JP (Tokyo, Osaka, Fukuoka)** — 5-10°C winter; humid summers; well-heated indoors
- **GE (Tbilisi)** — 2-7°C winter, 25-30°C summer; continental
- **IL (Tel Aviv, Jerusalem, Haifa)** — 10-18°C winter; hot dry summers
- **KR (Seoul, Busan, Jeju)** — Seoul -5 to +3°C winter, 26-31°C humid summer; Jeju milder
- **AD (Encamp, La Massana, Andorra la Vella)** — alpine 0-8°C winter, 18-25°C summer; ski-season Dec-Apr
- **LI (Vaduz, Schaan)** — alpine 0-5°C winter, 18-24°C summer; CH-aligned climate
- **MC (Monte-Carlo, La Condamine, Fontvieille)** — Mediterranean 8-15°C winter, 24-29°C summer; among the mildest in Europe
- **AM (Yerevan)** — continental — Yerevan -3 to +3°C winter, 28-35°C summer; **HIGH SEISMIC 1988 Spitak M6.8 baseline (~25,000 deaths) + Yerevan/Gyumri/Vanadzor microzoning**
- **AZ (Baku)** — moderate-arid Caspian — Baku 4-10°C winter, 27-33°C summer; **Caucasus + Caspian seismic (2000 Baku M6.8) + Caspian sea-level falling ~1m 2010-24 + Absheron mud volcanoes (unique)**

### Cold but stable, indoor-life-friendly
1. **DE, AT, CH, FR, BE, NL, LU, IE, UK, DK, SE, FI, NO, IS** — heating-cost concern; northern long darkness
2. **CZ, SK, PL, HU, BG, RO** — colder; cheaper

### Hot summers — emerging concern
- **ES interior, S Italy, GR mainland**: 40°C+ summer days increasingly common (2003, 2022, 2023, 2024 heatwaves)
- **PT interior**: similar; coastal milder
- **CY, MT, S IT**: water-scarcity overlay

### Avoid for climate-sensitive retirees
- 🇮🇸 IS: harsh winters, volcanic ash episodes, Reykjanes eruption series 2023+
- 🇸🇪🇫🇮🇳🇴 SE/FI/NO N: long dark winters, mood-affective concern
- 🇫🇷🇮🇹 inland mountain valleys: severe winter
- ME / AL coastal: high summer humidity + tourism crowds

## Expat retiree community density

### Established / largest
1. 🇪🇸 ES (Costa del Sol, Costa Blanca, Mallorca) — UK + DE + NL + Scandinavian retiree clusters; English+German+Dutch services pervasive
2. 🇵🇹 PT (Algarve, Lisbon, Madeira, Cascais) — UK + DE + FR + NL retirees; English-medium businesses
3. 🇫🇷 FR (Provence, Dordogne, Languedoc, Côte d'Azur) — UK + NL + DE retirees
4. 🇮🇹 IT (Tuscany, Umbria, Puglia, Sicily) — UK + DE + US retirees
5. 🇨🇾 CY (Paphos especially) — UK + Russian retirees
6. 🇲🇹 MT — UK + DE + IT retirees; English-medium

### Growing
- 🇲🇽 MX (San Miguel de Allende, Lake Chapala, Mérida, Playa del Carmen) — US/CA retirees
- 🇵🇦 PA (Boquete, Coronado, Panama City) — US/CA retirees
- 🇨🇷 CR (Atenas, Tamarindo, Manuel Antonio) — US/CA retirees
- 🇭🇺 HU (Budapest) — UK/DE retirees post-2020
- 🇲🇪 ME (Coastal Budva, Tivat) — RU pre-2022 historically; rebalancing
- 🇦🇱 AL (Saranda, Vlora) — IT/UK retirees post-2020
- 🇹🇷 TR (Bodrum, Antalya, Fethiye, Alanya) — UK/DE/RU/Scandinavian retirees; large established community since 2000s
- 🇹🇭 TH (Chiang Mai, Hua Hin, Phuket) — UK/US/AU/DE/Scandinavian; Chiang Mai US/EU writer-retiree hub
- 🇲🇾 MY (Penang, KL, Johor Bahru) — UK/AU/SG/JP retirees via MM2H legacy + new tiers
- 🇵🇭 PH (Cebu, Dumaguete, Bohol, Davao) — US/AU/JP/KR retirees via SRRV (most generous SE-Asia program)
- 🇮🇩 ID (Bali — Ubud, Canggu, Sanur) — AU/EU/US retirees via KITAP
- 🇻🇳 VN (Da Nang, Hoi An, Saigon expat enclaves) — growing US/EU/AU; visa pathway thinner than TH/PH/MY
- 🇩🇴 DO (Las Terrenas FR/IT enclave; Punta Cana US/CA; Sosúa DE/Scandinavian) — diverse expat communities
- 🇨🇴 CO (Medellín — El Poblado, Laureles; Cartagena) — surge in US/CA digital-nomad-aging-into-retirement crowd
- 🇺🇾 UY (Punta del Este AR seasonal + permanent EU; Colonia) — moderate but high-quality
- 🇨🇱 CL (Viña del Mar, La Serena) — small but growing US/EU
- 🇿🇦 ZA (Cape Town, Plettenberg Bay, Knysna) — UK/DE/NL retirees; Garden Route established
- 🇬🇪 GE (Tbilisi, Batumi) — RU+UA post-2022 surge; growing US/EU crypto-retiree subsegment
- 🇮🇱 IL (Tel Aviv, Netanya, Ra'anana, Jerusalem) — US/FR/UK/RU Olim retirees; large established community
- 🇲🇦 MA (Marrakech, Essaouira, Tangier, Agadir) — FR retirees dominant; UK/DE growing
- 🇪🇬 EG (Hurghada, El Gouna, Sahel) — RU/UA/DE/UK retirees; **currency volatility risk material**
- 🇦🇪 AE (Dubai marinas, Abu Dhabi) — UK/IN/RU/EU; new Retirement Visa post-2018
- 🇯🇵 JP (Tokyo, Yokohama, Fukuoka) — small but established US/UK; **no formal retirement visa**, HSP/Investor route only
- 🇸🇬 SG — small high-income retiree community; no retirement visa via property; LTSV (Long-Term Social Visit Pass) for parents of EP holders is the practical retiree pathway
- 🇭🇰 HK — moderate UK/AU/CA professional-retiree community; **CIES reactivated Mar 2024** (HK$30M + ≤HK$10M residential) opens an investment-track route again
- 🇰🇷 KR (Itaewon/Hannam-dong/Pangyo) — small US/EU/JP retiree community; **F-2 Investor (₩600M 5yr) → F-5 PR** is the route; F-4 for Korean diaspora
- 🇹🇼 TW (Tianmu/Da'an/Xinyi/Neihu) — moderate US/JP/EU retiree presence; **Gold Card** 4-yr work + residency (no investment) for high-skill applicants → APRC after 5yr
- 🇲🇴 MO — very small expat retiree community (heavily Cantonese/Portuguese); investment-residence SUSPENDED since 2007; Talent Programme 2024 NOT property-linked
- 🇦🇩 AD — moderate ES/FR/PT retiree community (~75% non-Andorran population); **Residència Activa/Passiva ~€600k** OR €350k + €50k AFA the route
- 🇲🇨 MC — small ultra-high-net-worth international retiree community (~38k pop, ~70% non-Monégasque); **carte temporaire 1yr → ordinaire 3yr → privilégiée 10yr** with ~€500k bank deposit + property/rental practitioner
- 🇱🇮 LI — very small (quota-based residency: ~28 EEA + ~17 third-country/year); CH-integrated retiree practice; **Personal Residence Programme** rare petition only
- 🇲🇩 MD (Chișinău) — small expat retiree community; **Romanian-citizenship-by-descent** is the practical EU-passport path for many MD residents (one of the cheapest EU-adjacent retirement bases by COL)
- 🇶🇦 QA (West Bay, The Pearl, Lusail) — small UK/IN/PH/EG/JOR expat retiree community; ~3.05M pop (12% Qatari + 88% expat); high-income segment dominant
- 🇸🇦 SA (Riyadh DQ, Jeddah Corniche, NEOM, Red Sea) — small UK/US/IN expat retiree community; ~36.4M pop (63% Saudi + 37% expat); Vision 2030 mega-projects (NEOM, Qiddiya, Diriyah, Red Sea, AlUla, Roshn) drive employment + foreign retiree pull
- 🇵🇪 PE (Lima Miraflores/Barranco/San Isidro; Cusco; Arequipa) — moderate US/EU/JP expat retiree community; Lima Metro ~10.7M; Spanish dominant + English in Miraflores/San Isidro expat zones
- 🇪🇨 EC (Cuenca, Quito Cumbayá/La Floresta, Salinas/Olón coast) — **Cuenca particularly strong US/CA expat retiree hub** (International Living top-rank); ~17.7M pop (Quito ~2M, Guayaquil ~2.7M, Cuenca ~600k); Spanish + Kichwa/Shuar; English in Cuenca expat zone
- 🇵🇾 PY (Asunción Carmelitas/Villa Morra, Encarnación) — small but growing AR/BR/RU/EU expat retiree community; ~7.4M pop; Spanish + Guaraní co-official; Mennonite German communities
- 🇦🇲 AM (Yerevan Kentron/Arabkir) — moderate diaspora repatriation segment (US ~1M, RU ~2M, FR, AR, LB, IR diasporas); ~2.78M pop + ~7M global diaspora; **post-2022/2023 Karabakh war + ~120k displaced Sep 2023 + Russian-relocant wave 2022-24 (~50% peak Yerevan appreciation)**; Armenian + Russian widely + English in tech/tourism
- 🇦🇿 AZ (Baku Yasamal/Nasimi) — small UK/TR/IR/RU expat retiree community; ~10.16M pop (Baku ~2.4M); Azerbaijani (Latin script since 2001) + Russian + English business + Turkish mutually intelligible; very low crime; oil-revenue stabilized economy
- 🇹🇳 TN (Tunis La Marsa/Carthage/Sidi Bou Said, Sousse, Hammamet, Djerba) — moderate FR/IT/DE/UK retiree community; FR cultural + linguistic ties strong; ~12.07M pop (Tunis Metro ~2.7M); Arabic + French in business/property + Tamazight + Tunisian Arabic dialect
- 🇮🇳 IN (Goa, Pondicherry, Kodagu, Kasauli/Shimla hill stations; Bengaluru/Pune urban) — small UK/RU/IL/Israeli/AU/CA expat retiree community concentrated in Goa coastal (Anjuna/Vagator/Assagao/Calangute) + Pondicherry French-quarter; ~1.428B pop (Mumbai 21M / Delhi NCR 33M / Bengaluru 13M); 22 scheduled languages + Hindi/English Union official; **English in business + legal + healthcare**; **NO golden-visa via real estate** (UNIQUE absence); **OCI lifetime multi-entry for Indian-origin descendants** is the practical retiree pathway; LRS USD 250k/yr cap on outbound remittance
- 🇳🇬 NG (Lagos VI/Ikoyi/Lekki, Abuja Maitama/Asokoro, Calabar) — small UK/IN/CN/LB diaspora retiree community concentrated in Lagos VI + Lekki gated communities + Abuja Maitama/Asokoro; ~218M pop (Lagos 22M largest African city); English official + Yoruba/Igbo/Hausa + Pidgin universal; **security risk requires private security + gated communities**; energy autonomy mandatory (generators + solar); 2024-25 cost-of-living protests + Tinubu reforms ongoing
- 🇰🇪 KE (Karen, Lavington, Westlands, Runda, Muthaiga, Kitisuru — Nairobi; Diani — Mombasa coast) — moderate UK/US/IT/DE/IN/diaspora retiree community concentrated in Nairobi expat suburbs (Karen British-cultural roots) + Diani beach south of Mombasa; ~55M pop (Nairobi Metro 5M, Mombasa 1.4M); English + Kiswahili official; **NO golden-visa via real estate** (UNIQUE absence in EAC); **Class K Resident Permit KES 200k+/yr passive income** is the practical retiree pathway; SGR Mombasa-Nairobi-Naivasha-Kisumu drives corridor RE; Safaricom 5G + M-PESA universal
- 🇯🇴 JO (Amman Abdoun/Sweifieh/Khalda; Aqaba ASEZ; Dead Sea resorts) — moderate Iraqi+Syrian+Palestinian diaspora + GCC retiree community + small UK/US/FR/AU/CA expat retiree community; ~11.4M pop (Amman Metro 4.5M, Zarqa 1.5M, Irbid 1.9M, Aqaba 200k); Arabic official + English business/tourism/medical (English-medium hospitals) + French educated diaspora; **CBI Jordan since 2018** (JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport — WEAK passport for mobility plays, rational mainly for diaspora reconnection / GCC business utility); Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable); among most water-poor globally
- 🇴🇲 OM (Muscat — Al Mouj / The Wave / Madinat Al Sultan Qaboos / Qurum / Shatti Al Qurum; Salalah Khareef-zone) — small UK/US/IN/PK/SA/EG/JOR expat retiree community; ~5.0M pop (Muscat Metro 1.7M, ~38% expat); Arabic official + English business; **5-yr ITC Investor Residency ≥OMR 250k (~USD 650k) freehold / 10-yr ITC ≥OMR 500k (~USD 1.3M)** Royal Decree 89/2021; Long-term Retiree ≥OMR 4,000/mo pension (~USD 10,400); **NO citizenship-by-investment** (Omani nationality strict); cyclone exposure HIGH (Gonu/Mekunu/Shaheen baseline); Vision 2040
- 🇧🇭 BH (Manama Seef / Diplomatic Area / Juffair / Adliya / Saar; Amwaj Islands; Riffa) — small UK/US/IN/PK/SA expat retiree community; ~1.49M pop (~52% Bahraini + 48% expat); Arabic official + English business + everyday widely; **Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k) → 10-yr renewable Self-Sponsored Residence Permit**; **Golden Residency Decree 16/2022** 10-yr for property owners ≥BHD 200k OR investors / talented / retirees (BHD 4k/mo); NO CBI; medium COL (cheaper than UAE Dubai but more expensive than OM); Saudi Causeway integration (King Hamad Causeway 2 planned)
- 🇰🇼 KW (Kuwait City — Salmiya / Salwa / Mishref / Bayan / Salwa; Hawalli) — small UK/US/IN/EG/PH/BD/SY/LB expat retiree community pathway VERY constrained; ~4.85M pop (~30% Kuwaiti + 70% expat — largest IN/EG/BD/PH/SY); Arabic official + English business + tech + medical; **NO golden-visa via real estate (UNIQUE absence in GCC)** — residency entirely via employment Iqama (Decree-Law 17/1959); citizenship effectively impossible (Decree-Law 15/1959); Bedoon stateless population pressing issue; Vision 2035
- 🇱🇧 LB (Beirut Achrafieh / Verdun / Hamra / Mar Mikhael / Gemmayzeh; Mount Lebanon Broummana / Beit Mery; Byblos / Jbeil) — large Lebanese diaspora retiree-returnee cohort (~13M global Mahjar diaspora — far larger than 5.5M domestic); ~5.5M pop (incl ~1.5M Syrian + ~470k Palestinian refugees) — Beirut Metro 2.4M; Arabic + French de facto + English in tech/business/healthcare + Armenian Beirut Bourj Hammoud; high COL Beirut for fresh-USD earners (locals have collapsed wealth); foreign-buyer cohort dominated by Lebanese diaspora returnees (US/CA/AU/FR/BR/AR diaspora dominant); **post-2019 banking collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war Sep-Nov 2024**; Lebanese descent streamlined naturalization; dual citizenship since 2007

### Limited / language-barrier
- 🇩🇪🇦🇹🇨🇭 DE/AT/CH inland: German required for admin
- Nordics: limited expat retiree community due to cost
- Eastern EU + Balkans: smaller communities
- 🇯🇵 JP — Japanese required outside expat enclaves; admin almost exclusively JP-language
- 🇪🇬 EG — Arabic-dominant; French in some elite circles; English limited outside tourism
- 🇨🇴🇺🇾🇨🇱 CO/UY/CL — Spanish required for daily life
- 🇻🇳 VN — Vietnamese required; English limited outside tourism districts

## Cost of living rough ranking (cheapest → expensive for retirees)

| Tier | Countries |
|---|---|
| **Cheap** | AL, BA, RS, MK, ME, BG, RO, HU, GE, EG, VN, PH, ID, MA, **MD**, **PY**, **AM**, **AZ**, **TN** (outside Tunis), **EC**, **IN** (Tier-3 cities), **NG** (outside Lagos prime), **KE** (outside Nairobi expat suburbs) |
| **Mid-low** | PL, CZ, SK, GR, PT, ES (interior), IT (S), CR, PA, MX, TR, TH (provincial), CO, DO, ZA, **PE** (outside Lima Miraflores), **TN** (Tunis), **JO** (outside Amman prime), **LB** (collapsed-wealth locals — fresh-USD COL inverts) |
| **Mid** | ES (coast), PT (Lisbon/Algarve), IT (TC/Umbria), HR, CY, MT, EE, LV, LT, MY (KL/Penang), TH (Bangkok/Phuket), CL, UY, **TW (Taipei prime)**, **PE (Lima Miraflores/Barranco/San Isidro)**, **IN (Mumbai/Bengaluru/Delhi NCR prime)**, **KE (Nairobi Karen/Lavington/Runda/Muthaiga)**, **NG (Lagos VI/Ikoyi/Lekki)**, **JO (Amman Abdoun/Sweifieh/Khalda)** |
| **Mid-high** | FR, DE, AT, NL, BE, IE, UK, FI, SE, DK, JP (regional), IL (peripheral), AE (mid-tier emirate), **KR (Seoul prime)**, **AD**, **MO**, **OM (Muscat Al Mouj prime)**, **BH (Manama Seef/Diplomatic Area)**, **LB (Beirut Achrafieh — fresh-USD)** |
| **Expensive** | CH, NO, IS, LU, US (NYC/SF/Boston), JP (Tokyo central), IL (Tel Aviv), AE (Dubai prime), **SG**, **HK**, **MC**, **LI**, **QA (Doha West Bay/Pearl)**, **SA (Riyadh DQ prime)**, **KW (Kuwait City Salmiya/Bayan)** |

## Special retirement programs

| Country | Program | Threshold |
|---|---|---|
| GR | Foreign Pensioner Tax Regime | 7% flat on foreign-source for 15 yrs |
| IT | Southern Italy 7% regime | 7% flat for 9 yrs (S municipalities <20k pop) |
| PT | IFICI (NHR 2.0) | Pensions NO LONGER exempt — narrower scope |
| PA | Pensionado | $1,000/mo pension; massive discounts on services |
| CR | Pensionado | $1,000/mo (lifetime pension); Rentista $2,500/mo |
| MX | Temp/Permanent residency | Income/savings thresholds (UMA-based) |
| MY | **MM2H (Silver/Gold/Platinum + SEZ/SFZ, post-2024 reform)** | Silver/Gold/Platinum — USD 150k / 500k / 1M fixed deposit + compulsory residence ≥ RM 600k / 1M / 2M; no income requirement on MOTAC category pages (2026 data, source MOTAC) |
| TH | **LTR Wealthy Pensioner** + Retirement (Non-O) | LTR: USD 80k/yr OR USD 40-80k + USD 250k investment; Non-O: age 50+, THB 800k bank or THB 65k/mo |
| PH | **SRRV (Special Resident Retiree's Visa)** | USD 10k–50k deposit (most generous SE-Asia); 4 sub-classes |
| ID | **Retirement KITAP** | Age 55+, USD 1.5k/mo pension proof, health insurance, hire local staff |
| AE | **Retirement Visa (5-yr renewable)** | Age 55+; AED 1M property OR AED 1M savings OR AED 20k/mo income |
| TR | **Turquoise Card / Long-stay residence** | No formal retirement program; Turquoise Card via investment route |
| ZA | **Retired Person Visa** | Pension/income ZAR 37,000/mo (~USD 2k/mo) — verify 2026 threshold at DHA |
| DO | **Pensionado / Rentista** | USD 1.5k/mo pension OR USD 2k/mo rentista; 50% discount on transfer + property tax |
| CO | **Migrante M Visa — Pensionado** | MOH-recognized pension >COP 3× SMLMV (COP 5.25M ≈ USD 1,671/mo at the 2026 SMLMV COP 1,750,905 and TRM 3,144.14 — computed) |
| UY | **Tax residency** (no formal retirement visa) | 11-yr foreign interest+dividend exemption (Ley 19.937) |
| CL | Standard residency | No retirement-specific program; 3-yr foreign-income exemption from arrival |
| GE | **Visa-free 1 year** | ~95 nationalities; no retirement-specific scheme needed |
| IL | **Aliyah (Olim)** | Direct citizenship for Jewish ancestry; 10-year tax holiday on foreign income (Amendment 168) |
| MA | **Carte de Séjour (long-stay)** | Standard residence permit; pension 80% abatement if remitted in DH |
| EG | **PM Decree 3099/2019 investor route** | USD 250k non-refundable Treasury contribution (GAFI form); outcome citizenship vs permanent residency unreconciled; verify currency-control / Form 4 risks |
| US | None federal; state-level | No US retirement visa for non-citizens (immigration via family/EB-5/marriage); domestic retirees: TX/FL/TN/NV/WA/SD/WY/AK no state income tax |
| JP | None retirement-specific | Highly Skilled Professional / Investor / Spouse routes; no pensioner-class visa |
| SG | None retirement-specific | LTSV (Long-Term Social Visit Pass for parent of EP/PR holder); GIP (S$10M business / S$25M family-office / S$200M-SFO via EDB) |
| HK | **CIES reactivated Mar 2024** | HK$30M total investment + up to HK$10M residential (Investments Office, ImmD); also QMAS / Top Talent Pass / IANG |
| KR | **F-2 Investor 5yr / F-5 PR** | ₩600M investment via designated business; F-4 for Korean diaspora; no property-only retirement track |
| TW | **Gold Card / Plum Blossom long-stay** | Gold Card 4-yr work+residency (no investment, high-skill); APRC after 5yr; no formal retirement visa |
| MO | **Investment Residence SUSPENDED since 2007** | Talent Programme 2024 NOT property-linked; verify with IPIM |
| AD | **Residència Passiva / Activa** | ~€600k investment OR €350k + €50k AFA deposit; passive ≥90d/yr / active ≥183d/yr; CASS social-security mandatory; 20yr to naturalisation |
| MC | **Carte temporaire → ordinaire → privilégiée** | ~€500k bank deposit + property purchase or rental practitioner; ~38k pop; NO PIT (except FR via 1963 Convention); NO CGT |
| LI | **Quota-based** | ~28 EEA + ~17 third-country/year via lottery; Personal Residence Programme rare petition; CH-integrated practice |
| MD | **Investor Residency Law 200/2010** | €250k 5yr investment → naturalisation eligibility 8yr; CBI ENDED via Law 100/2020; **no formal Digital Nomad Visa as of 2026** |
| QA | **NO citizenship-by-investment (Law 38/2005)**; **Investor Residency Law 21/2018 ≥QAR 730k → 5yr renewable**; PR Law 10/2018 ≥QAR 1M (capped ~100/yr) | Verify with MoI / GAT (General Authority of Customs); no formal pension-class visa |
| SA | **Premium Residency Vision 2030** | SAR 800k one-time / SAR 100k/yr renewable / Real-Estate-Owner SAR 4M; Mecca/Medina Muslim-only ownership constitutional; verify with Premium Residency Center (Iqama Premium) |
| PE | **Investor Visa USD 30k BUSINESS** (NOT real-estate exclusively) / **Rentista USD 1,500/mo** passive | PR after 3yr continuous; Peruvian passport after 2yr PR; verify with MIGRACIONES Peru |
| EC | **Pensioner Visa USD 1,500/mo** / **Investor Visa USD 42,500** (~100×SBU 2026 SBU USD 470/mo) | 2yr Temporary → Permanent after 21mo; naturalization 3yr PR; verify with Cancillería Ecuador |
| PY | **Resolución SET 1186/2023 reformed PR** — formerly cheapest formal RBI (~USD 5,200) → now **USD 70k SUACE business invest** OR active SET RUC | Citizenship 3yr continuous PR; verify with DGM / SUACE |
| AM | **Investor Residency AMD 50M (~USD 130k) deposit OR property → 5yr renewable**; **Citizenship by descent (Diaspora) Art. 13 streamlined** | Naturalization 3yr PR + dual citizenship since 2007; verify with Ministry of Foreign Affairs / Migration Service |
| AZ | **TRP via real estate ≥AZN 100k (~USD 60k) → 1yr renewable to 5+** | PR after 8yr continuous TRP; Strategic Investor Visa AZN 540k priority sectors; naturalization 5yr PR + Azeri language; **dual citizenship LIMITED exceptions**; verify with State Migration Service |
| TN | **Investor Residence Permit ≥TND 1M (~USD 320k)** | Citizenship 5yr continuous PR + Arabic + dual since 2014; **Tunisia Investor Visa drafted 2024 NOT gazetted** — verify gazette status; verify with Ministère de l'Intérieur |
| IN | **NO golden-visa via real estate (UNIQUE absence)** — India does NOT offer property-pegged residency or citizenship | OCI lifetime multi-entry for Indian-origin descendants (registered foreign citizens of India); naturalization 11+yr (very strict); dual citizenship NOT allowed; verify with MHA / Bureau of Immigration |
| NG | **NO golden-visa via real estate** — STR-1 Investor visa USD 100k business is the longer-term pathway | Naturalization 15+yr + Nigerian language + dual NOT allowed for native-born; verify with NIS (Nigeria Immigration Service) |
| KE | **NO golden-visa via real estate (UNIQUE absence in EAC)** | Class A1 Investor USD 100k business / **Class K Resident KES 200k+/yr passive** / PR 7yr / Citizenship 7yr + Swahili (dual allowed since 2010); verify with Department of Immigration Services |
| JO | **CBI Jordan since 2018** — JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport, ~50 visa-free destinations (WEAK passport for mobility plays); Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable); Bona Fide Investor ≥JOD 50k bank deposit 1+yr; Aqaba ASEZ separate framework | Verify with Ministry of Interior / Investment Commission |
| OM | **Investor Residency Royal Decree 89/2021** — 5-yr ≥OMR 250k (~USD 650k) ITC freehold / 10-yr ≥OMR 500k (~USD 1.3M) ITC; **Long-term Retiree Residence ≥OMR 4,000/mo pension (~USD 10,400)** | NO citizenship-by-investment (Omani nationality strict); cyclone exposure HIGH baseline; verify with MoCIIP / ROP |
| BH | **Bahrain Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k)** → 10-yr renewable Self-Sponsored Residence Permit (incl. spouse + children); **Golden Residency Decree 16/2022** 10-yr renewable for property owners ≥BHD 200k OR investors / talented / retirees (BHD 4k/mo) | NO CBI; verify with Nationality, Passports & Residence Affairs |
| KW | **NO golden-visa via real estate (UNIQUE absence in GCC)** | Residency entirely via employment Iqama (Decree-Law 17/1959); 5+yr to PR claim rarely granted; citizenship effectively impossible (Decree-Law 15/1959); Bedoon stateless population pressing issue; verify with Public Authority for Civil Information / MoI |
| LB | NO golden-visa via real estate; **Investor Residency ≥USD 50k Lebanese business (1-yr renewable)**; property ownership ≥USD 200k can support residency application but not automatic; Lebanese descent streamlined naturalization (~13M global Mahjar diaspora) | Citizenship 5+yr continuous + Arabic (rarely granted to non-Arabs); dual citizenship since 2007; verify with Direction Générale de la Sûreté Générale |

## Decision framework for retirees

```
1. CITIZENSHIP CHECK → which countries does your passport let you settle in?
   - EU citizen: 27 EU + EEA freely; UK requires visa post-Brexit
   - UK citizen: post-Brexit visa for EU; FOM remains for IE
   - US/CA citizen: visa-free tourism most; settlement requires visa
   - LatAm: most allow visa-free 90 days; settlement easier than EU

2. PENSION TAX → where will your pension be most tax-efficient?
   - Filter EU/territorial: GR 7%, IT 7% (S), PT IFICI (narrow), CY 5%, PA territorial, MX territorial, CR territorial
   - Filter non-tax / favourable: AE (no PIT), UY (11-yr foreign-int+div), IL (10-yr Olim holiday), MA (80% abatement), GE (territorial), CL (3-yr new-resident exemption), DO/PA territorial-leaning
   - Caution: TH post-2024 remittance rules tightened — verify; JP has 5-yr "non-permanent resident" carve-out but limited

3. HEALTHCARE → where will your healthcare be best/cheapest?
   - EU pensioner with S1: any EU member state (PT/ES/IT/GR/MT/CY popular)
   - Non-EU: private insurance + state where reciprocal exists
   - Quality + access: PT > ES > IT > GR > MT > CY (public-system rough order)

4. CLIMATE → can you tolerate the climate year-round?
   - Mild winter: PT, ES, IT (south), GR, MT, CY, MX, PA, CR
   - Cool summer: NL, BE, IE, UK, FR (Brittany/Normandy), DE (north), Nordics
   - Both (rare): PT (Lisbon), ES (Galicia/N coast), FR (Atlantic coast)

5. LANGUAGE → can you live in the language?
   - English-friendly: NL, IE, UK, MT, CY, PT (Algarve coast), some SE/FI/NO/DK
   - Dual: BE, CH, LU, DE/AT (English in cities), ES coastal, IT (some)
   - Required learning: rest

6. BUDGET → does the cost align?
   - <€1,500/mo: AL, BA, RS, MK, ME, BG, RO, GE, EG, VN, PH (provincial), ID (provincial), MA (provincial)
   - €1,500-2,500: PT (interior), ES (interior), IT (S), HR, GR, MT, CY, EE/LV/LT, MX, PA, CR, TR (Aegean), TH (Chiang Mai/Hua Hin), CO (Medellín), DO (Las Terrenas), ZA (Garden Route)
   - €2,500-4,000: PT/ES/IT (coastal), FR (provincial), DE/AT (provincial), NL, BE, MY (KL/Penang), TH (Bangkok/Phuket prime), UY (Punta del Este), CL (coastal), JP (regional), IL (peripheral)
   - €4,000+: CH, NO, IS, LU, US (NYC/SF), JP (Tokyo central), IL (Tel Aviv), AE (Dubai prime); major capitals (Paris, London, Amsterdam, Munich)
```

## Tier-1 + Tier-2 country profiles (added 2026-05)

Each profile lists: pension-tax regime · healthcare access · climate/lifestyle · expat density · retirement-visa pathway. Cross-link each visa pathway to [`visa-programs.md`](./visa-programs.md) for thresholds and current status.

### 🇺🇸 US
- **Pension tax**: Worldwide PIT for residents; foreign-source pension taxable; treaty relief common (DTAA network)
- **Healthcare**: Medicare from age 65 (resident-only, requires 10+ yrs payroll contributions); ACA marketplace alternative for under-65; **state variation material** (TX/FL/TN/NV no state PIT)
- **Climate**: FL/AZ/CA-S/TX warm winters (FL hurricane Jun-Nov; AZ extreme summer)
- **Expat density**: N/A for inbound retirees (no retirement visa); retiree mobility is intra-state
- **Visa**: **No US retirement visa** — non-citizens enter via family/EB-5/spouse routes only

### 🇹🇷 TR
- **Pension tax**: Worldwide for tax residents; progressive PIT (2026: 15-40%); treaty mitigates double-tax
- **Healthcare**: SGK universal for residents incl. expats; private network strong (Acibadem, Memorial); ~30-50% of UK private cost
- **Climate**: Aegean coast (Bodrum, Antalya, Fethiye, Alanya) 14-19°C winter, 28-35°C summer; rising heatwave + water-stress concern
- **Expat density**: Large UK/DE/RU/Scandinavian retiree presence on Aegean coast since 2000s
- **Visa**: **Turquoise Card** (investment-route long-stay) or standard residence permit; no formal pension-class visa — see `visa-programs.md`

### 🇦🇪 AE
- **Pension tax**: **NO income/pension tax** for individuals; territorial system; corporate 9% (FDL 47/2022) doesn't reach personal pension income
- **Healthcare**: Mandatory private health insurance (DHA Dubai / DOH Abu Dhabi); high quality but **premiums spike post-60**
- **Climate**: 18-25°C winter (excellent); **summer 42-48°C May-Sep — outdoors near-uninhabitable**
- **Expat density**: Large UK/IN/RU/EU communities; Dubai marinas + Abu Dhabi
- **Visa**: **Retirement Visa (5-yr renewable, age 55+)** — AED 1M property OR AED 1M savings OR AED 20k/mo income — verify 2026 thresholds at GDRFA

### 🇯🇵 JP
- **Pension tax**: Worldwide for residents; foreign pension taxable but treaty-relief common; "non-permanent resident" 5-yr carve-out for non-JP-source income not remitted
- **Healthcare**: Universal NHI (Kokuho) for all residents incl. expats; 30% co-pay; **language barrier severe outside Tokyo/Yokohama/Osaka**
- **Climate**: 4-season; Tokyo 5-10°C winter, 28-32°C humid summer; Fukuoka/Okinawa milder
- **Expat density**: Small but established Western retiree community; concentrated in Tokyo/Yokohama/Fukuoka
- **Visa**: **No formal retirement visa** — Highly Skilled Professional / Investor / Spouse routes only; pathway thin for typical retirees

### 🇹🇭 TH
- **Pension tax**: LTR Wealthy Pensioner: flat 17% on most assessable income; **2024 remittance rule reform** — foreign-source income remitted to TH may now be taxable (verify with Revenue Dept / tax adviser)
- **Healthcare**: Universal Coverage Scheme for citizens; expats use private (Bumrungrad, Bangkok Hospital — JCI-accredited); LTR requires USD 50k health insurance OR USD 100k deposit
- **Climate**: Tropical 22-32°C; Chiang Mai cool-season Nov-Feb (best months); **PM2.5 burning season Feb-Apr severe in N TH**
- **Expat density**: UK/US/AU/DE/Scandinavian retirees; Chiang Mai writer/retiree hub, Hua Hin Royal-family adjacent, Phuket beach
- **Visa**: **LTR Wealthy Pensioner** (USD 80k/yr OR USD 40-80k + USD 250k investment) or **Non-O Retirement** (age 50+, THB 800k bank or THB 65k/mo) — see `visa-programs.md`

### 🇩🇴 DO
- **Pension tax**: Foreign pension exempt from DO tax; territorial system; **50% discount on transfer + property tax** under retirement law
- **Healthcare**: SeNaSa public + SDSS private; expats use private (Hospiten, CEDIMAT); coordination with US Medicare limited
- **Climate**: Tropical 24-31°C; **hurricane season Jun-Nov** (Atlantic exposure)
- **Expat density**: Las Terrenas FR/IT enclave; Punta Cana US/CA; Sosúa DE/Scandinavian — distinct national clusters
- **Visa**: **Pensionado (USD 1.5k/mo) / Rentista (USD 2k/mo) / Investor (USD 200k)** → 2-3 yr citizenship pathway

### 🇨🇴 CO
- **Pension tax**: Worldwide PIT for tax residents (>183 days); pensionado visa holders pay CO PIT at progressive UVT-based rates
- **Healthcare**: EPS contributory (residents pay ~12% income); private (Sanitas, Colsanitas) Medellín/Bogotá compares to US private at fraction of cost
- **Climate**: **Medellín "City of Eternal Spring"** 18-22°C year-round (altitude-moderated); Cartagena 26-32°C tropical
- **Expat density**: Surge in US/CA digital-nomad-aging-into-retirement; Medellín El Poblado/Laureles, Cartagena historic centre
- **Visa**: **Migrante M Visa Pensionado** — MOH-recognized pension >COP 3× SMLMV (COP 5.25M ≈ USD 1,671/mo at the 2026 SMLMV COP 1,750,905 and TRM 3,144.14 — computed) — see `visa-programs.md`

### 🇺🇾 UY
- **Pension tax**: 11-year exemption on foreign interest+dividends (Ley 19.937, 2020+ reform); pension itself not exempt but progressive PIT modest; territorial-leaning
- **Healthcare**: Mutualistas (private cooperatives, ~USD 80-150/mo) excellent — most expats join; FONASA public for residents
- **Climate**: Humid subtropical; Punta del Este/Montevideo 12-16°C winter, 22-28°C summer
- **Expat density**: Moderate AR seasonal + permanent EU; Punta del Este, Colonia, Montevideo Carrasco
- **Visa**: **Tax residency** via investment OR 60-day physical presence; no formal retirement visa

### 🇨🇱 CL
- **Pension tax**: 3-yr foreign-source income exemption for new residents (DL 824 Art. 3); pensions taxable at progressive PIT thereafter (up to 40%)
- **Healthcare**: Dual FONASA / Isapres; retirees often Isapres but premiums rise sharply with age (post-2023 Constitutional Court ruling reshaping pricing)
- **Climate**: Mediterranean coast (Coquimbo, Ñuble) 12-18°C winter; arid trend / drought concern
- **Expat density**: Small but growing US/EU; Viña del Mar, La Serena
- **Visa**: Standard residency (no retirement-specific program); UF inflation-indexing protects real-asset purchases

### 🇿🇦 ZA
- **Pension tax**: Worldwide for tax residents; foreign pension may be exempt under s10(1)(gC) ITA if for services rendered abroad — verify per-case with SARS
- **Healthcare**: Public overstretched; expats universally on private (Discovery Health, Bonitas) + medical aid; **quality high but ZAR volatility risk**
- **Climate**: Cape Town/Garden Route Mediterranean 12-18°C winter; **Day Zero water-scarcity overlay** (2018 near-miss recurring)
- **Expat density**: UK/DE/NL retirees; Cape Town suburbs, Plettenberg Bay, Knysna
- **Visa**: **Retired Person Visa** — ZAR 37,000/mo pension/income (~USD 2k/mo) — verify 2026 threshold at DHA

### 🇬🇪 GE
- **Pension tax**: Territorial — foreign-source income not taxed; 1% small-business / favourable individual rates
- **Healthcare**: Universal Healthcare Program (state) for citizens/residents; private (Mediclub, Medi) Tbilisi growing; expats often medivac for serious conditions
- **Climate**: Continental — Tbilisi 2-7°C winter, 25-30°C summer; Batumi humid subtropical Black Sea
- **Expat density**: Major RU+UA surge post-2022; growing US/EU crypto-retiree subsegment; Tbilisi, Batumi
- **Visa**: **Visa-free 1-year for ~95 nationalities**; no retirement-specific scheme needed

### 🇮🇩 ID
- **Pension tax**: Worldwide for residents (>183 days); foreign pension taxable at progressive PIT; some treaty relief
- **Healthcare**: BPJS Kesehatan universal for residents incl. KITAS/KITAP holders; quality variable; Bali expats use private (BIMC, Siloam); **medivac to SG common**
- **Climate**: Tropical 26-30°C; Bali wet/dry seasons; volcanic risk (Agung, Merapi)
- **Expat density**: Bali — Ubud, Canggu, Sanur — large AU/EU/US community
- **Visa**: **Retirement KITAP** — age 55+, USD 1.5k/mo pension proof, health insurance, must hire local staff

### 🇲🇾 MY
- **Pension tax**: Foreign-source income exempt under territorial principle (post-2022 amendments narrowed for residents — verify with IRB)
- **Healthcare**: Strong universal public + private (Sunway, Pantai, Gleneagles); Penang/KL hospitals JCI-accredited; **medical-tourism destination**
- **Climate**: Tropical 25-32°C year-round; humid; minimal seasonal variation
- **Expat density**: UK/AU/SG/JP retirees via MM2H legacy + new tiers; Penang, KL, Johor Bahru
- **Visa**: **MM2H (Silver/Gold/Platinum + SEZ/SFZ, post-2024 reform)** — USD 150k–1M fixed deposit + compulsory residence ≥ RM 600k–2M (2026 data, source MOTAC) — see `visa-programs.md`

### 🇻🇳 VN
- **Pension tax**: Worldwide for residents (>183 days); foreign pension at progressive PIT (2026: up to 35%)
- **Healthcare**: Universal Health Insurance for residents; expats use private (Vinmec, FV Hospital); evac to TH/SG for complex cases
- **Climate**: Da Nang/Hoi An 22-32°C; **typhoon season Sep-Nov on central coast**; Saigon 25-32°C
- **Expat density**: Growing US/EU/AU; Da Nang, Hoi An, Saigon expat enclaves; **visa pathway thinner than TH/PH/MY**
- **Visa**: LD Labour visa or family-route only; **no formal retirement visa** — see `visa-programs.md`

### 🇵🇭 PH
- **Pension tax**: Foreign pension NOT taxed by PH for SRRV holders; territorial-style for non-resident-source income
- **Healthcare**: PhilHealth universal for residents; private (St. Luke's, Makati Med) strong in Metro Manila; provincial quality patchy
- **Climate**: Tropical 25-32°C; **typhoon season Jun-Nov** (Davao less typhoon-exposed); Cebu/Bohol mid-exposure
- **Expat density**: US/AU/JP/KR retirees; Cebu, Dumaguete, Bohol, Davao
- **Visa**: **SRRV (most generous SE-Asia)** — USD 10k–50k deposit depending on age/pension status; 4 sub-classes — see `visa-programs.md`

### 🇮🇱 IL
- **Pension tax**: New immigrants (Olim) get **10-year tax holiday** on foreign-source income+capital gains (Amendment 168, 2008); thereafter worldwide PIT
- **Healthcare**: Universal via 4 Sick Funds (Kupot Holim — Clalit, Maccabi, Meuhedet, Leumit); **Olim entitled from arrival**; English support varies
- **Climate**: 10-18°C winter, 28-35°C dry summer; Tel Aviv coastal humid
- **Expat density**: Large US/FR/UK/RU Olim retiree community; Tel Aviv, Netanya, Ra'anana, Jerusalem
- **Visa**: **Aliyah (Law of Return)** — direct citizenship for Jewish ancestry; purchase-tax incentives for Olim — see `visa-programs.md`

### 🇲🇦 MA
- **Pension tax**: Foreign pensions: **80% abatement if transferred permanently to MA in DH** (Art. 76 CGI); effective rate dramatically reduced
- **Healthcare**: AMO universal scheme being expanded (2024-2026 reform); expats use private (Cliniques Akdital, Cheikh Zaid); **French-system standards**
- **Climate**: Marrakech 18-22°C winter (35-40°C summer); Essaouira/Tangier Atlantic-cooled milder
- **Expat density**: FR retirees dominant; UK/DE growing; Marrakech, Essaouira, Tangier, Agadir
- **Visa**: **Carte de Séjour (long-stay)** — standard residence permit; no retirement-specific program

### 🇪🇬 EG
- **Pension tax**: Foreign-source pension generally not taxed by EG (territorial application varies — verify with ETA)
- **Healthcare**: New Universal Health Insurance (2018 law, phased rollout); expats use private (Cleopatra, As-Salam International); **medivac for serious cases recommended**
- **Climate**: Hurghada/Sahel/Sharm 18-35°C; very dry; summer extreme
- **Expat density**: RU/UA/DE/UK retirees; Hurghada, El Gouna, Sahel; **EGP currency volatility risk material** (post-2024 devaluations)
- **Visa**: **PM Decree 3099/2019 investor route** — USD 250k non-refundable Treasury contribution; outcome citizenship vs permanent residency unreconciled between GAFI and US State Dept 2025 ICS; verify currency-control / Form 4 repatriation risks before committing

## Tier-3 country profiles (added 2026-05-01)

### 🇸🇬 SG
- **Pension tax**: Foreign-source income generally NOT taxed for individuals received in SG (verify with IRAS); resident PIT 0-22% progressive on SG-source; CGT NONE
- **Healthcare**: MediShield Life universal for citizens/PRs; non-resident expats use private (Mount Elizabeth, Raffles, Gleneagles — JCI-accredited); among highest-quality globally per WHO 2023 indicators; English universal
- **Climate**: Equatorial 24-32°C year-round; minimal seasonal variation; very high humidity; Changi best-in-world airport for medical travel
- **Expat density**: Small high-income retiree community; cosmopolitan; English-medium pervasive
- **Visa**: **No retirement visa via property**; GIP (S$10M business / S$25M family-office / S$200M-SFO via EDB); ONE Pass (S$30k/mo); LTSV for parents of EP holders; GST 9% from Jan 2024 — see `visa-programs.md`

### 🇭🇰 HK
- **Pension tax**: Salaries Tax territorial — HK-source only (max 17% progressive or 15% standard); **foreign pension generally not taxed**; Property Tax 15% on rental income; HKD pegged to USD via LERS 7.75-7.85 (HKMA Convertibility Undertaking)
- **Healthcare**: HA public network — eligible-persons subsidy for HKID holders; expats commonly mix HA + private (Matilda, Hong Kong Adventist, Canossa); English universal
- **Climate**: Humid subtropical 14-19°C winter, 28-33°C humid summer (Jun-Sep); typhoon season Jul-Oct
- **Expat density**: Moderate UK/AU/CA professional-retiree community; partial post-2020 outflow, partial recovery 2023-2026
- **Visa**: **CIES reactivated Mar 2024** — HK$30M total investment + up to HK$10M residential (Investments Office); also QMAS / Top Talent Pass / IANG; **Article 23 (Mar 2024) sentiment factor** for some retirees — see `visa-programs.md`

### 🇰🇷 KR
- **Pension tax**: Worldwide for residents (>183 days); progressive 6-45%; CGT 6-45% separate + multi-home top rate up to 75%; **foreign-source income exemption first 5 of 10 yrs** for newly-resident foreign workers (PIT Act Art. 18-2)
- **Healthcare**: NHIS universal — mandatory enrolment for foreign residents 6+ months; quality high (Samsung Medical, Asan, Severance — JCI-accredited); **Korean dominant in admin** outside Itaewon/Gangnam English-medium clinics
- **Climate**: Cold continental — Seoul -5 to +3°C winter, 26-31°C humid summer; Jeju milder; aging society
- **Expat density**: Small US/EU/JP retiree community; clusters Itaewon/Hannam-dong/Pangyo; **gigabit fiber norm** (KT/SK/LG); Naver Maps + Kakao Maps
- **Visa**: **F-2 Investor (₩600M, 5yr) → F-5 PR**; F-4 for Korean diaspora; no property-only retirement track; **jeonse system** unique rental-deposit risk for renters (post-2022 HUG fraud-crisis reforms)

### 🇹🇼 TW
- **Pension tax**: Worldwide for residents (>183 days); progressive 5-40%; **AMT regime** may apply on foreign-source >NT$7M; 6% surtax on certain investment income — verify with NTBT
- **Healthcare**: NHI universal — mandatory enrolment for ARC/APRC holders after 6 months; consistently top-ranked globally on accessibility/cost (NHIA reports); English in major Taipei hospitals (NTUH, Taipei Medical, Cathay General)
- **Climate**: Tropical-subtropical; Taipei 14-20°C winter, 28-32°C summer; **2024 Hualien M7.4 earthquake** material to seismic disclosure; aging society
- **Expat density**: Moderate US/JP/EU retiree presence; clusters Tianmu/Da'an/Xinyi/Neihu; gigabit FTTH norm (Chunghwa, Taiwan Mobile); HSR + Taipei MRT
- **Visa**: **No retirement visa via property**; **Gold Card** 4-yr work+residency (no investment, high-skill route); Plum Blossom long-stay; **APRC after 5yr** — see `visa-programs.md`

### 🇲🇴 MO
- **Pension tax**: Macao Professional Tax territorial — foreign pension NOT subject to MO PIT; verify with DSF
- **Healthcare**: SSM (Serviços de Saúde de Macau) public + Hong Kong-style private gap-cover common; resident card holders entitled; Cantonese + Portuguese dominant; English in tourism-zone clinics
- **Climate**: Humid subtropical 14-20°C winter, 28-32°C summer; typhoon season; **post-Hato 2017 storm-surge resilience reforms**
- **Expat density**: Very small expat retiree community; ~673k pop; Cantonese + Portuguese co-official + English in tourism; gaming ~50% GDP (concessões 2022 renewed 10yr)
- **Visa**: **Investment Residence SUSPENDED since 2007**; Talent Programme 2024 NOT property-linked; MOP-HKD-USD double peg — verify with IPIM

### 🇦🇩 AD
- **Pension tax**: IRPF 0/5/10% — **lowest in Western Europe**; foreign pension taxed at AD-resident progressive but max 10%; CASS social-security mandatory
- **Healthcare**: CASS mandatory for residents; covers AD network + cross-border to FR/ES per agreement; private gap-cover common; Catalan/Spanish/French admin
- **Climate**: Alpine 0-8°C winter, 18-25°C summer; ski-season Dec-Apr; high mountain isolation
- **Expat density**: Moderate ES/FR/PT retiree community (~75% non-Andorran of ~85k pop); 4G/5G via Andorra Telecom (state monopoly); EUR via Monetary Treaty 2011 (not Eurozone)
- **Visa**: **Residència Passiva ~€600k** OR €350k + €50k AFA; passive ≥90d/yr / active ≥183d/yr; CASS mandatory; **20yr to naturalisation**; **STR Llei 26/2024 + parish quotas** (verify per parròquia)

### 🇲🇨 MC
- **Pension tax**: **NO personal income tax** (except French nationals via 1963 Convention); **NO CGT**; tax-residence is the principal draw
- **Healthcare**: Caisses Sociales de Monaco for residents/employees; CHPG state hospital; cross-border to FR/IT for specialised cases; private clinics English-friendly
- **Climate**: Mediterranean 8-15°C winter, 24-29°C summer; among the mildest in Europe; **sea-level rise concern** (Plan Bleu / Plan Climat)
- **Expat density**: Small ultra-high-net-worth international retiree community (~38k pop, ~70% non-Monégasque); French official + English/Italian common; very high COL (highest globally per Numbeo / Knight Frank wealth indices)
- **Visa**: **Carte temporaire 1yr → ordinaire 3yr → privilégiée 10yr**; ~€500k bank deposit + property purchase or rental practitioner — verify with Sûreté Publique

### 🇱🇮 LI
- **Pension tax**: Foreign pension at LI personal-tax rates (combined federal + commune ~2.5-22.4% — among lowest CH-area); double-tax treaty with most OECD; CHF currency union with CH
- **Healthcare**: KVG-equivalent compulsory health insurance — closely modelled on CH LAMal; Vaduz hospital + cross-border to CH (St. Gallen, Zurich) standard; German-system standard
- **Climate**: Alpine 0-5°C winter, 18-24°C summer; CH-aligned climate
- **Expat density**: Very small (~40k pop, quota-based residency: ~28 EEA + ~17 third-country/year by lottery); German official; very high COL; **OECD top GDP/capita**; Vaduz capital ~5,800
- **Visa**: **NO investment-track residency**; quota-based lottery; **Personal Residence Programme rare petition only**; **Schengen via 2011 extension**; verify with Ausländer- und Passamt

### 🇲🇩 MD
- **Pension tax**: Worldwide for residents (>183 days); foreign pension at flat 12% PIT (one of lowest in Europe); territorial-leaning for non-residents; verify with SFS
- **Healthcare**: CNAM mandatory; expats commonly use private (Medpark, Repromed); **medical-staff emigration to RO/EU is structural concern**; Romanian + Russian dominant
- **Climate**: Cold continental — Chișinău -3 to +1°C winter, 22-28°C summer; **lowest COL in Europe**
- **Expat density**: Small expat retiree community; ~2.5M pop (excl. Transnistria); Romanian official + Russian widely spoken; gigabit fiber Moldtelecom + Orange MD + StarNet (one of fastest fiber penetrations in Eastern Europe); **EU candidate Jun 2022**; NO Schengen
- **Visa**: **Investor Residency Law 200/2010** — €250k 5yr → naturalisation eligibility 8yr; **CBI ENDED via Law 100/2020**; **no formal Digital Nomad Visa as of 2026**; **Romanian-citizenship-by-descent → EU passport path** for many MD residents; Transnistria scope excluded

## Tier-4 country profiles (added 2026-05-01)

### 🇶🇦 QA
- **Pension tax**: NO PIT for individuals — foreign pension NOT subject to QA personal taxation; corporate ~10% only
- **Healthcare**: HMC public network (eligibility-gated for sponsored residents); expats use private (Aspetar, Sidra Medicine, Doha Clinic); high quality, premium pricing for retirees age 60+
- **Climate**: 18-42°C; **summer 45°C+ near-uninhabitable outdoors May-Sep + sandstorms + 2018/2021/2024 Doha storm-surge floods**; FIFA World Cup 2022 legacy + Lusail metro
- **Expat density**: Small UK/IN/PH/EG/JOR retiree community; ~3.05M pop (12% Qatari + 88% expat); Doha West Bay / The Pearl / Lusail
- **Visa**: **NO citizenship-by-investment (Law 38/2005)**; **Investor Residency Law 21/2018 ≥QAR 730k → 5yr renewable**; PR Law 10/2018 ≥QAR 1M (capped ~100/yr); verify with MoI / GAT — see `visa-programs.md`

### 🇸🇦 SA
- **Pension tax**: NO PIT for individuals (Saudi PIT regime is GCC-citizen Zakat 2.5% + corporate 20% non-Saudi); foreign pension NOT subject to SA PIT
- **Healthcare**: MOH public for citizens; mandatory CCHI private health insurance for expats; private (Saudi German, Dr. Sulaiman Al Habib, King Faisal Specialist — JCI-accredited); Vision 2030 healthcare expansion
- **Climate**: 12-45°C; **interior 50°C+ summer + sandstorms + 2009/2011 Jeddah catastrophic floods + drought + groundwater depletion**; **Mecca/Medina constitutional restriction (Muslim-only ownership)**
- **Expat density**: Small UK/US/IN expat retiree community; ~36.4M pop (63% Saudi + 37% expat); Vision 2030 mega-projects (NEOM, Qiddiya, Diriyah, Red Sea, AlUla, Roshn) drive employment
- **Visa**: **Premium Residency Vision 2030** — SAR 800k one-time / SAR 100k/yr renewable / Real-Estate-Owner SAR 4M; Riyadh Metro Phase 1 Dec 2024 — see `visa-programs.md`

### 🇵🇪 PE
- **Pension tax**: Worldwide for tax residents (>183 days); foreign pension at progressive 8-30%; foreign-source income earned BEFORE arrival potentially non-taxable per Art. 6 LIR — verify with SUNAT
- **Healthcare**: EsSalud (contributory) + SIS (subsidized public) + private (Clínica Anglo Americana, Clínica Ricardo Palma, Auna network); Lima quality fair-good but evac to US/MX for serious cases common
- **Climate**: Lima coastal 16-26°C year-round (Pacific cool current); inland Andes higher; **Pacific Ring of Fire HIGH seismic + tsunami coastal + 2017/2023 El Niño catastrophic floods + huaicos + volcanic Misti/Ubinas/Sabancaya south**
- **Expat density**: Moderate US/EU/JP retiree community; Lima Miraflores/Barranco/San Isidro; Cusco; Arequipa; Lima Metro ~10.7M; Spanish dominant + English in expat enclaves
- **Visa**: **Investor Visa USD 30k BUSINESS** (NOT real-estate exclusively); **Rentista USD 1,500/mo** passive; PR after 3yr continuous; passport after 2yr PR — see `visa-programs.md`

### 🇪🇨 EC
- **Pension tax**: Worldwide for tax residents (>183 days); foreign pension at progressive 5-37%; potentially exempt under Art. 9 LRTI if double-tax treaty + source-country pension already taxed; verify with SRI
- **Healthcare**: IESS social security + private (Hospital Metropolitano, Hospital Vozandes — Quito; Hospital Monte Sinaí — Cuenca); Cuenca particularly strong for retiree healthcare per International Living indices — verify
- **Climate**: Quito ~2,850m / Cuenca ~2,560m altitude-moderated 10-22°C year-round; **Pacific Ring seismic (2016 Pedernales M7.8) + Cotopaxi volcano active 2024 + Galapagos rising sea-temp + tsunami coastal**; Guayaquil hotter coastal
- **Expat density**: **Cuenca top US/CA expat retiree hub globally** (International Living top-rank, verify); ~17.7M pop; Spanish + Kichwa/Shuar; English in Cuenca expat zone
- **Visa**: **Pensioner Visa USD 1,500/mo** / **Investor Visa USD 42,500** (~100×SBU 2026 SBU USD 470/mo); 2yr Temp → Perm after 21mo; naturalization 3yr PR; **2024 Internal Armed Conflict Declaration** — violent crime peaks Guayaquil/Esmeraldas/Manta; Quito/Cuenca relatively safer

### 🇵🇾 PY
- **Pension tax**: Territorial PIT — foreign-source pension NOT subject to PY IRP; flat 8/9/10% on PY-source only
- **Healthcare**: IPS (Instituto de Previsión Social) public; private (Sanatorio Migone, Adventista, Hospital Bautista — Asunción); PY healthcare lags PE/EC; medivac to BR/AR for complex cases
- **Climate**: Asunción humid subtropical 14-34°C; **Río Paraguay flooding catastrophic 2014-15/2018/2019/2024 + Cerrado/Chaco wildfires 2019-20/2024 + drought**; minimal seismic
- **Expat density**: Small but growing AR/BR/RU/EU retiree community; ~7.4M pop (Asunción Metro ~3M); Spanish + Guaraní co-official + Portuguese border + German Mennonite communities
- **Visa**: **Resolución SET 1186/2023 reformed PR** — formerly cheapest formal RBI (~USD 5,200) → now **USD 70k SUACE business invest** OR active SET RUC; citizenship 3yr continuous PR; **Itaipú/Yacyretá #2 net electricity exporter** (cheap energy attracts data centers)

### 🇦🇲 AM
- **Pension tax**: Worldwide for tax residents (>183 days); foreign pension at flat 21% PIT (2026 — verify SRC); diaspora-repatriation incentives via Law on Foreign Investment
- **Healthcare**: state Healthcare Universal Programme + private; CMC and Erebouni Medical Center flagship Yerevan hospitals; medivac to TR/RU/EU historically common
- **Climate**: Yerevan continental — -3 to +3°C winter, 28-35°C summer; **HIGH SEISMIC 1988 Spitak M6.8 baseline (~25,000 deaths) + Yerevan/Gyumri/Vanadzor microzoning**; **post-2020/2023 Karabakh war + ~120k displaced Sep 2023 + CSTO suspension Feb 2024**
- **Expat density**: Moderate diaspora-repatriation segment (US ~1M, RU ~2M, FR, AR, LB, IR diasporas); ~2.78M pop + ~7M global diaspora; **Russian-relocant wave 2022-24 (~50% peak Yerevan appreciation)**; Armenian + Russian + English in tech/tourism
- **Visa**: **Investor Residency AMD 50M (~USD 130k) deposit OR property → 5yr renewable**; **Citizenship by descent (Diaspora) Art. 13 streamlined** / naturalization 3yr PR + dual since 2007 — see `visa-programs.md`

### 🇦🇿 AZ
- **Pension tax**: Worldwide for tax residents (>182 days); foreign pension at progressive 14-25% (2026 — verify Min. Tax)
- **Healthcare**: AzMedSv (state) + private; mandatory CMI phased 2020-2024; expats use private (Memorial Bahcelievler, Bona Dea International Hospital, MediClub Hospital — Baku); medivac to TR
- **Climate**: Baku moderate-arid Caspian — 4-10°C winter, 27-33°C summer; **Caucasus + Caspian seismic (2000 Baku M6.8) + AzDTN 2.4-1 2010 code + Caspian sea-level falling 2010-24 ~1m + Absheron mud volcanoes (unique)**; **2020+2023 Karabakh + East Zangezur reintegration** (ANAMA de-mining cert + AZ-citizen-priority subsidized)
- **Expat density**: Small UK/TR/IR/RU expat retiree community; ~10.16M pop (Baku ~2.4M, Ganja ~330k, Sumgayit ~340k); Azerbaijani (Latin script since 2001) + Russian + English business + Turkish mutually intelligible; **very low crime; oil-revenue stabilized economy**
- **Visa**: **TRP via real estate ≥AZN 100k (~USD 60k) → 1yr renewable to 5+**; PR after 8yr continuous TRP; Strategic Investor Visa AZN 540k priority sectors; naturalization 5yr PR + Azeri language; **dual citizenship LIMITED exceptions**

### 🇹🇳 TN
- **Pension tax**: Worldwide for tax residents (>183 days); foreign pension at progressive 0-35% (2026 — verify Direction Générale des Impôts); 80% abatement on foreign pension transferred permanently to TN in TND under similar logic to MA Art. 76 CGI (verify Code IRPP Art. 36)
- **Healthcare**: CNAM public + private; **French-system standards**; expats use private (Clinique Hannibal, Clinique Taoufik, Clinique El Manar — Tunis); **medical-tourism destination** (cosmetic surgery, dental, IVF) for FR/IT/MT clientele
- **Climate**: Tunis Mediterranean coast 11-32°C; **2018 Cap Bon catastrophic floods + 2023-24 record drought (reservoirs <30%) + APAL coastal erosion**; **post-2021 constitutional revisions + 2024 elections**
- **Expat density**: Moderate FR/IT/DE/UK retiree community (FR cultural + linguistic ties strong); ~12.07M pop (Tunis Metro ~2.7M, Sfax ~1M, Sousse ~290k, Djerba ~165k); Arabic + French in business/property + Tamazight + Tunisian Arabic + English in tech/tourism
- **Visa**: **Investor Residence Permit ≥TND 1M (~USD 320k)**; citizenship 5yr continuous PR + Arabic + dual since 2014; **Tunisia Investor Visa drafted 2024 NOT gazetted** — verify; **IMF EFF program SUSPENDED Mar 2024**

## Tier-5 country profiles (added 2026-05-01)

### 🇮🇳 IN
- **Pension tax**: Worldwide for tax residents (>182 days); foreign pension at progressive 0-30% + surcharge + 4% cess (2026 — verify CBDT); LRS USD 250k/yr cap on outbound remittance; treaty relief under DTAA (US/UK/CA — verify Income Tax Act s.90); NRO/NRE bank-account split material
- **Healthcare**: PMJAY public for low-income citizens (~500M beneficiaries) + extensive private (Apollo, Fortis, Max, Manipal, Medanta — JCI-accredited Bangalore/Hyderabad/Mumbai/Delhi NCR); **medical-tourism destination** at fraction of Western costs; English universal in private hospitals
- **Climate**: Mumbai 18-33°C / Delhi NCR 7-43°C / Bengaluru 16-33°C altitude-moderated / Kerala 23-31°C; **Indian monsoon Jun-Sep critical (Mumbai/Kerala flooding); Delhi PM2.5 crisis Oct-Feb annual; Bengaluru water-scarcity 2024+ acute; Joshimath subsidence 2023**; Bengaluru/Pune/Goa most retiree-amenable
- **Expat density**: Small UK/RU/IL/AU/CA expat retiree community concentrated in Goa coastal + Pondicherry French-quarter; Bengaluru/Pune urban tech-overlap; ~1.428B pop; English in business + legal + healthcare; aging slower than China
- **Visa**: **NO golden-visa via real estate (UNIQUE absence)** — India does NOT offer property-pegged residency or citizenship; **OCI lifetime multi-entry for Indian-origin descendants** is the practical pathway; naturalization 11+yr (very strict); dual citizenship NOT allowed; verify with MHA / Bureau of Immigration

### 🇳🇬 NG
- **Pension tax**: Worldwide for tax residents (>183 days); foreign pension at progressive 7-24% + 2.5% NHF (2026 — verify NRS, formerly FIRS); minimal treaty network
- **Healthcare**: NHIA (replaces NHIS since 2022) limited rollout; **mandatory private health insurance for expats**; private (Reddington Hospital, Lagoon Hospital, LUTH, First Cardiology — Lagos VI/Ikoyi); medivac to ZA/UK/UAE common for serious cases
- **Climate**: Lagos 22-32°C tropical humid + flooding rainy season Apr-Oct / Abuja FCT 18-31°C savanna milder altitude / Kano 13-39°C Sahel hot-arid; **Lagos coastal flooding chronic + Atlantic surge events + Niger-delta climate stress + Sahel drought**
- **Expat density**: Small UK/IN/CN/LB diaspora retiree community concentrated in Lagos VI + Lekki gated communities + Abuja Maitama/Asokoro; ~218M pop (Lagos 22M largest African city); English official + Yoruba/Igbo/Hausa + Pidgin universal; **security risk requires private security + gated communities + energy autonomy mandatory**
- **Visa**: **NO golden-visa via real estate**; STR-1 Investor visa USD 100k business is the longer-term pathway; naturalization 15+yr + Nigerian language + dual NOT allowed for native-born; verify with NIS

### 🇰🇪 KE
- **Pension tax**: Worldwide for tax residents (>183 days OR ≥122 days/yr × 3 yrs); foreign pension at progressive 10-35% PIT (2026 — verify KRA)
- **Healthcare**: NHIF public + Social Health Insurance Fund (SHIF — phased 2024-25 reform); private flagship **Aga Khan University Hospital Nairobi + Karen Hospital + Nairobi Hospital + MP Shah Hospital**; medivac to ZA/UK for complex; English + Kiswahili official; **M-PESA universal in admin (unique to KE)**
- **Climate**: Nairobi altitude-moderated 11-26°C year-round (~1,795m) "City in the Sun"; Mombasa coastal 22-32°C tropical-humid; **Rift Valley seismic baseline + 2018+ locust crises + drought NE/Turkana**
- **Expat density**: Moderate UK/US/IT/DE/IN/diaspora retiree community concentrated in Karen British-cultural roots + Lavington/Westlands/Runda/Muthaiga/Kitisuru + Diani beach south of Mombasa; ~55M pop (Nairobi Metro 5M); SGR Mombasa-Nairobi-Naivasha-Kisumu drives corridor RE
- **Visa**: **NO golden-visa via real estate (UNIQUE absence in EAC)**; **Class A1 Investor USD 100k business** / **Class K Resident KES 200k+/yr passive** / PR 7yr / Citizenship 7yr + Swahili (dual allowed since 2010); verify with Department of Immigration Services

### 🇯🇴 JO
- **Pension tax**: Worldwide for tax residents (>183 days); foreign pension at progressive 5-30% + 1% national-contribution (2026 — verify ISTD)
- **Healthcare**: Royal Medical Services (RMS — military-affiliated; serves civilians via referral) + private (King Hussein Cancer Center, Specialty Hospital, Istishari, Al-Khalidi — Amman); **medical-tourism hub for GCC + Iraq + Syria refugee population**; English-medium private hospitals; Arabic + English in healthcare admin
- **Climate**: Amman semi-arid altitude-moderated (~750m) 4-32°C; Aqaba Red Sea 12-39°C / Dead Sea 14-39°C below sea level (-430m); **among most water-poor globally per FAO + Disi aquifer depletion + Dead Sea shrinking ~1m/yr**
- **Expat density**: Moderate Iraqi+Syrian+Palestinian diaspora + GCC retiree community + small UK/US/FR/AU/CA expat; ~11.4M pop (Amman Metro 4.5M); Arabic official + English business/tourism/medical + French educated diaspora; among most water-poor globally
- **Visa**: **CBI Jordan since 2018** (JOD 750k bond OR JOD 1M private investment OR JOD 250k SME with 20+ employees → Jordanian passport, ~50 visa-free destinations — WEAK passport for mobility plays, rational mainly for diaspora reconnection / GCC business utility); **Investor Residence ≥JOD 200k Greater Amman / JOD 100k outside (5yr renewable)**; Bona Fide Investor ≥JOD 50k bank deposit 1+yr; Aqaba ASEZ separate framework — see `visa-programs.md`

### 🇴🇲 OM
- **Pension tax**: NO PIT for individuals (Oman individual income-tax law drafted 2022 NOT enacted as of May 2026 — verify Tax Authority)
- **Healthcare**: MoH public network for Omani citizens + sponsored expats; **mandatory private health insurance for expats (Dhamani 2025 phased rollout per RD 89/2021)**; private (Royal Hospital Muscat, Sultan Qaboos University Hospital, Burjeel Muscat); medivac to UAE common
- **Climate**: Muscat 17-42°C; **Salalah unique Khareef monsoon Jun-Sep (Indian Ocean SW monsoon) — only verdant zone in Arabian Peninsula**; Nizwa interior 8-44°C; **CYCLONE EXPOSURE HIGH** — Gonu 2007/Phet 2010/Mekunu 2018/Shaheen 2021/Tej 2023 catastrophic Muscat coast (insurance underwriting baseline)
- **Expat density**: Small UK/US/IN/PK/SA/EG/JOR expat retiree community; ~5.0M pop (Muscat Metro 1.7M, ~38% expat); Arabic official + English business; Vision 2040; quieter than UAE — appeals to retirees seeking less commercial GCC
- **Visa**: **Investor Residency Royal Decree 89/2021** — 5-yr ≥OMR 250k (~USD 650k) ITC freehold / 10-yr ≥OMR 500k (~USD 1.3M) ITC; **Long-term Retiree ≥OMR 4,000/mo pension (~USD 10,400)**; NO citizenship-by-investment — see `visa-programs.md`

### 🇧🇭 BH
- **Pension tax**: NO PIT for individuals; foreign pension NOT subject to BH PIT
- **Healthcare**: SEHATI (mandatory contributory + supplemental) + MoH public + private (King Hamad University Hospital, American Mission Hospital, Bahrain Specialist Hospital, Al Salam Specialist Hospital); Saudi Causeway integration drives weekend medical-tourism flow
- **Climate**: 14-39°C; **summer 40°C+ + sandstorms + sea-level rise + 2008/2009 Manama flooding + groundwater depletion + Saudi Causeway integration**; humid coastal vs UAE/Qatar
- **Expat density**: Small UK/US/IN/PK/SA expat retiree community; ~1.49M pop (~52% Bahraini + 48% expat); Arabic official + English business + everyday widely; banking + financial services hub historically; quieter than UAE — appeals to mid-tier investors
- **Visa**: **Bahrain Property Visa Decree 6/2017 ≥BHD 200k (~USD 530k) → 10-yr renewable Self-Sponsored Residence Permit (incl. spouse + children)**; **Golden Residency Decree 16/2022** 10-yr renewable for property owners ≥BHD 200k OR investors / talented / retirees (BHD 4k/mo); NO CBI — see `visa-programs.md`

### 🇰🇼 KW
- **Pension tax**: NO PIT for individuals; foreign pension NOT subject to KW PIT — but **residency entirely via employment Iqama (Decree-Law 17/1959)**; citizenship effectively impossible (Decree-Law 15/1959)
- **Healthcare**: MoH public for Kuwaiti citizens + **mandatory private health insurance for expats (Afya health-card system 2016+)** + KD 50/yr healthcare-fee; private (Al Salam International Hospital, Hadi Clinic, New Mowasat, Dar Al Shifa); medivac to UAE/UK common
- **Climate**: 8-49°C among hottest inhabited capitals; **summer 50°C+ near-uninhabitable May-Sep + sandstorms (Toz / shamal) + 2018 Kuwait flooding + groundwater depletion + 2003 Kuwait fires legacy + oil-fired heat-island effect**; Arabian Gulf coastal humid
- **Expat density**: Small UK/US/IN/EG/PH/BD/SY/LB expat retiree pathway VERY constrained; ~4.85M pop (~30% Kuwaiti + 70% expat — largest IN/EG/BD/PH/SY); Arabic official + English business + tech + medical; **Bedoon stateless population pressing issue**; periodic political deadlock (parliament dissolved 2024)
- **Visa**: **NO golden-visa via real estate (UNIQUE absence in GCC)**; residency entirely via employment Iqama; 5+yr to PR claim rarely granted — see `visa-programs.md`

### 🇱🇧 LB
- **Pension tax**: Worldwide for tax residents (>183 days); foreign pension at progressive 4-25% PIT (2026 — verify MoF); **post-2019 banking-sector collapse + 2020 Beirut Port explosion + 2024 Israel-Hezbollah war Sep-Nov 2024** structural overlay
- **Healthcare**: **Healthcare collapse since 2019 financial crisis** — private clinics + hospitals operating with import-shortages + currency-collapse fee dual-pricing (USD ↔ LBP); historically excellent French-system standards (American University of Beirut Medical Center, Hôtel-Dieu de France, Clemenceau Medical Center, Saint George); medivac to CY/IT/FR for fresh-USD-paying patients
- **Climate**: Beirut Mediterranean 11-30°C / Mount Lebanon altitude-moderated cooler / Cedars ski-zone 1,800-3,000m **only Middle Eastern country with skiing**; **2024 Israel-Hezbollah war Sep-Nov 2024 + 2020 Beirut Port explosion legacy + Litani River + drought**
- **Expat density**: Large Lebanese diaspora retiree-returnee cohort (~13M global Mahjar diaspora — far larger than 5.5M domestic); ~5.5M pop (incl ~1.5M Syrian + ~470k Palestinian refugees) — Beirut Metro 2.4M; Arabic + French de facto + English in tech/business/healthcare + Armenian Bourj Hammoud; high COL Beirut for fresh-USD earners (locals collapsed wealth)
- **Visa**: NO golden-visa via real estate; **Investor Residency ≥USD 50k Lebanese business (1-yr renewable)**; property ownership ≥USD 200k can support residency application but not automatic; **Lebanese descent streamlined naturalization** widely used by global Mahjar diaspora; dual citizenship since 2007 — see `visa-programs.md`

## Anti-hallucination

- **Pension tax regimes change** — IT 7%, GR 7%, PT NHR all reformed in 2023-2024 cycle; **TH 2024 remittance reform** materially changes LTR economics; **CL 2023 Isapres ruling** reshaping retiree healthcare premiums; **MY MM2H** retiered multiple times since 2021. Always verify with home + host-country tax adviser.
- **Healthcare reciprocity rules change post-Brexit, post-2024 EU directives** — verify S1 eligibility before committing
- **Climate ranking is current-decade snapshot** — climate trajectory (`--climate`) is the forward-looking view; **water-scarcity overlays (CY, ZA, CL, MA)** worth checking against latest drought/aquifer data
- **Cost-of-living tier is broad-stroke** — actual costs vary 2-3× between provincial and capital within most countries; AE/IL/JP costs concentrate sharply in prime city centres
- **Currency-volatility risk** — TR, EG, AR, ZA, ID retirees should consider FX exposure on pension stream vs local-cost; cross-link `--currency` for hedging strategies
- **Visa thresholds drift** — every program above (LTR, MM2H, SRRV, Retirement Visa, Pensionado, Olim incentives) has been re-priced or restructured at least once 2021-2026; treat all numeric thresholds as *as-of date-stamp* and verify at issuing authority before applying

## Status

Last refreshed: 2026-05-01 (Tier-5 additions — 87 countries total; Tier-5 added: IN, NG, KE, JO, OM, BH, KW, LB).
**Confidence**: MEDIUM — high-level regimes and visa names are sourced from current law where named (e.g., IL Amendment 168, MA Art. 76 CGI, Ley 19.937 UY, FDL 47/2022 AE, DL 824 CL, KR PIT Act Art. 18-2, MD Law 200/2010, HK CIES Mar 2024, QA Law 21/2018, SA Vision 2030 Premium Residency, PY SET 1186/2023, EC SBU 2026 ~USD 470/mo); specific thresholds (e.g., AED 1M, ZAR 37,000/mo, COP 3× SMLMV, USD 80k/yr LTR, HK$30M CIES, ₩600M F-2, AD ~€600k, MC ~€500k, MD €250k, QAR 730k, SAR 800k, AMD 50M, AZN 100k, TND 1M, USD 1,500/mo EC Pensioner) should be re-verified at issuing authority before user action since visa thresholds drift on 12-24 month cadence.
