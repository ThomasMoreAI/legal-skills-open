# Domain Coverage Checklist, israeli-tabu-extract-decoder

Generated: 2026-08-11. Every statutory row was verified against the source's own text layer on
he.wikisource.org, sliced directly from the rendered page so each quoted snippet is contiguous.

## Scope decision on fees and ordering: REOPENED 2026-09-19

The first release stated no fee, no ordering procedure and no printed-copy rule, because the registry
pages could not be read first-hand. On 2026-09-19 the service page
(https://www.gov.il/he/service/land_registration_extract) rendered in a real browser, and the fee
schedule was read in the consolidated regulations (wikisource) with the 2026 figures. So the skill now
states the three extract types, the online route (`מקרקעין ברשת`), the digital-original rule, and the
2026 fees (18 NIS electronic, 88 NIS certified paper, 154 NIS paper consolidated), each with its year.
Fees are indexed every 1 January (תקנה 2(ב)): re-read item 7 of the schedule each cycle.

## Must cover (core)

- [ ] `סעיף 125`: conclusive evidence for settled land, prima facie only for unsettled. Stated BEFORE
      anything on the page is characterised as established.
- [ ] `סעיף 124`: the registers are public, which is why anyone may obtain an extract for land in
      Israel proper.
- [ ] `סעיף 7`: a transaction is completed by registration; an unregistered transaction is an
      undertaking. This is the conceptual spine of the whole skill.
- [ ] `סעיף 3`: lease over five years is `חכירה`, over twenty five years `חכירה לדורות`. A public body
      as owner with the resident as `חוכר לדורות` is a normal registered right.
- [ ] `סעיף 5`: an easement carries no right to possess.
- [ ] `סעיף 85`: a later transaction has no effect against a purchaser at the mortgage's execution
      sale.
- [ ] `סעיף 86`: a redeemed rank may be refilled by a later mortgage where its terms so provide, so a
      discharge does not by itself free the rank.
- [ ] `סעיף 126`: a caveat records a WRITTEN undertaking to transact or refrain.
- [ ] `סעיף 127(א)`: the blocking effect while the caveat stands unerased.
- [ ] `סעיף 127(ב)`: the shield against later attachment, bankruptcy, winding up and receivership,
      INCLUDING the avoidance carve-out that most summaries drop.
- [ ] A caveat is not ownership, not a registered transaction, and not a lien.
- [ ] `סעיף 128`: notes conditioning a dealing on a third party's consent, and that nothing can be
      registered without that consent.
- [ ] `סעיף 57`: the share in the common property is the floor-area ratio in hundredths unless the
      bylaws say otherwise, which is why the fraction rarely matches intuition.
- [ ] `סעיף 62`: registered bylaws bind later owners, so a promised parking space belongs to the unit
      only if the register says so.
- [ ] `הצמדה` read per attachment, checking that what is being sold is attached to THIS sub-parcel.
- [ ] The identity block: `גוש`, `חלקה`, `תת-חלקה`, and that a sub-parcel number is not an apartment
      number.
- [ ] The `שטח` is the registered area on its own basis, not the marketed area.
- [ ] The extract speaks as at its production date.
- [ ] Ownership arithmetic: shares summing to the whole, every intended seller present, and a
      deceased registered owner as a transfer blocker.
- [ ] The registration regimes, and that a very large share of Israeli homes are not registered in
      the owner's name in this register. Naming the regime and the substitute document is a core
      output, not an edge case.
- [ ] What an extract does NOT contain: planning rights, permits, violations, debts, physical
      condition, unregistered tenancies, price.
- [ ] The refusal boundary: the skill never concludes that title is good, that an entry is harmless,
      or that it is safe to sign.

## Should cover (advanced / edge cases)

- [ ] Notes for restricted legal capacity and court-ordered notes, and that the register can carry
      further note types prescribed by regulation, so an unrecognised entry is routed rather than
      guessed.
- [ ] Registered versus unregistered leases, and that a sitting tenant under an unregistered lease is
      invisible on the extract.
- [ ] That a standard extract shows the current position, so a released attachment or a discharged
      mortgage will not appear on it.
- [ ] The Judea and Samaria register as a separate system with different categories and different
      access rules, routed rather than described.
- [ ] Ordering the underlying deed or condominium file when an entry is cryptic.

## Out of scope (explicit, with rationale)

Re-litigated 2026-09-19: "ordering an extract" was split. Telling the user HOW to order is now in
scope (captured); ordering it FOR them stays out (payment and identity). Every other row is kept: each
is either a reserved profession, a sibling skill, or absent from the extract.

- Valuation, comparable sales, price medians: `israeli-property-appraisal`, and a valuation is
  reserved to a licensed appraiser.
- Purchase tax, betterment tax, rental agreements, general transaction guidance: `israeli-real-estate`.
- Defects in a new apartment from a developer: `israeli-home-defect-report`.
- **Whether title is good, whether an entry defeats this deal, whether to sign.** Practice of law.
- Drafting a sale agreement, an irrevocable power of attorney, or the wording of an undertaking.
- Planning rights, building permits, violations, tama 38 and evacuation-reconstruction eligibility.
  None of these appears on an extract.
- Ordering an extract on the user's behalf, which needs payment and identity.
- Chasing a developer or a housing company on the user's behalf.

## Known bad claims circulating in the wild

- "A caveat makes you the owner." It records an undertaking. `סעיף 7` still requires registration to
  complete a transaction.
- "The register is always conclusive proof." Only for settled land (`סעיף 125(א)`); prima facie
  otherwise (`סעיף 125(ב)`).
- "If it is not in the tabu, you do not own it." Long leases from a public body, land-authority
  management, and housing-company registration are all real regimes.
- "The sub-parcel number is the apartment number." They coincide often enough to be dangerous.
- "The first mortgage was paid off, so rank one is free." `סעיף 86` allows a vacant rank to be
  refilled.
- "The extract shows building violations, debts, or the real apartment size." It shows none of these.
- A fee quoted without its year. Fees are index-linked and change every 1 January; the skill quotes 2026 figures with the year.

## Open items for the next update

1. DONE 2026-09-19: fee, extract types, ordering route and printed-copy status added (see top).
2. The property-activity alert service. Neither its cost nor its effectiveness is stated anywhere in
   this skill, because neither could be verified first-hand; do not describe it as free, and do not
   rank it against other precautions, until a readable registry page says so.
3. The Judea and Samaria register's extract categories and standing rules, from a readable source.
4. PARTLY DONE 2026-09-19: s.132(a) deletion grounds are stated (court order, or the Registrar
   satisfied of consent or a lapsed ground, after notice). The procedure for applying is still routed.
5. Deferred 2026-09-19 (unverified first-hand): the ILA online rights-confirmation service and fee; the
   Ministry of Construction new-build registration-status service; the Corporations Authority pledges
   search route and fee; the Judea and Samaria extract service URL.

## Authoritative sources

- https://he.wikisource.org/wiki/חוק_המקרקעין
- https://he.wikisource.org/wiki/תקנות_המקרקעין_%28אגרות%29
