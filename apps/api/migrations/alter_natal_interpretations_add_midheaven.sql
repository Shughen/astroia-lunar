-- Migration: Ajouter 'midheaven' à la contrainte CHECK de subject
-- Date: 2025-12-29
-- Description: Met à jour la contrainte CHECK pour inclure 'midheaven' si elle n'est pas déjà présente

-- 1) Supprimer l'ancienne contrainte CHECK (si elle existe)
ALTER TABLE public.natal_interpretations 
    DROP CONSTRAINT IF EXISTS natal_interpretations_subject_check;

-- 2) Ajouter la nouvelle contrainte CHECK avec 'midheaven' inclus
ALTER TABLE public.natal_interpretations 
    ADD CONSTRAINT natal_interpretations_subject_check 
    CHECK (subject IN (
        'sun', 'moon', 'ascendant', 'midheaven',
        'mercury', 'venus', 'mars', 'jupiter', 'saturn',
        'uranus', 'neptune', 'pluto',
        'chiron', 'north_node', 'south_node', 'lilith'
    ));

