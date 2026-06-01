---
name: caption-semantic-layer
title: /caption-semantic-layer
description: Two-tier caption architecture — key semantic captions (diegetic + branded) and subtitle fill with no-double enforcement.
author: prompted365
author_url: https://github.com/prompted365/context-grapple-gun/tree/main/cgg-runtime/skills/deprec_podcast_pipeline/caption-semantic-layer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# /caption-semantic-layer

You build the text layer of the edit. This is the most nuanced stage in the pipeline because text on video operates at two completely different levels simultaneously, and most content gets this wrong.

There are two layers. They serve different purposes, look different, and must never collide.

## Layer 1: Key Semantic Captions

These are the high-value text moments. They are not subtitles. They are *designed text events* that land with the weight of a visual composition choice.

### What qualifies as a key semantic

A key semantic is a word, phrase, or short sentence that functions as one of these:
- **Hook word/phrase**: The scroll-arrest moment in the opening seconds
- **Tension peak**: The moment stakes are highest — the word that crystallizes the tension
- **Resolution beat**: The payoff — the insight, punchline, or revelation
- **Loop anchor**: A phrase that appears at end and rhymes with the beginning
- **Quotable**: A standalone phrase the audience would screenshot and share

These are not the most *interesting* words. They are the most *load-bearing* ones. The test: if you removed this phrase, would the segment lose structural integrity?

### Styling: Over B-Roll (Diegetic)

When a key semantic appears during a b-roll slot, it is rendered as **diegetic text** — text that feels like it exists *inside the world of the image*, not on top of it.

What this means in practice:
- The text integrates with the scene's lighting, color, and depth
- It may appear as if printed on a surface, projected into space, or emerging from the environment
- It respects the scene's perspective and atmosphere
- The font, weight, and treatment match the emotional register of the visual
- It should feel *discovered*, not *placed*

The creative config's `caption_style.key_semantic.diegetic_treatment` field governs the specific approach. If the profile specifies "weathered analog" — the text looks like aged signage or faded print. If "luminous digital" — the text feels like projected light.

### Styling: Over Raw Footage (Branded)

When a key semantic appears over the speaker's footage (not b-roll), it is rendered as **differentiated branded text** — larger, kinetic typography that draws from the profile's aesthetic invariants.

- Position: from `caption_style.key_semantic.position`
- Font personality: from `caption_style.key_semantic.font_personality`
- Size behavior: from `caption_style.key_semantic.size_behavior` — how text scales with emphasis
- Animation: from `caption_style.key_semantic.animation` — how text enters and exits
- Color: from profile's `color_anchors`

These moments should feel *authored*. They are editorial emphasis, not transcription.

## Layer 2: Subtitle Fill

Full transcription subtitles that fill the timeline around the key semantics.

### Purpose
Accessibility and comprehension. Many viewers watch without audio (platform behavior data consistently shows 60-80% of Reels are viewed silently). Subtitles ensure the content is accessible.

### Styling
Intentionally subordinate to key semantics:
- Smaller text
- Simpler animation (fade or cut, not kinetic)
- Neutral position (bottom of frame, from `caption_style.subtitle.position`)
- Readable but not competing — the audience should barely notice them consciously
- Font personality from `caption_style.subtitle.font_personality`

### The No-Double Rule (Critical)

**If a phrase is rendered as a key semantic caption in a given time range, it does NOT appear as a subtitle in that same time range.**

This is enforced at the time range level, not the phrase level. The logic:
1. Map every key semantic to its display time range (start → end, including any animation time)
2. For each subtitle segment, check if its text overlaps with any active key semantic's time range
3. If overlap exists: suppress the overlapping words from the subtitle. The subtitle may show surrounding words but the key semantic phrase is removed.
4. If suppression would leave a subtitle segment empty or incoherent: drop that subtitle segment entirely for that time range.

The key semantic layer always takes precedence. Doubling reads as a mistake — as if the system doesn't know it already said that.

## Input

You receive:
- The EDL (cut structure with b-roll slots)
- The scored segment (with identified hook, tension, resolution, loop moments)
- The full profile + active creative (caption styling configs)
- The transcript text for the selected segment
- (Optional) Overshoot adjudication verdict — if a `draft_review` pass was run, it includes a `caption_sync` field (`good | minor_issues | major_issues`) and may flag specific timing problems

**Input contract**: Captions render AFTER b-roll assembly (Phase 5e). Your input video is the b-roll-assembled clip, not the raw base track. This means morph overlays are already baked in — your captions go on top of the final visual. The word-level verified transcript (Phase 1c) provides caption timing against the original audio spine, which is unchanged through assembly.

**Timestamp Drift Warning**: Subtitle timestamps derive from the transcript. If auto-transcribed, they may be 3-5s off from actual audio. The caption layer must consume the verified transcript (post-Phase 1c), not the raw transcript. If verification has not run, flag this in the `collision_audit` output as a `timestamp_drift_warning` field.

## Process

### Step 1: Key Semantic Identification
Read through the segment text and identify every key semantic candidate. For each:
- What type is it? (hook / tension_peak / resolution / loop_anchor / quotable)
- Where does it fall in the EDL timeline? (over b-roll or over raw footage?)
- What styling treatment applies? (diegetic or branded)

### Step 2: Key Semantic Design
For each selected key semantic:
- Write the exact text that appears (may be shortened from the full phrase)
- Specify the styling approach based on context (b-roll diegetic or raw branded)
- Specify timing: when it appears, how long it holds, when it exits
- Specify animation behavior per the creative config
- Note the emotional intention — what this text does to the viewer at this moment

### Step 3: Subtitle Generation
For the full segment:
- Generate word-accurate subtitles (2-3 words per subtitle group, timed to speech rhythm)
- Apply the no-double rule against the key semantic time ranges
- Flag any suppressed segments
- Verify subtitle legibility doesn't compete with key semantics at any point in the timeline

### Step 4: Collision Audit
Walk through the full timeline and verify:
- No moment has key semantic + subtitle showing simultaneously for the same words
- No moment has overlapping key semantics
- Text placement doesn't collide with b-roll focal points (check against b-roll composition notes)
- Overall text density is appropriate (not too much text on screen at any moment)
- **Morph zone clearance**: No key semantic animation (kinetic entrance/exit, scale change, position shift) may fire during an active morph transition window. Check the EDL's b-roll slots for `continuity_type: "morphing"` — during those timestamp ranges, the visual is mid-transformation between real footage and abstract energy (or vice versa). Caption animation during a morph creates visual chaos — two things moving independently in the same frame. Static captions (already on screen, not animating) may persist through morph zones. New caption entrances, kinetic text, and diegetic treatments must wait until the morph completes. Subtitle fill (small, static, bottom-positioned) is exempt from this rule — it's designed to be invisible.

To enforce: for each key semantic, check whether its `timestamp_start` through `timestamp_end` (including animation_in and animation_out durations) overlaps with any morph b-roll slot's reel window. If overlap: either shift the key semantic to land just before or just after the morph, or convert it to a static hold (no animation) for the duration of the overlap.

### Step 5: Overshoot Caption Sync Reconciliation (conditional)

If an Overshoot adjudication verdict is available with `caption_sync` data:
- **good**: No action needed — confirms the caption layer timing is sound
- **minor_issues**: Review the adjudicator's specific timing flags. Common causes: subtitle group boundaries misaligned with speech rhythm, key semantic animation overlapping with transition cuts. Adjust timing windows for flagged segments.
- **major_issues**: The caption layer likely needs structural rework. Check for: (1) key semantics placed at wrong emotional beats (the adjudicator sees the assembled video, not just the transcript), (2) subtitle groups too large causing delayed appearance, (3) caption animation timing conflicting with b-roll morph transitions. Reconcile against the adjudicator's `revision_notes` if present.

Record the reconciliation result in the output's `collision_audit` — add a `caption_sync_reconciled` field indicating whether adjudication data was consumed and what changed.

## Output Schema

```json
{
  "caption_layer_version": "1.0.0",
  "profile_id": "string",
  "creative_id": "string",
  
  "key_semantics": [
    {
      "id": "ks_1",
      "type": "hook | tension_peak | resolution | loop_anchor | quotable",
      "text": "string — exact text displayed",
      "source_text": "string — full phrase from transcript (may be longer than display text)",
      "timestamp_start": "string",
      "timestamp_end": "string",
      "duration_seconds": "float",
      "context": "broll | raw_footage",
      "styling": {
        "treatment": "diegetic | branded",
        "position": "string",
        "animation_in": "string",
        "animation_out": "string",
        "size": "string",
        "color_note": "string",
        "diegetic_description": "string — if diegetic, how text integrates with scene (null if branded)"
      },
      "emotional_intention": "string — what this text does to the viewer at this moment",
      "edl_beat": "int — which beat in the EDL this aligns with"
    }
  ],
  
  "subtitles": [
    {
      "id": "sub_1",
      "text": "string — 2-3 words",
      "timestamp_start": "string",
      "timestamp_end": "string",
      "suppressed": false,
      "suppressed_by": "null or key_semantic id that caused suppression"
    }
  ],
  
  "collision_audit": {
    "status": "clean | flagged",
    "flags": [
      {
        "timestamp": "string",
        "issue": "string — what collision was detected",
        "resolution": "string — how it was resolved"
      }
    ],
    "morph_zone_clearance": [
      {
        "slot": "int — b-roll slot number",
        "morph_window": "string — e.g. '16.8-20.5s'",
        "captions_in_window": ["string — caption IDs active during this window"],
        "conflicts": ["string — caption IDs with animation overlap"],
        "resolution": "string — shifted / converted to static hold / exempt (subtitle fill)"
      }
    ],
    "text_density_assessment": "string — overall assessment of text load"
  },
  
  "editorial_notes": "string — any notable decisions about what was or wasn't selected as key semantic"
}
```

## Taste Standard

The key semantic layer is where the pipeline's editorial voice is most visible to the audience. The words you choose to elevate — and the words you don't — define how the show *feels* when consumed in shortform.

Select too many key semantics: the piece feels desperate, over-emphasized, like it's trying too hard.
Select too few: the piece feels like a subtitle reel with no editorial point of view.

The sweet spot for a 60-second piece is typically 3-5 key semantics. One hook, one tension peak, one resolution, plus 1-2 quotables or loop anchors if they exist. Quality over quantity.

## Assembly Model Assumption

Captions are timed against the audio spine, which must remain untouched during assembly. If b-roll is assembled as overlay-at-timestamp (correct), caption timing holds. If assembled as insert-between-segments (incorrect), cumulative sync drift will invalidate all caption timestamps after the first insertion point.

The caption layer assumes overlay-at-timestamp assembly. If the pipeline's assembly model changes, the caption timing model must be re-validated.
