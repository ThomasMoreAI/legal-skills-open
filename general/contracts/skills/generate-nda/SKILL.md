---
name: generate-nda
title: Generate NDA
description: Generate a non-disclosure agreement PDF with party names, effective date, and standard confidentiality terms.
author: iterationlayer
author_url: https://github.com/iterationlayer/skills/tree/main/skills/generate-nda
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Generate NDA

Legal teams and SaaS companies generate NDAs programmatically with party details, effective date, and standard confidentiality clauses — ready for review and signature.

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
        "title": "Non-Disclosure Agreement",
        "author": "Nordlicht Technologies GmbH"
      },
      "page": {
        "size": { "preset": "A4" },
        "margins": {
          "top_in_pt": 72,
          "right_in_pt": 72,
          "bottom_in_pt": 72,
          "left_in_pt": 72
        }
      },
      "styles": {
        "text": {
          "font_family": "Helvetica",
          "font_size_in_pt": 11.0,
          "line_height": 1.5,
          "color": "#333333"
        },
        "headline": {
          "font_family": "Helvetica",
          "font_size_in_pt": 24.0,
          "color": "#111111",
          "spacing_before_in_pt": 12.0,
          "spacing_after_in_pt": 6.0,
          "font_weight": "bold"
        },
        "link": {
          "color": "#0066CC",
          "is_underlined": true
        },
        "list": {
          "text_style": {
            "font_family": "Helvetica",
            "font_size_in_pt": 11.0,
            "line_height": 1.5,
            "color": "#333333"
          },
          "marker_color": "#333333",
          "marker_gap_in_pt": 8.0
        },
        "table": {
          "header": {
            "background_color": "#333333",
            "text_color": "#FFFFFF",
            "font_size_in_pt": 11.0,
            "font_weight": "bold"
          },
          "body": {
            "background_color": "#FFFFFF",
            "text_color": "#333333",
            "font_size_in_pt": 11.0
          },
          "border": {
            "outer": {
              "top": {
                "color": "#CCCCCC",
                "width_in_pt": 1.0
              },
              "right": {
                "color": "#CCCCCC",
                "width_in_pt": 1.0
              },
              "bottom": {
                "color": "#CCCCCC",
                "width_in_pt": 1.0
              },
              "left": {
                "color": "#CCCCCC",
                "width_in_pt": 1.0
              }
            },
            "inner": {
              "horizontal": {
                "color": "#EEEEEE",
                "width_in_pt": 0.5
              },
              "vertical": {
                "color": "#EEEEEE",
                "width_in_pt": 0.5
              }
            }
          }
        },
        "grid": {
          "background_color": "#FFFFFF",
          "border_color": "#CCCCCC",
          "border_width_in_pt": 0.0,
          "gap_in_pt": 12.0
        },
        "separator": {
          "color": "#CCCCCC",
          "thickness_in_pt": 1.0,
          "spacing_before_in_pt": 12.0,
          "spacing_after_in_pt": 12.0
        },
        "image": {
          "border_color": "#000000",
          "border_width_in_pt": 0.0
        }
      },
      "footer": [
        {
          "type": "paragraph",
          "runs": [{
            "text": "Confidential — Nordlicht Technologies GmbH — NDA-2026-0389"
          }]
        }
      ],
      "content": [
        {
            "type": "headline",
            "level": "h1",
            "text": "Non-Disclosure Agreement",
        },
        { "type": "paragraph", "runs": [
          { "text": "This Non-Disclosure Agreement (\"Agreement\") is entered into as of " },
          {
              "text": "March 14,
              2026",
              "font_weight": "bold",
          },
          { "text": " (the \"Effective Date\") by and between " },
          {
              "text": "Nordlicht Technologies GmbH",
              "font_weight": "bold",
          },
          {
              "text": ",
              a German company with its principal office at Friedrichstrasse 68, 10117 Berlin,
              Austin,
              TX 78701 (the \"Disclosing Party\"),
              and ",
          },
          {
              "text": "Globex Corporation",
              "font_weight": "bold",
          },
          {
              "text": ",
              a German company with offices at Sonnenstrasse 12, 80331 Munich,
              Berlin,
              CA 94105 (the \"Receiving Party\").",
          }
        ] },
        { "type": "separator" },
        {
            "type": "headline",
            "level": "h2",
            "text": "Terms and Conditions",
        },
        {
          "type": "list",
          "variant": "ordered",
          "items": [
            {
                "text": "Definition of Confidential Information. \"Confidential Information\" means any non-public information disclosed by the Disclosing Party to the Receiving Party,
                whether orally,
                in writing,
                or by inspection,
                including but not limited to trade secrets,
                business plans,
                financial data,
                software,
                and technical specifications.",
            },
            {
                "text": "Obligations of Receiving Party. The Receiving Party agrees to hold all Confidential Information in strict confidence,
                use it solely for the purpose of evaluating a potential business relationship,
                and not disclose it to any third party without prior written consent.",
            },
            { "text": "Exclusions. This Agreement does not apply to information that: (a) is or becomes publicly available through no fault of the Receiving Party; (b) was known to the Receiving Party prior to disclosure; (c) is independently developed without use of Confidential Information; or (d) is required to be disclosed by law or court order." },
            { "text": "Term and Termination. This Agreement shall remain in effect for a period of two (2) years from the Effective Date. The obligations of confidentiality shall survive termination for an additional three (3) years." },
            {
                "text": "Return of Materials. Upon termination or request,
                the Receiving Party shall promptly return or destroy all Confidential Information and any copies thereof,
                and certify such destruction in writing.",
            },
            {
                "text": "Governing Law. This Agreement shall be governed by and construed in accordance with the laws of Germany,
                without regard to conflict of laws principles.",
            }
          ]
        },
        { "type": "separator" },
        {
          "type": "grid",
          "columns": [
            {
              "column_span": 6,
              "blocks": [
                { "type": "paragraph", "runs": [
                  {
                      "text": "Disclosing Party\n\n",
                      "font_weight": "bold",
                  },
                  { "text": "Signature: ________________________\n\n" },
                  {
                      "text": "Name: ",
                      "font_weight": "bold",
                  },
                  { "text": "____________________\n\n" },
                  {
                      "text": "Title: ",
                      "font_weight": "bold",
                  },
                  { "text": "____________________\n\n" },
                  {
                      "text": "Date: ",
                      "font_weight": "bold",
                  },
                  { "text": "____________________" }
                ] }
              ]
            },
            {
              "column_span": 6,
              "blocks": [
                { "type": "paragraph", "runs": [
                  {
                      "text": "Receiving Party\n\n",
                      "font_weight": "bold",
                  },
                  { "text": "Signature: ________________________\n\n" },
                  {
                      "text": "Name: ",
                      "font_weight": "bold",
                  },
                  { "text": "____________________\n\n" },
                  {
                      "text": "Title: ",
                      "font_weight": "bold",
                  },
                  { "text": "____________________\n\n" },
                  {
                      "text": "Date: ",
                      "font_weight": "bold",
                  },
                  { "text": "____________________" }
                ] }
              ]
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

const result = await client.generateDocument({
  format: "pdf",
  document: {
    metadata: {
      title: "Non-Disclosure Agreement",
      author: "Nordlicht Technologies GmbH",
    },
    page: {
      size: { preset: "A4" },
      margins: {
        top_in_pt: 72,
        right_in_pt: 72,
        bottom_in_pt: 72,
        left_in_pt: 72,
      },
    },
    styles: {
      text: {
        font_family: "Helvetica",
        font_size_in_pt: 11.0,
        line_height: 1.5,
        color: "#333333",
      },
      headline: {
        font_family: "Helvetica",
        font_size_in_pt: 24.0,
        color: "#111111",
        spacing_before_in_pt: 12.0,
        spacing_after_in_pt: 6.0,
        font_weight: "bold",
      },
      link: {
        color: "#0066CC",
        is_underlined: true,
      },
      list: {
        text_style: {
          font_family: "Helvetica",
          font_size_in_pt: 11.0,
          line_height: 1.5,
          color: "#333333",
        },
        marker_color: "#333333",
        marker_gap_in_pt: 8.0,
      },
      table: {
        header: {
          background_color: "#333333",
          text_color: "#FFFFFF",
          font_size_in_pt: 11.0,
          font_weight: "bold",
        },
        body: {
          background_color: "#FFFFFF",
          text_color: "#333333",
          font_size_in_pt: 11.0,
        },
        border: {
          outer: {
            top: {
              color: "#CCCCCC",
              width_in_pt: 1.0,
            },
            right: {
              color: "#CCCCCC",
              width_in_pt: 1.0,
            },
            bottom: {
              color: "#CCCCCC",
              width_in_pt: 1.0,
            },
            left: {
              color: "#CCCCCC",
              width_in_pt: 1.0,
            },
          },
          inner: {
            horizontal: {
              color: "#EEEEEE",
              width_in_pt: 0.5,
            },
            vertical: {
              color: "#EEEEEE",
              width_in_pt: 0.5,
            },
          },
        },
      },
      grid: {
        background_color: "#FFFFFF",
        border_color: "#CCCCCC",
        border_width_in_pt: 0.0,
        gap_in_pt: 12.0,
      },
      separator: {
        color: "#CCCCCC",
        thickness_in_pt: 1.0,
        spacing_before_in_pt: 12.0,
        spacing_after_in_pt: 12.0,
      },
      image: {
        border_color: "#000000",
        border_width_in_pt: 0.0,
      },
    },
    footer: [
      {
        type: "paragraph",
        runs: [{
          text: "Confidential — Nordlicht Technologies GmbH — NDA-2026-0389",
        }],
      },
    ],
    content: [
      {
          type: "headline",
          level: "h1",
          text: "Non-Disclosure Agreement",
      },
      { type: "paragraph", runs: [
        { text: "This Non-Disclosure Agreement (\"Agreement\") is entered into as of " },
        {
            text: "March 14,
            2026",
            font_weight: "bold",
        },
        { text: " (the \"Effective Date\") by and between " },
        {
            text: "Nordlicht Technologies GmbH",
            font_weight: "bold",
        },
        {
            text: ",
            a German company with its principal office at Friedrichstrasse 68, 10117 Berlin,
            Austin,
            TX 78701 (the \"Disclosing Party\"),
            and ",
        },
        {
            text: "Globex Corporation",
            font_weight: "bold",
        },
        {
            text: ",
            a German company with offices at Sonnenstrasse 12, 80331 Munich,
            Berlin,
            CA 94105 (the \"Receiving Party\").",
        },
      ] },
      { type: "separator" },
      {
          type: "headline",
          level: "h2",
          text: "Terms and Conditions",
      },
      {
        type: "list",
        variant: "ordered",
        items: [
          {
              text: "Definition of Confidential Information. \"Confidential Information\" means any non-public information disclosed by the Disclosing Party to the Receiving Party,
              whether orally,
              in writing,
              or by inspection,
              including but not limited to trade secrets,
              business plans,
              financial data,
              software,
              and technical specifications.",
          },
          {
              text: "Obligations of Receiving Party. The Receiving Party agrees to hold all Confidential Information in strict confidence,
              use it solely for the purpose of evaluating a potential business relationship,
              and not disclose it to any third party without prior written consent.",
          },
          { text: "Exclusions. This Agreement does not apply to information that: (a) is or becomes publicly available through no fault of the Receiving Party; (b) was known to the Receiving Party prior to disclosure; (c) is independently developed without use of Confidential Information; or (d) is required to be disclosed by law or court order." },
          { text: "Term and Termination. This Agreement shall remain in effect for a period of two (2) years from the Effective Date. The obligations of confidentiality shall survive termination for an additional three (3) years." },
          {
              text: "Return of Materials. Upon termination or request,
              the Receiving Party shall promptly return or destroy all Confidential Information and any copies thereof,
              and certify such destruction in writing.",
          },
          {
              text: "Governing Law. This Agreement shall be governed by and construed in accordance with the laws of Germany,
              without regard to conflict of laws principles.",
          },
        ],
      },
      { type: "separator" },
      {
        type: "grid",
        columns: [
          {
            column_span: 6,
            blocks: [
              { type: "paragraph", runs: [
                {
                    text: "Disclosing Party\n\n",
                    font_weight: "bold",
                },
                { text: "Signature: ________________________\n\n" },
                {
                    text: "Name: ",
                    font_weight: "bold",
                },
                { text: "____________________\n\n" },
                {
                    text: "Title: ",
                    font_weight: "bold",
                },
                { text: "____________________\n\n" },
                {
                    text: "Date: ",
                    font_weight: "bold",
                },
                { text: "____________________" },
              ] },
            ],
          },
          {
            column_span: 6,
            blocks: [
              { type: "paragraph", runs: [
                {
                    text: "Receiving Party\n\n",
                    font_weight: "bold",
                },
                { text: "Signature: ________________________\n\n" },
                {
                    text: "Name: ",
                    font_weight: "bold",
                },
                { text: "____________________\n\n" },
                {
                    text: "Title: ",
                    font_weight: "bold",
                },
                { text: "____________________\n\n" },
                {
                    text: "Date: ",
                    font_weight: "bold",
                },
                { text: "____________________" },
              ] },
            ],
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

result = client.generate_document(
    format="pdf",
    document={
        "metadata": {
            "title": "Non-Disclosure Agreement",
            "author": "Nordlicht Technologies GmbH",
        },
        "page": {
            "size": {"preset": "A4"},
            "margins": {
                "top_in_pt": 72,
                "right_in_pt": 72,
                "bottom_in_pt": 72,
                "left_in_pt": 72,
            },
        },
        "styles": {
            "text": {
                "font_family": "Helvetica",
                "font_size_in_pt": 11.0,
                "line_height": 1.5,
                "color": "#333333",
            },
            "headline": {
                "font_family": "Helvetica",
                "font_size_in_pt": 24.0,
                "color": "#111111",
                "spacing_before_in_pt": 12.0,
                "spacing_after_in_pt": 6.0,
                "font_weight": "bold",
            },
            "link": {
                "color": "#0066CC",
                "is_underlined": True,
            },
            "list": {
                "text_style": {
                    "font_family": "Helvetica",
                    "font_size_in_pt": 11.0,
                    "line_height": 1.5,
                    "color": "#333333",
                },
                "marker_color": "#333333",
                "marker_gap_in_pt": 8.0,
            },
            "table": {
                "header": {
                    "background_color": "#333333",
                    "text_color": "#FFFFFF",
                    "font_size_in_pt": 11.0,
                    "font_weight": "bold",
                },
                "body": {
                    "background_color": "#FFFFFF",
                    "text_color": "#333333",
                    "font_size_in_pt": 11.0,
                },
                "border": {
                    "outer": {
                        "top": {
                            "color": "#CCCCCC",
                            "width_in_pt": 1.0,
                        },
                        "right": {
                            "color": "#CCCCCC",
                            "width_in_pt": 1.0,
                        },
                        "bottom": {
                            "color": "#CCCCCC",
                            "width_in_pt": 1.0,
                        },
                        "left": {
                            "color": "#CCCCCC",
                            "width_in_pt": 1.0,
                        },
                    },
                    "inner": {
                        "horizontal": {
                            "color": "#EEEEEE",
                            "width_in_pt": 0.5,
                        },
                        "vertical": {
                            "color": "#EEEEEE",
                            "width_in_pt": 0.5,
                        },
                    },
                },
            },
            "grid": {
                "background_color": "#FFFFFF",
                "border_color": "#CCCCCC",
                "border_width_in_pt": 0.0,
                "gap_in_pt": 12.0,
            },
            "separator": {
                "color": "#CCCCCC",
                "thickness_in_pt": 1.0,
                "spacing_before_in_pt": 12.0,
                "spacing_after_in_pt": 12.0,
            },
            "image": {
                "border_color": "#000000",
                "border_width_in_pt": 0.0,
            },
        },
        "footer": [
            {
                "type": "paragraph",
                "runs": [{
                    "text": "Confidential — Nordlicht Technologies GmbH — NDA-2026-0389",
                }],
            },
        ],
        "content": [
            {
                "type": "headline",
                "level": "h1",
                "text": "Non-Disclosure Agreement",
            },
            {"type": "paragraph", "runs": [
                {"text": "This Non-Disclosure Agreement (\"Agreement\") is entered into as of "},
                {
                    "text": "March 14,
                    2026",
                    "font_weight": "bold",
                },
                {"text": " (the \"Effective Date\") by and between "},
                {
                    "text": "Nordlicht Technologies GmbH",
                    "font_weight": "bold",
                },
                {
                    "text": ",
                    a German company with its principal office at Friedrichstrasse 68, 10117 Berlin,
                    Austin,
                    TX 78701 (the \"Disclosing Party\"),
                    and ",
                },
                {
                    "text": "Globex Corporation",
                    "font_weight": "bold",
                },
                {
                    "text": ",
                    a German company with offices at Sonnenstrasse 12, 80331 Munich,
                    Berlin,
                    CA 94105 (the \"Receiving Party\").",
                },
            ]},
            {"type": "separator"},
            {
                "type": "headline",
                "level": "h2",
                "text": "Terms and Conditions",
            },
            {
                "type": "list",
                "variant": "ordered",
                "items": [
                    {
                        "text": "Definition of Confidential Information. \"Confidential Information\" means any non-public information disclosed by the Disclosing Party to the Receiving Party,
                        whether orally,
                        in writing,
                        or by inspection,
                        including but not limited to trade secrets,
                        business plans,
                        financial data,
                        software,
                        and technical specifications.",
                    },
                    {
                        "text": "Obligations of Receiving Party. The Receiving Party agrees to hold all Confidential Information in strict confidence,
                        use it solely for the purpose of evaluating a potential business relationship,
                        and not disclose it to any third party without prior written consent.",
                    },
                    {"text": "Exclusions. This Agreement does not apply to information that: (a) is or becomes publicly available through no fault of the Receiving Party; (b) was known to the Receiving Party prior to disclosure; (c) is independently developed without use of Confidential Information; or (d) is required to be disclosed by law or court order."},
                    {"text": "Term and Termination. This Agreement shall remain in effect for a period of two (2) years from the Effective Date. The obligations of confidentiality shall survive termination for an additional three (3) years."},
                    {
                        "text": "Return of Materials. Upon termination or request,
                        the Receiving Party shall promptly return or destroy all Confidential Information and any copies thereof,
                        and certify such destruction in writing.",
                    },
                    {
                        "text": "Governing Law. This Agreement shall be governed by and construed in accordance with the laws of Germany,
                        without regard to conflict of laws principles.",
                    },
                ],
            },
            {"type": "separator"},
            {
                "type": "grid",
                "columns": [
                    {
                        "column_span": 6,
                        "blocks": [
                            {"type": "paragraph", "runs": [
                                {
                                    "text": "Disclosing Party\n\n",
                                    "font_weight": "bold",
                                },
                                {"text": "Signature: ________________________\n\n"},
                                {
                                    "text": "Name: ",
                                    "font_weight": "bold",
                                },
                                {"text": "____________________\n\n"},
                                {
                                    "text": "Title: ",
                                    "font_weight": "bold",
                                },
                                {"text": "____________________\n\n"},
                                {
                                    "text": "Date: ",
                                    "font_weight": "bold",
                                },
                                {"text": "____________________"},
                            ]},
                        ],
                    },
                    {
                        "column_span": 6,
                        "blocks": [
                            {"type": "paragraph", "runs": [
                                {
                                    "text": "Receiving Party\n\n",
                                    "font_weight": "bold",
                                },
                                {"text": "Signature: ________________________\n\n"},
                                {
                                    "text": "Name: ",
                                    "font_weight": "bold",
                                },
                                {"text": "____________________\n\n"},
                                {
                                    "text": "Title: ",
                                    "font_weight": "bold",
                                },
                                {"text": "____________________\n\n"},
                                {
                                    "text": "Date: ",
                                    "font_weight": "bold",
                                },
                                {"text": "____________________"},
                            ]},
                        ],
                    },
                ],
            },
        ],
    },
)

```

```go
package main

import il "github.com/iterationlayer/sdk-go"

func main() {
	client := il.NewClient("YOUR_API_KEY")

	result, err := client.GenerateDocument(il.GenerateDocumentRequest{
		Format: "pdf",
		Document: il.DocumentDefinition{
			Metadata: il.DocumentMetadata{
				Title:  "Non-Disclosure Agreement",
				Author: "Nordlicht Technologies GmbH",
			},
			Page: il.PageConfig{
				Size:    il.PageSize{Preset: "A4"},
				Margins: il.Margins{
      TopInPt: 72,
      RightInPt: 72,
      BottomInPt: 72,
      LeftInPt: 72,
    },
			},
			Content: []il.ContentBlock{
				il.NewHeadlineBlock("h1", "Non-Disclosure Agreement"),
				il.ParagraphBlock{
      Type: "paragraph",
      Markdown: "This Non-Disclosure Agreement is entered into as of **March 14,
      2026** by and between **Nordlicht Technologies GmbH** (the \"Disclosing Party\") and **Globex Corporation** (the \"Receiving Party\").",
    },
				il.NewSeparatorBlock(),
				il.NewHeadlineBlock("h2", "Terms and Conditions"),
				il.ListBlock{Type: "list", Variant: "ordered", Items: []il.ListItem{
					{Text: "Definition of Confidential Information. \"Confidential Information\" means any non-public information disclosed by the Disclosing Party."},
					{Text: "Obligations of Receiving Party. The Receiving Party agrees to hold all Confidential Information in strict confidence."},
					{Text: "Exclusions. This Agreement does not apply to information that is publicly available or independently developed."},
					{Text: "Term and Termination. This Agreement shall remain in effect for two (2) years from the Effective Date."},
					{
       Text: "Return of Materials. Upon termination,
       the Receiving Party shall return or destroy all Confidential Information.",
     },
					{Text: "Governing Law. This Agreement shall be governed by the laws of Germany."},
				}},
				il.NewSeparatorBlock(),
				il.ParagraphBlock{
      Type: "paragraph",
      Markdown: "**Disclosing Party**\n\nSignature: ________________________",
    },
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
  "name": "Generate NDA",
  "nodes": [
    {
      "parameters": {
        "content": "## Generate NDA\n\nLegal teams and SaaS companies generate NDAs programmatically with party details, effective date, and standard confidentiality clauses \u2014 ready for review and signature.\n\n**Note:** This workflow uses the Iteration Layer community node (`n8n-nodes-iterationlayer`). Install it via Settings > Community Nodes on self-hosted n8n, or add it directly on n8n Cloud with Verified Community Nodes enabled.",
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
      "id": "058037e9-ed8f-457b-931e-548879d18af0",
      "name": "Overview"
    },
    {
      "parameters": {
        "content": "### Step 1: Generate Document\nResource: **Document Generation**\n\nConfigure the Document Generation parameters below, then connect your credentials.",
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
      "id": "87ef9e15-653e-47a3-b1f3-03ef6054a8f0",
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
      "id": "9f6064af-dc7a-4fad-b64d-2e7b698d8d5a",
      "name": "Manual Trigger"
    },
    {
      "parameters": {
        "resource": "documentGeneration",
        "format": "pdf",
        "documentJson": "{\n  \"metadata\": {\n    \"title\": \"Non-Disclosure Agreement\",\n    \"author\": \"Nordlicht Technologies GmbH\"\n  },\n  \"page\": {\n    \"size\": {\n      \"preset\": \"A4\"\n    },\n    \"margins\": {\n      \"top_in_pt\": 72,\n      \"right_in_pt\": 72,\n      \"bottom_in_pt\": 72,\n      \"left_in_pt\": 72\n    }\n  },\n  \"styles\": {\n    \"text\": {\n      \"font_family\": \"Helvetica\",\n      \"font_size_in_pt\": 11.0,\n      \"line_height\": 1.5,\n      \"color\": \"#333333\"\n    },\n    \"headline\": {\n      \"font_family\": \"Helvetica\",\n      \"font_size_in_pt\": 24.0,\n      \"color\": \"#111111\",\n      \"spacing_before_in_pt\": 12.0,\n      \"spacing_after_in_pt\": 6.0,\n      \"font_weight\": \"bold\"\n    },\n    \"link\": {\n      \"color\": \"#0066CC\",\n      \"is_underlined\": true\n    },\n    \"list\": {\n      \"text_style\": {\n        \"font_family\": \"Helvetica\",\n        \"font_size_in_pt\": 11.0,\n        \"line_height\": 1.5,\n        \"color\": \"#333333\"\n      },\n      \"marker_color\": \"#333333\",\n      \"marker_gap_in_pt\": 8.0\n    },\n    \"table\": {\n      \"header\": {\n        \"background_color\": \"#333333\",\n        \"text_color\": \"#FFFFFF\",\n        \"font_size_in_pt\": 11.0,\n        \"font_weight\": \"bold\"\n      },\n      \"body\": {\n        \"background_color\": \"#FFFFFF\",\n        \"text_color\": \"#333333\",\n        \"font_size_in_pt\": 11.0\n      },\n      \"border\": {\n        \"outer\": {\n          \"top\": {\n            \"color\": \"#CCCCCC\",\n            \"width_in_pt\": 1.0\n          },\n          \"right\": {\n            \"color\": \"#CCCCCC\",\n            \"width_in_pt\": 1.0\n          },\n          \"bottom\": {\n            \"color\": \"#CCCCCC\",\n            \"width_in_pt\": 1.0\n          },\n          \"left\": {\n            \"color\": \"#CCCCCC\",\n            \"width_in_pt\": 1.0\n          }\n        },\n        \"inner\": {\n          \"horizontal\": {\n            \"color\": \"#EEEEEE\",\n            \"width_in_pt\": 0.5\n          },\n          \"vertical\": {\n            \"color\": \"#EEEEEE\",\n            \"width_in_pt\": 0.5\n          }\n        }\n      }\n    },\n    \"grid\": {\n      \"background_color\": \"#FFFFFF\",\n      \"border_color\": \"#CCCCCC\",\n      \"border_width_in_pt\": 0.0,\n      \"gap_in_pt\": 12.0\n    },\n    \"separator\": {\n      \"color\": \"#CCCCCC\",\n      \"thickness_in_pt\": 1.0,\n      \"spacing_before_in_pt\": 12.0,\n      \"spacing_after_in_pt\": 12.0\n    },\n    \"image\": {\n      \"border_color\": \"#000000\",\n      \"border_width_in_pt\": 0.0\n    }\n  },\n  \"footer\": [\n    {\n      \"type\": \"paragraph\",\n      \"runs\": [\n        {\n          \"text\": \"Confidential \\u2014 Nordlicht Technologies GmbH \\u2014 NDA-2026-0389\"\n        }\n      ]\n    }\n  ],\n  \"content\": [\n    {\n      \"type\": \"headline\",\n      \"level\": \"h1\",\n      \"text\": \"Non-Disclosure Agreement\"\n    },\n    {\n      \"type\": \"paragraph\",\n      \"runs\": [\n        {\n          \"text\": \"This Non-Disclosure Agreement (\\\"Agreement\\\") is entered into as of \"\n        },\n        {\n          \"text\": \"March 14,\\n              2026\",\n          \"font_weight\": \"bold\"\n        },\n        {\n          \"text\": \" (the \\\"Effective Date\\\") by and between \"\n        },\n        {\n          \"text\": \"Nordlicht Technologies GmbH\",\n          \"font_weight\": \"bold\"\n        },\n        {\n          \"text\": \",\\n              a German company with its principal office at Friedrichstrasse 68, 10117 Berlin,\\n              Austin,\\n              TX 78701 (the \\\"Disclosing Party\\\"),\\n              and \"\n        },\n        {\n          \"text\": \"Globex Corporation\",\n          \"font_weight\": \"bold\"\n        },\n        {\n          \"text\": \",\\n              a German company with offices at Sonnenstrasse 12, 80331 Munich,\\n              Berlin,\\n              CA 94105 (the \\\"Receiving Party\\\").\"\n        }\n      ]\n    },\n    {\n      \"type\": \"separator\"\n    },\n    {\n      \"type\": \"headline\",\n      \"level\": \"h2\",\n      \"text\": \"Terms and Conditions\"\n    },\n    {\n      \"type\": \"list\",\n      \"variant\": \"ordered\",\n      \"items\": [\n        {\n          \"text\": \"Definition of Confidential Information. \\\"Confidential Information\\\" means any non-public information disclosed by the Disclosing Party to the Receiving Party,\\n                whether orally,\\n                in writing,\\n                or by inspection,\\n                including but not limited to trade secrets,\\n                business plans,\\n                financial data,\\n                software,\\n                and technical specifications.\"\n        },\n        {\n          \"text\": \"Obligations of Receiving Party. The Receiving Party agrees to hold all Confidential Information in strict confidence,\\n                use it solely for the purpose of evaluating a potential business relationship,\\n                and not disclose it to any third party without prior written consent.\"\n        },\n        {\n          \"text\": \"Exclusions. This Agreement does not apply to information that: (a) is or becomes publicly available through no fault of the Receiving Party; (b) was known to the Receiving Party prior to disclosure; (c) is independently developed without use of Confidential Information; or (d) is required to be disclosed by law or court order.\"\n        },\n        {\n          \"text\": \"Term and Termination. This Agreement shall remain in effect for a period of two (2) years from the Effective Date. The obligations of confidentiality shall survive termination for an additional three (3) years.\"\n        },\n        {\n          \"text\": \"Return of Materials. Upon termination or request,\\n                the Receiving Party shall promptly return or destroy all Confidential Information and any copies thereof,\\n                and certify such destruction in writing.\"\n        },\n        {\n          \"text\": \"Governing Law. This Agreement shall be governed by and construed in accordance with the laws of Germany,\\n                without regard to conflict of laws principles.\"\n        }\n      ]\n    },\n    {\n      \"type\": \"separator\"\n    },\n    {\n      \"type\": \"grid\",\n      \"columns\": [\n        {\n          \"column_span\": 6,\n          \"blocks\": [\n            {\n              \"type\": \"paragraph\",\n              \"runs\": [\n                {\n                  \"text\": \"Disclosing Party\\n\\n\",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"Signature: ________________________\\n\\n\"\n                },\n                {\n                  \"text\": \"Name: \",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"____________________\\n\\n\"\n                },\n                {\n                  \"text\": \"Title: \",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"____________________\\n\\n\"\n                },\n                {\n                  \"text\": \"Date: \",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"____________________\"\n                }\n              ]\n            }\n          ]\n        },\n        {\n          \"column_span\": 6,\n          \"blocks\": [\n            {\n              \"type\": \"paragraph\",\n              \"runs\": [\n                {\n                  \"text\": \"Receiving Party\\n\\n\",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"Signature: ________________________\\n\\n\"\n                },\n                {\n                  \"text\": \"Name: \",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"____________________\\n\\n\"\n                },\n                {\n                  \"text\": \"Title: \",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"____________________\\n\\n\"\n                },\n                {\n                  \"text\": \"Date: \",\n                  \"font_weight\": \"bold\"\n                },\n                {\n                  \"text\": \"____________________\"\n                }\n              ]\n            }\n          ]\n        }\n      ]\n    }\n  ]\n}"
      },
      "type": "n8n-nodes-iterationlayer.iterationLayer",
      "typeVersion": 1,
      "position": [
        500,
        300
      ],
      "id": "28a36a44-7981-411d-9e32-79bbb18874d6",
      "name": "Generate Document",
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
            "node": "Generate Document",
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
Generate a non-disclosure agreement PDF. Use the generate_document tool with format "pdf" and these content blocks:

- Headline: "Non-Disclosure Agreement"
- Paragraph: effective date and party names — [disclosing party] and [receiving party]
- Headline: "Definition of Confidential Information" with clause text
- Headline: "Obligations" with non-disclosure obligations
- Headline: "Term" with agreement duration
- Paragraph: signature lines for both parties with date fields
```

### Response


```json
{
  "success": true,
  "data": {
    "buffer": "JVBERi0xLjcKMSAwIG9iago8...",
    "mime_type": "application/pdf"
  }
}
```


## Links

- [Integration guide](https://iterationlayer.com/SKILL.md)
- [Full documentation](https://iterationlayer.com/docs)
- [OpenAPI spec](https://api.iterationlayer.com/openapi.json)
- [Browse all recipes](https://iterationlayer.com/recipes)
