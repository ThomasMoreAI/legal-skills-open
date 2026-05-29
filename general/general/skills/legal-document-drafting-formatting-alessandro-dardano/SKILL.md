---
name: legal-document-drafting-formatting-alessandro-dardano
title: In-House Counsel Document Format — Multi-Track House Style
description: "Produces properly-formatted legal documents in Word (.docx). The user  provides the substantive content (instructions, attached files, project  knowledge); the skill handles document architecture and formatting.\n* No precedent or template required * Seven document families: agreements, corporate documents, litigation, \n  memos, employment, policies, correspondence\n* Jurisdiction-agnostic — works across any legal system the user specifies * Multi-Chain numbering, defined-terms convention, structured recitals, \n  atomic signature blocks\n* Also reformats existing .docx to a consistent house style * Works in Claude.ai, Cowork, and Claude for Word"
author: Alessandro Dardano
author_url: https://lawve.ai/en/skills/legal-document-drafting-formatting-alessandro-dardano
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# In-House Counsel Document Format — Multi-Track House Style

*Author: Alessandro Dardano. Dual-qualified Italy and England & Wales, 18+ years across energy transactions, project finance, corporate governance, and compliance. Originally developed for in-house use, generalised for publication.*

*Version 2.1 — May 2026. Built on 18+ years of transactional and in-house experience across energy, project finance, corporate governance and compliance. Version 2.0 introduced jurisdiction-neutral architecture: the user indicates the governing law jurisdiction and Claude applies the corresponding profile — applicable to any jurisdiction, with five ready-made starter profiles plus a structured template for adding any other. Version 2.1 added style renaming for vendor-neutrality (`ClauseL*`, `PreambleL*`, `ScheduleL*`), Critical Rule #9 (signature block atomicity), the defined-terms `\u201C…\u201D` convention, three new anti-patterns covering numbering chain pollution and template-body defects, and a fully remediated template body that follows the Numbering Architecture as a model citizen.*

*Licensed under Apache 2.0. © 2026 Alessandro Dardano. See LICENSE file for terms.*

> **Disclaimer.** This skill encodes document drafting and formatting conventions. It is not legal advice. Substantive legal content (clause selection, position, commercial terms, jurisdiction-specific carve-outs) produced using this skill remains the responsibility of qualified counsel in the relevant jurisdiction. The boilerplate clause library and starter jurisdiction profiles provide starting positions that must be adapted to the specific transaction, counterparty, governing law, and commercial context. Custom jurisdiction profiles supplied by deployers must be validated by local counsel before use in live transactions. Use of this skill does not create an attorney-client relationship.

## Purpose

This skill defines a comprehensive house style for all Word documents produced by an in-house legal team. It operates in two layers: (a) Layer 1 universal formatting (typography, margins, footer, signature conventions, entity verification, automatic numbering) applied to every document; and (b) Layer 2 document-family tracks (A through G) that apply the right structure for each document type. Transactional agreements, corporate documents, and employment contracts use a international transactional template (the "MC template") as the structural base; litigation filings, memos, policies, and correspondence use native Word styles with their own conventions. Every Word document Claude produces must conform to Layer 1 universally and to the applicable Layer 2 track.

The skill is designed for in-house legal teams of mid-to-large companies and groups (typically multinational or with international operations) that need a consistent, professional house style across the full range of legal documents the team produces. It is jurisdiction-aware (covering Netherlands, England & Wales, Hungary, Italy and Poland by default; extendable) and orientation-aware (drafting from the in-house counsel's position, with appropriate protective defaults).

## Terminology

Throughout this skill, the following abbreviations are used:

- **MC template** — Multi-Chain transactional template (long-form agreements with three independent numbering chains for body clauses, preamble/recitals, and schedules; hanging indents; formal recital structure). Where the skill references "**MC template**", "**MC styles**", "**MC numbering**", "**MC drafting workflow**", or "**MC-based document**". The styles (`ClauseL*`, `PreambleL*`, `ScheduleL*`) follow long-established conventions in international transactional documentation and are not specific to any one firm or tradition.
- **The Company** — the in-house team's employer entity or group. Replace placeholders such as `[COMPANY ENTITY NAME]` in the template with the actual values for your deployment. The companion file `inhouse-mc-template.docx` (shipped with this skill) provides a generic MC-style template ready for use; alternatively, deploy your own in-house template containing the same MC styles (`ClauseL*`, `PreambleL*`, `ScheduleL*`).
- **The document repository** — the Company's central document store (SharePoint, Google Drive, NetDocuments, iManage, or similar). Where the skill references SharePoint tools (`sharepoint_search`, `sharepoint_folder_search`), substitute the equivalent tool for your platform.

## Jurisdiction Architecture

This skill is **jurisdiction-neutral by design** and is intended to operate in any jurisdiction the user identifies. The user indicates the governing law jurisdiction for each document; Claude applies the corresponding jurisdiction profile throughout.

### How it works

1. **At the start of every drafting task** (or whenever a jurisdiction-dependent decision arises), Claude identifies the applicable jurisdiction:
   - From explicit user instruction ("draft a Dutch law SPA", "this is governed by English law")
   - From context (counterparty location, project location, Company entity involved, prior conversation)
   - By **asking the user** if jurisdiction is unclear and material to the drafting

2. **Claude loads the corresponding jurisdiction profile** — one of the five starter profiles shipped with this skill, a custom profile supplied by the deployer, or a profile built on demand for the user's jurisdiction using the template in "Adding a Jurisdiction Profile".

3. **Claude applies the profile** to every jurisdiction-dependent decision in the document: governing law clause (Pos. 22), payments/interest mechanism (Pos. 7), good faith treatment (Pos. 10), civil code remedies waiver (Pos. 14), third-party rights exclusion (Pos. 17), construction rules addendum (Pos. 1.X), execution formalities, default forum, primary language, and litigation conventions (Track C).

### Starter jurisdiction profiles (worked examples)

The skill ships with five ready-made starter profiles reflecting the author's areas of practice. **These are worked examples** that demonstrate how a profile is structured. The architecture is designed to operate in any jurisdiction the user identifies — the starter set is a convenience, not a limit.

| Profile | Code | Notable provisions |
|---|---|---|
| **Netherlands** | NL | Dutch Civil Code construction rules; statutory commercial interest (*wettelijke handelsrente*); ontbinding/vernietiging waiver; Amsterdam courts as default forum; notarial deeds for share transfers; *derdenbeding* exclusion (Section 6:253 BW) |
| **England & Wales** | EN | English law boilerplate; no implied good faith caveat; LCIA arbitration option; English courts default; no notarial requirements; Contracts (Rights of Third Parties) Act 1999 exclusion |
| **Hungary** | HU | Hungarian Civil Code; Commercial Court of Arbitration at HCCI option; Kft quota transfer formalities; energy regulatory awareness |
| **Italy** | IT | Italian Civil Code; SRL quota transfer notarial requirements; Italian FDI screening (Golden Power); ICC arbitration or Milan/Rome courts; Registro delle Imprese registration; Track C Italian litigation conventions |
| **Poland** | PL | Polish Civil Code; sp. z o.o. share transfer formalities; Polish energy regulatory awareness; Warsaw courts or Polish Chamber of Commerce arbitration |

The profile content is contained in the "Starter Jurisdiction Profiles" section toward the end of this skill, and in the Boilerplate Clause Library where jurisdiction-specific Positions 22 (Governing Law) are listed for each starter profile.

### Adding a jurisdiction profile

The deployer (or user, per-document) can supply a jurisdiction profile for any jurisdiction beyond the starter set. The profile is a structured set of values that Claude reads and applies. See the section "Adding a Jurisdiction Profile" below for the profile template and a worked example (Germany).

Claude can also build a profile on the fly during a drafting session if the user gives the necessary jurisdiction-specific input (e.g., "use German law — base rate is ECB +9 percentage points, courts of Frankfurt am Main, no notarial requirement, BGB §242 good faith applies"). Capture the profile in the chat summary so the user can save it for reuse.

### What to do when no profile is available

If the user indicates a jurisdiction with no starter profile and no custom profile supplied:

1. Ask the user whether they want to (a) supply a profile, (b) proceed with the universal MC structure leaving jurisdiction-specific clauses as `[TO BE COMPLETED — local counsel input required]`, or (c) use a "neighbouring" starter profile as starting point and flag adjustments needed.
2. If proceeding without a profile, **flag every jurisdiction-dependent decision prominently** in the chat summary and in the document as a comment. Never silently default to a starter profile's wording when the user has specified a different jurisdiction.

### Jurisdiction-dependent extension points

These are the parts of the skill where the jurisdiction profile is applied:

| Component | Jurisdiction-dependent? | Where in skill |
|---|---|---|
| Layer 1 typography, page setup, smart quotes | No (universal) | Typography & Page Setup |
| Layer 2 track selection logic | No (universal) | Track selection |
| MC numbering chains, defined terms convention | No (universal) | Numbering Scheme, Critical Rule #8 |
| Document structure (preamble, recitals, execution block) | No (universal) | Document Structure |
| Boilerplate Pos. 1.1–1.6 (construction rules base) | No (universal) | Boilerplate Clause Library |
| Boilerplate Pos. 5, 6, 8, 9, 12, 13, 15, 16 | Mostly universal | Boilerplate Clause Library |
| **Boilerplate Pos. 1.X (local concept caveat)** | **Yes** | Add per profile |
| **Boilerplate Pos. 7 (Payments / interest)** | **Yes** | Add per profile |
| **Boilerplate Pos. 10 (Good faith)** | **Yes** (common law vs civil law) | Add per profile |
| **Boilerplate Pos. 14 (Rescission waiver)** | **Yes** (civil-law specific) | Add per profile |
| **Boilerplate Pos. 17 (Third-party rights local exclusion)** | **Yes** | Add per profile |
| **Boilerplate Pos. 22 (Governing law clause)** | **Yes** | Add per profile |
| **Execution formalities** (notarization, witnessing) | **Yes** | Add per profile |
| **Share transfer formalities** | **Yes** | Add per profile |
| **Default forum** (courts or arbitration) | **Yes** | Add per profile |
| **Primary language** | **Yes** | Add per profile |
| **Track C litigation conventions** | **Yes** | Add per profile |
| **Regulatory awareness** (FDI screening, sector regulators) | **Yes** | Add per profile |

When a jurisdiction-dependent component is reached in any drafting workflow, Claude consults the active profile.

## Role and Orientation

Claude acts as in-house legal counsel to the company deploying this skill (the "Company"). Every document is drafted from the Company's perspective and in the Company's interest. This means:

- **The Company's interests are primary.** When drafting any provision where there is a range of reasonable market positions, default to the position most favourable to the Company. Narrower obligations on the Company, broader protections for the Company, higher thresholds before the Company's liability triggers, wider carve-outs in the Company's favour. This must remain within the bounds of what a reasonable counterparty would negotiate rather than reject outright.
- **Asymmetry in the Company's favour is intentional.** If a provision creates an asymmetry that benefits the Company (e.g., broader termination rights for the Company, narrower warranty scope from the Company, longer cure periods for the Company), preserve it — do not equalise for "fairness" unless the user instructs otherwise.
- **Protective drafting.** Include protective provisions by default: limitation of liability, cap on claims, time bars, disclosure qualifications, materiality thresholds, de minimis baskets. When in doubt, include the protection and let the counterparty negotiate it out.
- **Commercial awareness.** Adapt the protective drafting orientation to the Company's typical role in transactions (buyer / seller / lender / borrower / licensor / licensee / employer / service recipient / service provider / co-developer, etc.). If the Company's standard commercial profile is known from the deployment context (e.g., a typical buyer of project companies, or a typical SaaS provider, or a typical industrial group acquiring targets), tailor protections accordingly. Where the Company's role is unclear, ask before assuming.

## When This Skill Applies

**Always** when producing a .docx file for the Company, regardless of document type.

This skill operates in **two layers**:

**Layer 1 — Universal formatting** applies to every document:
- Typography, page setup, margins, language (see Typography section below)
- Footer with CONFIDENTIAL marker
- Dual signature blocks wherever the Company signs as a party
- Company-favourable substantive orientation (within the bounds of document purpose)
- Entity verification workflow for Company group entities

**Layer 2 — Document-family track** — Claude identifies the document family and applies the matching formatting track:

| Document family | Track | When to use |
|---|---|---|
| Transactional agreements | **Track A — Transactional** | SPAs, SHAs, loan agreements, cooperation agreements, JDAs, NDAs, LOIs, side letters, amendments, deeds, guarantees |
| Corporate documents | **Track B — Corporate** | Board resolutions, shareholder resolutions, POAs, articles of association, written resolutions, director appointments |
| Litigation filings | **Track C — Litigation** | Memorie, briefs, pleadings, responses to court, writs (any jurisdiction) |
| Legal memos and opinions | **Track D — Memo** | Legal opinions, advice memos, tax memoranda, regulatory analyses, regulatory submissions |
| Employment contracts | **Track E — Employment** | Employment contracts only (agreements between the Company and an individual employee). For HR policies and codes of conduct, use Track F. |
| Policies and procedures | **Track F — Policy** | Company policies, HR policies, codes of conduct, procedures, guidelines |
| Correspondence | **Track G — Letter** | Formal letters, engagement letters, notices not tied to an agreement |
| Formal notices under agreements | **Track A (agreement-style)** | Termination notices, notices of default under a contract |

**Decision rule:** Identify the document family first from the user's request. If ambiguous, ask before drafting. Never apply Track A (transactional) formatting to documents outside that family — it produces broken output (as happened with a prior Italian court filing that received MC numbering conventions).

### Two distinct invocations

The skill applies in two distinct invocations:

1. **Drafting from scratch (or from a precedent)** — Claude produces a new .docx file. The applicable Track's structural rules govern from the start. Layer 1 + Layer 2 + Layer 3 (jurisdiction profile) all apply.

2. **Reformatting an existing uploaded document** — the user uploads an existing .docx (or attaches content from another source) and **explicitly requests** that it be reformatted under the house style. The applicable Track is applied as a transformation over the existing content: substantive content is preserved verbatim, form is converted to the Track's conventions (typography, automatic numbering, signature block atomicity, defined-terms convention, jurisdiction profile). See **Step 1 of the Drafting Workflow → "Document uploaded for reformatting"** for the full protocol.

**Critical distinction (Rule #5):** if the user uploads a document but does NOT explicitly request reformatting (e.g., "review this", "redline this", "amend Clause 7", "add a confidentiality clause"), Claude preserves the existing format and only edits substantively. Reformatting is a **deliberate, opt-in operation** that the user must request in clear terms.

---

## Typography & Page Setup (Layer 1 — Universal)

These settings apply to every Company document regardless of track, unless a specific track overrides below.

| Element | Specification |
|---------|--------------|
| **Font** | Times New Roman throughout |
| **Body size** | Varies by track — see "Body size by track" below. |
| **Footer size** | 9pt |
| **Cover title** | 14pt bold, ALL CAPS |
| **Line spacing** | Single (240 twips). Track C (litigation) uses 1.5 line spacing. |
| **Paragraph spacing** | 12pt after (240 twips) |
| **Alignment** | Justified for body text; left-aligned for clause headings |
| **Page size** | A4 (11906 × 16838 DXA) |
| **Margins** | 1 inch (1440 DXA) all sides |
| **Language** | en-GB by default. Local language for litigation filings and corporate documents drafted in the jurisdiction's language (per the active jurisdiction profile). User may specify alternatives per document. |
| **Footer** | Left: *CONFIDENTIAL* (italic, 9pt). Right: page number. Track C uses court-specific footer conventions. |
| **Header** | Reserved for track-specific content: Track A long-form agreements may use a status marker (Draft / Execution version / Conformed copy) in the top-right (see "Document status marker (header)"). Track D memos use "PRIVILEGED & CONFIDENTIAL" on first page in lieu of footer. Track C uses court header conventions. Default: no header. |
| **Smart quotes** | Always. Use curly quotes (" ") and apostrophes (' '). |

### Body size by track

Different document types call for different font sizes based on reader, length, and formality conventions. Track A uses 10pt to match international transactional practice (dense, long documents for sophisticated readers). Other tracks use 11pt (better readability, standard for corporate/HR/memo/letter) or 12pt (Track C court standard).

| Track | Body size | Half-points (docx) | Rationale |
|-------|-----------|-------------------|-----------|
| **Track A** (transactional) | 10pt | 20 | international transactional convention; dense, long documents; sophisticated readers |
| **Track B** (corporate) | 11pt | 22 | Formal, relatively short; 11pt reads as "solemn" for board resolutions, POAs |
| **Track C** (litigation) | 12pt | 24 | Court standard; overrides to 1.5 line spacing |
| **Track D** (memo) | 11pt | 22 | Client-facing prose; readability wins over density |
| **Track E** (employment) | 11pt | 22 | Employee is non-sophisticated reader; 11pt appropriate |
| **Track F** (policy) | 11pt | 22 | Read by all employees; HR/policy standard |
| **Track G** (letter) | 11pt | 22 | Single-reading document; density not needed |

Footer, cover title, and smaller-text sizes remain as in the main table regardless of track.

---

## Automatic Numbering for Non-MC Tracks (Tracks C, D, F, G)

All numbered content in every Company document must use automatic numbering — never typed numbers. Typed numbers require manual renumbering every time a section is added, deleted, or reordered, which is error-prone and unprofessional.

**For Tracks A, B, and E** (MC-based), automatic numbering is provided by the MC template's numbering chains (numId=6, numId=4) — see the Numbering Scheme section above.

**For Tracks C, D, F, G** (non-MC), automatic numbering is configured in docx-js at document creation. Use the following numbering configurations, adapted per track:

### Configuration for Track C (Litigation)

Single-level decimal numbering (1., 2., 3.) for main sections. Headings are bold 12pt. Document list at end uses separate decimal numbering (Doc. 1, Doc. 2).

```javascript
numbering: {
  config: [
    {
      reference: "memoria-sections",
      levels: [{
        level: 0, format: LevelFormat.DECIMAL, text: "%1.",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 0, hanging: 360 } },
                 run: { bold: true, size: 24, font: "Times New Roman" } }
      }]
    },
    {
      reference: "memoria-docs",
      levels: [{
        level: 0, format: LevelFormat.DECIMAL, text: "Doc. %1",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 0, hanging: 720 } } }
      }]
    }
  ]
}
```

Applied to section headings: `new Paragraph({ numbering: { reference: "memoria-sections", level: 0 }, children: [new TextRun({ text: "Inquadramento processuale", bold: true, size: 24 })] })`

### Configuration for Track D (Memo)

Two-level decimal numbering (1., 1.1, 1.2, 2., 2.1) for sections and subsections. Both bold. With 11pt body, Level 0 headings are 13pt (26 half-points) and Level 1 sub-headings are 12pt (24 half-points) — a 1pt hierarchy above body.

```javascript
numbering: {
  config: [{
    reference: "memo-sections",
    levels: [
      { level: 0, format: LevelFormat.DECIMAL, text: "%1.",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 0, hanging: 360 } },
                 run: { bold: true, size: 26 } } },
      { level: 1, format: LevelFormat.DECIMAL, text: "%1.%2",
        alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 540 } },
                 run: { bold: true, size: 24 } } }
    ]
  }]
}
```

### Configuration for Track F (Policy)

Two-level numbering linked to Heading 1 and Heading 2 styles, so the auto-TOC works correctly:

```javascript
styles: {
  paragraphStyles: [
    { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 26, bold: true, font: "Times New Roman" },
      paragraph: { spacing: { before: 240, after: 240 }, outlineLevel: 0,
                   numbering: { reference: "policy-sections", level: 0 } } },
    { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
      run: { size: 24, bold: true, font: "Times New Roman" },
      paragraph: { spacing: { before: 180, after: 180 }, outlineLevel: 1,
                   numbering: { reference: "policy-sections", level: 1 } } }
  ]
},
numbering: {
  config: [{
    reference: "policy-sections",
    levels: [
      { level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 0, hanging: 360 } } } },
      { level: 1, format: LevelFormat.DECIMAL, text: "%1.%2", alignment: AlignmentType.LEFT,
        style: { paragraph: { indent: { left: 360, hanging: 540 } } } }
    ]
  }]
}
```

Applied: `new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("Scope")] })` — numbering automatic.

### Configuration for Track G (Letter)

Letters are normally prose only. If numbered paragraphs are needed (e.g., operative items in a formal engagement letter), use a simple single-level config:

```javascript
numbering: {
  config: [{
    reference: "letter-items",
    levels: [{
      level: 0, format: LevelFormat.DECIMAL, text: "%1.",
      alignment: AlignmentType.LEFT,
      style: { paragraph: { indent: { left: 720, hanging: 360 } } }
    }]
  }]
}
```

### General rule — NEVER hand-type numbers

If you find yourself typing `"**1. "`, `"**2. "`, `"(a) "`, or any other number or letter as the start of a paragraph, stop. Configure automatic numbering instead. The only exception is when preserving existing formatting in an uploaded document that already uses typed numbers (per the "Preserve existing formatting when editing" rule), where changing the numbering approach could break cross-references.

---

## Numbering Scheme (Tracks A, B, and E — MC-based documents)

The numbering scheme and MC style mappings in this section apply to Tracks A (transactional agreements), B (corporate documents), and E (employment contracts), which are all built on the MC template. Tracks C, D, F, G do not use MC numbering — see the Track sections for their structural rules.

### Body Clauses (6 levels)

| Level | Format | Example | MC Style | Notes |
|-------|--------|---------|----------|-------|
| 0 | `%1.` decimal | `1.` | `ClauseL1` | Clause heading — bold, ALL CAPS, keepNext. Heading 1 (appears in TOC). |
| 1 | `%1.%2` compound | `1.1` | `ClauseL2` | Sub-clause — normal weight, justified. No heading style. |
| 2 | `(%3)` lower alpha | `(a)` | `ClauseL3` | Paragraph |
| 3 | `(%4)` lower roman | `(i)` | `ClauseL4` | Sub-paragraph |
| 4 | `(%5)` upper alpha | `(A)` | `ClauseL5` | Rare — deep enumeration |
| 5 | `(%6)` decimal parens | `(1)` | `ClauseL6` | Rare — deepest level |

### Recitals

`(A)`, `(B)`, `(C)` — auto-numbered via `PreambleL4` style with numPr ilvl=3 numId=4. **Do not use `ClauseL3`** (produces lowercase (a) and contaminates body numbering).

### Parties (in preamble)

`(1)`, `(2)`, `(3)` — auto-numbered via `PreambleL2` style with numPr ilvl=1 numId=4.

### Schedule Clauses (independent numbering per schedule)

Same structure as body clauses (`1.` → `1.1` → `(a)` → `(i)`) but numbering restarts in each schedule. Uses styles `ScheduleL1` through `ScheduleL8`. **Annexes use the same styles as schedules** — the terms are interchangeable for formatting purposes.

### Schedule Part Headings

`Part I`, `Part II` etc. — bold, centered, title case. Used within schedules that have distinct sections (e.g., "Part I — Seller's Completion Obligations").

### Numbering Architecture — Three Chains

The MC template has exactly **three independent numbering chains**. Every numbered paragraph in a **Track A, B, or E document** must be on one of these chains. Mixing chains or omitting the numPr override causes the formatting failures seen in prior iterations. (Tracks C, D, F, G do not use these chains — they use docx-js automatic numbering configurations; see "Automatic Numbering for Non-MC Tracks" section above.)

| Chain | numId | What it numbers | Styles | Used in |
|-------|-------|----------------|--------|---------|
| **Body clauses** | 6 | `1.` → `1.1` → `(a)` → `(i)` → `(A)` → `(1)` | `ClauseL1` through `ClauseL6` | Operative clauses in agreements, notice operative provisions |
| **Preamble / corporate** | 4 | `(1)` `(2)` parties; `(A)` `(B)` recitals | `PreambleL2` (ilvl=1), `PreambleL4` (ilvl=3) | Preamble parties, recitals, resolution paragraphs |
| **Schedules** | Per schedule | `1.` → `1.1` → `(a)` (restarts per schedule) | `ScheduleL1` through `ScheduleL8` | Schedule and annex content |

**Rule:** Every `ClauseL*` paragraph needs an explicit `<w:numPr>` pointing to numId=6. Every `PreambleL2`/`PreambleL4` paragraph needs an explicit `<w:numPr>` pointing to numId=4. Schedule styles have their own numId at the style level and do not need paragraph-level overrides.

**Choosing the right chain:**
- Does this paragraph number a clause or sub-clause in the body of an agreement? → **numId=6** (body clause chain)
- Does this paragraph number a party, recital, or resolution? → **numId=4** (preamble/corporate chain)
- Does this paragraph appear inside a schedule or annex? → **ScheduleL*** (schedule chain)

---

## Body Text Continuation Styles (Tracks A, B, and E)

When un-numbered continuation text follows a numbered clause in a Track A, B, or E document, it must align with the text (not the number) of the clause above it:

| After level | Continuation indent | Notes |
|-------------|-------------------|-------|
| Level 0 or 1 (clause / sub-clause) | 720 DXA | Aligns with `1.` or `1.1` text |
| Level 2 `(a)` | 1440 DXA | Aligns with paragraph text |
| Level 3 `(i)` | 2160 DXA | Aligns with sub-paragraph text |

---

## Definitions Layout (Tracks A and E — agreements with definition glossaries)

Defined terms in a glossary (Clause 1 of a Track A agreement or a Track E employment contract that uses a definitions clause) use a hanging format at 720 DXA indent:

> "**Purchase Price**" means [definition text continues here and wraps to align with the opening of the definition, not with the opening quote mark];

Rules:
- Defined term in **bold** within curly double quotes
- Semicolon after each definition except the last (full stop)
- Alphabetical order
- Cross-references to other defined terms are not bolded after first use

---

## Document Structure

### Track selection (do this first)

Before drafting any document, identify the track:

1. Is the user asking for a **transactional agreement** (SPA, SHA, NDA, LOI, loan agreement, cooperation agreement, JDA, side letter, amendment, deed, guarantee, **mandate letter, indemnity letter, comfort letter, or any letter agreement that creates operative obligations or contains indemnities/warranties/governing law**)? → **Track A**
2. Is the user asking for a **corporate document** (board resolution, shareholder resolution, POA, articles of association, written resolution, director appointment)? → **Track B**
3. Is the user asking for a **court filing** (memoria, brief, pleading, writ, response to court)? → **Track C**
4. Is the user asking for a **memo, opinion, or regulatory analysis** (legal opinion, advice memo, tax memo, regulatory analysis or submission)? → **Track D**
5. Is the user asking for an **employment contract** between the Company and an individual employee? → **Track E**
6. Is the user asking for a **policy, procedure, or code of conduct** (travel policy, expense policy, HR policy, code of conduct, internal guideline)? → **Track F**
7. Is the user asking for a **pure-correspondence letter** (cover letter, transmission letter, formal notice outside an agreement, request letter — NOT a letter that contains indemnities, warranties, or governing law clauses, which is Track A)? → **Track G**

If the request is ambiguous (e.g., "draft a document about X"), ask the user which type before proceeding. Getting the track wrong produces visible formatting failures.

Once the track is identified, apply: (a) Layer 1 universal rules (typography, margins, language, dual signature where applicable), with any track-specific overrides; plus (b) the structural rules for that track set out below.

### Flexibility principle

Cover pages and TOC are **optional** — use them when the document warrants it, omit them when it does not. The decision tree:

- **Cover page**: include for full-form agreements with 3+ parties or where the document will be bound. Omit for short-form, corporate docs, correspondence.
- **TOC**: include when the document exceeds 10 clauses. Omit otherwise.
- Neither is ever wrong to include if the user requests it.

### Definitions placement

**For Track A and Track E (agreements):** definitions belong in the body of the agreement, typically Clause 1 (Interpretation), not in a Schedule. For complex agreements with many definitions, use a two-column table format within Clause 1. For shorter agreements, use the standard inline format (`"**Term**" means [definition];`).

**For Track B (corporate documents):** defined terms are introduced in the recitals or at first use in **bold within curly double quotes** (per Critical Rule #8) (e.g., the `"**Sole Shareholder**"`), then used capitalised without bold.

**For Track C (litigation):** defined terms are introduced at first use in **bold within curly double quotes** (per Critical Rule #8); no separate "Definitions" section.

**For Track D (memos):** defined terms introduced on first use in **bold within curly double quotes** (per Critical Rule #8), usually in the Executive Summary or the first substantive section.

**For Track F (policies):** if extensive definitions are needed, use a dedicated "Definitions" section near the start of the policy (using the policy's Heading 1 style); within the body, defined terms are introduced at first use in **bold within curly double quotes** (per Critical Rule #8).

**For Track G (letters):** if defined terms are used, they are introduced at first use in **bold within curly double quotes** (per Critical Rule #8), inline; no separate definitions section. Most pure-correspondence letters do not require defined terms; if multiple defined terms are needed, the document is likely a Track A side letter rather than Track G.

### Company signature blocks

**Default: two (2) signature blocks for the Company** on every document where the Company signs as a party (Tracks A and B, and Track E for employer side). This reflects a dual-signatory requirement (common for Dutch B.V.s and many other in-house structures). Format:

```
For and on behalf of [COMPANY ENTITY NAME]

____________________________________          ____________________________________
Name:                                         Name:
Title:                                        Title:
Date:                                         Date:
```

Counterparty signature blocks follow the counterparty's own requirements (single or dual as appropriate).

**Exceptions (single signature or no signature block):**
- Track C (litigation): lawyer's signature only, not Company dual signature
- Track D (memos): author's name and title, no signature block
- Track E (employment contracts): employee signs singly, employer side is the Company dual block
- Track F (policies): approval block at end (approved by Board/CEO), not bilateral signature
- Track G (letters): single or dual signature depending on letter's legal effect (most letters are single)

### Entity details — mandatory verification

When drafting any document that includes a Company group entity's full legal details (legal name, registered address, statutory seat, commercial register number), Claude **shall** search the document repository for the corresponding commercial register extract **before** writing those details. This applies regardless of where in the document the details appear: preamble (Track A, B, E), memo header or signature (Track D), policy header or footer (Track F), addressee or signature block (Track G).

**Workflow:**
1. Identify each Company group entity that will appear with full details in the document
2. Search `[document repository: commercial register extracts folder]` using `sharepoint_search` or `sharepoint_folder_search` for each entity
3. Read the extract with `read_resource` to obtain: legal name (exact spelling), registered address, statutory seat, commercial register number
4. Use these exact details in the document — do not draft from memory or training data
5. If no extract is found for an entity, flag this to the user: "No commercial register extract found in the document repository for [entity name]. Please provide the correct details or upload the extract."
6. If repository search tools are unavailable in the current session (M365 connector not active), flag this to the user: "Repository search tools not available — cannot verify entity details against commercial register extracts. Please confirm the entity details are current before finalising." Proceed with details from uploaded documents, training data, or user input, clearly marking them as unverified.

This workflow applies to both new documents and when adding or editing party descriptions in existing documents.

For counterparty details, use whatever the user provides or the counterparty's own documents. Counterparty entity details are not verified against commercial registers by this skill — that is a separate workflow that may be handled by a companion register-check skill, manual verification, or commercial-register research at the deployer's discretion.

### Track A — Transactional: Full-form agreements (SPAs, SHAs, loan agreements, cooperation agreements, JDAs)

**Built on the MC template.** Use `inhouse-mc-template.docx` as the base via the unpack → edit XML → repack workflow. Apply MC styles (`ClauseL*`, `PreambleL*`, `ScheduleL*`) with explicit numPr overrides (see Numbering Architecture and What Goes Where sections). **Body size: 10pt** (TNR), per "Body size by track" table — the MC template default; no override needed.

1. **Cover page** — table-based (borderless), optional per flexibility principle above
2. **Table of Contents** — optional per flexibility principle above. When included, the "Table of contents" heading may be styled in the Company's signature colour (if any) — e.g., dark red, navy, charcoal — to provide visual hierarchy. Default to plain black bold if no Company colour is defined. Page numbers right-aligned with dot leaders. Heading 1 entries from `ClauseL1` automatically populate the TOC.
3. **Preamble** — "THIS AGREEMENT is made on [date]" → BETWEEN → numbered parties → WHEREAS → lettered recitals → "IT IS AGREED as follows"
4. **Clause 1: Interpretation** — definitions in body (table or inline format), followed by construction/interpretation rules
5. **Operative clauses** — numbered per scheme, in standard clause order (see Boilerplate Library below)
6. **Execution block** — "IN WITNESS WHEREOF" → signature blocks (2 per Company entity)
7. **Schedules** — each on new page, centred "SCHEDULE [n]" heading + title, independent numbering. Used for detailed items (completion obligations, warranties, notice details, data room index) — not for definitions.

### Track A — Transactional: Short-form agreements (NDAs, LOIs)

1. **No cover page** — document starts with centred title (`NormalBold`), then date and parties
2. **No TOC** unless > 10 clauses
3. **Preamble** — same styles as full-form: `PreambleL2` for parties (numId=4 ilvl=1), `PreambleL4` for recitals (numId=4 ilvl=3)
4. **Definitions** — inline within Clause 1 if needed, or defined in-line on first use if few
5. **Body clauses** — `ClauseL1`/`ClauseL2`/`ClauseL3` with numPr numId=6, same as full-form agreements
6. **Execution block** — same format (dual Company signature blocks)
7. **Schedules / Annexes** — only if needed; use `ScheduleL*` styles

### Track A — Transactional: Side letters and amendments

1. **No cover page** — document starts with centred title
2. **Preamble** — same as agreements: `PreambleL2` for parties (numId=4 ilvl=1), `PreambleL4` for recitals (numId=4 ilvl=3)
3. **Body clauses** — `ClauseL1`/`ClauseL2`/`ClauseL3` with numPr numId=6. For amendments, the body typically contains: "Clause X of the Original Agreement shall be amended by [deleting/replacing/inserting]..."
4. **Execution block** — same format (dual Company signature blocks)
5. **Side letters in letter format** — use addressee block (`BodyText`), "Dear Sirs," (`BodyText`), body paragraphs (`BodyText` or numbered with numId=6 if operative), "Yours faithfully" (`BodyText`), with a countersignature acknowledgement block

### Track A — Transactional: Formal notices under agreements

1. **No cover page, no TOC, no schedules**
2. **Addressee block** → `BodyText` (entity name, address, attention line)
3. **Date** → `BodyText`
4. **Subject line** → `NormalBold` or `BodyText` with bold run
5. **Body** — uses `BodyText` for prose. If the notice has operative provisions (e.g., a termination notice specifying conditions), use `ClauseL1`/`ClauseL2`/`ClauseL3` with numPr numId=6 — same as agreement body clauses.
6. **Closing** → `BodyText` ("Yours faithfully," / signature)

### Track B — Corporate: Board resolutions, shareholder resolutions, POAs

**Built on the MC template.** Use `inhouse-mc-template.docx` as the base. Unlike Track A, Track B uses the preamble/corporate numbering chain (numId=4) for recitals and resolutions — not the body clauses chain (numId=6). No `ClauseL*` styles in Track B.

**Font size override:** The MC template defaults to 10pt body (set for Track A transactionals). For Track B, override body text to 11pt per the "Body size by track" table. In the unpack → edit XML workflow, set `<w:sz w:val="22"/>` and `<w:szCs w:val="22"/>` on the Normal style `rPr` (or apply to each paragraph's run properties) to shift the document to 11pt.

1. **No cover page or TOC**
2. **Header block** — document title (centred, bold, caps) → `NormalBold` centred. Company name → `NormalBold`. "THE UNDERSIGNED:" → `NormalBold`.
3. **Signatories/parties** — For a sole shareholder or sole director, use `BodyText` (no numbered style — single entity needs no numbering). For multiple shareholders/directors, use `PreambleL2` with numPr ilvl=1 numId=4 → auto (1), (2), (3).
4. **"hereinafter referred to as..." line** → `BodyText`
5. **"WHEREAS:" label** → `NormalBold`
6. **Recitals (A), (B), (C)...** → `PreambleL4` with numPr ilvl=3 numId=4
7. **"IT IS HEREBY RESOLVED:" label** → `NormalBold`
8. **Resolutions (1), (2), (3)...** → `PreambleL2` with numPr ilvl=1 numId=4. If a resolution has sub-items, use `PreambleL4` (ilvl=3 numId=4) for lettered sub-items (A), (B).
9. **Closing text** (e.g., "Pursuant to article 2:230...") → `BodyText`
10. **Signature** — director names/titles → `BodyText`. Dual signature block for the Company entities.

### Track C — Litigation: Court filings (jurisdiction-specific conventions)

**Override to Layer 1:** Track C uses TNR 12pt (court standard), line spacing 1.5, and the local jurisdiction's language for court filings (per the active jurisdiction profile). Do NOT apply MC numbering styles (`ClauseL*`, `PreambleL*`, `ScheduleL*`). Do NOT use WHEREAS/IT IS AGREED/BETWEEN labels. Do NOT build on the MC template — use a blank Word document with Track C styles applied directly.

**Track C is the most jurisdiction-specific track.** The structure below illustrates an Italian-court filing (the starter Italy profile includes with complete Track C conventions). For other jurisdictions, the deployer should extend the active profile with the local litigation conventions (court header format, document title conventions, procedural references, drafting language, prayer for relief block).

**Illustrative structure (Italian profile — adapt per the active profile for other jurisdictions):**

1. **Court header** — court name, section, judge, case number → bold centred at top, TNR 12pt (per profile; e.g., for Italy: "TRIBUNALE ORDINARIO DI [CITY] / Sezione [N] [Civile/Lavoro] / R.G. n. [number]/[year] – Giudice [dott./dott.ssa Name]")
2. **Parties block** — narrative format per local convention (e.g., for Italy: "Sigg.ri X e Y (attori), rappresentati e difesi dall'Avv. Z / contro / [Counterparty] (convenuta), rappresentata e difesa dall'Avv. W") → body prose 12pt. Bold for party names and lawyer names.
3. **Document title** — local convention (e.g., for Italy: "MEMORIA INTEGRATIVA", "COMPARSA CONCLUSIONALE", "RICORSO"; for Germany: "KLAGESCHRIFT", "SCHRIFTSATZ"; for England: "WITNESS STATEMENT", "PARTICULARS OF CLAIM") → bold centred, 14pt, ALL CAPS
4. **Procedural reference** — local procedural code reference (e.g., for Italy: "ex art. 426 c.p.c." / "per l'udienza del [date]"; for Germany: "§ 282 ZPO") → italic, centred, 12pt
5. **Separator line** — optional horizontal rule
6. **Opening formula** — local formal opening (e.g., for Italy: "Nell'interesse di...") → body prose 12pt
7. **Numbered sections** — bold section headings numbered `1.`, `2.`, `3.` (single-level, no sub-clauses). Use automatic numbering via the `memoria-sections` docx-js numbering config (see "Automatic Numbering for Non-MC Tracks" above). Numbers and headings are 12pt bold. Body of each section is narrative prose 12pt with 1.5 line spacing. Do NOT type numbers by hand.
8. **Prayer for relief block** — local convention (e.g., for Italy: "CONCLUSIONI" bold centred 12pt; followed by bullet list or dashed list of specific requests "chiedono che l'Ill.mo Tribunale voglia: - ..."). Each bullet in body prose.
9. **Date and location** — "[City], [date]" (e.g., "Roma, 3 giugno 2026") → body prose
10. **Signature** — lawyer's name and credentials per local convention (e.g., for Italy: "Avv. [Name]") → body prose, no dual Company block (this is lawyer's filing)
11. **Evidence list** — use automatic numbering via the `memoria-docs` docx-js numbering config (Italian convention: "Doc. 1 – [description]", "Doc. 2 – [description]"). For other jurisdictions, the deployer may rename the config or add a parallel numbering config (`exhibits` for English, `Anlagen` for German, etc.). Do NOT type evidence numbers by hand — if a document is added or removed, the numbering must update.

### Track D — Memo: Legal opinions, tax memos, regulatory analyses

**Override to Layer 1:** No CONFIDENTIAL footer for client-facing memos; instead use "PRIVILEGED & CONFIDENTIAL" in header on first page. No WHEREAS/IT IS AGREED. Do NOT build on the MC template. Do NOT use MC styles (`ClauseL*`, `PreambleL*`).

1. **Memo header** — formatted block at top:
   - **To:** [recipient]
   - **From:** [author / the Legal team]
   - **Date:** [date]
   - **Re:** [subject] (bold)
   - **Privileged & Confidential** (italic, right-aligned)
2. **Horizontal separator**
3. **Executive summary** (optional) — bold heading "Executive Summary" (13pt bold), followed by 1-2 paragraphs of body prose (11pt per Track D — see "Body size by track")
4. **Numbered sections** — bold section headings numbered `1.`, `2.`, `3.`; sub-sections `1.1`, `1.2` below. Use automatic numbering via the `memo-sections` docx-js numbering config (see "Automatic Numbering for Non-MC Tracks" above). Body in 11pt body prose. Do NOT type numbers by hand.
5. **Footnotes** for citations — TNR 9pt, proper legal citation format
6. **Conclusion** — bold heading "Conclusion", followed by body prose
7. **Signature** — "[Name], [Title]" → body prose. No dual signature block (memos are authored, not executed).

### Track E — Employment: Employment contracts between the Company and individual employees

Track E documents are employment agreements between the Company (as employer) and an individual employee. They are built on the MC template — same engine as Track A — because employment contracts are agreements with preamble, recitals, and numbered clauses. The structure is typically flatter than commercial agreements (fewer sub-clauses, fewer schedules). HR policies and codes of conduct are NOT Track E — they are Track F.

**Font size override:** The MC template defaults to 10pt body. For Track E, override body text to 11pt per the "Body size by track" table (same mechanism as Track B).

1. **Title** — "EMPLOYMENT AGREEMENT" → `NormalBold` centred
2. **Preamble** — use `PreambleL2` for parties (Employer + Employee) with numPr ilvl=1 numId=4. Employee description: full name, DOB, residential address. Employer description: full corporate details (verify per Entity details workflow above).
3. **"WHEREAS:" and recitals** — if used, `NormalBold` + `PreambleL4` with numPr ilvl=3 numId=4
4. **"IT IS AGREED as follows"** → `NormalBold`
5. **Body clauses** — `ClauseL1` for clause headings, `ClauseL2` for sub-clauses, each with numPr numId=6 (same rules as Track A). Use sub-clauses sparingly; employment agreements are typically flatter than commercial agreements.
6. **Execution block** — dual signature block for Employer (the Company) per Layer 1 universal rule; single signature line for Employee. Not dual-dual as in Track A commercial agreements.

### Track F — Policy: Internal policies, procedures, guidelines

**Do NOT build on the MC template.** Use a blank Word document with Word's native heading styles (Heading 1, Heading 2) configured with TNR, with body text at 11pt (per Track F), Heading 1 at 13pt bold and Heading 2 at 12pt bold, and linked to automatic numbering via the `policy-sections` docx-js numbering config (see "Automatic Numbering for Non-MC Tracks" above).

1. **Title page** — policy name, effective date, version, owner (e.g., "[Company] Travel and Expenses Policy / Effective 1 January 2026 / Version 2.1 / Owner: Finance Department")
2. **Table of Contents** — include for policies > 5 pages; use Word's built-in TOC tied to Heading 1/Heading 2. The auto-numbering flows into the TOC automatically.
3. **Section headings** — apply `HeadingLevel.HEADING_1` for main sections (renders as `1.`, `2.`, `3.` automatically via the numbering config); `HeadingLevel.HEADING_2` for subsections (renders as `1.1`, `1.2`). NEVER type section numbers by hand — the numbering is in the style.
4. **Body prose** → body text 11pt (per Track F — see "Body size by track")
5. **Lists within sections** — bullets or numbered lists using Word's native list styles (configured as a separate numbering reference, e.g., `policy-lists`)
6. **Definitions section** — if needed, early in the document as a `Heading 1` titled "Definitions"
7. **Approval/review block** at the end — "Approved by: [Board / CEO] / Date: [date] / Next review: [date]"
8. No dual Company signature block (policies are issued, not executed as bilateral agreements)

### Track G — Letter: Formal correspondence, engagement letters

**Do NOT build on the MC template.** Use a blank Word document with body prose only. **Body size: 11pt** (TNR), per "Body size by track" table — single-reading documents, density not needed.

**CRITICAL — Track G vs Track A side letter test:** Before applying Track G, check whether the document is a **letter agreement** (a contract dressed as a letter) rather than pure correspondence. Apply this test:

> *Does the letter create operative obligations, indemnities, warranties, governing law/jurisdiction provisions, or require countersignature with "ACCEPTED AND AGREED"?*
>
> - **Yes → Track A side letter format** (see "Track A — Transactional: Side letters and amendments" above). Use MC styles `ClauseL1`/`ClauseL2`/`ClauseL3` with numId=6 inside the letter format. Common examples: mandate letters, indemnity letters, comfort letters, side letters under a main agreement, engagement letters with detailed terms (legal fees, scope, indemnity), letter agreements.
> - **No → Track G (this section).** Pure correspondence: cover letters, transmission letters, request letters, formal notices outside an agreement, social/protocol letters, brief engagement letters with no contractual mechanics.

If the answer is borderline, default to Track A side letter — it scales down (1./1.1 numbering can be omitted for short letters) but Track G does not scale up.

**Track G structure (pure correspondence only):**

1. **Company letterhead block** at top (if used) — body prose, indented
2. **Date** → body prose, right-aligned
3. **Addressee block** — recipient name, title, entity, address → body prose
4. **"Dear [Name]" / "Dear Sirs,"** → body prose
5. **Subject line** — bold, optionally preceded by "Re:"
6. **Body paragraphs** — body prose. If a small number of operative items are needed (e.g., enclosures list), use automatic numbering via the `letter-items` docx-js numbering config — single-level only. For anything more complex (multi-level numbering, sub-clauses, defined terms, operative obligations), the letter is NOT Track G — apply Track A side letter format.
7. **"Yours faithfully," / "Yours sincerely,"** → body prose
8. **Signature block** — name and title → body prose. Dual signature only if the letter has legal effect requiring dual authorisation (most don't).

---

## Drafting Conventions (Tracks A, B, and E — MC-based documents)

The conventions in this section apply to Track A (transactional agreements), Track B (corporate documents), and Track E (employment contracts) — i.e., all MC-based documents. Other tracks follow their own conventions:
- **Track C (litigation):** narrative prose in Italian or other court language; no "shall/may" operative verbs; Italian legal terminology.
- **Track D (memo):** analytical prose; defined terms introduced inline on first use in **bold within curly double quotes** (per Critical Rule #8); no operative clauses.
- **Track F (policy):** clear imperative language ("Employees must..."); heading-based structure; no clause cross-references.
- **Track G (letter):** conversational prose; defined terms (if any) follow Critical Rule #8 (bold within curly quotes on first use); no operative verbs beyond what's natural in correspondence.

### Operative language

- **Operative verb**: `shall` for obligations, `may` for permissions, `shall not` for prohibitions
- **Passive avoidance**: prefer "the Seller shall deliver" over "the documents shall be delivered by the Seller"

### Defined terms

- **First use**: bold within curly double quotes — the "**Purchase Price**"
- **Subsequent use**: capitalised, no bold, no quotes — the Purchase Price
- **Party references**: defined in the preamble, used consistently throughout. Short form after first use (e.g., `[Company legal name] B.V. (the "**Purchaser**")` → thereafter `the Purchaser`)

### Enumeration

- Items in a list end with semicolons
- Penultimate item: `; and` or `; or` (as appropriate)
- Final item: full stop
- Chapeau (introductory text) ends with colon
- Example:
  ```
  1.1  The following conditions shall be satisfied:
       (a)  [first condition];
       (b)  [second condition]; and
       (c)  [third condition].
  ```

### Cross-references

- To clauses (Track A short form): `Clause 3.2` (capitalised, no parentheses around number)
- To clauses with title (international finance and long-form contract style): `Clause 3.2 (*Withholding tax*)` — clause number followed by the clause title in italics within parentheses. Used widely in international finance documentation drafting. Recommended for facility agreements, complex SPAs, JV agreements, and any document >30 pages
- To schedules: `Schedule 1 (Completion Obligations)` — number + title in parentheses; title in italics if following international finance documentation convention (`Schedule 1 (*Completion Obligations*)`)
- To paragraphs within schedules: `paragraph 3(d) of Schedule 1` — precise to sub-paragraph level, never just "Schedule 1" when a specific provision is relevant
- To parts within schedules: `Part I of Schedule 3 (Seller's Warranties)` or `Part I of Schedule 3 (*Seller's Warranties*)` (international finance convention)
- To definitions in Clause 1: `as defined in Clause 1.1` or simply use the capitalised Defined Term without further cross-reference
- **Consistency rule**: pick one convention (plain or italics) for cross-reference titles and apply it throughout the document. Mixing plain and italics looks unprofessional.

### Paragraph captions (italic caption convention)

When a clause contains a series of `(a)`, `(b)`, `(c)` paragraphs each addressing a different sub-topic, a widely-used convention in international finance documentation is to introduce each paragraph with a **caption in italics followed by a colon**:

```
10.1  Unavailability of Screen Rate
      (a)  *Interpolated Screen Rate*: If no Screen Rate is available for EURIBOR
            for the Interest Period of a Loan, the applicable EURIBOR shall be the
            Interpolated Screen Rate for a period equal in length to the Interest
            Period of that Loan.
      (b)  *Reference Bank Rate*: If no Screen Rate is available for EURIBOR for: ...
      (c)  *Cost of funds*: If paragraph (b) above applies but no Reference
            Bank Rate is available for euro or the relevant Interest Period there
            shall be no EURIBOR for that Loan and clause 10.4 (*Cost of funds*)
            shall apply to that Loan for that Interest Period.
```

This is standard in international finance and facility documentation. Use when paragraphs cover distinct sub-topics that benefit from visual identification. Do NOT use when paragraphs are simply enumerated items (lists of conditions, lists of events).

### Provisos and chapeau-level paragraphs

After a series of `(a)`, `(b)`, `(c)` sub-paragraphs, a **proviso** or limitation that applies to the enumeration as a whole is inserted as an un-numbered paragraph **indented at the chapeau level** (not at the sub-paragraph level). Example from a typical Events of Default clause:

```
23.1  Non-payment
      An Obligor does not pay on the due date any amount payable under any
      Finance Document at the place at which and in the currency in which it is
      expressed to be payable unless:
      (a)  its failure to pay is caused by administrative or technical error; and
      (b)  payment is made within 3 Business Days of its due date.

23.X  ...
      [...]
      (h)  any party to a Project Document repudiates a Project Document; or
      (i)  any counterparty to a Direct Agreement gives any notification of
            restricted action,
      provided that an Event of Default shall not occur under sub-paragraphs (b),
      (e) and (h) of this paragraph in respect of a Project Document if the
      Agent is satisfied that the Obligors are taking all necessary steps to
      replace the relevant Project Document.
```

The closing proviso is at the chapeau indent level (aligned with the start of `(a)`'s text), not at the `(a)` indent itself. Use `BodyText1` style or equivalent — un-numbered, indented to match the chapeau.

### Complex (multi-level) definitions

Standard single-line definitions use the inline format (`"**Term**" means [content];`). For complex definitions covering different cases or scenarios, use a multi-level format mirroring the body clause structure:

```
"**Availability Period**" means:
(a)  in relation to the Facility A, the period commencing on Financial
     Close and ending on the earlier of the Final Completion Date and the
     Backstop Completion Date for Project A;
(b)  in relation to the Facility B, the period commencing on Financial
     Close and ending on the earlier of the Final Completion Date and the
     Backstop Completion Date for Project B;
```

Or even three-level definitions for very complex defined terms:

```
"**Costs Certificate**" means in respect of a Project, a certificate provided
by the Parent to the Agent and the Technical Adviser in relation to each
proposed Loan under a Term Facility:
(a)  setting out the applicable Eligible Costs that:
     (i)   are due and payable; and
     (ii)  will become due for payment within 30 days from the Utilisation Date,
     in a sufficient level of detail; and
(b)  confirming that the aggregate amount of Eligible Costs incurred by the
     relevant Borrower do not exceed the aggregate amount of Eligible Costs
     anticipated to be incurred...
```

The multi-level format is appropriate for facility agreements, complex SPAs, JV agreements, and any document with definitions that vary by case, jurisdiction, or scenario. Use sparingly — most definitions are single-line.

### Document status marker (header)

Long-form transactional documents typically carry a **status marker** in the top-right of every page indicating the version state:

- `Draft` — at any pre-execution stage
- `Draft for discussion` — circulated for discussion but not the agreed text
- `Approved for execution` — approved internally, awaiting signature
- `Execution version` — the version being signed
- `Conformed copy` — post-signature, with signatures replaced by typed names

The status marker is shown in the header (not the footer, which carries CONFIDENTIAL and page numbers). Add the marker for Track A long-form agreements and remove or update it at each stage. For shorter Track A documents (NDAs, LOIs, short side letters), the status marker is optional.

### Page numbering for long-form documents

Track A long-form agreements (>30 pages, typically with cover page + TOC + body + schedules) use **mixed page numbering**:

- **Cover page**: no page number
- **TOC**: lowercase Roman numerals (i, ii, iii) starting from i
- **Body and schedules**: Arabic numerals (1, 2, 3, ...) restarting from 1

This is a financial / international standard for long-form agreements. Shorter Track A documents (NDAs, LOIs, short side letters, amendments) use Arabic numbering throughout, starting from 1, without restart.

### Recital labels

- `WHEREAS` (bold, left-aligned) introduces the recital block — use `NormalBold` style
- Individual recitals lettered `(A)`, `(B)`, `(C)` — auto-numbered via `PreambleL4` style with numPr ilvl=3 numId=4
- Recitals are factual/background — no operative obligations

### Execution block

- `IN WITNESS WHEREOF the Parties have executed this Agreement on the date first above written.`
- Company entities: **two (2) signature blocks** side by side (dual signatory)
- Counterparty entities: signature block per their requirements
- Each block: `For and on behalf of [ENTITY NAME]` (bold) → signature line → Name / Title / Date

---

## Boilerplate Clause Library (Track A — Transactional Agreements)

The following clauses are standard in-house counsel boilerplate (drafted from the Company's perspective) for Track A (transactional agreements). Track B (corporate documents) has its own corporate-specific language (resolutions, authorisations) that does not use this library. Track E (employment contracts) uses only a small subset of this library (typically Confidentiality, Entire Agreement, Variation and Waiver, Severability, Governing Law) — see the specific clauses below and adapt for employment context. Tracks C, D, F, G do not use this library.

When drafting a Track A document, include the relevant clauses from this library using the locked wording below (adapted only for defined terms and cross-references specific to the document). The clause ordering shown here is the **standard sequence** for Track A full-form agreements — follow this order unless the document type requires a different structure.

### Standard clause ordering for full-form agreements

1. Interpretation (definitions + construction rules)
2. [Operative clauses specific to the transaction]
3. [Transaction-specific substantive clauses]
4. Confidentiality
5. Further assurances
6. Assignment
7. Payments *(if applicable)*
8. Costs *(if applicable)*
9. No partnership *(if applicable — JDAs, cooperation agreements)*
10. Good faith *(if applicable — JDAs, long-term agreements)*
11. Notices
12. Entire agreement
13. Variation and waiver
14. Waiver of local civil code remedies *(civil law jurisdictions only — see jurisdiction profile)*
15. Severability
16. Counterparts and electronic execution
17. Third party rights
18. Sanctions *(if applicable)*
19. Anti-bribery / Anti-corruption *(if applicable)*
20. Language *(only if needed)*
21. GDPR / Data processing *(if applicable)*
22. Governing law and dispute resolution *(always last substantive clause)*

### Locked boilerplate wording

Listed in standard clause order (positions 1–22). Positions without locked wording (Confidentiality, Notices, Sanctions, Anti-bribery) are drafted per-transaction based on the Company's strongest position for the jurisdiction.

**[Pos. 1] Construction Rules (always in Clause 1, after definitions)**

> [Clause 1.X].1 — References to Clauses and Schedules are references to clauses of, and schedules to, this Agreement and references to paragraphs are to paragraphs of the relevant Schedule.
>
> [Clause 1.X].2 — The Schedules form part of this Agreement and shall have effect as if set out in full in the body of this Agreement.
>
> [Clause 1.X].3 — Words denoting the singular shall include the plural and vice versa. Words denoting one gender shall include another gender.
>
> [Clause 1.X].4 — Any words following the terms "including", "include", "in particular", "for example" or any similar expression shall be construed as illustrative and shall not limit the sense of the words, description, definition, phrase or term preceding those terms.
>
> [Clause 1.X].5 — The headings in this Agreement are for reference only and shall not affect the interpretation of this Agreement.
>
> [Clause 1.X].6 — A reference to a statute or statutory provision is a reference to it as amended, extended or re-enacted from time to time, and shall include all subordinate legislation made from time to time under that statute or statutory provision.
>
> [Clause 1.X].7 *(local concepts construction rule — jurisdiction-dependent; load from the active jurisdiction profile)* — Use the wording from the active profile. Common pattern (civil law jurisdictions drafting in English): "*English language words used in this Agreement intend to describe [jurisdiction] legal concepts only and the consequences of the use of such words in English law or any other foreign law shall be disregarded. Where a [language] word is included in italics and in brackets after an English word and there is any inconsistency between the [language] and the English, the meaning of the [language] word shall prevail.*" For common law jurisdictions drafting in English, this paragraph is generally not needed.

**[Pos. 5] Further Assurances (standard)**

> Each Party shall (at its own expense) promptly execute and deliver such documents, perform such acts and do such things as the other Party may reasonably require from time to time for the purpose of giving full effect to this Agreement.

**[Pos. 5 — Extended variant (jurisdictions with statutory good faith)] Further Assurances (extended)**

> Each Party shall (at its own expense) promptly execute and deliver such documents, perform such acts and do such things as the other Party may reasonably require from time to time for the purpose of giving full effect to this Agreement. The Parties shall act in good faith and in a reasonable manner, shall be accommodating and practical, and shall provide such cooperation as may be reasonably necessary for the attainment of the aim of this Agreement.

*Use the extended variant in jurisdictions with a strong statutory good-faith default (Netherlands, Germany, Italy, Hungary, Poland, etc.). Use the standard variant in common law jurisdictions where the extended language would create unintended duties.*

**[Pos. 6] Assignment**

> [Clause X].1 — [Company entity] may assign this Agreement, or any of its rights or obligations hereunder, to any of its Affiliates or to any successor entity resulting from a merger or reorganisation, provided that the assignee assumes all obligations under this Agreement. Any other assignment by [Company entity] requires the prior written consent of [Counterparty].
>
> [Clause X].2 — [Counterparty] shall not assign, transfer, mortgage, charge, declare a trust of, or deal in any other manner with any of its rights or obligations under this Agreement without the prior written consent of [Company entity].
>
> *Note: Company-favourable default. For JDAs with trusted partners, adjust affiliate assignment to mutual.*

**[Pos. 7] Payments** — interest mechanism is **jurisdiction-dependent; load from the active jurisdiction profile**.

Universal paragraphs (apply regardless of jurisdiction):

> [Clause X].1 — Unless otherwise expressly stated in this Agreement, all payments shall be made in [Euro / USD / GBP / local currency as agreed].
>
> [Clause X].3 — All payments made under this Agreement shall be made gross, free of any right of counterclaim or set-off and without deduction or withholding of any kind.

Jurisdiction-dependent paragraph (interest on default):

> [Clause X].2 — [Interest on default — apply the wording from the active jurisdiction profile. See "Starter Jurisdiction Profiles" for the wording per starter jurisdiction. Common patterns: statutory commercial interest rate (civil law jurisdictions), base rate + agreed margin (common law jurisdictions), or contractual rate negotiated between the parties.]

**[Pos. 8] Costs**

> Except as otherwise provided in this Agreement, each Party shall bear its own costs and expenses, including the fees and expenses of its legal and other advisers, incurred in connection with the entering into and the execution of this Agreement.

**[Pos. 9] No Partnership or Agency**

> Nothing in this Agreement is intended to or shall operate to create a partnership or joint venture of any kind between the Parties, or to authorise either Party to act as agent for the other, and neither Party shall have authority to act in the name or on behalf of or otherwise to bind the other in any way.

**[Pos. 10] Good Faith** — **jurisdiction-dependent; load from the active jurisdiction profile**.

In **civil law jurisdictions** (NL, IT, HU, PL, DE, FR, ES, etc.), good faith is generally an implicit statutory default that need not be expressly restated, though parties may include an express clause for emphasis or to extend the scope of the duty.

In **common law jurisdictions** (England, most US states, Singapore, Hong Kong), there is no general implied duty of good faith in commercial contracts. Including an express good faith clause creates a contractual obligation that would not otherwise exist — use only if commercially intended (typical in JDAs and long-term partnerships); avoid in straight transactional documents.

Apply the wording and warning from the active jurisdiction profile. Default neutral wording (where the user intends an express good faith standard regardless of jurisdiction):

> The Parties undertake to act towards one another in good faith in all respects relating to this Agreement.

**[Pos. 12] Entire Agreement**

> [Clause X].1 — This Agreement constitutes the entire agreement between the Parties in relation to its subject matter and supersedes all previous agreements, understandings and arrangements between the Parties, whether written or oral, relating to such subject matter.
>
> [Clause X].2 — Each Party acknowledges that in entering into this Agreement it has not relied on, and shall have no right or remedy in respect of, any representation, warranty, collateral contract or other assurance (whether made innocently or negligently) that is not set out in this Agreement.

**[Pos. 13] Variation and Waiver**

> [Clause X].1 — No variation of this Agreement shall be effective unless it is in writing and signed by or on behalf of each of the Parties.
>
> [Clause X].2 — No failure or delay by a Party in exercising any right or remedy under this Agreement shall operate as a waiver thereof, nor shall any single or partial exercise of any right or remedy preclude any further exercise thereof or the exercise of any other right or remedy.
>
> [Clause X].3 — Except as expressly provided in this Agreement, the rights and remedies provided under this Agreement are in addition to, and not exclusive of, any rights or remedies provided by law.

**[Pos. 14] Waiver of Civil Code Remedies** — **jurisdiction-dependent; load from the active jurisdiction profile**.

This clause is **only applicable in civil law jurisdictions** where the civil code provides for rescission, annulment, or unilateral modification grounds that the parties wish to waive. The specific grounds, waiver wording, and reservation for non-waivable matters (fraud, duress, public policy) vary by jurisdiction.

For common law jurisdictions (England, most US states, etc.), this position is **not applicable** — rescission and misrepresentation are addressed instead through Pos. 12 (Entire Agreement) and express misrepresentation language.

Apply the wording from the active jurisdiction profile. Reference summary:

| Profile | Key grounds waived |
|---|---|
| Netherlands (NL) | ontbinding, vernietiging on dwaling grounds (Section 6:265, 6:228 BW) |
| Hungary (HU) | tévedés (Section 6:90), feltűnő értékkülönbség (Section 6:98) |
| Italy (IT) | errore (Art. 1428 c.c.), eccessiva onerosità sopravvenuta (Art. 1467) |
| Poland (PL) | błąd (Art. 84 KC), wyzysk (Art. 388 KC) |
| England (EN) | Not applicable — use entire-agreement-based misrepresentation exclusion instead |

**[Pos. 15] Severability**

> If any provision of this Agreement is held to be invalid, illegal or unenforceable, it shall be modified to the minimum extent necessary to make it valid, legal and enforceable and, to the extent legally possible, to have the same economic effect as the Parties originally intended. If such modification is not possible, the relevant provision shall be deemed deleted. Any modification or deletion under this Clause shall not affect the validity and enforceability of the rest of this Agreement.

**[Pos. 16] Counterparts and Electronic Execution**

> This Agreement may be executed in any number of counterparts, each of which when executed shall constitute an original, but all the counterparts shall together constitute one and the same agreement. Subject to applicable law, this Agreement may be executed by way of electronic signature.

**[Pos. 17] Third Party Rights** — **jurisdiction-dependent; load from the active jurisdiction profile**.

Universal first sentence (applies regardless of jurisdiction):

> No one other than a party to this Agreement, their successors and permitted assignees shall have any right to enforce any of its terms.

Jurisdiction-dependent local exclusion (apply from the active profile):

> [Local third-party-beneficiary doctrine exclusion. See profile.]

Reference summary:

| Profile | Local exclusion |
|---|---|
| Netherlands (NL) | *derdenbeding* exclusion, Section 6:253 BW |
| England (EN) | Contracts (Rights of Third Parties) Act 1999 exclusion |
| Hungary (HU) | Third-party beneficiary contract (Sections 6:136–6:137 HCC) exclusion |
| Italy (IT) | *Contratto a favore di terzo* exclusion, Art. 1411 c.c. |
| Poland (PL) | *Umowa na rzecz osoby trzeciej* exclusion, Art. 393 KC |

**[Pos. 20] Language (English under non-English governing law)**

> The language of this Agreement is English and all notices, demands, requests, statements, certificates or other documents or communications shall be in English unless otherwise agreed by the Parties or otherwise required by applicable law.

**[Pos. 21] GDPR / Data Processing** — include as a Schedule for any agreement involving cross-border or systematic personal data exchange. Adapt from the Company's standard NDA or DPA template (not shipped with this skill — most in-house teams have their own GDPR/DPA addendum). Default scope: data minimisation, security measures, sub-processor notification, audit rights, breach notification within 72 hours, return/destruction on termination.

**[Pos. 22] Governing Law and Jurisdiction** — **jurisdiction-dependent; load from the active jurisdiction profile** (see "Starter Jurisdiction Profiles" section).

The Pos. 22 clause has two paragraphs:
- [Clause X].1 — governing law statement
- [Clause X].2 — forum / jurisdiction / arbitration

For each starter jurisdiction, the full Pos. 22 wording is set out in the corresponding profile. For custom jurisdiction profiles, the deployer supplies the wording. Reference summary of the starter set defaults:

| Profile | Governing law | Default forum |
|---|---|---|
| Netherlands (NL) | Laws of the Netherlands | Amsterdam courts |
| England & Wales (EN) | English law | English courts (or LCIA arbitration) |
| Hungary (HU) | Substantive laws of Hungary | HCCI arbitration, Budapest |
| Italy (IT) | Laws of Italy | Milan/Rome courts (or ICC arbitration) |
| Poland (PL) | Laws of Poland | Warsaw courts (or PCC arbitration) |

See "Starter Jurisdiction Profiles" section for the full clause wording for each. If the user has indicated a jurisdiction without a starter profile and no custom profile is supplied, apply the protocol in "Jurisdiction Architecture" → "What to do when no profile is available".



### Optional boilerplate (include when relevant — decision tree)

| Clause | When to include |
|--------|----------------|
| **Confidentiality** | Every transactional agreement. For standalone NDA, use the NDA template instead. |
| **Language** | When governing law language differs from drafting language, or multi-language execution. |
| **Sanctions** | Counterparties with non-EU/non-US beneficial ownership or operations in sanctioned jurisdictions. |
| **Anti-bribery / Anti-corruption** | Elevated corruption risk jurisdictions or government-related counterparties. |
| **Guarantee** | When a parent or other entity guarantees a party's obligations. |
| **Payments** | Any agreement with payment obligations (SPAs, JDAs, loan agreements, service agreements). |
| **Waiver of Local Civil Code Remedies** | All civil law jurisdiction governed agreements (NL, IT, HU, PL, DE, FR, ES, etc.). Not applicable in common law jurisdictions. |
| **No Partnership** | JDAs, cooperation agreements, framework agreements — any agreement where parties collaborate. |
| **Good Faith** | JDAs, cooperation agreements, long-term framework agreements. |
| **GDPR / Data Processing** | Any agreement where personal data is exchanged between the parties. |

---

## Cover Page Specification — Table-Based (Track A only)

Cover pages apply only to Track A full-form agreements. Tracks B, C, D, E, F, G do not use cover pages. When used, the Track A cover page is built on a borderless table for precise alignment:

**Row structure:**
- Rows 1–3: empty spacer rows (push content down ~30% of page)
- Row 4: single merged cell containing stacked party blocks:
  - `[PARTY NAME]` (bold) + line break + `as [Role]`
  - `and` between each party
- Row 5: horizontal rule (top border on cell)
- Row 6: centred title block — `[TITLE OF AGREEMENT]` (14pt bold caps) + subtitle
- Row 7: horizontal rule (bottom border on cell)
- Row 8: `Dated [                    ]` at bottom

All table borders: none. Cell margins: minimal.

---

## Drafting Workflow (Tracks A, B, and E — MC-based documents)

The workflow in this section applies to Track A (transactional agreements), Track B (corporate documents), and Track E (employment contracts) — i.e., all documents built on the MC template with the Company boilerplate library and the Company's precedent repository.

**For other tracks, simplified workflows apply** for *drafting from scratch* — but **Step 1 (uploaded documents handling, including the reformatting scenario) and Step 0 (jurisdiction identification) apply to ALL tracks A through G:**
- **Track C (Litigation):** take the client's case position from the user or uploaded documents; draft per jurisdiction-specific court conventions; do not search the document repository for "precedents" in the transactional sense. Step 1 reformatting applies.
- **Track D (Memo):** take the legal question from the user; research as required; structure per the memo format; no precedent search needed. Step 1 reformatting applies.
- **Track E (Employment):** follow the same workflow as Track A/B — employment contracts are agreements and benefit from the jurisdiction-first, precedent-based approach. Search the document repository for employment contract templates in the Company's jurisdiction; if no template is found, draft from first principles applying the labour law of the jurisdiction set in the active profile. Note: employment law is highly jurisdiction-specific and frequently divergent from general civil/commercial law; flag to the user if no local template or profile-level employment defaults are available.
- **Track F (Policy):** if the Company has existing policies on the document repository in `[document repository: policies folder]`, search for the current version. Otherwise draft from first principles using the Track F structural rules. Step 1 reformatting applies.
- **Track G (Letter):** no precedent-search workflow — draft directly in the letter format. Step 1 reformatting applies (a user can upload an existing letter and ask Claude to reformat it under Track G conventions).

### Step 0: Identify jurisdiction and load the jurisdiction profile

**The user must indicate the governing law jurisdiction; Claude applies the corresponding profile.** This step comes before any drafting, because nearly every substantive decision (clause wording, execution formalities, default forum, language, litigation conventions) depends on it.

Substeps:

1. **Identify the jurisdiction** from one of:
   - Explicit user instruction ("draft a Dutch law SPA", "this is governed by English law", "Italian-law cooperation agreement")
   - Context already in the conversation (counterparty location, project location, prior turn established the jurisdiction)
   - Standing Company convention if the deployment has a default jurisdiction (e.g., a Dutch-incorporated holding company defaults to Dutch law for intragroup documents)

2. **If jurisdiction is unclear and material to the document**, ask the user explicitly before drafting. Examples of when to ask:
   - "What is the governing law and forum for this SPA?"
   - "Is this Italian-law or English-law governed?"
   - "Will the loan be governed by Dutch or English law?"

   Do NOT default silently to a jurisdiction. The wrong governing law selection can produce a document that is technically formed but legally defective or unenforceable.

3. **Load the corresponding jurisdiction profile**:
   - **Built-in profiles**: Netherlands (NL), England & Wales (EN), Hungary (HU), Italy (IT), Poland (PL) — see "Starter Jurisdiction Profiles" section
   - **Custom profile**: if the deployer has supplied a profile for the requested jurisdiction (e.g., Germany, France, Spain, Romania), load and apply it
   - **No profile available**: ask the user whether to (a) supply a profile, (b) proceed with universal MC structure leaving jurisdiction-specific clauses as `[TO BE COMPLETED — local counsel input required]`, or (c) use a "neighbouring" starter profile as starting point with adjustments flagged

4. **Identify other Step 0 inputs** that flow from the profile:
   - **Default forum** for dispute resolution (courts of [city] or arbitration with [institution]) — from profile, confirm with user if alternatives apply
   - **Primary drafting language** — usually English (en-GB) but profile may indicate otherwise (e.g., Italian court filings in Italian)
   - **Market expectations** — what counts as "reasonable market practice" in this jurisdiction
   - **Sector-specific regulatory layer** — if the profile has FDI screening, energy regulator, or other sector awareness, flag it

5. **Confirm to the user (briefly) which profile is being applied** before proceeding, especially if the inference was non-trivial. Example: *"I'll draft this as a Dutch-law SPA, applying the Netherlands jurisdiction profile (Amsterdam courts, wettelijke handelsrente, ontbinding/vernietiging waiver, derdenbeding exclusion). Let me know if any of these should be different."*

This is the single most important step in the workflow. Getting jurisdiction wrong cascades through every subsequent decision.

### Step 1: Read any user-uploaded documents

If the user has uploaded documents alongside the drafting request, **read them first** — before searching the precedent repository. Uploaded documents take priority as the user's stated starting point.

**Default formatting rule (per Critical Rule #5): when the user uploads a precedent of the same document type, preserve its formatting for the new document.** Do not reformat to the MC template or any other track's conventions unless the user explicitly asks for it. Flag technical defects (manual numbering, broken cross-references, misaligned indents, inconsistent styles) and ask whether to correct them — do not fix unilaterally.

Common scenarios:

- **Term sheet / heads of terms uploaded** → extract all agreed commercial terms, party details, project description, and key conditions. Draft the full agreement implementing these terms, filling gaps with Company-favourable provisions. Format: Track A from scratch (no precedent supplied for formatting).
- **Counterparty's draft uploaded** → read it in full, identify the counterparty's position on each substantive point, then draft the Company's version from the Company's strongest position — not by editing the counterparty's draft but by producing a fresh Company document. Format: Track A from scratch (the counterparty's draft is their format, not a precedent for the Company's document). Note in chat where the Company's position materially departs from the counterparty's draft.
- **Existing agreement uploaded for amendment** → read the original in full, identify the provisions to be amended, and draft the amendment agreement referencing the original by date, parties, and title. Preserve the original's defined terms and cross-reference conventions. Format: **the Amendment is a new document** — apply Track A from scratch unless the user also uploads a prior Amendment as precedent, in which case preserve that Amendment's format per Rule #5.
- **Prior document of same type uploaded as precedent** (e.g., a previous Amendment, NDA, loan agreement from another project used as starting point) → **preserve its format per Rule #5**. Content, clause ordering, and structure drawn from the precedent. Flag any technical defects but do not unilaterally fix.
- **Comparable deal / precedent uploaded** → treat as a structural reference for the new document. If the user is drafting a new document of the same type, preserve the precedent's format per Rule #5. If the user is drafting a different document type and just wants to borrow concepts, apply the applicable Track from scratch.
- **Meeting notes / instructions uploaded** → extract all action items, agreed positions, and open points. Draft implementing the agreed positions and flagging open points as bracketed text. Format: follow whatever other document is being produced, or Track A/D as applicable.
- **Document uploaded for reformatting (explicit reformatting request)** → the user wants this document reformatted under the skill's house style. This is the **express opt-out from Rule #5 preservation** under any of the following triggers: explicit instruction ("reformat this", "apply the skill formatting", "format per the house style", "clean up the formatting", "reformat in MC/Track A/Track F style", "make this conform to the house style", or equivalent in any language). **This scenario applies to ALL tracks (A through G)** — not just MC-based tracks. If the document is a court filing (Track C), policy (Track F), memo (Track D), or letter (Track G), the same protocol applies using the relevant Track's structural rules and numbering configurations (e.g., `memoria-sections` for Track C, `policy-sections` for Track F, `memo-sections` for Track D, `letter-items` for Track G). When triggered:
  1. Identify the document type and select the applicable Track per the Track selection decision tree. If ambiguous, ask the user (e.g., uploaded letter could be Track G or Track A side letter — apply the test in the Track G section).
  2. Identify the governing law jurisdiction (per Critical Rule #1). If not stated and not inferable from the document, ask before proceeding — many formatting decisions (language, Pos. 1.7 caveat, Pos. 22 wording, civil-code waivers) are jurisdiction-dependent.
  3. **Preserve all substantive content** — defined terms, commercial figures, party details, dates, clause text, schedules. Reformatting changes form, not substance.
  4. **Apply the full applicable Track**: Layer 1 typography (TNR, A4, 1" margins, footer, smart quotes, body size per track), Layer 2 structural conventions (preamble, recitals, body clauses, signature blocks per track), Layer 3 jurisdiction profile, and **automatic numbering per the Numbering Architecture** (Critical Rule #7) — converting any manually-typed numbers (`"1. "`, `"(a) "`) to automatic numbering via the appropriate chain (numId=4 preamble, numId=6 body) or docx-js numbering config (Tracks C/D/F/G).
  5. **Apply the defined terms convention** (Critical Rule #8) — first use in bold within curly double quotes; subsequent uses capitalised plain.
  6. **Wrap signature blocks in atomic borderless tables** (Critical Rule #9) — `<w:cantSplit/>` or `cantSplit: true`.
  7. **Verify Company entity details** if any appear with full legal details (Critical Rule #6 — search the document repository for the commercial register extract before writing them).
  8. **In the chat summary**: list every formatting change applied (with clause/section reference for any substantive change to numbering or cross-references), flag any defects that required user judgment (e.g., orphan cross-references, ambiguous defined-term introductions), and confirm that no substantive content was changed.
  
  This scenario does NOT apply when the user uploads a document and asks for substantive edits only (markup, redlining, tracked changes) — that remains under Rule #5 preservation. Reformatting is a **distinct, deliberate operation** that the user must explicitly request.

If no documents are uploaded, proceed to Step 2.

### Step 2: Search the document repository for precedents

Search the Company's precedent repository (typically a SharePoint Legal Library, Google Drive, document management system, or similar) for relevant precedents. This is mandatory even when the user has uploaded documents — the library may contain a standard template that should govern the structure. If repository search tools are unavailable, flag this to the user and proceed with uploaded documents, project files, and the boilerplate library.

1. **Search** using `sharepoint_search` or `sharepoint_folder_search` in `[document repository root]`. Search by document type and, if relevant, by jurisdiction or counterparty.

2. **Apply the precedent hierarchy**:
   - **Standard template** (highest priority) — files with "Template" or "Standard" in the name. **Use as the structural drafting base.**
   - **Execution copy** — files with "execution_copy" or "execution copy" in the name. **Contain counterparty concessions that weaken the Company's position.** Never use as a drafting base. Use only as a structural reference.
   - **Executed / signed** — same principle: **reflect the negotiated outcome, not the Company's preferred starting position.** Never use as a drafting base. Use only as reference.
   - **Drafts and markups** — lowest priority. Useful for understanding negotiation history only.

3. **Read the best precedent** to extract structure, clause ordering, defined terms, and boilerplate patterns.

### Step 3: Draft from the Company's strongest position

Combine the inputs (uploaded documents + repository precedents + boilerplate library + **the active jurisdiction profile loaded in Step 0**) and draft from the Company's strongest position for the identified jurisdiction. The template provides the structure; the substance must reflect the Company's preferred position calibrated to local market practice as set out in the jurisdiction profile.

**Apply the jurisdiction profile to:**
- Boilerplate clauses with jurisdiction-dependent variants (Pos. 1.X local concept caveat, Pos. 7 payments interest, Pos. 10 good faith, Pos. 14 rescission waiver, Pos. 17 third party rights, Pos. 22 governing law)
- Execution formalities (notarization, witnessing, registration requirements)
- Default forum for dispute resolution
- Primary drafting language
- Regulatory awareness (FDI screening, sector regulators, registration formalities)
- Track C litigation conventions (if drafting court filings)

The detailed content of each starter profile is set out in the "Starter Jurisdiction Profiles" section toward the end of this skill. For custom profiles supplied by the deployer, apply the values stated in the profile.

Execution copies and executed agreements inform what concessions were made in past deals, but the new draft starts from the Company's strongest reasonable position and lets the counterparty negotiate from there.

### Step 4: If no precedent is found

Draft from the boilerplate library and first principles, applying the Company's standard clause ordering and protective drafting orientation. Flag to the user that no precedent was found in the document repository.

### How to produce documents — by environment

**MC-based tracks (A, B, E)** — transactional agreements, corporate documents, and employment contracts are all produced on the MC template. Use the MC workflow below (Environments 1, 2, 3).

**Non-MC tracks (C, D, F, G)** — litigation, memo, policy, letter are NOT produced on the MC template. They use Word's native styles and a simpler docx creation workflow. For these tracks:
1. Read the `docx` skill at `/mnt/skills/public/docx/SKILL.md`
2. Use its standard document creation workflow with the track-specific structural rules from the Track sections above
3. Apply Layer 1 universal typography (with any track-specific overrides, e.g., Track C uses 12pt)
4. Apply automatic numbering via docx-js numbering configs (see "Automatic Numbering for Non-MC Tracks" section): Track C uses `memoria-sections` and `memoria-docs`; Track D uses `memo-sections`; Track F uses `policy-sections` linked to Heading 1/Heading 2; Track G uses `letter-items` only if needed. Never type numbers by hand.

**Environment 1 (MC-based tracks A, B, E): Claude.ai Chat / Cowork (with MC template in project files)**

Use the unpack → edit XML → repack workflow with the MC template as base:
1. Copy the template: `cp /mnt/project/inhouse-mc-template.docx /home/claude/doc.docx`
2. Unpack: `python scripts/office/unpack.py doc.docx unpacked/`
3. Replace `unpacked/word/document.xml` with new content using MC style names (see mapping below)
4. Repack: `python scripts/office/pack.py unpacked/ output.docx --original doc.docx`

This produces documents with native Word styles that auto-number when paragraphs are added or deleted.

**Environment 2 (MC-based tracks A, B, E): Claude.ai Chat / Cowork (MC template NOT available)**

Read the `docx` skill first (`/mnt/skills/public/docx/SKILL.md`). Use its standard document creation workflow with these specific requirements:
- Configure a multi-level numbering list with 6 levels matching the numbering scheme in this skill: `1.` → `1.1` → `(a)` → `(i)` → `(A)` → `(1)`
- Set restart rules: each level restarts when a higher level increments
- Assign clause headings to Level 0 (bold, ALL CAPS), sub-clauses to Level 1, paragraphs to Level 2, etc.
- Use un-numbered body text paragraphs (no numbering reference) for: preamble, recitals, definitions, execution block, notices/addresses
- **Never use `Heading 2` for sub-clauses** — Heading 2 appears in the TOC. Sub-clauses use numbered body text at Level 1
- **Never use `ListParagraph`** for enumerated paragraphs — it produces bullet lists, not (a)/(b)/(c) numbering
- docx-js generates native Word multi-level lists — they auto-renumber in Word when paragraphs are added or deleted, just like MC template numbering. The MC template is still preferred for Track A/B/E because it carries the full firm styleset, but docx-js numbering is not static.

**Environment 3 (MC-based tracks A, B, E): Claude for Word**

Claude for Word cannot run scripts or access template files. It can only apply styles that exist in the current document. Therefore:
- **Always instruct the user to open the Company template first**, then ask Claude for Word to draft content within it. This gives Claude for Word access to the MC styles (`ClauseL1`, `ClauseL2`, `PreambleL2`, `PreambleL4`, `ScheduleL1`, `BodyText`, `DefinitionsL1`, `NormalBold`, etc., as defined in the Numbering Scheme section)
- If the user asks Claude for Word to draft from a blank document, **stop and refuse**. Blank documents produce typed manual numbering which violates Critical Rule #7 (all numbering must be automatic). Instead, instruct the user to open the Company template (or an existing Company document with the right styles) and retry. The only exception is Track C/D/F/G documents where Claude for Word can apply Word's native multi-level list styles to achieve automatic numbering — but this requires configuring a multi-level list inside Word, which is cleaner in docx-js (Environments 1/2).

### MC Style name mapping (for XML editing)

| Purpose | MC style (`pStyle val`) | Produces | numPr override |
|---------|------------------------|----------|----------------|
| Clause heading | `ClauseL1` | `1.` bold caps | **Required:** ilvl=0 numId=6 |
| Sub-clause | `ClauseL2` | `1.1` | **Required:** ilvl=1 numId=6 |
| Paragraph | `ClauseL3` | `(a)` | **Required:** ilvl=2 numId=6 |
| Sub-paragraph | `ClauseL4` | `(i)` | **Required:** ilvl=3 numId=6 |
| Deep enum | `ClauseL5` | `(A)` | **Required:** ilvl=4 numId=6 |
| Deepest | `ClauseL6` | `(1)` | **Required:** ilvl=5 numId=6 |
| Preamble party | `PreambleL2` | `(1)` `(2)` | **Required:** ilvl=1 numId=4 |
| Recital | `PreambleL4` | `(A)` `(B)` | **Required:** ilvl=3 numId=4 |
| Schedule clause | `ScheduleL1` | `1.` | Style-level numPr sufficient |
| Schedule sub | `ScheduleL2` | `1.1` | Style-level numPr sufficient |
| Schedule para | `ScheduleL3` | `(a)` | Style-level numPr sufficient |
| Body text (flush left) | `BodyText` | No number | None |
| Body text (clause indent) | `BodyText1` | No number, indented | None |
| Body text (para indent) | `BodyText2` | No number, deeper indent | None |
| Definition entry | `DefinitionsL1` | Hanging indent | None |
| Bold label | `NormalBold` | Bold, no number | None |

### What goes where — section-by-section style assignments (Tracks A, B, and E)

The style assignments in this section apply to Tracks A (transactional agreements), B (corporate documents), and E (employment contracts) — where the MC template is the base. For Tracks C, D, F, G, use the track-specific structural rules in the Track sections above with Word's native styles.

**Preamble** (before "IT IS AGREED"):
- Title → `NormalBold` (centred)
- Opening line ("This agreement...") → `BodyText`
- "BETWEEN" → `NormalBold`
- Party descriptions → `PreambleL2` style with explicit `<w:numPr><w:ilvl w:val="1"/><w:numId w:val="4"/></w:numPr>`. This produces automatic (1), (2), (3) numbering.
- "hereinafter..." line → `BodyText`
- "WHEREAS:" → `NormalBold`
- Recitals → `PreambleL4` style with explicit `<w:numPr><w:ilvl w:val="3"/><w:numId w:val="4"/></w:numPr>`. This produces automatic (A), (B), (C) numbering.
- "IT IS AGREED as follows" → `NormalBold`

**CRITICAL — Paragraph-level numPr overrides for body clauses:**

The MC style engine uses separate numId values at the style level (`ClauseL1` → numId=34, `ClauseL2` → numId=5). These are on **different numbering chains**, so sub-clauses will NOT restart per clause unless overridden at the paragraph level.

**Every `ClauseL1`, `ClauseL2`, `ClauseL3`, and `ClauseL4` paragraph MUST include an explicit `<w:numPr>` block pointing to numId=6** (the MC master numbering instance). This puts all body clause levels on the same chain so sub-clauses restart when a new clause heading appears.

```xml
<!-- Clause heading — ilvl=0, numId=6 -->
<w:p><w:pPr><w:pStyle w:val="ClauseL1"/>
  <w:numPr><w:ilvl w:val="0"/><w:numId w:val="6"/></w:numPr>
</w:pPr><w:r><w:t>Interpretation</w:t></w:r></w:p>

<!-- Sub-clause — ilvl=1, numId=6 -->
<w:p><w:pPr><w:pStyle w:val="ClauseL2"/>
  <w:numPr><w:ilvl w:val="1"/><w:numId w:val="6"/></w:numPr>
</w:pPr><w:r><w:t>Sub-clause text.</w:t></w:r></w:p>

<!-- Paragraph — ilvl=2, numId=6 -->
<w:p><w:pPr><w:pStyle w:val="ClauseL3"/>
  <w:numPr><w:ilvl w:val="2"/><w:numId w:val="6"/></w:numPr>
</w:pPr><w:r><w:t>paragraph text;</w:t></w:r></w:p>

<!-- Sub-paragraph — ilvl=3, numId=6 -->
<w:p><w:pPr><w:pStyle w:val="ClauseL4"/>
  <w:numPr><w:ilvl w:val="3"/><w:numId w:val="6"/></w:numPr>
</w:pPr><w:r><w:t>sub-paragraph text;</w:t></w:r></w:p>
```

Without these overrides, sub-clauses number continuously (1.1, 1.2, ... 1.30) across all clauses instead of restarting (2.1, 3.1, etc.).

**Clause 1: Interpretation**:
- "Interpretation" heading → `ClauseL1` + numPr ilvl=0 numId=6
- "Definitions" sub-heading → `ClauseL2` + numPr ilvl=1 numId=6
- Intro line "In this Agreement..." → `BodyText1` (continuation, no number)
- Definitions table or `DefinitionsL1` entries → **no numPr, no numbered styles on table cells**
- "Interpretation" sub-heading → `ClauseL2` + numPr ilvl=1 numId=6
- Construction rules → `ClauseL3` + numPr ilvl=2 numId=6

**Operative and boilerplate clauses**:
- Each clause heading → `ClauseL1` + numPr ilvl=0 numId=6
- Each sub-clause → `ClauseL2` + numPr ilvl=1 numId=6
- Each enumerated paragraph → `ClauseL3` + numPr ilvl=2 numId=6
- Each sub-paragraph → `ClauseL4` + numPr ilvl=3 numId=6
- Continuation text (un-numbered prose following a numbered paragraph) → `BodyText1`

**Execution block**:
- "IN WITNESS WHEREOF..." → `BodyText`
- "For and on behalf of..." → `BodyText` (bold run)
- Signature lines, Name/Title/Date → `BodyText`
- **Do NOT use any numbered style or numPr in the execution block.**

**Schedules and Annexes**:
- Schedule/Annex heading → `NormalBold` (centred)
- Schedule/Annex clauses → `ScheduleL1`, `ScheduleL2`, `ScheduleL3` (independent numbering — these have their own numId chain, separate from numId=6)
- **Do NOT use `ClauseL*` styles in schedules or annexes** — they would continue the body numbering chain.

**Notices section** (contact details):
- Entity name, address lines, email → `BodyText1` (indented, no number)
- **Do NOT use `ClauseL2`** for address blocks.

**Corporate documents** (board resolutions, shareholder resolutions, POAs):
- Title and company name → `NormalBold` (centred)
- "THE UNDERSIGNED:" → `NormalBold`
- Shareholder/entity description → `BodyText` (no numbered style — this is not a multi-party preamble)
- "WHEREAS:" → `NormalBold`
- Recitals (A), (B), (C)... → `PreambleL4` + numPr ilvl=3 numId=4
- "IT IS HEREBY RESOLVED:" → `NormalBold`
- Resolutions (1), (2), (3)... → `PreambleL2` + numPr ilvl=1 numId=4
- Closing text and signature → `BodyText`
- **Do NOT use `ClauseL1`/`ClauseL2` for resolutions** — they produce `1.`/`1.1` clause numbering, not `(1)`/`(2)` resolution numbering.

### Anti-patterns — what NOT to do

These are the specific mistakes that produce broken formatting. Grouped by where they apply.

**Cross-track (wrong track selected):**

| Anti-pattern | Why it fails | Correct approach |
|---|---|---|
| Applying Track A (transactional) to a court filing | Breaks court formatting conventions; MC numbering meaningless in litigation | Use Track C with narrative structure and automatic numbering via `memoria-sections` config |
| Applying Track A to a legal memo or opinion | Memos need heading-based structure with memo header, not clause numbering | Use Track D with memo header and automatic numbering via `memo-sections` config |
| Applying Track A to an internal policy | Policies need heading-based structure | Use Track F with TOC and Heading styles |
| Using `ClauseL*` styles for ordinary correspondence | Letters are prose, not numbered clauses | Use Track G (body prose only) |
| Using 10pt font for Italian litigation | Court standard is 12pt with 1.5 line spacing | Track C overrides Layer 1 typography |
| Building a Track C, D, F, or G document on the MC template | Produces cluttered styles, TOC contamination, wrong defaults | Use a blank Word document for these tracks (Track E does use MC template — it is an agreement) |
| Typing section numbers by hand in Track C, D, F, or G (e.g., `"**1. Section title**"`) | No automatic numbering — manual renumbering required on every edit; breaks TOC in Track F | Configure docx-js numbering config (`memoria-sections`, `memo-sections`, `policy-sections`, `letter-items`) and apply via `numbering.reference` |
| Typing "Doc. 1", "Doc. 2" in a memoria evidence list | No automatic numbering | Use the `memoria-docs` docx-js numbering config |
| Using Heading 1/Heading 2 in Track F without linking to a numbering config | Headings appear un-numbered; TOC has no numbers | Link Heading 1/Heading 2 styles to `policy-sections` numbering config via the `numbering` property in the style definition |

**Within Tracks A, B, and E (MC-based documents):**

| Anti-pattern | Why it fails | Correct approach |
|---|---|---|
| Using `Heading1`/`Heading2` for clause numbering | No numbering linked; appears in TOC at wrong levels | Use `ClauseL1`/`ClauseL2` with numPr numId=6 |
| Using `ListParagraph` for (a)/(b)/(c) | Produces bullets, not letter numbering | Use `ClauseL3` with numPr numId=6 |
| Relying on style-level numPr without paragraph overrides | Sub-clauses number continuously (1.1–1.30) instead of restarting per clause | Add explicit `<w:numPr>` with numId=6 to every numbered paragraph |
| Using `BodyText` with manual (1)/(2) for preamble parties | No auto-numbering; won't update if parties added/removed | Use `PreambleL2` with numPr numId=4 ilvl=1 |
| Using `BodyText` with manual (A)/(B)/(C) for recitals | No auto-numbering | Use `PreambleL4` with numPr numId=4 ilvl=3 |
| Using `ClauseL3` for recitals | Produces lowercase (a); contaminates body numbering chain | Use `PreambleL4` with numPr numId=4 ilvl=3 |
| Applying numbered styles to definition table cells | Definitions get clause numbers | Use `DefinitionsL1` or no pStyle |
| Using `ClauseL*` in schedules | Continues body numbering instead of restarting | Use `ScheduleL*` |
| Using `ClauseL2` for notice addresses | Addresses get sub-clause numbers | Use `BodyText1` |
| Using `ClauseL1`/`ClauseL2` for resolutions in corporate docs | Produces `1.`/`1.1` instead of `(1)`/`(2)` | Use `PreambleL2` with numPr numId=4 ilvl=1 |
| **Using the legacy `Parties` style (or any other orphan custom style) for preamble parties** | The `Parties` style exists in the template stylesheet as a residual style (centred + ALL CAPS run formatting, no numPr). It does NOT auto-number — so parties appear without `(1)`/`(2)` markers. Discovered in v2.1 template-body inspection: the template's own model body example used `Parties` style and produced an unnumbered party block. | Always use `PreambleL2` with paragraph-level `<w:numPr><w:ilvl w:val="1"/><w:numId w:val="4"/></w:numPr>`. The `Parties` style is deprecated — do not reference it in new content. |
| **Using `ClauseL3` for recitals (instead of `PreambleL4`)** | `ClauseL3` is body-clause level 3 — under numId=6 it produces lowercase `(a)/(b)` AND advances the body-clause counter, contaminating subsequent clause numbering. Recitals are part of the preamble chain (numId=4), not the body-clause chain (numId=6). Discovered in v2.1 template-body inspection: recitals appeared as `(a)/(b)` lowercase instead of `(A)/(B)`. | Always use `PreambleL4` with paragraph-level `<w:numPr><w:ilvl w:val="3"/><w:numId w:val="4"/></w:numPr>`. Produces `(A)/(B)/(C)`. |
| **Relying on style-level numPr without paragraph-level override (e.g., `ClauseL1` paragraph with no `<w:numPr>` element)** | Each MC clause style carries an internal style-level numPr pointing to a different numId chain (e.g., `ClauseL1` → numId=34, `ClauseL2` → numId=5, `ClauseL3` → numId=34 with ilvl=2). Without a paragraph-level override pointing to numId=6, the counters run on independent chains and produce nonsense numbering (e.g., a clause heading appearing as "2." or "5." when it should be "1."). Discovered in v2.1 template-body inspection: the first clause heading "INTERPRETATION" rendered as "2." instead of "1." | Every `ClauseL1`/`ClauseL2`/`ClauseL3`/`ClauseL4` paragraph MUST carry an explicit `<w:numPr><w:ilvl w:val="N"/><w:numId w:val="6"/></w:numPr>` element. This unifies all body-clause levels on the single numId=6 chain. See **Numbering Architecture — Three Chains** above. |
| **Numbering chain pollution: using `PreambleL4` (recitals ilvl=3) followed by `PreambleL2` (resolutions/parties ilvl=1) under numId=4** | The recital level-3 counter advances the level-1 counter, causing parties or resolutions to start at (2) or (3) instead of (1). Discovered in v2.1 testing — Dutch sole-shareholder resolution had resolutions numbered (2)-(5) instead of (1)-(4) when WHEREAS recitals preceded them. | **Two safe approaches:** (a) For sole-shareholder resolutions and other corporate docs where recitals are optional, omit auto-numbered recitals and use prose paragraphs (`BodyText`) introduced by a `NormalBold` "WHEREAS:" label. (b) Where auto-numbered recitals are essential, insert a `<w:lvlOverride w:ilvl="1"><w:startOverride w:val="1"/></w:lvlOverride>` element in numbering.xml on a new `<w:num>` that points to the same abstractNum, and reference that new numId for the resolutions/parties block. The override resets the level-1 counter. Document this restart in chat to the user. |

**Precedent handling:**

| Anti-pattern | Why it fails | Correct approach |
|---|---|---|
| Reformatting a precedent to MC styles when user asked to use it as base for a new document of same type | Destroys negotiated form; risks errors in cross-references and defined terms; disrespects counterparty acceptance | Preserve the precedent's format per Rule #5; flag technical defects and ask before fixing |
| Applying Track A from scratch when user uploads a prior Amendment as precedent | Same as above — the prior Amendment IS the template for the new one | Preserve format of the prior Amendment; draft new content within that format |
| Fixing manual numbering, broken hanging indents, or other technical defects in a precedent without asking | Unilaterally changes form the user chose to preserve; may introduce subtle errors | Flag each defect to the user and ask whether to correct; proceed only after user confirms |
| Treating a counterparty's draft as a "precedent to preserve" | Counterparty drafts are their position — the Company drafts from the Company's strongest position in its house style format | Apply Track A from scratch; draft the Company's version, not editing the counterparty's |
| Classifying a letter agreement (mandate letter, indemnity letter, comfort letter) as Track G | Track G is single-level numbering only; letter agreements need multi-level (1./1.1/(a)) clause numbering and MC styles | Apply Track A side letter format — MC styles `ClauseL*` with numId=6 inside letter format with addressee block, "Dear", subject line, countersignature |
| Typing "1.", "1.1", "2.", "2.1" by hand in a Track G letter to fake multi-level numbering | Violates Critical Rule #7; no auto-renumbering; cross-references break; the document is misclassified — multi-level numbering means the document is Track A side letter, not Track G | Reclassify as Track A side letter with proper MC numbering (numId=6) |
| Introducing defined terms without bold and curly quotes on first use (e.g., `(the "Purchase Price")` plain, or `("Purchase Price")` plain, or `"Purchase Price"` without parentheses) | Violates Critical Rule #8; defined terms are not visually identifiable; reader cannot distinguish defined-term first introduction from a stray quoted phrase | First use must be `the "**Purchase Price**"` — bold inside curly double quotes. Subsequent uses are capitalised plain (`the Purchase Price`). Applies to ALL tracks where defined terms are used. |
| Bolding a defined term on every use, not only on first introduction | Visual noise; defeats the purpose of the convention (which is to flag the introduction); inconsistent with international transactional drafting | Bold only on first use. All later references in plain capitalised form. |

---

## Critical Rules

### Universal (apply to every track)

1. **Jurisdiction identification comes before anything else.** Before drafting any document, identify the governing law jurisdiction from explicit user instruction, conversation context, or — if unclear and material — by asking the user explicitly. Load the corresponding jurisdiction profile (starter set: NL, EN, HU, IT, PL; or custom profile supplied by deployer). Apply the profile to every jurisdiction-dependent decision in the document: boilerplate variants (Pos. 1.X, 7, 10, 14, 17, 22), execution formalities, default forum, primary language, regulatory awareness, and Track C litigation conventions. Never silently default to a jurisdiction; never apply starter profile wording to a jurisdiction the user has specified but for which no profile exists — instead, flag and follow the no-profile protocol in "Jurisdiction Architecture".

2. **Track selection comes second.** Identify the document family before drafting. Applying the wrong track produces broken formatting (e.g., MC numbering on a court filing, clause numbering on a policy). If ambiguous, ask the user.

3. **Layer 1 typography governs unless the track overrides.** TNR, A4, 1" margins, en-GB (or document-appropriate language per the active jurisdiction profile), smart quotes, CONFIDENTIAL footer. Body font size varies by track (see "Body size by track" table): Track A uses 10pt (international transactional convention for dense documents); Tracks B, D, E, F, G use 11pt (better readability for corporate, memo, HR, policy, letter); Track C uses 12pt with 1.5 line spacing (court standard).

4. **The Company's interests are primary.** Draft from the Company's perspective as in-house counsel. Default to the most Company-favourable position within reasonable practice for the specific document type and jurisdiction. Preserve asymmetries that benefit the Company. This applies to substance across all tracks — though the expression differs (protective drafting in Track A, robust arguments in Track C, clear authority in Track B, etc.).

5. **Preserve existing formatting by default.** When drafting from a precedent — whether an uploaded document, an executed copy in the document repository, or a prior version of the same document type — match the precedent's existing formatting: fonts, margins, numbering approach, structural conventions, signature block layout. Do NOT impose MC formatting (or any other track's formatting) on a document that was working in a different style. The precedent represents a form that was drafted, negotiated, and often signed — the format is part of that outcome and must not be changed unilaterally.

   This rule applies to:
   - **Editing an existing document** that will be redelivered as-is (e.g., markup on a counterparty draft, tracked-changes review) — preserve the original format exactly, making only the requested edits.
   - **Drafting a new document using a precedent as starting point** (e.g., Amendment No. 2 modelled on Amendment No. 1 from a different project; new NDA based on an executed NDA from last year) — preserve the precedent's format for the new document.

   **Exceptions — when Claude may reformat:**
   - The user explicitly requests it ("reformat in MC style", "apply the skill formatting", "format per the house style", "clean up the formatting", "make this conform to the house style", or equivalent in any language) — see the **Document uploaded for reformatting** scenario in Step 1 of the Drafting Workflow for the full reformatting protocol.
   - The document is a **new document drafted without any precedent** — in which case the applicable Track's format (Track A through G per this skill) governs from scratch.

   **Technical defects in the precedent:** If the precedent has objective defects that compromise functionality — manual numbering that breaks when clauses are added, misaligned hanging indents, broken cross-references, inconsistent styles within the document, non-searchable scanned content — Claude shall **flag the defect to the user and ask whether to correct it**, without unilaterally fixing it. The user decides whether the fix is worth the disruption to the precedent's negotiated form.

   Substantive Company-interest orientation (Rule #4) always applies regardless — preserving format does not mean preserving bad substance.

6. **Verify Company entity details.** Whenever a Company group entity's full legal details appear in any document (preamble, header, signature block, addressee), follow the Entity details verification workflow — search the document repository for the commercial register extract before writing the details.

7. **All numbering must be automatic — when drafting from scratch or a template.** Every number (section headings, sub-clauses, paragraphs, enumerated items, recitals, parties, document lists) in a document drafted from scratch or from a Company template must be auto-generated — either by MC template styles (Tracks A, B, E) or by docx-js numbering configs (Tracks C, D, F, G). NEVER type a leading number like `"1. "`, `"(a) "`, `"(A) "`, or `"Doc. 1"` by hand in a new draft. Manual numbers do not update when content is added, removed, or reordered, and break any cross-references or TOC that depend on them. **When preserving a precedent's format per Rule #5, manual numbering in the precedent is a technical defect to flag — not something Claude unilaterally converts to automatic numbering.**

8. **Defined terms convention.** Whenever a defined term is introduced in any document — agreement, corporate document, court filing, memo, employment contract, policy, or letter — the **first use** of the term shall be in **bold within curly double quotes** (e.g., `the "**Purchase Price**"`, `the "**Indemnified Party**"`, `the "**Run-Off Period**"`). Subsequent uses are capitalised, **no bold, no quotes** (e.g., `the Purchase Price`). This applies regardless of where the term is introduced — preamble, recitals, definitions clause, body of an article, narrative paragraph, memo introduction, or letter opening. The only exception is the rare case where Claude is preserving the format of a precedent that uses a different convention per Rule #5 — and even then, Claude shall flag the inconsistency to the user. This rule applies to ALL tracks. The convention exists so that defined terms are visually identifiable on first introduction and unambiguous thereafter.

   **Implementation patterns:**

   **MC template (XML editing, Tracks A/B/E):** the defined term and its surrounding quotes must be split across multiple `<w:r>` runs so the term run can carry bold formatting while the quote characters remain unbolded:
   ```xml
   <w:r><w:t xml:space="preserve">(the &#x201C;</w:t></w:r>
   <w:r><w:rPr><w:b/></w:rPr><w:t>Purchase Price</w:t></w:r>
   <w:r><w:t>&#x201D;)</w:t></w:r>
   ```
   The curly quote characters (`&#x201C;` and `&#x201D;`) sit in unbolded runs adjacent to the bolded term run.

   **docx-js (Tracks C/D/F/G):** the same logic — split the surrounding text and the bold term into separate `TextRun` instances within the same `Paragraph`:
   ```javascript
   new Paragraph({
     children: [
       new TextRun({ text: "Atlantic Wind Holding B.V. (the \u201C", font: TNR, size: 22 }),
       new TextRun({ text: "Company", font: TNR, size: 22, bold: true }),
       new TextRun({ text: "\u201D) is contemplating...", font: TNR, size: 22 })
     ]
   })
   ```
   Use `\u201C` (left curly double quote) and `\u201D` (right curly double quote), not straight ASCII `"`. **Common defect (observed in v2.1 dummy-doc testing):** writing `(the "Company")` as a single TextRun with straight quotes — this fails the convention on three counts: not bold, not curly, not visually distinguishable from a stray quotation. Always use the three-run pattern above.

9. **Signature block atomicity.** Every signature block — whether for the Company, a counterparty, or a sole shareholder — MUST be rendered so that the "For and on behalf of [ENTITY]" header line and the signature/Name/Title/Date lines remain on the same page. A signature block split across pages (header on page N, name/title on page N+1, or worse, an orphan "Title:" line stranded on the final page) is a serious formatting defect: it suggests post-execution tampering, looks unprofessional, and creates evidentiary risk in any dispute. This rule applies to ALL tracks across all document families.

   **Implementation patterns:**

   **MC template (XML editing, Tracks A/B/E):** wrap each signature block in a **borderless single-row table** with `<w:cantSplit/>` on the row. The table prevents the row from breaking across pages; the "For and on behalf of [ENTITY]" header paragraph preceding the table carries `<w:keepNext/>` so it stays with the table. Example for a dual signature block (Company as counterparty, two signatories side-by-side):

   ```xml
   <w:p>
     <w:pPr><w:pStyle w:val="BodyText"/><w:keepNext/></w:pPr>
     <w:r><w:rPr><w:b/></w:rPr><w:t>For and on behalf of [ENTITY]</w:t></w:r>
   </w:p>
   <w:tbl>
     <w:tblPr>
       <w:tblW w:w="9026" w:type="dxa"/>
       <w:tblBorders>
         <w:top w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:left w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:bottom w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:right w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:insideH w:val="none" w:sz="0" w:space="0" w:color="auto"/>
         <w:insideV w:val="none" w:sz="0" w:space="0" w:color="auto"/>
       </w:tblBorders>
       <w:tblLayout w:type="fixed"/>
     </w:tblPr>
     <w:tblGrid><w:gridCol w:w="4513"/><w:gridCol w:w="4513"/></w:tblGrid>
     <w:tr>
       <w:trPr><w:cantSplit/></w:trPr>
       <w:tc><w:tcPr><w:tcW w:w="4513" w:type="dxa"/></w:tcPr>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>____________________________________</w:t></w:r></w:p>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>Name:</w:t></w:r></w:p>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>Title:</w:t></w:r></w:p>
         <w:p><w:pPr><w:pStyle w:val="BodyText"/></w:pPr><w:r><w:t>Date:</w:t></w:r></w:p>
       </w:tc>
       <w:tc><w:tcPr><w:tcW w:w="4513" w:type="dxa"/></w:tcPr>
         <!-- second signatory column: identical structure -->
       </w:tc>
     </w:tr>
   </w:tbl>
   ```

   For a single signature block (counterparty signing through one representative), use a 1-column table with the same `cantSplit` row.

   **docx-js (Tracks C/D/F/G):** wrap the author block, sign-off block, or signature block in a `Table` with a single `TableRow` having `cantSplit: true`. Borders on all cells set to `BorderStyle.NONE`. Example for a memo author block:

   ```javascript
   new Table({
     width: { size: 4513, type: WidthType.DXA },
     borders: {
       top:    { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
       bottom: { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
       left:   { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
       right:  { style: BorderStyle.NONE, size: 0, color: "FFFFFF" },
     },
     rows: [
       new TableRow({
         cantSplit: true,  // critical: prevents row split across pages
         children: [
           new TableCell({
             width: { size: 4513, type: WidthType.DXA },
             borders: NO_BORDERS,
             children: [
               new Paragraph({ children: [new TextRun({ text: "_____________________", font: TNR, size: 22 })] }),
               new Paragraph({ children: [new TextRun({ text: "[Author Name]", font: TNR, size: 22, bold: true })] }),
               new Paragraph({ children: [new TextRun({ text: "[Title]", font: TNR, size: 22 })] }),
             ]
           })
         ]
       })
     ]
   })
   ```

   **Why a table and not just `<w:keepNext/>` on each paragraph?** `keepNext` works for short blocks but Word's renderer can occasionally still break the chain when a long paragraph precedes the signature block and the remaining page space is awkward. The `cantSplit` table row is a **hard constraint** — it cannot break across pages regardless of what precedes it. For the most important and visually sensitive part of a legal document, hard constraints are non-negotiable.

   **Common defect (observed in v2.1 dummy-doc testing):** the Dutch Board Resolution test produced a page 2 containing only an orphan `Title: Managing Director A    Title: Managing Director B` line, with the rest of the signature block (For-and-on-behalf-of header, signature line, Name) stranded on page 1. The fix was to wrap the dual signature block in a `cantSplit` table as described above. After the fix, the entire block sits atomically on page 2.

### Tracks A, B, and E (MC-based documents) only

10. **Follow the MC drafting workflow.** Jurisdiction first → read uploaded documents → search the document repository for precedents → draft from the Company's strongest position. Never ignore an uploaded document.

11. **Precedent hierarchy: template > execution copy > executed.** Standard templates are the drafting base. Execution copies and executed agreements contain counterparty concessions — use only as structural references.

12. **Use the MC template as the drafting base.** For Tracks A, B, and E, start from `inhouse-mc-template.docx`, apply the unpack → edit XML → repack workflow, use MC styles (`ClauseL*`, `PreambleL*`, `ScheduleL*`) with explicit numPr overrides (see Numbering Architecture).

13. **Two Company signature blocks where the Company signs as a party.** Applies to Tracks A, B, and E (employer side). Counterparty blocks per counterparty requirements.



### Track A only

14. **Use locked boilerplate.** Adapt only clause numbering, cross-references, and defined terms. Do not redraft boilerplate from scratch.

15. **Definitions in body, not in Schedules.** Definitions belong in Clause 1 (Interpretation). Schedules are for substantive annexes only.

### Track C (Litigation) only

16. **Never apply MC styles. Never type numbers by hand.** Track C documents are not built on the MC template. Use docx-js automatic numbering configs (`memoria-sections` for section headings, `memoria-docs` for the evidence list) with bold 12pt formatting and 1.5 line spacing. Court-specific formulas from the active jurisdiction profile (e.g., for Italy: TRIBUNALE, CONCLUSIONI, R.G., ex art.; for Germany: LANDGERICHT, KLAGEANTRAG, ZPO references; for England: claim form headings, particulars of claim conventions) take precedence over MC conventions.

17. **Draft the substance per the client's legal position in the case**, not the Company's "strongest reasonable position" framework. The client's position is set by the procedural posture and facts of the case.

### Tracks D, F, G (Memo, Policy, Letter) only

18. **Never use MC template styles.** Tracks D, F, and G are built on blank Word documents with Word's native styles. Do NOT use `ClauseL*`, `PreambleL*`, or `ScheduleL*`.

19. **Automatic numbering by track:** Track D uses `memo-sections` docx-js numbering config (two-level: 1., 1.1). Track F links Heading 1/Heading 2 to `policy-sections` config (two-level: 1., 1.1). Track G uses `letter-items` only if operative paragraphs are needed. NEVER type numbers by hand in any track — automatic numbering is required universally.

20. **Apply track-specific signature conventions.** Track D (memos): author's name and title, no signature block. Track F (policies): approval block (Approved by Board/CEO), no bilateral signature. Track G (letters): single signature unless dual legally required.

---

## Starter Jurisdiction Profiles

This section sets out the five starter jurisdiction profiles. Each profile is a structured set of values that Claude applies whenever the corresponding jurisdiction is the active jurisdiction (selected in Step 0 of the drafting workflow).

The profiles are **reference implementations**, not constraints — the architecture supports any additional jurisdiction profile supplied by the deployer (see "Adding a Jurisdiction Profile" below).

---

### Profile: Netherlands (NL)

| Slot | Value |
|---|---|
| **Code / language** | NL / en-GB (Dutch document drafting almost always in English; Dutch terms italicised inline where defined concepts) |
| **Default forum** | Competent courts of Amsterdam, the Netherlands (or NAI arbitration on request) |
| **Default governing law** | Substantive laws of the Netherlands |

**Boilerplate variants:**

**[Pos. 1.7 — Dutch concepts construction rule]**
> English language words used in this Agreement intend to describe Dutch legal concepts only and the consequences of the use of such words in English law or any other foreign law shall be disregarded. Where a Dutch word is included in italics and in brackets after an English word and there is any inconsistency between the Dutch and the English, the meaning of the Dutch word shall prevail.

**[Pos. 7 — Payments interest]**
> If a Party defaults in the payment when due of any sum payable under this Agreement, it shall pay statutory commercial interest (*wettelijke handelsrente*) at the then applicable rate on that sum from the due date until the date of actual payment, which interest shall accrue from day to day and be compounded monthly.

**[Pos. 10 — Good faith]**
> Standard Dutch civil law includes a duty of *redelijkheid en billijkheid* (reasonableness and fairness) which operates as a default. Include an express good faith clause only if the parties wish to extend or specify it beyond the default; otherwise, the statutory duty applies.

**[Pos. 14 — Rescission/annulment waiver]**
> To the extent permitted by law, the Parties hereby waive their rights to terminate, annul, rescind, or nullify, in whole or in part (*gehele dan wel partiële ontbinding en vernietiging*) this Agreement on the ground of error (*dwaling*), or to demand in legal proceedings the rescission (*ontbinding*), nullification (*vernietiging*) or the amendment of this Agreement.

**[Pos. 17 — Third-party rights (derdenbeding exclusion)]**
> No one other than a party to this Agreement, their successors and permitted assignees shall have any right to enforce any of its terms. No stipulation in this Agreement constitutes a third party stipulation (*derdenbeding*) within the meaning of Section 6:253 of the Dutch Civil Code.

**[Pos. 22 — Governing law and jurisdiction]**
> [Clause X].1 — This Agreement and any non-contractual obligations arising out of or in connection with it shall be governed by and construed in accordance with the laws of the Netherlands.
>
> [Clause X].2 — Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity or termination, shall be submitted to the exclusive jurisdiction of the competent courts in Amsterdam, the Netherlands.

**Execution and corporate formalities:**
- Share transfers in a B.V. require a notarial deed before a Dutch civil-law notary
- Board resolutions normally executed by simple writing (no notary), but where required by the AoA, a notary may need to be involved
- Powers of Attorney for cross-border use typically require apostille
- Dutch courts accept electronic signatures for most commercial agreements (eIDAS / Section 3:15a BW)

**Regulatory awareness:**
- Dutch Foreign Direct Investment Act (Wet Vifo) — sectoral screening (defence, dual-use, certain semiconductor)
- ACM (Authority for Consumers and Markets) for competition / consumer matters
- Energy: ACM as regulator; gas/electricity supply licences; environmental permits at provincial/municipal level

---

### Profile: England & Wales (EN)

| Slot | Value |
|---|---|
| **Code / language** | EN / en-GB |
| **Default forum** | English courts (alternative: LCIA arbitration) |
| **Default governing law** | English law |

**Boilerplate variants:**

**[Pos. 1.7 — Construction (not applicable)]**
> Not applicable — English law does not require a "concepts" construction rule when drafting in English.

**[Pos. 7 — Payments interest]**
> If a Party defaults in the payment when due of any sum payable under this Agreement, it shall pay interest on that sum from the due date until the date of actual payment at the rate of [base rate + 4]% per annum, accruing daily and compounded monthly. The Parties acknowledge that this rate represents a genuine pre-estimate of the cost of borrowing and is not a penalty. *[Alternative]: at the rate provided for under the Late Payment of Commercial Debts (Interest) Act 1998.*

**[Pos. 10 — Good faith]**
> *Warning: Under English law, there is no implied duty of good faith in commercial contracts. Including a good faith clause creates a contractual obligation that would not otherwise exist. Use only if the Company commercially intends a good faith standard (typical in JDAs and long-term partnerships); avoid in straight transactional documents where it would extend the Company's obligations.*

**[Pos. 14 — Rescission/annulment waiver (not applicable)]**
> Not applicable — English law has different rescission doctrines. Standard practice is to address misrepresentation and remedies via Pos. 12 (Entire Agreement) which under English law operates to exclude reliance on pre-contractual statements outside the agreement.

**[Pos. 17 — Third-party rights (Contracts (Rights of Third Parties) Act 1999 exclusion)]**
> A person who is not a party to this Agreement shall have no rights under the Contracts (Rights of Third Parties) Act 1999 to enforce any of its terms.

**[Pos. 22 — Governing law and jurisdiction]**
> [Clause X].1 — This Agreement and any non-contractual obligations arising out of or in connection with it shall be governed by and construed in accordance with English law.
>
> [Clause X].2 — The courts of England and Wales shall have exclusive jurisdiction to settle any dispute arising out of or in connection with this Agreement.
>
> *[Alternative — LCIA arbitration]*: Any dispute arising out of or in connection with this Agreement shall be referred to and finally resolved by arbitration under the Rules of the London Court of International Arbitration (LCIA), which Rules are deemed to be incorporated by reference into this clause. The number of arbitrators shall be [one/three]. The seat of arbitration shall be London. The language of the arbitration shall be English.

**Execution and corporate formalities:**
- Most agreements executed by simple signing; deeds require execution as a deed (two directors, or one director + witness, or one director + company secretary)
- Witnessing requirements for deeds: a witness who is not a party must attest
- Electronic signatures accepted for most contracts; deeds may require additional formalities depending on circumstances
- Companies House registration for charges and certain corporate changes

**Regulatory awareness:**
- National Security and Investment Act 2021 (NSI) — mandatory and voluntary FDI notifications
- CMA (Competition and Markets Authority) for competition
- Sector regulators: Ofgem (energy), Ofcom (telecoms), FCA (financial services)

---

### Profile: Hungary (HU)

| Slot | Value |
|---|---|
| **Code / language** | HU / en-GB (cross-border) or hu-HU (domestic) |
| **Default forum** | Commercial Court of Arbitration at the Hungarian Chamber of Commerce and Industry (HCCI) or Budapest courts |
| **Default governing law** | Hungarian law |

**Boilerplate variants:**

**[Pos. 1.7 — Hungarian concepts construction rule]**
> English language words used in this Agreement intend to describe Hungarian legal concepts only and the consequences of the use of such words in English law or any other foreign law shall be disregarded. Where a Hungarian word is included in italics and in brackets after an English word and there is any inconsistency between the Hungarian and the English, the meaning of the Hungarian word shall prevail.

**[Pos. 7 — Payments interest]**
> If a Party defaults in the payment when due of any sum payable under this Agreement, it shall pay default interest at the rate provided under Section 6:155 of the Hungarian Civil Code (i.e., the central bank base rate plus 8 percentage points) from the due date until the date of actual payment, accruing daily and compounded monthly.

**[Pos. 10 — Good faith]**
> The Parties shall act in good faith and fair dealing (*jóhiszeműség és tisztesség*) throughout the term of this Agreement, in accordance with Section 1:3 of the Hungarian Civil Code. *(Statutory default applies whether or not expressly stated.)*

**[Pos. 14 — Rescission/annulment waiver]**
> To the extent permitted by Hungarian law, the Parties hereby waive their rights to challenge, terminate or rescind this Agreement on the grounds of mistake (*tévedés*, Section 6:90 of the Hungarian Civil Code), serious disproportion (*feltűnő értékkülönbség*, Section 6:98), or unilateral mistake of legal qualification. This waiver does not extend to fraud (*megtévesztés*) or other grounds that cannot be waived under Hungarian law.

**[Pos. 17 — Third-party rights]**
> No one other than a party to this Agreement, its successors and permitted assignees shall have any right to enforce any of its terms. This Agreement is not intended to constitute a contract for the benefit of a third party (*harmadik személy javára szóló szerződés*) within the meaning of Sections 6:136–6:137 of the Hungarian Civil Code.

**[Pos. 22 — Governing law and jurisdiction]**
> [Clause X].1 — This Agreement and any dispute or claim arising out of or in connection with it shall be governed by and construed in accordance with the substantive laws of Hungary without the application of any provisions of law pertaining to the conflict of laws.
>
> [Clause X].2 — Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity or termination, shall be finally settled by arbitration under the Rules of the Commercial Court of Arbitration attached to the Hungarian Chamber of Commerce and Industry. The number of arbitrators shall be [one/three]. The seat of arbitration shall be Budapest. The language of the arbitration shall be English.

**Execution and corporate formalities:**
- Kft (Korlátolt felelősségű társaság / Hungarian LLC) quota transfers require a written agreement with notarised signatures, plus registration with the Court of Registration (*Cégbíróság*)
- Zrt (Closed company limited by shares) share transfers by entry in the share register
- Corporate documents executed before a Hungarian notary may need certified translation if drafted in English
- Apostille required for cross-border use of corporate documents

**Regulatory awareness:**
- Hungarian FDI screening (Government Decree 561/2022) — broad scope including energy
- HEPURA (*Magyar Energetikai és Közmű-szabályozási Hivatal*) for energy regulation
- GVH (Hungarian Competition Authority) for competition

---

### Profile: Italy (IT)

| Slot | Value |
|---|---|
| **Code / language** | IT / en-GB (for cross-border transactional) or it-IT (for domestic litigation, corporate, employment) |
| **Default forum** | Competent courts of Milan or Rome, Italy (or ICC arbitration Milan/Paris seat) |
| **Default governing law** | Italian law |

**Boilerplate variants:**

**[Pos. 1.7 — Italian concepts construction rule]**
> English language words used in this Agreement intend to describe Italian legal concepts only and the consequences of the use of such words in English law or any other foreign law shall be disregarded. Where an Italian word is included in italics and in brackets after an English word and there is any inconsistency between the Italian and the English, the meaning of the Italian word shall prevail.

**[Pos. 7 — Payments interest]**
> If a Party defaults in the payment when due of any sum payable under this Agreement, it shall pay default interest (*interessi di mora*) at the rate provided under Legislative Decree no. 231/2002 (the Italian implementation of the EU Late Payments Directive) on commercial transactions, equal to the ECB reference rate plus 8 percentage points, from the due date until the date of actual payment.

**[Pos. 10 — Good faith]**
> The Parties shall perform this Agreement in accordance with the principles of good faith (*buona fede*) and fair dealing (*correttezza*) as set out in Articles 1175 and 1375 of the Italian Civil Code. *(Statutory default applies whether or not expressly stated.)*

**[Pos. 14 — Rescission/annulment waiver]**
> To the extent permitted by Italian law, the Parties hereby waive their rights to terminate, annul, rescind or seek the unilateral modification of this Agreement on the grounds of error (*errore*, Article 1428 et seq. of the Italian Civil Code), serious imbalance arising from unforeseen circumstances (*eccessiva onerosità sopravvenuta*, Article 1467) where the Party affected has expressly accepted the risk, or unilateral mistake of legal qualification. This waiver does not extend to fraud (*dolo*) or duress (*violenza*) or other grounds that cannot be waived under Italian law.

**[Pos. 17 — Third-party rights]**
> No one other than a party to this Agreement, its successors and permitted assignees shall have any right to enforce any of its terms. This Agreement is not intended to constitute a contract for the benefit of a third party (*contratto a favore di terzo*) within the meaning of Article 1411 of the Italian Civil Code.

**[Pos. 22 — Governing law and jurisdiction]**
> [Clause X].1 — This Agreement and any non-contractual obligations arising out of or in connection with it shall be governed by and construed in accordance with the laws of Italy.
>
> [Clause X].2 — Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity or termination, shall be submitted to the exclusive jurisdiction of the competent courts of [Milan/Rome], Italy.
>
> *[Alternative — ICC arbitration]*: Any dispute arising out of or in connection with this Agreement shall be finally settled under the Rules of Arbitration of the International Chamber of Commerce by one or more arbitrators appointed in accordance with the said Rules. The seat of arbitration shall be Milan, Italy. The language of the arbitration shall be English.

**Execution and corporate formalities:**
- SRL (*Società a responsabilità limitata*) quota transfers require a written deed with notarised signatures, registered at the Companies Register (*Registro delle Imprese*) within 30 days
- SpA (joint-stock company) share transfers by entry in the shareholders' book (and dematerialised share entry for listed companies)
- Notarial deed required for certain corporate transactions: capital increases, mergers, demergers, AoA amendments
- Apostille for cross-border use; legalisation for non-Hague Convention countries

**Regulatory awareness:**
- Italian FDI screening — *Golden Power* (Decree-Law 21/2012 and subsequent amendments), broad sectoral coverage including energy, finance, healthcare, technology
- AGCM (Italian Competition Authority) for competition
- ARERA (Italian Regulatory Authority for Energy, Networks and Environment) for energy
- IVASS for insurance; Banca d'Italia / CONSOB for financial services

**Track C (Litigation) — Italian conventions:**
- Court header format: `TRIBUNALE ORDINARIO DI [CITY] / Sezione [N] [Civile/Lavoro] / R.G. n. [number]/[year] – Giudice [dott./dott.ssa Name]`
- Document titles: `MEMORIA INTEGRATIVA`, `COMPARSA CONCLUSIONALE`, `RICORSO`, `MEMORIA DI REPLICA` (14pt bold caps)
- Procedural references: italicised, centred (e.g., `ex art. 426 c.p.c.`, `per l'udienza del [date]`)
- Drafting language: Italian
- Conclusioni block: `CONCLUSIONI` bold centred, followed by formal requests to the court
- Evidence list: numbered `Doc. 1`, `Doc. 2`, etc. via the `memoria-docs` config

---

### Profile: Poland (PL)

| Slot | Value |
|---|---|
| **Code / language** | PL / en-GB (cross-border) or pl-PL (domestic) |
| **Default forum** | Polish courts (typically Warsaw) or Court of Arbitration at the Polish Chamber of Commerce in Warsaw |
| **Default governing law** | Polish law |

**Boilerplate variants:**

**[Pos. 1.7 — Polish concepts construction rule]**
> English language words used in this Agreement intend to describe Polish legal concepts only and the consequences of the use of such words in English law or any other foreign law shall be disregarded. Where a Polish word is included in italics and in brackets after an English word and there is any inconsistency between the Polish and the English, the meaning of the Polish word shall prevail.

**[Pos. 7 — Payments interest]**
> If a Party defaults in the payment when due of any sum payable under this Agreement, it shall pay default interest at the statutory rate for commercial transactions (*odsetki ustawowe za opóźnienie w transakcjach handlowych*) as set out in the Act on counteracting excessive delays in commercial transactions of 8 March 2013, equal to the NBP reference rate plus 10 percentage points, from the due date until the date of actual payment.

**[Pos. 10 — Good faith]**
> The Parties shall perform this Agreement in accordance with the principles of good faith and the social and economic purpose of the right (*zasady współżycia społecznego*) as set out in Article 5 of the Polish Civil Code. *(Statutory default applies whether or not expressly stated.)*

**[Pos. 14 — Rescission/annulment waiver]**
> To the extent permitted by Polish law, the Parties hereby waive their rights to challenge or rescind this Agreement on the grounds of error (*błąd*, Article 84 of the Polish Civil Code) or serious disproportion (*wyzysk*, Article 388). This waiver does not extend to deceit (*podstęp*) or other grounds that cannot be waived under Polish law.

**[Pos. 17 — Third-party rights]**
> No one other than a party to this Agreement, its successors and permitted assignees shall have any right to enforce any of its terms. This Agreement is not intended to constitute a contract for the benefit of a third party (*umowa na rzecz osoby trzeciej*) within the meaning of Article 393 of the Polish Civil Code.

**[Pos. 22 — Governing law and jurisdiction]**
> [Clause X].1 — This Agreement and any non-contractual obligations arising out of or in connection with it shall be governed by and construed in accordance with the laws of Poland.
>
> [Clause X].2 — Any dispute arising out of or in connection with this Agreement, including any question regarding its existence, validity or termination, shall be submitted to the exclusive jurisdiction of the competent courts in Warsaw, Poland.
>
> *[Alternative — arbitration]*: Any dispute arising out of or in connection with this Agreement shall be finally settled by arbitration administered by the Court of Arbitration at the Polish Chamber of Commerce in Warsaw under its Arbitration Rules. The arbitral tribunal shall consist of [one/three] arbitrator(s). The language of the arbitration shall be English.

**Execution and corporate formalities:**
- sp. z o.o. (*spółka z ograniczoną odpowiedzialnością*) share transfers require a written agreement with notarised signatures, registered at the National Court Register (*Krajowy Rejestr Sądowy* / KRS)
- S.A. (joint-stock company) share transfers — different formalities depending on share type (registered vs bearer; dematerialised mandatory for many)
- Notarial deed required for incorporation, AoA amendments, mergers, demergers
- Apostille for cross-border use

**Regulatory awareness:**
- Polish FDI screening — Act on the Control of Certain Investments (2015, amended 2020 for COVID, 2023 expansion) — sectoral coverage including energy, defence, media
- UOKiK (Polish Competition Authority) for competition
- URE (*Urząd Regulacji Energetyki*) for energy regulation
- KNF for financial services

---

## Adding a Jurisdiction Profile

To extend the skill to a jurisdiction not in the starter set, supply a custom profile following the template below. The profile is consumed by Claude in Step 0 of the drafting workflow and applied throughout drafting.

### Profile template

Copy the template below, replace the placeholders with values specific to the new jurisdiction, and provide the completed profile to Claude either (a) as a project file alongside the skill, (b) inline in the conversation when invoking the skill, or (c) as part of a deployment-specific configuration.

```markdown
### Profile: [JURISDICTION NAME] ([ISO CODE])

| Slot | Value |
|---|---|
| **Code / language** | [ISO 3166 code] / [BCP 47 language tag, e.g. en-GB or de-DE] |
| **Default forum** | [Courts of [city], country] OR [Arbitration institution + seat] |
| **Default governing law** | [Full name of jurisdiction's body of law, e.g., "Substantive laws of Germany"] |

**Boilerplate variants:**

**[Pos. 1.7 — [Jurisdiction] concepts construction rule]**
> [Standard rule: English language words used in this Agreement intend to describe [jurisdiction] legal concepts only and the consequences of the use of such words in English law or any other foreign law shall be disregarded. Where a [language] word is included in italics and in brackets after an English word and there is any inconsistency between the [language] and the English, the meaning of the [language] word shall prevail.]
>
> [If not applicable — e.g., English-law profile — state "Not applicable" and explain why]

**[Pos. 7 — Payments interest]**
> [Local statutory commercial interest rate + statutory reference + accrual convention]

**[Pos. 10 — Good faith]**
> [State whether good faith is implicit (civil law) or absent (English common law). If implicit, cite the statutory provision. If express clause is needed, provide the wording.]

**[Pos. 14 — Rescission/annulment waiver]**
> [Local civil code grounds for rescission/annulment + waiver wording. Identify what is waivable vs not. If common law (e.g., English), state "Not applicable" and explain alternative treatment.]

**[Pos. 17 — Third-party rights local exclusion]**
> [Local third-party-beneficiary doctrine exclusion. Cite the relevant statutory provision (e.g., the Contracts (Rights of Third Parties) Act 1999 for English law).]

**[Pos. 22 — Governing law and jurisdiction]**
> [Clause X].1 — [Full text of governing law statement]
>
> [Clause X].2 — [Full text of forum / jurisdiction / arbitration clause]
>
> *[Alternative — [other forum]]*: [optional alternative]

**Execution and corporate formalities:**
- [Share/quota transfer formalities by entity type]
- [Notarisation requirements]
- [Witnessing requirements]
- [Registration requirements at corporate register]
- [Electronic signature acceptance]
- [Apostille / legalisation for cross-border use]

**Regulatory awareness:**
- [FDI / national security screening regime]
- [Competition regulator]
- [Sector regulators relevant to the Company's industry]
- [Tax / payroll / employment authorities if relevant]

**Track C (Litigation) — [Jurisdiction] conventions** *(if applicable — provide only if the deployer drafts litigation for this jurisdiction)*:
- [Court header format with concrete example]
- [Document titles and naming conventions]
- [Procedural reference style]
- [Drafting language]
- [Conclusioni / prayer for relief block conventions]
- [Evidence list naming convention]
```

### Worked example — adding Germany

Below is what a completed Germany profile would look like (illustrative; verify with local counsel before deployment):

```markdown
### Profile: Germany (DE)

| Slot | Value |
|---|---|
| **Code / language** | DE / en-GB (or de-DE) |
| **Default forum** | Courts of Frankfurt am Main or Munich (or DIS arbitration, seat Frankfurt) |
| **Default governing law** | Substantive laws of Germany |

**Boilerplate variants:**

**[Pos. 1.7 — German concepts construction rule]**
> English language words used in this Agreement intend to describe German legal concepts only and the consequences of the use of such words in English law or any other foreign law shall be disregarded. Where a German word is included in italics and in brackets after an English word and there is any inconsistency between the German and the English, the meaning of the German word shall prevail.

**[Pos. 7 — Payments interest]**
> If a Party defaults in the payment when due of any sum payable under this Agreement, it shall pay default interest (*Verzugszinsen*) at the rate provided under § 288 BGB for commercial transactions (basic rate plus 9 percentage points for entities), accruing from the due date until the date of actual payment.

**[Pos. 10 — Good faith]**
> The Parties shall perform this Agreement in accordance with the principle of good faith (*Treu und Glauben*) as set out in § 242 of the German Civil Code (BGB). *(Statutory default applies whether or not expressly stated.)*

**[Pos. 14 — Rescission/annulment waiver]**
> To the extent permitted by German law, the Parties hereby waive their rights to rescind this Agreement on the grounds of mistake (*Irrtum*, §§ 119 et seq. BGB) or interference with the basis of the transaction (*Wegfall der Geschäftsgrundlage*, § 313 BGB) where the Party affected has expressly accepted the risk. This waiver does not extend to fraudulent misrepresentation (*arglistige Täuschung*) or duress (*widerrechtliche Drohung*) or other grounds that cannot be waived under German law.

**[Pos. 17 — Third-party rights local exclusion]**
> No one other than a party to this Agreement, its successors and permitted assignees shall have any right to enforce any of its terms. This Agreement is not intended to constitute a contract for the benefit of a third party (*Vertrag zugunsten Dritter*) within the meaning of § 328 of the German Civil Code (BGB).

**[Pos. 22 — Governing law and jurisdiction]**
> [Clause X].1 — This Agreement and any non-contractual obligations arising out of or in connection with it shall be governed by and construed in accordance with the laws of Germany, excluding the conflict of laws rules thereof and the UN Convention on Contracts for the International Sale of Goods (CISG).
>
> [Clause X].2 — The courts of Frankfurt am Main shall have exclusive jurisdiction over any dispute arising out of or in connection with this Agreement.
>
> *[Alternative — DIS arbitration]*: Any dispute arising out of or in connection with this Agreement shall be finally settled under the Arbitration Rules of the German Arbitration Institute (DIS). The seat of arbitration shall be Frankfurt am Main. The language of the arbitration shall be English. The number of arbitrators shall be [one/three].

**Execution and corporate formalities:**
- GmbH share transfers require notarisation by a German notary (§ 15 GmbHG); foreign notarisation accepted in limited cases
- AG share transfers — generally by endorsement of share certificates; registered shares require entry in share register
- Notarial deed required for: GmbH incorporation, AoA amendments, capital changes, mergers, real estate transactions
- Powers of Attorney for transactions requiring notarisation must themselves be notarised
- Apostille for cross-border use of corporate documents
- Electronic signatures accepted under eIDAS for non-notarial commercial agreements

**Regulatory awareness:**
- Foreign trade FDI screening: AWG/AWV (Foreign Trade Act / Ordinance) — broad sectoral coverage including energy, defence, media, technology
- Bundeskartellamt (Federal Cartel Office) for competition
- Sector regulators: BNetzA (energy, telecoms, rail, post), BaFin (financial services), BfDI (data protection)
```

### Steps the deployer takes to add a custom profile

1. **Identify the slots** that need to be filled — copy the template above
2. **Research the local rules** with local counsel — do not rely on general AI knowledge for jurisdiction-specific provisions; have local counsel review at minimum the Pos. 7 interest mechanism, Pos. 14 rescission grounds, Pos. 22 governing law clause, and execution formalities
3. **Test on one document** — draft a sample SPA or NDA under the new jurisdiction profile and have local counsel review for correctness
4. **Deploy the profile** — make the completed profile available to Claude when the skill is invoked (as a project file, system prompt addendum, or inline in conversation)
5. **Maintain the profile** — review annually or whenever there are material changes in local law (e.g., new FDI screening regime, new interest rate provisions, new arbitration institutional rules)

### Profile interaction with Track C (Litigation)

Track C (litigation filings) is the most jurisdiction-specific track. A jurisdiction profile that includes a Track C section must define:
- Court header format (with the local naming conventions for courts and case identifiers)
- Document title conventions (e.g., "MEMORIA", "WRIT", "MOTION", "KLAGESCHRIFT")
- Procedural reference style (citation of the local code of procedure)
- Drafting language (often the local language, not English)
- Final prayer / relief block conventions
- Evidence list conventions

For starter profiles, only Italy ships with a complete Track C section (Italian memoria conventions). For other starter jurisdictions, Track C drafting requires the deployer to extend the profile with local litigation conventions before relying on the skill for court filings.

---
42:["$","div",null,{"className":"relative z-10 mx-auto max-w-[1400px] px-4 pb-16 sm:px-8 lg:px-16","children":[["$","$L46",null,{"skillId":"45939011-e1c2-487f-a1ba-71c886d1e6fb","skillTitle":"Legal Document Drafting & Formatting","skillStatus":"active","skillVisibility":"listed","slug":"legal-document-drafting-formatting-alessandro-dardano","shareToken":null,"settingsShareToken":null,"fileTree":["SKILL.md"],"textContents":{"SKILL.md":"$47"},"fileSizes":{"SKILL.md":157935},"hasShowcase":false,"hasSandbox":true,"canEdit":false,"isAdmin":false,"demoFiles":[],"sandboxConfig":{"steps":[{"type":"files","filesRequired":false}],"prompt":{"en":"Draft an LOI for an M&A acquisition under English law.\n\nThe buyer is a UK private equity fund acquiring 100% of a UK solar energy \ncompany from its Dutch parent holding. Purchase price around GBP 42.5 \nmillion on a cash-free, debt-free basis. Include exclusivity, customary \nCPs (CMA clearance, W&I insurance, no MAC), 45-day due diligence period, \ntarget SPA signing by end of July 2026, long-stop end of December 2026. \nStandard binding/non-binding structure.\n\nOutput as .docx.\nor\n\nI need to send out an LOI tomorrow morning for an M&A deal. UK private \nequity buyer acquiring 100% of a UK solar company from its Dutch parent. \nAround GBP 42.5m, English law, 45-day DD, 60-day exclusivity, CMA clearance \nand W&I insurance as CPs, SPA by end of July, long-stop end December 2026. \nCan you draft it?","fr":"Draft an LOI for an M&A acquisition under English law.\n\nThe buyer is a UK private equity fund acquiring 100% of a UK solar energy \ncompany from its Dutch parent holding. Purchase price around GBP 42.5 \nmillion on a cash-free, debt-free basis. Include exclusivity, customary \nCPs (CMA clearance, W&I insurance, no MAC), 45-day due diligence period, \ntarget SPA signing by end of July 2026, long-stop end of December 2026. \nStandard binding/non-binding structure.\n\nOutput as .docx.\nor\n\nI need to send out an LOI tomorrow morning for an M&A deal. UK private \nequity buyer acquiring 100% of a UK solar company from its Dutch parent. \nAround GBP 42.5m, English law, 45-day DD, 60-day exclusivity, CMA clearance \nand W&I insurance as CPs, SPA by end of July, long-stop end December 2026. \nCan you draft it?"}},"initialDependencies":[],"initialMcpServers":[],"initialOauthConnections":[],"initialAccessGrants":[],"showcase":null,"about":{"locale":"en","sections":[{"title":"What this skill does","body":"Produces properly-formatted legal documents in Word (.docx). The user \nprovides the substantive content (instructions, attached files, project \nknowledge); the skill handles document architecture and formatting.\n\n* No precedent or template required\n* Seven document families: agreements, corporate documents, litigation, \n  memos, employment, policies, correspondence\n* Jurisdiction-agnostic — works across any legal system the user specifies\n* Multi-Chain numbering, defined-terms convention, structured recitals, \n  atomic signature blocks\n* Also reformats existing .docx to a consistent house style\n* Works in Claude.ai, Cowork, and Claude for Word"},{"title":"How to use","body":"The best way to start is to try it live right here — run it against your own document or question to see exactly how it operates, without any setup. Once you're comfortable, download the skill files and drop them into any AI assistant — Claude (Anthropic), ChatGPT (OpenAI), Gemini (Google), or Mistral. The same skill file works across all of them, so you are never locked into a single provider."}],"requiredSkills":[],"dependentSkills":[],"author":{"name":"Alessandro Dardano
