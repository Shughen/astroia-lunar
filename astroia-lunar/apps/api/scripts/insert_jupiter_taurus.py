#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Taurus en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_TAURUS = {
    ('taurus', 1): """# ♃ Jupiter en Taureau
**En une phrase :** Tu incarnes une présence rassurante et généreuse qui inspire confiance dès le premier regard.

## Ton moteur
Jupiter en Taureau en Maison 1 te donne une aura de stabilité et d'abondance. Tu occupes l'espace avec calme, sans forcer. Cette configuration amplifie ton rapport au corps : tu as besoin de te sentir ancré, nourri, en contact avec les plaisirs sensoriels. Ta présence physique communique fiabilité et générosité.

## Ton défi
Le piège : t'installer dans le confort au point de résister à tout changement, confondre stabilité et immobilisme, accumuler sans vraiment profiter. L'abondance véritable circule.

## Maison 1 en Taureau
Jupiter amplifie ta capacité à attirer les ressources. On te perçoit comme quelqu'un de solide, de concret, sur qui on peut compter. Ton corps a besoin de qualité — bonne nourriture, beaux vêtements, environnement agréable.

## Micro-rituel du jour (2 min)
- Savourer lentement un aliment ou une boisson de qualité, en pleine conscience
- Trois respirations profondes en sentant tes pieds ancrés au sol
- Journal : « Qu'est-ce qui me procure un sentiment d'abondance aujourd'hui ? »""",

    ('taurus', 2): """# ♃ Jupiter en Taureau
**En une phrase :** Tu bâtis ta sécurité financière avec patience et méthode — pour toi, l'abondance se construit pierre après pierre.

## Ton moteur
Jupiter en Taureau en Maison 2 amplifie ton talent pour accumuler des ressources de manière durable. Tu n'es pas pressé : tu préfères les investissements sûrs aux paris risqués. Cette configuration te donne un flair pour reconnaître la vraie valeur des choses et des personnes.

## Ton défi
Le piège : devenir trop attaché aux possessions, définir ta valeur par ce que tu possèdes, hésiter à partager par peur de manquer. La vraie sécurité vient de ta capacité à générer, pas à accumuler.

## Maison 2 en Taureau
Jupiter amplifie naturellement la maison qu'il visite. Ici, c'est le domaine de l'argent et des valeurs. Tu as un don pour transformer le temps et la patience en prospérité tangible. Les revenus peuvent venir de l'immobilier, de l'art, ou de tout ce qui a une valeur durable.

## Micro-rituel du jour (2 min)
- Faire le point sur une ressource que tu as construite patiemment et la célébrer
- Trois respirations en visualisant ta sécurité comme un sol fertile sous tes pieds
- Journal : « Quelle valeur ai-je cultivée récemment qui portera ses fruits plus tard ? »""",

    ('taurus', 3): """# ♃ Jupiter en Taureau
**En une phrase :** Tu communiques avec une voix posée et des mots concrets — tes idées ont du poids parce qu'elles s'appuient sur le réel.

## Ton moteur
Jupiter en Taureau en Maison 3 te donne une pensée méthodique et un apprentissage lent mais profond. Tu préfères maîtriser un sujet à fond plutôt que de survoler plusieurs. Ta communication est simple, directe, ancrée dans l'expérience pratique.

## Ton défi
Le piège : rejeter les idées abstraites ou les théories non prouvées, t'entêter dans tes opinions, communiquer trop lentement pour des interlocuteurs plus rapides. La richesse intellectuelle vient aussi de la flexibilité.

## Maison 3 en Taureau
Jupiter amplifie ta façon d'apprendre et de transmettre. Tu retiens mieux ce que tu expérimentes avec tes sens. Tes relations avec frères, sœurs et voisins peuvent être source de sécurité et de ressources pratiques.

## Micro-rituel du jour (2 min)
- Apprendre quelque chose de nouveau en le pratiquant plutôt qu'en le lisant
- Trois respirations en te concentrant sur le poids et la solidité de tes mots
- Journal : « Quelle idée concrète ai-je partagée ou reçue récemment ? »""",

    ('taurus', 4): """# ♃ Jupiter en Taureau
**En une phrase :** Ton foyer est un sanctuaire d'abondance — tu crées un chez-toi qui nourrit tous les sens et accueille généreusement.

## Ton moteur
Jupiter en Taureau en Maison 4 te pousse à construire un nid confortable et durable. Tu investis dans ton habitat, tu cultives peut-être un jardin, tu accumules des objets beaux et utiles. Ta maison est ton ancrage, le socle à partir duquel tu peux t'ouvrir au monde.

## Ton défi
Le piège : t'attacher excessivement à un lieu ou des biens familiaux, refuser de déménager même quand c'est nécessaire, confondre confort matériel et sécurité émotionnelle. Les racines les plus solides savent aussi se transplanter.

## Maison 4 en Taureau
Jupiter amplifie ton besoin de stabilité domestique. Ta famille t'a peut-être transmis un patrimoine, des terres, ou simplement le goût des bonnes choses. Tu as le don de créer une atmosphère accueillante où les autres se sentent nourris.

## Micro-rituel du jour (2 min)
- Ajouter un élément de beauté ou de confort à ton espace de vie
- Trois respirations en te connectant aux murs qui t'entourent, à leur solidité
- Journal : « Qu'est-ce qui rend mon foyer vraiment nourrissant ? »""",

    ('taurus', 5): """# ♃ Jupiter en Taureau
**En une phrase :** Tu savoures les plaisirs de la vie avec une générosité sensuelle — tes créations sont belles, durables et ancrées dans la matière.

## Ton moteur
Jupiter en Taureau en Maison 5 amplifie ta capacité à profiter de la vie. Tu as un talent pour transformer les plaisirs simples en moments d'abondance. Ta créativité passe par les mains, les sens, le contact avec la matière. En amour, tu es fidèle et généreux une fois engagé.

## Ton défi
Le piège : t'installer dans une routine de plaisirs au point de perdre la spontanéité, posséder plutôt qu'aimer, confondre confort et passion. La joie de vivre demande parfois de sortir de ta zone de confort.

## Maison 5 en Taureau
Jupiter amplifie ton magnétisme sensuel. Tu attires des partenaires qui apprécient la stabilité et les plaisirs concrets. Avec les enfants ou dans tes projets créatifs, tu transmets le goût de la qualité et de la patience.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir sensoriel de qualité : un bon repas, une texture agréable, une belle musique
- Trois respirations en laissant le plaisir infuser tout ton corps
- Journal : « Quel plaisir simple m'a nourri profondément récemment ? »""",

    ('taurus', 6): """# ♃ Jupiter en Taureau
**En une phrase :** Tu travailles avec méthode et constance — ta productivité vient de rythmes réguliers plutôt que d'efforts intenses.

## Ton moteur
Jupiter en Taureau en Maison 6 te donne un talent pour le travail bien fait et durable. Tu préfères avancer à ton rythme, sans stress, en produisant de la qualité. Cette configuration favorise les métiers manuels, artisanaux, ou tout ce qui demande patience et savoir-faire.

## Ton défi
Le piège : résister aux changements de méthode même quand ils sont nécessaires, t'enliser dans des routines qui ne servent plus, négliger ta santé par excès de gourmandise. L'efficacité durable demande aussi de l'adaptation.

## Maison 6 en Taureau
Jupiter amplifie ton rapport au corps et au quotidien. Tu as besoin d'un environnement de travail agréable et stable. Ta santé bénéficie d'une alimentation de qualité et d'exercices doux mais réguliers.

## Micro-rituel du jour (2 min)
- Améliorer un aspect de ton espace de travail pour le rendre plus confortable
- Trois respirations en remerciant ton corps pour sa fiabilité quotidienne
- Journal : « Quelle routine me soutient le mieux dans mon travail actuel ? »""",

    ('taurus', 7): """# ♃ Jupiter en Taureau
**En une phrase :** Tu construis des partenariats solides et durables — tes relations sont des investissements à long terme basés sur la confiance mutuelle.

## Ton moteur
Jupiter en Taureau en Maison 7 te pousse vers des relations stables et nourrissantes. Tu ne t'engages pas à la légère, mais une fois lié, tu es d'une fidélité remarquable. Tu attires des partenaires qui apportent sécurité, ressources ou un ancrage que tu apprécies.

## Ton défi
Le piège : rester dans une relation par confort plutôt que par amour, confondre sécurité matérielle et vraie compatibilité, posséder l'autre plutôt que le partager. Les meilleures relations permettent aussi à chacun de grandir.

## Maison 7 en Taureau
Jupiter amplifie ton besoin de stabilité relationnelle. Tu peux attirer des partenaires plus riches ou plus établis que toi. Les associations professionnelles basées sur des valeurs communes peuvent être particulièrement fructueuses.

## Micro-rituel du jour (2 min)
- Exprimer ta gratitude à un partenaire pour quelque chose de concret qu'il apporte
- Trois respirations en visualisant ta relation comme un arbre aux racines profondes
- Journal : « Comment ma relation actuelle me nourrit-elle concrètement ? »""",

    ('taurus', 8): """# ♃ Jupiter en Taureau
**En une phrase :** Tu traverses les crises avec une résilience tranquille — les pertes deviennent des terrains fertiles pour une nouvelle abondance.

## Ton moteur
Jupiter en Taureau en Maison 8 te donne une capacité remarquable à transformer les pertes en gains. Tu as un flair pour les ressources partagées : héritages, investissements communs, gestion des biens d'autrui. Cette configuration peut apporter des gains financiers par le mariage ou les partenariats.

## Ton défi
Le piège : t'accrocher aux choses ou aux personnes au-delà de leur temps, résister aux transformations nécessaires par attachement, confondre sécurité et contrôle. La vraie résilience accepte les cycles de mort et renaissance.

## Maison 8 en Taureau
Jupiter amplifie les ressources qui viennent des autres. Tu peux hériter de biens tangibles ou bénéficier de la générosité de partenaires. Ta sexualité est profonde, sensorielle, et peut être une source de régénération.

## Micro-rituel du jour (2 min)
- Identifier quelque chose que tu dois laisser partir pour faire place au nouveau
- Trois respirations en visualisant une transformation douce mais profonde
- Journal : « Quelle perte passée s'est finalement révélée être un cadeau ? »""",

    ('taurus', 9): """# ♃ Jupiter en Taureau
**En une phrase :** Ta philosophie de vie est ancrée dans le réel — tu crois ce que tu peux toucher, goûter, expérimenter directement.

## Ton moteur
Jupiter en Taureau en Maison 9 te pousse à explorer le monde à travers les sens. Tu préfères les voyages qui te font découvrir des cuisines, des paysages, des artisanats locaux. Ta spiritualité est terreà-terre : tu crois en ce qui fonctionne pratiquement.

## Ton défi
Le piège : rejeter les philosophies abstraites sans les explorer, limiter ta vision du monde au tangible, voyager pour consommer plutôt que pour te transformer. L'expansion véritable inclut aussi l'invisible.

## Maison 9 en Taureau
Jupiter amplifie ton rapport à l'étranger et aux grandes idées. Les études supérieures peuvent mener à des domaines pratiques : agronomie, finance, arts appliqués. Tu pourrais enseigner ou publier sur des sujets concrets.

## Micro-rituel du jour (2 min)
- Explorer une tradition culinaire ou artisanale d'une autre culture
- Trois respirations en visualisant tes pieds posés sur des terres lointaines
- Journal : « Quelle expérience concrète a récemment élargi ma vision du monde ? »""",

    ('taurus', 10): """# ♃ Jupiter en Taureau
**En une phrase :** Ta carrière se construit avec patience et méthode — tu vises une réussite durable plutôt qu'une ascension fulgurante.

## Ton moteur
Jupiter en Taureau en Maison 10 te donne une ambition tranquille mais tenace. Tu ne cours pas après les promotions : tu les mérites par un travail de qualité constant. Cette configuration favorise les carrières liées à la finance, l'immobilier, l'art, ou tout domaine où la valeur se construit dans le temps.

## Ton défi
Le piège : avancer trop lentement par excès de prudence, manquer des opportunités par attachement au confort actuel, confondre stabilité professionnelle et immobilisme. Le sommet demande parfois de prendre des risques.

## Maison 10 en Taureau
Jupiter amplifie ta réputation professionnelle. On te voit comme quelqu'un de fiable, de compétent, qui ne promet pas ce qu'il ne peut pas tenir. Ta réussite peut venir tardivement mais durer longtemps.

## Micro-rituel du jour (2 min)
- Identifier un projet professionnel que tu construis avec patience et mesurer son avancement
- Trois respirations en visualisant ta carrière comme un chêne qui grandit lentement
- Journal : « Quel investissement professionnel passé porte ses fruits aujourd'hui ? »""",

    ('taurus', 11): """# ♃ Jupiter en Taureau
**En une phrase :** Tu crées des réseaux solides et durables — tes amitiés sont des investissements à long terme qui portent leurs fruits avec le temps.

## Ton moteur
Jupiter en Taureau en Maison 11 te pousse vers des amitiés stables et nourrissantes. Tu préfères quelques amis fidèles à une multitude de contacts superficiels. Tes projets collectifs sont concrets, réalisables, orientés vers des résultats tangibles.

## Ton défi
Le piège : résister aux nouveaux membres qui bousculent tes habitudes, préférer la stabilité du groupe à son évolution, confondre réseau et cercle fermé. Les meilleures communautés savent s'ouvrir et se renouveler.

## Maison 11 en Taureau
Jupiter amplifie ton influence dans les groupes. Tu peux attirer des amis plus aisés ou des associations qui gèrent des ressources. Tes projets humanitaires ont une dimension pratique : tu veux des résultats concrets.

## Micro-rituel du jour (2 min)
- Entretenir une amitié de longue date par un geste simple mais sincère
- Trois respirations en visualisant ton réseau comme un jardin bien entretenu
- Journal : « Quelle amitié durable m'apporte actuellement le plus ? »""",

    ('taurus', 12): """# ♃ Jupiter en Taureau
**En une phrase :** Tu trouves la paix intérieure dans les plaisirs simples — ta spiritualité passe par le corps et les sens plutôt que par l'abstraction.

## Ton moteur
Jupiter en Taureau en Maison 12 crée un pont entre le monde matériel et l'invisible. Tu as une foi tranquille, non dogmatique, ancrée dans l'expérience sensorielle du sacré. La nature, l'art, la musique peuvent être tes voies de méditation.

## Ton défi
Le piège : utiliser les plaisirs matériels pour fuir les questions spirituelles, t'attacher aux consolations sensorielles au lieu d'affronter l'inconscient, confondre confort et paix intérieure. Le lâcher-prise demande parfois de renoncer au tangible.

## Maison 12 en Taureau
Jupiter amplifie ta connexion au mystère à travers les sens. Tu peux avoir des expériences spirituelles pendant un massage, une dégustation consciente, ou une marche en forêt. Tes rêves peuvent contenir des messages sur l'abondance et la sécurité.

## Micro-rituel du jour (2 min)
- Pratiquer une méditation sensorielle : toucher, goûter ou écouter quelque chose en pleine conscience
- Trois respirations en laissant ton corps devenir un temple
- Journal : « Quel plaisir simple m'a récemment connecté à quelque chose de plus grand ? »""",
}

async def insert_interpretations():
    """Insère les interprétations Jupiter/Taurus en base."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_TAURUS.items():
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
