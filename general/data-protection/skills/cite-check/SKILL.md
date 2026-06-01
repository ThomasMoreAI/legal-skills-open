---
name: cite-check
title: cite-check — Copilot CLI Skill
description: 'Verifiable legal-citation tooling for product counsel reviews. Two modes: (1) ORIGINATE — turn a PPL issue into a Word document of Citation Cards where every flagged risk is anchored by two highlighted quotes (legal source + product fact), byte-for-byte verified before write. (2) PRESSURE-TEST — given an existing review the user has already done, validate that each flagged risk is backed by verbatim, publicly-citable text on both the legal and factual sides, and surface gaps (paraphrased law, missing facts, internal-only sources used as primary cites).'
author: nkasuku
author_url: https://github.com/nkasuku/cite-check/tree/main/skills/cite-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# cite-check — Copilot CLI Skill

Helps a GitHub product counsel verify AI-generated legal citations in Privacy and Product Legal (PPL) reviews. Modeled on [`dvelton/eyeball`](https://github.com/dvelton/eyeball). Eyeball anchors one claim to one source. cite-check anchors one risk to two — the law and the fact — because in a legal review either anchor failing means the conclusion is wrong.

## Two modes

cite-check has two distinct workflows. Pick the right one based on what the user asked for.

### Mode A — ORIGINATE (build a fresh Citation Card)

Trigger when the user asks you to *do* the citation work: *"cite-check issue #847"*, *"build a citation card for the new MAI model review"*, *"run cite-check"*. You read the issue, identify risks, find the legal anchors, verify everything, build the .docx.

Use this mode when **no review yet exists** — the user wants you to produce one with verifiable citations.

### Mode B — PRESSURE-TEST (validate a review the user already has)

Trigger when the user asks you to *check* an existing review: *"pressure-test the cross-border transfer risk"*, *"pressure-test all the High-tier risks in the review above"*, *"validate the citations in that review"*, *"stress test the AI Act argument"*.

Use this mode when **a review already exists in the conversation** (either the user did it, or the product-counsel agent produced one earlier in the session). You don't re-do the review. You take its risk statements as input and validate them.

The output of Mode B is **a per-risk pass/fail report inline in chat**, never a Word doc unless the user explicitly asks "now build the doc."

## Activation

When the user invokes this skill, respond with one of:

> **cite-check (originate mode) is active.** I'll extract the product facts, identify the implicated legal provisions, byte-for-byte verify every quote, and produce a Word document of Citation Cards on your Desktop. Anything I cannot verify will be refused — never silently quoted.

> **cite-check (pressure-test mode) is active.** I'll take the risk(s) you've already flagged and check three things for each one: (a) the cited law actually says verbatim what the risk attributes to it, (b) the cited product fact actually appears in the issue, and (c) every primary cite is publicly citable. Gaps surface inline; nothing is silently smoothed over.

Then follow the workflow below for the chosen mode.

## Tool location

The cite-check Python utility lives at:

```
<plugin_dir>/skills/cite-check/tools/cite.py
```

To find the actual path on this machine:

```bash
find ~/.copilot -name "cite.py" -path "*/cite-check/*" 2>/dev/null
```

If you cannot find it under `~/.copilot`, ask the user for the path to their cite-check checkout.

## First-run setup

Before first use, check that dependencies are installed and the corpus is built:

```bash
python3 <path-to>/cite.py setup-check
```

If anything is missing, run the setup script from the cite-check repo root:

```bash
bash <path-to-repo>/setup.sh         # macOS / Linux
.\setup.ps1                          # Windows (PowerShell)
```

Then build the local corpus from `github/ppl-legal-reference`:

```bash
python3 <path-to>/cite.py refresh-corpus
```

Then fetch the **authoritative public source** (EUR-Lex, leginfo.legislature.ca.gov, gnu.org, docs.github.com, etc.) for every cached file that has one, so verification can run against the official publisher rather than the GitHub mirror:

```bash
python3 <path-to>/cite.py refresh-authoritative
```

Re-run both whenever the user mentions that the reference library has been updated, or whenever a regulation has been amended (e.g., a new SCC release, a docs.github.com Privacy Statement update). To detect mirror staleness on demand, run:

```bash
python3 <path-to>/cite.py verify-corpus
```

This diffs every cached corpus file against its authoritative source and reports drift (exit 1 if any file is out of sync).

## Hard rules (do not break)

These rules implement the user's standing custom instructions. They are non-negotiable.

1. **No fabricated citations.** Every quote that appears in a Citation Card must be byte-for-byte present in the cited source. Use `cite.py verify` on every quote before assembling the cards file. If verify returns exit code 2, you must either (a) replace the quote with one that does verify, or (b) drop the card.
2. **Authoritative-first verification for laws.** When a cited file has an `authoritative_url` configured in `taxonomy.json` (every public-law, public-guidance, open-source-license, and GitHub-public file does), pressure-test verifies the quote against that authoritative source — not against the cached mirror. The cached mirror is only the fallback when the authoritative source is unreachable. If `refresh-authoritative` has not been run for a file, pressure-test will WARN ("verified against cached mirror only — run refresh-authoritative") rather than silently passing on mirror-only verification.
3. **Public-source-only legal basis.** The `LEGAL PROVISION` quote in any card must come from a source classified as `public-law`, `public-guidance`, or `github-public`. Sources classified as `github-internal` (which now includes `04-msft-*` Microsoft contractual instruments) may appear *only* in an `INTERNAL CONTEXT — background only` quote inside a card, never as the legal basis. Use the classification field returned by `cite.py extract-source`.
4. **`[VERIFY]` tagging for web fetches.** Anything pulled by `cite.py extract-source --ref <https-URL>` (rather than from the cached corpus) is auto-classified as `verify-required`. You must keep that classification through to the cards file so the rendered card carries the `[VERIFY]` tag.
5. **Jurisdiction confirmation.** Before extracting any legal provisions, ask the user (use `ask_user`) which jurisdictions to analyze under. Default per the user's standing instructions: US federal + California. Always offer to add EU/UK if the product touches EU/UK users.
6. **Never paraphrase inside a quote block.** Citation card quote blocks contain only verbatim text from the source. Analytical text (your interpretation, the nexus, the recommendation) lives in the `nexus` and `action` fields, never in `quote`.
7. **No final legal advice.** The output document is always framed as a drafting aid. Do not change the disclaimer banner the build tool emits.

## Workflow — Mode A (ORIGINATE)

Follow these steps in order. The order matters.

### Step 1 — Confirm scope with the user

Use `ask_user` for each item. Do not bundle.

1. **Source of facts:** PPL issue ref (e.g., `github/ppl-reviews#847`) OR a pasted risk paragraph OR a pasted draft review. If they give an issue ref, capture it. If they paste text, write it to `~/.copilot/skills/cite-check/cache/facts/manual-<timestamp>.txt`.
2. **Jurisdictions:** default `US federal + California`. Offer EU/UK if not already obvious from the issue.
3. **Risk-tier filter for cards:** default `Medium and High`. Confirm.
4. **Output title and filename** for the Word doc on the Desktop.

### Step 2 — Extract product facts

If the user gave an issue ref:

```bash
python3 <path-to>/cite.py extract-facts --issue <owner>/<repo>#<N> --json
```

Read the JSON output. Identify and **record the verbatim spans** that you will quote later — pull them character-for-character from `body` or each comment's `body` field. Record the source ref as `<owner>/<repo>#<N>` for the issue body, or `<owner>/<repo>#<N>::comment_<id>` for a specific comment.

If the user pasted facts, those are the fact corpus — record verbatim spans with source ref `manual:<timestamp>::para_<n>`.

If the issue links to a design doc in another repo, fetch it with `gh api` or `view` and add it to the fact corpus.

### Step 3 — Identify candidate provisions

Read `<path-to>/taxonomy.json`. For each risk you intend to flag, look up the matching category and list the candidate provisions. The taxonomy is a starting cheat sheet — extend it if you flag a recurring risk that isn't there (edit `taxonomy.json` and tell the user you did).

If a risk doesn't fit any taxonomy category, you may still create a card — but you must locate the provision either in the cached corpus (`cite.py list-corpus` to browse) or via web fetch (auto-tagged `[VERIFY]`).

### Step 4 — Extract verbatim provision text

For each candidate provision:

```bash
python3 <path-to>/cite.py extract-source --ref "<filename>.md#<anchor>" --json
```

Or for a public-law URL not in the cache:

```bash
python3 <path-to>/cite.py extract-source --ref "https://eur-lex.europa.eu/..." --json
```

Read the returned text. Pick the **shortest verbatim span** that fully supports your claim — typically one to three sentences. Record:
- the verbatim quote
- the source ref (the same `--ref` value)
- the `classification` field from the JSON

### Step 5 — Verify every quote

For each quote you intend to put in a card:

```bash
python3 <path-to>/cite.py verify --quote "<exact text>" --source "<ref>"
```

Exit code `0` = verified, set `verified: true` in your card. Exit code `2` = NOT FOUND — you must replace the quote with one that does verify, or drop the card. **Do not edit the verify result.** Do not mark a quote `verified: true` without running this command.

For long multi-sentence quotes, prefer `--strict` to lock to byte-for-byte. For quotes that cross a line break in the source, the default whitespace-normalized mode is fine.

### Step 5b — (Optional) Pre-check screenshot rendering

`cite.py build` automatically renders a highlighted screenshot for each quote and embeds it in the Word doc. If a quote's source is not renderable (see source-ref shapes below), the build falls back to a verbatim text block and logs a "Screenshot render notes" page at the back. To pre-check whether one quote will screenshot cleanly:

```bash
python3 <path-to>/cite.py screenshot \
  --quote "<exact text>" \
  --source "<ref>" \
  --output /tmp/preview.png
```

Exit `0` = PNG written. Exit `2` = the quote text wasn't found in the rendered source (e.g., smart quotes vs. straight quotes, or wrapping that broke the search). If exit 2, either shorten the quote to a distinctive sub-span and re-run `verify` + `screenshot`, or accept the text-only fallback.

**Source-ref shapes that screenshot cleanly:**

| Shape | Example | Renders as |
|---|---|---|
| Cached corpus markdown | `03-reg-gdpr.md#Article 46` | Markdown rendered to a clean document page |
| Public URL | `https://eur-lex.europa.eu/...` | Live page rendered via Playwright (auto `[VERIFY]`) |
| Issue body | `github/ppl-reviews#847` | GitHub-style comment card |
| Specific comment | `github/ppl-reviews#847::comment_12345` | GitHub-style comment card with author + timestamp |

**Anchor conventions in the cached corpus** (what to put after `#` in `<filename>.md#<anchor>`):

| Document type | Anchor convention | Example |
|---|---|---|
| Regulations (GDPR, EU AI Act, ePrivacy, SCCs) | Bare `Article N`, `CHAPTER N`, `SECTION N`, `ANNEX N` | `03-reg-gdpr.md#Article 6`, `03-reg-eu-ai-act-text.md#ANNEX III` |
| US/state codes (CCPA) | `<section number>.` (with trailing dot) | `03-reg-ccpa.md#1798.105.` |
| US Code (Title 17 etc.) | `§<N>` (substring-matches the full `§N · Title` heading) | `06-ip-us-copyright-act-title17.md#§107` |
| Contracts / DPAs (GitHub DPA, Microsoft DPA) | `<N>. <Title>.` (the numbered heading line, dot included) | `01-github-github-dpa.md#9. Subprocessors.` |
| Markdown-structured docs (most policies, guidance) | The literal heading text (case-insensitive substring match) | `01-github-github-privacy-statement.md#Children` |
| Whole document (license texts, short policies) | Omit the `#anchor` entirely | `06-ip-mit-license.md` |

If you're not sure what anchor to use, run `cite.py list-corpus --file <filename>.md` first to see every section the indexer found.

**Source-ref shapes that do NOT screenshot (text-only fallback):**

| Shape | Why | What to do |
|---|---|---|
| `manual:<timestamp>::para_<n>` | No renderable source on disk | If the user pasted the text in chat, save it to a markdown file under the corpus dir and use a real `filename.md#Anchor` ref, then `refresh-corpus`. |

### Step 6 — Assemble the cards file

Write a JSON file to `~/.copilot/skills/cite-check/cache/facts/cards-<timestamp>.json` matching this schema:

```jsonc
{
  "title": "Citation Cards — Product Counsel review of <product>",
  "subtitle": "Source: github/ppl-reviews#847 · Generated by cite-check",
  "risks": [
    {
      "tier": "medium",                // "high" | "medium" | "low"
      "summary": "Cross-border transfer to AI subprocessor without SCCs",
      "quotes": [
        {
          "label": "LEGAL PROVISION",
          "quote": "...verbatim text...",
          "source_ref": "03-reg-gdpr.md#Article 46",
          "classification": "public-law",
          "verified": true
        },
        {
          "label": "GITHUB COMMITMENT",
          "quote": "...verbatim text...",
          "source_ref": "01-github-github-dpa.md#9. Subprocessors.",
          "classification": "github-public",
          "verified": true
        },
        {
          "label": "PRODUCT FACT",
          "quote": "...verbatim text from issue...",
          "source_ref": "github/ppl-reviews#847::comment_12345",
          "classification": "github-public",   // GitHub-internal source, but the FACT itself, not the legal basis
          "verified": true
        }
      ],
      "nexus": "EU personal data will move to a US subprocessor before any Art. 46 transfer mechanism is in place — non-compliant with the regulation and inconsistent with our own DPA commitment.",
      "action": "Block release until SCCs are executed OR Provider X is added to GitHub's approved subprocessor list."
    }
  ]
}
```

Notes on the schema:
- Each card must have at minimum one `LEGAL PROVISION` quote and one `PRODUCT FACT` quote. A `GITHUB COMMITMENT` quote is recommended where applicable.
- `classification` matches what `cite.py extract-source` reported. If the build tool sees `verify-required`, it will tag the rendered card `[VERIFY]`. If it sees `github-internal`, it will tag the rendered card `[INTERNAL CONTEXT — background only]`.
- `verified: true` is mandatory. The build tool refuses to render an unverified quote and lists refusals in the output document.

### Step 7 — Build the document

```bash
python3 <path-to>/cite.py build \
  --cards ~/.copilot/skills/cite-check/cache/facts/cards-<timestamp>.json \
  --output ~/Desktop/<title>.docx \
  --strict
```

`--strict` makes the build fail (exit 2) if any quote is unverified. Use `--strict` by default. Drop it only if the user explicitly wants to see refused-quote placeholders.

Each verified quote is:
1. Captured as a highlighted screenshot from the rendered source (yellow on the cited language) and embedded as a picture, OR
2. If the source ref is not renderable, shown as a verbatim text block with a small italic "screenshot unavailable" note.

In both cases the verbatim text appears on the page so the document is searchable. Render failures are listed on a "Screenshot render notes" page at the back — they do not block the build.

Pass `--no-screenshots` to skip rendering entirely (faster, text-only). Pass `--image-width 5.5` (inches) to shrink screenshots if they overflow.

### Step 8 — Deliver

Tell the user:
- the output file path
- how many cards were rendered, broken down by tier
- any refusals (verify failures, missing sources) and what the user should do about each
- the next reviewer action you'd recommend (e.g., "ready for your read; one card on data retention is parked because GDPR Art. 5(1)(e) wasn't yet in the cache — run `refresh-corpus` and re-run cite-check on that risk only")

## Workflow — Mode B (PRESSURE-TEST)

Use this when a review **already exists** in the conversation (the user did it, or the product-counsel agent produced it earlier in the session) and the user wants you to validate the citations rather than originate new ones.

### Step B1 — Confirm what to pressure-test

Use `ask_user` if it's ambiguous which risks to test. Common asks:
- *"pressure-test the cross-border transfer risk"* → one specific risk
- *"pressure-test all the High-tier risks"* → tier filter
- *"pressure-test that whole review"* → all risks

Do not bundle multiple questions. If the user said something specific, just go.

### Step B2 — Assemble the pressure-test spec

Read the existing review text (in conversation, in a file, or in a GitHub issue/comment). For each risk you'll test, build a JSON object with these fields. Save the full spec to `~/.copilot/skills/cite-check/cache/pressure-tests/spec-<timestamp>.json` (or `/tmp/pt-spec-<short-id>.json` for a quick one-off).

```json
{
  "review_target": "<owner>/<repo>#<N>  (e.g., github/product-and-privacy-legal#2398)",
  "review_summary": "One-sentence description of what was reviewed.",
  "risks": [
    {
      "id": "<short-stable-id>",
      "label": "<one-line risk title from the review>",
      "tier": "HIGH | MEDIUM | LOW",
      "claim": "<the actual sentence(s) from the review that state the risk and the legal conclusion>",
      "asserted_legal_sources": [
        {
          "label": "<human-readable label, e.g., 'GDPR Art. 5(1)(a)'>",
          "ref": "<a ref the dispatcher can resolve — see refs below>",
          "quote": "<OPTIONAL verbatim quote the review attributes to this source>"
        }
      ],
      "asserted_product_facts": [
        {
          "label": "<e.g., 'comment from kayreiman about telemetry opt-out'>",
          "ref": "<owner>/<repo>#<N>::comment_<id>  OR  <owner>/<repo>#<N>",
          "quote": "<REQUIRED verbatim quote the review attributes to this fact>"
        }
      ]
    }
  ]
}
```

**Resolvable `ref` formats** (handled by `_resolve_source_text`):
- `<filename-from-corpus>.md` → cached file in `~/.copilot/skills/cite-check/cache/corpus/`
- `<filename-from-corpus>.md#<anchor>` → specific section
- `https://...` → fetched live (auto-tagged `verify-required`)
- `<owner>/<repo>#<N>` → full issue body
- `<owner>/<repo>#<N>::comment_<id>` → single comment

**Spec-construction rules:**
1. Pull `claim` and `quote` strings *verbatim from the review*. Do not paraphrase. If the review paraphrases the law (no quote provided), leave `quote` empty on that legal source — pressure-test will warn about that.
2. If the review cites a private/internal document (PPL issue, internal playbook), include it anyway. Pressure-test will catch it and warn that it can be background only.
3. One risk per object. If the review bundles multiple legal hooks under one risk, that's fine — list them all under `asserted_legal_sources`.

### Step B3 — Run the pressure test

```bash
python3 <path-to>/cite.py pressure-test --spec <path-to-spec.json>
```

Optional flags:
- `--risk-id <id>` to test only one risk from the spec
- `--auth-freshness-days <N>` (default `30`) — warn (don't block) when a cited file's authoritative-source cache is older than `N` days. Use `0` to flag every cite as stale (useful for forcing a full re-fetch sweep), or a larger value to silence freshness warnings during quick iteration.
- `--json` for machine-readable output (use this if you'll post-process the results)

Exit code: `0` = all PASS, `1` = at least one WARN, `2` = at least one FAIL.

**Verification badges in the output:**
- `✓✓` — quote was verified against the **authoritative public source** (e.g., EUR-Lex for EU regulations, leginfo.legislature.ca.gov for California codes, gnu.org for license text, docs.github.com for GitHub commitments). This is the strongest possible signal: the law as published by the legislature/regulator/standards body actually contains the quoted language.
- `✓` — quote was verified against the cached mirror only. Two legitimate cases: (a) the source *is* the publisher copy (e.g., a GitHub issue/comment is the original; there's no upstream "authoritative" version), or (b) the file has no `authoritative_url` configured (intentional for internal documents).
- `⚠` (mirror-only warn) — the file has an `authoritative_url` but `refresh-authoritative` hasn't been run for it yet. Tell the user: "Run `cite.py refresh-authoritative` to upgrade this from mirror-only to authoritative verification."
- `⚠` (corpus drift) — the quote *is* in the cached mirror but is **NOT** in the authoritative source. This means the mirror is stale, the law has been amended, or the original transcription was wrong. Treat as a serious warning — recommend running `cite.py verify-corpus` to see all drift across the corpus, and `refresh-corpus` to update the mirror.
- `⚠` (stale auth) — the quote *was* verified `✓✓` against the authoritative source, but the cached copy of that source is older than the freshness threshold (default 30 days). This is a soft warning: the verification is still valid against what we last fetched, but the publisher may have amended the source since. Suggested follow-up: `cite.py refresh-authoritative --only <filename> --force`.
- `✗` — quote not found anywhere (paraphrased, hallucinated, or wrong source).

### Step B4 — Surface the report inline

The default output is markdown. Post the relevant sections inline in the conversation. For each risk:

- **PASS** — say so in one line and move on. If the legal anchor showed `✓✓`, mention that the quote is verified against the official publisher (it's a credibility multiplier).
- **WARN** — explain what the warning means (typically: a legal cite resolves but no verbatim quote was provided, OR a primary cite is `github-internal` and may only be background, OR the authoritative source hasn't been fetched yet, OR the mirror has drifted from the authoritative source).
- **FAIL** — be specific about which dimension failed and why. Common failures:
  - *Legal quote not verbatim:* the law doesn't actually say what the review claims it says. The reviewer needs to either find the right provision or rewrite the claim.
  - *Product fact not verbatim:* the issue/comment doesn't actually say what the review attributes to it. Possible hallucination or misattribution.
  - *Ref unresolved (HTTP error / 404):* almost always means a private/internal GitHub URL was cited. Pressure-test downgrades it to `github-internal` and warns. The reviewer may need to either authenticate the cite (find a public counterpart) or move it to background-only.
  - *Public-source policy ⚠:* a `github-internal` document is being used as a primary cite. Per product-counsel agent rules, internal docs are background context only — the legal conclusion has to rest on a public source.

### Step B5 — Offer follow-ups, but don't take them on your own

After delivering the report, offer (one at a time, do not bundle):
- *"Want me to search the corpus for a verbatim provision that actually supports risk X?"*
- *"Want me to build a Citation Card .docx for the risks that passed?"* (this is Mode A on the passing subset)
- *"Want to refresh the corpus and re-run? I noticed the cite for X isn't in the cached set."*

Do **not** modify the underlying review unless the user explicitly asks you to. Pressure-test is a diagnostic — fixing the review is a separate ask.

## Self-check before delivery

Before saving the cards file or running `build`, mentally verify:

1. Does each card have at least one `LEGAL PROVISION` quote and one `PRODUCT FACT` quote?
2. Is every `LEGAL PROVISION` quote classified `public-law`, `public-guidance`, or `github-public`?
3. Is no `LEGAL PROVISION` block sourced from a `github-internal` document?
4. Did `cite.py verify` actually return 0 for every quote you marked `verified: true`?
5. Does each `nexus` paragraph explain *why* the legal quote and the product quote together create a risk — not just restate them?
6. Are risk tiers conservative? Use 🔴 only for clear non-compliance with a binding rule; 🟡 for material concerns or ambiguity that needs negotiation; 🟢 for minor improvements.
7. Are `[VERIFY]` tags preserved on every web-fetched quote?

## When to extend the taxonomy

If you flag a risk that doesn't map to an existing category in `taxonomy.json`, and you expect this pattern to recur:

1. Read the taxonomy: `view <path-to>/taxonomy.json`
2. Add a new category with `summary` and `candidates` (each candidate needs `id`, `label`, `source_type`, `location`, `anchor`, `classification`).
3. Use `edit` to write the change in place.
4. Tell the user what you added so they can sanity-check.

## When to extend the cached corpus

If the right provision is on a public regulator's site but not in the cache, and you expect to cite it again:

1. Read the taxonomy: `view <path-to>/taxonomy.json`
2. Add the filename to `cached_corpus_allowlist`.
3. Note that the file must already exist in `github/ppl-legal-reference` for `refresh-corpus` to fetch it. If it doesn't, raise it as a follow-up for the user to add to the reference repo.

## Failure modes and how to handle them

| Symptom | What it means | What to do |
|---|---|---|
| `cite.py refresh-corpus` returns "✗ filename (gh api failed)" | File not in `github/ppl-legal-reference` yet | Skip that file; tell the user; suggest opening a PR to add it |
| `cite.py verify` returns exit 2 | Your quote is not in the source | Re-extract with `cite.py extract-source` and copy a span verbatim, or drop the card |
| `cite.py screenshot` returns exit 2 | Quote text wasn't found in the rendered source (smart quotes, ligatures, wrapping) | Try a shorter, more distinctive sub-span — re-`verify` it, then re-`screenshot`. If still fails, accept the text-only fallback. |
| `cite.py build --strict` returns exit 2 | At least one quote is still unverified | Fix verify failures one at a time; do not bypass `--strict` |
| User pastes a risk with no clear product fact | Missing factual anchor | Use `ask_user` to ask for the issue ref, design doc URL, or specific quote that triggered the concern. Do not invent a fact. |
| Provision exists only in a `github-internal` doc | Cannot serve as legal basis | Surface the *public* analogue (regulation, GitHub public commitment); demote the internal doc to `INTERNAL CONTEXT — background only` |
| Build succeeds but several render-notes appear | Screenshots failed for renderable sources (e.g., a public URL was 503) | Re-run build later, or drop `--no-screenshots` for a text-only doc, or replace the URL ref with a cached corpus ref if the same content is mirrored. |
| `pressure-test` reports a ref as "could not resolve" with HTTPError 404 | The cited URL is private/internal (or genuinely missing); pressure-test auto-classifies it as `github-internal` | Tell the user the cite is private. Either find a public counterpart or move that source to background-only and rest the legal conclusion on a public cite. |
| `pressure-test` reports `quote NOT found verbatim` on a product fact | The review attributes language to a comment/issue body that the source doesn't actually contain (paraphrase, hallucination, or wrong comment ID) | Re-extract the source with `extract-facts` and find the actual nearest verbatim span; either rewrite the claim to use real language or flag it for the reviewer's correction |
| `pressure-test` reports `ref resolves but no verbatim quote provided` (warn) | The reviewer cited a provision generically without pinning specific language | Ask the user whether they want help finding the most relevant verbatim sub-clause from that provision, or whether the generic cite is acceptable |
| `pressure-test` reports `quote verified against cached mirror only; authoritative source not yet fetched` (warn) | The corpus file has an `authoritative_url` configured but `refresh-authoritative` hasn't been run for it | Run `cite.py refresh-authoritative --only <filename>` to upgrade the verification from mirror-only to authoritative, then re-run pressure-test |
| `pressure-test` reports `quote is in the cached mirror but NOT in the authoritative source` (corpus drift) | The mirror copy of the law/regulation has diverged from the official publisher (mirror is stale, the law was amended, or the original transcription was wrong) | Run `cite.py verify-corpus` to see all drift across the corpus. If the mirror is stale, run `cite.py refresh-corpus`. If the law was genuinely amended, update the cited language in the review to match the current authoritative version. |
| `pressure-test` reports `authoritative copy is N.Nd old (threshold: 30d)` (stale auth) | The cited file *was* verified `✓✓` against its authoritative source, but the cached copy of that source is older than the freshness threshold (default 30 days). The verification is still valid against what we last fetched — this is a soft "you may want to re-confirm" warning, not a failure. | Run `cite.py refresh-authoritative --only <filename> --force` and re-run pressure-test. If you want to relax the threshold for a quick iteration loop, pass `--auth-freshness-days 90` (or any larger value). |
| `verify-corpus` flags drift on a file you didn't change | The authoritative public source has been updated since the mirror was built (e.g., docs.github.com Privacy Statement got a new effective date) | Run `cite.py refresh-corpus --only <filename>` to update the mirror; if the changes are substantive (e.g., a new SCC release, a regulation amendment), surface that as a finding to the reviewer because any prior reviews relying on the old text may need re-examination |
