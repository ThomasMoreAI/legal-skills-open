---
name: court-deadline
title: Court deadline
description: Calculate court filing deadlines based on jurisdiction rules
author: Compdeep
author_url: https://github.com/Compdeep/kaiju/tree/main/docs/examples/law-firm-skills/court-deadline
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
---

Calculate the filing deadline based on these rules:

Federal courts:
- Response to complaint: 21 days from service
- Appeal notice: 30 days from judgment
- Discovery responses: 30 days from service
- Motion responses: 14 days from service

Texas State courts:
- Response to complaint (answer): 20 days + next Monday rule
- Appeal notice: 30 days from judgment
- Discovery responses: 30 days from service
- Motion responses: 21 days from service

Starting from {{event_date}} in {{jurisdiction}} for deadline type {{deadline_type}}:
1. Calculate the calendar date
2. Check if it falls on a weekend or federal holiday — if so, move to next business day
3. Report the deadline date and how many calendar days remain from today
