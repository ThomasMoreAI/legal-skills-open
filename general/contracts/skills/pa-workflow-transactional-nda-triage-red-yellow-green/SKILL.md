---
name: pa-workflow-transactional-nda-triage-red-yellow-green
title: Transactional NDA Triage — Red / Yellow / Green
description: Use when a transactional lawyer or in-house team needs to rapidly triage an incoming NDA and assign a red / yellow / green approval status before investing full review time. Produces a structured triage report with a three-color risk rating, flagged issues by severity, and a recommended next step (sign as-is, redline specific points, or escalate). Applicable across multiple jurisdictions; MENA-aware for UAE, KSA, LB, and EG NDAs.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-transactional-nda-triage-red-yellow-green
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Transactional NDA Triage — Red / Yellow / Green

## Purpose

NDAs are high-volume, low-to-medium risk documents. An in-house team reviewing dozens per month cannot afford full legal review on every NDA. This triage workflow applies a structured three-color gate:
- **GREEN**: safe to sign with no or minimal changes
- **YELLOW**: sign after specific targeted redlines; no further escalation needed
- **RED**: escalate to senior counsel; significant issues require resolution before signing

The workflow outputs a decision in under 5 minutes and, where the rating is YELLOW, provides the specific redlines needed.

## Inputs

| Input | Required | Notes |
|---|---|---|
| NDA text | Yes | PDF, Word, or plain text |
| Client's position | Yes | Disclosing party / receiving party / mutual |
| Type of disclosure | Recommended | Business discussion, M&A diligence, vendor evaluation, technology partnership |
| Sensitivity of information to be shared | Recommended | Low (general business info) / Medium (financials, IP) / High (trade secrets, regulatory data) |
| Counterparty profile | Optional | Public company, PE-backed, government entity, individual |
| Prior NDA with same party | Optional | Supersession clause may be relevant |

## Triage Checklist

The triage runs through 12 checkpoints. Each checkpoint produces a GREEN / YELLOW / RED flag. The overall rating is determined by the worst individual flag.

### Checkpoint 1 — Mutual vs. unilateral

| Status | When |
|---|---|
| GREEN | NDA is mutual; both parties have equivalent obligations |
| YELLOW | NDA is unilateral but client is the receiving party; can sign with note |
| RED | NDA is unilateral and client is the disclosing party only; counterparty has no obligations |

### Checkpoint 2 — Definition of Confidential Information

| Status | When |
|---|---|
| GREEN | Standard definition — all non-public information disclosed; with standard exclusions (public domain, independently developed, received from third party) |
| YELLOW | Definition is overly broad but can be narrowed with a one-line clarification |
| RED | Definition has no exclusions; everything disclosed becomes permanently confidential |

### Checkpoint 3 — Permitted disclosure carve-outs

| Status | When |
|---|---|
| GREEN | Standard carve-outs: legal requirement, court order (with notice to disclosing party where possible) |
| YELLOW | Missing notice requirement for compelled disclosure — add with one-line amendment |
| RED | No permitted disclosures at all, including legal or regulatory requirements |

### Checkpoint 4 — Term and termination

| Status | When |
|---|---|
| GREEN | Fixed term (1–3 years) with survival of obligations for 2–5 years post-termination |
| YELLOW | Very long term (5+ years active obligations) — flag but acceptable for trade-secret-level disclosures |
| RED | Perpetual obligations with no end date (creates indefinite liability) OR no survival after termination |

### Checkpoint 5 — Standard of care for confidentiality

| Status | When |
|---|---|
| GREEN | Same care as own confidential information, but no less than reasonable care |
| YELLOW | "Best efforts" standard (too high; should be "reasonable efforts") — redline |
| RED | No standard stated; or "absolute" standard |

### Checkpoint 6 — No reverse-engineering / no-use restriction

| Status | When |
|---|---|
| GREEN | Use restricted to evaluation purpose; no reverse-engineering |
| YELLOW | Missing explicit no-reverse-engineering clause for technical disclosures |
| RED | No use restriction at all; information can be used for any purpose |

### Checkpoint 7 — Return or destruction on termination

| Status | When |
|---|---|
| GREEN | Return or destroy + certify within 30 days of termination / request |
| YELLOW | Return or destroy without certification — add one line |
| RED | No return or destruction obligation |

### Checkpoint 8 — No solicitation / no-hire

| Status | When |
|---|---|
| GREEN | Absent (standard for NDAs; these provisions belong in a separate agreement) OR limited to key personnel with 12-month window |
| YELLOW | Broad no-hire covering all employees for 2+ years |
| RED | Broad non-compete (not just non-solicit) buried in an NDA — NDAs should not contain non-competes |

### Checkpoint 9 — Injunctive relief provision

| Status | When |
|---|---|
| GREEN | Standard acknowledgment that breach may cause irreparable harm and injunctive relief is available (does not waive other remedies) |
| YELLOW | Present but overly broad (pre-acknowledges entitlement to injunction without requiring proof of irreparable harm) |
| RED | Waiver of right to challenge any injunction sought — unacceptable |

### Checkpoint 10 — Governing law and dispute resolution

| Status | When |
|---|---|
| GREEN | Clear governing law; sensible forum (matches where parties are located or where disputes are practical to resolve) |
| YELLOW | Missing governing law — add |
| RED | Governing law is the counterparty's home jurisdiction where enforcement would be impractical for client |

### Checkpoint 11 — Assignment and change of control

| Status | When |
|---|---|
| GREEN | No assignment without consent; or assignment allowed only in M&A context with acquirer bound by same obligations |
| YELLOW | Assignment to affiliates without restriction — acceptable if affiliates are clearly defined and bound |
| RED | Unrestricted assignment — allows counterparty to transfer obligations to any third party |

### Checkpoint 12 — Liquidated damages / penalty clause

| Status | When |
|---|---|
| GREEN | Absent (standard) |
| YELLOW | Pre-agreed damages at commercially reasonable level |
| RED | Unlimited or punitive pre-agreed damages; or criminal complaint right for breach (seen in some MENA NDAs) |

MENA note: Some Lebanese and Gulf NDAs include a clause giving the disclosing party the right to file a criminal complaint for breach of confidentiality. This is unusual and potentially problematic — flag as RED. Criminal complaint remedies for commercial disputes are a litigation-tactic risk.

## Output

### Triage Card

```markdown
## NDA Triage — [Counterparty Name] — [Date]

### OVERALL RATING: 🟡 YELLOW — Sign after 3 targeted redlines

| Checkpoint | Status | Issue |
|---|---|---|
| Mutual / unilateral | 🟢 GREEN | Mutual — OK |
| Definition of CI | 🟢 GREEN | Standard with exclusions |
| Permitted disclosure | 🟡 YELLOW | Missing notice for compelled disclosure |
| Term | 🟢 GREEN | 2-year term; 3-year survival |
| Standard of care | 🟡 YELLOW | "Best efforts" — should be "reasonable efforts" |
| No-use restriction | 🟢 GREEN | Purpose-limited |
| Return/destruction | 🟡 YELLOW | Missing certification obligation |
| No-solicit | 🟢 GREEN | Absent |
| Injunctive relief | 🟢 GREEN | Standard acknowledgment |
| Governing law | 🟢 GREEN | DIFC — appropriate |
| Assignment | 🟢 GREEN | Consent required |
| Penalties | 🟢 GREEN | Absent |

### REQUIRED REDLINES (3)

1. **Clause 6(b)** — Compelled disclosure: add "with prompt prior written notice to Disclosing Party where legally permitted"
2. **Clause 3** — Standard of care: replace "best efforts" with "reasonable efforts"
3. **Clause 9** — Return/destruction: add "and certify in writing such destruction within 10 business days"

### Recommendation
Sign with above 3 redlines. No escalation needed.
```

## MENA-Specific Notes

- **Arabic NDA requirement (UAE/KSA onshore)**: For agreements involving UAE mainland or KSA parties where disputes may be brought in local courts, the Arabic version controls in court proceedings. If the NDA is in English only, the party relying on it in a UAE or KSA court must obtain a certified Arabic translation. For high-sensitivity disclosures, consider drafting bilingually.
- **Notarization**: Standard NDAs do not require notarization in UAE or KSA. However, if the NDA forms part of a larger transaction that requires notarized documents, check whether the NDA needs to be part of that package.
- **Public-sector counterparties**: NDAs with UAE or KSA government entities require careful review — government-entity NDAs often exclude or limit obligations on the government side. Flag for senior review.

## Related Skills

- [[pa-workflow-transactional-contract-redline-20min]]
- [[pa-workflow-transactional-clause-library-check]]
- [[pa-workflow-transactional-msa-against-firm-playbook]]
- [[draft-nda-mutual]]
- [[router-legal-flows]]
