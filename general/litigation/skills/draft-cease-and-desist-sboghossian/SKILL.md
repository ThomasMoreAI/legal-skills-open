---
name: draft-cease-and-desist-sboghossian
title: Draft — Cease and Desist Letter
description: Use when asked to draft a cease-and-desist (C&D) letter demanding that a recipient stop specified infringing, wrongful, or harmful conduct. Covers the most common C&D use cases — trademark/IP infringement, defamation, breach of contract, harassment, and unfair competition — with a complete document structure, tone guidance, jurisdictional enforceability notes for MENA and common-law systems, and the DMCA cross-reference for online infringement.
author: sboghossian
author_url: https://github.com/sboghossian/mini-claude-for-legal/tree/main/skills/draft/draft-cease-and-desist
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: litigation
language: en
---

# Draft — Cease and Desist Letter

## When to use this

Use this skill to draft a cease-and-desist letter when a party needs to:
- Stop ongoing intellectual property infringement (trademark, copyright, patent, trade secret).
- Halt defamatory, libelous, or slanderous statements.
- Require cessation of a continuing contract breach.
- Stop harassment or unlawful conduct.
- Warn against unfair competition or passing off.

A C&D letter is usually the first formal legal step before litigation or arbitration. It creates a record that the infringer had notice (relevant to damages, especially in IP cases), provides an opportunity for voluntary compliance (avoiding cost and delay), and may preserve negotiating leverage for a settlement.

**Note**: A C&D letter is not a guarantee of rights — it is a demand. The letter may become evidence in subsequent proceedings, so tone and accuracy matter.

## Required inputs

| Input | Notes |
|---|---|
| Sender identity | Is counsel sending on behalf of a client, or the rights-holder directly? |
| Rights-holder identity (if different from sender) | Full legal name, trademark/copyright registration details if relevant |
| Recipient identity | Full legal name and address |
| Infringing / wrongful conduct | Specific acts, dates, channels, evidence |
| Legal basis | Registered trademark, copyright, contract clause, statute |
| Demands | What must the recipient do, and by when |
| Deadline | Clear calendar date for response / compliance |
| Jurisdiction | Governs tone and legal basis |

## Document structure

```
[Letterhead of sender / law firm]
[Date]
[Recipient full name and address]

Re: CEASE AND DESIST — [Brief description, e.g., "Infringement of Trademark 
Registration No. [X]" / "Defamatory Statements Regarding [Rights Holder]"]

PRIVATE AND CONFIDENTIAL — WITHOUT PREJUDICE

Dear [Recipient Name / "Sir or Madam"],

I. AUTHORITY AND REPRESENTATION
   [If from counsel:] "We are legal counsel to [Rights Holder] 
   ("Our Client") and write on their instructions."
   [If directly:] "[Company Name] writes this letter directly."

II. STATEMENT OF RIGHTS
   Our Client is the [owner / exclusive licensee] of:
   - [Registered Trademark / Copyright / Patent / Trade Secret / 
     Contract right] [description with registration details if available].
   - [Registration number, jurisdiction, classes (for trademarks)]
   - [Date of first use / registration date]
   Our Client has invested substantially in building the value and 
   reputation associated with [the mark / the work / the confidential 
   information].

III. INFRINGING / WRONGFUL CONDUCT
   It has come to Our Client's attention that you are [engaging in / 
   have engaged in] the following acts which infringe Our Client's rights:
   - [Specific act 1: e.g., "using a mark identical or confusingly similar 
     to Our Client's registered trademark in connection with [goods/services] 
     at [website/location], as documented in the annexed screenshot dated 
     [DATE]"]
   - [Specific act 2]
   [Include exhibits / screenshots / URLs as annexures to the letter]

IV. LEGAL BASIS
   Your conduct constitutes:
   [Select applicable:]
   - Trademark infringement under [applicable law];
   - Copyright infringement under [applicable law];
   - Defamation / libel under [applicable law];
   - Breach of [Agreement Name] dated [DATE], specifically Clause [X];
   - Passing off / unfair competition under [applicable law];
   - [Other].
   
   [Brief, accurate statement of why the conduct is infringing — do not 
   overstate or make claims not supported by the evidence.]

V. DEMANDS
   We demand that you, within [10 / 14 / 21] calendar days from the 
   date of this letter:

   1. IMMEDIATELY CEASE all use of [the infringing mark / content / 
      conduct described above].
   2. CONFIRM IN WRITING to the undersigned, within the stated period, 
      that you have ceased the conduct and will not resume it.
   3. [For IP infringement:] DESTROY or deliver to us all infringing 
      materials, products, and packaging bearing the infringing mark / 
      content.
   4. [For IP infringement:] PROVIDE an accounting of all revenues 
      derived from the infringing activity.
   5. [For defamation:] PUBLISH a retraction / correction of the 
      defamatory statement on [platform], in terms to be agreed with 
      Our Client.
   6. [For continuing breach:] REMEDY the breach by [specific action].

VI. CONSEQUENCES OF NON-COMPLIANCE
   If you fail to comply with these demands by [DEADLINE DATE], Our 
   Client reserves all rights and remedies, including without limitation:
   - Commencing legal proceedings against you for [injunctive relief / 
     damages / account of profits / other appropriate relief];
   - Seeking an emergency interim injunction;
   - Referring the matter to [relevant regulatory authority / customs 
     authority for border measures];
   - Claiming costs and legal fees.
   
   Our Client intends to act swiftly if these demands are not met.

VII. RESERVATION OF RIGHTS
   Nothing in this letter shall constitute a waiver of any of Our 
   Client's rights or remedies, all of which are expressly reserved.

Yours faithfully,

[Signature]
[Name]
[Firm / Direct contact]
[Reference number]

ANNEXURES:
  Exhibit A: [Evidence of rights — trademark certificate / copyright 
              registration / contract]
  Exhibit B: [Evidence of infringing conduct — screenshots, URLs, 
              photographs]
```

## Tone guidance

A C&D letter walks a line:
- **Firm**: the demands must be unambiguous; do not hedge the central ask.
- **Professional**: aggressive or abusive language weakens the letter's credibility if it becomes evidence and may expose the sender to counterclaims.
- **Accurate**: do not overstate the strength of the rights or the extent of the infringement. Courts and opposing counsel will scrutinize the letter; exaggerations undermine credibility.
- **Without prejudice** marker (where applicable): use "Without Prejudice" on letters that include settlement offers or admissions; absent a settlement offer, the letter can be marked "Private and Confidential" but need not be "Without Prejudice."

## IP-specific notes

### Trademark infringement
- State the registration number, jurisdiction, and classes of goods/services.
- Note the likelihood-of-confusion basis if the marks are not identical.
- For domain names: consider UDRP (WIPO Arbitration and Mediation Center) as a parallel fast-track remedy.
- Attach the trademark certificate as an exhibit.

### Copyright infringement
- Copyright subsists automatically in most jurisdictions (no registration required).
- In jurisdictions with registration (US, KSA): state the registration number.
- Specify the exact copyrighted work(s) and where the infringing copy is found.
- For online infringement: see [[draft-takedown-dmca]] for the DMCA notice procedure (US platforms).

### Patent infringement
- **Caution**: incorrect patent infringement assertions can expose the sender to a declaratory judgment action (in the US) or antitrust/unfair competition claims.
- Do not send a patent C&D without a freedom-to-operate opinion or strong professional review.
- State the patent number, jurisdiction, and the specific claims arguably infringed.
- A "notice of infringement" stops the infringer from claiming innocent infringement damages.

### Trade secret misappropriation
- Do not describe the trade secret in detail in the letter (that would disclose it further).
- Identify it by category: "our client's proprietary customer database / algorithm / manufacturing process."
- Reference the confidentiality agreement if one was in place.

## Jurisdictional notes

### UAE onshore
- C&D letters are common pre-litigation steps; courts expect them.
- For trademark infringement: UAE Federal Law on Industrial Property (Decree-Law 36/2021) — note trademark registration with Ministry of Economy.
- For copyright: UAE Federal Law on Intellectual Property (Federal Law 7/2002 as amended).
- C&D letter followed by filing a complaint with the IP Section of the Ministry of Economy is an administrative route.

### DIFC / ADGM
- English common-law principles; C&D letters follow UK practice.
- Interim injunctions (search orders, freezing orders) available from DIFC/ADGM Courts on short notice.

### KSA
- IP enforcement: Saudi Authority for Intellectual Property (SAIP).
- C&D letter sends a notice; follow with a complaint to SAIP or before the Commercial Court.
- Defamation claims are taken seriously; statements on social media can be criminal under Cybercrime Law.

### Lebanon
- IP: Intellectual Property Law (Law 75/1999); trademark registration with Ministry of Economy and Trade.
- Defamation: Criminal Code provisions; civil claim under Civil Code.

### US
- Copyright: DMCA takedown notice for online platforms is often faster than a C&D to the infringer.
- Patent: be aware of Inter Partes Review (IPR) and declaratory judgment risks before sending.
- Defamation: state law governs; truth is an absolute defense; opinion generally protected.

## Common mistakes

- **Vague demands**: "stop your infringing activities" is not a demand — specify exactly what must stop, what must be delivered, and by when.
- **Wrong legal basis**: asserting copyright infringement when what exists is a breach-of-contract claim (or vice versa) misleads the recipient and weakens the letter.
- **No evidence exhibits**: a C&D without supporting evidence is easily ignored.
- **Unreasonable deadline**: 2-3 days is typically unreasonable for a C&D response; 10-21 days is standard; enough time to compel compliance but short enough to maintain urgency.
- **Sending to the wrong person**: ensure the letter reaches the actual decision-maker at the infringing entity; registered agent addresses alone are insufficient.

## Related skills

- [[draft-arbitration-request]]
- [[draft-boilerplate-clauses]]
- [[review-contract-general]]
- [[draft-takedown-dmca]]
