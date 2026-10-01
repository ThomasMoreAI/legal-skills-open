---
name: import-notification-licenciement-sboghossian
title: 'Import: Notification de Licenciement (France)'
description: Use when migrating a French-law dismissal notification (lettre de licenciement) drafting or review skill into the mini-claude-for-legal format. The adapter maps legacy French employment-law logic — cause réelle et sérieuse requirements, mandatory content checklist, LRAR delivery rules, and CPH (Conseil de Prud'hommes) exposure analysis — into the standard skill model. Primary jurisdiction France; also relevant for Lebanon and French-influenced OHADA labour contexts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/import/import-notification-licenciement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: fr
practice: employment
language: fr
---

# Import: Notification de Licenciement (France)

## What it does

This import adapter migrates a **French-law dismissal notification skill** — covering the lettre de licenciement — into the `mini-claude-for-legal` standard format. In France, the dismissal letter is a critical legal instrument: it fixes the grounds (motifs) of dismissal, and the employer cannot later invoke different grounds at the CPH (Conseil de Prud'hommes). A poorly drafted lettre de licenciement is the single most common source of wrongful-dismissal liability in French employment litigation.

The source skill may have been a drafting template, a compliance checker, or both. The adapter normalises the shape and surfaces the legal requirements.

## Import config

| Field | Source mapping | Default if absent |
|---|---|---|
| `licenciement_type` | Legacy `type` | `cause_réelle_sérieuse` |
| `motif_specified` | Legacy `motif` | Prompt user — cannot be defaulted |
| `entretien_préalable_done` | Legacy `entretien_done` boolean | Prompt user |
| `délai_notification` | Legacy `délai` field | `2 jours ouvrables` after entretien |
| `delivery_mode` | Legacy `envoi` | `LRAR` (lettre recommandée avec accusé de réception) |
| `language` | Legacy `lang` | `fr` |
| `output_format` | Legacy `format` | `lettre_complete` |

## Dry-run preview

```
IMPORT PREVIEW — notification-licenciement
Source shape       : Lettre de licenciement template / checker
Type               : cause_réelle_sérieuse (default)
Motif              : [requires user input — cannot default]
Entretien préalable: [requires confirmation]
Délai              : minimum 2 jours ouvrables post-entretien
Envoi              : LRAR
Language           : French
Output             : lettre complète
```

## French dismissal procedure (context)

A valid dismissal in France requires compliance with the entire procedure — not just the letter:

1. **Convocation à entretien préalable** — written notice inviting the employee to a preliminary interview; must state the date, time, place, and right to be assisted by a workplace representative or external advisor (conseiller du salarié).
2. **Entretien préalable** — the employer presents the grounds; the employee responds. Minutes are not legally required but advisable.
3. **Délai d'attente** — minimum 2 working days (jours ouvrables) between entretien and dispatch of the dismissal letter.
4. **Lettre de licenciement** — sent by LRAR; must state the real and serious cause (cause réelle et sérieuse).
5. **Préavis (notice period)** — statutory or contractual; employee may work out notice or receive payment in lieu.
6. **Indemnité de licenciement** — statutory indemnity for employees with at least 8 months' service; calculated per the Labour Code (Code du Travail Art L1234-9).

## Mandatory content checklist for the letter

A legally compliant lettre de licenciement must contain:

- [ ] Identification of the employer and employee
- [ ] Date of the entretien préalable
- [ ] Statement that the letter constitutes notification of dismissal
- [ ] **The motif(s) — stated precisely and factually** (this is the critical element)
- [ ] The applicable notice period or waiver
- [ ] Reference to any dispense de préavis (payment in lieu)
- [ ] Information on the solde de tout compte and reçu

## Types of dismissal and specific requirements

| Type | Key legal requirement | CPH exposure if defective |
|---|---|---|
| Faute simple | Cause réelle et sérieuse; notice period due | Indemnité de licenciement sans cause réelle |
| Faute grave | Immediate dismissal; no notice or indemnity | Full notice + indemnity if grounds not proven |
| Faute lourde | Immediate; no indemnity; potential civil liability | Full indemnity + damages if grounds not sustained |
| Cause réelle et sérieuse (non-disciplinary) | Objective grounds; notice due | Reinstatement or Barème Macron indemnity |
| Inaptitude | Medical consultation + search for reclassification | Nullity of dismissal if procedure not followed |

## Barème Macron (indemnity scale)

Since the Ordonnances Macron (2017), CPH indemnity for dismissal without cause réelle et sérieuse is capped by the Barème Macron (Code du Travail Art L1235-3):

| Ancienneté | Minimum indemnity | Maximum indemnity |
|---|---|---|
| < 1 an | 0 mois | 1 mois |
| 1–2 ans | 1 mois | 2 mois |
| 3–4 ans | 3 mois | 4 mois |
| 5–10 ans | 3 mois | 10 mois |
| 10–20 ans | 3 mois | 15,5 mois |
| > 29 ans | 3 mois | 20 mois |

(Monthly salary = 1/12 of gross annual including bonuses)

Note: these caps do not apply to discriminatory dismissals or dismissals in violation of fundamental rights (nullité).

## Failure modes

| Error | Likely cause | Resolution |
|---|---|---|
| `motif_vague` | Source used generic "faute grave" without facts | Flag HIGH risk; prompt for specific factual grounds |
| `entretien_not_confirmed` | Legacy skipped entretien check | Add mandatory entretien confirmation gate |
| `délai_miscalculated` | Source used calendar days not jours ouvrables | Recalculate as working days |
| `lrar_not_specified` | Source used email delivery | Flag: email is insufficient for licenciement |

## Related skills

- [[import-requete-cph-licenciement-faute-grave]]
- [[draft-lettre-licenciement-fr]]
- [[review-employment-termination]]
- [[kb-employment-law-fr]]
- [[import-legal-risk-assessment-zacharie-laik]]
