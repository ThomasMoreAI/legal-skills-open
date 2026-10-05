---
name: legal-strategie-sigmacodeat
title: Legal-Strategie Skill
description: 'Generates legal strategy recommendations for a case, including procedural

  tactics, risk assessment, and recommended next steps. Uses the case''s facts,

  claims, defenses, evidence, and opponent profile to produce actionable

  strategy advice in structured format.'
author: Sigmacodeat
author_url: https://github.com/Sigmacodeat/Sigmabrain/tree/main/server/skills/legal-strategie
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: litigation
language: en
---

# Legal-Strategie Skill

> **Warning:** Strategy recommendations are advisory only. Final decisions
> rest with the licensed attorney handling the case.

## When To Use

- The user asks for a strategy recommendation for a specific case
- The user wants a risk assessment before filing
- The user needs procedural tactics (settlement vs. trial, timing)

## Protocol

### Step 1 — Gather Case Context

Search the brain for the case:
```
gbrain search "<case-title>" --type legal-case
```

Extract from the case page:
- Facts (Sachverhalt)
- Claims (Ansprüche)
- Defenses (Einwände)
- Evidence (Beweismittel)
- Opponent (Gegner)
- Jurisdiction (Rechtsgebiet)
- Court (Gericht)

### Step 2 — Analyze the Position

Strength assessment:
- **Strong position**: Clear facts, favorable precedent, strong evidence
- **Moderate position**: Mixed facts, some precedent, partial evidence
- **Weak position**: Unfavorable facts, unfavorable precedent, weak evidence

### Step 3 — Generate Strategy Options

Present 2-3 options with pros/cons:

**Option A: Full Litigation**
- Pros: Maximum recovery, precedent value
- Cons: Cost, time, uncertainty
- Best when: Strong position, high value

**Option B: Settlement Negotiation**
- Pros: Certainty, cost savings, speed
- Cons: Lower recovery, no precedent
- Best when: Moderate position, cost-sensitive

**Option C: Alternative Dispute Resolution**
- Pros: Confidentiality, creative solutions
- Cons: Non-binding (mediation), limited appeal
- Best when: Ongoing relationship, complex issues

### Step 4 — Risk Assessment

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| [Risk 1] | High/Med/Low | High/Med/Low | [Action] |
| [Risk 2] | High/Med/Low | High/Med/Low | [Action] |

### Step 5 — Recommended Next Steps

1. [Immediate action]
2. [Short-term action]
3. [Medium-term action]

## Output Format

```
## Rechtsstrategie — [Case Title]

### Positionsbewertung
[Strong / Moderate / Weak]

### Strategieoptionen

**Option A: [Name]**
[Description]
✅ Vorteile: [List]
❌ Nachteile: [List]

**Option B: [Name]**
...

### Risikoanalyse
| Risiko | Wahrscheinlichkeit | Auswirkung |
|---|---|---|
| ... | ... | ... |

### Empfohlene nächste Schritte
1. [Step]
2. [Step]
3. [Step]

---
⚠️ Dies ist eine strategische Orientierung. Die Entscheidung obliegt dem
mandatierten Rechtsanwalt.
```

## Anti-patterns

- Never promise a specific outcome
- Never ignore counter-arguments
- Never recommend illegal or unethical tactics
- Always flag risks
- Always present multiple options

## Contract

1. At least one concrete strategy is grounded in the matter's facts, claims and evidence.
2. Risks and procedural trade-offs are stated alongside each recommended step.
3. The output is decision support for the responsible lawyer, never autonomous advice.

## Anti-Patterns

- ❌ Recommending a tactic without tying it to the case facts/evidence in the brain.
- ❌ Presenting strategy as a guaranteed outcome.
- ❌ Ignoring the opponent profile or the cost/deadline constraints.

## Output Format

A strategy memo: situation · options with risk assessment · recommended next steps ·
open questions for the lawyer — marked AI-assisted, attorney decision required.
