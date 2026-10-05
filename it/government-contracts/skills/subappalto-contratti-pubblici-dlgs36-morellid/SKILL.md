---
name: subappalto-contratti-pubblici-dlgs36-morellid
title: Subappalto nei contratti pubblici (D.Lgs. 36/2023 art. 119)
description: Supporto documentale alla disciplina del subappalto nei contratti pubblici secondo il Codice dei contratti pubblici (D.Lgs. 31 marzo 2023, n. 36), art. 119. Use when an engineer, RUP, or economic operator must qualify a subcontracting arrangement in an Italian public contract and set up its authorization under D.Lgs. 36/2023 art. 119; it is a documentary aid and does NOT issue the authorization, does NOT verify the subcontractor's requirements, and does NOT replace the contracting authority or the RUP.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/subappalto-contratti-pubblici-dlgs36
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: government-contracts
language: it
tags: [subappalto, dlgs-36-2023, contratti-pubblici, codice-appalti, pagamento-diretto]
sources:
- title: Subappalto Checklist
  path: references/estratti/subappalto-checklist.md
- title: Dlgs 36 2023 Art119
  path: references/fonti/dlgs-36-2023-art119.md
---

# Subappalto nei contratti pubblici (D.Lgs. 36/2023 art. 119)

## Quando usare questa skill

Usala quando un **ingegnere, RUP, operatore di stazione appaltante o operatore economico**
deve inquadrare un **affidamento a terzi** in un **contratto pubblico** rispetto alla
disciplina del **subappalto**, secondo l'**art. 119 del Codice dei contratti pubblici**
(D.Lgs. 31 marzo 2023, n. 36):

- stabilire se l'affidamento **e' subappalto** (nozione e **soglie** del comma 2);
- distinguere i **sub-contratti** e le attivita' che **non** configurano subappalto (comma 3);
- verificare **condizioni**, **trasmissione**, **responsabilita' solidale**, **pagamento
  diretto** e **autorizzazione**.

Per la fase di **gara** (bandi-tipo, offerte, requisiti) usa `bandi-tipo-anac-checker`,
`oepv-valutatore-offerte-tecniche` e `specifiche-tecniche-ict-appalti-dlgs36`: questa copre
l'**istituto del subappalto** in fase esecutiva.

## Regola generale e nozione (commi 1-2)

- **Regola generale** (c. 1): gli affidatari **eseguono in proprio** le prestazioni. E'
  **nulla** la **cessione del contratto** (salvo art. 120, c. 1, lett. d) e l'accordo che
  affidi a terzi l'**integrale** esecuzione, o la **prevalente** esecuzione della **categoria
  prevalente** e dei contratti ad alta intensita' di manodopera. Il subappalto e' ammesso
  **solo** secondo l'art. 119.
- **Nozione** (c. 2): contratto con cui l'appaltatore affida a terzi **parte** delle
  prestazioni, con **organizzazione di mezzi e rischi** a carico del subappaltatore. Per i
  **lavori** e' comunque subappalto qualsiasi contratto con impiego di manodopera (forniture
  con posa in opera, noli a caldo) se **singolarmente** di importo **> 2%** delle prestazioni
  affidate **oppure > 100.000 euro** **e** con **incidenza del costo della manodopera > 50%**
  dell'importo del contratto da affidare.
- I **sub-contratti che non sono subappalto** vanno comunque **comunicati** alla stazione
  appaltante **prima dell'inizio** (nome, importo, oggetto).

## Cosa NON e' subappalto (comma 3)

Non si configurano come subappalto: l'affidamento di **attivita' secondarie/accessorie a
lavoratori autonomi** (con comunicazione); la **subfornitura a catalogo** di prodotti
informatici; l'affidamento di **servizi < 20.000 euro/anno a imprenditori agricoli** in
comuni montani/isole minori; le prestazioni rese in forza di **contratti continuativi di
cooperazione** stipulati **prima** dell'indizione della procedura.

## Condizioni, trasmissione e autorizzazione (commi 4-5, 16)

- **Condizioni** (c. 4), previa **autorizzazione**: subappaltatore **qualificato**; **assenza**
  di cause di esclusione; parti da subappaltare **indicate in offerta**.
- **Trasmissione** (c. 5): contratto di subappalto trasmesso **almeno venti giorni prima**
  dell'inizio, con **dichiarazione** del subappaltatore sui requisiti (artt. 100 e 103),
  verificata tramite la **Banca dati nazionale contratti pubblici**.
- **Autorizzazione** (c. 16): rilasciata **entro trenta giorni** (prorogabile **una sola
  volta**); decorso il termine **si intende concessa** (silenzio-assenso). Per subappalti
  **< 2%** o **< 100.000 euro** i termini sono **ridotti della meta'**.

## Responsabilita', pagamento diretto e tutele (commi 6-12)

- **Responsabilita' solidale** (c. 6-7): contraente principale e subappaltatore in solido
  verso la stazione appaltante; solidarieta' per obblighi retributivi/contributivi; DURC
  d'ufficio.
- **Pagamento diretto** al subappaltatore (c. 11): (a) subcontraente **microimpresa o piccola
  impresa**; (b) **inadempimento** dell'appaltatore; (c) **su richiesta** del subcontraente se
  la natura del contratto lo consente. Nei casi **a) e c)** l'appaltatore e' **liberato** dalla
  responsabilita' solidale del comma 6.
- **Tutele** (c. 12): trattamento **non inferiore** e **stesso CCNL** del contraente principale
  (o equivalente) per attivita' coincidenti o della categoria prevalente; **costi della
  sicurezza e della manodopera senza ribasso**.

## Subappalto a cascata (comma 17)

Le stazioni appaltanti indicano nei documenti di gara le prestazioni che, **pur
subappaltabili, non** possono essere **ulteriormente** subappaltate; all'ulteriore subappalto
si applicano comunque le disposizioni dell'art. 119.

## Cosa NON fa (limiti)

- **Non rilascia l'autorizzazione** al subappalto e **non verifica** i requisiti/qualificazione
  del subappaltatore.
- **Non sostituisce** la stazione appaltante ne' il RUP nelle valutazioni discrezionali (es.
  individuazione delle prestazioni da eseguire a cura dell'aggiudicatario, comma 2).
- **Non tratta** la fase di gara (requisiti, offerta, aggiudicazione) ne' la disciplina di
  altri istituti (avvalimento, contratti continuativi di cooperazione) se non nei richiami
  dell'art. 119.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`qualifica-subappalto`](tasks/qualifica-subappalto.md) | Stabilisce se un affidamento a terzi e' subappalto (soglie comma 2), sub-contratto da comunicare o attivita' non configurante subappalto (comma 3) |
| [`imposta-autorizzazione-subappalto`](tasks/imposta-autorizzazione-subappalto.md) | Imposta condizioni, trasmissione (20 giorni), autorizzazione (30 giorni), responsabilita' solidale e pagamento diretto |

## Riferimenti normativi

- **D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti pubblici) - **art. 119** (Subappalto):
  commi 1-2 (regola generale, nozione, soglie), 3 (attivita' non configuranti subappalto), 4-5
  (condizioni, trasmissione), 6-7 (responsabilita' solidale), 11 (pagamento diretto), 12
  (tutele dei lavoratori), 16 (autorizzazione a 30 giorni), 17 (subappalto a cascata).
- Articoli **richiamati** dall'art. 119 (non riprodotti): artt. **100 e 103** (qualificazione),
  **11** (CCNL), **120** (modifiche del contratto), **allegato II.2-bis** (revisione prezzi),
  **Capo II del Titolo IV della Parte V del Libro II** (cause di esclusione).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-36-2023-art119.md`,
`references/estratti/subappalto-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la qualificazione del subappalto, la verifica dei requisiti
del subappaltatore e il rilascio dell'autorizzazione restano responsabilita' dell'operatore
economico, della **stazione appaltante** e del **RUP**, sul testo vigente dell'art. 119 (il
Codice e' soggetto a decreti correttivi). La skill **non sostituisce** la stazione appaltante,
il RUP ne' la lettura dell'art. 119 e degli articoli da esso richiamati.
