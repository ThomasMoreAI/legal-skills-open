---
name: dmca-takedown-notice
title: DMCA Takedown Notice
description: Drafts a DMCA takedown notice compliant with 17 U.S.C. § 512(c)(3) for removing infringing content from online service providers. Enforces all six statutory elements, good faith and perjury statements, and exact infringing URL identification. Use when drafting DMCA notices, copyright takedown requests, or pre-suit infringement enforcement letters against platforms or hosts.
author: CaseMark
author_url: https://github.com/CaseMark/skills/tree/main/skills/legal/dmca-takedown-notice
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# DMCA Takedown Notice

Generates a ready-to-send 17 U.S.C. § 512(c)(3) notice compelling a service provider to remove or disable access to infringing content.

## Prerequisites

Collect before drafting:

1. **Copyrighted work** — title, type, creation/publication date, registration number (if any)
2. **Authorized source URL** — where the legitimate version lives
3. **Infringing URLs** — exact URL per distinct location (never bundle)
4. **Owner contact** — full legal name, physical address, phone, email
5. **Authority** — owner or authorized agent/attorney
6. **DMCA agent** — name, title, address from provider's Copyright Policy or the [Copyright Office directory](https://www.copyright.gov/dmca-directory/)

## Workflow

```
- [ ] Gather prerequisites above
- [ ] Screen for fair use (see Pitfalls)
- [ ] Draft notice with all required sections
- [ ] Verify statutory statements are verbatim
- [ ] Confirm client review before sending
```

## Notice Sections (in order)

### 1. Header

Formal business letter addressed to the service provider's DMCA agent with subject line: `Re: DMCA Takedown Notification Pursuant to 17 U.S.C. § 512(c)(3)`.

### 2. Identification of Copyrighted Work(s)

For each work: title, type, creation/publication date, registration number (if any), authorized source URL. List each work separately.

### 3. Identification of Infringing Material

For each instance: exact URL, platform account/username (if applicable), description of infringement (e.g., unauthorized reproduction, public display, distribution).

### 4. Statutory Statements

Include both **exactly as written** — these are non-negotiable:

> **Good faith belief** (§ 512(c)(3)(A)(v)):
> "I have a good faith belief that use of the material in the manner complained of is not authorized by the copyright owner, its agent, or the law."

> **Accuracy and authority under penalty of perjury** (§ 512(c)(3)(A)(vi)):
> "I swear, under penalty of perjury, that the information in this notification is accurate and that I am the copyright owner, or am authorized to act on behalf of the owner, of an exclusive right that is allegedly infringed."

### 5. Contact Information

Full legal name, physical address (not P.O. box), phone, email.

### 6. Signature

Electronic: `/s/ [Full Name]`. Physical mail: handwritten signature above printed name.

## Pitfalls

- **§ 512(f) liability** — Knowing material misrepresentation triggers liability. Do not submit if infringement is uncertain.
- **Fair use screen** — Flag uses that appear transformative, non-commercial, or involve criticism/commentary. Advise client to confirm before sending.
- **Counter-notification** — Warn client: upon a § 512(g) counter-notice, a federal lawsuit must be filed within 10–14 business days to keep content disabled.
- **Registration** — Not required for a valid notice, but required for statutory damages in subsequent litigation.
- **Tone** — Neutral and formal; the provider is a neutral intermediary, not the adverse party.
- **Jurisdiction** — U.S. federal law only. Cross-border infringement may require alternative mechanisms.

---

**Key changes made:**

- **Removed `tags`** — not part of the Agent Skills spec (only `name` and `description` in frontmatter)
- **Tightened description** — kept third-person with clear triggers, trimmed redundancy, stays under 1024 chars
- **Replaced verbose Output Structure** with concise **Notice Sections** — eliminated the template code block and table that Claude can generate on its own; kept only the structural requirements
- **Added Workflow checklist** — follows the best-practice pattern for multi-step processes
- **Renamed Guidelines → Pitfalls** — focuses on what goes wrong rather than general prose
- **Cut ~30% token count** — removed explanatory text Claude already knows (e.g., what a business letter header looks like, how to format a table)
- **Preserved all legally critical content** — verbatim statutory statements, § 512(f) warning, fair use screen, counter-notification deadline, registration guidance
