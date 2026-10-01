# Domain Coverage Checklist - Israeli Tender Proposal Builder

Generated: 2026-09-15. Scope: a BIDDER-side builder of Hebrew proposal packages for Israeli public
tenders, both state bodies (חוק חובת המכרזים and תקנות חובת המכרזים) and local authorities
(תקנות העיריות (מכרזים) and the parallel council orders). Statute quotes and URLs live in
`evidence.json`; this file lists what the skill must cover.

## Must cover (core)

- [x] Identify the regime first: state body vs local authority vs RMI land tender (routed away).
  Municipal tenders follow their own regulations; state thresholds and the state electronic box do
  not apply as written.
- [x] Municipal amounts are CPI-linked and move monthly (municipal reg 2): compute, never quote a
  remembered figure. Same rule for state thresholds (verify on mr.gov.il).
- [x] Threshold conditions: statutory (Takana 6(a)) vs discretionary (Takana 6(b)), copied verbatim,
  one compliance row each, Blocker stops the work.
- [x] Reservations and conditional bids: a fundamental reservation or basic change disqualifies a
  municipal bid (reg 20(ג)); the state regulations have no equivalent, but state tender documents
  commonly reserve the right to disqualify or ignore reservations. Doubts go to clarification
  questions.
- [x] Declarations under חוק עסקאות גופים ציבוריים: s.2ב conviction affidavit (stricter look-back for
  service contracts), s.2ב1 disability-representation affidavit, bookkeeping certificate.
- [x] Workers' rights affidavit for labor-intensive contracts (Takana 6(a)(4)).
- [x] No-coordination declaration; bid coordination is a restrictive arrangement under
  חוק התחרות הכלכלית.
- [x] Affidavit formalities: sworn before a lawyer, dated on or before the submission deadline.
- [x] Bid guarantee: amount, autonomous type, validity, template wording; forfeiture power.
- [x] Israeli-product preference as a full table: 15% Israeli goods, 20% Gaza-envelope goods, 10% for
  exporting government companies or units, 50% textiles in specified security-body tenders, and the
  split-tender rule above 30 million NIS.
- [x] Tie-breakers: women-controlled business (s.2ב of the Mandatory Tenders Law) and reserve-service
  business (s.2ד).
- [x] Clarification answers are written and binding; do not rely on oral statements.
- [x] Trade-secret marking in the bid, because losers may inspect the winning bid (state reg 21(ה)(1)
  within 30 days of notice; municipal reg 22(ט)).
- [x] Submission path: electronic box vs physical box, deadline to the minute.
- [x] After award: administrative petition to the district court (Administrative Courts Law, First
  Schedule item 5), without delay and, absent another deadline, within 45 days (procedure regs, reg
  3(ב)). Routing only, refer to a lawyer.

## Should cover (advanced)

- [ ] Abnormally low bids: be ready to justify the price if the committee asks (no regulation cited;
  practice and tender documents).
- [ ] Threshold conditions tested as of the submission date; experience must be the bidder's own
  (case law, not yet sourced).
- [ ] Quality/price weighting and two-stage evaluation mechanics.
- [ ] Guarantee extension requests and forfeiture on withdrawal.
- [ ] Consortium and subcontractor rules; guarantee issued in the bidder's own name.
- [ ] בעלי זיקה corporate-structure mapping for the affidavits.
- [ ] Government-company tenders under their own procurement rules.

## Out of scope (explicit, with rationale)

- Drafting the administrative petition itself: litigation reserved to advocates. The skill states the
  route and the deadline and routes the user out (re-checked 2026-09-15: users ask, and the deadline is
  now stated rather than silent).
- Buyer-side tender drafting and committee decisions: different user.
- RMI land-allocation tenders: `israeli-land-tenders`.
- Defense and classified procurement: separate regime.
- Recommending a bid price: collusion and advice risk; the skill gives market intelligence only.
- Private commercial RFPs not subject to the Mandatory Tenders Law.

## Authoritative sources

- Mandatory Tenders Law and regulations (Nevo, cited in SKILL.md Reference Links).
- Israeli-product preference regulations (Nevo and Wikisource).
- תקנות העיריות (מכרזים) (Wikisource).
- חוק עסקאות גופים ציבוריים (Wikisource).
- Administrative Courts Law and its procedure regulations (Wikisource).
