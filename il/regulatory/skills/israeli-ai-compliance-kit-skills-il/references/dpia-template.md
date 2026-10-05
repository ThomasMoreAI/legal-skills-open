# DPIA Template (Israeli PPL-aligned)

Data Protection Impact Assessment template aligned to the Israeli Privacy Protection Law and Amendment 13 (in force since August 14, 2025). Use this as a starting point for an ML system that processes personal data. Not legal advice.

## 1. System Identification

- System name:
- Owner (legal entity):
- Owner (named responsible person or role):
- System version:
- DPO name (if applicable):
- Data Security Officer name (if applicable):
- Assessment date:
- Next review date:

## 2. Purpose and Necessity

### 2.1 Purpose
Describe the purpose of the processing in plain language. Why does this system exist? What decisions or actions does it support?

### 2.2 Necessity
Why is processing personal data necessary for this purpose? Could the purpose be achieved with less data, anonymized data, or without ML at all? Justify.

### 2.3 Lawful basis
Identify the lawful basis under PPL. Examples: consent, contract necessity, legal obligation, vital interests, public task, legitimate interest. Document the analysis, not just the label.

## 3. Data Flow

### 3.1 Data sources
List each source of training, validation, and inference data. For each source: origin, lawful basis, consent status (if applicable), license terms, collection date range.

### 3.2 Data categories
List the categories of personal information processed. Flag sensitive categories (health, ethnicity, religion, political opinion, sexual orientation, biometric, genetic, criminal).

### 3.3 Data subjects
Who are the individuals whose data is processed? How many, approximately? Are any vulnerable groups involved (children, patients, employees in subordinate positions)?

### 3.4 Data flow diagram
Attach or describe the flow: collection → storage → preprocessing → training → inference → monitoring → deletion. Note crossings of organizational or national boundaries.

## 4. Processing Operations

### 4.1 Training
What processing happens during training? What intermediate data is created? How are training runs logged?

### 4.2 Inference
What is sent to the model at inference time? What is returned? What is logged?

### 4.3 Monitoring and drift detection
What data is re-processed for monitoring? Where is it stored? Who accesses it?

### 4.4 Automated decision-making
Does the system make automated decisions that significantly affect individuals? If yes, describe the human-in-the-loop mechanism and the appeal process.

## 5. International Transfers

List every jurisdiction where personal data is processed or stored, including managed LLM vendor locations and cloud provider regions. For each transfer outside Israel: legal mechanism, adequacy assessment, and safeguards.

## 6. Security Measures

Map to Data Security Regulations 2017:

- Access control (principle of least privilege, authentication, authorization)
- Encryption (in transit, at rest, for backups)
- Audit logging (what is logged, retention, tamper protection)
- Backup and disaster recovery
- Physical security
- Network segmentation
- Vulnerability management
- Incident response
- Personnel security (training, NDAs, access revocation)

## 7. Data Subject Rights

How the system honors each right:

- Access
- Correction
- Deletion (including limits when data is baked into model weights)
- Objection to automated decisions
- Portability (if applicable)

Describe the workflow and SLA for each.

## 8. Risk Analysis

For each identified risk, document:

- Risk description
- Likelihood (low / medium / high) with reasoning
- Severity (low / medium / high) with reasoning
- Affected data subjects (numbers, categories, vulnerability)
- Existing controls
- Residual risk
- Additional mitigations proposed
- Owner and deadline for mitigations

Common risks for ML systems:
- Training data leakage via memorization
- Bias producing discriminatory outcomes
- Re-identification of anonymized data
- Unauthorized access to training data
- Vendor sub-processing outside agreed jurisdictions
- Inference log retention beyond necessity
- Security incidents affecting model weights
- Improper deletion when data subjects exercise rights

## 9. Consultation

- Did you consult the DPO? Date and summary.
- Did you consult affected stakeholders or representative groups? Summary.
- Did you consult the Privacy Protection Authority where required? Summary.

## 10. Decision

- Approved to proceed
- Approved with conditions (list conditions and owners)
- Not approved (reasons and alternatives)

Signed by:
- DPO (if applicable)
- Legal
- System owner
- Executive sponsor

## 11. Review Schedule

This DPIA must be reviewed when:
- The processing purpose changes
- New data categories are added
- The system is materially updated
- A new cross-border transfer is introduced
- A security incident affects personal data
- PPL is amended (including any secondary regulations under Amendment 13)
- At minimum, annually

## Notes on Amendment 13

Amendment 13 came into force on August 14, 2025 and introduces or expands several obligations that affect this DPIA:

- Expanded personal information definition
- Sharper breach notification timelines
- Increased enforcement powers for the PPA, including administrative financial penalties (potentially millions of NIS) and authority to petition for cease-processing or deletion orders
- Stronger data subject rights over automated decisions

Existing DPIAs drafted before August 2025 should be reviewed and updated to reflect the amendment's obligations.
