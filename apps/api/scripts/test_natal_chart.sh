#!/usr/bin/env zsh

# Script de test pour POST /api/natal-chart (mode DEV_MOCK_EPHEMERIS=1)
# Usage: ./scripts/test_natal_chart.sh email password
#
# Prérequis .env:
#   EPHEMERIS_API_KEY=
#   DEV_MOCK_EPHEMERIS=1

API_URL=http://127.0.0.1:8000
EMAIL=$1
PASSWORD=$2

if [ -z $EMAIL ] || [ -z $PASSWORD ]; then
  echo 'Usage: ./scripts/test_natal_chart.sh email password' >&2
  exit 1
fi

echo '🔐 1. Login...'
TOKEN=$(./scripts/get_token.sh $EMAIL $PASSWORD)

if [ -z $TOKEN ] || [ $TOKEN = null ]; then
  echo '❌ Erreur login' >&2
  exit 1
fi

echo "✅ Token: ${TOKEN:0:20}..."
echo ''

# 2. Créer natal_chart (mode mock)
echo '✨ 2. POST /api/natal-chart (mode mock)...'

NATAL_PAYLOAD=$(python3 - << 'EOF'
import json
payload = {
    'date': '1990-05-15',
    'time': '14:30:00',
    'latitude': 48.8566,
    'longitude': 2.3522,
    'place_name': 'Paris, France',
    'timezone': 'Europe/Paris',
}
print(json.dumps(payload))
EOF
)

NATAL_HTTP_CODE=$(printf '%s' $NATAL_PAYLOAD | curl -s -o /tmp/natal_response.json -w '%{http_code}' \
  -X POST $API_URL/api/natal-chart \
  -H 'Authorization: Bearer '$TOKEN \
  -H 'Content-Type: application/json' \
  -d @-)

NATAL_BODY=$(cat /tmp/natal_response.json)

echo "   Status: $NATAL_HTTP_CODE"

if [ $NATAL_HTTP_CODE -ne 201 ]; then
  echo '❌ Erreur création natal_chart'
  echo "   Body: $NATAL_BODY"
  exit 1
fi

# Vérifier si c'est du JSON valide
NATAL_ID=$(printf '%s' $NATAL_BODY | python3 -c 'import sys, json; print(json.load(sys.stdin).get("id", "null"))' 2>/dev/null)
SUN_SIGN=$(printf '%s' $NATAL_BODY | python3 -c 'import sys, json; print(json.load(sys.stdin).get("sun_sign", "null"))' 2>/dev/null)

if [ -z $NATAL_ID ] || [ $NATAL_ID = null ]; then
  echo '❌ Réponse natal_chart invalide (pas de JSON ou id manquant)'
  echo "   Body brut: $NATAL_BODY"
  exit 1
fi

echo "   ✅ Natal chart créé - ID: $NATAL_ID, Sun: $SUN_SIGN"
echo ''
echo '📋 Réponse complète:'
printf '%s' $NATAL_BODY | python3 -m json.tool 2>/dev/null || echo "$NATAL_BODY"
echo ''
echo '🎉 Test POST /api/natal-chart réussi !'

