# TX Title Analysis Skill

**A structured AI skill for Texas residential and commercial title examination.**

This skill captures the workflow, decision logic, standards, and output templates that a Texas title examiner uses to analyze commitments, recorded instruments, surveys, and HOA documents. It produces DRAFT title opinion letters, requirements checklists, and exception cure recommendations — all for attorney review.

---

## What's New in v2.0

- **Commercial real estate** workflow (Step 5A) — ALTA/NSPS surveys, environmental due diligence, 1031 exchanges, commercial lease analysis, SNDA agreements, commercial endorsements
- **Manufactured housing** workflow (Step 5B) — SOL, TDHCA requirements, personal-to-real property conversion
- **Expanded reference library** — 8 new reference files covering liens, condemnation/eminent domain, foreclosure, probate, entity authority, water rights, minerals, and survey analysis
- **Structured data schema** — JSON Schema for standardized analysis records with CSV/Excel and XML mappings
- **Quality checklist** — 12-section pre-delivery verification guide
- **Sample outputs** — 3 example DRAFT documents demonstrating expected output format

---

## What's Included

```
tx-title-analysis/
├── SKILL.md                                    ← Core skill file (the main instruction set)
├── README.md                                   ← You're reading it
├── references/
│   ├── tx-exam-standards.md                    ← TX Title Examination Standards (Chs. I–XXI)
│   ├── tx-exceptions.md                        ← Schedule B exception classification guide
│   ├── tx-requirements.md                      ← Standard requirements & endorsements
│   ├── tx-forms.md                             ← TX title insurance form reference (T-1, T-7, T-19, etc.)
│   ├── tx-opinion-template.md                  ← Title opinion letter template
│   ├── tx-liens.md                             ← Constitutional, statutory & consensual liens  [NEW]
│   ├── tx-commercial.md                        ← Commercial RE title analysis guide  [NEW]
│   ├── tx-condemnation.md                      ← Eminent domain / condemnation  [NEW]
│   ├── tx-manufactured-housing.md              ← Manufactured housing title issues  [NEW]
│   ├── tx-foreclosure.md                       ← Foreclosure-specific analysis rules
│   ├── tx-minerals.md                          ← Mineral/royalty interest analysis
│   ├── tx-water-rights.md                      ← Water rights examination
│   ├── tx-probate.md                           ← Probate & heirship title issues
│   ├── tx-entities.md                          ← Entity authority verification
│   ├── tx-survey.md                            ← Survey analysis guidelines
│   ├── tx-quality-checklist.md                 ← Pre-delivery quality review checklist
│   ├── tx-data-schema.md                       ← Structured data output schema docs
│   └── sample-outputs/
│       ├── sample-title-opinion.md             ← Example generated opinion
│       ├── sample-requirements-checklist.md    ← Example requirements output
│       └── sample-exception-analysis.md        ← Example exception analysis
└── data/
    ├── title-analysis-schema.json              ← JSON schema for structured analysis output
    └── sample-analysis-record.json             ← Example structured JSON output
```

---

## Installation by Platform

### Claude Cowork (Desktop App)

Claude Cowork auto-detects skill files when they're in your working folder.

1. **Open Claude Desktop** and start a new Cowork session.
2. **Select a folder** — choose any folder on your computer, or create a new one (e.g., `~/Documents/legal-skills/`).
3. **Copy this entire `tx-title-analysis/` folder** into the selected folder.
4. Claude will automatically detect `SKILL.md` and all reference files. You'll see the skill appear in the available skills list.
5. **Upload a title commitment** and ask Claude to analyze it — the skill activates automatically.

> **Tip:** You can also place the skill folder inside a `.skills/skills/` subdirectory of your working folder for cleaner organization:
> ```
> your-working-folder/
> └── .skills/
>     └── skills/
>         └── tx-title-analysis/
>             ├── SKILL.md
>             ├── references/
>             │   ├── tx-exam-standards.md
>             │   └── ... (all reference files)
>             └── data/
>                 └── ... (schema files)
> ```

---

### Claude Code (CLI)

Claude Code reads skill files from your project directory or a global skills location.

1. **Create a skills directory** in your project (or globally):
   ```bash
   # Project-level (recommended)
   mkdir -p .claude/skills/tx-title-analysis

   # Or global
   mkdir -p ~/.claude/skills/tx-title-analysis
   ```

2. **Copy all skill files** into the directory:
   ```bash
   cp -r tx-title-analysis/* .claude/skills/tx-title-analysis/
   ```

3. **Reference in CLAUDE.md** (optional but recommended):
   ```markdown
   ## Available Skills
   - TX Title Analysis: `.claude/skills/tx-title-analysis/SKILL.md`
   ```

4. **Use it:**
   ```bash
   claude "Analyze this title commitment for 123 Main St, Dallas TX"
   ```

---

### OpenAI Codex

Codex reads instruction files from your repository or sandbox.

1. **Add the skill folder** to your project repository:
   ```bash
   mkdir -p .codex/skills/tx-title-analysis
   cp -r tx-title-analysis/* .codex/skills/tx-title-analysis/
   ```

2. **Reference in your AGENTS.md or system instructions:**
   ```markdown
   When performing Texas title examination, follow the workflow in
   .codex/skills/tx-title-analysis/SKILL.md and reference the
   supporting files in that directory.
   ```

3. **Or paste SKILL.md directly** into the Codex system prompt / instructions panel if you prefer a simpler setup.

4. Upload your title documents and ask Codex to analyze them following the skill workflow.

---

### ChatGPT (Custom GPT or Project)

ChatGPT can use skill files as Knowledge files in a Custom GPT or as Project instructions.

#### Option A: Custom GPT

1. Go to **[chat.openai.com](https://chat.openai.com)** → **Explore GPTs** → **Create**.
2. In the **Configure** tab:
   - **Name:** TX Title Examiner
   - **Instructions:** Copy the full contents of `SKILL.md` into the instructions field.
3. Under **Knowledge**, upload all the reference files from the `references/` directory:
   - `tx-exam-standards.md`, `tx-exceptions.md`, `tx-requirements.md`, `tx-forms.md`, `tx-opinion-template.md`, `tx-liens.md`, `tx-commercial.md`, `tx-condemnation.md`, `tx-manufactured-housing.md`, `tx-foreclosure.md`, `tx-minerals.md`, `tx-water-rights.md`, `tx-probate.md`, `tx-entities.md`, `tx-survey.md`, `tx-quality-checklist.md`, `tx-data-schema.md`
   - Optionally upload files from `data/` and `references/sample-outputs/`
4. **Save** and publish (private or shared link).
5. Upload a title commitment to your Custom GPT and it will follow the skill workflow.

#### Option B: ChatGPT Projects

1. Open **ChatGPT** → Create a new **Project**.
2. In **Project Instructions**, paste the contents of `SKILL.md`.
3. Upload reference files to the **Project Files** section.
4. All conversations within the project will have access to the skill.

---

### Google Gemini

Gemini can use skill files through Google AI Studio or Gems.

#### Option A: Google AI Studio

1. Go to **[aistudio.google.com](https://aistudio.google.com)**.
2. Create a new **Structured Prompt** or **Chat Prompt**.
3. In the **System Instructions** field, paste the full contents of `SKILL.md`.
4. Upload reference files as context documents.
5. Start your analysis conversation.

#### Option B: Gemini Gems

1. Open **Gemini** → **Gem Manager** → **New Gem**.
2. **Name:** TX Title Examiner
3. In the **Instructions** field, paste the contents of `SKILL.md`.
4. You can reference key portions of the supporting files in the instructions as well, or instruct the Gem to ask for documents to be uploaded during conversation.
5. **Save** and use the Gem for title analysis conversations.

> **Note:** Gemini's file upload limits may require you to consolidate some reference files. If so, combine the `tx-*.md` files into a single reference document.

---

## Quick Start

Once installed on any platform, try these prompts:

- *"Analyze this title commitment for [property address]. Identify all Schedule B exceptions and classify by risk level."*
- *"Review the chain of title and flag any gaps, breaks, or name discrepancies."*
- *"Generate a DRAFT title opinion letter for this residential transaction."*
- *"Create a requirements checklist prioritized for closing."*
- *"Analyze the mineral reservation in Exception #7 and recommend cure steps."*
- *"This is a commercial transaction — run the full commercial workflow including environmental and survey analysis."*
- *"The property has a manufactured home — check SOL status and TDHCA conversion requirements."*

---

## Customizing the Skill

This skill is a **living document** — it's designed to evolve with your practice.

**Common customizations:**

- **Opinion letter format:** Edit `references/tx-opinion-template.md` to match your firm's letterhead and style.
- **Quality standards:** Adjust `references/tx-quality-checklist.md` to add your firm's specific review criteria.
- **New reference areas:** Add new `references/tx-*.md` files for additional specialty areas (e.g., `tx-easements.md`, `tx-hoa-detailed.md`).
- **Decision logic:** Update the IF/THEN rules in `SKILL.md` to reflect your professional judgment on edge cases.
- **Data schema:** Modify `data/title-analysis-schema.json` to match your firm's data capture requirements.

Every edit you make trains the AI to work more like *you*.

---

## Important Disclaimer

All outputs generated by this skill are **DRAFT** documents intended for attorney review. AI-assisted analysis does not replace professional judgment. The attorney remains responsible for:

- Verifying all citations and legal standards
- Confirming factual accuracy against source documents
- Exercising independent professional judgment on all recommendations
- Final sign-off on any opinion letters or client-facing deliverables

---

## License

This skill file is shared for educational and professional use. Adapt it to your jurisdiction, practice area, and professional standards.

Built with the [Legal Skill File Framework](https://github.com) for AI-assisted legal analysis.
