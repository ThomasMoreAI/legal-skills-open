---
name: poland-protection-referral-xopoko
title: Poland Protection Referral
description: Protection referral. Use for asylum, international or temporary protection, unsafe return, or loss of protection in Poland.
author: Xopoko
author_url: https://github.com/Xopoko/poland/tree/main/skills/poland-protection-referral
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: pl
practice: immigration
language: en
---

# Poland Protection Referral

Use for international protection, temporary protection, unsafe return, loss of
protection, or uncertainty about the competent protection authority. This skill
provides official-source referral and safety-oriented next steps, not asylum
strategy or a credibility assessment.

First check for immediate danger, detention, removal, coercion, or an imminent
deadline. Route urgent safety needs to `poland-emergency-rights` without delaying
for documents or immigration intake. Otherwise ask only for non-identifying
route categories such as current country, stated status, protection type if
known, locality, and whether an official decision or deadline exists.

For a reported PESEL UKR or CUKR matter, classify these as separate routes:

- `udsc-ukraine-status-transition-2026` owns the general 5 March 2026 transition.
  It does not make every extension or exception applicable to every Ukrainian
  citizen or every UKR-status holder.
- `udsc-cukr-procedure` owns the CUKR route. At the 28 August 2026 source
  snapshot, the page says the electronic MOS procedure opened on 4 May 2026 and
  gives a current filing window ending 4 March 2027. Recheck the page before
  action and verify the source-defined applicant group, active-status dates,
  continuity, child branch, pending-case interaction, voivode, and current
  consequences. Never decide eligibility from the label PESEL UKR alone.
- `udsc-pesel-ukr-passport-update-2026` is the competent UdSC notice for the
  declaration-based 31 August identity-confirmation group. The broader
  `gov-pesel-ukr-passport-update-2026` outreach notice also names new or changed
  passports and children whose registration lacked a passport. The two pages
  differ in affected-group scope and in the certainty of the stated status
  consequence; preserve the route's explicit conflict gate instead of choosing
  one formulation. Use
  `sejm-ukraine-transition-act-2026` to classify the deadline: Article 25 sets
  31 August 2026 for identity confirmation when PESEL was assigned on the basis
  of a declaration, while Article 26 gives specified other original-document
  situations a separate 60-day period from travel-document issuance. Do not
  present either rule as a universal deadline for every PESEL UKR holder.
  Verify the original registration basis, whether identity was already
  confirmed, and current gmina or city-office instructions; treat a near
  deadline or unclear record as an escalation.

Do not merge the 31 August PESEL-record deadline with the CUKR application
window. Ordinary PESEL administration belongs to `poland-identity` after the
time-sensitive UKR-status branch has been classified.

Use current Office for Foreigners and other competent official or support sources
returned by the registry. Distinguish official observation, user-reported fact,
and unresolved legal judgment. Give the authority, source, questions to ask,
deadline-preservation step, and qualified legal-aid route. Do not predict an
outcome, assess evidence credibility, or prepare a personalized protection
claim.

If the user requests portal or correspondence assistance, apply
`../../references/automation-playbook.md` without delaying immediate safety or
legal-aid referral. The user authenticates, signs, and attests to the truth of a
protection account. For CUKR, a caller-owned tool may resume after the user's
authentication to inspect only the explicitly scoped record and prepare
administrative fields. Account creation, server-side draft creation, upload,
download, payment initiation, booking, or submission requires fresh action-time
confirmation; the user personally performs every signature and declaration.
For a PESEL UKR passport-data update, the agent may locate the competent gmina,
prepare a checklist, and prepare an appointment with confirmation, but the user
personally presents identity documents and authorizes any official-record
change. Do not turn operational assistance into a credibility assessment or
individualized asylum strategy, and report completion only from a visible
official receipt or confirmed office result.

Ordinary stay and residence belongs to `poland-stay-residence`; refusals and
review routes belong to `poland-appeals-review`. Read
`../../references/immigration-status-map.md` and
`../../references/emergency-and-escalation.md`.
