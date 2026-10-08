---
name: draft-cap-table-resolution-sboghossian
title: Draft — Cap Table Resolution
description: Use when a board or shareholder resolution is needed to formally record and authorize a cap table update following a share issuance, option exercise, transfer, conversion, or other equity event. Captures the pre- and post-event cap table, authorizes the share register update, and triggers any required registrar filing. Applicable across all corporate jurisdictions — format and filing requirements vary by jurisdiction.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-cap-table-resolution
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Draft — Cap Table Resolution

## When to use this

A cap table resolution is required whenever a company's equity ownership structure changes. Without a board or shareholder resolution formally authorizing the change and directing the share register update, the equity event is not properly documented and may be challenged.

**Triggering events**:
- New share issuance (to new investor, existing shareholder, or employee)
- Option or warrant exercise
- Transfer of shares between existing shareholders
- Conversion of convertible note or SAFE into equity
- Share buyback or cancellation
- Creation of a new share class
- Reclassification or consolidation of existing shares
- Vesting acceleration event

## Required inputs

| Input | Notes |
|---|---|
| Triggering event | Identify the specific equity event |
| Pre-event cap table | All shareholders, classes, share count, percentage |
| Post-event cap table | After the change, reflecting new ownership |
| New shareholder details (if applicable) | Full legal name, nationality, address, ID/registration number |
| Share details | Class, number of new/transferred/cancelled shares |
| Consideration (if applicable) | Price per share; aggregate consideration; date of payment |
| Authorization basis | Subscription agreement, option exercise notice, board approval of transfer |
| Registrar filing requirement | Does the jurisdiction require a filing to update the commercial register? |

## Document structure

### Resolution form

```
WRITTEN RESOLUTION OF THE BOARD OF DIRECTORS
OF [COMPANY NAME] ([REGISTRATION NUMBER])
Dated: [DATE]

The Board of Directors, having reviewed the [Subscription Agreement / 
Transfer Instrument / Option Exercise Notice / Conversion Notice] dated 
[DATE] relating to the [issuance / transfer / conversion] of [NUMBER] 
[CLASS] shares (the "Equity Event"), hereby RESOLVE as follows:

1. EQUITY EVENT AUTHORIZED
   RESOLVED THAT the [issuance of [NUMBER] new [CLASS] shares / transfer 
   of [NUMBER] [CLASS] shares from [Transferor] to [Transferee] / 
   conversion of [CONVERTIBLE INSTRUMENT] into [NUMBER] [CLASS] shares] 
   on the terms set out in the [Subscription Agreement / Transfer 
   Instrument] dated [DATE] be and is hereby approved and authorized.

2. UPDATED CAPITALIZATION

   Pre-Event Capitalization:
   ┌──────────────────┬───────────┬──────────┬──────────┐
   │ Shareholder      │ Class     │ Shares   │ %        │
   ├──────────────────┼───────────┼──────────┼──────────┤
   │ [Name A]         │ Ordinary  │ [X]      │ [X%]     │
   │ [Name B]         │ Ordinary  │ [X]      │ [X%]     │
   │ Option Pool      │ Options   │ [X]      │ [X%]     │
   │ TOTAL            │           │ [X]      │ 100%     │
   └──────────────────┴───────────┴──────────┴──────────┘

   Post-Event Capitalization:
   ┌──────────────────┬───────────┬──────────┬──────────┐
   │ Shareholder      │ Class     │ Shares   │ %        │
   ├──────────────────┼───────────┼──────────┼──────────┤
   │ [Name A]         │ Ordinary  │ [X]      │ [X%]     │
   │ [Name B]         │ Ordinary  │ [X]      │ [X%]     │
   │ [New Investor]   │ Pref A    │ [X]      │ [X%]     │
   │ Option Pool      │ Options   │ [X]      │ [X%]     │
   │ TOTAL            │           │ [X]      │ 100%     │
   └──────────────────┴───────────┴──────────┴──────────┘

3. SHARE REGISTER UPDATE
   RESOLVED FURTHER THAT the Company's share register (register of 
   members) be updated to reflect the post-event capitalization set out 
   above, with effect from [DATE].

4. REGISTRAR FILING [if required]
   RESOLVED FURTHER THAT [the Company Secretary / [Name], Director] is 
   authorized and directed to file the necessary notifications with 
   [Ministry of Economy / DED / DIFC Registrar / Commercial Register] 
   to register the changes to the Company's shareholding structure 
   within [X] days of this resolution.

5. SHARE CERTIFICATES [if applicable]
   RESOLVED FURTHER THAT new share certificates bearing the Company seal 
   be issued to [New Shareholder] in respect of [NUMBER] [CLASS] shares 
   and that any existing certificates affected by this Equity Event be 
   cancelled.

6. ANCILLARY AUTHORITY
   RESOLVED FURTHER THAT [Name / the Directors] are authorized to 
   execute all documents, make all filings, and take all steps necessary 
   to give effect to this resolution.

IN WITNESS WHEREOF:

_______________________        _______________________
[Director Name]                [Director Name]
Director                       Director
Date: ___________              Date: ___________
```

## Jurisdictional filing requirements

| Jurisdiction | Filing requirement | Platform | Deadline |
|---|---|---|---|
| **UAE onshore (LLC)** | File change-of-shareholders with DED (or free-zone authority) | TAMM / DED online | Typically within 30 days; vary by emirate |
| **UAE (PJSC)** | Notify SCA; update shareholder register with securities depository | Nasdaq Dubai / ADX depository | Per SCA rules |
| **KSA** | File with Ministry of Commerce; notarize and authenticate | Mawthq platform | Within the time stipulated in Companies Law |
| **DIFC** | File change in shareholders with DIFC Registrar | DIFC eportal | No fixed deadline but best practice: promptly |
| **ADGM** | File with ADGM Registration Authority | ADGM portal | Within 14 days for most events |
| **LB** | Notarize and register amendment with Commercial Register in jurisdiction of incorporation | Commercial Register | Promptly; publicity required |
| **US (Delaware)** | No filing for private companies unless authorized share count changes (amend Certificate of Incorporation) | Delaware SOC | Per DGCL |

## Special cases

### Convertible note conversion
When a convertible note converts to equity:
- The resolution should reference the convertible note agreement, the conversion trigger event, and the conversion price calculation.
- Attach: (a) copy of the convertible note; (b) conversion calculation showing principal + accrued interest ÷ conversion price = shares issued; (c) acknowledgment that the note is cancelled upon conversion.

### Option exercise
- Reference the equity plan and option grant letter.
- Confirm the exercise price has been paid (or the exercise method: cash / net exercise / cashless exercise).
- Issue shares from the unissued option pool.

### SAFE conversion
- SAFEs convert on a "qualified financing" trigger.
- Board resolution should confirm that the triggering financing qualifies under the SAFE terms.
- Confirm the conversion price methodology (cap-implied price vs discount-implied price, whichever is lower).
- See [[draft-convertible-note]] for the SAFE vs note discussion.

## Common mistakes

- **No pre/post cap table in the resolution**: the resolution must contain or reference the updated cap table; it is the authoritative record.
- **Forgetting to cancel old share certificates**: uncancelled certificates can be used fraudulently; always cancel and reissue.
- **Missing registrar filing deadline**: in UAE and KSA, delayed filings can result in fines and the change not being recognized by third parties.
- **Conversion calculation not attached**: for convertible note or SAFE conversions, always attach the calculation as an exhibit to avoid future disputes about the share count.
- **Not updating option pool**: if shares are issued from the option pool, the resolution must note the remaining unissued pool size.

## Related skills

- [[draft-board-resolution]]
- [[draft-articles-of-association]]
- [[draft-agm-minutes]]
- [[draft-convertible-note]]
