---
name: image-rights-checker-ur-grue
title: Image Rights Checker
description: Reviews the details of a specific image and flags potential rights clearance issues before publication, identifying which permissions you likely need and which questions to bring to your legal or picture desk.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/archive-legal/image-rights-checker
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: entertainment
language: en
tags: [rights, licensing, images, photos, archive, clearance]
---

# Image Rights Checker

## What This Skill Does
Reviews the details of a specific image and flags potential rights clearance issues before publication, identifying which permissions you likely need and which questions to bring to your legal or picture desk.

## When To Use This Skill
- Before publishing a photograph, illustration, or archival image in any format (print, digital, broadcast, social media)
- When you are unsure whether a Creative Commons or public domain claim genuinely covers your intended use
- When sourcing images from third-party stock libraries, press agencies, or social media accounts
- When repurposing an image that was previously licensed for a different format or territory
- When an editor asks for a rights summary before sign-off

## What You Need To Provide
**Required:**
- How you found or obtained the image (stock library, press agency, own photography, archive, social media, Creative Commons source, etc.)
- The license type or usage agreement you have, if any (e.g., "Getty editorial license", "CC BY 4.0", "no license — found on Instagram")
- Your intended use: publication format (web article, print magazine, broadcast, social media), territory, and whether the use is commercial or editorial
- Any known information about the image: who took it, when, whether identifiable people appear in it, whether it depicts private property or artworks

**Optional:**
- The specific publication or outlet name (helps assess territory and commercial context)
- Whether the image will appear in advertising or sponsored content
- Whether the subject of the image is a public figure or a private individual

## How the Assistant Approaches This
1. Identifies the rights category of the image based on how it was sourced — stock license, agency wire, Creative Commons, public domain, social media, or unknown — and notes what protections and restrictions typically apply to each category.
2. Cross-checks your intended use against the known restrictions for that rights category: editorial vs. commercial use, territory limits, attribution requirements, model and property release requirements, and format restrictions (print vs. digital vs. broadcast).
3. Flags every point where your intended use may conflict with or exceed the likely rights coverage, and assigns each flag a risk level (Low / Medium / High) with a plain-English explanation of what the risk means in practice.
4. Lists the specific clearance steps — questions to ask, documents to obtain, or parties to contact — needed before the image is safe to publish.

## Output Format
A structured checklist, approximately 300–500 words. Organised into three sections:

**Rights Summary** — what rights you likely have based on the information provided, in two to three plain sentences.

**Risk Flags** — a bulleted list of issues, each with a risk level tag (Low / Medium / High) and a one-sentence explanation.

**Clearance Steps** — a numbered action list of what to do before publishing. Each step is concrete and actionable (e.g., "Request a signed model release from the photographer" rather than "Ensure releases are in order").

Tone: direct and practical, written for a journalist or picture editor, not a lawyer. No legal jargon without explanation.

## Quality Criteria
- [ ] Every risk flag includes a clear, plain-English explanation of why it is a risk
- [ ] Risk levels (Low / Medium / High) are assigned to each flag — none left unrated
- [ ] Clearance steps are specific enough to act on without further interpretation
- [ ] Output does not render a legal verdict — it frames findings as flags and questions
- [ ] The Known Limitations disclaimer is reflected in tone throughout (flags, not rulings)
- [ ] No rights category is treated as automatically safe without noting the conditions that apply

## Example

### Input
Image details: A photograph of a crowd at a public street protest, taken by a freelance photographer. I found it on a Creative Commons image repository tagged as CC BY 2.0. The photographer's name is listed. The image shows identifiable faces in the crowd. Intended use: web article on a current affairs news site, UK and international digital edition, editorial (not advertising). No additional license agreement held.

### Output

**Rights Summary**

The image is published under a Creative Commons Attribution 2.0 (CC BY 2.0) license. This license permits reproduction and publication for editorial purposes, provided you credit the photographer in the format they specify. CC BY 2.0 does not restrict commercial use, but it also does not include any model releases or property releases — those remain the publisher's responsibility.

**Risk Flags**

- **Identifiable individuals in the crowd — Medium risk.** UK and many international jurisdictions extend privacy protections to individuals even in public spaces, particularly in political or protest contexts. Publishing recognisable images of protesters without consent may expose the outlet to claims under data protection law (UK GDPR) or privacy tort. The risk is heightened if the image could be used to identify political affiliation.

- **CC license version and scope — Low risk.** CC BY 2.0 is a legitimate, irrevocable license, but confirm the license has not been disputed or withdrawn by the repository host since original upload. Some repositories mislabel licenses.

- **Freelance photographer — third-party copyright — Low risk.** The photographer holds the underlying copyright. CC BY 2.0 covers your use, but confirm the photographer actually held the rights to license the image (i.e., was not hired under a work-for-hire arrangement that transferred copyright to another party).

- **Sensitive political context — Medium risk.** Images from protests may carry additional editorial sensitivity. If any individual depicted could be identified as a protest leader, check whether naming or publishing their image raises separate ethical or safety concerns beyond legal rights.

**Clearance Steps**

1. Credit the photographer exactly as specified in the Creative Commons license metadata or repository listing.
2. Check the repository page for any license dispute notices or takedown history on this specific image.
3. Consult your picture desk or legal team about whether the identifiable faces require pixelation or consent, given the political protest context and UK GDPR obligations.
4. Confirm with the photographer (if contactable) that they personally took the image and held the right to apply the CC license.
5. If the image is to be reused in print or broadcast at a later date, note that the CC BY 2.0 license covers those uses but the privacy/consent question about identifiable individuals must be re-evaluated for each new format.

## Known Limitations
- This skill flags potential issues and generates questions for your legal or picture desk — it does not provide legal advice and is not a substitute for qualified legal counsel. Always involve a media lawyer or your outlet's legal team before publishing in any situation where a High-risk flag has been raised.
- Rights landscapes differ significantly by country. Flags are based on widely applicable principles (UK, EU, US) but jurisdiction-specific rules may differ. Always verify against the law of the territory where you publish.
- This skill cannot search license databases, verify photographer credentials, or confirm whether a listed Creative Commons license is genuine. It reasons only from the information you provide.
- Model and property release requirements vary by outlet, insurer, and use case. This skill flags the issue; your picture desk or legal team must determine the specific standard that applies to your publication.

## Related Skills
- [legal-risk-checker](../legal-risk-checker/SKILL.md)
- [rights-clearance-checklist](../../media-business/legal/rights-clearance-checklist/SKILL.md)
- [defamation-risk-checker](../../magazine-journalism/legal/libel-check-brief/SKILL.md)
