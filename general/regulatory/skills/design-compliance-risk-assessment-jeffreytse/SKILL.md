---
name: design-compliance-risk-assessment-jeffreytse
title: Design Compliance Risk Assessment
description: Use when an organization needs to identify and prioritize its regulatory and compliance risk exposure on an ongoing basis — scoring the likelihood and impact of specific compliance failures across applicable regulations, rather than relying only on one-off contract reviews or a general risk-management process that isn't specifically structured around regulatory obligations.
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/business/operations/skills/design-compliance-risk-assessment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
tags: [business, operations, compliance-risk, regulatory-risk, iso-37301, governance]
---

# Design Compliance Risk Assessment

Identify and prioritize the organization's regulatory and compliance risk exposure on an ongoing basis — scoring the likelihood and impact of specific compliance failures across each applicable regulation or standard — rather than relying only on one-off contract reviews or a general risk-management process that isn't specifically structured around the organization's actual regulatory obligations.

## Why This Is Best Practice

**Adopted by:** ISO 37301, "Compliance Management Systems — Requirements with Guidance for Use," is the internationally recognized standard for organizational compliance management, requiring certified organizations to maintain an ongoing process for identifying, assessing, and prioritizing compliance obligations and the risk of failing to meet them, distinct from the organization's general enterprise risk management process.
**Impact:** An organization relying only on ad hoc compliance checks — a one-off contract review here, an incident-driven policy update there — lacks a systematic view of its full regulatory exposure and has no consistent basis for prioritizing which compliance obligations most urgently need attention; a dedicated compliance risk assessment specifically fills this gap by treating regulatory obligations as their own risk category requiring dedicated identification and scoring.
**Why best:** A general enterprise risk management process (see `apply-iso-31000-risk-framework`) can miss the specific structure of compliance risk, which is tied to a defined, often changing set of external regulatory obligations rather than internally generated risks — a dedicated compliance risk assessment process specifically tracks applicable regulations, assesses the likelihood and impact of failing to meet each, and prioritizes remediation accordingly, providing a level of regulatory-specific rigor a generic risk process doesn't guarantee.

Sources: ISO 37301:2021, "Compliance Management Systems — Requirements with Guidance for Use," International Organization for Standardization

## Steps

### Step 1: Identify all applicable regulatory and compliance obligations

Identify the full set of regulatory and compliance obligations applicable to the organization — across relevant jurisdictions, industries, and business activities — as the foundation for the assessment, since an incomplete inventory of applicable obligations undermines everything that follows.

### Step 2: Assess the organization's current compliance status against each obligation

For each identified obligation, assess the organization's current compliance status — fully compliant, partially compliant with specific known gaps, or an area of significant uncertainty — through documented review rather than an unverified assumption of compliance.

### Step 3: Score each compliance gap by likelihood and impact of failure

For each identified compliance gap or uncertain area, score the likelihood of an actual compliance failure occurring and the potential impact if it did (financial penalties, operational restrictions, reputational damage) — using this scoring to distinguish gaps that need urgent remediation from those that are lower priority.

### Step 4: Prioritize remediation based on the compliance risk scoring

Prioritize remediation effort based on the likelihood-impact scoring from Step 3, addressing the highest-priority compliance gaps first, rather than addressing compliance issues in whatever order they happen to be raised or discovered.

### Step 5: Monitor for regulatory changes and reassess on an ongoing basis

Monitor for changes in applicable regulations and reassess the organization's compliance risk on an ongoing, regular cadence — a compliance risk assessment accurate at one point in time can become outdated as regulations change or as the organization's business activities evolve into new regulatory territory.

## Rules

- Identify the full set of applicable regulatory obligations before assessing compliance status — an incomplete inventory undermines the rest of the process.
- Assess actual compliance status against each obligation through documented review, not an unverified assumption of compliance.
- Score compliance gaps by both likelihood and impact, using this scoring to prioritize remediation rather than addressing issues in an arbitrary order.
- Monitor for regulatory changes and reassess on an ongoing basis, since both the applicable regulations and the organization's own activities can change over time.

## Examples

**Compliance risk assessment surfacing an under-prioritized gap:** An organization's compliance risk assessment reveals a specific regulatory obligation with a documented partial-compliance gap that carries high potential impact despite not having previously seemed urgent — the assessment's structured scoring surfaces this gap for prioritized remediation before it results in an actual compliance failure.

**Ad hoc compliance handling missing a regulatory change (illustrative failure mode):** A different organization relies only on periodic contract reviews and incident-driven policy updates, without a dedicated ongoing compliance risk assessment process. A regulatory change applicable to the organization's business goes unnoticed for an extended period, resulting in an avoidable compliance failure that a dedicated, ongoing monitoring process would have caught.

## Common Mistakes

- **Starting from an incomplete inventory of applicable regulatory obligations** — this undermines the accuracy of everything the assessment subsequently produces.
- **Assuming compliance status rather than documenting an actual, verified review against each obligation** — an unverified assumption of compliance can hide real gaps until a failure actually occurs.
- **Prioritizing remediation based on whatever issue is most recently raised rather than a consistent likelihood-impact scoring** — this risks under-addressing a high-priority gap in favor of a more recently discussed but lower-priority one.
- **Treating the assessment as a one-time exercise rather than an ongoing, regularly repeated process** — regulatory obligations and the organization's own business activities both change over time, and a stale assessment can miss new or evolved compliance risk.

## When NOT to Use

- For a very small organization with minimal regulatory exposure, where the overhead of a formal ISO 37301-aligned assessment exceeds its practical value — a lighter, less formal compliance review may be proportionate in this case.
- As a substitute for the organization's general enterprise risk management process — compliance risk assessment addresses regulatory risk specifically; broader operational, financial, and strategic risks still need the general process (see `apply-iso-31000-risk-framework`).
- When the organization lacks the internal or external expertise to accurately identify its applicable regulatory obligations — in this case, engaging qualified legal or compliance expertise is a prerequisite to a meaningful assessment.
