---
name: client-intake-judicialmind
title: Client Intake
description: Client intake and onboarding skill for law firm operations. Use when the user needs assistance with new client screening, conflict checks, engagement letters, matter opening, or client onboarding. Triggers on keywords like "client intake", "new client", "conflict check", "conflicts", "engagement letter", "retainer", "fee agreement", "onboarding", "matter opening".
author: judicialmind
author_url: https://github.com/judicialmind/legal-skills/tree/main/skills/client-intake
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: general
language: en
sources:
- title: Conflict Procedures
  path: references/conflict-procedures.md
- title: Engagement Templates
  path: references/engagement-templates.md
- title: Intake Forms
  path: references/intake-forms.md
---

# Client Intake

This skill provides expert guidance for client onboarding, conflict checking, and engagement establishment.

## Core Capabilities

### 1. Client Screening
- Initial assessment
- Matter evaluation
- Capacity to represent
- Red flag identification

### 2. Conflict Checking
- Parties identification
- Database searching
- Conflict analysis
- Waiver procedures

### 3. Engagement Documentation
- Fee structures
- Scope of representation
- Terms and conditions
- Retainer arrangements

### 4. Matter Setup
- File opening
- Team assignment
- System configuration
- Communication protocols

## Intake Process

### Intake Workflow
```
┌─────────────────────────────────────────────────────────────────┐
│                    CLIENT INTAKE PROCESS                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Initial   →  Screening  →  Conflict  →  Engagement  →  Matter  │
│  Contact      Assessment    Check        Letter        Opening  │
│                                                                  │
│     ↓            ↓            ↓            ↓             ↓      │
│                                                                  │
│  Gather     Evaluate     Run search   Draft terms    Open file  │
│  basic      fit and      Analyze      Negotiate     Assign team │
│  info       capacity     results      Execute       Setup system│
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Initial Screening Questions
```
INITIAL INTAKE FORM

CONTACT INFORMATION
Name: _______________________
Company: ____________________
Phone: ______________________
Email: ______________________
Referred by: ________________

MATTER INFORMATION
Type of matter: ____________
Brief description: __________
Adverse parties: ___________
Urgency/deadlines: _________

INITIAL ASSESSMENT
□ Matter type within firm practice areas
□ No obvious conflicts identified
□ Client appears to have authority
□ Matter appears legitimate
□ Client can afford representation
```

### Red Flags
| Flag | Concern | Action |
|------|---------|--------|
| Fee complaints | Payment issues | Enhanced fee discussion |
| Prior counsel issues | Difficult client | References from prior counsel |
| Unrealistic expectations | Mismatch | Clear expectation setting |
| Urgency pressure | Poor planning | Evaluate capacity |
| Information withholding | Trust issues | Additional vetting |
| Aggressive tactics request | Ethics risk | Ethics discussion |
| Fee shopping | Price sensitivity | Clarify value proposition |

## Conflict Checking

### Parties to Search
1. **Prospective client** (individual and entity)
2. **Adverse parties** (known and anticipated)
3. **Related entities** (parents, subsidiaries, affiliates)
4. **Key individuals** (officers, directors, principals)
5. **Co-parties** (if applicable)
6. **Witnesses** (key witnesses)
7. **Related matters** (connected transactions/litigation)

### Search Protocol
```
CONFLICT SEARCH PROCEDURE

1. GATHER INFORMATION
   □ Full legal names (all variations)
   □ Trade names and DBAs
   □ Corporate affiliates
   □ Key individuals
   □ Related parties

2. RUN SEARCHES
   □ Client/matter database
   □ Conflicts database
   □ Name variations and spelling
   □ Phonetic matches
   □ Historical records

3. ANALYZE RESULTS
   □ Review all hits
   □ Identify potential conflicts
   □ Determine conflict type
   □ Assess severity

4. DOCUMENT
   □ Record search terms
   □ Document results
   □ Note analysis
   □ Obtain sign-off
```

### Conflict Types

**Concurrent Conflicts** (Model Rule 1.7):
| Type | Description | Waivable? |
|------|-------------|-----------|
| Direct adversity | Representing opposing parties | Sometimes |
| Material limitation | Other client/interest limits representation | Sometimes |
| Business transaction | Lawyer has interest adverse to client | With disclosure |

**Former Client Conflicts** (Model Rule 1.9):
| Type | Description | Waivable? |
|------|-------------|-----------|
| Same matter | Same or substantially related matter | With consent |
| Materially adverse | Using confidential information adversely | With consent |

**Prospective Client** (Model Rule 1.18):
- Duty of confidentiality to prospective client
- Cannot be adverse in same/related matter
- Screening may be available

### Conflict Waiver Elements
```
CONFLICT WAIVER

1. IDENTIFICATION
   - Affected clients identified
   - Nature of conflict explained
   - Potential effects described

2. DISCLOSURE
   - Material facts disclosed
   - Risks explained
   - Alternatives discussed

3. CONSENT
   - Informed consent obtained
   - In writing (required for many conflicts)
   - Signed by client

4. ONGOING OBLIGATIONS
   - Duty of loyalty continues
   - Confidentiality maintained
   - Competent representation
```

### Ethical Screens
When permitted (varies by jurisdiction/conflict type):
- Timely screen implementation
- No information sharing
- Written notice to affected client
- Screened lawyer's affirmation
- Periodic compliance certification

## Engagement Letters

### Essential Elements
```
ENGAGEMENT LETTER COMPONENTS

1. IDENTIFICATION
   - Client name (correct legal entity)
   - Matter description
   - Effective date

2. SCOPE OF REPRESENTATION
   - Services included
   - Services excluded
   - Matter limitations

3. FEES AND BILLING
   - Fee structure
   - Rates (current and changes)
   - Expense policy
   - Billing frequency
   - Payment terms
   - Retainer requirements

4. CLIENT RESPONSIBILITIES
   - Truthful information
   - Cooperation
   - Payment obligations
   - Communication

5. COMMUNICATION
   - Primary contacts
   - Response expectations
   - Email/electronic communication

6. TERMINATION
   - Client's right to terminate
   - Firm's right to withdraw
   - Effect of termination
   - File disposition

7. ADDITIONAL TERMS
   - Conflicts acknowledgment
   - Confidentiality
   - File retention
   - Dispute resolution

8. SIGNATURES
   - Firm signature
   - Client signature
   - Date
```

### Fee Structures

| Structure | Description | Best For |
|-----------|-------------|----------|
| Hourly | Time × rate | Litigation, complex matters |
| Flat fee | Fixed amount | Discrete tasks, predictable scope |
| Contingency | % of recovery | Plaintiff personal injury |
| Hybrid | Reduced hourly + success fee | Varied matters |
| Retainer | Prepaid amount | Ongoing representation |
| Subscription | Monthly fee | Corporate clients, ongoing advice |

### Retainer Types
| Type | Description | Accounting |
|------|-------------|------------|
| Security retainer | Held against future fees | Client funds until earned |
| Evergreen retainer | Replenished when drawn | Client funds |
| Classic retainer | Payment for availability | Earned when received |
| Flat fee (prepaid) | Paid in advance | Depends on jurisdiction |

### Engagement Letter Template
```
[FIRM LETTERHEAD]

[Date]

[Client Name]
[Address]

        Re: Engagement of [Firm Name]
            Matter: [Brief Description]

Dear [Client]:

Thank you for selecting [Firm] to represent you. This letter confirms our
engagement and sets forth the terms of our representation.

1. SCOPE OF ENGAGEMENT

We have been engaged to represent you in connection with [matter description].

Our representation does not include [exclusions, e.g., tax advice, appeals,
related matters].

2. FEES AND BILLING

Our fees will be calculated on an hourly basis at our standard rates:
- Partners: $[X] per hour
- Associates: $[X] per hour
- Paralegals: $[X] per hour

We reserve the right to adjust our rates periodically.

[OR for flat fee:]
Our fee for this matter is $[X], payable as follows: [payment schedule].

3. EXPENSES

In addition to fees, we will bill for reasonable out-of-pocket expenses
including [list: filing fees, travel, copying, etc.].

4. BILLING AND PAYMENT

We will submit invoices [monthly/upon completion]. Payment is due within
[30] days. Overdue amounts bear interest at [X]% per month.

5. RETAINER

Please provide an initial retainer of $[X] upon execution of this letter.
The retainer will be deposited in our trust account and applied to fees
and expenses as incurred. [Replenishment terms if evergreen.]

6. COMMUNICATION

[Attorney name] will be primarily responsible for this matter. We will
keep you informed of significant developments and consult with you on
major decisions. You agree to keep us informed of developments and
respond promptly to our requests.

7. FILE RETENTION

Upon conclusion of this matter, we will retain your file for [X] years,
after which it may be destroyed.

8. TERMINATION

You may terminate this engagement at any time. We may withdraw upon
reasonable notice, subject to court approval if required. Upon termination,
you will be responsible for fees and expenses incurred to that date.

Please indicate your agreement to these terms by signing below and
returning a copy with your retainer.

We appreciate your confidence in our firm and look forward to working
with you.

Very truly yours,

[FIRM NAME]


By: _________________________
    [Attorney Name]


AGREED AND ACCEPTED:


_____________________________    Date: _______________
[Client Name/Authorized Signatory]
```

## Matter Opening

### System Setup Checklist
- [ ] Client record created/updated
- [ ] Matter number assigned
- [ ] Billing setup confirmed
- [ ] Team members assigned
- [ ] Practice group assigned
- [ ] Responsible attorney designated
- [ ] Billing attorney designated
- [ ] Rate arrangements entered
- [ ] Budget entered (if applicable)
- [ ] Document folder created
- [ ] Calendar reminders set
- [ ] Conflicts cleared and documented

### Client Welcome Package
- [ ] Welcome letter
- [ ] Contact information
- [ ] Key team bios
- [ ] Communication guidelines
- [ ] Document request list
- [ ] Client portal access
- [ ] Billing information

## Integration with Other Skills

- **case-management**: Matter workflow
- **billing-operations**: Fee arrangements
- **contract-lifecycle**: Engagement letters
- **compliance-tracking**: KYC/AML requirements
- **legal-analytics**: Client relationship data

## Reference Files

For detailed guidance:
- `references/engagement-templates.md` - Engagement letter templates
- `references/conflict-procedures.md` - Conflict check protocols
- `references/intake-forms.md` - Intake form templates
