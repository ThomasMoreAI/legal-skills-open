---
name: handbook-updates-bossmann007
title: Handbook Updates
description: Diff a proposed handbook change against the current version, flag ripple effects and state supplement impacts. Use when user says "update the handbook", "add this to the handbook", "handbook change", or has a policy ready for insertion.
author: Bossmann007
author_url: https://github.com/Bossmann007/claude-legal-br/tree/main/employment-legal/skills/handbook-updates
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: employment
language: en
---

# Handbook Updates

## Matter context

**Matter context.** Check `## Matter workspaces` in the practice-level CLAUDE.md. If `Enabled` is `✗` (the default for in-house users), skip the rest of this paragraph — skills use practice-level context and the matter machinery is invisible. If enabled and there is no active matter, ask: "Which matter is this for? Run `/employment-legal:matter-workspace switch <slug>` or say `practice-level`." Load the active matter's `matter.md` for matter-specific context and overrides. Write outputs to the matter folder at `~/.claude/plugins/config/claude-for-legal/employment-legal/matters/<matter-slug>/`. Never read another matter's files unless `Cross-matter context` is `on`.

---

## Purpose

Handbook changes have ripple effects. Change the PTO policy and you've affected the final pay calculation, the leave policy cross-reference, and three state supplements. This skill finds the ripples before they become inconsistencies.

## Load context

`~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md` → handbook location, state supplements list, update cadence.

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

- Other policies that cite this one ("see the PTO policy for accrual rates")
- Defined terms that this section uses or defines
- State supplements that modify this section

Each cross-reference: does it still make sense after the change? Flag any that break.

### Step 4: State supplement impact

For each state supplement in `~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md`:

- Does this supplement modify the section being changed?
- Does the change make the supplement obsolete, wrong, or incomplete?
- Does the change create a need for a *new* supplement in a state that didn't need one before?

### Step 5: Promise check

Is the change reducing something the old version promised?

If yes: that's a risk. Some states treat handbook policies as contractual. Reducing a benefit may need more than just updating the document — advance notice, consideration, or in some cases it can't be done retroactively.

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

### State supplement impact

| State | Current supplement | After change | Action |
|---|---|---|---|
| [state] | [what it says] | [still valid / obsolete / needs update] | [none / update / new supplement needed] |

### Promise check

[If reducing a benefit: flag + jurisdictional risk note]

### Ready to publish

- [ ] Cross-references updated
- [ ] State supplements updated
- [ ] [If benefit reduction: notice/consideration addressed]
- [ ] Version number and date updated
- [ ] Acknowledgment process (if required)
```

## Consequential-action gate (before publishing handbook changes)

**Before publishing an updated handbook or sending it to employees:** Read `## Who's using this` in ~/.claude/plugins/config/claude-for-legal/employment-legal/CLAUDE.md. If the Role is **Non-lawyer**:

> Publishing a handbook change affects your entire workforce and can have legal consequences. It establishes (or modifies) terms of employment that may be deemed contractual or that trigger compliance obligations. Have you reviewed this with an attorney? If yes, proceed. If no, here's a brief to bring to them:
>
> - What changed and why (cost savings, legal requirement, policy refinement, etc.)
> - Whether this change reduces, maintains, or improves employee benefits or protections
> - If reducing a benefit (PTO, insurance, severance, leave policy, etc.) — what is the legal notice required, what is the effective date, and do existing employees need consent or consideration?
> - Whether the change affects different employee populations differently (e.g., remote vs. in-office, unionized vs. non-union, different states/countries)
> - Whether the change triggers any regulatory notice requirement (state leave laws, federal WARN Act if relevant, union notification if applicable)
> - Whether the change could be perceived as retaliatory or discriminatory against a protected class or individual
> - State-specific risks (some states, like California, limit reductions in handbook-promised benefits and may imply a contract from a handbook policy)
> - What could go wrong (wage claims, misclassification claims, regulatory audit of the accuracy of the handbook vs. actual practice, grievances)
> - What to ask the attorney (is this change legally enforceable; do we need employee acknowledgment; should we phase it in; should we offer something in exchange for the change)
>
> If you need to find a lawyer: the OAB (Ordem dos Advogados do Brasil) seccional of your estado is the starting point — its service for referral or the local subsecção can point you to counsel. (For a US or multi-country policy: contact the bar or professional body in the relevant jurisdiction.)

Do not publish a final handbook change past this gate without an explicit yes. A marked-DRAFT for attorney review is fine.

---

## What this skill does not do

- Approve handbook changes. HR/legal leadership does.
- Communicate changes to employees.
- Track acknowledgments.
