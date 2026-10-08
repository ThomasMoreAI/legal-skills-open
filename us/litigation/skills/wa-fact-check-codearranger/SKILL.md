---
name: wa-fact-check-codearranger
title: Fact-Check a Washington Court Filing
description: 'Use this skill to fact-check a Washington court filing (or packet of filings) before filing. Triggers include "fact check this", "fact-check", "verify citations", "check my citations", "consistency check", "audit this filing", "cite-check", "shepardize", "verify the law", "double-check the draft", "check for hallucinations". Runs four passes: (1) citation verification (RCW/CR/CRLJ/ER/GR/U.S.C./C.F.R./case law resolves to real sources); (2) internal consistency (dates, party names, cause number, dollar amounts, paragraph cross-refs); (3) packet consistency (caption, parties, cause number, key facts across documents); (4) sworn-vs.-argued consistency (facts in motion match declarations). Flags issues for user; does not silently rewrite content.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/wa-court-docs/skills/wa-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check a Washington Court Filing

The fastest way to lose credibility with a Washington judge is to
cite a case that doesn't exist or misstates its holding, or to
file a motion whose facts contradict the sworn declaration it
relies on. This skill runs a four-pass check — **citation
verification**, **internal consistency**, **packet consistency**,
and **sworn-vs.-argued consistency** — and produces a
human-reviewable report.

> **NOT LEGAL ADVICE.** Fact-checking verifies the surface — it
> doesn't tell the user whether the underlying legal position is
> sound. Pair with substantive review by counsel where stakes
> warrant.

> **Never silently rewrite.** This skill flags issues; the user
> (and, as needed, the drafting skills) fix them. Silent edits to
> citations or facts are how hallucinations get filed.

## Inputs to gather

Ask the user:

1. **Target scope** — a single file, or the whole packet?
2. **Path(s)** — absolute paths to each file (motion, declaration,
   exhibits, order, note, CoS)
3. **Intended filing date** — for determining whether recent
   statutory / rule amendments apply
4. **Jurisdiction** — superior / district (KCDC); some citation
   conventions differ
5. **Is this already in draft form** or freshly generated? — if
   freshly generated, run more aggressive hallucination checks

## Pass 1 — Citation verification

For every citation in the document, verify that it exists and that
the cited source supports the stated proposition.

### 1a. Identify every citation

Parse the document for:

- **Washington cases**: `\d+ Wn\.(2d|App\.) \d+` or
  `\d+ P\.(2d|3d) \d+`
- **U.S. Supreme Court**: `\d+ U\.S\. \d+` or `\d+ S\. ?Ct\. \d+`
- **Federal circuit / district**: `\d+ F\.(2d|3d|4th|Supp\.(2d|3d)) \d+`
- **RCW**: `RCW \d+\.\d+(\.\d+)?` (sometimes with subsection
  parentheticals)
- **Court rules**: `CR \d+(\([a-z]\))?`, `CRLJ \d+`, `ER \d+`,
  `GR \d+`, `RAP \d+\.\d+`
- **Federal statutes**: `\d+ U\.S\.C\. § \d+`
- **CFR**: `\d+ C\.F\.R\. (Part |§ ?)\d+(\.\d+)?`
- **Local rules**: `KCLCR \d+`, `KCDCLCR \d+`

Make a list; each entry becomes a verification item.

### 1b. Verify each citation

For each citation:

1. **Fetch the canonical source** using the URL patterns in
   `wa-law-references/references/online-sources.md`:
   - RCW → `https://app.leg.wa.gov/RCW/default.aspx?cite=X.XX.XXX`
   - CR / CRLJ / ER / GR → `https://www.courts.wa.gov/court_rules/`
     with the appropriate rule path
   - CFR → `https://www.ecfr.gov/current/title-XX/...`
   - U.S.C. → `https://www.law.cornell.edu/uscode/text/XX/XXXX`
   - Cases → CourtListener / Google Scholar

   For programmatic verification (preferred when fact-checking
   many cites), use the APIs in
   `wa-law-references/references/legal-data-apis.md`:
   - **CourtListener citation-lookup** —
     `POST https://www.courtlistener.com/api/rest/v3/citation-lookup/`
     with `{"text": "<citation>"}` returns the case + opinion text.
     This is the cleanest path for batch cite-checking.
   - **eCFR Versioner API** —
     `https://www.ecfr.gov/api/versioner/v1/full/<date>/title-<N>.xml?part=<P>`
     returns the in-force CFR text on a given date.
   - **USC USLM XML** — bulk download per release point from
     `uscode.house.gov` for offline cite verification at scale.
2. **Confirm the cite resolves** — the URL returns content that
   matches the cite
3. **Read the proposition the document attributes to the source**
4. **Verify the source supports the proposition** — not just that
   the case exists, but that its holding matches what the document
   claims
5. **Flag any mismatch** as one of:
   - **RED (existence)**: citation does not resolve to a real
     source — possible hallucination
   - **YELLOW (mismatch)**: source exists but does not support the
     stated proposition, or the proposition overstates the holding
   - **ORANGE (amendment)**: source exists and supports the
     proposition, but the statute/rule has been amended and the
     current version differs from what's quoted
   - **GREEN (ok)**: source exists, supports the proposition, and
     text is current

### 1c. Typical hallucination patterns to watch for

- **Case name correct, cite numbers wrong** — a real case at a
  different volume/page
- **Case name fabricated** — plausible-sounding case name that
  returns nothing on CourtListener
- **Real case, real cite, wrong holding** — the case exists but
  does not stand for the proposition in the motion
- **Circuit misattribution** — e.g., Ninth Circuit holding
  attributed to Sixth Circuit or vice versa
- **Year off** — 2009 case cited as 2019
- **Pinpoint cite wrong** — volume and page correct, but the cited
  paragraph is on a different page

### 1d. Recent-amendment check

For statutes and rules, note:

- **Effective date** on the source page
- Whether the document quotes the current text or an older version
- If older, whether the relevant subsection was amended (check
  "history" link on leg.wa.gov for RCW; check "session" on
  courts.wa.gov for rules)

Flag any citation where the text has changed since the cited
version as **ORANGE**.

## Pass 2 — Internal consistency

Within a single document, verify:

### 2a. Dates

- **Date of event vs. dates in the narrative** — a "January 12,
  2023" event referenced later as "January 21, 2023" is a
  contradiction
- **Deadline math** — if the motion says "Plaintiff served
  discovery on March 1 and responded on April 5 (35 days later)",
  verify 35 is actually the day count
- **Statute of limitations math** — if the filing claims the SOL
  bar date is X, verify it's actually X given the alleged default
  date
- **Signing / declaration dates** in the future or too far in the
  past

### 2b. Party names

- **Every reference to a party** uses the same name and styling
  (e.g., "Velocity Investments, LLC" consistently, not alternating
  with "Velocity Investments LLC" or "Velocity")
- **Pronouns match** — if the document introduces "Plaintiff", it
  should continue to use "Plaintiff" (or the specific name)
- **"Defendant" singular vs. plural** — consistent throughout

### 2c. Cause number

- Same cause number every time it appears
- Consistent format (`YYCIV######KCX` for KCDC)

### 2d. Dollar amounts

- Principal + interest + fees = claimed total
- Judgment amount consistent across paragraphs
- Settlement / offer amounts consistent

### 2e. Paragraph cross-references

- "As stated in paragraph 12 above" — paragraph 12 actually says
  that
- Exhibit references — "Exhibit A" in the motion matches "Exhibit
  A" in the declaration's exhibit list
- Footnote references in order and present

### 2f. Defined terms

- Every defined term ("the Account", "the Agreement", "the
  Debt") is defined once and used consistently after

## Pass 3 — Packet consistency

Across the documents in the packet (motion, memorandum,
declaration, exhibits, proposed order, note, CoS):

### 3a. Caption

Use `wa-statewide-format` caption conventions. Every document
should have:

- **Identical court name** (including division / department)
- **Identical cause number**
- **Identical party names and styling**
- **Title appropriate for the document type**

### 3b. Cross-referenced facts

- **The motion's fact recitation** matches **the declaration**'s
  factual content — the motion cannot "recite" facts that the
  declaration doesn't actually attest to
- **Exhibits referenced in the motion** match **exhibits attached
  to the declaration**
- **Proposed order findings** flow from the motion's arguments
  (the order cannot contain findings that the motion never
  asked for)

### 3c. Relief requested

- **Motion's prayer for relief** matches **proposed order's
  ordered relief** — if the motion asks for three things, the
  order grants three things
- **Note's indication of relief type** (e.g., "Motion for
  Dismissal") matches the motion title

### 3d. Service

- **Certificate of Service** lists every party the motion is
  being served on
- **Method of service** (mail, email, personal) matches what the
  service contacts allow

## Pass 4 — Sworn-vs.-argued consistency

The motion contains **arguments**; the declaration contains
**sworn facts**. Arguments must be grounded in sworn facts; sworn
facts must not be contradicted by arguments elsewhere.

### 4a. Every factual assertion in the motion has a sworn source

For each factual claim in the motion / memorandum:

- Is it supported by the declaration (cited by paragraph)?
- Is it supported by an exhibit (cited by exhibit letter and
  page)?
- Is it supported by a judicial admission (an opposing party's
  pleading or answer)?
- If none of the above, **flag as unsupported** — either add a
  sworn source or remove the factual assertion

### 4b. No contradictions between documents

- The motion says "Defendant made no payments after June 2018" —
  the declaration says "Defendant made a final payment in August
  2018" → contradiction
- The motion says "Plaintiff served only one set of RFPs" — the
  exhibit list shows three sets attached → contradiction

### 4c. Declarations are within the declarant's knowledge

- Declarant has personal knowledge of each assertion (CR 56(e) /
  CRLJ 56(e))
- No declarant testifies to events they could not have observed
- Hearsay within declarations is either excepted or flagged

## Producing the report

Output a structured fact-check report:

```
FACT-CHECK REPORT — [Case] [Date]

Scope: [files reviewed]

=============================================================
SUMMARY
=============================================================
Citations checked:            [N]
  GREEN (ok):                 [n]
  ORANGE (amendment):         [n]
  YELLOW (mismatch):          [n]
  RED (existence):            [n]
Internal consistency issues:  [N]
Packet consistency issues:    [N]
Sworn-vs.-argued issues:      [N]
OVERALL:                      [PASS / NEEDS ATTENTION / BLOCK]

=============================================================
PASS 1 — CITATIONS
=============================================================

[RED]  Motion ¶ 14: "Smith v. Jones, 125 Wn.2d 400 (2010)"
        Could not resolve on CourtListener or courts.wa.gov.
        Possible hallucination — user should verify or remove.

[YELLOW] Motion ¶ 22: "Hangman Ridge, 105 Wn.2d at 780, for the
        proposition that 'causation is presumed on a per se CPA
        claim'"
        Hangman Ridge at 780 addresses the public-interest element
        and the per se pathway generally but does not state that
        causation is presumed. See Hangman Ridge 105 Wn.2d at
        784-85; Indoor Billboard, 162 Wn.2d at 83. Suggested fix:
        cite Indoor Billboard for the causation proposition.

[ORANGE] Declaration ¶ 4: "RCW 4.84.080 provides for a statutory
        attorney fee of $125 in district court"
        Current RCW 4.84.080 (as of fetch date) shows $[amount]
        — verify the current amount and update.

[GREEN]  Motion ¶ 8: "15 U.S.C. § 1692e(2)(A)" — confirmed; text
        unchanged; proposition supported.

=============================================================
PASS 2 — INTERNAL CONSISTENCY
=============================================================

[Motion p. 3 ¶ 7 vs. Motion p. 6 ¶ 14]
   "account was opened in 2012" vs. "account originated in 2011"
   → Resolve the origination year.

[Declaration Ex. B is referenced twice, with different subjects]
   → Check whether there are two Exhibit B's or a scanning error.

=============================================================
PASS 3 — PACKET CONSISTENCY
=============================================================

[Caption mismatch]
   Motion caption:       "Velocity Investments, LLC"
   Declaration caption:  "Velocity Investments LLC"  (missing comma)
   Proposed order:       "Velocity Investments, LLC"
   → Standardize.

[Relief mismatch]
   Motion prays for: (1) dismissal, (2) fees, (3) sanctions
   Proposed order grants: (1) dismissal, (2) fees
   → Sanctions request dropped from the order — intentional?

=============================================================
PASS 4 — SWORN-VS.-ARGUED
=============================================================

[Unsupported assertion]
   Motion ¶ 9: "Plaintiff acquired the debt for less than 5% of
   face value."
   No declaration supports this. No exhibit supports this. If
   this is true and material, add a sworn source; if not
   supportable, remove the assertion.

[Potential contradiction]
   Motion ¶ 11: "Plaintiff has provided no monthly statements."
   Declaration ¶ 7: "Plaintiff provided three monthly statements
   but no statements for 2019."
   → Soften the motion's assertion to match the declaration.

=============================================================
RECOMMENDED FIXES (in priority order)
=============================================================

1. [BLOCKER] Resolve Motion ¶ 14 citation (possible hallucination)
2. [BLOCKER] Resolve Pass-4 contradiction about monthly statements
3. [IMPORTANT] Standardize caption party name across packet
4. [IMPORTANT] Verify RCW 4.84.080 current amount
5. [SUGGESTED] Re-cite proposition at Motion ¶ 22 to a case that
   supports it
```

## Blockers vs. flags

- **BLOCKER** — do not file: hallucinated citation, sworn-vs.-
  argued contradiction, caption mismatch on substantive party,
  cause number wrong
- **IMPORTANT** — fix before filing if possible: amended statute
  text, internal inconsistency that could be read as dishonest,
  unsupported factual assertion
- **SUGGESTED** — worth a second look but not disqualifying:
  stronger case available for a proposition; stylistic
  inconsistency

## Steps

1. **Load and parse** each document in the scope
2. **Extract citations** via pattern matching
3. **Fetch canonical sources** for each citation (prefer
   WebFetch; respect the web-content-restrictions — do **not**
   fall back to alternative fetch methods if WebFetch declines)
4. **Verify propositions** against fetched source
5. **Cross-document consistency** pass
6. **Sworn-vs.-argued** pass
7. **Produce report** with RED/YELLOW/ORANGE/GREEN flags
8. **Offer to re-draft** flagged items by handing off to the
   appropriate draft-* skill
9. **Do not silently edit** — every change to a citation or fact
   must be surfaced to the user

## Cross-references

- For format (GR 14) compliance, use `wa-quality-check`
- For citation format conventions, see
  `wa-law-references/references/citation-format.md`
- For canonical URLs, see
  `wa-law-references/references/online-sources.md`
- For re-drafting flagged sections, hand off to `wa-draft-motion`,
  `wa-draft-declaration`, or `wa-draft-order`

## Handling fetch failures

If WebFetch fails for a canonical URL:

1. Do **not** try alternative fetch methods
2. Flag the citation as **UNVERIFIED (fetch failed)** — distinct
   from RED (hallucination)
3. Continue with remaining citations
4. Report unverified items separately so the user can verify
   manually

## Notes

- **Fact-checking is not editing.** Changes are made by the user
  (or by a drafting skill invoked explicitly) — never by this
  skill silently
- **Shepardize matters.** A case that was good law when written
  into a memo template may have been overruled; include
  "overruled?" checks when the case is older than 5 years
- **Trust but verify even the plugin's own references.** This
  plugin's reference files (`wa-law-references/references/*.md`)
  summarize case holdings; those summaries can drift. Prefer
  canonical sources for verification
- **Keep the report readable.** A 50-page fact-check report that
  the user won't read is worse than a 2-page report that
  prioritizes blockers
- **Integrate with `wa-file-packet`** — `wa-file-packet` should
  offer to run `wa-fact-check` as part of preflight before any
  court filing
