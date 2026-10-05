# distanze-legali-costruzioni-cc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato civilista / CTU esperto di distanze da completare)

Skill di **supporto documentale** alle **distanze legali nelle costruzioni** e alla disciplina
delle **luci e vedute** del **Codice civile** (artt. 873-907), di diretto interesse per la
progettazione edilizia e le questioni di confine.

**Non risolve il caso concreto**, **non misura** in sito e **non sostituisce** il tecnico o il
consulente legale: inquadra i minimi civilistici e il coordinamento con l'urbanistica.

## Target

Ingegneri, architetti, geometri e CTU che verificano le distanze in un progetto o in una
controversia di confine.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-distanze-costruzioni` | Verifica le distanze tra costruzioni, muro di cinta, pozzi/tubi e alberi rispetto al confine |
| `verifica-luci-vedute` | Distingue luci e vedute e verifica le distanze delle aperture e delle costruzioni (artt. 905-907) |

Nucleo: distanza 3 m tra costruzioni (art. 873), muro di cinta (art. 878), pozzi 2 m / tubi 1 m
(art. 889), alberi 3/1,5/0,5 m (art. 892), vedute (diretta 1,5 m art. 905, obliqua 0,75 m art. 906,
costruzioni a 3 m dalle vedute acquisite art. 907).

## Fonti consultate

- **Codice civile (R.D. 16 marzo 1942, n. 262)** - artt. 873-907 - testo vigente su Normattiva
  (indice pinnato a `!vig=2026-07-16`, codice 042U0262)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- Le distanze civilistiche sono un **minimo derogabile in aumento** dai **regolamenti locali** e
  vanno coordinate con il **DM 1444/1968 art. 9** (distanze tra pareti finestrate), non riprodotto.
- **Non risolve il caso concreto** (servitù, usucapione della veduta, comunione del muro,
  prevenzione) né misura in sito.
- **Non sostituisce** il tecnico (verifica progettuale) né il consulente legale.

**La skill è un supporto documentale: non sostituisce il tecnico, il consulente legale né la
lettura del Codice civile e dei regolamenti edilizi/urbanistici locali.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
