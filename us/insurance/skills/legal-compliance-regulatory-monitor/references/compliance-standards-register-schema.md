# Compliance Standards Register Schema

Use this schema to normalize compliance intelligence into reusable controls.

## Register Fields

| Field | Description |
|---|---|
| Control ID | Stable unique ID for the requirement |
| Layer | Company, Industry, Federal, State |
| Jurisdiction | US or state identifier |
| Control statement | Clear requirement or prohibition |
| Applicability | Product, channel, audience tags |
| Evidence requirement | What proof supports compliant use |
| Disclosure requirement | Required qualifier and placement expectation |
| Risk trigger examples | Language or patterns likely to fail |
| Source reference | Citation to originating source |
| Effective date | Date control is in force |
| Status | Active, Pending, Superseded |
| Owner | Compliance owner responsible for updates |
| Last reviewed | Date of latest validation |

## Lifecycle Rules

- New controls start as Active or Pending with owner assignment.
- Superseded controls require replacement reference and rationale.
- Any control older than review cadence must be flagged for validation.

## Query Patterns

- By channel: retrieve social/email/landing-page constraints
- By jurisdiction: retrieve state overrides
- By claim type: retrieve performance, guarantee, comparative controls
- By product: retrieve life, annuity, retirement variants
