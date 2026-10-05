# CHANGELOG - compensi-ctu-dpr115

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0-alpha] - 2026-07-16

### Added (closes #42)
- Prima versione della skill di supporto documentale alla liquidazione dei compensi
  del CTU / ausiliario del magistrato (D.P.R. 115/2002, Parte III).
- Nuova **area di catalogo `forense`** (CTU & ingegneria forense) aggiunta ad
  `areas.yaml` su indicazione esplicita del maintainer (parte con 2 skill, #42 e
  #41, in deroga consapevole alla soglia di 3).
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.P.R. 30/5/2002 n. 115** - pagina indice Normattiva pinnata a `!vig=2026-07-16`
    SHA256: 8fc7d98b15951191c03aedf05cdb8de813819f2cd91d6f9f51511cc00580270a
    (riproducibile, doppio download). Artt. 49-58 (compensi, indennita', spese,
    adeguamento, custodia, commissario ad acta), 168 (decreto di pagamento) e 170
    (opposizione) letti via caricaArticolo e trascritti verbatim in
    `references/fonti/dpr-115-2002.md`.
- Estratto operativo `references/estratti/compensi-ctu-checklist.md`.
- Due task: `inquadra-compenso.md` e `prepara-istanza-liquidazione.md`.
- Due esempi: onorario a tempo (vacazioni) con urgenza; incarico collegiale +
  eccezionale complessita'.

### Limite di fonte e scope
- Le **tabelle tariffarie numeriche** (importo vacazione, onorari fissi/variabili,
  scaglioni a percentuale) sono delegate al **DM 30/5/2002** (art. 50; adeguamenti
  ISTAT ex art. 54), che **non risulta su Normattiva** (URN -> atto non trovato):
  gli **importi non sono riprodotti**. La skill copre il **quadro e la procedura**
  di liquidazione, **non il calcolo numerico** richiesto in origine dalla scheda
  #42. Quando il DM sara' reperibile (host in allowlist) o fornito, si potra'
  aggiungere il modulo di calcolo (onorari a vacazione/percentuale).
- Tratta i soli **ausiliari del magistrato** (CTU, periti, custodi, commissario ad
  acta); non i compensi del **CTP** (di parte, a contratto).

### Note di sviluppo
- Fonte Normattiva: ad ogni aggiornamento riscaricare la pagina pinnata (nuovo hash)
  e rileggere gli articoli; l'art. 170 rinvia al rito dell'art. 15 D.Lgs 150/2011.
- Validazione Livello 2 con CTU/avvocato esperto di liquidazioni.
