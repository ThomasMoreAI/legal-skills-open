# Belgium 🇧🇪 — Property Due-Diligence Playbook

ISO2: `be`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode**: 4 digits (`1000` Bruxelles, `2000` Antwerpen, `4000` Liège, `8000` Brugge)
- **Admin levels**: 3 régions (Wallonie, Vlaanderen, Bruxelles-Capitale) + 10 provinces + 581 communes
- **Currency**: EUR (€)
- **Languages**: French (Wallonie), Dutch (Vlaanderen), German (Eastern Cantons), bilingual (Bruxelles)
- **Significant regional autonomy** on housing/tax/environment — three different regimes for almost everything
- **Cadastre**: **AGDP / FOD Financiën** (federal) + regional registers
- **Identifier**: kadastraal nummer / matricule cadastral (`<commune> <section> <numéro>`)
- **Ownership types**: **pleine propriété** (freehold), **emphytéose** (long lease), **superficie** (right to build), **VME / co-propriété** (apartment)

## Section: `--price`

### Primary sources

- **STATBEL** (Belgian statistics): `https://statbel.fgov.be/en/themes/housing/real-estate` — official housing price index quarterly
- **Notaires.be / Notaris.be** — sale-price barometer: `https://www.notaire.be/` / `https://www.notaris.be/`
  - Quarterly **Baromètre des notaires** with detailed regional breakdowns
- **CIB Vlaanderen** + **Federia** + **Beroepsinstituut van Vastgoedmakelaars (BIV)** — agent body data
- **Cadastre** (FOD Financiën): `https://finances.belgium.be/fr/particuliers/habitation/cadastre`

### Listing platforms

- **Immoweb** — DOMINANT: `https://www.immoweb.be`
- **Logic-Immo BE**: `https://www.logic-immo.be/`
- **Zimmo**: `https://www.zimmo.be/`
- **Realo**: `https://www.realo.be/`
- **Vlan** (FR): `https://www.vlan.be/`
- Agency networks: **Era**, **Century 21**, **Engel & Völkers**

### 2025 price benchmarks (STATBEL + Notaires)

| Region | Avg €/m² (apt) | Avg total (semi-detached/maison) |
|---|---:|---:|
| **Bruxelles centre** | 4,000–7,500 | 500,000–950,000 |
| **Bruxelles périphérie** | 3,200–5,500 | 380,000–700,000 |
| **Antwerpen** | 3,500–6,000 | 380,000–700,000 |
| **Gent** | 3,200–5,500 | 380,000–650,000 |
| **Leuven** (university) | 4,000–6,500 | 450,000–800,000 |
| **Liège** | 1,800–3,200 | 220,000–380,000 |
| **Namur / Charleroi** | 1,600–2,800 | 180,000–320,000 |
| **Hasselt / Brugge** | 2,800–4,500 | 320,000–550,000 |
| **Coastal Vlaanderen** (Knokke, etc.) | 3,500–8,000+ | 400,000–1,200,000+ |
| **Rural Wallonie** | 1,200–2,200 | 150,000–280,000 |

### Compute

1. €/m² = price / **superficie habitable / bewoonbare oppervlakte**
2. **Revenu cadastral (RC) / kadastraal inkomen (KI)**: critical reference value for tax — pre-1975 baseline indexed
3. **VME / co-propriété**: must read **assemblées générales** + **état descriptif** + **règlement**

### Key terms

- Pleine propriété / volle eigendom = freehold
- Revenu cadastral (RC) / Kadastraal inkomen (KI) = cadastral income (1975 baseline + index)
- VME (Vereniging van Mede-Eigenaars) / ACP (association de copropriétaires) = HOA
- PEB / EPC = energy certificate

---

## Section: `--traffic`

### Sources

- **SPW Mobilité** (Wallonie): `https://mobilite.wallonie.be/`
- **MOW (Mobiliteit en Openbare Werken Vlaanderen)**: `https://mobiliteit.vlaanderen.be/`
  - **Verkeerstellingen op Vlaamse gewestwegen**: open data
- **Bruxelles Mobilité**: `https://mobilite-mobiliteit.brussels/`

### Key term

- **PJM (Pays Jour Moyen)** / **GMD (Gemiddelde Daagse Verkeersintensiteit)** = AADT-equivalent

### Verdict bands

- 🟢 < 1,500 v/d (rue résidentielle, voirie communale)
- 🟡 1,500–10,000 v/d (voirie communale principale, route régionale tranquille)
- 🟠 10,000–30,000 v/d (route régionale, axe urbain)
- 🔴 > 30,000 v/d (autoroute, ring, axe central)

---

## Section: `--tax`

### Annual property tax — Précompte immobilier / Onroerende voorheffing

**Three regional regimes** (RC/KI as base):

#### Wallonie

- Base: indexed RC × **1.25%** (régional SPW Fiscalité) + opcentimes provinciales + opcentimes communales (2026-05-27 verified, source: finances.wallonie.be)
- SPW Fiscalité has collected Wallonia précompte since 1 Jan 2021 (previously SPF Finances)
- Effective rate ~30–60% of indexed RC depending on commune
- Typical residential: **~€600–€2,500/yr est.** (indexed RC × ~30–60% effective rate above — verify on your own RC)
- **Réduction modeste** for primary residence under conditions

#### Vlaanderen

- Base: indexed KI × **3.97%** (basisheffing VLABEL) + opcentiemen provincie + opcentiemen gemeente (2026-05-27 verified, source: VLABEL belastingen.vlaanderen.be — highest regional base rate in BE)
- Effective rate ~35–65% of indexed KI
- Typical residential: **~€700–€2,800/yr est.** (indexed KI × ~35–65% effective rate above — verify on your own KI)
- **Vermindering** for primary residence + dependents

#### Bruxelles-Capitale

- Base: indexed RC × **1.25%** (régional Bruxelles Fiscalité) + opcentimes communales (Agglomération bruxelloise) (2026-05-27 verified, source: be.brussels/Bruxelles Fiscalité)
- Effective rate ~25–55% of indexed RC
- Typical residential: **~€1,000–€3,500/yr est.** (indexed RC × ~25–55% effective rate above — verify on your own RC)

### Transaction taxes — Droits d'enregistrement / Registratierechten

**MAJOR REFORM 1 January 2025** — both Vlaanderen + Wallonie cut for primary residence:

#### Vlaanderen (effective 1 Jan 2025)

- **Eigen woning (own home, primary)**: **2%** (down from 3%, from 1 Jan 2025) — confirmed by Beobank, Argenta, ABM-Altos
  - Conditions: only residence, must occupy
  - **Tightening from 1 Jan 2026** (2026-05-27 verified, source: vgd.eu/forumadvocaten/Andersen): buyer must maintain registered domicile ≥1 uninterrupted year; **natural persons only** (any legal-entity co-buyer → entire transaction reverts to 12%); full-ownership only (no naakte/vruchtgebruik splits); trigger date = compromis (not deed)
- **Andere woning (other / second / BTL)**: **12%** (since 1 Jan 2022, up from 10%)

#### Wallonie (effective 1 Jan 2025)

- **Habitation propre (own home, primary)**: **3%** (down from 12.5%) — confirmed
  - Conditions: must not own other residential, must establish primary within 3 yrs (5 yrs for building plot)
  - **Trade-off**: chèque-habitat + tax reduction up to €5,000 + 6% modest housing rate ALL ABOLISHED in exchange
- **Other (second home / BTL)**: **12.5%**

#### Bruxelles-Capitale

- **Standard**: **12.5%**
- **Abattement**: €200,000 abattement on first home (effective sees ~€25,000 saved)
- **Reduced 10%** in some cases (modest housing under €600,000)

### Frais de notaire / notariskosten

- ~1.5–2% on top of registration duties + fees
- Mostly fixed scale per Royal Decree

### TVA / BTW (new builds)

- **21%** (new build / off-plan first sale) — replaces droits d'enregistrement on the building portion (source: fin.belgium.be — verify current rate)
- Applies to the building/construction portion (21% VAT); the land portion is taxed under regional droits d'enregistrement / registratierechten — a building-vs-land split, not a time-based reversion (source: fin.belgium.be — verify)
- **6% demolition + reconstruction (permanent from 1 Jul 2025)** (2026-05-27 verified, source: fin.belgium.be / Loyens & Loeff): on construction works for owner-occupier primary residence ≤175 m² with ≥5-yr occupation OR long-term rental ≥15 yrs. From 18 Jul 2025 Programme Law (in force 29 Jul 2025), 6% **also covers the sale** of newly-reconstructed buildings (surface cap lowered from 200→175 m²).

### Total transaction cost (buyer side)

| Region | Primary residence | Second home / BTL |
|---|---:|---:|
| **Vlaanderen** | ~3.5–4.5% | ~13.5–14.5% |
| **Wallonie** | ~5–6% | ~14.5–16% |
| **Bruxelles** | ~8–11% | ~14.5–16% |

### Capital gains

- **Primary residence sale**: exempt
- **Investment property held >5 yrs**: exempt
- **Speculative (held <5 yrs)**: 16.5% (+ communal surcharges) — verify current rate at fin.belgium.be (the 2025 federal budget legislated a new general capital-gains regime taking effect 2026; this figure may be superseded)
- **Land speculation (<8 yrs)**: 33% (+ surcharges) — verify current rate at fin.belgium.be (same 2026 CGT-regime caveat as above)

### Future risk

- **Vlaanderen 2% rate** stable (post-2025 reform)
- **Wallonie 3% rate** stable + locked in (chèque-habitat abolished in trade)
- **Bruxelles** abattement increases discussed
- **RC reform**: long-discussed federal-level, no enacted reform 2025-2026

---

## Section: `--rental`

### Long-term residential

- **Bail de résidence principale / Hoofdverblijfsovereenkomst**: standard 9 yrs (3+3+3 break clauses)
- **Indexation**: per regional formula (CPI-based)
- **Vlaanderen Woninghuurdecreet** (2019)
- **Wallonie Code wallon de l'habitation durable** (2018)
- **Bruxelles Code bruxellois du logement** (2017)
- Tenant rights moderate (less strict than DE/AT)

### Short-let (Airbnb / hébergement touristique)

**Three regional regimes**:

#### Bruxelles-Capitale

- Very strict licensing — **autorisation préalable** required
- 90-day cap discussed
- **EU 2024/1028 transposition** in progress

#### Wallonie

- **CGT (Code wallon du tourisme)** — registration mandatory
- **Hébergement touristique** régime (HT licensing)
- **Vlan / Logic-Immo** for promotion regulated

#### Vlaanderen

- **Logiesdecreet** (2017) — registration mandatory at **Toerisme Vlaanderen**
- **Erkenning** + brandveiligheidsattest required
- **EU 2024/1028 transposition** — pending May 2026

### Tax on rental

- **Residential rental** (long-term): RC × 1.40 (uplift for furnished or rental); often substantially below market — **major tax-optimization advantage**
- **Short-let / commercial rental**: full income tax (progressive)

---

## Section: `--work=<profession>`

### Sources

- **Forem** (Wallonie): `https://www.leforem.be/`
- **VDAB** (Vlaanderen): `https://www.vdab.be/`
- **Actiris** (Bruxelles): `https://www.actiris.brussels/`
- **LinkedIn BE**, **StepStone**, **Indeed**, **References.be**

### Self-employment

- **Statut indépendant**: BCE (Banque Carrefour des Entreprises) / KBO registration
- **TVA** (VAT): from €25,000 turnover (franchise)
- **INASTI / RSVZ social contributions**: ~20.5% on net income
- **Personal income tax**: progressive 25% / 40% / 45% / 50%
- **Régime forfait** for small traders

### Salary benchmarks (2025)

- Median annual gross:
  - Bruxelles: ~€48,000–€68,000
  - Antwerpen / Gent: ~€42,000–€58,000
  - Wallonie: ~€36,000–€48,000

---

## Section: `--risks`

### Primary regional sources

| Source | URL | What it gives |
|---|---|---|
| **Geopunt Vlaanderen** | `https://www.geopunt.be/` | Vlaanderen geo-data, hazard layers |
| **WalOnMap** | `https://geoportail.wallonie.be/` | Wallonie geoportal |
| **BruGIS** | `https://gis.urban.brussels/brugis` | Bruxelles geoportal |
| **CIRGT Wallonie** | `https://environnement.wallonie.be/` | Risk maps Wallonie |
| **OVAM** (Vlaanderen bodempolluties) | `https://www.ovam.be/` | Soil pollution Vlaanderen |
| **Bruxelles Environnement** | `https://environnement.brussels/` | Bruxelles env data |
| **IRM (Institut Royal Météorologique)** | `https://www.meteo.be/` | Climate, weather |
| **AwAC** Wallonie air quality | `https://www.awac.be/` | Wallonie air |
| **VMM** Vlaamse Milieumaatschappij | `https://www.vmm.be/` | Vlaanderen environment |
| **CELINE** | `https://www.irceline.be/` | National air quality |

### Specific risks

- **Inondation / overstroming (flooding)** — major risk:
  - July 2021 catastrophic floods (Wallonie): ~40 dead, ~€2B damage; Liège, Verviers, Pepinster, Theux
  - Vesdre, Meuse, Ourthe basins
  - **Plan PARGI / Bekkenbeheerplan** for adaptation
- **Bodemverontreiniging / pollution du sol**: extensive industrial legacy in Wallonie + Antwerpen + Charleroi
- **Aardbeving / séisme**: low-moderate (Roer Valley fault); 1992 Roermond M 5.4 (felt in BE)
- **Mijnverzakkingen** (mining subsidence): Limburg (coal), Wallonie (Borinage); historic
- **Asbestos**: pre-1998 buildings extensively contaminated
- **Loodleidingen** (lead pipes) — pre-1960 buildings
- **Pollution de Charleroi-Mons-Liège axe**: heavy metal soil contamination
- **Klimaatverandering**: +2.0–4.0 °C by 2100; precipitation +20% winter

### Build-era hazards

| Era | Hazards |
|---|---|
| **Pre-1900** | No DPC, lead, damp, asbestos cement starts |
| **1900–1945** | Asbestos common, lead, weak insulation |
| **1945–1990** | Asbestos very common (banned 1998); cuves à mazout (oil tanks) |
| **1990s+** | Improved insulation; PEB phasing in |
| **2014+** | PEB strict; Q-ZEN / BEN energy standards |

### Mandatory at sale

| Document | Region | Required because | Validity |
|---|---|---|---|
| **PEB** (FR) / **EPC** (NL) | All | Energy cert | 10 years |
| **Bodemattest** | Vlaanderen | Soil report | At sale (sale BLOCKED without it) |
| **Asbestattest** | Vlaanderen | Mandatory since **23 Nov 2022** for sales | 10 years |
| **Attestation du sol / bodemcertificaat** | Bruxelles | Mandatory | At sale |
| **Pollution du sol** | Wallonie | Banque de Données de l'État des Sols | At sale |
| **Contrôle électrique** | All | If wiring >25 yrs | 25 years |
| **Citerne mazout** | Where applicable | Permit | Ongoing |
| **CIGT** (Wallonie certificat) | Wallonie | If applicable | Per case |

### Climate change projections

- +2.0–4.0 °C by 2100
- +20% winter precipitation, -20% summer
- More extreme rainfall (Vesdre 2021 type)
- Sea-level rise + coastal management Vlaamse Kust

---

## Section: `--mains`

### Sources

- **SWDE** (Société wallonne des eaux): `https://www.swde.be/` — Wallonie water
- **IECBW** (Intercommunale eaux Centre Brabant wallon)
- **IDEA** (Intercommunale développement économique Mons-Borinage)
- **CILE** (Compagnie intercommunale liégeoise eaux)
- **De Watergroep**, **Pidpa**, **Aquaduin** — Vlaanderen water
- **Vivaqua / Hydrobru**: `https://www.vivaqua.be/` — Bruxelles
- **Aquafin** (Vlaanderen wastewater): `https://www.aquafin.be/`

### Verification

- Universal in urban areas across all three régions
- Some rural Wallonie / Eifel border on individual systems (fosses septiques)
- Vlaanderen ~97% mains coverage (est.)
- Wallonie ~85% mains coverage

### Costs

| Scenario | Cost (€) |
|---|---:|
| Aansluiting riool / raccordement égout | 6,000–15,000 |
| Septique / IBA installation | 8,000–15,000 |
| Cuve mazout removal | 1,500–4,000 |

---

## Cost benchmarks (BE 2026) — est. ranges, verify with contractor quotes

| Work | Cost (€) |
|---|---:|
| PEB / EPC | 150–350 |
| Asbestattest (Vlaanderen) | 350–600 |
| Bodemattest (Vlaanderen) | 50–200 |
| Notaris fees | 1.5–2% of price |
| Registration duties (primary, Vlaanderen) | 2% (since 1 Jan 2025) |
| Registration duties (primary, Wallonie) | 3% (since 1 Jan 2025) |
| Registration duties (Bruxelles) | 12.5% (with abattement) |
| **Total transaction cost (Vlaanderen primary)** | **~3.5–4.5%** |
| **Total transaction cost (Wallonie primary)** | **~5–6%** |
| **Total transaction cost (Bruxelles primary)** | **~8–11%** |
| **Total transaction cost (second home)** | **~13.5–16%** |
| Septic to mains | 6,000–15,000 |
| Cuve mazout removal | 1,500–4,000 |
| Roof renovation | 15,000–30,000 |
| Asbestos removal | 1,000–10,000 |
| Energy retrofit (Class C → A) | 25,000–60,000 |

## Active fiscal incentives (2025-2026)

- **Wallonie**: chèque-habitat ABOLISHED for new buyers since 1 Jan 2025 (replaced by 3% rate)
- **Vlaanderen**: woonbonus phased out; 2% rate now
- **Bruxelles**: abattement €200k still in force
- **Régionalisation aides**: rénovation énergétique grants per région
- **Federal EE-loan**: max €50,000 mortgage
- **Mijn VerbouwLening** (Vlaanderen)
- **Renovation premium** Wallonie

## Common listing platforms

- **Immoweb** — DOMINANT
- **Logic-Immo BE** (FR/NL)
- **Zimmo** (NL focus)
- **Realo** (NL)
- **Vlan** (FR)

## Caveats unique to BE

- **Régionalisation extreme** — three different regimes for almost everything (transfer tax, energy, planning, environment)
- **2025 transfer tax reform** — Vlaanderen 3→2%, Wallonie 12.5→3%; major affordability boost
- **Bodemattest / asbestattest** mandatory in Vlaanderen — sale BLOCKED without these
- **Asbestattest mandatory since 23 Nov 2022** (Vlaanderen)
- **PEB E/F/G** increasingly restricted in Wallonie — minimum standards tightening
- **Cuve à mazout** strict regulations
- **RC/KI 1975 baseline** — wildly outdated; reform proposed for years
- **VME health** mandatory pre-purchase (apartment): assemblées + comptes + état
- **Régionalisation** of stamp duty since 2002 — complete divergence
- **Wallonie Vesdre flood 2021** memory shapes flood disclosure rules
- **Brussels Code du Logement** — strict tenant protections + minimum standards
- **3 régions, 3 EPC formats, 3 grant systems** — read region-specific rules

## Reddit / forum sources

- **r/belgium**, **r/Brussels**, **r/AskBelgium**
- **r/PersonalFinanceBE** — tax + mortgage discussions
- **Tweakers BE Forum**
- Expat: **The Bulletin**, **Expatica BE**, **Brussels Times**

## Verification authorities

| Authority | When to call |
|---|---|
| **AGDP / FOD Financiën cadastre** | Title verification, RC/KI |
| **Notaris** (mandatory for sale) | Final transfer + searches |
| **Commune urbanisme** | Permits, planning history |
| **Region-specific environment agency** (OVAM/SPW/Bruxelles Env) | Pollution, asbestos |
| **VME / ACP secretary** | If apartment: financials |
| **Région tax services** | Précompte, registration |

## Source URL templates

| Source | URL pattern |
|---|---|
| Cadastre FOD Fin | `https://finances.belgium.be/fr/particuliers/habitation/cadastre` |
| Notaires.be barometer | `https://www.notaire.be/` |
| STATBEL housing | `https://statbel.fgov.be/en/themes/housing/real-estate` |
| Geopunt Vlaanderen | `https://www.geopunt.be/` |
| WalOnMap | `https://geoportail.wallonie.be/` |
| BruGIS | `https://gis.urban.brussels/brugis` |
| OVAM Vlaanderen | `https://www.ovam.be/` |
| Bruxelles Environnement | `https://environnement.brussels/` |
| Immoweb | `https://www.immoweb.be/` |
| MOW Vlaanderen traffic | `https://mobiliteit.vlaanderen.be/` |
| SPW Mobilité | `https://mobilite.wallonie.be/` |

## Status

✅ **Fully populated** as of 2026-04-25.
**Coverage check**: pricing, traffic, tax (3 régions), rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for 2025 transfer tax reform (Beobank, Argenta, S-Team Law, ABM-Altos, Lexunion all confirm Vlaanderen 2% + Wallonie 3% from 1 Jan 2025), HIGH for asbestattest mandate (23 Nov 2022 Vlaanderen), HIGH for July 2021 flood as reform driver. MEDIUM for Bruxelles short-let (rapidly evolving + EU 2024/1028 transposition pending).

## Extension TODOs

- [ ] Per-commune précompte / onroerende voorheffing rates table
- [ ] Asbestattest detailed inspection checklist
- [ ] PEB regulations per région timetable (FR / NL / DE versions)
- [ ] Logies / hébergement licensing per région (Logiesdecreet, CGT)
- [ ] Vesdre 2021 flood-affected zones (rebuilding rules)
- [ ] Bodemattest decision tree (clean/contaminated/in-progress)
- [ ] Per-commune renovation premium eligibility
- [ ] EU 2024/1028 short-let transposition tracker (3 régions)
- [ ] Brussels heritage building constraints per zone
- [ ] German-speaking Eastern Cantons specific rules
