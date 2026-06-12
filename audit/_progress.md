# Skill classification audit — progress & method

**Goal:** verify each skill's `jurisdiction` and `practice` by READING its text
(frontmatter description + body), not by regex. Output → `skill-audit.csv`.

- Total skills: 3571 (git-tracked `*/skills/*/SKILL.md`; quarantine skillsmp/lawve excluded)
- Batches: 72 × 50 (last batch = 21)
- Ordered file list: `_filelist.txt` (1-based index = global idx)
- Practice vocabulary (48 slugs, controlled): `_practices-ref.md`
- Valid jurisdictions: ISO 3166-1 alpha-2 + `general`, `cross-jurisdiction`, `eu`

## CSV columns
idx, path, jurisdiction, jur_ok, jur_suggest, practice, prac_ok, prac_suggest, note
- jur_ok / prac_ok ∈ {ok, wrong, maybe}
- *_suggest: corrected value when wrong/maybe (else empty)
- note: short reason (Russian ok), only when not plainly ok

## How to run a batch
`./audit/dump_batch.sh <N>` prints 50 skills (capped ~62 lines each). READ them,
judge jurisdiction + practice, append 50 rows to skill-audit.csv. If a skill is
ambiguous from the cap, Read the full file before judging.

## State
LAST COMPLETED BATCH: 72
DONE - all 3571 audited
