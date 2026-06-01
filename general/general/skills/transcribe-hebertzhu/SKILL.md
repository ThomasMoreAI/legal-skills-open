---
name: transcribe-hebertzhu
title: Transcribe
description: Use when the user wants to transcribe audio or video, extract speech to text, or label speakers with optional diarization; prefer the bundled `scripts/transcribe_diarize.py` and require `OPENAI_API_KEY`.
author: hebertzhu
author_url: https://github.com/hebertzhu/agent-foundry/tree/main/skills/transcribe
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Transcribe

## Intent
- Use for converting recordings into text, optional speaker diarization, and structured transcript output for meetings, interviews, or media assets.

## Default operating pattern
1. Confirm the audio source, expected output format, and whether the user needs plain text or diarized output.
2. Collect any hints that materially improve recognition quality: language, known speaker names, or reference audio.
3. Prefer the bundled `scripts/transcribe_diarize.py` so the workflow remains deterministic and reusable.
4. Start with the simplest successful output, then add diarization or richer structure only when the user actually needs it.
5. Validate transcript quality, speaker labels, and segment boundaries before calling it done.

## Bundled helper
- `scripts/transcribe_diarize.py` supports transcription plus optional diarization with OpenAI audio models.

## Pack fit
- Included in: `docs-media`
- Best for turning audio or video into reusable text artifacts.

## Boundary
- Do not ask the user to paste the API key into chat.
- Do not overstate diarization confidence if the speaker separation is ambiguous.
