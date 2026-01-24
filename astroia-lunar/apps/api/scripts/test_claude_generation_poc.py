"""
POC minimal : Test génération Claude Opus 4.5 pour interprétations lunaires
Budget : 10 générations × $0.020 = $0.20
"""
import asyncio
import sys
from datetime import datetime
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from sqlalchemy import select
from models.lunar_return import LunarReturn
from services.lunar_interpretation_generator import generate_or_get_interpretation


async def test_poc_10_generations():
    """Test POC : 10 générations avec Claude Opus 4.5"""

    results = {
        'total': 0,
        'claude': 0,
        'db_temporal': 0,
        'db_template': 0,
        'hardcoded': 0,
        'errors': 0,
        'total_duration': 0.0,
        'generations': []
    }

    print("=" * 80)
    print("🚀 POC GÉNÉRATION LUNAIRE CLAUDE OPUS 4.5")
    print("=" * 80)
    print(f"📅 Date: {datetime.utcnow().isoformat()}")
    print(f"💰 Budget estimé: 10 générations × $0.020 = $0.20")
    print(f"🎯 Objectif: Valider génération temps réel + métriques\n")

    async with AsyncSessionLocal() as db:
        # Récupérer 10 LunarReturns de la DB
        result = await db.execute(
            select(LunarReturn)
            .order_by(LunarReturn.return_date.desc())
            .limit(10)
        )
        lunar_returns = result.scalars().all()

        if not lunar_returns:
            print("❌ Aucun LunarReturn trouvé dans la DB")
            return results

        print(f"✅ {len(lunar_returns)} LunarReturns trouvés\n")
        print("-" * 80)

        for i, lr in enumerate(lunar_returns, 1):
            try:
                print(f"\n[{i}/10] 🌙 LunarReturn ID: {lr.id} | User: {lr.user_id}")
                print(f"        📍 Moon: {lr.moon_sign} in House {lr.moon_house} | Asc: {lr.lunar_ascendant}")

                start = datetime.utcnow()

                # Force regenerate pour tester Claude API (bypass cache DB)
                output_text, weekly_advice, source, model = await generate_or_get_interpretation(
                    db=db,
                    lunar_return_id=lr.id,
                    user_id=lr.user_id,
                    subject='full',
                    version=2,
                    lang='fr',
                    force_regenerate=True  # ⚠️ Force appel Claude
                )

                duration = (datetime.utcnow() - start).total_seconds()

                # Stats
                results['total'] += 1
                results[source] = results.get(source, 0) + 1
                results['total_duration'] += duration

                # Store generation details
                results['generations'].append({
                    'id': lr.id,
                    'source': source,
                    'model': model,
                    'duration': duration,
                    'length': len(output_text),
                    'has_advice': bool(weekly_advice)
                })

                # Display result
                if source == 'claude':
                    print(f"        ✅ Source: {source} ({model})")
                else:
                    print(f"        ⚠️  Source: {source} (fallback, Claude failed)")

                print(f"        ⏱️  Duration: {duration:.2f}s")
                print(f"        📝 Length: {len(output_text)} chars")
                print(f"        💡 Weekly advice: {'✅' if weekly_advice else '❌'}")

            except Exception as e:
                results['errors'] += 1
                print(f"        ❌ Erreur: {type(e).__name__}: {str(e)[:100]}")

        # Final report
        print("\n" + "=" * 80)
        print("📊 RÉSULTATS POC")
        print("=" * 80)
        print(f"✅ Générations réussies: {results['total']}/10")
        print(f"   - Via Claude: {results.get('claude', 0)}")
        print(f"   - Via DB temporal (cache): {results.get('db_temporal', 0)}")
        print(f"   - Via DB template (fallback): {results.get('db_template', 0)}")
        print(f"   - Via hardcoded (fallback 2): {results.get('hardcoded', 0)}")
        print(f"❌ Erreurs: {results['errors']}")
        print(f"\n⏱️  Durée totale: {results['total_duration']:.2f}s")
        if results['total'] > 0:
            print(f"⏱️  Durée moyenne: {results['total_duration'] / results['total']:.2f}s/génération")

        # Coût estimé
        claude_count = results.get('claude', 0)
        estimated_cost = claude_count * 0.020
        print(f"\n💰 Coût estimé: ${estimated_cost:.3f} ({claude_count} appels Claude × $0.020)")

        # Success rate
        if results['total'] > 0:
            success_rate = (results.get('claude', 0) / results['total']) * 100
            print(f"📈 Taux succès Claude: {success_rate:.1f}%")

        print("\n" + "=" * 80)

    return results


if __name__ == "__main__":
    print("\n🎯 Lancement POC Génération Claude Opus 4.5...\n")

    try:
        results = asyncio.run(test_poc_10_generations())

        # Exit code basé sur les résultats
        if results['errors'] > 5:
            print("\n⚠️  Plus de 50% d'erreurs - POC échoué")
            sys.exit(1)
        elif results.get('claude', 0) == 0:
            print("\n⚠️  Aucune génération Claude réussie - vérifier ANTHROPIC_API_KEY")
            sys.exit(1)
        else:
            print("\n✅ POC terminé avec succès")
            sys.exit(0)

    except KeyboardInterrupt:
        print("\n\n⚠️  POC interrompu par l'utilisateur")
        sys.exit(130)
    except Exception as e:
        print(f"\n❌ Erreur fatale: {type(e).__name__}: {e}")
        sys.exit(1)
