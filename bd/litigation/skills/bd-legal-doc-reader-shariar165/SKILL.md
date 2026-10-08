---
name: bd-legal-doc-reader-shariar165
title: Bangladesh Legal Document Reader & Explainer
description: 'Use this skill whenever a user uploads or describes a Bangladeshi legal document and wants it read or explained. Triggers: "explain this document", "what does this say", "land document", "court summons", "property deed", "mutation", "porcha", "khatian", "baina", "heba", "nikah", "talaq", "NID", "birth certificate", "trade license", "court order", "judgment", "warrant", "legal notice", "contract", "চুক্তিপত্র", "দলিল", "পরচা", "নামজারি", "খতিয়ান", "সমন", "রায়", "বায়না", "হেবা", "তালাক", "কাবিন", "ওয়ারিশান", "আমমোক্তার", or any request to read a Bangladeshi official, legal, land, or government document — scanned, photographed, or described. Always trigger even for "I got this paper from court, what does it mean?"'
author: shariar165
author_url: https://github.com/shariar165/Project--Anchor/tree/main/skills/src/bd-legal-doc-reader
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: bd
practice: litigation
language: en
sources:
- title: Contracts Agreements
  path: references/contracts-agreements.md
- title: Court Documents
  path: references/court-documents.md
- title: Govt Id Documents
  path: references/govt-id-documents.md
- title: Land Property
  path: references/land-property.md
---

# Bangladesh Legal Document Reader & Explainer

A skill for reading, extracting, and plainly explaining any Bangladeshi legal, land, court,
government, or contractual document — in either English or বাংলা, based on the user's preference.

---

## Step 0 — Language Selection

**Detect the user's language from their message.**
- If they wrote in Bangla → respond in Bangla by default
- If they wrote in English → respond in English by default
- If mixed or unclear → ask: "Should I explain this in English or বাংলা?"

Always offer to switch: "I can also explain this in [Bangla/English] if you prefer."

---

## Step 1 — Receive and Read the Document

The user may provide the document as:
- **Uploaded image** (photo, scan, screenshot) → read the visible text using OCR vision
- **Uploaded PDF** → extract and read all text
- **Pasted text** → read directly
- **Description** ("I have a court summons that says...") → work from what they describe

### When reading an image or scan:
- Read ALL visible text carefully — both printed and handwritten
- Note the document type from headers, stamps, seals, or format
- Identify language(s): Bangla, English, or mixed
- Note any official seals (আদালতের সিল), signatures (স্বাক্ষর), registration numbers (রেজিস্ট্রেশন নং), dates
- Flag any text that is unclear, torn, or illegible — note it explicitly: "[text unclear]"
- Read both printed fields AND handwritten fill-ins (names, dates, amounts, plot numbers)

### Image quality issues:
- Blurry or partial scan: read what is visible, flag missing parts
- Handwritten in Bangla cursive: do best effort, flag uncertain words
- Multiple pages: process each page in order

---

## Step 2 — Identify the Document Type

Match to one of the categories below. Read the relevant reference file.

| Document Type | Reference File |
|---|---|
| Land / Property Documents | `references/land-property.md` |
| Court Documents | `references/court-documents.md` |
| Government / ID Documents | `references/govt-id-documents.md` |
| Contracts & Agreements | `references/contracts-agreements.md` |
| Family Law Documents | `references/family-law.md` |

If the document type is unclear after reading, describe what you see and ask the user to confirm.

---

## Step 3 — Explain the Document

### Structure your explanation in this order:

#### 1. Document Type & Purpose (1–2 sentences)
State clearly what kind of document this is and what it is generally used for.

**Example (English):** "This is a **Baina Deed (বায়না দলিল)** — a preliminary sale agreement used in Bangladesh when a buyer agrees to purchase land and pays an advance amount before the final registration."

**Example (Bangla):** "এটি একটি **বায়না দলিল** — জমি বিক্রির আগে ক্রেতা-বিক্রেতার মধ্যে অগ্রিম চুক্তির দলিল।"

#### 2. Key Parties Involved
List who is who:
- বিক্রেতা / Seller / বাদী / দাতা / Plaintiff
- ক্রেতা / Buyer / বিবাদী / গ্রহীতা / Defendant
- সাক্ষী / Witnesses
- নোটারি / রেজিস্ট্রার / কর্তৃপক্ষ

#### 3. Core Details (the most important facts)
Pull out and explain the critical information:
- Dates (তারিখ) — filing date, hearing date, deadline
- Amounts (পরিমাণ) — money, land size in শতক/কাঠা/বিঘা/একর
- Plot/Daag numbers (দাগ নম্বর), Khatian numbers (খতিয়ান নম্বর)
- Location / Mouza / District / Upazila
- Case number (মামলা নং) if applicable
- Deadlines or compliance dates

#### 4. What This Document Means for the User
In plain language — what action is required, what right is being granted, what risk exists.

- **If it's a court summons:** "You are being asked to appear in court on [date]. If you do not appear, a warrant may be issued against you."
- **If it's a land deed:** "This document transfers ownership of [X শতক] land in [Mouza] from [Seller] to [Buyer] for Tk [Amount]."
- **If it's a notice:** "You are being given [X] days to [action]. If you do not comply, [consequence]."

#### 5. Important Warnings ⚠️
Flag anything the user must not ignore:
- Deadlines that are approaching or have passed
- Missing signatures or seals that may invalidate the document
- Clauses that limit the user's rights
- Amounts owed or penalties

#### 6. Recommended Next Steps
Practical advice — never legal advice:
- "Bring this document to a lawyer (আইনজীবী) for review before signing."
- "Verify the plot number at your local Land Office (ভূমি অফিস)."
- "Respond before [date] to avoid a default judgment."
- "Keep the original. This is a registered document."

---

## Writing Standards

### Plain Language Rules
- No legal jargon without explanation
- Every Bangla legal term gets an English gloss in parentheses (and vice versa)
- Use short sentences — this audience may be stressed or unfamiliar with legal language
- Never assume the user is a lawyer

### Term Glossary (always explain these inline)
| Bangla Term | Plain Explanation |
|---|---|
| দলিল | Official deed / document |
| খতিয়ান | Land ownership record (Record of Rights) |
| পরচা / পর্চা | Certified copy of land record |
| দাগ নম্বর | Plot number in land records |
| নামজারি / মিউটেশন | Transfer of land ownership in government records |
| বায়না | Advance sale agreement |
| হেবা | Gift deed (transfer without payment) |
| আমমোক্তারনামা | Power of Attorney |
| ওয়ারিশান | Inheritance / heir document |
| সমন | Court summons |
| ওয়ারেন্ট | Arrest/search warrant |
| রায় | Court judgment |
| আরজি | Plaint (case filing document) |
| নালিশ | Complaint |
| কাবিননামা | Marriage contract (Nikahnama) |
| তালাকনামা | Divorce document |
| তফসিল | Schedule / property description section of a deed |

---

## Disclaimer (always include at end)

**English:** "This explanation is for general understanding only. It is not legal advice. For any legal action, court appearance, land transaction, or contract signing, please consult a qualified lawyer (আইনজীবী) or visit your local legal aid office."

**Bangla:** "এই ব্যাখ্যা শুধুমাত্র সাধারণ বোঝার জন্য। এটি আইনি পরামর্শ নয়। আদালতে উপস্থিতি, জমি লেনদেন, বা চুক্তি স্বাক্ষরের আগে অবশ্যই একজন যোগ্য আইনজীবীর পরামর্শ নিন।"

---

## Step 4 — Offer Follow-up

After explaining, always offer:
1. **Translation** — translate the full document text (Bangla → English or vice versa)
2. **Specific question** — "Is there a specific part you want me to explain in more detail?"
3. **Summary only** — short 3-sentence version if they need to share it with someone
4. **Red flag check** — "Want me to check if anything looks suspicious or missing in this document?"
