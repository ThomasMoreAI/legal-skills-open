---
name: psc-piano-sicurezza-coordinamento-dlgs81-morellid
title: PSC - Piano di Sicurezza e Coordinamento (D.Lgs 81/2008 art. 100 + Allegato XV)
description: 'Supporto documentale al coordinatore per la sicurezza in fase di progettazione (CSP) e al coordinatore per l''esecuzione (CSE) per la redazione e la verifica di completezza del Piano di Sicurezza e Coordinamento (PSC) nei cantieri temporanei o mobili secondo il D.Lgs 81/2008, art. 100 e Allegato XV. Aiuta a inquadrare: l''obbligo e la titolarita'' del PSC; l''articolo 100; i contenuti minimi del punto 2.1.2 dell''Allegato XV; i contenuti in riferimento all''area, all''organizzazione del cantiere e alle lavorazioni e interferenze (punti 2.2 e 2.3); e la stima dei costi della sicurezza del punto 4.1. Use when a safety coordinator (CSP/CSE) must draft or check the completeness of a Piano di Sicurezza e Coordinamento under the Italian D.Lgs 81/2008 art. 100 and Allegato XV; it is a documentary aid, does NOT replace the coordinator''s signed plan nor the site risk assessment, and is distinct from the POS.'
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/psc-piano-sicurezza-coordinamento-dlgs81
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: construction
language: it
tags: [psc, sicurezza-cantieri, coordinatore-sicurezza, dlgs-81-2008, costi-sicurezza]
sources:
- title: Psc Checklist
  path: references/estratti/psc-checklist.md
- title: Dlgs 81 2008 Art 100 Allegato Xv
  path: references/fonti/dlgs-81-2008-art-100-allegato-xv.md
---

# PSC - Piano di Sicurezza e Coordinamento (D.Lgs 81/2008 art. 100 + Allegato XV)

## Quando usare questa skill

Usala quando un **coordinatore per la sicurezza in fase di progettazione (CSP)** o **in fase di esecuzione (CSE)**
deve **redigere** o **verificare la completezza** di un **Piano di Sicurezza e Coordinamento (PSC)** nei cantieri
temporanei o mobili secondo il **D.Lgs 81/2008**, **art. 100** e **Allegato XV**:

- **obbligo e titolarità** del PSC (nomina CSP/CSE, art. 90; redazione CSP, art. 91; verifica/adeguamento CSE, art. 92);
- **art. 100** (natura, tavole, parte integrante del contratto, copia agli RLS);
- **contenuti minimi** del PSC (Allegato XV, punto 2.1.2) e in riferimento ad area/organizzazione/lavorazioni/
  interferenze (punti 2.2-2.3);
- **stima dei costi della sicurezza** (Allegato XV, punto 4.1).

È un **supporto documentale**: inquadra i contenuti minimi e la stima dei costi; **non** redige il piano al posto del
coordinatore né esegue la valutazione dei rischi del cantiere. È **distinta** da `pos-allegato-xv-checker` (POS,
redatto dal datore dell'impresa esecutrice) e da `coordinatori-sicurezza-cantieri-dlgs81` (ruoli/obblighi CSP/CSE).

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-contenuti-minimi-psc` | Obbligo/titolarità (artt. 90-92, 100) e contenuti minimi del PSC: punto 2.1.2 lett. a)-l), aree/organizzazione/lavorazioni (2.2), interferenze e cronoprogramma (2.3) |
| `imposta-stima-costi-sicurezza` | Stima dei costi della sicurezza (Allegato XV punto 4.1): voci, stima congrua/analitica, costi non soggetti a ribasso, liquidazione |

## Punti chiave (dal testo di legge)

- **Obbligo/titolarità**: nei cantieri con **più imprese anche non contemporanea** si nominano CSP e CSE (art. 90
  c.3-4); il **CSP redige** il PSC (art. 91 c.1 lett. a), il **CSE verifica e adegua** (art. 92 c.1).
- **Art. 100**: il PSC è **relazione tecnica + prescrizioni + stima costi** (punto 4 All. XV), **corredato da tavole**
  (almeno una planimetria); è **parte integrante del contratto**; copia agli **RLS almeno 10 giorni prima**.
- **Contenuti minimi** (Allegato XV, 2.1.2): a) identificazione/descrizione opera; b) soggetti con compiti di
  sicurezza; c) relazione **analisi/valutazione dei rischi**; d) scelte/procedure/misure per area/organizzazione/
  lavorazioni; e) prescrizioni operative e **DPI** per le **interferenze**; f) **misure di coordinamento** uso comune;
  g) cooperazione/coordinamento; h) **pronto soccorso/antincendio/evacuazione**; i) **cronoprogramma** ed entità in
  **uomini-giorno**; l) **stima dei costi**.
- **Costi della sicurezza** (Allegato XV, 4.1): apprestamenti, misure/DPI interferenze, impianti terra/antincendio/
  evacuazione fumi, mezzi di protezione collettiva, procedure, interventi di sfasamento, misure di coordinamento;
  stima **congrua e analitica**; **NON soggetti a ribasso** (4.1.4); liquidati dal **DL su approvazione del CSE**.

## Fonti

- **D.Lgs 9 aprile 2008 n. 81** - **art. 100 e Allegato XV** - Testo coordinato Edizione gennaio 2025 (INL), SHA256
  `f593e18...`, estratto con `pdftotext`. Edizione INL non ufficiale: per uso autoritativo cross-checkare su
  Normattiva/Gazzetta Ufficiale.

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti

- **Non redige** il PSC al posto del coordinatore né esegue la **valutazione dei rischi** del cantiere; non calcola
  i costi.
- **Non tratta** il **POS** (Allegato XV punto 3.2, → skill `pos-allegato-xv-checker`), i **ruoli/obblighi** di CSP/CSE
  (artt. 89-92, → skill `coordinatori-sicurezza-cantieri-dlgs81`), il **fascicolo dell'opera** (Allegato XVI) né la
  **notifica preliminare** (art. 99).
- **Non** sostituisce il coordinatore firmatario del piano.

**La skill è un supporto documentale: non sostituisce il coordinatore per la sicurezza firmatario del PSC né la lettura dell'art. 100 e dell'Allegato XV del D.Lgs 81/2008.**
