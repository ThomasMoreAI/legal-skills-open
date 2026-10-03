---
name: client-intake-compdeep
title: Client intake compdeep
description: Create a new client intake folder with standard template documents
author: Compdeep
author_url: https://github.com/Compdeep/kaiju/tree/main/docs/examples/law-firm-skills/client-intake
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

Create a new client intake folder and populate it with template documents.

1. Create folder: cases/{{client_name}}/
2. Create file: cases/{{client_name}}/intake.md with:
   - Client: {{client_name}}
   - Matter type: {{matter_type}}
   - Contact: {{contact_email}}
   - Intake date: (today's date)
   - Status: New
3. Create file: cases/{{client_name}}/notes.md with an empty notes template
4. Create file: cases/{{client_name}}/billing.csv with header row: Date,Hours,Description,Rate

Report back what was created.
