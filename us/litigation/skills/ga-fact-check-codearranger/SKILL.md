---
name: ga-fact-check-codearranger
title: Fact-Check Georgia Court Filings
description: 'Use to verify the citations in a Georgia court filing before it is filed. Triggers include "check my Georgia citations", "verify this O.C.G.A. cite", "is this Georgia case real", "fact-check my brief", "Bluebook Georgia citation format", "check the Ga. App. parallel cite", "is this O.C.G.A. section still good law", "audit the authorities in my Georgia motion". Runs four passes: (1) citation verification against canonical Georgia sources; (2) internal consistency within a single document (dates, dollar amounts, defined terms); (3) packet consistency across motion + affidavit + proposed order + certificate of service; (4) sworn-versus-argued consistency between affidavit assertions and motion arguments.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/ga-court-docs/skills/ga-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Georgia Court Filings

> **NOT LEGAL ADVICE.** Fact-checking detects citation and
> consistency errors but does not assess legal sufficiency. Verify
> substantive law independently before filing.

Use this skill before any Georgia court filing leaves the desk. It is
the deeper evidentiary-citation pass; it runs four passes.

## Pass 1 — Citation verification

For every rule, statute, regulation, and case citation in the
document, verify four things: (a) the authority **exists** and is
cited accurately; (b) it is **still good law** (not repealed,
superseded, overruled, or distinguished); (c) the **pinpoint** is
correct; and (d) the cited text actually says what the brief claims.

### Georgia citation conventions

Georgia follows its own appellate citation conventions (Georgia
Supreme Court Rule 22; Court of Appeals Rule 24). Georgia is **not**
a public-domain / neutral-citation jurisdiction — there is no
`[YEAR] GA [###]` vendor-neutral cite. Cite the **official reporters**
first, with the regional reporter as a parallel cite second:

- **Supreme Court of Georgia**: official **Georgia Reports** (`Ga.`)
  first, then **South Eastern Reporter** (`S.E.2d`) parallel second.
- **Court of Appeals of Georgia**: official **Georgia Appeals
  Reports** (`Ga. App.`) first, then `S.E.2d` parallel second.
- **Order of a full cite**:
  `Name, Vol. Ga. Page, Vol. S.E.2d Page (year).`
- **With a pincite** (point to the official-reporter page first, then
  the parallel page):
  `261 Ga. 491, 493, 405 S.E.2d 474, 476 (1991).`
- **Not-yet-reported opinions** (no Ga./Ga. App. volume yet): cite by
  case name + docket/case number + the decision date, e.g.
  `Name, No. S21A0001 (Ga. Mar. 1, 2021)`.
- **Statutes**: `O.C.G.A. § 9-11-56` (always the `§`; the official
  code is the Official Code of Georgia Annotated).
- **Court rules**: Uniform Superior Court Rules (`USCR`), Uniform
  State Court Rules, Uniform Magistrate Court Rules — cite by rule
  number, no `§`.
- **Federal statutes**: `15 U.S.C. § 1692g`.

Common errors to flag:

- Dropping the official `Ga.` / `Ga. App.` reporter and citing only
  the `S.E.2d` parallel — Georgia practice leads with the official
  reporter.
- Confusing the courts: `Ga.` is the Supreme Court, `Ga. App.` is the
  Court of Appeals. A case in `Ga. App.` cited as `Ga.` (or vice
  versa) is a real red flag.
- Inventing a neutral cite (`[YEAR] GA [###]`) — Georgia has none.
- Missing the `§` on an O.C.G.A. citation, or adding a `§` to a USCR
  rule citation (rules take no `§`).
- A pincite that points to the parallel `S.E.2d` page only, with no
  official-reporter pincite.

### Where to verify

The official O.C.G.A. text is published by LexisNexis and is
**paywalled/copyrighted** — do not rely on scraped "official" text.
Use these open verification sources instead:

- **O.C.G.A. sections (current)**: `https://codes.findlaw.com/ga/`
  (codes.findlaw.com/ga) — good for confirming a section exists and
  reading current statutory text.
- **Case law**: **CourtListener** — court IDs `ga` (Supreme Court of
  Georgia) and `gactapp` (Court of Appeals of Georgia). Confirms the
  case exists, the reporter volume/page, and the parties.
- **Case pages**: Justia case pages corroborate parties and
  citations, but **Justia 403s automated fetches** — expect to open
  it manually rather than fetch it programmatically.

For live verification, prefer the bundled **CourtListener** and
**Legal Data Hunter** MCP servers (shipped via the shared federal
dependency). They can confirm a case exists, surface the reporter
citation, and check subsequent-history / good-law status without
scraping paywalled or bot-gated sites.

### Known-good Georgia anchors

These citations are verified and may be relied on as anchors. If a
draft cites a Georgia proposition, prefer anchoring it to one of
these where it fits, rather than to an unverified cite:

- **Summary judgment** —
  *Lau's Corp., Inc. v. Haskins*, 261 Ga. 491, 405 S.E.2d 474 (1991).
  Celotex-style standard under O.C.G.A. § 9-11-56; movant may point to
  the absence of evidence.
- **Equitable distribution of marital property** —
  *Stokes v. Stokes*, 246 Ga. 765, 273 S.E.2d 169 (1980). Georgia is
  an equitable-distribution (not community-property) state.
- **Credit card account = written contract** —
  *Hill v. American Express*, 289 Ga. App. 576, 657 S.E.2d 547 (2008).
- **Debt-buyer standing / unbroken assignment chain** —
  *Nyankojo v. North Star Capital Acquisition*, 298 Ga. App. 6,
  679 S.E.2d 57 (2009). Go-to for attacking debt-buyer standing.
- **Debt-buyer account-stated / business-records foundation** —
  *Wirth v. CACH, LLC*, 300 Ga. App. 488 (2009); *Rutledge v. Gemini
  Capital Group, LLC*, 327 Ga. App. 454 (2014).
- **Open default — "proper case" prong** —
  *Bowen v. Savoy*, 308 Ga. 204 (2020) (O.C.G.A. § 9-11-55).

> **Re-verify reporter pincites.** Some reporter pin-cites in
> secondary sources have been flagged for re-verification (notably
> the parallel `S.E.2d` cites associated with the *Hill* /
> American Express line). Before filing, re-verify every reporter
> pincite — especially the parallel `S.E.2d` page — against an
> authenticated database (CourtListener or a paid reporter service),
> not against a secondary summary.

### Red flags — hallucinated / AI-generated citations

Treat any of these as a stop-and-verify signal:

- **A case that does not exist.** No hit on CourtListener (`ga` /
  `gactapp`) for the party names + reporter cite. AI tools fabricate
  plausible-looking Georgia cites; assume nothing is real until the
  reporter volume/page resolves to the named parties.
- **Wrong reporter for the court.** A Supreme Court holding cited to
  `Ga. App.`, or a Court of Appeals decision cited to `Ga.` — the
  court and the official reporter must match.
- **Mismatched parallel cite.** The `Ga.`/`Ga. App.` cite and the
  `S.E.2d` cite resolve to different cases or different years.
- **Repealed / superseded statute sections**:
  - The pre-2016 garnishment provisions at **O.C.G.A. §§ 18-4-110
    through 18-4-118 are REPEALED** (the garnishment article was
    rewritten effective 2016) — a cite into that old numbering is a
    dead section.
  - The **pre-2013 Georgia evidence numbering (old Title 24) is
    superseded** by the new Evidence Code (e.g., business records
    moved from former § 24-3-14 to § 24-8-803(6)). Flag any cite to
    the old Title 24 numbering.
- **Invented neutral cite.** Any `[YEAR] GA [###]` style cite is
  fabricated — Georgia has no neutral citation.

## Pass 2 — Internal consistency

Within a single document, verify:

- **Dates**: every date is consistent across all its appearances
  (date of service, date of contract, date of last payment, etc.).
- **Dollar amounts**: every amount is consistent and the totals add
  up (principal + interest + fees + costs = total demanded).
- **Defined terms**: a term defined with `(the "Account")` is used
  consistently throughout — no slipping into "the loan" or "the debt"
  once defined.
- **Party names**: each party named consistently (no switching among
  "Plaintiff", "Plaintiff Smith", and "Smith").
- **Cross-references**: every "see paragraph X" or "see Exhibit Y"
  resolves to something that exists at the cited location.
- **Numbered paragraphs**: sequential, with no gaps or duplicates.

## Pass 3 — Packet consistency

Across the multi-document filing packet (motion + affidavit + proposed
order + certificate of service):

- **Caption identical** in every document: court name, county, case
  number, and party names must match exactly.
- **Document title** matches in the certificate of service and the
  proposed order's title bar.
- **Dates** align: the certificate of service date matches the
  signature date on the motion; the affidavit's "sworn to" date
  aligns with when it was executed before the notary.
- **Relief sought** matches: the motion's prayer ("WHEREFORE,
  [movant] respectfully requests ____") must mirror the proposed
  order's ordering language ("IT IS HEREBY ORDERED that ____").
- **Exhibits** referenced in the motion are listed in the affidavit
  and physically attached.
- **Filing path**: confirm the destination court's e-filing route is
  consistent across the packet (the same county clerk / portal).

## Pass 4 — Sworn vs. argued

Compare what is **sworn** in the supporting affidavit against what is
**argued** in the motion or brief:

- Every **factual assertion** in the argument should be either
  (a) supported by a citation to an affidavit paragraph,
  (b) admitted in the pleadings, or (c) a matter of judicial notice.
- Identify any factual claim in the motion that is **not** supported
  by the affidavit — that gap must be fixed before filing.
- Identify any factual claim in the affidavit that is **not used** in
  the motion — decide whether it belongs there at all.
- Verify the affidavit's **personal-knowledge foundation** — flag any
  paragraph that begins "I believe" or "I understand" without a stated
  basis, since affidavits must rest on personal knowledge.

## Output format

When invoked on a packet, produce a structured report:

```
FACT-CHECK REPORT — [Document title / Case number]

Pass 1 (Citations)
  PASS  O.C.G.A. § 9-11-56                 — exists; correct subsection
  WARN  Hill v. American Express,          — re-verify S.E.2d parallel
        289 Ga. App. 576, 657 S.E.2d 547     pincite against an
        (2008)                               authenticated database
  FAIL  O.C.G.A. § 18-4-112                — REPEALED (pre-2016
                                             garnishment numbering)
  FAIL  Smith v. Jones, 300 Ga. 12         — no such case found on
                                             CourtListener (court ga)

Pass 2 (Internal consistency)
  PASS  Defined terms used consistently
  WARN  Paragraph numbering jumps from 6 to 8

Pass 3 (Packet consistency)
  PASS  Caption matches across motion, affidavit, proposed order
  FAIL  Motion seeks $4,500 in fees; Proposed Order awards $4,000

Pass 4 (Sworn vs. argued)
  FAIL  Motion ¶ 3 asserts "Plaintiff sent a 30-day notice"; no
        corresponding affidavit paragraph

Summary: 6 PASS / 2 WARN / 4 FAIL — DO NOT FILE until 4 FAILs resolved.
```

## Composition

- `ga-quality-check` — the lighter pre-filing format-and-content pass;
  this skill is the deeper evidentiary-citation pass.
- `ga-draft-motion` — when a fact-check turns up a missing or bad
  authority, re-draft the affected section.
- `ga-consumer-debt` — for verifying the debt-buyer / written-contract
  anchors (*Nyankojo*, *Wirth*, *Rutledge*, *Hill*) in a collection
  matter.
- `ga-family-law` — for verifying the equitable-distribution anchor
  (*Stokes*) and custody / support statutory cites.
- `ga-law-references` — the canonical Georgia corpora (court rules,
  O.C.G.A. statutes, and the shared federal symlinks) to verify cites
  against.
