---
name: copyright-holder-finder-ur-grue
title: Copyright Holder Finder
description: Produces a step-by-step research plan for identifying the copyright holder of a specific piece of content — image, footage, text, music, or other media — tailored to the content type and jurisdiction.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/media-business/legal/copyright-holder-finder
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: ip
language: en
tags: [business, legal, copyright, rights, research, clearance, licensing]
---

# Copyright Holder Finder

## What This Skill Does
Produces a step-by-step research plan for identifying the copyright holder of a specific piece of content — image, footage, text, music, or other media — tailored to the content type and jurisdiction.

## When To Use This Skill
- You want to license an image, clip, or music track but cannot identify who owns the rights
- You found archival footage or a photograph with no clear attribution and need to clear it for use
- You are producing a documentary or article and need to trace rights holders for third-party material
- You need to determine whether a work is orphaned (no identifiable rights holder) before applying fair use or other exceptions

## What You Need To Provide
**Required:**
- A description of the content you are trying to clear (what it is, where you found it, any identifying details — title, creator name, date, publication, watermark, metadata)
- The content type (photograph, video footage, music recording, text excerpt, illustration, etc.)

**Optional:**
- The jurisdiction you are working in (affects which registries and legal frameworks apply)
- What you already know about the provenance (e.g., "published in a magazine in the 1990s but no photographer credit," "found on a stock site with no licensing information")
- Your intended use (editorial, commercial, broadcast, online-only — this affects which rights you need to clear)
- Any deadline pressure (some research steps take weeks; knowing your timeline helps prioritise)

## How the Assistant Approaches This
1. **Assesses what is already known.** Before proposing research steps, the assistant inventories the identifying information you have — creator name, publication, date, metadata, watermarks, reverse image search results — to determine how close you already are to an answer and which gaps remain.

2. **Builds a research plan specific to the content type.** The path to a copyright holder differs by medium: photographs route through image agencies, photographer registries, and publication archives; music routes through performing rights organisations, mechanical rights databases, and publisher catalogues; text routes through publishers, literary agents, and copyright registration databases. The assistant selects the relevant path and provides specific registries, databases, and organisations to contact.

3. **Orders steps from fastest to slowest.** The plan starts with quick digital checks (reverse image search, metadata extraction, online database lookups) and progresses to slower methods (contacting publishers, submitting formal enquiries to collecting societies, searching national copyright offices). This ensures you do not spend two weeks on a letter when a five-minute search would have found the answer.

4. **Includes contact templates where useful.** For steps that require reaching out to organisations or individuals (e.g., a publisher's permissions department, a collecting society, or an archive), the assistant provides a brief template for the enquiry — what to say, what information to include, and what to ask for.

5. **Flags when to seek legal advice.** If the research plan suggests the work may be orphaned, the rights situation is legally complex (e.g., works created under employment, works from dissolved companies, pre-digital-era contracts), or the intended use carries significant financial risk, the assistant recommends consulting a media lawyer rather than proceeding on assumption.

## Output Format
A numbered research plan of 5–10 steps, ordered from fastest to slowest. Each step includes: what to do, where to do it (specific database, website, or organisation name), and what result to expect. Where relevant, a brief contact template is included. The plan ends with a "If All Else Fails" section covering orphan works procedures and a recommendation on when to consult a lawyer. Tone: practical, specific, no legal jargon. Total length: 400–600 words.

## Quality Criteria
- [ ] Research steps are specific to the content type — not a generic "search the internet" list
- [ ] Steps are ordered from fastest/cheapest to slowest/most resource-intensive
- [ ] Named registries, databases, and organisations are real and relevant to the content type
- [ ] Contact templates include what information the user should provide in their enquiry
- [ ] The plan acknowledges when the rights situation may be legally complex and recommends professional advice
- [ ] Orphan works possibility is addressed — not ignored
- [ ] Jurisdictional considerations are noted where relevant (different countries have different registries)

## Example

### Input
**Content:** A black-and-white photograph of a crowded fish market, estimated to be from the 1960s or 1970s. Found in a printed local history book published in 1985 by a small regional press. The book credits "Photograph courtesy of the Harbour Heritage Collection" but gives no photographer name. The publisher appears to be defunct.

**Content type:** Photograph.

**Jurisdiction:** United Kingdom.

**Intended use:** Editorial use in a television documentary about the decline of coastal fishing communities.

**What is already known:** The publisher's name (Saltmarsh Press) appears on the copyright page. No ISBN found. The Harbour Heritage Collection appears to be a local archive but has no web presence.

### Output

**Copyright Holder Research Plan — Fish Market Photograph (c. 1960s–70s)**

---

**1. Extract all available metadata from the book.**
Photograph the copyright page, the photo credit line, and any acknowledgements section. Note the book's title, publication year (1985), and any other credits. Check for an ISBN — even if you did not find one initially, it may appear on the back cover or inside the rear flyleaf.

**2. Search for the publisher.**
Saltmarsh Press may be defunct, but its catalogue may have been acquired. Search Companies House (companieshouse.gov.uk) for "Saltmarsh Press" to find dissolution records, successor companies, or named directors who may know what happened to the photographic rights. Search the British Library catalogue (explore.bl.uk) for other titles published by Saltmarsh Press — these may contain more detailed acknowledgements or photographer credits.

**3. Locate the Harbour Heritage Collection.**
Contact the local council's archives and heritage department for the area where the book was published. Local heritage collections are often held by county record offices, municipal libraries, or volunteer-run trusts. The Archives Hub (archiveshub.jisc.ac.uk) may have a catalogue entry. If the collection still exists, its custodian may hold documentation identifying the photographer.

**4. Search UK photographer registries.**
If a photographer name emerges at any step, search the Association of Photographers directory (the-aop.org), the British Press Photographers' Association, and the DACS (Design and Artists Copyright Society) payback database at dacs.org.uk. DACS manages rights for many visual artists and photographers in the UK and can confirm whether a named photographer is registered.

**5. Contact DACS directly with a rights enquiry.**
If no photographer name has been found, submit an enquiry to DACS describing the photograph, its provenance, and your intended use. Use this template:

> *Subject: Copyright enquiry — unattributed photograph, c. 1960s–70s*
>
> *I am seeking to identify the copyright holder of a black-and-white photograph of [brief description], published in [book title] by Saltmarsh Press in 1985. The credit reads "Photograph courtesy of the Harbour Heritage Collection" but no photographer is named. I am producing a television documentary and wish to license the image for editorial broadcast use. Could you advise whether this image or photographer is registered with DACS, or suggest a next step?*

**6. Try reverse image search.**
Scan or photograph the image at high resolution and run it through Google Images reverse search and TinEye (tineye.com). If the image appears elsewhere online — in another publication, archive, or stock library — the credit line may identify the photographer.

**7. Search the UK Copyright Tribunal and orphan works register.**
The UK Intellectual Property Office maintains an orphan works register (gov.uk/government/organisations/intellectual-property-office). Check whether this image has been previously registered as an orphan work by another user. If not, this register is where you may ultimately need to apply for a licence if the rights holder cannot be found.

**If All Else Fails**

If no rights holder can be identified after completing these steps, the photograph may qualify as an orphan work under UK law. The IPO operates an Orphan Works Licensing Scheme that allows use of orphan works for a set fee, provided you can demonstrate a diligent search. Document every step you have taken — the IPO requires evidence of your search effort.

For a television documentary, the financial and reputational risk of using an uncleared image is significant. If the diligent search does not produce a rights holder, consult a media lawyer before proceeding — they can advise on the orphan works application or on whether your use might qualify under another exception.

## Known Limitations
- The assistant provides a research methodology, not a rights clearance. The plan directs you to the right databases and organisations, but you must perform the searches and contacts yourself. The assistant cannot access external databases or verify current registry contents.
- Registry names and URLs are accurate at the time of writing but may change. Verify that the resources listed are still active, particularly for government databases and collecting societies.
- For content originating in jurisdictions outside the UK, US, and EU, the relevant registries and legal frameworks may differ significantly. The assistant can provide general guidance but may not know every national copyright office or collecting society.

## Related Skills
- [rights-clearance-checklist](../rights-clearance-checklist/SKILL.md) — a systematic checklist for clearing all third-party content in a production
- [licensing-brief-writer](../licensing-brief-writer/SKILL.md) — draft a licensing request once you have identified the rights holder
- [creative-commons-explainer](../creative-commons-explainer/SKILL.md) — understand what a Creative Commons licence allows before assuming you need to find the rights holder
