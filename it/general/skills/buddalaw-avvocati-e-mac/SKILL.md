---
name: buddalaw-avvocati-e-mac
title: BuddaLaw — Istruzioni comportamentali cross-runtime
description: 'Ricerca live di sentenze, normativa, contratti e atti processuali italiani tramite il server MCP BuddaLaw. Gestisce Cassazione (civile, penale, lavoro, tributaria), merito, TAR/Consiglio di Stato, Corti di Giustizia Tributaria, Garante Privacy, prassi Agenzia Entrate, template contrattuali e atti processuali. MANDATORY TRIGGERS: qualsiasi quesito che richieda di cercare, citare o verificare sentenze italiane; analisi o redazione di contratti; redazione di atti processuali; ricerca di prassi tributaria o provvedimenti del Garante; qualsiasi richiesta esplicita di usare BuddaLaw o le sue banche dati. ATTIVARE SEMPRE prima di rispondere a domande giuridiche che richiedono fonti citabili e aggiornate.'
author: avvocati-e-mac
author_url: https://github.com/avvocati-e-mac/skill-legali/tree/main/buddalaw/buddalaw
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: general
language: it
sources:
- title: Query Examples
  path: references/query-examples.md
- title: Test Suite
  path: references/test-suite.md
- title: Tool Reference
  path: references/tool-reference.md
---

# BuddaLaw — Istruzioni comportamentali cross-runtime

---

## COMPATIBILITÀ RUNTIME

Questa skill deve funzionare sia in ambienti Claude sia in ambienti OpenAI/Codex.

- **Se stai operando in Claude Desktop, Claude for Work/Cowork o Claude Code:** usa i tool MCP BuddaLaw esposti con i nomi logici indicati sotto (`check_access`, `search_case_law`, `get_judgement`, ecc.).
- **Se stai operando in Codex o in un ambiente OpenAI:** usa i tool MCP BuddaLaw disponibili nell'ambiente corrente (es. namespace `mcp__buddalaw` in Codex) mantenendo la stessa logica e gli stessi parametri descritti in questa skill.
- **Se i tool BuddaLaw non sono disponibili:** non citare giurisprudenza specifica dalla memoria interna. Dichiarare l'indisponibilità e offrire una risposta generale non supportata da ricerca live.

---

## PRINCIPIO ZERO — Verifica accesso

Chiamare `check_access` **una sola volta per sessione**, alla prima query che
attiva questa skill. Non richiamare nelle query successive della stessa sessione.

`check_access` serve **solo come gate di accesso** (verificare che l'abbonamento
sia attivo). Non far dipendere alcuna logica dal campo `modules_available`: può
tornare vuoto (`[]`) anche con accesso pienamente attivo. Se `has_access` è vero,
procedere con le ricerche indipendentemente da `modules_available`.

**Se `check_access` restituisce errore o timeout:**
> «Non riesco a raggiungere BuddaLaw in questo momento. Verifica che il tuo
> abbonamento sia attivo oppure riprova tra qualche minuto.»

Non riprovare in loop. Offrire di rispondere sulla base della conoscenza
generale dell'assistente, aggiungendo sempre — inline, non in un box finale:
`[⚠ risposta non supportata da ricerca live BuddaLaw — potrebbe non essere aggiornata]`

---

## REGOLA ASSOLUTA — Nessuna sentenza senza ricerca live

Non citare mai sentenze, ordinanze, provvedimenti o decisioni specifiche
(numero, anno, organo) basandosi sulla memoria interna dell'assistente. Ogni
riferimento giurisprudenziale citato deve provenire da una chiamata live a
`search_case_law` o `get_judgement` effettuata nella conversazione corrente.

Se l'utente cita una sentenza nel proprio messaggio (es. "Cass. n. 12345/2024"),
non usarla direttamente: eseguire prima `search_case_law` con `numero` e `anno`
per ottenere il `public_url` reale, poi citare con link.

Se la ricerca non trova la sentenza → citare come testo semplice senza link,
con indicazione inline: `[⚠ non reperita su BuddaLaw]`

---

## REGOLA CITAZIONE — Formato unico

Il formato è uno solo per tutte le banche dati:

```
[ORGANO Sez. XXX, n. NUMERO/ANNO](public_url)
```

Il `public_url` viene **sempre dal tool** — mai costruito a mano o inventato.
Se il tool non restituisce un URL valido, citare senza link con
`[⚠ URL non disponibile]` inline.

**Il link va sugli estremi della sentenza** — mai su "leggi qui", "testo
integrale", "disponibile su BuddaLaw" o simili.

| Banca dati | Esempio formato corretto |
|---|---|
| `civile` | `[Cass. Civ. Sez. II, n. 1234/2024](url)` |
| `civile` (lavoro) | `[Cass. Civ. Sez. Lav., ord. n. 12056/2026](url)` |
| `penale` | `[Cass. Pen. Sez. III, n. 5678/2023](url)` |
| `tributari` | `[CGT I grado Milano, n. 890/2024](url)` |
| `merito` | `[Trib. Roma, n. 2345/2023](url)` |
| `amministrativo` | `[TAR Lazio Sez. I, n. 567/2024](url)` |
| `privacy` | `[Garante Privacy, provv. n. 9920814/2023](url)` |
| `prassi` | `[AE, Circ. n. 14/E/2023](url)` |

Nessun disclaimer o NOTE box a fine documento: eventuali avvertenze vanno
inline, accanto alla singola voce interessata.

**Verifica citazione ↔ link.** Prima di scrivere `numero`/`anno` accanto a un
`public_url`, verifica che corrispondano al **documento effettivamente restituito**
dal tool e puntato da quell'URL. È facile, soprattutto in Cassazione, confondere un
numero citato *dentro* la motivazione con quello della decisione recuperata. Un
link che punta a un numero/anno diverso da quello citato è un errore grave: **mai
citare un numero/anno non confermato da una risposta del tool.**

---

## MAPPA DECISIONALE — Quale tool usare

### A. Ricerca giurisprudenziale generica → `search_case_law`

```
search_case_law(
  query="...",
  search_category="...",
  max_results=5,
  semantic_weight=0.7
)
```

**Mappa materia → `search_category`:**

| Materia | `search_category` |
|---|---|
| Contratti, obbligazioni, famiglia, proprietà, successioni | `civile` |
| Responsabilità civile, risarcimento danni | `civile` |
| Lavoro dipendente, licenziamento, sindacale | `civile` |
| Reati, pene, misure cautelari, processo penale | `penale` |
| IVA, imposte dirette, accertamento, riscossione | `tributari` |
| Provvedimenti, circolari, interpelli Agenzia Entrate | `prassi` |
| Tribunali e Corti d'Appello (civile, commerciale, lavoro) | `merito` |
| Provvedimenti del Garante della Privacy, GDPR | `privacy` |
| TAR, Consiglio di Stato, appalti pubblici, PA | `amministrativo` |

**`semantic_weight` — regola dinamica:**
- Default `0.7` per ricerche miste (concetto + parole chiave)
- Verso `0.9–1.0` per query concettuali descrittive (es. "principio di proporzionalità nella sanzione disciplinare")
- Verso `0.3–0.5` per termini tecnici esatti, numero di circolare o nome
  specifico di istituto giuridico

**`max_results` — regola adattiva:**
- `3` per ricerche mirate su sentenza specifica già nota
- `5` default
- `10` per ricerche esplorative/panoramiche tematiche

**Dopo ogni ricerca — pertinenza, non score:**

Il motore semantico **restituisce sempre risultati**, anche per query fuori tema:
non torna mai a vuoto. Di conseguenza **lo score è solo indicativo e non è
affidabile in nessuna delle due direzioni**:
- uno score **alto non garantisce** pertinenza (può essere il "vicino" vettoriale
  di una query mal posta);
- uno score **basso non significa** irrilevanza: una sentenza con score basso
  (es. 0.30) può essere proprio quella che **enuncia il principio di diritto
  centrale** sul quesito.

Regole operative:
- **Decidi la pertinenza leggendo `sintesi`/`caso_concreto`, non il numero di
  score.** Verifica che il contenuto sia tematicamente coerente con la query.
- **Non scartare né declassare** una sentenza pertinente solo perché ha score
  basso. Non aggiungere etichette di "rilevanza bassa" basate sullo score.
- **Riformula la query solo quando il *contenuto* dei risultati è fuori tema**
  (es. query su contratti di lavoro → risultati su diritto penale), non quando lo
  score è semplicemente basso. Per riformulare, usa termini più specifici o un
  `semantic_weight` diverso.
- Dopo 2 tentativi con risultati realmente fuori tema → comunicare
  esplicitamente: «Non ho trovato risultati pertinenti per questo quesito nella
  banca dati selezionata.»

**Ricerche temporali:**
Usare `data_deposito="YYYY-MM-DD"` quando l'utente chiede sentenze recenti, post-riforma o di un periodo specifico:
- «sentenze recenti» → `data_deposito` = 2 anni fa dalla data odierna
- «post-riforma Cartabia» → `data_deposito="2023-01-01"`
- «ultimo anno» → `data_deposito` = 1 anno fa dalla data odierna

**Attenzione:** il server non garantisce il filtraggio rigoroso per data. Dopo ogni ricerca con `data_deposito`, verificare il campo `data_deposito` di ciascun risultato e scartare quelli con data anteriore al limite indicato prima di presentarli all'utente.

---

### B. Sentenza specifica nota (numero + anno)

```
search_case_law(
  query="breve descrizione materia",
  search_category="civile",
  numero=12345,
  anno=2024,
  max_results=3
)
```

Se non trovata con `search_case_law`, tentare:

```
get_judgement(
  dominio="civile",
  numero=12345,
  anno=2024
)
```

---

### C. Gestione idatto GUID (Garante Privacy, CGT, prassi)

Alcune banche dati restituiscono `idatto` come GUID
(es. `"a1b2c3d4-e5f6-7890-abcd-ef1234567890"`). In tal caso:

- **Preferire il GUID** rispetto a numero+anno — è identificatore primario
- Se `public_url` è già nel risultato di `search_case_law`, usarlo direttamente
- Se serve il testo completo:

```
get_judgement(
  idatto="a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  dominio="privacy"
)
```

Non richiamare `get_judgement` con `numero`+`anno` quando si dispone del GUID.

**Regole `dominio` per `get_judgement`:**

| Organo | `dominio` |
|---|---|
| Cassazione civile, lavoro, commerciale, tributaria (Sez. V) | `civile` |
| Cassazione penale | `penale` |
| Corti di Giustizia Tributaria | `tributario` |
| Tribunali e Corti d'Appello | `merito` |
| TAR e Consiglio di Stato | `amministrativo` |
| Garante della Privacy | `privacy` |
| Circolari e interpelli AE | `tributario-prassi` |

---

### D. Analisi o redazione contratto — workflow 3 step

**Step 1** — Identifica le categorie disponibili:
```
list_contract_categories()
```

**Step 2** — Cerca il template pertinente:
```
search_contracts(query="nome tipo contratto")
```
oppure esplora per categoria:
```
list_contracts(category_id="...")
```

**Step 3** — Recupera template e requisiti normativi:
```
get_contract(contract_id="...")
get_contract_requirements(contract_id="...")
```

Usare `get_contract_requirements` per elencare i requisiti di legge obbligatori
prima di redigere o analizzare il contratto. I requisiti `general` vengono
spesso restituiti in duplicato: deduplicare per `title` prima di presentarli.
Ogni requisito include `reference_data` con fonte normativa: citarla sempre.

---

### E. Ricerca normativa → `search_articles`

```
search_articles(
  query="...",
  domain="...",
  max_results=5
)
```

**Mappa materia → `domain`:**

| Materia | `domain` |
|---|---|
| Contratti, obbligazioni, famiglia, proprietà | `civil_code` |
| Processo civile ordinario | `civil_procedure` |
| Leggi speciali (locazioni, consumatori, lavoro) | `special_civil` |
| Riti speciali (ATP, ingiunzione, ecc.) | `special_civil_procedure` |
| Codice penale e processo penale | `criminal` |
| IVA, imposte dirette, accertamento | `tax` |
| GDPR, Codice Privacy, dati personali | `privacy` |

---

### F. Atti processuali — workflow 2 step

**Step 1** — Identifica il tipo di atto:
```
list_processual_act_categories()
```
oppure cerca direttamente:
```
search_processual_acts(query="nome atto processuale", max_results=5)
```

**Step 2** — Recupera template e istruzioni di compilazione:
```
get_processual_act(act_id="...")
```

Il template restituito da `get_processual_act` contiene le istruzioni di
compilazione: seguirle rigorosamente.

---

### H. Quesiti trasversali — ricerca multi-DB

Quando un quesito tocca più piani del diritto (es. responsabilità civile e penale, lavoro e privacy, contratto e inadempimento tributario), eseguire ricerche separate per ogni banca dati rilevante e integrare i risultati nella risposta con sezioni distinte.

**Ordine di esecuzione:**
1. Prima la banca dati principale (dove risiede il principio cardine del quesito)
2. Poi le banche dati accessorie (per profili specifici o rimedi processuali)
3. Infine la normativa con `search_articles` per la base legislativa

**Esempi di combinazioni frequenti:**

| Quesito | DB principali | DB accessori |
|---|---|---|
| Infortunio sul lavoro | `civile` (Cassazione) | `penale`, `merito` |
| Licenziamento discriminatorio | `civile` | `privacy` (se dati personali coinvolti) |
| Appalto + inadempimento fiscale | `civile` | `tributari`, `amministrativo` |
| Data breach con danno al dipendente | `privacy` | `civile`, `merito` |

Non eseguire più di 3 ricerche parallele per lo stesso quesito senza presentare i risultati intermedi all'utente.

---

### G. Prassi tributaria — ordine obbligatorio a 3 livelli

Per qualsiasi quesito su IVA, imposte dirette, accertamento o riscossione,
seguire obbligatoriamente questo ordine:

1. **Normativa:** `search_articles(domain="tax", query="...")`
2. **Giurisprudenza tributaria:** `search_case_law(search_category="tributari", query="...")`
3. **Prassi amministrativa:** `search_case_law(search_category="prassi", query="...")`

Non saltare livelli. Se un livello non produce risultati pertinenti, indicarlo
esplicitamente prima di passare al successivo.

---

## REGOLE TRASVERSALI

1. **Mai rispondere a domande giuridiche senza aver chiamato almeno un tool
   BuddaLaw** — anche quando si conosce la risposta: il tool fornisce fonti
   citabili e aggiornate.

2. **Lingua:** Rispondere sempre in italiano, indipendentemente dalla lingua
   della domanda. Se la query arriva in un'altra lingua, rispondere in italiano,
   eseguire la ricerca con query tradotta in italiano, e avvisare l'utente:
   `[⚠ ricerca condotta su banche dati italiane]`

3. **Query:** Usare sempre linguaggio naturale giuridico italiano nelle query
   ai tool (es. `"risoluzione contratto locazione commerciale morosità"`).
   Evitare keyword isolate o abbreviazioni.

4. **`check_access`** va chiamato solo alla prima query della sessione.

5. **Usare la `sintesi` come fonte primaria**: il campo `sintesi` restituito da
   `search_case_law` è sufficiente per citare il principio di diritto e il caso
   concreto. Chiamare `get_judgement` solo se: (a) l'utente chiede esplicitamente
   il testo integrale; (b) serve estrarre un passaggio specifico della motivazione;
   (c) la sintesi è generica o assente; (d) **emerge una pronuncia nomofilattica o
   un contrasto** — in tal caso la lettura integrale è obbligatoria (vedi «REGOLA
   QUALITÀ — Sezioni Unite e contrasti»). Fuori da questi casi non chiamare
   `get_judgement` di default.

6. **Parametri `ufficio` e `giudice`**: usarli quando l'utente specifica un
   organo giudiziario o un giudice estensore noto.

7. **Mai inventare**: se non viene trovata una sentenza, non citarne una
   "simile" dalla memoria interna. Dichiarare esplicitamente: «Non ho trovato
   sentenze pertinenti su questo punto nella ricerca condotta.»

8. **Deduplicazione risultati**: prima di presentare i risultati, rimuovere i duplicati:
   - `search_case_law`: deduplicare per `idatto` — trattenere la prima occorrenza.
   - `search_articles`: deduplicare per `numero` + numero identificativo della legge estratto da `fonte_normativa` (es. «81/2008», «392/1978»). Il server restituisce varianti dello stesso atto con nomi diversi («Decreto Legislativo 81/2008» e «Decreto Legislativo n. 81 del 2008» sono lo stesso atto) — trattarle come duplicate.
   - `get_contract_requirements`: deduplicare per `title` (già previsto nella sezione D).

---

## REGOLA QUALITÀ — Sezioni Unite e contrasti (MANDATORY)

Vale per **tutti gli ambiti**, non solo il civile: civile, penale, lavoro,
tributario e amministrativo.

Quando una ricerca fa emergere una **pronuncia nomofilattica rilevante** o
**decisioni di segno opposto** sul punto, l'esposizione del contrasto è
**obbligatoria**: ometterla è un difetto della risposta anche se il resto è
corretto. Si considerano nomofilattiche:

- **Cassazione a Sezioni Unite** (civile, penale, lavoro, tributaria);
- **Adunanza Plenaria del Consiglio di Stato** (amministrativo);
- principi di diritto **consolidati** richiamati come tali.

In presenza di una di queste pronunce o di orientamenti contrastanti, l'assistente
**DEVE**:
1. **esporre i due (o più) orientamenti in contrasto** che hanno dato origine alla
   questione (distinguendo, dove serve, i piani diversi — es. rapporti tra
   imprenditori vs consumatore, civile vs penale);
2. **spiegare come la pronuncia nomofilattica ha risolto il contrasto**, enunciando
   il **principio di diritto** affermato.

**Il contrasto può non emergere da una sola query.** Quando il tema ha un **doppio
binario** (es. clausola vessatoria tra imprenditori ex art. 1341 c.c. *vs* verso il
consumatore ex Codice del Consumo; responsabilità civile *vs* penale; tutela reale
*vs* obbligatoria), una sola ricerca tende a restituire solo uno dei due piani. Per
questi temi **lancia ricerche dedicate a ciascun piano** — anche su banche dati
diverse (es. `merito` per il lato consumeristico, `civile`/Cassazione per il lato
B2B) — **prima di concludere che non esiste contrasto**. Non dedurre l'assenza di
orientamenti opposti da un'unica query.

**Lettura integrale (≥ 2019).** Per una SU / Adunanza Plenaria rilevante **del 2019
o successiva**, leggere il **testo integrale** con `get_judgement` (via
`idatto`+`dominio`) prima di redigere: non fidarsi del solo chunk né di una
citazione di seconda mano trovata dentro un'altra decisione.

**Fallback ante-2019 (limite del server).** `get_judgement` recupera solo decisioni
**dal 2019 in poi**: per quelle anteriori restituisce errore (HTTP 400). Se la
pronuncia nomofilattica rilevante è **anteriore al 2019** (es. SU Cass. 577/2008),
**non insistere** e **non inventare un link**: esporre comunque il contrasto e il
principio di diritto **come riportati nella sentenza che la cita**, in forma
testuale e senza `public_url`. Questa è l'unica eccezione consentita alla lettura
integrale obbligatoria di cui sopra.

---

## INTEGRAZIONE CON LA SKILL NORMATTIVA

Quando un risultato BuddaLaw contiene riferimenti normativi — nei campi `reference_data` dei requisiti contrattuali, nelle motivazioni delle sentenze citate, negli articoli restituiti da `search_articles` — applicare la skill **normattiva** per convertire ogni citazione in link Normattiva inline.

**Le due skill si attivano in sequenza:**
1. BuddaLaw recupera fonti giurisprudenziali, normative e documentali
2. Normattiva linka ogni riferimento normativo presente nei risultati

**Esempi di riferimenti da linkare:**
- `art. 28, Legge 392/1978` → link Normattiva
- `art. 2103 c.c.` → link Normattiva
- `art. 18, L. 300/1970` → link Normattiva (con attenzione alla versione vigente)

Se la skill normattiva non è attiva nella sessione, citare i riferimenti normativi in forma testuale senza inventare URL.

---

## FORMATO RISPOSTA GIURIDICA

**Struttura raccomandata:**

1. **Risposta diretta** (1-2 frasi) alla domanda
2. **Analisi per sezioni** con intestazioni markdown
3. **Citazioni inline** nel corpo del testo — MAI in un box separato finale
4. **Tabella riepilogativa** se utile (es. confronto lavoratore/dirigente)
5. **Raccomandazioni operative** se rilevanti

**Ricchezza della citazione (per ogni ambito).** L'utente è un avvocato: una
decisione citata non deve ridursi al dispositivo. Per ciascuna pronuncia rilevante
riporta — quando disponibili da `sintesi`/`caso_concreto`/testo integrale — il
**caso concreto** (i fatti su cui il giudice ha deciso) e la **ratio/motivazione**
che fonda il principio, così che il lettore capisca subito se la pronuncia è di
interesse per il suo caso. Un principio di diritto enunciato in un caso non
pertinente va segnalato come tale. Evita elenchi nudi di estremi di sentenze.

**Esempio CORRETTO:**
> «La sede aziendale non può essere annoverata tra le sedi protette
> ([Cass. Civ. Sez. Lav., ord. n. 12056/2026](https://www.buddalaw.com/...)).»

**Esempi SBAGLIATI (da non fare mai):**
> «Cass. Civ. Sez. Lav., n. 12056/2026» ← senza link
>
> «...disponibile su BuddaLaw» ← link su testo descrittivo
>
> «Cass. n. 12056/2026 (cfr.)» ← sentenza non cercata con tool live
