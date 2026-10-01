# Prohibited practices — Art 5

Basis: Regulation (EU) 2024/1689 Art 5, as amended by Regulation (EU) 2026/1744 Art 1(7). Commission Guidelines on prohibited artificial intelligence practices, published 4 February 2025 — non-binding; authoritative interpretation reserved to the CJEU.

Applicable since **2 February 2025**, except the two new points, applicable from **2 December 2026**.

Penalty ceiling: EUR 35 000 000 or 7 % of total worldwide annual turnover for the preceding financial year, whichever is **higher** (Art 5 breach, Art 99(3)). For SMEs and SMCs, whichever is **lower** (Art 99(6), (6a)).

A prohibition is not curable by documentation, consent, disclosure or a code of practice. If a screen hits, the feature does not ship.

## The eight original prohibitions

| Point | Practice | Note |
|---|---|---|
| 5(1)(a) | Subliminal techniques beyond a person's consciousness, or purposefully manipulative or deceptive techniques, with the objective or the effect of materially distorting behaviour by appreciably impairing the ability to make an informed decision, causing or reasonably likely to cause **significant harm** | "or the effect" — intent is not required. Significant harm is the limiter |
| 5(1)(b) | Exploiting vulnerabilities due to **age, disability, or a specific social or economic situation**, with the objective or effect of materially distorting behaviour, causing or reasonably likely to cause significant harm | Financial distress and debt status are "specific economic situation" |
| 5(1)(c) | Social scoring: evaluation or classification over a period of time based on social behaviour or known, inferred or predicted personal or personality characteristics, where the score leads to detrimental treatment (i) in unrelated contexts or (ii) disproportionate to the behaviour | Cross-context reuse of a behavioural score is the core wrong |
| 5(1)(d) | Predicting the risk of a natural person committing a criminal offence based **solely** on profiling or on assessing personality traits | Does not cover supporting a human assessment already grounded in objective, verifiable facts linked to criminal activity |
| 5(1)(e) | Creating or expanding facial recognition databases through **untargeted scraping** of facial images from the internet or CCTV footage | Absolute; no law-enforcement carve-out |
| 5(1)(f) | Inferring emotions of a natural person in the areas of **workplace and education institutions** | Exception only where intended for **medical or safety** reasons |
| 5(1)(g) | Biometric categorisation that categorises individuals based on biometric data to deduce or infer race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation | Does not cover labelling or filtering of lawfully acquired biometric datasets, or categorisation of biometric data in law enforcement |
| 5(1)(h) | Real-time remote biometric identification in publicly accessible spaces **for law enforcement**, save three exhaustive objectives, with Art 5(2) to (7) conditions including prior judicial or administrative authorisation and national implementing law | Not a private-sector question in ordinary product work |

## The two 2026 additions — applicable 2 December 2026

Inserted by Reg (EU) 2026/1744 Art 1(7)(a). Recitals 10 and 11 of that regulation give the rationale: "nudification" applications and synthetic child sexual abuse material.

**Art 5(1)(ba)** — placing on the market, putting into service or use of an AI system that generates or manipulates realistic images, videos, audio or similar material of an identifiable natural person's intimate parts, or of an identifiable natural person engaged in sexually explicit activities, **without that person's freely-given, specific, informed, unambiguous and explicit consent** for that generation or manipulation.

**Art 5(1)(bb)** — placing on the market, putting into service or use of an AI system that generates or manipulates material or performance within the meaning of Art 2, points (c) and (e), of Directive 2011/93/EU, except where a "without right" defence applies under national law.

Scoping, Art 5(1a) as inserted:

- **Placing on the market or putting into service** is prohibited only where (i) that generation or manipulation is the **intended purpose** of the system, or (ii) the system's design, training, architecture, capabilities or user-facing functionalities make that generation a **reasonably foreseeable and reproducible outcome without significant technical modification**, and the system lacks reasonable and adequate technical safety measures and other safeguards to reliably prevent it, taking account of reasonably foreseeable misuse, and to correct observed or reported misuse.
- **Use** is prohibited only where the deployer uses the system for the purpose of generating or manipulating such material.

Art 5(1b): manipulation that does not increase the exposure of any depicted intimate parts or alter the nature of any depicted sexually explicit activities is not "manipulation" for point (ba).

Operational consequence for anyone shipping an image or video generation or editing feature: limb (ii) makes safeguards a legal element, not a policy preference. The defensible position is documented input and output filtering, documented red-teaming against the reproducible-outcome test, and a documented pipeline for correcting reported misuse. Record it in the risk file.

## Practical screen for ordinary software

The prohibitions were written with state and platform-scale conduct in mind, but a small number of ordinary product patterns trip them. Screen for these before anything else.

| Product pattern | Provision at risk | What makes it a hit |
|---|---|---|
| Emotion or sentiment inference on employees, candidates or students — call-centre "agent stress" scoring, interview affect analysis, classroom attention tracking, exam engagement scoring | Art 5(1)(f) | Inferring **emotions** of a natural person in workplace or education. Note the medical-or-safety exception is narrow: fatigue detection for driver safety may qualify; productivity scoring does not |
| Any face-matching feature seeded from scraped web images or public CCTV | Art 5(1)(e) | Untargeted scraping to create or expand a facial recognition database. Buying a dataset built that way does not launder it |
| Enriching customer profiles with inferred ethnicity, religion, political leaning or sexual orientation from face or voice | Art 5(1)(g) | Biometric categorisation to deduce protected attributes. Inference from **biometric data** is the trigger; inference from purchase history is not Art 5(1)(g) but is a GDPR Art 9 problem |
| A cross-product trust or reputation score reused to deny an unrelated service | Art 5(1)(c) | Detrimental treatment in a context unrelated to where the data was generated |
| Dark-pattern personalisation tuned on vulnerability signals — targeting users flagged as in financial distress, or minors, with pressure mechanics | Art 5(1)(a), (b) | Materially distorting behaviour with significant harm. Financial harm counts |
| Gambling, lending, or subscription flows that adapt persuasion strength to detected distress | Art 5(1)(a), (b) | Same |
| Image or video generation, editing, "undress", face-swap or avatar features | Art 5(1)(ba), from 2 Dec 2026 | Reasonably foreseeable and reproducible NCII output without adequate safeguards |
| Any generative image feature without CSAM safeguards | Art 5(1)(bb), from 2 Dec 2026 | As above |
| Recidivism or "propensity to offend" scoring sold to public or private security | Art 5(1)(d) | Prediction based solely on profiling or personality traits |

Screens that look scary but are usually **not** Art 5:

- Fraud detection on transactions — behaviour of an account, not social scoring of a person across contexts. Note Annex III point 5(b) expressly excludes financial-fraud detection from the creditworthiness high-risk item.
- Sentiment analysis of product reviews or support tickets in aggregate — not inference of emotions of an identified natural person in a workplace or education institution; but individual-level agent monitoring is.
- Face **verification** to unlock a device or confirm a claimed identity — expressly excluded from Annex III point 1(a), and not Art 5(1)(e) unless the database was scraped.
- Personalised recommendations without vulnerability targeting and without significant harm.

## Where the boundary is genuinely unclear

Send these to a lawyer rather than resolving them in a design review:

- Emotion inference in a hybrid setting — customer-facing agents who are also employees; training simulations; healthcare staff.
- "Specific social or economic situation" under Art 5(1)(b): whether a segment amounts to a protected vulnerability.
- Whether a general-purpose image model with safety filters meets the "reasonable and adequate technical safety measures" standard in Art 5(1a)(a)(ii).
- Whether a bought dataset was built by untargeted scraping.

## Checkpoints

- [ ] All eight original points screened, each with a written yes or no
- [ ] Both 2026 points screened, with the 2 December 2026 date noted
- [ ] Emotion inference: workplace and education use explicitly ruled in or out, with the medical-or-safety exception assessed if invoked
- [ ] Provenance of any facial dataset documented
- [ ] For generative image or video features: safeguards documented against the Art 5(1a)(a)(ii) reproducible-outcome test, including misuse correction
- [ ] Any hit stops the feature; no mitigation-by-disclosure recorded as a fix
- [ ] Borderline calls routed to legal, not closed in the document
