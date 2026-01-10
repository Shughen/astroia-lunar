"""
Modèle SQLAlchemy pour natal_interpretations
"""

from sqlalchemy import Column, String, Integer, Text, DateTime, Index, ForeignKey
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.sql import func
from database import Base
import uuid


class NatalInterpretation(Base):
    """
    Stocke les interprétations astrologiques générées par Claude
    Cache intelligent basé sur chart_id stable
    """
    __tablename__ = "natal_interpretations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    chart_id = Column(String, nullable=False, index=True)
    subject = Column(String, nullable=False)
    lang = Column(String, nullable=False, default='fr')
    version = Column(Integer, nullable=False, default=1)
    input_json = Column(JSONB, nullable=False)
    output_text = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

    __table_args__ = (
        Index(
            'idx_natal_interpretations_unique',
            'user_id', 'chart_id', 'subject', 'lang', 'version',
            unique=True
        ),
        Index('idx_natal_interpretations_user_chart', 'user_id', 'chart_id'),
        Index('idx_natal_interpretations_created_at', 'created_at'),
    )

    def __repr__(self):
        return f"<NatalInterpretation(id={self.id}, subject={self.subject}, chart_id={self.chart_id})>"
