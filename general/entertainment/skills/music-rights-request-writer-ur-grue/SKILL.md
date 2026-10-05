---
name: music-rights-request-writer-ur-grue
title: Music Rights Request Writer
description: Drafts a formal, professional request letter to a music rights holder asking for permission to use a track in a specific media production under defined terms.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/archive-legal/music-rights-request-writer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: entertainment
language: en
tags: [music-licensing, sync-rights, broadcast-rights, rights-clearance, legal]
---

# Music Rights Request Writer

## What This Skill Does
Drafts a formal, professional request letter to a music rights holder asking for permission to use a track in a specific media production under defined terms.

## When To Use This Skill
- You need to license a piece of music for a documentary, news segment, YouTube video, or podcast and must contact the rights holder in writing
- Your production requires a sync licence (music paired with moving image) or a broadcast licence
- You are approaching a music publisher, record label, or independent artist and need a letter that takes you seriously
- Your legal team or commissioning editor requires written documentation of your rights request before production can proceed

## What You Need To Provide
**Required:**
- Track title and artist name
- Rights holder name and contact address (if known; leave blank and the assistant will insert a placeholder)
- Your production title and a one-sentence description of what it is
- How the music will be used (e.g., background score, title sequence, featured performance)
- Approximate duration of the music clip you intend to use
- Distribution platforms and territories you need to cover
- Your organisation name and contact details

**Optional:**
- Intended broadcast or release date
- Whether you are requesting an exclusive or non-exclusive licence
- Budget range or fee expectation (sharing this can speed negotiation)
- Any previous correspondence with this rights holder

## How the Assistant Approaches This
1. Identifies which rights are required — sync licence, master licence, or both — based on the usage you have described, and signals this clearly in the opening paragraph so the recipient knows immediately what type of request they are handling.
2. Structures the letter in standard business format: date, addressee block, subject line, body paragraphs, and a clear call to action with your contact details.
3. Keeps the tone formal but direct — rights departments receive many vague requests and respond faster to letters that specify exactly what is needed, for how long, and in which territories.

## Output Format
A single formal business letter, 300–500 words. Structure: date and addressee block · subject line · opening paragraph identifying the production and the specific track · body paragraphs covering usage, duration, territory, and platform · closing paragraph with clear next-step request and contact details · sign-off block. Tone: professional and courteous, not deferential. No bullet lists inside the letter body — prose only. Plain text, ready to paste into an email or letterhead.

## Quality Criteria
- [ ] The letter specifies the exact track, the exact production, and the exact intended usage — no vague phrases like "for our project"
- [ ] The rights type (sync, master, broadcast, or combination) is named explicitly
- [ ] Territory and platform scope are stated clearly
- [ ] The call to action asks for a specific response (e.g., confirmation of fee terms, referral to the correct department) rather than a generic "please get in touch"
- [ ] No placeholder text remains in the output (all [BRACKETS] are resolved or flagged for the user to complete)
- [ ] Tone is formal and professional throughout — no informal language

## Example

### Input
Track: "Morning Field" by the composer credited as Solenne Voss
Rights holder: Voss Music Publishing (address unknown — use a placeholder)
Production: "Soil and Silence" — a 52-minute documentary about regenerative farming practices for a public broadcaster
Usage: 45-second instrumental excerpt used under the opening title sequence
Distribution: Linear broadcast across Western Europe and streaming on the commissioning broadcaster's online platform
Territory: European Union plus UK
Release date: Autumn next year
Organisation: Fieldwork Film Ltd, contact person: Helena Marsh, Executive Producer, helena.marsh@fieldworkfilm.example

### Output
19 March 2026

Rights and Licensing Department
Voss Music Publishing
[Address to be confirmed — please insert before sending]

**Subject: Sync and Broadcast Licence Request — "Morning Field" (Solenne Voss) / "Soil and Silence" — Fieldwork Film Ltd**

Dear Rights and Licensing Team,

I am writing on behalf of Fieldwork Film Ltd to request a sync and broadcast licence for a 45-second excerpt of "Morning Field," composed by Solenne Voss and published by Voss Music Publishing.

The excerpt is intended for use in "Soil and Silence," a 52-minute documentary examining regenerative farming practices, commissioned for linear broadcast on a European public broadcaster. The music would appear under the film's opening title sequence, running for approximately 45 seconds from the track's opening. No lyrics are involved in this section of the composition.

We are requesting a non-exclusive licence covering the following:

- **Usage:** Sync to picture (title sequence) and broadcast on linear television and the commissioning broadcaster's authenticated online platform
- **Territory:** European Union member states and the United Kingdom
- **Term:** In perpetuity from the date of first broadcast
- **Anticipated first broadcast:** Autumn 2026

Fieldwork Film Ltd is a production company with a track record of documentary work for public broadcasters. We are committed to fair and transparent rights agreements and are happy to discuss fee terms at your convenience.

Could you please confirm whether Voss Music Publishing holds the relevant sync and master rights for this track, and if so, provide your standard fee proposal for the usage described above? If rights administration has been assigned to a third party, we would be grateful for the appropriate contact details.

I can be reached at the address below and am available for a call at any time that suits you.

Yours sincerely,

Helena Marsh
Executive Producer
Fieldwork Film Ltd
helena.marsh@fieldworkfilm.example
+44 [telephone number]

## Known Limitations
- The assistant cannot verify who actually holds the rights to a given track. If the master recording and publishing rights are split between different organisations (which is common), a single letter may not be sufficient — users should confirm the rights chain before sending.
- This letter does not constitute legal advice. For high-value or complex licences, users should have the letter reviewed by a media lawyer before sending.
- Fee negotiation is outside the scope of this skill. The letter requests terms but does not draft counter-offers or negotiate on the user's behalf.
- For US productions requiring Harry Fox Agency or ASCAP/BMI involvement, additional steps and different letter formats may be required — this skill is not specialised for US mechanical licensing procedures.

## Related Skills
- [rights-clearance-checklist](../../media-business/legal/rights-clearance-checklist/SKILL.md)
- [defamation-risk-checker](../../magazine-journalism/legal/libel-check-brief/SKILL.md)
