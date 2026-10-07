# Acceptance Test Plan — Contract QA v1.0.0

## Skill summary

Adaptive Q&A against a single contract with citation-grounded answers. Handles six question types: (A) factual extraction; (B) interpretation / meaning; (C) calculation / quantitative; (D) comparison across clauses; (E) conditional / scenario-based; (F) ambiguity / missing-information detection. Produces answers grounded in cited clauses with verification.

## Test corpus requirements

Source 4–6 anonymized representative contracts covering:

- **At least 1 NDA** (relatively short and structured).
- **At least 1 SaaS or commercial MSA** (longer, multi-section, more complex).
- **At least 1 employment-adjacent agreement** (offer letter, non-compete, severance).
- **At least 1 commercial agreement with notable defined-terms architecture** (extensive defined terms used inconsistently).

For each contract, prepare a question set covering all six question types — a total of ~30 questions across the corpus.

The question set is a deliberate part of the test corpus; it is documented alongside each test contract as `test-corpus/contract-qa/<contract-name>-questions.md`.

## Test scenarios

Each scenario in this test plan is a *question type*, run against representative contracts. Specific question examples should be prepared in advance and stored with the test corpus.

### Scenario 1: Type A — Factual extraction

**Inputs:** Specific factual questions answerable directly from the contract: "What is the term length?" "Who are the parties?" "What is the governing law?" "What is the payment frequency?"

**Expected output structure:**
- Direct answer with inline citation (`[Doc1, p.X, §Y]`).
- Citation resolves to the source clause.
- If multiple clauses bear on the answer, all relevant citations are surfaced.

**Expected calibration:**
- Answer is factually correct.
- Answer is appropriately scoped (does not over-elaborate beyond the question).
- Citation is verbatim-verifiable in source.
- If the answer cannot be definitively determined from the contract (e.g., the term is "five years from execution date" but the execution date is not in the document), the skill says so explicitly.

**Edge cases to verify:**
- If the same fact appears in conflicting forms (e.g., one clause says "thirty (30) days" and another says "thirty business days"), the skill surfaces both and flags the conflict.
- If the answer requires resolving a defined term, the skill resolves the term and cites both the use and the definition.

**Pass criteria:**
- Structural pass: Citations resolve; format is consistent.
- Calibration pass: Answer is factually correct on the source contract.

### Scenario 2: Type B — Interpretation / meaning

**Inputs:** Questions requiring interpretation of contract language: "What does 'reasonable efforts' mean in this contract?" "Does 'including' here mean exhaustive or non-exhaustive?" "What is the effect of the survival clause on Section 8?"

**Expected output structure:**
- Answer addresses the interpretive question with reasoning, grounded in cited clauses.
- The answer differentiates "what the contract says" from "what a court might hold" (the latter is deferred — interpretation skill defers enforceability and outcomes).

**Expected calibration:**
- Reasoning is supported by cited language.
- Answer surfaces ambiguity rather than papering over it.
- Answer does not assert a single definitive interpretation when the language is genuinely ambiguous; it surfaces both readings and notes the ambiguity.

**Edge cases to verify:**
- Where standard usage of a phrase ("best efforts" vs. "commercially reasonable efforts" vs. "reasonable efforts") differs across jurisdictions, the skill notes the cross-jurisdictional variation rather than asserting a single meaning.
- Where the contract has its own defined term that overrides standard usage, the skill resolves to the defined term.

**Pass criteria:**
- Calibration pass: Reviewing attorney confirms the interpretation is supported by the language and that ambiguity is surfaced rather than resolved by fiat.

### Scenario 3: Type C — Calculation / quantitative

**Inputs:** Questions requiring calculation: "What is the maximum liability under this contract?" "What is the effective notice period given the calendar conventions?" "What are the cumulative late fees if payment is 60 days overdue?"

**Expected output structure:**
- Answer shows the calculation (the relevant inputs and the arithmetic).
- Citations to the clauses providing the inputs.
- Final number is correct based on the cited inputs.

**Expected calibration:**
- Arithmetic is correct.
- The skill differentiates clear calculations (cap = $X) from conditional calculations (cap = greater of $X or 12-months-fees, depending on which applies).
- The skill does not invent inputs not present in the contract.

**Edge cases to verify:**
- If multiple liability caps interact (general cap + IP-indemnification carveout + super-cap on data breach), the skill surfaces the structure rather than collapsing to a single number.
- If the calculation depends on inputs the contract does not provide (e.g., "12 months of fees" when annual fees are not stated), the skill flags the missing input.

**Pass criteria:**
- Calibration pass: Reviewing attorney confirms calculation is correct and the structure is appropriately surfaced.

### Scenario 4: Type D — Comparison across clauses

**Inputs:** Questions requiring synthesis across multiple clauses: "How do the survival, termination, and indemnification clauses interact?" "Does the limitation-of-liability clause apply to the indemnification obligations?" "Are there inconsistencies between the warranty section and the limitation-of-liability section?"

**Expected output structure:**
- Answer synthesizes across the named clauses.
- Citations to each cited clause.
- The synthesis is coherent rather than a simple concatenation.

**Expected calibration:**
- The answer reflects how the clauses actually interact (or fail to interact) in this specific contract.
- If clauses are inconsistent, the skill surfaces the inconsistency.
- If clauses are silent on the interaction, the skill notes the silence.

**Edge cases to verify:**
- The skill does not assert standard market-position conclusions ("limitation-of-liability typically does not apply to indemnification obligations") when the specific contract's language differs.
- If the contract uses unusual ordering or cross-references that affect interpretation, the skill surfaces this.

**Pass criteria:**
- Calibration pass: Reviewing attorney confirms the synthesis is grounded in the contract's actual language.

### Scenario 5: Type E — Conditional / scenario-based

**Inputs:** Hypothetical scenario questions: "If the customer terminates for convenience in month 18 of a 36-month term, what payments are owed?" "If a vendor's sub-contractor causes a data breach, what is the customer's recourse?"

**Expected output structure:**
- Answer walks through the scenario step-by-step against the contract's clauses.
- Citations to each operative clause.
- Surfaces gaps where the contract is silent on the scenario.

**Expected calibration:**
- The walk-through is grounded in the contract's actual language.
- The skill does not assume contractual defaults or common-law defaults silently; if the contract is silent, the skill flags the silence and notes (without asserting outcome) that absence may be supplied by governing law.

**Edge cases to verify:**
- If the scenario triggers multiple clauses with potentially conflicting outcomes (e.g., termination for convenience triggers fee acceleration AND triggers limitation-of-liability), the skill surfaces both.
- If the scenario implicates third-party rights (e.g., a downstream customer in a sub-processor breach), the skill notes the third-party context.

**Pass criteria:**
- Calibration pass: Reviewing attorney confirms the scenario walkthrough is grounded and the silences are appropriately flagged.

### Scenario 6: Type F — Ambiguity / missing-information detection

**Inputs:** Questions probing for ambiguity or completeness: "Are there any ambiguities in the limitation-of-liability clause?" "What's missing from this contract's data-handling provisions that you'd expect to see?" "Is the termination-for-cause definition clear?"

**Expected output structure:**
- Answer surfaces specific ambiguities or missing items.
- Citations to the ambiguous or absent provisions.
- The answer is constructive — surfacing ambiguities rather than ignoring them.

**Expected calibration:**
- Ambiguities surfaced are real (a reviewing attorney would also identify them).
- Missing items are calibrated to what one would expect to see in this contract type.
- The skill does not over-flag (calling everything ambiguous) or under-flag (missing genuine ambiguities).

**Edge cases to verify:**
- The skill flags ambiguities that affect operational use (e.g., "the contract requires 'prompt' notification but does not define 'prompt'") at appropriate severity.
- The skill differentiates calling-out ambiguity from asserting one interpretation.

**Pass criteria:**
- Calibration pass: Reviewing attorney confirms ambiguity-detection is calibrated.

## Refusal scenarios

### Refusal 1: Question requires legal advice the skill cannot give

**Input:** "Is this contract enforceable?" "Will I win a breach claim under this contract?" "Should I sign this contract?"

**Expected behavior:**
- Skill explicitly declines to provide legal advice or outcome predictions.
- Skill notes that the question is outside the skill's scope and that the user should consult qualified legal counsel.
- Skill optionally offers to answer a related, in-scope question (e.g., "I can identify provisions that affect enforceability; would that be helpful?").

**Pass criteria:** Explicit refusal with appropriate reframe.

### Refusal 2: Question requires information not in the document

**Input:** "What is the typical industry liability cap for SaaS contracts?" "What does this clause typically mean in California?" (when no jurisdiction or industry context is in the document)

**Expected behavior:**
- Skill notes that the question requires information not in the document.
- Skill optionally provides general context (caveated) or recommends external research.

**Pass criteria:** Skill clearly distinguishes contract-grounded answers from general-knowledge answers.

## Cross-cutting verification

- **All citations resolve.** Every citation in every answer points at a clause that contains the cited content.
- **No invented contractual content.** The skill does not invent provisions, recite provisions that don't exist, or paraphrase in ways that change meaning.
- **No outcome assertions.** The skill does not assert outcomes ("the court will hold X"), enforceability ("this is enforceable / unenforceable"), or settlement values.
- **Refusals are clean.** Out-of-scope questions trigger explicit refusal rather than silently producing low-quality answers.
- **"What this skill does not do" enumeration present.** Typical: legal advice, outcome prediction, enforceability assessment, comparison to industry standards, jurisdiction-specific application.

## Pass / fail decision

Contract QA v1.0.0 passes acceptance testing when:

1. The corpus question set is run against each contract.
2. Each question type (A–F) is exercised at least 4 times across the corpus.
3. Structural checks pass: citations resolve; refusals trigger appropriately.
4. Calibration evaluation by reviewing attorney passes for each question type.
5. Cross-cutting verification passes on every answer.

## Reviewer notes

Contract QA is the most varied of the M1 starter skills (six question types, free-form question generation). The reviewing attorney should be experienced enough to recognize when a contract-grounded answer is correct, when it is wrong-but-plausible, and when it overclaims into legal advice.

Specific competencies:
- Recognizing when a calculation has the wrong inputs vs. the wrong arithmetic.
- Recognizing when an interpretation overclaims certainty on ambiguous language.
- Recognizing when an answer paraphrases the contract in ways that subtly change meaning.

Calibration assessment is documented in `test-results/contract-qa-v1.0.0/calibration-assessment.md`.

## Note on test corpus design

Contract QA's test corpus is unusual among the M1 skills because each contract requires a paired question set. The question set should:

- Cover all six question types (A–F).
- Include at least one question per type that has a clear, correct, contract-grounded answer.
- Include at least one question per type that probes an edge case (ambiguity, missing information, conflicting clauses).
- Include at least one out-of-scope question (legal advice, outcome prediction, industry-standard comparison) to verify refusal behavior.

The question set is a permanent artifact, updated alongside the test corpus as new edge cases surface.
