---
name: prompt-pack-due-diligence-report-sboghossian
title: Due Diligence Report
description: Use when preparing or summarizing a legal due diligence report on a target company in connection with an M&A transaction. Covers corporate structure, material contracts, regulatory compliance, litigation exposure, IP, real estate, employment, and IT/data. Identifies material risks, assigns risk ratings, and recommends deal protections. Relevant for transactions across MENA (UAE, KSA, DIFC, ADGM, LB, EG), UK, EU, and GCC. Trigger when buy-side counsel needs to consolidate findings from document review into a formal report for the client.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-due-diligence-report
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: corporate
language: en
---

# Due Diligence Report

## When to use this

Use this skill when preparing the formal legal due diligence (LDD) report that summarizes findings from review of the target company's documents and advises the buyer on risks, required deal protections, and deal-breakers. The LDD report is the primary deliverable from buy-side legal counsel in any M&A transaction.

Typical triggers:
- Buy-side counsel has completed document review from the VDR and needs to summarize findings
- Client needs an executive summary of legal risks before signing an SPA
- Buyer is evaluating a bid and needs a preliminary red-flag report
- Post-signing, buyer needs a comprehensive LDD report to support indemnity and escrow negotiations

## Required inputs

| Input | Why it matters | Default if omitted |
|---|---|---|
| Target company name and jurisdiction | Identity; determines applicable law and regulatory regime | Ask |
| Buying client name | Addressee of the report; framing of recommendations | Ask |
| Transaction type (share purchase / asset purchase / merger) | Affects which liabilities transfer to buyer | Ask |
| Documents reviewed | The basis for findings; should be listed | Ask; include VDR index if available |
| Key risk areas flagged during review | The substance of the report | Ask in detail |
| Governing law of transaction | Determines deal protections available | Ask |

## Optional inputs

- Industry / sector (affects regulatory and compliance sections)
- Deal timeline and urgency (affects depth of preliminary vs. full report)
- Price / valuation context (affects materiality thresholds)
- Identified deal-breakers or absolute red flags
- Seller's disclosure letter (to cross-reference against)

## Document structure

### Executive Summary

- Transaction overview (target, buyer, deal type, indicative price)
- Overall risk assessment: Green / Amber / Red
- Top 3-5 material risks in plain language
- Recommended deal protections (price chip, escrow, specific indemnities, conditions precedent)
- Any deal-breakers that require resolution before signing

### 1. Corporate Structure and Good Standing

- Target's entity type, jurisdiction, and registration number
- Ownership structure: shareholder register, ultimate beneficial owners
- Corporate approvals required for the transaction
- Subsidiaries and group structure
- Foreign ownership restrictions (critical in MENA — see jurisdictional notes)
- Any ownership or control issues: pledges on shares, pre-emption rights, drag-along/tag-along rights

**Risk indicators**: Nominee structures, unresolved share transfers, dormant subsidiaries with unknown liabilities.

### 2. Material Contracts

- Review of top contracts by value or strategic importance
- Change-of-control clauses requiring third-party consent
- Assignment restrictions
- Unusual termination rights triggered by the transaction
- Key customer and supplier concentration risk

**Risk indicators**: Single-customer dependency; contracts terminable on change of control without consent obligations.

### 3. Intellectual Property

- Registered IP (trademarks, patents, domain names): ownership confirmed in target's name
- Software: licensed or owned; open-source compliance
- Employee IP assignment agreements: all creators have assigned IP to target?
- IP infringement claims or third-party challenges

**Risk indicators**: Key IP registered in founder's personal name; missing assignment agreements; open-source code in commercial products without compliance.

### 4. Regulatory and Licensing

- All material licenses and permits held by target
- Sector-specific regulatory requirements (financial services, healthcare, education, food, telecoms)
- Foreign direct investment approvals required for the acquisition
- Anti-trust / competition filings required

**Risk indicators**: Expired or missing licenses; regulatory investigations; FDI approval required from government authority.

### 5. Litigation and Disputes

- Active litigation, arbitration, regulatory proceedings
- Threatened claims; outstanding demand letters
- Judgment enforcement history

**Risk indicators**: Pending claims exceeding X% of deal price; unresolved regulatory enforcement actions; criminal investigations.

### 6. Employment and HR

- Total headcount; senior management key-person risk
- Employment contracts: fixed-term vs. indefinite; unusual terms
- Pending employment claims and tribunal proceedings
- Employee benefits and accrued obligations (gratuity, pension, NSSF)
- Non-compete / non-solicitation enforceability

**Risk indicators**: Unfunded end-of-service gratuity obligations; pending discrimination or wage claims; key executives without retention arrangements.

### 7. Real Estate and Physical Assets

- Owned and leased properties: title confirmed?
- Lease terms: change-of-control clauses, renewal rights, rent review
- Planning or building violations

**Risk indicators**: Missing title deeds; defective title; leases terminable on change of control.

### 8. Tax

- Tax filings and payment status; open assessments
- Transfer pricing; related-party transactions at arm's length?
- Withholding tax obligations on dividends, intercompany payments
- Tax losses and deferred tax positions

**Risk indicators**: Underpaid tax; active audit; transfer pricing risks; non-arm's-length related-party transactions.

### 9. IT / Data Protection

- Data protection compliance: applicable law (GDPR, UAE PDPL, KSA PDPL, etc.)
- Data breaches or regulatory investigations
- IT infrastructure: outsourced vs. in-house; key vendor dependencies

**Risk indicators**: Notifiable data breaches not yet addressed; non-compliant data retention practices; material IT systems under terminating third-party contracts.

### 10. Risk Summary Table

| Risk | Description | Severity | Recommended Mitigation |
|---|---|---|---|
| [Risk A] | [Brief description] | High / Medium / Low | [Specific deal protection] |

### 11. Recommended Deal Protections

- Specific indemnities (identified known liabilities the seller should indemnify)
- Price adjustment mechanisms (locked box, completion accounts)
- Escrow arrangement (percentage of purchase price; term)
- Conditions precedent (regulatory approvals, third-party consents)
- Material adverse change (MAC) clause triggers
- Warranty and indemnity (W&I) insurance recommendation

## Jurisdictional notes

### MENA — Key Structural Considerations

| Jurisdiction | Foreign ownership | Mandatory approvals | End-of-service gratuity |
|---|---|---|---|
| **UAE** | UAE Companies Law limits foreign ownership in many onshore sectors; recent reforms allow 100% foreign ownership in most non-strategic sectors; strategic sectors require local partner | No general FDI screening authority; sector-specific approvals (Central Bank, Telecom, Energy) | Mandatory under UAE Labour Law; fully funded — acquirer assumes obligation; quantify in due diligence |
| **KSA** | SAGIA/MISA licenses required for foreign investors; restricted activity list | MISA investment license; Competition Authority merger review if thresholds met | Mandatory end-of-service award under Labour Law; calculate based on years of service |
| **Lebanon** | Foreign ownership of real estate restricted (Law 296/2001); financial institutions require BdL approval; general commercial entities less restricted | BdL approval for financial institutions; no general FDI screening | NSSF contributions and severance indemnity; significant underfunded obligations common in distressed deals |
| **Egypt** | Investment Law provides protections; real estate and media restrictions | Competition Authority approval if thresholds met; Central Bank for financial institutions | NSSF and statutory compensation; often underfunded in SME targets |
| **DIFC / ADGM** | 100% foreign ownership; no restrictions | DFSA / FSRA approval for regulated activities | DIFC Employment Law — DEWS scheme (defined contribution); quantify transferred obligations |

## Common mistakes

- **Materiality threshold miscalibration**: Setting thresholds too high causes material risks to be buried; too low drowns the report in noise. Calibrate to deal size.
- **No deal protection recommendations**: A report that identifies risks without recommending specific deal protections (escrow, specific indemnity, conditions precedent) has failed its purpose.
- **Ignoring gratuity and NSSF underfunding**: In MENA deals, accrued but unfunded end-of-service gratuity obligations are routinely underestimated; they can represent a material deal adjustment.
- **Missing change-of-control clauses**: A material contract that terminates automatically on change of control is a deal-breaker; every material contract must be reviewed for this.
- **Not flagging FDI approval requirements**: Failure to identify required government approvals as a condition precedent can cause deals to close unlawfully or require reversal.

## Related skills

- [[prompt-pack-due-diligence-request-list]]
- [[prompt-pack-disclosure-letter]]
- [[prompt-pack-escrow-agreement]]
- [[prompt-pack-investment-agreement-venture-capital]]
