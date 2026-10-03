---
name: open-agreements
title: 'Open agreements'
description: Navigate and use the OpenAgreements legal content library — source-cited practice guides, review checklists, 50-state law surveys, and fill-ready agreement templates. Look up state-by-state legal guides, checklists, and law surveys, or fill standard templates (NDAs, cloud service agreements, SAFEs) into signable DOCX files. Supports Common Paper, Bonterms, and Y Combinator templates. Use when the user needs a practice guide, a review checklist, a law survey, to draft a legal agreement, create an NDA, fill a contract template, or generate a SAFE. Includes lawyer-reviewed practice guides; see openagreements.org/editors.
author: open-agreements
author_url: https://github.com/open-agreements/open-agreements/tree/main/skills/agreements/open-agreements
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# open-agreements

OpenAgreements is a legal content library with four kinds of first-class
content: **practice guides**, **review checklists**, **law surveys**, and
**fill-ready agreement templates**. This skill makes an agent aware of all four
and able to navigate them. Filling a template into a signable DOCX is **one** of
those capabilities — see the fill workflow below.

## Route to the narrowest skill

Treat `open-agreements` as the flagship hub. Keep using it when a request spans
content types, starts with template discovery, or does not yet identify a
specific agreement. When the request is precise, route to the narrowest spoke;
those skills carry focused triggers, template choices, and safety instructions.

| User's task | Route to |
|-------------|----------|
| NDA, confidentiality agreement, mutual or one-way NDA | `nda` |
| SaaS agreement, MSA, cloud contract, order form, pilot agreement | `cloud-service-agreement` |
| Consulting contract, contractor agreement, services agreement, SOW | `services-agreement` |
| Offer letter, employment agreement, PIIA, employee onboarding documents | `employment-contract` |
| DPA, GDPR addendum, HIPAA BAA, data-processing or AI addendum | `data-privacy-agreement` |
| YC SAFE, valuation cap, discount, MFN, or pro-rata side letter | `safe` |
| NVCA or Series A financing documents | `venture-financing` |
| Explain non-compete or restrictive-covenant law | `non-compete-contract-explainer` |
| Explain U.S. state consumer-privacy law | `data-privacy-law-explainer` |

The spoke names are routing targets, not separate brands. They install from the
same `open-agreements/open-agreements` bundle, and this hub remains the fallback
for mixed or ambiguous agreement work.

## Lawyer-reviewed practice guides

OpenAgreements practice guides are lawyer-reviewed. Learn about the editors at
<https://openagreements.org/editors>. Third-party standard forms retain their
own authorship and license provenance.

## What's in OpenAgreements

| Content | What it is | How to read it |
|---------|-----------|----------------|
| **Practice guides** | Source-cited, state-by-state explanations of what the law says (e.g. non-compete, consumer privacy, AI in hiring). | Append `.md` or `.json` to a guide's canonical URL on openagreements.org. Browse as plain markdown under [`practice-guides/`](https://github.com/open-agreements/open-agreements/tree/main/practice-guides). |
| **Review checklists** | Requirement-by-requirement checklists for reviewing an agreement against a standard form (e.g. the YC SAFE). | Append `.md` or `.json` to a checklist's canonical URL. |
| **Law surveys** | 50-state comparison tables for a topic. | Append `.json` or `.csv` (spreadsheet import) to a survey's canonical URL; surveys have no `.md` twin. |
| **Agreement templates** | Standard forms (Common Paper, Bonterms, Y Combinator, OpenAgreements) you can fill into signable DOCX. | Use the MCP or CLI fill workflow below. |

For deep, jurisdiction-specific legal research, the `data-privacy-law-explainer`
and `non-compete-contract-explainer` skills wrap the practice-guide content,
bundling a per-jurisdiction snapshot offline.

## Fill a template (one capability)

The rest of this skill documents the **template-filling** capability,
discovering a standard form and filling it into a signable DOCX. Use the local
CLI by default. The other three content kinds above are read-only reference
content: fetch their machine-readable twins or browse the repo directly.

## Activation

Use this skill when the user wants to:
- Find a source-cited legal practice guide
- Compare a legal rule across U.S. states
- Review a draft against a requirement-by-requirement checklist
- Draft an NDA, confidentiality agreement, or cloud service agreement
- Generate a SAFE (Simple Agreement for Future Equity) for a startup investment
- Fill a legal template with their company details
- Generate a filled DOCX from a standard form

## Execution — MCP Tools (Optional, Not Bundled)

The Claude plugin does not install or start an MCP server. If the user has
separately configured the Open Agreements MCP server, you may use these tools.
For the hosted server, disclose that field values are sent to
openagreements.org before using `fill_template`.

**Remote MCP URL:** `https://openagreements.org/api/mcp`

### Available MCP Tools

| Tool | Purpose |
|------|---------|
| `list_templates` | List available templates as a paginated compact catalog (`template_id`, `display_name`, `category`, `description`, `field_count`, `priority_field_count`). Pages with `cursor` + `limit` (default 25, max 100). |
| `search_templates` | Search the catalog by topic when the desired agreement type is known |
| `get_template` | Get full field metadata for a specific template |
| `fill_template` | Fill a template with values and return a downloadable DOCX |

### MCP Workflow

1. **Discover templates:** Call `list_templates` (returns a compact, paginated catalog — page with `cursor` + `limit` until `next_cursor` is `null`). If you know the topic ahead of time, prefer `search_templates` over a full catalog walk. If user asked for a specific type (e.g. "NDA"), identify the right template from the list.
2. **Get field details:** Call `get_template` with the chosen `template_id` to get full field definitions (name, type, required, section, description, default).
3. **Collect field values:** Ask the user for values based on the field definitions. Use defaults where the user doesn't specify.
4. **Fill template:** Call `fill_template` with the template ID and values. Returns a download URL for the DOCX.
5. **User reviews document:** Present the download link. Wait for the user to confirm the document looks good.

## Confirm-before-signing fields (statutory compliance representations)

A few templates have boolean fields that recite a **past statutory-compliance
fact someone must actually have performed** (e.g. "the required advance notice
was given before signing"). Their `get_template` description begins with
`CONFIRM-BEFORE-SIGNING`, and they default to `false`.

- **You MUST ask the human to confirm the fact actually happened before setting
  one of these fields to `true`.** Setting it true asserts a real-world fact; do
  not infer it from context.
- When such a field is left `false` (unconfirmed) and the clause applies, the
  filled DOCX is **not** broken — the recital renders followed by a yellow
  `[CONFIRM before signing: …]` bracket, and a matching yellow notice appears on
  **page one** listing each item still needing confirmation. Tell the user these
  yellow brackets must be confirmed and deleted before the agreement is signed.
- Once the human confirms, set the field to `true` and the document renders
  clean (no bracket, no page-one notice).

## Execution — Local CLI (Default for Template Filling)

Use the CLI unless the user has already chosen a separately configured MCP
server.

### Step 1: Detect runtime

```bash
if command -v open-agreements >/dev/null 2>&1 &&
  test "$(open-agreements --version 2>/dev/null)" = "0.8.0"
then
  echo "GLOBAL"
elif command -v node >/dev/null 2>&1; then
  echo "NPX"
else
  echo "PREVIEW_ONLY"
fi
```

- **GLOBAL**: Use `open-agreements` directly only after its installed package
  version has been verified as `0.8.0`.
- **NPX**: Use `npx -y open-agreements@0.8.0` as prefix. **Always pin the version** — never use `@latest` to avoid pulling unexpected updates.
- **PREVIEW_ONLY**: No Node.js. Generate markdown preview only.

### Step 2: Discover templates

```bash
open-agreements list --json
```

Parse the `items` array. Each item has `name`, `description`, `license`, `source_url`, `source`, and `fields`.

### Step 3: Help user choose, collect values, fill

Same as MCP workflow steps 2-5. Keep the collected values in memory until the
user confirms them. Then create, use, and delete the values file in one shell
invocation:

```bash
(
  set -eu
  VALUES_FILE="$(mktemp "${TMPDIR:-/tmp}/oa-values.XXXXXX")"
  chmod 600 "$VALUES_FILE"
  trap 'rm -f "$VALUES_FILE"' EXIT HUP INT TERM

  cat > "$VALUES_FILE" <<'FIELDS'
{
  "field_name": "confirmed value"
}
FIELDS

  if command -v open-agreements >/dev/null 2>&1 &&
    test "$(open-agreements --version 2>/dev/null)" = "0.8.0"
  then
    open-agreements fill <template-name> -d "$VALUES_FILE" -o <output-name>.docx
  else
    npx -y open-agreements@0.8.0 fill <template-name> -d "$VALUES_FILE" -o <output-name>.docx
  fi
)
```

The restrictive permissions and cleanup trap keep confidential field values out
of a predictable shared path and remove them even if filling fails.

## Source Code and Audit

Open Agreements is fully open source (Apache-2.0 license). Review the complete source before installing:

- **GitHub**: https://github.com/open-agreements/open-agreements
- **npm registry**: https://www.npmjs.com/package/open-agreements
- **Remote MCP**: https://openagreements.org/api/mcp (optional, hosted service)
- **No postinstall scripts** — verify with `npm view open-agreements scripts`. The package declares no `postinstall`, `preinstall`, or `install` hooks. The `prepare` script only runs when installing from a git URL, not from the npm registry.

All template field definitions and fill logic are auditable in the repository.

### A note on versions

The two version numbers in this skill are independent and refer to different things:

- **Skill version** (in this file's frontmatter, currently `0.4.0`) — versions the skill documentation itself.
- **npm package version** (currently `0.8.0`) — the version of the upstream `open-agreements` npm package this skill recommends pinning. Check `npm view open-agreements version` for the latest.

A newer skill version means the documentation was updated. A newer npm package version means the underlying tool was updated. They are not synchronized.

## Install-Time vs Runtime Network Behavior

Open Agreements has three distinct network postures depending on which execution path you use:

| Path | Install-time network | Runtime network |
|------|---------------------|----------------|
| **Pinned global install** (`npm install -g open-agreements@0.8.0`) | One-time fetch from `registry.npmjs.org` | None for `list`/`fill`. |
| **Pinned npx** (`npx -y open-agreements@0.8.0`) | Fetch from `registry.npmjs.org` on first run, cached afterward | Same as above |
| **Remote MCP** (`https://openagreements.org/api/mcp`) | None | **Template contents and any field values are sent to openagreements.org.** Use only if you accept transmitting these values to the hosted service. |

**Use the local CLI path** (global or npx) if you need guaranteed offline behavior with no third-party data transfer.

## Offline / Pinned Installation

For environments where `npx` auto-fetch is unacceptable, install the package globally and pin the version:

```bash
# Install a specific pinned version globally (one-time)
npm install -g open-agreements@0.8.0

# Then use the installed binary directly — no npx fetching at runtime
open-agreements list --json
open-agreements fill <template-name> -d values.json -o output.docx
```

Before upgrading, review the changelog: https://github.com/open-agreements/open-agreements/blob/main/CHANGELOG.md

### Pin the version even when using npx

Even with `npx`, always pin the version:

```bash
npx -y open-agreements@0.8.0 list --json
```

Never use `@latest` — it pulls a fresh package on every cache miss and can introduce unexpected changes.

## Shared Execution Reference

For the full template-filling workflow (applicable to all agreement skills), see [template-filling-execution.md](template-filling-execution.md).

## Notes

- All templates produce Word DOCX files that preserve original formatting
- Templates are licensed by their respective authors (CC BY 4.0, CC0, or CC BY-ND 4.0)
- External templates (CC BY-ND 4.0, e.g. YC SAFEs) can be filled for your own use but must not be redistributed in modified form
- This tool does not provide legal advice — consult an attorney
- Templates are discovered dynamically — always use `list_templates` or `list --json` for the current inventory

## Feedback

If this skill helped, star us on GitHub: https://github.com/open-agreements/open-agreements
On ClawHub: `clawhub star open-agreements/open-agreements`
