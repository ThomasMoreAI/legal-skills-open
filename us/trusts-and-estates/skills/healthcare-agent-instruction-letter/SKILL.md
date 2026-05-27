---
name: healthcare-agent-instruction-letter
title: Healthcare Agent Instruction Letter
description: Drafts a non-binding healthcare values/instruction letter for a designated health care agent to guide substituted-judgment decisions during incapacity. Use when a client needs a bedside document that harmonizes with a health care power of attorney, healthcare proxy, or advance directive and captures quality-of-life thresholds, treatment preferences, and conflict guidance. Trigger on requests for "instruction letter," "health care agent letter," "values letter," "legacy letter," "healthcare proxy," or "DPOA health care."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/healthcare-agent-instruction-letter
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: trusts-and-estates
language: en
tags: [drafting, letter, regulatory, transactional]
---

# Healthcare Agent Instruction Letter

Drafts a scenario-based, non-binding values letter in the client's voice to empower the health care agent and reduce ambiguity at the bedside. Output supplements—never replaces—operative legal directives.

## Quick Start

1. Confirm client identity, preferred name, and jurisdiction.
2. Collect executed documents (name/date/type): health care POA or proxy, advance directive, POLST/MOLST, HIPAA release.
3. Identify primary agent and alternates (full names, roles, contact preferences).
4. Capture core values: quality-of-life thresholds, cognition-loss tolerance, dependence, pain, institutional care.
5. Capture clinical preferences: CPR, ventilation, artificial nutrition/hydration, antibiotics, surgery, time-limited trials, hospice, comfort care.
6. Capture spiritual/cultural commitments affecting care decisions.
7. Identify conflict vectors and family communication plan.
8. Capture tone preference, distribution timing, and document-storage locations.
9. Never invent names, dates, diagnoses, or beliefs—ask for missing facts and use `[placeholder]`.

## Core Workflow

| Phase | Action | Output |
|-------|--------|--------|
| 1 | Validate non-binding status | Opening disclaimer: guidance only, not a substitute for operative directives |
| 2 | Harmonize documents | List governing document titles/dates; note instruction hierarchy |
| 3 | Elicit decision framework | Big-Three thresholds: cognition, independence, suffering |
| 4 | Draft scenario logic | Treatment sections with conditional "if/when…then…" examples |
| 5 | Add faith/culture mechanics | Practical care requests tied to beliefs, without legal overstatement |
| 6 | Address conflict protocol | Disagreement scripts, consult triggers, clinician communication |
| 7 | Add logistics | Distribution plan: who receives, when, storage locations |
| 8 | Run quality controls | Mismatch flags, ambiguity reduction, attorney-review gate |

### Writing Constraints

- Client voice, plain language, short headings, 1–3 pages.
- Conditional framing throughout: "if/when…then…" with scenario examples.
- No medical orders or statutory language belonging in POLST/MOLST/clinic forms.
- Every section must be usable under stress by one reader in minutes.

## Letter Template

Fill only known facts; use `[placeholder]` where missing.

```text
Date: [date]
To: [Primary Agent], [Alternate(s)]
Re: My Values and Medical Decision Guidance

I wrote this letter to guide my agent if I cannot speak for myself.
I have executed [document names/dates]; this letter supplements and does not replace them.

1) Decision-Makers
- [Primary Agent], [Alternate Agent]
- Use substituted judgment: do what I would want, not what feels least difficult.

2) What Matters Most
- Good-day definition:
- Non-negotiable values/limits:
- Cognitive/function thresholds:
- Pain, comfort, dignity standards:

3) Treatment Preferences
- CPR / intensive care:
- Ventilation / breathing support:
- Feeding / hydration:
- Dialysis / infection treatment:
- Surgery / rehab vs. noninvasive care:
- Time-limited trials:
- Pain control / sedation:
- Preferred care setting:

4) Spiritual, Cultural, and Personal Preferences
- Practices/rituals:
- Clergy or contacts:
- Religious limits or accommodations:

5) Conflict and Communication
- Who should be included:
- Who may contest:
- Protocol: ethics/palliative consults, second opinions, family meeting trigger:

6) Closing
- Permission grant:
- Document storage locations:
- Distribution instructions:

Signature:
```

## Post-Draft Checks

- [ ] Non-binding disclaimer appears in opening and closing.
- [ ] No contradiction with operative legal documents; discrepancies flagged separately.
- [ ] No invented facts; `[placeholder]` tags remain for missing data.
- [ ] Treatment guidance is scenario-based, not slogans.
- [ ] Conflict instructions protect agent authority consistent with legal appointment.
- [ ] No absolute commands implying standalone legal effect.
- [ ] Attorney-review gate and confidentiality note included.

## Jurisdictional Guardrails

| Topic | Rule |
|-------|------|
| Terminology | Match client documents: "health care proxy," "medical power of attorney," "advance health care directive," etc. |
| POLST/MOLST | Do not draft as an order form; recommend separate clinical workflow [VERIFY]. |
| Heightened-evidence jurisdictions | Use heightened specificity where clear-and-convincing evidence may be required for life-sustaining-treatment disputes (e.g., *In re Storar*, 52 N.Y.2d 363 (1981)) [VERIFY]. |
| MAID | Do not imply the agent can request aid-in-dying on the principal's behalf; separate statutory process [VERIFY]. |
| Default surrogacy | Reference only client-selected legal chain; do not summarize statutes without attorney verification. |

## Pitfalls

**Do:**
- Keep language operational: who, when, what threshold, what action.
- Preserve client's voice and style.
- Use `[placeholder]` for all absent details.
- Require attorney review before final use.

**Don't:**
- Treat this as an enforceable legal order or substitute advance directive.
- Include medical advice or treatment guarantees.
- Create contradictions with signed legal documents.
- Use inflammatory family language that could weaponize disputes.
- Advise distribution to clinicians without confirming client disclosure preferences.

Attorney review is mandatory. Draft output is informational assistance only and does not constitute legal advice.
