---
name: prompt-pack-contract-summary-for-executives-sboghossian
title: Contract Summary for Executives
description: Use when a lawyer needs to summarise a contract for a non-lawyer executive in a one-page briefing covering the agreement's purpose, each party's key obligations, financial commitments, legal risks, and termination conditions — written so a busy executive can understand the agreement in under three minutes. Applicable to all contract types and jurisdictions; MENA-aware for UAE, KSA, LB, EG, and DIFC/ADGM commercial contexts.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-contract-summary-for-executives
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Summary for Executives

An executive contract summary is not a legal analysis — it is a communication tool. Its single purpose is to enable a decision-maker who has not read the contract to understand what they are committing to and what the top risks are, in the time it takes to read a briefing note.

## When to use this

- A CEO, CFO, or other C-suite executive needs to approve a contract but cannot read the full document before a board meeting or signing ceremony.
- A business development team needs to share a summary of a proposed agreement with stakeholders who are not lawyers.
- An in-house lawyer needs to accompany a contract approval request with a one-page cover note.
- A company is entering a new market in MENA and the local team needs an English-language summary of an Arabic-language contract.
- Post-signing, to onboard the operational team responsible for implementing the contract.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Contract text | The document to be summarised | User pastes or attaches the contract |
| Reviewing party name | The summary is written from one party's perspective | Ask the user |
| Target audience | Determines the technical depth and vocabulary | Default to "non-lawyer executive" unless stated otherwise |
| Any specific concerns the executive has flagged | Allows the summary to address the points most relevant to the decision | Ask the user |

## Optional inputs

- Maximum page length (default: one page or approximately 500 words of body text).
- Whether financial numbers should be prominently boxed or highlighted.
- Whether the summary will be translated into Arabic for use in a MENA jurisdiction.
- Whether a recommendation (sign / negotiate / do not sign) should be included.

## Document structure

The summary follows a strict five-section format matching the source skill's specification:

---

**[Document heading]**
CONTRACT BRIEFING NOTE — CONFIDENTIAL
Matter: [Description]
Parties: [Party A] and [Party B]
Date of agreement: [Date]
Prepared by: [Author]
Date prepared: [Date]

---

### 1. Purpose of the agreement
One to two sentences. Answer: what is this contract for, and why are we entering into it?

Example: "This is a three-year Master Services Agreement under which [Vendor] will provide IT infrastructure management services to [Company] across its UAE and KSA operations."

### 2. Key obligations — for each party
Use a two-column format:

| Our obligations (what we must do) | Their obligations (what they must do) |
|---|---|
| Pay monthly service fee of [amount] by the 15th of each month | Maintain system uptime of 99.5% measured monthly |
| Provide access to our premises and systems within [X] hours of request | Provide dedicated account manager and support team |
| Give [30]-day notice of any change in our requirements | Resolve critical incidents within [4] hours |

Keep to 4–6 bullet points per column. Omit minor or housekeeping obligations.

### 3. Financial commitments
State all monetary commitments clearly:
- **Annual value:** [Amount] (or total contract value over [X] years: [Amount]).
- **Payment schedule:** [Monthly / quarterly / milestone-based].
- **Currency:** [AED / USD / SAR / etc.].
- **Price escalation:** [State if there is an annual price increase mechanism — e.g., CPI-linked or fixed %].
- **Financial penalties or liabilities:** If we breach [key obligation], we are liable for penalties of up to [amount] or [formula].
- **Liability cap:** Our maximum total liability is capped at [amount]; theirs is capped at [amount].
- **Note on financial provisions in MENA context:** In UAE and KSA onshore contexts, payments described as "interest" may raise Sharia considerations. If the contract contains such provisions, flag for legal review before the executive signs.

### 4. Legal risks
List the top 3–5 legal risks in plain language, ordered by severity:

**Risk 1 — [Title] [Severity: High/Medium/Low]**
[One sentence explaining the risk in plain terms.]
Action: [What the executive should know or authorize.]

Example:
**Risk 1 — Uncapped liability for data breaches [High]**
If our data systems cause a client data breach, we have no monetary cap on our liability for that specific type of loss. This is unusual; most of our other agreements cap liability at 12 months' fees.
Action: Legal recommends we negotiate a cap before signing.

**Risk 2 — Termination for convenience penalty [Medium]**
If we terminate this agreement before the end of the three-year term, we owe [Vendor] a cancellation fee equal to six months' fees regardless of the reason for termination.
Action: Acceptable if we are confident in the three-year commitment; flag if there is strategic uncertainty.

### 5. Termination conditions
State clearly:
- **Who can terminate and when?** (Both parties / one party only / notice period required.)
- **Termination for cause:** Triggers (material breach, insolvency, regulatory action) and cure period (typically 30 days' written notice to cure).
- **Termination for convenience:** Notice period required; any financial consequence (e.g., cancellation fee, obligation to pay remaining minimum fees).
- **Automatic expiry:** Does the agreement expire automatically or renew automatically?
- **What happens at the end:** Transition assistance obligations; data return/destruction; survival of confidentiality and IP provisions.

---

**Recommendation (optional):**
[Safe to sign / Recommend negotiating [X] before signing / Do not sign until [issue] is resolved.]

---

**Prepared by:** [Author / Legal team]
**Note:** This summary is intended as a briefing for business decision-making only. It is not a substitute for full legal review. Please contact [Legal contact] with any questions.

---

## Drafting standards

- Maximum 500 words of body text (excluding tables and the header).
- No defined terms in parentheses — if a term matters, explain it in plain English.
- Lead with numbers: executives want to know the financial commitment in the first 30 seconds.
- The "Legal risks" section should be honest about severity — do not downplay risks to avoid awkward conversations.
- If the contract is in Arabic and the summary is in English (or vice versa), state this and note that the official version governs.

## What a good executive summary is not

- Not a clause-by-clause legal review — that is a different document.
- Not a redline — if the summary identifies a problem, it points to the risk; the redline is a separate work product.
- Not legal advice to the executive as an individual — it is information to enable a business decision by the company.

## Related skills

- [[prompt-pack-complex-law-simple-summary]]
- [[prompt-pack-convert-complex-document-into-key-points]]
- [[prompt-pack-contract-risk-matrix]]
- [[prompt-pack-contract-negotiation-preparation]]
- [[prompt-pack-client-advisory-note]]
