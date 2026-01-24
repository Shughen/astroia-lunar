#!/usr/bin/env python3
"""
Script Analyse Qualitative A/B Test - Opus vs Sonnet
Date: 2026-01-24
Version: 1.0

Usage:
    python scripts/ab_test_analyze.py --sample 20
    python scripts/ab_test_analyze.py --export report.md
"""

import asyncio
import sys
import os
import argparse
from datetime import datetime
from typing import List, Dict, Any
import json

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy import text
from database import get_db


async def get_paired_samples(sample_size: int) -> List[Dict[str, Any]]:
    """Récupérer paires Opus/Sonnet pour même lunar_return_id"""

    query = """
    WITH sample_returns AS (
        SELECT DISTINCT lunar_return_id
        FROM lunar_interpretations_ab_test
        GROUP BY lunar_return_id
        HAVING COUNT(DISTINCT model_tested) >= 2  -- Au moins 2 modèles testés
        ORDER BY RANDOM()
        LIMIT :sample_size
    )
    SELECT
        a.lunar_return_id,
        a.model_tested,
        a.output_text,
        a.duration_seconds,
        LENGTH(a.output_text) as length,
        a.created_at
    FROM lunar_interpretations_ab_test a
    JOIN sample_returns s ON a.lunar_return_id = s.lunar_return_id
    ORDER BY a.lunar_return_id, a.model_tested
    """

    async for db in get_db():
        result = await db.execute(text(query), {"sample_size": sample_size})
        rows = result.fetchall()

        # Regrouper par paires
        pairs = {}
        for row in rows:
            lr_id = row.lunar_return_id
            if lr_id not in pairs:
                pairs[lr_id] = {}

            pairs[lr_id][row.model_tested] = {
                "text": row.output_text,
                "duration": row.duration_seconds,
                "length": row.length,
                "created_at": row.created_at
            }

        return pairs


async def generate_comparison_report(pairs: Dict[int, Dict[str, Any]], output_file: str = None):
    """Générer rapport de comparaison qualitative"""

    if not pairs:
        print("❌ Aucune paire trouvée pour comparaison")
        return

    report_lines = []

    def add_line(text: str):
        report_lines.append(text)
        if not output_file:
            print(text)

    # Header
    add_line(f"# Rapport Comparaison Qualitative A/B Test")
    add_line(f"\n**Date** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    add_line(f"**Échantillon** : {len(pairs)} paires comparées\n")
    add_line(f"---\n")

    # Comparaison paire par paire
    for i, (lr_id, data) in enumerate(pairs.items(), 1):
        add_line(f"## Paire {i} - Lunar Return ID: {lr_id}\n")

        models_available = list(data.keys())

        if len(models_available) < 2:
            add_line("⚠️ Paire incomplète (un seul modèle testé)\n")
            continue

        # Tableau comparatif
        add_line("### Métriques\n")
        add_line("| Critère | " + " | ".join([m.upper() for m in models_available]) + " |")
        add_line("|---------|" + "|".join(["-------" for _ in models_available]) + "|")

        # Longueur
        lengths = [str(data[m]["length"]) + " chars" for m in models_available]
        add_line("| **Longueur** | " + " | ".join(lengths) + " |")

        # Durée
        durations = [f"{data[m]['duration']:.1f}s" for m in models_available]
        add_line("| **Durée** | " + " | ".join(durations) + " |")

        # Date
        dates = [data[m]['created_at'].strftime('%H:%M:%S') for m in models_available]
        add_line("| **Heure** | " + " | ".join(dates) + " |")

        add_line("")

        # Textes complets
        for model in models_available:
            text = data[model]["text"]
            add_line(f"### Texte {model.upper()}\n")
            add_line("```")
            add_line(text[:500] + "..." if len(text) > 500 else text)
            add_line("```\n")

        # Grille d'évaluation vide
        add_line("### Grille d'Évaluation\n")
        add_line("| Critère | " + " | ".join([m.upper() for m in models_available]) + " | Gagnant |")
        add_line("|---------|" + "|".join(["-------" for _ in models_available]) + "|---------|")
        add_line("| **Ton chaleureux** (1-5) | | | |")
        add_line("| **Cohérence astro** (1-5) | | | |")
        add_line("| **Conseils actionnables** (1-5) | | | |")
        add_line("| **Richesse vocabulaire** (1-5) | | | |")
        add_line("| **Structure claire** (1-5) | | | |")
        add_line("| **Inspiration** (1-5) | | | |")
        add_line("| **TOTAL** (/30) | | | |\n")

        add_line("---\n")

    # Résumé statistique
    add_line("## Résumé Statistique\n")

    # Calculer moyennes par modèle
    stats_by_model = {}

    for lr_id, data in pairs.items():
        for model, info in data.items():
            if model not in stats_by_model:
                stats_by_model[model] = {
                    "lengths": [],
                    "durations": []
                }

            stats_by_model[model]["lengths"].append(info["length"])
            stats_by_model[model]["durations"].append(info["duration"])

    add_line("| Modèle | Générations | Longueur moy. | Durée moy. |")
    add_line("|--------|-------------|---------------|------------|")

    for model, stats in stats_by_model.items():
        count = len(stats["lengths"])
        avg_length = sum(stats["lengths"]) / count if count > 0 else 0
        avg_duration = sum(stats["durations"]) / count if count > 0 else 0

        add_line(f"| **{model.upper()}** | {count} | {avg_length:.0f} chars | {avg_duration:.1f}s |")

    add_line("")

    # Sauvegarder si fichier spécifié
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n".join(report_lines))
        print(f"✅ Rapport sauvegardé : {output_file}")


async def calculate_cost_impact():
    """Calculer impact financier du switch Opus → Sonnet"""

    stats_sql = """
    SELECT
        model_tested,
        COUNT(*) as count,
        AVG(duration_seconds) as avg_duration
    FROM lunar_interpretations_ab_test
    GROUP BY model_tested
    """

    async for db in get_db():
        result = await db.execute(text(stats_sql))
        rows = result.fetchall()

        if not rows:
            print("❌ Aucune donnée trouvée")
            return

        stats = {row.model_tested: {"count": row.count, "avg_duration": row.avg_duration} for row in rows}

        print(f"\n{'='*80}")
        print(f"💰 Impact Financier - Switch Opus → Sonnet")
        print(f"{'='*80}\n")

        # Coûts unitaires (avec caching -90%)
        costs_cached = {
            "opus": 0.002,
            "sonnet": 0.0012,
            "haiku": 0.0002
        }

        # Projections mensuelles (1,000 users actifs)
        monthly_generations = 1000

        for model in ["opus", "sonnet", "haiku"]:
            if model in stats:
                count = stats[model]["count"]
                avg_duration = stats[model]["avg_duration"]
                cost_per_gen = costs_cached[model]
                monthly_cost = monthly_generations * cost_per_gen

                print(f"🤖 {model.upper()}")
                print(f"   Générations testées : {count}")
                print(f"   Durée moyenne       : {avg_duration:.1f}s")
                print(f"   Coût/génération     : ${cost_per_gen:.4f} (avec caching)")
                print(f"   Coût mensuel (1K users) : ${monthly_cost:.2f}")
                print()

        # Économie Sonnet vs Opus
        if "opus" in stats and "sonnet" in stats:
            opus_monthly = monthly_generations * costs_cached["opus"]
            sonnet_monthly = monthly_generations * costs_cached["sonnet"]
            saving_monthly = opus_monthly - sonnet_monthly
            saving_percent = (saving_monthly / opus_monthly) * 100

            print(f"💡 Économie Switch Opus → Sonnet")
            print(f"   Mensuel (1K users)  : ${saving_monthly:.2f} (-{saving_percent:.0f}%)")
            print(f"   Annuel (1K users)   : ${saving_monthly * 12:.2f}")
            print(f"   Annuel (5K users)   : ${saving_monthly * 12 * 5:.2f}")

        print(f"\n{'='*80}\n")
        break


async def export_raw_data(output_file: str):
    """Exporter données brutes pour analyse externe (CSV/JSON)"""

    query = """
    SELECT
        lunar_return_id,
        model_tested,
        LENGTH(output_text) as length,
        duration_seconds,
        created_at
    FROM lunar_interpretations_ab_test
    ORDER BY lunar_return_id, model_tested
    """

    async for db in get_db():
        result = await db.execute(text(query))
        rows = result.fetchall()

        if output_file.endswith(".json"):
            # Export JSON
            data = []
            for row in rows:
                data.append({
                    "lunar_return_id": row.lunar_return_id,
                    "model_tested": row.model_tested,
                    "length": row.length,
                    "duration_seconds": row.duration_seconds,
                    "created_at": row.created_at.isoformat()
                })

            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)

        elif output_file.endswith(".csv"):
            # Export CSV
            import csv
            with open(output_file, "w", encoding="utf-8", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["lunar_return_id", "model_tested", "length", "duration_seconds", "created_at"])

                for row in rows:
                    writer.writerow([
                        row.lunar_return_id,
                        row.model_tested,
                        row.length,
                        row.duration_seconds,
                        row.created_at.isoformat()
                    ])

        print(f"✅ Données exportées : {output_file}")
        break


def main():
    parser = argparse.ArgumentParser(
        description="Analyser résultats tests A/B Opus vs Sonnet"
    )
    parser.add_argument(
        "--sample",
        type=int,
        default=20,
        help="Nombre de paires à comparer (défaut: 20)"
    )
    parser.add_argument(
        "--export",
        type=str,
        help="Fichier de sortie pour rapport (ex: report.md)"
    )
    parser.add_argument(
        "--cost",
        action="store_true",
        help="Calculer impact financier uniquement"
    )
    parser.add_argument(
        "--raw",
        type=str,
        help="Exporter données brutes (CSV ou JSON)"
    )

    args = parser.parse_args()

    if args.cost:
        asyncio.run(calculate_cost_impact())
    elif args.raw:
        asyncio.run(export_raw_data(args.raw))
    else:
        async def run():
            pairs = await get_paired_samples(args.sample)
            await generate_comparison_report(pairs, args.export)

        asyncio.run(run())


if __name__ == "__main__":
    main()
