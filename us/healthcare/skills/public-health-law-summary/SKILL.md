---
name: public-health-law-summary
title: Public Health Law Summary
description: Generates structured, plain-language summaries of public health legislation and case law with Bluebook citations. Use when summarizing health statutes, vaccination mandates, emergency health powers, disease surveillance law, health equity legislation, or healthcare regulations for agencies, providers, or policy advisors.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/public-health-law-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# Public Health Law Summary

Produces accessible, actionable summaries of legislation or case law affecting public health policy. Outputs are structured for government agencies, healthcare providers, and policy advisors.

## Quick Start

Before summarizing, confirm three things:

1. **Source** — official statutory text, case opinion, or regulatory action
2. **Jurisdiction** — federal, state, or local scope
3. **Audience** — agency staff, clinicians, policy advisors, or general public

## Summary Structure

### 1. Header Block

| Field | Legislation | Case Law |
|-------|------------|----------|
| Title | Statute title | Full case name |
| Body | Legislature + chamber | Court name + level |
| Date | Enactment/effective date | Decision date |
| Jurisdiction | Federal/state/local | Circuit/district/state |
| Citation | Bill no., public law no., statutory cite | Case cite, docket no. |
| Procedural posture | N/A | Appeal status, history |

All citations in **Bluebook format** with links to authoritative sources (congress.gov, state legislature sites, PACER).

### 2. Background & Context (1-2 paragraphs)

- Public health crisis, policy gap, or litigation trigger
- Prior legal framework being modified or interpreted
- Key stakeholders and interests

### 3. Core Legal Analysis

**Legislation:** principal provisions in plain language, defined terms, new authorities or restrictions, funding mechanisms.

**Case law:** precise holding with plain-language explanation, key legal reasoning, concurrences/dissents only if they signal doctrinal shifts.

### 4. Public Health Areas Affected

Tag all that apply with brief impact explanation:

- Disease surveillance & reporting
- Vaccination requirements
- Environmental health standards
- Healthcare access & coverage
- Emergency powers
- Privacy / health data (HIPAA, state equivalents)
- Health equity & social determinants
- Controlled substances / behavioral health
- Food & drug safety

### 5. Practical Implications

| Stakeholder | Key Impacts |
|-------------|-------------|
| Government agencies | New duties, authorities, compliance deadlines |
| Healthcare providers | Clinical practice changes, reporting obligations |
| Patients / public | Rights, access, protections |
| Regulated entities | Compliance requirements, penalties |

Flag ambiguities requiring further regulatory guidance.

### 6. Scope & Limitations

- Populations, geographies, conditions **covered vs. excluded**
- Sunset provisions or expiration dates
- Conflicts with existing law — which provisions control
- Pending challenges or anticipated amendments
- **Cases only:** precedential scope (binding vs. persuasive)

### 7. Implementation

**Legislation:** effective date, phased schedule, responsible agencies, rulemaking timelines, enforcement mechanisms.

**Case law:** finality and appeal status, remand instructions, agency compliance obligations.

### 8. Forward-Looking Analysis

- Fit within broader trends (federalism, individual rights vs. collective health, health equity)
- Likely regulatory or legislative responses
- Stakeholder action items
- Related pending legislation or litigation to monitor

## Pitfalls & Checks

- **Plain language first** — define legal terms on first use; connect to public health practice
- **Bluebook citations required** — mark any unverified citation with `[VERIFY]`
- **No legal advice** — frame as informational summary, not counsel
- **Objectivity** — present without advocacy; note competing interpretations
- **Jurisdiction clarity** — distinguish federal from state authority; note preemption issues
- **Link to sources** — provide URLs to official government or court opinion databases
