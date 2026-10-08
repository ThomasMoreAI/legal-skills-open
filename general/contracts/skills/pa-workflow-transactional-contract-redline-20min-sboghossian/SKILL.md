---
name: pa-workflow-transactional-contract-redline-20min-sboghossian
title: Transactional Contract Redline — 20-Minute Workflow
description: Use when a transactional lawyer needs to perform a rapid first-pass redline review of a commercial contract within a 20-minute time budget. Produces a structured redline with prioritized issues, covering key commercial and legal risk areas across multiple jurisdictions. Designed to front-load the most critical issues so counsel can focus senior attention on flagged items rather than spending time on lower-risk provisions.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-transactional-contract-redline-20min
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Transactional Contract Redline — 20-Minute Workflow

## Purpose

A 20-minute redline is a structured triage — not a comprehensive legal review. The goal is to surface the 5–10 issues that most lawyers would redline on first read, provide draft redlined language for each, and give counsel a prioritized starting point so they spend time on risk, not routine scanning.

This workflow is calibrated for experienced practitioners who want AI to handle the first pass so they can focus their attention where it matters. It is not a substitute for full legal review.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Contract (full text) | Yes | PDF, Word, or plain text |
| Client's position | Yes | Buyer / seller / service provider / customer / licensor / licensee |
| Jurisdiction | Recommended | Governs legal standards for flagged issues |
| Contract type | Recommended | MSA, NDA, SPA, joint venture, lease, employment — determines which issues are most critical |
| Key commercial terms already agreed | Optional | Prevents flagging intentional deviations |
| Deal context | Optional | Cross-border? M&A? Startup? Corporate? Context calibrates risk tolerance |

## 20-Minute Review Scope

The 20-minute target covers:

1. **Liability and indemnification** (5 minutes)
2. **Governing law and dispute resolution** (3 minutes)
3. **Payment terms and pricing** (3 minutes)
4. **Term, termination, and exit rights** (3 minutes)
5. **IP ownership and licensing** (3 minutes)
6. **Confidentiality scope** (2 minutes)
7. **Key missing provisions** (1 minute)

Not covered in 20-minute triage (require full review):
- Regulatory compliance representations
- Complex schedules (SLAs, technical specifications)
- Tax structuring
- Change of control provisions (unless triggered)

## Review Methodology

### Liability and Indemnification

Flag:
- **No liability cap or an insufficient cap**: library standard is typically 12 months' fees; caps below 6 months are almost always worth redlining
- **One-sided indemnification**: indemnity flowing only one way without mutual equivalent
- **Gross negligence / fraud carve-out missing**: the cap should always exclude gross negligence, fraud, and willful misconduct
- **Consequential damages waiver**: both sides should have symmetrical consequential damages exclusion — or flag if it only protects one party
- **Third-party claim indemnity without notice / cooperation requirements**: indemnitor must have right to control defense

MENA note: UAE courts (and KSA courts) may modify disproportionate penalty clauses under their Civil Codes. However, this does not mean a bad liability clause is acceptable — flag it and let counsel decide whether to rely on judicial moderation.

### Governing Law and Dispute Resolution

This is a must-check on every MENA contract:
- Is governing law specified? If not, flag MISSING and provide standard clause.
- For UAE mainland entities: UAE law + UAE courts, or contractually opt for DIFC/ADGM governing law + DIAC/ADCCAC arbitration
- For KSA entities: Saudi law + SCCA arbitration is increasingly standard for commercial contracts
- For DIFC / ADGM entities: DIFC/ADGM law + respective court or arbitration
- Avoid UK law for contracts performed entirely in a MENA jurisdiction — enforceability risk if the counterparty or assets are onshore

Seat of arbitration vs. place of performance: these do not need to match, but MENA-seated arbitrations (DIAC, ADCCAC, SCCA) are generally better for enforcement against local counterparties.

### Payment Terms and Pricing

Flag:
- **No interest on late payment**: in Islamic-finance-context contracts (KSA, UAE for some entities), interest is Riba — use "late payment compensation" or "administrative fee" instead
- **Unilateral price change rights**: any right to change pricing without notice or consent
- **Invoicing requirements**: missing invoice specifications delay payment legitimately under most governing laws
- **Set-off rights without restriction**: unrestricted set-off can be used by a counterparty to avoid payment on disputed amounts

### Term, Termination, and Exit Rights

Flag:
- **Auto-renewal without notice**: contracts that auto-renew for long periods without a cancellation window
- **Termination for convenience rights**: does client have the right to exit without cause? At what cost?
- **No termination for breach**: if no termination right on breach, or if cure period is too long
- **Survival clause absent**: key provisions (confidentiality, IP, indemnification) should survive termination

### IP Ownership and Licensing

Flag:
- **Work-for-hire clause without client ownership**: service agreements where vendor retains IP in deliverables developed specifically for client
- **Background IP creep**: broad definitions of licensed IP that capture the client's own pre-existing materials
- **No-license-back**: if client must use vendor's IP to use deliverables, there must be a license
- **Open-source contamination**: service agreements should warrant that deliverables do not incorporate open-source code with copyleft requirements

### Confidentiality

Flag:
- **No confidentiality clause**: any contract involving exchange of sensitive information
- **No return or destruction obligation**: standard practice is to require return or certified destruction on termination
- **Permitted disclosure too broad**: "employees and contractors who need to know" is fine; "affiliates and advisors" without restrictions is too broad

## Output Format

```markdown
## 20-Minute Redline Report — [Contract Name] — [Date]
**Client position**: [Service Provider / Customer / etc.]
**Jurisdiction**: [UAE/DIFC/etc.]
**Contract type**: [MSA / NDA / SPA / etc.]
**Review time**: [actual time]

---

### PRIORITY 1 — FIX BEFORE SIGNING (3 issues)

#### Issue 1 — Liability cap is 1 month of fees (Clause 15.1)
**Risk**: Inadequate protection for [client]
**Current**: "...fees paid in the preceding month..."
**Proposed**: "...fees paid in the preceding twelve (12) months..."
**Rationale**: Market standard for MSAs in this category is 12 months; 1 month leaves [client] grossly exposed on a multi-year contract.

---

### PRIORITY 2 — NEGOTIATE (4 issues)
[Issues where client position is unfavorable but not critical]

---

### PRIORITY 3 — NOTE (2 issues)
[Non-standard but not immediately harmful]

---

### MISSING PROVISIONS
- [ ] Governing law and dispute resolution — add: [standard DIFC clause]
- [ ] Data protection schedule — required if personal data is processed
```

## Limits

- This is a first-pass triage. It does not replace full legal review for high-stakes transactions.
- Complex schedules, regulatory compliance, and tax implications are outside the 20-minute scope.
- Arabic-language contracts require Arabic parsing; flag if translation is needed before review.
- For contracts above USD 1M in value or involving property or IP transfers, escalate to full review.

## Related Skills

- [[pa-workflow-transactional-clause-library-check]]
- [[pa-workflow-transactional-nda-triage-red-yellow-green]]
- [[pa-workflow-transactional-msa-against-firm-playbook]]
- [[pa-workflow-transactional-deal-point-analysis]]
- [[router-legal-flows]]
