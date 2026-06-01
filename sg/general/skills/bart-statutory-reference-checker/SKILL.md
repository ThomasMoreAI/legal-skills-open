---
name: bart-statutory-reference-checker
title: 'BART: Statutory Reference Checker'
description: Use when checking statutory citations in Singapore legal documents, verifying references against Singapore statutes, or auditing Word documents for citation accuracy.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/bart-statutory-reference-checker
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: sg
practice: general
language: en
tags: [singapore, statutory-citation, legal-research, word-addin, compliance]
---

# BART: Statutory Reference Checker

## When to Use

- Auditing Singapore legal documents for statutory citation accuracy
- Verifying that cited Singapore statutes exist and are properly referenced
- Checking if statutory references have been amended or repealed
- Academic work on Singapore legislation
- Pre-filing review of submissions

## How It Works

### Backend (Python + Next.js frontend)

1. **Semantic search** over Singapore statute text using Legal-BERT/GEMMA
2. **BM25 + reranker** for precise citation matching
3. **ChromaDB** vector store for fast retrieval
4. **Word Add-in** integration for in-document checking

### Word Add-in Features

- Scan entire document for statutory references
- Validate against live Singapore statute database
- Flag missing amendments or repealed provisions
- Suggest correct chapter/section references
- Hover tooltips with current text of cited provisions

### Output

Report showing:
- All statutory references found
- Validation status (valid, amended, repealed, not found)
- Suggested corrections where needed

A `verified` or `valid` result means "the cited reference was found in the source statute database at the time of lookup" — not "this citation is authoritative" and not "this submission is fit to file." Every finding is a research aid that requires lawyer verification.

## Audience and Work Shape

Audience: Singapore-qualified lawyers, paralegals, and academic users running a statutory cite-check on a Singapore-law document (typically a submission, opinion, or academic paper). Not for unsupervised drafting, non-lawyer use, or non-Singapore documents.

Work shape: Pattern-Matched Review. Claude (or the BART pipeline) surfaces candidate citation mismatches; the lawyer adjudicates. Output is a list of findings, not a sign-off.

## Inputs and Halt-on-Missing

Required inputs before running:
- The target document (path or selection) containing the citations to check.
- The intended statute snapshot date (the version of the Singapore statute book the user wants citations checked against).
- The scope of the check (whole document, named section, or selection).

If any of these are missing, halt and ask. Do not proceed with assumed defaults — a stale snapshot date or wrong scope is a silent failure mode and the user must specify it explicitly.

## Scope and Legal Use

This skill provides legal *support*, not legal advice. The three legal failure modes are addressed below.

**Legal advice vs. legal support.** Outputs labelled `amended`, `repealed`, `not found`, or `suggested correction` are research signals, not legal conclusions. Whether a repealed provision still applies under transitional rules, whether an amendment is in force, and whether a different section is the correct citation for the proposition advanced are all questions for the responsible lawyer. The skill does not opine on substantive correctness or fitness to file.

**Privilege and confidentiality.** The BART pipeline routes document text (potentially including privileged drafts, pre-filing submissions, and client matter content) through an external "live Singapore statute database," a ChromaDB vector store, and Legal-BERT/GEMMA inference. This has direct privilege and confidentiality implications. Do not invoke on privileged or unfiled draft material unless the firm has assessed that routing the document (or extracted citation context) through the BART backend is acceptable under its information-handling rules. Where possible, configure the pipeline to send citation strings only — not surrounding factual or strategic context. Treat any input passed to this skill as if it were being sent to a third-party service.

**Accountability.** A qualified lawyer must review every flagged finding and every `verified`/`valid` citation before the document is filed, circulated, or relied upon. The skill must record which statute snapshot date was used so the basis of the check is auditable. Outputs are marked draft until a lawyer signs off; the skill itself is not the system of record.

## Confidence Bands

Every finding must carry a confidence band, surfaced alongside the reranker score where available:

- **High** — exact match on chapter and section against the named statute snapshot; statute is in force at that snapshot date.
- **Medium** — fuzzy or semantic match (e.g., near-identical section text under a different chapter, or a section number not present but a close semantic neighbour exists). Flag for lawyer review; do not auto-correct.
- **Low / Review** — `not found`, `repealed`, transitional-provision adjacent, suggestion produced by the semantic-search step without a direct lexical match, or non-SG citation detected. Do not present as `verified`. Halt and surface the original cite verbatim to the lawyer with the source text and snapshot date.

## Out of Scope

This skill does NOT do:
- Case citations (use a case-law citation checker such as sgcite).
- Subsidiary legislation, practice directions, or non-statute instruments unless explicitly listed as in scope.
- Foreign-law references — any non-Singapore citation in the input must fail loud and be routed to lawyer review.
- Pinpoint accuracy of the proposition cited (i.e., whether the section actually supports what the document says it supports).
- Transitional-provision analysis — flags repeals but does not determine whether transitional rules still apply.
- Sign-off on citation accuracy for the purposes of professional rules. The lawyer remains accountable.

## Escalation

Stop and route to the responsible lawyer when:
- a citation is returned as `not found`, `repealed`, or `amended`;
- the confidence band is Low / Review, or the reranker score falls below the firm's threshold;
- the input contains non-SG citations or non-statute instruments;
- the statute snapshot date is unknown, missing, or older than the firm's tolerance;
- the input may contain privileged or pre-filing material and the firm has not approved external lookups against the BART backend;
- the suggestion step produces a "correct" section without a direct lexical match against the document's existing reference.

In all escalation paths, surface the original citation verbatim, the source text the pipeline matched against, the snapshot date, and the confidence score. Do not silently substitute a "suggested correction."

## Limitations

- Currently private (access may be restricted). If the backend is unreachable or stale, treat the entire run as failed and do not present partial results as `verified`.
- Requires internet connection for live statute lookup.
- Singapore statutes only.
- Output depends on the freshness of the underlying ChromaDB vector store and the live database; a stale snapshot can silently miss recent amendments or repeals.

## QA Remediation (LegalQuants, 2026-05)

LegalQuants added the Audience and Work Shape, Inputs and Halt-on-Missing, Scope and Legal Use (covering legal-advice-vs-support, privilege/confidentiality, and accountability), Confidence Bands, Out of Scope, and Escalation sections to address gaps identified by `legal-builder-hub:qa` against the Legal Skill Design Framework. The original technical content describing the BART pipeline (semantic search, BM25 + reranker, ChromaDB, Word Add-in) is unchanged; the remediation reframes the pipeline's outputs as research signals requiring lawyer verification rather than authoritative conclusions, and makes explicit the confidentiality stance for documents passed to the live Singapore statute database. Original author attribution to Kevan Wee is preserved.
