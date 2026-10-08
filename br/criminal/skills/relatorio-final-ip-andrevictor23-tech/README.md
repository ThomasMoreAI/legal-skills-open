# relatorio-final-ip

> Produz relatórios finais de inquérito policial no padrão real da Delegacia de Polícia de Alta Floresta/MT e do NEAMV, entregues formatados diretamente no chat.

**English summary:** Produces the final report of a Brazilian police investigation (inquérito policial) in the real template of the Alta Floresta/MT precinct and its domestic-violence unit (NEAMV): pre-processes case files with local OCR, builds a chronology and an evidence-confrontation matrix, applies precise criminal classification, and self-checks the draft against per-offense checklists before delivery. Always a draft for the authority's review and signature.

## O que faz

A skill assume a persona de Delegado de Polícia Civil experiente e conduz a produção completa do relatório final de inquérito policial, em cinco fases: pré-processamento dos autos (extração de PDFs com OCR local, classificação, índice e cronologia via `scripts/pre_processador.py`), análise investigativa profunda (cronologia, matriz de confronto de provas e depoimentos, análise de vínculos, provas digitais e análise financeira quando o caso pedir), tipificação penal com análise jurídica (legalidade, anterioridade, lex mitior, abolitio criminis, concurso de crimes e prescrição), redação no template da unidade e entrega.

O ponto central são os **dois padrões reais de unidade**: IP iniciado com `392.4.` usa o template do **NEAMV** (crimes contra mulher e vulneráveis, com relato de diligências e depoimento verbatim da vítima); IP iniciado com `55.4.` usa o template da **Delegacia de Polícia** (crimes em geral, com seções de fatos, flagrante, oitivas, materialidade e conclusão). Cada template traz cabeçalho, fraseologia, estrutura de seções e checklist específico por tipo penal.

Antes da entrega, o rascunho passa obrigatoriamente pela skill `revisao-contradicoes` — um subagente independente que audita contradições internas, afirmações sem lastro nas provas, tipificação e excludentes, placeholders esquecidos e coerência da conclusão — e por um checklist final de forma, conteúdo e técnica. Há estratégia específica de processamento em lotes para autos de grande volume (500+ páginas).

## Quando usar

- "Redige/produz/elabora/finaliza o relatório do IP...";
- Casos de violência doméstica, descumprimento de medida protetiva, lesão corporal, ameaça, estupro de vulnerável, tráfico de drogas, armas e qualquer outro crime investigado pela Polícia Civil;
- Quando houver autos digitalizados (PDF) a analisar antes da redação.

Não use para: relatórios parciais ou de encaminhamento, ofícios e despachos (skill `despacho-plantao`), análise de RIF/COAF (skill `analise-rif`).

## Como usar

> "Redige o relatório final do IP 392.4.2026.12345, descumprimento de medida protetiva, com base nesses autos em PDF."

> "Finaliza esse inquérito de tráfico de drogas da Delegacia (IP 55.4.2026.678). Segue o APF, laudos e interrogatório."

> "Elabora o relatório final deste IP de estupro de vulnerável no padrão NEAMV, confrontando o depoimento da vítima com o interrogatório."

> "Produz o relatório deste IP de 600 páginas; processa os autos em lotes e me mostra o índice antes de redigir."

> "Quero o relatório final desse caso de lesão corporal, mas em arquivo Word para download."

## O que a skill entrega

- **Padrão: relatório completo formatado diretamente no chat** (Markdown espelhando o documento real: dados do IP, seções numeradas, depoimentos verbatim em itálico, data por extenso e assinatura) — sem necessidade de gerar arquivo;
- Arquivo **.docx** somente se solicitado ("quero em Word"), via skill `docx`, com A4, margens jurídicas, Arial 12, entrelinha 1,5 e cabeçalho/rodapé da unidade;
- Junto da entrega: pontos de atenção para revisão, registro do que a revisão independente apontou e sugestões de diligências complementares.

## Estrutura da pasta

| Item | Papel |
|---|---|
| `SKILL.md` | Instruções completas: fases, metodologia de confronto, tipificação, revisão obrigatória e checklists |
| `references/analise_financeira.md` | Metodologia de análise financeira (fluxos, compatibilidade patrimonial, COAF) |
| `references/analise_vinculos.md` | Metodologia de análise de vínculos (pessoas, empresas, contas, telefones) |
| `references/legislacao_penal.md` | Detalhamento dos princípios de tipificação e lei penal no tempo |
| `references/tipificacao_especial.md` | Tabela de tipos penais por área especializada |
| `scripts/pre_processador.py` | Classifica documentos extraídos, gera índice dos autos e rascunho de cronologia |
| `templates/modelo_neamv.md` | Template real do NEAMV (cabeçalho, seções, fraseologia, checklist) |
| `templates/modelo_delegacia.md` | Template real da Delegacia de Polícia |
| `templates/modelo_relatorio.md` | Modelo estrutural de relatório |

## Requisitos

- **Python 3** para `scripts/pre_processador.py`; **pandas** para ler CSVs de dados telefônicos/bancários;
- Extrator universal de documentos (Docling + EasyOCR em português, 100% local) instalado em `~/.claude/tools/` para PDFs escaneados — autos grandes não devem ser lidos direto no contexto;
- Entrada esperada: autos do IP (PDFs, termos, laudos), número do IP (para identificar a unidade), natureza do crime, nomes de vítima e suspeito e data do relatório;
- Skill `docx` apenas quando o usuário pedir arquivo Word.

## Avisos

- **A minuta exige revisão da Autoridade Policial**: a skill produz rascunho para conferência e assinatura humana, inclusive das citações literais (o OCR erra caracteres e não substitui a conferência contra o original).
- **Dados sigilosos dos autos não devem ser colados em ambientes não autorizados**; o processamento previsto na skill é local.
- Tratamento de dados pessoais de vítimas, testemunhas e investigados sujeito à **LGPD** (Lei 13.709/2018) e ao sigilo do inquérito.
- A skill segue as convenções da **Delegacia de Alta Floresta/MT e do NEAMV/Alta Floresta** (numeração de IP, cabeçalhos, fraseologia, assinatura); precisa de adaptação para uso em outras unidades.
