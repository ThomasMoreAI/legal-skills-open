---
name: privilege-preflight-en-matematicsolutions
title: Privilege Preflight EN - prompt check before sending to cloud AI
description: 'Pre-flight check for legal content BEFORE it is sent to an external, cloud-based AI tool (browser chatbot, office-suite assistant, any API outside the firm''s control). Inventories what actually sits in the prompt, scores five risk factors (client identifiability, facts under professional secrecy, litigation strategy and work-product, third-party personal data, AI provider terms), returns a banded verdict SAFE / CAUTION / STOP with a factor table and a disclosure-impact assessment, and for CAUTION prepares a redacted draft of the prompt for human approval. Sends nothing, never performs the final redaction. Use when: "can I paste this into ChatGPT", "does this prompt breach privilege", "privilege check before AI", "what to redact", "is this safe to send to a chatbot", law firm prompt audit, disclosure impact assessment before using cloud AI.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/ai-governance/skills/privilege-preflight-en
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Privilege Preflight EN - prompt check before sending to cloud AI

## Philosophy

**A prompt pasted into someone else's chatbot is a disclosure. Not "tool usage" - a disclosure.**

No lawyer would fax a case file to a newspaper to get a second opinion on the
drafting style. Yet the same lawyer will paste half a statement of claim into a
free chatbot "just to polish the wording". The two acts differ less than it seems:
the content leaves the firm and lands with a third party, on terms nobody read,
with retention nobody controls, possibly on servers outside the EEA.

This skill does one thing: it holds the hand above the Enter key for the length of
one check. It does not ban cloud AI - firms use it and will keep using it. It
forces a conscious decision instead: what exactly leaves, to whom, on what terms,
and what happens if it ever surfaces.

The verdict is banded, not binary. Most prompts are neither clean nor forbidden -
they are redactable. That is why the middle band (CAUTION) ends with a redacted
draft rather than a lecture.

The frame here is European: legal professional privilege as shaped by the Court of
Justice of the EU, national professional secrecy regimes, GDPR, and the Trade
Secrets Directive. US attorney-client privilege appears only as a comparative
footnote, not as the operating framework.

## When to use / What it does NOT do

**Use it:**
- before pasting client-matter content into an external AI chatbot,
- for a firm-wide prompt audit (retrospective: what people have been sending),
- as the skeleton of an internal AI usage policy - the SAFE/CAUTION/STOP bands
  translate directly into policy tiers,
- when a colleague asks "can I put this into the chatbot" - run the preflight
  instead of answering from gut feeling.

**What it does NOT do (explicit negative scope):**
- it does NOT send anything anywhere - verdict and draft stay on the machine,
- it does NOT perform the final redaction - it prepares a redacted version as a
  draft; a human reads it, corrects it and decides alone whether to send,
- it does NOT assess the legal merits of the prompt (other skills do that),
- it does NOT replace a GDPR impact assessment for deploying an AI tool in the
  firm - that is `gdpr-dpia-en`; the preflight checks a single piece of content,
  not a process,
- it does NOT give guarantees - a SAFE band means "no risk factor found",
  not "I vouch that no risk exists".

## Legal bases (cite with a confidence tag)

Quote an article number only when it is certain. Otherwise describe the duty in
words and mark it `[TO VERIFY]`. Never invent a citation.

- **Legal professional privilege (LPP), EU law** - settled CJEU case law: AM&S
  v Commission (Case 155/79) recognised LPP for communications with independent
  external lawyers in EU competition investigations; Akzo Nobel v Commission
  (Case C-550/07 P) confirmed that in-house counsel communications are NOT
  covered by LPP in EU Commission competition proceedings. Practical consequence:
  in-house teams pasting internal legal analysis into a cloud tool cannot assume
  even the baseline EU-level protection external counsel would have.
- **National professional secrecy regimes** - in most continental systems secrecy
  is the lawyer's own enforceable duty (adwokat, Rechtsanwalt, avocat, abogado),
  broader in scope than a common-law evidentiary privilege and typically unlimited
  in time. The exact statutory basis differs per jurisdiction - identify the
  user's regime and mark specifics `[TO VERIFY]` per country.
- **GDPR** - personal data of the client and of third parties inside a prompt is
  processing: definition of personal data (Art. 4(1)), the AI provider as a
  processor requiring a data processing agreement (Art. 28), transfers outside
  the EEA (Chapter V).
- **Trade Secrets Directive (EU) 2016/943** - protection depends on "reasonable
  steps" to keep the information secret; pasting a client's trade secret into a
  public chatbot is an argument AGAINST reasonable steps and can weaken the
  client's own protection, independently of any privilege question.
- **Disciplinary and liability exposure** - breach of professional secrecy is a
  disciplinary offence under bar rules and may found civil liability towards the
  client; the concrete provision depends on the bar involved `[TO VERIFY]`.
- **Comparative footnote only:** US attorney-client privilege and work-product
  doctrine raise a parallel waiver debate, but this skill does not use them as
  its framework.

## The five assessment factors

Score each factor separately: CLEAN / CAUTION / CRITICAL.

**(a) Client identifiability.** Direct (company name, registration number, personal
names, case reference) AND mosaic: the combination of industry, city, dispute
amount and event date can point to one client even though no single element does.
Mosaic test: would a local journalist with a search engine work out who this is?

**(b) Facts under professional secrecy.** Everything the lawyer learned in
connection with providing legal assistance - including facts that look neutral
(the mere fact that a client seeks advice on a given matter is itself covered).

**(c) Litigation strategy / work-product.** Planned pleas, assessment of the
weaknesses of one's own position, negotiation tactics, internal notes on witness
credibility. This is the most dangerous category - disclosure harms even after
full pseudonymisation, because the value sits in the reasoning itself, not in the
identity of the parties.

**(d) Third-party personal data.** Witnesses, the opposing party, family members,
the client's employees. They chose no law firm and accepted no terms - the lawful
basis for processing their data in a cloud AI tool is usually the weakest link.

**(e) Where the prompt goes.** The AI provider's terms: is prompt content used for
model training, what is the retention period (and can it be switched off), where
are the servers, is there a transfer outside the EEA and on what basis, is there a
data processing agreement (Art. 28 GDPR), free tier or business tier (the terms
can differ radically). If the user does not know - assume the worst variant and
say so explicitly.

## Workflow (step by step)

### 1. Content inventory
Break the prompt into elements: who is named (entities, persons), which facts,
which figures and dates, which document fragments, whether it contains the
lawyer's own reasoning (assessment, tactics), and where the user wants to send it
(tool name and tier). No inventory, no assessment - "I roughly know what is in
there" does not count.

### 2. Score the five factors
Each factor (a)-(e) gets CLEAN / CAUTION / CRITICAL plus one sentence of
justification quoting the fragment that drives the score.

### 3. Banded verdict
The aggregation rule is mechanical:
- any factor CRITICAL -> **STOP**,
- factor (c) strategy/work-product at CAUTION or above -> **STOP** (redaction
  does not cure work-product - see the factor description),
- otherwise, at least one CAUTION -> **CAUTION**,
- all CLEAN -> **SAFE**.

### 4. Disclosure impact assessment
For CAUTION and STOP: two-three sentences on what concretely happens if the
content surfaces - towards the client (lost trust, harm to the matter), towards
the lawyer (disciplinary exposure, liability), towards third parties (GDPR
claims). No scaremongering - a realistic scenario.

### 5. Redaction - draft (CAUTION only)
Prepare a redacted version of the prompt: pseudonymise entities and values with
placeholders [CLIENT], [COUNTERPARTY], [PERSON-1], [AMOUNT], [DATE], [PLACE],
[CASE-REF]; delete fragments unnecessary for the prompt's purpose (the cheapest
redaction is deletion); re-run the mosaic test AFTER redaction - does the
combination of what remains still point to the client. For STOP, produce no
draft - a redacted litigation strategy is still a litigation strategy.

### 6. Alternatives (on STOP)
Always show a way forward, not only a prohibition:
- a local zero-cloud environment (data never leaves the firm's machine),
- a local model on the firm's own hardware,
- reformulating the question into an abstract one (ask about the rule, not the
  matter),
- doing the task without AI, if the stakes demand it.

### 7. Human gate
Present the result and stop. See the "Human gate" section.

## Output format (literal template)

```
## Privilege preflight - <working name of the prompt>

Prompt purpose: <what the user wants to achieve by sending it>
Target tool: <name + tier (free/business) or "unknown - worst case assumed">

| Factor                               | Score     | Justification (content fragment)      |
|--------------------------------------|-----------|---------------------------------------|
| (a) Client identifiability           | CAUTION   | company name + city + industry        |
| (b) Facts under secrecy              | CAUTION   | course of negotiations described      |
| (c) Strategy / work-product          | CLEAN     | no tactical assessment in the text    |
| (d) Third-party personal data        | CAUTION   | witness named in full                 |
| (e) Provider terms                   | CRITICAL  | free tier, training on user content   |

VERDICT: STOP

Disclosure impact: <2-3 sentences, realistic scenario>

Recommendation: <on STOP - alternatives; on CAUTION - draft below; on SAFE - clear to send>

--- REDACTED VERSION (draft, CAUTION only - requires human approval) ---
<content with placeholders [CLIENT], [AMOUNT], [DATE]...>
--- END OF DRAFT ---

Mosaic check after redaction: <passed / failed + why>
The decision belongs to a human. This skill has sent nothing.
```

## Human gate

The skill's output is a draft, not a decision. Nothing gets sent until an
authorised human has read the verdict, the factor table and - on CAUTION - the
entire redacted draft, line by line. The human approves, corrects or rejects;
sending is always the human's own act, performed outside this skill.

The governance boundary is hard: the skill prepares, the human executes. This
covers redaction too - an automatically inserted placeholder can miss the context
(e.g. [AMOUNT] inside a contract quote where the amount is the very subject of
the question). A draft nobody read is worthless and must never be treated as
"already anonymised".

The SAFE band passes through the gate as well: the human sees the factor table
and presses Enter personally. SAFE shortens the deliberation, it does not remove
the responsibility.

## Companion skills

- `matematic-prompt-defense-pl` - hardening of a system prompt against attacks;
  the preflight watches what leaves the firm, prompt-defense watches what can
  attack the firm's own AI. Two sides of the same hygiene.
- `gdpr-dpia-en` - data protection impact assessment for DEPLOYING an AI tool as
  a process; the preflight is a per-item check. If preflights for the same tool
  keep ending in CAUTION/STOP, that is the signal for a DPIA and a systemic
  decision, not for yet another round of redactions.
- `doc-intel-contract-pl` - when the content comes from a document: extraction
  with confidence gating and redaction candidates (PII with checksums) gives the
  preflight better input than raw copy-paste.
- `legal-request-router-pl` - routing of a legal task; the preflight can be its
  first stop before the router even picks a verification path.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the ai-governance plugin (AI governance)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

These skills run regulatory triage for organisations deploying or building AI: EU AI Act classification and role mapping, NIS2 scope and obligations triage, and a privilege pre-flight check before legal content is sent to an external AI surface. Each ends in a draft for decision, not a finished act.

### Rules

- **Output is a draft for decision.** A classification card, a scope assessment or a redacted prompt is a starting point for counsel / the compliance owner. A person approves and acts on it.
- **Governance boundary - the outward act stays human.** Registering an AI system, notifying a CSIRT or supervisory authority, filing a FRIA, sending anything to an external AI service - the skill prepares the draft, it does not perform the act.
- **Regulation from the source, not from memory.** Article references carry confidence tags; anything uncertain is marked for verification against EUR-Lex (eu-sparql-search / mcp-eu-compliance connectors) or the national transposition before it is relied on. National transposition status changes - always check it at time of use.
- **Triage is not a conformity assessment.** These skills classify, map and flag. A high-risk or GPAI finding routes to a human and a full assessment; it is never the end of the analysis.
- **Not legal advice.** The skills organise obligations and map them to provisions; they do not replace legal analysis of a specific matter.
- **Confidentiality.** System descriptions, incident details and prompt content are confidential - do not move them outside the agreed flow. These skills add no outbound channel of their own; what reaches your model is decided by your configuration (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md).

### Plugin scope

Regulatory triage for AI and cyber (AI Act, NIS2) plus prompt-level privilege hygiene. It does not verify citations or fetch sources of law - use `verification-foundation` and `eu-law-sources` for that. GDPR operations (DPIA, breach, DSAR) live in `data-protection`; the AI Act triage pairs with `gdpr-dpia-en` when a system processes personal data.
<!-- shared-rules:end -->
