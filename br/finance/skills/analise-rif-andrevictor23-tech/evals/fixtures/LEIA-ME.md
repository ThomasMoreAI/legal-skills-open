# Fixtures de avaliação — DADOS 100% FICTÍCIOS

Todos os arquivos CSV desta pasta foram criados artificialmente para testar a skill `analise-rif`. Nomes, CPFs, CNPJs, contas, agências, valores, datas e números de comunicação são invenções sem qualquer correspondência com pessoas, empresas ou procedimentos reais.

| Pasta | O que testa |
|---|---|
| `caso1-estruturacao/` | Tipologia óbvia de fracionamento + interposta pessoa + incompatibilidade patrimonial. A skill deve identificar as tipologias e filtrar linhas não-indexadoras (legendas, hashes). |
| `caso2-atipica-explicavel/` | Movimentação alta mas com explicação lícita aparente (produtor rural em safra). A skill deve evitar acusar além do que os dados sustentam. |
| `caso3-truncado/` | Dados incompletos, truncados e inconsistentes. A skill deve declarar as limitações e jamais preencher lacunas por inferência. |

Os casos correspondem aos evals em `../evals.json`.
