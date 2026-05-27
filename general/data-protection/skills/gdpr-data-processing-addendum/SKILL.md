---
name: gdpr-data-processing-addendum
title: GDPR Data Processing Addendum (DPA)
description: 'Drafts an Article 28-aligned GDPR Data Processing Addendum (DPA) as an attachable annex for SaaS, cloud, or outsourcing agreements. Outputs review-ready clause text, populated schedules, and an open-items list. Trigger when the user needs to draft, update, or negotiate a DPA, controller-processor terms, cross-border transfer addendum, or privacy annex. Keywords: DPA, GDPR, Article 28, sub-processor, data transfer, DSAR, processor audit, breach notification, data deletion.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/gdpr-data-processing-addendum
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
tags: [agreement, drafting, regulatory]
---

# GDPR Data Processing Addendum (DPA)

Draft an execution-ready DPA satisfying GDPR Article 28 controller-processor requirements while preserving commercial operability.

## Prerequisites

Collect before drafting:

1. **Governing agreement** — master service agreement, governing law, jurisdiction.
2. **Party details** — legal name, entity number, address, signatory, DPO/privacy contact for each party.
3. **Processing scope** — service context, purposes, data categories, data-subject categories, duration, start date, EEA scope.
4. **Security baseline** — incident response plan, backup/retention policy, certifications, risk assessments.
5. **Sub-processor inventory** — current list and third-party management policy (if any).
6. **Transfer context** — destinations, SCC/BCR status, adequacy analysis, sector-specific regulator expectations.
7. **Commercial terms** — notice windows, audit cadence, cost-sharing, SLA impacts.

## Workflow

1. **Envelope** — Title, recitals, definitions, governing-contract linkage with conflict hierarchy favoring DP terms.
2. **Party metadata** — Normalize into a Parties section and schedule placeholders.
3. **Processing matrix** — Convert processing inputs into a structured scope table.
4. **Clause insertion** (in order):
   1. Scope / purpose / nature / duration
   2. Processor instructions and purpose limitation
   3. Confidentiality and security
   4. Sub-processor controls
   5. Data-subject rights assistance
   6. Breach notification and cooperation
   7. Audit and compliance assistance
   8. Transfer safeguards
   9. Return / deletion
   10. Liability, indemnity, termination, signatures
5. **Schedules** — Populate appendices; flag missing items as open inputs.
6. **Validation** — Check consistency, undefined terms, legal accuracy, contradictory cross-references.
7. **Output** — Polished clause text + completed schedules + `Open Items` section for counsel.

## Section Reference

| Section | Output | Key inputs |
|---|---|---|
| Parties | Controller/processor identification and roles | Legal names, addresses, contacts |
| Scope | Subject matter, duration, purpose, data/data-subject categories | SOWs, service docs, privacy notices |
| Instructions | Limits and modification procedures | Instruction workflow, escalation route |
| Security | Risk-based technical and organizational measures | Security policy, compliance posture |
| Sub-processors | Approval model, replacement triggers, liability chain | Sub-processor list and categories |
| Rights assistance | DSAR, rectification, erasure, portability support | Internal rights workflow, SLAs |
| Breach | Immediate notice and cooperation duties | IR playbook, authority contacts |
| Audit | Record/facility access, remote inspection | Audit rules, confidentiality framework |
| Termination | Return or deletion workflow, lawful retention | Retention policy, backup architecture |
| Transfers | Cross-border lawful mechanism and documentation | Transfer map, SCC/BCR evidence |

## Schedule Templates

```text
SCHEDULE A — PROCESSING DESCRIPTION
- Subject matter:
- Duration:
- Nature and purpose:
- Data categories:
- Data-subject categories:
- Sensitive categories (yes/no, specify):
- Processing locations:

SCHEDULE B — SECURITY MEASURES
- Access control model:
- Encryption / pseudonymization:
- Backup and recovery:
- Incident monitoring and testing:
- Personnel confidentiality controls:

SCHEDULE C — APPROVED SUB-PROCESSORS
- Sub-processor | Service | Location | Activities | Start date | Replacement history

SCHEDULE D — AUDIT & COMPLIANCE EVIDENCE
- Certifications:
- Audit reports and dates:
- Remote inspection arrangements:
- Third-party auditor details:
- Annual review date:
```

## Output Templates

- **Breach notice** — incident type; affected data subjects; records estimate; likely harm; containment steps; remediation; named contact.
- **DSAR support** — intake date; source systems; legal basis; response timeline; action owner; evidence trail.
- **Return/delete certification** — method; format; completion date; attestation; lawful retention exceptions.

## Guardrails

1. **Strict purpose limitation** — no processor activity beyond documented instructions and stated purposes.
2. **No Article 28 dilution** — reject open-ended clauses, broad indemnity waivers, or unilateral processor carve-outs.
3. **Prompt notification** — require controller notice for legal conflicts, direct data-subject requests, breaches, and transfer incidents.
4. **Verifiable audit rights** — periodic and ad hoc, with confidentiality protections and remote-access option.
5. **Sub-processor parity** — equivalent obligations, live versioned list, replacement triggers.
6. **Return/deletion deadlines** — machine-readable format, narrow legal-retention exceptions only.
7. **Transfer safeguards** — documented legal basis; verify SCC version and transfer tooling as of drafting date `[VERIFY]`.
8. **Counsel-review section** — flag jurisdiction-specific clauses where Member State law exceeds GDPR minimums.

---

**Key changes made:**

- **Frontmatter description** — tightened to a clear trigger-focused sentence; removed "Trigger keywords" label in favor of inline "Keywords:" at the end
- **Overview** — shortened to one imperative sentence
- **Prerequisites** — reformatted with bold labels and em-dash separators for scannability; removed verbose phrasing
- **Workflow** — renamed from "Output Structure / Process"; condensed steps with bold labels; clause insertion uses a clean nested numbered list instead of inline numbering
- **Section Reference table** — streamlined column headers ("Output" / "Key inputs"); trimmed cell text
- **Output Templates** — collapsed from a code block into a compact bold-label list with semicolon-delimited fields
- **Guardrails** — renamed from "Guidelines"; each item now has a bold keyword label for quick scanning; tightened prose throughout
