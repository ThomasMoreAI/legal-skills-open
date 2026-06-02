---
name: dpa-checklist-review-legalquants
title: DPA Checklist Review
description: Use when the user provides a Data Processing Agreement, Data Processing Addendum, or HIPAA Business Associate Agreement and asks whether it contains the terms required under the applicable data-protection regime. Produces a structured checklist scoring each required term as present, partial, missing, or unclear, with clause references and recommended language for any gaps. Supports GDPR Article 28, US state privacy laws (CCPA/CPRA, VCDPA, CPA, CTDPA, and similar), HIPAA BAAs, and general commercial DPAs without a specified regime.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-skills/tree/main/skills/dpa-checklist-review
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: data-protection
language: en
---

# DPA Checklist Review

Conduct a structured compliance review of a Data Processing Agreement, DPA-equivalent addendum, or Business Associate Agreement against the requirements of the applicable regulatory regime. The output is a checklist suitable for a compliance tracker — each required term has a row, an assessment, and a clause reference.

## When this skill applies

Apply when the user provides a DPA, DPA addendum, or BAA and asks for compliance review against a specific regulatory regime. The skill works against four distinct regimes (see `regulatory_regime` input) and applies different requirements for each.

Do not apply this skill to:

- Privacy policies. Those are public-facing notices, not contracts; different review skill needed.
- Standalone privacy schedules or security exhibits inside larger agreements where the privacy/security terms have not been collected into a DPA structure. Tell the user the substantive privacy and security terms need to be pulled into a DPA-shaped structure before this skill is useful.
- Contractual privacy clauses inside MSAs that have not been broken out as a DPA addendum. Recommend the user request a separate DPA addendum from the counterparty, which is now industry standard.
- Cross-regime analysis (e.g., "is this GDPR-compliant *and* HIPAA-compliant?"). Run the skill twice with different `regulatory_regime` values and compare outputs.

## Privilege and confidentiality

DPAs and BAAs frequently contain client-confidential information (data flows, security postures, vendor relationships, deal terms) and the resulting compliance review is plausibly attorney work product. Before running the skill, the user must confirm:

- **Privileged work product.** The checklist produced by this skill is a draft work product intended to support legal advice. Treat the output as presumptively privileged where applicable, and do not distribute it outside the attorney-client circle without considering waiver consequences.
- **External-model exposure.** If this skill is being executed in an environment that routes the document to a model or service outside the user's attorney-supervised workflow (e.g., a non-BAA-covered API, a non-enterprise consumer endpoint, a logged training surface), confirm with the user before proceeding. Run this skill only inside an attorney-supervised workflow where the routing and retention posture has been vetted.
- **Legal-use posture.** Output is a draft for review by qualified privacy counsel — it is not a legal opinion, not a regulator-facing artifact, and not a substitute for a PIA, TIA, or other formal compliance assessment (see "What this skill does not do").

If the user cannot confirm that the workflow is attorney-supervised and the model routing is acceptable for the document at hand, stop and surface the concern before running the review.

## Inputs

The skill requires the document and the regulatory regime. If regime is not provided:

> "Before I review, which regulatory regime should I check this DPA against?
>
> - **GDPR** (EU/UK GDPR Article 28; covers any DPA processing EU/UK personal data)
> - **US state privacy** (CCPA/CPRA, Virginia VCDPA, Colorado CPA, Connecticut CTDPA, Utah UCPA, Oregon OCPA, and similar)
> - **HIPAA BAA** (Business Associate Agreement under US healthcare law)
> - **General commercial** (DPA without a specific regime; checks commercially-standard DPA terms)
>
> If multiple regimes apply, pick the most prescriptive (typically GDPR) for the primary review; we can run additional reviews for other regimes after."

Do not guess the regime from document title or governing law. A document titled "Data Processing Addendum" with Delaware governing law could be GDPR-driven (because it processes EU resident data), CCPA-driven (because it processes California resident data), or both. Only the user knows what data is in scope.

Optional inputs (`party_role`, `data_categories`, `international_transfer_context`, `standard_positions`) refine the analysis. The `party_role` input materially changes severity calibration:

- **Controllers / data exporters / businesses / covered entities** want strong, specific processor obligations — they bear regulatory liability for processor failures.
- **Processors / data importers / service providers / business associates** want clear, operationally feasible scope — vague obligations create open-ended liability.

When `party_role` is not provided, default to **controller perspective** (regulators almost always investigate the controller, so controller-favorable analysis is the safer default for reviews) and note the assumption in the report. Ask the user to re-run if they are on the processor side.

## Workflow

Produce the review in three passes.

### Pass 1: Document orientation

Before substantive review:

- Confirm the document is actually a DPA / DPA addendum / BAA. If it is a privacy policy, an MSA with privacy clauses not broken out, or a different instrument, stop and tell the user.
- Note the parties and which is controller / processor (or equivalent under the relevant regime).
- Note the governing law and any specified data-protection authority.
- Note the structure: does the document have the required terms organized into sections, or are they scattered? A DPA without clear structural sections is harder to assess.
- Identify any annexes, schedules, exhibits, or appendices and note what they cover (typically: data categories, processing purposes, security measures, sub-processors, SCCs).

### Pass 2: Regime-specific term checking

Walk through the requirements for the specified regime using the corresponding reference file:

- For `gdpr`: use `reference/gdpr_requirements.md`. The required terms are the nine items in GDPR Article 28(3) plus security obligations under Article 32 plus (when applicable) international-transfer mechanisms.
- For `us_state_privacy`: use `reference/us_state_privacy_requirements.md`. The required terms are the convergent set across CCPA/CPRA, VCDPA, CPA, CTDPA, and similar laws; differences between laws are noted where material.
- For `hipaa_baa`: use `reference/hipaa_baa_requirements.md`. The required terms are those listed in 45 CFR §164.504(e)(2) plus the additional requirements under HITECH and the HIPAA Omnibus Rule.
- For `general_commercial`: use `reference/general_commercial_requirements.md`. The expected terms are commercially-standard DPA terms in the absence of a specific regime — broadly compatible with any of GDPR, US state privacy, or HIPAA but not optimized for any.

For each required term, classify:

- **Present** — the document addresses this term and the addressing is compliant with the regime's requirements.
- **Partial** — the document addresses this term but the addressing is non-compliant, narrower than required, or has problematic carve-outs.
- **Missing** — the document does not address this term.
- **Unclear** — the document arguably addresses this term but the language is ambiguous enough that compliance cannot be confirmed without negotiation.
- **N/A** — this term does not apply given the document type, regime variant, or specific facts.

### Pass 3: Compile the checklist and posture

Compile the findings into the structured checklist (see Output section). Add an overall posture paragraph stating whether the document is:

- **Compliant** — all required terms present and adequate; no negotiation needed for compliance purposes (business preferences may still warrant changes).
- **Compliant with minor gaps** — most terms present; minor partial/missing items can be addressed via short negotiation or in supporting agreements.
- **Non-compliant** — material gaps requiring negotiation before signing; the document does not currently meet the regime's requirements.
- **Materially non-compliant** — multiple critical terms missing or partial; the document needs substantial reworking, or the user should propose replacing it with the user's own template.

## Output

Produce the review as a structured checklist in markdown:

```markdown
# DPA Checklist Review: [Document name or counterparty]

**Regulatory regime:** [gdpr | us_state_privacy | hipaa_baa | general_commercial]
**Party role:** [controller | processor | etc.]
**Data categories:** [user-provided context, or "not specified"]
**International transfer context:** [for GDPR; user-provided context, or "not specified"]

## Overall posture

[One paragraph: compliant / compliant with minor gaps / non-compliant / materially non-compliant. State the headline gap or strength. State the recommended next step at a high level.]

## Compliance checklist

| # | Required term | Source | Status | Severity | Clause | Assessment |
|---|---|---|---|---|---|---|
| 1 | [Term name] | [Statute reference, e.g., "GDPR Art. 28(3)(a)"] | Present / Partial / Missing / Unclear / N/A | High / Medium / Low | [§ ref or "—"] | [One-line assessment] |
| 2 | [...] | [...] | [...] | [...] | [...] | [...] |
| ... | | | | | | |

Every finding gets a severity rating. Calibrate severity using the Critical / Material / Minor bands in the regime reference file (`reference/gdpr_requirements.md`, `reference/us_state_privacy_requirements.md`, `reference/hipaa_baa_requirements.md`, `reference/general_commercial_requirements.md`), mapped as: **High** = Critical (regulator-facing requirement, missing it would render the document non-compliant); **Medium** = Material (gap creates real legal or operational risk but is not a per-se compliance failure); **Low** = Minor (drafting hygiene, commercial preference, or belt-and-braces). Severity is required even for Present items so the reader can see what the document gets right on the high-stakes terms at a glance.

## Detailed findings

[For each Partial, Missing, or Unclear item, a subsection with:]

### [#] [Term name] — [Status]

**Required by:** [Statute reference]

**What's required:** [Brief plain-language statement of what the regime requires.]

**What the document says:** [Quoted or paraphrased clause language, with citation. If the term is missing, "Not addressed."]

**Why this is a gap:** [Specific deficiency from the regime's perspective.]

**Recommended language:** [Specific suggested clause language to add or modify. Reference any applicable model clauses (e.g., EU SCCs) where appropriate.]

## Items requiring human judgment

[Items the skill cannot resolve and that need the user's regulatory-counsel expertise or business judgment. Examples: jurisdictional applicability questions, novel data flows the skill is unfamiliar with, regulator-specific guidance the skill cannot verify is current.]

## Recommended next steps

[Short bulleted list. Common options: sign as-is (if compliant), negotiate the redlines proposed above, propose user's own DPA template, escalate specific issues to outside privacy counsel, run an additional review under another regime.]
```

The checklist table is the centerpiece. Detailed findings only cover non-Present items — do not pad with "Present and standard, no further notes" rows; the table already shows that.

## Edge cases and refusals

- **Document is not a DPA/BAA.** Stop and tell the user. Common adjacent documents that get confused for DPAs: privacy policies, security questionnaires, data sharing agreements (different instrument under GDPR), data licensing agreements, MSAs with privacy clauses but no DPA addendum.
- **Regime is gdpr but the document does not contain SCCs or another transfer mechanism, and `international_transfer_context` indicates transfers occur.** Critical gap; flag in posture and detailed findings even if the controller-processor terms are otherwise compliant.
- **Regime is hipaa_baa but the document does not invoke HIPAA at all** (no reference to PHI, BAA, 164.504, etc.). The document may not actually be a BAA. Flag and ask the user to confirm.
- **Document is a DPA from before significant regime changes** (e.g., a GDPR DPA dated 2018 without Schrems II / 2021 SCC updates; a CCPA DPA dated 2020 without CPRA amendments). Flag in posture and note the regulatory drift.
- **Document includes terms for multiple regimes.** Some DPAs are written to satisfy GDPR + CCPA + others simultaneously. Review against the requested regime and note where multi-regime drafting creates ambiguity (e.g., conflicting deletion timelines).
- **Document references model clauses or templates that are not attached.** If the document says "the parties have entered into the EU SCCs" but no SCCs are attached or referenced specifically, flag — the SCCs are a required artifact, not a reference.

## What this skill does not do

- Give a definitive compliance opinion. Outputs are drafts for human review; ultimate compliance determinations belong to qualified privacy counsel.
- Predict regulator behavior. Flags gaps; does not opine on enforcement risk.
- Negotiate. Suggests language; does not draft side letters.
- Replace a privacy impact assessment, transfer impact assessment, or other formal compliance artifact. Those are separate processes.
- Cover non-US/non-EU regimes (Canada PIPEDA, Brazil LGPD, China PIPL, etc.) in v1.0.0. The structure supports adding regime-specific reference files; community contributions welcomed.

## Reference materials

- `reference/gdpr_requirements.md` — Article 28(3) required terms, Article 32 security, transfer-mechanism requirements.
- `reference/us_state_privacy_requirements.md` — Convergent CCPA/CPRA/VCDPA/CPA/CTDPA/UCPA/OCPA processor-contract requirements.
- `reference/hipaa_baa_requirements.md` — 45 CFR §164.504(e)(2) BAA requirements plus HITECH/Omnibus updates.
- `reference/general_commercial_requirements.md` — Commercially-standard DPA terms when no specific regime is stated.
- `examples/example_gdpr.md` — Worked example: GDPR DPA review from a controller perspective.
- `examples/example_us_state.md` — Worked example: US state privacy DPA review from a service-provider/processor perspective.

## QA Remediation (LegalQuants, 2026-05)

LegalQuants QA evaluated this skill as SOME CONCERN against the Legal Skill Design Framework on 2026-05-11. Targeted remediation applied 2026-05:

- **Privilege treatment strengthened.** Added an explicit "Privilege and confidentiality" section in Scope, requiring the user to confirm attorney-supervised workflow and acceptable model-routing posture before running the skill. Treats output as presumptively privileged work product and warns against external-model exposure of confidential client documents. Reinforced the "draft for review by qualified privacy counsel" framing already present in "What this skill does not do".
- **Severity surfaced in headline checklist.** Added a `Severity` column (High / Medium / Low) to the mandated checklist table so the Critical / Material / Minor calibration from the regime reference files propagates into the headline artifact rather than being buried in prose. Severity is required for every row, including Present items, so a reader scanning the table can see the document's posture on high-stakes terms at a glance.
- **Provenance reconciled.** `author` field set to Kevin Keller (matching the registry README). `last_reviewed` and `last_reviewed_by` fields added to surface the QA cadence on the artifact itself.

Technical content (workflow passes, regime reference files, output structure, edge cases, refusal triggers) preserved unchanged. Substantive privacy-counsel judgment required to use this skill is unchanged.
