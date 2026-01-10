"""add natal_readings table

Revision ID: 5a9c8d3e4f6b
Revises: 3f8a5b2c6d9e
Create Date: 2025-11-12 20:30:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '5a9c8d3e4f6b'
down_revision = '3f8a5b2c6d9e'  # Lien vers la migration précédente
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Create natal_readings table"""
    op.create_table(
        'natal_readings',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('cache_key', sa.String(), nullable=False),
        sa.Column('birth_data', postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column('reading', postgresql.JSON(astext_type=sa.Text()), nullable=False),
        sa.Column('source', sa.String(), nullable=True),
        sa.Column('api_calls_count', sa.Integer(), nullable=True),
        sa.Column('language', sa.String(), nullable=True),
        sa.Column('includes_full_report', sa.Boolean(), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.Column('last_accessed_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_natal_readings_cache_key'), 'natal_readings', ['cache_key'], unique=True)
    op.create_index(op.f('ix_natal_readings_created_at'), 'natal_readings', ['created_at'], unique=False)
    op.create_index(op.f('ix_natal_readings_id'), 'natal_readings', ['id'], unique=False)


def downgrade() -> None:
    """Drop natal_readings table"""
    op.drop_index(op.f('ix_natal_readings_id'), table_name='natal_readings')
    op.drop_index(op.f('ix_natal_readings_created_at'), table_name='natal_readings')
    op.drop_index(op.f('ix_natal_readings_cache_key'), table_name='natal_readings')
    op.drop_table('natal_readings')
