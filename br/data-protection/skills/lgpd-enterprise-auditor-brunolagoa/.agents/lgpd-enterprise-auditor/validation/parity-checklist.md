# Validação — checklist de paridade entre a skill e o framework modular

## Objetivo
Validar que o framework modular (`.agents/lgpd-enterprise-auditor/`) e a skill (`SKILL.md`) mantêm a mesma cobertura e consistência funcional.

## Checklist de validação
Última verificação completa: **2026-10-05**, item a item, contra `SKILL.md` e os módulos do framework. Ao alterar um item coberto aqui, desmarcar e reverificar antes de marcar de novo.

Parte da paridade é conferida por máquina em `scripts/tests/test-framework.sh` (CI): catálogo de itens da skill igual ao dos módulos, pesos das áreas, mapa de domínios, faixas de classificação, cenários e módulos entre router, matriz, README e comandos. Os itens abaixo continuam valendo para o que depende de leitura.

- [x] Todos os 17 domínios de auditoria estão mapeados em módulos do framework (`validation/traceability-matrix.md`).
- [x] Nenhum módulo redefine severidade fora do `core/severity-model.md`.
- [x] Nenhum módulo redefine score fora do `core/scoring-engine.md`.
- [x] Todos os achados usam contrato `finding`.
- [x] Todos os itens avaliados usam contrato `check_item`.
- [x] Relatório final segue `core/reporting-engine.md`.
- [x] Toda não conformidade possui evidência associada.
- [x] Evidência usa os dois eixos canônicos na skill e no framework: `evidence_type` (`ENCONTRADA | PARCIAL | AUSENTE`) e `evidence_source` (`TECNICA | DOCUMENTAL`).
- [x] Rótulos de classificação final seguem o padrão canônico na skill e no framework: `CRITICO | BAIXO_NIVEL | PARCIALMENTE_CONFORME | ALTA_CONFORMIDADE | EXCELENTE`.
- [x] Regra de área `NAO_APLICAVEL` e redistribuição proporcional de pesos idêntica na skill (`SKILL.md`) e no framework (`core/scoring-engine.md`): só com evidência de que o objeto não existe, nunca só porque o módulo ou o domínio ficou fora da auditoria.
- [x] Modo `full_audit` ativa todos os módulos.
- [x] Matriz de ativação por cenário está coerente com o router.
- [x] Bases legais distinguem art. 7º (dados pessoais) de art. 11 (sensíveis) na skill e no framework.
- [x] Definição de dado sensível idêntica ao art. 5º, II na skill e no framework (inclui filiação a sindicato ou a organização de caráter religioso, filosófico ou político).
- [x] Requisitos de consentimento (art. 8º) com checklist na skill e no framework (`legal/legal-bases-engine.md`).
- [x] Cookies e tracking com checklist atômico no framework (`appsec/owasp-api.md`), equivalente ao domínio 5 da skill.
- [x] Transparência e política de privacidade (art. 9º) cobertas na skill e no framework (`legal/rights-of-data-subject.md`).
- [x] Prazo de atendimento ao titular (art. 19: imediato em formato simplificado ou declaração completa em até 15 dias) presente na skill e no framework.
- [x] Registro das operações de tratamento (art. 37), com forma simplificada para pequeno porte (Res. CD/ANPD nº 2/2022), presente na skill e no framework (`governance/dpo-framework.md`).
- [x] Dados pessoais em logs de aplicação e de observabilidade cobertos no framework (`appsec/owasp-api.md` e `cloud/cloud-audit.md`), equivalente ao domínio 11 da skill.
- [x] IA/LLM com os mesmos itens na skill e no framework, inclusive envenenamento de dados (`IA-07`), vazamento de memória entre sessões (`IA-08`), dado pessoal na saída do modelo (`IA-09`) e permissões de agentes (`IA-10`); governança com política de segurança (`GV-16`) e treinamento (`GV-17`).
- [x] Dados de crianças/adolescentes (art. 14) cobertos na skill (`SKILL.md`) e no framework (`legal/children-adolescents.md`).
- [x] Transferência internacional (arts. 33-36) coberta na skill e no framework (`legal/international-transfer.md`).
- [x] Prazo de comunicação de incidente (Res. CD/ANPD nº 15/2024, 3 dias úteis) presente em governança e template de incidente.
- [x] Regulamento do encarregado (Res. CD/ANPD nº 18/2024 — ato escrito, datado e assinado; DPO pessoa jurídica; dispensa de indicação para pequeno porte) presente na skill (`SKILL.md`) e no framework (`governance/dpo-framework.md`).
- [x] Cláusulas-padrão contratuais (Res. CD/ANPD nº 19/2024) com prazo de adaptação encerrado em 23/08/2025 refletidas na skill, em `legal/international-transfer.md` e no `templates/dpa-template.md`.
- [x] Adequação da União Europeia (Res. CD/ANPD nº 32/2026) reconhecida na skill e no framework, com a ressalva de que dispensa apenas o mecanismo do art. 33.
- [x] ANPD denominada **Agência** Nacional de Proteção de Dados e submetida ao regime da Lei nº 13.848/2019 (Lei nº 15.352/2026, art. 55-A) na skill e no framework, preservando sua condição de autarquia de natureza especial e sem "corrigir" o termo legal *autoridade nacional*.
- [x] ECA Digital (Lei nº 15.211/2025, Decretos nº 12.622/2025 e nº 12.880/2026) coberto na skill (`SKILL.md`, domínio 16) e no framework (`legal/eca-digital.md` + manifesto `eca-digital`).
- [x] Relatório semestral de transparência do art. 31 (limiar de 1.000.000 de usuários dessa faixa etária com conexão no País; sete incisos; primeiro ciclo até 17/09/2026, prazo já encerrado) presente na skill, no módulo `eca-digital` e no `templates/eca-transparency-report-template.md`.
- [x] Vedação à autodeclaração de idade citada com a base correta na skill e no framework: expressa no art. 9º, §1º para conteúdo impróprio; nos demais casos, insuficiência perante os arts. 10, 12 e 14.
- [x] Os três cortes etários preservados sem unificação: criança até 12 anos incompletos (LGPD art. 14), vinculação de conta até 16 anos (ECA Digital art. 24) e conteúdo impróprio a menores de 18 anos (art. 9º).
- [x] Sanções do art. 35 descritas com a repartição de competência correta: advertência e multa pela ANPD; suspensão e proibição pelo Poder Judiciário.
- [x] Modulação e dispensa editorial do art. 39 consideradas antes de emitir achado, na skill e no framework.
- [x] Modo `full_audit` ativa também os módulos `eca-digital` e `plataformas-digitais`.
- [x] Deveres de plataformas digitais (Decreto nº 12.975/2026 — Decreto nº 8.771/2016, arts. 15-A, 16-A a 16-P, 19-A e 20-A — e Decreto nº 12.976/2026) cobertos na skill (`SKILL.md`, domínio 17) e no framework (`legal/plataformas-digitais.md` + manifesto `plataformas-digitais`).
- [x] Exclusões do art. 16-O, regime de ordem judicial para crimes contra a honra (art. 16-J) e regra de que conteúdo isolado não caracteriza falha sistêmica consideradas antes de emitir achado, na skill e no framework.
- [x] Prazos do Decreto nº 12.976/2026 preservados sem unificação: conteúdo íntimo em até 2 horas (art. 7º, §1º); prazos transitórios de 6 horas e 24 horas e 24 horas após contestação (art. 12).
- [x] Guarda de registros de acesso por 6 meses com porta lógica (MCI art. 15 e art. 15-A) presente na skill, em `cloud/cloud-audit.md` e em `legal/plataformas-digitais.md`.
- [x] Normas não vigentes (ex.: PL nº 2338/2023) aparecem apenas em seções "Em monitoramento" e nunca originam `NAO_CONFORME`.
- [x] Cálculo do score fechado e idêntico na skill e no framework (`core/scoring-engine.md`): valor por status (`CONFORME` 1, `PARCIAL` 0,5, `NAO_CONFORME` 0), peso por criticidade (4/3/2/1) e arredondamento do score global para o inteiro mais próximo, com 0,5 para cima.
- [x] Catálogo de itens idêntico na skill e no framework: IDs, texto, criticidade, agravante ou atenuante, tipo de controle e fundamento. O bloco de catálogo da `SKILL.md` é gerado das tabelas dos módulos por `scripts/update-skill-catalog.sh`.
- [x] Regras do catálogo iguais nas duas formas: todos os itens dos módulos ou domínios auditados são avaliados; a criticidade só muda pelo agravante da linha do item ou pela modulação por porte; problema sem item entra como item extra `EX-nn`.
- [x] Nove áreas de score com os mesmos pesos na skill e no framework (`bases_legais` 12, `seguranca` 20, `direitos_titular` 12, `governanca` 12, `infraestrutura` 8, `apis_integracoes` 8, `ai_llm` 8, `eca_digital` 10, `plataformas_digitais` 10); os domínios 16 e 17 pontuam em `eca_digital` e `plataformas_digitais`.
- [x] Teto de classificação por achado `CRITICO` (`PARCIALMENTE_CONFORME`) e marca de escopo direcionado, na skill e no framework (`core/scoring-engine.md`).
- [x] Mapa de áreas por domínio idêntico na skill e no framework; cada item pontua em uma única área e nenhum módulo escolhe área caso a caso.
- [x] Score técnico e score documental informativos, sem efeito na classificação, na skill e no framework.
- [x] Modulação de severidade por porte (Res. CD/ANPD nº 2/2022) com as mesmas condições e vedações na skill e no framework (`core/severity-model.md`).
- [x] Registro de risco aceito, sem efeito em status, severidade ou score, na skill e no framework (`core/auditor-core.md`).
- [x] Leitura da documentação do projeto antes de perguntar e natureza do agente de tratamento como entrada inicial, na skill (fase 1 e modo de operação), em `orchestrator/router.md` e em todos os `commands/*.md`.
- [x] Dados de acesso público e manifestamente públicos (art. 7º, §§ 3º, 4º e 7º), inclusive dado sensível divulgado por órgão oficial, na skill e no framework (`legal/legal-bases-engine.md`).
- [x] Cloud cobre IaaS, PaaS e hospedagem compartilhada, com validação das respostas de produção, na skill (domínio 7) e no framework (`cloud/cloud-audit.md`).
- [x] Itens `PARCIAL` também geram achado, com severidade um nível abaixo da criticidade do item; contagem única (o item pontua pelo que resta do seu requisito, fica `NAO_APLICAVEL` quando depende de controle inexistente e é reprovado quando o requisito inteiro falha); precedência da regra de severidade mais específica — na skill e no framework.
- [x] Régua única de status (`CONFORME`, `PARCIAL`, `NAO_CONFORME`), aplicada em ordem, com a regra da metade dos elementos, a do vestígio e a do documento em rascunho, na skill e no framework (`core/evidence-engine.md`).
- [x] Fronteiras entre itens sobrepostos (`BL-01`/`BL-02`/`OP-02`, `CK-02`/`CK-03`/`CK-08`, `SE-02`/`IN-01`, `IN-06`/`IN-12`), lista fechada de dependências da contagem única (gerada para a skill junto com o catálogo) e prazo máximo do achado pela severidade, na skill e no framework.
- [x] Item com elementos verificáveis e elementos fora do alcance: falha verificável reprova; com todos os verificáveis atendidos, `NAO_VERIFICADO`, e nunca `CONFORME` — na skill e no framework (`core/scoring-engine.md`).
- [x] Critério de decisão do tratamento de alto risco (critério específico e critério geral, com decisão conservadora na dúvida) e definição de exposição explorável confirmada, na skill e no framework (`core/severity-model.md`).
- [x] Dado que revela informação sensível (art. 11, §1º) tratado como sensível em todos os itens, e agravante limitado ao objeto do item, na skill e no framework (`core/scoring-engine.md`).
- [x] Aplicabilidade pelos fatos do tratamento, não pela documentação (inclusive nos itens de consentimento), e limite entre `NAO_VERIFICADO` e `NAO_CONFORME` para controles de repositório e de painel, na skill e no framework.
- [x] Transferência internacional distingue mecanismo comprovadamente ausente (`CRITICO`) de não evidenciado (`ALTO`), e dispensa de encarregado e registro simplificado não valem para pequeno porte com tratamento de alto risco — na skill e no framework.
- [x] Aplicabilidade por item (`APLICAVEL | NAO_APLICAVEL | NAO_VERIFICADO`), com os mesmos limites, cobertura e marca de score parcial abaixo de 80%, na skill e no framework (`core/scoring-engine.md`).
- [x] Mais de uma evidência por item, origem `TECNICA + DOCUMENTAL` e confiança `ALTA | MEDIA | BAIXA` sem efeito no score, na skill e no framework (`core/evidence-engine.md`).
- [x] Papel do auditado por fluxo (controlador ou operador), com as obrigações do operador (art. 39) e o que fica `NAO_APLICAVEL` para ele, na skill e no framework (`legal/legal-bases-engine.md`).
- [x] Gatilho do ECA Digital: bloqueio por idade autodeclarada não afasta a auditoria quando há outro indício de acesso por menores, na skill (domínio 16) e em `orchestrator/router.md`.
- [x] Relatório com marcação de confidencialidade, "o que fazer agora", coluna `Área`, esforço `P | M | G`, riscos aceitos, glossário e aviso legal fixo, na skill e no framework (`core/reporting-engine.md` e `reports/*.md`).
- [x] Formato de saída perguntado sempre no início (`.md`, `.md` e `.html`, ou só `.html`), com `.md` quando não há resposta e só o resumo em tela quando há arquivo gravado; o `.html` é gerado pelo modelo `reports/html-report-template.html`, preenchendo só o bloco de dados (`reports/html-report.md`), na skill ("Arquivos do relatório") e no framework (`core/reporting-engine.md`).

## Evidências de teste esperadas
- execução de cenário `saas_web`;
- execução de cenário `web_site`;
- execução de cenário `mobile_app`;
- execução de cenário `ai_llm_system`;
- execução de cenário `devsecops_pipeline`;
- execução de cenário `eca_digital_platform`;
- execução de cenário `digital_platform`;
- execução `full_audit`.
