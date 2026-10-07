# Example Output

## Scenario

User asks: "Can we tell clients this desktop legal AI app keeps everything local?"

Access state: user-supplied architecture mode. Claude has a README, settings screenshots, and a network diagram, but no runtime packet capture.

## Good Output Shape

```yaml
access_mode: user_supplied_architecture

local_state_map:
  - data_type: uploaded_documents
    path_or_location: "Workspace/files/documents"
    sensitivity: high
    deletion_method: "Delete workspace folder"
    backup_implication: "Included in user backups"
    evidence: "README section 'Data layout'"
  - data_type: chat_history
    path_or_location: "Workspace/.app/app.sqlite"
    sensitivity: high
    deletion_method: "Delete workspace folder or purge conversations in app"
    backup_implication: "Included in user backups"
    evidence: "settings screenshot and README"

external_calls:
  - destination: "api.anthropic.com"
    trigger: "User runs model-backed analysis"
    payload: "Selected prompt, excerpts, and user instructions"
    credential: "User BYOK"
    retention: "provider documentation not supplied"
    opt_out: "Disable model-backed analysis"
    evidence: "settings screenshot supplied by user"
    retrieval_date: null
    status: user_supplied_source

  - destination: "find-caselaw.service.gov.uk"
    trigger: "User runs citation verification"
    payload: "Citation string / search query"
    credential: "none shown"
    evidence: "network diagram"
    status: user_supplied_source

user_disclosure_note:
  confidence: medium
  text: "Documents and generated files appear to be stored in the selected local workspace based on supplied materials. Model-backed analysis sends selected content to the configured model provider. Citation checks may send citation queries to public legal databases. This has not been verified by runtime network testing."

unknowns_and_verification_needed:
  - "No runtime network capture supplied; hidden paths are not_observed_not_excluded."
  - "Provider retention terms not supplied; retrieve current terms before client-facing claims."
```

## Bad Output To Avoid

```text
Everything stays local.
```

Do not make absolute privacy claims without code, dependency, configuration, provider, and runtime evidence.
