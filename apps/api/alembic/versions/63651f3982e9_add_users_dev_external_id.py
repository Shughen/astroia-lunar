"""add users.dev_external_id

Revision ID: 63651f3982e9
Revises: 9737ece7c259
Create Date: 2026-01-04 00:28:37.834010

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = '63651f3982e9'
down_revision = '9737ece7c259'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Ajoute la colonne dev_external_id à la table users.
    Migration idempotente : vérifie si la colonne existe déjà.
    """
    conn = op.get_bind()
    
    # Vérifier si la colonne existe déjà
    check_sql = text("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.columns
            WHERE table_schema = 'public'
              AND table_name = 'users'
              AND column_name = 'dev_external_id'
        )
    """)
    
    column_exists = conn.execute(check_sql).scalar()
    
    if not column_exists:
        # Ajouter la colonne seulement si elle n'existe pas
        op.add_column("users", sa.Column("dev_external_id", sa.String(), nullable=True))
    
    # Créer la contrainte unique seulement si elle n'existe pas
    constraint_sql = text("""
        SELECT EXISTS (
            SELECT 1 FROM information_schema.table_constraints
            WHERE table_schema = 'public'
              AND table_name = 'users'
              AND constraint_name = 'uq_users_dev_external_id'
              AND constraint_type = 'UNIQUE'
        )
    """)
    
    constraint_exists = conn.execute(constraint_sql).scalar()
    
    if not constraint_exists:
        op.create_unique_constraint("uq_users_dev_external_id", "users", ["dev_external_id"])
    
    # Créer l'index seulement s'il n'existe pas
    index_sql = text("""
        SELECT EXISTS (
            SELECT 1 FROM pg_indexes
            WHERE tablename = 'users'
              AND indexname = 'ix_users_dev_external_id'
        )
    """)
    
    index_exists = conn.execute(index_sql).scalar()
    
    if not index_exists:
        op.create_index("ix_users_dev_external_id", "users", ["dev_external_id"], unique=False)


def downgrade() -> None:
    # Drop index
    op.drop_index("ix_users_dev_external_id", table_name="users")
    
    # Drop unique constraint
    op.drop_constraint("uq_users_dev_external_id", "users", type_="unique")
    
    # Drop column
    op.drop_column("users", "dev_external_id")

