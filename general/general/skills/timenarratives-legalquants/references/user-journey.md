# User journey

The lawyer invokes `/timenarratives` at the end of a work conversation, or asks for narratives for a named matter and period. Use available current context immediately, including ordinary discussion and other LQ skill exchanges. Ask only for materially missing identity, matter or scope. A clear selection of related conversations authorises bounded native retrieval; do not require uploads or repeat consent for each selected chat.

Retrieve original messages where possible, preserving roles, order and source locators. Follow `conversation-context.md` and the internal `cli-contract.md`; the lawyer does not run separate helper commands. Inaccessible or incomplete history stays visible as a limitation. Use a selected export or lawyer account only where needed.

Offer additional documents or a matter folder briefly alongside the first useful draft, without delaying it. Follow `document-context.md` to combine that material and any account of work outside chat with the existing selected conversations. An expressly named folder selects its bounded ordinary contents; the runtime source root alone does not. New material creates a fresh combined packet and, if wording changes, a newly displayed draft for approval.

Draft the lawyer's supported contributions. Automated reports, AI drafting and tool execution do not themselves establish the lawyer's review or completion. Substantive challenges, corrections and reasoning can support that contribution. A colleague's work remains theirs even when quoted in the lawyer's chat. Reconcile the same activity across several skills or conversations without duplicating it.

Begin with “Draft entries”. Follow with a short “Needs your check” list only for material facts: “Did you revise the provisions, review someone else's revisions, or only circulate them?” A supported call need not wait for clarification about planned revisions. Generic approval does not answer that question. Administrative activity is outside this substantive-work scope, not a billability decision.

The first response is an in-memory, unposted draft. With no executable validator, label it “Unvalidated preview”; do not call it copy-ready or final. With validation, retain the displayed map's digest before the user's response. The user can say “use these” or correct the facts. Show materially revised wording before approval; ordinary approval binds only that displayed version. Publish after internal validation, matching reviewed digest and source freshness checks. Never ask the lawyer to handle a token or implementation command.

Use existing confirmed firm-style preferences, or a concise neutral default. Offer an optional one-time style choice alongside a useful draft. A preference changes expression, never personal responsibility, activity, completion or time figures. Store only explicitly agreed settings, without matter examples.

Show final entries in full with short source labels, any remaining withheld activity, and the JSON/Markdown artifact locations. State actual source scope and material coverage gaps. No hours, rates, fees, billing codes, billability decisions or posting. An empty result is appropriate where nothing is supported; it is not a substitute for independently supported work.

Always include:

> Checked only the sources you selected; this drafts narrative text for review and does not estimate time, decide billability, or post entries.

Fallback language:

- Missing context: “I cannot access that conversation here. I can use this chat, a selected export, or your brief account of the work.”
- Partial context: “Part of the selected conversation is unavailable. These entries use only the messages I could read.”
- Stale review: “The sources or draft changed. Please review the updated entries.”
