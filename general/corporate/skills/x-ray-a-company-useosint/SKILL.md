---
name: x-ray-a-company-useosint
title: X-ray a company
description: Corporate due-diligence workflow — resolve a brand or website to its registered legal entity, map group structure and beneficial ownership, profile officers and directors, enumerate the digital estate, and screen litigation, insolvency, procurement, sanctions, PEP and adverse media. Use when asked to check out, vet or research a company, verify a supplier or counterparty before signing or paying, or assess whether a business is real. Applies to vendor and third-party risk, KYC and KYB onboarding, M&A and investor diligence, procurement integrity, and shell-company assessment. Reference at useosint.com/skills/x-ray-a-company.
author: UseOSINT
author_url: https://github.com/UseOSINT/Skills/tree/main/skills/x-ray-a-company
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: corporate
language: en
---

# X-ray a company

Take a brand, a website, or an invoice and produce a defensible picture of who you
are actually dealing with. Four layers — legal entity, people, infrastructure,
reputation and risk — worked in that order. Skipping the first ruins everything
after it: the trading name on the contract, the brand on the website, and the
entity liable in court are routinely three different things, and every later
finding attaches to the wrong one if you assume they match.

## Step 1 — Authorized scope

Write the target, the decision the work supports, the risk areas in scope, the
jurisdictions involved, and what is out of bounds. Read
[../../ETHICS.md](../../ETHICS.md). Corporate research on public filings is
broadly lawful and often mandatory, but two limits bite. Stay passive toward the
company's own systems — reading DNS and certificate logs is OSINT, authenticating
or probing is not. And named individuals inside the company are still data
subjects: an officer's directorships are fair game, their family is not.

**Done when** the scope note names the decision, risk areas, and jurisdictions,
and states that no interactive testing is authorised.

## Step 2 — Resolve the legal entity first

You are looking for a registration number in a named registry. Until you have
one, you do not have a subject.

| What you hold | Route to the entity |
|---|---|
| A website | Footer, terms, and privacy policy — statutory disclosure rules in much of Europe force the legal name and number onto the site; then confirm in the registry |
| A brand or trading name | Trademark registers give the registered proprietor; national registries index trading names against the registrant |
| An invoice or contract | Company number, VAT/tax number, and registered office are usually on it; verify every one, do not trust the letterhead |
| A listed company | The securities regulator's filing system is richer than the company registry |
| A group name only | Find any one member entity, then walk the chain in both directions |

Run `who-really-owns-it` for the registry mechanics. Record legal name,
registration number, jurisdiction, incorporation date, status, registered office,
officers, and share capital. Prefer the number over the name downstream — names
change, numbers don't. Standard traps: an operating company and a holding company
with near-identical names; a dissolved entity still trading under its old brand;
a brand held by an IP entity in a different jurisdiction from the trading entity;
a website run by a marketing entity that would not be liable for the product.

**Done when** you can name the entity that would be a party to your contract,
with its registry and number, and have stated which other entities share the
brand.

## Step 3 — Group structure and beneficial ownership

Walk up to the ultimate parent and down to the subsidiaries. Sources: filed group
accounts and subsidiary lists, listed-company exhibits enumerating subsidiaries,
beneficial ownership registers, and the shared-officer and shared-address pivots
in `who-really-owns-it`. Cross-border chains are the norm, not a red flag. What
matters is whether the chain ends in a named natural person or dissolves into a
jurisdiction that publishes nothing. Record it as far as it goes and state where
it stopped — "traced to a Cayman entity whose register is not public" is a
finding, not a failure.

Beneficial ownership breaks down four predictable ways: nominees, legally recorded
and economically irrelevant; trusts and foundations, which most registers do not
pierce; layering, where no single register sees the whole chain; and thresholds,
blind by construction to four people each holding just under the line.

**Done when** the ownership chain is drawn to its terminus or to a documented
opacity point, and named beneficial owners are recorded with their source.

## Step 4 — People

Pull the officer list from the registry, not the website — the website shows who
they promote, the registry shows who is legally responsible. For each person who
matters to the decision run `find-anyone`, and run the officer-name pivot in
`who-really-owns-it` for their other and prior directorships. A director with a
trail of dissolved companies, or one on twenty unrelated boards, is a different
risk profile from one with a coherent career.

Employee enumeration — headcount and function mix from professional networks, job
postings, and the team page — tests whether the company is operationally what it
claims. Platform counts include stale and duplicate profiles, exclude non-users,
and skew hard by country and industry: use the shape of the workforce, not the
number.

**Done when** every officer of record is listed with their other directorships
checked, and the workforce claim is corroborated or flagged.

## Step 5 — Digital estate

Run `recon-a-domain-passively` as the entry point; it covers `who-owns-this-domain`,
`find-hidden-subdomains`, and `find-exposed-servers`. What diligence wants from it,
as opposed to security testing: registration dates contradicting the claimed
founding date, infrastructure shared with unrelated brands under one operator,
subdomains revealing unannounced products or partners, and job-posting evidence of
the real stack. Check `secrets-in-git-history` for public repositories and
`what-leaked-about-you` for breach exposure of the email domain.

**Done when** the domain portfolio is enumerated, registration dates are compared
to the corporate timeline, and discrepancies are written down.

## Step 6 — Litigation, insolvency, procurement, and disclosure

- **Litigation.** Court dockets and judgment databases for the entity, its former
  names, and its subsidiaries. Read the disposition, not the filing — being sued
  is not liability, and a settlement tells you less than a judgment.
- **Insolvency.** Insolvency registers and statutory gazettes carry winding-up
  petitions, administration, and liquidation notices. Check the officers' prior
  companies; that is where the pattern shows.
- **Procurement.** Public tender and contract-award databases are third-party
  verified revenue — the strongest free evidence of real operations, and badly
  under-used. Debarment and exclusion lists sit alongside them.

Calibrate financial findings to the filing regime first. A listed company files
audited statements, segment detail, related-party transactions, and risk factors.
A small private company in most jurisdictions files an abridged, often unaudited
balance sheet with no profit-and-loss and no turnover figure — so absence of
revenue disclosure there is the legal norm, not evasion. What *is* meaningful:
late filings, repeated auditor changes, auditor resignation, qualified opinions,
charges registered against assets, and accounts that do not square with the
claimed scale of operations. Named sources per risk area:
[reference/diligence-checklist.md](reference/diligence-checklist.md).

**Done when** litigation, insolvency, and procurement each have a sourced finding
or a recorded "searched these databases, nothing found", and financial findings
are framed against what this entity type was required to disclose.

## Step 7 — Sanctions, PEP, and adverse media

Its own step with its own record, because it is the one a regulator or a court
will ask you to evidence. Screen the entity, its parents and subsidiaries, and
every named individual. Primary publishers: OFAC's sanctions list search, the EU
consolidated list, the UK sanctions list, the UN consolidated list. OpenSanctions
aggregates sanctions and PEP datasets across jurisdictions and is the practical
start for a cross-jurisdiction sweep; OCCRP Aleph is a research index, for
investigative rather than compliance screening. PEP status is a risk factor, not
wrongdoing, and it extends to close associates and family — exactly where
automated screening is weakest.

Adverse media means a structured search of news and regulatory announcements
against the entity, its former names, and its principals, in the local language of
every jurisdiction in the chain. An English-only search on a company with a foreign
parent is close to worthless. Record search terms and date range so the negative is
evidentially meaningful.

**Done when** every entity and person in the chain is screened against sanctions
and PEP sources with sources and date recorded, and adverse media is searched in
the relevant languages.

## Step 8 — Shell-company assessment

Score the profile; do not react to one indicator. Weighted catalogue:
[reference/shell-company-red-flags.md](reference/shell-company-red-flags.md).
Core cluster: an address shared by hundreds or thousands of entities;
incorporation shortly before the transaction it is party to; no web presence, or
a domain post-dating the pitch; nominee directors recurring across unrelated
companies; no employees and no accounts showing activity; a name mimicking an
established firm; bank details in a jurisdiction unconnected to the entity, the
directors, or the work. Any one is common and innocent. Four together is the
answer.

**Done when** the entity is scored against the catalogue with each indicator
sourced, and the conclusion states which indicators drove it.

## Step 9 — Report

Hand to `write-the-intel-brief`. Lead with the entity chart — ultimate parent,
intermediate holdings, contracting entity, subsidiaries, key people — then
findings by risk area with source, date, and confidence. Gaps get their own
section; a diligence report that hides what it could not check is worse than one
that found nothing.

**Done when** the brief has an entity chart, per-risk-area findings, an explicit
gaps section, and a stated overall confidence.

## Where this goes wrong

- **Registry data is filed, not verified.** Most registrars check a form is
  complete, not true; a record proves only what was filed and when.
- **Staleness is designed in.** Annual filing cycles put published officers and
  accounts a year or more behind reality, and aggregators lag again on top of
  that — a dissolved company can still show active. Confirm at the registry.
- **Name matching produces both errors at once.** Common names create false
  matches; punctuation, legal-form suffixes, transliteration, and post-merger
  renames create false negatives. Search former names deliberately.
- **Absence of a filing may mean the wrong registry.** Separate federal, state,
  and municipal registers exist, plus separate ones for foreign branches and for
  partnerships and other non-corporate forms.
- **Sanctions screening is noisy.** Transliterated names generate large numbers
  of false hits; a hit is a review trigger, not a finding.
- **Adverse media has a language and wealth bias.** Coverage is thin outside
  major markets, and litigious subjects get coverage removed.

## Confidence grading

- **Confirmed** — on a filing at the primary registry or regulator, or in a court
  record, with the document retrieved and dated.
- **Probable** — from a reputable aggregator or a single credible report,
  consistent with the primary record and uncontradicted.
- **Unconfirmed** — company marketing, a single unsourced report, or inference
  from structure alone.
- **Gap** — a source that should hold it returned nothing, or the jurisdiction
  publishes nothing. Name the database and date; a documented negative is a
  deliverable.

Grade ownership claims separately from operational ones. You can be certain who
the registered shareholder is and have no idea who benefits.

## Worked example

Vendor "Halberd Logistics" pitching a supply contract; you hold a website and an
invoice.

1. Site footer names "Halberd Logistics Group Ltd" with a company number; the
   invoice names "Halberd Ops Ltd", a different number. The contracting party is
   the one on the invoice, and it is not the one carrying the brand.
2. Registry: Halberd Ops is fourteen months old, one director, micro-entity
   accounts; the Group entity is nine years old with real accounts. The pitch's
   trading history belongs to an entity you would not be contracting with.
3. Officer pivot on the Halberd Ops director returns two prior companies, both
   dissolved after compulsory strike-off.
4. Dead end: the registered office hosts roughly two hundred entities, but
   resolves to an accountancy practice. Ordinary — weighted low.
5. Domain registered three months before the invoice date against a claimed
   nine-year history. With 2 and 3: contract with the Group entity or not at all.

## Pivots

| Selector produced | Feed into |
|---|---|
| Registry number, officers, shareholders | `who-really-owns-it` |
| Officer or director name | `find-anyone` |
| Primary domain | `recon-a-domain-passively`, `who-owns-this-domain` |
| Officer addresses, phones, associates | `dig-through-data-brokers` |
| Parent or subsidiary entity | Re-enter this workflow at Step 2 |
| Company email domain, public repositories | `what-leaked-about-you`, `secrets-in-git-history` |
| Multi-entity ownership web | `graph-the-network` |
| Finished evidence set | `write-the-intel-brief` |

## Legal notes

KYB, AML, and sanctions-compliance obligations impose source and record-keeping
requirements this workflow does not discharge on its own; for a regulated purpose
your record must show what you searched, when, and with what result. Registry
data often carries reuse conditions and rate limits — use the published APIs and
bulk products rather than scraping. Officer residential addresses and dates of
birth are protected in many registers, and deliberately re-identifying a
protected address is an offence in some jurisdictions.
