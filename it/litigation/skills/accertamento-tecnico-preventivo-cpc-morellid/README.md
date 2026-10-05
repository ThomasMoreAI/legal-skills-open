# accertamento-tecnico-preventivo-cpc

> Versione: 0.1.0-alpha | Stato: in sviluppo (validazione Livello 1; Livello 2 con avvocato/magistrato o CTU esperto di istruzione preventiva da completare)

Skill di **supporto documentale** all'**istruzione preventiva** nel processo civile:
**accertamento tecnico preventivo / ispezione giudiziale** (art. 696) e **consulenza tecnica
preventiva ai fini della composizione della lite** (art. 696-bis), secondo il **Codice di
procedura civile**.

**Non instaura il procedimento**, **non redige** il ricorso né la relazione e **non
sostituisce** il giudice, l'avvocato né il CTU: inquadra strumenti, presupposti e procedimento.

## Target

Ingegneri che operano (o stanno per operare) come **CTU**, avvocati e parti che devono
inquadrare un ATP o la consulenza tecnica preventiva conciliativa.

## Cosa fa

| Sotto-attività | Descrizione |
|---|---|
| `scegli-strumento-preventivo` | Aiuta a scegliere tra ATP/ispezione giudiziale (art. 696) e consulenza tecnica preventiva conciliativa (art. 696-bis) in base a urgenza e finalità |
| `imposta-procedimento-atp` | Inquadra procedimento, sospensione (6 mesi), tentativo di conciliazione ed efficacia del verbale/relazione |

Nucleo: **art. 696** (ATP/ispezione su urgenza, estensione a cause e danni, nomina CTU,
sospensione fino al deposito CTU non oltre 6 mesi, liquidazione) e **art. 696-bis** (consulenza
tecnica preventiva conciliativa anche fuori urgenza, tentativo di conciliazione, verbale con
**efficacia di titolo esecutivo** esente da imposta di registro, acquisizione della relazione
nel merito, richiamo artt. 191-197).

## Fonti consultate

- **Codice di procedura civile (R.D. 28 ottobre 1940, n. 1443)** - artt. 696 e 696-bis - testo
  vigente su Normattiva (indice pinnato a `!vig=2026-07-16`, codice 040U1443)

Dettaglio in `references/sources.yaml`, `references/fonti/`, `references/estratti/`.

## Limiti noti

- **Non instaura il procedimento** né redige il ricorso/relazione.
- **Non fornisce il contenuto tecnico/di merito** della consulenza (→ `relazione-peritale-ctu-cpc`).
- **Non sostituisce** il giudice, l'avvocato né il CTU; non riproduce gli articoli richiamati
  (692-695, 191-197).

**La skill è un supporto documentale: non sostituisce il giudice, l'avvocato né il CTU, né la
lettura degli artt. 696/696-bis del c.p.c. e degli articoli richiamati.**

## Changelog

Vedi [`CHANGELOG.md`](CHANGELOG.md).
