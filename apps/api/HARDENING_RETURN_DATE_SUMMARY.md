# Hardening return_date: Résumé et checklist

**Date:** 2025-01-XX  
**Objectif:** Prévenir les régressions sur les types de colonnes critiques (user_id INTEGER, return_date timestamptz)

---

## ✅ Implémentation complète

### 1. Schema Sanity Check

**Fichier:** `utils/schema_sanity_check.py`

**Vérifications:**
- ✅ `natal_charts.id` = uuid
- ✅ `natal_charts.user_id` = integer
- ✅ `lunar_returns.id` = integer (pas UUID)
- ✅ `lunar_returns.user_id` = integer
- ✅ `lunar_returns.return_date` = timestamptz

**Intégration:**
- ✅ Au démarrage (`main.py` lifespan): fail-fast en dev si mismatch
- ✅ Endpoint `/health/db`: vérification admin à la demande

**Erreurs structurées:**
- ✅ Log ERROR avec `{detail, step, correlation_id}`
- ✅ Messages actionnables

---

### 2. Tests unitaires

**Fichier:** `tests/test_lunar_returns.py`

**Tests implémentés:**
- ✅ `test_success_generate_201`: POST `/api/lunar-returns/generate` renvoie 201 si natal_chart existe
- ✅ `test_error_json_shape`: Force erreur (pas de natal_chart) => réponse JSON contient `{detail, step, correlation_id}`
- ✅ `test_db_user_id_int`: Vérifie que `LunarReturn.user_id` est INTEGER dans le modèle SQLAlchemy

**Exécution:**
```bash
cd apps/api
pytest tests/test_lunar_returns.py -v
```

---

### 3. Script SQL d'introspection

**Fichier:** `scripts/sql/inspect_core_schema.sql`

**Vérifie:**
- `natal_charts.id`, `natal_charts.user_id`
- `lunar_returns.id`, `lunar_returns.user_id`, `lunar_returns.return_date`

**Exécution:**
```bash
psql $DATABASE_URL -f apps/api/scripts/sql/inspect_core_schema.sql
```

**Documentation:** Ajoutée dans `DB_SCHEMA_NOTES.md`

---

### 4. Migration documentée et idempotente

**Fichier:** `migrations/migrate_lunar_returns_user_id_to_int_simple.sql`

**Améliorations:**
- ✅ Idempotence: vérifie si colonnes/contraintes existent avant création
- ✅ Documentation: note sur alignement types DB <-> modèles
- ✅ Référence vers `inspect_core_schema.sql` pour vérification

**Note critique ajoutée:**
> ⚠️ RÈGLE CRITIQUE: Aligner types DB <-> modèles SQLAlchemy
> - user_id doit être INTEGER partout (pas UUID)
> - Vérifier après migration avec: scripts/sql/inspect_core_schema.sql

---

### 5. Analyse RLS / Auth

**Fichier:** `RLS_POLICIES_ANALYSIS.md`

**Analyse:**
- ✅ Comment `current_user.id` est dérivé du JWT (`sub` → `int`)
- ✅ Problèmes des policies RLS actuelles (utilisent `email` → `SELECT`)
- ✅ Recommandation: **Désactiver RLS** (FastAPI gère déjà l'auth)

**Recommandation:**
```sql
-- Désactiver RLS (FastAPI gère l'authentification)
ALTER TABLE natal_charts DISABLE ROW LEVEL SECURITY;
ALTER TABLE lunar_returns DISABLE ROW LEVEL SECURITY;
```

**Alternative (si RLS requis):** Utiliser `current_setting('request.jwt.claims')::json ->> 'sub'` directement

---

## 📋 Checklist de validation E2E

### 1. Schema sanity check au démarrage

```bash
cd apps/api
uvicorn main:app --reload
```

**Attendu:**
- Si schéma correct: `✅ Schema sanity check OK au démarrage`
- Si incorrect (dev): serveur ne démarre pas avec erreur claire

---

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

---

### 3. Script SQL d'introspection

```bash
psql $DATABASE_URL -f apps/api/scripts/sql/inspect_core_schema.sql
```

**Attendu:**
```
 table_name    | column_name | data_type                  | udt_name
---------------+-------------+----------------------------+----------
 lunar_returns | id          | integer                    | int4
 lunar_returns | return_date | timestamp with time zone   | timestamptz
 lunar_returns | user_id     | integer                    | int4
 natal_charts  | id          | uuid                       | uuid
 natal_charts  | user_id     | integer                    | int4
```

---

### 4. Tests unitaires

```bash
cd apps/api
pytest tests/test_lunar_returns.py::test_success_generate_201 -v
pytest tests/test_lunar_returns.py::test_error_json_shape -v
pytest tests/test_lunar_returns.py::test_db_user_id_int -v
```

**Attendu:** Tous les tests passent

---

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

## 📝 Fichiers modifiés

### Fichiers modifiés

1. `utils/schema_sanity_check.py`
   - Ajout vérification `return_date` (timestamptz)
   - Correction: `lunar_returns.id` est INTEGER (pas UUID)

2. `scripts/sql/inspect_core_schema.sql`
   - Ajout `return_date` dans la requête
   - Mise à jour documentation résultat attendu

3. `tests/test_lunar_returns.py`
   - Renommage: `test_success_generate_201`, `test_error_json_shape`, `test_db_user_id_int`
   - Amélioration `test_error_json_shape`: vérifie structure exacte `{detail, step, correlation_id}`

4. `migrations/migrate_lunar_returns_user_id_to_int_simple.sql`
   - Ajout idempotence (vérifications IF NOT EXISTS)
   - Documentation: note critique sur alignement types

5. `DB_SCHEMA_NOTES.md`
   - Ajout section sur `inspect_core_schema.sql`
   - Instructions d'exécution

### Fichiers créés

1. `RLS_POLICIES_ANALYSIS.md`
   - Analyse complète auth JWT vs RLS policies
   - Recommandation claire et actionnable

2. `HARDENING_RETURN_DATE_SUMMARY.md` (ce fichier)
   - Récapitulatif complet

---

## 🎯 Points clés

1. **Schema sanity check** vérifie maintenant `return_date` (timestamptz)
2. **Tests** vérifient structure erreur JSON exacte et types DB
3. **Migration** est idempotente et documentée
4. **RLS** recommandation: désactiver (FastAPI gère l'auth)

---

## 🔄 Maintenance future

### Après chaque migration SQL

1. Exécuter `scripts/sql/inspect_core_schema.sql`
2. Redémarrer l'app et vérifier les logs: `✅ Schema sanity check OK`
3. Tester `/health/db`

### Ajouter une nouvelle colonne critique

1. Ajouter dans `EXPECTED_SCHEMA` dans `utils/schema_sanity_check.py`
2. Mettre à jour `scripts/sql/inspect_core_schema.sql`
3. Ajouter un test unitaire si applicable

