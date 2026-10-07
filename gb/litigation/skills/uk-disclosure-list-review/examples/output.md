# Example Output

## Scenario

User asks: "Use a public authority to show how disclosure-list QC should flag privilege and inspection issues."

Access state: live source mode. Claude retrieved WH Holding Ltd v E20 Stadium LLP [2018] EWCA Civ 2652 from BAILII/public PDF text.

## Good Output Shape

```yaml
access_mode: live_source
materials_reviewed:
  - "WH Holding Ltd v E20 Stadium LLP [2018] EWCA Civ 2652"
missing_materials:
  - "Actual disclosure list to QC"
  - "Search/custodian record"
  - "Disclosure order"

coverage_flags:
  - issue: "Public authority illustrates why a privilege challenge may require sample inspection and careful evidence of purpose."
    source: "WH Holding [2018] EWCA Civ 2652 at [1]-[4]"
    status: authority_context
    severity: major
    confidence: high
    next_step: "In a live list, identify challenged withheld/redacted documents and the evidence supporting the privilege basis."

privilege_flags:
  - document_id: "sample category: board/stakeholder settlement emails"
    issue: "Dominant purpose must be assessed; documents about commercial settlement or business management may not all be privileged."
    source: "WH Holding [2018] EWCA Civ 2652 at [56]"
    status: needs_lawyer_review
    confidence: medium
    next_step: "For each withheld/redacted item, identify author, recipients, purpose, litigation context, and whether the dominant purpose was conducting litigation."

potentially_adverse:
  - document_id: "not assessed in public-authority example"
    basis: "No matter-specific disclosure list supplied."
    status: source_missing
    confidence: low
    next_step: "Provide the actual list and issue pleadings."

rule_status:
  disclosure_order: source_missing
  cpr_pd: verify_current_rule
```

## Bad Output To Avoid

```text
The disclosure exercise is adequate.
```

Do not certify disclosure compliance.
