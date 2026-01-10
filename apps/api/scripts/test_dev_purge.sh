#!/bin/bash
# Script de test pour /dev/purge avec DEV_AUTH_BYPASS
# User standardisé : 550e8400-e29b-41d4-a716-446655440000

set -e

# Détecter le répertoire du script de manière robuste
SCRIPT_DIR="$(cd -- "$(dirname "$0")" && pwd)"

# API URL avec override possible via variable d'environnement
API_URL="${API_URL:-http://127.0.0.1:8000}"
DEV_USER_UUID="550e8400-e29b-41d4-a716-446655440000"

echo "🧪 Test /dev/purge avec user UUID: $DEV_USER_UUID"
echo "📡 API: $API_URL"
echo "📂 Script dir: $SCRIPT_DIR"
echo ""

# Fonction helper pour faire un appel curl et parser le JSON
test_curl() {
    local url="$1"
    local description="$2"

    echo "$description"

    # Utiliser un fichier temporaire pour le body et récupérer http_code séparément
    local tmpfile=$(mktemp)
    trap "rm -f $tmpfile" EXIT

    # -w %{http_code} écrit SEULEMENT le code HTTP, pas de newline
    # -o $tmpfile écrit le body dans un fichier
    local http_code=$(curl -X POST "$url" \
      -H "X-Dev-External-Id: $DEV_USER_UUID" \
      -H "Content-Type: application/json" \
      -w "%{http_code}" \
      -o "$tmpfile" \
      -sS)

    # Afficher le code HTTP
    echo "HTTP Status: $http_code"

    # Si succès, pretty-print le JSON
    if [ "$http_code" = "200" ]; then
        # Vérifier que le fichier n'est pas vide
        if [ -s "$tmpfile" ]; then
            python3 -m json.tool < "$tmpfile" || {
                echo "❌ Erreur parsing JSON"
                echo "Body brut:"
                cat "$tmpfile"
                rm -f "$tmpfile"
                exit 1
            }
        else
            echo "⚠️ Body vide"
        fi
    else
        # Si erreur, afficher le body brut et exit 1
        echo "❌ Erreur HTTP $http_code"
        echo "Réponse:"
        cat "$tmpfile"
        rm -f "$tmpfile"
        exit 1
    fi

    rm -f "$tmpfile"
    echo ""
}

# Test 1: Purge
test_curl "$API_URL/api/lunar-returns/dev/purge" "1️⃣ Test purge..."

# Test 2: Purge idempotence
test_curl "$API_URL/api/lunar-returns/dev/purge" "2️⃣ Test purge idempotence (devrait renvoyer deleted_count=0)..."

echo ""
echo "✅ Tests terminés"
