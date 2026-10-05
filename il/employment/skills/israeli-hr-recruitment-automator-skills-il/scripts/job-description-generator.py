#!/usr/bin/env python3
"""
Israeli Job Description Generator

Draft Hebrew job descriptions and check them against the published
requirements of the Equal Employment Opportunities Law 1988. Flags wording
that matches known discriminatory patterns and outputs formatted markdown.
A clean run is NOT a compliance result.

Usage:
    python job-description-generator.py --title "מפתח/ת Full-Stack" --company "TechCo" --location "תל אביב"
    python job-description-generator.py --validate --input job_description.txt
    python job-description-generator.py --template tech --title "מפתח/ת תוכנה" --company "TechCo" --location "תל אביב"
    python job-description-generator.py --template-list
"""

import argparse
import re
import sys
from typing import Optional


# Anti-discrimination terms that should not appear in job descriptions
DISCRIMINATORY_PATTERNS = [
    # Gender-specific (non-inclusive)
    (r'\bדרוש\b(?!\s*/\s*ה)', 'gender_specific', 'Use "דרוש/ה" or inclusive language'),
    (r'\bמפתח\b(?!\s*/\s*ת)', 'gender_specific', 'Use "מפתח/ת" or inclusive language'),
    (r'\bמנהל\b(?!\s*/\s*ת)', 'gender_specific', 'Use "מנהל/ת" or inclusive language'),
    (r'\bמהנדס\b(?!\s*/\s*ת)', 'gender_specific', 'Use "מהנדס/ת" or inclusive language'),
    # Age restrictions
    (r'\bגילאי\s+\d+', 'age_restriction', 'Remove age range requirements'),
    (r'\bבני?\s+\d+\s*-\s*\d+', 'age_restriction', 'Remove age range requirements'),
    (r'\bצעירים\b', 'age_proxy', '"Young" can be an age proxy; remove or rephrase'),
    (r'\bבוגרים\s+טריים\b', 'age_proxy', '"Fresh graduates" can be age proxy; use "recent graduates" instead'),
    # Marital status
    (r'\bרווק', 'marital_status', 'Remove marital status references'),
    (r'\bנשוי', 'marital_status', 'Remove marital status references'),
    (r'\bגרוש', 'marital_status', 'Remove marital status references'),
    # Pregnancy
    (r'\bהריון\b', 'pregnancy', 'Remove pregnancy references'),
    (r'\bבהריון\b', 'pregnancy', 'Remove pregnancy references'),
    # Military unit requirements
    (r'\bיחידת\s+\d+', 'military_unit', 'Do not require specific military units'),
    (r'\b8200\b', 'military_unit', 'Do not require specific military units'),
    (r'\bממר"ם\b', 'military_unit', 'Do not require specific military units as criteria'),
    (r'\bבוגר.?\s+(קרבי|מודיעין)', 'military_unit', 'Do not require specific service types'),
    # Ethnicity/religion
    (r'\bיהודים?\s+בלבד\b', 'ethnicity', 'Remove ethnicity/religion restrictions'),
    (r'\bערבים?\s+בלבד\b', 'ethnicity', 'Remove ethnicity/religion restrictions'),
    (r'\bדתיים?\s+בלבד\b', 'religion', 'Remove religion restrictions'),
    (r'\bשומר.?\s+שבת\b', 'religion', 'Remove religious observance requirements unless GOQ'),
    # Place of residence: an enumerated section 2(a) ground and the one Israeli
    # job ads breach most routinely. No leading \b, Hebrew prefixes glue on.
    (r'(תושבי|תושב)\s+(המרכז|הצפון|הדרום|האזור)\s*(בלבד)?', 'place_of_residence', 'Place of residence is a protected ground under section 2(a); remove the restriction'),
    (r'מגורים\s+(באזור|בקרבת|קרוב)', 'place_of_residence', 'Cannot require the candidate to live in a particular area'),
    (r'(חובה|נדרשת|נדרש)\s+מגורים', 'place_of_residence', 'Cannot require residence in a particular place'),
    # Appearance: NOT a section 2(a) ground (the word מראה does not appear in the
    # law). Still flagged as bad practice and as a likely proxy for an enumerated
    # ground, but the message must not cite section 2(a).

    (r'\bמראה\s+(נאה|טוב|מרשים)', 'appearance_bad_practice', 'Appearance is not an enumerated section 2(a) ground, but it is a likely proxy for one; remove the requirement'),
    (r'\bגובה\s+מינימל', 'appearance_bad_practice', 'Not a section 2(a) ground; remove height requirements unless a genuine occupational qualification'),
    # Reserve duty
    (r'\bללא\s+מילואים\b', 'reserve_duty', 'Cannot exclude candidates with reserve duty'),
    (r'\bפטור\s+ממילואים\b', 'reserve_duty', 'Cannot require reserve duty exemption'),
    # No leading \b on these: a Hebrew conjunctive/prepositional prefix (ו, ש, ל)
    # glues onto the next word, so "ואין מילואים" has no boundary before "אין"
    # and a \b-anchored pattern silently misses the most common phrasing.
    (r'(אין|ללא)\s+(חובות|חובת|ימי)?\s*מילואים', 'reserve_duty', 'Cannot exclude candidates with reserve duty obligations'),
    (r'לא\s+(משרת|משרתת|משרתים)\s+במילואים', 'reserve_duty', 'Cannot require that a candidate does not serve reserve duty'),
    (r'(שירות|רקע)\s+קרבי\s+(חובה|נדרש|בלבד)', 'military_unit', 'Cannot require a specific type of military service'),
]

# Job templates by type
TEMPLATES = {
    'tech': {
        'title': 'מפתח/ת תוכנה',
        'requirements': [
            'ניסיון של [X] שנים בפיתוח תוכנה',
            'שליטה ב-[שפות תכנות]',
            'ניסיון עם [frameworks/technologies]',
            'יכולת עבודה בצוות ותקשורת טובה',
            'אנגלית ברמה גבוהה (קריאה וכתיבה טכנית)',
        ],
        'nice_to_have': [
            'ניסיון עם [טכנולוגיה ספציפית]',
            'תואר ראשון במדעי המחשב או תחום רלוונטי',
            'ניסיון בעבודה בסביבת סטארטאפ',
        ],
        'benefits': [
            'שכר תחרותי + אופציות',
            'קרן השתלמות (7.5% מעסיק + 2.5% עובד)',
            'ביטוח בריאות פרטי',
            'ארוחות במשרד',
            'גמישות בשעות העבודה ואפשרות עבודה היברידית',
            'תקציב למידה והשתלמויות',
        ],
    },
    'product': {
        'title': 'מנהל/ת מוצר',
        'requirements': [
            'ניסיון של [X] שנים בניהול מוצר',
            'יכולת ניתוח נתונים ועבודה עם מדדי מוצר',
            'ניסיון בעבודה עם צוותי פיתוח',
            'יכולת הובלת תהליכים מקצה לקצה',
            'אנגלית ברמת שפת אם',
        ],
        'nice_to_have': [
            'ניסיון במוצרי B2B/B2C',
            'רקע טכנולוגי',
            'ניסיון עם כלי BI ואנליטיקה',
        ],
        'benefits': [
            'שכר תחרותי + בונוס שנתי',
            'קרן השתלמות',
            'ביטוח בריאות פרטי',
            'ימי חופשה מעל המינימום החוקי',
        ],
    },
    'marketing': {
        'title': 'מנהל/ת שיווק דיגיטלי',
        'requirements': [
            'ניסיון של [X] שנים בשיווק דיגיטלי',
            'שליטה בכלי פרסום (Google Ads, Facebook Ads, LinkedIn)',
            'ניסיון בניהול תקציב שיווקי',
            'יכולת כתיבה שיווקית בעברית ובאנגלית',
            'יכולת ניתוח נתונים (Google Analytics, מערכות BI)',
        ],
        'nice_to_have': [
            'ניסיון בשיווק B2B',
            'ידע ב-SEO/SEM',
            'ניסיון עם כלי אוטומציה שיווקית',
        ],
        'benefits': [
            'שכר תחרותי',
            'קרן השתלמות',
            'אפשרות לעבודה היברידית',
            'תקציב השתלמויות וכנסים',
        ],
    },
}


def validate_job_description(text: str) -> list[dict]:
    """Validate a job description against anti-discrimination rules.

    Returns a list of violation dicts with keys: line, category, match, suggestion.
    """
    violations = []
    lines = text.split('\n')

    for line_num, line in enumerate(lines, 1):
        for pattern, category, suggestion in DISCRIMINATORY_PATTERNS:
            matches = re.finditer(pattern, line)
            for match in matches:
                violations.append({
                    'line': line_num,
                    'category': category,
                    'match': match.group(),
                    'suggestion': suggestion,
                    'context': line.strip(),
                })

    return violations


def generate_job_description(
    title: str,
    company: str,
    location: str,
    job_type: str = 'משרה מלאה',
    field: str = '',
    description: str = '',
    requirements: Optional[list[str]] = None,
    nice_to_have: Optional[list[str]] = None,
    benefits: Optional[list[str]] = None,
    template_type: Optional[str] = None,
) -> str:
    """Draft a Hebrew job description from structured input."""

    # Use template if specified
    if template_type and template_type in TEMPLATES:
        tmpl = TEMPLATES[template_type]
        if not requirements:
            requirements = tmpl['requirements']
        if not nice_to_have:
            nice_to_have = tmpl['nice_to_have']
        if not benefits:
            benefits = tmpl['benefits']
        if title == 'מפתח/ת תוכנה' or not title:
            title = tmpl['title']

    requirements = requirements or ['[דרישה 1]', '[דרישה 2]']
    nice_to_have = nice_to_have or ['[יתרון 1]']
    benefits = benefits or ['[הטבה 1]', '[הטבה 2]']

    if not description:
        description = (
            f'[תיאור התפקיד ב-2-3 פסקאות. תארו את הצוות, האתגרים והחברה. '
            f'הימנעו משפה מגדרית או אפליה על בסיס כל מאפיין מוגן.]'
        )

    req_lines = '\n'.join(f'- {r}' for r in requirements)
    nth_lines = '\n'.join(f'- {n}' for n in nice_to_have)
    ben_lines = '\n'.join(f'- {b}' for b in benefits)

    output = f"""# {title}

**חברה:** {company}
**מיקום:** {location}
**סוג משרה:** {job_type}
**תחום:** {field or '[תחום]'}

---

## תיאור התפקיד

{description}

## דרישות התפקיד

{req_lines}

## דרישות רצויות (יתרון)

{nth_lines}

## מה אנחנו מציעים

{ben_lines}

---

**להגשת מועמדות:** שלחו קורות חיים ל-[email] עם הנושא "{title} - {company}"

*חברת {company} מחויבת לשוויון הזדמנויות בעבודה ומעודדת הגשת מועמדויות מכל המגדרים, הגילאים והרקעים.*
"""

    return output


def print_validation_report(violations: list[dict]) -> None:
    """Print a formatted validation report."""
    if not violations:
        print('No matches for the patterns this script checks. This is NOT a compliance result: section 8 and most section 2(a) grounds are not machine-checkable.')
        print()
        print('Note: This automated check covers common patterns but is not')
        print('exhaustive. Manual review is still recommended for compliance')
        print('with the Equal Employment Opportunities Law 1988.')
        return

    print(f'FAIL: Found {len(violations)} potential violation(s):')
    print()

    categories = {}
    for v in violations:
        cat = v['category']
        if cat not in categories:
            categories[cat] = []
        categories[cat].append(v)

    for category, items in categories.items():
        cat_label = category.replace('_', ' ').title()
        print(f'  [{cat_label}]')
        for item in items:
            print(f'    Line {item["line"]}: "{item["match"]}"')
            print(f'    Context: {item["context"]}')
            print(f'    Suggestion: {item["suggestion"]}')
            print()


def main():
    parser = argparse.ArgumentParser(
        description='Draft and check Israeli job descriptions against the published '
                    'requirements of the Equal Employment Opportunities Law 1988. '
                    'A clean run is not a compliance result.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Generate a tech job description:
    %(prog)s --title "מפתח/ת Full-Stack" --company "TechCo" --location "תל אביב" --template tech

  Validate an existing job description:
    %(prog)s --validate --input job_description.txt

  Show available templates:
    %(prog)s --template-list

  Generate with custom requirements:
    %(prog)s --title "מנהל/ת מוצר" --company "StartupX" --location "הרצליה" \\
      --requirement "3+ שנות ניסיון בניהול מוצר" \\
      --requirement "ניסיון בעבודה עם צוותי פיתוח"
        """,
    )

    # Mode selection
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        '--validate',
        action='store_true',
        help='Validate an existing job description for compliance',
    )
    mode_group.add_argument(
        '--template-list',
        action='store_true',
        help='List available job description templates',
    )

    # Generation options
    parser.add_argument('--title', help='Job title in Hebrew (e.g., "מפתח/ת Full-Stack")')
    parser.add_argument('--company', help='Company name')
    parser.add_argument('--location', help='Job location (e.g., "תל אביב")')
    parser.add_argument('--job-type', default='משרה מלאה', help='Job type (default: "משרה מלאה")')
    parser.add_argument('--field', default='', help='Job field/industry')
    parser.add_argument('--template', choices=list(TEMPLATES.keys()), help='Use a predefined template')
    parser.add_argument('--requirement', action='append', dest='requirements', help='Add a requirement (repeatable)')
    parser.add_argument('--nice-to-have', action='append', dest='nice_to_have_list', help='Add a nice-to-have (repeatable)')
    parser.add_argument('--benefit', action='append', dest='benefits', help='Add a benefit (repeatable)')
    parser.add_argument('--description', help='Job description text')

    # Validation options
    parser.add_argument('--input', help='Input file to validate')
    parser.add_argument('--output', help='Output file (default: stdout)')

    args = parser.parse_args()

    # Template list mode
    if args.template_list:
        print('Available templates:')
        for name, tmpl in TEMPLATES.items():
            print(f'  {name:12s} - {tmpl["title"]}')
        sys.exit(0)

    # Validation mode
    if args.validate:
        if not args.input:
            parser.error('--validate requires --input <file>')

        try:
            with open(args.input, 'r', encoding='utf-8') as f:
                text = f.read()
        except FileNotFoundError:
            print(f'Error: File not found: {args.input}', file=sys.stderr)
            sys.exit(1)

        violations = validate_job_description(text)
        print_validation_report(violations)
        sys.exit(1 if violations else 0)

    # Generation mode
    if not args.title or not args.company or not args.location:
        parser.error('Generation mode requires --title, --company, and --location')

    job_desc = generate_job_description(
        title=args.title,
        company=args.company,
        location=args.location,
        job_type=args.job_type,
        field=args.field,
        description=args.description or '',
        requirements=args.requirements,
        nice_to_have=args.nice_to_have_list,
        benefits=args.benefits,
        template_type=args.template,
    )

    # Validate the generated description
    violations = validate_job_description(job_desc)
    if violations:
        print('WARNING: Generated description has potential compliance issues:',
              file=sys.stderr)
        print_validation_report(violations)
        print('---', file=sys.stderr)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(job_desc)
        print(f'Job description written to {args.output}')
    else:
        print(job_desc)


if __name__ == '__main__':
    main()
