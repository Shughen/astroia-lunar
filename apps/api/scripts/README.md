# Scripts de Test - Lunar Returns

## Test de Concurrence

### Description

Script de test pour valider le comportement de `GET /api/lunar-returns/current` en situation de concurrence:
- Lazy generate si DB vide
- Pas de duplication (une seule génération)
- Advisory lock PostgreSQL fonctionne (appels concurrents ne génèrent pas 2 fois)
- `return_date` jamais null
- Appels simultanés renvoient le même `lunar_return` (même id) après génération

### Prérequis

1. **Variables d'environnement:**
   ```bash
   export DEV_MOCK_EPHEMERIS=1
   export LUNAR_RETURNS_DEV_DELAY_MS=2000  # Délai pour rendre le lock observable
   export ALLOW_DEV_PURGE=1  # Pour activer la route /dev/purge
   ```

2. **Mode JWT (avec email/password):**
   ```bash
   python scripts/test_lunar_returns_concurrency.py <email> <password> [API_URL] [--concurrent N] [--delay-ms MS]
   ```

3. **Mode DEV_AUTH_BYPASS:**
   ```bash
   export DEV_AUTH_BYPASS=1
   export DEV_USER_ID=<UUID_STRING>  # UUID string (ex: "550e8400-e29b-41d4-a716-446655440000")
   python scripts/test_lunar_returns_concurrency.py --dev-user-id <UUID_STRING> [API_URL] [--concurrent N] [--delay-ms MS]
   ```
   
   **Note:** `--dev-user-id` accepte maintenant UUID string (recommandé pour Supabase) ou int string. Le script utilise `X-Dev-External-Id` header qui gère UUID via `resolve_dev_user()`.

### Options

- `--api-url URL`: URL de l'API (défaut: http://127.0.0.1:8000)
- `--email EMAIL`: Email pour login (requis en mode JWT)
- `--password PASSWORD`: Password pour login (requis en mode JWT)
- `--dev-user-id ID`: User ID (UUID string, int string, ou autre) pour DEV_AUTH_BYPASS
- `--concurrent N`: Nombre de requêtes concurrentes (défaut: 10)
- `--delay-ms MS`: Override `LUNAR_RETURNS_DEV_DELAY_MS` (ms)
- `--no-purge`: Ne pas purger les lunar returns avant test

### Exemples d'utilisation

```bash
# 1. Configuration
export DEV_MOCK_EPHEMERIS=1
export LUNAR_RETURNS_DEV_DELAY_MS=2000
export ALLOW_DEV_PURGE=1

# 2. Test avec JWT
python scripts/test_lunar_returns_concurrency.py \
  --email test@example.com \
  --password password \
  --api-url http://127.0.0.1:8000 \
  --concurrent 10

# 3. Test avec DEV_AUTH_BYPASS (UUID string)
export DEV_AUTH_BYPASS=1
export DEV_USER_ID="550e8400-e29b-41d4-a716-446655440000"
python scripts/test_lunar_returns_concurrency.py \
  --dev-user-id "550e8400-e29b-41d4-a716-446655440000" \
  --api-url http://127.0.0.1:8000 \
  --concurrent 10

# 4. Test avec DEV_AUTH_BYPASS (string custom)
export DEV_AUTH_BYPASS=1
export DEV_USER_ID="dev-remi"
python scripts/test_lunar_returns_concurrency.py \
  --dev-user-id "dev-remi" \
  --api-url http://127.0.0.1:8000 \
  --concurrent 10
```

### Output attendu

```
======================================================================
🧪 Test de Concurrence: GET /api/lunar-returns/current
======================================================================
API URL: http://127.0.0.1:8000
Mode: JWT
Concurrent requests: 10
DEV delay: 2000ms
DEV_MOCK_EPHEMERIS: 1

1️⃣  Login...
   ✅ Token obtenu: eyJhbGciOiJIUzI1NiIsIn...

2️⃣  Purge des lunar returns existants...
   ✅ Purge effectuée via /dev/purge

3️⃣  Premier batch: 10 requêtes concurrentes (DB vide → lazy generate)...
   🚀 Lancement de 10 requêtes concurrentes...
   ✅ OK: 10 requêtes, même id=42, return_date non-null partout

4️⃣  Deuxième batch: 10 requêtes concurrentes (après génération)...
   🚀 Lancement de 10 requêtes concurrentes...
   ✅ OK: 10 requêtes, même id=42, return_date non-null partout

5️⃣  Vérification cohérence entre batches...
   ✅ Même id dans les deux batches: 42

======================================================================
✅ Tests terminés: SUCCÈS
======================================================================

📋 Vérifications:
   - Premier batch: ✅
   - Deuxième batch: ✅
   - Même id entre batches: ✅

📝 Logs API à vérifier:
   - '[corr=...] 🚀 DB vide → déclenchement génération rolling automatique (lock acquis: X)'
   - '[corr=...] 🧪 DEV delay activé: 2000ms'
   - '[corr=...] ℹ️ Lock non obtenu (user_id=X), un autre process génère déjà → skip'
   - '[corr=...] ✅ Génération rolling automatique terminée: X retour(s)'
```

### Vérifications dans les logs API

Chercher dans les logs du serveur:
- `[corr=...] 🚀 DB vide → déclenchement génération rolling automatique (lock acquis: X)` → génération déclenchée
- `[corr=...] 🧪 DEV delay activé: 2000ms` → délai appliqué
- `[corr=...] ℹ️ Lock non obtenu (user_id=X), un autre process génère déjà → skip` → protection concurrence active
- `[corr=...] ✅ Génération rolling automatique terminée: X retour(s)` → génération réussie

### Notes importantes

1. **Délai DEV:** `LUNAR_RETURNS_DEV_DELAY_MS` doit être > 0 pour observer le lock (recommandé: 2000ms)
2. **Purge:** La route `/dev/purge` nécessite `ALLOW_DEV_PURGE=1` pour des raisons de sécurité
3. **Production:** Ne jamais activer `LUNAR_RETURNS_DEV_DELAY_MS` en production (défaut: 0)
4. **Remise à zéro:** Après les tests, remettre `LUNAR_RETURNS_DEV_DELAY_MS=0` ou non défini

### Dépannage

- **Erreur "Route non disponible":** Vérifier que `ALLOW_DEV_PURGE=1`
- **Tous les IDs différents:** Le lock ne fonctionne pas ou le délai est trop court
- **return_date null:** Vérifier que le fallback fonctionne (devrait être au 15 du mois à 12:00 UTC)
- **Timeout:** Augmenter le timeout dans le script ou réduire `--concurrent`

