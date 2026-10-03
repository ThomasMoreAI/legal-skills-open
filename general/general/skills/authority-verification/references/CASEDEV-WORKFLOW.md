# case.dev Authority Verification Workflow

This skill uses generic authority-verification terminology instead of vendor-branded citator language.

## Table of Contents

- [Scope](#scope)
- [Endpoint Map](#endpoint-map)
- [Recommended Sequence](#recommended-sequence)
- [Status Handling](#status-handling)
- [Terminology Rules](#terminology-rules)
- [Python SDK Notes](#python-sdk-notes)

## Scope

case.dev Legal Research supports:

- citation verification
- legal source search
- deep multi-query research
- similar-authority discovery
- citation extraction from text or URLs
- full document retrieval with highlights

It does not claim proprietary editorial treatment labels or branded citator signals.

## Endpoint Map

Docs:

- `POST /legal/v1/verify`
- `POST /legal/v1/find`
- `POST /legal/v1/research`
- `POST /legal/v1/similar`
- `POST /legal/v1/citations`
- `POST /legal/v1/citations-from-url`
- `POST /legal/v1/full-text`

Primary CLI equivalents:

```bash
casedev legal:v1 verify --text "531 U.S. 98"
casedev legal:v1 find --query "qualified immunity excessive force" --jurisdiction us-federal
casedev legal:v1 research \
  --query "employment discrimination disparate impact" \
  --additional-queries "Title VII disparate impact theory" \
  --additional-queries "Griggs v Duke Power significance"
casedev legal:v1 similar --url "https://www.courtlistener.com/opinion/118365/bush-v-gore/"
casedev legal:v1 get-full-text --url "https://www.courtlistener.com/opinion/118365/bush-v-gore/"
```

## Recommended Sequence

1. Verify the exact citation with `legal.verify`.
2. If verified, use the returned URL with `legal.fullText`.
3. Expand to related authorities with `legal.similar`.
4. If the issue is broader than one citation, use `legal.research` with 2-4 additional phrasings.
5. If reviewing a document, extract its authorities first with `legal.citations` or `legal.citationsFromUrl`.

## Status Handling

`verified`
: Citation matches a real authority in the database.

`not_found`
: No matching authority found. Check typos, reporter, year, or hallucinated text.

`multiple_matches`
: More than one plausible match. Manual review is required before citing.

## Terminology Rules

Use:

- verified citation
- candidate authority
- related authority
- source document
- manual treatment review

Avoid:

- Shepardize
- Shepardizing
- Shepard's report
- Shepard's Signal
- KeyCite
- good law

## Python SDK Notes

Docs use:

```python
import casedev

client = casedev.Casedev(api_key=os.environ["CASEDEV_API_KEY"])
```

Common calls:

```python
client.legal.v1.verify(text="531 U.S. 98")
client.legal.v1.find(query="qualified immunity excessive force", jurisdiction="us-federal")
client.legal.v1.research(
    query="employment discrimination disparate impact",
    additional_queries=[
        "Title VII disparate impact theory",
        "Griggs v Duke Power significance",
    ],
    jurisdiction="us-federal",
    num_results=15,
)
client.legal.v1.similar(url="https://www.courtlistener.com/opinion/118365/bush-v-gore/")
client.legal.v1.get_full_text(url="https://www.courtlistener.com/opinion/118365/bush-v-gore/")
```
