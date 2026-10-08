---
name: conversation-intake-msa-sboghossian
title: Intake — MSA (Master Services Agreement)
description: Use when a user wants to draft or negotiate a Master Services Agreement (MSA) and Claude must gather the commercial, IP, liability, and data-protection inputs before generating the document. Triggers on requests to prepare a framework services contract, master agreement, or any umbrella commercial arrangement that will govern future statements of work. Covers multi-jurisdictional use cases (UAE, DIFC, KSA, LB, EU, UK, US) with attention to GDPR / PDPL data-processing addendum requirements.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/conversation/conversation-intake-msa
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Intake — MSA (Master Services Agreement)

## When this applies

Activate when a user wants to draft an MSA (Master Services Agreement), framework services contract, or any umbrella commercial arrangement under which future work orders or statements of work (SOWs) will be issued. This skill collects the thirteen structural inputs before routing to [[draft-msa]]. A thin intake here produces an MSA that misallocates IP, caps liability at the wrong level, or omits a data-processing addendum that is legally required.

## Behavior

Multi-turn intake (two to three turns for complex arrangements). Extract any information already given. Confirm the data-protection exposure early — if personal data will be processed, a Data Processing Addendum (DPA) is legally required in the EU (GDPR), UAE (PDPL), and KSA (PDPL) contexts, and failing to include one exposes both parties to regulatory risk.

## Required fields

### 1. Parties

- **Provider**: full legal name, entity type, CR/registration number, registered address.
- **Customer**: same. Confirm whether the customer is a government entity, regulated financial institution, or healthcare provider — these sectors impose additional obligations (security, audit rights, localization) that must be reflected in the MSA.

### 2. Scope

What services will the Provider deliver to the Customer under this framework?
- General description of the service category.
- Whether the scope is fully defined in the MSA body or deferred to individual SOWs (statements of work or work orders). Most MSAs use the latter: the MSA sets the legal framework; each SOW specifies deliverables, timelines, fees, and acceptance criteria for a particular engagement.
- Confirm whether any services involve regulated activities (financial advice, legal services, medical services, data processing of sensitive personal data) — these require additional language or separate licensing.

### 3. Term, termination, and renewal

- **Initial term**: 1 year, 2 years, evergreen?
- **Termination for convenience**: either party may terminate on notice? Confirm notice period (30, 60, 90 days). Confirm whether fees already committed under active SOWs survive termination.
- **Termination for cause**: events that permit immediate termination without notice (material breach not cured within 30 days; insolvency; change of control).
- **Auto-renewal**: rolls over unless notice given before renewal date? Renewal notification window (e.g., 60-day notice window before anniversary).
- **Survival**: which provisions survive termination (confidentiality, IP, indemnity, limitation of liability, governing law)?

### 4. Fees, payment terms, and invoicing

- Fee model: time-and-materials, fixed fee per SOW, retainer, milestone-based, or SaaS subscription?
- Currency and payment timeline (net 30, net 45, net 60 — net 30 is market standard; longer terms common in GCC government procurement).
- Invoicing cadence: monthly, milestone, upon delivery, upon acceptance?
- Late payment: statutory interest (UK: Late Payment of Commercial Debts (Interest) Act 1998 — 8% over Bank of England base rate; EU: Late Payment Directive; UAE: contractual rate agreed or Central Bank overnight rate; KSA: contractual or courts apply equity).
- Disputed invoices mechanism: suspension of payment pending dispute resolution; payment of undisputed portion.

### 5. Confidentiality and IP

This is one of the most negotiated sections. Clarify each:

- **Confidentiality**: mutual or one-way? Duration: perpetual for trade secrets; typically 3–5 years for general information. Carve-outs: publicly available, independently developed, third-party disclosed, legally compelled.
- **Ownership of work product** (deliverables): who owns IP created specifically for the Customer under a SOW?
  - **Customer owns**: typical for bespoke software, custom reports, creative work.
  - **Provider owns; grants license to Customer**: typical for SaaS platforms and tool-based services; Customer gets a perpetual license to use the deliverable.
  - **Joint ownership**: rarely workable (requires mutual consent to exploit); avoid unless specifically required.
- **Background IP**: each party's pre-existing IP remains their own. Provider grants Customer a license to use background IP only to the extent necessary to use the deliverables.
- **License-back**: if Customer provides materials to Provider (data, brand assets, APIs), confirm the scope of the license back to the Provider for the purpose of delivering the services.
- **Open-source disclosure**: if deliverables incorporate open-source software, confirm which licenses (GPL, MIT, Apache) and whether they affect the Customer's ability to commercialize.

### 6. Warranties and service levels

- **Provider warranties**: will perform services in a professional and workmanlike manner; services will conform to specifications in the SOW for a warranty period (30, 60, 90 days post-delivery).
- **SLA / service levels**: if the services are ongoing (SaaS, managed services), confirm availability targets (99.5%, 99.9%), incident response times, and remedies for breach of SLA (service credits, escalation, termination right).
- **Disclaimer of implied warranties**: standard in common-law jurisdictions (DIFC, UK, US); note that civil-law jurisdictions (LB, FR) have non-waivable implied warranty of fitness for purpose in some contexts.

### 7. Indemnity and liability cap

- **Indemnity triggers**: Provider indemnifies Customer for third-party IP infringement claims; each party indemnifies the other for gross negligence and willful misconduct; data breach indemnity.
- **Liability cap**: total aggregate liability capped at what amount?
  - Common formulas: 100% of fees paid in the prior 12 months; fixed monetary cap; per-incident cap.
  - Note: a cap that is too low may not incentivize performance; a cap too high may be uninsurable.
- **Exclusion of consequential damages**: standard commercial practice to exclude lost profits, loss of revenue, loss of data, indirect loss. Note: UK Unfair Contract Terms Act 1977 and Consumer Rights Act 2015 prohibit exclusion of liability for death/personal injury; similar rules in UAE and LB consumer-facing contracts.
- **Carve-outs from the cap**: death/personal injury; IP indemnity; fraud; willful misconduct; data breach obligations.

### 8. Insurance

- Professional indemnity (PI/E&O) — confirm minimum coverage amount.
- Cyber liability insurance — increasingly required for technology providers processing personal data.
- General commercial liability.
- Workers' compensation (employer's liability) if applicable.
- Confirm that certificates of insurance are provided before services commence and are maintained throughout the term.

### 9. Data protection

**Critical for any MSA involving personal data**:

- Does the Provider process personal data on behalf of the Customer? If yes, a Data Processing Addendum (DPA) is required.
- Applicable law:
  - **EU/UK**: GDPR (Regulation 2016/679); UK GDPR; SCCs required for transfers to non-adequate third countries.
  - **UAE**: Federal Decree-Law No. 45/2021 on Personal Data Protection (PDPL); cross-border transfer restrictions apply.
  - **KSA**: Personal Data Protection Law (PDPL, Royal Decree M/19); executive regulations issued by SDAIA; data localization for sensitive data.
  - **LB**: draft data protection law not yet enacted as of 2025 (verify current status); privacy obligations arise under general civil law.
- DPA minimum content: subject matter and purpose of processing; nature and categories of personal data; obligations and rights of the data controller; sub-processor authorization and flow-down obligations; security measures; data subject rights assistance; breach notification (72 hours under GDPR; KSA PDPL: notify SDAIA and data subjects "without undue delay").

### 10. Subcontracting and assignment

- May the Provider subcontract work without Customer consent? If yes, Provider remains responsible for subcontractor performance.
- Change-of-control: does assignment of the MSA trigger Customer consent rights? Particularly important for Customer who is procuring AI services — if the AI vendor is acquired, the Customer may want termination rights.

### 11. Force majeure

- Events: pandemic, war, natural disaster, government action, cyberattack (increasingly included post-2020), infrastructure failure (power, internet).
- Obligations: notice within X days; obligation to mitigate; termination right if force majeure continues beyond 90/180 days.
- Note: force majeure does not excuse payment obligations that have already accrued.

### 12. Governing law and dispute resolution

| Option | Typical use |
|---|---|
| DIFC + DIFC Courts | International commercial services in or connected to UAE; English-language; judgment enforcement via DIFC-UAE gateway |
| UAE onshore + UAE courts | Domestic UAE transactions; Arabic proceedings |
| KSA + KSA courts | Saudi customers; SAMA-regulated services |
| LB + LB courts | Lebanon domestic; caution: enforce-ability of judgments against foreign counterparties requires separate analysis |
| English law + LCIA / ICC | International MSAs; widely used by multinationals |
| Tiered DR: negotiation → mediation → arbitration | Complex international deals; gives parties escalating options before arbitration |

Confirm venue for arbitration (DIAC, DIFC-LCIA, ICC Paris, LCIA London, CRCICA Cairo) if arbitration is chosen.

### 13. Notices addresses

Formal notice addresses for both parties (including email where contractually effective for notice purposes — confirm whether email notice is accepted under the governing law).

## Output

At the end of intake, produce:

1. A structured intake summary confirming all thirteen fields and outstanding items.
2. A flag if a DPA addendum is required (data-processing scenario confirmed).
3. A routing instruction to [[draft-msa]] with the completed intake data, and to [[draft-statement-of-work]] for the first SOW template if requested.

## Do not

- Draft the MSA without confirming IP ownership — it is the most frequently disputed clause post-signature.
- Omit the DPA addendum flag when personal data is being processed — it is a compliance requirement, not optional.
- Apply US-style "work-for-hire" copyright language to civil-law jurisdictions (UAE, LB, FR) — works created by employees vest in the employer under local law; works created by independent contractors do not automatically vest without an express assignment.

## Related skills

- [[draft-msa]]
- [[draft-statement-of-work]]
- [[conversation-intake-nda]]
- [[kb-commercial-contracts-mena]]
- [[kb-data-protection-mena]]
- [[conversation-uncertainty-language]]
