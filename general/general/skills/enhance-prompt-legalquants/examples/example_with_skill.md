# Worked Example — Expansion When a Skill Is Attached

This example shows Enhance Prompt working alongside an attached skill. The user has attached NDA Review and typed a short prompt; Enhance Prompt's job is to make the prompt explicit *without* duplicating or conflicting with the attached skill's instructions.

## Input

```yaml
raw_input: "review this please"
attached_skills:
  - name: nda-review
    description: |
      Use when the user uploads or pastes a non-disclosure agreement and asks
      for review, redline, risk assessment, or a recommendation on whether to
      sign. Identifies missing standard protections, one-sided or unusual
      provisions, and operational issues; produces a structured report with
      severity ratings and citations to specific clauses, calibrated to the
      user's perspective (discloser, recipient, or mutual).
attached_files:
  - name: "Acme_Vendor_NDA.pdf"
    type: pdf
    description: "Counterparty-prepared NDA, 4 pages"
chat_history: []
jurisdiction: "Delaware"
```

## Skip-condition check

- Already well-structured? No — 3 words.
- Conversational? No — task instruction.
- Follow-up? No — empty chat history.
- Operational? Yes-ish — "review this" is a direct operational ask. But the file is attached, the skill expects perspective input that has not been provided, and the prompt is ambiguous enough that the model may guess incorrectly. Expansion has value, but a *minimal* expansion focused only on filling skill inputs.
- **Skill attached that handles this:** yes — NDA Review. The skill's scope supersedes for review methodology. Enhance Prompt should not duplicate review instructions; it should only fill in skill inputs the user did not provide.

Proceed with **scoped** expansion: do not expand into review methodology (skill owns that). Do expand to fill the skill's required `perspective` input, which the user has not provided.

## Gap identification

Walk through the seven elements, scoped to what NDA Review does *not* already handle:

- **Role:** owned by the skill (in-house counsel, NDA review). Skip.
- **Jurisdiction:** Delaware is configured. NDA Review accepts jurisdiction as optional. Pass through.
- **Audience:** owned by the skill. Skip.
- **Scope:** owned by the skill. Skip.
- **Output format:** owned by the skill. Skip.
- **Constraints:** owned by the skill. Skip.
- **Citation expectations:** owned by the skill. Skip.

The only gap that Enhance Prompt should surface is the missing **perspective** input that NDA Review requires. The skill's frontmatter description specifies that perspective must be provided. If not, NDA Review will ask the user — but this creates an extra round-trip. Enhance Prompt can ask for perspective up-front so the user provides it once.

This is a special case: rather than expanding the prompt itself, Enhance Prompt should surface the missing skill input as a question to the user and let the user answer before the prompt is submitted.

## Output

```yaml
expansion_applied: true

expanded_prompt: |
  Review the attached NDA (Acme_Vendor_NDA.pdf). My perspective for this
  review is [PERSPECTIVE_TO_BE_FILLED]. Governing-law jurisdiction is
  Delaware. Apply the NDA Review skill.

reasoning:
  - "The NDA Review skill needs to know which side you're on — that fundamentally changes the analysis. I've left a placeholder for you to fill in (discloser / recipient / mutual)."
  - "Carried through your configured jurisdiction (Delaware) so the skill can flag any jurisdiction-specific issues."
  - "Did not add review methodology or output format — the NDA Review skill defines those, and duplicating them here would just create noise."

skip_reason: null

preview_to_user: |
  ## Enhance Prompt — Review before sending

  The NDA Review skill needs one piece of information you haven't provided yet:

  **Which side are you on for this review?**

  - **Discloser** — you're sharing information; you want strong protections on the recipient
  - **Recipient** — you're receiving information; you want narrow obligations on you
  - **Mutual** — both parties are exchanging information; you want balanced terms

  [ Discloser ] [ Recipient ] [ Mutual ]

  Once you choose, your prompt will be submitted as:

  > "Review the attached NDA (Acme_Vendor_NDA.pdf). My perspective for this
  > review is [your choice]. Governing-law jurisdiction is Delaware. Apply
  > the NDA Review skill."

  [ Edit ] [ Skip Enhance Prompt and submit original ]
```

## What this example demonstrates

- **Enhance Prompt respects skill boundaries.** When NDA Review handles review methodology, Enhance Prompt does not. The expansion is minimal — perspective and jurisdiction only.
- **Enhance Prompt fills skill inputs proactively.** Rather than letting the model ask for perspective in the response (which forces a second round-trip), Enhance Prompt surfaces the missing input as part of the review-before-sending screen.
- **The application UI handles the input collection.** Enhance Prompt returns the placeholder; the application renders it as a tappable choice. Skill inputs become first-class UI elements.
- **No duplication or conflict with skill instructions.** Enhance Prompt does not add "identify missing standard protections" or "produce a structured report" — those come from the skill.
- **The reasoning explains the restraint as well as the additions.** "Did not add review methodology or output format — the NDA Review skill defines those" educates the user that Enhance Prompt knows when to stop.

## A note on this pattern

This pattern — "Enhance Prompt fills missing skill inputs" — is a core integration point between Enhance Prompt and the rest of the LQ.AI skill ecosystem. Skills declare required and optional inputs in their frontmatter. Enhance Prompt reads those declarations from `attached_skills` and surfaces the missing required inputs to the user in a structured way before the prompt is submitted.

The result: skills with structured inputs become easier to use, because the application surfaces the inputs as form-like fields rather than waiting for the model to ask. This is one of the reasons the LQ.AI extension under `lq_ai:` in skill frontmatter exists — to enable exactly this kind of structured cooperation between skills.
