---
name: prompt-pack-data-retention-policy-sboghossian
title: Data Retention Policy
description: 'Use when a company needs to draft a Data Retention Policy specifying how long different categories of personal and business data are retained, the legal and business justification for each retention period, secure deletion procedures, and litigation hold protocols. MENA-aware: covers UAE PDPL, DIFC DP Law, ADGM DP Regs, KSA PDPL, and Lebanon/Egypt frameworks, as well as GDPR and commercial/regulatory retention minimums across GCC, EU, and UK.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-data-retention-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Data Retention Policy

A Data Retention Policy operationalises the data minimisation and storage limitation principles of every major data protection framework. It answers the question every lawyer and compliance officer faces: "How long can we keep this?" — and the equally important question that most organisations neglect: "How do we securely delete it when we no longer need it?"

## When to use this

- A company is implementing a data protection compliance program and needs a formal policy.
- A regulatory review or ISO 27001 / SOC 2 audit requires evidence of a documented retention policy.
- The company is responding to a data subject erasure request and needs to verify whether the applicable retention period has expired.
- Litigation has been filed or is anticipated and the company needs to implement a litigation hold (and stop the normal retention schedule for relevant data).
- The company is migrating to a new data platform and needs to know what data to migrate vs. what to delete first.
- A data mapping / ROPA (Records of Processing Activities) exercise has revealed data that has been retained without a documented basis.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Company name and jurisdiction(s) of operation | Determines applicable legal retention requirements | Ask the user |
| Categories of data processed | Retention periods vary by data type; policy must cover all categories | Ask the user to provide a data inventory or describe their main data categories |
| Industry sector | Some sectors have mandatory minimum retention periods (financial services, healthcare, employment) | Ask the user |
| Whether the company holds employee data | Employment law adds retention obligations beyond data protection law | Ask the user |
| Whether the company is subject to GDPR and/or MENA data protection laws | Determines which frameworks apply | Ask the user |

## Optional inputs

- Whether the policy will be shared with data subjects (affects language calibration).
- Whether the company uses third-party document management or DMS systems.
- Whether the company has an existing litigation hold process that the policy should integrate with.
- Whether the company's auditors have specified any record retention minimums.

## Policy structure

### 1. Purpose and scope
- The policy applies to all personal and business data held by the company in any format (paper and electronic).
- Purpose: to comply with applicable data protection law, meet regulatory and legal obligations, and protect the company from retaining data beyond the period for which there is a valid justification.
- Scope: all employees, contractors, and third parties who hold company data.

### 2. Governing principles

**2.1 Storage limitation (data protection law)**
Data must not be kept longer than necessary for the purpose(s) for which it was collected. This is a mandatory principle under:
- GDPR Art. 5(1)(e): storage limitation principle
- UAE PDPL: equivalent principle (Art. 15 — data must not be retained after the purpose is achieved)
- DIFC DP Law / ADGM DP Regs: storage limitation as a data processing principle
- KSA PDPL: Art. 10 — personal data must be destroyed or anonymised when no longer needed for the stated purpose

**2.2 Legal retention minimums**
Certain data must be retained for minimum periods specified by law — the policy cannot delete data earlier than the legal minimum even if the processing purpose has ended. See the Retention Schedule below.

**2.3 Balancing retention and minimisation**
When a mandatory minimum and a data minimisation obligation conflict, retain for the mandatory minimum and delete immediately upon expiry.

### 3. Retention schedule

Present as a table covering all major data categories. Tailor to the company's specific data inventory.

| Data category | Specific data types | Minimum retention period | Legal basis for minimum | Maximum retention | Deletion method |
|---|---|---|---|---|---|
| **Employee records** | Employment contracts, payroll, performance reviews, disciplinary records | 5–7 years after end of employment (varies by jurisdiction) | Employment law; social insurance law; tax law | 7 years post-employment | Secure deletion per Section 5 |
| **Customer/client records** | Identity documents, KYC files, correspondence | 5 years from end of relationship (AML); longer if pending proceedings | AML law (UAE, KSA, LB, EG, GCC); FATF Rec. 11 | 10 years if required by AML law | Secure deletion per Section 5 |
| **Financial and accounting records** | Invoices, contracts, bank records, tax records | 5–10 years depending on jurisdiction | UAE: 5 years (Commercial Transactions Law); KSA: 10 years (Commercial Court Law); LB: 10 years (Commercial Code); EG: 5 years (Tax Law); GDPR/EU: 10 years; UK: 6 years | Maximum legal period + 1 year | Secure deletion per Section 5 |
| **Legal records** | Contracts, litigation files, legal opinions | Until expiry of the applicable limitation period + 2 years | Limitation law (UAE Civil Code: 15 years general; KSA: 5 years; LB: 10 years; DIFC: 6 years; UK: 6 years) | Limitation period + 2 years | Secure deletion per Section 5 |
| **Health / medical records (employees)** | Medical certificates, occupational health reports | 10 years from last entry (or longer if occupational exposure involved) | Occupational health law; employment law | 10 years | Secure deletion with higher assurance level |
| **Marketing data** | Email lists, campaign data, analytics | Until consent is withdrawn or purpose ends; maximum 3 years from last interaction without refresh of consent | GDPR / UAE PDPL / KSA PDPL consent principles | 3 years unless consent renewed | Secure deletion per Section 5 |
| **Website / app logs and analytics** | Server logs, access logs, analytics data | As required for security purposes (typically 90 days); anonymised analytics may be retained longer | Legitimate interests (security); privacy law (minimisation) | 12 months (anonymised analytics: indefinitely) | Log deletion; anonymisation |
| **CCTV / surveillance footage** | Video footage from premises | 30–90 days unless required for incident | UAE CCTV regulations; employee privacy obligations | 90 days (or until resolution of any incident captured) | Overwrite / secure deletion |
| **Communications records** | Emails, chat logs, call recordings | Varies: financial services requires longer retention; general commercial = 3 years | Regulatory requirements; limitation periods | 7 years for regulated entities; 3 years for non-regulated | Secure deletion per Section 5 |

**MENA retention minimums:**

| Jurisdiction | Key mandatory minimums |
|---|---|
| UAE | Commercial records: 5 years (UAE Commercial Transactions Law); AML records: 5 years (AML Law); VAT records: 5 years (VAT Law) |
| KSA | Commercial records: 10 years; ZATCA tax records: 10 years; AML records: 10 years (AML Law) |
| Lebanon | Commercial records: 10 years (Code of Commerce); AML records: 5 years (Law No. 318 of 2001) |
| Egypt | Commercial records: 5 years (Tax Law); AML records: 5 years (AML Law No. 80 of 2002) |
| DIFC | Regulated entity records: as specified in DFSA Rulebook; general commercial: 6 years (DIFC Contract Law limitation period) |
| ADGM | Equivalent to DIFC; FSRA Rulebook specifies regulated entity minimums |

### 4. Review and categorisation responsibilities

| Role | Responsibilities |
|---|---|
| Data Protection Officer / Privacy Lead | Maintain and update the Retention Schedule; advise on legal requirements; approve exceptions |
| IT / Systems | Implement technical controls to enforce retention periods; manage secure deletion tools |
| HR | Manage employee data retention; liaise with DPO on employment law minimums |
| Finance / Accounting | Manage financial records in accordance with tax and accounting retention requirements |
| Legal / Compliance | Manage legal files; issue litigation holds; advise on limitation periods |
| All employees | Follow the policy; report data holdings not covered by the schedule; not delete data subject to a litigation hold |

### 5. Secure deletion procedures

**5.1 Electronic data:**
- Standard method: secure overwriting using NIST 800-88 compliant tools (for non-SSD media) or cryptographic erasure (for encrypted media).
- SSD/flash storage: ATA Secure Erase command or physical destruction.
- Cloud data: use the cloud provider's compliant deletion procedure (per DPA terms); obtain written confirmation of deletion.
- Backup media: after the backup retention period expires, securely destroy or overwrite.

**5.2 Paper records:**
- Cross-cut shredding (DIN 66399 security level P-4 or above) or contracted confidential waste destruction service.
- For highly sensitive data: strip-cut shredding (P-5/P-6) or incineration.
- Obtain destruction certificate for records of sensitive data.

**5.3 Confirmation of deletion:**
For all high-value or special-category data deletion, maintain a deletion log confirming: what was deleted, when, by whom, and by what method.

### 6. Litigation hold (legal hold)

When litigation is filed, threatened, or reasonably anticipated, the normal retention schedule is suspended for all data that is potentially relevant:
- The Legal team issues a Litigation Hold Notice to all custodians of relevant data.
- The notice overrides any automated deletion or scheduled destruction.
- All custodians must preserve relevant data until the hold is lifted.
- Failure to preserve relevant data after a hold is issued can result in sanctions in litigation (adverse inference, cost orders, striking out of claims).
- When litigation concludes, the Legal team issues a hold release and the normal schedule resumes.

### 7. Policy review and exceptions
- This policy is reviewed annually by the DPO.
- Requests for exceptions (extending retention beyond the scheduled period or deleting before the minimum) must be approved by the DPO in writing and documented.
- Any change to applicable law that affects retention periods must be reflected in the Retention Schedule within 30 days of the change taking effect.

## Common mistakes

- A Retention Schedule that specifies periods but does not identify who is responsible for enforcing deletion.
- No secure deletion procedure — deleting a file from a computer does not delete the data; the policy must specify the method.
- Not including AML-mandated retention periods — regulatory minimum retention is often longer than the data minimisation preference.
- Forgetting backup media — data deleted from primary systems may persist in backups for years.
- No litigation hold procedure — the most expensive data retention failure is not keeping data that should have been deleted, but deleting data that should have been preserved for litigation.

## Related skills

- [[prompt-pack-data-processing-agreement]]
- [[prompt-pack-data-breach-response-plan]]
- [[prompt-pack-data-subject-access-request-procedure]]
- [[prompt-pack-cross-border-data-transfer-assessment]]
- [[prompt-pack-cookie-policy]]
