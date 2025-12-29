#!/usr/bin/env python3
"""
Script pour supprimer et régénérer les révolutions lunaires d'un utilisateur
Usage: python scripts/regenerate_lunar_returns.py [user_id]
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:postgres@localhost:5432/astroia_lunar")
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def regenerate_lunar_returns(user_id: int = None):
    """
    Supprime et régénère les révolutions lunaires
    Si user_id est None, supprime pour tous les utilisateurs
    """
    session = Session()
    
    try:
        # Compter les révolutions existantes
        if user_id:
            count_query = text("SELECT COUNT(*) FROM lunar_returns WHERE user_id = :user_id")
            count = session.execute(count_query, {"user_id": user_id}).scalar()
            logger.info(f"📊 {count} révolutions lunaires trouvées pour user_id={user_id}")
            
            # Supprimer
            delete_query = text("DELETE FROM lunar_returns WHERE user_id = :user_id")
            session.execute(delete_query, {"user_id": user_id})
            logger.info(f"✅ Supprimé {count} révolutions lunaires pour user_id={user_id}")
        else:
            count_query = text("SELECT COUNT(*) FROM lunar_returns")
            count = session.execute(count_query).scalar()
            logger.info(f"📊 {count} révolutions lunaires trouvées (tous utilisateurs)")
            
            # Supprimer
            delete_query = text("DELETE FROM lunar_returns")
            session.execute(delete_query)
            logger.info(f"✅ Supprimé {count} révolutions lunaires (tous utilisateurs)")
        
        session.commit()
        logger.info("💾 Base de données mise à jour")
        logger.info("🔄 Régénérez maintenant via l'API ou l'app mobile pour voir les nouvelles dates variées")
        
    except Exception as e:
        session.rollback()
        logger.error(f"❌ Erreur: {e}")
        raise
    finally:
        session.close()

if __name__ == "__main__":
    user_id = None
    if len(sys.argv) > 1:
        try:
            user_id = int(sys.argv[1])
        except ValueError:
            logger.error(f"❌ user_id invalide: {sys.argv[1]}")
            sys.exit(1)
    
    if user_id:
        logger.info(f"🎯 Régénération pour user_id={user_id}")
    else:
        logger.info("🎯 Régénération pour tous les utilisateurs")
        response = input("⚠️  Êtes-vous sûr de vouloir supprimer TOUTES les révolutions lunaires ? (oui/non): ")
        if response.lower() != "oui":
            logger.info("❌ Annulé")
            sys.exit(0)
    
    regenerate_lunar_returns(user_id)

