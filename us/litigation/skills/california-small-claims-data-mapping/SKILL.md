---
name: california-small-claims-data-mapping
title: California small claims data mapping
description: Use this skill to map specific natural language case details to the legal requirements of the SC-100 form.
author: cxcscmu
author_url: https://github.com/cxcscmu/SkillLearnBench/tree/main/skills/b3-teacher-feedback-gemini-3.1-flash-lite-preview/court-form-filling/run1_california-small-claims-data-mapping
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: litigation
language: en
---

When mapping case details to the SC-100 form:

*   **Plaintiff/Defendant Information**: Ensure contact details are placed in the correct sections. 
    *   *Plaintiff (Joyce He)*: 655 S Fair Oaks Ave, Sunnyvale, CA 94086; 4125886066; he1998@gmail.com.
    *   *Defendant (Zhi Chen)*: 299 W Washington Ave, Sunnyvale, CA 94086; 5125658878.
*   **Claim Amount**: The amount ($1500) must be clearly stated in the "Amount Requested" field.
*   **Narrative (The "Why")**: Provide a concise summary: "Defendant failed to return $1500 security deposit as per signed roommate sublease contract. Attempts to resolve via text were ignored."
*   **Jurisdiction**: Confirm the filing location (Sunnyvale) matches the venue rules (Defendant's residence).
*   **Dates**: Ensure all dates are converted to YYYY-MM-DD format (e.g., 2026-01-19).
