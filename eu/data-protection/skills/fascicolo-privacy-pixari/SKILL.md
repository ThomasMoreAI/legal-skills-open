---
name: fascicolo-privacy-pixari
title: Fascicolo privacy (matter workspace)
description: 'Matter workspace privacy: fascicoli DSAR, DPA, violazioni, DPIA. Struttura cartelle, matter.md, collegamento CLAUDE.md. Nessuna consulenza legale.'
author: pixari
author_url: https://github.com/pixari/claude-per-il-diritto-italiano/tree/main/privacy-gdpr/skills/fascicolo-privacy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: it
---

# Fascicolo privacy (matter workspace)

> **Bozza — non consulenza legale.** Pattern EN `matter-workspace` adattato IT.

## Configurazione

1. Leggi [`privacy-gdpr/CLAUDE.md`](../../CLAUDE.md) → Processo DSAR, sistemi, escalation.
2. Path consigliato (documentazione, non codice):
   - Workspace: `matters/<slug>/`
   - Opzionale persistente: `~/.claude/plugins/config/pixari-italian-legal-skills/privacy-gdpr/matters/<slug>/`

## Intake

| Campo | Valore |
| --- | --- |
| Slug | `privacy_<anno>_<tipo>_<codice>` — no PII in slug pubblico |
| Tipo | dsar / dpa / violazione / dpia / gap |
| Titolare/responsabile ruolo cliente | |
| DPO coinvolto | sì/no |
| Scadenza operativa | `[da verificare]` art. 12 se DSAR |

## Struttura cartella

```
matters/<slug>/
  matter.md           # meta fascicolo
  00_richiesta/       # input interessato o incidente
  01_analisi/         # note interne, mappatura sistemi
  02_bozze/           # lettere, DPIA, gap table
  03_approvazioni/    # traccia DPO/legale
  log-decisioni.md
```

## File `matter.md` (template)

```markdown
# Matter: [titolo interno]
- Tipo:
- Data apertura:
- Stato: aperto | in revisione | chiuso
- Skill usati:
- Prossima azione:
- Escalation attiva: sì/no
```

## Skill per tipo

| Tipo | Skill |
| --- | --- |
| DSAR | `/privacy-gdpr:risposta-diritti-interessato` |
| DPA | `/privacy-gdpr:revisione-dpa` |
| Violazione | `/privacy-gdpr:violazione-dati` |
| Nuovo trattamento | `/privacy-gdpr:triage-trattamento` → `generazione-dpia` |
| Gap | `/privacy-gdpr:gap-normativo-privacy` |

## Cross-link hub

`/diritto-italiano-hub:fascicolo-mandato` se fascicolo misto privacy + contratto.

## Test

`testatti/privacy-fittizio/` per prova senza dati reali.

## Divieti

- Non committare matter con dati reali su repo pubblico
