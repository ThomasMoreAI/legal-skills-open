# ExChek Deemed Export / Foreign National Review Skill (exchek-deemed-export)

Walks through **15 CFR 734.2(b)** to determine whether a “release” of technology or source code to a foreign national is a **deemed export** under the EAR. Covers nationality, technology vs. software, fundamental research, and license/exception. Produces a short **Deemed Export Review Memo** (deemed export applies / does not apply / recommend counsel).

- **Docs:** https://docs.exchek.us  
- **Website:** https://exchek.us  

## What it does

- **Inputs:** Recipient (citizenship/nationality, immigration status), what is being released (technology/software description), context (employment, visit, collaboration), optional ECCN/classification, fundamental research or other carve-outs.
- **Outputs:** A filled **Deemed Export Review Memo** (markdown and optional .docx/.pages) with analysis and conclusion.

This skill does **not** perform classification or screening; it may consume user-provided classification and focuses solely on deemed-export analysis.

## Install

Copy this folder into your agent's skills directory:

```bash
# If from exchekinc repo:
cp -r exchek-skill-deemed-export ~/.cursor/skills/exchek-deemed-export

# Or from exchekskills repo:
git clone https://github.com/exchekinc/exchekskills exchekskills
cp -r exchekskills/exchek-skill-deemed-export ~/.cursor/skills/exchek-deemed-export
```

Restart your agent or run `claude skills list`. Skill name: **exchek-deemed-export**.

## How to use

Ask your agent to review a deemed export scenario, e.g.:

- "Is this a deemed export?"
- "Foreign national review for our new hire"
- "We're sharing this tech with a contractor—do we need a license?"
- "Deemed export memo for this release"
- "Does fundamental research apply here?"

See **SKILL.md** in this folder for full flow, references, and template.

## License

See ExChek, Inc. terms.
