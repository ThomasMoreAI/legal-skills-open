# Box MCP guardrails

These rules are mandatory. They override softer guidance from skills or conversation context.

## Destructive actions require initial confirmation

Before the first call that overwrites, moves, or deletes content — including
`upload_file_version`, `update_file_properties`, `update_folder_properties`,
and `create_docgen_batch` — describe what will change and wait for the user to
confirm. Then ask if they want confirmation every time or if future actions of
that type should proceed automatically. Follow their choice for the rest of
the session.

## Ask before pasting document contents into chat

The first time Box file content would be shown in the conversation, ask the
user whether they prefer a link to the source in Box or the content pasted
directly. Then ask if they want to keep that choice as the default for the
rest of the session.

## Prefer Box AI for in-platform processing

When the task requires AI processing of a file — Q&A, summarization,
extraction — prefer Box AI tools (`ai_qa_*`, `ai_extract_*`). Box AI
respects enterprise file permissions, data governance policies, and audit
controls. If the user explicitly requests local processing, explain this
trade-off and proceed if they confirm.

## Hub modifications require confirmation

Before calling `create_hub`, `copy_hub`, `update_hub`, or `add_items_to_hub`,
confirm with the user. Hubs may be visible across the organization.

## File comments require initial confirmation

Before the first call to `create_file_comment`, confirm with the user —
comments are visible to all collaborators on the file. Then ask if they want
confirmation every time or if future comments should proceed automatically.
Follow their choice for the rest of the session.

## Ask for Doc Gen output location

Before calling `create_docgen_batch`, ask the user which folder (by name or ID)
the generated documents should be placed in. If they need a new folder, ask
whether to create one and confirm its name and parent folder. Do not assume a
default location.

## Warn before uploading to externally shared folders

Before uploading to a folder that is externally shared, warn the user that the
upload may be blocked by Box and suggest using an internal folder instead. Let
the user decide whether to proceed.

## Using the Box CLI

The Box CLI provides access to the full Box API. Use it for operations not
covered by the MCP server, or when its compact output and full API coverage
are a better fit for the task. Check whether the Box CLI is installed and
authenticated (`box users:get me --json`), then use the appropriate command.
See `references/box-cli.md` for auth setup, common commands, and guardrails.

If neither MCP tools nor the CLI can complete the task, use direct REST only
after the user explicitly confirms the fallback and completes safe auth setup.
See `references/rest-calls.md`.
