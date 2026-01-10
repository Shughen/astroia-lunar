#!/bin/bash
# Test: Reproduire le bug MissingGreenlet sur /current après purge
# Scenario: purge → /current doit générer rolling + renvoyer 200 (pas 500)

set -e

SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"
API_URL="${API_URL:-http://127.0.0.1:8000}"
DEV_USER_UUID="550e8400-e29b-41d4-a716-446655440000"

echo "🧪 Test /api/lunar-returns/current après purge"
echo "📡 API: $API_URL"
echo "👤 User UUID: $DEV_USER_UUID"
echo ""

# Fonction helper curl
call_api() {
    local method="$1"
    local endpoint="$2"
    local description="$3"

    echo "$description"

    local tmpfile=$(mktemp)
    trap "rm -f $tmpfile" EXIT

    local http_code=$(curl -X "$method" "$API_URL$endpoint" \
      -H "X-Dev-External-Id: $DEV_USER_UUID" \
      -H "Content-Type: application/json" \
      -w "%{http_code}" \
      -o "$tmpfile" \
      -sS)

    echo "HTTP Status: $http_code"

    if [ "$http_code" = "200" ] || [ "$http_code" = "204" ]; then
        if [ -s "$tmpfile" ]; then
            python3 -m json.tool < "$tmpfile" 2>/dev/null || cat "$tmpfile"
        else
            echo "(Body vide)"
        fi
    else
        echo "❌ Erreur HTTP $http_code"
        cat "$tmpfile"
        rm -f "$tmpfile"
        exit 1
    fi

    rm -f "$tmpfile"
    echo ""
}

# Étape 1: Purge pour vider la table
echo "1️⃣ Purge lunar_returns..."
call_api "POST" "/api/lunar-returns/dev/purge" "Purge DB"

# Étape 2: Appeler /current (devrait générer rolling + renvoyer 200)
echo "2️⃣ Appel /current (DB vide → génération rolling attendue)..."
call_api "GET" "/api/lunar-returns/current" "GET /current"

# Étape 3: Re-appeler /current (devrait renvoyer 200 immédiat, pas de génération)
echo "3️⃣ Re-appel /current (devrait utiliser cache/DB)..."
call_api "GET" "/api/lunar-returns/current" "GET /current (2e fois)"

echo ""
echo "✅ Tests terminés sans erreur 500 (bug MissingGreenlet corrigé)"
