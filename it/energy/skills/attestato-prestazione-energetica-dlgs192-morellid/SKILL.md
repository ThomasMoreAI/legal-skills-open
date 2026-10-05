---
name: attestato-prestazione-energetica-dlgs192-morellid
title: 'Attestato di prestazione energetica (APE): obblighi e sanzioni (D.Lgs. 192/2005)'
description: Supporto documentale agli obblighi relativi all'attestato di prestazione energetica (APE) secondo il D.Lgs. 19 agosto 2005, n. 192, artt. 6 e 15. Use when an engineer or professional must frame the obligations around an Italian energy performance certificate (APE) for a sale, lease, or new building under D.Lgs. 192/2005 artt. 6/15; it is a documentary aid and does NOT calculate, draft, or certify the APE, does NOT reproduce the AgID/ministerial technical methods, and does NOT replace the qualified technician or the competent authority.
author: morellid
author_url: https://github.com/morellid/skill-per-ingegneri/tree/main/skills/attestato-prestazione-energetica-dlgs192
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: energy
language: it
tags: [attestato-prestazione-energetica, ape, dlgs-192-2005, certificazione-energetica, compravendita-locazione]
sources:
- title: Ape Checklist
  path: references/estratti/ape-checklist.md
- title: Dlgs 192 2005 Artt 6 15
  path: references/fonti/dlgs-192-2005-artt-6-15.md
---

# Attestato di prestazione energetica (APE): obblighi e sanzioni (D.Lgs. 192/2005)

## Quando usare questa skill

Usala quando un **ingegnere o professionista** (o un proprietario/agenzia) deve inquadrare gli
**obblighi relativi all'attestato di prestazione energetica (APE)** in una **compravendita**,
**locazione** o per un **nuovo edificio**, secondo gli **artt. 6 e 15 del D.Lgs. 19 agosto 2005,
n. 192**:

- stabilire **quando l'APE e' dovuto** e **chi lo produce**;
- gestire **dotazione, consegna, clausola contrattuale** e **annuncio commerciale**;
- conoscere **validita'** e **sanzioni**.

Per la **prestazione dell'involucro** (trasmittanza) usa `trasmittanza-termica-opache-dm2015`;
per la **diagnosi energetica** delle imprese usa `diagnosi-energetica-dlgs102`; per l'**esercizio
degli impianti termici** usa `esercizio-controllo-impianti-termici-dpr74`. Questa skill copre
l'**APE** (dotazione/obblighi/sanzioni), non il calcolo.

## Quando serve l'APE e chi lo produce (art. 6, c. 1-2)

- L'APE e' rilasciato per edifici/unita' **costruiti, venduti o locati** a nuovo locatario.
- **Nuovi edifici** e **ristrutturazioni importanti**: dotati di APE **prima del certificato di
  agibilita'** (a cura del **costruttore**); **esistenti**: a cura del **proprietario**.
- In **vendita/locazione**: il proprietario **rende disponibile** l'APE al potenziale
  acquirente/locatario **all'avvio delle trattative** e lo **consegna al termine**; per la
  vendita/locazione **prima della costruzione**, APE entro **quindici giorni** dalla richiesta di
  agibilita'.

## Clausola nel contratto (art. 6, c. 3)

- Nei contratti di **compravendita** e nelle **nuove locazioni** soggetti a registrazione:
  **clausola** di avvenuta ricezione dell'APE e **copia allegata** (tranne locazione di **singole**
  unita').
- **Omessa dichiarazione/allegazione**: sanzione in solido **3.000-18.000 euro** (locazione di
  singole unita' **1.000-4.000 euro**, **ridotta a meta'** se la durata non eccede **tre anni**);
  resta l'obbligo di presentare dichiarazione/copia entro **quarantacinque giorni**.

## Validita', edifici pubblici, annuncio (art. 6, c. 5-8, 10)

- **Validita'**: massimo **dieci anni**, **aggiornato** a ogni intervento che cambia la **classe**
  energetica; **decade** il **31 dicembre dell'anno successivo** se non si rispettano i controlli
  di efficienza (DPR 74/2013 e 75/2013).
- **Edifici PA aperti al pubblico** > **500 m²** (dal 9/7/2015 > **250 m²**): APE **affisso**
  all'ingresso (c. 6-7).
- **Annuncio commerciale** (salvo residenziali usati < 4 mesi/anno): riporta **indici** di
  prestazione (involucro e globale) e **classe energetica** (c. 8).
- La dotazione **non** e' dovuta se c'e' gia' un APE **in corso di validita'** (c. 10).

## Sanzioni (art. 15)

- **Professionista** che rilascia un APE **senza i criteri** dell'art. 6: **700-4200 euro** (c. 3),
  con comunicazione all'ordine/collegio.
- **Costruttore/proprietario** che **non dota** di APE **nuovi edifici/ristrutturazioni
  importanti**: **3.000-18.000 euro** (c. 7). **Vendita** senza APE: **3.000-18.000 euro** (c. 8).
  **Nuova locazione** senza APE: **300-1.800 euro** (c. 9).
- **Annuncio** senza i parametri energetici: **500-3.000 euro** (c. 10).
- L'APE e' reso come **dichiarazione sostitutiva di atto notorio** (art. 47 DPR 445/2000), con
  controlli ex art. 71 e sanzioni penali ex art. 76 in caso di falso (c. 1-2).

## Cosa NON fa (limiti)

- **Non calcola, non redige e non certifica** l'APE (attivita' del **tecnico abilitato**).
- **Non riproduce** le **metodologie di calcolo** e i **modelli** (DM 26 giugno 2015 - Linee guida
  APE; metodologie ex art. 4; UNI/TS 11300): vi **rinvia**.
- **Non applica** le sanzioni (autorita' competenti: **regioni/comuni**) e non tratta i
  **requisiti minimi** di progetto (art. 3, 4) ne' la relazione tecnica (art. 8) se non come
  richiamo.

## Sotto-attivita'

| Task | Descrizione |
|---|---|
| [`verifica-obbligo-ape`](tasks/verifica-obbligo-ape.md) | Stabilisce se l'APE e' dovuto (nuovo edificio, vendita, locazione), chi lo produce e i tempi/adempimenti (dotazione, consegna, clausola, annuncio) |
| [`inquadra-sanzioni-ape`](tasks/inquadra-sanzioni-ape.md) | Individua la sanzione applicabile (art. 6 c. 3 e art. 15) per mancata dotazione, omessa clausola/allegazione o annuncio senza parametri |

## Riferimenti normativi

- **D.Lgs. 19 agosto 2005, n. 192** - **art. 6** (APE: rilascio, dotazione prima dell'agibilita',
  disponibilita' e consegna, clausola e allegazione con sanzioni, validita' 10 anni, affissione
  edifici pubblici, annuncio commerciale, contenuti e sistema informativo/catasto), **art. 15**
  (sanzioni: DSAN ex DPR 445/2000; professionista 700-4200; mancata dotazione 3.000-18.000;
  locazione 300-1.800; annuncio 500-3.000).
- **Richiamati** (non riprodotti): decreti attuativi (**DM 26 giugno 2015** Linee guida APE;
  metodologie **ex art. 4**), **DPR 74/2013** e **DPR 75/2013**, **DPR 445/2000** (artt. 47, 71, 76).

Dettaglio in `references/sources.yaml`, `references/fonti/dlgs-192-2005-artt-6-15.md`,
`references/estratti/ape-checklist.md`.

## Avvertenza

Skill di **supporto documentale**: la **redazione**, il **calcolo** e la **certificazione**
dell'APE restano del **tecnico abilitato**, e l'irrogazione delle sanzioni delle **autorita'
competenti** (regioni/comuni), sul testo vigente del D.Lgs. 192/2005 e sui decreti attuativi. La
skill **non sostituisce** tali soggetti ne' la lettura degli artt. 6/15 e delle Linee guida APE.
