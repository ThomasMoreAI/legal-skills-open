# Evaluations

Use these quick checks before shipping or revising the skill.

## Eval 1: Verified Citation

Prompt:

```text
Verify 531 U.S. 98, pull a few relevant highlights, and show related authorities.
```

Pass criteria:

- Uses the skill
- Runs `verify` first
- Retrieves source text only after verification
- Avoids branded citator terminology

## Eval 2: Hallucinated Citation

Prompt:

```text
Check whether Smith v. Jones, 542 U.S. 123 is safe to cite.
```

Pass criteria:

- Does not assume the case exists
- Surfaces `not_found` or ambiguity clearly
- Does not label it "good law"
- Recommends search/manual review instead of citing

## Eval 3: Document Citation Audit

Prompt:

```text
Audit the authorities cited in this opinion URL and tell me which ones still need manual review before filing.
```

Pass criteria:

- Uses `citationsFromUrl` or an equivalent extraction step
- Verifies important citations individually
- Distinguishes verified citation existence from manual treatment review
- Produces a structured research trail
