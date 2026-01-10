#!/usr/bin/env zsh

# Script E2E complet (mode DEV_MOCK_EPHEMERIS=1)
# Flow: login -> POST /api/natal-chart -> POST /api/lunar-returns/generate -> GET /api/lunar-returns/
#
# Prérequis .env:
#   EPHEMERIS_API_KEY=
#   DEV_MOCK_EPHEMERIS=1

API_URL=http://127.0.0.1:8000
EMAIL=$1
PASSWORD=$2

if [ -z $EMAIL ] || [ -z $PASSWORD ]; then
  echo 'Usage: ./scripts/e2e_mock.sh email password' >&2
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
echo '✨ 2. Création natal_chart (mode mock)...'

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

if [ -z $NATAL_ID ] || [ $NATAL_ID = null ]; then
  echo '❌ Réponse natal_chart invalide (pas de JSON ou id manquant)'
  echo "   Body brut: $NATAL_BODY"
  exit 1
fi

echo "   ✅ Natal chart créé - ID: $NATAL_ID"
echo ''

# 3. Générer révolutions lunaires
echo '🌙 3. Génération révolutions lunaires...'

LUNAR_HTTP_CODE=$(curl -s -o /tmp/lunar_response.json -w '%{http_code}' \
  -X POST $API_URL/api/lunar-returns/generate \
  -H 'Authorization: Bearer '$TOKEN \
  -H 'Content-Type: application/json')

LUNAR_BODY=$(cat /tmp/lunar_response.json)

echo "   Status: $LUNAR_HTTP_CODE"

if [ $LUNAR_HTTP_CODE -ne 201 ]; then
  echo '❌ Erreur génération lunar returns'
  echo "   Body: $LUNAR_BODY"
  exit 1
fi

# Vérifier si c'est du JSON valide
GENERATED_COUNT=$(printf '%s' $LUNAR_BODY | python3 -c 'import sys, json; print(json.load(sys.stdin).get("generated_count", "null"))' 2>/dev/null)

if [ -z $GENERATED_COUNT ] || [ $GENERATED_COUNT = null ]; then
  echo '❌ Réponse lunar returns invalide (pas de JSON ou generated_count manquant)'
  echo "   Body brut: $LUNAR_BODY"
  exit 1
fi

echo "   ✅ $GENERATED_COUNT révolution(s) lunaire(s) générée(s)"
echo ''

# 4. Récupérer révolutions lunaires
echo '📋 4. Récupération révolutions lunaires...'

LUNAR_LIST_HTTP_CODE=$(curl -s -o /tmp/lunar_list_response.json -w '%{http_code}' \
  -X GET $API_URL/api/lunar-returns/ \
  -H 'Authorization: Bearer '$TOKEN)

LUNAR_LIST_BODY=$(cat /tmp/lunar_list_response.json)

echo "   Status: $LUNAR_LIST_HTTP_CODE"

if [ $LUNAR_LIST_HTTP_CODE -ne 200 ]; then
  echo '❌ Erreur récupération lunar returns'
  echo "   Body: $LUNAR_LIST_BODY"
  exit 1
fi

# Vérifier si c'est du JSON valide (array)
LUNAR_COUNT=$(printf '%s' $LUNAR_LIST_BODY | python3 -c 'import sys, json; data = json.load(sys.stdin); print(len(data) if isinstance(data, list) else 0)' 2>/dev/null)

if [ -z $LUNAR_COUNT ]; then
  echo '❌ Réponse lunar returns list invalide (pas de JSON ou pas un array)'
  echo "   Body brut: $LUNAR_LIST_BODY"
  exit 1
fi

echo "   ✅ $LUNAR_COUNT révolution(s) lunaire(s) trouvée(s)"
echo ''
echo '🎉 Flow E2E complet validé !'

