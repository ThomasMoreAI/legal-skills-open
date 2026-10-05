---
name: israeli-ecommerce-compliance-skills-il
title: Israeli E-Commerce Compliance
description: Audit and ensure Israeli e-commerce legal compliance, covering Consumer Protection Law, return policies, price display, accessibility, and cookie consent. Use when user asks about "online store compliance Israel", "Chok Hagnat HaTzarchan", "consumer protection Israel", "return policy Israel", "IS 5568 ecommerce", "cookie consent Israel", or "חוק הגנת הצרכן". Covers cooling-off period validation, price display requirements, Hebrew terms of service generation, accessibility compliance (IS 5568), and business disclosure verification. Do NOT use for food-specific compliance (use israeli-food-business-compliance) or privacy/GDPR (use israeli-privacy-shield).
author: skills-il
author_url: https://github.com/skills-il/security-compliance/tree/master/israeli-ecommerce-compliance
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: consumer
language: en
sources:
- title: Consumer Protection Law
  path: references/consumer-protection-law.md
---

# Israeli E-Commerce Compliance

## Legal notice

This is a free information tool operated by an AI model. It explains the law and the procedure and helps you organise your own documents. All of its outputs are produced automatically by an AI model, with no involvement, review, or approval by an advocate. The output is not legal advice and not a legal opinion, but a general explanation and a template only: it does not read the full file of your matter, does not check current case law, and does not examine your specific circumstances. An AI model may err, omit data, or present a wrong conclusion.

Any text this tool drafts is an automatic draft for your personal preparation only. It is not a document prepared by an advocate and must not be relied on as evidence. This tool is not a substitute for advice that takes account of the particular circumstances and needs of each person. Before starting proceedings, signing a document, or filing with an authority or a court, consult an advocate. All use of its output is the user's sole responsibility.


## Instructions

> **Note:** This skill provides compliance guidance. It does not replace legal counsel. Recommend consulting a consumer protection attorney (orech din specializing in mishpat tzarchani) for specific compliance decisions.

### Step 1: Scan for Consumer Protection Law Compliance (Chok Hagnat HaTzarchan)
Verify 14-day cooling-off period for distance selling (mecher merachok):
- Right to cancel within 14 days of receiving the product, OR 14 days from receipt of the disclosure document, whichever is later
- Extended to 4 months for people with disabilities, seniors (65+), and new immigrants (under 5 years in Israel), but ONLY when there was a prior conversation between the business and the consumer (phone call, chat, or other electronic communication) before the transaction (per Tikun 47, 2016, codified in Sec. 14ג1). Pure web-store purchases with no conversation get only the standard 14-day window for these groups.
- Cancellation fee: up to 5% of transaction or 100 NIS, whichever is lower
- Return shipping: at buyer's expense unless item is defective

Check for required pre-purchase disclosures:
- Full product/service description
- Total price including all fees and taxes
- Delivery timeline and costs
- Cancellation and return policy
- Seller's full details (see Step 5)

### Step 2: Validate Price Display Requirements
- All prices MUST include VAT (18%), Israeli law requires consumer-facing prices to be inclusive
- Delivery/shipping costs must be clearly stated before checkout
- Total order cost (including all fees) must be shown before payment confirmation
- Currency must be NIS (display as ₪ or ש"ח)
- Discounted items ("מבצע"): BOTH the pre-sale price and the sale price must be shown together (not "מחיר מומלץ" / list price as the comparison). If the pre-sale price was not actually in effect for at least 21 consecutive days before the sale started, the announcement must state the period during which that price was in effect. Per the Consumer Protection (Credit Sales, Special Sale and Door-to-Door Transaction) Regulations, 1983, reg. 6.
- "From" pricing (e.g., "from X shekels") only allowed when the base price actually exists
- VAT-exempt threshold for personal imports has been volatile in 2025-2026: the standing exemption is USD 75 and a ministerial move to double it to USD 150 was announced, with later reversals reported. Do not state a figure without checking the current one at gov.il / Israel Tax Authority.

**Card payment compliance (PCI DSS 4.0.1).** The current standard is PCI DSS v4.0.1 (released June 2024). PCI DSS v3.2.1 was retired on 31 March 2024, and the 51 future-dated v4.x requirements (stricter authentication, continuous monitoring, customized approach) became mandatory on 31 March 2025. Any store that processes, stores, or transmits card data must comply with v4.0.1. Most Israeli stores rely on a tokenized payment gateway (Tranzila, Cardcom, iCredit, Stripe, etc.) to offload PCI scope, which is strongly recommended for merchants under SAQ A/SAQ A-EP eligibility.

### Step 3: Generate Hebrew Terms of Service and Return Policy
Generate compliant Hebrew Terms of Service (תנאי שימוש) including:
- Company details (name, registration number, address, contact)
- Product/service descriptions
- Payment terms and accepted methods
- Delivery policy and timeframes
- Return and cancellation policy per Consumer Protection Law
- Warranty terms (if applicable)
- Dispute resolution mechanism

Generate Return Policy (מדיניות החזרות) per legal requirements:
- 14-day cancellation right clearly stated
- Process for requesting cancellation
- Refund timeline (up to 14 days from cancellation notice)
- Exceptions to cancellation right (perishables, custom items, digital content after download)

### Step 4: Check Accessibility Compliance (IS 5568 / Amendment 36)
Israeli websites must comply with IS 5568 accessibility standard (based on WCAG 2.1 AA).
Use browser automation to scan for:
- Alt text on images
- Keyboard navigation support
- Screen reader compatibility
- Color contrast ratios (4.5:1 minimum for normal text)
- Form labels and error messages
- Language declaration (Hebrew RTL)
- Accessibility statement page

Amendment 36 to the Equal Rights for People with Disabilities Law applies to all businesses providing public services online and government services. Revenue thresholds:
- Businesses with annual revenue below NIS 100,000 are exempt
- Businesses with annual revenue above NIS 300,000 must comply immediately
- Businesses in between have a graduated compliance timeline

### Step 5: Verify Business Disclosure (Osek Number, Address, Contact)
Israeli e-commerce sites must prominently display:
- Business name (as registered with Registrar of Companies)
- Registration number (osek murshe number or company number)
- Physical address (not just PO Box)
- Phone number
- Email address
- Full name of business owner or authorized contact

These must appear on the website (typically in footer or "About Us").
Must also appear on every invoice/receipt.

**E-Invoicing Reform (Allocation Numbers):**
Starting January 2025, electronic invoices for B2B transactions above NIS 20,000 must include an allocation number (mispar haktza'a) from the Tax Authority. The threshold drops to NIS 10,000 in January 2026, and NIS 5,000 in June 2026. Ensure your invoicing system supports Israel Tax Authority API integration for allocation number requests.

### Step 6: Validate Cookie Consent and Privacy Compliance
Following Privacy Protection Law Amendment 13 (in force August 14, 2025) and the 2025 PPA Guidelines on Informed Consent, the PPA treats opt-in consent for non-essential cookies as the expected standard. Israel has no cookie-specific statute like the EU ePrivacy Directive; the obligation flows from the general consent requirement in the Privacy Protection Law plus PPA guidance. A 2025 German ruling (Verwaltungsgericht Hannover) requiring an equally visible "Reject All" button alongside "Accept All" is persuasive best practice internationally but is NOT binding Israeli precedent. Implement an equally prominent "Reject All" button as best practice.
- Cookie consent banner for non-essential cookies, with equally prominent "Accept All" and "Reject All" buttons
- Clear description of cookie types and purposes
- Opt-in for marketing/analytics cookies (not opt-out, not pre-checked)
- Easy way to withdraw consent (linked from every page)
- Privacy policy linking to cookie details

Essential cookies (login, shopping cart) don't require consent.
Analytics and marketing cookies require explicit opt-in.

**Section 30A (Anti-Spam Law).** Section 30A of the Communications Law requires explicit prior opt-in for any SMS, email, fax, or robocall advertisement sent to consumers. Statutory damages up to NIS 1,000 per message, no proof of harm required. Email-capture forms, SMS marketing, and post-checkout marketing emails must be wired to opt-in checkboxes that are NOT pre-checked.

**Amendment 13 to the Privacy Protection Law (effective August 2025):**
This amendment significantly expands privacy obligations for online businesses:
- Expanded definition of "personal data" now includes IP addresses, geolocation, and online identifiers
- Businesses processing data at scale must appoint a privacy officer
- Mandatory data breach notification to the PPA and affected individuals
- New provisions for AI governance and automated decision-making

For comprehensive privacy compliance beyond cookies, use the `israeli-privacy-shield` skill.

## Examples

### Example 1: Full Compliance Audit for New Online Store
User says: "I'm launching an online clothing store, make sure it's compliant with Israeli law"
Actions:
1. Scan website for Consumer Protection Law compliance (return policy, cooling-off)
2. Validate price display (VAT included, delivery costs visible)
3. Check business disclosure (registration, address, contact visible)
4. Test accessibility (IS 5568 automated checks)
5. Verify cookie consent implementation
6. Generate compliance report with pass/fail per section
Result: Compliance report: 4/6 sections pass. Issues found: return policy doesn't mention extended cancellation for elderly/disabled, cookie banner uses opt-out instead of opt-in. Recommended fixes provided with Hebrew legal text.

### Example 2: Generating Compliant Return Policy
User says: "I need a return policy for my electronics store that's legal in Israel"
Actions:
1. Determine product categories (electronics, standard 14-day applies)
2. Draft Hebrew return policy per Consumer Protection Law
3. Include all mandatory clauses: 14-day cooling-off, extended periods, exceptions
4. Include cancellation fee disclosure (up to 5% or 100 NIS)
5. Add refund timeline commitment (14 days)
Result: Complete Hebrew return policy (מדיניות החזרות) ready to publish. Includes all legally required clauses, clear customer-facing language, and specific exceptions for electronics (e.g., opened software).

### Example 3: Accessibility Audit for Existing Store
User says: "We got a complaint about our website's accessibility, can you check it?"
Actions:
1. Determine if business falls under IS 5568 requirements (revenue-based thresholds and public service obligation)
2. Run automated accessibility scan using browser automation
3. Check: alt text, keyboard nav, contrast ratios, form labels, RTL support
4. Identify: 12 images missing alt text, 3 forms without labels, contrast below 4.5:1 on 2 pages
5. Generate prioritized fix list with effort estimates
Result: Accessibility report: 15 issues found (8 critical, 7 moderate). Critical issues: missing form labels (checkout page), insufficient contrast on CTA buttons. Fix guide provided with HTML/CSS corrections.

## Bundled Resources

### References
- `references/consumer-protection-law.md`, Summary of Israeli Consumer Protection Law requirements for e-commerce: distance selling rules, cooling-off periods (standard and extended), cancellation fees, price display requirements, required disclosures, and exceptions. Consult when auditing compliance in Steps 1-2 or generating legal documents in Step 3.

## Gotchas

- The Israeli 14-day cooling-off period for online purchases starts from the delivery date or the date the consumer received the contract terms, whichever is later. Agents may incorrectly calculate it from the order date.
- Israeli law requires all prices to include 18% VAT (ma'am). Agents may generate price displays excluding tax, which is illegal for consumer-facing Israeli e-commerce.
- The extended 4-month cancellation period applies to people with disabilities, seniors (65+), and new immigrants (under 5 years in Israel). Agents may only mention the standard 14-day period.
- IS 5568 (Israeli accessibility standard) is based on WCAG 2.1 AA but has additional Hebrew RTL-specific requirements. Agents may apply generic WCAG checks without RTL-specific validations.
- Cookie consent in Israel: the PPA strongly recommends opt-in for analytics and marketing cookies, but Israel does not yet have a cookie-specific statute like the EU ePrivacy Directive. Section 30A of the Communications Law covers unsolicited advertising, not cookies directly. Agents may overstate the legal requirement or understate the best practice.
- Amendment 13 to the Privacy Protection Law (effective August 2025) expands the definition of personal data to include IP addresses and geolocation. Agents trained on older data may not account for the new privacy officer requirements or data breach notification obligations.
- E-invoicing reform (January 2025): B2B invoices above NIS 20,000 require allocation numbers from the Tax Authority. Agents may generate invoices without allocation numbers, which is non-compliant for qualifying transactions.

## Troubleshooting

### Error: "Cookie consent not compliant"
Cause: Using opt-out instead of opt-in for non-essential cookies, or consent banner not appearing on all pages.
Solution: Implement opt-in consent per PPA recommendations. Although Israel lacks a cookie-specific statute, opt-in is considered best practice and aligns with the PPA's guidance. Ensure banner appears on first visit before any non-essential cookies are set. Include clear categories (essential, analytics, marketing) with individual toggle controls.

### Error: "Accessibility scan incomplete"
Cause: Dynamic content loaded via JavaScript may not be captured by automated scanning.
Solution: Ensure scan waits for full page load including lazy-loaded content. Run additional manual checks for JavaScript-heavy pages. Focus on checkout flow and forms, these are highest-priority accessibility targets.

### Error: "Price display violation"
Cause: Prices shown without VAT or delivery costs hidden until checkout.
Solution: All consumer-facing prices must include 18% VAT. Delivery costs must be shown before the payment confirmation step. Use clear format: "₪X.XX (כולל מע"מ)" for all prices. Ensure cart total includes delivery before asking for payment details.

### Error: "Business disclosure missing"
Cause: Required business details not visible or not on every required page.
Solution: Add business name, registration number, physical address, phone, email, and contact name to footer (appears on all pages). Also verify these appear on order confirmations and invoices. Israeli Consumer Protection Law specifically requires these for distance selling.
