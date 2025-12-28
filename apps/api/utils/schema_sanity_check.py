"""
Vérification de cohérence du schéma DB vs modèles SQLAlchemy

Détecte les mismatches de types critiques (UUID vs INTEGER) pour prévenir les bugs.
"""

import logging
from typing import Dict, List, Tuple, Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from uuid import uuid4

logger = logging.getLogger(__name__)

# Schéma attendu: (table, column, expected_type, expected_udt)
EXPECTED_SCHEMA = [
    ("natal_charts", "id", "uuid", "uuid"),
    ("natal_charts", "user_id", "integer", "int4"),
    ("lunar_returns", "id", "integer", "int4"),  # INTEGER, pas UUID
    ("lunar_returns", "user_id", "integer", "int4"),
    ("lunar_returns", "return_date", "timestamp with time zone", "timestamptz"),  # timestamptz pour return_date
]


async def check_schema_sanity(db: AsyncSession, correlation_id: Optional[str] = None) -> Tuple[bool, List[Dict[str, str]]]:
    """
    Vérifie que les types de colonnes critiques correspondent aux attentes.
    
    Returns:
        (is_valid, errors) où errors est une liste de dicts avec:
        - table_name
        - column_name
        - expected_type
        - actual_type
        - message
    """
    if correlation_id is None:
        correlation_id = str(uuid4())
    
    errors = []
    
    try:
        # Requête pour obtenir les types réels
        query = text("""
            SELECT 
                table_name,
                column_name,
                data_type,
                udt_name
            FROM information_schema.columns
            WHERE table_schema = 'public'
                AND table_name IN ('natal_charts', 'lunar_returns')
                AND column_name IN ('id', 'user_id', 'return_date')
            ORDER BY table_name, column_name
        """)
        
        result = await db.execute(query)
        rows = result.fetchall()
        
        # Créer un dict pour lookup rapide: (table, column) -> (data_type, udt_name)
        actual_schema = {
            (row.table_name, row.column_name): (row.data_type, row.udt_name)
            for row in rows
        }
        
        # Vérifier chaque colonne attendue
        for table, column, expected_dtype, expected_udt in EXPECTED_SCHEMA:
            key = (table, column)
            
            if key not in actual_schema:
                errors.append({
                    "table_name": table,
                    "column_name": column,
                    "expected_type": expected_dtype,
                    "actual_type": "NOT_FOUND",
                    "message": f"Colonne {table}.{column} introuvable en DB"
                })
                continue
            
            actual_dtype, actual_udt = actual_schema[key]
            
            # Comparer data_type (plus flexible) et udt_name (plus précis)
            # On accepte si l'un des deux correspond
            dtype_match = actual_dtype == expected_dtype
            udt_match = actual_udt == expected_udt
            
            if not dtype_match and not udt_match:
                errors.append({
                    "table_name": table,
                    "column_name": column,
                    "expected_type": f"{expected_dtype} (udt: {expected_udt})",
                    "actual_type": f"{actual_dtype} (udt: {actual_udt})",
                    "message": (
                        f"Type mismatch: {table}.{column} devrait être {expected_dtype}/{expected_udt}, "
                        f"mais est {actual_dtype}/{actual_udt}"
                    )
                })
        
        # Vérifier aussi les contraintes FK (optionnel mais utile)
        fk_query = text("""
            SELECT 
                tc.table_name,
                kcu.column_name,
                ccu.table_name AS foreign_table_name,
                ccu.column_name AS foreign_column_name
            FROM information_schema.table_constraints AS tc
            JOIN information_schema.key_column_usage AS kcu
                ON tc.constraint_name = kcu.constraint_name
                AND tc.table_schema = kcu.table_schema
            JOIN information_schema.constraint_column_usage AS ccu
                ON ccu.constraint_name = tc.constraint_name
                AND ccu.table_schema = tc.table_schema
            WHERE tc.constraint_type = 'FOREIGN KEY'
                AND tc.table_schema = 'public'
                AND tc.table_name IN ('natal_charts', 'lunar_returns')
                AND kcu.column_name = 'user_id'
        """)
        
        fk_result = await db.execute(fk_query)
        fk_rows = fk_result.fetchall()
        
        # Vérifier que user_id pointe bien vers users.id
        for row in fk_rows:
            if row.foreign_table_name != "users" or row.foreign_column_name != "id":
                errors.append({
                    "table_name": row.table_name,
                    "column_name": row.column_name,
                    "expected_type": "FK -> users.id",
                    "actual_type": f"FK -> {row.foreign_table_name}.{row.foreign_column_name}",
                    "message": (
                        f"FK incorrecte: {row.table_name}.{row.column_name} devrait pointer vers users.id, "
                        f"mais pointe vers {row.foreign_table_name}.{row.foreign_column_name}"
                    )
                })
        
        is_valid = len(errors) == 0
        
        if is_valid:
            logger.info(f"[corr={correlation_id}] ✅ Schema sanity check OK - tous les types sont corrects")
        else:
            error_msg = f"[corr={correlation_id}] ❌ Schema sanity check FAILED - {len(errors)} erreur(s)"
            for err in errors:
                error_msg += f"\n  - {err['message']}"
            logger.error(error_msg)
        
        return is_valid, errors
        
    except Exception as e:
        logger.error(
            f"[corr={correlation_id}] ❌ Erreur lors du schema sanity check: {e}",
            exc_info=True
        )
        errors.append({
            "table_name": "UNKNOWN",
            "column_name": "UNKNOWN",
            "expected_type": "N/A",
            "actual_type": "N/A",
            "message": f"Erreur lors de la vérification: {str(e)}"
        })
        return False, errors

