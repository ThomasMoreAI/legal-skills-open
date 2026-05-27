---
name: confidentiality-agreement
title: Confidentiality Agreement (NDA)
description: Drafts corporate NDAs and confidentiality agreements for M&A, due diligence, partnerships, JVs, and licensing negotiations. Handles mutual vs. unilateral structuring, CI definitions and exclusions, compelled-disclosure procedures, standstill and non-solicit provisions, return/destroy obligations, and equitable relief. Use when initiating any pre-deal evaluation or sensitive business discussion requiring enforceable confidentiality protections.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/confidentiality-agreement
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: contracts
language: en
---

# Confidentiality Agreement (NDA)

Drafts enforceable corporate NDAs calibrated for mutual or unilateral disclosure in M&A, partnerships, or due diligence contexts.

## Prerequisites

Gather before drafting:

1. **Parties** — exact legal names, entity types, states of formation, principal addresses
2. **Structure** — mutual (bidirectional) or unilateral (one-way)
3. **Transaction purpose** — asset purchase, stock purchase, merger, JV, licensing, partnership exploration
4. **Parameters** — CI protection period, standstill period, non-solicit period, governing law/venue
5. **Public company flag** — if either party is publicly traded (triggers Reg FD / MNPI considerations)

## Quick Start

1. Identify mutual vs. unilateral structure
2. Draft header with party details and effective date
3. Define CI scope and standard exclusions
4. Set core obligations (use restriction, care standard, non-disclosure)
5. Add protective provisions as needed (standstill, non-solicit)
6. Include term, return/destroy, remedies, and general provisions
7. Validate against the pitfalls checklist below

## Core Drafting Workflow

### 1. Header and Purpose

- Title reflects directionality ("Mutual Confidentiality Agreement" or "Non-Disclosure Agreement")
- Effective date, full party identification (legal name, entity type, formation state, address)
- Purpose statement describing the specific transaction being evaluated
- Include: no obligation to proceed; no binding commitment absent separate definitive agreement

### 2. Confidential Information Definition

**Covered categories:** financial data, strategic plans, technical IP, personnel information, customer/supplier lists, oral disclosures, and the fact/existence of discussions themselves.

**Standard exclusions (with evidence requirements):**

| Exclusion | Evidence |
|---|---|
| Public domain at disclosure | None |
| Becomes public without breach | None |
| Already possessed pre-disclosure | Pre-existing written records |
| Independently developed | Contemporaneous written records |
| Received from unrestricted third party | Written documentation |

### 3. Core Obligations

- **Use restriction** — CI solely for evaluating the stated transaction; no competitive use, product development, or solicitation
- **Care standard** — same degree as receiving party's own CI, no less than reasonable care; specify "highest degree" for highly sensitive categories
- **Non-disclosure** — no third-party disclosure without written consent, except to permitted Representatives

### 4. Permitted Disclosures

Define "Representatives" narrowly: need-to-know employees/officers/directors + transaction-specific external advisors.

Before disclosing to any Representative:
- [ ] Need-to-know confirmed for the specific CI
- [ ] Informed of confidential nature and obligations
- [ ] Bound by equally restrictive confidentiality obligations
- [ ] Receiving party remains liable for Representative breaches

### 5. Compelled Disclosure

1. Prompt written notice before disclosure (nature of requirement, CI at issue, circumstances)
2. Cooperate in seeking protective order or limitation
3. Disclose only the minimum legally required; seek confidential treatment

### 6. Optional Protective Provisions

**Non-solicitation** (when deal involves employee exposure):

| Element | Range |
|---|---|
| Covered employees | Those contacted or identified in CI |
| Duration | 1–3 years |
| Scope | Direct/indirect solicitation + hiring |

**Standstill** (for potential acquisitions, especially public companies):

| Element | Range |
|---|---|
| Duration | 6 months – 2 years |
| Exceptions | Board consent; response to disclosing party solicitation; competing bid |

Prohibited: acquiring securities/assets, proposing combinations, seeking board seats, forming groups, related public announcements.

### 7. Term, Return/Destroy, and Remedies

**Protection periods:**

| Category | Duration |
|---|---|
| General business CI | 2–3 years |
| Trade secrets | Indefinite (until public without breach) |
| Highly sensitive technical | 5 years or indefinite |

**Return/destroy obligation:** on written request or termination — return or destroy all CI materials (originals, copies, derivatives); electronic deletion with reasonable steps; officer-signed certification of compliance.

**Remedies:** equitable relief (injunction without bond or proof of actual damages), actual damages, specific performance, prevailing-party fees if included.

### 8. General Provisions

- [ ] Entire agreement superseding prior discussions
- [ ] Amendments only by signed written instrument
- [ ] No waiver by failure to enforce
- [ ] Severability with reformation
- [ ] No assignment without consent (consider M&A carve-out)
- [ ] Counterparts and electronic signatures
- [ ] IP disclaimer — no license granted; CI remains disclosing party's property
- [ ] Governing law, exclusive jurisdiction, jury trial waiver
- [ ] Signature blocks with authority confirmation

## Pitfalls

- **Mutual symmetry** — if mutual, all obligations must run bidirectionally; do not patch with one-sided carve-outs
- **Trade secret vs. general CI** — fixed-term protection may limit trade secret rights under state UTSA; distinguish and protect trade secrets indefinitely [VERIFY by jurisdiction]
- **Public companies** — add Reg FD compliance and MNPI trading restriction language
- **Standstill scope** — narrower is more defensible; tailor to deal context and bargaining position
- **No-obligation language** — make conspicuous; absence invites implied good-faith-to-negotiate claims
- **Cross-border** — this template is US-baseline; address GDPR, export controls, and foreign judgment enforcement separately
- **Electronic execution** — confirm E-SIGN Act and state UETA compliance [VERIFY]
- **Signatory authority** — verify actual (not apparent) authority; request board resolutions for significant transactions

---

**Key changes from the original:**

- **Frontmatter**: removed `tags` (not in spec), tightened `description` while keeping trigger guidance
- **Reduced from 175 to ~115 lines** by consolidating sections — merged IP disclaimer and governing law into the General Provisions checklist, combined Term/Return/Remedies into one section
- **Added Quick Start** section for at-a-glance workflow
- **Renamed "Guidelines" to "Pitfalls"** to match the best-practices pattern
- **Eliminated redundancy**: removed the standalone signature block section (folded into General Provisions), collapsed verbose obligation formatting into bullet lists, stripped repeated explanatory prose
- **Preserved all legal substance**: CI categories, exclusion table with evidence requirements, compelled disclosure procedure, standstill/non-solicit parameters, protection period tiers, equitable relief language, and all [VERIFY] flags
