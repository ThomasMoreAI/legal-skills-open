# Módulo Governança — encarregado, registro das operações e accountability

## Escopo
Avaliar governança de privacidade, accountability e controles organizacionais.

## Regulamento do Encarregado (Res. CD/ANPD nº 18/2024)
- A indicação do encarregado deve ser formalizada por **ato escrito, datado e assinado** pelo agente de tratamento.
- O encarregado pode ser **pessoa natural ou pessoa jurídica** (permitindo DPO as a service).
- Devem estar assegurados autonomia técnica, acesso à alta direção e ausência de conflito de interesses.
- **Agentes de tratamento de pequeno porte** (Res. CD/ANPD nº 2/2022) estão dispensados da **indicação formal**, mas não das obrigações de canal de comunicação com titulares e ANPD. A dispensa não vale para quem se enquadra nas exclusões da resolução, como o tratamento de alto risco (art. 3º).
- A identidade e o contato devem ser divulgados de forma clara, objetiva e de fácil acesso, preferencialmente no site.

## Registro das operações de tratamento (art. 37)
- Controlador e operador devem manter registro das operações de tratamento que realizarem (art. 37). É a base do mapeamento de dados.
- Conteúdo mínimo esperado: inventário e classificação dos dados (comum, sensível, de criança/adolescente), finalidade, base legal (art. 7º ou 11), categorias de titulares, compartilhamentos e transferências internacionais, retenção/descarte e medidas de segurança.
- Agentes de tratamento de pequeno porte podem cumprir a obrigação de forma **simplificada** (Res. CD/ANPD nº 2/2022), mas não estão dispensados dela; a forma simplificada também não vale nas exclusões da resolução, como o tratamento de alto risco (art. 3º).

## Retenção e eliminação (arts. 15 e 16)
- O tratamento termina quando a finalidade é alcançada ou os dados deixam de ser necessários, ao fim do período de tratamento, por comunicação do titular (inclusive revogação) ou por determinação da ANPD (art. 15).
- Terminado o tratamento, os dados devem ser eliminados; a conservação só é autorizada para cumprimento de obrigação legal ou regulatória, estudo por órgão de pesquisa (anonimizados sempre que possível), transferência a terceiro respeitados os requisitos de tratamento, ou uso exclusivo do controlador com dados anonimizados e vedado o acesso por terceiro (art. 16).

## Checklist atômico
Itens do catálogo (regras em `core/scoring-engine.md`, "Catálogo de itens"): avaliar todos, cada um com sua `applicability`. `GV-06` e `GV-07` só se aplicam a provedor de aplicações de internet; `GV-02` e `GV-11` nunca valem juntos: agente de pequeno porte dispensado de indicar encarregado (Res. CD/ANPD nº 2/2022, sem tratamento de alto risco) tem `GV-02` `NAO_APLICAVEL` e é avaliado por `GV-11`; nos demais casos vale `GV-02`, e `GV-11` fica `NAO_APLICAVEL`. Quando o auditado é só operador, `GV-03` e `GV-08` ficam `NAO_APLICAVEL` nos fluxos em que ele não é controlador.

| ID | Item | Domínio | Criticidade | Agravante ou atenuante | Controle | Fundamento |
|---|---|---|---|---|---|---|
| `GV-01` | Existe registro das operações de tratamento atualizado, com inventário e classificação de dados, ciclo de vida, compartilhamentos e retenção, sem dados órfãos (sem finalidade ou responsável)? Agente de pequeno porte pode usar a forma simplificada. | 1 | `MEDIO` | `ALTO` com dado sensível ou de crianças e adolescentes | `DOCUMENTAL` | art. 37; Res. CD/ANPD nº 2/2022 |
| `GV-02` | Existe encarregado indicado por ato escrito, datado e assinado? | 13 | `ALTO` | `MEDIO` se o encarregado já exerce a função e só falta o ato formal | `DOCUMENTAL` | art. 41; Res. CD/ANPD nº 18/2024 |
| `GV-03` | Existe RIPD para as operações de maior risco? | 13 | `MEDIO` | `ALTO` em tratamento de alto risco (critérios da Res. CD/ANPD nº 2/2022) | `DOCUMENTAL` | arts. 5º, XVII e 38 |
| `GV-04` | Existe política de retenção aprovada e aplicada, com prazo por categoria de dado e a hipótese do art. 16 que justifica cada conservação? | 15 | `MEDIO` | — | `DOCUMENTAL` | arts. 15 e 16 |
| `GV-05` | A identidade e o contato do encarregado são divulgados publicamente, de forma clara e objetiva, preferencialmente no site? | 13 | `MEDIO` | — | `DOCUMENTAL` | art. 41, §1º |
| `GV-06` | Provedor de aplicações: há canal de denúncia permanente e de fácil acesso, que preveja a notificação de conteúdos criminosos ou ilícitos? | 13 | `ALTO` | — | `TECNICO` | Decreto nº 8.771/2016, art. 16-A, II; LGPD art. 6º, VIII |
| `GV-07` | Provedor de aplicações: há sede e representante legal pessoa jurídica no País, com contato acessível no site? | 13 | `MEDIO` | — | `DOCUMENTAL` | Decreto nº 8.771/2016, art. 16-A, I; LGPD art. 6º, X |
| `GV-08` | Existe processo de resposta a incidentes com responsáveis definidos e comunicação à ANPD e aos titulares em até 3 dias úteis? | 13 | `ALTO` | — | `DOCUMENTAL` | art. 48; Res. CD/ANPD nº 15/2024 |
| `GV-09` | Operadores e suboperadores, inclusive o provedor de hospedagem, têm contrato com cláusulas de proteção de dados (DPA)? | 14 | `MEDIO` | `ALTO` se o operador tratar dados sensíveis ou de crianças e adolescentes | `DOCUMENTAL` | art. 39 |
| `GV-10` | O encarregado tem autonomia técnica, acesso à alta direção e ausência de conflito de interesses? | 13 | `MEDIO` | — | `DOCUMENTAL` | Res. CD/ANPD nº 18/2024 |
| `GV-11` | Agente de pequeno porte sem encarregado indicado: existe canal de comunicação com titulares e com a ANPD, divulgado? | 13 | `MEDIO` | — | `DOCUMENTAL` | art. 41; Res. CD/ANPD nº 2/2022 |
| `GV-12` | A eliminação ou anonimização ao fim do prazo é automática e alcança réplicas, backups e operadores? | 15 | `MEDIO` | — | `TECNICO` | art. 16 |
| `GV-13` | O descarte de dados e mídias é seguro e registrado? | 15 | `MEDIO` | — | `TECNICO` | arts. 16 e 46 |
| `GV-14` | As retenções legais (ex.: fiscais, trabalhistas, registros de acesso do MCI art. 15) estão identificadas e limitadas ao prazo legal? | 15 | `MEDIO` | — | `DOCUMENTAL` | art. 16, I |
| `GV-15` | Existe trilha de auditoria e evidência documental contínua das decisões de privacidade (versões de políticas, atas, revisões)? | 13 | `MEDIO` | — | `DOCUMENTAL` | arts. 6º, X e 50 |
| `GV-16` | Existe política de segurança da informação aprovada e conhecida por quem trata dados pessoais? | 13 | `MEDIO` | — | `DOCUMENTAL` | arts. 46 e 50 |
| `GV-17` | Há treinamento periódico de quem trata dados pessoais, com registro de participação? | 13 | `BAIXO` | — | `DOCUMENTAL` | arts. 41, §2º, III e 50 |

Dependências (contagem única de `core/scoring-engine.md`): com o segundo item `NAO_CONFORME`, o primeiro fica `NAO_APLICAVEL`.
- `GV-05` depende de `GV-02`: não há contato de encarregado a divulgar sem encarregado indicado.
- `GV-10` depende de `GV-02`: não há autonomia de encarregado a avaliar sem encarregado indicado.
- `GV-13` depende de `GV-12`: não há descarte a registrar enquanto nada é eliminado.

Modelos de apoio: [[ropa-template]] (registro das operações), [[dpo-appointment-template]] (ato de indicação do encarregado), [[ripd-template]], [[retention-policy-template]], [[dpa-template]] e [[incident-response-template]].

## Critérios de evidência
- registro das operações de tratamento versionado;
- política de retenção e evidência de execução da eliminação (jobs de expurgo, logs de descarte);
- nomeação formal do DPO;
- RIPD(s) atualizados;
- políticas versionadas;
- runbook de incidentes;
- contratos/DPA com operadores e subprocessadores.

## Mapeamento para severidade e score
- Ausência de encarregado (quando exigível) ou de RIPD em tratamento de alto risco (critérios da Res. CD/ANPD nº 2/2022): `ALTO`; demais falhas de encarregado ou RIPD: `MEDIO`.
- Posição do framework sobre o RIPD: embora o art. 38 o torne exigível quando a ANPD o solicita, a ausência em tratamento de alto risco é `ALTO`, porque o relatório precisa estar pronto para ser apresentado e é a principal evidência de gestão de risco.
- Ausência de processo de resposta a incidentes que permita comunicar ANPD e titulares em 3 dias úteis: `ALTO`.
- Quando o auditado é o operador, o contrato com o controlador e as demais obrigações do art. 39 seguem `legal/legal-bases-engine.md` (seção "Papel do auditado").
- Operador sem contrato com cláusulas de proteção de dados (DPA), inclusive o provedor de hospedagem: `MEDIO`; `ALTO` se o operador tratar dados sensíveis ou de crianças e adolescentes.
- Provedor de aplicações sem os deveres gerais do art. 16-A: sem canal de denúncia permanente, `ALTO` (`GV-06`); sem representante legal pessoa jurídica no País, `MEDIO` (`GV-07`). Esses dois deveres são avaliados só aqui, com o módulo `plataformas-digitais` ativo ou não.
- Ausência de registro das operações de tratamento (art. 37): `MEDIO`; `ALTO` quando houver tratamento de dados sensíveis ou de crianças e adolescentes.
- Encarregado exercendo a função sem ato formal de indicação: `MEDIO`.
- Retenção sem prazo definido ou sem fundamento no art. 16 (retenção obscura): `MEDIO`.
- Falhas documentais de baixa materialidade: `BAIXO` ou `MEDIO`.
- A criticidade de cada item está na tabela do checklist; as regras acima explicam os agravantes e atenuantes.
- Área de score (mapa por domínio de `core/scoring-engine.md`): `governanca` (domínios 1, 13, 14 e 15) para todos os itens deste módulo.

## Relação com outros módulos
- Regulamentos da ANPD aplicáveis: ver [[anpd-guidelines]].
- Obrigações de transparência para público infantojuvenil: ver [[eca-digital]].
- Deveres de provedores de aplicações de internet (representante legal, canal de denúncia, relatório anual de transparência): ver [[plataformas-digitais]].
