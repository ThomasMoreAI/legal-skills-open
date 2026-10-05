---
name: distanze-legali-costruzioni-cc-morellid
title: Distanze legali nelle costruzioni, luci e vedute (Codice civile)
description: Supporto documentale alle distanze legali nelle costruzioni e alla disciplina delle luci e vedute del Codice civile (artt. 873-907), di diretto interesse per la progettazione edilizia. Use when an engineer, architect, geometra, or CTU must check the Italian civil-law distances between buildings, wells, pipes, trees and the rules on lights and views for a design or a boundary dispute; it is a documentary aid that frames the civil-law minimums (which local building regulations may increase) and the coordination with town-planning rules (e.g. Ministerial Decree 1444/1968, Article 9, on distances between windowed walls, not reproduced), and does NOT resolve the specific case, does not measure the distances on site and does not replace the technician or the legal adviser.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/distanze-legali-costruzioni-cc
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: construction
language: it
tags: [distanze-legali, codice-civile, luci-e-vedute, distanze-costruzioni, edilizia]
sources:
- title: Distanze Costruzioni Checklist
  path: references/estratti/distanze-costruzioni-checklist.md
- title: Cc Distanze 873 907
  path: references/fonti/cc-distanze-873-907.md
---

# Distanze legali nelle costruzioni, luci e vedute (Codice civile)

## Quando usare questa skill

Usala quando un **ingegnere, architetto, geometra o CTU** deve verificare le **distanze legali**
nelle costruzioni e la disciplina delle **luci e vedute** del **Codice civile** (artt. 873-907),
per un progetto o per una questione di confine:

- **distanza tra costruzioni**, muro di cinta, costruzione in aderenza;
- distanze per **pozzi, tubi, depositi** e **alberi**;
- **luci e vedute** (aperture, balconi, distanze).

Le distanze del codice civile sono un **minimo derogabile in aumento** dai **regolamenti locali**
e vanno coordinate con la disciplina **urbanistico-edilizia** (es. **DM 1444/1968 art. 9**,
distanze tra pareti finestrate), qui richiamata ma non riprodotta.

## Distanze nelle costruzioni (artt. 873-879)

- **Art. 873 - distanza tra costruzioni**: le costruzioni su **fondi finitimi**, se non unite o
  aderenti, devono stare a **distanza non minore di 3 metri**; i **regolamenti locali** possono
  stabilire una **distanza maggiore**.
- **Art. 878 - muro di cinta**: il muro di cinta (o altro muro isolato) **non superiore a 3 m**
  **non** e' computato ai fini della distanza dell'art. 873.
- **Art. 877 - costruzione sul confine / in aderenza** e **art. 879 - edifici non soggetti**:
  disciplinano l'aderenza al confine e i casi di esenzione (verificarne le condizioni).

## Pozzi, tubi, depositi (artt. 889-890)

- **Art. 889**: **pozzi, cisterne, fosse** di latrina o concime presso il confine -> **almeno 2
  metri** (dal confine al perimetro interno dell'opera); **tubi** d'acqua, gas e simili ->
  **almeno 1 metro** dal confine.
- **Art. 890**: **fabbriche e depositi nocivi o pericolosi** -> distanze dei regolamenti e cautele
  per non danneggiare il vicino.

## Alberi (art. 892)

Distanze dal confine (salvo regolamenti/usi locali): **3 metri** per gli alberi di **alto fusto**;
**1,5 metri** per quelli **non di alto fusto**; **0,5 metri** per **viti, arbusti, siepi vive e
piante da frutto** non superiori a 2,5 m (con eccezioni: **1 m** per siepi di ontano/castagno che
si recidono periodicamente, **2 m** per le siepi di robinie). Nessuna distanza se sul confine
esiste un **muro divisorio** e le piante non superano la sommita' del muro.

## Luci e vedute (artt. 900-907)

- **Luci vs vedute** (art. 900): le **luci** danno passaggio a luce e aria ma **non** permettono
  di affacciarsi; le **vedute** permettono di **affacciarsi** e guardare. A esse si applicano
  regole diverse (luci: artt. 901-904).
- **Art. 905 - veduta diretta e balconi**: **distanza minima 1,5 metri** tra il fondo del vicino
  e la faccia esteriore del muro/lo sporto (balconi, terrazze, lastrici con parapetto).
- **Art. 906 - veduta laterale od obliqua**: **distanza minima 0,75 metri**, misurata dal piu'
  vicino lato della finestra o dello sporto.
- **Art. 907 - costruzioni dalle vedute acquisite**: chi ha acquistato il diritto di **veduta
  diretta** impedisce al vicino di **fabbricare a meno di 3 metri** (misurati ai sensi dell'art.
  905); per la veduta obliqua, i 3 metri valgono anche dai lati della finestra.

## Cosa NON fa (limiti)

- **Non risolve il caso concreto** ne' **misura** le distanze in sito: inquadra le regole
  civilistiche e i minimi.
- **Non riproduce la disciplina urbanistico-edilizia** (regolamenti edilizi comunali, DM
  1444/1968): la richiama per il coordinamento.
- **Non sostituisce** il tecnico (verifica progettuale) ne' il **consulente legale** (contenzioso
  su distanze, comunione del muro, prevenzione, servitu').

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-distanze-costruzioni`](tasks/verifica-distanze-costruzioni.md) | Verifica le distanze tra costruzioni, muro di cinta, pozzi/tubi e alberi rispetto al confine |
| [`verifica-luci-vedute`](tasks/verifica-luci-vedute.md) | Distingue luci e vedute e verifica le distanze delle aperture e delle costruzioni (artt. 905-907) |

## Riferimenti normativi

- **Codice civile** (R.D. 16 marzo 1942, n. 262) - **art. 873** (distanze tra costruzioni),
  **artt. 877-879** (aderenza, muro di cinta, esenzioni), **art. 889** (pozzi/tubi), **art. 890**
  (depositi nocivi/pericolosi), **art. 892** (alberi), **artt. 900-904** (luci), **artt. 905-907**
  (vedute).
- **DM 2 aprile 1968, n. 1444** - **art. 9** (distanze minime tra fabbricati/pareti finestrate) -
  richiamato per il coordinamento urbanistico, non riprodotto.

Dettaglio in `references/sources.yaml`, `references/fonti/cc-distanze-873-907.md`,
`references/estratti/distanze-costruzioni-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la verifica delle distanze nel progetto e la soluzione delle
controversie di confine restano responsabilita' del **tecnico** e del **consulente legale**, sui
regolamenti locali e sulla disciplina urbanistica applicabili. La skill **non sostituisce** il tecnico, il consulente legale ne' la lettura del Codice civile e dei regolamenti edilizi/urbanistici locali.
