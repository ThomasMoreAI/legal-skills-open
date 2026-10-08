---
name: lgpd-eca-digital
description: Executa auditoria direcionada de LGPD + ECA Digital (Lei nº 15.211/2025) para plataformas acessadas por crianças e adolescentes.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.8.1"
---

# LGPD + ECA Digital (público infantojuvenil)

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- tipo de produto (rede social, plataforma de vídeo, jogo, mensageria, marketplace, app educacional);
- público-alvo declarado e público real (há usuários menores de 18 anos?);
- volume de usuários registrados menores de 18 anos (limiar de 1 milhão define o relatório de transparência);
- fluxo de cadastro e mecanismo de aferição de idade em uso;
- existência de vinculação de conta de menor a responsável e de ferramentas de supervisão parental;
- configurações padrão de privacidade para perfis de menores;
- regras de publicidade, perfilamento e recomendação algorítmica;
- mecânicas de jogo, itens virtuais pagos e caixas de recompensa (loot boxes);
- fluxo de denúncia, moderação e remoção de conteúdo, com política de retenção;
- país de origem do provedor e existência de representante legal no Brasil.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `eca_digital_platform`:
- `core`, `legal`, `eca-digital`, `governance`, `appsec`, `mobile`.

Adicione `ai-llm` se houver recomendação algorítmica, moderação automatizada ou IA generativa.

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- aplicar `.agents/lgpd-enterprise-auditor/legal/eca-digital.md` junto de `.agents/lgpd-enterprise-auditor/legal/children-adolescents.md`;
- usar `.agents/lgpd-enterprise-auditor/templates/age-assurance-checklist.md` para a aferição de idade;
- usar `.agents/lgpd-enterprise-auditor/templates/eca-transparency-report-template.md` quando o provedor superar 1 milhão de usuários menores;
- tratar autodeclaração simples de idade como NAO_CONFORME (vedação expressa do art. 9º, §1º para conteúdo impróprio; insuficiência perante os arts. 10, 12 e 14 nos demais casos);
- verificar a modulação e a dispensa editorial do art. 39 antes de emitir achado;
- não unificar os cortes etários: criança até 12 anos incompletos (LGPD art. 14), vinculação de conta até 16 anos (art. 24) e conteúdo impróprio a menores de 18 anos (art. 9º);
- fundamentar cada achado no dispositivo do ECA Digital e no correlato da LGPD (art. 14 e/ou art. 6º);
- registrar exposição cumulativa: sanções do art. 35 da Lei nº 15.211/2025 e do art. 52 da LGPD;
- exigir evidência por requisito;
- produzir relatório conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
