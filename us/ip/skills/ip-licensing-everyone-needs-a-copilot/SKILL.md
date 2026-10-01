---
name: ip-licensing-everyone-needs-a-copilot
title: IP Licensing Skill
description: IP licensing clause review and negotiation. Use for license scope, sublicensing, improvements, audit rights, warranties, infringement indemnity, termination, Background IP, and deliverable ownership.
author: Everyone-Needs-A-Copilot
author_url: https://github.com/Everyone-Needs-A-Copilot/codex-copilot/tree/main/packs/writing-legal/skills/ip-licensing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# IP Licensing Skill

An IP license defines who can use what, for what purpose, in what territory, for how long, and on what financial terms. Get any of these wrong and you either give away more than you intended or receive less than you need.

---

## The Three IP Categories (ENAC Context)

### Background IP
Pre-existing IP. Created before or independent of a specific client engagement.
- Owned entirely by ENAC
- Licensed to clients (not assigned)
- License scope: to use embedded in deliverables, for client's internal purposes only
- Examples: "Not a Pitch Deck" framework, slide-copywriting methodology, all agent definitions and prompt libraries, alignment document structure, ENAC Four Agents framework

### Foreground IP
Created specifically for and delivered to the client under the engagement.
- Can be assigned to the client
- Does NOT include Background IP incorporated into the deliverable
- Examples: a specific organizational assessment report, a client-specific presentation deck, a custom data analysis

### Derivative IP
Improvements or modifications to Background IP that emerge during a client engagement.
- Belongs to ENAC, not the client
- Must be documented and captured in the skills repository after each engagement
- Client receives a license to use derivative IP to the extent embedded in deliverables
- Examples: a refined version of ENAC's assessment methodology developed while working on a specific engagement

---

## License Grant: Key Dimensions

Every license grant must specify these five dimensions. Missing any one creates ambiguity that will be resolved in litigation.

### 1. Exclusivity
**Non-exclusive:** ENAC can grant the same license to multiple clients. **Default and preferred for ENAC.**
**Exclusive:** Only one licensee. Typically requires significant compensation. Incompatible with ENAC's business model unless in a very narrow field.

### 2. Scope (Field of Use)
What can the licensee do with the IP?
- Read-only / view only
- Internal use only (cannot be shared with third parties)
- Cannot be used to train AI systems
- Cannot be used as a basis for competing services

**ENAC's standard:** Client may use Background IP "solely to the extent embedded in the final deliverables specifically identified in the Statement of Work for County's internal business purposes only."

### 3. Territory
Geographic restriction on use. For ENAC: "within the jurisdictional boundaries of [Adams County/Colorado]" or "for internal business purposes" (territory-neutral). No sublicensing.

### 4. Duration
**Term license:** For the duration of the contract or a specified period.
**Perpetual license:** Survives termination of the contract. Standard for deliverables: the client needs to use the report after the engagement ends.

**ENAC's standard:** Perpetual for use of Background IP in delivered reports, but NOT perpetual for ongoing access to ENAC's methodology more broadly.

### 5. Sublicensing Rights
Can the licensee grant rights to third parties? **No.** ENAC does not permit sublicensing of Background IP. Include explicitly: "This license is non-transferable and may not be sublicensed."

---

## Government IP Rights Framework (FAR 52.227-14)

For federally-funded contracts, the Federal Acquisition Regulation defines three tiers of government rights:

**Unlimited Rights:**
The government can use, reproduce, disclose, and modify the work without restriction. This is what the government wants and what ENAC must avoid for Background IP.

**Limited Rights:**
Applies to trade secrets and confidential commercial information included in data deliverables. The government can use internally but cannot disclose to third parties without the contractor's consent. ENAC should assert limited rights for all Background IP submitted as part of deliverables.

**Restricted Rights:**
Applies to commercial computer software. The government gets only the rights specified in the license. ENAC's software tools and AI system configurations, if delivered, should be subject to restricted rights.

**How to assert restricted/limited rights:**
Mark all Background IP materials with a legend such as:
> "These materials contain trade secrets and Background Intellectual Property of ENAC, subject to Limited Rights as defined in FAR 52.227-14. Disclosure, reproduction, or use beyond the terms set forth in the contract is not authorized without ENAC's written consent."

---

## Improvements and Derivative Works

Who owns improvements to the licensed IP?

**ENAC's position:** Any improvement to ENAC's Background IP remains ENAC's property, regardless of when it was developed. The client pays for the output, not for ownership of the methodology improvements that occurred while producing it.

**Clause language:**
> "Any modifications, improvements, or derivative works of ENAC's Background IP developed by or with input from either party during the term of this Agreement shall be owned by ENAC. ENAC grants County a license to use such derivative works to the extent incorporated in the final deliverables, subject to the same terms as the license granted for Background IP."

**Why this matters:** ENAC's methodology improves with every engagement. If the client owns the improvements, ENAC must license back its own updated methodology from every past client. This makes the business model impossible.

---

## AI Output Copyrightability

Post-Thaler v. Perlmutter (D.D.C. 2023, on appeal): AI-generated work without sufficient human authorship is not protected by copyright.

**Practical implications for ENAC's deliverables:**
- Purely AI-generated text with no human editing: not copyrightable
- AI-generated analysis reviewed, edited, and approved by a human consultant: likely protectable based on the human's creative contribution
- Document human editorial decisions per deliverable

**For client contracts:** Do not promise copyright ownership of AI-generated output unless the extent of human authorship has been confirmed. Frame as "work product" with the IP carve-out structure rather than as copyrighted works.

---

## IP Infringement Indemnification

Government clients often require ENAC to indemnify them against third-party IP infringement claims arising from ENAC's deliverables.

**Acceptable:**
Indemnify for ENAC's own IP (i.e., ENAC's deliverables do not infringe a third party's IP). Capped at fees paid.

**Not acceptable:**
- Indemnify for the client's use of deliverables beyond the scope of the license grant
- Indemnify for open-source components the client adds to ENAC's deliverables
- Unlimited indemnification for IP claims

**Clause language:**
> "ENAC shall defend, indemnify, and hold harmless County from third-party claims that the deliverables (excluding Background IP licensed hereunder) infringe a valid U.S. patent, copyright, or trademark, provided that County notifies ENAC promptly of any such claim, cooperates fully in ENAC's defense, and grants ENAC sole control of the defense. ENAC's obligations under this section are subject to the limitation of liability set forth in [Section X]."

---

## License Termination for IP Breach

What happens to the client's license if the contract is breached?

**ENAC's position:** If the client uses Background IP outside the scope of the license (e.g., shares ENAC's methodology with third parties, uses it to train AI, uses it to build competing services), ENAC can terminate the license.

**Clause language:**
> "This license shall terminate automatically if County (a) uses Background IP beyond the scope specified herein, (b) sublicenses or transfers Background IP to any third party, (c) uses Background IP to develop products or services competitive with ENAC's consulting offerings, or (d) materially breaches its confidentiality obligations. Upon termination, County shall immediately cease all use of Background IP and return or destroy all copies."

---

## Open-Source License Compliance

For any code or software components used in deliverables:

| License Type | Can Be Used in Government Deliverables? | Notes |
|-------------|----------------------------------------|-------|
| MIT | Yes | Attribution required |
| Apache 2.0 | Yes | Attribution + NOTICE file required |
| BSD 2/3-clause | Yes | Attribution required |
| LGPL | With care | Dynamic linking generally OK; static linking may trigger copyleft |
| GPL / AGPL | Risky | May require source code disclosure of modified works |
| Creative Commons BY | Yes | Attribution required |
| CC BY-SA | With care | Share-alike requirement |
| Proprietary | Only with license | Verify license permits government delivery |

Flag any GPL or AGPL dependencies before delivering to a government client.

---

## Output Structure

1. **License grant analysis**: Five dimensions assessed (exclusivity, scope, territory, duration, sublicensing)
2. **Background IP carve-out**: Confirmed present and adequate, or redline required
3. **Derivative IP ownership**: Confirmed retained by ENAC or clause required
4. **Government rights tier**: For federally-funded contracts: unlimited/limited/restricted rights asserted
5. **AI output copyrightability**: Human authorship confirmed or flagged
6. **IP indemnification scope**: Capped and reasonable, or redline required
7. **Open-source compliance**: Any flagged dependencies

---

## Anti-Generic Rules

- NEVER confuse a license with an assignment: they are legally distinct and one is irrevocable
- NEVER grant exclusive rights to Background IP without a significant premium and specific business justification
- NEVER accept FAR "unlimited rights" to ENAC's Background IP in federally-funded contracts
- NEVER omit the derivative IP clause: improvements to methodology must remain with ENAC
- NEVER allow sublicensing of Background IP without explicit, specific written authorization
