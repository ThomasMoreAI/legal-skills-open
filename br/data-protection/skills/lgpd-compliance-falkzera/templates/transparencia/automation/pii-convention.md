# Convenção de Anotação @pii: `{{APP_NOME}}`

> Como anotar campos de PII no código pra a skill `lgpd-compliance` gerar o inventário público automaticamente. Sem isso, `scripts/gerar-inventario.py` não consegue mapear o que está sendo coletado.

## Filosofia

**Manifesto escrito à mão envelhece em duas sprints.** Aqui, ele é gerado do código, o que significa que **o código é a fonte da verdade**. Pra isso funcionar, cada campo de PII precisa ter anotação estruturada.

## Sintaxe

### Postgres (`COMMENT ON COLUMN`)

```sql
COMMENT ON COLUMN users.email IS
  '@pii @finalidade=autenticacao,comunicacao_transacional @base=art_7_V_contrato @retencao=conta+5y @sensibilidade=baixa @compartilha=resend';
```

### Python (decorator)

```python
from lgpd_compliance.pii import pii

@pii(
    finalidade=["autenticacao", "comunicacao_transacional"],
    base_legal="art_7_V_contrato",
    retencao="conta+5y",
    sensibilidade="baixa",
    compartilha_com=["resend"],
)
class User(Base):
    email: Mapped[str] = mapped_column(String(255))
```

Decorator também aceita anotação por campo individual em Pydantic/dataclass:

```python
class UserSchema(BaseModel):
    email: Annotated[str, PII(
        finalidade=["autenticacao"],
        base_legal="art_7_V_contrato",
        retencao="conta+5y",
        sensibilidade="baixa",
    )]
```

### TypeScript (JSDoc / comment)

```typescript
interface User {
  /** @pii(finalidade=[autenticacao,comunicacao_transacional], base=art_7_V_contrato, retencao=conta+5y, sensibilidade=baixa, compartilha=resend) */
  email: string;

  /** @pii(finalidade=[autenticacao], base=art_7_V_contrato, sensibilidade=critica) */
  passwordHash: string;
}
```

### Prisma schema

```prisma
model User {
  /// @pii(finalidade=[autenticacao,comunicacao_transacional], base=art_7_V_contrato, retencao=conta+5y, sensibilidade=baixa, compartilha=resend)
  email String @unique

  /// @pii(finalidade=[autenticacao], base=art_7_V_contrato, sensibilidade=critica)
  passwordHash String
}
```

### Drizzle schema

```typescript
export const users = pgTable('users', {
  // @pii(finalidade=[autenticacao,comunicacao_transacional], base=art_7_V_contrato, retencao=conta+5y, sensibilidade=baixa, compartilha=resend)
  email: text('email').notNull().unique(),
});
```

### SQLAlchemy

```python
class User(Base):
    __tablename__ = "users"
    # @pii(finalidade=[autenticacao], base=art_7_V_contrato, retencao=conta+5y, sensibilidade=baixa, compartilha=resend)
    email: Mapped[str] = mapped_column(String(255))
```

## Campos da anotação

| Campo | Obrigatório | Valores | Descrição |
|---|---|---|---|
| `finalidade` | **Sim** | Lista de IDs de `transparencia/finalidades.yaml` | Pra que esse dado é usado |
| `base` | **Sim** | `art_7_I_consentimento`, `art_7_II_obrigacao_legal`, `art_7_III_politicas_publicas`, `art_7_IV_pesquisa`, `art_7_V_contrato`, `art_7_VI_processo`, `art_7_VII_protecao_vida`, `art_7_VIII_tutela_saude`, `art_7_IX_legitimo_interesse`, `art_7_X_credito`, `art_11_I_consentimento_sensivel`, `art_11_II_a_obrigacao_legal_sensivel`, etc. | Base legal LGPD |
| `retencao` | **Sim** | String descritiva (`conta+5y`, `5y_apos_ultima_compra`, `6m`, `ate_revogacao`, `enquanto_durar`, etc.) | Quanto tempo guardamos |
| `sensibilidade` | **Sim** | `baixa`, `media`, `alta`, `critica`, `variavel`, `alta_inferencia` | Nível de risco |
| `compartilha` | Não | Lista de IDs de `transparencia/terceiros.yaml` | Operadores que recebem |
| `visivel_para` | Não | Lista (`titular`, `admin_auditoria`, `admin_fiscal`, etc.) | RBAC |
| `criptografia_repouso` | Não | String descritiva | Quando aplicável |
| `obrigatorio` | Não | `true`/`false` | Se o usuário pode optar por não fornecer |

## Marcadores complementares

### `@contains_pii` na tabela/classe

Marca que a tabela inteira contém PII, útil pra o CI verificar que todas as colunas devem ter `@pii` ou justificar exceção.

```sql
COMMENT ON TABLE users IS '@contains_pii';
```

```python
@contains_pii
class User(Base):
    ...
```

### `@no_pii` em campo específico

Quando a tabela tem `@contains_pii` mas um campo específico não é PII (ex: chave estrangeira opaca):

```sql
COMMENT ON COLUMN users.created_at IS '@no_pii';
COMMENT ON COLUMN users.organization_id IS '@no_pii';
```

## Validação automatizada

O CI (`templates/transparencia/automation/ci-check.yml`) verifica:

1. **Toda tabela `@contains_pii`** tem todas as colunas com `@pii` ou `@no_pii`.
2. **Todo `@finalidade=X`** existe em `transparencia/finalidades.yaml`.
3. **Todo `@compartilha=X`** existe em `transparencia/terceiros.yaml`.
4. **Toda `@base=X`** é valor válido (lista acima).
5. **Toda `@sensibilidade=X`** é valor válido.
6. **PR que mexe em schema** sem atualizar `transparencia/inventario.yaml` (gerado) **falha**.

## Como aplicar a um projeto existente

Roteiro de adoção em 3 passos:

1. **Anotar schema**, comece pelas tabelas com PII óbvia (users, orders, sessions). Use `@contains_pii` no `COMMENT ON TABLE`, depois anote cada coluna.
2. **Rodar `scripts/gerar-inventario.py`**, gera o primeiro `inventario.yaml` com base nas anotações.
3. **Ativar CI**, copie `.github/workflows/transparency-check.yml` pro repo. A partir daí, qualquer PR que quebrar a convenção falha.

## Exemplo completo: projeto mínimo

```sql
-- Migration 001_users.sql
CREATE TABLE users (
  id            uuid PRIMARY KEY DEFAULT gen_random_uuid(),
  email         text NOT NULL UNIQUE,
  name          text NOT NULL,
  password_hash text NOT NULL,
  cpf           text,
  created_at    timestamptz NOT NULL DEFAULT now()
);

COMMENT ON TABLE users IS '@contains_pii';
COMMENT ON COLUMN users.id IS '@no_pii';
COMMENT ON COLUMN users.email IS '@pii @finalidade=autenticacao,comunicacao_transacional @base=art_7_V_contrato @retencao=conta+5y @sensibilidade=baixa @compartilha=resend';
COMMENT ON COLUMN users.name IS '@pii @finalidade=personalizacao,comunicacao_transacional @base=art_7_V_contrato @retencao=conta+5y @sensibilidade=baixa';
COMMENT ON COLUMN users.password_hash IS '@pii @finalidade=autenticacao @base=art_7_V_contrato @retencao=conta @sensibilidade=critica';
COMMENT ON COLUMN users.cpf IS '@pii @finalidade=emissao_nf,kyc @base=art_7_II_obrigacao_legal @retencao=5y_apos_ultima_compra @sensibilidade=media @compartilha=stripe @obrigatorio=false';
COMMENT ON COLUMN users.created_at IS '@no_pii';
```

Rodando `python scripts/gerar-inventario.py`, esse schema vira automaticamente uma seção do `inventario.yaml` que é renderizada em `/transparencia/inventario`.
