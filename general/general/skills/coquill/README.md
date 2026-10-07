# coquill

A document assembly skill for Claude. Match a user request to a pre-approved template, interview them for variable values, and render a completed `.docx`, `.html`, or `.md` file — without drafting from scratch or exercising legal judgment.

Designed for lawyers and trained paralegals working from an approved template library. All output is a working draft; review by qualified counsel is required before use.

---

## Documentation and source

- **Docs:** [houfu.github.io/coquill](https://houfu.github.io/coquill)
- **Source:** [github.com/houfu/coquill](https://github.com/houfu/coquill)

This folder is the **lq-skills distribution** of CoQuill — a stable snapshot bundled for use with the lq-skills registry. The canonical development repository is `houfu/coquill`.

> **Feature requests, bug reports, and contributions** should be directed to the [main repository](https://github.com/houfu/coquill/issues), not to lq-skills.

---

## What it does

1. Searches the template library for a match to the user's request.
2. Analyzes the template for variables, conditional sections, and loops.
3. Interviews the user conversationally to collect all required values.
4. Renders the completed document and saves it to a job folder alongside a session transcript.

---

## Bundle structure

CoQuill ships as four skills. The orchestrator is the only one users interact with directly; the other three are called internally.

```
coquill/
├── SKILL.md              # Orchestrator — the skill users invoke
├── analyzer/
│   ├── SKILL.md          # Parses templates and generates manifest.yaml
│   └── analyze.py
├── renderer/
│   ├── SKILL.md          # Renders variables into the template and validates output
│   └── render.py
├── transcriber/
│   ├── SKILL.md          # Writes a human-readable transcript.md from the interview log
│   └── transcribe.py
└── templates/_examples/  # Bundled starter templates (see below)
```

---

## Bundled example templates

Three ready-to-use templates ship inside `templates/_examples/`. Each one demonstrates a different combination of CoQuill features and renders to a different output format, so you have a working reference for each pipeline.

| Template | Format | Demonstrates |
|---|---|---|
| `Bonterms_Mutual_NDA/` | `.docx` | Real-world legal template (Bonterms Mutual NDA v1.0, CC BY 4.0). Variable substitution into a docx via `docxtpl`; signing-block fields. |
| `invoice/` | `.html` | Simple HTML template rendered via Jinja2; basic typed variables (`text`, `date`, `number`). |
| `meeting_notes/` | `.md` | Full v2 feature surface: choice variables, boolean conditionals, loops, interview groups, cross-field validation, and a developer `config.yaml`. |

Trigger CoQuill and ask for "an NDA", "an invoice", or "meeting notes" to exercise each one.

---

## Trigger phrases

CoQuill activates when you say things like:

- "Prepare a [document type]"
- "Draft an NDA for [party]"
- "Fill out the [template name] template"
- "I need a tenancy agreement"

---

## License

MIT — see [LICENSE](LICENSE).  
For the full version history and changelog, see [CHANGELOG.md](CHANGELOG.md).
