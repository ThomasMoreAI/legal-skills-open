---
name: generate-compliance-audit-document
title: Generate a Compliance Audit Document
description: Generate a formatted PDF compliance audit document with findings, risk ratings, remediation recommendations, and sign-off sections.
author: iterationlayer
author_url: https://github.com/iterationlayer/skills/tree/main/skills/generate-compliance-audit-document
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: data-protection
language: en
---

# Generate a Compliance Audit Document

Compliance agencies and internal audit teams use this recipe to generate standardized audit documents — with structured findings tables, risk classifications, remediation timelines, and sign-off sections ready for stakeholder review.

## APIs Used

Document Generation (2 credits/request)

## Prerequisites

You need an Iteration Layer API key. Get one at [platform.iterationlayer.com](https://platform.iterationlayer.com) — free trial credits included, no credit card required.

For full integration guidance (SDKs, auth, MCP, error handling), see the [Iteration Layer Integration Guide](https://iterationlayer.com/SKILL.md).

## Implementation


```bash
curl -X POST https://api.iterationlayer.com/document-generation/v1/generate \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "format": "pdf",
    "document": {
      "metadata": {
        "title": "GDPR Compliance Audit Report — DataFlow Analytics",
        "author": "Sentinel Compliance Partners"
      },
      "page": {
        "size": {
          "preset": "A4"
        },
        "margins": {
          "top_in_pt": 54,
          "right_in_pt": 54,
          "bottom_in_pt": 54,
          "left_in_pt": 54
        }
      },
      "content": [
        {
          "type": "headline",
          "level": "h1",
          "text": "GDPR Compliance Audit Report"
        },
        {
          "type": "paragraph",
          "runs": [
            {
              "text": "Client: ",
              "font_weight": "bold"
            },
            {
              "text": "DataFlow Analytics GmbH\n"
            },
            {
              "text": "Audit Period: ",
              "font_weight": "bold"
            },
            {
              "text": "January 1 – March 31, 2026\n"
            },
            {
              "text": "Prepared by: ",
              "font_weight": "bold"
            },
            {
              "text": "Sentinel Compliance Partners\n"
            },
            {
              "text": "Report Date: ",
              "font_weight": "bold"
            },
            {
              "text": "April 10, 2026"
            }
          ]
        },
        {
          "type": "separator"
        },
        {
          "type": "headline",
          "level": "h2",
          "text": "Executive Summary"
        },
        {
          "type": "paragraph",
          "runs": [
            {
              "text": "This audit assessed DataFlow Analytics' compliance with the General Data Protection Regulation (GDPR) across data processing activities, consent management, data subject rights handling, and technical security measures. The overall compliance posture is rated as Satisfactory with three findings requiring remediation."
            }
          ]
        },
        {
          "type": "separator"
        },
        {
          "type": "headline",
          "level": "h2",
          "text": "Findings"
        },
        {
          "type": "table",
          "header": {
            "cells": [
              {
                "text": "#"
              },
              {
                "text": "Finding"
              },
              {
                "text": "Risk"
              },
              {
                "text": "Remediation"
              },
              {
                "text": "Due Date"
              }
            ]
          },
          "rows": [
            {
              "cells": [
                {
                  "text": "1"
                },
                {
                  "text": "Data Processing Agreements missing for 2 sub-processors"
                },
                {
                  "text": "High"
                },
                {
                  "text": "Execute DPAs with identified sub-processors"
                },
                {
                  "text": "2026-05-15"
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "2"
                },
                {
                  "text": "Cookie consent banner does not offer granular opt-out"
                },
                {
                  "text": "Medium"
                },
                {
                  "text": "Implement category-level consent controls"
                },
                {
                  "text": "2026-06-01"
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "3"
                },
                {
                  "text": "Data retention schedule not enforced for analytics logs"
                },
                {
                  "text": "Medium"
                },
                {
                  "text": "Configure automated log deletion after 90 days"
                },
                {
                  "text": "2026-05-30"
                }
              ]
            }
          ]
        },
        {
          "type": "separator"
        },
        {
          "type": "headline",
          "level": "h2",
          "text": "Overall Assessment"
        },
        {
          "type": "table",
          "header": {
            "cells": [
              {
                "text": "Area"
              },
              {
                "text": "Rating"
              }
            ]
          },
          "rows": [
            {
              "cells": [
                {
                  "text": "Lawful Basis & Consent"
                },
                {
                  "text": "Needs Improvement"
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "Data Subject Rights"
                },
                {
                  "text": "Compliant"
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "Data Processing Agreements"
                },
                {
                  "text": "Non-Compliant"
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "Technical Security Measures"
                },
                {
                  "text": "Compliant"
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "Data Retention"
                },
                {
                  "text": "Needs Improvement"
                }
              ]
            },
            {
              "cells": [
                {
                  "text": "Breach Notification Procedures"
                },
                {
                  "text": "Compliant"
                }
              ]
            }
          ]
        },
        {
          "type": "separator"
        },
        {
          "type": "headline",
          "level": "h2",
          "text": "Sign-Off"
        },
        {
          "type": "paragraph",
          "runs": [
            {
              "text": "Lead Auditor: ",
              "font_weight": "bold"
            },
            {
              "text": "Dr. Katrin Hoffmann, CIPP/E\n"
            },
            {
              "text": "Date: ",
              "font_weight": "bold"
            },
            {
              "text": "April 10, 2026\n\n"
            },
            {
              "text": "Client Acknowledgment: ",
              "font_weight": "bold"
            },
            {
              "text": "________________________________\n"
            },
            {
              "text": "Date: ",
              "font_weight": "bold"
            },
            {
              "text": "________________________________"
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

const audit = await client.generateDocument({
  format: "pdf",
  document: {
    metadata: { title: "GDPR Compliance Audit Report — DataFlow Analytics", author: "Sentinel Compliance Partners" },
    page: { size: { preset: "A4" }, margins: { top_in_pt: 54, right_in_pt: 54, bottom_in_pt: 54, left_in_pt: 54 } },
    content: [
      { type: "headline", level: "h1", text: "GDPR Compliance Audit Report" },
      {
        type: "paragraph",
        runs: [
          { text: "Client: ", font_weight: "bold" }, { text: "DataFlow Analytics GmbH\n" },
          { text: "Audit Period: ", font_weight: "bold" }, { text: "January 1 – March 31, 2026\n" },
          { text: "Prepared by: ", font_weight: "bold" }, { text: "Sentinel Compliance Partners\n" },
          { text: "Report Date: ", font_weight: "bold" }, { text: "April 10, 2026" },
        ],
      },
      { type: "separator" },
      { type: "headline", level: "h2", text: "Executive Summary" },
      { type: "paragraph", runs: [{ text: "This audit assessed DataFlow Analytics' GDPR compliance across data processing, consent management, data subject rights, and technical security. Overall posture: Satisfactory with three findings requiring remediation." }] },
      { type: "separator" },
      { type: "headline", level: "h2", text: "Findings" },
      {
        type: "table",
        header: { cells: [{ text: "#" }, { text: "Finding" }, { text: "Risk" }, { text: "Remediation" }, { text: "Due Date" }] },
        rows: [
          { cells: [{ text: "1" }, { text: "DPAs missing for 2 sub-processors" }, { text: "High" }, { text: "Execute DPAs" }, { text: "2026-05-15" }] },
          { cells: [{ text: "2" }, { text: "Cookie consent lacks granular opt-out" }, { text: "Medium" }, { text: "Add category-level controls" }, { text: "2026-06-01" }] },
          { cells: [{ text: "3" }, { text: "Analytics log retention not enforced" }, { text: "Medium" }, { text: "Auto-delete after 90 days" }, { text: "2026-05-30" }] },
        ],
      },
      { type: "separator" },
      { type: "headline", level: "h2", text: "Overall Assessment" },
      {
        type: "table",
        header: { cells: [{ text: "Area" }, { text: "Rating" }] },
        rows: [
          { cells: [{ text: "Lawful Basis & Consent" }, { text: "Needs Improvement" }] },
          { cells: [{ text: "Data Subject Rights" }, { text: "Compliant" }] },
          { cells: [{ text: "Data Processing Agreements" }, { text: "Non-Compliant" }] },
          { cells: [{ text: "Technical Security" }, { text: "Compliant" }] },
          { cells: [{ text: "Data Retention" }, { text: "Needs Improvement" }] },
          { cells: [{ text: "Breach Notification" }, { text: "Compliant" }] },
        ],
      },
      { type: "separator" },
      { type: "headline", level: "h2", text: "Sign-Off" },
      {
        type: "paragraph",
        runs: [
          { text: "Lead Auditor: ", font_weight: "bold" }, { text: "Dr. Katrin Hoffmann, CIPP/E\n" },
          { text: "Date: ", font_weight: "bold" }, { text: "April 10, 2026" },
        ],
      },
    ],
  },
});
```

```python
from iterationlayer import IterationLayer
client = IterationLayer(api_key="YOUR_API_KEY")

audit = client.generate_document(
    format="pdf",
    document={
        "metadata": {"title": "GDPR Compliance Audit Report — DataFlow Analytics", "author": "Sentinel Compliance Partners"},
        "page": {"size": {"preset": "A4"}, "margins": {"top_in_pt": 54, "right_in_pt": 54, "bottom_in_pt": 54, "left_in_pt": 54}},
        "content": [
            {"type": "headline", "level": "h1", "text": "GDPR Compliance Audit Report"},
            {"type": "paragraph", "runs": [
                {"text": "Client: ", "font_weight": "bold"}, {"text": "DataFlow Analytics GmbH\n"},
                {"text": "Audit Period: ", "font_weight": "bold"}, {"text": "January 1 – March 31, 2026\n"},
                {"text": "Prepared by: ", "font_weight": "bold"}, {"text": "Sentinel Compliance Partners\n"},
                {"text": "Report Date: ", "font_weight": "bold"}, {"text": "April 10, 2026"},
            ]},
            {"type": "separator"},
            {"type": "headline", "level": "h2", "text": "Executive Summary"},
            {"type": "paragraph", "runs": [{"text": "Overall posture: Satisfactory with three findings requiring remediation."}]},
            {"type": "separator"},
            {"type": "headline", "level": "h2", "text": "Findings"},
            {
                "type": "table",
                "header": {"cells": [{"text": "#"}, {"text": "Finding"}, {"text": "Risk"}, {"text": "Remediation"}, {"text": "Due Date"}]},
                "rows": [
                    {"cells": [{"text": "1"}, {"text": "DPAs missing for 2 sub-processors"}, {"text": "High"}, {"text": "Execute DPAs"}, {"text": "2026-05-15"}]},
                    {"cells": [{"text": "2"}, {"text": "Cookie consent lacks granular opt-out"}, {"text": "Medium"}, {"text": "Add category-level controls"}, {"text": "2026-06-01"}]},
                    {"cells": [{"text": "3"}, {"text": "Analytics log retention not enforced"}, {"text": "Medium"}, {"text": "Auto-delete after 90 days"}, {"text": "2026-05-30"}]},
                ],
            },
            {"type": "separator"},
            {"type": "headline", "level": "h2", "text": "Overall Assessment"},
            {
                "type": "table",
                "header": {"cells": [{"text": "Area"}, {"text": "Rating"}]},
                "rows": [
                    {"cells": [{"text": "Lawful Basis & Consent"}, {"text": "Needs Improvement"}]},
                    {"cells": [{"text": "Data Subject Rights"}, {"text": "Compliant"}]},
                    {"cells": [{"text": "Data Processing Agreements"}, {"text": "Non-Compliant"}]},
                    {"cells": [{"text": "Technical Security"}, {"text": "Compliant"}]},
                    {"cells": [{"text": "Data Retention"}, {"text": "Needs Improvement"}]},
                    {"cells": [{"text": "Breach Notification"}, {"text": "Compliant"}]},
                ],
            },
            {"type": "separator"},
            {"type": "headline", "level": "h2", "text": "Sign-Off"},
            {"type": "paragraph", "runs": [
                {"text": "Lead Auditor: ", "font_weight": "bold"}, {"text": "Dr. Katrin Hoffmann, CIPP/E\n"},
                {"text": "Date: ", "font_weight": "bold"}, {"text": "April 10, 2026"},
            ]},
        ],
    },
)
```

```go
package main

import il "github.com/iterationlayer/sdk-go"

func main() {
	client := il.NewClient("YOUR_API_KEY")

	_, err := client.GenerateDocument(il.GenerateDocumentRequest{
		Format: "pdf",
		Document: il.DocumentDefinition{
			Metadata: il.DocumentMetadata{Title: "GDPR Compliance Audit Report — DataFlow Analytics", Author: "Sentinel Compliance Partners"},
			Page: &il.DocumentPage{Size: il.DocPageSize{Preset: "A4"}, Margins: il.DocMargins{TopInPt: 54, RightInPt: 54, BottomInPt: 54, LeftInPt: 54}},
			Content: []il.ContentBlock{
				il.ContentBlock{"type": "headline", "level": "h1", "text": "GDPR Compliance Audit Report"},
				il.ContentBlock{"type": "paragraph", "runs": []map[string]string{
					{"text": "Client: ", "font_weight": "bold"}, {"text": "DataFlow Analytics GmbH\n"},
					{"text": "Audit Period: ", "font_weight": "bold"}, {"text": "January 1 – March 31, 2026\n"},
					{"text": "Prepared by: ", "font_weight": "bold"}, {"text": "Sentinel Compliance Partners"},
				}},
				il.ContentBlock{"type": "separator"},
				il.ContentBlock{"type": "headline", "level": "h2", "text": "Findings"},
				il.ContentBlock{"type": "table",
					"header": map[string]any{"cells": []map[string]string{{"text": "#"}, {"text": "Finding"}, {"text": "Risk"}, {"text": "Remediation"}, {"text": "Due Date"}}},
					"rows": []map[string]any{
						{"cells": []map[string]string{{"text": "1"}, {"text": "DPAs missing for 2 sub-processors"}, {"text": "High"}, {"text": "Execute DPAs"}, {"text": "2026-05-15"}}},
						{"cells": []map[string]string{{"text": "2"}, {"text": "Cookie consent lacks granular opt-out"}, {"text": "Medium"}, {"text": "Add category-level controls"}, {"text": "2026-06-01"}}},
					},
				},
				il.ContentBlock{"type": "separator"},
				il.ContentBlock{"type": "headline", "level": "h2", "text": "Sign-Off"},
				il.ContentBlock{"type": "paragraph", "runs": []map[string]string{{"text": "Lead Auditor: Dr. Katrin Hoffmann, CIPP/E"}}},
			},
		},
	})
	if err != nil {
		panic(err)
	}
}
```

```n8n
{
  "name": "Generate compliance audit document in Iteration Layer",
  "nodes": [
    {
      "parameters": {
        "content": "## Generate a Compliance Audit Document\n\nCompliance agencies and internal audit teams use this recipe to generate standardized audit documents — with structured findings tables, risk classifications, and remediation timelines.\n\n**Note:** This workflow uses the Iteration Layer community node (`n8n-nodes-iterationlayer`). Install it via Settings > Community Nodes on self-hosted n8n, or add it directly on n8n Cloud with Verified Community Nodes enabled.",
        "height": 280,
        "width": 500,
        "color": 2
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [200, 40],
      "id": "a9b0c1d2-e3f4-5678-abcd-678901234501",
      "name": "Overview"
    },
    {
      "parameters": {
        "content": "### Step 1: Generate Audit Document\nResource: **Document Generation**\n\nConfigure the Document Generation parameters below, then connect your credentials.",
        "height": 160,
        "width": 300,
        "color": 6
      },
      "type": "n8n-nodes-base.stickyNote",
      "typeVersion": 1,
      "position": [475, 100],
      "id": "a9b0c1d2-e3f4-5678-abcd-678901234502",
      "name": "Step 1 Note"
    },
    {
      "parameters": {},
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "id": "a9b0c1d2-e3f4-5678-abcd-678901234503",
      "name": "Manual Trigger"
    },
    {
      "parameters": {
        "resource": "documentGeneration",
        "format": "pdf",
        "documentJson": "{\n  \"metadata\": { \"title\": \"GDPR Compliance Audit Report\", \"author\": \"Sentinel Compliance Partners\" },\n  \"page\": { \"size\": { \"preset\": \"A4\" }, \"margins\": { \"top_in_pt\": 54, \"right_in_pt\": 54, \"bottom_in_pt\": 54, \"left_in_pt\": 54 } },\n  \"content\": [\n    { \"type\": \"headline\", \"level\": \"h1\", \"text\": \"GDPR Compliance Audit Report\" },\n    { \"type\": \"separator\" },\n    { \"type\": \"headline\", \"level\": \"h2\", \"text\": \"Findings\" },\n    { \"type\": \"table\", \"header\": { \"cells\": [{ \"text\": \"#\" }, { \"text\": \"Finding\" }, { \"text\": \"Risk\" }, { \"text\": \"Remediation\" }, { \"text\": \"Due Date\" }] }, \"rows\": [{ \"cells\": [{ \"text\": \"1\" }, { \"text\": \"DPAs missing\" }, { \"text\": \"High\" }, { \"text\": \"Execute DPAs\" }, { \"text\": \"2026-05-15\" }] }] },\n    { \"type\": \"separator\" },\n    { \"type\": \"headline\", \"level\": \"h2\", \"text\": \"Sign-Off\" },\n    { \"type\": \"paragraph\", \"runs\": [{ \"text\": \"Lead Auditor: Dr. Katrin Hoffmann\" }] }\n  ]\n}"
      },
      "type": "n8n-nodes-iterationlayer.iterationLayer",
      "typeVersion": 1,
      "position": [500, 300],
      "id": "a9b0c1d2-e3f4-5678-abcd-678901234504",
      "name": "Generate Audit Document",
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
            "node": "Generate Audit Document",
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
Generate a compliance audit document for [client name]. Use the generate_document tool to create an A4 PDF with:

- Report header with client name, audit period, preparer, and report date
- Executive summary paragraph
- Findings table with columns: #, Finding, Risk (High/Medium/Low), Remediation, Due Date
- Overall assessment table rating each compliance area (Compliant / Needs Improvement / Non-Compliant)
- Sign-off section with lead auditor name and client acknowledgment lines
```

### Response


```json
{
  "success": true,
  "data": {
    "buffer": "JVBERi0xLjQ...",
    "mime_type": "application/pdf"
  }
}
```


## Links

- [Integration guide](https://iterationlayer.com/SKILL.md)
- [Full documentation](https://iterationlayer.com/docs)
- [OpenAPI spec](https://api.iterationlayer.com/openapi.json)
- [Browse all recipes](https://iterationlayer.com/recipes)
