---
name: litigation-case-strategy
title: Litigation Case Strategy
description: 'Develops comprehensive litigation strategy across the full case lifecycle, from initial assessment through discovery, motion practice, trial preparation, and appeal. Produces case theory analysis, chronologies from document sets, discovery plans, deposition outlines, brief drafts, cross-examination questions, and appellate record summaries. Use when evaluating a new litigation matter, preparing case strategy memos, building case chronologies from emails or documents, preparing for depositions, drafting motions or briefs, developing trial strategy, or preparing appellate filings. Trigger keywords: litigation strategy, case assessment, case theory, case chronology, discovery plan, deposition prep, motion to dismiss, summary judgment, trial preparation, cross-examination, appellate brief, argument evaluation, case timeline.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/litigation-case-strategy
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [memo, brief, summary, analysis, drafting, research]
---

# Litigation Case Strategy

Develops and pressure-tests litigation strategy across the full case lifecycle. Takes case documents as input and produces structured work product — from initial case assessment through appellate practice.

## Prerequisites

1. **Case documents** — complaints, answers, key correspondence, contracts at issue, prior court orders, relevant statutes
2. **Procedural posture** — current stage (pre-filing, pleading, discovery, pre-trial, trial, post-trial, appeal)
3. **Client role** — plaintiff or defendant; first-party or third-party
4. **Jurisdiction** — court, applicable law, any special procedural rules
5. **Case objectives** — desired outcome, settlement authority if any, budget constraints
6. **Known facts** — key facts favorable and unfavorable; witness list if available

Specify which stage(s) to focus on, or request a full lifecycle assessment.

## Stage 1: Initial Case Assessment

### Case Theory Development

From the originating documents, develop:

1. **Factual narrative** — chronological summary of events giving rise to the dispute
2. **Legal theories** — each viable claim or defense with:
   - Elements required
   - Facts supporting each element (cite to specific documents)
   - Facts undermining each element (adverse facts)
   - Strength assessment (Strong / Moderate / Weak) with reasoning
3. **Opposing theories** — anticipate the other side's best arguments
4. **Leverage analysis** — settlement value drivers, litigation cost exposure, publicity risk, business relationship impact
5. **Early case budget** — estimated phases and resource requirements

### Document-Based Chronology

When provided with a set of documents (emails, contracts, letters, filings):

1. Extract key events with:
   - Date and time (where available)
   - Participants (sender/recipient for correspondence)
   - Event description (one sentence)
   - Source document reference
   - Significance to case theory
2. Sort chronologically
3. Flag gaps — periods with no documentation that may require follow-up
4. Identify pivotal events — turning points that strengthen or weaken the case
5. Note privilege concerns — flag potentially privileged communications

Output as a structured chronology table:

| Date | Event | Participants | Source | Significance | Notes |
|---|---|---|---|---|---|

## Stage 2: Discovery Planning

### Discovery Strategy

1. **Information needs** — what facts must be established, from which sources
2. **Document requests** — targeted RFPs tied to case theories, with specific document categories and date ranges
3. **Interrogatories** — contention interrogatories and fact interrogatories tied to elements
4. **Deposition targets** — priority witnesses with justification and sequencing rationale
5. **Third-party discovery** — subpoenas needed, custodians, potential objections
6. **Preservation obligations** — litigation hold scope, key custodians, ESI sources
7. **Proportionality analysis** — scope justified relative to amount in controversy

### Discovery Response Review

When reviewing received discovery:
- Evaluate sufficiency of responses against the requests
- Identify evasive, incomplete, or boilerplate objections
- Flag documents that support or undermine case theories
- Generate follow-up requests or meet-and-confer points
- Note any privilege log issues

## Stage 3: Deposition Practice

### Deposition Preparation

For each deponent, produce:

1. **Witness profile** — role, relationship to events, likely knowledge areas, credibility factors
2. **Key topics** — organized by case theory, not chronologically
3. **Question outlines** — structured by topic with:
   - Foundation questions (establish knowledge base)
   - Substantive questions (elicit key admissions)
   - Impeachment questions (prior inconsistent statements, documents)
   - Pin-down questions (foreclose escape routes)
4. **Exhibit list** — documents to use, sequence, and purpose for each
5. **Risks** — what the deponent might volunteer that hurts the case; how to handle

### Deposition Summary

From a transcript, extract:
- Key admissions (with page:line citations)
- Inconsistencies with other testimony or documents
- Topics where witness was evasive or non-responsive
- New facts or leads revealed
- Impeachment material for trial
- Areas requiring follow-up discovery

## Stage 4: Motion Practice

### Brief and Motion Drafting

For any motion type (dismiss, summary judgment, in limine, compel, sanctions):

1. **Legal standard** — applicable standard of review with controlling authority
2. **Argument structure** — organize by strongest argument first; each argument includes:
   - Legal rule with citation
   - Application to case facts (cite record)
   - Anticipate and address counterarguments
   - Conclusion on this point
3. **Statement of facts** — persuasive but accurate; cite record throughout
4. **Procedural requirements** — page limits, local rules, certificate of conference if required

### Argument Evaluation

When provided with a draft brief or complaint:

1. **Strength assessment** — grade each argument (Strong / Moderate / Weak)
2. **Vulnerability analysis** — identify what opposing counsel will attack:
   - Factual gaps or unsupported assertions
   - Legal authority that cuts the other way
   - Logical weaknesses in the argument chain
   - Procedural deficiencies
3. **Improvement suggestions** — for each vulnerability:
   - Additional authority to cite
   - Factual support to add
   - Alternative framing
   - Language tightening
4. **Missing arguments** — theories or authorities not raised that should be considered
5. **Opposing brief preview** — draft the strongest response the other side could file

## Stage 5: Trial Preparation

### Cross-Examination Development

For each opposing witness:

1. **Objectives** — what admissions or impeachment points to achieve
2. **Question sequences** — leading questions organized by topic:
   - Establish the undisputed fact
   - Box in the witness with prior statements
   - Confront with contradicting document or testimony
   - Secure the admission or demonstrate the inconsistency
3. **Exhibit choreography** — when to introduce each document, foundation requirements
4. **Contingency plans** — if witness denies expected answer, alternative paths
5. **Red lines** — questions to avoid (opens door to harmful testimony)

### Trial Document Organization

From the case record, identify and organize:
- Exhibits by witness and topic
- Demonstratives needed
- Stipulations to propose
- Motions in limine (offensive and defensive)
- Jury instructions / proposed findings of fact

## Stage 6: Post-Trial and Appeals

### Appellate Analysis

1. **Preserved issues** — identify which trial objections and motions preserved error
2. **Standards of review** — for each potential issue (de novo, abuse of discretion, clear error, plain error)
3. **Issue prioritization** — rank appellate issues by:
   - Likelihood of reversal
   - Standard of review favorability
   - Strength of record support
   - Impact if won (remand vs. reversal with direction)
4. **Record compilation** — identify key transcript excerpts, exhibits, and orders for the appendix
5. **Argument outline** — for each issue: error, prejudice, relief sought

## Guidelines

- Every factual assertion must cite a specific source document, exhibit, or transcript reference
- Present both favorable and unfavorable facts — do not omit adverse information
- Grade arguments honestly — a "Weak" rating with explanation is more useful than false confidence
- Tailor all work product to the specific jurisdiction's rules and standards
- Mark [VERIFY] on any case citation, statutory reference, or local rule not confirmed against current authority
- Distinguish between facts in the record and inferences drawn from those facts
- When building chronologies, include only events supported by documents — do not interpolate
- For deposition outlines, use leading questions only (cross-examination style) — never open-ended
- Maintain attorney-client privilege awareness — flag communications that may be privileged before including in work product
- Separate strategic recommendations from factual analysis
