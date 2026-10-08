# AGENTS.md - ai-act-compliance (versione italiana - work in progress)

> Convenzioni di dominio per agent che lavorano su questa skill. Per le convenzioni globali del repo vedi `../../AGENTS.md`.

## Stato

**ATTENZIONE**: questa skill e' una **versione italiana preliminare** dell'AI Act compliance. La versione completa, inglese, full-feature, e' nel **repo separato** `/Users/davidemorelli/work/ai-act-skill/` (pubblico su GitHub: `morellid/ai-act-skill`).

Stato in skill-per-ingegneri:
- SKILL.md: scaffold placeholder, non personalizzato
- 5 task files: contenuto incompleto / da finalizzare
- 6 estratti normativi: presenti ma da verificare
- sources.yaml: scaffold con placeholder
- Profili nazionali (v0.2.0): D.Lgs. 160/2026 trascritto in `references/fonti/dlgs-160-2026.md` (SHA256 registrato), estratto e task `check-profili-nazionali-italia.md` completi

**Decisione strategica**: sviluppo full-feature su `ai-act-skill` (inglese, EU consultancy market, MIT, distribuito autonomamente). La versione italiana qui resta come bozza per uso da parte di ingegneri Ordini, da rifinire eventualmente con focus italiano specifico (riferimenti al Garante, AGID, DDL Italiano AI Act in approvazione).

## Quando aggiornare questa skill (vs il repo dedicato)

- Aggiornare **questa skill** se: stiamo aggiungendo riferimenti italiani specifici (L. 132/2025, D.Lgs. 160/2026 e suoi decreti attuativi, linee guida AGID per AI nella PA, posizioni Garante su scoring, ecc.).
- Aggiornare **il repo `ai-act-skill`** per: tutto il resto. La skill inglese e' la fonte di verita' per il regolamento UE.

## Dominio

**Reg. UE 2024/1689 - AI Act**. Classificazione sistemi AI (vietato / alto rischio / rischio limitato / GPAI), obblighi provider e deployer, GPAI con rischio sistemico (10^25 FLOPs), trasparenza art. 50, FRIA art. 27.

## Fonti autoritative (ufficiali)

- **Reg. UE 2024/1689** - testo OJ:L_202401689 (EUR-Lex)
- **GPAI Code of Practice** (luglio 2025) - voluntary tool
- **Commission Guidelines on GPAI scope** (luglio 2025)
- **AI Act Service Desk** - tool ufficiale Commissione (`ai-act-service-desk.ec.europa.eu`)
- **CEN-CENELEC JTC 21** - standard armonizzati in preparazione
- (Italia) **D.Lgs. 9 settembre 2026, n. 160** - GU SG n. 214 del 15/09/2026: polizia, reato 437-bis c.p., 231 art. 25-vicies, strumenti processuali civili
- (Italia) **AGID** - linee guida AI per PA, quando emergeranno
- (Italia) **Garante** - posizioni su scoring, biometrici, AI nel lavoro

## Calendario di applicazione (post Digital Omnibus - accordo provvisorio 7 maggio 2026, non ancora in GUUE)

- 2 febbraio 2025: prohibitions art. 5 lett. a-h, AI literacy art. 4 - **IN VIGORE**
- 2 agosto 2025: GPAI obligations cap. V, governance, sanzioni - **IN VIGORE**
- 2 agosto 2026: obblighi trasparenza art. 50 par. 1/3/4/4bis
- **2 dicembre 2026**: watermarking art. 50 par. 2 (output sintetici machine-readable) + nuovo divieto Omnibus per CSAM/nudifier/deepfake sessuali non consensuali
- **2 dicembre 2027**: high-risk Annex III + FRIA art. 27 (era 2 agosto 2026, rinvio Omnibus)
- **2 agosto 2028**: high-risk Annex I products (era 2 agosto 2027, rinvio Omnibus)

> Le date Omnibus sono subordinate a endorsement formale, revisione legale-linguistica e pubblicazione in GUUE. Riconfermare alla pubblicazione finale.

## Convenzioni specifiche (se la skill viene completata)

### Cosa NON fare
- Non sostituire avvocato AI law per casi reali.
- Non confondere "user" (concetto pre-GDPR) con "deployer" (concetto AI Act).
- Non assumere che un upstream GPAI provider copra le obbligazioni del downstream system.
- D.Lgs. 160/2026: non indicare una data di entrata in vigore (il decreto non la fissa, verificare su Normattiva); non trattare "utilizzatore professionale" (art. 437-bis c.4 c.p.) come sinonimo testuale di deployer; non descrivere il 612-quater c.p. (richiamato ma non riportato dal decreto); non attribuire al Titolo I obblighi ulteriori rispetto al Reg. 2024/1689 (art. 1 c.3).

### Cosa fare
- Citare articolo + comma + lettera preciso (es. "Art. 5(1)(f)", "Annex III area 4(b)").
- Distinguere ruoli: provider, deployer, importer, distributor.
- Sanzioni: fino a 35M EUR / 7% fatturato globale per art. 5 (massima); 15M / 3% per altre violazioni.

## Cosa fare adesso

Se stai lavorando su questa skill: **prima parla con l'autore (Davide Morelli)** per stabilire se completarla in italiano o solo mantenerla come stub. Per la versione operativa, riferisciti a `ai-act-skill`.
