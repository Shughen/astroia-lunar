-- Migration: Créer table natal_interpretations pour cacher les interprétations générées par Claude
-- Date: 2025-12-29
-- Description: Stocke les interprétations astrologiques par objet céleste (Soleil, Lune, planètes, Ascendant)
--              avec cache intelligent basé sur chart_id stable

-- 1) Créer la table
CREATE TABLE IF NOT EXISTS public.natal_interpretations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id INTEGER NOT NULL REFERENCES public.users(id) ON DELETE CASCADE,
    chart_id TEXT NOT NULL,
    subject TEXT NOT NULL CHECK (subject IN (
        'sun', 'moon', 'ascendant', 'midheaven',
        'mercury', 'venus', 'mars', 'jupiter', 'saturn',
        'uranus', 'neptune', 'pluto',
        'chiron', 'north_node', 'south_node', 'lilith'
    )),
    lang TEXT NOT NULL DEFAULT 'fr' CHECK (lang IN ('fr', 'en')),
    version INT NOT NULL DEFAULT 1,
    input_json JSONB NOT NULL,
    output_text TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

-- 2) Index unique pour éviter les doublons
CREATE UNIQUE INDEX IF NOT EXISTS idx_natal_interpretations_unique
    ON public.natal_interpretations(user_id, chart_id, subject, lang, version);

-- 3) Index de performance pour les queries
CREATE INDEX IF NOT EXISTS idx_natal_interpretations_user_chart
    ON public.natal_interpretations(user_id, chart_id);

CREATE INDEX IF NOT EXISTS idx_natal_interpretations_created_at
    ON public.natal_interpretations(created_at DESC);

-- 4) Trigger auto-update du updated_at
CREATE OR REPLACE FUNCTION update_natal_interpretations_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_natal_interpretations_updated_at
    BEFORE UPDATE ON public.natal_interpretations
    FOR EACH ROW
    EXECUTE FUNCTION update_natal_interpretations_updated_at();

-- 5) RLS (Row Level Security) Policies
ALTER TABLE public.natal_interpretations ENABLE ROW LEVEL SECURITY;

-- Policy: Les utilisateurs peuvent lire uniquement leurs propres interprétations
CREATE POLICY "Users can view their own interpretations"
    ON public.natal_interpretations
    FOR SELECT
    USING (auth.uid() = user_id);

-- Policy: Les utilisateurs peuvent insérer uniquement leurs propres interprétations
CREATE POLICY "Users can insert their own interpretations"
    ON public.natal_interpretations
    FOR INSERT
    WITH CHECK (auth.uid() = user_id);

-- Policy: Les utilisateurs peuvent mettre à jour uniquement leurs propres interprétations
CREATE POLICY "Users can update their own interpretations"
    ON public.natal_interpretations
    FOR UPDATE
    USING (auth.uid() = user_id)
    WITH CHECK (auth.uid() = user_id);

-- Policy: Les utilisateurs peuvent supprimer uniquement leurs propres interprétations
CREATE POLICY "Users can delete their own interpretations"
    ON public.natal_interpretations
    FOR DELETE
    USING (auth.uid() = user_id);

-- 6) Commentaires pour documentation
COMMENT ON TABLE public.natal_interpretations IS 'Stocke les interprétations astrologiques générées par Claude pour chaque objet céleste du thème natal';
COMMENT ON COLUMN public.natal_interpretations.chart_id IS 'Identifiant stable du thème natal (hash basé sur date/heure/lieu de naissance)';
COMMENT ON COLUMN public.natal_interpretations.subject IS 'Objet céleste concerné (sun, moon, ascendant, planètes)';
COMMENT ON COLUMN public.natal_interpretations.lang IS 'Langue de l''interprétation (fr ou en)';
COMMENT ON COLUMN public.natal_interpretations.version IS 'Version du prompt/modèle utilisé (permet de régénérer si on améliore le prompt)';
COMMENT ON COLUMN public.natal_interpretations.input_json IS 'Données d''entrée (signe, maison, degré, etc.) pour transparence et debug';
COMMENT ON COLUMN public.natal_interpretations.output_text IS 'Texte d''interprétation généré par Claude (markdown)';

-- 7) Grant permissions (si nécessaire selon votre config Supabase)
-- GRANT ALL ON public.natal_interpretations TO authenticated;
-- GRANT USAGE ON SCHEMA public TO authenticated;
