---
name: itar-technology-control-plan
title: ITAR Technology Control Plan
description: Drafts an ITAR Technology Control Plan (TCP) for U.S. export control compliance under 22 CFR 120-130. Use when a user needs to create or update a TCP, export control program, or deemed-export compliance plan. Trigger on mentions of ITAR, TCP, DDTC, USML, deemed export, technical data, or defense article in a compliance-planning context.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/itar-technology-control-plan
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: sanctions
language: en
tags: [drafting, memo, research]
---

# ITAR Technology Control Plan

Produces an organization-specific, auditable TCP covering USML scoping, technical data controls, U.S. person screening, deemed-export safeguards, cybersecurity, training, audits, and incident response.

## Prerequisites

Collect before drafting:

1. **Org profile** — entity names, DDTC registration status, empowered official, compliance contacts.
2. **Programs & scope** — contracts, USML categories, items/technical data, facility list.
3. **People & access** — personnel roster, foreign nationals, visitor workflows, subcontractors.
4. **Systems & storage** — IT architecture, data repos, collaboration tools, physical storage.
5. **Authorizations** — licenses/agreements (DSP-5, DSP-73, TAA, MLA), CJ determinations, prior disclosures.
6. **Existing policies** — security, HR screening, IT, visitor control, incident response, records retention.

## Quick Start

1. Gather all prerequisites; flag gaps early.
2. Draft each required section (see Section Outline below).
3. Populate the role matrix, inventory, and training tables with org-specific data.
4. Mark every regulatory citation with [VERIFY] for counsel review.
5. Attach appendices (forms, checklists, facility maps, access roster).
6. Route for empowered-official approval and signature.

## Required Sections

| # | Section | Key Content |
|---|---------|-------------|
| 1 | Purpose & Authority | TCP applicability; cite ITAR 22 CFR 120-130 [VERIFY]. |
| 2 | Definitions | Defense article, technical data, export, U.S. person, deemed export — with citations [VERIFY]. |
| 3 | Scope | Programs/contracts, USML categories (22 CFR 121.1) [VERIFY], facilities, remote-work boundaries. |
| 4 | Roles & Governance | Empowered official, compliance officer, IT/security, HR, program owners. |
| 5 | Classification & Inventory | USML mapping, CJ workflow (22 CFR 120.4) [VERIFY], marking, version control. |
| 6 | Access Controls | U.S. person verification, badge logic, visitor escorts, need-to-know. |
| 7 | IT & Cybersecurity | Segmentation, MFA, encryption, logging, device/media restrictions. |
| 8 | Handling & Transmission | Storage rules, secure transfer, travel, remote-access constraints. |
| 9 | Training | Initial + annual; role-based modules; completion records. |
| 10 | Audits & Monitoring | Annual audits, trigger-based reviews, corrective actions. |
| 11 | Incident Response | Containment, investigation, voluntary disclosure (22 CFR 127.12) [VERIFY]. |
| 12 | Records & Retention | 5-year retention (22 CFR 122.5) [VERIFY]; record types, custody. |
| 13 | Revision Control | Versioning, approvals, distribution, acknowledgment. |
| — | Appendices | Forms, checklists, logs, access roster, facility maps. |

## Role Responsibilities

| Role | Key TCP Duties |
|------|---------------|
| Empowered Official | Approves TCP; oversees disclosures and licensing. |
| Export Compliance Officer | Maintains TCP; coordinates audits/training; classification oversight. |
| IT/Security | Implements segmentation, logging, encryption. |
| HR | U.S. person verification; onboarding/offboarding workflow. |
| Program Manager | Enforces scope, need-to-know, reporting. |

## Core Controls

### Access

- Only verified U.S. persons may access controlled areas/systems.
- Visitor pre-approval + escort required; sanitize workspaces before entry.
- Deemed-export prevention: cover/remove technical data, restrict conversations near foreign persons.

### U.S. Person Verification (appendix checklist)

- Verify with original documents (passport, I-551, asylum/refugee/TPS evidence) [VERIFY].
- Record verifier, date, document type, expiration, re-verification schedule.
- Deny access until verification is completed and logged.

### Cybersecurity Baseline

- Segmented network for ITAR data — no routing to general networks.
- MFA + least-privilege for all access.
- Encryption at rest and in transit (AES-256 or equivalent) [VERIFY].
- Prohibit personal devices, removable media, consumer cloud storage.

### Transmission

- No standard email for ITAR data.
- Approved secure transfer only; verify recipient authorization and need-to-know.
- Confirm export authorization before any foreign disclosure.

### International Travel

- Pre-approval and licensing for temporary exports (e.g., DSP-73) [VERIFY].
- No access to ITAR data abroad without specific authorization.

## Training Matrix

| Audience | Frequency | Topics |
|----------|-----------|--------|
| All with access | Initial + annual | ITAR basics, deemed export, TCP rules, reporting. |
| Empowered Official | Annual + updates | Licensing, disclosures, penalties. |
| IT/Security | Annual + updates | Segmentation, logging, incident response. |
| HR | Annual + updates | U.S. person screening, onboarding/offboarding. |

## Audit Plan

- Annual full TCP audit — sample access logs, training records, inventories.
- Trigger audits after org changes, new programs, incidents, or regulatory updates.
- Document findings, corrective actions, closure dates.

## Incident Response

1. Contain exposure; revoke access.
2. Preserve evidence and logs.
3. Identify data/items, USML category, persons involved, duration.
4. Assess authorization gap and potential unauthorized export.
5. Escalate to empowered official and legal counsel.
6. Evaluate voluntary disclosure timeline (22 CFR 127.12) [VERIFY].
7. Implement corrective actions; update TCP.

## Records Retention

| Record Type | Retention | Owner |
|-------------|-----------|-------|
| Licenses/agreements | 5 yrs from expiration/export [VERIFY] | Compliance |
| CJ requests/determinations | 5 yrs [VERIFY] | Compliance |
| Access/visitor logs | 5 yrs [VERIFY] | Security |
| Training records | 5 yrs [VERIFY] | HR/Compliance |

## Inventory Schema

| Asset ID | Type | USML Cat | Location/System | Owner | Classification Date | Marking Applied |
|----------|------|----------|-----------------|-------|---------------------|-----------------|

**Standard marking:** `ITAR CONTROLLED — Export of this information to foreign persons is prohibited without authorization from the U.S. Department of State.`

## Pitfalls & Checks

- Use exact program names, contract numbers, facilities, and system identifiers — no placeholders in final output.
- Explicitly mark public-domain or EAR-controlled items and exclude them from ITAR controls (22 CFR 120.11) [VERIFY].
- When classification or jurisdiction is unclear, apply interim ITAR controls pending CJ determination.
- Never permit foreign-person access without applicable authorization and documented approval.
- Maintain a single source of truth for inventory and access lists; reconcile quarterly.
- Tag every unconfirmed regulatory citation with [VERIFY] for counsel review.

---

**Key changes from the original:**

- **Description** tightened to third-person with clear trigger guidance, removing redundant keyword list formatting.
- **Added Quick Start** section for fast orientation.
- **Consolidated "Output Structure / Process"** into cleaner sections: Required Sections table, Role Responsibilities, Core Controls (grouped by domain), Training Matrix, Audit Plan, Incident Response, Records Retention, and Inventory Schema.
- **Removed the signature block template** (boilerplate that adds tokens without instructional value).
- **Renamed "Guidelines" to "Pitfalls & Checks"** for clarity.
- **Eliminated redundant bold headers** like "fill-in", "use table", "insert", "state explicitly" that described formatting intent rather than content.
- **Overall ~25% token reduction** while preserving all domain-specific legal content and regulatory citations.
