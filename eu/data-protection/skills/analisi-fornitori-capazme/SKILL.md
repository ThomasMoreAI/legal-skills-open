---
name: analisi-fornitori-capazme
title: Analisi fornitori — screening privacy del mastrino
description: Usa questa skill quando il cliente invia il mastrino fornitori (o un elenco fatture/fornitori) e serve lo screening privacy — es. «analizza il mastrino fornitori», «chi dobbiamo nominare responsabile ex art. 28», «screening fornitori GDPR», «analisi fornitori per la nomina», «il cliente ci ha mandato l'elenco dei fornitori/fatture». Estrae i fornitori da qualunque formato (Excel, CSV, PDF, scansioni, corpo mail), li deduplica, li identifica via web e VIES, ipotizza il ruolo privacy di ciascuno (Responsabile art. 28 / Titolare autonomo / Fuori perimetro) con confidenza tarata, produce l'Excel standard con genera_report_fornitori e, su conferma, le bozze di nomina ex art. 28 con genera_dpa per i responsabili senza DPA proprio.
author: capazme
author_url: https://github.com/capazme/mcp-legal-it/tree/main/plugin/skills/analisi-fornitori
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
sources:
- title: Classificazione
  path: references/classificazione.md
- title: Metodologia
  path: references/metodologia.md
---

# Analisi fornitori — screening privacy del mastrino

Qualifica ogni fornitore del mastrino rispetto al ruolo privacy nel rapporto con il
**cliente dello studio (il titolare del trattamento)**. È uno screening di primo
livello: la qualifica dipende dalla prestazione CONCRETA resa al cliente, che il
mastrino non rivela — l'esito va validato con cliente e contratti, e la Confidenza
deve rifletterlo.

## Regole d'oro (valgono in ogni fase)

1. **Mai inventare**: attività, P.IVA e servizi si affermano solo con una fonte
   (URL) o con conferma VIES. Fornitore non identificabile → categoria più
   probabile + Confidenza `basso` + alternative in `note`.
2. **Gli importi sono irrilevanti**: ignorarli sempre.
3. **Confidenza al ribasso**: nel dubbio, abbassa. `alto` SOLO con identificazione
   univoca confermata (P.IVA presente o agganciata via VIES). Senza P.IVA nel
   mastrino, `alto` è l'eccezione.
4. **Contratto canonico**: ogni fornitore analizzato è un oggetto JSON con i campi
   di `references/metodologia.md` §Contratto. I tool lo validano — rispettalo.

## Fase 0 — Setup

Chiedi (se non già noti): denominazione del **cliente titolare** e file del
mastrino. Crea `analisi_fornitori_checkpoint.json` accanto al mastrino (fallback:
directory corrente). Se esiste già un checkpoint per quel mastrino, proponi di
riprendere dal primo fornitore non analizzato invece di ripartire.

Struttura del checkpoint:

```json
{
  "versione": 1,
  "cliente": "...",
  "file_mastrino": "...",
  "creato": "ISO-8601",
  "fase": "estrazione | dedup | ricerca | completata",
  "fornitori_estratti": [],
  "fornitori_unici": [],
  "analisi": []
}
```

Aggiorna il checkpoint dopo OGNI mutazione (fine estrazione, fine dedup, fine di
ogni blocco di ricerca).

## Fase 1 — Estrazione

Leggi il mastrino nel formato in cui arriva (guida per formato in
`references/metodologia.md` §Estrazione). Estrai per ogni riga: denominazione
e P.IVA/CF se presente. Se il file è illeggibile (scansione pessima, corrotto):
fermati e chiedi una copia migliore. Salva in `fornitori_estratti`.

## Fase 2 — Dedup e gate

Applica le regole di `references/metodologia.md` §Dedup. Salva in
`fornitori_unici` (con le varianti unificate in `varianti`). Poi **fermati** e
chiedi: *«N fornitori unici (da M righe). Procedo con la ricerca? [tempo stimato:
~X min]»*. Sopra ~40 fornitori proponi anche la modalità parallela (sotto).

## Fase 3 — Ricerca e classificazione

A blocchi di ~15 fornitori. Per ciascuno:

1. **Aggancio**: se ha P.IVA → `verifica_partita_iva_vies(partita_iva=...)`. Se
   `valido` e `denominazione` compatibile → identità confermata (`fonte_piva`
   resta `"mastrino"`; annota la conferma). Se il VIES è indisponibile
   (`disponibile: false`) → prosegui web-only e annotalo in `note`.
2. **Ricerca web**: attività e servizi reali (strategia e query in
   `references/metodologia.md` §Identificazione). Cita sempre la fonte in `fonti`.
3. **Classificazione**: applica `references/classificazione.md` (3 categorie,
   casi controversi con default e flag).
4. **DPA** (solo responsabili): chiama `verifica_dpa_fornitore(dominio=...)` con
   il dominio del sito ufficiale già trovato al passo 2. Mappatura dell'esito:
   - `dpa_dedicato` → `dpa_proprio: "si"`; l'URL dell'evidenza va in `fonti`.
   - `clausola_in_condizioni` → `dpa_proprio: "si"` **e annota obbligatoriamente
     in `note`** che la nomina è una clausola interna alle condizioni del
     servizio, quindi la copertura dipende dal servizio effettivamente
     acquistato (caso Aruba).
   - `non_trovato` / `bloccato` / `dominio_irraggiungibile` → NON sono un «no»:
     fai la ricerca mirata «{fornitore} data processing agreement / DPA / nomina
     responsabile». Se anche la ricerca non trova nulla: PMI locale o fornitore
     senza DPA pubblicato → `dpa_proprio: "no"` (serve la nomina del titolare,
     tool `genera_dpa`); nel dubbio → `da_verificare`.

   **In entrambi i casi `si`**, la pubblicazione non equivale alla copertura:
   la nomina risulta di norma superflua solo se il DPA pubblicato è
   effettivamente accettato o richiamato nel contratto stipulato con quel
   fornitore — la pubblicazione da sola non basta. È una verifica che il tool
   non esegue (accerta che il DPA esiste pubblicato, non che il cliente lo
   abbia accettato).

   **Una pagina che parla di GDPR non è un DPA.** Prima di scrivere `si` il
   riferimento deve portare a un testo contrattuale che designa il fornitore
   responsabile ex art. 28 — non all'informativa privacy del sito, non a una
   pagina divulgativa sulla conformità.
5. **Confidenza**: tabella in `references/metodologia.md` §Confidenza.

Appendi ogni record completato ad `analisi` nel checkpoint a fine blocco.

### Modalità parallela (>~40 fornitori, su conferma dell'utente)

Dispatch di un subagent generico per blocco (~15 fornitori) con questo prompt,
compilando i placeholder.

**Etichette di classe condivise.** I blocchi non si vedono fra loro: se ognuno
inventa le proprie etichette, lo stesso tipo di fornitore torna come
`giornalista` da un blocco e `giornalista freelance` da un altro, e il controllo
di coerenza — che confronta le etichette per stringa esatta — non le riconosce
come la stessa classe. Mantieni quindi un **elenco progressivo delle
`classe_attivita` già emesse** (parte vuoto, si arricchisce a ogni blocco
chiuso) e passalo a ogni blocco nel placeholder `{CLASSI GIA USATE}`. I blocchi
vanno lanciati a ondate, non tutti insieme, proprio per poter propagare
l'elenco.

> Sei un DPO esperto di GDPR e prassi del Garante. Analizza questi fornitori del
> cliente «{CLIENTE}» (titolare del trattamento) e restituisci SOLO un array JSON
> di record canonici, nessun altro testo. Per ogni fornitore: (1) se ha P.IVA
> usa il tool verifica_partita_iva_vies per confermare l'identità; (2) ricerca
> web per attività/servizi, cita gli URL in `fonti`, non inventare nulla; (3)
> classifica secondo le regole che seguono; (4) per i responsabili chiama
> verifica_dpa_fornitore col dominio del sito ufficiale e applica la mappatura
> del passo 4 della skill, ricadendo sulla ricerca mirata se l'esito è
> non_trovato/bloccato/dominio_irraggiungibile; (5) taratura confidenza: `alto`
> solo con P.IVA confermata, nel dubbio abbassa. Fornitore non identificabile o
> omonimia → categoria più probabile, confidenza `basso`, alternative in `note`.
> ETICHETTE DI CLASSE — VINCOLANTE: per `classe_attivita` DEVI riusare, identica
> carattere per carattere, un'etichetta di questo elenco ogni volta che il
> fornitore vi rientra: {CLASSI GIA USATE}. Non inventare varianti, sinonimi o
> specificazioni di un'etichetta esistente (se l'elenco contiene `giornalista`,
> usa `giornalista` — non `giornalista freelance`, non `giornalista pubblicista`).
> Conia un'etichetta nuova SOLO per un tipo di fornitore che nessuna etichetta
> dell'elenco copre, e tienila breve e generica.
> REGOLE DI CLASSIFICAZIONE: {contenuto integrale di references/classificazione.md}
> CONTRATTO RECORD: {sezione Contratto di references/metodologia.md}
> FORNITORI DA ANALIZZARE: {blocco JSON da fornitori_unici}

Al merge di ogni blocco applica i **guardrail**:
- record con `confidenza: "alto"` senza P.IVA confermata → declassa a `"medio"`;
- record che non rispettano il contratto → scarta e rifai quel blocco in
  modalità sequenziale;
- **riconciliazione delle etichette** (prima della coerenza di classe): elenca
  le `classe_attivita` distinte presenti nel merge e cerca le sinonime — stessa
  radice con qualificatore (`giornalista` / `giornalista freelance`), singolare
  e plurale, sigla ed esteso, italiano e inglese (`hosting` / `hosting cloud`).
  Ogni gruppo di sinonimi va **riscritto sull'etichetta unica** scelta, in tutti
  i record, e l'etichetta unica va aggiunta all'elenco passato ai blocchi
  successivi. Il controllo del tool confronta le etichette per stringa esatta:
  due sinonimi restano due classi separate, ciascuna internamente coerente, e il
  lotto incoerente passa. **Questa riconciliazione va fatta PRIMA di chiamare
  `genera_report_fornitori`** — è l'unico punto in cui il problema è visibile;
- **coerenza di classe**: sulle etichette già riconciliate, raggruppa i record
  per `classe_attivita` e verifica che ogni classe porti UNA sola
  qualificazione. Blocchi diversi non si vedono fra loro, quindi fornitori dello
  stesso tipo possono tornare qualificati in modo diverso senza che nulla lo
  segnali. Se una classe è incoerente, decidi la qualificazione corretta per
  l'intera classe e riallinea i record — non spezzare la classe per far passare
  il controllo. `genera_report_fornitori` rifiuta comunque il lotto.

## Fase 4 — Report

Prima di chiamare il tool, **riconcilia le etichette `classe_attivita`**: scorri
le etichette distinte presenti in `analisi` e unifica le sinonime su una sola
(vedi il guardrail della modalità parallela). Il controllo di coerenza del tool
confronta le etichette per stringa esatta, quindi due sinonimi gli nascondono
l'incoerenza che deve intercettare.

Chiama `genera_report_fornitori(fornitori=<analisi dal checkpoint>,
cliente=..., data_analisi=..., file_sorgente=...)`. Se restituisce errori di
validazione, correggi i record indicati e richiama. Consegna il file all'utente
e imposta `fase: "completata"` (report e nomine sono rigenerabili in qualsiasi
momento dai dati del checkpoint).

## Fase 5 — Nomine ex art. 28 (su conferma)

Elenca i responsabili con `dpa_proprio: "no"` e chiedi UNA conferma per
generarle tutte. Per ciascuno chiama `genera_dpa` con titolare = cliente,
responsabile = fornitore (usa denominazione confermata e P.IVA se nota) e la
descrizione del trattamento derivata da `attivita`/`categorie_dati`. Un DOCX
per fornitore. Ricorda all'utente che per i responsabili `da_verificare` va
prima chiarito il rapporto contrattuale.
