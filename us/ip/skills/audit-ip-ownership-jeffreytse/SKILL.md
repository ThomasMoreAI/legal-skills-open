---
name: audit-ip-ownership-jeffreytse
title: Audit IP Ownership
description: Use when verifying that a company or individual owns the intellectual property they believe they own
author: jeffreytse
author_url: https://github.com/jeffreytse/grimoire-core/tree/main/skills/law/ip/skills/audit-ip-ownership
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [law, intellectual-property, ownership, assignment, work-for-hire]
---

# Audit IP Ownership

Systematically verify that all intellectual property assets are properly owned and documented.

## Why This Is Best Practice

**Adopted by:** USPTO, ABA IP Law Section; required by VC firms and acquirers in due diligence; mandatory in M&A and financing transactions
**Impact:** NVCA (National Venture Capital Association) reports that IP ownership defects are one of the top three issues that kill or reprice M&A deals; IP ownership problems discovered post-acquisition create indemnification claims and escrow disputes worth millions.

**Why best:** IP ownership is not automatic. Creating IP does not mean owning it — the legal owner depends on who created it, under what employment or contractor relationship, and whether proper assignment agreements were executed. Auditing IP ownership closes the gap between assumed and documented ownership before a transaction surfaces the problem.

## Steps

1. **Inventory all IP assets** — Categorize: (1) Patents and patent applications (utility, design, provisional); (2) Copyrights (software code, documentation, marketing materials, databases); (3) Trademarks (registered and unregistered marks, trade dress); (4) Trade secrets (proprietary algorithms, customer lists, formulas, processes); (5) Domain names and social media handles.
2. **Identify all creators** — List everyone who contributed to creating each IP asset: current employees, former employees, founders (pre-company and post-incorporation), contractors, consultants, and co-developers (other companies).
3. **Apply the work-for-hire test** — Under 17 U.S.C. § 101, copyrights created by employees in the scope of employment are work-for-hire (employer owns). For contractors: work-for-hire applies only to 9 specific categories (including software written as part of a collective work) AND a written agreement must expressly state "work for hire"; absent both, the contractor owns the copyright.
4. **Confirm written IP assignment agreements** — For all non-employee creators: verify a signed IP Assignment Agreement (IPAA) exists, explicitly assigns all IP to the company, includes a present-tense assignment ("hereby assigns," not "will assign"), and was signed before or contemporaneously with the work.
5. **Audit founder IP contributions** — Confirm: (a) any IP created by founders before incorporation has been formally assigned to the company via a Founder IP Assignment Agreement; (b) founders signed a PIIA (Proprietary Information and Inventions Agreement) upon joining; (c) founders' prior employer IP assignment clauses do not cover the company's IP (prior employer analysis).
6. **Review open source usage** — Catalog all open source code incorporated in the company's products; assess license obligations (copyleft licenses — GPL, AGPL — may require source disclosure if distributed); confirm no GPL code is embedded in proprietary products without legal review.
7. **Verify patent chain of title** — For each patent application and issued patent: confirm all inventors are listed (inventorship ≠ ownership — all named inventors must have assigned rights); trace assignment chain from inventors to company in USPTO records.
8. **Document and remediate gaps** — List all IP with documentation defects; execute retroactive assignments where possible (they are less legally robust but better than nothing); flag any gaps that cannot be remediated for disclosure in financings or M&A.

## Rules

- A verbal agreement to assign IP is not enforceable for copyrights or patents; written, signed assignment is mandatory.
- Never assume employment alone transfers IP; the work must be within the scope of employment AND the jurisdiction must recognize work-for-hire for that category of IP.
- Always include a power of attorney clause in IP assignment agreements to allow the company to execute patent applications on behalf of the assignor if they become unavailable.
- Confirm that all contractor statements of work explicitly state that all deliverables are either work-for-hire or are assigned to the company.
- Check whether any open source license requires disclosure of patent claims (GPL v3 includes a patent license; AGPL extends this to network use).

## Examples

**Common gap found in audit:** Early contractor wrote the core algorithm before the company executed a services agreement; the contractor signed an NDA but no IP assignment. Risk: contractor owns the copyright to the core algorithm. Remediation: negotiate a retroactive IP Assignment Agreement; consider paying a one-time settlement fee to secure clear title.

## Common Mistakes

- **Relying on NDA for IP ownership** — An NDA protects confidentiality; it does not transfer IP ownership; a separate assignment agreement is required.
- **Not auditing founder prior employer agreements** — A founder's prior employer IP assignment clause may cover inventions in the new company's field; this cloud on title is a deal-killer in M&A and requires clearance opinion from IP counsel.
- **Assuming contractor work is work-for-hire without a written agreement** — This is the most common IP ownership defect in startups; contractor IP must be explicitly assigned in writing.

---

> **Law disclaimer:** This skill encodes professional best practices for educational purposes. It is not legal advice. Consult a licensed attorney before making legal decisions.
