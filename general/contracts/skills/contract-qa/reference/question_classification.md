# Question Classification

This reference helps the skill correctly classify a user's question into one of the six types defined in the SKILL.md. Misclassification produces wrong-shaped answers (a paragraph when a sentence was wanted, or vice versa); accurate classification is the central skill move.

## Quick decision rules

Read the question. Apply these rules in order; the first match wins.

1. **If the question can be answered by quoting one clause without explanation, it's Type A (Direct lookup).** Test: would "the clause says [quote]" be a satisfying answer? If yes, Type A.

2. **If the question asks "what does X mean," "how does X work," or "what would X require," it's Type B (Interpretation).** The user has located the clause; they want help understanding it.

3. **If the question contains comparative language — "unusual," "standard," "aggressive," "favorable," "common," "compare to," "how does this stack up" — it's Type C (Comparison).** The answer is calibrated against typical practice for the contract type.

4. **If the question contains conditional language — "if," "what happens when," "in the event that," "suppose that," "what if" — it's Type D (Scenario).** The answer traces the contractual consequence of a hypothetical fact pattern.

5. **If the question asks about multiple topics, or asks broadly about a topic with multiple distinct aspects ("walk me through," "summarize," "what are the [X] terms"), it's Type E (Multi-issue).** The answer is structured findings.

6. **If the question is asking for a full review, legal research, drafting, or opinion, it's Type F (Out of scope).** Route, don't answer.

When two rules could apply, pick the type that produces the more useful answer. When in doubt between B and E, ask whether the topic has one core operative provision (B) or several (E). When in doubt between A and B, ask whether the user wanted to find the clause (A) or understand it (B); a good test is whether the user already knew which clause they were asking about.

## Examples by type

### Type A — Direct lookup

> "What's the term of this agreement?"

The user wants a fact. The answer is a sentence: "The term is three years from the effective date, with automatic one-year renewals unless either party provides 60 days' notice of non-renewal." Quote the clause; cite; done.

> "Does this contract have a force majeure clause?"

Yes/no question. The answer is "yes, in §14.7" or "no, there is no force majeure provision." Brief.

> "Where is indemnification addressed?"

Locator question. The answer identifies the section(s): "Indemnification is in Article 9 (§§9.1–9.4); §9.1 is the mutual indemnification, §9.2 is the IP indemnification carve-out, §9.3 is procedure, §9.4 is the cap." Brief; pointer.

### Type B — Interpretation

> "What does this indemnification clause actually require?"

The user has the clause; they want to understand its operation. The answer is a paragraph: identify the trigger (claims arising from), the obligation (defend and indemnify), the scope (third-party claims; not first-party damages), the limits (cap; carve-outs), and any conditions (notice, control of defense).

> "How does the renewal mechanism work?"

Operational question. Walk through: when notice is required, how it's delivered, what happens if no notice, what happens if either party gives notice. Cite the controlling clauses.

> "If we terminate, what survives?"

Asking how the termination clause operates with respect to surviving provisions. Identify the survival clause; list what survives; note any conditions on survival.

### Type C — Comparison / unusualness

> "Is this limitation of liability unusual?"

Comparative question. Quote the clause; describe how it sits relative to typical practice for the contract type (cap at fees paid in 12 months prior is standard for SaaS MSAs; cap at fees paid in 6 months is below market; uncapped liability for IP indemnification is standard but uncapped for everything is unusual). Calibrate to perspective if specified.

> "How aggressive is this non-compete?"

Comparative-with-judgment question. Describe the scope (geographic, duration, activity); compare to typical non-competes for the contract type and jurisdiction; identify what would make a tamer version.

> "Is the IP assignment scope appropriate for a vendor agreement?"

Comparative question with strong perspective implication. Describe the scope; describe what's typical; identify whether the deviation is favorable to one side or the other.

### Type D — Scenario

> "What happens if we miss the renewal notice deadline?"

Conditional question. The answer traces what the contract says about missed deadlines: typically auto-renewal applies (which clauses); the consequence (committed for another term); whether there's a cure mechanism (usually not for renewal notices); whether equity might intervene (out of scope; note the contract's answer).

> "If they breach the confidentiality clause, what are our remedies?"

Conditional question about consequences. Trace through: the breach provision; available remedies (damages? equitable relief? attorneys' fees?); any cap on damages; any conditions (notice; opportunity to cure).

> "If we want to assign this contract, what do we have to do?"

Conditional question about a permitted action's mechanics. Identify the assignment clause; note whether consent is required; note any deemed consents (e.g., assignment to successor in M&A); note any notice requirements.

### Type E — Multi-issue

> "What are the IP and confidentiality terms?"

Multiple topics in one question. Structure: §IP terms, §Confidentiality terms, each with its own quote and explanation, plus a closing paragraph if they interact (e.g., the IP assignment may be qualified by the confidentiality reservation).

> "Walk me through the termination provisions."

Topic with multiple aspects. Structure: termination for cause, termination for convenience, effect of termination (survival), post-termination obligations, any wind-down provisions.

> "What protections do we have if they go bankrupt?"

Topic with multiple operative clauses. Structure: any bankruptcy-specific termination right, IP licensing protections (Section 365(n) language), payment acceleration, return of property, ongoing obligations of debtor's estate.

### Type F — Out of scope

> "Is this contract a good deal?"

Opinion / judgment. Reframe: explain what the contract says about specific terms; identify the trade-offs; let the user decide.

> "Should I sign this NDA?"

Same. Provide analysis, not advice.

> "Is the indemnification cap enforceable in California?"

Jurisdiction-specific legal research. Describe the clause; note the question; route to research.

> "Compare this with our standard MSA."

Multi-document. Out of scope for v1; deferred to v2 (DE-060).

> "Review this contract and tell me what to worry about."

Full review request. Route to appropriate review skill (NDA Review, MSA Review, etc.).

## Hard cases

### When the question is mixed-type

> "What does this indemnification clause require, and is it unusual?"

This is B + C. Answer in C format (the unusualness analysis includes interpretation; it's the more demanding format that subsumes the simpler one). Lead with the comparative verdict; explain the clause as part of describing what's standard.

> "Where is renewal addressed, and what happens if we miss the deadline?"

This is A + D. Answer in D format (the scenario walkthrough cites the location naturally). Don't produce two separate answers.

### When the question is implicit

> "I'm worried about IP."

Not a question; a concern. Reframe: *"Are you asking what the IP terms are (Type E), how the IP assignment works (Type B), or whether the IP terms are unusual (Type C)? They produce different answers."* Or, if the user's signal is clear enough, default to E and give an overview that covers all three.

### When the question is technically out of scope but a partial answer would help

> "Is this clause enforceable in California?"

The skill should not produce an enforceability opinion, but it can describe the clause and note where the enforceability question turns. *"The clause says [X]. Whether it's enforceable in California depends on [the relevant test, e.g., Cal. Bus. & Prof. Code §16600 for non-competes]; that's a research question. I can answer document questions; for the legal question, recommend a separate research query."*

### When the user asks a Type C question without perspective

> "Is this provision favorable?"

The skill should not invent a perspective. Ask: *"Favorable to whom — your side, the counterparty, or both?"* Then answer once perspective is given.

If the user's perspective is obvious from prior context (e.g., they've referred to the counterparty as "the vendor" throughout), the skill can default to "your side" and note the assumption.

### When the question is well-formed but the answer is "the contract doesn't address this"

This is a valid answer; do not pad it. *"The contract does not address what happens if a sub-processor is acquired. The closest provisions are §3.4 (sub-processor approval) and §10.2 (assignment), but neither resolves the scenario directly. The answer would depend on default contract law and the parties' course of dealing."*

This is itself a Type D scenario answer — just one where the document is silent.

## When the classification is wrong

If the user pushes back on the answer's shape ("that's too long" / "I just wanted a quick answer" / "I need more detail than that"), reclassify and re-answer. The user's feedback is the ground truth; the classifier is heuristic. A reclassification is not a failure; it's how the skill calibrates to the user.
