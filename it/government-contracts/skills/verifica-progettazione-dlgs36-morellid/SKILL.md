---
name: verifica-progettazione-dlgs36-morellid
title: Verifica della progettazione e validazione del progetto (D.Lgs. 36/2023 art. 42)
description: Supporto documentale al RUP (responsabile unico del progetto), al soggetto verificatore e al progettista per la verifica della progettazione e la validazione del progetto posto a base di gara nei contratti pubblici di lavori, ai sensi del D.Lgs. 31 marzo 2023, n. 36 (Codice dei contratti pubblici), art. 42. Use when a project procedure manager (RUP), a design checker, or a designer must frame the design verification and the validation of the project put out to tender under D.Lgs. 36/2023 art. 42; it is a documentary aid and does NOT perform the verification, does NOT draft the verification report or the validation act, does NOT reproduce annex I.7 or the seismic obligations, and does NOT replace the RUP, the checker, or the designer.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/verifica-progettazione-dlgs36
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: government-contracts
language: it
tags: [verifica-progettazione, validazione-progetto, dlgs-36-2023, contratti-pubblici, rup]
sources:
- title: Verifica Progettazione Checklist
  path: references/estratti/verifica-progettazione-checklist.md
- title: Dlgs 36 2023 Art 42
  path: references/fonti/dlgs-36-2023-art-42.md
---

# Verifica della progettazione e validazione del progetto (D.Lgs. 36/2023 art. 42)

## Quando usare questa skill

Usala quando un **RUP** (responsabile unico del progetto), un **soggetto verificatore** o un
**progettista** deve **inquadrare** la **verifica della progettazione** e la **validazione** del progetto
posto a base di gara nei **contratti pubblici di lavori**, secondo il **D.Lgs. 31 marzo 2023, n. 36**
(Codice dei contratti pubblici), **art. 42**:

- **oggetto** e **tempi** della verifica in relazione al livello progettuale (c. 1);
- **ruolo del RUP** e **incompatibilità** della verifica (c. 2);
- **effetti** della verifica positiva (deposito sismico, denuncia al genio civile) (c. 3);
- **validazione** del progetto a base di gara (c. 4) e rinvio all'**Allegato I.7** (c. 5).

**Non è** uno strumento che esegue la verifica o redige il rapporto/atto di validazione: è un **supporto
documentale** che inquadra oggetto, tempi, soggetti ed effetti.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-progetto` | Inquadra oggetto e tempi della verifica per livello, il ruolo del RUP e le incompatibilità (art. 42 cc. 1-2) |
| `inquadra-validazione-effetti` | Inquadra gli effetti della verifica positiva (deposito sismico, Archivio OO.PP.) e la validazione a base di gara (art. 42 cc. 3-5) |

## Punti chiave (verificati sul testo)

- **Oggetto** (c. 1): rispondenza al **documento d'indirizzo (DIP)** + **conformità alla normativa**;
  verifica **durante lo sviluppo**, per livello (**PFTE**/esecutivo). Congiunto/PPP: PFTE **prima
  dell'affidamento**, esecutivo **prima dell'inizio lavori**.
- **RUP e incompatibilità** (c. 2): il RUP verifica o **segue** con **contraddittorio**; la verifica è
  **incompatibile** con progettazione, coordinamento sicurezza, **direzione lavori** e **collaudo**.
- **Effetti** (c. 3): la verifica positiva **assolve** deposito/autorizzazione **sismica** e **denuncia
  al genio civile**; deposito nell'**Archivio informatico nazionale delle opere pubbliche** (MIT).
- **Validazione** (c. 4): **atto formale** del **RUP** con gli esiti della verifica, riferito al
  **rapporto conclusivo** e alle **controdeduzioni** del progettista; **estremi nel bando/lettera
  d'invito**.
- **Contenuti/soggetti** (c. 5): **Allegato I.7** (contenuti, modalità e soggetti; correlati all'importo
  dei lavori); oneri **nelle risorse dell'opera**.

## Fonti

- **D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti pubblici) - **art. 42** - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 23G00044, idGruppo 5).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non esegue** la verifica né redige il **rapporto di verifica** o l'**atto di validazione**.
- **Non riproduce** l'**Allegato I.7** (soglie di importo e soggetti verificatori) né gli **obblighi
  sismici** del DPR 380.
- **Non tratta** la **verifica di conformità/collaudo in esecuzione** (skill
  `collaudo-verifica-conformita-dlgs36`) né i **contenuti del PFTE** (skill `pfte-allegato-i7-checker`)
  se non nei richiami.

**La skill è un supporto documentale: non sostituisce il RUP, il soggetto verificatore o il progettista,
né la lettura dell'art. 42 del D.Lgs. 36/2023 e dell'Allegato I.7.**
