---
name: immigration-fact-check-codearranger
title: Fact-Check an Immigration Filing
description: 'Use this skill to verify citations and consistency of any immigration draft (brief, motion, declaration, USCIS letter, BIA appeal, petition for review). Triggers: "verify this immigration citation", "is this INA cite right", "INA vs USC", "check my immigration brief", "fact check", "is this BIA case real", "cite-check", "8 CFR 208 or 1208", "DHS or EOIR regulation", "FAM cite", "check hallucinations", "consistency check", "audit this filing", "A-number consistent". Four passes: (1) citation verification — INA/USC/CFR/FAM/I&N Dec./circuit cites resolve to real sources; (2) internal consistency — dates, A-number, names, cross-refs; (3) packet consistency — caption, A-number across documents; (4) sworn-vs-argued consistency — brief facts don''t contradict declarations. Flags: INA-vs-8-U.S.C. mismatch, DHS-vs-EOIR duplication, FAM-is-guidance-not-law. **Verification only** — never rewrites.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/claude-legal-immigration-laws/skills/immigration-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check an Immigration Filing

The fastest way to lose credibility before an immigration judge, the Board, a
USCIS officer, or a circuit panel is to cite a provision that doesn't exist,
confuse the INA section with the 8 U.S.C. section, cite the DHS regulation when
the EOIR one governs, or file a brief whose facts contradict the sworn
declaration. This skill runs a four-pass check and produces a human-reviewable
**verification report**.

> **NOT LEGAL ADVICE.** Fact-checking verifies the surface — it does not tell
> the user whether the underlying legal position is sound, nor whether a cited
> case is still good law on the facts. Immigration consequences are severe and
> often irreversible; pair this with substantive review by a licensed
> immigration attorney or an EOIR-accredited representative.

> **Never silently rewrite.** This skill flags issues; the user (and, as
> needed, the drafting skills) fix them. Silent edits to citations or facts are
> how hallucinations get filed.

## Inputs to gather

1. **Scope** — a single document, or the whole packet?
2. **Path(s)** — absolute paths to each file.
3. **Forum** — USCIS, EOIR immigration court, BIA, circuit, or consular. The
   forum decides *which* of the duplicated regulations governs (see traps).
4. **Intended filing date** — for catching post-snapshot amendments.

## Pass 1 — Citation verification

Parse the document for every citation type — **INA** (`INA § 240`), **U.S.
Code** (`8 U.S.C. § 1229a`), **CFR** (Title 8 **and** 22), **FAM** (`9 FAM`),
**BIA/AG precedent** (`28 I&N Dec. 199`), and **circuit / Supreme Court**
(`F.3d` / `U.S.`) — then verify each resolves to a real source that supports
the stated proposition.

### 1a. INA ↔ 8 U.S.C. cross-check (the #1 trap)

For **every** statutory cite, verify *both* the INA number and the 8 U.S.C.
number against the crosswalk in
[`../../references/immigration-statutes/README.md`](../../references/immigration-statutes/README.md).
The offset is **not constant** — never compute it. The common right answers:
INA § 240 = 8 U.S.C. § 1229a; INA § 212 = 8 U.S.C. § 1182; INA § 245 =
8 U.S.C. § 1255; INA § 208 = 8 U.S.C. § 1158; INA § 242 = 8 U.S.C. § 1252.
A brief that says "INA § 240 (8 U.S.C. § 1182)" is **mismatched** — flag it.
Confirm the verbatim text in the matching
[`../../references/immigration-statutes/`](../../references/immigration-statutes/)
subchapter file actually says what the draft claims.

### 1b. CFR cross-check against the regulation corpus

Resolve each CFR cite against the file in
[`../../references/immigration-regulations/`](../../references/immigration-regulations/)
(e.g., `8CFR-1240-removal-eoir.md`, `22CFR-042-immigrant-visas.md`). Confirm the
part/section exists and supports the proposition.

### 1c. Case-law verification (CourtListener)

Case law is **not** snapshotted — verify on demand per
[`../../references/legal-data-apis.md`](../../references/legal-data-apis.md).
Use the **bundled CourtListener MCP server** (declared in this plugin's
`.mcp.json`; if its tools are absent, have the user run `/mcp` to sign in) —
the citation-lookup / search tools, per the `immigration-case-law` skill — to
confirm a **circuit** opinion is real and says what the draft claims — watch for circuit misattribution (the
Ninth Circuit `ca9` has the largest immigration docket). **BIA precedent** is
cited **"I&N Dec."** (e.g., *Matter of A-B-*, 28 I&N Dec. 199 (BIA 2021)) —
EOIR's Virtual Law Library is the publisher of record and CourtListener indexes
many; confirm the precedent has not been certified/overruled by the Attorney
General.

Flag each cite **RED** (does not resolve — possible hallucination),
**YELLOW** (resolves but does not support the proposition / overstates it),
**ORANGE** (resolves and supports, but the provision was amended since the
quoted version), or **GREEN** (resolves, supports, current).

## The three immigration citation traps

- **INA-vs-8-U.S.C. mismatch.** See Pass 1a. Verify both numbers; never assume
  a constant offset.
- **DHS-vs-EOIR regulation duplication.** Several regulations exist in **two
  parallel versions** — the DHS copy and the EOIR copy — and the draft must
  cite the one that governs its forum:
  | Subject | DHS (USCIS / CBP / ICE) | EOIR (court / BIA) |
  |---|---|---|
  | Asylum | 8 CFR Part **208** | 8 CFR Part **1208** |
  | Removal proceedings | 8 CFR Part **240** | 8 CFR Part **1240** |
  | EOIR / BIA procedure | — | 8 CFR Part **1003** |
  A removal-defense brief filed in immigration court that cites "8 CFR § 208.13"
  (DHS) instead of "8 CFR § 1208.13" (EOIR) is citing the wrong sovereign's
  rule — flag it **YELLOW** and point to the forum-correct part in the
  regulation corpus.
- **FAM is guidance, not law.** A `9 FAM` / `8 FAM` / `7 FAM` cite is **State
  Department internal guidance**, not binding authority. Never let a FAM cite
  stand alone — flag any FAM cite that is not paired with the controlling
  **INA / 8 CFR / 22 CFR** provision, and verify the FAM text against
  [`../../references/foreign-affairs-manual/`](../../references/foreign-affairs-manual/).

## Pass 2 — Internal consistency

Within a single document, verify:

- **A-number** (`A2NN-NNN-NNN`) is identical every time it appears, and matches
  the NTA / receipt notice. A drifting A-number is a blocker.
- **Receipt numbers** (`XYZ` + 10 digits), **priority dates**, and **A-file**
  references are consistent.
- **Dates** agree (date of entry, NTA service date, hearing date, deadline
  math). A "30 days from service" claim should compute correctly.
- **Party / declarant names** and **country of nationality** are styled
  consistently throughout.
- **Paragraph and exhibit cross-references** ("as stated in ¶ 12") actually
  point where they claim.

## Pass 3 — Packet consistency

Across every document in the filing (brief, motion, declaration, exhibit index,
proposed order, certificate of service):

- **Caption** — identical forum/court, A-number, and party names on every page.
- **Cross-referenced facts** — the brief's fact recitation matches the
  declaration's sworn content; exhibits cited in the brief match the exhibit
  index.
- **Relief requested** — the motion's prayer matches the proposed order.
- **Service** — the certificate lists every party (and, in EOIR matters, DHS /
  the ICE Office of the Principal Legal Advisor).

## Pass 4 — Sworn-vs.-argued consistency

The brief contains **arguments**; the declaration / affidavit contains **sworn
facts**. Verify:

- Every factual assertion in the brief has a sworn source (declaration ¶ or
  exhibit) — flag unsupported assertions.
- No argument contradicts a sworn statement (e.g., brief says "entered in
  2019"; declaration swears "2018").
- Each declarant attests only within personal knowledge; flag hearsay.

## Producing the report

Output a structured report with a summary count
(GREEN / ORANGE / YELLOW / RED + consistency issues), one section per pass with
the exact location and suggested fix, and a prioritized fix list tagged
**BLOCKER** (hallucinated cite, INA/USC mismatch, wrong-forum regulation,
A-number drift, sworn-vs-argued contradiction), **IMPORTANT** (amended text,
unpaired FAM cite, internal inconsistency), or **SUGGESTED** (stronger
authority available; stylistic drift). Keep it readable — a 2-page report that
prioritizes blockers beats a 50-page dump.

## Handling fetch failures

If a canonical fetch fails, flag the item **UNVERIFIED (fetch failed)** —
distinct from RED (hallucination) — and continue. Report unverified items
separately so the user can confirm them manually. Do not silently rewrite.

## Artifacts this skill drafts

- A **verification report** (the four-pass output above).
- A **citation table** mapping each cite to its INA/USC pair, forum-correct
  regulation, and verification status.
- A **prioritized fix list** (BLOCKER / IMPORTANT / SUGGESTED).

## Related authority

- INA ↔ 8 U.S.C. crosswalk — [`../../references/immigration-statutes/README.md`](../../references/immigration-statutes/README.md)
  and the subchapter text in [`../../references/immigration-statutes/`](../../references/immigration-statutes/).
- 8 CFR / 22 CFR text — [`../../references/immigration-regulations/`](../../references/immigration-regulations/)
  (note the DHS `208`/`240` vs. EOIR `1208`/`1240`/`1003` duplication).
- FAM guidance — [`../../references/foreign-affairs-manual/`](../../references/foreign-affairs-manual/).
- Case-law lookup (CourtListener / BIA / AAO) —
  [`../../references/legal-data-apis.md`](../../references/legal-data-apis.md)
  and [`../../references/online-sources.md`](../../references/online-sources.md).

## Composition

Runs after any drafting skill and before filing. Composes with
`immigration-pro-se` (orientation), `eoir-removal-defense`,
`eoir-motions-to-reopen-reconsider`, `bia-appeals`, `uscis-benefit-requests`,
`consular-visa-refusal`, and `circuit-petition-for-review` (re-draft flagged
items by handing back to the originating skill), and with `immigration-deadlines`
(to confirm any deadline math the draft asserts).
