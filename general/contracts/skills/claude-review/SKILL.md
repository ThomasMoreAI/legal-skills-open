---
name: claude-review
title: /claude-review
description: Agentic contract review using superdoc-redlines. Spawns parallel sub-agents for comprehensive document review with tracked changes.
author: yuch85
author_url: https://github.com/yuch85/superdoc-redlines/tree/main/.claude/skills/claude-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# /claude-review

Agentic contract review skill that uses the superdoc-redlines library to review and amend legal documents with tracked changes. For large documents (>50K tokens), spawns parallel sub-agents for comprehensive coverage.

## Usage

```
/claude-review [--single-agent|--multi-agent] <document> <instructions>
```

**Arguments:**
- `--single-agent` (optional) - Force single-agent workflow regardless of document size
- `--multi-agent` (optional) - Force multi-agent workflow regardless of document size
- `<document>` - Path to the DOCX file to review
- `<instructions>` - Review instructions (e.g., "Convert from UK to Singapore jurisdiction")

**Examples:**
```
/claude-review contract.docx Convert from UK to Singapore law
/claude-review --multi-agent contract.docx Convert from UK to Singapore law
/claude-review --single-agent large-contract.docx Review warranties only
/claude-review ./contracts/bta.docx Review warranties and update statutory references
/claude-review "Business Transfer Agreement.docx" Adapt for Singapore jurisdiction, update all UK statutes
```

## How It Works

This skill reads `$ARGUMENTS` for the document path and instructions.

### Argument Parsing

Parse arguments as follows:
1. Check for optional workflow flags: `--single-agent` or `--multi-agent` (if present, remove from arguments)
2. First remaining argument: document path (may be quoted if contains spaces)
3. Remaining arguments: review instructions (joined as a single string)

If arguments are missing, prompt the user for:
1. Document path
2. Review instructions

**Workflow Override:**
- If user specifies `--single-agent` or `--multi-agent`, that workflow MUST be used
- User-specified workflow overrides any automatic selection based on document size
- If no workflow flag is provided, use automatic selection based on document size

### Workflow Selection

**Priority 1 - User Override (if specified):**
- If user provides `--single-agent` flag: Use single-agent workflow
- If user provides `--multi-agent` flag: Use multi-agent workflow

**Priority 2 - Automatic Selection (if no flag):**
Based on document size, choose the appropriate workflow:

| Document Size | Workflow | Reason |
|---------------|----------|--------|
| < 50K tokens | Single-agent | Direct review per CONTRACT-REVIEW-SKILL.md |
| >= 50K tokens | Multi-agent | Orchestrator + sub-agents per CONTRACT-REVIEW-AGENTIC-SKILL.md |

**CRITICAL: User-specified workflow flags override automatic selection.**

## Step-by-Step Procedure

### Step 1: Validate Document

```bash
cd /home/tyc/ross-ide-contract/superdoc-redlines
node superdoc-redline.mjs read --input "<document>" --stats-only
```

Verify the document exists and get statistics:
- `blockCount` - Number of blocks
- `estimatedTokens` - Token estimate
- `recommendedChunks` - Suggested chunk count

### Step 2: Extract Document Structure

```bash
node superdoc-redline.mjs extract --input "<document>" --output "<document>-ir.json"
```

This creates the block ID mapping needed for edits.

### Step 3: Choose Workflow

**CRITICAL: If user specified --single-agent or --multi-agent flag, use that workflow regardless of document size.**

**Otherwise, use automatic selection:**

**If estimatedTokens < 50,000:** Use single-agent workflow
- Follow CONTRACT-REVIEW-SKILL.md methodology
- Two-pass review (Discovery + Amendment)
- Output: `<document>-edits.json`

**If estimatedTokens >= 50,000:** Use multi-agent workflow
- Follow CONTRACT-REVIEW-AGENTIC-SKILL.md methodology
- Orchestrator performs discovery, spawns sub-agents
- Sub-agents work in parallel on assigned sections
- Merge results into `merged-edits.json`

### Step 4: Discovery Pass

Read all chunks to build the Context Document:

```bash
# Read each chunk until hasMore: false
node superdoc-redline.mjs read --input "<document>" --chunk 0 --max-tokens 10000
node superdoc-redline.mjs read --input "<document>" --chunk 1 --max-tokens 10000
# ... continue
```

Build Context Document with:
- Defined Terms Registry (all terms and their usage locations)
- Provisions to change (based on user instructions)
- Cross-reference map
- Section map with block ranges

### Step 5: Amendment Pass

#### Single-Agent Path
Process each chunk with full Context Document, drafting exact amendments.

#### Multi-Agent Path
1. Plan sub-agent assignments (non-overlapping block ranges)
2. Spawn sub-agents in parallel using Task tool:

```
Task({
  subagent_type: "general-purpose",
  description: "Review [section] blocks b[start]-b[end]",
  prompt: "[Sub-agent prompt with Context Document and block range]"
})
```

3. Each sub-agent produces `edits-[section].json`
4. Merge all edit files:

```bash
node superdoc-redline.mjs merge \
  edits-*.json \
  -o merged-edits.json \
  -c combine \
  -v "<document>"
```

### Step 6: Validate and Apply

```bash
# Validate
node superdoc-redline.mjs validate --input "<document>" --edits "<edits-file>"

# Apply with track changes
node superdoc-redline.mjs apply \
  --input "<document>" \
  --output "<document>-amended.docx" \
  --edits "<edits-file>" \
  --author-name "AI Legal Counsel"
```

### Step 7: Report Results

Report to user:
- Total edits applied
- Breakdown by category (replacements, deletions, insertions, comments)
- Output file path
- Any issues or items needing human review

## Reference Documentation

The detailed methodology is documented in:

- **Single-agent workflow:** `superdoc-redlines/CONTRACT-REVIEW-SKILL.md`
- **Multi-agent workflow:** `superdoc-redlines/CONTRACT-REVIEW-AGENTIC-SKILL.md`
- **Library reference:** `superdoc-redlines/README.md`
- **Quick skill reference:** `superdoc-redlines/SKILL.md`

## Sub-Agent Prompt Template

When spawning sub-agents for multi-agent workflow, use this template:

```markdown
You are a contract review sub-agent. Review your assigned section and produce an edits JSON file.

## Assignment
- Block Range: b[START] to b[END]
- Section: [SECTION_NAME]
- Output: edits-[section].json

## Review Instructions
[USER_INSTRUCTIONS]

## Context Document
[FULL_CONTEXT_DOCUMENT]

## Procedure
1. Read your assigned chunks:
   ```bash
   cd /home/tyc/ross-ide-contract/superdoc-redlines
   node superdoc-redline.mjs read --input "[DOCUMENT]" --chunk [N] --max-tokens 10000
   ```

2. For each block in your range, assess amendments needed based on:
   - The review instructions
   - Defined terms changes from Context Document
   - Provisions requiring deletion or replacement

3. Draft EXACT replacement text (not vague directions)

4. Create edits file:
   ```json
   {
     "version": "0.2.0",
     "agent": "[AGENT_ID]",
     "blockRange": { "start": "b[START]", "end": "b[END]" },
     "edits": [...]
   }
   ```

5. Save to: edits-[section].json

## Rules
- ONLY edit blocks in your assigned range
- Draft exact replacement text
- Use diff: true for surgical edits, diff: false for rewrites
- Cite Singapore statutes with year (e.g., "Companies Act 1967")
```

## Working Directory

All commands should be run from:
```
/home/tyc/ross-ide-contract/superdoc-redlines
```

## Output Files

| File | Purpose |
|------|---------|
| `<document>-ir.json` | Extracted document structure with block IDs |
| `<document>-context.md` | Context Document (for multi-agent) |
| `edits-*.json` | Edit files from each agent |
| `merged-edits.json` | Combined edits (multi-agent only) |
| `<document>-amended.docx` | Final output with tracked changes |

## Error Handling

- If document doesn't exist: Report error, ask for correct path
- If sub-agent fails: Re-spawn for remaining blocks or process directly
- If merge conflicts: Review and resolve, re-merge with appropriate strategy
- If validation fails: Identify and fix problematic edits, re-validate
