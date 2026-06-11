---
name: aml-compliance
title: Overview
description: Anti-Money Laundering (AML) and Know Your Customer (KYC) compliance workflow. Sanctions screening, PEP detection, transaction monitoring, suspicious activity reporting (SAR), and OFAC compliance.
author: mkurman
author_url: https://github.com/mkurman/zorai/tree/main/skills/scientific-skills/aml-compliance
license: MIT
version: 0.1.1
execution_mode: open
jurisdiction: us
practice: white-collar
language: en
tags: [aml, kyc, compliance, anti-money-laundering, sanctions, regulatory, zorai]
---

## Overview

AML/KYC compliance covers sanctions screening, PEP detection, transaction monitoring, currency transaction reports (CTR), suspicious activity reports (SAR), and OFAC compliance. Essential for fintech, banking, and payment applications handling regulated financial transactions.

## Installation

```bash
uv pip install requests  # for sanctions API integration
```

## Screening Rules

```python
THRESHOLDS = {"ctr": 10000, "structuring_lookback": 5000}
HIGH_RISK_COUNTRIES = {"IR", "KP", "SY", "CU", "MM"}

def screen_tx(tx):
    alerts = []
    if tx.amount >= THRESHOLDS["ctr"]:
        alerts.append("CTR required — cash transaction over $10k")
    if tx.country in HIGH_RISK_COUNTRIES:
        alerts.append("OFAC sanctioned jurisdiction — enhanced due diligence")
    if tx.is_pep:
        alerts.append("PEP flagged — enhanced monitoring")
    return alerts
```

## References
- [FinCEN BSA](https://www.fincen.gov/)
- [OFAC SDN search](https://sanctionssearch.ofac.treas.gov/)
- [FATF recommendations](https://www.fatf-gafi.org/)
