---
name: vendor-privacy-policy-first-pass
title: Vendor Privacy Policy First Pass
description: Use when the user has a vendor's published privacy policy (URL, PDF, or pasted text) and wants a fast triage assessment to decide whether deeper diligence is warranted. Produces a short structured report covering what the policy says about key data practices (collection, use, sharing, retention, transfers, rights) plus identification of red flags that warrant escalation to deeper review. Explicitly a first pass, not a full privacy assessment, DPA negotiation, or compliance certification.
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-ai/tree/main/skills/vendor-privacy-policy-first-pass
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Vendor Privacy Policy First Pass

Conduct a fast triage assessment of a vendor's privacy policy to help the user decide whether deeper diligence is warranted before sharing data with the vendor. The output is a structured summary plus red-flag identification, not a full privacy assessment.

This skill is calibrated for the in-house counsel use case: a vendor has been proposed, the user has limited time, and the question is "does this policy contain anything that would change our decision to proceed, or does it look standard enough that we can move to DPA negotiation and security review?"

## When this skill applies

Apply when the user provides a vendor's privacy policy (or what is presented as one) and asks for a quick assessment. Common triggers:

- Vendor proposed during procurement; quick read needed before deeper review.
- Vendor's published policy used as a baseline for DPA negotiation (the policy describes what the vendor *says* it does; the DPA captures what the vendor *commits* to do).
- Periodic re-review of an existing vendor's updated privacy policy.
- Pre-meeting prep before a vendor security/privacy review call.

Do not apply when:

- **The user wants a full privacy assessment.** This skill is a first pass; full assessments are out of scope. Recommend a comprehensive privacy assessment performed by qualified privacy counsel, especially for high-sensitivity data flows.
- **The user wants DPA review.** Use DPA Checklist Review for that. The privacy policy is the vendor's public representation; the DPA is the contractual commitment. They serve different purposes and warrant different reviews.
- **The user wants to evaluate the vendor's actual security practices.** Privacy policies describe data practices, not security architecture. Security questionnaires, SOC 2 Type II reports, and penetration test summaries are the appropriate inputs for security review.
- **The document is something other than a privacy policy** (cookie policy alone; terms of service; security exhibit; AUP). Privacy policies have a recognizable structure (data collection, use, sharing, retention, rights, contact). If the document doesn't have these elements, it isn't a privacy policy.
- **The user wants assistance drafting a privacy policy.** Out of scope; recommend privacy counsel and a policy template appropriate to the user's jurisdiction and data practices.

## Inputs

The skill requires the document. Optional inputs (`vendor_context`, `applicable_regimes`, `data_to_share`) refine the analysis:

- **`vendor_context`** changes severity calibration. A privacy policy that allows broad data sharing is a red flag for a marketing automation vendor handling customer PII; the same policy may be standard for an analytics tool handling only aggregated metrics. Without `vendor_context`, the skill uses general calibration and notes the assumption.
- **`applicable_regimes`** prioritizes regime-specific elements in the report. With `applicable_regimes: gdpr`, the skill checks for GDPR-required disclosures (Article 13/14 elements, transfer mechanisms, lawful basis); with `ccpa`, the skill checks for CCPA/CPRA-required disclosures (categories, sale/sharing, sensitive PI, rights). Without specification, the skill assesses against general commercial standards and notes regime-specific considerations as flags rather than findings.
- **`data_to_share`** affects red-flag severity. ML training rights on aggregated metrics is different from ML training rights on user PII. SSN handling considerations matter only if SSNs are in scope.

When optional inputs are not provided, the skill uses default assumptions and notes them in the report.

## Workflow

The workflow has three steps. Total elapsed time should be short — this is triage.

### Step 1: Document orientation

Before substantive review:

- Confirm the document is a privacy policy. The recognizable structure: a "what we collect" section, a "how we use it" section, a "who we share with" section, a "your rights" or "choices" section, a contact section. If these elements are absent, the document is something else.
- Note the policy's effective date. Stale policies (over 18 months old without update) warrant a flag — privacy law has been evolving rapidly.
- Note the vendor's stated jurisdiction(s) of operation, if disclosed.
- Note any references to external documents (separate cookie policy, separate AI/ML policy, separate California addendum, separate California "Notice at Collection," GDPR addendum, regional supplement). The skill flags external references but does not fetch them.
- Estimate the policy's length and density. Short policies (under 1,500 words) often have material omissions; very long policies (over 8,000 words) may bury important provisions.

### Step 2: Structured summary

Produce a structured summary covering the standard topics. Use `reference/policy_topics.md` to ensure coverage. For each topic, note: what the policy says, in plain language; specific clause/section references where applicable; whether the policy's treatment is clear, ambiguous, or absent.

The topics are:

1. **What data is collected** — categories, sources (direct from user, automatic via cookies/SDKs, third parties), and whether sensitive categories are included.
2. **Why data is used** — stated purposes; legal basis (for GDPR-applicable contexts); whether secondary uses are disclosed.
3. **Who data is shared with** — categories of recipients (service providers, affiliates, advertisers, partners, government, anyone via "sale" under CCPA), whether the vendor sells/shares per CCPA, sub-processor arrangements.
4. **Cross-border transfers** — whether transfers occur, mechanisms (SCCs, adequacy, BCRs), and recipient countries if disclosed.
5. **Retention** — stated retention periods or methodology.
6. **User rights and how to exercise them** — access, deletion, correction, opt-out (sale/sharing under CCPA; processing under GDPR), portability, objection, automated-decision-making.
7. **Security** — stated commitments (typically high-level; the policy is not a security statement).
8. **Children's data** — whether the service is directed at children; COPPA/GDPR-K compliance disclosures.
9. **Contact and complaints** — privacy contact information; complaint mechanisms; supervisory-authority disclosure for GDPR.
10. **AI / ML use of data** — whether vendor uses customer data for AI/ML training, how, and whether opt-outs exist (the dominant 2025-2026 issue).

### Step 3: Red-flag identification

Walk through the red-flag list in `reference/red_flags.md`. For each red flag found, note:

- What the policy says (with citation).
- Why it's a red flag.
- Severity (Critical / Material / Minor — using the same rubric tier-down as MSA Review for consistency, but calibrated to triage stakes).
- What the user should do (e.g., "negotiate in DPA", "request specific contractual carve-out", "request clarification from vendor", "escalate to privacy counsel").

The red-flag categories include:

- **Data collection breadth** — collecting categories of data unrelated to the service.
- **Use breadth** — broad use rights including secondary uses.
- **Sharing practices** — broad sharing with affiliates, advertisers, partners; vendor categorized as "selling" or "sharing" under CCPA when not expected.
- **AI / ML training rights** — vendor uses customer data for ML training without opt-out.
- **Data retention** — indefinite retention, unclear retention, retention beyond service necessity.
- **Cross-border transfers without mechanism disclosure.**
- **Rights mechanism gaps** — rights enumerated but no clear exercise mechanism, charges for rights requests, or rights subordinated to vendor's discretion.
- **Vague or boilerplate disclosures** — privacy policy is generic and doesn't reflect the actual service.
- **Stale policy** — last updated long ago.
- **Inconsistencies with vendor's marketing materials or DPA** — privacy policy says one thing; vendor's other materials say another.

## Output

Produce the report in markdown with this structure (deliberately short — triage):

```markdown
# Vendor Privacy Policy First Pass: [Vendor / Document name]

**Vendor context:** [user-provided, or "not specified"]
**Applicable regimes considered:** [list, or "general commercial"]
**Data the user expects to share:** [user-provided, or "not specified"]
**Policy effective date:** [date from policy, or "not stated"]

## Bottom line

[Two to three sentences. Headline assessment: clean / standard / has notable concerns / has serious red flags. Recommendation: proceed to DPA / proceed with specific concerns flagged / escalate for deeper review / decline pending substantial vendor changes.]

## Structured summary

[For each of the 10 topics in the workflow's Step 2, a brief subsection. Each subsection: 2-4 sentences plus a citation. Topics where the policy is silent are noted explicitly ("Not addressed.") rather than omitted.]

### Data collected
[Brief description; categories; sources.]

### Use of data
[Brief description; stated purposes; secondary uses if any.]

### Sharing
[Categories of recipients; sale/sharing under CCPA; sub-processors.]

### Cross-border transfers
[Whether transfers occur; mechanisms; recipient countries.]

### Retention
[Periods or methodology.]

### User rights and exercise mechanisms
[Rights enumerated; how to exercise.]

### Security
[Stated commitments.]

### Children's data
[Disclosures, or note the policy doesn't address.]

### Contact and complaints
[Privacy contact; complaint mechanisms.]

### AI / ML use of data
[Whether vendor uses data for ML training; opt-outs.]

## Red flags

[Items requiring user attention. Each with: what the policy says, why it's a flag, severity (Critical / Material / Minor), recommended user action. If no red flags, this section is one sentence: "No red flags identified at the first-pass level."]

## Items the policy doesn't address (gaps)

[Things a comprehensive privacy policy would typically address but this policy doesn't. Distinct from red flags — these are absences rather than problematic provisions. May overlap with regime-specific requirements when `applicable_regimes` is provided.]

## Recommended next steps

[Short bulleted list. Common options: proceed to DPA negotiation; request clarification from vendor on specific items; escalate specific issues to privacy counsel; obtain SOC 2 / security questionnaire; decline pending vendor changes.]

## Out of scope for this first pass

[A short paragraph reminding the user what this skill did NOT do: full privacy assessment, DPA review, security architecture review, jurisdictional enforceability analysis, etc. Direct the user to the appropriate next step for each.]
```

The report should be short. A typical first-pass report runs 1-3 pages. If the report is running long (over 4 pages), the document warrants a more comprehensive review than triage; the report should say so and recommend escalation rather than continuing to expand.

## Edge cases and refusals

- **Document is not a privacy policy.** Stop and tell the user. Common confusion: terms of service (different focus); cookie policy alone (subset of privacy policy); security exhibit (not a privacy policy); AUP (different document); DPA (use DPA Checklist Review).
- **Document is a privacy policy stub** — extremely short, missing core sections. Note the inadequacy as a critical finding ("policy does not contain core sections required to be a meaningful privacy notice"); recommend escalation.
- **Document is a privacy policy in a language the user did not flag.** Note the language and ask the user to confirm before proceeding.
- **Document is dated and the user has indicated the policy may be outdated.** Note the date prominently and flag potential staleness as a finding.
- **Document references many external sub-policies.** The skill cannot fetch external content. Note the references explicitly and recommend the user gather the referenced documents and consider running this skill on each.
- **Document is a vendor's privacy policy for one service when the user is evaluating a different service from the same vendor.** Vendors often have product-specific privacy policies. Verify the policy applies to the service in scope.
- **Vendor uses customer data for AI/ML training based on what the policy says.** Flag explicitly as critical regardless of `vendor_context` — this is the dominant 2025-2026 issue and warrants explicit treatment.

## What this skill does not do

- **Full privacy assessment.** This is triage. A full assessment requires: review of the DPA, security exhibit, sub-processor list, transfer impact assessment, audit reports, and operational practices. None of those are in scope here.
- **Compliance certification.** The skill does not certify that a policy is GDPR-compliant or CCPA-compliant. Compliance certification requires affirmative legal opinion based on full facts; this is not that.
- **DPA negotiation.** The privacy policy is the vendor's public representation; the DPA is the contractual commitment. The DPA review is a separate skill (DPA Checklist Review).
- **Security review.** The privacy policy describes data practices, not security architecture. Security review requires SOC 2 reports, penetration tests, security questionnaires.
- **Comparative analysis with other vendors' policies.** The skill assesses one policy at a time. Multi-vendor comparison is out of scope (deferred enhancement candidate).
- **Detailed jurisdictional analysis.** The skill flags regime-relevance ("this policy may not satisfy GDPR Article 13 disclosure requirements") but does not give jurisdictional opinions ("this policy violates GDPR").

## Reference materials

- `reference/policy_topics.md` — the 10 standard topics covered in the structured summary, with what to look for in each.
- `reference/red_flags.md` — categorized red-flag list with severity calibration guidance.
- `examples/example_clean_policy.md` — worked example: vendor's privacy policy that's clean enough to proceed to DPA.
- `examples/example_red_flags.md` — worked example: vendor's privacy policy with multiple red flags warranting escalation.
