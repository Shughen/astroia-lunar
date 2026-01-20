# return_date comme colonne métier : Récapitulatif complet

**Date:** 2025-01-XX  
**Objectif:** Utiliser `return_date` (timestamptz) comme colonne métier indexable/requêtable pour les révolutions lunaires

---

## ✅ Ce qui a été fait

### 1. Base de données

- ✅ Colonne `return_date`: `timestamptz NOT NULL`
- ✅ Trigger PostgreSQL: Remplit automatiquement depuis `raw_data.return_datetime`
- ✅ Index: `idx_lunar_returns_user_return_date` sur `(user_id, return_date)`
- ✅ Contrainte UNIQUE: `uq_lunar_returns_user_return_day` sur `(user_id, DATE(return_date))`
- ✅ Backfill: Toutes les lignes existantes ont `return_date` renseigné

### 2. Code Python

- ✅ Modèle SQLAlchemy: `return_date = Column(DateTime(timezone=True), nullable=False)`
- ✅ Schema API: `LunarReturnResponse.return_date: datetime` (ISO 8601)
- ✅ Endpoints: Nouveaux endpoints utilisant `return_date`

---

## 📊 Requêtes SQL prêtes à l'emploi

Voir `scripts/sql/lunar_returns_queries.sql` pour toutes les requêtes.

### A) Prochain retour lunaire

```sql
SELECT id, user_id, month, return_date, lunar_ascendant, moon_house, moon_sign, interpretation
FROM public.lunar_returns
WHERE user_id = :user_id AND return_date >= NOW()
ORDER BY return_date ASC
LIMIT 1;
```

### B) Liste des 12 retours d'une année

```sql
SELECT id, user_id, month, return_date, lunar_ascendant, moon_house, moon_sign, interpretation
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= DATE_TRUNC('year', :year_date::date)
    AND return_date < DATE_TRUNC('year', :year_date::date) + INTERVAL '1 year'
ORDER BY return_date ASC;
```

### C) Retour lunaire correspondant à une date (nearest)

```sql
WITH ranked_returns AS (
    SELECT id, user_id, month, return_date, lunar_ascendant, moon_house, moon_sign,
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

---

## 🌐 Endpoints API FastAPI

### GET `/api/lunar-returns/next`

**Description:** Prochain retour lunaire (>= maintenant)

**Exemple:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/next
```

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

---

### GET `/api/lunar-returns/year/{year}`

**Description:** Révolutions lunaires d'une année (triées par return_date)

**Exemple:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/year/2025
```

---

### GET `/api/lunar-returns/range`

**Description:** Révolutions lunaires dans une plage de dates

**Query params:**
- `from_date`: ISO 8601 datetime (ex: `2025-01-01T00:00:00Z`)
- `to_date`: ISO 8601 datetime (ex: `2025-12-31T23:59:59Z`)

**Exemple:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  "http://localhost:8000/api/lunar-returns/range?from_date=2025-01-01T00:00:00Z&to_date=2025-12-31T23:59:59Z"
```

---

### GET `/api/lunar-returns/near/{target_date}`

**Description:** Retour lunaire le plus proche d'une date (tolérance ±1 jour)

**Exemple:**
```bash
curl -H "Authorization: Bearer $TOKEN" \
  http://localhost:8000/api/lunar-returns/near/2025-03-15T12:00:00Z
```

---

## 🔧 Queries Supabase (si utilisé directement)

Si vous utilisez Supabase Client directement (JavaScript/TypeScript):

### Prochain retour lunaire

```javascript
const { data, error } = await supabase
  .from('lunar_returns')
  .select('*')
  .eq('user_id', userId)
  .gte('return_date', new Date().toISOString())
  .order('return_date', { ascending: true })
  .limit(1)
  .single();
```

### Liste des retours d'une année

```javascript
const yearStart = new Date(year, 0, 1).toISOString();
const yearEnd = new Date(year + 1, 0, 1).toISOString();

const { data, error } = await supabase
  .from('lunar_returns')
  .select('*')
  .eq('user_id', userId)
  .gte('return_date', yearStart)
  .lt('return_date', yearEnd)
  .order('return_date', { ascending: true });
```

### Range de dates

```javascript
const { data, error } = await supabase
  .from('lunar_returns')
  .select('*')
  .eq('user_id', userId)
  .gte('return_date', fromDate.toISOString())
  .lte('return_date', toDate.toISOString())
  .order('return_date', { ascending: true });
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
SELECT user_id, DATE(return_date) AS return_day, COUNT(*) AS count
FROM public.lunar_returns
GROUP BY user_id, DATE(return_date)
HAVING COUNT(*) > 1;
-- Devrait retourner 0 lignes
```

---

## 🚀 Migration safe (production)

### Checklist pré-déploiement

1. ✅ Vérifier que le trigger fonctionne
2. ✅ Vérifier qu'il n'y a pas de NULL
3. ✅ Vérifier qu'il n'y a pas de doublons
4. ✅ Backup de la table (optionnel)

### Étapes

1. **Backup:**
   ```sql
   CREATE TABLE lunar_returns_backup_$(date +%Y%m%d) AS SELECT * FROM lunar_returns;
   ```

2. **Appliquer les contraintes:**
   ```bash
   psql $DATABASE_URL -f apps/api/scripts/sql/lunar_returns_constraints_migration.sql
   ```

3. **Vérifier post-migration:**
   ```sql
   -- Vérifier NOT NULL
   SELECT COUNT(*) FILTER (WHERE return_date IS NULL) FROM lunar_returns;
   
   -- Vérifier contrainte unique
   SELECT user_id, DATE(return_date), COUNT(*) 
   FROM lunar_returns 
   GROUP BY user_id, DATE(return_date) 
   HAVING COUNT(*) > 1;
   ```

4. **Déployer le code** (modèle SQLAlchemy + endpoints)

5. **Tests E2E:**
   ```bash
   # Test prochain retour
   curl -H "Authorization: Bearer $TOKEN" \
     http://localhost:8000/api/lunar-returns/next
   
   # Test année
   curl -H "Authorization: Bearer $TOKEN" \
     http://localhost:8000/api/lunar-returns/year/2025
   ```

---

## 📝 Tests de vérification

### Test trigger

```sql
-- Insérer avec raw_data mais return_date NULL
INSERT INTO public.lunar_returns (user_id, month, raw_data)
VALUES (999, '2025-13', '{"return_datetime": "2025-12-25T15:30:00Z"}'::jsonb)
RETURNING id, return_date, raw_data->>'return_datetime';

-- Vérifier que return_date a été rempli
-- Devrait montrer return_date = 2025-12-25 15:30:00+00

DELETE FROM public.lunar_returns WHERE user_id = 999;
```

### Test contrainte unique

```sql
-- Devrait réussir
INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
VALUES (999, '2025-01', '2025-01-15T12:00:00Z'::timestamptz, '{}'::jsonb);

-- Devrait échouer (même jour, même user)
INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
VALUES (999, '2025-02', '2025-01-15T13:00:00Z'::timestamptz, '{}'::jsonb);
-- Erreur: duplicate key value violates unique constraint "uq_lunar_returns_user_return_day"

DELETE FROM public.lunar_returns WHERE user_id = 999;
```

---

## 📚 Fichiers de référence

- `scripts/sql/lunar_returns_queries.sql` - Toutes les requêtes SQL
- `scripts/sql/lunar_returns_constraints_migration.sql` - Migration safe avec contraintes
- `RETURN_DATE_MIGRATION_GUIDE.md` - Guide détaillé de migration
- `models/lunar_return.py` - Modèle SQLAlchemy mis à jour
- `routes/lunar_returns.py` - Endpoints API mis à jour

---

## 🎯 Utilisation future

Les futures features peuvent maintenant s'appuyer sur `return_date`:
- Home "next lunar return" → `GET /api/lunar-returns/next`
- Timeline → `GET /api/lunar-returns/year/{year}`
- Notifications → Requête SQL directe sur `return_date >= NOW()`
- Calendrier → Range queries sur `return_date`

Plus besoin de parser `raw_data.return_datetime` côté application !

