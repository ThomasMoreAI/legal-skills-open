---
name: pa-workflow-litigation-transcript-search-q-and-a-indexing
title: Litigation — Transcript Search and Q&A Indexing
description: Use when a litigation team needs to index and search deposition transcripts, trial hearing transcripts, or arbitration session transcripts for witness preparation, cross-examination planning, or factual reconstruction. Builds a Q&A-indexed, topic-clustered, searchable corpus from raw transcripts; detects intra-witness and inter-witness contradictions; and powers the real-time trial assist and deposition binder workflows.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/pa-workflow/pa-workflow-litigation-transcript-search-q-and-a-indexing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Litigation — Transcript Search and Q&A Indexing

## Purpose

Raw deposition and hearing transcripts are unwieldy: a complex commercial arbitration can generate thousands of pages across dozens of witnesses. This workflow transforms raw transcript text into a structured, searchable Q&A index — enabling counsel to find every statement a witness made on a given topic in seconds, cluster testimony by subject matter, and immediately surface potential contradictions across witnesses or between sessions.

## Inputs

| Input | Required | Notes |
|---|---|---|
| Transcript files | Yes | PDF, plain text, Word — single or batch |
| Transcript type | Yes | Deposition / trial hearing / arbitration session / regulatory investigation |
| Witness name(s) | Yes | For attribution and per-witness indexing |
| Dates of transcript(s) | Yes | Critical for contradiction timeline analysis |
| Matter summary | Recommended | Drives topic clustering |
| Prior-session transcripts (same witness) | Optional | Enables intra-witness contradiction detection |
| Opposing witness transcripts | Optional | Enables inter-witness contradiction detection |

## Processing Pipeline

### Step 1 — Ingestion and parsing

- Accept transcript in any standard format
- Identify and tag: question-asker (examining counsel, opposing counsel, arbitrator/judge), witness, objections, non-answer responses ("I don't recall," "I'm not sure," "that's not accurate")
- Assign a sequential Q&A number to every question-answer pair
- Flag: interrupted answers, objections sustained / overruled, documents shown to witness during examination

### Step 2 — Q&A indexing

For each Q&A pair, produce:

```json
{
  "qa_id": "DEP-AhmedAlSayed-2023-03-14-Q247",
  "witness": "Ahmed Al-Sayed",
  "date": "2023-03-14",
  "transcript_type": "Deposition",
  "page": 47,
  "line": 12,
  "examiner": "Plaintiff's counsel",
  "question": "Did you review vendor contracts over $50,000 before they were signed?",
  "answer": "Yes, I personally reviewed and approved every vendor contract over $50,000.",
  "topics": ["contract_approval", "authorization", "vendor_management"],
  "exhibit_shown": null,
  "non_answer": false,
  "flag": null
}
```

### Step 3 — Topic clustering

Automatically group Q&A pairs into topic clusters using the matter summary as a guide:
- Contract formation / approval
- Payments and financial transactions
- Corporate authority and authorization
- Communications with specific parties
- Knowledge of specific events
- Timeline of events

Output: per-topic index with all relevant Q&A pairs from all transcripts, sorted chronologically.

### Step 4 — Contradiction detection

**Intra-witness (same witness, multiple transcripts/sessions):**
- Compare statements on the same factual proposition across deposition session 1, session 2, and hearing
- Flag: direct factual contradiction (same question, different answer), timeline inconsistency (date stated differently), denial of knowledge when prior session indicates knowledge

**Inter-witness (across witnesses, same matter):**
- Compare statements on the same factual proposition across different witnesses
- Flag: conflicting accounts of the same event; different characterizations of the same document; contradictory claims about who attended a meeting or made a decision

**Contradiction severity:**

| Level | Definition |
|---|---|
| HIGH | Direct factual contradiction on a material issue — usable for impeachment |
| MEDIUM | Inconsistency that requires explanation — may be innocent (faulty memory, different vantage point) |
| LOW | Tone or characterization difference — unlikely to be significant |

### Step 5 — Search interface

The indexed corpus supports:
- Full-text keyword search ("wire transfer," "approval," "contract No. 4")
- Per-witness search (all Q&As by Ahmed Al-Sayed on topic X)
- Date-range search (all testimony from after September 2022)
- Topic search (all Q&As on "authorization" across all witnesses)
- Contradiction search (all HIGH-level contradictions for witness X)

## Output

### Per-witness testimony profile

```markdown
## Testimony Profile — Ahmed Al-Sayed
**Sessions indexed**: Deposition 2023-03-14 (87 pages), Deposition 2023-05-22 (53 pages)
**Total Q&A pairs**: 641

### Key Admissions
- Q247 (3/14/23): Confirmed personal approval of all vendor contracts over $50K
- Q312 (3/14/23): Confirmed he signed Exhibit 22 (contract approval form)
- Q089 (5/22/23): Confirmed receipt of the memo dated 2022-09-01

### Contradictions Found
| ID | Topic | Prior statement | Later statement | Severity |
|---|---|---|---|---|
| C-001 | Contract review | "I reviewed all contracts" (Dep 1, Q247) | "I never reviewed that document" (Dep 2, Q156) | HIGH |

### Non-Answer Instances (41 total)
Topics where witness claimed lack of recall: [list]
```

### Matter-wide topic index

For each topic cluster: a consolidated table of all Q&As from all witnesses, enabling counsel to compare accounts side by side.

### Contradiction master log

All contradictions across all witnesses, ranked by severity, with transcript references.

## Integration with Other Workflows

This workflow's output feeds directly into:
- [[pa-workflow-litigation-deposition-binder-builder]] — per-witness document packages
- [[pa-workflow-litigation-witness-contradiction-finder]] — full contradiction analysis
- [[pa-workflow-litigation-real-time-trial-assist-api]] — the indexed corpus is the trial database

## Jurisdictional Notes

- **US**: Court reporters produce verbatim transcripts. Errata sheets (changes by witness post-deposition) must be captured and noted — changed answers are themselves impeachable.
- **UK / DIFC / ADGM**: Written witness statements serve as direct examination; oral examination is cross-examination and re-examination. Index witness statements as "transcripts" and cross-examination as separate sessions.
- **International Arbitration**: Procedural orders may limit transcript availability to approved parties. Ensure proper handling of confidential arbitration transcripts.
- **UAE onshore / KSA**: Court sessions are not typically transcribed verbatim by a court reporter. Session minutes (da'wa records) are prepared by the court clerk. These are the transcript equivalent for indexing purposes and are in Arabic. Ensure Arabic-language parsing is enabled for MENA court session notes.
- **Lebanon / Egypt**: Similar to UAE — court session records (procès-verbaux) are the indexable source. Bilingual (Arabic/French for Lebanon) processing may be required.

## Related Skills

- [[pa-workflow-litigation-witness-contradiction-finder]]
- [[pa-workflow-litigation-deposition-binder-builder]]
- [[pa-workflow-litigation-real-time-trial-assist-api]]
- [[pa-workflow-litigation-expert-witness-prep-memo]]
- [[pa-workflow-litigation-discovery-first-pass-tagging]]
