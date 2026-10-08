# Módulo IA/LLM — governança e privacidade em inteligência artificial

## Escopo
Auditar uso de IA/LLM com foco em privacidade, segurança e conformidade regulatória.

## Checklist atômico
Perguntas de enquadramento (não pontuam):
- A funcionalidade de IA pode gerar ou alterar imagem ou som de pessoas? Se sim, ativar [[plataformas-digitais]]: as salvaguardas contra conteúdo íntimo de terceiro (Decreto nº 12.976/2026, arts. 9º e 10) são avaliadas lá (`PD-15`).
- Menores estão expostos a recomendação algorítmica ou perfilamento? Se sim, ativar [[eca-digital]].
- Dados biométricos ou neurodados alimentam o modelo? Se sim, aplicar o regime de dado sensível (art. 11) em `BL-01`.

Avaliados em outros módulos, sem item próprio aqui: transferência internacional ao provedor do modelo (itens `TI`, `legal/international-transfer.md`) e revisão de decisão automatizada (`DT-08`, `legal/rights-of-data-subject.md`).

Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `IA-01` | Os prompts e os dados enviados ao modelo são minimizados e anonimizados ou mascarados, sem dado pessoal além do necessário? | 12 | `ALTO` | `CRITICO` com dado sensível enviado a LLM externo sem proteção ou base legal | `TECNICO` | arts. 6º, III, 11 e 46 |
| `IA-02` | Há política de retenção para prompts, respostas, logs e embeddings, aplicada no sistema e no provedor? | 12 | `ALTO` | — | `TECNICO` | arts. 15 e 16 |
| `IA-03` | Há defesa contra prompt injection e vazamento de contexto (separação de instruções e dados, filtros de entrada e de saída, testes)? | 12 | `ALTO` | — | `TECNICO` | art. 46 |
| `IA-04` | O uso de dados pessoais para treino ou fine-tuning tem base legal e, quando necessário, consentimento? | 12 | `ALTO` | — | `DOCUMENTAL` | arts. 6º, I, 7º e 11 |
| `IA-05` | A memória vetorial ou o RAG entrega só os dados que a finalidade e a permissão de quem consulta autorizam? | 12 | `ALTO` | — | `TECNICO` | arts. 6º, I e 46 |
| `IA-06` | A geração ou manipulação sintética de imagem ou voz de pessoas (deepfake) tem base legal e autorização do retratado? | 12 | `ALTO` | — | `DOCUMENTAL` | arts. 7º e 11 |
| `IA-07` | Os dados e documentos que alimentam treino, fine-tuning ou RAG têm origem controlada e validação contra envenenamento (data poisoning)? | 12 | `MEDIO` | — | `TECNICO` | arts. 6º, V e 46 |
| `IA-08` | A memória de conversa e o contexto são isolados por usuário e por cliente, sem vazamento entre sessões (memory leakage)? | 12 | `ALTO` | — | `TECNICO` | art. 46 |
| `IA-09` | A saída do modelo é verificada para não expor dado pessoal de terceiros nem afirmar fato inexato sobre pessoa identificável? | 12 | `MEDIO` | — | `TECNICO` | arts. 6º, V e 46 |
| `IA-10` | Agentes e ferramentas acionados pelo modelo têm permissões mínimas, com confirmação humana para ações sobre dados pessoais? | 12 | `ALTO` | — | `TECNICO` | arts. 6º, VIII e 46 |
| `IA-11` | O contrato e a configuração do provedor de LLM vedam o uso dos dados para treino do provedor e limitam a retenção? | 12 | `ALTO` | — | `DOCUMENTAL` | arts. 6º, I e 39 |
| `IA-12` | O titular é informado de que interage com IA ou de que seus dados são tratados por IA? | 12 | `MEDIO` | — | `DOCUMENTAL` | arts. 6º, VI e 9º |
| `IA-13` | Existe política de uso de IA (casos permitidos, dados vedados, responsáveis e revisão)? | 12 | `MEDIO` | — | `DOCUMENTAL` | art. 50 |

## Referências técnicas da ANPD
Não vinculantes, mas úteis como parâmetro de boa prática e como evidência documental:
- Radar Tecnológico nº 3 — IA generativa;
- Radar Tecnológico nº 4 — Neurotecnologias;
- Radar Tecnológico nº 6 — Deepfakes;
- Notas técnicas de fiscalização sobre sistemas de IA (ex.: NT nº 1/2026 — Grok; atuações sobre IA generativa da Meta e uso de dados de menores).
Ver [[anpd-guidelines]] para a lista completa e para os temas prioritários de fiscalização 2026-2027.

## Critérios de evidência
- política de uso de IA e governança;
- configuração de retenção no provedor de LLM;
- evidência de anonimização/redação;
- documentação de fluxo internacional de dados;
- controles de segurança para RAG/vector database;
- contrato e painel do provedor de LLM (uso para treino, retenção);
- permissões das ferramentas expostas a agentes e registros de confirmação humana;
- testes de prompt injection e de isolamento entre sessões.

## Mapeamento para severidade e score
- Dado sensível enviado a LLM externo sem proteção/base legal: `CRITICO`.
- Geração ou modificação de conteúdo íntimo de terceiro por IA (Decreto nº 12.976/2026, art. 9º): `CRITICO` — detalhado em [[plataformas-digitais]].
- Retenção inadequada de prompts e embeddings: `ALTO`.
- Ausência parcial de política de IA: `MEDIO`.
- Contexto ou memória vazando entre usuários ou clientes: `ALTO`.
- Agente com permissão excessiva sobre dados pessoais, sem confirmação humana: `ALTO`.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `ai_llm` (domínio 12) para todos os itens deste módulo. A criticidade de cada item está na tabela do checklist.

## Em monitoramento (não vigente — não gera não conformidade)
- **PL nº 2338/2023 — Marco Legal da IA**: aprovado no Senado em 10/12/2024, em tramitação na Câmara dos Deputados, sem sanção até 2026-09 (em set/2026, aguardando parecer do relator na Comissão Especial). Prevê classificação por nível de risco, direitos de transparência/explicação/contestação, governança de IA e sanções próprias.
- Enquanto não sancionado, mapear os controles correspondentes apenas como `recomendacoes_tecnicas` no relatório, rotulados como preparação para norma futura. Nunca gerar `finding` com fundamento no PL.
- **Rotulagem de conteúdo sintético** (identificação de imagem, voz ou vídeo gerados por IA): sem dever geral na base normativa vigente deste módulo; registrar apenas como `recomendacoes_tecnicas`.
