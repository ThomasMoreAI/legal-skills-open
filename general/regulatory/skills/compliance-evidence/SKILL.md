---
name: compliance-evidence
title: Compliance Evidence
description: Compliance artifact generator. Auto-generates audit evidence from guardrail detections, 4-eyes review gates, and DLP scans. Maps control evidence to SOC 2 Type II, ISO 27001, NIST CSF, and GDPR Article 30. Generates evidence packages on demand for auditors and tracks control effectiveness over time. Use for audit preparation, compliance evidence collection, or SOC 2/ISO 27001 artifact generation.
author: aadityaparab
author_url: https://github.com/aadityaparab/sentinel-stack/tree/main/skills/compliance-evidence
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Compliance Evidence

**Aliases:** compliance evidence, audit evidence, SOC 2 evidence, ISO 27001, compliance artifact, audit preparation, control evidence, compliance documentation

**Maturity:** Production

**Description:**
Auto-generate compliance artifacts from guardrail detections, 4-eyes review gates, and DLP scans. Map control evidence to SOC 2 Type II, ISO 27001, NIST CSF, and GDPR Article 30. Generate evidence packages on demand for auditors. Track control effectiveness over time and produce compliance dashboards.

---

## Overview

Compliance is a byproduct of good operations. This skill turns every guardrail detection and human review into compliance *evidence* — the audit trail that proves you've implemented and are operating controls.

Instead of scrambling to gather evidence when auditors arrive, this skill:

1. **Auto-tags** every guardrail action with the control it demonstrates (e.g., "data blocking" → "AC-1: Access Control Policy")
2. **Maps** controls to frameworks (SOC 2, ISO 27001, NIST, GDPR)
3. **Packages** evidence on demand for audit requests
4. **Tracks** control effectiveness (are controls actually working, or are we just logging actions?)
5. **Generates** compliance dashboards showing audit readiness

No spreadsheets, no scrambling. Evidence generation is continuous.

---

## Core Capabilities

### 1. Auto-Mapping: Guardrail Actions → Control Evidence

Every guardrail action produces a compliance artifact:

**DLP Hard Block → Data Classification & Loss Prevention Control**

```
Guardrail Action:
  Timestamp: 2026-04-12 14:32 UTC
  Type: DLP Hard Block
  Trigger: Health records (PHI) classification detected
  Action: Data export blocked
  
Auto-Generated Compliance Evidence:
  Framework: SOC 2 Type II
    Control: CC6.1 (Logical Access Control Policy)
    Evidence: System detected and blocked unauthorized access to 
              classified health data, per organizational data 
              classification policy. Incident log entry: BLOCK-2026-1847.
    
  Framework: ISO 27001
    Control: A.9.1.1 (Access Control Policy)
    Evidence: Data access control enforced; unauthorized classification 
              prevented. System maintained tamper-evident log of block.
  
  Framework: GDPR Article 32
    Control: Pseudonymization & Encryption
    Evidence: System prevents exposure of PII to unauthorized channels.
              Hard block prevents any processing without proper safeguards.
  
  Artifact ID: EVIDENCE-DLP-20260412-001
  Mappings: [CC6.1, A.9.1.1, Article 32(1)(a)]
```

**4-Eyes Review Gate → Segregation of Duties & Authorization Control**

```
Guardrail Action:
  Timestamp: 2026-04-12 15:18 UTC
  Type: 4-Eyes Review Gate Triggered
  Scenario: Purchase order > $500k requires executive approval
  Requester: Manager A (dept: procurement)
  Approver: Director B (dept: finance)
  Decision: Approved
  Documentation: Audit log with both signatures
  
Auto-Generated Compliance Evidence:
  Framework: SOC 2 Type II
    Control: CC7.2 (Segregation of Duties)
    Evidence: System enforced segregation between requester and approver.
              No single person can authorize and execute transactions above 
              threshold. Documented approval with audit trail.
    
  Framework: COSO Internal Control Framework
    Control: Authority & Responsibility (Principle 6)
    Evidence: Defined approval authorities enforced; management approval 
              documented; financial transaction authorized by responsible 
              party (Director) separate from requester (Manager).
  
  Framework: ISO 27001
    Control: A.10.1.3 (Segregation of Duties)
    Evidence: Access control enforced; incompatible duties separated.
  
  Artifact ID: EVIDENCE-4EYES-20260412-001
  Transaction ID: PO-2026-18472
  Mappings: [CC7.2, COSO Principle 6, A.10.1.3]
```

**DLP Soft Block (Monitored) → Data Loss Prevention & Monitoring Control**

```
Guardrail Action:
  Timestamp: 2026-04-12 16:45 UTC
  Type: DLP Soft Block (Monitoring)
  Trigger: Processing financial data with confidence 0.68 (below 0.75 threshold)
  Action: Allowed, but flagged for monitoring & logging
  
Auto-Generated Compliance Evidence:
  Framework: SOC 2 Type II
    Control: CC3.2 (Monitoring Activities)
    Evidence: System detected lower-confidence data classification and 
              continued monitoring. Audit log created. Daily monitoring 
              report generated for compliance review.
    
  Framework: GDPR Article 30 (Records of Processing)
    Evidence: Processing activity logged with classification confidence 
              metadata. Demonstrates org tracks data handling and risk level.
  
  Framework: NIST CSF
    Control: DE.AE-5 (Alerting)
    Evidence: System alerted to lower-confidence classification; created 
              evidence artifact for follow-up review.
  
  Artifact ID: EVIDENCE-DLP-SOFT-20260412-001
  Mapping: [CC3.2, Article 30(1)(f), DE.AE-5]
  Follow-up: Assigned to Compliance Officer for manual review
```

**Behavioral Anomaly Detection → Fraud Detection & Investigation Control**

```
Guardrail Action:
  Timestamp: 2026-04-12 18:22 UTC
  Type: Behavioral Anomaly Detected
  Signal: Employee accessed 500+ records in 2 hours (3× normal pattern)
  Action: Flagged for investigation
  
Auto-Generated Compliance Evidence:
  Framework: SOC 2 Type II
    Control: CC6.2 (Physical/Logical Access)
    Evidence: Continuous monitoring detected anomalous access pattern. 
              Investigation initiated per incident response plan. 
              No unauthorized access occurred (access was authorized but 
              unusual volume).
    
  Framework: COSO Internal Control Framework
    Control: Monitoring Activities (Principle 16)
    Evidence: Management monitoring of user access controls; anomaly 
              detection working as designed.
  
  Framework: ISO 27001
    Control: A.12.4.1 (Event Logging)
    Evidence: System logging access behavior; anomalies trigger 
              investigation protocol.
  
  Artifact ID: EVIDENCE-ANOMALY-20260412-001
  Investigation Status: In Progress
  Owner: CISO
  Mappings: [CC6.2, COSO Principle 16, A.12.4.1]
```

---

### 2. Framework Mapping Matrix

Skill maintains a **mapping table** between internal guardrails and audit frameworks:

```
COMPLIANCE FRAMEWORK MAPPING

┌────────────────────────────────────────────────────────────────┐
│ Guardrail Action → Control Evidence → Framework Artifact       │
├────────────────────────────────────────────────────────────────┤
│ DLP Hard Block → Data Loss Prevention Control                  │
│   SOC 2: CC6.1 (Logical Access)                               │
│   ISO 27001: A.9.1.1 (Access Control Policy)                  │
│   NIST CSF: AC-3 (Access Enforcement)                         │
│   GDPR: Article 32(1)(a) (Pseudonymization & Encryption)      │
│                                                                 │
│ 4-Eyes Gate → Segregation of Duties                           │
│   SOC 2: CC7.2 (Segregation of Duties)                        │
│   ISO 27001: A.10.1.3 (Segregation of Duties)                 │
│   COSO: Principle 6 (Authority & Responsibility)              │
│   GDPR: Article 5(2) (Integrity & Confidentiality)            │
│                                                                 │
│ Behavioral Anomaly Detection → Continuous Monitoring           │
│   SOC 2: CC3.2 (Monitoring Activities)                         │
│   ISO 27001: A.12.4.1 (Event Logging)                         │
│   NIST CSF: DE.AE-5 (Alerting)                                │
│   COSO: Principle 16 (Monitoring Activities)                  │
│                                                                 │
│ AI Risk Classification → Model Governance & Transparency       │
│   EU AI Act: Articles 9-13 (Documentation)                    │
│   GDPR: Article 22 (Automated Decision-Making)                │
│   ISO 27001: A.6.1.1 (Information Security Policy)            │
│   NIST CSF: GV-1 (Governance & Risk Management)               │
└────────────────────────────────────────────────────────────────┘
```

---

### 3. On-Demand Evidence Packages for Auditors

**Scenario:** Auditor requests evidence of access control implementation.

**Skill generates:**

```
AUDIT EVIDENCE PACKAGE: Access Control (SOC 2 CC6.1)
Generated: 2026-04-12
Auditor: [Big 4 Firm Name]
Request: Evidence of logical access control policy implementation

═════════════════════════════════════════════════════════════════

CONTROL OBJECTIVE CC6.1: Logical Access Policy Implemented

Evidence Artifacts:
  1. Data Classification Policy (Document)
     - Effective date: 2025-06-01
     - Approval by: Chief Risk Officer
     - File: /policies/data-classification-v2.pdf
  
  2. DLP System Configuration (Technical)
     - System: Sentinel Stack DLP Module
     - Classification rules: 47 active patterns
     - Last update: 2026-04-05
     - Hard blocks configured for PII, PHI, PCI
  
  3. Hard Block Incident Log (90 days)
     - Period: 2026-01-12 to 2026-04-12
     - Total blocks: 23
     - Blocks by category:
       * PII (SSN, passport): 8
       * PHI (health records): 12
       * PCI (credit cards): 3
     - Effectiveness: 100% (no unauthorized data access)
     - Example incidents: [BLOCK-2026-1847, BLOCK-2026-1823, ...]
  
  4. Access Control Testing (Quarterly)
     - Test date: 2026-03-01
     - Scope: Random sample of 50 users
     - Method: Attempted unauthorized data access
     - Results: 49/50 blocked as designed, 1 required remediation
     - Remediation: User retraining completed 2026-03-15
  
  5. Monitoring & Alerting (Continuous)
     - Daily monitoring reports: 90-day sample
     - Alert thresholds configured and validated
     - Alert response SLA: 4 hours (avg response time: 2.3 hours)

CONTROL FREQUENCY: Continuous
TESTING EVIDENCE: Quarterly + Incident Response
EFFECTIVENESS RATING: Effective (No design or operating deficiencies)

═════════════════════════════════════════════════════════════════

COMPLIANCE STATEMENT:
  The organization has implemented and is operating a logical access 
  control policy that effectively prevents unauthorized access to 
  classified data. Evidence artifacts demonstrate:
  
  ✓ Policy documented and approved
  ✓ System controls configured and functioning
  ✓ Incidents monitored and logged
  ✓ Effectiveness tested quarterly
  ✓ No unauthorized access occurred
  
SOC 2 Type II Conclusion: CONTROL IS OPERATING EFFECTIVELY

═════════════════════════════════════════════════════════════════

Artifact Package Contents:
  - 5 pieces of documentary evidence
  - 90-day incident log (detailed)
  - Quarterly test results (last 3 quarters)
  - Daily monitoring reports (sample)
  - System configuration export (technical)
  - Management sign-off (CRO & CISO)

Package ID: PKG-CC6.1-20260412-001
Prepared by: Compliance Evidence Skill
QA Checked: 2026-04-12 by Compliance Officer
```

**Auditor can now assess** whether control is "operating effectively" vs. "design deficiency" vs. "operating deficiency."

---

### 4. GDPR Article 30 Records of Processing

Every data processing activity auto-generates a Record of Processing:

```
RECORD OF PROCESSING (GDPR Article 30)

Processing ID: PROC-2026-004
Activity: Customer Transaction Monitoring

1. NAME & PURPOSE OF PROCESSING
   Name: Transaction Fraud Detection & Prevention
   Purpose: Identify potentially fraudulent transactions; protect 
            customers and company from financial loss
   
2. LEGAL BASIS
   Article 6(1)(f): Legitimate interest (fraud prevention)
   
3. DATA CONTROLLER
   Company Name: [Org Name]
   Contact: dpo@[org].com
   
4. DATA CATEGORIES PROCESSED
   - Transaction amount
   - Merchant category
   - Geographic location
   - Timestamp
   - Historical spending pattern
   
5. SPECIAL CATEGORY DATA (If applicable)
   None processed in this activity
   
6. RECIPIENT CATEGORIES
   - Fraud Investigation Team (internal)
   - Payment processor (third party)
   - Law enforcement (if suspected fraud confirmed)
   
7. RETENTION PERIOD
   - Transactions: 3 years (retained for regulatory reporting)
   - Flagged fraud cases: 7 years (potential litigation)
   
8. TECHNICAL & ORGANIZATIONAL MEASURES
   ✓ Encryption in transit (TLS 1.3)
   ✓ Encryption at rest (AES-256)
   ✓ Access control (role-based)
   ✓ Anomaly detection (continuous monitoring)
   ✓ Regular backups (daily)
   ✓ Incident response plan (tested quarterly)
   
9. AUTOMATED DECISION-MAKING (Article 22)
   Does this involve automated decision-making with legal effect?
   Yes: Transactions flagged as fraudulent may be declined.
   
   Safeguards:
   ✓ Human review if flagged (optional customer escalation)
   ✓ Explanation provided to customer on request
   ✓ Right to object: Customer can contact fraud team
   ✓ Appeal process: Documented and tested
   
10. INTERNATIONAL TRANSFERS
    No transfers outside EU/EEA
    
11. CONTACT FOR QUESTIONS
    Data Protection Officer: dpo@[org].com
    Privacy Team: privacy@[org].com

═════════════════════════════════════════════════════════════════

Auto-generated from Sentinel Stack on 2026-04-12
Last reviewed: 2026-04-10
Next review: 2026-05-10 (mandatory quarterly review)
```

This becomes the evidence for **GDPR Article 30 compliance.**

---

### 5. Control Effectiveness Tracking

**Skill tracks:** Are controls actually reducing risk?

```
CONTROL EFFECTIVENESS METRICS (90-day rolling)

Control: DLP Hard Block (Data Classification)
Objective: Prevent unauthorized access to sensitive data

Metrics:
  Effectiveness: 100% (23/23 blocks successful; 0 unauthorized access)
  Detection rate: 23 incidents detected per quarter
  False positive rate: 0% (all blocks were legitimate blocks)
  Time to block: < 100ms (median)
  
  Trend (Last 4 quarters):
    Q4 2025: 15 blocks
    Q1 2026: 23 blocks (↑ 53%)
    Interpretation: More detections = more enforcement activity; 
                    either more violations occurring OR better detection.
    Root cause analysis: New healthcare client (vertical expansion); 
                        staff training gap. (MITIGATE: training in progress)

Risk Reduction Impact:
  Before control: 0 blocks, potential data breaches (unquantified)
  After control: 23/23 attempts blocked; 0 breaches
  Effectiveness: HIGH (preventive control working)

═════════════════════════════════════════════════════════════════

Control: 4-Eyes Approval Gate (Segregation of Duties)
Objective: Prevent unauthorized financial transactions

Metrics:
  Transactions requiring approval: 18 (per quarter)
  Approvals granted: 16
  Approvals denied: 2 (flagged as policy violations)
  Approval time: 4.2 hours (median)
  Audit sample: 10/18 sampled; all correctly approved
  
Trend (Last 4 quarters):
    Q4 2025: 12 approvals
    Q1 2026: 18 approvals (↑ 50%)
    Interpretation: More high-value transactions; approvals working as 
                    designed. 2 denials indicate proper policy enforcement.

Risk Reduction Impact:
  Before control: Manual approval, risk of collusion
  After control: System-enforced segregation; documented audit trail
  Effectiveness: HIGH (operating as designed)
```

These metrics feed **audit readiness dashboards** and **board reports.**

---

### 6. Compliance Dashboard & Audit Readiness

Skill generates a **live compliance status dashboard:**

```
COMPLIANCE READINESS DASHBOARD

═════════════════════════════════════════════════════════════════

FRAMEWORK: SOC 2 Type II

Control Implementation Status:
  ✓ Access Control (CC6.1, CC6.2)           100% [Evidence ready]
  ✓ Risk Assessment (CC3.1)                  95% [1 minor gap]
  ✓ Change Management (CC7.3)                100% [Evidence ready]
  ✓ Segregation of Duties (CC7.2)            100% [Evidence ready]
  ✓ Monitoring Activities (CC3.2)            100% [Evidence ready]
  → OVERALL SOC 2 READINESS: 99%

Evidence Coverage:
  Total controls: 17
  Fully evidenced: 16
  Partially evidenced: 1 (CC3.1 - Design gap in policy approval workflow)
  Not evidenced: 0
  
Audit Readiness: READY (Minor remediation before audit)
Last audit: 2024-06-15
Next audit: 2026-06-15 (14 months away)

═════════════════════════════════════════════════════════════════

FRAMEWORK: ISO 27001

Control Status:
  A.5 (Governance)                           95% [1 policy update pending]
  A.6 (HR Security)                          100%
  A.7 (Asset Management)                     100%
  A.8 (Access Control)                       100%
  A.9 (Cryptography)                         100%
  A.10 (Physical & Environmental)            90%  [2 office locations]
  A.11 (Operations)                          95%
  A.12 (Communications)                      100%
  → OVERALL ISO 27001 READINESS: 97%

Evidence Quality: HIGH
  - 167 total control evidence artifacts generated
  - 89% from automated guardrail detection
  - 11% from manual documentation
  
Audit Readiness: READY
Last certification: 2023-09-30
Recertification due: 2026-09-30 (17 months away)

═════════════════════════════════════════════════════════════════

FRAMEWORK: GDPR Article 30 (Records of Processing)

Records Complete:
  Total processing activities: 43
  Documented: 42
  Missing documentation: 1 (new activity added this month)
  
Articles 30-35 Compliance:
  ✓ Data Protection Impact Assessments: 8/8 for high-risk processing
  ✓ Data Processing Agreements: 12/12 with third parties
  ✓ Breach notification procedure: Documented & tested
  ✓ DPO contact info: Published on website
  
Compliance Status: 98%
Inspection Readiness: READY
Last GDPR audit (self-assessment): 2026-02-01

═════════════════════════════════════════════════════════════════

OUTSTANDING ITEMS (Action Required):

  1. CC3.1 (Risk Assessment Policy) - ISO 27001
     Owner: Chief Risk Officer
     Deadline: 2026-04-20
     Status: In Progress (80%)
  
  2. A.5 (Governance Policy Update) - ISO 27001
     Owner: CISO
     Deadline: 2026-04-15
     Status: Awaiting Legal review
  
  3. PROC-2026-NEW (Record of Processing) - GDPR
     Owner: DPO
     Deadline: 2026-04-20
     Status: Data gathering in progress

═════════════════════════════════════════════════════════════════

AUDITOR PACKAGE READY FOR DOWNLOAD:
  SOC 2 Type II: Full evidence package (500+ pages)
  ISO 27001: Full evidence package (800+ pages)
  GDPR Article 30: Records of Processing (45 records)

Next scheduled audit: 2026-06-15 (SOC 2)
Estimated readiness: 100% (if outstanding items completed on schedule)
```

---

## Integration with Sentinel Stack

```
Guardrail Layer
  │
  ├─ DLP Hard Block
  ├─ 4-Eyes Gate
  ├─ Behavioral Anomaly
  └─ AI Risk Classification
       ↓
Compliance Evidence Layer
  ├─ Auto-map to control
  ├─ Assign to frameworks
  ├─ Generate artifact
  └─ Track effectiveness
       ↓
Audit Evidence Package
  ├─ SOC 2 Type II evidence
  ├─ ISO 27001 evidence
  ├─ GDPR Article 30 records
  ├─ NIST CSF mapping
  └─ Ready for auditor review
```

---

## How to Invoke

**Trigger Phrases:**
- "Generate SOC 2 evidence package"
- "What's our compliance status?"
- "Create an audit readiness dashboard"
- "Generate GDPR Records of Processing"
- "Is control X effective?"
- "What evidence do we have for this control?"
- "Prepare evidence package for auditor"
- "Show control effectiveness metrics"

**Example Prompt:**
```
Skill: compliance-evidence

Generate a complete SOC 2 Type II evidence package for controls 
CC6.1, CC6.2, CC7.2, and CC3.2. Include incident logs from the 
last 90 days, quarterly testing results, and a summary of control 
effectiveness. Use the auditor template.
```

---

## Configuration Requirements

Expects `config/org-config.yaml`:

```yaml
compliance-evidence:
  frameworks:
    - SOC 2 Type II
    - ISO 27001
    - GDPR Article 30
    - NIST CSF
  
  controls-mapping:
    dpl-hard-block:
      - "CC6.1"
      - "A.9.1.1"
      - "AC-3"
    
    four-eyes-gate:
      - "CC7.2"
      - "A.10.1.3"
      - "COSO Principle 6"
    
    behavioral-anomaly:
      - "CC3.2"
      - "A.12.4.1"
      - "DE.AE-5"
  
  audit-schedule:
    soc2: "2026-06-15"  # Next audit date
    iso27001: "2026-09-30"  # Recertification date
    gdpr: "continuous"  # No formal audit, but Article 30 reviewed quarterly
  
  retention-policy:
    evidence-artifacts: "P7Y"  # 7 years
    incident-logs: "P3Y"  # 3 years
    test-results: "P3Y"  # 3 years
```

---

## Outputs & Artifacts

- **Control Evidence Artifacts** — Auto-generated from guardrail actions
- **Framework Mapping** — Control → SOC 2 / ISO 27001 / NIST / GDPR
- **Audit Evidence Packages** — On-demand for auditor requests
- **GDPR Records of Processing** — Auto-maintained Article 30 records
- **Control Effectiveness Dashboard** — Real-time control performance metrics
- **Compliance Readiness Report** — Framework-by-framework status & audit readiness
- **Management Sign-Offs** — Approval trail (CRO, CISO, DPO)

---

## Key Principles

1. **Evidence is a byproduct.** Compliance artifacts are generated automatically; you don't create evidence, you enable operations that produce it.
2. **Audit-ready, always.** When an auditor arrives, your evidence package is ready. No scrambling, no gaps.
3. **Control effectiveness is measurable.** You can quantify whether controls are actually reducing risk, not just whether they exist.
4. **Framework-agnostic mapping.** Same guardrails map to SOC 2, ISO 27001, GDPR, and NIST; no duplicative effort.
5. **Continuous, not annual.** Evidence is generated continuously. Audits are a checkpoint, not the driver.

---

## See Also

- `ai-governance` skill — Provides AI system classification & governance artifacts
- `risk-register` skill — Risk scoring & treatment tracking (inputs to control effectiveness)
- `DLP` guardrails — Core detection mechanism that feeds evidence generation
