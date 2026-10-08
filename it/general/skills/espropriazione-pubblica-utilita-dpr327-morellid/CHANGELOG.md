# CHANGELOG - espropriazione-pubblica-utilita-dpr327

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-17

### Added (closes #285)
- Prima versione della skill di supporto al **procedimento di espropriazione per pubblica utilità**,
  ai sensi del **D.P.R. 8 giugno 2001, n. 327** (artt. 8, 12, 20, 22, 22-bis, 23, 42-bis), nell'area
  `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 8 giugno 2001, n. 327** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: b52bf6e1a58840619595d43710b82ec72f45c8d01bf33f7cc26540fdbfbf4abd
    (codice 001G0372). Artt. 8, 12, 20, 22, 22-bis, 23, 42-bis via `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dpr-327-2001-artt-8-12-20-22-22bis-23-42bis.md`.
- Estratto operativo `references/estratti/espropriazione-checklist.md`.
- Due task: `inquadra-fasi-esproprio.md` e `verifica-decreto-esproprio.md`.
- Due esempi: dalla dichiarazione di pubblica utilità al decreto (artt. 8, 12, 20, 23); occupazione
  d'urgenza preordinata all'esproprio (art. 22-bis).

### Contenuto ancorato al testo
- Art. 8 fasi/presupposti (vincolo + pubblica utilità + indennità); art. 12 atti che comportano la
  dichiarazione di pubblica utilità; art. 20 indennità provvisoria (30 gg, offerta, condivisione
  irrevocabile, acconto 80%, deposito Cassa DD.PP.); art. 22 indennità urgente (L. 443/2001, > 50
  destinatari, 60 gg); art. 22-bis occupazione d'urgenza (immissione in possesso entro 3 mesi,
  indennità di occupazione, decadenza); art. 23 contenuto/effetti del decreto (a-h, notifica 7 gg
  prima, trascrizione, opposizione del terzo 30 gg); art. 42-bis acquisizione sanante (forfait
  10%/20%, Corte dei conti).

### Scope e limiti
- Non calcola l'indennità (criteri di stima artt. 37/40/45), non redige gli atti/il decreto, non
  esegue notifiche/trascrizioni, non sostituisce l'autorità espropriante, il promotore, il tecnico
  stimatore o il legale. Artt. 9-11, 13, 21, 24 citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.P.R. 327/2001 pinnato (nuovo hash) e
  verificare le modifiche (testo tra `(( ))`).
- Validazione Livello 2 con tecnico/ufficio espropri o legale amministrativista.
