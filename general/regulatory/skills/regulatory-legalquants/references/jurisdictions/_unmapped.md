# When there is no registry entry

The registry covers a handful of jurisdictions properly. It will not cover the
one in front of you today. That is expected, and it is not a reason to lower the
standard — it is a reason to say out loud what you could not establish.

**The failure mode this file exists to prevent:** a search returns a clean,
well-formatted page with the text of the law on it, and it gets quoted. The page
belongs to a law firm, a legal database, a university, a translation project or
a regulator's summary. It reads exactly like the statute. It is not the statute,
and nothing in the output will show the difference.

## The protocol

**1. Say so first.** Before anything else, tell the lawyer this jurisdiction is
unmapped and that the version check will be weaker as a result. They may know
the publisher off the top of their head — local counsel usually does — and one
question saves the whole exercise.

**2. Find the publisher, not the best search result.** Search ranking is
popularity. Ask instead:

- Is the site operated by the state, a state body, or a body the state names?
- Does the **law itself** designate an official gazette or an official
  electronic source as authentic? Many jurisdictions do exactly this, and the
  designating provision is the answer to the question.
- Does the site make a claim about its own authority, and what exactly does it
  claim? "Official" and "authentic" are different words. Some official sites
  publish convenience copies and say so in the footer.

**2a. Four findings, and they do not substitute for each other.** Publisher
identity, publication authority, language and version are four separate
questions. A state body can host a copy it says is unofficial; an authentic text
can exist in a language you are not reading; a copy can be authentic and out of
date. Answer them one at a time and write each answer down, because the harm
here is not getting one wrong — it is letting a strong answer to one stand in
for a missing answer to another.

**The furniture trap.** A page can carry the words "official and authoritative"
in something that is not about the law at all. Illinois: the ILGA act page shows
a Google Translate modal reading *"The English language version is always the
official and authoritative version of this website"* — a translation notice
about the **website**, invisible in the ordinary page view — while the ILGA's
own user guide says the online ILCS and Public Act text is not official or
authoritative. A run read the first and titled its note an official-source
assessment.

So: the statement that settles publication authority is the publisher's
statement about the **statutory text**. Look for it where publishers put it — a
guide, an "about this database" page, a footer, or the enabling statute — and
quote it. A language notice, a cookie banner, a copyright line and an
accessibility statement are not evidence about the law. If the publisher makes
no statement about the text, record that absence as the finding rather than
resolving it in the publisher's favour.

**3. Expect the gazette split.** In a great many jurisdictions the authentic
text is the gazette as published — often a PDF, often not consolidated — while
the searchable website is an editorial consolidation with no legal status. That
is the same two-text problem EU law has, and it is more common than not. Find
out which one you have.

**4. Establish the version by hand.** With no markers to run, put the five
questions to the page yourself and write down the answers:

- Which version is this — as enacted, consolidated/revised, or in force today?
- Consolidated to what date? Where does the page say so?
- Amended since, by what instrument?
- Any provisions not yet commenced, or amendments not yet incorporated?
- Is this the authentic language?

If the page will not answer a question, that is a finding. Record it as one.

**5. Language.** If the authentic text is not in English, the English version is
either a second authentic text or it is a translation. Establish which. Never
quote a translation in an operative position without saying it is a translation
and naming who produced it. A machine translation is not a source at all.

This is a finding about the text. A site-wide notice naming a language "official
and authoritative" answers a question about the website's own pages, not about
which language the legislature enacted — step 2a.

**6. If you cannot establish provenance, do not manufacture it.** Two honest
outputs remain:

> I could not confirm an official publisher for this instrument. What follows is
> from [source], which is not the publisher, and I have not been able to verify
> the version. Treat it as a lead, not as text you can cite.

or, where the question actually turns on the wording:

> I can't answer this to a standard you could rely on. The text I can reach
> isn't authoritative and I can't date it. This needs local counsel or a
> subscription database.

The second answer is a real answer. Producing a confident memo from an unsourced
text is the specific harm this skill exists to prevent.

A third case sits between them and is the common one: the publisher is
unmistakably the state, and the state says this particular copy is not the
authentic text. That copy can carry an answer, in its own words:

> This is [publisher]'s online copy of [instrument]. [Publisher] states that
> [quote the disclaimer]. The authentic text is [publication]. I have quoted the
> online copy, and the quotations are verbatim from the bytes I retrieved from
> it; what I cannot prove is that it matches the authentic text.

A firm may set a stricter rule and require the authentic publication. What is
never acceptable is dropping the disclaimer because the domain looked official.

## Never these

- A law firm client alert or blog, however good the firm.
- A commercial database's editorial copy quoted as the text.
- A tracker, a news aggregator, or a monitoring service — these tell you an
  instrument **exists** and are genuinely useful for that. They do not tell you
  what it says.
- A model's recollection of the text. Not a source under any circumstances.
- An unofficial mirror or a scraped copy, even one that looks identical.

## Adding an entry

If you have worked a jurisdiction properly, it is worth an entry. The bar:

**Fetch at least two versions of the same instrument and watch the markers
behave both ways.** A marker you have only ever seen fire is not verified — you
do not yet know that it stays silent when it should. This is not theoretical:
`legislation.gov.uk` prints the phrase *"Original (As enacted)"* on the revised
page as well as the as-enacted one, because it is the version-switcher label. A
marker written from a single page would have misread half of all UK fetches.

So: pick an instrument that has been amended, fetch both versions with
`fetch_source.py`, extract the marker text from the saved bytes, and write only
the patterns that separate the two. Then copy the shape of `eu.md` or `uk.md`:
a `json` block with `code`, `name`, `publisher`, `publisher_name`,
`consolidated_text`, `authentic_languages`, `citation_format`,
`preferred_url_form` and `markers`, then the prose that carries the traps.

Severities:

| | |
|---|---|
| `superseded` | the fetched text is not the operative version — stops the run |
| `incomplete` | right version, known changes not written into it — stops the run |
| `info` | a fact the note must carry — does not stop the run |

The prose matters as much as the patterns. The patterns catch the version; the
prose is where a lawyer who has never worked the jurisdiction learns what it
does differently. Write the thing you had to find out the hard way.

A wrong entry is worse than no entry, because no entry sends you here.
