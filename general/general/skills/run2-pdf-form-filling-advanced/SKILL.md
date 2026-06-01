---
name: run2-pdf-form-filling-advanced
title: Advanced PDF Form Filling
description: Advanced techniques for filling PDF forms with fillable fields.
author: cxcscmu
author_url: https://github.com/cxcscmu/SkillLearnBench/tree/main/skills/b2-self-feedback-gemini-3-flash-preview/court-form-filling/run2_pdf-form-filling-advanced
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

# Advanced PDF Form Filling

1. **Mandatory Fields**: Each entry in `field_values.json` MUST include `field_id`, `page`, and `value`.
```json
{
  "field_id": "...",
  "page": 1,
  "value": "..."
}
```
2. **Date Formats**: Adhere strictly to requested date formats (e.g., `xxxx-xx-xx`).
3. **Multi-line Text**: For long descriptions, ensure they fit the field or are concisely summarized.
4. **Validation**: Always verify the existence of the output file and, if possible, check for errors in the filling script output.
5. **Empty Fields**: Leave optional or non-relevant fields empty as per user instructions.
