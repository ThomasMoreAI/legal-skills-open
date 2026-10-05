---
name: legal-subsumption-sigmacodeat
title: Legal Subsumption Skill
description: 'Performs legal subsumption: maps a concrete fact pattern (Sachverhalt) to the

  applicable legal norm (Tatbestand → Rechtsfolge). Works for DE/AT/CH law.

  Steps: extract facts → identify applicable norms → subsume facts under norms →

  state the legal consequence. Cites exact §§ and controlling case law from the

  brain. NEVER issues binding legal advice; flags every conclusion as an

  AI-assisted legal analysis requiring attorney review.'
author: Sigmacodeat
author_url: https://github.com/Sigmacodeat/Sigmabrain/tree/main/server/skills/legal-subsumption
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: general
language: en
---

# Legal Subsumption Skill

> **Warning:** AI-generated legal analysis. All conclusions require attorney review before use.
> **Convention:** See [conventions/quality.md](../conventions/quality.md). Every § reference cites the exact norm.
> **Chains with:** [precedent-finder](../precedent-finder/SKILL.md) for controlling case law.

## Contract

This skill guarantees:
1. Every applicable norm is cited with § number and statute acronym
2. The subsumption follows Gutachtenstil (issue → norm → subsumption → result)
3. Controlling BGH/OGH/BFH decisions are cited where found in brain
4. The output is marked as attorney-review-required

## Trigger Conditions

Use this skill when the user presents a fact pattern and asks for legal classification,
applicable norms, or the legal consequence. Do NOT use for pure factual queries.

## Protocol

### Step 1 — Extract the Fact Pattern

Parse the user's input into:
- **Parties**: Who is involved (Kläger/Beklagter, Schuldner/Gläubiger)?
- **Acts**: What happened (Handlung, Unterlassen, Erfolg)?
- **Context**: Which legal area applies (Zivilrecht, Strafrecht, Steuerrecht, Verwaltungsrecht)?
- **Jurisdiction**: DE / AT / CH / EU (default: DE if not specified)

### Step 2 — Norm Search

```
gbrain search "<key facts> Anspruchsgrundlage §" --mode balanced --source legal-corpus
gbrain search "<key facts> Norm Tatbestand" --source legal-corpus
```

If the brain has the law corpus loaded (DE: BGB, StGB, ZPO, HGB, AO, UStG, EStG; AT: ABGB, StGB, ZPO; CH: OR, ZGB):
- Search for the relevant norms by fact pattern keywords
- Retrieve the exact § text

### Step 3 — Subsumption (Gutachtenstil)

Output format (strictly follow this structure):

```
## Rechtliche Analyse — [Datum] — Vorläufig, kein Anwaltsverhältnis

### I. Sachverhalt
[Zusammenfassung des Sachverhalts in 3–5 Sätzen]

### II. Anwendbare Normen
- § [X] [Gesetz]: [Tatbestand in einem Satz]
- § [Y] [Gesetz]: [Rechtsfolge in einem Satz]
[Quellen: brain pages mit §§]

### III. Subsumption

**Zu § [X] [Gesetz]:**
Tatbestandsmerkmal 1 ([Wortlaut]): [Sachverhalt-Umstand] → [erfüllt / nicht erfüllt]
Tatbestandsmerkmal 2 ([Wortlaut]): [Sachverhalt-Umstand] → [erfüllt / nicht erfüllt]
...

**Ergebnis zu § [X]:** [Rechtsfolge tritt ein / tritt nicht ein], weil [Begründung in 1–2 Sätzen].

### IV. Leitentscheidungen
[BGH/OGH/BFH-Entscheide aus dem Brain, falls gefunden]
- [Az.]: [Leitsatz]

### V. Rechtliche Einordnung (Gesamtergebnis)
[1 Absatz Zusammenfassung]

### VI. Empfehlungen
- [ ] Anwaltliche Überprüfung erforderlich
- [ ] Fehlende Informationen: [Liste]
- [ ] Nächste Schritte: [Liste]

---
⚠️ Diese Analyse ist KI-generiert und ersetzt keine anwaltliche Beratung.
Erstellt: [Datum] | Skill: legal-subsumption v1.0.0
```

### Step 4 — File in Brain

```
gbrain put_page \
  --slug "legal/analyses/subsumption-[slug]-[date]" \
  --type "legal_document" \
  --metadata '{"document_type": "analysis", "requires_review": true}'
```

## Jurisdiction Quick Reference

| Jurisdiction | Civil | Criminal | Tax | Procedure |
|---|---|---|---|---|
| DE | BGB, HGB, GmbHG | StGB, OWiG | EStG, KStG, UStG, AO | ZPO, StPO |
| AT | ABGB, UGB | StGB, VStG | EStG, UStG, BAO | ZPO, StPO |
| CH | OR, ZGB | StGB | DBG, MWSTG | ZPO, StPO |
| EU | DSGVO, HGB | — | MwStSystRL | EuGH-Verfahren |

## Error Handling

- If no relevant norm is found in brain: say so explicitly; suggest attorney consultation
- If the fact pattern is incomplete: list what information is needed before subsumption
- If multiple norms could apply: subsume under all of them separately

## Anti-Patterns

- ❌ Stating a legal conclusion as binding advice — every result is "vorläufig, anwaltlich zu prüfen".
- ❌ Subsuming without citing the exact § and statute; if the norm is not in the brain, say so.
- ❌ Mixing jurisdictions silently — default DE, switch only when stated.
- ❌ Skipping a Tatbestandsmerkmal because it is "obvious".

## Output Format

Gutachtenstil: I. Sachverhalt · II. Anwendbare Normen (cited §§) · III. Subsumption
(per Tatbestandsmerkmal) · IV. Leitentscheidungen · V. Gesamtergebnis · VI. Empfehlungen,
ending with the AI / attorney-review notice. See "Step 3 — Subsumption".
