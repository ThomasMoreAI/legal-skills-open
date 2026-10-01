---
name: procure-quotazioni-capazme
title: Procure e Quotazioni — recupero crediti seriale
description: Genera in serie procure alle liti (art. 83 c.p.c.) e lettere di quotazione compensi D.M. 55/2014 in DOCX per posizioni di recupero crediti, partendo da un Excel di posizioni o dai dati forniti, con rilevamento della fase processuale (monitorio, esecuzione forzata, opposizione a decreto ingiuntivo). Usa quando l'utente deve preparare, rifare o aggiornare procure e quotazioni/preventivi per pratiche di recupero crediti — anche dopo una rinuncia al mandato o un cambio di difensore o di firmatario — o quando dice "procure e quotazioni", "quotazioni monitori", "preventivi per i decreti ingiuntivi", "rifai le procure per i clienti di X".
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/procure-quotazioni
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
sources:
- title: Rilevamento Fase
  path: references/rilevamento-fase.md
---

# Procure e Quotazioni — recupero crediti seriale

Produce, per ogni posizione, due DOCX pronti-firma: la procura alle liti e la lettera di quotazione con blocco di accettazione del cliente. Il calcolo e l'impaginazione sono deterministici (tool server); questa skill governa la parte critica: leggere le posizioni, capire la fase, non inventare dati.

## Workflow

### 1. Config studio (dati fissi)

Cerca un file `studio.json` con i dati ricorrenti (mandante, firmatario, difensori, domicilio, PEC): prima nella cartella di lavoro, poi in `~/.claude/legal-it/studio.json`. Formato in `references/studio.esempio.json`. Se manca, chiedi i dati una volta sola e proponi di salvarli in `~/.claude/legal-it/studio.json` per le prossime esecuzioni. I dati reali dello studio restano locali: mai inserirli nel repository del plugin.

Se il firmatario del mandante è cambiato (es. firma il presidente del CdA invece del consigliere), verifica su visura camerale che abbia la rappresentanza legale **anche in giudizio** prima di intestargli le procure, e riporta in `firmatario_qualifica` la carica reale.

### 2. Leggere le posizioni

Da Excel (leggilo con il Python di sistema; se manca openpyxl chiedi un export CSV) o dai dati nel prompt. Per ogni posizione servono: debitore, valore del credito, azione, stato (esecutorietà/note).

Normalizza gli importi prima di usarli: separatori svizzeri (`3'513.60`), apostrofi tipografici (`3’513.60`), stringhe con spazi. Una cella che si legge come data/durata (datetime, timedelta) è un importo **corrotto**: non usarla — recupera l'importo dal ricorso o dalle fatture in fascicolo, o chiedi all'utente. Segnala sempre nel report i valori recuperati da fonte diversa dall'Excel.

### 3. Determinare la fase di ogni posizione

La quotazione dipende dalla **fase processuale**, non solo dal valore: quotare il monitorio a una posizione già esecutiva o opposta produce un preventivo sbagliato. Leggi `references/rilevamento-fase.md` e classifica ogni posizione: `monitorio`, `esecuzione` o `opposizione`. In caso di dubbio chiedi, non tirare a indovinare.

### 4. Dati identificativi del debitore

Nella procura la clausola del debitore (denominazione, legale rappresentante, sede, C.F./P.IVA) va **copiata verbatim** dagli atti già in fascicolo (vecchie procure, ricorsi: estraili con `pdftotext`), non ricostruita a memoria. Nel cercare la clausola giusta, ancora il confronto all'**inizio** della denominazione: "Uno S.r.l." è contenuto in "Beta Progetto Uno S.r.l." e un match per sottostringa aggancia il debitore sbagliato. Se non esiste un atto precedente, usa i dati forniti in input e segnala nel report che C.F./P.IVA vanno verificati su visura camerale.

### 5. Generare i documenti

Per ogni posizione chiama:

1. `legal-it:genera_procura_liti_docx` — passa la clausola debitore verbatim in `controparte`
2. `legal-it:genera_quotazione_docx` — `tipo` dalla fase rilevata; `livello` "minimi" salvo diversa indicazione dell'utente (es. una posizione specifica "ai medi")

I tool salvano in una directory temporanea e restituiscono il percorso: sposta i file nella cartella di destinazione (es. `NUOVE PROCURE/<Cliente>/`, o quella indicata dall'utente) con nomi parlanti, una sottocartella per cliente, così i nuovi documenti non si confondono con quelli storici.

### 6. Report finale

Chiudi con una tabella riepilogativa (cliente, debitore, valore, fase, livello, totale quotazione) e una sezione "verifiche consigliate": dati debitore da confermare su visura, importi recuperati da fonti alternative, posizioni escluse perché fuori perimetro (es. azione diversa: giudizio ordinario, sola diffida).

## Output atteso

| Documento | Contenuto |
|-----------|-----------|
| Procura alle liti | Art. 83, co. 3, c.p.c.; dichiarazioni mediazione/negoziazione/privacy; una pagina; firma mandante + autentica difensori |
| Quotazione | Lettera al cliente con prospetto D.M. 55/2014, oneri accessori (CU, marca), imposta di registro, firme difensori, accettazione cliente |

## Risorse

- `references/rilevamento-fase.md` — regole di classificazione della fase e tabelle compensi/CU usate dai tool
- `references/studio.esempio.json` — formato del file di configurazione studio (dati di esempio)
