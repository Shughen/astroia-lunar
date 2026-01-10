"""make_user_id_nullable_in_natal_readings

Revision ID: f5b1dd89edf9
Revises: 5a9c8d3e4f6b
Create Date: 2025-11-24 19:29:24.506554

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5b1dd89edf9'
down_revision = '5a9c8d3e4f6b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Rend user_id nullable dans natal_readings.
    Les lectures natales sont partagées entre utilisateurs via cache_key,
    donc user_id n'est pas obligatoire.
    
    Utilise une requête SQL conditionnelle pour modifier la colonne
    uniquement si elle existe.
    """
    # Exécuter une requête SQL conditionnelle pour rendre user_id nullable
    # si la colonne existe
    op.execute("""
        DO $$ 
        BEGIN
            -- Vérifier si la colonne existe et la rendre nullable
            IF EXISTS (
                SELECT 1 
                FROM information_schema.columns 
                WHERE table_name = 'natal_readings' 
                AND column_name = 'user_id'
            ) THEN
                ALTER TABLE natal_readings 
                ALTER COLUMN user_id DROP NOT NULL;
            END IF;
        END $$;
    """)


def downgrade() -> None:
    """
    Revert: rendre user_id NOT NULL (si la colonne existe)
    Note: Attention, cela peut échouer si des valeurs NULL existent.
    """
    op.execute("""
        DO $$ 
        BEGIN
            -- Vérifier si la colonne existe et la rendre NOT NULL
            IF EXISTS (
                SELECT 1 
                FROM information_schema.columns 
                WHERE table_name = 'natal_readings' 
                AND column_name = 'user_id'
            ) THEN
                -- Mettre à jour les valeurs NULL avant de rendre NOT NULL
                UPDATE natal_readings SET user_id = 0 WHERE user_id IS NULL;
                
                ALTER TABLE natal_readings 
                ALTER COLUMN user_id SET NOT NULL;
            END IF;
        END $$;
    """)

