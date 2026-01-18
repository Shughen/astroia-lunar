"""
Modèle SQLAlchemy pour pregenerated_natal_interpretations
Stocke les interprétations génériques pré-générées (templates réutilisables)
"""

from sqlalchemy import Column, String, Integer, Text, DateTime, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from database import Base
import uuid


class PregeneratedNatalInterpretation(Base):
    """
    Stocke les interprétations astrologiques pré-générées (templates génériques)

    Différence avec NatalInterpretation:
    - NatalInterpretation = cache par utilisateur (user_id + chart_id)
    - PregeneratedNatalInterpretation = templates génériques réutilisables

    Scope: 2160 lignes max (15 sujets × 12 signes × 12 maisons)
    """
    __tablename__ = "pregenerated_natal_interpretations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    subject = Column(String(50), nullable=False, index=True)        # sun, moon, mercury, etc.
    sign = Column(String(50), nullable=False, index=True)           # aries, taurus, gemini, etc. (EN)
    house = Column(Integer, nullable=False, index=True)             # 1-12
    version = Column(Integer, nullable=False, default=2, index=True)  # 2, 4, etc.
    lang = Column(String(10), nullable=False, default='fr', index=True)  # fr, en, es, etc.
    content = Column(Text, nullable=False)                          # Markdown complet
    length = Column(Integer, nullable=False)                        # Longueur du contenu (pour stats)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        # Contrainte unicité : 1 seule interprétation par (subject, sign, house, version, lang)
        Index(
            'idx_pregenerated_unique',
            'subject', 'sign', 'house', 'version', 'lang',
            unique=True
        ),
        # Index pour lookup rapide
        Index('idx_pregenerated_lookup', 'subject', 'sign', 'house', 'version', 'lang'),
        Index('idx_pregenerated_created_at', 'created_at'),
    )

    def __repr__(self):
        return f"<PregeneratedNatalInterpretation(subject={self.subject}, sign={self.sign}, house={self.house}, version={self.version}, lang={self.lang})>"
