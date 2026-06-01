---
name: hipaa-compliance-check
title: HIPAA Compliance Check Skill
description: 'Use when performing hipaa compliance check — hIPAA compliance review covering

  PHI handling, encryption requirements, access controls, audit logging,

  Business Associate Agreements, and breach notification readiness. Use for

  healthcare application assessments, vendor onboarding, or annual compliance

  reviews.'
author: cloudthinker-ai
author_url: https://github.com/cloudthinker-ai/CloudSkills/tree/main/skills/templates/hipaa-compliance-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
---

# HIPAA Compliance Check Skill

Perform a HIPAA compliance review for **{{ system_name }}** handling **{{ phi_types }}** as a **{{ covered_entity }}**.

## Workflow

### Step 1 — PHI Data Mapping

Identify where PHI exists in the system:
1. **Data at rest**: Databases, file storage, backups, archives
2. **Data in transit**: API calls, message queues, email, file transfers
3. **Data in use**: Application memory, caches, logs, analytics
4. **Data derivatives**: Reports, exports, de-identified datasets

Document each PHI touchpoint with data type, location, and classification.

### Step 2 — Administrative Safeguards (§164.308)

```
ADMINISTRATIVE SAFEGUARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Security Officer designated
[ ] Risk analysis conducted within last 12 months
[ ] Risk management plan documented and active
[ ] Workforce security: background checks for PHI access
[ ] Security awareness training completed by all workforce members
[ ] Sanctions policy for security violations documented
[ ] Information system activity review (audit log review) on schedule
[ ] Contingency plan: data backup, disaster recovery, emergency operations
[ ] Business Associate Agreements (BAAs) in place with all vendors handling PHI
[ ] BAA inventory current and reviewed annually
```

### Step 3 — Physical Safeguards (§164.310)

```
PHYSICAL SAFEGUARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Facility access controls documented
[ ] Workstation use policies defined
[ ] Workstation security (screen lock, encryption)
[ ] Device and media controls for disposal and re-use
[ ] Cloud provider BAA covers physical security (AWS/GCP/Azure)
```

### Step 4 — Technical Safeguards (§164.312)

```
TECHNICAL SAFEGUARDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ACCESS CONTROL
[ ] Unique user identification for all PHI access
[ ] Emergency access procedure documented
[ ] Automatic session timeout (≤15 min inactivity)
[ ] Encryption of PHI at rest (AES-256 or equivalent)

AUDIT CONTROLS
[ ] Audit logs capture all PHI access (read, write, delete)
[ ] Audit logs are immutable and retained ≥6 years
[ ] Audit log review performed regularly
[ ] Failed login attempts logged and alerted

INTEGRITY CONTROLS
[ ] Data integrity checks on PHI (checksums, validation)
[ ] Mechanism to authenticate electronic PHI

TRANSMISSION SECURITY
[ ] PHI encrypted in transit (TLS 1.2+)
[ ] Email containing PHI encrypted
[ ] API endpoints handling PHI require authentication
[ ] VPN or private connectivity for PHI data flows
```

### Step 5 — Breach Notification Readiness (§164.400)

```
BREACH NOTIFICATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Breach detection mechanisms in place
[ ] Breach risk assessment process documented
[ ] Individual notification procedure (within 60 days)
[ ] HHS notification procedure documented
[ ] Media notification procedure (>500 individuals)
[ ] Breach log maintained
[ ] Annual breach notification drill conducted
```

### Step 6 — Minimum Necessary & De-identification

```
DATA MINIMIZATION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[ ] Minimum necessary standard applied to PHI access
[ ] Role-based access limits PHI to job function requirements
[ ] De-identification follows Safe Harbor or Expert Determination method
[ ] Analytics and reporting use de-identified data where possible
[ ] Test/staging environments use synthetic data (not production PHI)
```

### Step 7 — Compliance Summary

| Safeguard Area | Items Passed | Items Failed | Compliance Status |
|---------------|-------------|-------------|-------------------|
| Administrative | X/Y | Z | COMPLIANT/GAP |
| Physical | X/Y | Z | COMPLIANT/GAP |
| Technical | X/Y | Z | COMPLIANT/GAP |
| Breach Notification | X/Y | Z | COMPLIANT/GAP |
| Data Minimization | X/Y | Z | COMPLIANT/GAP |

## Counter-Rationalizations

| Shortcut | Counter | Why |
|----------|---------|-----|
| "We can skip some steps for this case" | Adapt the workflow steps, don't skip them | Skipped steps are where incidents and oversights originate |
| "The user seems to already know what to do" | Complete all workflow phases with the user | The workflow catches blind spots that experience alone misses |
| "This is a minor case, full process is overkill" | Scale the process down, don't turn it off | Minor cases become major when unstructured; the process scales, not disappears |
| "I'll fill in the details later" | Complete each section before moving on | Deferred details are forgotten; real-time capture is more accurate |
| "The template output isn't necessary" | Always produce the structured output format | Structured output enables comparison, audit trails, and handoff to other teams |

## Output Format

Produce a HIPAA compliance report with:
1. **System overview** (name, PHI types, entity type, data flow diagram)
2. **PHI data map** with all touchpoints identified
3. **Safeguard checklists** with COMPLIANT/GAP per item
4. **BAA status** for all vendors handling PHI
5. **Remediation plan** with prioritized findings, owners, and deadlines
