---
name: tn-statewide-format-codearranger
title: Tennessee Statewide Court Document Formatting
description: 'Use when the user asks to "draft a pleading", "format a Tennessee court document", "apply Tenn. R. Civ. P. 10", "build a Tennessee caption", or "format a filing" for any Tennessee court. Covers Tenn. R. Civ. P. 10 form-of-pleadings (caption with party block, docket-number line, document title; numbered paragraphs; attaching written instruments), the Rule 11 signature block with BPR number, certificate of service under Rule 5, line-numbered pleading-paper conventions, and Tennessee citation format (S.W.3d, Tenn. Sup. Ct. R. 4, Bluebook). Key point: Tennessee has NO statewide page/margin/font rule — typography and page limits come from each court''s LOCAL RULES. Line numbering is universal marketplace convention applied by default to pleadings.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/tn-court-docs/skills/tn-statewide-format
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Tennessee Statewide Court Document Formatting

> **NOT LEGAL ADVICE.** This skill assists with drafting and
> formatting only. Verify against the current Tennessee Rules of
> Civil Procedure and the local rules of the filing court before
> submitting any document.

Use these conventions whenever drafting a paper to be filed in a
Tennessee state trial court. The form of a Tennessee pleading is
governed by **Tenn. R. Civ. P. 10** (form of pleadings) and
**Tenn. R. Civ. P. 11** (signing of pleadings), supplemented by
**Tenn. R. Civ. P. 5** (service and filing of subsequent papers).

## Key architectural point: there is NO statewide page/margin/font rule

Tennessee does **not** publish a single statewide rule prescribing
paper size, margins, font, line spacing, or page limits. The form of
a pleading is set by:

- **Tenn. R. Civ. P. 10** — caption, numbered paragraphs, and
  attachment of written instruments (content/structure, not
  typography);
- **Tenn. R. Civ. P. 11** — the signature and its representations;
  and
- the **LOCAL RULES of the filing court** — each judicial district /
  county court publishes its own local rules covering margins, font,
  page limits, chambers copies, proposed-order requirements, and
  e-filing mechanics. These are indexed on the Administrative Office
  of the Courts "Local Rules of Practice" page at **tncourts.gov**.

So this skill states the **common-practice defaults** for typography
and **defers page limits / margins / font specifics to local rules**.
Always pull the controlling court's local rules before relying on any
page limit or margin figure. (Davidson, Shelby, Knox, and Hamilton
each have their own overlay skill — see Composition.)

## Common-practice typographic defaults (verify against local rules)

These are the customary defaults Tennessee practitioners use absent a
contrary local rule. They are conventions, not a statewide mandate —
confirm against the filing court's local rules.

| Item | Common-practice default |
|------|--------------------------|
| Paper size | US Letter, 8½ × 11 inches |
| Margins | 1 inch on all four sides |
| Body font | 12 point, serif (Times New Roman or Century Schoolbook) |
| Line spacing | Double-spaced body text; single-spaced block quotes, captions, and signature blocks |
| Ink | Black |
| Page numbers | Each page numbered; `Page X of Y` in the footer |

`scripts/format-check.py` validates a generated `.docx` against these
common-practice defaults and flags departures so they can be checked
against the controlling local rule.

## Line numbering (pleading paper) — applied BY DEFAULT

Apply continuous line numbering down the left margin of every
generated Tennessee pleading. Line numbers count every body line and
**restart on each page**.

Tenn. R. Civ. P. 10 does **not** itself require line numbering, and a
Tennessee pleading filed without line numbers is rule-compliant. But
line-numbered pleading paper is universal practice across the
`claude-legal` marketplace: it lets the court and opposing counsel
cite an exact location ("page 4, lines 12-15") and never harms a
Tennessee filing. Apply it **by default** to every motion, memorandum,
declaration, affidavit, notice, and proposed order. Exhibits and
attachments are exempt.

For programmatically generated `.docx` documents, apply line numbering
through the section's `lineNumbers` property:

```javascript
import { LineNumberRestartFormat } from "docx";

sections: [{
  properties: {
    page: { /* size + margins */ },
    lineNumbers: {
      countBy: 1,                                // number every line
      restart: LineNumberRestartFormat.NEW_PAGE, // restart 1.. each page
    },
  },
  // ...
}]
```

This emits `<w:lnNumType w:countBy="1" w:restart="newPage"/>` into
the section's `<w:sectPr>`. The numbers render in the left margin and
do not shift the 1-inch text margin.

**Do NOT set `start` explicitly.** An explicit `start: 1` renders off
by one in LibreOffice (the first body line shows "2"). Omit `start` —
it defaults to 1 in OOXML.

## Required footer (mandatory on every generated document)

Every generated document MUST carry a running footer on every page:

- **Left**: a short document identifier — typically
  `[Document title] — Docket No. [docket number]` (e.g.,
  `Motion to Dismiss — Docket No. 25C-1234`). Keep it to a single
  line so it never wraps.
- **Right**: `Page X of Y`, where `X` is the current page number and
  `Y` is the total page count. Use Word's `PAGE` and `NUMPAGES`
  fields — never a static number.
- **Font**: 10 pt; matches body font family.
- **Alignment**: a right-aligned tab stop at 9,360 DXA (6.5") places
  the page counter flush right while the title stays flush left.

The footer runs continuously from page 1 through the last exhibit
page — do not restart or suppress pagination anywhere.

## Caption structure (Tenn. R. Civ. P. 10.01)

Rule 10.01 requires every pleading to contain a caption stating the
**name of the court**, the **title of the action** (the parties), the
**file (docket) number**, and a **designation** of the pleading per
Rule 7.01. The Tennessee caption stacks four elements:

```
        IN THE CIRCUIT COURT FOR DAVIDSON COUNTY, TENNESSEE

VELOCITY INVESTMENTS, LLC,             )
                                       )
       Plaintiff,                      )
                                       )
v.                                     )   Docket No. ____________
                                       )
JOHN DOE,                              )
                                       )
       Defendant.                      )

                        ANSWER OF DEFENDANT
```

### The four caption elements in order

1. **Court identifier line** (centered, ALL CAPS). Name the court and
   county:
   - Circuit Court: `IN THE CIRCUIT COURT FOR [COUNTY] COUNTY, TENNESSEE`
   - Chancery Court: `IN THE CHANCERY COURT FOR [COUNTY] COUNTY, TENNESSEE, AT [CITY]`
     (many Chancery Courts name the sitting city, e.g., "AT MEMPHIS")
   - General Sessions: `IN THE GENERAL SESSIONS COURT FOR [COUNTY] COUNTY, TENNESSEE`
     (note General Sessions practice is informal — see `tn-general-sessions`)
2. **Party block.** On the left, the parties stacked with their
   designations, separated by a centered `v.`; on the right, a column
   of right parentheses `)` (the traditional Tennessee "tied bracket"
   style) closing into the docket-number line. Use the designations
   that match the case type:
   - **Plaintiff / Defendant** for actions at law (Circuit Court);
   - **Plaintiff / Defendant** is also common in Chancery, but
     **Petitioner / Respondent** is used in domestic-relations
     matters and many special Chancery proceedings (`In re:` for
     in-rem captions).
3. **Docket-number line.** `Docket No. ____________` (some clerks use
   `No. ____` or `Case No. ____`). The filer leaves it blank on an
   initial pleading — the clerk assigns and stamps the number on
   filing — and populates it on every subsequent paper.
4. **Document title** (centered, ALL CAPS) immediately below the
   caption: e.g., `COMPLAINT`, `MOTION TO DISMISS`,
   `ANSWER AND COUNTERCLAIM`, `MOTION FOR SUMMARY JUDGMENT`.

### Caption variants by court

- **Chancery Court** routinely adds the sitting city ("AT MEMPHIS",
  "AT NASHVILLE") and is presided over by a Chancellor with a Clerk &
  Master as the equity clerk.
- **Domestic relations** (divorce may be filed in either Circuit or
  Chancery) uses `IN RE THE MARRIAGE OF` or Petitioner / Respondent.
  See `tn-family-law` and `tn-family-court`.
- **General Sessions** civil matters are commenced by a **civil
  warrant**, not a formal captioned complaint — the warrant form
  supplies the caption fields. See `tn-general-sessions`.

## Numbered paragraphs (Tenn. R. Civ. P. 10.02)

Under Rule 10.02, all averments of claim or defense are made in
**numbered paragraphs**, the contents of each limited as far as
practicable to a **single set of circumstances**. Number with an
Arabic numeral, a period, and a tab: `1.\tThe Defendant is a
resident of Davidson County, Tennessee.` Claims founded on separate
transactions should be stated in separate counts when separation
facilitates clarity.

## Attaching written instruments (Tenn. R. Civ. P. 10.03)

Under Rule 10.03, when a claim or defense is founded on a **written
instrument** (a contract, note, lease, assignment, etc.), a copy must
be **attached as an exhibit** unless its absence is excused, and the
exhibit is a part of the pleading for all purposes. Reference each
exhibit by letter in the body ("a true and correct copy of the
[instrument] is attached as **Exhibit A**") and attach the copies
after the signature block and certificate of service.

## Signature block (Tenn. R. Civ. P. 11)

Under Rule 11, every pleading, motion, or other paper must be
**signed by at least one attorney of record** in the attorney's
individual name, or, **if the party is not represented, by the party**.
The signature certifies the Rule 11.02 representations (the paper is
not interposed for delay, claims are warranted by law, factual
contentions have evidentiary support, etc.).

An attorney's signature block must include the attorney's
**Tennessee Board of Professional Responsibility (BPR) number** — the
attorney-registration number assigned through the Tennessee Supreme
Court's Board of Professional Responsibility:

```
Respectfully submitted,


                                   ____________________________
                                   [Name]
                                   BPR No. #####
                                   [Firm name]
                                   [Street address]
                                   [City, TN ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   Attorney for [Party]
```

**Pro se filers omit the BPR number** and identify themselves as
self-represented:

```
                                   ____________________________
                                   [Name]
                                   [Street address]
                                   [City, TN ZIP]
                                   Phone: (###) ###-####
                                   Email: name@example.com
                                   Pro Se / Self-Represented
```

See `tn-pro-se` for the full self-represented drafting framework.

## Verification / declaration language

Many Tennessee filings use a traditional **notarized affidavit** with
a jurat; Tennessee also recognizes **unsworn declarations** in certain
contexts. For a declaration, close the body with:

```
I declare under penalty of perjury under the laws of the State of
Tennessee that the foregoing is true and correct.

Executed on [date] at [city], [state].

                                   ____________________________
                                   [Declarant name]
```

For a sworn affidavit, use the jurat ("Sworn to and subscribed before
me this ___ day of ____, 20__") with the notary block. Verify whether
a particular filing must be sworn (notarized) rather than declared and
that the current statute authorizes an unsworn declaration for that
use.

## Certificate of service (Tenn. R. Civ. P. 5)

Every paper required to be served must carry a certificate of service
under Rule 5. Place it at the foot of the document, above or below the
signature block per local custom:

```
                    CERTIFICATE OF SERVICE

I certify that on [date] a true and correct copy of the foregoing
[Document Title] was served on:

  [Opposing party / counsel name]
  [Address]
  via [the court's electronic-filing system / U.S. Mail, postage
       prepaid / hand delivery / email per Tenn. R. Civ. P. 5.02].

                                   ____________________________
                                   [Signer name]
```

Rule 5.02 prescribes the permissible methods of service of subsequent
papers (mail, delivery, and — where authorized — electronic service
through the court's e-filing system). Initial process is served under
**Tenn. R. Civ. P. 4** (summons; 90-day issuance/return), not Rule 5.

## Exhibits

Attach exhibits after the signature block and certificate of service:

1. An **Exhibit List** page, centered title, each entry like
   `Exhibit A:    [one-line description]`.
2. One **cover page per exhibit**: `EXHIBIT A` centered and bold,
   followed by an italic caption, then the exhibit content.
3. Footer pagination continues through the exhibits — do not restart
   the page counter.

A written instrument attached under Rule 10.03 is itself an exhibit
and is part of the pleading for all purposes.

## Citation format

Tennessee follows **standard Bluebook** style; there is no mandatory
Tennessee-specific style manual.

- Tennessee Supreme Court: `Rye v. Women's Care Ctr. of Memphis, MPLLC,
  477 S.W.3d 235 (Tenn. 2015)`
- Tennessee Court of Appeals: `Smith v. Jones, 123 S.W.3d 456 (Tenn.
  Ct. App. 2003)`
- Court of Criminal Appeals: `(Tenn. Crim. App. [year])`
- Statutes: `Tenn. Code Ann. § 28-3-109` (or `T.C.A. § 28-3-109`)
- Rules: `Tenn. R. Civ. P. 56.04`; `Tenn. R. Evid. 803(6)`

**Tenn. Sup. Ct. R. 4** governs publication and citation: a
**published** opinion is controlling authority; an **unpublished**
opinion is persuasive only and may be cited (subject to the
limitations in Rule 4), unless it has been designated not-for-citation.
See `tn-fact-check` for citation verification.

## Producing documents programmatically

For `.docx` generation, use the `docx` npm package. Key points:

- Set page size explicitly to US Letter (12,240 × 15,840 DXA) —
  `docx-js` defaults to A4.
- Use Times New Roman at `size: 24` (half-points = 12 pt).
- Apply uniform 1,440 DXA margins to all four sides on every section
  (a common-practice default — confirm against local rules).
- Build the footer with a right-aligned tab stop at 9,360 DXA and use
  `PageNumber.CURRENT` / `PageNumber.TOTAL_PAGES` for "Page X of Y".
- Apply the `lineNumbers` section property above (omit `start`).

Run `scripts/format-check.py` on the generated `.docx` to validate the
common-practice defaults.

## Filing mechanics: paper vs. e-filing

Tennessee has **no universal statewide e-filing mandate** — the
platform is county-by-county. Davidson Chancery uses eFileTN/Odyssey
(Tyler); Shelby Circuit and Chancery use eFlex; other counties use
Tybera (TnCIS) or accept paper. Confirm the venue platform and whether
e-filing is mandatory before assembling a packet. The appellate courts
use the statewide AOC e-filing portal. See the venue skills and
`tn-file-packet`.

## Composition

- For Davidson County (Nashville, 20th JD): `tn-davidson`
- For Shelby County (Memphis, 30th JD): `tn-shelby`
- For Knox County (Knoxville, 6th JD): `tn-knox`
- For Hamilton County (Chattanooga, 11th JD): `tn-hamilton`
- For limited-jurisdiction / civil-warrant practice:
  `tn-general-sessions`
- For other counties: `tn-county-courts`
- For drafting specific document types: `tn-draft-motion`,
  `tn-draft-declaration`, `tn-draft-note`, `tn-draft-order`
- For pro se conventions: `tn-pro-se`
- For pre-filing QC: `tn-quality-check`
- For citation verification: `tn-fact-check`

## References

- `tn-law-references` — canonical Tenn. R. Civ. P., Tenn. R. Evid.,
  T.C.A., and local-rules corpus
- `scripts/format-check.py` — common-practice format validation
