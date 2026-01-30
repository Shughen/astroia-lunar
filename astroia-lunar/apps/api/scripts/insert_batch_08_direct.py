#!/usr/bin/env python3
"""
Insertion directe des 10 aspects du Batch 8 en base de données (version=5)
Généré manuellement - Paires: moon-jupiter (5 aspects) + moon-saturn (5 aspects)
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

# Les 10 aspects du Batch 8
ASPECTS = [
    # === MOON-JUPITER (5 aspects) ===
    {
        "planet1": "moon",
        "planet2": "jupiter",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Lune - Jupiter

**En une phrase :** Ton cœur s'élargit — tu vois le bon partout, tu crois en la vie

## L'énergie de cet aspect

Tes besoins émotionnels (Lune) fusionnent avec ton optimisme (Jupiter) ce mois-ci. Tu te sens expansif, généreux, plein d'espoir. Tes émotions deviennent larges, accueillantes. Tu as foi en l'avenir, en les gens, en toi.

## Manifestations concrètes

- **Générosité spontanée** : Tu donnes facilement, tu partages ce que tu as
- **Optimisme contagieux** : Tu vois le positif, tu remontes le moral des autres
- **Besoin d'espace** : Tu veux explorer, voyager, découvrir de nouveaux horizons

## Conseil pratique

Dis oui à une opportunité qui t'excite — ton instinct te pousse vers du bon ce mois-ci.

## Attention

Gare aux excès — Jupiter peut te faire promettre trop, manger trop, dépenser trop."""
    },
    {
        "planet1": "moon",
        "planet2": "jupiter",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Lune - Jupiter

**En une phrase :** Tu oscilles entre confort et aventure — dur de trouver la juste mesure

## L'énergie de cet aspect

Ton besoin de sécurité (Lune) s'oppose à ton désir d'expansion (Jupiter) ce mois-ci. Une partie de toi veut rester au chaud, l'autre veut tout larguer pour vivre grand. Cette tension crée de l'agitation, parfois de la sur-compensation.

## Manifestations concrètes

- **Excès compensatoires** : Tu combles ton vide émotionnel par trop de nourriture, de dépenses, de promesses
- **Projets démesurés** : Tu vises trop grand par rapport à tes ressources réelles
- **Insatisfaction chronique** : Rien n'est jamais assez, tu veux toujours plus

## Conseil pratique

Demande-toi : qu'est-ce que je fuis en voulant toujours plus ? Puis reviens au présent.

## Attention

Attention à confondre quantité et qualité — plus n'est pas toujours mieux."""
    },
    {
        "planet1": "moon",
        "planet2": "jupiter",
        "aspect_type": "square",
        "content": """# □ Carré Lune - Jupiter

**En une phrase :** Tu promets trop, tu te surestimes — la chute risque d'être dure

## L'énergie de cet aspect

Tes émotions (Lune) et ton optimisme (Jupiter) se frottent ce mois-ci. Tu te sens invincible, tu minimises les risques, tu crois que tout va s'arranger. Mais cet excès de confiance peut te mettre dans des situations délicates.

## Manifestations concrètes

- **Promesses excessives** : Tu t'engages dans trop de choses en même temps
- **Dépenses impulsives** : Tu achètes sur un coup de tête, convaincu que l'argent rentrera
- **Naïveté dangereuse** : Tu fais confiance trop vite, tu ne vois pas les drapeaux rouges

## Conseil pratique

Avant de dire oui à quoi que ce soit, attends 24h — ton enthousiasme a besoin d'un filtre.

## Attention

Gare à la sur-confiance — Jupiter peut te faire croire que tu es immunisé contre les conséquences."""
    },
    {
        "planet1": "moon",
        "planet2": "jupiter",
        "aspect_type": "trine",
        "content": """# △ Trigone Lune - Jupiter

**En une phrase :** Ta foi te porte — tu attires naturellement le bon

## L'énergie de cet aspect

Tes besoins (Lune) et ton optimisme (Jupiter) collaborent ce mois-ci. Tu te sens bien, confiant, aligné. Ta générosité attire la générosité. Ta foi crée des opportunités. Tu es au bon endroit au bon moment.

## Manifestations concrètes

- **Chance facile** : Les choses se placent, les portes s'ouvrent sans forcer
- **Relations enrichissantes** : Tu rencontres des gens qui t'élèvent, t'inspirent
- **Sérénité profonde** : Tu sais que tout va bien, même quand c'est compliqué

## Conseil pratique

Partage ton abondance — qu'elle soit matérielle, émotionnelle ou intellectuelle — elle se multipliera.

## Attention

Attention à tenir cette chance pour acquise — la gratitude maintient le flux."""
    },
    {
        "planet1": "moon",
        "planet2": "jupiter",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Lune - Jupiter

**En une phrase :** Tu grandis en douceur — chaque expérience nourrit ton espoir

## L'énergie de cet aspect

Tes émotions (Lune) et ton besoin de sens (Jupiter) se stimulent ce mois-ci. Tu apprends de ce que tu vis. Tes expériences te font grandir. Tu trouves du bon même dans les moments difficiles.

## Manifestations concrètes

- **Optimisme réaliste** : Tu vois le positif sans nier le négatif
- **Apprentissages fluides** : Ce que tu découvres s'intègre facilement, ça nourrit ton cœur
- **Générosité mesurée** : Tu donnes sans te vider, tu reçois sans culpabilité

## Conseil pratique

Explore une philosophie, une spiritualité, un enseignement qui t'attire — tu es prêt à grandir.

## Attention

Gare à éviter les émotions difficiles sous prétexte de rester positif — tout a sa place."""
    },

    # === MOON-SATURN (5 aspects) ===
    {
        "planet1": "moon",
        "planet2": "saturn",
        "aspect_type": "conjunction",
        "content": """# ☌ Conjonction Lune - Saturne

**En une phrase :** Ton cœur se durcit — tu te protèges mais tu te gèles aussi

## L'énergie de cet aspect

Tes besoins émotionnels (Lune) fusionnent avec tes limites (Saturne) ce mois-ci. Tu ressens de la lourdeur, de la solitude, parfois de la tristesse. Tes émotions deviennent sérieuses, contrôlées, parfois étouffées. Tu as du mal à demander de l'aide.

## Manifestations concrètes

- **Isolement choisi** : Tu te retires, tu préfères être seul que vulnérable
- **Émotions réprimées** : Tu ne pleures pas, tu ne montres pas ta peine
- **Responsabilités lourdes** : Tu portes tout seul, tu ne délègues pas

## Conseil pratique

Autorise-toi une émotion que tu retiens — pleure, crie, écris — laisse sortir la pression.

## Attention

Gare à la dépression silencieuse — Saturne peut transformer la tristesse en résignation."""
    },
    {
        "planet1": "moon",
        "planet2": "saturn",
        "aspect_type": "opposition",
        "content": """# ☍ Opposition Lune - Saturne

**En une phrase :** Tu veux être aimé mais tu te penses indigne — le rejet te hante

## L'énergie de cet aspect

Ton besoin de connexion (Lune) s'oppose à ta peur du rejet (Saturne) ce mois-ci. Tu veux qu'on s'occupe de toi mais tu crois que tu ne le mérites pas. Cette tension crée de la distance dans tes relations, parfois de l'amertume.

## Manifestations concrètes

- **Peur de déranger** : Tu n'oses pas demander de l'aide, tu minimises tes besoins
- **Rejet anticipé** : Tu te retires avant qu'on te rejette
- **Relations froides** : Tu gardes les gens à distance pour te protéger

## Conseil pratique

Demande un câlin, un soutien, une présence — même si ça fait peur, même si tu crois ne pas le mériter.

## Attention

Attention à tester les gens — si tu pousses tout le monde, tu te retrouveras seul par prophétie auto-réalisatrice."""
    },
    {
        "planet1": "moon",
        "planet2": "saturn",
        "aspect_type": "square",
        "content": """# □ Carré Lune - Saturne

**En une phrase :** Tes émotions te font honte — tu te punis d'avoir des besoins

## L'énergie de cet aspect

Tes besoins (Lune) entrent en conflit avec ton exigence (Saturne) ce mois-ci. Tu te juges d'être faible quand tu ressens quelque chose. Tes émotions te semblent déplacées, embarrassantes. Cette guerre intérieure crée de la tristesse, de la rigidité.

## Manifestations concrètes

- **Auto-critique sévère** : Tu te traites durement quand tu pleures ou que tu as besoin
- **Émotions gelées** : Tu ne ressens plus grand-chose, comme anesthésié
- **Devoirs écrasants** : Tu t'imposes des responsabilités pour ne pas sentir

## Conseil pratique

Parle à ton enfant intérieur — dis-lui qu'il a le droit d'avoir besoin, d'être triste, d'être humain.

## Attention

Gare à la dureté avec toi-même — Saturne peut devenir un tyran intérieur si tu ne poses pas de limites."""
    },
    {
        "planet1": "moon",
        "planet2": "saturn",
        "aspect_type": "trine",
        "content": """# △ Trigone Lune - Saturne

**En une phrase :** Ta maturité émotionnelle devient ta force — tu tiens debout sereinement

## L'énergie de cet aspect

Tes émotions (Lune) et ta structure (Saturne) travaillent ensemble ce mois-ci. Tu sais ce dont tu as besoin et tu le poses calmement. Tu assumes ta sensibilité sans t'excuser. Tes limites sont claires, tes émotions sont stables.

## Manifestations concrètes

- **Stabilité émotionnelle** : Tu ne te laisses plus déstabiliser facilement
- **Limites saines** : Tu protèges ton cœur sans te couper des autres
- **Sagesse tranquille** : Tu comprends que les émotions passent, tu ne t'y identifies plus

## Conseil pratique

Deviens une présence stable pour quelqu'un qui en a besoin — ton calme peut apaiser.

## Attention

Attention à devenir trop stoïque — parfois il faut aussi lâcher le contrôle et laisser couler."""
    },
    {
        "planet1": "moon",
        "planet2": "saturn",
        "aspect_type": "sextile",
        "content": """# ⚹ Sextile Lune - Saturne

**En une phrase :** Tu construis ta sécurité émotionnelle — pierre par pierre, tu te stabilises

## L'énergie de cet aspect

Tes besoins (Lune) et ta capacité à structurer (Saturne) se complètent ce mois-ci. Tu identifies ce qui te fait du bien et tu le protèges. Tu poses des limites douces mais fermes. Tu construis ta stabilité intérieure.

## Manifestations concrètes

- **Routines réconfortantes** : Tu crées des rituels qui te font du bien
- **Limites claires** : Tu dis non sans culpabiliser, tu préserves ton énergie
- **Engagement mesuré** : Tu choisis tes batailles, tu ne te disperses plus

## Conseil pratique

Crée une routine qui nourrit ton cœur — méditation, marche, journal — et tiens-la sur la durée.

## Attention

Gare à confondre sécurité et rigidité — parfois il faut aussi laisser place à l'imprévu."""
    }
]


async def insert_batch_08():
    """Insère les 10 aspects du Batch 8 en base de données."""

    print(f"=== Insertion Batch 8 ({len(ASPECTS)} aspects) ===\n")

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
    print(f"📊 Progression : {count}/130 aspects ({round(count/130*100, 1)}%)")


if __name__ == '__main__':
    asyncio.run(insert_batch_08())
