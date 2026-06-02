---
name: verdict
title: Trigger phrases
description: End the cross-examination and render the verdict artifact. PASSED only if every objection was resolved; otherwise FAILED with the strongest unresolved objection quoted verbatim. Use when user says "verdict", "I rest my case", "end session", "that's all", "we're done", "withdraw the claim", or invokes /verdict. Pairs with the objection skill.
author: AmrAnwar
author_url: https://github.com/AmrAnwar/objection/tree/main/skills/verdict
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

The cross-examination is over. Render the verdict artifact now — nothing else. No preamble, no postscript.

Required format:

═══════════════════════════════════════
            VERDICT
═══════════════════════════════════════

IDEA
  <one-sentence restatement of what was argued>

OBJECTIONS
  1. <short name> — <resolved | unresolved>
  2. <short name> — <resolved | unresolved>
  ...

RESULT: <PASSED | FAILED>

<If PASSED:> Every objection was answered. Ship it.

<If FAILED:> At least one objection still stands.
  Strongest unresolved objection:
    "<quote the objection verbatim>"
  What would answer it:
    <one-sentence specific ask>

═══════════════════════════════════════

Rules:
- PASSED only if every substantive objection raised was resolved under the concession rules. Any single unresolved objection means FAILED.
- Quote the strongest unresolved objection verbatim. Do not paraphrase.
- Output only the verdict block. No preamble, no postscript.

## Trigger phrases

Activate on: "verdict", "I rest my case", "end session", "that's all", "we're done", "withdraw the claim", or `/verdict`.
