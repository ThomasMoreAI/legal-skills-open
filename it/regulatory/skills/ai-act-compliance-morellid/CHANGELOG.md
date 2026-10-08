# CHANGELOG - ai-act-compliance

Tutte le modifiche significative alla skill sono documentate qui.

Formato basato su [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
versionamento [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Da fare
- Riconfermare date Omnibus dopo pubblicazione in GUUE (testo definitivo + lettera precisa per il nuovo divieto su CSAM/nudifier/deepfake sessuali)
- Catalogare linee guida Commissione su pratiche vietate, classificazione art. 6, norme armonizzate

## [0.2.0] - 2026-09-27

### Added - profili nazionali D.Lgs. 9 settembre 2026, n. 160 (issue #501)

- Fonte `dlgs-160-2026-gu214`: PDF GU Serie Generale n. 214 del 15/09/2026, SHA256 registrato; trascrizione in `references/fonti/dlgs-160-2026.md` (Titoli II e III integrali, Titolo I per le parti operative)
- Estratto `references/estratti/dlgs-160-2026-profili-nazionali.md`
- Task `tasks/check-profili-nazionali-italia.md`: reato art. 437-bis c.p., art. 25-vicies D.Lgs. 231/2001, accesso alle prove (art. 17), presunzione del nesso causale (art. 18), irrilevanza della sola conformità (art. 19), azione diretta verso l'assicuratore (art. 20), Forze di polizia (artt. 1-10, 21)
- Esempio `examples/profili-nazionali-triage-pronto-soccorso/`
- Rinvii nei task `check-deployer-obligations.md` (sorveglianza umana, sinergie) e `check-high-risk-provider.md` (art. 14, sinergie)
- `normative_refs`, descrizione, routing in `SKILL.md`, README, AGENTS.md, `agents/openai.yaml`

### Note - differenze rispetto al testo della issue

- Il decreto **non contiene un articolo sull'entrata in vigore** e non fissa alcuna data: nessuna data riportata nella skill.
- Il 437-bis richiede pericolo per la **vita o l'incolumità pubblica o individuale** (o per la sicurezza dello Stato), non per la "sicurezza pubblica".
- Il termine di **30 giorni** (art. 20) è quello per comunicare l'esistenza della polizza RC, non un termine di adeguamento.
- La presunzione del nesso causale (art. 18) non è limitata al fornitore.
- L'art. 25-vicies prevede anche **sanzioni interdittive** (art. 9 c.2 lett. b-e D.Lgs. 231/2001).
- Il Titolo I (polizia) dichiara di **non introdurre nuovi obblighi** rispetto al Reg. 2024/1689.
- Il decreto richiama l'art. 612-quater c.p. senza descriverlo: la skill non lo qualifica.

## [0.1.3] - 2026-05-17

### Changed - rinvii Digital Omnibus (accordo provvisorio 7 maggio 2026, issue #163)

- Aggiornate date di applicazione AI Act per riflettere accordo provvisorio Digital Omnibus:
  - Alto rischio Allegato III + FRIA art. 27: rinviato da **02/08/2026** a **02/12/2027**
  - Alto rischio Allegato I (componenti sicurezza prodotti): rinviato da **02/08/2027** a **02/08/2028**
  - Watermarking art. 50 par. 2 (output sintetici machine-readable): rinviato da **02/08/2026** a **02/12/2026** (gli altri par. dell'art. 50 restano al 02/08/2026)
- Tabella date in `SKILL.md` rivista per distinguere paragrafi dell'art. 50
- File aggiornati: `SKILL.md`, `AGENTS.md`, `tasks/classifica-sistema.md`, `tasks/check-high-risk-provider.md`, `references/estratti/ai-act-art-5-pratiche-vietate.md`, `references/estratti/ai-act-art-50-trasparenza.md`, esempi

### Added

- Nuova pratica vietata Omnibus: sistemi di generazione di CSAM, immagini intime non consensuali, deepfake sessuali espliciti (app "nudifier"). Adeguamento entro **02/12/2026**.
- Note diffuse sullo stato provvisorio dell'accordo Omnibus (mancano endorsement formale, revisione legale-linguistica e pubblicazione in GUUE - le date sono soggette a riconferma).

### Note

- Fonti citate nell'issue #163: Agendadigitale, Tom's Hardware, AI4Business - consultate il 2026-05-17.
- Skill resta `0.1.x-alpha` (versione italiana stub); la versione full-feature inglese `ai-act-skill` (repo separato) resta fonte di verita' principale per la skill EU.

## [0.1.2] - 2026-05-11

### Fixed (source-grounding CI - issue #92 v2)

- Corretto `references/sources.yaml`: il campo `binary_path` era impostato a
  `not_in_repo/ai-act-it-eurlex.pdf` e `sha256` a `a61b6170...`, ma EUR-Lex
  risponde con challenge WAF AWS (HTTP 202, corpo vuoto) a qualsiasi richiesta
  programmatica, causando hash mismatch `e3b0c442...` (SHA256 di contenuto vuoto)
  nel job `validate-sources` della CI.
- Impostati `binary_path: null` e `sha256: null` in coerenza con il comportamento
  del server (la CI salta il fetch per `binary_path: null`, conforme alla logica
  di `verify-sources.py`). Il campo `md_path` rimane invariato:
  `references/fonti/ai-act-it-eurlex.md` esiste ed e' non vuoto (329 righe di
  trascrizione reale del PDF letto il 2026-04-25, SHA256 a61b6170...).
- Aggiornato URL canonico da `http://data.europa.eu/eli/reg/2024/1689/oj`
  (reindirizza con 307 a EUR-Lex, poi WAF) a
  `https://eur-lex.europa.eu/legal-content/IT/TXT/PDF/?uri=OJ:L_202401689`
  (URL diretto PDF italiano, comunque bloccato da WAF in contesto CI).

### Note

- Il file `references/fonti/ai-act-it-eurlex.md` rimane la prova di lettura
  effettiva del PDF. Contiene trascrizione fedele di Art. 3, 5, 6, 9, 26, 27,
  50, 51-55, 113, All. II e III, con pagine OJ indicate.
- Per futura verifica automatica: l'hash originale del PDF era a61b6170...
  (calcolato il 2026-04-25 su not_in_repo/ai-act-it-eurlex.pdf). Quando EUR-Lex
  smette di usare WAF o viene trovato un mirror stabile, ripristinare
  binary_path e sha256 con verifica CI.

## [0.1.1] - 2026-05-09

### Fixed (source-grounding remediation - issue #92)

- Creato `references/fonti/ai-act-it-eurlex.md`: trascrizione fedele del PDF scaricato (`not_in_repo/ai-act-it-eurlex.pdf`, SHA256 a61b6170...), coprendo Art. 3, 5, 6, 9, 26, 27, 50, 51-55, 113, Allegato II e III. File mancante in 0.1.0-alpha.
- Aggiornato `references/sources.yaml`: rimosso placeholder-example `esempio-dlgs`, aggiunta voce reale `ai-act-it-eurlex` con tutti i campi compilati (sha256, url, binary_path, excerpt_path, license, notes).
- Riscritto `SKILL.md`: rimosso scaffold generico template, sostituito con contenuto reale della skill (routing task, date applicazione, target, limiti).

### Note

- La fonte PDF `not_in_repo/ai-act-it-eurlex.pdf` era gia' presente nel repo prima di questa fix; la remediation ha aggiunto la trascrizione fonti/ mancante.
- Gli estratti in `references/estratti/` sono stati verificati contro il testo del PDF e risultano coerenti con il contenuto letto.

### Da fare
- Validazione Livello 1 con `scripts/validate.sh`
- Validazione Livello 2 da consulente legale specializzato in diritto digitale
- Test su caso reale di compliance AI Act (con consenso cliente)
- Catalogare linee guida Commissione su pratiche vietate (febbraio 2025) appena disponibili
- Catalogare linee guida Commissione su classificazione art. 6 (scadenza 02/02/2026)
- Aggiungere estratti di Allegato XI (doc tecnica GPAI) e XII (info per integratori) quando piu' rilevanti
- Aggiungere estratto di Allegato IV (documentazione tecnica art. 11) per provider high-risk
- Esempi aggiuntivi:
  - `provider-credit-scoring-gap/` per check-high-risk-provider
  - `deployer-pa-assistenza/` per check-deployer-obligations
  - `gpai-provider-llm-rischio-sistemico/` per check-gpai-provider
- Tracciare aggiornamenti norme armonizzate ETSI/CEN-CENELEC
- Tracciare Code of Practice GPAI quando definitivo

## [0.1.0-alpha] - 2026-04-25

### Added
- Scaffold completo via `scripts/new-skill.sh`
- `SKILL.md` con frontmatter, routing a 5 task files, disclaimer art. 99 sanzioni
- 6 estratti normativi:
  - `references/estratti/ai-act-art-5-pratiche-vietate.md` - 8 pratiche vietate + esempi tipici per ingegneri
  - `references/estratti/ai-act-art-6-9-classificazione-high-risk.md` - classificazione + sistema gestione rischi
  - `references/estratti/ai-act-allegato-iii.md` - 8 settori high-risk + mappa tipica per use case
  - `references/estratti/ai-act-art-26-27-deployer-fria.md` - obblighi deployer + FRIA
  - `references/estratti/ai-act-art-50-trasparenza.md` - 5 categorie trasparenza
  - `references/estratti/ai-act-art-51-55-gpai.md` - GPAI standard + rischio sistemico
- 5 task files operativi:
  - `tasks/classifica-sistema.md` - 9 step di classificazione + obblighi applicabili
  - `tasks/check-high-risk-provider.md` - checklist art. 8-22 + conformity assessment
  - `tasks/check-deployer-obligations.md` - obblighi art. 26 + FRIA art. 27
  - `tasks/check-gpai-provider.md` - obblighi art. 53 + 55
  - `tasks/check-trasparenza.md` - 5 categorie obblighi art. 50
- `references/sources.yaml` con hash SHA256 reale per AI Act italiano (a61b6170...)
- 2 esempi:
  - `examples/classifica-chatbot-cs/` - chatbot CS basato su GPT-4 = TRASPARENZA art. 50
  - `examples/classifica-hr-emozioni/` - video-interview HR con sentiment analysis = VIETATO art. 5 lett. f, con percorso di pivot a high-risk

### Note di sviluppo
- Skill considerata draft finche' non passa Livello 2 di validazione (consulente legale specializzato)
- Validatore di dominio target: avvocato diritto digitale UE / consulente AI compliance
- Skill commercialmente valida sia per uso open via repo (ingegneri italiani) sia per consulenza enterprise (vedi piano boutique business)
- Sinergica con skill `gdpr-registro-dpia` per casi che intersecano dati personali

### Date di applicazione AI Act (riferimento al momento del rilascio 0.1.0-alpha, pre-Omnibus)
- 02/02/2025: pratiche vietate (art. 5) + AI literacy (art. 4)
- 02/08/2025: GPAI (art. 53-55) + governance + sanzioni
- 02/08/2026: high-risk Allegato III (maggior parte degli obblighi)
- 02/08/2027: high-risk Allegato I (componenti sicurezza prodotti)

> **Aggiornamento 2026-05-17 (v0.1.3)**: queste date sono state riviste dall'accordo provvisorio Digital Omnibus del 7 maggio 2026. Vedi entry 0.1.3 sopra per le nuove date.
