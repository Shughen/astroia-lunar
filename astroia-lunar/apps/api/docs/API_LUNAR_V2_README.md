# API Lunar V2 - Guide d'utilisation

## 📚 Documentation

### Fichiers disponibles

1. **`API_LUNAR_V2.md`** - Documentation complète de l'API
   - Introduction et architecture
   - Authentification
   - 3 endpoints documentés avec exemples
   - Modèles de données
   - Codes d'erreur
   - Exemples TypeScript/React Native
   - Guide de migration V1→V2

2. **`API_LUNAR_V2_TESTS.sh`** - Script de tests cURL automatisé
   - Tests des 3 endpoints principaux
   - Vérification des metadata V2
   - Validation des réponses

## 🧪 Tester l'API

### Prérequis

1. API en cours d'exécution :
```bash
cd apps/api
uvicorn main:app --reload
```

2. Utilisateur de test créé (ou utilisez vos credentials)

### Lancer les tests

```bash
cd apps/api/docs

# Avec valeurs par défaut
./API_LUNAR_V2_TESTS.sh

# Avec credentials personnalisés
TEST_EMAIL="your@email.com" TEST_PASSWORD="yourpass" ./API_LUNAR_V2_TESTS.sh

# Avec API distante
API_URL="https://api.astroia.app" TEST_EMAIL="your@email.com" TEST_PASSWORD="yourpass" ./API_LUNAR_V2_TESTS.sh
```

### Output attendu

```
🧪 Tests API Lunar V2
=====================
API URL: http://localhost:8000

[1/5] Health check...
✅ API is running

[2/5] Login...
✅ Login successful
Token: <JWT_TOKEN_REDACTED>

[3/5] GET /api/lunar-returns/current/report...
✅ Current report retrieved
   Source: claude
   Model: claude-opus-4-5-20251101

[4/5] POST /api/lunar/interpretation/regenerate...
✅ Interpretation regenerated
   Forced: true ✓

[5/5] GET /api/lunar/interpretation/metadata...
✅ Metadata retrieved
   Total interpretations: 42
   Cached rate: 85.7%

================================
✅ Tests terminés
================================
```

## 📖 Utilisation de la documentation

### Pour les développeurs frontend

1. Lire **Section 3 (Endpoints)** pour comprendre les routes disponibles
2. Consulter **Section 6 (Exemples d'utilisation)** pour les code examples TypeScript
3. Lire **Section 7 (Migration V1→V2)** si migration depuis V1

### Pour les développeurs backend

1. Lire **Section 1 (Introduction)** pour comprendre l'architecture V2
2. Consulter **Section 4 (Modèles de données)** pour les schémas DB
3. Référence : `docs/LUNAR_ARCHITECTURE_V2.md` pour détails architecture

### Pour les testeurs

1. Utiliser le script `API_LUNAR_V2_TESTS.sh` pour tests automatisés
2. Consulter **Section 5 (Codes d'erreur)** pour debugging
3. Modifier les exemples cURL selon vos besoins

## 🔗 Ressources supplémentaires

- **Architecture V2** : `LUNAR_ARCHITECTURE_V2.md`
- **Plan migration** : `MIGRATION_PLAN.md`
- **Monitoring** : `MONITORING.md` (à créer - Vague 5 Task 5.1)
- **Code source** :
  - Generator : `services/lunar_interpretation_generator.py`
  - Routes : `routes/lunar_returns.py`, `routes/lunar.py`
  - Modèles : `models/lunar_interpretation.py`

## ❓ Troubleshooting

### API not accessible

```bash
# Vérifier que l'API tourne
curl http://localhost:8000/health

# Si erreur, démarrer l'API
cd apps/api
uvicorn main:app --reload
```

### Login failed

```bash
# Créer un utilisateur de test
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123","name":"Test User"}'
```

### No lunar return found (404)

```bash
# Créer un thème natal d'abord
curl -X POST http://localhost:8000/api/natal-chart \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "birth_date": "1990-01-01",
    "birth_time": "12:00",
    "birth_place": "Paris, France",
    "latitude": 48.8566,
    "longitude": 2.3522,
    "timezone": "Europe/Paris"
  }'
```

## 📝 Notes

- Les tests utilisent `test@example.com` / `test123` par défaut
- Changez `API_URL`, `TEST_EMAIL`, `TEST_PASSWORD` via variables d'environnement
- Le script teste automatiquement les 3 endpoints principaux V2
- Tous les exemples sont validés contre le code source actuel

## ✅ Validation

Cette documentation a été générée et validée le **2026-01-23** dans le cadre de la **Vague 5 - Task 5.2** du Sprint 5.

**Status** : ✅ Complète et prête pour production

**Agent responsable** : Agent B (Documentation API Utilisateur)
