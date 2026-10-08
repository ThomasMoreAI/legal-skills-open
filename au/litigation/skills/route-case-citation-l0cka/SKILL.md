---
name: route-case-citation-l0cka
title: Route Case Citation
description: Parse an Australian case citation — medium-neutral, reported or bare case name — identify the issuing court and jurisdiction, and route the request to the matching official-source verification skill. Use first whenever a user asks to verify, check or confirm an Australian case citation, judgment or authority, including checking documents for fabricated or hallucinated citations. Do not use for non-Australian citations, treatment analysis (overruled, followed, distinguished), or substantive legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/route-case-citation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: litigation
language: en
---

# Route Case Citation

Read [../../references/case-law-verification-method.md](../../references/case-law-verification-method.md)
before routing. It defines the citation grammar, the official-source
hierarchy and the five-outcome result semantics every downstream skill uses.

Routing is deterministic because a medium-neutral citation names its issuing
court. This skill only identifies where verification must happen; it never
declares a citation verified.

## Workflow

1. Extract every citation from the request or supplied document. Accept
   medium-neutral citations (`[2023] HCA 12`), reported citations
   (`(2020) 94 ALJR 1`) and bare case names (`Smith v Jones`).
   - When command execution is available, use the bundled parser:

     ```bash
     python3 <skill-root>/scripts/parse_citation.py "[2023] HCA 12" "(1992) 175 CLR 1"
     ```

     Resolve `<skill-root>` as the directory containing this `SKILL.md`. The
     parser is offline and read-only: it reports citation type, court and the
     verification route, and proves nothing about whether the decision
     exists. Without command execution, apply the same grammar manually.
2. Route each citation.
   - `HCA`, and `CLR`/`ALJR` reported citations → `verify-hca-judgment`.
   - NSW court and tribunal identifiers (`NSWSC`, `NSWCA`, `NSWCCA`,
     `NSWDC`, `NSWLEC`, `NSWCATAP`, …) and `NSWLR` → `verify-nsw-judgment`.
   - `FCA`, `FCAFC`, `FedCFamC…`, `FCCA`, `FamCA`, `FamCAFC` and `FCR` →
     `verify-federal-judgment`.
   - Recognised but unsupported courts (Victoria, Queensland, WA, SA,
     Tasmania, ACT, NT) → report `UNVERIFIABLE` for that citation, name the
     court's own website as the manual check, and say the jurisdiction is not
     yet supported.
   - A bare case name with no citation → route by any stated court or
     jurisdiction; if none, ask which court decided it or search the most
     plausible official publisher and say which was searched.
3. For an unrecognised report series, state that the series cannot be
   resolved from free official sources and route the underlying decision by
   court if the court is identifiable, otherwise report `UNVERIFIABLE`.
4. Hand each routed citation to its verification skill and consolidate the
   results in one table when more than one citation was checked.

## Result contract

For each citation report:

```text
Citation: <as supplied>
Citation type: <medium-neutral / reported / case name / unknown>
Issuing court: <court or not established>
Jurisdiction: <jurisdiction or not established>
Route: <verification skill, manual official source, or none>
Routing note: <resolution steps or unsupported-jurisdiction statement>
```

Routing itself never outputs `VERIFIED`. Only a verification skill that
inspected the official publisher may do that.

## Fail closed

When the citation is malformed, the court identifier is unknown, or the
request depends on a jurisdiction this plugin does not support, say so and
route to a manual official source. Never guess a court from a case name
alone, and never treat a routing result as evidence the decision exists.
