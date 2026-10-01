---
name: design-export-control-compliance-program-jeffreytse
title: Design Export Control Compliance Program
description: Use when a company exports goods, software, or technology internationally and needs a compliance program addressing export control classification, restricted-party screening, and licensing requirements under the EAR or ITAR — building automated screening into transaction workflows rather than relying on manual, case-by-case review that can't scale with transaction volume.
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/corporate/skills/design-export-control-compliance-program
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: sanctions
language: en
tags: [law, corporate, export-control-compliance, ear, itar, restricted-party-screening]
---

# Design Export Control Compliance Program

Build an export control compliance program addressing classification, restricted-party screening, and licensing requirements under the EAR or ITAR — with automated screening built into transaction workflows — rather than relying on manual, case-by-case review that can't scale with transaction volume.

## Why This Is Best Practice

**Adopted by:** The Bureau of Industry and Security's Export Administration Regulations compliance guidance and the State Department's International Traffic in Arms Regulations compliance program guidance both specify structured program elements — classification, screening, and licensing determination — as the expected components of an effective export compliance program, and automated restricted-party screening integrated into order and shipping systems is standard practice among companies with meaningful export transaction volume.
**Impact:** Companies relying on manual, case-by-case export compliance review are documented to experience materially higher error rates as transaction volume grows, since manual review doesn't scale — a restricted party or a controlled destination can be missed simply due to the volume of transactions requiring individual manual check, a risk automated screening integrated into transaction workflows specifically addresses by applying consistent screening to every transaction regardless of volume.
**Why best:** Export control violations frequently occur not from willful violation but from an inadequate compliance infrastructure failing to catch a restricted party or controlled item amid routine transaction volume — automated screening integrated directly into order processing and shipping workflows catches this risk consistently and at scale, in a way manual, case-by-case review inherently cannot as transaction volume increases.

Sources: U.S. Department of Commerce, Bureau of Industry and Security, Export Administration Regulations (EAR) compliance program guidance; U.S. Department of State, Directorate of Defense Trade Controls, International Traffic in Arms Regulations (ITAR) compliance program guidance

## Steps

### Step 1: Classify products, software, and technology under applicable export control lists

Classify the company's products, software, and technology under the applicable export control classification system (Export Control Classification Numbers under the EAR, or the U.S. Munitions List under ITAR), since the applicable licensing requirements and restrictions depend entirely on this classification.

### Step 2: Build automated restricted-party screening into transaction workflows

Build automated screening against applicable restricted-party lists (the Bureau of Industry and Security's Entity List and Denied Persons List, the Treasury's Specially Designated Nationals list, and other applicable lists) directly into order processing and shipping workflows, so every transaction is screened consistently regardless of volume, rather than relying on manual review that doesn't scale.

### Step 3: Determine licensing requirements based on classification, destination, and end-use

Determine whether a specific transaction requires an export license based on the item's classification, the destination country, the end user, and the stated end-use, since license requirements vary substantially across these factors and a classification alone doesn't determine the full licensing analysis.

### Step 4: Screen for red flags in end-use and end-user information

Screen transactions for red flags suggesting a prohibited end-use or undisclosed end-user — an unusual shipping route, a buyer with no clear need for the specific technical capability, reluctance to provide standard end-use information — since these red flags are documented indicators of potential diversion risk requiring additional due diligence before proceeding.

### Step 5: Train relevant staff and maintain records supporting compliance decisions

Train sales, shipping, and international operations staff on export control requirements relevant to their specific role, and maintain documented records of classification determinations, screening results, and licensing decisions supporting the company's compliance position if later reviewed by regulators.

## Rules

- Classify products, software, and technology under the applicable export control system before determining licensing requirements — classification is the necessary first step.
- Build automated restricted-party screening into transaction workflows rather than relying on manual, case-by-case review that can't scale with volume.
- Screen for documented red-flag indicators of diversion risk (unusual routing, unclear end-use, reluctance to provide information), not only formal restricted-party list matches.
- Maintain documented records of classification, screening, and licensing decisions to support the company's compliance position.

## Examples

**Automated screening catching a restricted-party match:** A company's automated order-processing screening flags a proposed shipment to an entity that appears on the Bureau of Industry and Security's Entity List — a match the system catches automatically as part of routine transaction processing, rather than depending on an individual employee recognizing the entity name amid high transaction volume.

**Red-flag screening prompting additional due diligence:** A sales team notices a customer's unusual reluctance to specify the actual end-use for a dual-use technology purchase, and the company's documented red-flag protocol requires additional due diligence before the transaction proceeds — potentially preventing a transaction that automated restricted-party list screening alone (which wouldn't catch this specific red flag) would have missed.

## Common Mistakes

- **Relying on manual, case-by-case compliance review rather than automated screening built into transaction workflows** — manual review doesn't scale reliably with transaction volume, increasing the risk of a missed restricted party or controlled destination.
- **Screening only against formal restricted-party lists without also training staff to recognize documented red-flag indicators** — diversion risk often requires catching behavioral red flags that a list-match screening alone won't surface.
- **Failing to classify products and technology accurately before determining licensing requirements** — an inaccurate classification undermines the entire subsequent licensing analysis.
- **Neglecting to maintain documented records of classification and screening decisions** — undocumented compliance decisions are difficult to defend if later reviewed by regulators.

## When NOT to Use

- For a company with no international export activity in controlled goods, software, or technology — apply program rigor proportionate to actual export exposure.
- As a substitute for the company's broader sanctions compliance program — export control and sanctions compliance are related but distinct regulatory regimes, each requiring its own specific program elements (see `design-sanctions-compliance-program`).
- For determining whether a specific historical transaction actually violated export control law — that determination requires case-specific legal analysis of the applicable regulations at the time of the transaction.

> **Legal disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Export control compliance carries significant civil and criminal liability exposure — consult licensed export control counsel before designing or implementing a compliance program.
