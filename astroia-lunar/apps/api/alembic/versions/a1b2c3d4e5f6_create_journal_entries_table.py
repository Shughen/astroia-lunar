"""create journal_entries table

Revision ID: a1b2c3d4e5f6
Revises: ff1311a24bb9
Create Date: 2026-01-16 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import text


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = 'ff1311a24bb9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    """
    Crée la table journal_entries pour les entrées de journal quotidien.
    Migration idempotente : vérifie si la table existe déjà.
    """
    conn = op.get_bind()

    # Vérifier si la table existe déjà (compatible PostgreSQL et SQLite)
    from sqlalchemy import inspect
    inspector = inspect(conn)
    table_exists = 'journal_entries' in inspector.get_table_names()

    if not table_exists:
        # Créer la table journal_entries
        op.create_table(
            'journal_entries',
            sa.Column('id', sa.Integer(), nullable=False),
            sa.Column('user_id', sa.Integer(), nullable=False),
            sa.Column('date', sa.Date(), nullable=False),
            sa.Column('mood', sa.String(), nullable=True),
            sa.Column('note', sa.Text(), nullable=True),
            sa.Column('month', sa.String(), nullable=True),
            sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
            sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
            sa.PrimaryKeyConstraint('id'),
            sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE')
        )

        # Créer les index
        op.create_index('ix_journal_entries_user_id', 'journal_entries', ['user_id'], unique=False)
        op.create_index('ix_journal_entries_date', 'journal_entries', ['date'], unique=False)
        op.create_index('ix_journal_entries_month', 'journal_entries', ['month'], unique=False)


def downgrade() -> None:
    # Drop index
    op.drop_index('ix_journal_entries_month', table_name='journal_entries')
    op.drop_index('ix_journal_entries_date', table_name='journal_entries')
    op.drop_index('ix_journal_entries_user_id', table_name='journal_entries')

    # Drop table
    op.drop_table('journal_entries')
