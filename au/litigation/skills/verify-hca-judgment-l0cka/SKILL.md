---
name: verify-hca-judgment-l0cka
title: Verify HCA Judgment
description: Verify that a cited High Court of Australia decision exists at the official High Court website, resolving medium-neutral HCA citations, CLR volumes 1-100 and ALJR references to the published judgment and recording provenance. Use when the citation is already known to be a High Court citation (route-case-citation sends HCA citations here) and a user asks whether it is genuine, what case a High Court citation refers to, or to check High Court authorities in a document for fabrication. Do not use for other courts, subsequent treatment, case summaries or legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/verify-hca-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: litigation
language: en
---

# Verify HCA Judgment

Use `hcourt.gov.au` as the controlling source. Produce a provenance record,
not a bare assertion that a case "exists".

The website's coverage (checked 2026-08-26) is four collections, and nothing
else: judgments 1998 to current, Commonwealth Law Reports volumes 1–100
(roughly 1903–1959), unreported judgments 1906–1994 (an incomplete set, per
the Court), and single Justice judgments since January 2024. Judgment
summaries (since December 2002) are not judgments and are not a
verification source.
Reported decisions from roughly 1959 to 1997 — CLR volumes above 100 — are
not published there. A citation in that gap is `UNVERIFIABLE` at the
official publisher, never `NOT FOUND`. Note also that the High Court only
began issuing medium-neutral citations in 1998; an earlier `[YEAR] HCA N`
citation is a retrospective identifier that the official publisher does not
index, so verify such cases by case name and reported citation instead.

Read [../../references/case-law-verification-method.md](../../references/case-law-verification-method.md)
before verifying. It defines the outcome semantics, access rules and
restriction handling.

## Workflow

1. Fix the scope.
   - Accept medium-neutral `[YEAR] HCA N` citations, CLR citations within
     volumes 1–100, ALJR citations, and High Court case names.
   - Return `OUTSIDE SCOPE` for other courts, transcripts (`HCATrans`),
     special-leave dispositions unless published as judgments, treatment
     analysis or advice.
2. Place the citation inside or outside coverage.
   - Determine which collection should hold the decision. If none can —
     most reported decisions from roughly 1959 to 1997 — return
     `UNVERIFIABLE` with the coverage boundary stated and a manual path
     (the Court registry or a library copy of the report series).
3. Resolve the citation at the official publisher.
   - Search the matching collection's keyword search by distinctive case
     name terms, then match the result row's displayed `Citation:` field
     exactly. The keyword index does not match bracketed citation strings,
     so never conclude anything from a citation-string search alone.
   - The 1998–current collection publishes each judgment PDF at a
     deterministic path (`/sites/default/files/eresources/YEAR/HCA/N.pdf`);
     a resolved and opened PDF corroborates the citation, but cite it only
     after it resolved and was inspected.
   - Make one targeted lookup per citation. Do not crawl listings.
4. Confirm identity.
   - Match the case name, year, citation number and decision date as
     published. Record the case name exactly as the Court publishes it.
   - Treat a supplied case name that differs materially from the published
     name as a qualification, and say which differs.
5. Check restrictions before reproducing anything.
   - Look for suppression or non-publication notations and pseudonymised
     parties on the judgment page. Preserve any found.
6. Report using the result contract.

## Result contract

Lead with one status: `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`,
`UNVERIFIABLE`, `NOT FOUND` or `OUTSIDE SCOPE`, as defined in the shared
method. `NOT FOUND` means the High Court's own database was searched by
citation and case name and contains no matching decision — report it as a
fabrication flag for human confirmation, never as an accusation.

```text
Requested check: <citation or case name as supplied>
Jurisdiction: Commonwealth of Australia (High Court)
Citation type: <medium-neutral / reported / case name>
Official case name: <as published, or not established>
Medium-neutral citation: <[YEAR] HCA N, or not established>
Reported citation: <CLR/ALJR reference if verified, or not applicable>
Decision date: <as published, or not established>
Coverage note: <inside a hcourt.gov.au collection / inside the 1959-1997 reported gap>
Restrictions: <none observed / notation preserved verbatim>
Official sources: <exact hcourt.gov.au URLs actually inspected>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

## Fail closed

Return `UNVERIFIABLE`, not `NOT FOUND`, when `hcourt.gov.au` is unreachable,
the search function fails, or the citation falls outside the website's four
collections — including the roughly 1959–1997 reported gap. Return
`NOT FOUND` only when the citation falls inside a covered collection and a
case name search of that collection returned no match. Never cite a search
URL that was not opened, and never infer existence from an aggregator,
secondary source or model memory.
