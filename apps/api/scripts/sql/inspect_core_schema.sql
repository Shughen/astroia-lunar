-- Script d'introspection du schéma DB pour vérifier les types de colonnes critiques
-- Tables: natal_charts, lunar_returns
-- Colonnes critiques: id, user_id, return_date
--
-- Usage:
--   - Via Supabase SQL Editor: copier-coller et exécuter
--   - Via psql: psql $DATABASE_URL -f apps/api/scripts/sql/inspect_core_schema.sql
--
-- Objectif: Détecter les mismatches entre types DB et modèles SQLAlchemy
-- pour prévenir les bugs de type (UUID vs INTEGER, timestamptz vs string).

SELECT 
    table_name,
    column_name,
    data_type,
    udt_name,
    is_nullable,
    column_default
FROM information_schema.columns
WHERE table_schema = 'public'
    AND table_name IN ('natal_charts', 'lunar_returns')
    AND column_name IN ('id', 'user_id', 'return_date')
ORDER BY table_name, column_name;

-- Vérification supplémentaire: contraintes FK
SELECT 
    tc.table_name,
    kcu.column_name,
    ccu.table_name AS foreign_table_name,
    ccu.column_name AS foreign_column_name,
    tc.constraint_name
FROM information_schema.table_constraints AS tc
JOIN information_schema.key_column_usage AS kcu
    ON tc.constraint_name = kcu.constraint_name
    AND tc.table_schema = kcu.table_schema
JOIN information_schema.constraint_column_usage AS ccu
    ON ccu.constraint_name = tc.constraint_name
    AND ccu.table_schema = tc.table_schema
WHERE tc.constraint_type = 'FOREIGN KEY'
    AND tc.table_schema = 'public'
    AND tc.table_name IN ('natal_charts', 'lunar_returns')
    AND kcu.column_name = 'user_id'
ORDER BY tc.table_name;

-- Résultat attendu après migrations:
-- natal_charts.id: uuid (PK)
-- natal_charts.user_id: integer (FK -> users.id)
-- lunar_returns.id: integer (PK) - NOT UUID
-- lunar_returns.user_id: integer (FK -> users.id)
-- lunar_returns.return_date: timestamp with time zone / timestamptz (NOT NULL, indexé)

