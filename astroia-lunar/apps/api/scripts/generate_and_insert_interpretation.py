"""
Script pour générer et insérer une interprétation en DB
Usage: python scripts/generate_and_insert_interpretation.py --subject sun --sign aquarius --house 11

IMPORTANT: Ce script nécessite que vous génériez MANUELLEMENT le texte de l'interprétation
avec Claude Code (Opus 4.5) et le colliez dans le prompt interactif.

Workflow:
1. Vous lancez le script avec les paramètres (subject, sign, house)
2. Le script affiche le prompt à utiliser avec Claude Code
3. Vous générez l'interprétation avec Claude Code
4. Vous collez le texte généré dans le terminal
5. Le script insère en DB
"""

import sys
import asyncio
import argparse
from pathlib import Path

# Ajouter le dossier parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation


# Mapping des sujets
SUBJECTS = {
    'sun': ('Soleil', '☀️'),
    'moon': ('Lune', '🌙'),
    'mercury': ('Mercure', '☿️'),
    'venus': ('Vénus', '♀️'),
    'mars': ('Mars', '♂️'),
    'jupiter': ('Jupiter', '♃'),
    'saturn': ('Saturne', '♄'),
    'uranus': ('Uranus', '♅'),
    'neptune': ('Neptune', '♆'),
    'pluto': ('Pluton', '♇'),
    'ascendant': ('Ascendant', '↑'),
    'midheaven': ('Milieu du Ciel', '⬆️'),
    'north_node': ('Nœud Nord', '☊'),
    'south_node': ('Nœud Sud', '☋'),
    'chiron': ('Chiron', '⚕️')
}

# Mapping des signes (EN → FR)
SIGNS = {
    'aries': 'Bélier',
    'taurus': 'Taureau',
    'gemini': 'Gémeaux',
    'cancer': 'Cancer',
    'leo': 'Lion',
    'virgo': 'Vierge',
    'libra': 'Balance',
    'scorpio': 'Scorpion',
    'sagittarius': 'Sagittaire',
    'capricorn': 'Capricorne',
    'aquarius': 'Verseau',
    'pisces': 'Poissons'
}

# Labels maisons
HOUSES_LABELS = {
    1: "identité, apparence",
    2: "ressources, valeurs",
    3: "communication, environnement proche",
    4: "foyer, racines",
    5: "créativité, plaisir",
    6: "quotidien, service",
    7: "relations, partenariats",
    8: "intimité, transformation",
    9: "philosophie, expansion",
    10: "carrière, accomplissement",
    11: "projets collectifs, idéaux",
    12: "spiritualité, inconscient"
}


def build_prompt(subject_label: str, sign_label: str, house: int, emoji: str) -> str:
    """Construit le prompt pour Claude Code (Opus 4.5)"""
    house_label = HOUSES_LABELS.get(house, "domaine de vie")
    house_full = f"Maison {house} : {house_label}"

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
[1-2 phrases : comment {subject_label} exprime {sign_label} concrètement dans le domaine de la Maison {house} ({house_label}). Croiser les 3 infos.]

## Micro-rituel du jour (2 min)
- [Action relationnelle concrète pour {subject_label} en {sign_label} en Maison {house}, formulée à l'infinitif]
- [Action corps/respiration concrète]
- [Journal prompt : 1 question ouverte sur le croisement planète-signe-maison]

CONTRAINTES STRICTES:
1. LONGUEUR: 900 à 1200 caractères (max absolu 1400). Compte tes caractères.
2. INTERDIT: "tu es quelqu'un de...", "tu ressens profondément...", généralités vides.
3. INTERDIT: Prédictions ("tu vas rencontrer...", "il arrivera...").
4. INTERDIT: Conseils santé/diagnostic.
5. OBLIGATOIRE: CROISER SYSTÉMATIQUEMENT {subject_label} + {sign_label} + Maison {house} dans CHAQUE section.
6. TON: Présent ou infinitif. Jamais futur. Vocabulaire simple, moderne.
7. FORMAT: Markdown strict. Les ## sont obligatoires. Pas de titre supplémentaire après le #.

GÉNÈRE L'INTERPRÉTATION MAINTENANT (français, markdown, 900-1200 chars):

IMPORTANT: Retourne UNIQUEMENT le texte markdown de l'interprétation, sans frontmatter YAML, sans préambule, sans explication. Commence directement par "# {emoji} {subject_label} en {sign_label}"."""

    return prompt


async def insert_interpretation(subject: str, sign: str, house: int, content: str, version: int = 2, lang: str = 'fr'):
    """Insère une interprétation en DB"""
    async with AsyncSessionLocal() as db:
        # Vérifier si existe déjà
        from sqlalchemy import select
        result = await db.execute(
            select(PregeneratedNatalInterpretation).where(
                PregeneratedNatalInterpretation.subject == subject,
                PregeneratedNatalInterpretation.sign == sign,
                PregeneratedNatalInterpretation.house == house,
                PregeneratedNatalInterpretation.version == version,
                PregeneratedNatalInterpretation.lang == lang
            )
        )
        existing = result.scalar_one_or_none()

        if existing:
            print(f"\n⚠️  Interprétation déjà existante en DB")
            response = input("Voulez-vous la mettre à jour ? (y/N): ")
            if response.lower() != 'y':
                print("❌ Annulé")
                return

            existing.content = content
            existing.length = len(content)
            await db.commit()
            print(f"\n✅ Interprétation mise à jour : {subject} en {sign} M{house}")
        else:
            interpretation = PregeneratedNatalInterpretation(
                subject=subject,
                sign=sign,
                house=house,
                version=version,
                lang=lang,
                content=content,
                length=len(content)
            )
            db.add(interpretation)
            await db.commit()
            print(f"\n✅ Interprétation insérée : {subject} en {sign} M{house}")


def main():
    parser = argparse.ArgumentParser(
        description='Génère et insère une interprétation en DB'
    )
    parser.add_argument('--subject', required=True, choices=list(SUBJECTS.keys()),
                        help='Sujet (sun, moon, mercury, etc.)')
    parser.add_argument('--sign', required=True, choices=list(SIGNS.keys()),
                        help='Signe en anglais (aries, taurus, gemini, etc.)')
    parser.add_argument('--house', required=True, type=int, choices=range(1, 13),
                        help='Maison (1-12)')
    parser.add_argument('--version', type=int, default=2, choices=[2, 4],
                        help='Version du prompt (default: 2)')
    parser.add_argument('--lang', default='fr', help='Langue (default: fr)')

    args = parser.parse_args()

    subject_label, emoji = SUBJECTS[args.subject]
    sign_label = SIGNS[args.sign]

    print("=" * 80)
    print(f"GÉNÉRATION INTERPRÉTATION : {subject_label} en {sign_label} (Maison {args.house})")
    print("=" * 80)
    print()

    # Afficher le prompt
    prompt = build_prompt(subject_label, sign_label, args.house, emoji)
    print("📝 PROMPT POUR CLAUDE CODE (Opus 4.5):")
    print("-" * 80)
    print(prompt)
    print("-" * 80)
    print()

    print("🤖 Copiez ce prompt et utilisez-le avec Claude Code (Task tool, model='opus')")
    print()
    print("📋 Une fois l'interprétation générée, collez-la ci-dessous:")
    print("   (Terminez par une ligne vide, puis tapez 'END' sur une nouvelle ligne)")
    print()

    # Collecter l'input multi-lignes
    lines = []
    while True:
        try:
            line = input()
            if line.strip() == 'END':
                break
            lines.append(line)
        except EOFError:
            break

    content = '\n'.join(lines).strip()

    if not content:
        print("\n❌ Aucun contenu fourni, annulé")
        return

    # Valider la longueur
    length = len(content)
    if length < 900 or length > 1400:
        print(f"\n⚠️  Longueur hors limites: {length} chars (attendu 900-1400)")
        response = input("Continuer quand même ? (y/N): ")
        if response.lower() != 'y':
            print("❌ Annulé")
            return

    print(f"\n📊 Longueur: {length} chars ✅")
    print()

    # Insérer en DB
    try:
        asyncio.run(insert_interpretation(
            subject=args.subject,
            sign=args.sign,
            house=args.house,
            content=content,
            version=args.version,
            lang=args.lang
        ))
    except Exception as e:
        print(f"\n❌ Erreur insertion DB: {e}")
        return

    print()
    print("=" * 80)
    print("✅ TERMINÉ")
    print("=" * 80)


if __name__ == "__main__":
    main()
