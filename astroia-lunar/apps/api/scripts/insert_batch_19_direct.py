#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 19 en base de données (version=5)
Généré manuellement - Paires: mars-pluto (5 aspects) + jupiter-uranus (5 aspects)
Extension : aspects secondaires 5/8
"""

import sys
import asyncio
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.dialects.postgresql import insert
from models.pregenerated_natal_aspect import PregeneratedNatalAspect
from config import Settings

settings = Settings()

# Les 10 aspects du Batch 19
ASPECTS = [
    # === MARS-PLUTO (5 aspects) ===
    {
        "planet1": "mars",
        "planet2": "pluto",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Mars - Pluton

**En une phrase :** Ta rage devient volcan — ton pouvoir peut créer ou détruire

## L'énergie de cet aspect

Ton action (Mars) fusionne avec ta puissance brute (Pluton) ce mois-ci. Tu as une énergie colossale, presque effrayante. Chaque geste que tu poses a un impact disproportionné. Tu peux tout transformer ou tout anéantir.

## Manifestations concrètes

- **Force surhumaine** : Ton énergie dépasse ce que tu croyais possible
- **Transformation radicale** : Tu détruis ce qui doit mourir, tu reconstruis du neuf
- **Intensité dangereuse** : Ta colère peut devenir violence si tu ne la canalises pas

## Conseil pratique

Engage-toi dans une transformation majeure — carrière, relation, vie entière — tu as le pouvoir de tout changer.

## Attention

Gare à la destruction — Mars-Pluton peut raser ce qui ne mérite pas de mourir."""
    },
    {
        "planet1": "mars",
        "planet2": "pluto",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Mars - Pluton

**En une phrase :** Tu luttes pour le pouvoir — chaque action devient guerre totale

## L'énergie de cet aspect

Ton besoin d'agir (Mars) s'oppose à ton besoin de contrôler (Pluton) ce mois-ci. Chaque situation devient un combat de pouvoir. Tu ne peux rien faire à moitié, c'est tout ou rien. Cette tension crée des conflits violents, parfois destructeurs.

## Manifestations concrètes

- **Guerres de pouvoir** : Chaque relation devient un rapport de force
- **Colère explosive** : Ta rage s'accumule puis explose sans prévenir
- **Attirance pour le danger** : Tu cherches les situations extrêmes

## Conseil pratique

Identifie où tu luttes pour le contrôle — puis demande-toi si cette guerre en vaut la peine.

## Attention

Attention à la violence — Mars-Pluton peut détruire irrémédiablement."""
    },
    {
        "planet1": "mars",
        "planet2": "pluto",
        "aspect_type": "square",
        "content": """# □ Carré Mars - Pluton

**En une phrase :** Ta rage te consume — tu détruis tout, toi y compris

## L'énergie de cet aspect

Ton action (Mars) entre en guerre avec ton ombre (Pluton) ce mois-ci. Tu te bats contre toi-même. Ta colère se retourne contre toi ou explose sur les autres. Cette guerre intérieure crée de l'autodestruction, de la violence.

## Manifestations concrètes

- **Auto-sabotage violent** : Tu détruis ce que tu construis
- **Colère incontrôlable** : Tu passes de 0 à 100 sans transition
- **Comportements extrêmes** : Tu prends des risques stupides, tu provoques le danger

## Conseil pratique

Trouve un exutoire physique intense — boxe, sport extrême, travail physique — évacue avant d'exploser.

## Attention

Gare aux gestes irréversibles — Mars-Pluton peut créer des dégâts permanents."""
    },
    {
        "planet1": "mars",
        "planet2": "pluto",
        "aspect_type": "trine",
        "content": """# △ Trigone Mars - Pluton

**En une phrase :** Ta puissance devient naturelle — tu agis avec une force tranquille

## L'énergie de cet aspect

Ton action (Mars) et ta profondeur (Pluton) s'harmonisent ce mois-ci. Tu as un pouvoir immense mais tu le maîtrises. Tes gestes transforment profondément. Tu ne forces rien, tu changes tout.

## Manifestations concrètes

- **Pouvoir magnétique** : Les gens sentent ta force sans que tu aies à la montrer
- **Transformation naturelle** : Tu changes les choses sans violence
- **Endurance incroyable** : Tu tiens dans des situations qui briseraient les autres

## Conseil pratique

Utilise ton pouvoir pour transformer en profondeur — guérison, leadership, création radicale.

## Attention

Attention à l'abus de pouvoir — même harmonieux, Pluton peut corrompre."""
    },
    {
        "planet1": "mars",
        "planet2": "pluto",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Mars - Pluton

**En une phrase :** Tu découvres ta force — chaque action révèle ton pouvoir réel

## L'énergie de cet aspect

Ton action (Mars) et ta capacité de transformation (Pluton) se complètent ce mois-ci. Tu oses aller plus loin. Tes gestes ont plus d'impact. Tu découvres une puissance que tu ne te connaissais pas.

## Manifestations concrètes

- **Audace mesurée** : Tu repousses tes limites sans te détruire
- **Actions profondes** : Ce que tu fais change vraiment les choses
- **Résilience accrue** : Tu encaisses mieux, tu tiens plus longtemps

## Conseil pratique

Engage-toi dans un projet qui te fait peur — teste ta vraie puissance.

## Attention

Gare à l'ivresse du pouvoir — la force peut devenir addiction."""
    },

    # === JUPITER-URANUS (5 aspects) ===
    {
        "planet1": "jupiter",
        "planet2": "uranus",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Jupiter - Uranus

**En une phrase :** Tu veux tout casser pour tout réinventer — ta vision devient révolution

## L'énergie de cet aspect

Ton optimisme (Jupiter) fusionne avec ton besoin de rupture (Uranus) ce mois-ci. Tu ne supportes plus l'ancien monde. Tu veux créer quelque chose de radicalement nouveau. Tes idées sont audacieuses, parfois utopiques.

## Manifestations concrètes

- **Vision révolutionnaire** : Tu vois un futur meilleur et tu veux y aller maintenant
- **Audace maximale** : Tu oses des choses que personne n'ose
- **Changements radicaux** : Tu casses tout pour reconstruire mieux

## Conseil pratique

Lance un projet disruptif — startup, mouvement, art avant-gardiste — tu as la foi et l'audace.

## Attention

Gare à l'utopie destructrice — parfois il faut améliorer l'existant, pas tout raser."""
    },
    {
        "planet1": "jupiter",
        "planet2": "uranus",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Jupiter - Uranus

**En une phrase :** Tu veux la liberté mais sans limite — impossible de tenir

## L'énergie de cet aspect

Ton désir d'expansion (Jupiter) s'oppose à ton besoin de rupture (Uranus) ce mois-ci. Tu veux tout avoir, tout changer, tout vivre en même temps. Cette tension crée de l'instabilité, de la dispersion, parfois du chaos.

## Manifestations concrètes

- **Instabilité chronique** : Tu changes de cap sans cesse, personne ne te suit
- **Opportunités ratées** : Tu vois trop de possibilités, tu n'en saisis aucune
- **Rébellion excessive** : Tu rejettes tout, même ce qui pourrait t'aider

## Conseil pratique

Choisis une direction et tiens-la 3 mois — prouve que tu peux tenir un cap sans t'ennuyer.

## Attention

Attention à la dispersion — Jupiter-Uranus peut te faire courir partout sans arriver nulle part."""
    },
    {
        "planet1": "jupiter",
        "planet2": "uranus",
        "aspect_type": "square",
        "content": """# □ Carré Jupiter - Uranus

**En une phrase :** Tu promets la révolution puis tu changes d'avis — personne ne te croit

## L'énergie de cet aspect

Ton optimisme (Jupiter) entre en conflit avec ton besoin d'indépendance (Uranus) ce mois-ci. Tu t'engages dans des projets fous puis tu les abandonnes. Tu prêches la liberté mais tu fuis les responsabilités. Cette friction crée de l'incohérence.

## Manifestations concrètes

- **Promesses non tenues** : Tu t'engages trop vite, tu te dégages trop vite
- **Rébellion stérile** : Tu te bats contre tout sans construire rien
- **Excès d'optimisme** : Tu crois que tout est possible sans effort

## Conseil pratique

Termine un projet avant d'en commencer un nouveau — prouve que tu peux aller au bout.

## Attention

Gare à la crédibilité — personne ne te suivra si tu changes toujours d'avis."""
    },
    {
        "planet1": "jupiter",
        "planet2": "uranus",
        "aspect_type": "trine",
        "content": """# △ Trigone Jupiter - Uranus

**En une phrase :** Ton audace devient génie — tu innoves avec foi

## L'énergie de cet aspect

Ton optimisme (Jupiter) et ton originalité (Uranus) collaborent ce mois-ci. Tu vois des possibilités que personne ne voit. Tu oses croire en l'impossible. Tes projets sont innovants ET réalisables.

## Manifestations concrètes

- **Innovation inspirée** : Tu crées du neuf avec confiance
- **Opportunités inattendues** : Les bonnes surprises arrivent de partout
- **Liberté expansive** : Tu grandis sans te limiter

## Conseil pratique

Lance un projet qui mélange innovation et vision — tu as la créativité et la foi pour le mener.

## Attention

Attention à l'arrogance — même avec du génie, il faut rester connecté au réel."""
    },
    {
        "planet1": "jupiter",
        "planet2": "uranus",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Jupiter - Uranus

**En une phrase :** Tu explores l'inconnu avec joie — chaque nouveauté t'ouvre

## L'énergie de cet aspect

Ton besoin de sens (Jupiter) et ton besoin de nouveauté (Uranus) se stimulent ce mois-ci. Tu explores des territoires inconnus avec confiance. Chaque changement devient opportunité. Tu grandis en osant.

## Manifestations concrètes

- **Curiosité audacieuse** : Tu testes ce qui te fait peur, avec optimisme
- **Opportunités décalées** : Les bonnes choses viennent des chemins inattendus
- **Croissance par rupture** : Tu grandis en changeant, pas en répétant

## Conseil pratique

Dis oui à une opportunité qui sort de ta zone de confort — Jupiter-Uranus ouvre des portes inattendues.

## Attention

Gare à la superficialité — trop de nouveautés peuvent t'empêcher d'approfondir."""
    }
]


async def insert_batch_19():
    """Insère les 10 aspects du Batch 19 en base de données."""

    print(f"=== Insertion Batch 19 ({len(ASPECTS)} aspects) ===\n")

    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    inserted_count = 0

    async with async_session() as session:
        async with session.begin():
            for aspect in ASPECTS:
                planet1 = aspect['planet1']
                planet2 = aspect['planet2']
                aspect_type = aspect['aspect_type']
                content = aspect['content']

                # Normaliser en ordre alphabétique
                p1_norm = planet1.lower().strip()
                p2_norm = planet2.lower().strip()
                if p1_norm > p2_norm:
                    p1_norm, p2_norm = p2_norm, p1_norm

                # Upsert
                stmt = insert(PregeneratedNatalAspect).values(
                    planet1=p1_norm,
                    planet2=p2_norm,
                    aspect_type=aspect_type.lower(),
                    version=5,
                    lang='fr',
                    content=content,
                    length=len(content)
                )

                stmt = stmt.on_conflict_do_update(
                    index_elements=['planet1', 'planet2', 'aspect_type', 'version', 'lang'],
                    set_={
                        'content': stmt.excluded.content,
                        'length': stmt.excluded.length,
                    }
                )

                await session.execute(stmt)
                inserted_count += 1

                print(f"  ✓ {p1_norm} {aspect_type} {p2_norm}")

    await engine.dispose()

    print(f"\n✅ {inserted_count} aspects insérés (version=5, lang=fr)")

    # Vérifier le total
    await check_total_in_db()


async def check_total_in_db():
    """Vérifie le nombre total d'aspects v5 en BD."""
    engine = create_async_engine(settings.DATABASE_URL, echo=False)
    async_session = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

    async with async_session() as session:
        from sqlalchemy import select, func
        result = await session.execute(
            select(func.count()).select_from(PregeneratedNatalAspect).where(
                PregeneratedNatalAspect.version == 5,
                PregeneratedNatalAspect.lang == 'fr'
            )
        )
        count = result.scalar()

    await engine.dispose()

    print(f"🔍 Vérification BD : {count} aspects version=5 lang=fr")
    print(f"📊 Progression aspects secondaires : {count - 130}/80 aspects ({round((count - 130)/80*100, 1)}%)")


if __name__ == '__main__':
    asyncio.run(insert_batch_19())
