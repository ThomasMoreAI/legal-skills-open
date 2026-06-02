---
name: case-file-analyzer
title: Stateless Case File Analyzer (Ralph Loop Edition)
description: Use when running structured, adversarial analysis across large case-file directories — extracts facts, claims, and legal views into XML metadata via a stateless R.A.L.P.H. loop, then synthesizes contradictions and timeline across all files. Proof of concept; not a finished product.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/case-file-analyzer
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
tags: [case-files, multi-agent, adversarial, ralph-loop, verification]
---

# Stateless Case File Analyzer (Ralph Loop Edition)

⚠️ **Proof of concept.** This is an open-source demo showing how far agentic case file revision can be implemented efficiently. It is not a finished ready-to-use product.

| Attribute | Value |
| :--- | :--- |
| **Description** | Stateless, autonomous AI agent utilizing the R.A.L.P.H. pattern for adversarial and structured case file analysis. Runs parallel verification for factual claims, logic, and completeness across massive document directories. |
| **Author** | Attorney Dennis G. Jansen / J-Law.de |
| **Version** | 3.1.0 |
| **Jurisdiction** | Agnostic |
| **Last Reviewed** | 2026-05 |
| **Last Reviewed By** | LegalQuants (QA remediation) |
| **Tags** | legal-analysis, quality-control, multi-agent, verification, adversarial, certificate, ralph-loop |

## What it does & What it doesn't do

**What it does:**
* **Granular Extraction:** Scans case files one by one in isolated executions, extracting facts, claims, and legal views into standardized XML metadata.
* **Context Preservation:** Uses the R.A.L.P.H. pattern (stateless disk-I/O loops) to prevent "Lost in the Middle" context degradation on massive case files.
* **Adversarial Synthesis:** Acts as a quality gate, reviewing fully prepared metadata across all files to synthesize a cohesive legal perspective and timeline.

**What it doesn't do:**
* **No Memory:** It does not remember past conversational context. If it is not written to `PRD.md` or a state file, it does not exist.
* **No Legal Advice:** It does not replace licensed human counsel. It is a structural decomposition and synthesis tool.
* **No Conversational Filler:** It does not chat. It reads instructions, executes a single task, writes to disk, and terminates.

## The 3-Step Execution Process

When triggered via `"scan case files"`, the agent orchestrator must execute the following sequence via the R.A.L.P.H. loop:

1. **Step 1: Granular Review & Metadata Extraction**
   Review each file individually. Create metadata, tags, and review results via the [Ralphing Skill](references/ralphing_skill.md), *unless* the existing review on the disk is already complete and sufficient. Output using the Individual Summary Template.
2. **Step 2: Perspective Analysis**
   Review the fully prepared review results and metadata from Step 1 across *all* files under a specific, user-defined legal perspective (e.g., procedural errors, substantive validity, evidentiary contradictions).
3. **Step 3: Holistic Synthesis**
   Synthesize the conclusion and results across all relevant files into a final case report, utilizing the Synthesis Template.

## System References

Initialize the workspace with the following reference modules:
* **[Configuration](references/configuration.md):** Model settings and workspace initialization.
* **[Definitions](references/definitions.md):** Strict guidelines for example for classifying Facts vs. Opinions.
* **[Ralphing Skill](references/ralphing_skill.md):** The bash orchestrator and execution loop mechanics.
* **[Templates](references/templates.md):** XML disk-write schemas for metadata and synthesis.

## Audience and Work Shape

**Audience.** Qualified litigators, dispute-resolution lawyers, paralegals, and litigation-support staff who already work with structured case files and understand the role of fact-vs-claim distinction. Not for unsupervised use by non-lawyers, opposing parties, or self-represented litigants. Treat outputs as worked input for a lawyer, not a deliverable.

**Work shape — dual.** This skill operates in two distinct shapes across its pipeline. Both shapes apply on every run:

- **Pattern-Matched Review (Steps 1-2: extraction and perspective analysis).** Each file is parsed against a fixed schema (facts / opinions / legal views) using definitional rules in `references/definitions.md`. The model checks each unit against a known template. Outputs are lists of extracted units with XML tags, not conclusions.
- **Accretive Judgment (Step 3: holistic synthesis).** The synthesis step builds a coherent timeline, identifies contradictions across files, and produces a holistic assessment. This is not pattern matching against a reference — it is reasoning across the corpus and accumulating a position. Outputs must be treated as draft analysis for lawyer review, not a finding.

The dual shape matters because confidence and escalation rules differ between the two stages, and downstream readers must not treat the synthesis output as if it were the same kind of artifact as the extraction output.

## Scope and Legal Use

This skill provides legal **support**, not legal advice. A completed synthesis is a structured restatement of what is in the case files, with timeline and contradiction flags. It is not a case theory, a litigation recommendation, an admissibility ruling, or a sign-off on any factual or legal conclusion.

**Privilege and confidentiality of case files being scanned.** Case files routinely contain privileged client communications, work product, settlement-privileged material, and material covered by data-protection regimes (GDPR, attorney-client privilege under the applicable jurisdiction, professional-secrecy rules). Running this skill against such files moves their contents through whichever model API is configured in `references/configuration.md` and writes structured extracts to disk in the output directory.

Before invoking on real matter files:
- Confirm with the responsible lawyer (and the client, where required by professional rules) that routing the case-file contents through the configured model API is permitted on this matter.
- Confirm that the output directory is inside a firm-approved storage location with the matter's confidentiality classification, not a general scratch directory.
- Treat the generated `summary_*.xml`, `perspective_review.xml`, and `final_synthesis.xml` artifacts as **work product** — apply the same retention, access, and destruction controls as you would to a paralegal's litigation summary.
- Do not invoke on third-party privileged material that arrived in error, on opposing-party documents you are not authorized to process, or on material under a protective order whose terms you have not checked.

**Accountability gap.** Stateless agents are designed to forget. The R.A.L.P.H. loop deliberately discards context after each iteration, which is good for context-window hygiene but means there is no in-model record of why a given extraction was made, what was discarded, or what edge cases the agent encountered. The on-disk artifacts (`PRD.md`, `progress.txt`, `summary_*.xml`) are the only record. A qualified lawyer must:
- Review the granular `summary_*.xml` outputs against the source files before any extracted fact is relied upon.
- Re-read the `final_synthesis.xml` against the underlying corpus before any contradiction, timeline entry, or holistic assessment is acted upon.
- Sign off in their own name on any output that leaves the firm, is filed, or is shown to a client. The skill does not, and cannot, sign off.

## Confidence Bands

Confidence is reported separately for the extraction phase and the synthesis phase, because the two work shapes warrant different reliability profiles.

**Extraction (Steps 1-2):**
- **High** — file parsed cleanly; each extracted unit is wrapped in the correct tag (`<fact>`, opinion, legal view); quotes match the source verbatim; no `[FAILED]` markers in `progress.txt` for this file.
- **Medium** — file parsed but with one or more of: ambiguous fact-vs-claim classification, missing date or party reference, OCR-suspect source, or partial extraction. Route to lawyer review of that file.
- **Low / Review** — file marked `[FAILED]`, classification rules in `definitions.md` could not be applied confidently, or the source contains material that does not fit the schema (e.g., diagrams, images, handwritten annotations). Do not include in synthesis without lawyer triage.

**Synthesis (Step 3):**
- **High** — all input `summary_*.xml` files have High extraction confidence; the timeline is reconstructable from `<fact>` tags alone; identified contradictions are between explicit, quoted claims.
- **Medium** — synthesis includes any Medium-confidence inputs; or the perspective requested in Step 2 requires the agent to bridge gaps between files using non-quoted inference. Flag the bridge points.
- **Low / Review** — any Low-confidence input was included; the perspective requested requires reasoning the corpus does not support; or the adversarial sub-agents disagree on whether a flagged item is a material contradiction. Mark `<status>REVIEW REQUIRED</status>` in `final_synthesis.xml` and stop.

## Out of Scope

- **Live-litigation strategy decisions.** Not for "should we settle", "should we move to dismiss", "is this a winning argument" — outputs are extracts and contradiction flags, not strategic recommendations.
- **Memory-dependent reasoning.** The R.A.L.P.H. loop is stateless by design. Anything that requires continuity of reasoning across files within a single context window (e.g., long chains of dependent inference) cannot be done here without manual lawyer assembly.
- **Sensitive matters without firm-approved data flow.** Do not invoke on matters where the configured model API, the output directory, or the host machine has not been cleared by the firm's information-security and confidentiality controls. This includes regulated-data matters (health, financial, criminal-defense), matters under protective order, and any matter where the client has restricted AI processing.
- **Substantive legal advice or fitness-to-file sign-off.** The skill does not assess admissibility, sufficiency of evidence, jurisdiction, applicable law, limitation periods, or procedural compliance.
- **Verification of citations or authorities.** The skill extracts legal views as stated in the source; it does not verify whether the cited statute, case, or paragraph reference actually says what the document claims.
- **Cross-jurisdiction translation or comparative analysis.** Jurisdiction-agnostic extraction means the skill does not adapt its categories to a specific procedural code; it does not flag jurisdiction-specific issues.

## Escalation

Stop the loop and route to the responsible lawyer when:
- The agent detects material that may be **privileged or covered by professional secrecy** and the matter file has not been pre-cleared for AI processing — halt before writing further artifacts, log the file path in `progress.txt`, and exit.
- The agent encounters a file or matter whose **jurisdiction is unknown or ambiguous** — the extraction categories (Facts / Opinions / Legal Views) are jurisdiction-agnostic, but applicable rules on what counts as a fact, what is privileged, and how legal views should be framed are not. Halt and ask.
- The **adversarial sub-agents disagree on material facts** — i.e., the perspective-analysis step in Step 2 produces contradictory readings of the same `<fact>` across runs, or the synthesis step flags a contradiction that depends on which sub-agent's extraction is trusted. Do not paper over the disagreement in the synthesis; surface both readings and stop.
- The corpus contains **non-text or structurally non-schema material** (diagrams, exhibits, audio transcripts with timestamps, images) that the schema cannot represent — flag the file, do not silently drop its content from synthesis.
- The model in use is **not the one configured** in `references/configuration.md`, and the substitution was not approved — halt rather than proceed with a model that may not satisfy the reasoning or confidentiality profile required for the matter.

On escalation, the agent writes the trigger and the file path to `progress.txt`, marks the synthesis status as `REVIEW REQUIRED` if Step 3 is in progress, and exits cleanly. The responsible lawyer decides whether to override, restart, or abandon the run.

## QA Remediation (LegalQuants, 2026-05)

LegalQuants applied design-quality QA against the Legal Skill Design Framework and added the Audience-and-Work-Shape, Scope-and-Legal-Use (covering legal-advice-vs-support, privilege/confidentiality of case-file inputs, and the accountability gap created by stateless operation), Confidence Bands, Out of Scope, and Escalation sections. The frontmatter was normalized to standard Anthropic Skills format and the file renamed from `agent.md` to `SKILL.md`. The technical content (R.A.L.P.H. pattern, 3-step execution process, attribute table, references) is unchanged. Dennis G. Jansen / J-Law.de is retained as author of the underlying skill.
