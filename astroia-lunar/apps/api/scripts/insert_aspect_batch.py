#!/usr/bin/env python3
"""
Script d'insertion d'un batch d'interprétations en base de données

Usage:
    python insert_aspect_batch.py --batch-file data/batches/batch_01.json --version 5

Insère les interprétations dans la table pregenerated_natal_aspects.
Supporte l'upsert (met à jour si existe déjà).
"""

import os
import sys
import json
import argparse
import asyncio
from pathlib import Path
from datetime import datetime

# Ajouter le dossier parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from models.pregenerated_natal_aspect import PregeneratedNatalAspect
from config import DATABASE_URL


async def insert_batch(batch_file: str, version: int = 5):
    """Insère un batch en base de données."""

    # Charger le batch
    with open(batch_file, 'r', encoding='utf-8') as f:
        batch_data = json.load(f)

    batch_number = batch_data.get('batch_number', '?')
    aspects = batch_data.get('aspects', [])

    print(f"=== Insertion Batch {batch_number} ===\n")

    # Connexion DB
    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    inserted_count = 0
    updated_count = 0

    async with async_session() as session:
        async with session.begin():
            for aspect in aspects:
                planet1 = aspect['planet1']
                planet2 = aspect['planet2']
                aspect_type = aspect['aspect_type']

                # Normaliser en ordre alphabétique
                p1_norm = planet1.lower().strip()
                p2_norm = planet2.lower().strip()
                if p1_norm > p2_norm:
                    p1_norm, p2_norm = p2_norm, p1_norm

                # Sélectionner version A ou B
                selected = aspect.get('selected', 'a')
                version_key = f"version_{selected}"

                if version_key not in aspect:
                    print(f"⚠️  {p1_norm}-{p2_norm} {aspect_type}: Version {selected} introuvable, skip")
                    continue

                version_data = aspect[version_key]
                markdown = version_data.get('markdown', '')

                if not markdown:
                    print(f"⚠️  {p1_norm}-{p2_norm} {aspect_type}: Markdown vide, skip")
                    continue

                # Upsert (insert ou update)
                stmt = insert(PregeneratedNatalAspect).values(
                    planet1=p1_norm,
                    planet2=p2_norm,
                    aspect_type=aspect_type.lower(),
                    version=version,
                    lang='fr',
                    content=markdown,
                    length=len(markdown)
                )

                stmt = stmt.on_conflict_do_update(
                    index_elements=['planet1', 'planet2', 'aspect_type', 'version', 'lang'],
                    set_={
                        'content': stmt.excluded.content,
                        'length': stmt.excluded.length,
                        'created_at': datetime.now()
                    }
                )

                result = await session.execute(stmt)

                # Vérifier si c'était un insert ou update
                # Note: PostgreSQL n'a pas de façon simple de distinguer, on compte tout comme inserted
                inserted_count += 1

                print(f"  ✓ {p1_norm}-{p2_norm} {aspect_type} (version {selected})")

    await engine.dispose()

    print(f"\n✅ {inserted_count} aspects insérés/mis à jour (version={version}, lang=fr)")

    # Mettre à jour progress.json
    update_progress(batch_data, inserted_count)

    # Afficher statistiques
    print(f"💰 Coût cumulé : ${batch_data.get('cost_usd', 0):.2f} USD")

    # Vérifier total en BD
    await check_total_in_db(version)


def update_progress(batch_data: Dict, inserted_count: int):
    """Met à jour le fichier progress.json."""
    progress_file = Path("data/progress.json")

    if progress_file.exists():
        with open(progress_file, 'r') as f:
            progress = json.load(f)
    else:
        progress = {
            "total_aspects": 130,  # V1 optimisé
            "completed_batches": 0,
            "total_batches": 10,
            "aspects_inserted": 0,
            "progress_percent": 0,
            "total_cost_usd": 0,
            "last_batch_at": None,
            "batches": []
        }

    # Ajouter ce batch
    progress["completed_batches"] += 1
    progress["aspects_inserted"] += inserted_count
    progress["total_cost_usd"] += batch_data.get('cost_usd', 0)
    progress["progress_percent"] = round((progress["aspects_inserted"] / progress["total_aspects"]) * 100, 1)
    progress["last_batch_at"] = datetime.now().isoformat()

    progress["batches"].append({
        "number": batch_data.get('batch_number'),
        "aspects": inserted_count,
        "cost_usd": batch_data.get('cost_usd', 0),
        "committed_at": datetime.now().isoformat()
    })

    # Sauvegarder
    progress_file.parent.mkdir(parents=True, exist_ok=True)
    with open(progress_file, 'w') as f:
        json.dump(progress, f, indent=2)

    print(f"📊 Total v5 en BD : {progress['aspects_inserted']}/130 ({progress['progress_percent']}%)")


async def check_total_in_db(version: int):
    """Vérifie le nombre total d'aspects v5 en BD."""
    engine = create_async_engine(DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        result = await session.execute(
            select(PregeneratedNatalAspect).where(
                PregeneratedNatalAspect.version == version,
                PregeneratedNatalAspect.lang == 'fr'
            )
        )
        aspects = result.scalars().all()

    await engine.dispose()

    print(f"🔍 Vérification BD : {len(aspects)} aspects version={version} lang=fr")


def main():
    parser = argparse.ArgumentParser(description="Insérer un batch d'interprétations en BD")
    parser.add_argument('--batch-file', required=True, help="Fichier batch JSON à insérer")
    parser.add_argument('--version', type=int, default=5, help="Version des interprétations (défaut: 5)")

    args = parser.parse_args()

    asyncio.run(insert_batch(args.batch_file, args.version))


if __name__ == '__main__':
    main()
