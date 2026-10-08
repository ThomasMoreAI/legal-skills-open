# AGENTS.md - espropriazione-pubblica-utilita-dpr327

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **procedimento di espropriazione per pubblica utilità**: fasi e presupposti,
dichiarazione di pubblica utilità, determinazione dell'indennità (provvisoria/urgente), occupazione
d'urgenza, decreto di esproprio e acquisizione sanante, secondo il **D.P.R. 8 giugno 2001, n. 327**
(artt. 8, 12, 20, 22, 22-bis, 23, 42-bis). Target: ingegneri, tecnici stimatori, enti/autorità
espropriante, legali.

**È una skill documentale**: inquadra fasi/presupposti/termini; **non calcola** l'indennità, **non
redige** gli atti/il decreto, non sostituisce l'autorità espropriante, il promotore, il tecnico
stimatore o il legale.

## Nota sull'area

Area **appalti-opere-pubbliche**. Complementare e distinta dalle skill di gara/progettazione
(`bandi-tipo-anac-checker`, `oepv-valutatore-offerte-tecniche`, `pfte-allegato-i7-checker`,
`specifiche-tecniche-ict-appalti-dlgs36`): questa copre l'**esproprio** in fase attuativa dell'opera.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dpr-327-2001-artt-8-12-20-22-22bis-23-42bis**: D.P.R. 8 giugno 2001, n. 327, pagina indice
  Normattiva pinnata a `!vig=2026-07-17` (hash `b52bf6e1...`; codice 001G0372). Artt. 8, 12, 20, 22,
  22-bis, 23, 42-bis caricati via `caricaArticolo` e trascritti verbatim.

Trascrizione in `references/fonti/dpr-327-2001-artt-8-12-20-22-22bis-23-42bis.md`; estratto operativo
in `references/estratti/espropriazione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Presupposti del decreto** (art. 8): vincolo preordinato + dichiarazione di pubblica utilità +
  indennità (anche provvisoria).
- **Dichiarazione di pubblica utilità** (art. 12): approvazione del progetto definitivo/piani;
  equivalenze; efficacia.
- **Indennità**: provvisoria (art. 20: 30 gg, offerta, condivisione irrevocabile, acconto 80%,
  deposito Cassa DD.PP.); urgente (art. 22: casi L. 443/2001, > 50 destinatari, 60 gg).
- **Occupazione d'urgenza** (art. 22-bis): decreto motivato, immissione in possesso entro 3 mesi
  (perentorio), indennità di occupazione, decadenza.
- **Decreto di esproprio** (art. 23): elementi a-h, passaggio di proprietà sotto condizione, notifica
  7 gg prima, trascrizione, pubblicazione, opposizione del terzo (30 gg).
- **Acquisizione sanante** (art. 42-bis): indennizzo (valore venale + 10%/20% forfait), Corte dei conti.

## Convenzioni specifiche

### Cosa NON fare
- Non **calcolare** l'indennità (criteri di stima artt. 37/40/45): rinviarvi.
- Non **redigere** gli atti (dichiarazione di pubblica utilità, decreto di indennità, decreto di
  esproprio) né eseguire notifiche/trascrizioni.
- Non inventare **termini/percentuali** (usare 30/60 gg, 3 mesi, 7 gg, 80%, 10%/20% come da testo).

### Cosa fare
- **Ricostruire** le fasi e i presupposti; **verificare** la struttura del decreto; **inquadrare**
  l'acquisizione sanante, con rinvio agli articoli sulla stima.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.P.R. 327/2001 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
gli artt. 8, 12, 20, 22, 22-bis, 23, 42-bis (testo tra `(( ))`).

## Validatori

- Non ancora assegnato (Livello 2 con tecnico/ufficio espropri o legale amministrativista).

## Stato attuale

- Versione: 0.1.0-alpha
- Task files: 2 (`inquadra-fasi-esproprio.md`, `verifica-decreto-esproprio.md`)
- Esempi: 2 (dalla pubblica utilità al decreto; occupazione d'urgenza art. 22-bis)
