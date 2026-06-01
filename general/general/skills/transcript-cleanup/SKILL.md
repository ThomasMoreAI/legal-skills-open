---
name: transcript-cleanup
title: Transcript cleanup
description: This skill should be used when the user asks to "clean up a transcript", "fix speech artifacts", "edit interview quotes", "polish transcription", "clean up quotes from a recording", or when working with speech-to-text output that needs light editing while preserving the speaker's voice.
author: birdseyeglobal
author_url: https://github.com/birdseyeglobal/portage/tree/main/plugins/prose/skills/transcript-cleanup
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Transcript cleanup

Clean speech-to-text artifacts from transcripts and direct quotes without editorializing. The goal is readability, not rewording. Preserve the speaker's vocabulary, sentence structure, and personality. Fix only what a competent transcriptionist would fix.

## The rule

If you cannot point to a specific speech artifact or transcription error, do not change the sentence. "Sounds better" is not a reason to edit. Every edit must fall into one of the pattern categories below.

## Pattern categories

### 1. Filler "like"

Spoken English uses "like" as a verbal pause. Remove it when it serves no grammatical function. Keep it when it means "such as" or "similar to."

| Before                                              | After                                               | Why                       |
| --------------------------------------------------- | --------------------------------------------------- | ------------------------- |
| has like a road map                                 | has a road map                                      | filler before article     |
| is like no more than three digits                   | is no more than three digits                        | filler before adverb      |
| was like AI is important                            | where the message was AI is important               | filler replacing a clause |
| a mega corp like Apple                              | a mega corp like Apple                              | means "such as" -- keep   |
| a generic topic like generative engine optimization | a generic topic like generative engine optimization | means "such as" -- keep   |

**Test:** Remove "like" and read the sentence. If it still makes grammatical sense and the meaning is unchanged, the "like" was filler.

### 2. Spoken grammar

Speakers routinely break grammar rules that readers notice on the page. Fix subject-verb agreement and comparison constructions.

| Before                      | After                     | Rule                                         |
| --------------------------- | ------------------------- | -------------------------------------------- |
| there's so many signals     | there are so many signals | subject-verb agreement ("signals" is plural) |
| as powerful than if we had  | as powerful as if we had  | "as...as" comparison, not "as...than"        |
| as much of a signal than if | as much of a signal as if | same pattern                                 |

**Test:** Read the sentence aloud slowly. If the grammar error is obvious when spoken deliberately rather than quickly, fix it.

### 3. Word order from natural speech

Speakers front-load or rearrange words in ways that read awkwardly on paper. Restore standard English word order.

| Before                                 | After                             |
| -------------------------------------- | --------------------------------- |
| put in specifically keywords           | specifically put in keywords      |
| that's like deep on a bottom of funnel | that's deep on a bottom-of-funnel |

### 4. Orphan words

Mid-sentence restructuring during speech leaves behind words that no longer connect to anything. Remove them.

| Before                          | After                     | Orphan                                     |
| ------------------------------- | ------------------------- | ------------------------------------------ |
| things that while seem exciting | things that seem exciting | "while" left over from an abandoned clause |

### 5. Transcription artifacts

Speech-to-text engines sometimes drop words, merge sentences, or mishear connectives. Restore the minimal missing words needed for the sentence to parse.

| Before                                                                    | After                                                                      | Fix                                               |
| ------------------------------------------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------- |
| was like AI is important                                                  | where the message was AI is important                                      | restored dropped clause                           |
| who is higher up in the organization chart like a chief marketing officer | who is higher up in the organization chart, like a chief marketing officer | added comma before "like" (parenthetical example) |

Only add words when the sentence is genuinely unparseable without them. If the meaning is clear despite missing words, leave it alone.

## Process

1. Read the full transcript or quote set before editing anything.
2. Identify each artifact by pattern category (1-5 above).
3. Make the smallest edit that fixes the artifact.
4. Re-read the edited version aloud. If the speaker's voice is gone, revert.
5. When in doubt, leave it. A slightly rough quote is better than a polished one that no longer sounds like the person who said it.

## What not to touch

- Informal vocabulary ("gonna", "kind of", "a lot") -- these are voice, not errors
- Sentence fragments that work as emphasis -- speakers use these deliberately
- Repeated words used for emphasis ("it's really, really important")
- Regional or personal speech patterns -- do not normalize dialect
- Content or meaning -- never change what the speaker said, only how clearly the transcription conveys it
- Sentences that are merely inelegant -- ugly-but-clear is fine

## Working with direct quotes

When cleaning quotes embedded in documents (blockquotes, inline quotes), apply extra caution. The reader knows this is a quote from a real person. Overcleaning makes quoted speech sound ghostwritten.

For attributed quotes (with a speaker name), preserve more roughness. The attribution signals "this is how they actually talk." For unattributed quotes used as pull-quotes or callouts, slightly more cleanup is acceptable since the reader expects polished text.

## Batch editing workflow

When cleaning an entire transcript or document with many quotes:

1. Grep for all direct quotes across the file set.
2. Categorize each fix by pattern (1-5) before editing.
3. Apply fixes file by file, not pattern by pattern, to maintain reading context.
4. Flag any borderline cases for human review rather than guessing.
