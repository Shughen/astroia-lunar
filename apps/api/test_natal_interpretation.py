#!/usr/bin/env python3
"""
Script de test pour vérifier l'intégration complète des interprétations natales
"""
import asyncio
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

async def test_anthropic_connection():
    """Test 1: Connexion à l'API Anthropic"""
    print("\n🔍 Test 1: Connexion à l'API Anthropic")
    print("-" * 50)

    try:
        from anthropic import Anthropic

        api_key = os.getenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("❌ ANTHROPIC_API_KEY non définie dans .env")
            return False

        print(f"✅ Clé API trouvée: {api_key[:20]}...{api_key[-4:]}")

        client = Anthropic(api_key=api_key)

        # Test simple
        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=50,
            messages=[
                {"role": "user", "content": "Réponds juste 'OK' si tu me reçois."}
            ]
        )

        response_text = message.content[0].text
        print(f"✅ Réponse de Claude: {response_text}")
        print(f"✅ Tokens utilisés: input={message.usage.input_tokens}, output={message.usage.output_tokens}")

        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False


async def test_natal_service():
    """Test 2: Service de génération d'interprétation"""
    print("\n🔍 Test 2: Service de génération d'interprétation")
    print("-" * 50)

    try:
        from services.natal_interpretation_service import generate_interpretation_with_claude
        from schemas.natal_interpretation import ChartPayload

        # Payload de test (Soleil en Bélier)
        test_payload = ChartPayload(
            subject_label="Soleil",
            sign="Bélier",
            degree=15.5,
            house=1,
            ascendant_sign="Bélier"
        )

        print(f"📝 Génération pour: {test_payload.subject_label} en {test_payload.sign}")
        print(f"   Maison: {test_payload.house}, Ascendant: {test_payload.ascendant_sign}")

        interpretation = await generate_interpretation_with_claude("sun", test_payload)

        print(f"\n✅ Interprétation générée ({len(interpretation)} caractères)")
        print("─" * 50)
        print(interpretation[:500] + "..." if len(interpretation) > 500 else interpretation)
        print("─" * 50)

        # Vérifications
        if len(interpretation) < 900:
            print(f"⚠️  Interprétation courte: {len(interpretation)} chars (min attendu: 900)")
        elif len(interpretation) > 1400:
            print(f"⚠️  Interprétation longue: {len(interpretation)} chars (max attendu: 1400)")
        else:
            print(f"✅ Longueur conforme: {len(interpretation)} chars (900-1400)")

        if "**☀️" in interpretation or "**Soleil" in interpretation:
            print("✅ Format markdown détecté")
        else:
            print("⚠️  Format markdown non détecté")

        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_database_connection():
    """Test 3: Connexion à la base de données"""
    print("\n🔍 Test 3: Connexion à la base de données")
    print("-" * 50)

    try:
        from database import AsyncSessionLocal
        from sqlalchemy import text

        async with AsyncSessionLocal() as session:
            # Test simple
            result = await session.execute(text("SELECT 1"))
            print("✅ Connexion à la base de données OK")

            # Vérifier si la table existe
            check_table = await session.execute(
                text("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'natal_interpretations')")
            )
            table_exists = check_table.scalar()

            if table_exists:
                print("✅ Table 'natal_interpretations' existe")

                # Compter les entrées
                count_result = await session.execute(text("SELECT COUNT(*) FROM natal_interpretations"))
                count = count_result.scalar()
                print(f"📊 Nombre d'interprétations en cache: {count}")
            else:
                print("❌ Table 'natal_interpretations' n'existe pas")
                print("   ⚠️  Exécutez la migration SQL dans Supabase Studio:")
                print("   📄 apps/api/migrations/create_natal_interpretations_table.sql")
                return False

        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Exécute tous les tests"""
    print("=" * 50)
    print("🧪 TESTS - Interprétations Natales Lunation")
    print("=" * 50)

    results = []

    # Test 1: Anthropic
    results.append(("Anthropic API", await test_anthropic_connection()))

    # Test 2: Service
    results.append(("Service Génération", await test_natal_service()))

    # Test 3: Database
    results.append(("Base de données", await test_database_connection()))

    # Résumé
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES TESTS")
    print("=" * 50)

    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")

    all_pass = all(result[1] for result in results)

    if all_pass:
        print("\n🎉 Tous les tests sont passés avec succès!")
        print("\n📱 Prochaines étapes:")
        print("1. Lancer l'API: uvicorn main:app --reload --host 0.0.0.0 --port 8000")
        print("2. Lancer l'app mobile: cd apps/mobile && npx expo start")
        print("3. Tester dans l'app: Thème Natal → Cliquer sur Soleil/Lune/etc.")
    else:
        print("\n⚠️  Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")

    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
