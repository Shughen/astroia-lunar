#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Virgo en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_VIRGO = {
    ('virgo', 1): """# ♃ Jupiter en Vierge
**En une phrase :** Tu incarnes une présence utile et fiable — on te reconnaît pour ta capacité à améliorer concrètement les situations.

## Ton moteur
Jupiter en Vierge en Maison 1 te donne une aura de compétence pratique. Tu observes, tu analyses, tu proposes des solutions. Cette configuration amplifie ton besoin d'être utile et reconnu pour ton efficacité plutôt que pour ton charisme.

## Ton défi
Le piège : être trop critique envers toi-même et les autres, te perdre dans les détails au détriment de la vision globale, minimiser tes réussites. L'expansion véritable accepte aussi l'imperfection.

## Maison 1 en Vierge
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un de précis, de serviable, de modeste mais compétent. Ton corps reflète ton attention aux détails — soigné, fonctionnel.

## Micro-rituel du jour (2 min)
- Améliorer un petit détail concret dans ton environnement immédiat
- Trois respirations en acceptant que tu es assez tel que tu es
- Journal : « Comment ai-je été utile à quelqu'un aujourd'hui ? »""",

    ('virgo', 2): """# ♃ Jupiter en Vierge
**En une phrase :** Tu construis ta sécurité par le travail bien fait — ta valeur se mesure à ta compétence et à ton utilité concrète.

## Ton moteur
Jupiter en Vierge en Maison 2 te pousse à gagner de l'argent par ton savoir-faire technique. Tu économises avec méthode, tu investis dans ce qui a une vraie utilité. Cette configuration favorise les métiers de service, d'analyse, de santé.

## Ton défi
Le piège : ne jamais te sentir assez compétent pour mériter ton salaire, être trop prudent financièrement, confondre frugalité et avarice. L'abondance mérite aussi d'être appréciée.

## Maison 2 en Vierge
Jupiter amplifie ton rapport analytique à l'argent. Tu calcules, tu compares, tu optimises. Tes valeurs sont liées au travail bien fait, à la santé, à l'amélioration continue. Tu dépenses pour des choses utiles et durables.

## Micro-rituel du jour (2 min)
- Identifier une compétence que tu pourrais mieux valoriser financièrement
- Trois respirations en acceptant que tu mérites l'abondance
- Journal : « Quelle expertise mérite d'être mieux rémunérée dans ma vie ? »""",

    ('virgo', 3): """# ♃ Jupiter en Vierge
**En une phrase :** Tu communiques avec précision et utilité — tes mots sont choisis, tes analyses sont claires, tes conseils sont pratiques.

## Ton moteur
Jupiter en Vierge en Maison 3 te donne un esprit analytique et une communication détaillée. Tu décomposes les problèmes, tu expliques clairement, tu corriges les erreurs. Cette configuration favorise l'écriture technique, l'enseignement pratique, le conseil.

## Ton défi
Le piège : communiquer de façon trop critique, se perdre dans les détails au détriment du message principal, avoir du mal à exprimer des idées non vérifiables. La communication inclut aussi l'intuition et l'émotion.

## Maison 3 en Vierge
Jupiter amplifie ton attention aux détails dans les échanges. Tu remarques les erreurs, les incohérences. Tes relations avec frères, sœurs et voisins peuvent inclure du service mutuel. Tu apprends par la pratique et l'analyse.

## Micro-rituel du jour (2 min)
- Simplifier un sujet complexe pour quelqu'un qui en a besoin
- Trois respirations en laissant l'esprit se reposer des analyses
- Journal : « Quelle information utile ai-je partagée récemment ? »""",

    ('virgo', 4): """# ♃ Jupiter en Vierge
**En une phrase :** Ton foyer est un espace organisé et fonctionnel — tu crées un chez-toi qui fonctionne bien et prend soin de ses habitants.

## Ton moteur
Jupiter en Vierge en Maison 4 te donne un besoin d'ordre et d'efficacité dans ton espace de vie. Tout a sa place, tout fonctionne, tout est propre et sain. Tu prends soin de ton foyer comme on entretient un organisme vivant.

## Ton défi
Le piège : être trop exigeant sur l'ordre domestique, critiquer les membres de la famille qui ne respectent pas tes standards, avoir du mal à te détendre chez toi. Le foyer a aussi besoin de chaleur et de lâcher-prise.

## Maison 4 en Vierge
Jupiter amplifie ton attention aux détails domestiques. Tu as peut-être grandi dans une famille qui valorisait le travail, la santé, l'amélioration continue. Ton foyer peut inclure un potager, une pharmacie naturelle, un espace de travail bien organisé.

## Micro-rituel du jour (2 min)
- Ranger ou optimiser un coin de ton espace de vie pour le rendre plus fonctionnel
- Trois respirations en acceptant que la perfection domestique n'existe pas
- Journal : « Comment mon chez-moi soutient-il ma santé et mon bien-être ? »""",

    ('virgo', 5): """# ♃ Jupiter en Vierge
**En une phrase :** Tu crées avec méthode et précision — tes œuvres sont soignées, utiles, perfectionnées jusqu'au moindre détail.

## Ton moteur
Jupiter en Vierge en Maison 5 te donne une créativité qui passe par le travail technique et l'amélioration constante. Tu préfères maîtriser ton art plutôt que d'improviser. En amour, tu cherches des partenaires fiables et tu exprimes ton affection par des actes de service.

## Ton défi
Le piège : ne jamais trouver tes créations assez parfaites pour les montrer, critiquer tes partenaires amoureux, avoir du mal à te lâcher dans le jeu et le plaisir. La créativité demande aussi de l'imperfection joyeuse.

## Maison 5 en Vierge
Jupiter amplifie ton attention aux détails dans les domaines du plaisir. Tu peux avoir des hobbies techniques ou artisanaux. Avec les enfants, tu es un parent éducatif et attentif à leur santé.

## Micro-rituel du jour (2 min)
- Permettre à une création d'être imparfaite et la montrer quand même
- Trois respirations en laissant le plaisir exister sans perfection
- Journal : « Comment puis-je m'amuser sans me soucier du résultat ? »""",

    ('virgo', 6): """# ♃ Jupiter en Vierge
**En une phrase :** Tu excelles dans le travail méthodique — ton quotidien est un chef-d'œuvre d'organisation et d'amélioration continue.

## Ton moteur
Jupiter en Vierge en Maison 6 est une position puissante pour le travail et la santé. Tu as un talent naturel pour optimiser les processus, améliorer les systèmes, prendre soin des détails qui font la différence. Les métiers de santé, d'analyse ou de service te conviennent parfaitement.

## Ton défi
Le piège : devenir perfectionniste au point de t'épuiser, critiquer constamment ton travail et celui des autres, négliger ta santé par surmenage. L'efficacité durable inclut aussi le repos.

## Maison 6 en Vierge
Jupiter amplifie naturellement ce domaine. Tu es fait pour le travail consciencieux et le service. Ta santé peut être excellente si tu l'entretiens avec méthode, ou fragile si tu négliges les signaux.

## Micro-rituel du jour (2 min)
- Célébrer une amélioration récente dans ta façon de travailler ou de vivre
- Trois respirations en remerciant ton corps pour son service quotidien
- Journal : « Quelle petite amélioration a fait une vraie différence dans ma vie ? »""",

    ('virgo', 7): """# ♃ Jupiter en Vierge
**En une phrase :** Tes relations sont des partenariats de service mutuel — tu cherches des partenaires fiables avec qui améliorer la vie quotidienne.

## Ton moteur
Jupiter en Vierge en Maison 7 te pousse vers des partenariats pratiques et fonctionnels. Tu attires des personnes compétentes, parfois critiques, souvent dans les métiers de service ou de santé. L'amour passe par les actes concrets plus que par les grandes déclarations.

## Ton défi
Le piège : critiquer ton partenaire au lieu de l'accepter, chercher la perfection relationnelle qui n'existe pas, transformer l'amour en liste de tâches. Les meilleures relations acceptent aussi les imperfections.

## Maison 7 en Vierge
Jupiter amplifie ton besoin de fonctionnalité dans les partenariats. Tu peux t'associer avec des personnes du domaine de la santé ou de l'analyse. Tes contrats sont détaillés et précis.

## Micro-rituel du jour (2 min)
- Exprimer ton appréciation pour quelque chose de concret que fait ton partenaire
- Trois respirations en acceptant les imperfections de l'autre avec bienveillance
- Journal : « Comment mon partenaire me rend-il la vie plus facile au quotidien ? »""",

    ('virgo', 8): """# ♃ Jupiter en Vierge
**En une phrase :** Tu traverses les crises avec méthode — les transformations deviennent des opportunités d'analyse et d'amélioration profonde.

## Ton moteur
Jupiter en Vierge en Maison 8 te donne une capacité à gérer les crises de façon méthodique. Tu analyses ce qui ne fonctionne pas, tu trouves des solutions pratiques, tu reconstruis sur des bases saines. Les ressources partagées bénéficient de ta gestion précise.

## Ton défi
Le piège : intellectualiser les émotions profondes au lieu de les traverser, critiquer ta façon de gérer les crises, avoir du mal à lâcher le contrôle. La transformation demande parfois de laisser le chaos faire son œuvre.

## Maison 8 en Vierge
Jupiter amplifie ta capacité d'analyse dans les domaines profonds. Tu peux avoir un talent pour la recherche, la psychologie, la gestion des héritages. Ta sexualité peut être liée au service ou au perfectionnisme.

## Micro-rituel du jour (2 min)
- Identifier un domaine de ta vie qui a besoin d'une transformation et faire un premier petit pas
- Trois respirations en acceptant que la transformation n'est pas toujours ordonnée
- Journal : « Quelle crise passée m'a appris à mieux gérer les difficultés ? »""",

    ('virgo', 9): """# ♃ Jupiter en Vierge
**En une phrase :** Ta quête de sens passe par l'analyse critique — tu cherches des philosophies qui fonctionnent concrètement et peuvent être vérifiées.

## Ton moteur
Jupiter en Vierge en Maison 9 te donne un rapport analytique aux grandes idées. Tu ne crois pas sur parole, tu vérifies, tu testes, tu compares. Cette configuration favorise les études scientifiques, la recherche, l'enseignement technique.

## Ton défi
Le piège : rejeter les philosophies qui ne sont pas prouvables, manquer de foi ou d'ouverture au mystère, critiquer les systèmes de croyances des autres. La sagesse inclut aussi ce qui ne se mesure pas.

## Maison 9 en Vierge
Jupiter amplifie ton besoin de rigueur dans l'exploration des grandes questions. Tu peux voyager pour apprendre des techniques, étudier des systèmes de santé étrangers. Ton enseignement est pratique et vérifié.

## Micro-rituel du jour (2 min)
- Explorer une idée ou une philosophie nouvelle avec un esprit ouvert mais critique
- Trois respirations en acceptant que certaines vérités dépassent l'analyse
- Journal : « Quelle grande idée a résisté à mon analyse critique ? »""",

    ('virgo', 10): """# ♃ Jupiter en Vierge
**En une phrase :** Ta carrière se construit sur la compétence — tu réussis en étant le meilleur dans les détails qui comptent.

## Ton moteur
Jupiter en Vierge en Maison 10 te pousse vers des professions où la précision et le service sont valorisés. Tu peux exceller dans la santé, l'analyse, l'administration, tout métier qui demande rigueur et amélioration continue.

## Ton défi
Le piège : ne jamais te sentir assez compétent pour le poste, critiquer ta propre réussite, refuser les promotions par modestie excessive. Le succès mérite d'être accepté avec grâce.

## Maison 10 en Vierge
Jupiter amplifie ta réputation de professionnel fiable et précis. On te confie les missions délicates parce qu'on sait que tu gères les détails. Ta carrière peut évoluer lentement mais sûrement.

## Micro-rituel du jour (2 min)
- Identifier une compétence professionnelle que tu pourrais encore améliorer
- Trois respirations en acceptant que tu es déjà suffisamment compétent
- Journal : « Quelle réussite professionnelle mérite d'être célébrée ? »""",

    ('virgo', 11): """# ♃ Jupiter en Vierge
**En une phrase :** Tu contribues aux groupes par ton expertise — tes amitiés sont des collaborations où chacun apporte ses compétences.

## Ton moteur
Jupiter en Vierge en Maison 11 te donne un talent pour améliorer les organisations et les groupes. Tu identifies ce qui ne fonctionne pas, tu proposes des solutions pratiques, tu rends les projets collectifs plus efficaces.

## Ton défi
Le piège : critiquer les amis ou les groupes qui ne correspondent pas à tes standards, avoir du mal à profiter des réunions sans chercher à les améliorer, être le perfectionniste que personne n'a demandé. Les communautés ont aussi besoin de se détendre.

## Maison 11 en Vierge
Jupiter amplifie ton besoin d'utilité dans les groupes. Tu peux attirer des amis dans les domaines de la santé ou de l'analyse. Tes projets humanitaires ont une dimension pratique et mesurable.

## Micro-rituel du jour (2 min)
- Offrir une aide concrète à un ami ou un groupe sans qu'on te le demande
- Trois respirations en acceptant les groupes tels qu'ils sont
- Journal : « Comment mes compétences ont-elles récemment aidé une cause collective ? »""",

    ('virgo', 12): """# ♃ Jupiter en Vierge
**En une phrase :** Tu explores l'invisible avec méthode — ta spiritualité passe par des pratiques concrètes qui améliorent ta vie intérieure.

## Ton moteur
Jupiter en Vierge en Maison 12 crée un pont entre l'analyse et l'invisible. Tu as peut-être un talent pour des pratiques spirituelles qui sont aussi des techniques : yoga, méditation guidée, rituels précis. Ton inconscient peut te livrer ses messages sous forme de listes ou d'analyses.

## Ton défi
Le piège : vouloir contrôler l'inconscient avec des méthodes, critiquer ta progression spirituelle, avoir du mal à lâcher l'analyse pour entrer dans le mystère. Le sacré échappe parfois aux techniques.

## Maison 12 en Vierge
Jupiter amplifie ta quête de pratiques spirituelles efficaces. Tu peux avoir des talents cachés de guérisseur ou d'analyste de l'inconscient. Les retraites qui combinent discipline et lâcher-prise te conviennent particulièrement.

## Micro-rituel du jour (2 min)
- Pratiquer une technique de méditation ou de relaxation avec méthode et lâcher-prise
- Trois respirations en acceptant que l'invisible ne se maîtrise pas
- Journal : « Quelle pratique spirituelle m'aide à me connecter au mystère ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_VIRGO.items():
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
