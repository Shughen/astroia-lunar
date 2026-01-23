"""create lunar_interpretations table

Revision ID: 6b2c3d4e5f6a
Revises: 5a1b2c3d4e5f
Create Date: 2026-01-23 14:05:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB


# revision identifiers, used by Alembic.
revision = '6b2c3d4e5f6a'
down_revision = '5a1b2c3d4e5f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Créer la table lunar_interpretations
    op.create_table(
        'lunar_interpretations',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id', ondelete='CASCADE'), nullable=False),
        sa.Column('lunar_return_id', sa.Integer, sa.ForeignKey('lunar_returns.id', ondelete='CASCADE'), nullable=False),
        sa.Column('subject', sa.String(50), nullable=False),
        sa.Column('version', sa.Integer, nullable=False, server_default='2'),
        sa.Column('lang', sa.String(10), nullable=False, server_default='fr'),
        sa.Column('input_json', JSONB, nullable=False),
        sa.Column('output_text', sa.Text, nullable=False),
        sa.Column('weekly_advice', JSONB, nullable=True),
        sa.Column('model_used', sa.String(50), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    # Créer les index
    op.create_index('idx_lunar_interpretations_unique', 'lunar_interpretations',
                    ['lunar_return_id', 'subject', 'lang', 'version'], unique=True)
    op.create_index('idx_lunar_interpretations_user', 'lunar_interpretations', ['user_id'])
    op.create_index('idx_lunar_interpretations_return', 'lunar_interpretations', ['lunar_return_id'])
    op.create_index('idx_lunar_interpretations_subject', 'lunar_interpretations', ['subject'])
    op.create_index('idx_lunar_interpretations_created_at', 'lunar_interpretations', ['created_at'])
    op.create_index('idx_lunar_interpretations_lookup', 'lunar_interpretations',
                    ['lunar_return_id', 'subject', 'lang', 'version'])


def downgrade() -> None:
    # Supprimer les index
    op.drop_index('idx_lunar_interpretations_lookup', 'lunar_interpretations')
    op.drop_index('idx_lunar_interpretations_created_at', 'lunar_interpretations')
    op.drop_index('idx_lunar_interpretations_subject', 'lunar_interpretations')
    op.drop_index('idx_lunar_interpretations_return', 'lunar_interpretations')
    op.drop_index('idx_lunar_interpretations_user', 'lunar_interpretations')
    op.drop_index('idx_lunar_interpretations_unique', 'lunar_interpretations')

    # Supprimer la table
    op.drop_table('lunar_interpretations')
