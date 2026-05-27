---
name: settlement-license-agreement
title: Settlement and License Agreement
description: Drafts a dual-purpose Settlement and License Agreement resolving IP litigation while establishing an ongoing licensing framework. Covers mutual releases, covenants not to sue, IP license grants, royalty structures, confidentiality, indemnification, and post-termination rights. Use when drafting IP settlement agreements, litigation resolution with license-back provisions, or combined release-and-license instruments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/settlement-license-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
tags: [litigation, transactional, agreement, drafting]
---

# Settlement and License Agreement

Drafts an agreement that simultaneously resolves IP litigation and establishes a licensing framework between the parties.

## Prerequisites

1. **Case documents** — pleadings, complaints, counterclaims, case numbers, court identifications
2. **IP portfolio** — patent numbers, trademark registrations, copyright registrations, trade secret descriptions
3. **Prior negotiations** — term sheets, settlement correspondence, mediation briefs
4. **Financial terms** — agreed settlement amounts, proposed royalty structures, payment schedules
5. **Party details** — full legal names, entity types, jurisdictions of organization, principal places of business

## Output Structure

### 1. Preamble and Recitals

| Element | Content |
|---|---|
| Parties | Full legal names, entity types, organization jurisdictions, addresses, signing capacity |
| Dispute history | Case numbers, courts, claims asserted, IP at issue |
| Recital narrative | Context sufficient for a third party to understand what was settled and why |
| Mutual intent | Desire to resolve disputes and establish licensing relationship |

### 2. Definitions

Define all key terms on first use. At minimum:
- Licensed IP (enumerate by registration/patent number)
- Licensed Field of Use
- Licensed Territory
- Net Sales / Royalty Base
- Confidential Information
- Affiliate / Related Party

### 3. Settlement and Release

| Component | Requirements |
|---|---|
| Mutual general release | Scope: all claims asserted or assertable; extend to affiliates, successors, assigns; carve out obligations under this agreement |
| Covenant not to sue | Additional layer beyond the release |
| Litigation dismissal | Stipulated dismissal with prejudice; specify timeline and filing responsibility |
| Survival | Release must survive license termination — draft explicit language |

- Balance breadth (finality) against specificity (enforceability)
- Include Cal. Civ. Code § 1542 waiver or equivalent if California law applies [VERIFY]

### 4. License Grant

| Parameter | Address |
|---|---|
| IP type | Patents (by number), trademarks (by reg. no. + common law), copyrights, trade secrets, know-how |
| Exclusivity | Exclusive, non-exclusive, or sole |
| Field of use | Product categories, industries, applications |
| Territory | Geographic scope |
| Duration | Term of years, perpetual, or patent life |
| Sublicensing | Permitted? Sublicense survival on termination? |
| Improvements | Included? Derivative ownership? Grant-back provisions? |

### 5. Financial Terms

Distinguish settlement consideration from license royalties — different tax treatment.

**Settlement payments:**
- Lump sum amount and payment schedule
- Characterization (damages vs. license consideration vs. both)
- Tax treatment allocation

**Ongoing royalties:**
- [ ] Royalty base (net sales, gross revenue, units)
- [ ] Rate (flat, tiered, per-product)
- [ ] Payment frequency (quarterly/annually)
- [ ] Accounting and reporting obligations with deadlines
- [ ] Audit rights (frequency, scope, cost allocation, underpayment penalty threshold)
- [ ] Late payment interest rate
- [ ] Minimum royalty provisions if applicable

### 6. Confidentiality

- [ ] Define Confidential Information (include agreement terms if required)
- [ ] Permitted disclosures: attorneys, accountants, court order, regulatory
- [ ] Compelled disclosure: prompt notice + cooperation on protective order
- [ ] Public announcement: mutual approval of press language
- [ ] Survival post-termination (typically 3–5 years; trade secrets indefinite)

### 7. Representations, Warranties, and Indemnification

| Party | Representations |
|---|---|
| Mutual | Authority to enter agreement; no conflict with existing obligations |
| Licensor | Ownership of licensed IP; right to grant license; no known third-party infringement (knowledge qualifier) |
| Licensee | Ability to perform obligations; compliance with applicable laws |

**Indemnification:** scope of covered claims, notice requirements, control of defense, liability caps, consequential damages exclusion, "as-is" disclaimer where appropriate.

### 8. Term, Termination, and Post-Termination

| Provision | Settlement Component | License Component |
|---|---|---|
| Duration | Irrevocable on execution | Defined term or perpetual |
| Termination triggers | N/A | Material breach, non-payment, bankruptcy |
| Cure period | N/A | 30 days written notice (standard) |
| Post-termination | Release survives | Cease use, wind-down period, inventory sell-off |
| Surviving provisions | Release, confidentiality | Audit rights, accrued payments |

**Critical:** License termination must NOT revive settled claims.

### 9. Dispute Resolution

| Step | Timeframe |
|---|---|
| Executive negotiation | 15–30 days |
| Mediation | 30–60 days |
| Binding arbitration or litigation | Per rules selected |

Specify: governing law, venue/arbitration seat, arbitration rules (AAA, JAMS, ICC), prevailing party fee-shifting, jury trial waiver (if litigation path), whether settlement vs. license disputes use different mechanisms.

### 10. General Provisions

- [ ] Entire agreement / integration clause
- [ ] Amendment: written consent required
- [ ] Assignment restrictions (consent required; change-of-control trigger)
- [ ] Severability
- [ ] Waiver (no implied waiver from failure to enforce)
- [ ] Notice provisions with addresses and methods
- [ ] Counterparts and electronic signature authorization
- [ ] Signature blocks with officer name, title, date, authority confirmation
- [ ] Board approval / regulatory filing confirmation if required

## Guidelines

- **Release–license interaction** — Always address whether the release survives license termination. Ambiguity here risks revived claims.
- **Tax characterization** — Settlement payments and royalties differ in tax treatment. Flag for tax counsel.
- **Antitrust risk** — License-back provisions and field-of-use restrictions in settlement context may raise antitrust concerns. Flag if present.
- **Bankruptcy** — IP licenses receive special treatment under 11 U.S.C. § 365(n) [VERIFY]. Include licensee protective language.
- **Recording** — Patent and trademark licenses may require USPTO recording. Include cooperation obligation.
- **Internal consistency** — Cross-check defined terms, section cross-references, and numbering before final output.
- **No legal advice** — Flag all jurisdiction-specific provisions for attorney review. Settlement agreements require human oversight.
