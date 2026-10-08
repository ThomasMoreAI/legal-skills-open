---
name: heuristic-no-us-style-boilerplate-in-civil-law-jx-sboghossian
title: No US-Style Boilerplate in Civil-Law Jurisdictions
description: Use when drafting contracts or reviewing documents for civil-law jurisdictions (Lebanon, KSA, UAE onshore, Egypt, France). Prevents the direct transplantation of US or UK common-law boilerplate into civil-law documents without adaptation. Identifies the specific clauses that do not translate (consideration recitals, "time is of the essence", "best efforts", "hold harmless and indemnify") and directs the drafter to civil-law equivalents. Contrasts with DIFC/ADGM, where common-law boilerplate is appropriate.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/heuristic/heuristic-no-us-style-boilerplate-in-civil-law-jx
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# No US-Style Boilerplate in Civil-Law Jurisdictions

## When this applies

This heuristic fires when:
- Drafting a commercial contract for a civil-law jurisdiction: Lebanon, KSA, UAE onshore (federal), Egypt, France, or any other jurisdiction in the French or Egyptian code family.
- Reviewing a contract and finding common-law boilerplate in a civil-law-governed instrument.
- The user asks to "adapt a standard US/UK template" for a MENA jurisdiction.

It does **not** apply to DIFC, ADGM, or other common-law enclaves within the MENA region, where US/UK boilerplate generally fits.

## The core problem

Most template contracts in circulation — especially in corporate, M&A, and finance — originate from US or English law practice. These templates contain structural elements and specific clauses that carry legal meaning in their source system but are meaningless, unenforceable, or actively harmful when transplanted into a civil-law contract.

A document that contains US-style boilerplate under UAE onshore, Lebanese, or KSA governing law is not merely stylistically unusual — it may contain provisions that courts will treat as void, provisions that create unintended obligations, and gaps where civil-law defaults would have provided protection.

## Clauses that do not translate

### "Time is of the essence"

**Common-law meaning**: makes every deadline of the essence, meaning breach of any time-related obligation is a repudiatory breach entitling the innocent party to terminate.

**Civil-law position**: civil-law systems (LB: Code of Obligations and Contracts; UAE: Civil Code) have specific rules about delay, notice requirements before termination, and judicial discretion to grant additional time (*délai de grâce*). "Time is of the essence" language does not override these statutory defaults. The clause is at best redundant; at worst misleading, because a party relying on it may believe they have termination rights they do not have.

**Civil-law equivalent**: draft an express termination-for-cause clause specifying the obligations whose breach permits immediate termination, and the notice period required.

### "Best efforts" vs "Reasonable efforts"

**Common-law meaning**: "best efforts" is generally interpreted as requiring the obligor to do everything in its power, even at significant cost to itself; "reasonable efforts" is a lower standard. The distinction matters in US/UK contract litigation.

**Civil-law position**: civil-law systems use the French-origin concept of *bonne foi* (good faith) and a duty to act with *diligence normale* (normal diligence). The common-law distinction between "best" and "reasonable" efforts does not map onto civil-law obligation theory. Courts may interpret both identically.

**Civil-law equivalent**: specify the obligation substantively — what exactly must be done, to what standard, by what date. If the obligation is a best-endeavors obligation, define the specific steps required.

### "Hold harmless and indemnify"

**Common-law meaning**: "hold harmless" allocates risk so one party is not exposed even if the other's negligence caused the loss; "indemnify" creates a right to be made whole. Together they are a risk-allocation mechanism that works in common-law systems.

**Civil-law position**: civil-law handles this differently. Lebanese, UAE, and Egyptian civil codes have specific rules on *garantie* (warranty), *réparation du dommage* (damage compensation), and limitation/exclusion of liability. A "hold harmless" clause may be interpreted as a liability exclusion and subjected to civil-code restrictions on exclusion clauses. The typical US-style indemnity language does not have a direct civil-law equivalent.

**Civil-law equivalent**: draft an express limitation-of-liability clause referencing the applicable civil code provisions, and a specific indemnity obligation with clearly defined scope, triggering events, and procedure.

### Acknowledgment of receipt of consideration

**Common-law meaning**: "for good and valuable consideration, the receipt and sufficiency of which is hereby acknowledged" — necessary in common-law systems where a contract without consideration is not binding.

**Civil-law position**: civil-law systems do not require consideration. Contracts are binding based on agreement (*consentement*), object (*objet*), and cause (*cause*) — consideration is not a required element. This recital is meaningless in a civil-law contract. It is not harmful, but it signals that the drafter is using a common-law template without adaptation, which undermines confidence.

### "Representations and warranties" distinctions

**Common-law meaning**: "representation" and "warranty" are legally distinct — a false representation gives rise to misrepresentation; a breached warranty gives rise to breach of contract. The combination creates different remedy routes.

**Civil-law position**: civil law uses different concepts — *vices cachés* (hidden defects), *obligation d'information* (disclosure obligation), *garanties* (guarantees). The US "reps and warranties" structure is often grafted wholesale into civil-law contracts but interpreted through a civil-law lens, which can produce unexpected results. Specifically, the detailed "bring-down" rep-and-warranty mechanism in M&A transactions does not have a perfect civil-law equivalent.

**Civil-law approach**: in civil-law M&A drafting, use a combination of: express representations (with appropriate remedies specified), a contractual guarantee regime, and reference to the civil code's sale-of-business provisions where applicable.

## Where common-law boilerplate is appropriate

| Jurisdiction | Legal system | US/UK boilerplate fit |
|---|---|---|
| DIFC | Common law (English) | Clean fit |
| ADGM | Common law (English) | Clean fit |
| Qatar Financial Centre (QFC) | Common law | Mostly clean fit |
| UAE federal / Dubai onshore | Civil law (French-Egyptian family) | Adapt; do not use directly |
| KSA | Civil law + Sharia | Adapt significantly |
| Lebanon | Civil law (French family) | Adapt; do not use directly |
| Egypt | Civil law (Egyptian code) | Adapt |
| France | Civil law | Adapt |

## Hybrid considerations

Some MENA commercial contracts are deliberately structured as "hybrid" instruments — using a civil-law governing law for local courts, but common-law drafting conventions for international parties' comfort. This is a legitimate commercial choice, but:

1. The drafter must know which provisions are legal nullities under the governing law.
2. The parties should be advised that common-law provisions in a civil-law-governed contract will be interpreted through a civil-law lens if disputed in a civil-law forum.
3. If the document is for DIFC arbitration with UAE governing law, the hybrid approach is more defensible than if it is for UAE courts.

For civil-law-adapted boilerplate clauses, see [[draft-boilerplate-clauses]].

## Related skills

- [[heuristic-governing-law-must-match-forum]]
- [[heuristic-always-state-jurisdiction-first]]
- [[draft-boilerplate-clauses]]
- [[review-commercial-contract]]
- [[heuristic-bilingual-ar-en-mirror-clauses]]
