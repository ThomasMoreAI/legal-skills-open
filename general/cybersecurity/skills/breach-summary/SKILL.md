---
name: breach-summary
title: Cybersecurity Breach Summary
description: 'Summarizes cybersecurity breach incidents into structured legal and compliance records. Trigger when synthesizing incident reports, forensics, logs, or notifications into a defensible chronology, scope-impact analysis, response ledger, or regulatory-risk assessment. Keywords: data breach, incident response, unauthorized access, ransomware, exfiltration, GDPR, CCPA, HIPAA.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/breach-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: cybersecurity
language: en
tags: [regulatory, summarization, summary]
---

# Cybersecurity Breach Summary

Produces a sourced, fact-based breach summary for counsel, security leadership, and regulator-facing communications. Every assertion is cited and uncertainty is labeled explicitly.

## Quick Start

Before drafting, confirm you have:

1. **Source documents** — incident ticket, forensics reports, SOC/SIEM logs, legal notices, board updates, insurance correspondence.
2. **Data map** — affected systems, data types, populations (customers, employees, patients, etc.).
3. **Jurisdiction map** — impacted individuals/entities, contractual/processor obligations.
4. **Privilege check** — identify attorney-client or confidential material before summarizing.
5. **Notification status** — timeline of notices already sent (internal, regulator, affected persons, law enforcement).

## Workflow

### Phase 1 — Intake Matrix

List each source with creator, date range, reliability rating, and key gaps.

### Phase 2 — Header Block

Incident ID | Reporting period | Primary custodians (security/counsel/compliance) | Severity (High/Medium/Low) | Status (Ongoing/Contained/Remediated)

### Phase 3 — Executive Overview

Discovery date/time, attack type, likely entry point, impacted systems, data sensitivity, immediate business impact.

### Phase 4 — Chronology

Initial compromise date/time with confidence level, detection source, forensic milestones, containment actions, notification milestones. Use consistent, explicit time zones throughout.

### Phase 5 — Scope & Impact

Attack vector and exploit chain, systems/databases affected, data categories accessed/exfiltrated/altered, estimated affected records/persons (min–max range), evidence of secondary spread or persistence.

### Phase 6 — Response Ledger

Actions taken vs. pending, law enforcement/third-party involvement, stakeholder notifications by date/method, patches/hardening completed. Include owner for every open item.

### Phase 7 — Legal & Regulatory Assessment

Jurisdictions with statutory impact, triggered obligations, compliance deadlines (met or missed), pending legal/commercial exposure, insurance/contractual notice status.

### Phase 8 — Open Issues & Remediation

Facts under investigation, missing data, next evidence needed, root causes, process/policy fixes, verification plan, responsible owners and target dates.

## Regulatory Checklist

| Framework | Checks | Core Evidence |
|---|---|---|
| GDPR | Supervisory-authority notification timeliness [VERIFY] | Breach triage memo, EU-persons index |
| CCPA/CPRA | Consumer notice scope and timing [VERIFY] | Data-location map, notification draft |
| HIPAA | PHI-specific breach-notification duties [VERIFY] | PHI inventory, HITECH risk assessment |
| US state laws | State deadlines, notice thresholds, media notice rules | State population map, attorney matrix |
| Contractual | Processor notices, indemnity, SLA reporting clauses | Agreements, SLAs, addenda |

## Pitfalls

- **Never overstate certainty.** Label every assertion `Verified`, `Corroborated`, or `Unverified`; describe the next validation step for unknowns.
- **Cite every statement** — `(document name, timestamp, section/page)`.
- **Separate law from fact.** Keep legal analysis distinct from the factual log to preserve evidentiary utility.
- **Protect privilege.** Reference evidence indexes without quoting legal advice.
- **Flag gaps.** Missing records that could alter legal exposure must be called out explicitly.
- **Escalate missed deadlines.** Lead with impact and corrective plan, then detail.

---

Key changes from the original:

- **Trimmed the description** — removed redundant trigger keyword list from frontmatter, kept the essential ones
- **Replaced verbose Prerequisites** with a compact **Quick Start** checklist
- **Collapsed the dual Output Structure table + repeated text templates** into a single streamlined **Workflow** with 8 phases, each described in one concise paragraph instead of separate code-fence templates
- **Condensed the regulatory table** — shorter cell text, same coverage
- **Renamed Guidelines to Pitfalls** — rewritten as terse, actionable bullet points instead of soft guidance prose
- **Eliminated ~50% of tokens** while preserving all domain-critical content (evidence tiers, citation format, privilege handling, deadline escalation)
