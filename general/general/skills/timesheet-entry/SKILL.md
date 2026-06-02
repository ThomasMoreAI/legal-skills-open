---
name: timesheet-entry
title: Timesheet entry
description: Creates a CSV timesheet entry for a specified client and matter and appends it to the corresponding timesheet file, adding a header row if the file does not yet exist.
author: Compdeep
author_url: https://github.com/Compdeep/kaiju/tree/main/docs/examples/law-firm-skills/timesheet
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

Create a timesheet entry in CSV format and append it to the timesheet file.

Format: {{date}},{{client}},{{matter}},{{hours}},{{description}}

Append this line to the file: timesheets/{{client}}-{{matter}}.csv

If the file doesn't exist yet, add a header row first:
Date,Client,Matter,Hours,Description
