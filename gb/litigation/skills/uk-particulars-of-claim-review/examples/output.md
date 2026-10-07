# Example Output

## Scenario

User asks: "Review these draft Particulars of Claim for an E&W contract claim before counsel sees them."

Access state: user-supplied source mode. Claude has the draft PoC, contract, two key emails, and a chronology. No current CPR source has been retrieved.

## Good Output Shape

```yaml
access_mode: user_supplied_source
pleading_reviewed: "Draft Particulars of Claim v3"
rule_status:
  cpr_pd16: verify_current_rule
  pre_action_protocol: verify_current_rule

element_map:
  cause_of_action: breach_of_contract
  law_basis: "User-supplied pleading theory; verify_current_law"
  elements:
    - element: "Contract formation / parties"
      pleaded_facts: "Paras 3-5 identify the parties and agreement date."
      source: "Contract front page and signature block"
      gap: ""
    - element: "Term relied on"
      pleaded_facts: "Para 9 pleads clause 4 delivery obligation."
      source: "Contract clause 4"
      gap: ""
    - element: "Breach"
      pleaded_facts: "Para 15 alleges delivery occurred five days late."
      source: "Email AB-004; delivery record missing"
      gap: "Delivery record needed to prove actual delivery date."
    - element: "Loss caused by breach"
      pleaded_facts: "Para 21 pleads loss generally."
      source: source_missing
      gap: "No pleaded causal route from delay to claimed losses."

issues:
  - paragraph: 21
    severity: major
    confidence: high
    issue: "Loss is not particularised."
    rule_or_source_checked: "Draft and supplied documents only; CPR/PD16 to verify."
    next_step: "Add heads of loss, amounts or method of calculation, and source documents."
  - paragraph: 24
    severity: critical
    confidence: medium
    issue: "Interest claimed but no basis/rate/period pleaded."
    rule_or_source_checked: verify_current_rule
    next_step: "Confirm statutory/contractual basis and plead period."

questions_for_lawyer:
  - "Is there a standstill agreement or limitation issue not shown in the draft?"
  - "Is specific performance sought, or damages only?"
```

## Bad Output To Avoid

```text
The claim is viable.
```

This skill reviews pleading structure and gaps; it does not certify merits.
