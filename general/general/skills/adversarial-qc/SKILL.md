---
name: adversarial-qc
title: Adversarial QC
description: 'Adversarial quality control for AI deliverables. Run structured parallel verification using one or two models before delivering reports, plans, analyses, scripts, or any substantive work. Use when: (1) reviewing a deliverable before sending to a human, (2) user asks to ''QC this'', ''review this'', ''check this'', ''verify this'', (3) user wants a quality gate on AI output, (4) validating factual claims, numbers, logic, or completeness. Configurable: single-model (two agents, same model) or cross-model (two different providers). Outputs a QC certificate with pass/fail/review items and evidence.'
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/adversarial-qc
license: Apache-2.0
version: 0.1.1
execution_mode: open
jurisdiction: general
practice: general
language: en
tags:
- quality-control
- multi-agent
- verification
- adversarial
- certificate
sources:
- title: Certificate template
  path: references/certificate-template.md
- title: Checklist
  path: references/checklist.md
- title: Config
  path: references/config.md
- title: Custom checklists
  path: references/custom-checklists.md
---

# Adversarial QC

Structured quality control for AI deliverables. Two agents independently verify a deliverable against a checklist, then results are compared. Agreements = high confidence. Disagreements = flagged for human review.

## Quick Start

1. Read the deliverable to be reviewed
2. Read `references/checklist.md` for the verification checklist
3. Read `references/config.md` for model configuration
4. Run the QC process (see Workflow below)
5. Generate the QC certificate

## Configuration

The user controls these settings. Ask if not specified:

- **Mode**: `single` (one model, two agent personas) or `cross` (two different models)
- **Models**: Which model(s) to use. Defaults: primary = current session model, secondary = user's choice
- **Checklist**: `standard` (general-purpose) or a custom checklist path
- **Output**: `certificate` (PDF), `inline` (text summary), or `both`
- **Depth**: `quick` (5-item core checklist, ~30s), `standard` (full checklist, ~2min), `deep` (full checklist + source re-verification, ~5min)

## Workflow

### Step 1: Ingest

Read the deliverable. Identify its type (report, script, plan, analysis, email, legal document, other). This determines which checklist items are relevant.

### Step 2: Run Agent A (Verifier)

Spawn a sub-agent with these instructions:

```
You are QC Agent A — a verification specialist. Your job is to check a deliverable against a structured checklist. You must be thorough, skeptical, and evidence-based.

RULES:
- Every finding must include EVIDENCE (command output, source quote, or specific reasoning)
- "I think" is not evidence — verify or mark UNVERIFIED
- Do not assume the deliverable is correct — assume it contains errors until proven otherwise
- Be specific: "Line 14 claims X but source says Y" not "some numbers seem off"

DELIVERABLE:
[Insert deliverable text]

CHECKLIST:
[Insert from references/checklist.md — only items relevant to deliverable type]

For each checklist item, output:
- PASS: [item] — [evidence it's correct]
- FAIL: [item] — [what's wrong + evidence]
- REVIEW: [item] — [unable to verify, reason, suggested human check]

End with a summary: X pass, Y fail, Z review.
```

### Step 3: Run Agent B (Challenger)

Spawn a second sub-agent (different model if cross-mode). Same instructions but with this addition:

```
You are QC Agent B — an independent challenger. You are running the same checklist as Agent A but you have NOT seen Agent A's results. Your job is to find what Agent A might miss.

Pay special attention to:
- Claims that SOUND correct but aren't verified
- Numbers that are plausible but unchecked
- Logic that flows well but has gaps
- Things that would embarrass the author if a domain expert read them
```

If single-model mode: use different system prompts to create genuine perspective difference. Agent A is methodical and checklist-driven. Agent B is adversarial and tries to break things.

### Step 4: Compare Results

For each checklist item:
- **Both PASS** → High confidence. Mark GREEN.
- **Both FAIL** (same issue) → Confirmed error. Mark RED.
- **One PASS, one FAIL** → Disagreement. Mark YELLOW. Include both agents' evidence. Flag for human review.
- **Either REVIEW** → Unverifiable. Mark YELLOW. Flag for human review.

### Step 5: Generate Certificate

Use the template in `references/certificate-template.md`. Output as:
- **Inline**: Text summary in chat (for quick checks)
- **PDF**: Full certificate with evidence (for formal deliverables)
- **Both**: If user wants both

## Checklist Customization

Users can create custom checklists for specific domains. See `references/custom-checklists.md` for examples (legal, financial, technical, editorial).

To use a custom checklist: place a `.qc-checklist.md` file in the project directory, or specify `--checklist path/to/checklist.md`.

## Cost Guidance

| Depth | Single-model | Cross-model |
|-------|-------------|-------------|
| Quick | ~$0.02-0.05 | ~$0.04-0.10 |
| Standard | ~$0.10-0.30 | ~$0.20-0.50 |
| Deep | ~$0.30-1.00 | ~$0.50-1.50 |

Costs assume Sonnet-tier models. Using Opus increases ~5-10x.

## Tips

- For routine checks, `quick` + `single` is fine
- For client-facing deliverables, `standard` + `cross` catches more
- For high-stakes work (legal filings, financial reports), `deep` + `cross` + human review of all YELLOW items
- The certificate is the audit trail — save it alongside the deliverable

## Audience and Work Shape

Audience: AI-assisted reviewers (lawyers, analysts, drafters) running a structured pre-delivery quality gate on a generated artefact. Not for unsupervised drafting, not a substitute for a domain expert, and not appropriate for non-AI-fluent users who would treat a GREEN certificate as a sign-off.

Work shape: Pattern-Matched Review with an accretive overlay. Most items (factual claims, numbers, attribution, formatting, consistency) are pattern-matched against a checklist; the `cringe test`, `adversarial read`, and `recipient test` items are accretive-judgment moves dressed as pattern matching. The skill produces a list of findings, evidence, and item-level confidence — never a sign-off.

## Scope and Legal Use

This skill provides AI-output *support*, not legal advice and not legal substance review. A GREEN certificate means "both agents agreed each checklist item is satisfied at the surface level" — it does not mean the deliverable is legally sufficient, fit to file, fit to send, or correct on substance.

**Legal advice vs. legal support.** When the deliverable is a legal document, filing, regulatory submission, or contract, the QC pass is mechanical: numbers checked, citations attributed, defined terms consistent, cross-references resolved. It is *not* a review of legal sufficiency, doctrinal correctness, jurisdictional fit, or professional-responsibility obligations. A GREEN certificate on a legal deliverable is not a lawyer's sign-off and must not be relied upon as one. The user, not this skill, owns the legal-substance call.

**Privilege and confidentiality.** The QC certificate is written to disk as a permanent record of two agents' reasoning about the deliverable. That artefact may be discoverable, may sit outside the attorney-client and work-product privileges depending on jurisdiction and circumstance, and may not be appropriate to retain alongside a privileged draft. Before running this skill on privileged or pre-decisional legal material, confirm with the responsible lawyer that (a) generating a written QC trail is acceptable in this matter and (b) the certificate's storage location is consistent with the matter's privilege posture. Default: save the certificate inside the matter workspace, not in a shared or general-purpose directory.

**Accountability.** The two agents are not signatories. The certificate's `agent signatures` and the README's MIT disclaimer do not close the accountability gap on regulated work. A qualified human reviewer must sign off on any deliverable typed as legal, filing-bound, client-facing, financial, or regulatory — regardless of whether the certificate is GREEN. The mandatory human-reviewer field on the certificate (added in this revision; see Escalation) is the operational anchor for accountability — disclaimer text in the footer is not sufficient.

## Confidence Bands

Item level (existing):
- **GREEN** — Both agents PASS with cited evidence. High confidence at the surface level only.
- **YELLOW** — Agents disagree, or one or both returned REVIEW (unable to verify). Flag for human review.
- **RED** — Both agents FAIL with the same issue. Confirmed surface defect.

Certificate level (new — required to address the gap where 16 GREEN + 1 YELLOW reads identically to 5 GREEN + 12 YELLOW):
- **High Confidence** — 100% GREEN across all relevant checklist items, deliverable type is non-legal, non-regulatory, non-client-facing. Safe to ship subject to user judgement.
- **Mixed** — Any YELLOW items present, or any RED items resolved by human review, or deliverable type is legal/filing/client-facing/regulatory regardless of item results. Requires human reviewer sign-off before ship.
- **Do Not Ship** — Any unresolved RED items, or deliverable type is not identifiable, or the agents agreed but the agreement is suspicious (both confidently asserting an unverifiable claim). Escalate.

The certificate must show the certificate-level band on the front page. A deliverable cannot be marked **High Confidence** if its type is legal, filing-bound, client-facing, regulatory, or court-bound — those route to **Mixed** at minimum.

## Out of Scope

- Does **not** verify legal substance, doctrinal correctness, jurisdictional fit, or fitness to file.
- Does **not** satisfy professional-responsibility QC duties (lawyer's duty of competence and supervision is not discharged by a GREEN certificate).
- Does **not** check privilege exposure, confidentiality status, or whether the deliverable should leave the firm at all.
- Does **not** detect AI hallucinations that both agents share — shared model blind spots are an acknowledged limit of the pattern.
- Does **not** replace second-chair human review on filings, regulatory submissions, court-bound material, or contracts being signed.
- Does **not** verify the agents' own reasoning for hallucination — the certificate records what the agents said, not whether they were right.
- Does **not** validate non-Word output paths, sandbox the PDF rendering pipeline, or police where the certificate is saved.

## Escalation

Stop and route to a qualified human reviewer (do not rely on agent agreement alone) when any of the following triggers fire:

- Deliverable type is **legal document, filing, regulatory submission, court-bound material, or contract being signed** — route to a qualified lawyer regardless of GREEN/RED status. The certificate's `human reviewer:` field is mandatory and must be signed by a named human before ship.
- Deliverable type is **client-facing** (sent outside the firm) — route to the supervising lawyer or accountable owner regardless of item-level results.
- Deliverable references a **jurisdiction or domain the agents may lack reliable training on** — flag and require human verification of the substantive claims.
- The deliverable is **above a complexity or stakes threshold** the user has set (e.g., contract value, regulatory exposure, public-statement risk) — escalate per the user's pre-set rule.
- The two agents **agree** but the agreement is on an **unverifiable or unsourced claim** — treat as suspicious and surface to a human; both agents can be confidently wrong.
- The deliverable **type cannot be identified** at Step 1 — STOP and ask the user before running. Do not proceed with a generic checklist on an unknown artefact.
- **Sources are not accessible** at Step 2 — Agent A's REVIEW state must not be silently swallowed. Halt and ask the user before continuing.
- The certificate would be written to a path **outside the matter workspace or designated skill output directory** — STOP and confirm the output location with the user.

The Step 4 disagreement rule (YELLOW → flag) remains in force for every other case, but the triggers above override agreement: a GREEN on a legal filing still routes to human sign-off.

## QA Remediation (LegalQuants, 2026-05)

LegalQuants added the Audience and Work Shape, Scope and Legal Use (with all three legal failure modes — legal advice vs. support, privilege, and accountability), Confidence Bands (with a new certificate-level overall verdict), Out of Scope, and Escalation sections to address gaps surfaced by the legal-builder-hub:qa framework. The original technical content (Quick Start, Configuration, Workflow, Checklist Customization, Cost Guidance, Tips) is unchanged. The `references/certificate-template.md` Chromium invocation was hardened to remove the `--no-sandbox` flag (a real security weakening that the QA scan flagged as Category 8). Original authorship by Alexios van der Slikke-Kirillov is preserved in the frontmatter.
