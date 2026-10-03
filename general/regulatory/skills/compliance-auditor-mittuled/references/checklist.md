# Master Compliance Checklist: compliance-auditor

57-item checklist organized by regulatory framework for comprehensive compliance auditing.

## SOC 2 — Trust Services Criteria (12 Items)

### Security (CC6)
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 1 | Logical access controls restrict system access to authorized users | Access control policies, user provisioning/deprovisioning logs, access review records | Critical |
| 2 | System boundaries defined with network segmentation and firewall rules | Network diagrams, firewall configurations, segmentation documentation | Critical |
| 3 | Encryption in transit (TLS 1.2+) and at rest for sensitive data | TLS configuration scans, encryption key management procedures, storage encryption settings | High |
| 4 | Security event monitoring and alerting operational | SIEM configuration, alert rules, incident response logs, on-call rotation records | High |

### Availability (A1)
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 5 | Business continuity and disaster recovery plans documented and tested | BCP/DR plans, test results, recovery time actuals vs. targets | High |
| 6 | System uptime monitoring with defined SLAs | Uptime monitoring dashboards, SLA definitions, historical uptime reports | Medium |

### Processing Integrity (PI1)
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 7 | Data processing validated for completeness and accuracy | Input validation rules, reconciliation procedures, error handling logs | Medium |
| 8 | Change management process controls system modifications | Change management policy, approval records, deployment logs, rollback procedures | High |

### Confidentiality (C1)
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 9 | Confidential information identified and classified | Data classification policy, inventory of confidential data, labeling procedures | Medium |
| 10 | Confidential data disposal procedures documented and followed | Data retention policy, disposal records, certificate of destruction | Medium |

### Privacy (P1)
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 11 | Privacy notice provided to data subjects at collection | Published privacy policy, consent mechanisms, collection point documentation | High |
| 12 | Data subject rights requests processed within required timeframes | Rights request log, response time records, fulfillment procedures | High |

## HIPAA (8 Items)

### Privacy Rule
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 13 | Minimum necessary standard applied to PHI access | Access policies scoped to roles, minimum necessary determinations, access audit logs | Critical |
| 14 | Notice of Privacy Practices provided to patients | Published NPP, acknowledgment records, distribution procedures | High |
| 15 | Business Associate Agreements executed with all vendors handling PHI | BAA inventory, executed BAAs, vendor compliance attestations | Critical |

### Security Rule
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 16 | Risk analysis conducted and documented | Risk assessment report, threat inventory, vulnerability findings, risk register | Critical |
| 17 | Workforce training on HIPAA requirements completed | Training materials, completion records, attestation logs, training cadence documentation | High |
| 18 | Audit controls record access to systems containing PHI | Audit log configurations, log retention policies, sample audit trail reports | High |

### Breach Notification
| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 19 | Breach notification procedures documented with 60-day timeline | Breach response plan, notification templates, timeline tracking procedures | Critical |
| 20 | Breach risk assessment methodology defined for determining notification obligations | Risk assessment framework, past breach assessments, determination criteria | High |

## GDPR (10 Items)

| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 21 | Lawful basis identified and documented for each processing activity | Records of processing activities (ROPA), legal basis determinations per purpose | Critical |
| 22 | Valid consent obtained where consent is the legal basis | Consent mechanism implementation, consent records, withdrawal mechanism | Critical |
| 23 | Data subject rights fulfilled within 30-day timeline | Rights request procedures, response logs, fulfillment records with timestamps | High |
| 24 | Data Protection Impact Assessments conducted for high-risk processing | DPIA procedures, completed DPIAs, risk mitigation records | High |
| 25 | International data transfers have valid transfer mechanisms | Standard contractual clauses, adequacy decisions, transfer impact assessments | Critical |
| 26 | Data processing agreements with all processors | DPA inventory, executed DPAs, sub-processor lists and approval records | High |
| 27 | Data breach notification to supervisory authority within 72 hours | Breach response plan, notification procedures, past breach notification records | Critical |
| 28 | Records of processing activities maintained | ROPA document, regular update records, completeness verification | High |
| 29 | Data Protection Officer appointed (where required) | DPO appointment documentation, contact information published, independence safeguards | Medium |
| 30 | Privacy by design and default implemented in new processing | Design review procedures, privacy review checklists, implementation evidence | Medium |

## CCPA (6 Items)

| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 31 | Privacy policy discloses categories of PI collected and purposes | Published privacy policy, category mapping, update cadence records | High |
| 32 | Opt-out mechanism for sale/sharing of personal information | "Do Not Sell" link implementation, opt-out processing logs, GPC signal handling | Critical |
| 33 | Consumer deletion requests fulfilled within 45-day timeline | Deletion request procedures, fulfillment logs, verification methods | High |
| 34 | Non-discrimination for consumers exercising CCPA rights | Pricing policies, service level documentation, non-discrimination policy | Medium |
| 35 | Service provider agreements include CCPA-required terms | Contract inventory, CCPA addenda, purpose limitation clauses | High |
| 36 | Sensitive personal information use limitations disclosed and honored | Sensitive PI inventory, limitation mechanisms, "Limit Use" link implementation | High |

## ISO 27001 (9 Items)

| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 37 | Information Security Management System (ISMS) scope and policy defined | ISMS scope document, information security policy, management approval records | Critical |
| 38 | Risk assessment methodology defined and executed | Risk assessment methodology, risk register, risk treatment plan | Critical |
| 39 | Statement of Applicability (SoA) documents Annex A control selections | SoA document with justification for inclusion/exclusion of each control | High |
| 40 | Internal audit programme operational | Audit schedule, audit reports, finding tracking, auditor independence records | High |
| 41 | Management review conducted at planned intervals | Management review minutes, input data, decisions and actions recorded | Medium |
| 42 | Corrective actions tracked to closure | Non-conformity register, root cause analyses, corrective action evidence, closure verification | High |
| 43 | Asset inventory maintained with ownership assigned | Asset register, owner assignments, classification levels, review records | Medium |
| 44 | Access control policy implemented per Annex A.9 | Access control policy, role-based access matrix, review cadence, privileged access controls | High |
| 45 | Incident management procedure operational per Annex A.16 | Incident response plan, incident log, post-incident reviews, escalation procedures | High |

## PCI DSS (7 Items)

| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 46 | Network segmentation isolates cardholder data environment | Network diagrams, segmentation testing results, firewall rules for CDE | Critical |
| 47 | Cardholder data encrypted in storage and transit | Encryption configurations, key management procedures, PAN masking/truncation evidence | Critical |
| 48 | Vulnerability management programme with regular scanning | Vulnerability scan reports, patch management records, penetration test results | High |
| 49 | Access to cardholder data restricted by business need-to-know | Access control lists, role definitions for CDE access, quarterly access reviews | High |
| 50 | Audit trail for all access to cardholder data | Log configurations, log retention (12 months), daily log review procedures | High |
| 51 | Security policies and procedures documented and distributed | Security policy documents, employee acknowledgments, annual review records | Medium |
| 52 | Regular security testing (penetration tests, vulnerability scans) | Penetration test reports (annual), ASV scan results (quarterly), remediation records | High |

## SOX (5 Items)

| # | Requirement | Evidence Needed | Severity |
|---|------------|----------------|----------|
| 53 | Internal controls over financial reporting (ICFR) documented | Control matrices, process narratives, risk-control mapping | Critical |
| 54 | Segregation of duties enforced for financial processes | SOD matrix, access controls for financial systems, exception approvals | Critical |
| 55 | Change management controls for financial systems | Change tickets for financial system modifications, approval records, testing evidence | High |
| 56 | Audit trail for financial transactions maintained | Transaction logs, journal entry approvals, reconciliation records, retention compliance | High |
| 57 | Management assessment of ICFR effectiveness completed annually | Assessment report, testing results, deficiency classifications, remediation tracking | Critical |

## Common Findings by Framework

| Framework | Most Common Finding | Typical Root Cause |
|-----------|-------------------|--------------------|
| SOC 2 | Access reviews not conducted quarterly | No automated access review tooling; manual process forgotten |
| HIPAA | BAAs missing for cloud sub-processors | Shadow IT; vendors onboarded without legal review |
| GDPR | ROPA incomplete or outdated | No owner assigned; new processing activities not registered |
| CCPA | Opt-out mechanism not processing GPC signals | Engineering unaware of GPC requirement; not in product backlog |
| ISO 27001 | Risk register not updated after significant changes | Risk assessment treated as annual exercise, not continuous |
| PCI DSS | Network segmentation not validated after infrastructure changes | Segmentation testing not integrated into change management |
| SOX | Segregation of duties exceptions not reviewed | Small team; SOD conflicts accepted without compensating controls |
