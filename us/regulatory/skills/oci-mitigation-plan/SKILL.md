---
name: oci-mitigation-plan
title: OCI Mitigation Plan
description: Drafts FAR 9.5-compliant Organizational Conflict of Interest mitigation plans for federal government contractors. Analyzes unequal access, impaired objectivity, and biased ground rules conflicts, then produces firewalls, recusals, compliance architecture, and certifications. Use when responding to solicitations with OCI concerns, preparing proposals requiring OCI disclosure, or drafting conflict mitigation documents.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/oci-mitigation-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: regulatory
language: en
---

# OCI Mitigation Plan

Produces a complete OCI mitigation plan under FAR Subpart 9.5 covering conflict identification, tailored mitigation strategies, compliance architecture, and binding certifications.

## Prerequisites

Gather before drafting:

1. **Contractor identity** — legal name, corporate structure, parent/subsidiary relationships, UEI, CAGE code
2. **Procurement details** — solicitation/contract number, agency, SOW, contract type, performance period
3. **Prior government work** — relevant contracts, advisory roles, non-public information access
4. **OCI correspondence** — prior communications with the contracting officer
5. **Organizational relationships** — teaming agreements, subcontractors, equity interests, consulting arrangements

## Quick Start

1. Extract key data from uploaded documents (corporate structure, solicitation scope, prior contracts, non-public info accessed, personnel with dual exposure, prior OCI communications)
2. Analyze each FAR 9.5 conflict category for materiality
3. Draft tailored mitigation measures for each identified conflict
4. Build compliance and monitoring framework
5. Include binding certification by authorized corporate officer

## Output Structure

### Section 1: Executive Summary

- Contractor identification (name, UEI, CAGE, corporate family)
- Procurement identification (solicitation #, agency, scope)
- Legal basis (CO request / proposal requirement / voluntary disclosure)
- Prior OCI correspondence with dates
- Summary table: identified conflicts → proposed mitigations

### Section 2: Conflict Identification & Materiality

Analyze each FAR 9.5 category:

| Category | FAR Basis | Key Questions |
|---|---|---|
| **Unequal Access to Information** | 9.505-4 | Non-public info obtained? Through which contracts? Still competitively useful? |
| **Impaired Objectivity** | 9.505-3 | Advising on matters with financial interest in outcomes? Equity/teaming with benefiting entities? |
| **Biased Ground Rules** | 9.505-1, 9.505-2 | Drafted specs, SOW, or evaluation criteria? Prior work shaped requirements? |

For each conflict, document:
1. Factual narrative (contracts, dates, personnel)
2. Government interests at risk and competitive implications
3. Materiality rating (substantial vs. theoretical)
4. Whether appearance of impropriety alone warrants mitigation

### Section 3: Mitigation Strategies

Tailor measures to each conflict from this toolkit:

**Organizational Firewalls** — physical separation, electronic controls (separate networks, restricted access), administrative controls (separate reporting chains, NDAs), personnel assignment criteria, breach detection protocols

**Personnel Recusal** — objective recusal criteria, documentation/approval process, backfill procedures, communication of restrictions

**Disclosure & Transparency** — categories subject to ongoing disclosure, notification timeframes, regular reporting cadence, government recipients and format

**Business Activity Restrictions** (when firewalls insufficient) — non-competition commitments, information use restrictions, divestiture/relationship termination, scope reductions

### Section 4: Implementation & Compliance

**Governance**: Designate OCI Compliance Officer with independence from program management, direct executive access, authority to halt activities.

**Training**: All contract personnel receive initial + annual training on FAR OCI principles and specific restrictions. Supervisors, BD staff, and new hires to affected programs receive targeted training. Require signed acknowledgments.

**Monitoring & Audit**: Active verification (access logs, recusal records, firewall integrity), compliance reviews at defined intervals, documented investigation reports.

**Periodic Certifications**: Quarterly certifications to CO affirming plan effectiveness, disclosing violations/remediations, flagging changed circumstances. Senior official signs with due diligence.

**Change Management**: Define material change triggers (reorgs, personnel moves, new relationships, scope changes). Prompt CO notification. Written OCI assessment before modifications.

**Corrective Action**: Immediate containment → investigation → root cause → discipline → systemic fix → full CO disclosure with remediation plan.

### Section 5: Binding Certification

Draft certification by authorized corporate officer:

```
CERTIFICATION

I, [Name], [Title], of [Contractor Legal Name], hereby certify that:

1. The foregoing OCI analysis is complete and accurate after reasonable inquiry;
2. All material facts bearing on potential conflicts have been disclosed;
3. [Contractor] commits to implementing mitigation measures as described;
4. This plan, upon government acceptance, constitutes a binding contractual obligation;
5. Non-compliance may result in: termination for default, suspension/debarment,
   referral for investigation, and all other available remedies.

_____________________________
Name / Title / Organization / Date
```

Certifying official must have binding authority (corporate officer or equivalent). For subsidiaries, assess whether parent ratification is needed.

## Checks

- **No boilerplate** — every mitigation must be tailored to the identified conflict; generic firewalls without factual grounding will be rejected
- **Appearance matters** — mitigate conflicts creating appearance of impropriety even if actual harm is unlikely
- **Temporal scope** — address both performance-period and post-performance residual conflicts
- **Agency supplements** — flag when DFARS, NFS, or other supplements impose additional requirements [VERIFY citations against current regulations]
- **Regulatory basis** — FAR 9.504 (CO responsibilities), 9.505 (representations), 9.505-1 through 9.505-4 (specific conflict types)
- **Tone** — professional, candid, formal; avoid defensive posturing
- **Audience** — contracting officers, agency counsel, IG offices, potentially GAO
- **Dual purpose** — satisfy legal/regulatory requirements AND serve as operational implementation guide
