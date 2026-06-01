---
name: transcribe-calvin-corbett
title: Transcribe
description: Convert audio or video speech into structured text with timestamps, speaker hints, and downstream-ready summaries.
author: Calvin-Corbett
author_url: https://github.com/Calvin-Corbett/thomas/tree/main/skills/transcribe
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Transcribe

Use this skill when Thomas needs reliable text from audio or video before analysis or editing work continues.

## Workflow
1. Confirm the source file, language, and expected output shape.
2. Transcribe with timestamps and speaker labeling when available.
3. Normalize names, obvious transcription errors, and action items carefully.
4. Preserve uncertainty markers when speech is ambiguous.
5. Hand off both the transcript and any concise summary the task needs.

## Rules
- Do not invent speaker certainty that the audio does not support.
- Keep timestamps when later editing or clipping depends on them.
