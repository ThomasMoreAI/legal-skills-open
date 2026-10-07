# Connectors

## How tool references work

This skill operates on files inside an OpenAgreements repo checkout. It does not
require any MCP servers to author the canonical source — only Node.js to run the
generator and tests after editing.

## Connectors for this skill

| Category | Placeholder | Recommended | Other options |
|----------|-------------|-------------|---------------|
| OpenAgreements repo | `~~open-agreements-repo` | Local clone of [open-agreements/open-agreements](https://github.com/open-agreements/open-agreements) | Worktree of the same repo (recommended when multiple agents may edit concurrently) |
| Node toolchain | `~~node` | Node.js >= 20 with `npm` | `pnpm`/`yarn` work for the install step but `npm run generate:templates` is the canonical entry point |

### Setting up the repo

```bash
git clone https://github.com/open-agreements/open-agreements.git
cd open-agreements
npm ci
```

After editing a `template.md`:

```bash
npm run generate:templates
```

This regenerates `templates/<slug>/.template.generated.json` and
`templates/<slug>/template.docx` from the canonical source.

### Verifying canonical → JSON sync

```bash
npx vitest run integration-tests/canonical-source-authoring.test.ts
```

Fails if any canonical `template.md` has drifted from its committed
`.template.generated.json`. Run it before committing.

### Broader test coverage

For a more thorough check across the canonical compiler, JSON-spec renderer,
and the MCP fill path:

```bash
npx vitest run \
  integration-tests/canonical-source-authoring.test.ts \
  integration-tests/template-validation.test.ts \
  packages/contract-templates-mcp/tests/tools.test.ts
```

### Worktrees for concurrent editing

If multiple agents may edit the same repo, prefer a per-task worktree:

```bash
git worktree add /tmp/oa-canonical-<topic> -b <branch>
cd /tmp/oa-canonical-<topic>
npm ci
```

This isolates `template.md` edits and the regenerated JSON/DOCX from other
in-flight work.
