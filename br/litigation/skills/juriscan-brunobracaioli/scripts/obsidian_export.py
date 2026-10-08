#!/usr/bin/env python3
"""
obsidian_export.py — Gera vault Obsidian a partir da análise de processo jurídico.

Recebe o diretório de análise (com index.json + chunks analisados) e gera
uma estrutura de vault Obsidian com:
- _INDEX.md (resumo executivo)
- _TIMELINE.md (cronologia completa)
- _CONTRADIÇÕES.md (mapa de contradições)
- _ENTIDADES.md (partes, advogados, juízes)
- peças/ (uma nota por peça processual)
- legislação/ (uma nota por artigo citado)
- jurisprudência/ (uma nota por precedente)
- diagramas/ (Mermaid files)

Usage:
    python3 obsidian_export.py --input ./analysis/ --analysis ./analysis/analyzed.json --output ./vault/
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def sanitize_filename(name: str) -> str:
    """Make a string safe for filenames."""
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    name = re.sub(r'\s+', '-', name.strip())
    return name.lower()[:80]


def generate_frontmatter(data: dict) -> str:
    """Generate YAML frontmatter block."""
    lines = ['---']
    for key, value in data.items():
        if isinstance(value, list):
            lines.append(f'{key}:')
            for item in value:
                lines.append(f'  - "{item}"')
        elif value is not None:
            if isinstance(value, str) and (':' in value or '"' in value):
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f'{key}: {value}')
    lines.append('---')
    return '\n'.join(lines)


def generate_index(analysis: dict, processo_number: str) -> str:
    """Generate _INDEX.md — executive summary of the case."""
    fm = generate_frontmatter({
        'tipo': 'índice-processo',
        'processo': processo_number or 'N/A',
        'gerado_em': datetime.now().strftime('%Y-%m-%d %H:%M'),
        'total_pecas': len(analysis.get('chunks', [])),
        'tags': ['processo', 'índice', 'mapa'],
    })
    
    chunks = analysis.get('chunks', [])
    
    md = f"""{fm}

# 📋 Processo {processo_number or 'N/A'}

## Resumo Executivo

> [!summary] Visão Geral
> Processo com **{len(chunks)} peças** analisadas.
> Veja [[_TIMELINE|Timeline Completa]] | [[_CONTRADIÇÕES|Mapa de Contradições]] | [[_ENTIDADES|Entidades]]

## Mapa de Peças

| # | Peça | Data | Chars | Link |
|---|------|------|-------|------|
"""
    
    for i, chunk in enumerate(chunks):
        label = chunk.get('label', f'Peça {i}')
        date = chunk.get('primary_date', '—')
        chars = chunk.get('char_count', 0)
        filename = f"{i:02d}-{sanitize_filename(label)}"
        md += f"| {i:02d} | {label} | {date} | {chars:,} | [[peças/{filename}\\|Ver]] |\n"
    
    md += """
## Links Rápidos

- [[_TIMELINE|📅 Timeline Cronológica]]
- [[_CONTRADIÇÕES|⚠️ Contradições Detectadas]]
- [[_ENTIDADES|👥 Partes e Entidades]]

## Análise Detalhada por Peça

"""
    
    for i, chunk in enumerate(chunks):
        label = chunk.get('label', f'Peça {i}')
        filename = f"{i:02d}-{sanitize_filename(label)}"
        resumo = chunk.get('resumo', 'Resumo não disponível.')
        md += f"### {i:02d}. [[peças/{filename}|{label}]]\n\n{resumo}\n\n"
    
    return md


def generate_timeline(analysis: dict, processo_number: str) -> str:
    """Generate _TIMELINE.md with chronological events."""
    fm = generate_frontmatter({
        'tipo': 'timeline',
        'processo': processo_number or 'N/A',
        'tags': ['processo', 'timeline', 'cronologia'],
    })
    
    events = []
    for chunk in analysis.get('chunks', []):
        if chunk.get('primary_date'):
            events.append({
                'date': chunk['primary_date'],
                'label': chunk.get('label', 'N/A'),
                'resumo': chunk.get('resumo', ''),
                'decisao': chunk.get('decisao'),
            })
        for prazo in chunk.get('prazos', []):
            if prazo.get('data_inicio') or prazo.get('data_fim'):
                events.append({
                    'date': prazo.get('data_inicio') or prazo.get('data_fim'),
                    'label': f"⏰ PRAZO: {prazo.get('tipo', 'N/A')}",
                    'resumo': f"Prazo de {prazo.get('tipo', 'N/A')}",
                })
    
    # Sort by date (best effort)
    def parse_date_sort(d):
        try:
            parts = d.split('/')
            if len(parts) == 3:
                return f"{parts[2]}{parts[1]}{parts[0]}"
        except:
            pass
        return d
    
    events.sort(key=lambda x: parse_date_sort(x.get('date', '')))
    
    md = f"""{fm}

# 📅 Timeline — Processo {processo_number or 'N/A'}

⬅️ [[_INDEX|Voltar ao Índice]]

"""
    
    for evt in events:
        decisao = f"\n> **Decisão:** {evt['decisao']}" if evt.get('decisao') else ""
        md += f"""### {evt['date']} — {evt['label']}

{evt.get('resumo', '')}{decisao}

---

"""
    
    # Mermaid gantt
    md += """## Diagrama Visual

```mermaid
gantt
    title Timeline do Processo
    dateFormat  DD/MM/YYYY
"""
    
    for evt in events:
        safe_label = evt['label'].replace('"', "'")[:40]
        md += f"    {safe_label} : {evt['date']}, 1d\n"
    
    md += "```\n"
    
    return md


def generate_contradictions(analysis: dict, processo_number: str) -> str:
    """Generate _CONTRADIÇÕES.md."""
    fm = generate_frontmatter({
        'tipo': 'contradições',
        'processo': processo_number or 'N/A',
        'tags': ['processo', 'contradições', 'análise-forense'],
    })
    
    contradictions = analysis.get('contradictions', [])
    
    md = f"""{fm}

# ⚠️ Contradições — Processo {processo_number or 'N/A'}

⬅️ [[_INDEX|Voltar ao Índice]]

> [!warning] Contradições Detectadas
> Total de **{len(contradictions)}** contradições/inconsistências identificadas.

"""
    
    if not contradictions:
        md += "> Nenhuma contradição registrada. Execute a análise de contradições para popular esta seção.\n"
        return md
    
    for i, c in enumerate(contradictions):
        impact_icon = {'ALTO': '🔴', 'MÉDIO': '🟡', 'BAIXO': '🟢'}.get(c.get('impacto', ''), '⚪')
        
        md += f"""## {i+1}. {c.get('tipo', 'N/A')} {impact_icon}

**Impacto:** {c.get('impacto', 'N/A')}
**Peças envolvidas:** {', '.join(c.get('pecas', []))}

### Divergência

{c.get('descricao', 'N/A')}

### Exploração Processual

{c.get('sugestao', 'N/A')}

---

"""
    
    return md


def generate_entities(analysis: dict, processo_number: str) -> str:
    """Generate _ENTIDADES.md with all parties and entities."""
    fm = generate_frontmatter({
        'tipo': 'entidades',
        'processo': processo_number or 'N/A',
        'tags': ['processo', 'entidades', 'partes'],
    })
    
    # Aggregate entities from all chunks
    all_autores = set()
    all_reus = set()
    all_advogados = set()
    all_juizes = set()
    all_peritos = set()
    varas = set()
    
    for chunk in analysis.get('chunks', []):
        partes = chunk.get('partes', {})
        for a in partes.get('autor', []):
            all_autores.add(a)
        for r in partes.get('reu', []):
            all_reus.add(r)
        for adv in partes.get('advogados_autor', []) + partes.get('advogados_reu', []):
            all_advogados.add(adv)
        if partes.get('juiz'):
            all_juizes.add(partes['juiz'])
        if partes.get('perito'):
            all_peritos.add(partes['perito'])
        if partes.get('vara'):
            varas.add(partes['vara'])
    
    md = f"""{fm}

# 👥 Entidades — Processo {processo_number or 'N/A'}

⬅️ [[_INDEX|Voltar ao Índice]]

## Polo Ativo (Autor/Requerente)

"""
    for a in sorted(all_autores):
        md += f"- **{a}**\n"
    
    md += "\n## Polo Passivo (Réu/Requerido)\n\n"
    for r in sorted(all_reus):
        md += f"- **{r}**\n"
    
    md += "\n## Advogados\n\n"
    for adv in sorted(all_advogados):
        md += f"- {adv}\n"
    
    md += "\n## Magistrados\n\n"
    for j in sorted(all_juizes):
        md += f"- **{j}**\n"
    
    if all_peritos:
        md += "\n## Peritos\n\n"
        for p in sorted(all_peritos):
            md += f"- {p}\n"
    
    if varas:
        md += "\n## Varas / Câmaras\n\n"
        for v in sorted(varas):
            md += f"- {v}\n"
    
    return md


def generate_piece_note(chunk: dict, index: int, processo_number: str) -> str:
    """Generate a note for a single legal piece."""
    label = chunk.get('label', f'Peça {index}')
    
    fm_data = {
        'tipo': sanitize_filename(label),
        'processo': processo_number or 'N/A',
        'data': chunk.get('primary_date') or chunk.get('data'),
    }
    
    partes = chunk.get('partes', {})
    if partes.get('autor'):
        fm_data['partes_autor'] = partes['autor']
    if partes.get('reu'):
        fm_data['partes_reu'] = partes['reu']
    if partes.get('juiz'):
        fm_data['juiz'] = partes['juiz']
    if partes.get('vara'):
        fm_data['vara'] = partes['vara']
    
    valores = chunk.get('valores', {})
    if valores.get('causa'):
        fm_data['valor_causa'] = valores['causa']
    if valores.get('condenacao'):
        fm_data['valor_condenacao'] = valores['condenacao']
    
    fm_data['tags'] = ['processo', 'peça', sanitize_filename(label)]
    
    fm = generate_frontmatter(fm_data)
    
    md = f"""{fm}

# {label}

⬅️ [[../_INDEX|Voltar ao Índice]] | [[../_TIMELINE|Timeline]]

"""
    
    if chunk.get('resumo'):
        md += f"> [!abstract] Resumo\n> {chunk['resumo']}\n\n"
    
    if chunk.get('assunto'):
        md += f"**Assunto:** {chunk['assunto']}\n\n"
    
    # Pedidos
    if chunk.get('pedidos'):
        md += "## Pedidos\n\n"
        for p in chunk['pedidos']:
            md += f"- {p}\n"
        md += "\n"
    
    # Argumentos
    if chunk.get('argumentos_chave'):
        md += "## Argumentos-Chave\n\n"
        for a in chunk['argumentos_chave']:
            md += f"- {a}\n"
        md += "\n"
    
    # Decisão
    if chunk.get('decisao'):
        md += f"## Decisão\n\n> [!verdict] Dispositivo\n> {chunk['decisao']}\n\n"
    
    # Fatos relevantes
    if chunk.get('fatos_relevantes'):
        md += "## Fatos Relevantes\n\n"
        for f in chunk['fatos_relevantes']:
            md += f"- {f}\n"
        md += "\n"
    
    # Valores
    if valores and any(valores.values()):
        md += "## Valores\n\n"
        if valores.get('causa'):
            md += f"- **Valor da causa:** {valores['causa']}\n"
        if valores.get('condenacao'):
            md += f"- **Condenação:** {valores['condenacao']}\n"
        if valores.get('honorarios'):
            md += f"- **Honorários:** {valores['honorarios']}\n"
        for outro in valores.get('outros', []):
            md += f"- **{outro.get('descricao', 'Outro')}:** {outro.get('valor', 'N/A')}\n"
        md += "\n"
    
    # Legislação
    if chunk.get('artigos_lei'):
        md += "## Legislação Citada\n\n"
        for art in chunk['artigos_lei']:
            # Create wikilink
            safe = sanitize_filename(art[:50])
            md += f"- [[legislação/{safe}|{art}]]\n"
        md += "\n"
    
    # Jurisprudência
    if chunk.get('jurisprudencia'):
        md += "## Jurisprudência\n\n"
        for j in chunk['jurisprudencia']:
            safe = sanitize_filename(j[:50])
            md += f"- [[jurisprudência/{safe}|{j}]]\n"
        md += "\n"
    
    # Prazos
    if chunk.get('prazos'):
        md += "## Prazos\n\n"
        for p in chunk['prazos']:
            md += f"- **{p.get('tipo', 'N/A')}**: {p.get('data_inicio', '?')} → {p.get('data_fim', '?')}\n"
        md += "\n"
    
    return md


def generate_legislation_note(article: str) -> str:
    """Generate a stub note for a cited law article."""
    fm = generate_frontmatter({
        'tipo': 'legislação',
        'artigo': article,
        'tags': ['legislação'],
    })
    
    return f"""{fm}

# {article}

> [!info] Artigo de Lei
> Referenciado no processo. Adicione aqui o texto integral e anotações.

## Texto do Artigo

_Insira o texto do artigo aqui._

## Notas

## Peças que Citam

_Links automáticos via backlinks do Obsidian._
"""


def generate_jurisprudence_note(reference: str) -> str:
    """Generate a stub note for cited jurisprudence."""
    fm = generate_frontmatter({
        'tipo': 'jurisprudência',
        'referencia': reference,
        'tags': ['jurisprudência'],
    })
    
    return f"""{fm}

# {reference}

> [!scales] Precedente Judicial
> Jurisprudência citada no processo.

## Ementa

_Insira a ementa aqui._

## Tese Firmada

_Insira a tese aqui._

## Peças que Citam

_Links automáticos via backlinks do Obsidian._
"""


def generate_risk_view(analysis: dict, processo_number: str) -> str:
    """Generate _RISCO.md — risk assessment dashboard."""
    fm = generate_frontmatter({
        'tipo': 'risco',
        'processo': processo_number or 'N/A',
        'tags': ['processo', 'risco', 'análise-forense'],
    })

    risk = analysis.get('risk_assessment', {})
    level = risk.get('risk_level', 'N/A')
    score = risk.get('overall_score', 'N/A')
    icon = {'ALTO': '🔴', 'MÉDIO': '🟡', 'BAIXO': '🟢'}.get(level, '⚪')

    md = f"""{fm}

# {icon} Avaliação de Risco — Processo {processo_number or 'N/A'}

⬅️ [[_INDEX|Voltar ao Índice]]

> [!warning] Risco: {level} ({score}/10)

## Risco Processual

"""
    proc = risk.get('procedural_risk', {})
    md += f"**Score:** {proc.get('score', 'N/A')}/10\n\n"
    for f in proc.get('factors', []):
        md += f"- {f.get('fator', '')} (impacto: {f.get('impacto', '')})\n"

    md += "\n## Indicadores de Mérito\n\n"
    merit = risk.get('merit_indicators', {})
    md += f"**Score:** {merit.get('score', 'N/A')}/10\n\n"
    if merit.get('favorable_factors'):
        md += "### Fatores Favoráveis\n\n"
        for f in merit['favorable_factors']:
            md += f"- ✅ {f.get('fator', '')}\n"
    if merit.get('unfavorable_factors'):
        md += "\n### Fatores Desfavoráveis\n\n"
        for f in merit['unfavorable_factors']:
            md += f"- ❌ {f.get('fator', '')}\n"

    md += "\n## Exposição Monetária\n\n"
    monetary = risk.get('monetary_exposure', {})
    if monetary.get('max_exposure'):
        md += f"- **Exposição máxima:** {monetary['max_exposure']}\n"
    likely = monetary.get('likely_range', {})
    if likely.get('min') or likely.get('max'):
        md += f"- **Faixa provável:** {likely.get('min', '?')} — {likely.get('max', '?')}\n"
    costs = monetary.get('costs', {})
    if costs.get('honorarios_sucumbencia'):
        md += f"- **Honorários sucumbência:** {costs['honorarios_sucumbencia']}\n"

    recs = risk.get('strategic_recommendations', [])
    if recs:
        md += "\n## Recomendações Estratégicas\n\n"
        for r in recs:
            md += f"1. {r}\n"

    return md


def generate_instance_view(analysis: dict, processo_number: str) -> str:
    """Generate _INSTÂNCIAS.md — argument evolution across instances."""
    fm = generate_frontmatter({
        'tipo': 'instâncias',
        'processo': processo_number or 'N/A',
        'tags': ['processo', 'instâncias', 'argumentos'],
    })

    tracking = analysis.get('instance_tracking', {})
    instances = tracking.get('instances', {})
    tracks = tracking.get('argument_tracks', [])

    md = f"""{fm}

# 🏛️ Rastreamento por Instância — Processo {processo_number or 'N/A'}

⬅️ [[_INDEX|Voltar ao Índice]]

## Fluxo entre Instâncias

"""
    order = ['1a_instancia', 'tj', 'stj', 'stf']
    labels = {'1a_instancia': '1ª Instância', 'tj': 'Tribunal de Justiça', 'stj': 'STJ', 'stf': 'STF'}

    for inst in order:
        data = instances.get(inst)
        if not data:
            continue
        md += f"### {labels.get(inst, inst)}\n\n"
        for p in data.get('pieces', []):
            md += f"- **{p.get('label', '?')}** ({p.get('data', '?')})\n"
        if data.get('decisao_final'):
            md += f"\n> **Decisão:** {data['decisao_final'][:200]}\n"
        if data.get('resultado'):
            md += f"> **Resultado:** {data['resultado']}\n"
        md += "\n---\n\n"

    if tracks:
        md += "## Evolução de Argumentos\n\n"
        md += "| Argumento | Instâncias | Status |\n|---|---|---|\n"
        for t in tracks[:20]:
            insts = ', '.join(t.get('instancias_presentes', []))
            status = t.get('status_final', '—')
            arg = t.get('argumento', '?')[:80]
            md += f"| {arg} | {insts} | {status} |\n"

    return md


def generate_prazo_view(analysis: dict, processo_number: str) -> str:
    """Generate _PRAZOS.md — deadline dashboard."""
    fm = generate_frontmatter({
        'tipo': 'prazos',
        'processo': processo_number or 'N/A',
        'tags': ['processo', 'prazos', 'deadlines'],
    })

    prazos = analysis.get('prazos_calculados', [])

    md = f"""{fm}

# ⏰ Prazos Processuais — Processo {processo_number or 'N/A'}

⬅️ [[_INDEX|Voltar ao Índice]]

"""
    if not prazos:
        md += "> Nenhum prazo calculado. Execute `prazo_calculator.py` para popular esta seção.\n"
        return md

    vencidos = [p for p in prazos if p.get('status') == 'vencido']
    em_prazo = [p for p in prazos if p.get('status') == 'em_prazo']
    ultimo = [p for p in prazos if p.get('status') == 'ultimo_dia']

    md += f"> **Total:** {len(prazos)} prazo(s) | "
    md += f"🟢 Em prazo: {len(em_prazo)} | "
    md += f"🟡 Último dia: {len(ultimo)} | "
    md += f"🔴 Vencidos: {len(vencidos)}\n\n"

    md += "| Tipo | Fundamento | Intimação | Limite | Status | Restante |\n"
    md += "|---|---|---|---|---|---|\n"

    for p in prazos:
        icon = {'em_prazo': '🟢', 'ultimo_dia': '🟡', 'vencido': '🔴'}.get(p.get('status', ''), '⚪')
        rest = f"{p.get('dias_restantes', '—')} dias" if p.get('dias_restantes') is not None else '—'
        md += (
            f"| {p.get('tipo', '?')} | {p.get('fundamento_legal', '?')} | "
            f"{p.get('data_intimacao', '?')} | {p.get('data_limite', '?')} | "
            f"{icon} {p.get('status', '?')} | {rest} |\n"
        )

    return md


def generate_auditoria_view(analysis: dict, processo_number: str) -> str:
    """v3 — Render auditor_findings grouped by impact. Phase 6 Step 6.3."""
    findings = analysis.get('auditor_findings') or []
    if not findings:
        return ""
    impact_order = {'ALTO': 0, 'MÉDIO': 1, 'BAIXO': 2}
    findings_sorted = sorted(findings, key=lambda f: impact_order.get(f.get('impacto', 'BAIXO'), 3))

    lines = [
        "---",
        f"processo: \"{processo_number}\"",
        "tipo: auditoria",
        "---",
        "",
        "# Auditoria Processual",
        "",
        "Findings do `juriscan-auditor-processual` — análise imparcial de vícios,",
        "nulidades, omissões e gatilhos processuais que nenhum dos advogados",
        "tem incentivo de apontar.",
        "",
        f"**Total de findings:** {len(findings_sorted)}",
        "",
    ]
    for i, f in enumerate(findings_sorted, 1):
        tipo = f.get('tipo', 'OUTRO')
        impacto = f.get('impacto', '?')
        fundamento = f.get('fundamento', '')
        peca_ref = f.get('peca_ref', '')
        lines += [
            f"## {i}. {tipo} — impacto {impacto}",
            "",
            f"**Fundamento:** {fundamento}",
        ]
        if peca_ref:
            lines.append(f"**Peça:** {peca_ref}")
        lines += [
            "",
            f"**Descrição:** {f.get('descricao', '')}",
            "",
            f"**Ação sugerida:** {f.get('acao_sugerida', '')}",
            "",
            "---",
            "",
        ]
    lines += ["", "⬅️ [[_INDEX|Voltar ao Índice]]", ""]
    return "\n".join(lines)


def generate_verificacoes_view(analysis: dict, processo_number: str) -> str:
    """v3 — Render verifications as a status table. Phase 6 Step 6.3."""
    verifications = analysis.get('verifications') or []
    if not verifications:
        return ""
    summary = analysis.get('verification_summary') or {}
    status_emoji = {
        'CONFIRMADO': '✅',
        'DIVERGENTE': '⚠️',
        'NAO_ENCONTRADO': '❌',
    }
    lines = [
        "---",
        f"processo: \"{processo_number}\"",
        "tipo: verificações",
        "---",
        "",
        "# Verificações de Jurisprudência",
        "",
        "Citações verificadas pelo `juriscan-verificador` contra fontes oficiais",
        "(whitelist em `references/whitelist_fontes.json`).",
        "",
    ]
    if summary:
        lines += [
            f"**Total:** {summary.get('total_verifications', len(verifications))} | "
            f"✅ {summary.get('confirmed', 0)} | "
            f"⚠️ {summary.get('divergent', 0)} | "
            f"❌ {summary.get('unverified', 0)}",
            "",
        ]
    lines += [
        "| Status | Tipo | Citação | Fonte | Data de acesso |",
        "|---|---|---|---|---|",
    ]
    for v in verifications:
        status = v.get('status', '?')
        emoji = status_emoji.get(status, '?')
        tipo = v.get('tipo', '')
        citacao = (v.get('citacao_original') or '').replace('|', '\\|')
        url = v.get('source_url') or ''
        fonte_link = f"[link]({url})" if url else '—'
        data = v.get('access_date') or ''
        lines.append(f"| {emoji} {status} | {tipo} | {citacao} | {fonte_link} | {data} |")
    # Detailed divergences
    divergents = [v for v in verifications if v.get('status') == 'DIVERGENTE']
    if divergents:
        lines += ["", "## Divergências", ""]
        for v in divergents:
            lines += [
                f"### {v.get('citacao_original', '')}",
                "",
                f"**Divergência:** {v.get('divergencia') or '(não explicitada)'}",
                "",
                f"**Trecho oficial:** > {v.get('trecho_oficial') or '—'}",
                "",
            ]
    lines += ["", "⬅️ [[_INDEX|Voltar ao Índice]]", ""]
    return "\n".join(lines)


def generate_perspectives_view(analysis: dict, processo_number: str) -> str:
    """v3 — Two-column perspectives (autor vs. réu). Phase 6 Step 6.3."""
    perspectives = analysis.get('perspectives') or {}
    autor = perspectives.get('autor')
    reu = perspectives.get('reu')
    if not (autor or reu):
        return ""

    def _section(label: str, persp: dict | None) -> list[str]:
        if not persp:
            return [f"## {label}", "", "_sem dados_", ""]
        out = [
            f"## {label}",
            "",
            f"**Risco:** {persp.get('risk_level', '?')} (score {persp.get('risk_score', '?')}/10)",
            "",
            "### Forças",
        ]
        for f in (persp.get('forcas') or []):
            out.append(f"- **{f.get('titulo', '')}** — {f.get('descricao', '')}")
        out += ["", "### Fraquezas"]
        for f in (persp.get('fraquezas') or []):
            out.append(f"- **{f.get('titulo', '')}** — {f.get('descricao', '')}")
        out += ["", "### Recursos cabíveis"]
        for r in (persp.get('recursos_cabiveis') or []):
            out.append(
                f"- **{r.get('recurso', '')}** — {r.get('cabimento', '')} "
                f"(prazo {r.get('prazo_dias', '?')}d)"
            )
        out.append("")
        return out

    lines = [
        "---",
        f"processo: \"{processo_number}\"",
        "tipo: perspectivas",
        "---",
        "",
        "# Perspectivas (Polos Ativo × Passivo)",
        "",
        "Análise dialética do `juriscan-advogado-autor` e `juriscan-advogado-reu`.",
        "Os dois scores medem coisas diferentes — risco é sempre relativo ao polo.",
        "",
    ]
    lines += _section("⚖️ Autor (polo ativo)", autor)
    lines += _section("🛡️ Réu (polo passivo)", reu)
    lines += ["", "⬅️ [[_INDEX|Voltar ao Índice]]", ""]
    return "\n".join(lines)


def export_vault(analysis: dict, output_dir: str):
    """Export full Obsidian vault structure."""
    processo_number = analysis.get('processo_number', 'N/A')

    # Create directories
    dirs = ['peças', 'legislação', 'jurisprudência', 'diagramas']
    for d in dirs:
        os.makedirs(os.path.join(output_dir, d), exist_ok=True)

    # Generate main files
    files = {
        '_INDEX.md': generate_index(analysis, processo_number),
        '_TIMELINE.md': generate_timeline(analysis, processo_number),
        '_CONTRADIÇÕES.md': generate_contradictions(analysis, processo_number),
        '_ENTIDADES.md': generate_entities(analysis, processo_number),
        '_RISCO.md': generate_risk_view(analysis, processo_number),
        '_INSTÂNCIAS.md': generate_instance_view(analysis, processo_number),
        '_PRAZOS.md': generate_prazo_view(analysis, processo_number),
    }

    # Phase 6 Step 6.3 — v3 views, only generated when the corresponding fields
    # are present. Backwards compat: legacy v2 outputs produce the same file set
    # as before.
    auditoria = generate_auditoria_view(analysis, processo_number)
    if auditoria:
        files['_AUDITORIA.md'] = auditoria
    verificacoes = generate_verificacoes_view(analysis, processo_number)
    if verificacoes:
        files['_VERIFICAÇÕES.md'] = verificacoes
    perspectivas = generate_perspectives_view(analysis, processo_number)
    if perspectivas:
        files['_PERSPECTIVAS.md'] = perspectivas
    
    for filename, content in files.items():
        with open(os.path.join(output_dir, filename), 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Generate piece notes
    all_articles = set()
    all_jurisprudence = set()
    
    for i, chunk in enumerate(analysis.get('chunks', [])):
        label = chunk.get('label', f'peça-{i}')
        filename = f"{i:02d}-{sanitize_filename(label)}.md"
        content = generate_piece_note(chunk, i, processo_number)
        
        with open(os.path.join(output_dir, 'peças', filename), 'w', encoding='utf-8') as f:
            f.write(content)
        
        for art in chunk.get('artigos_lei', []):
            all_articles.add(art)
        for jur in chunk.get('jurisprudencia', []):
            all_jurisprudence.add(jur)
    
    # Generate legislation stubs
    for art in all_articles:
        filename = f"{sanitize_filename(art[:50])}.md"
        content = generate_legislation_note(art)
        with open(os.path.join(output_dir, 'legislação', filename), 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Generate jurisprudence stubs
    for jur in all_jurisprudence:
        filename = f"{sanitize_filename(jur[:50])}.md"
        content = generate_jurisprudence_note(jur)
        with open(os.path.join(output_dir, 'jurisprudência', filename), 'w', encoding='utf-8') as f:
            f.write(content)
    
    # Generate reference graph mermaid
    mermaid = "graph LR\n"
    for i, chunk in enumerate(analysis.get('chunks', [])):
        label = chunk.get('label', f'P{i}')
        node_id = f"P{i}"
        mermaid += f'    {node_id}["{label}"]\n'
        
        for art in chunk.get('artigos_lei', [])[:8]:  # Top 8 per piece
            art_id = f"L_{sanitize_filename(art[:20]).replace('-', '_')}"
            mermaid += f'    {node_id} --> {art_id}["{art[:30]}"]\n'
    
    with open(os.path.join(output_dir, 'diagramas', 'reference-graph.mermaid'), 'w', encoding='utf-8') as f:
        f.write(mermaid)
    
    return {
        'output_dir': output_dir,
        'files_created': sum(len(files) for _, _, files in os.walk(output_dir)),
        'pieces': len(analysis.get('chunks', [])),
        'legislation_stubs': len(all_articles),
        'jurisprudence_stubs': len(all_jurisprudence),
    }


def main():
    parser = argparse.ArgumentParser(description='Export legal analysis to Obsidian vault')
    parser.add_argument('--analysis', '-a', required=True, help='Path to analyzed.json')
    parser.add_argument('--output', '-o', required=True, help='Output vault directory')
    args = parser.parse_args()
    
    with open(args.analysis, 'r', encoding='utf-8') as f:
        analysis = json.load(f)
    
    result = export_vault(analysis, args.output)
    
    print(f"\n✅ Obsidian vault exported!")
    print(f"   Output: {result['output_dir']}")
    print(f"   Pieces: {result['pieces']}")
    print(f"   Legislation stubs: {result['legislation_stubs']}")
    print(f"   Jurisprudence stubs: {result['jurisprudence_stubs']}")
    print(f"\n   Abra a pasta no Obsidian como vault e aproveite os backlinks automáticos!")


if __name__ == '__main__':
    main()
