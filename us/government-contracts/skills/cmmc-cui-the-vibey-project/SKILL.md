---
name: cmmc-cui-the-vibey-project
title: CMMC 2.0 and CUI — DoD Cybersecurity Requirements
description: Use when dealing with CMMC (Cybersecurity Maturity Model Certification) levels, CUI (Controlled Unclassified Information) handling, DoD contract requirements, or cybersecurity disclosure decisions. Use whenever a user mentions DFARS, CMMC, CUI, FCI, government contract security, defense contractor compliance, or incident reporting to DoD. Covers CMMC 2.0 levels, CUI identification, SPRS submission, and 72-hour incident reporting.
author: the-vibey-project
author_url: https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_tools/skills/plugins/compliance-frameworks/skills/cmmc-cui
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: government-contracts
language: en
---

# CMMC 2.0 and CUI — DoD Cybersecurity Requirements

## What This Skill Does

This skill guides you through the Cybersecurity Maturity Model Certification (CMMC) 2.0 framework, CUI identification and handling, DFARS clause requirements, assessment types, and cybersecurity incident disclosure decisions. It covers who needs what level, how to scope your environment, and the specific obligations that trigger reporting to the DoD.

---

## CMMC 2.0 Model Overview

CMMC 2.0 was announced November 2021 (final rule effective December 2024). It replaced CMMC 1.0's 5 levels with 3 streamlined levels tied to specific information types and security requirement sets.

### Level 1 — Foundational (17 Practices)
**What it protects:** Federal Contract Information (FCI)
**Who needs it:** ALL DoD contractors who receive FCI — essentially any company with a DoD prime or subcontract
**Requirements:** The 17 practices from FAR 52.204-21 (basic safeguarding of covered contractor information systems)
**Assessment type:** Annual self-assessment; company executive must affirm compliance
**SPRS submission:** Not required by CMMC Level 1 specifically, but DFARS 252.204-7019 requires SPRS score for any contract requiring NIST 800-171

### Level 2 — Advanced (110 Practices)
**What it protects:** Controlled Unclassified Information (CUI)
**Who needs it:** DoD contractors who handle CUI — the majority of the defense industrial base (DIB)
**Requirements:** All 110 practices from NIST SP 800-171 r2 (one-to-one mapping)
**Assessment type:**
- **Self-assessment** (with annual executive affirmation + SPRS score): Allowed for some Level 2 contracts (non-prioritized acquisitions)
- **C3PAO third-party assessment** (3-year certification): Required for contracts designated as "prioritized" by the DoD (typically sensitive programs)
**SPRS submission:** Required prior to contract award; DoD can request SSP for verification

### Level 3 — Expert (110 + 24 Practices)
**What it protects:** CUI in the most sensitive DoD programs (critical programs and technologies)
**Who needs it:** Contractors supporting the highest-priority programs (determined by DoD Program Office)
**Requirements:** All 110 NIST 800-171 practices + 24 additional practices from NIST SP 800-172
**Assessment type:** Government-led assessment by DIBCAC (Defense Industrial Base Cybersecurity Assessment Center)
**Renewal:** Every 3 years


---

## Determining Which Level Applies

### Step 1: Do you have a DoD prime or subcontract?
- No → CMMC likely does not apply (check for other federal contracts via FAR)
- Yes → Continue

### Step 2: Does the contract involve FCI?
**Federal Contract Information (FCI)** = information provided by or generated for the government under a contract to develop or deliver a product or service to the government, not intended for public release.

If you have any DoD contract for goods or services, you almost certainly have FCI. → **Level 1 minimum**

### Step 3: Does the contract involve CUI?
**Controlled Unclassified Information (CUI)** = information the government creates or possesses (or that an entity creates or possesses on behalf of the government) that requires safeguarding per law, regulation, or government policy.

Check your contract for:
- DFARS 252.204-7012 clause (CUI handling and cyber incident reporting)
- The phrase "Controlled Unclassified Information" or "CUI" in the Statement of Work
- Data types like: technical drawings, specifications, export-controlled data (ITAR/EAR), sensitive program information, research data

If CUI is present → **Level 2 minimum**

### Step 4: Is this a critical program?
If the DoD Program Office has designated the acquisition as requiring Level 3, the contract will specify. This is rare and applies to highly sensitive defense programs.

---

## CUI Identification and Handling

### What Is CUI?
CUI is defined by Executive Order 13556 and managed by the National Archives (NARA) CUI Registry (https://www.archives.gov/cui). It is NOT classified information — it is sensitive unclassified information.

**Common CUI Categories in the Defense Industrial Base:**
- **CTI** (Controlled Technical Information): Technical documents, engineering drawings, specifications
- **ITAR/EAR**: Export-controlled technology and data (International Traffic in Arms Regulations / Export Administration Regulations)
- **Privacy/PII**: Personally Identifiable Information related to DoD personnel
- **Naval Nuclear Propulsion**: Highly sensitive nuclear information
- **Critical Infrastructure**: Information about critical facilities or systems
- **Law Enforcement**: Sensitive law enforcement information

### CUI Marking Requirements
CUI must be marked with the appropriate designation. At minimum, documents should include:
- "CUI" banner marking at top and bottom of each page
- The CUI category designation (e.g., "CUI//CTI")
- Distribution/dissemination controls if applicable (e.g., "FEDCON" — distribute only to federal employees and contractors)

**Digital files:** Should be labeled in metadata, file names, or document headers where possible.
**Email:** Subject line or body should include CUI marking when transmitting CUI.

### CUI Handling Requirements
- Store only in systems that meet NIST 800-171 requirements
- Encrypt CUI at rest and in transit
- Limit access to individuals with need-to-know
- Do not store CUI on personal devices unless device meets security requirements
- Destroy CUI per NIST 800-88 (media sanitization) when no longer needed
- Report unauthorized disclosure immediately (see incident reporting below)


---

## Key DFARS Clauses

### DFARS 252.204-7012 — Safeguarding Covered Defense Information (CDI)
**The foundational clause for DoD cybersecurity.** Required in most DoD contracts where CUI is involved.

Key obligations:
1. Implement NIST SP 800-171 security requirements on all systems that process, store, or transmit Covered Defense Information
2. Report cybersecurity incidents to DoD **within 72 hours** of discovery
3. Preserve images of compromised systems for 90 days post-incident report
4. Submit malicious software discovered during incident response to DoD Cyber Crime Center (DC3)
5. Flow down clause requirements to subcontractors handling CDI

"Covered Defense Information" under 7012 includes CUI and operationally critical support information.

### DFARS 252.204-7019 — Notice of NIST SP 800-171 DoD Assessment Requirements
Requires contractors to:
- Have a current NIST 800-171 assessment on file
- Submit the SPRS score to SPRS before contract award
- Have the SSP available for DoD review

### DFARS 252.204-7020 — NIST SP 800-171 DoD Assessment Requirements
Grants DoD the right to conduct assessments of contractor compliance with 800-171. Contractors must:
- Provide access to facilities, systems, and personnel for government assessments
- Cooperate with DoD/DIBCAC assessments

### DFARS 252.204-7021 — CMMC Requirements
The clause that specifically requires CMMC certification. Invoked when a contract requires a specific CMMC level. Contractors must:
- Have and maintain the required CMMC level throughout contract performance
- Ensure subcontractors at all tiers have the required level
- Not flow down higher level requirements than what subcontractor's scope requires

---

## SPRS Score Submission

The Supplier Performance Risk System (SPRS) score must be submitted before contract award for any contract invoking DFARS 252.204-7019.

**Process:**
1. Complete NIST 800-171 self-assessment against all 110 controls
2. Calculate score using DoD Assessment Methodology (110 - deductions)
3. Have company executive review and affirm the score
4. Submit via SPRS portal (https://www.sprs.csd.disa.mil)
5. Provide copy of SSP to contracting officer upon request

**Score characteristics:**
- Maximum: 110 (all controls met)
- Minimum: Can go negative
- DoD does NOT specify a minimum passing score — but contracting officers consider scores in award decisions
- A score of 110 at time of award with known deficiencies is fraudulent (False Claims Act risk)

**SPRS score vs. CMMC certification:**
- SPRS score = self-assessment result (immediate requirement for most contracts)
- CMMC certification = third-party validation (required for designated contracts when CMMC rule is fully implemented)
- Current transitional period: Many contracts require SPRS + conditional CMMC compliance plan

---

## Cybersecurity Incident Disclosure Framework

### What Triggers Reporting (DFARS 252.204-7012)
A cybersecurity incident must be reported when a contractor discovers an incident that:
- Affected or is reasonably suspected to affect a covered contractor information system (any system with CDI/CUI)
- Involves a compromise or potential compromise of CUI
- Includes exfiltration, manipulation, or destruction of CDI
- Affects ability to provide operationally critical support

**Reporting is required even if:**
- You are not certain a breach occurred (suspected incidents count)
- The incident was contained quickly
- No data was confirmed exfiltrated

### 72-Hour Reporting Requirement
From the moment of **discovery** (not confirmation), the contractor has **72 hours** to report to DoD.

**Where to report:** DoD Cyber Crime Center (DC3) via https://dibnet.dod.mil
**What to include in the report:**
- Company name, point of contact, and contract numbers affected
- Description of the incident (when, what systems, what data potentially affected)
- Indication whether the incident is ongoing
- Type of compromise (malware, unauthorized access, data exfiltration, etc.)
- Unique identifier of reported incident for tracking

**After reporting:**
- Preserve forensic images of compromised systems for 90 days
- Submit malware samples to DC3
- Provide damage assessment to prime contractor and contracting officer
- Continue to investigate and update report as findings develop


### Cybersecurity Disclosure Decision Tree

```
Did a security event occur on a system that has CUI or CDI?
├── No → Not a DFARS reportable incident (may still be internal IR)
└── Yes →
    Was the event a: malware infection, unauthorized access, data modification,
    exfiltration, or destruction affecting that system?
    ├── No (e.g., probe/scan that was blocked, no compromise) → Log internally;
    │   document why no compromise occurred; consider voluntary report
    └── Yes (or cannot confirm it DIDN'T happen) →
        ↳ REPORT WITHIN 72 HOURS to DC3 via DIBNet
        ↳ Preserve system images for 90 days
        ↳ Submit malware samples if applicable
        ↳ Notify prime contractor (if subcontractor)
        ↳ Notify contracting officer

Was a specific amount or type of CUI confirmed exfiltrated or compromised?
├── Unknown → Still report; describe what is known; update as investigation proceeds
└── Yes → Include data types and estimated scope in report; conduct damage assessment
```

### When NOT to Report (Common Misconceptions)
- A phishing email received but not clicked → Not required (no system compromise)
- A port scan from external IP that was blocked by firewall → Not required
- A user accidentally sent an email to wrong address with non-CUI content → Not required
- A failed login attempt (brute force blocked) → Not required unless account was compromised

**When in doubt: report.** Over-reporting is far preferable to under-reporting. False Claims Act risk applies to knowing failure to report, not to good-faith over-reporting.

---

## Scoping System Boundaries for CUI

### What to Include in Your CUI Enclave
All systems, devices, and cloud services that:
- Store CUI (databases, file servers, cloud storage, email with CUI)
- Process CUI (workstations where CUI is accessed, servers, applications)
- Transmit CUI (email servers, VPN endpoints, collaboration tools with CUI)
- Provide security functions to the above (domain controllers, PAM, SIEM, patch management)

### Scope Reduction Strategies
**CUI Segregation:** Create a dedicated CUI environment (physical or logical) that is isolated from general corporate systems. Only systems in the CUI enclave need to meet 800-171.

**Cloud Enclave:** Use a FedRAMP Authorized cloud service (e.g., Microsoft 365 GCC High, Azure Government) for CUI processing. The cloud provider handles many controls; contractor inherits them.

**Enclave Documentation:**
- Network diagram showing CUI boundary
- Data flow diagram showing CUI movement
- List of all in-scope system components (hardware, software, cloud services)
- Interconnection agreements for any external systems that touch CUI

---

## Assessment Types in Detail

### Self-Assessment (Level 1 and some Level 2)
- Contractor assesses own compliance against all applicable controls
- Executive officer affirms results in SPRS
- No independent verification required (at this time)
- Annual reassessment required
- DoD can request the SSP at any time (DFARS 252.204-7020)

### C3PAO Third-Party Assessment (Level 2 priority contracts)
- C3PAO = CMMC Third-Party Assessment Organization (certified by Cyber AB)
- Conducts assessment against all 110 NIST 800-171 controls
- Reviews evidence: Examine (documents), Interview (personnel), Test (technical validation)
- Issues a Level 2 CMMC Certificate valid for 3 years
- Annual affirmations required between assessments

### DIBCAC Government-Led Assessment (Level 3)
- Defense Industrial Base Cybersecurity Assessment Center
- Government assessors; most rigorous process
- Assesses all 134 practices (110 + 24 NIST 800-172)
- Required for Level 3 certification

---

## Common CMMC/CUI Implementation Gaps

### No CUI Identification Process
**Problem:** Organization does not know what it has that qualifies as CUI.
**Fix:** Conduct CUI data discovery. Review contracts and deliverables. Work with customers to identify CUI categories. Document CUI types and locations in SSP.

### CUI Stored in Non-Compliant Systems
**Problem:** CUI in personal email, personal cloud drives (Dropbox, Google Drive consumer), or unencrypted local drives.
**Fix:** Migrate CUI to compliant systems. Deploy Microsoft 365 GCC or equivalent. Encrypt local drives. Remove CUI from personal services.

### No Flow-Down to Subcontractors
**Problem:** Prime has DFARS clauses but has not flowed them to subs that handle CUI.
**Fix:** Audit all subcontracts. Add DFARS 252.204-7012, 7019, 7020, 7021 clauses to subcontracts. Obtain SPRS scores from subs. Confirm subs understand their reporting obligations.

### SPRS Score Inflated
**Problem:** SPRS score does not reflect actual compliance; score was calculated optimistically.
**Fix:** Conduct a rigorous self-assessment using 800-171A assessment procedures. Score each control honestly. Submit a lower score with a strong POA&M showing active remediation — this is legally safer than a falsely high score.

### No Incident Response Plan for DoD Reporting
**Problem:** IRP does not include DFARS 252.204-7012 reporting procedures; team does not know the 72-hour rule.
**Fix:** Add a DoD incident reporting section to the IRP. Define the trigger criteria. Identify who submits the report to DIBNet. Practice the scenario in tabletop exercises.
