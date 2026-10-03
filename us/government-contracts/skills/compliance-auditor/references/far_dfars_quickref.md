# FAR/DFARS Quick Reference

The most-frequently encountered clause families in federal RFPs and what they govern. Use to drive `APPLIES_TO` validation in check C1.

## FAR (Federal Acquisition Regulation)

| Family       | Governs                                    |
| ------------ | ------------------------------------------ |
| FAR 52.2     | Contract clauses (general)                 |
| FAR 52.203-x | Contractor ethics, anti-kickback           |
| FAR 52.204-x | Administrative matters, SAM, info security |
| FAR 52.212-x | Commercial items                           |
| FAR 52.215-x | Negotiation                                |
| FAR 52.219-x | Small business programs                    |
| FAR 52.222-x | Labor laws (SCA, DBA, EEO)                 |
| FAR 52.227-x | Patents, data rights                       |
| FAR 52.232-x | Payment terms                              |
| FAR 52.246-x | Quality assurance                          |
| FAR 52.249-x | Termination                                |

## DFARS (Defense FAR Supplement)

| Family          | Governs                                               |
| --------------- | ----------------------------------------------------- |
| DFARS 252.204-x | Cybersecurity (notably 7012, 7019, 7020, 7021 — CMMC) |
| DFARS 252.225-x | Foreign acquisition (Buy American, etc.)              |
| DFARS 252.227-x | Patent / data rights (DoD-specific)                   |
| DFARS 252.246-x | Quality assurance (DoD-specific)                      |

## Agency Supplements

- **AFFARS** — Air Force
- **AFARS** — Army
- **NMCARS** — Navy/Marine Corps
- **NFS** — NASA
- **DEAR** — Department of Energy
- **HSAR** — DHS

## Validation Hint

A `clause` entity whose name starts with `FAR 52.2`, `DFARS 252.`, `AFFARS`, etc. should always have `APPLIES_TO` at least one workspace entity. If it doesn't, that's a C1 finding (orphan clause).
