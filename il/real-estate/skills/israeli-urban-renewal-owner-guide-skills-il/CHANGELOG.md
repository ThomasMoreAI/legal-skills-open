# Changelog

All notable changes to this skill.

## [1.1.0] - 2026-08-31

### Added

Closes the remaining Should-cover items from the coverage checklist. Every figure below was read
from the statute's or the regulations' own text layer, and all 33 reachable evidence snippets
re-verified at source.

- **A third track, for war-damaged buildings.** chok shikum nizkei milchama be-derech shel
  hitchadshut ironit, 2026, was not mentioned at all in earlier versions. A building the local
  authority's engineer has determined destroyed or due for demolition after war damage falls under
  it, with its own declaration process and its own disjunctive special majority: a majority of
  owners holding a majority of apartments in each of most buildings in the declared area, or at
  least four fifths of all apartments in it. This was the largest gap in the skill: an owner whose
  building was hit would previously have been answered from the wrong statute.
- **Predatory signing (hachtama pog'anit)**, s.5b of the 2006 law and s.5d of the 2008 law. Four
  circumstances in which the Memuneh may declare the transaction void, including being given
  misleading information about how many owners had already agreed. That is the most commonly
  reported pressure tactic, and it turns out to be a voiding ground rather than merely sharp
  practice.
- **The disclosure duty and the right to withdraw**, s.6 and s.6a of the 2006 law. Anyone acting
  for the developer, paid by the developer or the builder, or whose fee depends on the deal
  happening, must disclose it in the first approach and in the agreement, and must report
  non-negligible differences in temura between owners. Breach lets an owner withdraw consent even
  after signing a binding agreement, and no stipulation against the owner's favour is valid.
- **Procedural-defect cancellation at the 40 percent mark**, s.1c of the 2006 law and s.5b(e) of
  the 2008 law, distinct from the lapse clocks.
- **Prescribed form and content**, s.1e and s.5g1, under which breach can render a transaction void
  with the Memuneh able to confirm it.
- **What cancelling costs**, the 2025 regulations made under s.1d(e): a published per-apartment
  schedule, zero in several cases and topping out at 10,000 NIS on the pinui-binui track and
  1,800 NIS on the strengthening track. Stated as the published schedule with indexation and row
  selection left to the owner's advocate.
- **s.4 of the 2008 law, sixty percent for apartment enlargement**, completing that statute's
  majority ladder.
- **The guarantee vocabulary**, deliberately framed as market instruments rather than a statutory
  checklist, because none of the four core statutes names a specific instrument. What is statutory
  is only that inadequate securities make a refusal reasonable and that the transaction must carry
  an undertaking to provide guarantees. Adequacy stays out of scope by design.

## [1.0.2] - 2026-08-31

### Added

Two gaps the earlier review flagged as likely omissions, both now read from the statutory text.

- **Pre-signature duties, s.1a of the 2006 law.** A kinus of the apartment owners before the first
  transaction is signed, and a mismach ikarei hatzaa delivered to every owner in the building at
  least two weeks before that first signature, naming the temura principles, the securities offered
  and the developer's professional experience. An owner can check both against their own calendar
  without professional input, which makes it the most actionable pre-signature right in the domain.
- **The lapse clocks, per track, plus what cancellation actually does.** The two tracks carry
  DIFFERENT periods for analogous triggers: pinui-binui runs 2 years / 4 years / 4 years 6 months
  under s.1d(a), while the strengthening track runs 18 months / 3 years / 3 years 6 months under
  s.5g. Both are extended by a year in a complex of 120 units or more, and where at most 40 percent
  of the apartments are public housing the first-limb proportions count only the non-public ones.
  Most importantly, s.1d(d): once the majority has resolved and written notice is given, an owner
  who cancels is NOT treated as having breached the engagement, and the developer may claim only
  under regulations made by the Minister of Justice. The fear of a breach claim is what keeps owners
  in dead projects, so this is the provision that changes their position.

Note on sourcing: the review that prompted this reported the strengthening-track clocks only, and
did not carry the different pinui-binui periods, the 120-unit extension, the public-housing carve
out, or the cancellation mechanism. All were read from the statute before being written.

## [1.0.1] - 2026-08-31

### Fixed

Two substantive corrections found by a late domain review, both verified against the statutory
text before being applied.

- **The six-apartment rule was misread.** v1.0.0 said that for a beit meshutaf of six apartments
  or more the demolition-and-rebuild majority is computed under section 4 of the pinui-binui law
  "NOT under the plain two-thirds rule", implying a different and higher threshold. That is wrong.
  Section 4 is headed "baalut al yoter mi-dira achat" and is a DISCOUNT rule: an owner holding more
  than thirty percent of the apartments is counted as holding thirty percent plus one third of the
  excess. The two-thirds threshold is unchanged; only the counting changes. This mattered because
  most Israeli apartment buildings have six or more apartments. The bundled script encoded the same
  error and has been corrected, and it now shows the discount arithmetic via a new
  `--largest-owner-apartments` flag.
- **The refusal grounds are a named-subset import, and v1.0.0 implied they were not.** All seven
  grounds in s.2(b) apply in pinui-binui, and all seven are imported into the demolition track by
  s.5a(a2). But the new-apartment track imports **only grounds (1), (3) and (4)** via s.5(b1)(2).
  The disability grounds, the kashish alternatives menu and the 75-plus ground do not cross over;
  that track carries a separate flat prohibition at s.5(b1)(1) instead. Telling an owner on the
  new-apartment track that the kashish menu is available to them was wrong.

### Added

- Worked explanation of the section 4 discount, with an example.
- A per-track table of which refusal grounds actually apply.
- Four further entries in the checklist's "Known bad figures", including two errors that were
  present in this skill's own commissioning brief and were caught before they reached the content:
  the pinui-binui tax exemption is perek chamishi 4, not 5, and chok pinui u-vinui (pitzuyim) is
  the same statute as chok pinui u-vinui (idud mizmei pinui u-vinui), renamed by Amendment 6.

## [1.0.0] - 2026-08-31

### Added

Initial release.

Explains Israeli urban renewal from the apartment owner's side: the pinui-binui and
strengthening tracks, the statutory majorities and how they vary by track, work type and
building size, the seven grounds on which the law treats a refusal to sign as reasonable, the
statutory minimum content of the transaction, the organizer's duties to the owners, and the free
statutory ombudsman who investigates complaints of pressure to sign.

Notes on scope, which are deliberate rather than incidental:

- The skill explains and does not advise. It does not read the user's own agreement, value an
  apartment, state what compensation is owed, or rule on whether a refusal is reasonable. Those
  are reserved acts under Israeli law and belong to an advocate, a shamai mekarkein, and the
  court or the mefake'ach.
- Every statutory figure was read from the statute's own text layer rather than from secondary
  guides, which were found to be wrong at a high rate in this domain. See
  `references/domain-checklist.md`, "Known bad figures".
- Both the current and the superseded demolition-and-rebuild thresholds are documented, because
  the superseded four-fifths rule still governs matters measured under the pre-1.7.2023 regime.
- The skill states the correct position on TAMA 38: it stopped taking new permit applications,
  but Amendment 7 in 2022 widened the definition of the strengthening plan so the owner
  protections carry over to the municipal plans that succeeded it.

### Origin

Reframed from a public directory submission that asked for a tool to review a signed pinui-binui
agreement and state what compensation the owner was owed, without legal advice. That shape could
not be published. The underlying need, an owner who cannot fund private representation and does
not understand what is happening, is met here by explaining the law and routing to the free
statutory complaint channel.
