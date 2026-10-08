---
name: prompt-pack-agreement-legal-draft-review-sboghossian
title: Agreement / Legal Draft Review
description: Use when reviewing an existing agreement or legal draft to identify legal risks, tax implications, and compliance issues. This prompt-pack skill for corporate/commercial review applies a structured risk-flagging methodology across contract law, regulatory compliance, and tax — with MENA-specific attention to civil-law defaults, mandatory provisions, and cross-border enforceability traps.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-agreement-legal-draft-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Agreement / Legal Draft Review

## When to use this

Use this skill when a user needs a structured review of an existing agreement or legal draft to identify:
- Legal risks and exposure
- Tax implications
- Compliance issues (regulatory, mandatory law, competition law)
- Unfavorable terms, missing protections, or unusual provisions
- Cross-border enforceability issues

This is the general-purpose contract review prompt. For specialized document types (NDA, employment contract, arbitration clause), the relevant specialist skill should be layered alongside this one.

---

## Prompt template

> Review the following agreement and identify legal risks, tax implications, and clauses that may create compliance issues.

Use [[conversation-clarifying-questions]] to elicit jurisdiction, parties, and purpose before applying this prompt.

---

## Required inputs

| Input | Why it matters |
|-------|---------------|
| The agreement text | Core input |
| Jurisdiction(s) | Determines applicable mandatory law, tax treatment, and regulatory framework |
| Reviewing party | Risk analysis is always party-specific — a clause favorable to Buyer is unfavorable to Seller |
| Purpose of review | Transactional review vs. compliance audit vs. regulatory submission |

---

## Review methodology

Apply the following four-pass review:

### Pass 1 — Structural completeness
Check that the agreement has all essential components:
- Parties identified with full legal names and jurisdiction
- Consideration (what each party is giving)
- Term and termination provisions
- Governing law and dispute resolution
- Signature blocks appropriate for the jurisdiction

Flag missing sections as **Gap — Missing provision**.

### Pass 2 — Legal risk clauses
Examine each substantive clause for legal risk. Key categories:

| Risk category | What to check |
|--------------|--------------|
| Liability | Is liability capped? At what amount? Are consequential damages excluded? Is the cap realistic? |
| Indemnity | Who indemnifies whom? Are indemnities mutual or unilateral? Is there a procedure (notice, control)? |
| Termination | Notice periods adequate? Grounds for termination for cause well-defined? Effect of termination on accrued rights? |
| IP | Ownership of work product clearly assigned? License scope defined? Moral rights addressed (civil-law jurisdictions)? |
| Confidentiality | Definition of confidential information clear? Duration reasonable? Carve-outs for public domain, prior knowledge? |
| Force majeure | Definition broad enough to cover relevant risks? Notification requirements? Duration after which either party may terminate? |
| Governing law / jurisdiction | Applicable? Enforceable? Does it conflict with mandatory local law? |
| Payment / financial | Currency specified? Payment timing? Late payment remedy (interest vs. suspension — note: riba prohibition in KSA)? |

### Pass 3 — Tax implications
Identify clauses with tax implications:
- Withholding tax on cross-border payments (especially royalties, management fees, interest)
- VAT / GST treatment of supplies under the agreement
- Permanent establishment risk from the agreement structure
- Transfer pricing implications if between related parties
- Stamp duty / registration fees (LB, EG: contract stamping costs)

Flag tax issues as requiring specialist tax counsel review; do not provide definitive tax advice.

### Pass 4 — Compliance and mandatory law
- Applicable competition law (UAE Competition Law, KSA Competition Law) — does the agreement contain exclusivity or price-fixing elements that require clearance?
- Data protection requirements (UAE PDPL Federal Decree-Law 45/2021, Saudi PDPL, DIFC Data Protection Law, GDPR for EU parties) — does the agreement address data sharing?
- Anti-bribery / anti-corruption provisions — is there an FCPA / UKBA / equivalent representation where required?
- Sector-specific regulation (financial services, healthcare, real estate) — does the agreement comply?
- Mandatory law overrides — identify clauses that may be unenforceable because local mandatory law applies (e.g., MENA commercial agency law, UAE labour law)

---

## Output format

Structure the review as:

```
## Review Summary
[2-3 sentence overall risk assessment: high / medium / low risk; key findings]

## Structural Issues
[List of missing provisions or structural gaps]

## Risk Register
| Clause | Issue | Risk Level | Recommendation |
|--------|-------|-----------|----------------|
| §X | ... | High / Medium / Low | ... |

## Tax Flags
[Bullet list of tax issues for specialist review]

## Compliance Issues
[Bullet list of regulatory compliance concerns]

## Recommended Redlines
[Specific redline suggestions for the highest-risk clauses]
```

Risk levels:
- **High**: material legal exposure; recommend addressing before execution
- **Medium**: notable issue; recommend addressing or acknowledging the risk
- **Low**: minor issue or stylistic concern; note for completeness

---

## Jurisdictional notes

### Civil-law jurisdictions (LB, UAE-onshore, EG, FR)
In civil-law jurisdictions, the Civil Code fills contractual gaps with default rules. This means:
- A missing provision may not be a fatal gap — the Code provides a default
- But the Code's default may not be favorable — review the applicable Code provisions before concluding a gap is acceptable
- Good faith (bonne foi / حسن النية) is implied by law; it cannot be contracted out
- Limitation of liability clauses are enforceable but subject to proportionality review by courts; deliberately harmful conduct cannot be limited

### Common-law jurisdictions (DIFC, ADGM, UK)
- Caveat emptor (buyer beware) means gaps are riskier — there is no statutory default framework as comprehensive as a Civil Code
- Entire agreement clauses are more significant: they exclude pre-contractual representations
- Penalty clauses: post-Cavendish Square Holding BV v Makdessi [2015] UKSC 67, penalty clauses are enforceable unless they are unconscionable — but MENA practitioners often use US-style LDs clauses that may be read as penalties

### KSA
- Interest (riba) clauses are unenforceable under Sharia law; late-payment provisions must use alternative formulations
- Liability caps expressed as multiples of contract value are generally enforceable
- Exclusive dealing arrangements may require notification to the General Authority for Competition

---

## Limits and escalation

This review identifies legal risks for the reviewing party's consideration. It does not:
- Constitute legal advice on whether to proceed with the transaction
- Replace specialist tax, competition, or sector-regulatory counsel on specific issues flagged
- Assess factual or commercial due diligence (credit risk, counterparty reputation)

Flag all High-risk items for attorney review before execution.

---

## Related skills

- [[review-contract-general]] — the deep-dive contract review skill
- [[heuristic-always-state-jurisdiction-first]] — ensure jurisdiction is established before review
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]] — identify US boilerplate that does not work in civil law
- [[output-table-of-comparisons]] — multi-jurisdiction comparison format for cross-border agreements
- [[router-confidence-scorer]] — confidence calibration for uncertain legal positions
