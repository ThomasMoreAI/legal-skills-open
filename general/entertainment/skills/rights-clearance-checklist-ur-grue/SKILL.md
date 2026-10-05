---
name: rights-clearance-checklist-ur-grue
title: Rights Clearance Checklist
description: Generates a comprehensive rights clearance checklist for a media project, covering music, archive footage, interview releases, third-party IP, and location permissions — tailored to the project's format and content.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/media-business/legal/rights-clearance-checklist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: entertainment
language: en
tags: [media-business, legal, rights, clearance, music, archive, production]
---

# Rights Clearance Checklist

## What This Skill Does
Generates a comprehensive rights clearance checklist for a media project, covering music, archive footage, interview releases, third-party IP, and location permissions — tailored to the project's format and content.

## When To Use This Skill
- You are entering post-production on a documentary or film and need to audit everything that requires clearance
- A broadcaster or distributor has requested a rights clearance report before signing a deal
- You are a first-time producer who wants to make sure nothing has been missed before delivery
- You are conducting a legal review of an existing project before distribution

## What You Need To Provide
**Required:** Project title and format (documentary, drama, short, podcast, etc.), a description of the types of content the project contains (talking heads, archive footage, music, on-camera brands/logos, locations, etc.), the intended distribution (broadcast, streaming, festival, podcast platforms).

**Optional:** Specific items you know require clearance (e.g., named archive provider, specific piece of music), territory of distribution, any clearances already obtained, any items you believe are in the public domain.

## How the Assistant Approaches This
1. Identifies all categories of rights that apply to the project based on the content description — music (sync and master), archive footage, talent releases, location releases, third-party IP (logos, brands, artworks visible on screen), and any special categories (news footage, AI-generated content, crowd scenes)
2. For each category, generates a specific checklist of items to be cleared, documents to obtain, rights holders to contact, and common mistakes to avoid
3. Flags any high-risk items (e.g., music with complex ownership, famous faces in crowd footage, footage from contested archives) and recommends specialist legal review where the risk is material
4. Closes with a "Next Step" note: which HIGH RISK item to address first and whether to contact an entertainment lawyer before beginning clearance on that item, and whether release-form-writer or licensing-brief-writer should be run for specific items still not started

## Output Format
Structured checklist by category, with a summary table at the top listing all categories and a status column (completed, in progress, not started). Each category section contains: what requires clearance, what documents are needed, who to contact, and any specific risk notes. Length varies with project complexity — typically 600–900 words. Uses checkboxes and tables for easy tracking. Includes a note on items that require entertainment lawyer review, not just standard clearance. Output ends with a "Next Step" note: which HIGH RISK item to tackle first, whether legal review is needed immediately, and whether to run release-form-writer or licensing-brief-writer for specific items.

## Quality Criteria
- [ ] All relevant clearance categories are identified based on the content description — nothing generically omitted
- [ ] Each category specifies the actual document or licence type needed (e.g., sync licence + master licence for music, not just "music clearance")
- [ ] High-risk items are flagged explicitly with a risk note, not buried in the general list
- [ ] The checklist distinguishes between clearances the producer can handle directly and those requiring legal counsel
- [ ] Distribution territory and platform type are reflected in the clearance requirements (e.g., streaming adds different requirements than theatrical only)
- [ ] Output includes at least one concrete next action the user can take immediately (start the highest-risk clearance, contact a lawyer for high-risk items, or run release-form-writer or licensing-brief-writer)

## Example

### Input
Project: The Collector — a feature documentary about a man who spent 30 years amassing a private collection of vintage advertising posters. The film includes: talking head interviews with the subject and his family; archive footage from a national film institute; clips from 1950s–1970s advertising films visible on a projection screen during filming; original music composed for the film; a brief sequence with a famous pop song playing on a radio; archive photographs from a commercial photo agency; exterior shots at a historic building (public access); a scene in the subject's home with branded items visible on shelves.
Distribution: Theatrical + streaming (global), broadcast (European)
Clearances obtained so far: Talent releases for all interviewees signed.

### Output

## Rights Clearance Checklist — THE COLLECTOR

### Summary Status Table

| Category | Items | Status |
|---|---|---|
| Talent releases | All interviewees | Completed |
| Archive footage — film institute | 1 archive provider | In progress |
| Advertising film clips | Multiple rights holders (unknown) | Not started — HIGH RISK |
| Commissioned music | Original score | Not started |
| Third-party music — synchronisation | 1 pop song | Not started — HIGH RISK |
| Archive photographs | 1 commercial agency | Not started |
| Location release | Historic building exterior | Not started |
| Third-party IP — brands/logos | Multiple products visible | Not started |
| Public domain assessment | Advertising films, photographs | Not started |

---

### Talent Releases
- [x] Written release forms signed by all interview subjects
- [ ] Confirm releases cover global theatrical + streaming + broadcast — check the scope of the releases already signed. If they were signed for "documentary use," confirm with your lawyer that this covers all intended distribution platforms.
- [ ] If any subject is a minor: parental or guardian consent required in addition to their own release.

---

### Archive Footage — National Film Institute
- [ ] Licence agreement specifying: territory (global), platforms (theatrical, streaming, broadcast), duration (in perpetuity or fixed term), usage type (documentary context)
- [ ] Confirm the institute holds all rights or can confirm they are not liable for underlying rights (music in archive footage can require separate clearance)
- [ ] Obtain a written representation from the institute about the rights status of music in any archive clips used

---

### Advertising Film Clips — HIGH RISK
The advertising films visible on-screen during filming are derived works — they contain original footage, music, voiceover, and potentially third-party IP. **Specialist legal advice required before these clips are included in the final edit.**

- [ ] Identify the original advertiser/brand for each clip
- [ ] Identify the production company that produced each clip
- [ ] Determine rights status: are these in the public domain? (Copyright law varies significantly by jurisdiction and date of production — do not assume public domain without legal advice)
- [ ] If rights holders identifiable: obtain a licence for each clip covering all distribution territories and platforms
- [ ] Consider whether these clips can be reframed (shown on the projection screen in a way that makes them incidental, not featured) — this may affect the clearance requirement

---

### Commissioned Music
- [ ] Written agreement with composer covering: ownership of master recording (producer should own or licence the master), right to use the music in all distribution formats and territories, moral rights waiver (UK and EU requirement)
- [ ] Confirm MCPS/performing rights registration is handled and that no third-party samples are embedded in the score

---

### Third-Party Music — Pop Song — HIGH RISK
A pop song "playing on a radio" is not automatically exempt from clearance. **Two separate licences are required:**

- [ ] Sync licence: from the music publisher (covers the underlying composition/song)
- [ ] Master licence: from the record label (covers the specific recording)
- [ ] Determine if this is fair use/fair dealing in your jurisdiction — this is a legal determination, not a production decision
- [ ] If the song is prominent or identifiable: assume clearance is required and budget accordingly. Pop song licences for global streaming can be expensive.

---

### Archive Photographs — Commercial Agency
- [ ] Confirm the agency's licence covers: editorial documentary use, all intended distribution platforms, all territories
- [ ] Request a representation that the agency owns or controls the rights they are licensing

---

### Location Release — Historic Building Exterior
- [ ] Obtain written location release from the building owner or management authority
- [ ] Check whether the building's exterior is protected by architectural copyright in your jurisdiction (relevant for some post-war buildings in Europe)

---

### Third-Party IP — Branded Products Visible on Shelves
In most jurisdictions, incidental appearance of branded products in documentary footage does not require clearance. However:
- [ ] Confirm products are genuinely incidental (not featured or mentioned by name in commentary)
- [ ] If any branded item is discussed, described, or held up to camera: seek legal advice on whether a product placement disclosure or clearance is required

---

### Recommended Legal Review Items
The following items require review by an entertainment lawyer before the project is delivered:
1. Advertising film clips — copyright status and clearance strategy
2. Pop song clearance — confirm fair dealing/fair use assessment and obtain licences
3. Review of talent releases for global streaming/broadcast scope

## Known Limitations
- This checklist covers the most common clearance categories for documentary production. Highly unusual content (classified documents, AI-generated content featuring real people, historical news footage from conflict zones) may have additional clearance requirements not covered here.
- Copyright law varies significantly by jurisdiction. Public domain determinations and fair dealing/fair use assessments are legal conclusions that must be made by a qualified entertainment lawyer in the relevant territory — this checklist cannot make those determinations.
- This skill generates a clearance framework; it does not complete the clearances. Every item marked "Not started" remains the producer's responsibility to resolve.

## Related Skills
- [licensing-brief-writer](../licensing-brief-writer/SKILL.md)
- [release-form-writer](../release-form-writer/SKILL.md)
- [press-release-writer](../../../pr-communications/press-office/press-release-writer/SKILL.md)
