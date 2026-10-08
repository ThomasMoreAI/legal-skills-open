# AI Automation Contracts — Contract Generation Skill

An agent skill that drafts ready-to-sign contracts, worded in the provider's favor, for the turnkey automation-with-AI business model:

```
project data → templates (implementation / maintenance / work order) → filled .docx → PDF check → deliver
```

It covers the three documents a typical automation sale needs — the full turnkey **implementation** contract, an optional monthly **maintenance** retainer, and one-page **work orders** for one-off return visits — with a fixed set of provider-favorable policy decisions (IP split, liability cap, tacit acceptance, three-layer AI performance standard) already baked into the templates.

Works with agent harnesses that support file-based skills (Claude Code, Codex, and similar).

## What's in this folder

| Path | Purpose |
|---|---|
| [SKILL.md](SKILL.md) | The skill itself: workflow, redaction rules, fixed policy decisions |
| [references/intake.md](references/intake.md) | Full intake checklist, grouped by block, marking what comes from the client vs. what the provider decides |
| [assets/implementacion.md](assets/implementacion.md) | Template: the full implementation contract, legal body plus Annexes I and II |
| [assets/mantenimiento.md](assets/mantenimiento.md) | Template: monthly maintenance retainer (hours included, response time, auto-renewal) |
| [assets/orden-trabajo.md](assets/orden-trabajo.md) | Template: one-page work order for a punctual intervention |
| [assets/defaults.json](assets/defaults.json) | Default values for every policy variable (deadlines, thresholds, standard clauses) — edit here to change policy across all future contracts |
| [scripts/generar_contrato.py](scripts/generar_contrato.py) | Fills a template's `{{PLACEHOLDERS}}` from a data JSON and builds the formatted `.docx` |

## Key features

- **Three documents, one dependency chain** — implementation is always generated and is the document the other two lean on; maintenance and work orders reference it instead of repeating its legal body. Selling implementation plus a retainer never produces a fourth document: both are generated and signed together, deliberately, so cancelling the retainer never affects the implementation already delivered.
- **Intake that doesn't stall on missing data** — `references/intake.md` gives the full checklist by block; the agent asks only what's missing and relevant, in short grouped batches, and cross-checks against a commercial proposal you already sent the client instead of re-asking. Fields still open when generation runs come out marked `[COMPLETAR: X]` in red in the document, and are listed at the end — the contract is never blocked waiting on a detail.
- **Policy fixed in the templates, not improvised per contract** — obligation of means, not results, a three-layer AI performance standard (deterministic actions, a 90% threshold for verifiable AI roles, no metric on writing quality, with three separate exclusions), split IP (the specific build assigned in full but non-exclusive; base components — flow templates, prompt libraries, architectures — retained with reuse rights, licensed to the client to operate and modify), unrestricted publicity rights over the delivered work, a 30-day warranty with broad exclusions and a fix-only remedy, tacit acceptance at 7 days, client non-collaboration timeouts, and a 50%-of-price liability cap. All documented in [SKILL.md](SKILL.md) so the agent can explain any of them if a client objects.
- **Content-block redaction, not fill-in-the-blank** — variables like `ALCANCE_INCLUIDO`, `ROLES_IA`, `CRITERIOS_ACEPTACION`, `ESQUEMA_PAGOS` and `ACCESOS_REQUERIDOS` are drafted in legal register as short bulleted lists, not copied verbatim from conversational input, and acceptance criteria are always written as verifiable system behavior — never "client satisfaction."
- **Local, dependency-light `.docx` generation** — `scripts/generar_contrato.py` renders the filled markdown into a formatted Word document (Calibri 10.5, justified body, page break before each Annex) with no network calls and no paid API; the only dependency is `python-docx`.
- **Built-in PDF check before delivery** — the workflow converts the generated `.docx` to PDF and inspects at least the first page and the signature page before handing it over.
- **One mandatory warning, not repeated** — the first contract of a series reminds you this template needs a one-time review by a lawyer in your own jurisdiction before real clients sign it; the skill produces a consistent, provider-favorable, reusable document, and that single legal review is what makes it safe to reuse indefinitely.

## Installation

**Option A — let your agent install it (recommended).** Open Claude Code and paste:

```text
Install the ai-automation-contracts skill from https://github.com/aurelioagency/skills :
1. Run: git clone --filter=blob:none --sparse https://github.com/aurelioagency/skills.git into a temporary folder.
2. Inside it, run: git sparse-checkout set ai-automation-contracts
3. Copy the ai-automation-contracts/ folder into ~/.claude/skills/ai-automation-contracts/
4. Delete the temporary clone and confirm the skill loads.
5. Check the requirements: Python 3 and python-docx (pip install python-docx).
   Install anything missing (ask me to approve each install command).
6. Explain how to use the skill and ask me if we draft my first contract now.
```

The agent fetches only this skill (not the whole collection), installs it permanently in `~/.claude/skills/` for all future chats, and walks you into your first job.

**Option B — manual.** Clone the repo and run the bundled installer:

```powershell
git clone https://github.com/aurelioagency/skills.git
cd skills
node install-skills.mjs ai-automation-contracts          # Claude Code
node install-skills.mjs ai-automation-contracts --codex  # Codex
```

Any other harness: point it at this folder's `SKILL.md`.

## Updating

Improvements land in this repo; your installed copy never updates itself. To update, re-run the installer — it replaces the installed skill cleanly, records the installed commit in `.installed-from.json`, and prints the old and new commits. Open Claude Code and paste:

```text
Update my installed ai-automation-contracts skill from https://github.com/aurelioagency/skills :
1. If I have a clone of the repo, run git pull in it; otherwise make a temporary
   sparse clone like in the install prompt.
2. In the clone, run: node install-skills.mjs ai-automation-contracts
3. The installer prints the previous and new commit. Summarize what changed
   between them (git log --oneline <old>..<new> -- ai-automation-contracts) in my language.
4. Confirm the skill still loads. Delete the temporary clone if you made one.
```

To find out whether you are behind without installing anything, run this in an up-to-date clone:

```powershell
node install-skills.mjs ai-automation-contracts --check
```

It compares the commit recorded in your installed copy against the checkout, counting only commits that touch this skill (exit code 3 means an update is available). Teams working on the repo can keep a permanent clone: updating is just `git pull` + the installer command.

> **Careful if you improved your installed copy by hand.** The installer replaces the skill's files. Anything you edited inside `~/.claude/skills/ai-automation-contracts/` that was never committed to the repo is lost on update — this applies especially to `assets/defaults.json` if you tuned it locally. Bring changes to the repo first.

## Uninstalling

The installed skill lives entirely in one folder: `~/.claude/skills/ai-automation-contracts/`. Removing it never touches contracts you already generated (they live in your own project folders), other installed skills, or any clone of this repo. Open Claude Code and paste:

```text
Remove the ai-automation-contracts skill from my machine:
1. Delete the folder ~/.claude/skills/ai-automation-contracts/ (all of it).
2. Confirm the skill no longer loads. Do not touch my generated contracts,
   other installed skills, or any clone of the skills repo.
```

Or manually — from a clone of the repo:

```powershell
node install-skills.mjs ai-automation-contracts --remove
```

(which only deletes the installed copy, never the repo folder), or simply delete `~/.claude/skills/ai-automation-contracts/` yourself.

## Requirements

- **Python 3** on `PATH`.
- **`python-docx`** (`pip install python-docx`) — builds the formatted `.docx`.
- A PDF-conversion path for the delivery check (e.g. LibreOffice's `soffice` headless mode) plus `pdftoppm` to render the check pages — optional but recommended before handing a contract over.
- **No API keys and no paid providers** — everything runs locally.

## Usage

Once installed, the skill lives in `~/.claude/skills/ai-automation-contracts/` and is available in **every** Claude Code session on the machine, forever. Nothing is re-installed per contract.

Trigger it by describing the job, for example:

> Necesito el contrato de implementación para el proyecto que le cerré a `<cliente>`

> Armame implementación más mantenimiento para este proyecto

> Orden de trabajo para `<cliente>`, volvió a pedir un ajuste

From there the skill:

1. Confirms which documents are needed (implementation alone, or implementation plus maintenance).
2. Reads `references/intake.md` and asks only for what's missing, in short grouped batches, cross-checking against anything you already gave it (a commercial proposal often already covers scope, timeline, price and platforms).
3. Builds a `datos.json` from `assets/defaults.json` overridden with the project's own data.
4. Runs `scripts/generar_contrato.py` to produce the formatted `.docx`.
5. Converts to PDF and checks the first page and the signature page.
6. Delivers the file and lists any field still marked `[COMPLETAR: X]`.

### Editing policy defaults

`assets/defaults.json` holds every variable with a standard value (deadlines, thresholds, boilerplate exclusions). Edit it directly to change policy across every future contract — client-specific data always overrides it per project and is never written back into the defaults.

## License

MIT — see [LICENSE](../LICENSE) at the repo root.
