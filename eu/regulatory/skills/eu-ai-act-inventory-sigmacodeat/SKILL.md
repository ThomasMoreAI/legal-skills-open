---
name: eu-ai-act-inventory-sigmacodeat
title: EU-AI-Act-Inventory Skill
description: 'Maintains the organisation''s EU AI Act inventory: classifies each AI system

  (prohibited / high-risk per Annex III / limited-risk per Art. 50 / minimal),

  lists the obligations that follow, and flags the evidence still missing before

  the 2 Aug 2026 deadline (Art. 50 labeling, logged human oversight, Annex-III

  classification memo, risk-management doc). Supports the compliance officer;

  classification is per-system and requires sign-off.'
author: Sigmacodeat
author_url: https://github.com/Sigmacodeat/Sigmabrain/tree/main/server/skills/eu-ai-act-inventory
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# EU-AI-Act-Inventory Skill

> **Warning:** AI-assisted EU AI Act classification. The classification is
> per-system and legally consequential — it requires compliance-officer sign-off.
> **Regulatory basis:** VO (EU) 2024/1689 — Art. 50 (transparency), Annex III
> (high-risk), Art. 113 (timeline; most duties from 02.08.2026).
> **Chains with:** [control-effectiveness](../control-effectiveness/SKILL.md), [dsgvo-compliance](../dsgvo-compliance/SKILL.md).

## Contract

This skill guarantees:
1. Each AI system gets a risk class (prohibited / high-risk Annex III / limited Art.50 / minimal) with the reason.
2. The obligations that follow the class are listed.
3. Missing evidence is flagged against the 02.08.2026 deadline.
4. Output is decision-support, marked classification-requires-sign-off.

## Trigger Conditions

Use to classify an AI system or maintain the AI inventory. Do NOT use for GDPR
processing analysis (→ dsgvo-compliance) or general control assessment
(→ control-effectiveness).

## Protocol

1. **Identify** the AI system: purpose, users, decisions it influences, data.
2. **Classify**: prohibited (Art. 5) / high-risk (Annex III incl. 8a justice) / limited (Art. 50) / minimal — with the reason.
3. **Obligations**: list what the class requires (labeling, human oversight, logging, risk-management, conformity).
4. **Gap**: flag the missing evidence vs. the 02.08.2026 deadline; file/update an inventory page.

## Output Format

```
## EU-AI-Act-Inventar — [System] — Einstufung zu prüfen (Compliance-Freigabe)

### System
Zweck · Nutzer · beeinflusste Entscheidungen · Datenbasis

### Einstufung
Klasse: [verboten / hochrisiko (Annex III Nr. X) / begrenzt (Art. 50) / minimal]
Begründung: […]

### Pflichten
- [ ] [Pflicht je Klasse]

### Fehlende Nachweise (bis 02.08.2026)
- [ ] [z. B. Aufsichts-Protokoll, Annex-III-Memo]

---
⚠️ KI-gestützt · Einstufung je System, Freigabe erforderlich. Erstellt: [Datum] | eu-ai-act-inventory v1.0.0
```

## Anti-Patterns

- ❌ Presenting the risk class as a final legal determination — it needs sign-off.
- ❌ Defaulting everything to "minimal" to avoid obligations.
- ❌ Listing obligations without flagging the missing evidence.
- ❌ Ignoring the 02.08.2026 deadline on open items.

## Error Handling
- System purpose/usage unclear → ask; classification without it is unreliable.
- Borderline Annex III → flag both readings and route to a human decision.
