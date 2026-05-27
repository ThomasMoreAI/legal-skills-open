---
name: letter-of-intent
title: Letter of Intent (LOI)
description: Drafts corporate Letters of Intent for M&A and business transactions, structuring binding vs. non-binding provisions, deal terms, exclusivity, and confidentiality. Use when drafting LOIs, preliminary term sheets, deal memoranda, or pre-definitive agreement correspondence.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/letter-of-intent
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
---

# Letter of Intent (LOI)

Formalizes preliminary deal terms between parties contemplating a corporate transaction, balancing binding and non-binding provisions. Targets U.S. transactions — flag cross-border elements for additional counsel review.

## Prerequisites

Gather before drafting. Ask focused questions for any missing items.

1. **Parties** — legal names, entity types, authorized signatories
2. **Transaction type** — acquisition, merger, asset purchase, investment, partnership
3. **Economics** — price/amount, payment structure, timing
4. **Timeline** — due diligence period, target closing, exclusivity duration
5. **Contingencies** — financing, regulatory approvals, third-party consents
6. **Prior documents** — term sheets, correspondence, NDAs (if any)

## Document Sections

| Section | Content |
|---|---|
| Header | Date, recipient, subject: "Letter of Intent – Proposed [Transaction Type]" |
| Opening | Party identification, transaction purpose, deal description |
| Transaction Overview | Assets/equity/units involved, deal structure |
| Principal Terms | See checklist below |
| Binding/Non-Binding Designation | Explicit non-binding statement with binding carve-outs |
| Confidentiality | Standalone provision or NDA cross-reference |
| Exclusivity | No-shop period, scope, duration, breach consequences |
| Governing Provisions | Governing law, good-faith obligation, termination/expiration |
| Signature Blocks | Authorized reps, titles, counterpart/e-signature authorization |

## Principal Terms Checklist

Draft with enough specificity to show serious intent; note definitive agreements will elaborate.

- [ ] Purchase price / investment amount
- [ ] Payment structure and timing (cash, stock, seller note, earnout)
- [ ] Proposed closing date and flexibility conditions
- [ ] Transaction cost allocation
- [ ] Key reps and warranties expected in definitive agreements
- [ ] Material conditions precedent to closing
- [ ] Post-closing obligations (earnouts, non-competes, indemnification)
- [ ] Break-up or termination fees (if any)

## Binding vs. Non-Binding Provisions

| Typically Binding | Typically Non-Binding |
|---|---|
| Confidentiality obligations | Purchase price and payment terms |
| Exclusivity / no-shop | Representations and warranties |
| Cost/expense allocation | Closing conditions |
| Governing law / disputes | Post-closing covenants |
| Non-binding designation clause | Timeline targets |

## Key Provisions

### Confidentiality

If no separate NDA exists, include a binding section covering:
- Scope of confidential information
- Permitted uses (solely evaluating the transaction)
- Permitted disclosures (advisors, lenders — bound by same obligations)
- Duration (typically 18–24 months post-termination)
- Return/destruction of materials if transaction fails

If a separate NDA exists, cross-reference it and confirm it survives the LOI.

### Exclusivity

- **Duration**: 30–90 days (specify exact period)
- **Scope**: no solicitation or engagement with competing buyers/investors
- **Exceptions**: unsolicited inbound inquiries, fiduciary-out (if negotiated)
- **Breach consequence**: termination right + expense reimbursement

## Pitfalls and Checks

- **Label every provision** as binding or non-binding — ambiguity creates unintended obligations
- **Include good-faith covenant** to negotiate definitive agreements with a target date; state failure to reach terms creates no liability beyond breach of binding provisions
- **Confirm governing law** with user — default to target's state of organization or primary transaction jurisdiction
- **Don't over-detail** — avoid full indemnification mechanics or rep schedules that belong in definitive documents; the LOI frames expectations, it doesn't replace the purchase agreement
- **Tone** — professional and direct; accessible to legal and business readers; avoid adversarial framing
- **Include counterpart/e-signature** authorization language

---

**Key changes made:**

- **Description**: Tightened to focus on what it does + clear trigger, removed `tags` (not in the spec's required frontmatter)
- **Removed redundant prose**: Cut the overview paragraph's repetition of the description; collapsed verbose section headers
- **Flattened structure**: Merged the "Confidentiality Provision Template" and "Exclusivity Provision" code blocks into concise bullet lists under a single "Key Provisions" section
- **Consolidated guidelines → "Pitfalls and Checks"**: Matches the recommended skill body pattern; each item is actionable and terse
- **Removed code fences** around list content that didn't need them (confidentiality and exclusivity were wrapped in unnecessary code blocks)
- **Shortened throughout**: ~96 lines down from ~96, but with significantly less visual noise and better signal density per token

Want me to try writing the file again, or would you like to copy this directly?
