# Comparable-Transaction (Sold-Price) Database Registry

Per-country registry of **transacted-price** sources — distinct from asking-price portals in `shared/listing-aggregators.md`. Use this to triangulate true market value rather than aspirational list prices.

**Snapshot**: April 2026.

## Universal contract

For each country, return:
1. **Authority** (cadastre / land registry / tax authority / private aggregator)
2. **URL** (verified live)
3. **Access mode**: public / paid / partner-only / no public access
4. **Granularity**: address / postcode / commune / region
5. **Lag**: typical 1mo / 3mo / 12mo
6. **Coverage start date**
7. **API/CSV/RSS available?**
8. **Cost** if paid
9. **Notes / quirks**

**Legend**:
- **Mode**: `public` (free, no login) · `paid` (per-extract) · `partner-only` · `none` (no public source)
- **Granularity**: `address` · `postcode` · `commune` · `region`

---

## EU Member States

### 🇫🇷 France

| Field | Value |
|---|---|
| Authority | **DGFiP** — Direction Générale des Finances Publiques |
| Public tool | **DVF** — https://app.dvf.etalab.gouv.fr/ |
| Raw data | https://www.data.gouv.fr/fr/datasets/demandes-de-valeurs-foncieres/ |
| Mode | public (open data) |
| Granularity | **address-level** (parcel + street number, m², rooms, type) |
| Lag | ~6 months (semi-annual: April + October) |
| Coverage | **2014 → present** |
| API/CSV | full CSV per dépt + commune; GeoJSON via Etalab; REST API at api.cquest.org/dvf |
| Cost | free |
| Quirks | Excludes **Alsace-Moselle** (67/68/57 — local Livre Foncier) and Mayotte. VEFAs (off-plan) appear under construction date. Donations and inherited transfers excluded. |

### 🇮🇹 Italy

| Field | Value |
|---|---|
| Authority | Agenzia delle Entrate — **OMI** (Osservatorio Mercato Immobiliare) |
| URL | https://www1.agenziaentrate.gov.it/servizi/Consultazione/ricerca.htm |
| Mode | public bands; full transaction-level paid via SISTER |
| Granularity | **OMI zone** (sub-municipal grid: B1, C2, D3) — NOT address |
| Lag | semi-annual (~6 months) |
| Coverage | OMI bands 2004 → |
| Cost | bands free; visura ipotecaria ~€5–€15 |
| Quirks | Free tier is min/max €/m² band per zone, NOT actual prices. Address-level requires notary or paid ipocatastale. |

### 🇨🇿 Czech Republic

| Field | Value |
|---|---|
| Authority | **ČÚZK** |
| URL | https://nahlizenidokn.cuzk.gov.cz/ |
| Mode | public lookup; price extracts paid |
| Granularity | parcel-level |
| Lag | ~1–3 months |
| Cost | výpis ~CZK 100 (€4) |
| Quirks | Sale price in deed but accessing requires per-LV order. No bulk open dataset. **Cenová mapa** (cenovamapa.cz) and Sreality stats offer indicative trends. |

### 🇸🇰 Slovakia

| Field | Value |
|---|---|
| Authority | **ÚGKK SR** |
| URL | https://kataster.skgeodesy.sk/eskn-portal |
| Mode | partner-only / paid |
| Granularity | parcel-level |
| Cost | per-extract ~€8 |
| Quirks | No DVF-style open dataset. NBS publishes quarterly residential indices (region) — useful for trends, not specifics. |

### 🇩🇪 Germany

| Field | Value |
|---|---|
| Authority | **Gutachterausschüsse** (one per Land/Kreis) |
| Federal portal | **BORIS-D** — https://www.bodenrichtwerte-boris.de/boris-d/ |
| Mode | public for **Bodenrichtwerte**; transaction prices partner-only / paid |
| Granularity | Bodenrichtwert: zone-level. Transaction kaufpreissammlung: parcel (restricted) |
| Cost | Bodenrichtwerte free; Grundstücksmarktbericht free; full kaufpreissammlung €30–€500 per query |
| Quirks | No federal sold-price registry. 16 Länder + 100+ Gutachterausschüsse each runs its own. **ImmoScout24** sells partner-only Datenbank Pro. Bayern + SH most restrictive. |

### 🇦🇹 Austria

| Field | Value |
|---|---|
| Authority | **Grundbuch** (Bezirksgerichte) + **Statistik Austria** |
| URL | https://justizonline.gv.at/ |
| Mode | per-property paid; aggregated index public |
| Cost | per-extract ~€15–€25 |
| Quirks | Sale prices public on Grundbuch deed but per-property paid lookup. **ImmoUnited** (immounited.com) sells transaction databases to professionals. |

### 🇨🇭 Switzerland

| Field | Value |
|---|---|
| Authority | **Cantonal land registries** (26 cantons) |
| Federal stats | **BFS** Wohnimmobilienpreisindex — https://www.bfs.admin.ch/ |
| Mode | mostly partner-only |
| Cost | per-extract typically CHF 20–50 |
| Quirks | **Wüest Partner**, **IAZI**, **FPRE** dominant private aggregators (institutional pricing CHF 5k+/yr). Geneva, Zürich, Vaud most digitized. |

### 🇪🇸 Spain

| Field | Value |
|---|---|
| Authority | **Catastro** + **Registro de la Propiedad** (Colegio de Registradores) |
| URL | https://www.sedecatastro.gob.es/ · https://www.registradores.org/en/actualidad/portal-estadistico-registral/estadisticas-de-propiedad |
| Mode | Catastro free; Registro paid per nota simple |
| Cost | nota simple ~€9 |
| Quirks | **Catastral value ≠ market price** (often 30-60% below). Real price in escritura via Registro. Idealista + Tinsa sell transaction-derived indices. |

### 🇵🇹 Portugal

| Field | Value |
|---|---|
| Authority | **IRN** Casa Pronta + **INE** |
| URL | https://www.casapronta.pt/CasaPronta/ · https://www.ine.pt/ |
| Mode | per-property paid; aggregate quarterly public |
| Granularity | INE: municipal + freguesia |
| Cost | certidão permanente ~€15 |
| Quirks | INE publishes **median €/m² per parish** — best free granular sold-price proxy in PT. |

### 🇸🇪 Sweden

| Field | Value |
|---|---|
| Authority | **Lantmäteriet** + **SCB** |
| URL | https://www.lantmateriet.se/ |
| Mode | per-property paid; aggregate free via SCB |
| Cost | per-property lookup ~SEK 50 |
| Quirks | **Hemnet** publishes "slutpris" for ~85% of market — effectively free sold-price dataset. **Booli** (Hemnet subsidiary) has free archive back to ~2007. |

### 🇫🇮 Finland

| Field | Value |
|---|---|
| Authority | **Maanmittauslaitos (NLS)** + **Tilastokeskus** |
| URL | https://www.maanmittauslaitos.fi/en |
| Mode | NLS Kauppahintarekisteri paid extract; aggregated public |
| Cost | NLS subscription €100s+/yr; per-property ~€20 |
| Quirks | **Asuntojen hintatiedot** (asuntojen.hintatiedot.fi) — public free portal showing actual sale prices by postcode for past 12 months. **Best free address-area sold-price source in EU.** |

### 🇳🇴 Norway

| Field | Value |
|---|---|
| Authority | **Kartverket** + **Eiendom Norge** |
| URL | https://eiendomnorge.no/boligprisstatistikk |
| Mode | aggregated public; per-property paid |
| Cost | Kartverket per-extract NOK 207 (~€18) |
| Quirks | **Finn.no** publishes "Solgt" archive — free sold-price proxy. Eiendomsverdi (paid) is institutional benchmark. |

### 🇬🇧 United Kingdom

| Field | Value |
|---|---|
| Authority | **HM Land Registry** (England + Wales) |
| URL | https://www.gov.uk/government/statistical-data-sets/price-paid-data-downloads |
| Mode | **fully public open data** — gold standard |
| Granularity | **address-level** (full postcode + house number) |
| Lag | monthly (typically T+1) |
| Coverage | **1995 → present** for England + Wales |
| API/CSV | full CSV; **SPARQL endpoint** at https://landregistry.data.gov.uk/; INSPIRE GeoJSON |
| Cost | free |
| Quirks | **Excludes Scotland** — use **Registers of Scotland** ScotLIS (paid £30/search). **Excludes Northern Ireland** — use **LPS** + NISRA. Rightmove/Zoopla mash up Land Registry with their photos. |

### 🇳🇱 Netherlands

| Field | Value |
|---|---|
| Authority | **Kadaster** |
| URL | https://www.kadaster.nl/zakelijk/vastgoedinformatie/vastgoedcijfers/vastgoeddashboard |
| Mode | aggregate public; per-property paid |
| Cost | Kadaster eigendomsinformatie ~€2.85; Koopsom rapport €27 |
| Quirks | **Kadaster Koopsommen** gives full transaction history (paid). NVM "Marktinformatie" sells aggregated agent-side data. **Funda** publishes "Verkocht" listings free. WOZ-waardeloket — public tax-assessed (NOT transacted). |

### 🇧🇪 Belgium

| Field | Value |
|---|---|
| Authority | **Statbel** + AGDP/FPS Finance |
| URL | https://statbel.fgov.be/en/themes/housing/real-estate |
| Mode | aggregate public (median + percentiles); per-property paid |
| Quirks | Statbel publishes **median + Q1/Q3 sale price per commune per quarter** — excellent free granular aggregate. Three regions (FL/WA/Brussels) have separate cadastre access portals. |

### 🇩🇰 Denmark

| Field | Value |
|---|---|
| Authority | **Vurderingsstyrelsen** + **OIS/BBR** |
| URL | https://www.ois.dk/ · https://bbr.dk/ |
| Mode | **fully public open data** |
| Granularity | **address-level** |
| Coverage | **1992 → present** via OIS |
| Cost | free |
| Quirks | One of most transparent regimes alongside UK + NL. **Boliga** (boliga.dk/salg) has free archive with map + filters. Voluntary "family sales" (familiehandel) at 85% rule visible but flagged. |

### 🇮🇸 Iceland

| Field | Value |
|---|---|
| Authority | **HMS / Þjóðskrá** (Registers Iceland → HMS) |
| URL | https://hms.is/ |
| Mode | **fully public** |
| Granularity | **address-level** |
| Coverage | 2006 → present |
| Cost | free |
| Quirks | Tiny market (~6,000 transactions/year) but very transparent. HMS publishes monthly housing index by region. |

### 🇸🇮 Slovenia

| Field | Value |
|---|---|
| Authority | **GURS** |
| URL | https://www.e-prostor.gov.si/ — public **ETN** (Evidenca trga nepremičnin) |
| Mode | **public** (free login; address-level transactions) |
| Granularity | **address + parcel** |
| Lag | 30 days (statutory reporting deadline) |
| Coverage | **2007 → present** |
| Cost | free |
| Quirks | **One of the most granular open transaction registers in CEE** — every sale, lease, exchange must be reported within 30 days. |

### 🇮🇪 Ireland

| Field | Value |
|---|---|
| Authority | **PSRA** |
| URL | https://propertypriceregister.ie/ |
| Mode | **fully public open data** |
| Granularity | **address-level** |
| Coverage | **January 2010 → present** |
| API/CSV | full CSV monthly per county |
| Cost | free |
| Quirks | Includes price, address, date, market/non-market flag, VAT-inclusive flag, new/second-hand, freehold/leasehold. Excludes commercial. Daft.ie + MyHome.ie overlay PPR data. |

### 🇬🇷 Greece

| Field | Value |
|---|---|
| Authority | **AADE** + **Ktimatologio** |
| URL | https://www.ktimatologio.gr/ · https://www.aade.gr/ |
| Mode | partner-only / paid for transactions; **objective values** public |
| Cost | per-extract ~€10–€20 |
| Quirks | **Objective tax value ≠ actual sale price** (historically under-declared). BoG publishes RPPI quarterly. Ktimatologio rollout 2003 → 2025+ still completing. |

### 🇵🇱 Poland

| Field | Value |
|---|---|
| Authority | **GUGiK** — RCiWN (Rejestr Cen i Wartości Nieruchomości) |
| URL | https://dane.gov.pl/ + per-powiat starostwo |
| Mode | aggregated public (NBP + GUS); per-transaction **partner-only** (notaries, valuers, banks) |
| Quirks | **Otodom Insights** + **rynekpierwotny.pl** sell aggregated data. NBP publishes weighted avg + median per major city per quarter. RCiWN per-transaction restricted by law. |

### 🇪🇪 Estonia

| Field | Value |
|---|---|
| Authority | **Maa-amet** |
| URL | https://maaruum.ee/en/land-registry-and-land-valuation/real-estate-transactions/real-estate-transaction-statistics |
| Mode | **fully public open data** |
| Granularity | parcel + cadastral unit |
| Coverage | **2003 → present** |
| Cost | free |
| Quirks | Most digital + transparent property data regime in Baltics. Filterable by type, use, m², year built. |

### 🇭🇷 Croatia

| Field | Value |
|---|---|
| Authority | **DGU** OSS (joint cadastre + land book) |
| URL | https://oss.uredjenazemlja.hr/ |
| Mode | per-property paid; aggregate via Porezna uprava + DZS |
| Cost | zemljišnoknjižni izvadak ~€4 |
| Quirks | Porezna uprava publishes annual transaction values by city for tax purposes. No open transaction-level dataset. |

### 🇭🇺 Hungary

| Field | Value |
|---|---|
| Authority | **Földhivatal** + **KSH** |
| URL | https://www.foldhivatal.hu/ · https://www.ksh.hu/ |
| Mode | aggregate public; per-property paid |
| Cost | tulajdoni lap ~€10 |
| Quirks | **MNB** publishes housing price map down to settlement level. Ingatlan.com publishes sold-price dashboard ("eladott" filter). NAV maintains non-public DB. |

### 🇱🇹 Lithuania

| Field | Value |
|---|---|
| Authority | **Registrų Centras** |
| URL | https://www.registrucentras.lt/ |
| Mode | aggregate public; per-property paid |
| Cost | per-property extract ~€2.90 |
| Quirks | RC quarterly "real estate market overview" gives median + average per municipality per type — strongest free aggregate in Baltics after EE. |

### 🇱🇻 Latvia

| Field | Value |
|---|---|
| Authority | **VZD** |
| URL | https://www.vzd.gov.lv/ · Kadastrs.lv |
| Mode | aggregate public; per-property paid |
| Cost | extract ~€4 |
| Quirks | VZD operates **Nekustamā īpašuma tirgus pārskats** quarterly — free PDF. **Latio** + **Arco Real Estate** publish private market reports. **Lursoft** sells per-property transaction lookup. |

### 🇷🇴 Romania

| Field | Value |
|---|---|
| Authority | **ANCPI** |
| URL | https://www.ancpi.ro/ |
| Mode | per-property paid; aggregate via INS + BNR |
| Cost | extras de carte funciară ~€5 |
| Quirks | **Notarial reference grids** (CNPB minimum values) public + used for tax — these are floors, not actual prices. Imobiliare.ro publishes monthly indices. |

### 🇧🇬 Bulgaria

| Field | Value |
|---|---|
| Authority | **AGKK** + **Imotni Registar** (Justice Min) |
| URL | https://www.cadastre.bg/ · https://portal.registryagency.bg/ |
| Mode | per-property paid; aggregate via NSI + BNB |
| Cost | per-extract ~€2.50–€7.50 |
| Quirks | Sale prices in нотариален акт public via Imotni Registar (per-property lookup). Tax minimum values widely used. |

### 🇱🇺 Luxembourg

| Field | Value |
|---|---|
| Authority | **ACT** + **Observatoire de l'Habitat** (LISER) |
| URL | https://logement.public.lu/fr/observatoire-habitat.html |
| Mode | aggregate public (very granular); per-property paid |
| Granularity | aggregate: **commune-level €/m²** quarterly |
| Cost | extrait cadastral ~€10 |
| Quirks | **Median + Q1/Q3 €/m² per commune per quarter** for both apartments and houses (existing + new build) — extremely granular for such a small country. |

### 🇨🇾 Cyprus

| Field | Value |
|---|---|
| Authority | **DLS** |
| URL | https://portal.dls.moi.gov.cy/ |
| Mode | per-property paid; aggregate via CBC + CyStat |
| Cost | search certificate ~€10 |
| Quirks | Sale prices in transfer deeds — accessible per-property only. **RICS Cyprus** publishes private quarterly index. **TRNC** is separate jurisdiction with no internationally recognized title registry. |

### 🇲🇹 Malta

| Field | Value |
|---|---|
| Authority | **Land Registry** + **NSO** + **CBM** |
| URL | https://nso.gov.mt/ · https://www.centralbankmalta.org/ |
| Mode | aggregate public; per-property paid |
| Cost | search ~€4.66 |
| Quirks | Two parallel indices: CBM advertised (asking) + NSO contract-based (actual deeds). **Many older properties only in Public Registry** (not Land Registry). |

## Western Balkans

### 🇷🇸 Serbia

| Field | Value |
|---|---|
| Authority | **RGZ** |
| URL | https://www.rgz.gov.rs/ |
| Mode | aggregate public via RGZ market reports; per-property paid |
| Lag | annual + semi-annual (~6 months) |
| Cost | list nepokretnosti ~€12 |
| Quirks | RGZ market reports reasonably granular for non-EU country — Belgrade broken to municipality + zone with avg €/m². No open transaction-level dataset. |

### 🇲🇪 Montenegro

| Field | Value |
|---|---|
| Authority | **Uprava za nekretnine** |
| URL | https://www.gov.me/uzn |
| Mode | per-property paid; **NO public aggregate transaction dataset** |
| Cost | list nepokretnosti ~€5 |
| Quirks | MONSTAT publishes construction cost index only. Local agencies (Dr. Real Estate, MaxValues) publish proprietary reports. Coastal vs inland market vastly different. |

### 🇧🇦 Bosnia and Herzegovina

| Field | Value |
|---|---|
| Authority | FBiH + RS-entity + Brčko (3 separate cadastres) |
| URL | https://www.katastar.ba/ · https://www.rgurs.org/ |
| Mode | per-property paid; **NO public aggregate** |
| Cost | extract ~€5 |
| Quirks | **3 parallel land book + cadastre systems**. BHAS publishes construction cost only. Olx.ba + nekretnine.ba are listing-only. |

### 🇲🇰 North Macedonia

| Field | Value |
|---|---|
| Authority | **AKN** |
| URL | https://www.katastar.gov.mk/ |
| Mode | per-property paid; aggregate via SSO |
| Cost | extract ~€4 |
| Quirks | SSO publishes annual avg dwelling sale price by city. AKN provides parcel info via e-Kat. |

### 🇦🇱 Albania

| Field | Value |
|---|---|
| Authority | **ASHK** |
| URL | https://www.ashk.gov.al/ |
| Mode | per-property paid; **NO public sold-price aggregate** |
| Cost | certifikatë pronësie ~€5 |
| Quirks | BoA publishes Tirana housing price index quarterly (broker survey-based, not transaction). INSTAT no transaction price stats. Significant informal market. |

## Anglo non-EU

### 🇨🇦 Canada

| Field | Value |
|---|---|
| Authority | **Provincial land titles** (10 provinces + 3 territories) |
| URLs | ON: OnLand https://www.onland.ca/ · BC: LTSA https://ltsa.ca/ · QC: Registre foncier https://www.registrefoncier.gouv.qc.ca/ · AB: SPIN II https://alta.registries.gov.ab.ca/spinii/ · NS: PROL https://www.novascotia.ca/programs-and-services/land-and-property |
| Mode | per-property paid; aggregate public via CREA |
| Cost | ON ~CAD 30, BC ~CAD 12, QC ~CAD 10 |
| Quirks | **Teranet–National Bank HPI** = canonical national index. **HouseSigma** + **Zolo** scrape MLS sold data for free. BC Land Owner Transparency Registry (LOTR) since 2020. |

### 🇦🇺 Australia

| Field | Value |
|---|---|
| Authority | **State Valuer-Generals + Land Titles Offices** (8 states/territories) |
| URLs | NSW: https://valuation.property.nsw.gov.au/ · VIC: Landata · QLD: Titles QLD · WA: Landgate · SA: SAILIS |
| Mode | per-property paid; aggregate via ABS |
| Cost | NSW ~AUD 25, VIC ~AUD 33, QLD ~AUD 36 |
| Quirks | **NSW publishes free bulk sales data** (annual + weekly CSV) ~150k transactions/yr. VIC/QLD/WA/SA charge per query. **CoreLogic** dominant private aggregator. Domain + realestate.com.au show "Sold" for past 24 months. |

### 🇳🇿 New Zealand

| Field | Value |
|---|---|
| Authority | **LINZ** + **REINZ** |
| URL | https://www.linz.govt.nz/ · https://www.reinz.co.nz/ |
| Mode | LINZ paid; REINZ aggregate paid; council "rating valuations" public |
| Cost | LINZ title search ~NZD 3 (low) |
| Quirks | **homes.co.nz** + **OneRoof** + **Trade Me Property** show estimated values + sale history per address — **best free address-level sold-price proxy**. Council "Capital Value" / Rating Valuation is tax assessment, NOT actual sale price. |

## Latin America

### 🇲🇽 Mexico

| Field | Value |
|---|---|
| Authority | **Registros Públicos de la Propiedad** (32 states + CDMX, no federal) + **SHF** |
| URL | https://www.gob.mx/shf · per-state RPP varies |
| Mode | per-property paid; aggregate via SHF |
| Cost | RPP MXN 100–500 (~€5–25) |
| Quirks | **No federal sold-price registry**. SHF publishes canonical "Índice SHF de Precios de la Vivienda" by city. **Tinsa MX** + **Softec** are private aggregators (paid). State RPPs vary in digitization. **Common practice of under-declaring sale price** vs valor catastral. |

### 🇧🇷 Brazil

| Field | Value |
|---|---|
| Authority | **Cartórios de Registro de Imóveis** (~3,800 nationwide) |
| Federal | **CIB** national rollout 2025–2026 |
| URLs | https://www.onr.org.br/ (ONR — Operador Nacional do Sistema de Registro Eletrônico de Imóveis, instituted by Lei n. 13.465/2017; **SREI is the system ONR operates, not a separate portal** — `registradores.org.br` now terminates on ONR hosting with a `*.onr.org.br` certificate) |
| Mode | per-property paid via cartório or ONR Central Eletrônica |
| Cost | certidão de matrícula ~€10–30 |
| Quirks | **CIB national rollout 2025–2026** aims to standardize. **FIPE-ZAP** = de facto national benchmark (asking, not transacted). **Abrainc-FIPE** covers new-build sold prices in major cities. **ITBI** (municipal transfer tax) records are closest to actual sales — São Paulo's **GeoSampa** includes ITBI declared values per parcel. |

### 🇦🇷 Argentina

| Field | Value |
|---|---|
| Authority | **Registros de la Propiedad Inmueble** (24 provinces, no federal) |
| URLs | RPI BA: https://www.dnrpi.jus.gob.ar/ |
| Mode | per-property paid; **NO reliable public sold-price aggregate** |
| Cost | informe de dominio ~€5–15 |
| Quirks | **No federal sold-price aggregate**. Reporte Inmobiliario + Zonaprop + Argenprop publish asking-price indices. Sale prices historically under-declared (escritura vs USD-cash reality). Most market data quoted in USD/m². Recent dollarization 2024–25 may improve transparency. |

### 🇨🇷 Costa Rica

| Field | Value |
|---|---|
| Authority | **Registro Nacional** |
| URL | https://www.rnp.go.cr/ |
| Mode | per-property paid; **NO public sold-price aggregate** |
| Cost | estudio registral ~€2.50 |
| Quirks | **No public transaction-level dataset**. BCCR publishes construction cost index only. Encuentra24 + Properties Costa Rica are listings only. Significant USD-denominated market for foreign buyers. |

### 🇵🇦 Panama

| Field | Value |
|---|---|
| Authority | **Registro Público** |
| URL | https://www.registro-publico.gob.pa/ |
| Mode | per-property paid; **NO public sold-price aggregate** |
| Cost | certificado de finca ~USD 30 |
| Quirks | **No public sold-price**. MIVIOT + Contraloría publish construction cost only. ACOBIR publishes occasional asking-price reports. USD is local currency — no FX noise. Beneficial-ownership transparency added 2020. |

---

## Summary matrix — transparency tiers

| Tier | Countries | Characteristic |
|---|---|---|
| **A — Open address-level** | UK, IE, DK, IS, EE, SI, FR | Free CSV, address/parcel-level, monthly to semi-annual |
| **B — Open aggregate, paid per-property** | NL, BE, LU, MT, NO, SE, FI, ES, PT, IT, DE, AT, CH, PL, HR, HU, LT, LV, CY, SK, AU (NSW free) | Granular aggregate (commune/postcode/suburb) free; address-level requires extract |
| **C — Per-property paid only, weak aggregate** | CZ, RO, BG, GR, RS, MK, CA (most provinces), AU (most states), NZ, MX, BR (pre-CIB) | Sale price in deed but no open dataset; private aggregators dominate |
| **D — No public sold-price source** | ME, BA, AL, AR, CR, PA | Construction cost or asking-price proxies only |

## Real-terms (inflation-adjusted) historical reconstruction

For the handful of **Tier-A** markets with deep, open, address-level transaction history, a sold-price series can be reconstructed in **real terms** (constant purchasing power) rather than nominal — the most useful long-run signal a buyer can derive from this registry. It is a transparent **computation**, not a new dataset:

1. **Pull the nominal series** from the Tier-A source for the locality (commune / postcode / address): **UK** Price Paid Data (1995 →), **DK** OIS (1992 →), **SI** (2007 →), **IS** (2006 →), **EE** (2003 →), **IE** (Jan 2010 →), **FR** DVF (2014 →). Deep-history sources outside this registry's open-CSV core: **JP** Reinfolib / MLIT (2005 →, free API key), **AU**-NSW free bulk sales CSV.
2. **Deflate by the national CPI / HICP** — use the consumer-price index catalogued per country in `macro.md` (national statistics office / Eurostat HICP). Rebase the CPI to your target year, then compute `real €/m²(t) = nominal €/m²(t) × CPI(target) ÷ CPI(t)`, showing the inputs inline (anti-hallucination computed-number rule). Name the as-of year of each index.
3. **Or skip the recompute** — for cross-country *real* growth, cite the ready-made **BIS Residential Property Price** real series / FRED, already cross-referenced in `price-index-feeds.md` § *BIS / FRED cross-references (international comparable)*, rather than rebuilding what BIS publishes.

**Honest scope**: only ~7–12 of 121 markets have BOTH open address-level *history* AND a clean deflator (the Tier-A set above + KR RTMS, TW actual-price registration, US many-counties). For Tier-B / C / D markets there is **no open transaction-level history to reconstruct** — fall back to the HPI series + BIS real-terms cross-ref in `price-index-feeds.md`; never fabricate a back-series. *(This is the salvaged slice of the rejected `--inflation-adjusted-history` section candidate — a method box here, not a standalone 121-cell section that would duplicate this registry; see ROADMAP decision log 2026-06-13.)*

## Operational notes

- **Cross-check Tier A countries against listings** — sold prices 15%+ below asking are normal in soft markets; >25% suggests distressed or data error
- **For Tier B, build "neighborhood comparable" rather than "address comparable"** — median €/m² of commune/postcode is the legally defensible reference
- **For Tier C, default to a private aggregator** (CoreLogic AU, HouseSigma CA, Tinsa MX, Idealista ES, ImmoUnited AT, Wüest CH) and disclose the data source's commercial nature
- **For Tier D, fall back to construction cost + replacement value methodology** rather than market-comparison; flag this explicitly to the user
- **Lag ≥6 months** (FR DVF, IT OMI, RS RGZ): note current-quarter market may have moved; cross-check against listing-portal trend
- **VAT, transfer tax, "non-arm's-length" exclusions** vary by registry — verify gross-of-tax vs net when comparing across borders

## Anti-hallucination

- **Do NOT fabricate URLs** for D-tier countries
- **Surface the commercial nature** of private aggregators (Wüest, IAZI, FPRE, CoreLogic, Tinsa)
- **Verify VAT-inclusive vs net** before quoting cross-border comparisons
- **Note coverage gaps** explicitly (UK excludes Scotland, FR excludes Alsace-Moselle, etc.)

## Status

Last refreshed: 2026-04-26.
