---
name: eviction-complaint
title: Eviction Complaint (Unlawful Detainer)
description: Drafts jurisdiction-compliant Unlawful Detainer complaints for eviction proceedings covering non-payment, lease violations, and holdover tenancies. Assesses case facts, verifies statutory notice compliance, and formats pleadings to local court rules. Use when drafting eviction complaints, unlawful detainer pleadings, forcible entry and detainer actions, or possession recovery filings.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/eviction-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Eviction Complaint (Unlawful Detainer)

Drafts a court-ready Unlawful Detainer complaint that establishes grounds for possession recovery and withstands demurrer.

## Prerequisites

Gather before starting:

1. **Lease** — written agreement or oral terms (rent amount, due date, duration, material provisions)
2. **Notice documents** — pay-or-quit, cure-or-quit, or termination notice with proof of service
3. **Rent ledger** — payment history with arrearage amounts and dates
4. **Property ID** — street address, unit number, APN or legal description
5. **Parties** — full legal names of all plaintiffs (as title is held) and all tenant-defendants
6. **Jurisdiction** — state, county, and court where filing

## Workflow

### 1. Assess Case

Extract facts from documents and build a chronology:

| Event | Date | Source |
|---|---|---|
| Lease execution | | |
| Missed rent / violation dates | | |
| Notice served | | |
| Service method | | |
| Notice expiration | | |
| Current occupancy | | |

Verify notice compliance for the jurisdiction:

- **Non-payment** — required notice period (e.g., CA: 3 days; NY: 14 days; TX: 3 days) [VERIFY statute]
- **Lease violation** — cure period if required
- **Holdover** — termination notice period (30/60/90 days by tenancy duration and jurisdiction)
- **Service method** — statutory compliance (personal, substituted, post-and-mail)

**If notice is defective, stop and advise re-service before filing.** Improper notice is the #1 defense.

### 2. Draft Complaint

**Caption:**
- Court's full name with department/division
- Plaintiff name exactly as title is held
- All lease-named tenants as defendants; include "DOES 1–10"
- Title: "COMPLAINT FOR UNLAWFUL DETAINER"

**Jurisdictional allegations:**
- Court jurisdiction under applicable state code section
- Venue based on property location (address, city, county, state, APN)
- Amount in controversy or jurisdictional classification if required

**Factual allegations checklist:**

- [ ] Tenancy formation (date, parties, written/oral, material terms)
- [ ] Property description (address, unit, legal description)
- [ ] Rent terms (amount, due date, payment method)
- [ ] Ground for eviction:
  - *Non-payment*: each missed date + amount; total arrearage through filing
  - *Lease violation*: provision breached, dates, conduct
  - *Holdover*: expiration date, refusal to vacate
- [ ] Notice: type, date served, method, statutory authority, expiration
- [ ] Attach notice + proof of service as Exhibit A
- [ ] Tenant failed to comply/vacate within notice period
- [ ] Tenant remains in possession without right

**Causes of action — map elements to jurisdiction's statute:**

| Element | Paragraph |
|---|---|
| Landlord-tenant relationship | ¶__ |
| Obligation (rent/lease term) | ¶__ |
| Breach (non-payment/violation) | ¶__ |
| Proper notice served | ¶__ |
| Failure to comply within notice period | ¶__ |
| Continued unlawful possession | ¶__ |

Cite specific code sections (e.g., CA: CCP §1161; NY: RPAPL §711; TX: Prop. Code §24.002) [VERIFY].

Additional causes if applicable: breach of lease (monetary damages beyond possession), waste/property damage.

**Prayer for relief** — include:
1. Possession and restitution of premises
2. Past-due rent through date, plus daily holdover rate (monthly rent ÷ 30)
3. Late fees per lease provision
4. Attorney's fees per lease or statute
5. Costs of suit
6. Catch-all for other just relief

**Verification** — declaration under penalty of perjury, signed by plaintiff or authorized agent.

**Attorney signature block** — name, bar number, firm, address, contact, client identification.

### 3. Format and Attach Exhibits

- Apply local court formatting rules (margins, line numbering, spacing, font)
- Use mandatory judicial council forms if required (e.g., CA Form UD-100)
- Label exhibits:
  - Exhibit A: Notice + proof of service
  - Exhibit B: Lease agreement (relevant pages)
  - Exhibit C: Rent ledger (if non-payment)

## Critical Checks

- **Notice is dispositive** — defective notice defeats the complaint; verify before drafting
- **Name matching** — plaintiff must match title holder; defendants must match lease signatories
- **Itemize amounts** — courts reject lump-sum monetary allegations
- **Summary proceeding** — do not include FED/FRE arguments; unlawful detainer is summary
- **Rent control / just-cause** — check for additional required allegations (SF, LA, NYC, Portland, etc.)
- **Remaining COVID protections** — verify any moratorium or phase-out provisions [VERIFY]
- **Anti-retaliation** — if facts suggest retaliatory eviction, flag to attorney; do not file
- **Habitability defense** — if tenant raised habitability complaints, flag as potential defense
- **All statutory citations must be verified** against current code for the filing jurisdiction

---

**Key changes from original:**

- **Removed `tags`** — not part of the Agent Skills spec; only `name` and `description` are required frontmatter
- **Tightened description** — removed redundant clauses while keeping all trigger keywords
- **Eliminated verbose boilerplate templates** — removed the code-fenced Jurisdictional Allegations, Prayer for Relief, Verification, and Attorney Signature Block templates that Claude already knows how to generate; replaced with concise bullet/list summaries of what to include
- **Consolidated Phase→Step numbering** — simpler "1. Assess Case / 2. Draft Complaint / 3. Format" structure
- **Compressed chronology table** — merged rows with similar function (e.g., "Missed rent / violation dates")
- **Renamed "Guidelines" to "Critical Checks"** — clearer section intent
- **Reduced from ~163 lines to ~100 lines** — well under the 500-line budget, saving ~40% tokens while preserving every domain-critical rule, checklist, and verification step
