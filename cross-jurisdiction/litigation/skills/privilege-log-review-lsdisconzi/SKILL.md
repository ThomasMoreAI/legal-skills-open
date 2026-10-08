---
name: privilege-log-review-lsdisconzi
title: Privilege Log Review
description: Analyze cross-border privilege and confidentiality. Distinguishes each jurisdiction's privilege protections and identifies cross-border privilege risks.
author: lsdisconzi
author_url: https://github.com/lsdisconzi/craudio-para-adevogados/tree/main/skills/privilege-log-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: litigation
language: en
---

# Privilege Log Review

Cross-border litigation creates complex privilege issues. This engine analyzes which protections apply to which documents under each jurisdiction's law and identifies privilege risks. It names no statute — privilege protections are loaded from jurisdiction packs.

## Inputs

- **Matter facts** — the document inventory and counsel/co-counsel structure from `{vault root}`.
- **Jurisdiction pack(s)** — `procedural-rules.yaml` supplies each jurisdiction's privilege protections (attorney-client confidentiality, professional secrecy, work-product equivalents, joint-defense recognition) with their sources, scope, and exceptions.

## Running this skill

1. **Load configuration.** Read the configured matter profile and firm profile from the plugin config directory (see CLAUDE.md `## Configuration Location`). If a file is missing, or a critical field still shows `[PLACEHOLDER]`, STOP — tell the attorney: "This plugin needs setup. Run the `cold-start-interview` skill."
2. **Apply the frame.** The Plugin Operating Rules, Shared Guardrails, Decision posture, Jurisdiction recognition, Retrieved-content trust, and Ontology Governance sections of CLAUDE.md govern this skill. The workflow below is a FLOOR, not a ceiling.
3. **Resolve vault paths.** Every `{vault root}` reference resolves against `## Vault location` in CLAUDE.md. Never hard-code an absolute path.
4. **Determine active packs.** Read which jurisdiction packs the matter declares (matter profile `## Packs`); load their privilege protections.
5. **Apply the work-product header** from CLAUDE.md `## Outputs` to every internal deliverable; suppress it on externally-facing output per Quiet mode.
6. **Run the workflow below.**
7. **Close** with the `⚠️ Reviewer note` block and the next-steps decision tree from CLAUDE.md `## Outputs`. Run the `ontology-validate` skill on the output before it reaches a court or counterparty.

---

## Workflow

### 1. Privilege framework by jurisdiction
For each jurisdiction pack the matter declares, tabulate its privilege protections: protection name, source, scope, and exceptions. Note where one jurisdiction's protection is narrower than another's — that gap is the source of cross-border risk.

### 2. Document classification
Classify every matter document by privilege level — attorney-client communications, internal legal analysis / work product, client-supplied evidence, third-party evidence, court filings, co-counsel communications. Assign each the appropriate marking in the language of the relevant jurisdiction.

### 3. Cross-border privilege risks
For each document type that may move between jurisdictions, assess the risk that the destination jurisdiction does not recognize the origin jurisdiction's protection, and state a mitigation. Pay particular attention to: work-product equivalents (often narrower outside common-law systems), recordings made in public spaces (generally not privileged), co-counsel communications (joint-defense privilege may not be recognized), and expert reports.

### 4. Privilege log preparation
For any confidential document withheld from disclosure, produce a log row: Doc ID, date, author, recipient, description, privilege basis, redaction.

### 5. Destination check
Before any document leaves the firm, apply the CLAUDE.md destination-check guardrail: is the recipient inside the privilege circle? Sending to a recipient outside it may waive protection.

### 6. Output
- **Document privilege classification** — all matter documents categorized
- **Cross-border privilege risk matrix** — jurisdiction × document type × risk
- **Privilege log template** — for discovery/disclosure
- **Co-counsel protocol** — how to communicate without waiver
- **Client confidentiality instructions** — what the client should and should not share

## Guardrails

- This skill identifies privilege risks, not legal conclusions on privilege.
- Privilege determinations are jurisdiction-specific — consult local counsel.
- Never waive privilege without the client's informed consent.
- When in doubt, mark as privileged and flag for attorney review (two-way door).
- The "no silent supplement" rule applies: if unsure about privilege status, flag it.
- **Ontology compliance:** outputs must satisfy the litigation-relevant error codes in `core/ontology/error-catalog.md`. If an invariant violation is detected, flag with `[ONT-ERROR: <code>]` and do not produce confident output. I-1 is absolute: no conclusory language.
