# verifica-progettazione-dlgs36

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con RUP / esperto di verifica progetti da completare)

Skill di **supporto documentale** al **RUP** (responsabile unico del progetto), al **soggetto
verificatore** e al **progettista** per la **verifica della progettazione** e la **validazione** del
progetto posto a base di gara nei contratti pubblici di lavori, ai sensi del **D.Lgs. 31 marzo 2023, n.
36 (Codice dei contratti pubblici), art. 42**.

**Non esegue** la verifica, **non redige** il rapporto di verifica né l'atto di validazione e **non
sostituisce** il RUP, il soggetto verificatore o il progettista: inquadra oggetto, tempi, soggetti ed
effetti.

## Target

RUP, uffici tecnici, organismi/soggetti di verifica e progettisti che devono inquadrare la verifica
della progettazione e la validazione del progetto.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-verifica-progetto` | Oggetto e tempi della verifica per livello, ruolo del RUP e incompatibilità (art. 42 cc. 1-2) |
| `inquadra-validazione-effetti` | Effetti della verifica positiva (deposito sismico, Archivio OO.PP.) e validazione a base di gara (art. 42 cc. 3-5) |

Nucleo: **oggetto** (rispondenza al DIP + conformità normativa) e **tempi** per livello (art. 42 c. 1),
**RUP e incompatibilità** (c. 2), **effetti** con assolvimento sismico e Archivio OO.PP. (c. 3),
**validazione** con estremi nel bando (c. 4), rinvio all'**Allegato I.7** (c. 5).

## Fonti consultate

- **D.Lgs. 31 marzo 2023, n. 36** (Codice dei contratti pubblici) - art. 42 - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 23G00044, idGruppo 5).

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non esegue** la verifica né redige il rapporto di verifica o l'atto di validazione.
- **Non riproduce** l'Allegato I.7 (soglie di importo e soggetti verificatori) né gli obblighi sismici
  del DPR 380.
- **Non tratta** la verifica di conformità/collaudo in esecuzione (skill
  `collaudo-verifica-conformita-dlgs36`) né i contenuti del PFTE (skill `pfte-allegato-i7-checker`) se
  non nei richiami.

**La skill è un supporto documentale: non sostituisce il RUP, il soggetto verificatore o il progettista,
né la lettura dell'art. 42 del D.Lgs. 36/2023 e dell'Allegato I.7.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
