# Property-balancing worksheet (איזון משאבים)

Method for building an equal-value balance under the Spousal Property Relations Law, 5733-1973 (חוק יחסי ממון בין בני זוג, תשל"ג-1973), section 5. This is a preparation tool, not a court filing. Do not treat the output as a final settlement; a family lawyer confirms classification and a court gives it force.

## The rule in one line

On divorce each spouse is entitled to half the value of ALL the couple's assets (כלל נכסי בני הזוג), MINUS a closed list of excluded assets. You balance VALUE, not the physical items: one spouse can keep an asset and pay the other half its value.

## Step 1: list every asset (balanceable pool)

Include assets accrued during the marriage:

| Line item | Whose name | Current value (ILS) | Balanceable? |
|-----------|-----------|---------------------|--------------|
| Family home / real estate | | | usually yes |
| Savings and current accounts | | | yes |
| Pension / study fund / provident fund accrued in marriage | | | yes (division math -> israeli-pension-advisor) |
| Vehicles | | | yes |
| Business value / goodwill | | | usually yes |
| Securities and crypto | | | yes |

## Step 2: subtract the excluded assets (section 5)

These stay with the owning spouse and are NOT put in the pool:

- Assets owned before the marriage (ערב הנישואין).
- Gifts and inheritances received during the marriage (מתנה או ירושה).
- National Insurance / Bituach Leumi benefits (גמלה מהמוסד לביטוח לאומי).
- Personal-injury compensation (פיצוי בגין נזק גוף).
- Anything agreed in writing not to balance.

Commingling caveat: an excluded asset can be dragged back into the pool if it was mixed with joint property (for example a pre-marriage apartment re-registered in both names). Flag it, do not decide it.

## Step 3: subtract debts

Net each spouse's debts (mortgage balance, loans, overdrafts) against the pool, EXCEPT debts connected with excluded assets: section 6(a) deducts debts `למעט חובות בקשר לנכסים שאין לאזן שוויים`. A mortgage on a pre-marriage apartment leaves the balance together with the apartment. A debt only partly connected with an excluded asset (for example a refinanced mortgage partly spent on a family car) should be split into two lines, and how to split it is a lawyer question. Balancing is on net worth, not gross assets.

If a spouse's debts exceed their balanceable assets, the section 6(b) half-the-difference formula would make the other spouse share the deficit. Courts do not apply that mechanically, especially to debts not taken for the family; flag it for a lawyer rather than presenting the figure as owed.

## Step 4: compute the equalizing payment

1. Pool value = (sum of balanceable assets) minus (debts not connected with excluded assets).
2. Each spouse's share = Pool value / 2.
3. For each spouse, net position = (value of balanceable assets currently in their name) minus (debts in their name).
4. Default-rule difference = how far the higher net position sits above the half share. Under the 50/50 default that is the amount that would move to equalize, but it is arithmetic on your own classification, not a finding of what anyone owes; section 8 lets a court vary it.

The bundled script `scripts/izun_mashabim.py` does this arithmetic once you have classified each line as balanceable or excluded.

## Timing note (early balancing)

Section 5א lets a spouse ask to balance before the get is finalized once a balancing request is filed and a condition is met (for example a year has passed since a dissolution proceeding or property claim opened). Useful when one spouse stalls the get to freeze the money. Confirm eligibility with a lawyer.
