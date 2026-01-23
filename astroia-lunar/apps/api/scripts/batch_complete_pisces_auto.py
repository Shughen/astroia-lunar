#!/usr/bin/env python3
"""
Batch script to AUTO-GENERATE complete Pisces lunar interpretations via Anthropic API.
Generates 144 interpretations (12 houses × 12 ascendants) in blocks of 24.
"""

import os
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

import asyncio
import uuid
from datetime import datetime
from database import AsyncSessionLocal
from models.pregenerated_lunar_interpretation import PregeneratedLunarInterpretation
from anthropic import Anthropic
from sqlalchemy.dialects.postgresql import insert
import time

# Configuration
MOON_SIGN = "Pisces"
ANTHROPIC_MODEL = "claude-opus-4.5-20251101"  # Opus 4.5 for max quality
CHAR_MIN = 800
CHAR_MAX = 1200

# Pisces traits for context
PISCES_CONTEXT = """Pisces (Poissons) : signe d'eau mutable
Traits clés :
- Intuitif et empathique, capte les émotions subtiles
- Rêveur et imaginatif, connecté au monde invisible
- Spirituel et mystique, cherche le sens profond
- Compassionnel et altruiste, veut aider et guérir
- Sensible aux énergies, peut absorber les émotions d'autrui
- Artistique et inspiré, s'exprime par la créativité
- Fluide et adaptable, suit le courant naturel
"""

# All houses and ascendants
HOUSES = list(range(1, 13))
ASCENDANTS = ["Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
              "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"]

# French ascendant names for prompts
ASCENDANT_FR = {
    "Aries": "Bélier", "Taurus": "Taureau", "Gemini": "Gémeaux",
    "Cancer": "Cancer", "Leo": "Lion", "Virgo": "Vierge",
    "Libra": "Balance", "Scorpio": "Scorpion", "Sagittarius": "Sagittaire",
    "Capricorn": "Capricorne", "Aquarius": "Verseau", "Pisces": "Poissons"
}


def generate_batch_interpretations(client: Anthropic, moon_sign: str, house: int, ascendants: list[str]) -> dict[str, str]:
    """
    Generate interpretations for one house across all ascendants.

    Args:
        client: Anthropic client
        moon_sign: Moon sign (e.g., "Pisces")
        house: House number (1-12)
        ascendants: List of ascendants to generate for

    Returns:
        Dictionary mapping ascendant -> interpretation text
    """
    asc_fr_list = ", ".join([ASCENDANT_FR[asc] for asc in ascendants])

    prompt = f"""Tu es un expert en astrologie lunaire francophone. Génère des interprétations personnalisées et chaleureuses pour la Lune en {moon_sign} (Poissons) en Maison {house} pour TOUS les ascendants suivants.

{PISCES_CONTEXT}

CONTEXTE DE LA MAISON {house} :
{get_house_context(house)}

Pour CHAQUE ascendant, écris une interprétation complète de 800-1200 caractères qui :
1. Explique comment la Lune en Poissons en Maison {house} influence la personne
2. Tient compte des spécificités de l'ascendant et de ses interactions avec Poissons
3. Décrit les émotions, besoins affectifs et dynamiques relationnelles
4. Utilise un ton chaleureux, personnel, inspirant (tutoiement)
5. Inclut TOUS les accents français appropriés (é, è, ê, à, ô, ç, etc.)
6. Structure : introduction engageante + domaine activé + approche instinctive + tensions possibles + conseil clé

Ascendants à traiter : {asc_fr_list}

FORMAT DE SORTIE EXACT :
Pour chaque ascendant, commence par "=== ASCENDANT: [NOM EN ANGLAIS] ===" suivi du texte, puis ligne vide.

Exemple :
=== ASCENDANT: Aries ===
Avec votre Lune en Poissons en Maison {house} et votre Ascendant Bélier, vous oscillez entre sensibilité émotionnelle et action impulsive...
[800-1200 caractères avec accents français]

=== ASCENDANT: Taurus ===
Votre Lune en Poissons en Maison {house} combinée à votre Ascendant Taureau crée une recherche de sécurité émotionnelle ancrée dans le concret...
[800-1200 caractères avec accents français]

IMPORTANT : Utilise les NOMS ANGLAIS dans les balises (Aries, Taurus, etc.) mais écris le texte en français avec tous les accents.

Génère maintenant les {len(ascendants)} interprétations complètes."""

    print(f"  Generating House {house} for {len(ascendants)} ascendants...")

    try:
        response = client.messages.create(
            model=ANTHROPIC_MODEL,
            max_tokens=16000,  # Large enough for 12 interpretations
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )

        full_text = response.content[0].text

        # Parse response to extract interpretations
        interpretations = {}
        current_ascendant = None
        current_text = []

        for line in full_text.split('\n'):
            if line.startswith('=== ASCENDANT:'):
                # Save previous interpretation if exists
                if current_ascendant and current_text:
                    interpretations[current_ascendant] = '\n'.join(current_text).strip()

                # Extract new ascendant name (English)
                parts = line.split('===')
                if len(parts) >= 2:
                    asc_part = parts[1].strip().replace('ASCENDANT:', '').strip()
                    current_ascendant = asc_part
                    current_text = []
            elif current_ascendant:
                current_text.append(line)

        # Save last interpretation
        if current_ascendant and current_text:
            interpretations[current_ascendant] = '\n'.join(current_text).strip()

        # Validate we got all ascendants
        missing = set(ascendants) - set(interpretations.keys())
        if missing:
            print(f"  WARNING: Missing interpretations for: {missing}")

        # Validate lengths
        for asc, text in interpretations.items():
            if len(text) < CHAR_MIN:
                print(f"  WARNING: {asc} too short ({len(text)} chars)")
            elif len(text) > CHAR_MAX:
                print(f"  WARNING: {asc} too long ({len(text)} chars)")

        return interpretations

    except Exception as e:
        print(f"  ERROR generating House {house}: {e}")
        return {}


def get_house_context(house: int) -> str:
    """Return thematic context for each house."""
    contexts = {
        1: "Identité, image personnelle, corps physique, manière de se présenter au monde",
        2: "Ressources matérielles, argent, valeurs personnelles, sécurité financière, estime de soi",
        3: "Communication, apprentissages, fratrie, environnement proche, mobilité, expression verbale",
        4: "Foyer, famille, racines, intimité, sécurité émotionnelle, vie privée, patrimoine familial",
        5: "Créativité, romance, plaisir, enfants, expression personnelle, jeu, prise de risque",
        6: "Travail quotidien, santé, routines, service, organisation, perfectionnement, hygiène de vie",
        7: "Partenariats, relations, mariage, contrats, collaboration, l'autre comme miroir",
        8: "Transformation, intimité profonde, sexualité, héritage, occultisme, crises régénératrices",
        9: "Philosophie, voyages lointains, éducation supérieure, spiritualité, expansion de conscience",
        10: "Carrière, réputation publique, accomplissement social, vocation, autorité, visibilité",
        11: "Amitié, réseaux, projets collectifs, idéaux, fraternité, innovations, causes sociales",
        12: "Inconscient, solitude, spiritualité profonde, retraite, épreuves cachées, dissolution de l'ego"
    }
    return contexts.get(house, "")


async def insert_interpretations(moon_sign: str, house_num: int, interpretations: dict[str, str]) -> int:
    """
    Insert interpretations into database.

    Returns:
        Number of interpretations inserted
    """
    count = 0

    async with AsyncSessionLocal() as session:
        for ascendant, text in interpretations.items():
            # Validate length
            char_count = len(text)
            if char_count < CHAR_MIN or char_count > CHAR_MAX:
                print(f"    WARNING: {ascendant} length {char_count} outside [{CHAR_MIN}, {CHAR_MAX}]")

            # Use upsert to handle existing records
            stmt = insert(PregeneratedLunarInterpretation).values(
                id=uuid.uuid4(),
                moon_sign=moon_sign,
                moon_house=house_num,
                lunar_ascendant=ascendant,
                version=1,
                lang='fr',
                interpretation_full=text,
                length=char_count,
                model_used=ANTHROPIC_MODEL
            )

            stmt = stmt.on_conflict_do_update(
                index_elements=['moon_sign', 'moon_house', 'lunar_ascendant', 'version', 'lang'],
                set_={
                    'interpretation_full': text,
                    'length': char_count,
                    'model_used': ANTHROPIC_MODEL,
                    'updated_at': datetime.now()
                }
            )

            await session.execute(stmt)
            count += 1
            print(f"    ✓ Inserted/Updated {ascendant} ({char_count} chars)")

        await session.commit()

    return count


async def main():
    """Main execution."""
    print("=" * 60)
    print(f"BATCH AUTO-GENERATION: {MOON_SIGN} Complete (144 interpretations)")
    print("=" * 60)

    # Check API key
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: ANTHROPIC_API_KEY not found in environment")
        print("Please set it in your .env file")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    # Check existing count
    async with AsyncSessionLocal() as session:
        from sqlalchemy import select, func
        result = await session.execute(
            select(func.count()).select_from(PregeneratedLunarInterpretation).where(
                PregeneratedLunarInterpretation.moon_sign == MOON_SIGN,
                PregeneratedLunarInterpretation.version == 1,
                PregeneratedLunarInterpretation.lang == 'fr'
            )
        )
        existing_count = result.scalar()

    print(f"\nExisting {MOON_SIGN} interpretations: {existing_count}/144")
    print(f"Model: {ANTHROPIC_MODEL}")
    print(f"Target length: {CHAR_MIN}-{CHAR_MAX} chars\n")

    # Confirm before proceeding (skip if --yes flag passed)
    if existing_count > 0 and '--yes' not in sys.argv:
        response = input(f"\nFound {existing_count} existing interpretations. Continue? (y/n): ")
        if response.lower() != 'y':
            print("Aborted.")
            sys.exit(0)
    elif existing_count > 0:
        print(f"\nFound {existing_count} existing interpretations. Skipping existing, generating missing...")

    total_inserted = 0
    total_cost_estimate = 0.0

    # Process in blocks of 2 houses (24 interpretations each)
    blocks = [
        (1, 2),   # Houses 1-2
        (3, 4),   # Houses 3-4
        (5, 6),   # Houses 5-6
        (7, 8),   # Houses 7-8
        (9, 10),  # Houses 9-10
        (11, 12)  # Houses 11-12
    ]

    for block_num, (start_house, end_house) in enumerate(blocks, 1):
        print(f"\n{'=' * 60}")
        print(f"BLOCK {block_num}/6: Houses {start_house}-{end_house} (24 interpretations)")
        print(f"{'=' * 60}\n")

        for house_num in range(start_house, end_house + 1):
            print(f"Processing House {house_num}...")

            # Generate for all 12 ascendants at once
            interpretations = generate_batch_interpretations(
                client, MOON_SIGN, house_num, ASCENDANTS
            )

            if interpretations:
                inserted = await insert_interpretations(MOON_SIGN, house_num, interpretations)
                total_inserted += inserted
                print(f"  ✓ Inserted {inserted}/{len(ASCENDANTS)} interpretations for House {house_num}")

                # Estimate cost (Opus 4.5: $15/M input, $75/M output)
                # Rough: ~3000 tokens input + ~12000 tokens output per house
                cost_per_house = (3000 * 0.000015) + (12000 * 0.000075)
                total_cost_estimate += cost_per_house

            # Rate limiting between houses
            time.sleep(2)

        # Longer pause between blocks
        if block_num < len(blocks):
            print(f"\n⏸️  Block {block_num} complete. Pausing 5 seconds before next block...")
            time.sleep(5)

    # Final summary
    print("\n" + "=" * 60)
    print("GENERATION COMPLETE")
    print("=" * 60)

    # Check final count
    async with AsyncSessionLocal() as session:
        from sqlalchemy import select, func
        result = await session.execute(
            select(func.count()).select_from(PregeneratedLunarInterpretation).where(
                PregeneratedLunarInterpretation.moon_sign == MOON_SIGN,
                PregeneratedLunarInterpretation.version == 1,
                PregeneratedLunarInterpretation.lang == 'fr'
            )
        )
        final_count = result.scalar()

    print(f"\nInserted: {total_inserted} new interpretations")
    print(f"Final count: {final_count}/144")
    print(f"Estimated cost: ${total_cost_estimate:.2f}")

    if final_count == 144:
        print(f"\n🎉 {MOON_SIGN} IS COMPLETE! 🎉")
    else:
        missing = 144 - final_count
        print(f"\n⚠️  Still missing {missing} interpretations")


if __name__ == "__main__":
    asyncio.run(main())
