# Source policies for employment-law work

When researching or building dashboards for US employment law, the source you cite depends on the *type of statement* you're making. There are two buckets, and the rules are different.

## Bucket A — "Statutory claim" content (PRIMARY SOURCES ONLY)

Any statement about what the law actually says or requires. This includes:

- The text of a statute, rule, or regulation.
- An effective date.
- A penalty amount, cure period, enforcement authority, private right of action.
- A statutory definition (of "AI," "automated decision system," "covered employer," etc.).
- Required notice content, recordkeeping period, audit obligation, etc.
- Whether a particular obligation applies to a particular kind of employer.

For these statements, cite **only**:

1. The statute itself (link to the official legislative text — `.gov`, `.us`, or the official state legislature site).
2. The regulation or rule (link to the official rules code).
3. Official agency guidance hosted on a government domain (e.g., DCWP page on `nyc.gov`, IDHR page on `illinois.gov`, EEOC guidance on `eeoc.gov`).

**Do NOT cite** law firm summaries, secondary commentary, news articles, or even reputable trackers — even if they happen to be accurate. Primary sources only. If you can't find a primary source for a claim, that's a signal to re-examine the claim itself rather than to fall back on secondary support.

## Bucket B — "Lay of the land" content (SECONDARY SOURCES WELCOME)

Statements about the broader landscape — what's happening, who's tracking it, what practitioners are saying. This includes:

- Multi-state trackers and surveys ("here are the comprehensive trackers practitioners use").
- Recent reporting and analysis ("here's a Cooley alert from last month explaining the landscape").
- Counts of pending bills across states ("25+ states have pending legislation" — sourced to a tracker org, not the statutes themselves).
- Practitioner perspectives, recommended approaches, soft warnings.

For these, cite reputable secondary sources:

- Major law firm alerts (Littler, Cooley, K&L Gates, Greenberg Traurig, etc.).
- Tracker organizations (Multistate.ai, Bloomberg Law, etc. — note that NCSL has been less reliably updated for AI legislation since 2024).
- Established legal publications (National Law Review, Bloomberg Law, Law360).
- Government agency reports and audits (e.g., NYC Comptroller).

Avoid: blog posts from unknown authors, marketing content from vendors, AI-generated summaries.

## How this maps to dashboard sections

| Section | Bucket | Why |
|---|---|---|
| Masthead meta stats | A (with footnote → B) | Stats like "25+ states with pending bills" need a tracker citation |
| TL;DR | A | Statements like "five enacted laws, three already live" must be backed by primary sources |
| Multi-state trackers section | B | This *is* a list of secondary trackers |
| Recent articles section | B | This *is* a list of secondary commentary |
| Comparison table — every cell | A | These are compliance claims about specific laws |
| Comparison table — "Law" column citations | A | Statute, reg, official guidance only |
| Deep dive card | A | Statutory requirements |
| Footer / footnotes | Either | Whichever the underlying claim is |

## A quick gut check

When you write a sentence, ask: "If a litigator put this in a brief, would they cite the statute, or would they cite a Cooley alert?" If the answer is the statute, use Bucket A. If the answer is the Cooley alert, use Bucket B.

If you're tempted to cite a law firm alert because the statute is hard to find or hard to read, push through. Find the statute. The whole point of the dashboard is to be a thin layer over primary sources.
