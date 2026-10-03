# Israeli Legal Databases Guide

## Overview
This guide covers the primary legal databases and resources available for
Israeli legal research, including both paid and free options.

## Paid Databases

### Nevo (nevo.co.il)
- **Publisher:** Nevo Publishing Ltd.
- **Coverage:** Comprehensive: legislation, case law, legal articles, secondary sources
- **Strengths:**
  - Most comprehensive Israeli legal database
  - Full text of all Knesset legislation (current and historical versions)
  - Supreme Court, District Court, and specialized court rulings
  - Legal articles and commentary
  - Advanced search with Hebrew morphological analysis
  - Cross-references between legislation and case law
- **Access:** Subscription required (monthly/annual)
- **URL:** https://www.nevo.co.il
- **API:** No public API available
- **Tips for researchers:**
  - Use the "consolidated version" (nusach meshulav) for current law text
  - Check amendment history (tikunim) for recent changes
  - Use the "related rulings" feature to find relevant case law

### Takdin (takdin.co.il)
- **Publisher:** Takdin Legal Database Ltd.
- **Coverage:** Legislation, case law, legal forms
- **Strengths:**
  - Strong case law collection
  - Recently adding AI-powered search features
  - Legal forms and templates
  - Lower cost than Nevo for individual practitioners
- **Access:** Subscription required
- **URL:** https://www.takdin.co.il
- **API:** No public API available
- **Tips for researchers:**
  - Good alternative when Nevo is unavailable
  - Form templates useful for document preparation
  - AI search can surface relevant precedents quickly

### Psakdin (psakdin.co.il)
- **Publisher:** Psakdin Ltd.
- **Coverage:** Court rulings focus
- **Strengths:**
  - Specialized in court rulings
  - Good coverage of lower court decisions
  - Summary and analysis of significant rulings
- **Access:** Subscription required
- **URL:** https://www.psakdin.co.il

## Free Resources

### Knesset Legislation Portal
- **Publisher:** The Knesset (Israeli Parliament)
- **Coverage:** All primary legislation passed by the Knesset
- **Strengths:**
  - Free access to all legislation text
  - Official source for law text
  - Legislative history and committee discussions
  - Bills (hatzaot chok) tracking
- **Limitations:**
  - May not always have the most recent consolidated version
  - Search functionality is basic
  - No case law
- **URL:** https://main.knesset.gov.il/Activity/Legislation/
- **Tips:**
  - Use for verifying official law text
  - Check Reshumot (official gazette) for publication dates
  - Committee protocols provide legislative intent context

### Court Rulings Portal (supreme.court.gov.il)
- **Publisher:** Israeli Courts Administration
- **Coverage:** Selected court rulings
- **Strengths:**
  - Free access to published court rulings
  - Includes Supreme Court (Elyon), District, and some Magistrate rulings
  - Recent rulings published quickly
- **Limitations:**
  - Not all rulings are published
  - Search is limited compared to commercial databases
  - Historical coverage is incomplete
  - The site enforces an aggressive WAF that blocks foreign IPs and many user agents; access from an Israeli network or via a real browser session is most reliable
- **URLs:**
  - Supreme Court portal: https://supreme.court.gov.il/ (the deep `/sites/he/Pages/home.aspx` path was retired; use the domain root, then navigate to verdicts search. WAF-blocked to bots, opens in a real browser)
  - Judicial Authority landing: https://www.gov.il/he/departments/the_judicial_authority/govil-landing-page
  - Court fees reference: https://www.gov.il/he/pages/fees_16
- **Tips:**
  - Supreme Court (Bagatz and civil/criminal appeals) best covered
  - Use case number format: XX/XXXXX (year/number)
  - High Court of Justice petitions use format: Bagatz XXXX/XX

### Kol Zchut (kolzchut.org.il)
- **Publisher:** Kol Zchut (All Rights) non-profit
- **Coverage:** Legal rights information wiki
- **Strengths:**
  - Free, comprehensive rights information
  - Written in accessible Hebrew (not legalese)
  - Covers employment, housing, health, social security, consumer rights
  - Available in Hebrew, Arabic, English, Russian, Amharic
  - Content under Creative Commons license
  - Regularly updated
- **Limitations:**
  - Not a primary legal source
  - Simplified explanations may miss nuances
  - Not suitable for advanced legal research
- **URL:** https://www.kolzchut.org.il
- **Tips:**
  - Excellent starting point for understanding rights
  - Each article links to relevant legislation
  - Good for client-facing explanations

### National Insurance Institute (btl.gov.il)
- **Publisher:** Bituach Leumi (National Insurance Institute)
- **Coverage:** Social security rights and benefits
- **Strengths:**
  - Official information on all NII benefits
  - Calculators for benefit amounts
  - Application forms and procedures
- **URL:** https://www.btl.gov.il

## Research Methodology

### Step 1: Identify the Legal Area
Determine which area of law is relevant (contract, employment, tort, etc.)

### Step 2: Find Primary Legislation
Use Knesset portal or Nevo to locate the relevant chok or pkuda

### Step 3: Check Current Version
Verify you have the consolidated version including all amendments (tikunim)

### Step 4: Find Relevant Case Law
Search for Supreme Court interpretations of the relevant sections

### Step 5: Check Secondary Sources
Look for legal articles and commentary explaining the law

### Step 6: Verify Currency
Confirm no recent amendments or pending legislation changes

## Citation Format
Israeli legal citations typically follow this format:
- **Legislation:** Chok [Name], Tashla"a-[Year], Sefer HaChukim [number], amud [page]
- **Court ruling:** [Court type] [case number] [Party 1] neged [Party 2]
- **Example:** Baga"tz 5100/94 HaVaad HaTziburi Neged Inuyim BeYisrael neged Medinat Yisrael (Public Committee Against Torture v. State of Israel). Always copy the exact docket number and party names from a verified source; never reconstruct them from memory.
