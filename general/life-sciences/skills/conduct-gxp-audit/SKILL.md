---
name: conduct-gxp-audit
title: Conduct GxP Audit
description: Conduct a GxP audit of computerized systems and processes. Covers audit planning, opening meetings, evidence collection, finding classification (critical/major/minor), CAPA generation, closing meetings, report writing, and follow-up verification. Use for scheduled internal audits, supplier qualification audits, pre-inspection readiness assessments, for-cause audits triggered by deviations or data integrity concerns, or periodic compliance posture reviews of validated systems.
author: pjt222
author_url: https://github.com/pjt222/agent-almanac/tree/main/i18n/caveman-lite/skills/conduct-gxp-audit
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: life-sciences
language: en
---

# Conduct GxP Audit

Plan and execute a GxP audit of computerized systems, data integrity practices, or regulated processes.

## When to Use

- Scheduled internal audit of a validated computerized system
- Supplier/vendor qualification audit for GxP-relevant software
- Pre-inspection readiness assessment before a regulatory audit
- For-cause audit triggered by a deviation, complaint, or data integrity concern
- Periodic review of a validated system's compliance posture

## Inputs

- **Required**: Audit scope (system, process, or site to audit)
- **Required**: Applicable regulations (21 CFR Part 11, EU Annex 11, GMP, GLP, GCP)
- **Required**: Previous audit reports and open CAPA items
- **Optional**: System validation documentation (URS, VP, IQ/OQ/PQ, traceability matrix)
- **Optional**: SOPs, training records, change control logs
- **Optional**: Specific risk areas or concerns triggering the audit

## Procedure

### Step 1: Develop the Audit Plan

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

**Got:** Audit plan approved by quality management and communicated to auditee at least 2 weeks before the audit.
**If fail:** Reschedule if auditee cannot provide required documentation or personnel.

### Step 2: Conduct Opening Meeting

Agenda:
1. Introduce audit team and roles
2. Confirm scope, schedule, and logistics
3. Explain finding classification system (critical/major/minor)
4. Confirm confidentiality agreements
5. Identify auditee escorts and document custodians
6. Address questions

**Got:** Opening meeting documented with attendance record.
**If fail:** If key personnel are unavailable, reschedule affected audit activities.

### Step 3: Collect and Review Evidence

Review documentation and records against audit criteria:

#### 3a. Validation Documentation Review
- [ ] URS exists and is approved
- [ ] Validation plan matches system category and risk
- [ ] IQ/OQ/PQ protocols executed with results documented
- [ ] Traceability matrix links requirements to test results
- [ ] Deviations documented and resolved
- [ ] Validation summary report approved

#### 3b. Operational Controls Review
- [ ] SOPs current and approved
- [ ] Training records demonstrate competence for all users
- [ ] Change control records complete (request, assessment, approval, verification)
- [ ] Incident/deviation reports handled per SOP
- [ ] Periodic review conducted on schedule

#### 3c. Data Integrity Assessment
- [ ] Audit trail enabled and not modifiable by users
- [ ] Electronic signatures meet regulatory requirements
- [ ] Backup and recovery procedures documented and tested
- [ ] Access controls enforce role-based permissions
- [ ] Data is attributable, legible, contemporaneous, original, accurate (ALCOA+)

#### 3d. System Configuration Review
- [ ] Production configuration matches validated state
- [ ] User accounts reviewed — no shared accounts, inactive accounts disabled
- [ ] System clocks synchronized and accurate
- [ ] Security patches applied per approved change control

**Got:** Evidence collected as screenshots, document copies, interview notes with timestamps.
**If fail:** Record "unable to verify" as an observation and note the reason.

### Step 4: Classify Findings

Classify each finding by severity:

| Classification | Definition | Response Required |
|---------------|------------|-------------------|
| **Critical** | Direct impact on product quality, patient safety, or data integrity. Systematic failure of a key control. | Immediate containment + CAPA within 15 business days |
| **Major** | Significant departure from GxP requirements. Potential to impact data integrity if uncorrected. | CAPA within 30 business days |
| **Minor** | Isolated deviation from procedure. No direct impact on data integrity or product quality. | Correction within 60 business days |
| **Observation** | Opportunity for improvement. Not a regulatory requirement. | Optional — tracked for trend analysis |

Document each finding:

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

**Got:** Every finding has classification, evidence, and regulatory reference.
**If fail:** If classification is disputed, escalate to the audit program manager for adjudication.

### Step 5: Conduct Closing Meeting

Agenda:
1. Present findings summary (no new findings should be raised)
2. Review finding classifications
3. Discuss preliminary CAPA expectations and timelines
4. Confirm next steps and report timeline
5. Acknowledge auditee cooperation

**Got:** Closing meeting documented with attendance. Auditee acknowledges findings (acknowledgement ≠ agreement).
**If fail:** If auditee disputes a finding, document the disagreement and escalate per SOP.

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

**Got:** Report issued within 15 business days of the closing meeting.
**If fail:** If delayed beyond 15 days, notify stakeholders and document the reason.

### Step 7: Track CAPA and Verify Effectiveness

For each finding requiring a CAPA:

```markdown
## CAPA Tracking
| Finding ID | CAPA ID | Root Cause | Corrective Action | Due Date | Status | Effectiveness Check |
|-----------|---------|------------|-------------------|----------|--------|-------------------|
| F-001 | CAPA-2025-042 | Configuration oversight during upgrade | Enable audit trail, verify all modules | 2025-04-15 | Open | Scheduled 2025-07-15 |
| F-002 | CAPA-2025-043 | Training matrix not updated | Complete training, update tracking | 2025-05-01 | Open | Scheduled 2025-08-01 |
```

**Got:** CAPAs assigned, tracked, and effectiveness verified per defined timeline.
**If fail:** Unresolved CAPAs escalate to QA management and are flagged in the next audit cycle.

## Validation

- [ ] Audit plan approved and communicated before audit
- [ ] Opening and closing meetings documented with attendance
- [ ] Evidence collected with timestamps and source references
- [ ] Every finding has classification, evidence, and regulatory reference
- [ ] Audit report issued within 15 business days
- [ ] CAPAs assigned with due dates for all critical and major findings
- [ ] Previous audit CAPAs verified for closure effectiveness

## Pitfalls

- **Scope creep**: Expanding the audit scope during execution without formal agreement leads to incomplete coverage and disputes.
- **Opinion-based findings**: Findings must reference specific regulatory requirements, not personal preferences.
- **Adversarial tone**: Audits are collaborative quality improvement exercises, not interrogations.
- **Ignoring positives**: Reporting only findings without acknowledging good practices undermines trust.
- **No effectiveness check**: Closing a CAPA without verifying the fix actually works is a recurring regulatory citation.

## Related Skills

- `perform-csv-assessment` — full CSV lifecycle assessment (URS through validation summary)
- `setup-gxp-r-project` — project structure for validated R environments
- `implement-audit-trail` — audit trail implementation for electronic records
- `write-validation-documentation` — IQ/OQ/PQ protocol and report writing
- `security-audit-codebase` — security-focused code audit (complementary perspective)
