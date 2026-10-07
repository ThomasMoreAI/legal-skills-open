# Example Output

## Scenario

User asks: "Check whether this commercial appeal skeleton is aligned with public Court of Appeal drafting signals in recent contract/construction appeals."

Access state: live source mode. Claude retrieved DnaNudge Limited v Ventura Capital GP Limited [2023] EWCA Civ 1142 and Palladian Partners LP v Republic of Argentina [2024] EWCA Civ 641 from Find Case Law.

## Good Output Shape

```yaml
access_mode: live_source
court_context:
  document_type: skeleton
  court: Court of Appeal
  context: civil_commercial
  procedural_stage: permission_refused_below_renewed_oral
  known_panel_or_judges:
    - name: "Unknown"
      status: unknown

source_corpus:
  sources_searched:
    - source: "Find Case Law"
      query: '"EWCA Civ" commercial contract construction "commercial consequences"'
      date_checked: "2026-05-10"
  included_decisions:
    - case_name: "DnaNudge Limited v Ventura Capital GP Limited"
      neutral_citation: "[2023] EWCA Civ 1142"
      judge_or_panel: "Lord Justice Snowden"
      source_url: "https://caselaw.nationalarchives.gov.uk/ewca/civ/2023/1142"
      date_checked: "2026-05-10"
      reason_for_inclusion: "Court of Appeal company/articles construction appeal discussing commercial consequences."
    - case_name: "Palladian Partners LP v The Republic of Argentina"
      neutral_citation: "[2024] EWCA Civ 641"
      judge_or_panel: "Lord Justice Popplewell"
      source_url: "https://caselaw.nationalarchives.gov.uk/ewca/civ/2024/641"
      date_checked: "2026-05-10"
      reason_for_inclusion: "Court of Appeal securities construction appeal with detailed economic/commercial consequences analysis."
  corpus_limits:
    - "Only two public judgments included in this illustration."
    - "No judge-specific finding because no known panel was supplied."
    - "Judgments are not skeleton arguments; findings are drafting signals only."

preference_findings:
  - dimension: commercial_pragmatism
    observation: "The public sample treats commercial consequences as part of an iterative construction exercise, but still anchors the analysis in the wording and structure of the instrument."
    scope: case_type_specific
    confidence: medium
    supporting_sources:
      - case_name: "DnaNudge Limited v Ventura Capital GP Limited"
        neutral_citation: "[2023] EWCA Civ 1142"
        paragraphs: "41-43"
        excerpt: "the process of interpretation is an iterative one... tested against... commercial consequences"
        source_url: "https://caselaw.nationalarchives.gov.uk/ewca/civ/2023/1142"
      - case_name: "Palladian Partners LP v The Republic of Argentina"
        neutral_citation: "[2024] EWCA Civ 641"
        paragraphs: "49-50"
        excerpt: "the iterative process involved in ascertaining the meaning of the words used... and the economic and commercial consequences"
        source_url: "https://caselaw.nationalarchives.gov.uk/ewca/civ/2024/641"
    uncertainty: "Medium confidence: small public sample; no judge-specific inference."

  - dimension: factual_narrative
    observation: "The public sample opens by identifying the issue on appeal before expanding into background detail."
    scope: case_type_specific
    confidence: medium
    supporting_sources:
      - case_name: "DnaNudge Limited v Ventura Capital GP Limited"
        neutral_citation: "[2023] EWCA Civ 1142"
        paragraphs: "1"
        excerpt: "The case concerns the interpretation of the Articles of Association..."
        source_url: "https://caselaw.nationalarchives.gov.uk/ewca/civ/2023/1142"
      - case_name: "Palladian Partners LP v The Republic of Argentina"
        neutral_citation: "[2024] EWCA Civ 641"
        paragraphs: "1-2"
        excerpt: "This appeal is concerned with the proper construction of a short provision..."
        source_url: "https://caselaw.nationalarchives.gov.uk/ewca/civ/2024/641"
    uncertainty: "Signals are from judgments, not skeleton arguments."

draft_assessment:
  strengths:
    - location: "Ground 1 heading"
      point: "Identifies alleged error of law directly."
      source_linked_reason: "Aligned with issue-first structure in comparator decisions."
  risks:
    - location: "Facts section, paras 5-29"
      issue: "Long factual narrative delays identification of appellate error."
      severity: major
      why_it_matters: "Comparator decisions in this corpus use short fact summaries before analysis."
      supporting_preference_finding: factual_narrative
      suggested_revision_direction: "Cut background facts to what is needed for Ground 1 and move detail to chronology or appendix."
    - location: "Ground 2, paras 45-52"
      issue: "Argument is framed as broad fairness rather than wording, structure, and commercial consequence."
      severity: major
      why_it_matters: "Comparator decisions use commercial consequences inside an iterative construction analysis, not as a free-standing fairness appeal."
      supporting_preference_finding: commercial_pragmatism
      suggested_revision_direction: "Lead with clause wording, then show the commercial consequence of the rival construction."

legal_safety:
  not_legal_advice: true
  outcome_prediction: prohibited
  citation_verification_status: style_sources_only
```

## No-Source Mode

```yaml
access_mode: no_source
output: draft_structure_review_only
not_done:
  - "No judge-specific preference findings."
  - "No public-source Court of Appeal corpus."
next_step: "Provide public judgments, FCL/BAILII URLs, or enable web access."
```
