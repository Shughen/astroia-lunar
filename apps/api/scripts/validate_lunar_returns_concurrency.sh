#!/bin/bash
set -euo pipefail

# Script de validation de la concurrence pour GET /api/lunar-returns/current
# Vérifie: migration UNIQUE, purge, test concurrence, absence de doublons

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
API_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
MIGRATION_FILE="$API_DIR/migrations/add_unique_constraint_lunar_returns_user_month.sql"
BACKEND_PID=""
DEV_USER_ID="${DEV_USER_ID:-1}"  # Doit être un entier pour X-Dev-User-Id
API_URL="${API_URL:-http://127.0.0.1:8000}"
HEALTH_CHECK_URL="${API_URL}/health"
MAX_WAIT_SECONDS=30
CONCURRENT_REQUESTS=10

# Couleurs pour output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonctions utilitaires
log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

pass() {
    echo -e "${GREEN}[PASS]${NC} $1"
}

fail() {
    echo -e "${RED}[FAIL]${NC} $1"
    return 1
}

cleanup() {
    if [ -n "$BACKEND_PID" ] && kill -0 "$BACKEND_PID" 2>/dev/null; then
        log_info "Arrêt du backend (PID: $BACKEND_PID)..."
        kill "$BACKEND_PID" 2>/dev/null || true
        wait "$BACKEND_PID" 2>/dev/null || true
    fi
}

trap cleanup EXIT INT TERM

# ============================================
# Étape 1: Charger .env si présent
# ============================================
log_info "Étape 1: Chargement des variables d'environnement..."

if [ -f "$API_DIR/.env" ]; then
    log_info "Chargement de $API_DIR/.env..."
    set -a
    source "$API_DIR/.env"
    set +a
    pass "Variables d'environnement chargées depuis .env"
else
    log_warn ".env non trouvé, utilisation des variables d'environnement existantes"
fi

# Vérifier les variables critiques
if [ -z "${DATABASE_URL:-}" ]; then
    fail "DATABASE_URL non défini"
    exit 1
fi

# Variables par défaut si non définies
export APP_ENV="${APP_ENV:-development}"
export DEV_AUTH_BYPASS="${DEV_AUTH_BYPASS:-1}"
export ALLOW_DEV_PURGE="${ALLOW_DEV_PURGE:-1}"
export DEV_MOCK_EPHEMERIS="${DEV_MOCK_EPHEMERIS:-1}"
export LUNAR_RETURNS_DEV_DELAY_MS="${LUNAR_RETURNS_DEV_DELAY_MS:-2000}"

# Valider DEV_USER_ID: doit être un entier pour X-Dev-User-Id
if ! [[ "$DEV_USER_ID" =~ ^[0-9]+$ ]]; then
    fail "DEV_USER_ID doit être un entier (reçu: $DEV_USER_ID). Le backend attend X-Dev-User-Id avec un entier."
    exit 1
fi

# Logger DATABASE_URL (masquée) et extraire host/port/dbname si possible
DB_INFO=$(echo "$DATABASE_URL" | sed -E 's|postgresql://[^:]+:[^@]+@([^/]+)/(.+)$|\1/\2|' 2>/dev/null || echo "N/A")
log_info "Variables configurées:"
log_info "  APP_ENV=$APP_ENV"
log_info "  DEV_AUTH_BYPASS=$DEV_AUTH_BYPASS"
log_info "  ALLOW_DEV_PURGE=$ALLOW_DEV_PURGE"
log_info "  DEV_MOCK_EPHEMERIS=$DEV_MOCK_EPHEMERIS"
log_info "  LUNAR_RETURNS_DEV_DELAY_MS=$LUNAR_RETURNS_DEV_DELAY_MS"
log_info "  DEV_USER_ID=$DEV_USER_ID (entier validé)"
log_info "  DATABASE_URL: postgresql://***@$DB_INFO"

# Sanity check DB: vérifier que la connexion fonctionne
log_info "Vérification de la connexion DB..."
if ! psql "$DATABASE_URL" -c "SELECT 1" >/dev/null 2>&1; then
    fail "Impossible de se connecter à la base de données (sanity check échoué)"
    log_error "Vérifiez DATABASE_URL et que PostgreSQL est accessible"
    exit 1
fi
pass "Connexion DB OK"

# ============================================
# Étape 2: Appliquer la migration UNIQUE
# ============================================
log_info "Étape 2: Application de la migration UNIQUE..."

if [ ! -f "$MIGRATION_FILE" ]; then
    fail "Fichier de migration non trouvé: $MIGRATION_FILE"
    exit 1
fi

# Vérifier si l'index existe déjà
INDEX_EXISTS=$(psql "$DATABASE_URL" -tAc "
    SELECT COUNT(*) FROM pg_indexes 
    WHERE tablename = 'lunar_returns' 
    AND indexname = 'uq_lunar_returns_user_month';
" 2>/dev/null || echo "0")

if [ "$INDEX_EXISTS" = "1" ]; then
    pass "Index UNIQUE déjà présent (skip migration)"
else
    log_info "Application de la migration..."
    if psql "$DATABASE_URL" -f "$MIGRATION_FILE" >/dev/null 2>&1; then
        pass "Migration appliquée avec succès"
    else
        fail "Erreur lors de l'application de la migration"
        exit 1
    fi
    
    # Vérifier que l'index existe maintenant
    INDEX_EXISTS_AFTER=$(psql "$DATABASE_URL" -tAc "
        SELECT COUNT(*) FROM pg_indexes 
        WHERE tablename = 'lunar_returns' 
        AND indexname = 'uq_lunar_returns_user_month';
    " 2>/dev/null || echo "0")
    
    if [ "$INDEX_EXISTS_AFTER" = "1" ]; then
        pass "Index UNIQUE vérifié en DB"
    else
        fail "Index UNIQUE non trouvé après migration"
        exit 1
    fi
fi

# ============================================
# Étape 3: Lancer le backend en background
# ============================================
log_info "Étape 3: Lancement du backend..."

cd "$API_DIR"

# Vérifier si le backend est déjà lancé
EXISTING_BACKEND_PID=""
if curl -s "$HEALTH_CHECK_URL" >/dev/null 2>&1; then
    log_warn "Backend déjà lancé sur $API_URL"
    
    # Identifier le PID du processus sur le port 8000
    if command -v lsof >/dev/null 2>&1; then
        EXISTING_BACKEND_PID=$(lsof -ti :8000 2>/dev/null || echo "")
    fi
    
    # Fallback: chercher via ps aux | grep uvicorn
    if [ -z "$EXISTING_BACKEND_PID" ]; then
        EXISTING_BACKEND_PID=$(ps aux | grep -E '[u]vicorn.*main:app' | awk '{print $2}' | head -n1 || echo "")
    fi
    
    if [ -n "$EXISTING_BACKEND_PID" ]; then
        log_info "PID backend existant détecté: $EXISTING_BACKEND_PID"
        
        # Vérifier l'option KEEP_RUNNING_BACKEND
        if [ "${KEEP_RUNNING_BACKEND:-0}" = "1" ]; then
            log_warn "KEEP_RUNNING_BACKEND=1 → conservation du backend existant"
            pass "Backend accessible (conservé)"
        else
            log_info "Arrêt du backend existant pour relancer avec les bonnes env vars..."
            kill "$EXISTING_BACKEND_PID" 2>/dev/null || true
            sleep 2
            
            # Vérifier que le processus est bien arrêté
            if kill -0 "$EXISTING_BACKEND_PID" 2>/dev/null; then
                log_warn "Processus encore actif, kill -9..."
                kill -9 "$EXISTING_BACKEND_PID" 2>/dev/null || true
                sleep 1
            fi
            
            # Vérifier que le port est libéré
            if curl -s "$HEALTH_CHECK_URL" >/dev/null 2>&1; then
                log_warn "Backend toujours accessible, attente supplémentaire..."
                sleep 3
            fi
            
            pass "Backend existant arrêté"
        fi
    else
        log_warn "Backend accessible mais PID non identifié (peut être un autre service)"
    fi
fi

# Lancer le backend si nécessaire (pas déjà lancé OU arrêté)
if ! curl -s "$HEALTH_CHECK_URL" >/dev/null 2>&1 || [ "${KEEP_RUNNING_BACKEND:-0}" != "1" ]; then
    # Activer venv si présent
    if [ -d "$API_DIR/.venv" ]; then
        source "$API_DIR/.venv/bin/activate"
    fi
    
    # Lancer le backend en background avec les env vars du script
    log_info "Démarrage de uvicorn avec les env vars configurées..."
    uvicorn main:app --reload --port 8000 --host 0.0.0.0 >/tmp/astroia_backend.log 2>&1 &
    BACKEND_PID=$!
    
    # Attendre que le backend réponde
    log_info "Attente du démarrage du backend (max ${MAX_WAIT_SECONDS}s)..."
    WAIT_COUNT=0
    while [ $WAIT_COUNT -lt $MAX_WAIT_SECONDS ]; do
        if curl -s "$HEALTH_CHECK_URL" >/dev/null 2>&1; then
            pass "Backend accessible sur $API_URL"
            break
        fi
        sleep 1
        WAIT_COUNT=$((WAIT_COUNT + 1))
        echo -n "."
    done
    echo ""
    
    if [ $WAIT_COUNT -ge $MAX_WAIT_SECONDS ]; then
        fail "Backend non accessible après ${MAX_WAIT_SECONDS}s"
        log_error "Logs backend:"
        tail -20 /tmp/astroia_backend.log 2>/dev/null || true
        exit 1
    fi
    
    # Attendre un peu plus pour que le backend soit complètement prêt
    sleep 2
fi

# ============================================
# Étape 4: Provisioning DEV user + natal chart
# ============================================
log_info "Étape 4: Provisioning DEV user et natal chart..."

cd "$API_DIR"

# Activer venv si présent
if [ -d "$API_DIR/.venv" ]; then
    source "$API_DIR/.venv/bin/activate"
fi

# Définir PYTHON_CMD de façon déterministe
if [ -f "$API_DIR/.venv/bin/python" ]; then
    PYTHON_CMD="$API_DIR/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Exécuter le script de provisioning
if "$PYTHON_CMD" "$API_DIR/scripts/ensure_dev_user_and_natal.py" >/tmp/provisioning.log 2>&1; then
    pass "Provisioning DEV user et natal chart réussi"
else
    fail "Erreur lors du provisioning DEV user et natal chart"
    log_error "Logs du provisioning:"
    tail -20 /tmp/provisioning.log
    exit 1
fi

# ============================================
# Étape 5: Purge via /dev/purge
# ============================================
log_info "Étape 5: Purge des lunar returns via /dev/purge..."

# Utiliser X-Dev-User-Id (entier) au lieu de X-Dev-External-Id
PURGE_RESPONSE=$(curl -s -w "\n%{http_code}" -X POST "$API_URL/api/lunar-returns/dev/purge" \
    -H "X-Dev-User-Id: $DEV_USER_ID" \
    -H "Content-Type: application/json" 2>/dev/null || echo -e "\n000")

# Extraire HTTP code (dernière ligne) et body (toutes sauf dernière ligne)
# Utilisation de sed pour compatibilité macOS/Linux (évite head -n -1 qui est GNU-only)
HTTP_CODE=$(printf "%s\n" "$PURGE_RESPONSE" | tail -n 1)
PURGE_BODY=$(printf "%s\n" "$PURGE_RESPONSE" | sed '$d')

if [ "$HTTP_CODE" = "200" ]; then
    DELETED_COUNT=$(echo "$PURGE_BODY" | grep -o '"deleted_count":[0-9]*' | cut -d: -f2 || echo "0")
    pass "Purge effectuée (deleted_count: $DELETED_COUNT)"
else
    fail "Erreur lors de la purge (HTTP $HTTP_CODE)"
    log_error "Header utilisé: X-Dev-User-Id: $DEV_USER_ID"
    log_error "Body de la réponse:"
    echo "$PURGE_BODY" | head -10
    exit 1
fi

# ============================================
# Étape 6: Test de concurrence
# ============================================
log_info "Étape 6: Test de concurrence ($CONCURRENT_REQUESTS requêtes)..."

cd "$API_DIR"

# Définir PYTHON_CMD de façon déterministe
if [ -f "$API_DIR/.venv/bin/python" ]; then
    PYTHON_CMD="$API_DIR/.venv/bin/python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
else
    PYTHON_CMD="python"
fi

# Logger le Python utilisé
log_info "Python utilisé: $PYTHON_CMD"
PYTHON_EXECUTABLE=$("$PYTHON_CMD" -c "import sys; print(sys.executable)" 2>/dev/null || echo "N/A")
log_info "Python executable: $PYTHON_EXECUTABLE"

# Vérifier que aiohttp est installé
log_info "Vérification des dépendances Python..."
if ! "$PYTHON_CMD" -c "import aiohttp" >/dev/null 2>&1; then
    log_warn "aiohttp non trouvé, installation..."
    if [ -f "$API_DIR/.venv/bin/python" ]; then
        "$API_DIR/.venv/bin/pip" install aiohttp >/dev/null 2>&1 || {
            fail "Impossible d'installer aiohttp"
            exit 1
        }
        pass "aiohttp installé"
    else
        fail "aiohttp non installé et pas de venv pour installation automatique"
        log_error "Installez aiohttp: pip install aiohttp"
        exit 1
    fi
fi

# Lancer le script de test (avec verbose si DEBUG=1)
VERBOSE_FLAG=""
if [ "${DEBUG:-0}" = "1" ]; then
    VERBOSE_FLAG="--verbose"
    log_info "Mode DEBUG activé (verbose)"
fi

# Lancer le script de test
if "$PYTHON_CMD" "$SCRIPT_DIR/test_lunar_returns_concurrency.py" \
    --dev-user-id "$DEV_USER_ID" \
    --api-url "$API_URL" \
    --concurrent "$CONCURRENT_REQUESTS" \
    --no-purge \
    $VERBOSE_FLAG >/tmp/concurrency_test.log 2>&1; then
    pass "Test de concurrence réussi"
else
    fail "Test de concurrence échoué"
    log_error "Logs du test:"
    tail -30 /tmp/concurrency_test.log
    exit 1
fi

# ============================================
# Étape 7: Vérification anti-doublons en DB
# ============================================
log_info "Étape 7: Vérification anti-doublons (user_id, month)..."

# Récupérer le user_id depuis la DB (si DEV_USER_ID est un string, on doit le résoudre)
# Pour simplifier, on vérifie tous les utilisateurs
DOUBLONS=$(psql "$DATABASE_URL" -tAc "
    SELECT COUNT(*) 
    FROM (
        SELECT user_id, month, COUNT(*) as count
        FROM public.lunar_returns
        GROUP BY user_id, month
        HAVING COUNT(*) > 1
    ) as duplicates;
" 2>/dev/null || echo "-1")

if [ "$DOUBLONS" = "-1" ]; then
    fail "Erreur lors de la vérification des doublons"
    exit 1
elif [ "$DOUBLONS" = "0" ]; then
    pass "Aucun doublon détecté (user_id, month)"
else
    fail "$DOUBLONS doublon(s) détecté(s) en DB"
    
    # Afficher les doublons
    log_error "Détails des doublons:"
    psql "$DATABASE_URL" -c "
        SELECT user_id, month, COUNT(*) as count, array_agg(id ORDER BY id) as ids
        FROM public.lunar_returns
        GROUP BY user_id, month
        HAVING COUNT(*) > 1
        ORDER BY count DESC, user_id, month;
    "
    exit 1
fi

# ============================================
# Résumé final
# ============================================
echo ""
log_info "=========================================="
log_info "✅ Validation complète: SUCCÈS"
log_info "=========================================="
log_info "Résumé:"
log_info "  - Migration UNIQUE: ✅"
log_info "  - Backend lancé: ✅"
log_info "  - Provisioning DEV: ✅"
log_info "  - Purge effectuée: ✅"
log_info "  - Test concurrence: ✅"
log_info "  - Aucun doublon: ✅"
echo ""

exit 0

