---
name: prompt-pack-contract-playbook-sboghossian
title: Contract Playbook
description: Use when a legal ops team or in-house legal department needs to create a contract playbook for a specific agreement type — documenting the company's standard positions, acceptable fallbacks, red lines, approval requirements, and negotiation guidance for key clauses. Enables consistent, faster negotiation and reduces reliance on senior lawyer involvement for routine matters. Applicable across all agreement types and jurisdictions; MENA-aware for UAE, KSA, LB, and GCC enforcement realities.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-contract-playbook
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Playbook

A contract playbook is a standing operating document that codifies the legal team's negotiating positions on a specific agreement type. It is the difference between a consistent, efficient contracting process and one where every NDA or SaaS agreement requires a senior lawyer to reinvent the wheel.

## When to use this

- An in-house legal team negotiates the same agreement type repeatedly (NDAs, MSAs, SaaS terms, employment contracts, distribution agreements) and wants to scale the process.
- A legal operations initiative is underway to reduce average contract cycle time.
- New associates or business users need a reference document to handle routine negotiations without escalating every issue.
- The company has just entered a new jurisdiction and needs to document the local-law adaptations to its standard positions.
- Following a litigation or arbitration that exposed weaknesses in the company's standard contracting practice.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Agreement type | The playbook is specific to one contract type | Ask the user |
| Company name and role in the agreement (buyer / seller / licensor / etc.) | Positions are written from one party's perspective | Ask the user |
| Key clauses to be covered | The playbook should cover 5–12 clauses that recur in negotiation | Ask the user to list 5–7; supplement with standard high-risk clauses |
| Jurisdiction(s) of use | Enforceability of positions varies by jurisdiction | Ask the user |
| Approval authority / escalation levels | Determines what fallbacks require sign-off | Ask the user |

## Optional inputs

- Existing precedent agreement the playbook should be anchored to.
- Business units covered (different BUs may have different risk tolerances).
- Whether the playbook will be made available to non-lawyers (business users) or only to the legal team.
- Language (Arabic version required for MENA onshore use).

## Playbook structure

### Cover page
- Agreement type (e.g., "NDA Playbook — Unilateral (Disclosing Party)").
- Company name and date of last revision.
- Confidentiality level (typically "Internal Use Only").
- Owner (legal team contact) and version number.

### 1. Purpose and scope
- What the playbook covers and what it does not.
- Who may use the playbook (legal team only / business users for pre-approved positions / etc.).
- When to escalate outside the playbook.
- How often the playbook is reviewed (recommended: annually, or after any material judgment or regulatory change).

### 2. Overview of the agreement
Brief explanation of the contract type:
- Its commercial purpose.
- The typical parties and their roles.
- The company's most common position in this agreement (buyer/seller; licensor/licensee; etc.).
- Business context that informs negotiating posture (is this agreement standard-form, one-off negotiation, or high-value bespoke?).

### 3. Key clause guidance — per clause

For each major negotiable clause, use this standard structure:

---

**Clause: [Clause Title] (e.g., "Liability Cap")**

| Element | Content |
|---|---|
| Standard position | The company's preferred position as drafted in its standard form |
| Rationale | Why the company takes this position (business and legal reason) |
| Acceptable fallback 1 | First concession the legal team can make without escalation |
| Acceptable fallback 2 | Second concession; may require business sign-off |
| Red line | The position the company will not go below; triggers escalation |
| Escalation path | Who approves any deviation from the red line |
| Jurisdiction notes | Enforceability differences in UAE / KSA / LB / EG / DIFC that affect the position |
| Common counterparty positions | What the other side typically asks for |
| Response strategy | How to handle the most common counterparty pushbacks |

---

**Clauses to cover in a standard commercial agreement playbook:**

1. **Liability cap** — amount, exclusions (fraud, IP, confidentiality, death/personal injury), consequential loss exclusion.
2. **Indemnification** — scope, mutual vs. one-sided, survival period.
3. **Payment terms** — payment schedule, currency, late payment interest (Sharia consideration for KSA/UAE onshore).
4. **Governing law and dispute resolution** — preferred seat of arbitration (DIAC, ICC, LCIA, ADGM), language of proceedings.
5. **IP ownership and assignment** — ownership of deliverables, background IP, license-back.
6. **Confidentiality** — definition of confidential information, duration, permitted disclosures.
7. **Termination** — for cause, for convenience, notice periods, consequences.
8. **Force majeure** — definition, cure period, termination right.
9. **Assignment and change of control** — consent requirement, deemed assignment on corporate restructuring.
10. **Warranties and representations** — scope, survival period, disclaimer of implied warranties.
11. **Audit rights** — frequency, notice, cost allocation.
12. **Liquidated damages / penalties** — enforceability notes (court reduction risk in civil-law MENA).

### 4. Pre-approved deviations
List any fallback positions that have already been pre-approved at the relevant authority level, so the legal team can accept them without further sign-off. Example: "Liability cap equivalent to 200% of fees paid in prior 12 months — pre-approved (no escalation required)."

### 5. Escalation matrix

| Issue type | Authority required |
|---|---|
| Deviation within fallback 1 or 2 | Senior Associate / Senior Counsel |
| Deviation beyond fallback 2 | General Counsel / Head of Legal |
| Deviation from red line | GC + CFO / CEO depending on contract value |
| New issue not covered by playbook | Refer to legal for ad hoc analysis |

### 6. Jurisdiction-specific annexes
If the company operates in multiple MENA jurisdictions, include a short annex per jurisdiction noting where the standard positions need to be adapted:
- UAE onshore: Arabic language version; liquidated damages are court-reducible; interest provisions require care.
- KSA: governing law clause should be considered carefully; Sharia-compliant interest mechanics if onshore.
- Lebanon: force majeure clauses interpreted liberally by courts since 2019; consider enhanced protections.
- DIFC/ADGM: full freedom of contract; common law interpretation; no Sharia constraint on financial terms.

### 7. Frequently asked questions
A short FAQ covering:
- "The counterparty says their standard form is non-negotiable — what do I do?" (Escalate; flag the red-line issues; log the exception.)
- "The counterparty is using a foreign law NDA — can I just sign it?" (Check governing law and dispute resolution first; escalate if non-MENA law applies to a MENA operation.)
- "The counterparty has crossed out our liability cap entirely — what now?" (Hard stop; escalate to GC.)

### 8. Revision log

| Version | Date | Change summary | Author |
|---|---|---|---|
| 1.0 | [Date] | Initial version | [Author] |

## Quality bar for playbook content

- Every position must have a rationale — without reasoning, the playbook is just a list of demands that business users cannot defend in negotiation.
- Jurisdiction notes must be accurate and specific; do not copy UAE notes into the KSA section without adaptation.
- Escalation paths must be real names or role titles; abstract references to "management" are unworkable.
- The playbook must be reviewed whenever: a court or arbitral tribunal rules on a key clause type; a material regulatory change affects enforceability; a significant negotiation reveals a gap.

## Common mistakes

- A playbook that is so detailed it takes longer to read than to negotiate the contract.
- Standard positions that are pure maximalism — if every position is a red line, the counterparty disregards the playbook.
- No jurisdiction notes — a playbook built for DIFC common-law deals will give wrong guidance for UAE onshore civil-law negotiations.
- No escalation matrix — the playbook becomes a source of internal disputes about who can agree to what.
- The playbook is written once and never updated — outdated guidance is worse than no guidance.

## Related skills

- [[prompt-pack-contract-negotiation-preparation]]
- [[prompt-pack-contract-risk-matrix]]
- [[prompt-pack-client-intake-form]]
- [[prompt-pack-delegation-of-authority-matrix]]
- [[prompt-pack-contract-summary-for-executives]]
