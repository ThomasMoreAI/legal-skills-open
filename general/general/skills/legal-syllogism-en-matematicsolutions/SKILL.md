---
name: legal-syllogism-en-matematicsolutions
title: Legal syllogism - make the reasoning explicit
description: 'Builds the explicit legal syllogism for an issue - lays out the major premise (the rule and its interpretation), the minor premise (the material facts), the application (subsuming facts under each element of the rule), and the conclusion, then flags the weak links: unstated assumptions, contested facts, debatable interpretation. Forces every step to be said out loud and checkable instead of jumping from facts to a holding. Maps to civil-law subsumption and common-law IRAC/CREAC. Jurisdiction-neutral method: it supplies no rule and checks no citation, so the major premise has to come from a source you trust. Use when: "build the syllogism", "lay out the legal reasoning", "apply the rule to the facts", "IRAC this", "where is the gap in the argument", "major and minor premise", "structure the analysis" - when drafting an opinion, brief, or memo.'
author: matematicsolutions
author_url: https://github.com/matematicsolutions/awesome-matematic-skills-en/tree/main/verification-foundation/skills/legal-syllogism-en
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Legal syllogism - make the reasoning explicit

## Philosophy

**A flawed opinion rarely fails at the conclusion - it fails at the premise nobody stated.** Legal
reasoning is a syllogism: the rule (major premise), the facts (minor premise), the application, and
the conclusion. When a step is left unsaid - "because it's obvious" - that is where the gap hides,
and that is where the other side, or the court, will strike. This skill forces each step to be
stated and marks what is settled and what is contested.

It **structures** the reasoning; it does not decide the case. Judgement and the decision stay with
the lawyer.

## Method (subsumption / IRAC)

1. **Major premise (rule + interpretation)** - identify the governing rule, then its reading: how
   each element of the rule is construed (text, structure, purpose). Note where authority or
   commentary splits.
2. **Minor premise (material facts)** - list the facts that matter to the rule's elements. Separate
   undisputed facts from contested ones, and facts from characterisations.
3. **Application (subsumption)** - for each element of the rule, show which fact satisfies it (or
   does not). This is the real work: matching fact to element.
4. **Conclusion** - the legal consequence that follows from the application.
5. **Weak-link test** - mark which elements are contested in interpretation, which facts are
   contested on the evidence, and which assumptions were made silently. This is the map for
   adversarial-legal-review-en.

## Output format

```
ISSUE: <the legal question>

MAJOR PREMISE (rule): <provision/authority> - "<elements>"
  Interpretation: <how the elements are read; any split in authority>

MINOR PREMISE (material facts):
  - undisputed: <...>
  - contested (evidence): <...>

APPLICATION (element -> fact):
  - <element 1> : satisfied by <fact> | NOT satisfied | contested
  - <element 2> : ...

CONCLUSION: <legal consequence>

WEAK LINKS (for adversarial-legal-review-en):
  - interpretation: <which element is contested and why>
  - facts: <what needs proof>
  - silent assumptions: <...>
```

## Limits

- The syllogism orders reasoning - it does not perform interpretation or fact-finding. Whether the
  rule, its reading, and the facts are right is for the lawyer.
- It does not weigh competing arguments (that is adversarial-legal-review-en) - it arranges them so
  attack and verification have something to work on.
- Subsumption assumes a rule with elements. For open-textured standards and the balancing of
  principles, a pure syllogism is not enough - mark it as balancing, not subsumption.

## Attribution

The legal syllogism (subsumption; IRAC/CREAC) is a classical method of legal reasoning. The idea of
an explicit syllogism scaffold for AI is inspired in part by **Fuzi.Mingcha** (irlab-sdu) - without
using its code or models. Rules, format, and framing are MateMatic's own. MateMatic interpretation,
not the position of any bar or regulator.

<!-- shared-rules:begin (generated from ../../SHARED-RULES.md by scripts/shared-rules-sync.py - do not edit here) -->
## Shared rules of the verification-foundation plugin

These rules apply to every skill in this plugin, including where the skill itself is silent. They are copied into each skill, so they hold whether you install the whole plugin or a single skill.

### Five layers of protection (before any disclaimer)

1. **Source verification** - provisions and case law from databases, not the model's memory.
2. **Confidence class** - every legal claim marked: verified / check / do not use.
3. **Premise check** - facts from the user are tested before analysis.
4. **Explicit negative scope** - each skill states what it does NOT do.
5. **Human gate** - a qualified person reviews and approves the output.

If an error would pass without being stopped by layers 1-5, the fault is in the skill. Fix the tool, do not add a note. "This is not legal advice" stops no error and transfers no responsibility.

### Confidence tags

- **Verified** - source checked in this session, with a full identifier: `(GDPR Art. 6)`, `(Case C-311/18, CJEU)`.
- **Check** - plausible, unverified: `[check on EUR-Lex]`.
- **Do not use** - an invented case number or provision. Omit it, never fabricate.

The tag sits next to the line it concerns. A case number that exists is not enough - check the content.

### Human gate

Nothing is sent, filed, signed or published before a qualified person checks and approves it. A skill output is a draft, not a finished document.

### Scope

The verification foundation is jurisdiction-neutral - the method, not the substance of any one legal system. It connects to no external source (no MCP connectors) and makes no outbound calls of its own; what you type still goes to your configured model (see https://github.com/matematicsolutions/awesome-matematic-skills-en/blob/main/TRUST.md). Substance comes from separate plugins (eu-law-sources). Deep national law (e.g. Polish case law) lives in the Polish marketplace, by design.
<!-- shared-rules:end -->
