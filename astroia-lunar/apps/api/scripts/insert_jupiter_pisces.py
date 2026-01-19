#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Pisces en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_PISCES = {
    ('pisces', 1): """# ♃ Jupiter en Poissons
**En une phrase :** Tu incarnes une présence fluide et compassionnelle qui dissout les frontières et crée des ponts entre les mondes.

## Ton moteur
Jupiter en Poissons en Maison 1 te donne une aura de mystère et de sensibilité. Tu absorbes l'atmosphère autour de toi, tu perçois ce qui est invisible aux autres. Cette configuration amplifie ton empathie et ta connexion au transcendant.

## Ton défi
Le piège : te perdre dans les émotions des autres, avoir du mal à définir tes limites, fuir la réalité concrète. La vraie compassion sait aussi se protéger.

## Maison 1 en Poissons
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un de sensible, de rêveur, de profondément humain. Ton corps reflète ta fluidité — gestuelle douce, regard qui semble voir au-delà.

## Micro-rituel du jour (2 min)
- Identifier une façon dont ta sensibilité t'a servi aujourd'hui
- Trois respirations en visualisant des limites douces mais claires autour de toi
- Journal : « Comment ma compassion a-t-elle touché quelqu'un récemment ? »""",

    ('pisces', 2): """# ♃ Jupiter en Poissons
**En une phrase :** Tu développes tes ressources de façon intuitive — ta valeur réside dans ta capacité à percevoir des possibilités invisibles aux autres.

## Ton moteur
Jupiter en Poissons en Maison 2 te donne un rapport fluide et intuitif à l'argent. Tu peux recevoir de façon inattendue, attirer l'abondance par ta foi plutôt que par tes calculs. Les métiers créatifs, de soin ou spirituels peuvent être lucratifs.

## Ton défi
Le piège : avoir un rapport flou à l'argent, être trop généreux au point de te démunir, confondre abondance spirituelle et matérielle. La vraie prospérité demande aussi de l'attention au concret.

## Maison 2 en Poissons
Jupiter amplifie ton rapport intuitif à l'argent. Tes revenus peuvent fluctuer de façon imprévisible. Tes valeurs sont liées à la compassion, la créativité, la connexion au transcendant.

## Micro-rituel du jour (2 min)
- Identifier une ressource que tu as reçue de façon inattendue et remercier
- Trois respirations en faisant confiance à l'abondance de l'univers
- Journal : « Comment ma foi a-t-elle attiré des ressources dans ma vie ? »""",

    ('pisces', 3): """# ♃ Jupiter en Poissons
**En une phrase :** Tu communiques avec poésie et intuition — tes mots créent des ponts vers l'invisible et touchent les cœurs au-delà de la logique.

## Ton moteur
Jupiter en Poissons en Maison 3 te donne une communication imagée et intuitive. Tu parles en métaphores, tu captes l'ambiance derrière les mots. Cette configuration favorise l'écriture poétique, la communication artistique, le conseil intuitif.

## Ton défi
Le piège : communiquer de façon trop vague, avoir du mal à être précis et factuel, confondre impression et information. La vraie communication sait aussi être concrète.

## Maison 3 en Poissons
Jupiter amplifie ta sensibilité dans les échanges. Tu perçois ce qui n'est pas dit. Tes relations avec frères, sœurs et voisins peuvent inclure des liens psychiques ou des sacrifices mutuels.

## Micro-rituel du jour (2 min)
- Partager quelque chose de façon poétique ou imagée avec quelqu'un
- Trois respirations en écoutant l'invisible dans une conversation
- Journal : « Quel non-dit ai-je perçu récemment dans un échange ? »""",

    ('pisces', 4): """# ♃ Jupiter en Poissons
**En une phrase :** Ton foyer est un sanctuaire de paix — tu crées un chez-toi qui nourrit l'âme et offre refuge à ceux qui en ont besoin.

## Ton moteur
Jupiter en Poissons en Maison 4 te donne un rapport profondément émotionnel et spirituel à ton espace de vie. Ton foyer est un lieu de ressourcement, de méditation, d'accueil inconditionnel. Tu peux avoir des liens psychiques avec ta famille.

## Ton défi
Le piège : absorber les problèmes émotionnels de ta famille, avoir du mal à établir des limites chez toi, fuir dans le rêve pour éviter les difficultés domestiques. Le vrai foyer a aussi besoin de structure.

## Maison 4 en Poissons
Jupiter amplifie la dimension spirituelle de ta vie familiale. Tu as peut-être grandi dans une famille aux liens subtils ou une atmosphère floue. Ton foyer peut inclure une dimension de soin, d'art ou de méditation.

## Micro-rituel du jour (2 min)
- Créer un moment de paix et de beauté dans ton espace de vie
- Trois respirations en visualisant ton foyer comme un temple de ressourcement
- Journal : « Comment mon chez-moi nourrit-il mon âme ? »""",

    ('pisces', 5): """# ♃ Jupiter en Poissons
**En une phrase :** Tu crées avec l'âme — tes œuvres, tes amours et tes joies sont des expressions de l'invisible qui touchent profondément ceux qui les reçoivent.

## Ton moteur
Jupiter en Poissons en Maison 5 te donne une créativité qui vient de l'au-delà du conscient. Tu ne crées pas avec ta tête mais avec ton âme. En amour, tu cherches une fusion mystique, une connexion qui transcende l'ordinaire.

## Ton défi
Le piège : idéaliser les partenaires amoureux au point d'être déçu, fuir dans les rêves créatifs plutôt que de concrétiser, confondre inspiration et accomplissement. La vraie créativité demande aussi de la discipline.

## Maison 5 en Poissons
Jupiter amplifie la dimension transcendante de tes plaisirs. Tu peux avoir des expériences amoureuses ou créatives qui te connectent à quelque chose de plus grand. L'art, la musique, la danse sont des voies naturelles d'expression.

## Micro-rituel du jour (2 min)
- Créer quelque chose en laissant l'inspiration venir sans contrôle
- Trois respirations en ouvrant un canal vers l'invisible créatif
- Journal : « Quelle création m'a récemment connecté à quelque chose de plus grand ? »""",

    ('pisces', 6): """# ♃ Jupiter en Poissons
**En une phrase :** Tu travailles avec compassion et intuition — ton quotidien est orienté vers le service aux autres et la guérison.

## Ton moteur
Jupiter en Poissons en Maison 6 te pousse vers des métiers de soin, de guérison ou de service compassionnel. Tu perçois intuitivement ce dont les autres ont besoin. Cette configuration favorise les métiers de santé holistique, d'accompagnement, d'art-thérapie.

## Ton défi
Le piège : absorber les souffrances de ceux que tu aides, avoir du mal à mettre des limites dans le service, négliger ta propre santé pour celle des autres. Le vrai service durable commence par prendre soin de soi.

## Maison 6 en Poissons
Jupiter amplifie ta sensibilité dans le travail quotidien. Tu travailles mieux dans des environnements calmes et bienveillants. Ta santé est sensible aux atmosphères et peut bénéficier d'approches holistiques.

## Micro-rituel du jour (2 min)
- Apporter un geste de soin ou de compassion à quelqu'un au travail
- Trois respirations en te reconnectant à ton propre corps et ses besoins
- Journal : « Comment puis-je servir les autres tout en prenant soin de moi ? »""",

    ('pisces', 7): """# ♃ Jupiter en Poissons
**En une phrase :** Tes relations sont des fusions d'âmes — tu cherches des partenaires avec qui transcender les limites de l'ego et toucher l'infini.

## Ton moteur
Jupiter en Poissons en Maison 7 te pousse vers des partenariats profondément spirituels et compassionnels. Tu attires des personnes sensibles, parfois blessées, souvent artistiques ou spirituelles. L'amour est pour toi une voie de transcendance.

## Ton défi
Le piège : te perdre dans l'autre au point de t'oublier, attirer des partenaires qui ont besoin d'être sauvés, confondre compassion et codépendance. Les meilleures relations maintiennent deux individualités distinctes.

## Maison 7 en Poissons
Jupiter amplifie la dimension spirituelle de tes partenariats. Tu peux avoir des liens karmiques avec tes partenaires ou les rencontrer de façon mystérieuse. Tes contrats bénéficient de ta capacité à percevoir les intentions cachées.

## Micro-rituel du jour (2 min)
- Exprimer ta gratitude pour la connexion profonde avec un partenaire
- Trois respirations en maintenant ton centre tout en t'ouvrant à l'autre
- Journal : « Comment ma relation me connecte-t-elle à quelque chose de plus grand ? »""",

    ('pisces', 8): """# ♃ Jupiter en Poissons
**En une phrase :** Tu traverses les crises avec foi — les transformations deviennent des dissolutions de l'ancien pour faire place au nouveau.

## Ton moteur
Jupiter en Poissons en Maison 8 te donne une capacité à traverser les crises avec une foi profonde dans le processus de transformation. Tu lâches prise plus facilement que d'autres, tu fais confiance à la mort symbolique comme porte vers la renaissance.

## Ton défi
Le piège : te dissoudre dans les crises au lieu de les traverser, fuir la réalité des pertes, avoir du mal à agir concrètement dans les moments difficiles. La vraie transformation demande aussi de l'action.

## Maison 8 en Poissons
Jupiter amplifie ta connexion aux mystères de la vie et de la mort. Tu peux avoir des perceptions psychiques, des expériences de dissolution de l'ego. Les ressources partagées peuvent venir de façon mystérieuse ou spirituelle.

## Micro-rituel du jour (2 min)
- Méditer sur ce qui veut mourir en toi pour laisser place au nouveau
- Trois respirations en faisant confiance au processus de transformation
- Journal : « Quelle dissolution récente m'a ouvert à plus de vie ? »""",

    ('pisces', 9): """# ♃ Jupiter en Poissons
**En une phrase :** Ta quête de sens est une mystique — tu cherches l'union avec le tout à travers la spiritualité, l'art ou la compassion universelle.

## Ton moteur
Jupiter en Poissons en Maison 9 te donne une soif de transcendance et d'absolu. Tu ne te satisfais pas des philosophies intellectuelles : tu veux l'expérience directe du divin. Cette configuration favorise les voies mystiques, artistiques ou de service universel.

## Ton défi
Le piège : fuir la réalité dans des croyances floues, adhérer à des gourous douteux, confondre rêverie et spiritualité. La vraie foi s'incarne aussi dans le quotidien.

## Maison 9 en Poissons
Jupiter amplifie ta connexion aux dimensions spirituelles. Tu peux avoir des expériences mystiques en voyage ou en méditation. Ton enseignement passe par l'exemple et la transmission subtile plus que par les mots.

## Micro-rituel du jour (2 min)
- Méditer sur ta connexion à quelque chose de plus grand que toi
- Trois respirations en t'ouvrant à l'infini
- Journal : « Quelle expérience m'a récemment connecté au transcendant ? »""",

    ('pisces', 10): """# ♃ Jupiter en Poissons
**En une phrase :** Ta carrière est un sacerdoce — tu réussis en servant quelque chose de plus grand que toi-même avec compassion et vision.

## Ton moteur
Jupiter en Poissons en Maison 10 te pousse vers des professions qui servent le bien commun ou le transcendant. Tu ne cherches pas la gloire personnelle mais l'impact sur les âmes. Cette configuration favorise les carrières dans le soin, l'art, la spiritualité, l'humanitaire.

## Ton défi
Le piège : avoir du mal avec les aspects pratiques de la réussite, te sacrifier professionnellement sans recevoir en retour, confondre mission et exploitation. La vraie vocation mérite aussi d'être rémunérée.

## Maison 10 en Poissons
Jupiter amplifie ta réputation de personne inspirante et compatissante. On te perçoit comme quelqu'un qui sert une vision plus grande. Ta carrière peut sembler floue mais suivre un fil spirituel cohérent.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière sert quelque chose de plus grand que toi
- Trois respirations en connectant ton travail à ta mission d'âme
- Journal : « Comment ma vocation professionnelle nourrit-elle le monde ? »""",

    ('pisces', 11): """# ♃ Jupiter en Poissons
**En une phrase :** Tu crées des communautés d'âmes — tes amitiés et tes groupes sont des espaces de compassion et de connexion spirituelle.

## Ton moteur
Jupiter en Poissons en Maison 11 te donne un talent pour créer des liens profonds dans les groupes. Tu attires des amis sensibles, artistiques, spirituels. Tes projets collectifs ont une dimension de guérison ou de service universel.

## Ton défi
Le piège : te perdre dans les besoins du groupe, attirer des amis qui ont besoin d'être sauvés, avoir du mal avec les aspects pratiques de l'action collective. Les meilleures communautés ont aussi une structure.

## Maison 11 en Poissons
Jupiter amplifie la dimension spirituelle de tes réseaux. Tu peux avoir des liens karmiques avec certains amis ou les rencontrer de façon synchronistique. Tes projets humanitaires touchent à la compassion, la guérison, l'art.

## Micro-rituel du jour (2 min)
- Partager un moment de connexion profonde avec un ami ou un groupe
- Trois respirations en visualisant ton réseau comme un cercle d'âmes
- Journal : « Quelle amitié me connecte à quelque chose de plus grand ? »""",

    ('pisces', 12): """# ♃ Jupiter en Poissons
**En une phrase :** Tu habites l'invisible — ta spiritualité est une immersion dans l'océan de la conscience universelle.

## Ton moteur
Jupiter en Poissons en Maison 12 est une position de grande profondeur spirituelle. Tu as un accès naturel aux dimensions invisibles, à l'inconscient collectif, aux réalités subtiles. Cette configuration favorise la méditation profonde, la guérison spirituelle, l'art transcendant.

## Ton défi
Le piège : te perdre dans les dimensions invisibles au détriment de la vie concrète, confondre dissolution de l'ego et éveil, fuir la réalité dans la spiritualité. La vraie transcendance inclut aussi l'incarnation.

## Maison 12 en Poissons
Jupiter amplifie au maximum ta connexion au mystère. Tu peux avoir des capacités psychiques développées, des rêves prophétiques, une sensibilité aux atmosphères. Les retraites spirituelles profondes te régénèrent mais demandent un retour progressif au quotidien.

## Micro-rituel du jour (2 min)
- Méditer en laissant aller toute identité, juste être
- Trois respirations en te fondant dans l'océan de la conscience
- Journal : « Quel message de l'invisible m'a récemment touché l'âme ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_PISCES.items():
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
