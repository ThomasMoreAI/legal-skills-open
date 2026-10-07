# Acceptance Test Plan — Comms Improver v1.0.0

## Skill summary

Rewrites legal-jargon-heavy text in plain language for a specified non-legal audience (executive, sales team, customer-facing, board). Preserves substantive meaning while transforming style, tone, and vocabulary. Supports `audience` input (executive / sales / customer / board / non-legal-layperson) and `preserve_authority` mode (when the rewrite must preserve cited authorities).

## Test corpus requirements

Source 6–10 anonymized text samples covering:

- **At least 2 contractual clauses** that would benefit from plain-language rewriting (e.g., a complex limitation-of-liability clause, a multi-clause indemnification provision).
- **At least 2 legal memos / analysis paragraphs** that would benefit from executive-summary-style rewriting.
- **At least 2 regulatory/compliance language samples** (e.g., a paragraph from a privacy policy, a HIPAA-related advisory).
- **At least 1 sample requiring authority preservation** (citation to a case or regulation that must be retained in the rewrite).
- **At least 1 sample with technical legal terminology** that has no clean plain-language equivalent (e.g., "promissory estoppel", "respondeat superior").

For each sample, run with at least two different `audience` inputs to verify audience-specific calibration.

## Test scenarios

### Scenario 1: Contract clause for non-legal layperson audience

**Inputs:** A complex contract clause (e.g., a limitation-of-liability clause). Audience: `non_legal_layperson`.

**Expected output structure:**
- Rewritten text in plain language.
- Optional brief note ("What changed in the rewrite") summarizing the simplifications applied.
- Citation back to original clause (which clause / section).
- "What this skill does not do" note if relevant.

**Expected calibration:**
- Rewritten text is meaningfully simpler (shorter sentences, fewer clauses, common-vocabulary words).
- Substantive meaning is preserved (the rewrite says the same thing).
- The rewrite does not change the legal effect (a "shall" doesn't become a "may"; an exception doesn't become a guarantee).
- Words removed in simplification are non-substantive (legalese for legalese's sake).

**Edge cases to verify:**
- If the original clause has a defined term, the defined term is preserved (or explained in plain language without changing its scope).
- If the original clause has carveouts or exceptions, all are preserved.
- If the original clause has cross-references to other clauses, the references are preserved or replaced with self-contained explanation.

**Pass criteria:**
- Structural pass: Rewrite is provided; format is consistent.
- Calibration pass: Reviewing attorney confirms substantive meaning is preserved and simplification is meaningful.

### Scenario 2: Legal memo for executive audience

**Inputs:** A multi-paragraph legal memo or analysis. Audience: `business_executive`.

**Expected output structure:** Rewritten text optimized for executive consumption — bottom-line-up-front, decision-oriented, with strategic implications surfaced.

**Expected calibration:**
- The rewrite leads with the recommendation or the conclusion.
- Detail is appropriately compressed (an executive summary is shorter than the underlying memo).
- Strategic implications are surfaced.
- The rewrite preserves the analysis's substantive conclusions; it does not assert different conclusions.

**Edge cases to verify:**
- If the original memo has multiple conclusions or alternatives, the rewrite preserves the optionality.
- If the original memo has caveats, the rewrite preserves the caveats (or surfaces them in a "Caveats" section).

**Pass criteria:** As above with executive-audience-specific verification.

### Scenario 3: Regulatory language for sales-team audience

**Inputs:** A paragraph from a privacy policy or HIPAA advisory. Audience: `sales_team` (or "non-legal customer-facing").

**Expected output structure:** Rewrite optimized for sales-team understanding — focused on what the sales team can say to customers, what they cannot say, what they should escalate.

**Expected calibration:**
- The rewrite is operationally usable by the sales team.
- The rewrite does not invent permissions or restrictions not in the original.
- Caveats and escalation triggers are preserved.

**Edge cases to verify:**
- The rewrite does not turn a regulatory restriction into a sales pitch.
- If the original mentions enforcement risks, the rewrite preserves the risk awareness.

**Pass criteria:** As above with sales-audience-specific verification.

### Scenario 4: Authority-preservation mode

**Inputs:** A legal memo with cited authority (a case, a regulation). Audience: any. `preserve_authority: true`.

**Expected output structure:** Rewrite preserves the cited authority verbatim; the rewrite is around the citation, not on top of it.

**Expected calibration:**
- Citations are preserved exactly.
- The rewrite does not invent or alter authorities.
- The reasoning chain that connects the authority to the conclusion is preserved.

**Edge cases to verify:**
- If the original has multiple authorities, all are preserved.
- If the original has a quotation from an authority, the quotation is preserved verbatim.

**Pass criteria:** Reviewing attorney confirms citations are preserved unaltered.

### Scenario 5: Technical legal terminology

**Inputs:** A passage with technical legal terminology that lacks clean plain-language equivalents ("promissory estoppel", "respondeat superior", "force majeure", "novation"). Audience: `non_legal_layperson`.

**Expected output structure:** The rewrite either explains the term in plain language (with the term preserved on first use) or replaces with operational equivalent that captures the meaning.

**Expected calibration:**
- The skill does not silently drop technical terms or replace them with imprecise equivalents.
- The skill differentiates "term has no clean equivalent" from "term has a clean equivalent" and handles each appropriately.
- If the term is operationally significant, the term is preserved with explanation.

**Edge cases to verify:**
- The rewrite does not lose precision in service of simplification.
- The rewrite flags terms it cannot fully capture in plain language.

**Pass criteria:** Reviewing attorney confirms precision is preserved.

### Scenario 6: Audience-comparison run

**Inputs:** The same source text run twice with different audiences (e.g., `business_executive` vs. `non_legal_layperson`).

**Expected output structure:** Two distinct rewrites, each calibrated to its audience.

**Expected calibration:**
- The two rewrites differ in tone, depth, and emphasis appropriate to their audiences.
- Both preserve the same substantive meaning.
- Neither omits information the other includes (audience-driven emphasis differs; substance does not).

**Edge cases to verify:**
- Audience differences are visible in the rewrite (executive version leads with recommendation; layperson version uses simpler vocabulary).
- The two rewrites would not be reconciled into a single "right" answer — they are appropriately different.

**Pass criteria:** Reviewing attorney confirms both audience-calibrations are appropriate.

## Refusal scenarios

### Refusal 1: Source text is not a candidate for rewriting

**Input:** A short, already-clear sentence; or a non-legal text (e.g., a marketing email).

**Expected behavior:**
- Skill notes that the text doesn't need rewriting (or doesn't have legal content amenable to legal-jargon simplification).
- Skill optionally proceeds with light edits and a note.

**Pass criteria:** Skill avoids producing low-quality rewrites of text that doesn't need rewriting.

### Refusal 2: Rewrite would substantively alter legal effect

**Input:** A passage where simplification would inevitably change the legal effect (e.g., "best efforts" to "try to" — these are not legally equivalent).

**Expected behavior:**
- Skill explicitly flags that simplification would alter legal effect.
- Skill either preserves the original term with explanation, or refuses to simplify the specific phrase.

**Pass criteria:** Skill distinguishes preservation of meaning from simplification of vocabulary.

## Cross-cutting verification

- **No substantive alteration.** The rewrite preserves the substantive meaning of the original. Practical test: the rewriting reviewer confirms that the rewrite, if relied on instead of the original, would lead to the same operational decisions.
- **No invented content.** The rewrite does not add factual claims, exceptions, or qualifications not in the original.
- **No omission of substantive content.** The rewrite does not silently drop substantive provisions in the name of simplification.
- **Audience calibration is real.** Different audiences produce visibly different rewrites.
- **Citations preserved.** When `preserve_authority: true` or when authorities are operative, the citations are preserved.
- "What this skill does not do" enumeration present.

## Pass / fail decision

Comms Improver v1.0.0 passes acceptance testing when:

1. All 6 test scenarios pass structural checks.
2. All 6 test scenarios pass calibration evaluation — a reviewing attorney confirms substantive preservation across the rewrites.
3. Both refusal scenarios trigger documented refusal behavior.
4. Cross-cutting verification passes on every scenario.

## Reviewer notes

The reviewing attorney for Comms Improver acceptance testing should be experienced enough to recognize subtle substantive shifts in rewrites. Specific competencies:

- Recognizing when "shall" vs. "may" vs. "will" shifts change legal effect.
- Recognizing when a simplification has dropped an exception or carveout.
- Recognizing when audience calibration has slipped into substantive change.
- Calibrating "good plain language for executives" against "good plain language for laypeople" — both are plain language, but they differ.

Calibration assessment is documented in `test-results/comms-improver-v1.0.0/calibration-assessment.md`.
