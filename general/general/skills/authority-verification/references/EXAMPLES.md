# Examples

## Table of Contents

- [Verified citation check](#verified-citation-check)
- [Unverified citation handling](#unverified-citation-handling)
- [Document audit workflow](#document-audit-workflow)

## Verified Citation Check

Goal: verify a citation, pull source text, and expand to related authorities.

CLI:

```bash
bash scripts/verify_authority.sh "531 U.S. 98" "equal protection"
```

Python:

```bash
python3 scripts/verify_authority.py --citation "531 U.S. 98" --highlight-query "equal protection"
```

TypeScript:

```bash
npx tsx scripts/verify_authority.ts --citation "531 U.S. 98" --highlight-query "equal protection"
```

Expected result shape:

```json
{
  "citation": "531 U.S. 98",
  "summary": {
    "verified": 1
  },
  "results": [
    {
      "status": "verified",
      "case": {
        "name": "Bush v. Gore"
      },
      "highlights": [],
      "relatedAuthorities": []
    }
  ]
}
```

## Unverified Citation Handling

Goal: catch a likely hallucinated or malformed citation and stop before citing it.

CLI:

```bash
casedev legal:v1 verify --text "Smith v. Jones, 542 U.S. 123" --json
```

Expected behavior:

- If `not_found > 0`, do not cite the case.
- Search by issue instead:

```bash
casedev legal:v1 find --query "topic from the bad citation" --num-results 5 --json
```

## Document Audit Workflow

Goal: extract authorities from a document URL, then verify key citations individually.

Extract:

```bash
casedev legal:v1 citations-from-url \
  --url "https://www.courtlistener.com/opinion/118365/bush-v-gore/" \
  --json
```

Then verify a citation from the extracted list:

```bash
casedev legal:v1 verify --text "531 U.S. 98" --json
```

Use this when reviewing a brief, article, or opinion for citation hygiene.
