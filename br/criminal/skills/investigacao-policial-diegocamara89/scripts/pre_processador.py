#!/usr/bin/env python3
"""
pre_processador.py — Pré-processamento de dados de investigação policial

Uso:
    python3 pre_processador.py /caminho/dos/arquivos /caminho/saida

Funcionalidades:
    - Extrai texto de PDFs (nativo e OCR)
    - Extrai dados de planilhas (XLSX, CSV)
    - Extrai texto de DOCX
    - Gera índice dos autos
    - Gera cronologia de eventos
"""

import os
import sys
import json
import re
from datetime import datetime
from pathlib import Path


def extrair_texto_pdf(filepath):
    """Extrai texto de PDF. Tenta pdfplumber primeiro, depois OCR."""
    texto_paginas = []
    
    try:
        import pdfplumber
        with pdfplumber.open(filepath) as pdf:
            for i, page in enumerate(pdf.pages):
                texto = page.extract_text()
                if texto and len(texto.strip()) > 50:
                    texto_paginas.append({
                        'pagina': i + 1,
                        'texto': texto,
                        'metodo': 'pdfplumber'
                    })
                else:
                    # Tentar OCR
                    texto_ocr = extrair_texto_ocr_pagina(filepath, i)
                    if texto_ocr:
                        texto_paginas.append({
                            'pagina': i + 1,
                            'texto': texto_ocr,
                            'metodo': 'OCR'
                        })
                    else:
                        texto_paginas.append({
                            'pagina': i + 1,
                            'texto': '[PÁGINA SEM TEXTO EXTRAÍVEL]',
                            'metodo': 'falha'
                        })
    except Exception as e:
        print(f"Erro ao processar PDF {filepath}: {e}")
    
    return texto_paginas


def extrair_texto_ocr_pagina(filepath, pagina_idx):
    """Extrai texto via OCR de uma página específica."""
    try:
        from pdf2image import convert_from_path
        import pytesseract
        
        images = convert_from_path(filepath, first_page=pagina_idx+1, 
                                    last_page=pagina_idx+1, dpi=300)
        if images:
            texto = pytesseract.image_to_string(images[0], lang='por')
            return texto if texto.strip() else None
    except Exception as e:
        print(f"OCR falhou para página {pagina_idx+1}: {e}")
    return None


def extrair_tabelas_pdf(filepath):
    """Extrai tabelas de PDF."""
    tabelas = []
    try:
        import pdfplumber
        with pdfplumber.open(filepath) as pdf:
            for i, page in enumerate(pdf.pages):
                page_tables = page.extract_tables()
                for j, table in enumerate(page_tables):
                    if table:
                        tabelas.append({
                            'pagina': i + 1,
                            'tabela_idx': j + 1,
                            'dados': table
                        })
    except Exception as e:
        print(f"Erro ao extrair tabelas de {filepath}: {e}")
    return tabelas


def extrair_dados_planilha(filepath):
    """Extrai dados de XLSX, XLS ou CSV."""
    try:
        import pandas as pd
        
        ext = Path(filepath).suffix.lower()
        if ext in ['.xlsx', '.xls']:
            xls = pd.ExcelFile(filepath)
            dados = {}
            for sheet in xls.sheet_names:
                df = pd.read_excel(filepath, sheet_name=sheet)
                dados[sheet] = {
                    'colunas': list(df.columns),
                    'linhas': len(df),
                    'dados': df.to_dict(orient='records')
                }
            return dados
        elif ext == '.csv':
            # Tentar diferentes encodings
            for enc in ['utf-8', 'latin-1', 'cp1252']:
                try:
                    df = pd.read_csv(filepath, encoding=enc)
                    return {
                        'Sheet1': {
                            'colunas': list(df.columns),
                            'linhas': len(df),
                            'dados': df.to_dict(orient='records')
                        }
                    }
                except:
                    continue
    except Exception as e:
        print(f"Erro ao extrair planilha {filepath}: {e}")
    return None


def extrair_texto_docx(filepath):
    """Extrai texto de DOCX."""
    try:
        import subprocess
        result = subprocess.run(
            ['pandoc', filepath, '-t', 'plain'],
            capture_output=True, text=True
        )
        return result.stdout
    except Exception as e:
        print(f"Erro ao extrair DOCX {filepath}: {e}")
    return None


def classificar_documento(texto, nome_arquivo):
    """Classifica tipo de documento policial baseado no conteúdo."""
    texto_lower = texto.lower() if texto else ''
    nome_lower = nome_arquivo.lower()
    
    classificacoes = {
        'portaria': ['portaria', 'instauração', 'instaura'],
        'boletim_ocorrencia': ['boletim de ocorrência', 'b.o.', 'reds', 'registro de evento'],
        'depoimento': ['depoimento', 'oitiva', 'declarações', 'inquirido'],
        'interrogatorio': ['interrogatório', 'interrogado', 'direito ao silêncio'],
        'laudo_pericial': ['laudo', 'perícia', 'perito', 'pericial', 'exame'],
        'auto_apreensao': ['auto de apreensão', 'auto de busca', 'apreensão'],
        'extrato_bancario': ['extrato', 'saldo', 'débito', 'crédito', 'banco'],
        'quebra_sigilo': ['sigilo', 'afastamento', 'quebra'],
        'rif_coaf': ['rif', 'coaf', 'uif', 'relatório de inteligência financeira'],
        'oficio': ['ofício', 'encaminho', 'solicito'],
        'certidao': ['certidão', 'certifico', 'dou fé'],
        'auto_flagrante': ['auto de prisão em flagrante', 'flagrante', 'apfd'],
        'mandado': ['mandado de busca', 'mandado de prisão'],
        'representacao': ['representação', 'represento'],
        'relatorio_investigacao': ['relatório de investigação', 'relatório parcial'],
        'dados_telefonicos': ['ere', 'erb', 'chamada', 'ligação', 'imei'],
    }
    
    for tipo, palavras in classificacoes.items():
        for palavra in palavras:
            if palavra in texto_lower or palavra in nome_lower:
                return tipo
    
    return 'outros'


def gerar_indice_autos(documentos):
    """Gera índice estruturado dos autos."""
    indice = []
    for doc in documentos:
        indice.append({
            'arquivo': doc['arquivo'],
            'tipo': doc.get('tipo', 'não classificado'),
            'paginas': doc.get('total_paginas', 'N/A'),
            'resumo': doc.get('resumo', ''),
        })
    return indice


def extrair_datas(texto):
    """Extrai datas do texto para construção de cronologia."""
    padroes = [
        r'(\d{2}/\d{2}/\d{4})',
        r'(\d{2}\.\d{2}\.\d{4})',
        r'(\d{2}-\d{2}-\d{4})',
        r'(\d{4}-\d{2}-\d{2})',
    ]
    datas = []
    for padrao in padroes:
        matches = re.findall(padrao, texto)
        datas.extend(matches)
    return list(set(datas))


def processar_diretorio(input_dir, output_dir):
    """Processa todos os arquivos de um diretório de investigação."""
    os.makedirs(output_dir, exist_ok=True)
    
    documentos = []
    
    for arquivo in sorted(os.listdir(input_dir)):
        filepath = os.path.join(input_dir, arquivo)
        if not os.path.isfile(filepath):
            continue
        
        ext = Path(arquivo).suffix.lower()
        doc_info = {
            'arquivo': arquivo,
            'caminho': filepath,
            'extensao': ext,
        }
        
        print(f"Processando: {arquivo}")
        
        if ext == '.pdf':
            paginas = extrair_texto_pdf(filepath)
            tabelas = extrair_tabelas_pdf(filepath)
            texto_completo = '\n'.join([p['texto'] for p in paginas])
            doc_info['paginas'] = paginas
            doc_info['tabelas'] = tabelas
            doc_info['total_paginas'] = len(paginas)
            doc_info['tipo'] = classificar_documento(texto_completo, arquivo)
            doc_info['datas'] = extrair_datas(texto_completo)
            doc_info['resumo'] = texto_completo[:500] + '...' if len(texto_completo) > 500 else texto_completo
            
        elif ext in ['.xlsx', '.xls', '.csv']:
            dados = extrair_dados_planilha(filepath)
            doc_info['dados_planilha'] = dados
            doc_info['tipo'] = 'planilha'
            
        elif ext == '.docx':
            texto = extrair_texto_docx(filepath)
            doc_info['texto'] = texto
            doc_info['tipo'] = classificar_documento(texto or '', arquivo)
            doc_info['datas'] = extrair_datas(texto or '')
            
        elif ext in ['.txt', '.md']:
            with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
                texto = f.read()
            doc_info['texto'] = texto
            doc_info['tipo'] = classificar_documento(texto, arquivo)
            doc_info['datas'] = extrair_datas(texto)
            
        elif ext in ['.jpg', '.jpeg', '.png', '.tiff', '.bmp']:
            try:
                import pytesseract
                from PIL import Image
                img = Image.open(filepath)
                texto = pytesseract.image_to_string(img, lang='por')
                doc_info['texto'] = texto
                doc_info['tipo'] = classificar_documento(texto, arquivo)
            except:
                doc_info['tipo'] = 'imagem'
        
        documentos.append(doc_info)
    
    # Gerar índice
    indice = gerar_indice_autos(documentos)
    
    # Salvar resultados
    with open(os.path.join(output_dir, 'indice_autos.json'), 'w', encoding='utf-8') as f:
        json.dump(indice, f, ensure_ascii=False, indent=2)
    
    with open(os.path.join(output_dir, 'documentos_processados.json'), 'w', encoding='utf-8') as f:
        # Salvar sem dados binários
        docs_clean = []
        for doc in documentos:
            doc_clean = {k: v for k, v in doc.items() 
                        if k not in ['dados_planilha']}  # planilhas salvas separadas
            docs_clean.append(doc_clean)
        json.dump(docs_clean, f, ensure_ascii=False, indent=2, default=str)
    
    # Salvar planilhas processadas separadamente
    for doc in documentos:
        if 'dados_planilha' in doc and doc['dados_planilha']:
            nome_base = Path(doc['arquivo']).stem
            with open(os.path.join(output_dir, f'planilha_{nome_base}.json'), 'w', encoding='utf-8') as f:
                json.dump(doc['dados_planilha'], f, ensure_ascii=False, indent=2, default=str)
    
    print(f"\nProcessamento concluído!")
    print(f"Total de documentos: {len(documentos)}")
    print(f"Tipos identificados:")
    tipos = {}
    for doc in documentos:
        t = doc.get('tipo', 'desconhecido')
        tipos[t] = tipos.get(t, 0) + 1
    for tipo, qtd in sorted(tipos.items()):
        print(f"  - {tipo}: {qtd}")
    print(f"\nResultados salvos em: {output_dir}")


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Uso: python3 pre_processador.py <diretorio_entrada> <diretorio_saida>")
        sys.exit(1)
    
    processar_diretorio(sys.argv[1], sys.argv[2])
