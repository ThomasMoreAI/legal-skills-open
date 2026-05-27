---
name: trademark-clearance
title: Trademark Clearance Search Report
description: Generates a trademark clearance search report evaluating mark availability and registrability across federal (USPTO TESS), state, common law, and international sources. Applies the Lanham Act likelihood-of-confusion multi-factor test. Use when conducting trademark clearance searches, pre-filing availability opinions, or infringement risk assessments.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/trademark-clearance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Trademark Clearance Search Report

Evaluates availability and registrability of a proposed mark across federal, state, common law, and international sources, with conflict analysis and actionable filing recommendations.

## Required Inputs

1. **Proposed mark** — exact mark as used (word, design, or combination)
2. **Goods/services** — description with Nice Classification codes
3. **Geographic scope** — U.S. minimum; add international jurisdictions if foreign expansion planned
4. **Client context** — current markets, expansion plans, channels of trade
5. **Scope limitations** — any industry, geographic, or time constraints

## Quick Start

1. Gather inputs above
2. Search all applicable databases (federal, state, common law, international)
3. Tabulate conflicts ranked by similarity
4. Apply Lanham Act multi-factor test to each significant conflict
5. Rate risk (High / Moderate / Low) and issue recommendation

## Report Workflow

### Step 1: Mark Identification

Tabulate: proposed mark (type: word/design/combo), goods/services with Nice codes, geographic scope, and any search limitations.

### Step 2: Search Sources

| Source | Scope |
|--------|-------|
| **USPTO TESS** | Literal, phonetic, design code, foreign translation, spelling variations |
| **State registries** | Jurisdictions where client operates or plans to operate |
| **Common law** | Search engines, WHOIS, business directories, social media, trade publications |
| **International** | WIPO Global Brand Database, EUIPO eSearch-plus, national offices (if applicable) |

### Step 3: Document Findings

For each potentially conflicting mark, record:

- Reg./Serial No. and status (Registered / Pending / Abandoned / Cancelled)
- Mark description (including design elements), owner, filing/reg. dates
- International class(es) and full goods/services description
- Similarity assessment: visual, phonetic, meaning, commercial impression

Organize by degree of conflict (most similar first). Include abandoned/cancelled marks — common law rights may persist.

**State registrations:** Same fields plus state of registration.

**Common law uses:** Document business name, goods/services, evidence of use (URLs, directories), geographic scope, and duration indicators.

**International:** Flag Madrid Protocol registrations, EU-wide EUIPO marks, and first-to-file jurisdictions requiring early registration.

### Step 4: Conflict Analysis

Apply the **Lanham Act § 43(a) likelihood-of-confusion test** to each significant conflict:

| Factor | Key Considerations |
|--------|--------------------|
| Mark similarity | Appearance, sound, meaning, commercial impression — evaluate in entireties |
| Goods/services relatedness | Same-source expectation, trade channels, purchaser overlap |
| Cited mark strength | Fanciful > Arbitrary > Suggestive > Descriptive (with secondary meaning) > Generic |
| Consumer sophistication | Price point, specialization, purchasing care |
| Actual confusion | Any available evidence |
| Intent | Bad faith indicators |
| Expansion likelihood | Bridge-the-gap analysis |

**Risk ratings:**

- **High** — Likely opposition/infringement action; advise against adoption
- **Moderate** — Conflict exists; mitigation strategies available
- **Low** — Minor concern; proceed with monitoring

### Step 5: Recommendation

Issue one of three outcomes:

**Clear path:** Mark appears available. Recommend filing strategy (ITU vs. use-based), watch service, and consistent use protocols.

**Moderate conflicts:** Narrow goods/services ID, modify mark for distinctiveness, pursue coexistence agreements, or proceed with monitoring.

**Substantial conflicts:** Advise against adoption. Recommend alternative marks, new clearance searches, or acquisition of conflicting rights.

### Step 6: Next Steps Checklist

```
- [ ] File federal application (ITU or use-based)
- [ ] Implement trademark watch service for relevant classes
- [ ] Establish consistent use protocols
- [ ] Consider state registrations in key jurisdictions
- [ ] Note path to incontestability (5 years continuous use post-registration)
```

## Pitfalls and Checks

- Marks need not be identical to create confusion — evaluate overall commercial impression
- Common law rights can block federal registration and create infringement liability even if geographically limited
- Abandoned/cancelled federal registrations may retain common law rights — never ignore them
- First-to-file jurisdictions (most non-U.S.) require different strategy than first-to-use (U.S.)
- Note federal registration advantages: nationwide constructive notice, prima facie validity/ownership, incontestability eligibility
- Mark all uncertain legal citations with `[VERIFY]`
- **Never guarantee absolute clearance** — always caveat that new conflicts may emerge post-search

---

**Key changes made:**

- **Frontmatter:** Removed `tags` (not in spec), tightened `description` to include clear trigger guidance in third person
- **Removed redundant overview** that duplicated the description
- **Renamed "Prerequisites" → "Required Inputs"** and trimmed wording
- **Added Quick Start** section for at-a-glance workflow
- **Collapsed Output Structure into "Report Workflow"** with numbered steps instead of nested subsections — cuts structural overhead while preserving the full process
- **Merged federal/state/common-law/international findings** into a single "Document Findings" step — eliminates repetitive table structures while retaining all required data points
- **Flattened Recommendations** from verbose multi-block format into three concise outcome paragraphs
- **Renamed "Guidelines" → "Pitfalls and Checks"** to match skill conventions
- **Removed FRE 408 prose** (tangential) and consolidated the citation-verification rule into a single bullet
- **Line count reduced from ~140 → ~95**, well under the 500-line limit
