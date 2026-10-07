/**
 * lib/templates-de/render.js — Moteur de rendu minimal sans dépendance.
 *
 * Syntaxe supportée :
 *   - {{ variable }}                  — substitution simple
 *   - {{ obj.sous_propriete }}        — chemin pointé
 *   - {{ var | default('fallback') }} — valeur par défaut
 *   - {% for x in liste %} ... {% endfor %}  — boucle (loop.index disponible)
 *   - {% if condition %} ... {% endif %}     — bloc conditionnel
 *
 * Volontairement strict et lisible. Pour des cas plus complexes, utiliser une
 * lib externe (mustache, nunjucks).
 *
 * LIMITATIONS CONNUES :
 *   - Pas de support des blocs imbriqués ({% for %} dans {% for %}, ou
 *     {% if %} dans {% for %}). Les regex sont non-récursives.
 *   - Pas de support de {% else %}.
 *   - Les 6 templates DE livrés ont été conçus pour rester dans ce périmètre :
 *     une boucle simple sur tagesordnung/positionen, des conditions au niveau
 *     racine sur reverse_charge / mwst_befreit. Pour des templates plus complexes,
 *     basculer sur nunjucks.
 */

function getPath(obj, path) {
  if (!obj || !path) return undefined;
  return path.split('.').reduce((o, k) => o?.[k], obj);
}

function evalExpr(expr, ctx) {
  expr = expr.trim();
  // Gestion du filtre | default('...')
  const defMatch = expr.match(/^(.+?)\s*\|\s*default\(\s*['"]([^'"]*)['"]\s*\)\s*$/);
  if (defMatch) {
    const v = getPath(ctx, defMatch[1].trim());
    return v == null || v === '' ? defMatch[2] : v;
  }
  return getPath(ctx, expr);
}

function renderLoop(template, ctx) {
  const re = /\{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%\}([\s\S]*?)\{%\s*endfor\s*%\}/g;
  return template.replace(re, (_, varName, listName, body) => {
    const list = getPath(ctx, listName);
    if (!Array.isArray(list)) return '';
    return list.map((item, i) => {
      const subCtx = { ...ctx, [varName]: item, loop: { index: i + 1, index0: i } };
      return renderConditions(renderVars(body, subCtx), subCtx);
    }).join('');
  });
}

function renderConditions(template, ctx) {
  const re = /\{%\s*if\s+([\w.]+)\s*%\}([\s\S]*?)\{%\s*endif\s*%\}/g;
  return template.replace(re, (_, condVar, body) => {
    const v = getPath(ctx, condVar);
    return v ? renderVars(body, ctx) : '';
  });
}

function renderVars(template, ctx) {
  return template.replace(/\{\{\s*([^}]+?)\s*\}\}/g, (_, expr) => {
    const v = evalExpr(expr, ctx);
    return v == null ? '' : String(v);
  });
}

/**
 * Rend un template avec un contexte JSON.
 * Ordre : boucles → conditions → variables (les boucles peuvent contenir conditions et vars).
 */
export function renderTemplate(template, ctx) {
  let out = renderLoop(template, ctx);
  out = renderConditions(out, ctx);
  out = renderVars(out, ctx);
  return out;
}
