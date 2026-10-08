---
name: prompt-pack-content-license-agreement-sboghossian
title: Content License Agreement
description: Use when a licensor needs to grant rights to use content (images, video, articles, music, software, brand assets) to a licensee for defined purposes. Produces a structured Content License Agreement covering scope, exclusivity, permitted uses, restrictions, attribution, fees, and takedown obligations. Relevant across MENA (UAE, KSA, LB, EG), DIFC/ADGM, EU (GDPR and DSA), and UK; addresses how copyright treatment differs between civil-law MENA systems and common-law DIFC/ADGM/UK frameworks.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/prompt-pack/prompt-pack-content-license-agreement
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: contracts
language: en
---

# Content License Agreement

A content license grants a licensee the right to use specified content without transferring ownership. The agreement's commercial value depends entirely on how precisely the license scope, restrictions, and term are defined — vague grants lead to infringement disputes; overly narrow grants mean the licensee cannot use the content for its intended purpose.

## When to use this

- A photographer, artist, or media company is licensing images, video, or editorial content to a commercial publisher or advertiser.
- A company is licensing its brand assets (logo, imagery, marketing materials) to a distributor, franchisee, or JV partner.
- A news agency, music label, or content platform is licensing content to a streaming service or re-distributor.
- A software company is licensing proprietary datasets, training data, or documentation to a third party.
- A digital media company is acquiring rights to user-generated content for commercial use.

## Required inputs

| Input | Why it matters | Sensible default |
|---|---|---|
| Licensor and licensee identification | Both parties' full legal names and jurisdictions | Ask the user |
| Description of the content | The more precise, the better; include format, quantity, catalogue reference | Ask the user |
| Permitted use | What the licensee may do with the content | Ask the user — this is the commercial heart of the deal |
| Territory | Where the license applies — critical for IP registrations | Ask the user; default to the countries of the licensee's operation |
| Exclusivity | Exclusive or non-exclusive? | Ask the user; default to non-exclusive |
| License fee and royalty structure | Fixed fee, per-use, revenue share, or royalty | Ask the user |
| Term | Duration of the license | Ask the user |

## Optional inputs

- Attribution / credit requirements (many content creators require "Photo by X" or equivalent).
- Sublicensing rights (can the licensee further license the content?).
- Platforms and channels permitted (print, digital, social media, out-of-home).
- Moral rights waiver (relevant in civil-law systems where moral rights are inalienable).
- Whether AI training use is permitted or prohibited (emerging issue globally).
- Takedown and audit rights.

## Document structure

### 1. Parties and recitals
- Full legal names, jurisdiction of incorporation, registered addresses.
- Brief recital identifying the content, the commercial relationship, and the parties' intent.

### 2. Grant of license
The single most important clause. Must specify:
- **What is licensed:** precise description of the content (by title, catalogue number, file list, or attached Schedule).
- **What rights are granted:** reproduce, display, distribute, modify, create derivative works — list each right expressly; do not use catch-all language.
- **Exclusivity:** if exclusive, state this expressly and the geographic or use-specific scope of exclusivity.
- **Territory:** list countries or regions; "worldwide" is acceptable if intended.
- **Term:** start date and end date (or rolling with renewal rights).
- **Sublicensing:** whether the licensee may sublicense and, if so, subject to what conditions.

### 3. Permitted uses and restrictions

State affirmatively what the licensee may do:
- Use in [specific media / channels / platforms].
- Reproduce up to [X copies / impressions].
- Modify in [specified ways] or prohibit modification entirely.

State expressly what the licensee may NOT do:
- Use outside the defined territory.
- Use for purposes other than those stated.
- Remove copyright or attribution notices.
- Sublicense without prior written consent.
- Use the content in connection with illegal, defamatory, or harmful material.
- Use for AI model training (include if relevant and desired).

### 4. Attribution and credit
- Required credit line (e.g., "© [Licensor Name] [Year]. All rights reserved.").
- Placement and size requirements.
- Consequences of failure to credit (breach of license; obligation to remedy within [X] days of notice).

### 5. License fees and royalties
- Fixed upfront fee (if applicable), payment timing, currency.
- Royalty rate (if applicable): % of net revenue, per-unit royalty, minimum guarantee.
- Audit rights: licensee must keep records of usage and revenue; licensor may audit once per year on [X] days' notice.
- Late payment interest: specify rate (e.g., central bank rate + 2%).

### 6. Moral rights (civil-law jurisdictions)
In most civil-law jurisdictions (UAE, LB, EG, FR), authors have inalienable moral rights (right of integrity, right of paternity) that cannot be waived. The practical effect:
- The licensee may not modify the content in a manner that distorts or mutilates the work in a way that prejudices the author's honor or reputation.
- Attribution (right of paternity) cannot be waived by contract in these jurisdictions — include the attribution clause as a compliance measure.
- **UAE Copyright Law (Federal Law No. 38 of 2021):** recognizes both economic rights (licensable) and moral rights (not licensable).
- **DIFC / ADGM / UK:** more flexible; moral rights can be waived by the author in writing.

### 7. Representations and warranties
**Licensor warrants:**
- It owns or controls the rights licensed.
- The content does not infringe third-party IP.
- The content does not defame any person or violate applicable law.
- No consent of any third party is required that has not been obtained (including model releases, property releases, music sync rights if applicable).

**Licensee warrants:**
- It will use the content only for the permitted purposes.
- It will not do anything to harm the licensor's reputation or IP.

### 8. Infringement and takedown
- The licensee must notify the licensor immediately of any actual or suspected infringement of the licensed content.
- The licensor retains the right (but not the obligation) to pursue infringers.
- The licensee must cooperate with takedown requests from the licensor, including platform takedowns under DMCA (US), DSA (EU), and equivalent MENA regimes.
- If the licensee becomes aware of a platform hosting the content without authorization, it must notify the licensor within [X] days.

### 9. Indemnification
- Licensor indemnifies licensee against third-party claims arising from the content (IP infringement, defamation) provided the licensee has used the content strictly within the permitted scope.
- Licensee indemnifies licensor against claims arising from the licensee's unauthorized use or modification of the content.

### 10. Term and termination
- Automatic termination on expiry of the term.
- Termination for cause: material breach (including unauthorized use) if not cured within [15–30] days of written notice.
- Termination for insolvency of either party.
- Effect of termination: licensee must cease use of the content, destroy all copies, and certify destruction in writing within [30] days.

### 11. General provisions
- Governing law and jurisdiction / arbitration.
- No implied licenses — all rights not expressly granted are reserved.
- Entire agreement; amendments in writing only.

## Jurisdictional notes

| Jurisdiction | Copyright framework | Key issue |
|---|---|---|
| UAE (onshore) | Federal Law No. 38 of 2021 | Moral rights inalienable; Arabic language version required for court proceedings; copyright registration with Ministry of Culture strengthens enforcement |
| UAE (DIFC) | DIFC IP Law No. 4 of 2019 (based on English copyright law) | Moral rights waivable; strong enforcement through DIFC Courts |
| KSA | Royal Decree No. M/41 of 1424H (Copyright Law) | Arabic registration recommended; enforcement through Ministry of Media |
| Lebanon | Law No. 75 of 1999 (IP Law) | Moral rights inalienable; Lebanese courts can award injunctions; enforcement variable |
| Egypt | Law No. 82 of 2002 (IP Law) | Moral rights recognized; Copyright Office registration available |
| EU / UK | GDPR data protection overlay for content featuring individuals; DSA content moderation obligations for platforms | GDPR consent required if content features identifiable persons; UK CDPA 1988 governs copyright |

## Common mistakes

- License scope is too vague ("use the content as needed") — this is unenforceable and will lead to disputes about what was actually licensed.
- Omitting platform-specific restrictions (social media, OOH, broadcast) — each channel has different commercial value and rate.
- Not addressing model releases or property releases for photographic content — the licensor should warrant these are in place.
- Ignoring AI training use — as of 2026 this is a live dispute in content licensing; state the position expressly.
- Failing to include a takedown mechanism — if unlicensed distribution occurs, the licensor needs a fast contractual pathway to require removal.

## Related skills

- [[prompt-pack-ip-assignment-agreement]]
- [[prompt-pack-nda-mutual]]
- [[prompt-pack-consulting-agreement]]
- [[prompt-pack-software-license-agreement]]
- [[prompt-pack-data-processing-agreement]]
