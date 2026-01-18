"""
Génère les interprétations natales pré-générées avec Claude Opus 4.5
Usage: python scripts/generate_natal_interpretations.py --mode validation|full --version 2
"""

import anthropic
import os
import sys
from pathlib import Path
from typing import Tuple, List, Optional
import time
import argparse
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

# Essayer d'importer tqdm (optionnel, utilisé seulement en mode full)
try:
    from tqdm import tqdm
    HAS_TQDM = True
except ImportError:
    HAS_TQDM = False
    print("⚠️  tqdm non installé, barre de progression désactivée pour le mode full")

# Ajouter le dossier parent au path pour imports relatifs
sys.path.insert(0, str(Path(__file__).parent.parent))

# Sujets célestes (15 sujets)
SUBJECTS = [
    ('sun', 'Soleil', '☀️'),
    ('moon', 'Lune', '🌙'),
    ('mercury', 'Mercure', '☿️'),
    ('venus', 'Vénus', '♀️'),
    ('mars', 'Mars', '♂️'),
    ('jupiter', 'Jupiter', '♃'),
    ('saturn', 'Saturne', '♄'),
    ('uranus', 'Uranus', '♅'),
    ('neptune', 'Neptune', '♆'),
    ('pluto', 'Pluton', '♇'),
    ('ascendant', 'Ascendant', '↑'),
    ('midheaven', 'Milieu du Ciel', '⬆️'),
    ('north_node', 'Nœud Nord', '☊'),
    ('south_node', 'Nœud Sud', '☋'),
    ('chiron', 'Chiron', '⚕️')
]

# Signes du zodiaque (12 signes)
SIGNS = [
    ('aries', 'Bélier'),
    ('taurus', 'Taureau'),
    ('gemini', 'Gémeaux'),
    ('cancer', 'Cancer'),
    ('leo', 'Lion'),
    ('virgo', 'Vierge'),
    ('libra', 'Balance'),
    ('scorpio', 'Scorpion'),
    ('sagittarius', 'Sagittaire'),
    ('capricorn', 'Capricorne'),
    ('aquarius', 'Verseau'),
    ('pisces', 'Poissons')
]

# Maisons astrologiques (1-12)
HOUSES = list(range(1, 13))

# Exemples de validation (Phase 1)
VALIDATION_EXAMPLES = [
    ('sun', 'aquarius', 11),       # Soleil en Verseau, Maison 11
    ('moon', 'taurus', 2),          # Lune en Taureau, Maison 2
    ('mercury', 'gemini', 3),       # Mercure en Gémeaux, Maison 3
    ('venus', 'libra', 7),          # Vénus en Balance, Maison 7
    ('mars', 'aries', 1),           # Mars en Bélier, Maison 1
    ('jupiter', 'sagittarius', 9),  # Jupiter en Sagittaire, Maison 9
    ('saturn', 'capricorn', 10),    # Saturne en Capricorne, Maison 10
    ('north_node', 'aquarius', 11), # Nœud Nord en Verseau, Maison 11
]


def get_house_label(house_num: int) -> Tuple[str, str]:
    """
    Retourne le label court et la description d'une maison

    Returns:
        tuple: (label_court, description_complete)
    """
    house_data = {
        1: ("identité, apparence", "Maison 1 : identité, apparence, nouveau départ, comment tu te présentes au monde"),
        2: ("ressources, valeurs", "Maison 2 : ressources personnelles, valeurs, sécurité matérielle, rapport à l'argent"),
        3: ("communication, environnement proche", "Maison 3 : communication, apprentissage, environnement proche, frères et sœurs"),
        4: ("foyer, racines", "Maison 4 : foyer, famille, racines, vie privée, bases émotionnelles"),
        5: ("créativité, plaisir", "Maison 5 : créativité, plaisir, expression personnelle, romance, enfants"),
        6: ("quotidien, service", "Maison 6 : quotidien, santé, service, travail, organisation, routines"),
        7: ("relations, partenariats", "Maison 7 : relations, partenariats, l'autre comme miroir, collaboration"),
        8: ("intimité, transformation", "Maison 8 : intimité, transformation, ressources partagées, liens profonds, pouvoir"),
        9: ("philosophie, expansion", "Maison 9 : philosophie, voyages, expansion de conscience, enseignement supérieur"),
        10: ("carrière, accomplissement", "Maison 10 : carrière, accomplissement social, réputation, visibilité publique"),
        11: ("projets collectifs, idéaux", "Maison 11 : projets collectifs, amitiés, idéaux, communauté, réseaux"),
        12: ("spiritualité, inconscient", "Maison 12 : spiritualité, inconscient, transcendance, solitude, ce qui est caché")
    }

    return house_data.get(house_num, ("domaine de vie", f"Maison {house_num}"))


def build_prompt_v2(subject_label: str, sign_label: str, house: int, emoji: str) -> str:
    """
    Construit le prompt pour Opus 4.5 selon template v2
    Adapté de build_interpretation_prompt_v2() du service
    """
    house_short_label, house_full = get_house_label(house)

    prompt = f"""Tu es un·e astrologue moderne pour l'app Lunation. Ton rôle : éclairer, pas prédire. Ton style : concret, chaleureux, jamais mystique.

DONNÉES DU THÈME:
- {subject_label} en {sign_label}
- {house_full}

TEMPLATE À SUIVRE (EXACT):

# {emoji} {subject_label} en {sign_label}
**En une phrase :** [UNE phrase très spécifique qui croise {subject_label} + {sign_label} + Maison {house}, pas de généralité]

## Ton moteur
[2-3 phrases max : ce que {subject_label} en {sign_label} en Maison {house} pousse à faire, rechercher, exprimer. Croiser SYSTÉMATIQUEMENT ces 3 dimensions. Concret, pas "tu es quelqu'un de..."]

## Ton défi
[1-2 phrases : le piège typique de {subject_label} en {sign_label} en Maison {house}. Équilibré lumière-ombre.]

## Maison {house} en {sign_label}
[1-2 phrases : comment {subject_label} exprime {sign_label} concrètement dans le domaine de la Maison {house} ({house_short_label}). Croiser les 3 infos.]

## Micro-rituel du jour (2 min)
- [Action relationnelle concrète pour {subject_label} en {sign_label} en Maison {house}, formulée à l'infinitif]
- [Action corps/respiration concrète]
- [Journal prompt : 1 question ouverte sur le croisement planète-signe-maison]

CONTRAINTES STRICTES:
1. LONGUEUR: 900 à 1200 caractères (max absolu 1400). Compte tes caractères.
2. INTERDIT: "tu es quelqu'un de...", "tu ressens profondément...", généralités vides.
3. INTERDIT: Prédictions ("tu vas rencontrer...", "il arrivera...").
4. INTERDIT: Conseils santé/diagnostic.
5. OBLIGATOIRE: CROISER SYSTÉMATIQUEMENT {subject_label} + {sign_label} + Maison {house} dans CHAQUE section. C'est le triptyque central de l'interprétation.
6. TON: Présent ou infinitif. Jamais futur. Vocabulaire simple, moderne.
7. FORMAT: Markdown strict. Les ## sont obligatoires. Pas de titre supplémentaire après le #.

GÉNÈRE L'INTERPRÉTATION MAINTENANT (français, markdown, 900-1200 chars):"""

    return prompt


def generate_interpretation(
    client: anthropic.Anthropic,
    subject: Tuple[str, str, str],
    sign: Tuple[str, str],
    house: int,
    version: int = 2
) -> Tuple[str, int]:
    """
    Appelle Opus 4.5 pour générer UNE interprétation complète

    Returns:
        tuple: (texte_markdown, longueur)
    """
    subject_key, subject_label, emoji = subject
    sign_key, sign_label = sign

    prompt = build_prompt_v2(subject_label, sign_label, house, emoji)

    try:
        print(f"  🤖 Appel Opus 4.5 pour {subject_label} en {sign_label} M{house}...", end="", flush=True)

        response = client.messages.create(
            model="claude-opus-4-5-20251101",
            max_tokens=2000,
            temperature=0.7,
            messages=[{"role": "user", "content": prompt}]
        )

        text = response.content[0].text.strip()
        length = len(text)

        # Valider longueur (900-1400 chars pour v2)
        if length < 900:
            print(f" ⚠️ Trop court ({length} chars), retry...", end="", flush=True)
            # Retry avec ajustement
            retry_prompt = f"{prompt}\n\nATTENTION: Ta réponse précédente faisait {length} chars. Développe davantage, vise 1000-1200 chars."
            response = client.messages.create(
                model="claude-opus-4-5-20251101",
                max_tokens=2000,
                temperature=0.7,
                messages=[{"role": "user", "content": retry_prompt}]
            )
            text = response.content[0].text.strip()
            length = len(text)

        elif length > 1400:
            print(f" ⚠️ Trop long ({length} chars), retry...", end="", flush=True)
            # Retry avec ajustement
            retry_prompt = f"{prompt}\n\nATTENTION: Ta réponse précédente faisait {length} chars. Réduis à 1000-1200 chars en retirant les répétitions."
            response = client.messages.create(
                model="claude-opus-4-5-20251101",
                max_tokens=2000,
                temperature=0.7,
                messages=[{"role": "user", "content": retry_prompt}]
            )
            text = response.content[0].text.strip()
            length = len(text)

        # Si toujours trop long, tronquer
        if length > 1400:
            text = text[:1397] + "..."
            length = 1400

        print(f" ✅ {length} chars")
        return text, length

    except Exception as e:
        print(f" ❌ ERREUR: {str(e)[:100]}")
        raise


def save_to_markdown(
    content: str,
    subject: Tuple[str, str, str],
    sign: Tuple[str, str],
    house: int,
    version: int = 2
) -> Path:
    """
    Sauvegarde dans data/natal_interpretations/v{version}/{subject}/{sign}_{house}.md

    Returns:
        Path: Chemin du fichier sauvegardé
    """
    subject_key, subject_label, emoji = subject
    sign_key, sign_label = sign

    # Créer dossier si nécessaire
    output_dir = Path(__file__).parent.parent / f"data/natal_interpretations/v{version}/{subject_key}"
    output_dir.mkdir(parents=True, exist_ok=True)

    # Fichier
    filename = f"{sign_key}_{house}.md"
    filepath = output_dir / filename

    # Frontmatter YAML
    frontmatter = f"""---
subject: {subject_key}
subject_label: {subject_label}
sign: {sign_label}
house: {house}
emoji: {emoji}
version: {version}
lang: fr
length: {len(content)}
---

"""

    # Écrire
    filepath.write_text(frontmatter + content, encoding='utf-8')
    print(f"  💾 Sauvegardé: {filepath.relative_to(Path.cwd())}")

    return filepath


def run_validation_mode(client: anthropic.Anthropic, version: int = 2):
    """
    Phase 1 : Génère 8 exemples de validation pour vérification qualité
    """
    print("=" * 80)
    print("🚀 PHASE 1 : GÉNÉRATION D'EXEMPLES DE VALIDATION")
    print("=" * 80)
    print(f"Mode: Validation ({len(VALIDATION_EXAMPLES)} exemples)")
    print(f"Version: v{version} (Moderne avec micro-rituel)")
    print(f"Modèle: Claude Opus 4.5 (claude-opus-4-5-20251101)")
    print("=" * 80)
    print()

    results = []
    total_cost = 0.0

    for i, (subject_key, sign_key, house) in enumerate(VALIDATION_EXAMPLES, 1):
        # Trouver les tuples complets
        subject_tuple = next((s for s in SUBJECTS if s[0] == subject_key), None)
        sign_tuple = next((s for s in SIGNS if s[0] == sign_key), None)

        if not subject_tuple or not sign_tuple:
            print(f"❌ Erreur: sujet/signe invalide: {subject_key}/{sign_key}")
            continue

        print(f"\n[{i}/{len(VALIDATION_EXAMPLES)}] {subject_tuple[1]} en {sign_tuple[1]} (Maison {house})")

        try:
            # Générer
            text, length = generate_interpretation(client, subject_tuple, sign_tuple, house, version)

            # Sauvegarder
            filepath = save_to_markdown(text, subject_tuple, sign_tuple, house, version)

            # Stats
            is_valid = 900 <= length <= 1400
            results.append({
                'subject': subject_tuple[1],
                'sign': sign_tuple[1],
                'house': house,
                'length': length,
                'valid': is_valid,
                'file': filepath
            })

            # Coût estimé (Opus 4.5: ~$0.015 par requête)
            total_cost += 0.015

            # Rate limiting (éviter throttling)
            time.sleep(0.5)

        except Exception as e:
            print(f"  ❌ ÉCHEC: {str(e)[:100]}")
            results.append({
                'subject': subject_tuple[1],
                'sign': sign_tuple[1],
                'house': house,
                'error': str(e)
            })

    # Résumé
    print("\n" + "=" * 80)
    print("📊 RÉSUMÉ DE LA GÉNÉRATION")
    print("=" * 80)

    successful = [r for r in results if 'length' in r]
    failed = [r for r in results if 'error' in r]

    if successful:
        lengths = [r['length'] for r in successful]
        avg_length = sum(lengths) / len(lengths)
        min_length = min(lengths)
        max_length = max(lengths)
        valid_count = sum(1 for r in successful if r['valid'])

        print(f"\n✅ Succès: {len(successful)}/{len(VALIDATION_EXAMPLES)}")
        print(f"   Longueur moyenne: {avg_length:.0f} chars")
        print(f"   Longueur min/max: {min_length}/{max_length} chars")
        print(f"   Dans les limites (900-1400): {valid_count}/{len(successful)}")
        print(f"\n💰 Coût estimé: ${total_cost:.2f} USD")

    if failed:
        print(f"\n❌ Échecs: {len(failed)}/{len(VALIDATION_EXAMPLES)}")
        for r in failed:
            print(f"   - {r['subject']} en {r['sign']} M{r['house']}: {r['error'][:80]}")

    print("\n" + "=" * 80)
    print("✅ PHASE 1 TERMINÉE")
    print("=" * 80)
    print("\nProchaines étapes:")
    print("1. Vérifier la qualité des exemples générés dans:")
    print(f"   {Path(__file__).parent.parent / f'data/natal_interpretations/v{version}'}")
    print("2. Valider le ton, le style, la longueur, les micro-rituels")
    print("3. Si validé, lancer la génération complète avec: --mode full")
    print()


def run_full_mode(client: anthropic.Anthropic, version: int = 2):
    """
    Phase 2 : Génère TOUTES les combinaisons (2160 interprétations)
    """
    total = len(SUBJECTS) * len(SIGNS) * len(HOUSES)

    print("=" * 80)
    print("🚀 PHASE 2 : GÉNÉRATION MASSIVE COMPLÈTE")
    print("=" * 80)
    print(f"Mode: Full (TOUTES les combinaisons)")
    print(f"Total: {total} interprétations (15 sujets × 12 signes × 12 maisons)")
    print(f"Version: v{version} (Moderne avec micro-rituel)")
    print(f"Modèle: Claude Opus 4.5 (claude-opus-4-5-20251101)")
    print(f"Coût estimé: ${total * 0.015:.2f} USD")
    print(f"Temps estimé: ~3-4 heures")
    print("=" * 80)

    # Demander confirmation
    response = input("\n⚠️  CONFIRMER la génération massive ? (y/N): ")
    if response.lower() != 'y':
        print("❌ Annulé par l'utilisateur")
        return

    print("\n🚀 Lancement de la génération...")

    count = 0
    errors = []
    lengths = []

    # Utiliser tqdm si disponible, sinon simple boucle
    if HAS_TQDM:
        iterator = tqdm(total=total, desc="Génération", unit="interp")
    else:
        iterator = None

    for subject in SUBJECTS:
        for sign in SIGNS:
            for house in HOUSES:
                try:
                    # Générer
                    text, length = generate_interpretation(client, subject, sign, house, version)

                    # Sauvegarder
                    save_to_markdown(text, subject, sign, house, version)

                    # Stats
                    count += 1
                    lengths.append(length)

                    if iterator:
                        iterator.update(1)

                    # Checkpoint tous les 50 fichiers
                    if count % 50 == 0:
                        avg = sum(lengths) / len(lengths) if lengths else 0
                        msg = f"\n📊 Checkpoint: {count}/{total} | Moyenne: {avg:.0f} chars"
                        if iterator:
                            iterator.write(msg)
                        else:
                            print(msg)

                    # Rate limiting
                    time.sleep(0.5)

                except Exception as e:
                    errors.append((subject, sign, house, str(e)))
                    if iterator:
                        iterator.update(1)

    if iterator:
        iterator.close()

    # Résumé final
    print("\n" + "=" * 80)
    print("📊 RÉSUMÉ FINAL")
    print("=" * 80)
    print(f"\n✅ Fichiers créés: {count}/{total}")

    if lengths:
        avg_length = sum(lengths) / len(lengths)
        min_length = min(lengths)
        max_length = max(lengths)
        valid_count = sum(1 for l in lengths if 900 <= l <= 1400)

        print(f"   Longueur moyenne: {avg_length:.0f} chars")
        print(f"   Longueur min/max: {min_length}/{max_length} chars")
        print(f"   Dans les limites (900-1400): {valid_count}/{len(lengths)}")
        print(f"\n💰 Coût total: ${count * 0.015:.2f} USD")

    if errors:
        print(f"\n❌ Erreurs: {len(errors)}")
        for subject, sign, house, error in errors[:10]:  # Max 10
            print(f"   - {subject[1]} en {sign[1]} M{house}: {error[:60]}")
        if len(errors) > 10:
            print(f"   ... et {len(errors) - 10} autres erreurs")

    print("\n" + "=" * 80)
    print("✅ PHASE 2 TERMINÉE")
    print("=" * 80)


def main():
    """Point d'entrée principal"""
    parser = argparse.ArgumentParser(
        description='Génère les interprétations natales pré-générées avec Claude Opus 4.5'
    )
    parser.add_argument(
        '--mode',
        choices=['validation', 'full'],
        default='validation',
        help='Mode de génération: validation (8 exemples) ou full (2160 interprétations)'
    )
    parser.add_argument(
        '--version',
        type=int,
        choices=[2],
        default=2,
        help='Version du prompt (2 = Moderne avec micro-rituel)'
    )

    args = parser.parse_args()

    # Vérifier la clé API
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ERREUR: ANTHROPIC_API_KEY non défini dans .env")
        print("\nDéfinir la variable d'environnement:")
        print("  export ANTHROPIC_API_KEY=sk-ant-...")
        print("\nOu ajouter dans .env:")
        print("  ANTHROPIC_API_KEY=sk-ant-...")
        sys.exit(1)

    # Créer client Anthropic
    client = anthropic.Anthropic(api_key=api_key)

    # Lancer le mode approprié
    if args.mode == 'validation':
        run_validation_mode(client, args.version)
    else:
        run_full_mode(client, args.version)


if __name__ == "__main__":
    main()
