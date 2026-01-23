"""create lunar_interpretation_templates table

Revision ID: 5a1b2c3d4e5f
Revises: ef694464b50e
Create Date: 2026-01-23 14:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID, JSONB


# revision identifiers, used by Alembic.
revision = '5a1b2c3d4e5f'
down_revision = 'ef694464b50e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Créer la table lunar_interpretation_templates
    op.create_table(
        'lunar_interpretation_templates',
        sa.Column('id', UUID(as_uuid=True), primary_key=True),
        sa.Column('template_type', sa.String(50), nullable=False),
        sa.Column('moon_sign', sa.String(50), nullable=True),
        sa.Column('moon_house', sa.Integer, nullable=True),
        sa.Column('lunar_ascendant', sa.String(50), nullable=True),
        sa.Column('version', sa.Integer, nullable=False, server_default='2'),
        sa.Column('lang', sa.String(10), nullable=False, server_default='fr'),
        sa.Column('template_text', sa.Text, nullable=False),
        sa.Column('weekly_advice_template', JSONB, nullable=True),
        sa.Column('model_used', sa.String(50), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.func.now(), nullable=False),
    )

    # Créer les index
    op.create_index('idx_lunar_templates_unique', 'lunar_interpretation_templates',
                    ['template_type', 'moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'], unique=True)
    op.create_index('idx_lunar_templates_lookup', 'lunar_interpretation_templates',
                    ['template_type', 'moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'])
    op.create_index('idx_lunar_templates_type', 'lunar_interpretation_templates', ['template_type'])
    op.create_index('idx_lunar_templates_created_at', 'lunar_interpretation_templates', ['created_at'])

    # Migrer les données de pregenerated_lunar_interpretations vers lunar_interpretation_templates
    op.execute("""
        INSERT INTO lunar_interpretation_templates (
            id,
            template_type,
            moon_sign,
            moon_house,
            lunar_ascendant,
            version,
            lang,
            template_text,
            weekly_advice_template,
            model_used,
            created_at,
            updated_at
        )
        SELECT
            id,
            'full' AS template_type,
            moon_sign,
            moon_house,
            lunar_ascendant,
            version,
            lang,
            interpretation_full AS template_text,
            weekly_advice AS weekly_advice_template,
            model_used,
            created_at,
            updated_at
        FROM pregenerated_lunar_interpretations
    """)

    # Renommer l'ancienne table (backup)
    op.rename_table('pregenerated_lunar_interpretations', 'pregenerated_lunar_interpretations_backup')


def downgrade() -> None:
    # Restaurer l'ancienne table
    op.rename_table('pregenerated_lunar_interpretations_backup', 'pregenerated_lunar_interpretations')

    # Supprimer les index
    op.drop_index('idx_lunar_templates_created_at', 'lunar_interpretation_templates')
    op.drop_index('idx_lunar_templates_type', 'lunar_interpretation_templates')
    op.drop_index('idx_lunar_templates_lookup', 'lunar_interpretation_templates')
    op.drop_index('idx_lunar_templates_unique', 'lunar_interpretation_templates')

    # Supprimer la table
    op.drop_table('lunar_interpretation_templates')
