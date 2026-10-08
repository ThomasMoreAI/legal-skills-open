---
name: penalista-cautelare-synthos-logic
title: Skill — Misure Cautelari Personali
description: 'Workflow completo per le misure cautelari personali nel processo penale italiano. ATTIVARE SEMPRE per: riesame cautelare, appello de libertate, revoca o sostituzione misura cautelare, calcolo termini di fase della custodia cautelare, istanza di scarcerazione per scadenza termini, analisi dei presupposti cautelari (gravi indizi, esigenze cautelari, proporzionalita), verifica adeguatezza della misura vigente, udienza di convalida dell''arresto. Attivare anche quando l''avvocato dice: ''il cliente e in custodia'', ''dobbiamo chiedere il riesame'', ''quando scade la custodia'', ''possiamo chiedere i domiciliari'', ''come contestiamo la misura'', ''il tribunale del riesame non ha deciso'', ''istanza di scarcerazione''.'
author: Synthos-Logic
author_url: https://github.com/Synthos-Logic/penalista-italia/tree/main/skills/penalista-cautelare
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: criminal
language: it
---

# Skill — Misure Cautelari Personali

Questa skill gestisce l'intero ciclo difensivo delle misure cautelari personali: dall'analisi dei presupposti al riesame, dalla revoca alla verifica dei termini di fase. I termini cautelari sono tra i più critici del processo penale — un errore può tenere un innocente in carcere oltre i termini legali.

---

## ⚠️ Quadro normativo vigente (verificato giugno 2026)

Due novità della Riforma Nordio (L. 114/2024) incidono direttamente su questa skill:

**1. Interrogatorio preventivo (art. 291 co. 1-bis c.p.p.) — IN VIGORE.**
Salvo i casi eccettuati (esigenze cautelari incompatibili con il preavviso, reati di maggiore gravità, pericolo attuale di fuga o inquinamento), il giudice deve interrogare la persona **prima** di applicare la misura, con registrazione audio/video integrale. Per la difesa è un'occasione nuova: preparare il cliente, valutare il silenzio, depositare documentazione sulle esigenze cautelari **prima** che la misura sia disposta. L'omissione dell'interrogatorio fuori dai casi consentiti è motivo di impugnazione — verificarla sempre nell'analisi dell'ordinanza (Modulo 2).

**2. GIP collegiale per la custodia in carcere (art. 328 co. 1-quinquies c.p.p.) — NON ANCORA IN VIGORE.**
L'entrata in vigore, originariamente fissata al 25 agosto 2026, è stata **differita a fine febbraio 2027** (decreto-legge approvato dal CdM il 4 giugno 2026) [VERIFICARE estremi G.U.]. Fino ad allora decide il GIP monocratico. Dettagli in [[AGGIORNAMENTO_NORMATIVO_2025-2026]].

---

## Prima di procedere

Identifica la situazione cautelare. Chiedi in un'unica domanda le informazioni mancanti:

- **Tipo di misura vigente** (custodia cautelare in carcere / arresti domiciliari / altra)
- **Data di esecuzione della misura**
- **Reato contestato** (per determinare il regime dei termini di fase)
- **Fase processuale** (indagini / UP / primo grado / appello / Cassazione)
- **Cosa serve fare** (riesame / revoca / verifica termini / analisi presupposti / udienza convalida)

---

## MODULO 1 — VERIFICA IMMEDIATA DEI TERMINI

Da eseguire **sempre per primo** quando si gestisce un fascicolo con detenuto.

### Calcolo termine di fase

Determina se i termini di fase della custodia cautelare sono rispettati.

**Reati "normali" vs. reati gravi (art. 407 co. 2 c.p.p.):**
I reati gravi includono: associazione mafiosa, terrorismo, sequestro di persona a scopo di estorsione, traffico internazionale di stupefacenti, omicidio aggravato ex art. 416-bis. Per tutti gli altri: regime "reati normali".

| Fase | Reati normali | Reati art. 407 co. 2 |
|---|---|---|
| Indagini | 3 mesi | 6 mesi (+ proroga a 1 anno) |
| UP | 3 mesi | 3 mesi |
| I grado | 6 mesi | 1 anno |
| Appello | 6 mesi | 1 anno |
| Cassazione | **45 giorni** | **3 mesi** |

**Output:** mostrare la scadenza del termine di fase attuale, con data precisa.

> ⚠️ **Tabella semplificata.** I termini dell'art. 303 c.p.p. variano anche in base alla pena edittale del reato contestato (fasce diverse entro la stessa fase). Prima di comunicare una scadenza al difensore, **verificare sempre il termine sul testo vigente dell'art. 303 c.p.p.** (PDF in `penalista-fonti/` o Normattiva) e applicare la regola conservativa: nel dubbio, il termine più breve.

**Se il termine è già scaduto o scade entro 48 ore:** → EMERGENZA CAUTELARE — passare immediatamente al Modulo 5 (istanza di scarcerazione).

---

## MODULO 2 — ANALISI DEI PRESUPPOSTI CAUTELARI

Analizza sistematicamente i tre presupposti dell'ordinanza cautelare per costruire la strategia di contestazione.

### Gravi indizi di colpevolezza (art. 273 c.p.p.)

I "gravi indizi" non sono prove di colpevolezza, ma elementi che, allo stato degli atti, rendono probabile la colpevolezza. La difesa deve contestare:

**Solidità del quadro indiziario:**
- Le intercettazioni: sono utilizzabili? Il decreto del GIP è motivato adeguatamente? Il reato era tra quelli ammessi?
- Le dichiarazioni accusatorie: provenienza (collaboratori / coimputati)? Hanno riscontri? I riscontri sono indipendenti?
- Le prove documentali: autenticità? Correttezza dell'interpretazione?
- Le prove tecniche (perizie, analisi): metodologia corretta? Il perito è qualificato?

**Domande critiche:**
- Gli indizi sono plurimi e convergenti, o isolati e equivoci?
- Ci sono elementi di segno contrario che il GIP ha ignorato?
- La fonte indiziaria principale è attendibile?

### Esigenze cautelari (art. 274 c.p.p.)

Ogni esigenza cautelare deve essere concreta, attuale e specifica. Non basta l'astratta possibilità.

**Pericolo di fuga (art. 274 lett. b):**
- Reato punito con pena superiore a 2 anni di reclusione (presupposto)
- Ci sono elementi concreti (non astratti) che il soggetto fuggirà? Disponibilità di documenti esteri? Tentativi pregressi?
- Elementi contrari: radicamento familiare, lavorativo, immobiliare; incensuratezza; collaborazione durante le indagini

**Pericolo di inquinamento probatorio (art. 274 lett. a):**
- Concreto e attuale — non basta la possibilità astratta
- Se le indagini sono chiuse o avanzate: il pericolo è residuo o già superato?
- I testimoni sono già stati escussi? Le prove documentali già acquisite?
- Con che mezzi potrebbe avvenire il condizionamento? Il sospettato ha rapporti con i testimoni?

**Pericolo di reiterazione (art. 274 lett. c):**
- Richiede una prognosi criminologica concreta — non basta la gravità del reato
- Precedenti penali specifici per lo stesso tipo di reato?
- Elementi che indicano una condotta seriale?
- Il contesto è cambiato (es. cessata l'attività professionale che aveva facilitato il reato)?

### Adeguatezza e proporzionalità (art. 275 c.p.p.)

Anche se le esigenze cautelari sussistono, la misura deve essere la MENO AFFLITTIVA adeguata allo scopo.

**Scala della proporzionalità:**
Prescrizioni → divieto di avvicinamento → divieto di espatrio → obbligo di presentazione → arresti domiciliari (senza braccialetto) → arresti domiciliari con braccialetto → custodia cautelare in carcere

**Argomenti per la sostituzione con misura meno afflittiva:**
- Situazione familiare (figli minori, caregiver di familiari malati — art. 275 co. 4)
- Stato di salute incompatibile con la detenzione (art. 275 co. 4-bis)
- Prima esperienza carceraria — effetto desocializzante
- Condizioni abitative idonee per i domiciliari
- Braccialetto elettronico come alternativa efficace alla custodia

---

## MODULO 3 — RIESAME EX ART. 309 C.P.P.

### Termini e procedura

**Termine per proporre il riesame:** 10 giorni dall'esecuzione o notifica della misura — PERENTORIO.
**Il Tribunale del Riesame deve decidere entro:** 10 giorni dalla ricezione degli atti.
**Conseguenza del mancato rispetto del termine del Tribunale:** perdita di efficacia automatica della misura (art. 309 co. 10) — monitorare.

### Come costruire i motivi di riesame

Strutturare i motivi nell'ordine seguente, contestando separatamente ogni pilastro dell'ordinanza:

**I. Gravi indizi — contestazione specifica**
Non contestare "in blocco" — contestare ogni elemento indiziario su cui il GIP ha fondato la misura. Per ogni elemento: qual è il limite probatorio? Quali riscontri mancano? Ci sono prove di segno contrario?

**II. Esigenze cautelari — contestazione per ciascuna**
Se il GIP ha motivato su più esigenze, contestarle tutte — anche quelle che sembrano più solide. Se ne cade anche solo una, la misura può essere attenuata.

**III. Adeguatezza — misura alternativa**
Proporre sempre la misura alternativa in concreto: dove si troverebbero gli arresti domiciliari? Con chi? Quale dispositivo di sorveglianza elettronica è disponibile?

**IV. Vizi formali dell'ordinanza (se presenti)**
Mancanza di motivazione autonoma del GIP (che si è limitato a recepire la richiesta del PM senza valutazione propria) → nullità.

### Cosa allegare al riesame

- Documentazione sulla situazione familiare e lavorativa
- Certificati medici (se rilevanti per art. 275 co. 4-bis)
- Planimetria/documentazione dell'abitazione proposta per i domiciliari
- Contratto di lavoro, residenza, famiglia anagrafica
- Dichiarazioni di disponibilità di terzi all'ospitalità (se domiciliari in casa altrui)

---

## MODULO 4 — REVOCA E SOSTITUZIONE (artt. 299–300 c.p.p.)

### Quando si può chiedere

La revoca è possibile in ogni momento durante il procedimento quando:
- Vengono meno i gravi indizi di colpevolezza
- Vengono meno le esigenze cautelari (o si attenuano)
- Sopravvengono nuovi elementi favorevoli

La sostituzione con misura meno afflittiva è possibile quando le esigenze cautelari residue possono essere soddisfatte con una misura meno grave.

### Quando è strategicamente opportuno

- Dopo l'escussione dei testimoni chiave (il pericolo di inquinamento è cessato)
- Dopo il deposito degli atti e la chiusura delle indagini
- Dopo una sentenza di proscioglimento su un punto che indebolisce il quadro indiziario
- Quando il tempo trascorso in custodia ha prodotto un mutamento della situazione
- Quando le condizioni di salute si sono aggravate (art. 275 co. 4-bis)

### Struttura dell'istanza

Vedere `penalista-atti` — sezione "Istanza di revoca o sostituzione".

---

## MODULO 5 — ISTANZA DI SCARCERAZIONE PER SCADENZA TERMINI

### Quando si attiva

Immediatamente quando:
- Il termine di fase della custodia cautelare è scaduto o scadrà entro 24–48 ore
- Il Tribunale del Riesame non ha deciso entro 10 giorni dalla ricezione degli atti (art. 309 co. 10)
- Il GIP non ha convalidato l'arresto entro 96 ore dall'arresto stesso (art. 391 co. 7)

### Struttura dell'istanza di scarcerazione

```
[Intestazione]
[GIP / Autorità competente] di [Città]

Istanza di scarcerazione per decorrenza termini ex art. [303 / 309 co. 10 / 391 co. 7] c.p.p.
nei confronti di [Nome Cognome]

Avv. [Nome Cognome], difensore di fiducia di [Nome Cognome],
attualmente detenuto presso [istituto] in esecuzione dell'ordinanza [numero/data],

PREMESSO CHE:
- La misura della custodia cautelare è stata applicata in data [data]
- La fase processuale attuale è [fase]
- Il termine massimo di custodia cautelare per la fase in corso è di [durata]
- Tale termine è decorso in data [data]

TUTTO CIÒ PREMESSO,

chiede la IMMEDIATA SCARCERAZIONE di [Nome Cognome] per intervenuta
scadenza del termine di fase della custodia cautelare ex art. 303 c.p.p.,
con conseguente perdita di efficacia della misura.

[Città], [data e ora]
Avv. [Nome Cognome]
```

**Nota:** questa istanza è urgente — depositarla nel modo più rapido possibile (fax / PEC / deposito diretto in cancelleria). Se il GIP non provvede entro poche ore, presentare istanza al Presidente del Tribunale o ricorrere in Cassazione.

---

## MODULO 6 — UDIENZA DI CONVALIDA

### Preparazione

**Termini:** la comunicazione dell'arresto deve avvenire entro 24 ore; il GIP fissa l'udienza entro 48 ore dalla comunicazione. Il totale non deve superare 96 ore dall'arresto.

**Prima dell'udienza, verificare:**
- Il decreto di convalida è motivato su tutti i presupposti?
- L'arresto è avvenuto in flagranza (art. 382 c.p.p.) o per fermo (art. 384 c.p.p.)?
- I presupposti della flagranza o del pericolo di fuga (per il fermo) sussistevano?
- L'avviso ex art. 386 co. 1 c.p.p. è stato dato all'imputato (diritto al silenzio, difensore)?

**In udienza:**
- Il difensore può articolare l'esame dell'arrestato
- Depositare documentazione a discarico già disponibile
- Formulare la richiesta di misura alternativa (arresti domiciliari o misura meno afflittiva)
- Contestare i presupposti della flagranza/fermo se presenti vizi

### Dopo la convalida

Se il GIP convalida e applica misura cautelare → 10 giorni per il riesame (dies a quo: giorno della convalida / esecuzione della misura).

Se il GIP non convalida → l'arrestato è immediatamente libero.

---

## INTEGRAZIONE CON IL SISTEMA DI MEMORIA

Ogni volta che si lavora su un fascicolo cautelare:
- Aggiornare la sezione "Scadenze cautelari" di [[SCADENZIARIO]] con i termini di fase calcolati
- Inserire nel file fascicolo [[wikilink]] la misura vigente, la data di applicazione e le scadenze
- Se ci sono più imputati detenuti, creare una voce per ciascuno nello scadenziario
