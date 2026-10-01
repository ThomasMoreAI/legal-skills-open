#!/usr/bin/env bash
# Ispeziona il container Google Tag Manager REALE lato server (nessun ad-blocker).
# Estrae gli ID dei tag effettivamente configurati.
#
# Uso:  bash inspect_container.sh GTM-XXXXXXX
#       bash inspect_container.sh G-XXXXXXXXXX   # anche un measurement GA4 diretto (gtag.js)
#
# Perché lato server: un browser con uBlock/adblock riceve uno STUB di gtm.js
# (~pochi KB) e non mostra i tag reali. curl bypassa l'ad-blocker.

set -euo pipefail
ID="${1:-}"
if [[ -z "$ID" ]]; then echo "Uso: bash inspect_container.sh <GTM-XXXX|G-XXXX>"; exit 1; fi

UA="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36"
case "$ID" in
  GTM-*) URL="https://www.googletagmanager.com/gtm.js?id=${ID}" ;;
  G-*|AW-*|DC-*) URL="https://www.googletagmanager.com/gtag/js?id=${ID}" ;;
  *) echo "ID non riconosciuto: $ID (atteso GTM-/G-/AW-/DC-)"; exit 1 ;;
esac

TMP="$(mktemp -t gtmcontainer.XXXXXX)"
trap 'rm -f "$TMP"' EXIT
curl -s -A "$UA" --referer "https://www.googletagmanager.com/" "$URL" -o "$TMP"

SIZE=$(wc -c < "$TMP" | tr -d ' ')
echo "== Container $ID =="
echo "URL:  $URL"
echo "Peso: ${SIZE} byte"
if grep -qi "uBlock\|noopfn\|ublockorigin" "$TMP"; then
  echo "⚠️  ATTENZIONE: risposta = STUB di un ad-blocker, non il container reale. Rilancia in rete senza filtri."
  exit 2
fi
if [[ "$SIZE" -lt 10000 ]]; then
  echo "⚠️  Container sospettosamente piccolo (<10KB): possibile stub o container vuoto."
fi

echo
echo "-- GA4 (misurazione) --";        grep -oE 'G-[A-Z0-9]{6,12}'          "$TMP" | sort -u || true
echo "-- Google Ads (conversioni) --"; grep -oE 'AW-[0-9]{8,12}'            "$TMP" | sort -u || true
echo "-- Floodlight --";               grep -oE 'DC-[0-9]{6,12}'            "$TMP" | sort -u || true
echo "-- Universal Analytics (legacy) --"; grep -oE 'UA-[0-9]{4,10}-[0-9]+' "$TMP" | sort -u || true

echo
echo "-- Tipi di tag configurati (__googtag/__gaawc=GA4 config, __gaawe=GA4 event, __ogt_*=Ads) --"
grep -oE '"function":"__[a-z_]+"' "$TMP" | sort | uniq -c | sort -rn | head -20 || true

echo
echo "-- Terze parti non-Google referenziate --"
grep -oiE '(connect\.facebook\.net|facebook\.com/tr|px\.ads\.linkedin\.com|snap\.licdn\.com|static\.hotjar\.com|clarity\.ms|hs-scripts\.com|hubspot|analytics\.tiktok\.com|bat\.bing|pinterest|reddit)' "$TMP" | sort | uniq -c | sort -rn || echo "   (nessuna)"

echo
echo "-- Consent Mode v2 / Google Signals --"
grep -oiE '(ad_storage|analytics_storage|ad_user_data|ad_personalization|ads_data_redaction|google_signals|conversion_linker|url_passthrough|wait_for_update)' "$TMP" | sort | uniq -c | sort -rn | head || echo "   (nessun segnale consent-mode: verificare il gating dei tag)"

echo
echo "Nota: riferimenti a googleadservices/doubleclick in un container con solo G- sono boilerplate GA4, non tag Ads separati (vedi cmp-tracker-fingerprints.md)."
