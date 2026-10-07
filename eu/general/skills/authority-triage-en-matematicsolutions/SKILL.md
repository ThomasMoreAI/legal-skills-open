---
name: authority-triage-en-matematicsolutions
title: Authority Triage EN - route the source before the answer
description: 'Routes source authority BEFORE a legal answer is generated - maps an EU or member-state legal question onto source layers (EU primary law, general principles, Charter, regulations, directives with transposition check, decisions, CJEU case law, national constitution-statute-regulation chain, national apex courts, soft law from EDPB/ESMA/EBA), sets the verification order, checks collision rules and points to the right MCP connector for each layer. Use when: "where do I check this", "what is the source hierarchy", "which source prevails", "where do I start the research", "map the sources for this question", before any legal research without one obvious source.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/eu-law-sources/skills/authority-triage-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: eu
practice: general
language: en
---

# Authority Triage EN - route the source before the answer

## Philosophy

Before a legal answer exists, you need to know which source controls it.
A model that starts from the conclusion and then shops for a provision works
in the wrong order - first the layer map, then the research, then the thesis.

This skill is the layer BEFORE grounding. Three skills, three jobs:

- **authority-triage-en** (this skill) says WHERE to look and IN WHAT ORDER,
- **citation-grounding-pl** verifies WHETHER a quote and citation are real,
- **legal-request-router-pl** decides WHAT level of control the result gets.

The skill gives no legal advice. It produces a source map and a verification
order. The output is a draft that goes through the human gate.

## When to use

- An EU or member-state legal question with no single obvious source
  ("can a controller...", "is this clause enforceable...", "what sanctions
  apply under...").
- The user asks directly: where to check this, what prevails, where to start,
  what the hierarchy is.
- Before firing connectors - so queries follow the layer order instead of
  hitting databases at random.
- Whenever a directive may be in play (transposition status changes the
  answer) or two instruments may collide.

## What it does NOT do

- Does not verify quote content or citation existence - that is
  citation-grounding-pl.
- Does not assess stakes or pick a control path - that is
  legal-request-router-pl.
- Does not answer the legal question on the merits - it delivers a map,
  not a conclusion.
- Does not fetch sources itself - it names the connector, the connector fetches.
- Does not resolve a national-constitution vs EU-primacy standoff - that
  collision is flagged to the human.

## Layer map

### Layer 1 - EU primary law

| # | Source | Notes |
|---|---|---|
| 1 | Treaties (TEU, TFEU) | the constitutional frame of the EU legal order |
| 2 | Charter of Fundamental Rights | same rank as the Treaties (Art. 6(1) TEU); binds member states when implementing EU law (Art. 51 CFR) |
| 3 | General principles of EU law | proportionality, legal certainty, legitimate expectations, effectiveness - developed by the CJEU |

### Layer 2 - EU secondary law

| Instrument | How it binds | Research consequence |
|---|---|---|
| Regulation | directly applicable in all member states, no transposition | read the regulation itself; national law only fills opening clauses |
| Directive | binding as to result; member states transpose | ALWAYS run the transposition check: which national act implements it, was the deadline met; after the deadline, vertical direct effect is possible if the provision is clear, precise and unconditional |
| Decision | binding on its addressees | check who the addressee is before citing it against anyone else |

Primacy: on collision between national law and EU law, EU law prevails
(Costa v ENEL, 6/64); direct effect since Van Gend en Loos (26/62).
A collision between EU law and a national constitution is not resolved
here - flag it to the human.

### Layer 3 - case law

| Court | Authority status |
|---|---|
| CJEU | interpretation of EU law binds national courts; preliminary rulings under Art. 267 TFEU; no formal stare decisis, but settled case law controls in practice |
| National apex courts | supreme / cassation courts and constitutional courts; authority without formal precedent in most civil-law systems - weigh whether the ruling is an isolated decision or a settled line |
| ECtHR | binds the respondent state in the case; the Strasbourg line steers ECHR interpretation across all parties |

### Layer 4 - national chain

For every member state involved, map the same chain:
constitution -> statutes -> executive regulations -> local acts.
Internal administrative acts bind the administration, not the citizen.
The exact chain is national - if the member state is unknown, ask; if the
national provision cannot be confirmed in a database this session, tag it
[TO VERIFY].

### Layer 5 - soft law (not a source of law; reliance on it can shield the addressee)

| Instrument | Body |
|---|---|
| Guidelines, opinions, binding decisions under Art. 65 GDPR | EDPB |
| Guidelines, Q&As, technical standards drafts | ESMA |
| Guidelines, opinions, Q&As | EBA |
| National regulator guidance | e.g. data-protection and financial-market authorities |

Soft law never wins a collision with a statute or a regulation. Cite it as
regulator practice, clearly separated from the norm.

## Workflow

1. **Classify the question into layers.** Which layers can control the
   answer? Usually 2-3 (e.g. GDPR: EU regulation + national act filling the
   opening clauses + EDPB guidelines + CJEU case law).
2. **Set the verification order.** Top layer down: the higher norm frames the
   question before you read the implementing act or regulator practice.
   Soft law is read LAST, against the norm.
3. **Check collisions.** Rules: lex superior, lex specialis, lex posterior
   (but a later general norm does not displace an earlier special one) plus
   EU primacy over national statutes. For directives, the collision check
   includes the transposition gap: national act missing, late or defective.
   A collision the rules cannot close goes to the human gate.
4. **Point to the connector for each layer:**

   | Layer | Connector |
   |---|---|
   | EU law, CJEU case law (EUR-Lex / Cellar) | eu-sparql-search |
   | National legislation (ELI) | national *-eli-mcp from the MateMatic line (e.g. sejm-eli-mcp for PL) |
   | EU digital / data / cyber compliance acts | mcp-eu-compliance |
   | French legislation and codes | mcp-fr-legal |
   | German legislation | mcp-de-legal [TO VERIFY availability - pre-release] |

5. **Flag the temporal version.** Three questions, every time:
   - law as of the DATE OF THE EVENT or as of today? (dispute research =
     version in force at the event; compliance = version in force now),
   - vacatio legis / application date - EU acts often split entry into force
     and date of application (the GDPR pattern: in force 2016, applying 2018),
   - transitional provisions - does the old norm still govern pending cases.

## Output format

Return exactly this template:

```markdown
# Source map: [the question in one sentence]

Law as of: [event date / today - justify the choice]
Member state(s): [list or "EU level only"]

| Layer | Act / source | Connector | Verification status | Flags |
|---|---|---|---|---|
| EU primary | [treaty / Charter article] | eu-sparql-search | verified / to check | [Art. 51 CFR scope?] |
| EU secondary | [regulation / directive / decision + article] | eu-sparql-search / mcp-eu-compliance | verified / to check | [transposition? direct effect? application date?] |
| CJEU | [case, e.g. C-xxx/xx] | eu-sparql-search | to check | [settled line or isolated ruling?] |
| National statute | [act + article] | *-eli-mcp / mcp-fr-legal (DE: [TO VERIFY availability]) | verified / to check | [temporal version, vacatio legis] |
| National courts | [apex court ruling] | national connector / manual | to check | [authority without precedent] |
| Soft law | [EDPB / ESMA / EBA guideline] | manual | to check | [not a source of law] |

## Verification order
1. [source] - because [hierarchy rule]
2. ...

## Collisions
[lex superior / specialis / posterior / EU primacy / transposition gap -
or "none detected"; unresolvable collision -> human gate]

## Temporal flags
[provision version, vacatio legis / application date, transitional rules -
or "none"]

## For the human gate
[what needs a lawyer's decision before an answer is generated]
```

Any article number not confirmed in a database this session gets the
[TO VERIFY] tag - never present a number from memory as certain.

## Human gate

The source map is a research draft, not a legal answer. A qualified human:

- approves the temporal choice (event date vs today),
- resolves collisions the rules cannot close (especially national
  constitution vs EU primacy),
- judges whether a case-law line is current,
- takes responsibility for the answer built on this map.

Nothing goes to a client on the strength of the map alone.

## Companion skills

- **citation-grounding-pl** - next step: verify that fetched quotes and
  citations are real.
- **legal-request-router-pl** - the layer above the result: which control
  path (plain answer / grounding / adversarial debate / audit bundle).
- **saos-orzecznictwo**, **eu-sparql-search** - the connectors this map
  routes to.
- **legal-data-hunter-pl** - when a layer has no connector and a data source
  must be found first.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the eu-law-sources plugin (EU law sources)

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

### Sources, not memory

This plugin searches and fetches EU law (legislation and CJEU case law) through an MCP connector (read-only, public EUR-Lex / Cellar SPARQL). Every legal claim belongs to a class:

- **Verified** - confirmed in the database, with an identifier: `(Case C-311/18, CJEU)`, `(CELEX 32016R0679)`.
- **Check** - plausible, not yet confirmed: `[verify on EUR-Lex]`.
- **Do not use** - a CELEX or case number with no match. Omit it, never fabricate.

A case number that exists is not enough - check that the judgment decides what you cite. Whether case law is still good law is a human assessment.

### Connector in this plugin

`.mcp.json` declares the EU SPARQL connector (EUR-Lex / Cellar, read-only, public data). It needs `node`/`npx` in the environment. This is EU-level, language-neutral law - national law of a specific member state is out of scope here.

### Human gate

Output is a draft for review. Nothing is sent or filed before a qualified person checks it and takes professional responsibility.
<!-- shared-rules:end -->
