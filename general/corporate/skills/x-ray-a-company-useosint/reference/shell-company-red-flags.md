# Shell-company red-flag catalogue

A shell is a company with no substantive operations. Shells are legal and
extremely common — holding companies, dormant subsidiaries, special-purpose
vehicles, and newly formed startups all look like shells on paper. The question
is never "is this a shell" but "is this a shell being used to obscure something,
in a context where that matters".

Score the cluster. Single indicators are noise.

## Weighting

- **Low** — ordinary in legitimate business; only meaningful in combination.
- **Medium** — warrants a specific explanation from the counterparty.
- **High** — proceed only with a documented, verified explanation.

## Registration and address

| Indicator | Weight | Why it is ambiguous |
|---|---|---|
| Registered office shared with hundreds or thousands of entities | Low-medium | Company formation agents and accountants legitimately host thousands of clients. Check what the address actually is before weighting it: a professional firm is ordinary; a mail-forwarding box or a residential flat with 900 companies is not |
| Registered office is a virtual office or mail drop | Medium | Common for genuine small and remote businesses |
| Registered office in a jurisdiction with no connection to the business, directors, or customers | Medium-high | Legitimate for tax and IP structuring; suspicious when combined with opacity |
| Incorporated shortly before the transaction it is party to | Medium-high | SPVs are created for transactions all the time; the flag is a *new* entity claiming an *old* track record |
| Repeated changes of registered office in a short period | Medium | Often just a change of accountant |
| Name closely mimicking an established company | High | Rarely accidental. Check for a legal-form suffix swap, a missing word, or a lookalike character |

## Officers and ownership

| Indicator | Weight | Why it is ambiguous |
|---|---|---|
| A single director who is also director of many unrelated companies | Medium | Professional directors and company-secretarial firms are a legitimate industry |
| Directors resident in a jurisdiction unconnected to operations | Medium | Normal in international groups |
| Officers appointed and resigned in rapid succession | Medium-high | Sometimes genuine churn at formation |
| Corporate directors rather than natural persons | Medium | Restricted or banned in some jurisdictions; where allowed, it is a legitimate group practice but adds a layer |
| Ownership chain terminating in a jurisdiction with no public register | Medium-high | Extremely common; the flag is the combination with other indicators, not the jurisdiction itself |
| Beneficial owner declared as "none identified" or the entity itself | High | Legally permitted in narrow circumstances; usually means the chain was not walked |
| Directors with prior companies dissolved after compulsory strike-off or insolvency | High | Business failure is normal once; a pattern is not |
| Nominee arrangements evidenced by a director who cannot answer basic operational questions | High | Only detectable outside OSINT, but worth noting as the follow-up question |

## Operations and footprint

| Indicator | Weight | Why it is ambiguous |
|---|---|---|
| No web presence at all | Medium | Genuine for holding entities and B2B contractors |
| Domain registered after the claimed founding date, or very recently | Medium-high | Rebrands and domain acquisitions happen; ask for the prior domain |
| Website is a template with stock imagery and no named staff | Medium | Common for small firms |
| No employees on any professional network, or a workforce that does not match the claimed scale | Medium-high | Skews heavily by country and sector; weak signal outside major markets |
| No filed accounts, or accounts showing no activity, in an entity claiming substantial trading | High | Dormant filings are unambiguous when the pitch claims revenue |
| No sectoral licence for a business that legally requires one | High | Check the specific regulator; this is often the fastest disqualifier |
| No physical premises evidence — the address is not a building consistent with the operation | Medium-high | Remote and distributed businesses are normal now |

## Financial and transactional

| Indicator | Weight | Why it is ambiguous |
|---|---|---|
| Payment requested to a bank in a jurisdiction unconnected to the entity, directors, or work | High | Legitimate for multinationals with treasury centres; a strong flag for a small entity |
| Bank account name differs from the contracting entity name | High | Also the signature of invoice-redirection fraud |
| Payment terms or structure that make no commercial sense — round sums, prepayment, unusual currency | Medium-high | Sector-dependent |
| Accounts filed late, repeatedly | Medium | Small companies file late constantly |
| Auditor resignation or a qualified opinion | High | Rare enough to be meaningful |

## Structural

| Indicator | Weight | Why it is ambiguous |
|---|---|---|
| Multiple layered entities with no apparent commercial purpose | Medium-high | Tax and liability structuring is a real purpose; the flag is layering without one |
| Circular or self-referential ownership between group entities | High | Occasionally a legacy artefact |
| A group where every entity shares one address and one director | Medium | Standard for small family groups |
| Entity is a party to contracts far larger than its balance sheet supports | High | Ask who is standing behind it and get that in writing |

## Reading the score

- **One or two low/medium indicators** — normal small business. Note and move on.
- **Three or more medium indicators clustering across different categories** —
  the pattern is doing work. Ask specific questions and require documents.
- **Any single high indicator, or two mediums plus opacity in ownership** —
  do not proceed on OSINT alone. Escalate to enhanced diligence, and in a
  regulated context consider your reporting obligations.

## The two counter-errors

Do not confuse **opacity** with **wrongdoing**. Plenty of entirely legitimate
businesses are structured through jurisdictions that publish nothing, for
liability, privacy, or tax reasons that are entirely lawful. Your finding is that
you could not verify, and the correct output is a stated residual risk, not an
accusation.

Do not confuse **substance** with **legitimacy** either. A sophisticated fraud
will have employees, an office, a website with named staff, and filed accounts.
The shell checklist catches lazy structures. It does not catch good ones — for
those, the signal is in Step 6's litigation and procurement history and in Step 7's
adverse media, not here.
