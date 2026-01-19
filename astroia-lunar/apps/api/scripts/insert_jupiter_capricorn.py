#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Capricorn en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_CAPRICORN = {
    ('capricorn', 1): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu incarnes une présence sobre et ambitieuse qui inspire le respect par ta maturité et ta rigueur.

## Ton moteur
Jupiter en Capricorne en Maison 1 te donne une aura de sérieux et de compétence. Tu ne cherches pas à impressionner par le spectacle mais par les résultats. Cette configuration amplifie ton ambition et ta capacité à construire sur le long terme.

## Ton défi
Le piège : paraître trop froid ou inaccessible, confondre respect et distance, te priver de légèreté par souci de crédibilité. La vraie autorité sait aussi sourire.

## Maison 1 en Capricorne
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un de responsable, de mature, d'ambitieux. Ton corps reflète ta rigueur — posture droite, gestuelle mesurée, présence sobre.

## Micro-rituel du jour (2 min)
- Identifier un objectif ambitieux que tu as accompli et reconnaître ta valeur
- Trois respirations en te permettant un moment de détente
- Journal : « Comment ma rigueur m'a-t-elle servi récemment ? »""",

    ('capricorn', 2): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu construis ta sécurité financière avec méthode et patience — ta valeur se mesure à tes accomplissements durables.

## Ton moteur
Jupiter en Capricorne en Maison 2 te donne un rapport discipliné à l'argent. Tu accumules avec prudence, tu investis pour le long terme, tu construis une sécurité qui dure. Les métiers liés à la gestion, l'immobilier, ou les entreprises familiales peuvent être lucratifs.

## Ton défi
Le piège : être trop restrictif financièrement, confondre richesse et statut, te priver de plaisirs par austérité excessive. L'abondance mérite aussi d'être appréciée.

## Maison 2 en Capricorne
Jupiter amplifie ton besoin de sécurité matérielle structurée. Tu préfères les investissements sûrs aux paris risqués. Tes valeurs sont liées au travail, à la responsabilité, à la construction durable.

## Micro-rituel du jour (2 min)
- Célébrer une ressource que tu as patiemment construite
- Trois respirations en acceptant de profiter de ce que tu possèdes
- Journal : « Quelle construction financière me rend fier aujourd'hui ? »""",

    ('capricorn', 3): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu communiques avec autorité et structure — tes mots ont du poids parce qu'ils sont réfléchis et fondés sur l'expérience.

## Ton moteur
Jupiter en Capricorne en Maison 3 te donne une communication sobre et efficace. Tu ne parles pas pour rien : chaque mot compte. Cette configuration favorise les écrits structurés, les présentations professionnelles, l'enseignement technique.

## Ton défi
Le piège : communiquer de façon trop formelle, avoir du mal avec la légèreté conversationnelle, paraître condescendant. La vraie autorité sait aussi plaisanter.

## Maison 3 en Capricorne
Jupiter amplifie la rigueur de tes échanges. Tes relations avec frères, sœurs et voisins peuvent être marquées par le respect ou la compétition. Tu apprends de façon méthodique et structurée.

## Micro-rituel du jour (2 min)
- Partager une idée ou une connaissance de façon concise et utile
- Trois respirations en te permettant aussi la légèreté dans les échanges
- Journal : « Quelle expertise ai-je partagée récemment de façon efficace ? »""",

    ('capricorn', 4): """# ♃ Jupiter en Capricorne
**En une phrase :** Ton foyer est une fondation solide — tu crées un chez-toi structuré qui soutient tes ambitions et ta stabilité.

## Ton moteur
Jupiter en Capricorne en Maison 4 te donne un rapport sérieux à ton espace de vie. Tu investis dans la pierre, tu construis des traditions familiales durables, tu crées un foyer qui représente ta réussite. La famille peut être liée à tes ambitions professionnelles.

## Ton défi
Le piège : faire passer le travail avant la vie familiale, transformer le foyer en vitrine de réussite, avoir du mal à te détendre chez toi. Le vrai foyer a aussi besoin de chaleur et d'imperfection.

## Maison 4 en Capricorne
Jupiter amplifie ton besoin de structure domestique. Tu as peut-être hérité de responsabilités familiales tôt ou grandi avec un parent autoritaire. Ton foyer peut être lié à un patrimoine ou une tradition à perpétuer.

## Micro-rituel du jour (2 min)
- Identifier un aspect de ton foyer dont tu es fier et le célébrer
- Trois respirations en te permettant de te sentir chez toi, pas en représentation
- Journal : « Comment mon foyer soutient-il mes ambitions et ma stabilité ? »""",

    ('capricorn', 5): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu crées avec discipline et ambition — tes œuvres, tes amours et tes joies ont une structure qui leur donne de la durabilité.

## Ton moteur
Jupiter en Capricorne en Maison 5 te donne une créativité qui se construit avec méthode. Tu préfères les œuvres accomplies aux inspirations passagères. En amour, tu cherches des partenaires matures avec qui construire quelque chose de solide.

## Ton défi
Le piège : avoir du mal à te lâcher dans le plaisir, transformer la créativité en travail, confondre mériter la joie et la recevoir librement. La vraie créativité sait aussi être spontanée.

## Maison 5 en Capricorne
Jupiter amplifie ta discipline dans les domaines du plaisir. Tu peux attirer des partenaires plus âgés ou plus établis. Avec les enfants ou les projets créatifs, tu transmets la valeur du travail bien fait.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir sans te demander si tu le mérites
- Trois respirations en laissant la joie exister sans productivité
- Journal : « Comment puis-je m'autoriser plus de légèreté dans mes plaisirs ? »""",

    ('capricorn', 6): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu travailles avec excellence et ambition — ton quotidien est une ascension méthodique vers la maîtrise de ton domaine.

## Ton moteur
Jupiter en Capricorne en Maison 6 te donne une éthique de travail remarquable. Tu vises l'excellence dans tout ce que tu entreprends, tu acceptes de gravir les échelons patiemment. Cette configuration favorise les carrières qui récompensent la compétence et l'ancienneté.

## Ton défi
Le piège : te surmener par perfectionnisme, avoir du mal à déléguer, négliger ta santé au profit de ta productivité. L'efficacité durable inclut aussi le repos.

## Maison 6 en Capricorne
Jupiter amplifie ta rigueur dans le travail quotidien. Tu as besoin de structure et de responsabilités claires. Ta santé bénéficie de routines disciplinées mais souffre du stress et de l'excès de travail.

## Micro-rituel du jour (2 min)
- Identifier un accomplissement quotidien et le reconnaître
- Trois respirations en relâchant la pression de la performance
- Journal : « Comment puis-je maintenir mon excellence sans m'épuiser ? »""",

    ('capricorn', 7): """# ♃ Jupiter en Capricorne
**En une phrase :** Tes relations sont des alliances stratégiques — tu cherches des partenaires qui partagent tes ambitions et ta vision à long terme.

## Ton moteur
Jupiter en Capricorne en Maison 7 te pousse vers des partenariats sérieux et durables. Tu ne t'engages pas à la légère, mais une fois lié, tu construis avec patience et loyauté. Les partenariats professionnels peuvent être particulièrement importants.

## Ton défi
Le piège : choisir des partenaires pour leur statut plutôt que pour l'amour, avoir du mal à exprimer la tendresse, transformer le couple en entreprise. Les meilleures relations incluent aussi la spontanéité.

## Maison 7 en Capricorne
Jupiter amplifie ton besoin de sécurité dans les partenariats. Tu peux attirer des partenaires plus âgés, plus établis ou plus ambitieux. Tes contrats et mariages sont réfléchis et orientés vers le long terme.

## Micro-rituel du jour (2 min)
- Exprimer de la tendresse à un partenaire de façon spontanée
- Trois respirations en acceptant la vulnérabilité dans la relation
- Journal : « Comment puis-je ajouter plus de chaleur à mes partenariats ? »""",

    ('capricorn', 8): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu traverses les crises avec discipline — les transformations deviennent des occasions de reconstruire sur des bases plus solides.

## Ton moteur
Jupiter en Capricorne en Maison 8 te donne une capacité à gérer les crises de façon structurée. Tu transformes les pertes en apprentissages, tu gères les ressources partagées avec rigueur. Cette configuration peut apporter des responsabilités liées aux héritages ou aux patrimoines.

## Ton défi
Le piège : contrôler les émotions profondes au lieu de les traverser, transformer la transformation en projet, avoir du mal à lâcher prise. La vraie renaissance demande parfois de perdre le contrôle.

## Maison 8 en Capricorne
Jupiter amplifie ta capacité à structurer les ressources partagées. Tu peux hériter de responsabilités ou de patrimoine. Ta sexualité peut être liée au pouvoir, au contrôle ou à l'engagement profond.

## Micro-rituel du jour (2 min)
- Identifier un domaine de ta vie qui demande un lâcher-prise que tu évites
- Trois respirations en acceptant que la transformation n'est pas toujours contrôlable
- Journal : « Quelle restructuration profonde suis-je en train de traverser ? »""",

    ('capricorn', 9): """# ♃ Jupiter en Capricorne
**En une phrase :** Ta quête de sens est pragmatique — tu cherches des philosophies qui fonctionnent concrètement et qui se prouvent par les résultats.

## Ton moteur
Jupiter en Capricorne en Maison 9 te donne un rapport structuré aux grandes questions. Tu ne te satisfais pas des croyances vagues : tu veux des systèmes qui tiennent la route, des philosophies applicables. Cette configuration favorise le droit, l'économie, les études de systèmes.

## Ton défi
Le piège : rejeter les philosophies qui ne sont pas prouvables, confondre cynisme et réalisme, manquer de foi ou d'émerveillement. La vraie sagesse accepte aussi le mystère.

## Maison 9 en Capricorne
Jupiter amplifie ton besoin de structure dans l'exploration des grandes idées. Tu peux étudier des domaines sérieux et traditionnels. Les voyages d'affaires ou d'études t'attirent plus que le tourisme sans but.

## Micro-rituel du jour (2 min)
- Identifier une croyance ou une philosophie qui structure ta vie de façon utile
- Trois respirations en t'ouvrant à une dimension de mystère
- Journal : « Quelle sagesse pratique guide mes décisions importantes ? »""",

    ('capricorn', 10): """# ♃ Jupiter en Capricorne
**En une phrase :** Ta carrière est ton chef-d'œuvre — tu construis ta réussite avec patience, méthode et une vision à long terme.

## Ton moteur
Jupiter en Capricorne en Maison 10 te donne une ambition professionnelle structurée et puissante. Tu vises le sommet, mais tu acceptes de gravir chaque marche. Cette configuration favorise les grandes carrières dans les domaines traditionnels, la direction, l'entrepreneuriat durable.

## Ton défi
Le piège : sacrifier ta vie personnelle à ta carrière, confondre réussite et valeur personnelle, avoir du mal à profiter de tes accomplissements. Le vrai succès inclut aussi le bonheur.

## Maison 10 en Capricorne
Jupiter amplifie au maximum ton ambition et ton sens de la structure. Tu es fait pour les positions de responsabilité et de leadership. Ta réputation se construit sur tes accomplissements concrets et ta fiabilité.

## Micro-rituel du jour (2 min)
- Célébrer un accomplissement professionnel et te permettre d'en être fier
- Trois respirations en séparant ta valeur de tes résultats
- Journal : « Comment puis-je apprécier ma réussite tout en continuant à grandir ? »""",

    ('capricorn', 11): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu construis des réseaux structurés — tes amitiés et tes groupes sont des alliances qui servent des objectifs clairs et durables.

## Ton moteur
Jupiter en Capricorne en Maison 11 te donne un talent pour organiser les groupes et les projets collectifs de façon efficace. Tu attires des amis ambitieux et responsables. Tes projets humanitaires ont une structure et des objectifs mesurables.

## Ton défi
Le piège : transformer les amitiés en relations utilitaires, avoir du mal avec les groupes non structurés, préférer l'efficacité à la chaleur. Les meilleures communautés incluent aussi l'informel.

## Maison 11 en Capricorne
Jupiter amplifie ta capacité à structurer les projets collectifs. Tu peux attirer des amis plus âgés ou plus établis. Tes réseaux peuvent être liés à ta carrière ou à des institutions respectées.

## Micro-rituel du jour (2 min)
- Contacter un ami juste pour le plaisir, sans objectif particulier
- Trois respirations en acceptant l'amitié pour ce qu'elle est
- Journal : « Comment puis-je ajouter plus de chaleur à mes réseaux ? »""",

    ('capricorn', 12): """# ♃ Jupiter en Capricorne
**En une phrase :** Tu explores l'invisible avec discipline — ta spiritualité passe par des pratiques structurées qui construisent une sagesse durable.

## Ton moteur
Jupiter en Capricorne en Maison 12 crée un pont entre ta rigueur et le monde invisible. Tu as peut-être une spiritualité sobre, orientée vers les résultats intérieurs. Les traditions contemplatives anciennes peuvent t'attirer particulièrement.

## Ton défi
Le piège : vouloir contrôler l'inconscient avec des méthodes, juger ta progression spirituelle comme une carrière, avoir du mal à lâcher la structure. Le sacré échappe parfois aux plans.

## Maison 12 en Capricorne
Jupiter amplifie ta quête de maîtrise spirituelle. Tu peux avoir des talents cachés de guérisseur ou de guide, que tu exerces discrètement. Les retraites qui combinent discipline et silence te conviennent particulièrement.

## Micro-rituel du jour (2 min)
- Pratiquer une méditation ou une contemplation avec structure et lâcher-prise
- Trois respirations en acceptant que l'invisible n'a pas de deadline
- Journal : « Quelle pratique spirituelle structurée me connecte au mystère ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_CAPRICORN.items():
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
