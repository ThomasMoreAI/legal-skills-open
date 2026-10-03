# Privacy Regulation Checklists

Reference checklists for major data privacy regulations relevant to software projects.

## GDPR (General Data Protection Regulation) — EU/EEA

### Applicability
Applies to any organization processing personal data of EU/EEA residents, regardless of where the organization is based.

### Key Principles
- [ ] **Lawfulness, Fairness, Transparency:** Clear lawful basis for all processing; privacy notice provided
- [ ] **Purpose Limitation:** Data collected for specified, explicit, legitimate purposes only
- [ ] **Data Minimization:** Only collect data that is adequate, relevant, and necessary
- [ ] **Accuracy:** Keep data accurate and up-to-date; erase or rectify inaccurate data
- [ ] **Storage Limitation:** Retain data only as long as necessary; define retention periods
- [ ] **Integrity and Confidentiality:** Appropriate security measures (encryption, pseudonymization)
- [ ] **Accountability:** Document compliance; maintain records of processing activities

### Data Subject Rights
- [ ] **Right to Access (Art. 15):** Users can request a copy of their data
- [ ] **Right to Rectification (Art. 16):** Users can correct inaccurate data
- [ ] **Right to Erasure (Art. 17):** Users can request deletion ("right to be forgotten")
- [ ] **Right to Restrict Processing (Art. 18):** Users can limit how data is used
- [ ] **Right to Data Portability (Art. 20):** Users can receive data in machine-readable format
- [ ] **Right to Object (Art. 21):** Users can object to processing (including direct marketing)
- [ ] **Automated Decision-Making (Art. 22):** Users can opt out of profiling and automated decisions

### Operational Requirements
- [ ] **Data Protection Officer (DPO):** Appointed if core activities involve large-scale processing
- [ ] **Data Processing Agreements (DPA):** Signed with all processors handling EU personal data
- [ ] **Data Protection Impact Assessment (DPIA):** Conducted for high-risk processing
- [ ] **Breach Notification:** Notify authorities within 72 hours; notify affected users without undue delay
- [ ] **Cross-Border Transfers:** Adequacy decision, Standard Contractual Clauses (SCCs), or Binding Corporate Rules (BCRs) in place
- [ ] **Consent:** Freely given, specific, informed, unambiguous; withdrawable at any time
- [ ] **Children's Data:** Parental consent required for under-16 (varies by member state, 13-16)
- [ ] **Records of Processing:** Maintain Article 30 records

### Technical Measures
- [ ] Encryption at rest and in transit (TLS 1.2+)
- [ ] Pseudonymization and anonymization where possible
- [ ] Access controls and role-based permissions
- [ ] Audit logging for data access and modifications
- [ ] Data backup and disaster recovery procedures
- [ ] Secure deletion / data disposal procedures

---

## CCPA/CPRA (California Consumer Privacy Act / California Privacy Rights Act) — California, USA

### Applicability
Applies to for-profit businesses that collect California residents' personal information and meet at least one threshold: (a) $25M+ annual revenue, (b) buys/sells/shares data of 100,000+ consumers/households, or (c) derives 50%+ of revenue from selling/sharing data.

### Consumer Rights
- [ ] **Right to Know:** Consumers can request disclosure of categories and specific pieces of data collected
- [ ] **Right to Delete:** Consumers can request deletion of personal information
- [ ] **Right to Correct:** Consumers can correct inaccurate personal information (CPRA addition)
- [ ] **Right to Opt-Out:** Consumers can opt out of sale/sharing of personal information
- [ ] **Right to Limit Use:** Consumers can limit use of sensitive personal information (CPRA addition)
- [ ] **Non-Discrimination:** No discrimination for exercising CCPA rights

### Operational Requirements
- [ ] **Privacy Notice:** Disclose categories of data collected, purposes, and whether data is sold/shared
- [ ] **"Do Not Sell or Share" Link:** Clear, conspicuous link on homepage and privacy page
- [ ] **Opt-Out Mechanism:** At least two methods to submit opt-out requests
- [ ] **Response Timeline:** Respond to verified requests within 45 days (+45 day extension with notice)
- [ ] **Data Retention:** Disclose retention periods for each category of personal information
- [ ] **Service Provider Contracts:** Written contracts with limitations on use of personal information
- [ ] **Sensitive Data:** Obtain opt-in consent for sensitive personal information (CPRA)
- [ ] **Data Minimization:** Collect, use, retain only what is reasonably necessary (CPRA)
- [ ] **Risk Assessments:** Conduct cybersecurity audits and risk assessments (CPRA)
- [ ] **Global Opt-Out:** Honor browser-based opt-out preference signals (CPRA)

---

## HIPAA (Health Insurance Portability and Accountability Act) — USA (Healthcare)

### Applicability
Applies to Covered Entities (healthcare providers, health plans, healthcare clearinghouses) and Business Associates that handle Protected Health Information (PHI).

### PHI Safeguards
- [ ] **Administrative Safeguards:** Security management process, assigned security responsibility, workforce training
- [ ] **Physical Safeguards:** Facility access controls, workstation security, device/media controls
- [ ] **Technical Safeguards:** Access controls, audit controls, integrity controls, transmission security
- [ ] **Encryption:** PHI encrypted at rest and in transit (addressable, not required if documented why not)
- [ ] **Access Controls:** Unique user IDs, automatic logoff, emergency access procedures
- [ ] **Audit Controls:** Hardware/software mechanisms to record and examine PHI access

### Business Associate Agreements (BAA)
- [ ] BAA signed with all vendors that create, receive, maintain, or transmit PHI
- [ ] BAA includes permitted uses, safeguards, breach reporting obligations
- [ ] Subcontractor compliance chain maintained

### Breach Notification
- [ ] Notify affected individuals within 60 days of breach discovery
- [ ] Notify HHS within 60 days (within 60 days of calendar year end if < 500 affected)
- [ ] Notify media if breach affects 500+ individuals in a state/jurisdiction

### Patient Rights
- [ ] **Right to Access:** Patients can inspect and obtain copies of their PHI
- [ ] **Right to Amend:** Patients can request corrections to their PHI
- [ ] **Right to Accounting:** Patients can request a list of disclosures
- [ ] **Right to Restrict:** Patients can request restrictions on uses/disclosures
- [ ] **Notice of Privacy Practices:** Must be provided to patients

---

## General Privacy Patterns (Best Practices)

### Data Minimization
- [ ] Collect only data that is strictly necessary for the defined purpose
- [ ] Avoid collecting sensitive data unless absolutely required
- [ ] Default all optional fields to "not collected"
- [ ] Regularly audit collected data fields and remove unused ones

### Purpose Limitation
- [ ] Define and document the specific purpose for each data collection point
- [ ] Do not repurpose data without new consent or lawful basis
- [ ] Separate consent for different processing purposes (no bundling)
- [ ] Review purposes periodically and update privacy notices

### Retention Limits
- [ ] Define retention periods per data category (e.g., logs: 90 days, analytics: 26 months)
- [ ] Implement automated data purging based on retention schedules
- [ ] Anonymize data rather than deleting where possible
- [ ] Document retention rationale and review annually

### Security Baseline
- [ ] Encryption at rest (AES-256 or equivalent) for all stored personal data
- [ ] Encryption in transit (TLS 1.2+) for all data transmission
- [ ] Access controls: least privilege, role-based access, MFA for sensitive systems
- [ ] Audit logging: record who accessed what data and when
- [ ] Regular penetration testing and vulnerability scanning
- [ ] Incident response plan with defined breach notification procedures

### Consent Management
- [ ] Granular consent options (not all-or-nothing)
- [ ] Clear, plain-language consent requests (no legalese)
- [ ] Easy withdrawal mechanism (as easy as giving consent)
- [ ] Consent records maintained with timestamps and scope
- [ ] Cookie consent banners that respect "Do Not Track" / GPC signals

### Cross-Border Data Transfers
- [ ] Identify all jurisdictions where data is stored or processed
- [ ] Document transfer mechanisms (SCCs, BCRs, adequacy decisions)
- [ ] Conduct Transfer Impact Assessments (TIA) for high-risk transfers
- [ ] Maintain transfer records for regulatory inspection

### Vendor / Third-Party Management
- [ ] Inventory all third parties that receive or process personal data
- [ ] DPAs signed with all data processors
- [ ] Regular vendor security assessments and compliance reviews
- [ ] Data processing limited to what is specified in the DPA
