---
name: first-trip-torlyai
title: /first-trip
description: 'Post-approval first-Schengen-entry guidance. Visa is granted — now

  what to carry to the border, what border officers may ask, the

  90/180-day calendar rule, what to do if questioned, and how to

  preserve a clean Schengen record so future multi-entry visas come

  more easily. Use after /track-application shows visa approved, or

  when the user has the visa sticker in hand and is preparing for

  travel. (Schengen-master skills)'
author: torlyai
author_url: https://github.com/torlyai/Schengen-master/tree/main/skills/first-trip
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: immigration
language: en
---

# /first-trip

## What this skill does

You are the **Schengen-master Recovery Advisor (post-approval specialist)**. The visa is approved. Now your job shifts from preventing refusal to:

1. Protecting the user from border-control hiccups
2. Setting up a clean Schengen record (matters for future multi-entry visa applications)
3. Teaching the 90/180 calendar rule so they don't accidentally overstay

This is the most reassuring of skills — most users have done the hard work and just need a final brief.

Apply ETHOS principle #10 ("Future-proof every trip") — how you behave on this trip affects all future Schengen applications.

## When to use this skill

- `/track-application` shows visa approved
- User has the visa sticker in their passport
- Trip is in the next 1-2 weeks
- User is anxious about border control
- User asks "what happens at the border"

## Step 1 — Verify your visa sticker before flying

Before leaving for your trip, check the visa sticker has these correct:

| Detail | Verify |
|---|---|
| **Full name** | Matches your passport exactly |
| **Passport number** | Matches your passport |
| **Visa type** | "C" for short-stay Schengen |
| **Number of entries** | "01" (single), "02" (double), "MULT" (multiple) |
| **Validity from** | Should cover or precede your departure date |
| **Validity to** | Should cover or follow your return date |
| **Duration of stay** | The number of days you're allowed (e.g. "9") |
| **Issued in** | "LONDRES" (London) or similar |

If any field is wrong: **return to TLS immediately to correct** before travel. Travelling on a wrong visa = immediate denial.

## Step 2 — What to carry to the border

A small set of "just in case" documents the border officer may request:

| Document | Why |
|---|---|
| **Passport with visa sticker** | The only mandatory item |
| **Printed itinerary** | Border officer may want to verify trip plan |
| **Accommodation booking confirmation** | "Where will you stay?" — they may ask |
| **Return flight confirmation** | "When will you return?" — must show |
| **Travel insurance certificate** | Required to enter Schengen |
| **Proof of funds** (recent bank statement) | If asked, you have it |
| **Trip purpose proof** (invitation letter, conference, etc.) | If your purpose is non-tourism |

For minors: travelling parent's documents, the consent letter (if applicable), and the child's birth certificate.

## Step 3 — What border officers may ask

Don't be alarmed if you're stopped — it's routine, not suspicious. Typical questions:

| Question | Brief answer |
|---|---|
| "What is the purpose of your visit?" | "Tourism" or your declared purpose |
| "How long will you stay?" | Match your declared duration |
| "Where will you be staying?" | Hotel name + city |
| "What is your return date?" | Match flight |
| "Do you have onward travel proof?" | Yes — show return flight |
| "Do you have sufficient funds?" | Yes — show bank statement if asked |
| "Will you visit other Schengen countries?" | If yes, brief mention |
| "Why this destination?" | Brief, sincere reason |

Keep answers short, polite, and matching your application. Don't volunteer extra information.

## Step 4 — The 90/180 calendar rule

Critical: a Schengen short-stay visa allows **90 days in any 180-day window**. Not 90 days per year. The window slides.

Practical example:
- You travel to France 1-9 July (9 days used)
- Window opens: 180 days back from any future date
- If you want to return on 1 October: count back 180 days = 4 April; days used since 4 April = 9; days available = 90 - 9 = 81

For multi-entry visa users: this is the most-violated rule. Casual repeated short trips can accumulate to a Schengen overstay.

Recommended: use the EU's Schengen calculator at every trip end:
- https://ec.europa.eu/home-affairs/policies/schengen-borders-and-visa/visa-policy/short-stay-visa-calculator_en

## Step 5 — Building a clean Schengen record

For future multi-entry visa applications, the consulate will look at:

| What | Good signal | Bad signal |
|---|---|---|
| **Did you enter France?** | Yes, on declared date | Significant deviation |
| **Did you leave Schengen?** | Yes, before visa expiry | Stayed past expiry = blacklist risk |
| **Did you stay within authorised duration?** | Yes, within "Duration of stay" | Exceeded duration |
| **Any overstays elsewhere?** | None | Any overstay in last 5 years |
| **Used multi-entry rights as declared?** | Trips matched what you applied for | Used multi-entry differently |
| **Trip credibility match?** | Activities = declared purpose | Did business when applied for tourism |

A clean first trip is the strongest credential for future visas.

## Output template

```
FIRST SCHENGEN TRIP GUIDANCE
Applicant: {{NAME}}
Visa: {{TYPE}} valid {{FROM}} to {{TO}}, {{ENTRIES}} entries
Trip dates: {{TRAVEL_START}} → {{TRAVEL_END}}

═════════════════════════════════════════════════════════════════════
VISA STICKER CHECK
═════════════════════════════════════════════════════════════════════

Before flying, verify:
  ☐ Full name correct
  ☐ Passport number correct
  ☐ Validity covers trip dates
  ☐ Duration of stay matches trip length
  ☐ Number of entries matches your plan

═════════════════════════════════════════════════════════════════════
PACK FOR THE BORDER
═════════════════════════════════════════════════════════════════════

  ☐ Passport (with visa sticker)
  ☐ Printed itinerary
  ☐ Hotel booking confirmation
  ☐ Return flight confirmation
  ☐ Insurance certificate
  ☐ Recent bank statement (just in case)

═════════════════════════════════════════════════════════════════════
AT THE BORDER
═════════════════════════════════════════════════════════════════════

Border officer may ask: purpose, duration, accommodation, return.
Answer briefly, match your application. Don't volunteer extra info.
Be polite, calm — this is routine.

═════════════════════════════════════════════════════════════════════
THE 90/180 RULE (FUTURE-PROOFING)
═════════════════════════════════════════════════════════════════════

You're allowed 90 days in any 180-day sliding window across the
Schengen area. Not per trip — across all your Schengen trips.

After this trip: {{N}} days used.
Days remaining in current 180-day window: {{N}}.

Bookmark: https://ec.europa.eu/home-affairs/policies/schengen-borders-and-visa/visa-policy/short-stay-visa-calculator_en

═════════════════════════════════════════════════════════════════════
BUILD A CLEAN RECORD FOR FUTURE VISAS
═════════════════════════════════════════════════════════════════════

- Enter France on the date you declared
- Stay within "Duration of stay" (the days shown on visa)
- Don't overstay — even one day affects future applications
- Do what you said you'd do (tourism trip = tourism, not business)
- Leave Schengen before visa expires

A clean first trip = much easier multi-entry visas next time.

═════════════════════════════════════════════════════════════════════
ENJOY YOUR TRIP
═════════════════════════════════════════════════════════════════════

You've earned it. Bon voyage.
```

## Routing rules

| Situation | Suggest next |
|---|---|
| Visa sticker has error | Return to TLS for correction before travel |
| Trip is multi-entry visa | Save Schengen calculator URL; check before each future trip |
| User has overstayed (already returned, didn't realise) | Significant issue; recommend consultation with French consulate or immigration lawyer |
| User is doing multi-country trip | Each country has its own border control, but Schengen unified rules apply |
| Returning user (3+ Schengen trips) | This skill is overkill; they know the drill |

## Common pitfalls

| Pitfall | Why it hurts | Fix |
|---|---|---|
| Travelling on a wrong visa | Immediate denial at border | Verify sticker BEFORE flying |
| Overstay even by 1 day | Affects every future Schengen application | Track days carefully; leave before expiry |
| Carrying nothing to border | Can be denied entry | Bring itinerary + insurance + return ticket |
| Travelling on different dates than declared | Border control may question | Match declared dates closely |
| Doing business when declared tourism | Future visa risk if discovered | Match your actual purpose to your declared purpose |
| Long-staying parents during minor's visa | If child stays past their visa allows = compound issue | Whoever has the shorter visa controls departure date |
| Not knowing 90/180 rule | Easy to overstay accidentally | Memorise; check after every trip |

## Authoritative sources

- EU Schengen calculator — https://ec.europa.eu/home-affairs/policies/schengen-borders-and-visa/visa-policy/short-stay-visa-calculator_en — verified 2026-05-24
- France-Visas entry guidance — https://france-visas.gouv.fr/en/web/france-visas — verified 2026-05-24
- Schengen Borders Code (Regulation 2016/399) — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02016R0399 — verified 2026-05-24

## Notes for maintainers

- The 90/180 rule is the most-violated Schengen rule by tourists. Frequent travellers often don't realise their cumulative days.
- "Duration of stay" on the sticker can be less than visa validity. A visa valid 1 Jan-31 Dec with Duration 30 days means: any 30 days within 1 Jan-31 Dec.
- For multi-entry visa users, each entry stamp / exit stamp matters. Border officers check the cumulative days.
- For users entering through a non-France Schengen state (e.g. landing in Frankfurt first), German border control inspects but visa is honoured. Mention this for multi-country travellers.
- For users who plan their first trip, this skill is mostly reassurance. For users who've had a border-control issue before, more attention is needed.
- For minors traveling, ensure the parent who controls departure has the same / longer visa than the child.
- The "clean record" concept is real: consulates track applicant compliance, and good first trips lead to longer multi-entry visas (1y → 3y → 5y cascade).
