# Migration return_date: Guide complet

**Date:** 2025-01-XX  
**Objectif:** Utiliser `return_date` (timestamptz) comme colonne métier indexable/requêtable

---

## 📋 Résumé de la migration

### État actuel (après backfill et trigger)

1. ✅ **Colonne `return_date`**: `timestamptz NOT NULL` en DB
2. ✅ **Trigger PostgreSQL**: Remplit automatiquement `return_date` depuis `raw_data.return_datetime`
3. ✅ **Index**: `idx_lunar_returns_user_return_date` sur `(user_id, return_date)`
4. ✅ **Backfill**: Toutes les lignes existantes ont `return_date` renseigné

### Changements code

1. ✅ **Modèle SQLAlchemy**: `return_date` est maintenant `DateTime(timezone=True)` au lieu de `String`
2. ✅ **Schema API**: `LunarReturnResponse.return_date` est `datetime` (ISO 8601)
3. ✅ **Endpoints**: Nouveaux endpoints utilisant `return_date` pour trier/filtrer

---

## 🔧 Requêtes SQL prêtes à l'emploi

Voir `scripts/sql/lunar_returns_queries.sql` pour toutes les requêtes détaillées.

### 1. Prochain retour lunaire (>= maintenant)

```sql
SELECT 
    id, user_id, month, return_date, lunar_ascendant, moon_house, moon_sign, interpretation
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= NOW()
ORDER BY return_date ASC
LIMIT 1;
```

**Usage:** Home "next lunar return", notifs, etc.

### 2. Liste des 12 retours d'une année

```sql
SELECT 
    id, user_id, month, return_date, lunar_ascendant, moon_house, moon_sign, interpretation
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= DATE_TRUNC('year', :year_date::date)
    AND return_date < DATE_TRUNC('year', :year_date::date) + INTERVAL '1 year'
ORDER BY return_date ASC;
```

**Usage:** Timeline, calendrier annuel, historique

### 3. Retour lunaire correspondant à une date (nearest)

```sql
WITH ranked_returns AS (
    SELECT 
        id, user_id, month, return_date, lunar_ascendant, moon_house, moon_sign,
        ABS(EXTRACT(EPOCH FROM (return_date - :target_date::timestamptz))) AS seconds_diff,
        ROW_NUMBER() OVER (
            ORDER BY ABS(EXTRACT(EPOCH FROM (return_date - :target_date::timestamptz))),
                     return_date DESC
        ) AS rn
    FROM public.lunar_returns
    WHERE user_id = :user_id
)
SELECT id, user_id, month, return_date, lunar_ascendant, moon_house, moon_sign, seconds_diff
FROM ranked_returns
WHERE rn = 1;
```

**Usage:** "Quel était mon retour lunaire le 15 mars 2025 ?"

---

## 🌐 Endpoints API

### GET `/api/lunar-returns/next`

Récupère le prochain retour lunaire (>= maintenant)

**Réponse:**
```json
{
  "id": 123,
  "month": "2025-03",
  "return_date": "2025-03-15T14:32:00+00:00",
  "lunar_ascendant": "Taurus",
  "moon_house": 4,
  "moon_sign": "Aries",
  "aspects": [...],
  "interpretation": "..."
}
```

**Exemple curl:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/next
```

---

### GET `/api/lunar-returns/year/{year}`

Récupère les révolutions lunaires d'une année (triées par return_date)

**Paramètres:**
- `year` (path): Année (ex: 2025)

**Exemple curl:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/year/2025
```

---

### GET `/api/lunar-returns/range`

Récupère les révolutions lunaires dans une plage de dates

**Query params:**
- `from_date` (required): ISO 8601 datetime (ex: `2025-01-01T00:00:00Z`)
- `to_date` (required): ISO 8601 datetime (ex: `2025-12-31T23:59:59Z`)

**Exemple curl:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  "http://localhost:8000/api/lunar-returns/range?from_date=2025-01-01T00:00:00Z&to_date=2025-12-31T23:59:59Z"
```

---

### GET `/api/lunar-returns/near/{target_date}`

Récupère le retour lunaire le plus proche d'une date donnée (tolérance ±1 jour)

**Paramètres:**
- `target_date` (path): ISO 8601 datetime (ex: `2025-03-15T12:00:00Z`)

**Exemple curl:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/near/2025-03-15T12:00:00Z
```

---

### GET `/api/lunar-returns/` (modifié)

Trie maintenant par `return_date` au lieu de `month`

**Exemple curl:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/
```

---

## 🛡️ Validations et contraintes

### Contrainte UNIQUE partielle

**Fichier:** `scripts/sql/lunar_returns_constraints_migration.sql`

Empêche d'avoir deux retours lunaires le même jour pour un même user:

```sql
CREATE UNIQUE INDEX uq_lunar_returns_user_return_day
ON public.lunar_returns (user_id, DATE(return_date));
```

**Vérification:**
```sql
-- Devrait retourner 0 lignes
SELECT user_id, DATE(return_date) AS return_day, COUNT(*) AS count
FROM public.lunar_returns
GROUP BY user_id, DATE(return_date)
HAVING COUNT(*) > 1;
```

---

## 🚀 Migration safe (production)

### Checklist pré-migration

1. ✅ Vérifier que le trigger fonctionne:
   ```sql
   -- Insérer une ligne test avec raw_data mais return_date NULL
   INSERT INTO public.lunar_returns (user_id, month, raw_data)
   VALUES (1, '2025-01', '{"return_datetime": "2025-01-15T12:00:00Z"}'::jsonb);
   
   -- Vérifier que return_date a été rempli
   SELECT id, return_date, raw_data->>'return_datetime' 
   FROM public.lunar_returns WHERE user_id = 1 ORDER BY id DESC LIMIT 1;
   ```

2. ✅ Vérifier qu'il n'y a pas de NULL:
   ```sql
   SELECT COUNT(*) FILTER (WHERE return_date IS NULL) AS null_count
   FROM public.lunar_returns;
   -- Devrait être 0
   ```

3. ✅ Vérifier qu'il n'y a pas de doublons (même jour pour un user):
   ```sql
   SELECT user_id, DATE(return_date) AS return_day, COUNT(*) AS count
   FROM public.lunar_returns
   GROUP BY user_id, DATE(return_date)
   HAVING COUNT(*) > 1;
   -- Devrait retourner 0 lignes
   ```

### Étapes de migration

1. **Backup** (optionnel mais recommandé):
   ```sql
   CREATE TABLE lunar_returns_backup AS SELECT * FROM lunar_returns;
   ```

2. **Appliquer les contraintes** (si pas déjà fait):
   ```bash
   psql $DATABASE_URL -f apps/api/scripts/sql/lunar_returns_constraints_migration.sql
   ```

3. **Vérifier post-migration**:
   ```sql
   -- Vérifier NOT NULL
   SELECT COUNT(*) FILTER (WHERE return_date IS NULL) FROM lunar_returns;
   
   -- Vérifier contrainte unique
   SELECT user_id, DATE(return_date), COUNT(*) 
   FROM lunar_returns 
   GROUP BY user_id, DATE(return_date) 
   HAVING COUNT(*) > 1;
   
   -- Vérifier index
   SELECT indexname FROM pg_indexes WHERE tablename = 'lunar_returns' 
     AND indexname = 'idx_lunar_returns_user_return_date';
   ```

4. **Déployer le code**:
   - Mettre à jour le modèle SQLAlchemy
   - Déployer les nouveaux endpoints
   - Tester les endpoints

5. **Rollback** (si nécessaire):
   ```sql
   -- Supprimer la contrainte unique
   DROP INDEX IF EXISTS uq_lunar_returns_user_return_day;
   
   -- Remettre return_date nullable (si vraiment nécessaire)
   -- ALTER TABLE lunar_returns ALTER COLUMN return_date DROP NOT NULL;
   ```

---

## 🧪 Tests et vérifications

### Test 1: Trigger fonctionne

```sql
-- Insérer avec raw_data mais return_date NULL
INSERT INTO public.lunar_returns (user_id, month, raw_data)
VALUES (999, '2025-13', '{"return_datetime": "2025-12-25T15:30:00Z"}'::jsonb)
RETURNING id, return_date, raw_data->>'return_datetime';

-- Vérifier que return_date a été rempli automatiquement
-- Supprimer la ligne test
DELETE FROM public.lunar_returns WHERE user_id = 999;
```

### Test 2: Contrainte unique fonctionne

```sql
-- Devrait réussir
INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
VALUES (999, '2025-01', '2025-01-15T12:00:00Z'::timestamptz, '{}'::jsonb);

-- Devrait échouer (même jour)
INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
VALUES (999, '2025-02', '2025-01-15T13:00:00Z'::timestamptz, '{}'::jsonb);
-- Erreur attendue: duplicate key value violates unique constraint

-- Nettoyer
DELETE FROM public.lunar_returns WHERE user_id = 999;
```

### Test 3: Requêtes SQL

Voir `scripts/sql/lunar_returns_queries.sql` pour toutes les requêtes de test.

### Test 4: Endpoints API

```bash
# 1. Login
TOKEN=$(curl -s -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=test@example.com&password=password123" | jq -r .access_token)

# 2. Générer les retours lunaires (si pas déjà fait)
curl -X POST http://localhost:8000/api/lunar-returns/generate \
  -H "Authorization: Bearer $TOKEN"

# 3. Prochain retour
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/next | jq

# 4. Année 2025
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/year/2025 | jq

# 5. Range
curl -H "Authorization: Bearer $TOKEN" \
  "http://localhost:8000/api/lunar-returns/range?from_date=2025-01-01T00:00:00Z&to_date=2025-12-31T23:59:59Z" | jq

# 6. Near date
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/near/2025-03-15T12:00:00Z | jq
```

---

## 📝 Notes importantes

### Format return_date

- **DB**: `timestamptz` (UTC)
- **API**: `datetime` ISO 8601 (ex: `2025-03-15T14:32:00+00:00`)
- **Trigger**: Parse depuis `raw_data.return_datetime` (string) et convertit en `timestamptz` UTC

### Performance

L'index `idx_lunar_returns_user_return_date` sur `(user_id, return_date)` optimise toutes les requêtes par user et date.

### Compatibilité legacy

L'endpoint `GET /api/lunar-returns/{month}` est conservé pour compatibilité, mais il est recommandé d'utiliser les nouveaux endpoints basés sur `return_date`.

---

## 🔄 Migration future

Si on veut supprimer la colonne `month` (legacy):
1. Vérifier qu'aucun code ne l'utilise
2. Créer une migration pour supprimer `month`
3. Mettre à jour tous les endpoints

Pour l'instant, `month` est conservé pour compatibilité.

