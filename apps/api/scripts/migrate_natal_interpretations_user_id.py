#!/usr/bin/env python3
"""
Script pour migrer user_id de UUID vers INTEGER dans natal_interpretations
"""

import asyncio
import sys
from pathlib import Path

# Ajouter le répertoire parent au path pour importer les modules
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import engine
from sqlalchemy import text
from config import settings

async def migrate():
    """Migre user_id de UUID vers INTEGER"""
    print("🔄 Migration: user_id UUID → INTEGER dans natal_interpretations")
    print(f"📊 Database: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'local'}")
    
    async with engine.begin() as conn:
        # Vérifier si la table existe
        result = await conn.execute(text("""
            SELECT EXISTS (
                SELECT FROM information_schema.tables 
                WHERE table_schema = 'public' 
                AND table_name = 'natal_interpretations'
            )
        """))
        table_exists = result.scalar()
        
        if not table_exists:
            print("ℹ️  La table natal_interpretations n'existe pas encore")
            print("   Elle sera créée avec le bon type (INTEGER) lors de la première utilisation")
            return
        
        # Vérifier le type actuel de user_id
        result = await conn.execute(text("""
            SELECT data_type 
            FROM information_schema.columns 
            WHERE table_schema = 'public' 
            AND table_name = 'natal_interpretations' 
            AND column_name = 'user_id'
        """))
        row = result.first()
        
        if not row:
            print("⚠️  Colonne user_id introuvable")
            return
        
        current_type = row[0]
        print(f"📊 Type actuel de user_id: {current_type}")
        
        if current_type == 'integer':
            print("✅ La colonne est déjà en INTEGER, pas besoin de migration")
            return
        
        if current_type != 'uuid':
            print(f"⚠️  Type inattendu: {current_type}")
            return
        
        print("⚠️  La colonne est en UUID, exécution de la migration...")
        
        # Exécuter la migration étape par étape
        try:
            # 1) Supprimer les politiques RLS qui utilisent user_id
            await conn.execute(text("DROP POLICY IF EXISTS \"Users can view their own interpretations\" ON public.natal_interpretations"))
            await conn.execute(text("DROP POLICY IF EXISTS \"Users can insert their own interpretations\" ON public.natal_interpretations"))
            await conn.execute(text("DROP POLICY IF EXISTS \"Users can update their own interpretations\" ON public.natal_interpretations"))
            await conn.execute(text("DROP POLICY IF EXISTS \"Users can delete their own interpretations\" ON public.natal_interpretations"))
            print("  ✅ Politiques RLS supprimées")
            
            # 2) Supprimer la contrainte de clé étrangère existante si elle existe
            await conn.execute(text("""
                ALTER TABLE public.natal_interpretations 
                DROP CONSTRAINT IF EXISTS natal_interpretations_user_id_fkey
            """))
            print("  ✅ Contrainte FK supprimée")
            
            # 3) Supprimer les index qui utilisent user_id
            await conn.execute(text("DROP INDEX IF EXISTS public.idx_natal_interpretations_unique"))
            await conn.execute(text("DROP INDEX IF EXISTS public.idx_natal_interpretations_user_chart"))
            print("  ✅ Index supprimés")
            
            # 4) Supprimer toutes les données existantes (car on ne peut pas convertir UUID vers INTEGER)
            await conn.execute(text("TRUNCATE TABLE public.natal_interpretations"))
            print("  ✅ Données supprimées")
            
            # 5) Modifier le type de colonne user_id de UUID vers INTEGER
            await conn.execute(text("""
                ALTER TABLE public.natal_interpretations 
                ALTER COLUMN user_id TYPE INTEGER USING NULL
            """))
            print("  ✅ Type de colonne modifié")
            
            # 6) Ajouter la contrainte de clé étrangère vers public.users(id)
            await conn.execute(text("""
                ALTER TABLE public.natal_interpretations 
                ADD CONSTRAINT natal_interpretations_user_id_fkey 
                FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE
            """))
            print("  ✅ Contrainte FK ajoutée")
            
            # 7) Recréer les index
            await conn.execute(text("""
                CREATE UNIQUE INDEX IF NOT EXISTS idx_natal_interpretations_unique
                ON public.natal_interpretations(user_id, chart_id, subject, lang, version)
            """))
            await conn.execute(text("""
                CREATE INDEX IF NOT EXISTS idx_natal_interpretations_user_chart
                ON public.natal_interpretations(user_id, chart_id)
            """))
            print("  ✅ Index recréés")
            
            # 8) Recréer les politiques RLS (mais adaptées pour INTEGER au lieu de UUID)
            # Note: Les politiques RLS utilisent auth.uid() qui est un UUID Supabase
            # Pour FastAPI, on désactive RLS ou on adapte les politiques
            # Pour l'instant, on laisse RLS désactivé car FastAPI gère l'authentification
            print("  ℹ️  RLS: Les politiques seront recréées si nécessaire (actuellement géré par FastAPI)")
            
            print("✅ Migration exécutée avec succès")
            
            # Vérifier le nouveau type
            result = await conn.execute(text("""
                SELECT data_type 
                FROM information_schema.columns 
                WHERE table_schema = 'public' 
                AND table_name = 'natal_interpretations' 
                AND column_name = 'user_id'
            """))
            new_type = result.scalar()
            print(f"✅ Nouveau type de user_id: {new_type}")
            
        except Exception as e:
            print(f"❌ Erreur lors de la migration: {e}")
            raise

if __name__ == "__main__":
    asyncio.run(migrate())

