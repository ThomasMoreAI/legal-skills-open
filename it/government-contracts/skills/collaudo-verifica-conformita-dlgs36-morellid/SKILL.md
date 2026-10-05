---
name: collaudo-verifica-conformita-dlgs36-morellid
title: Collaudo e verifica di conformita' - D.Lgs. 36/2023 art. 116
description: Supporto documentale al collaudo dei lavori e alla verifica di conformita' di servizi e forniture nei contratti pubblici ai sensi del D.Lgs. 36/2023, art. 116. Use when a RUP, tender officer, testing engineer (collaudatore) or economic operator must frame the testing/conformity-verification phase closing an Italian public contract; it is a documentary aid, does not draft the test certificate or the CRE, does not reproduce Annex II.14, does not appoint the testers and does not replace the contracting authority, the RUP or the testing body.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/collaudo-verifica-conformita-dlgs36
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: government-contracts
language: it
tags: [dlgs-36-2023, codice-contratti-pubblici, collaudo, verifica-conformita, certificato-regolare-esecuzione, esecuzione-contratto]
sources:
- title: Collaudo Verifica Checklist
  path: references/estratti/collaudo-verifica-checklist.md
- title: L 152 2026 Sospensione Recupero Anticipazione
  path: references/estratti/l-152-2026-sospensione-recupero-anticipazione.md
- title: Dlgs 36 2023 Art 116
  path: references/fonti/dlgs-36-2023-art-116.md
- title: L 152 2026 Gu 192
  path: references/fonti/l-152-2026-gu-192.md
---

# Collaudo e verifica di conformita' - D.Lgs. 36/2023 art. 116

## Quando usare questa skill

Usala quando devi **inquadrare la fase di collaudo/verifica di conformita'** che chiude
un contratto pubblico e ancorarla al **D.Lgs. 36/2023, art. 116**:

- distinguere il **collaudo** (per i **lavori**) dalla **verifica di conformita'** (per
  **servizi e forniture**) e la loro funzione: certificare il rispetto delle
  **caratteristiche tecniche, economiche e qualitative**, degli **obiettivi** e dei
  **tempi** (c. 1);
- i **termini** - **art. 116 c. 2**: completamento **entro 6 mesi** dall'ultimazione
  (elevabile a **1 anno** per i casi di **particolare complessita'** dell'allegato
  II.14; riducibile per opere di limitata complessita'); il **certificato** ha
  carattere **provvisorio** e diventa **definitivo dopo 2 anni**, con **approvazione
  tacita**;
- la **responsabilita' dell'appaltatore** per vizi e difformita' (anche riconoscibili)
  denunciati prima che il certificato diventi definitivo, **salvo l'art. 1669 c.c.**
  (c. 3);
- la **nomina dei collaudatori** (da **1 a 3**, requisiti di **moralita', competenza,
  professionalita'** e **indipendenza**), il **collaudatore statico** e la **segreteria
  tecnica** (cc. 4, 4-bis, 4-ter);
- la **verifica di conformita'** per servizi/forniture da parte del **RUP** o del
  **direttore dell'esecuzione** (c. 5);
- le **incompatibilita'** all'incarico (c. 6) e il rinvio all'**allegato II.14** per le
  **modalita'/tempi** e i casi di **certificato di regolare esecuzione (CRE)** (c. 7),
  con le regole su tempi, documenti finali e **accertamenti di laboratorio** non
  soggetti a ribasso (cc. 8-11).

Sul versante contabile della chiusura, la skill segnala anche la **deroga temporanea
in vigore dal 21 agosto 2026**: l'**art. 1-bis del D.L. 107/2026** (inserito dalla
**L. 7 agosto 2026, n. 152**) autorizza le stazioni appaltanti, **su richiesta
dell'appaltatore**, a **sospendere il recupero dell'anticipazione** dell'**art. 125
D.Lgs. 36/2023** negli **appalti di lavori in corso di esecuzione**, per il tempo
strettamente necessario e comunque **non oltre il 31 dicembre 2026**, con
**esclusione degli interventi finanziati anche solo in parte con risorse PNRR**.
Poiche' l'**art. 125 c. 7** lega il certificato di pagamento della **rata di saldo**
all'esito positivo del collaudo o della verifica di conformita', alla chiusura del
contratto puo' residuare una quota di anticipazione non recuperata. Il testo
dell'art. 1-bis **non menziona l'art. 116** e non contiene alcuna disposizione su
termini del collaudo, natura del certificato o responsabilita' per vizi.

**Non e' una skill che redige atti**: non compila il certificato di collaudo/CRE, non
riproduce l'allegato II.14, non nomina i collaudatori e non sostituisce la stazione
appaltante, il RUP o l'organo di collaudo.

## Cosa NON fa (limiti)

- Non **redige** il **certificato di collaudo**, il **certificato di verifica di
  conformita'** ne' il **CRE**: fornisce lo schema di riferimento normativo.
- Non riproduce l'**allegato II.14** (modalita' tecniche, tempi, casi di CRE, compensi)
  ne' l'**allegato II.15** (costi degli accertamenti di laboratorio): sono citati.
- Non **nomina** i collaudatori ne' verifica in concreto i **requisiti/incompatibilita'**
  (art. 16, conflitto di interesse): fornisce l'elenco dei casi.
- Non tratta il **collaudo statico** strutturale (DPR 380 art. 67): coperto da
  `denuncia-opere-strutturali-l1086`.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`inquadra-collaudo-termini`](tasks/inquadra-collaudo-termini.md) | Distingue collaudo/verifica di conformita' e ricostruisce i termini e la natura del certificato (provvisorio/definitivo), con la responsabilita' dell'appaltatore (art. 116 cc. 1-3, 7) |
| [`verifica-collaudatori-incompatibilita`](tasks/verifica-collaudatori-incompatibilita.md) | Inquadra la nomina dei collaudatori/verificatori (numero, requisiti) e i casi di incompatibilita' all'incarico (art. 116 cc. 4-6) |

## Riferimenti normativi

- **D.Lgs. 31/3/2023 n. 36** (Codice dei contratti pubblici) - **art. 116** (Collaudo e
  verifica di conformita'); rinvio all'**allegato II.14** (modalita'/CRE) e
  all'**allegato II.15** (costi accertamenti).
- **L. 7 agosto 2026, n. 152** (conversione del D.L. 26 giugno 2026, n. 107; GU Serie
  generale n. 192 del 20/8/2026) - **art. 1-bis** del D.L. 107/2026, con il testo
  dell'**art. 125 D.Lgs. 36/2023** riportato nei "Riferimenti normativi" della stessa
  GU. **Deroga a termine: scade il 31 dicembre 2026.**

Dettaglio in `references/sources.yaml`,
`references/fonti/dlgs-36-2023-art-116.md`,
`references/fonti/l-152-2026-gu-192.md`,
`references/estratti/collaudo-verifica-checklist.md`,
`references/estratti/l-152-2026-sospensione-recupero-anticipazione.md`.

## Avvertenza

Skill di **supporto documentale**: la nomina dei collaudatori, lo svolgimento del
collaudo/verifica, la redazione del certificato o del CRE e ogni determinazione sul
caso concreto restano in capo alla **stazione appaltante**, al **RUP** e all'**organo
di collaudo/verifica**, con l'**allegato II.14**. **Non sostituisce** la stazione
appaltante, il RUP ne' l'organo di collaudo, ne' la lettura dell'art. 116 del D.Lgs.
36/2023.
