"""
Modèle SQLAlchemy pour lunar_interpretations
Stocke les interprétations IA temporelles des révolutions lunaires
"""

from sqlalchemy import Column, String, Integer, Text, DateTime, Index, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base
import uuid


class LunarInterpretation(Base):
    """
    Interprétations IA temporelles des révolutions lunaires

    Différence critique vs pregenerated_lunar_interpretations:
    - Liée à un événement astronomique daté (lunar_return_id FK)
    - User-specific (user_id FK)
    - Régénérable (input_json stocké)
    - Versionnable (version + model_used)

    Architecture:
    - Layer 1: LunarReturn (faits astronomiques)
    - Layer 2: LunarInterpretation (narration IA) ← CE MODÈLE
    - Layer 3: LunarReport (cache application)
    - Layer 4: LunarInterpretationTemplate (fallback)

    Types de sujets:
    - 'full': Interprétation complète du mois
    - 'climate': Ambiance générale
    - 'focus': Zones de focus
    - 'approach': Approche du mois

    Clé d'idempotence: (lunar_return_id, subject, lang, version)
    """
    __tablename__ = "lunar_interpretations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    # Relations (ownership + lien temporel)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    lunar_return_id = Column(Integer, ForeignKey("lunar_returns.id", ondelete="CASCADE"), nullable=False, index=True)

    # Type d'interprétation
    subject = Column(String(50), nullable=False, index=True)  # 'full' | 'climate' | 'focus' | 'approach'

    # Versionning
    version = Column(Integer, nullable=False, default=2, index=True)
    lang = Column(String(10), nullable=False, default='fr', index=True)

    # Contenu IA
    input_json = Column(JSONB, nullable=False)   # Contexte complet envoyé à Claude (traçabilité)
    output_text = Column(Text, nullable=False)   # Interprétation générée
    weekly_advice = Column(JSONB, nullable=True) # Conseils hebdomadaires (si subject='full')

    # Métadonnées
    model_used = Column(String(50), nullable=True)  # 'claude-opus-4-5', 'claude-sonnet-4', etc.
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relations
    user = relationship("User", backref="lunar_interpretations")
    lunar_return = relationship("LunarReturn", backref="interpretations")

    __table_args__ = (
        # Contrainte unicité (idempotence)
        Index(
            'idx_lunar_interpretations_unique',
            'lunar_return_id', 'subject', 'lang', 'version',
            unique=True
        ),
        # Indexes pour performance
        Index('idx_lunar_interpretations_user', 'user_id'),
        Index('idx_lunar_interpretations_return', 'lunar_return_id'),
        Index('idx_lunar_interpretations_subject', 'subject'),
        Index('idx_lunar_interpretations_created_at', 'created_at'),
        # Index composite pour lookup rapide
        Index(
            'idx_lunar_interpretations_lookup',
            'lunar_return_id', 'subject', 'lang', 'version'
        ),
    )

    def __repr__(self):
        return (
            f"<LunarInterpretation("
            f"id={self.id}, lunar_return_id={self.lunar_return_id}, "
            f"subject={self.subject}, version={self.version}, lang={self.lang})>"
        )
