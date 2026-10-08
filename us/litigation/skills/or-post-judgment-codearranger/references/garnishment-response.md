# Garnishment Response — Oregon

When a judgment creditor obtains a Writ of Garnishment, the
debtor receives a **Notice of Writ of Garnishment** (ORS
18.625). The debtor has **30 days** to file a Challenge to
Writ of Garnishment claiming exemptions.

## Two types of garnishment

### Wage garnishment

Writ served on the debtor's **employer**. The employer:

- Withholds up to 25% of disposable earnings (ORS 18.385)
- Withholds nothing if disposable earnings are below ~40×
  federal minimum wage
- Pays the withheld portion to the court

Wage garnishment continues until the judgment is satisfied
or the debtor leaves the employer.

### Bank levy (account garnishment)

Writ served on the debtor's **bank**. The bank:

- Freezes funds in the account up to the judgment amount
- Holds the funds for a waiting period (typically 10–21 days
  per ORS 18.638)
- After the waiting period, pays to the court unless the
  debtor files a successful Challenge

Bank levy is **one-time** — it captures funds in the account
on the day of service. Future deposits are not captured.

## The 30-day Challenge window

ORS 18.700+ governs Challenges. The 30-day clock starts on
the date the debtor receives the Notice of Writ of
Garnishment (which the creditor must serve on the debtor
under ORS 18.625).

### What to file

The OJD form is **Notice of Exemption Claim and Request for
Hearing** (CV-W-1 or similar — pull current form from
courts.oregon.gov/forms). The Challenge:

- Identifies the writ being challenged
- States which property is claimed exempt
- States the statutory ground for each exemption
- Requests a hearing

### Where to file

File in the court that **issued the writ** (typically the same
court that entered the judgment). On File and Serve. Serve the
creditor under ORCP 9.

### What happens after filing

The court holds a hearing within ~21 days. At the hearing:

- The debtor must show the property is exempt
- The creditor can rebut
- The court orders release of exempt funds or upholds the
  garnishment

## Exemption analysis — wage garnishment

For a wage garnishment, the analysis is mostly mechanical:

1. **Compute disposable earnings**: gross wages – mandatory
   deductions (federal/state tax, FICA, mandatory retirement)
2. **If disposable earnings < 40× federal minimum wage per
   week** (~$290/week at $7.25 federal min wage; verify
   current): **zero garnishment**
3. **If above the threshold**: garnishment is the lesser of
   25% of disposable, OR the amount by which disposable
   exceeds 40× minimum wage

### Federal benefits going into wages

If the debtor's wages reflect deposit of federal benefits
(Social Security, VA, federal retirement), the benefits
portion is fully exempt and should not be garnished from
wages. Pull the wage history and identify the federal-benefit
portion.

### Hardship deviation

ORS 18.385 allows a debtor to ask the court to reduce the
garnishment percentage on a showing of hardship. The court has
discretion; the debtor must show actual hardship (eviction,
medical, dependents) and that the standard 25% is unsustainable.

## Exemption analysis — bank levy

A bank levy is more fact-specific. Common exemption scenarios:

### Direct-deposited federal benefits (31 CFR 212)

If the levied account received Social Security, SSI, VA, or
federal retirement benefits within 2 months before the levy,
the bank must apply a **safe-harbor protection** equal to the
sum of those benefits.

To claim: file the Challenge identifying:

- The specific federal benefits deposited
- The dates and amounts of deposits
- The protected amount under 31 CFR 212

Attach bank statements showing the federal-benefit deposits.

### Direct-deposited Oregon benefits

ORS 18.345 protects:

- Unemployment compensation
- Workers' compensation
- Public assistance (TANF, OHP)
- Other identified state benefits

The protection applies to identified state benefits even when
commingled in a general checking account — but commingling
makes the showing harder. Best practice: maintain a separate
account for benefits if possible.

### Wages deposited in account

Once wages are deposited in a bank account, they generally
**lose** their wage-exemption character under Oregon law
(unlike federal benefits, which retain their exempt
character). Wages in a bank account are subject to garnishment
unless they are a recent direct deposit (in which case some
courts treat them as tracing to the wage exemption).

This is a fact-specific area; consult counsel if the levy is
significant.

### Joint accounts

If the account is jointly held with a non-debtor (spouse,
adult child), the non-debtor's portion is not subject to the
judgment. The Challenge should identify what portion belongs
to the non-debtor.

### Identifiable trust funds

Funds held in trust for another (e.g., child's savings) are
not the debtor's property and not subject to the judgment.

## Challenge to Writ — sample form content

```
            IN THE CIRCUIT COURT OF THE STATE OF OREGON
                  FOR THE COUNTY OF MULTNOMAH

VELOCITY INVESTMENTS, LLC,      │   Case No. 25CV12345
                                │
     Plaintiff/Judgment         │   CHALLENGE TO WRIT OF
     Creditor,                  │   GARNISHMENT AND CLAIM
                                │   OF EXEMPTION UNDER
     v.                         │   ORS 18.700 ET SEQ.
                                │
JOHN DOE,                       │   REQUEST FOR HEARING
                                │
     Defendant/Judgment         │
     Debtor.                    │
────────────────────────────────────────────────────────────

Defendant John Doe, pro se, challenges the Writ of
Garnishment issued in this matter and claims the following
exemptions:

1.  WRIT IDENTIFICATION

    Writ issued: [date]
    Garnishee: [Wells Fargo Bank / employer]
    Notice served on Defendant: [date]
    Amount garnished: $[amount]

2.  EXEMPTION CLAIMED

    [Select applicable categories — example for bank levy
     containing federal benefits:]

    Defendant claims the following amounts as exempt under
    31 CFR 212 and ORS 18.345:

    -  Social Security retirement benefits deposited on
       [dates]: $[amount]
    -  VA disability compensation deposited on [date]:
       $[amount]

    Total exempt: $[amount]

    These funds are federal benefits as defined in 31 CFR
    212. The bank was required to apply the safe-harbor
    protection but did not. Bank statements showing the
    deposits are attached as Exhibit 1.

3.  REQUEST FOR HEARING

    Defendant requests an in-person hearing under ORS
    18.700, at the earliest available date.

4.  CONTACT INFORMATION FOR SERVICE

    [Address, phone, email]

DATED this ____ day of __________, 20__.

______________________________________
JOHN DOE
Defendant/Judgment Debtor, pro se
[Address]
[Phone]
[Email]


                  CERTIFICATE OF SERVICE
[Per UTCR 1.090, served on Plaintiff's counsel by email and
USPS Certified Mail]
```

## Hearing preparation

The Challenge hearing is held within ~21 days of filing.
Bring:

- Bank statements showing the deposits and source
- Pay stubs (if wage garnishment)
- Award letters for federal benefits (Social Security
  notice, VA letter)
- The notice of writ
- Bank levy confirmation
- A computation of the exempt amount

The hearing is typically before the assigned civil judge,
either in-person or WebEx (per the assigned judge's standing
order). See `or-hearings` for general hearing prep.

## After the hearing

If the court grants the exemption:

- The bank releases the exempt funds back to the debtor (or
  the levy is reduced to the non-exempt amount)
- The order goes to the bank/employer through the
  garnishment process

If the court denies the exemption:

- The garnishment proceeds
- Consider whether to appeal (ORS 19.255 — 30 days)
- Consider whether other property is now at risk

## Continuing garnishment after partial release

If only some property is exempt, the garnishment continues
against the non-exempt portion. The debtor may need to claim
new exemptions if circumstances change (new wage period, new
federal-benefit deposit, etc.).

## Subsequent garnishments

A creditor can issue multiple writs over the 10-year judgment
life. Each writ triggers a new 30-day Challenge window. Don't
assume one Challenge protects against future writs.

## Pro se debt-defense overlap

For consumers in debt-collection cases, garnishment response is
often the last opportunity to vacate the underlying judgment
(see `references/motion-to-vacate.md`). Combine:

- Challenge to Writ — claim exemptions, get the garnishment
  released
- Motion to Vacate — re-open the case on the merits

Both can be filed in parallel. Some debtors win the Challenge
on exemptions but still want to vacate the judgment to clear
their credit and stop future writs.

## References

- `or-post-judgment` SKILL — overall framework
- `references/exemptions.md` — full annotated exemption
  catalog
- `references/motion-to-vacate.md` — ORCP 71 motion
- `or-deadlines` — 30-day computation
- `or-hearings` — Challenge hearing prep
- `or-law-references/references/or-ors-debt/ORS-18.md` (when
  populated) — verbatim ORS 18 text
