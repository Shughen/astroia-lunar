#!/usr/bin/env python3
"""
Script pour appliquer la migration lunar_returns.user_id UUID -> INTEGER
Peut être exécuté directement depuis Python
"""

import asyncio
import sys
from sqlalchemy import text
from database import engine
from config import settings

MIGRATION_SQL = """
-- Migration: Convertir lunar_returns.user_id de UUID vers INTEGER
DO $$
DECLARE
    current_type TEXT;
    deleted_count INTEGER;
BEGIN
    -- Vérifier le type actuel
    SELECT data_type INTO current_type
    FROM information_schema.columns
    WHERE table_schema = 'public'
      AND table_name = 'lunar_returns'
      AND column_name = 'user_id';
    
    IF current_type IS NULL THEN
        RAISE NOTICE '⚠️ Colonne user_id n''existe pas dans lunar_returns';
        RETURN;
    END IF;
    
    RAISE NOTICE '📊 Type actuel de lunar_returns.user_id: %', current_type;
    
    -- Si déjà INTEGER, pas besoin de migration
    IF current_type = 'integer' THEN
        RAISE NOTICE '✅ lunar_returns.user_id est déjà INTEGER - pas de migration nécessaire';
        RETURN;
    END IF;
    
    -- Si UUID, on continue la migration
    IF current_type = 'uuid' THEN
        RAISE NOTICE '🔄 Migration nécessaire: UUID -> INTEGER';
        
        -- Supprimer les données existantes (elles seront régénérées)
        DELETE FROM lunar_returns;
        GET DIAGNOSTICS deleted_count = ROW_COUNT;
        RAISE NOTICE '🗑️  % entrée(s) supprimée(s)', deleted_count;
        
        -- Supprimer l'ancienne FK si elle existe
        DECLARE
            fk_name TEXT;
        BEGIN
            SELECT constraint_name INTO fk_name
            FROM information_schema.table_constraints
            WHERE table_schema = 'public'
              AND table_name = 'lunar_returns'
              AND constraint_name LIKE '%user_id%'
              AND constraint_type = 'FOREIGN KEY'
            LIMIT 1;
            
            IF fk_name IS NOT NULL THEN
                EXECUTE format('ALTER TABLE lunar_returns DROP CONSTRAINT IF EXISTS %I', fk_name);
                RAISE NOTICE '✅ Ancienne FK supprimée: %', fk_name;
            END IF;
        END;
        
        -- Supprimer l'ancienne colonne user_id (UUID)
        ALTER TABLE lunar_returns DROP COLUMN user_id;
        RAISE NOTICE '✅ Ancienne colonne user_id (UUID) supprimée';
        
        -- Créer la nouvelle colonne user_id (INTEGER)
        ALTER TABLE lunar_returns
        ADD COLUMN user_id INTEGER NOT NULL;
        
        -- Ajouter la FK
        ALTER TABLE lunar_returns
        ADD CONSTRAINT fk_lunar_returns_user_id
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
        
        RAISE NOTICE '✅ Migration réussie: user_id est maintenant INTEGER NOT NULL';
    ELSE
        RAISE WARNING '⚠️ Type inattendu: % - migration peut échouer', current_type;
    END IF;
END $$;
"""


async def apply_migration():
    """Applique la migration SQL"""
    print("🔄 Application de la migration lunar_returns.user_id UUID -> INTEGER...")
    print(f"📊 Database: {settings.DATABASE_URL.split('@')[1] if '@' in settings.DATABASE_URL else 'local'}")
    print()
    
    async with engine.begin() as conn:
        try:
            result = await conn.execute(text(MIGRATION_SQL))
            print("✅ Migration exécutée avec succès")
            print()
            print("📋 Vérification du schéma final...")
            
            # Vérifier le type final
            check_result = await conn.execute(text("""
                SELECT data_type, is_nullable
                FROM information_schema.columns
                WHERE table_schema = 'public'
                  AND table_name = 'lunar_returns'
                  AND column_name = 'user_id'
            """))
            
            row = check_result.fetchone()
            if row:
                data_type, is_nullable = row
                print(f"   Type: {data_type}")
                print(f"   Nullable: {is_nullable}")
                
                if data_type == 'integer' and is_nullable == 'NO':
                    print()
                    print("✅ Migration réussie ! lunar_returns.user_id est maintenant INTEGER NOT NULL")
                    return 0
                else:
                    print()
                    print(f"⚠️  Migration incomplète: type={data_type}, nullable={is_nullable}")
                    return 1
            else:
                print()
                print("❌ Colonne user_id n'existe pas après migration")
                return 1
                
        except Exception as e:
            print(f"❌ Erreur lors de la migration: {e}")
            import traceback
            traceback.print_exc()
            return 1


if __name__ == "__main__":
    exit_code = asyncio.run(apply_migration())
    sys.exit(exit_code)

