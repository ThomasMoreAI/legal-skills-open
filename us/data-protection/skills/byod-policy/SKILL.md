---
name: byod-policy
title: BYOD Policy
description: Drafts a Bring Your Own Device (BYOD) policy for U.S. employers governing personal device access to company systems. Covers MDM enrollment, encryption, remote wipe authority, privacy expectations, data classification, and regulatory overlays (HIPAA, GLBA, SOX, GDPR). Use when creating or updating BYOD policies, mobile device security policies, or personal device programs.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/byod-policy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: data-protection
language: en
---

# BYOD Policy

Generates an employer-facing BYOD policy balancing operational flexibility with data security, regulatory compliance, and enforceable employee obligations.

## Prerequisites

Gather before drafting:

1. **Organization profile** — industry, size, applicable regulations (HIPAA, GLBA, SOX, GDPR, CCPA)
2. **Device scope** — smartphones, tablets, laptops, wearables
3. **MDM platform** — company-approved mobile device management software, if any
4. **Data classification** — which tiers are permitted on personal devices
5. **IT support boundaries** — helpdesk scope for personal vs. company apps
6. **Stipend terms** — any reimbursement for device use

## Output Structure

| # | Section | Key Contents |
|---|---------|-------------|
| 1 | Purpose & Scope | Why BYOD is permitted; covered employees, devices, systems |
| 2 | Eligibility & Enrollment | Approval process; IT registration; MDM installation |
| 3 | Security Requirements | Minimum device standards (see checklist below) |
| 4 | Company Rights | Remote access, monitoring, wipe authority and triggers |
| 5 | Privacy Expectations | What company may/may not access; commingled data |
| 6 | Employee Responsibilities | Reporting obligations; financial responsibility |
| 7 | Data Handling | Permitted classifications; backup, retention, deletion |
| 8 | Regulatory Compliance | Industry-specific overlays |
| 9 | Support & Liability | IT support scope; negligence liability |
| 10 | Acknowledgment | Signature block; disciplinary consequences |

## Key Section Details

### Security Requirements (Section 3)

Include minimum standards:

- Screen lock: PIN/password ≥ [X] chars, biometric, or MFA
- Patching: OS/security updates within [X] days of release
- MDM agent installed and active
- Full-device or work-profile encryption enabled
- Auto-lock timeout ≤ [X] minutes
- Remote wipe confirmed before enrollment
- Prohibited: jailbroken/rooted devices; sideloaded apps

### Remote Wipe (Section 4)

Enumerate trigger conditions: termination/resignation, lost/stolen device, confirmed/suspected breach, sustained non-compliance (after notice), employee opt-out.

Distinguish **selective wipe** (corporate data only) from **full device wipe** and specify which MDM capability applies to each.

### Privacy Scope (Section 5)

| Company MAY access | Company will NOT access |
|---|---|
| Business email, calendar, contacts synced to company systems | Personal photos, texts, personal email |
| Company app activity and data | Personal app data outside company systems |
| Traffic routed through company VPN | Personal browsing not on company infrastructure |
| Documents in company cloud storage | Personal files never synced to company systems |

### Acknowledgment (Section 10)

Include: employee printed name, signature, date, department/manager, optional witness/HR signature. Statement must confirm employee has read, understands, and agrees to comply, with notice that violations may result in discipline up to termination, BYOD revocation, and/or legal action.

## Drafting Checks

- **Jurisdiction**: U.S.-focused; flag state-specific laws (CA CPRA, IL BIPA, NY SHIELD) requiring additional notice
- **Healthcare**: HIPAA minimum necessary standard; assess BAA obligations if PHI on personal devices
- **Finance**: GLBA Safeguards Rule controls; SOX retention if device stores covered records
- **Cross-border**: GDPR Art. 32 measures; data transfer restrictions for EU employee data
- **Enforceability**: Require signed acknowledgment before granting access; retain in personnel files
- **MDM transparency**: Disclose what MDM monitors (app inventory, location, call logs) to reduce privacy claims and comply with state wiretapping statutes
- **Stipend**: Document device stipends in separate written agreement to avoid wage-and-hour issues
- **Review cadence**: Annual review; mandatory update on MDM platform change, new regulation, or data classification change
