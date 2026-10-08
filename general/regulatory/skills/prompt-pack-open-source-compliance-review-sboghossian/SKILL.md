---
name: prompt-pack-open-source-compliance-review-sboghossian
title: Open Source Compliance Review
description: Use when conducting an open source licence compliance review for a software product or codebase. Identifies open source components, classifies licence types (permissive, weak copyleft, strong copyleft), assesses compatibility with proprietary and other open source licences, flags disclosure and attribution obligations, and recommends remediation. Applicable to companies commercializing software or undergoing M&A IP due diligence.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-open-source-compliance-review
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
---

# Open Source Compliance Review

## When to use this

Use this skill when a company needs to identify and assess its open source software (OSS) obligations before a commercial product launch, M&A transaction, or regulatory audit. Open source licence compliance failures can result in mandatory source code disclosure, loss of IP protection, and litigation risk.

Triggers:
- "We're about to sell our SaaS product — does our use of open source create any disclosure obligations?"
- "The investor wants an OSS compliance review as part of IP due diligence."
- "Our engineering team used GPL libraries — what does that mean for our proprietary code?"
- "Conduct an open source compliance review of our software product."

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Product / codebase description | Scopes the review | Ask user |
| Component inventory (if available) | List of libraries, frameworks, dependencies | Ask user — if unavailable, recommend tooling |
| Distribution method | Distributed as binary / SaaS / embedded in hardware / open source | Determines which licence obligations are triggered |
| Licensing intent for the product | Proprietary / commercial / open source release | Ask user |

## Optional inputs

- Bill of Materials (SBOM) if generated
- Whether the review is for M&A due diligence or internal compliance
- Prior OSS compliance reviews
- Jurisdiction of primary market (affects software patent risk analysis for patent claims in OSS licences)

## Step 1: Component Inventory

If the company does not have an SBOM, recommend using automated tooling before conducting the legal review:
- **FOSS scanning tools**: Black Duck, FOSSA, WhiteSource/Mend, Scancode, OSS Review Toolkit (ORT)
- **Package manager analysis**: review `package.json` (npm), `pom.xml` (Maven), `requirements.txt` (pip), `go.mod`, `Cargo.toml` as applicable
- **Binary analysis**: for compiled code where source is not available

The inventory should capture for each component:
- Component name and version
- Source / repository
- Declared licence (from package metadata)
- Actual licence (from source code headers — may differ from declared licence)
- How it is used: modified / unmodified; statically linked / dynamically linked / SaaS usage / loosely coupled

## Step 2: Licence Classification

Classify each component's licence into one of three risk tiers:

### Tier 1 — Permissive Licences (Low risk)
These licences permit use in proprietary software with minimal obligations (attribution, copyright notice, no warranty disclaimer removal):
- **MIT License**: attribution required; no source disclosure; widely used
- **Apache License 2.0**: attribution required; NOTICE file required; includes patent grant; compatible with most licences
- **BSD 2-Clause / BSD 3-Clause**: attribution required; 3-clause adds no-endorsement provision
- **ISC License**: functionally equivalent to simplified BSD

**Risk**: Low. Attribution requirements must be met (include copyright notices and licence text in documentation or about screen). Apache 2.0 includes a patent grant that terminates if you initiate patent litigation — note this.

### Tier 2 — Weak Copyleft Licences (Medium risk)
These licences permit use in proprietary software but require modifications to the licensed component itself to be released under the same licence:
- **LGPL v2.1 / v3**: modifications to the LGPL library must be released; the proprietary application may use the library if it is dynamically linked; static linking creates stronger copyleft obligations
- **Mozilla Public License 2.0 (MPL-2.0)**: file-level copyleft; modifications to MPL files must be MPL; proprietary code in separate files is not affected
- **Eclipse Public License 2.0 (EPL-2.0)**: similar to MPL but with explicit patent grant

**Risk**: Medium. Dynamic linking generally avoids copyleft contamination of proprietary code under LGPL, but legal analysis of "combined work" is fact-specific. Static linking with LGPL components requires careful analysis.

### Tier 3 — Strong Copyleft Licences (High risk — requires careful analysis)
These licences require that any derivative work or combined work be released under the same open source licence:
- **GPL v2 / v3**: if GPL-licensed code is combined with proprietary code, the combined work may be required to be released under the GPL; GPL v3 adds anti-tivoization and patent provisions
- **AGPL v3 (Affero GPL)**: GPL v3 plus: if the software is used over a network (SaaS), users must be able to obtain the source code; most dangerous licence for SaaS companies
- **EUPL v1.2 (European Union Public Licence)**: copyleft; used by EU government open source; compatible with some but not all other licences

**Risk**: High. Use of GPL or AGPL components in commercial software requires either:
1. Releasing the combined work as GPL/AGPL (open sourcing the product), or
2. Obtaining a commercial licence from the rights holder (dual-licenced open source), or
3. Removing or replacing the GPL/AGPL component

### Tier 4 — Non-Commercial Licences (Prohibit commercial use)
- Creative Commons **NC** variants: prohibit commercial use; not suitable for any commercial product
- **JSON License**: "shall be used for good, not evil" — famously declined by some corporates; legal enforceability disputed
- Various "source available" licences that are not true OSS

## Step 3: Compatibility Analysis

| Combination | Compatible? | Notes |
|---|---|---|
| MIT + Apache 2.0 | Yes | Both permissive |
| MIT + GPL v2 | Only if overall work released as GPL | MIT code can go into a GPL project |
| Apache 2.0 + GPL v2 | Incompatible (FSF view) | Apache 2.0's patent termination clause incompatible with GPL v2 |
| Apache 2.0 + GPL v3 | Compatible | GPL v3 includes Apache-compatible patent provisions |
| LGPL + proprietary (dynamic link) | Generally yes | Legal analysis required |
| AGPL + proprietary SaaS | Generally no | SaaS distribution triggers source disclosure |
| GPL v2 + GPL v3 | Incompatible | Unless "v2 or later" wording permits upgrade |

## Step 4: Obligations Inventory

For each component by licence tier, list the obligations that must be met:

| Component | Licence | Obligation | Status | Action required |
|---|---|---|---|---|
| [Library X] | MIT | Attribution in docs / about screen | Outstanding | Add copyright notice |
| [Library Y] | Apache 2.0 | NOTICE file inclusion | Completed | Verify in build |
| [Library Z] | LGPL v3 | Dynamic linking confirmed; modification source available | Under review | Confirm linkage method |
| [Library W] | GPL v3 | Combined work analysis required | Risk identified | Seek commercial licence or replace |

## Step 5: Remediation Recommendations

| Risk level | Finding | Recommended action |
|---|---|---|
| **Critical** | AGPL component used in SaaS product | Immediately assess whether source disclosure is required; seek commercial licence from maintainer; or replace with permissive alternative |
| **High** | GPL v2/v3 component statically linked with proprietary code | Legal opinion on "combined work"; obtain commercial licence or replace component |
| **Medium** | LGPL component statically linked | Confirm dynamic linking is feasible; if not, obtain LGPL exception or replace |
| **Low** | MIT / Apache 2.0 attribution notices missing | Add copyright and licence notices to product documentation, about screen, or NOTICES file |

## Step 6: Compliance Documentation

Best-practice OSS compliance documentation:
- **SBOM (Software Bill of Materials)**: machine-readable inventory of all components and licences (CycloneDX or SPDX format)
- **NOTICES / THIRD-PARTY LICENSES file**: included in product distribution; lists all OSS components, versions, and licence texts
- **Copyright attribution**: display in product about screen, documentation, or packaging
- **Written Offer**: for GPL v2 / v3 if binaries are distributed, include a written offer to provide source code for 3 years

## M&A due diligence note

For M&A transactions, OSS compliance issues can affect deal value:
- Critical findings (AGPL in SaaS, GPL contamination of proprietary product) are material and must be disclosed or remediated pre-closing
- Include an OSS compliance representation in the SPA / representations and warranties
- Consider requesting an updated SBOM with clean compliance certification as a condition to closing

See [[prompt-pack-ip-due-diligence-checklist]] for the broader IP due diligence framework.

## Common mistakes

- **Not distinguishing SaaS from distribution**: distribution of binaries triggers GPL/LGPL obligations; pure SaaS (no binary distribution to users) does not trigger GPL/LGPL, but does trigger AGPL.
- **Assuming all MIT/BSD licences are identical**: check the specific version and text; there are non-standard variants that add restrictions.
- **Ignoring indirect (transitive) dependencies**: the direct dependency may be MIT but it may pull in a GPL transitive dependency; automated tooling is required to catch all transitive dependencies.
- **Missing patent grant implications**: Apache 2.0 grants a patent licence from contributors; GPL v3 terminates the patent licence if you initiate patent litigation against any contributor. These are material for patent-holding companies.

## Related skills

- [[prompt-pack-ip-due-diligence-checklist]]
- [[prompt-pack-ip-assignment-agreement]]
- [[prompt-pack-patent-license-agreement]]
- [[prompt-pack-nda-strength-check]]
