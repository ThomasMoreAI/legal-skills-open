# AGENTS.md - distanze-legali-costruzioni-cc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alle **distanze legali nelle costruzioni** e alla disciplina delle **luci e
vedute** del **Codice civile** (artt. 873-907), di interesse per la progettazione edilizia e le
questioni di confine. Target: ingegneri, architetti, geometri, CTU.

**E' una skill documentale**: inquadra le distanze civilistiche (minimi) e il coordinamento con
l'urbanistica; **non risolve il caso concreto**, non misura in sito e non sostituisce il tecnico o
il consulente legale.

## Nota sull'area e sulla complementarita'

Area **edilizia-urbanistica-catasto**. Complementare a `modulistica-edilizia-unificata`,
`contributo-costruzione-dpr380` e (per le CTU) alle skill dell'area forense: questa copre le
**distanze civilistiche**. Le distanze del codice civile sono un **minimo derogabile in aumento**
dai regolamenti locali e vanno coordinate con il **DM 1444/1968 art. 9** (distanze tra pareti
finestrate), richiamato ma non riprodotto.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **codice-civile-distanze**: Codice civile (R.D. 262/1942), indice Normattiva pinnato
  `!vig=2026-07-16` (hash `39089217...`, codice 042U0262). Artt. 873, 877, 878, 879, 889, 890, 892,
  905, 906, 907 (testo vigente) via `caricaArticolo`, trascritti verbatim.

Trascrizione in `references/fonti/cc-distanze-873-907.md`; estratto in
`references/estratti/distanze-costruzioni-checklist.md`.

## Punti chiave (verificati sul testo)

- **Costruzioni** (art. 873): **3 m** (salvo regolamenti locali maggiori); muro di cinta <= 3 m non
  computato (art. 878); aderenza/confine (art. 877); esenzioni (art. 879).
- **Pozzi/fosse** (art. 889): **2 m**; **tubi**: **1 m**; depositi nocivi/pericolosi (art. 890).
- **Alberi** (art. 892): **3 / 1,5 / 0,5 m** (alto fusto / non alto fusto / viti-siepi-frutto),
  eccezioni 1 m ontano/castagno, 2 m robinie.
- **Vedute**: diretta **1,5 m** (art. 905); obliqua **0,75 m** (art. 906); costruzioni **3 m** dalle
  vedute acquisite (art. 907); distinzione luci/vedute (artt. 900-904).

## Convenzioni specifiche

### Cosa NON fare
- Non **presentare i minimi civilistici come esaustivi**: i regolamenti locali e il DM 1444/1968
  possono imporre distanze maggiori (spesso 10 m tra pareti finestrate). Non riprodurre le norme
  urbanistiche.
- Non **risolvere il caso concreto** (servitu', usucapione della veduta, prevenzione, comunione del
  muro): e' del consulente legale.

### Cosa fare
- Inquadrare le distanze civilistiche per ciascun elemento e rinviare al coordinamento urbanistico.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del Codice civile pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 873-907 (soggetti a rare modifiche); verificare l'evoluzione del coordinamento con il DM
1444/1968 e la giurisprudenza.

## Validatori

- Non ancora assegnato (Livello 2 con avvocato civilista / CTU esperto di distanze).

## Stato attuale

- Versione: 0.1.0-alpha (closes #261)
- Task files: 2 (`verifica-distanze-costruzioni.md`, `verifica-luci-vedute.md`)
- Esempi: 2 (nuova costruzione presso il confine; finestra e vedute)
