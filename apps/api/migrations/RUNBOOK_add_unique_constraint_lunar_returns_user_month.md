# Runbook: Migration UNIQUE (user_id, month) sur lunar_returns

## Étape 1: Détecter les doublons existants (AVANT migration)

```bash
# Charger DATABASE_URL depuis .env
cd apps/api
source .venv/bin/activate 2>/dev/null || true
export $(grep -v '^#' .env | grep DATABASE_URL | xargs)

# Détecter les doublons
psql "$DATABASE_URL" -c "
SELECT user_id, month, COUNT(*) as count
FROM public.lunar_returns
GROUP BY user_id, month
HAVING COUNT(*) > 1
ORDER BY count DESC, user_id, month;
"
```

**Résultat attendu**: Aucune ligne (pas de doublons) OU liste des doublons.

---

## Étape 2: Appliquer la migration

```bash
# Charger DATABASE_URL depuis .env
cd apps/api
source .venv/bin/activate 2>/dev/null || true
export $(grep -v '^#' .env | grep DATABASE_URL | xargs)

# Appliquer la migration
psql "$DATABASE_URL" -f migrations/add_unique_constraint_lunar_returns_user_month.sql
```

**Résultat attendu**: 
- `DROP CONSTRAINT` → OK (même si n'existe pas)
- `CREATE UNIQUE INDEX` → `CREATE INDEX` (succès)

---

## Étape 3: Vérifier que l'index existe

```bash
psql "$DATABASE_URL" -c "
SELECT 
    schemaname,
    tablename,
    indexname,
    indexdef
FROM pg_indexes
WHERE tablename = 'lunar_returns'
  AND indexname = 'uq_lunar_returns_user_month';
"
```

**Résultat attendu**: 1 ligne avec `indexname = 'uq_lunar_returns_user_month'`

---

## Étape 4: Vérifier que l'index est UNIQUE

```bash
psql "$DATABASE_URL" -c "
SELECT 
    i.indexname,
    i.indexdef,
    CASE WHEN i.indexdef LIKE '%UNIQUE%' THEN 'OUI' ELSE 'NON' END as is_unique
FROM pg_indexes i
WHERE i.tablename = 'lunar_returns'
  AND i.indexname = 'uq_lunar_returns_user_month';
"
```

**Résultat attendu**: `is_unique = 'OUI'` ET `indexdef` contient `UNIQUE`

---

## Étape 5: Vérifier les colonnes de l'index (user_id, month)

```bash
psql "$DATABASE_URL" -c "
SELECT 
    a.attname as column_name,
    a.attnum as column_position
FROM pg_index i
JOIN pg_class c ON c.oid = i.indrelid
JOIN pg_attribute a ON a.attrelid = c.oid AND a.attnum = ANY(i.indkey)
WHERE c.relname = 'lunar_returns'
  AND i.indexrelid = (
      SELECT oid FROM pg_class WHERE relname = 'uq_lunar_returns_user_month'
  )
ORDER BY a.attnum;
"
```

**Résultat attendu**: 2 lignes:
- `column_name = 'user_id'`, `column_position = 1`
- `column_name = 'month'`, `column_position = 2`

---

## Étape 6: Test fonctionnel (vérifier que l'index bloque les doublons)

```bash
psql "$DATABASE_URL" -c "
-- Récupérer un user_id et month existants pour le test
DO \$\$
DECLARE
    test_user_id INTEGER;
    test_month TEXT;
BEGIN
    SELECT user_id, month INTO test_user_id, test_month
    FROM public.lunar_returns
    LIMIT 1;
    
    IF test_user_id IS NOT NULL THEN
        RAISE NOTICE 'Test: tentative insertion doublon (user_id=%, month=%)', test_user_id, test_month;
        BEGIN
            INSERT INTO public.lunar_returns (user_id, month, return_date, raw_data)
            VALUES (test_user_id, test_month, NOW(), '{}');
            RAISE EXCEPTION 'ERREUR: L''index UNIQUE n''a PAS bloqué le doublon!';
        EXCEPTION WHEN unique_violation THEN
            RAISE NOTICE 'SUCCÈS: L''index UNIQUE bloque correctement les doublons';
        END;
    ELSE
        RAISE NOTICE 'Aucune donnée existante pour tester';
    END IF;
END \$\$;
"
```

**Résultat attendu**: Message `SUCCÈS: L'index UNIQUE bloque correctement les doublons`

---

## ❌ SI LA MIGRATION ÉCHOUE (doublons existants)

### 6.1 Lister tous les doublons avec détails

```bash
psql "$DATABASE_URL" -c "
SELECT 
    lr1.id as id_1,
    lr2.id as id_2,
    lr1.user_id,
    lr1.month,
    lr1.return_date as return_date_1,
    lr2.return_date as return_date_2,
    lr1.created_at as created_at_1,
    lr2.created_at as created_at_2
FROM public.lunar_returns lr1
JOIN public.lunar_returns lr2 
    ON lr1.user_id = lr2.user_id 
    AND lr1.month = lr2.month
    AND lr1.id < lr2.id
ORDER BY lr1.user_id, lr1.month, lr1.id;
"
```

### 6.2 Stratégie de correction (garder le plus récent)

```bash
# Option A: Supprimer les doublons en gardant le plus récent (return_date)
psql "$DATABASE_URL" -c "
DELETE FROM public.lunar_returns lr1
WHERE EXISTS (
    SELECT 1
    FROM public.lunar_returns lr2
    WHERE lr2.user_id = lr1.user_id
      AND lr2.month = lr1.month
      AND lr2.id > lr1.id
      AND (
          lr2.return_date > lr1.return_date
          OR (lr2.return_date = lr1.return_date AND lr2.created_at > lr1.created_at)
      )
);
"
```

**OU** Option B: Supprimer les doublons en gardant le plus ancien (id min)

```bash
psql "$DATABASE_URL" -c "
DELETE FROM public.lunar_returns lr1
WHERE EXISTS (
    SELECT 1
    FROM public.lunar_returns lr2
    WHERE lr2.user_id = lr1.user_id
      AND lr2.month = lr1.month
      AND lr2.id < lr1.id
);
"
```

### 6.3 Vérifier qu'il n'y a plus de doublons

```bash
psql "$DATABASE_URL" -c "
SELECT user_id, month, COUNT(*) as count
FROM public.lunar_returns
GROUP BY user_id, month
HAVING COUNT(*) > 1;
"
```

**Résultat attendu**: Aucune ligne (0 doublons)

### 6.4 Réappliquer la migration

```bash
psql "$DATABASE_URL" -f migrations/add_unique_constraint_lunar_returns_user_month.sql
```

---

## ✅ Checklist finale

- [ ] Aucun doublon détecté avant migration (Étape 1)
- [ ] Migration appliquée sans erreur (Étape 2)
- [ ] Index `uq_lunar_returns_user_month` existe (Étape 3)
- [ ] Index est UNIQUE (Étape 4)
- [ ] Index couvre (user_id, month) (Étape 5)
- [ ] Test fonctionnel: index bloque les doublons (Étape 6)

---

## Commandes rapides (tout-en-un)

```bash
cd apps/api
export $(grep -v '^#' .env | grep DATABASE_URL | xargs)

# 1. Détecter doublons
echo "=== 1. Détection doublons ==="
psql "$DATABASE_URL" -c "SELECT user_id, month, COUNT(*) FROM public.lunar_returns GROUP BY user_id, month HAVING COUNT(*) > 1;"

# 2. Appliquer migration
echo "=== 2. Application migration ==="
psql "$DATABASE_URL" -f migrations/add_unique_constraint_lunar_returns_user_month.sql

# 3. Vérifier index
echo "=== 3. Vérification index ==="
psql "$DATABASE_URL" -c "SELECT indexname, indexdef FROM pg_indexes WHERE tablename = 'lunar_returns' AND indexname = 'uq_lunar_returns_user_month';"
```

