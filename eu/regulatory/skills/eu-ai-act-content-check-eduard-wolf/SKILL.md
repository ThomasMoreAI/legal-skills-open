---
name: eu-ai-act-content-check-eduard-wolf
title: EU AI Act content check (Article 50)
description: 'Use before publishing or deploying web content, articles, images, audio or video created with AI assistance: checks which EU AI Act Article 50 transparency duties apply (deepfake labelling, public-interest text disclosure, editorial-review exception) and prepares the editorial review record for the git-native gate.'
author: eduard-wolf
author_url: https://github.com/eduard-wolf/eu-ai-act-content-transparency/tree/main/plugins/eu-ai-act-content-check/skills/eu-ai-act-content-check
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: eu
practice: regulatory
language: en
---

# EU AI Act content check (Article 50)

> ⚠️ **Not legal advice.** This skill is a technical and editorial working aid. The European Commission's guidelines
> (C(2026) 5054 final, 20 July 2026) are legally non-binding; only the CJEU can interpret Regulation (EU) 2024/1689
> with binding effect. There is no case law on Article 50 yet — this builds a defensible position, not a safe
> harbour. **As of: 24 August 2026.**

Article 50 has applied since 2 August 2026 (guidelines para 153). Below, "para" always means a paragraph of
C(2026) 5054 final. Chapter names refer to files in this repository; if only this skill folder was copied, the tree
below still stands on its own. Those chapters — and this file — are labelled as AI-generated: they were produced by
AI agents without editorial review by a human with relevant subject-matter expertise, so the exception of Art. 50(4),
second subparagraph is not claimed for them; `PROVENANCE.md` records what was verified and what was not.

**Two sentences to carry through every check:**

- The editorial exception is **text only**. For images, audio and video there is none — there only the deepfake test
  decides, and the art exception merely relaxes the **form** of disclosure (Art. 50(4); paras 119–123, 133). A
  deepfake stays labelled no matter how carefully a human reviewed it.
- Mnemonic: **text asks "who checked it?" — image asks "does it look real?"**

Run before content is published, deployed, handed to a client or merged into a publishing branch — once **per content
item** (a page with one text and three images is four checks), and again whenever a reviewed item changes.

## The tree (8 steps, 0-7, self-contained)

**Step 0 — Exposure and audience.** Art. 2(10) removes only the **deployer** obligations of natural persons acting
purely personally **and** non-professionally; provider duties (including the Art. 50(2) machine-readable marking) and
other Union and national law stay untouched (para 20). So a private use never ends the check here — go on to Step 1
(are *you* the provider of the system?) and to Step 7. Any activity yielding regular economic benefit or done in a
professional, business, trade or freelance capacity counts as professional (para 19) — a monetised channel is in
scope. The duty holder is whoever has authority over the deployment and its outputs; employees, contractors and
commissioned agencies are not separate deployers (paras 12, 14). Then split by modality: **text** duties require
publication (Step 3), **deepfake** duties do **not** — para 112 lists only AI system + professional use + deepfake +
no law-enforcement exception, and the example catalogue expressly includes an internal *"AI-generated video featuring
a realistic synthetic avatar of a company CEO congratulating employees …"* (box after para 116). So internal deepfakes
are labelled too. The yardstick is the reasonably foreseeable audience (para 115): a subscriber-only area or a
corporate newsletter does not force a broad-public assumption, but if children or people with low AI literacy are
foreseeably in the audience, deception towards *them* counts.

**Step 1 — Direct AI interaction?** Chatbot, voicebot, AI hotline, agent → Art. 50(1) disclosure, unless the AI nature
is obvious to a reasonably well-informed, observant and circumspect person. The duty addresses the **provider** (para
28). You are the provider if you developed the bot in-house and put it into service under your own name, or if you
**modified** a bought-in system (in the example *"with new training data"*) and afterwards put it into service under
your own name (Art. 3(3); paras 10, 11). An unmodified bought-in bot leaves the duty with its maker — check in your
own embedding that the notice really appears, and put it in the contract (`playbook/en/05-agencies-and-contracts.md`). The
notice belongs **in the conversation at first interaction**, not in an imprint, manual or terms of use (Art. 50(5);
paras 33, 142, 143); agents must disclose both their artificial nature and on whose behalf they act (para 31). This
step never ends the check — Art. 50(1) and (4) can apply cumulatively (para 8), so continue with the content itself.

**Step 2 — Image / audio / video: the deepfake test.** Four cumulative criteria (para 113, from Art. 3(60)):

1. **appreciable resemblance** to the simulated subject (recital 134);
2. the subject **exists, could plausibly exist, or could plausibly have existed** — invented photorealistic humans and
   avatars included, representations breaking laws of nature or biology excluded;
3. the subject is a **person, object, place, entity or event** — incl. digital replicas, realistic AI avatars and
   personas, voice, behaviour, performances, buildings, consumer goods, depicted services;
4. it **would falsely appear authentic or truthful** — judged objectively from resemblance, claim, context and
   foreseeable audience; **no intent to deceive is required**, photorealism alone is *"not determinative"* (para 114).

One criterion missing → no deepfake (illustration, cartoon, evidently surreal scene, instrumental music bed depicting
no reality). *Trivial-edit gate (para 116):* insignificant interventions on pre-existing material create no deepfake —
*"editing background details (e.g. removing passerby)"*, lighting, audio parameters, colour correction, noise removal,
accessibility improvements, compression, cosmetic adjustments; in product advertising and packaging also background
extensions, *"replacements of backgrounds for clearly aesthetic purposes"*, arrangements of existing products,
re-scaling. It flips when the manipulation misleads about the **product or subject itself**, or when **journalistic
images** are edited *"beyond standard technical, editorial practices"*. *Art gate (paras 119–123):* evidently
artistic, creative, satirical or fictional works stay under the duty — only the **form** relaxes to *"an appropriate
manner that does not hamper the display or enjoyment of the work"*. *"Evidently"* is narrow, ambiguous content falls
out, on mixed character *"the informative character should always prevail"* (para 122), and Art. 50(5) timing still
applies (para 123).

**Step 3 — Text: published?** *"Published"* = accessible to an indeterminate, fairly large number of unrelated
potential readers, whether or not against payment (para 131 i). Out: private and professional one-to-one
correspondence, closed small groups, organisation-internal texts, and a chatbot answer seen only by the person who
asked. The **publication** date decides, not the generation date (para 154). No → no text duty, go to Step 7.

**Step 4 — Text: matter of public interest?** Para 131 iii lists politics and democratic processes, administration and
public services, justice and law enforcement, fundamental rights, public security, **health**, environmental
protection, **consumer safety**, and any economic, financial, political, scientific or cultural development that may
be a relevant subject of public debate. Very short texts conveying no knowledge, opinion or fact fall out
(para 131 ii). Advertising and product copy are out — **but** expressly *"not including any claims related to e.g.
health, consumer safety or sustainability"*, which puts such copy back in. No → no text duty, go to Step 7.

**Step 5 — Text: the editorial exception (Art. 50(4) subpara 2).** Two **cumulative** conditions (para 133): (1) human
review or editorial control — *"deliberate examination of the substance"* by people with relevant knowledge and
professional judgement, where *"Fact-checking the accuracy of the content is a minimum requirement"* (para 134); (2) a
named natural or legal person holding **ultimate legal responsibility**, whose identity and contact details are
publicly findable (para 138). Not sufficient (para 135): spell- and grammar-checking, the mere existence of an
editorial policy, automated review ("AI reviews AI"), cursory approval without substantive engagement. Met → no label,
but keep the evidence (review record below). Not met → label required — for the labelling path as a whole (when it
is the right choice, the label line, placement, provenance page, as-of date) see `playbook/en/09-labelling-path.md`.

**Step 6 — Form of the label.** See "If a label is required" below and `playbook/en/04-labelling-form.md`.

**Step 7 — Neighbouring duties.** A label is no free pass: unfair-competition (UWG) misleading claims, copyright, data
protection and personality rights remain untouched (para 124; footnotes 32, 34). Platform policies and the DSA apply
alongside. Report these as a note, never as clearance.

## Output: one verdict per content item

```
[file or item]  —  DUTY | NO DUTY | GREY ZONE
Modality:   text | image | audio | video | interactive
Reason:     one or two sentences, in the words of the test that decided it
Anchor:     Art. 50(…) / para …
Next step:  concrete label proposal, or review record, or "nothing to do"
```

- **DUTY** — name the criterion that is met. **NO DUTY** — name the criterion that fails, e.g. "criterion 4 not met:
  stylised infographic, no claim to authenticity (para 113 iv, 114)".
- **GREY ZONE** — flag with ⚠️ and the standing sentence: *grey zone — record the classification with a short
  justification (see `gate/`)*. Never resolve a grey zone silently in either direction; it is a human judgement call
  and the written justification is what makes it defensible. Recurring ones: object removal and background swaps
  (para 116), advertising vs. public-interest information (para 131 iii), half-open distribution lists (para 131 i),
  what counts as a "substantive" AI edit after sign-off (para 136).
- Anchors must be exact. If no source covers the case, write `[zu verifizieren: …]` and say so — never invent a
  paragraph number, a judgment or a file number.

## If a label is required

Match the label language to the content language. Full library incl. the optional EU icons:
`playbook/en/04-labelling-form.md`.

| Case | DE | EN |
|---|---|---|
| Chatbot / direct interaction | „Sie chatten mit einem KI-Assistenten." | "You are chatting with an AI assistant." |
| Image deepfake | „KI-generiertes Bild" · „Mit KI verändertes Bild" | "AI-generated image" · "AI-modified image" |
| Fully synthetic video | „Dieses Video enthält KI-generierte Bild- und Sprachsequenzen." | "This video contains AI-generated visuals and speech." |
| Partly manipulated video | „Einzelne Bild- oder Sprachsequenzen dieses Videos wurden mit künstlicher Intelligenz verändert." | "Parts of this video's visuals or speech have been modified using artificial intelligence." |
| Audio deepfake (audible) | „Dieser Beitrag enthält eine KI-generierte Stimme." | "This recording contains an AI-generated voice." |
| Labelled text | „Dieser Text wurde mit künstlicher Intelligenz erstellt." | "This text was generated using artificial intelligence." |

**Label line for text — three rules** (`playbook/en/09-labelling-path.md`, section 3). The line is a statement of
origin, not a quality verdict; it carries at most three kinds of statement, and only two belong in it.
(1) **Mandatory core — the origin statement:** that the text *"has been artificially generated or manipulated"*
(Art. 50(4) subpara 2), *"clear and perceivable by natural persons (e.g. visible or audible measures) without them
needing to rely on any specific technical tools or performing dedicated actions"* (para 132) — no wording is
prescribed and the EU icon is optional. (2) **True process facts are allowed — if true:** "not editorially reviewed",
"machine-checked against the sources" or "as of <date>" may be added because they shape what readers may legitimately
expect, but each must be backed by a real run (the date comes from the last substantive generation or check run,
never from a build, deploy or layout commit), since, on this playbook's reading, an untrue process statement is a
statement about an essential characteristic of the service and open to attack as misleading (§ 5(2) no. 1 UWG,
German unfair-competition law; whether that reference point holds for free content is undecided, and no ruling
specifically on process statements is on record) — a wrong as-of date is worse than none. (3) **No
self-evaluative claims:** "professionally created", "by AI experts" or "high-quality" are advertising claims about
the trader's qualifications and the service (§ 5(2) no. 3 and no. 1 UWG), not origin statements — they stay out of
the line, as do norm citations (para 142 asks for information that is *"noticeable, easy to understand by and
accessible for the natural person concerned"*), and evidence belongs on the provenance page the line links to. Where
the label path is taken because the competence test in Step 5 fails, draft **no** review record — a record without a
substantive review documents a false statement (this playbook's reading of para 135); note the decision in one
sentence instead ("labelled because the competence test for this topic came out negative").

**Placement** — clear and distinguishable, at the latest at first exposure, with no click, hover or tooling required
(Art. 50(5); para 142): **image** into the image itself where no overlay covers it, then check the responsive crops;
**video** at the start and repeated, at minimum after interruptions; **audio** audibly before the content starts — a
note in the description does not label the audio; **text** above or at the top, near the headline. Terms of use,
footers, metadata and menu layers do not qualify (para 142). Those placement specifics come from the **Code of
Practice on Transparency of AI-Generated Content**, Sec. 2 — image: Sub-measure 1.2.2 lit. a; video: Sub-measure 1.2.2
lit. b; audio: Measure 1.1 with Sub-measure 1.2.3; text: Sub-measure 1.2.2 lit. f. The code binds only its
signatories; non-signatories must demonstrate compliance *"through other adequate means"* and are expected to run a
gap analysis against it (paras 147, 148). What the guidelines themselves carry is the reason for repeating: where it
is foreseeable that people do not perceive the content from its beginning, a disclosure at the start alone *"should be
complemented with disclosure at later moments, where possible"* (para 143). Two standing warnings: the provider's
machine-readable marking under Art. 50(2) **never** replaces your own perceivable label — deployers *"cannot rely on
the machine-readable marking"* (para 117); and a platform AI toggle can carry the disclosure only *"within the context
of the VLOP or VLOSE used"*, never for re-use on your own site or after a repost (para 126).

## If the editorial exception is claimed: draft the review record

Write `<name>.review.json` next to `<name>.md`. Prefill only what you can know; leave every field that attests a human
act empty. **The draft is deliberately incomplete — running the gate on it MUST fail until a human completes it. That
is the expected state, not a bug.**

```json
{
  "content_path": "examples/blog-artikel.md",
  "content_sha256": "",
  "reviewed_at": "",
  "reviewer": { "name": "", "role": "", "fachkompetenz": "" },
  "editorial_responsibility": { "traeger": "", "kontakt_oeffentlich": "" },
  "pruefung": { "faktencheck": false, "quellen_geprueft": false, "aenderungen_vorgenommen": "" },
  "scope": {
    "einstufung": "Veröffentlicht (Rn. 131 i) und öffentliches Interesse bejaht (Rn. 131 iii, Gesundheitsaussage) — Kennzeichnungspflicht dem Grunde nach, redaktionelle Ausnahme wird geltend gemacht.",
    "labels_erforderlich": [],
    "begruendung": "Zwei bis drei Sätze: warum diese Einstufung, welche Grauzone bewusst wie entschieden wurde."
  },
  "ki_beteiligung": "Konkret: welches Modell/Tool, für welchen Schritt (Rohentwurf, Umformulierung, Übersetzung, Zusammenfassung), was davon im veröffentlichten Stand steht."
}
```

- **You fill in:** `content_path` (POSIX path to the content file, normally relative to the repository root),
  `scope.einstufung`, `scope.labels_erforderlich`, `scope.begruendung`, `ki_beteiligung` — the classification and your
  own AI use. Leave `editorial_responsibility.traeger` empty even where the repository appears to name the bearer —
  naming who carries the ultimate legal responsibility is the human's act, not a classification.
- **Only the human fills in:** `content_sha256`, `reviewed_at`, all `reviewer` fields, both
  `editorial_responsibility` fields (`kontakt_oeffentlich` = the publicly findable location, e.g. the imprint URL,
  para 138) and the whole `pruefung` object. `false` means "not attested" — a human flips a boolean to `true` only
  after actually doing the work. Field types and patterns: `gate/review-record.schema.json`.

**Hand the human these instructions:**

1. Review the substance: check the facts (the legal minimum, para 134), verify the sources, change or reject what does
   not hold. Spell-checking, waving it through, or having a model check the model does not qualify (para 135).
2. Enter your name, role and the subject-matter competence that qualifies you, the review date, and the bearer of
   editorial responsibility with a publicly findable contact (para 138). Set the `pruefung` booleans to what is true.
3. Compute the hash **last**, over the raw bytes of the final file, and paste it into `content_sha256`:
   `shasum -a 256 <file> | cut -d' ' -f1` (macOS) · `sha256sum <file> | cut -d' ' -f1` (Linux).
4. Run the gate: `node gate/scripts/check-review-record.mjs <dir>` — green means the record is complete and bound to
   exactly this version of the file.

## Never do these

- **Never attest a human review.** Do not enter a reviewer name, do not fill either `editorial_responsibility` field,
  do not set `faktencheck` or `quellen_geprueft` to `true`, do not fill `reviewed_at`, do not compute the final hash
  into the record yourself. A record produced end-to-end by an agent is exactly the *"automated review process"* that
  para 135 rules out — it would document a breach instead of compliance.
- **Never edit content after the review.** Para 136: *"Any substantive AI intervention occurring after the human
  review or editorial control process has taken place will therefore cause the exception to become void."* If you
  rewrite, shorten, translate, summarise or regenerate a headline or teaser on a reviewed file, the record is void and
  a human must review again; the gate's hash binding enforces it by turning CI red. Purely technical steps (minify,
  format conversion, encoding fix) do not change the substance — where exactly the line runs is a grey zone, so say so
  instead of deciding it away. If something must change, say so plainly and ask for re-review. Never update the hash
  to make the gate pass.
- **Never present the result as legal advice or as compliance.** The gate enforces the **process** and makes it
  auditable; it does not enforce the quality of the review. It is a documentation form going beyond the legal minimum
  and expressly permitted (Code of Practice on Transparency of AI-Generated Content, Sec. 2, Commitment 4) — **not a
  safe harbour**.

## Where to read further

In this repository: decision tree `playbook/en/01-decision-tree.md` · classified cases `playbook/en/02-case-catalog.md` ·
editorial exception `playbook/en/03-editorial-exception.md` · label form `playbook/en/04-labelling-form.md` ·
commissioned work `playbook/en/05-agencies-and-contracts.md` · common errors `playbook/en/06-myths-faq.md` · watermarks
`playbook/en/07-provider-marking.md` · official sources `playbook/en/08-legal-basis.md` · labelling path
`playbook/en/09-labelling-path.md` · the gate `gate/README.md`. From this file: [playbook](../../../../playbook/en/01-decision-tree.md) · [gate](../../../../gate/README.md).
