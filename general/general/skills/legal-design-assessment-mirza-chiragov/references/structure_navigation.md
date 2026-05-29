# Structure and Navigation — Reference

Loaded when the audit reaches Step 5. Assesses how the document organises information at the level of sections, headings, and cross-references — independent of the language used within.

## What this pillar covers

A document can have perfect plain-language prose at sentence level and still fail its reader because the right information is in the wrong place, or because the reader cannot navigate to what they need. This pillar evaluates:

1. Heading hierarchy and coherence.
2. Section length distribution.
3. Table of contents and findability.
4. Defined terms management.
5. Cross-reference density and chain depth.
6. Layered drafting and signposting.
7. Information grouping (related obligations together vs. scattered).

## Checkpoints

### 1. Heading hierarchy

Look for:

- **Heading levels used.** Most well-drafted long documents use 2–4 levels (e.g., Part / Section / Subsection / Paragraph). 5+ levels is usually unmanageable. 1 level (a flat list of 50 clauses with no grouping) is also a problem.
- **Heading wording.** Headings should be **descriptive** ("Payment schedule and late fees") rather than **abstract** ("General provisions"). Count abstract headings ("General", "Miscellaneous", "Other matters", "Sundry", "Diverses dispositions", "Sonstiges", "Allgemeine Bestimmungen" — in moderation each is fine; a quarter of the document under "Miscellaneous" is a warning sign).
- **Numbering consistency.** Mixed numbering (1, 1.1, 1.1.1 interleaved with A, B, C without rule) is a navigation failure.
- **Skipped levels.** Section 3 → Section 3.1 → 3.1.1.1 (skipping 3.1.1) is disorienting.

Severity:

- All headings descriptive, hierarchy 2–4 levels deep, consistent numbering → Green.
- Largely descriptive with 1–2 abstract catch-alls of reasonable length → Yellow.
- Significant share of content under abstract catch-all headings, or inconsistent numbering → Amber.
- No usable hierarchy, "Miscellaneous" sections containing material obligations, or heading wording that misrepresents content → Red.

### 2. Section length distribution

Compute, for each top-level section:

- Word count.
- Number of sub-sections.

Identify outliers — sections more than 3 standard deviations longer than the document-wide mean. A 12,000-word document where one section is 4,000 words is a navigation failure even if each sentence is well written.

Report the distribution as a short table:

| Section | Words | Sub-sections | Note |
| --- | --- | --- | --- |
| 1. Definitions | 1,400 | 0 | High — definitions should usually use a glossary block |
| 2. Term and termination | 600 | 4 | OK |
| 12. Miscellaneous | 3,200 | 8 | Outlier — material obligations buried |

### 3. Table of contents

For documents over ~3,000 words or with more than 10 sections:

- Is there a ToC? If not, mark deficiency.
- Is it accurate? (When ToC entries do not match actual section titles or numbers.)
- Are page numbers / hyperlinks present (where format permits)?
- Does it expose at least two levels of hierarchy?

For shorter documents, ToC absence is not a deficiency by itself.

### 4. Defined terms

Defined terms are powerful but break down at scale. Assess:

- **Total count.** A document with 80+ defined terms is taxing the reader's working memory.
- **Definition placement.** Inline definitions (defined at first use) vs. consolidated glossary at the start. Modern legal-design practice prefers the glossary approach for documents over ~5,000 words.
- **"Including without limitation" definitions.** Definitions that include open-ended categories ("Affiliate means…and any other entity that…") shift interpretive load to the reader at every use. Note them.
- **Definitions used only once.** A defined term used only once is wasted machinery. Count and report.
- **Defined-term capitalisation discipline.** If the document uses initial capitals for defined terms ("the Party", "the Services"), every use of "party" / "services" in lower case is either an undefined common-noun use (fine) or a drafting inconsistency (problem). Flag inconsistencies — they materially confuse readers.

### 5. Cross-references — chain depth

In addition to cross-reference density (covered in the linguistic-patterns pillar):

- **Chain depth.** A cross-reference to clause 7.2, which itself contains a cross-reference to schedule B, which itself cross-references the master agreement, is a 3-deep chain. Any chain over 2 deep is Amber. Over 3 deep is Red.
- **Unresolved references.** "As defined in Annex C" where Annex C is not provided is Red regardless of context.
- **Forward references.** "As provided in clause 23" appearing in clause 5 — forces the reader to either jump or read on faith. Count occurrences.

### 6. Layered drafting and signposting

Legal-design practice favours **layering**: a one-paragraph summary at the top of a long clause, with detail below; or a "key terms" box at the start of a consumer T&C. Assess:

- Presence of executive summary or "this contract in plain English" sections.
- Presence of clause-level summaries for the longest clauses.
- Signposting language ("This section explains…", "In short:", "Diese Klausel regelt…", "L'objet de la présente clause est…").

Documents with effective layering earn an explicit Green note in this pillar even if other metrics are mixed.

### 7. Information grouping

Read across the document for related obligations that are scattered:

- Payment obligations split across "Price", "Payment", "Late fees", and "Termination" without cross-references.
- Data-protection obligations partly in a privacy notice and partly in the contract body.
- Limitation of liability appearing in three separate clauses with overlapping or conflicting caps.

Flag scattered families of obligations. This is impactful for the prioritised attention list in Section 10 of the report.

## Pillar score for Structure and Navigation

Combine the seven checkpoints into a 0–100 pillar score using equal weights:

1. Heading hierarchy.
2. Section length distribution.
3. Table of contents (or absence justified by length).
4. Defined terms management.
5. Cross-reference chains.
6. Layered drafting / signposting.
7. Information grouping.

Each checkpoint maps to a component:

- Green → 90.
- Yellow → 70.
- Amber → 45.
- Red → 20.
- Grey / Not applicable → exclude from the average.

Pillar score = mean of applicable components, rounded.

## What to report in the pillar section

Lead with the heading-hierarchy assessment and the section-length distribution table. Then enumerate the deficiencies as a findings table:

| # | Issue | Location | Severity | Note |
| --- | --- | --- | --- | --- |
| 5.1 | "Miscellaneous" section contains termination triggers | Clause 24 | Red | Material obligations under an abstract heading; reader cannot find them |
| 5.2 | Defined term "Services" used in both initial-cap and lower-case forms inconsistently | document-wide | Amber | 14 of 41 occurrences are lower case |
| 5.3 | Cross-reference chain 3 deep | Clause 7.2 → Schedule B → Master Agreement § 3 | Amber | Reader must consult three documents |
| 5.4 | No table of contents in 14,000-word contract | — | Amber | A ToC would resolve navigation |

End with a one-paragraph synthesis of the structural posture.
