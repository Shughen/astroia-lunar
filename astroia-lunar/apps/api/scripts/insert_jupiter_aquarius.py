#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Aquarius en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_AQUARIUS = {
    ('aquarius', 1): """# ♃ Jupiter en Verseau
**En une phrase :** Tu incarnes une présence originale et visionnaire qui inspire les autres à penser différemment et à embrasser le changement.

## Ton moteur
Jupiter en Verseau en Maison 1 te donne une aura d'innovation et d'indépendance. Tu ne rentres pas dans les cases, tu crées les tiennes. Cette configuration amplifie ton besoin de liberté et ta capacité à voir le futur avant les autres.

## Ton défi
Le piège : te définir uniquement par ta différence, rejeter la tradition sans discernement, confondre originalité et provocation. La vraie innovation sait aussi reconnaître ce qui fonctionne.

## Maison 1 en Verseau
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un d'unique, de progressiste, parfois un peu excentrique. Ton corps reflète ton non-conformisme — style personnel, gestuelle imprévisible.

## Micro-rituel du jour (2 min)
- Exprimer une idée ou un aspect de toi qui te rend unique
- Trois respirations en appréciant ce qui te distingue des autres
- Journal : « Comment ma différence a-t-elle inspiré quelqu'un récemment ? »""",

    ('aquarius', 2): """# ♃ Jupiter en Verseau
**En une phrase :** Tu développes tes ressources de façon innovante — ta valeur réside dans ta capacité à voir des opportunités que les autres n'imaginent pas.

## Ton moteur
Jupiter en Verseau en Maison 2 te pousse à générer de l'abondance par l'innovation et la technologie. Tu n'es pas attaché aux façons traditionnelles de gagner de l'argent. Les domaines de pointe, les startups, le numérique peuvent être lucratifs pour toi.

## Ton défi
Le piège : être trop détaché de l'argent, avoir des revenus irréguliers par manque de structure, négliger les besoins matériels de base. L'abondance demande aussi de l'attention au concret.

## Maison 2 en Verseau
Jupiter amplifie ton rapport innovant à l'argent. Tu peux avoir des sources de revenus atypiques ou liées à la technologie. Tes valeurs sont liées à la liberté, l'innovation, le collectif.

## Micro-rituel du jour (2 min)
- Identifier une façon innovante de valoriser une de tes compétences
- Trois respirations en connectant abondance et liberté
- Journal : « Quelle innovation pourrait améliorer ma situation financière ? »""",

    ('aquarius', 3): """# ♃ Jupiter en Verseau
**En une phrase :** Tu communiques avec originalité et vision — tes idées sont en avance sur leur temps et stimulent de nouvelles façons de penser.

## Ton moteur
Jupiter en Verseau en Maison 3 te donne une communication innovante et non conventionnelle. Tu remets en question les évidences, tu proposes des perspectives nouvelles. Cette configuration favorise les métiers de l'innovation, de la technologie, de la communication de rupture.

## Ton défi
Le piège : communiquer de façon trop abstraite ou futuriste, avoir du mal à te faire comprendre du commun des mortels, rejeter les idées conventionnelles sans les examiner. La vraie innovation sait aussi être accessible.

## Maison 3 en Verseau
Jupiter amplifie ton réseau de contacts variés et originaux. Tes relations avec frères, sœurs et voisins peuvent être atypiques ou à distance. Tu apprends par l'expérimentation et la remise en question.

## Micro-rituel du jour (2 min)
- Partager une idée innovante ou originale avec quelqu'un
- Trois respirations en ouvrant ton esprit à des perspectives nouvelles
- Journal : « Quelle idée non conventionnelle m'a récemment enthousiasmé ? »""",

    ('aquarius', 4): """# ♃ Jupiter en Verseau
**En une phrase :** Ton foyer est un laboratoire de vie — tu crées un chez-toi qui expérimente de nouvelles façons de vivre ensemble.

## Ton moteur
Jupiter en Verseau en Maison 4 te donne un rapport innovant à ton espace de vie. Tu peux vivre dans un logement atypique, expérimenter des formes de cohabitation alternatives, ou simplement avoir un foyer qui ne ressemble à aucun autre.

## Ton défi
Le piège : avoir du mal à créer des racines stables, idéaliser la liberté au détriment de la sécurité, déconnecter de tes origines par souci d'originalité. Le vrai foyer a aussi besoin de continuité.

## Maison 4 en Verseau
Jupiter amplifie l'aspect innovant de ta vie familiale. Tu as peut-être grandi dans une famille non conventionnelle ou tu crées la tienne selon des règles nouvelles. Ton foyer peut être un lieu de rassemblement pour des gens de tous horizons.

## Micro-rituel du jour (2 min)
- Identifier un aspect de ton foyer ou ta vie familiale qui est unique et le célébrer
- Trois respirations en connectant liberté et appartenance
- Journal : « Comment mon foyer reflète-t-il mes valeurs innovantes ? »""",

    ('aquarius', 5): """# ♃ Jupiter en Verseau
**En une phrase :** Tu crées avec originalité et vision — tes œuvres, tes amours et tes joies sont des expérimentations qui brisent les conventions.

## Ton moteur
Jupiter en Verseau en Maison 5 te donne une créativité avant-gardiste et expérimentale. Tu ne crées pas pour plaire mais pour explorer de nouvelles possibilités. En amour, tu cherches des partenaires qui respectent ta liberté et partagent ta vision du futur.

## Ton défi
Le piège : avoir du mal avec l'engagement amoureux traditionnel, créer pour choquer plutôt que pour exprimer, confondre détachement et liberté. La vraie joie sait aussi s'ancrer dans l'intimité.

## Maison 5 en Verseau
Jupiter amplifie ton besoin de liberté dans les plaisirs. Tu peux avoir des relations amoureuses non conventionnelles ou être attiré par des partenaires excentriques. Ta créativité peut toucher à la technologie ou aux arts expérimentaux.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui sort de l'ordinaire
- Trois respirations en laissant ta créativité être libre et imprévisible
- Journal : « Quelle création récente m'a permis d'exprimer mon originalité ? »""",

    ('aquarius', 6): """# ♃ Jupiter en Verseau
**En une phrase :** Tu travailles avec innovation et indépendance — ton quotidien est une expérimentation continue de nouvelles façons d'être efficace.

## Ton moteur
Jupiter en Verseau en Maison 6 te pousse à réinventer ta façon de travailler. Tu es attiré par les environnements flexibles, les méthodes innovantes, les technologies qui transforment le quotidien. Cette configuration favorise les métiers de la tech, des startups, de l'innovation sociale.

## Ton défi
Le piège : avoir du mal avec les routines traditionnelles, résister aux structures nécessaires, confondre innovation et désorganisation. L'efficacité demande parfois des méthodes éprouvées.

## Maison 6 en Verseau
Jupiter amplifie ton besoin de liberté dans le travail quotidien. Tu travailles mieux avec de l'autonomie et des horaires flexibles. Ta santé peut bénéficier d'approches alternatives ou de technologies de bien-être.

## Micro-rituel du jour (2 min)
- Identifier une innovation qui pourrait améliorer ta routine quotidienne
- Trois respirations en acceptant que l'efficacité peut prendre différentes formes
- Journal : « Quelle nouvelle façon de travailler m'a récemment inspiré ? »""",

    ('aquarius', 7): """# ♃ Jupiter en Verseau
**En une phrase :** Tes relations sont des expérimentations — tu cherches des partenaires qui partagent ta vision du futur et respectent ton besoin de liberté.

## Ton moteur
Jupiter en Verseau en Maison 7 te pousse vers des partenariats non conventionnels. Tu as besoin de liberté dans le couple, de partenaires qui pensent différemment. Tu attires des personnes originales, parfois excentriques, toujours stimulantes intellectuellement.

## Ton défi
Le piège : fuir l'engagement par peur de perdre ta liberté, avoir du mal avec l'intimité traditionnelle, idéaliser des partenariats utopiques. Les meilleures relations combinent liberté et engagement.

## Maison 7 en Verseau
Jupiter amplifie ton besoin d'innovation dans les partenariats. Tu peux avoir des mariages ou des associations qui ne rentrent pas dans les moules. Tes contrats peuvent être liés à des projets innovants ou technologiques.

## Micro-rituel du jour (2 min)
- Proposer quelque chose de nouveau ou d'inhabituel à un partenaire
- Trois respirations en équilibrant connexion et liberté
- Journal : « Comment mes partenariats permettent-ils à chacun de rester unique ? »""",

    ('aquarius', 8): """# ♃ Jupiter en Verseau
**En une phrase :** Tu traverses les crises avec détachement visionnaire — les transformations deviennent des occasions de réinventer ta façon de vivre.

## Ton moteur
Jupiter en Verseau en Maison 8 te donne une capacité à voir les crises comme des opportunités de changement radical. Tu n'as pas peur de tout remettre en question, de tout reconstruire différemment. Les ressources partagées peuvent venir de projets innovants ou technologiques.

## Ton défi
Le piège : te détacher émotionnellement au lieu de traverser la douleur, intellectualiser les transformations sans les vivre, confondre rupture et libération. La vraie transformation inclut aussi les émotions.

## Maison 8 en Verseau
Jupiter amplifie ta capacité à innover dans les moments de crise. Tu peux avoir des insights visionnaires sur les transformations nécessaires. Ta sexualité peut être liée à l'expérimentation ou au détachement.

## Micro-rituel du jour (2 min)
- Identifier une transformation en cours et imaginer des façons nouvelles de la traverser
- Trois respirations en acceptant les émotions qui accompagnent le changement
- Journal : « Quelle crise récente m'a ouvert à de nouvelles possibilités ? »""",

    ('aquarius', 9): """# ♃ Jupiter en Verseau
**En une phrase :** Ta quête de sens est révolutionnaire — tu cherches des philosophies qui libèrent l'esprit et préparent le monde de demain.

## Ton moteur
Jupiter en Verseau en Maison 9 te donne une soif de connaissances qui remettent en question les paradigmes établis. Tu es attiré par les philosophies progressistes, les sciences du futur, les visions utopiques. Cette configuration favorise l'étude des systèmes, de la technologie, des alternatives.

## Ton défi
Le piège : rejeter la sagesse traditionnelle par réflexe, adhérer à des utopies irréalistes, confondre originalité et vérité. La vraie sagesse intègre aussi le passé.

## Maison 9 en Verseau
Jupiter amplifie ton rapport progressiste aux grandes questions. Tu peux étudier des domaines de pointe ou voyager pour découvrir des expérimentations sociales. Ton enseignement est orienté vers le futur.

## Micro-rituel du jour (2 min)
- Explorer une idée ou une philosophie qui challenge tes croyances actuelles
- Trois respirations en t'ouvrant à une vision du monde élargie
- Journal : « Quelle vision du futur m'inspire actuellement ? »""",

    ('aquarius', 10): """# ♃ Jupiter en Verseau
**En une phrase :** Ta carrière est une mission — tu réussis en apportant des solutions innovantes à des problèmes que les autres n'osent pas affronter.

## Ton moteur
Jupiter en Verseau en Maison 10 te pousse vers des professions innovantes ou humanitaires. Tu ne veux pas juste réussir, tu veux changer le monde. Cette configuration favorise les carrières dans la tech, l'innovation sociale, les organisations progressistes.

## Ton défi
Le piège : être trop en avance sur ton temps pour être reconnu, avoir du mal avec les structures hiérarchiques traditionnelles, confondre provocation et leadership. Le vrai impact sait aussi collaborer avec le système.

## Maison 10 en Verseau
Jupiter amplifie ta réputation d'innovateur et de visionnaire. On te remarque pour tes idées originales, ta capacité à penser différemment. Ta carrière peut être liée à des causes progressistes ou technologiques.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière contribue à un changement positif dans le monde
- Trois respirations en connectant ton ambition à une mission plus large
- Journal : « Quel impact innovant ai-je envie d'avoir dans mon domaine ? »""",

    ('aquarius', 11): """# ♃ Jupiter en Verseau
**En une phrase :** Tu rassembles des visionnaires — tes amitiés et tes groupes sont des laboratoires d'idées nouvelles et de projets qui changent le monde.

## Ton moteur
Jupiter en Verseau en Maison 11 est une position puissante pour l'action collective et l'innovation sociale. Tu attires des amis originaux et visionnaires. Tes projets humanitaires sont à la pointe du changement social ou technologique.

## Ton défi
Le piège : préférer les idéaux aux personnes réelles, avoir du mal avec les imperfections des groupes, te disperser dans trop de causes. Les meilleures communautés acceptent aussi leurs limites.

## Maison 11 en Verseau
Jupiter amplifie au maximum ton influence dans les réseaux innovants. Tu es fait pour les projets collectifs qui changent le monde. Tes amis sont des innovateurs, des rebelles, des penseurs du futur.

## Micro-rituel du jour (2 min)
- Partager une vision d'avenir inspirante avec un groupe ou un ami
- Trois respirations en visualisant ta communauté comme un réseau de changement
- Journal : « Quel projet collectif m'enthousiasme le plus actuellement ? »""",

    ('aquarius', 12): """# ♃ Jupiter en Verseau
**En une phrase :** Tu explores l'invisible avec une vision du futur — ta spiritualité est connectée à la conscience collective et aux possibilités évolutives de l'humanité.

## Ton moteur
Jupiter en Verseau en Maison 12 crée un pont entre ta vision progressiste et les dimensions invisibles. Tu peux percevoir les courants de l'inconscient collectif, avoir des intuitions sur l'évolution de l'humanité. Ta spiritualité est connectée au nous plutôt qu'au je.

## Ton défi
Le piège : fuir l'intimité spirituelle dans les grandes causes, confondre détachement et éveil, avoir du mal avec les aspects personnels de la transformation. La vraie spiritualité inclut aussi le cœur.

## Maison 12 en Verseau
Jupiter amplifie ta connexion à l'inconscient collectif. Tu peux avoir des rêves ou des intuitions sur l'avenir de l'humanité. Les pratiques spirituelles en groupe ou connectées à une vision planétaire te conviennent particulièrement.

## Micro-rituel du jour (2 min)
- Méditer sur ta connexion à quelque chose de plus grand que toi
- Trois respirations en t'ouvrant à l'inconscient collectif
- Journal : « Quel message de l'invisible concernant l'avenir ai-je reçu récemment ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_AQUARIUS.items():
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
