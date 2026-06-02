---
name: audit-crossrefs
title: 'Phase 7: Cross-References'
description: 'Phase 7: Convert hardcoded cross-references to auto-updating NOTEREF fields'
author: edwinhu
author_url: https://github.com/edwinhu/workflows/tree/main/skills/bluebook-audit/skills/audit-crossrefs
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Phase 7: Cross-References

Convert hardcoded supra/infra note numbers to NOTEREF field codes that auto-update when footnotes are renumbered, then tie each cross-reference to a bibkey from `references/sources.bib` so the bibliography becomes the semantic identity layer.

## Canonical 3-script pipeline

```
sources.bib ← make_bib_from_docx.py       # BOOTSTRAP (once per paper, Gemini)
                       ↓
docx ← create_crossrefs.py                # ONE-TIME conversion of hand-typed text
                       ↓
docx ← audit_crossref_targets.py --grep --apply        # DRIFT CORRECTION (deterministic)
                       ↓
docx ← bib_integrate.py --bib references/sources.bib   # BIBKEY-TAG SYNC (deterministic)
       (also pre-computes cached display values)
```

All four live in `${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/`.

### Maintenance one-liner

After a Word session that added/edited footnotes (including new hand-typed
`<X>, supra note N` text), run:

```bash
"${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/sync_crossrefs.sh" \
  draft.docx references/sources.bib
```

The shell wrapper runs create_crossrefs → audit_crossref_targets → bib_integrate
in sequence. All three are idempotent and fully deterministic — re-running
on a clean doc does nothing; ~5 seconds total runtime.

| Stage | Script | Gemini? | When |
|-------|--------|---------|------|
| Bootstrap | `make_bib_from_docx.py` | Yes (one-off batch) | Paper has hand-typed footnotes and no `sources.bib` yet |
| Initial conversion | `create_crossrefs.py` | No | Convert hardcoded `supra note N` text → NOTEREF fields |
| Drift correction | `audit_crossref_targets.py --grep` | No | After footnote edits — fix any supras whose target drifted |
| Drift correction (ambiguous) | `audit_crossref_targets.py --batch` | Yes | Only for refs grep can't resolve uniquely |
| Bibkey-tag sync | `bib_integrate.py` | No | After cross-refs settle — rename bookmarks to `_RefBib_<bibkey>` and pre-compute cached display |

## Initial conversion (one-time)

Convert hardcoded `<X>, supra note N` text to NOTEREF cross-reference fields.

```bash
# Preview
uv run python3 "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/create_crossrefs.py" --docx <path> --dry-run

# Apply
uv run python3 "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/create_crossrefs.py" --docx <path>
```

## Workflow

1. **Bootstrap the bib** (only if no `references/sources.bib` yet):
   ```bash
   uv run --with lxml --with google-genai --with google-cloud-storage python3 \
     "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/make_bib_from_docx.py" \
     --docx <path> --out references/sources.bib
   ```
   Walks the docx footnotes, skips supra-only / bio fns, sends each first-cite candidate to Gemini Vertex Batch, emits BibTeX with `note = {fnN}` linking each entry to its source footnote.
2. **Dry run create_crossrefs** — review the cross-reference map and bookmark plan
3. **Apply create_crossrefs** — the script backs up the original before writing
4. **Audit + retarget** — run `audit_crossref_targets.py --grep --apply` (see below). Hand-typed `supra note N` numbers go stale as footnotes are added or reordered; the create_crossrefs script faithfully bookmarks the literal N, which can be silently wrong for every reference. Grep resolves the easy cases deterministically; only ambiguous refs need `--batch`.
5. **Bibkey-tag** — run `bib_integrate.py --bib references/sources.bib --apply`. Renames bookmarks to `_RefBib_<bibkey>`, retargets supras by bibkey, and pre-computes cached display values so the doc renders correctly on first read (no F9 needed).
6. **Verify in Word** — open the DOCX, spot-check 5-10 supras. Cmd+A → `fn+F9` (Mac) or `Ctrl+A → F9` (Windows) to force-refresh fields if needed.
7. **Renumber test** (optional) — add a footnote before a referenced target and confirm the supra numbers update.

### `audit_crossref_targets.py` (drift correction, also runnable standalone)

```bash
# Mechanical audit only — flags refs whose surnames don't appear in the target footnote
uv run --with lxml python3 \
  "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/audit_crossref_targets.py" \
  --docx <path>

# Deterministic first pass — grep each reference for its first cite. No LLM cost.
#   On a 138-ref test set: resolved 62 refs unique with 98% accuracy, deferred
#   76 truly ambiguous cases. Always run this BEFORE invoking Gemini/Batch — it
#   strips the easy cases and saves LLM calls.
uv run --with lxml python3 \
  "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/audit_crossref_targets.py" \
  --docx <path> --grep --apply

# Grep + production LLM batch for the residue (recommended for full pipeline)
uv run --with lxml --with google-genai --with google-cloud-storage python3 \
  "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/audit_crossref_targets.py" \
  --docx <path> --grep --batch --apply --location global

# LLM-only paths (skip grep — coverage-risky for --gemini):
uv run … --docx <path> --batch --model gemini-3.1-flash-lite-preview --apply
uv run … --docx <path> --gemini --apply
```

### `bib_integrate.py` (bibkey-tag sync, fully deterministic)

```bash
uv run --with lxml python3 \
  "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/bib_integrate.py" \
  --docx <path> --bib references/sources.bib --apply
```

What it does:

1. Parses `sources.bib`.
2. For each bib entry, derives signature tokens (author surnames + distinctive title words + institutional bibkey prefix) and finds the docx footnote whose body text contains all of them. This re-derives the `fn_id → bibkey` map from current docx content — sidesteps any drift between bib's `note={fnN}` tag and current numbering.
3. For each supra/infra NOTEREF, picks the best matching bibkey (target-fn bonus + global token scoring).
4. Creates `_RefBib_<bibkey>` bookmarks wrapping body footnoteReferences. Multi-cite footnotes get multiple bookmarks (one per source) — each pointing at the same body footnoteReference, so the displayed number stays the same; only the bookmark name differs by source.
5. Rewrites each NOTEREF instr text to point at its bibkey-named bookmark.
6. Pre-computes cached NOTEREF display values (using `--bio-count`, default 3 for `*, †, ‡` author bios that don't consume display numbers when `numRestart=eachSect` is set).
7. Emits `SUPRA_BIB_AUDIT.md` listing any supras whose surnames don't match the picked bibkey's haystack (author + title + howpublished + bibkey).

Fully deterministic — no LLM calls. Idempotent on re-runs.

### `make_bib_from_docx.py` (bootstrap, Gemini)

```bash
uv run --with lxml --with google-genai --with google-cloud-storage python3 \
  "${CLAUDE_SKILL_DIR}/../../../../skills/bluebook-audit/scripts/make_bib_from_docx.py" \
  --docx <path> --out references/sources.bib
```

Walks the docx footnotes, splits multi-cite footnotes on `;`, sends each first-cite candidate to a Vertex AI Batch job (one independent request per citation; `gemini-3.1-flash-lite-preview` default). Emits BibTeX entries with bibkey conventions `firstauthorlastYEAR` for academic works and short slugs (`gao2017`, `crs2024`, `secReg2020`) for institutional sources.

Each entry includes `note = {fnN}` linking back to the source footnote.

Once `sources.bib` exists, **maintain it directly** — do not regenerate. Edits to the bib (typos, missing fields, new sources) should be in-place.

**Vertex AI batch requires:**
- `gcloud auth application-default login` for ADC
- `--project` (default `$GOOGLE_CLOUD_PROJECT` or `activist-defense-nal`)
- `--gcs-bucket` (default `$GEMINI_BATCH_BUCKET` or `nal-batch-extraction`)
- Location: `us-central1` (default)

For `gemini-3.x` models, `thinkingLevel: MINIMAL` is set automatically — without it, batch responses silently return empty content (see /gemini-batch SKILL gotcha 12).

Output written to `<docx-dir>/scratch/`:
- `crossref_audit.json` — every cross-reference with current target + match status
- `crossref_remap.json` — Gemini's proposed corrections (with confidence)
- `CROSSREF_AUDIT.md` — human-readable diff report

The audit is **safe to run standalone** without re-running the rest of the bluebook-audit workflow. Use it any time create_crossrefs has been run and you want to validate that hand-typed supra/infra numbers were correct.

### Recommended pipeline order

1. **`--grep` first.** Cheapest, deterministic, ~98% precision on `unique`
   matches. Resolves ~half the refs at $0 cost.
2. **`--batch`** (Vertex AI, per-ref independence) on the deferred set.
3. **Manual first-cite verification** on remaining mechanical flags (Step 4 below).

### How `--grep` works

A cross-reference reads `<short-form identifier>, supra/infra note N`. The
identifier can be any Bluebook short form, not just author surnames:

- author group:        `Hu, Malenko & Zytnick`
- hereinafter tag:     `GAO Report`, `CRS Report`, `Rosenberg`, `2020 SEC Regulation`
- institutional doc:   `Best Practice Principles`, `Policies and Procedures`, `Senate Banking Committee Letter`
- case name:           `ISS v. SEC`
- title fragment:      `Choi, Fisch & Kahan, Power of Proxy Advisors`

For each reference the script:

1. Tokenizes the identifier (filters Bluebook signals like `See`, `But see`, `E.g.`).
2. Strips every `<X>, supra/infra note <N>` phrase from each candidate footnote, so a footnote that merely *cites* the same identifier via supra doesn't count as the first cite.
3. Searches every footnote — except the source — for one whose post-supra-strip text contains all the identifier tokens with word-boundary matches.
4. If **exactly one** footnote matches → `unique`, apply deterministically.
5. If **multiple** match → `ambiguous`, defer to LLM (picking the earliest is wrong ~17% of the time — typically when the identifier appears in passing in one footnote and as a first cite in another).
6. If **none** match → `no_match`, defer to LLM (which has the catalog and can guess, or correctly say "not in document").

### Step 4 (mandatory): Manual first-cite verification on residuals

**Iron Law: Neither Gemini pass is fully trustworthy on its own.** A two-batch consensus is high-confidence, but the residual disagreements ALWAYS require human first-cite verification. Do not stop after `--apply`.

The failure modes we observed on a real 248-footnote draft:
- **Single-batched call**: model returns uniform "medium" confidence — a smoking-gun signal it didn't reason per-reference.
- **Per-reference Vertex Batch**: model returns uniform "high" with detailed reasoning, but still confidently picks **wrong** targets when:
  - the cited work isn't in the doc (model hallucinates a plausible-sounding nearby match)
  - the first cite is buried mid-footnote in a `See also` or multi-cite list (model misses it and picks a different paper by the same author)
  - the reference is to a self-referencing pattern (model returns the source footnote itself)
- **Mechanical surname check**: only inspects the leading 250 chars of the target footnote, so first cites buried after `See`/`hereinafter`/inline-discussion lead-ins are flagged as mismatches even when correct.

#### Recipe

1. **Compare both Gemini passes**, taking the intersection where they agree as the high-confidence consensus. Apply that subset first.
2. **For each disagreement**, search the doc for the **first non-supra cite** of the disputed surname / title fragment. The script's regex below catches mid-footnote occurrences:
   ```python
   for fn in fns.findall('.//w:footnote'):
       txt = ''.join(t.text or '' for t in fn.iter('w:t'))
       if re.search(r'<surname-pattern>', txt) and 'supra' not in txt[:300].lower():
           print(fn.get('w:id'), txt[:200])
   ```
3. **Build a manual remap** of `(source_fn, surnames, current_bookmark) → correct_fn_id`, save as `crossref_remap_manual.json`, and apply with `--remap PATH --apply`.
4. **For the "no first cite in document" residue** (works the author cites without ever having introduced):
   - Search broadly first — the first cite is often mid-footnote in a `See also`/multi-cite list.
   - Only if truly absent: flag for an author edit. Write `SUPRA_UNRESOLVED.md` listing the source FN, surnames, and the search patterns tried.
5. **Final re-audit** will still show "mechanical mismatches" for the false-positive cases — verify each by spot-checking the target footnote content. Do not retarget these.

#### Gate

- [ ] Consensus retargets applied (intersection of `--gemini` and `--batch`)
- [ ] Manual remap built and applied for disagreements
- [ ] Each surviving "mismatch" flag spot-checked against actual target content
- [ ] No supra/infra reference points at an unrelated footnote
- [ ] `SUPRA_UNRESOLVED.md` written (or empty if all resolved)

## What Gets Converted

| Pattern | Example | Result |
|---------|---------|--------|
| Single supra | `supra note 42` | NOTEREF to FN42 bookmark |
| Single infra | `infra note 188` | NOTEREF to FN188 bookmark |
| Range | `infra notes 209-210` | Two NOTEREFs with separator |
| With pincite | `supra note 42, at 15` | NOTEREF + roman `, at 15` |
| Existing NOTEREF | (already converted) | Skipped |

## What Is NOT Converted (Phase 2 — Future)

- Part/Section references (`supra Section I.A.`, `infra Part III`)
- These require a heading-to-bookmark mapping strategy since heading numbering is partially auto-generated

## Gate: Exit Cross-References

- [ ] Dry run reviewed — cross-reference map is correct
- [ ] NOTEREF fields created for all supra/infra note references
- [ ] **Target audit passed** — `audit_crossref_targets.py` run + Step 4 manual verification complete; no NOTEREF points at an unrelated footnote
- [ ] Backup DOCX exists
- [ ] Word field update (Ctrl+A, F9) confirms correct numbers

## Workflow Complete

Present final summary to user:
- Total formatting corrections applied (from Phase 4)
- Total URLs archived (from Phase 6)
- Total NOTEREF fields created (from Phase 7)
- Final DOCX file path
