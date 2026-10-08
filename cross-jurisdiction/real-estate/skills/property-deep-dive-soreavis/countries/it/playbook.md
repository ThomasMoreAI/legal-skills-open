# Italy 🇮🇹 — Property Due-Diligence Playbook

ISO2: `it`. Status: ✅ Fully populated (researched 2026-04).

## Country profile

- **Postcode (CAP)**: 5 digits
- **Admin levels**: 20 regioni → 100+ province → 7,900+ comuni → frazioni
- **Currency**: EUR (€)
- **Languages**: Italian + DE (Bolzano), FR (Aosta), SL (FVG), AL (Calabria/Sicilia)
- **Cadastre**: Catasto Nazionale (Agenzia delle Entrate) — visura catastale **FREE since 1 Jan 2025** via SPID/CIE
- **Identifier**: codice catastale comune (4-char alphanumeric, e.g., `H501` for Roma) — different from CAP
- **Massive North/South divide**: prices, services, risks, build quality vary enormously

## Section: `--price`

### Primary sources

- **OMI (Osservatorio del Mercato Immobiliare)** — Agenzia delle Entrate official quotations:
  - Search portal: `https://www1.agenziaentrate.gov.it/servizi/Consultazione/ricerca.htm`
  - Updated semestrally (1° / 2° semestre)
  - Search by: semester + provincia + comune + zona OMI + destinazione d'uso (residenziale, commerciale, etc.)
  - Returns €/m² min-max per zona for each property type
  - Direct dataset: `https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/omi/banche-dati`

- **Visura catastale online** (FREE since 2025) — for actual rendita catastale:
  - `https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/visura-catastale/visura-catastale-online`
  - Access: SPID, CIE, or CNS required
  - Returns: rendita catastale (€/yr base), categoria (A/1-A/11 residential), classe, vani, superficie

- **Sister platform** (paid, for professionals): `https://sister.agenziaentrate.gov.it`

### Listing platforms

- **Immobiliare.it** — largest, full coverage: `https://www.immobiliare.it/<vendita-case>/<provincia>/<comune>/`
- **Idealista.it**: `https://www.idealista.it/<comune>/`
- **Casa.it**: `https://www.casa.it/<comune>/`
- **Subito.it Immobili**: classifieds, smaller listings
- **Tecnocasa, Gabetti** quarterly market reports (PDF)
- **Borsino Immobiliare** valuations

### Compute

1. Listing €/m² = listing price / superficie commerciale (note: commerciale = lordo + balconi × coefficient, may differ from Carrez-equivalent)
2. OMI €/m² gives the official band for the zone — compare
3. Valore catastale = rendita catastale × 1.05 × 160 (residential coefficient) — used for tax calculations
4. **Trap**: superficie commerciale ≠ superficie utile ≠ rendita catastale "vani" — clarify which the listing uses

### Market context

- North (Milano, Bologna, Firenze, Torino): high €/m², high liquidity
- Centro (Roma, Pisa, Perugia): mixed
- Sud (Napoli, Palermo, Bari, Cagliari): lower €/m², lower liquidity
- **Borghi a 1 euro** schemes — mandatory renovation timeline + caution funds (Sicilia, Calabria, Sardegna, Abruzzo, Molise)
- **Centro storico** premium — but heavy Soprintendenza restrictions on any work

---

## Section: `--traffic`

### Primary sources

- **ANAS Osservatorio del Traffico**: `https://www.stradeanas.it/it/osservatorio-del-traffico`
  - Covers strade statali (SS) + autostrade (A) of national interest
  - System: PANAMA (~1,200 sezioni di conteggio, ~1,450 impianti)
  - Reports: monthly, quarterly, annual TGM
- **MIT Open Data**: `https://dati.mit.gov.it/catalog/dataset/traffico-giornaliero-medio-anas`
  - Downloadable CSV/JSON for all ANAS-managed roads
- **Regional/Provincial roads**: each Regione has its own count (often less granular):
  - Piemonte: regione.piemonte.it
  - Lombardia: regione.lombardia.it
  - Toscana: regione.toscana.it
  - etc.
- **Highway operators** (Autostrade per l'Italia, ASPI): `https://www.autostrade.it` — for A-roads

### Compute

- TGM = Traffico Giornaliero Medio Annuo
- Coarse band from OSM `highway` if no count point nearby
- Heavy vehicles % via ANAS report

### Verdict bands (urban / rural Italy)

- 🟢 < 500 v/d (rural strada comunale)
- 🟡 500–2,000 v/d (small SP / SR)
- 🟠 2,000–10,000 v/d (busy SP / urban arterial)
- 🔴 > 10,000 v/d (SS, autostrada, urban core)

---

## Section: `--tax`

### Annual property taxes

**IMU (Imposta Municipale Unica)** — most important:
- **Prima casa NON di lusso** (cat. A/1, A/8, A/9): exempt
- **Seconda casa**: aliquota base 8.6‰ (0.86%); il comune può azzerarla o aumentarla fino a 10.6‰ (1.06%), e fino a 11.4‰ nei soli comuni con ex-maggiorazione TASI (L. 160/2019 art. 1 c. 754-755). Verify the current rate on the comune's IMU page (2026-07-03 verified, source Gazzetta Ufficiale L. 160/2019)
- **Calcolo**: `IMU = rendita catastale × 1.05 × 160 × aliquota`
- Bills: 16 giugno (acconto) + 16 dicembre (saldo), or full payment by giugno
- Reduction for canone concordato: 75% of IMU
- Affitto: comune può abbassare al 4‰

**TASI**: merged into IMU since 2020 (no separate bill)

**TARI (rifiuti)**: communal, ~€100–€500/yr, varies by surface + family size

### Transaction taxes (one-time at purchase)

For **existing residential** (used homes):

| Buyer status | Imposta di registro | Ipotecaria | Catastale |
|---|---:|---:|---:|
| Prima casa | **2 %** of valore catastale (min €1,000) | €50 fixed | €50 fixed |
| Seconda casa / non resident | **9 %** of valore catastale | €50 fixed | €50 fixed |

For **new builds (vendita da impresa)**:
- IVA 4 % (prima casa) or 10 % (standard) or 22 % (lusso)
- Imposta di registro €200, ipotecaria €200, catastale €200

**Notaio fees**: 1.5–2.5 % of price (negotiable; fee tariff abolished 2012)

**Total transaction cost**: typically **+10–13 % on top of price** for prima casa, **+13–17 %** for seconda casa.

### Future risk

- **Riforma del catasto** (cadastral reform) on the political table for years; could double valori catastali if enacted (high impact on IMU + transaction taxes)
- **Imposta patrimoniale** periodically debated nationally; not yet enacted

---

## Section: `--rental`

### Short-term rentals (locazioni turistiche / affitti brevi ≤30 giorni)

**Mandatory: CIN (Codice Identificativo Nazionale) since 1 Jan 2025** (2026-08-07 verified, sources [Ministero del Turismo — Avviso di entrata in funzione della BDSR](https://www.ministeroturismo.gov.it/cin-pubblicato-lavviso-di-entrata-in-funzione-della-banca-dati-strutture-ricettive-e-del-portale-telematico-per-lassegnazione-del-codice); Ministero del Turismo BDSR FAQ, updated 11 May 2026):
- **Legal basis**: art. 13-ter DL 145/2023 conv. L. 191/2023 — became applicable 2 Nov 2024, the 60th day after the Avviso attesting entry into function of the BDSR and its telematic portal was published in Gazzetta Ufficiale (3 Sep 2024); the portal had already opened earlier region-by-region in a sanction-free pilot phase. Obligation to hold a CIN in force from 1 Jan 2025 (Ministero del Turismo notice 22 Oct 2024)
- Does NOT replace regional/provincial codes (CIR etc.): where a regional or provincial code is required, both codes must be obtained and displayed (Ministero del Turismo BDSR FAQ 1.3, updated 11 May 2026)
- Apply at: `https://bdsr.ministeroturismo.gov.it/` (BDSR — Banca Dati Strutture Ricettive)
- Login via SPID or CIE
- Required for: ALL short-term rentals, B&B, casa vacanze, locazione turistica
- Without CIN: cannot list on Airbnb / Booking / Vrbo (platforms must verify)
- **Sanctions applicable from 2 Jan 2025**: €800–€8,000 for absence of CIN; €500–€5,000 for non-display or non-indication of the code — per structure or unit — plus immediate removal of the irregular listing
- Does NOT replace or abolish regional licensing / codes (some regioni still need additional notice to comune)
- Free; alphanumeric code

**Tax regime — Cedolare secca (sostitutiva)** (2026-08-07 verified, sources [L. 199/2025 (Legge di Bilancio 2026) art. 1 c. 17](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199) modifying L. 178/2020 art. 1 c. 595; rate scheme set by L. 213/2023 art. 1 c. 63; underlying regime DL 50/2017 art. 4 commi 2-3; [Agenzia Entrate Locazioni Brevi e Cedolare Secca](https://www.agenziaentrate.gov.it/portale/le-locazioni-brevi-e-la-cedolare-secca)):
- **1° immobile**: 21 % flat (cedolare ridotta) — applies only if a SINGLE property is leased short-term in the tax year
- **2° immobile**: 26 % flat (cedolare ordinaria)
- **Soglia dal 1 gen 2026**: max 2 immobili in cedolare secca per contribuente per periodo d'imposta (era 4 fino al 2025; ridotto da L. 199/2025 art. 1 c. 17). Il ≤2-cap e la presunzione di impresa ≥3 sono la **stessa soglia espressa in due modi**, non due limiti distinti
- **3°+ immobile**: presunzione di legge di attività imprenditoriale ex art. 2082 c.c. → P.IVA obbligatoria, SCIA al comune, tassazione come reddito d'impresa (non IRPEF ordinaria sul reddito da locazione), perdita del regime cedolare (per Guida AdE aprile 2026)
- **Nessun rinvio**: la proroga di sei mesi al 1 lug 2026, circolata come emendamento al Milleproroghe, NON è stata approvata — il testo coordinato del DL 200/2025 conv. L. 26/2026 (GU 28 feb 2026) non contiene alcuna disposizione sulle locazioni brevi; la soglia dei 2 immobili si applica dal 1 gen 2026 (2026-08-07 verified, sources Agenzia delle Entrate + Gazzetta Ufficiale)
- Only for contracts ≤ 30 days
- Optional alternative: regime ordinario IRPEF on rental income

**Other obligations**:
- **Tassa di soggiorno**: collected from guests, set per comune — e.g. Milan 2026 €9.50/n per person for locazioni brevi / B&B (2026 data, source Confcommercio Milano, secondary — verify at the comune's imposta di soggiorno page)
- **Comunicazione alle autorità di PS** — ogni guest registered via Alloggiati Web (Polizia)
- **Ricevuta** issued to guest with marca da bollo if ≥€77.47

### Long-term residential

- **Cedolare secca canone libero**: 21 %
- **Cedolare secca canone concordato**: 10 % (in comuni ad alta tensione abitativa)
- **Regime ordinario IRPEF**: marginal rate

### Strategic notes

- North + tourist hotspots (lakes, Cinque Terre, Toscana, Amalfi, Dolomiti): highest yields
- South (Sicilia, Puglia coast, Sardegna): high seasonality (4-month season concentration)
- **Firenze centro storico STR ban IN FORCE** — regolamento (Del. C.C. 27/2025, in force 31 May 2025; underlying Variante al Piano Operativo Del. C.C. 19 & 20/2025) bans NEW short-term rentals in the UNESCO Nucleo Storico (Zona A): units legally let for tourism in 2024 may continue only under the Tuscan Testo Unico transitional derogation expiring 31 May 2028; adds 5-yr authorisations (lapsing after 12 months' inactivity unless let on contracts over 30 days), 28 sqm minimum apartment size, €1,000–€10,000 sanctions (2025 regolamento, source Comune di Firenze); owner+unit tie and keybox ban per secondary reporting — verify in the Comune di Firenze regolamento text. UPHELD, not overturned: Corte Cost. sent. 186/2025 (16 Dec 2025) validated the framework, then TAR Toscana 14 May 2026 dismissed 19 appeals (sent. 916 & 925/2026); TAR Toscana Sez. I sent. 1752/2026 (9 Sep 2026) again rejected the challenge to the Variante but held a use 'insediato' from the formation of its building title (e.g. SCIA edilizia), so a title formed before the Variante's adoption escapes the ban (one SUAP refusal annulled). EXTENDED to A3/A4 subzones (Campo di Marte, San Jacopino, Gavinana, Statuto-Rifredi, Libertà, Bronzino and other first-ring districts — 67,780 homes / 11.21 km², 2026 data, source Comune di Firenze) by Del. C.C. 28 del 4 Jun 2026, in force 21 Jun 2026 (2026-07-02 verified, sources [Comune di Firenze](https://www.comune.firenze.it/novita/area-stampa/comunicati-stampa/modifica-al-regolamento-affitti-turistici-brevi-il-consiglio); [DirittoPA](https://www.dirittopa.it/it/interventi/urbanistica/affitti-turistici-e-poteri-di-regolazione-comunale))
- Venezia caps tightening
- **Venezia — Contributo di Accesso NOT currently applied**: the €5 day-tripper access fee (€10 if paid in the 3 days before the access day) applied to the **Città antica only** — minor lagoon islands excluded. Exempt: overnight guests in imposta-di-soggiorno accommodation, Venezia/Veneto residents, under-14s, and workers incl. commuters and students. The 2026 run was 60 non-consecutive days, 3 Apr–26 Jul (Fri–Sun plus the 24–30 Apr and 1–7 Jun blocks), under the new regolamento approved by Del. C.C. 190/2025. That sperimentazione **TERMINATED** — the contributo has **NOT been applied since 27 Jul 2026**, with no payment and no exemption request needed; application in 2027 or later requires fresh Comune di Venezia provvedimenti, none approved as of 2026-08-07 (2026-08-07 verified, source [Comune di Venezia — Contributo di Accesso](https://cda.ve.it/it/))
- **Pool / view / parcheggio** = top revenue levers
- **CIR/CIN registration** is the gating step — start there

---

## Section: `--work=<profession>`

### Job platforms

- **InfoJobs.it**, **Indeed.it**, **Subito.it Lavoro**
- **LinkedIn IT** (very active in North + cadres)
- **Monster.it**, **Helpwiz**
- Profession-specific bodies (ordini): albo for lawyers, doctors, architects, engineers, journalists, etc.

### Self-employment

**Partita IVA**:
- **Regime forfettario**: 15 % flat (5 % first 5 yrs) up to €85,000/yr revenue
- **Regime ordinario**: marginal IRPEF + INPS gestione separata
- Profession-specific casse (architects, ingegneri, avvocati, etc.)

### Healthcare / regulated professions

- Doctolib (medici, fisioterapisti)
- iscrizione albo + insurance mandatory

### Catchment

- Italy is more concentrated than France — most provinces have a clear capital with most services
- Within 30 min of a provincia capital = decent catchment
- Sub 1,000-pop comuni in Sud / Appennino are very thin markets

---

## Section: `--risks`

### Primary national sources

| Source | URL | What it gives |
|---|---|---|
| **IdroGEO (ISPRA)** — hydrogeological dissesto | `https://idrogeo.isprambiente.it/app/` | Address-level rischio frane + alluvioni P1/P2/P3/P4 |
| **IdroGEO Hazard & Risk** | `https://idrogeo.isprambiente.it/app/pir` | Aggregated risk indicators |
| **ISPRA flood maps (PGRA)** | `https://www.isprambiente.gov.it/pre_meteo/idro/Mappe_peric.html` | River basin flood hazard maps |
| **INGV MPS04 sismicità** | `http://esse1-gis.mi.ingv.it/` | PGA per cell at 0.05° resolution |
| **INGV zone sismiche** | `http://zonesismiche.mi.ingv.it/` | Zona 1/2/3/4 per comune |
| **Istat Mappa dei rischi** | `https://www.istat.it/.../mappa-dei-rischi-dei-comuni-italiani/` | Aggregated risk dashboard per comune |
| **Protezione Civile rischio vulcanico** | `https://www.protezionecivile.gov.it` | Vulcanic risk Vesuvio/Etna/Stromboli/Campi Flegrei |
| **ARPA regionali** | varies (see below) | Air quality, water, waste, soil pollution |
| **SNPA** (national env. system) | `https://www.snpambiente.it/` | Aggregator of all 21 ARPAs |

### ARPA regional portals (verify pollution / contaminated sites)

| Regione | Portal |
|---|---|
| Lombardia | `https://www.arpalombardia.it` |
| Veneto | `https://www.arpa.veneto.it` |
| Emilia-Romagna | `https://www.arpae.it` |
| Toscana | `https://www.arpat.toscana.it` |
| Lazio | `https://www.arpalazio.it` |
| Sicilia | `https://www.arpa.sicilia.it` |
| Piemonte | `https://www.arpa.piemonte.it` |
| Sardegna | `https://www.arpa.sardegna.it` |
| Campania | `https://www.arpacampania.it` |
| (and 12 others — all linked via SNPA) | |

### Seismic zoning (CRUCIAL for Italy)

INGV MPS04 classifies every comune into:
- **Zona 1** — high (PGA > 0.25g) — most of Calabria, Sicilia centro-orientale, Friuli, Marche/Umbria interno, Abruzzo, central Appennini
- **Zona 2** — medium-high — most of Centre + South Italy
- **Zona 3** — medium — Po valley, Sardegna nord, parts of North
- **Zona 4** — low (only Sardegna and parts of Veneto, FVG, Liguria)

**Build-era hazards** depend on zone × age:
- **Pre-1974**: pre-seismic standards. **DANGEROUS** in zone 1/2.
- **1974–1996**: incremental improvements (Legge 64/1974, DM 03/03/1975)
- **1996–2003**: OPCM 3274/2003 transition
- **Post-2008**: NTC 2008 (proper modern seismic)
- **Post-2018**: NTC 2018 (current standard)

L'Aquila (2009), Amatrice/Norcia (2016) are the recent reminders.

### Other build-era hazards

- **Amianto (asbestos)**: pre-1992 builds very likely (eternit, copertura, tubazioni). Smaltimento mandatory if friabile. Cost: est. €15–€60/m² removal (verify with licensed smaltimento operator quote; cf. roof-removal benchmark below).
- **Aluminosis** (Italian variant): rare, but check 1960s–70s edilizia popolare
- **Vespasiano / Roma 1950s-70s**: scarce concrete, possible.

### Mandatory diagnostics at sale (NULLITY-RISK level)

| Document | Required because | Risk if missing |
|---|---|---|
| **APE (Attestato Prestazione Energetica)** | All sales (announcement must show class) | Sale cannot complete |
| **Conformità urbanistica** | Post-17 March 1985 builds — must declare titoli abilitativi | **NULLITÀ DELL'ATTO** |
| **Conformità catastale** | DL 78/2010, all sales | **NULLITÀ** |
| **Certificato impianti** (elettrico, idrico, termico) | DM 37/2008, all installations after 1990 | Sale possible but acquirente liability |
| **Libretto impianto termico** | All boilers + AC | Mandatory transfer |
| **Visura catastale aggiornata** | All sales | Identifies any difformità |
| **Visura ipotecaria** | Mortgage / liens check | Sale risk |

### Abuso edilizio risk (Italy-specific, CRITICAL)

- Italy has chronic illegal-building issues, particularly in Sud + coastal
- Three condono windows expired (1985, 1994, 2003)
- Today: only **sanatoria ordinaria** with **doppia conformità** (current rules + rules at time of build)
- **If unresolved abuso**: atto può essere null; acquirente eredita l'obbligo di demolizione
- Pre-rogito: technician must verify conformità urbanistica vs catastale vs stato di fatto
- Common abusi: verandas, soppalchi, frazionamenti, cambi destinazione d'uso

**Always commission a tecnico (geometra/architetto)** for pre-rogito conformità check on any property >20 yrs old. Cost: €300–€1,000.

### Climate change projections (CMCC / ISPRA)

- Drought intensifying esp. Po basin + Sardegna + Sicilia
- Sea-level rise: Venezia, Adriatico nord, Mar Tirreno coasts
- Glacial retreat: Alpi (impact on alpine real estate)
- Wildfires up: Sicilia, Sardegna, Calabria, Basilicata
- Mediterranean storms increasing

---

## Section: `--mains`

### Primary sources

- **ARERA ATID (Anagrafica Territoriale Servizio Idrico Integrato)**: `https://www.arera.it/area-operatori/atidrhtm`
  - Definitive list of which gestore covers which comune
  - ~2,399 gestori in IT (1,997 enti locali + 394 aziende + 8 multiutility quotate) — verify current count at arera.it (ATID portal above)
- **Comune** + **gestore idrico locale** (acquedotto + fognatura + depurazione typically same operator)

### Major water operators (regional/multiutility)

| Operator | Coverage |
|---|---|
| **Acea** | Roma + Lazio |
| **Iren** | Liguria, Piemonte, Emilia |
| **A2A / SAL** | Lombardia (Milano + Brescia areas) |
| **Hera** | Emilia-Romagna |
| **Smat** | Torino metropolitana |
| **Acqualatina** | Lazio sud |
| **Mediterranea delle Acque** | Genova |
| **Publiacqua** | Toscana centro |
| **GAIA / GORI / Acquedotto Lucano** | regional Sud |

### Verification

- Most centro storico + recent suburbs: mains universal
- Rural Sud + Appennino frazioni montane often on **fossa biologica / Imhoff**
- Listing keywords: "fognatura" / "scarico in pubblica fognatura" / "fossa biologica" / "vasca Imhoff" / "subirrigazione"

### Costs

| Scenario | Cost |
|---|---:|
| Connection to mains where available | €1,500–€4,000 |
| Septic to mains conversion | €5,000–€15,000 |
| New fossa biologica + filtro | €3,000–€8,000 |
| Imhoff replacement | €5,000–€10,000 |

---

## Cost benchmarks (IT 2026)

| Work | Cost |
|---|---:|
| APE | €100–€300 |
| Visura catastale (FREE since 2025 via SPID) | €0 |
| Notaio | 1.5–2.5 % of price |
| Imposta di registro (prima casa) | 2 % of valore catastale |
| Imposta di registro (seconda casa) | 9 % of valore catastale |
| IVA new build (standard) | 10 % |
| Tecnico per conformità (geometra) | €300–€1,000 |
| Septic to mains | €5,000–€15,000 |
| Roof (terracotta tiles, 200 m²) | €15,000–€30,000 |
| Antiseismic retrofit (small house) | €30,000–€80,000 (Sismabonus 50 % prima casa / 36 % seconda nel 2025-2026) |
| Asbestos removal (200 m² roof) | €5,000–€15,000 |
| Energy retrofit (Ecobonus 50 %) | €20,000–€60,000 |
| **Total transaction cost (prima casa)** | ~10–13 % over price |
| **Total transaction cost (seconda casa)** | ~13–17 % over price |

## Active fiscal incentives (2025)

- **Sismabonus** prima casa **50 %** / seconda **36 %** (2025 e 2026 — decalage sospeso da [L. 199/2025 art. 1 c. 22](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199) modificante DL 63/2013 art. 16); 36 %/30 % programmato per 2027 salvo proroga; cap €96,000/unit; spread su 10 quote annuali; statute underlying: art. 16-bis TUIR (DPR 917/1986) + art. 16 c. 1-septies DL 63/2013 per acquisti (2026-05-27 verified, sources normattiva.it L. 199/2025 + DL 63/2013)
- **Ecobonus** energy retrofit: 50 % prima casa / 36 % seconda (2025-2026)
- **Bonus Ristrutturazione**: 50 % up to €96k; cap aliquote scendono progressivamente
- **Superbonus 110 %** sostanzialmente concluso; trasceso a 65 % e poi a regime ordinario
- **Bonus Mobili**: legato a ristrutturazione, 50 % up to €5k

## Common listing platforms

- **Immobiliare.it** — largest, full extraction
- **Idealista.it** — modern, mobile-friendly
- **Casa.it** — good for Sud
- **Wikicasa, Bakeca** — secondary
- **Subito.it** — privates, attention to abusi
- **Tecnocasa, Gabetti, RE/MAX** — agency networks

## Caveats unique to IT

- **Conformità urbanistica + catastale = nullità rischio** — never sign without tecnico verification
- **Abuso edilizio** epidemic, especially Sud + coastal — pre-rogito audit is mandatory
- **Centro storico + paesaggistica vincolo**: any work requires Soprintendenza approval (3–12 month delays)
- **CIN obbligatorio dal 1 gen 2025** for any short-term rental — without it, cannot list; sanzioni dal 2 gen 2025: €800–€8,000 per assenza di CIN, €500–€5,000 per mancata esposizione o indicazione del codice (per struttura o unità), più rimozione immediata dell'annuncio irregolare
- **Cedolare secca limit 2 properties from 1 Jan 2026** (nessun rinvio: l'emendamento Milleproroghe al 1 lug 2026 non è stato approvato) — affects rental investment math
- **Nord/Sud disparity**: massive gap in services, tax, value, liquidity
- **Borghi a 1 euro** schemes: cheap entry but mandatory €20k–€50k renovation timeline + caution fund (often €5,000–€10,000)
- **Diritti reali**: usufrutto, servitù di passaggio, prelazione agraria — careful notaio review

## Reddit / forum sources

- **r/italy** (Italian-language)
- **r/AskItalia**, **r/ItalyExpat**
- **CodicePedone.it forum**, **Idealista.it news section**
- **Forum BastaBidaste** for real-estate insiders
- Expat communities: **The Local Italy**, **Italian Property Insider**, **InTuscany**

## Verification authorities

| Authority | When to call |
|---|---|
| **Comune** (Ufficio Tecnico) | Conformità urbanistica + IMU + permesso di costruire |
| **Agenzia delle Entrate** | Visura catastale + rendita + OMI |
| **Catasto comunale** | Conformità catastale |
| **Notaio** | Final compravendita + visure ipotecarie + sanity check |
| **Tecnico (geometra/architetto)** | Pre-rogito conformità audit (MANDATORY) |
| **Gestore idrico** (ARERA list) | Mains drains verification |
| **ARPA regionale** | Pollution / soil contamination |
| **Soprintendenza** | If centro storico / vincolo |

## Quirks to know

- **OMI quotations are zonal (per zona OMI within comune)** — listing might be in a different zona than the comune average; always check zone-specific OMI for accurate comparison
- **Superficie commerciale** (used in listings) ≠ superficie utile/Carrez ≠ rendita catastale "vani" — never compare €/m² across these naïvely
- **CAP can span multiple comuni** in Italy (unlike France 1 CAP = 1 comune typically); verify codice catastale comune for accurate lookup
- **Rendita catastale revaluation 1.05** dates from 1996; multiple political pushes for cadastre reform have stalled
- **Polizza Catastrofale (CatNat) obbligatoria per le imprese — in vigore per tutte le categorie tranne pesca/acquacoltura (termine prorogato al 31 dic 2026), entrata scaglionata**: grandi imprese entro 31 mar 2025, medie entro 30 set 2025, micro/piccole entro 31 dic 2025; micro/piccole turistico-ricettive e somministrazione prorogate al 31 mar 2026 (DL 200/2025 Milleproroghe, conv. L. 26/2026); pesca/acquacoltura prorogate al 31 dic 2026 (DL 25/2026 art. 9 c. 6, conv. L. 59/2026). Inadempienza = se ne tiene conto nell'assegnazione di contributi, sovvenzioni e agevolazioni pubbliche (L. 213/2023 art. 1 c. 102); il DM MIMIT 18 giu 2025 subordina all'adempimento l'accesso alle agevolazioni DGIAI elencate nel decreto. NON ancora residenziale, ma worth noting (2026-07-03 verified, source MIMIT polizze rischi catastrofali Cat Nat)

## Source URL templates

| Source | URL pattern |
|---|---|
| OMI search | `https://www1.agenziaentrate.gov.it/servizi/Consultazione/ricerca.htm` |
| Visura catastale (SPID) | `https://www.agenziaentrate.gov.it/portale/schede/fabbricatiterreni/visura-catastale/visura-catastale-online` |
| IdroGEO | `https://idrogeo.isprambiente.it/app/` |
| INGV MPS04 | `http://esse1-gis.mi.ingv.it/` |
| INGV zone sismiche | `http://zonesismiche.mi.ingv.it/` |
| ANAS open data | `https://dati.mit.gov.it/catalog/dataset/traffico-giornaliero-medio-anas` |
| BDSR Ministero Turismo (CIN) | `https://bdsr.ministeroturismo.gov.it/` |
| ARERA ATID | `https://www.arera.it/area-operatori/atidrhtm` |
| SNPA | `https://www.snpambiente.it/` |
| Immobiliare.it search | `https://www.immobiliare.it/vendita-case/<provincia>/<comune>/` |
| Idealista.it | `https://www.idealista.it/<comune>/` |
| Istat mappa rischi | `https://www.istat.it/statistiche-per-temi/focus/informazioni-territoriali-e-cartografiche/rappresentazioni-cartografiche-interattive/mappa-dei-rischi-dei-comuni-italiani/` |

## Status

✅ **Fully populated** (initially populated 2026-04-25).
**Last verified**: 2026-08-07 (`--rental` re-verified — CIN block against Ministero del Turismo BDSR, the cedolare secca property threshold, and the Venice Contributo di Accesso season; balance of playbook 2026-07-03 Tier-A quarterly refresh — fast-moving claims re-verified; structural sections unchanged). Insurance / rental tracker entries re-checked 2026-09-24 (October and November regwatch waves, the November wave run early; see shared/regulatory-watch.md).
**Coverage check**: pricing, traffic, tax, rental, work, risks, mains all have primary government sources + cost benchmarks + caveats.
**Confidence**: HIGH for tax + risk + rental sources (multi-source corroborated). MEDIUM for work catchment heuristics (region-dependent).

## Extension TODOs (deepen on first real run)

- [ ] Per-regione CIN/short-let regional addenda (Veneto, Lombardia, Toscana, Lazio specifics)
- [ ] OMI zona-coding lookup for major comuni (Roma centro vs Roma periferia)
- [ ] Sismabonus tracking as 2025 → 2026 → 2027 percentages decline
- [ ] Sanatoria / abuso edilizio detection workflow (likely needs tecnico in person)
- [ ] Local IMU aliquota per comune (need scraping per ~7,900 comuni — start with top 100)
- [ ] Nord/Sud cost-benchmark differentiation (renovation prices differ ~30–50 %)
