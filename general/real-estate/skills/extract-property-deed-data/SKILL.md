---
name: extract-property-deed-data
title: Extract Property Deed Data
description: Extract property ownership, legal descriptions, encumbrances, and recording details from property deeds and land registry documents.
author: iterationlayer
author_url: https://github.com/iterationlayer/skills/tree/main/skills/extract-property-deed-data
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: real-estate
language: en
---

# Extract Property Deed Data

Real estate agencies and title companies use this recipe to process property deeds — extracting grantor/grantee details, legal descriptions, and encumbrances for title searches and transaction management.

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
        "name": "deed-2026-DR-18742.pdf",
        "url": "https://example.com/deeds/deed-2026-DR-18742.pdf"
      }
    ],
    "schema": {
      "fields": [
        {
          "name": "recording_number",
          "type": "TEXT",
          "description": "Recording or instrument number"
        },
        {
          "name": "recording_date",
          "type": "DATE",
          "description": "Date recorded with the county"
        },
        {
          "name": "deed_type",
          "type": "TEXT",
          "description": "Type of deed, e.g. warranty, quitclaim, grant"
        },
        {
          "name": "grantor",
          "type": "TEXT",
          "description": "Grantor name (seller/transferor)"
        },
        {
          "name": "grantee",
          "type": "TEXT",
          "description": "Grantee name (buyer/transferee)"
        },
        {
          "name": "property_address",
          "type": "ADDRESS",
          "description": "Property street address"
        },
        {
          "name": "legal_description",
          "type": "TEXTAREA",
          "description": "Legal description of the property (lot, block, subdivision)"
        },
        {
          "name": "parcel_number",
          "type": "TEXT",
          "description": "Assessor parcel number or tax ID"
        },
        {
          "name": "consideration_amount",
          "type": "CURRENCY_AMOUNT",
          "description": "Consideration or sale price stated in the deed"
        },
        {
          "name": "encumbrances",
          "type": "TEXTAREA",
          "description": "Easements, liens, or encumbrances noted"
        },
        {
          "name": "notary_name",
          "type": "TEXT",
          "description": "Notary public name"
        },
        {
          "name": "county",
          "type": "TEXT",
          "description": "County where the property is located"
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
      name: "deed-2026-DR-18742.pdf",
      url: "https://example.com/deeds/deed-2026-DR-18742.pdf",
    },
  ],
  schema: {
    fields: [
      { name: "recording_number", type: "TEXT", description: "Recording or instrument number" },
      { name: "recording_date", type: "DATE", description: "Date recorded with the county" },
      { name: "deed_type", type: "TEXT", description: "Type of deed, e.g. warranty, quitclaim, grant" },
      { name: "grantor", type: "TEXT", description: "Grantor name (seller/transferor)" },
      { name: "grantee", type: "TEXT", description: "Grantee name (buyer/transferee)" },
      { name: "property_address", type: "ADDRESS", description: "Property street address" },
      { name: "legal_description", type: "TEXTAREA", description: "Legal description of the property" },
      { name: "parcel_number", type: "TEXT", description: "Assessor parcel number or tax ID" },
      { name: "consideration_amount", type: "CURRENCY_AMOUNT", description: "Consideration or sale price" },
      { name: "encumbrances", type: "TEXTAREA", description: "Easements, liens, or encumbrances noted" },
      { name: "notary_name", type: "TEXT", description: "Notary public name" },
      { name: "county", type: "TEXT", description: "County where the property is located" },
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
            "name": "deed-2026-DR-18742.pdf",
            "url": "https://example.com/deeds/deed-2026-DR-18742.pdf",
        }
    ],
    schema={
        "fields": [
            {"name": "recording_number", "type": "TEXT", "description": "Recording or instrument number"},
            {"name": "recording_date", "type": "DATE", "description": "Date recorded with the county"},
            {"name": "deed_type", "type": "TEXT", "description": "Type of deed"},
            {"name": "grantor", "type": "TEXT", "description": "Grantor name (seller/transferor)"},
            {"name": "grantee", "type": "TEXT", "description": "Grantee name (buyer/transferee)"},
            {"name": "property_address", "type": "ADDRESS", "description": "Property street address"},
            {"name": "legal_description", "type": "TEXTAREA", "description": "Legal description of the property"},
            {"name": "parcel_number", "type": "TEXT", "description": "Assessor parcel number or tax ID"},
            {"name": "consideration_amount", "type": "CURRENCY_AMOUNT", "description": "Consideration or sale price"},
            {"name": "encumbrances", "type": "TEXTAREA", "description": "Easements, liens, or encumbrances noted"},
            {"name": "notary_name", "type": "TEXT", "description": "Notary public name"},
            {"name": "county", "type": "TEXT", "description": "County where the property is located"},
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
				Name: "deed-2026-DR-18742.pdf",
				Url: "https://example.com/deeds/deed-2026-DR-18742.pdf",
			},
		},
		Schema: il.ExtractionSchema{
			Fields: []any{
				il.TextFieldConfig{
					Name: "recording_number",
					Type: "TEXT",
					Description: "Recording or instrument number",
				},
				il.DateFieldConfig{
					Name: "recording_date",
					Type: "DATE",
					Description: "Date recorded with the county",
				},
				il.TextFieldConfig{
					Name: "deed_type",
					Type: "TEXT",
					Description: "Type of deed, e.g. warranty, quitclaim, grant",
				},
				il.TextFieldConfig{
					Name: "grantor",
					Type: "TEXT",
					Description: "Grantor name (seller/transferor)",
				},
				il.TextFieldConfig{
					Name: "grantee",
					Type: "TEXT",
					Description: "Grantee name (buyer/transferee)",
				},
				il.AddressFieldConfig{
					Name: "property_address",
					Type: "ADDRESS",
					Description: "Property street address",
				},
				il.TextareaFieldConfig{
					Name: "legal_description",
					Type: "TEXTAREA",
					Description: "Legal description of the property (lot, block, subdivision)",
				},
				il.TextFieldConfig{
					Name: "parcel_number",
					Type: "TEXT",
					Description: "Assessor parcel number or tax ID",
				},
				il.CurrencyAmountFieldConfig{
					Name: "consideration_amount",
					Type: "CURRENCY_AMOUNT",
					Description: "Consideration or sale price stated in the deed",
				},
				il.TextareaFieldConfig{
					Name: "encumbrances",
					Type: "TEXTAREA",
					Description: "Easements, liens, or encumbrances noted",
				},
				il.TextFieldConfig{
					Name: "notary_name",
					Type: "TEXT",
					Description: "Notary public name",
				},
				il.TextFieldConfig{
					Name: "county",
					Type: "TEXT",
					Description: "County where the property is located",
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
  "name": "Extract property deed data in Iteration Layer",
  "nodes": [
    {
      "parameters": {
        "content": "## Extract Property Deed Data\n\nReal estate agencies and title companies use this recipe to process property deeds — extracting grantor/grantee details, legal descriptions, and encumbrances for title searches and transaction management.\n\n**Note:** This workflow uses the Iteration Layer community node (`n8n-nodes-iterationlayer`). Install it via Settings > Community Nodes on self-hosted n8n, or add it directly on n8n Cloud with Verified Community Nodes enabled.",
        "height": 280,
        "width": 500,
        "color": 2
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [200, 40],
      "id": "f2a3b4c5-d6e7-8901-fabc-901234567801",
      "name": "Overview"
    },
    {
      "parameters": {
        "content": "### Step 1: Extract Deed Data\nResource: **Document Extraction**\n\nConfigure the Document Extraction parameters below, then connect your credentials.",
        "height": 160,
        "width": 300,
        "color": 6
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [475, 100],
      "id": "f2a3b4c5-d6e7-8901-fabc-901234567802",
      "name": "Step 1 Note"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "id": "f2a3b4c5-d6e7-8901-fabc-901234567803",
      "name": "Manual Trigger"
    },
    {
      "parameters": {
        "resource": "documentExtraction",
        "schemaInputMode": "rawJson",
        "schemaJson": "{\"fields\":[{\"name\":\"recording_number\",\"type\":\"TEXT\",\"description\":\"Recording or instrument number\"},{\"name\":\"recording_date\",\"type\":\"DATE\",\"description\":\"Date recorded\"},{\"name\":\"deed_type\",\"type\":\"TEXT\",\"description\":\"Type of deed\"},{\"name\":\"grantor\",\"type\":\"TEXT\",\"description\":\"Grantor name\"},{\"name\":\"grantee\",\"type\":\"TEXT\",\"description\":\"Grantee name\"},{\"name\":\"property_address\",\"type\":\"ADDRESS\",\"description\":\"Property address\"},{\"name\":\"legal_description\",\"type\":\"TEXTAREA\",\"description\":\"Legal description\"},{\"name\":\"parcel_number\",\"type\":\"TEXT\",\"description\":\"Parcel number\"},{\"name\":\"consideration_amount\",\"type\":\"CURRENCY_AMOUNT\",\"description\":\"Consideration amount\"},{\"name\":\"encumbrances\",\"type\":\"TEXTAREA\",\"description\":\"Encumbrances\"},{\"name\":\"notary_name\",\"type\":\"TEXT\",\"description\":\"Notary name\"},{\"name\":\"county\",\"type\":\"TEXT\",\"description\":\"County\"}]}",
        "files": {
          "fileValues": [
            {
              "fileInputMode": "url",
              "fileName": "deed-2026-DR-18742.pdf",
              "fileUrl": "https://example.com/deeds/deed-2026-DR-18742.pdf"
            }
          ]
        }
      },
      "type": "n8n-nodes-iterationlayer.iterationLayer",
      "typeVersion": 1,
      "position": [500, 300],
      "id": "f2a3b4c5-d6e7-8901-fabc-901234567804",
      "name": "Extract Deed Data",
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
            "node": "Extract Deed Data",
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
Extract property deed data from the document at [file URL]. Use the extract_document tool with these fields:

- recording_number (TEXT): Recording or instrument number
- recording_date (DATE): Date recorded with the county
- deed_type (TEXT): Type of deed, e.g. warranty, quitclaim, grant
- grantor (TEXT): Grantor name (seller/transferor)
- grantee (TEXT): Grantee name (buyer/transferee)
- property_address (ADDRESS): Property street address
- legal_description (TEXTAREA): Legal description of the property (lot, block, subdivision)
- parcel_number (TEXT): Assessor parcel number or tax ID
- consideration_amount (CURRENCY_AMOUNT): Consideration or sale price stated in the deed
- encumbrances (TEXTAREA): Easements, liens, or encumbrances noted
- notary_name (TEXT): Notary public name
- county (TEXT): County where the property is located
```

### Response


```json
{
  "success": true,
  "data": {
    "recording_number": {
      "value": "2026-DR-18742",
      "confidence": 0.99,
      "citations": ["Recording No. 2026-DR-18742"]
    },
    "recording_date": {
      "value": "2026-03-15",
      "confidence": 0.98,
      "citations": ["Recorded: March 15, 2026"]
    },
    "deed_type": {
      "value": "General Warranty Deed",
      "confidence": 0.98,
      "citations": ["GENERAL WARRANTY DEED"]
    },
    "grantor": {
      "value": "Robert and Maria Chen, as joint tenants",
      "confidence": 0.97,
      "citations": ["GRANTOR: Robert Chen and Maria Chen, husband and wife, as joint tenants"]
    },
    "grantee": {
      "value": "Lakeview Capital Partners LLC",
      "confidence": 0.98,
      "citations": ["GRANTEE: Lakeview Capital Partners LLC"]
    },
    "property_address": {
      "value": {
        "street": "1247 Magnolia Lane",
        "city": "Raleigh",
        "state": "NC",
        "postal_code": "27607",
        "country": "US"
      },
      "confidence": 0.96,
      "citations": ["1247 Magnolia Lane, Raleigh, NC 27607"]
    },
    "legal_description": {
      "value": "Lot 14, Block C, Magnolia Estates Subdivision, Phase II, as recorded in Plat Book 142, Page 87, Wake County Registry.",
      "confidence": 0.94,
      "citations": ["Lot 14, Block C, Magnolia Estates Subdivision, Phase II, Plat Book 142, Page 87"]
    },
    "parcel_number": {
      "value": "0784-52-4821",
      "confidence": 0.97,
      "citations": ["PIN: 0784-52-4821"]
    },
    "consideration_amount": {
      "value": {
        "amount": "625000.00",
        "currency": "USD"
      },
      "confidence": 0.97,
      "citations": ["for the consideration of $625,000.00"]
    },
    "encumbrances": {
      "value": "Subject to utility easement along the northern 10 feet of the property, recorded in Book 98, Page 214, Wake County Registry.",
      "confidence": 0.92,
      "citations": ["SUBJECT TO: Utility easement along the northern 10 feet"]
    },
    "notary_name": {
      "value": "Jennifer L. Tate",
      "confidence": 0.96,
      "citations": ["Notary Public: Jennifer L. Tate"]
    },
    "county": {
      "value": "Wake County",
      "confidence": 0.99,
      "citations": ["Wake County, North Carolina"]
    }
  }
}
```


## Links

- [Integration guide](https://iterationlayer.com/SKILL.md)
- [Full documentation](https://iterationlayer.com/docs)
- [OpenAPI spec](https://api.iterationlayer.com/openapi.json)
- [Browse all recipes](https://iterationlayer.com/recipes)
