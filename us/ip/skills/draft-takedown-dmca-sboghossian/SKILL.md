---
name: draft-takedown-dmca-sboghossian
title: DMCA Takedown Notice
description: Use when drafting a DMCA takedown notice (US 17 USC 512) or an equivalent notice-and-action request under EU DSA Article 16, UK copyright law, or MENA platform procedures. Covers the statutory elements for a valid DMCA notice, the counter-notice procedure, and equivalents for non-US infringing content. Flags that trademark infringement requires a separate instrument (cease-and-desist or platform trademark form) and that repeat-infringement subpoenas require court process.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-takedown-dmca
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: ip
language: en
---

# DMCA Takedown Notice

A DMCA takedown notice is a formal copyright-enforcement tool under the US Digital Millennium Copyright Act (17 USC 512) that requires online service providers to remove or disable access to infringing content upon receipt of a notice that meets the statutory requirements. For non-US platforms or non-US content, equivalent national procedures apply — the underlying principles are similar but the procedural requirements and enforcement leverage differ.

## When to use this

- A rights-holder or their authorized agent discovers infringing content on a platform, website, or cloud service
- The infringer has posted copyrighted text, images, video, audio, or code without authorization
- The platform is US-based, or the platform uses a DMCA-equivalent notice procedure
- For MENA-hosted content: platform-specific or court-order escalation path

**This skill is for copyright infringement only.** Trademark infringement requires a platform-specific trademark form or a cease-and-desist letter (see [[draft-cease-and-desist]]). Defamatory content requires separate legal process; the DMCA does not cover defamation.

## Required inputs

| Input | Why it matters | Default |
|---|---|---|
| Rights-holder identity (legal name, organization) | Establishes who owns the copyright | Must provide |
| Description of the original copyrighted work | Identifies what is being infringed | Must provide |
| URL(s) of infringing material | Must be specific enough to locate; platform needs to know what to remove | Must provide — collect all URLs |
| Contact information for the rights-holder or authorized agent | Required for DMCA validity; also needed for counter-notice response | Must provide |
| Authorization statement | Confirms sender is the rights-holder or authorized to act on their behalf | Required |
| Good-faith belief statement | That the use is not authorized by the rights-holder, its agent, or law | Required |
| Accuracy statement | That information in the notice is accurate, under penalty of perjury | Required; high-risk declaration |

## US DMCA Notice — Statutory Elements (17 USC 512(c)(3))

All six elements are mandatory for a valid DMCA notice; a notice missing any element may be treated as "substantially defective" and not trigger the OSP's safe-harbor obligation to remove:

1. **Physical or electronic signature** of the person authorized to act on behalf of the copyright owner
2. **Identification of the copyrighted work** claimed to be infringed (if multiple works at a single site, a representative list is sufficient)
3. **Identification of the infringing material** with sufficient information to locate it (specific URLs — provide the direct URL to the specific page or content, not the homepage)
4. **Contact information** for the complaining party: address, telephone number, and email address
5. **Good-faith belief statement**: "I have a good faith belief that the use of the copyrighted material described above is not authorized by the copyright owner, its agent, or the law."
6. **Accuracy and authority statement**: "The information in this notice is accurate, and under penalty of perjury, I am authorized to act on behalf of the owner of an exclusive right that is allegedly infringed."

### DMCA Notice Template

```
To: [Platform DMCA Agent / Copyright Agent]
[Platform Name, DMCA Agent Address / email]
Date: [Date]

DMCA Takedown Notice

I am [Full Name], [Title], acting on behalf of [Rights-Holder Legal Name]
(the "Rights-Holder"), which owns the copyright in the work described below.

1. COPYRIGHTED WORK

Description: [Title of work, or description if untitled] — a [photograph /
article / video / software code / musical composition] originally published
at [URL or other identification] on [date].

2. INFRINGING MATERIAL

The following URL(s) host content that infringes the Rights-Holder's
copyright in the above work without authorization:

  [URL 1 — exact URL of infringing page/post/file]
  [URL 2]
  [URL 3]

Description of how the material infringes: [e.g., "The above URL displays
the Rights-Holder's photograph [Title] without permission, license, or
any other authorization. The photograph has been reproduced in full without
attribution."]

3. STATEMENTS

Good-faith belief: I have a good faith belief that the use of the
copyrighted material described above is not authorized by the Rights-Holder,
its agent, or the law.

Accuracy and authority: The information in this notice is accurate and,
under penalty of perjury, I am authorized to act on behalf of the owner
of an exclusive right that is allegedly infringed.

4. CONTACT INFORMATION

[Full Name]
[Address]
[Phone]
[Email]

[Electronic or physical signature]
[Date]
```

### Where to Send
Find the platform's designated DMCA agent at the US Copyright Office's DMCA Agent Directory (copyright.gov/dmca-directory). Major platforms also have web forms (Google, Meta, YouTube, X/Twitter, Automattic/WordPress). Use the designated agent; sending to a general customer service address does not start the statutory clock.

## Non-US Equivalents

### EU — Digital Services Act (DSA) Article 16 Notice-and-Action

The EU's Digital Services Act (Regulation 2022/2065), fully applicable as of February 2024, requires online platforms to have a clear mechanism for notifying illegal content (including copyright infringement). The notice must include:
- Explanation of the specific reasons why the information is illegal
- Precise URL and, where necessary, additional identifying information
- If the notice relates to an individual: their name/nickname and electronic contact details
- Statement of genuine belief that the information constitutes illegal content (replacing the "good faith" formulation)

EU DSA notices do not carry the specific perjury risk of DMCA notices, but false notices can be subject to abuse-of-process claims.

### UK — Copyright, Designs and Patents Act 1988 (CDPA)
UK platforms use notice-and-takedown procedures similar to DMCA but governed by their own terms of service and the CDPA. No dedicated statutory agent directory; use platform's specified IP complaint mechanism. IP court proceedings (including IPEC — Intellectual Property Enterprise Court) for non-compliant platforms.

### MENA — UAE, KSA

| Jurisdiction | Mechanism | Notes |
|---|---|---|
| UAE | Platform-specific notice (major platforms); for non-compliant platforms, escalate to TDRA (Telecommunications and Digital Government Regulatory Authority); court injunction available | UAE Federal Decree-Law 34/2021 on combating rumors and cybercrime; copyright under UAE Federal Law 7/2002 (as amended) |
| KSA | Platform-specific notice; escalate to Communications, Space, and Technology Commission (CSC, formerly CITC) if platform unresponsive; Anti-Cybercrime Law and Copyright Law (Royal Decree M/41) | KSA Copyright Law provides criminal penalties for infringement; civil courts for civil remedies |
| General MENA | For non-compliant hosts (typically outside US/EU), court orders (interim injunctions / saisie) are necessary; identify the hosting provider's ISP and serve the ISP | MENA courts can order ISPs to block/filter infringing content |

## After Filing the Takedown

### Monitoring
- Keep records: dates of notice, URLs, screenshots of the infringing content before removal
- Monitor the URL for re-uploads; most infringers re-post within days of removal
- For platforms with repeat-infringer policies, document each incident to build a pattern
- Set up Google Alerts, TinEye (images), or Copyscape (text) to detect new infringements

### Repeat Infringers — Subpoena for Identification
Under DMCA 17 USC 512(h), a copyright owner may subpoena a service provider for the identity of a subscriber who is alleged to have infringed (before filing suit). Requirements:
- Must be issued by a US court
- Filed with the clerk of the district court
- Must be accompanied by a proposed subpoena and a copy of the notice

This is the mechanism to unmask anonymous infringers for purposes of a lawsuit.

### Counter-Notice Procedure
If the alleged infringer files a DMCA counter-notice claiming the removal was mistaken or misidentifying, the platform will:
1. Forward the counter-notice to the rights-holder
2. Restore the content within 10–14 business days unless the rights-holder provides notice of having filed a lawsuit against the alleged infringer

If the rights-holder receives a counter-notice and believes the infringement is real, they have 10–14 business days to file suit in the appropriate US federal court (or provide a settlement communication). Failure to file = content restored.

Counter-notices must include:
- Subscriber's name, address, phone, email
- Identification of removed material and URL
- Statement under penalty of perjury of good-faith belief that material was removed as a result of mistake or misidentification
- Consent to jurisdiction of the federal district court for the district where the subscriber is located (or, if outside US, in any judicial district where the service provider may be found)

## Risk Management

### The perjury declaration is serious
The "under penalty of perjury" statement in a DMCA notice means that knowingly false notices can result in criminal liability and civil damages. Before sending:
- Confirm you own or are duly authorized to act on the copyright
- Confirm the specific use is not authorized (check for Creative Commons licenses, fair use arguments)
- Confirm the use is not transformative in a way that might qualify as fair use

### Takedown abuse
DMCA notices sent for the purpose of suppressing legitimate criticism, fair use commentary, or competitor speech (rather than genuine copyright infringement) constitute "knowing material misrepresentation" under DMCA 17 USC 512(f) and expose the sender to damages.

## Related skills

- [[draft-cease-and-desist]]
- [[review-ip-infringement]]
- [[kb-ip-law-mena]]
- [[draft-trademark-application]]
