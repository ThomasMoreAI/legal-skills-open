---
name: creative-commons-explainer-ur-grue
title: Creative Commons Explainer
description: Explains a specific Creative Commons licence in plain language, telling a media professional exactly what they can and cannot do with the licensed content — including attribution requirements, commercial use rules, and derivative work restrictions.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/media-business/legal/creative-commons-explainer
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
tags: [business, legal, creative-commons, licensing, rights, open-access, attribution]
---

# Creative Commons Explainer

## What This Skill Does
Explains a specific Creative Commons licence in plain language, telling a media professional exactly what they can and cannot do with the licensed content — including attribution requirements, commercial use rules, and derivative work restrictions.

## When To Use This Skill
- You found an image, video, audio clip, or text labelled with a Creative Commons licence and need to know if you can use it
- You want to understand the difference between CC licence types before choosing one for your own work
- You need to confirm whether a specific use (commercial broadcast, remix, adaptation, social media repost) is permitted under a given CC licence
- You are writing usage guidelines for your team and need a clear, jargon-free summary of each licence type

## What You Need To Provide
**Required:**
- The Creative Commons licence type (e.g., CC BY 4.0, CC BY-SA 3.0, CC BY-NC-ND 4.0, CC0) — the full name, the abbreviation, or the URL from the licence deed

**Optional:**
- Your intended use (editorial article, commercial broadcast, YouTube video, podcast, social media, remix/adaptation, print publication)
- Whether you plan to modify the work (crop, edit, translate, incorporate into a larger piece)
- Whether your use is commercial or non-commercial
- The specific content you are licensing (helps the assistant give concrete examples of compliant attribution)

## How the Assistant Approaches This
1. **Identifies the licence and version.** Creative Commons licences differ meaningfully between versions (2.0, 3.0, 4.0). The assistant confirms the exact licence and version, notes any differences from the current version if relevant, and flags if the licence URL or abbreviation does not match a valid CC licence.

2. **Explains the licence in four plain-language categories.** Every CC licence answer covers: (a) Can I use this commercially? (b) Can I modify, remix, or adapt it? (c) Do I have to credit the creator, and how? (d) Do I have to share my version under the same licence? These four questions cover 95% of what media professionals need to know.

3. **Applies the licence to the stated use case.** If you describe your intended use, the assistant gives a direct yes/no answer on whether that use is permitted, with a brief explanation of why. No hedging when the answer is clear; honest flagging when it is genuinely ambiguous.

4. **Provides a model attribution line.** For licences that require attribution, the assistant writes an example attribution line that meets the licence requirements — including the creator's name (if known), the work title, the licence name, and a link to the licence deed. This is copy-paste ready.

5. **Flags common mistakes.** Many media professionals misunderstand "non-commercial" (it does not mean "I am not making money from this specific piece"), confuse ShareAlike with attribution-only, or forget that NoDerivatives prohibits cropping or editing. The assistant identifies the most common mistake for the specific licence and warns against it.

## Output Format
200–350 words. Structured in clear sections: Licence Summary (one sentence), What You Can Do, What You Cannot Do, Attribution Requirement (with a model attribution line), and Common Mistakes. If a specific use case was provided, a "Your Use Case" section gives a direct yes/no verdict. Tone: plain English, no legal jargon, written for someone who has never read a licence in their life. No disclaimers about not being a lawyer — the output is practical guidance, clearly presented.

## Quality Criteria
- [ ] The licence type and version are correctly identified
- [ ] The four key questions (commercial use, modification, attribution, share-alike) are all answered
- [ ] The model attribution line meets the actual requirements of the stated licence
- [ ] If a specific use case is described, a clear yes/no verdict is given
- [ ] Common mistakes are relevant to the specific licence — not generic warnings
- [ ] Language is plain enough for someone with no legal training to understand and act on
- [ ] No false reassurance — genuinely ambiguous situations are flagged honestly

## Example

### Input
**Licence:** CC BY-NC-SA 4.0

**Intended use:** Using a photograph found on a government research website in a YouTube documentary about ocean pollution. The documentary is monetised through YouTube ads and a Patreon membership.

**Modification planned:** Cropping the image and adding a text overlay with a statistic.

### Output

**Licence Summary**
CC BY-NC-SA 4.0 (Attribution-NonCommercial-ShareAlike 4.0 International) lets you copy, redistribute, and adapt the work — but only for non-commercial purposes, with credit to the creator, and only if you share your adapted version under the same licence.

**What You Can Do**
- Copy, share, and display the photograph in any medium or format
- Modify the photograph — crop it, add overlays, incorporate it into a larger work
- Use it in educational, personal, and non-commercial projects

**What You Cannot Do**
- Use it for commercial purposes — any use primarily intended for commercial advantage or monetary compensation is restricted
- Share an adapted version under a different, less restrictive licence — if you modify the work, your version must also carry CC BY-NC-SA 4.0 (or a compatible licence)
- Remove or obscure the attribution

**Attribution Requirement**
You must credit the creator, provide the licence name, and link to the licence deed. A compliant attribution for a YouTube video would appear in the video description:

> *Photograph: [Creator Name], "[Image Title]," licensed under CC BY-NC-SA 4.0 (creativecommons.org/licenses/by-nc-sa/4.0/). Image cropped and text overlay added.*

Note the final line — when you modify a CC-licensed work, best practice is to indicate what changes you made.

**Your Use Case**
**No — this use is likely not permitted.** Your YouTube documentary is monetised through ads and Patreon memberships. Under CC BY-NC-SA 4.0, "NonCommercial" means the use is not primarily intended for or directed toward commercial advantage or private monetary compensation. A monetised YouTube channel is generally considered commercial use, even if the documentary itself is educational in content. Using this photograph in a monetised video would violate the NC restriction.

**Options:** Contact the rights holder directly to request a separate commercial licence. Alternatively, search for a similar image released under CC BY 4.0 or CC BY-SA 4.0, which permit commercial use.

**Common Mistake**
The most frequent error with NC licences is assuming that "non-commercial" means "I am not a business" or "I am not selling this specific image." It does not. If the platform, channel, or publication where you use the work generates revenue — through ads, subscriptions, memberships, or sponsorship — the use is generally considered commercial, regardless of whether the specific piece of content is directly monetised.

## Known Limitations
- Creative Commons licences are legal instruments, and edge cases exist. The assistant provides practical guidance that is accurate for straightforward use cases, but genuinely ambiguous situations (e.g., whether a specific use qualifies as "non-commercial" in a particular jurisdiction) may require legal advice.
- The assistant cannot verify that the person who applied the CC licence to a work actually held the rights to do so. If the original uploader did not own the copyright, the CC licence may be invalid. When in doubt about provenance, verify the source.
- The explanation covers the licence terms as written by Creative Commons. Some institutions apply additional terms or restrictions alongside CC licences (e.g., "CC BY 4.0, but please notify us of use"). The assistant addresses the CC licence only, not supplementary conditions.

## Related Skills
- [copyright-holder-finder](../copyright-holder-finder/SKILL.md) — find the rights holder when a work is not CC-licensed and you need permission
- [rights-clearance-checklist](../rights-clearance-checklist/SKILL.md) — systematically clear all third-party content in a production
- [licensing-brief-writer](../licensing-brief-writer/SKILL.md) — draft a licensing request for content that requires permission
