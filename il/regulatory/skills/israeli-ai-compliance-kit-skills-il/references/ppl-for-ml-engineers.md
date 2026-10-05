# Privacy Protection Law for ML Engineers

Practical mapping of Israel's Privacy Protection Law (PPL) and Amendment 13 to real ML pipeline stages. Not legal advice. Consult a qualified Israeli privacy lawyer for enforcement-level questions.

## Key Framework

- Primary statute: Privacy Protection Law, 1981 (Chok Hagnat HaPratiyut)
- Implementing regulations: Data Security Regulations, 2017
- Regulator: Privacy Protection Authority (PPA, Rashut LeHaganat HaPratiyut)
- First AI-specific signal: PPA AI guidance, 2025 (public consultation closed June 5, 2025; still formally in draft as of August 2026, but the PPA enforces it as its operative compliance standard, so align with it as if binding)

## PPL Vocabulary You Will Encounter

| Hebrew term | English | What it means for ML |
|-------------|---------|----------------------|
| Meyda Ishi | Personal information | Any data identifying or related to an individual. Broad. Amendment 13 expands it further |
| Maagar Meyda | Database | Organized collection of personal information. ML training sets often qualify |
| Rasham Hamaagarim | Registrar of Databases | Body where databases above threshold must be registered |
| Beeli-Maagar | Database owner | Legal entity responsible for the database |
| Mamuneh Al Hahayganat Hamida | Data Security Officer | Required role under Data Security Regulations for some databases |
| Memuneh Al Hagat Hapratiyut | Data Protection Officer (DPO) | New under Amendment 13 for certain orgs |
| Tzaava Al Avarat Meyda | Cross-border transfer order | Required for transfers outside Israel in some cases |

## Pipeline Stage Mapping

### Stage 1: Data Collection

Legal questions:
- What is the lawful basis? Consent, contract necessity, legal obligation, legitimate interest?
- Is notice provided to data subjects at collection?
- For web-scraped data: is the source explicitly or implicitly licensing the content?

PPA draft AI guidance is clear: unauthorized scraping of personal data for AI training is prohibited. Scraping from terms-of-service-protected sites creates direct exposure.

Concrete controls:
- Data source registry with lawful basis per source
- Retention of consent records where consent is the basis
- Documented legitimate interest assessment (LIA) where that is the basis
- PII scanning on ingested data

### Stage 2: Data Storage

Legal questions:
- Does the dataset meet Registrar of Databases registration thresholds?
- Are Data Security Regulations 2017 security measures applied?
- What is the retention period and justification?

Concrete controls:
- Encryption at rest
- Access control list with principle of least privilege
- Audit logging of access
- Backup policy with security applied
- Retention clock enforced

### Stage 3: Preprocessing and Feature Engineering

Legal questions:
- Is the purpose of processing aligned with the purpose at collection?
- Has data been minimized to what is needed for the task?
- Are derived features also personal information (PPL definition is broad)?

Concrete controls:
- Purpose limitation policy
- Minimization review per feature
- Feature-level sensitivity tagging
- Pseudonymization or anonymization where appropriate

### Stage 4: Training

Legal questions:
- Can training data be extracted from the model (memorization)?
- Are training runs logged for auditability?
- What access do engineers have to raw training data?

Concrete controls:
- Memorization testing on sensitive classes
- Training logs retained with integrity protection
- Engineer access gated and logged
- Model weight storage at security level appropriate to training data sensitivity

### Stage 5: Inference

Legal questions:
- Are user inputs personal information? Almost always yes
- Are inference logs retained? For how long? Who can see them?
- Can data subjects exercise access, correction, and deletion rights over inference traces?

Concrete controls:
- Input logging policy explicit and user-facing
- Retention timer on inference logs
- Data subject rights workflow covering inference logs
- Vendor DPAs for managed LLM APIs

### Stage 6: Monitoring and Drift Detection

Legal questions:
- Does monitoring re-process personal data?
- Are monitoring records separate from production data and correctly secured?

Concrete controls:
- Monitoring data flow diagram
- Separate retention policy for monitoring traces
- Same security level as training data

### Stage 7: Deletion and Model Decommissioning

Legal questions:
- Can you honor a deletion request for data already in the model?
- Is model retirement documented? Are backups purged?

Concrete controls:
- Deletion request workflow tested end to end
- Documented limitations where deletion from trained weights is infeasible (and mitigation)
- Backup purge schedule
- Model decommissioning procedure

## Amendment 13 Changes (Now In Force)

Amendment 13 entered into force on August 14, 2025. Key changes that are now enforceable:

- Expanded definition of personal information brings more data into scope
- Broader breach notification obligations with tighter timelines
- Increased enforcement powers for the PPA, including administrative financial penalties (fines can reach millions of NIS) and authority to petition for cease-processing or deletion orders
- Sharper data subject rights, including around automated decisions

Budget headcount for DPO if you fall into the triggers. The role must be reasonably independent, reporting high enough in the org to raise issues without retaliation risk.

## Common Mistakes

- Treating PPL database registration as equivalent to GDPR Article 30 records. They are different obligations with different triggers.
- Assuming training data that is "public" is lawful to use. Public does not mean unrestricted. PPA draft AI guidance was explicit on this point.
- Using managed LLM vendors without a DPA or without verifying data residency and sub-processing terms.
- Forgetting that inference logs are personal data and subject to the same rules as training data.
