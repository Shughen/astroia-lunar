#!/usr/bin/env python3
"""
Script pour ajouter 'midheaven' à la contrainte CHECK de subject dans natal_interpretations
"""
import asyncio
import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy import text
from database import engine


async def migrate():
    """Exécute la migration pour ajouter 'midheaven' à la contrainte CHECK"""
    
    migration_sql = """
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
    """
    
    async with engine.begin() as conn:
        print("🔄 Suppression de l'ancienne contrainte CHECK...")
        await conn.execute(text("ALTER TABLE public.natal_interpretations DROP CONSTRAINT IF EXISTS natal_interpretations_subject_check;"))
        
        print("✅ Ajout de la nouvelle contrainte CHECK avec 'midheaven'...")
        await conn.execute(text("""
            ALTER TABLE public.natal_interpretations 
            ADD CONSTRAINT natal_interpretations_subject_check 
            CHECK (subject IN (
                'sun', 'moon', 'ascendant', 'midheaven',
                'mercury', 'venus', 'mars', 'jupiter', 'saturn',
                'uranus', 'neptune', 'pluto',
                'chiron', 'north_node', 'south_node', 'lilith'
            ));
        """))
        
        print("✅ Migration terminée avec succès !")
        print("   La contrainte CHECK inclut maintenant 'midheaven'.")


if __name__ == "__main__":
    asyncio.run(migrate())

