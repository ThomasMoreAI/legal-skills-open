---
name: transcribe
title: Meeting Transcription with Speaker Diarization
description: Transcribe a meeting recording with speaker diarization using Deepgram API. Use when the user says "transcribe this recording", "расшифруй запись", "транскрибируй встречу", "сделай транскрипт".
author: ayusavin
author_url: https://github.com/ayusavin/skill-transcribe
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Meeting Transcription with Speaker Diarization

Transcribe an audio or video recording of a meeting using the Deepgram API (model nova-3) with automatic speaker diarization, then identify speakers by name.

The input file path is provided as `$ARGUMENTS`.

## Step 0: Environment Check

1. Check that `.env` exists in the project root and contains `DEEPGRAM_API_KEY`:
   ```
   grep DEEPGRAM_API_KEY .env
   ```
   If the key is missing or `.env` does not exist, read `${CLAUDE_SKILL_DIR}/references/deepgram-setup.md` and walk the user through the setup guide. Do not proceed until the key is configured.

2. Check that the Python virtual environment exists:
   ```
   test -d .venv || python3 -m venv .venv
   ```

3. Install dependencies:
   ```
   source .venv/bin/activate && pip install -q deepgram-sdk python-dotenv
   ```

## Step 1: Transcribe

Run the transcription script bundled with this skill:

```
source .venv/bin/activate && python ${CLAUDE_SKILL_DIR}/scripts/transcribe.py $ARGUMENTS
```

The script will:
- Send the file to Deepgram API (model nova-3, language: ru, diarization enabled)
- Cache the raw API response as `<file>.deepgram.json` (reused on subsequent runs — no duplicate API charges)
- Generate a draft transcript as `<file>.transcript.md` with generic speaker labels (Speaker 0, Speaker 1, ...)

If a `.deepgram.json` cache already exists, the script skips the API call and reuses it.

## Step 2: Auto-identify Speakers

Read the generated `.transcript.md` file and analyze the conversation to identify speakers:

1. Look for self-introductions: "Привет, я Никита", "Меня зовут Мария", etc.
2. Look for how speakers address each other: "Никита, расскажи...", "Как думаешь, Арсений?"
3. Look for role mentions: "я ведущий разработчик", "мы в Positive Technologies"
4. Cross-reference with known project participants if available (check `.assistant/submissions/` for speaker names)

Build a proposed mapping like:
```
Speaker 0 → Арсений Савин (track curator, leads the conversation)
Speaker 1 → Никита Гурняк (speaker, discusses their talk topic)
```

Present the proposed mapping to the user and ask for confirmation or corrections using AskUserQuestion. Show a few representative quotes from each speaker to help the user verify.

## Step 3: Relabel

Once the user confirms the speaker mapping, run the relabel command:

```
source .venv/bin/activate && python ${CLAUDE_SKILL_DIR}/scripts/transcribe.py $ARGUMENTS --relabel '{"Speaker 0": "Confirmed Name", "Speaker 1": "Another Name"}'
```

This rewrites `.transcript.md` with real names. The cached `.deepgram.json` is reused — no API call is made.

## Step 4: Save

Ask the user where to save the final transcript. Suggest a sensible default based on the project structure (e.g., a `transcripts/` directory).

Move the final `.transcript.md` to the chosen location with a descriptive filename.

Report the final file path to the user.

## Notes

- Supported formats: mp4, mp3, wav, m4a, webm, ogg, flac, and other common audio/video formats
- Transcription of a 1-hour recording takes ~1-2 minutes
- The Deepgram nova-3 model works well with Russian language
- Cached `.deepgram.json` files can be large (10-50 MB) — consider adding them to .gitignore
