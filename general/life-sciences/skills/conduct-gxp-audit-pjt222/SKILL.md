---
name: conduct-gxp-audit-pjt222
title: Conduct GxP Audit
description: Conduct a GxP audit of computerized systems and processes. Covers audit planning, opening meetings, evidence collection, finding classification (critical/major/minor), CAPA generation, closing meetings, report writing, and follow-up verification. Use for scheduled internal audits, supplier qualification audits, pre-inspection readiness assessments, for-cause audits triggered by deviations or data integrity concerns, or periodic compliance posture reviews of validated systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/caveman-ultra/skills/conduct-gxp-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: life-sciences
language: en
---

# Conduct GxP Audit

Plan + execute GxP audit of computerized systems, data integrity practices, or regulated procs.

## Use When

- Scheduled internal audit of validated computerized system
- Supplier/vendor qualification audit for GxP-relevant software
- Pre-inspection readiness assessment before regulatory audit
- For-cause audit triggered by deviation, complaint, or data integrity concern
- Periodic review of validated system's compliance posture

## In

- **Required**: Audit scope (system, proc, or site to audit)
- **Required**: Applicable regs (21 CFR Part 11, EU Annex 11, GMP, GLP, GCP)
- **Required**: Prev audit reports + open CAPA items
- **Optional**: System valid. docs (URS, VP, IQ/OQ/PQ, traceability matrix)
- **Optional**: SOPs, training records, change control logs
- **Optional**: Specific risk areas / concerns triggering audit

## Do

### Step 1: Develop Audit Plan

```markdown
# Audit Plan
## Document ID: AP-[SYS]-[YYYY]-[NNN]

### 1. Objective
[State the purpose: scheduled, for-cause, supplier qualification, pre-inspection]

### 2. Scope
- **System/Process**: [Name and version]
- **Regulations**: [21 CFR Part 11, EU Annex 11, ICH Q7, etc.]
- **Period**: [Date range of records under review]
- **Exclusions**: [Any areas explicitly out of scope]

### 3. Audit Criteria
| Area | Regulatory Reference | Key Requirements |
|------|---------------------|------------------|
| Electronic records | 21 CFR 11.10 | Controls for closed systems |
| Audit trail | 21 CFR 11.10(e) | Secure, computer-generated, time-stamped |
| Electronic signatures | 21 CFR 11.50 | Manifestation, legally binding |
| Access controls | EU Annex 11, §12 | Role-based, documented |
| Data integrity | MHRA guidance | ALCOA+ principles |
| Change control | ICH Q10 | Documented, assessed, approved |

### 4. Schedule
| Date | Time | Activity | Participants |
|------|------|----------|-------------|
| Day 1 AM | 09:00 | Opening meeting | All |
| Day 1 AM | 10:00 | Document review | Auditor + QA |
| Day 1 PM | 13:00 | System walkthrough | Auditor + IT + System Owner |
| Day 2 AM | 09:00 | Interviews + evidence collection | Auditor + Users |
| Day 2 PM | 14:00 | Finding consolidation | Auditor |
| Day 2 PM | 16:00 | Closing meeting | All |

### 5. Audit Team
| Role | Name | Responsibility |
|------|------|---------------|
| Lead Auditor | [Name] | Plan, execute, report |
| Subject Matter Expert | [Name] | Technical assessment |
| Auditee Representative | [Name] | Facilitate access and information |
```

**→** Audit plan approved by QA mgmt + communicated to auditee ≥ 2 weeks before audit.
**If err:** Reschedule if auditee can't provide req'd docs or personnel.

### Step 2: Conduct Opening Meeting

Agenda:
1. Introduce audit team + roles
2. Confirm scope, schedule, logistics
3. Explain finding classification (critical/major/minor)
4. Confirm confidentiality
5. ID auditee escorts + doc custodians
6. Address questions

**→** Opening meeting doc'd w/ attendance record.
**If err:** Key personnel unavail → reschedule affected audit activities.

### Step 3: Collect + Review Evidence

Review docs + records vs. audit criteria:

#### 3a. Validation Documentation Review
- [ ] URS exists + approved
- [ ] Valid. plan matches system category + risk
- [ ] IQ/OQ/PQ protocols executed w/ results doc'd
- [ ] Traceability matrix links req's to test results
- [ ] Deviations doc'd + resolved
- [ ] Valid. summary report approved

#### 3b. Operational Controls Review
- [ ] SOPs current + approved
- [ ] Training records show competence all users
- [ ] Change control records complete (req, assessment, approval, valid.)
- [ ] Incident/deviation reports handled per SOP
- [ ] Periodic review conducted on schedule

#### 3c. Data Integrity Assessment
- [ ] Audit trail enabled + not user-modifiable
- [ ] Electronic sigs meet reg req's
- [ ] Backup + recovery docs'd + tested
- [ ] Access controls enforce role-based perms
- [ ] Data: attributable, legible, contemporaneous, original, accurate (ALCOA+)

#### 3d. System Configuration Review
- [ ] Prod config matches validated state
- [ ] User accounts reviewed — no shared accounts, inactive disabled
- [ ] System clocks sync'd + accurate
- [ ] Security patches applied per approved change control

**→** Evidence collected as screenshots, doc copies, interview notes w/ timestamps.
**If err:** Can't verify → record "unable to verify" as observation + reason.

### Step 4: Classify Findings

Classify each finding by severity:

| Classification | Definition | Response Required |
|---------------|------------|-------------------|
| **Critical** | Direct impact on product quality, patient safety, or data integrity. Systematic failure of a key control. | Immediate containment + CAPA within 15 business days |
| **Major** | Significant departure from GxP requirements. Potential to impact data integrity if uncorrected. | CAPA within 30 business days |
| **Minor** | Isolated deviation from procedure. No direct impact on data integrity or product quality. | Correction within 60 business days |
| **Observation** | Opportunity for improvement. Not a regulatory requirement. | Optional — tracked for trend analysis |

Doc each finding:

```markdown
## Finding F-[NNN]
**Classification:** [Critical / Major / Minor / Observation]
**Area:** [Audit trail / Access control / Change control / etc.]
**Reference:** [Regulatory clause, e.g., 21 CFR 11.10(e)]

**Observation:**
[Objective description of what was found]

**Evidence:**
[Document ID, screenshot reference, interview notes]

**Regulatory Expectation:**
[What the regulation requires]

**Risk:**
[Impact on data integrity, product quality, or patient safety]
```

**→** Every finding has classification, evidence, reg ref.
**If err:** Classification disputed → escalate to audit program manager for adjudication.

### Step 5: Conduct Closing Meeting

Agenda:
1. Present findings summary (no new findings should be raised)
2. Review finding classifications
3. Discuss prelim CAPA expectations + timelines
4. Confirm next steps + report timeline
5. Acknowledge auditee cooperation

**→** Closing meeting doc'd w/ attendance. Auditee acknowledges findings (acknowledgement ≠ agreement).
**If err:** Auditee disputes finding → doc disagreement + escalate per SOP.

### Step 6: Write Audit Report

```markdown
# Audit Report
## Document ID: AR-[SYS]-[YYYY]-[NNN]

### 1. Executive Summary
An audit of [System/Process] was conducted on [dates] against [regulations].
[N] findings were identified: [n] critical, [n] major, [n] minor, [n] observations.

### 2. Scope and Methodology
[Summarize audit plan scope, criteria, and methods used]

### 3. Findings Summary
| Finding ID | Classification | Area | Brief Description |
|-----------|---------------|------|-------------------|
| F-001 | Major | Audit trail | Audit trail disabled for batch record module |
| F-002 | Minor | Training | Two users missing annual GxP training |
| F-003 | Observation | Documentation | SOP formatting inconsistencies |

### 4. Detailed Findings
[Include full finding details from Step 4 for each finding]

### 5. Positive Observations
[Document areas of good practice observed during the audit]

### 6. Conclusion
The overall compliance status is assessed as [Satisfactory / Needs Improvement / Unsatisfactory].

### 7. Distribution
| Recipient | Role |
|-----------|------|
| [Name] | System Owner |
| [Name] | QA Director |
| [Name] | IT Manager |

### Approval
| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Auditor | | | |
| QA Director | | | |
```

**→** Report issued within 15 business days of closing meeting.
**If err:** Delayed beyond 15 days → notify stakeholders + doc reason.

### Step 7: Track CAPA + Verify Effectiveness

Each finding requiring CAPA:

```markdown
## CAPA Tracking
| Finding ID | CAPA ID | Root Cause | Corrective Action | Due Date | Status | Effectiveness Check |
|-----------|---------|------------|-------------------|----------|--------|-------------------|
| F-001 | CAPA-2025-042 | Configuration oversight during upgrade | Enable audit trail, verify all modules | 2025-04-15 | Open | Scheduled 2025-07-15 |
| F-002 | CAPA-2025-043 | Training matrix not updated | Complete training, update tracking | 2025-05-01 | Open | Scheduled 2025-08-01 |
```

**→** CAPAs assigned, tracked, effectiveness verified per defined timeline.
**If err:** Unresolved CAPAs escalate to QA mgmt + flag in next audit cycle.

## Check

- [ ] Audit plan approved + communicated pre-audit
- [ ] Opening + closing meetings doc'd w/ attendance
- [ ] Evidence collected w/ timestamps + source refs
- [ ] Every finding has classification, evidence, reg ref
- [ ] Audit report issued within 15 business days
- [ ] CAPAs assigned w/ due dates for all critical + major findings
- [ ] Prev audit CAPAs verified for closure effectiveness

## Traps

- **Scope creep**: Expanding scope during exec w/o formal agreement → incomplete coverage + disputes.
- **Opinion-based findings**: Findings must ref specific reg req's, not personal preferences.
- **Adversarial tone**: Audits = collaborative quality improvement, not interrogations.
- **Ignore positives**: Reporting only findings w/o acknowledging good practices undermines trust.
- **No effectiveness check**: Closing CAPA w/o verifying fix actually works = recurring regulatory citation.

## →

- `perform-csv-assessment` — full CSV lifecycle assessment (URS through validation summary)
- `setup-gxp-r-project` — project structure for validated R environments
- `implement-audit-trail` — audit trail impl for electronic records
- `write-validation-documentation` — IQ/OQ/PQ protocol + report writing
- `security-audit-codebase` — security-focused code audit (complementary perspective)
