---
name: draft-contract-skeleton-builder-sboghossian
title: Contract Skeleton Builder
description: Use as the master structural template for drafting any commercial contract. All document-type draft skills inherit this skeleton. Defines the standard 13-part structure — title, parties, recitals, definitions, operative provisions, reps and warranties, covenants, conditions, term and termination, confidentiality, boilerplate, signature block, and schedules — with jurisdiction-specific guidance on which parts civil-law and common-law systems handle differently. The first skill to invoke when building any contract from scratch.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-contract-skeleton-builder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract Skeleton Builder

## When to use this

Use this skill as the **master structural template** whenever you need to draft a commercial contract from scratch. It defines the complete, ordered structure that all other `draft.*` skills inherit and adapt. The skeleton is jurisdiction-aware — some parts are standard across all systems; others require deliberate choices based on whether the contract will be governed by civil law (Lebanon, KSA, UAE onshore, France, Egypt) or common law (DIFC, ADGM, UK, US).

## The standard skeleton

### Part 1 — Title
```
[AGREEMENT / CONTRACT NAME]
e.g., SERVICE AGREEMENT
     SHARE PURCHASE AGREEMENT
     NON-DISCLOSURE AGREEMENT
```
State the agreement type. In common-law drafting, "agreement" is standard; "contract" is also acceptable. In Arabic / civil-law drafting, "عقد" (contract) or "اتفاقية" (agreement) — use consistently.

### Part 2 — Date and parties block
```
This [Agreement] is entered into as of [DATE] (the "Effective Date")

BETWEEN:

[Party 1 full legal name], a [company type] incorporated in [jurisdiction] 
with registration number [XX] and having its registered office at [address]
("Company" / "Buyer" / [short-form name])

AND

[Party 2 full legal name], a [company type] incorporated in [jurisdiction]
with registration number [XX] and having its registered office at [address]
("Counterparty" / "Seller" / [short-form name]).
```

**Drafting notes**:
- Full legal name must match the commercial registration exactly.
- For civil-law MENA: state the name in Arabic and (transliteration / English form if different).
- For individuals: name, nationality, passport/ID number, address.
- "Duly represented by [Name], [Title]" — include where signing authority needs to be established on the face of the document (common in civil-law jurisdictions).
- Date: use "as of" or "dated" — do not leave it blank to be filled in later (creates execution date ambiguity).

### Part 3 — Recitals (WHEREAS clauses)
```
RECITALS / BACKGROUND

WHEREAS, [Party 1] is engaged in [business description];
WHEREAS, [Party 2] is engaged in [business description];
WHEREAS, the parties wish to [summary of the commercial relationship];
NOW, THEREFORE, in consideration of the mutual promises and covenants 
contained herein, and for other good and valuable consideration, the 
receipt and sufficiency of which are hereby acknowledged, the parties 
agree as follows:
```

**When to use recitals**:
- Common-law (UK, US, DIFC, ADGM): standard; provides commercial context and aids interpretation.
- Civil-law (LB, KSA, UAE onshore, FR): recitals are less common and shorter; courts rely on the operative text; long US-style WHEREAS recitals look unusual. A short background paragraph is acceptable.
- Recitals are not operative; do not put binding obligations in the recitals.

**See also**: [[draft-recitals-builder]] for detailed recitals construction.

### Part 4 — Definitions
```
1. DEFINITIONS

In this Agreement, the following terms shall have the meanings set out below:

"Affiliate" means, with respect to a Party, any entity that directly or 
indirectly controls, is controlled by, or is under common control with 
that Party.

"Business Day" means a day (other than a Friday, Saturday, or public 
holiday) on which banks are open for business in [jurisdiction].

"Confidential Information" means [...].

[Continue for each defined term, alphabetically]
```

**When to use a Definitions section**:
- Common-law contracts: always; a separate definitions section with all defined terms in alphabetical order.
- Civil-law contracts: optional; French/Lebanese practice often defines terms in-line on first use; KSA practice is evolving toward common-law style for international contracts.
- Do not define terms that are not used more than once; do not use definitions to insert substantive obligations.

**See also**: [[draft-definitions-builder]].

### Part 5 — Operative provisions
The deal itself. Structure:
```
2. [MAIN OBLIGATION — e.g., SALE AND PURCHASE / SERVICES / LICENSE]
   2.1 [Core obligation of Party 1]
   2.2 [Core obligation of Party 2]
   2.3 [Conditions on the obligation]
```
Use hierarchical numbering:
- Articles (1, 2, 3) → Sections (1.1, 1.2) → Sub-sections (1.1.1, 1.1.2)
- Avoid going deeper than three levels; reorganize rather than subdividing further.

Number every operative clause. Never use unnumbered paragraphs in operative text.

### Part 6 — Representations and warranties
```
[PARTY] REPRESENTATIONS AND WARRANTIES
[Party] represents and warrants to [other Party] that, as of the 
Effective Date [and as of the Closing Date]:

(a) Organization and authority: [Party] is duly organized and 
    validly existing under the laws of [jurisdiction]; has full 
    power and authority to enter into this Agreement; this Agreement 
    has been duly authorized, executed, and delivered;

(b) No conflicts: execution and performance of this Agreement does 
    not violate [Party's] constitutional documents, any applicable 
    law, or any material agreement;

(c) [Transaction-specific reps: financial statements, title, IP, 
    employees, litigation, etc.]
```

**Civil-law note**: reps and warranties are a common-law concept. Civil-law systems achieve similar results through implied statutory warranties, good faith obligations, and civil liability for misrepresentation (vice caché, dol). Long reps and warranties sections can be included in civil-law contracts but should be styled as factual declarations rather than warranty-style representations, to align with the civil-law framework.

### Part 7 — Covenants
Ongoing obligations of the parties after execution:
```
COVENANTS

[Party] covenants that, during [the Term / the period from 
Signing to Closing / [specified period]]:

(a) [Affirmative covenant — something Party must do];
(b) [Negative covenant — something Party must not do];
```

Covenants are prospective (what the parties will do after signing). They are distinct from reps (statements of current fact) and conditions (triggers for other obligations).

### Part 8 — Conditions
Conditions precedent (things that must occur before the main obligation is triggered) and conditions subsequent (events that terminate or modify obligations):
```
CONDITIONS PRECEDENT

This Agreement [the Closing / the Service commencement] is conditional upon:
(a) [Condition 1 — e.g., regulatory approval];
(b) [Condition 2 — e.g., board resolution];

If the conditions are not satisfied by [LONGSTOP DATE], either Party 
may terminate this Agreement by written notice.
```

### Part 9 — Term and termination
```
TERM AND TERMINATION

9.1 Term: This Agreement commences on [DATE] and continues until 
    [DATE / until terminated] (the "Term").

9.2 Termination for convenience: Either Party may terminate this 
    Agreement on [30/60/90] days' written notice.

9.3 Termination for cause: Either Party may terminate immediately 
    on written notice if the other Party [materially breaches this 
    Agreement and fails to cure within [14/30] days of notice / 
    becomes insolvent / ceases to carry on business].

9.4 Effect of termination: [Payment of sums accrued; return of 
    materials; survival of obligations].

9.5 Survival: [List provisions that survive termination — 
    confidentiality, IP ownership, indemnification, governing law].
```

### Part 10 — Confidentiality
If a standalone NDA is in place and incorporated by reference, this section can be shortened to a cross-reference. Otherwise:
```
CONFIDENTIALITY

Each Party shall keep confidential all Confidential Information 
received from the other Party and shall not disclose it to any 
third party without the disclosing Party's prior written consent, 
except: (a) to its own officers, employees, advisors who need to 
know; (b) as required by law or regulatory order.

This obligation survives termination of this Agreement for 
[3 years / indefinitely for trade secrets].
```

### Part 11 — Boilerplate / general provisions
See [[draft-boilerplate-clauses]] for the full clause library. Standard minimum:
- Entire Agreement (integration)
- No Waiver
- Severability
- Notices
- **Governing Law** ← always specify
- **Dispute Resolution** ← always specify; arbitration or courts
- Force Majeure
- Counterparts and Electronic Signatures
- Assignment
- Headings and Construction

### Part 12 — Signature block
```
IN WITNESS WHEREOF, the parties have executed this Agreement as of 
the date first written above.

[PARTY 1 NAME]                    [PARTY 2 NAME]

By: ______________________        By: ______________________
Name:                             Name:
Title:                            Title:
Date:                             Date:
```

**Civil-law MENA requirements**:
- **Initials on every page**: required or strongly expected in LB, FR, KSA, UAE onshore to prevent page-substitution fraud; plan for this in multi-page agreements.
- **Corporate seal / stamp**: UAE and KSA companies often affix a company stamp; not legally required but common practice.
- **Witness or notarization**: some contract types require witness signatures or notarization (real estate, powers of attorney, marriage contracts — vary by jurisdiction).
- **Arabic signature block**: where required, include the Arabic equivalent.

### Part 13 — Schedules / annexes
Schedules contain the technical or commercial detail that would clutter the main agreement:
```
SCHEDULE A — [SERVICES DESCRIPTION / SCOPE OF WORKS / SPECIFICATIONS]
SCHEDULE B — [FEES / PAYMENT SCHEDULE / PRICING]
SCHEDULE C — [KEY PERSONNEL / CONTACT LIST]
SCHEDULE D — [FORM OF [NDA / ASSIGNMENT / ORDER FORM]]
```

**Schedules are operative**: they are legally part of the agreement. A provision in a schedule prevails over the same provision in the body text unless the body text expressly states otherwise (or vice versa — define the hierarchy explicitly).

**See also**: [[draft-schedule-annex-builder]].

## Jurisdiction matrix — what to include or omit

| Part | Common-law (DIFC, ADGM, UK, US) | Civil-law (LB, FR, UAE onshore, KSA) |
|---|---|---|
| Recitals | Standard; often detailed | Short or omit for simple contracts |
| Definitions | Always; alphabetical | Optional; in-line definition acceptable |
| Reps and warranties | Standard; detailed | Include as factual declarations; civil-law courts read strictly |
| Conditions precedent | Standard | Standard |
| Boilerplate | Detailed; include all standard clauses | Shorter; civil code supplies many defaults |
| Governing law | Freely chosen; specify explicitly | Often mandatory (lex loci or lex situs) |
| Signature page | Single signature page | Initials on all pages; company stamp |
| Schedules | Standard | Standard |

## Language and bilingual drafting

For MENA contracts requiring Arabic-English: see [[draft-bilingual-ar-en-side-by-side]]. The skeleton above applies to both versions; the Arabic version follows the same part structure.

## Related skills

- [[draft-boilerplate-clauses]]
- [[draft-bilingual-ar-en-side-by-side]]
- [[heuristic-no-us-style-boilerplate-in-civil-law-jx]]
- [[draft-recitals-builder]]
- [[draft-definitions-builder]]
- [[draft-schedule-annex-builder]]
