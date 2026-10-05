---
name: check-nsw-legislation-l0cka
title: Check NSW Legislation
description: Verify the identity, collection, status, applicable point-in-time version, commencement signals, authorisation and currency qualifications of NSW Acts, statutory instruments and environmental planning instruments using the official NSW legislation website. Use when a user asks whether NSW legislation is in force or repealed, which version applied on a date, or whether a citation or supplied provision matches an authorised version. Do not use for Commonwealth or other State or Territory legislation, Bills, Gazettes, as-made-only material, court deadlines, court rules, case treatment or substantive legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/check-nsw-legislation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Nsw Legislation Method
  path: references/nsw-legislation-method.md
---

# Check NSW Legislation

Use the NSW legislation website as the controlling source. Produce a
provenance record, not a bare assertion that legislation is "current".

Read [references/nsw-legislation-method.md](references/nsw-legislation-method.md)
before performing a check. It defines the official-source hierarchy,
authorisation boundary, point-in-time method and URL structure.

## Workflow

1. Fix the scope.
   - Accept Acts, statutory instruments and environmental planning instruments
     in the website's In force and Repealed collections.
   - Record the requested date. If none is given, use today's
     `Australia/Sydney` date and state it explicitly.
   - Return `OUTSIDE SCOPE` for Bills, Gazettes, as-made-only material, another
     jurisdiction, deadlines, court rules, case treatment or legal advice.
   - Treat an environmental planning instrument map or a document adopted by
     reference as an authorisation limitation; do not represent it as
     authorised NSW legislation.
2. Resolve identity and collection.
   - Search `legislation.nsw.gov.au` and identify the official status page.
   - Match the exact title, type, year and number, NSW website identifier, and
     present In force or Repealed collection. Treat multiple plausible titles
     as ambiguous.
   - When command execution is available, use the bundled navigation helper
     after establishing the identifier and collection:

     ```bash
     python3 <skill-root>/scripts/nsw_lookup.py urls act-1987-015 \
       --collection inforce --as-at 2024-01-01
     ```

     Resolve `<skill-root>` as the directory containing this `SKILL.md`. The
     `--collection` value is the title's present collection. For an explicit
     historical date, the helper returns the present title page separately and
     generates the selected-version URLs under the site's `inforce/<date>`
     route. It does not prove that the title operated on that date or establish
     identity, currency, commencement or authorisation. Do not cite a generated
     URL as a source used unless it resolved and was inspected. The helper is
     optional, offline and read-only; it only formats official URLs and
     makes no network requests. Without command execution, follow the same
     steps on the official website directly.
3. Select the point-in-time version.
   - Use the status-page timeline and the Legislative history table of
     versions for the requested date.
   - Record whether the selected text is described as Current or Historical,
     its effective date range, and the date used in the official URL.
   - If an exact-date page cannot be opened, use another accessible official
     page for the same displayed version plus the table of versions to establish
     the effective range. Explain the fallback and do not list the inaccessible
     page as inspected.
   - Keep the title's present In force or Repealed collection separate from
     whether a historical version applied on the requested date.
   - Do not infer that the date embedded in a URL is the version's effective
     start date; confirm the displayed Currency of version statement.
4. Check commencement, currency and authorisation.
   - Read Status Information, including Currency of version, Provisions in
     force, Notes, file-last-modified details and the access timestamp.
   - Inspect Legislative history for original and amending legislation,
     commencement information, the table of versions and provision-level
     history notes relevant to the request.
   - Treat "Does not include amendments by" and partial-commencement notices as
     qualifications. A Bill listed under "See also" is not an amendment.
   - Account for the website's stated update lag after a change (confirm
     the current statement on the site's help pages). Do not give an
     unqualified result when a recent relevant change may fall inside that
     interval.
   - HTML and PDF versions in the In force and Repealed collections, including
     historical versions, are authorised under the website's stated section
     45C framework. Do not transfer that assurance to EPI maps, documents
     adopted by reference or material outside those collections.
   - For an exact provision, inspect the selected version's text and relevant
     commencement and history material; do not rely on title-level metadata.
5. Report using the required result contract.

## Result contract

Lead with one status:

- `VERIFIED` — one official title and applicable version were identified with
  no unresolved qualification relevant to the request.
- `VERIFIED WITH QUALIFICATIONS` — identity and version were established, but
  an identified commencement, currency or authorisation limitation matters.
- `NOT VERIFIED` — official evidence is missing, inconsistent or insufficient.
- `OUTSIDE SCOPE` — the request is outside this NSW metadata and text check.

Then provide:

```text
Requested check: <legislation and provision, if any>
Jurisdiction: New South Wales, Australia
As at: <YYYY-MM-DD>
Official title: <title>
Type: <Act / statutory instrument / environmental planning instrument>
NSW identifier: <act/sl/epi identifier>
Website collection: <In force / Repealed>
Current title status: <present collection status>
Applicable version: <Current/Historical and effective date range>
Provisions in force: <official statement or not established>
Currency flags: <none or itemised flags>
Authorisation: <authorised status and any boundary relevant to the request>
Official sources: <exact status, selected text, history or XML links actually inspected>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

Use a separate evidence table when verifying more than one proposition. Cite
the exact official page supporting each field. Never describe the result as
legal advice or as proof of interpretation, application or legal effect.

## Fail closed

Return `NOT VERIFIED` instead of guessing when the title or collection is
ambiguous, the requested date cannot be tied to a displayed version, the
official site is unavailable, a relevant amendment or commencement issue
cannot be resolved, a recent change may be inside the stated update interval,
or the requested proposition depends on an EPI map or adopted document whose
authorisation cannot be established.
