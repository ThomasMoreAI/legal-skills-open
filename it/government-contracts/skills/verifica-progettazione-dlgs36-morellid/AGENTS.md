# AGENTS.md - verifica-progettazione-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale al **RUP** (responsabile unico del progetto), al **soggetto verificatore** e al
**progettista** per la **verifica della progettazione** e la **validazione** del progetto posto a base
di gara nei contratti pubblici di lavori, ai sensi del **D.Lgs. 31 marzo 2023, n. 36 (Codice dei
contratti pubblici), art. 42**. Target: RUP, uffici tecnici, organismi di verifica, progettisti.

**E' una skill documentale per il tecnico**: inquadra oggetto, tempi, soggetti ed effetti della
verifica/validazione; **non esegue** la verifica, **non redige** il rapporto di verifica ne' l'atto di
validazione.

## Nota sull'area e sulla complementarita'

Area **appalti-opere-pubbliche**. Distinta da `collaudo-verifica-conformita-dlgs36` (verifica di
conformita'/collaudo in **fase di esecuzione**) e da `pfte-allegato-i7-checker` (contenuti del **PFTE**,
art. 41 e Allegato I.7): questa copre la **verifica preventiva della progettazione** (art. 42).
Complementare a `rup-responsabile-unico-progetto-dlgs36`, a `direzione-lavori-esecuzione-dlgs36` e alle
skill DPR 380 sul deposito sismico (assolto dalla verifica positiva, art. 42 c. 3).

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-art-42**: D.Lgs. 36/2023, pagina indice Normattiva pinnata a `!vig=2026-07-17` (hash
  `0e9a1938...`; codice 23G00044, idGruppo 5). Art. 42 (versione 1) caricato via `caricaArticolo`
  (formato AKN) e trascritto verbatim.

Trascrizione in `references/fonti/dlgs-36-2023-art-42.md`; estratto operativo in
`references/estratti/verifica-progettazione-checklist.md`.

## Punti chiave (verificati sul testo)

- **Oggetto** (c. 1): rispondenza al **documento d'indirizzo (DIP)** + **conformita' alla normativa**;
  verifica durante lo sviluppo, per livello. Congiunto/PPP: PFTE prima dell'affidamento, esecutivo prima
  dell'inizio lavori.
- **RUP e incompatibilita'** (c. 2): verifica diretta o seguita col **contraddittorio**;
  **incompatibile** con progettazione, coordinamento sicurezza, DL e collaudo.
- **Effetti** (c. 3): la verifica positiva **assolve** deposito/autorizzazione **sismica** e **denuncia
  al genio civile**; deposito nell'**Archivio informatico nazionale delle opere pubbliche**.
- **Validazione** (c. 4): atto formale del **RUP**, riferito al rapporto e alle controdeduzioni; estremi
  nel **bando/lettera d'invito**.
- **Allegato I.7** (c. 5): contenuti, modalita' e **soggetti** della verifica (per importo); oneri nelle
  risorse dell'opera.

## Convenzioni specifiche

### Cosa NON fare
- Non **eseguire** la verifica ne' **redigere** il **rapporto di verifica** o l'**atto di validazione**.
- Non riprodurre l'**Allegato I.7** (soglie di importo e soggetti verificatori) ne' gli **obblighi
  sismici** del DPR 380: rinvio.
- Non confondere la **verifica preventiva della progettazione** (art. 42) con la **verifica di
  conformita'/collaudo in esecuzione** (skill dedicata).

### Cosa fare
- Inquadrare oggetto, tempi e soggetti (cc. 1-2), effetti della verifica positiva e validazione (cc.
  3-4), rinvio all'Allegato I.7 (c. 5).

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 36/2023 pinnato a nuovo `!vig=` (nuovo hash) e rileggere
l'art. 42, verificando le modifiche dei doppi tondi `(( ))` (es. correttivo D.Lgs. 209/2024) e
l'aggiornamento dell'Allegato I.7.

## Validatori

- Non ancora assegnato (Livello 2 con RUP/esperto di verifica progetti).

## Stato attuale

- Versione: 0.1.0-alpha (closes #362)
- Task files: 2 (`inquadra-verifica-progetto.md`, `inquadra-validazione-effetti.md`)
- Esempi: 2 (appalto integrato: tempi e soggetti; verifica positiva: effetti sismici e validazione)
