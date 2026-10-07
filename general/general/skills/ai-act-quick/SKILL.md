---
name: ai-act-quick
title: EU AI Act Quick Assessment
description: EU AI Act Quick Assessment — fast 15-25 minute triage for preliminary classification and compliance assessment. This skill should be used when the user asks to "do a quick AI Act assessment", "check if the AI Act applies to us", "run a preliminary classification", "do an AI Act triage", "quick check", "preliminary assessment", "Schnellprüfung", "Ersteinschätzung", or needs a fast initial assessment before committing to full analysis.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/ai-act-quick
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
sources:
- title: Compliance deadlines
  path: references/compliance-deadlines.md
- title: Jurisdiction flags
  path: references/jurisdiction-flags.md
- title: Quick decision tree
  path: references/quick-decision-tree.md
---

# EU AI Act Quick Assessment

Fast triage tool (15-25 minutes) for preliminary AI Act classification and compliance assessment. Produces a preliminary output and flags where a full AI Act assessment and qualified legal counsel are needed before relying on the result. This skill is self-contained: a "full assessment" means a documented, depth classification / role / obligation analysis and legal review — not another tool you need to install.

## Disclaimer (show at session start, do not block)

> **Important:** This is a preliminary AI Act assessment based on Regulation (EU) 2024/1689, designed for rapid triage. It is not legal advice and does not replace a full assessment — validate every "Likely" determination through a full, documented AI Act assessment (depth classification, role analysis, and obligation mapping) and qualified legal counsel before relying on it. Effective dates for high-risk obligations reflect the AI Omnibus 2026 postponement (Annex III: 2 December 2027; Annex I: 2 August 2028).

---

## Who this is for, and what kind of work this is

**Operator.** This triage can be run by a **non-lawyer — a product owner, compliance manager, or founder scoping AI Act exposure** — as well as by counsel. That is exactly why the output is preliminary by construction: if you are not a lawyer, your job is to **route the resulting card to qualified counsel**, not to treat "Likely Minimal" as an all-clear. No special AI fluency is assumed beyond describing the system in plain language.

**Work shape.** This is **bounded-transactional triage**: a single system run once through a fixed 6-gate sequence to produce a directional classification card — fast, pattern-matched, and deliberately shallow. It is the *opening* move of an accretive workflow, not the conclusion: a plausible high-risk or prohibited branch is meant to escalate into the full, documented assessment and counsel (see *Recommended Next Steps*), never to stop at the card. The speed is bought by narrowing scope, and the skill stays inside that narrow scope.

---

## When to Search the Web

**On activation — search for:**
```
EU AI Act latest enforcement updates [current year]
EU AI Act Commission guidelines status [current year]
```

---

## Quick Assessment Workflow

### Phase 1: Quick Context (Adaptive 2-Batch Flow)

Gather context through a conversational 2-batch approach. Maximum 2 interaction turns — 1 if the user is detailed, 2 if gaps remain.

#### Batch 1: Essential Questions (always asked)

Present these three questions with a natural, conversational welcome:

> **Let's get started with a quick EU AI Act assessment.**
>
> You can answer in your own words — a short paragraph, bullet points, whatever works. I'll ask follow-up questions only if I need more detail.
>
> **1. What does the AI system do?** (2-3 sentences: what it does, how it works at a high level, what outputs it produces)
>
> **2. Where is the system deployed?** (For reference: EU/EEA market, Switzerland with EU reach, outside EU but outputs used in EU, or no EU connection)
>
> **3. What is your organization's relationship to it?** (For reference: developed in-house, purchased/licensed, modified/finetuned, distribute/import, or evaluating for acquisition)

#### Coverage Analysis (internal — not shown to user)

After the user responds to Batch 1, silently check whether their answer covers each of the 8 required fields. Be generous with extraction — e.g., "German Mittelstand" covers both jurisdiction (DE) and organization size (medium); "CV screening tool" covers sector (HR/employment) and affected persons (employees/job applicants).

| # | Field | Extract from |
|---|-------|-------------|
| 1 | System description | Batch 1 Q1 |
| 2 | Deployment context | Batch 1 Q2 |
| 3 | Organization role | Batch 1 Q3 |
| 4 | Sector | Often inferable from system description |
| 5 | Affected persons | Often inferable from system description + sector |
| 6 | Modifications | Often inferable from organization role |
| 7 | Organization size | Sometimes mentioned in context |
| 8 | Jurisdiction(s) | Often inferable from deployment context |

Mark each field: **Covered** / **Partially covered** / **Not covered**.

#### Batch 2: Adaptive Follow-Up (only if gaps remain)

- **All 8 fields covered** → Skip Batch 2. Briefly confirm your extractions and proceed to Phase 2.
- **Gaps remain** → Send ONE follow-up message covering ONLY the missing or partially covered fields, conversationally framed. Do not re-ask what was already answered.
- **Partially covered fields** → Use confirmation prompts, not full re-asks. Example: "You mentioned healthcare — is this specifically in the medical devices sector?"
- **Unclear fields** → If still unresolvable after Batch 2, mark as `[UNCLEAR — proceeding with cautious assumptions]` and note the assumption made.

Example follow-up (if sector, size, and jurisdiction are missing):
> **Just a few more details to round out the picture:**
>
> - What sector does this fall into? (e.g., healthcare, financial services, HR/employment, education, public administration, other)
> - Roughly how large is your organization? (e.g., under 50 employees, 50-249, or 250+)
> - Which EU/EEA country or countries are involved?

#### Information Normalization (internal — before Phase 2)

Before proceeding to Phase 2, normalize all gathered information into the structured 8-field format so the Phase 2 gate sequence can reference fields consistently:

1. **System description** — free text
2. **Deployment context** — one of: EU/EEA market, Switzerland with EU reach, Outside EU but outputs used in EU, No EU connection
3. **Organization role** — one of: Developed in-house, Purchased/licensed, Modified/finetuned, Distribute/import, Evaluating
4. **Sector** — mapped to: Healthcare/medical devices, Financial services, HR/employment, Education, Law enforcement/justice, Critical infrastructure, Public administration, Consumer/retail, Other
5. **Affected persons** — one or more of: Employees/workers, Customers/consumers, Citizens/public, Students, Patients, Internal only
6. **Modifications** — one of: No modifications, Configuration within intended range, Finetuning/retraining, Changed intended purpose, Own brand applied
7. **Organization size** — one of: Micro (<10), Small (10-49), Medium (50-249), Large (250+)
8. **Jurisdiction(s)** — list of EU/EEA Member States or Switzerland

---

### Phase 2: Rapid Classification (6-Step Gate Sequence)

Read [references/quick-decision-tree.md](references/quick-decision-tree.md) for the condensed classification logic.

Process the answers through the 6-step gate sequence **internally** (do not ask additional questions unless critical information is missing). Output the result as a single assessment.

**Gate 1: Scope Check (Art. 2)**
- If deployment context is "No EU connection" → likely out of scope → note and proceed cautiously
- Check for military, personal use, pure R&D exclusions based on system description

**Gate 2: AI System Test (Art. 3(1))**
- Quick determination based on system description
- Apply simplified 3-question test: (1) machine-based? (2) infers/generates beyond rules? (3) influences environment?

**Gate 3: Prohibited Practice Screen (Art. 5)**
- Rapid screen based on system description and sector
- Flag any potential Art. 5 concern for detailed review

**Gate 4: High-Risk Assessment (Annex I + III)**
- Map sector + use case to Annex I/III categories
- Use sector answer as primary trigger indicator
- If Annex III triggered: quick Art. 6(3) exception check
- If the high-risk branch is plausible, flag that a **full Art. 6 high-risk assessment** — grounded in the Commission's Art. 6(3) / Annex III guidelines and the classification's documented reasoning — is needed before treating the system as in or out of the high-risk tier.

**Gate 5: GPAI Check**
- Based on system description: does it use a general-purpose AI model?
- If yes: note GPAI obligations

**Gate 6: Transparency Triggers (Art. 50)**
- Check for direct human interaction, synthetic content generation, emotion recognition, deep fakes

---

### Confidence — three bands, three behaviors

The `Confidence` field in the output is not decorative. Each level changes what you do with the determination, so an ambiguous call never reads the same as a clear one:

- **High** — the gates land cleanly on the facts given → **proceed**: present the card as a confident preliminary, with the normal "validate before compliance decisions" caveat.
- **Medium** — the classification turns on an assumption or a field marked partially covered → **surface and ask**: state the determination, but name the specific assumption it rests on and put the open question to the user rather than smoothing it over.
- **Low** — key facts are missing, the system sits on a risk-tier boundary, or an Art. 5 / Annex III branch is plausible but unconfirmed → **hand back**: lead with the uncertainty, flag the higher risk tier as the working assumption, and make escalation to the full assessment and counsel the headline, not a footnote.

When in doubt between two bands, pick the lower one.

---

### Phase 3: Preliminary Output

Generate a consolidated preliminary assessment using the following structure:

```markdown
## AI Act Quick Assessment — PRELIMINARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠ PRELIMINARY ASSESSMENT — Full analysis required for compliance decisions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

System:           [name/description]
Date:             [date]
Assessment Type:  PRELIMINARY (Quick Assessment)

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
CLASSIFICATION SUMMARY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI System (Art. 3(1)):     [Likely YES / Likely NO / Unclear — full test needed]
Scope (Art. 2):            [In scope / Likely excluded — Art. 2(x)]
Risk Tier:                 [Likely Prohibited / Likely High-Risk / Likely GPAI / Likely Limited / Likely Minimal / Unclear]
Classification Basis:      [Likely Art. 5(1)(x) / Likely Annex III Nr. X / Likely Art. 50 / Likely minimal]
Confidence:                [High / Medium / Low]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ROLE ASSESSMENT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Likely Role:               [Provider / Deployer / Quasi-Provider / Importer / Distributor]
Quasi-Provider Risk:       [None / Possible — [trigger]]
Key Concern:               [if any — e.g., finetuning may trigger Art. 25]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
TOP OBLIGATIONS (if high-risk or GPAI)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
| # | Obligation | Article | Urgency | Effort Estimate |
|---|-----------|---------|---------|-----------------|
| 1 | [top obligation] | [Art. X] | [Immediate/Short-term/Ongoing] | [Low/Medium/High] |
| 2 | [second obligation] | [Art. X] | [Immediate/Short-term/Ongoing] | [Low/Medium/High] |
| 3 | [third obligation] | [Art. X] | [Immediate/Short-term/Ongoing] | [Low/Medium/High] |
| 4 | [fourth obligation] | [Art. X] | [Immediate/Short-term/Ongoing] | [Low/Medium/High] |
| 5 | [fifth obligation] | [Art. X] | [Immediate/Short-term/Ongoing] | [Low/Medium/High] |

For ALL risk tiers:
| - | AI competence (Art. 4) | Art. 4 | Immediate (since Feb 2025) | Low-Medium |

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
COMPLIANCE TIMELINE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Applicable Deadline:       [2 Feb 2025 / 2 Aug 2025 / 2 Dec 2027 (Annex III — Omnibus) / 2 Aug 2028 (Annex I — Omnibus)]
Days Remaining:            [X days]
Urgency:                   [OVERDUE / CRITICAL / HIGH / MEDIUM / LOW]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
JURISDICTION FLAGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Jurisdiction-specific flags based on deployment country, e.g.:]
[DE: Works council co-determination likely required (BetrVG §87)]
[FR: CSE consultation required before deployment]
[Finance sector: BaFin/[regulator] AI model governance requirements apply]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FINANCIAL EXPOSURE (PRELIMINARY)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Maximum penalty:           [EUR XM or X% turnover — Art. 99(X)]
SME proportionality:       [Applies / Does not apply]
Penalty tier:              [Tier 1/2/3]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
FLAGS & WARNINGS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[List any flags, e.g.:]
[PROHIBITED PRACTICE RISK — Art. 5(1)(x) — immediate legal review required]
[QUASI-PROVIDER RISK — finetuning may trigger Art. 25]
[PROFILING DETECTED — may affect Art. 6(3) exception]
[GDPR OVERLAP — DPIA likely required under Art. 35 GDPR]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ASSESSMENT CONTEXT (carry forward to the full assessment / counsel)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
System: [name]
Classification: [risk tier]
Basis: [legal basis]
Role: [role]
Quasi-Provider: [risk level]
Sector: [sector]
Jurisdiction: [list]
Org Size: [size]
Art. 50: [applicable triggers]
GPAI: [yes/no, systemic risk]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
RECOMMENDED NEXT STEPS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Full classification with documented reasoning — re-run every gate at depth
   (Art. 2 scope, Art. 3(1) AI-system test, Art. 5 prohibited screen, Annex I/III
   high-risk with the Art. 6(3) exception analysis, GPAI, Art. 50), recording the
   legal basis for each determination.
   [Priority: HIGH / MEDIUM — based on preliminary findings]

2. Detailed role determination — confirm provider / deployer / quasi-provider /
   importer / distributor, including any Art. 25 quasi-provider trigger from
   fine-tuning, substantial modification, or own-branding.
   [Priority: HIGH if quasi-provider risk detected / MEDIUM otherwise]

3. Complete obligation mapping with owners (RACI) for the confirmed risk tier and role.
   [Priority: HIGH if high-risk / MEDIUM if limited risk]

4. Formal assessment documentation for the file — classification record
   (Prüfprotokoll), obligation/compliance register, and management briefing
   (Entscheidungsvorlage).
   [Priority: HIGH for regulatory files / MEDIUM for internal tracking]

5. Engage legal counsel for:
   [List specific areas requiring legal judgment]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠ This preliminary assessment provides directional guidance only. Every
  determination marked "Likely" requires validation through a full, documented
  AI Act assessment (steps 1–4 above) and legal review before it is relied on.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### Phase 4: Template Offer (Optional)

After presenting the preliminary assessment, offer:

> "Would you like me to generate a preliminary version of any of the following templates? These will be marked as preliminary and should be finalized after a full assessment."
>
> 1. **Classification Record (Prüfprotokoll)** — preliminary audit trail
> 2. **Compliance Register Entry** — preliminary obligation tracker
> 3. **Management Briefing (Entscheidungsvorlage)** — preliminary decision document

If requested, generate the chosen template from the assessment fields above using a standard structure
— **Classification Record:** system, role, risk tier, legal basis per gate, confidence, open
questions; **Compliance Register Entry:** obligation, article, owner, urgency, deadline, status;
**Management Briefing:** one-paragraph summary, risk tier + exposure, decision asked of management,
recommended next steps. Mark every output prominently as "PRELIMINARY — Full assessment recommended."

---

## Critical Reminders

1. **This is a triage tool** — always recommend a full, documented assessment for compliance decisions
2. **"Likely" is not "confirmed"** — preliminary determinations require validation
3. **Err on the side of caution** — if uncertain between risk tiers, flag the higher risk tier as possible
4. **Flag uncertainty explicitly** — the Confidence band drives behavior: High → proceed, Medium → surface the assumption and ask, Low → lead with the uncertainty and hand back (see *Confidence — three bands, three behaviors*)
5. **National requirements matter** — always flag jurisdiction-specific obligations using [references/jurisdiction-flags.md]
6. **Compliance timeline** — reference [references/compliance-deadlines.md] for deadline urgency
7. **Enforcement exposure (Art. 99)** — for penalty context: prohibited practices (Art. 5) up to **€35M or 7%** of total worldwide annual turnover, whichever is higher (Art. 99(3)); most other provider/deployer breaches up to **€15M or 3%** (Art. 99(4)); supplying incorrect/incomplete/misleading information to authorities up to **€7.5M or 1%** (Art. 99(5)); for SMEs and start-ups the **lower** of the fixed amount or the percentage applies (Art. 99(6))

## What this skill does not do

This section is a feature, not a disclaimer reflex — it tells the user when to escalate beyond the skill.

- **It is not legal advice and does not produce a compliance decision.** It is a rapid triage that yields "Likely" determinations only; it does not replace a full, documented AI Act assessment or qualified legal counsel.
- **It does not confirm a risk tier.** Prohibited-practice (Art. 5) and high-risk (Annex I/III + Art. 6(3)) determinations are flagged as *possible* and must be confirmed through depth analysis — a "Likely High-Risk" output is a prompt to investigate, not a classification to rely on.
- **It does not invent legal substance or citations.** Article and Annex references come from the reference files; where the inputs are too thin to support a determination, the skill marks the field `[UNCLEAR]` and proceeds on stated cautious assumptions rather than guessing.
- **It does not certify compliance or quantify actual fines.** Penalty figures are the Art. 99 statutory maxima for context, not a prediction of exposure in a given case.
- **It does not track live enforcement or guideline status.** It prompts a web search on activation because Commission guidelines and national enforcement are still developing; determinations are calibrated to the picture at authoring time.
- **It is self-contained at LegalQuants.** Where it refers to a "full assessment," that means the depth analysis and legal review described in the Recommended Next Steps — not a dependency on any other installed skill.

## Liability

This skill is provided **"as is" under the Apache License 2.0** — without warranties of any kind, and subject to the limitation of liability in §§ 7–8 of that license. It is not legal advice and creates no attorney–client relationship. To the fullest extent permitted by law, the author (Oliver Schmidt-Prietz, Rechtsanwalt, Germany) accepts no liability for any use of, or reliance on, this skill or its output; users use it at their own responsibility and are solely responsible for validating results and for their own compliance decisions.
