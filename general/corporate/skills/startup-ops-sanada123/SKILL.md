---
name: startup-ops-sanada123
title: Startup Ops
description: 'The non-code stuff that kills startups. Company registration, contracts (NDA, SOW, freelancer), accounting basics, tax calendars, legal entity selection, IP protection, insurance, compliance (GDPR, Israeli privacy law), domain/trademark basics, and vendor management. Covers Israel, US, and UAE jurisdictions. Use when discussing legal setup, contracts, accounting, compliance, insurance, IP, trademarks, or any operational/legal founder question. Triggers on: "register company", "NDA", "contract", "accountant", "legal", "GDPR", "privacy policy", "trademark", "insurance", "עוסק מורשה", "חברה בע"מ", "LLC", "free zone", הקמת חברה, חוזה, עורך דין.'
author: sanada123
author_url: https://github.com/sanada123/openclaw-skills/tree/main/startup-ops
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# Startup Ops

**The boring stuff that keeps you out of trouble.**

Nobody starts a company to write NDAs and file tax returns. But ignoring ops is how founders
end up with lawsuits, tax penalties, and IP disputes. This skill covers the minimum viable
operations — what you actually need, when you need it, and what can wait.

## Core Philosophy

```
DONE > PERFECT.     A basic contract signed beats a perfect one "in progress."
EARLY > LATE.       Fix legal/tax issues when they're cheap, not when they're lawsuits.
SIMPLE > COMPLEX.   Start as sole proprietor. Incorporate when you need to.
PROFESSIONAL HELP.  This is guidance, not legal advice. Get a lawyer for anything serious.
```

**⚠️ Disclaimer:** This skill provides general operational guidance. It is NOT legal advice,
tax advice, or a substitute for licensed professionals. Laws vary by jurisdiction and change
frequently. Always consult a lawyer/accountant for your specific situation.

---

## When to Activate

- Registering a business entity
- Drafting or reviewing contracts
- Setting up basic accounting
- Compliance questions (GDPR, privacy)
- IP/trademark protection
- Insurance decisions
- Vendor/contractor management

---

## 1. Company Registration — When & What

### Decision Tree

```
Just you, no employees, testing an idea?
  → Sole proprietor / עוסק פטור / Freelancer
  
Revenue > $10K/mo OR taking investment OR hiring?
  → LLC / חברה בע"מ / Free Zone company
  
Multiple co-founders?
  → MUST incorporate. Get a founders' agreement BEFORE writing code.
```

### Israel

| Entity | When | Cost | Complexity |
|--------|------|------|-----------|
| **עוסק פטור** | Revenue < ₪120K/yr, testing idea | Free to register | Minimal — annual report only |
| **עוסק מורשה** | Revenue > ₪120K/yr, need VAT invoices | Free to register | Monthly/bi-monthly VAT reports |
| **חברה בע"מ** | Investment, multiple founders, liability protection | ~₪2,500-5,000 setup | Annual reports, board minutes, accountant required |

**Registration steps (עוסק):**
```
1. Open תיק במס הכנסה (tax file) — online at misim.gov.il
2. Register at מע"מ (VAT authority) — choose פטור or מורשה
3. Register at ביטוח לאומי (National Insurance) — automatic with tax file
4. Open business bank account — bring registration certificate
5. Get חשבוניות (invoices) — use Greeninvoice or similar service
```

**Registration steps (חברה בע"מ):**
```
1. Choose company name — check availability at justice.gov.il
2. Draft תקנון (articles of association)
3. File with רשם החברות (Companies Registrar) — online
4. Get company number (ח.פ.)
5. Register at tax authority, VAT, national insurance
6. Open corporate bank account
7. Appoint accountant
8. If co-founders: sign founders' agreement (שלב הכי חשוב!)
```

### United States

| Entity | When | Cost | Complexity |
|--------|------|------|-----------|
| **Sole proprietor** | Just starting, US-based | Free (some states require registration) | Schedule C on personal taxes |
| **LLC** | Want liability protection | $50-500 (varies by state) | Annual filing, operating agreement |
| **C-Corp (Delaware)** | Taking VC investment | ~$1,000-2,000 setup | Most complex. Required for VC. |
| **S-Corp** | Profitable LLC wanting tax savings | LLC + S-Corp election | Payroll required |

**Best state for registration:**
- Operating locally → your home state
- VC-backed startup → Delaware (C-Corp)
- Online business, no physical presence → Wyoming or Delaware (LLC)

### UAE

| Entity | When | Cost | Complexity |
|--------|------|------|-----------|
| **Free Zone LLC** | Foreign founder, no local partner needed | AED 10,000-50,000/yr | 100% ownership, tax benefits |
| **Mainland LLC** | Need to sell to UAE government or locally | AED 15,000-30,000 + local sponsor fee | Requires UAE national partner or service agent |
| **Freelance permit** | Solo consultant | AED 7,500-15,000/yr | Simplest, limited to services |

**Popular free zones:**
- DMCC (Dubai) — commodities, trading, crypto
- DIFC (Dubai) — fintech, financial services
- ADGM (Abu Dhabi) — financial services, tech
- IFZA (Fujairah) — cheapest, general purpose
- Dubai Silicon Oasis — tech startups

---

## 2. Essential Contracts

### NDA (Non-Disclosure Agreement)

**When you need it:**
- Before sharing your idea with potential partners/investors
- Before hiring contractors who'll see proprietary code
- Before discussing acquisition/partnership

**Key clauses:**
```
1. Definition of Confidential Information (be specific)
2. Duration (2-3 years is standard)
3. Exclusions (publicly known info, independently developed)
4. Permitted disclosures (legal requirements, employees who need to know)
5. Remedies for breach
6. Governing law and jurisdiction
```

**When you DON'T need it:**
- Talking to VCs (they won't sign, and you shouldn't ask)
- General networking
- Discussing publicly available information

### Freelancer/Contractor Agreement

**Must include:**
```
1. Scope of work (detailed — what exactly they'll deliver)
2. Timeline and milestones
3. Payment terms (amount, schedule, method)
4. IP assignment (CRITICAL — all work product belongs to you)
5. Confidentiality clause
6. Non-compete (reasonable: 6-12 months, same industry)
7. Termination clause (how either party can exit)
8. Warranty (contractor warrants original work, no infringement)
```

**The IP trap:** Without explicit IP assignment, the contractor may legally own what they built for you. ALWAYS include IP assignment clause.

### Client SOW (Statement of Work)

```
1. Project description (what you'll build/deliver)
2. Deliverables (specific, measurable outputs)
3. Timeline (with milestones)
4. Pricing (fixed or T&M with cap)
5. Payment schedule (50% upfront, 50% on delivery — or milestones)
6. Change request process (how scope changes are handled + priced)
7. Acceptance criteria (what "done" means)
8. Warranty period (30-90 days of bug fixes)
9. Limitation of liability
10. Termination (kill fee if they cancel mid-project)
```

### Founders' Agreement

**If you have a co-founder and no agreement — STOP EVERYTHING AND DO THIS FIRST.**

```
Must cover:
1. Equity split (and rationale)
2. Vesting schedule (4 years, 1-year cliff is standard)
3. Roles and responsibilities (who does what)
4. Decision-making (tie-breaking mechanism)
5. IP assignment (everything built → company)
6. Full-time commitment (or not — be explicit)
7. What happens if someone leaves (vesting, buyback)
8. What happens if you disagree (mediation → arbitration)
9. Non-compete during and after
10. Expenses and salary policy
```

---

## 3. Accounting Basics

### The Minimum System

```
Level 1: Spreadsheet (revenue < $5K/mo)
  - Google Sheet with: Date, Description, Amount, Category (income/expense)
  - Reconcile with bank statement monthly
  - Save all receipts (photo + cloud folder)

Level 2: Accounting software (revenue $5K-50K/mo)
  - Wave (free), QuickBooks ($15/mo), Xero ($15/mo)
  - Connect bank account for auto-import
  - Monthly reconciliation
  - Quarterly P&L review

Level 3: Professional accountant ($50K+/mo or complex structure)
  - Hire a bookkeeper ($200-500/mo)
  - Accountant for tax filing + strategy
  - Monthly financial reports
```

### Financial Statements You Need

| Report | What It Shows | When |
|--------|-------------|------|
| **P&L (Profit & Loss)** | Revenue - Expenses = Profit | Monthly |
| **Cash Flow** | Money in vs money out | Weekly |
| **Balance Sheet** | What you own vs what you owe | Quarterly |
| **Tax Summary** | What you owe the government | Quarterly |

### Receipt Management

```
Rule: If you spent business money, you need a receipt.

System:
1. Take photo of receipt immediately (phone camera)
2. Forward to dedicated email (receipts@yourdomain.com) or folder
3. Categorize: hosting, travel, food, software, contractor, etc.
4. At month-end: reconcile with bank statement

Tools: Dext, Expensify, or just a Google Drive folder with subfolders by month
```

---

## 4. Compliance Basics

### GDPR (EU — Required if You Have EU Users)

**Core requirements:**
```
1. Privacy policy on your website (what you collect, why, how long)
2. Cookie consent banner (active opt-in, not pre-checked)
3. Right to deletion (users can request data removal)
4. Data processing agreement with vendors (Stripe, analytics, etc.)
5. Breach notification (72 hours to report to authority)
6. Data minimization (collect only what you need)
```

**Minimum viable privacy policy must state:**
- What data you collect
- Why you collect it
- How long you keep it
- Who you share it with
- How to contact you for deletion requests
- Your legal basis for processing

### Israeli Privacy Law (חוק הגנת הפרטיות)

```
1. Register database with ILITA if > 10,000 records
2. Privacy policy required (similar to GDPR)
3. Email marketing: explicit opt-in required (חוק הספאם)
4. Data security: reasonable measures required
5. Cross-border transfer: adequate protection required
```

### CAN-SPAM (US Email)

```
1. Don't use deceptive headers or subject lines
2. Identify message as ad (if applicable)
3. Include physical address
4. Include unsubscribe mechanism
5. Honor opt-outs within 10 business days
```

---

## 5. IP Protection

### What to Protect First

| Asset | Protection | Cost | Priority |
|-------|-----------|------|----------|
| **Brand name** | Trademark | $250-1,500 per class per country | 🔴 Do early |
| **Domain** | Buy it | $10-50/yr | 🔴 Do first day |
| **Code** | Copyright (automatic) + IP assignment clauses | Free (assignment = contract clause) | 🔴 Critical |
| **Trade secrets** | NDAs + access controls | Free (legal cost for NDA) | 🟡 When you have employees |
| **Inventions** | Patent | $5,000-15,000+ | 🟢 Only if genuinely novel |

### Trademark Basics

```
1. Search existing trademarks BEFORE choosing a name
   - US: USPTO (trademark.gov)
   - Israel: ILPO (ilpo.gov.il)
   - International: WIPO Global Brand Database

2. Register in your primary market first
   - Class 9 (software), Class 42 (SaaS/tech services) most common for tech

3. Use ™ immediately (no registration needed)
   Use ® only after approved registration
```

---

## 6. Insurance

### What Founders Actually Need

| Insurance | When | Why | Cost |
|-----------|------|-----|------|
| **Professional liability (E&O)** | Client-facing services | Covers mistakes/negligence claims | $500-2,000/yr |
| **Cyber liability** | Handling customer data | Covers data breaches | $500-1,500/yr |
| **General liability** | Physical office/events | Covers physical injury/property damage | $300-1,000/yr |
| **D&O** | Have a board/investors | Covers director/officer decisions | $1,000-5,000/yr |
| **Health insurance** | Always | You're useless if you're sick | Varies |

**Minimum for solo SaaS founder:** Professional liability + cyber liability. ~$1,000-3,000/yr total.

---

## 7. Vendor & Contractor Management

### Before Signing Any Vendor

```
Checklist:
- [ ] What's the cancellation policy? (avoid annual lock-in)
- [ ] Where is data stored? (relevant for GDPR)
- [ ] What happens to my data if I leave?
- [ ] Is there an SLA? (uptime guarantee)
- [ ] What's the pricing after the promo period?
- [ ] Do they have SOC 2 / ISO 27001? (for enterprise sales later)
```

### Contractor vs Employee

| Factor | Contractor | Employee |
|--------|-----------|----------|
| **Cost** | Higher hourly, no benefits | Lower hourly, + benefits + tax |
| **Control** | What, not how | What AND how |
| **Commitment** | Project-based | Ongoing |
| **IP** | Need explicit assignment | Usually automatic (check local law) |
| **Tax** | They handle their own | You handle withholding |
| **Risk** | Misclassification penalties | Employment law obligations |

---

## Output Standards

When giving ops/legal guidance:
- **Disclaim always**: "This is general guidance, not legal advice"
- **Jurisdiction-aware**: Always ask which country first
- **Action-oriented**: "Register at misim.gov.il" not "consider registering"
- **Priority-ordered**: What to do first, second, third
- **Cost-transparent**: Include expected costs where possible
- **Refer out**: Complex legal → "get a lawyer." Complex tax → "get an accountant."

---

*Because the #2 reason startups die (after running out of money) is legal/operational problems they could have prevented.*

**Contributing:** Lawyers, accountants, founders who survived legal nightmares — your war stories are welcome.
Open an issue or PR at [github.com/sanada123/openclaw-skills](https://github.com/sanada123/openclaw-skills).
