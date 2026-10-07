# Connectors

## How tool references work

This skill uses `~~category` placeholders for optional integrations. The skill works without any connectors configured — they enhance the experience when available.

## Connectors for this skill

| Category | Placeholder | Recommended server | Other options |
|----------|-------------|-------------------|---------------|
| Contract templates | `~~contract-templates` | Local CLI: [`open-agreements@0.8.0` on npm](https://www.npmjs.com/package/open-agreements) | [Open Agreements Remote MCP](https://openagreements.org/api/mcp) (optional hosted service) |

### Local CLI (default)

For local template listing and filling, use the pinned npm package. Requires
Node.js 20 or later. See the
[README](https://github.com/open-agreements/open-agreements#use-with-claude-code)
for details.

### Remote MCP (optional)

The hosted MCP is not bundled with the Claude plugin. A user may configure it
separately, but template contents and field values are then sent to
openagreements.org for server-side DOCX generation. Disclose that transfer and
obtain the user's choice before using it.
