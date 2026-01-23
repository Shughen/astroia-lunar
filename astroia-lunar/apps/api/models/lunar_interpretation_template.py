"""
Modèle SQLAlchemy pour lunar_interpretation_templates
Stocke les templates d'interprétations génériques (fallback statique)
"""

from sqlalchemy import Column, String, Integer, Text, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from database import Base
import uuid


class LunarInterpretationTemplate(Base):
    """
    Templates d'interprétations lunaires génériques (fallback)

    Utilisés comme fallback quand la génération IA échoue.
    Migrés depuis pregenerated_lunar_interpretations.

    Types de templates:
    - 'full': Interprétation complète (1728 combinaisons)
    - 'climate': Par signe lunaire seulement (12 combinaisons)
    - 'focus': Par maison lunaire seulement (12 combinaisons)
    - 'approach': Par ascendant lunaire seulement (12 combinaisons)

    Clé composite: (template_type, moon_sign, moon_house, lunar_ascendant, version, lang)
    """
    __tablename__ = "lunar_interpretation_templates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Type de template
    template_type = Column(String(50), nullable=False, index=True)  # 'full' | 'climate' | 'focus' | 'approach'

    # Clés de combinaison (nullable selon type)
    moon_sign = Column(String(50), nullable=True, index=True)        # NULL si template_type='focus'
    moon_house = Column(Integer, nullable=True, index=True)          # NULL si template_type='climate'
    lunar_ascendant = Column(String(50), nullable=True, index=True)  # NULL si template_type='focus'

    # Versionning
    version = Column(Integer, nullable=False, default=2, index=True)
    lang = Column(String(10), nullable=False, default='fr', index=True)

    # Contenu template
    template_text = Column(Text, nullable=False)
    weekly_advice_template = Column(JSONB, nullable=True)

    # Métadonnées
    model_used = Column(String(50), nullable=True)  # Model qui a généré le template initial
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        # Contrainte unicité
        Index(
            'idx_lunar_templates_unique',
            'template_type', 'moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang',
            unique=True
        ),
        # Index pour lookup rapide
        Index(
            'idx_lunar_templates_lookup',
            'template_type', 'moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'
        ),
        Index('idx_lunar_templates_type', 'template_type'),
        Index('idx_lunar_templates_created_at', 'created_at'),
    )

    def __repr__(self):
        return (
            f"<LunarInterpretationTemplate("
            f"type={self.template_type}, moon_sign={self.moon_sign}, "
            f"moon_house={self.moon_house}, lunar_ascendant={self.lunar_ascendant}, "
            f"version={self.version}, lang={self.lang})>"
        )
