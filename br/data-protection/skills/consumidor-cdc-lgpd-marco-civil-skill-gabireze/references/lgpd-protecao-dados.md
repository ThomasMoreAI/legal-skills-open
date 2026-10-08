# LGPD e protecao de dados

Use este guia quando o caso envolver dados pessoais, politica de privacidade, cookies, cadastro, conta online, analytics, marketing, compartilhamento, operadores, transferencia internacional, direitos do titular, encarregado, incidentes de seguranca, criancas/adolescentes ou revisao de produto digital com tratamento de dados.

**Ultima conferencia web:** 2026-07-03.

## Fontes oficiais

- Lei nº 13.709/2018, LGPD, texto compilado:  
  https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13709compilado.htm
- Lei nº 15.352/2026, altera a LGPD e trata da ANPD:  
  https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/lei/L15352.htm
- Portal da ANPD:  
  https://www.gov.br/anpd/pt-br
- Regulamentacoes da ANPD:  
  https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd
- Comunicacao de Incidente de Seguranca (CIS):  
  https://www.gov.br/anpd/pt-br/assuntos/comunicacao-de-incidentes-de-seguranca-cis
- Relatorio de Impacto a Protecao de Dados Pessoais (RIPD):  
  https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/relatorio-de-impacto-a-protecao-de-dados-pessoais-ripd

## Normas e materiais ANPD relevantes

- Resolução CD/ANPD nº 1/2021: processo de fiscalizacao e processo administrativo sancionador.
- Resolução CD/ANPD nº 2/2022: aplicacao da LGPD para agentes de tratamento de pequeno porte.
- Resolução CD/ANPD nº 4/2023: dosimetria e aplicacao de sancoes administrativas.
- Resolução CD/ANPD nº 15/2024: regulamento de comunicacao de incidente de seguranca.
- Resolução CD/ANPD nº 18/2024: atuacao do encarregado pelo tratamento de dados pessoais.
- Resolução CD/ANPD nº 19/2024: transferencia internacional de dados, incluindo clausulas-padrao e outros mecanismos.

Sempre confira a pagina de regulamentacoes da ANPD antes de citar numero, vigencia, prazo ou procedimento.

## Separacao de bases

| Camada | Use para | Nao use para |
|---|---|---|
| LGPD | tratamento de dados pessoais por pessoa natural ou juridica, inclusive nos meios digitais | resolver sozinha relacao de consumo, conteudo de terceiro ou crime |
| CDC | transparencia na oferta, relacao B2C, publicidade, atendimento, cancelamento, cobranca e clausulas abusivas | definir base legal de tratamento de dados |
| Marco Civil | provedores, registros, IP, guarda de logs, neutralidade, responsabilidade por conteudo de terceiros | substituir analise de base legal LGPD |
| ANPD | regulacao, fiscalizacao, incidentes, guias, sancoes, transferencia internacional, encarregado | atuar como advogado do titular ou do controlador |
| ECA/Lei 15.211 | criancas e adolescentes em ambiente digital | caso adulto comum sem risco infantojuvenil |

## Conceitos essenciais

- **Dado pessoal:** informacao relacionada a pessoa natural identificada ou identificavel.
- **Dado sensivel:** origem racial ou etnica, conviccao religiosa, opiniao politica, filiacao a sindicato ou organizacao religiosa/filosofica/politica, dado referente a saude ou vida sexual, dado genetico ou biometrico quando vinculado a pessoa natural.
- **Dado anonimizado:** dado que nao permite identificacao do titular considerando meios tecnicos razoaveis. Hash, token ou ID interno geralmente nao bastam.
- **Pseudonimizacao:** reduz identificabilidade, mas continua no regime de dado pessoal.
- **Controlador:** decide sobre o tratamento.
- **Operador:** trata dados em nome do controlador.
- **Encarregado:** canal entre controlador, titulares e ANPD, nos termos da LGPD e regulacao aplicavel.
- **Tratamento:** qualquer operacao com dado pessoal, como coleta, uso, armazenamento, compartilhamento, acesso, eliminacao ou transferencia.

## Fluxo de analise

1. **Mapear dados e fontes.** Formularios, conta, logs, cookies, analytics, pagamento, suporte, CRM, marketing, app, SDKs, operadores e terceiros.
2. **Classificar dados.** Nao pessoal, pessoal comum, sensivel, crianca/adolescente, financeiro/alto impacto, identificadores online.
3. **Separar operacoes.** Coleta, uso, armazenamento, compartilhamento, transferencia internacional, eliminacao e resposta a direitos.
4. **Definir finalidade especifica.** Uma frase por operacao. Finalidade generica como "melhorar servicos" exige detalhamento.
5. **Escolher base legal por operacao.** Nao escolher base por documento ou por empresa inteira.
6. **Checar ciclo de vida.** Aviso, minimizacao, retencao, seguranca, operadores, compartilhamento, transferencia e eliminacao.
7. **Checar direitos do titular.** Acesso, confirmacao, correcao, anonimização/bloqueio/eliminacao, portabilidade, informacao sobre compartilhamento, revogacao de consentimento e revisao quando aplicavel.
8. **Avaliar risco.** Dado sensivel, crianca/adolescente, larga escala, monitoramento, perfilamento, decisao automatizada, fraude, vazamento ou alto impacto podem exigir RIPD e revisao especializada.

## Bases legais

### Dados pessoais comuns, art. 7º

Hipoteses recorrentes:

- consentimento;
- cumprimento de obrigacao legal ou regulatoria;
- execucao de politicas publicas pela administracao publica;
- estudos por orgao de pesquisa, com anonimizacao sempre que possivel;
- execucao de contrato ou procedimentos preliminares a pedido do titular;
- exercicio regular de direitos;
- protecao da vida ou incolumidade fisica;
- tutela da saude, por profissionais/servicos de saude ou autoridade sanitaria;
- legitimo interesse, com teste de balanceamento e transparencia reforcada;
- protecao do credito.

Cautelas:

- Consentimento deve ser livre, informado e inequivoco, para finalidade determinada, e revogavel.
- Legítimo interesse nao vale para dados sensiveis e exige teste documentado.
- Execucao de contrato cobre apenas dados necessarios ao contrato ou procedimento pedido pelo titular.
- Obrigacao legal exige indicar a norma concreta.

### Dados sensiveis, art. 11

Usar regime mais restrito:

- consentimento especifico e destacado, para finalidades especificas; ou
- hipoteses sem consentimento previstas na LGPD, como obrigacao legal/regulatoria, politicas publicas, pesquisa, exercicio regular de direitos, protecao da vida, tutela da saude e prevencao a fraude/seguranca do titular em identificacao/autenticacao.

Cautelas:

- Nao usar legitimo interesse para dados sensiveis.
- Foto comum pode virar biometria se usada para identificacao/autenticacao.
- Dado de saude, biometria, genetico, vida sexual, religiao, opiniao politica e filiacao sindical exigem revisao forte.

## Criancas e adolescentes

Use art. 14 da LGPD, ECA, Lei nº 15.211/2025 e Decreto nº 12.880/2026 quando o produto for direcionado a criancas/adolescentes ou de acesso provavel por eles.

Regras praticas:

- Tratar no melhor interesse da crianca/adolescente.
- Avaliar consentimento especifico de pelo menos um dos pais ou responsavel quando exigido.
- Reduzir coleta, publicidade comportamental, perfilamento e compartilhamento.
- Usar linguagem adequada a idade.
- Encaminhar a autoridade competente se houver risco, abuso, exploracao, violencia ou incidente relevante.

## Politica de privacidade

Uma politica boa deve explicar:

- quem e o controlador e como contata-lo;
- quais dados sao tratados;
- finalidades especificas;
- bases legais por finalidade ou grupo de finalidade;
- compartilhamentos e operadores;
- transferencia internacional;
- cookies, SDKs e tecnologias similares;
- retencao e criterios de eliminacao;
- direitos do titular e canal de atendimento;
- encarregado ou canal equivalente, conforme obrigacao aplicavel;
- seguranca e incidentes em linguagem honesta;
- dados de criancas/adolescentes, se houver.

Red flags:

- "Podemos usar seus dados para qualquer finalidade".
- Consentimento unico para tudo.
- Ausencia de base legal ou base legal generica.
- Retencao indefinida sem criterio.
- Compartilhamento com "parceiros" sem categorias/finalidades.
- Politica contradiz checkout, app, cookies, SDKs, logs ou contratos.
- Dificultar revogacao de consentimento ou exercicio de direitos.

## Cookies, SDKs e analytics

Coletar:

- lista de cookies/SDKs/tags;
- finalidade de cada tecnologia;
- fornecedor terceiro;
- duracao;
- se identifica ou perfila pessoa;
- se ha transferencia internacional;
- se e estritamente necessario, funcional, analytics, publicidade ou antifraude.

Cautelas:

- Cookie necessario e diferente de marketing ou analytics comportamental.
- Banner que so informa, sem opcao adequada quando necessaria, pode ser insuficiente.
- Transferencia para ferramentas estrangeiras exige analise de transferencia internacional.

## Incidentes de seguranca

Use LGPD art. 48 e regulacao da ANPD.

Coletar:

- o que ocorreu;
- quando foi detectado;
- categorias e volume de dados;
- titulares afetados;
- medidas tecnicas e administrativas;
- risco ou dano relevante;
- comunicacao interna, a titulares e a ANPD;
- operadores/terceiros envolvidos.

Cautelas:

- Nao afirmar que todo incidente deve ser comunicado publicamente; depende de risco ou dano relevante e regulacao aplicavel.
- Para controladores, a Comunicacao de Incidente de Seguranca tem fluxo proprio na ANPD.
- Titular que quer noticiar incidente deve usar canal de denuncia, nao o fluxo de comunicacao do controlador.

## Transferencia internacional

Aplicar LGPD art. 33 e Resolução CD/ANPD nº 19/2024.

Verificar:

- pais ou regiao de destino;
- operador/suboperador;
- mecanismo: decisao de adequacao, clausulas-padrao, clausulas especificas, normas corporativas globais, consentimento especifico, execucao de contrato, cumprimento legal ou outra hipotese;
- contrato com operador;
- transparencia ao titular.

## Saida recomendada

```md
Nivel de certeza: [base legal direta | tese plausivel | tema controvertido | fora do escopo da skill]

Enquadramento:
- LGPD: [dados, finalidade e base provavel].
- CDC: [se houver relacao de consumo/transparencia B2C].
- Marco Civil: [se houver provedor, logs, aplicacao, IP ou conteudo].
- ANPD/norma setorial: [se aplicavel].

Pontos que faltam:
1. [dado/documento/fluxo]
2. [base/retencao/operador]

Caminho pratico:
1. mapear dados e finalidades;
2. revisar bases legais por operacao;
3. ajustar politica/canal/retencao/contratos;
4. procurar encarregado, ANPD, advogado ou especialista se houver risco relevante.
```

Evite:

- "Esta politica esta 100% conforme a LGPD."
- "Consentimento resolve tudo."
- "Dado anonimizado" quando e apenas hash, token, ID ou pseudonimo.
- "LGPD nao se aplica a logs/IP/cookies."
- "Todo vazamento gera dano moral automatico."
