---
name: revisione-dpa-pixari
title: Revisione DPA (art. 28 GDPR)
description: 'Revisione contratto di nomina responsabile (art. 28 GDPR) term-by-term: istruzioni, sub-responsabile, misure, breach, audit, trasferimenti. Output tabella gap con severity. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/revisione-dpa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
sources:
- title: Checklist Art28
  path: references/checklist-art28.md
---

# Revisione DPA (art. 28 GDPR)

> **Bozza — non consulenza legale.** Verificare clausole tipo UE, decisioni adeguatezza e TIA. Non sostituisce negoziazione né firma.

## Input

- Testo DPA / allegato privacy al contratto commessa o fornitura
- Ruolo del cliente: **titolare** che revisiona il DPA del responsabile, o **responsabile** che propone al titolare
- Eventuale `CLAUDE.md` → playbook clausole accettate / red lines

Leggi anche `skills/revisione-dpa/references/checklist-art28.md` se presente nel workspace.

---

## Step 1 — Qualificazione ruoli

| Ruolo | Verifica |
| --- | --- |
| Titolare | Definisce finalità e mezzi; istruzioni documentate |
| Responsabile | Tratta per conto del titolare; solo su istruzioni documentate |
| Sub-responsabile | Autorizzazione generale/specifica art. 28(2) `[da verificare]` |
| Joint controller | Art. 26 — non confondere con semplice responsabile |

Se il contratto mescola **licenza software** e **trattamento dati** → separa le due matrici di rischio.

---

## Step 2 — Checklist art. 28(3) — obblighi minimi

Per ogni voce: **OK** / **Gap** / **N/A** + formulazione bozza suggerita.

| # | Requisito art. 28(3) | Esito | Note / severity |
| --- | --- | --- | --- |
| a | Trattare solo su istruzioni documentate | | |
| b | Personale vincolato a riservatezza | | |
| c | Misure art. 32 (TOM) — allegato o riferimento | | |
| d | Non sub-delegare senza autorizzazione | | |
| e | Assistenza diritti interessati | | |
| f | Assistenza sicurezza, DPIA, consultazione | | |
| g | Cancellazione/restituzione a fine rapporto | | |
| h | Prove conformità + audit | | |
| i | Informare titolare su sub-responsabile | | |
| j | Responsabilità solidale verso interessato (ove applicabile) | | `[da verificare]` |

**Severity:** `alta` = non firmabile senza fix; `media` = negoziabile; `bassa` = preferenza commerciale.

---

## Step 3 — Temi oltre il minimo legale

| Tema | Cosa cercare |
| --- | --- |
| **Definizioni** | Allineamento art. 4 GDPR; "dati personali", "violazione" |
| **Durata** | Coerente con contratto principale; sopravvivenza obblighi |
| **Data breach** | Notifica titolare: tempi (es. 24–48h), contenuto, cooperazione |
| **Sub-responsabile** | Lista / generale + diritto opposizione; flusso informativo |
| **Trasferimenti extra-SEE** | SCC UE, UK IDTA, decisioni adeguatezza, TIA `[da verificare]` |
| **Audit** | Frequenza, on-site vs remoto, costi, limiti riservatezza terzi |
| **Responsabilità** | Cap, esclusioni, indennizzo — coerenza con cap contratto principale |
| **Legge applicabile / foro** | Coerenza con commessa; attenzione clausole imperative consumatore B2C |
| **Assistenza Garante** | Cooperazione con autorità; costi |
| **IP / backup** | Restituzione supporti, distruzione certificata |

---

## Step 4 — Trasferimenti e Schrems II

Se dati fuori SEE:

1. Base trasferimento identificata? (adeguatezza, SCC, BCR, deroga art. 49 `[da verificare]`)
2. TIA / valutazione impatto trasferimento documentata?
3. Misure supplementari descritte?

**Flag:** `richiede-DPO-transfer` se base assente o solo "consenso generico".

---

## Step 5 — Output

### Tabella gap (obbligatoria)

| ID | Clausola | Gap | Severity | Bozza formulazione |
| --- | --- | --- | --- | --- |
| G1 | … | … | alta/media/bassa | testo suggerito |

### Executive summary (5–10 righe)

- Firmabile sì/no condizionato
- Top 3 rischi
- Prossimi passi (negoziazione, DPO, aggiornamento registro trattamenti)

### Cross-link

- Clausole privacy nel contratto commerciale → `/diritto-civile:revisione-contratto-b2b` con flag privacy
- DSAR in corso → `/privacy-gdpr:risposta-diritti-interessato`

---

## Appendice — Matrice clausole SCC (bozza checklist)

| Elemento SCC | Presente | Gap |
| --- | --- | --- |
| Modulo e data SCC | | |
| Descrizione trasferimenti | | |
| Responsabilità sub-processor | | |
| Misure supplementari TIA | | |
| Legge terzo paese e rimedi | | |

## Appendice — Negoziazione (suggerimenti bozza)

| Gap | Controparte tipica | Controproposta bozza |
| --- | --- | --- |
| Audit illimitato | Rifiuto | Audit annuale 1 giorno, notice 30gg |
| Notifica breach 72h | "tempestiva" | Entro 24h dalla scoperta |
| Sub-processor | Lista chiusa | Generale + notifica 30gg + opposizione |

## Divieti

- Non dichiarare conformità GDPR globale
- Non omettere flag su trasferimenti USA/cloud senza SCC aggiornate `[da verificare]`

## Appendice — Checklist finale sessione

- [ ] Output inizia con disclaimer bozza / non consulenza
- [ ] Norme e sentenze non verificate: `[da verificare]`
- [ ] Escalation documentata se applicabile
- [ ] Prossimi passi con responsabile (legale, DPO, HR)
- [ ] Nessun dato reale di mandato in Issue/PR pubbliche

## Appendice — Workflow collegati

| Esigenza | Comando |
| --- | --- |
| Profilo studio | `/diritto-italiano-hub:cold-start-interview` |
| Metodo e citazioni | `/diritto-italiano-hub:metodo-giuridico`, `citazione-italiana` |
| Avvertenze | `/diritto-italiano-hub:avvertenze-legali` |
| Fascicolo | `/diritto-italiano-hub:fascicolo-mandato` |

## Appendice — Fonti (non in repo)

Verificare su: Normattiva, EUR-Lex, garanteprivacy.it, database giuridici dello studio.

## Appendice — Test

Fascicoli fittizi in `testatti/` — personaggi inventati.

## Appendice — Revisione umana

Ogni bozza richiede revisione da professionista abilitato prima di invio, deposito o firma.
