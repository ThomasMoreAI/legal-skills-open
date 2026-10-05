---
name: healthcare-law-judicialmind
title: Healthcare Law
description: Healthcare law skill for medical and health industry legal matters. Use when the user needs assistance with HIPAA compliance, healthcare regulations, medical malpractice, FDA matters, healthcare transactions, or provider licensing. Triggers on keywords like "HIPAA", "healthcare", "medical", "hospital", "physician", "malpractice", "FDA", "PHI", "patient", "provider", "Medicare", "Medicaid", "Stark", "Anti-Kickback".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/healthcare-law
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: healthcare
language: en
sources:
- title: Fda Pathways
  path: references/fda-pathways.md
- title: Hipaa Compliance
  path: references/hipaa-compliance.md
- title: Stark Analysis
  path: references/stark-analysis.md
---

# Healthcare Law

This skill provides expert guidance for healthcare regulatory compliance, transactions, and litigation.

## Core Capabilities

### 1. Regulatory Compliance
- HIPAA Privacy and Security
- Fraud and abuse laws
- Licensing and credentialing
- Medicare/Medicaid compliance

### 2. Healthcare Transactions
- Provider acquisitions
- Joint ventures
- Management agreements
- Ancillary service arrangements

### 3. Litigation
- Medical malpractice defense
- Regulatory investigations
- Qui tam defense
- Peer review matters

### 4. Life Sciences
- FDA compliance
- Clinical trials
- Drug/device approvals
- Product liability

## HIPAA Compliance

### HIPAA Components
| Rule | Scope | Key Requirements |
|------|-------|------------------|
| Privacy Rule | Use/disclosure of PHI | Notice, authorization, minimum necessary |
| Security Rule | Electronic PHI safeguards | Administrative, physical, technical |
| Breach Notification | Notification requirements | Individual, HHS, media notification |
| Enforcement Rule | Penalties and procedures | Civil and criminal penalties |

### Protected Health Information (PHI)
**Individually Identifiable Health Information**:
- Past, present, or future physical/mental health
- Provision of healthcare
- Payment for healthcare
- Identifies individual or reasonable basis to identify

**18 HIPAA Identifiers**:
1. Names
2. Geographic data
3. Dates (except year)
4. Phone numbers
5. Fax numbers
6. Email addresses
7. Social Security numbers
8. Medical record numbers
9. Health plan beneficiary numbers
10. Account numbers
11. Certificate/license numbers
12. Vehicle identifiers
13. Device identifiers
14. Web URLs
15. IP addresses
16. Biometric identifiers
17. Full-face photographs
18. Any other unique identifying number

### Privacy Rule Requirements

**Permitted Uses Without Authorization**:
- Treatment, payment, healthcare operations (TPO)
- Required by law
- Public health activities
- Abuse/neglect reporting
- Health oversight activities
- Judicial proceedings
- Law enforcement (limited)
- Research (with IRB/Privacy Board approval)

**Patient Rights**:
- Access to PHI
- Amendment of PHI
- Accounting of disclosures
- Request restrictions
- Confidential communications
- Notice of privacy practices

### Security Rule Safeguards

**Administrative Safeguards**:
- [ ] Risk analysis and management
- [ ] Workforce training
- [ ] Access management
- [ ] Security incident procedures
- [ ] Contingency planning
- [ ] Business associate agreements

**Physical Safeguards**:
- [ ] Facility access controls
- [ ] Workstation use policies
- [ ] Workstation security
- [ ] Device and media controls

**Technical Safeguards**:
- [ ] Access controls
- [ ] Audit controls
- [ ] Integrity controls
- [ ] Transmission security

### Breach Notification Requirements
| Affected Individuals | Notification Deadline |
|---------------------|----------------------|
| 1-499 | 60 days of discovery |
| 500+ | 60 days (immediate to media/HHS) |
| HHS | Annual log (under 500); immediate (500+) |

### HIPAA Penalties
| Violation Level | Per Violation | Annual Maximum |
|-----------------|---------------|----------------|
| Did not know | $137-$68,928 | $2,067,813 |
| Reasonable cause | $1,379-$68,928 | $2,067,813 |
| Willful neglect (corrected) | $13,785-$68,928 | $2,067,813 |
| Willful neglect (not corrected) | $68,928 | $2,067,813 |

## Healthcare Fraud and Abuse

### False Claims Act (31 U.S.C. §3729)
**Prohibited Conduct**:
- Knowingly presenting false claims
- Knowingly making false statements
- Concealing/avoiding obligation to pay

**Scienter**: Actual knowledge, deliberate ignorance, or reckless disregard

**Penalties**:
- Civil penalties: $13,946-$27,894 per claim (2024)
- Treble damages
- Exclusion from federal programs

### Anti-Kickback Statute (42 U.S.C. §1320a-7b)
**Prohibited**: Knowingly and willfully offering, paying, soliciting, or receiving remuneration to induce referrals for services covered by federal healthcare programs.

**Elements**:
1. Remuneration (anything of value)
2. Knowingly and willfully
3. To induce referrals
4. For items/services covered by federal programs

**Safe Harbors** (Selected):
| Safe Harbor | Key Requirements |
|-------------|------------------|
| Employment | Bona fide employment relationship |
| Personal services | Written agreement, FMV, specified services |
| Space rental | Written agreement, FMV, one year term |
| Equipment rental | Written agreement, FMV, one year term |
| Discounts | Properly disclosed and reflected |
| EHR | ONC-certified technology, conditions met |
| Referral services | Written agreement, conditions met |

### Stark Law (42 U.S.C. §1395nn)
**Prohibited**: Physician referral of designated health services (DHS) to entities with which physician (or family member) has financial relationship, unless exception applies.

**Designated Health Services**:
1. Clinical laboratory services
2. Physical therapy
3. Occupational therapy
4. Radiology and imaging
5. Radiation therapy
6. Durable medical equipment
7. Parenteral and enteral nutrients
8. Prosthetics, orthotics, prosthetic devices
9. Home health services
10. Outpatient prescription drugs
11. Inpatient and outpatient hospital services

**Exceptions** (Selected):
| Exception | Key Requirements |
|-----------|------------------|
| In-office ancillary | Services in same building, supervised |
| Employment | Bona fide employment, FMV compensation |
| Personal services | Written agreement, FMV, commercially reasonable |
| Rental | Written agreement, FMV, exclusive use |
| Isolated transactions | One-time payment, FMV, commercially reasonable |
| Group practice | Meeting all group practice requirements |

### Civil Monetary Penalties
| Violation | Per-Violation Penalty |
|-----------|----------------------|
| False claim | $11,000-$22,000 |
| Anti-kickback | $100,000 |
| Stark violation | $15,000-$100,000 |
| EMTALA violation | $50,000-$100,000 |

## Compliance Programs

### OIG Compliance Program Elements
1. Written policies and procedures
2. Compliance officer and committee
3. Training and education
4. Communication lines (hotline)
5. Internal monitoring and auditing
6. Enforcement and discipline
7. Response to detected offenses

### Compliance Risk Areas
- [ ] Billing and coding accuracy
- [ ] Medical necessity documentation
- [ ] Stark/Anti-Kickback arrangements
- [ ] EMTALA compliance
- [ ] HIPAA privacy and security
- [ ] Credentialing verification
- [ ] Quality of care
- [ ] Marketing practices
- [ ] Kickback arrangements

## Medical Malpractice

### Elements of Medical Malpractice
1. **Duty**: Physician-patient relationship
2. **Breach**: Violation of standard of care
3. **Causation**: Breach caused injury
4. **Damages**: Compensable harm

### Standard of Care
- Care that a reasonably prudent healthcare provider would provide
- Same or similar circumstances
- Same specialty and training level
- Expert testimony typically required

### Common Defenses
- No breach of standard of care
- No causation (injury would have occurred anyway)
- Comparative negligence
- Statute of limitations
- Assumption of risk
- Good Samaritan laws
- Peer review immunity

### Damages
| Type | Description |
|------|-------------|
| Economic | Medical expenses, lost wages, future care |
| Non-economic | Pain and suffering, loss of consortium |
| Punitive | Gross negligence or intentional misconduct |

## FDA Regulatory Framework

### Product Categories
| Category | Regulation | Key Requirements |
|----------|------------|------------------|
| Drugs | FDCA, NDA/ANDA | Safety and efficacy |
| Biologics | PHSA, BLA | Same + manufacturing |
| Medical devices | FDCA, Class I/II/III | Risk-based regulation |
| Food | FDCA | Safety, labeling |
| Cosmetics | FDCA | Safety, no disease claims |

### Drug Approval Process
```
Preclinical Testing → IND Application →
Phase 1 (Safety) → Phase 2 (Efficacy) → Phase 3 (Confirmation) →
NDA Submission → FDA Review → Approval
```

### Medical Device Classification
| Class | Risk | Regulatory Pathway |
|-------|------|-------------------|
| I | Low | General controls, most exempt |
| II | Moderate | 510(k) premarket notification |
| III | High | PMA (premarket approval) |

## Integration with Other Skills

- **compliance-tracking**: Healthcare regulatory monitoring
- **litigation**: Medical malpractice, regulatory defense
- **corporate-ma**: Healthcare transactions
- **contract-lifecycle**: Provider agreements
- **employment-labor**: Credentialing, employment matters

## Reference Files

For detailed guidance:
- `references/hipaa-compliance.md` - HIPAA implementation guide
- `references/stark-analysis.md` - Stark exception checklist
- `references/fda-pathways.md` - FDA approval processes
