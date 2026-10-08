# Switzerland 🇨🇭 — Property Due-Diligence Playbook

ISO2: `ch`. Status: ✅ Fully populated (researched 2026-04; Tier-A quarterly refresh 2026-07-03 — fast-moving claims re-verified, structural sections unchanged).

## Country profile

- **Postcode (PLZ/NPA)**: 4 digits (`8001` Zürich, `1201` Genève, `4001` Basel)
- **Admin levels**: 26 cantons (high autonomy) + 2,100+ communes (Gemeinden / communes)
- **Currency**: **CHF** (Swiss franc); 1 EUR ≈ 0.95 CHF (variable, often near parity)
- **Languages**: German (62 %), French (23 %), Italian (8 %), Romansh (0.5 %); 4 official
- **Cadastre**: cantonal Grundbuch + **swisstopo** (Bundesamt für Landestopografie)
- **Identifier**: Grundbuchblatt-Nummer + Liegenschafts-Nr. per commune
- **Federal structure** — most rules are cantonal; **massive variation** across 26 systems
- **Switzerland is NOT in EU** (just EEA-adjacent through bilateral agreements)
- Distinct ownership types: **Eigentum** (freehold), **Stockwerkeigentum** (commonhold apartment, since 1965), **Bauernrecht/Baurecht** (leasehold ground)

## Section: `--price`

### Primary sources

- **Comparis** (consumer aggregator): `https://en.comparis.ch/immobilien`
- **Homegate** (largest listings): `https://www.homegate.ch/`
- **ImmoScout24.ch**: `https://www.immoscout24.ch/`
- **Wüest Partner Marktanalysen**: `https://www.wuestpartner.com/`
- **Fahrländer Partner**: `https://www.fpre.ch/`
- **Newhome.ch**, **RealAdvisor**
- **BFS (Bundesamt für Statistik)** Wohnkostenindex + Immobilienpreisindex: `https://www.bfs.admin.ch/`
- **SNB (Swiss National Bank)** financial stability reports + quarterly monetary-policy assessments (policy rate 0% since Jun 2025, held 18 Jun 2026 and 24 Sep 2026): `https://www.snb.ch/en/publications/communication/press-releases-restricted/pre_20260924` (2026-09-24 verified)
- **Cantonal Grundbuchämter** for actual sale-price extracts (paid)

### Listing/agency networks

- **UBS, ZKB, Raiffeisen**: bank-affiliated brokerage
- **Engel & Völkers Schweiz, Sotheby's**: premium
- **Properstar**, **ApartHotel**

### Price benchmarks (2025-2026)

> est. ranges aggregated from Comparis / Homegate / ImmoScout24 asking-price listings 2025-2026 (see Primary sources, L21-29) — asking, not transaction; verify with cantonal Grundbuchamt sale-price extracts.
>
> Market direction (BFS IMPI Q1 2026, Q4-2019 = 100): +4.7 % YoY, +1.5 % QoQ to 126.8 points; urban communes of large agglomerations +3.1 % QoQ, small-agglomeration / non-agglomeration towns flat. Asking ranges below trend upward. (2026-07-03, per BFS release of 30 Apr 2026 via SRF/AWP)

| Region | EFH €/m² (CHF) | Wohnung €/m² (CHF) |
|---|---:|---:|
| **Zürich City** | 14,000–22,000 | 14,000–25,000 |
| **Genève** | 13,000–20,000 | 13,000–22,000 |
| **Zug** | 14,000–20,000 | 14,000–22,000 |
| **Basel** | 9,000–14,000 | 9,000–15,000 |
| **Bern** | 7,000–11,000 | 7,500–12,000 |
| **Lausanne** | 9,500–14,000 | 10,000–15,000 |
| **Lugano** | 7,500–12,000 | 8,000–14,000 |
| **St. Gallen** | 6,000–9,000 | 6,500–10,000 |
| Rural alpine | 4,000–8,000 | 4,500–10,000 (resort towns higher) |

### Compute

1. Price/m² = listing CHF / Wohnfläche (per Bauberufe)
2. **Trap**: NWF (Nettowohnfläche) vs BGF (Bruttogeschossfläche) vs HNF (Hauptnutzfläche)
3. **Trap**: Stockwerkeigentum has Wertquote (share %) determining Hauseigentum-Beteiligung — important
4. Compare to canton-specific Wüest Partner / Comparis index

---

## Section: `--traffic`

### Sources

- **ASTRA (Bundesamt für Strassen)** — federal roads + autobahnen: `https://www.astra.admin.ch/`
- Cantonal Tiefbauämter — state roads
- Major cities: Zürich Gemeinde Verkehrsamt, Genève direction des routes, etc.

### Key term

**DTV (Durchschnittlicher täglicher Verkehr)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (Wohnstrasse, Bergstrasse)
- 🟡 1,000–8,000 v/d (Kantonsstrasse, Stadtstrasse)
- 🟠 8,000–30,000 v/d (Hauptstrasse, urban arterial)
- 🔴 > 30,000 v/d (Autobahn N1/A1, urban core, Stadtumfahrung)

---

## Section: `--tax`

### MAJOR REFORM 2025: Eigenmietwert ABOLISHED

**Federal popular vote 28 September 2025 → 57.7 % YES** to abolish Eigenmietwert (imputed rental value taxation on owner-occupied homes).

- **Implementation: FIXED 1 January 2029** — the Federal Council set the entry-into-force date at its **1 April 2026** session; a 2028 start is off the table (2029 was chosen so cantons *can* introduce the linked second-home Objektsteuer simultaneously). Owner-occupied maintenance deductions + federal energy/environment deductions fall away from the same date; rented/leased property keeps the maintenance deduction; time- and amount-limited Ersterwerberabzug (mortgage-interest deduction) for first-time buyers. (2026-07-03 verified, source [admin.ch Medienmitteilung 1 Apr 2026](https://www.admin.ch/de/newnsb/yGTqBPowRqyVh0zPokW-q))
- Applies to **primary AND secondary residences**
- Owner-occupiers no longer declare notional rental income
- **BUT**: deductions for maintenance/renovations also eliminated
- **Cantons can introduce special property tax on second homes** (constitutional change passed alongside)
- Regional split: French-speaking cantons all voted NO; German-speaking (except Basel-Stadt) voted YES

### Annual property tax — before + from 2029

**Until 31 Dec 2028 (current)**:
- **Eigenmietwert** (imputed rental income): typically 60–70 % of market rental → added to taxable income → ~10–35 % tax depending on canton + commune
- **Liegenschaftssteuer** (cantonal property tax) — exists in some cantons:
  - **Genève**: 0.05–0.3 % of valeur fiscale
  - **Vaud**: 0.05–0.1 %
  - **Tessin/Ticino**: 0.025–0.075 %
  - **Zürich, Bern, Aargau, Schwyz**: NO Liegenschaftssteuer
  - Most cantons: low to moderate
- **Vermögenssteuer** (wealth tax): cantonal + communal; property included; ~0.13–0.85 % on net wealth (varies hugely)
- **Eigenmietwert + Vermögenssteuer** combined **est. ~0.5–1.5 %** of property value/yr for owner-occupiers (model composite of the Eigenmietwert income-tax effect (L97) + Vermögenssteuer (L104) — illustrative, canton- and income-dependent; verify per canton)

**From 1 Jan 2029 (after Eigenmietwert abolition)**:
- No more Eigenmietwert imputed income
- Vermögenssteuer continues
- New **cantonal property tax on second homes** likely (each canton decides)
- Many alpine cantons (Wallis, Graubünden, Tessin) likely introduce strong second-home tax

### Transaction taxes

**Handänderungssteuer** (transfer tax) — cantonal, varies massively:

> Rates per cantonal Steuerverwaltung schedules; rows without an inline cite below are unverified for as-of year — verify per canton (cantonal Steuerverwaltung). Vaud (L125) and Neuchâtel (L126) carry inline source + verified date.

| Canton | Rate |
|---|---:|
| **Zürich** | **0 %** (abolished 2005) |
| **Schwyz** | **0 %** |
| **Bern** | **1.8 %** |
| **Basel-Land** | 2.5 % |
| **Basel-Stadt** | 3.0 % |
| **Genève** | **3.0 %** + 0.4 % registration |
| **Vaud** | **2.2 % cantonal + up to 1.1 % communal Zuschlag** (max 3.3 % combined; varies by commune) (2026-05-27 verified, source PBM Avocats + immobilienverkauf-rechner) |
| **Neuchâtel** | **3.3 %** (buyer-paid) (2026-05-27 added — was missing) |
| **Wallis** | 1.5 % |
| **Ticino** | 1.5 % + minor fees |

**Notarkosten + Grundbuchgebühr**: 0.5–1.5 % typical
**Maklerprovision**: 2–3 %, usually paid by seller

### Total transaction cost (buyer side)

- **0–6 %** depending on canton — Zürich is among lowest in EU/Western Europe
- Vaud, Genève, BS: **~5–7 %**
- Zürich, Schwyz: **~1–2 %** (no Handänderungssteuer)

### MwSt. (VAT)

- 8.1 % standard (raised from 7.7 % in 2024)
- 3.8 % special rate (Beherbergung / hotel + short-let accommodation)
- 2.6 % reduced (food, books)
- Real estate: residential exempt; commercial 8.1 %
- **Pending increase** to part-fund the 13th AHV pension (Parliament final vote 19 Jun 2026): standard 8.1 → 8.5 %, Beherbergung 3.8 → 4.0 %, reduced 2.6 % unchanged; subject to a mandatory popular vote expected 29 Nov 2026 (BSV: *voraussichtlich*), unlikely in force before 2028. (2026-07-03 verified, source [BSV umsetzung-13-ahv-rente](https://www.bsv.admin.ch/de/umsetzung-13-ahv-rente))

### Capital gains — Grundstückgewinnsteuer

- **Cantonal**, varies by holding period
- est. ~25–50 % at short holding, tapering to ~5–10 % after 20+ years (cantonal — illustrative range, varies widely by canton; verify with the cantonal Steueramt)
- Owner-occupied + reinvestment within 2 yrs often exempt

### Future risk

- **Eigenmietwert abolition** active implementation (1 January 2029, fixed 1 Apr 2026 — see L87 for canonical dates + source) (2026-07-03 verified)
- Cantonal second-home property taxes coming
- Wealth tax rates stable

---

## Section: `--rental`

### Long-term residential

- **Mietrechtliche Vorschriften** (rental law): tenant-protective, esp. Zürich + Genève
- **Mietrecht des OR** (Code of Obligations): caps initial rent in tense markets
- **Anfechtung**: tenants can challenge rent increases
- **Kündigungsschutz**: limited eviction grounds

### Short-let (Ferienwohnung / Airbnb)

**Lex Koller** (Federal Act on the Acquisition of Real Estate by Persons Abroad):
- **Foreign nationals (non-CH residents) face restrictions** on second-home + investment property
- Each canton has annual quota
- **Zweitwohnungsgemeinden** (>20 % second homes) face additional restrictions under the **Zweitwohnungsgesetz (ZWG, in force 1 Jan 2016)**, implementing **Art. 75b BV** (2012 initiative); ARE publishes annual Wohnungsinventar. Lex Koller / BewG quotas: **national annual ceiling 1,500 holiday-home authorisations** to foreign non-residents; max plot **1,000 m²**, max living area **200 m²**; Wallis (Valais) 330/yr (highest); smallest cantons 20/yr. B/C permit holders + Swiss citizens not subject to authorisation. (2026-05-27 verified, source ARE + Engel & Völkers Lex Koller guide)
- **PENDING (consultation CLOSED, not yet law):** On **15 April 2026** the Federal Council opened a Vernehmlassung (consultation CLOSED **15 July 2026**) to *tighten* Lex Koller (BewG) — make main-residence purchases by third-country (non-EU/EFTA) nationals permit-liable (with a duty to sell within 2 years of moving away), restrict holiday-home purchases by persons abroad, ban business-real-estate purchases intended for renting/leasing out (own-use stays permit-free), and for the first time bar persons abroad from buying listed housing-company shares and regularly-traded real-estate fund / SICAV units. Part of the accompanying-measures package the Federal Council adopted in January 2025 alongside its rejection (recommendation to reject) of the «Keine 10-Millionen-Schweiz» initiative — the initiative itself was rejected at the popular vote of 14 June 2026 (45.2 % yes; 8 full cantons yes / 12 no — 2026 data, source BFS OGD federal vote results); the BewG revision is a separate bill and continues. Separately, the Nationalrat adopted point 1 of SVP motion 24.3961 (broader rollback of BewG relaxations; Federal Council proposed rejection) on 22 Sep 2026 (123-54-17 per Tages-Anzeiger, secondary) and the motion now sits with the Ständerat committee (source parlament.ch Curia Vista 24.3961) — motion only, no bill. **Consultation closed on schedule 15 Jul 2026; submissions (Kantone/Parteien/Organisationen) published 27 Jul 2026; Federal Council now evaluating — no Ergebnisbericht/Botschaft yet.** Consultation → Botschaft → Parliament → optional referendum: NOT enacted; monitor. (2026-08-05 verified, source [admin.ch Medienmitteilung 15 Apr 2026](https://www.admin.ch/de/newnsb/4mzivVX5Ko4dpap06YtuI) + [bj.admin.ch Revision Lex Koller](https://www.bj.admin.ch/de/revision-lex-koller))

**Cantonal patente cantonale** required in many cantons (Genève, Vaud, Zürich):
- Application + tourism tax + safety inspection
- Geneva: max 90 days/yr without commercial license
- Zürich: tightening 2024-2025

**Tax treatment**:
- Income tax + Mehrwertsteuer (8.1 %) above threshold
- Tourist tax per canton/commune (Kurtaxe): CHF 2-5/night/person typical

### Strategic notes

- **Lex Koller restricts foreign buyers** of second homes — major regulatory hurdle
- **Zweitwohnungsinitiative** (2012): max 20 % second homes per Gemeinde — pop. cap
- **Imputed rent abolition** (1 January 2029, fixed 1 Apr 2026 — see L87) changes investment math significantly
- High purchase costs (Vaud, Genève) eat margins

---

## Section: `--work=<profession>`

### Job platforms

- **jobs.ch** (largest)
- **jobup.ch** (French-speaking CH)
- **LinkedIn CH**, **Indeed.ch**, **JobScout24**, **Stepstone.ch**
- **Bundeskanzlei Karriere** (federal): `https://www.admin.ch/`
- Cantonal employment offices

### Self-employment

- **Selbstständigerwerbende** (sole trader): register at AHV-Ausgleichskasse
- **AHV/IV/EO** contributions mandatory
- **Pensionskasse** (BVG) typically not for self-employed
- **GmbH**: min CHF 20,000 capital
- **AG (Aktiengesellschaft)**: min CHF 100,000 capital, 50,000 paid

### Salary benchmarks (2025)

- Median monthly gross:
  - Zürich, Genève: ~CHF 7,000-8,500
  - Bern, Basel: ~CHF 6,500-7,500
  - Smaller cities: ~CHF 5,500-6,500
- **Mindestlohn**: no national floor; statutory cantonal minima (1 Jan 2026, indexed annually — verify at cantonal source): Genève ~CHF 24.59/hr, Basel-Stadt ~CHF 22.20, Jura ~CHF 21.40, Neuchâtel ~CHF 21.35, Ticino ~CHF 20.00–20.50 (tiered by sector); Stadt Luzern city-level minimum since 2026 (est. ~CHF 22.00–22.75 — sources disagree, verify); other cantons none (sectoral GAV minima may still apply)

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **GUNA Naturgefahrenkarte** (federal) | `https://www.naturgefahren.ch/` | Aggregated alpine + general hazards |
| **swisstopo** | `https://www.swisstopo.admin.ch/` | Geological + topographic + cadastre |
| **swisseo Earthquake hazard** | `https://www.seismo.ethz.ch/` | ETH Zürich Schweizer Erdbebendienst |
| **GIRRES Bundesamt für Umwelt** | `https://www.bafu.admin.ch/` | Environment + flood + landslide |
| **Lawinen** SLF (Institut für Schnee- und Lawinenforschung) | `https://www.slf.ch/` | Avalanche zones |
| **Cantonal Naturgefahrenkarten** | per canton geoportal | Detailed parcel-level hazards |
| **GEOview** (Berner Oberland, etc.) | per canton | Alpine specifics |

### Specific risks

- **Lawinen** (avalanches) — major risk in alpine areas (VS, GR, BE, GL, UR, OW, NW, TI)
  - SLF zones: red (high), blue (medium), white (none)
- **Hochwasser** — Rhein, Aare, Rhone, Reuss, Limmat valleys
- **Erdrutsch / Murgang** (landslide / mudflow) — widespread in mountainous regions
- **Steinschlag** (rockfall) — alpine slopes
- **Permafrost-Schmelze** — alpine foundations affected by permafrost retreat
- **Earthquake** — moderate:
  - **Wallis** + **Basel** highest seismic hazard
  - **Engadin, Ticino, Graubünden** elevated
  - 1356 Basel quake M 6.2 historical reference
- **Hagel** (hail) — increasing damage Mittelland
- **Sturm** — Atlantic + Föhn (alpine wind)

### Build-era hazards

- Pre-1945: lead, asbestos, no thermal envelope, slate roofs
- 1945–1989: asbestos very common, low insulation
- 1990–2010: improving; **MuKEn** (Mustervorschriften der Kantone im Energiebereich) phasing in
- Post-2014 MuKEn 2014: stricter
- Post-2020 MuKEn 2020: nZEB-equivalent

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **GEAK (Gebäudeenergieausweis der Kantone)** | All sales since 2018-2025 (varies canton); some cantons strictly require | 10 years |
| **Grundbuchauszug** | Verify owner + Lasten | At sale |
| **Pläne (Lageplan, Grundriss, Schnitte)** | Standard | At sale |
| **Stockwerkeigentumsreglement + Hausordnung** | If condo | At sale |
| **Schadstoffbericht** | If pre-1990 building (asbestos, PCB, radon) | Recommended |
| **Servitut-Auszug** | Easements | At sale |

### Climate change projections

- +1.0–4.5 °C by 2050 (CH-2018, NCCS scenarios)
- Glacial retreat: significant loss of Alpine ice
- Snow line rising: skiing affected at lower altitudes
- More extreme rainfall + flood events
- Heat waves: Mittelland affected

---

## Section: `--mains`

### Sources

- Each Gemeinde has Wasserversorgung + Abwasserentsorgung
- Major: Wasserversorgung Zürich (WVZ), Industrielle Werke Basel (IWB), SIG Genève (Services Industriels)
- Universal in populated areas; alpine huts on independent systems

### Verification

- Most populated areas: kommunale mains universal
- Alpine Maiensässe / Berghütten: Hauskläranlage / Senkgrube
- **Anschlussbescheid** required at sale

---

## Cost benchmarks (CH 2026, indicative)

| Work | Cost (CHF) |
|---|---:|
| GEAK | 800–1,500 |
| Notar + Grundbuch | 0.5–1.5 % of price |
| Handänderungssteuer | 0–3.3 % (cantonal) |
| Maklerprovision (seller-paid typically) | 2–3 % |
| **Total transaction cost (buyer)** | **1–6 %** |
| Asbestsanierung (small house) | 30,000–80,000 |
| Energetische Sanierung (Klasse C → A) | 80,000–200,000 |
| Erdbebenverstärkung | 50,000–150,000 |
| Lawinenschutz alpine | varies massively |
| Permafrost foundation upgrade | 100,000–300,000 |
| Roof in Alpine zone (slate) | 30,000–80,000 |

## Active fiscal incentives (2025-2026)

- **Gebäudeprogramm** (federal energy retrofit subsidies)
- **Förderprogramm Klima- und Energiefonds** per canton — varies massively
- **Steuerabzug Energetische Sanierung**: deductible from cantonal income tax
- **Wärmepumpe Förderung** per canton
- **Mietkredit** in some cantons for eligible buyers

## Common listing platforms

- **Homegate** — biggest, full extraction
- **ImmoScout24.ch** — premium + standard
- **Comparis** — aggregator across platforms
- **Newhome** — agency-driven
- **Acheter-Louer.ch** — French-speaking CH
- **Immobilien Tessin / Immobiliare.ch** — Italian-speaking

## Caveats unique to CH

- **Lex Koller restricts foreign buyers** of residential second homes — major issue for non-CH/EU residents
- **Zweitwohnungsinitiative 20 % cap** in many alpine + tourist Gemeinden
- **Eigenmietwert ABOLITION** (1 January 2029, fixed 1 Apr 2026 — see L87) changes ROI math for owner-occupiers
- **Stockwerkeigentum** since 1965 — most apartments; verify Wertquote + Reglement
- **Bauernhof + Bäuerliches Bodenrecht** (BGBB): special restrictions on agricultural property
- **Permafrost-Risiko** for high-alpine builds
- **MuKEn 2020/2025** drives thermal renovation mandates
- **Cantonal patchwork**: 26 different tax + planning systems
- **Federal popular vote** can change rules quickly (Eigenmietwert 2025 example)
- **Erbrecht** different per canton + family law
- **CHF currency** strong but volatile vs EUR; affects foreign-buyer purchasing power
- **No EU but EEA-adjacent** — bilateral agreements complex

## Reddit / forum sources

- **r/Switzerland**, **r/Zurich**, **r/Geneva**, **r/SwissPersonalFinance**
- **20 Minuten forum**, **Cash.ch**
- Expat: **The Local Switzerland**, **English Forum Switzerland**
- **Comparis Tipps + Tricks** community

## Verification authorities

| Authority | When to call |
|---|---|
| **Cantonal Grundbuchamt** | Title verification, encumbrances |
| **Gemeinde Bauamt** | Permits, Zonenplan, Bauakt history |
| **Steueramt (kantonal + Gemeinde)** | Liegenschaftssteuer, Eigenmietwert (until abolition — 1 Jan 2029, fixed 1 Apr 2026) |
| **Notar (Notariat) per canton** | Final transfer, Grundbuch eintragung |
| **Wasserwerk Gemeinde** | Mains drains verification |
| **Schweizerischer Erdbebendienst (SED)** | Seismic info |
| **SLF** | Avalanche zones |
| **Cantonal Naturgefahrenfachstelle** | Hazard verification |
| **STWE-Verwaltung (condo)** | Hausgeld, Erneuerungsfonds, Beschlüsse |

## Quirks to know

- **Wertquote in Stockwerkeigentum** allocates Erneuerungsfonds + voting rights
- **Grundbuchauszug Hauptregister + Stammgrundbuch + Tagebuch** — different parts
- **Servitut** (easements) common; Wegrecht, Wohnrecht, Niessbrauch
- **Vorkaufsrecht** (preemption) sometimes attached
- **Nutzniessung** (usufruct) often in inheritance situations
- **NABEG** (Nutzungsbeschränkungen) cantonal restrictions
- **Notar role**: in CH, notar handles Grundbuch directly (no separate solicitor)
- **Bauernhöfe** require agricultural-residence proof (BGBB)
- **Almhütten + Maiensässe** usually with Bauernrecht

## Source URL templates

| Source | URL pattern |
|---|---|
| Comparis | `https://en.comparis.ch/immobilien` |
| Homegate | `https://www.homegate.ch/` |
| ImmoScout24.ch | `https://www.immoscout24.ch/` |
| swisstopo | `https://www.swisstopo.admin.ch/` |
| Naturgefahren.ch | `https://www.naturgefahren.ch/` |
| swisseo Earthquake | `https://www.seismo.ethz.ch/` |
| SLF Avalanche | `https://www.slf.ch/` |
| BFS Wohnungsdaten | `https://www.bfs.admin.ch/` |
| Wüest Partner | `https://www.wuestpartner.com/` |
| Gebäudeprogramm | `https://www.dasgebaeudeprogramm.ch/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-08-05 (Lex Koller BewG consultation re-verified — closed 15 Jul 2026, submissions published 27 Jul, not enacted; balance of 2026-07-03 Tier-A refresh unchanged). SNB 24 Sep 2026 policy-rate hold re-verified 2026-09-24 in the October regwatch wave. Rental / foreign-buyer tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (post-2025 Eigenmietwert vote definitive; SLF + Naturgefahren well-maintained). MEDIUM for short-let regulation (Lex Koller stable but cantonal patente updates ongoing); HIGH for the 2029 Eigenmietwert implementation roadmap (fixed 1 Apr 2026).

## Extension TODOs

- [ ] Per-canton Liegenschaftssteuer + Vermögenssteuer rate tables
- [ ] Lex Koller cantonal quotas + foreign-buyer eligibility per residence status
- [ ] Zweitwohnungsinitiative quota per Gemeinde (alpine focus)
- [ ] Per-canton Handänderungssteuer + notar fee structures
- [ ] Eigenmietwert 2029 implementation tracking (each canton's adaptation)
- [ ] Cantonal second-home property tax adoption tracking
- [ ] STWE Reglement + Erneuerungsfonds health check heuristics
