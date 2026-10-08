# Universal `--home-tax` Section

Buyer-nationality tax overlay for foreign property. Indexed by **buyer's tax-residence country** (not the property country). Covers 20+ buyer cohorts plus 10 cross-cutting structural traps. Companion to the property-country `--tax` layer (per-country playbook: taxe foncière / IBI / IMU / etc.) and `shared/finance.md` (mortgage availability for non-resident buyers).

**Snapshot**: 2026-05-09. Tax law moves fast — every numeric claim is statute / form / circular-cited and date-stamped. Where a parliamentary bill is mid-flight (NL Wet WRBox3 → 2028; FR PLF 2026 exit-tax extension; IT 2026 PLF 24-bis to €300k; KR 2028 Inheritance Acquisition System; US TCJA estate-exemption sunset/OBBBA permanence) the document flags MEDIUM confidence and points to the parliamentary tracker.

**Anti-hallucination**: every cluster ends with `Confidence: HIGH/MEDIUM/LOW` and a `Last verified` date. Every numeric claim either cites a primary statute / form / circular OR is labelled `est.` with computation shown. Forbidden phrasings per `shared/anti-hallucination.md` § Forbidden phrasings are avoided throughout.

**Disambiguation — `--home-tax` vs `--tax` vs `--finance` vs `--notary`**:
- `--home-tax` = **buyer-residence-side**. What the buyer's home tax authority does to them annually + at disposal + at death + at emigration because they own foreign property.
- `--tax` = **property-country-side**. Local property tax, transaction tax, future revaluations.
- `--finance` = mortgage availability for non-resident buyers in the property country.
- `--notary` = transaction-completion process (deed, days from offer to closing, closing costs).

Tax due in BOTH countries is the norm, with bilateral relief via DTT (credit method or exemption-with-progression). Both must be modelled.

## Universal contract

For the **buyer's tax-residence country**, return:

1. **Tax-residence trigger** — what makes a buyer a tax resident (days-test + domicile/centre-of-life test + treaty tie-breaker)
2. **Worldwide-income reach** — does the home country tax foreign rental? Form / schedule for reporting?
3. **Foreign-asset disclosure** — mandatory annual reporting (FBAR + Form 8938 / T1135 / Modelo 720 / Quadro RW / Schedule FA / Form 3916 / Anlage AUS / Form 5060 / Bens no Exterior + CBE)
4. **CGT on disposal** — rate, holding-period exemptions, treaty allocation (situs vs credit), principal-residence relief
5. **Annual wealth / property tax on overseas RE** — IFI (FR), Patrimonio + ITSGF (ES), Formueskatt (NO), Box 3 (NL), IVIE (IT), Vermögenssteuer (CH), Ejendomsværdiskat (DK)
6. **Estate / inheritance exposure** — worldwide for resident decedent/heir? Treaty network (US 16, UK ~10, DE 5, FR ~7, IT ~7, ES ~3)
7. **Departure / exit tax** — does emigration trigger a deemed disposition on foreign RE? (US/CA/AU/IL/ZA YES on direct foreign RE; DE/FR/JP/KR shareholdings only)
8. **2024-2026 reforms** — date-stamped reform calendar
9. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Home-Country Tax Overlay (buyer's residence: <ISO2>)

**Tax-residence trigger**: <days / domicile / centre-of-life test>
**Worldwide income**: <yes/no/territorial>
**Foreign rental reporting**: <form / schedule>
**Foreign-asset disclosure**: <form name + threshold + penalty>
**CGT on foreign disposal**: <rate, holding-period, principal-residence relief>
**Annual wealth/property on foreign RE**: <name / rate / threshold>
**Estate/inheritance worldwide**: <yes/no + treaty count>
**Exit tax on foreign RE**: <yes/no + statute>
**Special inbound regimes**: <Beckham / 24-bis / FIG / Olim / RNOR>
**Confidence**: <HIGH/MEDIUM/LOW>
**Last verified**: <YYYY-MM-DD>
**Sources**: <primary URLs>
```

## Cross-cutting traps to surface every time

These appear across multiple buyer cohorts and warrant a flag whenever a buyer is shopping abroad. Detailed mechanism + statutory anchors are in the **Cross-cutting structural detail** section near the end.

1. **Phantom currency-gain on foreign mortgage payoff** — most-missed item for US buyers (IRC § 988 ordinary gain on FX swing of mortgage principal — separate from the property's CGT computation). Anchor case ***Quijano v. United States*** rejects netting FX loss against property gain on personal-use mortgage. Australian Div 775 Forex Realisation Event 4 + Canadian ITA § 39(2) + Japanese § 57-3 produce similar exposure. **Integrated systems (UK Bentley v Pike; DE Anlage V-Ausland; FR CGI 150 U; IT TUIR Art. 67) avoid the bifurcation.**

2. **PFIC trap on foreign collective-investment vehicles (US-only)** — IRC § 1297. Spanish SOCIMI, French SCPI, German Offene Immobilienfonds, UK REIT, Australian LIT/MIT, Singapore/HK property funds → almost always PFIC for US individual holders. Three regimes (§ 1291 default punitive / § 1295 QEF requires PFIC Annual Information Statement / § 1296 mark-to-market only for marketable PFICs). Direct ownership avoids PFIC; pooled vehicles trigger it. Foreign-property-fund ETFs sold by Charles Schwab to US clients in their UK/AU/HK arms are still PFICs.

3. **Wealth tax on overseas property — multi-country footprint** — most DTTs do NOT cover wealth tax. **FR IFI** worldwide for FR resident > €1.3M; **ES Patrimonio + ITSGF** worldwide > €700k base + ITSGF > €3M; **NO Formueskatt** worldwide > NOK 1.7M; **CH Vermögenssteuer** cantonal worldwide; **NL Box 3** deemed-return on worldwide assets; **IT IVIE** 1.06% asset-class-specific on foreign RE only; **DK Ejendomsværdiskat** uniquely applies to foreign property at Danish rates. A French resident buying a Madrid pied-à-terre is in scope for BOTH IFI (worldwide) AND ES Patrimonio (Spanish-situs) — overlap not eliminated by DTT.

4. **Estate / inheritance-tax patchwork** — bilateral estate-tax treaties are RARE. US has 16 ([IRS estate & gift treaties](https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international)); UK ~10; DE 5 (DK · FR · CH · US · GR — SE 2007 / AT 2008 terminated); FR ~7; IT ~7; ES ~3; NL handful. Most foreign property held by a resident decedent gets DOUBLE-TAXED on death. State-level estate taxes (NY/MA/CT/IL/MN/OR/WA/RI/ME/VT/MD/HI/DC) layer on without treaty relief.

5. **Departure / exit-tax events** — **direct foreign real estate is in exit-tax scope in US (§ 877A) / CA (ITA § 128.1) / AU (CGT event I1) / IL (§ 100A) / ZA (§ 9H)** and **OUT of scope in DE (§ 6 AStG only on shareholdings ≥ 1%) / FR (Art. 167 bis only on shareholdings > €800k or > 50%) / JP (§ 60-2 securities > ¥100M) / KR (Art. 118-9 securities > ₩500M)**. Verify before structuring exit. Holding foreign rental via a German GmbH brings DE § 6 AStG into scope on emigration even though direct property would not.

6. **Special-inbound-regime lock-in** — IT 24-bis (€100k or €200k flat on foreign income, 15-year cap) / IT 24-ter (7% pensioners' Mezzogiorno, 9-year cap) / ES Beckham (24% flat 6 years) / UK FIG (4-year exemption post-non-dom abolition) / IL Olim (10-year foreign-income exemption + 2026 reporting reform) / NL 30%-ruling (→ 27% from 2027). Each has tight grandfathering windows and entry conditions; missing the window or breaking residency continuity loses the regime irrecoverably.

7. **Treaty FTC vs treaty exemption — DTT cascade** — real-property income is allocated to *situs* country under OECD MTC Art. 6 but BOTH countries can typically tax (Art. 24 Methods). **Exemption-with-progression** (DE / AT / FR / CH for most EU treaties) → foreign income free but pushes domestic into higher band. **Credit method** (US / UK / CA / AU / JP / IN) → fully taxable with foreign-tax credit capped at home tax on that income. Excess credit carries forward 10y in US; 1-year carryback / 10-year carryforward; lost immediately in AU and NZ (no carryforward). The German Anrechnungsmethode applied to ES rental (DE-ES DTT 2013) is a CREDIT regime — atypical for DE. Verify each treaty's Article 24 method case-by-case.

---

## Buyer cohort: United States — citizenship-based (IRC + IRS)

US tax residence is uniquely **citizenship-based** — a US citizen owes US tax on worldwide income regardless of where they live or whether they ever set foot in the US. Three triggers: US citizen (forever, until § 877A renunciation); lawful permanent resident under IRC § 7701(b)(1)(A)(i) until I-407 surrender or treaty tie-breaker; substantial presence test (≥ 31 d current + ≥ 183 weighted d over 3 y). Treaty tie-breaker (Form 8833) changes computation, NOT filing — FBAR + Form 8938 + Form 8621 + Form 3520 all still apply.

### Worldwide-income reach — IRC § 61, § 469, § 168(g)
- Schedule E for foreign rental income/expenses, **USD with annual averaging** (Rev. Rul. 89-78). § 988 functional-currency election available for QBU (rare for individuals).
- Net rental loss limitation under § 469 passive activity rules; suspended until passive income or disposition; active-participation $25k allowance phases out $100k–$150k AGI.
- Depreciation: IRC § 168(g)(1)(A) **mandates ADS for tangible property used predominantly outside the US**. Residential rental → **30-year ADS** post-TCJA (was 40, now 30 per § 168(g)(2)(C)(iii) effective post-2017). Bonus depreciation under § 168(k) **does not apply** to ADS property — OBBBA's restored 100% bonus is moot for foreign property.
- Mortgage interest § 163(h) deductible on foreign principal/second residence subject to $750k acquisition-debt cap (post-TCJA; $1M for pre-15-Dec-2017 debt).

### FATCA Form 8938 — IRC § 6038D
Filing thresholds (verified 2025 IRS instructions):

| Filer | EOY threshold | Anytime threshold |
|---|---|---|
| Single / MFS, US-based | $50,000 | $75,000 |
| MFJ, US-based | $100,000 | $150,000 |
| Single / MFS, abroad | $200,000 | $300,000 |
| MFJ, abroad | $400,000 | $600,000 |

Real estate **held DIRECTLY** is NOT a "specified foreign financial asset" — but **interest in a foreign corporation/partnership/trust holding the RE** IS. Common traps: French SCI, German GmbH, Spanish SL, UK Ltd, BVI/Cayman holding company. Foreign bank accounts opened to service the property (notary escrow, deposit account for utilities/HOA, currency-conversion account) ARE SFFAs. Penalties under IRC § 6038D(d) / § 6662(j): $10k initial + $10k per 30-day continuation up to $50k additional + 40% accuracy-related on understatement attributable to undisclosed asset.

### FBAR / FinCEN 114 — Title 31 § 5314 + 31 CFR § 1010.350
Filed with FinCEN (NOT Title 26). Aggregate > **$10,000** at any moment in calendar year on foreign financial accounts. **Signature authority counts.** Notary escrow, foreign mortgage offset account, deposit account for rental income, currency-broker account (Wise/Revolut multi-currency wallets reportable per FinCEN), utility-direct-debit account → all reportable. Real estate held directly is NOT reportable (not a financial account). Penalties (31 CFR 1010.821, 2025): non-willful up to $16,536 per violation; willful greater of $165,353 or 50% of account balance. **Bittner v. United States, 598 U.S. (28 Feb 2023)** — non-willful penalty **per FBAR form, not per account** (5–4 Gorsuch). [SCOTUS opinion](https://www.supremecourt.gov/opinions/22pdf/21-1195_h3ci.pdf).

### PFIC — IRC § 1297, § 1291/1295/1296, Form 8621
Foreign corp is PFIC if 75%+ gross passive income OR 50%+ assets produce passive income. Most pooled foreign property vehicles ARE PFICs:

| Vehicle | Country | PFIC status |
|---|---|---|
| SOCIMI | ES | YES — practitioner consensus |
| SCPI | FR | YES — practitioner consensus |
| Offene Immobilienfonds | DE | YES — practitioner consensus |
| REIT (UK / SG / HK) | various | YES for individual US holders |
| LIT / MIT (property trust) | AU | YES if elected corporate status |
| Direct title in own name | any | NO — not a corporation |

§ 1291 default = punitive (ordinary-rate tax + interest charge on excess distributions back to acquisition). § 1295 QEF requires PFIC Annual Information Statement (most foreign funds don't issue). § 1296 mark-to-market only for "marketable" PFICs (publicly listed).

### § 988 functional-currency phantom-gain — the Vinaigrette / Quijano trap
IRC § 988(a)(1) treats foreign-currency gain/loss on § 988 transactions as **ordinary income** (not capital). § 988(c)(1)(B)(iii) defines a debt instrument denominated in non-functional currency as a § 988 transaction. Functional currency for an individual = USD (§ 985(b)(1)(A)).

**Mechanism**: paying off a foreign-currency mortgage when USD has strengthened = ordinary § 988 gain on the FX swing of principal, taxed at marginal up to 37%. Separate from § 121 / capital-gain on the property itself. Refinancing (closing old, opening new) is a triggering event.

**§ 988(e) personal-transaction rule**: gain ≤ $200 per transaction excluded; if gain > $200, ALL of it is taxable (cliff). Gains taxable, losses non-deductible (§ 165(c) personal-loss limitation) — one-way asymmetry. Anchor case ***Quijano v. United States*** (US Tax Court — UK couple selling UK home; IRS denied integration of FX loss with property gain; § 988(d)(1) hedging-transaction argument rejected because mortgage wasn't trade-or-business). The "Vinaigrette" colloquial name lacks a citable opinion — use *Quijano* as authority.

### Sale of foreign principal residence — IRC § 121
$250k single / $500k MFJ exclusion applies **worldwide**. Ownership AND use as principal residence ≥ 2 of prior 5 years. § 988 mortgage gain is computed separately and is **NOT** excluded by § 121.

### Sale of foreign rental — § 1031 + § 1250 + § 1411
LTCG > 12 months at 0/15/20% federal + 3.8% NIIT. **§ 1031(h)(1) explicitly: foreign-to-US 1031 prohibited; foreign-to-foreign permitted.** § 1250 unrecaptured depreciation taxed at max 25% federal on gain attributable to ADS depreciation taken. NIIT 3.8% on net investment income > $200k single / $250k MFJ.

### Foreign Tax Credit — IRC § 901, § 904, Form 1116
Separate baskets under § 904(d): passive (rental), general, foreign branch, GILTI, treaty-resourced. Direct FTC usually preferred over § 911 FEIE (FEIE covers earned income only). § 904 cap: credit can't exceed US tax allocable to foreign-source income; excess: 1y carryback + 10y carryforward. Capital-gain rate-differential trap (§ 904(b)(2)(B)) — if foreign gain taxed at preferential US LTCG rate, FTC scaled down proportionally. HTKO ("high-tax kick-out") election kicks passive income taxed > 37% by foreign country into general basket.

### Federal estate tax + treaty patchwork
**OBBBA reform 4 Jul 2025** — TCJA doubled exemption made permanent at **$15M per individual** ($30M MFJ) effective 1 Jan 2026, indexed from 2025 base. TCJA-sunset-to-$7M scenario no longer operative. ([Arnold & Porter advisory](https://www.arnoldporter.com/en/perspectives/advisories/2025/07/increases-to-the-federal-estate-and-gift-tax-exemption-under-the-obbba)) Worldwide gross estate (IRC § 2031, § 2033). Top rate 40% on excess (§ 2001(c)).

**Estate-tax treaty list — 15 current treaty partners** ([IRS page](https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international)): AU · AT · CA (via Income Treaty Art XXIX B) · DK · FI · FR · DE · GR · IE · IT · JP · NL · ZA · CH · UK. (NO terminated 2015, SE terminated 2007 — both now dropped from the current IRS table; older lists may include them.) Without treaty: worldwide US estate + foreign-country situs = double-tax with limited § 2014 FTC mitigation. State-level estate/inheritance taxes (MA/OR/WA/RI/ME/VT/MN/IL/MD/HI/NY/DC + CT raised to fed level 2024; MD + NJ separate inheritance) layer without treaty relief.

### § 877A expatriation tax
Triggered by: renunciation (CLN issued); long-term green-card (8 of 15 years) abandonment under I-407 or treaty tie-breaker. Covered expatriate = net worth ≥ $2M OR 5-year average net income tax > $211k (2026 per Rev. Proc. 2025-32; $206k 2025) OR failure to certify 5-year compliance on Form 8854. Mark-to-market deemed sale of all property at FMV day before expatriation. § 877A(a)(3) exclusion: $890k (2025) / $910k (2026). Deferral election § 877A(b) with security + treaty filing.

### Foreign trust + foreign corporation
Foreign-grantor-trust IRC § 671-679. § 679 deems any US transferor to a foreign trust with US beneficiary the grantor (100% income attribution) for 5 years post-transfer. Form 3520 annual return for transactions with foreign trust + foreign gift > $100k/year individual or > $19,570 (2026) corp. Form 3520-A annual info return; trustee files; if won't, US owner files substitute by 15 Mar. **IRS Oct 2024 announcement** — automatic penalties on late 3520/3520-A no longer assessed for foreign-gift filings; reasonable-cause review standard. Form 5471 (≥10% US person ownership of foreign corp); Form 8865 (foreign partnership). GILTI § 951A — if foreign rental held in CFC, GILTI sweeps tested income annually; § 962 election allows individual taxation at corporate rate + FTC; § 954(b)(4) high-tax exclusion where foreign effective rate > 18.9%.

### State-level overlay
- **California** — § 17041 worldwide; FTB 1031 sticky domicile rules.
- **New York** — IT-201 worldwide; statutory residence test (183 d + permanent place of abode); NY estate tax $7.16M exemption 2025 with 105% cliff.
- **9 no-income-tax states** — FL, TX, WA, NV, SD, WY, AK, TN, NH (NH I&D sunsets 1 Jan 2027). Cleanest exposure for foreign-property-owning US persons.

### 2024-2026 reforms

| Date | Reform |
|---|---|
| 2025-07-04 | OBBBA — estate exemption permanent $15M (2026 base, indexed) |
| 2024-10 | IRS ends automatic penalties on late 3520/3520-A foreign-gift filings |
| 2024-05 | Treasury proposed regs on foreign-trust transactions (89 Fed Reg 39440) |
| 2023-02-28 | Bittner v. US — non-willful FBAR per form, not per account |
| 2024 (CT) | CT estate-tax exemption raised to federal level |
| 2027-01-01 | NH I&D sunsets |

**Confidence: HIGH** for cited statute + IRS guidance; **MEDIUM** for vehicle-specific PFIC classifications + § 988 personal-use treatment (no Treasury reg or Tax Court case carving out personal-residence mortgage from § 988 — practitioner consensus only).
**Last verified**: 2026-05-09.

---

## Buyer cohort: United Kingdom — FA 2025 FIG + LTR (post-non-dom abolition)

The UK is mid-2026 transition through the BIGGEST overhaul of overseas-asset taxation in 40+ years: **non-dom regime abolished 6 Apr 2025**; replaced by 4-year FIG regime; **IHT shifted from domicile-based to residence-based 6 Apr 2025**. Non-doms previously claiming remittance basis are now potentially exposed to UK tax on global rental from 6 Apr 2025.

### UK Statutory Residence Test (SRT) — Sch 45 FA 2013
Apply in sequence; first decisive answer wins:

1. **Automatic overseas tests** (Sch 45 §§ 12-16): < 16 d if resident in any of 3 prior years; < 46 d if not resident in any of 3 prior; full-time work overseas (≥ 35 hrs/wk avg) AND < 91 UK days AND < 31 UK workdays.
2. **Automatic UK tests** (§§ 6-9): ≥ 183 d in tax year; only home in UK for ≥ 91 d (used ≥ 30); full-time work in UK over 365-day period.
3. **Sufficient ties test** (§§ 17-20): 4 ties for leavers (family, accommodation, work, 90-day prior, country tie); 4 for arrivers (no country tie). Day-count vs ties matrix in RDR3 § 3.4-3.5.
4. **Split-year treatment** (Pt 3 §§ 43-55): 8 cases (1-3 leavers, 4-8 arrivers).

Case-law trap: ***A Taxpayer v HMRC* [2025] EWCA Civ 106** — Court of Appeal restored FTT's exceptional-circumstances exclusion (Sch 45 § 22(4)) for sister's grave illness. Burden of proof is day-by-day on the taxpayer.

### FIG regime — FA 2025 Sch 9 (effective 6 Apr 2025)
Domicile is **gone** for income tax + CGT. Replaced by:
- **4-year FIG** for "qualifying new residents": UK resident after ≥ 10 consecutive non-UK-resident tax years → first 4 years' foreign income & gains exempt UK tax. Claim by 31 Jan in Y+2 via SA return.
- Cost: lose Personal Allowance and CGT Annual Exempt Amount that year.
- After year 4: full UK tax on global income + CGT — no residual remittance shelter.
- **Temporary Repatriation Facility (TRF)** transitional — 12% (yrs 1-2) / 15% (yr 3) flat charge to remit pre-2025 unremitted income/gains.

[RFIG41000 introduction](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig41000) · [GOV.UK FIG regime claim guide](https://www.gov.uk/guidance/check-if-you-can-claim-the-4-year-foreign-income-and-gains-regime). HMRC manual still being populated; consultation responses still emerging.

### Foreign rental — overseas property business
ITTOIA 2005 §§ 264-265 (overseas property business chargeable only if carried on by UK resident). Computed using UK-property-business rules; profits **pooled separately** — overseas losses cannot offset UK pool, only future overseas profits. Reported on **SA106 Foreign Pages**, in £-sterling.

**Mortgage/finance-cost restriction** ITTOIA 2005 §§ 272A-B (FA No. 2 2015 § 24, fully phased in 6 Apr 2020): no deduction from rental for residential finance costs; replaced by 20% basic-rate tax reducer capped at lower of finance costs / property profits / total income above PA. **Applies equally to UK and overseas property** (§ 272A(7)).

**FTCR** under ITA 2007 §§ 793-806 / TIOPA 2010 Pt 2: credit foreign tax paid against UK income tax on same income, capped at UK tax payable. Excess foreign tax is unclaimable. Helpsheet HS263.

**FHL abolished 6 Apr 2025** (FA 2024-25): Furnished Holiday Letting regime for UK *and* EEA properties gone — full mortgage-interest deduction, capital allowances on new spend, BADR on disposal, pension-relevant earnings status all removed. Transitional (HMRC Nov 2024 guidance): existing capital allowances pool continues WDA; carried-forward FHL losses transferable to ordinary UK or overseas property pool; BADR claimable on cessation up to 3 yrs before 6 Apr 2025; anti-forestalling for unconditional contracts 6 Mar 2024 - 5 Apr 2025.

### CGT on foreign property disposal — TCGA 1992 § 1
Residential, individuals, post-30 Oct 2024 Budget cut: basic rate 18%, **higher/additional 24%** (cut from 28%). Annual exempt amount £3,000 (2025-26) — slashed from £12,300 (2022-23). PPR relief § 222-223; § 222(5) nomination required where > 1 residence (**2 years** from new combination — Griffin v Craig-Harvey); § 223 final-period relief 9 months. § 222B/§ 222C overseas residence eligible only if not a "non-qualifying tax year". § 222(5A) saves late nominations only where taxpayer didn't realise they had two PPRs.

### Forex in CGT — Bentley v Pike controlling
***Bentley v Pike*** [1981] STC 360 (53 TC 590) — **sterling is the only permissible unit of account**; foreign-currency cost translated at acquisition-date rate, proceeds at disposal-date rate. No US § 988-style bifurcation; currency movement is part of chargeable gain. HMRC manual [CG78310 foreign currency](https://www.gov.uk/hmrc-internal-manuals/capital-gains-manual/cg78310). Foreign mortgage repayment: any £ "saving" on weak-£ acquisition followed by strong-£ disposal increases the £ gain even if foreign-currency P&L is flat. Operational consequence: refinance during weak £ period locks in higher base cost (helpful); dispose during strong £ period accelerates gain (painful).

### IHT — residence-based from 6 Apr 2025
**Pre-6 Apr 2025**: domicile-based — UK-doms taxed worldwide; non-doms taxed UK-situs only. Deemed-dom 15/20.

**Post-6 Apr 2025 — Long-Term Resident (LTR) test** — IHTA 1984 § 6A ff. (FA 2025 Sch 13):
- Trigger: UK resident **≥ 10 of prior 20 tax years** ending year before chargeable event → worldwide IHT.
- Tail on leaving: 3 years (10-13 yrs LTR) increasing 1 year per additional year of residence, **capped at 10 years** (20+ yrs UK residence → 10-yr tail).
- Reset: 10 consecutive non-UK-resident years break LTR.
- Transitional (IHTM47021): individuals non-resident 2025-26 AND not UK-domiciled 30 Oct 2024 stay on old domicile test for pre-6-Apr-2025 events.

Rates: 40% over £325k nil-rate band; £175k residence nil-rate band (qualifying residential interest to direct descendants; tapered for estates > £2M). Both bands frozen until at least 5 Apr 2030 (Autumn 2024 Budget).

**IHT treaties** (~10 partners): FR (1963 Estate Duty Convention), IT (1968), NL, IE (1978), IN, PK, ZA, CH, SE, US. **Pre-1975 treaties (FR, IT, IN, PK)** lack deemed-domicile articles → may **override** the new LTR rule for treaty residents. Outside treaty: unilateral relief IHTA 1984 § 159 credits foreign death tax against UK IHT on same asset.

[IHTM47020 long-term UK residence](https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm47020) · [IHTM47021 transitional](https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm47021).

### Reporting cadence

| Obligation | Form | Deadline |
|---|---|---|
| Foreign rental | SA100 + SA106 | 31 Jan following year-end |
| CGT on **UK** residential | UK Property CGT return + payment | **60 days** of completion |
| CGT on **overseas** residential | SA108 with annual return | 31 Jan following year-end |
| FIG regime claim | SA return | 31 Jan in Y+2 |
| Voluntary catch-up | Worldwide Disclosure Facility | 90 days post-DRN |

Important: 60-day reporting applies to **UK residential disposals only**. Foreign residential disposals by UK residents go on the next SA return. ([ATT guide](https://www.att.org.uk/cgt-uk-property-reporting-service-users-guide))

No US-style FBAR / 8938 / 720 equivalent — but **CRS** delivers HMRC automatic data from 100+ jurisdictions; from Jan 2024 Airbnb / Booking.com submitted UK host data via DAC7-equivalent rules. HMRC nudge-letter campaigns 2017-onward (foreign income, offshore structures, from 2024 specifically overseas-property rentals).

### 2024-2026 reform calendar

| Date | Reform |
|---|---|
| 6 Apr 2024 | CGT AEA cut £6k → £3k |
| 30 Oct 2024 (Budget) | Residential CGT higher rate 28% → 24%; non-resi 10/20% → 18/24% |
| 6 Apr 2025 | Non-dom abolished; FIG 4-y regime live |
| 6 Apr 2025 | IHT residence-based (LTR test) |
| 6 Apr 2025 | FHL abolished UK + EEA |
| 6 Apr 2025 | TRF opens 3-yr window |

**Confidence: HIGH** for statute / black-letter law; **MEDIUM** for FA 2025 transitional rules where HMRC manual content is still being populated.
**Last verified**: 2026-05-09.

---

## Buyer cohort: Canada — CRA + Income Tax Act (RSC 1985 c.1 5th Supp.)

### Tax residence
Common-law factual + ITA § 250(1)(a) deemed (sojourn ≥ 183 d). Folio S5-F1-C1 governs residential-ties test: primary (dwelling, spouse, dependants) + secondary (DL, healthcare, club, professional, banking). Treaty tie-breaker (OECD Art. 4) overrides domestic deeming.

### Foreign rental — Form T776, BoC FX
Income/expenses converted to CAD using **BoC daily rates** (or annual average for high-volume — T1 General Guide). **CCA optional + restricted by Reg § 1100(11)**: cannot create or increase a rental loss — only reduce net to nil. Rule applies identically to foreign and Canadian rentals. **FTC** under ITA § 126(1) → Form **T2209**; per-country and capped at Canadian tax on that source.

### T1135 Foreign Income Verification Statement
Mandatory if total cost amount of specified foreign property > **CAD 100,000** at any time in year (ITA § 233.3). **Personal-use real estate is excluded** — vacation home > 50% personal NOT specified property. **Rented foreign property IS specified property** even below CAD 100k individually (counts toward threshold). Mixed-use AirBnB grey zone — CRA's "primarily" (> 50%) test fact-specific. Simplified Method (Part A) CAD 100k–250k; Detailed Method (Part B) > CAD 250k. Penalty: $25/day max $2,500/yr (§ 162(7)); $500/mo or $1,000/mo gross-negligence (§ 162(10)); $12,000/$24,000 false-statement caps; 3-yr extended reassessment (§ 152(4)(b.2)). VDP IC00-1R6 for catch-up.

### Disposal — 50% inclusion (66.67% proposal cancelled)
50% inclusion **remains in force**. Budget-2024 proposal to raise to 66.67% on individual gains > CAD 250k (effective 25 Jun 2024) was **deferred 31 Jan 2025 to 1 Jan 2026 then formally cancelled by PM Carney 21 Mar 2025** (Liberals). All gains continue under 50% rate.

**Principal Residence Exemption** § 40(2)(b) + § 54 — overseas property eligible if qualifies as PR for the year (CRA Folio S1-F3-C2 ¶ 2.11–2.13: ordinarily inhabited rule liberal — even short annual occupation can satisfy). One-PR-per-family-unit-per-year (§ 54(c.1)) post-1981 — choose strategically year-by-year. T2091(IND) designation form mandatory for all PR dispositions for 2016+ tax years (CRA news release 03 Oct 2016). 2017 amendment: trusts can no longer designate PR unless tightly defined.

### Departure tax — § 128.1(4) deemed disposition, foreign RE INCLUDED
On ceasing CA residence, all property deemed disposed at FMV — except § 128.1(4)(b)(i)–(iv) carve-outs: Canadian RE, Canadian resource property, Canadian business property of PE, RPP/RRSP/TFSA, employee stock options. **Foreign RE NOT carved out — fully exposed.** Form T1243 computes gain; T1244 elects deferral under § 220(4.5). Security required if federal tax owing > CAD 16,500 (CAD 13,777.50 for ex-Quebec). Practitioner trap: CA-RE excluded from departure tax but post-emigration disposal triggers § 116 25% non-resident withholding; foreign RE does the opposite — taxed on the way out.

### Estate — no estate tax, but § 70(5) deemed disposition
On death, § 70(5) deems disposition at FMV → terminal CGT (50% inclusion). Spousal/CLP rollover § 70(6). Probate fees provincial: ON 1.5%, BC 1.4%, AB flat, QC notarial wills exempt.

### 2024-2026 reforms
- 23 Jun 2024: CGT inclusion-rate hike 66.67% **CANCELLED 21 Mar 2025**.
- UHT: Bill C-15 (tabled 18 Nov 2025) proposes elimination 2025+. Most CA-resident individuals "excluded owners" since 2023.
- Bare-trust reporting (§ 150(1.1)) — pulled in 31 Dec 2023 via Bill C-32; CRA suspended for 2023, re-introduced for 2024 with carve-outs.

**Confidence: HIGH** (current law); **MEDIUM** on UHT elimination Royal Assent timing.
**Last verified**: 2026-05-09.

---

## Buyer cohort: Australia — ATO + ITAA 1936/1997

### Tax residence — 4 tests under ITAA 1936 § 6(1)
Resides test (common-law, primary), Domicile test, 183-day test, Cwlth super-fund test. ATO ruling **TR 2023/1** (finalised Jun 2023) replaces TR 98/17. **2021 Budget proposed bright-line 183-day primary + factor secondary** — Treasury consultation closed Sep 2023; **as of May 2026 NOT enacted**, no draft bill, increasingly treated as shelved.

### Worldwide income — § 6-5(2) ITAA 1997
FX translation Subdiv 960-C ITAA 1997 + functional-currency § 960-50: rental items translated at daily rate or yearly average (PCG 2017/4).

### Foreign rental — negative gearing into AU income
**Foreign-loss quarantining REPEALED 1 Jul 2008** (Tax Laws Amendment (2007 Measures No. 4) Act 2007 Sch 1). Foreign rental losses can offset Australian salary, business, investment income — same negative-gearing as domestic. Deductible: interest, Div 40 depreciation (§ 40-27 prohibits depreciation on second-hand depreciating assets in residential rental post-9 May 2017 Budget — applies to foreign too), capital works Div 43 (2.5% × 40 yrs). **FITO** Div 770 — capped at AU tax on that income; AUD 1,000 de minimis; **no carry-forward**.

### CGT — Div 855 ITAA 1997
Australian residents subject to CGT on worldwide assets. CGT event A1 (§ 104-10) on disposal. **50% individual discount** § 115-25 for assets held > 12 months. Cost base in AUD (§ 960-50 daily-rate at incurrence). **Main Residence Exemption** § 118-110 extends to overseas dwelling — BUT **MRE for foreign residents REMOVED post-30 Jun 2020** (Treasury Laws Amendment (Reducing Pressure on Housing Affordability) Act 2019, RA 12 Dec 2019). Life-events test exception: foreign residency ≤ 6 continuous years AND qualifying life event.

**FRCGW** — threshold removed and rate raised to **15% from 1 Jan 2025** (TLA Bill, RA 10 Dec 2024). Applies to Australian RE only when expat sells. Threshold was AUD 750k @ 12.5% pre-change. Important ordering trap: this affects Aussies returning to sell their AU home while non-resident, NOT foreign-property sales by AU residents.

### CFC / FIF — Part X ITAA 1936
Direct ownership of foreign residential RE NOT a CFC interest. CFC attribution where AU resident has ≥ 10% interest in foreign company with ≥ 40% control. Property-holding foreign companies (FR SCI, ES SL) **can** trigger CFC if AU owner controls. French SCI is transparent under FR domestic law but ATO will treat as company unless partnership election applies — verify with private ruling.

### Disclosure
No T1135-equivalent. Foreign income at **Item 20 (Supplementary)** — labels for foreign rental, foreign pensions, FITO, controlled-entity attributable income. CRS active 2017+. ATO 2024-25 Budget AUD 187m additional for Tax Avoidance Taskforce.

### Estate — no death duties; CGT event K3
Estate/inheritance taxes abolished 1979. § 104-215 CGT event K3 deems disposal at FMV when asset passes to foreign-resident or tax-exempt beneficiary. Passing to AU-resident beneficiary uses § 128-15 rollover. Deceased's main residence has 2-yr post-death sale window.

### 2024-2026 reforms
- 1 Jan 2025: FRCGW 12.5% → 15%, threshold AUD 750k → 0 (AU RE only).
- 1 Jul 2024: Stage 3 personal-tax cuts.
- 2024-25 Budget: ATO Tax Avoidance Taskforce funding increased.
- 2021 residency reform: NOT enacted.

**Confidence: HIGH** (current law; reform stalled).
**Last verified**: 2026-05-09.

---

## Buyer cohort: New Zealand — IRD + Income Tax Act 2007

### Tax residence — § YD 1
Permanent place of abode (PPOA) test primary, fact-based, ties-driven. 183-day backstop in any 12-mo period (§ YD 1(3)). **Transitional resident relief § HR 8** — new arrivers (incl. returning Kiwis after ≥ 10 yr non-resident) get a 4-year exemption on most foreign passive income (incl. foreign rental); does NOT cover NZ-source or employment income.

### Foreign rental — IR3R, ring-fenced losses
Reported on **IR3R schedule** + IR3 individual return. NZD conversion at IRD-published mid-month rates. **Ring-fenced rental losses § EL 4-EL 12** (Taxation (Annual Rates 2019-20, GST and Information Sharing) Act 2019, RA 26 Jun 2019, retrospective 2019/20): **applies to overseas residential rentals**. Losses cannot offset salary/wages/business income — carry forward against future residential property income only. **Interest deductibility for residential rentals fully restored 1 Apr 2025** (100%; phased: 80% 2024-25, 100% 2025-26). FTC § LJ 1 capped at NZ tax; per-country segregation; excess generally lost (no carry-forward).

### FIF — § EX 28 ff. — the surprise on foreign property holding entities
**Direct ownership of foreign RE is NOT a FIF interest** (§ EX 31, § EX 35 — interest in foreign company is FIF; bare RE is not). **BUT**: ownership through foreign company / unit trust / superannuation / LP-treated-as-company **IS** a FIF. French SCIs, Spanish SLs, US LLCs, German GmbHs holding the property → FIF.

**NZD 50,000 threshold (§ CQ 5(1)(d))** — total cost of all FIF interests (individuals only — NOT trusts or companies). Below: exempt from FIF, only actual dividends/distributions taxable. Above: FIF income computed under FDR (Fair Dividend Rate) 5% deemed annually × opening market value, Cost Method, Comparative Value, Attributable FIF, or Branch Equivalent. FDR most common.

Trap: NZ owner of FR SCI / ES SL holding a single property thinks "just a holding entity, ignore it" — actually FIF, deemed 5% income annually regardless of cash flow, plus rental income separately. Many foreign legal forms force entity ownership for civil-law reasons (succession, asset protection) — NZ tax tail can wag the structuring dog.

### Bright-line property test — § CB 6A — ALSO APPLIES TO OVERSEAS PROPERTY
Residential land, NZ or overseas (for NZ tax residents): **2-year bright-line** for disposals on/after 1 Jul 2024 (Restoring Tax Deductibility for Residential Investment Property Bill, RA Jun 2024). Pre-1 Jul 2024 follow 5-/10-year tests under prior National-Labour see-saw. **The bright-line test also applies to NZ tax residents who buy and sell overseas residential property** (2026 data, source IRD `https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test`). Outside the bright-line period, foreign-property disposal gains are taxed only under intent-of-resale § CB 6, business of dealing § CB 7, or business of erecting buildings § CB 12. NZ has **no general CGT** — regime is intent-based plus bright-line proxy.

### Estate — no inheritance/estate tax
Estate Duty abolished 1992; Gift Duty abolished 1 Oct 2011. No deemed disposition on death. Foreign-jurisdiction estate tax may bite (FR 60% non-spouse non-direct, ES regional, etc.) — tax-treaty estate articles relevant.

### 2024-2026 reforms
- 1 Jul 2024: bright-line back to 2 years (NZ and overseas residential land held by NZ tax residents).
- 1 Apr 2024: tax-bracket adjustments (10.5% to NZD 15,600; 17.5% to 53,500; 30% to 78,100; 33% to 180,000; 39% above) — first since 2010.
- 1 Apr 2025: residential interest deductibility 100% restored.
- Foreign-buyer ban (Overseas Investment Amendment Act 2018) still in force (NZ-purchase by non-residents prohibited; not relevant for NZ buyer abroad).

**Confidence: HIGH**.
**Last verified**: 2026-05-09.

---

## Buyer cohort: Germany — EStG · AStG · ErbStG · AO

### Tax residence — § 8 / § 9 AO + § 1 EStG
Wohnsitz (§ 8 AO — dwelling kept for use) OR gewöhnlicher Aufenthalt (§ 9 AO — > 6 months presence) → **unbeschränkt steuerpflichtig** with worldwide income (§ 1 EStG). DTT tie-breaker (centre of vital interests, then habitual abode, nationality) governs dual-residence cases. (gesetze-im-internet.de/ao, /estg)

### Foreign rental — §§ 21 + 34d EStG (Anlage V + Anlage AUS)
- **EU/EEA property (FR/IT/PT/AT/NL/BE/etc.)**: most DTTs apply **Freistellung mit Progressionsvorbehalt** (treaty-exempt, but progression effect on bracket via § 32b EStG) — declared in Anlage AUS for progression only.
- **Spain — exception**: DE-ES DTT (in force since 2013) uses the **Anrechnungsmethode** (credit) for rental income; report in Anlage V + Anlage AUS, deduct Spanish IRPF up to German cap.
- **Non-EU/EEA**: § 2a Abs. 1 Nr. 6 EStG — foreign rental losses only offset same-country same-source positive income (Drittstaaten-Verlustabzugsbeschränkung); no § 10d carry-back.
- **AfA**: § 7 (4) — 2% straight-line; 3% for buildings completed post-2023 (Wachstumschancengesetz). § 7 (5a) — degressive 5% over 6 years for residential buildings with construction start 1 Oct 2023 – 30 Sep 2029 (rate cut from originally proposed 6% during Vermittlungsausschuss; signed Mar 2024).

### Disposal — § 23 EStG
- **Spekulationsfrist 10 years** for real estate (held privately, including foreign): outside → tax-free; within → ordinary marginal rate.
- BFH confirmed: Germany retains taxation right on gain by an unbeschränkt resident regardless of property situs, subject to DTT. Most DTTs (FR/IT/ES/AT/NL) allocate to situs country with **Freistellung** + progression in Germany.
- Trap: if property was rented during ownership, full 10y window applies. Self-use 3y prior to sale (last year + two preceding) restores § 23 exemption.

### Wegzugsbesteuerung — § 6 AStG
- Direct foreign real estate **NOT in scope** — only > 1% shareholdings in corporations.
- **Reform 1 Jan 2022 (ATAD-Umsetzungsgesetz)**: unlimited interest-free EU/EEA deferral abolished; replaced by 7-year installment plan (interest-free, but security required); residence-pre-departure threshold cut from 10 → 7 years.
- **17 Aug 2023** retroactive tightening of permanent-deferral conditions for pre-2022 emigrants.
- Trap: holding foreign rental via a German GmbH that holds the foreign real estate → emigration of the > 1% shareholder triggers § 6 AStG.

### Inheritance — ErbStG
- Worldwide if decedent OR heir is German-resident (§ 2 (1) Nr. 1 ErbStG).
- **§ 21 ErbStG**: foreign IHT credit, capped at German IHT on the same foreign asset.
- DTT estate-tax network (only **5** in force): **DK · FR · CH · US · GR** (the SE treaty was terminated 2007; the AT treaty was terminated effective 2008) — without DTT only § 21 unilateral credit.
- Allowances: spouse €500k · child €400k · grandchild €200k · sibling/unrelated €20k. Rates 7-50% by class.

### Wealth tax — abolished
Vermögensteuer suspended since 1997 (BVerfG 22 Jun 1995 ruling on unequal valuation). No annual return.

### Reporting — § 138 AO
- Acquisition of foreign **business** / permanent establishment / participation ≥ 10% (or > €150k cumulative cost in foreign corporation) → notifiable to BZSt + local FA via official interface, with the next income-tax return (latest 14 months after period-end). Penalty up to **€25k** (§ 379 AO).
- **Direct foreign rental real estate is NOT § 138 AO reportable** — but rental income must be in the annual return (Anlage V + Anlage AUS).
- No Italian-style Quadro RW or Spanish Modelo 720 equivalent.

### 2024-2026 reforms
- Wachstumschancengesetz Mar 2024: § 7 (5a) degressive AfA 5% × 6y for residential, plus § 7 (4) bump 2 → 3% for post-2022 completions.
- Mindestbesteuerungsrichtlinie-Umsetzungsgesetz (Pillar Two) 1 Jan 2024 — MNE > €750M only; not retail buyers.
- § 6 AStG amendments still bedding down post-ECJ scrutiny (C-355/22 line of cases).

**Confidence: HIGH** · **Last verified**: 2026-05-09

---

## Buyer cohort: France — CGI · DGFiP

### Tax residence — Art. 4 B CGI
Resident if ANY of: foyer / lieu de séjour principal in France · main professional activity · centre des intérêts économiques. Treaty tie-breaker overlays. (legifrance.gouv.fr)

### Foreign rental — formulaires 2047 + 2042 (+ 2044 unfurnished, + 2042-C-PRO furnished)
- **Unfurnished foreign rental** → revenus fonciers (form 2044) + 2047 + 2042.
- **Furnished foreign rental** → BIC under LMNP / LMP (form 2042-C-PRO + 2031).
- Most EU DTTs: **exonération avec taux effectif** (foreign rental exempt in France but counted to set the marginal rate on French-source income — exact French analogue of the German Progressionsvorbehalt).
- DTT credit method applies for some non-EU treaties (US, etc.).

### CGT on disposal — Art. 244 bis A + 150 U CGI
- Plus-values immobilières: abatement schedule that yields full IR exemption at **22 years** of holding and full social-charges exemption at **30 years**.
  - Income tax: 6%/y from year 6-21, then 4% in year 22 → 0% IR.
  - Prélèvements sociaux: 1.65%/y from year 6-21, 1.6% in year 22, 9%/y from year 23-30.
- Most EU DTTs (DE/IT/ES/etc.) allocate situs taxation to property country; France typically applies the credit method or treaty-exempts. France retains taxation right where DTT says "may be taxed" — verify per treaty.

### IFI — Impôt sur la Fortune Immobilière (Art. 964-973 CGI)
- Worldwide real estate at FMV; resident threshold **€1.3M net taxable** (tax computed from €800k); rates 0.5% → 1.5% in 6 brackets.
- **Résidence principale 30% abatement** (Art. 973 I CGI) — only owner-occupied direct ownership, not via SCI. One property only per foyer fiscal.
- Mortgage/acquisition debt deductible against the property; LF 2024 (Art. 973 IV CGI) tightened deductibility of holding-company debt — shareholder current-account advances only deductible if used to acquire/build/refinance taxable real estate.
- DTT estate/wealth treaties limit IFI relief — only ~3 still cover wealth.

### Exit tax — Art. 167 bis CGI
- Triggered on unrealised gains on shareholdings > €800k OR > 50% in companies, on losing French residence.
- **Direct real estate NOT in scope**.
- Current regime (post-2019 reform): tax extinguishes at year 2 (small holdings) or year 5 (≥ €2.57M); much narrower than pre-2018 15-year version.
- **PLF 2026 (under parliamentary navette as of Nov 2025)**: National Assembly amendment to **restore 15-year holding period** — verify final adoption before relying on the current short window.

### Inheritance — Art. 750 ter CGI
- Worldwide for French-resident decedent OR French-resident heir (post-1998: 6+ years out of 10 prior).
- Spouse and PACS partners: **exonérés** (Loi TEPA 22 Aug 2007). Children: €100k allowance, then 5-45%. Siblings: €15,932 + 35-45%. Unrelated: €1,594 + 60% flat.
- Foreign IHT credit: Art. 784 A CGI (limited to French IHT on same foreign asset).

### Reporting
- **Form 3916 / 3916-bis**: declaration of every foreign account / brokerage / crypto-platform / life-insurance contract held by a French resident. **€1,500 penalty per undeclared account/year**, raised to **€10,000** if account is in a non-cooperative state. Statute of limitations 10y when undeclared (vs. 3y normally).
- **Form 2074-IMM** for foreign property capital gain.
- **§ 1649 AA CGI**: foreign life-insurance contract disclosure.

### 2024-2026 reforms
- LF 2024 (Dec 2023): IFI valuation tightening — shareholder current-account debt restrictions (Art. 973 IV CGI).
- Pillar Two transposition 1 Jan 2024.
- 30 Jul 2024 — DGFiP BOFIP refresh on overseas property gain computation (BOI-RFPI-PVI / PVINR).
- PLF 2026: proposed exit-tax extension to 15y (Assembly 1st-reading); proposed 2% tax on holding-company financial assets — all unenacted as of date stamp.

**Confidence: HIGH** (except exit-tax PLF 2026 = MEDIUM, in flux) · **Last verified**: 2026-05-09

---

## Buyer cohort: Italy — TUIR · DL 201/2011 · D.Lgs. 209/2023

### Tax residence — Art. 2 TUIR (DPR 917/86)
- **Reformed 1 Jan 2024 (D.Lgs. 209/2023)**: resident if for > 183 days (more than half the tax year) ANY of:
  1. **Residenza** (civil-code sense — habitual abode) in Italy;
  2. **Domicilio** — redefined to "place where personal and family relations mainly develop" (broke from prior centre-of-economic-interests definition);
  3. **Physical presence** in Italy;
  4. Iscrizione anagrafe — now a **rebuttable presumption** (was conclusive pre-2024).
- Operational guidance: AdE Circolare n. 20/E del 4 novembre 2024.

### Foreign rental — Quadro RL Modello Redditi PF
- DTT credit or exemption depending on treaty.
- **Cedolare secca (21% flat) does NOT apply** to foreign rental — must be ordinary IRPEF (taxed at marginal rate up to 43%).

### IVIE — Foreign Real Estate Tax (DL 201/2011 Art. 19)
- **Rate raised from 0.76% → 1.06% from 1 Jan 2024** (L. 213/2023 · Legge di Bilancio 2024 art. 1 c. 91). Verified against AdE scheda.
- Tax base:
  - **EU/EEA with adequate exchange**: cadastral value of host country, else acquisition cost, else FMV.
  - **Non-EU/non-cooperative**: acquisition cost or FMV.
- Rate 0.4% on principal residence (categorie A/1, A/8, A/9 only); €200 detrazione for principal residence.
- Foreign property-tax credit (IMU-equivalent) deductible from IVIE.
- 2025 payment deadline postponed to 1 Dec 2025.

### IVAFE — Foreign Financial Assets (DL 201/2011 Art. 19)
- 0.20% annual on financial assets abroad (raised to 0.40% for assets in non-cooperative blacklist countries from 2024).
- Bank account fixed €34.20.
- **Real estate excluded** from IVAFE (covered by IVIE).

### Quadro RW — Foreign Asset Monitoring (Modello Redditi)
- Mandatory disclosure of all foreign assets (banks, securities, real estate, art, gold, life insurance, crypto) held by Italian residents — **even if no income earned**.
- Real estate listed at original cost in EUR.
- Penalties: 3-15% of undeclared amounts (6-30% for blacklist countries); reduced regime via ravvedimento operoso. €258 fixed if filed within 90 days. From 1 Sep 2024 some violation categories cut to 25% (D.Lgs. 87/2024 sanctions reform).

### CGT on disposal — Art. 67 TUIR
- Real estate held **> 5 years** = exempt from IRPEF (applies to foreign property too).
- Within 5y: ordinary IRPEF marginal OR **26% imposta sostitutiva** (DPR 600/73 art. 38-bis), elected via the deed/notary at sale (foreign property: option requires reporting through Italian notary or substitute filing).
- Treaty allocation typically situs to property country.

### Inheritance — D.Lgs. 346/90
- Worldwide for Italian-resident decedent.
- Spouse / direct line: €1M nil-rate band per heir, then 4%; siblings €100k, 6%; others 8%.
- DTT estate-tax network: ~7 countries.

### Special regimes
- **Art. 24-bis TUIR — neo-resident lump-sum**:
  - €100k/y flat tax on foreign income for individuals transferring residence to Italy who were non-resident for ≥ 9 of last 10 years.
  - **Doubled to €200k/y** for residence-transfer **on/after 10 Aug 2024** (DL 113/2024 · Decreto Omnibus). Pre-10-Aug-2024 movers grandfathered at €100k for life of regime (15 years).
  - Family-member add-on €25k each.
  - **Exempts from IVIE/IVAFE and Quadro RW** for assets covered.
  - **2026 PLF (draft)** proposes raising to €300k for new opt-ins from 1 Jan 2026 — not yet law as of date stamp.
- **Art. 24-ter TUIR — pensioners' 7% flat**:
  - Foreign-pension recipients moving to Mezzogiorno (SI/CL/SA/CM/BA/AB/MO/PU) communes < 20,000 inhabitants → 7% flat tax on all foreign income, 9 years.
  - **Population limit raised 20k → 30k by L. 34/2026 effective 7 Apr 2026** — broadens eligible communes.

### 2024-2026 reforms
- **L. 213/2023** (LdB 2024): IVIE → 1.06%; IVAFE blacklist → 0.40%.
- **D.Lgs. 209/2023**: residenza fiscale rules (1 Jan 2024).
- **DL 113/2024** (10 Aug 2024): 24-bis flat tax doubled to €200k.
- **D.Lgs. 87/2024**: monitoring-violation penalties reformed (1 Sep 2024).
- **L. 34/2026**: 24-ter Mezzogiorno 30k pop limit.
- **PLF 2026 draft**: 24-bis → €300k under negotiation.

**Confidence: HIGH** (except 24-bis € figure pending PLF 2026 = MEDIUM) · **Last verified**: 2026-05-09

---

## Buyer cohort: Spain — LIRPF · LIP · ITSGF · LISD

### Tax residence — Art. 9 LIRPF (Ley 35/2006)
ANY of: > 183 days in Spain in calendar year · centro de intereses económicos in Spain · spouse + minor children resident (presumption).

### Foreign rental — Sección H Modelo 100
- Reported as capital inmobiliario in IRPF; taxed in **base general** at progressive rates up to 47% (state + autonomous).
- **60% reduction (Art. 23 LIRPF)** for residential leases applies **ONLY to Spanish properties** — foreign rental gets no 60% reduction.

### Imputed income on **unrented** foreign property — Art. 85 LIRPF
Resident must impute notional income annually on any foreign second home that is not rented out (treated like Spanish 2nd homes):
- 1.1% of cadastral-equivalent value if revised in last 10 years; else 2%.
- For foreign property without cadastral value: **1.1% × 50% of value used for Wealth Tax** (acquisition cost or higher FMV).

### CGT on disposal — base ahorro
- **Brackets from 1 Jan 2025**: 19% (≤ €6k) · 21% (6-50k) · 23% (50-200k) · 27% (200-300k) · **30% (> €300k)** — top bracket raised from 28% → 30%.
- DTT allocation: usually situs to property country with credit method in Spain.
- **Habitual residence reinvestment exemption (Art. 38 LIRPF + RIRPF Art. 41)**: gain on principal residence sale exempt if reinvested in another principal residence (in Spain, EU or EEA-with-exchange) within 2 years before/after.
- **Persons > 65**: full exemption on principal-residence sale (Art. 33.4.b LIRPF).

### Wealth Tax — IP (Ley 19/1991)
- Worldwide net assets; state minimum exempt €700k + €300k for habitual residence.
- Autonomous communities can vary: **Madrid 100% bonificación** (paused while ITSGF active — see below); **Andalucía** restored bonificación for ≤ €3.7M from 2024; **Cataluña** has its own scale.
- Foreign real estate at acquisition value or higher market.

### ITSGF — Impuesto Temporal de Solidaridad de las Grandes Fortunas (since 28 Dec 2022)
- State-level surtax on net wealth > **€3M**; rates 1.7% (3-5M) · 2.1% (5-10M) · 3.5% (> €10M); first €700k exempt + autonomic exempt threshold considered.
- Designed to neutralise Madrid/Andalucía wealth-tax bonificación — IP paid is creditable against ITSGF.
- **Real Decreto-ley 8/2023 (27 Dec 2023)** extended ITSGF **indefinitely** ("hasta que no se revise la tributación patrimonial en el marco de la financiación autonómica"). Filed via **Modelo 718** between 1-31 July following the tax year.

### Beckham Law — Art. 93 LIRPF (impatriates regime)
- 24% flat on Spanish-source employment income up to €600k (47% above); foreign-source income generally **untaxed** in Spain (favorable for cross-border buyers).
- 6 tax years (year of arrival + 5).
- **Reformed by Ley 28/2022 (Startups Law) effective 1 Jan 2023**: extended to international teleworkers (visa under L. 14/2013), entrepreneurial-activity movers, qualified-skill professionals; spouse + minor children eligible.

### Reporting — Modelo 720 + Modelo 721
- **Modelo 720** (annual, by 31 March): foreign assets > **€50k per category** (accounts / securities-funds-pensions / real estate). Once filed, refile only if value increased > €20k or asset disposed of.
- **ECJ Case C-788/19 (27 Jan 2022)**: M720 penalty regime ruled disproportionate. **Ley 5/2022 (9 Mar 2022)** removed the special penalty regime — now ordinary LGT penalties apply.
- **Modelo 721** since 2024: separate crypto-asset disclosure.

### Inheritance — ISD (Ley 29/1987)
- Worldwide for Spanish-resident heir (or for non-resident on Spanish-situs assets).
- Autonomous variation enormous — **Madrid 99% bonificación · Andalucía 99% direct line · Murcia 99% · Valencia 99% post-Jul-2023**.
- Heir gets **stepped-up basis** at ISD-assessed FMV — no carry-over.
- DTT estate-tax: only ~3 countries.

### 2024-2026 reforms
- 1 Jan 2025: top base-ahorro bracket 28% → **30%** for > €300k.
- ITSGF extended indefinitely (RDL 8/2023).
- Beckham extended to teleworkers + entrepreneurs (Ley 28/2022, effective Jan 2023).
- L. 13/2023 anti-fraud / DAC7 transposition.
- 1 Jan 2025: Pillar Two transposition.

**Confidence: HIGH** · **Last verified**: 2026-05-09

---

## Buyer cohort: Netherlands — Wet IB 2001 · AWR · Successiewet 1956

### Tax residence — Art. 4 AWR
Facts-and-circumstances; family ties primary (where the family physically lives weighs heavier than registration). Treaty tie-breaker overlays.

### Foreign real estate — **Box 3 (vermogensbelasting via fictief rendement)**
- Box 3 = deemed (fictitious) return on net wealth on 1 Jan reference date. Not capital gains; not actual rent.
- **Threshold 2026: heffingsvrij vermogen €59,357 / €118,714 fiscal partners** (raised from €57,000 / €114,000 in 2024).
- **Forfait rates 2026**: 1.44% on bank savings · **6.04% on overige bezittingen (incl. real estate, both Dutch and foreign)** · 2.62% on debts.
- Foreign real estate enters at FMV minus mortgage debt. Most DTTs allocate to situs country with NL **vrijstelling met progressievoorbehoud** (treaty exemption with averaging effect on the Box 3 rate calc).
- Valuation: **Hoge Raad** confirmed WOZ-equivalent / market value; for property available for own use, market rental value may be added from 2026.

### Box 3 reform — the live constitutional crisis
- **Hoge Raad 6 Jun 2024** (and 14 Jun 2024 follow-ups, then **20 Dec 2024**): existing Box 3 forfait still violates Art. 1 EP ECHR; **actual return** must cap the levy. **Voordeel wegens eigen gebruik** (own-use benefit) of real estate set to **NIL** for actual-return purposes.
- **Tegenbewijsregeling** ("counter-proof rule"): from 2025 (covering 2017-2024 affected years; 2025+ forward), taxpayers can demonstrate actual return < forfait via **OWR — Opgaaf Werkelijk Rendement** (folded into regular IB return from tax year 2025).
- **Wet werkelijk rendement box 3** — full move to actual-return basis: originally 2026 → postponed to 2027 → **postponed again to 1 Jan 2028**. Tweede Kamer adopted the bill 12 Feb 2026; the Eerste Kamer deferred its final vote on 30 Jun 2026 pending an announced novelle, and the Belastingplan 2027 bill of 15 Sep 2026 contains no Box 3 measure, with no novelle introduced (Eerste Kamer file 36.748, 17 Sep 2026); the cabinet's 14 Sep 2026 letter (EK 36.748, Q) asks the Senate to keep holding the bill and lists withdrawing it, with the forfaitaire system plus tegenbewijsregeling kept longer and a full vermogenswinstbelasting in 2030, as one of four scenarios. **Status as of 2026-09-17: bill (36.748) held in the Eerste Kamer; entry into force by royal decree with 1 Jan 2028 as an unsecured target — model the forfaitaire system with the tegenbewijsregeling for 2026 and 2027.**

### Box 1 — only if "more than asset management"
If active landlord status (multiple foreign properties + professional involvement) → Box 1 progressive (2025 top rate 49.5%). High threshold; rare for individual foreign-property buyers.

### CGT on disposal — none for individuals
NL has **no separate CGT** for individuals on real estate held privately. Box 3 deemed return only; actual gain on disposal not separately taxed. Treaty allocates to situs country.

### Inheritance — Successiewet 1956
- Worldwide for Dutch-resident decedent.
- **10-year rule (tienjaarsregeling, Art. 3 SW)**: a person of **Dutch nationality** who dies (or makes a gift) within 10 years after emigration is deemed Dutch-resident → Dutch IHT still applies regardless of where assets sit. Non-Dutch nationals: only 1-year window for gifts; no IHT post-emigration.
- Allowances 2024 (verify 2026 figures): spouse €795k · child €25,187 · others €2,690. Rates 10-40% (sliding by class + bracket).

### Reporting
- No comprehensive foreign-asset register equivalent to Modelo 720 / Quadro RW.
- Box 3 question on foreign assets in IB return.
- CRS auto-exchange handles bank/brokerage data.
- Belastingdienst foreign-asset compliance team active; CRS gap-analysis used to surface non-disclosure.

### 2024-2026 reforms
- **30%-ruling**: original 2024 plan was 30/20/10 stair-step; **reversed by Tax Plan 2025** (Senate 17 Dec 2024) → flat **27% from 1 Jan 2027** with €50,436 income standard; existing 30% rulings grandfathered at 30% through 2026.
- Box 3 actual-return Wet WRBox3 → 1 Jan **2028** target NOT secured (bill held in the Eerste Kamer; the cabinet's 14 Sep 2026 letter lists withdrawal as one of four scenarios — verify).

**Confidence: HIGH** for Box 3 thresholds + 30%-ruling timeline; **MEDIUM-LOW** for the actual-return effective date (still in parliamentary navette) · **Last verified**: 2026-05-09

---

## Buyer cohort: Nordics — SE / NO / DK / FI

### Sweden — IL (Inkomstskattelagen 1999:1229) + Skatteverket
- Residence (IL § 3:7): bosatt OR stadigvarande vistelse > 6 mo continuous. Worldwide income for residents (§ 3:8).
- Foreign rental: kapitalinkomst flat **30%**. Treaty WHT credited.
- CGT on disposal: privatbostad effective **22%** (§ 45:33 quotient); non-private 30%. Foreign property qualifies as privatbostad if used as own/family residence + meets § 2:8 criteria.
- Uppskov (deferral on replacement): available within EU/EEA only.
- **No wealth tax** (abolished 2007). **No inheritance tax** (abolished 2005).
- Tio-årsregeln § 3:19 — 10-year tail on **shares only**; foreign RE outside scope (treaty allocates situs).
- 2024-26: no major changes; capital-income rate stable at 30%.
- **Confidence: HIGH**.

### Norway — Skatteloven (LOV-1999-03-26-14) + Skatteetaten
- Residence (§ 2-1): > 183 d in any 12-mo OR > 270 d in 36 mo. Worldwide income for residents.
- Foreign rental: kapitalinntekt **22%** (general rate 2024-26).
- DTT method: **credit** (§ 16-20 ff.), not exemption.
- **Formueskatt** (wealth tax): net worth > NOK 1.7M; rate 1.0% state + 0.7% municipal ~1.1% combined; surtax 0.4% > NOK 20M. Foreign property included at FMV; mortgage deductible. **Foreign property valuation cap**: taxable value capped at **30% of market value** (formuesverdi).
- CGT (§ 9-3): primary-residence exemption requires owned ≥ 1y AND lived ≥ 1 of last 2 years; rule applies equally to foreign primary residence (Skatteetaten BFU practice). Otherwise 22%.
- **Exit tax § 10-70 — substantially tightened 2024-25**: NOK 500k threshold replaced with NOK 3M basic allowance; mandatory 12-year payment cap; 70% of dividends must service exit-tax liability from 7 Oct 2024. **Shares only — not direct RE**.
- **Inheritance tax: ABOLISHED 2014**.
- 2026 reform: new formuesverdi model from income year 2026 using sub-municipal data.
- **Confidence: HIGH**.

### Denmark — KSL · LL · EVSL + Skattestyrelsen
- Residence (KSL § 1): full tax liability on residence + 6-month presumption.
- Foreign rental: kapitalindkomst (or personlig if active). LL § 15O flat-rate scheme available for holiday-home letting.
- DTT method: credit (treaty exemption rare).
- **Ejendomsværdiskat (EVS) on FOREIGN property** — Danish tax residents pay EVS on foreign-located residential property at the **same rates as Danish properties**: **0.51% up to DKK 9.4M / 1.4% above** (2024). Tax basis = market value 1 Jan of preceding income year, OR purchase price adjusted by an approved foreign price index.
- **2024 property-tax reform** — new property-tax model effective 1 Jan 2024 (Boligskatteloven). Tax-credit ("skatterabat") protects pre-2024 buyers from any net increase vs. old rules; applies equally to foreign property. UK index approved by Vurderingsstyrelsen with forward effect from 2024.
- CGT — Ejendomsavancebeskatningsloven (EBL) § 1; principal-residence/sommerhus exemption (§ 8 / § 9) applies to foreign property if served as actual residence (parcelhusreglen).
- **Wealth tax: ABOLISHED 1995**.
- Inheritance (boafgift) — Boafgiftsloven § 1: worldwide for resident decedent; **spouse exempt**; descendants/parents **15%**; other heirs **36.25%**; 2025 tax-free threshold DKK 346,000.
- **Confidence: HIGH**.

### Finland — TVL (Tuloverolaki 1535/1992) + Verohallinto
- Residence (TVL § 9): yleisesti verovelvollinen if domicile in Finland OR continuous presence > 6 months. Worldwide income for residents.
- Foreign rental: pääomatulo **30% up to €30,000**, **34% above** (2024-26). Reported on Form 7H + Form 16B.
- DTT method: credit primarily.
- Loss offset (TVL § 50): capital loss offset only against capital income within same and following 5 tax years.
- CGT: myyntivoitto pääomatulo 30/34%. Own-use residence exemption TVL **§ 48**: tax-free if owned ≥ 2y AND used as own/family principal residence ≥ 2 continuous years before sale. **Applies to foreign principal residence** per Verohallinto cross-border guidance.
- **Wealth tax: ABOLISHED 2006**.
- Perintövero (inheritance) — worldwide for resident decedent. 2024 brackets: spouse personal exemption €90,000; child €20,000; Class I 7-19%; Class II 19-33%.
- **Confidence: HIGH**.

---

## Buyer cohort: Switzerland — DBG/LIFD + cantonal Steuergesetze + ESTV

### Tax residence — DBG Art. 3
Unbeschränkte Steuerpflicht via domicile, OR ≥ 30 days physical presence with gainful activity, OR ≥ 90 days without. Worldwide income at federal — but **treaty allocates RE income to situs (Art. 6 OECD MTC)**, so foreign rental is exempted from Swiss tax base, **retained for rate progression**.

### Eigenmietwert (imputed rental) on foreign owner-occupied property
Art. 21 Abs. 2 DBG: notional rental value of foreign primary/secondary residence is **included in Swiss tax base for rate-progression purposes** (then stripped from taxable income via treaty). Practitioner trap: even unrented foreign holiday homes raise Swiss marginal rate.

### Foreign mortgage interest
Deductible against worldwide income subject to **Schuldzinsenabzug-Quote** (debt-allocation by asset location); foreign mortgage on foreign property generally allocates deduction to foreign income source, reducing Swiss benefit.

### Vermögenssteuer (cantonal wealth tax)
Worldwide net wealth INCLUDING foreign RE; rates 0.1-1% by canton (typical bands: ZH 0.07-0.30%, GE 0.4-1%, VS up to 0.5%). Treaty allocates wealth tax on RE to situs — Swiss canton excludes from taxable wealth but **uses for rate progression**.

### CGT — cantonal Grundstückgewinnsteuer
Federal does NOT tax CGT on private RE gain. **Most cantons tax only domestically-located RE** — foreign RE gains typically out of cantonal scope (verify canton).

### Lump-sum / Pauschalbesteuerung
DBG Art. 14: still available federally; **5 cantons abolished cantonally** (ZH, BS, BL, SH, AR).

### Inheritance — cantonal
Spouse exempt in essentially all cantons; children exempt in most (taxed in BL, AG, AR, OW). Foreign RE typically allocated to situs canton/state.

### MAJOR REFORM — Eigenmietwert ABOLISHED
- **Vote**: 28 Sept 2025, **57.7% Yes** — constitutional amendment + new Federal Decree on cantonal property taxes on second homes.
- **Implementation**: **1 January 2029**, set by Federal Council decision of 1 Apr 2026 (2026 data, source [admin.ch media release](https://www.admin.ch/de/newnsb/yGTqBPowRqyVh0zPokW-q); German only — `https://www.admin.ch/en/newnsb/yGTqBPowRqyVh0zPokW-q` returns the English portal landing, "this content is not available in English").
- **Effect on foreign property**: imputed rental of foreign owner-occupied home no longer included for rate progression after Jan 2029; foreign property still declarable for **wealth tax progression**.
- **Mortgage interest deduction** also abolished in tandem; transitional 10-year tapered deduction for first-time buyers (married couple: CHF 10k year 1, declining CHF 1k/year to zero).
- **Maintenance/renovation deductions** also abolished.
- **Until 1 Jan 2029**: existing Eigenmietwert-on-foreign-property regime fully in force.

**Confidence: HIGH** (reform passed; effective date locked at 2029) · **Last verified**: 2026-05-09

---

## Buyer cohort: Asia — JP / KR / SG / HK / CN

### Japan — Income Tax Act (Shotokuzeihō, Act No. 33 of 1965) + NTA
Three-tier residence:
- **Non-resident** — Japan-source only.
- **Non-Permanent Resident (NPR)** — resident but Japan-domiciled < 5 years in last 10. Taxed on Japan-source + foreign-source paid in Japan + foreign-source remitted to Japan.
- **Permanent Resident (PR)** — > 5 years in last 10. Worldwide income.

5-year transition trap: PR status auto-attaches once threshold crossed, NOT linked to immigration "permanent residence" visa. Foreign rental switches from NPR-remittance regime to full taxation.

Foreign rental (PR): fudosan shotoku, comprehensive income; aggregate progressive 5-45% national + 10% local + 2.1% reconstruction surtax.

CGT on foreign disposal:
- **Long-term (> 5y holding)**: 15% national + 5% local + 0.315% reconstruction surtax = **~20.315%**.
- **Short-term (≤ 5y)**: 30% national + 9% local = **~39%+**.

Principal-residence ¥30M deduction (§ 35 ITA) applies to foreign principal residence per NTA practice.

Exit tax (§ 60-2 ITA): **securities/derivatives ≥ ¥100M** held by individuals resident in Japan ≥ 5 of last 10 years before departure (rule from 1 Jul 2015). **Real estate (Japan or foreign) explicitly NOT included.** Flat 15.315% on deemed gain.

Inheritance (sōzokuzei): 10-55% sliding; basic deduction ¥30M + ¥6M × statutory heirs. Worldwide if decedent/heir Japan-resident — **including foreign property**. **10-year tail**: Japanese nationals leaving Japan remain in Japanese inheritance scope for 10 years post-departure (2017 reform). **Visa-based scope**: Table 2 visa holders (PR, spouse-of-Japanese, long-term resident) taxed on worldwide assets if jusho is in Japan.

Foreign-Asset Disclosure (Form 5060 / kokugaizaisanchosho): foreign assets ≥ ¥50M at year-end; understatement penalty 5-30%.

**Confidence: HIGH**.

### South Korea — KITA + NTS + Inheritance & Gift Tax Act
- Residence (Art. 1-2): domicile in Korea OR ≥ 183 days. Worldwide for residents.
- **Foreign-national 5-year shield**: non-Korean tax residents domiciled/resident in Korea ≤ 5 years (cumulative) in prior 10-year period taxed only on Korean-source + foreign-source paid in or remitted to Korea. After 5 of last 10 → full worldwide.
- Foreign rental: 종합소득 (jonghap sodek), comprehensive aggregate; brackets 6.6%-49.5% (incl. 10% local surcharge); 2024 bracket adjustment.
- CGT — yangdo sodeukse: 6-45% sliding > 2y; surtax to 50% < 1y.
- Foreign-asset reporting: Form 해외금융계좌 (Article 34 IITA) if aggregate foreign financial accounts > KRW 500M month-end. **Foreign real estate NOT reportable on this form.**
- Exit tax (Art. 118-9): since 1 Jul 2018; departing residents holding stock ≥ KRW 500M. **NOT real estate.**
- Inheritance: globally for Korean-resident decedent; rates 10-50% (top rate 50% > KRW 3B); among highest in OECD.
- **2025-28 reform**: National Assembly Dec 2025 passed minor amendments. **Inheritance Acquisition System** — planned shift from estate-tax to per-heir-share, bill submission May 2026, target **2028 (NOT yet enacted)**. Per-child basic deduction proposed KRW 50M → 500M; spouse exemption raised.
- **Confidence: HIGH** (current law); **MEDIUM** on 2028 reform timing.

### Singapore — Income Tax Act 1947 + IRAS
- Residence (s.2): ≥ 183 d physical presence in calendar year, OR continuous 3-year arrangement.
- **Territorial principle** — Singapore taxes only Singapore-source income + foreign income received in Singapore.
- **Foreign rental — INDIVIDUAL EXEMPTION** — Section 13(7A) ITA exempts foreign-sourced income (incl. rental) received in Singapore by **resident individuals** (not via partnership), in force since 1 Jan 2004. Effectively: foreign rental is **never taxable in Singapore** for resident individuals.
- Foreign property disposal: Singapore has **no general CGT**. Gains not taxable unless trade/business in property dealing.
- Property Tax Act only on SG-located property. **No wealth tax. No estate duty** (abolished for deaths from 15 Feb 2008).
- CRS active 2017+.
- 2024-26: GST raised to 9% Jan 2024; FSIE-MNE refinements (Pillar Two-aligned) for **corporates, not individuals**.
- **Confidence: HIGH**.

### Hong Kong — Inland Revenue Ordinance Cap. 112 + IRD
- **Territorial principle** — only HK-source profits/income taxable.
- Foreign rental income — **NOT taxable** (sourced offshore). HK Property Tax (IRO Part X) only on HK-located property.
- Foreign property disposal — **no general CGT**; not taxable.
- **No wealth tax. No estate duty** (abolished for deaths after 11 Feb 2006).
- **FSIE regime** — Dec 2022 / Jan 2023 + 2024 refinement (IRO ss.15H–15Q): certain foreign-sourced passive income (interest, dividend, IP, disposal gain) of an **MNE entity carrying on a trade/business in HK** is treated as HK-source if received without economic-substance compliance. **Does NOT apply to individuals' foreign rental.**
- Stamp duty (BSD/SSD/AVD) only on HK property; cooling measures relaxed Feb-Oct 2024 (BSD/SSD/NRSD removed 28 Feb 2024).
- New Capital Investment Entrant Scheme — relaunched 1 Mar 2024, HK$30M minimum (residential property excluded).
- **Confidence: HIGH**.

### China — PRC Individual Income Tax Law (2018 revision, eff. 1 Jan 2019) + STA
- Residence (Art. 1): domiciled in China OR ≥ 183 days in tax year. Worldwide taxation for residents (post-2019 reform).
- **6-Year Rule (IIT Implementing Regulations Art. 4)** — for non-domiciled foreign individuals resident ≥ 183 d/year: foreign-source income exempted unless paid by China entity/individual or remitted, **until 6 consecutive years are accumulated**. Single absence > 30 consecutive days in any year **resets the count**. Period started 2019 — first cumulative crossing possible **2025 tax year**.
- Foreign rental: under IIT comprehensive income, "income from lease of property" — flat **20% on net rental** (after 20% standard deduction or actual expenses, whichever lower).
- Foreign property disposal: IIT "income from transfer of property" at **20% on gain**.
- DTT method: credit (foreign tax credit Art. 7).
- **No wealth tax. No inheritance tax** — proposed since the 1990s, **never enacted**; **as of 2026, no inheritance/estate tax in PRC**.
- Foreign-exchange constraint — SAFE individual outbound quota **USD 50,000/year** — practical barrier to large-scale foreign-property purchase/sale repatriation, independent of tax.
- CRS active 2017+; 2024 individual annual reconciliation campaign sharply raised foreign-asset enforcement against HNW residents.
- **Confidence: HIGH** (rules); **MEDIUM** on enforcement intensity (escalating).

---

## Buyer cohort: Israel — Income Tax Ordinance + ITA (Tax Authority)

### Tax residence
Center-of-life test (Section 1 ITO; no fixed-day rule though days considered).

### Foreign rental — § 14(a)(7) ITO regime choice
- **15% flat** on gross rental, no deductions/depreciation, no foreign-tax credit; OR
- **Marginal rates** with full deductions/depreciation + FTC.

Election made annually on Form 1301.

### Olim Chadashim / Returning-Resident 10-year exemption (§ 14(a) ITO)
Full income/CGT exemption on foreign-sourced income for 10 years from Israeli tax residency (post-2008 Olim Reform).

### MAJOR 2026 REFORM — disclosure repeal + new 5-year incentive
- **Reporting exemption REPEALED from 1 January 2026**: olim and returning residents must henceforth **report** foreign income/assets and trust positions, even where still tax-exempt. (OECD pressure; draft published Feb 2025.)
- **NEW 5-year regime** for arrivals **5 Nov 2025 – 31 Dec 2026**: enhanced exemption on Israeli-sourced income for tax years 2026-2030 up to defined ceiling, layered on top of the existing 10-year foreign-income/asset exemption (which itself remains intact).
- The 10-year tax exemption on foreign rental income remains in force; the change is purely on the **reporting** side.

### CGT on foreign disposal (§ 88-91 ITO)
Real CGT (post-1 Jan 1994 inflation-stripped) at **25%** for individuals; **30%** if seller was a 10%+ shareholder of the entity holding the asset (or in the prior 12 months). Linear inflation/CPI adjustment.

### Exit tax (§ 100A ITO)
Applies on cessation of Israeli residency; deemed sale of all assets; payment may be deferred until actual disposal with security/lien provisions.

### Inheritance: ABOLISHED 1981
**No estate duty.**

**Confidence: HIGH** (2026 reform); **MEDIUM** on whether the 10-year tax exemption survives beyond 2027 (under continued OECD scrutiny).
**Last verified**: 2026-05-09.

---

## Buyer cohort: Emerging-market — IN · BR · MX · ZA · AE · SA · GCC

The EU-core + common-law regimes above are baseline. Foreign-property buyers also come from emerging-market jurisdictions whose home-tax overlay is materially different (capital controls + outbound-FX taxes + black-money disclosure + Zakat — instead of the EU's wealth-tax + monitoring-form pattern).

### India — Income-tax Act 1961 + RBI/FEMA + Black Money Act 2015
- **Residence** (ITA § 6): resident if 182d in PY, OR 60d in PY + 365d in 4 prior PYs. The 60-day threshold is **120d** for Indian-citizens / PIOs whose **non-foreign-source income > ₹15 lakh** (post-1 Apr 2020 Finance Act 2020).
- **RNOR transition**: 2-year favourable bracket on return — foreign-source income generally NOT taxable unless received in India. RNOR if NR in 9 of 10 prior PYs OR ≤ 729d in 7 prior PYs.
- **Worldwide income**: ROR yes; RNOR only India-received; NR only India-source.
- **Foreign rental** (ROR): Schedule HP / Schedule OS — slab rates up to 30% + cess (4%).
- **Foreign CGT** (ROR): LTCG (> 24m holding for immovable) **12.5%** post-23 Jul 2024 Budget — **indexation removed**; was 20% with indexation. Pre-23-Jul-2024 properties grandfathered: resident individuals/HUFs may elect 20%-with-indexation. STCG marginal slab.
- **LRS — Liberalised Remittance Scheme** (RBI Master Direction): **USD 250,000/yr** per resident outward, including foreign immovable acquisition.
- **TCS on LRS**: **20%** on outward remittance > **₹7 lakh** (eff. 1 Oct 2023; raised from 5%). Education/medical lower rates.
- **Schedule FA** (Foreign Assets schedule of ITR): mandatory for ROR — even jointly-held foreign property; even if no taxable income.
- **Black Money Act 2015 § 43 / § 50**: penalty **₹10 lakh per year** for non-disclosure (or inaccurate disclosure) in ITR; tax 30% + penalty 90% (300% of tax) on undisclosed; 7y + 3m–10y prosecution.
- **FEMA repatriation**: sale proceeds of foreign immovable acquired under LRS must generally be repatriated to India within **180 days** (FEMA 21/2000-RB). NRIs separately can repatriate USD 1M/yr from NRO accounts.
- **DTT relief**: credit method (Form 67 mandatory before due-date of return).
- **Inheritance**: Estate Duty abolished 1985; carry-over cost basis on inherited foreign property.
- 2024-26: TCS-LRS 20% (1 Oct 2023); LTCG 12.5% no-indexation (23 Jul 2024); Schedule FA expansions; AY 2026-27 ITR-form refresh.
- **Confidence: HIGH** (statute + CBDT primary).

### Brazil — RFB + Lei 14.754/2023 + EC 132/2023
- **Residence**: visto permanente OR **183d in 12 mo** (RFB IN 208/2002).
- **Worldwide income**: residents — yes.
- **Lei 14.754/2023** (eff. **1 Jan 2024**): annual taxation of offshore financial investments + controlled-entity profits — replaces the prior repatriation-deferred regime. **Flat 15% IRPF** on offshore capital income/gain. Exchange-rate variation now part of computation.
- **Foreign rental** (resident): **Carnê-Leão Web** monthly self-assessment, progressive to 27.5%; reconciled annually in DIRPF.
- **Foreign CGT — Ganho de Capital**: sliding **15% / 17.5% / 20% / 22.5%** for gain brackets up to R$5M / R$10M / R$30M / > R$30M; converted to BRL via PTAX.
- **Bens no Exterior** (DIRPF annual): mandatory declaration of foreign assets including immovable property at cost basis.
- **CBE — Capitais Brasileiros no Exterior** (BCB declaration): mandatory if **assets > USD 1M** at year-end (annual); quarterly if > USD 100M.
- **IOF outbound**: **1.10%** for outbound FX for investment purposes (post-Decree 12,466/2025); **0.38%** for property-purchase remittances at the lower band — IOF rate has been politically volatile through 2025, verify weekly.
- **CRS**: active 2018+ (RFB receives via AEOI).
- **ITCMD inheritance** (state, 2-8%; SP/RJ 4%, MG 5%): EC 132/2023 made progressivity **mandatory** + brought foreign assets into scope; PLP 108/2024 standardisation pending; LC 227/2026 regulates trusts + abroad-asset taxation.
- 2024-26: Lei 14.754/2023 (1 Jan 2024); EC 132/2023 ITCMD progressivity; PLP 108/2024 + LC 227/2026 ITCMD harmonisation.
- **Confidence: HIGH** on Lei 14.754; **MEDIUM** on ITCMD harmonisation final shape.

### Mexico — LISR + SAT
- **Residence** (CFF Art. 9): domicilio + family + centre-of-vital-interests; > 50% income from Mexican source = resident.
- **Worldwide income** (LISR Art. 1): residents — yes.
- **Foreign rental** (resident): LISR Título IV Cap. III — comprehensive ISR up to **35%** marginal; deductions on actual basis OR 35% blind deduction.
- **Foreign CGT** (resident): included in worldwide ISR base; FTC under treaty (LISR Art. 5).
- **Foreign-asset disclosure**: **Anexo 8 / Anexo 9** of annual declaration; REGIN reporting; high penalties Forms 76/77 for transactions with REFIPRES (low-tax) jurisdictions.
- **Inheritance**: federal — none; state — varies (zero in most); worldwide for resident heir.
- **Fideicomiso quirk**: when Mexican holds foreign property via a Mexican trust, § 988-style FX issues arise on the Mexican side; Art. 24 USA-MX DTT relief if US-side property.
- 2024-26: Reforma Hacendaria 2024 announcements; FATCA / CRS continued; SAT enforcement intensification on undeclared foreign accounts.
- **Confidence: HIGH** (LISR + SAT primary). NOTE: a non-resident landlord on Mexican rental faces 25% gross withholding (LISR Art. 158) — that's the source-side, often confused; for the **home** side of a Mexican-resident buying abroad, slab rates apply.

### South Africa — ITA 58/1962 + SARS + SARB
- **Residence** (ITA § 1): "ordinarily resident" common-law test OR physical-presence test (91d in current YOA + 91d in each of 5 prior + 915d aggregate).
- **Worldwide income** (post-2001 source-to-residence reform): yes.
- **Foreign rental**: marginal rate up to **45%**; **§ 6quat** rebate for foreign tax paid (credit method).
- **SARB Exchange Control**:
  - **Single Discretionary Allowance (SDA)**: **R1M/yr** per adult — no SARS clearance under R1M.
  - **Foreign Investment Allowance (FIA)**: **R10M/yr** above SDA — Tax Compliance Status (TCS) PIN from SARS required.
  - Above R11M: SARS Approval for International Transfer (AIT) PIN application + supporting docs.
- **§ 9D Controlled Foreign Company**: net-income attribution to SA-resident participants > 50% / > 10%.
- **CGT on foreign property** (§ 26A): inclusion rate **40%** for individuals × top 45% rate ≈ **18% effective** (~25% in highest brackets).
- **Primary residence exclusion**: **R2M** (raised to **R3M from 1 Mar 2026** per 2026 Budget) — applies to foreign primary residence too if ordinarily resided.
- **§ 9H exit tax**: deemed disposition on cessation of residence — worldwide assets EXCEPT SA-situs immovable. **Foreign property INCLUDED**. R40k annual exclusion, 40% inclusion × marginal rate.
- **Estate Duty Act**: global for resident decedent; **R3.5M abatement**; **20%** rate (25% > R30M).
- **Reporting**: SARS auto-receives via CRS; explicit foreign-asset section on ITR12.
- 2024-26: 2024 Budget left major rates flat; SARS HNW unit enforcement up; AIT PIN process tightened 2024.
- **Confidence: HIGH**.

### UAE — Federal Decree-Law 47/2022 + FTA
- **PIT for individuals**: **NONE**.
- **Foreign rental income** held by UAE-resident individual: **NOT taxable in UAE**. Source-country tax applies.
- **Corporate tax** (eff. **1 Jun 2023**): **9%** on business profits > **AED 375,000**; 0% below.
- **Natural-person CT scope**: triggered when individual conducts a "business activity" with **annual turnover > AED 1M**. Passive foreign rental held in personal name — generally OUT of scope.
- **Reporting**: no individual income tax → no Form 8938 / T1135 / Modelo 720 / Quadro RW equivalent.
- **CRS**: UAE active since 2018 (FATCA earlier).
- **VAT**: 5% on commercial UAE rental; residential exempt.
- **Foreign-property exposure for UAE-resident** is mostly:
  1. Source-country tax (where the property sits).
  2. NEW home-country tax if they relocate (UAE residents often have IN/EG/PK/UK/RU origin — relocation triggers their original system's worldwide rules).
- 2024-26: CT launch (1 Jun 2023); family-foundation regime added 2024 (Cabinet Decision 261/2024); Pillar Two domestic top-up tax for in-scope groups (proposed Jan 2025).
- **Confidence: HIGH** for the no-PIT baseline; MEDIUM for boundary cases.

### Saudi Arabia — Zakat regime + ZATCA
- **Saudi nationals + GCC nationals**: **Zakat 2.5%** on net zakatable assets (not income tax) — ZATCA-administered. Ministerial Resolution 1007 (21 Mar 2024) issued new Executive Regulations effective fiscal years from 1 Jan 2024.
- **Non-Saudi / non-GCC residents**: generally NOT taxable on personal income unless conducting business through PE.
- **Foreign rental** (individual, passive): generally **outside Zakat scope** for non-business individual; ZATCA hasn't published explicit guidance — treat as data-not-publicly-available, verify with tax adviser.
- 2024-26: Zakat Executive Regulations 2024; e-invoicing waves continue.
- **Confidence: MEDIUM** (individual passive foreign-property treatment under-documented).

### QA / KW / OM / BH
- Generally no PIT for individual residents.
- Foreign-property rental income — outside individual tax scope.
- KW partial Zakat (corporates); **OM PIT proposed 2024 but repeatedly deferred** — unconfirmed as of May 2026, verify quarterly.
- CRS active in all four (FATCA earlier).
- **Confidence: MEDIUM** (Oman PIT timing fluid).

---

## Cross-cutting structural detail

These are the universal lessons that apply REGARDLESS of home jurisdiction. The cross-cutting layer is what differentiates a good due-diligence skill from a country-by-country tax sheet.

### Phantom currency-gain on foreign mortgage payoff (US § 988 + others)

A US person who finances a foreign property with a foreign-currency mortgage, then pays it off when USD has strengthened against that currency, recognises **§ 988 ordinary FX gain** — taxed at marginal rates up to **37%** federal — on the FX swing of the principal. The gain is *phantom*: the homeowner sees no cash benefit; they bought a house, sold the house, paid back the same nominal mortgage. The gain happens because the dollars needed to retire the GBP/EUR/JPY mortgage are FEWER than the dollars they were "obligated to" at acquisition.

- **Anchor case**: ***Quijano v. United States*** (US Tax Court — UK couple sold a UK home; IRS denied integration of FX loss with property gain). Court rejected the § 988(d)(1) hedging-transaction argument because the mortgage wasn't entered into in a trade or business and was personal-use. ([Journal of Accountancy 1997 case note](https://www.journalofaccountancy.com/issues/1997/jan/taxcase.html); [Cornell LII 26 USC § 988](https://www.law.cornell.edu/uscode/text/26/988)) The case is the canonical citation for "you cannot net the FX loss on a personal mortgage against the gain on the home." (The "Vinaigrette" case sometimes cited colloquially — could not source as a published opinion. Use *Quijano* as citable authority.)
- **§ 988(e) personal-transaction limitation**: losses on personal-use FX positions are NOT deductible — one-way asymmetry (gains taxable, losses not deductible). This is the asymmetry buyers underestimate.
- **AU equivalent**: ITAA 1997 Div 775 — Forex Realisation Event 4 ("Ceasing to have an obligation to pay foreign currency") triggers on foreign-mortgage discharge. Gain assessable; private-or-domestic loss generally not deductible. ([ATO forex events](https://www.ato.gov.au/businesses-and-organisations/corporate-tax-measures-and-assurance/foreign-exchange-gains-and-losses/forex-realisation-events))
- **CA equivalent**: ITA § 39(2) — forex gain/loss on capital transaction; first CAD 200 personal-use exemption; remainder is capital, not income (less punitive than US but real).
- **JP equivalent**: yen-denominated computation forces FX into the gain calc (ITA § 57-3; treated as miscellaneous income).
- **NOT a trap in (integrated systems)**: UK (*Bentley v Pike* — currency swing folded into CGT, not separate); DE (Anlage V-Ausland integrated computation); FR (CGI Art. 150 U integrated); IT (computed in EUR throughout).

### PFIC trap — foreign collective investment vehicles (US-only but huge)

Any foreign corporation that meets either the income test (≥ 75% passive income) or asset test (≥ 50% passive-income-producing assets) is a **PFIC under IRC § 1297**. Foreign property funds almost always qualify.

| Vehicle | Country | Typical PFIC status |
|---|---|---|
| **SOCIMI** | ES | PFIC (RE > 50% assets, income passive) |
| **SCPI** | FR | PFIC if held as fund-of-fund or outside the direct-REIT-equivalent path; direct status debated ([HTJ Tax SCPI](https://htj.tax/2022/05/us-tax-treatment-of-french-scpi/)) |
| **Offene Immobilienfonds** | DE | PFIC |
| **REIT** (UK / AU LIT-MIT / SG / HK) | various | PFIC for individual US holders (REIT-comparable status doesn't override PFIC tests) |
| Private property syndicate | various | usually PFIC if > 50% RE-passive |

Three regimes for the US holder ([IRS Form 8621 instructions](https://www.irs.gov/instructions/i8621)):

- **§ 1291 default**: tax + interest charge on excess distributions / sale gain — punitive, can exceed gain itself for long holds.
- **§ 1295 QEF**: pass-through inclusion — but requires PFIC Annual Information Statement, which most foreign funds don't issue.
- **§ 1296 mark-to-market**: only if PFIC stock is "marketable" on a regulated exchange.

**Mitigation**: hold direct (not via fund); accept that "the US-REIT-style efficient vehicle" rarely exists outside US for US-resident holders; or accept § 1291 pain.

### Wealth tax on overseas property — multi-country footprint

Wealth tax rarely makes the buyer's checklist, but it bites hardest on cross-border footprints because **most DTTs DO NOT cover wealth tax**.

| Country | Tax | Threshold | Worldwide for resident? |
|---|---|---|---|
| **FR** | IFI (Impôt sur la Fortune Immobilière) | €1.3M | YES — worldwide RE for FR-resident; FR-situs only for non-resident |
| **ES** | Patrimonio + ITSGF | €700k base + €300k habitual; ITSGF > €3M | YES for resident; ES-situs only for non-resident |
| **NO** | Formueskatt | NOK 1.7M (~€150k) | YES — worldwide net wealth |
| **CH** | Vermögenssteuer (cantonal) | varies by canton | YES — worldwide net wealth |
| **NL** | Box 3 | €59,357 / €118,714 (2026) | YES — deemed-return on worldwide assets |
| **IT** | IVIE on foreign RE | no threshold | 1.06% on foreign RE (NB: this is asset-class-specific, not net-wealth) |
| **DK** | Ejendomsværdiskat | DKK 9.4M lower bracket | YES — Danish rates apply to foreign RE uniquely |

Limited estate / wealth-tax DTTs exist (FR-IT, FR-CH, ES-IT, FR-DE 2002 still in force) — but most DTTs allocate income only, not capital stock. **Practitioner trap**: a French resident buying a Madrid pied-à-terre is in scope for BOTH IFI (worldwide) AND Spanish Patrimonio (Spanish-situs) — the FR-ES treaty does not eliminate the overlap on the Madrid flat itself.

### Estate / inheritance-tax patchwork

Bilateral estate-tax treaties are RARE. The US has **16** ([IRS estate & gift treaties](https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international)): AU, AT, DK, FI, FR, DE, GR, IE, IT, JP, NL, NO, ZA, SE, CH, UK. Anywhere else — foreign property held by a US-domiciled decedent gets DOUBLE-TAXED on death. Other countries' networks are even thinner: DE has 5 in force (DK, FR, CH, US, GR); FR ~7; IT ~7; ES ~3; NL handful.

- **Common scenarios**:
  - US-domiciled buys a Lisbon flat → Portuguese stamp-duty/IMT-mirror on lifetime transfer + US 40% federal estate tax above $13.99M (2025) / $15M (2026 OBBBA permanent) exemption — no PT-US estate-tax treaty.
  - UK-domiciled (post-FIG-regime 6 Apr 2025) — UK IHT 40% on worldwide estate; treaty coverage mostly old (FR, IT, IN, NL, IE, US, ZA, SE).
- **Mitigation**: foreign-grantor-trust (US § 679 gotcha attached); QDOT for non-citizen spouses; life-insurance wrapper for non-US-tax-treaty estates; jurisdiction-shopping for HNW. **Holding via foreign company** can change estate situs but introduces PFIC + CFC + Form 5471/8865 reporting — net neutral or worse for many retail buyers.
- **TCJA estate-exemption**: US federal exemption made **permanent at $15M from 2026** by OBBBA (4 Jul 2025), indexed from 2025 base. Sunset to ~$7M no longer operative. State-level estate / inheritance taxes (NY/MA/CT/IL/MN/OR/WA/RI/ME/VT/MD/HI/DC + MD/NJ inheritance) layer on without treaty relief.

### Departure / exit-tax events

The buyer who moves to a no-tax jurisdiction (UAE, Monaco, Singapore) often discovers their *departure* triggers a deemed-disposition of foreign assets — including the foreign property they just bought.

| Country | Statute | Trigger | Direct foreign RE in scope? |
|---|---|---|---|
| **US** | IRC § 877A | Covered expatriate (net worth ≥ $2M, avg tax liability, certified) — MTM all worldwide | YES |
| **CA** | ITA § 128.1 | Cease residence | YES (foreign RE included) |
| **AU** | ITAA 1997 CGT event I1 | Cease residence | YES (election to defer for some pre-CGT assets) |
| **DE** | § 6 AStG (post-1 Jan 2022 ATAD reform) | ≥ 7 of last 12y resident; **shareholdings ≥ 1%**; new EU/EEA 7-instalment relief replaced indefinite deferral | NO — direct RE NOT in § 6; shareholdings only |
| **FR** | CGI Art. 167 bis | Shareholdings > €800k or > 50% | NO — direct RE NOT in scope |
| **JP** | ITA § 60-2 | Securities > ¥100M (since 2015) | NO — securities only |
| **KR** | ITA Art. 118-9 | Securities > ₩500M (since 2018) | NO — securities only |
| **NO** | Skatteloven § 10-70 | Shareholdings (post-2024 reform: NOK 3M allowance, 12-y cap) | NO — securities only |
| **IL** | § 100A ITO | Emigration; 10y deferral option | YES (broad scope) |
| **ZA** | ITA § 9H | Cessation of residence — deemed worldwide disposal except SA-situs RE | YES (foreign RE included) |

The pattern: **direct foreign real estate is in exit-tax scope in US/CA/AU/IL/ZA and OUT in DE/FR/JP/KR/NO**. Verify always — case law on "deemed residence break" timing has cost real money.

### Structural decisions — direct vs corp vs trust vs LLC

The single biggest strategic question for a foreign-property buyer with material wealth.

- **Direct ownership**: simple notarial chain; full estate-tax exposure to home country; full transparency (no PFIC); full wealth-tax base; usually best for retail buyers under HNW threshold.
- **Foreign company** (Spanish SL, French SCI, Italian Srl): changes estate-tax situs (shareholding can be re-domiciled; shares may attract different tax regime than RE); but US holder is in **PFIC + Form 5471 / 8865** territory. Common in UK/AU buyer-of-Spain footprints.
- **Foreign trust**: § 679 grantor-trust rule for US persons + Form 3520 + 3520-A; complex but useful for non-US grantor with US beneficiary.
- **Fiscally-transparent SPV / LLC** (UK LLP, US LLC, FR EURL): same flow-through tax as direct ownership PLUS legal-liability shield. Common for Anglos buying Spanish/Italian/Portuguese property — but each home jurisdiction's classification of the entity (transparent vs opaque) determines whether it triggers CFC / PFIC / hybrid-mismatch.
- **Joint ownership with spouse**: US estate scenario hinges on **QDOT** (qualified domestic trust) for non-US-citizen spouses — without it, the unlimited marital deduction is denied on US-situs assets if the survivor is non-citizen.

There is no universally "best" structure. **The right structure depends on (a) home jurisdiction, (b) source jurisdiction, (c) net worth, (d) residency intent, (e) succession plan.** Anyone giving a generic "always use an SCI" recommendation without those five inputs is pattern-matching, not advising.

### Treaty FTC vs treaty exemption — DTT cascade

Real-property income is allocated to the *situs* country under OECD MTC Art. 6 — but BOTH countries can typically tax (Art. 24 Methods).

- **Exemption method (with progression)** — home country exempts the foreign-source RE income, but uses it to bracket-up domestic income. Common in DE / AT / FR / CH. Effect: foreign-source income is "free" but pushes domestic into a higher band.
- **Credit method** — home country taxes worldwide, gives credit for foreign tax paid (capped at home tax on that foreign income). Common in US / UK / CA / AU / JP / IN.

**Practitioner consequence**: a German resident's French rental is exempt-with-progression in DE → effective rate hits domestic income harder. A US resident's French rental is fully taxable in US with FTC → if French tax > US tax on that income, the excess credit carries forward 10 years or back 1 year (limited use).

Verify each treaty's Art. 24 method before assuming. Note: the German Anrechnungsmethode applied to ES rental (DE-ES DTT 2013) is a CREDIT regime — not the exemption-with-progression that applies to most other DE-EU treaties. One-treaty-at-a-time.

### Common Reporting Standard (CRS) visibility

100+ jurisdictions auto-exchange financial-account data annually under the OECD CRS. A bank account at the property-country bank → home tax authority sees it within ~12 months.

- Property *ownership* itself is NOT directly reported via CRS (CRS is account-based, not asset-based) — BUT rental escrow, utility deposits, mortgage payments, notarial trust accounts all leave a CRS-reportable fingerprint.
- Some countries share property-registry data via DTT MLI bilateral exchanges (GR / IT / PT / ES catastros increasingly cross-referenced).
- **Voluntary-disclosure programs** (US Streamlined / IRS Voluntary Disclosure Practice; IN BMA Compliance Window when re-opened; ZA Special Voluntary Disclosure Programme) are the safest path for past non-disclosure — penalties dramatically lower than discovery-driven enforcement.

### Pillar Two GMT for HNW + family-office structures

The OECD Pillar Two **15% global minimum tax** went live **1 Jan 2024** in the EU, UK, AU (IIR), CA, JP, KR. Threshold: MNE groups with consolidated revenue ≥ €750M in 2 of 4 prior years.

- US: announced (Jan 2026) that US-headquartered companies will be **exempt** from Pillar Two — political settlement in flux; verify quarterly.
- Family offices generally below the €750M threshold but some single-family offices with extensive RE portfolios have crossed it.
- Affects **structured ownership**, not direct individual ownership.

### Foreign currency reporting baskets (US Form 1116)

For US holders, the foreign tax credit is computed on **separate Form 1116 per income basket** ([IRS Form 1116 instructions 2025](https://www.irs.gov/instructions/i1116)):

1. Passive category income
2. General category income
3. Section 951A (GILTI)
4. Foreign branch
5. Section 901(j) (sanctioned)
6. Treaty-resourced specific income
7. Lump-sum distributions

**Foreign rental** = passive (default). **Cross-basket loss not allowed.** The HTKO ("high-tax kick-out") election kicks passive income taxed at > 37% by foreign country into the *general* basket — useful when the foreign country's effective rate exceeds US top rate, allowing better cross-basket utilisation. ([Golding Lawyers HTKO](https://www.goldinglawyers.com/high-tax-kick-out-htko-irs-reduction-in-the-foreign-tax-credit/))

This matters for high-tax jurisdictions (FR, DE, NL, BE, JP) where the foreign rental tax often exceeds US rates → HTKO can save 10-15% on the FTC limitation.

---

## Universal mitigations (apply across all home jurisdictions)

These work regardless of buyer's home country and prevent the most common cross-border tax pitfalls:

1. **Get tax advice in BOTH jurisdictions before signing** — buyer's-side and property-side. The buyer's home-country accountant rarely knows IVIE / Modelo 720 / Schedule FA / Quadro RW filings; the property-country notary rarely knows § 988 / FBAR / T1135. The DTT applies BETWEEN them but neither side automatically computes it.
2. **Voluntary-disclosure pre-CRS-discovery is the safest catch-up path** — US Streamlined / VDP, UK Worldwide Disclosure Facility, IN Black Money Compliance Window when open, IT ravvedimento operoso, ES regularización extraordinaria, BR DERCAT. Penalties on volunteer disclosure are dramatically lower than discovery-driven enforcement (typically 10-25% vs. 50-300% with criminal exposure).
3. **Verify treaty Article 24 method before assuming relief mechanic** — the German Anrechnungsmethode for Spanish rental (DE-ES DTT 2013) is a CREDIT regime; most other DE-EU treaties are Freistellung-mit-Progressionsvorbehalt. Mistaking one for the other inverts the bracket math. Always pull the actual treaty text + protocols at [oecd.org tax conventions](https://www.oecd.org/tax/treaties/) or each tax authority's bilateral page.
4. **Pre-departure tax planning windows close fast** — US covered-expatriate Form 8854; CA T1243 + T1244 within 90 days; AU CGT event I1 election within 12 months; ZA § 9H clearance before fund repatriation. Plan emigration timing around the home-country exit-tax event, not just the visa date.
5. **Document FX rates at every transaction date** — for buyers from US (§ 988), AU (Div 775), CA (§ 39(2)), JP (§ 57-3) the FX-translation rule requires per-transaction conversion. Save the bank's FX rate confirmation, the central-bank reference rate (BoC, ATO published, IRS yearly average), and the actual amount transferred. Reconstructing 5 years later is painful and audit-vulnerable.
6. **Don't bypass the foreign-asset disclosure form even when no income is earned** — Modelo 720 (ES), Quadro RW (IT), T1135 (CA), Form 8938 + FBAR (US), Schedule FA (IN) all require declaration of HOLDING the asset, not just income from it. The penalty cascade for non-disclosure independently of any tax owed can dwarf the tax itself.
7. **Avoid foreign collective-investment vehicles for US holders without PFIC analysis** — SOCIMIs, SCPIs, Offene Immobilienfonds, UK REITs are generally PFICs. Even when sold by a US-bank's foreign branch with apparent US compatibility, the underlying vehicle is subject to § 1291. Direct property ownership avoids the entire PFIC regime.

---

## Cross-country quick reference

| Topic | US | UK | DE | FR | IT | ES | NL | NO | DK | AU | CA |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Worldwide income | ✅ citizenship-based | ✅ post-FIG year 4 | ✅ § 1 EStG | ✅ Art. 4 B CGI | ✅ Art. 3 TUIR | ✅ Art. 2 LIRPF | ✅ Art. 2.1 IB 2001 | ✅ § 2-1 | ✅ KSL § 1 | ✅ § 6-5 ITAA | ✅ § 2 ITA |
| Annual on foreign RE | ❌ (federal) | ❌ | ❌ (1997) | **IFI** > €1.3M | **IVIE** 1.06% | **IP + ITSGF** | **Box 3** 6.04% RE | **Formueskatt** | **EVS** 0.51-1.4% | ❌ | ❌ |
| Foreign-asset disclosure | **8938 + FBAR** | None comprehensive (CRS) | None for direct RE | **Form 3916** (accounts) | **Quadro RW** (everything) | **Modelo 720** | None comprehensive | None comprehensive | Item 20 | **T1135** > CAD 100k (rental) |
| CGT on foreign disposal | LTCG 0/15/20% + NIIT 3.8% | 18%/24% (post-Oct 2024) | § 23 EStG, 10y exempt | 22y IR / 30y soc. abated | 5y exempt | 19-30% (2025) | None for individuals | 22% | EBL § 1 | 50% inclusion |
| Exit tax foreign RE | YES (§ 877A) | NO (FIG regime exit) | NO | NO | NO | NO | NO | NO | NO | YES (§ 128.1) | YES (CGT event I1) |
| Inheritance worldwide | YES ($15M from 2026) | YES (LTR 10/20) | YES (decedent OR heir) | YES (decedent OR 6/10y heir) | YES (decedent) | YES (heir-resident) | YES + 10y emigrant | NO (abolished 2014) | YES (decedent) | NO (1979) | NO (deemed disposition § 70(5)) |
| Special inbound regime | None | **FIG** 4y | None (post-2009) | None standalone | **24-bis** €200k / **24-ter** 7% | **Beckham** 24% | **30%-ruling** → 27% from 2027 | None | None | None | None |

---

## Honest uncertainties (read before relying)

- **CN inheritance tax** — proposed 2010, never enacted. Treat any "China inheritance tax 20%" claim as fabrication unless dated to a post-NPC enactment.
- **IL Olim status (returning resident exemption)** — 10-year foreign-source exemption under § 14 ITO; the 2026 Knesset reform package proposed narrowing it; current status fluid as of May 2026 — verify with Israel Tax Authority before relying.
- **BR EC 132/2023 ITCMD harmonisation** — PLP 108/2024 + LC 227/2026 are still being implemented state-by-state through 2026; foreign-asset taxation rules vary by state until federal harmonisation completes.
- **US TCJA estate-exemption sunset 1 Jan 2026** — was scheduled to halve; OBBBA (4 Jul 2025) made it permanent at $15M (2026 base, indexed from 2025). Confirm current IRS IRB before estate-planning advice.
- **Saudi individual passive foreign-property rental** — ZATCA's individual-side guidance under-documented; treat as MEDIUM confidence.
- **OM individual income tax** — proposed for 2024 introduction, repeatedly deferred; unconfirmed as of May 2026.
- **CA UHT elimination** — Bill C-15 tabled 18 Nov 2025 proposes elimination 2025+; Royal Assent timing pending.
- **AU residency reform 2021 proposal** — not enacted as of May 2026; treat current 4-test framework as authoritative.
- **NL Wet WRBox3 actual-return** — bill in First Chamber as of date stamp; effective date 1 Jan 2028 not yet locked.
- **FR exit-tax PLF 2026** — National Assembly amendment proposes restoring 15-y holding period; awaiting parliamentary navette completion.

---

## Status

**Confidence (overall)**: HIGH for the cited statutes and primary forms across all 20+ buyer cohorts; MEDIUM for items in active 2026 reform (NL Wet WRBox3 effective date · FR exit-tax PLF 2026 · IT 24-bis €300k PLF 2026 · KR 2028 Inheritance Acquisition System · CA UHT elimination · IL 10y olim survival · CH Eigenmietwert pre-2029 transition); LOW flagged inline (SA individual passive RE · OM PIT timing · § 988 personal-use treatment).

**Last verified**: 2026-05-09.

**Re-verify cadence**: every 6 months — these jurisdictions all have annual finance laws that move thresholds and rates. NL Box 3, FR exit tax, IL Olim reform, KR inheritance reform, US OBBBA technical corrections, and IT 24-bis PLF 2026 should be re-checked **after each parliamentary milestone**, not just on the 6-month timer.

**Re-stamp triggers (calendar-actionable)**:
- 2026-Q4: HMRC FIG-regime manual stabilisation target.
- 2026-12-31: NL Wet WRBox3 First-Chamber adoption deadline for 2028 effective date.
- 2027-01-01: NL 30%-ruling flat 27% goes live.
- 2028: KR Inheritance Acquisition System target.
- 2029-01-01: CH Eigenmietwert abolished.
- Annual: US Rev. Proc. inflation adjustments (§ 877A, § 988(e), FBAR civil penalty table); state estate-tax legislative changes; CA Budget UHT.

## Authority URLs

- **US IRS**: https://www.irs.gov · [§ 7701(b)](https://www.law.cornell.edu/uscode/text/26/7701) · [§ 988](https://www.law.cornell.edu/uscode/text/26/988) · [§ 877A](https://www.law.cornell.edu/uscode/text/26/877A) · [§ 1297](https://www.law.cornell.edu/uscode/text/26/1297) · [§ 6038D](https://www.law.cornell.edu/uscode/text/26/6038D) · [Form 8938](https://www.irs.gov/forms-pubs/about-form-8938) · [FinCEN 114](https://bsaefiling.fincen.treas.gov/) · [Estate-tax treaties](https://www.irs.gov/businesses/small-businesses-self-employed/estate-gift-tax-treaties-international)
- **UK HMRC**: https://www.gov.uk/government/organisations/hm-revenue-customs · [SRT Sch 45 FA 2013](https://www.legislation.gov.uk/ukpga/2013/29/schedule/45) · [RFIG41000 FIG](https://www.gov.uk/hmrc-internal-manuals/residence-and-fig-regime-manual/rfig41000) · [IHTM47020 LTR](https://www.gov.uk/hmrc-internal-manuals/inheritance-tax-manual/ihtm47020) · [PIM4702 overseas rent](https://www.gov.uk/hmrc-internal-manuals/property-income-manual/pim4702)
- **CA CRA**: https://canada.ca/cra · [T1135](https://www.canada.ca/en/revenue-agency/services/forms-publications/forms/t1135.html) · [§ 128.1 ITA](https://laws-lois.justice.gc.ca/eng/acts/I-3.3/section-128.1.html) · [Folio S1-F3-C2 PR](https://www.canada.ca/en/revenue-agency/services/tax/technical-information/income-tax/income-tax-folios-index/series-1-individuals/folio-3-family-unit-issues/income-tax-folio-s1-f3-c2-principal-residence.html)
- **AU ATO**: https://www.ato.gov.au · [FRCGW](https://www.ato.gov.au/individuals-and-families/investments-and-assets/capital-gains-tax/foreign-residents-and-capital-gains-tax/foreign-resident-capital-gains-withholding/foreign-resident-capital-gains-withholding-overview) · [Worldwide income](https://www.ato.gov.au/individuals-and-families/income-deductions-offsets-and-records/income-you-must-declare/foreign-and-worldwide-income/australian-resident-foreign-and-worldwide-income)
- **NZ IRD**: https://www.ird.govt.nz · [Bright-line](https://www.ird.govt.nz/property/buying-and-selling/when-you-need-to-pay/the-brightline-test) · [Property interest rules](https://www.ird.govt.nz/property-interest-rules)
- **DE BMF**: https://www.bundesfinanzministerium.de · gesetze-im-internet.de/ao · /estg · /astg · /erbstg · BZSt § 138: https://www.bzst.de/DE/Unternehmen/EUInternational/ErfassungAuslandsbeteiligungen/Mitteilungspflicht_138_Abs_2_AO/
- **FR DGFiP**: https://www.impots.gouv.fr · BOFIP: https://bofip.impots.gouv.fr · Légifrance CGI: https://www.legifrance.gouv.fr/codes/texte_lc/LEGITEXT000006069577/
- **IT Agenzia Entrate**: https://www.agenziaentrate.gov.it · IVIE scheda: https://www.agenziaentrate.gov.it/portale/schede/pagamenti/imposta-sul-valore-degli-immobili-estero-ivie/base-imponibile-e-aliquota-scheda-ivie · Circolare 20/E del 4 nov 2024: https://www.agenziaentrate.gov.it/portale/documents/20143/6519685/circolare+n.+20+de+4+novembre+2024+residenza+pdf.pdf
- **ES AEAT**: https://sede.agenciatributaria.gob.es · M720: https://sede.agenciatributaria.gob.es/Sede/procedimientoini/GI34.shtml · ITSGF: https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/impuesto-temporal-solidaridad-grandes-fortunas_.html
- **NL Belastingdienst**: https://www.belastingdienst.nl · Box 3 2026: https://www.belastingdienst.nl/wps/wcm/connect/nl/box-3/content/berekening-box-3-inkomen-2026 · Rijksoverheid Wet WRBox3 timeline: https://www.rijksoverheid.nl/onderwerpen/inkomstenbelasting/plannen-werkelijk-rendement-box-3/tijdlijn-werkelijk-rendement-box-3 · Hoge Raad 6 Jun 2024: https://www.hogeraad.nl/actueel/nieuwsoverzicht/2024/december/hoge-raad-bepaling-werkelijke-rendement-box-3-voordeel-wegens-eigen/
- **SE Skatteverket**: https://www.skatteverket.se · **NO Skatteetaten**: https://www.skatteetaten.no · **DK Skat**: https://skat.dk · **FI Vero**: https://www.vero.fi
- **CH ESTV**: https://www.estv.admin.ch · admin.ch federal decree: https://www.admin.ch/gov/en/start/documentation/votes/20250928/federal-decree-on-cantonal-property-taxes-on-second-homes.html
- **JP NTA**: https://www.nta.go.jp · **KR NTS**: https://www.nts.go.kr · **SG IRAS**: https://www.iras.gov.sg · **HK IRD**: https://www.ird.gov.hk · **CN STA**: https://www.chinatax.gov.cn
- **IL Israel Tax Authority**: https://www.gov.il/he/departments/israel_tax_authority
- **IN Income Tax**: https://incometaxindia.gov.in · BMA: https://www.indiacode.nic.in/handle/123456789/2147 · CBDT Circular 10/2023: https://incometaxindia.gov.in/communications/circular/circular-10-2023.pdf
- **BR Receita Federal**: https://www.gov.br/receitafederal · Planalto L14754: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14754.htm
- **MX SAT**: https://www.sat.gob.mx · **ZA SARS**: https://www.sars.gov.za · **AE FTA**: https://tax.gov.ae · **SA ZATCA**: https://zatca.gov.sa
