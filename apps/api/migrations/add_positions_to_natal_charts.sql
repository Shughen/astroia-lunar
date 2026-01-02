-- Migration: Ajouter colonne positions JSONB à natal_charts
-- Date: 2025-01-XX
-- Objectif: Aligner le schéma DB avec le modèle SQLAlchemy qui attend positions JSONB

-- Étape 1: Ajouter la colonne positions (nullable pour permettre migration progressive)
ALTER TABLE public.natal_charts
ADD COLUMN IF NOT EXISTS positions JSONB;

-- Étape 2: Migrer les données depuis les colonnes existantes vers positions
-- Structure attendue dans positions:
-- {
--   "sun": {...},
--   "moon": {...},
--   "ascendant": {...},
--   "planets": {...},
--   "houses": {...},
--   "aspects": [...]
-- }
UPDATE public.natal_charts
SET positions = (
    SELECT jsonb_build_object(
        'sun', CASE 
            WHEN sun_sign IS NOT NULL THEN jsonb_build_object('sign', sun_sign)
            ELSE NULL
        END,
        'moon', CASE 
            WHEN moon_sign IS NOT NULL THEN jsonb_build_object('sign', moon_sign)
            ELSE NULL
        END,
        'ascendant', CASE 
            WHEN ascendant IS NOT NULL THEN jsonb_build_object('sign', ascendant)
            ELSE NULL
        END,
        'planets', COALESCE(planets::jsonb, '{}'::jsonb),
        'houses', COALESCE(houses::jsonb, '{}'::jsonb),
        'aspects', COALESCE(aspects::jsonb, '[]'::jsonb)
    )
)
WHERE positions IS NULL 
  AND (sun_sign IS NOT NULL OR moon_sign IS NOT NULL OR ascendant IS NOT NULL 
       OR planets IS NOT NULL OR houses IS NOT NULL OR aspects IS NOT NULL);

-- Étape 3: Si raw_data existe et contient déjà la structure positions, l'utiliser
-- raw_data est de type JSON, donc on le convertit en JSONB
UPDATE public.natal_charts
SET positions = (raw_data::jsonb)->'positions'
WHERE positions IS NULL 
  AND raw_data IS NOT NULL 
  AND (raw_data::jsonb) ? 'positions'
  AND jsonb_typeof((raw_data::jsonb)->'positions') = 'object';

-- Étape 4: Si raw_data existe mais n'a pas de clé 'positions', utiliser raw_data directement
-- (si raw_data a déjà la structure attendue: sun, moon, planets, etc.)
UPDATE public.natal_charts
SET positions = raw_data::jsonb
WHERE positions IS NULL 
  AND raw_data IS NOT NULL
  AND jsonb_typeof(raw_data::jsonb) = 'object'
  AND ((raw_data::jsonb) ? 'sun' OR (raw_data::jsonb) ? 'moon' OR (raw_data::jsonb) ? 'planets');

-- Étape 5: Créer un index GIN sur positions pour les requêtes JSONB
CREATE INDEX IF NOT EXISTS idx_natal_charts_positions_gin 
ON public.natal_charts USING GIN (positions);

-- Étape 6: Commenter la colonne pour documentation
COMMENT ON COLUMN public.natal_charts.positions IS 
'Données astrologiques au format JSONB. Contient: sun, moon, ascendant, planets, houses, aspects';

