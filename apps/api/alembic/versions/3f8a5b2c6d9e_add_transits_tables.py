"""add_transits_tables

Revision ID: 3f8a5b2c6d9e
Revises: 2e3f9a1c4b5d
Create Date: 2025-01-15 12:00:00.000000

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '3f8a5b2c6d9e'
down_revision: Union[str, None] = '2e3f9a1c4b5d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Créer la table transits_overview
    # NOTE: Cette migration créait la colonne 'summary', mais elle a été renommée en 'overview'
    # dans la DB réelle. Le modèle SQLAlchemy (models/transits.py) utilise maintenant 'overview'.
    # Si cette migration n'a pas encore été exécutée, remplacer 'summary' par 'overview' ci-dessous.
    op.create_table(
        'transits_overview',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('month', sa.String(), nullable=False),
        sa.Column('summary', postgresql.JSONB(astext_type=sa.Text()), nullable=False),  # RENOMMÉ EN 'overview' dans la DB
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transits_overview_id'), 'transits_overview', ['id'], unique=False)
    op.create_index(op.f('ix_transits_overview_month'), 'transits_overview', ['month'], unique=False)
    op.create_index('ix_transits_overview_user_month', 'transits_overview', ['user_id', 'month'], unique=False)

    # Créer la table transits_events
    op.create_table(
        'transits_events',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=False),
        sa.Column('date', sa.Date(), nullable=False),
        sa.Column('transit_planet', sa.String(), nullable=False),
        sa.Column('natal_point', sa.String(), nullable=False),
        sa.Column('aspect_type', sa.String(), nullable=False),
        sa.Column('orb', sa.Integer(), nullable=False),
        sa.Column('interpretation', sa.Text(), nullable=True),
        sa.Column('raw_data', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_transits_events_id'), 'transits_events', ['id'], unique=False)
    op.create_index(op.f('ix_transits_events_date'), 'transits_events', ['date'], unique=False)
    op.create_index('ix_transits_events_user_date', 'transits_events', ['user_id', 'date'], unique=False)
    op.create_index('ix_transits_events_planet_aspect', 'transits_events', ['transit_planet', 'aspect_type'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_transits_events_planet_aspect', table_name='transits_events')
    op.drop_index('ix_transits_events_user_date', table_name='transits_events')
    op.drop_index(op.f('ix_transits_events_date'), table_name='transits_events')
    op.drop_index(op.f('ix_transits_events_id'), table_name='transits_events')
    op.drop_table('transits_events')
    
    op.drop_index('ix_transits_overview_user_month', table_name='transits_overview')
    op.drop_index(op.f('ix_transits_overview_month'), table_name='transits_overview')
    op.drop_index(op.f('ix_transits_overview_id'), table_name='transits_overview')
    op.drop_table('transits_overview')

