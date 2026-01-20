# Hardening: Validation du schéma DB et prévention de régression

**Date:** 2025-01-XX  
**Objectif:** Prévenir les bugs de type (UUID vs INTEGER) entre le schéma DB et les modèles SQLAlchemy

---

## 📋 Résumé des changements

### 1. Script SQL d'introspection

**Fichier:** `scripts/sql/inspect_core_schema.sql`

Script pour vérifier les types de colonnes critiques:
- `natal_charts.id` → uuid
- `natal_charts.user_id` → integer
- `lunar_returns.id` → integer
- `lunar_returns.user_id` → integer

**Usage:**
```bash
psql $DATABASE_URL -f apps/api/scripts/sql/inspect_core_schema.sql
```

---

### 2. Schema Sanity Check

**Fichier:** `utils/schema_sanity_check.py`

Fonction `check_schema_sanity()` qui:
- Vérifie que les types DB correspondent aux attentes
- Retourne une liste d'erreurs si mismatch
- Utilise `correlation_id` pour le logging

**Intégration:**
- **Au démarrage** (`main.py` lifespan): vérifie le schéma et fail-fast en dev si problème
- **Endpoint `/health/db`**: endpoint admin pour vérifier l'état du schéma

**Comportement:**
- **Dev mode**: Fail-fast si mismatch détecté (serveur ne démarre pas)
- **Prod mode**: Log ERROR mais continue (pour éviter de bloquer en prod si DB temporairement inaccessible)

---

### 3. Tests unitaires

**Fichier:** `tests/test_lunar_returns.py`

Trois tests ajoutés:

1. **`test_generate_lunar_returns_201_when_natal_exists`**
   - Vérifie que POST `/api/lunar-returns/generate` renvoie 201 quand natal_chart existe (mode mock)

2. **`test_generate_lunar_returns_error_json_structure`**
   - Vérifie que les erreurs ont la structure JSON `{detail, step, correlation_id}`
   - Force une erreur (natal_chart manquant) et vérifie la réponse 404

3. **`test_lunar_return_user_id_is_integer`**
   - Vérifie que `LunarReturn.user_id` est bien INTEGER dans le modèle SQLAlchemy
   - Vérifie que le type de colonne est `Integer` (pas UUID)

**Fichier:** `tests/test_health.py`

Test ajouté:
- **`test_health_db_endpoint`**: Vérifie que `/health/db` renvoie une réponse valide

**Exécution:**
```bash
cd apps/api
pytest tests/test_lunar_returns.py -v
pytest tests/test_health.py -v
```

---

### 4. Documentation des migrations

**Fichier:** `DB_SCHEMA_NOTES.md`

Ajout d'une section importante:

**⚠️ RÈGLE CRITIQUE:**
- **`user_id` doit être INTEGER partout** dans toutes les tables qui référencent `users.id`
- Ne jamais utiliser UUID pour `user_id` (même si `id` peut être UUID)
- Toujours vérifier l'alignement après une migration en utilisant `scripts/sql/inspect_core_schema.sql`

**Migrations documentées:**
- `natal_charts.user_id` (UUID → INTEGER)
- `lunar_returns.user_id` (UUID → INTEGER)

---

### 5. Policies RLS recommandées

**Fichier:** `scripts/sql/rls_policies_recommended.sql`

Analyse et recommandations pour les policies RLS:

**Problème identifié:**
- Policies actuelles utilisent `auth.jwt() ->> 'email'` puis SELECT pour trouver `users.id`
- C'est inefficace et fragile (email peut changer)

**Recommandations:**
1. **Option A (si JWT disponible dans PostgreSQL):**
   - Utiliser `current_setting('request.jwt.claims', true)::json ->> 'sub'` pour extraire directement `users.id`
   - Comparer `user_id = (sub::integer)`

2. **Option B (recommandé pour FastAPI standalone):**
   - Désactiver RLS
   - Gérer l'accès côté application via `get_current_user()` qui vérifie le JWT
   - Plus simple et évite les problèmes de synchronisation JWT

**Note:** Le script contient les deux options avec commentaires explicatifs.

---

## ✅ Checklist de validation E2E

### 1. Schema Sanity Check au démarrage

```bash
cd apps/api
uvicorn main:app --reload
```

**Attendu:**
- Si schéma correct: `✅ Schema sanity check OK au démarrage`
- Si schéma incorrect (dev): serveur ne démarre pas avec erreur claire
- Si schéma incorrect (prod): log ERROR mais serveur démarre

### 2. Endpoint /health/db

```bash
curl http://localhost:8000/health/db | jq
```

**Attendu:**
```json
{
  "status": "healthy",
  "correlation_id": "...",
  "checks": {
    "database_connection": "ok",
    "schema_sanity": "ok"
  },
  "errors": []
}
```

Si problème:
```json
{
  "status": "unhealthy",
  "checks": {
    "schema_sanity": "failed"
  },
  "errors": [
    {
      "table": "lunar_returns",
      "column": "user_id",
      "message": "Type mismatch: lunar_returns.user_id devrait être integer/int4, mais est uuid/uuid"
    }
  ]
}
```

### 3. Script SQL d'introspection

```bash
psql $DATABASE_URL -f apps/api/scripts/sql/inspect_core_schema.sql
```

**Attendu:**
```
 table_name    | column_name | data_type | udt_name | is_nullable | column_default
---------------+-------------+-----------+----------+-------------+----------------
 lunar_returns | id          | integer   | int4     | NO          | nextval(...)
 lunar_returns | user_id     | integer   | int4     | NO          | NULL
 natal_charts  | id          | uuid      | uuid     | NO          | gen_random_uuid()
 natal_charts  | user_id     | integer   | int4     | NO          | NULL
```

### 4. Tests unitaires

```bash
cd apps/api
pytest tests/test_lunar_returns.py::test_lunar_return_user_id_is_integer -v
pytest tests/test_health.py::test_health_db_endpoint -v
```

**Attendu:** Tous les tests passent

### 5. Test E2E complet (mode mock)

```bash
cd apps/api
./scripts/e2e_mock.sh remi.beaurain@gmail.com 'MonMotDePasse123!'
```

**Attendu:**
- ✅ Login OK
- ✅ Création natal_chart (201)
- ✅ Génération lunar returns (201)

---

## 🔧 Maintenance future

### Après chaque migration SQL

1. Exécuter `scripts/sql/inspect_core_schema.sql` pour vérifier les types
2. Redémarrer l'app et vérifier les logs: `✅ Schema sanity check OK`
3. Tester `/health/db` pour confirmer que tout est OK

### Ajouter une nouvelle colonne critique

1. Ajouter l'entrée dans `EXPECTED_SCHEMA` dans `utils/schema_sanity_check.py`
2. Mettre à jour `scripts/sql/inspect_core_schema.sql` si nécessaire
3. Ajouter un test unitaire si applicable

---

## 📝 Notes techniques

### Correlation ID

Tous les logs et erreurs utilisent `correlation_id` pour le tracking:
- Généré via `uuid.uuid4()`
- Présent dans les logs: `[corr={correlation_id}] ...`
- Présent dans les erreurs JSON: `{..., "correlation_id": "...", ...}`

### Structure d'erreur JSON

Toutes les erreurs renvoient:
```json
{
  "detail": {
    "detail": "Message d'erreur",
    "correlation_id": "uuid",
    "step": "nom_de_l_etape",
    "error_type": "TypeError"  // optionnel
  }
}
```

Ou si FastAPI transforme en string:
```json
{
  "detail": "Message d'erreur"
}
```
(mais `correlation_id` est toujours dans les logs)

---

## 🚀 Prochaines étapes

- [ ] Exécuter les tests en CI/CD
- [ ] Ajouter un test d'intégration qui vérifie réellement la DB (nécessite DB de test)
- [ ] Monitorer les logs de schema sanity check en production
- [ ] Considérer désactiver RLS si l'app FastAPI gère déjà l'autorisation

