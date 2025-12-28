#!/usr/bin/env zsh

# Script zsh pour récupérer un JWT depuis l'API Astroia Lunar
# Usage:
#   ./scripts/get_token.sh email password
# Exemple:
#   TOKEN=$(./scripts/get_token.sh remi+test1@local.dev 'MonMotDePasse123!')
#   echo ${TOKEN:0:20}

API_URL=http://127.0.0.1:8000

EMAIL=$1
PASSWORD=$2

if [ -z "$EMAIL" ] || [ -z "$PASSWORD" ]; then
  echo 'Usage: ./scripts/get_token.sh email password' >&2
  exit 1
fi

RESPONSE=$(curl -s -X POST $API_URL/api/auth/login \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d username="$EMAIL" \
  -d password="$PASSWORD")

# Parser la réponse JSON et extraire le token
# Utiliser un fichier temporaire pour éviter les problèmes de quoting
TOKEN=$(echo "$RESPONSE" | python3 -c "
import sys
import json

try:
    data = sys.stdin.read()
    if not data:
        sys.exit(1)
    parsed = json.loads(data)
    token = parsed.get('access_token')
    if not token:
        detail = parsed.get('detail', '')
        if detail:
            sys.stderr.write('Erreur login: ' + detail + '\n')
        sys.exit(1)
    print(token, end='')
except json.JSONDecodeError:
    sys.stderr.write('Erreur: réponse JSON invalide\n')
    sys.exit(1)
except Exception as e:
    sys.stderr.write('Erreur: ' + str(e) + '\n')
    sys.exit(1)
")

if [ $? -ne 0 ] || [ -z "$TOKEN" ]; then
  exit 1
fi

echo "$TOKEN"
