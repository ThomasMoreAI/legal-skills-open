# Classification Nice

Use this reference for class selection and goods/services drafting.

## Drafting Funnel

1. Inventory the goods the applicant sells and the services it performs, including realistic near-term expansion.
2. Use `get_nice_heading` or `list_nice_headings` to orient the class. A heading is not a checklist and does not cover every item in that class.
3. Search WDL terms using `search_wdl` with activity vocabulary and candidate classes.
4. Validate proposed labels with `validate_term` and distinguish exact accepted terms from close or custom wording.
5. Calibrate granularity with Swissreg examples, `get_class_combinations`, and `get_sector_benchmark` from comparable sectors.
6. Narrow wording to the genuine activity. Do not claim a full heading by default.
7. Check the filing language: Swiss national applications require German, French, or Italian labels.

## Rules

- Prefer exact WDL terms. If no accepted term fits, custom wording may be necessary; label it as custom and verify it in the live IPI classification tool before filing.
- Separate labels with semicolons.
- Draft labels in the user's working language, normally French for this plugin.
- Preserve source wording where possible.
- Avoid unsupported English-only output for Swiss national filings. If the client works in English, provide a working English explanation plus a filing-ready French, German, or Italian list.
- Treat empty or unsupported WDL rows as unusable. Do not draft from blank labels.
- Do not use a target number of labels as a quality metric. Include each commercially relevant item once, at defensible precision, and omit speculative padding.

## Frequent Patterns

- Class 35 covers advertising, business management, administration, office functions, and specified retail/wholesale services. The sale of the applicant's own goods is not itself a service; do not add class 35 mechanically to every product business.
- Class 39 is not needed for ordinary e-commerce delivery unless the applicant provides logistics/transport services as a business activity.
- Class 41 covers education, training, entertainment, sporting, and cultural activities.
- Class 42 covers scientific/technological services, software as a service, design, development, and technical consulting.
- Class 43 covers services for providing food and drink and temporary accommodation. Classify transport/delivery services separately when the applicant actually provides them.
- Class 45 covers legal services and certain personal/security services.

## Limitations

Use clauses such as `tous les services précités étant limités au domaine ...` only when they accurately narrow identifiable services. A vague field limitation cannot cure an otherwise unclear list; verify custom language with the IPI tool.

## Versioning

Use the corpus-reported Nice version. For the current package, Nice is reported as `NCL(13-2026)` and must be verified against WIPO/IPI at filing time.

## Official Sources

- [IPI — List of goods and services](https://www.ige.ch/en/protecting-your-ip/trade-marks/before-you-apply/your-ip-protection-strategy/list-of-goods-and-services): official-language requirement, precision, limits of class headings, and five-year use reminder.
- [IPI — Classification tool](https://www.ige.ch/en/services/digital-resources/online-services/classification-tool): live wording validation and early-examination guidance; use of the tool is not a legal guarantee.
- [WIPO — Nice Classification](https://www.wipo.int/classifications/nice/nclpub/en/fr/): current headings, explanatory notes, and alphabetical list.
