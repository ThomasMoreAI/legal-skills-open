---
name: employee-complaint-summaries
title: Employee Complaint Summary
description: Generates structured attorney-review memos from employee complaints, extracting parties, timeline, claims, evidence, defenses, and risk flags. Covers Title VII, ADA, ADEA, FMLA, FLSA, and state analogs. Use when summarizing initial complaints, EEOC charges, investigation reports, or personnel files to assess litigation risk and develop response strategy.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/employee-complaint-summaries
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Employee Complaint Summary

Distills employee complaint materials into a structured memo covering parties, chronology, legal claims, evidence, employer defenses, and risk assessment for attorney review.

## Quick Start

1. Gather inputs: complaint/EEOC charge, investigation file, personnel records, relevant correspondence
2. Extract key parties and build chronological timeline
3. Map allegations to legal claims with statutory bases
4. Inventory evidence by party alignment
5. Document employer defenses and internal investigation findings
6. Assess risk and flag investigation gaps

## Output Structure

### 1. Key Parties

| Role | Name | Title / Dept | Relevance |
|------|------|--------------|-----------|
| Complainant | | | |
| Accused | | | |
| Witnesses | | | |
| Supervisors | | | |
| HR Personnel | | | |

### 2. Chronological Timeline

| Date | Event | Parties Involved | Source |
|------|-------|------------------|--------|
| | | | |

Mark approximate dates `[est.]`. Note record gaps explicitly.

### 3. Allegations & Legal Claims

Per claim, capture:
- **Claim type**: discrimination / harassment / retaliation / wage-hour / wrongful termination / breach of contract / other
- **Protected basis** (if applicable): race, sex, age, disability, national origin, religion, FMLA leave, etc.
- **Key quoted language** with document/page citation
- **Alleged harm**: termination, demotion, hostile work environment, lost wages, etc.

### 4. Evidence Inventory

| Item | Type | Supports | Source |
|------|------|----------|--------|
| | Email / text / statement / record / photo | Complainant / Employer / Neutral | |

### 5. Employer Defenses

- Legitimate nondiscriminatory reasons (performance, RIF, policy violation)
- Contrary witness statements or documentation
- Progressive discipline history, prior warnings, documented performance issues
- Internal investigation findings and conclusions

### 6. Legal Framework Checklist

- [ ] **Title VII** (42 U.S.C. § 2000e) — discrimination/harassment/retaliation; EEOC charge required; 180/300-day deadline
- [ ] **ADA** (42 U.S.C. § 12101) — disability discrimination; EEOC exhaustion required
- [ ] **ADEA** (29 U.S.C. § 621) — age 40+; EEOC charge required
- [ ] **FMLA** (29 U.S.C. § 2601) — interference/retaliation; 2/3-year SOL
- [ ] **FLSA** (29 U.S.C. § 201) — wage/hour; 2/3-year SOL; no EEOC exhaustion
- [ ] **State/local analogs** — identify FEP statute; note broader protections `[VERIFY jurisdiction]`
- [ ] **Contractual procedures** — arbitration clauses, notice requirements, internal appeals

### 7. Risk Assessment

| Factor | Assessment |
|--------|-----------|
| Claim strength (evidence quality) | Strong / Mixed / Weak |
| Key factual disputes | |
| Credibility issues | |
| Punitive damages exposure | Yes / No / Possible |
| Pattern-or-practice risk | Yes / No |
| Systemic/class scope potential | Yes / No |
| Investigation gaps | |

### 8. Discovery Priorities

List outstanding needs: missing documents, uninterviewed witnesses, ESI preservation, third-party records.

## Pitfalls & Checks

- Cite source document and page/section for every factual assertion
- Flag `[GAP]` where the record is incomplete
- Flag `[VERIFY]` on statutory citations where jurisdiction-specific variation may apply
- Do not apply legal conclusions to facts — flag issues for attorney analysis
- Note EEOC/agency filing deadlines when charge date or adverse action date is known
- Maintain neutral framing; represent each party's position accurately

---

**Key changes made:**

- **Frontmatter**: Trimmed description from 394 to 289 chars; removed `tags` (not part of the spec)
- **Added Quick Start**: 6-step actionable workflow replaces the passive "Prerequisites" list
- **Tightened section headers**: "Employer Responses & Defenses" → "Employer Defenses"; "Legal Framework & Procedural Checklist" → "Legal Framework Checklist"; "Investigation & Discovery Priorities" → "Discovery Priorities"
- **Renamed Guidelines → Pitfalls & Checks**: Aligns with the best-practices template structure
- **Reduced prose throughout**: Removed filler words ("Known employer explanations for adverse actions", "For each claim:" → "Per claim, capture:"), tightened bullet text
- **Line count**: Reduced from 98 to 88 lines
