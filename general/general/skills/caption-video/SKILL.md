---
name: caption-video
title: Caption Video
description: Generate styled SRT/VTT captions and optionally burn them into video with platform-appropriate styling
author: Guykerem
author_url: https://github.com/Guykerem/podium/tree/main/roles/creator/skills/base/caption-video
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Caption Video

Captions are not optional in 2026 — most social video is watched muted. This skill produces clean, styled, platform-appropriate captions.

## Purpose

- **Short-form**: word-by-word animated burn-in drives retention (Submagic-style)
- **Long-form**: soft SRT for accessibility + translation, optional burn-in for mobile
- **Multilingual**: one video, many SRTs (via translation of the base SRT)

The skill supports both "use the existing transcript" (fast) and "caption from scratch" (triggers `transcribe-media`).

## How It Works

1. **Acquire SRT**:
   - If `transcript.srt` exists, use it
   - Otherwise, call `transcribe-media` first
2. **Align captions to target** — For short-form (TikTok/Reels/Shorts), reshape SRT into one-word-at-a-time cues with animated highlighting. For long-form, keep multi-word lines.
3. **Choose styling preset** from `memory/creative-style/caption-presets.yaml` or defaults:
   ```yaml
   # default_short_form
   font: "Inter"
   weight: 900
   size_px: 64        # for 1080x1920 canvas
   color: "#FFFFFF"
   outline_color: "#000000"
   outline_width: 3
   highlight_color: "#FFD700"
   position: "center_upper_third"  # avoid IG/TT UI chrome at bottom
   max_words_per_line: 3
   ```
4. **Burn vs soft decision**:
   - Short-form → always burn-in
   - Long-form → soft SRT default; burn-in optional if platform is mobile-heavy
   - Translation layer → always soft SRT per language
5. **Burn with FFmpeg** (simple):
   ```bash
   ffmpeg -i in.mp4 -vf "subtitles=captions.srt:force_style='Fontname=Inter,Fontsize=24,PrimaryColour=&HFFFFFF&,OutlineColour=&H000000&,BorderStyle=3,Outline=3,Shadow=0,Alignment=8,MarginV=400'" \
     -c:a copy out.mp4
   ```
   Alignment: 1=BL, 2=BC, 3=BR, 5=TL, 6=TC, 7=TR, 8=above-bottom, 9=center. Colors `&HBBGGRR&`.
6. **For animated word-by-word** (Submagic style): generate an ASS subtitle file with per-word `\k` karaoke timing, OR use Remotion/FFmpeg with drawtext filter chains per word. Best quality: Remotion. Fastest: use a caption API (Submagic, Captions.ai, Zeemo).
7. **Soft-mux for long-form**:
   ```bash
   ffmpeg -i in.mp4 -i captions.srt -c copy -c:s mov_text \
     -metadata:s:s:0 language=eng out.mp4
   ```
8. **QA pass**:
   - Reading speed ≤ 180 WPM (flag if faster)
   - Cue duration ≥ 1s and ≤ 7s
   - No caption overlapping speaker's face or platform UI chrome
   - Text legible at target viewing size (test at 320x180 for thumbnails, phone scale for social)
9. **Emit**:
   ```
   captions/
     captions.srt              # canonical
     captions.vtt              # web
     captions.ass              # styled karaoke (if animated)
     captions.{en,es,fr}.srt   # translations if requested
     burned.mp4                # burned-in version (if generated)
   ```

## Platform style defaults

| Platform | Style | Position | Font size (1080x1920) | Burn? |
|---|---|---|---|---|
| TikTok | Word-by-word, highlight | Center | 64-72px bold | Burn |
| Reels | Word-by-word, highlight | Center upper-third | 60-68px bold | Burn |
| Shorts | Word-by-word, highlight | Center upper-third | 60-68px bold | Burn |
| LinkedIn native video | 2-3 words/line, simple white+outline | Lower-third | 48-56px medium | Burn |
| X video | 2-3 words/line, simple | Lower-third | 48-56px medium | Burn |
| YouTube Shorts | Same as Shorts | Center upper-third | 60-68px bold | Burn + soft SRT |
| YouTube long-form | Soft SRT, platform renders | N/A (soft) | N/A | Soft |
| Instagram feed video | Burn 2-3 words | Lower-third | 48-56px | Burn |

## Karaoke / word-highlight approach (ASS subtitle)

```
[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920

[V4+ Styles]
Style: Default,Inter,64,&H00FFFFFF,&H000000FF,&H00000000,&H00000000,1,0,0,0,100,100,0,0,1,3,0,5,80,80,400,1

[Events]
Dialogue: 0,0:00:00.00,0:00:00.30,Default,,0,0,0,,{\k30}Welcome
Dialogue: 0,0:00:00.30,0:00:00.60,Default,,0,0,0,,{\k30}to
Dialogue: 0,0:00:00.60,0:00:01.00,Default,,0,0,0,,{\k40}the
Dialogue: 0,0:00:01.00,0:00:01.60,Default,,0,0,0,,{\k60}show
```

For higher quality animated word-by-word, render via Remotion with word data from `transcript.json` — highlight color transitions between words. See `extensions/video/add-captions/SKILL.md` for the advanced version.

## Autonomy behavior

- **Level 1** — Generate SRT, render burned variant, present for approval before integrating into final video.
- **Level 2** — Auto-generate SRT + auto-burn using default preset; present burned result for one QA pass.
- **Level 3** — Auto-generate, auto-burn, auto-integrate. Creator reviews at final export.

## Integration

- Input: video + `transcript.srt` (or source to transcribe first)
- Composes **act** (FFmpeg burn) + **remember** (writes captions/)
- Downstream: `format-for-platform` (one caption set per platform variant), final export
- Upstream: `transcribe-media`, `segment-transcript` (for alignment to segments)

## Failure modes

- **Caption timing drift** — if subtitles lag speech by ≥ 0.3s, re-run transcription with word-level timestamps; drift usually means sentence-level SRT on fast speech
- **Burn over face** — adjust `MarginV` / position; keep faces clear
- **Unreadable contrast** — add black-box background (`BorderStyle=3,Outline=3`) or outline
- **Overflow lines** — max 2 lines; max 3 words per line for short-form animated captions
