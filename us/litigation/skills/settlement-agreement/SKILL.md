---
name: settlement-agreement
title: Settlement Agreement
description: Drafts execution-ready settlement agreements for commercial litigation with mutual releases, payment schedules, confidentiality provisions, and dismissal mechanics. Handles Cal. Civ. Code § 1542 waivers, ADEA-compliant releases, and tax allocation. Use when finalizing settlement terms, drafting mutual releases, or memorializing negotiated resolutions.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/settlement-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Settlement Agreement

Drafts a binding settlement agreement memorializing negotiated terms with enforceability and finality.

## Prerequisites

Gather before drafting:

1. **Parties** — legal names, capacities, addresses, authority to bind
2. **Dispute** — case caption, court, claims, key dates
3. **Terms** — amounts, payment schedule, non-monetary obligations
4. **Confidentiality** — scope, permitted disclosures, remedies
5. **Litigation** — docket number, dismissal preference (with/without prejudice)
6. **Governing contract** — forum-selection, choice-of-law, fee-shifting clauses

## Document Structure

| Section | Key Contents |
|---|---|
| Title & Preamble | "Settlement Agreement and Mutual Release"; party names, defined terms |
| Recitals | Neutral dispute background (no admissions); mutual desire to resolve; consideration acknowledged |
| Definitions | Capitalize consistently; define on first use or in standalone section |
| Payment Terms | Amount, schedule, method, wire instructions, late-payment acceleration |
| Mutual Releases | Scope (known/unknown claims), carve-outs, effective date |
| Confidentiality | Protected info, permitted disclosures (legal/tax/regulatory/subpoena), breach remedies |
| Non-Admission | Settlement ≠ admission of liability |
| Representations & Warranties | Authority, no assignment of claims, accuracy |
| Dismissal Mechanics | Filing party, timeline, prejudice status, cost allocation |
| Tax Provisions | Tax responsibility, 1099 reporting, indemnification |
| General Provisions | Governing law, dispute resolution, severability, integration, counterparts, fees |
| Signature Blocks | Name, title, date, notarization if required |
| Exhibits | Payment schedule, dismissal stipulation, property descriptions |

## Release Drafting Checklist

- [ ] Define released claims specifically (causes of action, time period, subject matter)
- [ ] State whether release covers known and unknown claims
- [ ] If unknown claims included, add Cal. Civ. Code § 1542 waiver (or jurisdiction equivalent):

```
Each Party expressly waives any rights under California Civil Code
§ 1542, which provides: "A general release does not extend to claims
that the creditor or releasing party does not know or suspect to exist
in his or her favor at the time of executing the release and that, if
known by him or her, would have materially affected his or her
settlement with the debtor or released party."
```

- [ ] Identify carve-outs (agreement rights, indemnification, future conduct)
- [ ] Confirm release is mutual unless agreed otherwise

## Payment Terms Pattern

```
(a) [Payor] shall pay [Payee] $[AMOUNT] ("Settlement Amount"):
    (i)  $[AMOUNT] within [X] business days of Effective Date;
    (ii) $[AMOUNT] on or before [DATE]; ...

(b) Payment by [wire transfer/certified check] to: [account/address]

(c) Late payment: entire balance due immediately plus [X]% annual interest.
```

## ADEA Compliance

When releasing age-discrimination claims (29 U.S.C. § 626(f)):

| Requirement | Detail |
|---|---|
| Knowing & voluntary | Plain-language explanation of rights waived |
| Consideration | Must exceed existing entitlements |
| Written advisement | Advise to consult attorney |
| Consideration period | 21 days (individual) / 45 days (group/RIF) |
| Revocation period | 7 days after execution |
| Specific reference | Must reference ADEA claims by name |

## Special Parties

- **Minors / incapacitated** — condition effectiveness on court approval; guardian ad litem or conservator signs
- **Structured settlements** — identify funding mechanism, qualified assignment, IRC § 104(a)(2) considerations

## Critical Checks

- **Neutral recitals** — use "disputed claims," "alleged," "without conceding"; no admissions
- **Release precision** — enumerate claims or use "any and all" with explicit carve-outs; vague releases invite relitigation
- **Dismissal timing** — tie to payment completion, not execution date
- **Confidentiality carve-outs** — always permit legally required disclosures; include subpoena notice-and-object mechanism
- **Integration clause** — "entire agreement… supersedes all prior negotiations, representations, and agreements, whether written or oral"
- **E-signature** — include counterparts clause; confirm E-SIGN Act / UETA validity
- **Jurisdiction rules** — verify enforceability requirements (e.g., Cal. Code Civ. Proc. § 664.6 for stipulated settlements)
- **Tax allocation** — allocate explicitly across claim types (lost wages vs. emotional distress); treatment differs under IRC § 104
