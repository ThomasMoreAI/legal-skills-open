# Domain coverage checklist: Israeli workplace rights

Anchor for the Expert Review gate. Each row is enumerated at the level the rate actually varies, so a one-line "topic covered" entry cannot hide a missing sub-rate.

## Must cover (core)

### Minimum wage (Minimum Wage Law, 1987; Minimum Wage Regulations (Working Youth and Apprentices), 1987)

Enumerate every band as its own row. The statute sets youth pay as a percentage of the adult monthly minimum, so a skill carrying only the adult row overstates a young worker's entitlement.

| Row | Covered? | Where |
|-----|----------|-------|
| Adult full-time monthly minimum | Yes | SKILL.md Step 4, `entitlements-calculator.md` |
| Adult hourly minimum (monthly / 182) | Yes | same |
| Youth up to age 16, 70% | Yes | `entitlements-calculator.md` youth table |
| Youth up to age 17, 75% | Yes | same |
| Youth up to age 18, 83% | Yes | same |
| Apprentice (chanich) under the Apprenticeship Law, 60% | Yes | same |
| Youth full-time week is 40 hours and the youth hourly divisor is 173, not 182 | Yes | same |
| Birthday-month pro-rata split between bands | Yes | same |
| Part-time pro-rating | Yes | SKILL.md Step 4 |

### Overtime and weekly rest day (Hours of Work and Rest Law, 1951, ss.16-17)

Enumerate each hour tier on each day type. The rest-day premium and the overtime premium are separate entitlements that stack, so a flat rest-day rate understates a long shift.

| Row | Covered? | Where |
|-----|----------|-------|
| Weekday, first 2 overtime hours, 125% | Yes | SKILL.md Step 4 |
| Weekday, beyond 2 overtime hours, 150% | Yes | same |
| Rest day, ordinary hours, 150% | Yes | same |
| Rest day, first 2 overtime hours, 175% | Yes | same |
| Rest day, beyond 2 overtime hours, 200% | Yes | same |
| Cumulative method caps at 200% | Yes | `entitlements-calculator.md` overtime section |
| Monthly salaried vs hourly/daily split on the rest-day premium (50% addition vs 150% full rate) | Yes | same |
| Compensatory rest: paid for monthly salaried, unpaid for hourly/daily, never redeemable in money | Yes | same |
| Pension and severance provisioning on rest-day hours | Yes | same |
| 16 overtime hours per week ceiling, 12-hour day ceiling (general permit 14.03.2018) | Yes | SKILL.md Step 4 |
| Managers and personal-trust exemption | Yes | SKILL.md Step 4, Troubleshooting |

### Other core areas

| Row | Covered? |
|-----|----------|
| Annual leave table by seniority, both the calendar-day gross column and the 5-day-week net column | Yes |
| Sick pay: day 1 at 0%, days 2-3 at 50%, day 4 onward at 100%; accrual 1.5 days/month; 90-day cap | Yes |
| Child sick days, including the malignant-illness and dialysis tracks | Yes |
| Convalescence pay: days by seniority, private and public daily rates | Yes |
| Severance: one month per year, s.14 arrangement, 6% vs 8.33% distinction, tax-exemption ceiling | Yes |
| Notice period: monthly vs hourly/daily, by tenure tier | Yes |
| Birth and parenting period, paternity leave, birth allowance eligibility and daily cap | Yes |
| Mandatory pension rates and the s.45a tax credit | Yes |
| Pay slip duty (Wage Protection Law s.24) | Yes |
| Dismissal protections, pregnancy, harassment prevention, disability accommodation | Yes |

## Should cover (advanced)

| Row | Covered? |
|-----|----------|
| Travel reimbursement (Travel-to-Work Extension Order) | Yes |
| Motzaei Shabbat and Friday-into-Shabbat boundary rules for the rest-day premium | Partly, summarised in `entitlements-calculator.md` |
| Global overtime pay arrangements (gmul globali) | No, deferred |
| Holiday (chag) pay as distinct from weekly rest day | No, deferred |
| Youth employed on the weekly rest day: the employment is unlawful, but the overtime premium is still owed | No, deferred |

## Out of scope (explicit)

- **Drafting or reviewing an employment contract.** Routed to `israeli-employment-contracts` and `israeli-employment-contract-reviewer`. Reviewed 2026-08-19: still out of scope; a user asking this is asking for a different work product, not a missing rate. (Reviewed 2026-08-19)
- **Reserve-duty (miluim) pay and protections.** Routed to `israeli-miluim-manager`. Reviewed 2026-08-19: an ordinary user would ask for it, and the routing already answers them; the figures are maintained in that skill and duplicating them here would create a drift surface. (Reviewed 2026-08-19)
- **Salary negotiation and market rates.** Routed to `israeli-tech-salary-negotiator`; not a statutory entitlement. (Reviewed 2026-08-19)
- **Foreign-worker and live-in caregiver specific regimes** (25-hour weekly rest, caregiver rest-day compensation). Named and pointed at, not enumerated; a distinct statutory regime with its own rate structure. (Reviewed 2026-08-19)
- **Sector-specific collective agreements and extension orders** (cleaning, security, catering, waiting staff). The skill states the statutory floor and that a more favourable agreement prevails; enumerating every sector's grid is a different skill. (Reviewed 2026-08-19)

## Authoritative sources

| Source | URL |
|--------|-----|
| Kol Zchut, youth pay | https://www.kolzchut.org.il/he/תשלום_שכר_לבני_נוער |
| Kol Zchut, weekly rest day premium | https://www.kolzchut.org.il/he/גמול_עבור_העסקה_במנוחה_השבועית |
| Kol Zchut, minimum wage | https://www.kolzchut.org.il/he/שכר_מינימום |
| Ministry of Labour | https://www.gov.il/he/pages/aboutlabor |
| Nevo, Severance Pay Law | https://www.nevo.co.il/law_html/law01/p189_001.htm |
