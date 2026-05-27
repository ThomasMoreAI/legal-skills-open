---
name: discovery-and-bill-of-particulars
title: Demand for Discovery and Bill of Particulars
description: Drafts a combined Demand for Discovery and Bill of Particulars for U.S. criminal or civil litigation. Extracts case details, identifies underspecified allegations or evidence gaps, and produces numbered discovery requests paired with particularization demands. Use after initial pleadings or return date when charges or claims lack specificity, evidence is opaque, or trial-preparation disclosures are incomplete. Trigger keywords include discovery demand, bill of particulars, motion to compel, FRCP 16, FRCP 26, FRCP 33, FRCP 34, FRCP 37, particularity.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/discovery-and-bill-of-particulars
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Demand for Discovery and Bill of Particulars

Drafts a court-ready pleading combining targeted discovery demands with a bill of particulars to force disclosure, narrow vague theories, and preserve an enforceable compliance record.

## Prerequisites

1. **Jurisdiction and court** — court, division/department, case number, local rules, standing filing/formatting orders
2. **Case posture** — criminal, civil, or hybrid; current procedural stage
3. **Case file** — charging document or complaint, prior pleadings, motions, stipulations, existing discovery responses
4. **Information gaps** — ambiguous allegations or missing disclosures blocking trial preparation
5. **Privilege constraints** — potential privilege categories and any protective-order limitations
6. **Enforcement posture** — preferred path: meet-and-confer, motion to compel, fee/sanction relief

If any prerequisite is missing, pause and ask — do not assume or fill gaps.

## Output Structure

### 1. Regime Selection

Identify the governing track before drafting:

| Track | Governing Rules | Baseline Deadline |
|-------|----------------|-------------------|
| Criminal | Fed. R. Crim. P. 16; 7(f) + local rules | Local rule/time limit [VERIFY] |
| Federal civil | FRCP 26(b)(1), 26(e), 26(g), 33, 34, 36, 37 | 30 days from service [VERIFY] |
| State | State procedure + local rules | State-specific [VERIFY] |

### 2. Case Information Block

| Field | Value |
|-------|-------|
| Court | [jurisdiction] |
| Judge/department | [if required] |
| Plaintiff/Prosecution | [name] |
| Defendant | [name] |
| Case number | [xxxx] |
| Document title | Demand for Discovery and Bill of Particulars |
| Strategic objective | [narrow charges / obtain disclosure / prepare defenses] |

### 3. Authority and Need

- State party status, case stage, and necessity for relief
- Criminal: cite Fed. R. Crim. P. 16, 7(f) for disclosure and particularized charge notice
- Civil: cite FRCP 26(b)(1), 33, 34, 36, 37 for relevance, specificity, and sanctions path
- Include proportionality statement; affirm requests are not harassing or overbroad

### 4. Discovery Demands

Numbered requests with strict specificity:

| Req. | Category | Custodian/Source | Time Range | Format | Rationale |
|------|----------|-----------------|------------|--------|-----------|
| 1 | Documents/ESI | [party + affiliates] | [from/to] | Native + metadata | [defense use] |
| 2 | Communications | [emails/texts/notes] | [from/to] | Native + index | [defense use] |
| 3 | Witness IDs | [trial/public witnesses] | [if ongoing] | Contact + scope | Trial prep/notice |
| 4 | Expert materials | [experts] | [all] | CVs, reports, data, opinions | Rebuttal/cross prep |

Per-request template:

```
[No.] Request for [documents | communications | identity | expert materials]:
Request:
Ground:
Response format:
Privilege carve-out:
```

### 5. Bill of Particulars

Per-demand template:

```
Demand [No.]:
Allegation to specify:
Exact information required:
Reason tied to element/issue:
```

**Criminal particulars:**
- Acts constituting each charged offense
- Exact dates, times, and locations
- Identified participants, co-conspirators, or accomplices
- Manner and means for each offense
- Nexus to venue, elements, and defenses

**Civil particulars:**
- Statutory or contractual provisions breached and breach conduct
- Itemized damages per category with calculation basis
- Each referenced document described with production-level specificity

### 6. Compliance and Deadlines

- State response deadline and service method
- Require complete, verified responses per local/operative rules
- Require supplementation duty as new information becomes known
- Include escalation sequence: meet-and-confer → motion to compel → sanctions/preclusion/fee recovery
- Use explicit court-ready language for incomplete, evasive, or untimely responses

### 7. Certification and Service

```
I certify under [applicable rule] that this demand is grounded in law,
not interposed for delay or harassment, and not unduly burdensome.

Attorney:
Bar/Firm/Contact:
/s/ [Attorney]
Date:

Certificate of Service:
Served on [party/counsel] via [ECF/e-service/mail]
Date/time/method:
```

## Jurisdiction-Specific Compliance

- [ ] Governing rules identified for correct track (criminal / federal civil / state)
- [ ] Local captioning, formatting, and e-filing requirements followed
- [ ] Response deadlines verified against applicable rules — no invented dates
- [ ] Nomenclature matches jurisdiction (e.g., "demand" vs. "motion" vs. "request")
- [ ] Service method complies with local practice

## Guidelines

- Every request must map to a litigation purpose — no fishing expeditions
- Use parallel phrasing for criminal and civil tracks; never mix standards without citing the governing rule
- Separate factual requests from relief/remedy requests to reduce objections
- Avoid vague terms; include exact relief language to build an escalation-ready record
- Acknowledge privilege and nonparty constraints in each request where applicable
- Eliminate duplicate or mutually inconsistent requests
- Mark jurisdictional assumptions with `[VERIFY]` when local law is uncertain
- All citations must be verified — do not hallucinate rule numbers, deadlines, or case law

---

Key improvements from the original:

- **Frontmatter description** rewritten in third-person with clearer trigger guidance
- **Prerequisites** now use bold labels with dash separators matching codebase convention; added the "pause and ask" instruction
- **Regime selection** condensed from a 5-column matrix to a focused 3-column table
- **Case information** converted from a code block to a proper table
- **"Final control checks"** section (step 8) removed — those checks are now folded into a dedicated **Jurisdiction-Specific Compliance** checklist section with checkboxes, matching the pattern used by `abstract-of-judgment` and `alibi-notice`
- **Certification block** fixed the "harrasment" typo
- **Guidelines** tightened to 8 focused bullets with an added hallucination guard
- Overall ~20% shorter while preserving all legal substance
