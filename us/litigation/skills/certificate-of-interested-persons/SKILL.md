---
name: certificate-of-interested-persons
title: Certificate of Interested Persons
description: Drafts a FRAP 26.1-compliant Certificate of Interested Persons identifying all parties, entities, and affiliates with financial or legal interests in a federal appeal. Adapts to circuit-specific local rules. Use when filing appeals, corporate disclosure statements, or conflict-of-interest certificates in U.S. Courts of Appeals.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/certificate-of-interested-persons
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
tags: [drafting, pleading]
---

# Certificate of Interested Persons

Discloses all persons and entities with a financial or legal interest in the outcome of a federal appeal per FRAP 26.1 and circuit local rules.

## Prerequisites

1. **Case caption** — appellate case number, full party names as on the notice of appeal
2. **Lower court filings** — complaints, answers, corporate disclosure statements, settlement agreements
3. **Corporate structure** — ownership charts, parent/subsidiary relationships, merger/acquisition records
4. **Representation details** — all law firms and attorneys of record per party
5. **Target circuit** — specific U.S. Court of Appeals (requirements vary)

## Process

### 1. Identify Circuit Requirements

[VERIFY] Research the destination circuit's local rules. Key variations:

| Requirement | Variation |
|---|---|
| Document title | "Certificate of Interested Persons" vs. "Corporate Disclosure Statement" vs. "Disclosure of Corporate Affiliations and Financial Interests" |
| Listing order | Alphabetical vs. categorical by party |
| Amici disclosure | Anticipated amici vs. only filed briefs |
| Negative statements | Some circuits require explicit "none" for empty categories |
| Formatting | Single- vs. double-spaced; page limits |

### 2. Extract Interested Persons

Search all uploaded documents for every disclosable person/entity:

| Category | Disclose |
|---|---|
| **Named parties** | All parties including dismissed/settled; complete legal names |
| **Counsel** | Law firms, office locations, individual attorneys of record |
| **Parent corporations** | Every layer to ultimate parent; note wholly-owned subsidiaries |
| **Subsidiaries** | Those affected by litigation outcome |
| **10%+ stockholders** | Publicly held companies owning ≥10% of a party's stock |
| **Insurers** | Companies covering claims at issue |
| **Litigation funders** | Third-party financiers with recovery interest |
| **Indemnitors/guarantors** | Entities obligated to satisfy judgment |
| **Bankruptcy parties** | Trustee, DIP, creditors' committee if applicable |
| **Amici curiae** | Orgs that have filed or indicated intent to file |

### 3. Draft the Certificate

**Caption:** Full court name, appellate case number, party names exactly as on notice of appeal, document title per local rule.

**Disclosure body:**
- Complete legal name for each person/entity — no abbreviations or trade names
- Relationship descriptor (e.g., "Parent corporation of Defendant XYZ Corp.")
- Full corporate ownership chain for corporate parties

**Certification statement:**
- Reference FRAP 26.1 and applicable local rule by number
- Attest completeness after reasonable inquiry
- Acknowledge continuing duty to supplement
- Include FRAP 32(g) certification

**Signature block:** Attorney name, signature (CM/ECF compliant), bar number, jurisdiction, firm name, address, phone, email, date.

### 4. Quality Checks

- [ ] All names spelled correctly; complete legal names used (no trade names)
- [ ] Every required category addressed, including negative statements where required
- [ ] Corporate ownership chains fully traced
- [ ] Consistent with prior trial-court disclosure statements
- [ ] Changes in corporate structure or representation since trial court flagged
- [ ] Formatting meets circuit specifications (margins, typeface, spacing, page limits)
- [ ] Properly dated and signed

## Guidelines

- **Completeness over brevity** — omitting an interested person risks recusal motions and procedural delays; when in doubt, disclose
- **Verify corporate structures with client** — public filings may be outdated; confirm current ownership before filing
- **Flag changes from trial court** — note any corporate structure or representation changes explicitly
- **Never abbreviate entity names** — courts use these for automated conflict checks
- **Supplement promptly** — file a supplemental certificate immediately upon discovering new interested persons
- **Circuit rules control** — FRAP 26.1 sets the floor, not the ceiling; always check local rules
