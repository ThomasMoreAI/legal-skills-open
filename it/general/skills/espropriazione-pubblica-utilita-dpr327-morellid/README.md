# espropriazione-pubblica-utilita-dpr327

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con tecnico/ufficio espropri o legale amministrativista da completare)

Skill di **supporto documentale** al **procedimento di espropriazione per pubblica utilità**: fasi e
presupposti, dichiarazione di pubblica utilità, determinazione dell'indennità (provvisoria/urgente),
occupazione d'urgenza, decreto di esproprio e acquisizione sanante, secondo il **D.P.R. 8 giugno
2001, n. 327** (T.U. espropriazione), artt. 8, 12, 20, 22, 22-bis, 23, 42-bis.

**Non calcola** l'indennità, **non redige** gli atti/il decreto e **non sostituisce** l'autorità
espropriante, il promotore, il tecnico stimatore o il legale: inquadra fasi, presupposti e termini.

## Target

Ingegneri, tecnici stimatori, enti/autorità espropriante e legali coinvolti in procedure espropriative.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `inquadra-fasi-esproprio` | Verifica presupposti del decreto (art. 8), dichiarazione di pubblica utilità (art. 12) e la fase di indennità applicabile (artt. 20/22/22-bis) |
| `verifica-decreto-esproprio` | Controlla contenuto ed effetti del decreto di esproprio (art. 23) e inquadra l'acquisizione sanante (art. 42-bis) |

Nucleo: **fasi/presupposti** (art. 8); **dichiarazione di pubblica utilità** (art. 12); **indennità**
provvisoria (art. 20) e urgente (art. 22); **occupazione d'urgenza** (art. 22-bis); **decreto di
esproprio** (art. 23); **acquisizione sanante** (art. 42-bis).

## Fonti consultate

- **D.P.R. 8 giugno 2001, n. 327** - artt. 8, 12, 20, 22, 22-bis, 23, 42-bis - testo vigente su
  Normattiva (indice pinnato a `!vig=2026-07-17`, codice 001G0372)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non calcola** l'indennità (criteri di stima: valore venale, aree edificabili/agricole - artt.
  37, 40, 45): rinvio agli articoli sulla stima.
- **Non redige** gli atti (dichiarazione di pubblica utilità, decreto di indennità, decreto di
  esproprio) né esegue notifiche/trascrizioni.
- **Non sostituisce** l'autorità espropriante, il promotore, il tecnico stimatore o il legale; non
  tratta il contenzioso (opposizione alla stima, ricorsi).

**La skill è un supporto documentale: non sostituisce l'autorità espropriante, il tecnico stimatore
né il legale, né la lettura del D.P.R. 327/2001 e dei criteri di stima richiamati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
