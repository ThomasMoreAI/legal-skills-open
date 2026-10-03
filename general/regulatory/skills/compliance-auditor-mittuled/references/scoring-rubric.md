# Scoring Rubric: compliance-auditor

Evaluates the overall compliance posture of an organization across applicable regulatory frameworks using seven framework-aligned criteria.

## Criteria

| # | Criterion | Weight | Description |
|---|-----------|--------|-------------|
| 1 | SOC 2 Trust Services | 20% | Compliance with Security, Availability, Processing Integrity, Confidentiality, and Privacy criteria |
| 2 | HIPAA | 15% | Compliance with Privacy Rule, Security Rule, and Breach Notification requirements |
| 3 | GDPR | 15% | Compliance with lawfulness, consent, data subject rights, DPIAs, and international transfers |
| 4 | CCPA | 10% | Compliance with disclosure, opt-out, deletion, and non-discrimination requirements |
| 5 | ISO 27001 | 15% | ISMS implementation, risk management, Annex A controls, and audit programme effectiveness |
| 6 | PCI DSS | 15% | Network security, cardholder data protection, vulnerability management, and monitoring |
| 7 | SOX | 10% | Internal controls over financial reporting, segregation of duties, and audit trail |
| **Total** | | **100%** | |

> **Note**: Weights are adjusted based on framework applicability. Frameworks that do not apply receive zero weight and their percentage is redistributed proportionally among applicable frameworks.

## Scale

Each criterion is scored **0-10**:
- **0**: No evidence / completely absent
- **5**: Partially present with significant gaps
- **10**: Fully present, comprehensive, no gaps

**Composite Score** = Σ (criterion score x weight)

## Grade Bands

| Grade | Composite Score | Label | Description | Recommended Action |
|-------|----------------|-------|-------------|-------------------|
| A+ | 9.0 – 10.0 | Audit Ready | All applicable controls documented, implemented, tested, and continuously monitored with evidence | Proceed to certification audit; maintain monitoring cadence |
| A | 8.0 – 8.9 | Strong Posture | Controls implemented with minor documentation or testing gaps that do not affect operating effectiveness | Address minor gaps; schedule certification audit within 60 days |
| B | 7.0 – 7.9 | Good Posture | Most controls in place but several areas lack testing evidence or have procedural gaps | Remediate gaps over 90 days; conduct internal re-assessment before external audit |
| C | 5.0 – 6.9 | Partial Compliance | Significant gaps in implementation or testing across multiple frameworks; some critical controls missing | Major remediation programme required; delay certification audit until gaps resolved |
| D | 3.0 – 4.9 | Weak Compliance | Majority of controls undocumented or not implemented; critical areas non-compliant | Comprehensive compliance programme build-out needed; 6+ month remediation timeline |
| F | 0.0 – 2.9 | Non-Compliant | No formal compliance programme; controls absent or fundamentally deficient across all frameworks | Engage external compliance consultancy; establish programme from ground up |

## Signal Tables

### SOC 2 Trust Services

| Score | Evidence |
|-------|----------|
| 9-10 | All 5 TSCs scoped and addressed, controls documented in control matrix with owners, quarterly access reviews completed, annual penetration testing done, continuous monitoring operational, evidence collected automatically |
| 7-8 | Security TSC fully addressed, 2-3 additional TSCs covered, controls documented but some lack testing evidence, access reviews conducted semi-annually |
| 5-6 | Security TSC partially addressed, basic controls exist but documentation incomplete, access reviews conducted annually or ad-hoc, no continuous monitoring |
| 3-4 | Some security controls exist informally, no control matrix, no structured evidence collection, access reviews not conducted |
| 0-2 | No SOC 2 controls, no documentation, no awareness of Trust Services Criteria requirements |

### HIPAA

| Score | Evidence |
|-------|----------|
| 9-10 | Risk analysis current, BAAs with all vendors handling PHI, workforce trained annually, audit controls operational, breach notification procedures tested, minimum necessary standard enforced technically |
| 7-8 | Risk analysis conducted within 2 years, BAAs in place for known vendors, training completed but not refreshed annually, audit logs enabled but not regularly reviewed |
| 5-6 | Risk analysis outdated (3+ years), some BAAs missing, training conducted once, basic audit logging exists, breach procedures documented but untested |
| 3-4 | No formal risk analysis, BAAs missing for multiple vendors, no training programme, minimal audit logging |
| 0-2 | No HIPAA compliance programme, PHI handled without safeguards, no BAAs, no training, no breach procedures |

### GDPR

| Score | Evidence |
|-------|----------|
| 9-10 | ROPA complete and current, lawful basis documented per activity, consent mechanisms with withdrawal, DSR procedures with sub-30-day fulfilment, DPIAs for high-risk processing, valid transfer mechanisms, DPA with all processors |
| 7-8 | ROPA exists with minor gaps, lawful basis mostly documented, consent mechanisms functional, DSRs fulfilled within 30 days with occasional delays, DPIAs conducted for major processing |
| 5-6 | Partial ROPA, lawful basis determinations incomplete, basic consent mechanism, DSR process exists but timeframes inconsistent, no DPIAs conducted |
| 3-4 | No ROPA, lawful basis not formally documented, consent mechanism basic or non-compliant, DSR process ad-hoc |
| 0-2 | No awareness of GDPR obligations, no processing records, no consent mechanisms, no DSR procedures, international transfers without safeguards |

### CCPA

| Score | Evidence |
|-------|----------|
| 9-10 | Privacy policy current with all required disclosures, "Do Not Sell" link functional with GPC support, deletion requests fulfilled within 45 days, non-discrimination policy documented, service provider agreements include CCPA terms |
| 7-8 | Privacy policy covers most CCPA requirements, opt-out mechanism functional but no GPC support, deletion requests fulfilled with minor delays, service provider agreements being updated |
| 5-6 | Privacy policy exists but missing CCPA-specific disclosures, opt-out mechanism present but not fully functional, deletion process manual and slow |
| 3-4 | Privacy policy does not address CCPA, no opt-out mechanism, deletion requests handled ad-hoc |
| 0-2 | No CCPA awareness, no privacy policy updates for CCPA, no opt-out or deletion mechanisms |

### ISO 27001

| Score | Evidence |
|-------|----------|
| 9-10 | ISMS fully implemented with certified scope, risk assessment current, SoA complete with justifications, internal audits on schedule, management reviews documented, corrective actions tracked to closure, Annex A controls implemented and tested |
| 7-8 | ISMS implemented, risk register maintained, SoA complete, internal audits conducted with some scheduling delays, management reviews held, most corrective actions closed |
| 5-6 | ISMS scope defined, risk assessment conducted but not updated, SoA drafted, internal audits inconsistent, some Annex A controls not implemented |
| 3-4 | ISMS in early stages, risk assessment incomplete, no SoA, no internal audit programme, limited Annex A control implementation |
| 0-2 | No ISMS, no risk assessment, no formal security management system, Annex A controls not considered |

### PCI DSS

| Score | Evidence |
|-------|----------|
| 9-10 | CDE segmented and validated, cardholder data encrypted in transit and at rest, quarterly ASV scans clean, annual penetration test completed, access restricted by need-to-know with quarterly reviews, audit trails operational with daily review |
| 7-8 | CDE segmented, encryption implemented, ASV scans conducted with minor findings remediated, penetration test completed, access controls in place but reviews semi-annual |
| 5-6 | Basic CDE segmentation, encryption partially implemented, vulnerability scans conducted but findings backlogged, access controls exist but not regularly reviewed |
| 3-4 | Minimal network segmentation, encryption gaps, vulnerability scanning irregular, access controls loosely defined |
| 0-2 | No CDE segmentation, cardholder data unencrypted, no vulnerability management, no access controls for payment data |

### SOX

| Score | Evidence |
|-------|----------|
| 9-10 | ICFR fully documented with control matrices, SOD enforced with technical controls and exception tracking, change management for financial systems with approval records, complete audit trail, annual management assessment completed with no material weaknesses |
| 7-8 | ICFR documented, SOD mostly enforced with some exceptions documented, change management in place, audit trail exists, management assessment completed with minor findings |
| 5-6 | ICFR partially documented, SOD policies exist but enforcement inconsistent, basic change management, audit trail incomplete for some transaction types |
| 3-4 | Minimal ICFR documentation, SOD conflicts unresolved, limited change management for financial systems, audit trail gaps |
| 0-2 | No ICFR programme, no SOD enforcement, no change management for financial systems, no audit trail for financial transactions |
