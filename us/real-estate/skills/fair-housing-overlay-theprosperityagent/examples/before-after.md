# Before / After — fair-housing-overlay

## Rule Set 1 — FHA patterns

**Before (no overlay):**

> Beautiful 3-bedroom home in a wonderful family-friendly neighborhood with great schools nearby. Perfect for young professionals or growing families! Safe, quiet streets and a tight-knit community.

**After (overlay loaded):**

> Three-bedroom home with an open floor plan, primary suite on the main level, and a 0.4-acre lot. 12 minutes to the regional medical center, 8 minutes to downtown Springfield, and a public park three blocks over.

What changed:
- "Family-friendly neighborhood" → dropped. Replaced with objective lot + features.
- "Great schools nearby" → dropped. Replaced with commute time + park.
- "Perfect for young professionals or growing families" → dropped. FHA demographic.
- "Safe, quiet streets" → dropped. "Safe" has no compliant replacement. "Quiet" only if backed by objective data.
- "Tight-knit community" → dropped. Coded FHA demographic.

## Rule Set 2 — TCPA patterns

**Before (no overlay):**

> Reaching out to all the past Zillow leads we have on file! We have some amazing new listings — text me back if interested.

**After (overlay loaded):**

> SKILL REFUSED. This pattern reads as cold-list re-engagement targeting non-currently-opted-in contacts. TCPA prohibits unsolicited blast outreach to consumers without prior express written consent. The skill outputs nothing for this prompt.

Redirect: route to a re-consent path (one-time opt-in form, re-subscribe link, permission-based ad). After re-consent, the contact is back in the cadence.

## Rule Set 3 — MLS data quality

**Before (no overlay):**

> A must-see hidden gem in Springfield! This rare opportunity won't last long. Act now — priced to sell!

**After (overlay loaded):**

> Brand-new listing in Springfield. Four-bedroom, three-bath plan with a screened porch off the back and primary on the main. Built in 2018 — recent systems. 0.6-acre fenced lot.

What changed: 7 banned clichés removed. MLS feeds (Realtor.com, Zillow, Redfin) downrank pages with these phrases. Removal both protects compliance AND helps SEO.

## Rule Set 4 — Always positive

**Before (no overlay):**

> Unlike the overpriced new construction across town, this home offers real value in a still-affordable Springfield neighborhood. Skip the bidding wars at a competing builder and come see what real value looks like.

**After (overlay loaded):**

> SKILL REFUSED. This pattern knocks competing builders by name. NAR Code of Ethics Article 12 prohibits making misrepresentations about other agents or their listings. Always-positive rule blocks competitor takedowns.

Rewrite (skill returns):
> Strong value at $385K for a 4-bedroom on a 0.6-acre fenced lot in Springfield. Recent build, current finishes, and an open floor plan.

## A real bilateral example — the LinkedIn post that almost shipped

Victoria drafted a LinkedIn post critiquing Zillow's iBuyer model. The overlay caught it:

**Before:**
> Zillow's iBuyer experiment cost them $500M and proved what we always knew — algorithms don't understand neighborhoods like local agents do. Don't trust your largest financial decision to a Zestimate.

**After (overlay's always-positive rule):**
> Local agents bring something to a transaction that lives outside an algorithm — relationship with the listing agent on the other side, knowledge of pending inspections in the neighborhood, eyes on whether your kitchen update will return at sale. These are the things a kitchen-table conversation surfaces that no number can.

Same point landed without the Zillow takedown. Less SEO competition (no negative keyword association), zero NAR-Code-of-Ethics-Article-12 risk, more constructive for the reader.

## The compounding case

A single FHA violation in a public listing description, caught by HUD, results in:

- $16,000-$21,000 first-violation civil penalty (federal).
- License-defense legal costs: $5,000-$50,000+.
- Brokerage exposure (your broker can be named).
- Reputational damage in a small market.

Annual cost of running the overlay: $0 (it's a skill file).

The math is overwhelming.
