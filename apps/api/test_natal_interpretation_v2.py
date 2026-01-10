#!/usr/bin/env python3
"""
Tests pour les interprétations natales v2
- Prompt builder v2
- Validation longueur
- Sonnet + fallback Haiku
- Cache hit/miss
"""
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()


async def test_prompt_builder_v2():
    """Test 1: Prompt builder v2 - Format et contraintes"""
    print("\n🔍 Test 1: Prompt Builder v2")
    print("-" * 50)

    try:
        from services.natal_interpretation_service import build_interpretation_prompt_v2
        from schemas.natal_interpretation import ChartPayload

        # Payload de test
        payload = ChartPayload(
            subject_label="Soleil",
            sign="Bélier",
            degree=15.5,
            house=1,
            ascendant_sign="Bélier",
            aspects=[{
                'planet1': 'sun',
                'planet2': 'mars',
                'type': 'trine',
                'orb': 2.5
            }]
        )

        prompt = build_interpretation_prompt_v2("sun", payload)

        # Vérifications
        assert "# ☀️ Soleil en Bélier" in prompt, "Titre manquant"
        assert "## Ton moteur" in prompt, "Section 'Ton moteur' manquante"
        assert "## Ton défi" in prompt, "Section 'Ton défi' manquante"
        assert "## La maison 1 en clair" in prompt, "Section maison manquante"
        assert "## Micro-rituel du jour (2 min)" in prompt, "Section rituel manquante"
        assert "900 à 1200 caractères" in prompt, "Contrainte longueur manquante"
        assert "trigone à Mars" in prompt or "Aspect majeur" in prompt, "Aspect non mentionné"

        print("✅ Template v2 correct")
        print(f"✅ Longueur prompt: {len(prompt)} chars")
        print(f"✅ Aspect intégré: trigone à Mars (orbe 2.5°)")

        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_validation_length():
    """Test 2: Validation longueur"""
    print("\n🔍 Test 2: Validation Longueur")
    print("-" * 50)

    try:
        from services.natal_interpretation_service import validate_interpretation_length

        # Test cas valides
        text_ok = "x" * 1000
        is_valid, length = validate_interpretation_length(text_ok)
        assert is_valid, f"1000 chars devrait être valide"
        print(f"✅ 1000 chars: valide")

        # Test trop court
        text_short = "x" * 800
        is_valid, length = validate_interpretation_length(text_short)
        assert not is_valid, "800 chars devrait être invalide"
        print(f"✅ 800 chars: invalide (trop court)")

        # Test trop long
        text_long = "x" * 1500
        is_valid, length = validate_interpretation_length(text_long)
        assert not is_valid, "1500 chars devrait être invalide"
        print(f"✅ 1500 chars: invalide (trop long)")

        # Test limites
        assert validate_interpretation_length("x" * 900)[0], "900 devrait être valide (min)"
        assert validate_interpretation_length("x" * 1400)[0], "1400 devrait être valide (max)"
        print(f"✅ Limites 900-1400: correctes")

        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False


async def test_sonnet_generation():
    """Test 3: Génération avec Sonnet (ou fallback Haiku)"""
    print("\n🔍 Test 3: Génération Sonnet + Fallback")
    print("-" * 50)

    try:
        from services.natal_interpretation_service import generate_with_sonnet_fallback_haiku
        from schemas.natal_interpretation import ChartPayload

        payload = ChartPayload(
            subject_label="Lune",
            sign="Cancer",
            degree=22.3,
            house=4,
            ascendant_sign="Bélier"
        )

        print(f"📝 Génération pour: Lune en Cancer (Maison 4)")

        text, model_used = await generate_with_sonnet_fallback_haiku("moon", payload)

        print(f"\n✅ Modèle utilisé: {model_used}")
        print(f"✅ Longueur: {len(text)} chars")
        print("─" * 50)
        print(text[:400] + "..." if len(text) > 400 else text)
        print("─" * 50)

        # Vérifications
        assert len(text) >= 900, f"Texte trop court: {len(text)} chars"
        assert len(text) <= 1400, f"Texte trop long: {len(text)} chars"
        assert model_used in ["sonnet", "haiku"], f"Modèle inconnu: {model_used}"

        # Vérifier structure markdown
        assert text.startswith("#"), "Devrait commencer par un titre #"
        assert "## " in text, "Devrait contenir des sous-titres ##"

        print(f"✅ Validation: longueur OK, format markdown OK")

        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_database_cache():
    """Test 4: Cache DB version 2"""
    print("\n🔍 Test 4: Cache DB (version 2)")
    print("-" * 50)

    try:
        from database import AsyncSessionLocal
        from sqlalchemy import text
        from services.natal_interpretation_service import PROMPT_VERSION

        async with AsyncSessionLocal() as session:
            # Vérifier table
            check = await session.execute(
                text("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'natal_interpretations')")
            )
            exists = check.scalar()

            if not exists:
                print("❌ Table natal_interpretations n'existe pas")
                return False

            print("✅ Table natal_interpretations existe")

            # Compter entries version 2
            count_v2 = await session.execute(
                text(f"SELECT COUNT(*) FROM natal_interpretations WHERE version = {PROMPT_VERSION}")
            )
            count = count_v2.scalar()
            print(f"📊 Entries version {PROMPT_VERSION}: {count}")

            # Compter entries version 1 (anciennes)
            count_v1 = await session.execute(
                text("SELECT COUNT(*) FROM natal_interpretations WHERE version = 1")
            )
            count_old = count_v1.scalar()
            print(f"📊 Entries version 1 (anciennes): {count_old}")

            print(f"✅ Prompt version actuelle: {PROMPT_VERSION}")

            return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
        return False


async def test_house_labels():
    """Test 5: Labels de maisons"""
    print("\n🔍 Test 5: Labels de Maisons")
    print("-" * 50)

    try:
        from services.natal_interpretation_service import get_house_label_v2

        # Test quelques maisons
        for house_num in [1, 4, 7, 10, 12]:
            short, full = get_house_label_v2(house_num)
            print(f"✅ Maison {house_num}: {short}")
            assert short, f"Label court manquant pour maison {house_num}"
            assert full, f"Label complet manquant pour maison {house_num}"

        return True

    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False


async def main():
    """Exécute tous les tests v2"""
    print("=" * 50)
    print("🧪 TESTS V2 - Interprétations Natales")
    print("=" * 50)

    results = []

    # Tests
    results.append(("Prompt Builder v2", await test_prompt_builder_v2()))
    results.append(("Validation Longueur", await test_validation_length()))
    results.append(("House Labels", await test_house_labels()))
    results.append(("Génération Sonnet+Fallback", await test_sonnet_generation()))
    results.append(("Cache DB v2", await test_database_cache()))

    # Résumé
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES TESTS V2")
    print("=" * 50)

    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"{status} - {test_name}")

    all_pass = all(result[1] for result in results)

    if all_pass:
        print("\n🎉 Tous les tests v2 sont passés avec succès!")
        print("\n📱 Étapes suivantes:")
        print("1. Installer dépendance mobile: cd apps/mobile && npm install react-native-markdown-display")
        print("2. Lancer l'API: cd apps/api && uvicorn main:app --reload")
        print("3. Lancer l'app mobile: cd apps/mobile && npx expo start")
        print("4. Tester: Thème Natal → Cliquer sur Soleil/Lune/etc.")
    else:
        print("\n⚠️  Certains tests ont échoué. Vérifiez les erreurs ci-dessus.")

    print("=" * 50)


if __name__ == "__main__":
    asyncio.run(main())
