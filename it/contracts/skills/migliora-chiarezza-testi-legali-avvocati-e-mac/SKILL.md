---
name: migliora-chiarezza-testi-legali-avvocati-e-mac
title: Migliora chiarezza testi legali — metodo Garner
description: 'Migliora la chiarezza, la leggibilità e la precisione di contratti, clausole, pareri legali e atti giudiziari in italiano, riducendo ambiguità, formule inutili e strutture sintattiche opache. La skill usa il metodo di Bryan Garner sul plain language legale, adattato al contesto giuridico italiano. MANDATORY TRIGGERS: redazione o revisione di un contratto, di una clausola contrattuale, di un parere legale scritto per un cliente, di un atto giudiziario (citazione, comparsa, memoria, appello, ricorso) o di un atto normativo/amministrativo in italiano, quando l''obiettivo esplicito o implicito include la chiarezza, la leggibilità o la riduzione dell''ambiguità del testo.'
author: avvocati-e-mac
author_url: https://github.com/avvocati-e-mac/skill-legali/tree/main/migliora-chiarezza-testi-legali/migliora-chiarezza-testi-legali
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: contracts
language: it
sources:
- title: Bibliografia
  path: references/bibliografia.md
- title: Esempi Atti Giudiziari
  path: references/esempi-atti-giudiziari.md
- title: Interpretazione Civilistica
  path: references/interpretazione-civilistica.md
- title: Principi Garner
  path: references/principi-garner.md
- title: Tradizione Italiana
  path: references/tradizione-italiana.md
---

# Migliora chiarezza testi legali — metodo Garner

Skill generale, riutilizzabile su qualsiasi contratto, parere o atto legale
in italiano. Non è specifica a un singolo cliente, materia o fascicolo.

## Compatibilità runtime

Questa skill deve funzionare sia in ambienti Claude sia in ambienti
OpenAI/Codex.

- **Se stai operando in Claude Desktop, Claude for Work/Cowork o Claude
  Code:** usa le skill, i tool, i subagenti e i file di riferimento
  disponibili nell'ambiente Claude. Se non puoi leggere direttamente i
  documenti o i reference, chiedi all'utente di fornirli.
- **Se stai operando in Codex o in un ambiente OpenAI:** usa i tool MCP,
  shell, browser o subagenti disponibili nell'ambiente corrente, rispettando
  le regole di accesso ai file e ai permessi del runtime. Leggi i file in
  `references/` solo quando il caso li richiede.
- **Se uno strumento non è disponibile nel runtime corrente:** non inventare
  un equivalente. Usa il fallback documentato in questa skill oppure chiedi
  conferma all'utente.

## Principio di fondo

L'ambiguità in un testo legale è quasi sempre un difetto di progettazione
del testo, non una caratteristica ineliminabile del linguaggio giuridico:
frasi sovraccariche, condizioni nascoste, terminologia incoerente e formule
arcaiche creano contenzioso interpretativo evitabile. Il testo va scritto
per chi lo dovrà leggere e applicare (cliente, controparte, giudice), non
per dimostrare gravità professionale.

## Come applicare la skill

1. **Leggi** l'intero testo (contratto, clausola, parere o atto) prima di
   intervenire riga per riga.
2. **Applica la checklist rapida** qui sotto e segna ogni criticità
   trovata.
3. Per **ogni criticità**, produci sempre una coppia PRIMA/DOPO più una
   motivazione in una riga — mai solo un'osservazione astratta ("è poco
   chiaro"). Vedi gli esempi sotto per il formato atteso.
4. Se il testo è un **contratto**, verifica le clausole più critiche
   (responsabilità, garanzie, standard di comportamento) contro i criteri
   di interpretazione degli artt. 1362-1371 c.c.: se una clausola si
   presta a più letture secondo quei criteri, va riscritta ora, non
   lasciata all'interpretazione futura di un giudice — vedi
   `references/interpretazione-civilistica.md`.
   Se il testo è un **atto giudiziario**, apri sempre
   `references/esempi-atti-giudiziari.md`: contiene un vincolo normativo
   cogente (D.M. 110/2023) di cui tenere conto, non solo principi
   stilistici facoltativi.
5. **Consegna un output finale** con il testo riscritto e un sommario
   sintetico delle modifiche principali (non serve annotare ogni virgola).

## Esempi (formato atteso)

**Diffida — soggetto nascosto e subordinate annidate**
PRIMA: "In difetto l'eventuale blocco della produzione della società, in
quanto non rispetta le normativa HACCP e quindi con il rischio che la
relativa licenza sia revocata, qualora l'AUSL di Modena provveda ad
ulteriori verifiche, sarà da imputare alla Vostra negligenza."
DOPO: "Se la Vostra società non rispetta le normative HACCP e l'AUSL di
Modena effettua ulteriori verifiche, la licenza potrebbe essere revocata e
la produzione bloccata. La responsabilità di questo blocco sarà interamente
Vostra."
Motivo: frase unica con soggetto nascosto e subordinate annidate → sequenza
di frasi brevi, soggetto esplicito, nesso causale lineare.

**Clausola contrattuale — standard vago e avverbio superfluo**
PRIMA: "Il Noleggiatore garantisce che l'automezzo è conforme alle
normative vigenti, inclusa la normativa ATP, e che l'impianto refrigerante
è perfettamente funzionante."
DOPO: "L'automezzo rispetta le normative vigenti, inclusa la normativa ATP.
L'impianto refrigerante funziona correttamente e mantiene le temperature
dichiarate nella certificazione ATP."
Motivo: elimina l'avverbio superfluo ("perfettamente") e sostituisce una
valutazione soggettiva con un parametro verificabile — riduce l'ambiguità e
il contenzioso interpretativo.

Altri esempi (clausole di responsabilità, atti giudiziari, ridondanze
lessicali, deep issue, throat-clearing) sono in
`references/principi-garner.md` e `references/esempi-atti-giudiziari.md` —
apri quei file quando serve un esempio più vicino al testo che stai
revisionando.

## Checklist rapida

1. Ogni termine tecnico ricorrente è definito una volta sola ed è usato
   sempre nella stessa forma? Elimina le varianti sinonimiche.
2. Ogni clausola/periodo ha una sola idea principale? Spezza le frasi con
   più condizioni annidate.
3. Le condizioni e le eccezioni sono collocate accanto a ciò che
   modificano, senza ambiguità di riferimento? Se ce n'è più di una nella
   stessa clausola, ordinale dalla più generale alla più specifica.
4. Le clausole comparabili (obblighi, diritti, eccezioni dello stesso
   tipo) sono scritte con la stessa struttura sintattica in tutto il
   documento? Le eccezioni sono raggruppate in una sezione dedicata,
   invece di alternarsi disordinatamente alle regole?
5. Sono state eliminate le doppiette/triplette ridondanti, le
   nominalizzazioni verbose (es. "si obbliga a utilizzare" → "utilizza")
   e le formule di "riscaldamento" prive di contenuto (es. "si fa
   presente che", "è importante notare che")?
6. Il verbo modale usato per gli obblighi è coerente in tutto il testo
   (niente alternanza immotivata "dovrà"/"è tenuto a"/"provvede a")?
7. Ogni sezione/clausola/paragrafo dichiara subito la sua funzione
   (issue-first) invece di richiederne la lettura integrale per capirne lo
   scopo? Negli atti giudiziari e nei pareri: il concetto centrale precede
   la citazione di giurisprudenza, non viceversa.
8. Ci sono standard vaghi non definiti ("normale deperimento d'uso", "uso
   improprio", "massima diligenza")? Sostituiscili con parametri oggettivi
   o criteri verificabili.
9. La forma passiva nasconde chi esercita un potere o una discrezionalità
   (es. "il canone potrà essere aumentato")? Riscrivi in forma attiva
   indicando chi decide e a quali condizioni.
10. Applicando i criteri ermeneutici degli artt. 1362-1371 c.c. alla
    clausola, emergono letture alternative plausibili? Se sì, riscrivere
    prima della firma — vedi `references/interpretazione-civilistica.md`.
11. Date, importi e riferimenti normativi sono completi (nessun campo in
    bianco, nessun rinvio "mobile" indeterminato senza valore di default)?

## File di approfondimento (references/)

Ogni file va aperto solo quando il tipo di documento in lavorazione lo
richiede — non aprirli "di routine" per ogni clausola:

- **references/principi-garner.md** — i principi di Garner per esteso
  (definizioni, sintassi, lessico, struttura), ciascuno con più esempi
  prima/dopo, inclusi esempi da atti giudiziari e da un secondo dominio
  contrattuale (prestazione d'opera). Apri quando vuoi il ragionamento
  completo dietro una voce della checklist o cerchi altri esempi oltre a
  quelli già in questo file.
- **references/esempi-atti-giudiziari.md** — apri **sempre** quando il
  testo da revisionare è un atto giudiziario (citazione, comparsa,
  memoria, appello, ricorso): contiene il vincolo normativo del D.M.
  110/2023 (limiti dimensionali, struttura obbligatoria) oltre a esempi
  prima/dopo specifici per il contenzioso.
- **references/interpretazione-civilistica.md** — apri quando il punto 10
  della checklist segnala un dubbio, o serve giustificare la riscrittura
  di una clausola con un riferimento normativo/giurisprudenziale.
- **references/tradizione-italiana.md** — apri solo se l'utente chiede
  esplicitamente fonti/riferimenti italiani, o se stai scrivendo un parere
  che cita fonti di supporto (per non inventare o sovrastimare un "Garner
  italiano" inesistente di tua iniziativa).
- **references/bibliografia.md** — apri quando l'utente chiede i
  riferimenti bibliografici completi per approfondire di persona un
  autore o un testo citato in una delle altre reference.
