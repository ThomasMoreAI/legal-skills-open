---
name: convert-contract-to-markdown
title: Convert Contract to Markdown
description: Convert a contract PDF to clean markdown for clause extraction or LLM analysis.
author: iterationlayer
author_url: https://github.com/iterationlayer/skills/tree/main/skills/convert-contract-to-markdown
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Convert Contract to Markdown

Legal and compliance teams use this recipe to convert contract PDFs to structured markdown before feeding them into LLM analysis pipelines or clause extraction workflows.

## APIs Used

Document to Markdown (1 credit per page)

## Prerequisites

You need an Iteration Layer API key. Get one at [platform.iterationlayer.com](https://platform.iterationlayer.com) — free trial credits included, no credit card required.

For full integration guidance (SDKs, auth, MCP, error handling), see the [Iteration Layer Integration Guide](https://iterationlayer.com/SKILL.md).

## Implementation


```bash
curl -X POST https://api.iterationlayer.com/document-to-markdown/v1/convert \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "file": {
      "type": "url",
      "name": "contract.pdf",
      "url": "https://example.com/contracts/service-agreement-2026.pdf"
    }
  }'
```

```typescript
import { IterationLayer } from "iterationlayer";

const client = new IterationLayer({ apiKey: "YOUR_API_KEY" });

const result = await client.convertDocumentToMarkdown({
  file: {
    type: "url",
    name: "contract.pdf",
    url: "https://example.com/contracts/service-agreement-2026.pdf",
  },
});
```

```python
from iterationlayer import IterationLayer

client = IterationLayer(api_key="YOUR_API_KEY")

result = client.convert_document_to_markdown(
    file={
        "type": "url",
        "name": "contract.pdf",
        "url": "https://example.com/contracts/service-agreement-2026.pdf",
    }
)
```

```go
import il "github.com/iterationlayer/sdk-go"

client := il.NewClient("YOUR_API_KEY")

result, err := client.ConvertDocumentToMarkdown(il.ConvertDocumentToMarkdownRequest{
  File: il.FileInput{Type: "url", Name: "contract.pdf", Url: "https://example.com/contracts/service-agreement-2026.pdf"},
})
```

```n8n
{
  "name": "Convert Contract to Markdown",
  "nodes": [
    {
      "parameters": {
        "content": "## Convert Contract to Markdown

Legal and compliance teams use this recipe to convert contract PDFs to structured markdown before feeding them into LLM analysis pipelines or clause extraction workflows.

**Note:** This workflow uses the Iteration Layer community node (`n8n-nodes-iterationlayer`). Install it via Settings > Community Nodes on self-hosted n8n, or add it directly on n8n Cloud with Verified Community Nodes enabled.",
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
      "id": "38e6da76-3ed5-468e-83b8-f6be1ed8a9d6",
      "name": "Overview"
    },
    {
      "parameters": {
        "content": "### Step 1: Convert Document to Markdown
Resource: **Document to Markdown**

Configure the Document to Markdown parameters below, then connect your credentials.",
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
      "id": "d407a240-e883-4d83-b7b9-b12a1a5cfc70",
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
      "id": "ce36c899-26c8-45c0-838c-194728865698",
      "name": "Manual Trigger"
    },
    {
      "parameters": {
        "resource": "documentToMarkdown",
        "fileInputMode": "url",
        "fileName": "contract.pdf",
        "fileUrl": "https://example.com/contracts/service-agreement-2026.pdf"
      },
      "type": "n8n-nodes-iterationlayer.iterationLayer",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "id": "75deb29a-0241-4a13-b160-c0dae41bada0",
      "name": "Convert Document to Markdown",
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
            "node": "Convert Document to Markdown",
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
Convert the contract at [file URL] to markdown. Use the convert_document_to_markdown tool with the file URL.
```

### Response


```json
{
  "success": true,
  "data": {
    "name": "contract.pdf",
    "mime_type": "application/pdf",
    "markdown": "# Service Agreement\n\n**Parties:** Nordlicht Consulting GmbH (\"Provider\") and Contoso Ltd. (\"Client\")\n\n**Effective Date:** 2026-03-01\n\n## 1. Services\n\nProvider agrees to deliver software development services as described in Schedule A attached hereto.\n\n## 2. Payment Terms\n\nClient shall pay Provider within 30 days of invoice receipt. Late payments accrue interest at 1.5% per month.\n\n## 3. Confidentiality\n\nEach party agrees to keep confidential all non-public information received from the other party.\n\n## 4. Termination\n\nEither party may terminate this agreement with 30 days written notice."
  }
}
```


## Links

- [Integration guide](https://iterationlayer.com/SKILL.md)
- [Full documentation](https://iterationlayer.com/docs)
- [OpenAPI spec](https://api.iterationlayer.com/openapi.json)
- [Browse all recipes](https://iterationlayer.com/recipes)
