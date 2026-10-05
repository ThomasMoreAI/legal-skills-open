# compensi-ctu-dpr115

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con CTU/avvocato esperto di liquidazioni da completare)

Skill di **supporto documentale alla liquidazione dei compensi del CTU / ausiliario
del magistrato** ai sensi del **Testo Unico spese di giustizia (D.P.R. 115/2002,
Parte III)**.

**Non e' una skill di calcolo numerico**: inquadra spettanze, tipo di onorario e
aumenti/riduzioni; **non calcola gli importi** (le tabelle tariffarie sono nel DM
30/5/2002, delegato e non reperibile su Normattiva), non redige il decreto di
pagamento e non tratta il CTP di parte.

## Target

Ingegneri iscritti all'albo dei CTU e, in generale, ausiliari del magistrato.

## Cosa fa

| Sotto-attivita' | Descrizione |
|---|---|
| `inquadra-compenso` | Individua le spettanze (art. 49), il tipo di onorario (artt. 50-51) e gli aumenti/riduzioni applicabili (artt. 51-53) |
| `prepara-istanza-liquidazione` | Struttura l'istanza di liquidazione (onorario + indennita' + spese documentate) e richiama la procedura del decreto di pagamento e dell'opposizione (artt. 55-56, 168, 170) |

Nucleo: **spettanze** (art. 49), **tipo di onorario** (fisso/variabile/a tempo,
artt. 50-51), **aumenti/riduzioni** (urgenza 20%, fino al doppio, collegiale +40%,
artt. 51-53), **indennita'/spese** (artt. 55-56), **liquidazione e opposizione**
(artt. 168, 170).

## Fonti consultate

- **D.P.R. 30/5/2002 n. 115** (T.U. spese di giustizia), artt. 49-58, 168, 170 -
  testo vigente su Normattiva (pagina indice pinnata a `!vig=`)
- **DM 30/5/2002** (tabelle tariffarie) - **citato, non riprodotto** (non su
  Normattiva)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola gli importi** (vacazione, onorari, scaglioni %): tabelle nel **DM
  30/5/2002**, non reperibile su Normattiva
- Non redige il **decreto di pagamento** ne' l'opposizione
- Non tratta i compensi del **CTP** (di parte, a contratto)

**La skill e' un supporto documentale: non sostituisce il magistrato, il consulente
legale ne' la lettura delle tabelle del DM.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
