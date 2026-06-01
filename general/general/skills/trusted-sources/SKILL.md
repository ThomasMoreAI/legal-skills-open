---
name: trusted-sources
title: trusted-sources
description: Acquire authoritative reference documents — statutes, regulations, official policies, terms of service, agency guidance — into the case folder with provenance and plaintext extraction. Triggers when the user names a specific law/regulation/policy/ToS the case will cite, asks "do we have a copy of <X>" or "where do I find the official text of <Y>", supplies a copy and asks "can we use this", or when packet-builder needs a reference appendix that isn't on disk.
author: EvanOchsner
author_url: https://github.com/EvanOchsner/personal-advocacy-toolkit/tree/main/.claude/skills/trusted-sources
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# trusted-sources

Three independent paths to the same authoritative text:

- **Path A — User-supplied copy.** The user already has the doc. Ingest it, then *assess* what's visible (truncation flags, missing effective dates, watermarks). The user makes the call on whether to trust it.
- **Path B — Project-known trusted source.** Look up the curated source directory in `data/reference_sources.yaml` for the doc's `(kind, jurisdiction)` pair (e.g., `(statute, MD)` → Maryland General Assembly).
- **Path C — Constrained web search.** Allowlist-only fetch (`*.gov`, `*.us`, NAIC, courts.gov, Cornell LII, etc.) with explicit denylist (Wikipedia, paywalled aggregators, marketing legal sites).

When two or more paths produce a copy, **report both side-by-side**. Hash-equal copies are consolidated; differences get a `compare` report and the user decides. Never silently prefer one path over another.

## When this skill fires

- The user names a specific statute, regulation, policy, or ToS the case will cite.
- The user says "I have a copy of the policy / TOS / statute, can we use it?"
- The user asks "do we have a copy of `<citation>`?" or "where do I find the official text of `<X>`?"
- `packet-builder` is about to compile a reference appendix whose source isn't already under `references/`.
- `authorities-finder` or `authorities-reconcile` has just identified a regulator and the next step is pulling the rules they enforce.

## Procedure

1. **Identify the doc.** Get all of:
   - `kind` ∈ {`statute`, `regulation`, `official-policy`, `tos`, `guidance`, `case-law`, `other`}
   - `citation` (e.g., `"Md. Code Ins. § 27-303"`, `"15 USC § 45"`, `"Acme TOS as of 2026-04-15"`)
   - `jurisdiction` (2-letter US state, `"federal"`, or `"*"` for cross-jurisdiction docs like ToS)
   - `title` (optional but useful for the index)

   If the user is vague ("the statute about car insurance claims in Maryland"), translate to a concrete cite before proceeding. Don't ingest something the user can't name.

2. **Ask about Path A.** "Do you already have a copy?" If yes:
   - Locate the file (the user may name a path or hand you one).
   - Run the ingester with `--source-origin user-supplied`:

     ```
     uv run python -m scripts.references.ingest \
         --file <path> \
         --kind <kind> --citation "<citation>" --jurisdiction <juris> \
         --source-label "<where they got it, in their words>"
     ```

   - Read the assessment block in the resulting sidecar. **Report flags to the user verbatim** with the canonical phrasing: *"You make the call on whether this copy is good enough; I can flag what I see but I can't certify authority."*

3. **Look up Path B.** Read `data/reference_sources.yaml` for `(kind, jurisdiction)`. If a curated entry exists, present each source to the user with name, URL, and `how:` instructions. Then ask: *"Want me to fetch this for you (recommended for first cross-check), or would you rather download it yourself and hand me the file?"*

   - **Fetch path:** run the ingester with `--url`:

     ```
     uv run python -m scripts.references.ingest \
         --url <url> \
         --kind <kind> --citation "<citation>" --jurisdiction <juris> \
         --source-label "<from data/reference_sources.yaml>"
     ```

   - **Manual-download path:** print the URL and the `how:` text, wait for the user to drop the file into `references/raw/` (or anywhere), then ingest it as in Path A but with `--source-origin manual-download`.

4. **Optional Path C — constrained web search.** When Path B is sparse or a cross-check is wanted, search via the same allowlist as `authorities-web-research`. Forbidden: Wikipedia (for cites), paywalled aggregators, AI answer panels, marketing-legal sites. The fetcher will refuse non-allowlisted hosts; if the user is confident in a specific host that isn't listed, you may pass `--allow-unknown` *only after explicit user confirmation* and only for primary publishers (`.gov`, `.us`, official agency domains).

5. **Cross-check when 2+ paths produced a copy.** Run:

   ```
   uv run python -m scripts.references.compare \
       --refs references/structured/<a>.json references/structured/<b>.json \
       --out notes/references/$(date +%Y-%m-%d)_<slug>_compare.md
   ```

   - **Hash-equal:** byte-identical copies; just note that the two paths agreed.
   - **Hash-differ but text-equal:** the rendering differs (PDF vs HTML) but the substance is the same; safe.
   - **Text-differs:** show the diff. Likely causes: the user's copy is older, an excerpt, or from a non-authoritative source. Ask the user to read the diff and decide.

6. **Re-hash the references tree.** The ingester does this automatically (it refreshes `<case>/.references-manifest.sha256` on each call). If the user manually moves files under `references/`, run:

   ```
   uv run python -m scripts.references.ingest --help  # confirm path
   # the manifest also gets refreshed by every ingest; if you need a manual refresh:
   #   python -c "from scripts.references._manifest import refresh_sha256_manifest; from pathlib import Path; refresh_sha256_manifest(Path('references'), Path('.references-manifest.sha256'))"
   ```

7. **Hand back to caller.** Typically that's `pat-workflow` (continuing to Phase 4) or `packet-builder` (which can now reference the doc from `packet-manifest.yaml > reference_appendices`).

## Path A — assessing user-supplied copies

The agent does **not** certify authority. It surfaces what's visible and the user decides. Verbatim phrasing:

> *"You make the call on whether this copy is good enough; I can flag what I see but I can't certify authority."*

The ingester runs heuristics in `scripts/references/assess.py` that produce flags:

| Code | Meaning |
|---|---|
| `truncation-suspected` | Text ends mid-sentence or without final punctuation. |
| `short-for-kind` | Text is below a typical floor for this kind (e.g., a statute under 400 chars). |
| `has-truncation-marker` | Contains literal `[truncated]`, `(continued)`, `* * *`, etc. |
| `looks-like-excerpt` | First 500 chars contain "EXCERPT", "PARTIAL", "SAMPLE". |
| `has-watermark` | Contains "DRAFT", "CONFIDENTIAL", etc. |
| `no-effective-date` | No "as of", "effective", "last updated", or version marker found. |
| `no-section-numbers` | For `statute` / `regulation`, no `§`, "Section N", or `(a)(b)` markers. |
| `encoding-issues` | Replacement characters / mojibake. |

Report **every `warn`-level flag** to the user. `info`-level flags are background; mention them only if relevant.

If the assessment looks bad and the user wants the doc anyway, that's fine — note the flags in the sidecar and proceed. The user owns the trust call.

## Path B — project-known trusted sources

`data/reference_sources.yaml` is the curated map of *where to get* authoritative text. Two top sections:

- **Allow/denylist** — domain glob patterns with `trust` levels (`primary`, `secondary-trusted`, `secondary-confirm`). Used by the fetcher.
- **Source directory** — keyed by `(kind, jurisdiction)`, lists 1-N curated sources with `name`, `url`, `how:`, and `trust:`. Falls back to `(kind, "*")` when the specific jurisdiction isn't listed (e.g., ToS is jurisdiction-agnostic).

Present sources to the user verbatim — don't paraphrase the `how:` line. The point of the curated directory is that the *exact* path-to-text instructions have been written down.

If the directory has nothing for `(kind, jurisdiction)`, say so plainly and offer Path C. Don't invent a source.

## Path C — constrained web search

Same allow/deny policy as `authorities-web-research`. Trust hierarchy:

- **Primary**: official publisher of the text (`mgaleg.maryland.gov`, `ecfr.gov`, `govinfo.gov`, the agency's own `.gov` site, the platform's own `/legal` page).
- **Secondary-trusted**: well-known free legal-information providers (`law.cornell.edu`, `courtlistener.com`). Allowed; sidecar records the trust level so the user knows it isn't first-party.
- **Secondary-confirm**: archives, mirrors, secondary republishers. Refused unless the user explicitly types `--allow-unknown` after you've explained why.

Forbidden by default: Wikipedia (as a cite), paywalled aggregators (`westlaw.com`, `lexisnexis.com`, `casetext.com`), AI answer panels, marketing legal sites (`findlaw.com`, `justia.com`, etc. — fine for orientation, never as a cite source).

## Cross-source comparison

When ≥2 paths produced a copy, always compare. The compare tool emits markdown by default; drop it under `notes/references/<date>_<slug>_compare.md` so the dual-process result is preserved alongside the case-intake notes.

- **`raw_sha256_equal: true`** — byte-identical bytes. Consolidate to one record (the duplicate ingest can be removed by hand if desired).
- **`raw_sha256_equal: false, readable_text_equal: true`** — different containers (PDF vs HTML), same substance. Keep both; note in the user-facing summary.
- **`readable_text_equal: false`** — the rendered text differs. Show the diff to the user. Likely causes: one is older, one is an excerpt, one is from a non-authoritative republisher. The user decides which to rely on.

## Disclaimers (verbatim — do not paraphrase or strip)

- Stamp into every sidecar JSON: `"This is reference information, not legal advice."`
- On any cite extracted from a fetched doc and quoted in a draft: `[VERIFY WITH COUNSEL]`.
- For Path A user-supplied copies: *"You make the call on whether this copy is good enough; I can flag what I see but I can't certify authority."*

These strings are embedded by `scripts/references/ingest.py` automatically; do not strip or rephrase them when reporting to the user.

## Definition of done

For each doc the user wants:

1. `references/raw/<slug>.<ext>` exists (byte-identical copy of the source).
2. `references/readable/<slug>.txt` exists (extracted plaintext; may be empty if the format has no extractor — that's a flagged outcome, not a failure).
3. `references/structured/<slug>.json` exists with full sidecar including `disclaimer`, `assessment`, `extraction.method`, `source_origin`, and (if fetched) `fetch.host` + `fetch.trust`.
4. `references/.references-manifest.yaml` has an entry for `source_id`.
5. `<case>/.references-manifest.sha256` is refreshed.
6. If 2+ paths produced copies, a comparison report exists under `notes/references/`.

Hand back to the caller (`pat-workflow` or `packet-builder`).

## Synthetic example (Maryland-Mustang)

Maryland-Mustang's complaint cites `Md. Code Ins. § 27-303` (unfair claim settlement practices) and `COMAR 31.15.07` (motor-vehicle total-loss claim regulations). Pulling them via Path B (project-known trusted source):

```
uv run python -m scripts.references.ingest \
    --url "https://mgaleg.maryland.gov/mgawebsite/Laws/StatuteText?article=gin&section=27-303" \
    --kind statute --citation "Md. Code Ins. § 27-303" --jurisdiction MD \
    --source-label "Maryland General Assembly"

uv run python -m scripts.references.ingest \
    --url "http://www.dsd.state.md.us/comar/SubtitleSearch.aspx?search=31.15.07" \
    --kind regulation --citation "COMAR 31.15.07" --jurisdiction MD \
    --source-label "COMAR — Code of Maryland Regulations"
```

After ingest, the packet manifest can reference them:

```yaml
reference_appendices:
  - name: "md-statutory-reference"
    title: "Maryland Statutes and Regulations Cited"
    sources:
      - "../references/raw/md-code-ins-27-303.html"
      - "../references/raw/comar-31-15-07.html"
    note: |
      Public-domain Maryland statutes and regulations cited in the
      complaint. Verify against the publisher's site before relying
      on a specific provision.
```

## Do not

- Do not invent statutes, regulations, or citations that aren't in the user's facts, in `data/authorities.yaml`, or surfaced by an actual fetch. If the user can't name the cite, ask — don't guess.
- Do not strip the disclaimer (`"This is reference information, not legal advice."`) from sidecars, summaries, or downstream drafts.
- Do not auto-fetch from a non-allowlisted domain. The fetcher refuses by design; `--allow-unknown` is for after-the-fact user confirmation, not for batch convenience.
- Do not collapse a dual-source report into "the answer is X." If the user asked for a cross-check, present both.
- Do not treat a single source as authoritative when others were unreachable. Say "Path B was unavailable" plainly.
- Do not mutate `references/raw/` after ingest. If a doc needs replacing (e.g., the agency posted a new version), re-ingest it; the ingester writes a new slug or, with `--force`, overwrites the manifest entry while preserving sha256 history.
- Do not use the case-folder evidence pre-commit hook as a reason to put reference docs under `evidence/`. They belong under `references/` precisely because they are reproducible third-party text.
