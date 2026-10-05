# AGENTS.md - accertamento-tecnico-preventivo-cpc

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale all'**istruzione preventiva** nel processo civile: **accertamento tecnico
preventivo / ispezione giudiziale** (art. 696 c.p.c.) e **consulenza tecnica preventiva ai fini
della composizione della lite** (art. 696-bis c.p.c.). Target: ingegneri che operano come CTU,
avvocati, parti.

**E' una skill documentale**: inquadra strumenti, presupposti e procedimento; **non instaura**
il procedimento, **non redige** ricorso/relazione, non sostituisce giudice, avvocato ne' CTU.

## Nota sull'area e sulla complementarita'

Area **forense**. Complementare e distinta da `relazione-peritale-ctu-cpc` (relazione del CTU
nel merito, artt. 191-201) e `compensi-ctu-dpr115` (liquidazione compensi): questa copre la
fase **preventiva** (ATP e ATP conciliativo). Fa crescere l'area forense (intento in `areas.yaml`).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **cpc-696-696bis**: Codice di procedura civile (R.D. 1443/1940), pagina indice Normattiva
  pinnata a `!vig=2026-07-16` (hash `7a53e745...`; codice 040U1443). Artt. 696 (idSottoArticolo
  1, versione 7) e 696-bis (idSottoArticolo 2, versione 3), idGruppo=118, caricati via
  `caricaArticolo` e trascritti verbatim. Stesso atto usato da `relazione-peritale-ctu-cpc`.

Trascrizione in `references/fonti/cpc-696-696bis.md`; estratto operativo in
`references/estratti/atp-checklist.md`.

## Punti chiave (verificati sul testo)

- **Art. 696**: ATP/ispezione giudiziale su **urgenza** di verificare stato di luoghi/qualita'
  di cose; estensione a **cause e danni** (c. 2); nomina CTU (c. 3); **sospensione** fino al
  deposito CTU, **non oltre 6 mesi** (c. 4); definizione con deposito e liquidazione (c. 5).
- **Art. 696-bis**: consulenza tecnica preventiva **anche fuori urgenza** per crediti da
  inadempimento/fatto illecito; **tentativo di conciliazione** del consulente; **verbale** con
  **efficacia di titolo esecutivo** esente da imposta di registro; acquisizione della relazione
  nel merito; richiamo **artt. 191-197**.

## Convenzioni specifiche

### Cosa NON fare
- Non **instaurare il procedimento** ne' redigere ricorso/relazione.
- Non riprodurre gli **articoli richiamati** (692-695, 191-197): rinviarvi.
- Non fornire il **contenuto tecnico/di merito** della consulenza (cfr. `relazione-peritale-ctu-cpc`).

### Cosa fare
- Aiutare a **scegliere** tra art. 696 e 696-bis su urgenza/finalita' e a **inquadrare**
  procedimento, sospensione, conciliazione ed efficacia del verbale/relazione.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del c.p.c. pinnato a nuovo `!vig=` (nuovo hash) e rileggere
artt. 696/696-bis, verificando le modifiche (es. riforma Cartabia D.Lgs. 149/2022, segnalata
dai doppi tondi `(( ))`).

## Validatori

- Non ancora assegnato (Livello 2 con avvocato/magistrato o CTU esperto di istruzione preventiva).

## Stato attuale

- Versione: 0.1.0-alpha (closes #269)
- Task files: 2 (`scegli-strumento-preventivo.md`, `imposta-procedimento-atp.md`)
- Esempi: 2 (infiltrazioni: ATP conservativo art. 696; difetti appalto: 696-bis conciliativo)
