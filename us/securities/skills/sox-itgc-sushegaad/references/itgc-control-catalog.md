# ITGC Control Catalog — Controls, Tests, Evidence

Cadences and sample sizes below are prevailing audit convention (no SEC/PCAOB rule prescribes them); align final figures with the external auditor.

## Domain 1 — Access to Programs and Data
| Control | Test procedure | Evidence |
|---|---|---|
| New/modified access granted on documented, role-appropriate approval | Sample new hires/transfers → trace ticket → approval → granted rights match request | Access request tickets, approval trail, system rights report |
| Terminations deprovisioned timely (24–72h convention) | Full population: HR term list vs system disable dates; test exceptions | HR extract, disable timestamps, exception analysis |
| Quarterly user access reviews (UARs) for in-scope systems | Sample quarters → completeness of population, reviewer independence, evidence of revocations executed | UAR workbooks, sign-offs, revocation tickets |
| Privileged access restricted and monitored | Enumerate admin/superuser (incl. DB sysadmin, OS root, ERP profiles like SAP_ALL); justify each; review monitoring/vault logs | Privileged account inventory, PAM logs, justification matrix |
| SoD within access design | Test rule set for conflicting duties (e.g., create vendor + pay vendor; develop + deploy) | SoD ruleset, conflict report, mitigations |
| Authentication policy enforced (incl. MFA where deployed) | Inspect configuration vs policy; test service/generic accounts ownership and password vaulting | Config screenshots, service account register |
| Direct data access (DB/OS) restricted | Enumerate direct-write access to financial data outside the application | DB permission listings, firefighter/elevated-access logs |

## Domain 2 — Program Changes
| Control | Test procedure | Evidence |
|---|---|---|
| Changes approved before production migration | Sample changes (25 convention for frequent) → approval precedes migration date | Change tickets, CAB minutes, deployment logs |
| Testing performed and documented before migration | Same sample → test plans/results/UAT sign-off | Test evidence attached to ticket |
| Developer/deployer segregation | Compare developer list to production-migration rights; where tooling merges roles, test compensating review | Access listings for deploy tooling, pipeline permissions |
| Emergency changes controlled | Sample emergency changes → expedited authorization + after-the-fact approval and review | Emergency change log, post-implementation reviews |
| Configuration changes in scope | Confirm change population includes config/master-data-engine/workflow changes, not just code | Population completeness reconciliation (tool extract vs deployment log) |

## Domain 3 — Computer Operations
| Control | Test procedure | Evidence |
|---|---|---|
| Financially relevant batch jobs scheduled and monitored; failures resolved | Sample days/failures → alert → ticket → resolution → rerun evidence | Scheduler logs, incident tickets |
| Backups executed and monitored | Sample periods → completion logs, failure follow-up | Backup reports, failure tickets |
| Restore testing performed periodically | Inspect most recent restore test for in-scope systems | Restore test results |
| Incidents affecting financial systems managed | Sample incidents → triage, resolution, escalation to finance where data integrity implicated | Incident records |

## Domain 4 — Program Development
| Control | Test procedure | Evidence |
|---|---|---|
| New system/major implementation authorized | Project charter/steering approval | Charter, minutes |
| Testing strategy incl. UAT with business sign-off | Inspect test phases and finance sign-off before go-live | UAT results, sign-off |
| Data conversion validated | Reconciliations of converted balances; error handling | Conversion recs, sign-off |
| Go-live approval and hypercare | Cutover approval; post-go-live issue tracking | Go-live approval, hypercare log |

## Cross-cutting
- **IPE (information produced by the entity)**: any report used in a control needs accuracy/completeness validation (source, parameters, logic).
- **End-user computing**: in-scope spreadsheets need access restriction, input control, and change/version protection proportional to complexity.
- **SOC 1 reliance**: map subservice CUECs into your control set; verify the report period covers your fiscal year; bridge letters for gaps.
- **AI/automation (emerging)**: model/prompt/config changes to automated financial controls follow Domain 2; monitor PCAOB focus on GenAI at issuers (2025 priorities).
