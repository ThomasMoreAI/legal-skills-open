---
name: run1-pdf-form-filling
title: Run1 pdf form filling
description: Use this skill to identify, extract, and populate specific fields within a PDF form using the pdftk or pikepdf toolsets.
author: cxcscmu
author_url: https://github.com/cxcscmu/SkillLearnBench/tree/main/skills/b3-teacher-feedback-gemini-3.1-flash-lite-preview/court-form-filling/run1_pdf-form-filling
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

To fill a PDF form programmatically:

1.  **Identify Field Names**: Use `pdftk /root/sc100-blank.pdf dump_data_fields` to list all available form fields and their current values.
2.  **Prepare Data**: Create a data mapping of the field names found in the previous step to the values provided in the case description (e.g., Plaintiff Name, Defendant Address, Claim Amount).
3.  **Populate**: Use `pdftk /root/sc100-blank.pdf fill_form data.fdf output /root/sc100-filled.pdf` or an equivalent Python library like `pypdf` to inject the data.
4.  **Verification**: Always inspect the output file to ensure that long strings (like addresses) are not truncated and that formatting (like date strings) matches the required format (YYYY-MM-DD).
