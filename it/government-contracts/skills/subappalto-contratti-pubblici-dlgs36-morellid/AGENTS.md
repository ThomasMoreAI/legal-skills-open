# AGENTS.md - subappalto-contratti-pubblici-dlgs36

> Convenzioni di dominio per agent che lavorano su questa skill. Per le
> convenzioni globali del repo vedi `../../AGENTS.md`.

## Dominio

Supporto documentale alla **disciplina del subappalto** nei **contratti pubblici**: nozione e
soglie, attivita' non configuranti subappalto, condizioni di affidamento, trasmissione del
contratto, responsabilita' solidale, pagamento diretto al subappaltatore, autorizzazione della
stazione appaltante e subappalto a cascata, secondo l'**art. 119 del D.Lgs. 31 marzo 2023, n.
36**. Target: ingegneri, RUP, operatori di stazione appaltante, operatori economici.

**E' una skill documentale**: inquadra l'istituto e i suoi adempimenti; **non rilascia**
l'autorizzazione, **non verifica** i requisiti del subappaltatore, non sostituisce la stazione
appaltante ne' il RUP.

## Nota sull'area e sulla complementarita'

Area **appalti-opere-pubbliche**. Complementare a `bandi-tipo-anac-checker`,
`oepv-valutatore-offerte-tecniche` e `specifiche-tecniche-ict-appalti-dlgs36` (fase di gara):
questa copre l'**istituto del subappalto** in fase esecutiva.

## Fonti autoritative

Catalogata in `references/sources.yaml`:

- **dlgs-36-2023-art119**: D.Lgs. 31 marzo 2023, n. 36, pagina indice Normattiva pinnata a
  `!vig=2026-07-16` (hash `8d14a74f...`; codice 23G00044). Art. 119 (versione 2, idGruppo 18)
  caricato via `caricaArticolo` e trascritto verbatim.

Trascrizione in `references/fonti/dlgs-36-2023-art119.md`; estratto operativo in
`references/estratti/subappalto-checklist.md`.

## Punti chiave (verificati sul testo)

- **Nozione e soglie** (c. 2): parte delle prestazioni con organizzazione di mezzi e rischi;
  per i lavori, soglia **> 2%** delle prestazioni affidate **o > 100.000 euro** con
  **manodopera > 50%**.
- **Non e' subappalto** (c. 3): attivita' accessorie a lavoratori autonomi, subfornitura a
  catalogo di prodotti informatici, servizi < 20.000 euro/anno a imprenditori agricoli in
  comuni montani/isole minori, contratti continuativi di cooperazione anteriori alla procedura.
- **Condizioni** (c. 4): qualificazione, assenza cause di esclusione, indicazione in offerta.
- **Trasmissione** (c. 5): almeno **20 giorni prima** dell'inizio.
- **Responsabilita' solidale** (c. 6-7); **pagamento diretto** (c. 11: microimpresa/piccola
  impresa, inadempimento, richiesta del subcontraente); **tutele e CCNL** (c. 12).
- **Autorizzazione** (c. 16): **30 giorni**, silenzio-assenso; termini **dimezzati** sotto
  soglia (< 2% o < 100.000 euro). **Subappalto a cascata** (c. 17).

## Convenzioni specifiche

### Cosa NON fare
- Non **rilasciare l'autorizzazione** ne' verificare i requisiti/qualificazione del
  subappaltatore.
- Non riprodurre gli **articoli richiamati** (100, 103, 11, 120, allegato II.2-bis, cause di
  esclusione): rinviarvi.
- Non trattare la **fase di gara** ne' altri istituti (avvalimento) se non nei richiami dell'art. 119.

### Cosa fare
- Qualificare l'affidamento (subappalto / sub-contratto da comunicare / non subappalto) sulle
  soglie del comma 2-3; impostare condizioni, trasmissione, autorizzazione, responsabilita' e
  pagamento diretto.

## Aggiornamento delle fonti

Normattiva: riscaricare l'indice del D.Lgs. 36/2023 pinnato a nuovo `!vig=` (nuovo hash) e
rileggere l'art. 119, verificando le modifiche dei **decreti correttivi** (es. D.Lgs.
209/2024) segnalate nel testo dai doppi tondi `(( ))`.

## Validatori

- Non ancora assegnato (Livello 2 con esperto di contrattualistica pubblica / RUP).

## Stato attuale

- Versione: 0.1.0-alpha (closes #265)
- Task files: 2 (`qualifica-subappalto.md`, `imposta-autorizzazione-subappalto.md`)
- Esempi: 2 (nolo a caldo sotto soglia non-subappalto; subappalto di lavorazioni con pagamento diretto a PMI)
