# Austria 🇦🇹 — Property Due-Diligence Playbook

ISO2: `at`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (PLZ)**: 4 digits (`1010` Wien Innere Stadt, `4020` Linz, `5020` Salzburg, `6020` Innsbruck)
- **Admin levels**: 9 Bundesländer → 95 Bezirke → 2,093 Gemeinden
- **Currency**: EUR (€)
- **Languages**: German (Hochdeutsch + dialects); minorities: Slovene (Kärnten), Hungarian (Burgenland), Croatian (Burgenland), Czech (Wien)
- **Cadastre**: **BEV (Bundesamt für Eich- und Vermessungswesen)** + **Grundbuch** (Justice ministry)
- **Identifier**: Einlagezahl (EZ) + Katastralgemeinde + Grundstücksnummer
- **CRITICAL**: Federal structure — most rules harmonized but **Wohnbauförderung + Naturschutz vary by Bundesland**
- Distinct ownership types: **Eigentum** (freehold), **Wohnungseigentum** (condominium under WEG 2002), **Mietkauf**, **Baurecht** (leasehold ground)

## Section: `--price`

### Primary sources

- **Statistik Austria Häuserpreisindex (HPI) + OOH PI**:
  - `https://www.statistik.at/statistiken/volkswirtschaft-und-oeffentliche-finanzen/preise-und-preisindizes/haeuserpreisindex-und-ooh-pi`
  - Calculated from Grundbuch contracts; gold-standard
- **OeNB (Österreichische Nationalbank) Wohnimmobilienpreisindex**:
  - `https://www.oenb.at/Statistik/Standardisierte-Tabellen/Preise-Wettbewerbsfaehigkeit/immobilien/wohnimmobilienpreisindex.html`
  - Vienna-specific separate series
- **Statistik Austria Immobilien-Durchschnittspreise**:
  - `https://www.statistik.at/statistiken/volkswirtschaft-und-oeffentliche-finanzen/preise-und-preisindizes/immobilien-durchschnittspreise`
- **Grundbuch (online via Justizportal)**:
  - `https://www.justiz.gv.at/home/service/grundbuch~36.de.html`
  - Paid abrufs (~€14 for Grundbuchauszug per EZ)

### Listing platforms

- **Willhaben.at** — largest: `https://www.willhaben.at/iad/immobilien`
- **ImmobilienScout24.at**: `https://www.immobilienscout24.at/`
- **derStandard Immo**: `https://immobilien.derstandard.at/`
- **Bazar.at**, **Quoka.at** — privates
- Premium: **EHL Immobilien**, **Engel & Völkers AT**, **JP Immobilien** Wien

### 2025 price benchmarks (Statistik Austria + OeNB)

| City / Area | Wohnungen €/m² (2024-2025) | Häuser €/m² |
|---|---:|---:|
| **Wien (Gesamt)** | ~5,000–6,500 | ~4,000–5,500 |
| Wien Innere Bezirke (1./4./7./8./9.) | 8,000–14,000 | n/a (kaum Häuser) |
| **Salzburg** | 5,500–7,500 | 4,500–6,000 |
| **Innsbruck** | 6,000–8,500 | 5,000–7,000 |
| **Graz** | 3,500–5,500 | 3,000–4,500 |
| **Linz** | 3,500–5,000 | 2,800–4,000 |
| **Klagenfurt** | 3,000–4,500 | 2,500–3,500 |
| **Bregenz** | 4,500–6,500 | 3,800–5,500 |
| Rural Bundesländer (NÖ, Burgenland, Kärnten) | 1,500–3,500 | 1,200–2,500 |

National averages 2024 (Statistik Austria):
- **Eigentumswohnung**: 4,000 €/m²
- **Einfamilienhaus**: 2,709 €/m²

### 2025 trend (OeNB)

- 2025 full year (OeNB, press release 29 Jan 2026): nominal **+2.1 % YoY**; real (vs 3.8 % inflation) **≈ −1.7 %** — prices fell in real terms again
- Wien **+2.9 %** vs Austria-ex-Wien **+1.6 %**; new Wien apartments +3.8 %, used +2.8 %
- OeNB Wohnimmobilienpreisindex **272.2 in Q1 2026 (record high)** — market stabilizing/recovering after 2022-24 correction (2026-07-03 verified)

### Compute

1. Listing €/m² = listing price / Wohnnutzfläche (per WEG/Wohnungsgemeinnützigkeitsgesetz)
2. **Trap**: Nutzfläche includes Lager, Keller — check what's counted
3. **Trap**: Quadratmeterpreis vs Pauschalpreis — Vienna Altbau often pauschal
4. Compare to Statistik Austria for the Bezirk
5. Grundbuchauszug needed for definitive ownership + encumbrances

---

## Section: `--traffic`

### Primary sources

- **ASFINAG** — autobahnen + Schnellstraßen: `https://www.asfinag.at/`
- **Bundesländer Verkehrszählung**:
  - Wien Stadtinformation: `https://www.wien.gv.at/`
  - Tirol: `https://www.tirol.gv.at/`
  - OÖ: `https://www.land-oberoesterreich.gv.at/`
  - Each Bundesland has Verkehrsabteilung
- OSM `highway` class fallback

### Key term

**JDTV (Jährlicher durchschnittlicher täglicher Verkehr)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,000 v/d (Wohnstraße, Forststraße)
- 🟡 1,000–8,000 v/d (Landesstraße, Stadtstraße)
- 🟠 8,000–30,000 v/d (Bundesstraße, Stadteinfahrt)
- 🔴 > 30,000 v/d (Autobahn, Schnellstraße, Stadtring)

---

## Section: `--tax`

### Annual property tax — Grundsteuer

**Very low** compared to W. Europe — residential **~€100–€500/yr est.** (derived from the Einheitswert × Steuermesszahl × Hebesatz formula below; verify on the seller's Grundsteuerbescheid).

```
Grundsteuer = Einheitswert × Steuermesszahl × Hebesatz × 1.4 (Bundeszuschlag)
```

- **Einheitswert**: very outdated valuation (mostly 1973 base) — est. ~5–20 % of market value
- **Steuermesszahl**: 0.05 % – 0.2 %
- **Hebesatz**: set by Gemeinde, ~500 % est.
- **Bundeszuschlag**: factor 1.4

### Reform pending

Long-debated Grundsteuerreform — multiple political parties want full revaluation. As of 2026: **not yet enacted**.

### Transaction taxes — Grunderwerbsteuer (GrESt)

**3.5 % flat on price** — same across Austria, no Bundesland variation (§ 7 GrEStG).

**Stufentarif** for *unentgeltliche* / Familienverband transfers (§ 26a GGG; basis = **Grundstückswert**, not Kaufpreis) — 3-band scale:
- **0.5 %** on first **€250,000**
- **2.0 %** on next **€150,000** (€250k–€400k)
- **3.5 %** on excess above **€400,000**

(2026-05-27 verified; source [BMF Steuersatz](https://www.bmf.gv.at/themen/steuern/immobilien-grundstuecke/grunderwerbsteuer/steuersatz.html) + [USP GrESt](https://www.usp.gv.at/themen/steuern-finanzen/weitere-steuern-und-abgaben/grunderwerbsteuer.html))

**Share-deal RETT reform (eff. 1 Jul 2025)**: Anteilsvereinigungs-/share-consolidation threshold dropped from **95 % → 75 %**. Indirect (chain) share consolidations also caught. **Observation period extended 5 → 7 years.** Increased **3.5 % rate on fair-market value (gemeiner Wert)** for share-deal transfers — closes Anteilsvereinigung loophole. Relevant for SPV/GmbH structures. (2026-07-03 verified; source [DLA Piper](https://www.dlapiper.com/en-de/insights/publications/2025/06/new-regime-on-austrian-real-estate-transfer-tax) + [Wolf Theiss](https://www.wolftheiss.com/insights/austria-to-introduce-stricter-real-estate-transfer-tax-rules-for-share-deals/))

### Eintragungsgebühr (Grundbuch entry fee)

**1.1 % of price** — separate fee for Grundbuch registration.

**Hauptwohnsitz-Befreiung (Grundbuch-Eintragungsgebühr) — EXPIRED 30 Jun 2026.** Ran 1 Jul 2024 – 30 Jun 2026 (application had to reach the Grundbuch by 1 Jul 2026): Eintragungsgebühr (1.1 %) + Pfandrechts-Eintragungsgebühr (1.2 %) waived up to **€500,000 Bemessungsgrundlage** for a Hauptwohnsitz purchase. **No extension enacted or planned** (federal govt, May 2026) — the standard 1.1 % + 1.2 % fees now apply again. (2026-07-03 verified; source [BMJ Befreiung](https://www.bmj.gv.at/themen/Zivilrecht/Befreiung-von-der-Grundbuch-Eintragungsgeb%C3%BChr-bei-Erwerb-von-Wohnraum.html))

### Immobilienertragsteuer (ImmoESt)

Special-rate income tax of **30 %** on private property-sale gains (since 1 Jan 2016; was 25 % between 1 Apr 2012 – 31 Dec 2015) — § 30 EStG. No 10-year speculation period since 1 Apr 2012. **Umwidmungszuschlag** of 30 % surcharge applies since **1 Jul 2025** for re-zoned (umgewidmete) properties. Hauptwohnsitzbefreiung (2-yr or 5-of-10-yr tests under § 30 Abs 2 Z 1 EStG) and Herstellerbefreiung are the main relief paths. Altgrundstück (acquired pre-31 Mar 2002) vs Neugrundstück (post) split applies. Selbstberechnung durch Parteienvertreter (Notar/Anwalt). (2026-05-27 verified; source [oesterreich.gv.at ImmoESt](https://www.oesterreich.gv.at/de/themen/steuern_und_finanzen/immobilienertragsteuer/Seite.2420002) + [USP ImmoESt](https://www.usp.gv.at/themen/steuern-finanzen/weitere-steuern-und-abgaben/immobilienertragsteuer.html))

### Notarkosten / Anwaltskosten

- 1.0–2.5 % typical (regulated by RATG)

### Maklerprovision

- Typically 3 % buyer + 3 % seller (excl. VAT 20 %); since 1 Sep 2023, **Bestellerprinzip** in residential — usually paid by who hired

### Total transaction cost (buyer side)

- 3.5 % GrESt + 1.1 % Eintragung + 1.0–2.5 % Notar + 3.6 % Makler = **~9–11 %**

### VAT (USt.)

- 20 % standard
- 10 % reduced (food, books, residential rent)
- New residential property: 20 %; existing: exempt

### Future risk

- **Grundsteuerreform** likely 2026–2028 — could 5–10× annual bills for properties with low Einheitswert
- **Erbschaftsteuer** abolished 2008, but periodic political resurfacing of reintroduction debate
- **Wegzugsbesteuerung** for emigrants

---

## Section: `--rental`

### Long-term residential — MRG categories

**Mietrechtsgesetz (MRG)** divides rentals:
- **Vollanwendung** (full application): pre-1953 buildings, Genossenschaftswohnungen, Gemeindewohnungen → strict rent control + protection
- **Teilanwendung** (partial): post-1953 mostly → indexed rent, max-rent rules
- **Nichtanwendung** (no application): Eigentumswohnungen, single-family homes → free market

### Vienna-specific (most regulated)

- **Wiener Wohnen** (Gemeindewohnungen): ~220,000 units est., regulated rent (verify at wienerwohnen.at)
- **Genossenschaft** (cooperative): regulated rent + Eigenmittel
- **Privatmarkt** Vollanwendung: Richtwertmietzins per Bundesland, max +25 % zone bonus
- **2026 Richtwert Wien: €6.74/m²** (from €6.67, ~+1 % valorization eff. 1 Apr 2026), max +25 % zone bonus. **Mieten-Wertsicherungsgesetz (MieWeG), in force 1 Jan 2026** (via 5. Mietrechtliches Inflationslinderungsgesetz, 5. MILG): caps existing contractual Wertsicherungsklauseln (creates no adjustment right of its own) — regulated MRG rents capped at **1 % (2026), 2 % (2027)**; from 2028, index-linked residential contracts in multi-unit buildings incl. free-market rents pass on only half of any inflation portion above 3 % (e.g. 4.5 % inflation → max 3.75 %); adjustment once/yr, earliest 1 April (Richtwert increases effective 1 May). Excludes Ein-/Zweifamilienhäuser and WGG/Genossenschaft rents (own regime). (2026-07-03 verified)

### Short-term rentals (Ferienwohnung / Airbnb)

**Wien**:
- **Wiener Bauordnungsnovelle 2023** (short-let limits city-wide from 1 Jul 2024): max 90 days per calendar year for temporary short-let of a dwelling without giving up one's residence (legal persons cannot use the 90-day allowance); above that, outside a Wohnzone only with an Ausnahmebewilligung under § 129 Abs 1a BO limited to five years, inside a Wohnzone only as a Beherbergungsstätte after an Umwidmung under § 7a Abs 5 BO (2026 data, source MA 37 Merkblatt Kurzzeitvermietung + Stadt Wien press release 2026-09-19); registration number planned from 1 Jan 2027 under the WKVRG (announced, not yet enacted — see STR-VO note below)
- WEG approval typically required
- Penalty: up to €50,000

**Salzburg, Innsbruck**: similar restrictions

**EU 2024/1028 (STR-VO)**: Austria has NOT opted in — the Wirtschaftsministerium (BMWET) confirms the STR-VO is applied in **no Bundesland as of its 20 May 2026 start date** ("vorerst"); no national STR registration-number regime, though individual Länder may opt in later (BMWET is building the Single Digital Entry Point). Short-let stays governed by each Land's Bauordnung. **Wien is opting in**: Stadt Wien announced on 19 Sep 2026 a new Wiener Kurzzeitvermietungsregistergesetz (WKVRG), built on the EU regulation, to be passed by the Wiener Landtag in November 2026 and in force **1 Jan 2027** (hosts already listing: transition to the end of Q1 2027). Every platform host would need a registration number and platforms could only list Wien dwellings that have one; fines up to €50,000 per violation, minimum €2,000 for repeat offences. Announced, not yet enacted (source [Stadt Wien press release 2026-09-19](https://presse.wien.gv.at/presse/2026/09/19/buergermeister-ludwig-wien-ist-vorbild-beim-schutz-von-leistbaren-wohnungen-fuer-die-bevoelkerung)). (2026-07-03 verified; source [BMWET STR-VO](https://www.bmwet.gv.at/Themen/Tourismus/Tourismus-in-Oesterreich/Rechtliches/kurzzeitvermietung_str_vo.html))

### Tax treatment

- **§ 28 EStG (Vermietung & Verpachtung)** for non-commercial private rental
- **Gewerbliche Vermietung**: Gewerbesteuer + Sozialversicherung (SVS) if hotel-style services
- VAT: 10 % reduced for short-stay accommodation
- **Tourismusabgabe**: per night, set by Gemeinde (Wien ~€3.50/night/person)

---

## Section: `--work=<profession>`

### Job platforms

- **AMS (Arbeitsmarktservice)**: `https://www.ams.at/`
- **karriere.at**, **stepstone.at**, **LinkedIn AT**, **derStandard Karriere**
- **Bundeskanzleramt Karriere** (public sector): `https://www.bka.gv.at/`

### Self-employment regimes

- **Selbstständig (Gewerbeschein)**: standard self-employed; **SVS** (Sozialversicherung der Selbstständigen) mandatory
  - 2025 min. Beitragsgrundlage: ~€7,824/yr → ~€1,680/yr SVS minimum
- **Neue Selbstständige**: § 109a EStG, pension+health via SVS
- **Freier Beruf** (liberal): doctors, lawyers, architects — own Kammern + own Sozialversicherung
- **GmbH**: min €10,000 capital (paid up €5,000)
- **EPU (Einzelpersonenunternehmen)**: ~70 % of OE-Selbstständige
- **Pauschalierung**: simplified tax regime for small businesses

### Salary benchmarks (2025)

- Median monthly gross:
  - Wien: ~€3,800
  - Salzburg, Innsbruck: ~€3,600
  - Steiermark, OÖ, NÖ: ~€3,200
  - Burgenland, Kärnten: ~€2,900
- **Mindestkollektivvertragslöhne**: vary by branch, typical €1,800–€2,200 für Einsteiger

### Cultural quirks

- **13. + 14. Gehalt** standard (taxed at lower rate)
- **Kollektivvertrag** governs ~95 % of salaried jobs

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **HORA** (Natural Hazard Overview & Risk Assessment) | `https://hora.gv.at/` | Floods, earthquakes, storms, hail, lightning, snow, landslides — UNIQUE all-in-one portal |
| **HORA 3D** (interactive) | from `https://hora.gv.at/` | Address-level 3D risk visualization |
| **WISA Hochwasser-Risiko** | `https://maps.wisa.bmluk.gv.at/gefahren-und-risikokarten-zweiter-zyklus?g_card=hwrisiko_gefahren_ueff` | Detailed Q30/Q100/Q300 |
| **AGES Radonkarte** | `https://geogis.ages.at/GEOGIS_RADON.html` | Radon hazard per Gemeinde |
| **GeoSphere Austria** (formerly ZAMG + GBA) | `https://www.geosphere.at/` | Earthquake + climate + geology |
| **Naturgefahren-Bundesländer** | per state geoportal | Lawinen, Mure, Steinschlag |
| **OEROK-Atlas Hochwasserrisiko** | `https://www.oerok-atlas.at/` | Aggregated indicators |

### HORA — the gold standard

Austria's **HORA** is one of the few free, address-level, all-hazards-in-one-place natural hazards portals in the EU. Initiated 2002 after the disaster Donau flood; managed by BMLUK + VVO (Versicherungsverband). Free, address-level, all hazards in one place.

### Specific risks

- **Hochwasser**: Donau, Drau, Mur, Inn, Salzach valleys — recurring; 2002, 2013, 2024 major events
- **Lawinen** (avalanche): Tirol, Salzburg, Vorarlberg alpine — strict zoning
- **Mure** (mudslides): alpine + Pre-alpine
- **Erdrutsch** (landslide): widespread in Voralpen + Alpen
- **Steinschlag** (rockfall): alpine slopes
- **Earthquakes** — moderate:
  - **Wienerwald** (Vienna western suburbs): M 4-5 historical
  - **Mur-Mürz-Tal** (Steiermark): seismically active
  - **Kärnten**: low-moderate
  - 2024 Vienna M 4.1 reminder
- **Hagel** (hail): increasing damage Süden + Westen
- **Sturm/Orkan**: Atlantic + Mediterranean depressions
- **Radon**: Austria has elevated levels; granite Mühlviertel + Waldviertel + parts of Tirol/Salzburg
- **Hangrutsch** (slope movements): post-storm + heavy rain

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1945 Gründerzeit** | Lead, asbestos, Holzbalkendecken, Holzwurm |
| **1945–1965 Wiederaufbau** | Asbestos common, lead pipes, energy-inefficient |
| **1965–1980** | "Plattenbau" Wien-style + Eternit asbestos roofs |
| **1980–2000** | Phasing out asbestos, basic insulation |
| **Post-2008** | OIB-Richtlinien strict; modern envelope |

### Mandatory diagnostics at sale

| Document | Required because | Validity |
|---|---|---|
| **Energieausweis (EAW)** | All sales | 10 years; penalty up to ~€1,450 est. — verify current cap |
| **Grundbuchauszug** | Verify owner + Lasten | At sale |
| **Lageplan / Mappenkopie** | Boundaries | Per case |
| **WEG-Vereinbarung + Nutzwertgutachten** | If Wohnungseigentum | At sale |
| **Hausverwaltung Auskunft** (Rücklage, Hausgeld) | If apartment | At sale |
| **Wohnnutzwertgutachten** | If WEG | At sale |
| **Gefahrenzonenplan** | If alpine / flood-prone | Per case |

### Climate change projections (GeoSphere Austria)

- +2.0–3.5 °C by 2050 (RCP scenarios)
- Heat waves: longer + more intense
- Precipitation: more extreme events; +Starkregen
- **Lawinen**: less reliable below 1,500m altitude
- **Wasser**: drought risk Pannonisches Becken (Burgenland, Niederösterreich)
- **Schnee**: ski-season decreasing in lower Alps

---

## Section: `--mains`

### Sources

- Each Gemeinde has Wasserwerk + Abwasserverband
- **ÖVGW (Österreichischer Vereinigung für das Gas- und Wasserfach)**: `https://www.ovgw.at/`
- Major operators: Wien Wasser, Linz AG, Salzburg AG, IKB Innsbruck

### Verification

- Most populated areas: städtische mains universal
- Almhütten + Maiensässe + Streusiedlungen alpine: Hauskläranlage / Senkgrube
- **Anschlussbescheid** required at sale

### Costs

| Scenario | Cost (€, est. 2026) |
|---|---:|
| Anschluss to mains (where available) | ~3,000–8,000 |
| Mains-line extension if needed | varies by Gemeinde |
| Hauskläranlage (4 EW) | ~6,000–15,000 |
| Senkgrube replacement | ~4,000–10,000 |

*Est. — verify with local installer / Gemeinde; figures may have changed since 2026.*

---

## Cost benchmarks (AT 2026)

| Work | Cost (€, est. 2026) |
|---|---:|
| Energieausweis | ~250–600 |
| Notar / Anwalt | 1.0–2.5 % of price |
| Grunderwerbsteuer | 3.5 % |
| Eintragungsgebühr Grundbuch | 1.1 % |
| Maklerprovision (3 % each side excl. VAT) | ~3.6 % typical |
| **Total transaction cost** | **9–11 %** of price |
| Lawinenverbauung repair (alpine specific) | varies |
| Asbestsanierung (small house) | ~15,000–60,000 |
| Energetische Sanierung Klasse C → A | ~50,000–120,000 |
| Heizungstausch (Wärmepumpe) — incl. Förderung | ~25,000–40,000 |
| Dachsanierung Tiroler Schindel (200 m²) | ~30,000–60,000 |

*Construction/retrofit ranges are est. — verify with quotes; figures may have changed since 2026.*

## Active fiscal incentives (2025-2026)

- **Sanierungsoffensive 2024–2030** (federal + Bundesländer): up to ~€15,000 est. for fossil → renewable heating (verify current cap at umweltfoerderung.at)
- **Wohnbauförderung** (per Bundesland) — varies massively
- **Sonder-AfA** for new Mietwohnungen
- **Klimaticket Effizienzhaus** subsidy
- **Investitionsfreibetrag (IFB)**: 10 % deduction for retrofit
- **Erneuerbare-Wärme-Gesetz (EWG)** from 2024: oil/gas heating bans phasing in

## Common listing platforms

- **Willhaben.at** — biggest, full extraction
- **ImmobilienScout24.at**
- **derStandard Immo**
- **Bazar.at, Quoka.at** — privates
- **EHL, JP Immobilien, Otto Immobilien** — premium agency Wien
- **immo.tt.com** Tirol-specific

## Caveats unique to AT

- **Ausländergrunderwerb** (foreign buyer rules): non-EU/EEA buyers need a **grundverkehrsbehördliche Genehmigung** in some Bundesländer (esp. Tirol, Salzburg, Vorarlberg), granted by the Grundverkehrs-Landeskommission — an **approval regime with no quota and no percentage cap**; EU/EEA nationals are equated with Austrians. Do not conflate it with the nationality-neutral second-home thresholds below — they are two distinct regimes. (2026-08-07 verified; source RIS konsolidiertes Landesrecht Tirol/Salzburg + Land Vorarlberg Grundverkehr)
- **Zweitwohnsitz-/Freizeitwohnsitz-Schwellen** (nationality-neutral — NOT a foreign-buyer quota): **Tirol** — new Freizeitwohnsitze may not be declared permissible once the Freizeitwohnsitz share exceeds **8 v.H.** of total dwellings per the last Gebäude- und Wohnungszählung (§ 13 Abs 5 lit a TROG 2022, consolidated version in force 7 Jul 2026, LGBl 43/2022 as amended by LGBl 51/2026). **Salzburg** — Zweitwohnung-Beschränkungsgemeinden are communes where non-Hauptwohnsitz dwellings exceed **16 %** of the total stock (§ 31 Abs 1 Z 1 ROG 2009, in force 1 Mar 2023, LGBl 95/2022), designated by Landesregierung-Verordnung **every five years** on the five-year arithmetic mean at Stichtag 31 Oct — not annually; a Gemeinde may apply to have its percentage raised. No tightening verified through Aug 2026 (Tirol LGBl 51/2026, kundgemacht 6 Jul 2026, is a building/energy-law omnibus; Salzburg ROG amendment LGBl 79/2026 touches only §§ 5 Z 2, 53 Abs 2 Z 11, 60 Abs 1 und 5 and 88 Abs 9). (2026-08-07 verified; source [RIS ROG 2009 § 31](https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=LrSbg&Gesetzesnummer=20000615&Paragraf=31) + RIS konsolidiertes Landesrecht Tirol)
- **Naturschutz** restrictions on alpine constructions — strict
- **MRG categories** make rental investment math depend heavily on building age
- **Mietkauf** model (rent-to-own via Genossenschaft) common
- **HORA portal is free, address-level, all-hazards-in-one-place** — use it as the single source of truth for risks
- **Erbenermittlung** can stall purchases for months if Grundbuch unclear
- **Bauernhof** (farm) special restrictions; Anerbenrecht
- **Schenkungsmeldegesetz** since 2008 — mandatory disclosure for gifts
- **Tourismusabgabe** per Gemeinde — affects rental margins
- **Lex Koller-style** restrictions in some Bundesländer
- **Almhütten** + **Bauernhöfe** subject to special rural property law

## Reddit / forum sources

- **r/Austria**, **r/wien**
- **r/AustrianEconomy**
- **derStandard Forum** (active discussions)
- **Bauen-Wohnen.at**, **Energiesparhaus.at** forums
- Expat: **Vienna Würstelstand**, **The Local Austria**

## Verification authorities

| Authority | When to call |
|---|---|
| **Bezirksgericht Grundbuch** | Title verification, encumbrances |
| **Gemeinde / Bauamt** | Bauakt, Flächenwidmungsplan, permits |
| **Finanzamt** | Grundsteuer assessment, Einheitswert |
| **Notar** | Final transfer, escrow |
| **Wasserwerk Gemeinde** | Mains drains verification |
| **Bundesland Wasserrechtsbehörde** | Flood zone confirmation |
| **AGES** | Radon, food safety |
| **GeoSphere Austria** | Seismic + climate |
| **Wohnungseigentumsverwaltung (WEG)** | Hausgeld, Rücklage, Beschlüsse |

## Quirks to know

- **Einlagezahl (EZ)** + **Katastralgemeinde** — the Austrian way to identify property; PLZ + address often insufficient
- **Grundbuchauszug A1/A2/B/C blätter** — read all 4 sections (rights, encumbrances, mortgages, etc.)
- **Wohnnutzwert** vs Nutzwert — share-allocation in WEG
- **Anteil + Tagsatz** allocate Hausgeld
- **Wohnungseigentumsvertrag** + **Nutzwertgutachten** at sale
- **Bestandschutz** for old buildings; new requirements only on changes
- **Schillingbescheid**: legacy 1995 property tax base in some files
- **Grundverkehr** restrictions in Tirol/Salzburg/Vorarlberg — approval (Genehmigungspflicht), not a quota
- **Pflegeregress** (since 2018, abolished — but check older estates)
- **Anerbenrecht**: peasant inheritance rules in Tirol, Salzburg, Kärnten

## Source URL templates

| Source | URL pattern |
|---|---|
| HORA | `https://hora.gv.at/` |
| WISA Hochwasser | `https://maps.wisa.bmluk.gv.at/gefahren-und-risikokarten-zweiter-zyklus` |
| AGES Radon | `https://geogis.ages.at/GEOGIS_RADON.html` |
| GeoSphere Austria | `https://www.geosphere.at/` |
| Statistik Austria HPI | `https://www.statistik.at/statistiken/volkswirtschaft-und-oeffentliche-finanzen/preise-und-preisindizes/haeuserpreisindex-und-ooh-pi` |
| OeNB Wohnimmobilienpreis | `https://www.oenb.at/Statistik/Standardisierte-Tabellen/Preise-Wettbewerbsfaehigkeit/immobilien/wohnimmobilienpreisindex.html` |
| Willhaben Immobilien | `https://www.willhaben.at/iad/immobilien/<typ>/<bundesland>/<bezirk>` |
| ImmobilienScout24.at | `https://www.immobilienscout24.at/regional/<bundesland>/<bezirk>` |
| Justizportal Grundbuch | `https://www.justiz.gv.at/home/service/grundbuch~36.de.html` |
| BMF Finanzonline | `https://finanzonline.bmf.gv.at/` |

## Status

✅ **Fully populated** as of 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + cadastre sources (HORA + Statistik Austria + Grundbuch all gold-standard). MEDIUM for short-let regulation (Wiener Bauordnung 2024 + EU 2024/1028 transposition still evolving).
**Last verified**: 2026-08-07 — `--tax` ownership caveats only (Grundverkehr approval regime + Tirol/Salzburg second-home share thresholds re-verified against RIS konsolidiertes Landesrecht); all other sections remain at 2026-07-03. Rental / tax tracker entries re-checked 2026-09-24 (November regwatch wave, run early; see shared/regulatory-watch.md).

## Extension TODOs

- [ ] Per-Bundesland Ausländergrunderwerb rules
- [ ] HORA 3D parcel-level extraction
- [ ] Per-Gemeinde Tourismusabgabe rates
- [ ] Wohnbauförderung per Bundesland decision tree
- [ ] MRG category detection from build year + Bezirk
- [ ] Anerbenrecht detection from Grundbuch
- [ ] Zweitwohnsitz quota per alpine Gemeinde
- [ ] Grundsteuerreform tracking (likely 2026-2028)
