---
name: extract-nda-terms
title: Extract NDA Terms
description: Extract parties, obligations, restrictions, permitted disclosures, and expiry dates from non-disclosure agreements.
author: iterationlayer
author_url: https://github.com/iterationlayer/skills/tree/main/skills/extract-nda-terms
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Extract NDA Terms

Legal teams and contract managers use this recipe to extract key terms from NDAs at scale — pulling out parties, confidentiality scope, duration, permitted disclosures, and governing law for centralized tracking and compliance review.

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
        "name": "nda-vanguard-tech.pdf",
        "url": "https://example.com/legal/nda-vanguard-tech-2026.pdf"
      }
    ],
    "schema": {
      "fields": [
        {
          "name": "disclosing_party",
          "type": "TEXT",
          "description": "Name of the disclosing party"
        },
        {
          "name": "receiving_party",
          "type": "TEXT",
          "description": "Name of the receiving party"
        },
        {
          "name": "effective_date",
          "type": "DATE",
          "description": "NDA effective date"
        },
        {
          "name": "expiry_date",
          "type": "DATE",
          "description": "NDA expiration or end date"
        },
        {
          "name": "confidentiality_duration",
          "type": "TEXT",
          "description": "Duration of confidentiality obligations"
        },
        {
          "name": "scope_of_confidential_info",
          "type": "TEXTAREA",
          "description": "Definition and scope of confidential information"
        },
        {
          "name": "permitted_disclosures",
          "type": "TEXTAREA",
          "description": "Exceptions or permitted disclosures"
        },
        {
          "name": "return_of_materials",
          "type": "TEXTAREA",
          "description": "Obligations to return or destroy materials"
        },
        {
          "name": "non_solicitation",
          "type": "BOOLEAN",
          "description": "Whether the NDA includes a non-solicitation clause"
        },
        {
          "name": "governing_law",
          "type": "TEXT",
          "description": "Governing law and jurisdiction"
        },
        {
          "name": "breach_remedies",
          "type": "TEXTAREA",
          "description": "Remedies available in case of breach"
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
      name: "nda-vanguard-tech.pdf",
      url: "https://example.com/legal/nda-vanguard-tech-2026.pdf",
    },
  ],
  schema: {
    fields: [
      { name: "disclosing_party", type: "TEXT", description: "Name of the disclosing party" },
      { name: "receiving_party", type: "TEXT", description: "Name of the receiving party" },
      { name: "effective_date", type: "DATE", description: "NDA effective date" },
      { name: "expiry_date", type: "DATE", description: "NDA expiration or end date" },
      { name: "confidentiality_duration", type: "TEXT", description: "Duration of confidentiality obligations" },
      { name: "scope_of_confidential_info", type: "TEXTAREA", description: "Definition and scope of confidential information" },
      { name: "permitted_disclosures", type: "TEXTAREA", description: "Exceptions or permitted disclosures" },
      { name: "return_of_materials", type: "TEXTAREA", description: "Obligations to return or destroy materials" },
      { name: "non_solicitation", type: "BOOLEAN", description: "Whether the NDA includes a non-solicitation clause" },
      { name: "governing_law", type: "TEXT", description: "Governing law and jurisdiction" },
      { name: "breach_remedies", type: "TEXTAREA", description: "Remedies available in case of breach" },
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
            "name": "nda-vanguard-tech.pdf",
            "url": "https://example.com/legal/nda-vanguard-tech-2026.pdf",
        }
    ],
    schema={
        "fields": [
            {"name": "disclosing_party", "type": "TEXT", "description": "Name of the disclosing party"},
            {"name": "receiving_party", "type": "TEXT", "description": "Name of the receiving party"},
            {"name": "effective_date", "type": "DATE", "description": "NDA effective date"},
            {"name": "expiry_date", "type": "DATE", "description": "NDA expiration or end date"},
            {"name": "confidentiality_duration", "type": "TEXT", "description": "Duration of confidentiality obligations"},
            {"name": "scope_of_confidential_info", "type": "TEXTAREA", "description": "Definition and scope of confidential information"},
            {"name": "permitted_disclosures", "type": "TEXTAREA", "description": "Exceptions or permitted disclosures"},
            {"name": "return_of_materials", "type": "TEXTAREA", "description": "Obligations to return or destroy materials"},
            {"name": "non_solicitation", "type": "BOOLEAN", "description": "Whether the NDA includes a non-solicitation clause"},
            {"name": "governing_law", "type": "TEXT", "description": "Governing law and jurisdiction"},
            {"name": "breach_remedies", "type": "TEXTAREA", "description": "Remedies available in case of breach"},
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
				Name: "nda-vanguard-tech.pdf",
				Url: "https://example.com/legal/nda-vanguard-tech-2026.pdf",
			},
		},
		Schema: il.ExtractionSchema{
			Fields: []any{
				il.TextFieldConfig{
					Name: "disclosing_party",
					Type: "TEXT",
					Description: "Name of the disclosing party",
				},
				il.TextFieldConfig{
					Name: "receiving_party",
					Type: "TEXT",
					Description: "Name of the receiving party",
				},
				il.DateFieldConfig{
					Name: "effective_date",
					Type: "DATE",
					Description: "NDA effective date",
				},
				il.DateFieldConfig{
					Name: "expiry_date",
					Type: "DATE",
					Description: "NDA expiration or end date",
				},
				il.TextFieldConfig{
					Name: "confidentiality_duration",
					Type: "TEXT",
					Description: "Duration of confidentiality obligations",
				},
				il.TextareaFieldConfig{
					Name: "scope_of_confidential_info",
					Type: "TEXTAREA",
					Description: "Definition and scope of confidential information",
				},
				il.TextareaFieldConfig{
					Name: "permitted_disclosures",
					Type: "TEXTAREA",
					Description: "Exceptions or permitted disclosures",
				},
				il.TextareaFieldConfig{
					Name: "return_of_materials",
					Type: "TEXTAREA",
					Description: "Obligations to return or destroy materials",
				},
				il.BooleanFieldConfig{
					Name: "non_solicitation",
					Type: "BOOLEAN",
					Description: "Whether the NDA includes a non-solicitation clause",
				},
				il.TextFieldConfig{
					Name: "governing_law",
					Type: "TEXT",
					Description: "Governing law and jurisdiction",
				},
				il.TextareaFieldConfig{
					Name: "breach_remedies",
					Type: "TEXTAREA",
					Description: "Remedies available in case of breach",
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
  "name": "Extract NDA terms in Iteration Layer",
  "nodes": [
    {
      "parameters": {
        "content": "## Extract NDA Terms\n\nLegal teams and contract managers use this recipe to extract key terms from NDAs at scale — pulling out parties, confidentiality scope, duration, permitted disclosures, and governing law for centralized tracking and compliance review.\n\n**Note:** This workflow uses the Iteration Layer community node (`n8n-nodes-iterationlayer`). Install it via Settings > Community Nodes on self-hosted n8n, or add it directly on n8n Cloud with Verified Community Nodes enabled.",
        "height": 280,
        "width": 500,
        "color": 2
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [200, 40],
      "id": "d1e2f3a4-b5c6-7890-defa-567890123401",
      "name": "Overview"
    },
    {
      "parameters": {
        "content": "### Step 1: Extract NDA Terms\nResource: **Document Extraction**\n\nConfigure the Document Extraction parameters below, then connect your credentials.",
        "height": 160,
        "width": 300,
        "color": 6
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [475, 100],
      "id": "d1e2f3a4-b5c6-7890-defa-567890123402",
      "name": "Step 1 Note"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "id": "d1e2f3a4-b5c6-7890-defa-567890123403",
      "name": "Manual Trigger"
    },
    {
      "parameters": {
        "resource": "documentExtraction",
        "schemaInputMode": "rawJson",
        "schemaJson": "{\"fields\":[{\"name\":\"disclosing_party\",\"type\":\"TEXT\",\"description\":\"Name of the disclosing party\"},{\"name\":\"receiving_party\",\"type\":\"TEXT\",\"description\":\"Name of the receiving party\"},{\"name\":\"effective_date\",\"type\":\"DATE\",\"description\":\"NDA effective date\"},{\"name\":\"expiry_date\",\"type\":\"DATE\",\"description\":\"NDA expiration or end date\"},{\"name\":\"confidentiality_duration\",\"type\":\"TEXT\",\"description\":\"Duration of confidentiality obligations\"},{\"name\":\"scope_of_confidential_info\",\"type\":\"TEXTAREA\",\"description\":\"Definition and scope of confidential information\"},{\"name\":\"permitted_disclosures\",\"type\":\"TEXTAREA\",\"description\":\"Exceptions or permitted disclosures\"},{\"name\":\"return_of_materials\",\"type\":\"TEXTAREA\",\"description\":\"Obligations to return or destroy materials\"},{\"name\":\"non_solicitation\",\"type\":\"BOOLEAN\",\"description\":\"Whether the NDA includes a non-solicitation clause\"},{\"name\":\"governing_law\",\"type\":\"TEXT\",\"description\":\"Governing law and jurisdiction\"},{\"name\":\"breach_remedies\",\"type\":\"TEXTAREA\",\"description\":\"Remedies available in case of breach\"}]}",
        "files": {
          "fileValues": [
            {
              "fileInputMode": "url",
              "fileName": "nda-vanguard-tech.pdf",
              "fileUrl": "https://example.com/legal/nda-vanguard-tech-2026.pdf"
            }
          ]
        }
      },
      "type": "n8n-nodes-iterationlayer.iterationLayer",
      "typeVersion": 1,
      "position": [500, 300],
      "id": "d1e2f3a4-b5c6-7890-defa-567890123404",
      "name": "Extract NDA Terms",
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
            "node": "Extract NDA Terms",
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
Extract NDA terms from the file at [file URL]. Use the extract_document tool with these fields:

- disclosing_party (TEXT): Name of the disclosing party
- receiving_party (TEXT): Name of the receiving party
- effective_date (DATE): NDA effective date
- expiry_date (DATE): NDA expiration or end date
- confidentiality_duration (TEXT): Duration of confidentiality obligations
- scope_of_confidential_info (TEXTAREA): Definition and scope of confidential information
- permitted_disclosures (TEXTAREA): Exceptions or permitted disclosures
- return_of_materials (TEXTAREA): Obligations to return or destroy materials
- non_solicitation (BOOLEAN): Whether the NDA includes a non-solicitation clause
- governing_law (TEXT): Governing law and jurisdiction
- breach_remedies (TEXTAREA): Remedies available in case of breach
```

### Response


```json
{
  "success": true,
  "data": {
    "disclosing_party": {
      "value": "Vanguard Technologies Inc.",
      "confidence": 0.99,
      "citations": ["Disclosing Party: Vanguard Technologies Inc."]
    },
    "receiving_party": {
      "value": "Meridian Consulting Group",
      "confidence": 0.98,
      "citations": ["Receiving Party: Meridian Consulting Group"]
    },
    "effective_date": {
      "value": "2026-04-01",
      "confidence": 0.99,
      "citations": ["Effective Date: April 1, 2026"]
    },
    "expiry_date": {
      "value": "2029-04-01",
      "confidence": 0.95,
      "citations": ["This Agreement shall remain in effect for three (3) years from the Effective Date"]
    },
    "confidentiality_duration": {
      "value": "3 years from the effective date",
      "confidence": 0.97,
      "citations": ["Confidentiality obligations shall survive for a period of three (3) years"]
    },
    "scope_of_confidential_info": {
      "value": "All technical specifications, business plans, customer data, financial projections, and proprietary algorithms shared by the Disclosing Party in written or electronic form.",
      "confidence": 0.96,
      "citations": ["Confidential Information includes all technical specifications, business plans, customer data, financial projections, and proprietary algorithms"]
    },
    "permitted_disclosures": {
      "value": "Disclosures required by court order, regulatory requirement, or applicable law. Information that becomes publicly available through no fault of the Receiving Party. Information independently developed without reference to Confidential Information.",
      "confidence": 0.95,
      "citations": ["Exceptions: (a) disclosures required by court order or applicable law; (b) information that becomes publicly available; (c) independently developed information"]
    },
    "return_of_materials": {
      "value": "All confidential materials must be returned or certified destroyed within 30 days of written request or termination of the agreement.",
      "confidence": 0.96,
      "citations": ["The Receiving Party shall return or certify destruction of all Confidential Information within thirty (30) days"]
    },
    "non_solicitation": {
      "value": true,
      "confidence": 0.94,
      "citations": ["Neither party shall solicit employees of the other party for a period of twelve (12) months"]
    },
    "governing_law": {
      "value": "Germany",
      "confidence": 0.98,
      "citations": ["Governed by the laws of Germany"]
    },
    "breach_remedies": {
      "value": "The Disclosing Party is entitled to injunctive relief without posting bond, in addition to any other remedies available at law or in equity. The breaching party shall be liable for all damages and reasonable attorney fees.",
      "confidence": 0.95,
      "citations": ["The Disclosing Party shall be entitled to seek injunctive relief without the necessity of posting any bond"]
    }
  }
}
```


## Links

- [Integration guide](https://iterationlayer.com/SKILL.md)
- [Full documentation](https://iterationlayer.com/docs)
- [OpenAPI spec](https://api.iterationlayer.com/openapi.json)
- [Browse all recipes](https://iterationlayer.com/recipes)
