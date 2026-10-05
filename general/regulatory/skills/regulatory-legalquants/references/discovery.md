# Discovery — finding the instruments before proving them

Method version: **discovery/v1 (2026-09-06)**. Record this line in every
`check` note, so a matter researched under v1 can be rerun when the method
improves, rather than merely re-checked for amendments to laws already known.

The spine proves the text you fetched. It can never prove you fetched the right
set of instruments — the false negative in a `check` lives entirely in the
selection step, before the first fetch. This file is the method for that step.
It does not promise exhaustive research; it replaces unaided recall with a
search surface that can be audited, and it makes the uncovered ground visible.

Discovery is a separate phase with its own gate. A `check` note whose quotes all
verify is still not complete unless the discovery receipt below is in it.

## 1. Model the conduct, then generate candidates

Decompose the activity on these dimensions. Every populated dimension generates
candidate instruments; a dimension you skip is a branch nobody searched.

- **Actors** — manufacturer, developer, importer, distributor, operator,
  controller, processor, employer, professional, service provider.
- **Objects** — hardware, software, data, communications, money, chemicals,
  energy, controlled items, regulated services.
- **Actions** — manufacture, import, collect, infer, transmit, store, decide,
  move, advise, advertise, sell, update, repair, dispose.
- **Affected people** — purchasers, users, bystanders, children, workers,
  vulnerable people, people who have not consented.
- **Places** — private property, public space, workplaces, regulated
  facilities, interstate and international boundaries.
- **Lifecycle** — development, sourcing, manufacture, importation,
  certification, marketing, sale, activation, operation, updating, repair,
  disposal. Duties cluster at stages the client is not thinking about yet.
- **Failure modes** — injury, surveillance, discrimination, fraud,
  interference, compromise, loss of control, environmental harm, denial of
  service. The regime that catches a product is often the one written for its
  worst day.

## 2. Search by consequence as well as subject

Subject searches find the regime everyone knows about. Consequence questions
find the one housed under a different doctrine:

what can prohibit manufacture · prevent importation · require approval before
sale · prohibit marketing · force reporting, remediation or recall · restrict
operation · require notice, consent, access, correction, deletion or
portability · create a private cause of action · impose civil or criminal
penalties · change the legal classification after a software update.

## 3. Regulators before instruments

Name every body with a plausible connection to the conduct before settling on
laws: product and market regulators; communications and infrastructure;
trade, customs, export-control and sanctions authorities; privacy,
consumer-protection and civil-rights regulators; sector regulators; state
attorneys general and specialist state agencies; local licensing authorities.

For each plausible regulator, look beyond codified law to the official sources
that change without codification: prohibition and covered-entity lists,
licensing and authorisation registers, binding determinations, emergency and
stop-sale orders, product recalls, exemptions and conditional approvals, and
pending rules that will be operative by the activity date. Record the access
date for every dynamic source consulted — a sanctions list checked in June is
a June fact.

## 4. Rules, exceptions, and alternate pathways — searched separately

For every candidate regime: the general rule; its scope definitions;
exclusions and exemptions; preemption; conditional approvals; grandfathering
and transition rules; treatment of previously authorised conduct; component,
affiliate, ownership and control attribution; future-effective amendments.
Finding the rule without its exemption produces a false positive; finding
neither produces the invisible kind.

## 5. Optimise discovery for recall

At this stage a false positive is cheap — the spine will kill it against the
official text. A false negative is invisible forever. A candidate proceeds to
the spine when it plausibly could: block market access; impose criminal
liability; require prior authorisation; create mandatory reporting,
remediation or recall duties; carry a private right of action or statutory
damages; affect a substantial part of the planned market; or apply under a
factually plausible test the supplied facts leave unresolved. Rejected
candidates are recorded with the reason — a rejection is a finding.

## 6. The discovery coverage receipt

The `check` note carries this table. It discloses the search surface, not just
the instruments found. Statuses: **complete** / **partial** / **unresolved** —
and for feature-dependent regimes, **resolved** / **unresolved**.

| Dimension | Status | Evidence |
|---|---|---|
| Actors and roles | | roles considered |
| Lifecycle | | stages reviewed |
| Regulators | | authorities considered |
| Geographic perimeter | | jurisdictions examined |
| Pre-market permissions | | registers and approval systems searched |
| Dynamic official sources | | sources and access dates |
| Future-effective law | | research cutoff and target date |
| Feature-dependent regimes | | missing factual triggers |

Never collapse a branch into "the regulator was reviewed generally". Materially
different types of authority get separate entries. A row you did not work gets
**unresolved**, not silence.

`scripts/check_receipt.py <note>` audits the finished table against this
section, section 7 and section 8. It is the same kind of gate as the quote
check: it proves the receipt is whole, and says nothing about whether the
research behind it was right.

## 7. Four kinds of nothing

"Nothing found" is never delivered unqualified. Every negative states which of
these it is:

1. **Expressly outside scope** — an instrument contains an applicable
   exclusion. Quote it; it verifies like any other quote.
2. **Test not met on supplied facts** — responsive provisions exist, an
   element is absent. Name the element.
3. **No responsive instrument identified after specified searches** — a
   bounded result. The bound is the searches in the receipt, and the sentence
   says so.
4. **Not investigated** — no inference permitted. This is a receipt row, not a
   footnote.

The difference between 3 and 4 is the difference between research and its
absence, and collapsing them is how incomplete research gets delivered as a
legal negative.

## 8. The omission challenge

Before delivery, put the coverage receipt and the one-line conduct description
— never the draft answer — to a fresh-context reviewer (a subagent where the
host has one; a cold re-read against sections 1–4 of this file where it does
not) with one question: *name the regulator or regime most likely to be
missing.* Record the answer in the note, either as a new branch worked or as a
named gap. An unanswered challenge is a gap in the receipt.

## 9. Future conduct

A `check` is dated at launch, not at research. Distinguish law effective on the
research date; enacted law effective by the target date; final rules with
future compliance dates; approvals required before launch; dynamic lists that
may change before launch; sunset and transition provisions; and pending
measures that are not yet law. The note states a mandatory refresh date for
every volatile source and launch-critical question — a `check` against a
sanctions list has the shelf life of the list.
