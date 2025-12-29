-- Migration: Modifier user_id de UUID vers INTEGER dans natal_interpretations
-- Date: 2025-12-29
-- Description: La table existe déjà avec user_id UUID, on la modifie pour utiliser INTEGER
--              pour correspondre au modèle User.id (Integer)

-- 1) Supprimer la contrainte de clé étrangère existante si elle existe
ALTER TABLE IF EXISTS public.natal_interpretations 
DROP CONSTRAINT IF EXISTS natal_interpretations_user_id_fkey;

-- 2) Supprimer les index qui utilisent user_id
DROP INDEX IF EXISTS public.idx_natal_interpretations_unique;
DROP INDEX IF EXISTS public.idx_natal_interpretations_user_chart;

-- 3) Supprimer toutes les données existantes (car on ne peut pas convertir UUID vers INTEGER)
--    Si vous avez des données importantes, il faudra les sauvegarder avant
TRUNCATE TABLE IF EXISTS public.natal_interpretations;

-- 4) Modifier le type de colonne user_id de UUID vers INTEGER
ALTER TABLE IF EXISTS public.natal_interpretations 
ALTER COLUMN user_id TYPE INTEGER USING NULL;

-- 5) Ajouter la contrainte de clé étrangère vers public.users(id)
ALTER TABLE IF EXISTS public.natal_interpretations 
ADD CONSTRAINT natal_interpretations_user_id_fkey 
FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;

-- 6) Recréer les index
CREATE UNIQUE INDEX IF NOT EXISTS idx_natal_interpretations_unique
    ON public.natal_interpretations(user_id, chart_id, subject, lang, version);

CREATE INDEX IF NOT EXISTS idx_natal_interpretations_user_chart
    ON public.natal_interpretations(user_id, chart_id);

-- 7) Vérifier que la colonne est bien de type INTEGER
DO $$
BEGIN
    IF EXISTS (
        SELECT 1 FROM information_schema.columns 
        WHERE table_schema = 'public' 
        AND table_name = 'natal_interpretations' 
        AND column_name = 'user_id' 
        AND data_type = 'integer'
    ) THEN
        RAISE NOTICE '✅ Colonne user_id modifiée avec succès en INTEGER';
    ELSE
        RAISE EXCEPTION '❌ Échec: user_id n''est pas de type INTEGER';
    END IF;
END $$;

