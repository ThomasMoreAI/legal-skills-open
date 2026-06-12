# Practice profile: Constitutional & Public Law — Cross-jurisdiction

Orchestrator cold-start for plugin `cross-jurisdiction-constitutional`. Loaded after `cross-jurisdiction/CLAUDE.md`, before invoking a specific skill.

## Scope

The interface between supranational (EU) law and national constitutional law: primacy/application precedence (Anwendungsvorrang), direct effect of EU norms, and how national courts must apply Union law. Covers the delineation between the EU legal order and member-state constitutional law, the duties of national courts, and the limits each order asserts against the other.

## Forums & authorities

Court of Justice of the European Union (CJEU) on questions of EU law; national constitutional and apex courts (e.g. the German Federal Constitutional Court, BVerfG) on the constitutional reception of EU law. The two orders interact but do not share a single hierarchy — name which court's doctrine you rely on.

## Key sources of law

- **Primacy / application precedence:** Case 6/64, *Costa v ENEL*, EU:C:1964:66; Case 106/77, *Simmenthal*, EU:C:1978:49.
- **Direct effect:** Case 26/62, *Van Gend en Loos*, EU:C:1963:1.
- **Treaty basis:** Art. 288 TFEU (legal acts of the Union), Art. 267 TFEU (preliminary reference); Charter of Fundamental Rights, Art. 51 (scope of application to member states).
- **National constitutional limits:** the German *Solange II* line (BVerfGE 73, 339) and ultra-vires / constitutional-identity review.

Attribute each rule to its order (EU vs. a named national constitution); never merge them. See `cross-jurisdiction/CLAUDE.md` for the jurisdiction guardrail.

## Citation discipline

Follow the rules in `cross-jurisdiction/CLAUDE.md`: cite EU instruments and CJEU cases in EU form (e.g. "Case 6/64, *Costa v ENEL*"), national decisions in that state's form (e.g. "BVerfGE [vol], [page]"). **Never invent** article numbers, case names, or docket numbers — verify the current Treaty article numbering (post-Lisbon TFEU/TEU) and the reported citation before relying on it.

## When this plugin does NOT apply

- One member state's purely internal constitutional law → that state's `{iso}/constitutional`
- EU-law remedies and procedure before the CJEU (preliminary ruling, actions for annulment) → `eu/litigation`
- General EU regulatory subject-matter → `eu/regulatory`

## Mandatory disclaimer in output

> This output is informational only and is not legal advice. Verify against the current
> statute, regulation, and court/agency rules before relying on it.
