---
name: extract-court-filing-data
title: Extract Court Filing Data
description: Extract case numbers, parties, filing dates, court details, and relief sought from court filing documents and legal pleadings.
author: iterationlayer
author_url: https://github.com/iterationlayer/skills/tree/main/skills/extract-court-filing-data
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Extract Court Filing Data

Legal process outsourcing agencies and law firm operations teams use this recipe to digitize court filings — extracting case metadata, party details, and filing information for case management systems.

## APIs Used

Document Extraction (1 credit per page)

## Prerequisites

You need an Iteration Layer API key. Get one at [platform.iterationlayer.com](https://platform.iterationlayer.com) — free trial credits included, no credit card required.

For full integration guidance (SDKs, auth, MCP, error handling), see the [Iteration Layer Integration Guide](https://iterationlayer.com/SKILL.md).

## Implementation


```bash
curl -X POST https://api.iterationlayer.com/document-extraction/v1/extract \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "files": [
      {
        "type": "url",
        "name": "complaint-2026-CV-04821.pdf",
        "url": "https://example.com/legal/complaint-2026-CV-04821.pdf"
      }
    ],
    "schema": {
      "fields": [
        {
          "name": "case_number",
          "type": "TEXT",
          "description": "Court case or docket number"
        },
        {
          "name": "court_name",
          "type": "TEXT",
          "description": "Name of the court"
        },
        {
          "name": "jurisdiction",
          "type": "TEXT",
          "description": "Jurisdiction, e.g. state, federal, district"
        },
        {
          "name": "filing_date",
          "type": "DATE",
          "description": "Date the document was filed"
        },
        {
          "name": "document_type",
          "type": "TEXT",
          "description": "Type of filing, e.g. complaint, motion, answer"
        },
        {
          "name": "plaintiff",
          "type": "TEXT",
          "description": "Plaintiff name or names"
        },
        {
          "name": "defendant",
          "type": "TEXT",
          "description": "Defendant name or names"
        },
        {
          "name": "plaintiff_counsel",
          "type": "TEXT",
          "description": "Attorney or firm representing the plaintiff"
        },
        {
          "name": "defendant_counsel",
          "type": "TEXT",
          "description": "Attorney or firm representing the defendant"
        },
        {
          "name": "cause_of_action",
          "type": "TEXT",
          "description": "Legal cause of action or claim type"
        },
        {
          "name": "relief_sought",
          "type": "TEXTAREA",
          "description": "Summary of relief or damages sought"
        },
        {
          "name": "judge_assigned",
          "type": "TEXT",
          "description": "Assigned judge if listed"
        }
      ]
    }
  }'
```

```typescript
import { IterationLayer } from "iterationlayer";
const client = new IterationLayer({ apiKey: "YOUR_API_KEY" });

const result = await client.extractDocument({
  files: [
    {
      type: "url",
      name: "complaint-2026-CV-04821.pdf",
      url: "https://example.com/legal/complaint-2026-CV-04821.pdf",
    },
  ],
  schema: {
    fields: [
      { name: "case_number", type: "TEXT", description: "Court case or docket number" },
      { name: "court_name", type: "TEXT", description: "Name of the court" },
      { name: "jurisdiction", type: "TEXT", description: "Jurisdiction, e.g. state, federal, district" },
      { name: "filing_date", type: "DATE", description: "Date the document was filed" },
      { name: "document_type", type: "TEXT", description: "Type of filing, e.g. complaint, motion, answer" },
      { name: "plaintiff", type: "TEXT", description: "Plaintiff name or names" },
      { name: "defendant", type: "TEXT", description: "Defendant name or names" },
      { name: "plaintiff_counsel", type: "TEXT", description: "Attorney or firm representing the plaintiff" },
      { name: "defendant_counsel", type: "TEXT", description: "Attorney or firm representing the defendant" },
      { name: "cause_of_action", type: "TEXT", description: "Legal cause of action or claim type" },
      { name: "relief_sought", type: "TEXTAREA", description: "Summary of relief or damages sought" },
      { name: "judge_assigned", type: "TEXT", description: "Assigned judge if listed" },
    ],
  },
});
```

```python
from iterationlayer import IterationLayer
client = IterationLayer(api_key="YOUR_API_KEY")

result = client.extract_document(
    files=[
        {
            "type": "url",
            "name": "complaint-2026-CV-04821.pdf",
            "url": "https://example.com/legal/complaint-2026-CV-04821.pdf",
        }
    ],
    schema={
        "fields": [
            {"name": "case_number", "type": "TEXT", "description": "Court case or docket number"},
            {"name": "court_name", "type": "TEXT", "description": "Name of the court"},
            {"name": "jurisdiction", "type": "TEXT", "description": "Jurisdiction"},
            {"name": "filing_date", "type": "DATE", "description": "Date the document was filed"},
            {"name": "document_type", "type": "TEXT", "description": "Type of filing"},
            {"name": "plaintiff", "type": "TEXT", "description": "Plaintiff name or names"},
            {"name": "defendant", "type": "TEXT", "description": "Defendant name or names"},
            {"name": "plaintiff_counsel", "type": "TEXT", "description": "Attorney or firm representing the plaintiff"},
            {"name": "defendant_counsel", "type": "TEXT", "description": "Attorney or firm representing the defendant"},
            {"name": "cause_of_action", "type": "TEXT", "description": "Legal cause of action or claim type"},
            {"name": "relief_sought", "type": "TEXTAREA", "description": "Summary of relief or damages sought"},
            {"name": "judge_assigned", "type": "TEXT", "description": "Assigned judge if listed"},
        ]
    },
)
```

```go
package main

import il "github.com/iterationlayer/sdk-go"

func main() {
	client := il.NewClient("YOUR_API_KEY")

	result, err := client.ExtractDocument(il.ExtractDocumentRequest{
		Files: []il.FileInput{
			il.FileInput{
				Type: "url",
				Name: "complaint-2026-CV-04821.pdf",
				Url: "https://example.com/legal/complaint-2026-CV-04821.pdf",
			},
		},
		Schema: il.ExtractionSchema{
			Fields: []any{
				il.TextFieldConfig{
					Name: "case_number",
					Type: "TEXT",
					Description: "Court case or docket number",
				},
				il.TextFieldConfig{
					Name: "court_name",
					Type: "TEXT",
					Description: "Name of the court",
				},
				il.TextFieldConfig{
					Name: "jurisdiction",
					Type: "TEXT",
					Description: "Jurisdiction, e.g. state, federal, district",
				},
				il.DateFieldConfig{
					Name: "filing_date",
					Type: "DATE",
					Description: "Date the document was filed",
				},
				il.TextFieldConfig{
					Name: "document_type",
					Type: "TEXT",
					Description: "Type of filing, e.g. complaint, motion, answer",
				},
				il.TextFieldConfig{
					Name: "plaintiff",
					Type: "TEXT",
					Description: "Plaintiff name or names",
				},
				il.TextFieldConfig{
					Name: "defendant",
					Type: "TEXT",
					Description: "Defendant name or names",
				},
				il.TextFieldConfig{
					Name: "plaintiff_counsel",
					Type: "TEXT",
					Description: "Attorney or firm representing the plaintiff",
				},
				il.TextFieldConfig{
					Name: "defendant_counsel",
					Type: "TEXT",
					Description: "Attorney or firm representing the defendant",
				},
				il.TextFieldConfig{
					Name: "cause_of_action",
					Type: "TEXT",
					Description: "Legal cause of action or claim type",
				},
				il.TextareaFieldConfig{
					Name: "relief_sought",
					Type: "TEXTAREA",
					Description: "Summary of relief or damages sought",
				},
				il.TextFieldConfig{
					Name: "judge_assigned",
					Type: "TEXT",
					Description: "Assigned judge if listed",
				},
			},
		},
	})
	if err != nil {
		panic(err)
	}

	_ = result
}
```

```n8n
{
  "name": "Extract court filing data in Iteration Layer",
  "nodes": [
    {
      "parameters": {
        "content": "## Extract Court Filing Data\n\nLegal process outsourcing agencies and law firm operations teams use this recipe to digitize court filings — extracting case metadata, party details, and filing information for case management systems.\n\n**Note:** This workflow uses the Iteration Layer community node (`n8n-nodes-iterationlayer`). Install it via Settings > Community Nodes on self-hosted n8n, or add it directly on n8n Cloud with Verified Community Nodes enabled.",
        "height": 280,
        "width": 500,
        "color": 2
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [200, 40],
      "id": "e1f2a3b4-c5d6-7890-efab-890123456701",
      "name": "Overview"
    },
    {
      "parameters": {
        "content": "### Step 1: Extract Court Filing Data\nResource: **Document Extraction**\n\nConfigure the Document Extraction parameters below, then connect your credentials.",
        "height": 160,
        "width": 300,
        "color": 6
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [475, 100],
      "id": "e1f2a3b4-c5d6-7890-efab-890123456702",
      "name": "Step 1 Note"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "id": "e1f2a3b4-c5d6-7890-efab-890123456703",
      "name": "Manual Trigger"
    },
    {
      "parameters": {
        "resource": "documentExtraction",
        "schemaInputMode": "rawJson",
        "schemaJson": "{\"fields\":[{\"name\":\"case_number\",\"type\":\"TEXT\",\"description\":\"Court case or docket number\"},{\"name\":\"court_name\",\"type\":\"TEXT\",\"description\":\"Name of the court\"},{\"name\":\"jurisdiction\",\"type\":\"TEXT\",\"description\":\"Jurisdiction\"},{\"name\":\"filing_date\",\"type\":\"DATE\",\"description\":\"Date filed\"},{\"name\":\"document_type\",\"type\":\"TEXT\",\"description\":\"Type of filing\"},{\"name\":\"plaintiff\",\"type\":\"TEXT\",\"description\":\"Plaintiff name\"},{\"name\":\"defendant\",\"type\":\"TEXT\",\"description\":\"Defendant name\"},{\"name\":\"plaintiff_counsel\",\"type\":\"TEXT\",\"description\":\"Plaintiff attorney\"},{\"name\":\"defendant_counsel\",\"type\":\"TEXT\",\"description\":\"Defendant attorney\"},{\"name\":\"cause_of_action\",\"type\":\"TEXT\",\"description\":\"Cause of action\"},{\"name\":\"relief_sought\",\"type\":\"TEXTAREA\",\"description\":\"Relief sought\"},{\"name\":\"judge_assigned\",\"type\":\"TEXT\",\"description\":\"Assigned judge\"}]}",
        "files": {
          "fileValues": [
            {
              "fileInputMode": "url",
              "fileName": "complaint-2026-CV-04821.pdf",
              "fileUrl": "https://example.com/legal/complaint-2026-CV-04821.pdf"
            }
          ]
        }
      },
      "type": "n8n-nodes-iterationlayer.iterationLayer",
      "typeVersion": 1,
      "position": [500, 300],
      "id": "e1f2a3b4-c5d6-7890-efab-890123456704",
      "name": "Extract Court Filing Data",
      "credentials": {
        "iterationLayerApi": {
          "id": "1",
          "name": "Iteration Layer API"
        }
      }
    }
  ],
  "connections": {
    "Manual Trigger": {
      "main": [
        [
          {
            "node": "Extract Court Filing Data",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {
    "executionOrder": "v1"
  }
}
```

```prompt
Extract court filing data from the document at [file URL]. Use the extract_document tool with these fields:

- case_number (TEXT): Court case or docket number
- court_name (TEXT): Name of the court
- jurisdiction (TEXT): Jurisdiction, e.g. state, federal, district
- filing_date (DATE): Date the document was filed
- document_type (TEXT): Type of filing, e.g. complaint, motion, answer
- plaintiff (TEXT): Plaintiff name or names
- defendant (TEXT): Defendant name or names
- plaintiff_counsel (TEXT): Attorney or firm representing the plaintiff
- defendant_counsel (TEXT): Attorney or firm representing the defendant
- cause_of_action (TEXT): Legal cause of action or claim type
- relief_sought (TEXTAREA): Summary of relief or damages sought
- judge_assigned (TEXT): Assigned judge if listed
```

### Response


```json
{
  "success": true,
  "data": {
    "case_number": {
      "value": "2026-CV-04821",
      "confidence": 0.99,
      "citations": ["Case No. 2026-CV-04821"]
    },
    "court_name": {
      "value": "Superior Court of New Jersey, Chancery Division",
      "confidence": 0.98,
      "citations": ["Superior Court of New Jersey, Chancery Division"]
    },
    "jurisdiction": {
      "value": "Essex County, New Jersey",
      "confidence": 0.97,
      "citations": ["Essex County"]
    },
    "filing_date": {
      "value": "2026-03-28",
      "confidence": 0.98,
      "citations": ["Filed: March 28, 2026"]
    },
    "document_type": {
      "value": "Complaint",
      "confidence": 0.99,
      "citations": ["COMPLAINT AND DEMAND FOR JURY TRIAL"]
    },
    "plaintiff": {
      "value": "Harborview Properties LLC",
      "confidence": 0.98,
      "citations": ["Plaintiff: Harborview Properties LLC"]
    },
    "defendant": {
      "value": "Coastal Development Group Inc.",
      "confidence": 0.98,
      "citations": ["Defendant: Coastal Development Group Inc."]
    },
    "plaintiff_counsel": {
      "value": "Morgan & Whitfield LLP",
      "confidence": 0.97,
      "citations": ["Attorney for Plaintiff: Morgan & Whitfield LLP"]
    },
    "defendant_counsel": {
      "value": "Not yet assigned",
      "confidence": 0.90,
      "citations": []
    },
    "cause_of_action": {
      "value": "Breach of contract and fraud in the inducement",
      "confidence": 0.96,
      "citations": ["FIRST COUNT: Breach of Contract", "SECOND COUNT: Fraud in the Inducement"]
    },
    "relief_sought": {
      "value": "Compensatory damages in excess of $2,400,000 for losses arising from defendant's failure to complete contracted renovation work, plus punitive damages, attorney fees, and costs of suit.",
      "confidence": 0.93,
      "citations": ["WHEREFORE, Plaintiff demands judgment against Defendant"]
    },
    "judge_assigned": {
      "value": "Hon. Patricia Delgado, J.S.C.",
      "confidence": 0.95,
      "citations": ["Assigned: Hon. Patricia Delgado, J.S.C."]
    }
  }
}
```


## Links

- [Integration guide](https://iterationlayer.com/SKILL.md)
- [Full documentation](https://iterationlayer.com/docs)
- [OpenAPI spec](https://api.iterationlayer.com/openapi.json)
- [Browse all recipes](https://iterationlayer.com/recipes)
