# Hidden Conditions — Reference

Loaded when the audit reaches Step 6. Surfaces material obligations that are present in the document but **placed where the reader will not naturally find them**.

This pillar is the most consequential one for consumer documents. In B2B documents it is also the pillar that overlaps most with unfair-terms / standard-terms control regimes (UCTD in the EU, AGB-Recht in Germany, Code de la consommation in France, Consumer Rights Act 2015 in the UK).

## What counts as "hidden"

A condition is hidden if the document contains it but a reader pursuing the obligation by following the document's stated organisation would miss it. There are six recurring techniques.

### 1. Obligations buried under non-suggestive headings

A material obligation appears under a heading that does not indicate its presence. Classic examples:

- An arbitration / class-action waiver clause inside a section titled "Governing law", "Miscellaneous", or "General".
- An automatic-renewal provision inside "Term", with the renewal trigger only in a sub-clause two levels deep.
- A unilateral price-change right inside "Payment", with no cross-reference from "Price" or "Term".
- A consent to international data transfer inside "Privacy" or a privacy notice incorporated by reference, when the contract body says nothing about transfers.

For each such finding, **quote the clause verbatim**, identify the heading under which it sits, and note the heading the reader would have expected it under.

### 2. "Provided that" tails

A clause states an operative rule, then in its closing words materially limits or reverses it. Typical English form: *"The Supplier shall provide [X], provided that the Customer has fulfilled [Y]"* where Y is the actual deal-breaker. French form: *"sous réserve que…"*. German form: *"sofern…", "soweit…", "vorbehaltlich…"*.

A "provided that" tail is not inherently problematic; it becomes hidden when:

- The tail introduces a material limitation that is not the natural reading of the clause head.
- The tail is set off only by a comma or semicolon, with no paragraph break.
- The tail uses negative phrasing that reverses the operative meaning ("provided that the Customer has *not*…").

Count and quote each instance. Severity is Red if the tail materially limits a right the reader would otherwise have understood to be unconditional.

### 3. Incorporation by reference of materially different terms

The document incorporates another document by reference, and that other document contains material obligations not flagged in the contract body. Examples:

- "These Terms incorporate our Acceptable Use Policy, available at [URL]" where the AUP contains the actual obligation that triggers termination.
- "Subject to our Service Level Agreement, as updated from time to time" where the SLA contains the actual remedy regime.
- "Privacy practices are governed by our Privacy Notice" where the privacy notice contains material consents.

For each such reference:
- Note the referenced document.
- State whether it appears to be attached / available / accessible.
- Note whether the contract body summarises its material terms or merely points.
- Note whether the reference includes "as updated from time to time" or equivalent — which makes the incorporated terms unilaterally variable.

Severity scales with materiality of what is incorporated.

### 4. Definitional capture

A defined term has a natural meaning, and the document's definition departs materially from that meaning. Examples:

- "Confidential Information" defined to include "any information disclosed in connection with this Agreement", which captures publicly available information by accident.
- "Affiliate" defined to include "any entity that, in the reasonable opinion of [Party], is associated with the other Party", which is a one-sided discretionary scope.
- "Force Majeure" defined to include "any event causing material adverse effect on [Party]'s business", which captures commercial misfortune the reader would not consider force majeure.
- "Service" / "Services" defined narrowly so the supplier's obligations are smaller than the reader's natural expectation.

Flag definitions that diverge materially from natural meaning. Quote the definition verbatim.

### 5. Footnotes, asterisks, and "*restrictions apply*" patterns

In documents with significant marketing or consumer-facing framing, footnotes and asterisks frequently carry material obligations:

- *"Free trial — cancel anytime."* with a footnote that limits cancellation to a 24-hour window.
- *"Refund available."* with a footnote restricting to a specific payment method.
- *"Worldwide service."* with a footnote excluding a list of jurisdictions.

Note every footnote / asterisk that limits an operative promise. Severity Red if the limitation contradicts the headline.

### 6. Modifications-by-notice clauses without notice mechanics

The contract reserves a right to modify terms unilaterally, but does not specify a notification mechanism the reader can practically monitor:

- "We may amend these Terms at any time. The current version is available at [URL]."
- "These Conditions may be updated. Continued use of the Service constitutes acceptance."
- "Wir können diese AGB jederzeit ändern. Die aktuelle Fassung gilt."

These provisions hide future obligations rather than current ones. Flag them, note that they are widely scrutinised under unfair-terms regimes (UCTD Annex point 1(j), Consumer Rights Act 2015 Schedule 2 paragraph 13, AGB-Recht § 308 No. 4 BGB).

## Severity calibration

For each finding, severity depends on **what** is hidden, not just **that** it is hidden:

- **Red.** The hidden condition materially affects price, term, termination, dispute resolution, jurisdiction, liability cap, or a fundamental consumer right.
- **Amber.** The hidden condition materially affects rights of practical importance but not the headline economics.
- **Yellow.** Hidden but the condition is itself non-material or genre-typical.
- **Green.** Section contains no hidden conditions.

## Pillar score

The hidden-conditions pillar does not lend itself to formulaic component-averaging — one well-hidden material clause matters more than a dozen minor placement issues. Use the following rule:

| Severity profile | Pillar score |
| --- | --- |
| No Red findings; ≤ 2 Amber; rest Yellow / Green | 85–95 |
| No Red; 3–5 Amber | 65–80 |
| 1 Red **or** 6+ Amber | 40–60 |
| 2 Red | 25–40 |
| 3+ Red | 0–25 |

Set the pillar score within the band based on the materiality of the highest-severity finding.

## What to report in the pillar section

For each finding, report:

| # | Technique | Quote (verbatim) | Location | Severity | Note |
| --- | --- | --- | --- | --- | --- |
| 6.1 | Buried obligation | "Disputes shall be resolved by binding arbitration administered by [X]…" | Clause 24.7 (under "Miscellaneous") | Red | Arbitration clause under abstract heading; reader following the contract's table of contents will not find this |
| 6.2 | "Provided that" tail | "The Customer shall be entitled to the refund described above, provided that the Customer has notified the Supplier within 48 hours of the relevant event" | Clause 12.3 | Red | Tail introduces a 48-hour notification cliff not signalled in the operative clause head |
| 6.3 | Modification-by-notice without mechanic | "We may update these Terms at any time…" | Clause 19.1 | Amber | No notification mechanism specified; widely scrutinised under unfair-terms regimes |

End with a synthesis paragraph naming the technique(s) most heavily used and the impact on the reader.

## Cross-cutting notes

- Hidden conditions and statutory duplication are sometimes related: a clause that recites a mandatory statutory right may **also** be drafted to bury an additional restriction. Flag the same passage under both pillars only if the restriction is genuinely a separate finding.
- This pillar is jurisdiction-agnostic in detection but jurisdiction-sensitive in materiality assessment: a unilateral modification clause may be standard practice in one jurisdiction and outright unenforceable in another. Note the materiality framing but do not opine on enforceability — that is outside this skill.
