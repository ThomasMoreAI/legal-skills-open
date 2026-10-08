---
name: heuristic-governing-law-must-match-forum-sboghossian
title: Governing Law Must Match Forum (or be Explicit)
description: Use when drafting or reviewing governing law and dispute resolution clauses. Enforces the rule that the governing law and the dispute resolution forum must be compatible — or, if intentionally mismatched, that the mismatch is acknowledged and its consequences managed. Mismatched governing law and forum creates enforcement risk, cost, and uncertainty. Applies to all commercial contracts with MENA parties or MENA-seated arbitration. Flags the common anti-patterns including "international law" as governing law and unmatched arbitration/court clauses.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/heuristic/heuristic-governing-law-must-match-forum
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Governing Law Must Match Forum (or be Explicit)

## When this applies

Every commercial contract needs two things in its boilerplate: a governing law clause and a dispute resolution clause. This heuristic fires whenever either or both of those clauses are being drafted or reviewed. The goal is to ensure the two clauses are coherent — or, where they are deliberately mismatched, that the practitioner has consciously accepted the consequence.

## The standard: alignment

The cleanest and most enforceable configuration is where governing law and the forum's lex arbitri (or the forum's procedural law) are the same legal system:

**Examples of clean alignment:**

> *"This Agreement is governed by the laws of England and Wales. Any dispute shall be finally resolved by arbitration under the LCIA Rules, with the seat of arbitration in London."*
>
> The LCIA applies English law as its lex arbitri; governing law is English law. Perfect alignment.

> *"This Agreement is governed by the laws of the DIFC. Disputes shall be resolved by the DIFC Courts."*
>
> DIFC Courts apply DIFC law. Perfect alignment.

> *"This Agreement is governed by UAE federal law. Disputes shall be referred to the Dubai International Arbitration Centre (DIAC), seated in Dubai."*
>
> DIAC seated in Dubai applies UAE arbitration law (Federal Arbitration Law No. 6 of 2018) as lex arbitri; governing law is UAE federal. Compatible.

## Mismatch examples and their consequences

### UAE governing law + New York courts
A New York court must apply UAE federal law as foreign law. This requires:
- Expert testimony on UAE law (expensive, contested).
- Uncertainty about how a US court interprets UAE civil code provisions.
- Potential for the case to turn on procedural issues rather than substantive merits.

Acceptable only where: the transaction is New York-centered, or the lender insists on New York court jurisdiction for enforcement purposes.

### Sharia as governing law + ICC Paris arbitration
An ICC tribunal seated in Paris would need to:
- Determine which version of Sharia applies (Hanafi? Hanbali? AAOIFI standards?).
- Apply French civil procedure as the lex arbitri.
- Potentially face a clash between Sharia and the New York Convention on award enforcement.

This combination appears in some Islamic finance documentation but creates real complexity in enforcement outside the GCC.

### No governing law + arbitration clause
If the governing law is not specified, the tribunal applies conflict-of-laws rules to determine the applicable law. This is uncertain and can result in the tribunal applying a law neither party anticipated.

### Multiple governing-law clauses across documents
When a main contract specifies one governing law and a schedule or side letter specifies a different governing law, the schedule's governing law applies to the schedule's subject matter. This is sometimes intentional (e.g., IP license governed by English law within an agreement otherwise governed by UAE law) but more often is a drafting oversight.

## When mismatch is commercially acceptable

Some mismatches are negotiated and should be explicitly acknowledged:

- **New York governing law + DIFC Courts**: common in international financing transactions where the lender is New York-based but the borrower is in the Gulf. The DIFC Courts are experienced in applying foreign law; the choice reflects a desire for Gulf-region enforcement against assets combined with New York commercial law comfort.
- **English governing law + DIAC arbitration**: English law is well-developed for commercial purposes; DIAC offers a Gulf-region seat preferred for enforcement in the UAE. This is a common and defensible combination.

When drafting an intentional mismatch, add a recital or note explaining the rationale and confirming the parties understand the consequence.

## Anti-patterns to flag

| Anti-pattern | Problem |
|---|---|
| "Governed by international law" | No such body of law; meaningless in practice. A tribunal will reject this or apply its own conflict-of-laws rules |
| "Governed by the laws of the GCC" | GCC is not a single legal system; each member state has its own law |
| "Disputes resolved amicably" (without escalation) | Amicable resolution clauses without a backstop mechanism (arbitration, court) are unenforceable as a dispute-resolution mechanism |
| "Disputes referred to a committee of experts" (without legal process) | Ambiguous; typically non-binding; no enforcement pathway |
| Mixed arbitration and court jurisdiction without a clear hierarchy | Creates parallel proceedings risk and enforcement uncertainty |
| Governing law clause in the recitals | Recitals are typically not operative; the governing law must be in the operative provisions |
| "Subject to applicable law" as governing law | Not a governing law selection; tautological and unenforceable as written |

## Drafting checklist for governing law + forum clauses

1. **Select a governing law**: name a specific national or supra-national legal system (DIFC law, English law, UAE federal law, KSA law, French law). Do not use regional names, vague concepts, or "international law."
2. **Select a forum**: court of competent jurisdiction OR arbitration. Be specific — which court? Which arbitral institution? Which rules?
3. **Check alignment**: is the lex arbitri (or the court's own procedural law) compatible with the governing law? If mismatched, is the mismatch intentional and documented?
4. **Language of proceedings**: specify the language of arbitration or litigation where material. For GCC disputes, bilingual proceedings (Arabic + English) may be available and preferred.
5. **Cross-document consistency**: check all schedules, ancillary agreements, and related documents for conflicting governing law selections.

## MENA-specific traps

- **KSA public policy**: KSA courts apply Sharia as a matter of public policy; foreign governing law does not override Sharia public-policy review on enforcement of Saudi-seated awards or against Saudi assets.
- **UAE mandatory law**: certain UAE federal provisions (employment, real estate, company law) apply regardless of contractual governing law for UAE-nexus matters.
- **Lebanon**: in the post-2019 crisis environment, enforcement of judgments and awards against Lebanese-domiciled parties is particularly complex; consider enforcement options carefully when advising on forum selection.
- **DIFC/ADGM carve-out**: for financial services activities within DIFC or ADGM, the DFSA/FSRA regulatory perimeter imposes mandatory rules that override contractual governing law on regulated matters.

## Related skills

- [[heuristic-always-state-jurisdiction-first]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
- [[draft-dispute-resolution-clause]]
- [[review-commercial-contract]]
- [[heuristic-refuse-if-no-jurisdiction-given]]
