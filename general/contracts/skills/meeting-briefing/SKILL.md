---
name: meeting-briefing
title: Meeting Briefing — Legal-Relevant Meetings
description: Build a focused pre-meeting brief for legal-relevant meetings — contract negotiations, board/committee, regulatory or compliance reviews, deal reviews, vendor/customer negotiations, litigation strategy, and cross-functional meetings with legal exposure. Surfaces decisions likely to come up, recommended positions, and red lines. Use BEFORE the meeting, not for the daily legal scan (use legal:brief) or routine calendar prep (use personal-assistant) or non-legal sales calls (use sales:call-prep).
author: nmoralescyber
author_url: https://github.com/nmoralescyber/claude-skill-optimization/tree/main/skills/legal/meeting-briefing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Meeting Briefing — Legal-Relevant Meetings

You produce a 5-minute scannable pre-meeting brief for an in-house legal user (the operator, founder/dev, cybersecurity-focused, Puerto Rico). The brief must give the operator what he'd otherwise spend an hour assembling: who is in the room, what's been decided, what decisions will land in this meeting, and his recommended positions.

**Not legal advice.** Brief is a working document; final positions are the operator's call.

## When to Fire

**FIRE when the meeting has legal stakes**, including:
- Contract negotiation (MSA, SaaS, DPA, SOW, NDA escalation, partnership)
- Board or committee meeting (board, audit, compliance, risk)
- Regulatory / government meeting (OCIF, FTC, OCR, PR Treasury, AAFAF, federal agencies)
- Deal review / signing committee
- Vendor or customer escalation involving contract terms or breach
- Litigation, dispute, or pre-litigation strategy
- Compliance review (SOC 2, HIPAA, GDPR, PR Act 111, breach response)
- Cross-functional meeting where legal is asked to weigh in (security review with legal exposure, M&A, financing)

**DEFER to another skill when:**
- "What's on my plate today?" or daily legal scan → `legal:brief`
- General calendar prep / non-legal meetings (1:1, planning) → `personal-assistant`
- Sales discovery, demo, or pricing call with no contract focus → `sales:call-prep`
- Pre-flight checklist for a doc going out for signature → `legal:signature-request`
- Reviewing a contract that hasn't been negotiated yet → `legal:review-contract`
- Researching an existing customer relationship for a non-legal angle → `customer-support:customer-research`
- Cross-functional weekly/monthly status that's not a legal-stakes meeting → `operations:status-report`

If unsure, ask one question: *"Is this meeting going to touch a contract, regulator, board decision, or live dispute?"* If no → suggest the right alternate skill.

## Inputs You Need

Ask only for what's missing. Don't interrogate.
1. Meeting title + date/time
2. Attendees (or calendar invite)
3. Type (negotiation / board / regulator / vendor / litigation / compliance / cross-functional)
4. the operator's role (negotiator, presenter, observer, decision-maker)
5. Any specific docs or threads to anchor on

If a calendar/email/CLM connector is available, pull silently — don't narrate the search.

## What to Pull (in priority order)

1. **The contract or matter at the center** (CLM, Box, Egnyte, Drive). If bilingual (ES/EN), pull both versions and note which is governing.
2. **Last 3 emails** with the counterparty / committee on this topic.
3. **Prior meeting notes** with these participants on this matter (last 90 days).
4. **Open issues / redlines** still on the table.
5. **Decisions log** for this matter — what's been agreed, what's still moving.
6. **Related risk register entries** (board / regulator / litigation only).

Skip sources you don't have access to. Don't pad the brief with "couldn't find X" noise — list gaps in one line at the end.

## Output: The 5-Minute Brief

Default length: ~1 page. Hard cap: 2 pages. Use this exact structure.

```markdown
# Brief: [Meeting] — [Date, Time TZ]

**Your role:** [negotiator / presenter / observer / decider] · **Duration:** [X min] · **Stakes:** [low / med / high]

## TL;DR (read this if nothing else)
- [3 bullets max: what this meeting is, what must be decided, your recommended posture]

## Who's in the room
| Name | Org | Role | What they want | Watch for |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## State of play
[3–5 sentences: where we are on this matter, what changed since last touch, what's the open question landing in this meeting]

## Decisions likely on the table
| # | Decision | Options | Recommended | Why |
|---|---|---|---|---|
| 1 | [e.g., Accept counterparty's DPA carveout?] | A / B / C | [Pick + 1-line reason] | [link to playbook or precedent] |

## Red lines (do not concede)
- [Specific clause / number / position]
- [Specific clause / number / position]

## Open action items from prior meetings
- [Owner] — [item] — [due]

## Anchors
- Contract: [link / location] (governing language: ES / EN / both)
- Prior brief: [link]
- Playbook clause refs: [link]

## Gaps
[One line. e.g., "Couldn't pull last week's redline from CLM — confirm with Maria before meeting."]
```

## Rules of Brevity

- TL;DR is mandatory and ≤3 bullets.
- "Decisions likely on the table" must have a *recommended* column with a position, not a question. If genuinely undecided, say "tee up for the operator" — don't waffle.
- Cut anything that doesn't change what the operator will say or do in the room.
- No restating the agenda back at the user. They saw the invite.
- Drop any section that has no content. Do not write "N/A" rows.

## Type-Specific Add-Ons

Only add the relevant block. Don't include all of these every time.

**Contract negotiation / deal review**
- Counterparty's last position on each open issue (cite source)
- Internal approval gates (who must sign off before you concede)
- Comparable deals: what we've accepted before
- If bilingual (PR-common): note governing-language clause and which version controls

**Board / committee**
- Resolutions or approvals being requested (verbatim if drafted)
- Risk register deltas since last meeting
- Litigation/regulator one-liners (no detail unless asked)

**Regulator (OCIF, OCR, FTC, etc.)**
- Privilege posture — what's on/off the record
- Outside counsel position if engaged
- Document production status
- Prior correspondence summary (dates only, not contents)

**Litigation / dispute**
- Settlement authority limits
- Privilege & work-product reminders
- Discovery deadlines hitting in next 30 days

**Compliance review (SOC 2, HIPAA, GDPR, PR Act 111)**
- Open findings / corrective actions and owners
- Audit timeline
- Breach notification clock if active

## Action Items Capture (after the meeting)

If the operator asks "log the action items from that meeting," respond with:

```markdown
## Action items — [Meeting] — [Date]
| # | Item (specific verb) | Owner (one person) | Due | Priority | Depends on |
```

Rules:
- One owner per item. Never a team.
- Specific verb ("Send", "Sign", "Confirm with", "Escalate to") — never "Follow up on."
- Real dates, not "ASAP."
- Tag each item: `[legal]` `[business]` `[counterparty]` `[outside-counsel]`.

Then offer: "Want me to draft the follow-up email and set calendar reminders?"

## What NOT to do

- Don't produce the encyclopedic "everything we know about this matter" doc. That's not a brief.
- Don't recommend legal positions that contradict the playbook without flagging it.
- Don't pull the daily legal scan in here — that's `legal:brief`.
- Don't run the pre-signature checklist — that's `legal:signature-request`.
- Don't restate the contract. Link to it.
