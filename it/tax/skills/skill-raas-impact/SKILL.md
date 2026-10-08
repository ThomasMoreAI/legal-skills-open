---
name: skill-raas-impact
title: Diritto Italiano — Normativa e Prassi Fiscale
description: Ricerca nella normativa e nella prassi fiscale italiana. Usa questa skill quando l'utente vuole trovare leggi, decreti o atti legislativi italiani (Normattiva), oppure cercare interpelli, circolari, risoluzioni e altri documenti di prassi fiscale (Agenzia delle Entrate, Ministeri, INPS, ecc.). Attiva per qualsiasi richiesta del tipo "cerca la legge su X", "trova il decreto Y", "cosa dice la legge italiana su Z", "c'è un interpello su W", "cosa dice l'AdE su V", "cerca su normattiva", "qual è la posizione del Fisco su U".
author: RAAS-Impact
author_url: https://github.com/RAAS-Impact/normattiva-claude-mcb/tree/main/skill
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: it
practice: tax
language: it
---

# Diritto Italiano — Normativa e Prassi Fiscale

Questa skill copre due ambiti complementari della ricerca giuridica italiana. Prima di agire, classifica la richiesta dell'utente e segui le istruzioni del file corretto.

---

## Routing: quale istruzione seguire

| L'utente chiede… | File da seguire | Esempi |
|---|---|---|
| Testo di una legge, decreto, atto normativo | **normattiva.md** | "Cerca la legge sulla privacy", "Art. 18 dello Statuto dei Lavoratori", "decreto sicurezza sul lavoro", "legge 300/1970" |
| Versione vigente o storica di una norma | **normattiva.md** | "Testo del GDPR italiano vigente al 2020", "modifiche alla legge X tra il 2023 e il 2024" |
| Esportazione/download di collezioni di atti | **normattiva.md** | "Scarica tutti i decreti legislativi del 2024" |
| Interpello, circolare, risoluzione, prassi fiscale | **interpelli.md** | "Interpello n. 82 del 2026", "cosa dice l'AdE sulle cripto", "circolare INPS su X" |
| Posizione ufficiale di un ente su una norma tributaria | **interpelli.md** | "Qual è la posizione del Fisco sulle stock option?", "c'è prassi sul bonus ricerca?" |
| Norma + sua interpretazione fiscale | **Entrambi** | "Cosa dice l'art. 67 TUIR e come lo interpreta l'AdE?" → normattiva.md per il testo, interpelli.md per la prassi |

### Quando usare entrambi

Se la richiesta coinvolge sia il testo normativo sia la sua interpretazione da parte dell'amministrazione finanziaria, combinare i due flussi:
1. Recuperare il testo della norma con i tool MCP Normattiva (vedi **normattiva.md**)
2. Cercare la prassi interpretativa correlata (vedi **interpelli.md**)
3. Presentare all'utente entrambi i risultati, distinguendo chiaramente tra norma e prassi

---

## Struttura di questa skill

- **normattiva.md** — Istruzioni per cercare e recuperare atti normativi dalla banca dati ufficiale Normattiva (`dati.normattiva.it`) tramite i tool MCP del server Normattiva.
- **interpelli.md** — Istruzioni per cercare interpelli, circolari, risoluzioni e altra prassi fiscale dai portali dell'Agenzia delle Entrate e del Dipartimento delle Finanze, tramite navigazione web.
