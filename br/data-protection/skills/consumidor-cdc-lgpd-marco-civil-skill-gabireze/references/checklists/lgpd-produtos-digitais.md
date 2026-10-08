# Checklist: LGPD para produtos digitais

Use para revisar app, SaaS, marketplace, e-commerce, landing page, checkout, politica de privacidade, cookies, termos, fluxo de cadastro, suporte, CRM, analytics e incidentes.

## Classificacao inicial

- [ ] O fluxo coleta dado pessoal comum?
- [ ] O fluxo coleta dado sensivel?
- [ ] Ha dado de crianca/adolescente?
- [ ] Ha identificadores online: IP, cookie, device ID, advertising ID, user agent, fingerprint?
- [ ] Ha dados financeiros, score, antifraude ou pagamento?
- [ ] Ha foto, biometria, geolocalizacao ou documento oficial?
- [ ] Ha texto livre que possa conter dado pessoal/sensivel?

## Operacoes de tratamento

- [ ] Coleta
- [ ] Uso interno
- [ ] Armazenamento
- [ ] Compartilhamento com operador
- [ ] Compartilhamento com controlador terceiro
- [ ] Transferencia internacional
- [ ] Uso para marketing, perfilamento ou recomendacao
- [ ] Logs, auditoria, seguranca e antifraude
- [ ] Eliminacao, anonimização ou bloqueio

## Evidencias minimas

- [ ] Politica de privacidade vigente e historico de versoes.
- [ ] Termos de uso e tela de aceite.
- [ ] Formulario, checkout, app screens, cookie banner e central de preferencias.
- [ ] Inventario de cookies, SDKs, tags, analytics e pixels.
- [ ] Lista de operadores, subprocessadores e terceiros.
- [ ] Retencao por dado/finalidade.
- [ ] Canal de direitos do titular.
- [ ] Contratos com operadores.
- [ ] Plano ou registro de incidente, se houver.

## Base legal por operacao

| Operacao | Pergunta | Cautela |
|---|---|---|
| Cadastro/conta | O dado e necessario para criar ou manter a conta? | Execucao de contrato nao cobre dado opcional. |
| Pagamento | O dado e necessario para cobrar, emitir nota ou prevenir fraude? | Separar pagamento, fiscal, antifraude e suporte. |
| Marketing | O titular espera esse uso? Ha opt-out/consentimento quando necessario? | Consentimento generico ou pre-marcado e arriscado. |
| Analytics | Identifica pessoa ou e agregado? | Cookie/SDK pode envolver transferencia internacional. |
| Suporte | O dado e necessario para resolver o ticket? | Texto livre pode conter sensivel. |
| Segurança/logs | Qual evento e registrado, por quanto tempo e quem acessa? | Minimizar logs e mascarar PII. |
| Compartilhamento | O terceiro e operador ou controlador independente? | Cada finalidade precisa de base e contrato. |
| Transferencia internacional | Dados saem do Brasil ou sao acessados fora? | Ver Resolução CD/ANPD nº 19/2024. |

## Direitos do titular

- [ ] Confirmacao de tratamento.
- [ ] Acesso aos dados.
- [ ] Correcao.
- [ ] Anonimizacao, bloqueio ou eliminacao quando cabivel.
- [ ] Portabilidade quando regulamentada/aplicavel.
- [ ] Informacao sobre compartilhamento.
- [ ] Revogacao de consentimento.
- [ ] Informacao sobre consequencias da negativa.
- [ ] Revisao de decisoes automatizadas quando aplicavel.

## Red flags

- Politica sem controlador ou canal claro.
- Uso de "legitimo interesse" sem teste de balanceamento.
- Base legal unica para todas as finalidades.
- Consentimento agrupado em termos de uso.
- Dados sensiveis tratados como dados comuns.
- Dados de criancas/adolescentes sem melhor interesse e cautelas proprias.
- Retencao "por tempo indeterminado".
- Logs com CPF, token, senha, documento, cartao ou dado sensivel.
- Operadores sem contrato ou sem instrucao documentada.
- Transferencia internacional omitida.
- Incidente tratado sem avaliar comunicacao a ANPD/titulares.

## Saida sugerida

```md
## Diagnostico LGPD
[Resumo do fluxo e principal risco.]

## Classificacao
| Dado/fonte | Categoria | Finalidade | Base legal provavel | Retencao | Risco |
|---|---|---|---|---|---|

## Ajustes recomendados
1. [ajuste]
2. [ajuste]

## Texto sugerido
[Trecho de politica, aviso, banner ou comunicacao.]

## Cautelas
- Confirmar fontes oficiais e regulamentacoes da ANPD.
- Revisao juridica/especialista recomendada se houver dado sensivel, crianca/adolescente, alto risco, incidente ou transferencia internacional relevante.
```
