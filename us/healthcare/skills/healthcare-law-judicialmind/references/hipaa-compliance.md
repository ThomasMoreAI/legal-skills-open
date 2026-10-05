# HIPAA Compliance Reference Guide

## Overview

The Health Insurance Portability and Accountability Act of 1996 (HIPAA), Pub. L. 104-191, establishes national standards for protecting sensitive patient health information. The implementing regulations are found at 45 CFR Parts 160, 162, and 164.

## Key Definitions

### Protected Health Information (PHI)
PHI is individually identifiable health information that:
- Is created or received by a covered entity or business associate
- Relates to past, present, or future physical or mental health condition
- Relates to provision of health care or payment for health care
- Identifies the individual or provides reasonable basis for identification

**45 CFR § 160.103**

### Covered Entities
1. **Health Care Providers** - Any provider who transmits health information electronically in connection with HIPAA transactions
2. **Health Plans** - Health insurance companies, HMOs, employer-sponsored health plans, Medicare, Medicaid
3. **Health Care Clearinghouses** - Entities that process health information into standard formats

### Business Associates
Persons or entities that perform functions involving PHI on behalf of covered entities:
- Claims processing
- Data analysis
- Billing services
- Legal services
- Accounting services
- IT services and cloud storage

**45 CFR § 160.103**

---

## HIPAA Privacy Rule (45 CFR Part 164, Subpart E)

### Minimum Necessary Standard
Covered entities must make reasonable efforts to limit PHI to the minimum necessary to accomplish the intended purpose. **45 CFR § 164.502(b)**

Exceptions to minimum necessary:
- Disclosures to or requests by health care providers for treatment
- Disclosures to the individual
- Uses or disclosures made pursuant to valid authorization
- Disclosures to HHS for compliance investigations
- Uses or disclosures required by law
- Uses or disclosures required for HIPAA compliance

### Uses and Disclosures

#### Permitted Without Authorization (45 CFR § 164.502(a)(1))
- **Treatment, Payment, Health Care Operations (TPO)** - Core health care functions
- **With opportunity to agree/object** - Facility directories, notifications to family
- **Incident to permitted use** - If minimum necessary applied and safeguards in place
- **Public interest activities** - 12 national priority purposes under § 164.512

#### Required Disclosures (45 CFR § 164.502(a)(2))
1. To the individual upon request (with limited exceptions)
2. To HHS for compliance investigations

#### Authorization Requirements (45 CFR § 164.508)
Valid authorization must contain:
- Description of information to be used or disclosed
- Name of person authorized to make disclosure
- Name of person to whom disclosure may be made
- Purpose of the use or disclosure
- Expiration date or event
- Individual's signature and date
- If signed by representative, description of authority

### Individual Rights

| Right | Citation | Timeframe |
|-------|----------|-----------|
| Access to PHI | § 164.524 | 30 days (one 30-day extension) |
| Amendment | § 164.526 | 60 days (one 30-day extension) |
| Accounting of disclosures | § 164.528 | 60 days (one 30-day extension) |
| Request restrictions | § 164.522(a) | No specified timeframe |
| Confidential communications | § 164.522(b) | Must accommodate reasonable requests |
| Notice of Privacy Practices | § 164.520 | At first service delivery |

### Notice of Privacy Practices (NPP)
Required elements under **45 CFR § 164.520(b)**:
- Header: "THIS NOTICE DESCRIBES HOW MEDICAL INFORMATION ABOUT YOU MAY BE USED AND DISCLOSED AND HOW YOU CAN GET ACCESS TO THIS INFORMATION. PLEASE REVIEW IT CAREFULLY."
- Uses and disclosures for TPO
- Other permitted uses without authorization
- Uses requiring authorization
- Individual rights
- Covered entity's duties
- Contact information for complaints
- Effective date

---

## HIPAA Security Rule (45 CFR Part 164, Subpart C)

### Applicability
Applies to electronic PHI (ePHI) held or transmitted by covered entities and business associates.

### General Requirements (45 CFR § 164.306)
1. Ensure confidentiality, integrity, and availability of ePHI
2. Protect against reasonably anticipated threats
3. Protect against reasonably anticipated impermissible uses/disclosures
4. Ensure workforce compliance

### Safeguard Categories

#### Administrative Safeguards (§ 164.308)
| Safeguard | Standard | Implementation |
|-----------|----------|----------------|
| Security Management Process | Required | Risk analysis, risk management, sanction policy, review |
| Assigned Security Responsibility | Required | Designate security official |
| Workforce Security | Required | Authorization, supervision, clearance procedures |
| Information Access Management | Required | Access authorization, access establishment/modification |
| Security Awareness Training | Required | Security reminders, malware protection, login monitoring, password management |
| Security Incident Procedures | Required | Response and reporting |
| Contingency Plan | Required | Data backup, disaster recovery, emergency mode operations |
| Evaluation | Required | Periodic technical and nontechnical evaluation |
| Business Associate Contracts | Required | Written contracts with satisfactory assurances |

#### Physical Safeguards (§ 164.310)
- Facility access controls
- Workstation use policies
- Workstation security
- Device and media controls

#### Technical Safeguards (§ 164.312)
- Access controls (unique user ID, automatic logoff, encryption)
- Audit controls
- Integrity controls
- Person or entity authentication
- Transmission security

### Required vs. Addressable Specifications
- **Required (R)**: Must be implemented
- **Addressable (A)**: Must assess whether reasonable and appropriate; if not, document why and implement equivalent alternative

---

## Breach Notification Rule (45 CFR Part 164, Subpart D)

### Definition of Breach (45 CFR § 164.402)
Acquisition, access, use, or disclosure of PHI in violation of the Privacy Rule that compromises the security or privacy of the PHI.

### Presumption of Breach
A use or disclosure is presumed to be a breach unless the covered entity demonstrates a low probability that the PHI has been compromised based on risk assessment considering:
1. Nature and extent of PHI involved
2. Unauthorized person who used PHI or to whom disclosure was made
3. Whether PHI was actually acquired or viewed
4. Extent to which risk to PHI has been mitigated

### Exceptions to Breach Definition
1. Unintentional acquisition, access, or use by workforce member acting in good faith within scope
2. Inadvertent disclosure between authorized persons at same covered entity or business associate
3. Good faith belief that unauthorized recipient could not reasonably retain information

### Notification Requirements

#### Individual Notification (§ 164.404)
- **Timing**: Without unreasonable delay, no later than 60 days from discovery
- **Method**: First-class mail; email if individual agreed
- **Content**: Description of breach, types of information, steps to protect, entity's mitigation steps, contact information

#### Media Notification (§ 164.406)
- Required if breach affects 500+ residents of a State or jurisdiction
- Timing: Without unreasonable delay, no later than 60 days
- Must notify prominent media outlets

#### HHS Notification (§ 164.408)
- **500+ individuals**: Contemporaneously with individual notice
- **Fewer than 500**: Annual log submission within 60 days of calendar year end

---

## Business Associate Agreements (45 CFR § 164.504(e))

### Required Provisions
1. Establish permitted and required uses and disclosures
2. Prohibition on further use/disclosure except as permitted
3. Require appropriate safeguards
4. Require breach reporting
5. Ensure subcontractor compliance
6. Provide access to PHI
7. Permit amendments
8. Provide accounting information
9. Make internal practices available to HHS
10. Return or destroy PHI at termination

### Termination Provisions
Covered entity must terminate contract if it knows of material breach by business associate, if cure is not possible.

---

## Enforcement and Penalties

### Civil Monetary Penalties (45 CFR § 160.404)

| Violation Category | Per Violation | Annual Maximum |
|-------------------|---------------|----------------|
| Did Not Know | $100 - $50,000 | $1,500,000 |
| Reasonable Cause | $1,000 - $50,000 | $1,500,000 |
| Willful Neglect (Corrected) | $10,000 - $50,000 | $1,500,000 |
| Willful Neglect (Not Corrected) | $50,000 | $1,500,000 |

*As adjusted for inflation under 45 CFR § 160.404*

### Criminal Penalties (42 USC § 1320d-6)
- **Knowing violation**: Up to $50,000 and/or 1 year imprisonment
- **False pretenses**: Up to $100,000 and/or 5 years imprisonment
- **Intent to sell or cause harm**: Up to $250,000 and/or 10 years imprisonment

### State Attorneys General
HITECH Act authorized State AGs to bring civil actions for HIPAA violations. **42 USC § 1320d-5(d)**

---

## HITECH Act Modifications (Pub. L. 111-5)

### Key Changes (2009)
1. Direct liability for business associates
2. Breach notification requirements
3. Enhanced penalties
4. State AG enforcement authority
5. Increased individual rights
6. Limitations on marketing and sale of PHI

### Omnibus Rule (2013)
Final rule implementing HITECH modifications:
- Expanded "business associate" definition
- Modified breach standard (harm threshold removed)
- Strengthened privacy protections for genetic information
- Enhanced enforcement

---

## Compliance Program Elements

### Risk Assessment
Annual or upon significant change:
- Identify all ePHI locations
- Assess current security measures
- Identify threats and vulnerabilities
- Determine likelihood and impact
- Assign risk levels
- Document findings

### Policies and Procedures
Required documentation:
- Privacy policies
- Security policies
- Breach notification procedures
- Authorization forms
- Business associate agreement templates
- Sanction policies
- Training materials

### Training Requirements
- New workforce members: Before access to PHI
- Existing workforce: Periodic refresher training
- Documentation: Maintain training records

---

## Key Citations

- **Statute**: 42 USC §§ 1320d - 1320d-9
- **Privacy Rule**: 45 CFR Part 164, Subpart E
- **Security Rule**: 45 CFR Part 164, Subpart C
- **Breach Notification**: 45 CFR Part 164, Subpart D
- **Enforcement**: 45 CFR Part 160, Subparts C-E
- **HITECH Act**: Pub. L. 111-5, Title XIII

---

*Last Updated: March 2026*
*This reference is for informational purposes only and does not constitute legal advice.*
