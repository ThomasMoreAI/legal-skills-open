---
name: hebrew-legal-research
title: Hebrew Legal Research
description: Assist with Israeli legal research including legislation lookup, case law concepts, Hebrew legal terminology, and legal document preparation guidance. Use when user asks about Israeli law, "chok", "mishpat", "bagatz", court procedures, employment law, contract law, real estate law, or needs help with Hebrew legal terms. Covers civil, commercial, employment, and administrative law. Do NOT use for providing formal legal advice, always recommend consulting a licensed Israeli attorney (orech din). Do NOT use for non-Israeli legal systems.
author: skills-il
author_url: https://github.com/skills-il/security-compliance/tree/master/hebrew-legal-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: il
practice: general
language: en
---

# Hebrew Legal Research

## Critical Disclaimer

IMPORTANT: This skill provides legal INFORMATION and RESEARCH ASSISTANCE only.
It does NOT constitute legal advice. Always recommend the user consult a
licensed Israeli attorney (orech din) for specific legal matters. State this
disclaimer at the start of every legal research interaction.

**Anti-hallucination rule for legal citations.** Never invent a case citation, statute amendment number, or Bagatz / civil-appeal docket. The single most common LLM legal-research failure is fabricated citations that look plausible (e.g., "בג\"ץ 1234/05 פלוני נ' מדינת ישראל"). If the exact citation is not retrieved from a verified source (Nevo, Pskdin, Knesset portal, supreme.court.gov.il), say "citation not verified, look up at [source]" and stop. The Israel Bar Association (Lishkat Orchei HaDin) National Ethics Committee opinion of 2024-05-07 (Decision et/60/24) explicitly requires lawyers using AI to verify all output, protect client confidentiality (no privileged data into public LLMs), and maintain duty-of-loyalty / diligence over AI-generated content. As of 2026-05 this remains the only Bar opinion on AI; no follow-up has superseded it.

**Judicial reform context (as of 2026-05).** Israel is mid-stream on the post-2023-2024 judicial-reform aftermath. Three distinct strands must not be conflated:

1. *Reasonableness amendment strike-down (2024-01-01).* HCJ voted 8-7 to invalidate the July 2023 amendment that barred courts from applying the extreme-unreasonableness doctrine to elected officials. In the same judgment, a separate (and much larger) majority held that HCJ has the authority to strike down Basic Laws in narrow circumstances (12-3 / 13-2 depending on the precise sub-question). Do NOT cite the 8-7 vote for the Basic-Laws authority point.
2. *Judicial Selection Committee reform (Knesset law of 2025-03-27).* Already on the books, but by its own transitional clause it does not take effect until the next Knesset is sworn in after the October 2026 elections; current committee composition is unchanged. An 11-justice HCJ panel is scheduled to hear the consolidated petitions on **June 21, 2026**.
3. *Judicial Overhaul Redux (active 2026 legislative push).* Multiple new bills are mid-process: an AG split bill (separate Prosecutor General and Government Representative to Courts, both political appointments); subordination of ministerial legal advisers to political directors-general; politicization of the Police Internal Investigations Department (Mahash) and the Civil Service Commissioner appointment. None of these are law yet, but any answer about who has legal-advisory authority must flag the in-flight status.

Tense every administrative-law and separation-of-powers answer to the current state, not to pre-2023 doctrine.

## Instructions

### Step 1: Understand the Legal Question
Classify the query:
- **Legislation lookup:** Which law or regulation applies?
- **Concept explanation:** What does a Hebrew legal term mean?
- **Procedure guidance:** What court, what process, what deadlines?
- **Document preparation:** Structure for a contract, claim, or notice?
- **Rights inquiry:** What are someone's rights in a given situation?

### Step 2: Identify the Area of Law
Israeli law is organized by area:
| Area | Key Legislation | Hebrew |
|------|----------------|--------|
| Constitutional | Basic Laws | Chukei Yesod |
| Contract | Contracts Law (General Part) 1973 | Chok HaChozim |
| Employment | Employment laws bundle | Chukei Avoda |
| Real Estate | Land Law 1969, Planning Law 1965 | Chok HaMikrkain |
| Corporate | Companies Law 1999 | Chok HaChevarot |
| Consumer | Consumer Protection Law 1981 (with multiple amendments including recent updates for digital commerce) | Chok Haganat HaTzarchan |
| Privacy | Privacy Protection Law 1981 (last major reform: Amendment 13, in force August 14, 2025: independent Privacy Protection Authority enforcement; mandatory DPO triggers with a compliance grace period that ended 2025-10-31; "prompt" PPA notification of severe security incidents (the statute does NOT use the GDPR 72-hour wording); administrative fines on controllers in the NIS 1,000-320,000 per-offense range, doubled in severe cases, with a separate per-data-subject statutory-damages component up to NIS 100,000 without proof of harm. First published enforcement: HOT, NIS 70,000) | Chok Haganat HaPratiut |
| Torts | Torts Ordinance (New Version) | Pkudat HaNezikin |
| Family | Various personal status laws | Dinei Mishpacha |
| Tax | Income Tax Ordinance, VAT Law | Pkudat Mas Hachnasa, Chok Maam |
| Administrative | Administrative Courts Law 2000 | Chok Batei Mishpat LeInynaim Minhaliyim |

### Step 3: Research and Present
When researching:
1. Start with the primary legislation (the "chok" or "pkuda")
2. Note relevant amendments (tikunim) and their dates
3. Reference key court rulings (psikot din) if relevant
4. Explain in plain language first, then provide Hebrew legal terms
5. Link to public sources when available (Knesset website, Kol Zchut)

### Step 4: Provide Context
For every legal research response:
- State which law(s) apply and their section numbers (saifim)
- Note if the law has been recently amended
- Mention if there are pending legislative changes
- Suggest specific sections of Kol Zchut for free detailed information
- Recommend consulting an orech din for specific cases

## Hebrew Legal Terminology Reference
| Hebrew | English | Context |
|--------|---------|---------|
| chok | law/statute | Primary legislation by Knesset |
| pkuda | ordinance | Pre-state legislation still in force |
| takana | regulation | Secondary legislation by minister |
| psak din | court ruling | Binding precedent |
| bagatz | High Court of Justice | Supreme Court sitting as HCJ |
| tvia | claim/lawsuit | Filing a legal action |
| ktav tvia | statement of claim | Opening document in civil case |
| ktav hagana | statement of defense | Defendant's response |
| orech din | attorney/lawyer | Licensed legal practitioner |
| roeh cheshbon | accountant | Certified public accountant |
| notar | notary | Public notary |
| saif | section | Section of a law |
| saif katan | subsection | Subsection of a law |

## Examples

### Example 1: Employment Rights Question
User says: "What severance pay is an employee entitled to in Israel?"
Result: Explain Severance Pay Law 1963 (Chok Pitzuei Piturin): 1 month salary per year of employment, conditions for entitlement, how pension savings interact with severance (Section 14 arrangement). Recommend Kol Zchut page and consulting an employment lawyer.

### Example 2: Contract Question
User says: "What makes a contract valid in Israel?"
Result: Explain Contracts Law (General Part) 1973: offer (hatzaa), acceptance (kibul), consideration not required in Israeli law (unlike common law), good faith requirement (tom lev), void vs. voidable contracts.

### Example 3: Starting a Business
User says: "What legal structure should I use for a startup in Israel?"
Result: Compare options: Chevra Baam (Ltd company), Shutfut (partnership), Osek Morsheh/Patur (sole proprietor). Explain Companies Law 1999 requirements, registration with Companies Registrar (Rasham HaChevarot).

## Bundled Resources

### Scripts
- `scripts/legal_term_lookup.py`, Interactive Hebrew legal terminology database with 40+ terms covering courts, legislation types, legal proceedings, professionals, contract law, employment law, and property law. Supports single-term lookup, area-filtered listing, and full dictionary display. Run: `python scripts/legal_term_lookup.py --help`

### References
- `references/legal-databases-guide.md`, Comprehensive guide to Israeli legal research databases including paid platforms (Nevo, Takdin, Psakdin) and free resources (Knesset portal, Court rulings portal, Kol Zchut, Bituach Leumi). Consult when the user needs to find legislation text, court rulings, or rights information and you need to recommend the right source.
- `references/legislation-index.md`, Index of key Israeli legislation organized by area (constitutional, contract, employment, corporate, real estate, consumer, tort, privacy, tax, criminal, administrative) with Hebrew names, key section numbers, and practical notes. Consult when you need to identify which specific law applies to a user's question.

## Gotchas

- Israeli laws are referenced by their Hebrew year of enactment (e.g., תשמ"א / tashma"a = 1981; תשמ"ב / tashma"b = 1982), not the Gregorian year. Agents may cite the wrong law when searching by year number alone.
- The Israeli legal system is a mixed system (not pure common law or civil law). Agents trained on US/UK case law may incorrectly assume binding precedent rules or jury trials, neither of which apply in Israel.
- Kol Zchut (All Rights) is the authoritative free legal information wiki in Israel, not Wikipedia. Agents may link to generic sources instead of kol-zchut.org.il for Israeli rights information.
- Israeli court decisions are cited by case number and court (e.g., "bagatz 1234/05"), not by party names as in US law. Agents may generate incorrect citation formats.
- Many Israeli laws from the British Mandate era (pkudot) are still in force. Agents may assume pre-1948 legislation is obsolete when it is not.
- The 2024-01-01 HCJ judgment had TWO separate votes. The 8-7 vote struck down the reasonableness amendment. A separate (larger) majority (12-3 / 13-2 depending on the sub-question) held that HCJ has authority to strike down Basic Laws in narrow circumstances. Agents routinely conflate the two and cite "8-7" for the Basic-Laws-review authority point. Cite each holding to its own count.
- Contract-interpretation doctrine in Israel shifted with the Apropim reversal (2025-2026); pre-Apropim case law that treated subjective intent as co-equal with text is no longer the safe default. Verify before relying on older contract-interpretation precedent.
- Status of the 2025 Judicial Selection Committee reform: the law passed Knesset on 2025-03-27 but does NOT take effect until the next Knesset is sworn in after the October 2026 elections. Treat current committee composition as unchanged when answering questions about who appoints judges today.
- Several 2026 "judicial-overhaul-redux" bills (AG split into Prosecutor General + Government Representative; ministerial legal advisers reporting to political DGs; Mahash politicization; Civil Service Commissioner appointment without competition) are MID-PROCESS. Do not present them as enacted law.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Knesset legislation portal | https://main.knesset.gov.il/Activity/Legislation/ | Primary Israeli legislation, amendments (tikunim) |
| Kol Zchut | https://www.kolzchut.org.il | Rights and benefits wiki in Hebrew, Arabic, English |
| Nevo | https://www.nevo.co.il | Comprehensive (paid) Israeli legal database |
| Takdin | https://www.takdin.co.il | Alternative (paid) legal database |
| Bituach Leumi (NII) | https://www.btl.gov.il | Social security benefits, entitlements and appeals |

## Troubleshooting

### Error: "Cannot access Nevo/Takdin"
Cause: These are paid databases requiring subscription
Solution: Use free alternatives: Knesset legislation portal, Court rulings portal, Kol Zchut wiki. Note that free sources may not be as comprehensive.

### Error: "Law may have been amended"
Cause: Israeli laws are frequently amended; information may be outdated
Solution: Always recommend verifying current version on Knesset website or Nevo. Note the last known amendment date.
