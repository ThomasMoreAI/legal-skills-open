# Advanced Interview — Conditionals, Loops, and Validation

This file is read by the Orchestrator when the manifest contains `conditionals`, `loops`, or `validation` sections. It extends Phases 3–5 of SKILL.md.

---

## Phase 3 Extensions

### Auto-Grouping with Conditionals and Loops

When `groups` is absent from the manifest and you auto-group:
- Identify gate variables (from `dependencies`) and place them in groups that come **before** their dependent conditional groups.
- Create one group per conditional block containing its `if_variables` (and `else_variables` if any).
- Create one group per loop block, placed last.

Order: unconditional groups first, conditional groups interleaved after their gate variables have been collected, loop groups last.

### Planning Questions for Advanced Types

- For `boolean` types (gate variables): phrase as a yes/no question.
- For `choice` types that gate conditionals: present the available options and note which triggers follow-up questions.

---

## Phase 4b — Conditional Groups

After collecting a gate variable's value, evaluate the condition:

**Boolean gate** (`gate_type: boolean`):
- `true` if the user answered yes/affirmative/true
- `false` otherwise

**Equality gate** (`gate_type: equality`):
- `true` if the collected value of `gate_variable` equals `gate_value`
- `false` otherwise

Then:
1. If condition is **true**: present the `if_variables` group and collect answers.
2. If condition is **false** and `else_variables` is non-empty: present the `else_variables` group and collect answers.
3. If condition is **false** and `else_variables` is empty: skip. Inform the user naturally (e.g., "Since you chose cheque, we'll skip the bank details section.").

When introducing a conditional group, provide context: "Since you indicated IP should be assigned, I'll need a few more details about that."

Log a `group_start` entry with `branch`: `"if"`, `"else"`, or `"skipped"`. If skipped, log a `skip` entry with the gate variable name, value, and readable reason.

---

## Phase 4c — Loop Groups

For each loop group:

1. **Introduce**: Tell the user what you're collecting and that you'll ask one item at a time.
2. **Collect first item**: Ask for all sub-variables as a group.
3. **Confirm the item**: Summarize what you captured.
4. **Prompt for more**: "Would you like to add another [item]?"
5. **Repeat** steps 2-4 for each additional item.
6. **Minimum check**: Ensure at least `min_items` (default 1) items are collected. If the user tries to stop early, inform them of the minimum.
7. **Summary**: After the user finishes, summarize all items as a numbered list.

Log a `group_start` entry once before item 1, then a `loop_item` entry per confirmed item with `item_index`, `question`, `answer`, and `values` (parsed sub-variable dict).

Store the collected data as a list of dictionaries under the collection name.

---

## Phase 5b — Validation Rules

If the manifest includes `validation` rules, evaluate them after presenting the summary:

1. Parse each rule (e.g., `"end_date > effective_date"`).
2. Compare the collected values accordingly (dates compared chronologically, numbers numerically).
3. If any rule fails, report the error message from the manifest and ask the user to correct the relevant values.
4. Re-validate after corrections.
5. Do not proceed to rendering until all rules pass.

---

## Phase 5c Extensions — Gate and Loop Edits

During confirmation, the user may make edits that affect conditionals or loops:

- **Change a gate answer**: This reveals or hides dependent sections.
  - If changing from false to true: ask the newly-required conditional questions before re-confirming.
  - If changing from true to false: remove the previously-collected conditional values and mark the section as skipped.
  - If changing a choice value that gates a conditional: re-evaluate which conditional sections apply.
- **Add loop items**: Re-enter the loop collection flow, appending to the existing list.
- **Edit a loop item**: Ask which item number to edit, then ask for updated values.
- **Remove a loop item**: Ask which item number to remove. Enforce `min_items` after removal.

If the user re-triggers conditional questions (false -> true), also append `question` and `answer` entries for those newly-asked questions.

Append a `correction` entry with optional `note` if the change triggered conditional re-evaluation (e.g., "Changing payment_method from bank_transfer to cheque removed Bank Details section").

---

## Summary Display with Advanced Features

When presenting the Phase 5a summary:
- **Conditional sections**: If the condition was true, display collected values. If skipped, show "*Skipped (not applicable)*".
- **Loop items**: Show as a numbered list under the group heading.
