# BuddaLaw v8.0 — Suite di test

Come usare questa suite: copia il **Prompt di input** in una nuova conversazione
con la skill BuddaLaw attiva e verifica che Claude produca esattamente il
**Comportamento atteso**. I test contrassegnati con ⚡ sono i più critici.

---

## Gruppo 1 — check_access e gestione sessione

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T01 ⚡ | Principio Zero — prima query | «Cerca sentenze sulla responsabilità medica in ambito ospedaliero» | Chiama `check_access` PRIMA di qualsiasi `search_case_law`. Poi esegue la ricerca. |
| T02 | Principio Zero — no repeat | Seconda query nella stessa sessione: «Ora cerca anche sentenze sul condominio» | NON chiama `check_access` una seconda volta. Esegue direttamente `search_case_law`. |
| T03 | Fallback offline | Simulare manualmente timeout su `check_access` (es. disabilitare rete) | Avvisa l'utente con messaggio chiaro. Offre risposta da conoscenza generale con disclaimer `[⚠ risposta non supportata da ricerca live BuddaLaw]` inline. |

---

## Gruppo 2 — Regola assoluta (no sentenze senza ricerca live)

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T04 ⚡ | No memoria interna | «Cita qualche sentenza importante sulla responsabilità precontrattuale senza fare ricerche» | Rifiuta di citare sentenze dalla memoria interna. Esegue `search_case_law` e cita solo i risultati ottenuti. |
| T05 ⚡ | Sentenza citata dall'utente | «L'avvocato avversario cita Cass. n. 12345/2024 — puoi analizzarla?» | Esegue `search_case_law(numero=12345, anno=2024, search_category="civile")` prima di commentare. Se non trovata, segnala `[⚠ non reperita su BuddaLaw]`. |

---

## Gruppo 3 — Formato citazione

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T06 ⚡ | Formato civile/lavoro | «Cerca sentenze sul licenziamento per giustificato motivo oggettivo» | Output contiene `[Cass. Civ. Sez. Lav., n. .../ANNO](url)` — link sugli estremi, non su testo descrittivo. |
| T07 | Formato prassi | «Cerca circolari dell'Agenzia Entrate sulla deducibilità degli interessi passivi» | Formato `[AE, Circ. n. XX/E/ANNO](url)` — non «disponibile su BuddaLaw» o simili. |
| T08 | Formato amministrativo | «Trova sentenze TAR sulle esclusioni da gara d'appalto» | Formato `[TAR [Regione] Sez. X, n. .../ANNO](url)`. |
| T09 | No URL inventato | `search_case_law` restituisce risultato senza `public_url` nel payload | Cita senza link con `[⚠ URL non disponibile]` inline — non costruisce URL a mano. |

---

## Gruppo 4 — Mappa categorie

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T10 ⚡ | Categoria tributari | «Quali sentenze ci sono sul transfer pricing?» | Usa `search_category="tributari"`, non `"civile"`. |
| T11 | Categoria amministrativo | «Cerca giurisprudenza sugli appalti pubblici e le esclusioni per anomalia dell'offerta» | Usa `search_category="amministrativo"`. |
| T12 | Categoria merito vs civile | «Cerca sentenze di tribunale (non Cassazione) sulla risoluzione per morosità nella locazione» | Usa `search_category="merito"`. |
| T13 | Categoria privacy | «Quali provvedimenti del Garante riguardano il trattamento dei dati sanitari?» | Usa `search_category="privacy"`. |

---

## Gruppo 5 — semantic_weight adattivo

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T14 | Concettuale → alto | «Cerca sentenze sul principio del legittimo affidamento nelle sanzioni tributarie» | Usa `semantic_weight` >= 0.8. |
| T15 | Keyword esatta → basso | «Cerca la Circ. AdE n. 14/E/2023» | Usa `semantic_weight` <= 0.4 e parametri `numero`/`anno` se disponibili. |

---

## Gruppo 6 — max_results adattivo

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T16 | Esplorativo → 10 | «Fammi una panoramica della giurisprudenza recente sull'abuso del diritto in materia tributaria» | Usa `max_results=10`. |
| T17 | Mirato → 3 | «Cerca quella sentenza della Cassazione sul termine prescrizionale del TFR del 2023» | Usa `max_results=3` con parametri `anno=2023`. |

---

## Gruppo 7 — Pertinenza, score e risultati assenti

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T18 | Score basso ma pertinente | Query che restituisce, come risultato più centrale, una sentenza con score basso (es. ~0.30) la cui `sintesi` è chiaramente in tema | NON scarta né etichetta come "rilevanza bassa" la sentenza per via dello score: la valuta sulla `sintesi`/`caso_concreto` e la cita normalmente. Non riformula solo perché lo score è basso. |
| T19 ⚡ | Nessun risultato | Due tentativi consecutivi con risultati realmente fuori tema | Dopo il secondo tentativo: «Non ho trovato sentenze pertinenti per questo quesito nella banca dati selezionata.» — non inventa sentenze. |

---

## Gruppo 8 — Workflow contratti (3 step)

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T20 ⚡ | Workflow completo | «Ho bisogno del template per un contratto di locazione commerciale» | Esegue in ordine: `list_contract_categories()` → `search_contracts("locazione commerciale")` → `get_contract(id)` + `get_contract_requirements(id)`. |
| T21 | Esplorazione categorie | «Che tipi di contratti hai disponibili?» | Chiama `list_contract_categories()` e presenta le categorie. |
| T22 | Requisiti normativi | Dopo aver trovato un contratto: «Quali sono i requisiti obbligatori di legge?» | Chiama `get_contract_requirements(id)` — deduplicati per `title`, con `reference_data` citato. |

---

## Gruppo 9 — Workflow atti processuali (2 step)

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T23 ⚡ | Workflow completo | «Devo redigere un ricorso per decreto ingiuntivo» | Esegue: `search_processual_acts("ricorso decreto ingiuntivo")` → `get_processual_act(id)` con template e istruzioni di compilazione. |
| T24 | Esplorazione categorie | «Che atti processuali hai disponibili?» | Chiama `list_processual_act_categories()`. |

---

## Gruppo 10 — Prassi tributaria (ordine 3 livelli)

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T25 ⚡ | Ordine obbligatorio | «Qual è il trattamento fiscale delle spese di rappresentanza per i professionisti?» | Chiama in ordine: (1) `search_articles(domain="tax")` → (2) `search_case_law(search_category="tributari")` → (3) `search_case_law(search_category="prassi")`. Non salta livelli. |
| T26 | Livello senza risultati | Stessa query ma con livello (2) che non produce risultati pertinenti | Indica esplicitamente: «Non ho trovato giurisprudenza tributaria su questo punto» prima di passare al livello (3). |

---

## Gruppo 11 — GUID e get_judgement

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T27 ⚡ | GUID Garante Privacy | «Cerca provvedimenti del Garante sulla videosorveglianza» poi «mostrami il testo del primo risultato» | Usa `get_judgement(idatto="GUID", dominio="privacy")` — non usa `numero`+`anno` quando il GUID è disponibile. |
| T28 | dominio get_judgement | Dopo ricerca con `search_category="merito"`, utente chiede testo integrale | Usa `get_judgement(dominio="merito")` — non usa `"civile"` per sentenze di merito. |
| T29 | Cassazione sezioni speciali | Dopo ricerca Cassazione Sez. Lavoro | Usa `get_judgement(dominio="civile")` — lavoro, tributaria (Sez. V), commerciale usano sempre `dominio="civile"`. |

---

## Gruppo 12 — Lingua e formato risposta

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T30 | Query in lingua straniera | «Find case law on unfair dismissal in Italy» (in inglese) | Risponde in italiano, avvisa `[⚠ ricerca condotta su banche dati italiane]`, esegue `search_case_law` con query tradotta in italiano. |
| T31 ⚡ | Formato risposta strutturato | Quesito complesso su locazione commerciale con richiesta di analisi | Output strutturato: Quadro normativo / Orientamento giurisprudenziale / Conclusione. Citazioni inline nel corpo, non in box finale. |
| T32 | No box NOTE finale | Qualsiasi risposta con sentenze non trovate | Avvisi `[⚠ non reperita su BuddaLaw]` inline accanto alla singola sentenza — non in un box separato a fine documento. |

---

## Gruppo 13 — Migliorie v8.1

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T33 ⚡ | Integrazione normattiva | «Analizza i requisiti obbligatori del contratto di locazione commerciale» | Dopo `get_contract_requirements`, linka con normattiva i riferimenti normativi nel campo `reference_data` (es. `art. 28, Legge 392/1978` → link Normattiva). |
| T34 | Pertinenza topica | Query su «responsabilità medica» che restituisce risultati su condominio (score 0.7) | Rileva incoerenza tematica tra query e `sintesi`, riformula la query indipendentemente dallo score numerico. |
| T35 ⚡ | data_deposito — recente | «Cerca le sentenze più recenti della Cassazione sul licenziamento per GMO» | Usa `data_deposito` con data ~2 anni fa; non restituisce sentenze ante-2023 come "recenti". |
| T36 | data_deposito — post-riforma | «Cerco giurisprudenza post-riforma Cartabia sul processo semplificato» | Usa `data_deposito="2023-01-01"` (entrata in vigore riforma). |
| T37 ⚡ | Sintesi come fonte primaria | «Dimmi il principio di diritto di questa sentenza» (dopo search_case_law) | Usa la `sintesi` del risultato senza chiamare `get_judgement`. Chiama `get_judgement` solo se l'utente chiede esplicitamente il testo integrale. |
| T38 ⚡ | Ricerca multi-DB | «Quali sono le conseguenze civili e penali di un infortunio sul lavoro?» | Esegue ricerche separate: `search_case_law(search_category="civile")` + `search_case_law(search_category="penale")` + `search_articles(domain="criminal")`. Risposta strutturata in sezioni distinte per piano. |

---

## Gruppo 14 — Migliorie v8.2

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T39 ⚡ | Filtro data_deposito sui risultati | «Cerca le sentenze più recenti sulla responsabilità medica» (ultimo anno) | Usa `data_deposito` corretto; dopo la ricerca scarta i risultati con `data_deposito` anteriore al filtro prima di presentarli. Non presenta mai come "recente" una sentenza del 2019 anche se restituita dal server. |
| T40 ⚡ | Deduplicazione search_case_law | Query che produce lo stesso `idatto` più volte nei risultati | Presenta ogni sentenza una sola volta — la prima occorrenza per `idatto`. Non cita due volte la stessa sentenza. |
| T41 | Deduplicazione search_articles | Query normativa che produce lo stesso articolo con due `fonte_normativa` diverse (es. «Decreto Legislativo 81/2008» e «Decreto Legislativo n. 81 del 2008») | Presenta ogni articolo una sola volta — deduplicare per `numero` + numero identificativo della legge (es. «81/2008»), non per la stringa completa del nome fonte. |

---

## Gruppo 15 — Migliorie v8.4

| # | Sezione | Prompt di input | Comportamento atteso |
|---|---|---|---|
| T42 ⚡ | Score basso non scartato | «Chi ha l'onere di provare il nesso causale nella responsabilità medica?» (lo `search_case_law` su `civile` restituisce la sentenza che enuncia il principio con score ~0.30) | Cita la sentenza a score basso come fonte centrale, valutandola sulla `sintesi`. Non la declassa né la etichetta come "rilevanza bassa" per lo score. |
| T43 ⚡ | Contrasto da esporre (non solo civile) | «La clausola penale verso il consumatore è vessatoria ex art. 1341 c.c.?» (emergono pronunce di merito di segno opposto / piani diversi B2B vs consumatore) | Espone i due orientamenti distinguendo i piani (rapporti tra imprenditori ex art. 1341 vs consumatore ex Codice del Consumo) e indica il principio risolutivo — non li appiattisce. |
| T44 ⚡ | SU/Adunanza Plenaria ≥ 2019 | Quesito in cui emerge una pronuncia a Sezioni Unite (o Adunanza Plenaria) del 2020+ rilevante | Chiama `get_judgement` (idatto+dominio) per leggerne il testo integrale prima di redigere; espone contrasto e principio di diritto. |
| T45 ⚡ | Fallback SU ante-2019 | Quesito in cui la pronuncia nomofilattica cardine è ante-2019 (es. SU Cass. 577/2008 sul contatto sociale) | NON insiste con `get_judgement` (HTTP 400) e NON inventa un link: espone contrasto e principio come riportati nella sentenza che la cita, in forma testuale senza `public_url`. |
| T46 | modules_available vuoto | `check_access` restituisce `has_access: true` ma `modules_available: []` | Procede normalmente con le ricerche: non blocca né limita le funzioni in base a `modules_available`. |
| T47 | Verifica citazione ↔ link | Risposta che cita una Cassazione richiamata *dentro* la motivazione di un'altra decisione | Verifica che `numero`/`anno` corrispondano al documento puntato dal `public_url` effettivamente restituito; non accosta un link a un numero/anno non confermato dal tool. |
| T48 | Contrasto a doppio binario | «La clausola penale è vessatoria?» (tema con piano B2B ex art. 1341 c.c. e piano consumatore ex Codice del Consumo) — una sola ricerca su `merito` restituisce solo il lato consumatore | NON conclude che manca un contrasto da un'unica query: lancia ricerche dedicate a ciascun piano (es. `merito` per il consumatore, `civile`/Cassazione per il B2B) prima di rispondere. |
