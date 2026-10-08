# Citation form — NY courts and federal courts

Load when: formatting citations for a filing, or reading a citation to tell what it is.
Verified 2026-09-28: CPLR 5529(e) text; Style Manual edition.

## Which system

| Writing for | Use |
|---|---|
| NY state court papers, and anything a NY judge reads | **Official New York Law Reports Style Manual** (the "Tanbook"; 2022 edition with 2024 update; free at nycourts.gov/reporter). CPLR 5529(e) requires NY decisions to be cited **from the official reports, if any**, in appellate briefs; follow it everywhere in NY state practice |
| Federal court | *The Bluebook* (plus the court's local rules) |
| Internal memo | Either, consistently. Prefer official NY reports for NY cases |

## Reporters you'll see

| Court | Official | Unofficial (West) |
|---|---|---|
| NY Court of Appeals | N.Y., N.Y.2d, N.Y.3d | N.E., N.E.2d, N.E.3d; N.Y.S.2d/3d |
| Appellate Division | A.D., A.D.2d, A.D.3d | N.Y.S., N.Y.S.2d, N.Y.S.3d |
| Trial courts, Appellate Term | Misc., Misc. 2d, Misc. 3d | N.Y.S.2d/3d |
| Online-only / unreported NY | NY Slip Op (unreported: "(U)") | |
| U.S. Supreme Court | U.S. | S. Ct.; L. Ed./L. Ed. 2d |
| Courts of appeals / district courts | | F., F.2d, F.3d, F.4th; F. Supp. 2d/3d; F. App'x |

## Shapes

```
Tanbook:   Babcock v Jackson, 12 NY2d 473 [1963]                (no periods in v / NY2d; brackets for year)
           Matter of Smith, 45 AD3d 123, 125 [2d Dept 2007]     (department in the bracket)
           People v Doe, 2023 NY Slip Op 01234 [1st Dept 2023]
           CPLR 3211 (a) (7); EPTL 3-2.1 (a) (4); Penal Law § 125.25 (1)

Bluebook:  Babcock v. Jackson, 12 N.Y.2d 473, 481 (1963).
           Mountain View Coach Lines, Inc. v. Storms, 102 A.D.2d 663 (2d Dep't 1984).
           N.Y. C.P.L.R. 3211(a)(7) (McKinney 2026).
           28 U.S.C. § 1332(a); Fed. R. Civ. P. 12(b)(6); Fed. R. Evid. 803(2).
```

The pinpoint page (", 481") is required when citing a specific holding. A cite without one is
a signal the proposition wasn't located in the opinion.

## Red flags in a draft (likely fabricated or wrong)

- A reporter that doesn't match the court (an "A.D.3d" cite for a Court of Appeals case; F.3d
  for a district court).
- A year outside the reporter's run (N.Y.3d began in 2003; A.D.3d in 2003; F.4th in 2021;
  F. Supp. 3d in 2014).
- A case name that doesn't match the record name at that volume and page (`cite_check.py`
  reports `NAME-MISMATCH`).
- A quotation with no pinpoint, or a quotation you can't find in the opinion.
- Westlaw/Lexis cites (`2021 WL 1234567`) for a published case that has an official cite.
