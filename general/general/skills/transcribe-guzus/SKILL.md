---
name: transcribe-guzus
title: Input handling
description: Transcribe and summarize video or audio content. Use when the user shares a video URL (X/Twitter, direct mp4/webm link), asks to 'transcribe this', 'summarize this video', 'what does this video say', or provides a tweet URL containing a video.
author: guzus
author_url: https://github.com/guzus/birdy/tree/main/.claude/skills/transcribe
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

Transcribe video/audio content and produce a structured summary.

## Input handling

1. Determine the video source from the user's input:
   - **X/Twitter URL**: Extract the tweet ID, run `go run . read <id> --json` from the birdy repo root to get the `media[].videoUrl`. If multiple video qualities exist, prefer the highest resolution.
   - **Direct video/audio URL**: Use as-is.
   - **Local file path**: Use as-is, skip download.

2. If the source is an X/Twitter URL and `go run .` fails (not in birdy repo), fall back to `birdy read <id> --json` or `bird read <id> --json`.

## Download

3. Create a temp working directory: `mkdir -p /tmp/transcribe-work`.
4. Download the video: `curl -L -o /tmp/transcribe-work/video.mp4 "<url>"`.
5. If the file is already audio-only (mp3/wav/m4a), skip the extraction step.

## Extract audio

6. Extract audio with ffmpeg:
   ```
   ffmpeg -y -i /tmp/transcribe-work/video.mp4 -vn -acodec pcm_s16le -ar 16000 -ac 1 /tmp/transcribe-work/audio.wav
   ```
7. Delete the video file to save disk space: `rm /tmp/transcribe-work/video.mp4`.

## Transcribe

8. Check if `mlx_whisper` is importable in Python 3. If not, install it: `pip3 install mlx-whisper`.
9. Run transcription with the following Python script:
   ```python
   import mlx_whisper
   result = mlx_whisper.transcribe(
       '/tmp/transcribe-work/audio.wav',
       path_or_hf_repo='mlx-community/whisper-small-mlx',
       language='en'
   )
   with open('/tmp/transcribe-work/transcript.txt', 'w') as f:
       for seg in result['segments']:
           start = int(seg['start'])
           m, s = divmod(start, 60)
           f.write(f'[{m:02d}:{s:02d}] {seg["text"].strip()}\n')
   ```
   - If disk space is tight (the large model fails), fall back to `mlx-community/whisper-small-mlx`.
   - For non-English content, omit the `language` parameter or set it appropriately.

## Summarize

10. Read the full transcript from `/tmp/transcribe-work/transcript.txt`.
11. Produce a structured summary with:
    - **Title and metadata** (speakers, host, source)
    - **Key takeaways** — the 4-6 most important points, each with a bold heading and 2-3 sentence explanation
    - **Notable quotes or claims** if any stand out
    - Keep the summary concise but substantive. Match the depth to the content length (short video = brief summary, long podcast = detailed breakdown).
12. Present the summary to the user. Mention that the full timestamped transcript is at `/tmp/transcribe-work/transcript.txt`.

## Cleanup

13. Delete `/tmp/transcribe-work/audio.wav` after transcription to free space. Keep `transcript.txt`.
