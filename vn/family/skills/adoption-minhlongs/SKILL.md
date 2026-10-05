---
name: adoption-minhlongs
title: Vietnamese Child Adoption & Hague Intercountry Adoption Suite (`mekong adoption` / `mekong connuoi`)
description: Vietnamese Child Adoption & Hague Intercountry Adoption Suite (Law 52/2010 & Decree 19/2011).
author: minhlongs
author_url: https://github.com/minhlongs/mekong-cli/tree/main/.agents/skills/adoption
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: vn
practice: family
language: en
---

# Vietnamese Child Adoption & Hague Intercountry Adoption Suite (`mekong adoption` / `mekong connuoi`)

The **Child Adoption Suite** codifies statutory procedures for domestic child adoption, intercountry adoption under the 1993 Hague Convention, post-placement semi-annual monitoring, official certificate issuance, and judicial terminations under:
- **Law on Adoption 2010 (Luật Nuôi con nuôi - Law No. 52/2010/QH12)**.
- **Decree No. 19/2011/ND-CP** detailing the implementation of the Law on Adoption.
- **Decree No. 24/2019/ND-CP** amending and supplementing Decree No. 19/2011/ND-CP.
- **Circular No. 10/2020/TT-BTP** on adoption forms, records, and registries.
- **Hague Convention on Protection of Children and Co-operation in Respect of Intercountry Adoption 1993**.
- **Law on Marriage and Family 2014 (Law No. 52/2014/QH13)**.

---

## Key Capabilities

1. **Eligibility Screening & Age Rules (Điều 8 & Điều 14 Law 52/2010)**:
   - Validates child eligibility: under 16 years of age, or 16 to under 18 if adopted by step-parent or aunt/uncle.
   - Adopter age difference check: unrelated adopter must be at least 20 years older than the adopted child. Step-parents and aunts/uncles are statutorily exempted from the 20-year gap.
2. **Statutory Consent Verification (Điều 21)**:
   - Mandatory consent of biological parents or legal guardians.
   - Mandatory direct consent of the child if 9 years of age or older.
3. **1993 Hague Intercountry Adoption Processing (Điều 28-43)**:
   - Coordination with the Department of Child Adoption - Ministry of Justice (`Cục Con nuôi - Bộ Tư pháp`).
   - Accreditation of foreign adoption agencies, home study report verification, and Provincial People's Committee adoption decision.
4. **Post-Placement Monitoring & Child Welfare (Điều 23 & Điều 39)**:
   - Enforces semi-annual welfare reports (6, 12, 18, 24, 30, and 36 months) for 3 consecutive years post-handover.
   - Tracks physical health, linguistic/educational adaptation, and psychological well-being.
5. **Certificates & Register Books (Thông tư 10/2020/TT-BTP)**:
   - Issues official Certificate of Adoption (`Giấy chứng nhận nuôi con nuôi`) and records entry into the National Adoption Register Book with digital signature verification.
6. **Judicial Termination of Adoption (Điều 25-27)**:
   - Enforces court judgments terminating adoption in cases of serious abuse or mutual agreement upon adulthood, updating child custody arrangements and revoking certificates.

---

## CLI Commands

```bash
# Executive Dashboard & Telemetry
mekong adoption
mekong adoption --json
mekong adoption status --json
mekong connuoi --json

# Domestic Adoption Application
mekong adoption apply --type DOMESTIC --adopter "Nguyen Van Binh" --adopter-dob "1980-05-15" --adopter-id "001080001234" --child "Tran Bao An" --child-dob "2020-08-20" --gender MALE --origin "Trung tam Bao tro xa hoi 1 Ha Noi" --rel UNRELATED

# Step-Parent Adoption (Exempt from 20-Year Age Difference Gap)
mekong adoption apply --type DOMESTIC --adopter "Pham Minh Duc" --adopter-dob "1994-03-10" --adopter-id "001094005678" --child "Le Tuan Kiet" --child-dob "2016-11-05" --gender MALE --origin "Gia dinh tai Phuong Hang Bai" --rel STEP_PARENT

# Hague Intercountry Adoption Dossier
mekong adoption intercountry --app-id "ADP-12345678" --country "France" --central-authority "Mission de l'Adoption Internationale (MAI)" --agency "Agence Francaise de l'Adoption" --home-study "2025-01-10" --dept-approval "QD-55/CCN-BTP" --provincial-decision "QD-120/UBND-TP" --hague

# Post-Placement 6-Month Welfare Report
mekong adoption report --app-id "ADP-12345678" --period 6 --health "Excellent physical health, weight 18kg" --edu "Enrolled in kindergarten, learning French and Vietnamese" --psych "Happy, well-bonded with adoptive parents" --assessor "Marie Dubois" --org "Social Welfare Service Paris" --rating EXCELLENT

# Issue Official Adoption Certificate
mekong adoption certificate --app-id "ADP-12345678" --new-name "Tran Bao An Dubois" --authority "UBND Quan Hoan Kiem, Ha Noi"

# Judicial Termination of Adoption
mekong adoption terminate --app-id "ADP-12345678" --judgment "BA-12/2026/HN-ST" --court "TAND Quan Hoan Kiem" --grounds "Violations of child rights under Art 25" --custody "Returned to biological mother"

# Query Records
mekong adoption list --category application --limit 20
mekong adoption list --category report --json
```

---

## Native MCP Tools

- `mekong_adoption_apply`: Register and validate child adoption application under Law 52/2010.
- `mekong_adoption_intercountry`: Process 1993 Hague Convention intercountry dossier.
- `mekong_adoption_report`: Submit post-placement 6-month welfare and adaptation report.
- `mekong_adoption_certificate`: Issue official Adoption Certificate with digital signature token.
- `mekong_adoption_terminate`: Record judicial termination of adoption relationship.
- `mekong_adoption_list`: Query adoption records by category.
- `mekong_adoption_status`: Return aggregate child adoption telemetry and metrics.
