# France 🇫🇷 — Property Due-Diligence Playbook

ISO2: `fr`. Status: ✅ Fully populated.

## Country profile

- Postcode pattern: 5 digits (`XXXXX`)
- INSEE code: 5-digit commune identifier (different from postcode)
- Geocode commune → INSEE: use `https://geo.api.gouv.fr/communes?codePostal=<postcode>` or address-api `https://data.geopf.fr/geocodage/search?q=<query>`
- Currency: EUR (€)
- Language: French (with German/Italian/Catalan/Basque regional pockets)
- Cadastre: free public via `cadastre.gouv.fr`

## DROM overlay (overseas départements)

If the address resolves to one of the five **DROM** — postcode prefix **971 Guadeloupe (`gp`) · 972 Martinique (`mq`) · 973 Guyane (`gf`) · 974 La Réunion (`re`) · 976 Mayotte (`yt`)** — this metropolitan playbook still applies as the baseline (same *Code civil*, euro, *impots.gouv.fr*, *notaire*, cadastre framework), **but you MUST also load [`shared/fr-drom-overlay.md`](../../shared/fr-drom-overlay.md) and apply its deltas**: DROM-specific TVA rates, *octroi de mer*, *taxe foncière* abattements, majored notary *émoluments*, the Letchimy indivision regime, and per-DROM cyclone/seismic hazard profiles. The overlay lists ONLY the deltas — anything it does not override follows this playbook.

## Section: `--price`

**Data sources** (priority order — primary first):

1. **DVF Etalab — canonical actual sale prices** (DGFiP open data via Etalab):
   - Map portal: `https://app.dvf.etalab.gouv.fr/` (form-based; search by commune)
   - Bulk dataset: [data.gouv.fr DVF](https://www.data.gouv.fr/datasets/demandes-de-valeurs-foncieres/) (CSV per département per year, ~3-yr lag)
   - Clean passthrough UI: [immo-dvf.fr](https://www.immo-dvf.fr/) (same DVF data, easier to read; commune-level page is `/prix-immobilier/<region>/<dept>/<commune>-<postcode>/`)
2. **Aggregator estimates** (cross-check only — methodology + freshness varies):
   - [meilleursagents.com](https://www.meilleursagents.com/prix-immobilier/) — €/m² + history
   - [journaldunet.com patrimoine](https://www.journaldunet.com/patrimoine/prix-immobilier/) — JDN aggregated
   - [orpi.com prix-immobilier](https://www.orpi.com/prix-immobilier/) — Orpi network estimate
   - [immobilier.lefigaro.fr prix-immobilier](https://immobilier.lefigaro.fr/prix-immobilier/)
   - [pap.fr](https://www.pap.fr/vendeur/prix-m2/) — backup
3. **WebSearch live listings**: `"<commune>" maison à vendre prix` for current comp listings
4. **Avoid for primary data**: third-party DVF API mirrors (e.g., `api.cquest.org`) — frequently return non-JSON or stale; prefer Etalab + immo-dvf.fr passthrough

**Sparse-DVF fallback**: rural communes <1,000 pop typically have <10 transactions/year — DVF median for the commune is statistically noisy. **Use the nearest larger market town (sub-prefecture or chef-lieu de canton) as the reference** and apply a **0.7–0.85× rural correction factor** for outlying lieu-dit (depends on distance + amenities). Document the extrapolation explicitly + flag confidence MEDIUM, NOT HIGH.

**Compute**:
- Price/m² = listing FAI / surface m² (Carrez)
- Discount/premium vs commune average: `(commune_avg - listing_psqm) / commune_avg`
- Walk-away price = listing × (1 − reasonable_discount). For 1970s-1990s rural homes "à rafraîchir," reasonable_discount = 5–10 %.

**Caveats**:
- Rural communes have thin DVF samples (5–20 sales/yr); flag confidence as low if <10 transactions
- The "FAI" (Frais d'Agence Inclus) price includes the agency fee (~5–6 %); compute against the net seller price for notary fees

---

## Section: `--traffic`

**Data sources**:
- OSM Overpass for the way's `ref`, `highway`, `maxspeed` (already in pre-flight)
- Conseil Départemental traffic count PDF — search `"département <name>" comptage routier carte trafic <year>` and download
- Examples:
  - Vienne 86: `https://www.lavienne86.fr/fileadmin/medias/.../A1_Trafic_<year>.pdf` (~27 MB)
  - Most départements publish annually as A1 QGIS-rendered PDFs

**Extraction technique**:
1. `curl -sL -o trafic.pdf <url>`
2. `pdftotext -layout trafic.pdf - | grep "^.*D<road>"` → finds TMJA values in tabular form
3. For map labels (village names): `pdftoppm -png -r 200 trafic.pdf p` then crop to the commune location and read images
4. Color legend (most depts identical):
   - 🟧 orange: < 500 v/d
   - 🟦 cyan: 500–1500 v/d
   - 🟩 green: 1500–3000 v/d
   - 🟪 magenta: > 3000 v/d

**Compute**:
- TMJA on property's road (or estimated from nearest measured)
- Vehicle/hour daylight ≈ TMJA × 0.06; night ≈ TMJA × 0.01
- Heavy vehicles (PL) often listed alongside as percentage

**Verdict bands for rural FR**:
- 🟢 < 200 v/d
- 🟡 200–800 v/d
- 🟠 800–3000 v/d
- 🔴 > 3000 v/d

---

## Section: `--tax`

**Data sources** (priority order — canonical first):

1. **DGFiP open data — communal tax rates** (canonical, all communes):
   - DGFiP fiscal data on data.economie.gouv.fr: [data.economie.gouv.fr — taux fiscalité directe locale](https://data.economie.gouv.fr/explore/?q=taux+fiscalit%C3%A9+directe+locale)
   - Service-Public.fr lookup tool overview: [service-public.gouv.fr A18426](https://www.service-public.gouv.fr/particuliers/actualites/A18426)
   - Délibérations fiscales votées par les collectivités: [collectivites-locales.gouv.fr — Taux votés](https://www.collectivites-locales.gouv.fr/etudes-et-statistiques/acces-par-thematique/fiscalite/taux-de-fiscalite-directe-locale-votes-par-les-collectivites)
2. **Department-level reference** (rank + average): [DGFiP — Données générales sur les taux et les montants de la fiscalité directe locale](https://www.impots.gouv.fr/donnees-generales-sur-les-taux-et-les-montants-de-la-fiscalite-directe-locale) — "Répartition régionale et départementale du taux de prélèvement depuis 2018 : TF, TH, CFE (.xls)", updated 05/05/2026; latest bulletin "En 2025, la taxe foncière progresse de 2,4 %" (DGFiP Statistiques n°46, mai 2026). Primary publisher, replacing the former IndiceVille aggregator (2026 data, source DGFiP; 2026-09-18 verified)
3. **Third-party aggregator** (use only if DGFiP open data lookup fails for the specific commune): `https://www.impots-locaux.org/impots-locaux-<commune-slug>-<postcode>/`
4. **WebSearch fallback**: `"<commune>" taxe fonciere taux <year>` + TEOM rate

**Confidence note**: department-level data (e.g., "Dordogne avg TFPB 47.34%") is HIGH; commune-specific extrapolation when DGFiP open data lookup is sparse is MEDIUM. State explicitly which you're using.

**Compute**:
1. Estimate VLC (Valeur Locative Cadastrale): for rural 1970s build, tarif ≈ €15–25/m²/yr after current revaluations (varies by commune category 5/6/7).
2. Annual taxe foncière = `VLC × 50% × (taux_communal + taux_interco) + TEOM_amount`
3. Annual taxe d'habitation RS = `VLC × 100% × (taux_communal + taux_syndicat)`. Surcharge majoration 5–60 % if zone tendue (verify on liste).
4. Frais de notaire on €P (FAI minus agency fee): ≈ 7.5–8 % for ancien
   - DMTO: **6.32 %** in the large majority of départements since Apr 2025 (5.00 % département + 1.20 % commune + ~0.12 % frais d'assiette, computed as 2.37 % × dept rate) — the +0.5 pp département-share hike (art. 116, LOI n° 2025-127) applies **only to acts signed 1 Apr 2025 – 31 Mar 2028**; for acts from 1 Apr 2028 rates revert to the previously voted level. A shrinking minority still holds **5.81 %** — 10 départements as of 1 Apr 2026 (Hautes-Alpes, Alpes-Maritimes, Ardèche, Charente, Drôme, Lozère, Oise, Hautes-Pyrénées, Saône-et-Loire, Guadeloupe; per impots.gouv.fr rate table as relayed by professional trackers) — and Indre + Mayotte keep the 3.80 % dept share (**≈5.09 %** total). Départements re-vote annually (delib changes typically effective ~1 June) — **always pull the current [impots.gouv.fr DMTO PDF](https://www.impots.gouv.fr/sites/default/files/media/1_metier/3_partenaire/notaires/dmto/dmto_2026-02.pdf) edition for the live rate**. **Primo-accédants** (no main-residence ownership in the prior 2 years, buying as main residence) are statutorily exempt from the +0.5 pp hike. (2026-07-03 verified; sources [Légifrance LF 2025 art. 116](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000051169081) + impots.gouv.fr DMTO PDF + [AN question n° 5129](https://www.assemblee-nationale.fr/dyn/17/questions/QANR5L17QE5129))
   - Émoluments notaire: dégressif ~0.8–1.2 %
   - Débours + sécurité immobilière: €600–1,500
5. Future risk: **Révision des Valeurs Locatives des Locaux d'Habitation (RVLLH)** ⚠️ postponed to **2028 declarations → 2030 new values → 2031 tax impact** by **LFI 2026** (art. 106, LOI n° 2026-103 du 19 février 2026; CGI art. 1518 A quinquies A) — *not* PLF 2024/2025; an unofficial **est. +20–40 % for rural homes** circulates but no official figure is published (unverified — re-source or drop). Nothing rolls in 2026–2028; the Government's report to Parliament is now due **1 Sept 2029** (was 1 Sept 2026), and Sénat rapport l25-312 notes this volet would not be fully executed before **c.2040** — parliamentary commentary, not statute, but it is the realistic horizon for any buyer treating this as a live cost. Dates per [ANIL — analyse LF 2026 art. 106](https://www.anil.org/aj-loi-finances-2026/) + [Légifrance art. 106](https://www.legifrance.gouv.fr/jorf/article_jo/JORFARTI000053508773) (2026-08-07 verified — dates; % still unverified)

**Decision tree for residence type**:
- Primary: only taxe foncière + TEOM
- Secondary (résidence secondaire): + taxe d'habitation RS
- Loi de finances may evolve thresholds annually — check current

---

## Section: `--rental` (gîte / Airbnb)

**Data sources**:
- Local tourism office hébergements guide PDF — search `"<département>" hébergements meublés tourisme PDF`
- `https://www.airbnb.fr/<commune>-france/stays`
- `https://www.gitesdefrance-<dept-name>.com`
- Tourism observatoire PDF for occupancy rates: `<dept>.fr/.../tourisme/observatoire/`
- INSEE saison touristique data
- Reddit/forums for honest operator income reports

**Compute**:
1. Map existing competition (5–10 nearest gîtes with capacity + weekly tariff)
2. Pick configuration:
   - Convert one wing/basement → smaller unit, sleeps 4–6
   - Whole-house gîte → sleeps 8–12
   - Chambres d'hôtes → up to 5 rooms with breakfast
3. Realistic year-3 stabilised gross: 16–22 weeks × commune-typical rate
4. Apply tax regime:
   - Below €15k AND non-classé → micro-BIC 30 % abatement
   - Classé (or chambres d'hôtes) → micro-BIC **50 %** abatement (a non-classé above the €15k plafond cannot use micro-BIC → régime réel; 2025 data, source Service-Public A17883) (classement via organisme accrédité COFRAC) — plafond **€83,600 for 2026 income onward** (€77,700 applies to 2025 income declared in 2026; classé + chambres d'hôtes, per Loi Le Meur 2024-1039 en vigueur 1 Jan 2025 — was €188,700 pre-reform — then the 2026-2028 triennial revaluation). (2026-07-03 verified; sources [Légifrance Loi 2024-1039](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000050612711) + [Service-Public entreprendre A18813](https://entreprendre.service-public.gouv.fr/actualites/A18813))
   - Above €23k revenue → URSSAF 6 % (classé) or 21.2 % (non-classé)
   - Above €83.6k (2026 income; €77.7k for 2025 income) → régime réel

5. Subtract 35–45 % operating costs (cleaning, linen, utilities, commissions)
6. Compute net at TMI 11 % and TMI 30 %
7. Note: classement = 50 % abatement + 6 % URSSAF + plafond €83,600 (2026 income onward; €77,700 for 2025 income) vs 30 %/21.2 %/€15k unclassified (Loi Le Meur 2024-1039 + 2026-2028 triennial revaluation)

**Strategic levers**:
- **Classify it** — free in most departments via the ADT (Agence Départementale du Tourisme)
- **Pool / spa** is the single biggest revenue lever
- **Service à la personne** registration if you also offer in-person services
- **Taxe foncière exonération** under CGI art. 1383 E bis — many rural communes allow exoneration of meublés classés

**Caveats**:
- Loi Le Meur (Nov 2024) lowered non-classé thresholds drastically (was 77.7k → now 15k)
- National registration number via a single national téléservice operated by the DGE (statutory date **20 May 2026**, décrets n° 2026-196 and 2026-197 du 19 mars 2026; called Declaloc in secondary sources) — per the DGE API meublés page (updated 23 Jul 2026) the lessor téléservice opens only in **Q4 2026**, as a Démarche Numérique form on a public DGE page; until then the commune's existing procedure applies (communal registration where instituted, otherwise mairie declaration) and platforms cannot demand a number in communes without a registration procedure; apimeubles.finances.gouv.fr is the commune / EPCI / platform portal, not a lessor entry point — administrative fines pronounced by the maire up to **€10,000** (défaut d'enregistrement) / **€20,000** (fausse déclaration or faux numéro, art. 4 Loi Le Meur). (2026-09-24 verified, source DGE API meublés page)
- Loi Climat: DPE F-G gîtes increasingly restricted

---

## Section: `--work=<profession>`

**Data sources** (depending on profession):
- **Healthcare**: Doctolib, ARS, ordres professionnels (Conseil de l'Ordre)
- **Teaching**: Pôle Emploi, écoles de musique régionales, conservatoires CRR/CRD/CIOL, EMIG-style intercommunal schools
- **Trades**: Chambre de Métiers et de l'Artisanat, INSEE artisans, Pages Jaunes
- **Tech / cadres**: APEC, LinkedIn, Welcome to the Jungle, AppelService
- **Tutoring / private**: Superprof, Aladom, Apprentus, Allegro Musique, Spectable
- **Salaries general**: INSEE DADS / DSN, Hellowork, JournaldDuNet salaire

**Legal status options** (always include):
- **Auto-entrepreneur (BNC libéral)**: simple, ~22.2 % charges (rate NOT re-verified in this pass and may be stale — verify current rate at URSSAF before relying), plafond **€83,600** (2026-2028 triennium; was €77,700 through 2025) — BIC services and BNC libéral share the €83,600 services plafond per [URSSAF seuils 2026](https://www.autoentrepreneur.urssaf.fr/portail/accueil/sinformer-sur-le-statut/toutes-les-actualites/2026--modification-des-seuils-de.html) (2026-07-03 verified — plafond only)
- **Service à la personne (SAP)**: 50 % tax credit for client; activate via URSSAF
- **CCN ÉCLAT (associative music schools)**: coefficient 265 × point ~€6.85 ≈ €1,815/mo gross full-time — point value is a renegotiated collective-agreement figure; verify current point at the convention's latest avenant salaires before relying on
- **CDI public conservatoire**: needs DE + concours
- **Association loi 1901**: for community projects, no income to self
- **Régime réel BNC**: above €83.6k (2026 income onward; €77.7k for 2025 income)
- **Profession libérale réglementée** (médecin, avocat, etc.): specific regimes

**Catchment formula**:
- Local population in 30-min drive
- 60-min for online or rare specialties
- Account for English-speaking expat communities (Vienne, Charente, Haute-Vienne, Dordogne) — significant for British/Dutch/German-speaking professions

**Output sections to include**:
1. Catchment + competition table
2. Salaried options (CCN / convention)
3. Independent options (auto-entrepreneur)
4. Online / hybrid options
5. Realistic year-3 net (3 scenarios)
6. 12-month build plan

---

## Section: `--risks`

**Data sources** (in order of recommended individual-query path):

1. **ERRIAL — parcel-level synthesis (PRIMARY for individual address lookup)**: [errial.georisques.gouv.fr](https://errial.georisques.gouv.fr/) — form-based, address lookup, returns full PDF with all 11 risk categories pre-filled. **This is the canonical individual-buyer entry point**; use first before going to file/PDF or API.
2. **DICRIM (commune-level statutory doc)**: `https://files.georisques.fr/DICRIM/DICRIM_<INSEE>.pdf` — download with curl (verify file exists, not all communes publish), render with pdftoppm if scanned
3. **IAL (Information Acquéreurs Locataires) — département-level zoning maps**: `https://www.<dept>.gouv.fr/.../IAL_Risques-zones+par+commune.pdf`
4. **Géorisques portal (general risk lookup)**: `https://www.georisques.gouv.fr/mes-risques/connaitre-les-risques-pres-de-chez-moi`
5. **Géorisques API** (developer): API endpoints exist (`api/v1/...`) but are not officially-documented; **use the ERRIAL portal for individual queries** unless you need batch-scale extraction. If invoking the API: respect [robots.txt](https://www.georisques.gouv.fr/robots.txt) + add `User-Agent: <descriptive>` header.
5. **IRSN potentiel radon**: `https://recherche-expertise.asnr.fr/savoir-comprendre/environnement/connaitre-potentiel-radon-ma-commune`
6. **DRIAS climate**: `https://www.drias-climat.fr/`
7. **PPI nucléaire** (if any plant within 50 km): EDF site + préfecture
8. **OSM industrial overlay**: Overpass query within 5 km

**11 risk categories to evaluate** (DICRIM standard):
1. Inondation
2. Mouvement de terrain (RGA argiles)
3. Sismicité (zone 1-5)
4. Tempête / grand froid / canicule
5. Cavités souterraines
6. Feu de forêt
7. TMD (transport matières dangereuses)
8. Rupture de barrage
9. Risque nucléaire
10. Risque industriel (ICPE Autorisation/Seveso)
11. Sécheresse

**Build-era hazards**:
- < 1949: lead paint (CREP), often poor foundations
- 1949–1997: asbestos very likely (slates, flue, vinyl, fibrocement)
- 1949–1980: poor thermal envelope
- 1975–1995: aluminum wiring potential
- After 2000: modern standards but check if RT2012 compliant for thermal

**Climate change to 2050 (Vienne basin example, similar across rural FR)**:
- +1.6 °C (RCP 4.5) to +2.2 °C (RCP 8.5)
- +5 to +10 drought days/summer
- Less summer rain, more winter rain
- More heatwaves (longer + hotter)
- Forest fire risk rising

**Verdict logic for radon**:
- Zone 1 / Faible: 🟢 negligible
- Zone 2 / Moyen: 🟡 test recommended
- Zone 3 / Significatif: 🟠 test required, may need VMC/ventilation upgrade

---

## Section: `--mains`

**Data sources**:
1. **Sispea** (national registry): `https://www.services.eaufrance.fr/commune/<INSEE>/<latest_year>` — confirms which services exist
2. **Selectra** mirror: `https://eau.selectra.info/commune/<INSEE>` — operator details
3. **Listing language** for assainissement keywords ("tout-à-l'égout", "fosse septique", "assainissement individuel")
4. **PLU / Géoportail Urbanisme**: `https://www.geoportail-urbanisme.gouv.fr/` — for zonage assainissement when published
5. **Mairie phone** (always note this is the authoritative source)

**Compute**:
1. Does the commune have a collective sewer service at all?
2. Is the property in the bourg (likely connected) or hamlet (likely individual)?
3. What did the listing say (silence is itself a signal)?
4. Confidence level: high (listing explicit + Sispea + bourg) / medium / low

**Verification path**:
1. Call **Mairie de <commune>**: phone in DICRIM
2. Ask: « Est-ce que la parcelle au <address> est en zone d'assainissement collectif et raccordée au réseau ? »
3. Request from seller:
   - Collective: certificat de conformité du branchement
   - ANC: diagnostic ANC < 3 years old (mandatory at sale)

**Cost ranges (rural FR 2026)**:
- On collective, conform: redevance ≈ €1.50–2.50/m³ + connection fixed
- On collective, non-conform branchement (1975 build typical): €2,000–€5,000 upgrade
- In collective zone, not connected: €2,500–€8,000 + PFAC fee
- Outside collective (ANC septic to install or replace): €7,000–€15,000

---

## Mandatory diagnostics matrix at sale (2026)

| Diagnostic | Required because | Validity |
|---|---|---|
| DPE | All sales | 10 years |
| Audit énergétique | DPE = E/F/G | 5 years |
| ERP / ERRIAL | All sales | 6 months |
| Amiante | Built before 1 July 1997 | Indefinite if no amiante; 3 yrs if found |
| Plomb (CREP) | Built before 1 Jan 1949 | 1 year if positive, indefinite if negative |
| Termites | Commune in arrêté préfectoral | 6 months |
| Électricité | Installation > 15 yrs old | 3 years |
| Gaz | Installation > 15 yrs old (if gas) | 3 years |
| Assainissement non-collectif | Rural, no mains | 3 years |
| Mérule | Commune in arrêté zone | 6 months |

⚠️ **DPE recalculated from 1 Jan 2026** (arrêté du 13 août 2025, JO 26 Aug 2025): electricity primary-energy conversion coefficient lowered 2.3 → 1.9. Officially ~850,000 homes exit F/G with no works (base 1 Jan 2023, of 4.8M passoires; a Nov 2025 reassessment reported ~700,000 — secondary source, verify at ONRE); no label is downgraded, and only electric-heated homes benefit (the label stays the worse of the energy/GES scales — oil/gas-heated rural homes gain nothing). DPEs edited from 1 Jan 2026 auto-apply the new coefficient; pre-2026 DPEs stay valid and a re-labelling attestation is free (no new visit) via the ADEME Observatoire DPE-Audit. (2026-07-03 verified; source [economie.gouv.fr](https://www.economie.gouv.fr/actualites/un-nouveau-dpe-au-1er-janvier-2026-pour-favoriser-le-chauffage-electrique) + notaires.fr)

## Cost benchmarks (rural FR, 2026)

| Work | Cost |
|---|---:|
| Asbestos removal (small) | €1,500–€5,000 |
| Septic tank replacement | €7,000–€15,000 |
| Mains drains connection | €2,500–€8,000 |
| Full electrical rewire (200 m²) | €12,000–€20,000 |
| Roof replacement (slate, 150 m²) | €18,000–€30,000 |
| Insulation upgrade DPE E→D | €15,000–€25,000 |
| Insulation upgrade DPE E→C | €30,000–€50,000 |
| Wood stove installation | €3,000–€7,000 |
| Heat pump installation | €12,000–€20,000 |
| Pool (above-ground 6×3) | €5,000–€10,000 |
| Pool (in-ground 8×4 with deck) | €25,000–€45,000 |
| Building inspection (independent surveyor) | €600–€1,200 |
| Notary fees on €145k ancien | €10,500–€11,200 |

## Common listing platforms

- **SAFTI** — clean fields, full extraction
- **SeLoger** — JS-heavy, prefer mobile version
- **Leboncoin** — sparse, often need manual reading
- **ParuVendu, Logic-Immo, Bien'ici** — standard
- **Orpi, Century 21, IAD, Capifrance** — standard agency
- **Le Bon Coin** — private sales

## Reddit / forum sources for operator stories

- r/AskFrance, r/france (FR-language)
- r/AmerExit, r/IWantOut (expat moves)
- Mumsnet "living overseas" Vienne / Charente / Limousin
- FrenchEntrée, Complete France, The Good Life France
- Living Magazine, etcetera magazine (English-speaking Vienne / Charente)
- AngloInfo Poitou-Charentes / Limousin

## Caveats unique to FR

- RVLLH cadastral reform ⚠️ postponed by LFI 2026 (art. 106) to **2028 declarations → 2031 tax impact** → unofficial est. +20–40 % taxe foncière for rural, unverified (2026-07-03 verified — dates per ANIL LF 2026; % unverified)
- DPE F (2028) and E (2034) banned for rental
- Loi Le Meur (Nov 2024) tightens short-let regime
- Service à la personne credit = 50 % deduction for client (huge competitive lever)
- Auto-entrepreneur plafonds change by activity (BIC ≠ BNC ≠ chambres d'hôtes)

## Quirks to know

- The IAL "argiles faible" is for the village center; the DICRIM commune-level RGA map often shows wider areas as Moyen
- Rural communes' collective sewer often only covers Rue Principale + immediate adjacent streets
- Many small départements only count traffic on D-roads with > 500 v/d; smaller D-roads are absent from the count program
- Departmental TFPB rate was merged into communal in the 2021 reform — current rates already reflect this
- Termites zone in Vienne 86 covers 117 communes (arrêté 14 Oct 2020) — but the diagnostic may still be common practice elsewhere

## Verification authorities

- Mairie of the commune (phone in DICRIM)
- Notaire (for tax + sale conformity)
- SPANC (Service Public d'Assainissement Non Collectif) at the communauté de communes level
- ADT / Office de tourisme (for classement meublé tourisme)
- DDT (Direction Départementale des Territoires) for risks

## Leaving France — origin-country deregistration entry points

For FR-resident buyers moving abroad. **Doorway only** — see [`shared/cross-border.md`](../../shared/cross-border.md) for the framework + [`shared/home-tax.md`](../../shared/home-tax.md) § France for tax detail. Mandatory call-out: engage cross-border tax counsel in BOTH jurisdictions before moving the centre of vital interests.

| Register | Action | Authority | URL |
|---|---|---|---|
| Tax residence | File final-year déclaration with foreign address; verify CGI Art. 4 B residence test against destination DTA tie-breaker; flag CGI Art. 167 bis exit-tax check (shareholdings > €800k or > 50% interest) | DGFiP — Particulier international | [impots.gouv.fr/international-particulier](https://www.impots.gouv.fr/les-conventions-internationales) |
| Tax address change | Change adresse fiscale via espace particulier | DGFiP | [impots.gouv.fr](https://www.impots.gouv.fr/) |
| Civil register | No central FR civil register; tax-address change is the binding state notice. Mairie of last residence may also be informed (informal). | Mairie | (commune-level) |
| Health insurance | Notify CPAM; if EU/EEA/CH destination, request **S1 form** via [Reg 883/2004](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883) for transition coverage | Assurance Maladie / CPAM | [ameli.fr](https://www.ameli.fr/) |
| Social security coordination | S1 (EU/EEA/CH) or bilateral totalisation agreement | CLEISS — Centre des Liaisons Européennes et Internationales de Sécurité Sociale | [cleiss.fr](https://www.cleiss.fr/) |
| IFI (wealth tax) | If worldwide RE > €1.3M as FR resident — final-year IFI filing; first non-resident year, IFI scope reduces to French-situs RE only | DGFiP IFI | [impots.gouv.fr/IFI](https://www.impots.gouv.fr/particulier/calcul-de-lifi) |
| France-treaty register (DTA lookup) | Find the relevant FR-destination DTA + tie-breaker article + MLI matches | DGFiP — Conventions fiscales internationales | [impots.gouv.fr/conventions-internationales](https://www.impots.gouv.fr/les-conventions-internationales) |

**Cross-link**: invoke `--cross-border` for the framework (DTA tie-breaker pointer + POEM/PE check + EU/EEA/CH free-movement clarification) and `--home-tax` for France-side annual / disposal / death / emigration detail (Art. 167 bis, IFI, Form 3916, etc.).

## Status

✅ **Fully populated** as of 2026-07-03 (Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged; department-level tax reference re-pointed to DGFiP 2026-09-18 per impots.gouv.fr). Rental / tax tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).

**Confidence**: HIGH for tax + risk + rental sources (impots.gouv.fr / Géorisques / DGFiP — multi-source corroborated). MEDIUM for work catchment heuristics (département-dependent).
