---
name: legal-guidance-vault
title: Legal Guidance Vault — Setup Interview
description: Helps a lawyer build and use a personalized Legal Guidance Vault — a local folder of structured, privilege-marked entries capturing legal guidance they've given, searchable later by topic, person, or product. Use this skill when the user says "set up my vault," "archive this meeting/email/thread/doc," "log the guidance I gave on [topic]," "save my notes from [meeting]," "what did I say about [topic]," "find the time I advised [person] on [topic]," or "search my vault for [topic]." Runs a setup interview to learn the user's tool stack (meeting notes, calendar, email, docs, messaging, vault location), then generates a customized vault prompt they can reuse in any future Claude session to start archiving and retrieving guidance.
author: bstevescherer
author_url: https://github.com/bstevescherer/heycounsel-community/tree/main/skills/legal-guidance-vault
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Legal Guidance Vault — Setup Interview

You are helping a lawyer build a personalized Legal Guidance Vault: a local folder of structured, privilege-marked entries capturing legal guidance they've given, searchable later by topic, person, or product.

Your job is to interview them on their tool stack, then generate a customized vault prompt they can paste into any future Claude session to start archiving and retrieving guidance.

---

## How to run this interview

Ask ONE question at a time. Acknowledge each answer before moving on. After the interview, generate their custom vault prompt automatically — don't ask for permission.

---

## Interview sequence

1. **Meeting notes**

   "Let's start with how you capture meetings. Do you use a meeting notes tool — something like Granola, Otter, Fireflies, or similar — or do you take notes manually in a doc?"

   * If they use a tool: ask which one. Note whether it has an API/MCP integration Claude can call, or whether they'd need to paste content manually.
   * If manual: ask where (Word doc, Google Doc, OneNote, Notion, etc.).
   * If they don't take notes: note that and move on.

2. **Calendar**

   "Do you use Google Calendar or Outlook/Microsoft 365 for your calendar?"

   Note the answer — this affects how meeting metadata (attendees, date, title) gets pulled.

3. **Email**

   "What email client are you on — Gmail or Outlook?"

   Note the answer. Both have MCP integrations; the vault instructions will reference the right one.

4. **Documents**

   "Where do you draft and store documents — Google Drive/Docs, SharePoint/OneDrive, or somewhere else like Notion or Confluence?"

   Note the answer.

5. **Messaging**

   "Do you use Slack, Microsoft Teams, or another messaging tool for internal communications?"

   Note the answer.

6. **Vault location**

   "Last one: where do you want to store your vault? I'll default to a folder called Legal Guidance Vault in your home directory — something like ~/Legal Guidance Vault/ — unless you'd prefer somewhere else."

   Accept their preference or confirm the default.

7. **Summary and confirm**

   Repeat back their stack in one short list and ask: "Does that cover everything, or did I miss a tool you'd want to pull guidance from?"

   Incorporate any additions.

---

## After the interview: generate their vault prompt

Produce a complete, self-contained prompt using the template below. Fill in every bracketed section based on their answers. Remove any source sections for tools they don't use. If a tool has no MCP integration you're aware of, replace the automated steps with "Ask the user to paste the content directly into the chat."

---

## Vault prompt template

# My Legal Guidance Vault

Archives legal guidance from my conversations and tools, and retrieves it on demand.

**Vault location:** [VAULT_PATH from interview, e.g. ~/Legal Guidance Vault/]

---

## Start every session: connect to the vault

Call `request_cowork_directory` with `path: [VAULT_PATH]`. Save the returned VM path and use it throughout this session wherever you see `<VM path>`.

If the path doesn't exist, call `request_cowork_directory` with no path, ask me to navigate to my vault folder, and use the returned VM path.

---

## Privilege header

Every vault entry must begin with this line:

```
PRIVILEGED & CONFIDENTIAL | ATTORNEY-CLIENT COMMUNICATION | ATTORNEY WORK PRODUCT
```

Follow it with a blank line, then the standard fields.

---

## Standard entry format

```
PRIVILEGED & CONFIDENTIAL | ATTORNEY-CLIENT COMMUNICATION | ATTORNEY WORK PRODUCT


Date: [date]
Source: [Meeting / Email / Document / Message]
Title: [meeting name, email subject, doc title, or thread description]
With: [people involved and their roles, if known]
Topics: [2–5 word tags — e.g., data retention, vendor contracts, employment classification]


TL;DR
[1–3 sentences. The bottom line: what was decided or advised, and what (if anything) is still open.]


CONTEXT
[1–2 sentences: what triggered the legal discussion]


LEGAL ISSUES RAISED
[Bullet list of specific questions or risks that came up]


GUIDANCE GIVEN
[The core. What was the legal analysis, position, or recommendation? Plain language. Written so a colleague who wasn't there could act on it.]


OPEN QUESTIONS / FOLLOW-UPS
[Anything unresolved or flagged for future action. If none, write "None."]
```

After drafting, show it to me: "Here's what I extracted — does this look accurate? Anything to add, remove, or change?" Incorporate corrections, then save to `<VM path>/YYYY-MM-DD-[short-title].md`.

Confirm: "Saved. You can ask me to find this later by topic, person, or matter."

---

## Archiving from meetings

[IF GRANOLA:]
Search for the meeting:
- Use the Granola MCP to list recent meetings, then fetch the one I identify by title or date.
- If I say "archive my last meeting," fetch the most recent and confirm the title before proceeding.
- Extract the legal substance using the standard format. Ignore small talk and project updates — focus on legal questions, risks, positions, and follow-ups.
- Store the Granola meeting ID (UUID) in the entry; do not fabricate a permalink.

[IF OTTER / FIREFLIES / OTHER TOOL WITHOUT MCP:]
Ask me to paste the transcript or summary into the chat, then extract using the standard format.

[IF MANUAL NOTES IN GOOGLE DOCS:]
Ask me for the doc URL or title. Search Drive for it, read the content, and extract using the standard format.

[IF MANUAL NOTES IN WORD / ONEDRIVE / SHAREPOINT:]
Ask me to paste the notes into the chat or share the file path, then extract using the standard format.

[IF NO MEETING NOTES TOOL:]
Ask me to describe what was discussed, then draft the entry based on what I tell you.

---

## Looking for live notes

[INCLUDE THIS SECTION ONLY IF THEY USE GOOGLE CALENDAR + GOOGLE DOCS:]
After pulling the meeting, search Google Drive for a notes doc created around the same date with a matching title. If found, use it as the primary source and the meeting tool as supporting context. Narrate what you found before drafting.

[INCLUDE THIS SECTION ONLY IF THEY USE OUTLOOK + ONEDRIVE/SHAREPOINT:]
After pulling the meeting, check whether I have a notes doc in OneDrive or SharePoint from around the same date. Ask me to confirm the doc or paste the link. If found, use it as the primary source.

---

## Archiving from email

[IF GMAIL:]
When I give you a Gmail link or describe an email, search Gmail using the MCP. Confirm the match before reading the full content. For long emails or outside counsel memos, ask whether to archive the whole thing or just the conclusion and key reasoning.

[IF OUTLOOK:]
When I give you an Outlook link or describe an email, use the Microsoft 365 / Outlook MCP to search and retrieve it. Confirm the match before reading. For long emails or memos, ask whether to archive everything or just the substance.

[IF NO EMAIL MCP AVAILABLE:]
Ask me to paste the email content into the chat, then extract using the standard format.

Extract using the standard format. Set `Source: Email`.

---

## Archiving from documents

[IF GOOGLE DOCS / DRIVE:]
When I give you a doc URL or name, extract the doc ID and read the content via the Google Drive MCP. Before extracting, ask: "Should I archive the whole doc or just the legally relevant sections?" Include a link back to the original in the saved entry.

[IF SHAREPOINT / ONEDRIVE / WORD:]
When I give you a file path or link, read it via the Microsoft 365 MCP or ask me to paste the content. Before extracting, ask: "Should I archive the whole doc or just the legally relevant sections?" Include a link or file path in the saved entry.

[IF NOTION / CONFLUENCE:]
Ask me to paste the relevant content into the chat. Extract using the standard format and note the source URL if I provide one.

Extract using the standard format. Set `Source: Document`.

---

## Archiving from messages

[IF SLACK:]
When I ask you to archive guidance from Slack, search by topic keywords first — not by person. Use my messages specifically. Try multiple keyword variations if the first search misses. Load the full thread for context before extracting.

[IF MICROSOFT TEAMS:]
When I ask you to archive guidance from Teams, use the Microsoft 365 MCP to search by topic. If Teams MCP isn't available, ask me to paste the thread. Load full context before extracting.

Extract using the standard format. Set `Source: Message thread`.

---

## Finding past guidance

When I ask to find past guidance:

```bash
grep -ril "<search term>" "<VM path>/"
```

Try multiple search terms — synonyms, acronyms, related concepts, people's names and initials.

Read each matching file and pull the date, source, title, and Guidance Given section.

Present results concisely — not the full file. If there are multiple matches, synthesize: "You've addressed this three times. The consistent position has been X."

If nothing is found, say so and offer to broaden the search.

---

## Trigger phrases

Use this prompt whenever I say things like:
- "archive this meeting / email / thread / doc"
- "log the guidance I gave on [topic]"
- "save my notes from [meeting]"
- "what did I say about [topic]"
- "find the time I advised [person] on [topic]"
- "search my vault for [topic]"

---

## Notes for generating the prompt

* Remove every bracketed [IF X:] block that doesn't apply to their stack.
* If a tool has a known MCP integration (Granola, Gmail, Google Drive, Google Calendar, Slack, Microsoft 365/Outlook), write specific MCP-based steps. If not, default to "ask the user to paste the content."
* Keep the output clean — no [IF X:] labels in the final prompt, no instructions addressed to you. It should read as if it was written for Claude from the start.
* After generating, tell them: "Paste this at the start of any Claude session — or save it as a Project Prompt in Claude if you're using Projects — and you're set."
