---
name: bar-benchmark-cure-consulting-group
title: NY Bar Benchmark
description: Scores legal competency on a NY bar-style bank (MBE, NYLE, MPRE, MEE essays). Use when baselining a model, gating legal skill changes, or measuring the legal skills' uplift live.
author: Cure-Consulting-Group
author_url: https://github.com/Cure-Consulting-Group/ProductEngineeringSkills/tree/main/skills/legal/bar-benchmark
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
---

# NY Bar Benchmark

A legal skill library that *sounds* right and one that *is* right look identical until something
is measured. This skill is the measurement: a scored, validated question bank shaped like the
New York bar, a runner that sits a model for it live, and a remediation loop for every miss.

Done means: a score per component against its pass mark, the uplift from the `legal-doctrine`
references (bare vs with-references arm), and each miss mapped to the reference file that should
have prevented it.

## What the score is and isn't

The bundled bank is **original and self-authored** (NCBE questions are copyrighted). Any model
that helped write it will score it generously. So the number is:

- a **regression gate** for changes to the legal skills,
- an **uplift instrument**: bare arm vs doctrine arm on the same items,
- a **weak-area finder**.

It is **not** a prediction of bar passage. That needs a licensed NCBE or commercial bank run as a
local overlay (below), and even then passing is not a license to practice (NY Judiciary Law §478).

## The real exam (verified 2026-09-28)

| NY requirement | Real standard | This bank's proxy mark |
|---|---|---|
| UBE: MBE 50% / MEE 30% / MPT 20% | Scaled **266/400** | MBE ≥70%, MEE rubric ≥7/10 |
| MBE: 200 items (175 scored, 25 per subject × 7) | ≈60–65% raw typically passes | 20 items × 7 subjects |
| NY Law Exam (NYLE): 50 items, 2 hrs, open book | **60%** (30/50) | ≥75%, ~54 items over the 12 NYLC subjects |
| MPRE | Scaled **85** | ≥80%, 30 items |

NY replaces the UBE with the **NextGen** bar exam from **July 2028** and keeps the NYLC/NYLE.
When that happens, add NextGen-shaped sets (integrated skills items) rather than editing these.

## Step 1: Classify

| Request | Run |
|---|---|
| "How good is the model at law?" | `run_live.py --arm both` over the full bank |
| "Did my change to a legal skill break anything?" | `run_live.py --arm doctrine --subject <subject>`, compare to the last result in `results/` |
| "Which areas are weak?" | Score, then the remediation loop |
| "Do the skills actually help?" | `cite_probe.py`: citation integrity, bare vs skill. MCQ scores are at the ceiling for frontier models, so uplift shows here, not there |
| Add or fix questions | Edit `benchmark/questions/*.json`, then `validate_bank.py` |

## Step 2: Run

```bash
S="<plugin>/skills/legal/bar-benchmark/scripts"
python3 "$S"/validate_bank.py                          # structural lint; must be clean
python3 "$S"/bar_bench.py stats                        # coverage
python3 "$S"/run_live.py --backend claude --arm both   # live: bare vs doctrine, writes results/
python3 "$S"/run_live.py --backend codex --component nyle
python3 "$S"/cite_probe.py --backend claude --runs 2    # citation integrity: memos, live statute check
python3 "$S"/bar_bench.py list --component mpre        # exam mode for a human or another agent
python3 "$S"/bar_bench.py score answers.json           # grade an answer file; exit 1 on fail
```

`run_live.py` sends questions without the key to a headless CLI in an empty temporary directory
and batches 10 MCQs per call. Isolation differs by backend: `claude` runs with no tools, no
plugins, no MCP servers, and no project settings; `codex` runs in its read-only sandbox with MCP
servers disabled (it can still read files and loads your global Codex instructions); `agy` has no
tools-off mode, so the runner refuses it unless you pass `--allow-agy`. Every item's `ref` must
name a file in `legal-doctrine/reference/`, and the run stops otherwise. The runner grades essays
with a judge. The judge defaults to a different model family (Codex for a Claude candidate);
same-family judging is labeled advisory. Each run writes `results/<date>-<backend>.json` with
scores, answers, and cost. Results from runs on client material (overlays) stay out of git.

**Self-assessment in a session** (no CLI): `list` the questions only, answer every one before
opening the key or any reference file, then `score`. Consulting the key first makes the number
meaningless.

## Step 3: Remediation loop

For each miss:

1. Read the item's `cite` and `why` (`bar_bench.py key --set <set>`), then the primary source.
2. Is the key right? Self-authored banks have errors. If the key is wrong, fix the item and log
   it in `benchmark/VALIDATION.md`. That's a bank defect, not a model miss.
3. If the key is right, open the item's `ref` file in `legal-doctrine`:
   - rule present and right → retrieval failure; make the rule more prominent or route to it;
   - rule present and wrong → fix it and check sibling claims written at the same time;
   - rule absent → coverage gap; add it.
4. Add a variant item that tests the same rule from another angle, and re-run. A fix that doesn't
   move the score didn't fix anything.

A miss on a NY-distinction item matters more than an MBE miss: that is the gap a real NY matter
would expose.

## Question bank

| Component | Files | Items |
|---|---|---|
| MBE-style | `mbe-<subject>.json` × 7 | 140 |
| NYLE-style | `nyle-cluster-{a,b,c,d}.json` | ~54 |
| MPRE-style | `mpre.json` | 30 |
| MEE-style essays | `mee-cluster-{a,b,c,d}.json` | 7, rubric-scored /10 |

Every item carries `cite`, `why` (why each wrong choice is wrong), and `ref` (the reference file
that should carry its rule). The schema is in `benchmark/README.md`. Validation history (blind
key verification, disputes, fixes) is in `benchmark/VALIDATION.md`.

### Local overlays — licensed banks and matter-specific sets

Never commit licensed questions or client facts here. Put them in:

```
.claude/bar-benchmark/questions/*.json    # auto-discovered under the working directory
BAR_BENCHMARK_QUESTIONS=dir1:dir2         # or by environment
--questions <dir>                         # or per run
```

Same schema; an overlay item with a bundled id replaces it. `bar_bench.py sources` shows what
loaded.

## Scripts

- `scripts/bar_bench.py`: list / template / key / stats / sources / score (`--json`).
- `scripts/run_live.py`: live two-arm run against `claude`, `codex`, `agy`, or `mock`.
- `scripts/validate_bank.py`: schema, ids, key validity, letter balance, rubric sums, `ref` targets.
- `scripts/cite_probe.py`: six NY research-memo prompts, bare vs skill arm; counts statute cites
  that don't exist (live), case cites carrying a verification status, and VERIFIED overclaims.

## Related

`legal-doctrine` (what's measured), `legal-research` (citation integrity), the `legal-analyst`
agent (runs the benchmark gate before memo work), `cpa-benchmark` (the same pattern for tax).
