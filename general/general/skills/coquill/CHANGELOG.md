# CHANGELOG.md

This tracks the current version mainatained in the lq-skills repository.
For the latest developed version of coquill, refer to https://github.com/houfu/coquill

## 2026-05-13 — Add: bundled example templates

Three starter templates shipped under `skills/coquill/templates/_examples/`:

- `Bonterms_Mutual_NDA/` — docx, real-world legal template (Bonterms Mutual NDA v1.0, CC BY 4.0). Exercises the docx pipeline and signing-block fields.
- `invoice/` — HTML, simple typed-variable example covering the html→pdf pipeline.
- `meeting_notes/` — Markdown, full v2 feature surface: choice variables, boolean conditionals, loops, interview groups, cross-field validation, and a developer `config.yaml`.

Each template ships with its own `manifest.yaml` so the analyzer hits a cache on first use and the renderer can be exercised end-to-end without any pre-processing. `coquill/SKILL.md` Phase 1 template discovery now lists `${CLAUDE_PLUGIN_ROOT}/skills/coquill/templates/_examples/` as the bundled lookup path for this distribution, alongside the existing `${CLAUDE_PLUGIN_ROOT}/templates/_examples/` for the standalone `houfu/coquill` plugin layout.

## 2026-05-13 — Merge: upstream QA remediation (LegalQuants, 2026-05)

Merged LegalQuants' QA remediation pass (upstream commit `9684c5a`) into the reorganized skill structure introduced by the PR.

**Resolved by reorganization (no further action needed):**
- Upstream flagged `scripts/analyze.py`, `scripts/render.py`, `scripts/transcribe.py` as "not bundled, must search `$CLAUDE_PLUGIN_ROOT`". The reorganization ships each script inside its corresponding subskill directory (`skills/coquill/{analyzer,renderer,transcriber}/`), so the concern is structurally resolved. The "ships alongside" language in each subskill SKILL.md is the new canonical posture.
- Severity bands on analyzer Step 2 warnings (upstream tagged `[H]`/`[M]`/`[L]`; this repo uses 🔴/🟡/🟢 with identical semantics).
- Halt rule on high-severity analyzer warnings.
- Analyzer escalation check (zero variables → hard stop, orphaned gate → user prompt) in `coquill/SKILL.md` Phase 2.
- Validation requirement (unfilled placeholders, unrendered control tags) in the renderer.
- Work Shape (Bounded Transactional) declaration in `coquill/SKILL.md`.
- "What This Skill Does Not Do" / Out of Scope listing in `coquill/SKILL.md`.

**Newly added in this merge:**
- `coquill/SKILL.md` § "Escalation Triggers" — consolidated trigger list (unknown template, conflicting answers, missing required variables, unfilled placeholders at render time, unusual values on substantive variables). Complements the per-phase escalation logic already present.
- `coquill/SKILL.md` § "Draft Output Requirement" — promotes the existing `draft_notice` parameter-passing into a named, top-level output contract: every rendered document and `transcript.md` MUST carry the `**DRAFT — review and revise before execution**` header.
- Frontmatter on all four SKILL.md files updated with `author: Hou Fu Ang`, `last_reviewed: 2026-05`, `last_reviewed_by: LegalQuants (QA remediation)`. `version: 3.0.0+cicero` retained on `coquill/SKILL.md` (more specific than upstream's `0.1.0`); subskills retain `version: inherits from coquill`.

**Not ported:**
- Verbatim "QA Remediation (LegalQuants, 2026-05)" footers on each SKILL.md. This CHANGELOG entry is the provenance record for the merge; SKILL.md bodies stay instructional.

## v 3.0.0+Cicero -- The "Cicero" release (the original version on lq-skills)
**New Features**
* Markdown templates — .md files are now a fully supported template format, rendered via Jinja2 with optional PDF output (via markdown + weasyprint)
* PDF output for .docx templates — produced automatically when Microsoft Word (docx2pdf) or LibreOffice is available; soft-fails with a warning if neither is found
* Interview transcripts — every document assembly session now saves an interview_log.json and a human-readable transcript.md to the job folder, recording questions asked, answers given, and confirmed values
* Transcriber (coquill-transcriber) — generates transcript.md from the interview log after each document assembly session
* On-demand dependency installation — docx2pdf is installed only for docx jobs, weasyprint only for HTML/markdown jobs; no unnecessary packages loaded
* Modular renderer — rendering logic extracted into a dedicated render.py script for cleaner skill architecture
* Conditional logic with {% if %} / {% else %} / {% endif %} support
* Loop sections with {% for item in items %} / {% endfor %} support
* Developer configuration via optional config.yaml per template
* Interview grouping, conditional groups, and loop groups
* Cross-field validation rules
* Skill separation: Orchestrator, Analyzer, and Renderer skills
* Manifest v2 schema with schema_version: 2, conditionals, loops, and dependencies
* Enhanced Meeting Notes example template (md) demonstrating all v2 features: choice variables, equality and boolean conditionals, loops, and config.yaml
* Simple variable substitution in .docx and .html templates. Jinja2-style {{ variable_name }} placeholders with type inference from name suffixes.
