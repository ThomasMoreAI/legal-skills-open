---
name: video-captions
title: Auto-detect language, output SRT
description: Generate professional captions and subtitles with multi-engine transcription, word-level timing, styling presets, and burn-in.
author: clawic
author_url: https://github.com/clawic/skills/tree/main/skills/video-captions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

## When to Use

User needs captions or subtitles for video content. Agent handles transcription, timing, formatting, styling, translation, and burn-in across all major formats and platforms.

## Quick Reference

| Topic | File |
|-------|------|
| Transcription engines | `engines.md` |
| Output formats | `formats.md` |
| Styling presets | `styling.md` |
| Platform requirements | `platforms.md` |

## Core Rules

### 1. Engine Selection by Context

| Scenario | Engine | Why |
|----------|--------|-----|
| Default (recommended) | Whisper local | 100% offline, no data leaves machine |
| Apple Silicon | MLX Whisper | Native acceleration, still local |
| Word timestamps | whisper-timestamped | DTW alignment, still local |

Default: Whisper local (turbo model). See `engines.md` for optional cloud alternatives.

### 2. Format Selection by Platform

| Platform | Format | Notes |
|----------|--------|-------|
| YouTube | VTT or SRT | VTT preferred |
| Netflix/Pro | TTML | Strict timing rules |
| Social (TikTok, IG) | Burn-in (ASS) | Embedded in video |
| General | SRT | Universal compatibility |
| Karaoke/effects | ASS | Advanced styling |

Ask user's target platform if not specified.

### 3. Professional Timing Standards

**Netflix-compliant (default):**
- Min duration: 5/6 second (0.833s)
- Max duration: 7 seconds
- Max chars/line: 42
- Max lines: 2
- Gap between subtitles: 2+ frames

**Social media:**
- Shorter segments (2-4 words)
- More frequent breaks
- Centered or dynamic positioning

### 4. Segmentation Rules

Break lines:
- After punctuation marks
- Before conjunctions (and, but, or)
- Before prepositions

Never separate:
- Article from noun
- Adjective from noun
- First name from last name
- Verb from subject pronoun
- Auxiliary from verb

### 5. Word-Level Timestamps

Use word timestamps for:
- Karaoke-style highlighting
- Precise sync verification
- TikTok/Instagram animated captions
- Quality checking transcript accuracy

Enable with `--word-timestamps` flag.

### 6. Speaker Identification

For multi-speaker content:
- Use diarization (pyannote local, or cloud APIs if configured)
- Format: `[Speaker 1]` or `[Name]` if known
- SDH format: `JOHN: What do you think?`

### 7. Quality Verification

Before delivering:
- Check sync at start, middle, end
- Verify character limits per line
- Confirm speaker labels if multi-speaker
- Test burn-in render quality

## Workflow

### Basic Transcription
```bash
# Auto-detect language, output SRT
whisper video.mp4 --model turbo --output_format srt

# Specify language
whisper video.mp4 --model turbo --language es --output_format srt

# Multiple formats
whisper video.mp4 --model turbo --output_format all
```

### Word-Level Timestamps
```bash
# Using whisper-timestamped
whisper_timestamped video.mp4 --model large-v3 --output_format srt

# With VAD pre-processing (reduces hallucinations)
whisper_timestamped video.mp4 --vad silero --accurate
```

### Styled Subtitles (ASS)
```bash
# Generate SRT first, then convert with style
ffmpeg -i video.mp4 -vf "subtitles=video.srt:force_style='FontName=Arial,FontSize=24,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2'" output.mp4
```

### Burn-In for Social Media
```bash
# TikTok/Instagram style (centered, bold)
ffmpeg -i video.mp4 -vf "subtitles=video.srt:force_style='FontName=Montserrat-Bold,FontSize=32,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=3,Shadow=0,Alignment=10,MarginV=50'" output.mp4

# Netflix style (bottom, clean)
ffmpeg -i video.mp4 -vf "subtitles=video.srt:force_style='FontName=Netflix Sans,FontSize=48,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,Outline=2,Shadow=1,Alignment=2'" output.mp4
```

### Translation
```bash
# Transcribe + translate to English
whisper video.mp4 --model turbo --task translate --output_format srt
```

### Format Conversion
```bash
# SRT to VTT
ffmpeg -i video.srt video.vtt

# SRT to ASS (for styling)
ffmpeg -i video.srt video.ass
```

## Caption Traps

- **Hallucinations on silence** → Use VAD pre-processing or trim silent sections
- **Wrong language detection** → Specify `--language` explicitly for mixed content
- **Timing drift in long videos** → Use word timestamps + manual spot-check
- **Character limit violations** → Set `--max_line_width 42` for Netflix compliance
- **Missing speaker IDs** → Enable diarization for multi-speaker content
- **Burn-in quality loss** → Use high bitrate output (`-b:v 8M`)

## Common Scenarios

### YouTube Video
1. Transcribe: `whisper video.mp4 --output_format vtt`
2. Upload .vtt to YouTube Studio
3. Review auto-sync suggestions

### TikTok/Instagram Reel
1. Transcribe with word timestamps
2. Apply bold animated style
3. Burn-in: `ffmpeg -i video.mp4 -vf "subtitles=video.ass" -c:a copy output.mp4`
4. Export at platform resolution

### Netflix/Professional
1. Use Whisper large-v3 for best local accuracy
2. Export TTML format
3. Verify: 42 chars/line, 2 lines max, timing gaps
4. Include translator credit as last subtitle

### Podcast/Interview
1. Enable speaker diarization
2. Format as dialogue: `[SPEAKER]: text`
3. SDH option: include `[music]`, `[laughter]` descriptions

### Foreign Film Translation
1. Transcribe in original language
2. Translate: `--task translate` for English
3. Or use external translation + timing sync

## External Endpoints

**Default: 100% LOCAL processing. No network calls.**

| Endpoint | Data Sent | When Used |
|----------|-----------|-----------|
| Whisper (local) | None (local) | Default — always |
| api.assemblyai.com | Audio file | Only if user sets ASSEMBLYAI_API_KEY |
| api.deepgram.com | Audio file | Only if user sets DEEPGRAM_API_KEY |

Cloud APIs are **documented as alternatives** but never used unless user explicitly provides API keys and requests cloud processing. By default, all processing stays on your machine.

## Security & Privacy

**Default workflow is 100% offline:**
- Whisper runs locally on your machine
- Generated subtitle files stay local
- Burned-in videos stay local
- No network calls made

**Cloud APIs are OPTIONAL and OPT-IN:**
- Only used if you set `ASSEMBLYAI_API_KEY` or `DEEPGRAM_API_KEY`
- Only triggered when you explicitly use cloud engine commands
- If you never set these keys, no audio ever leaves your machine

**This skill does NOT:**
- Upload anything by default
- Require internet connection for basic use
- Store data externally

## Related Skills
Install with `clawhub install <slug>` if user confirms:
- `ffmpeg` — video/audio processing
- `video` — general video tasks
- `video-edit` — video editing
- `audio` — audio processing

## Feedback

- If useful: `clawhub star video-captions`
- Stay updated: `clawhub sync`
