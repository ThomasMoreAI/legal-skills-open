# Liechtenstein 🇱🇮 — Property Due-Diligence Playbook

ISO2: `li`. Status: ✅ Fully populated (researched 2026-05).

## Country profile

- **Postcode (PLZ)**: 4 digits, Swiss-aligned, range **9485–9498** (`9490` Vaduz, `9494` Schaan, `9495` Triesen, `9493` Mauren, `9485` Nendeln, `9498` Planken)
- **Admin levels**: principality → 11 Gemeinden (no Bezirk/canton tier — 11 communes is the only sub-national layer)
  - Oberland: Vaduz, Triesen, Triesenberg, Balzers, Schaan, Planken
  - Unterland: Eschen, Mauren, Gamprin, Ruggell, Schellenberg
- **Population**: ~40,000 total (Statistik Liechtenstein, 2024 figures via `https://www.llv.li/de/landesverwaltung/amt-fuer-statistik`)
  - Schaan ~6,000; Vaduz (capital) ~5,800; Triesen ~5,400; Balzers ~4,800
  - **~34% foreign nationals** (Swiss, Austrian, German dominant)
- **Currency**: **CHF** (Swiss franc) — currency union with Switzerland under the Customs and Currency Treaty 1923 (Zollvertrag 1923 + Währungsvertrag 1980); SNB monetary policy applies; **no Liechtenstein franc**
- **Language**: German (official); spoken language is **Alemannic dialect** (Liechtensteinerdeutsch) — close to St. Galler / Vorarlberger; written = Hochdeutsch
- **Cadastre**: **Liegenschaftsregister (LREG)** + **Grundbuch** kept centrally by the **Amt für Justiz** (Liechtensteinische Landesverwaltung, Vaduz) — `https://www.llv.li/de/landesverwaltung/amt-fuer-justiz/grundbuch-gb-`
  - **Land-use viewer**: `https://service.geo.llv.li/` (Geodatenportal Liechtenstein)
- **Identifier**: Parzellennummer + Gemeinde
- **Memberships**: **EEA** (since 1995), **Schengen** (since 2011), **EFTA**; **NOT in EU**, NOT in Swiss customs union for goods (Liechtenstein is in EEA single market with CH bilateral overlay)
- **Ownership types**: **Eigentum** (freehold), **Stockwerkeigentum** (condominium under Sachenrecht / SR), **Baurecht** (leasehold ground right)

> ⚠️ **Single biggest deal-killer for foreign buyers**: residential acquisition is governed by the **Grundverkehrsgesetz (GVG, LR 214.11)** — non-residents are effectively excluded from buying residential property; even EEA/EU residents need Liechtenstein domicile + permit + commission approval. See `--rental` and "Foreign-buyer rules" below.

## Section: `--price`

### Primary sources

- **Amt für Statistik (AS / Statistik Liechtenstein)**: `https://www.llv.li/de/landesverwaltung/amt-fuer-statistik`
  - Annual **Bautätigkeit + Wohnungsstatistik** (construction + housing stock); residential transaction-price index is **NOT published at the granularity of CH/AT** — small-country sample-size limits
  - Statistisches Jahrbuch (Yearbook) annual: `https://www.llv.li/de/landesverwaltung/amt-fuer-statistik/publikationen-as` (verify exact URL — page restructured 2024)
- **Liechtensteinische Landesbank (LLB) Marktanalyse**: `https://www.llb.li/` — bank publishes occasional Liechtenstein real-estate notes (institutional, not free index)
- **VP Bank Research**: `https://www.vpbank.com/` — wealth-manager market views
- **Amt für Justiz — Grundbuch**: `https://www.llv.li/de/landesverwaltung/amt-fuer-justiz/grundbuch-gb-` — paid Auszug (Grundbuchauszug) for individual parcel sale-price extracts; **no public sale-price API**
- **Cross-reference Swiss data** (St. Galler Rheintal + Werdenberg): Wüest Partner, Comparis, Homegate often used as proxy because catchment is contiguous and price levels track Sarganserland / Werdenberg ±10%

> ⚠️ Liechtenstein does NOT publish a Statistik-Austria-equivalent Häuserpreisindex at quarterly frequency. Aggregate price benchmarks below are **est.** based on cross-border comparables + reported Verkaufsfälle in Statistisches Jahrbuch + sampled listings on homegate.li and llb.li/immo. Verify any specific deal via an Amt für Justiz Grundbuchauszug.

### Listing platforms

- **homegate.ch** (Liechtenstein listings appear): `https://www.homegate.ch/kaufen/immobilien/land-liechtenstein/trefferliste`
- **immoscout24.ch** Liechtenstein filter: `https://www.immoscout24.ch/`
- **liewo.li / Vaterland Immo / Volksblatt Immo**: local newspaper portals (`https://www.vaterland.li/`, `https://www.vaterland.li/` ❌ DEPRECATED — primary source removed; verify with Liechtensteiner Vaterland (vaterland.li)) — small inventory, German only
- **Newhome.ch** with LI filter
- Premium agency: **Engel & Völkers Liechtenstein** (Vaduz office), **Marxer Immobilien**, **First Immobilien**

### Price benchmarks (2024-2026, est. — verify per deal)

| Gemeinde | EFH CHF/m² (est.) | Wohnung CHF/m² (est.) |
|---|---:|---:|
| **Vaduz** (capital, central) | ≈ 12,000–18,000 | ≈ 11,000–16,000 |
| **Schaan** | ≈ 10,000–14,000 | ≈ 9,000–13,000 |
| **Triesen** | ≈ 9,000–13,000 | ≈ 8,000–12,000 |
| **Balzers** | ≈ 8,500–12,000 | ≈ 7,500–11,000 |
| **Triesenberg** (mountain, view) | ≈ 9,500–14,000 | ≈ 8,500–13,000 |
| **Eschen / Mauren** (Unterland) | ≈ 8,000–11,500 | ≈ 7,500–11,000 |
| **Ruggell / Schellenberg** (north Unterland) | ≈ 7,500–10,500 | ≈ 7,000–10,000 |
| **Planken** (smallest, alpine) | ≈ 9,000–13,000 | scarce inventory |

> Source: cross-tabulated from homegate.ch LI listings (2025-2026) + LLB market notes + adjacent CH Werdenberg/Sarganserland Wüest Partner data. **Liechtenstein property is among the most expensive per m² in Europe**, broadly comparable to Zürich-region tier-2 communes; small lot supply + GVG demand-restriction + tax-resident affluence drive scarcity premium. `(per listings — verify with the Amt für Justiz + bank appraisal on visit)`

### Compute

1. CHF/m² = listing CHF / **Wohnfläche** (BGF or Nettowohnfläche per Schweizerische Norm SIA 416 — same conventions as CH)
2. **Trap**: Stockwerkeigentum **Wertquote** (share %) determines Erneuerungsfonds + voting weight; verify in Begründungsurkunde
3. **Trap**: Liechtenstein appraisals often use **Realwert** (replacement cost) + **Ertragswert** (income value) blend per LLB / VP Bank standard — list price may exceed banker's appraised lendable value
4. Cross-check against St. Galler Rheintal Comparis index for the parallel Swiss commune (e.g., Vaduz ≈ Sevelen / Buchs SG +10–20% premium)
5. **Verkaufsfälle** counts in Statistisches Jahrbuch ≈ 200–350 transactions/yr nationally — **thin market**, single comparable deals can swing benchmarks materially

---

## Section: `--traffic`

### Primary sources

- **Amt für Bau und Infrastruktur (ABI)**: `https://www.llv.li/de/landesverwaltung/abi` — operates Liechtenstein road network + traffic counts (Verkehrszählungen)
  - Verkehrsdaten viewer linked from ABI; granularity is per-counting-station, ~30 permanent + rotating stations
- **Cross-border**: Vorarlberg Land Tirol (`https://vmobil.at/` AT side), Kanton St. Gallen Tiefbauamt CH side — Liechtenstein commuter traffic spills onto adjacent Swiss/Austrian arterials
- **Geodatenportal**: `https://service.geo.llv.li/` — road class layer
- **OSM `highway` class** as universal fallback

### Key term

**DTV (Durchschnittlicher täglicher Verkehr)** = AADT-equivalent (same convention as CH). ABI publishes Werktag-DTV (weekday) + JDTV (annual) for principal roads.

### Verdict bands

- 🟢 < 1,000 v/d (Wohnstrasse, Quartierstrasse, Bergstrasse Triesenberg/Planken)
- 🟡 1,000–8,000 v/d (Gemeindestrassen, Sammelstrassen)
- 🟠 8,000–20,000 v/d (Landstrasse — e.g., Vaduzer Strasse Schaan-Vaduz axis)
- 🔴 > 20,000 v/d (cross-border feeder Schaan-Buchs, Tunnel Gnalp, peak ABI counts on Vaduz-Triesen B16)

> Liechtenstein has **no autobahn**; the Schaan-Vaduz-Triesen axis is the heaviest corridor (~25–30k DTV peaks per ABI counts, last published 2023 series — verify current at `https://www.llv.li/de/landesverwaltung/abi`). Cross-border Schaan→Buchs SG via Rheinbrücke is a chronic peak-hour bottleneck.

---

## Section: `--tax`

### Annual property tax — taxed via WEALTH TAX, not standalone

**Liechtenstein has NO standalone Grundsteuer / Liegenschaftssteuer.** Real estate is folded into the **Vermögenssteuer** base.

```
Vermögenssteuer base = Steuerwert (cadastral value) of property
Sollertrag = 4 % × Steuerwert (notional yield)
Sollertrag is added to taxable INCOME and taxed under Erwerbssteuer
```

- **Legal basis**: Steuergesetz (SteG, LR 640.0), Art. 14 Vermögenssteuer / Art. 15 Sollertrag — `https://www.gesetze.li/konso/2010.340`
- **Mechanism**:
  1. Property is included in net wealth (Vermögen)
  2. 4% of net wealth is treated as **notional income (Sollertrag)** and taxed at the personal income-tax (Erwerbssteuer) rate
  3. Effective annual property "tax" = roughly **0.05–0.15%** of cadastral value, depending on Erwerbssteuer marginal rate (state + Gemeinde) — typically much lower than market value because Steuerwert << market
- **Erwerbssteuer rates 2026**: state progressive 1–8% + **Gemeindezuschlag** (commune surcharge) 150–250% of state tax → effective combined top **~22.4%** (Vaduz/Schaan low-tax communes; some communes higher)
  - Per-Gemeinde Steuerzuschlag table updated annually: `https://www.llv.li/de/landesverwaltung/steuerverwaltung`
- **Verification**: ask seller for last **Steuerveranlagung** (assessment notice) to see Steuerwert + applied Sollertrag

> ⚠️ Steuerwert is set by the **Steuerschätzung** (cadastral appraisal) and is typically substantially below market value. Practical effective annual property tax is among the **lowest in Europe** for owners of average residential property — primary fiscal cost is the Sollertrag×Erwerbssteuer combination, not a property tax in the usual sense. Verify: Steuerverwaltung `https://www.llv.li/de/landesverwaltung/steuerverwaltung`.

### Transaction taxes — Handänderungsabgabe

- **Handänderungsabgabe (transfer fee)**: nominally **1.0%** of purchase price for residential, paid by buyer (or split per contract); Gemeinden may set own rate but typical practice is 1.0% — verify per Gemeinde
  - Some Gemeinden levy partial fee 0.5%; **always confirm with the Gemeindesteueramt** of the property's commune
- **Grundbuch-Eintragungsgebühr (registration fee)**: **6 ‰ (0.6 %) of the consideration** — of the Steuerschätzwert where there is none — **minimum CHF 200 per Handänderung**, per the Grundbuch- und Handelsregistergebührenverordnung (GbHr-GebV, LR 214.011, Fassung 01.08.2024, Anhang 1 B(a)), levied by the **Amt für Justiz** (2024 tariff in force, source Lilex LR 214.011; 2026-09-18 verified) — [ordinance text](https://www.gesetze.li/konso/2003067000)
- **Notar / Rechtsanwalt**: notarial deed is **NOT mandatory** for property transfer in Liechtenstein (unlike CH/AT/DE). Sale contract can be private (Schriftlichkeitsgebot per § 481 ABGB-LI / Sachenrecht), then submitted to the Amt für Justiz. **A Rechtsanwalt is in practice always engaged** for drafting + GVG application — fees typically 0.5–1.5% of price; regulated by Liechtensteiner Rechtsanwaltskammer schedule (`https://www.lirak.li/`)
- **Maklerprovision**: typically 2–3% (often seller-paid, no Bestellerprinzip statute as in AT/CH) — verify in Mäklervertrag

### Total transaction cost (buyer side, est.)

- **Handänderungsabgabe** ~1.0% + **Eintragungsgebühr** ~0.3–0.5% + **Anwalt** 0.5–1.5% + GVG application **CHF 200–800** + Maklerprovision (if buyer-side) 0–3% = **est. ~2–6% of price**
- **Significantly lower than AT (~9–11%) or DE (~10–13%)** — lowest band in DACH region for the transaction itself; the GVG approval barrier is the *real* foreign-buyer cost (see "Foreign-buyer rules")

### MwSt. (VAT)

- **Liechtenstein is in Swiss VAT zone** (Zollvertrag) — Mehrwertsteuersatz Schweiz applies: **8.1% standard** (since 2024), **2.6% reduced**
- Residential rent and resale residential: **VAT exempt**
- New-build sale: typically VAT-exempt for residential (commercial different)
- Verification: **Liechtensteinische Steuerverwaltung** + ESTV CH

### Capital gains — Grundstücksgewinnsteuer

- **Grundstücksgewinnsteuer** (Art. 35-43 SteG): tax on capital gains from real-estate sale.
- **Rate structure** (no holding-period adjustment in statute — the regime is gain-size-progressive, NOT holding-period-degressive): **Tarif Art. 19 Bst. a SteG** progressive bands on the taxable gain after **CHF 15,000 Grundfreibetrag** + Anlagekosten deductions: 1 % bottom (CHF 15-20k slice) → 8 % top (gain > CHF 200k). Then **200 % Zuschlag** per **Art. 43 SteG** → effective top marginal ≈ **8 % × 3 = 24 %** at the top bracket only. (2026-05-27 verified, source Steuerverwaltung Merkblatt Grundstücksgewinnsteuer gültig ab 2013-06-01 + Art. 35-43 SteG.)
- **Steueraufschub grounds (Art. 36 SteG, closed catalog)**: inheritance / Erbvorbezug / gift; Güterzusammenlegung / Baulandumlegung / Grenzbereinigungen; Art. 52 restructurings; spouse transfers. **No general owner-occupier Ersatzbeschaffungs-Aufschub** in the statute — the "Swiss kantonale 2-year reinvestment rollover" concept was NOT adopted in the 2010 SteG; verify any reinvestment scenario directly with Steuerverwaltung. (2026-05-27 verified — supersedes prior wording.)
- Source: Steuerverwaltung Merkblatt — `https://www.llv.li/de/landesverwaltung/steuerverwaltung`; SteG primary text [gesetze.li/konso/2010.340](https://www.gesetze.li/konso/2010.340).

### Future risk

- **Steuerschätzung modernisation**: ongoing technical revaluation of Steuerwerte under SteG amendments — could moderately raise Vermögenssteuer base; not a large reform on the public horizon for 2026
- **Erbschafts-/Schenkungssteuer abolished entirely on 1 January 2011** (SteG 2011 reform) — applies to all degrees of relation, not only direct line. In their place, **Widmungssteuer** applies to asset endowments into Liechtenstein Stiftung / Anstalt / Trust vehicles — verify with Steuerverwaltung if the planning structure uses these vehicles. (2026-05-27 verified, source PwC Widmungsbesteuerung in Liechtenstein + de.wikipedia Erbschaftsteuer.)
- Watch: OECD Pillar Two minimum-tax effects on Liechtenstein corporate base could indirectly affect property-investment vehicles (Stiftung / Anstalt), not direct ownership

---

## Section: `--rental`

### Long-term residential

- Governed by **§ 1090 ff. ABGB-LI** (Mietrecht in the Liechtenstein ABGB) and the **Mietrechts-Sonderbestimmungen** in special provisions; **less prescriptive than Swiss Mietrecht des OR**, no Mietzinsindex / Richtwertmietzins-style caps — predominantly free-market with general civil-law balance + ordre public
- Tenant protection: standard Kündigungsfristen (3 months residential), no Mietpreiskontrolle equivalent, but Wuchergrenze applies
- Deposit (Kaution): typically 2–3 monthly rents, escrow account customary

### Short-let (Ferienwohnung / Airbnb)

- **Beherbergungsverordnung** + **Gewerbegesetz**: short-let activity that is *gewerbsmässig* (commercial — recurring, marketed, hotel-style services) requires **Gewerbebewilligung (Patent)** from the **Amt für Volkswirtschaft (AVW)** — `https://www.llv.li/de/landesverwaltung/avw`
- Occasional / private letting of own residence is generally tolerated without patent under threshold (no formal night-cap law equivalent to Vienna 90 days as of 2026 — verify with Gemeinde + AVW)
- **Tourismusabgabe / Kurtaxe**: Liechtenstein Marketing levies a per-night Beherbergungsabgabe; small flat amount per overnight (CHF ~2/night typical) — verify at `https://tourismus.li/`
- **WEG / Stockwerkeigentum**: condominium short-let frequently restricted by Hausordnung — verify Reglement before assuming legal Airbnb is possible
- **Realistic constraint**: Liechtenstein is a small, residential-character country; the GVG regime + foreign-buyer ban means a non-resident can rarely **own** a unit to short-let in the first place, making the question moot for most international buyers

### Tax treatment

- Rental income is **Erwerbseinkommen** under SteG → progressive Erwerbssteuer + Gemeindezuschlag
- Deductible: maintenance, mortgage interest, depreciation per SteG schedule
- VAT: residential long-let exempt; short-let above commercial threshold may trigger CH MwSt registration

---

## Section: `--work=<profession>`

### Job platforms

- **Jobs.li**: `https://www.jobs.li/` — Liechtenstein-specific
- **Job-Room (AHV-IV-FAK Liechtenstein)**: state job exchange — `https://www.llv.li/de/landesverwaltung/avw/arbeit-und-arbeitslosigkeit`
- **Cross-border**: jobs.ch + xing.com regularly used; ~50% of LI workforce **commutes from CH/AT/DE** (Grenzgänger)
- LinkedIn LI

### Self-employment

- **Selbständigerwerbende**: register at **AHV (Liechtensteinische Alters- und Hinterlassenenversicherung)** — `https://www.ahv.li/`
- **Gewerbeschein / Patent** required for most regulated trades — issued by **Amt für Volkswirtschaft (AVW)**
- **AHV/IV/FAK** social-insurance contributions mandatory; rates aligned with Swiss model (Liechtenstein has its own institution but similar parameters)
- **GmbH (Gesellschaft mit beschränkter Haftung)**: min CHF 30,000 capital
- **AG**: min CHF 50,000 capital
- **Anstalt + Stiftung + Treuhänderschaft**: Liechtenstein-specific vehicles — popular for asset-holding, NOT typical operating company; regulated by **FMA Liechtenstein** for fiduciary services (`https://www.fma-li.li/`)

### Salary benchmarks (2025-2026, est.)

- Liechtenstein **median monthly gross**: ≈ CHF 7,500–8,500 (Statistik Liechtenstein 2024 Lohnstatistik — verify exact at `https://www.llv.li/de/landesverwaltung/amt-fuer-statistik`)
- **Finance / banking** (LLB, VP Bank, LGT, Bank Frick): premium — senior CHF 12,000–25,000+/month
- **Industry** (Hilti HQ in Schaan, Hilcona, Ivoclar, ThyssenKrupp Presta, Hoval): solid CHF 6,500–9,500/month median
- **Public sector**: per Lohngesetz tariff
- **No statutory minimum wage** — collective bargaining + market levels set floors
- Income tax: see `--tax` (combined ~22% top in low-tax Gemeinden)

### Cultural quirks

- Strong fiduciary-services + private-banking sector + industrial export niche (Hilti world-leading power tools); **mismatch** between premium incomes + housing scarcity drives the price/wage divergence
- Most workers commute **into** Liechtenstein from CH/AT — buying property as a non-resident commuter is **not** legal (GVG bar)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **Amt für Bevölkerungsschutz (ABS)** | `https://www.llv.li/de/landesverwaltung/abs` | Civil protection, hazard mapping coordination |
| **Geodatenportal** | `https://service.geo.llv.li/` | Gefahrenkarten Hochwasser / Lawinen / Rutschungen layers |
| **Hochwasserschutz Rhein (IRR)** — Internationale Rheinregulierung | `https://www.rheinregulierung.org/` | Rhine flood-risk + dyke programme (CH/AT/LI joint) |
| **MeteoSwiss** (Liechtenstein has no national met office) | `https://www.meteoswiss.admin.ch/` | Climate, precipitation, wind |
| **SED (Schweizerischer Erdbebendienst, ETH Zürich)** | `https://www.seismo.ethz.ch/` | Seismic hazard — covers LI as part of CH catalog |
| **SLF** (Institut für Schnee- und Lawinenforschung) | `https://www.slf.ch/` | Avalanche zones — applicable to LI alpine slopes |

### Specific risks

- **Hochwasser (flooding)** — **primary natural risk**:
  - **Rhein (Rhine)** west boundary: dyked under IRR programme; design event ~Q300 dyke standard but historic 1927 event overtopped; ongoing Rhein-Erhöhung works (joint AT-CH project, 2030+ horizon)
  - **Binnenkanal + Esche + Spiersbach**: internal drainages — local flash-flood risk in Unterland (Eschen, Mauren, Ruggell)
  - Flood maps via Geodatenportal Liechtenstein
- **Lawinen (avalanches)**: **Triesenberg, Malbun, Steg** alpine slopes; SLF/Liechtenstein hazard zoning enforced — Bauverbot in Roten Zonen
- **Murgang / Hangmuren** (mudflows / landslides): Triesenberg + alpine slopes after heavy rain
- **Steinschlag (rockfall)**: Drei-Schwestern + Falknis slopes
- **Earthquake**: **low-to-moderate** — LI is in the same seismotectonic zone as eastern Switzerland; PGA per SED national hazard map ≈ 0.6–1.0 m/s² (475-yr return), comparable to Vaduz/St. Gallen; **no major historical destructive event** in country boundaries
- **Hagel + Sturm**: increasing trend (alpine-foothills hailstreak vulnerability); building insurance covers
- **Radon**: parts of Triesenberg + alpine substrate elevated; the Liechtenstein **Strahlenschutzkommission** + **Amt für Umwelt (AU)** reference data — `https://www.llv.li/de/landesverwaltung/au`. Reference value 300 Bq/m³ aligned with EU-BSS

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1945** | Lead pipes, asbestos in roofs (later additions), Holzbalkendecken, low thermal envelope |
| **1945–1980** | Eternit / Asbestos-Zement roofs widespread, lead, low insulation, single-pane glass |
| **1980–2005** | Phasing out asbestos, basic insulation; Polychlorbiphenyle (PCB) in joint sealants |
| **Post-2008** | SIA-norms (Swiss SIA 380/1 thermal) increasingly applied; better envelope |
| **Post-2017** | Stricter energy-performance standards aligned with **Energiegesetz (EnG-LI, LR 730.0)** + EU EED transposition |

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energieausweis (GEAK-equivalent)** | Required at sale + new build per Energiegesetz (EnG-LI); aligned with Swiss GEAK methodology | 10 years |
| **Grundbuchauszug** | Verify Eigentum + Lasten (Servituten, Pfandrechte) | At sale |
| **GVG-Bewilligung** (if foreign buyer) | Mandatory **before** transfer registration | Per transaction |
| **Stockwerkeigentums-Begründungsurkunde + Reglement** | If condominium | At sale |
| **Lageplan (situation plan)** + Gebäudeversicherungs-Auszug | Boundaries + insurance value | At sale |
| **Schadstoffbericht** (if pre-1990) | Asbestos, PCB, lead | Recommended; required for renovation permits |

### Climate change projections

- Liechtenstein climate projections inherit from **NCCS Switzerland** (CH-2018 scenarios) — applicable via MeteoSwiss
- **+1.5–4.0 °C by 2050** (CH-2018, RCP2.6 to RCP8.5)
- More extreme rainfall + flood-risk pressure on Rhein dykes + Binnenkanal
- **Snow line rising**: Malbun ski (1,600 m base) marginal in low-snow scenarios; alpine snow days declining
- Heatwaves in Rheintal lowland increasing (urban heat in Vaduz / Schaan)

---

## Section: `--mains`

### Sources

- **Each Gemeinde** runs its own Wasserversorgung + Abwasserentsorgung (11 communes = 11 utilities) — most populated areas universally served
- **Liechtensteinische Gas- und Versorgungs AG (LGV / LKW Group)**: gas + electricity — `https://www.lgv.li/` and `https://www.lkw.li/`
- **Liechtensteinische Kraftwerke (LKW)**: electricity DSO (state-owned)
- **Internet/fibre**: **Telecom Liechtenstein (FL1)**, **CableCom**; FTTH near-universal in valley communes by 2024
- **Geodatenportal** layer "Werkleitungskataster" (utilities cadastre) for parcel-level service map

### Verification

- Most populated areas: kommunale mains **universal** — no individual verification typically needed
- Alpine huts, isolated parcels in Triesenberg / Malbun: independent systems (Hauskläranlage, Quellfassung) possible
- **Anschlussbescheid** (connection certificate) requested at sale via Gemeindebauamt
- For new connections: Anschlussgebühr CHF 5,000–15,000 typical for water + sewer combined (verify per Gemeinde)

### Costs

| Scenario | Cost (CHF, est.) |
|---|---:|
| Anschlussgebühr Wasser + Abwasser (new build) | 5,000–15,000 (Gemeinde-set) |
| Hauskläranlage (small, isolated) | 12,000–25,000 |
| Annual Wassergebühr | typically CHF 300–800 residential |
| Annual Abwassergebühr | typically CHF 400–1,000 residential |

---

## Section: `--crime`

See `shared/crime-sources.md`. Liechtenstein-specific:

- **Landespolizei (Liechtenstein National Police)**: `https://www.landespolizei.li/`
- **Polizeiliche Kriminalstatistik (PKS)**: published annually, available from Landespolizei + Statistik Liechtenstein
- **Population ~40,000** → small absolute numbers; **statistical noise** is significant — single events shift YoY rates dramatically. Prefer 5-year averages.
- **Headline**: among the **lowest crime rates in Europe** — typical residential burglary count ~50–100/yr nationally; violent crime very rare
- For comparison vs national average use `shared/crime-sources.md` template; expect 🟢 verdict band for nearly all communes

---

## Section: `--amenities`

Universal — see `shared/amenities-osm.md`. Liechtenstein notes:

- Dominant supermarket chain: **Migros LI** (Schaan, Vaduz, Eschen, Triesen, Balzers), **Coop**, **Denner**, **SPAR** (Aldi / Lidl absent — entered Schaan 2023+ with Lidl pilot, verify currency)
- DIY: **Bauhaus Schaan**, **HG Commerciale**
- Pharmacy: **Apotheke** branding (German); branches in each major Gemeinde
- Primary care: **Hausarzt** network listed at `https://www.aerztekammer.li/`
- Hospital: **Landesspital Liechtenstein** (Vaduz) — `https://www.landesspital.li/` — small (~30 beds); secondary/tertiary care typically referred to **Kantonsspital St. Gallen** or **Universitätsspital Zürich** under cross-border treaties
- Schools: state Primarschulen + Sekundarschulen + Liechtensteinisches Gymnasium (Vaduz)
- Public transport: **LIEmobil** (national bus) — `https://www.liemobil.li/`; **NO railway station inside Liechtenstein** (sole stop is **Schaan-Vaduz** on the Buchs SG ↔ Feldkirch ÖBB line, served sparsely); for rail use **Buchs SG (CH)** or **Sargans (CH)** or **Feldkirch (AT)**

---

## Section: `--climate`

Universal — see `shared/climate-projections.md`. Liechtenstein-specific override:

- **MeteoSwiss** is the de-facto met service; LI has no national equivalent → use CH-2018 / NCCS scenarios as primary
- Köppen-Geiger: **Cfb** (oceanic, alpine-modified) in valley; **Dfc / ET** at altitude
- Föhn (alpine wind) effects — winter warming events
- Snow-line + glacial retreat: relevant for Malbun ski + alpine huts on Sarganserland-side slopes
- **Rhein flood multipliers** under climate change: see `--risks`

---

## Cost benchmarks (LI 2026, indicative — CHF)

| Work | Cost (CHF, est.) |
|---|---:|
| Energieausweis (GEAK-equivalent) | 800–1,500 |
| Anwalt (Vertrag + GVG-Antrag) | 0.5–1.5% of price |
| Handänderungsabgabe | ~1.0% of price |
| Eintragungsgebühr Grundbuch | ~0.3–0.5% |
| GVG application fee | 200–800 |
| Maklerprovision (often seller-paid) | 2–3% |
| **Total transaction cost (buyer side)** | **~2–6% of price** |
| Asbestsanierung (small house) | 30,000–80,000 |
| Energetische Sanierung (Klasse C → A) | 100,000–250,000 (LI building costs ≈ Zürich tier) |
| Lawinenschutz alpine | varies — by Triesenberg site |
| Heizungstausch (Wärmepumpe) inkl. Förderung | 30,000–55,000 |
| Dachsanierung 200 m² | 35,000–70,000 |

> Liechtenstein construction-cost level is among the **highest in Europe** — comparable to Zürich tier; small construction-firm market + Swiss labour rates apply.

## Active fiscal incentives (2025-2026)

- **Energieförderung Liechtenstein** (state energy subsidies): per Energiegesetz EnG-LI — grants for Wärmepumpe, Photovoltaik, Sanierung; portal at `https://www.llv.li/de/landesverwaltung/au` (Amt für Umwelt) → Energie + Klimaschutz
- **Photovoltaik Förderung**: typically CHF 200–400/kWp installed (verify current Förderbeiträge)
- **Wärmepumpe Förderung**: CHF 4,000–10,000 typical
- **Sanierung Förderung Hülle/Fenster**: per m² rates
- **Klimaplan 2030**: national climate strategy — `https://www.llv.li/` (search "Klimaplan 2030")
- **NO standalone first-time-buyer tax credit** (no Bëllegen-Akt-equivalent); Erwerbssteuer-residency benefits apply broadly

## Foreign-buyer rules — the deal-killer section

### Grundverkehrsgesetz (GVG, LR 214.11) — the primary regulatory gate

Liechtenstein's **Grundverkehrsgesetz** is the single most restrictive residential-property regime in continental Europe (CH Lex Koller is the closest cousin, but LI is **stricter**).

- **Statute**: Grundverkehrsgesetz (GVG) — Liechtensteinisches Landesgesetzblatt LR 214.11; consolidated text at `https://www.gesetze.li/konso/2009.025`
- **Approving body**: **Grundverkehrskommission (GVK)** — operates under the Regierung; decisions published periodically
- **Coverage**: applies to **all transfers** (purchase, exchange, gift, inheritance with non-LI heirs, long-term lease >5 yr) of residential + agricultural land

### Eligibility tiers

| Buyer | Status |
|---|---|
| **Liechtenstein citizens (Landesbürger) with domicile in LI** | Free to acquire — notification only |
| **EEA nationals (incl. CH)** with **active LI residence permit + domicile** | Eligible after notification + GVG approval (routine if conditions met) |
| **EEA nationals NOT resident in LI** | Effectively **NOT eligible** — must demonstrate "particular Liechtenstein connection" (besonderes Interesse, e.g., business presence, family) — vetted case-by-case; **rare grants** |
| **Non-EEA nationals (e.g., US, UK, GCC, AS)** | **Effectively excluded** from residential acquisition. Special permits exist for state-interest cases (typically NOT granted to private individuals). Only inheritance + marriage routes are practically open |

> The GVG also requires a **declared intent to occupy** (Selbstnutzung) for residential purchases; pure investment ownership by non-resident foreigners is essentially blocked.

#### GVG-approved acquisition — quantitative cap

Where the Grundverkehrsbehörde (Amt für Justiz, Abteilung Grundverkehr) grants approval based on **berechtigtes Interesse** (Wohnbedarf / Erholungsbedarf / Bauwesen-Interesse per Art. 6 GVG), the **quantitative cap** is:

- **One baureifes Grundstück, maximum 1,440 m²** (= 400 Klafter² historic measure) — for a single residential building, **PLUS**
- **One condominium unit (Stockwerkeigentumseinheit)**, OR alternatively **two condominium units instead of the building plot**.

Source: **Art. 6 GVG** (LR 214.11, [gesetze.li/konso/1993.049](https://www.gesetze.li/konso/1993.049)) + **GVO 2007** (LR 214.111, [gesetze.li/konso/pdf/2007168000](https://www.gesetze.li/konso/pdf/2007168000?version=5)). Without justified interest, exemptions exist for: spouses, registered partners, blood relatives (direct line or up to 3rd-degree collateral), value-equal property exchanges, inheritance / will / forced sales. (2026-05-27 verified, source jwt.li Grundverkehrsrecht overview + primary GVG text.)

### Residency: NOT linked to property

- **Residency in Liechtenstein is QUOTA-based, NOT investment-based** — there is **no golden visa** in any form
- **Annual quota** under the **Personenfreizügigkeitsgesetz (PFZG)** + Verordnung: ~**56 permits/year** total, split:
  - ~28 EEA permits via **Auslosung (lottery)** (approx half drawn by lot, half by Regierungsentscheid for "wirtschaftliches Interesse")
  - ~17 third-country permits
  - Verify current quota at **Ausländer- und Passamt (APA)** — `https://www.llv.li/de/landesverwaltung/apa`
- **No investment-based residency programme** exists. Wealthy applicants sometimes apply for a **Spezialbewilligung** (special permit on grounds of significant economic / fiscal interest to Liechtenstein) under PFZG — extremely rare in practice
- **Schengen movement**: LI is in Schengen — but Liechtenstein **residence permit** is the gating right, not Schengen visa

### Inheritance + marriage routes

- **Erbgang (inheritance)**: real estate can pass cross-border to non-resident heirs; the heir then has limited time to either move into LI residency or **resell** to an eligible buyer (typically 2 years)
- **Marriage to a Landesbürger / resident**: spouse becomes eligible after fulfilling residence + permit requirements

### Practical implication

For nearly all international buyers without an existing Liechtenstein residence permit, the answer to "can I buy a Liechtenstein house?" is **no**. The regulatory bar — not price, not tax — is the binding constraint. Confirm GVK approval feasibility **before** deal-stage diligence; pursuing diligence on a property you cannot legally acquire wastes time and money.

> **Verification**: any serious enquiry must start with a **conditional GVG application** routed through a Liechtensteiner Rechtsanwalt. Decisions of the Grundverkehrskommission are published; the Anwalt can pre-test feasibility against current case law before the buyer commits to a deal.

## Common listing platforms

- **Homegate.ch** (LI filter) — broadest inventory
- **ImmoScout24.ch** (LI filter)
- **Vaterland Immo, Volksblatt Immo** — local newspaper portals (German)
- **Engel & Völkers Liechtenstein**, **Marxer Immobilien**, **First Immobilien** — agencies
- **LLB / VP Bank Immobilienbörse** — bank-affiliated listings (occasional)
- **Notariat-listed auction sales** via **Landgericht Vaduz** (Zwangsversteigerung) — rare

## Caveats unique to LI

- **GVG is the single biggest non-price barrier** to foreign acquisition — see "Foreign-buyer rules"
- **Currency union with CH (no LI-issued franc)**: SNB monetary policy applies; CHF strength affects EUR-denominated buyers
- **No standalone property tax** — property folded into Vermögenssteuer / Sollertrag-mechanism; effective annual fiscal burden is **modest**
- **No notary-mandate for transfer** (unlike CH/AT/DE) — but in practice always go through a Rechtsanwalt
- **No Erbschafts-/Schenkungssteuer** in direct line — favourable for inheritance planning
- **No statutory minimum wage**; high median income vs European context
- **Bauernhof / landwirtschaftliches Eigentum**: agricultural land has additional bäuerliches Bodenrecht-style restrictions — separate GVG agricultural track
- **Stiftung / Anstalt / Treuhänderschaft**: Liechtenstein-specific legal vehicles for asset-holding — historically used for cross-border estate-planning; **NOT a route around GVG** for residential property (GVG looks through the legal vehicle for residential-acquisition control)
- **Statistik Liechtenstein limitations**: small-country sample sizes mean published price/transaction series are thin — cross-reference Swiss Werdenberg / Sarganserland data
- **Rail: only Schaan-Vaduz** on the Buchs SG–Feldkirch ÖBB line (RegioExpress) — most travel is road; Bus LIEmobil is the spine of public transport
- **Cross-border worker dynamics**: ~50% of LI workforce is Grenzgänger from CH/AT/DE — they push housing demand in adjacent CH/AT communes (Buchs SG, Feldkirch), not in Liechtenstein
- **Liechtenstein has no airport**; nearest international = **Zürich (ZRH, ~85 km)** + **Friedrichshafen DE (FDH, ~50 km)** + **St. Gallen-Altenrhein (ACH, ~50 km)**

## Reddit / forum sources

- **r/europe**, **r/Switzerland** (Liechtenstein-specific subs are very small)
- **Vaterland.li** + **Volksblatt.li** comment sections
- Expat: **InterNations Liechtenstein chapter**, **The Local Switzerland** occasional LI coverage
- **LinkedIn LI community groups** (financial-services + Hilti / Ivoclar employee networks) for first-hand commute / housing data

## Verification authorities

| Authority | When to call |
|---|---|
| **Amt für Justiz — Grundbuch** | Title verification, encumbrances — `https://www.llv.li/de/landesverwaltung/amt-fuer-justiz/grundbuch-gb-` |
| **Grundverkehrskommission (GVK)** | GVG approval (foreign-buyer feasibility) |
| **Ausländer- und Passamt (APA)** | Residence permits / quotas — `https://www.llv.li/de/landesverwaltung/apa` |
| **Steuerverwaltung** | Vermögenssteuer / Sollertrag / Erwerbssteuer — `https://www.llv.li/de/landesverwaltung/steuerverwaltung` |
| **Amt für Umwelt (AU)** | Radon, environmental hazards, energy subsidies — `https://www.llv.li/de/landesverwaltung/au` |
| **Amt für Bau und Infrastruktur (ABI)** | Building permits, road traffic — `https://www.llv.li/de/landesverwaltung/abi` |
| **Amt für Volkswirtschaft (AVW)** | Gewerbe (commercial use), short-let business permit — `https://www.llv.li/de/landesverwaltung/avw` |
| **Gemeindebauamt** (Vaduz / Schaan / Triesen / etc.) | Zonenplan, Anschluss, local permits |
| **Liechtensteinische Rechtsanwaltskammer (LiRAK)** | Anwalt directory — `https://www.lirak.li/` |
| **Landesspital + Ärztekammer** | Medical-services verification |
| **Landespolizei** | Crime stats — `https://www.landespolizei.li/` |
| **FMA Liechtenstein** | Banking / fiduciary regulation (relevant for Stiftung/Anstalt vehicles) — `https://www.fma-li.li/` |

## Quirks to know

- **Parzellennummer + Gemeinde** = the canonical property identifier (PLZ + street is often insufficient for register pulls)
- **Grundbuchauszug** sections (Liechtenstein follows the Sachenrecht structure modelled on Swiss ZGB): Hauptbuch + Tagebuch + Beilagen — request all three
- **Servituten** (easements): Wegrecht, Wohnrecht, Niessbrauch — common; verify via the Amt für Justiz
- **Vorkaufsrecht** (preemption) sometimes attached, especially family-line agricultural parcels
- **Stockwerkeigentum Wertquote** allocates Erneuerungsfonds + voting rights — read the Begründungsurkunde + Reglement
- **Currency reality**: list prices ALWAYS in CHF; mortgage offers from LLB / VP Bank in CHF; EUR-denominated foreign buyer carries FX exposure
- **Mortgage practice (banks)**: LLB, VP Bank, Bank Frick — typical max LTV **80% for residents**, **50–65% for non-residents** (where GVG even allows acquisition); CHF rates trail SNB policy rate; affordability calculations align with FINMA guidelines (used by reference even though LI has its own FMA)
- **No private mortgages enforceable against third parties without Grundbuch entry** (Grundpfandverschreibung)
- **Inheritance**: Erbrecht under ABGB-LI; **Pflichtteil** preserved (forced heirship for spouses + descendants)
- **Cross-border CH-LI legal interplay**: many tax + civil rules mirror CH; bilateral agreements (e.g., 2015 LI-CH double-tax treaty) govern income + asset coordination

## Source URL templates

| Source | URL pattern |
|---|---|
| Amt für Justiz — Grundbuch | `https://www.llv.li/de/landesverwaltung/amt-fuer-justiz/grundbuch-gb-` |
| Geodatenportal | `https://service.geo.llv.li/` |
| Statistik Liechtenstein | `https://www.llv.li/de/landesverwaltung/amt-fuer-statistik` |
| Steuerverwaltung | `https://www.llv.li/de/landesverwaltung/steuerverwaltung` |
| Amt für Bau und Infrastruktur | `https://www.llv.li/de/landesverwaltung/abi` |
| Amt für Umwelt | `https://www.llv.li/de/landesverwaltung/au` |
| Ausländer- und Passamt | `https://www.llv.li/de/landesverwaltung/apa` |
| Amt für Volkswirtschaft | `https://www.llv.li/de/landesverwaltung/avw` |
| Gesetzesdatenbank | `https://www.gesetze.li/` |
| Regierung Liechtenstein | `https://www.regierung.li/` |
| Landespolizei | `https://www.landespolizei.li/` |
| LiRAK Anwaltskammer | `https://www.lirak.li/` |
| FMA Liechtenstein | `https://www.fma-li.li/` |
| Tourismus Liechtenstein | `https://tourismus.li/` |
| LIEmobil (transport) | `https://www.liemobil.li/` |
| Homegate (LI filter) | `https://www.homegate.ch/kaufen/immobilien/land-liechtenstein/trefferliste` |
| ImmoScout24 (LI filter) | `https://www.immoscout24.ch/` |
| MeteoSwiss | `https://www.meteoswiss.admin.ch/` |
| SED Earthquake | `https://www.seismo.ethz.ch/` |
| SLF Avalanche | `https://www.slf.ch/` |
| Internationale Rheinregulierung | `https://www.rheinregulierung.org/` |

## Status

**Confidence**: MEDIUM — HIGH on foundational legal/fiscal framework (Grundstücksgewinnsteuer Tarif Art. 19 Bst. a SteG + 200% Zuschlag Art. 43 SteG with no holding-period adjustment in statute, Erbschafts-/Schenkungssteuer abolished entirely 1 Jan 2011 across all relations, Widmungssteuer on Stiftung endowments, GVG Art. 6 + GVO 2007 foreign-acquisition cap 1,440 m² + 1 building OR 2 condos, CHF currency via 1980 monetary agreement). MEDIUM on Ersatzbeschaffung relief (Art. 36 SteG closed-catalog reading — no 2-yr rollover available for private real estate), Bank Frick + LLB mortgage-list current product mix (verify at point of analysis), and population / foreign-share datapoints. LOW on residential listing-price currentness (thin market, low transaction volume — pull current asking at point of analysis).

**Last verified**: 2026-05-27 (Grundbuch registration fee and registry authority corrected 2026-09-18 per Lilex LR 214.011)

**Researched by**: Sonnet 4.6 + Opus 4.7 (parallel-subagent batch, 2026-05)

**Notes**: For 95%+ of international buyers the **Grundverkehrsgesetz (GVG, LR 214.11) approval gate is the binding deal-killer** — non-resident foreigners are effectively barred from residential acquisition regardless of price/tax fundamentals; only EEA nationals with active Liechtenstein residence permit + domicile, or rare "particular Liechtenstein connection" cases, clear the Grundverkehrskommission. Residency itself is quota-based via lottery (~28 EEA + ~17 third-country permits/year per APA) with no investment-track equivalent to Monaco/Andorra. Tax + transaction costs are modest (no standalone property tax; property folded into Vermögenssteuer/Sollertrag; ~2–6% buyer transaction cost) and absolute price levels are Zürich-tier — but the legal/permission bar dominates. Primary-source confidence is HIGH for GVG/quotas/tax structure (gesetze.li + llv.li); MEDIUM for granular per-Gemeinde €/m² benchmarks (no STATEC-grade quarterly index — small-country sample limit means ranges are est. and cross-referenced against adjacent CH Werdenberg/Sarganserland Wüest Partner data — verify any specific deal via an Amt für Justiz Grundbuchauszug + bank appraisal).

## Extension TODOs

- [ ] Per-Gemeinde Gemeindezuschlag table (annual) for Erwerbssteuer effective rate
- [ ] Per-Gemeinde Handänderungsabgabe rate (where it deviates from 1.0%)
- [ ] GVK published-decisions corpus → "particular Liechtenstein connection" interpretation guide
- [ ] APA quota lottery historic outcomes (Auslosung yields/year) for residency-route diligence
- [ ] LI-specific Stockwerkeigentum-Reglement red-flag heuristics (tighter than CH)
- [ ] Energieförderung subsidy schedule (annual updates)
- [ ] Cross-border Werdenberg/Sarganserland ↔ LI price-spread tracking for proxy benchmarking
