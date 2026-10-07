# Citation pack

Every risk factor in `risk_taxonomy.md` traces to one of the sources below. Quoted excerpts are kept short for fair use; pin-cites are provided for verification against the primary source.

Currency: April 2026. Verify all citations against primary sources before relying on them in client work or court filings.

---

## 1. United States v. Heppner — A/C privilege and work product BOTH fail (criminal posture)

**Citation:** *United States v. Heppner*, 25 Cr. 503 (JSR), 2026 U.S. Dist. LEXIS 32697; 2026 WL 436479 (S.D.N.Y. Feb. 17, 2026) (Rakoff, J.).

**Posture:** Criminal. Defendant created ~31 documents memorializing exchanges with Claude after receiving a grand jury subpoena, intending to use them to inform discussions with counsel. Counsel did not direct the use of Claude. The government seized the documents pursuant to a search warrant executed at defendant's home, not via pretrial discovery.

**Holding:** Neither the attorney-client privilege nor the work-product doctrine protects the AI Documents from government inspection.

### Attorney-client privilege analysis

The court applied the three-element test from *United States v. Mejia*, 655 F.3d 126, 132 (2d Cir. 2011): (1) communication between client and attorney, (2) intended to be and in fact kept confidential, (3) for the purpose of obtaining or providing legal advice.

- **Element 1 fails (not a communication with an attorney):** "Because Claude is not an attorney, that alone disposes of Heppner's claim of privilege."
- **Element 2 fails (not confidential):** "the written privacy policy to which users of Claude consent provides that Anthropic collects data on both users' 'inputs' and Claude's 'outputs,' that it uses such data to 'train' Claude, and that Anthropic reserves the right to disclose such data to a host of 'third parties,' including governmental regulatory authorities."
- **Element 3 fails (not for purpose of obtaining legal advice):** Heppner used Claude on his own volition, not at counsel's direction. "Had counsel directed Heppner to use Claude, Claude might arguably be said to have functioned in a manner akin to a highly trained professional who may act as a lawyer's agent within the protection of the attorney-client privilege." (citing *United States v. Kovel*, 296 F.2d 918 (2d Cir. 1961)). Further, Claude itself disclaims giving legal advice.

The court rejected the cloud-software analogy: "all '[r]ecognized privileges' require, among other things, 'a trusting human relationship,' such as, in the attorney-client context, a relationship 'with a licensed professional who owes fiduciary duties and is subject to discipline.' No such relationship exists, or could exist, between an AI user and a platform such as Claude." (citing Ira P. Robbins, *Against an AI Privilege*, JOLT Dig., Harv. L. Sch. (Nov. 7, 2025)).

The court also held that sharing non-privileged AI documents with counsel did not retroactively confer privilege: "non-privileged communications are not somehow alchemically changed into privileged ones upon being shared with counsel." (citing *Gould, Inc. v. Mitsui Min. & Smelting Co.*, 825 F.2d 676, 679–80 (2d Cir. 1987)).

### Work-product analysis

The court held the AI Documents were not protected by the work-product doctrine because (1) they were not prepared "by or at the behest of counsel," and (2) they did not reflect defense counsel's strategy. Counsel conceded the documents "were prepared by the defendant on his own volition" and that while they "affect[ed]" counsel's strategy going forward, they did not "reflect" counsel's strategy at the time created.

### CRITICAL LIMITATION

The Heppner court explicitly did NOT reach the question of work-product protection from discovery under Federal Rule of Criminal Procedure 16(b)(2)(A) or Federal Rule of Civil Procedure 26(b)(3). The government obtained the AI Documents via search warrant, not via discovery requests. This limitation is essential to reconciling Heppner with Warner and Morgan (below).

---

## 2. Warner v. Gilbarco — Work product PROTECTS pro se party's AI use (civil posture)

**Citation:** *Warner v. Gilbarco Inc.*, No. 2:24-cv-12333, 2026 WL 373043 (E.D. Mich. Feb. 10, 2026).

**Posture:** Civil. Pro se plaintiff used ChatGPT in connection with the lawsuit. Defendants moved to compel all documents concerning plaintiff's AI use.

**Holding:** Plaintiff's communications with ChatGPT are protected as work product under FRCP 26(b)(3).

**Key reasoning:**
- AI is a "tool, not a person" — disclosure to ChatGPT is not disclosure to an adversary.
- Work-product waiver requires disclosure "to an adversary or in a way likely to get in an adversary's hand."
- Compelling disclosure of AI interactions "would nullify virtually all work-product protection where a software tool such as ChatGPT is used as a drafting aid."

---

## 3. Morgan v. V2X — Following Warner; AI tool identity IS discoverable

**Citation:** *Morgan v. V2X Inc.*, No. 25-cv-01991-SKC-MDB, 2026 WL 864223 (D. Colo. Mar. 30, 2026).

**Posture:** Civil, pro se.

**Holding:** Following Warner, pro se party's AI tool communications are work-product protected under FRCP 26(b)(3). HOWEVER, the *identity* of the precise AI tools used is NOT protected.

**Distinguishing Heppner:** "[Heppner] at first blush may appear contrary," but it was a criminal case and did not implicate Rule 26(b)(3), which extends work-product protection explicitly to parties.

**On waiver:** "even though AI use technically 'discloses' information to a third party, it is highly unlikely the information will fall into the hands of an adversary absent some legal process to compel it. Thus, AI interactions do not automatically compromise work product protections."

---

## 4. Federal Rules — the textual hook for Warner/Morgan

**FRCP 26(b)(3)(A):** "Ordinarily, a party may not discover documents and tangible things that are prepared in anticipation of litigation or for trial by another party or its representative ... ."

**FRCP 26 Advisory Committee Notes, 1970 Amendment:** "Subdivision (b)(3) reflects the trend of the cases by requiring a special showing, not merely as to materials prepared by an attorney, but also as to materials prepared in anticipation of litigation or preparation for trial by or for a party or any representative acting on his behalf."

**Wright & Miller, Federal Practice & Procedure §2024:** "The 1970 amendment also extended the work product protection to documents and things prepared for litigation or trial by or for the adverse party itself or its agent."

**FRCrimP 16(b)(2)(A):** parallel protection in criminal pretrial discovery for "reports, memoranda, or other documents made by the defendant, or the defendant's attorney or agent, during the case's investigation or defense." (Did not apply in Heppner because government obtained via warrant, not discovery.)

---

## 5. ABA Formal Opinion 512 (July 29, 2024) — the ethics floor

The opinion states that "lawyers using generative artificial intelligence tools must fully consider their applicable ethical obligations, including their duties to provide competent legal representation, to protect client information, to communicate with clients, to supervise their employees and agents, to advance only meritorious claims and contentions, to ensure candor toward the tribunal, and to charge reasonable fees."

### Competence (Model Rule 1.1)

"To competently use a GAI tool in a client representation, lawyers need not become GAI experts. Rather, lawyers must have a reasonable understanding of the capabilities and limitations of the specific GAI technology that the lawyer might use."

"This is not a static undertaking. Given the fast-paced evolution of GAI tools, technological competence presupposes that lawyers remain vigilant about the tools' benefits and risks."

### Confidentiality (Model Rule 1.6)

"Before lawyers input information relating to the representation of a client into a GAI tool, they must evaluate the risks that the information will be disclosed to or accessed by others outside the firm."

"Self-learning GAI tools into which lawyers input information relating to the representation, by their very nature, raise the risk that information relating to one client's representation may be disclosed improperly, even if the tool is used exclusively by lawyers at the same firm."

"Because many of today's self-learning GAI tools are designed so that their output could lead directly or indirectly to the disclosure of information relating to the representation of a client, **a client's informed consent is required prior to inputting information relating to the representation into such a GAI tool.**"

"To obtain informed consent when using a GAI tool, **merely adding general, boiler-plate provisions to engagement letters purporting to authorize the lawyer to use GAI is not sufficient.**"

"As a baseline, all lawyers should read and understand the Terms of Use, privacy policy, and related contractual terms and policies of any GAI tool they use to learn who has access to the information that the lawyer inputs into the tool ... ."

### Communication (Model Rule 1.4)

"Lawyers must disclose their GAI practices if asked by a client how they conducted their work, or whether GAI technologies were employed in doing so, or if the client expressly requires disclosure under the terms of the engagement agreement or the client's outside counsel guidelines."

Client consultation about the use of a GAI tool is also necessary "when its output will influence a significant decision in the representation."

### Candor toward tribunal (Model Rule 3.3) and Meritorious Claims (Rule 3.1)

"Output from a GAI tool must be carefully reviewed to ensure that the assertions made to the court are not false."

"In judicial proceedings, duties to the tribunal likewise require lawyers, before submitting materials to a court, to review these outputs, including analysis and citations to authority, and to correct errors, including misstatements of law and fact, a failure to include controlling legal authority, and misleading arguments."

### Supervision (Model Rules 5.1, 5.3)

"Managerial lawyers must establish clear policies regarding the law firm's permissible use of GAI, and supervisory lawyers must make reasonable efforts to ensure that the firm's lawyers and nonlawyers comply with their professional obligations when using GAI tools."

### Vendor due diligence checklist (cloud/outsourcing analogy applied to GAI)

The opinion endorses these requirements for any GAI vendor relationship:
- Configuration to preserve confidentiality and security; enforceable obligation; breach/process notice
- Investigation of reliability, security measures, policies, and liability limits
- Determination of whether the tool retains submitted information before/after service termination, or asserts proprietary rights
- Recognition that GAI servers may be cyber-attack targets

### Fees (Model Rule 1.5)

Lawyers "may not charge a client to learn about how to use a GAI tool ... that the lawyer will regularly use for clients because lawyers must maintain competence in the tools they use."

---

## 6. Florida-specific overlay

**Fla. Stat. § 90.502** — codifies attorney-client privilege; protects only confidential communications made for the purpose of obtaining legal services. Disclosure to third parties (other than as necessary for legal services) defeats the privilege.

**Fla. Bar Rule 4-1.6** — confidentiality of client information; mirrors Model Rule 1.6.

**Fla. Bar Rule 4-1.1** — competence; recently amended to reflect technology obligations.

**Florida Bar Professional Ethics Op. 24-1 (Jan. 19, 2024):** "[C]onfidentiality concerns may be mitigated by use of an in-house generative AI rather than an outside generative AI where the data is hosted and stored by a third-party."

**Fla. 17th Jud. Cir. AO 2026-03-Gen** and **Fla. 7th Jud. Cir. AO G-2026-045-SC** — require attorneys to disclose and certify the use of AI in court filings; verify accuracy and ethical compliance.

---

## 7. Other persuasive authorities

**DC Bar Ethics Op. 388 (April 2024):** "Most technology companies that provide these [free] services make no secret of what they will do with any information submitted to them in connection with their publicly usable services: from their perspective, user inputs are theirs to use and share as they see fit." Free public versions of GAI products are off-limits for matters involving confidential information.

**California State Bar, Practical Guidance for the Use of Generative AI in the Practice of Law (Nov. 16, 2023):** "A lawyer who intends to use confidential information in a generative AI product should ... ensure that the provider does not share inputted information with third parties or utilize the information for its own use in any manner, including to train or improve its product."

**Pa. & Philadelphia Joint Formal Opinion 2024-200:** flags risk that LLMs "without safeguards similar to those already in use in law offices, such as ethical walls ... may run afoul of Rules 1.7 and 1.9 by using the information developed from one representation to inform another."

**West Virginia Lawyer Disciplinary Board Op. 24-01 (2024):** consistent with ABA 512 on informed consent.

**Stanford RegLab study (Magesh et al., 2024):** leading legal AI tools (Lexis+ AI, Westlaw AI-Assisted Research, Ask Practical Law AI) hallucinate between 17% and 33% of the time. Two failure modes: (a) factually incorrect law; (b) correct law cited to sources that do not actually support the conclusion.

**Fletcher v. Experian Information Solutions, Inc.**, 168 F.4th 231 (5th Cir. Feb. 18, 2026) — sanctions for fabricated AI-generated citations; example of court enforcing Model Rule 3.3 / Rule 11 in the AI context.

---

## How the analyzer uses this pack

The risk taxonomy maps each surface characteristic, content element, and posture fact to one or more entries above. When the analyzer raises a factor, it cites the entry by section number (e.g., "§ 1 — Heppner element 2: not confidential because of Anthropic ToS"). This makes every Pass / Caution / Stop traceable to a primary source.
