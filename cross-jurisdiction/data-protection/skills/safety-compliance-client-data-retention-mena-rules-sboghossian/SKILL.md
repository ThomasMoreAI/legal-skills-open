---
name: safety-compliance-client-data-retention-mena-rules-sboghossian
title: Client Data Retention — MENA Rules
description: Use when configuring client data retention periods for a law firm operating in MENA, or advising on regulatory retention minimums. Covers mandatory retention floors for legal files, AML records, and tax records across KSA, UAE, Lebanon, and Egypt — with applicable bar association rules, AML legislation, and tax law references. Describes Louis's per-matter retention settings, auto-anonymization at the retention floor, and legal-hold freeze functionality.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/safety-compliance/safety-compliance-client-data-retention-mena-rules
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# Client Data Retention — MENA Rules

## When This Applies

Apply this skill when:
- Configuring data retention periods for a law firm or legal team operating in MENA
- Advising a law firm client on how long to keep legal files, client records, or matter documentation
- Setting up Louis's per-matter retention settings for an eFirm tenant
- Determining when a matter file can be closed, anonymized, or purged
- Responding to a data subject access request (DSAR) that requires knowing what client data is still held

## Why Retention Rules Matter

Law firms are subject to two overlapping retention obligations:
1. **Professional obligation** (bar association rules): keep files long enough to defend against malpractice claims and respond to regulatory inquiries
2. **Statutory retention** (AML, tax, corporate): keep records as mandated by specific legislation

Retaining data too long creates privacy law exposure; retaining too short creates professional liability and regulatory risk. The floor set by the most demanding applicable requirement determines the minimum retention period.

## Retention Floors by Jurisdiction

### Saudi Arabia (KSA)

| Record type | Minimum retention period | Authority |
|---|---|---|
| Client legal file / matter documents | 5 years post-matter-close | Saudi Bar Association rules |
| AML / anti-money-laundering records | 10 years | Saudi AML Law and its Implementing Regulations (FATF-aligned) |
| Tax records | 5 years (corporate taxpayers) | Zakat, Tax and Customs Authority (ZATCA) rules |
| Banking / financial documents | 10 years | Saudi Central Bank (SAMA) requirements |

**Note**: for matters involving regulated industries (financial services, healthcare, telecoms), sector-specific regulations may impose longer retention periods. Verify with the relevant regulator.

### UAE

| Record type | Minimum retention period | Authority |
|---|---|---|
| Client legal file / matter documents | 5 years post-matter-close | UAE Bar Association (UAE Federal Law on Legal Profession) |
| DFSA-regulated AML records | 6 years | Dubai Financial Services Authority (DFSA) rules (DIFC firms) |
| UAE federal AML records | 10 years | UAE Federal AML Law (Federal Decree-Law No. 20 of 2018) |
| Tax / VAT records | 5 years | UAE Federal Tax Authority (FTA) requirements |
| Corporate records | 5 years minimum | UAE Companies Law |

**DIFC / ADGM context**: firms in DIFC are regulated by the DFSA; firms in ADGM are regulated by the FSRA. Both have AML/CFT obligations with 6-year retention minimums for regulated activities. Legal practices operating as Designated Non-Financial Businesses and Professions (DNFBPs) are subject to AML retention obligations.

### Lebanon

| Record type | Minimum retention period | Authority |
|---|---|---|
| Client legal file | 10 years (customary / limitation period basis) | No specific bar rule; based on 10-year contractual limitation period under Code of Obligations and Contracts |
| Banking secrecy archives | 5 years | Banque du Liban regulations |
| Tax records | 10 years | Lebanese tax administration practice (Directorate General of Finance) |
| Commercial records | 10 years | Code of Commerce Article 10 (general commercial record-keeping) |

**Practical note**: Lebanon's legal and regulatory environment is in flux. The 10-year customary retention period is prudent given the 10-year general limitation period for contractual claims. Retain client files for at least 10 years post-matter-close.

### Egypt

| Record type | Minimum retention period | Authority |
|---|---|---|
| Client legal file | 10 years post-matter-close | Egyptian Bar Association rules (inferred from 15-year general limitation period; 10 years is the conservative floor) |
| Tax records | 10 years | Egyptian Tax Authority (ETA) requirements |
| AML records | 10 years | Egyptian AML Law No. 80 of 2002 and its executive regulations (Central Bank of Egypt / Financial Regulatory Authority requirements) |
| Commercial records | 10 years | Egyptian Commercial Law (Qanun al-Tijarah) |

## Retention Matrix Summary

| Jurisdiction | Legal file minimum | AML minimum | Tax minimum |
|---|---|---|---|
| KSA | 5 years | 10 years | 5 years |
| UAE | 5 years (Bar) | 10 years (federal AML) / 6 years (DFSA) | 5 years |
| Lebanon | 10 years | N/A (no current comprehensive AML data retention rule) | 10 years |
| Egypt | 10 years | 10 years | 10 years |

**Effective retention period** = the maximum of all applicable floors for the relevant record type.

## Louis eFirm: Per-Matter Retention Settings

Louis's eFirm product allows per-matter retention configuration:

### Setting the Retention Period

When opening a matter, the firm administrator or supervising attorney sets the retention period in the matter settings. The system enforces the following logic:

- **Cannot be set below the statutory floor**: for a KSA matter with AML-covered transactions, the minimum is 10 years — the system will not accept a lower value
- **Can be set above the statutory floor**: if the firm's own policy (e.g., internal risk management) requires 15 years, this is permitted
- **Default**: Louis applies a conservative default of 10 years for all MENA matters (the highest floor across the supported jurisdictions)

### Auto-Anonymization at the Retention Floor

When the retention period expires and no legal hold is active:
1. Louis triggers a **notification** to the matter supervisor confirming that the retention period has expired
2. After a configurable grace period (default: 30 days), Louis **auto-anonymizes** the matter file:
   - Client names are replaced with pseudonyms
   - Personal identification numbers (passport, ID, national ID) are redacted
   - Financial account details are redacted
   - The legal content of the file (clauses, legal analysis, correspondence text without identifying details) is retained for quality assurance and insurance purposes
3. The anonymization is logged in the audit trail with the date and supervising attorney

### Legal Hold Freeze

A legal hold flag prevents auto-anonymization and purging regardless of the retention period expiry:

- **Set by**: the matter supervisor or firm administrator
- **Triggers**: active litigation, regulatory investigation, DSAR requiring preserved evidence, auditor request
- **Effect**: the system freezes all auto-anonymization and deletion scheduled for the matter until the hold is lifted
- **Notification**: the system notifies the matter supervisor 30 days before any scheduled action (anonymization, purge) and prompts confirmation that no hold should be applied

### Legal Hold Release Protocol

When lifting a legal hold:
1. Matter supervisor confirms in writing (within Louis's matter notes) that the hold reason has resolved
2. System re-calculates the retention period from current date (does not use the original expiry — retention clock resets from the hold-lift date to ensure full retention period is served post-resolution)
3. Auto-anonymization scheduled per the above protocol

## Data Subject Access Requests (DSARs) and Retention

If a data subject (e.g., a party to a matter whose personal data was processed) submits a DSAR under KSA PDPL, UAE PDPL, DIFC DPL, or ADGM DPR:

- Louis's matter search function can identify which matters hold that data subject's information
- The legal hold flag should be set on all matters containing the data subject's data while the DSAR is being processed
- The firm's data protection officer (DPO) or equivalent should supervise the DSAR response

## Interaction with AML Obligations

Law firms in MENA are classified as Designated Non-Financial Businesses and Professions (DNFBPs) under FATF recommendations, which have been implemented in KSA, UAE, Lebanon, and Egypt. This imposes:
- Customer due diligence (CDD) / Know-Your-Client (KYC) obligations
- AML record-keeping for: client identification documents, transaction records, due diligence files, suspicious transaction reports (where filed)
- **10-year retention** for AML records is the FATF standard and is adopted in KSA and Egypt; UAE federal law also requires 10 years; DFSA requires 6 years for DIFC-regulated firms

AML records must be kept even if the client matter itself would be closed and anonymized at the shorter legal-file retention floor. Apply the **most demanding floor** per record category.

## Common Mistakes

- Setting a single global retention period (e.g., 5 years for all matters) without considering AML records — which require up to 10 years in KSA and Egypt
- Purging matter files without checking for active legal holds
- Anonymizing before the AML retention floor has passed — AML records must remain identifiable for regulatory inspection purposes
- Failing to log the anonymization event in the audit trail — creates uncertainty about what was purged and when

## Related Skills

- [[safety-compliance-attorney-work-product-ai-handling]]
- [[safety-compliance-ai-not-privileged-disclaimer-us]]
- [[review-ksa-pdpl-readiness]]
