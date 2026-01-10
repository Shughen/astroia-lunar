"""fix lunar_returns return_date timestamptz

Revision ID: ff1311a24bb9
Revises: 63651f3982e9
Create Date: 2026-01-04 11:51:39.971785

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = 'ff1311a24bb9'
down_revision = '63651f3982e9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Convertit lunar_returns.return_date de VARCHAR vers TIMESTAMPTZ.
    
    Étapes:
    1. Nettoyer les valeurs NULL existantes (les mettre à une date par défaut si nécessaire)
    2. Convertir la colonne en TIMESTAMPTZ avec cast
    3. Changer nullable à False (pour correspondre au modèle SQLAlchemy)
    4. Créer l'index sur return_date (demandé par le modèle)
    """
    conn = op.get_bind()
    
    migration_sql = text("""
    DO $$
    DECLARE
        current_type TEXT;
        column_exists BOOLEAN;
    BEGIN
        -- Vérifier si la colonne existe
        SELECT EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_schema = 'public'
              AND table_name = 'lunar_returns'
              AND column_name = 'return_date'
        ) INTO column_exists;
        
        IF NOT column_exists THEN
            RAISE NOTICE '⚠️ Colonne return_date n''existe pas - skip migration';
            RETURN;
        END IF;
        
        -- Vérifier le type actuel
        SELECT data_type INTO current_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND column_name = 'return_date';
        
        RAISE NOTICE '📊 Type actuel de lunar_returns.return_date: %', current_type;
        
        -- Si déjà timestamptz, pas besoin de migration
        IF current_type = 'timestamp with time zone' OR current_type = 'timestamptz' THEN
            RAISE NOTICE '✅ lunar_returns.return_date est déjà TIMESTAMPTZ - pas de migration nécessaire';
            
            -- Vérifier et créer l'index si nécessaire
            IF NOT EXISTS (
                SELECT 1 FROM pg_indexes
                WHERE tablename = 'lunar_returns'
                  AND indexname = 'ix_lunar_returns_return_date'
            ) THEN
                CREATE INDEX ix_lunar_returns_return_date ON lunar_returns(return_date);
                RAISE NOTICE '✅ Index ix_lunar_returns_return_date créé';
            END IF;
            
            -- Changer nullable à False si nécessaire
            IF EXISTS (
                SELECT 1 FROM information_schema.columns
                WHERE table_schema = 'public'
                  AND table_name = 'lunar_returns'
                  AND column_name = 'return_date'
                  AND is_nullable = 'YES'
            ) THEN
                -- Nettoyer les valeurs NULL avant de changer nullable
                UPDATE lunar_returns
                SET return_date = NOW() AT TIME ZONE 'UTC'
                WHERE return_date IS NULL;
                
                ALTER TABLE lunar_returns
                ALTER COLUMN return_date SET NOT NULL;
                RAISE NOTICE '✅ return_date est maintenant NOT NULL';
            END IF;
            
            RETURN;
        END IF;
        
        -- Si VARCHAR/TEXT, convertir vers TIMESTAMPTZ
        IF current_type IN ('character varying', 'varchar', 'text') THEN
            RAISE NOTICE '🔄 Migration nécessaire: VARCHAR -> TIMESTAMPTZ';
            
            -- Étape 1: Nettoyer les valeurs NULL (les remplacer par une date par défaut)
            UPDATE lunar_returns
            SET return_date = NOW() AT TIME ZONE 'UTC'
            WHERE return_date IS NULL OR return_date = '';
            
            -- Étape 2: Convertir la colonne en TIMESTAMPTZ avec cast
            ALTER TABLE lunar_returns
            ALTER COLUMN return_date TYPE TIMESTAMP WITH TIME ZONE
            USING return_date::timestamptz;
            
            RAISE NOTICE '✅ Colonne convertie en TIMESTAMPTZ';
            
            -- Étape 3: Changer nullable à False
            ALTER TABLE lunar_returns
            ALTER COLUMN return_date SET NOT NULL;
            
            RAISE NOTICE '✅ return_date est maintenant NOT NULL';
            
            -- Étape 4: Créer l'index sur return_date (si n'existe pas)
            IF NOT EXISTS (
                SELECT 1 FROM pg_indexes
                WHERE tablename = 'lunar_returns'
                  AND indexname = 'ix_lunar_returns_return_date'
            ) THEN
                CREATE INDEX ix_lunar_returns_return_date ON lunar_returns(return_date);
                RAISE NOTICE '✅ Index ix_lunar_returns_return_date créé';
            END IF;
            
            RAISE NOTICE '✅ Migration réussie: return_date est maintenant TIMESTAMPTZ NOT NULL';
        ELSE
            RAISE WARNING '⚠️ Type inattendu: % - migration peut échouer', current_type;
        END IF;
    END $$;
    """)
    
    conn.execute(migration_sql)


def downgrade() -> None:
    """
    Rollback: convertit lunar_returns.return_date de TIMESTAMPTZ vers TEXT.
    """
    conn = op.get_bind()
    
    rollback_sql = text("""
    DO $$
    DECLARE
        current_type TEXT;
    BEGIN
        -- Vérifier le type actuel
        SELECT data_type INTO current_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'lunar_returns'
          AND column_name = 'return_date';
        
        -- Si déjà TEXT/VARCHAR, rien à faire
        IF current_type IN ('character varying', 'varchar', 'text') THEN
            RAISE NOTICE '✅ Déjà en TEXT - skip rollback';
            RETURN;
        END IF;
        
        -- Si TIMESTAMPTZ, convertir vers TEXT
        IF current_type = 'timestamp with time zone' OR current_type = 'timestamptz' THEN
            -- Supprimer l'index d'abord
            DROP INDEX IF EXISTS ix_lunar_returns_return_date;
            
            -- Reconvertir en TEXT avec cast
            ALTER TABLE lunar_returns
            ALTER COLUMN return_date TYPE TEXT
            USING return_date::text;
            
            -- Changer nullable à True (car TEXT peut être NULL)
            ALTER TABLE lunar_returns
            ALTER COLUMN return_date DROP NOT NULL;
            
            RAISE NOTICE '⚠️ Rollback effectué: return_date est maintenant TEXT';
        END IF;
    END $$;
    """)
    
    conn.execute(rollback_sql)
