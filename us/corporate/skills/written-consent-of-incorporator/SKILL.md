---
name: written-consent-of-incorporator
title: Action by Written Consent of Incorporator
description: Drafts a U.S. corporate Action by Written Consent of Incorporator for post-formation organizational actions (adopting bylaws, appointing directors, transitioning authority to board). Use when the prompt mentions "written consent," "incorporator," "formation filing," "adopt bylaws," "appoint initial directors," or "organize corporation."
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/written-consent-of-incorporator
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: corporate
language: en
tags: [agreement, drafting]
---

# Action by Written Consent of Incorporator

Generates an execution-ready incorporator written-consent resolution for post-formation organizational actions and minute-book filing.

## Required Inputs

Collect before drafting:

1. Corporation legal name (must match Articles exactly)
2. State of incorporation
3. Articles of Incorporation filing date
4. Incorporator(s) full legal name(s)
5. Initial directors' full legal names
6. Bylaws text or instruction to attach separately
7. Any nonstandard actions (bank authorization, fiscal year, stock issuance, etc.)
8. Whether multiple incorporators consent jointly

## Quick Start

1. Validate all inputs against formation documents.
2. Draft the consent using the structure below.
3. Run quality checks before delivering.

## Document Structure

Draft sections in this order:

1. **Title**: `ACTION BY WRITTEN CONSENT OF INCORPORATOR of [Corporation Name], a [State] Corporation`
2. **Preamble**: Identify incorporator(s), cite corporation name/state/filing date, state purpose under applicable corporation law.
3. **Resolutions** (numbered):
   - Adopt bylaws (reference as Exhibit A or note separate attachment)
   - Appoint/elect initial directors
   - Additional organizational actions only if requested
4. **Transition clause**: Incorporator confirms completion of duties; authority transfers to board.
5. **Execution block**: Minute-book filing instruction, signature line per incorporator (printed name / title / date).

### Template

```text
ACTION BY WRITTEN CONSENT OF INCORPORATOR
of [Corporation Name], a [State] Corporation

[Effective Date]

The undersigned [sole incorporator / incorporators], [name(s)],
hereby adopt this written consent on behalf of [Corporation Name],
a [State] corporation, pursuant to filing of its Articles of
Incorporation on [Filing Date].

RESOLVED THAT:
1. [Adopt Bylaws as Exhibit A ...]
2. [The following persons are appointed as initial directors: ...]
3. [Additional organizational action(s) as requested.]

RESOLVED FURTHER THAT the undersigned incorporator(s) has completed
all acts of an incorporator and all authority is transferred to the
board of directors.

Executed this [Date].

_________________________________
[Incorporator Printed Name]   Signature
```

## Quality Checks

- [ ] No bracketed placeholders remain
- [ ] Corporation name, state, filing date, incorporator identity consistent throughout
- [ ] Director count aligns with charter/state requirements
- [ ] Numbered resolutions, clear headings, execution-ready format

## Pitfalls

- **Multiple incorporators**: Use a separate subsection to clarify consent authority per incorporator.
- **Jurisdiction gaps**: Tag unconfirmed state-specific rules with `[VERIFY]`. Default to MBCA-style conventions but check governing state law.
- **Statutory neutrality**: Keep language generic unless a specific state rule is provided.
- **Notarization**: Usually not required for written consent; flag if jurisdiction or filing office requires it.
- **No legal advice**: Draft the governance instrument only — never imply attorney-client advice.
