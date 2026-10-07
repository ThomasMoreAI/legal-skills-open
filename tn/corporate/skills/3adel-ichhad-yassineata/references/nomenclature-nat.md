# NAT — Nomenclature des Activités Tunisiennes (for the RNE form)

## What this is and why you need it

When you file your SUARL / SARL / patente at the RNE, the registration form asks for an **activity code** (code activité principal + secondaires). That code comes from the **NAT — Nomenclature des Activités Tunisiennes**, maintained by the **Institut National de la Statistique (INS)**. NAT is aligned with the European **NACE Rev. 2** standard.

**If you leave that field blank, or if you put a label the clerk does not recognise, the dossier is returned.** This is one of the most common silent rejection reasons for tech founders — because we say things like "AI startup", "agentic software", "SaaS", and the clerk needs `62.01` or `58.29`.

> ⚠️ [REQUIRES MANUAL LEGAL VERIFICATION] The codes below are derived from NACE Rev. 2 (the EU standard NAT is built on). The live INS Nomenclature des Activités Tunisiennes (2026 version) may include minor local re-codings or additional sub-classes. **Cross-check with the current INS PDF before final RNE filing.** The codes here are correct at the section level (62, 63, 70, etc.) and at the divisional level (62.01, 62.02, etc.); the risk is mainly in 4-digit / 5-digit sub-classes that this file does not enumerate.

The structured version of this table is in `data/nat_codes.json` and the recommended combinations for tech profiles are at the end of this file.

---

## Tech-relevant codes — the short list

| Code | Label (FR) | What it covers | Typical fit |
|---|---|---|---|
| **62.01** | Programmation informatique | Custom software development, web/mobile app dev, API/backend dev, DevOps as a deliverable | Primary code for most devs and dev studios |
| **62.02** | Conseil informatique | Software architecture consulting, code audit, cloud migration advisory, AI strategy (advisory only) | Pair with 62.01 if you both build and advise |
| **62.03** | Gestion d'installations informatiques | Managed IT services, running a client's infrastructure on retainer | Only if you actually run client infra |
| **62.09** | Autres activités informatiques | LLM integration on top of existing systems, n8n / Make / Zapier automation work, IT services that do not fit 62.01–62.03 | **Critical for "AI Automation Agency" positioning** |
| **63.11** | Traitement de données, hébergement et activités connexes | Hosting client workloads, SaaS infra operation, data pipelines as a service, vector DB hosting | Add only if you actually host/operate something |
| **63.12** | Portails Internet | Running a marketplace or news portal | Use only if you run a portal product |
| **63.99** | Autres services d'information n.c.a. | Data labeling, specialised research-as-a-service | Niche |
| **58.21** | Édition de jeux électroniques | Indie game studios publishing on Steam / App Store / itch.io | Default for a game studio SUARL |
| **58.29** | Édition d'autres logiciels | Selling your own SaaS, desktop app, or mobile app under your own brand | **Use this instead of 62.01 when you publish your own product** |
| **70.22** | Conseil pour les affaires et autres conseils de gestion | Business-process automation consulting, digital transformation strategy, AI for ops consulting | Pair with 62.09 for automation work |
| **74.10** | Activités spécialisées de design | UI/UX, product design, brand design | Default for designers |
| **74.90** | Autres activités spécialisées, scientifiques et techniques n.c.a. | Translation services, project management consulting | Catch-all |
| **85.59** | Enseignements divers | Coding bootcamps, paid tech workshops, online courses sold under a TN entity | Use if training is a real revenue line |
| **47.91** | Vente à distance | E-commerce sale of physical goods | Triggers customs implications (see `diwana.md`) |
| **73.11** | Activités des agences de publicité | Full-service ad / performance-marketing agency | Only if marketing is the actual business |

---

## Recommended code combinations for tech profiles

The whole point: pick **2–3 codes**, not one. A solo dev who also advises clients needs 62.01 **and** 62.02. An AI automation agency needs 62.01, 62.09, and 70.22. Don't try to fit your whole story into a single code.

### Solo freelance dev (services to foreign clients)
**Codes:** `62.01` + `62.02`
**Object clause (FR):**
> *« Programmation informatique (NAT 62.01), conseil en systèmes informatiques (NAT 62.02), et toutes prestations connexes. »*

### AI Automation Agency
**Codes:** `62.01` + `62.09` + `70.22`
**Object clause (FR):**
> *« Programmation informatique (NAT 62.01), autres activités informatiques incluant l'intégration de systèmes d'intelligence artificielle et l'automatisation des processus métier (NAT 62.09), conseil en gestion et en organisation (NAT 70.22). »*

### SaaS / product studio
**Codes:** `58.29` + `62.01` + `63.11`
**Object clause (FR):**
> *« Édition de logiciels (NAT 58.29), programmation informatique (NAT 62.01), traitement de données et hébergement (NAT 63.11). »*

### Indie game studio
**Codes:** `58.21` + `62.01` + `74.10`
**Object clause (FR):**
> *« Édition de jeux électroniques (NAT 58.21), programmation informatique (NAT 62.01), design (NAT 74.10). »*

### Design / UX freelancer who also codes
**Codes:** `74.10` + `62.01`
**Object clause (FR):**
> *« Activités spécialisées de design (NAT 74.10) et programmation informatique (NAT 62.01). »*

### Training / bootcamp side
**Codes:** `62.02` + `85.59`
**Object clause (FR):**
> *« Conseil informatique (NAT 62.02) et enseignements divers, notamment formations techniques (NAT 85.59). »*

---

## Words to avoid in the object clause

These are real labels you can write in your articles in addition to the NAT code, but they will not pass the RNE clerk **on their own**. NAT code first, marketing label second.

| You may want to write | Combine with NAT code | Note |
|---|---|---|
| "Intelligence artificielle" | 62.01 or 62.09 | OK to use as a sub-label, never as the primary activity |
| "Agentic AI" | 62.09 | Translate it: "intégration et orchestration de systèmes intelligents" |
| "SaaS" | 58.29 | French equivalent: "édition de logiciels en mode service" |
| "Startup" | not a code | Drop it — it has no legal meaning on the RNE form |
| "Web3", "blockchain" | 62.01 + 62.09 | Add: "développement d'applications décentralisées" |
| "DevOps as a service" | 62.01 or 62.03 | If retainer-based → 62.03 |
| "AI Automation Agency" | 62.01 + 62.09 + 70.22 | See combination above |

---

## What the agent must do

This is the hard rule wired into `3adel-ichhad/SKILL.md`:

> The agent **never** outputs a SUARL / SARL object clause without:
> - at least **one** NAT code from this file inserted inline, OR
> - an explicit flag: `[NAT CODE UNRESOLVED — request manual code lookup against the INS Nomenclature des Activités 2026]`.
>
> The agent **never** invents a new code. If the user's activity does not fit any code in this file, the agent says so and asks for human confirmation against the live INS PDF.

---

## Sources

- INS — Institut National de la Statistique (publisher of the official NAT)
- NACE Rev. 2 (EU statistical classification — Tunisia's NAT is aligned to it)
- `data/nat_codes.json` (structured schema)
- `code-societes.md` (Article 3 of the SUARL articles: object clause)
- `rne.md` (Bordereau d'immatriculation: where the code goes on the form)
