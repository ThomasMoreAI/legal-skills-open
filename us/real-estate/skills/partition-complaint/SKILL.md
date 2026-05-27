---
name: partition-complaint
title: Partition Complaint
description: Drafts a U.S. civil complaint for partition of real property by co-owners, pleading jurisdiction, ownership interests, property description, encumbrances, and grounds for partition in kind or by sale. Trigger when the user needs a partition action, co-owner dispute complaint, tenant-in-common or joint-tenancy division, or court-ordered sale of real property.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/partition-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
tags: [drafting, litigation, pleading]
---

# Partition Complaint

Draft a complaint establishing jurisdiction, ownership, property description, and grounds for partition in kind or by sale.

## Quick Start

Collect before drafting:

| Item | Details |
|---|---|
| Court / county | Venue where property is located |
| Parties | Full legal names, capacity, addresses, entity info |
| Co-ownership basis | Purchase, inheritance, gift, divorce |
| Tenancy type | Tenants in common or joint tenants |
| Property | Street address, APN, county, legal description (metes/bounds or lot/block) |
| Ownership interests | Percentages or fractional shares; acquisition method and dates |
| Encumbrances | Mortgages, liens, easements, amounts |
| Partition type | In kind or by sale with supporting facts |
| Prior efforts | Negotiations, demands, ADR if required |

## Pleading Structure

Number all allegations sequentially.

1. **Caption** — Court, parties, title "Complaint for Partition of Real Property."
2. **Nature of Action** — Identify partition statute; state action type.
3. **Jurisdiction and Venue** — Subject-matter jurisdiction; personal jurisdiction via ownership in forum; venue in property county.
4. **Parties** — Identity and relationship to property. Entities: formation state and principal place. Estates: personal representative or heirs.
5. **Property Description** — Street address, APN, full legal description. Attach as Exhibit A when required.
6. **Ownership Interests** — Tenancy type, specific shares, acquisition method and dates.
7. **Encumbrances and Contributions** — Recorded liens and material encumbrances. Disproportionate payments or improvements if seeking accounting.
8. **Grounds for Partition** — Inability to agree on disposition; necessity of partition.
9. **Partition Type** — Plead in-kind feasibility or sale necessity (see checklist below).
10. **Statutory Compliance** — Cite statute; plead satisfaction of preconditions (notice, ADR).
11. **Prayer for Relief** — See relief menu below.
12. **Verification and Signature** — Verification if required; attorney or pro se signature block.

## Partition-by-Sale Checklist

Allege one or more when seeking sale over in-kind division:

- Physical division impracticable (size, configuration, access, utilities)
- Single structure cannot be divided without destroying value
- Zoning or subdivision rules prevent lawful division
- Division would materially diminish value compared to whole-property sale
- Fractional interests make equitable in-kind division infeasible

## Relief Menu

| Relief | When to include |
|---|---|
| Partition in kind | Physical division feasible and equitable |
| Partition by sale | In kind impracticable or causes material injury |
| Referee / commissioner | Statute or local practice requires appointment |
| Accounting | Dispute over rents, profits, taxes, or improvements |
| Costs and fees | Authorized by statute, contract, or equity |
| Sale procedure | Court-supervised sale and distribution needed |

## Pitfalls

- Join all co-owners and necessary lienholders; identify unknown claimants per local rules.
- Use the deed's legal description verbatim; attach as exhibit when required.
- Plead tenancy type precisely — do not assume joint tenancy without record support.
- Tie partition-by-sale allegations to concrete property facts; avoid conclusory statements.
- Check local rules for verification, special notices, or pre-filing ADR requirements.
- Never include settlement communications or privileged material.
- Plead statutory or contractual basis for any fee or credit requests.

---

**Key changes made:**

- **Description**: Tightened to one sentence of purpose + one sentence of trigger guidance; removed keyword list (tags and description text handle discoverability).
- **Removed template skeleton**: The verbose caption template added tokens without instructional value — the pleading structure already covers ordering.
- **Merged Prerequisites into Quick Start**: Combined the prerequisites list and facts-intake table into a single "Quick Start" table, eliminating redundancy.
- **Renamed sections**: "Output Structure / Process" → "Pleading Structure" (direct); "Guidelines" → "Pitfalls" (standard best-practice heading); "Partition Type Checklist" → "Partition-by-Sale Checklist" (more precise).
- **Compressed pleading steps**: Each step is now a single dash-separated line instead of bold + multi-line prose, cutting ~40% of tokens in that section while preserving all substantive guidance.
- **Removed "Property use" row**: It was not referenced elsewhere in the skill and isn't a required pleading element — improvements are captured under encumbrances/contributions.
