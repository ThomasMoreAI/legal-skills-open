---
name: hipaa-baa
title: HIPAA Business Associate Agreement (BAA)
description: 'Drafts HIPAA/HITECH-compliant Business Associate Agreements governing PHI/ePHI handling between covered entities and business associates. Covers Privacy Rule and Security Rule obligations, breach notification, subcontractor flow-downs, individual-rights support, and state-law overlays. Use when drafting or updating a BAA, negotiating vendor PHI access, or attaching HIPAA terms to a services agreement. Trigger keywords: BAA, business associate agreement, HIPAA contract, PHI vendor agreement, HITECH breach notice.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hipaa-baa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
tags: [agreement, drafting, regulatory]
---

# HIPAA Business Associate Agreement (BAA)

Produces a HIPAA/HITECH-compliant BAA tailored to services, PHI flow, and risk profile.

## Prerequisites

1. Party identities, entity types, jurisdictions, notice addresses.
2. Underlying services agreement/SOW with plain-language service description.
3. PHI data map: categories, ePHI vs. paper, systems, storage locations, data flows.
4. Regulatory overlays: state privacy/breach laws, 42 CFR Part 2, VA/military records.
5. Security posture: safeguards summary, risk assessment cadence, incident contacts.
6. Risk allocation: indemnity, insurance limits, liability caps.
7. Preferred timelines: breach notice deadline, cure period, termination notice.

## Output Structure

Draft sections in this order, filling placeholders from matter facts:

1. **Parties, Effective Date, Recitals** — basis for BA relationship
2. **Definitions** — HIPAA statutory terms + agreement-specific terms
3. **Permitted Uses/Disclosures; Prohibited Uses**
4. **Safeguards** — Privacy Rule + Security Rule
5. **Breach/Incident Notification**
6. **Subcontractor Flow-Downs**
7. **Individual Rights Support**
8. **Government Access / Compliance Cooperation**
9. **Term/Termination; Return/Destruction of PHI**
10. **Indemnity/Insurance; Liability Allocation**
11. **Miscellaneous** — amendment, governing law, notices, assignment, severability, survival
12. **Signatures; Exhibits** — implementation checklist

### Definitions

Include all applicable terms with statutory citations:

| Term | Source |
|---|---|
| Protected Health Information (PHI) | 45 CFR 160.103 [VERIFY] |
| Electronic PHI (ePHI) | 45 CFR 160.103 [VERIFY] |
| Breach | 45 CFR 164.402 [VERIFY] |
| Security Incident | 45 CFR 164.304 [VERIFY] |
| Unsecured PHI | HHS Guidance / NIST [VERIFY] |
| Designated Record Set | 45 CFR 164.501 [VERIFY] |
| Required by Law, Individual, Secretary, Subcontractor, Use, Disclosure | HIPAA definitions [VERIFY] |

### Required Clauses (Minimums)

- [ ] Permit/limit uses and disclosures to services + required by law
- [ ] Prohibit uses/disclosures that would violate Privacy Rule if done by covered entity
- [ ] Require safeguards: Privacy Rule + Security Rule (45 CFR 164.308/310/312) [VERIFY]
- [ ] Require breach notification and security incident reporting
- [ ] Flow-down to subcontractors with same restrictions/conditions
- [ ] Support individual access/amendment/accounting rights
- [ ] Make records available to HHS Secretary for compliance review
- [ ] Provide return/destruction of PHI or extend protections if infeasible
- [ ] Allow termination for material breach

### Permitted and Prohibited Uses

| Topic | Drafting Requirement |
|---|---|
| Core permitted uses | Tie each to a service obligation; include data aggregation if applicable |
| Management/admin uses | Allow only if required by law or with recipient assurances |
| Required by law | Permit with notice to covered entity where allowed |
| Minimum necessary | Require policies; define exceptions (treatment, disclosures to CE) |
| Prohibited uses | No sale of PHI; no marketing without authorization; no psychotherapy notes unless authorized |

### Safeguards

- [ ] **Administrative**: security official, access management, workforce training, incident response, contingency plan
- [ ] **Physical**: facility access controls, workstation use/security, device/media disposal
- [ ] **Technical**: unique IDs, emergency access, auto-logoff, encryption, audit controls, integrity controls, authentication, transmission security
- [ ] **Risk analysis**: documented, updated regularly, remediation tracked

### Breach / Incident Notification

| Element | Requirement |
|---|---|
| Deadline | "Without unreasonable delay," capped in days (e.g., 10 business days) |
| Discovery standard | Knowledge or would-have-known with reasonable diligence |
| Content | Dates, description, PHI types, affected count, mitigation steps, contact info |
| Supplemental updates | Required as new facts emerge |
| Incident logs | Maintain and provide periodic summaries of non-breach incidents |

### Individual Rights Support

| Right | BA Obligation |
|---|---|
| Access | Provide Designated Record Set data within X days per 45 CFR 164.524 [VERIFY] |
| Amendment | Implement amendments within X days; flow-down to subcontractors |
| Accounting | Maintain disclosure logs per 45 CFR 164.528 [VERIFY] |
| Restrictions / confidential comms | Implement covered entity instructions |

### Subcontractors

- [ ] Prior written approval required (if negotiated)
- [ ] Written BAA-equivalent flow-down with identical restrictions
- [ ] Ongoing monitoring/audit rights and prompt notice of issues

### Termination / PHI Disposition

- [ ] Term tied to services; survives until PHI returned/destroyed
- [ ] Cure period and immediate termination triggers for material breach
- [ ] Return/destroy within X days; certification of destruction
- [ ] If infeasible: extend protections, limit further uses/disclosures

### Exhibit: Implementation Checklist

- [ ] Contact points and escalation path
- [ ] Security program baseline and audit cadence
- [ ] Subcontractor list and approvals
- [ ] Incident response tabletop schedule

## Guidelines

- Match obligations to actual operational capability — do not promise controls the BA cannot meet.
- Align with the underlying services agreement; reconcile conflicting terms.
- Apply state-law and special-category overlays; use the most protective rule.
- Use defined terms consistently; avoid ambiguity in permitted uses.
- Mark uncertain citations with `[VERIFY]`.
- Include an amendment mechanism for post-execution regulatory changes.

## Troubleshooting

- **Scope mismatch**: If services description is vague, narrow permitted uses to specific PHI categories rather than broad access.
- **Conflicting flow-down terms**: When a subcontractor resists identical restrictions, verify which HIPAA requirements are non-negotiable vs. commercially flexible.
- **State-law conflicts**: Where state breach-notification deadlines are shorter than the negotiated BAA deadline, the shorter deadline controls.
- **Infeasible return/destruction**: Document the specific reason return is infeasible and ensure protections extend indefinitely with use/disclosure limited to the purpose making return infeasible.

---

Key changes from the original:

- **Description**: tightened to stay third-person and under 1024 chars while preserving trigger keywords
- **Output structure**: replaced the code fence block with a bolded numbered list (cleaner, more scannable)
- **Subsections promoted to `###`**: Definitions, Required Clauses, Permitted Uses, etc. are now nested under Output Structure for clear hierarchy
- **Fixed non-English text**: replaced Russian "обязанность" with "BA Obligation" in the Individual Rights table
- **Removed redundant framing**: cut "Use this section order and fill placeholders with matter facts" prose, bold-label intros like "Definitions checklist (include all that apply)"
- **Added Troubleshooting section**: required by the SKILL-SPEC validation checklist — covers four common BAA drafting pitfalls
- **Token savings**: ~15% reduction while preserving all domain-accurate checklists, tables, and `[VERIFY]` flags
