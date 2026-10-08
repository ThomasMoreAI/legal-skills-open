---
name: draft-engagement-letter-sboghossian
title: Engagement Letter (Law Firm Retainer)
description: Use when drafting a law firm engagement letter (retainer agreement) establishing the terms of legal representation. Covers scope, fee structures (hourly/fixed/contingency/hybrid), trust account requirements, conflict-of-interest acknowledgment, file retention, and termination rights. Includes bar-rule compliance notes for LB, KSA, UAE/DIFC/ADGM, and US (NY, CA) jurisdictions, plus anti-patterns including vague scope and missing estimates.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-engagement-letter
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Engagement Letter (Law Firm Retainer)

## When to use this

An engagement letter establishes the legal services relationship between a law firm (or solo practitioner) and a client. It is the foundational document for:

- Defining what legal services will be provided (and what is out of scope).
- Establishing how the client will be billed and when.
- Recording that a conflict check has been conducted.
- Confirming the client's identity and authority.
- Protecting both parties in the event of a fee dispute.

Most bar associations in MENA, Europe, and the US require written engagement letters for all matters above a minimum fee threshold, or for all matters of substance. Even where not required, an engagement letter is best practice.

Use this skill whenever a lawyer or law firm is beginning a new matter or a new matter phase.

## Required inputs

| Input | Why it matters | Default |
|-------|----------------|---------|
| Firm name, address, supervising lawyer | Identifies the professional responsible | — |
| Client (full legal name + entity type) | Defines who the client is; essential for conflict-check and engagement-letter enforceability | — |
| Matter description (specific and bounded) | Scope disputes are the primary cause of fee disagreements; vague scope benefits neither party | — |
| Fee structure (hourly / fixed / contingency / hybrid) | Determines billing rights; some structures restricted or prohibited in certain jurisdictions | — |
| Conflict-of-interest check confirmation | Bar obligation; firm should have run and documented the check before sending | — |
| Effective date of engagement | When legal obligations on both sides begin | Date of client signature |
| Retainer / advance required (if any) | Some matters require an advance against fees | — |

## Optional inputs
- Estimated total fees (required in some jurisdictions even for hourly matters).
- Named co-counsel or collaborating firms.
- Client authority confirmation (for corporate clients: whose authority; board resolution).
- Dispute-resolution clause for fee disputes (mediation / arbitration preferred over litigation in fee disputes).
- Language of documents (Arabic / English / bilingual).

## Document structure

### 1. Identification of parties
Firm's full name and address. Client's full legal name, entity type (company, individual), and address. If corporate client: confirm the individual signing has authority to engage the firm on behalf of the entity.

### 2. Scope of engagement
**This is the most important section.** Be specific:
- **In scope**: "Advising on and negotiating the acquisition by Client of a 40% stake in Company X, including conducting legal due diligence on Company X's share structure and material contracts, reviewing the Share Purchase Agreement, and attending completion."
- **Out of scope**: "Tax advice, employment law advice, regulatory filings, and any dispute arising post-completion are outside the scope of this engagement unless agreed in a separate engagement letter."

Vague scope ("legal advice as needed") invites scope-creep disputes and makes the letter unenforceable as a fee agreement.

### 3. Fee structure

**Hourly billing**
- Rates by seniority: partner / senior associate / associate / paralegal — state the rate per hour.
- Billing increments: 0.1 hour (6-minute) increments standard in common-law jurisdictions.
- Fee estimate: many bars require a good-faith estimate even for hourly matters. Include with caveat that it is an estimate, not a cap.
- Travel time: state whether billable and at what rate.

**Fixed fee**
- Defined scope locked; fee amount fixed.
- Scope-change mechanism: state the hourly rate for out-of-scope work.
- Payment milestones: on engagement; on delivery of draft; on completion.

**Contingency fee**
- Percentage of recovery; state clearly.
- Expense responsibility: who pays disbursements during the matter.
- Net vs. gross recovery calculation.
- MENA restriction: contingency fees are restricted or prohibited in certain matter types in KSA and LB; see Jurisdictional Notes.

**Hybrid / blended**
- Combination of reduced hourly rate + success fee.
- Define success event precisely.

### 4. Expenses and disbursements
- Pass-through of third-party costs: court fees, notarial fees, translation, expert witnesses, travel.
- Firm's internal expenses policy (printing, courier, etc.): include or cap.
- Advance payment for significant disbursements (e.g., court fees above a threshold).

### 5. Billing cadence and payment terms
- Monthly billing on the last day of each month.
- On-completion billing for fixed-fee matters.
- Payment due within [15 / 30] days of invoice.
- Interest on overdue invoices at [agreed rate].
- Right to suspend services for non-payment after [X] days.

### 6. Retainer / advance
- If required: amount; replenishment trigger (when reduced below a threshold).
- Segregated client trust account: most bar rules require retainers to be held in a separate client trust account, not the firm's operating account.
- Refundable vs. non-refundable retainer — be explicit.
- Return of unused retainer balance on engagement end.

### 7. Conflict-of-interest acknowledgment
> "Prior to accepting this engagement, [Firm Name] has conducted its standard conflict-of-interest review. We have not identified any current conflict of interest that would prevent us from representing you in this matter. You agree to promptly notify us of any new circumstances that could create a conflict with other clients of this Firm."

If there is a potential conflict (e.g., former client relevant to the matter), address it explicitly with appropriate waivers.

### 8. Confidentiality
Bar rules of professional responsibility apply. The firm will maintain client confidences except as required by law, a court order, or an applicable professional rule (e.g., anti-money-laundering reporting obligations). Client agrees to provide all information relevant to the matter.

### 9. File retention
- Duration: files retained for [5/7/10] years after conclusion of the matter (varies by jurisdiction and matter type).
- Destruction: files destroyed after the retention period; client notified.
- Client's right to obtain copies of their own documents.
- Return of original documents on request.

### 10. Termination rights
- **Client's right**: client may terminate at any time for any reason. Fees are due for work completed to termination date.
- **Firm's right**: firm may withdraw for non-payment, client misconduct, conflict of interest, or other bar-rule-permitted grounds, with reasonable notice to allow the client to retain new counsel.
- Post-termination: firm will cooperate in transitioning files to successor counsel.

### 11. Fee disputes
Optional but recommended:
> "Any dispute arising out of or in connection with our fees shall first be referred to the firm's senior partner for review. If unresolved within 30 days, disputes shall be referred to [mediation under [rules] / arbitration under [rules] in [seat]]."

### 12. Governing law
Specify the law governing the engagement letter — typically the jurisdiction where the firm is admitted to practice and where services are primarily rendered.

## Jurisdictional notes

### Lebanon
- The Lebanese Bar Association (Beirut and Tripoli Bars) regulates fee agreements.
- **Contingency fees**: permitted in civil/commercial matters but subject to Bar rules on reasonable percentage. Not permitted for criminal matters.
- Lawyers must be members of the Beirut or Tripoli Bar; foreign lawyers must associate with a Lebanese bar member.
- Written engagement letters are strongly recommended; the Bar recommends using standard form letters.
- Fee disputes: the Beirut Bar has a fee arbitration committee.

### KSA
- Lawyers must be licensed by the Ministry of Justice; foreign law firms may advise on international law only.
- **Contingency fees**: restricted. Contingency arrangements for court matters are disfavoured and may require MOJ declaration or approval.
- Fixed-fee or hourly arrangements are standard.
- Bilingual Arabic/English engagement letters are recommended; Arabic controls.
- Trust accounts: SAMA-licensed bank account required; most firms use escrow arrangements.

### UAE (onshore)
- Lawyers must be licensed by the Ministry of Justice UAE.
- DIFC and ADGM: international law firms may practice without UAE MOJ license in their respective free zones.
- Fee flexibility: all fee structures permitted; no contingency restriction for civil/commercial matters.
- Trust account: no mandatory IOLTA equivalent; client funds should be segregated.

### DIFC and ADGM
- Greater fee flexibility; international market rates and structures.
- DIFC Courts and ADGM Courts enforce engagement letters under common-law principles.
- No restriction on contingency fees for commercial matters.

### US
- Each state bar has specific fee agreement rules (e.g., NY RPC Rule 1.5; CA Rule 1.5).
- Written fee agreements required in CA for most matters; highly recommended in NY.
- Contingency fee agreements must be in writing signed by client.
- IOLTA accounts mandatory for client funds.

## Anti-patterns

| Anti-pattern | Problem | Fix |
|---|---|---|
| Vague scope ("legal advice as needed") | Creates scope-creep disputes; no clear basis for fee | Specify matter, activities included, and exclusions |
| Hourly without estimate | Many bars require an estimate; client cannot budget | Provide good-faith estimate with caveat |
| Retainer held in operating account | Violates bar trust-account rules in most jurisdictions | Open and designate a client trust account |
| No termination provision | Both parties unclear on their rights | Include termination clause with post-termination obligations |
| Contingency in prohibited matter type | Unenforceable and disciplinary risk | Confirm applicable bar rules on contingency |
| No conflict-of-interest check record | Firm cannot prove it checked; disciplinary exposure | Document the check; include confirmation in letter |
| English-only for MENA client | Non-enforceable in local courts | Draft bilingual; Arabic controls |

## Related skills

- [[efirm-engagement-letter-draft]] — eFirm workflow integration for engagement letter generation and client onboarding
- [[draft-msa]] — master services agreement for ongoing advisory relationships
- [[draft-confidentiality-agreement]] — where a separate NDA with the client is needed before the engagement
- [[review-legal-services-agreement]] — reviewing an existing engagement letter or legal services contract
