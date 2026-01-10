-- ============================================
-- REQUÊTES SQL PRODUIT pour lunar_returns
-- Utilisation de return_date (timestamptz) comme colonne métier
-- ============================================

-- ============================================
-- 1. PROCHAIN RETOUR LUNAIRE d'un user (>= now())
-- ============================================
-- Usage: Home "next lunar return", notifs, etc.
-- Performance: utilise l'index (user_id, return_date)

SELECT 
    id,
    user_id,
    month,
    return_date,
    lunar_ascendant,
    moon_house,
    moon_sign,
    interpretation,
    calculated_at
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= NOW()
ORDER BY return_date ASC
LIMIT 1;

-- Alternative: si on veut inclure raw_data pour les détails
SELECT 
    lr.*,
    raw_data->>'return_datetime' AS return_datetime_string
FROM public.lunar_returns lr
WHERE user_id = :user_id
    AND return_date >= NOW()
ORDER BY return_date ASC
LIMIT 1;


-- ============================================
-- 2. LISTE des 12 retours d'un user sur une année
-- ============================================
-- Usage: Timeline, calendrier annuel, historique
-- Performance: utilise l'index (user_id, return_date)

-- Option A: Année calendaire complète (du 1er jan au 31 déc)
SELECT 
    id,
    user_id,
    month,
    return_date,
    lunar_ascendant,
    moon_house,
    moon_sign,
    interpretation,
    calculated_at
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= DATE_TRUNC('year', :year_date::date)
    AND return_date < DATE_TRUNC('year', :year_date::date) + INTERVAL '1 year'
ORDER BY return_date ASC;

-- Option B: 12 mois glissants depuis une date donnée
SELECT 
    id,
    user_id,
    month,
    return_date,
    lunar_ascendant,
    moon_house,
    moon_sign,
    interpretation,
    calculated_at
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= :from_date
    AND return_date < :from_date + INTERVAL '12 months'
ORDER BY return_date ASC;

-- Option C: Tous les retours (limité pour éviter trop de données)
SELECT 
    id,
    user_id,
    month,
    return_date,
    lunar_ascendant,
    moon_house,
    moon_sign,
    interpretation,
    calculated_at
FROM public.lunar_returns
WHERE user_id = :user_id
ORDER BY return_date ASC
LIMIT 12;


-- ============================================
-- 3. RETOUR LUNAIRE correspondant à une date donnée
-- ============================================
-- Usage: "Quel était mon retour lunaire le 15 mars 2025 ?"
-- Options: exact match, range, ou nearest

-- Option A: Exact match (jour précis, tolérance ±1 jour)
SELECT 
    id,
    user_id,
    month,
    return_date,
    lunar_ascendant,
    moon_house,
    moon_sign,
    interpretation,
    calculated_at,
    ABS(EXTRACT(EPOCH FROM (return_date - :target_date::timestamptz))) AS seconds_diff
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= :target_date::timestamptz - INTERVAL '1 day'
    AND return_date <= :target_date::timestamptz + INTERVAL '1 day'
ORDER BY return_date ASC
LIMIT 1;

-- Option B: Range (tous les retours dans une période)
SELECT 
    id,
    user_id,
    month,
    return_date,
    lunar_ascendant,
    moon_house,
    moon_sign,
    interpretation,
    calculated_at
FROM public.lunar_returns
WHERE user_id = :user_id
    AND return_date >= :from_date::timestamptz
    AND return_date <= :to_date::timestamptz
ORDER BY return_date ASC;

-- Option C: Nearest (le plus proche d'une date, avant ou après)
-- Si plusieurs à égale distance, on prend le plus récent
WITH ranked_returns AS (
    SELECT 
        id,
        user_id,
        month,
        return_date,
        lunar_ascendant,
        moon_house,
        moon_sign,
        interpretation,
        calculated_at,
        ABS(EXTRACT(EPOCH FROM (return_date - :target_date::timestamptz))) AS seconds_diff,
        ROW_NUMBER() OVER (
            ORDER BY ABS(EXTRACT(EPOCH FROM (return_date - :target_date::timestamptz))),
                     return_date DESC
        ) AS rn
    FROM public.lunar_returns
    WHERE user_id = :user_id
)
SELECT 
    id,
    user_id,
    month,
    return_date,
    lunar_ascendant,
    moon_house,
    moon_sign,
    interpretation,
    calculated_at,
    seconds_diff
FROM ranked_returns
WHERE rn = 1;


-- ============================================
-- 4. REQUÊTES UTILITAIRES
-- ============================================

-- Vérifier qu'il n'y a pas de doublons (même jour pour un user)
-- Devrait retourner 0 lignes si la contrainte unique fonctionne
SELECT 
    user_id,
    DATE(return_date) AS return_day,
    COUNT(*) AS count,
    ARRAY_AGG(id) AS ids
FROM public.lunar_returns
GROUP BY user_id, DATE(return_date)
HAVING COUNT(*) > 1;

-- Statistiques par user (nombre de retours, dates min/max)
SELECT 
    user_id,
    COUNT(*) AS total_returns,
    MIN(return_date) AS first_return,
    MAX(return_date) AS last_return,
    COUNT(*) FILTER (WHERE return_date >= NOW()) AS future_returns
FROM public.lunar_returns
GROUP BY user_id;

-- Prochains retours pour tous les users (dashboard admin)
SELECT 
    user_id,
    MIN(return_date) AS next_return_date
FROM public.lunar_returns
WHERE return_date >= NOW()
GROUP BY user_id
ORDER BY next_return_date ASC;

