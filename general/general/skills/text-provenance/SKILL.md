---
name: text-provenance
title: text-provenance
description: Use when you need to identify the likely source of a text passage, attribute text to documents in a RAG system, detect plagiarism, or match contract clauses to their origin.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/text-provenance
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [text-analysis, rag, citation, provenance, similarity, attribution]
---

# text-provenance

## When to Use

- RAG citation highlighting — show which source document a generated text came from
- Contract playbook matching — find which standard clause a contract clause derives from
- Plagiarism detection
- Source attribution for AI-generated legal text
- Any text provenance task where you need to trace text back to its origin

## How It Works

### Core Approach

Lightweight text similarity metrics — no embeddings or API calls at runtime. Fast, deterministic string matching that works in-browser or server-side.

### Comparison Methods

- **Surface similarity** — character-level comparison
- **N-gram overlap** — phrase-level matching
- **Fingerprint matching** — exact phrase detection

### Usage

```javascript
import { findProvenance } from 'text-provenance';

const sources = await findProvenance(
  "the quick brown fox jumps over the lazy dog",
  corpusDocuments
);
// Returns ranked list of potential sources with confidence scores
```

### Edge Cases

Works where embeddings fail:
- Short text snippets
- Exact phrase matching
- High-precision attribution tasks
- Privacy-sensitive contexts (no data leaves the machine)

## Audience and Work Shape

Audience: developers and lawyers building RAG-citation, contract-derivation, or plagiarism-detection workflows. The output is a *candidate ranking*, not a finding.

Work shape: Pattern-Matched Review. Lexical similarity is the matching function; the user decides what counts as a match.

## Scope and Legal Use

This skill provides legal *support*, not legal advice. The output is a ranked list of candidate sources with similarity scores — never an attribution conclusion, never a plagiarism finding, never a contract-derivation determination of legal effect.

**Privilege and confidentiality.** Runs client-side with no network calls. No text leaves the user's machine unless the calling application chooses to transmit it. Skill itself does not create new privilege exposure.

**Accountability.** A qualified lawyer must review and accept any output before relying on it for an attribution, plagiarism, or contract-derivation decision. The similarity score is a signal, not a verdict.

## Confidence Bands

Map the raw similarity score to action bands:

- **High (≥ 0.85)** — strong lexical match; lawyer can rely on this as a likely source but must still verify the underlying passage.
- **Medium (0.55 – 0.85)** — possible match; route to human comparison before relying.
- **Low (< 0.55)** — weak signal; do not treat as a source attribution. Show alongside other candidates but do not single out.

## Out of Scope

- Not a plagiarism adjudication or finding of academic/professional misconduct.
- Not legal advice on copyright, IP, or contract-derivation claims.
- Not evidentiary; results are not formatted for proceedings.
- Not a semantic search — lexically different paraphrases will be missed.
- Not a substitute for embedding-based retrieval where semantic match is required.

## Escalation

Stop and route to the responsible lawyer when:
- the top result is in the Low band but the calling workflow expects a definitive source;
- the use case is disciplinary, evidentiary, or potentially defamatory (e.g., flagging a lawyer or student for plagiarism);
- two or more candidates score within 0.05 of each other and the workflow requires a single source attribution.

## Limitations

- Cannot handle semantically similar but lexically different text
- Works best with longer source documents
- Not a substitute for embedding-based retrieval in all contexts
