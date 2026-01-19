#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Cancer en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_CANCER = {
    ('cancer', 1): """# ♃ Jupiter en Cancer
**En une phrase :** Tu incarnes une présence protectrice et chaleureuse qui fait que les autres se sentent immédiatement accueillis.

## Ton moteur
Jupiter en Cancer en Maison 1 te donne une aura de bienveillance maternelle (quel que soit ton genre). Tu prends soin des autres naturellement, tu crées des espaces de sécurité émotionnelle partout où tu vas. Cette configuration amplifie ta sensibilité et ton intuition.

## Ton défi
Le piège : absorber les émotions des autres au point de te perdre, utiliser le soin pour contrôler, avoir du mal à recevoir quand tu donnes si facilement. L'expansion véritable inclut aussi de te nourrir toi-même.

## Maison 1 en Cancer
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un de maternel, de rassurant, de profondément humain. Ton corps reflète tes émotions — tu changes selon ton état intérieur.

## Micro-rituel du jour (2 min)
- Offrir une attention bienveillante à quelqu'un qui en a besoin aujourd'hui
- Trois respirations en posant une main sur ton cœur, sentir sa chaleur
- Journal : « Comment ai-je nourri quelqu'un aujourd'hui ? Et moi-même ? »""",

    ('cancer', 2): """# ♃ Jupiter en Cancer
**En une phrase :** Tu construis ta sécurité financière pour protéger ceux que tu aimes — l'abondance est un nid que tu tisses patiemment.

## Ton moteur
Jupiter en Cancer en Maison 2 te donne un besoin profond de sécurité matérielle liée au foyer et à la famille. Tu économises pour un chez-toi, tu investis dans ce qui protège les tiens. L'argent est un cocon que tu construis avec amour.

## Ton défi
Le piège : accumuler par peur de manquer plutôt que par abondance, confondre valeur personnelle et capacité à nourrir les autres, avoir du mal à dépenser pour toi-même. La vraie sécurité vient aussi de l'intérieur.

## Maison 2 en Cancer
Jupiter amplifie ton rapport émotionnel à l'argent. Tes revenus peuvent fluctuer selon tes états d'âme. Tu as un talent pour les métiers du soin, de l'alimentation, de l'immobilier, tout ce qui touche au foyer et à la protection.

## Micro-rituel du jour (2 min)
- Identifier un achat récent qui nourrit vraiment ta sécurité émotionnelle
- Trois respirations en visualisant ton abondance comme un lac calme et profond
- Journal : « Qu'est-ce qui me fait me sentir vraiment en sécurité financièrement ? »""",

    ('cancer', 3): """# ♃ Jupiter en Cancer
**En une phrase :** Tu communiques avec le cœur — tes mots portent une chaleur qui touche les gens au-delà de leur sens littéral.

## Ton moteur
Jupiter en Cancer en Maison 3 te donne une communication teintée d'émotion et d'intuition. Tu captes ce qui n'est pas dit, tu devines les besoins derrière les mots. Cette configuration favorise l'écriture intime, le conseil, tout métier où l'empathie enrichit l'échange.

## Ton défi
Le piège : communiquer seulement quand tu te sens en sécurité, te refermer dès que l'atmosphère devient froide, confondre ce que tu ressens et ce que l'autre pense. La communication demande parfois de traverser l'inconfort.

## Maison 3 en Cancer
Jupiter amplifie tes liens avec ton entourage proche. Frères, sœurs, voisins sont comme une famille élargie. Tu apprends mieux dans un environnement chaleureux et sécurisant. Les déplacements courts te ramènent souvent vers des lieux familiers.

## Micro-rituel du jour (2 min)
- Envoyer un message chaleureux à quelqu'un de ton entourage proche
- Trois respirations en laissant la tendresse colorer tes pensées
- Journal : « Quelle conversation récente m'a touché émotionnellement ? »""",

    ('cancer', 4): """# ♃ Jupiter en Cancer
**En une phrase :** Ton foyer est un sanctuaire sacré — tu crées un chez-toi qui accueille, nourrit et régénère tous ceux qui y entrent.

## Ton moteur
Jupiter en Cancer en Maison 4 amplifie au maximum ton besoin d'un foyer nourrissant. Tu as probablement un grand appartement ou une maison qui peut accueillir beaucoup de monde. La cuisine, les traditions familiales, l'héritage émotionnel sont centraux dans ta vie.

## Ton défi
Le piège : t'enfermer dans le cocon familial au point de refuser le monde extérieur, étouffer les tiens par excès de protection, avoir du mal à quitter le nid ou à laisser les autres le faire. Le foyer est une base, pas une prison.

## Maison 4 en Cancer
Jupiter est ici dans sa position d'exaltation traditionnelle. Tu as peut-être hérité d'une grande maison ou d'une tradition familiale riche. Ton sens de la famille est profond, incluant les ancêtres et les générations futures.

## Micro-rituel du jour (2 min)
- Cuisiner ou partager un plat qui évoque un souvenir familial heureux
- Trois respirations en visualisant ton foyer comme un cœur qui bat
- Journal : « Quel héritage émotionnel de ma famille est-ce que je chéris le plus ? »""",

    ('cancer', 5): """# ♃ Jupiter en Cancer
**En une phrase :** Tu crées avec ton cœur — tes œuvres, tes amours et ta joie ont une profondeur émotionnelle qui touche les autres intimement.

## Ton moteur
Jupiter en Cancer en Maison 5 te donne une créativité qui vient des profondeurs émotionnelles. Tu crées pour exprimer ce que tu ressens, pour guérir, pour connecter. En amour, tu cherches une intimité profonde, pas des aventures superficielles.

## Ton défi
Le piège : te refermer si tes créations ne sont pas accueillies avec chaleur, aimer avec possessivité, utiliser les enfants ou les projets pour combler un vide émotionnel. La joie véritable accepte aussi la légèreté.

## Maison 5 en Cancer
Jupiter amplifie ton désir d'enfants ou de projets qui te prolongent émotionnellement. Tu es un parent ou un créateur profondément investi. Les plaisirs simples et familiaux te nourrissent plus que les sorties mondaines.

## Micro-rituel du jour (2 min)
- Créer quelque chose de petit qui exprime ton état émotionnel actuel
- Trois respirations en connectant ton cœur à ta créativité
- Journal : « Quelle émotion ai-je envie d'exprimer à travers une création ? »""",

    ('cancer', 6): """# ♃ Jupiter en Cancer
**En une phrase :** Tu travailles avec le cœur — ton quotidien est nourri par le soin que tu apportes aux autres et à toi-même.

## Ton moteur
Jupiter en Cancer en Maison 6 te donne un besoin de travailler dans un environnement chaleureux et bienveillant. Tu prends soin de tes collègues, tu crées une atmosphère familiale au bureau. Cette configuration favorise les métiers du soin, de la santé, de l'alimentation.

## Ton défi
Le piège : t'épuiser à prendre soin des autres dans ton travail, avoir du mal à poser des limites professionnelles, négliger ta propre santé en te concentrant sur celle des autres. Le service durable commence par se nourrir soi-même.

## Maison 6 en Cancer
Jupiter amplifie ton rapport émotionnel au travail et à la santé. Tu travailles mieux quand tu te sens en sécurité. Ta digestion et ton système émotionnel sont liés — le stress affecte ton ventre.

## Micro-rituel du jour (2 min)
- Apporter un geste de soin à ton espace de travail ou à un collègue
- Trois respirations en posant une main sur ton ventre, respirer dans cette zone
- Journal : « Comment puis-je mieux prendre soin de moi au travail ? »""",

    ('cancer', 7): """# ♃ Jupiter en Cancer
**En une phrase :** Tes relations sont des foyers émotionnels — tu cherches des partenaires avec qui construire un nid d'intimité et de sécurité mutuelle.

## Ton moteur
Jupiter en Cancer en Maison 7 te pousse vers des partenariats profondément nourissants. Tu as besoin de te sentir en famille avec ton partenaire, de créer ensemble un cocon sécurisant. Tu attires des personnes maternantes ou qui ont besoin de protection.

## Ton défi
Le piège : te fusionner avec l'autre au point de perdre ton identité, chercher un parent dans un partenaire, étouffer l'autre par trop de sollicitude. Les meilleures relations laissent aussi de l'espace.

## Maison 7 en Cancer
Jupiter amplifie ton besoin de sécurité émotionnelle dans les partenariats. Tu peux te marier pour créer une famille ou t'associer avec des personnes qui partagent tes valeurs de protection et de soin.

## Micro-rituel du jour (2 min)
- Exprimer à un partenaire ce qui te fait te sentir en sécurité dans la relation
- Trois respirations en visualisant votre lien comme un foyer partagé
- Journal : « Comment mon partenaire me nourrit-il émotionnellement ? »""",

    ('cancer', 8): """# ♃ Jupiter en Cancer
**En une phrase :** Tu traverses les crises en t'appuyant sur tes racines — les pertes deviennent des occasions de retrouver ce qui compte vraiment.

## Ton moteur
Jupiter en Cancer en Maison 8 te donne une capacité à transformer la douleur en croissance émotionnelle. Tu as une intuition profonde pour les héritages, les legs, tout ce qui passe d'une génération à l'autre. Les ressources partagées peuvent venir de la famille.

## Ton défi
Le piège : t'accrocher aux liens familiaux toxiques, utiliser l'intimité pour contrôler, avoir du mal à lâcher les deuils qui te relient aux disparus. La vraie transformation demande parfois de couper les cordons.

## Maison 8 en Cancer
Jupiter amplifie ton rapport émotionnel aux crises et aux transformations. Tu peux hériter de la maison familiale ou de biens liés aux racines. Ta sexualité est profondément liée au besoin de sécurité et d'intimité.

## Micro-rituel du jour (2 min)
- Identifier un héritage émotionnel familial que tu veux transformer ou honorer
- Trois respirations en visualisant des racines qui se régénèrent après une coupe
- Journal : « Quel deuil ou quelle transformation m'a rapproché de mes vraies valeurs ? »""",

    ('cancer', 9): """# ♃ Jupiter en Cancer
**En une phrase :** Ta quête de sens passe par le cœur — tu cherches une philosophie qui nourrit l'âme et crée un sentiment d'appartenance universelle.

## Ton moteur
Jupiter en Cancer en Maison 9 te donne une spiritualité basée sur le sentiment d'être chez soi dans l'univers. Tu peux trouver du sacré dans les traditions familiales, les rituels ancestraux, les lieux qui évoquent un chez-soi cosmique. Les voyages te ramènent souvent à tes racines.

## Ton défi
Le piège : idéaliser une culture d'origine au détriment des autres, chercher une mère dans chaque enseignant spirituel, avoir du mal à t'aventurer loin de ce qui est familier. L'expansion véritable inclut aussi l'inconnu.

## Maison 9 en Cancer
Jupiter amplifie ton besoin de trouver un foyer philosophique ou spirituel. Tu peux étudier l'histoire familiale, la généalogie, les traditions de guérison. L'étranger t'attire quand il offre une chaleur humaine authentique.

## Micro-rituel du jour (2 min)
- Explorer une tradition spirituelle ou culturelle qui évoque un sentiment de foyer
- Trois respirations en visualisant l'univers entier comme ta maison
- Journal : « Quelle croyance me fait me sentir en sécurité dans le monde ? »""",

    ('cancer', 10): """# ♃ Jupiter en Cancer
**En une phrase :** Ta carrière est une extension de ta mission de prendre soin — tu réussis en nourrissant les autres et en créant des espaces sécurisants.

## Ton moteur
Jupiter en Cancer en Maison 10 te pousse vers des professions liées au soin, à la protection, à la création de foyers. Tu peux exceller dans l'immobilier, la restauration, les métiers de la santé, l'éducation de la petite enfance, tout ce qui nourrit et protège.

## Ton défi
Le piège : confondre carrière et famille au point de négliger ta vie privée, jouer un rôle parental avec tes subordonnés, avoir du mal à recevoir de la reconnaissance sans donner en retour. Le succès mérite d'être savouré.

## Maison 10 en Cancer
Jupiter amplifie ta réputation de personne bienveillante et protectrice. On te confie des responsabilités parce qu'on sent que tu prends soin. Ta carrière peut être liée à l'histoire familiale ou à un héritage professionnel.

## Micro-rituel du jour (2 min)
- Identifier comment ton travail nourrit ou protège les autres
- Trois respirations en visualisant ta carrière comme un grand foyer que tu crées
- Journal : « Comment ma mission professionnelle prolonge-t-elle mes valeurs familiales ? »""",

    ('cancer', 11): """# ♃ Jupiter en Cancer
**En une phrase :** Tu crées des communautés comme des familles — tes amitiés et tes groupes sont des espaces de chaleur et de soutien mutuel.

## Ton moteur
Jupiter en Cancer en Maison 11 te donne un talent pour transformer les groupes en familles choisies. Tu prends soin de tes amis comme de tes proches, tu crées des traditions communes, tu offres un sentiment d'appartenance à ceux qui se sentent seuls.

## Ton défi
Le piège : attendre des amis ce qu'on attend d'une famille, être déçu quand les groupes ne répondent pas à tes besoins émotionnels, avoir du mal à accepter la distance que certaines amitiés demandent. Les communautés saines ont aussi des limites.

## Maison 11 en Cancer
Jupiter amplifie ton besoin d'appartenance communautaire. Tu peux créer ou rejoindre des groupes qui fonctionnent comme des familles. Tes projets humanitaires touchent souvent aux thèmes de l'enfance, du foyer, de la protection des vulnérables.

## Micro-rituel du jour (2 min)
- Organiser ou participer à un moment de partage chaleureux avec un groupe
- Trois respirations en visualisant ta communauté comme un cercle de protection
- Journal : « Quelle amitié me fait me sentir vraiment appartenir à une famille choisie ? »""",

    ('cancer', 12): """# ♃ Jupiter en Cancer
**En une phrase :** Tu trouves le divin dans l'intime — ta spiritualité passe par le sentiment de retour à un foyer originel, une source maternelle universelle.

## Ton moteur
Jupiter en Cancer en Maison 12 crée un pont entre ton besoin de sécurité et l'infini. Tu as peut-être des souvenirs de vies passées ou un sentiment de nostalgie pour un lieu que tu n'as jamais connu. Ton inconscient est riche d'héritages émotionnels à explorer.

## Ton défi
Le piège : utiliser la spiritualité pour fuir le monde réel, chercher une mère cosmique au lieu d'assumer ta propre maturité, te perdre dans les rêves du passé. L'éveil véritable inclut aussi le présent.

## Maison 12 en Cancer
Jupiter amplifie ta connexion au monde invisible à travers les émotions. Tu peux avoir des rêves prophétiques liés à la famille, des intuitions sur les ancêtres, un accès aux mémoires collectives. Les retraites en lien avec l'eau te régénèrent particulièrement.

## Micro-rituel du jour (2 min)
- Méditer sur un souvenir d'enfance qui évoque un sentiment de sécurité absolue
- Trois respirations en visualisant un océan maternel qui te berce
- Journal : « Quel message de mon inconscient évoque un sentiment de retour au foyer ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_CANCER.items():
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
