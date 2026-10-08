---
name: verify-nsw-judgment-l0cka
title: Verify NSW Judgment
description: Verify that a cited New South Wales court or tribunal decision exists on the official NSW Caselaw website, resolving medium-neutral NSW citations and NSWLR references to the published decision while preserving restriction notations and the Copyright in Judicial Decisions Notice 1995 conditions. Use when the citation is already known to be a NSW court or tribunal citation (route-case-citation sends NSW citations here) and a user asks whether it is genuine, what case a NSW citation refers to, or to check NSW authorities in a document for fabrication. Do not use for other jurisdictions, subsequent treatment, case summaries or legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/verify-nsw-judgment
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: criminal
language: en
---

# Verify NSW Judgment

Use `caselaw.nsw.gov.au` as the controlling source. NSW Caselaw is the
official publisher for the Supreme Court, Court of Appeal, Court of Criminal
Appeal, Land and Environment Court, District Court, Local Court, NCAT and
other NSW courts and tribunals, with coverage from 1999 onward (earlier for
some courts). Produce a provenance record, not a bare assertion that a case
"exists".

Read [../../references/case-law-verification-method.md](../../references/case-law-verification-method.md)
before verifying. It defines the outcome semantics, access rules and
restriction handling.

## Workflow

1. Fix the scope.
   - Accept medium-neutral NSW citations (`NSWSC`, `NSWCA`, `NSWCCA`,
     `NSWDC`, `NSWLC`, `NSWLEC`, `NSWCATAP`, `NSWCATAD` and other NSW
     identifiers), NSWLR reported citations, and NSW case names.
   - Return `OUTSIDE SCOPE` for other jurisdictions, treatment analysis or
     advice. Note that decisions before a court's NSW Caselaw coverage start
     may exist without being published there; that is an `UNVERIFIABLE`
     boundary, not `NOT FOUND`.
2. Resolve the citation at the official publisher.
   - Use the advanced search's Medium Neutral Citation field. The citation
     must include the square brackets, as the form itself states.
   - The search executes only when the request carries the form's full
     query string, including the site's `courts` and `tribunals` identifier
     parameters — a bare `mnc` parameter returns the empty form. Submit the
     search through the site's own form (directly or in a browser) rather
     than a hand-built minimal URL, and read the `Displaying X - Y of Z`
     marker for the result count.
   - Make one targeted lookup per citation; never crawl or bulk-download
     listings.
   - For an NSWLR citation, resolve to the medium-neutral citation through
     the site's search before concluding anything.
3. Confirm identity.
   - Match the case name, citation, court and decision date as published,
     and record the NSW Caselaw decision URL.
   - A direct fetch of a decision page returns the metadata header only —
     citation, case name, dates, before, catchwords and the Restrictions
     field — which is sufficient for existence and identity. The judgment
     body loads in a browser session; quote checks need the rendered page
     or the site's document download, not the bare HTML fetch.
   - Treat a supplied case name that differs materially from the published
     name as a qualification, and say which differs.
4. Respect the publisher's conditions.
   - The Copyright in Judicial Decisions Notice 1995 (NSW) permits
     reproduction conditioned on accuracy and proper context. Reproduce
     nothing inaccurately, and do not republish party names into contexts a
     search engine indexes.
   - Check the decision page for restriction, suppression or
     non-publication notations before quoting anything. Preserve any found
     and treat them as qualifications.
5. Report using the result contract.

## Result contract

Lead with one status: `VERIFIED`, `VERIFIED WITH QUALIFICATIONS`,
`UNVERIFIABLE`, `NOT FOUND` or `OUTSIDE SCOPE`, as defined in the shared
method. `NOT FOUND` means NSW Caselaw was searched by citation and case name
within its coverage period and contains no matching decision — report it as
a fabrication flag for human confirmation, never as an accusation.

```text
Requested check: <citation or case name as supplied>
Jurisdiction: New South Wales, Australia
Citation type: <medium-neutral / reported / case name>
Official case name: <as published, or not established>
Medium-neutral citation: <[YEAR] COURT N, or not established>
Court or tribunal: <as published, or not established>
Decision date: <as published, or not established>
Coverage note: <inside NSW Caselaw coverage / possible pre-coverage decision>
Restrictions: <none observed / notation preserved verbatim>
Official sources: <exact caselaw.nsw.gov.au URLs actually inspected>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

## Fail closed

Return `UNVERIFIABLE`, not `NOT FOUND`, when NSW Caselaw is unreachable, the
search fails, the citation predates the court's coverage, or an NSWLR
citation cannot be resolved to a medium-neutral form. Return `NOT FOUND`
only after both a citation search and a case name search inside the coverage
period returned no match. Never infer existence from an aggregator,
secondary source or model memory.
