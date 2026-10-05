# CHANGELOG - collaudo-verifica-conformita-dlgs36

Il formato e' basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.2.0-alpha] - 2026-08-25

### Added (closes #496)
- Fonte scaricata, hashata e letta (Regola zero):
  - **GU Serie generale n. 192 del 20-8-2026** (PDF integrale del fascicolo)
    SHA256: 1131f5ce3b7b807e2627a33b51069bc79b377600f0293cf9a60441026b10c058
    contenente la **L. 7 agosto 2026, n. 152** (cod. red. 26G00165, conversione del
    D.L. 26 giugno 2026, n. 107) con il suo Allegato di modificazioni e il **testo
    coordinato** del D.L. 107/2026 (cod. red. 26A04179).
  - Trascrizione verbatim in `references/fonti/l-152-2026-gu-192.md`: **art. 1-bis**
    (Sospensione temporanea del recupero dell'anticipazione nei contratti di lavori
    pubblici, pag. 49) e **art. 125 D.Lgs. 36/2023** (Anticipazione, modalita' e
    termini di pagamento del corrispettivo, cc. 1-10) come riportato nei "Riferimenti
    normativi" della stessa GU.
- Estratto `references/estratti/l-152-2026-sospensione-recupero-anticipazione.md`:
  condizioni cumulative della deroga, nesso con la rata di saldo, silenzio della fonte
  sulla garanzia dell'anticipazione, elenco di cio' che la norma non dice.
- `tasks/inquadra-collaudo-termini.md`: nuovo passo 6 "Rata di saldo e anticipazione
  non recuperata".

### Changed
- `SKILL.md`: nuovo paragrafo sulla deroga temporanea nella sezione "Quando usare
  questa skill", fonte aggiunta ai "Riferimenti normativi", nuovo `normative_refs`;
  version 0.1.0-alpha -> 0.2.0-alpha.
- `references/sources.yaml`: `last_verified` 2026-07-17 -> 2026-08-25.

### Contenuto ancorato al testo
- Art. 1-bis c. 1: facolta' della stazione appaltante ("sono autorizzate a
  sospendere"), su richiesta dell'appaltatore, di sospendere il recupero
  dell'anticipazione ex art. 125 D.Lgs. 36/2023, negli appalti di lavori in corso di
  esecuzione, per il tempo strettamente necessario, nei limiti delle risorse
  disponibili a legislazione vigente e comunque non oltre il 31 dicembre 2026.
- Art. 1-bis c. 2: esclusione degli interventi finanziati, in tutto o in parte, con
  risorse PNRR.
- Art. 125 c. 7: certificato di pagamento della rata di saldo subordinato all'esito
  positivo del collaudo o della verifica di conformita' (nesso con l'art. 116).
- Entrata in vigore della L. 152/2026: 21 agosto 2026 (art. 1, c. 2).

### Scope e limiti
- La deroga e' **a termine**: dal 1 gennaio 2027 la skill non deve piu' proporla come
  praticabile. Il vincolo e' scritto sia nel SKILL.md sia nell'estratto sia nel task.
- Il testo dell'art. 1-bis non menziona l'art. 116 e non contiene disposizioni su
  termini del collaudo, natura del certificato o responsabilita' per vizi: la skill lo
  dichiara come silenzio della fonte, non come modifica implicita.
- L'interazione tra sospensione del recupero e riduzione graduale della garanzia
  fideiussoria (art. 125 c. 1) non e' disciplinata dalla fonte: l'estratto lo dichiara
  come lacuna, non la colma.

## [0.1.0-alpha] - 2026-07-17

### Added (closes #315)
- Prima versione della skill di supporto al **collaudo dei lavori** e alla **verifica di
  conformita'** di servizi e forniture nei contratti pubblici, ai sensi del **D.Lgs.
  36/2023, art. 116**, nell'area `appalti-opere-pubbliche`.
- Fonte scaricata, hashata e letta (Regola zero):
  - **D.Lgs. 31/3/2023 n. 36** - indice Normattiva pinnato `!vig=2026-07-17`
    SHA256: 0e9a193836e379cb33cb6daf1a5a988c608eb9559d84b91a841d9ed9791a62af
    (codice 23G00044). Art. 116 versione 2, idGruppo 18, flagTipoArticolo 0, via
    `caricaArticolo`.
  - Trascrizione verbatim in `references/fonti/dlgs-36-2023-art-116.md`.
- Estratto operativo `references/estratti/collaudo-verifica-checklist.md`.
- Due task: `inquadra-collaudo-termini.md` e `verifica-collaudatori-incompatibilita.md`.
- Due esempi: termini e natura del certificato di collaudo (cc. 1-3, 7); nomina del
  collaudatore e incompatibilita' (cc. 4-6).

### Contenuto ancorato al testo
- Art. 116 c. 1 collaudo (lavori)/verifica di conformita' (servizi-forniture); c. 2
  termini 6 mesi/1 anno (all. II.14), certificato provvisorio->definitivo a 2 anni,
  approvazione tacita; c. 3 responsabilita' appaltatore per vizi/difformita' salvo art.
  1669 c.c.; cc. 4/4-bis/4-ter nomina 1-3 collaudatori (requisiti, indipendenza, PA/non
  PA), collaudatore statico, segreteria tecnica; c. 5 verifica di conformita' del
  RUP/direttore dell'esecuzione; c. 6 incompatibilita' (a-e); c. 7 rinvio all'allegato
  II.14 per modalita' e CRE; cc. 8-11 modalita'/tempi verifica, documenti finali (piano
  di manutenzione, BIM art. 43), accertamenti di laboratorio non soggetti a ribasso.

### Scope e limiti
- Non redige il certificato di collaudo/verifica ne' il CRE, non riproduce gli allegati
  II.14/II.15, non nomina i collaudatori ne' valuta requisiti/conflitto di interesse
  (art. 16), non tratta il collaudo statico (DPR 380 art. 67), non sostituisce la
  stazione appaltante, il RUP o l'organo di collaudo. Allegati II.14/II.15, artt. 16, 29,
  43, 45 e art. 1669 c.c. citati e non trascritti.

### Note di sviluppo
- Normattiva: ad ogni aggiornamento riscaricare l'indice del D.Lgs. 36/2023 pinnato
  (nuovo hash) e rileggere l'art. 116 (testo tra `(( ))`, es. correttivo D.Lgs. 209/2024).
- Validazione Livello 2 con RUP / collaudatore / esperto di contratti pubblici.
