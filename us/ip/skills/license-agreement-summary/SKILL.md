---
name: license-agreement-summary
title: IP License Agreement Summary
description: 'Produces a structured U.S. IP license agreement summary covering parties, grant scope, exclusivity, territory, financial terms, restrictions, IP management, risk allocation, and termination. Use when summarizing IP license agreements, extracting deal terms, or flagging licensing risks. Trigger keywords: license agreement, IP license, royalty, exclusivity, field of use, sublicense, audit, termination.'
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/license-agreement-summary
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
tags: [agreement, summarization, summary, transactional]
---

# IP License Agreement Summary

Produce a concise, decision-ready summary of the license deal and its risks.

## Prerequisites

1. Complete, executed agreement and all exhibits/schedules.
2. Amendments, side letters, or addenda.
3. Referenced policies or incorporated documents.
4. Definitions section or list of key defined terms.
5. Business context if available (product, market, commercialization plan).

## Output Structure / Process

1. **Deal Snapshot**

   Mark missing terms `Not specified`.

   | Item | Summary |
   | --- | --- |
   | Licensor | |
   | Licensee | |
   | Effective Date | |
   | Agreement Term | |
   | Renewal | |
   | Territory | |
   | Field of Use | |
   | Exclusivity | |
   | Licensed IP | |
   | Grant Scope | |
   | Sublicensing | |
   | Assignment / Change of Control | |
   | Governing Law | |
   | Dispute Resolution | |
   | Confidentiality | |
   | Notice Method | |

2. **Licensed IP Details**

   List each IP type, identifiers, ownership, and retained rights.

   | IP Type | Identifier / Description | Owner | Notes |
   | --- | --- | --- | --- |
   | Patents | | | |
   | Trademarks | | | |
   | Copyright | | | |
   | Trade Secrets | | | |
   | Know-How / Data | | | |

3. **Financial Terms**

   | Item | Summary |
   | --- | --- |
   | Upfront Fee | |
   | Running Royalty Rate | |
   | Royalty Base | |
   | Minimum Royalties | |
   | Milestones | |
   | Equity / Other Consideration | |
   | Reporting Frequency | |
   | Payment Timing | |
   | Audit Rights | |
   | Royalty Adjustments | |
   | Taxes / Withholding | |
   | Currency | |

4. **Performance Obligations**

   | Party | Obligations | Deadlines / Metrics |
   | --- | --- | --- |
   | Licensee | | |
   | Licensor | | |

5. **Restrictions and Use Limits**

   Include non-competes, field carve-outs, and no-challenge clauses.

   | Restriction | Applies To | Notes |
   | --- | --- | --- |
   | | | |

6. **IP Management and Enforcement**

   | Topic | Summary |
   | --- | --- |
   | Prosecution / Maintenance | |
   | Enforcement Rights | |
   | Defense of Infringement Claims | |
   | Improvements / Derivatives | |
   | Ownership of Improvements | |
   | Marking / Quality Control | |

7. **Risk Allocation**

   | Topic | Summary |
   | --- | --- |
   | Warranties | |
   | Disclaimers | |
   | Indemnities | |
   | Liability Cap | |
   | Exclusions from Cap | |
   | Insurance | |

8. **Termination and Effects**

   | Item | Summary |
   | --- | --- |
   | Termination for Breach | |
   | Termination for Convenience | |
   | Termination on Insolvency | |
   | Termination on Change of Control | |
   | Cure Periods | |
   | Wind-Down / Sell-Off | |
   | Sublicense Survival | |
   | Survival Clauses | |

9. **Key Dates and Notices**

   | Event | Date / Timing | Notice Requirement |
   | --- | --- | --- |
   | Renewal Deadline | | |
   | Milestone Dates | | |
   | Reporting Deadlines | | |
   | Cure Deadlines | | |

10. **Risk Flags and Ambiguities**

    Assign `High`, `Medium`, or `Low` severity.

    | Risk / Ambiguity | Severity | Why It Matters |
    | --- | --- | --- |
    | | | |

## Guidelines

- Prioritize contract language over assumptions; mark missing terms `Not specified`.
- Quote defined terms exactly; do not paraphrase scope or exclusivity.
- Flag unusual clauses: MFN, grant-back, no-challenge, broad audit rights, termination at will.
- Call out inconsistencies between exhibits and the main body.
- Assume U.S. context unless the agreement specifies otherwise.
- Do not provide legal advice; summarize and flag issues only.
