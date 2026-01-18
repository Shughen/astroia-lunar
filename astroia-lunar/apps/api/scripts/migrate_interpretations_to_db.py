"""
Script de migration des interprétations pré-générées depuis fichiers .md vers DB
Usage: python scripts/migrate_interpretations_to_db.py
"""

import sys
import asyncio
from pathlib import Path
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

# Ajouter le dossier parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation


def parse_markdown_file(file_path: Path) -> dict:
    """
    Parse un fichier markdown avec frontmatter YAML

    Returns:
        dict avec subject, sign, house, version, lang, content, length
    """
    content = file_path.read_text(encoding='utf-8')

    # Extraire frontmatter YAML
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            frontmatter_raw = parts[1].strip()
            markdown_text = parts[2].strip()

            # Parser le frontmatter (simple)
            metadata = {}
            for line in frontmatter_raw.split('\n'):
                if ':' in line:
                    key, value = line.split(':', 1)
                    metadata[key.strip()] = value.strip()

            return {
                'subject': metadata.get('subject', ''),
                'sign_label': metadata.get('sign', ''),
                'house': int(metadata.get('house', 0)),
                'version': int(metadata.get('version', 2)),
                'lang': metadata.get('lang', 'fr'),
                'content': markdown_text,
                'length': int(metadata.get('length', len(markdown_text)))
            }

    return None


# Mapping signe français → anglais (pour DB)
SIGN_FR_TO_EN = {
    'Bélier': 'aries',
    'Taureau': 'taurus',
    'Gémeaux': 'gemini',
    'Cancer': 'cancer',
    'Lion': 'leo',
    'Vierge': 'virgo',
    'Balance': 'libra',
    'Scorpion': 'scorpio',
    'Sagittaire': 'sagittarius',
    'Capricorne': 'capricorn',
    'Verseau': 'aquarius',
    'Poissons': 'pisces'
}


async def migrate_interpretations():
    """Migre toutes les interprétations des fichiers .md vers la DB"""
    print("=" * 80)
    print("MIGRATION INTERPRÉTATIONS PRÉ-GÉNÉRÉES : FICHIERS .MD → DB")
    print("=" * 80)
    print()

    # Trouver tous les fichiers .md
    base_path = Path(__file__).parent.parent
    interpretations_path = base_path / "data/natal_interpretations/v2"

    if not interpretations_path.exists():
        print(f"❌ Dossier introuvable: {interpretations_path}")
        return

    markdown_files = list(interpretations_path.glob("**/*.md"))
    print(f"📁 Fichiers trouvés: {len(markdown_files)}")
    print()

    # Parser tous les fichiers
    interpretations_data = []
    for file_path in markdown_files:
        data = parse_markdown_file(file_path)
        if data:
            # Convertir le signe FR → EN
            sign_en = SIGN_FR_TO_EN.get(data['sign_label'], data['sign_label'].lower())
            data['sign'] = sign_en
            interpretations_data.append(data)
            print(f"  ✅ Parsé: {data['subject']} en {data['sign_label']} M{data['house']} ({data['length']} chars)")
        else:
            print(f"  ⚠️ Échec parsing: {file_path}")

    print()
    print(f"📊 Total parsé: {len(interpretations_data)} interprétations")
    print()

    # Insérer en DB
    async with AsyncSessionLocal() as db:
        inserted_count = 0
        skipped_count = 0
        updated_count = 0

        for data in interpretations_data:
            try:
                # Vérifier si existe déjà
                result = await db.execute(
                    select(PregeneratedNatalInterpretation).where(
                        PregeneratedNatalInterpretation.subject == data['subject'],
                        PregeneratedNatalInterpretation.sign == data['sign'],
                        PregeneratedNatalInterpretation.house == data['house'],
                        PregeneratedNatalInterpretation.version == data['version'],
                        PregeneratedNatalInterpretation.lang == data['lang']
                    )
                )
                existing = result.scalar_one_or_none()

                if existing:
                    # Mettre à jour si le contenu a changé
                    if existing.content != data['content']:
                        existing.content = data['content']
                        existing.length = data['length']
                        updated_count += 1
                        print(f"  🔄 Mise à jour: {data['subject']} en {data['sign']} M{data['house']}")
                    else:
                        skipped_count += 1
                        print(f"  ⏭️  Déjà existant: {data['subject']} en {data['sign']} M{data['house']}")
                else:
                    # Insérer nouveau
                    interpretation = PregeneratedNatalInterpretation(
                        subject=data['subject'],
                        sign=data['sign'],
                        house=data['house'],
                        version=data['version'],
                        lang=data['lang'],
                        content=data['content'],
                        length=data['length']
                    )
                    db.add(interpretation)
                    inserted_count += 1
                    print(f"  ➕ Insertion: {data['subject']} en {data['sign']} M{data['house']}")

            except Exception as e:
                print(f"  ❌ Erreur: {data['subject']} en {data['sign']} M{data['house']}: {e}")

        # Commit toutes les modifications
        await db.commit()

    print()
    print("=" * 80)
    print("RÉSUMÉ")
    print("=" * 80)
    print(f"✅ Insérés: {inserted_count}")
    print(f"🔄 Mis à jour: {updated_count}")
    print(f"⏭️  Ignorés (déjà existants): {skipped_count}")
    print(f"📊 Total traité: {inserted_count + updated_count + skipped_count}")
    print()
    print("✅ Migration terminée !")


if __name__ == "__main__":
    asyncio.run(migrate_interpretations())
