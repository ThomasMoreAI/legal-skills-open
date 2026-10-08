# Universal `--macro` Section

Macroeconomic context for property decisions: inflation, GDP growth, central-bank policy rate, sovereign yield. Sets the cyclical backdrop for `--price`, `--finance`, and `--currency`.

**Snapshot**: May 2026 (Tier-5 additions).

## Universal contract

For the property's country, return:
1. **CPI inflation** (latest YoY)
2. **GDP growth** (latest YoY real)
3. **Central-bank policy rate** (current)
4. **10-yr sovereign yield**
5. **Eurostat HICP / IMF WEO cross-reference**
6. **Cyclical phase**: expansion / late-cycle / contraction / recovery
7. **Confidence**: HIGH / MEDIUM / LOW

## Output template

```markdown
## Macro Profile

**Country**: <ISO2>
**CPI inflation (latest YoY)**: <%>
**GDP growth (latest YoY real)**: <%>
**Central-bank policy rate**: <%>
**10-yr sovereign yield**: <%>
**Cyclical phase**: <expansion | late-cycle | contraction | recovery>
**Sources**: <central bank + statistics office URLs>
**Confidence**: <HIGH/MEDIUM/LOW>
```

---

## Authoritative source registry

For each country, primary macro sources:

| Country | Central bank | Statistics office | Eurostat / OECD / IMF |
|---|---|---|---|
| FR | BdF (https://www.banque-france.fr/) | INSEE | Eurostat HICP |
| IT | BdI (https://www.bancaditalia.it/) | ISTAT | Eurostat HICP |
| ES | BdE (https://www.bde.es/) | INE | Eurostat HICP |
| PT | BdP (https://www.bportugal.pt/) | INE | Eurostat HICP |
| DE | Bundesbank (https://www.bundesbank.de/) | Destatis | Eurostat HICP |
| AT | OeNB (https://www.oenb.at/) | Statistik Austria | Eurostat HICP |
| CH | SNB (https://www.snb.ch/) | BFS | OECD |
| NL | DNB (https://www.dnb.nl/) | CBS | Eurostat HICP |
| BE | NBB (https://www.nbb.be/) | STATBEL | Eurostat HICP |
| LU | BCL (https://www.bcl.lu/) | STATEC | Eurostat HICP |
| IE | CBI (https://www.centralbank.ie/) | CSO | Eurostat HICP |
| UK | BoE (https://www.bankofengland.co.uk/) | ONS | OECD |
| GR | BdGr (https://www.bankofgreece.gr/) | ELSTAT | Eurostat HICP |
| MT | CBM (https://www.centralbankmalta.org/) | NSO | Eurostat HICP |
| CY | CBC (https://www.centralbank.cy/) | CyStat | Eurostat HICP |
| FI | SP (https://www.suomenpankki.fi/) | Tilastokeskus | Eurostat HICP |
| SE | Riksbank (https://www.riksbank.se/) | SCB | Eurostat HICP |
| NO | NB (https://www.norges-bank.no/) | SSB | OECD |
| DK | DN (https://www.nationalbanken.dk/) | DST | Eurostat HICP |
| IS | CBI (https://www.cb.is/) | Hagstofa | OECD |
| SI | BS (https://www.bsi.si/) | SURS | Eurostat HICP |
| PL | NBP (https://nbp.pl/) | GUS | Eurostat HICP |
| EE | EP (https://www.eestipank.ee/) | StatEE | Eurostat HICP |
| LV | LB (https://www.bank.lv/) | CSP | Eurostat HICP |
| LT | LB (https://www.lb.lt/) | OSP | Eurostat HICP |
| HR | HNB (https://www.hnb.hr/) | DZS | Eurostat HICP |
| HU | MNB (https://www.mnb.hu/) | KSH | Eurostat HICP |
| CZ | ČNB (https://www.cnb.cz/) | ČSÚ | Eurostat HICP |
| SK | NBS (https://www.nbs.sk/) | ŠÚ SR | Eurostat HICP |
| RO | BNR (https://www.bnr.ro/) | INS | Eurostat HICP |
| BG | BNB (https://www.bnb.bg/) | NSI | Eurostat HICP |
| RS | NBS (https://www.nbs.rs/) | RZS | IMF WEO |
| ME | CBCG (https://www.cbcg.me/) | MONSTAT | IMF WEO |
| BA | CBBH (https://www.cbbh.ba/) | BHAS | IMF WEO |
| MK | NBRSM (https://www.nbrm.mk/) | MAKSTAT | IMF WEO |
| AL | BoA (https://www.bankofalbania.org/) | INSTAT | IMF WEO |
| CA | BoC (https://www.bankofcanada.ca/) | StatCan | OECD |
| AU | RBA (https://www.rba.gov.au/) | ABS | OECD |
| NZ | RBNZ (https://www.rbnz.govt.nz/) | StatsNZ | OECD |
| MX | Banxico (https://www.banxico.org.mx/) | INEGI | OECD |
| BR | BCB (https://www.bcb.gov.br/) | IBGE | IMF WEO |
| AR | BCRA (https://www.bcra.gob.ar/) | INDEC | IMF WEO |
| CR | BCCR (https://www.bccr.fi.cr/) | INEC | IMF WEO |
| PA | INEC (https://www.inec.gob.pa/) | INEC | IMF WEO |
| US | Federal Reserve (https://www.federalreserve.gov/) | BLS / BEA | OECD |
| TR | TCMB (https://www.tcmb.gov.tr/) | TÜİK | IMF WEO |
| AE | CBUAE (https://www.centralbank.ae/) | FCSC | IMF WEO |
| JP | BoJ (https://www.boj.or.jp/) | e-Stat / MIC | OECD |
| TH | BoT (https://www.bot.or.th/) | NSO / NESDC | IMF WEO |
| DO | BCRD (https://www.bancentral.gov.do/) | ONE | IMF WEO |
| CO | BanRep (https://www.banrep.gov.co/) | DANE | IMF WEO |
| UY | BCU (https://www.bcu.gub.uy/) | INE | IMF WEO |
| CL | BCCh (https://www.bcentral.cl/) | INE | OECD |
| ZA | SARB (https://www.resbank.co.za/) | StatsSA | IMF WEO |
| GE | NBG (https://www.nbg.gov.ge/) | GeoStat | IMF WEO |
| ID | BI (https://www.bi.go.id/) | BPS | IMF WEO |
| MY | BNM (https://www.bnm.gov.my/) | DOSM | IMF WEO |
| VN | SBV (https://www.sbv.gov.vn/) | GSO | IMF WEO |
| PH | BSP (https://www.bsp.gov.ph/) | PSA | IMF WEO |
| IL | BoI (https://www.boi.org.il/) | CBS | OECD |
| MA | BAM (https://www.bkam.ma/) | HCP | IMF WEO |
| EG | CBE (https://www.cbe.org.eg/) | CAPMAS | IMF WEO |
| SG | MAS (https://www.mas.gov.sg/) | Singstat | OECD |
| HK | HKMA (https://www.hkma.gov.hk/) | C&SD | IMF WEO |
| KR | BOK (https://www.bok.or.kr/) | KOSTAT | OECD |
| TW | CBC (https://www.cbc.gov.tw/) | DGBAS | IMF WEO |
| LI | SNB (https://www.snb.ch/) — CHF via 1980 Currency Treaty | Statistik Liechtenstein | OECD |
| MO | AMCM (https://www.amcm.gov.mo/) | DSEC | IMF WEO |
| AD | n/a (EUR via 2011 Monetary Treaty, not Eurozone) | Estadística d'Andorra | IMF WEO |
| MC | n/a (EUR via 2002 Monetary Convention with FR, not Eurozone formally) | IMSEE | IMF WEO |
| MD | BNM (https://www.bnm.md/) | BNS | IMF WEO |
| QA | QCB (https://www.qcb.gov.qa/) | PSA Planning & Statistics Authority | IMF WEO |
| SA | SAMA (https://www.sama.gov.sa/) | GASTAT | IMF WEO |
| PE | BCRP (https://www.bcrp.gob.pe/) | INEI | IMF WEO |
| EC | BCE (https://www.bce.fin.ec/) | INEC | IMF WEO |
| PY | BCP (https://www.bcp.gov.py/) | INE | IMF WEO |
| AM | CBA (https://www.cba.am/) | ARMSTAT | IMF WEO |
| AZ | CBAR (https://www.cbar.az/) | SSC | IMF WEO |
| TN | BCT (https://www.bct.gov.tn/) | INS | IMF WEO |
| IN | RBI (https://www.rbi.org.in/) | NSO / MoSPI | IMF WEO |
| NG | CBN (https://www.cbn.gov.ng/) | NBS | IMF WEO |
| KE | CBK (https://www.centralbank.go.ke/) | KNBS | IMF WEO |
| JO | CBJ (https://www.cbj.gov.jo/) | DOS | IMF WEO |
| OM | CBO (https://cbo.gov.om/) | NCSI | IMF WEO |
| BH | CBB (https://www.cbb.gov.bh/) | iGA | IMF WEO |
| KW | CBK (https://www.cbk.gov.kw/) | CSB | IMF WEO |
| LB | BDL (https://www.bdl.gov.lb/) | CAS | IMF WEO |

## Apr 2026 snapshot — central-bank policy rates

| Country / region | Rate | Direction |
|---|---|---|
| **ECB Deposit Rate** | 2.50% | hold (post-2024 cuts paused on Iran energy shock) |
| **BoE Bank Rate** | 3.75% | hold (since Dec 2025) |
| **SNB Policy Rate** | 0.00% | held; CHF safe-haven appreciation 2024-26 |
| **Riksbank** | 1.75% | paused after Sep 2025 cut |
| **Norges Bank** | 4.00% | hold |
| **DNB** (DK) | 3.10% (effective via FX peg) | hold |
| **CBI Iceland** | 7.50% | gradually cutting |
| **CNB Czech** | 3.25% | held |
| **NBP Poland** | 4.50% | held; FX-loan legacy concerns |
| **MNB Hungary** | 6.50% | hold (HUF volatility-management) |
| **NBS Slovakia** | ECB-bound | ECB Deposit |
| **BNR Romania** | 6.50% | hold (RON managed float) |
| **BNB Bulgaria** | ECB-bound (since 1 Jan 2026) | ECB Deposit |
| **HNB Croatia** | ECB-bound (since 1 Jan 2023) | ECB Deposit |
| **NBS Serbia** | 5.50% | hold |
| **CBCG Montenegro** | n/a (EUR unilateral) | ECB Deposit indirect |
| **CBBH Bosnia** | n/a (currency board) | ECB Deposit indirect |
| **NBRSM N. Macedonia** | 5.50% | hold |
| **BoA Albania** | 2.75% | hold |
| **BoC Canada** | 2.75% | held; review 2026 considering AU-style FIRB post-2027 |
| **RBA Australia** | 4.10% | gradually cutting |
| **RBNZ NZ** | 3.50% | gradually cutting |
| **Banxico** | 7.00% | post-300bps-cut-in-2025; pausing |
| **BCB Brazil** | **14.75%** | cuts paused on Iran energy shock Mar 2026 |
| **BCRA Argentina** | n/a (volatile post-Milei) | currency-band managed; effective lending rates 25-38% UVA |
| **BCCR Costa Rica** | 3.50% | held |
| **PA (USD-dollarized)** | follows Fed Funds 4.25-4.50% | Fed-bound |
| **Fed Funds (US)** | 4.25-4.50% | hold (Fed paused after 2024 cuts; Q1 2026 print pending — verify FOMC) |
| **TCMB (Turkey)** | 37.00% | set 23 Jan 2026, held through PPK 10 Sep 2026 (TCMB 2026-38); eased from 50% Mar-2024 peak — verify against latest TCMB MPC |
| **CBUAE (UAE)** | ~4.40% (EIBOR-aligned) | Fed-bound via AED/USD peg 3.6725 |
| **BoJ (Japan)** | 1.25% | 0.50% (Jan 2025) → 0.75% (Dec 2025) → 1.0% (16 Jun 2026) → 1.25% (18 Sep 2026, effective 24 Sep 2026; 2026 data, source BoJ MPM k260918a); first hike cycle since 2007 — next MPM 29-30 Oct 2026 |
| **BoT (Thailand)** | 2.50% | hold; cut path debated as THB strengthens |
| **BCRD (DR)** | 6.00% est. | gradual easing; verify latest BCRD comunicado |
| **BanRep (Colombia)** | ~9.00% est. | mid-cycle cuts from 13.25% peak (Dec 2023) — verify |
| **BCU (Uruguay)** | 8.50% est. | hold; TPM in restrictive territory — verify |
| **BCCh (Chile)** | ~4.50% est. | cut cycle from 11.25% (Oct 2023) — verify against next IPoM |
| **SARB (South Africa)** | 7.50% est. | gradual cuts since 2024 — verify next MPC |
| **NBG (Georgia)** | 8.25% (2026 data, source NBG MPC 9 Sep 2026) | hold after +0.25pp hike 6 May 2026; Aug 2026 CPI 5.6% vs 3% target |
| **BI (Indonesia)** | 6.00% est. | BI-Rate; FX-defence stance — verify |
| **BNM (Malaysia)** | 3.00% (OPR) | held; CPI low — verify next MPC |
| **SBV (Vietnam)** | 4.50% (refi) est. | accommodative; managed VND — verify |
| **BSP (Philippines)** | 5.75% est. | cut path from 6.50% peak — verify |
| **BoI (Israel)** | 4.50% est. | war-affected; cautious cuts — verify |
| **BAM (Morocco)** | 2.50% est. | hold; CPI near target — verify |
| **CBE (Egypt)** | ~22-24% est. | held high post-Mar 2024 IMF devaluation; CPI declining from 30%+ — verify |
| **MAS (Singapore)** | n/a (FX-based policy via S$NEER managed float) | macroprudential via SSD/ABSD/LTV; no policy rate — verify next MAS MPS https://www.mas.gov.sg |
| **HKMA (Hong Kong)** | Base Rate ~4.75% est. (Fed-bound via LERS Convertibility Undertaking 7.75-7.85) | Fed-tracking; no independent policy rate — verify https://www.hkma.gov.hk |
| **BOK (Korea)** | 2.75% est. | gradual cuts from 3.50% peak (2023) — verify next BOK MPC https://www.bok.or.kr |
| **CBC (Taiwan)** | 2.00% est. (Discount Rate) | hold; macroprudential focus — verify https://www.cbc.gov.tw |
| **SNB (Liechtenstein)** | 0.00% (CHF-bound via 1980 Currency Treaty) | SNB-bound; no independent monetary policy |
| **AMCM (Macao)** | Base Rate ~4.75% est. (HKD-bound via MOP/HKD peg + LERS indirect Fed-bound) | Fed-tracking via double peg — verify https://www.amcm.gov.mo |
| **n/a (Andorra)** | EUR-using (2011 Monetary Treaty); no central bank | ECB Deposit indirect |
| **n/a (Monaco)** | EUR-using (2002 Monetary Convention with FR); no central bank | ECB Deposit indirect |
| **BNM (Moldova)** | 6.50% est. | hold/easing trajectory post-2022 inflation peak — verify next BNM MPC https://www.bnm.md |
| **QCB (Qatar)** | ~5.00% est. (QCB Lending Rate) | Fed-bound via QAR/USD peg 3.64 since 2001 — verify https://www.qcb.gov.qa |
| **SAMA (Saudi Arabia)** | ~5.50% est. (SAMA Repo) | Fed-bound via SAR/USD peg 3.75 since 1986 — verify https://www.sama.gov.sa |
| **BCRP (Peru)** | ~4.50% est. | mid-cycle cuts from 7.75% peak (2023) — verify https://www.bcrp.gob.pe |
| **BCE (Ecuador)** | n/a (USD adopted Sep 2000) | Fed-bound; no monetary independence — verify https://www.bce.fin.ec |
| **BCP (Paraguay)** | ~6.00% est. | hold; CPI ~4% Q1 2026 — verify https://www.bcp.gov.py |
| **CBA (Armenia)** | ~7.00% est. | gradual cuts as CPI near target — verify https://www.cba.am |
| **CBAR (Azerbaijan)** | ~7.25% est. (Refinancing Rate) | hold; AZN de-facto pegged USD 1.70 since 2017 — verify https://www.cbar.az |
| **BCT (Tunisia)** | 8.00% est. | hold; CPI ~7-8% post-2022-23 shock; IMF EFF SUSPENDED Mar 2024 — verify https://www.bct.gov.tn |
| **RBI (India)** | ~6.00% est. (Repo) | mid-cycle cuts from 6.50% peak; INR managed-float; FEMA + LRS USD 250k/yr cap — verify https://www.rbi.org.in |
| **CBN (Nigeria)** | ~27.50% est. (MPR) | hold/easing post-NGN unification Jun 2023; CPI 30%+ — verify https://www.cbn.gov.ng |
| **CBK (Kenya)** | ~10.75% est. (CBR) | gradual cuts as CPI eased to 6-7% — verify https://www.centralbank.go.ke |
| **CBJ (Jordan)** | ~6.50% est. | Fed-bound via JOD/USD peg 0.7080 since 1995 — verify https://www.cbj.gov.jo |
| **CBO (Oman)** | ~5.50% est. | Fed-bound via OMR/USD peg 0.385 since 1986 — verify https://cbo.gov.om |
| **CBB (Bahrain)** | ~6.00% est. (1-week deposit) | Fed-bound via BHD/USD peg 0.376 since 2001 — verify https://www.cbb.gov.bh |
| **CBK (Kuwait)** | ~4.25% est. (Discount Rate) | basket-managed since 20 May 2007 (was USD-pegged); KWD ≈ USD 3.25 (highest face-value globally) — verify https://www.cbk.gov.kw |
| **BDL (Lebanon)** | n/a (multiple rates post-2019 collapse) | LBP unified 2023-24 around USD 89,500-90,000 (was 1,507.5 since 1997 → decoupled Sep 2019); de-facto USD-dollarized 80%+ prime — verify https://www.bdl.gov.lb |

## Apr 2026 snapshot — sovereign 10-yr yields

Approximate (verify on FRED / Refinitiv / each central bank's website):

| Country | 10-yr yield | Spread vs Bund |
|---|---|---|
| DE | 2.40% | benchmark |
| FR | 2.85% | +45 bps |
| IT | 3.30% | +90 bps |
| ES | 3.05% | +65 bps |
| PT | 2.80% | +40 bps |
| GR | 3.15% | +75 bps |
| AT | 2.55% | +15 bps |
| NL | 2.50% | +10 bps |
| BE | 2.70% | +30 bps |
| IE | 2.65% | +25 bps |
| FI | 2.60% | +20 bps |
| CY | 3.10% | +70 bps |
| MT | 2.90% | +50 bps |
| LU | 2.45% | +5 bps |
| SK | 3.20% | +80 bps |
| SI | 2.90% | +50 bps |
| EE | 3.40% | +100 bps |
| LV | 3.50% | +110 bps |
| LT | 3.30% | +90 bps |
| HR | 3.00% | +60 bps |
| HU | 6.20% | (HUF) — non-eurozone |
| PL | 5.40% | (PLN) |
| RO | 7.50% | (RON) |
| CZ | 4.10% | (CZK) |
| SE | 2.55% | (SEK) |
| NO | 4.20% | (NOK) |
| DK | 2.70% | (DKK ERM-II) |
| IS | 7.00% | (ISK) |
| CH | 0.50% | safe-haven |
| UK | 4.20% | (GBP) |
| BG | 3.00% | (eurozone since 2026) |
| RS | 5.00% | (RSD) |
| ME | 4.50% | (EUR-effective) |
| BA | 3.50% | (BAM-currency-board) |
| MK | 5.00% | (MKD) |
| AL | 5.50% | (ALL) |
| CA | 3.50% | (CAD) |
| AU | 4.30% | (AUD) |
| NZ | 4.10% | (NZD) |
| US | 4.30% | (USD) |
| MX | 9.50% | (MXN) |
| BR | 14.20% | (BRL) — Selic-driven |
| AR | 30%+ | (ARS) — UVA-indexed |
| CR | 7.50% | (CRC) |
| PA | 4.30% | (USD-dollarized) |
| US | 4.30% est. | (USD) — benchmark for emerging-market USD-equivalent yields |
| TR | ~28-32% est. (TRY) / USD eurobond ~7.5% | TRY yield reflects hyperinflation; USD eurobond is the cleaner foreign-buyer reference — verify Hazine + ICE BofA |
| AE | ~4.40% (USD-linked) | AED pegged; sovereign USD eurobonds track UST + ~50-100 bps |
| JP | 1.50% est. | (JPY) — BoJ YCC fully unwound; verify MoF/JGB market |
| TH | 2.50% est. | (THB) |
| DO | 11.0% est. | (DOP); USD eurobonds ~7-8% — verify |
| CO | 11.5% est. | (COP); USD eurobonds ~7-8% |
| UY | 8.50% est. | (UYU); USD eurobonds ~6-7% (IG-rated) |
| CL | 5.80% est. | (CLP); USD eurobonds ~5-6% |
| ZA | 10.50% est. | (ZAR); R2032 generic — verify JSE |
| GE | 8.50% est. | (GEL); USD eurobonds ~7% |
| ID | 7.00% est. | (IDR); USD eurobonds ~5-5.5% |
| MY | 3.90% est. | (MYR); IG-rated |
| VN | 3.00% est. | (VND); USD eurobonds ~5-6% |
| PH | 6.30% est. | (PHP); USD eurobonds ~5-5.5% |
| IL | 4.80% est. | (ILS); war-risk premium ~50 bps over pre-Oct-2023 — verify |
| MA | 4.50% est. | (MAD); IG-rated; USD eurobonds ~5% |
| EG | ~25% est. | (EGP); USD eurobonds ~9-11% — distressed; verify post-IMF |
| SG | 2.80% est. | (SGD) — AAA-rated; SGS 10y benchmark |
| HK | 4.50% est. | (HKD-USD peg) — tracks UST + ~10-20 bps |
| KR | 3.20% est. | (KRW) — KTB 10y; AA-rated |
| TW | 1.60% est. | (TWD) — central-government bond; AA-rated |
| LI | n/a | (CHF via Currency Treaty) — no domestic sovereign issuance; AAA-rated |
| MO | 4.50% est. | (MOP-HKD-USD double peg) — tracks UST |
| AD | 3.00% est. | (EUR-using) — limited sovereign issuance via Treasury |
| MC | n/a | (EUR-using) — no domestic sovereign issuance |
| MD | ~9% est. | (MDL) — high inflation/FX risk premium; B-rated; USD eurobonds ~7-8% |
| QA | ~4.40% est. | (QAR pegged USD) — USD eurobonds tracking UST + ~30-50 bps; AA-rated |
| SA | ~4.80% est. | (SAR pegged USD) — USD eurobonds tracking UST + ~50-80 bps; A-rated |
| PE | ~6.50% est. | (PEN); USD eurobonds ~5-6%; BBB-rated |
| EC | ~9.00% est. | (USD-dollarized) — USD eurobonds; B-/CCC distressed-trading post-2024 default proximity — verify |
| PY | ~7.50% est. | (PYG); USD eurobonds ~6-7%; BB+ rated |
| AM | ~8.50% est. | (AMD); USD eurobonds ~6-7%; BB- rated |
| AZ | ~7.00% est. | (AZN de-facto pegged USD); USD eurobonds ~5-6%; BB+ rated; SOFAZ FX-buffer ~US$60bn |
| TN | ~12-14% est. | (TND); USD eurobonds ~10-12% distressed-trading post-IMF EFF suspension Mar 2024; CCC+ — verify |
| IN | ~6.80% est. | (INR); G-Sec 10y benchmark; USD eurobonds limited (capital-controls + FEMA); BBB- rated |
| NG | ~18-20% est. | (NGN) post-Jun 2023 unified-float; USD eurobonds ~9-11%; B-/Caa1 rated; CPI 30%+ overlay |
| KE | ~13.50% est. | (KES); USD eurobonds ~9-10%; B/Caa1 rated; 2024 Eurobond refinancing partial |
| JO | ~5.50% est. | (JOD pegged USD 0.7080 since 1995); USD eurobonds ~6-7%; BB- rated |
| OM | ~5.20% est. | (OMR pegged USD 0.385 since 1986); USD eurobonds ~UST + 70-100 bps; BB+ rated |
| BH | ~5.80% est. | (BHD pegged USD 0.376 since 2001); USD eurobonds ~UST + 200-300 bps; B+/BB- rated |
| KW | ~4.50% est. | (KWD basket-managed since 2007 ~ USD 3.25); USD eurobonds ~UST + 30-50 bps; AA-rated |
| LB | n/a | (LBP unified 2023-24 around USD 89,500-90,000); USD eurobonds in default since Mar 2020 (sovereign default); restructuring stalled — verify; SD/C rated |

## Why macro context matters for property

1. **Mortgage rate environment** (cross-reference `--finance`)
   - 10-yr fixed mortgages closely track 10-yr sovereign yields + bank spread (~150-200 bps)
   - Higher policy rate → tighter mortgage origination

2. **Currency stability** (cross-reference `--currency`)
   - High inflation + weak FX = property price volatility in foreign-buyer terms
   - AR / TR / EG (not in skill) are extreme cases — properties priced in USD/EUR

3. **Cyclical timing**
   - Expansion + low rates + GDP growth → upward pressure on prices
   - Late-cycle + rising rates → cooling
   - Recession + rate cuts → price stabilization, possibly bounce

4. **Sovereign risk** for foreign buyers
   - Spreads >300 bps over Bund signal sovereign-risk premium
   - HU / PL / RO / TR / EG are cases — affect mortgage availability and currency

## Cyclical phase classification (Apr 2026)

### Late-cycle / soft landing
- Eurozone (ECB held 2.50% post-cuts)
- UK (BoE 3.75%)
- US (Fed 4.25-4.50%)
- CA (BoC 2.75%)
- IL (BoI cautious; war-recovery)
- HK (HKMA Fed-bound ~4.75%)
- MO (AMCM Fed-bound ~4.75%)
- TW (CBC Discount Rate 2.00%)
- KR (BOK 2.75% mid-cut path)

### Recovery / cutting
- AU (RBA cutting 4.10%)
- NZ (RBNZ cutting 3.50%)
- IS (CBI cutting 7.50%)
- MX (Banxico paused after 300 bps cuts)
- CL (BCCh ~4.5% from 11.25% peak)
- CO (BanRep ~9% from 13.25% peak)
- PH (BSP ~5.75% mid-cut path)
- ZA (SARB gradual cuts ~7.5%)

### Active tightening / hold high
- HU (MNB 6.50% — HUF volatility)
- BR (BCB 14.75% — Selic on hold post-cuts)
- TR (TCMB 37.0% — held 10 Sep 2026, eased from 50% Mar-2024 peak; CPI 31.51% YoY Aug 2026)
- AR (volatile peso band)
- EG (CBE ~22-24% post-IMF Mar 2024 devaluation; CPI declining from 30%+)
- UY (BCU 8.5% — restrictive)
- GE (NBG hiked 0.25pp to 8.25% on 6 May 2026, held 9 Sep 2026; EU candidate, accession de facto halted since 27 Jun 2024)

### Normalization (post-deflation / post-NIRP)
- JP (BoJ exited NIRP Mar 2024 → 0.5% Jan 2025 → 0.75% Dec 2025 → 1.0% Jun 2026 → 1.25% Sep 2026; first sustained hike cycle in ~17 years)

### Expansion / loose
- VN (SBV accommodative; ~6% GDP)
- ID (BI 6% holding; ~5% GDP)
- MY (BNM OPR 3% steady; ~5% GDP)
- TH (BoT 2.5% steady; ~3% GDP)
- MA (BAM 2.5% stable)
- DO (BCRD easing)

### Stable / pegged
- BG (joined eurozone Jan 2026)
- HR (eurozone since 2023)
- ME (unilateral euroisation)
- BA (currency board)
- DK (ERM-II)
- AE (AED pegged to USD 3.6725 — Fed-bound monetary policy)
- PA (USD-dollarized — Fed-bound)
- SG (S$NEER managed-float against undisclosed basket — MAS macroprudential tools)
- LI (CHF via 1980 Currency Treaty — SNB-bound)
- AD (EUR via 2011 Monetary Treaty — ECB indirect)
- MC (EUR via 2002 Monetary Convention with FR — ECB indirect)

### Active tightening / hold high (additional)
- MD (BNM 6.50% post-2022 war shock; MDL volatile)
- TN (BCT 8.00% post-2022-23 inflation shock; CPI 7-8%; IMF EFF SUSPENDED Mar 2024)
- AM (CBA ~7.00% gradual cuts as CPI near target)
- AZ (CBAR ~7.25% hold; AZN de-facto pegged USD)

### Stable / pegged (additional Tier-4)
- QA (QAR pegged USD 3.64 since 2001 — Fed-bound)
- SA (SAR pegged USD 3.75 since 1986 — Fed-bound)
- EC (USD adopted Sep 2000 — Fed-bound, no monetary independence)

### Recovery / cutting (additional Tier-4)
- PE (BCRP ~4.50% mid-cycle cuts from 7.75% peak 2023)
- PY (BCP ~6.00% hold)

### Tier-5 additions (2026-05-01)

#### Active tightening / hold high (Tier-5)
- NG (CBN ~27.50% est. post-NGN unification Jun 2023; CPI 30%+)
- KE (CBK ~10.75% gradual cuts; KES managed-float ~2-5%/yr USD depreciation)
- IN (RBI ~6.00% mid-cycle cuts; INR managed-float; FEMA + LRS USD 250k/yr cap)

#### Stable / pegged (Tier-5)
- JO (JOD pegged USD 0.7080 since 1995 — Fed-bound, NO FX risk)
- OM (OMR pegged USD 0.385 since 1986 — Fed-bound, NO FX risk)
- BH (BHD pegged USD 0.376 since 2001 — Fed-bound, NO FX risk; UNIQUE highest face-value globally)
- KW (KWD basket-managed since 20 May 2007 ≈ USD 3.25 — world's HIGHEST face-value currency; CBK active basket-management)

#### Distressed / sovereign-default (Tier-5)
- LB (BDL n/a; LBP HISTORICAL HYPERINFLATION — pegged USD 1,507.5 since 1997 → decoupled Sep 2019 → black-market peak USD 100,000+ 2022 → unified 2023-24 around USD 89,500-90,000; de-facto USD-dollarization 80%+ prime; **2024 Israel-Hezbollah war Sep-Nov 2024**; sovereign default since Mar 2020)

## Inflation trajectory (Apr 2026, recent quarter)

EU rough YoY: 2.2-2.8% (post-2022 peak)
UK: 2.5-3.0%
US: ~2.5% est. (Q1 2026 print pending — verify BLS CPI release)
HU: 4-5% (HUF volatility)
PL: 3-4%
RO: 4-5% (post-VAT-hike)
TR: 31.51% YoY Aug 2026 (TÜFE, TÜİK via TCMB PPK summary 2026-42 — high-inflation regime, easing trajectory; verify TÜİK)
AR: 30%+ (post-Milei normalization)
BR: 4-5% (Selic on hold)
JP: ~2-3% (BoJ target met; first sustained 2%+ run since 1990s)
TH: ~1-2% (sub-target)
AE: ~2-3% (low; pegged regime)
DO: ~3-5%
CO: ~5%
UY: ~5-6%
CL: ~3-4% (within BCCh 3% target band)
ZA: ~4-5% (within SARB 3-6% band)
GE: ~2-3%
ID: ~3% (within BI 2.5±1% target)
MY: ~2-3%
VN: ~3-4% (within SBV 4.5% ceiling)
PH: ~3-4% (within BSP 2-4% target)
IL: ~3% (war-affected supply shocks)
MA: ~2%
EG: ~30%+ declining (post-Mar 2024 EGP devaluation; verify CAPMAS)
SG: ~2.4% est. (Mar 2026 — verify MAS CPI release https://www.mas.gov.sg)
HK: ~1.7% est. (Q1 2026 — verify https://www.censtatd.gov.hk)
KR: ~2.1% est. (Q1 2026 — verify KOSTAT)
TW: ~2.0% est. (Q1 2026 — verify DGBAS https://www.dgbas.gov.tw)
LI: ~1.5% est. (CHF-bound, tracks CH; verify Statistik Liechtenstein)
MO: ~2% est. (verify DSEC https://www.dsec.gov.mo)
AD: ~3% est. (verify Estadística d'Andorra https://www.estadistica.ad)
MC: ~3% est. (verify IMSEE https://www.monacostatistics.mc)
MD: ~4-5% est. (Q1 2026 — post-2022 shock easing; verify BNS https://statistica.gov.md)
QA: ~2.5% est. (Q1 2026 — verify at the National Planning Council https://www.npc.qa/, successor to the PSA; psa.gov.qa is egress-filtered)
SA: ~2.0% est. (Q1 2026 — verify GASTAT https://www.stats.gov.sa)
PE: ~2.5% est. (Q1 2026 — within BCRP 1-3% target; verify INEI https://www.inei.gob.pe)
EC: ~1.5% est. (Q1 2026 — USD-dollarized low-CPI regime; verify INEC https://www.ecuadorencifras.gob.ec)
PY: ~4% est. (Q1 2026 — verify INE https://www.ine.gov.py)
AM: ~2.5% est. (Q1 2026 — near CBA target; verify ARMSTAT https://www.armstat.am)
AZ: ~3% est. (Q1 2026 — verify SSC https://www.stat.gov.az)
TN: ~7-8% est. (Q1 2026 — post-2022-23 shock; verify INS https://www.ins.tn)
IN: ~4-5% est. (Q1 2026 — within RBI 4±2% target; verify NSO/MoSPI https://www.mospi.gov.in)
NG: ~30%+ est. (Q1 2026 — post-NGN unification Jun 2023 shock easing; verify NBS https://nigerianstat.gov.ng)
KE: ~6-7% est. (Q1 2026 — verify KNBS https://www.knbs.or.ke)
JO: ~2.5% est. (Q1 2026 — pegged regime low CPI; verify DOS https://dosweb.dos.gov.jo/)
OM: ~1.5% est. (Q1 2026 — pegged regime low CPI; verify NCSI https://www.ncsi.gov.om)
BH: ~2.0% est. (Q1 2026 — pegged regime; verify iGA https://www.iga.gov.bh)
KW: ~3.0% est. (Q1 2026 — verify CSB https://www.csb.gov.kw)
LB: ~30%+ est. (Q1 2026 — post-hyperinflation stabilization phase but volatile; verify CAS http://www.cas.gov.lb)

## Tier-1 + Tier-2 country macro snapshots (Apr 2026)

The 18 countries below were added to the skill in 2026-Q1/Q2 (Tier-1 PR #57; Tier-2 PR #60); 9 Tier-3 countries (PR #65), 8 Tier-4 countries (added 2026-05-01) and 8 Tier-5 countries (added 2026-05-01) follow. Snapshots are 2025 H2 / Q1 2026 where published; figures stamped `est.` require verification against the next official print.

### Tier-1 (PR #57)

**US** — CPI ~2.5% YoY (Q1 2026 est., verify BLS https://www.bls.gov/cpi/); GDP ~2.5% (2025 BEA advance est., verify https://www.bea.gov); Fed Funds 4.25-4.50% (hold since Q4 2024); 10y UST ~4.30%; cyclical phase: late-cycle / soft-landing.

**TR** — TÜFE 31.51% YoY Aug 2026 (TÜİK via TCMB PPK summary 2026-42; high-inflation regime, easing from Oct-2022 peak 85.51%; verify TÜİK https://www.tuik.gov.tr); GDP ~3-4% (2025 est., verify); TCMB policy rate 37.00% (held at PPK 10 Sep 2026, TCMB 2026-38; cut from 50% Mar-2024 peak — verify against latest MPC https://www.tcmb.gov.tr); 10y TRY yield ~28-32%; USD eurobond ~7.5% — that's the cleaner foreign-buyer reference. Macro flag: **post-hyperinflation normalization, FX risk extreme** — TRY lost ~80% vs USD 2021-2024.

**AE** — CPI ~2-3% (low, pegged regime); GDP ~3-4% (2025); CBUAE EIBOR ~4.40% — Fed-bound via AED/USD peg 3.6725 (no independent monetary policy); USD-equivalent 10y ~4.40%. Macro flag: **stable / pegged**, USD-correlated.

**JP** — CPI ~2-3% (BoJ 2% target met first sustained period since 1990s); GDP ~1% (slow); BoJ policy rate 1.25% (NIRP exit Mar 2024 → 0.50% Jan 2025 → 0.75% Dec 2025 → 1.0% Jun 2026 → 1.25% 18 Sep 2026, effective 24 Sep 2026; 2026 data, source BoJ MPM k260918a https://www.boj.or.jp/en/mopo/mpmdeci/mpr_2026/k260918a.pdf); 10y JGB ~1.50%. Macro flag: **post-NIRP normalization** — first sustained tightening cycle since 2007.

**TH** — CPI ~1-2% (sub-target); GDP ~3% (2025); BoT 2.50% (hold; cut path debated); 10y THB ~2.50%. Macro flag: **stable / soft expansion**, THB strengthening.

**DO** — CPI ~3-5%; GDP ~5% (2025 est.); BCRD ~6.00% est. (gradual easing); 10y DOP ~11%, USD eurobonds ~7-8%. Macro flag: **stable expansion**, BB-rated.

**CO** — CPI ~5%; GDP ~2-3%; BanRep ~9.00% est. (mid-cycle cuts from 13.25% peak Dec 2023); 10y COP ~11.5%, USD eurobonds ~7-8%. Macro flag: **cutting cycle**, BBB-/BB+ split rating.

**UY** — CPI ~5-6%; GDP ~3%; BCU TPM 8.50% est. (restrictive — top of LatAm IG); 10y UYU ~8.5%, USD eurobonds ~6-7%. Macro flag: **stable IG-rated**, restrictive.

**CL** — CPI ~3-4% (within target); GDP ~2-3%; BCCh ~4.50% est. (cut from 11.25% Oct 2023 peak — verify next IPoM https://www.bcentral.cl); 10y CLP ~5.80%; A-rated. Macro flag: **cutting cycle**, IG.

**ZA** — CPI ~4-5% (within SARB 3-6% band); GDP ~1% (Eskom drag easing post-2024); SARB 7.50% est. (gradual cuts from 8.25% peak); 10y ZAR ~10.50%. Macro flag: **slow recovery**, BB-rated, FX volatility.

### Tier-2 (PR #60)

**GE** — CPI 5.6% Aug 2026 (2026 data, source NBG MPC 9 Sep 2026); GDP ~5-6%; NBG 8.25% (held 9 Sep 2026); 10y GEL ~8.5%, USD eurobonds ~7%. Macro flag: **EU candidate, accession de facto halted since 27 Jun 2024 (European Council)** — but watch geopolitical premium (Russia exposure, 2024 foreign-agent law tensions).

**ID** — CPI ~3% (within BI 2.5±1% target); GDP ~5%; BI-Rate 6.00% est. (FX-defence stance protecting IDR); 10y IDR ~7%, USD eurobonds ~5-5.5%. Macro flag: **stable expansion**, BBB-rated.

**MY** — CPI ~2-3%; GDP ~5%; BNM OPR 3.00% (held since 2023); 10y MYR ~3.90%; A-/BBB+. Macro flag: **stable expansion**, IG.

**VN** — CPI ~3-4% (within SBV 4.5% ceiling); GDP ~6% (top regional); SBV refinance rate 4.50% est. (accommodative); 10y VND ~3%, USD eurobonds ~5-6%. Macro flag: **expansion**, BB+ — managed VND.

**PH** — CPI ~3-4% (within BSP 2-4% target); GDP ~6%; BSP ~5.75% est. (cut path from 6.50% peak); 10y PHP ~6.30%, USD eurobonds ~5-5.5%. Macro flag: **expansion / cutting cycle**, BBB-rated.

**IL** — CPI ~3% (war-affected supply shocks); GDP recovery (2024 contracted, 2025 rebound est.); BoI ~4.50% est.; 10y ILS ~4.80% (war-risk premium ~50 bps over pre-Oct-2023 — verify). Macro flag: **war-recovery, sovereign risk premium elevated**.

**MA** — CPI ~2%; GDP ~3-4%; BAM 2.50% est. (hold); 10y MAD ~4.50%; BB+/IG-borderline. Macro flag: **stable expansion**.

**EG** — CPI ~30%+ declining from 2024 peak ~38%; GDP ~3-4% (devaluation drag); CBE ~22-24% est. (held high post-Mar 2024 IMF-conditioned EGP devaluation; verify https://www.cbe.org.eg); 10y EGP ~25%, USD eurobonds ~9-11% (distressed-trading); B-rated. Macro flag: **post-devaluation stabilization, FX crisis residual** — EGP devalued ~60% Mar 2024 under IMF/UAE/EU rescue package.

### Tier-3 (PR pending — added 2026-05-01)

**SG** — CPI ~2.4% est. (Mar 2026 — verify MAS CPI release https://www.mas.gov.sg); GDP ~3-4% (2025 est. — verify Singstat); MAS uses S$NEER managed-float band against undisclosed basket (no policy rate — macroprudential SSD/ABSD/LTV); 10y SGS ~2.80%; AAA-rated. Macro flag: **stable expansion**, financial-hub safe-haven; population ~5.94M (Singstat 2024).

**HK** — CPI ~1.7% est. (Q1 2026 — verify https://www.censtatd.gov.hk); GDP recovering 2024-25 from China-tech / Article-23 NSL Mar 2024 sentiment drag; HKMA Base Rate ~4.75% est. (Fed-bound via Linked Exchange Rate System Convertibility Undertaking 7.75-7.85); 10y HKGB ~4.50%; AA+/AA-. Macro flag: **Fed-bound, sentiment-affected** — Article 23 National Security Law Mar 2024 added sovereign-risk premium for some foreign buyers.

**KR** — CPI ~2.1% est. (Q1 2026 — verify KOSTAT); GDP ~2% (2025); BOK 2.75% est. (gradual cuts from 3.50% peak — verify next BOK MPC https://www.bok.or.kr); 10y KTB ~3.20%; AA-rated. Macro flag: **late-cycle / cutting**, demographic cliff (TFR 0.72 — lowest globally per KOSTAT 2024).

**TW** — CPI ~2.0% est. (Q1 2026 — verify DGBAS https://www.dgbas.gov.tw); GDP ~3-4% (2025, AI-export driven); CBC Discount Rate 2.00% est. (hold; macroprudential focus on Taipei/New Taipei); 10y CGB ~1.60%; AA-rated. Macro flag: **stable expansion**, geopolitical premium (cross-Strait risk).

**LI** — CPI ~1.5% est. (CHF-bound, tracks CH; verify Statistik Liechtenstein https://www.llv.li/en/national-administration/office-of-statistics); GDP ~3-5% (2024 est. — small economy, verify); SNB-bound via 1980 Currency Treaty (no independent rate); no domestic sovereign issuance; AAA-rated. Macro flag: **stable / pegged via CHF**, OECD top-tier GDP/capita; tiny housing market (~40k pop per Statistik Liechtenstein 2024).

**MO** — CPI ~2% est. (verify DSEC https://www.dsec.gov.mo); GDP volatile (gaming-driven ~50% of GDP — recovering 2024-25 post-COVID); AMCM Base Rate ~4.75% est. (HKD-bound via MOP/HKD peg + LERS indirect Fed-bound); 10y MOP not actively traded; AA-rated. Macro flag: **Fed-bound via double peg, gaming-cycle exposed**.

**AD** — CPI ~3% est. (verify Estadística d'Andorra https://www.estadistica.ad); GDP ~1-2% (2024 est. — ski + retail + finance, verify); EUR-using via 2011 Monetary Treaty (not Eurozone, no ECB voting); ECB Deposit rate indirect; sovereign issuance via Treasury; BBB+ rated. Macro flag: **EUR-using, small economy**, ~85k pop.

**MC** — CPI ~3% est. (verify IMSEE https://www.monacostatistics.mc); GDP ~6-8% (2024 est. — finance + real-estate, verify); EUR-using via 2002 Monetary Convention with France (not Eurozone formally); ECB Deposit rate indirect; no domestic sovereign issuance; AA+/AAA-equivalent. Macro flag: **EUR-using, ultra-HNW property market**, ~38k pop (9,500 Monégasques + ~28,500 others per IMSEE).

**MD** — CPI ~4-5% est. (Q1 2026 — post-2022 shock easing; verify BNS https://statistica.gov.md); GDP ~2-3% (2024-25 recovery from 2022 war-shock contraction); BNM 6.50% est. (hold/easing — verify next MPC https://www.bnm.md); 10y MDL ~9%; B-rated. Macro flag: **EU candidate (Jun 2022) → accession negotiations opened Jun 2024**, war-adjacent (Transnistria frozen conflict), MDL volatile 2022-24 from war shock and energy-cutoff.

### Tier-4 (added 2026-05-01)

**QA** — CPI ~2.5% est. (Q1 2026 — verify at the National Planning Council https://www.npc.qa/, successor to the PSA; psa.gov.qa is egress-filtered); GDP ~1-2% (2025 est. — LNG-export driven, post-2022 World Cup base effect); QCB Lending Rate ~5.00% est. (Fed-bound via QAR/USD peg 3.64 since 2001 — verify https://www.qcb.gov.qa); 10y QAR not actively traded; USD eurobonds ~UST + 30-50 bps; AA-rated. Macro flag: **stable / pegged via USD**, hydrocarbon-buffered, Vision 2030 (QNV2030) infra-driven; LNG export competitiveness vs US/AU.

**SA** — CPI ~2.0% est. (Q1 2026 — verify GASTAT https://www.stats.gov.sa); GDP ~3-4% (2025 est. — non-oil sector growing under Vision 2030 mega-projects: NEOM, Diriyah, Red Sea, Riyadh expansion); SAMA Repo ~5.50% est. (Fed-bound via SAR/USD peg 3.75 since 1986 — verify https://www.sama.gov.sa); 10y SAR ~5%; USD eurobonds ~UST + 50-80 bps; A-rated. Macro flag: **stable / pegged via USD**, Vision 2030 mega-project capex driving Riyadh + Jeddah + Eastern Province; aridification + extreme heat (50°C+) infra-stress.

**PE** — CPI ~2.5% est. (Q1 2026 — within BCRP 1-3% target; verify INEI https://www.inei.gob.pe); GDP ~3% (2025 est. — recovery post-2023 contraction); BCRP ~4.50% est. (mid-cycle cuts from 7.75% peak 2023 — verify https://www.bcrp.gob.pe); 10y PEN ~6.50%; USD eurobonds ~5-6%; BBB-rated. Macro flag: **cutting cycle**, IG-rated, Pacific Ring of Fire seismic + Andean glacier retreat physical-risk overlay.

**EC** — CPI ~1.5% est. (Q1 2026 — USD-dollarized low-CPI regime; verify INEC https://www.ecuadorencifras.gob.ec); GDP ~1-2% (2025 est. — security-crisis + drought-driven energy rationing 2024); BCE n/a (USD adopted Sep 2000 — Fed-bound, no monetary independence); 10y USD eurobonds ~9% est., distressed-trading post-2024 default proximity — verify; B-/CCC. Macro flag: **USD-dollarized, sovereign-distress** — 2024 violent-crime peak Guayaquil/Esmeraldas/Manta + Cotopaxi/Tungurahua/Reventador volcanic + INOCAR tsunami coastal exposure.

**PY** — CPI ~4% est. (Q1 2026 — verify INE https://www.ine.gov.py); GDP ~3-4% (2025 est. — Itaipú/Yacyretá hydro + agribusiness export); BCP ~6.00% est. (hold — verify https://www.bcp.gov.py); 10y PYG ~7.50%; USD eurobonds ~6-7%; BB+ rated. Macro flag: **stable expansion**, IG-borderline, Río Paraguay flooding (2014-24 reference) physical-risk; INE no national transactional RE PI (LIGHT — listings via InfoCasas/Properati only).

**AM** — CPI ~2.5% est. (Q1 2026 — near CBA target; verify ARMSTAT https://www.armstat.am); GDP ~5-7% (2024-25 — Russian capital + IT boom post-2022); CBA ~7.00% est. (gradual cuts; verify https://www.cba.am); 10y AMD ~8.50%; USD eurobonds ~6-7%; BB-rated. Macro flag: **expansion / cutting**, AMD strengthened materially 2022-24 from Russian capital + IT inflow; HIGH seismic (1988 Spitak Mw 6.8 baseline); ~7M global diaspora structural FX inflow.

**AZ** — CPI ~3% est. (Q1 2026 — verify SSC https://www.stat.gov.az); GDP ~2-3% (2025 est. — hydrocarbon-driven; SOFAZ State Oil Fund FX-buffer ~US$60bn); CBAR Refinancing Rate ~7.25% est. (hold — verify https://www.cbar.az); 10y AZN ~7%; USD eurobonds ~5-6%; BB+ rated. Macro flag: **stable / de-facto pegged via AZN/USD 1.70 since 2017** (NOT formal currency-board, breached 2015 twice); Caspian sea-level falling 2010-24 ~1m + Absheron mud volcanoes (unique physical-risk profile); Republic Seismological Survey Center + AzDTN 2.4-1 2010 code (2000 Baku Mw 6.8 baseline).

**TN** — CPI ~7-8% est. (Q1 2026 — post-2022-23 shock; verify INS https://www.ins.tn); GDP ~1-2% (2025 est. — IMF EFF SUSPENDED Mar 2024 leaves financing gap); BCT 8.00% est. (hold — verify https://www.bct.gov.tn); 10y TND ~12-14%; USD eurobonds ~10-12% distressed-trading; CCC+ — verify. Macro flag: **post-IMF-suspension financing-gap stress**, TND semi-convertible (capital controls), CPI elevated, low-mod seismic (ONM); APAL coastal-erosion overlay.

### Tier-5 (added 2026-05-01)

**IN** — CPI ~4-5% est. (Q1 2026 — within RBI 4±2% target; verify NSO/MoSPI https://www.mospi.gov.in); GDP ~6-7% (2025 est. — among highest among major EM); RBI Repo ~6.00% est. (mid-cycle cuts from 6.50% peak — verify https://www.rbi.org.in); 10y G-Sec ~6.80%; BBB- rated. Macro flag: **expansion**, INR managed-float capital controls via FEMA + LRS USD 250k/yr cap; **NHB Residex 50+ cities + RBI HPI 10-city quarterly**; ~1.428B pop (2011 last full census, 2021 deferred to 2025-26); India Stack (Aadhaar + UPI + DigiLocker + ONDC) digital infrastructure; coworking Bengaluru/Hyderabad/Mumbai/Pune/Gurgaon (WeWork/Awfis/91springboard).

**NG** — CPI ~30%+ est. (Q1 2026 — post-NGN unification Jun 2023 shock easing; verify NBS https://nigerianstat.gov.ng); GDP ~3% (2025 est. — devaluation drag + non-oil recovery); CBN MPR ~27.50% est. (hold/easing — verify https://www.cbn.gov.ng); 10y NGN ~18-20%; USD eurobonds ~9-11%; B-/Caa1 rated. Macro flag: **post-FX-unification stabilization, hyperinflation-adjacent regime** — NGN/USD 460→1,500+ peak post-Jun 2023 unified-float (was dual-rate); ~227M pop (UN 2024 proj — 2006 was last full census); 2024-25 grid collapses recurring; coworking Lagos VI/Ikoyi (Workstation/Capital Square/Workbench).

**KE** — CPI ~6-7% est. (Q1 2026 — easing; verify KNBS https://www.knbs.or.ke); GDP ~5% (2025 est. — agriculture + services); CBK CBR ~10.75% est. (gradual cuts — verify https://www.centralbank.go.ke); 10y KES ~13.50%; USD eurobonds ~9-10%; B/Caa1 rated. Macro flag: **stable expansion**, KES managed-float ~2-5%/yr USD depreciation; ~55M pop (2019 census 47.6M, 2024 KNBS); M-PESA mobile money 95%+ adoption (financial inclusion best-in-class); SGR Mombasa-Nairobi corridor; coworking Nairobi Westlands/Karen/Kilimani (iHub/Nailab/Workstyle/The Mint Hub).

**JO** — CPI ~2.5% est. (Q1 2026 — pegged regime low CPI; verify DOS https://dosweb.dos.gov.jo/); GDP ~2-3% (2025 est. — IMF EFF on track + tourism recovery despite regional war); CBJ ~6.50% est. (Fed-bound via JOD/USD peg 0.7080 since 1995 — verify https://www.cbj.gov.jo); 10y JOD ~5.50%; USD eurobonds ~6-7%; BB- rated. Macro flag: **stable / pegged via USD**, NO FX risk; ~11.4M pop (2024 DOS estimate including refugees); among most water-poor globally — Disi+Red-Dead project; aridification + Dead Sea declining 1m/yr; Vision 2025/2033.

**OM** — CPI ~1.5% est. (Q1 2026 — pegged regime; verify NCSI https://www.ncsi.gov.om); GDP ~1-2% (2025 est. — hydrocarbon-driven, Vision 2040 diversification); CBO ~5.50% est. (Fed-bound via OMR/USD peg 0.385 since 1986 — verify https://cbo.gov.om); 10y OMR not actively traded; USD eurobonds ~UST + 70-100 bps; BB+ rated. Macro flag: **stable / pegged via USD**, NO FX risk; ~5.0M pop (NCSI 2024); cyclone exposure HIGH — Gonu 2007/Mekunu 2018/Shaheen 2021 catastrophic Muscat; Khareef monsoon Salalah Jul-Sep; Vision 2040.

**BH** — CPI ~2.0% est. (Q1 2026 — pegged regime; verify iGA https://www.iga.gov.bh); GDP ~2-3% (2025 est. — financial-services + manufacturing); CBB 1-week deposit ~6.00% est. (Fed-bound via BHD/USD peg 0.376 since 2001 — verify https://www.cbb.gov.bh); 10y BHD ~5.80%; USD eurobonds ~UST + 200-300 bps; B+/BB- rated. Macro flag: **stable / pegged via USD**, NO FX risk, UNIQUE highest face-value globally (BHD ≈ USD 2.66); ~1.49M pop (iGA 2024); minimal natural risk except 45°C+ heat + sandstorms; National Spatial Strategy 2050 + Saudi Causeway 2.

**KW** — CPI ~3.0% est. (Q1 2026 — verify CSB https://www.csb.gov.kw); GDP ~2-3% (2025 est. — hydrocarbon-driven; future generations sovereign-fund FX-buffer ~US$700bn KIA est.); CBK Discount Rate ~4.25% est. (basket-managed since 20 May 2007 — was USD-pegged — verify https://www.cbk.gov.kw); 10y KWD ~4.50%; USD eurobonds ~UST + 30-50 bps; AA-rated. Macro flag: **stable / basket-managed**, KWD ≈ USD 3.25 — world's HIGHEST face-value currency; ~4.85M pop (2024 PACI); minimal seismic + extreme heat 50°C+ summers + sandstorms + Apr 2018 + 2024 catastrophic flash floods Wadi; Vision 2035 + Mubarak Al-Kabeer Port + Silk City planned.

**LB** — CPI ~30%+ est. (Q1 2026 — post-hyperinflation stabilization phase but volatile; verify CAS http://www.cas.gov.lb); GDP contracted ~40% peak-to-trough since 2019 collapse (2024-25 partial recovery est.); BDL n/a (multiple rates post-2019); USD eurobonds in default since Mar 2020 (sovereign default); restructuring stalled — verify; SD/C rated. Macro flag: **sovereign-default + post-hyperinflation + war-affected** — LBP pegged USD 1,507.5 since 1997 → decoupled Sep 2019 → black-market peak USD 100,000+ 2022 → unified 2023-24 around USD 89,500-90,000; de-facto USD-dollarization 80%+ prime; **2024 Israel-Hezbollah war Sep-Nov 2024** damage S Lebanon + Bekaa + Beirut SE Dahieh; Aug 2020 Beirut Port explosion; ~5.5M pop (incl ~1.5M Syrian + ~470k Palestinian refugees, CAS estimate); EDL electricity 3-12 hr/day + private generator subscription mandatory; Joseph Aoun presidency Jan 2025 ended 2-yr political vacuum.

### What to verify before use

For any of the 43 above (Tier-1 + Tier-2 + Tier-3 + Tier-4 + Tier-5), the standard pre-output flow is:

1. Pull latest CPI print from the country's statistics office (named in the source registry above).
2. Check the central bank's most-recent MPC statement for current policy rate (the rate cycle moves faster than this snapshot).
3. For EM countries (TR, EG, AR-equiv): always cite the **USD eurobond** yield as the foreign-buyer reference, NOT the local-currency 10y — the local yield is an inflation/FX number, not a rate-of-return for a USD/EUR-paying buyer.
4. Stamp the section `**Last verified**: <YYYY-MM-DD>` and confidence band.

## Quality bar for `--macro`

- **Cite source within last 90 days** for HIGH confidence
- **Use Eurostat HICP / OECD / IMF WEO** as cross-reference for HIGH confidence
- **Flag if data >12 months old** as MEDIUM
- **For Western Balkans + LatAm**: IMF WEO is often the cleanest comparable source

## Cost-of-living — net-of-tax country index (sourcing + the city-vs-home cap)

A working-age mover's real question is "what will daily life cost me, **after tax**, here vs where I am now?" That has a genuinely orthogonal, fully-sourced **country-level** answer — but the **city-vs-home** number everyone actually wants is **not** primary-sourceable below the national line outside the US. Classify the granularity before quoting anything:

- 🟢 **Official sub-national / city price parities — US ONLY**: [US BEA Regional Price Parities](https://www.bea.gov/data/prices-inflation/regional-price-parities-state-and-metro-area) (50 states + DC + metro areas; 2024 reference year, released Feb 2026). A US city-vs-city real-purchasing-power comparison may be quoted as sourced.
- 🟡 **Sub-national but stale / region-only — UK**: [ONS Relative Regional Consumer Price Levels](https://www.ons.gov.uk/economy/inflationandpriceindices/articles/relativeregionalconsumerpricelevelsuk/2016) — a **single 2016 one-off** (5 headline regions); quote only date-stamped "(2016, one-off)".
- 🟠 **Country-level only (the whole rest of the corpus)** — give the **net-of-tax country index** and STOP at the national line: combine **net take-home** ([OECD Taxing Wages 2026](https://www.oecd.org/en/publications/2026/04/taxing-wages-2026_d1f39986/full-report/overview_d93131c3.html), ref year 2025, 38 OECD members — net pay for single / one-earner+2-kids / two-earner+2-kids profiles) with a **comparative price level** ([Eurostat PLI 2024](https://ec.europa.eu/eurostat/statistics-explained/index.php?title=Comparative_price_levels_of_consumer_goods_and_services), 36 European countries + JP/US/UK, EU=100, COICOP-decomposable; OECD PLI/PPP for non-EU OECD; [World Bank ICP 2021](https://www.worldbank.org/en/programs/icp/data) for the ~176-economy long tail).
- 🔴 **No current PLI** → "data not publicly available — verify at the national statistics office."

**The net-of-tax method (the orthogonal slice)**: *real disposable position ≈ net take-home (Taxing Wages, by household profile) ÷ price level (PLI, EU=100 or PPP)*. This is what neither `--retirement` (gross pension tiers) nor `--digital-nomad` (EUR income bands) carries: a working-age, **after-tax**, profile-aware, country-level cost position.

**Honest tail (the hard cap)**: **city-level is hard-capped to 🟢/🟡** — for everywhere except the US (and stale UK regions) the honest output is the country-level net-of-tax index, NOT a city-vs-home ratio. **Numbeo / Expatistan may appear ONLY tagged "crowdsourced, not primary," never as a verdict basis** (user-submitted, unweighted). The `--compare` / `--match` `cost-of-living` criterion is sourced from the primary datasets above (per household profile), never from a crowdsourced aggregate.

## Status

Last refreshed: 2026-05-01 (Tier-5 expansion: +8 countries — IN, NG, KE, JO, OM, BH, KW, LB; cumulative 87 countries: 44 original + 10 Tier-1 + 8 Tier-2 + 9 Tier-3 + 8 Tier-4 + 8 Tier-5). Next refresh: monthly (rates/inflation), quarterly (GDP).
