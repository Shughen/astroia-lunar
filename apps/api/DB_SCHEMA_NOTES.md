# Schéma DB - Table `natal_charts`

**Date:** 2025-01-XX  
**Table:** `public.natal_charts`  
**Objectif:** Documenter le schéma réel pour aligner le modèle SQLAlchemy.

---

## 📊 Requête SQL de vérification

### Vérification complète (toutes les colonnes d'une table)

```sql
SELECT 
    column_name,
    data_type,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_schema = 'public' 
  AND table_name = 'natal_charts'
ORDER BY ordinal_position;
```

### Vérification des colonnes critiques (script d'introspection)

**Script:** `apps/api/scripts/sql/inspect_core_schema.sql`

**Exécution:**
```bash
# Via psql
psql $DATABASE_URL -f apps/api/scripts/sql/inspect_core_schema.sql

# Via Supabase SQL Editor: copier-coller le contenu du fichier
```

**Vérifie:**
- `natal_charts.id` → uuid
- `natal_charts.user_id` → integer
- `lunar_returns.id` → integer
- `lunar_returns.user_id` → integer
- `lunar_returns.return_date` → timestamp with time zone / timestamptz

**Résultat attendu:**
- Tous les `user_id` doivent être `integer` / `int4`
- `natal_charts.id` doit être `uuid`
- `lunar_returns.id` doit être `integer` / `int4`
- `lunar_returns.return_date` doit être `timestamp with time zone` / `timestamptz`

---

## ✅ Schéma attendu (après migration)

**Colonnes existantes :**

| column_name   | data_type                   | is_nullable | column_default       |
|---------------|-----------------------------|-------------|----------------------|
| id            | uuid                        | NO          | (uuid_generate_v4)   |
| user_id       | integer                     | NO          | NULL                 |
| positions     | jsonb                       | YES         | NULL                 |
| calculated_at | timestamp with time zone    | YES         | now()                |

**⚠️ Important :** 
- `id` est **UUID** (PK), pas INTEGER
- `user_id` est **INTEGER** FK vers `users.id` (INTEGER), pas UUID
- `user_id` est **NOT NULL** (après migration complète, peut être nullable temporairement pendant la migration)

---

## ❌ Colonnes absentes (supprimées en V2)

Ces colonnes **n'existent plus** dans la table et ne doivent **pas** être déclarées dans le modèle SQLAlchemy :

- `sun_sign` (varchar/text)
- `moon_sign` (varchar/text)
- `ascendant` (varchar/text)
- `planets` (json/jsonb)
- `houses` (json/jsonb)
- `aspects` (json/jsonb)
- `raw_data` (json/jsonb)

**Toutes ces données sont maintenant stockées dans `positions` JSONB.**

---

## 🔍 Vérification du schéma réel

### Option 1 : Via Supabase Dashboard

1. Aller dans Supabase → SQL Editor
2. Exécuter la requête ci-dessus
3. Comparer avec le tableau attendu

### Option 2 : Via psql (local ou Supabase)

```bash
# Connexion (adapter selon votre config)
psql $DATABASE_URL

# Puis exécuter la requête
\dt natal_charts
\d natal_charts
```

### Option 3 : Via script Python (dans l'app)

```python
# Dans un script ou endpoint debug
from sqlalchemy import text
result = await db.execute(text("""
    SELECT column_name, data_type, is_nullable
    FROM information_schema.columns
    WHERE table_schema = 'public' 
      AND table_name = 'natal_charts'
    ORDER BY ordinal_position
"""))
for row in result:
    print(f"{row.column_name}: {row.data_type} (nullable={row.is_nullable})")
```

---

## 📝 Notes importantes

### `user_id` INTEGER FK

- **`user_id`** : INTEGER NOT NULL, FK vers `users.id` (INTEGER)
- Après migration : l'ancienne colonne `user_id` (UUID) est supprimée et remplacée par `user_id` (INTEGER)

**⚠️ Important :** 
- `user_id` est **INTEGER**, pas UUID
- `users.id` est **INTEGER**
- La migration convertit `natal_charts.user_id` de UUID vers INTEGER

### `positions` JSONB

Structure attendue dans `positions` :

```json
{
  "sun": {
    "sign": "Taurus",
    "degree": 25.5,
    "absolute_longitude": 55.5
  },
  "moon": {
    "sign": "Pisces",
    "degree": 28.1,
    "absolute_longitude": 328.1,
    "house": 4
  },
  "ascendant": {
    "sign": "Leo",
    "degree": 5.2
  },
  "planets": {
    "Sun": {...},
    "Moon": {...},
    ...
  },
  "houses": {
    "1": {...},
    "2": {...},
    ...
  },
  "aspects": [...]
}
```

### `calculated_at`

- Type : `timestamp with time zone`
- Nullable : YES (mais a une valeur par défaut `now()`)
- SQLAlchemy : `Column(DateTime(timezone=True), server_default=func.now())`

---

## 🔧 Si le schéma réel diffère

### Cas 1 : `calculated_at` absent

Si la colonne n'existe pas :

**Option A : Supprimer du modèle** (si pas nécessaire)
```python
# Ne pas déclarer calculated_at dans le modèle
```

**Option B : Créer la colonne** (via migration Supabase)
```sql
ALTER TABLE natal_charts 
ADD COLUMN IF NOT EXISTS calculated_at TIMESTAMP WITH TIME ZONE DEFAULT now();
```

### Cas 2 : Type différent pour `positions`

Si `positions` est `json` au lieu de `jsonb` :

**Option A : Modifier le modèle** (si on peut vivre avec json)
```python
from sqlalchemy import JSON
positions = Column(JSON)
```

**Option B : Migrer vers jsonb** (recommandé pour performances)
```sql
ALTER TABLE natal_charts 
ALTER COLUMN positions TYPE jsonb USING positions::jsonb;
```

---

## ✅ Checklist de validation (après migration)

- [ ] La requête SQL retourne exactement 4 colonnes
- [ ] `id` : uuid, NOT NULL, primary key
- [ ] `user_id` : integer, NOT NULL, FK vers users.id
- [ ] `positions` : jsonb, nullable
- [ ] `calculated_at` : timestamp with time zone, nullable (default now())
- [ ] Aucune colonne `sun_sign`, `moon_sign`, `ascendant`, `planets`, `houses`, `aspects`, `raw_data`
- [ ] `users.id` est bien INTEGER (vérifier via requête SQL)
- [ ] Contrainte FK `fk_natal_charts_user_id` existe
- [ ] Contrainte UNIQUE sur `user_id` (1 natal chart par user)

## 📋 Migrations SQL

### Migration natal_charts.user_id (UUID -> INTEGER)

Voir le fichier `scripts/sql/migrate_natal_charts_user_id_to_int.sql` pour la migration complète.

**Résumé de la migration :**
1. Ajouter `user_id_int INTEGER` nullable
2. Backfill (ou supprimer données DEV)
3. Ajouter FK + UNIQUE constraints
4. Supprimer `user_id` UUID
5. Renommer `user_id_int` -> `user_id`
6. Rendre `user_id` NOT NULL (après backfill)

### Migration lunar_returns.user_id (UUID -> INTEGER)

Voir le fichier `migrations/migrate_lunar_returns_user_id_to_int_simple.sql` pour la migration complète.

**Résumé de la migration :**
1. Supprimer les données existantes (seront régénérées)
2. Supprimer les policies RLS qui dépendent de user_id
3. Supprimer l'ancienne FK
4. Supprimer l'ancienne colonne user_id (UUID)
5. Créer la nouvelle colonne user_id (INTEGER NOT NULL)
6. Ajouter la FK vers users.id
7. Recréer les policies RLS avec user_id INTEGER

**⚠️ IMPORTANT - Alignement types DB <-> modèles :**

**Règle critique à respecter :**
- **`user_id` doit être INTEGER partout** dans toutes les tables qui référencent `users.id`
- Ne jamais utiliser UUID pour `user_id` (même si `id` peut être UUID)
- Toujours vérifier l'alignement après une migration en utilisant `scripts/sql/inspect_core_schema.sql`

**Tables concernées :**
- `natal_charts.user_id` → INTEGER FK → `users.id` (INTEGER)
- `lunar_returns.user_id` → INTEGER FK → `users.id` (INTEGER)

**Vérification :**
```sql
-- Exécuter après chaque migration
SELECT table_name, column_name, data_type, udt_name
FROM information_schema.columns
WHERE table_schema = 'public'
    AND table_name IN ('natal_charts', 'lunar_returns')
    AND column_name = 'user_id'
ORDER BY table_name;
```

**Résultat attendu :**
- `data_type` = `integer`
- `udt_name` = `int4`

