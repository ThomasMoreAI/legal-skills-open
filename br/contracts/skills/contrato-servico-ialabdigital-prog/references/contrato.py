#!/usr/bin/env python3
"""
Contrato - Gera contrato de prestação de serviços para lead fechado
"""

import sys
import os
import json
import shutil
from pathlib import Path
from typing import Dict, Optional
from datetime import datetime

BASE_DIR = Path(__file__).parent.parent.parent.parent
sys.path.insert(0, str(BASE_DIR))


def load_config() -> Dict:
    config_file = BASE_DIR / "prospector-config.json"
    if not config_file.exists():
        return {}
    return json.loads(config_file.read_text())


def load_lead(slug: str) -> Optional[Dict]:
    """Carrega lead do leads.md"""
    leads_file = BASE_DIR / "leads.md"
    if not leads_file.exists():
        return None
    
    content = leads_file.read_text(encoding='utf-8')
    for line in content.split('\n'):
        if '|' in line and not line.startswith('| #') and not line.startswith('|---'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 11:
                lead_slug = parts[1].lower().replace(' ', '-')
                if lead_slug == slug:
                    return {
                        'slug': slug,
                        'nome': parts[1],
                        'email': parts[4],
                        'telefone': parts[5],
                        'whatsapp': parts[6],
                        'site_atual': parts[7],
                        'motivo': parts[8],
                        'status': parts[9],
                        'url_nova': parts[10] if len(parts) > 10 else '',
                        'valor': parts[12] if len(parts) > 12 else '',
                        'manutencao': parts[13] if len(parts) > 13 else '',
                    }
    return None


def load_template() -> str:
    """Carrega template do contrato"""
    template_file = BASE_DIR / "skills" / "contrato-servico" / "references" / "contrato-template.md"
    if not template_file.exists():
        # Template padrão embutido
        return get_default_template()
    return template_file.read_text(encoding='utf-8')


def get_default_template() -> str:
    return '''# CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE DESENVOLVIMENTO WEB

**CONTRATANTE:** {{cliente_nome}}, {{cliente_cpf_cnpj}}, {{cliente_endereco}}
**CONTRATADO:** {{prestador_nome}}, {{prestador_cpf_cnpj}}, {{prestador_endereco}}

## 1. OBJETO
{{objeto}}. Inclui: estrutura responsiva, SEO on-page, integração WhatsApp, formulário de contato, deploy em servidor do CONTRATADO com SSL, página de proposta (antes/depois), e treinamento básico de edição.

## 2. PRAZO
Entrega em {{prazo_entrega}} dias úteis após: (a) assinatura deste contrato, (b) pagamento da entrada, (c) recebimento de todos os materiais (textos, fotos, logos, credenciais de domínio/hospedagem se aplicável).

## 3. VALOR E PAGAMENTO
- **Total:** R$ {{valor_total}}
- **Entrada ({{valor_entrada_pct}}%):** R$ {{valor_entrada}} — na assinatura
- **Parcelas:** {{parcelas}}x de R$ {{valor_parcela}} — vencimentos mensais a partir da entrega

{% if manutencao_mensal > 0 %}
- **Manutenção mensal (opcional):** R$ {{manutencao_mensal}}/mês — inclui hospedagem, SSL, backups semanais, atualizações de segurança, pequenas alterações de texto/imagem (até 2h/mês). Vigência: {{vigencia_manutencao}} meses, renovável automaticamente.
{% endif %}

Pagamento via PIX (chave informada pelo CONTRATADO) ou transferência. Comprovante = quitação.

## 4. OBRIGAÇÕES DO CONTRATANTE
- Fornecer materiais completos e corretos em até 7 dias da assinatura.
- Aprovar layout/estrutura em até 3 dias úteis após apresentação (silêncio = aprovação).
- Informar alterações de domínio, e-mail ou hospedagem com 30 dias de antecedência.

## 5. OBRIGAÇÕES DO CONTRATADO
- Entregar site funcional, responsivo, com SSL válido, nos prazos acordados.
- Garantir funcionamento por 30 dias pós-entrega (bugs = correção gratuita).
- Manter sigilo de dados e credenciais do CONTRATANTE.

## 6. PROPRIEDADE INTELECTUAL
Código, design e estrutura = propriedade do CONTRATADO (licença de uso perpétua ao CONTRATANTE para o fim contratado). Conteúdo (textos, fotos, marca) = propriedade do CONTRATANTE.

## 7. RESCISÃO
Qualquer parte pode rescindir com 15 dias de aviso prévio. Se o CONTRATANTE rescindir após início: entrada retida + proporcionais aos dias trabalhados. Se o CONTRATADO rescindir: devolve valores pagos integralmente.

## 8. FORO
Foro da comarca de {{cidade_foro}} para dirimir dúvidas.

---

**E, por estarem assim justos e contratados, assinam digitalmente:**

_________________________________________    _________________________________________
{{cliente_nome}}                              {{prestador_nome}}
Data: __/__/____                              Data: __/__/____'''


def render_template(template: str, data: Dict) -> str:
    """Renderiza template com dados"""
    import re
    result = template
    
    # Substitui variáveis simples {{var}}
    for key, value in data.items():
        if isinstance(value, (str, int, float)):
            result = result.replace(f'{{{{{key}}}}}', str(value))
        elif isinstance(value, bool):
            result = result.replace(f'{{{{{key}}}}}', 'Sim' if value else 'Não')
    
    # Condicionais {% if var %}...{% endif %}
    # Simple implementation - remove blocks where condition is false
    for key, value in data.items():
        if isinstance(value, (int, float)):
            is_true = value > 0
        elif isinstance(value, str):
            is_true = bool(value.strip())
        elif isinstance(value, bool):
            is_true = value
        else:
            is_true = bool(value)
        
        pattern = r'\{% if ' + key + r' %\}(.*?)\{% endif %\}'
        if is_true:
            result = re.sub(pattern, r'\1', result, flags=re.DOTALL)
        else:
            result = re.sub(pattern, '', result, flags=re.DOTALL)
    
    return result


def generate_contrato(slug: str, dados_extras: Dict = None) -> Dict:
    """Gera contrato para um lead"""
    print(f"📋 Gerando contrato para: {slug}")
    
    lead = load_lead(slug)
    if not lead:
        return {'success': False, 'error': f'Lead não encontrado: {slug}'}
    
    config = load_config()
    assinatura = config.get('assinatura', {})
    
    # Dados do template
    dados = {
        'cliente_nome': lead['nome'],
        'cliente_cpf_cnpj': dados_extras.get('cliente_cpf_cnpj', 'PENDENTE') if dados_extras else 'PENDENTE',
        'cliente_endereco': lead.get('endereco', '') or dados_extras.get('cliente_endereco', 'PENDENTE') if dados_extras else 'PENDENTE',
        'prestador_nome': assinatura.get('nome', ''),
        'prestador_cpf_cnpj': assinatura.get('cpf_cnpj', 'PENDENTE'),
        'prestador_endereco': assinatura.get('endereco', 'PENDENTE'),
        'objeto': 'Desenvolvimento de website institucional + página de proposta + deploy + SSL',
        'prazo_entrega': str(dados_extras.get('prazo_entrega', 15) if dados_extras else 15),
        'valor_total': f"{float(dados_extras.get('valor_total', 0)):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') if dados_extras else '0,00',
        'valor_entrada_pct': str(dados_extras.get('valor_entrada_pct', 50) if dados_extras else 50),
        'valor_entrada': f"{float(dados.get('valor_total', 0) * (dados.get('valor_entrada_pct', 50) / 100)):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') if dados else '0,00',
        'parcelas': str(dados.get('parcelas', 2) if dados else 2),
        'valor_parcela': f"{float(dados.get('valor_total', 0) * (100 - dados.get('valor_entrada_pct', 50)) / 100 / dados.get('parcelas', 2)):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.') if dados else '0,00',
        'manutencao_mensal': float(dados.get('manutencao_mensal', 0)) if dados else 0,
        'vigencia_manutencao': str(dados.get('vigencia_manutencao', 12) if dados else 12),
        'cidade_foro': dados.get('cidade_foro', 'São Paulo/SP') if dados else 'São Paulo/SP',
    }
    
    template = load_template()
    contrato_md = render_template(template, dados)
    
    # Salva arquivos
    contratos_dir = BASE_DIR / "contratos"
    contratos_dir.mkdir(parents=True, exist_ok=True)
    
    md_file = contratos_dir / f"{slug}-contrato.md"
    md_file.write_text(contrato_md, encoding='utf-8')
    
    # Gera HTML para impressão/PDF
    html = contrato_md.replace('\n', '<br>').replace('# ', '<h1>').replace('## ', '<h2>').replace('**', '<strong>').replace('*', '<em>')
    html = f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><title>Contrato - {lead['nome']}</title>
<style>body{{font-family:system-ui;max-width:800px;margin:0 auto;padding:40px 20px;line-height:1.6}}hr{{margin:30px 0}}pre{{white-space:pre-wrap}}</style></head><body>{html}</body></html>'''
    
    html_file = BASE_DIR / "contratos" / f"{slug}-contrato.html"
    html_file.write_text(html, encoding='utf-8')
    
    # Atualiza leads.md
    update_leads_md(slug, 'contratoStatus', 'enviado', datetime.now().isoformat())
    
    print(f"   ✅ Contrato gerado: {md_file}")
    return {
        'success': True,
        'slug': slug,
        'md_file': str(md_file),
        'html_file': str(html_file)
    }


def update_leads_md(slug: str, campo: str, valor: str, data: str = None):
    """Atualiza campo no leads.md"""
    leads_file = BASE_DIR / "leads.md"
    if not leads_file.exists():
        return
    
    lines = leads_file.read_text(encoding='utf-8').split('\n')
    for i, line in enumerate(lines):
        if '|' in line and not line.startswith('| #') and not line.startswith('|---'):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 2 and parts[1].lower().replace(' ', '-') == slug:
                # Mapear campo para índice
                idx_map = {'status': 9, 'url_nova': 10, 'data_proposta': 11, 'valor': 12, 'manutencao': 13, 'contratoStatus': 14, 'contratoEm': 15, 'pago': 16}
                if campo in idx_map and idx_map[campo] < len(parts):
                    parts[idx_map[campo]] = valor
                    if data and campo == 'contratoEm':
                        parts[idx_map['contratoEm']] = data[:10]
                    lines[i] = '| ' + ' | '.join(parts[1:-1]) + ' |'
                    break
    leads_file.write_text('\n'.join(lines), encoding='utf-8')


async def main():
    if len(sys.argv) < 2:
        print("Uso: python3 contrato.py <slug> [--valor VALOR] [--entrada PCT] [--parcelas N] [--manutencao VALOR] [--prazo DIAS] [--cpf CPF] [--endereco ENDERECO] [--foro CIDADE]")
        sys.exit(1)
    
    slug = sys.argv[1]
    dados_extras = {}
    
    # Parse args
    i = 2
    while i < len(sys.argv):
        arg = sys.argv[i]
        if arg == '--valor' and i+1 < len(sys.argv):
            dados_extras['valor_total'] = float(sys.argv[i+1])
            i += 2
        elif arg == '--entrada' and i+1 < len(sys.argv):
            dados_extras['valor_entrada_pct'] = int(sys.argv[i+1])
            i += 2
        elif arg == '--parcelas' and i+1 < len(sys.argv):
            dados_extras['parcelas'] = int(sys.argv[i+1])
            i += 2
        elif arg == '--manutencao' and i+1 < len(sys.argv):
            dados_extras['manutencao_mensal'] = float(sys.argv[i+1])
            i += 2
        elif arg == '--prazo' and i+1 < len(sys.argv):
            dados_extras['prazo_entrega'] = int(sys.argv[i+1])
            i += 2
        elif arg == '--cpf' and i+1 < len(sys.argv):
            dados_extras['cliente_cpf_cnpj'] = sys.argv[i+1]
            i += 2
        elif arg == '--endereco' and i+1 < len(sys.argv):
            dados_extras['cliente_endereco'] = sys.argv[i+1]
            i += 2
        elif arg == '--foro' and i+1 < len(sys.argv):
            dados_extras['cidade_foro'] = sys.argv[i+1]
            i += 2
        else:
            i += 1
    
    result = generate_contrato(slug, dados_extras)
    if result['success']:
        print(f"✅ Contrato gerado: {result['md_file']}")
        print(f"   HTML: {result['html_file']}")
    else:
        print(f"❌ {result['error']}")


if __name__ == '__main__':
    asyncio.run(main())