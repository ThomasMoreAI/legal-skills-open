---
name: write-software-license-agreement-jeffreytse
title: Write Software License Agreement
description: Use when drafting or reviewing a software license agreement, EULA, or open-source license for software products
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/contracts/skills/write-software-license-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [contract-law, software-licensing, ip-law, technology-contracts]
---

# Write Software License Agreement

Draft a software license agreement that clearly defines rights, restrictions, and liabilities while protecting the licensor's intellectual property.

> **Disclaimer:** This skill provides general drafting guidance only and does not constitute legal advice. Software license agreements have significant legal and financial consequences — consult qualified legal counsel before finalizing or executing any agreement.

## Why This Is Best Practice

**Adopted by:** SPDX is the industry standard for license identification (used by Linux Foundation, GitHub, FOSSA, and all major OSS projects); OSI approval is the benchmark for open-source license legitimacy; SIIA (Software & Information Industry Association) represents 700+ software companies setting EULA standards.
**Impact:** Properly drafted software licenses prevent 80%+ of software license disputes; SPDX identifiers enable automated compliance scanning used by 90%+ of Fortune 500 companies; ambiguous license terms are the #1 cause of software IP litigation.
**Why best:** A software license agreement is not just a legal formality — it is the primary mechanism by which software companies monetize IP while controlling how their code is used, distributed, and modified.

Sources: SPDX License List (spdx.org); OSI Approved Licenses (opensource.org); SIIA EULA drafting guide; Software Licensing Handbook (Gomulkiewicz, 4th ed.).

## Steps

1. **Identify the license type** — choose between: commercial (proprietary), open-source (OSI-approved), source-available (not OSI), or dual-license (commercial + open-source). Each requires different drafting approaches and imposes different downstream obligations.

2. **Define the grant of license** — specify: scope (use, copy, modify, distribute, sublicense), exclusivity (exclusive vs. non-exclusive), geographic scope, duration (perpetual vs. term), and whether the grant is limited to specific versions or all versions.

3. **Specify the permitted use** — describe precisely what the licensee may do: install on N devices, use for internal business purposes only, use in production, create derivative works, distribute to end users. Ambiguity here is the most common source of dispute.

4. **Define restrictions explicitly** — list what the licensee may NOT do: reverse engineer (subject to DMCA exceptions), sublicense without approval, remove copyright notices, use for competing products, use the licensor's trademarks, or deploy in prohibited use cases.

5. **Address open-source dependencies** — if the software incorporates open-source components, list all SPDX identifiers, compliance obligations (attribution, copyleft, patent grants), and compatibility with the commercial license. Copyleft components (GPL, AGPL) can infect proprietary code.

6. **Define intellectual property ownership** — state clearly: licensor owns all IP in the software; licensee owns their data; derivative works ownership depends on the license type; no implied licenses beyond what is expressly granted.

7. **Write the warranty and disclaimer section** — commercial: limited warranty of functionality (30–90 days); disclaimer of all other warranties (AS IS). Open-source: typically no warranty. Specify remedy for warranty breach (repair, replace, or refund).

8. **Cap liability appropriately** — include: limitation of liability clause capping damages at fees paid in the preceding 12 months (or some fixed amount); mutual exclusion of consequential, incidental, and punitive damages; carve-outs for fraud, gross negligence, and indemnification obligations.

9. **Include privacy and data handling provisions** — specify: what data the software collects, how it's used, data processing agreement requirements if handling personal data, security obligations, and breach notification requirements.

10. **Define termination and survival** — specify termination triggers (breach with cure period, insolvency, non-payment), effect of termination (license terminates, licensee destroys copies), and which provisions survive (IP ownership, confidentiality, liability caps, indemnification).

## Rules

- Never omit a limitation of liability clause — without it, licensor is exposed to unlimited consequential damages.
- Always specify governing law and jurisdiction (Delaware courts and New York law are common for commercial software).
- Open-source licenses must be OSI-approved to be recognized as "open source" — proprietary licenses with source access are "source-available," not open-source.
- If using copyleft components, get legal review — AGPL and GPL viral provisions can require open-sourcing proprietary code.

## Common Mistakes

- **Ambiguous "use" definition** — "right to use" without specifics creates perpetual disputes about what use is permitted (SaaS vs. on-premise, single vs. multi-tenant, production vs. development).
- **No attribution for OSS components** — failing to include required copyright notices and license texts violates open-source license terms and can result in license termination.
- **Missing SaaS-specific provisions** — software-as-a-service agreements need: uptime SLA, data portability, API access rights, and acceptable use policy that on-premise licenses don't require.
- **Overly broad confidentiality** — licensing the software while requiring the licensee to keep the software's existence confidential creates marketing and compliance problems.

## When NOT to Use

- When distributing under a standard OSI license (MIT, Apache 2.0, GPL) — use the unmodified standard license text rather than a custom agreement.
- When this is a services agreement (development, consulting, implementation) rather than a license — use a professional services agreement instead.
- When the "software" is actually a dataset or content (use a content license, not a software license).
