# Prassi Fiscale Italiana (Interpelli e documenti collegati)

---

## 1. Cos'è un interpello (conoscenza di dominio)

Un **interpello** è una richiesta formale con cui un contribuente (o il suo rappresentante) chiede a un'autorità fiscale di esprimere il proprio parere interpretativo su una norma tributaria applicata a una situazione concreta e personale. La risposta dell'ente è vincolante solo per il soggetto che ha presentato l'istanza.

### Tipologie di interpello (AdE)
- **Ordinario**: interpretazione di norme obiettivamente incerte rispetto a un caso specifico
- **Probatorio**: verifica della sussistenza di condizioni o idoneità di elementi probatori per accedere a un regime fiscale
- **Anti-abuso**: valutazione preventiva se un'operazione configura abuso del diritto
- **Disapplicativo**: richiesta di disapplicare norme antielusive in presenza di condizioni specifiche
- **Nuovi investimenti**: per piani di investimento rilevanti in Italia da parte di soggetti non residenti

### Prassi: il quadro più ampio
L'interpello è solo una delle forme con cui gli enti fiscali producono **prassi**, ovvero documenti interpretativi ufficiali. Le altre tipologie principali sono:
- **Circolare**: istruzione interpretativa o applicativa di carattere generale, rivolta agli uffici e ai contribuenti
- **Risoluzione**: risposta a quesiti specifici, storicamente il precedente dell'interpello moderno
- **Nota / Direttiva**: comunicazioni interne o indirizzate ad altri enti
- **Consulenza giuridica**: risposta a quesiti di associazioni di categoria o ordini professionali (non del singolo contribuente)

### Enti che producono prassi fiscale rilevante
Non solo l'Agenzia delle Entrate. Tra i principali:
- **Agenzia delle Entrate** — tributi erariali (IRPEF, IRES, IVA, imposte di registro, ecc.)
- **Agenzia delle Dogane e dei Monopoli** — accise, dazi, dogane
- **Ministero dell'Economia e delle Finanze (MEF) / Dipartimento delle Finanze** — politica fiscale, norme di attuazione
- **Ministero del Lavoro e delle Politiche Sociali** — aspetti fiscali del lavoro
- **INPS** — previdenza e contributi
- **Guardia di Finanza** — applicazione delle norme tributarie
- **IVASS** — assicurazioni
- **Banca d'Italia / CONSOB** — aspetti fiscali di strumenti finanziari

---

## 2. Le fonti disponibili

Questa skill usa due fonti complementari. Ogni fonte ha un ambito diverso: **non sono intercambiabili**.

### Fonte A — Agenzia delle Entrate (`agenziaentrate.gov.it`)

**Cosa contiene:**
- Esclusivamente le **risposte agli interpelli dell'Agenzia delle Entrate**
- Copertura: **dal 1° settembre 2018** in poi (pubblicazione resa obbligatoria per legge)
- Include anche: interpelli sui nuovi investimenti, princìpi di diritto, risposte a consulenza giuridica

**Cosa NON contiene:**
- Circolari, risoluzioni, note
- Prassi di enti diversi da AdE
- Interpelli AdE precedenti al 2018

**Struttura di navigazione:**
- Archivio per anno: `https://www.agenziaentrate.gov.it/portale/interpelli-[ANNO]` (es. `/portale/interpelli-2025`)
- Ogni anno → lista di mesi con i rispettivi href — **gli URL mensili NON sono costruibili a priori**: vanno letti direttamente dalla pagina annuale tramite `javascript_tool` (`document.querySelectorAll('main a')`), perché il pattern è irregolare (es. Febbraio 2026 è `/portale/febbraio-20261`, non `/portale/febbraio-2026-interpelli`)
- Ogni mese → lista di voci nel formato "Risposta n. [N] del [GG/MM/AAAA] — [oggetto]" con link diretto al PDF
- I link PDF si trovano **fuori dal tag `<main>`**: usare `document.querySelectorAll('a[href*="pdf"]')` sull'intero documento
- PDF con UUID imprevedibile: non costruibile dall'esterno, va letto dalla pagina mensile

**Quando usarla:**
- L'utente cerca un interpello AdE per **numero e/o anno** specifici (es. "interpello n. 82 del 2026")
- L'utente vuole **scorrere gli interpelli recenti** di AdE per periodo

---

### Fonte B — def.finanze.it (`def.finanze.it/DocTribFrontend`)

**Cosa contiene:**
- **Tutta la prassi fiscale italiana** — interpelli, circolari, risoluzioni, note, direttive, delibere, comunicati stampa — di **decine di enti pubblici** (ministeri, agenzie, autorità di vigilanza, INPS, Banca d'Italia, CONSOB, ecc.)
- Gli interpelli AdE sono inclusi **dal 2022** (quando è stata avviata l'integrazione con il portale AE)
- Copertura storica molto più ampia rispetto al sito AdE

**Cosa NON contiene:**
- Interpelli AdE dal 2018 al 2021 in modo completo (la copertura può essere parziale per quel periodo)

**Quattro ambiti di ricerca (tab nel sito):**

| Tab | `ambitoRicerca` | Pagina form avanzato | Endpoint risultati |
|---|---|---|---|
| Normativa | `N` | `callRicAvanzataNormativa.do?js_enabled=1&reset=y` | `executeAdvancedNormativaSearch.do` |
| Prassi | `P` | `callRicAvanzataPrassi.do?js_enabled=1&reset=y` | `executeAdvancedPrassiSearch.do` |
| Giurisprudenza | `G` | `callRicAvanzataGiurisprudenza.do?js_enabled=1&reset=y` | `executeAdvancedGiurisprudenzaSearch.do` |
| Collezioni | — | `documentiRilevanti.do?js_enabled=1&agenzia=COL` | `executeSearchRil.do` |

**Due modalità di ricerca:**
- **Ricerca semplice (solo parole chiave):** GET a `https://def.finanze.it/DocTribFrontend/executeSearch.do?ambitoRicerca=X&parole=...` — nessuna navigazione form necessaria
- **Ricerca avanzata (con filtri):** le `executeAdvanced*.do` accettano solo POST — navigare il form, compilare con `javascript_tool`, fare `f.submit()`

**Parametri per ambito** (i nomi corrispondono ai campi `name` dei form):

*Comuni a Normativa, Prassi, Giurisprudenza:*
- `parole` — termini di ricerca in full-text
- `tipoCriterioRicerca` — `0`=tutte le parole, `1`=almeno una, `2`=frase esatta, `3`=parole adiacenti, `4`=operatori logici
- `tipo_ord` — `DATA` (cronologico) o `RANK` (rilevanza)
- `ricercaNelTitolo` — `on` per limitare la ricerca al solo titolo
- `tipoEstremi` — tipo documento (valori diversi per ambito; per Prassi: `Interpello`, `Circolare`, `Risoluzione`, `Nota`, `Direttiva`, `Delibera`, `Lettera circolare`, `Comunicato Stampa`, `Telegramma`)
- `numero` — numero del documento
- `annoDataEmissioneDa` / `meseDataEmissioneDa` / `giornoDataEmissioneDa` — inizio intervallo data emissione
- `annoDataEmissioneA` / `meseDataEmissioneA` / `giornoDataEmissioneA` — fine intervallo data emissione
- `ente` — ente emanante esatto (per Prassi es. `Agenzia delle Entrate`, `INPS`, `Banca d'Italia`, `Agenzia delle Dogane e dei Monopoli`; lascia vuoto per tutti)
- `superEnte` — ministero/dipartimento (`Finanze`, `Lavoro`, `Tesoro`, ecc.; lascia vuoto per tutti)
- `materiaFiscale` — categoria tematica fiscale
- `classificazioneArgomento` — sottocategoria tematica

*Solo Normativa (`ambitoRicerca=N`):*
- `articolo`, `numArticolo`, `comma` — ricerca per articolo specifico
- `numeroGU` — numero Gazzetta Ufficiale
- `annoDataGUDa` / `meseDataGUDa` / `giornoDataGUDa` e `...A` — intervallo data GU

*Solo Giurisprudenza (`ambitoRicerca=G`):*
- `ricercaPresenzaMassima` — `on` per cercare solo pronunce con massima

*Solo Collezioni (form `documentiRilevanti.do`):*
- `classAgenzia` — codice collezione (es. `COLLEZIONI-0005`=Leggi di bilancio, `COLLEZIONI-0011`=Fatturazione elettronica, `COLLEZIONI-0100`–`COLLEZIONI-0104`=Massime Cassazione 2020–2024); lascia vuoto per tutte
- `parole`, `tipoCriterioRicerca`, `tipo_ord`, `numero`, campi data emissione — stessi di sopra (no `ente`, `tipoEstremi`, `materiaFiscale`)

**Quando usarla:**
- L'utente cerca per **argomento** senza specificare ente o numero → Prassi (`ambitoRicerca=P`)
- L'utente cerca prassi di **enti diversi da AdE** → Prassi con filtro `ente`
- L'utente cerca **circolari, risoluzioni** o altri tipi di prassi → Prassi con filtro `tipoEstremi`
- L'utente cerca **testo normativo** (leggi, decreti) → Normativa (`ambitoRicerca=N`)
- L'utente cerca **giurisprudenza** (sentenze, massime) → Giurisprudenza (`ambitoRicerca=G`)
- L'utente cerca in una **collezione tematica** → Collezioni con `classAgenzia`
- Punto di ingresso predefinito per qualsiasi ricerca per contenuto: Prassi

---

## 3. Routing: quale fonte usare

Prima di navigare, classifica la richiesta:

| Tipo di richiesta | Fonte | Ambito / form |
|---|---|---|
| Numero e anno specifico AdE ("interpello 82/2026") | **Fonte A** (AE) | Navigazione diretta per anno/mese |
| Prassi per argomento ("cosa dice l'AdE su X") | **Fonte B** | Prassi (`ambitoRicerca=P`) |
| Prassi ente non-AdE ("circolare INPS su X") | **Fonte B** | Prassi + filtro `ente` |
| Tipo specifico ("circolari su X", "risoluzioni su Y") | **Fonte B** | Prassi + filtro `tipoEstremi` |
| Testo normativo ("testo del D.Lgs. 231/2001") | **Normattiva MCP** o **Fonte B** | Normativa (`ambitoRicerca=N`) |
| Giurisprudenza ("sentenze Cassazione su X") | **Fonte B** | Giurisprudenza (`ambitoRicerca=G`) |
| Collezione tematica ("massime Cassazione 2023") | **Fonte B** | Collezioni (`classAgenzia=COLLEZIONI-0103`) |
| Browsing recente AdE | **Fonte A** (AE) | Homepage o anno corrente |
| Argomento + periodo specifico | **Fonte B** | Prassi + filtro anno |

---

## 4. Flusso operativo

Segui sempre questo flusso in cinque passi:

### Passo 1 — Classifica la richiesta
Determina: è una ricerca per numero/data? Per argomento? Quale ente? Quale tipo di documento?

### Passo 2 — Naviga la fonte appropriata

**Fonte A (AE) — ricerca per numero/anno:**
1. Naviga `https://www.agenziaentrate.gov.it/portale/interpelli-[ANNO]`
   - Se la pagina restituisce 404, tenta il percorso alternativo per anni storici:
     `https://www.agenziaentrate.gov.it/portale/normativa-e-prassi/risposte-agli-interpelli/interpelli/archivio-interpelli/interpelli-[ANNO]`
     (es. per il 2018: `.../archivio-interpelli/interpelli-2018`; per il 2019: `.../archivio-interpelli/interpelli-2019`)
   - Se anche questo restituisce 404, naviga la pagina radice dell'archivio generale degli interpelli: `https://www.agenziaentrate.gov.it/portale/normativa-e-prassi/risposte-agli-interpelli/interpelli/archivio-interpelli`
   - Se anche questo restituisce 404, comunica il problema all'utente senza inventare risultati
   - **Nota 2018:** per quell'anno i link mensili nella pagina archivio hanno già il percorso completo (es. `.../interpelli-2018/dicembre-2018-interpelli`); il selettore `main a` li legge correttamente, non è necessario alcun adattamento.
2. Usa `javascript_tool` con `document.querySelectorAll('main a')` per leggere gli href reali dei mesi — non costruire gli URL a mano (il pattern è inconsistente tra anni storici e recenti; es. agosto 2025 è `/portale/agosto-2025-interpello` al singolare)
3. Individua il mese corretto dall'indicazione "dalla n° X alla n° Y" e naviga quell'href
4. Usa `javascript_tool` con questa query per ottenere numero, titolo e href di ogni interpello della pagina (i link PDF sono fuori da `<main>`, quindi si opera sull'intero documento):
   ```js
   JSON.stringify(Array.from(document.querySelectorAll('a[href*="pdf"]')).map(a => {
     // Pattern principale (2019–oggi): "Risposta+n.+82_2026.pdf" — il "+" dopo "n." è opzionale,
     // il suffisso "_ANNO" può mancare. Pattern di riserva (2018–2019): "Interpello+N+ANNO_..."
     // (usato per filenames anomali come "Risposta.+14.pdf" o "Risposta+n.+3_vers2.pdf")
     const m = a.href.match(/Risposta\+n\.\+?(\d+)(?:_(\d+))?\.pdf/i)
            || a.href.match(/Interpello\+(\d+)\+(\d{4})/i);
     // Il wrapper div.indcart_gn contiene sia "Risposta n. X del GG/MM/AAAA"
     // sia il titolo; closest('li,p,div') si fermerebbe al <p> interno (solo titolo)
     const container = a.closest('.indcart_gn') || a.closest('div');
     return {
       num:   m ? parseInt(m[1]) : null,
       anno:  m ? m[2] : null,
       testo: container?.textContent?.trim().replace(/\s+/g, ' ') || a.textContent.trim(),
       href:  a.href
     };
   }).sort((a, b) => (a.num || 0) - (b.num || 0)))
   ```
5. Annota internamente l'href del PDF corrispondente al numero cercato — **non navigare al PDF**. La pagina mensile deve restare aperta nel browser fino a che l'utente non conferma di voler leggere il documento.

**Fonte B (def.finanze) — ricerca per argomento:**

**Caso A — ricerca solo per parole chiave (nessun filtro):** usa `navigate` direttamente:
```
https://def.finanze.it/DocTribFrontend/executeSearch.do?ambitoRicerca=P&parole=TERMINI
https://def.finanze.it/DocTribFrontend/executeSearch.do?ambitoRicerca=N&parole=TERMINI
https://def.finanze.it/DocTribFrontend/executeSearch.do?ambitoRicerca=G&parole=TERMINI
https://def.finanze.it/DocTribFrontend/executeSearchRil.do?classAgenzia=COLLEZIONI-0103&parole=TERMINI
```
I risultati (e `$risultati`) sono disponibili immediatamente dopo la navigazione — nessun JS necessario.

**Caso B — ricerca avanzata (con filtri per tipo, ente, date, numero, ecc.):** le `executeAdvanced*.do` accettano solo POST; navigare prima il form, poi compilare con `javascript_tool` e fare `f.submit()`.

| Ambito | Form URL | Form `id` |
|---|---|---|
| Prassi | `callRicAvanzataPrassi.do?js_enabled=1&reset=y` | `formRicAvanzP` |
| Normativa | `callRicAvanzataNormativa.do?js_enabled=1&reset=y` | `formRicAvanzN` |
| Giurisprudenza | `callRicAvanzataGiurisprudenza.do?js_enabled=1&reset=y` | `formRicAvanzG` |
| Collezioni | `documentiRilevanti.do?js_enabled=1&agenzia=COL` | (form unico) |

Snippet generico per compilare e inviare (sostituire `#formRicAvanzP` con l'id corretto e impostare solo i campi necessari):
```js
const f = document.querySelector('#formRicAvanzP');
f.querySelector('[name="parole"]').value          = 'TERMINI DI RICERCA';
f.querySelector('[name="tipoEstremi"]').value      = 'Interpello';      // '' per tutti
f.querySelector('[name="ente"]').value             = 'Agenzia delle Entrate'; // '' per tutti
f.querySelector('[name="annoDataEmissioneDa"]').value = '2024';         // ometti se non serve
f.querySelector('[name="annoDataEmissioneA"]').value  = '2025';         // ometti se non serve
// Solo Normativa: f.querySelector('[name="tipoEstremi"]').value = 'Decreto Legislativo';
// Solo Normativa: f.querySelector('[name="numArticolo"]').value = '18';
// Solo Giurisprudenza: f.querySelector('[name="ricercaPresenzaMassima"]').checked = true;
// Solo Collezioni: f.querySelector('[name="classAgenzia"]').value = 'COLLEZIONI-0103';
f.submit();
```

2. Dopo la navigazione (Caso A) o il submit (Caso B), leggi i risultati con `get_page_text`. Il totale è indicato come "Documenti trovati: N".
3. **Accesso diretto ai risultati — `$risultati`:**
   Il motore carica i risultati in batch da 50 documenti. Tutti i documenti del batch corrente sono accessibili nella variabile globale jQuery `$risultati` (collection cumulativa: cresce di 50 ad ogni batch). Per estrarre metadati e URL PDF **senza navigare ogni singolo documento**:
   ```js
   JSON.stringify($risultati.toArray().slice(-50).map(prov => {
     const el = $(prov);
     const tmp = document.createElement('div');
     tmp.innerHTML = el.find('titoliProvvedimento').text();
     return {
       idElemento: el.find('elemento').first().attr('idElemento'),
       estremi: el.find('estremi').text().trim(),
       titolo: tmp.textContent.trim().replace(/\s+/g, ' ').substring(0, 150)
     };
   }))
   ```
   `idElemento` è il GUID del PDF: URL diretto = `https://def.finanze.it/DocTribFrontend/getContent.do?id={idElemento}`.

   **Batch successivo:** naviga a `https://def.finanze.it/DocTribFrontend/paginatorXml.do` — carica i prossimi 50 documenti e li aggiunge a `$risultati`. Riesegui il `javascript_tool` qui sopra per estrarre i nuovi 50.

   **Attenzione:** la sessione è server-side. Se dopo la navigazione a `paginatorXml.do` la pagina non mostra risultati pertinenti, la sessione è scaduta: ripetere la ricerca (Caso A o B).

   Segnalare all'utente quanti documenti totali esistono (variabile `totDocs` o "Documenti trovati: N") e chiedere prima di procedere al batch successivo, salvo richiesta esplicita di elencarli tutti.

### Passo 3 — Presenta la lista all'utente
Mostra i risultati trovati con: tipo documento, numero, data, ente, oggetto/titolo.
**Non aprire ancora i PDF.** Chiedi all'utente quale documento vuole approfondire.

### Passo 4 — Consegna il documento all'utente
Quando l'utente indica quale documento vuole:

1. Ottieni l'URL del PDF:
   - **Fonte A**: usa l'href già annotato nel Passo 2 step 5. Se il browser non è più sulla pagina mensile, torna alla pagina mensile e riesegui la query `javascript_tool` del Passo 2 step 4 — **non eseguire il selettore su una pagina PDF già aperta**.
   - **Fonte B**: usa l'`idElemento` già estratto al Passo 2 step 4. Solo se non disponibile (risultati letti esclusivamente via `get_page_text`), naviga `getPrassiDetail.do?id={idProvvedimento}` e leggi `document.querySelector('a[href*="getContent.do"]').href`
2. Costruisci l'URL cliccabile: partendo dall'`idElemento` (es. `{17FC0849-...}`) o dall'href del PDF, percent-encoda i caratteri `{` → `%7B` e `}` → `%7D` (necessario perché le graffe rompono il parser markdown). Es: `https://def.finanze.it/DocTribFrontend/getContent.do?id=%7B17FC0849...%7D`. Chiama questo valore `[URL_ENCODED]`.

3. Mostra all'utente il messaggio seguente (sostituendo `[TITOLO]` e `[URL_ENCODED]` con i valori reali):

   > Ho trovato il documento: **[TITOLO]**
   >
   > Non posso aprire i PDF direttamente. Scaricalo qui: [Apri documento]([URL_ENCODED])
   >
   > Poi scegli come condividermelo:
   > - **Solo per questa conversazione** → trascinalo nella chat (o usa l'icona allegato)
   > - **Per tutte le sessioni future** → aggiungilo ai file del progetto (*Progetto → Aggiungi file*)
   >
   > Appena è disponibile, lo analizzo subito.

4. Attendi che l'utente alleghi il file alla chat.

### Passo 5 — Analizza e cita
Quando il PDF è disponibile — allegato nella chat **oppure** già presente nei file del progetto — leggilo e riassumi il contenuto in risposta alla domanda originale. Indica sempre: tipo documento, numero, data, ente emanante, e link diretto al documento.

Se il documento è già nei file del progetto (l'utente lo segnala o lo si riconosce dal contesto), non chiedere di allegarlo nuovamente: è già leggibile.

---

## 5. Note operative

- Usa i tool `mcp__Claude_in_Chrome__*` per navigare: `navigate`, `get_page_text`, `javascript_tool`
- Le pagine di entrambi i siti sono server-rendered: `get_page_text` è sufficiente per leggere lista di risultati e metadati
- **I PDF non si scaricano automaticamente**: mostrare sempre l'URL all'utente e attendere che alleghi il file come descritto al Passo 4
- Non costruire mai URL mensili AE a mano: leggerli sempre dalla pagina annuale con `javascript_tool`
- **Anni storici AE (2018–2021):** la struttura delle pagine potrebbe differire da quella degli anni recenti. Se la pagina annuale non ha la suddivisione per mese o i link PDF hanno un pattern diverso, adattarsi al contenuto trovato anziché aspettarsi un formato fisso
- **Gestione errori:** se una pagina non risponde o un PDF non è raggiungibile, comunicarlo all'utente senza inventare contenuti. Non affermare di aver letto un documento che non è stato effettivamente recuperato
- def.finanze.it restituisce risultati misti (interpelli + circolari + risoluzioni): usa il filtro `tipoEstremi=Interpello` se l'utente vuole solo interpelli
- Non aprire mai PDF in autonomia senza che l'utente abbia scelto il documento: la lista dei titoli è sufficiente per il primo livello di risposta
