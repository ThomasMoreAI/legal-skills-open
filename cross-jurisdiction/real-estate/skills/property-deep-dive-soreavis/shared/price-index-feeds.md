# Price-Index Data Feeds Catalog

Per-country house price index sources, including API/CSV/RSS availability, frequency, latest verifiable value. **This catalog supports `--update --refresh-only`** — when the validator is pulling fresh comp values for `--price`, this is the source-of-truth registry.

**Snapshot**: May 2026 (Tier-5 additions).

## Universal contract

For each country, return:
1. **Authoritative source** (national statistics office or central bank)
2. **Index URL** (HTML, hopefully also CSV/JSON)
3. **API/CSV/RSS availability** (machine-readable feed?)
4. **Frequency** (monthly / quarterly / annual)
5. **Latest verifiable value** as of refresh-date
6. **Eurostat HPI cross-reference** (most EU sources align with Eurostat HPI series)

## Output template

```markdown
## Price-Index Feed

**Country**: <ISO2>
**Source**: <authority>
**Index name**: <official series name>
**HTML**: <URL>
**Machine-readable**: <CSV / JSON / RSS / FRED / none>
**Frequency**: <quarterly | monthly | annual>
**Latest value (date)**: <number with date>
**Eurostat HPI ref**: <https://ec.europa.eu/eurostat/databrowser/view/prc_hpi_q__custom_xxx/default/table>
```

---

## Europe — verified sources

| ISO | Source | Index | HTML / data | Frequency | Latest value (Apr 2026) |
|---|---|---|---|---|---|
| **FR** | INSEE | Indice des prix des logements | https://www.insee.fr/fr/statistiques/serie/000857179 | quarterly | Q4 2025 |
| **IT** | ISTAT | Indice dei prezzi delle abitazioni | https://www.istat.it/it/files/abitazioni/ | quarterly | Q4 2025 |
| **CZ** | ČSÚ | Cenové indexy bytů | https://csu.gov.cz/ | quarterly | Q4 2025 |
| **SK** | NBS / ŠÚ SR | RBNV | https://nbs.sk/statisticke-udaje/ + https://slovak.statistics.sk/ | quarterly | Q4 2025 |
| **DE** | Destatis | Häuserpreisindex | https://www.destatis.de/DE/Themen/Wirtschaft/Preise/Baupreise-Immobilienpreisindex/ | quarterly | Q4 2025 |
| **AT** | Statistik Austria + OeNB | Wohnimmobilien | https://www.statistik.at/ + https://www.oenb.at/ | quarterly | Q4 2025 |
| **CH** | Wüest Partner / Swiss FSO | swiss real-estate index | https://www.wuestpartner.com/ + https://www.bfs.admin.ch/ | quarterly | Q4 2025 |
| **ES** | INE | IPV (Índice de Precios de Vivienda) | https://www.ine.es/dyngs/INEbase/es/operacion.htm?c=Estadistica_C&cid=1254736152838&menu=ultiDatos&idp=1254735976607 | quarterly | Q4 2025 |
| **PT** | INE | IPHab (Índice de Preços da Habitação) | https://www.ine.pt/ | quarterly | Q4 2025 |
| **SE** | SCB + Lantmäteriet | Fastighetsprisindex | https://www.scb.se/ | quarterly | Q4 2025 |
| **FI** | Tilastokeskus | Asuntojen hintaindeksi | https://stat.fi/en/statistics/ashi | quarterly | Q4 2025 |
| **NO** | SSB + Eiendom Norge | Boligprisindeks | https://www.ssb.no/en/statbank/list/bpi | monthly | Q4 2025 |
| **UK** | UK HPI (HMLR + ONS + Land Registry) | UK HPI | https://www.gov.uk/government/collections/uk-house-price-index-reports | monthly | Latest published |
| **NL** | CBS + Kadaster | Prijsindex bestaande koopwoningen | https://www.cbs.nl/ | monthly | Q4 2025 |
| **BE** | STATBEL | Prijzen onroerende goederen | https://statbel.fgov.be/ | quarterly | Q4 2025 |
| **DK** | Danmarks Statistik | Ejendomspriser | https://www.dst.dk/en | quarterly | Q4 2025 |
| **IS** | HMS / Þjóðskrá | Vísitala íbúðaverðs | https://hms.is/en/ | monthly | Latest |
| **SI** | SURS / GURS | Cene stanovanjskih nepremičnin | https://www.stat.si/StatWeb/en | quarterly | Q4 2025 |
| **IE** | CSO | Residential Property Price Index | https://www.cso.ie/en/statistics/prices/residentialpropertypriceindex/ | monthly | Latest |
| **GR** | Bank of Greece + Hellenic Stat | RPPI | https://www.bankofgreece.gr/ + https://www.statistics.gr/en/home | quarterly | Q4 2025 |
| **PL** | NBP BaRN | RBNV | https://nbp.pl/en/statistic/property-prices/ | quarterly | Q4 2025 |
| **EE** | Statistics Estonia | RBNV | https://andmed.stat.ee/ | quarterly | Q4 2025 |
| **HR** | DZS + HNB | RBNV | https://podaci.dzs.hr/en/ + https://www.hnb.hr/ | quarterly | Q4 2025 |
| **HU** | KSH + MNB | Lakásárindex | https://www.ksh.hu/ + https://www.mnb.hu/en | quarterly | Q4 2025 |
| **LT** | Ober-Haus + OSP | OHBI + HPI | https://www.ober-haus.lt/en/rinkos_apzvalgos/lithuanian-price-index/ + https://osp.stat.gov.lt/ | monthly + quarterly | Dec 2025 (Vilnius +10.7% YoY) |
| **LV** | CSP + Latvijas Banka | HPI | https://stat.gov.lv/en + https://www.bank.lv/ | quarterly | Q4 2025: 224.02 (+8.4% YoY through Q3) |
| **RO** | INS | IPL (Indicele prețurilor locuințelor) | https://www.insse.ro/ | quarterly | Q4 2025: 168.99 |
| **BG** | NSI | HPI | https://www.nsi.bg/en/metadata/house-price-index-hpi-227 | quarterly | Q4 2025: 256.71 |
| **LU** | STATEC + Observatoire de l'Habitat | HPI | https://statistiques.public.lu/en/publications/series/logement-chiffres.html | quarterly | Q1 2025: apartments €8,094/m² (+3.7% YoY) |
| **CY** | Central Bank of Cyprus | RPPI | https://www.centralbank.cy/en/publications/residential-property-price-indices | quarterly | Q4 2025: +2.3% QoQ; house +7.1% YoY; Limassol apt 150.1 |
| **MT** | NSO + Central Bank of Malta | RPPI | https://nso.gov.mt/property/ + https://www.centralbankmalta.org/ | quarterly | Q4 2025: 177.36 (+6.1% YoY) |

## European microstates / non-EU enclaves

| ISO | Source | Index | URL | Granularity | Frequency | Latest period | Methodology |
|---|---|---|---|---|---|---|---|
| LI | Statistik Liechtenstein + Liechtenstein Bankenverband | no mature standalone HPI — CHF/CH-grid integrated | https://www.llv.li/en/national-administration/office-of-statistics | national | annual (real-estate transaction tables) | Latest published (verify) | **No mature public HPI.** Statistik Liechtenstein publishes transaction counts + average values; cross-reference Wüest Partner CH index for valuation context |
| AD | Estadística d'Andorra (Departament d'Estadística) | Estadístiques d'habitatge | https://www.estadistica.ad/ | national + 7 parròquies | annual (transaction counts + values) | Latest published (verify) | **No standalone HPI series.** Estadística d'Andorra publishes price-per-m² aggregates from registered transactions; verify via 3+ active listings + transaction tables |
| MC | IMSEE (Institut Monégasque de la Statistique) | Observatoire de l'immobilier (annual report) | https://www.monacostatistics.mc/ | national + 4 wards (Monaco-Ville / La Condamine / Monte-Carlo / Fontvieille) | annual | Latest published (verify) | IMSEE Observatoire publishes average price-per-m² for new + resale; tiny market (~5-10 luxury transactions/yr in some segments) means individual deals move averages — verify against 3+ active listings (Savills / Knight Frank Monaco) |
| MD | BNM (Banca Națională a Moldovei) + BNS | Indicele Prețurilor Imobiliare | https://www.bnm.md/ + https://statistica.gov.md/ | national + Chișinău + Bălți | quarterly + annual | Latest published (verify) | BNM publishes Real Estate Price Index for primary + secondary segments Chișinău; BNS publishes annual transaction tables; war-shock 2022-24 created series-break (MDL volatility + USD/EUR-pegged listings dominate Chișinău) |

## Western Balkans

| ISO | Source | Index | URL | Frequency |
|---|---|---|---|---|
| RS | NBS price index | RPPI | https://www.nbs.rs/ | quarterly |
| ME | MONSTAT + CBCG | HPI | https://www.monstat.org/eng/ + https://www.cbcg.me/en | quarterly |
| BA | BHAS + entity statistics offices | HPI | https://bhas.gov.ba/ | annual / quarterly |
| MK | MAKSTAT + NBRSM | HPI | https://www.stat.gov.mk/ | quarterly |
| AL | INSTAT + Bank of Albania (Fischer HPI) | HPI | https://www.instat.gov.al/en/ + https://www.bankofalbania.org/ | quarterly |

## Anglo non-EU

| ISO | Source | Index | URL | Frequency |
|---|---|---|---|---|
| CA | CREA | MLS HPI | https://www.crea.ca/ | monthly |
| AU | ABS RPPI + CoreLogic | RPPI | https://www.abs.gov.au/ + https://www.corelogic.com.au/ | quarterly + monthly |
| NZ | REINZ HPI + QV | HPI | https://www.reinz.co.nz/ + https://www.qv.co.nz/ | monthly |

## Latin America

| ISO | Source | Index | URL | Frequency | Latest period | Methodology |
|---|---|---|---|---|---|---|
| MX | SHF | HPI | https://www.gob.mx/shf | quarterly | — | hedonic, transaction-side |
| BR | FIPE-ZAP + IGMI-R (BCB) | HPI | https://www.fipe.org.br/ + https://www.bcb.gov.br/ | monthly | — | FIPE-ZAP asking-side; IGMI-R repeat-sales (BCB collateral) |
| AR | Reporte Inmobiliario + INDEC | HPI | https://www.reporteinmobiliario.com/ | monthly | — | asking-side, USD-denominated |
| CR | BCCR + INEC | HPI | https://www.bccr.fi.cr/ | quarterly | — | hedonic |
| PA | INEC + Acobir | HPI | https://www.inec.gob.pa/ + https://www.acobir.com/ | annual | — | mixed |
| CO | DANE + BanRep | IPVN (Índice de Precios de Vivienda Nueva) | https://www.dane.gov.co/ + https://www.banrep.gov.co/ | quarterly | Q4 2025 (verify) | DANE IPVN new-build hedonic; BanRep IPVU used-housing tracker (Bogotá/Medellín/Cali) |
| UY | INE + BCU | IPV (Índice de Precios de Inmuebles) | https://www.ine.gub.uy/ + https://www.bcu.gub.uy/ | quarterly | Q4 2025 (verify) | transaction-side, asking-side cross-check via Mercado Libre / InfoCasas |
| CL | INE + CChC | IRPV (Índice Real de Precios de Vivienda) | https://www.ine.gob.cl/ + https://www.cchc.cl/ | quarterly | Q4 2025 (verify) | INE IRPV national hedonic in UF; CChC Cámara Chilena de la Construcción regional |
| DO | BCRD (emerging) + Encuentra24 / Inmobiliaria.com.do | no national HPI | https://www.bancentral.gov.do/ | n/a (BCRD HPI not yet routine-public) | n/a | **No mature public HPI.** BCRD index emerging; listing aggregators (Encuentra24, Inmobiliaria.com.do) provide asking-side only. Verify any €/m² claim via 3+ active listings + DGII transfer-tax records |
| PE | BCRP + INEI + CAPECO | IPV Lima (Índice de Precios de Viviendas) + Encuesta Nacional Continua | https://www.bcrp.gob.pe/ + https://www.inei.gob.pe/ | quarterly (BCRP) + monthly (CAPECO listings) | Q4 2025 (verify; ~3-month lag) | BCRP IPV Lima quarterly hedonic transaction-side from notarial records; INEI Encuesta Nacional Continua tracks rentals + dwelling characteristics; CAPECO (Cámara Peruana de la Construcción) monthly asking-side primary-market |
| EC | INEC + Plusvalía / Properati listings | INEC Indice Precios Vivienda | https://www.ecuadorencifras.gob.ec/ + https://www.plusvalia.com/ | quarterly (INEC) + monthly (listings) | Q4 2025 (verify; ~3-month lag) | INEC IPV hedonic limited coverage Quito/Guayaquil/Cuenca; Plusvalía + Properati asking-side listings provide complementary signal; **2024 security situation Guayaquil/Esmeraldas/Manta affecting transactional volume — verify against latest INEC** |
| PY | INE + InfoCasas / Properati | no national transactional HPI (LIGHT — listings only) | https://www.ine.gov.py/ + https://www.infocasas.com.py/ | quarterly (INE) + monthly (listings) | n/a (INE HPI not routine-public) | **No mature transactional HPI.** INE publishes housing characteristics but not transaction-side price index; InfoCasas + Properati monthly are asking-side only. Verify any USD/m² claim via 3+ active listings + DGRP (Dirección General de Registros Públicos) transfer records |

## North America (non-Anglo grouping)

| ISO | Source | Index | URL | Granularity | Frequency | Latest period | Methodology |
|---|---|---|---|---|---|---|---|
| US | FHFA | HPI (purchase-only + all-transactions) | https://www.fhfa.gov/data/hpi | national / division / state / metro / 3-digit ZIP | monthly + quarterly | Q4 2025 (verify) | repeat-sales on conforming GSE-backed mortgages |
| US | S&P CoreLogic Case-Shiller | National + 20-City Composite | https://www.spglobal.com/spdji/en/index-family/indicators/sp-corelogic-case-shiller/ | national + 20 metros | monthly | Latest published | repeat-sales, value-weighted |
| US | NAR | Median Sales Price of Existing Homes | https://www.nar.realtor/research-and-statistics | national / metro | monthly + quarterly | Latest published | median, transaction-side (NOT quality-adjusted — use FHFA/Case-Shiller for trend) |
| US | Zillow | ZHVI (Zillow Home Value Index) | https://www.zillow.com/research/data/ | national / metro / city / ZIP / neighborhood | monthly | Latest published | smoothed, asking-side automated valuation — NOT a transaction index |
| US | Redfin Data Center | Median sale price + days on market | https://www.redfin.com/news/data-center/ | national / metro / ZIP | weekly + monthly | Latest published | transaction-side, MLS-derived |

## MENA (Middle East + North Africa)

| ISO | Source | Index | URL | Granularity | Frequency | Latest period | Methodology |
|---|---|---|---|---|---|---|---|
| TR | TÜİK + TCMB | Konut Fiyat Endeksi (KFE) | https://data.tuik.gov.tr/Kategori/GetKategori?p=Konut-114 + https://www.tcmb.gov.tr/ | national + 3 metros (Istanbul / Ankara / Izmir) + 26 regions | monthly + quarterly | Latest published (verify) | hedonic, transaction-side from valuation reports — note nominal vs real divergence under high inflation |
| AE | DLD + Bayut + Property Monitor + Property Finder | Bayut Index / Property Monitor PMI / DLD transaction tables | https://www.bayut.com/mybayut/market-trends/ + https://www.propertymonitor.com/ + https://dubailand.gov.ae/ | emirate / community / building | monthly (transactions) | Latest published | DLD = transaction-side primary register; Bayut/PF = asking-side aggregators. **No national HPI** — Dubai-centric coverage |
| IL | CBS (Lamas) | Dwelling Price Index | https://www.cbs.gov.il/he/subjects/Pages/%D7%9E%D7%97%D7%99%D7%A8%D7%99-%D7%93%D7%99%D7%A8%D7%95%D7%AA.aspx | national + 7 districts | monthly + quarterly | Latest published | hedonic, transaction-side from Tax Authority deeds |
| MA | HCP | IPAI (Indice des Prix des Actifs Immobiliers) | https://www.hcp.ma/ | national + main cities | quarterly | Latest published | hedonic, transaction-side jointly with Bank Al-Maghrib |
| EG | CAPMAS / Property Finder Egypt | no mature public HPI | https://www.capmas.gov.eg/ + https://www.propertyfinder.eg/en/research | n/a | monthly (asking-side via Property Finder) | n/a | **No transaction-grade public HPI.** CAPMAS coverage limited; REPA records not queryable; Property Finder Egypt monthly is asking-side only. Verify via 3+ listings + notarised deed comps |
| QA | QCB Real Estate Price Index built on Ministry of Justice transaction data | Qatar Central Bank Real Estate Price Index (REPI) | https://www.qcb.gov.qa/en/pages/realestatepriceindex.aspx + https://www.moj.gov.qa/ | national + Doha (limited) | quarterly | Latest published (verify; ~2-3 month lag) | **QCB** created and publishes the REPI from data issued by the **Ministry of Justice** — methodology in QCB Financial Stability Report III, pp. 85-86 (2026 data, source Qatar Central Bank; 2026-09-18 verified); Doha-centric coverage; thin transaction volume in some segments (5-10 deals/qtr) means individual deals move averages — verify against 3+ active listings (Property Finder QA / Hapondo) |
| SA | GASTAT Real Estate Price Index + REGA + Suhail | GASTAT RE Price Index + Suhail (REGA) transactional platform | https://www.stats.gov.sa/ + https://rega.gov.sa/ + https://rei.rega.gov.sa/en | national + 13 regions + Riyadh / Jeddah / Eastern Province per-district | quarterly | Latest published (verify; ~2-3 month lag) | GASTAT RE PI quarterly hedonic transaction-side from MoJ deeds; REGA Suhail platform publishes transactional registry (mandatory listing per 2024 reform); Vision 2030 mega-project cycles (NEOM, Diriyah, Red Sea) create regional volatility |
| TN | INS + Tayara / Mubawab listings | INS Real Estate Price Index (LIGHT coverage) | https://www.ins.tn/ + https://www.tayara.tn/ + https://www.mubawab.tn/ | n/a (INS HPI light coverage) | annual (INS) + monthly (listings) | Latest published (verify) | **No mature quarterly transactional HPI.** INS publishes annual housing-statistics; Tayara + Mubawab monthly are asking-side only; capital controls (TND semi-convertible) + IMF EFF SUSPENDED Mar 2024 affect foreign-buyer pricing dynamics. Verify any TND/m² claim via 3+ active listings + Conservation de la Propriété Foncière records |
| JO | DOS + CBJ + Jordan Real Estate Investors Association (JREIA) | Sale Price Index — Apartments | http://dosweb.dos.gov.jo/ + https://www.cbj.gov.jo/ | national + Amman + secondary cities | quarterly | Latest published (verify; ~3-month lag) | DOS publishes quarterly Apartment Sale Price Index for Amman + national; JOD pegged USD 0.7080 since 1995 — pricing dynamics anchored to USD via peg; primary + secondary segments tracked; refugee-driven demand overlay (Syrian + Palestinian) affects secondary cities |
| OM | NCSI Real Estate Activity Bulletin + Ministry of Housing & Urban Planning | NCSI RE Activity Bulletin (transaction values + counts) | https://www.ncsi.gov.om/ + https://www.mhut.gov.om/ | national + per-governorate (11 muhafazat) | monthly + annual | Latest published (verify; ~2-month lag) | **No mature standalone HPI series.** NCSI Real Estate Activity Bulletin publishes transaction values + counts (sale + mortgage + rental contracts) per governorate; OMR pegged USD 0.385 since 1986 — pricing anchored to USD; Vision 2040 mega-project cycles (Sultan Haitham City, Yiti, Khazaen) create regional volatility; verify any OMR/m² claim via 3+ active listings + MHUP transactional records |
| BH | iGA + MoH Real Estate Registry + Real Estate Regulatory Authority (RERA Bahrain) | iGA Statistical Bulletin RE chapter + RERA market reports | https://www.iga.gov.bh/ + https://www.rera.gov.bh/ + https://www.moh.gov.bh/ | national + 4 governorates (Capital / Muharraq / Northern / Southern) | quarterly + annual | Latest published (verify; ~3-month lag) | **No mature standalone HPI series.** iGA publishes quarterly Real Estate transaction values + counts; RERA Bahrain publishes market reports + escrow registry; BHD pegged USD 0.376 since 2001 — pricing anchored to USD; small market (~1.49M pop) means thin transaction volume in some segments; verify any BHD/m² claim via 3+ active listings + RERA escrow records |
| KW | MoJ Real Estate Registry + CSB | MoJ monthly Real Estate Transaction Bulletin (نشرة العقارات الشهرية) + Public Authority for Industry data | https://www.moj.gov.kw/ + https://www.csb.gov.kw/ | national + per-governorate (6) + per-area (qit'a) for select segments | monthly | Latest published (verify; ~1-2 month lag) | **No mature standalone HPI series.** MoJ Real Estate Registry publishes monthly transaction-bulletin (residential / investment / commercial); CSB Statistical Abstract has limited RE coverage; KWD basket-managed since 20 May 2007 (≈ USD 3.25 — world's HIGHEST face-value); verify any KWD/m² claim via 3+ active listings (Bo Property / 4Sale / OpenSooq KW) + MoJ monthly bulletin |
| LB | BDL + CAS + Olx.com.lb / Realestate.com.lb listings | no formal HPI (HISTORICAL HYPERINFLATION + sovereign default) | https://www.bdl.gov.lb/ + http://www.cas.gov.lb/ + https://www.olx.com.lb/ + https://www.realestate.com.lb/ | n/a | n/a (BDL + CAS RE indicators not routine-public post-2019 collapse) | n/a | **No mature public HPI.** BDL series interrupted post-2019 collapse + sovereign default Mar 2020; CAS limited coverage; Olx.com.lb + Realestate.com.lb monthly are asking-side only and **routinely USD-denominated** (de-facto USD-dollarization 80%+ prime); LBP unified 2023-24 around USD 89,500-90,000 (was 1,507.5 since 1997 → decoupled Sep 2019 → black-market peak 100,000+ 2022); 2024 Israel-Hezbollah war Sep-Nov 2024 damage S Lebanon/Bekaa/Beirut SE Dahieh creating regional dispersion. Verify any USD/m² claim via 3+ active listings + Direction Générale du Cadastre (notarised deed) records |

## Asia-Pacific

| ISO | Source | Index | URL | Granularity | Frequency | Latest period | Methodology |
|---|---|---|---|---|---|---|---|
| JP | MLIT (国土交通省) | 不動産価格指数 (Real Estate Price Index) | https://www.mlit.go.jp/totikensangyo/totikensangyo_tk5_000085.html | national + region + prefecture | monthly + quarterly | Latest published | hedonic, transaction-side (registered transfers) |
| JP | MLIT | 公示地価 (Kōji-chika land price) | https://www.reinfolib.mlit.go.jp/ | parcel-level (~26k assessment points) | annual (1 Jan reference) | 2026 (1 Jan) | official appraised land prices, parcel-level |
| JP | NTA (国税庁) | 路線価 (Rosen-ka inheritance/gift tax road-frontage value) | https://www.rosenka.nta.go.jp/ | road-segment (parcel proxy) | annual (1 Jul publish) | 2025 (verify 2026 publish) | tax-assessment value, ~80% of Kōji-chika |
| TH | REIC + AREA | REIC HPI / AREA market reports | https://www.reic.or.th/ + http://www.area.co.th/ | Bangkok metropolitan + selected provinces | quarterly | Latest published (verify) | REIC = Bank of Thailand-affiliated, transaction-side; AREA = private survey-based |
| ID | BPS + BI | IHPR (Indeks Harga Properti Residensial) / SHPR survey | https://www.bps.go.id/ + https://www.bi.go.id/ | national + 18 cities (BI primary-market survey) | quarterly | Latest published (verify) | BI SHPR primary-market survey of developers (asking-side); BPS hedonic |
| MY | NAPIC (JPPH) | Malaysian House Price Index (MHPI) | https://napic.jpph.gov.my/ | national + 14 states + key districts | quarterly | Latest published (verify) | hedonic, transaction-side from stamp-duty records — best-in-class regional tracker |
| VN | GSO + MOC | Real Estate Price Index + provincial land-price tables | https://www.nso.gov.vn/en/homepage/ + https://moc.gov.vn/ | national + provincial | quarterly (HPI), annual (provincial land-price tables) | Latest published (verify) | GSO HPI hedonic; **2024 Land Law replaced 5-yr land-price tables with annual provincial tables** — significant methodological shift, see regulatory-watch.md |
| PH | PSA + BSP | RREPI (Residential Real Estate Price Index) | https://psa.gov.ph/ + https://www.bsp.gov.ph/ | national + NCR + Areas Outside NCR | quarterly | Latest published (verify) | hedonic, transaction-side from BSP-supervised banks' housing-loan appraisals |
| SG | URA + HDB | URA Private Residential Property Price Index (PPI) + HDB Resale Price Index (RPI) + Realis (subscription) | https://www.ura.gov.sg/Corporate/Media-Room/Media-Releases + https://www.hdb.gov.sg/cs/infoweb/about-us/news-and-publications/press-releases | national + planning regions (CCR / RCR / OCR for private) + HDB town for HDB resale | quarterly | Latest published (verify) | URA PPI hedonic transaction-side from caveats lodged at URA; HDB RPI hedonic from resale transactions; Realis (paid SLA — Singapore Land Authority) gives parcel-level transaction history |
| HK | RVD (Rating & Valuation Department) | Hong Kong Property Price Index | https://www.rvd.gov.hk/en/publications/property_market_statistics.html | territory + class A-E (size bands) + region (HK Island / Kowloon / NT) | monthly + quarterly | Latest published (verify) | hedonic, transaction-side from stamp-duty register; class A (smallest) to E (largest) by saleable area |
| KR | MOLIT (Ministry of Land, Infrastructure & Transport) + KB Kookmin | RTMS (실거래가) Real-Price Disclosure System + 공시지가 Official Land Price + KB Housing Price Index | http://rt.molit.go.kr/ + https://www.reb.or.kr/ + https://kbland.kr/ | national + 17 provinces/metropolitan-cities + per-gu (district) + Seoul gu-dong; RTMS = parcel/apartment-level transaction history | monthly + quarterly + annual (공시지가) | Latest published (verify) | **RTMS (실거래가) since 2006 = mandatory transaction-price disclosure system, parcel-level transparency** — best-in-class Asia-wide; 공시지가 (Kongsi-jiga) annual official land-price assessment; KB Housing Price Index (private bank, also used by media) |
| TW | MOI (Ministry of Interior) + Taiwan Real Estate Information Platform | 不動產資訊平台 (Real Estate Information Platform) + 實價登錄 2.0 (Actual Price Registration 2.0) | https://lvr.land.moi.gov.tw/ + https://pip.moi.gov.tw/ | national + 6 special municipalities + 16 county/city + per-village (里); 實價登錄 = parcel-level | monthly (transaction registrations) | Latest published (verify) | **實價登錄 2.0 since 2012 (1.0) → 2021 (2.0 — pre-sale included) = mandatory transaction-price registration** — parcel-level transparency comparable to KR RTMS; MOI publishes price-per-坪 (ping = 3.3m²) aggregates per district |
| MO | DSEC + DSF (Direcção dos Serviços de Finanças) + IH Instituto de Habitação | DSEC Property Sales Transaction tables + IH public-housing reference | https://www.dsec.gov.mo/ + https://www.dsf.gov.mo/ + https://www.ihm.gov.mo/ | national + parish-level (7 freguesias) | quarterly | Latest published (verify) | DSEC publishes per-parish transaction counts + average price-per-m² from stamp-duty register; gaming-economy cycle creates volatility; **no mature standalone HPI series** — verify via 3+ active listings + DSEC tables |
| IN | NHB (National Housing Bank) + RBI + MoSPI | **NHB RESIDEX** (50+ cities, primary HPI benchmark) + **RBI House Price Index** (10-city quarterly) + RBI Residential Asset Price Monitoring Survey (RAPMS) | https://www.nhb.org.in/about-residex/ + https://www.rbi.org.in/ + https://www.mospi.gov.in/ | NHB RESIDEX: 50+ cities (Mumbai/Delhi/Bengaluru/Kolkata/Chennai/Hyderabad/Pune/Ahmedabad/etc.); RBI HPI: 10 cities (Mumbai/Delhi/Bengaluru/Kolkata/Chennai/Lucknow/Ahmedabad/Jaipur/Kanpur/Kochi); per-city + sub-city for major metros | quarterly (NHB RESIDEX + RBI HPI) | Latest published (verify; ~3-month lag) | **NHB RESIDEX since 2007** = transaction-side index covering 50+ cities (Composite + sub-city); methodological refresh 2017 to base 2017-18=100; **RBI HPI since 2007** parallel 10-city quarterly from registration authorities; INR managed-float capital controls via FEMA + LRS USD 250k/yr cap affect foreign-buyer + NRI dynamics; RERA (Real Estate Regulation Act 2016) project-registration mandatory in scope — separate state RERA portals (Maharashtra MahaRERA / Karnataka K-RERA / Delhi DDA-RERA) provide complementary supply-side data |

## Africa (sub-Saharan)

| ISO | Source | Index | URL | Granularity | Frequency | Latest period | Methodology |
|---|---|---|---|---|---|---|---|
| ZA | SARB | QB (Quarterly Bulletin) HPI references | https://www.resbank.co.za/ | national | quarterly | Latest published | aggregated from private indices |
| ZA | FNB (First National Bank) | FNB House Price Index | https://blog.fnb.co.za/category/property/ | national + metro | monthly | Latest published | hedonic, FNB-financed transactions |
| ZA | Lightstone | Residential Property Indices | https://lightstone.co.za/ | national + province + suburb | monthly + annual | Latest published | repeat-sales on full deeds-office register — broadest coverage |
| ZA | ABSA | ABSA House Price Index | https://www.absa.co.za/indices/ | national | monthly | Latest published | hedonic, ABSA-financed transactions |
| NG | NBS + CBN + Nigerian Property Centre / PropertyPro listings | NBS RE Activities GDP component + CBN Financial Stability Report (RE chapter) | https://nigerianstat.gov.ng/ + https://www.cbn.gov.ng/ + https://nigeriapropertycentre.com/ + https://www.propertypro.ng/ | national + Lagos / FCT-Abuja / Rivers (Port Harcourt) headlines | quarterly (NBS GDP) + monthly (listings) | Latest published (verify) | **No mature standalone HPI series.** NBS publishes Real Estate Activities GDP component quarterly; CBN Financial Stability Report has bank-collateral RE references; Nigerian Property Centre + PropertyPro monthly are asking-side only; **NGN/USD 460→1,500+ peak post-Jun 2023 unified-float (was dual-rate)** — listings in NGN often re-priced in USD for foreign-buyer segments. Verify any NGN/m² claim via 3+ active listings + Lagos State Land Registry records |
| KE | KNBS + HassConsult Property Index + CBK | HassConsult Land + Sale Price Index (Nairobi quarterly, dominant private benchmark) + KNBS Statistical Abstract | https://www.knbs.or.ke/ + https://www.hassconsult.com/ + https://www.centralbank.go.ke/ | Nairobi (HassConsult) + national headlines (KNBS); HassConsult covers ~18 Nairobi suburbs | quarterly (HassConsult + KNBS) | Latest published (verify; ~1-month lag HassConsult) | HassConsult Property Index is the dominant private benchmark — quarterly Land Price Index + Sale Price Index covering 18 Nairobi suburbs (Westlands/Karen/Kilimani/Lavington/Runda/Spring Valley/Kileleshwa/Riverside/Loresho/Muthaiga/Gigiri/Kitisuru/Ridgeways/Donholm/Kiambu/Ruaka/Limuru/Tigoni); KNBS publishes Statistical Abstract RE chapter; KES managed-float ~2-5%/yr USD depreciation; M-PESA mobile money 95%+ adoption simplifies cash-flow tracking |

## Caucasus

| ISO | Source | Index | URL | Granularity | Frequency | Latest period | Methodology |
|---|---|---|---|---|---|---|---|
| GE | Geostat | Real Estate Price Index | https://www.geostat.ge/en | national + Tbilisi + 4 secondary cities | quarterly | Latest published (verify) | hedonic, transaction-side from Public Registry |
| AM | ARMSTAT (Statistical Committee of Armenia) | RE Price Index Yerevan + national | https://www.armstat.am/ | national + Yerevan + 9 marzes | quarterly | Latest published (verify; ~2-month lag) | ARMSTAT publishes quarterly Real Estate Price Index; Yerevan + national coverage; AMD strengthened materially 2022-24 from Russian capital + IT boom — re-verify nominal vs real terms; primary + secondary segments tracked |
| AZ | SSC (State Statistical Committee) | RE Statistics (quarterly) | https://www.stat.gov.az/ | national + Baku + 9 economic regions | quarterly | Latest published (verify; ~2-month lag) | SSC publishes quarterly Real Estate Statistics including price-per-m² by segment; AZN de-facto pegged USD 1.70 since 2017 (NOT formal currency-board, breached 2015 twice) — pricing dynamics anchored to USD via peg; primary + secondary segments tracked |

---

## BIS / FRED cross-references (international comparable)

The Bank for International Settlements (BIS) maintains a uniform Residential Property Price database; FRED republishes it. Use these for cross-country comparable real-terms growth — NOT for level €/m² values.

- **BIS portal**: https://www.bis.org/statistics/pp.htm
- **BIS by-country**: https://www.bis.org/statistics/pp_selected.htm
- **FRED collection**: https://fred.stlouisfed.org/categories/32218

Examples:
- LT: https://fred.stlouisfed.org/series/QLTN628BIS
- LV: https://fred.stlouisfed.org/series/QLVN628BIS
- BG: https://fred.stlouisfed.org/series/QBGN628BIS

## Eurostat HPI

Pan-EU comparable index (quality-adjusted, base=100). For all EU+EEA countries.

- **Database**: https://ec.europa.eu/eurostat/web/housing/database
- **Methodology**: https://ec.europa.eu/eurostat/cache/metadata/en/prc_hpi_oo_esms.htm

---

## Refresh logic for `--update --refresh-only`

Per country playbook:

1. **Fetch latest index value** from authoritative source (HTML scrape OR machine-readable endpoint where available)
2. **Cross-check against Eurostat HPI** for EU/EEA (any divergence >5% YoY = flag)
3. **Compute YoY + QoQ delta** vs prior playbook value
4. **Update country playbook §price** with: latest value, source URL, retrieval timestamp
5. **Trigger anti-hallucination check 4** ("source ranking — never silently upgrade")
6. **Log to `playbook.md.bak-<date>`** as part of standard updater flow

## Frequency-of-refresh recommendation

- **Monthly**: countries with monthly index (UK, NL, IE, NO, IS, CR, BR, CA, NZ, LT/Ober-Haus)
- **Quarterly**: most EU + LV/RO/BG/LU/CY/MT
- **Per-event**: any reform (BG eurozone, RO VAT, ES regional ITP) triggers an immediate re-fetch

## Status

Last refreshed: 2026-05-01 (added 8-country Tier-5 expansion: IN, NG, KE, JO, OM, BH, KW, LB; cumulative 87 countries). QA REPI producer re-verified against QCB 2026-09-18; PSA attribution corrected — the "Latest published" freshness was NOT re-checked. "Latest period" cells marked `(verify)` await first round of `--update --refresh-only` to capture the actual published Q4 2025 / Q1 2026 values from each authority.

**Confidence**: MEDIUM — every URL is the canonical authority's own domain; methodology notes reflect each authority's published metadata. Specific Q4 2025 / Q1 2026 numeric values were NOT fetched in this expansion pass, so they're labelled `Latest published (verify)` rather than asserted. DO, EG, LI, AD, MC, MO, PY, TN, NG, OM, BH, KW, LB flagged plainly as having no mature standalone public HPI — verification path documented in-row. KR RTMS (실거래가) and TW 實價登錄 2.0 are best-in-class parcel-level transaction-price disclosure systems Asia-wide; SA REGA Suhail platform (mandatory listing per 2024 reform) is the regional best-in-class transactional registry for the Gulf. **IN: NHB RESIDEX (50+ cities) + RBI HPI (10-city quarterly) are the canonical Indian HPI benchmarks; KE: HassConsult Property Index is the dominant private-sector benchmark for Nairobi.**
