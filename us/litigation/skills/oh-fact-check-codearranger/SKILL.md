---
name: oh-fact-check-codearranger
title: Fact-Check Ohio Court Filings
description: 'Use to verify citations in Ohio filings — Civ. R., Evid. R., R.C., case citations in Ohio public-domain format. Triggers include ''verify Ohio citation'', ''check Ohio R.C.'', ''Ohio public-domain citation YYYY-Ohio-NNNN'', ''Ohio case citation format'', ''verify Ohio rule'', ''spot-check Ohio filing''. Four-pass framework: (1) citation verification against authoritative sources; (2) internal-consistency check; (3) packet-consistency check; (4) sworn-vs-argued alignment.'
author: codearranger
author_url: https://github.com/codearranger/claude-legal/tree/main/plugins/oh-court-docs/skills/oh-fact-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

# Fact-Check Ohio Court Filings

> **NOT LEGAL ADVICE.** This skill is a pre-filing
> verification pass, not a substitute for substantive legal
> research.

## Four-pass framework

### Pass 1: Citation verification

For each citation in the filing:

- **R.C. section** — verify the section exists at
  `codes.ohio.gov/ohio-revised-code/section-NNNN.NN` or in
  the local `oh-statutes-debt/` corpus
- **Ohio Civ. R. / Evid. R. / Sup. R. / etc.** — verify
  the rule exists at the cited number in the local
  `court-rules/` corpus
- **Ohio case** — verify the citation is in the **Ohio
  public-domain format** for post-2002 appellate cases:
  `YYYY-Ohio-NNNN`. Example: `2003-Ohio-1234`. The
  pre-2002 format `Ohio St.3d` continues to apply to older
  decisions.

### Pass 2: Internal consistency

- Numbered paragraphs follow sequence (no jumps or
  duplicates)
- Cross-references in one paragraph match what they refer
  to (e.g., "as set forth in paragraph 5" actually points
  to paragraph 5)
- Exhibits referenced in the body correspond to attached
  exhibits
- Affirmative defenses match the facts pled

### Pass 3: Packet consistency

When filing a packet (motion + affidavit + memorandum +
proposed order):

- Caption + case number identical on every document
- Party names spelled identically across documents
- Service date in certificate of service matches the actual
  service event
- Proposed order's relief tracks the motion's prayer for
  relief

### Pass 4: Sworn-vs-argued alignment

For affidavits supporting motions:

- Every factual assertion in the motion's memorandum traces
  back to either (a) a paragraph in the supporting
  affidavit or (b) an exhibit attached to the affidavit
- The memorandum does NOT introduce new facts not in the
  record
- Conclusions of law are in the memorandum; statements of
  personal knowledge are in the affidavit

## Ohio-specific citation conventions

### Public-domain citation (post-2002)

`*Smith v. Jones*, 100 Ohio St.3d 543, 2003-Ohio-1234,
paragraph 12`

Pin-cite uses `paragraph N` rather than a page number for
public-domain decisions.

### Statutory citation

- `R.C. 1345.01` (preferred in Ohio briefs)
- `Ohio Rev. Code Ann. § 1345.01` (full form; rarely needed
  in-state)
- For rule citations: `Civ. R. 12(B)(6)`, `Evid. R.
  803(6)`, `Sup. R. 26`, `Prof. Cond. R. 1.7`

### Case citation

- Ohio Supreme Court: `Ohio St.3d` (third series, post-
  1980); `Ohio St.2d` (1965-1980)
- Ohio Court of Appeals: `Ohio App.3d` (third series)
- Trial court (unofficial): `Ohio Misc.2d`

### Federal court citations

Standard Bluebook conventions: `Smith v. Jones`, 538 U.S.
44, 123 S.Ct. 1234 (2003).

## Common citation errors in Ohio practice

- Citing `Ohio Rev. Code` for in-state pleadings (`R.C.` is
  preferred and shorter)
- Omitting the `paragraph N` pin-cite for post-2002 Ohio
  appellate decisions
- Citing `Ohio St.` (no series number) — must be `Ohio
  St.3d` or `Ohio St.2d`
- Citing federal-style "Section 1345.01" instead of `R.C.
  1345.01`

## Composition with other oh- skills

- `oh-quality-check` — runs this skill as part of the pre-
  filing QC
- `oh-law-references` — authoritative R.C. + rules corpus
- `oh-draft-motion` / `-declaration` — drafting skills that
  produce citations this one verifies
