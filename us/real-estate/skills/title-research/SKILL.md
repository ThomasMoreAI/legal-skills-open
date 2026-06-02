---
name: title-research
title: Title Researcher Agent
description: Title and due diligence agent. Verifies clear title and researches liens.
author: Dbillionaer
author_url: https://github.com/Dbillionaer/wholesaile/tree/main/workspace/skills/title-research
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: us
practice: real-estate
language: en
---

# Title Researcher Agent

Verify clear title, identify liens, and ensure deals can close.

## Knowledge Base Integration

**Before researching title**, load relevant guides:

```
# Load title research playbook
memory_get("Understanding_and_Working_with_Your_Title_Company.md")
memory_get("Contract_Walkthroughs_Guide.md")

# Find trusted title companies in this area
memory_search("title company [CITY/STATE] trusted vendor")
memory_search("title company contact [ZIP CODE]")

# Check for known issues in this area
memory_search("title issue [COUNTY] common problems")
memory_search("agent lesson title problem [deal type]")
```

**After completing title research**, write findings to deal file and note any new patterns:
```
# Update: ~/.openclaw/workspace/deals/[deal-file].md
# If new title issue pattern found, note in agent-lessons
```

## Research Sources

| Document | Source | What to Look For |
|----------|--------|-----------------|
| Deed | County Recorder | Current owner, title type, transfer history |
| Mortgage | County Recorder | Outstanding loans, lender info |
| Tax Lien | County Treasurer | Unpaid property taxes |
| Federal Tax Lien | IRS / County | IRS liens (take priority) |
| Judgment Lien | County Clerk | Court-ordered debts |
| HOA Lien | County Recorder | Unpaid HOA dues |
| Lis Pendens | County Clerk | Active lawsuits |
| Bankruptcy | Federal PACER | Active bankruptcy proceedings |

## Title Search Process

1. **Ownership Verification** — Confirm seller has authority to sell
   - Search: "[COUNTY] county recorder property search [ADDRESS]"
   
2. **Chain of Title** — Trace ownership 10+ years
   - Look for gaps, quitclaim deeds, unusual transfers
   
3. **Lien Search** — Find all encumbrances
   - Tax liens, judgment liens, HOA liens, mechanic's liens
   
4. **Encumbrance Check** — Easements, restrictions, covenants
   - HOA rules, deed restrictions, utility easements

5. **Bankruptcy Check** — Federal PACER search
   - Search: pacer.gov for seller's name

## Deal-Killers (Walk Away)

| Issue | Why It's a Problem |
|-------|-------------------|
| Active IRS Tax Lien | Takes priority over all other liens |
| Active Bankruptcy | Automatic stay prevents transfer |
| Active Lawsuit (Lis Pendens) | Cannot transfer during litigation |
| Multiple Mortgages > ARV | Underwater, no equity to work with |
| Clouded Title | Ownership dispute, cannot close |

## Workable Issues (Can Negotiate)

| Issue | Solution |
|-------|----------|
| Property Tax Delinquency | Negotiate payoff at closing |
| HOA Lien | Negotiate payoff at closing |
| Judgment Lien | Negotiate settlement |
| Mechanic's Lien | Negotiate payoff |
| Old Mortgage (paid off) | Get release/satisfaction deed |

## Title Research Output Format

```markdown
## Title Report: [ADDRESS]

**Owner of Record**: [Name] (matches seller: ✅/❌)
**Title Type**: Fee Simple / Joint Tenancy / Tenancy in Common / Trust

**Liens Found**:
| Type | Amount | Holder | Status |
|------|--------|--------|--------|
| Mortgage | $[X] | [Lender] | Active |
| Tax Lien | $[X] | [County] | Delinquent |

**Total Encumbrances**: $[X]
**Estimated Equity**: $[ARV] - $[Encumbrances] = $[X]

**Deal-Killers**: None / [List if any]
**Workable Issues**: [List with proposed solutions]

**Recommendation**: ✅ CLEAR TO PROCEED / ⚠️ NEGOTIATE LIENS / ❌ WALK AWAY

**Preferred Title Company**: [Name] | [Phone] | [Why recommended]
```

## Title Company Selection

Search for trusted title companies:
```
memory_search("title company [CITY STATE] trusted")
memory_search("title company contact [ZIP]")
```

If none found, search online and add to knowledge base:
```
# Add to: ~/Documents/wholesale-kb/market-data/[ZIP]-market-notes.md
# Under "Title Companies Active in Area"
```

## Level 3 Helper
Use scripts/county-lookup.sh for FL clerks.

## Level 3 Helper
Run `./scripts/county-lookup.sh` for FL county clerk sites.
