# Runbook: Test de concurrence GET /api/lunar-returns/current

## Prérequis

- Backend FastAPI lancé et accessible sur `http://127.0.0.1:8000`
- Base de données accessible
- Utilisateur test avec thème natal existant (pour génération des lunar returns)
- Script `test_lunar_returns_concurrency.py` disponible

---

## Étape 1: Purge des lunar returns (via /dev/purge)

```bash
cd apps/api

# Exporter variables pour purge
export APP_ENV=development
export DEV_AUTH_BYPASS=1
export ALLOW_DEV_PURGE=1

# Purge via curl (remplacer "dev-test" par votre dev_user_id)
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: dev-test" \
  -H "Content-Type: application/json" \
  | jq
```

**Résultat attendu**: JSON avec `"deleted_count"` et `"count_after": 0`

**OU** laisser le script faire la purge automatiquement (étape 2).

---

## Étape 2: Exporter les variables d'environnement

```bash
cd apps/api

# Variables requises pour le test
export APP_ENV=development
export DEV_AUTH_BYPASS=1
export ALLOW_DEV_PURGE=1
export DEV_MOCK_EPHEMERIS=1
export LUNAR_RETURNS_DEV_DELAY_MS=2000

# Optionnel: définir DEV_USER_ID si vous voulez utiliser celui-ci au lieu de --dev-user-id
export DEV_USER_ID="dev-test"  # UUID string, int string, ou autre

# Vérifier les exports
echo "APP_ENV=$APP_ENV"
echo "DEV_AUTH_BYPASS=$DEV_AUTH_BYPASS"
echo "ALLOW_DEV_PURGE=$ALLOW_DEV_PURGE"
echo "DEV_MOCK_EPHEMERIS=$DEV_MOCK_EPHEMERIS"
echo "LUNAR_RETURNS_DEV_DELAY_MS=$LUNAR_RETURNS_DEV_DELAY_MS"
echo "DEV_USER_ID=$DEV_USER_ID"
```

**Résultat attendu**: Toutes les variables affichées avec les bonnes valeurs.

**Note**: `LUNAR_RETURNS_DEV_DELAY_MS=2000` ralentit la génération de 2 secondes pour rendre le lock observable.

---

## Étape 3: Lancer le script de test de concurrence

```bash
cd apps/api

# Activer venv si nécessaire
source .venv/bin/activate

# Lancer le test avec 10 requêtes concurrentes
python scripts/test_lunar_returns_concurrency.py \
  --dev-user-id "dev-test" \
  --api-url http://127.0.0.1:8000 \
  --concurrent 10
```

**Options disponibles:**
- `--dev-user-id`: ID utilisateur pour DEV_AUTH_BYPASS (string, UUID, ou int)
- `--api-url`: URL de l'API (défaut: `http://127.0.0.1:8000`)
- `--concurrent N`: Nombre de requêtes concurrentes (défaut: 10)
- `--delay-ms MS`: Override `LUNAR_RETURNS_DEV_DELAY_MS` (ms)
- `--no-purge`: Ne pas purger avant le test (si vous voulez purger manuellement)

**Exemple avec override du délai:**

```bash
python scripts/test_lunar_returns_concurrency.py \
  --dev-user-id "dev-test" \
  --api-url http://127.0.0.1:8000 \
  --concurrent 10 \
  --delay-ms 3000
```

---

## Étape 4: Observer les résultats

### Sortie console attendue

```
======================================================================
🧪 Test de Concurrence: GET /api/lunar-returns/current
======================================================================
API URL: http://127.0.0.1:8000
Mode: DEV_AUTH_BYPASS (--dev-user-id=dev-test)
DEV User ID: dev-test (string)
Concurrent requests: 10
DEV delay: 2000ms
DEV_MOCK_EPHEMERIS: 1

1️⃣  Mode DEV_AUTH_BYPASS activé (pas de login)

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

### Exit code

- **0**: Succès (tous les critères validés)
- **1**: Échec (IDs différents, erreurs, ou return_date null)

---

## Étape 5: Critères de succès

### ✅ Critère 1: 10/10 réponses OK

**Vérification**: Toutes les requêtes retournent HTTP 200 OK.

**Dans la sortie console:**
```
✅ OK: 10 requêtes, même id=42, return_date non-null partout
```

**Si échec:**
```
❌ Erreurs: ['req_0: status=500', 'req_1: payload null', ...]
```

### ✅ Critère 2: Même lunar_return.id

**Vérification**: Tous les IDs retournés sont identiques.

**Dans la sortie console:**
```
✅ OK: 10 requêtes, même id=42, return_date non-null partout
```

**Si échec:**
```
❌ IDs différents: {42, 43, 44}
```

### ✅ Critère 3: Aucun doublon en DB (user_id, month)

**Requête SQL de vérification:**

```bash
# Charger DATABASE_URL depuis .env
cd apps/api
export $(grep -v '^#' .env | grep DATABASE_URL | xargs)

# Vérifier l'absence de doublons
psql "$DATABASE_URL" -c "
SELECT 
    user_id, 
    month, 
    COUNT(*) as count,
    array_agg(id ORDER BY id) as ids
FROM public.lunar_returns
WHERE user_id = (
    SELECT id FROM users WHERE email LIKE '%test%' LIMIT 1
    -- OU utiliser directement votre user_id si connu
    -- WHERE user_id = 42
)
GROUP BY user_id, month
HAVING COUNT(*) > 1
ORDER BY count DESC, user_id, month;
"
```

**Résultat attendu**: Aucune ligne (0 doublons).

**Si doublons détectés:**
```
 user_id |  month   | count |      ids      
---------+----------+-------+---------------
      42 | 2024-01  |     2 | {100, 101}
      42 | 2024-02  |     2 | {102, 103}
```

**Requête alternative (tous les utilisateurs):**

```bash
psql "$DATABASE_URL" -c "
SELECT 
    user_id, 
    month, 
    COUNT(*) as count
FROM public.lunar_returns
GROUP BY user_id, month
HAVING COUNT(*) > 1
ORDER BY count DESC, user_id, month;
"
```

---

## Étape 6: Vérification des logs serveur

Dans les logs du backend, vous devez voir:

### Logs de génération (premier batch)

```
INFO:     [corr=<uuid1>] 🚀 DB vide → déclenchement génération rolling automatique (lock acquis: 42)
INFO:     [corr=<uuid1>] 🧪 DEV delay activé: 2000ms
INFO:     [corr=<uuid1>] 📅 Génération rolling automatique: 2024-01 à 2024-12
INFO:     [corr=<uuid1>] ✅ Génération rolling automatique terminée: 12 retour(s)
INFO:     [corr=<uuid1>] 🔓 Lock libéré: 42
```

### Logs de lock non obtenu (autres requêtes du premier batch)

```
INFO:     [corr=<uuid2>] ℹ️ Lock non obtenu (user_id=42), un autre process génère déjà → skip
INFO:     [corr=<uuid3>] ℹ️ Lock non obtenu (user_id=42), un autre process génère déjà → skip
...
```

### Logs de re-sélection (après génération)

```
INFO:     [corr=<uuid2>] 🔄 Re-recherche après tentative génération (generated=False)...
INFO:     [corr=<uuid2>] ✅ Révolution lunaire trouvée: 2024-01 (return_date=2024-01-15T12:00:00+00:00)
```

---

## Checklist de validation

- [ ] Variables d'environnement exportées (`APP_ENV`, `DEV_AUTH_BYPASS`, `ALLOW_DEV_PURGE`, `LUNAR_RETURNS_DEV_DELAY_MS`, `DEV_MOCK_EPHEMERIS`)
- [ ] Backend lancé et accessible
- [ ] Purge effectuée (via curl ou script)
- [ ] Script lancé avec `--concurrent 10`
- [ ] **Critère 1**: 10/10 réponses OK (HTTP 200)
- [ ] **Critère 2**: Même `lunar_return.id` dans toutes les réponses
- [ ] **Critère 3**: Aucun doublon en DB (requête SQL retourne 0 lignes)
- [ ] Logs serveur montrent: lock acquis, delay activé, génération unique
- [ ] Exit code du script = 0 (succès)

---

## Commandes rapides (tout-en-un)

```bash
# 1. Setup environnement
cd apps/api
export APP_ENV=development
export DEV_AUTH_BYPASS=1
export ALLOW_DEV_PURGE=1
export DEV_MOCK_EPHEMERIS=1
export LUNAR_RETURNS_DEV_DELAY_MS=2000
export DEV_USER_ID="dev-test"

# 2. Purge (optionnel, le script le fait automatiquement)
curl -X POST http://127.0.0.1:8000/api/lunar-returns/dev/purge \
  -H "X-Dev-External-Id: dev-test" \
  | jq

# 3. Lancer le test
source .venv/bin/activate
python scripts/test_lunar_returns_concurrency.py \
  --dev-user-id "dev-test" \
  --api-url http://127.0.0.1:8000 \
  --concurrent 10

# 4. Vérifier doublons en DB (après test)
export $(grep -v '^#' .env | grep DATABASE_URL | xargs)
psql "$DATABASE_URL" -c "
SELECT user_id, month, COUNT(*) as count
FROM public.lunar_returns
GROUP BY user_id, month
HAVING COUNT(*) > 1;
"
```

---

## Dépannage

### Problème: Script retourne "Lock non obtenu" mais génération échoue

**Cause:** Le lock est libéré trop tôt ou la génération échoue.

**Solution:**
```bash
# Vérifier les logs serveur pour erreurs
# Vérifier que DEV_MOCK_EPHEMERIS=1
# Vérifier que le thème natal existe pour l'utilisateur test
```

### Problème: IDs différents dans les réponses

**Cause:** Génération concurrente non protégée ou contrainte UNIQUE absente.

**Solution:**
```bash
# Vérifier que la migration UNIQUE est appliquée
psql "$DATABASE_URL" -c "
SELECT indexname FROM pg_indexes 
WHERE tablename = 'lunar_returns' 
AND indexname = 'uq_lunar_returns_user_month';
"

# Si absent, appliquer la migration
psql "$DATABASE_URL" -f migrations/add_unique_constraint_lunar_returns_user_month.sql
```

### Problème: Doublons détectés en DB

**Cause:** Contrainte UNIQUE absente ou migration non appliquée.

**Solution:**
```bash
# 1. Lister les doublons
psql "$DATABASE_URL" -c "
SELECT user_id, month, COUNT(*), array_agg(id)
FROM public.lunar_returns
GROUP BY user_id, month
HAVING COUNT(*) > 1;
"

# 2. Supprimer les doublons (garder le plus récent)
psql "$DATABASE_URL" -c "
DELETE FROM public.lunar_returns lr1
WHERE EXISTS (
    SELECT 1 FROM public.lunar_returns lr2
    WHERE lr2.user_id = lr1.user_id
      AND lr2.month = lr1.month
      AND lr2.id > lr1.id
);
"

# 3. Appliquer la migration
psql "$DATABASE_URL" -f migrations/add_unique_constraint_lunar_returns_user_month.sql
```

### Problème: LUNAR_RETURNS_DEV_DELAY_MS non pris en compte

**Cause:** Variable non exportée ou backend pas redémarré.

**Solution:**
```bash
# Vérifier que la variable est bien exportée
echo "LUNAR_RETURNS_DEV_DELAY_MS=$LUNAR_RETURNS_DEV_DELAY_MS"

# Redémarrer le backend après export
# (Arrêter avec CTRL+C puis relancer)
```

---

## Notes

- Le script fait **automatiquement** la purge via `/dev/purge` (sauf si `--no-purge`)
- Le script lance **2 batches** de requêtes concurrentes:
  - **Batch 1**: DB vide → doit déclencher lazy generation
  - **Batch 2**: Après génération → doit retourner même id, pas de re-génération
- Le `LUNAR_RETURNS_DEV_DELAY_MS` ralentit la génération pour rendre le lock observable
- Après les tests, **remettre `LUNAR_RETURNS_DEV_DELAY_MS=0`** ou non défini (ne pas laisser en production)

