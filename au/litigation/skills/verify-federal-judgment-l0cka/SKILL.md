---
name: verify-federal-judgment-l0cka
title: Verify Federal Judgment
description: Verify that a cited Federal Court of Australia or Federal Circuit and Family Court decision exists at the courts' official publishers, resolving FCA, FCAFC, FedCFamC, FCCA, FamCA and FCR citations, with an explicit browser-guided or manual path where the Federal Court website challenges automated access. Use when the citation is already known to be a Federal Court or FCFCOA citation (route-case-citation sends federal citations here) and a user asks whether it is genuine, what case a federal citation refers to, or to check federal authorities in a document for fabrication. Do not use for the High Court, State courts, subsequent treatment or legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/verify-federal-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: litigation
language: en
---

# Verify Federal Judgment

Two official publishers control this skill. The Federal Circuit and Family
Court publishes its judgments at `fcfcoa.gov.au` and answers direct
requests. The Federal Court publishes through Federal Law Search on
`fedcourt.gov.au`, which challenges automated clients — that path is
human-operated browser only, and this skill never solves or bypasses the
challenge. Produce a provenance record, not a bare assertion that a case
"exists".

Read [../../references/case-law-verification-method.md](../../references/case-law-verification-method.md)
before verifying. It defines the outcome semantics, access rules and
restriction handling.

## Workflow

1. Fix the scope.
   - Accept `FCA`, `FCAFC`, `FedCFamC1A`, `FedCFamC1F`, `FedCFamC2F`,
     `FedCFamC2G` citations, the historical `FCCA`, `FamCA` and `FamCAFC`
     identifiers, FCR reported citations, and federal case names.
   - Return `OUTSIDE SCOPE` for the High Court, State or Territory courts,
     treatment analysis or advice.
2. Choose the publisher path.
   - `FedCFamC…`, `FCCA`, `FamCA`, `FamCAFC` → search `fcfcoa.gov.au`
     directly. One targeted lookup per citation; never crawl listings.
   - `FCA`, `FCAFC`, `FCR` → Federal Law Search on `fedcourt.gov.au`.
     - With a human-operated browser tool available, guide the lookup
       through the judgments search at
       `fedcourt.gov.au/digital-law-library/judgments/search`, entering
       the citation without brackets in the Case Name/MNC field (for
       example `2023 FCA 555`). The results page reports
       `Display results X - Y of Z` with the case name, reported citation
       and decision date. Never automate around the bot challenge; the
       search backend challenges non-browser clients as well.
     - Without a browser, return `UNVERIFIABLE` and give that search page
       URL and the exact search terms for a manual check. State plainly
       that unverifiable is not evidence of fabrication.
3. Confirm identity.
   - Match the case name, citation, court and decision date as published.
   - For an FCR citation, resolve to the medium-neutral citation through
     the court's search before concluding anything.
   - Treat a supplied case name that differs materially from the published
     name as a qualification, and say which differs.
4. Check restrictions before reproducing anything.
   - Family-law decisions are published under statutory anonymisation
     (Family Law Act 1975 (Cth) pt XIVB, s 114Q; formerly s 121 before
     6 May 2024); treat the pseudonym as the official case name and never
     attempt to identify parties.
   - Preserve any suppression or non-publication notation found.
5. Report using the result contract.

## Result contract

Lead with one status: `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`,
`UNVERIFIABLE`, `NOT FOUND` or `OUTSIDE SCOPE`, as defined in the shared
method. `NOT FOUND` means the issuing court's own database was searched by
citation and case name and contains no matching decision — report it as a
fabrication flag for human confirmation, never as an accusation.

```text
Requested check: <citation or case name as supplied>
Jurisdiction: Commonwealth of Australia (federal courts)
Citation type: <medium-neutral / reported / case name>
Official case name: <as published, or not established>
Medium-neutral citation: <[YEAR] COURT N, or not established>
Court: <as published, or not established>
Decision date: <as published, or not established>
Publisher path: <fcfcoa.gov.au direct / Federal Law Search via browser / manual check required>
Restrictions: <none observed / statutory anonymisation / notation preserved verbatim>
Official sources: <exact URLs actually inspected, or the manual search URL supplied>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

## Fail closed

Return `UNVERIFIABLE`, not `NOT FOUND`, when the required publisher cannot
be consulted — including every case where the Federal Court's bot challenge
blocks access and no human-operated browser is available. Return `NOT FOUND`
only after the issuing court's own database was actually searched by
citation and case name with no match. Never solve a bot challenge, never
cite a URL that was not opened, and never infer existence from an
aggregator, secondary source or model memory.
