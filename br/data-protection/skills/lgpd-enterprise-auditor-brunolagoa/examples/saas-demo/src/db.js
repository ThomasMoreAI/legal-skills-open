const { Pool } = require('pg');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: { rejectUnauthorized: true },
  max: 5,
});

module.exports = {
  query: (texto, parametros) => pool.query(texto, parametros),
};
