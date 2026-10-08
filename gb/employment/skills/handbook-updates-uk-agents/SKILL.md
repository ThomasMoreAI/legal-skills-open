---
name: handbook-updates-uk-agents
title: Handbook Updates
description: Diff a proposed handbook change against the current version, flag ripple effects and jurisdiction supplement impacts. Use when user says "update the handbook", "add this to the handbook", "handbook change", or has a policy ready for insertion.
author: uk-agents
author_url: https://github.com/uk-agents/uk-legal-plugins/tree/main/employment-legal-uk/skills/handbook-updates
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: gb
practice: employment
language: en
---

# Handbook Updates

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal-uk:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Handbook changes have ripple effects. Change the holiday policy and you've affected the final pay calculation, the leave policy cross-reference, and any Northern Ireland supplement. This skill finds the ripples before they become inconsistencies.

## Load context

`~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md` → handbook location, jurisdiction supplements list, update cadence.

## Workflow

### Step 1: Get the change

- What section is changing?
- What's the new language?
- Why? (Legal requirement, policy decision, cleanup)

### Step 2: Diff against current

Read the current handbook section. Show the diff:

```diff
- [old language]
+ [new language]
```

### Step 3: Find cross-references

Search the handbook for references to the changed section:

- Other policies that cite this one ("see the holiday policy for accrual rates")
- Defined terms that this section uses or defines
- Jurisdiction supplements that modify this section

Each cross-reference: does it still make sense after the change? Flag any that break.

### Step 4: Jurisdiction supplement impact

For each jurisdiction supplement in `~/.claude/plugins/config/uk-legal-plugins/employment-legal-uk/CLAUDE.md`:

- Does this supplement modify the section being changed?
- Does the change make the supplement obsolete, wrong, or incomplete?
- Does the change create a need for a *new* supplement in a state that didn't need one before?

### Step 5: Promise check

Is the change reducing something the old version promised?

If yes: that's a risk. Employment tribunal judges read handbook policies as creating legitimate expectations enforceable as contractual terms or implied duties of trust and confidence. Reducing a benefit unilaterally may constitute a breach of contract or a constructive dismissal risk. Reducing a benefit may need more than just updating the document — advance notice, consultation, consideration (e.g., a corresponding enhancement elsewhere), and in some cases it cannot be done retroactively without individual consent.

Flag this. Don't block it — but flag it.

## Output

```markdown
## Handbook Update: [Section name]

### Change

[diff]

### Cross-reference impact

| Section | References changed section | Still accurate? | Fix needed |
|---|---|---|---|
| [name] | [how] | ✅/⚠️ | [what] |

### Jurisdiction supplement impact

| Jurisdiction | Current supplement | After change | Action |
|---|---|---|---|
| Northern Ireland | [what it says] | [still valid / obsolete / needs update] | [none / update / new supplement needed] |
| [Country] | [what it says] | [still valid / obsolete / needs update] | [none / update / new supplement needed] |

### Promise check

[If reducing a benefit: flag + jurisdictional risk note]

### Ready to publish

- [ ] Cross-references updated
- [ ] Jurisdiction supplements updated
- [ ] [If benefit reduction: notice/consideration addressed]
- [ ] Version number and date updated
- [ ] Acknowledgment process (if required)
```

## What this skill does not do

- Approve handbook changes. HR/legal leadership does.
- Communicate changes to employees.
- Track acknowledgments.
