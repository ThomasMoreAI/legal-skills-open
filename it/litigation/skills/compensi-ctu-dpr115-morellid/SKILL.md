---
name: compensi-ctu-dpr115-morellid
title: Compensi del CTU / ausiliario del magistrato (D.P.R. 115/2002)
description: Supporto documentale alla liquidazione dei compensi del CTU / ausiliario del magistrato ai sensi del Testo Unico spese di giustizia (D.P.R. 115/2002, Parte III). Aiuta a inquadrare le spettanze, a individuare il tipo di onorario applicabile, ad applicare aumenti e riduzioni, a gestire indennita' e spese e a impostare l'istanza di liquidazione e l'eventuale opposizione al decreto di pagamento (artt. 168, 170). Use when an engineer serving as court-appointed expert (CTU/ausiliario) must prepare or check a fee-liquidation request under the Italian TU spese di giustizia; it is a documentary aid and does NOT compute the numeric amounts (the tariff tables are set by the Ministero della Giustizia decree DM 30/5/2002, not reproduced), does not draft the judge's payment decree and does not cover party-appointed consultant (CTP) fees.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/compensi-ctu-dpr115
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: litigation
language: it
tags: [dpr-115-2002, ctu, compensi-ausiliari, ingegneria-forense, liquidazione]
sources:
- title: Compensi Ctu Checklist
  path: references/estratti/compensi-ctu-checklist.md
- title: Dpr 115 2002
  path: references/fonti/dpr-115-2002.md
---

# Compensi del CTU / ausiliario del magistrato (D.P.R. 115/2002)

## Quando usare questa skill

Usala quando, come **ingegnere iscritto all'albo dei CTU** (o comunque **ausiliario
del magistrato**), devi **predisporre o verificare l'istanza di liquidazione** dei
tuoi compensi ai sensi del **Testo Unico spese di giustizia (D.P.R. 115/2002, Parte
III)**:

- inquadrare le **spettanze**: onorario, indennita'/spese di viaggio, rimborso
  spese (art. 49);
- individuare il **tipo di onorario** (fisso; variabile per difficolta'/completezza/
  pregio; **a tempo** con vacazioni/compenso orario) (artt. 50-51);
- applicare **aumenti e riduzioni**: urgenza fino al **20%**, eccezionale
  complessita' fino al **doppio**, riduzione per mancato completamento, **incarico
  collegiale +40%** per componente (artt. 51-53);
- gestire **indennita' e spese** (viaggio/soggiorno, nota specifica) (artt. 55-56);
- impostare la **liquidazione** (decreto di pagamento) e l'eventuale **opposizione**
  (artt. 168, 170).

**Non e' una skill di calcolo numerico**: gli **importi** delle tariffe (vacazione,
onorari fissi/variabili, scaglioni a percentuale) sono nelle **tabelle del DM
30/5/2002** (delegate dall'art. 50, aggiornate ISTAT ex art. 54), **non riprodotte**.

## Cosa NON fa (limiti)

- Non **calcola l'importo** finale: le tabelle tariffarie numeriche sono nel **DM
  30/5/2002** (non su Normattiva) e vanno lette a parte.
- Non redige il **decreto di pagamento** (spetta al magistrato) ne' l'atto di
  opposizione.
- Non tratta i compensi del **CTP** (consulente tecnico di parte, a contratto):
  solo gli **ausiliari del magistrato** (CTU, periti, custodi, commissario ad acta).

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-compenso`](tasks/inquadra-compenso.md) | Dato l'incarico, individua le spettanze (art. 49), il tipo di onorario (artt. 50-51) e gli aumenti/riduzioni applicabili (artt. 51-53) |
| [`prepara-istanza-liquidazione`](tasks/prepara-istanza-liquidazione.md) | Struttura l'istanza di liquidazione (onorario + indennita' + spese documentate) e richiama la procedura del decreto di pagamento e dell'opposizione (artt. 55-56, 168, 170) |

## Riferimenti normativi

- **D.P.R. 30/5/2002 n. 115** (T.U. spese di giustizia), Parte III - **artt. 49-58**
  (compensi, indennita', spese degli ausiliari; adeguamento; custodia) e **artt.
  168, 170** (decreto di pagamento; opposizione ex art. 15 D.Lgs 150/2011).
- **DM 30/5/2002** (tabelle tariffarie, delegato dall'art. 50) - **citato, non
  riprodotto** (non reperibile su Normattiva).

Dettaglio in `references/sources.yaml`, `references/fonti/dpr-115-2002.md`,
`references/estratti/compensi-ctu-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la determinazione degli importi (tabelle DM), la
valutazione della difficolta'/complessita' e la liquidazione con decreto motivato
spettano al **magistrato**; l'ammontare finale dipende dalle tabelle tariffarie
vigenti. La skill **non sostituisce** il magistrato, il consulente legale ne' la
lettura delle tabelle del DM.
