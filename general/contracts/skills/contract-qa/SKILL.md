---
name: contract-qa
title: Contract QA
description: Use when the user has a contract loaded and asks a specific question about it — what a clause means, where something is addressed, whether a term is unusual, how a provision compares to standard practice, or what would happen in a specified scenario under the contract. Produces an answer calibrated to the question's shape (direct answer for fact lookups, paragraph with context for "is this unusual" questions, structured findings for multi-issue questions), with verbatim citations to specific clauses. Does not perform full reviews — for that, use the appropriate review skill (NDA Review, DPA Checklist Review, MSA Review, etc.).
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-ai/tree/main/skills/contract-qa
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Contract QA

Answer the user's specific question about a loaded contract. The answer is precise, cited to the document, and shaped by the question — not by a fixed template.

This skill handles question-driven inquiry against a single contract. It is the right skill when the user has a *specific question* and wants a *specific answer*. It is the wrong skill when the user wants a comprehensive review of a contract — for that, route to the appropriate review skill (NDA Review, DPA Checklist Review, MSA-SaaS Review, etc.).

## When this skill applies

Apply when:

- The user has loaded a contract and asks a specific question about its content.
- The user asks "where" something is addressed in the contract.
- The user asks whether a clause is unusual, standard, or aggressive.
- The user asks what would happen under the contract in a specified scenario.
- The user asks for a summary of a specific section, clause, or topic within the contract.

Do not apply when:

- The user asks for a full review or risk assessment of the contract — route to the appropriate review skill.
- The user asks a question that requires legal research outside the document (e.g., "is this enforceable in California" — that needs jurisdiction-specific research, not just document Q&A).
- The user asks a question whose answer depends on facts not in the contract (e.g., "did we breach this" — that depends on facts the skill does not have).
- The user asks for legal opinion (e.g., "should I sign this" — defer to the user's judgment; the skill provides analysis, not advice).
- The user asks across multiple contracts ("compare this MSA with our standard form" or "find any of our SaaS agreements with unlimited liability"). This is multi-document Q&A; deferred to v2.

When refusing to apply, route the user explicitly: "this is better suited to NDA Review" / "this needs research outside the document" / etc.

## Inputs

The skill requires the document and the question. If the user has a contract loaded but no specific question, ask:

> "What would you like to know about this contract?"

Optional inputs (`contract_type`, `perspective`, `jurisdiction`, `prior_context`) calibrate the answer. The skill should:

- **Infer `contract_type` from the document** if not provided, and state the inference in answers where it affects calibration ("Treating this as a SaaS MSA based on the structure...").
- **Use `perspective` when answering perspective-sensitive questions.** "Is this unusual" reads differently from each side. If perspective is not provided and the question is perspective-sensitive, either ask for it or answer from a neutral lens with a note.
- **Reference `jurisdiction` only when the question depends on it.** Most contract Q&A is jurisdiction-agnostic (what does the document say); jurisdiction matters for interpretation and enforceability questions.

## Workflow

The workflow has three steps. Each step's behavior depends on the question type identified in step 1.

### Step 1: Classify the question

Read the user's question and classify it into one of these types. The classification drives the output format (adaptive output is the whole reason this step matters).

**Type A: Direct lookup.** The user wants to know what the contract says about a specific topic.
- "Where does the contract address indemnification?"
- "What's the term of this agreement?"
- "What does Section 7 say?"
- "Does this contract have an arbitration clause?"
- Output format: **direct answer with verbatim quote and citation.** Brief.

**Type B: Interpretation.** The user wants to understand what a clause means, how it operates, or how to apply it.
- "What does this indemnification clause actually require?"
- "How does the renewal mechanism work?"
- "If we terminate, what survives?"
- Output format: **explanation paragraph with verbatim quote and citation.** Plain language; preserve precision.

**Type C: Comparison / unusualness.** The user wants to know whether a provision is standard, unusual, aggressive, or favorable.
- "Is this limitation of liability unusual?"
- "How does this non-compete compare to standard?"
- "Is the IP assignment scope aggressive?"
- Output format: **paragraph with context.** Quote the provision; describe how it sits relative to typical practice for the contract type; calibrate to perspective if specified.

**Type D: Scenario.** The user wants to know what would happen in a specified factual scenario.
- "What happens if we miss the renewal notice deadline?"
- "If they breach, what are our remedies?"
- "If we want to assign this contract, what do we have to do?"
- Output format: **scenario walk-through.** Cite the controlling clauses; trace the consequence; note where the answer depends on facts the skill does not have.

**Type E: Multi-issue.** The user asks about multiple topics in one question, or asks about a topic that has multiple distinct aspects.
- "What are the IP and confidentiality terms?"
- "Walk me through the termination provisions."
- "What protections do we have if they go bankrupt?"
- Output format: **structured findings.** One subsection per issue, each with quote and citation.

**Type F: Out of scope.** The question is one the skill should not answer (full review, legal research, scenario depending on external facts, opinion).
- Route to the appropriate path; do not answer.

If the question does not cleanly fit one type, default to the type that produces the most useful answer (typically B or E).

### Step 2: Find the relevant content in the document

For every question type except F:

- Locate the clauses, sections, or content in the document that answer the question.
- For Type A and B, this is typically one or a few specific clauses.
- For Type C, this includes the clause being asked about plus any related provisions (e.g., a limitation of liability question may need the LoL clause plus any carve-outs in the indemnification section).
- For Type D, this includes the controlling clause plus any conditions, exceptions, and consequence provisions that the scenario triggers.
- For Type E, this includes all clauses relevant to all issues asked about.

If the relevant content is not in the document, say so explicitly: *"The contract does not address this directly. The closest provisions are [X], which suggests [interpretation], but the question is not resolved by the document."*

If the relevant content is ambiguous, say so: *"The contract is ambiguous on this point. Section X says [quote A], which would suggest [interpretation 1], but Section Y says [quote B], which would suggest [interpretation 2]. The contract does not resolve the conflict."*

### Step 3: Produce the answer

Format the answer per the question type identified in Step 1.

**For all formats:** Lead with the answer. The user asked a question; the first sentence should answer it. Citations support the answer; they do not bury it.

**Verbatim quotes** must be exact. If you cannot quote verbatim, paraphrase explicitly ("The clause says, in substance, ..."). Do not produce reconstructed quotes that look verbatim but aren't.

**Citations** include the section/clause reference and (where the document supports it) the page reference. Format: `[§4.2(b)]` or `[§4.2(b), p. 7]`.

**Length is proportional to question shape.** A Type A question gets a sentence. A Type C question gets a paragraph. A Type E question gets one subsection per issue. Do not pad.

**Always identify what you cannot answer.** If part of the question is out of scope, or depends on facts not in the document, name that explicitly at the end: *"The skill cannot determine [X] from the document alone — that depends on [the user's facts / jurisdiction-specific law / counterparty's behavior]."*

## Output formats by question type

### Type A — Direct lookup format

```markdown
[Direct answer in one sentence.]

> [Verbatim quote from the contract]

[§ ref, p. ref]

[If relevant: brief note on context, e.g., "This is in the boilerplate section; no special carve-outs apply."]
```

### Type B — Interpretation format

```markdown
[Direct answer / interpretation in one or two sentences.]

The relevant clause is [§ ref]:

> [Verbatim quote]

[Two to four sentences explaining how the clause operates: what triggers it, what it requires, what its scope is, what its limits are. Use plain language; preserve legal precision where it matters.]

[If applicable: cross-references to related clauses that affect the interpretation.]
```

### Type C — Comparison / unusualness format

```markdown
[Direct verdict in one sentence: standard / unusual / aggressive / favorable to [perspective].]

The clause says [§ ref]:

> [Verbatim quote]

[One to two sentences describing how this provision sits relative to typical practice for [contract_type]. What's the typical range? Where does this fall in that range? What's the practical effect of the deviation, if any?]

[If perspective was specified: how this reads from the user's side specifically.]

[If unusual / aggressive: what a more standard version would look like.]
```

### Type D — Scenario format

```markdown
[Direct answer in one sentence: under the contract, [the scenario produces this outcome].]

The controlling provisions are:

- **[§ ref]** — [brief description of what this clause does in the scenario]

  > [Verbatim quote of the relevant language]

[If multiple clauses operate together, include each. Trace the chain of consequence: clause X triggers, which produces consequence Y, which interacts with clause Z, etc.]

[Note any conditions, exceptions, or facts the answer depends on that are not in the document. Be specific: "This assumes [fact]; if [different fact], the answer changes to [different outcome]."]
```

### Type E — Multi-issue format

```markdown
[One- or two-sentence orientation: there are [N] distinct issues here; here's how they break down.]

### [Issue 1]

[Sub-answer for issue 1, formatted appropriately to its type — usually B or C.]

### [Issue 2]

[Sub-answer for issue 2.]

[etc.]

[If the issues interact: a brief closing paragraph identifying the interactions.]
```

## Edge cases and refusals

- **Question is out of scope.** Route the user to the appropriate skill: NDA Review, MSA Review, DPA Checklist Review for full reviews; legal-research skill for jurisdiction-specific questions; etc. Do not attempt to answer.

- **Question is unanswerable from the document alone.** Say so. Identify what would be needed to answer (specific facts, jurisdictional analysis, counterparty's interpretation) and stop. Do not speculate.

- **Question is ambiguous.** Ask one clarifying question rather than guessing: *"Are you asking about [interpretation 1] or [interpretation 2]? They produce different answers."*

- **Question requires reading the contract to answer but the document is missing pages, has OCR errors, or is otherwise incomplete.** Note the document quality issue: *"The document I have appears to be incomplete — [§ X] references [§ Y] which is not in the file. Answer based on what's present, with that caveat."*

- **User asks for legal advice ("should I sign this")**. Reframe: *"That's a judgment call I won't make for you. What I can tell you about the contract is [factual analysis]. Whether that's acceptable depends on your business judgment about [the trade-off involved]."*

- **User asks "is this clause enforceable in [jurisdiction]"** Partial answer: describe what the clause says, note that enforceability depends on jurisdiction-specific law, and route to legal research: *"The clause says [X]. Whether that's enforceable in [jurisdiction] depends on [the relevant law]; I can analyze the document but not the law. Recommend a research query."*

- **User asks a perspective-sensitive question ("is this favorable")** but no perspective was specified. Ask: *"Favorable to whom — your side, the counterparty, or neutral?"*

- **User has been asking many questions about the same document and shows signs of wanting a full review.** Suggest the route: *"Based on the questions so far, you may want a full review using NDA Review / MSA Review / etc. — that produces a structured report rather than answering question-by-question."*

## What this skill does not do

- Full contract review (route to the appropriate review skill).
- Multi-document Q&A (deferred to v2; tracked as DE-060).
- Legal research outside the document (route to research skill).
- Enforceability opinions (route to research; note as user judgment).
- Drafting (route to drafting skill).
- Strategy advice (out of scope; the user owns business judgment).

## Reference materials

- `reference/question_classification.md` — examples and edge cases for the six question types, with classification heuristics.
- `reference/citation_format.md` — conventions for citing within Contract QA outputs.
- `examples/example_type_a_lookup.md` — worked example: direct lookup question.
- `examples/example_type_c_unusualness.md` — worked example: comparison question with perspective.
- `examples/example_type_d_scenario.md` — worked example: scenario walkthrough with conditional outcomes.
- `examples/example_type_e_multi_issue.md` — worked example: multi-issue question producing structured findings.
