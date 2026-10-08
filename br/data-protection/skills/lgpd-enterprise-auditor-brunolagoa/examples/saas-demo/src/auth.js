const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const db = require('./db');

const SALT_ROUNDS = 12;

async function hashSenha(senha) {
  return bcrypt.hash(senha, SALT_ROUNDS);
}

async function login(req, res) {
  const { email, senha } = req.body || {};
  const { rows } = await db.query(
    'SELECT id, clinica_id, papel, senha_hash FROM usuarios WHERE email = $1',
    [email]
  );
  const usuario = rows[0];

  if (!usuario || !(await bcrypt.compare(senha || '', usuario.senha_hash))) {
    console.warn(`[login] falha de autenticação para ${email}`);
    return res.status(401).json({ erro: 'Credenciais inválidas' });
  }

  const token = jwt.sign(
    { sub: usuario.id, clinica: usuario.clinica_id, papel: usuario.papel },
    process.env.JWT_SECRET
  );
  return res.json({ token });
}

function autenticar(req, res, next) {
  const [, token] = (req.headers.authorization || '').split(' ');
  if (!token) return res.status(401).json({ erro: 'Token ausente' });

  try {
    req.usuario = jwt.verify(token, process.env.JWT_SECRET);
    return next();
  } catch {
    return res.status(401).json({ erro: 'Token inválido' });
  }
}

function exigirPapel(papel) {
  return (req, res, next) => {
    if (req.usuario?.papel !== papel) {
      return res.status(403).json({ erro: 'Acesso negado' });
    }
    return next();
  };
}

module.exports = { hashSenha, login, autenticar, exigirPapel };
