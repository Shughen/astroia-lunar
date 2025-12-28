"""fix_transits_overview_user_id_uuid_to_integer

Revision ID: 7737e03699e5
Revises: 3f8a5b2c6d9e
Create Date: 2025-12-28 18:17:31.962910

Corrige l'incohérence de type: transits_overview.user_id était UUID dans la DB
mais Integer dans le modèle SQLAlchemy. Convertit la colonne en INTEGER pour
s'aligner avec users.id (INTEGER).

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision: str = '7737e03699e5'
down_revision: Union[str, None] = '3f8a5b2c6d9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """
    Convertit transits_overview.user_id de UUID vers INTEGER.
    Migration idempotente et sûre (vérifie le type avant conversion).
    """
    # Utiliser execute avec text() pour exécuter du SQL PostgreSQL natif
    conn = op.get_bind()
    
    # Vérifier le type actuel et convertir si nécessaire
    migration_sql = text("""
    DO $$
    DECLARE
        current_type TEXT;
        fk_name TEXT;
        deleted_count INTEGER;
    BEGIN
        -- Vérifier si la table existe
        IF NOT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = 'transits_overview'
        ) THEN
            RAISE NOTICE '⚠️ Table transits_overview n''existe pas - skip migration';
            RETURN;
        END IF;
        
        -- Vérifier le type actuel de user_id
        SELECT data_type INTO current_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'transits_overview'
          AND column_name = 'user_id';
        
        IF current_type IS NULL THEN
            RAISE NOTICE '⚠️ Colonne user_id n''existe pas dans transits_overview - skip migration';
            RETURN;
        END IF;
        
        RAISE NOTICE '📊 Type actuel de transits_overview.user_id: %', current_type;
        
        -- Si déjà INTEGER, pas besoin de migration
        IF current_type = 'integer' THEN
            RAISE NOTICE '✅ transits_overview.user_id est déjà INTEGER - pas de migration nécessaire';
            RETURN;
        END IF;
        
        -- Si UUID, on convertit vers INTEGER
        IF current_type = 'uuid' THEN
            RAISE NOTICE '🔄 Migration nécessaire: UUID -> INTEGER';
            
            -- Supprimer les données existantes (seront régénérées)
            DELETE FROM transits_overview;
            GET DIAGNOSTICS deleted_count = ROW_COUNT;
            RAISE NOTICE '🗑️  % entrée(s) supprimée(s)', deleted_count;
            
            -- Supprimer l'ancienne FK si elle existe
            SELECT constraint_name INTO fk_name
            FROM information_schema.table_constraints
            WHERE table_schema = 'public'
              AND table_name = 'transits_overview'
              AND constraint_name LIKE '%user_id%'
              AND constraint_type = 'FOREIGN KEY'
            LIMIT 1;
            
            IF fk_name IS NOT NULL THEN
                EXECUTE format('ALTER TABLE transits_overview DROP CONSTRAINT IF EXISTS %I', fk_name);
                RAISE NOTICE '✅ Ancienne FK supprimée: %', fk_name;
            END IF;
            
            -- Supprimer les index qui dépendent de user_id
            DROP INDEX IF EXISTS ix_transits_overview_user_month;
            
            -- Supprimer l'ancienne colonne user_id (UUID)
            ALTER TABLE transits_overview DROP COLUMN user_id CASCADE;
            RAISE NOTICE '✅ Ancienne colonne user_id (UUID) supprimée';
            
            -- Créer la nouvelle colonne user_id (INTEGER NOT NULL)
            ALTER TABLE transits_overview
            ADD COLUMN user_id INTEGER NOT NULL;
            
            -- Recréer l'index composite
            CREATE INDEX ix_transits_overview_user_month ON transits_overview(user_id, month);
            
            -- Ajouter la FK vers users.id
            ALTER TABLE transits_overview
            ADD CONSTRAINT fk_transits_overview_user_id
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE;
            
            RAISE NOTICE '✅ Migration réussie: user_id est maintenant INTEGER NOT NULL';
        ELSE
            RAISE WARNING '⚠️ Type inattendu: % - migration peut échouer', current_type;
        END IF;
    END $$;
    """)
    
    conn.execute(migration_sql)


def downgrade() -> None:
    """
    Rollback: convertit transits_overview.user_id de INTEGER vers UUID.
    ⚠️ ATTENTION: Cette opération peut perdre des données si users.id n'est pas UUID.
    """
    conn = op.get_bind()
    
    rollback_sql = text("""
    DO $$
    DECLARE
        current_type TEXT;
        fk_name TEXT;
    BEGIN
        -- Vérifier si la table existe
        IF NOT EXISTS (
            SELECT 1 FROM information_schema.tables 
            WHERE table_schema = 'public' AND table_name = 'transits_overview'
        ) THEN
            RETURN;
        END IF;
        
        -- Vérifier le type actuel
        SELECT data_type INTO current_type
        FROM information_schema.columns
        WHERE table_schema = 'public'
          AND table_name = 'transits_overview'
          AND column_name = 'user_id';
        
        -- Si déjà UUID, rien à faire
        IF current_type = 'uuid' THEN
            RAISE NOTICE '✅ Déjà en UUID - skip rollback';
            RETURN;
        END IF;
        
        -- Si INTEGER, convertir vers UUID
        IF current_type = 'integer' THEN
            -- Supprimer les données (car conversion INTEGER -> UUID impossible sans mapping)
            DELETE FROM transits_overview;
            
            -- Supprimer FK
            SELECT constraint_name INTO fk_name
            FROM information_schema.table_constraints
            WHERE table_schema = 'public'
              AND table_name = 'transits_overview'
              AND constraint_name LIKE '%user_id%'
              AND constraint_type = 'FOREIGN KEY'
            LIMIT 1;
            
            IF fk_name IS NOT NULL THEN
                EXECUTE format('ALTER TABLE transits_overview DROP CONSTRAINT IF EXISTS %I', fk_name);
            END IF;
            
            -- Supprimer index
            DROP INDEX IF EXISTS ix_transits_overview_user_month;
            
            -- Supprimer colonne INTEGER
            ALTER TABLE transits_overview DROP COLUMN user_id CASCADE;
            
            -- Créer colonne UUID
            ALTER TABLE transits_overview
            ADD COLUMN user_id UUID NOT NULL;
            
            -- Recréer index
            CREATE INDEX ix_transits_overview_user_month ON transits_overview(user_id, month);
            
            RAISE NOTICE '⚠️ Rollback effectué: user_id est maintenant UUID (FK non recréée - doit être manuelle)';
        END IF;
    END $$;
    """)
    
    conn.execute(rollback_sql)

