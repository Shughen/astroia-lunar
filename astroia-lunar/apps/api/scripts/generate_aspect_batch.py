#!/usr/bin/env python3
"""
Script de génération d'interprétations d'aspects par batch avec Claude Opus 4.5

Usage:
    python generate_aspect_batch.py --batch-number 1 --pairs "sun,venus" "sun,mars" --ab-test

Génère les interprétations en format markdown v5 avec sections:
- Brief (résumé émotionnel)
- L'énergie de cet aspect (insight)
- Manifestations concrètes (3 bullets)
- Conseil pratique (action)
- Attention (ombre/piège)
"""

import os
import sys
import json
import argparse
import asyncio
from datetime import datetime
from typing import List, Dict, Tuple, Optional
from pathlib import Path

# Ajouter le dossier parent au path pour les imports
sys.path.insert(0, str(Path(__file__).parent.parent))

# Charger le .env
from dotenv import load_dotenv
load_dotenv()

import anthropic
from anthropic import Anthropic
from config import Settings

# Charger les settings
settings = Settings()

# === CONSTANTES ===

ASPECT_TYPES = ['conjunction', 'opposition', 'square', 'trine', 'sextile']

ASPECT_SYMBOLS = {
    'conjunction': '☌',
    'opposition': '☍',
    'square': '□',
    'trine': '△',
    'sextile': '⚹',
}

ASPECT_NAMES_FR = {
    'conjunction': 'Conjonction',
    'opposition': 'Opposition',
    'square': 'Carré',
    'trine': 'Trigone',
    'sextile': 'Sextile',
}

EXPECTED_ANGLES = {
    'conjunction': 0,
    'opposition': 180,
    'square': 90,
    'trine': 120,
    'sextile': 60,
}

PLANET_FUNCTIONS = {
    'sun': 'ton identité centrale, ta vitalité, ta volonté',
    'moon': 'tes besoins émotionnels, ta sécurité, tes réactions instinctives',
    'mercury': 'ton intellect, ta communication, ton analyse',
    'venus': 'tes désirs, tes valeurs, ton affectivité',
    'mars': 'ton action, tes pulsions, ton affirmation',
    'jupiter': 'ton expansion, ton optimisme, ta foi',
    'saturn': 'ta structure, tes limites, tes responsabilités',
    'uranus': 'tes ruptures, ton innovation, ton indépendance',
    'neptune': 'ton imaginaire, ta dissolution, ta transcendance',
    'pluto': 'ta transformation radicale, ton pouvoir',
}

PLANET_DISPLAY_NAMES = {
    'sun': 'Soleil',
    'moon': 'Lune',
    'mercury': 'Mercure',
    'venus': 'Vénus',
    'mars': 'Mars',
    'jupiter': 'Jupiter',
    'saturn': 'Saturne',
    'uranus': 'Uranus',
    'neptune': 'Neptune',
    'pluto': 'Pluton',
}

ASPECT_NATURE = {
    'conjunction': 'fusion, unification, intensité',
    'opposition': 'tension, polarité, complémentarité',
    'square': 'friction, challenge, action',
    'trine': 'fluidité, talent naturel, facilité',
    'sextile': 'opportunité, collaboration, soutien',
}

# === PROMPTS A/B ===

PROMPT_VERSION_A = """Tu es un astrologue bienveillant et accessible, expert en interprétation d'aspects astrologiques.

Génère une interprétation pour cet aspect :
- **Aspect** : {planet1} {aspect_type} {planet2}
- **Type** : {aspect_type_fr} ({expected_angle}°)
- **Nature** : {nature}

Contexte astrologique :
- {planet1} représente : {planet1_function}
- {planet2} représente : {planet2_function}

Génère en format markdown structuré :

# {symbol} {aspect_type_fr} {planet1_display} - {planet2_display}

**En une phrase :** [Accroche émotionnelle vivante, 10-15 mots, accessible à un débutant]

## L'énergie de cet aspect

[2-3 phrases expliquant l'interaction planétaire en langage simple, sans jargon. Utilise des métaphores de la vie quotidienne.]

## Manifestations concrètes

- [Manifestation 1 : Exemple dans la vie quotidienne avec détail sensoriel]
- [Manifestation 2 : Impact dans les relations avec exemple concret]
- [Manifestation 3 : Effet au travail/créativité avec situation réaliste]

## Conseil pratique

[Une action concrète et actionnable, 1-2 phrases max. Commence par un verbe d'action (Profite, Lance, Prends le temps de...)]

## Attention

[Le piège ou la limite à connaître, 1 phrase. Commence par "Attention à ne pas..." ou "Gare à..."]

---

**Contraintes strictes** :
- Ton : Bienveillant, accessible, inspirant (parle comme un ami qui connaît l'astro)
- Vocabulaire : Niveau collège, évite absolument : "indissociation", "contextualiser", "observer"
- Exemples : Concrets et sensoriels ("Ta créativité explose", pas "potentiel créatif activé")
- Longueur résumé : 50-80 caractères
- Longueur manifestations : 350-650 caractères total
- Longueur conseil : 100-200 caractères
- Longueur attention : 80-150 caractères
"""

PROMPT_VERSION_B = """Tu es un coach en développement personnel utilisant l'astrologie comme outil de connaissance de soi.

Génère une interprétation pour cet aspect qui aide la personne à AGIR :
- **Aspect** : {planet1} {aspect_type} {planet2}
- **Type** : {aspect_type_fr} ({expected_angle}°)
- **Nature** : {nature}

Contexte astrologique :
- {planet1} représente : {planet1_function}
- {planet2} représente : {planet2_function}

Génère en format markdown structuré :

# {symbol} {aspect_type_fr} {planet1_display} - {planet2_display}

**En une phrase :** [Accroche sous forme de mini-histoire ou question qui interpelle, 10-15 mots]

## L'énergie de cet aspect

[Raconte l'interaction planétaire comme une histoire. Utilise "tu" et le présent. Évoque des scènes concrètes.]

## Manifestations concrètes

- [Scène 1 : Raconte une situation précise où cet aspect se manifeste]
- [Scène 2 : Un autre contexte avec dialogue intérieur ou action]
- [Scène 3 : Impact sur un projet ou une relation avec résultat]

## Conseil pratique

[Un conseil ultra-concret avec verbe d'action. Donne un timing si pertinent ("Cette semaine, profite de..."). Propose une mini-action (5min max).]

## Attention

[Alerte bienveillante sur le piège. Utilise "Attention" ou "Gare à" + conséquence concrète.]

---

**Contraintes strictes** :
- Ton : Coach bienveillant qui raconte des histoires
- Vocabulaire : Conversationnel, tutoiement, présent de l'indicatif
- Exemples : Mini-scènes avec contexte précis ("Lundi matin au bureau, tu...", "En soirée entre amis, tu remarques que...")
- Longueur résumé : 50-80 caractères
- Longueur manifestations : 350-650 caractères total
- Longueur conseil : 100-200 caractères
- Longueur attention : 80-150 caractères
"""


# === FONCTIONS ===

def parse_aspect_interpretation(markdown: str) -> Dict:
    """Parse le markdown généré pour extraire les sections."""
    import re

    parsed = {
        'summary': '',
        'why': [],
        'manifestation': '',
        'advice': '',
        'shadow': ''
    }

    # Extraire "En une phrase"
    match = re.search(r'\*\*En une phrase\s*:\*\*\s*(.+?)(?:\n\n|\n##|$)', markdown, re.DOTALL)
    if match:
        parsed['summary'] = match.group(1).strip()

    # Extraire "L'énergie de cet aspect"
    match = re.search(r"##\s*L'[eé]nergie de cet aspect\s*\n(.+?)(?:\n##|$)", markdown, re.DOTALL)
    if match:
        energy = match.group(1).strip()
        # Séparer en bullets pour why
        sentences = energy.split('. ')
        parsed['why'] = [s.strip() + ('.' if not s.endswith('.') else '') for s in sentences[:2] if s.strip()]
        parsed['manifestation'] = energy  # Garder le texte complet aussi

    # Extraire "Manifestations concrètes"
    match = re.search(r"##\s*Manifestations concr[eè]tes\s*\n(.+?)(?:\n##|$)", markdown, re.DOTALL)
    if match:
        # Concaténer avec l'énergie
        manifestations = match.group(1).strip()
        if parsed['manifestation']:
            parsed['manifestation'] += "\n\n" + manifestations
        else:
            parsed['manifestation'] = manifestations

    # Extraire "Conseil pratique"
    match = re.search(r"##\s*Conseil pratique\s*\n(.+?)(?:\n##|$)", markdown, re.DOTALL)
    if match:
        parsed['advice'] = match.group(1).strip()

    # Extraire "Attention"
    match = re.search(r"##\s*Attention\s*\n(.+?)(?:\n##|$)", markdown, re.DOTALL)
    if match:
        parsed['shadow'] = match.group(1).strip()

    return parsed


async def generate_aspect_interpretation(
    client: Anthropic,
    planet1: str,
    planet2: str,
    aspect_type: str,
    prompt_template: str
) -> Tuple[str, int, int]:
    """
    Génère une interprétation d'aspect avec Claude Opus 4.5.

    Returns:
        (markdown_content, prompt_tokens, completion_tokens)
    """
    # Préparer les variables du prompt
    prompt = prompt_template.format(
        planet1=planet1,
        planet2=planet2,
        aspect_type=aspect_type,
        aspect_type_fr=ASPECT_NAMES_FR[aspect_type],
        expected_angle=EXPECTED_ANGLES[aspect_type],
        nature=ASPECT_NATURE[aspect_type],
        planet1_function=PLANET_FUNCTIONS[planet1],
        planet2_function=PLANET_FUNCTIONS[planet2],
        planet1_display=PLANET_DISPLAY_NAMES[planet1],
        planet2_display=PLANET_DISPLAY_NAMES[planet2],
        symbol=ASPECT_SYMBOLS[aspect_type]
    )

    # Appel Claude Opus 4.5
    response = client.messages.create(
        model="claude-opus-4-5-20251101",
        max_tokens=2000,
        temperature=0.7,
        messages=[{
            "role": "user",
            "content": prompt
        }]
    )

    markdown_content = response.content[0].text
    prompt_tokens = response.usage.input_tokens
    completion_tokens = response.usage.output_tokens

    return markdown_content, prompt_tokens, completion_tokens


async def generate_batch(
    batch_number: int,
    pairs: List[Tuple[str, str]],
    ab_test: bool,
    output_file: str
):
    """Génère un batch d'interprétations."""

    # Initialiser le client Anthropic
    api_key = os.getenv('ANTHROPIC_API_KEY')
    if not api_key:
        print("❌ ANTHROPIC_API_KEY non définie")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    batch_data = {
        "batch_number": batch_number,
        "generated_at": datetime.now().isoformat(),
        "pairs": [f"{p1}-{p2}" for p1, p2 in pairs],
        "aspects": [],
        "cost_usd": 0.0,
        "total_tokens": 0
    }

    total_aspects = len(pairs) * len(ASPECT_TYPES)
    current = 0

    for planet1, planet2 in pairs:
        for aspect_type in ASPECT_TYPES:
            current += 1
            print(f"\n[{current}/{total_aspects}] Génération {planet1}-{planet2} {aspect_type}...")

            aspect_entry = {
                "planet1": planet1,
                "planet2": planet2,
                "aspect_type": aspect_type,
            }

            # Génération version A
            print("  → Version A (insight)...")
            markdown_a, prompt_tokens_a, completion_tokens_a = await generate_aspect_interpretation(
                client, planet1, planet2, aspect_type, PROMPT_VERSION_A
            )

            parsed_a = parse_aspect_interpretation(markdown_a)

            aspect_entry["version_a"] = {
                "markdown": markdown_a,
                "parsed": parsed_a,
                "tokens": {
                    "prompt": prompt_tokens_a,
                    "completion": completion_tokens_a
                }
            }

            # Génération version B (seulement si A/B test activé)
            if ab_test:
                print("  → Version B (storytelling)...")
                await asyncio.sleep(2)  # Rate limiting

                markdown_b, prompt_tokens_b, completion_tokens_b = await generate_aspect_interpretation(
                    client, planet1, planet2, aspect_type, PROMPT_VERSION_B
                )

                parsed_b = parse_aspect_interpretation(markdown_b)

                aspect_entry["version_b"] = {
                    "markdown": markdown_b,
                    "parsed": parsed_b,
                    "tokens": {
                        "prompt": prompt_tokens_b,
                        "completion": completion_tokens_b
                    }
                }

                batch_data["total_tokens"] += prompt_tokens_a + completion_tokens_a + prompt_tokens_b + completion_tokens_b
            else:
                batch_data["total_tokens"] += prompt_tokens_a + completion_tokens_a
                # Sélection automatique version A
                aspect_entry["selected"] = "a"
                aspect_entry["selection_reason"] = "Version A uniquement (pas d'A/B test)"

            batch_data["aspects"].append(aspect_entry)

            # Pause pour rate limiting
            await asyncio.sleep(2)

    # Calculer coût estimé ($15 / 1M input tokens, $75 / 1M output tokens pour Opus 4.5)
    input_tokens = sum(
        a["version_a"]["tokens"]["prompt"] + (a.get("version_b", {}).get("tokens", {}).get("prompt", 0) or 0)
        for a in batch_data["aspects"]
    )
    output_tokens = sum(
        a["version_a"]["tokens"]["completion"] + (a.get("version_b", {}).get("tokens", {}).get("completion", 0) or 0)
        for a in batch_data["aspects"]
    )

    batch_data["cost_usd"] = (input_tokens / 1_000_000 * 15.0) + (output_tokens / 1_000_000 * 75.0)

    # Sauvegarder
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(batch_data, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Batch {batch_number} généré : {output_file}")
    print(f"   Aspects : {len(batch_data['aspects'])}")
    print(f"   Tokens : {batch_data['total_tokens']:,}")
    print(f"   Coût estimé : ${batch_data['cost_usd']:.2f}")


def main():
    parser = argparse.ArgumentParser(description="Générer un batch d'interprétations d'aspects")
    parser.add_argument('--batch-number', type=int, required=True, help="Numéro du batch")
    parser.add_argument('--pairs', nargs='+', required=True, help="Paires de planètes (ex: sun,venus sun,mars)")
    parser.add_argument('--ab-test', action='store_true', help="Générer versions A et B pour A/B test")
    parser.add_argument('--output', type=str, help="Fichier de sortie JSON (défaut: data/batches/batch_XX.json)")

    args = parser.parse_args()

    # Parser les paires
    pairs = []
    for pair_str in args.pairs:
        p1, p2 = pair_str.split(',')
        pairs.append((p1.strip(), p2.strip()))

    # Déterminer le fichier de sortie
    if args.output:
        output_file = args.output
    else:
        output_file = f"data/batches/batch_{args.batch_number:02d}.json"

    # Générer le batch
    asyncio.run(generate_batch(args.batch_number, pairs, args.ab_test, output_file))


if __name__ == '__main__':
    main()
