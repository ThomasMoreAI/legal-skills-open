# Example Output

## Scenario

User asks: "Use public authority to show how you would flag hearsay/source issues in a witness statement review."

Access state: live source mode. Claude retrieved W (Fact Finding: Hearsay Evidence) [2013] EWCA Civ 1374 from Find Case Law.

## Good Output Shape

```yaml
access_mode: live_source
document_reviewed: "Illustrative witness evidence review using W (Fact Finding: Hearsay Evidence) [2013] EWCA Civ 1374"
rule_status:
  court_order: not_applicable_to_public_example
  cpr_pd_checks: verify_current_rule
  hearsay_weight: "Public authority source reviewed"
  pd_57ac: not_applicable_or_verify

issues:
  - paragraph: "Example issue from judgment paras 9-13"
    classification: hearsay_or_reported_fact
    issue: "Central evidence was reported hearsay where the witness had not provided a statement or attended to give evidence."
    severity: major
    confidence: high
    source_pinpoint: "W [2013] EWCA Civ 1374 at [9]-[13]"
    rule_or_source_checked: "Find Case Law public judgment"
    suggested_fix: "For a draft statement, identify whether the witness gives first-hand evidence; if relying on hearsay, explain source, availability, and why direct evidence is not provided."

  - paragraph: "Example issue from judgment para 17"
    classification: source_quality
    issue: "Reported account passed through multiple hands and lacked supporting detail/context."
    severity: major
    confidence: high
    source_pinpoint: "W [2013] EWCA Civ 1374 at [17]"
    rule_or_source_checked: "Find Case Law public judgment"
    suggested_fix: "For a draft statement, flag multiple-hearsay chains and ask for contemporaneous records or first-hand witness evidence."

  - paragraph: "Example issue from judgment para 23"
    classification: weight_of_hearsay
    issue: "Where a witness statement or attendance is missing, reasons for that absence matter to weight."
    severity: major
    confidence: medium
    source_pinpoint: "W [2013] EWCA Civ 1374 at [23]"
    rule_or_source_checked: "Find Case Law public judgment; Civil Evidence Act point to verify in current rules"
    suggested_fix: "In a live review, ask why direct evidence is unavailable and whether hearsay notice/rule compliance is needed."

questions_for_lawyer:
  - "Is the witness giving first-hand evidence or reporting what someone else said?"
  - "If the evidence is hearsay, what procedural notice or explanation is required?"
  - "Does PD 57AC apply to this trial witness statement?"
```

## Bad Output To Avoid

```text
The statement is compliant and ready to sign.
```

Do not certify truth, compliance, or readiness to sign.
