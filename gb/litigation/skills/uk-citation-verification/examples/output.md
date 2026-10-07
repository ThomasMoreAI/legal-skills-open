# Example Output

## Scenario

User asks: "Check the UK citations in this skeleton. I have not uploaded the judgments."

Access state: mixed. Claude has web access for Find Case Law/BAILII, but one authority cannot be retrieved.

## Good Output Shape

```yaml
access_mode: live_source
date_checked: "2026-05-10"

citations:
  - citation: "[2023] EWCA Civ 100"
    document_location: "Skeleton para 14"
    cited_case_name: "DnaNudge Ltd v Ventura Capital GP Ltd"
    retrieved_case_name: "DnaNudge Limited v Ventura Capital GP Limited"
    retrieved_citation: "[2023] EWCA Civ 1142"
    retrieved_court_date: "Court of Appeal, 2023-10-05"
    status: verified
    confidence: high
    matched_source: "Find Case Law"
    source_type: public database
    sources_searched:
      - source: "Find Case Law"
        query: '"DnaNudge" "[2023] EWCA Civ 1142"'
        result: "matched"
    issue: "Citation number in draft is wrong: draft says [2023] EWCA Civ 100; retrieved source is [2023] EWCA Civ 1142."
    suggested_next_step: "Correct neutral citation and party-name spelling."

  - citation: "[2021] EWCA Civ 9999"
    document_location: "Skeleton para 22"
    cited_case_name: "Case name as drafted; no retrieved public match"
    status: citation-not-found
    confidence: high
    matched_source: ""
    source_type: public database
    sources_searched:
      - source: "Find Case Law"
        query: '"[2021] EWCA Civ 9999"'
        result: "no match"
      - source: "BAILII"
        query: '"Acme Trading Ltd" "North Wharf"'
        result: "no match"
    issue: "No matching public authority found from the sources searched."
    suggested_next_step: "Check whether citation or party names are wrong; provide judgment text or subscription-source result if available."

  - citation: "[2019] EWCA Civ 55"
    document_location: "Skeleton para 31 quote"
    cited_case_name: "Lindner v Rawlins"
    retrieved_case_name: "Lindner v Rawlins"
    retrieved_citation: "[2015] EWCA Civ 61"
    status: citation-mismatch
    confidence: medium
    matched_source: "BAILII"
    source_type: public database
    issue: "Party names point to a real EWCA authority, but the citation in the draft is wrong."
    suggested_next_step: "Correct citation before checking any paragraph or quote."
```

## No-Source Mode

```yaml
access_mode: no_source
citations_extracted:
  - "[2023] EWCA Civ 100"
  - "[2021] EWCA Civ 9999"
verification_status: unverified-source-unavailable
next_step: "Provide FCL/BAILII URLs, judgment text, or enable web/browser access."
```
