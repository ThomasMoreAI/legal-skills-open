# Relatório de validação da skill

Data: 2026-07-03

Versão revisada: 1.4.0

## Resultado

A skill foi revisada para maior precisão jurídica, melhor uso por agentes, melhor aderência ao padrão reutilizável de skills, maior robustez em produtos digitais e total alinhamento com a estrutura oficial de customizações do Gemini/Antigravity.

## Principais correções

1. Escopo ampliado para produtos digitais, aplicativos, SaaS, marketplaces, assinaturas e comunicações ao consumidor.
2. Separação explícita entre CDC, LGPD, Marco Civil e regulação setorial.
3. Linguagem jurídica ajustada para evitar conclusões categóricas.
4. Cautelas reforçadas sobre dano moral, inversão do ônus da prova, repetição em dobro, fraude, crime e prazos.
5. Matriz de temas expandida para termos de uso, política de privacidade, checkout, comunicados e assinatura digital.
6. Checklists adicionados para produtos digitais, comunicados e cancelamento de assinaturas digitais.
7. Templates ajustados para reduzir exposição de dados pessoais e separar base consumerista de LGPD.
8. Casos de teste expandidos para produto digital, marketplace e política de privacidade.
9. `SKILL.md` reduzido para frontmatter padrão e instruções operacionais, com referências carregáveis sob demanda.
10. Adicionado `references/pesquisa-e-atualizacao.md` para protocolo de vigência, citação e navegação.
11. Adicionado `agents/openai.yaml` com metadados de interface.
12. Fontes oficiais atualizadas com Lei nº 13.543/2017, Lei nº 13.455/2017, página direta da Lei nº 9.099/1995 no Planalto e cautela sobre Súmula 675/STJ.
13. Adicionada camada de Marco Civil com `references/marco-civil-internet.md` e `references/checklists/marco-civil-plataformas.md`.
14. Incluídas fontes oficiais do Marco Civil, Decreto nº 8.771/2016, Decreto nº 12.975/2026, Lei nº 15.211/2025 e Decreto nº 12.880/2026.
15. Registrada cautela de vigência: em 2026-07-03, o Decreto nº 12.975/2026 ainda estava em vacatio legis, com entrada em vigor prevista para 2026-07-20, salvo conferência oficial posterior.
16. Adicionada camada LGPD com `references/lgpd-protecao-dados.md` e `references/checklists/lgpd-produtos-digitais.md`.
17. Incluídas fontes oficiais da LGPD compilada, Lei nº 15.352/2026, ANPD, comunicação de incidente, RIPD e regulamentações ANPD.
18. Matriz expandida para bases legais, dados sensíveis, direitos do titular, encarregado, incidentes, transferência internacional, agentes de pequeno porte e sanções.
19. Reestruturação da skill para conformidade com a especificação agentskills.io e padrão do Gemini/Antigravity: diretórios `references/` (antiga `docs/`), `assets/` (antiga `templates/`) e `evals/` (contendo os casos de teste em markdown), com conversão de referências para links Markdown clicáveis.

## Fontes oficiais conferidas

- Lei nº 8.078/1990, Código de Defesa do Consumidor, Planalto.
- Decreto nº 7.962/2013, comércio eletrônico, Planalto.
- Decreto nº 11.034/2022, SAC, Planalto.
- Decreto nº 2.181/1997, SNDC, Planalto.
- Lei nº 10.962/2004 e Decreto nº 5.903/2006, preços, Planalto.
- Lei nº 14.181/2021, superendividamento, Planalto.
- Decreto nº 11.150/2022 e Decreto nº 11.567/2023, mínimo existencial, Planalto.
- Lei nº 12.965/2014, Marco Civil da Internet, Planalto.
- Lei nº 13.709/2018, LGPD compilada, Planalto.
- Lei nº 15.352/2026, alteração da LGPD e ANPD, Planalto.
- Decreto nº 8.771/2016, regulamentação do Marco Civil, Planalto.
- Decreto nº 12.975/2026, alteração do Decreto nº 8.771/2016, Planalto.
- Lei nº 15.211/2025 e Decreto nº 12.880/2026, proteção de crianças e adolescentes em ambientes digitais, Planalto.
- ANPD: regulamentações, comunicação de incidente, RIPD, dosimetria, encarregado, transferência internacional e agentes de pequeno porte.
- Consumidor.gov.br e Senacon/MJSP.
- STJ para súmulas e jurisprudência qualificada.

## Limitações

- A revisão não substitui advogado.
- A legislação e a jurisprudência devem ser conferidas novamente antes de publicação ou uso em caso concreto relevante.
- Políticas de privacidade exigem revisão específica de LGPD.
- Setores regulados exigem consulta à regulação própria.
