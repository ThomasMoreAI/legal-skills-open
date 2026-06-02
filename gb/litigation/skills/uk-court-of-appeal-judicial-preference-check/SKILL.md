---
name: uk-court-of-appeal-judicial-preference-check
title: uk-court-of-appeal-judicial-preference-check
description: Use when users say "check this Court of Appeal skeleton", "judicial preference check", "CoA style", "is this too factual", "commercial vs black letter", or need England and Wales appellate drafts tested against public-source Court of Appeal drafting and judicial preference signals.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/uk-court-of-appeal-judicial-preference-check
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: litigation
language: en
tags: [court-of-appeal, skeleton-arguments, grounds-of-appeal, judicial-preferences, legal-writing]
---

# uk-court-of-appeal-judicial-preference-check

## When to Use

- A user wants to test a draft against Court of Appeal style, expectations, and public-source judicial preference signals.
- The document is a skeleton argument, grounds of appeal, respondent's notice, written submission, judgment-style memo, or appellate advice.
- A panel or likely judge is known and the user wants source-backed drafting signals.
- The user asks whether the draft reads too factual, too doctrinal, too aggressive, too long, too authority-heavy, too commercial, too black-letter, or insufficiently appellate.

This skill identifies source-backed drafting tendencies and judicial preference signals visible in public decisions. It does not predict votes, infer private judicial psychology, or replace counsel's advocacy judgment.

## Audience and Work Shape

Audience: experienced appellate counsel, litigation solicitors, and supervised appellate teams drafting or reviewing England and Wales Court of Appeal materials.

Work shape: pattern-matched review of a draft against a public-source corpus, producing accretive judgment for counsel. It is not a transactional output and not for unsupervised self-represented use.

## Legal Failure Modes

- Legal support, not legal advice: the output is drafting-signal analysis, not advocacy strategy or merits advice.
- Privilege/confidentiality: the draft may be privileged work product; use only approved environments and avoid unnecessary client-identifying detail in public-source searches.
- Accountability: counsel owns the final drafting choices and any decision to adopt, reject, or ignore a signal.

## Access Modes

This skill works in three modes:

1. **Live source mode** - use browser, web search, MCP, API, or other configured access to retrieve public Court of Appeal decisions from Find Case Law, BAILII, court pages, or equivalent public sources.
2. **User-supplied source mode** - use public judgments, URLs, PDFs, HTML, screenshots, exports, or pasted text supplied by the user.
3. **No-source mode** - review the draft's internal appellate structure and prepare a research plan, but do not make source-backed judicial preference findings.

If public decisions cannot be retrieved or supplied, do not infer preferences from model memory. Ask for decisions, URLs, exports, or source access. Judge-specific findings require an actual public-source corpus.

## Inputs Needed

Confirm:

- Document type and procedural stage.
- Civil, criminal, family, or specialist Court of Appeal context.
- Grounds or issues on appeal.
- Known or possible panel, if any.
- Key authorities and lower-court decision.
- Whether the user wants court-wide style, case-type style, division/context style, or judge-authored-public-decision style.

If the panel is unknown, do not invent judge-specific preferences. Work at court-wide or case-type level.

## How It Works

### 1. Build a public-source corpus

Use retrieved public decisions, preferably:

1. The National Archives Find Case Law.
2. BAILII.
3. Court or judiciary pages.
4. User-supplied public decisions.

For each included decision, record:

| Field | Meaning |
|---|---|
| `case_name` | decision name |
| `neutral_citation` | citation |
| `court` | Court of Appeal division/context |
| `date` | judgment date |
| `judge_or_panel` | author and panel where available |
| `source_url` | public URL |
| `date_checked` | retrieval date |
| `reason_for_inclusion` | same judge, same area, same procedural posture, recent CoA sample, etc. |

Do not rely on model memory for judgment content. If no public-source corpus can be retrieved or supplied, stop and ask for sources.

### 2. Extract public-source preference signals

Look for source-backed patterns:

- Structure: issue-first, chronology-first, ground-by-ground, or principle-then-application.
- Factual narrative: short appellate summary versus detailed factual retelling.
- Authority treatment: few controlling cases versus broad survey; treatment of first-instance authorities; statute-first or case-law-first reasoning.
- Appellate standard: respect for evaluative judgment, error of law framing, reasons challenge, discretion challenge.
- Tone: restraint, directness, criticism of overstatement, treatment of allegations.
- Commercial pragmatism versus black-letter doctrinal analysis.
- Treatment of procedural history and orders.
- Remedy/disposition framing.
- Treatment of policy, context, or practical consequences.

Every finding must cite specific decisions, paragraph references, short excerpts, and URLs.

### 3. Classify the scope of each signal

Use:

- `court_general` - supported across a general Court of Appeal sample.
- `case_type_specific` - supported in the same subject-matter or procedural type.
- `division_context` - supported in civil, criminal, family, or specialist context.
- `judge_specific` - supported by multiple public decisions authored by or materially involving the named judge.
- `single-source-lead` - interesting but not enough to generalise.

Judge-specific observations require multiple relevant public decisions. Frame them as public writing and reasoning signals, not personality traits or outcome predictions.

## Confidence Bands

- High: multiple closely comparable public decisions support the signal, with paragraph references and excerpts.
- Medium: limited but relevant public corpus supports the signal.
- Low: single-source lead, weak comparator fit, unknown panel, or conflicting corpus signals.

### 4. Profile the draft

Assess:

- Opening structure and issue framing.
- Whether grounds are separated cleanly.
- Whether the draft identifies the alleged appealable error.
- Ratio of facts to issues to law to relief.
- Authority load and hierarchy.
- Length, repetition, and signposting.
- Treatment of adverse points.
- Remedy sought and practical disposition.

Record locations by paragraph, heading, page, or section.

### 5. Compare draft to the source-backed signals

For each mismatch, explain:

- The draft feature.
- The public-source signal.
- Why the mismatch matters in Court of Appeal advocacy.
- A revision direction, not a ghostwritten replacement unless the user asks.

Examples:

- "The draft spends 8 pages on factual chronology before identifying the appealable error; the comparator decisions state the issue in the first two pages."
- "The authority section surveys first-instance cases, but the comparator CoA decisions in this area move from statute to leading appellate authority to application."
- "The draft presses commercial common sense, but the judge-specific sample is more text-and-structure oriented in this statutory context. Confidence: medium; corpus: 3 decisions."

## Output Schema

```yaml
court_context:
  document_type: skeleton | grounds | respondent_notice | memo | submission | other
  court: Court of Appeal
  context: civil | criminal | family | specialist | unknown
  procedural_stage: string
  known_panel_or_judges:
    - name: string
      status: known | possible | unknown

source_corpus:
  sources_searched:
    - source: string
      query: string
      date_checked: string
  included_decisions:
    - case_name: string
      neutral_citation: string
      date: string
      judge_or_panel: string
      source_url: string
      date_checked: string
      reason_for_inclusion: string
  corpus_limits:
    - string

preference_findings:
  - dimension: structure | concision | factual_narrative | authorities | issue_framing | commercial_pragmatism | doctrinal_analysis | tone | remedies | appellate_standard
    observation: string
    scope: court_general | case_type_specific | division_context | judge_specific | single-source-lead
    confidence: low | medium | high
    supporting_sources:
      - case_name: string
        neutral_citation: string
        paragraphs: string
        excerpt: string
        source_url: string
    uncertainty: string

draft_assessment:
  strengths:
    - location: string
      point: string
      source_linked_reason: string
  risks:
    - location: string
      issue: string
      severity: critical | major | minor | verify
      why_it_matters: string
      supporting_preference_finding: string
      suggested_revision_direction: string

research_limits:
  - string

legal_safety:
  not_legal_advice: true
  outcome_prediction: prohibited
  citation_verification_status: style_sources_only | separately_verified | not_verified
```

## Guardrails

- Use retrieved public sources or user-supplied public decisions only.
- Do not invent authorities, quotations, paragraph references, or judicial preferences.
- Do not claim to know a judge's psychology, temperament, ideology, private preferences, likely vote, or motivations.
- Do not treat one decision as a stable preference. Use `single-source-lead`.
- Distinguish court-wide practice, case-type tendency, and judge-specific public-writing pattern.
- Treat absence of evidence as a research gap, not proof of tolerance or intolerance.
- If a preference finding depends on a named judge, state the corpus size and dates.
- Keep citation verification and proposition checking separate; invoke those skills if the issue is whether authorities exist or support propositions.

## Escalation

Stop and redirect when the target court is not the Court of Appeal of England and Wales, including UKSC, Privy Council, Inner House, NICA, tribunals, or foreign appellate courts. If public-source signals conflict across the corpus, report the split rather than averaging them. If the user asks for outcome prediction, refuse and reframe as drafting-signal analysis.

## Example

```text
Check this draft Court of Appeal skeleton against recent public CoA decisions in commercial cases, especially any decisions by the listed panel. Identify whether the draft is too factual, too doctrinal, too long, or misaligned with public judicial preference signals. Cite every finding to public decisions.
```

For a compact output pattern, see `examples/output.md`.
For corpus selection, scope labels, and appellate preference signal rules, see `references/appellate-preference-model.md`.

## Limitations

- Public decisions show judicial writing and reasoning, not private preferences.
- Published judgments are not the same genre as skeleton arguments, so comparisons are drafting signals only.
- Panel composition, case type, procedural posture, and issue complexity can outweigh style tendencies.
- This skill does not predict outcome.
