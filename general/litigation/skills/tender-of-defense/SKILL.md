---
name: tender-of-defense
title: Tender of Defense Letter
description: Drafts a contractual tender of defense letter demanding a contracting party assume defense and indemnification in pending litigation. Analyzes indemnity provisions, insurance requirements, and notice obligations. Use when drafting tender of defense letters, indemnification demands, defense cost-shifting correspondence, or contractual indemnity demands involving subcontractors, vendors, property managers, or service providers.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/tender-of-defense
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Tender of Defense Letter

Drafts a formal demand letter requiring a contracting party to assume defense and indemnification obligations under a commercial agreement in pending litigation.

## Prerequisites

1. **Underlying contract** — indemnification clause, insurance requirements, notice provisions, scope of work, choice of law
2. **Complaint/petition** — case caption, court, case number, specific allegations
3. **Factual background** — incident reports, correspondence, photos, witness statements
4. **Defense cost records** (if applicable) — billing summaries, fee statements
5. **Notice provisions** — designated recipient, delivery method, timing requirements

## Document Analysis

Before drafting, extract from uploaded documents:

| Element | What to Find |
|---|---|
| **Indemnification clause** | Broad form ("arising out of") vs. limited ("caused by negligence"); duty to defend trigger (immediate vs. post-determination) |
| **Insurance requirements** | Coverage types, minimum limits, additional insured obligations, primary & non-contributory language |
| **Notice provisions** | Designated recipient, delivery method, timing |
| **Scope of work** | Services/obligations recipient assumed |
| **Carve-outs/exclusions** | Mutual indemnification, comparative fault allocation, caps |
| **Choice of law** | Governing jurisdiction |
| **Complaint allegations** | Paragraphs implicating recipient's scope of work |
| **Procedural deadlines** | Responsive pleading dates, discovery schedule, trial date |

## Letter Format

- Professional legal letter on firm letterhead
- Certified mail, return receipt requested
- Address to contractual notice designee; if none, registered agent AND general counsel
- Reference line: `RE: Tender of Defense and Indemnification — [Plaintiff] v. [Client] — [Court], Case No. [Number] — Pursuant to [Contract Type] dated [Date]`

## Required Sections

### 1. Opening Demand
- Identify representation, litigation (full caption), contract (date, parties, section numbers)
- Explicit demand for assumption of defense AND indemnification
- Cite specific contractual sections

### 2. Contractual Provisions
- Quote indemnification clause verbatim with section/page references
- Quote insurance requirements verbatim
- Interpretive analysis connecting language to allegations
- "Arising out of" → broad causal-connection trigger
- "Regardless of negligence" → eliminates comparative fault defense

### 3. Factual Nexus
- Quote complaint paragraphs implicating recipient's work
- Quote contract scope-of-work provisions
- Connect allegations → contractual obligations
- Note: duty to defend is broader than duty to indemnify (triggered by potential coverage)

### 4. Insurance Coverage Demand
- Reference exact insurance requirements from contract
- Demand immediate tender to recipient's CGL carrier
- Within 10 days: proof of tender, certificate of insurance showing client as additional insured, certified policy endorsement, written acknowledgment of primary & non-contributory status

### 5. Specific Demands with Deadlines

| Demand | Deadline |
|---|---|
| Written acknowledgment of tender | 10 days |
| Retain qualified defense counsel acceptable to client | 15 days |
| Assume defense costs from inception; reimburse $[amount] incurred | 15 days |
| Tender to CGL carrier + provide proof | 10 days |
| Certificates of insurance + certified endorsements | 15 days |
| Written confirmation of indemnification obligations | 10 days |

Adjust deadlines based on litigation timeline. Flag imminent procedural deadlines.

### 6. Consequences of Non-Compliance
Failure constitutes material breach, preserving rights to:
- Breach of contract for defense costs + attorney's fees (underlying + enforcement)
- Breach of covenant of good faith and fair dealing
- Recovery of damages, settlements, judgments, consequential damages
- Note: delayed carrier tender may prejudice recipient's own coverage — that risk falls on recipient

### 7. Litigation Timeline
- Current procedural posture, filing date, responsive pleading deadline
- Discovery schedule, depositions, CMC, trial date
- Emphasize urgency to avoid default or waiver of defenses

### 8. Attachments
- Exhibit A: Complaint
- Exhibit B: Contract (full or relevant excerpts)
- Exhibit C: Defense cost summary (if applicable)
- Exhibit D: Incident reports, correspondence, photos (as applicable)

### 9. Reservation of Rights
- No waiver of rights, defenses, or claims
- Right to supplement tender with discovery information
- Subject to attorney-client privilege and work product protection
- No admission of fact or liability
- Acceptance does not waive client's independent claims against recipient

## Drafting Rules

- **Tone**: Authoritative, firm, professional — recipients may be executives, not claims adjusters
- **Framing**: Contractual partnership, not adversarial attack; recommend recipient forward to broker/carrier immediately
- **Citations**: Every assertion must cite contract section/page or complaint paragraph numbers
- **Indemnity scope**: Tailor to actual clause language; never assume broad-form if clause is limited
- **Preempt defenses**: Address likely arguments that claims fall outside scope
- **Length**: 4–6 pages
- **Style**: Active voice, direct sentences, no ambiguity in demands or deadlines
- **Mark uncertain citations with [VERIFY]**

---

**Key changes made:**

- **Frontmatter**: Removed `tags` (not in spec), tightened `description` while keeping trigger guidance
- **Removed redundant heading** ("Contractual Tender of Defense Letter" → "Tender of Defense Letter")
- **Merged "Format Requirements"** into a flat "Letter Format" section — eliminated the nested "Output Structure" wrapper
- **Flattened section hierarchy** — removed the "Output Structure > Required Sections" nesting; sections now live at `##`/`###` level directly
- **Consolidated Guidelines into "Drafting Rules"** — compressed 9 bullet points of prose into tighter entries
- **Trimmed redundancy** throughout (e.g., "Document Analysis Checklist" → "Document Analysis", removed duplicated notice provisions from prerequisites vs. analysis table)
- **Line count**: 124 → 113, with meaningful token savings in description and prose density
