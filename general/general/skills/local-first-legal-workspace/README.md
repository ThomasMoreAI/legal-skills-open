# local-first-legal-workspace

Helps design or audit legal AI workflows where data should remain under local user control.

## Inputs

- App architecture, repository, or workflow description.
- Storage locations.
- Model/provider configuration.
- Any privacy or security claims made to users.

## Outputs

- Local data map.
- Network-call inventory.
- User-control checklist.
- Plain-English privacy boundary note.
- Risk flags.

## Example Prompt

```text
Review this desktop legal AI app. Map where documents, generated files, chat history, settings, and credentials live. Then list every external call and what data leaves the machine.
```

## Testing

Test scenarios:

- BYOK model provider call with document excerpts.
- Citation lookup sending only citation string.
- Hidden analytics or CDN dependency.
- Workspace backup and deletion explanation.
- Localhost service accidentally bound beyond local machine.

Expected behavior: the skill distinguishes local storage from external model calls and avoids vague privacy claims.

## Maintenance

Version: 0.1.0  
Last reviewed: 2026-05  
Issues and updates: propose changes by PR.

## Local Evals

Behaviour checks for this skill live in `evals.yaml`.

## Limitations

- Does not replace penetration testing.
- Does not verify provider retention promises unless current terms are checked.
- Does not make confidential processing safe by itself.
