---
name: lgpd-plataformas-digitais
description: Executa auditoria LGPD + deveres de plataformas digitais (Decretos nº 12.975/2026 e nº 12.976/2026, regulamentação do Marco Civil da Internet) para provedores de aplicações com conteúdo de terceiros.
license: MIT
metadata:
  author: BrunoCastro
  version: "1.8.1"
---

# LGPD + Plataformas Digitais (conteúdo de terceiros)

Antes de perguntar, leia o que o projeto já documenta (`CLAUDE.md`, `AGENTS.md`, `README*`, `docs/`, manifestos de dependências e de infraestrutura) e apresente o contexto inferido. Pergunte apenas o que faltar ou não puder ser confirmado:
- natureza do agente de tratamento: pessoa natural ou jurídica, com ou sem fins econômicos, porte (agente de pequeno porte, Res. CD/ANPD nº 2/2022) e se há tratamento de alto risco;
- papel do auditado em cada fluxo de dados: controlador, operador ou ambos;
- tipo de serviço (rede social, plataforma de vídeo, fórum, marketplace, comentários públicos, mensageria com grupos abertos, IA generativa de imagem/voz);
- se há intermediação de conteúdo gerado por terceiros com difusão pública;
- canal de denúncia, fluxo de notificação, remoção e contestação, com métricas de prazo;
- políticas de moderação, gestão de riscos sistêmicos e detecção de redes artificiais;
- ferramentas de anúncio ou impulsionamento pago e política de aceite de anúncios;
- guarda de registros de acesso (IP, porta lógica, data/hora) e política de expurgo;
- sede e representante legal no Brasil;
- termos de uso e relatório anual de transparência;
- funcionalidades de IA capazes de gerar ou alterar imagem ou som de pessoas.

Pergunte sempre, na mesma rodada, em qual formato gravar o relatório, salvo se o pedido já disser: `.md`, `.md` e `.html` (resultado completo, com custo maior) ou só `.html` (versão visual, para abrir no navegador).

Ative o cenário `digital_platform`:
- `core`, `legal`, `plataformas-digitais`, `governance`, `appsec`, `cloud`.

Adicione `ai-llm` se houver IA generativa ou moderação automatizada, e `eca-digital` se o serviço for direcionado ou provavelmente acessado por menores de 18 anos (gatilhos do router).

Regras obrigatórias:
- considerar `.agents/lgpd-enterprise-auditor/` como caminho base canônico em qualquer projeto;
- seguir `.agents/lgpd-enterprise-auditor/orchestrator/router.md`;
- ler só os arquivos listados em `files` nos manifestos dos módulos ativos (`.agents/lgpd-enterprise-auditor/orchestrator/manifests/`) e avaliar todos os itens do catálogo desses módulos, cada um com o seu ID;
- aplicar `.agents/lgpd-enterprise-auditor/legal/plataformas-digitais.md`;
- verificar as exclusões do art. 16-O (e-mail, mensageria interpessoal, videoconferência restrita) e o regime de ordem judicial para crimes contra a honra (art. 16-J) antes de emitir achado;
- nunca tratar conteúdo ilícito isolado como falha sistêmica: o achado aponta processos ausentes ou insuficientes (art. 16-B, §3º);
- não unificar os prazos: conteúdo íntimo em até 2 horas (Decreto nº 12.976/2026, art. 7º, §1º); prazos transitórios de 6 horas e 24 horas e 24 horas após contestação (art. 12);
- fundamentar cada achado no dispositivo do decreto (e do Marco Civil, quando houver) e no correlato da LGPD;
- registrar exposição cumulativa: sanções do art. 12 do Marco Civil e do art. 52 da LGPD (e do art. 35 do ECA Digital, havendo menores);
- exigir evidência por requisito;
- produzir relatório conforme `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`;
- gravar o relatório no formato escolhido (`.md`, `.md` e `.html`, ou só `.html`), conforme a seção "Arquivos gerados" de `.agents/lgpd-enterprise-auditor/core/reporting-engine.md`.
