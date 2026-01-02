#!/usr/bin/env python3
"""
Script pour inspecter le schéma réel de la base de données
Affiche toutes les colonnes des tables critiques avec leurs contraintes
"""
import os
import sys
import asyncio
import json
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# Charger DATABASE_URL depuis .env ou environnement
script_dir = os.path.dirname(os.path.abspath(__file__))
api_dir = os.path.dirname(script_dir)
env_path = os.path.join(api_dir, ".env")

if os.path.exists(env_path):
    from dotenv import load_dotenv
    load_dotenv(env_path)

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    print("❌ DATABASE_URL non définie", file=sys.stderr)
    sys.exit(1)

# Convertir postgresql:// en postgresql+asyncpg://
if DATABASE_URL.startswith("postgresql://"):
    ASYNC_DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://", 1)
else:
    ASYNC_DATABASE_URL = DATABASE_URL

async def inspect_table(session, table_name):
    """Inspecte une table et retourne ses colonnes"""
    query = text("""
        SELECT 
            column_name,
            data_type,
            udt_name,
            is_nullable,
            column_default,
            character_maximum_length,
            numeric_precision,
            numeric_scale
        FROM information_schema.columns
        WHERE table_schema = 'public' 
          AND table_name = :table_name
        ORDER BY ordinal_position;
    """)
    result = await session.execute(query, {"table_name": table_name})
    rows = result.fetchall()
    
    columns = []
    for row in rows:
        col_info = {
            "name": row.column_name,
            "type": row.data_type,
            "udt_name": row.udt_name,
            "nullable": row.is_nullable == "YES",
            "default": row.column_default,
        }
        if row.character_maximum_length:
            col_info["max_length"] = row.character_maximum_length
        if row.numeric_precision:
            col_info["precision"] = row.numeric_precision
        if row.numeric_scale:
            col_info["scale"] = row.numeric_scale
        columns.append(col_info)
    
    return columns

async def count_rows(session, table_name):
    """Compte les lignes d'une table"""
    query = text(f"SELECT COUNT(*) FROM public.{table_name}")
    result = await session.execute(query)
    return result.scalar()

async def inspect_schema():
    engine = create_async_engine(ASYNC_DATABASE_URL, echo=False)
    async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
    
    output = {
        "users": {"columns": [], "row_count": 0},
        "natal_charts": {"columns": [], "row_count": 0},
        "lunar_returns": {"columns": [], "row_count": 0},
    }
    
    async with async_session() as session:
        # Inspecter users
        print("=" * 80)
        print("📊 SCHÉMA users")
        print("=" * 80)
        users_cols = await inspect_table(session, "users")
        users_count = await count_rows(session, "users")
        output["users"]["columns"] = users_cols
        output["users"]["row_count"] = users_count
        
        for col in users_cols:
            default_str = col["default"] or "NULL"
            nullable_str = "NULL" if col["nullable"] else "NOT NULL"
            print(f"  {col['name']:30} {col['type']:25} {col['udt_name']:15} {nullable_str:10} default={default_str}")
        print(f"\n  📈 Row count: {users_count}")
        
        # Inspecter natal_charts
        print("\n" + "=" * 80)
        print("📊 SCHÉMA natal_charts")
        print("=" * 80)
        natal_cols = await inspect_table(session, "natal_charts")
        natal_count = await count_rows(session, "natal_charts")
        output["natal_charts"]["columns"] = natal_cols
        output["natal_charts"]["row_count"] = natal_count
        
        for col in natal_cols:
            default_str = col["default"] or "NULL"
            nullable_str = "NULL" if col["nullable"] else "NOT NULL"
            print(f"  {col['name']:30} {col['type']:25} {col['udt_name']:15} {nullable_str:10} default={default_str}")
        print(f"\n  📈 Row count: {natal_count}")
        
        # Inspecter lunar_returns
        print("\n" + "=" * 80)
        print("📊 SCHÉMA lunar_returns")
        print("=" * 80)
        lunar_cols = await inspect_table(session, "lunar_returns")
        lunar_count = await count_rows(session, "lunar_returns")
        output["lunar_returns"]["columns"] = lunar_cols
        output["lunar_returns"]["row_count"] = lunar_count
        
        for col in lunar_cols:
            default_str = col["default"] or "NULL"
            nullable_str = "NULL" if col["nullable"] else "NOT NULL"
            print(f"  {col['name']:30} {col['type']:25} {col['udt_name']:15} {nullable_str:10} default={default_str}")
        print(f"\n  📈 Row count: {lunar_count}")
        
        # Vérifications spécifiques
        print("\n" + "=" * 80)
        print("🔍 VÉRIFICATIONS SPÉCIFIQUES")
        print("=" * 80)
        
        # Colonnes birth_* dans users
        birth_cols = [col for col in users_cols if col["name"].startswith("birth_")]
        print(f"\n  Colonnes birth_* dans users: {len(birth_cols)}")
        for col in birth_cols:
            print(f"    - {col['name']}: {col['type']} ({'NULL' if col['nullable'] else 'NOT NULL'})")
        
        # positions dans natal_charts
        positions_col = next((col for col in natal_cols if col["name"] == "positions"), None)
        if positions_col:
            print(f"\n  ✅ positions existe dans natal_charts: {positions_col['type']} ({'NULL' if positions_col['nullable'] else 'NOT NULL'})")
        else:
            print(f"\n  ❌ positions N'EXISTE PAS dans natal_charts")
        
        # raw_data dans natal_charts
        raw_data_col = next((col for col in natal_cols if col["name"] == "raw_data"), None)
        if raw_data_col:
            print(f"  ✅ raw_data existe dans natal_charts: {raw_data_col['type']} ({'NULL' if raw_data_col['nullable'] else 'NOT NULL'})")
        else:
            print(f"  ❌ raw_data N'EXISTE PAS dans natal_charts")
    
    await engine.dispose()
    
    # Sauvegarder en JSON pour usage programmatique
    output_file = os.path.join(api_dir, ".schema_inspection.json")
    with open(output_file, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\n💾 Schéma sauvegardé dans: {output_file}")
    
    return output

if __name__ == "__main__":
    asyncio.run(inspect_schema())

