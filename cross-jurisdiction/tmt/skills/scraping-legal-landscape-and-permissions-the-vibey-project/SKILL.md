---
name: scraping-legal-landscape-and-permissions-the-vibey-project
title: 'Web Scraping: The Legal Landscape, Whether to Scrape, and the Permission Layer'
description: 'Use when deciding whether and how you are permitted to scrape: the four separate legal questions, computer-access law and the hiQ and Bright Data line under the CFAA, contract and terms-of-service exposure where scrapers actually lose, the DMCA §1201 shift, copyright, database rights and personal data, the AI-training layer and GDPR, the risk gradient, whether to scrape at all and what to do instead, and robots.txt and the emerging crawl-permission and payment layer. Includes the router for the whole web-scraping reference.'
author: the-vibey-project
author_url: https://github.com/the-vibey-project/vibey/tree/develop/src/vibey_tools/skills/plugins/web-scraping/skills/scraping-legal-landscape-and-permissions
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: cross-jurisdiction
practice: tmt
language: en
---

# Web Scraping: The Legal Landscape, Whether to Scrape, and the Permission Layer

> **Part 1 of 5** of the *Web Scraping* reference (plugin `web-scraping`), covering §0–§3. Sibling skills: `scraping-tooling-extraction-and-blocking` (§4–§7), `scraping-scale-reliability-and-data-quality` (§8–§10), `scraping-ethics-ai-corpora-and-site-defense` (§11–§13), `scraping-reference` (§14–§19). Section numbers are shared across the set; a reference written as §N → `skill` points into that sibling skill.
>
> **Currency:** Verified August 2026. See §16 → `scraping-reference` for the currency snapshot and what goes stale first.

> **How to read this.** Reference, not tutorial. Three markers:
> - **[DURABLE]** — how HTTP and the web work, engineering practice, or ethics. Doesn't expire.
> - **[VERSIONED]** — case law, regulation, tooling, platform behaviour. **This domain's
>   legal layer is moving faster than its technical layer right now.** Verify.
> - **[CONTESTED]** — genuine disagreement.
>
> **⚠️ GOTCHA** boxes mark the mistakes that get you blocked, sued, or quietly producing
> wrong data for months.
>
> **This is not legal advice.** §1 is a map of the frameworks that apply and the questions
> to put to counsel, not an answer for your jurisdiction or your use case. **The legal
> position depends heavily on what data, from where, about whom, and for what purpose** —
> and those four variables move the answer more than any technical choice you make.
>
> **The three framings that organize everything below:**
> 1. **The legal question is not "is scraping legal." It is four separate questions** —
>    *how did you access it* (computer-access law), *what did you agree to* (contract),
>    *what is the data* (copyright, personal data), and *what will you do with it*
>    (privacy, AI training, resale). **They have different answers and you need all four**
>    (§1).
> 2. **You are a guest on someone else's infrastructure, and they're paying for it.**
>    Nearly every operational rule in this document — rate limiting, caching, conditional
>    requests, off-peak scheduling — follows from taking that seriously, and doing so also
>    happens to be what keeps you unblocked (§11 → `scraping-ethics-ai-corpora-and-site-defense`).
> 3. **Scrapers rot.** A scraper is a hard dependency on someone else's HTML, which they
>    will change without telling you. **Silent breakage that produces plausible-looking
>    wrong data is the characteristic failure of this field** (§9 → `scraping-scale-reliability-and-data-quality`), and it's worse than
>    a crash because nobody notices.

---

## §0. Routing

| Asked about... | Go to |
|---|---|
| **Legality, regulation, risk** | **§1 — start here** |
| Should I scrape at all; alternatives | §2 |
| robots.txt and crawl permissions | §3 |
| How pages actually serve data | §4 → `scraping-tooling-extraction-and-blocking` |
| Choosing a tool | §5 → `scraping-tooling-extraction-and-blocking` |
| Parsing and extraction | §6 → `scraping-tooling-extraction-and-blocking` |
| Why I'm getting blocked | §7 → `scraping-tooling-extraction-and-blocking` |
| Scale, reliability, architecture | §8 → `scraping-scale-reliability-and-data-quality` |
| Data quality and validation | §9 → `scraping-scale-reliability-and-data-quality` |
| Storage, pipelines, monitoring | §10 → `scraping-scale-reliability-and-data-quality` |
| Operational ethics | §11 → `scraping-ethics-ai-corpora-and-site-defense` |
| Scraping for AI / RAG | §12 → `scraping-ethics-ai-corpora-and-site-defense` |
| Handling crawlers on your own site | §13 → `scraping-ethics-ai-corpora-and-site-defense` |
| "Don't do this" | §14 → `scraping-reference` |
| "Which approach is better?" | §15 → `scraping-reference` |
| "Is this still current?" | §16 → `scraping-reference` |
| Docs, books, people | §17 → `scraping-reference` |

---

## §1. The Legal Landscape

### 1.1 The four questions

**[DURABLE] "Is web scraping legal?" is unanswerable as asked**, because at least four
independent frameworks apply and **an operation can be fine under one and unlawful under
another.**

| Question | Framework | Rough position |
|---|---|---|
| **How did you access it?** | Computer-access law (CFAA, UK CMA, etc.) | **Public, logged-out access is defensible** (§1.2) |
| **What did you agree to?** | Contract / Terms of Service | **This is where scrapers actually lose** (§1.3) |
| **What is the data?** | Copyright, database rights, personal data | Facts ≠ creative works; personal data is its own regime (§1.5) |
| **What will you do with it?** | Privacy law, AI regulation, resale | **The fastest-moving layer in 2026** (§1.5–1.6) |

### 1.2 Computer-access law: the settled part

**[VERSIONED, and this is the most favourable line for scrapers.]**

- **Van Buren v. United States (2021, US Supreme Court, 6–3)** narrowed the CFAA's
  "exceeds authorized access" clause to accessing **areas that are off-limits** — using
  permitted access for the wrong purpose is not a CFAA violation. **This set the ceiling
  on how far the CFAA reaches scraping.**
- **hiQ v. LinkedIn (9th Cir., reaffirmed April 2022)** held that **scraping publicly
  accessible data does not violate the CFAA.** The court's reasoning is worth knowing:
  a broad reading would give platforms "free rein to decide, on any basis, who can collect
  and use" public data, risking "possible creation of information monopolies that would
  disserve the public interest."
- **Meta v. Bright Data (N.D. Cal., January 2024)** extended it to social platforms —
  **Judge Chen dismissed Meta's CFAA claim** over scraping public Facebook and Instagram
  pages **in a logged-out state**.

**[DURABLE] The line that emerged and keeps holding: logged-out public scraping is
defensible; anything behind a login is not.** If the server hands you the page without
authentication, you had authorization to access it.

### 1.3 Contract: where scrapers actually lose

> **⚠️ GOTCHA — hiQ won the CFAA argument and lost the case.** In November 2022 the court
> found hiQ had **breached LinkedIn's User Agreement, which it had accepted by creating
> accounts.** The matter ended in a consent judgment: **$500,000, a permanent injunction,
> and destruction of the scraped corpus.** The favourable CFAA precedent survives; hiQ
> did not.
>
> **The CFAA protects you from hacking claims. It does not protect you from contracts you
> agreed to.**

**The distinction courts have drawn**: terms accepted by **creating an account** (clickwrap)
bind you. **Browsewrap terms** — the "by using this site you agree" link in the footer,
which a logged-out visitor never affirmatively accepts — are a **much weaker basis**.
In *Meta v. Bright Data* the contract claim **partially survived, but only for the period
when Bright Data had an active contractual relationship with Meta** as a former partner.

**[DURABLE] The practical rule: never scrape a service you hold an account with, using or
alongside that account, if its terms prohibit it.** That is the single highest-risk
configuration in this entire domain, and it is also the most common.

### 1.4 The §1201 shift — the live frontier

**[VERSIONED, and this is the most important development for scrapers since hiQ.]**

**Reddit sued Perplexity AI and several data-collection providers in late 2025**, and the
central claim is **not** CFAA — it's **DMCA §1201**, alleging **circumvention of
technological protection measures including rate limits and anti-bot systems** to scrape
content for AI training.

**Why this matters enormously**: §1201 **targets the circumvention, not the publicness of
the data.** The public-data cases predate the AI training boom, and the new wave reframes
the question from *"was it public?"* to **"did you defeat a protection to get it, and what
did you do with it?"** — a question the hiQ line does not answer in your favour.

**[CONTESTED and unresolved.]** The case was pending as of early 2026. **But the strategic
implication is already actionable: deliberately defeating anti-bot measures now carries a
legal theory it didn't clearly carry before**, independent of whether the underlying data
was public. Similar circumvention and IP theories appear in creator suits over alleged
YouTube scraping for model training.

### 1.5 Copyright, databases, and personal data

**Copyright**: **facts are not copyrightable; creative expression is.** Extracting prices,
specifications, or statistics sits differently from reproducing articles, images, or long
creative excerpts. **The EU's text-and-data-mining exception is the main carveout — and it
is subject to a machine-readable opt-out** (§3.2). The **EU sui generis database right**
has no close US equivalent and protects substantial extraction from a database as such.

**Personal data is a separate regime that public availability does not exempt.**
**[DURABLE] This is the point most technically-minded scrapers miss**: GDPR applies to
personal data regardless of whether it was publicly posted, and it applies
**extraterritorially** to anyone processing EU residents' data wherever they're based.

**[VERSIONED] The Clearview AI line is the object lesson.** Clearview scraped billions of
facial images from public sites to build a biometric database, drawing **€30.5M from the
Dutch DPA (2024)** plus actions from the Italian Garante and CNIL, and **$75M+ in
cumulative fines across the US, UK, and EU.** The UK's **Upper Tribunal held Clearview's
processing was within UK GDPR scope** despite the company being wholly outside the UK,
and rejected the law-enforcement exemption for a private company — reinforcing
extraterritorial reach.

**⚠️ Note precisely what those cases turned on.** As one analysis puts it: **none of them
turned on whether the data was technically public.** They turned on **the absence of a
documented legal basis, the absence of transparency toward the people whose data was
collected**, and — for biometrics — the absence of any Article 9 exemption.

### 1.6 The AI-training layer

**[VERSIONED — the fastest-moving material in this document.]**

**EDPB Guidelines 03/2026 on web scraping in the context of generative AI** were adopted
at the Board's **July 2026 plenary** — **the first pan-EU framework addressing AI training
data collection directly**, confirming that **GDPR applies in full to personal data scraped
to train AI models, with no carve-out for AI.** Reported headline positions:
- **Consent is unlikely to be a valid legal basis** for scraping at this scale.
- **Legitimate interest survives only a documented three-part test**, assessed
  **per deployment**.
- **Data minimisation applies before scraping**, not after.
- **Sensitive data carries a near-prohibition.**
- ⚠️ **Once a model is trained, personal data cannot easily be deleted from it** — which
  **turns AI data governance into an upstream engineering problem you must solve before
  training, not after launch.**
- Applies both to organizations scraping directly **and to those acquiring pre-scraped
  datasets from third parties**, including data brokers.

Companion **anonymisation guidelines** set a three-criterion test. **Both were open for
public consultation until 30 October 2026 — they are draft guidance, not settled law**,
but they signal where enforcement is heading.

**EU AI Act**: in force since 1 August 2024, GPAI obligations from **2 August 2025**, with
**enforcement teeth from 2 August 2026** (GPAI fines up to **€15M or 3% of turnover**).
Two obligations land directly on data collection: **GPAI providers must publish a summary
of training data sources**, and must **operate a copyright policy respecting
machine-readable opt-outs.** **[DURABLE-ish implication] Machine-readable "don't mine me"
signals — robots.txt, TDM reservations — now carry legal weight for anyone training models
for the EU market**, which is a change in kind from their previous purely-voluntary status
(§3). The Act also **bans untargeted scraping of facial images** for facial-recognition
databases, while distinguishing targeted from untargeted collection.

### 1.7 The risk gradient

**[DURABLE] A usable mental model, lowest to highest risk:**
```
LOW    public factual data · logged-out · no personal data · rate-limited ·
       own use · robots.txt respected
  │
  │    public data incl. some personal data · documented legal basis · GDPR-compliant
  │    aggregate/derived output · commercial use
  │
  │    ⚠️ defeating anti-bot measures  ← the §1201 theory (§1.4)
  │    ⚠️ republishing creative content
  │    ⚠️ training models on it, especially with personal data (§1.6)
  ▼
HIGH   behind a login, against accepted terms · biometric or sensitive data ·
       bypassing authentication · volume causing operational harm
```

---

## §2. Should You Scrape At All?

**[DURABLE] Scraping is the option of last resort, and teams reach for it first.** Check,
in order:

1. **Is there an API?** Documented, stable, rate-limited, and it won't break when they
   redesign. **Even a paid API is usually cheaper than maintaining a scraper** once you
   price the engineering time.
2. **Is there a bulk dataset or data dump?** Wikipedia, government open data, Common Crawl,
   academic corpora, and many companies publish more than people realise.
3. **Is there an RSS/Atom feed, sitemap, or structured-data markup?** (§4.3 → `scraping-tooling-extraction-and-blocking` — sites often
   hand you clean JSON-LD for free.)
4. **Can you license it?** A commercial data agreement removes the entire legal layer of
   §1 and often costs less than the litigation risk.
5. **Can you just ask?** ⚠️ **Genuinely underused.** Small sites and researchers frequently
   say yes, and an email creates a written record of permission.
6. **Does a data provider already have it?** Often cheaper than building it.

**[DURABLE] Then scrape** — and note that the maintenance cost is the real cost. A scraper
is not a project; it is an ongoing obligation to someone else's front-end decisions.

---

## §3. robots.txt and the Permission Layer

### 3.1 robots.txt

**[DURABLE] The Robots Exclusion Protocol is a voluntary convention** (standardized as
**RFC 9309**), served at `/robots.txt`. It tells well-behaved crawlers what they may access.
Key directives: `User-agent`, `Disallow`, `Allow`, `Sitemap`, and `Crawl-delay` (widely
implemented, not in the RFC).

**⚠️ robots.txt is not an access control and never was.** It does not enforce anything;
it declares a preference. **But ignoring it is now materially riskier than it used to be**
for three separate reasons: it evidences bad faith in a contract or tort dispute, it
signals to the site's defensive layer that you're not a good-faith crawler, and under the
EU AI Act **machine-readable opt-outs now carry copyright significance for model training**
(§1.6).

**[DURABLE] Read it, respect it, and identify yourself.** A descriptive `User-Agent` with
a contact URL costs nothing and is the difference between a site owner emailing you and a
site owner blocking your whole ASN.

### 3.2 The emerging permission and payment layer

**[VERSIONED — a genuinely new stratum of the web, and it is consolidating fast.]**

**Cloudflare** has become the de facto enforcement layer:
- **"Content Independence Day" (July 2025)** introduced a one-click **Block AI Bots**
  toggle and the **Pay Per Crawl** private beta, which **revived HTTP 402 (Payment
  Required)** — blocked crawlers receive a 402 signalling that content is available for a
  price, with Cloudflare acting as **merchant of record**.
- **1 July 2026**: the binary toggle was replaced with **three separately controllable
  categories — Search, Agent, and Training** — each with states from allow through
  "block only on pages with ads" to "block everywhere." **Available to all customers
  including the free tier.**
- ⚠️ **15 September 2026**: **Training and Agent crawlers blocked by default on
  ad-serving pages** for new domains, new sites of existing customers, and **all existing
  free-tier customers.** Search remains allowed by default. Cloudflare's stated reasoning:
  "an ad is a signal that a website owner meant for a person to land there and see it."
- ⚠️ **The mixed-use trap**: if a zone blocks Training, **multi-purpose crawlers such as
  Googlebot, Applebot, and BingBot get blocked too**, even where Search is allowed. This
  only applies to zones that have actively enabled Training blocking — but **site owners
  who toggle "block AI" without understanding this can remove themselves from search.**
- **Content Signals** in robots.txt gained a **`use` parameter** expressing post-crawl
  usage preferences at three levels: **Immediate** (no storage or reuse), **Reference**
  (indexing, excerpts, links back), **Full** (summaries or reproduction). Not enforceable
  by robots.txt itself, but Cloudflare reports Verified Bot compliance via BotBase.

**The standards picture is fragmented**: **IETF AIPREF** (working toward a standards-track
spec, with a Content-Usage header and matching robots.txt rule), **RSL (Really Simple
Licensing)** handling the permission and compensation layer AIPREF omits, plus **ai.txt**
and **TDMRep**, each proposing its own file. **[CONTESTED] Nobody has won**, and a site
may express preferences in three incompatible places.

**⚠️ The economics driving this are stark.** Cloudflare-network analysis reported that
**89.4% of AI crawler traffic serves training or mixed purposes rather than search**, and
tracked crawl-to-referral ratios in the **hundreds-to-thousands of pages crawled per
referral sent back** — which is precisely why the historic crawler bargain (we take your
content, we send you traffic) has broken down and why the permission layer exists at all.
