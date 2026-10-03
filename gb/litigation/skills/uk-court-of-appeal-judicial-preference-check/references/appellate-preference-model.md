# Appellate Preference Model

Use this reference when comparing a draft appellate document to public Court of Appeal decisions.

## What Counts as a Preference Signal

A preference signal is a pattern visible in public judgments or orders. It is not private psychology.

Acceptable:

- how a judge structures reasons in public judgments,
- how a case type is usually framed,
- whether recent decisions emphasise text, statutory structure, commercial consequence, discretion, or appellate restraint,
- treatment of authority hierarchy,
- tolerance or criticism of overlong factual narrative where visible in public reasons.

Prohibited:

- likely vote,
- temperament,
- ideology,
- private preferences,
- personal motivation,
- claims from gossip, directories, or model memory.

## Scope Labels

Use:

- `court_general` - supported across a general Court of Appeal sample.
- `case_type_specific` - supported in similar subject matter or procedural posture.
- `division_context` - civil, criminal, family, or specialist context.
- `judge_specific` - supported by multiple public decisions involving the named judge.
- `single_source_lead` - one useful public source; do not generalise.

## Corpus Selection

Record:

- sources searched,
- queries,
- date checked,
- reason for inclusion,
- reason for exclusion,
- court level,
- date range,
- subject-matter fit,
- author/panel where available.

For judge-specific observations, aim for multiple relevant public decisions. If only one is available, use `single_source_lead`.

## Draft Assessment Dimensions

Assess:

- issue framing,
- appellate error identification,
- ground-by-ground structure,
- fact-to-law ratio,
- authority hierarchy,
- statutory or contractual text anchoring,
- commercial pragmatism versus black-letter analysis,
- tone/restraint,
- treatment of adverse points,
- remedy/disposition.

## Argument Dependency

For key grounds, identify:

- proposition needed,
- authority relied on,
- citation verification status,
- proposition support status if checked,
- risk if authority/proposition fails.

Do not perform citation/proposition checking unless sources are available and the user asks or the skill invokes that workflow separately.

## Output Discipline

Every preference finding needs:

- dimension,
- observation,
- scope,
- confidence,
- supporting decisions,
- paragraph references,
- short excerpts,
- source URLs,
- uncertainty/corpus limits.

No-source mode may review internal structure only. It must not make source-backed preference findings.
