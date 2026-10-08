# Bar-benchmark question bank

Original, self-authored items shaped like the New York bar components. See `../SKILL.md` for
what the score means (a regression gate and uplift instrument, not a bar-passage prediction).

## Set file

```jsonc
{
  "set": "mbe-civil-procedure",
  "title": "MBE-style — Civil Procedure",
  "component": "mbe",            // mbe | nyle | mpre | mee
  "jurisdiction": "multistate",  // multistate | NY
  "questions": [ … ]
}
```

## MCQ item

| Field | Rule |
|---|---|
| `id` | `MBE-<SUBJ>-NNN`, `NYLE-<SUBJ>-NNN`, `MPRE-NNN`; unique across all sets |
| `subject`, `area` | Subject, then the tested sub-topic |
| `type` | `mcq` |
| `difficulty` | `remember` / `application` / `analysis` |
| `q` | Fact pattern and call of the question; must not leak the answer |
| `choices` | Exactly `A`–`D`; no all/none-of-the-above |
| `answer` | The key letter |
| `cite` | Controlling statute, rule, or case (name + court + year; reporter only when certain) |
| `why` | Why the key is right and each distractor wrong |
| `ref` | `legal-doctrine/reference/<file>.md` that should carry the rule |

## Essay item

`type: "essay"`, `component: "mee"`: `q` (facts + numbered calls), `rubric` (list of
`{point, weight}` summing to 10), `model_answer` (IRAC, ≤350 words), `cite`, `ref`.

## Rules

- Original questions only; never NCBE, NYBOLE, or commercial-course items. Licensed banks run as a
  local overlay and are never committed.
- `validate_bank.py` must be clean before commit.
- Any key change is logged in `VALIDATION.md` with the reason and the source checked.
