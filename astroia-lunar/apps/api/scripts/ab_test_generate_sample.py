#!/usr/bin/env python3
"""
Script Génération Échantillon A/B Test - Opus vs Sonnet
Date: 2026-01-24
Version: 1.0

Usage:
    python scripts/ab_test_generate_sample.py --model opus --count 100
    python scripts/ab_test_generate_sample.py --model sonnet --count 100
"""

import asyncio
import sys
import os
import argparse
import time
from datetime import datetime
from typing import Dict, Any
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database import get_db
from services.lunar_interpretation_generator import (
    generate_or_get_interpretation,
    CLAUDE_MODELS
)
from config import settings


async def create_ab_test_table():
    """Créer table temporaire pour stocker résultats A/B test"""

    create_table_sql = """
    CREATE TABLE IF NOT EXISTS lunar_interpretations_ab_test (
        id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
        user_id INTEGER NOT NULL,
        lunar_return_id INTEGER NOT NULL,
        model_tested VARCHAR(50) NOT NULL,  -- 'opus' | 'sonnet'
        output_text TEXT NOT NULL,
        weekly_advice JSONB,
        metadata JSONB,
        duration_seconds FLOAT,
        created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
    );

    CREATE INDEX IF NOT EXISTS idx_ab_test_model
    ON lunar_interpretations_ab_test(model_tested);

    CREATE INDEX IF NOT EXISTS idx_ab_test_lunar_return
    ON lunar_interpretations_ab_test(lunar_return_id);
    """

    async for db in get_db():
        await db.execute(text(create_table_sql))
        await db.commit()
        print("✅ Table lunar_interpretations_ab_test créée/vérifiée")
        break


async def get_sample_lunar_returns(count: int):
    """Récupérer échantillon de lunar_returns pour test"""

    query = """
    SELECT
        lr.id as lunar_return_id,
        lr.user_id,
        lr.moon_sign,
        lr.moon_house,
        lr.lunar_ascendant
    FROM lunar_returns lr
    WHERE lr.user_id IS NOT NULL
    ORDER BY RANDOM()
    LIMIT :count
    """

    async for db in get_db():
        result = await db.execute(text(query), {"count": count})
        rows = result.fetchall()
        print(f"✅ Récupéré {len(rows)} lunar_returns pour test")
        return rows


async def generate_with_model(
    lunar_return_id: int,
    user_id: int,
    model: str,
    force: bool = True
) -> Dict[str, Any]:
    """Générer interprétation avec modèle spécifique"""

    # Override temporairement le modèle configuré
    original_model = settings.LUNAR_CLAUDE_MODEL
    settings.LUNAR_CLAUDE_MODEL = model

    try:
        start_time = time.time()

        async for db in get_db():
            result = await generate_or_get_interpretation(
                db=db,
                lunar_return_id=lunar_return_id,
                user_id=user_id,
                subject="full",
                force_regenerate=force
            )

            duration = time.time() - start_time

            return {
                "output_text": result[0],
                "weekly_advice": result[1],
                "metadata": result[2],
                "source": result[3],
                "duration_seconds": duration
            }

    finally:
        # Restaurer modèle original
        settings.LUNAR_CLAUDE_MODEL = original_model


async def save_ab_test_result(
    user_id: int,
    lunar_return_id: int,
    model: str,
    result: Dict[str, Any]
):
    """Sauvegarder résultat dans table A/B test"""

    insert_sql = """
    INSERT INTO lunar_interpretations_ab_test
    (user_id, lunar_return_id, model_tested, output_text, weekly_advice, metadata, duration_seconds)
    VALUES (:user_id, :lunar_return_id, :model_tested, :output_text, :weekly_advice, :metadata, :duration_seconds)
    """

    async for db in get_db():
        await db.execute(text(insert_sql), {
            "user_id": user_id,
            "lunar_return_id": lunar_return_id,
            "model_tested": model,
            "output_text": result["output_text"],
            "weekly_advice": json.dumps(result["weekly_advice"]),
            "metadata": json.dumps(result["metadata"]),
            "duration_seconds": result["duration_seconds"]
        })
        await db.commit()
        break


async def run_ab_test(model: str, count: int, force: bool = True):
    """Exécuter test A/B pour un modèle donné"""

    print(f"\n{'='*60}")
    print(f"🧪 A/B Test - Modèle: {model.upper()}")
    print(f"   Générations: {count}")
    print(f"   Force regenerate: {force}")
    print(f"{'='*60}\n")

    # Créer table si nécessaire
    await create_ab_test_table()

    # Récupérer échantillon lunar_returns
    sample = await get_sample_lunar_returns(count)

    if not sample:
        print("❌ Aucun lunar_return trouvé pour test")
        return

    # Générer interprétations
    total_cost = 0.0
    total_duration = 0.0
    successful = 0
    failed = 0

    model_cost = {
        "opus": 0.020,
        "sonnet": 0.012,
        "haiku": 0.002
    }

    cost_per_gen = model_cost.get(model, 0.020)

    for i, row in enumerate(sample, 1):
        lunar_return_id = row.lunar_return_id
        user_id = row.user_id

        try:
            print(f"[{i}/{count}] Génération {model} (lunar_return_id={lunar_return_id})...", end=" ")

            result = await generate_with_model(
                lunar_return_id=lunar_return_id,
                user_id=user_id,
                model=model,
                force=force
            )

            # Sauvegarder résultat
            await save_ab_test_result(
                user_id=user_id,
                lunar_return_id=lunar_return_id,
                model=model,
                result=result
            )

            # Stats
            duration = result["duration_seconds"]
            source = result["source"]
            length = len(result["output_text"])

            if source == "claude":
                total_cost += cost_per_gen * 0.1  # -90% avec caching

            total_duration += duration
            successful += 1

            print(f"✅ {duration:.1f}s | {source} | {length} chars")

        except Exception as e:
            failed += 1
            print(f"❌ Erreur: {str(e)}")

    # Rapport final
    print(f"\n{'='*60}")
    print(f"📊 Résultats A/B Test - {model.upper()}")
    print(f"{'='*60}")
    print(f"Générations réussies : {successful}/{count} ({successful/count*100:.1f}%)")
    print(f"Générations échouées : {failed}/{count}")
    print(f"Durée moyenne        : {total_duration/successful:.1f}s" if successful > 0 else "N/A")
    print(f"Durée totale         : {total_duration:.1f}s ({total_duration/60:.1f} minutes)")
    print(f"Coût estimé          : ${total_cost:.3f} (avec Prompt Caching -90%)")
    print(f"Coût sans caching    : ${successful * cost_per_gen:.3f}")
    print(f"Économie caching     : ${successful * cost_per_gen - total_cost:.3f} ({(1 - total_cost/(successful * cost_per_gen))*100:.0f}%)")
    print(f"{'='*60}\n")


async def show_statistics():
    """Afficher statistiques comparatives des tests A/B"""

    stats_sql = """
    SELECT
        model_tested,
        COUNT(*) as total_generations,
        AVG(LENGTH(output_text)) as avg_length,
        MIN(LENGTH(output_text)) as min_length,
        MAX(LENGTH(output_text)) as max_length,
        AVG(duration_seconds) as avg_duration,
        MIN(duration_seconds) as min_duration,
        MAX(duration_seconds) as max_duration,
        CASE
            WHEN model_tested = 'opus' THEN COUNT(*) * 0.002
            WHEN model_tested = 'sonnet' THEN COUNT(*) * 0.0012
            WHEN model_tested = 'haiku' THEN COUNT(*) * 0.0002
        END as total_cost_cached
    FROM lunar_interpretations_ab_test
    GROUP BY model_tested
    ORDER BY model_tested
    """

    async for db in get_db():
        result = await db.execute(text(stats_sql))
        rows = result.fetchall()

        if not rows:
            print("❌ Aucune donnée A/B test trouvée")
            return

        print(f"\n{'='*80}")
        print(f"📊 Statistiques Comparatives A/B Test")
        print(f"{'='*80}")

        for row in rows:
            model = row.model_tested
            count = row.total_generations
            avg_length = row.avg_length
            min_length = row.min_length
            max_length = row.max_length
            avg_duration = row.avg_duration
            min_duration = row.min_duration
            max_duration = row.max_duration
            cost = row.total_cost_cached

            print(f"\n🤖 Modèle: {model.upper()}")
            print(f"   Générations      : {count}")
            print(f"   Longueur (chars) : {avg_length:.0f} (min={min_length}, max={max_length})")
            print(f"   Durée (secondes) : {avg_duration:.1f}s (min={min_duration:.1f}s, max={max_duration:.1f}s)")
            print(f"   Coût total       : ${cost:.3f} (avec caching)")

        print(f"\n{'='*80}\n")
        break


def main():
    parser = argparse.ArgumentParser(
        description="Générer échantillon pour tests A/B Opus vs Sonnet"
    )
    parser.add_argument(
        "--model",
        type=str,
        choices=["opus", "sonnet", "haiku"],
        required=True,
        help="Modèle Claude à tester"
    )
    parser.add_argument(
        "--count",
        type=int,
        default=100,
        help="Nombre de générations (défaut: 100)"
    )
    parser.add_argument(
        "--no-force",
        action="store_true",
        help="Ne pas forcer la régénération (utiliser cache si disponible)"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Afficher statistiques comparatives uniquement"
    )

    args = parser.parse_args()

    if args.stats:
        asyncio.run(show_statistics())
    else:
        force = not args.no_force
        asyncio.run(run_ab_test(args.model, args.count, force))


if __name__ == "__main__":
    main()
