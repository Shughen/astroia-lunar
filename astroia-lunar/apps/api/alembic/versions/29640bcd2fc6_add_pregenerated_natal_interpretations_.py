"""add pregenerated natal interpretations table

Revision ID: 29640bcd2fc6
Revises: 4c67743b2a3f
Create Date: 2026-01-18 12:00:15.051507

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID


# revision identifiers, used by Alembic.
revision = '29640bcd2fc6'
down_revision = '4c67743b2a3f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Créer la table pregenerated_natal_interpretations
    op.create_table(
        'pregenerated_natal_interpretations',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),  # UUID généré côté Python par SQLAlchemy
        sa.Column('subject', sa.String(50), nullable=False),
        sa.Column('sign', sa.String(50), nullable=False),
        sa.Column('house', sa.Integer, nullable=False),
        sa.Column('version', sa.Integer, nullable=False, server_default='2'),
        sa.Column('lang', sa.String(10), nullable=False, server_default='fr'),
        sa.Column('content', sa.Text, nullable=False),
        sa.Column('length', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    # Créer les index
    op.create_index('idx_pregenerated_unique', 'pregenerated_natal_interpretations',
                    ['subject', 'sign', 'house', 'version', 'lang'], unique=True)
    op.create_index('idx_pregenerated_lookup', 'pregenerated_natal_interpretations',
                    ['subject', 'sign', 'house', 'version', 'lang'])
    op.create_index('idx_pregenerated_created_at', 'pregenerated_natal_interpretations', ['created_at'])


def downgrade() -> None:
    # Supprimer les index
    op.drop_index('idx_pregenerated_created_at', 'pregenerated_natal_interpretations')
    op.drop_index('idx_pregenerated_lookup', 'pregenerated_natal_interpretations')
    op.drop_index('idx_pregenerated_unique', 'pregenerated_natal_interpretations')

    # Supprimer la table
    op.drop_table('pregenerated_natal_interpretations')

