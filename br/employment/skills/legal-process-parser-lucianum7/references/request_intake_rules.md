# Gate adaptativo de escopo

## Regra geral

Comece pelos materiais disponíveis: arquivos enviados, `manifest.json`,
`relatorio_processual.md`, índices e versões preservadas. Extraia deles o que
for possível sobre arquivo/processo, entrega, partes, órgão, objetivo, prazo,
sigilo e profundidade. Não faça perguntas para repetir informações que já
estejam nos autos ou no histórico.

Pergunte somente se pelo menos uma destas condições ocorrer:

- o pedido não identifica uma tarefa ou há mais de uma interpretação plausível;
- os arquivos entram em conflito e a escolha altera o resultado;
- um dado indispensável para a entrega não pode ser encontrado;
- a redação de uma petição ou auditoria completa exigiria uma autorização que
  não foi dada de forma clara.

Se o pedido for claro, execute diretamente uma única tarefa e produza somente
os artefatos correspondentes. Nunca descarte upload, original ou relatório
anterior: novos itens são incorporados e o histórico é atualizado.

## Perfis de tarefa

| Tarefa | Perguntas de fallback (somente se necessário) | Saída permitida |
|---|---|---|
| ingest | formato de preservação, OCR ou revisão visual que não puder ser inferido | base documental e localização por página |
| analyze | questão processual ou profundidade que não puder ser determinada | cronologia, controvérsias, matriz documental, provas e riscos solicitados |
| petition | tipo de peça, pedidos ou órgão ausente e indispensável | checklist e minuta marcada como não protocolável |
| deadlines | marco, calendário ou responsável ausente e indispensável | prazos e pendências para conferência; nunca cálculo definitivo |
| evidence | fato controvertido ou escopo de comparação não localizado | mapa de provas e fontes |
| audit | autorização para pacote completo quando o pedido não a indicar | todos os relatórios previstos |

As perguntas acima são um mecanismo de recuperação, não um formulário
obrigatório. Se o dado estiver identificável nos documentos, registre a fonte e
continue sem interromper o usuário.

## Confirmação opcional

`--confirm-scope` pode registrar uma confirmação explícita no manifesto, mas não
é requisito para executar. Uma confirmação curta é recomendada apenas quando a
interpretação escolhida possa gerar uma peça ou auditoria materialmente diferente
do que o usuário pretendia.

Exemplo quando realmente necessário:

> Encontrei a decisão e os anexos no histórico. Vou executar `analyze` somente
> para a questão de prazo indicada na fl. 12 e atualizar
> `relatorio_processual.md`. Confirmo essa interpretação?

## Atualizações

Ao receber novo upload, compare o SHA-256, preserve o original em `original/`,
arquive a execução anterior em `versions/` e reconstrua o relatório cumulativo.
Nenhum arquivo enviado anteriormente deve ser removido; a versão atual fica na
raiz e cada versão antiga permanece localizável pelo manifesto e pelos índices.
