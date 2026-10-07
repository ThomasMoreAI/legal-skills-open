# Example Output

## Scenario

User asks: "Check whether the cited authorities actually support this draft commercial appeal argument."

Access state: live source mode. Claude retrieved DnaNudge Limited v Ventura Capital GP Limited [2023] EWCA Civ 1142 from Find Case Law.

## Good Output Shape

```yaml
access_mode: live_source
source_register:
  - id: "DnaNudge [2023] EWCA Civ 1142"
    type: public_judgment
    source: "Find Case Law"
    url: "https://caselaw.nationalarchives.gov.uk/ewca/civ/2023/1142"
    date_checked: "2026-05-10"

propositions:
  - paragraph: 18
    proposition: "DnaNudge concerned the interpretation of articles of association and conversion of Series A shares."
    proposition_type: legal/factual background
    citation: "DnaNudge [2023] EWCA Civ 1142 at [1]"
    status: supported
    confidence: high
    source_location: "Find Case Law, para 1"
    source_excerpt: "The case concerns the interpretation of the Articles of Association of the Company..."
    problem: ""
    suggested_fix: "Keep, with accurate pinpoint."

  - paragraph: 24
    proposition: "The Court of Appeal endorsed an iterative approach to contractual interpretation that checks rival meanings against the document and commercial consequences."
    proposition_type: legal
    citation: "DnaNudge [2023] EWCA Civ 1142 at [41]-[43]"
    status: supported
    confidence: high
    source_location: "Find Case Law, paras 41-43"
    source_excerpt: "the process of interpretation is an iterative one in which potential meanings... are tested against... commercial consequences"
    problem: ""
    suggested_fix: "Keep, subject to citation formatting."

  - paragraph: 31
    proposition: "The authorities establish a strict no-loss rule."
    proposition_type: legal
    citation: "[2018] EWCA Civ 404"
    status: unverified-source-unavailable
    confidence: low
    source_location: source_missing
    problem: "No authority text, URL, or live access available."
    suggested_fix: "Provide judgment text/URL or move to verification queue."

dependency_risk:
  - argument: "Ground 2: commercial absurdity"
    risk: "Supported in principle by DnaNudge/Arnold/Wood line, but the draft still needs to show the rival construction is textually available."
    action: "Tie commercial-consequence argument back to the clause wording before relying on it."
```

## Bad Output To Avoid

```text
That case probably supports the point because it is a well-known principle.
```

Do not assess support from model memory.
