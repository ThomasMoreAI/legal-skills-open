---
name: privacy-policy-maltehedderich
title: Privacy Policy and GDPR Transparency
description: Draft, review, or debug EU privacy policies and GDPR transparency notices for SaaS products. Use when mapping lawful basis by processing purpose, documenting data subject rights, defining retention periods, disclosing international transfers (SCCs/DPF), separating cookie/tracking disclosures, clarifying controller vs processor role boundaries, listing subprocessors, or governing policy change communication for European products.
author: maltehedderich
author_url: https://github.com/maltehedderich/master-class-agents/tree/main/skills/privacy-policy
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: de
practice: data-protection
language: en
---

# Privacy Policy and GDPR Transparency

## What This Skill Does

Turn real data practices into clear, defensible, regulator-ready privacy disclosures for European SaaS.

This skill treats a privacy policy as a transparency artifact governed by Articles 12–14 of the GDPR, anchored to a documented record of processing. The controlling rule: describe what the product actually does today, with each purpose tied to a lawful basis, retention logic, recipients, and transfer mechanism that operations can defend.

Use this skill to:

- Draft a new privacy policy or transparency notice grounded in actual processing.
- Review an existing policy against EDPB/ICO/CNIL expectations.
- Map purposes to Article 6 (and Article 9 where relevant) lawful bases.
- Specify retention by data category and purpose with concrete criteria.
- Document international transfers post-Schrems II (adequacy, SCCs, DPF, supplementary measures).
- Operationalize data subject rights handling, including request channels and verification.

This skill is for European privacy policy craft. It is not for cookie banner mechanics (use the cookie-policy skill), full DPA drafting, or final legal advice.

## When to Use

- The request involves drafting, reviewing, or debugging a privacy policy or transparency notice for an EU-relevant product.
- A SaaS product is launching or onboarding regulated customers and needs a policy that survives DPA scrutiny.
- A team needs purposes mapped to lawful bases, with retention and transfers tied to the data flow.
- A product has expanded processing (new vendors, new transfers, new purposes) and the policy is now stale.

Do not use this skill for:

- Cookie banner UX, CMP configuration, or ePrivacy mechanics — use the cookie-policy skill.
- Terms of service or commercial contract drafting — use the terms-of-service skill.
- Generating final legal advice or representing as legal counsel.

## Inputs To Gather

Ask for whatever is missing before drafting or reviewing.

- `goal` — `draft`, `review`, `debug`, or `update`.
- `product_context` — B2B vs B2C, regulated sector, audience scope (EEA, UK, global).
- `data_flows` — purpose-driven inventory: purpose, data categories, lawful basis, recipients, transfers, retention.
- `role_boundaries` — controller vs processor activities, joint-controller risks.
- `transfer_details` — destination regions/countries, mechanism (adequacy, SCCs, DPF), supplementary measures.
- `subprocessors` — list and update mechanism.
- `rights_handling` — request channels, verification logic, internal SLAs, response templates.
- `existing_policy` — exact current text when reviewing.

If the request is to review or update, ask for the current policy and the changes since it was last published. If net-new, ask whether the user has a documented record of processing before drafting.

## Non-Negotiable Constraints

Treat these as defaults unless the user explicitly narrows scope.

1. The policy describes facts. If the operation cannot defend the claim, do not draft it.
2. Each processing purpose is tied to a lawful basis (Article 6 and Article 9 where applicable), with associated data categories, recipients, retention, and transfers.
3. Plain-language layered structure. Lead with a user-readable summary; follow with the precise section detail legal and procurement reviewers need.
4. Transfers are first-class disclosures. Name the destination regions, the mechanism, and the safeguards in concrete terms.
5. Retention is testable. Use concrete periods or explicit criteria by data category and purpose. "As long as necessary" without criteria is not acceptable.
6. Rights are operational. Provide practical request channels, verification, and realistic timelines aligned with GDPR.
7. Keep GDPR transparency separate from cookie/ePrivacy mechanics.
8. Version the policy. Communicate material changes. Maintain change history.

## Procedure

Follow the steps in order. Do not skip the data-flow modeling step.

### Step 1 — Establish the job and the audience

Determine:

- whether the task is draft, review, debug, or update.
- the product audience (consumer, business, both) and the regulatory scope (GDPR, UK GDPR, member-state add-ons).
- the deliverable shape (full policy, summary layer, specific section, redline).

Default to the strictest realistic EU audience unless the user specifies otherwise.

### Step 2 — Model the data flows

Build or validate a purpose-driven matrix:

- Purpose (login, billing, support, analytics, model training, marketing, etc.).
- Data categories per purpose.
- Lawful basis under Article 6 (and Article 9 where relevant).
- Recipients (internal teams, vendors, subprocessors, public).
- Transfers per purpose (region, country, mechanism, safeguards).
- Retention period or criteria.
- Source of the data (subject, third party, automated capture).

If the matrix is missing, stop and request it. Do not draft against unknown processing.

### Step 3 — Classify role boundaries

Distinguish:

- Controller activities (the company decides purposes and means).
- Processor activities (the company processes on a customer's instruction).
- Joint-controller scenarios (shared decisions over purposes/means).

Make sure the policy's role claim matches commercial contracts and the actual operations. Misalignment here is a frequent regulator finding.

### Step 4 — Draft the layered structure

Produce the policy in two layers:

- Executive summary for users in plain language.
- Section-level detail for legal and procurement review.

Structure sections so each can be cited independently: who you are, what you process, why, how long, who receives it, transfers, rights, complaints, changes.

### Step 5 — Make retention and transfers concrete

For retention, use periods or explicit criteria per data category and per purpose. For transfers, name the destination, the mechanism, the safeguards, and any supplementary measures. Avoid one-line transfer boilerplate.

### Step 6 — Make rights operational

Specify, for each right:

- The request channel (email, in-product, DPO contact).
- Verification logic that does not over-collect data.
- Realistic response timelines (one-month default, extension rules).
- How fulfillment is logged.

Include the right to lodge a complaint with a supervisory authority and the relevant authority for the user's jurisdiction.

### Step 7 — Stress-test for regulator questions

For each section, ask whether a DPA could plausibly say "show me where this happens in practice." If the claim is not auditable against the record of processing, vendor inventory, or system behavior, fix the claim or fix the operation.

### Step 8 — Wire versioning and change governance

Specify:

- Policy version and effective date.
- How material changes are communicated.
- Where users can find prior versions.
- The internal trigger for policy review (new vendors, new purposes, new regions, regulatory changes).

### Step 9 — Flag legal-review boundaries

Identify:

- Jurisdiction-sensitive interpretations (member-state add-ons).
- Sector-specific obligations (children, health, financial).
- Anything that requires qualified DPO or external counsel sign-off before publication.

## Branching Logic

- **Net-new SaaS.** Begin with the data-flow matrix; refuse to draft policy text against unknown processing. Default to layered structure with a strong summary.
- **Reviewing an existing policy.** Lead with gaps and risks: undisclosed vendors, vague retention, missing transfer mechanism, unclear lawful basis, unclear rights mechanics.
- **Heavy controller-processor blend (B2B SaaS).** Separate the controller-facing notice from the processor disclosures that belong in commercial contracts and the DPA. Do not collapse them.
- **AI training or model improvement processing.** Treat training data as its own purpose with its own lawful basis, retention, and opt-out mechanics. Do not bury it in "service improvement."
- **Substantial new vendor or new region.** Treat as a material change: update the policy, log the version, and define communication.
- **User base spans EEA and non-EEA.** Default the policy to GDPR-compliant baseline; identify any region-specific overlays needed (UK GDPR, Swiss FADP, etc.).

## Output Format

Match the deliverable to the task.

For `draft`:

1. Layered policy with summary plus section-level detail.
2. Data-flow matrix in a usable table format.
3. Concrete retention and transfer language.
4. Operational rights section.
5. Versioning and change-governance notes.
6. "Fact Checks Required" list.
7. "Legal Review Required" note.

For `review` or `debug`:

1. Risk and gap summary at the top, ordered by severity.
2. Findings grouped by transparency, lawful basis, retention, transfers, rights, role boundaries, and change governance.
3. Concrete revisions or replacement text for high-risk sections.
4. "Fact Checks Required" and "Legal Review Required" lists.

For `update`:

1. Redline of the changed sections.
2. New version metadata and a short user-facing change summary.
3. Anything that requires fresh legal review.

## Quality Checks

The work is ready only when all of the following are true:

1. Each purpose maps to a lawful basis with associated data, recipients, retention, and transfers.
2. Retention is concrete (period or explicit criteria), not "as long as necessary."
3. Transfers name the destination, the mechanism, and the safeguards.
4. Role boundaries match the commercial reality and the DPA.
5. Rights sections include actual mechanics and timelines.
6. Cookie/ePrivacy disclosures are separated from GDPR transparency.
7. Version and change-governance language is present and operable.
8. Member-state-sensitive points are flagged for qualified legal review.

## Failure Modes To Avoid

- Drafting policy text against an unknown or stale data-flow matrix.
- Vague catch-all language ("may," "including but not limited to," unnamed "partners") when concrete disclosures are possible.
- Collapsing GDPR transparency and ePrivacy/cookie disclosures into one section.
- Claiming retention, rights handling, or transfer safeguards that are not operationally implemented.
- Treating AI training as a vague "service improvement" purpose without its own basis.
- Outputting final legal advice or claiming to act as legal counsel.

## Default Stance

Be specific, plain, and traceable. The boring policy that matches operations beats the impressive one that does not. Use concrete tables and matrices over abstract prose. When member-state interpretations diverge, default to the stricter realistic EU bar and flag jurisdiction-sensitive points for legal review.
