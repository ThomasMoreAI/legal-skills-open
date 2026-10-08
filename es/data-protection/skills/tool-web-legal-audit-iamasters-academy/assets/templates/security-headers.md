# Headers HTTP de seguridad — snippets por servidor

## Nginx

```nginx
# Añadir dentro del bloque server { ... }

add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
add_header X-Content-Type-Options "nosniff" always;
add_header X-Frame-Options "SAMEORIGIN" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Permissions-Policy "geolocation=(), microphone=(), camera=()" always;

# CSP básica — ajustar según scripts de terceros que necesites permitir
add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com https://www.google-analytics.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:; font-src 'self' data:; connect-src 'self' https://www.google-analytics.com; frame-ancestors 'self';" always;
```

## Apache (.htaccess)

```apache
<IfModule mod_headers.c>
  Header always set Strict-Transport-Security "max-age=31536000; includeSubDomains; preload"
  Header always set X-Content-Type-Options "nosniff"
  Header always set X-Frame-Options "SAMEORIGIN"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  Header always set Permissions-Policy "geolocation=(), microphone=(), camera=()"
  Header always set Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline' https://www.googletagmanager.com; style-src 'self' 'unsafe-inline'; img-src 'self' data: https:;"
</IfModule>
```

## Vercel (next.config.js)

```js
const securityHeaders = [
  { key: 'Strict-Transport-Security', value: 'max-age=31536000; includeSubDomains; preload' },
  { key: 'X-Content-Type-Options', value: 'nosniff' },
  { key: 'X-Frame-Options', value: 'SAMEORIGIN' },
  { key: 'Referrer-Policy', value: 'strict-origin-when-cross-origin' },
  { key: 'Permissions-Policy', value: 'geolocation=(), microphone=(), camera=()' },
];

module.exports = {
  async headers() {
    return [{ source: '/:path*', headers: securityHeaders }];
  },
};
```

## Cloudflare Workers

```js
const headers = {
  'Strict-Transport-Security': 'max-age=31536000; includeSubDomains; preload',
  'X-Content-Type-Options': 'nosniff',
  'X-Frame-Options': 'SAMEORIGIN',
  'Referrer-Policy': 'strict-origin-when-cross-origin',
  'Permissions-Policy': 'geolocation=(), microphone=(), camera=()',
};

addEventListener('fetch', event => event.respondWith(handle(event.request)));
async function handle(req) {
  const res = await fetch(req);
  const r = new Response(res.body, res);
  for (const [k, v] of Object.entries(headers)) r.headers.set(k, v);
  return r;
}
```

## Verificación

Tras aplicar, prueba en:

- https://securityheaders.com
- https://observatory.mozilla.org
- https://www.ssllabs.com/ssltest/

Target: A o A+.

## Cookies seguras (Express / Node)

```js
res.cookie('session', value, {
  httpOnly: true,
  secure: true,         // solo en HTTPS
  sameSite: 'lax',      // 'strict' si no hay OAuth
  maxAge: 1000 * 60 * 60 * 8, // 8 horas
  path: '/',
});
```
