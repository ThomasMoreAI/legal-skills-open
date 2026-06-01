---
name: grant-writing
title: Grant Writing — NIH, NSF, and ERC Proposals
description: 'Use this Skill to structure research grant proposals: NSF/NIH Specific Aims, budget justification, ERC narrative sections, structured abstracts, and biosketch formatting.'
author: xjtulyc
author_url: https://github.com/xjtulyc/awesome-rosetta-skills/tree/main/skills/00-universal/grant-writing
license: MIT
version: 0.1.0
execution_mode: open
jurisdiction: general
practice: general
language: en
tags: [universal, grant-writing, nsf, nih, erc, research-funding]
---

# Grant Writing — NIH, NSF, and ERC Proposals

> **TL;DR** — Produce well-structured grant proposal sections using Jinja2
> templates (NIH Specific Aims, ERC B1/B2 narratives), auto-generate budget
> tables with pandas, and format reference lists with pybtex. Covers NIH, NSF,
> and ERC Starting Grant conventions.

---

## When to Use This Skill

Use this Skill whenever you need to:

- Draft or refine a NIH Specific Aims page following the standard one-page format
- Structure an NSF Project Description with explicit intellectual merit and broader impacts
- Outline ERC Starting Grant B1 (extended synopsis) and B2 (scientific proposal) sections
- Generate a personnel budget justification table with fringe, indirect, and total costs
- Format an NIH Biosketch (personal statement, positions, contributions to science)
- Write a 250-word structured abstract with labeled sections for any funding agency
- Format a BibTeX reference list using pybtex for grant submissions

| Task | When to apply |
|---|---|
| Specific Aims page | NIH R01, R21, K-series, SBIR/STTR submissions |
| NSF Project Description | NSF CAREER, standard grants, RAPID, EAGER |
| ERC B1/B2 narrative | ERC StG, CoG, AdG applications |
| Budget justification | Any sponsored research with modular or detailed budget |
| Biosketch | NIH applications; NSF equivalent (Facilities & Other Resources) |
| Structured abstract | Journal submission cover letters, conference abstracts |

---

## Background & Key Concepts

### NIH Specific Aims Page

The Specific Aims page is the single most important page in an NIH application.
Reviewers read it first and it determines whether the full application receives
detailed review. The canonical one-page structure is:

1. **Opening paragraph** — Establishes the research problem, knowledge gap, and
   why the problem matters (~100 words).
2. **Long-term goal** — The overarching scientific objective beyond this grant.
3. **Objective** — What this specific project will accomplish.
4. **Central hypothesis** — A testable, falsifiable statement derived from
   preliminary data.
5. **Specific Aims list** — Typically 2–4 aims, each with a brief rationale and
   expected outcome.
6. **Innovation** — What is new about the approach or the scientific question.
7. **Impact** — Expected contribution to the field and public health relevance.

### NSF Project Description

NSF requires explicit separation of **intellectual merit** (advancing knowledge
within a field) and **broader impacts** (benefits to society). Page limits vary
by program (typically 15 pages for standard grants, 20 for CAREER). Word count
guidance:

| Section | Typical length |
|---|---|
| Introduction & significance | 1–2 pages |
| Preliminary results | 2–3 pages |
| Research plan (each aim) | 2–3 pages per aim |
| Intellectual merit summary | 0.5–1 page |
| Broader impacts | 1–2 pages |
| References cited | Does not count toward page limit |

### ERC Starting Grant B1/B2 Structure

| Section | Description | Page limit |
|---|---|---|
| B1 — Extended synopsis | Short self-contained overview of the project | 5 pages |
| B2 — Scientific proposal | Full research plan: state of the art, methodology, resources | 15 pages |

ERC reviewers assess **scientific excellence** (novelty, ambition, feasibility)
and **principal investigator quality** (track record, independence).

### Budget Categories

A typical NIH R01 modular budget ($250 K/year direct costs) or detailed budget
includes:

| Category | Description |
|---|---|
| Personnel | PI, co-I, postdocs, graduate students, technicians |
| Fringe benefits | As percentage of salary (typically 25–40 %) |
| Equipment | Items ≥ $5 000 with useful life ≥ 1 year |
| Travel | Domestic + international conferences |
| Materials & supplies | Lab consumables, software licenses |
| Other direct costs | Publication fees, patient costs, subcontract |
| Indirect (F&A) | Negotiated rate × modified total direct costs |

### Structured Abstract (250 words)

All NIH applications require a structured abstract with labeled sections:
Background, Objective, Methods, Expected Results, and Significance. The total
must not exceed 250 words.

---

## Environment Setup

```bash
# Create a dedicated virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install required packages
pip install "jinja2>=3.0" "pybtex>=0.24" "pandas>=1.5" "python-dotenv>=1.0"

# Verify installation
python -c "import jinja2, pybtex, pandas; print('Setup OK')"
```

For AI-assisted draft generation, set your API key:

```bash
# export OPENAI_API_KEY="<paste-your-key>"
# export ANTHROPIC_API_KEY="<paste-your-key>"
python -c "import os; print(os.getenv('OPENAI_API_KEY', 'NOT SET'))"
```

---

## Core Workflow

### Step 1 — Render NIH Specific Aims Page with Jinja2

Define your grant content as a Python dictionary and render a structured
Specific Aims page using a Jinja2 template.

```python
import os
from jinja2 import Environment, BaseLoader
from dotenv import load_dotenv

load_dotenv()

SPECIFIC_AIMS_TEMPLATE = """
SPECIFIC AIMS

{{ background }}

Long-term goal: {{ long_term_goal }}

Objective: {{ objective }}

Central hypothesis: {{ central_hypothesis }}

Rationale: {{ rationale }}

SPECIFIC AIMS:
{% for aim in aims %}
Aim {{ loop.index }}: {{ aim.title }}
  {{ aim.description }}
  Expected outcome: {{ aim.expected_outcome }}
{% endfor %}

Innovation: {{ innovation }}

Impact: {{ impact }}
""".strip()


def render_specific_aims(content: dict) -> str:
    """
    Render a NIH Specific Aims page from a structured content dictionary.

    Args:
        content: Dictionary with keys: background, long_term_goal, objective,
                 central_hypothesis, rationale, aims (list of dicts with
                 title/description/expected_outcome), innovation, impact.

    Returns:
        Rendered Specific Aims text as a string.

    Example:
        >>> text = render_specific_aims(EXAMPLE_AIMS_CONTENT)
        >>> print(text[:200])
    """
    env = Environment(loader=BaseLoader())
    template = env.from_string(SPECIFIC_AIMS_TEMPLATE)
    return template.render(**content)


EXAMPLE_AIMS_CONTENT = {
    "background": (
        "Alzheimer's disease (AD) affects 6.7 million Americans and currently "
        "lacks disease-modifying treatments. Neuroinflammation driven by "
        "microglial activation is increasingly recognized as a key pathological "
        "mechanism, yet the molecular switches that convert microglia from "
        "homeostatic to disease-associated states remain poorly understood."
    ),
    "long_term_goal": (
        "Elucidate microglial state transitions in AD to identify novel "
        "therapeutic targets for neuroinflammation."
    ),
    "objective": (
        "Characterize the transcriptional and epigenetic regulators governing "
        "microglial activation in human AD brain tissue and validated mouse models."
    ),
    "central_hypothesis": (
        "TREM2 signaling coordinates with APOE-mediated lipid metabolism to drive "
        "disease-associated microglial (DAM) state transitions, and disrupting "
        "this axis will attenuate amyloid pathology."
    ),
    "rationale": (
        "Preliminary data from our lab demonstrate that TREM2-deficient microglia "
        "fail to upregulate DAM markers in 5xFAD mice, supporting the central "
        "hypothesis. Identifying the upstream regulators will open new therapeutic "
        "windows."
    ),
    "aims": [
        {
            "title": "Define the TREM2-dependent transcriptional network in human AD microglia.",
            "description": (
                "We will perform single-nucleus RNA-seq and ATAC-seq on "
                "post-mortem prefrontal cortex from 40 AD and 20 control donors "
                "stratified by TREM2 genotype."
            ),
            "expected_outcome": (
                "A high-resolution atlas of microglial states linked to TREM2 "
                "variant status and amyloid burden."
            ),
        },
        {
            "title": "Determine how APOE isoforms modulate TREM2-driven microglial lipid metabolism.",
            "description": (
                "Using APOE knock-in mice crossed with 5xFAD, we will apply "
                "lipidomics and CRISPR-interference screens to identify lipid "
                "mediators downstream of TREM2 signaling."
            ),
            "expected_outcome": (
                "Identification of 3–5 lipid species that serve as rheostat "
                "switches for DAM induction."
            ),
        },
        {
            "title": "Test whether pharmacological modulation of the TREM2-APOE axis reduces AD pathology.",
            "description": (
                "Lead compounds identified in Aim 2 will be administered to "
                "5xFAD mice; amyloid plaque load, synaptic density, and "
                "cognitive performance will be quantified."
            ),
            "expected_outcome": (
                "At least one compound that reduces plaque burden by ≥30 % and "
                "rescues novel-object recognition deficits."
            ),
        },
    ],
    "innovation": (
        "This project is innovative because it integrates multi-omic single-cell "
        "profiling with functional CRISPR screens in a genotype-stratified human "
        "cohort — a combination not previously applied to TREM2-APOE interactions."
    ),
    "impact": (
        "Success will produce a mechanistic framework for microglial reprogramming "
        "in AD and candidate therapeutic targets ready for preclinical IND-enabling "
        "studies, directly advancing NIH's goal of developing disease-modifying "
        "AD therapies."
    ),
}


if __name__ == "__main__":
    text = render_specific_aims(EXAMPLE_AIMS_CONTENT)
    output_path = "specific_aims.txt"
    with open(output_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"Specific Aims page written to {output_path}")
    print(f"Character count: {len(text)} (target ≤ 3500 for one page)")
```

### Step 2 — Generate Budget Justification Table with pandas

```python
import pandas as pd
import numpy as np


def build_budget_table(
    personnel: list[dict],
    equipment: list[dict] | None = None,
    travel_domestic: float = 2000.0,
    travel_international: float = 3000.0,
    materials: float = 15000.0,
    other_direct: float = 5000.0,
    indirect_rate: float = 0.52,
    years: int = 4,
) -> pd.DataFrame:
    """
    Build a multi-year NIH detailed budget justification table.

    Args:
        personnel:            List of dicts with keys: role, name, effort_pct,
                              annual_salary, fringe_rate.
        equipment:            List of dicts with keys: item, cost, year (1-indexed).
        travel_domestic:      Annual domestic travel per year (USD).
        travel_international: Annual international travel per year (USD).
        materials:            Annual materials & supplies (USD).
        other_direct:         Annual other direct costs (USD).
        indirect_rate:        Facilities & administrative rate (fraction, e.g. 0.52).
        years:                Project duration in years.

    Returns:
        DataFrame with one row per line item per year plus totals row.
    """
    rows = []

    for yr in range(1, years + 1):
        # Personnel + fringe
        for p in personnel:
            salary_cost = p["annual_salary"] * p["effort_pct"] / 100
            # Apply 3 % annual escalation from year 2 onward
            salary_cost *= (1.03 ** (yr - 1))
            fringe_cost = salary_cost * p["fringe_rate"]
            rows.append({
                "year": yr,
                "category": "Personnel",
                "line_item": f"{p['role']} — {p['name']}",
                "direct_cost": round(salary_cost, 2),
                "notes": f"{p['effort_pct']}% effort; fringe ${fringe_cost:,.0f}",
            })

        # Equipment (year-specific)
        if equipment:
            for eq in equipment:
                if eq["year"] == yr:
                    rows.append({
                        "year": yr,
                        "category": "Equipment",
                        "line_item": eq["item"],
                        "direct_cost": eq["cost"],
                        "notes": "One-time purchase ≥ $5,000",
                    })

        # Travel
        rows.append({
            "year": yr,
            "category": "Travel",
            "line_item": "Domestic conference travel",
            "direct_cost": travel_domestic,
            "notes": "1 PI + 1 trainee × 1 conference",
        })
        rows.append({
            "year": yr,
            "category": "Travel",
            "line_item": "International conference travel",
            "direct_cost": travel_international,
            "notes": "1 PI × 1 international meeting",
        })

        # Materials
        rows.append({
            "year": yr,
            "category": "Materials & Supplies",
            "line_item": "Lab consumables & reagents",
            "direct_cost": materials,
            "notes": "Antibodies, cell culture, sequencing reagents",
        })

        # Other direct
        rows.append({
            "year": yr,
            "category": "Other Direct Costs",
            "line_item": "Publication fees & software",
            "direct_cost": other_direct,
            "notes": "Open-access fees, statistical software licenses",
        })

    df = pd.DataFrame(rows)

    # Compute indirect costs per year
    indirect_rows = []
    for yr, grp in df.groupby("year"):
        mtdc = grp["direct_cost"].sum()
        indirect = round(mtdc * indirect_rate, 2)
        indirect_rows.append({
            "year": yr,
            "category": "Indirect (F&A)",
            "line_item": f"Indirect costs @ {indirect_rate*100:.0f}% MTDC",
            "direct_cost": indirect,
            "notes": f"Applied to MTDC of ${mtdc:,.0f}",
        })
    df = pd.concat([df, pd.DataFrame(indirect_rows)], ignore_index=True)

    # Grand totals row
    total_cost = df["direct_cost"].sum()
    total_row = pd.DataFrame([{
        "year": "ALL",
        "category": "TOTAL",
        "line_item": "Total Project Cost",
        "direct_cost": round(total_cost, 2),
        "notes": "",
    }])
    df = pd.concat([df, total_row], ignore_index=True)
    return df


SAMPLE_PERSONNEL = [
    {"role": "Principal Investigator", "name": "Dr. J. Smith",
     "effort_pct": 20, "annual_salary": 120000, "fringe_rate": 0.30},
    {"role": "Postdoctoral Researcher", "name": "Dr. A. Lee",
     "effort_pct": 100, "annual_salary": 58000, "fringe_rate": 0.28},
    {"role": "Graduate Research Assistant", "name": "M. Chen",
     "effort_pct": 50, "annual_salary": 32000, "fringe_rate": 0.10},
]

SAMPLE_EQUIPMENT = [
    {"item": "High-content fluorescence microscope", "cost": 85000, "year": 1},
    {"item": "Ultra-low temperature freezer (-80 °C)", "cost": 12000, "year": 2},
]

if __name__ == "__main__":
    budget_df = build_budget_table(
        personnel=SAMPLE_PERSONNEL,
        equipment=SAMPLE_EQUIPMENT,
        travel_domestic=2500,
        travel_international=3500,
        materials=18000,
        other_direct=6000,
        indirect_rate=0.52,
        years=4,
    )
    budget_df.to_csv("budget_justification.csv", index=False)
    print(budget_df.to_string(index=False))

    # Summary by year
    yearly = budget_df[budget_df["year"] != "ALL"].copy()
    yearly["direct_cost"] = pd.to_numeric(yearly["direct_cost"])
    print("\nAnnual totals:")
    print(yearly.groupby("year")["direct_cost"].sum().apply(lambda x: f"${x:,.0f}"))
```

### Step 3 — Format References with pybtex and Write Structured Abstract

```python
import textwrap
from pybtex.database import BibliographyData, Entry, Person
from pybtex.database.output.bibtex import Writer as BibTexWriter
import io


def create_bibtex_entry(
    key: str,
    authors: list[str],
    title: str,
    journal: str,
    year: int,
    volume: str = "",
    pages: str = "",
    doi: str = "",
) -> Entry:
    """
    Create a pybtex BibTeX Entry object for a journal article.

    Args:
        key:     BibTeX citation key (e.g., 'Smith2024').
        authors: List of author names in 'Last, First' format.
        title:   Article title.
        journal: Journal name.
        year:    Publication year.
        volume:  Journal volume number.
        pages:   Page range (e.g., '123-145').
        doi:     Digital object identifier.

    Returns:
        pybtex Entry object of type 'article'.
    """
    persons = {"author": [Person(a) for a in authors]}
    fields = {
        "title": title,
        "journal": journal,
        "year": str(year),
    }
    if volume:
        fields["volume"] = volume
    if pages:
        fields["pages"] = pages
    if doi:
        fields["doi"] = doi

    return Entry("article", persons=persons, fields=fields)


def render_bibliography(entries: dict[str, Entry]) -> str:
    """Render a set of pybtex entries as a BibTeX string."""
    bib_data = BibliographyData(entries=entries)
    writer = BibTexWriter()
    stream = io.StringIO()
    writer.write_stream(bib_data, stream)
    return stream.getvalue()


def write_structured_abstract(
    background: str,
    objective: str,
    methods: str,
    expected_results: str,
    significance: str,
    word_limit: int = 250,
) -> str:
    """
    Compose and validate a structured 250-word abstract.

    Args:
        background:       1–2 sentences on the problem and knowledge gap.
        objective:        1 sentence stating the study objective.
        methods:          2–3 sentences describing design, participants, measures.
        expected_results: 2–3 sentences on anticipated findings.
        significance:     1–2 sentences on importance and next steps.
        word_limit:       Maximum word count (default 250 for NIH).

    Returns:
        Formatted abstract string with word count report.
    """
    sections = [
        ("Background", background),
        ("Objective", objective),
        ("Methods", methods),
        ("Expected Results", expected_results),
        ("Significance", significance),
    ]
    lines = []
    for label, text in sections:
        wrapped = textwrap.fill(f"{label}: {text}", width=80)
        lines.append(wrapped)

    abstract = "\n\n".join(lines)
    word_count = len(abstract.split())

    status = "OK" if word_count <= word_limit else f"OVER LIMIT by {word_count - word_limit} words"
    footer = f"\n\n[Word count: {word_count}/{word_limit} — {status}]"
    return abstract + footer


# ── Usage ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Bibliography
    entries = {
        "Smith2023": create_bibtex_entry(
            key="Smith2023",
            authors=["Smith, Jane", "Lee, Andrew"],
            title="TREM2 variants and microglial activation in Alzheimer disease",
            journal="Nature Neuroscience",
            year=2023,
            volume="26",
            pages="1234-1245",
            doi="10.1038/s41593-023-XXXX-X",
        ),
        "Jones2022": create_bibtex_entry(
            key="Jones2022",
            authors=["Jones, Robert", "Patel, Sunita", "Kim, David"],
            title="APOE4 modulates lipid metabolism in disease-associated microglia",
            journal="Cell",
            year=2022,
            volume="185",
            pages="3456-3471",
            doi="10.1016/j.cell.2022.XX.XXX",
        ),
    }
    bib_str = render_bibliography(entries)
    with open("references.bib", "w", encoding="utf-8") as fh:
        fh.write(bib_str)
    print("BibTeX references written to references.bib")

    # Structured abstract
    abstract = write_structured_abstract(
        background=(
            "Alzheimer's disease (AD) lacks disease-modifying treatments; "
            "microglial neuroinflammation is a mechanistically plausible target "
            "but the upstream regulators of microglial state transitions remain "
            "unknown."
        ),
        objective=(
            "To identify TREM2- and APOE-dependent transcriptional regulators "
            "of disease-associated microglia (DAM) in human AD brain tissue."
        ),
        methods=(
            "We will perform single-nucleus RNA-seq and ATAC-seq on 60 "
            "post-mortem prefrontal cortex samples stratified by TREM2 genotype "
            "and AD status. Hits will be validated in APOE knock-in/5xFAD mice "
            "using CRISPR-interference screens and lipidomics."
        ),
        expected_results=(
            "We expect to identify 3–5 transcription factors that gate DAM "
            "induction in a TREM2-dependent manner and lipid mediators that "
            "link APOE isoforms to TREM2 signaling. At least one compound will "
            "reduce plaque burden by ≥30 % in vivo."
        ),
        significance=(
            "These findings will establish a mechanistic basis for targeting "
            "the TREM2-APOE axis in AD and will nominate preclinical candidates "
            "for IND-enabling studies, accelerating the pipeline of "
            "neuroinflammation-targeted AD therapies."
        ),
    )
    print(abstract)
```

---

## Advanced Usage

### NIH Biosketch Formatting

The NIH Biosketch (Form PHS 2590 / SciENcv format) contains four sections:

1. **Personal Statement** — 4 sentences maximum. State why you are well-suited
   for this project. Reference up to 4 publications.
2. **Positions, Scientific Appointments, and Honors** — Reverse-chronological
   list with institution, role, and dates.
3. **Contributions to Science** — Up to 5 paragraphs, each with a brief
   narrative and up to 4 publications. Describe the historical context, your
   contribution, and significance.
4. **Additional Information** — Research support (current and pending).

```python
BIOSKETCH_TEMPLATE = """
BIOGRAPHICAL SKETCH

NAME: {{ name }}
eRA COMMONS USER NAME: {{ era_commons }}
POSITION TITLE: {{ position_title }}
EDUCATION/TRAINING:
{% for edu in education %}
  {{ edu.institution }} | {{ edu.degree }} | {{ edu.field }} | {{ edu.year }}
{% endfor %}

A. Personal Statement
{{ personal_statement }}
Key publications:
{% for pub in personal_pubs %}
  {{ loop.index }}. {{ pub }}
{% endfor %}

B. Positions, Scientific Appointments, and Honors
{% for pos in positions %}
  {{ pos.dates }}: {{ pos.role }}, {{ pos.institution }}
{% endfor %}

C. Contributions to Science
{% for contrib in contributions %}
{{ loop.index }}. {{ contrib.narrative }}
   Publications:
{% for pub in contrib.publications %}
   {{ loop.index }}. {{ pub }}
{% endfor %}
{% endfor %}
""".strip()


def render_biosketch(data: dict) -> str:
    """Render NIH Biosketch from structured dictionary using Jinja2."""
    from jinja2 import Environment, BaseLoader
    env = Environment(loader=BaseLoader())
    template = env.from_string(BIOSKETCH_TEMPLATE)
    return template.render(**data)
```

### ERC Starting Grant B1 / B2 Outline

ERC proposals require explicit evidence of **scientific excellence** and
**PI independence**. Structure B1 (5 pages) as follows:

| Subsection | Content |
|---|---|
| B1.1 Overview | Project title, keywords, short abstract (10 lines) |
| B1.2 State of the art | Current knowledge and open question |
| B1.3 Objectives | 3–5 numbered objectives aligned with work packages |
| B1.4 Methodology | Key experimental/computational approaches |
| B1.5 Originality | How the proposal goes beyond the state of the art |
| B1.6 Resources | Team composition, key infrastructure |

For B2 (15 pages), expand each subsection and add:
- Work package (WP) table with lead, duration, deliverables, milestones
- Risk assessment table (risk, probability, mitigation)
- Timeline Gantt chart

### NSF Broader Impacts Template

NSF reviewers score broader impacts independently of intellectual merit. Include:

- **STEM workforce development** — graduate/undergraduate mentoring plan
- **Broadening participation** — recruitment strategy for underrepresented groups
- **K-12 outreach** — partnerships with local schools or science museums
- **Open science** — data sharing, software release, preprint posting
- **Dissemination** — target journals, conferences, policy briefs

---

## Troubleshooting

| Problem | Likely cause | Fix |
|---|---|---|
| Jinja2 `UndefinedError` | Missing key in content dictionary | Add all required keys; use `default('')` filter in template |
| Budget rows duplicated | `years` parameter too high | Verify `years` matches Notice of Award period |
| pybtex `PybtexError` | Malformed author string | Use "Last, First" format; escape special characters |
| Abstract word count over limit | Run-on sentences | Use `write_structured_abstract()` validator; trim each section |
| BibTeX missing fields | Incomplete entry dict | Check required fields: author, title, journal, year |
| Indirect rate mismatch | Stale F&A agreement | Retrieve current negotiated rate from institutional grants office |

---

## External Resources

- NIH Specific Aims guidance: <https://grants.nih.gov/grants/how-to-apply-application-guide/format-and-write/write-your-application.htm>
- NSF Proposal & Award Policies: <https://www.nsf.gov/pubs/policydocs/pappg25_1/index.jsp>
- ERC Work Programme: <https://erc.europa.eu/funding/starting-grants>
- NIH Biosketch instructions: <https://grants.nih.gov/grants/forms/biosketch.htm>
- SciENcv biosketch builder: <https://www.ncbi.nlm.nih.gov/sciencv/>
- pybtex documentation: <https://docs.pybtex.org/>
- Jinja2 template designer docs: <https://jinja.palletsprojects.com/en/3.1.x/templates/>

---

## Examples

### Example 1 — Full NIH Specific Aims Page Rendered via Jinja2

```python
# Run from the project root; requires jinja2 and python-dotenv installed
import os
from dotenv import load_dotenv
load_dotenv()

# Re-use functions defined in Step 1
text = render_specific_aims(EXAMPLE_AIMS_CONTENT)
word_count = len(text.split())
char_count = len(text)

print(f"=== NIH Specific Aims Page ({'~' + str(word_count)} words) ===\n")
print(text)
print(f"\n[Characters: {char_count} | Target: ≤ 3500 for one page at 11pt Arial]")

# Save to file for review
with open("specific_aims_final.txt", "w", encoding="utf-8") as fh:
    fh.write(text)
print("\nSaved to specific_aims_final.txt")
```

### Example 2 — NSF Budget Table and Broader Impacts Template

```python
import pandas as pd

# --- Budget Table for NSF CAREER (5 years) ---
nsf_personnel = [
    {"role": "Principal Investigator", "name": "Dr. M. Rivera",
     "effort_pct": 25, "annual_salary": 110000, "fringe_rate": 0.32},
    {"role": "Graduate Research Assistant (0.5 FTE)", "name": "TBD",
     "effort_pct": 50, "annual_salary": 34000, "fringe_rate": 0.08},
    {"role": "Undergraduate Researcher (summer)", "name": "TBD",
     "effort_pct": 100, "annual_salary": 10000, "fringe_rate": 0.08},
]
nsf_equipment = [
    {"item": "Confocal laser scanning microscope (shared)", "cost": 45000, "year": 1},
]

nsf_budget = build_budget_table(
    personnel=nsf_personnel,
    equipment=nsf_equipment,
    travel_domestic=3000,
    travel_international=4000,
    materials=12000,
    other_direct=4000,
    indirect_rate=0.56,
    years=5,
)
nsf_budget.to_csv("nsf_career_budget.csv", index=False)

# Year 1 direct cost summary
yr1 = nsf_budget[
    (nsf_budget["year"] == 1) & (nsf_budget["category"] != "Indirect (F&A)")
]
yr1_direct = pd.to_numeric(yr1["direct_cost"]).sum()
print(f"NSF CAREER Year 1 direct costs: ${yr1_direct:,.0f}")

# --- Broader Impacts template ---
BROADER_IMPACTS = """
BROADER IMPACTS

Intellectual Merit: [Summarize contribution to fundamental knowledge]

Broader Impacts:
1. Graduate and postdoctoral training: One PhD student and one postdoc will
   receive training in [field], preparing them for careers in academia and
   industry. Mentoring will follow the Individual Development Plan (IDP)
   framework.

2. Broadening participation: We will partner with [HBCU/MSI partner] to
   host two REU undergraduates per summer from underrepresented groups.
   Travel support will be provided.

3. K-12 outreach: We will develop two inquiry-based modules for local high
   schools in partnership with [School District], reaching ~200 students
   per year.

4. Open science: All datasets will be deposited in [repository] under CC-BY
   license within 12 months of collection. Analysis code will be released on
   GitHub under MIT license.

5. Policy engagement: Findings will be communicated to [agency] via annual
   stakeholder briefings and one policy brief per project year.
"""
print(BROADER_IMPACTS)
with open("nsf_broader_impacts.txt", "w", encoding="utf-8") as fh:
    fh.write(BROADER_IMPACTS)
print("Broader impacts template saved to nsf_broader_impacts.txt")
```

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0.0 | 2026-03-18 | Initial release — Jinja2 Specific Aims, pandas budget table, pybtex references, structured abstract, biosketch template |
