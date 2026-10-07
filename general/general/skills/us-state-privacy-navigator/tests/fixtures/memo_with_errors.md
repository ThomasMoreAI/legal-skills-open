# Test Memo — Intentional Citation Errors

This file is used to test the citation auditor. It contains intentional errors
the auditor should detect and flag.

## Section 1 — Missing citations

The CCPA imposes opt-out obligations on covered businesses. This sentence has no citation and should be flagged as missing supporting authority.

The Texas TDPSA requires sensitive-data consent. This sentence also has no citation.

## Section 2 — Bad citation formats

Under Cal. Civ. Code § 1798.999999 controllers must honor opt-out preference signals.
[The section number is implausible and should fail the section-existence check.]

The Virginia VCDPA at Va. Code § 999.999 prohibits sale of children's data.
[Implausible section number for VA Code]

## Section 3 — Properly cited claims (control)

The CCPA establishes a private right of action for security breaches at Cal. Civ. Code § 1798.150.

Texas's comprehensive privacy law is the Texas Data Privacy and Security Act, Tex. Bus. & Com. Code § 541.001 et seq.

Colorado's Privacy Act applies at thresholds set forth in Colo. Rev. Stat. § 6-1-1304.

## Section 4 — Orphaned citation marker

This sentence has a [citation needed] marker that should be flagged.
