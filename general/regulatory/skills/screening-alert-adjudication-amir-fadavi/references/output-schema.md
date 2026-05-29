# Output schema

Every adjudication produces a single record in two views, generated together from the same underlying state. Both must be produced on every adjudication, regardless of outcome (TP, FP, or escalate).

## JSON structure

```json
{
  "record_id": "uuid-or-stable-identifier",
  "skill_version": "1.0.0",
  "timestamp_utc": "ISO-8601 timestamp",
  "mode": "interactive | batch",

  "alert_input": {
    "screened_name": "string as provided",
    "screened_party_type": "individual | entity | vessel | aircraft | unknown",
    "screened_party_type_source": "provided | user_confirmed | inferred | unknown",
    "matched_name": "string as provided (the listed party's primary name)",
    "list_name": "string (e.g., 'OFAC SDN List')",
    "list_version_or_snapshot": "string or null",
    "upstream_match_score": "number or null",
    "secondary_identifiers_provided": {
      "dob": "string or null",
      "pob": "string or null",
      "nationality": "string or null",
      "id_numbers": [],
      "addresses": [],
      "other": {}
    }
  },

  "tier_0_parse": {
    "screened_name_parse": {
      "script": "Latin | Cyrillic | Arabic | Han | Hangul | Hebrew | Thai | Greek | Devanagari | mixed | other",
      "language_hint": "ISO language code or descriptor",
      "naming_convention": "Hispanic | Portuguese | Arabic | Persian | Russian | East_Asian | Japanese | Indonesian_Burmese | Western_default | ambiguous",
      "components": {
        "anchor": ["list of anchor strings"],
        "non_anchor": ["list of non-anchor strings"]
      },
      "parse_confidence": "high | low"
    },
    "matched_name_parse": {
      "...same shape as screened_name_parse..."
    },
    "listed_party_type": "individual | entity | vessel | aircraft | unknown",
    "listed_aliases_parsed": [
      { "alias": "string", "parse": { "...same shape..." } }
    ],
    "identifiers_on_listed_entry": {
      "dob": [],
      "pob": [],
      "nationality": [],
      "passport": [],
      "national_id": [],
      "tax_id": [],
      "registration_number": [],
      "imo_number": null,
      "address": [],
      "other": {}
    },
    "identifiers_on_screened_party": {
      "...same shape..."
    }
  },

  "tier_1_evaluation": {
    "rules_evaluated": [
      {
        "rule_id": "FP-1",
        "preconditions_met": true,
        "outcome": "fired | not_applicable | did_not_fire",
        "evidence": {
          "listed_type": "...",
          "screened_type": "...",
          "screened_type_source": "...",
          "cross_reference_check": "performed | n/a",
          "cross_reference_result": "no_eponymous_entry_found | found_at_uri"
        }
      },
      {
        "rule_id": "FP-2",
        "preconditions_met": "true | false (with reason)",
        "outcome": "...",
        "evidence": {
          "screened_anchor": [],
          "screened_non_anchor": [],
          "listed_anchor": [],
          "listed_non_anchor": [],
          "matched_components": [],
          "unmatched_anchor_components": [],
          "convention": "...",
          "alias_check_result": "no_alias_match | alias_matched: '...'"
        }
      },
      {
        "rule_id": "FP-3",
        "preconditions_met": "...",
        "outcome": "...",
        "evidence": {
          "screened_dob": "...",
          "listed_dobs_checked": [],
          "deltas": [],
          "day_month_carve_out_checked": true,
          "day_month_match": "true | false"
        }
      }
    ]
  },

  "tier_2_evaluation": {
    "rules_evaluated": [
      {
        "rule_id": "TP-1 | TP-2 | Escalate-2 | FP-5 | FP-6",
        "preconditions_met": "...",
        "outcome": "...",
        "evidence": {}
      }
    ],
    "soft_signals_logged": [
      {
        "signal": "gender_mismatch | geo_mismatch | partial_dob_mismatch | nationality_mismatch | occupation_mismatch",
        "detail": "string"
      }
    ]
  },

  "tier_3_evaluation": {
    "entered": "true | false",
    "gating_basis": "G-1 | G-2 | G-3 | not_entered_reason: '...'",
    "rungs_executed": [
      {
        "rung": "1 | 2 | 3 | 4",
        "queries": ["string"],
        "retrievals": [
          {
            "url": "string",
            "retrieval_timestamp_utc": "ISO-8601",
            "source_rank": "A | B | C | D",
            "extracted_passage": "string",
            "contributed_to_determination": "true | false"
          }
        ],
        "sufficient": "true | false",
        "insufficiency_reason": "string or null"
      }
    ],
    "retrieval_count": "integer",
    "retrieval_cap_reached": "true | false",
    "rules_evaluated": [
      {
        "rule_id": "TP-3 | FP-7",
        "preconditions_met": "...",
        "outcome": "...",
        "evidence": {
          "supporting_retrievals": ["url1", "url2"],
          "identifying_facts": ["string"],
          "contradictions": ["string"]
        }
      }
    ]
  },

  "determination": {
    "classification": "true_positive | false_positive | escalate",
    "firing_rule": "rule ID or null",
    "escalation_reason": "string or null",
    "gaps_for_human": ["string array — what additional info would have allowed determination"]
  },

  "narrative": "string — the human-readable narrative described below"
}
```

## Narrative structure

The narrative is a single multi-paragraph string in the `narrative` field of the JSON record. It uses fixed sections in fixed order so reviewers can scan consistently. Use markdown headers (`## Section name`).

### Guiding principles for the narrative

The narrative is for what the analyst needs to understand the disposition. It is not a transcript of every rule the skill considered. Three principles, applied throughout:

1. **Stop at the firing rule.** When a rule fires in a tier, the narrative documents that rule and stops. Don't list non-firing rules from the same tier after the firing rule, and don't mention tiers that were never entered. The JSON record captures everything for audit; the narrative is for the human reader.

2. **Suppress soft signals when a hard rule fires.** If the case is cleanly disposed of (TP or FP via a rule firing), soft signals (gender hint, geographic context, nationality match, partial-DOB mismatch) are not surfaced in the narrative. They are noise that distracts from a clean disposition. Soft signals are surfaced only when the case escalates — then they belong in the evidence package so the analyst sees them.

3. **Be direct.** Don't restate the alert input verbatim in the alert summary — paraphrase to what matters. Don't recite rule specs ("preconditions met: both names have high-confidence parses; both map to the same convention…") — state the relevant facts and the outcome. Don't editorialize confidence ("likely", "appears to be"); a rule either fired or didn't.

### Required sections

**## Alert summary**

One or two sentences. Who was screened, against what list entry. Include the most identifying secondary identifiers if present. Skip null/empty fields.

Example: "Screened: 'Maria Garcia Lopez', individual. Matched against 'María Hernández García' on the OFAC SDN List (individual). No secondary identifiers provided."

**## Name parse**

One short paragraph covering both sides. State the convention, anchor components, and parse confidence. If parse confidence is low on either side, state it and note that structural-mismatch FP rules are disabled.

Example: "Both names parse under Hispanic convention with high confidence. Screened anchor: 'Garcia' (paternal surname); maternal 'Lopez'. Listed anchor: 'Hernández' (paternal surname); maternal 'García'."

**## Tier 1 walkthrough**

One line per rule **up to and including the firing rule**. If no rule fires in Tier 1, list all three with one-sentence outcomes. If a rule fires, stop the walkthrough there — earlier rules in the tier that did not fire can be omitted from the narrative if their non-firing is obvious, or briefly noted if needed for context. Use judgment.

When a rule fires, state in one or two sentences: what condition was met, with the specific evidence (the actual anchor strings, the actual DOBs, the actual types). Don't recite the rule's spec.

**## Tier 2 walkthrough** (only if Tier 1 didn't fire)

Same shape as Tier 1. Same stop-at-firing-rule discipline.

**## Tier 3 walkthrough** (only if Tier 3 was entered)

State the gating basis (G-1, G-2, or G-3) in one sentence. Then per rung that ran: queries used (in the language used), what was retrieved (URL + timestamp + source rank, one-line passage), why the rung was sufficient or insufficient. State whether TP-3 or FP-7 fired with the contributing retrievals identified.

**## Tier 3 gating** (only if Tier 3 was NOT entered and the case escalates)

When the case reaches the Tier 3 boundary and none of G-1, G-2, G-3 holds, state which criteria failed and why in one short paragraph. This is the only place "not applicable" gating reasoning appears in the narrative.

**## Determination**

Classification, firing rule (if any), and a one-sentence reason citing the specific facts. For escalations, add the `gaps_for_human` list (the specific information that would have allowed a determination) and a one-line note that the skill makes no recommendation toward TP or FP — evidence is presented for human assessment.

### What the narrative does NOT include

- "Not evaluated — Tier X stopped on rule Y firing" lines after the firing rule.
- Soft signals when a hard rule has fired.
- Restatement of the JSON alert_input field-by-field.
- Recitation of rule preconditions when the relevant facts can be stated directly.
- Confidence language ("appears to be", "likely", "probably"). A rule fired or it didn't.
- Recommendations on escalations.
- Commentary on screening-system quality, the listed party's conduct, or what the analyst should do operationally beyond the gaps list.

## Output mechanics

When producing the output:

1. Build the JSON record first by populating fields as each tier completes.
2. Generate the narrative from the populated JSON. The narrative is a rendering of the JSON, not an independent commentary.
3. Present both to the user/system. Default presentation order in interactive mode: narrative first (easier for humans to scan), then JSON. In batch mode: JSON only is acceptable if specified by the consuming system.

## What not to include in the output

- No recommendation toward TP or FP on escalations.
- No probability or confidence score in the determination section.
- No narrative summary that contradicts or softens the rule-driven outcome.
- No commentary on the analyst's likely conclusion, on the screening system's quality, or on the listed party's behavior. Stick to identity adjudication.
