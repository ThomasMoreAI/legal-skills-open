---
name: accertamento-tecnico-preventivo-cpc-morellid
title: Accertamento tecnico preventivo e consulenza tecnica preventiva (c.p.c. 696, 696-bis)
description: Supporto documentale all'inquadramento dell'istruzione preventiva nel processo civile secondo il Codice di procedura civile, artt. 696 e 696-bis. Aiuta a scegliere tra accertamento tecnico preventivo / ispezione giudiziale e consulenza tecnica preventiva ai fini della composizione della lite. Use when an engineer acting or about to act as a court-appointed expert (CTU), or a lawyer/party, must frame an Italian pre-trial technical assessment (ATP) or the conciliatory preventive technical consultancy under artt. 696/696-bis c.p.c.; it is a documentary aid and does NOT file the proceeding, does NOT draft the petition or the merits report, and does NOT replace the judge, the lawyer, or the CTU.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/accertamento-tecnico-preventivo-cpc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
tags: [accertamento-tecnico-preventivo, atp, consulenza-tecnica-preventiva, codice-procedura-civile, ctu]
sources:
- title: Atp Checklist
  path: references/estratti/atp-checklist.md
- title: Cpc 696 696Bis
  path: references/fonti/cpc-696-696bis.md
---

# Accertamento tecnico preventivo e consulenza tecnica preventiva (c.p.c. 696, 696-bis)

## Quando usare questa skill

Usala quando un **ingegnere che opera (o e' in procinto di operare) come CTU**, oppure un
**avvocato/parte**, deve inquadrare l'**istruzione preventiva** nel processo civile secondo gli
**artt. 696 e 696-bis del Codice di procedura civile**:

- scegliere tra **accertamento tecnico preventivo / ispezione giudiziale** (art. 696) e
  **consulenza tecnica preventiva ai fini della composizione della lite** (art. 696-bis);
- inquadrare **presupposti**, **procedimento**, **sospensione**, **tentativo di conciliazione**
  ed **efficacia del verbale**.

Per la **relazione del CTU nel merito** (artt. 191-201) usa `relazione-peritale-ctu-cpc`; per
la **liquidazione dei compensi** del CTU usa `compensi-ctu-dpr115`. Questa skill copre la fase
**preventiva** (ATP e ATP conciliativo).

## Due strumenti dell'istruzione preventiva

- **Accertamento tecnico preventivo / ispezione giudiziale** (art. 696): presuppone
  l'**urgenza** di **far verificare, prima del giudizio**, lo **stato di luoghi** o la
  **qualita'/condizione di cose** (o, ricorrendone l'urgenza, sulla **persona**). E' uno
  strumento di **conservazione della prova**.
- **Consulenza tecnica preventiva** (art. 696-bis): richiedibile **anche fuori dai casi di
  urgenza** dell'art. 696, c. 1, per l'**accertamento e la determinazione dei crediti** da
  **inadempimento contrattuale** o **fatto illecito**. Ha **funzione deflattiva/conciliativa**.

## Accertamento tecnico preventivo (art. 696)

- **Oggetto esteso** (c. 2): puo' comprendere anche **valutazioni su cause e danni** relativi
  all'oggetto della verifica.
- **Procedimento** (c. 3): il giudice provvede nelle forme degli artt. 694-695 (in quanto
  applicabili), **nomina il CTU** e **fissa l'inizio** delle operazioni.
- **Sospensione** (c. 4): il **conferimento dell'incarico** (o, se successivo, il **giuramento**)
  sospende il procedimento fino al **deposito della CTU** e **comunque non oltre sei mesi**; la
  sospensione **non impedisce** l'espletamento della consulenza.
- **Definizione** (c. 5): con il **deposito della CTU**; segue la **liquidazione** di onorario e
  spese dell'ausiliario.

## Consulenza tecnica preventiva conciliativa (art. 696-bis)

- Il **consulente**, **prima di depositare la relazione**, **tenta - ove possibile - la
  conciliazione** delle parti.
- **Se le parti si conciliano**: si forma **processo verbale**; il giudice gli attribuisce con
  **decreto efficacia di titolo esecutivo** (espropriazione, esecuzione in forma specifica,
  iscrizione di ipoteca giudiziale). Il verbale e' **esente dall'imposta di registro**.
- **Se la conciliazione non riesce**: **ciascuna parte** puo' chiedere che la **relazione** sia
  **acquisita** nel successivo **giudizio di merito**.
- Si applicano gli **artt. da 191 a 197** in quanto compatibili (nomina, giuramento, operazioni
  con parti/CTP, verbale, relazione).

## Cosa NON fa (limiti)

- **Non instaura il procedimento**, **non redige** il ricorso ex art. 696/696-bis ne' la
  relazione tecnica.
- **Non fornisce il contenuto tecnico/di merito** della consulenza (cfr.
  `relazione-peritale-ctu-cpc`).
- **Non sostituisce** il **giudice**, l'**avvocato** ne' il **CTU**; non copre il rito e i
  termini di dettaglio del procedimento cautelare (artt. 692-695).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`scegli-strumento-preventivo`](tasks/scegli-strumento-preventivo.md) | Aiuta a scegliere tra ATP/ispezione giudiziale (art. 696) e consulenza tecnica preventiva conciliativa (art. 696-bis) in base a urgenza e finalita' |
| [`imposta-procedimento-atp`](tasks/imposta-procedimento-atp.md) | Inquadra procedimento, sospensione (6 mesi), tentativo di conciliazione ed efficacia del verbale/relazione |

## Riferimenti normativi

- **Codice di procedura civile (R.D. 28 ottobre 1940, n. 1443)** - **art. 696** (accertamento
  tecnico e ispezione giudiziale preventivi; cause e danni; sospensione fino al deposito CTU,
  non oltre 6 mesi), **art. 696-bis** (consulenza tecnica preventiva conciliativa; verbale con
  efficacia di titolo esecutivo esente da imposta di registro; acquisizione nel merito; richiamo
  artt. 191-197). Testo aggiornato alla riforma Cartabia (D.Lgs. 149/2022).
- Articoli **richiamati** (non riprodotti): **692-695** (procedimento di istruzione preventiva),
  **191-197** (disciplina della CTU).

Dettaglio in `references/sources.yaml`, `references/fonti/cpc-696-696bis.md`,
`references/estratti/atp-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la scelta dello strumento, l'instaurazione del procedimento
e la valutazione tecnica di merito restano responsabilita' del **giudice**, dell'**avvocato** e
del **CTU**, sul testo vigente degli artt. 696/696-bis. La skill **non sostituisce** tali
soggetti ne' la lettura degli articoli e degli atti richiamati.
