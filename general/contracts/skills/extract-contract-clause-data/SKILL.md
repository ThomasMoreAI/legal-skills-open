---
name: extract-contract-clause-data
title: Extract Contract Clause Data
description: Extract parties, dates, and clauses from a contract into structured JSON for legal review workflows.
author: iterationlayer
author_url: https://github.com/iterationlayer/skills/tree/main/skills/extract-contract-clause-data
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Extract Contract Clause Data

Legal teams and contract management platforms use this recipe to automate contract review. Upload a contract and receive structured JSON with involved parties, key dates, and individual clauses — ready for a compliance check, risk analysis, or contract database.

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
        "name": "contract.pdf",
        "url": "https://example.com/contracts/service-agreement.pdf"
      }
    ],
    "schema": {
      "fields": [
        {
          "name": "parties",
          "type": "ARRAY",
          "description": "Parties involved in the contract",
          "fields": [
            {
              "name": "name",
              "type": "TEXT",
              "description": "Name of the party"
            },
            {
              "name": "role",
              "type": "TEXT",
              "description": "Role of the party (e.g. client, provider)"
            }
          ]
        },
        {
          "name": "effective_date",
          "type": "DATE",
          "description": "Date the contract takes effect"
        },
        {
          "name": "termination_date",
          "type": "DATE",
          "description": "Date the contract expires or terminates"
        },
        {
          "name": "clauses",
          "type": "ARRAY",
          "description": "Individual contract clauses",
          "fields": [
            {
              "name": "title",
              "type": "TEXT",
              "description": "Clause heading or title"
            },
            {
              "name": "content",
              "type": "TEXTAREA",
              "description": "Full text of the clause"
            }
          ]
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
      name: "contract.pdf",
      url: "https://example.com/contracts/service-agreement.pdf",
    },
  ],
  schema: {
    fields: [
      {
        name: "parties",
        type: "ARRAY",
        description: "Parties involved in the contract",
        fields: [
          {
            name: "name",
            type: "TEXT",
            description: "Name of the party",
          },
          {
            name: "role",
            type: "TEXT",
            description: "Role of the party (e.g. client, provider)",
          },
        ],
      },
      {
        name: "effective_date",
        type: "DATE",
        description: "Date the contract takes effect",
      },
      {
        name: "termination_date",
        type: "DATE",
        description: "Date the contract expires or terminates",
      },
      {
        name: "clauses",
        type: "ARRAY",
        description: "Individual contract clauses",
        fields: [
          {
            name: "title",
            type: "TEXT",
            description: "Clause heading or title",
          },
          {
            name: "content",
            type: "TEXTAREA",
            description: "Full text of the clause",
          },
        ],
      },
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
            "name": "contract.pdf",
            "url": "https://example.com/contracts/service-agreement.pdf",
        }
    ],
    schema={
        "fields": [
            {
                "name": "parties",
                "type": "ARRAY",
                "description": "Parties involved in the contract",
                "fields": [
                    {
                        "name": "name",
                        "type": "TEXT",
                        "description": "Name of the party",
                    },
                    {
                        "name": "role",
                        "type": "TEXT",
                        "description": "Role of the party (e.g. client, provider)",
                    },
                ],
            },
            {
                "name": "effective_date",
                "type": "DATE",
                "description": "Date the contract takes effect",
            },
            {
                "name": "termination_date",
                "type": "DATE",
                "description": "Date the contract expires or terminates",
            },
            {
                "name": "clauses",
                "type": "ARRAY",
                "description": "Individual contract clauses",
                "fields": [
                    {
                        "name": "title",
                        "type": "TEXT",
                        "description": "Clause heading or title",
                    },
                    {
                        "name": "content",
                        "type": "TEXTAREA",
                        "description": "Full text of the clause",
                    },
                ],
            },
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
				Name: "contract.pdf",
				Url: "https://example.com/contracts/service-agreement.pdf",
			},
		},
		Schema: il.ExtractionSchema{
			Fields: []any{
				il.ArrayFieldConfig{
					Name: "parties",
					Type: "ARRAY",
					Description: "Parties involved in the contract",
					Fields: []any{
						il.TextFieldConfig{
							Name: "name",
							Type: "TEXT",
							Description: "Name of the party",
						},
						il.TextFieldConfig{
							Name: "role",
							Type: "TEXT",
							Description: "Role of the party (e.g. client, provider)",
						},
					},
				},
				il.DateFieldConfig{
					Name: "effective_date",
					Type: "DATE",
					Description: "Date the contract takes effect",
				},
				il.DateFieldConfig{
					Name: "termination_date",
					Type: "DATE",
					Description: "Date the contract expires or terminates",
				},
				il.ArrayFieldConfig{
					Name: "clauses",
					Type: "ARRAY",
					Description: "Individual contract clauses",
					Fields: []any{
						il.TextFieldConfig{
							Name: "title",
							Type: "TEXT",
							Description: "Clause heading or title",
						},
						il.TextareaFieldConfig{
							Name: "content",
							Type: "TEXTAREA",
							Description: "Full text of the clause",
						},
					},
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
  "name": "Extract Contract Clause Data",
  "nodes": [
    {
      "parameters": {
        "content": "## Extract Contract Clause Data\n\nLegal teams and contract management platforms use this recipe to automate contract review. Upload a contract and receive structured JSON with involved parties, key dates, and individual clauses \u2014 ready for a compliance check, risk analysis, or contract database.\n\n**Note:** This workflow uses the Iteration Layer community node (`n8n-nodes-iterationlayer`). Install it via Settings > Community Nodes on self-hosted n8n, or add it directly on n8n Cloud with Verified Community Nodes enabled.",
        "height": 280,
        "width": 500,
        "color": 2
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        200,
        40
      ],
      "id": "6e40f220-51d4-4a97-ad58-88b23de638e5",
      "name": "Overview"
    },
    {
      "parameters": {
        "content": "### Step 1: Extract Data\nResource: **Document Extraction**\n\nConfigure the Document Extraction parameters below, then connect your credentials.",
        "height": 160,
        "width": 300,
        "color": 6
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [
        475,
        100
      ],
      "id": "bf59c222-8e4c-4369-86ab-6be21dce4a57",
      "name": "Step 1 Note"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [
        250,
        300
      ],
      "id": "e5f6a7b8-c9d0-1234-efab-345678901234",
      "name": "Manual Trigger"
    },
    {
      "parameters": {
        "resource": "documentExtraction",
        "schemaInputMode": "rawJson",
        "schemaJson": "{\"fields\":[{\"name\":\"parties\",\"type\":\"ARRAY\",\"description\":\"Parties involved in the contract\",\"fields\":[{\"name\":\"name\",\"type\":\"TEXT\",\"description\":\"Name of the party\"},{\"name\":\"role\",\"type\":\"TEXT\",\"description\":\"Role of the party (e.g. client, provider)\"}]},{\"name\":\"effective_date\",\"type\":\"DATE\",\"description\":\"Date the contract takes effect\"},{\"name\":\"termination_date\",\"type\":\"DATE\",\"description\":\"Date the contract expires or terminates\"},{\"name\":\"clauses\",\"type\":\"ARRAY\",\"description\":\"Individual contract clauses\",\"fields\":[{\"name\":\"title\",\"type\":\"TEXT\",\"description\":\"Clause heading or title\"},{\"name\":\"content\",\"type\":\"TEXTAREA\",\"description\":\"Full text of the clause\"}]}]}",
        "files": {
          "fileValues": [
            {
              "fileInputMode": "url",
              "fileName": "contract.pdf",
              "fileUrl": "https://example.com/contracts/service-agreement.pdf"
            }
          ]
        }
      },
      "type": "n8n-nodes-iterationlayer.iterationLayer",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "id": "f6a7b8c9-d0e1-2345-fabc-456789012345",
      "name": "Extract Data",
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
            "node": "Extract Data",
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
Extract contract clause data from the file at [file URL]. Use the extract_document tool with these fields:

- parties (ARRAY): Each with name (TEXT) and role (TEXT)
- effective_date (DATE): Date the contract takes effect
- termination_date (DATE): Date the contract expires or terminates
- clauses (ARRAY): Each with title (TEXT) and content (TEXTAREA)
```

### Response


```json
{
  "success": true,
  "data": {
    "parties": {
      "value": [
        {
          "name": {
            "value": "Nexus Technologies Inc.",
            "confidence": 0.98,
            "citations": ["Nexus Technologies Inc."]
          },
          "role": {
            "value": "Client",
            "confidence": 0.96,
            "citations": ["hereinafter the \"Client\""]
          }
        },
        {
          "name": {
            "value": "CloudServe Solutions LLC",
            "confidence": 0.97,
            "citations": ["CloudServe Solutions LLC"]
          },
          "role": {
            "value": "Provider",
            "confidence": 0.95,
            "citations": ["hereinafter the \"Provider\""]
          }
        }
      ],
      "confidence": 0.96,
      "citations": []
    },
    "effective_date": {
      "value": "2026-04-01",
      "confidence": 0.98,
      "citations": ["effective as of April 1, 2026"]
    },
    "termination_date": {
      "value": "2028-03-31",
      "confidence": 0.97,
      "citations": ["terminating on March 31, 2028"]
    },
    "clauses": {
      "value": [
        {
          "title": {
            "value": "Limitation of Liability",
            "confidence": 0.98,
            "citations": ["Section 8: Limitation of Liability"]
          },
          "content": {
            "value": "Neither party shall be liable for any indirect, incidental, or consequential damages arising out of this agreement, except in cases of gross negligence or willful misconduct.",
            "confidence": 0.94,
            "citations": [
              "Neither party shall be liable for any indirect, incidental, or consequential damages"
            ]
          }
        },
        {
          "title": {
            "value": "Confidentiality",
            "confidence": 0.99,
            "citations": ["Section 5: Confidentiality"]
          },
          "content": {
            "value": "Both parties agree to maintain the confidentiality of all proprietary information disclosed during the term of this agreement for a period of three years following termination.",
            "confidence": 0.93,
            "citations": [
              "maintain the confidentiality of all proprietary information"
            ]
          }
        }
      ],
      "confidence": 0.95,
      "citations": []
    }
  }
}
```


## Links

- [Integration guide](https://iterationlayer.com/SKILL.md)
- [Full documentation](https://iterationlayer.com/docs)
- [OpenAPI spec](https://api.iterationlayer.com/openapi.json)
- [Browse all recipes](https://iterationlayer.com/recipes)
