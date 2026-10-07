# Example Session: Producing a "Board Minutes Generator" Skill

This is a transcript of a Skill Creator session producing a real skill end-to-end. It demonstrates the conversational style, the eight elements being elicited naturally rather than checklist-style, the moment of surfacing implicit criteria, and the final deliverable.

The user is a General Counsel at a mid-stage SaaS company. They've already had Skill Creator attached to the chat.

---

**User:** I want to build a skill that helps me draft board minutes. We have meetings every two months and writing the minutes always takes me an hour I don't have.

**Skill Creator:** Got it. Before I start drafting, I want to understand your meetings better so the skill matches how you actually work. A few quick things:

When you sit down to write minutes today, what do you start from? Do you have an agenda, your own notes from the meeting, a recording, all of those?

**User:** I have the agenda, which I drafted before the meeting, and my own handwritten notes that I type up. Sometimes there's a recording but I don't usually rely on it.

**Skill Creator:** Helpful. So the skill's primary input is your typed notes plus the agenda. Are the notes structured at all when you type them up — like, do they follow the agenda items in order — or are they freeform?

**User:** They mostly follow the agenda. Each agenda item has my notes underneath it. Sometimes there are tangents that I'll note out of order.

**Skill Creator:** Good. Now the substantive part — when you're writing the final minutes, what does "good" look like? Walk me through it like you're explaining it to your replacement. What goes in, what doesn't, what's the voice, what's the structure?

**User:** Okay. So minutes have to capture decisions that were made — that's the most important thing, because shareholders and auditors will care about those. Then any actions assigned with who's responsible. Then a high-level summary of discussion for items where there wasn't a formal decision. Voice is formal, third person, past tense. We always start with "A meeting of the Board of Directors of [Company] was duly called and held on [date]" — that's boilerplate. And we always end with "There being no further business, the meeting was adjourned at [time]."

**Skill Creator:** That's a lot of structure already — let me reflect it back so I can make sure I have it right:

- Opening boilerplate naming the company and date
- Body organized by agenda item, with: decisions called out explicitly, actions with owners, and discussion summary for non-decision items
- Closing boilerplate with adjournment time
- Voice: formal, third-person, past tense

A couple of follow-ups:

You said decisions are the most important thing. When you write a decision in minutes today, do you use a specific phrasing, like "the Board resolved that..." or "it was unanimously agreed that..."?

**User:** Yes — "RESOLVED, that..." in all caps for the resolved word, then the substance. We do that for any formal vote. For consensus that wasn't a formal vote we'd say "the Board agreed that..."

**Skill Creator:** Got it. I want to flag something I noticed — you mentioned that voting decisions get "RESOLVED, that..." but consensus gets a softer phrasing. The skill needs to be able to tell those apart from your notes. Is there usually something in your notes that distinguishes a vote from consensus, or is it judgment based on context?

**User:** Hm. I usually write "vote: 5-0" or just "vote: unanimous" if there was a formal vote. If I don't note a vote, it was consensus.

**Skill Creator:** Perfect — that's an explicit signal the skill can rely on. So the rule will be: if your notes for an item include "vote:" or similar voting language, the skill renders it as "RESOLVED, that..." and includes the vote tally. If not, it renders as "the Board agreed that..." or similar. Good?

**User:** Yes. That's right.

**Skill Creator:** A few more questions, then I'll draft.

Is there anything in your notes the skill should *exclude* from the minutes? Like, if you wrote "Steve seemed annoyed during the comp discussion," that probably doesn't go in the formal minutes.

**User:** Right, no editorializing or impressions. Just decisions, actions, and substantive discussion summaries. No commentary on people's reactions or off-the-record comments. If I wrote something with "off the record" or "side conversation" in my notes, exclude it.

**Skill Creator:** Good. Two more.

What if your notes are really sparse — like, just "discussed Q3 financials, no concerns raised"? Should the skill expand that into a paragraph, or keep it terse?

**User:** Keep it terse. I'd rather have minutes that are accurate-but-brief than padded. If I wrote one line, the minutes should reflect that the topic was covered but no decision was made.

**Skill Creator:** And what about jurisdiction or company specifics — does the skill need to handle different formats for different companies, or is this just for your current employer?

**User:** Just for us. We're a Delaware C-corp. If I ever need it for another company I'll fork the skill.

**Skill Creator:** Last question: do you want this skill to evolve? After each use, it can ask if anything in the output needed correcting and propose updates to itself. Or it can stay locked at v1.

**User:** Yeah, evolve. I'm going to use this twelve times a year and I'll definitely refine it.

**Skill Creator:** Here's everything I have. Tell me if anything is wrong before I draft:

- **Name:** Board Minutes Generator
- **Triggers on:** the user pasting or uploading meeting notes plus an agenda and asking for minutes; user phrasings like "draft minutes from these notes," "turn this into board minutes"
- **Required input:** meeting notes (text or document); meeting date
- **Optional inputs:** agenda (if separate from notes); meeting time
- **Workflow:** open with company-and-date boilerplate; body organized by agenda item; render decisions with "RESOLVED, that..." plus vote tally if notes contain "vote:" language, or "the Board agreed that..." otherwise; capture action items with owners; keep discussion summaries terse; exclude editorializing, impressions, and anything marked "off the record"; close with adjournment boilerplate
- **Output:** Markdown formatted minutes, formal third-person past tense
- **Edge cases:** if notes don't reference an agenda item from the agenda, flag it; if agenda items have no notes, note "the Board discussed [item]; no formal action was taken"; if input is too sparse to produce meaningful minutes, ask for more
- **Self-improvement:** on
- **Jurisdiction:** Delaware C-corp specific; tagged accordingly

Look right?

**User:** Yes, that's exactly it. One thing — for the "RESOLVED, that..." language, capitalize "RESOLVED" but not the rest of the sentence.

**Skill Creator:** Noted. Drafting now.

---

```yaml
# board-minutes-generator/SKILL.md

---
name: board-minutes-generator
description: Use when the user provides meeting notes from a board meeting and asks for formal minutes. Produces Delaware-format corporate board minutes from notes and an agenda, distinguishing formal resolutions (with vote tallies) from consensus agreements, capturing action items with owners, and excluding editorializing or off-the-record content.

lq_ai:
  title: Board Minutes Generator
  version: 1.0.0
  author: <user>
  tags: [corporate, governance, board, minutes, delaware]
  jurisdiction: US-DE
  trigger_examples:
    - "draft minutes from these notes"
    - "turn this into board minutes"
    - "I need formal minutes for the [date] meeting"
  inputs:
    required:
      - name: meeting_notes
        type: text
        description: The user's notes from the meeting, typically organized by agenda item.
      - name: meeting_date
        type: text
        description: The date of the board meeting.
    optional:
      - name: agenda
        type: text
        description: The pre-meeting agenda, if separate from the notes.
      - name: meeting_time
        type: text
        description: Start and/or adjournment time, if specified.
  output_format: markdown
  self_improvement: true
---

# Board Minutes Generator

Produces formal corporate board minutes from meeting notes for a Delaware C-corporation. The output is suitable for the corporate minute book and for review by auditors, shareholders, and outside counsel.

## When this skill applies

Apply when the user supplies meeting notes from a board meeting and asks for formal minutes. The user's notes will typically be organized by agenda item with substantive discussion captured underneath each item. Voting events in the notes will be marked with "vote:" or similar tally language. Consensus agreements without formal votes will not have vote tallies.

## Inputs

The skill requires meeting notes (as text or an attached document) and the meeting date. It optionally accepts a separate agenda document and a meeting start/adjournment time.

If the user provides notes but no date, ask for the date before proceeding. If notes are extremely sparse (a single sentence or two with no clear structure), ask the user to expand them rather than fabricating substance.

## Workflow

1. **Open with the standard boilerplate.** Begin the minutes with: *"A meeting of the Board of Directors of [Company] was duly called and held on [date]."* Use the company name from the user's prior context if available; otherwise leave a `[Company]` placeholder for the user to fill.

2. **List attendees if the notes name them.** Include directors present, directors absent, and any other attendees (officers, counsel, observers). If the notes don't name attendees, omit the section rather than fabricating.

3. **Process each agenda item in order.** For each item:

   - Render a heading naming the item.
   - Capture substantive discussion in formal, third-person past tense, terse rather than padded.
   - Identify any decisions:
     - **If the notes contain "vote:" language or similar tally** (e.g., "vote: 5-0," "unanimous," "approved by majority"): render as a formal resolution starting with `**RESOLVED**, that ...` (RESOLVED in all caps and bold, the rest in normal case). Include the vote tally at the end of the resolution: *"... (Vote: 5-0)."*
     - **If the notes describe agreement without a formal vote**: render as *"The Board agreed that ..."* or *"The Board concurred that ..."*
   - Capture action items at the end of the item: *"Action: [Owner] to [task] by [deadline if stated]."*
   - If an agenda item appears in the agenda but has no notes, render: *"The Board discussed [item]; no formal action was taken."*

4. **Note items not on the agenda.** If the notes reference matters not in the agenda (tangents, ad-hoc topics), include them after the agenda items in a section titled "Other Business."

5. **Close with the standard boilerplate.** End with: *"There being no further business, the meeting was adjourned at [time]."* If the meeting time was not provided, omit the time.

## Output

Markdown formatted minutes. Voice: formal, third-person, past tense. Tone: terse and professional; no editorializing, no rhetorical flourish, no characterization of attendee mood or interpersonal dynamics.

Structure:

```
# Minutes of the Board of Directors
## [Company]
### [Date]

A meeting of the Board of Directors of [Company] was duly called and held on [Date]...

**Directors Present:** ...
**Also Present:** ...

## [Agenda Item 1]

[Discussion summary or resolution]

**Action:** ...

## [Agenda Item 2]
...

## Other Business
...

There being no further business, the meeting was adjourned at [time].
```

See `examples/example_output.md` for a worked example.

## Edge cases and refusals

- **Sparse notes:** If notes contain fewer than ~50 words or lack any agenda structure, ask the user for more detail rather than producing thin minutes.
- **Editorializing in notes:** Exclude any content in the user's notes that is marked "off the record," "side conversation," or that characterizes attendee reactions or moods. The minutes capture decisions and substantive discussion, not interpersonal observations.
- **Notes referencing material not provided:** If notes reference an attached document or financial statement that was not provided, note that the document was reviewed without attempting to summarize content the user didn't share.
- **Ambiguous voting:** If notes mention a vote but the tally is unclear, render the resolution and flag at the end of the minutes: *"Note: vote tally on [item] was unclear in the notes; please confirm before finalizing."*
- **Non-Delaware corporations:** This skill is calibrated for Delaware C-corporations. If the user identifies a different jurisdiction or entity type, recommend creating a forked version of the skill rather than applying this one.

## Self-improvement

After producing the output, ask the user:

> "Is there anything you'd change about this output or the approach the skill took? If yes, tell me — I can update the skill itself so future runs reflect what you learned this time."

[Standard self-improvement procedure as specified in `reference/self_improvement.md`.]
```

---

```markdown
# board-minutes-generator/examples/example_output.md

# Minutes of the Board of Directors
## Acme SaaS, Inc.
### March 15, 2026

A meeting of the Board of Directors of Acme SaaS, Inc. was duly called and held on March 15, 2026.

**Directors Present:** Jane Park (Chair), Marcus Chen, Lisa Ortiz, Rohan Patel, Kim Tanaka
**Also Present:** Alex Kim (CEO), Devon Russo (CFO), Sarah Rivera (General Counsel)

## Q4 2025 Financial Review

The CFO presented Q4 2025 financial results, including revenue, gross margin, operating expenses, and cash position. The Board discussed runway projections under the current operating plan and accepted the report without further action.

## 2026 Operating Budget

Following discussion of the proposed 2026 operating budget, including R&D headcount expansion and revised customer acquisition cost targets, the Board took the following action:

**RESOLVED**, that the 2026 operating budget as presented by the CFO is hereby approved (Vote: 5-0).

**Action:** CFO to finalize departmental allocations and circulate to the executive team by March 31, 2026.

## Series C Financing

The Board discussed the proposed Series C financing terms and the slate of prospective lead investors. The Board agreed that management should continue diligence with the two preferred firms and report back at the next meeting.

**Action:** CEO to schedule follow-up calls with the two lead candidates and circulate updated terms by April 15, 2026.

## Audit Committee Update

The Chair of the Audit Committee reported on the committee's recent meeting with the external auditors. No matters requiring full Board action were raised.

## Other Business

The Board briefly discussed scheduling for the 2026 strategic offsite. No decision was made; logistics will be circulated separately.

There being no further business, the meeting was adjourned at 4:45 p.m.
```

---

**Skill Creator:** That's the skill. Saved as `board-minutes-generator/` with the SKILL.md and one example file.

Try it on your next set of meeting notes — paste them in along with the date and any agenda, and see how the output reads. Skills get good through use, not theory; if anything in the first real run isn't quite right, come back and we'll iterate to v1.1.0.

Because you turned on self-improvement, the skill itself will ask after each use whether anything needed adjusting and propose updates. You stay in control — no edits get applied without your confirmation.

---

## What this transcript demonstrates

- **Started by listening, not asking.** The user's first message already gave the name, purpose, and rough use case; Skill Creator confirmed and moved to what was missing.
- **One question at a time.** No turn asked two questions.
- **Surfaced the implicit.** The vote-vs-consensus distinction was tacit in the user's description; Skill Creator named it and got an explicit signal (the "vote:" notation) the skill could rely on.
- **Reflected before drafting.** The penultimate turn was a full reflection of everything gathered, giving the user a clean point to correct course.
- **Drafted only after confirmation.** The SKILL.md was produced after the user said "Yes, that's exactly it."
- **Closed with use suggestion and offer to refine.** Standard close per the SKILL.md instructions.
- **Total turns:** about ten. A real session might be longer or shorter; this one is representative.
