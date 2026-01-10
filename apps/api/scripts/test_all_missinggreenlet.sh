#!/bin/bash
# Script de test complet pour valider tous les endpoints fixés contre MissingGreenlet

set -e

API_URL="${API_URL:-http://127.0.0.1:8000}"
USER_ID="550e8400-e29b-41d4-a716-446655440000"

echo "🧪 Test MissingGreenlet Prevention - Tous les endpoints"
echo "📡 API: $API_URL"
echo "👤 User UUID: $USER_ID"
echo ""

# 1. POST /natal-chart (DEV_MOCK_NATAL)
echo "1️⃣ Test POST /natal-chart (DEV_MOCK_NATAL)"
tmpfile=$(mktemp)
trap "rm -f $tmpfile" EXIT

http_code=$(curl -X POST "$API_URL/api/natal-chart" \
  -H "X-Dev-External-Id: $USER_ID" \
  -H "Content-Type: application/json" \
  -d '{
    "date": "1990-01-15",
    "time": "14:30",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "place_name": "Paris, France"
  }' \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

if [ "$http_code" = "200" ] || [ "$http_code" = "201" ]; then
  echo "✅ POST /natal-chart: HTTP $http_code"
else
  echo "❌ POST /natal-chart: HTTP $http_code (expected 200/201)"
  cat "$tmpfile"
  exit 1
fi

# 2. GET /natal-chart
echo ""
echo "2️⃣ Test GET /natal-chart"
http_code=$(curl -X GET "$API_URL/api/natal-chart" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ GET /natal-chart: HTTP $http_code"
else
  echo "❌ GET /natal-chart: HTTP $http_code (expected 200)"
  cat "$tmpfile"
  exit 1
fi

# 3. POST /lunar-returns/dev/purge
echo ""
echo "3️⃣ Test POST /lunar-returns/dev/purge"
http_code=$(curl -X POST "$API_URL/api/lunar-returns/dev/purge" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ POST /dev/purge: HTTP $http_code"
else
  echo "❌ POST /dev/purge: HTTP $http_code (expected 200)"
  cat "$tmpfile"
  exit 1
fi

# 4. GET /lunar-returns/current
echo ""
echo "4️⃣ Test GET /lunar-returns/current"
http_code=$(curl -X GET "$API_URL/api/lunar-returns/current" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ GET /current: HTTP $http_code"
else
  echo "⚠️ GET /current: HTTP $http_code (attendu 200, peut retourner null)"
  # Pas d'exit ici car null est acceptable
fi

# 5. POST /lunar-returns/generate
echo ""
echo "5️⃣ Test POST /lunar-returns/generate"
http_code=$(curl -X POST "$API_URL/api/lunar-returns/generate" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

if [ "$http_code" = "201" ]; then
  echo "✅ POST /generate: HTTP $http_code"
else
  echo "❌ POST /generate: HTTP $http_code (expected 201)"
  cat "$tmpfile"
  exit 1
fi

# 6. GET /lunar-returns/current (après génération)
echo ""
echo "6️⃣ Test GET /lunar-returns/current (après génération)"
http_code=$(curl -X GET "$API_URL/api/lunar-returns/current" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ GET /current (après génération): HTTP $http_code"
else
  echo "❌ GET /current: HTTP $http_code (expected 200 après génération)"
  cat "$tmpfile"
  exit 1
fi

# 7. GET /lunar-returns/rolling
echo ""
echo "7️⃣ Test GET /lunar-returns/rolling"
http_code=$(curl -X GET "$API_URL/api/lunar-returns/rolling" \
  -H "X-Dev-External-Id: $USER_ID" \
  -w "%{http_code}" \
  -o "$tmpfile" \
  -sS)

if [ "$http_code" = "200" ]; then
  echo "✅ GET /rolling: HTTP $http_code"
else
  echo "❌ GET /rolling: HTTP $http_code (expected 200)"
  cat "$tmpfile"
  exit 1
fi

rm -f "$tmpfile"

echo ""
echo "✅ Test terminé - Tous les endpoints critiques OK"
echo "   Aucune erreur MissingGreenlet détectée !"
