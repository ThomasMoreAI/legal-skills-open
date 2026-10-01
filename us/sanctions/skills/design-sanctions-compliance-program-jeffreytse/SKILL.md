---
name: design-sanctions-compliance-program-jeffreytse
title: Design Sanctions Compliance Program
description: Use when a company doing business internationally needs a sanctions compliance program addressing OFAC and equivalent restrictions — building the program around the five components OFAC has explicitly defined as essential, including automated screening and periodic testing, rather than an ad hoc process without OFAC's specific structural expectations built in.
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/corporate/skills/design-sanctions-compliance-program
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: sanctions
language: en
tags: [law, corporate, sanctions-compliance, ofac, restricted-party-screening, regulatory-compliance]
---

# Design Sanctions Compliance Program

Build a sanctions compliance program around the five components OFAC has explicitly defined as essential — management commitment, risk assessment, internal controls, testing/auditing, and training — rather than an ad hoc process without OFAC's specific structural expectations built in.

## Why This Is Best Practice

**Adopted by:** OFAC's "Framework for OFAC Compliance Commitments" (2019) explicitly defines five components of an effective sanctions compliance program and states that OFAC will consider whether an organization had an effective program in place when determining the appropriate enforcement response to an apparent violation — making this specific five-component structure the reference standard companies use when building sanctions compliance programs.
**Impact:** OFAC's own enforcement guidelines document that the presence (or absence) of these specific program elements is an explicit factor in determining penalty severity for violations — companies demonstrating a genuinely operating program built around OFAC's own defined framework receive documented mitigation credit compared to companies without one, even when a violation still occurred.
**Why best:** OFAC has explicitly told regulated entities what it expects an effective program to contain — building a program around exactly these five stated components (rather than an independently designed structure that might miss elements OFAC specifically evaluates) directly aligns the program with the actual standard the regulator applies when assessing program effectiveness and determining enforcement outcomes.

Sources: U.S. Department of the Treasury, Office of Foreign Assets Control (OFAC), "A Framework for OFAC Compliance Commitments" (May 2019)

## Steps

### Step 1: Secure senior management commitment to the program

Secure and document explicit senior management commitment to the sanctions compliance program — adequate resourcing, clear designation of a compliance officer with sufficient authority, and visible leadership support — since OFAC's framework explicitly identifies management commitment as the foundational first component of an effective program.

### Step 2: Conduct a risk assessment across customers, products, and geographies

Conduct a risk assessment identifying the company's specific sanctions risk exposure — which customers, products, transaction types, and geographies carry the highest risk of touching sanctioned parties, countries, or activities — as the basis for calibrating the program's controls to actual risk.

### Step 3: Implement internal controls including automated restricted-party screening

Implement internal controls including automated screening of customers, counterparties, and transactions against OFAC's Specially Designated Nationals list and other applicable sanctions lists, built into transaction workflows so screening applies consistently at the volume the business actually operates at.

### Step 4: Conduct periodic independent testing and auditing of the program

Conduct periodic independent testing and auditing of the compliance program's actual operation — not merely its written existence — verifying that screening controls are functioning as designed and that risk assessments remain current as the business evolves, since OFAC's framework specifically identifies testing/auditing as a distinct required component beyond simply having controls in place.

### Step 5: Provide sanctions-specific training calibrated to role-based risk exposure

Provide sanctions compliance training calibrated to each role's actual risk exposure — employees in customer-facing, international sales, or trade finance roles require deeper, more specific training than employees with no exposure to potentially sanctioned counterparties or transactions.

## Rules

- Build the program around OFAC's explicitly defined five components (management commitment, risk assessment, internal controls, testing/auditing, training) rather than an independently designed structure.
- Base internal controls on a genuine, documented risk assessment of the company's specific customer, product, and geographic exposure.
- Implement automated screening built into transaction workflows, not manual review that can't scale with volume.
- Conduct periodic independent testing of the program's actual operation, distinct from simply having controls documented on paper.

## Examples

**Program alignment with OFAC's framework supporting mitigation credit:** A company subject to an OFAC investigation is able to demonstrate all five of OFAC's explicitly defined program components were genuinely operating — documented management commitment, a current risk assessment, automated screening controls, recent independent testing, and role-calibrated training. Consistent with OFAC's stated enforcement approach, this demonstrated program is a documented mitigating factor in the resulting enforcement outcome.

**Independent testing catching a control gap:** A company's periodic independent audit of its sanctions screening system reveals that a recent system migration inadvertently excluded a subset of transactions from automated screening — a gap the testing/auditing component specifically caught before it resulted in an actual violation, illustrating why this component is distinct from simply having screening controls in place.

## Common Mistakes

- **Building a sanctions compliance program without reference to OFAC's explicitly stated five-component framework** — this risks missing elements OFAC specifically evaluates when assessing program effectiveness.
- **Implementing screening controls without periodic independent testing to verify they're actually functioning as designed** — controls that exist on paper can fail in practice (e.g., due to a system change) without ongoing testing to catch this.
- **Providing generic compliance training with no sanctions-specific content calibrated to actual role-based risk** — employees with genuine transaction-level sanctions exposure need training specific to their actual risk, not a generic ethics overview.
- **Failing to secure and document genuine senior management commitment** — OFAC's framework specifically identifies this as foundational; a program lacking visible leadership support and adequate resourcing tends to be less effective in practice.

## When NOT to Use

- For a company with no international transactions, customers, or counterparties carrying any plausible sanctions exposure — apply program rigor proportionate to actual sanctions risk.
- As a substitute for the company's export control compliance program — sanctions and export control are related but distinct regulatory regimes, each requiring its own program elements (see `design-export-control-compliance-program`).
- For determining whether a specific historical transaction actually violated applicable sanctions — that determination requires case-specific legal analysis of the transaction and the sanctions in effect at the time.

> **Legal disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Sanctions compliance carries significant civil and criminal liability exposure, including strict-liability elements under some sanctions programs — consult licensed sanctions counsel before designing or implementing a compliance program.
