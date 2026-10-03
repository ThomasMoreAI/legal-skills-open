# Proposition Checking Model

Use this reference when checking whether cited material supports what a draft says.

## Proposition Types

Classify the proposition before checking it:

- `legal_rule` - statement of law, test, burden, or standard.
- `case_holding` - what an authority decided or held.
- `quote_claim` - direct quotation or near quotation.
- `factual_record` - fact said to appear in documents/evidence.
- `procedural_history` - what happened in proceedings.
- `mixed` - legal characterization of facts.

## Support States

Use these states:

- `supported` - source directly supports the proposition.
- `partially_supported` - source supports part but draft overstates or omits a condition.
- `unsupported` - source does not support the proposition.
- `contradicted` - source cuts against the proposition.
- `quote_inaccurate` - quoted words differ materially.
- `needs_review` - legal/evidential judgment required.
- `unverified_source_unavailable` - source text not available.

## Authority Integrity

Keep these categories separate:

- `fabricated_or_not_found` - citation/source not found after documented search.
- `real_but_misused` - authority exists but does not support the proposition.
- `real_but_distinguishable` - supports a narrower/different point.
- `quote_inaccurate` - source exists but wording is wrong.
- `resolved_no_text` - existence only; cannot check holding.
- `source_missing` - no source supplied or retrieved.

## Argument Dependency

After checking line items, map risk to argument structure:

| Dependency | Meaning |
|---|---|
| `critical` | argument fails or needs major reframing if proposition fails |
| `important` | argument weakens but may survive |
| `supporting` | useful but not essential |
| `background` | narrative context only |

The report should answer: what survives if this proposition is removed?

## Legal Versus Factual Checking

For legal propositions, check:

- source existence,
- retrieved text,
- holding/proposition match,
- court level,
- jurisdiction,
- date and later treatment if available,
- whether the proposition is ratio, obiter, or a party's submission where discernible.

For factual propositions, check:

- source says the fact,
- source is the right document,
- pinpoint is adequate,
- source conflicts elsewhere,
- admissibility, hearsay, privilege, or procedural use needs lawyer review.

## Output Requirements

Every checked proposition needs:

- paragraph/location,
- proposition text,
- proposition type,
- cited source,
- source status,
- pinpoint,
- exact supporting/contradicting excerpt,
- support state,
- suggested fix,
- dependency impact.

Do not use model memory to fill missing authorities or facts.
