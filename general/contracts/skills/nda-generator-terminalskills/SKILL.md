---
name: nda-generator-terminalskills
title: NDA Generator
description: Generate professional Non-Disclosure Agreements for meetings, partnerships, and employment. Use when a user asks to create an NDA, draft a confidentiality agreement, generate a non-disclosure document, make an NDA for a meeting, or prepare a mutual NDA for a partnership. Supports unilateral and mutual NDAs.
author: TerminalSkills
author_url: https://github.com/TerminalSkills/skills/tree/main/skills/nda-generator
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# NDA Generator

## Overview

Generate professional Non-Disclosure Agreements (NDAs) tailored to specific business contexts. This skill creates legally structured NDA documents covering confidentiality terms, obligations, duration, exclusions, and remedies. Supports mutual and unilateral NDAs for employment, partnerships, meetings, and contractor engagements.

## Instructions

When a user asks to create or generate an NDA, follow these steps:

### Step 1: Determine the NDA type and context

Identify what kind of NDA is needed:
- **Mutual NDA**: Both parties share confidential information (partnerships, joint ventures)
- **Unilateral NDA**: One party discloses to the other (employee, contractor, investor pitch)

Collect required details:
- **Disclosing party**: Name, title, company, address
- **Receiving party**: Name, title, company, address
- **Purpose**: Why confidential information is being shared
- **Duration**: How long the confidentiality obligation lasts (typically 1-5 years)
- **Governing law**: Jurisdiction / state for legal enforcement
- **Specific exclusions**: Any carve-outs or exceptions the user wants

### Step 2: Select the appropriate template sections

Every NDA should include these core sections:

1. **Preamble**: Date, party names, purpose statement
2. **Definition of Confidential Information**: What is covered (documents, data, trade secrets, discussions)
3. **Obligations of Receiving Party**: Non-disclosure, limited use, protection standards
4. **Exclusions**: Information that is not covered (publicly available, independently developed, prior knowledge)
5. **Term and Duration**: Effective date, confidentiality period, survival clauses
6. **Return or Destruction**: What happens to materials when the NDA expires
7. **Remedies**: Injunctive relief, damages for breach
8. **General Provisions**: Governing law, jurisdiction, amendments, entire agreement, severability
9. **Signature Block**: Lines for both parties with name, title, date

### Step 3: Generate the document

Create the NDA as a DOCX file (editable) or PDF:

```python
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def generate_nda(data, output_path="nda.docx"):
    doc = Document()

    # Title
    title = doc.add_heading('NON-DISCLOSURE AGREEMENT', level=0)
    title.alignment = WD_ALIGN_PARAGRAPH.CENTER

    # Preamble
    doc.add_paragraph(
        f"This Non-Disclosure Agreement (\"Agreement\") is entered into as of "
        f"{data['effective_date']} (\"Effective Date\") by and between:"
    )
    doc.add_paragraph(
        f"{data['party_a']['name']}, located at {data['party_a']['address']} "
        f"(\"{'Disclosing Party' if not data['mutual'] else 'Party A'}\")"
    )
    doc.add_paragraph(
        f"{data['party_b']['name']}, located at {data['party_b']['address']} "
        f"(\"{'Receiving Party' if not data['mutual'] else 'Party B'}\")"
    )

    # Add each section with heading and content
    for section in data['sections']:
        doc.add_heading(section['title'], level=1)
        doc.add_paragraph(section['content'])

    # Signature block
    doc.add_heading('SIGNATURES', level=1)
    doc.add_paragraph(f"\n{'_' * 40}\n{data['party_a']['name']}\nTitle: {data['party_a'].get('title', '')}\nDate: _______________")
    doc.add_paragraph(f"\n{'_' * 40}\n{data['party_b']['name']}\nTitle: {data['party_b'].get('title', '')}\nDate: _______________")

    doc.save(output_path)
    return output_path
```

### Step 4: Review and present

After generating:
1. Display a summary of key terms
2. List all sections included
3. Remind the user to have a lawyer review before signing

## Examples

### Example 1: Mutual NDA for a business partnership

**User request:** "Create a mutual NDA between my company TechFlow Inc and DataBridge LLC for a potential data integration partnership"

**Actions taken:**
1. Set up as mutual NDA
2. Include standard partnership confidentiality terms
3. Default to 2-year term

**Output:**
```
Generated: nda_techflow_databridge.docx

NDA Summary:
  Type: Mutual Non-Disclosure Agreement
  Party A: TechFlow Inc
  Party B: DataBridge LLC
  Purpose: Evaluation of potential data integration partnership
  Duration: 2 years from Effective Date
  Governing Law: State of Delaware

Sections included:
  1. Definition of Confidential Information
  2. Mutual Obligations
  3. Exclusions from Confidential Information
  4. Term and Termination
  5. Return of Materials
  6. Remedies
  7. General Provisions
  8. Signature Block

IMPORTANT: This is a template. Have legal counsel review before signing.
```

### Example 2: Employee NDA

**User request:** "Generate an NDA for a new software engineer joining our company. They'll have access to our source code and customer data."

**Actions taken:**
1. Create unilateral NDA (company discloses to employee)
2. Specifically cover source code and customer data
3. Include post-employment obligations

**Output:**
```
Generated: nda_employee_agreement.docx

NDA Summary:
  Type: Unilateral (Employee Confidentiality Agreement)
  Disclosing Party: [Your Company]
  Receiving Party: [Employee Name]
  Scope: Source code, customer data, trade secrets, business processes
  Duration: During employment + 3 years post-termination
  Non-solicitation: 12 months post-termination

Sections included:
  1. Definition of Confidential Information (specifically covers source code
     and customer data)
  2. Employee Obligations
  3. Exclusions
  4. Intellectual Property Assignment
  5. Non-Solicitation
  6. Term and Survival
  7. Return of Company Property
  8. Remedies and Enforcement
  9. Signature Block
```

### Example 3: Meeting NDA

**User request:** "I need a quick NDA for a meeting with an investor tomorrow where I'll be sharing our product roadmap"

**Actions taken:**
1. Create unilateral NDA for investor meeting
2. Scope to product roadmap and business plans
3. Keep terms standard and concise

**Output:**
```
Generated: nda_investor_meeting.docx

NDA Summary:
  Type: Unilateral (Investor Meeting)
  Disclosing Party: [Your Company]
  Receiving Party: [Investor Name]
  Purpose: Evaluation of potential investment opportunity
  Scope: Product roadmap, financial projections, business strategy
  Duration: 2 years

This is a concise 3-page NDA suitable for investor meetings.
Fill in the bracketed fields before the meeting.
```

## Guidelines

- Always include a disclaimer that the generated NDA is a template and should be reviewed by legal counsel before execution.
- Default confidentiality duration to 2 years for business partnerships and 3 years post-termination for employment NDAs.
- Generate DOCX format by default so the user can edit the document. Offer PDF as an alternative.
- Use clear, plain language where possible while maintaining legal precision.
- Include standard exclusions in every NDA: publicly available information, independently developed information, information received from third parties, and information disclosed by court order.
- For mutual NDAs, ensure obligations are symmetric and apply equally to both parties.
- Bracketed placeholders like [Company Name] should be used for any information the user has not provided, making it easy to fill in later.
- Install python-docx with `pip install python-docx` if not available.
