# Redline Emailer

A [Claude Code skill](https://docs.anthropic.com/en/docs/claude-code) that turns contract redlines into copy-paste-ready emails — tone-matched to the recipient. Plain English for your client, professional legal cover for opposing counsel.

## What it does

- **Reads tracked changes** from a `.docx` with Track Changes, a redlined PDF, or a verbal description of edits
- **Generates a client email** that explains each change in plain English — what changed, why, and what it means for them
- **Generates a counsel email** that lists changes by section number with precise references, neutral tone, no over-explanation
- **Adapts tone automatically** — casual, contentious, sophisticated client, first draft, multiple rounds
- **Validates before delivery** — checks for legalese leaks, missing section context, completeness, neutral tone, and reading level

## Input modes

| Mode | Trigger | How it works |
|---|---|---|
| `.docx` tracked changes | Drop a Word file with Track Changes | Parses Word XML for insertions, deletions, and comments |
| Redlined PDF | Drop a PDF with strikethrough/underline formatting | Extracts changes from visual formatting |
| Verbal description | Describe the changes, no file needed | Structures your description into the email |

The skill auto-detects the mode from what you provide.

## Usage

| You say | What happens |
|---|---|
| "Write the redline email for opposing counsel" + drop .docx | Extracts changes, generates a professional cover email with section references |
| "Summarize these changes for the client" + drop PDF | Parses redlines, generates a plain-English summary email |
| "Turn this redline into an email" | Asks: client or counsel? Then generates the appropriate version |
| "We changed the liability cap to 24 months and added a termination for convenience" | Generates email from your verbal description |

After delivery, it offers to adjust tone, add/remove details, or generate a version for the other recipient.

## Installation

```
claude install-skill ./redline-emailer
```

## Skill contents

```
redline-emailer/
├── SKILL.md                          <- skill definition and workflow
└── reference/
    ├── email-templates.md            <- tone guides and structural templates
    ├── intake-questions.md           <- minimal intake flow
    └── validation-rules.md           <- quality checks per recipient type
```

## License

MIT
