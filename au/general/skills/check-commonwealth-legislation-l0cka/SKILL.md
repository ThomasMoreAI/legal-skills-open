---
name: check-commonwealth-legislation-l0cka
title: Check Commonwealth Legislation
description: Verify the identity, status, applicable point-in-time version, Register IDs, and currency qualifications of Australian Commonwealth Acts and registered instruments using the Federal Register of Legislation. Use when a user asks whether Commonwealth legislation is current or in force, which compilation applied on a date, whether a citation or supplied provision matches the official text, or for an evidence-linked legislation currency check. Do not use for State or Territory law, Bills, court deadlines, case treatment, or substantive legal advice.
author: l0cka
author_url: https://github.com/l0cka/legal-skills/tree/main/plugins/australian-legal-research/skills/check-commonwealth-legislation
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: au
practice: general
language: en
sources:
- title: Register Method
  path: references/register-method.md
---

# Check Commonwealth Legislation

Use the Federal Register of Legislation as the controlling source. Produce a
provenance record, not a bare assertion that legislation is "current".

Read [references/register-method.md](references/register-method.md) before
performing a check. It defines the official-source rules, edge cases and result
schema.

## Workflow

1. Fix the scope.
   - Accept Commonwealth Acts and registered legislative or notifiable
     instruments.
   - Record the requested date. If none is given, use today's
     `Australia/Sydney` date and state it explicitly.
   - Return `OUTSIDE SCOPE` for State or Territory law, Bills, deadlines, case
     treatment or a request for legal advice. Do not silently substitute a
     secondary source.
2. Resolve identity.
   - Search `legislation.gov.au` and identify the official title page.
   - Match the name, collection, principal/amending character, year/number and
     Title ID. Treat multiple plausible titles as ambiguous.
   - When command execution is available, use the bundled helper:

     ```bash
     python3 <skill-root>/scripts/frl_lookup.py search "Privacy Act 1988"
     python3 <skill-root>/scripts/frl_lookup.py check C2004A03712 --as-at 2024-01-01
     ```

     Resolve `<skill-root>` as the directory containing this `SKILL.md`. The
     helper supplies metadata only; it does not complete the legal check. It
     is optional and read-only, and it makes network requests only to
     `legislation.gov.au`. Without command execution, follow the same steps on
     the official website directly.
3. Identify the point-in-time version.
   - Use the Register's point-in-time result and All versions page.
   - Record the compilation ID, compilation number, start date and end date.
   - Keep the title's current status separate from the selected version's
     status at the requested date.
   - Do not equate an as-made effective date with commencement.
   - Do not infer that every provision commenced because the title status is
     `InForce`.
4. Check currency qualifications.
   - Inspect the title and All versions pages for commenced but unincorporated
     amendments, known future amendments, citation/name changes and status
     history.
   - Inspect Downloads for replacement or rectification history.
   - For an exact provision or historical proposition, inspect the selected
     compilation's text, commencement provisions and endnotes.
   - Call a PDF authorised only after confirming its official authorisation
     stamp. Do not transfer that label to HTML or a modified copy.
5. Report using the required result contract.

## Result contract

Lead with one status:

- `VERIFIED` — one official title and applicable version were identified with
  no unresolved currency flag relevant to the request.
- `VERIFIED WITH QUALIFICATIONS` — identity and version were established, but
  an identified limitation or currency issue requires attention.
- `NOT VERIFIED` — official evidence is missing, inconsistent or insufficient.
- `OUTSIDE SCOPE` — the request is outside this Commonwealth metadata check.

Then provide:

```text
Requested check: <legislation and provision, if any>
Jurisdiction: Commonwealth of Australia
As at: <YYYY-MM-DD>
Official title: <title>
Collection: <Act / legislative instrument / notifiable instrument>
Title ID: <ID>
Current title status: <current status, with commencement caveat if relevant>
Applicable version: <compilation number and Register ID, or not established>
Version status: <status at the requested date>
Version period: <start to end/current>
Currency flags: <none or itemised flags>
Official sources: <title, point-in-time, versions and authorised-PDF links used>
Checked: <date and Australian timezone>
Limitations and review: <what remains unverified and the human-review point>
```

Use a separate evidence table when verifying more than one proposition. Cite
the exact official page supporting each field. Never describe the result as
legal advice or as proof of how a court would interpret or apply the law.

## Example

A completed `VERIFIED WITH QUALIFICATIONS` result. Every value below is
illustrative; take real values only from the official pages inspected during
the check.

```text
VERIFIED WITH QUALIFICATIONS

Requested check: Privacy Act 1988 (Cth) s 13G
Jurisdiction: Commonwealth of Australia
As at: 2024-01-01
Official title: Privacy Act 1988
Collection: Act
Title ID: C2004A03712
Current title status: In force (present status; commencement caveat below)
Applicable version: Compilation No. 97, Register ID C2023C00347
Version status: In force at the requested date
Version period: 2023-10-18 to 2024-05-22
Currency flags: None reported by the Register for this version; check the
  All versions page for amending Acts commencing after 2024-01-01
Official sources: Title page, point-in-time result and All versions page for
  C2004A03712; authorised PDF for the selected compilation
Checked: 2026-08-26, Australia/Sydney
Limitations and review: Interpretation and application of s 13G are for
  lawyer review; case law was not considered
```

The qualification is what separates this from `VERIFIED`: identity and version
are established, but a currency flag relevant to the request must be surfaced
rather than silently dropped.

## Fail closed

Return `NOT VERIFIED` instead of guessing when the Title ID is ambiguous, the
requested date falls outside available compilations, the Register is
unavailable, an amendment has commenced but is not incorporated, or the
relevant commencement/endnote material cannot be checked.
