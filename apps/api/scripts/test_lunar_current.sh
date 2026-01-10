#!/bin/bash
# Script de test pour l'endpoint /api/lunar/current
# Calcule la position actuelle de la Lune avec Swiss Ephemeris

echo "🌙 Test de l'endpoint /api/lunar/current"
echo "=========================================="
echo ""

# Vérifier que le serveur est en cours d'exécution
if ! curl -s http://127.0.0.1:8000/health > /dev/null 2>&1; then
    echo "❌ Erreur: Le serveur API n'est pas démarré sur http://127.0.0.1:8000"
    echo "Lancez le serveur avec: cd apps/api && uvicorn main:app --reload"
    exit 1
fi

echo "✅ Serveur API détecté"
echo ""

# Appel 1: Calcul initial (cache miss)
echo "📡 Appel 1: Calcul Swiss Ephemeris (cache miss attendu)..."
RESULT1=$(curl -s http://127.0.0.1:8000/api/lunar/current)
echo "$RESULT1" | python3 -m json.tool
echo ""

# Appel 2: Vérification du cache (cache hit)
echo "📡 Appel 2: Vérification du cache (cache hit attendu)..."
sleep 1
RESULT2=$(curl -s http://127.0.0.1:8000/api/lunar/current)
echo "$RESULT2" | python3 -m json.tool
echo ""

# Vérification que les résultats sont identiques
if [ "$RESULT1" == "$RESULT2" ]; then
    echo "✅ Cache fonctionne correctement (résultats identiques)"
else
    echo "⚠️ Résultats différents (cache peut-être expiré ou erreur)"
fi

echo ""
echo "📖 Documentation de l'endpoint:"
echo "  GET /api/lunar/current"
echo "  Cache serveur: 5 minutes"
echo "  Retour: { sign: string, degree: number, phase: string }"
echo ""
echo "  Phases possibles:"
echo "    - Nouvelle Lune, Premier Croissant, Premier Quartier, Lune Gibbeuse"
echo "    - Pleine Lune, Lune Disseminante, Dernier Quartier, Dernier Croissant"
echo ""
echo "  Signes possibles:"
echo "    - Aries, Taurus, Gemini, Cancer, Leo, Virgo"
echo "    - Libra, Scorpio, Sagittarius, Capricorn, Aquarius, Pisces"
