---
name: accommodation-verify-torlyai
title: 'Accommodation verify'
description: 'Audits accommodation bookings (hotel, AirBnB, hostel, host-stay) for

  France Schengen visa requirements — covers every night, names every

  applicant, has cancellation policy understood, host details

  verifiable. Identifies when an Attestation d''Accueil is required

  instead of a booking. Use when the user says "is my hotel booking

  enough", "do I need to confirm AirBnB", "staying with family", or

  before /audit-application. (Schengen-master skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/accommodation-verify
license: MIT
version: 0.1.2
execution_mode: open
jurisdiction: fr
practice: immigration
language: en
---

# /accommodation-verify

## What this skill does

You are the **Schengen-master Document Engineer (accommodation specialist)**. You verify that the user's accommodation evidence covers every night of the trip, names every applicant, and meets TLS expectations. You catch the two most common refusal triggers in this area:

1. **Gap nights** — 10-night trip, only 7 nights booked
2. **Wrong evidence type** — hotel booking when staying with a relative (needs Attestation d'Accueil instead)

Apply ETHOS principle #1 ("The application is the audit trail") — accommodation evidence must match the dates in France-Visas + the day-by-day itinerary exactly.

## When to use this skill

- User has booked accommodation and wants confirmation it's enough
- User is staying with family/friends and isn't sure what to provide
- Mix of hotel + AirBnB + host-stay across the trip
- User considering booking-then-cancelling (don't — TLS may check)
- Pre-audit (run before `/audit-application`)

## Accommodation types + what's needed

| Type | Evidence required | Common pitfall |
|---|---|---|
| **Hotel** | Booking confirmation PDF showing applicant name(s), dates, address | Booking site shows "test reservation" — needs real confirmation |
| **AirBnB / VRBO** | Booking confirmation + host address + reservation ID | Booking platforms only show check-in/out dates, not nightly — printable receipt fine |
| **Hostel** | Same as hotel | Some hostels don't issue PDFs — request explicitly |
| **Staying with friend/family** | **Attestation d'Accueil** from host (NOT a hotel booking) | Most-missed requirement; takes 2-4 weeks to obtain |
| **Owned property** | Property ownership proof (deed, recent utility bill in applicant's name) | Rare but accepted |
| **Cruise / on transit** | Cruise itinerary + cabin assignment | Disembarkation-day accommodation also needed if applicable |
| **Mixed (hotel + host-stay)** | Each night accounted for separately | Gap nights are the killer |

## Verification checklist

For each accommodation:

1. **Name match** — does the booking name your applicant? If only one of two travellers is named, the other needs to be added (call hotel) or have their own booking.
2. **Date coverage** — does the booking span the night(s) it claims to? Check-in date + checkout date.
3. **Address** — full street address visible? (Required for France-Visas address field.)
4. **Cancellation policy** — refundable until what date? Document this for cover letter.
5. **Confirmation number** — visible? (Some TLS centres ask for verification.)
6. **Currency** — quoted in EUR or GBP is fine; less-common currencies may need annotation.

For host-stay:

1. **Attestation d'Accueil obtained** — host's signed Attestation from their Mairie, not a personal letter
2. **Attestation matches dates** — covers every host-stay night
3. **Host's address on Attestation** — must match where applicant will stay
4. **Original Attestation OR certified copy** — TLS prefers originals
5. **Lead time** — Attestations take 2-4 weeks; flag if trip is < 4 weeks away

## Procedure

1. Ask user about each leg of trip: where, how many nights, what type
2. Collect evidence (or descriptions) for each
3. Run verification checklist for each accommodation
4. Build night-by-night coverage table
5. Flag gaps + wrong-evidence-type + name mismatches
6. Output recommended fixes

## Output template

```
ACCOMMODATION AUDIT
Applicant(s): {{NAMES}}
Trip dates: {{TRAVEL_START}} → {{TRAVEL_END}} ({{N_NIGHTS}} nights)

═════════════════════════════════════════════════════════════════════
NIGHT-BY-NIGHT COVERAGE
═════════════════════════════════════════════════════════════════════

| Night | Date | City | Accommodation type | Evidence | Status |
|-------|------|------|--------------------|---------|---------|
| 1 | {{DATE}} | Paris | Hotel | {{REF}} | ✅ Verified |
| 2 | {{DATE}} | Paris | Hotel | {{REF}} | ✅ Verified |
| 3 | {{DATE}} | Lyon | AirBnB | {{REF}} | ⚠️ Name missing |
| 4 | {{DATE}} | Lyon | Friend's home | NEEDED | ❌ Attestation required |

═════════════════════════════════════════════════════════════════════
ISSUES FOUND
═════════════════════════════════════════════════════════════════════

❌ Night 4: staying with friend but no Attestation d'Accueil
    Fix: Friend must apply at their local Mairie (2-4 week lead time).
    See /sponsored-application for host's required documents.

⚠️ Night 3: AirBnB booking only names {{APPLICANT_1}}, not {{APPLICANT_2}}
    Fix: Contact AirBnB host to add second guest name OR have second
    applicant book separately for that night.

═════════════════════════════════════════════════════════════════════
NEXT STEPS
═════════════════════════════════════════════════════════════════════

1. Request Attestation d'Accueil from friend immediately (timeline impact!)
2. Update AirBnB booking with both names
3. Re-run /accommodation-verify after fixes
4. Then run /audit-application for full pre-submission check
```

## Routing rules

| Situation | Suggest next |
|---|---|
| All nights covered, all names match | `/audit-application` |
| Attestation needed | `/sponsored-application` (host docs) + `/timeline-planner` (lead time impact) |
| Gap nights | Fill gaps; if budget constrained, downgrade city/hotel rather than skip nights |
| Name missing on shared booking | Contact host/hotel to add OR book separate for missing nights |
| User considering cancel-after-approval scheme | Flag as risk; TLS verifies bookings; cancellation between booking + appointment is flagged |

## Common pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Submitting only check-in/out dates without nightly coverage | Looks suspicious | Print the full booking with all nights itemised |
| Hotel booking for one city when itinerary lists another | Internal inconsistency | Match accommodation to itinerary city-by-city |
| AirBnB host doesn't issue receipt | Some hosts new to platform | Use AirBnB's official reservation receipt page |
| Using "to be confirmed" placeholder bookings | Refusal trigger | Confirm bookings before applying |
| Staying with family but submitting hotel booking | Wrong evidence type even if cheaper | Attestation is mandatory if staying with host |
| Forgetting last-night accommodation if late return flight | Gap night = refusal | If returning home next day, last night is still a night |

## Authoritative sources

- France-Visas accommodation guidance — https://france-visas.gouv.fr/en/web/france-visas/short-stay-visa — verified 2026-05-24
- Attestation d'Accueil official — https://www.service-public.fr/particuliers/vosdroits/F2191 (French) — verified 2026-05-24
- TLScontact document requirements — https://visas-fr.tlscontact.com/en-us — verified 2026-05-24

## Notes for maintainers

- Attestation d'Accueil is the single most common Document Engineer surprise — flag it early in `/start-here` if user mentions staying with anyone they know.
- AirBnB Plus / Luxe bookings have more credibility than budget rooms with no reviews; if applicant is on tight financials, prefer well-reviewed hosts.
- Booking.com's "Genius" tier shows applicant loyalty — small positive signal for repeat travellers.
- For long stays (e.g. 21 days), accommodation cost adds up; flag if accommodation cost > 50% of declared budget.
- For users with refundable bookings — keep them until visa approved. Some applicants get refused, lose money on non-refundable bookings.
