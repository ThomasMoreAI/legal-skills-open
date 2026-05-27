---
name: hearing-prep
title: Hearing Preparation Summary
description: Generates structured hearing preparation briefings from case documents, evidence, authorities, and procedural details. Use when preparing for court hearings, administrative hearings, arbitrations, trials, motion hearings, evidentiary hearings, or status conferences.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/hearing-prep
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Hearing Preparation Summary

Synthesizes case materials into a structured briefing document for advance preparation and quick reference during proceedings.

## Prerequisites

- **Case documents** — pleadings, discovery, correspondence, exhibits
- **Hearing details** — date, time, location, presiding judge/officer, proceeding type
- **Witness information** — expected witnesses, depositions, declarations
- **Legal authority** — controlling statutes, rules, case law

## Output Structure

### 1. Procedural Header

Table with: hearing date/time, location/courtroom, presiding judge/officer, proceeding type (motion hearing / evidentiary / status conference / trial / other), matters to be addressed, filing deadlines.

### 2. Case Background

- Parties and relationship
- Genesis of dispute
- Chronological procedural history through current posture
- Prior rulings or orders affecting this hearing
- Cite source documents for every factual assertion

### 3. Issue Analysis

For each discrete issue the court will consider:

- **Issue statement** — one-sentence framing
- **Factual background** — key facts with document citations
- **Legal standard** — controlling statute/rule/case law; mark uncertain citations `[VERIFY]`
- **Our position** — arguments and supporting evidence
- **Opposing position** — anticipated arguments and their evidence
- **Evidentiary considerations** — anticipated objections, authentication requirements, motions in limine

### 4. Witness Summary

For each anticipated witness:

- **Name / role** — relationship to case
- **Expected testimony** — key points
- **Prior statements** — deposition/declaration cites with page references
- **Credibility issues** — inconsistencies, impeachment material
- **Direct questions** — organized by topic, tied to legal theories
- **Cross-examination points** — for opposing witnesses

For expert witnesses, add: qualifications summary, opinions, methodology basis, Daubert/Frye vulnerability assessment.

### 5. Exhibit Inventory

Table with columns: exhibit #, description, relevance (issue/witness), pre-marked status, authentication status, stipulation status.

- Flag authenticity disputes
- Cross-reference each exhibit to its supporting issue and/or witness

### 6. Strategic Assessment

- **Strengths** — strongest facts, favorable authority, equitable factors
- **Vulnerabilities** — weaknesses with suggested responses
- **Opposing counsel's likely approach** — anticipated arguments and tactics
- **Decision-maker considerations** — known ruling patterns, equitable factors beyond legal merits
- **Recommended presentation strategy** — order of proof, thematic framing

### 7. Procedural Checklist

- [ ] Trial brief / proposed findings filed by deadline
- [ ] Exhibit list exchanged
- [ ] Witness list exchanged
- [ ] Exhibits pre-marked and organized
- [ ] Technology tested for evidence presentation
- [ ] Local rules and standing orders reviewed
- [ ] Copies prepared for court and opposing counsel

## Pitfalls

- **Uncited facts** — every factual assertion must cite its source document so counsel can locate materials instantly
- **Unverified citations** — format legal citations properly; mark uncertain ones `[VERIFY]`
- **Minimizing weaknesses** — maintain objectivity; present honest assessment of both sides
- **Missing gaps** — explicitly flag missing documents, unresolved discovery, or unavailable witnesses
- **Poor organization** — group all analysis, evidence, and authority by the discrete issue it addresses
