---
name: review-open-source-license-jeffreytse
title: Review Open Source License
description: Use when evaluating open source software licenses for commercial use, distribution, or modification rights
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/ip/skills/review-open-source-license
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
tags: [law, open-source, licensing, copyleft, permissive, spdx]
---

# Review Open Source License

Evaluate open source software licenses to determine usage rights, obligations, and commercial compatibility.

## Why This Is Best Practice

**Adopted by:** Linux Foundation, CNCF (Cloud Native Computing Foundation), OSI, legal teams at Google, Microsoft, Red Hat
**Impact:** The Linux Foundation's FOSS Compliance study found that OSS license non-compliance is the most common IP risk in software acquisitions; GPL violations have resulted in significant litigation (BusyBox/VMware, MySQL/Progress Software), injunctions, and forced source disclosure.

**Why best:** Open source licenses are not uniformly permissive. Copyleft licenses impose distribution obligations that can require disclosure of proprietary source code when triggered. Understanding the trigger conditions and the compatibility matrix between multiple licenses is essential before incorporating any open source component into a commercial product.

## Steps

1. **Identify the SPDX identifier** — Every OSI-approved license has a standardized SPDX identifier (e.g., MIT, Apache-2.0, GPL-2.0-only, AGPL-3.0-or-later); use the exact SPDX identifier when documenting licenses; avoid ambiguous shorthand.
2. **Classify the license type** — Permissive (attribution only, no distribution obligation): MIT, BSD-2-Clause, BSD-3-Clause, Apache-2.0, ISC. Weak copyleft (file-level): LGPL-2.1, LGPL-3.0, MPL-2.0. Strong copyleft (work-level): GPL-2.0, GPL-3.0. Network copyleft (SaaS-triggered): AGPL-3.0 (copyleft applies even when software is not distributed but used to provide a network service).
3. **Identify the copyleft trigger** — GPL/LGPL: triggered by distribution of modified or combined work as a binary; AGPL: triggered by both distribution AND provision of the software's functionality over a network; determine whether your use case (internal use, SaaS, embedded, redistributed product) triggers the copyleft obligation.
4. **Review the patent grant** — Apache-2.0 includes an explicit patent license grant (contributors grant patent rights to use, make, sell); MIT and BSD do not; GPL-3.0 includes patent grant; GPLv2 does not; Apache-2.0 is preferred over MIT for this reason in patent-risk-sensitive contexts.
5. **Check license compatibility for combined works** — GPL-2.0 and GPL-3.0 are not compatible (cannot combine code under both in a single binary without upgrading to GPL-3.0 or later); Apache-2.0 is compatible with GPL-3.0 but NOT GPL-2.0. Use the FSF license compatibility matrix; incompatible combinations are a license violation.
6. **Assess SaaS/cloud deployment implications** — For internal use (never distributed): most copyleft licenses do not trigger (exception: AGPL). For SaaS (network distribution): AGPL requires source disclosure; evaluate whether replacing AGPL components with permissive alternatives is feasible.
7. **Catalog all dependencies transitively** — Use SBOM (Software Bill of Materials) tooling (SPDX SBOM, CycloneDX, Syft) to identify all direct and transitive dependencies and their licenses; manual review of only direct dependencies misses copyleft obligations from indirect dependencies.
8. **Document obligations and comply** — Permissive licenses: include copyright notice and license text in distributions; GPL: provide access to complete corresponding source code; attribute all open source components in product documentation or legal notices file.

## Rules

- Never include AGPL-licensed components in a commercial SaaS product without either: (a) complying with AGPL source disclosure obligations, or (b) obtaining a commercial license from the copyright holder.
- Always generate an SBOM for production software; manual license review without automated dependency scanning is insufficient for modern dependency trees.
- Do not combine GPL-2.0-only code with Apache-2.0 code in a single binary; they are incompatible.
- If a copyright holder offers both GPL and commercial licensing (dual licensing), obtain the commercial license before distributing a proprietary product.
- Attribution is mandatory for all permissive licenses (MIT, BSD, Apache); failure to include copyright notices is a license breach even for permissive licenses.

## Examples

**License review scenario:** Product uses Redis (BSD-3-Clause → safe, permissive), Elasticsearch (SSPL-1.0 → NOT OSI-approved, commercial use requires license), and a utility library under AGPL-3.0 (triggers network copyleft for SaaS). Action: replace AGPL library with MIT-licensed alternative; negotiate commercial license or use Elastic Cloud for Elasticsearch; document Redis attribution in NOTICE file.

## Common Mistakes

- **Treating "open source" as synonym for "free to use commercially"** — SSPL, CC-NC, and Business Source License are not OSI-approved; they restrict commercial use; always verify OSI approval status.
- **Ignoring transitive dependencies** — A direct dependency under MIT may pull in a transitive dependency under GPL; the copyleft obligation applies regardless of how many layers removed.
- **Modifying LGPL code and statically linking** — Static linking an LGPL library into a proprietary binary may trigger full LGPL copyleft; dynamic linking is the safer option to limit obligations.

---

> **Law disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Consult a licensed attorney before making legal decisions.
