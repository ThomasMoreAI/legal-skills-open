# attestato-prestazione-energetica-dlgs192

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con certificatore energetico / esperto EPBD da completare)

Skill di **supporto documentale** agli **obblighi relativi all'attestato di prestazione
energetica (APE)**: quando è dovuto e chi lo produce, dotazione e consegna, clausola nel
contratto, annuncio commerciale, validità, affissione negli edifici pubblici e sanzioni, secondo
gli **artt. 6 e 15 del D.Lgs. 19 agosto 2005, n. 192**.

**Non calcola, non redige e non certifica** l'APE (attività del tecnico abilitato) e **non
applica** le sanzioni: inquadra obblighi, soggetti e sanzioni.

## Target

Ingegneri, tecnici, proprietari e agenzie che devono gestire gli obblighi APE in una
compravendita, locazione o per un nuovo edificio.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `verifica-obbligo-ape` | Stabilisce se l'APE è dovuto (nuovo edificio, vendita, locazione), chi lo produce e i tempi/adempimenti (dotazione, consegna, clausola, annuncio) |
| `inquadra-sanzioni-ape` | Individua la sanzione applicabile (art. 6 c. 3 e art. 15) per mancata dotazione, omessa clausola/allegazione o annuncio senza parametri |

Nucleo: **quando serve l'APE** e **chi lo produce** (art. 6 c. 1-2), **clausola/allegazione** con
sanzioni (c. 3: 3.000-18.000 €; locazione singole 1.000-4.000 €), **validità 10 anni** (c. 5),
**affissione** edifici PA > 500 (poi 250) m² (c. 6-7), **annuncio** con indici e classe (c. 8), e
le **sanzioni** dell'art. 15 (professionista 700-4200 €; mancata dotazione 3.000-18.000 €;
locazione 300-1.800 €; annuncio 500-3.000 €).

## Fonti consultate

- **D.Lgs. 19 agosto 2005, n. 192** - artt. 6 e 15 - testo vigente su Normattiva (indice pinnato
  a `!vig=2026-07-16`, codice 005G0219)
- Decreti attuativi (**DM 26 giugno 2015** - Linee guida APE; metodologie ex art. 4) e **DPR
  74/2013**, **DPR 75/2013** - citati

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola/redige/certifica** l'APE né riproduce le metodologie/modelli (DM 26/6/2015,
  UNI/TS 11300): rinvio ai decreti.
- **Non applica** le sanzioni (autorità competenti: regioni/comuni).
- **Non tratta** i requisiti minimi di progetto (art. 3-4) né la relazione tecnica (art. 8) se
  non come richiamo.

**La skill è un supporto documentale: non sostituisce il tecnico abilitato né l'autorità
competente, né la lettura degli artt. 6/15 del D.Lgs. 192/2005 e delle Linee guida APE.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
