# Expansion Patterns

Different categories of legal work have different implicit elements. This reference catalogs the common gaps and the typical fixes for each category.

These are patterns, not formulas. Apply judgment — the goal is to surface what is implicit in the user's specific prompt, not to mechanically apply a template.

## Contract Review

**Common gaps:**
- Perspective (which side are we on?)
- Scope (full review vs. specific issue check)
- Output format (memo, table, list of issues with severity)
- Citation expectations (cite specific clauses or just identify issues?)

**Typical expansion moves:**
- "Review this contract" → "As in-house counsel, review this contract from [perspective]'s perspective. Identify [scope]. Cite specific clauses for each finding. Output as [format]."
- "What should I watch for" → "Identify the most material issues from [perspective]'s perspective, ordered by severity. For each, briefly state the issue, the relevant clause, and why it matters."
- Beware: do not insert specific severity rubrics (those belong in skills). Use generic "ordered by severity" without prescribing the criteria.

**Skip when:** an attached skill already handles contract review (e.g., NDA Review, MSA Review). The skill's scope supersedes.

## Drafting

**Common gaps:**
- Audience (who reads this?)
- Tone (formal, plain-language, casual)
- Length (one paragraph, one page, multi-page memo)
- Specific elements to include or exclude
- Citations or supporting authority requirements

**Typical expansion moves:**
- "Draft a clause for X" → "Draft a [type] clause covering [substance]. Audience is [audience]. Tone should be [formal/plain-language]. Include [elements]. Length: [target]."
- "Write a response to opposing counsel" → "Draft a [letter/email] in response to opposing counsel's [topic]. Tone: [professional but firm / cooperative / declining]. Length: [target]. Address the following points: [carry over user's substantive points]."
- Beware: drafting prompts often have an unspoken adversarial posture. Surface it — "favorable to us as [party]" or "neutral and balanced" — rather than letting the model guess.

## Research

**Common gaps:**
- Jurisdiction
- Depth (quick orientation vs. comprehensive analysis)
- Source preferences (statutes, cases, regulatory guidance, secondary sources)
- Time horizon (current law, historical evolution, pending changes)

**Typical expansion moves:**
- "What does the law say about X" → "Summarize the current law on [topic] in [jurisdiction]. Include [statutes, leading cases, regulatory guidance] as applicable. Note any pending changes or recent developments. Output as a brief memo with citations."
- "Is X allowed" → "Analyze whether [activity] is permitted under [jurisdiction] law. Identify the applicable [statutes/regulations], any leading cases, and any meaningful exceptions or conditions. State whether the answer is settled or contested."
- Beware: never frame research expansions in a way that asks the model to give a definitive legal opinion. Use "summarize the law on" or "analyze how courts have treated," not "what is the answer to."

## Advice / Analysis

**Common gaps:**
- The decision to be made (what is the user trying to decide?)
- Stakeholder context (who is asking, what do they need?)
- Confidence level needed (rough orientation vs. thorough analysis)

**Typical expansion moves:**
- "Should we do X" → "Analyze the legal considerations involved in [doing X]. Identify the key risks, the magnitude of each, and any mitigating steps. Frame the analysis as input to a business decision, not as a legal opinion. Output as a brief memo with sections for [risks / considerations / recommendations]."
- "What are the risks" → "Identify the [legal/regulatory/contractual] risks associated with [activity]. For each, state the nature of the risk, the likelihood of it materializing, and the magnitude if it does. Distinguish risks that have a clear legal answer from those that turn on factual or business judgments."
- Beware: do not insert risk-tolerance assumptions. The user owns the risk-tolerance call.

## Translation / Simplification

**Common gaps:**
- Audience (board? employees? customers?)
- Constraints (preserve precision vs. prioritize accessibility)
- Length

**Typical expansion moves:**
- "Make this simpler" → "Rewrite the following in plain language for a [audience] audience. Preserve the substantive meaning while removing legal jargon, qualifying clauses, and unnecessary hedging. Target length: [comparable / shorter]."
- "Summarize this" → "Produce a brief summary of [document] for [audience]. Length: [target]. Focus on [decisions / obligations / risks / takeaways]."

## Triage / Quick Orientation

**Common gaps:**
- The triage criterion (what is the user looking for? deal-breakers? unusual provisions? overall posture?)
- Time budget (this signals depth)

**Typical expansion moves:**
- "Quick look at this" → "Provide a 2-minute orientation on this [document/situation]. Identify the type of [document/issue], the key terms, anything unusual or notable, and a one-line bottom line."
- "Anything I should worry about" → "Skim this [document/situation] for material issues. Surface anything that warrants my attention; skip anything routine. Be concise — bullets, not memos."

## Always Apply

Across all categories, certain expansions apply broadly:

- **Default role:** in-house counsel for legal prompts; subject-matter expert for non-legal prompts.
- **Default constraint:** "Output is a draft for human review, not a final legal opinion." Always include for prompts that produce legal advice.
- **Default citation behavior:** "Cite specific [clauses/statutes/cases] where relevant; do not invent citations." For document-based prompts.
- **Preserve user-stated constraints:** if the user said "in two paragraphs" or "without legalese," carry that through verbatim. Do not "improve" their constraints.

## When in Doubt

A short, clear prompt is better than a long, busy expansion. If the gaps you would surface are minor or the prompt is already adequate, skip rather than expand. The user's tolerance for friction is finite; preserve it for prompts where expansion genuinely helps.
