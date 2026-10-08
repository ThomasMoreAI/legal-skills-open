#!/usr/bin/env python3
"""
extract_and_chunk.py — Extração e chunking inteligente de processos jurídicos.

Recebe um PDF de processo judicial e:
1. Extrai texto completo (com fallback para OCR)
2. Divide por peça processual (não por página)
3. Salva chunks individuais + índice JSON

Usage:
    python3 extract_and_chunk.py --input processo.pdf --output ./analysis/
"""

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# Import enhanced utils
sys.path.insert(0, os.path.dirname(__file__))
from utils.dates import extract_all_dates, find_primary_date, format_date_br
from utils.cnj import parse_cnj, extract_cnj_numbers
from integrity_check import calculate_ocr_confidence


# ============================================================================
# PIECE DETECTION PATTERNS (Brazilian Legal System)
# ============================================================================

PIECE_PATTERNS = [
    # Fase Postulatória
    (r'(?i)(?:^|\n)\s*(?:PETIÇÃO\s+INICIAL|EXORDIAL)', 'PETIÇÃO INICIAL'),
    (r'(?i)(?:^|\n)\s*CONTESTAÇÃO', 'CONTESTAÇÃO'),
    (r'(?i)(?:^|\n)\s*(?:RÉPLICA|IMPUGNAÇÃO\s+À\s+CONTESTAÇÃO)', 'RÉPLICA'),
    (r'(?i)(?:^|\n)\s*RECONVENÇÃO', 'RECONVENÇÃO'),
    
    # Fase Instrutória
    (r'(?i)(?:^|\n)\s*ATA\s+DE\s+AUDIÊNCIA', 'ATA DE AUDIÊNCIA'),
    (r'(?i)(?:^|\n)\s*(?:LAUDO\s+PERICIAL|PERÍCIA|LAUDO\s+DO\s+PERITO)', 'LAUDO PERICIAL'),
    (r'(?i)(?:^|\n)\s*PARECER\s+(?:DO\s+MINISTÉRIO\s+PÚBLICO|DA\s+PROCURADORIA)', 'PARECER MP'),
    
    # Fase Decisória
    (r'(?i)(?:^|\n)\s*SENTENÇA', 'SENTENÇA'),
    (r'(?i)(?:^|\n)\s*ACÓRDÃO', 'ACÓRDÃO'),
    (r'(?i)(?:^|\n)\s*(?:DESPACHO|DECISÃO\s+INTERLOCUTÓRIA)', 'DESPACHO'),
    
    # Fase Recursal
    (r'(?i)(?:^|\n)\s*APELAÇÃO', 'APELAÇÃO'),
    (r'(?i)(?:^|\n)\s*(?:AGRAVO\s+DE\s+INSTRUMENTO|AGRAVO\s+INTERNO|AGRAVO)', 'AGRAVO'),
    (r'(?i)(?:^|\n)\s*EMBARGOS\s+(?:DE\s+DECLARAÇÃO|INFRINGENTES|DE\s+TERCEIRO)', 'EMBARGOS'),
    (r'(?i)(?:^|\n)\s*(?:RECURSO\s+ESPECIAL|RESP)', 'RECURSO ESPECIAL'),
    (r'(?i)(?:^|\n)\s*(?:RECURSO\s+EXTRAORDINÁRIO|RE\b)', 'RECURSO EXTRAORDINÁRIO'),
    (r'(?i)(?:^|\n)\s*CONTRARRAZÕES', 'CONTRARRAZÕES'),
    (r'(?i)(?:^|\n)\s*(?:RAZÕES\s+FINAIS|MEMORIAIS|ALEGAÇÕES\s+FINAIS)', 'MEMORIAIS'),
    
    # Fase Executória
    (r'(?i)(?:^|\n)\s*CUMPRIMENTO\s+DE\s+SENTENÇA', 'CUMPRIMENTO DE SENTENÇA'),
    (r'(?i)(?:^|\n)\s*IMPUGNAÇÃO\s+AO\s+CUMPRIMENTO', 'IMPUGNAÇÃO AO CUMPRIMENTO'),
    (r'(?i)(?:^|\n)\s*(?:TERMO\s+DE\s+PENHORA|AUTO\s+DE\s+PENHORA)', 'PENHORA'),
    (r'(?i)(?:^|\n)\s*ALVARÁ', 'ALVARÁ'),
    
    # Comunicações e Certidões
    (r'(?i)(?:^|\n)\s*(?:MANDADO\s+DE\s+CITAÇÃO|CARTA\s+PRECATÓRIA)', 'MANDADO/CARTA'),
    (r'(?i)(?:^|\n)\s*CERTIDÃO', 'CERTIDÃO'),
    (r'(?i)(?:^|\n)\s*OFÍCIO', 'OFÍCIO'),
    (r'(?i)(?:^|\n)\s*(?:PROCURAÇÃO|SUBSTABELECIMENTO)', 'PROCURAÇÃO'),
    
    # Tutelas e Liminares
    (r'(?i)(?:^|\n)\s*(?:TUTELA\s+(?:ANTECIPADA|DE\s+URGÊNCIA|PROVISÓRIA))', 'TUTELA'),
    (r'(?i)(?:^|\n)\s*(?:LIMINAR|MEDIDA\s+CAUTELAR)', 'LIMINAR/CAUTELAR'),
]

# Tribunal header patterns to strip
TRIBUNAL_HEADER_PATTERNS = [
    r'(?i)PODER\s+JUDICIÁRIO.*?\n',
    r'(?i)TRIBUNAL\s+DE\s+JUSTIÇA.*?\n',
    r'(?i)JUSTIÇA\s+(?:FEDERAL|DO\s+TRABALHO|ESTADUAL).*?\n',
    r'(?i)Processo\s+(?:Digital|Eletrônico).*?\n',
    r'(?i)Documento\s+assinado\s+digitalmente.*?\n(?:.*?\n){0,5}',
    r'(?i)Este\s+documento\s+(?:é|foi)\s+cópia.*?\n',
    r'(?i)Página\s+\d+\s+de\s+\d+',
    r'(?i)fls?\.\s*\d+',
]

# Date extraction patterns
DATE_PATTERNS = [
    r'(\d{1,2})\s+de\s+(janeiro|fevereiro|março|abril|maio|junho|julho|agosto|setembro|outubro|novembro|dezembro)\s+de\s+(\d{4})',
    r'(\d{2})[/.-](\d{2})[/.-](\d{4})',
    r'(\d{4})[/.-](\d{2})[/.-](\d{2})',
]

MONTH_MAP = {
    'janeiro': '01', 'fevereiro': '02', 'março': '03', 'abril': '04',
    'maio': '05', 'junho': '06', 'julho': '07', 'agosto': '08',
    'setembro': '09', 'outubro': '10', 'novembro': '11', 'dezembro': '12'
}

# Process number pattern (CNJ format)
PROCESSO_PATTERN = r'\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}'


def extract_text(pdf_path: str) -> str:
    """Extract text from PDF, with OCR fallback."""
    # Try pdftotext first
    try:
        result = subprocess.run(
            ['pdftotext', '-layout', pdf_path, '-'],
            capture_output=True, text=True, timeout=120
        )
        text = result.stdout
        
        # Check if we got meaningful text
        if len(text.strip()) > 100:
            return text
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    
    # Fallback: pypdf
    try:
        from pypdf import PdfReader
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text + "\n\n"
        
        if len(text.strip()) > 100:
            return text
    except Exception:
        pass
    
    # Fallback: OCR via pdftoppm + pytesseract
    try:
        import pytesseract
        from PIL import Image
        
        tmpdir = '/tmp/ocr_pages'
        os.makedirs(tmpdir, exist_ok=True)
        
        subprocess.run(
            ['pdftoppm', '-jpeg', '-r', '200', pdf_path, f'{tmpdir}/page'],
            capture_output=True, timeout=300
        )
        
        pages = sorted(Path(tmpdir).glob('page-*.jpg'))
        text = ""
        for page_img in pages:
            img = Image.open(page_img)
            page_text = pytesseract.image_to_string(img, lang='por')
            text += page_text + "\n\n"
        
        return text
    except Exception as e:
        print(f"[WARN] OCR fallback failed: {e}", file=sys.stderr)
        return ""


def strip_tribunal_headers(text: str) -> str:
    """Remove repetitive tribunal headers/footers."""
    for pattern in TRIBUNAL_HEADER_PATTERNS:
        text = re.sub(pattern, '', text)
    return text


def extract_dates(text: str) -> list:
    """Extract all dates found in text."""
    dates = []
    
    # Portuguese written dates
    for m in re.finditer(DATE_PATTERNS[0], text, re.IGNORECASE):
        day, month_name, year = m.groups()
        month = MONTH_MAP.get(month_name.lower(), '01')
        dates.append(f"{day.zfill(2)}/{month}/{year}")
    
    # DD/MM/YYYY
    for m in re.finditer(DATE_PATTERNS[1], text):
        day, month, year = m.groups()
        if 1 <= int(month) <= 12 and 1900 <= int(year) <= 2100:
            dates.append(f"{day}/{month}/{year}")
    
    return dates


def extract_processo_number(text: str) -> str | None:
    """Extract CNJ-format process number."""
    m = re.search(PROCESSO_PATTERN, text)
    return m.group(0) if m else None


def chunk_by_piece(text: str) -> list:
    """Split text into chunks by legal piece type."""
    all_matches = []
    
    for pattern, label in PIECE_PATTERNS:
        for m in re.finditer(pattern, text):
            all_matches.append((m.start(), label, m.group().strip()))
    
    # Sort by position
    all_matches.sort(key=lambda x: x[0])
    
    # Deduplicate close matches (within 200 chars)
    deduped = []
    for match in all_matches:
        if not deduped or match[0] - deduped[-1][0] > 200:
            deduped.append(match)
    
    chunks = []
    for i, (start, label, raw_header) in enumerate(deduped):
        end = deduped[i+1][0] if i+1 < len(deduped) else len(text)
        chunk_text = text[start:end].strip()

        if len(chunk_text) < 50:  # Skip tiny fragments
            continue

        # Enhanced: use utils for dates and CNJ parsing
        all_dates = extract_all_dates(chunk_text)
        dates_found = [format_date_br(d['parsed']) for d in all_dates]

        # Smart primary date extraction per piece type
        primary_result = find_primary_date(chunk_text, label)
        primary_date = format_date_br(primary_result['parsed']) if primary_result else None

        # Enhanced: CNJ number extraction with validation
        cnj_numbers = extract_cnj_numbers(chunk_text[:2000])
        processo = cnj_numbers[0].formatted if cnj_numbers else extract_processo_number(chunk_text[:1000])

        # Enhanced: OCR confidence scoring
        ocr_confidence = calculate_ocr_confidence(chunk_text)

        # Enhanced: page mapping from fls. markers
        fls_markers = re.findall(r'(?i)fls?\.\s*(\d+)', chunk_text)
        page_range = None
        if fls_markers:
            pages = [int(p) for p in fls_markers]
            page_range = {'start': min(pages), 'end': max(pages)}

        chunks.append({
            'index': len(chunks),
            'label': label,
            'raw_header': raw_header,
            'text': chunk_text,
            'char_start': start,
            'char_end': end,
            'char_count': len(chunk_text),
            'dates_found': dates_found,
            'processo_number': processo,
            'primary_date': primary_date,
            'ocr_confidence': ocr_confidence,
            'page_range': page_range,
        })

    # If no pieces detected, treat as single document
    if not chunks:
        all_dates = extract_all_dates(text[:5000])
        dates_found = [format_date_br(d['parsed']) for d in all_dates]
        cnj = extract_cnj_numbers(text[:2000])
        chunks = [{
            'index': 0,
            'label': 'DOCUMENTO_COMPLETO',
            'raw_header': '',
            'text': text,
            'char_start': 0,
            'char_end': len(text),
            'char_count': len(text),
            'dates_found': dates_found,
            'processo_number': cnj[0].formatted if cnj else extract_processo_number(text[:2000]),
            'primary_date': dates_found[0] if dates_found else None,
            'ocr_confidence': calculate_ocr_confidence(text[:5000]),
            'page_range': None,
        }]

    return chunks


def get_pdf_info(pdf_path: str) -> dict:
    """Get PDF metadata."""
    info = {'pages': 0, 'file_size_mb': 0}
    
    try:
        result = subprocess.run(
            ['pdfinfo', pdf_path], capture_output=True, text=True, timeout=30
        )
        for line in result.stdout.splitlines():
            if line.startswith('Pages:'):
                info['pages'] = int(line.split(':')[1].strip())
            elif line.startswith('File size:'):
                size_str = line.split(':')[1].strip()
                # Parse bytes
                num = int(re.search(r'\d+', size_str).group())
                info['file_size_mb'] = round(num / 1024 / 1024, 2)
            elif line.startswith('Title:'):
                info['title'] = line.split(':', 1)[1].strip()
            elif line.startswith('CreationDate:'):
                info['creation_date'] = line.split(':', 1)[1].strip()
    except Exception:
        # Fallback: file size from OS
        info['file_size_mb'] = round(os.path.getsize(pdf_path) / 1024 / 1024, 2)
    
    return info


def main():
    parser = argparse.ArgumentParser(description='Extract and chunk legal process PDFs')
    parser.add_argument('--input', '-i', required=True, help='Input PDF path')
    parser.add_argument('--output', '-o', required=True, help='Output directory')
    parser.add_argument('--strip-headers', action='store_true', default=True,
                        help='Strip tribunal headers (default: True)')
    parser.add_argument('--no-strip-headers', action='store_false', dest='strip_headers')
    args = parser.parse_args()
    
    input_path = args.input
    output_dir = args.output
    
    if not os.path.exists(input_path):
        print(f"[ERROR] File not found: {input_path}", file=sys.stderr)
        sys.exit(1)
    
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'chunks'), exist_ok=True)
    
    print(f"[1/4] Getting PDF info...")
    pdf_info = get_pdf_info(input_path)
    print(f"       Pages: {pdf_info.get('pages', '?')} | Size: {pdf_info.get('file_size_mb', '?')} MB")
    
    print(f"[2/4] Extracting text...")
    full_text = extract_text(input_path)
    
    if not full_text.strip():
        print("[ERROR] No text extracted. PDF may be image-only — try OCR.", file=sys.stderr)
        sys.exit(1)
    
    if args.strip_headers:
        full_text = strip_tribunal_headers(full_text)
    
    # Save full text
    with open(os.path.join(output_dir, 'full_text.txt'), 'w', encoding='utf-8') as f:
        f.write(full_text)
    print(f"       Extracted {len(full_text):,} characters")
    
    print(f"[3/4] Chunking by legal piece...")
    chunks = chunk_by_piece(full_text)
    print(f"       Found {len(chunks)} pieces")
    
    # Save individual chunks
    for chunk in chunks:
        chunk_filename = f"{chunk['index']:02d}-{chunk['label'].lower().replace(' ', '-')}.txt"
        with open(os.path.join(output_dir, 'chunks', chunk_filename), 'w', encoding='utf-8') as f:
            f.write(chunk['text'])
    
    # Save index (without full text to keep it small)
    print(f"[4/4] Generating index...")
    processo_number = None
    for c in chunks:
        if c.get('processo_number'):
            processo_number = c['processo_number']
            break
    
    index = {
        'generated_at': datetime.now().isoformat(),
        'source_file': os.path.basename(input_path),
        'pdf_info': pdf_info,
        'processo_number': processo_number,
        'total_characters': len(full_text),
        'total_chunks': len(chunks),
        'chunks': [
            {
                'index': c['index'],
                'label': c['label'],
                'char_count': c['char_count'],
                'primary_date': c['primary_date'],
                'dates_found': c['dates_found'],
                'processo_number': c['processo_number'],
                'ocr_confidence': c.get('ocr_confidence'),
                'page_range': c.get('page_range'),
                'chunk_file': f"chunks/{c['index']:02d}-{c['label'].lower().replace(' ', '-')}.txt"
            }
            for c in chunks
        ]
    }
    
    with open(os.path.join(output_dir, 'index.json'), 'w', encoding='utf-8') as f:
        json.dump(index, f, ensure_ascii=False, indent=2)
    
    print(f"\n✅ Done!")
    print(f"   Output: {output_dir}")
    print(f"   Index:  {output_dir}/index.json")
    print(f"   Chunks: {output_dir}/chunks/ ({len(chunks)} files)")
    print(f"\n   Pieces found:")
    for c in chunks:
        date_str = f" [{c['primary_date']}]" if c['primary_date'] else ""
        print(f"   {c['index']:02d}. {c['label']}{date_str} ({c['char_count']:,} chars)")


if __name__ == '__main__':
    main()
