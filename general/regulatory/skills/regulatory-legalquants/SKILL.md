---
name: regulatory-legalquants
title: /regulatory
description: 'Regulatory research, refreshing earlier research, jurisdiction comparison and legality checks built on primary sources — retrieves the instrument from its official publisher, proves which version it is, and quotes only from the bytes it fetched. Use when the user has a regulation problem: understanding what a law requires, checking whether text they hold is current, re-running earlier research against the instrument as it stands today, or comparing how a rule differs across markets. Domain- and sector-agnostic: any instrument, country or area of law. Trigger even without the word "regulatory" — e.g. "what does the AI Act require," "is this still in force," "has this changed since we advised," "how does this differ in the UK," "we''re planning to launch X, where does that land," "find me the actual text of," "is our compliance memo out of date." Answers questions about legal requirements with cited support; identifies unresolved facts and judgments without deciding disputed
  application questions.'
author: LegalQuants
author_url: https://github.com/LegalQuants/lq-plugin-oss/tree/main/plugins/legalquants-litigation/skills/regulatory
license: Apache-2.0
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: regulatory
language: en
sources:
- title: Citation Handoff
  path: references/citation-handoff.md
- title: Construction Rubric
  path: references/construction-rubric.md
- title: Discovery
  path: references/discovery.md
- title: Unmapped
  path: references/jurisdictions/_unmapped.md
- title: Eu
  path: references/jurisdictions/eu.md
- title: Index
  path: references/jurisdictions/index.md
- title: Sg
  path: references/jurisdictions/sg.md
- title: Uk
  path: references/jurisdictions/uk.md
- title: Us Ca
  path: references/jurisdictions/us-ca.md
- title: Us Federal
  path: references/jurisdictions/us-federal.md
- title: Run Format
  path: references/run-format.md
- title: Version Check
  path: references/version-check.md
---

# /regulatory

## Profile & playbook (per AGENTS.md — clean separation)

**Read:** exactly one thing before working — your own namespace in
`lqplaybook.md` (`[regulatory] ...` confirmed lines: house citation format,
jurisdictions this user works in, how much version detail they want on
screen). If the file or namespace is absent, use defaults. Apply them over the defaults here. Read nothing else; the journey
file never influences work product. If the user asks "explain how this works"
or wants coaching, you may read their archetype from `lqprofile.md` and pitch
the explanation at their level. A one-line declinable walkthrough offer on
first use is fine.

**Write:** nothing to the journey — the scribe owns that. One exception: when
the user reveals a preference in-session (a citation style, a jurisdiction they
always need alongside another), propose the exact `[regulatory]` playbook line
and write it only on an explicit yes.

Never client-identifying facts, in any entry.

## The one rule

> **Secondary sources tell you an instrument exists. Only the official
> publisher tells you what it says.**

Nothing is quoted that did not come from the publisher's own bytes. Not from a
search result, not from a law firm note, not from a tracker, not from a
database, not from memory, and not from a web-fetch tool's rendering of a page
— that is a model's summary of the text, not the text.

Trackers, alerts and search are excellent for **finding** instruments. Use them
for that. They are never the source layer.

## The second rule

Answer the question about legal requirements, connecting the verified provisions
to the supplied facts and clearly stated assumptions. Distinguish law, official
guidance and additional contract terms. Reserve unresolved factual findings,
disputed interpretations and evaluative judgments for the lawyer; explain the
precise issue and evidence needed, rather than withholding an answerable duty.

`references/construction-rubric.md` governs this in detail. Read it before
writing any output.

## What this produces

Two labelled levels: **Your answer** (normally 150–250 words, essential citations,
assumptions and qualifications) then **Supporting analysis**. The initial chat
must state the substance of the answer, even when a fuller file is delivered.
Keep version qualifications brief unless they change or prevent the answer.
Source receipts, hashes, amendment history and extraction diagnostics belong in
a separate verification record. For broader questions, explain a necessary
length exception briefly; do not repeat points across sections.

Use a temporary run folder inside the user's workspace for official bytes and
one master extraction dataset per instrument, even for an on-screen answer.
Persistent retention is optional: offer to keep the audit package; otherwise
remove temporary material on completion and disclose that no retained package
will remain. Never describe ephemeral verification as a retained audit package.

`references/run-format.md` gives the shape of the note, the rules for quoting
and what a saved folder holds. The quoting rules there are enforced by a script,
so read it before writing a note.

## Intake

Ask one question at a time. Skip any the user has already answered — most
people open with question 1 unprompted. Never ask all of these at once.

**Before the fetch, ask only these two:**

1. What's the problem? Tell me the way you'd tell a colleague.
2. Is there a specific law or rule in play, or are you trying to work out what
   applies?

**Then retrieve the text.** Use any supplied link immediately. Establish the
jurisdiction and research/as-of date before selecting a version; ask only if
missing and material. Ask about activity, role, location and missing facts only
when needed to answer the question. Do not demand a client name.

A material version problem merits a short progress update. It does not replace
the answer-first delivery. Ask about persistent retention before keeping a run;
temporary verification does not depend on that choice.

`check` runs this order differently, because it has no instrument to fetch until
the conduct is described. Its section says how.

Do **not** ask about size or thresholds — the instrument generates those, and
asking first anchors the analysis. Do not ask "which regulators do you watch";
that is a monitoring product's question, and this skill starts before you know
what catches you. Do not ask about sector or output format.

## Routing

If the user typed a shortcut — `research`, `refresh`, `compare`, `check` — use
it. `track` is the older name for `refresh` and still routes there.
Otherwise route on what they said:

| They gave you | Workflow |
|---|---|
| A named instrument, or a link, or "what does X require" | `research` |
| Two or more jurisdictions, or "how does this differ in..." | `compare` |
| Something the client does, plans, or is about to ship | `check` |
| An earlier run plus "what's changed" / "is this still right" | `refresh` |

Genuinely ambiguous → ask intake question 1. It is not wasted work.

## The spine

All four workflows run this. It is the whole value; the workflows are what you
do with the result.

Read `references/version-check.md` and `references/jurisdictions/index.md`
every run, then the entry for the jurisdiction in play. If there is no entry,
read `references/jurisdictions/_unmapped.md` and follow it — do not guess a
publisher.

### 1. Identify the instrument

Get to a specific instrument: name, number, year, jurisdiction. Search and
trackers are fine here — this is finding, not sourcing. If the user described a
problem rather than a law, name the candidates and go to step 2.

### 2. Confirm with the user before fetching

State the instrument you are about to fetch and the publisher you will fetch it
from. One line, and carry on unless they stop you. Fetching the wrong
instrument well is worse than fetching nothing.

### 3. Fetch from the official publisher

    python3 scripts/fetch_source.py <url> <dir> --publisher <host> --label "<version>" \
        --jurisdiction <code> --profile <source-profile-id> --instrument-id <stable-id>

`--publisher` comes from the registry entry. The script refuses to save
anything that redirects off that host. If it refuses, report that — do not fall
back to a secondary source.

A redirect that stays on the publisher is reported, not refused, and the notice
is worth reading: some are the publisher canonicalising your URL, and some are
an error page served with HTTP 200 from the right host. Read the saved bytes
before quoting from them.

Read the registry entry's "Getting the bytes" section before the first fetch of
a jurisdiction. Publishers differ in what they will serve to a script, and the
entry says what was needed — California, for one, needs a trust store its
certificate chain resolves in.

**Then check that what came back is what you asked for.** Publishers serve
ranges of sections on one page, and a range URL answers successfully whether or
not your provision is inside it: California's group pages are cut by title, and
§1798.82 sits in Title 1.81 while the adjacent group is Title 1.81.5. The host
is right, the bytes are a real statute, and the provision is absent. So search
the saved file for the number you came for before going on. If it is not there,
the remedy is another fetch — the individual section's own URL — and the finding
is about the fetch. Extraction has not been tried yet and cannot be blamed.

**Four findings, kept apart.** Before anything is quoted, establish and state
each of these separately: **publisher identity** — whose site this is;
**publication authority** — what this copy *is*, the authentic text or a
convenience copy; **language** — authentic, second authentic, or translation;
and **version**. They are independent findings, and collapsing any two of them
is how an unofficial copy comes to be labelled official.

The trap is site furniture. A page's language notice — *"the English language
version is always the official and authoritative version of this website"* — is
a translation-widget disclaimer about the website. It establishes nothing about
the legal authority of the statute printed on it, and the same publisher may say
in its own user guide that the text is unofficial. Both were true of Illinois at
once. So quote the publisher's statement about the **statutory text**, not a
notice that happens to contain the word "official"; if the publisher makes no
such statement, that absence is the finding, and it gets written down.

A government-hosted convenience copy that disclaims its own authenticity can
still carry a qualified answer — that is the default, and a firm may set a
stricter one. What it can never do is carry a silent one. Put the publisher's
disclaimer in the note, in its own words, and name the authentic publication
that would settle the point.

### 4. Check the version

    python3 scripts/read_version.py <dir>/source.html --jurisdiction <code> --json <dir>/version.json

Non-zero exit means the publisher's own markers say this is not the text to
quote. **Refetch the version the marker names.** A caveat on a stale quote is
still a stale quote.

No recognized marker is also non-zero and blocks extraction. For a dated
question about superseded law, record both `--historical-effective <date>` and
`--research-date <date>`; this creates an explicit historical selection rather
than weakening the current-law check.

Then do the part no regex does: read the amendment list and say which of them
touch the provisions this question turns on; check commencement for the
provisions you are relying on, not for the instrument; check whether anything
you plan to quote is tagged prospective.

### 5. Extract the provisions

    python3 scripts/extract_provisions.py <dir>/source.html <dir>/provisions.json --provenance <dir>

Confirm the numbering convention if it is not obviously right — the script
reports what it detected, and `--calibrate-only` shows the counts without
writing anything. Everything downstream cites these ids, so a wrong convention
fails quietly.

Automatic detection needs two headings before it commits, because one line that
reads like a heading is more often a cross-reference. **A single-section source
is normal, not a refusal** — most code sections are published on their own page.
When the script reports one heading it names the convention; confirm it with
`--pattern <name>` and extraction runs normally, keeping the section's
subdivisions. Confirm it the same way in every workflow, and record that you
confirmed it. What you may never do is force a convention the text does not use:
that is a run whose every quote is cited to one undivided block, and the script
now refuses it rather than reporting a calibration it did not achieve.

Extraction also refuses a source in which two provisions come out under the same
label or the same id. That is the one break with no downstream signal: a note
quoting either one cites a real section and passes the checker, just not the
section the words came from. It is usually the publisher's page furniture — a
contents list, a breadcrumb or a page title repeating a heading the body also
carries — so fetch the section or chapter itself rather than an index or search
view. It is a finding about the source, not something to edit away.

**When extraction refuses, the source is evidence, not a formatting problem.**
The refusal is about the document, so the only supported move is to name the
convention the text actually uses — `--pattern <name>` — or to stop and report
what the file looks like. Four things are out of bounds, and testing found all
four: editing or rewriting the publisher's headings so they match a pattern;
fetching a larger document to raise the heading count; hand-writing
`provisions.json`; and piping text in rather than saving it. Each puts the model
between the publisher and the quotation, which is the one thing this skill
exists to prevent — and each broke something further downstream, so the run cost
two to three times the tokens and several extra minutes and still answered
nothing. If you find yourself repairing the tools instead of reading the law,
that is the signal to stop and say so.

**A chaptered act is not the code it amends.** Fetch a session law — a
California `SEC. 2.`, an Illinois Public Act — and the provisions are *act*
sections, each containing the code section it enacts. The act's own numbering is
what the run cites. Two consequences worth stating in the note: a code-section
citation must name the act section carrying it, and a bill that carries several
alternative versions of one code section (California's `SEC. 2.` through
`SEC. 2.3.`) has them all extracted side by side. Which one took effect is a
question for the act's own operative-condition sections, read in step 4 — never
a choice made during extraction.

The output classes every provision (`recital`, `preamble`, `operative`,
`annex`, `schedule`) and indexes every term the instrument defines. Both
matter: nothing classed `recital` may be quoted as imposing a duty, and any
ordinary word the instrument defines is not being used in its ordinary sense.
The output also carries the instrument identity and exact source lineage. If a
PDF or other publisher file was converted to text, write `transformation.json`
as described in `references/run-format.md`; extraction refuses an unreceipted
derivative.

### 6. Construe, and quote

Per `references/construction-rubric.md`. Quote verbatim from the fetched text.
Give the provision and the version each quote came from. Lay the note out as
`references/run-format.md` describes — the format is what makes step 7 possible.

### 7. Check the quotes before the note goes out

    python3 scripts/verify_quotes.py <dir>/note.md <dir>/provisions.json \
        --depends-on <provision-id>="<why unquoted text affects the analysis>"

Every quote must be verbatim from the fetched bytes and cited to the provision
the words actually live in. Do this even when the note is only going on screen
and nothing is being saved — write it to a temporary file and check it there.

This is the one error that has no symptom. A paraphrase of a provision reads
exactly as well as the provision, so it survives your own review and the
lawyer's. If a quote fails, fix it or cut it. Never ship it with a caveat.

**Fixing a quote means changing the quote, not the formatting around it.** A
failing quotation set as a code span, in bold, or in single quotes leaves the
same words in front of the lawyer and takes them out of this check; the run then
exits 0 over fewer quotations than it started with. `verify_quotes.py` reports
`unquoted-instrument-text` for words of the instrument carried outside quotation
marks, so the escape is closed — but the reason it is closed is that the coverage
falling is invisible in a way a failing quote never is. Broadening a pinpoint
until the attribution check stops objecting is the same move: the citation gets
vaguer, the check gets quieter, and the note now cites a thousand words for one
sentence.

Record every unquoted definition, exception, scope, commencement, annex, or
cross-reference the analysis depends on with a separate `--depends-on`. Quote
verification recomputes the saved source and complete provenance chain before
accepting the note.

**The note ends with the links.** Every source you consulted, official ones kept
separate from everything else, with the addresses taken from the fetch receipts
rather than retyped — `references/run-format.md`, "Sources". This is not a
courtesy at the end of the work. A reader who has to ask where a quotation came
from has been handed a claim, and the run folder they would have found it in is
usually deleted after delivery. `verify_quotes.py` refuses a note that does not
carry the address its text came from.

## The four workflows

Each is a delta on the spine, not a separate machine.

### research — "I need to understand this law."

The spine, then: the provisions that decide the question the user asked,
quoted; the defined terms those provisions rest on; the outstanding questions.

Lead with the answer to the question. Include a version difference in that
answer only if it changes the answer or prevents a verified answer.

### refresh — "Is the research we already did still right?"

This re-runs research you already hold against today's publisher text and
reports the delta. It does not watch anything: nothing happens between the two
runs, and a user who asks to "track" an instrument is usually picturing a
standing monitor. Say what this does — one line, at the start — so they know
whether they got what they wanted.

Needs an earlier saved run. Run the spine again into a **new dated folder** —
never over the old one, because the comparison can only use what is still there.
Then:

    python3 scripts/diff_runs.py <earlier>/provisions.json <later>/provisions.json \
        --manifest <earlier>/run.json

`run.json` is the manifest `verify_quotes.py` wrote when the earlier note was
verified. It preserves the complete provision set, while separately identifying
quoted provisions and unquoted semantic dependencies. The diff compares only
matching instrument identities, assesses every preserved provision, and
highlights the identified dependencies. It never treats unchanged quotations as
proof that the legal conclusion remains valid.

Lead with the provisions the earlier analysis rested on. The rest of the
preserved set is listed in full beneath them — never dropped, because "three
things changed elsewhere" is what makes a lawyer ask to look.

**The answer is about the later text, not about the refresh.** Open with the
result under the later version, the words that produce it, and any condition
that immediately limits that result. A lawyer who reads the first paragraph and
stops should have all three. Everything below is support for them.

Four openings fail that test, and all four are recorded:

- **The fate of the earlier research.** "Completed; earlier research is
  unchanged" is a fact about files. An amendment does not reach back and change
  what the earlier analysis said about the earlier text, so preservation is an
  audit fact and belongs in the verification record. One run opened with it and
  then said the earlier conclusion materially changes — both true, about
  different things, and left for the lawyer to reconcile. If the earlier
  analysis was actually wrong, that is a correction, and it is said as one.
- **The part that did not move.** One run opened with access eligibility, which
  was unchanged, and reached the new prohibition on copying fees afterwards.
  Lead with what moved. The conditions that survived follow it, and they are
  shorter than they look.
- **The software.** Comparator statuses, hashes, exit codes, pagination
  artefacts and recovered shell errors go in the verification record, reachable
  by one link. The exception is a failure that prevents a reliable answer: that
  goes first, worded as what could not be established rather than as which
  command exited non-zero.
- **A banner repeated in every section.** "Provisional and unverified" four
  times tells the lawyer nothing to do. Once, near the answer, name the source
  actually checked, the edition it supports, what was not verified, and the
  missing fact that would change the answer. Keep separate questions separate —
  whether the text is official, whether it is in force, what identification a
  requester must produce, whether a record falls in an exception. And **"not
  verified as in force" does not mean "not in force."**

**A definition that appeared or moved is a change in the law's reach**, even
where the provisions using the term are reported unchanged. `diff_runs.py`
prints those under "Defined terms" from the extractor's own index. Follow the
term into the provisions that use it and say what it does there; a new
definition of "legal guardian" reaches every subdivision that grants a guardian
access, and none of those subdivisions will show a single moved word.

**Quote the amendment; do not describe it.** For every provision reported as
`amended` or `replaced`, the diff hands over the words themselves — a `was` run
and a `now` run for each region that moved. Put those in the answer as the
before and after they are. Do not go back to the two source texts and write your
own account of what changed: a paraphrase is the model authoring the amendment,
and it is the one sentence in a refresh that `verify_quotes.py` cannot check.
The failure this prevents is quiet. An amendment that renames a custodian often
re-anchors the anaphors further down the same provision — "the department" now
means a different department, spelled out where it used to be implied. A summary
that reports the rename is true and still loses the second half. The words do
not lose it.

Where a run was extracted with `--no-text`, the diff says so instead of showing
words. That is a report of hashes only: name it as such, and do not fill the gap
from the source texts.

**Check a refresh note against both runs.** The `was` side of every amendment is,
by construction, not in today's extraction, so step 7 has to be given the earlier
one as well:

    python3 scripts/verify_quotes.py <later>/note.md <later>/provisions.json \
        --earlier <earlier>/provisions.json

Without `--earlier` every quotation of the text as it read comes back
`not-in-text` — "a rendering or a recollection, not the instrument" — which is
both false and the accusation most likely to be worked around instead of
answered. With it, those quotations verify against the earlier run's hashed
bytes, and the cite has to say which edition it is: `— § 1347.08(B)(2), as it
read before the amendment`. A cite that does not say so fails as
`superseded-as-current`, because repealed words quoted as current law are worse
than a misquote — every word of them is genuine.

Read `replaced` carefully and explain it in full. It means the number survived
but now holds a different provision — the earlier note's citation still
resolves, and resolves to something else. Do not describe it as an amendment,
and do not go looking for where the old provision went: if it was repealed while
its neighbours moved up, there is nowhere for it to have gone.

`retitled` is the quieter neighbour of `replaced`: the heading changed over a
body the comparison found substantially kept. The earlier note's citation still
points at the provision it always did, under a name the publisher has retired.
Say that the heading changed and that the rules did not, and do not import
`replaced`'s warning into it — a recaption sends nobody looking for a repeal.
Where one of the runs was extracted with `--no-text` the body cannot be read at
all, so a changed heading is reported as `replaced` on the conservative side;
that is a limit of the run, not a finding about the instrument, and it is
resolved by re-extracting with text rather than by reasoning around it.

**When the diff cannot run, that is the first line.** The earlier run may not
carry what a comparison needs — no `provisions.json`, no `run.json`, a different
instrument identity. Open with **Comparison blocked**, say which prerequisite is
missing, then describe the later research separately and by name: fetching,
version-checking and extracting today's text is real work and worth reporting,
but it is not a refresh, and "Completed the refresh" at the top of an answer
whose fourth bullet says the comparison never ran is a line a skimming reader
will act on. The earlier files stay exactly as they are — the missing baseline
is never reconstructed, and a reconstructed one would make the diff a comparison
of your own work against itself.

### compare — "How does this differ across our markets?"

Run the spine once per jurisdiction, separately versioned — they will not be
current to the same date, and saying so is part of the answer.

Output is one row per test, one column per jurisdiction, each cell citing that
jurisdiction's provision and its own version. Never merge two jurisdictions'
text into a single statement, and never let the jurisdiction you fetched first
set the frame for the others. `references/run-format.md` gives the table's
shape and the worked example.

Step 7 runs per jurisdiction too: each column's quotes are checked against that
jurisdiction's own `provisions.json`.

A stop is per jurisdiction as well. Name which columns resolved, which stopped,
and at which step each one stopped: "the extractor failed on all three" is three
separate failures reported as one, and it buries the fact that they may have
three different remedies — or that one of them was never an extraction failure
at all.

### check — "We're planning X. Where does it land?"

Intake runs the other way round. The other three workflows start from an
instrument and ask what it says; this one starts from conduct and has to work
out which instruments are even in play. So the questions that select them come
before the fetch, and the version finding lands later than usual. Say so when
you ask — the user is being asked more before they see anything back, and
knowing why is the difference between intake and interrogation.

Before selecting instruments, establish any missing material facts:

- What will they actually do? The activity, step by step, as it will happen.
- Who is on the other side — consumers, businesses, children, employees?
- Where does it happen, and where are the people it affects?
- What is their role in the chain — do they build it, deploy it, resell it,
  host it?
- When does it start?

Use links already supplied and ask only for remaining material facts.

**A sector is not an activity.** "We're a fintech", "it's a health app" — those
name a market, and instruments do not test markets. Ask once more: what does the
thing do on the day a customer uses it? If the answer is still a product
category, the analysis will be about a category and will be wrong.

**A role is not an identity.** Instruments assign duties by role — provider and
deployer, controller and processor, manufacturer and importer — and one company
holds different roles under different instruments, sometimes more than one under
a single instrument. Role follows from what they do in the transaction, so it
cannot be settled before the activity is described concretely.

**Discovery is its own phase, with its own gate.** Once the conduct is
described, read `references/discovery.md` and work it before fetching anything:
model the activity on its dimensions — actor, object, action, affected people,
place, lifecycle stage, failure mode — and generate candidate instruments from
every populated one. Ask what could prohibit, license, recall or penalise the
conduct, not only which subject headings apply. Name the plausible regulators
before settling on instruments, and check their lists, registers and orders as
well as their statutes. Prefer false positives here: the spine kills a weak
candidate against the official text, but nothing downstream can resurrect the
instrument nobody named. A verified note is not a complete note — the discovery
coverage receipt is what closes the gap between the two.

**The last question is doing more work than it looks.** A `check` is a question
about the future, so the version discipline changes shape: `research` asks
whether this is the current text, and `check` asks what will be in force when
they do this. A provision that is prospective today, or effective but not yet
operative, or commenced for some Parts and not others, is precisely what this
workflow exists to catch — and each of those is printed on the page for a reader
who looks. Run step 4 against the launch date, not against today.

Then the spine per candidate instrument, then the output: each provision the
conduct engages, quoted, with the fact that would decide it and the class it
falls into. Where the conduct meets a standard rather than a bright line —
reasonable, appropriate, proportionate — name the judgment being asked for and
stop. That is where the lawyer's opinion starts and this skill's job ends.

**Say what you did not check.** This is the only workflow whose failure is a
false negative, and the spine cannot protect against it: it proves the text you
fetched, never the instrument nobody thought of. So the note carries the
discovery coverage receipt from `references/discovery.md` — the search surface,
row by row, with unworked branches marked unresolved rather than left silent —
and every negative finding states which of the four kinds of nothing it is:
expressly excluded, test not met on the supplied facts, nothing found after the
searches named, or not investigated. Run the omission challenge before
delivery. "We found nothing that catches this" is a sentence this skill must
never produce on its own.

Then check the receipt the way you check the quotes:

    python3 scripts/check_receipt.py <dir>/note.md

It audits the receipt, never the research. It cannot know whether the right
regulators were named; it knows that the regulators row was filled in, that a
dynamic source carries the date that makes it a dated fact, that a negative
says which kind of nothing it is, and that the challenge came back with an
answer. Those are the omissions that survive review, because an incomplete
receipt reads exactly like a complete one.

**Expect to be pushed for a verdict**, harder here than anywhere else, because
the user is deciding something. The answer to "so are we allowed?" is the
provisions engaged and the facts still needed to apply them. Give it plainly and
without apologising for it: a lawyer reading that list knows within a minute
whether the plan is fine, which is the thing they actually came for.

## Scripts reference

| Script | Does | Stops the run when |
|---|---|---|
| `fetch_source.py` | Retrieves publisher bytes; records URL, HTTP date, retrieval time and sha256 | Redirected off the asserted publisher; empty body; HTTP error; destination already holds a run |
| `read_version.py` | Matches the registry's version markers against the fetched bytes | Version unresolved or blocked; historical selection must be dated |
| `extract_provisions.py` | Splits and hashes provisions, classes them, indexes defined terms, carries provenance | Version unresolved or blocked; broken provenance; no numbering convention detected; a forced convention matches nothing; two provisions carry the same label or id |
| `verify_quotes.py` | Matches every quote in the note against the extracted provisions, and every citation against the provision holding the words; writes the run manifest | A quote is not in the fetched text, is uncited, names the wrong provision, quotes a recital as though it were operative, quotes the earlier edition as though it were current, or carries the instrument's words outside quotation marks |
| `diff_runs.py` | Compares two runs of one instrument — amended, retitled, replaced, added, removed — and the defined terms, filtered by the manifest | Exit 1 means something moved; exit 2 means the two runs are not the same instrument |
| `check_receipt.py` | Audits a `check` note's discovery coverage receipt: every dimension recorded, dynamic sources dated, negatives classified, omission challenge answered | A receipt row is missing, blank or wrongly statused; a negative finding is unqualified; the challenge has no answer; the method version is absent or superseded |

All scripts are stdlib-only. For PDF source text, use this cascade: the host's
built-in document extraction or a separately available open-source extractor,
then a firm-approved legal-grade OCR/document service when required. Feed the
resulting text or Markdown to `extract_provisions.py`; the skill never bundles
or silently installs a PDF dependency.

These scripts refuse rather than degrade. When one stops, report what it said.
Working around a refusal defeats the only thing this skill offers.

Every script reads saved files and nothing else — a pipe, a device or a
directory is refused on sight, because the whole chain depends on being able to
read the same bytes twice and hash them. Save the text and pass the path.

## Source failure and delivery gate

If official retrieval returns HTTP 202, a challenge, empty content, an error,
or inaccessible documents, reject it as evidence. Try another format or endpoint
on the verified official publisher, within a bounded retry budget (at most two
alternative attempts per source). User-supplied official downloads may be checked
with host tools, but must retain origin and version evidence; never fabricate a
fetch receipt. Secondary sources can locate a document, not substitute for it.

If official bytes, the version, extraction coverage, or attribution cannot be
verified, do not issue a definitive report on affected points. Begin **Your
answer — provisional and unverified**, identify exactly which points lack proof,
and state what document/date/check would resolve them. A failed quote is removed
or corrected; the provisional label does not license unchecked quotations. Keep
verified and unresolved points distinguishable. Do not report a complete official
source package unless every relied-on source is actually retained and linked.

**Report the attempt that happened, not the one you would have expected.** A
stop record names the command that ran, the file it was given, and what it
printed. When a stage never executed, it is "not attempted" — a different
sentence from "attempted and failed", and the only one of the two that tells the
lawyer a step is still open. Never carry a failure across inputs: an extraction
that refused a group page has established nothing about the individual section's
page, and describing it as though it had is how a source that would have worked
gets written up as unusable. Before saving a stop record, read it against the
commands you actually ran; a stop record is evidence about the run, and it is
the only part of the run nothing downstream checks.

Scripts are optional host capabilities. Without Python/network/file retention,
perform the same checks using available host tools and record their coverage;
if equivalent checks cannot be completed, use the provisional route. Never claim
script verification when the scripts did not run. Tool cascade: official public
publishers and stdlib helpers by default → firm-selected legal-grade retrieval
or document services when required, retaining official origin and version proof.

Before delivery, inspect the actual first chat response and ordinary deliverable:
answer present; default length met or exception explained; citations and
qualifications visible; law/guidance/contract separated; no repeated analysis;
verification scope accurate; unresolved application judgments left explicit.

## Bounded statutory citation handoff

For a statutory citation unit referred by another workflow, read
`references/citation-handoff.md`. Run only that bounded verification, using the
same source/version/quotation gates. This receiving interface does not enable
routing in another skill by itself.
