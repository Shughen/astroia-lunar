#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Sagittarius manquantes en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Seulement les maisons manquantes: M2, M3, M5, M6, M8, M11, M12
# M1, M4, M7, M9, M10 existent déjà
JUPITER_SAGITTARIUS = {
    ('sagittarius', 2): """# ♃ Jupiter en Sagittaire
**En une phrase :** Tu développes tes ressources avec optimisme et aventure — ta valeur réside dans ta capacité à voir plus grand et à inspirer l'abondance.

## Ton moteur
Jupiter en Sagittaire en Maison 2 te donne un rapport expansif à l'argent et aux possessions. Tu gagnes en visant haut, en prenant des risques calculés, en croyant que l'abondance vient naturellement à ceux qui osent. Les métiers liés à l'enseignement, au voyage ou à l'édition peuvent être lucratifs.

## Ton défi
Le piège : dépenser plus que tu ne gagnes par excès d'optimisme, confondre opportunité et spéculation, négliger la gestion au profit de la vision. L'abondance durable demande aussi de la discipline.

## Maison 2 en Sagittaire
Jupiter amplifie ton besoin de liberté financière. Tu préfères gagner de façon expansive que de compter chaque centime. Tes valeurs sont liées à la sagesse, l'aventure, la quête de sens.

## Micro-rituel du jour (2 min)
- Identifier une façon d'élargir ta vision de l'abondance possible pour toi
- Trois respirations en visualisant les ressources comme un horizon qui s'étend
- Journal : « Comment ma quête de sens se reflète-t-elle dans ma façon de gagner ma vie ? »""",

    ('sagittarius', 3): """# ♃ Jupiter en Sagittaire
**En une phrase :** Tu communiques avec enthousiasme et vision — tes mots élargissent les horizons de ceux qui t'écoutent.

## Ton moteur
Jupiter en Sagittaire en Maison 3 te donne une communication inspirante et visionnaire. Tu parles pour ouvrir les esprits, transmettre des idées qui font grandir, partager des découvertes qui changent la perspective. Cette configuration favorise l'enseignement, l'écriture, le journalisme.

## Ton défi
Le piège : exagérer pour convaincre, promettre plus que tu ne peux tenir verbalement, parler sans écouter. La vraie communication inclut aussi la modestie et la réception.

## Maison 3 en Sagittaire
Jupiter amplifie ton entourage vers l'international ou l'intellectuel. Tu peux avoir des frères et sœurs qui vivent loin ou qui sont dans l'enseignement. Tes apprentissages passent par l'exploration et le débat philosophique.

## Micro-rituel du jour (2 min)
- Partager une idée ou une découverte qui t'enthousiasme avec quelqu'un aujourd'hui
- Trois respirations en visualisant tes mots qui ouvrent des portes
- Journal : « Quelle idée m'a récemment donné envie d'apprendre et de transmettre ? »""",

    ('sagittarius', 5): """# ♃ Jupiter en Sagittaire
**En une phrase :** Tu crées avec foi et passion — tes œuvres, tes amours et tes joies sont des aventures qui élargissent ton horizon.

## Ton moteur
Jupiter en Sagittaire en Maison 5 te donne une créativité expansive et aventureuse. Tu crées pour explorer, pour inspirer, pour repousser les limites du possible. En amour, tu cherches des partenaires qui partagent ta soif d'aventure et de croissance.

## Ton défi
Le piège : ne jamais te satisfaire du présent en rêvant toujours d'ailleurs, fuir l'engagement amoureux par peur de perdre ta liberté, promettre plus de passion que tu ne peux offrir. La vraie joie sait aussi rester.

## Maison 5 en Sagittaire
Jupiter amplifie ton besoin d'aventure dans les plaisirs. Tu peux tomber amoureux de personnes d'autres cultures ou rencontrées en voyage. Avec les enfants ou les projets créatifs, tu transmets le goût de l'exploration et de la sagesse.

## Micro-rituel du jour (2 min)
- T'offrir une activité créative qui élargit tes horizons (nouveau style, nouvelle technique)
- Trois respirations en sentant la joie d'explorer et de créer librement
- Journal : « Quelle aventure créative ou amoureuse m'appelle en ce moment ? »""",

    ('sagittarius', 6): """# ♃ Jupiter en Sagittaire
**En une phrase :** Tu travailles avec vision et sens — ton quotidien est orienté vers des objectifs qui te dépassent et donnent du sens à l'effort.

## Ton moteur
Jupiter en Sagittaire en Maison 6 te pousse à trouver du sens dans ton travail quotidien. Tu as besoin de sentir que tes efforts contribuent à quelque chose de plus grand. Cette configuration favorise les métiers liés à l'international, à l'éducation, au conseil.

## Ton défi
Le piège : trouver les tâches routinières trop ennuyeuses, négliger les détails en faveur de la vision globale, surcharger ton quotidien par excès d'optimisme. L'efficacité durable passe aussi par l'humilité des petites choses.

## Maison 6 en Sagittaire
Jupiter amplifie ton besoin de liberté dans le travail quotidien. Tu travailles mieux quand tu as de l'autonomie et une vision claire du but. Ta santé bénéficie de l'exercice physique en extérieur et de pratiques qui nourrissent l'esprit.

## Micro-rituel du jour (2 min)
- Identifier comment une tâche quotidienne sert un objectif plus large qui te motive
- Trois respirations en reliant ton travail du jour à ta quête de sens
- Journal : « Comment mon travail quotidien contribue-t-il à quelque chose de plus grand ? »""",

    ('sagittarius', 8): """# ♃ Jupiter en Sagittaire
**En une phrase :** Tu traverses les crises avec foi — les transformations deviennent des initiations qui élargissent ta compréhension de la vie.

## Ton moteur
Jupiter en Sagittaire en Maison 8 te donne une capacité à trouver du sens dans les épreuves. Tu transformes les crises en enseignements, les pertes en sagesse. Cette configuration peut apporter des gains soudains par héritage ou investissements chanceux.

## Ton défi
Le piège : minimiser la gravité des crises par excès d'optimisme, philosopher sur la souffrance au lieu de la traverser, prendre des risques financiers excessifs. La vraie sagesse inclut aussi le respect des ombres.

## Maison 8 en Sagittaire
Jupiter amplifie ta capacité à rebondir avec foi. Tu peux avoir des insights spirituels dans les moments de crise. Les ressources partagées peuvent venir de l'étranger ou de personnes liées à l'enseignement.

## Micro-rituel du jour (2 min)
- Identifier un enseignement que tu as tiré d'une crise passée
- Trois respirations en visualisant les transformations comme des initiations
- Journal : « Quelle sagesse ai-je acquise à travers les épreuves récentes ? »""",

    ('sagittarius', 11): """# ♃ Jupiter en Sagittaire
**En une phrase :** Tu rassembles des visionnaires — tes amitiés et tes groupes sont des espaces d'exploration collective et de projets qui voient grand.

## Ton moteur
Jupiter en Sagittaire en Maison 11 te donne un talent pour rassembler des personnes autour de grandes visions. Tu attires des amis de cultures diverses, des penseurs, des voyageurs. Tes projets collectifs ont une ambition qui dépasse le local.

## Ton défi
Le piège : promettre plus que le groupe peut tenir, avoir du mal avec les détails de mise en œuvre, rassembler des gens sans jamais concrétiser. Les meilleures communautés savent aussi passer de la vision à l'action.

## Maison 11 en Sagittaire
Jupiter amplifie ton réseau vers l'international et l'intellectuel. Tu peux avoir des amis sur plusieurs continents, impliqués dans l'enseignement ou les causes humanitaires. Tes projets collectifs ont une dimension éducative ou philosophique.

## Micro-rituel du jour (2 min)
- Partager une vision inspirante avec un groupe ou un ami
- Trois respirations en visualisant ta communauté comme un cercle d'éclaireurs
- Journal : « Quelle grande vision partageons-nous dans mon cercle d'amis ? »""",

    ('sagittarius', 12): """# ♃ Jupiter en Sagittaire
**En une phrase :** Tu explores l'invisible avec confiance — ta spiritualité est une aventure de foi qui élargit tes horizons intérieurs.

## Ton moteur
Jupiter en Sagittaire en Maison 12 te donne une foi profonde dans un ordre plus grand. Tu as peut-être un guide intérieur, une connexion avec des dimensions spirituelles expansives. Cette configuration favorise les pratiques méditatives, les retraites, les pèlerinages.

## Ton défi
Le piège : utiliser la spiritualité pour fuir les contraintes du réel, confondre foi aveugle et vraie sagesse, t'attacher à des systèmes spirituels au lieu de les transcender. La vraie expansion inclut aussi le doute.

## Maison 12 en Sagittaire
Jupiter amplifie ta connexion aux dimensions invisibles. Tu peux avoir des rêves prophétiques, des intuitions qui se vérifient, un accès à une sagesse qui dépasse l'intellect. Les retraites spirituelles et les voyages intérieurs te régénèrent profondément.

## Micro-rituel du jour (2 min)
- Méditer sur l'horizon infini de ta conscience
- Trois respirations en t'ouvrant à une guidance intérieure
- Journal : « Quel message de l'invisible m'a récemment guidé ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_SAGITTARIUS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'jupiter',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP jupiter/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='jupiter',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT jupiter/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
