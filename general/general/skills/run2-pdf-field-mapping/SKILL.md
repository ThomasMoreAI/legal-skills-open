---
name: run2-pdf-field-mapping
title: PDF Field Mapping
description: Techniques for mapping case descriptions to PDF form fields.
author: cxcscmu
author_url: https://github.com/cxcscmu/SkillLearnBench/tree/main/skills/b2-self-feedback-gemini-3-flash-preview/court-form-filling/run2_pdf-field-mapping
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# PDF Field Mapping

When mapping case data to PDF fields:

1. **Analyze Field IDs**: Look for keywords in the `field_id` (e.g., `PlaintiffName`, `DefendantAddress`, `ClaimAmount`).
2. **Use Bounding Boxes**: If IDs are cryptic, use the `rect` (bounding box) and the page number to identify the field's position on the form.
3. **Handle Checkboxes**: Identify the `checked_value` for "Yes" or "No" options. Usually, `/1` is Yes and `/2` or `/Off` is No, but verify in `field_info.json`.
4. **Consistency Check**: Ensure that data like names and addresses are consistent across different sections of the form (e.g., caption vs. detailed info).
