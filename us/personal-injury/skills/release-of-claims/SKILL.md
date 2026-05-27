---
name: release-of-claims
title: Release of All Claims — Personal Injury
description: Drafts enforceable Release of All Claims documents for personal injury settlement resolution. Produces general releases with broad discharge language, unknown-claims waivers (including Cal. Civ. Code § 1542), consideration recitals, protective representations, and execution formalities. Use when drafting settlement releases, general releases, claim waivers, discharge agreements, or mutual release documents in personal injury litigation.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/release-of-claims
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: personal-injury
language: en
tags: [agreement, drafting, litigation]
---

# Release of All Claims — Personal Injury

Drafts an enforceable general release that terminates all claims between parties in exchange for settlement consideration, with maximum-breadth discharge language and jurisdiction-appropriate unknown-claims waivers.

## Prerequisites

1. **Party identification** — full legal names, addresses, corporate designations, representative capacity (executor, trustee, guardian, officer)
2. **Underlying dispute** — incident dates, claim types, case numbers if filed
3. **Settlement terms** — dollar amount, payment schedule, non-monetary components
4. **Governing law / jurisdiction** — state law selection, venue, statutory waiver requirements
5. **Scope decisions** — mutual vs. unilateral release; any carve-outs from released claims
6. **Prior agreements** — settlement agreement, mediation terms, confidentiality provisions to cross-reference

## Output Structure

### 1. Preamble & Parties

| Element | Requirements |
|---|---|
| Releasor | Full legal name, address, capacity; match to underlying litigation captions |
| Releasee | Full legal name + DBAs, former names; state whether extends to affiliates, subsidiaries, officers, directors, employees, agents, insurers, successors, assigns |
| Defined terms | Define "Releasor" and "Releasee" broadly to encompass all intended related parties |

### 2. Recitals

- Reference underlying dispute with specificity to define scope (dates, general nature)
- Frame as mutual desire for finality — **no liability admissions**
- Denial clause: *"Releasee denies all liability but provides consideration to avoid expense and uncertainty of litigation"*
- Acknowledge Releasor's opportunity to investigate facts, review documents, consult counsel
- Cross-reference parent settlement agreement (maintain confidentiality consistency)

### 3. Release Clause

Draft with **maximum breadth** covering all claims, demands, causes of action, suits, debts, obligations, damages, losses, costs, expenses, and attorneys' fees — known or unknown, suspected or unsuspected, matured or unmatured — from the beginning of time through execution.

Legal theory coverage — explicitly enumerate: contract (express/implied), tort (negligence, gross negligence, intentional torts, fraud, misrepresentation), statute, regulation, ordinance, common law, equity.

**Unknown-claims waiver:**

- Acknowledge Releasor may discover new facts; release remains effective regardless
- If California law applies, quote Cal. Civ. Code § 1542 and expressly waive [VERIFY current statutory text]
- For other jurisdictions, include analogous unknown-claims statute if applicable

**Carve-outs** (if any): *"Notwithstanding the foregoing, this Release does not extend to: [specific excluded claims]"*

Common exclusions: breach of settlement agreement itself, surviving indemnification obligations, post-execution claims.

### 4. Consideration

| Element | Detail |
|---|---|
| Monetary | Exact amount in numerals and words, currency, payment method, schedule, delivery instructions |
| Non-monetary | Property return, mutual releases, dismissal with prejudice, forbearance, specific performance |
| Receipt | *"Releasor acknowledges receipt and sufficiency of consideration"* (immediate) or conditions precedent (deferred) |
| Tax | Address characterization, reporting responsibility, withholding as applicable |
| Integration | *"This is the sole consideration; no other promises have been made"* |

### 5. Representations & Warranties

Releasor must represent:

- No prior assignment, transfer, or encumbrance of released claims
- Full right, power, and authority to grant release
- Has read and understands all provisions
- Adequate time to review; opportunity to consult counsel (consulted or voluntarily declined)
- Executes freely and voluntarily — no duress, coercion, or undue influence
- Of legal age, mentally competent, no legal disability
- Understands release is final and irrevocable; giving up substantial rights
- Conducted adequate factual investigation; not relying on external representations
- Understands significance of any statutory waiver provisions

### 6. Governing Law & Dispute Resolution

Include as applicable:

- Governing law clause with state selection, without conflict-of-laws principles
- Exclusive jurisdiction and venue designation
- ADR clause (mediation → arbitration → litigation) with rules, location, cost allocation
- Jury trial waiver — **conspicuous ALL-CAPS format required**
- Severability, integration/merger, modification-requires-writing, and no-waiver clauses
- Prevailing party attorneys' fees (if negotiated)

### 7. Execution Formalities

| Element | When Required |
|---|---|
| Signature blocks | Always — printed name, title if representative capacity, date |
| Notarization | Check jurisdiction; often required/advisable for PI releases |
| Witnesses | Advisable for significant consideration, vulnerable parties, capacity concerns |
| Corporate authority | Entity signatories: *"By: [Name], its [Title]"*; attach resolutions if needed |
| Counterparts | Standard clause permitting separate execution |
| Electronic signatures | Reference E-SIGN Act or UETA compliance if applicable |

## Guidelines

- **Construe against drafter** — courts apply this rule; eliminate all ambiguity in release scope
- **Consideration adequacy** — overly broad release with minimal consideration risks unconscionability challenge
- **Non-waivable rights** — never release: workers' comp (most states), future fraud, certain statutory claims, rights against public policy
- **OWBPA compliance** — if employment claims overlap (age discrimination), 21-day consideration and 7-day revocation periods apply [VERIFY applicability]
- **Cross-document consistency** — consideration, party names, and scope must match parent settlement agreement exactly
- **Confidentiality** — if settlement terms are confidential, ensure recitals do not disclose protected information
- **Tax implications** — characterization of damages (physical injury vs. punitive vs. emotional distress) affects IRC § 104(a)(2) exclusion; flag for counsel review
- **Consistent terminology** — use defined terms throughout; avoid ambiguous pronouns

---

**Changes from original:**

- **Description** trimmed slightly for conciseness while preserving trigger keywords
- **Release Clause (§3)** — removed verbose code-fenced template block; collapsed into inline prose that conveys the same maximum-breadth drafting instruction more token-efficiently
- **Unknown-claims waiver** — removed the full § 1542 quotation (agent should verify and quote at draft time anyway, per `[VERIFY]`); kept the instruction to quote and waive
- **Representations (§5)** — converted from checkbox `- [ ]` format to plain bullets (checkboxes are for interactive use; these are drafting instructions)
- **Governing Law (§6)** — removed code-fenced template; consolidated checkbox items into a concise bullet list, merging boilerplate clauses (severability, integration, modification, no-waiver) into a single line
- **Guidelines** — removed one redundant entry ("Consistent terminology" duplicated cross-document consistency guidance); reordered for logical flow
