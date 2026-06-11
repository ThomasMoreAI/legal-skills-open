---
name: cybersecurity-breach-summary
title: Cybersecurity Breach Summary
description: 'Produces structured cybersecurity breach summary documents for regulatory and compliance use. Use when drafting breach summaries, incident response reports, forensic report syntheses, board updates, or regulatory notification prep. Triggers: data breach, cybersecurity incident, breach summary, incident report, forensic analysis, notification timeline, GDPR, CCPA/CPRA, HIPAA, state breach law.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/cybersecurity-breach-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: cybersecurity
language: en
---

# Cybersecurity Breach Summary

Legally defensible, source-attributed incident summary for executive, counsel, and regulator review.

## Quick Start

1. Gather incident reports, forensic analyses, system logs, and response documentation.
2. Confirm privilege boundaries and confidentiality flags from counsel.
3. Populate the template below with verified facts only — attribute each assertion to a source and date.
4. Separate known facts from hypotheses or open questions.

## Template

````
# Executive Overview
- Discovery date/time (timezone):
- Incident window (earliest to latest evidence):
- Incident type / attack vector:
- Affected systems:
- Data categories involved:
- Estimated affected individuals:
- Current status (contained/ongoing):
- Immediate actions taken:
- Material business impact:

# Incident Timeline
| Date/Time (TZ) | Event | Source (doc + date) | Owner | Confidence |
|---|---|---|---|---|

# Technical Summary
- Initial access vector:
- Vulnerability or control failure:
- Lateral movement / persistence:
- Exfiltration evidence:
- Integrity/availability impacts:

# Systems Affected
| System/App | Environment | Data Stored | Impact | Status | Source |
|---|---|---|---|---|---|

# Data Impact
| Data Category | Regulated? | Population Type | Est. Count | Jurisdictions | Source |
|---|---|---|---|---|---|

# Affected Population
| Population | Est. Count | Jurisdictions | Notes |
|---|---|---|---|

# Response Actions
| Action | Date | Owner | Status | Source |
|---|---|---|---|---|

# Notifications
| Recipient | Legal Basis | Deadline | Sent Date | Method | Summary | Source |
|---|---|---|---|---|---|---|

# Legal/Regulatory Assessment
| Regime | Trigger | Deadline Rule | Status | Notes |
|---|---|---|---|---|
| GDPR Art. 33/34 [VERIFY] | | | | |
| HIPAA (45 CFR 164.400–414) [VERIFY] | | | | |
| CCPA/CPRA [VERIFY] | | | | |
| State breach laws (list states) | | | | |

# Contractual / Litigation Exposure
- Contracts with notice obligations:
- SLAs or security addenda implicated:
- Potential claims and venues:
- Preservation actions taken:

# Insurance
- Carrier/policy:
- Notice sent (date/time):
- Coverage issues or reservations:

# Open Issues
-

# Remediation
| Gap/Root Cause | Corrective Action | Owner | Due Date | Status |
|---|---|---|---|---|

# Source Map
| Fact | Source Document | Date | Page/Section |
|---|---|---|---|
````

## Pitfalls

- **Speculation**: Label unknowns explicitly. Do not opine on liability — describe exposure factors only.
- **Timezone drift**: Use consistent date/time with timezone; maintain a single chronological basis.
- **Jurisdiction scope**: List all jurisdictions implicated by affected individuals, not just HQ location.
- **Unverified citations**: Mark uncertain legal citations or deadlines with `[VERIFY]`.
- **Privilege leaks**: Keep privileged content in clearly marked sections per counsel direction.
- **Vague counts**: Use ranges when scope is uncertain and explain the estimation basis.
