---
name: patent-infringement-complaint
title: Patent Infringement Complaint
description: Drafts a federal patent infringement complaint for U.S. District Court satisfying FRCP Rules 8, 10, 11 and Twombly/Iqbal plausibility. Covers direct (§ 271(a)), induced (§ 271(b)), and contributory (§ 271(c)) infringement with TC Heartland venue analysis and Halo willfulness. Use when initiating patent infringement litigation, drafting an IP complaint, or preparing a pleading to survive a Rule 12(b)(6) motion.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/patent-infringement-complaint
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# Patent Infringement Complaint

Drafts a litigation-ready complaint for patent infringement in U.S. District Court, structured to survive a 12(b)(6) motion and preserve all damages and equitable remedies under 35 U.S.C. §§ 283–285.

## Prerequisites

Gather before drafting:

- **Patent documents** — patent number, issue/filing dates, inventors, asserted claim language, prosecution history, any IPR/PGR/reexam outcomes
- **Accused product evidence** — product names, model numbers, specs, marketing materials, sales/distribution data
- **Ownership chain** — assignment records, USPTO recording confirmation, any licenses affecting standing
- **Venue facts** — defendant's state of incorporation, registered agent, physical facilities in district, in-district sales
- **Pre-suit notice** — C&D letters, licensing negotiations, defendant's citations to plaintiff's patent
- **Party records** — exact legal names, entity types, states of incorporation, principal places of business

## Complaint Structure

### 1. Caption

Court name/division per venue facts, exact party names, civil action number placeholder.

### 2. Jurisdiction and Venue

| Allegation | Basis | Key Facts |
|---|---|---|
| Subject matter | 28 U.S.C. § 1338(a) | Arises under 35 U.S.C. § 1 et seq. |
| Venue — incorporation | § 1400(b); *TC Heartland*, 137 S. Ct. 1514 (2017) | Domestic corp resides only in state of incorporation |
| Venue — place of business | § 1400(b) | Physical address, permanency, infringing acts in district |
| Personal jurisdiction | Forum contacts | Sales, employees, offices, registered agent in district |

**TC Heartland**: For domestic defendants, venue requires (a) state of incorporation, or (b) acts of infringement AND a regular and established place of business in the district. Plead specific physical locations with addresses. Do not rely on general personal jurisdiction for venue.

### 3. Parties

**Plaintiff**: Legal name, incorporation, principal place of business, ownership of patent-in-suit, chain of title if not original assignee.

**Each Defendant**: Legal name, entity type, incorporation, principal place of business, relevant business activities, co-defendant relationships.

### 4. Patent and Factual Background

- Patent-in-suit: title, U.S. Patent No., issue date, application date, priority claims, inventors
- Technical field: problem solved, prior art, nature of advancement (lay-accessible)
- Post-grant proceedings and outcomes
- Plaintiff's commercialization and market activities
- Defendant's accused activities: timeline, scope, revenue, distribution chain

### 5. Infringement Counts

**Count I — Direct Infringement (35 U.S.C. § 271(a))**

For each asserted claim:
- Identify claim number and what it covers
- Map each limitation to accused product/process, citing defendant's own docs
- Allege lack of authorization
- If doctrine of equivalents: plead function-way-result or insubstantial differences with factual support

**Count II — Induced Infringement (§ 271(b))** *(if facts support)*

- [ ] Third-party direct infringement (customers, end users)
- [ ] Defendant's actual knowledge of the patent
- [ ] Specific intent to cause infringement
- [ ] Affirmative acts: instructions, manuals, marketing encouraging infringing use

**Count III — Contributory Infringement (§ 271(c))** *(if facts support)*

- [ ] Sale/offer of component that is a material part of the invention
- [ ] Component especially made/adapted for infringing use
- [ ] No substantial noninfringing use
- [ ] Defendant's knowledge component was designed for infringement

### 6. Willfulness *(if facts support)*

Under *Halo Electronics v. Pulse Electronics*, 136 S. Ct. 1923 (2016):

- [ ] Actual pre-suit knowledge (notice letter, licensing talks, defendant's own citations)
- [ ] Deliberate decision to infringe without license, counsel opinion, or design-around
- [ ] No colorable good-faith basis for non-infringement or invalidity
- [ ] Characterize as willful, deliberate, wanton, reckless disregard

Pray for treble damages (§ 284) and attorney fees (§ 285, exceptional case).

### 7. Prayer for Relief

- [ ] Judgment of infringement (literal and/or DOE)
- [ ] Permanent injunction (§ 283) — plead four-factor *eBay* test
- [ ] Compensatory damages (§ 284) — reasonable royalty floor; lost profits, price erosion
- [ ] Treble damages (§ 284) for willfulness
- [ ] Prejudgment and post-judgment interest
- [ ] Costs and attorney fees (§ 285)
- [ ] Further relief as court deems proper

### 8. Jury Demand

Separate section invoking FRCP 38(b). Must appear in complaint or within 14 days of last directed pleading.

### 9. Signature Block

FRCP 11 signature: attorney name, bar number, firm, address, phone, email, party represented, date.

## Pitfalls

- **Twombly/Iqbal**: No bare recitals. Each theory needs specific factual allegations tying claim limitations to identified accused products. Per-limitation allegations required for plausibility.
- **Venue**: Post-*TC Heartland*, plead § 1400(b) facts with specificity. Do not rely on general personal jurisdiction.
- **Willfulness**: Do not plead absent pre-suit knowledge facts. Conclusory willfulness allegations are routinely struck.
- **Standing**: If plaintiff is exclusive licensee, evaluate all-substantial-rights test. Patent owner may need joinder.
- **Local rules**: Caption formatting, spacing, fonts, page limits vary by district. Confirm before filing.
- **Citation format**: Bluebook — case names italicized, statutory citations as `35 U.S.C. § 271`, patents as `U.S. Patent No. X,XXX,XXX`.

---

Key changes from the original:

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` in frontmatter)
- **Trimmed description** — kept all statutory/case law references but removed redundant phrasing (down from ~530 to ~370 chars)
- **Condensed Parties section** — collapsed verbose bullet lists into single-line summaries (Claude knows party pleading conventions)
- **Removed signature block template** — replaced with one-line summary of required elements (Claude knows FRCP 11 format)
- **Removed jury demand boilerplate quote** — distilled to the two actionable rules (separate section, timing deadline)
- **Removed verbose TC Heartland callout box** — merged into a tighter paragraph after the table
- **Renamed "Guidelines" to "Pitfalls"** — matches best-practice structure and signals these are guardrails, not general advice
- **Removed "claim charts not required" guideline** — already covered by per-limitation language in Count I
- **Removed certificate of service bullet** — too granular; subsumed by "Local rules" pitfall
- **Cut ~40 lines** (141 → ~100) while preserving every statutory reference, case cite, and structural requirement
