# Eval results for redfern-schedule

Method: each test case in `evals.json` was run twice, once with the skill and once against a clean baseline (a model with no access to the skill and no file access), then graded on the objective assertions in `evals.json`. This follows the Anthropic skill-creator methodology. There is no automated viewer here, so this is a written summary rather than the skill-creator's HTML benchmark.

## Outcome

With the skill, every assertion passed across all four cases (requesting, producing, tribunal, out-of-scope).

Against the clean baseline, the skill added clear value on the high-stakes behaviours:

| Behaviour | With skill | Clean baseline |
|---|---|---|
| Privilege gate fires first (eval 1) | Yes | No, skipped entirely |
| Tribunal decision left blank, nothing proposed (eval 3) | Yes | No, proposed a ruling ("granted, subject to redaction") and suggested decision wording |
| Discrete privileged flags memo of the user's own weak points (evals 1, 2) | Yes | Flags mixed into the served output |
| Objections paired with Article 9.5 measures, not flat refusal (eval 2) | Yes | More maximalist, flat "production refused" |
| Declines to invent an unpleaded relevance case (eval 1) | Yes | Invented comparator relevance theories |

Non-discriminating (a strong general model already handles these without the skill): flagging the "all documents concerning X" fishing request, routing a non-party document to Article 3.9, and asserting Article 9.2(f) on governmental content but not on a state-owned party's commercial pricing. The skill's value is therefore in discipline and structure (the gate, the no-decision rule for the tribunal, the privileged flags memo, the no-invention rule), not in supplying arbitration law a capable model already knows.

## Honest caveats

- The first run of the baselines was discarded: as filesystem-enabled agents they discovered the skill on disk and used it, so they were not true no-skill baselines. The table above uses re-run baselines with no file access.
- The eval-1 prompt did not state that the Claimant is the same party as the named licence counterparty, so neither run flagged that request under Gate C as "already held". The skill does catch this when the fact is explicit. This is an eval-prompt limitation, not a skill defect.
