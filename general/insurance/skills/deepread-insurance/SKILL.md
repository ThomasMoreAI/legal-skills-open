---
name: deepread-insurance
title: DeepRead Insurance Document Processing
description: Extract structured data from insurance claims, policies, EOBs, and loss reports. Pre-built schemas for claimant info, coverage, damages, adjuster notes. PII redaction for compliant sharing. 97%+ accuracy. Free 2,000 pages/month.
author: deepread-tech
author_url: https://github.com/deepread-tech/skills/tree/main/skills/insurance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: insurance
language: en
---

# DeepRead Insurance Document Processing

Extract structured data from insurance claims, policy documents, Explanations of Benefits (EOBs), loss reports, and adjuster notes. Then redact claimant PII before sharing with third parties.

> This skill instructs the agent to POST documents to `https://api.deepread.tech` and poll for results. No system files are modified.

## What You Get Back

Submit a claim form and get structured JSON. Extracted fields come back as a list under `extraction.fields[]` (each field has `key`, `value`, `needs_review`, and `location.page`):

```json
{
  "schema_version": "dp02",
  "status": "completed",
  "extraction": {
    "fields": [
      {"key": "claim_number", "value": "CLM-2026-078432", "needs_review": false, "location": {"page": 1}},
      {"key": "policy_number", "value": "POL-HO3-445521", "needs_review": false, "location": {"page": 1}},
      {"key": "claimant_name", "value": "Robert Johnson", "needs_review": false, "location": {"page": 1}},
      {"key": "date_of_loss", "value": "2026-02-14", "needs_review": false, "location": {"page": 1}},
      {"key": "date_reported", "value": "2026-02-15", "needs_review": false, "location": {"page": 1}},
      {"key": "loss_type", "value": "Water Damage", "needs_review": false, "location": {"page": 1}},
      {"key": "loss_description", "value": "Burst pipe in basement caused flooding to finished living area, damaged drywall, carpet, and personal property", "needs_review": false, "location": {"page": 2}},
      {"key": "property_address", "value": "789 Elm Dr, Denver, CO 80202", "needs_review": false, "location": {"page": 1}},
      {"key": "coverage_type", "value": "Homeowners HO-3", "needs_review": false, "location": {"page": 1}},
      {"key": "deductible", "value": 1000.00, "needs_review": false, "location": {"page": 1}},
      {"key": "estimated_damages", "value": 24500.00, "needs_review": true, "review_reason": "Multiple estimates on different pages", "location": {"page": 1}},
      {"key": "adjuster", "value": "Sarah Martinez, License #ADJ-44521", "needs_review": false, "location": {"page": 3}},
      {"key": "line_items", "value": [
        {"category": "Structural", "description": "Drywall replacement — basement", "amount": 8500.00},
        {"category": "Flooring", "description": "Carpet removal and replacement", "amount": 6200.00},
        {"category": "Personal Property", "description": "Damaged furniture and electronics", "amount": 5800.00},
        {"category": "Mitigation", "description": "Water extraction and drying", "amount": 4000.00}
      ], "needs_review": false, "location": {"page": 3}},
      {"key": "status", "value": "Under Review", "needs_review": false, "location": {"page": 1}}
    ]
  }
}
```

Fields with `needs_review: true` need human review (check `review_reason`). Everything else is high-confidence.

## Setup

### Get Your API Key

```bash
open "https://www.deepread.tech/dashboard/?utm_source=clawhub"
```

Save it:
```bash
export DEEPREAD_API_KEY="sk_live_your_key_here"
```

## Insurance Claim Schema

Pre-built schema for insurance claims and loss reports:

```json
{
  "type": "object",
  "properties": {
    "claim_number": {"type": "string", "description": "Claim number or reference ID"},
    "policy_number": {"type": "string", "description": "Insurance policy number"},
    "claimant_name": {"type": "string", "description": "Name of the claimant or insured"},
    "date_of_loss": {"type": "string", "description": "Date the loss or incident occurred (YYYY-MM-DD)"},
    "date_reported": {"type": "string", "description": "Date the claim was reported (YYYY-MM-DD)"},
    "loss_type": {"type": "string", "description": "Type of loss (Water Damage, Fire, Theft, Auto Collision, Liability, etc.)"},
    "loss_description": {"type": "string", "description": "Detailed description of the loss or incident"},
    "property_address": {"type": "string", "description": "Address of the property or location of incident"},
    "coverage_type": {"type": "string", "description": "Type of coverage (Homeowners, Auto, Commercial, Liability, etc.)"},
    "deductible": {"type": "number", "description": "Policy deductible amount"},
    "estimated_damages": {"type": "number", "description": "Total estimated damage amount"},
    "adjuster": {"type": "string", "description": "Claims adjuster name and license number"},
    "line_items": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "category": {"type": "string", "description": "Damage category (Structural, Personal Property, Medical, etc.)"},
          "description": {"type": "string", "description": "Description of damage or expense"},
          "amount": {"type": "number", "description": "Cost or estimate amount"}
        }
      },
      "description": "Itemized list of damages or expenses"
    },
    "status": {"type": "string", "description": "Claim status (Filed, Under Review, Approved, Denied, Settled)"},
    "settlement_amount": {"type": "number", "description": "Final settlement amount if resolved"},
    "denial_reason": {"type": "string", "description": "Reason for denial if applicable"}
  }
}
```

## Extract Data From Insurance Documents

### Python

```python
import requests
import json
import time

API_KEY = "sk_live_YOUR_KEY"
BASE = "https://api.deepread.tech"
headers = {"X-API-Key": API_KEY}

schema = json.dumps({
    "type": "object",
    "properties": {
        "claim_number": {"type": "string", "description": "Claim number"},
        "policy_number": {"type": "string", "description": "Policy number"},
        "claimant_name": {"type": "string", "description": "Claimant name"},
        "date_of_loss": {"type": "string", "description": "Date of loss (YYYY-MM-DD)"},
        "loss_type": {"type": "string", "description": "Type of loss"},
        "loss_description": {"type": "string", "description": "Description of the loss"},
        "coverage_type": {"type": "string", "description": "Coverage type"},
        "deductible": {"type": "number", "description": "Deductible amount"},
        "estimated_damages": {"type": "number", "description": "Total estimated damages"},
        "line_items": {
            "type": "array",
            "items": {"type": "object", "properties": {
                "category": {"type": "string"},
                "description": {"type": "string"},
                "amount": {"type": "number"}
            }},
            "description": "Itemized damages"
        },
        "status": {"type": "string", "description": "Claim status"}
    }
})

with open("claim.pdf", "rb") as f:
    job = requests.post(
        f"{BASE}/v1/process",
        headers=headers,
        files={"file": f},
        data={"schema": schema},
    ).json()

job_id = job["id"]
print(f"Processing: {job_id}")

delay = 5
while True:
    time.sleep(delay)
    result = requests.get(f"{BASE}/v1/jobs/{job_id}", headers=headers).json()

    if result["status"] == "completed":
        fields = result.get("extraction", {}).get("fields", [])
        print(json.dumps(fields, indent=2))

        for f in fields:
            if f.get("needs_review"):
                print(f"\n  REVIEW: {f['key']} — {f.get('review_reason')}")
        break
    elif result["status"] == "failed":
        print(f"Failed: {result.get('error')}")
        break

    delay = min(delay * 1.5, 15)
```

### cURL

```bash
curl -s -X POST https://api.deepread.tech/v1/process \
  -H "X-API-Key: $DEEPREAD_API_KEY" \
  -F "file=@claim.pdf" \
  -F 'schema={"type":"object","properties":{"claim_number":{"type":"string","description":"Claim number"},"policy_number":{"type":"string","description":"Policy number"},"claimant_name":{"type":"string","description":"Claimant name"},"date_of_loss":{"type":"string","description":"Date of loss"},"loss_type":{"type":"string","description":"Type of loss"},"estimated_damages":{"type":"number","description":"Total damages"},"status":{"type":"string","description":"Claim status"}}}'
```

## Redact Claimant PII Before Sharing

Redact claimant personal information before sending to adjusters, contractors, or third-party reviewers:

```python
# Step 1: Extract the claim data you need
with open("claim.pdf", "rb") as f:
    extract_job = requests.post(
        f"{BASE}/v1/process",
        headers=headers,
        files={"file": f},
        data={"schema": schema},
    ).json()

# Step 2: Redact PII from the original
with open("claim.pdf", "rb") as f:
    redact_job = requests.post(
        f"{BASE}/v1/pii/redact",
        headers=headers,
        files={"file": f},
    ).json()

redact_id = redact_job["id"]
delay = 5
while True:
    time.sleep(delay)
    result = requests.get(f"{BASE}/v1/pii/{redact_id}", headers=headers).json()
    if result["status"] == "completed":
        report = result["report"]
        print(f"Redacted {report['total_redactions']} PII instances")
        for pii_type, info in report["pii_detected"].items():
            print(f"  {pii_type}: {info['count']} found")
        pdf = requests.get(result["redacted_file_url"]).content
        with open("claim_redacted.pdf", "wb") as f:
            f.write(pdf)
        print("Saved: claim_redacted.pdf")
        break
    elif result["status"] == "failed":
        print(f"Failed: {result.get('error')}")
        break
    delay = min(delay * 1.5, 15)
```

## Use Cases

- **Claims Processing** — Extract claim numbers, dates, damage descriptions, and amounts from incoming claims
- **Policy Document Analysis** — Pull coverage terms, limits, deductibles, and exclusions from policy documents
- **EOB Processing** — Extract procedure codes, allowed amounts, patient responsibility from Explanations of Benefits
- **Loss Reports** — Parse adjuster field reports for damage categories, estimates, and recommendations
- **Subrogation** — Extract third-party liability information and recovery amounts
- **Fraud Detection** — Batch-process claims and flag inconsistencies in dates, amounts, or descriptions
- **Auto Claims** — Extract vehicle info, driver details, accident descriptions, and repair estimates
- **Workers Comp** — Pull injury descriptions, medical provider info, and lost wage calculations

## Tips for Insurance Documents

- **Specify claim-specific field names** — Using "Claim number or reference ID" works better than just "number"
- **Include status values** — Adding expected statuses (Filed, Under Review, Approved, Denied) in descriptions helps extraction
- **Create blueprints for recurring form types** — If you process the same carrier's claim forms repeatedly, train a blueprint at deepread.tech/dashboard/optimizer for 20-30% improvement
- **Always redact before external sharing** — Use PII redaction before sending to contractors, adjusters, or legal teams

## BYOK — Zero Processing Costs

Connect your own OpenAI, Google, or OpenRouter key via the dashboard. All document processing routes through your provider — zero DeepRead LLM costs, page quota skipped.

Set it up: https://www.deepread.tech/dashboard/byok

## Related DeepRead Skills

- **deepread-ocr** — General OCR and structured extraction — `clawhub install uday390/deepread-ocr`
- **deepread-pii** — Redact PII from any document — `clawhub install uday390/deepread-pii`
- **deepread-form-fill** — Fill PDF forms with AI vision — `clawhub install uday390/deepread-form-fill`
- **deepread-invoice** — Invoice and receipt processing — `clawhub install uday390/deepread-invoice`
- **deepread-medical** — Medical records processing — `clawhub install uday390/deepread-medical`
- **deepread-legal** — Legal document processing — `clawhub install uday390/deepread-legal`
- **deepread-agent-setup** — OAuth device flow authentication — `clawhub install uday390/deepread-agent-setup`
- **deepread-byok** — Bring Your Own Key setup — `clawhub install uday390/deepread-byok`

## Support

- **Dashboard**: https://www.deepread.tech/dashboard
- **Demo Repo**: https://github.com/deepread-tech/deepread-demo
- **n8n Node**: https://www.npmjs.com/package/n8n-nodes-deepread
- **Issues**: https://github.com/deepread-tech/deep-read-service/issues
- **Email**: hello@deepread.tech

---

**Get started free:** https://www.deepread.tech/dashboard/?utm_source=clawhub
