---
name: draft-copyright-assignment-sboghossian
title: Copyright Assignment Agreement
description: 'Use when a user needs to draft a copyright assignment agreement transferring ownership of authored works — software, creative content, marketing copy, photography, or other copyright-eligible output — from one party to another. Covers identification of works, scope of rights transferred, moral rights handling (jurisdiction-specific), warranty of clean title, and further-assurances mechanics. Most relevant in corporate/IP contexts: contractor-to-client transfers, employee IP cleanup, M&A IP tidying, and publishing deals across MENA, EU, UK, and US.'
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-copyright-assignment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
---

# Copyright Assignment Agreement

## When to use this

Reach for this skill whenever a party needs to formally transfer copyright ownership — not merely license it — to another party. Typical trigger scenarios:

- A company commissioning creative or software work from a freelancer or agency wants to ensure it holds copyright outright (not just a license).
- A founder assigning pre-incorporation code or creative assets to the new company.
- An M&A deal requires IP cleanup as a condition precedent to closing.
- A publishing deal transferring author rights to a publisher.
- An employer wanting belt-and-suspenders assignment beyond the statutory "work for hire" doctrine.

Do **not** use this skill if the parties intend a license only — use [[draft-ip-license]] instead.

## Required inputs

| Input | Why it matters | Sane default |
|-------|----------------|--------------|
| Assignor (current owner) | Must be the actual copyright holder; if jointly authored, all joint owners must sign | — |
| Assignee (recipient) | Exact legal entity including jurisdiction of formation | — |
| Description of works | Specific titles, file names, functional descriptions, creation dates | Schedule A attached |
| Consideration | Must be adequate; nominal ("$1") is common in employment/founder contexts | "good and valuable consideration" recited |
| Effective date | Date rights transfer; may be retroactive | Date of signature |
| Warranty of title | Confirm Assignor holds full ownership with no encumbrances | Included by default |
| Jurisdiction for governing law | Determines moral-rights treatment and registration obligations | Party domicile or IP registry jurisdiction |

## Optional inputs

- **Future works clause** — whether the assignment covers works yet to be created in a defined category or project scope.
- **Retained license-back** — whether Assignor needs a license to continue using the work for its own purposes (common for agencies keeping portfolio rights).
- **Scope limitation** — field of use, territory, or medium (less common in full assignment, but sometimes negotiated for partial assignments).
- **Sublicensing rights** — whether Assignee may sublicense; default is yes for a full assignment.
- **Power of attorney** — authorizing Assignee to execute registration-related documents on Assignor's behalf in each jurisdiction.

## Document structure

1. **Recitals** — identify the parties, describe the background, and state the commercial rationale for the assignment.
2. **Definitions** — "Works" (enumerated in Schedule A), "Intellectual Property Rights", "Moral Rights" (if addressed separately), "Effective Date".
3. **Assignment** — full, irrevocable, worldwide, perpetual transfer of all copyright and related rights, including the right to sue for past infringement.
4. **Future works** (if applicable) — Assignor assigns on creation any works developed in connection with [defined scope] during the period [start] to [end], automatically without further action.
5. **Moral rights** — see Jurisdictional Notes; explicit waiver or consent clause.
6. **Warranty of title** — Assignor warrants: (a) sole owner; (b) no encumbrances, liens, or licenses granted to third parties; (c) no pending or threatened challenges; (d) work does not infringe third-party rights.
7. **Indemnification** — Assignor indemnifies Assignee against warranty breaches.
8. **Further assurances** — Assignor will execute such further documents and do such further acts as Assignee reasonably requests to perfect title in any jurisdiction.
9. **Power of attorney** (irrevocable, coupled with interest) — Assignee as attorney-in-fact to sign registration documents.
10. **Confidentiality** — terms of assignment confidential; disclosure only on legal necessity or investor due diligence.
11. **Governing law + dispute resolution**
12. **Schedule A** — itemized list of works with as much specificity as possible.

## Jurisdictional notes

| Jurisdiction | Moral rights | Registration | Key trap |
|---|---|---|---|
| **France (FR)** | Inalienable (droit moral) — attribution + integrity cannot be transferred or waived; Assignee must credit Assignor unless Assignor expressly waives enforcement. Full waiver language is void under French law. | Optional; deposit with BnF for evidential purposes. | A blanket "moral rights waived" clause is unenforceable — use a consent clause instead. |
| **Germany** | Moral rights are inalienable; only licenses possible under German copyright theory. An assignment in the civil-law sense of transferring authorship is not recognized. Draft as an exclusive license with buyout language if German law governs. | Copyright registered via VG Wort / VG Bild-Kunst for remuneration. | Calling the instrument "assignment" may be legally incorrect under German law. |
| **UK** | Moral rights exist (CDPA 1988) but are waivable by written agreement. Assignment must be in writing and signed by assignor. | No formal registration; deposit at British Library for published works. | Moral rights default to author unless waived. Include waiver. |
| **US** | Moral rights are very limited (VARA for visual art only). Work-for-hire doctrine may mean employer/commissioner is deemed author if criteria met — confirm which doctrine applies before drafting a separate assignment. | Copyright Office registration not required for rights but creates presumption + enables statutory damages. Consider registration within 3 months of publication. | Work-for-hire ambiguity. If it qualifies as WFH, no assignment needed. If not, assignment is required. |
| **UAE (onshore)** | UAE Federal Copyright Law (Federal Law 38/1992, amended) recognizes moral rights but assignment of economic rights is permitted. Arabic version required for court use. | Ministry of Economy registration optional but useful. | Assignment must be in writing; oral transfers ineffective. |
| **KSA** | KSA Copyright Law (Royal Decree M/41 2002) permits assignment of economic rights. Moral rights are inalienable. | SDAIA / SAIP registration for evidential purposes. | Assignment contracts must be in Arabic for enforcement. |
| **Lebanon** | Law No. 75/1999 on Intellectual Property recognizes moral rights as inalienable. Economic rights assignable. | MOE/IP Directorate. | Assignment of software output in commercial context — employment exception may apply if created during employment. |
| **DIFC / ADGM** | English-law style; moral rights waivable. Full common-law assignment available. | No copyright register in DIFC/ADGM specifically; governed by chosen law. | Confirm whether the work is registered IP or relies on unregistered rights. |

## Drafting standards

- **Specificity of works** — a vague description ("all software created for the project") is litigated routinely. Enumerate files, versions, commit hashes, or project names in Schedule A.
- **No placeholders at delivery** — if a default applies (e.g., nominal consideration, current date), state it in the document; do not leave `[INSERT]` gaps.
- **Retroactive assignment** — if the work was already delivered, state explicitly that the assignment is retroactive to the date of creation.
- **Joint authorship** — if multiple authors contributed, every co-author must sign; partial assignment from one co-author conveys only that person's share.
- **License-back** — if Assignor needs a license, draft the license-back in the same document or as an exhibit; a separate email is not reliable.
- **Governing law and lex protectionis** — for patents and trademarks, lex loci protectionis (law of the country where protection is claimed) governs validity; IP assignments are governed by governing-law clause for the contractual relationship but registry perfection follows local law.

## Common mistakes

1. **Moral rights waiver in civil-law jurisdictions** — a blanket waiver clause is void in France, Germany, and many MENA jurisdictions. Use a consent clause or a narrowly framed waiver targeted at specific uses.
2. **Forgetting future works** — in contractor or employment relationships, the assignment often needs to cover works not yet created.
3. **Missing registry filings** — assignment takes effect contractually on signing but may not be enforceable against third parties until recorded at the relevant IP registry (USPTO, EUIPO, KIPO, SAIP, etc.).
4. **Work-for-hire overlap** (US) — if the work qualifies as WFH, a separate assignment is redundant but harmless. If it doesn't qualify, omitting the assignment leaves ownership with the creator. Confirm status before drafting.
5. **No power of attorney** — if Assignor is unavailable post-signing (dissolved company, departed employee), the PoA provision allows Assignee to complete registry filings independently.
6. **Inadequate consideration** — nominal consideration ("$1 and other good and valuable consideration") is adequate contractually in common-law jurisdictions but may attract transfer-pricing or tax scrutiny in some MENA jurisdictions.

## Related skills

- [[draft-ip-assignment]] — broader IP assignment covering patents, trademarks, trade secrets, and designs alongside copyright
- [[draft-consulting-agreement]] — services agreement that should include an IP-assignment clause for deliverables
- [[draft-founders-agreement]] — founders assigning pre-incorporation IP to the company
- [[draft-nda-mutual]] — confidentiality layer often paired with assignment
- [[review-ip-ownership]] — reviewing existing agreements for IP ownership gaps
