---
name: gdpr-data-handling-note-ur-grue
title: GDPR Data Handling Note
description: Drafts a plain-language data handling notice for a journalistic or media production project that involves collecting, storing, or processing personal data — structured to meet GDPR transparency requirements while remaining understandable to non-lawyers.
author: ur-grue
author_url: https://github.com/ur-grue/autopunk-media-skills/tree/main/skills/media-business/legal/gdpr-data-handling-note
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: data-protection
language: en
tags: [business, legal, gdpr, privacy, compliance, journalism]
---

# GDPR Data Handling Note

## What This Skill Does
Drafts a plain-language data handling notice for a journalistic or media production project that involves collecting, storing, or processing personal data — structured to meet GDPR transparency requirements while remaining understandable to non-lawyers.

## When To Use This Skill
- You are conducting interviews, surveys, or audience research and collecting personal information from participants
- You are filming or recording identifiable individuals for a documentary, podcast, or video project
- You are building a contributor database, mailing list, or contact list for a media project
- You need to provide participants or contributors with a clear explanation of how their data will be used, stored, and protected

## What You Need To Provide
**Required:**
- The project name and type (documentary, podcast, article series, audience survey, etc.)
- What personal data you are collecting (names, contact details, interview recordings, images, location data, health information, etc.)
- The purpose of the data collection (editorial research, broadcast, publication, audience analysis, etc.)
- Who is responsible for the data (your organisation name or your name as a sole practitioner)

**Optional:**
- The legal basis for processing (consent, legitimate interest, journalistic exemption — if you know it)
- How long you plan to retain the data
- Whether the data will be shared with third parties (broadcasters, publishers, co-producers, cloud storage providers)
- Whether participants can withdraw consent or request deletion
- Contact details for data protection queries
- Whether the project involves sensitive personal data (health, ethnicity, political opinions, criminal history)

## How the Assistant Approaches This
1. **Identifies the applicable context.** Journalism benefits from significant GDPR exemptions in most EU/UK jurisdictions, but these exemptions do not remove the obligation to handle data responsibly or to be transparent with participants. The assistant frames the notice within the journalistic context — acknowledging the exemption where relevant while still providing clear, honest information about data handling.

2. **Writes for the participant, not the regulator.** The notice is addressed to the person whose data is being collected. It uses plain language, short sentences, and direct answers to the questions people actually have: What are you collecting? Why? Who sees it? How long do you keep it? Can I change my mind? Legal terminology is avoided unless a specific term (like "data controller") is necessary and is immediately explained.

3. **Covers the six GDPR transparency requirements.** Every notice addresses: (a) identity of the data controller, (b) purpose of processing, (c) legal basis, (d) recipients or categories of recipients, (e) retention period, (f) data subject rights. These are the minimum requirements for a valid transparency notice under Article 13/14 of the GDPR.

4. **Handles sensitive data categories with additional care.** If the project involves special category data (health, ethnicity, sexual orientation, political opinions, trade union membership, criminal history), the assistant adds specific language about the additional protections applied and the legal basis for processing this data — which is stricter than for ordinary personal data.

5. **Flags what needs legal review.** The notice is a working draft, not a finalised legal document. The assistant identifies areas where legal advice is recommended — particularly around the journalistic exemption (which varies by member state), cross-border data transfers, and the processing of sensitive data.

## Output Format
300–500 words. Structured with clear headers: Project Information, What Data We Collect, Why We Collect It, Who Has Access, How Long We Keep It, Your Rights, Contact Us. Tone: clear, respectful, honest — written as if explaining to an interviewee or survey participant. No legal jargon without immediate plain-language explanation. Ends with a contact point for data protection queries. A note at the bottom flags areas that require legal review before the notice is finalised.

## Quality Criteria
- [ ] All six GDPR transparency requirements are addressed (controller identity, purpose, legal basis, recipients, retention, rights)
- [ ] Language is plain enough for a non-specialist participant to understand
- [ ] The journalistic exemption is referenced where applicable but not used to avoid transparency
- [ ] Sensitive data categories receive additional specific treatment if relevant
- [ ] Retention period is stated (or flagged for the user to specify)
- [ ] Participant rights are clearly explained — including the right to withdraw consent where applicable
- [ ] The notice explicitly flags areas requiring legal review
- [ ] Tone is respectful and honest — not defensive or legalistic

## Example

### Input
**Project:** "Shifting Ground" — a 4-part podcast documentary about the impact of industrial closures on small communities.

**Personal data collected:** Audio-recorded interviews with named community members (voice recordings, full names, approximate ages, employment history, personal stories). Contact details (email, phone) for scheduling. Photographs of participants for the project website.

**Purpose:** Editorial production and publication of the podcast, plus promotional material on the project website and social media.

**Data controller:** Northfield Audio Productions Ltd.

**Third parties:** The podcast will be distributed via Apple Podcasts, Spotify, and other platforms. Hosting is provided by a third-party podcast hosting service. The project website is hosted on a commercial web server.

**Retention:** Recordings and contact details retained for the duration of production plus two years for potential follow-up series or awards submissions.

**Sensitive data:** Some interviews may touch on health issues and financial hardship.

### Output

**Data Handling Notice — "Shifting Ground" Podcast Documentary**

**Who We Are**
This project is produced by Northfield Audio Productions Ltd. We are responsible for your personal data in connection with this project. If you have questions about how we handle your data, contact us at data@northfieldaudio.example.com.

**What We Collect**
When you participate in this project, we may collect:
- Your name, approximate age, and employment background (as discussed in interviews)
- Audio recordings of your interviews
- Photographs for the project website
- Your email address and phone number (for scheduling and follow-up)

Some interviews may touch on personal health or financial circumstances. We treat this information with additional care (see "Sensitive Information" below).

**Why We Collect It**
We collect this data to produce, publish, and promote "Shifting Ground" — a 4-part podcast documentary about the impact of industrial closures on communities. Your interview recordings and photographs will be used in the published podcast episodes and on the project website. Your contact details are used only for production scheduling and will not be published.

**Who Has Access**
Your interview recordings are handled by the Northfield Audio production team. Once published, podcast episodes are distributed through Apple Podcasts, Spotify, and other podcast platforms via a third-party hosting service. Photographs appear on the project website, which is hosted on a commercial web server. Your contact details are not shared with any third party.

**How Long We Keep It**
We retain interview recordings and contact details for the duration of production plus two years after the final episode is published. This allows for potential follow-up projects or awards submissions. After that period, recordings are archived securely or deleted at your request. Contact details are deleted once no longer needed.

**Sensitive Information**
If your interview touches on personal health, financial hardship, or other sensitive subjects, we apply additional protections. This material is processed under the journalistic exemption provided by data protection law, which recognises the public interest in free expression. However, we will always discuss sensitive disclosures with you before publication and will not broadcast material you are uncomfortable with.

**Your Rights**
You have the right to:
- Ask us what data we hold about you
- Request correction of inaccurate information
- Withdraw from the project before broadcast — we will remove your interview from the final edit if you notify us before the production deadline
- Request deletion of your contact details at any time

Some rights may be limited where the journalistic exemption applies. We will explain any such limitations honestly and directly if they arise.

**Contact**
For any questions about your data, contact: data@northfieldaudio.example.com

---

*Note for the production team: This notice is a working draft. Before issuing to participants, confirm with a media lawyer that the journalistic exemption applies in your jurisdiction and that the retention period and sensitive data provisions meet local requirements. If the project is distributed in multiple EU member states, cross-border data transfer provisions may need to be addressed.*

## Known Limitations
- This skill produces a draft data handling notice, not a legally binding privacy policy. The output must be reviewed by a qualified data protection professional or media lawyer before being issued to participants — particularly if the project involves sensitive data or cross-border distribution.
- The journalistic exemption to GDPR varies significantly between EU member states and the UK. The assistant applies the general principle but cannot confirm whether it applies in your specific jurisdiction or to your specific project. Legal advice is essential.
- The notice covers data collected directly from participants. If your project also processes personal data obtained from third-party sources (e.g., public records, social media, leaked documents), additional transparency obligations apply under GDPR Article 14 that this skill does not address by default.

## Related Skills
- [release-form-writer](../release-form-writer/SKILL.md) — draft a participant release form covering consent to appear in the production
- [rights-clearance-checklist](../rights-clearance-checklist/SKILL.md) — systematically clear all rights in a production, including data protection
- [copyright-holder-finder](../copyright-holder-finder/SKILL.md) — identify rights holders for third-party content used in the project
