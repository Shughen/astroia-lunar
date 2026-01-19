#!/usr/bin/env python3
"""Script d'insertion des interprétations Neptune/Aries, Taurus, Gemini, Cancer en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

NEPTUNE_INTERPRETATIONS = {
    # ARIES - 12 maisons
    ('aries', 1): """# ♆ Neptune en Bélier
**En une phrase :** Tu incarnes une vision idéaliste de l'action — ton identité cherche à fusionner courage et compassion.

## Ton moteur
Neptune en Bélier en Maison 1 te donne une personnalité qui rêve d'héroïsme et de causes nobles. Tu veux agir pour quelque chose de plus grand que toi, être le champion d'un idéal.

## Ton défi
Le piège : une identité floue qui s'accroche à des idéaux irréalistes, confondre rêve et action, se perdre dans des croisades impossibles. La vraie action inspirée sait aussi être réaliste.

## Maison 1 en Bélier
Neptune adoucit et spiritualise ton énergie d'action. Tu projettes une image de guerrier spirituel. Ton apparence peut refléter tes idéaux et tes rêves d'héroïsme.

## Micro-rituel du jour (2 min)
- Identifier une action concrète qui sert un idéal qui te tient à cœur
- Trois respirations en alignant rêve et réalité
- Journal : « Comment puis-je agir pour mes idéaux de façon réaliste ? »""",

    ('aries', 2): """# ♆ Neptune en Bélier
**En une phrase :** Tu rêves d'une prospérité héroïque — tes ressources viennent quand tu sers une cause plus grande.

## Ton moteur
Neptune en Bélier en Maison 2 crée une relation idéaliste à l'argent. Tu ne veux pas juste gagner de l'argent — tu veux que tes revenus servent quelque chose de noble.

## Ton défi
Le piège : une relation confuse à l'argent, donner tout pour des causes sans te protéger, confondre générosité et sacrifice. La vraie prospérité inspirée inclut aussi ta propre sécurité.

## Maison 2 en Bélier
Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par des activités qui inspirent l'action ou défendent des causes. Tes valeurs sont liées à l'héroïsme et à l'idéalisme.

## Micro-rituel du jour (2 min)
- Identifier comment tes revenus peuvent servir tes idéaux tout en te sécurisant
- Trois respirations en équilibrant générosité et sécurité
- Journal : « Comment puis-je prospérer tout en servant mes causes ? »""",

    ('aries', 3): """# ♆ Neptune en Bélier
**En une phrase :** Tu communiques avec une vision inspirée — tes mots éveillent le courage et l'idéalisme chez les autres.

## Ton moteur
Neptune en Bélier en Maison 3 te donne une communication qui inspire à l'action. Tu sais motiver les autres, éveiller leur courage, leur donner envie de se battre pour quelque chose de beau.

## Ton défi
Le piège : une communication qui exagère ou manipule, promettre plus que possible, confondre inspiration et illusion. La vraie communication inspirée reste aussi honnête.

## Maison 3 en Bélier
Neptune spiritualise tes échanges. Tu peux avoir une communication qui éveille les âmes. Tes relations avec frères, sœurs et voisins peuvent inclure des idéaux partagés.

## Micro-rituel du jour (2 min)
- Partager une vision inspirante de façon honnête avec quelqu'un
- Trois respirations en alignant inspiration et vérité
- Journal : « Comment ma communication peut-elle inspirer sans exagérer ? »""",

    ('aries', 4): """# ♆ Neptune en Bélier
**En une phrase :** Tu rêves d'un foyer héroïque — ta maison devient un lieu où naissent les rêves d'action et de courage.

## Ton moteur
Neptune en Bélier en Maison 4 crée un environnement familial idéaliste et inspirant. Ton foyer peut être un lieu où l'on rêve grand, où l'on se prépare à l'action noble.

## Ton défi
Le piège : une vie familiale confuse par excès d'idéalisme, projeter des attentes héroïques sur ta famille, confondre rêve et réalité chez toi. La vraie maison inspirée a aussi des fondations concrètes.

## Maison 4 en Bélier
Neptune spiritualise ta vie familiale. Tu as peut-être grandi avec des idéaux familiaux ou tu crées un foyer qui inspire au courage. Ton chez-toi peut être un lieu de ressourcement spirituel actif.

## Micro-rituel du jour (2 min)
- Créer un moment d'inspiration concrète chez toi
- Trois respirations en ancrant tes rêves dans ton foyer
- Journal : « Comment mon foyer peut-il nourrir mes rêves de façon réaliste ? »""",

    ('aries', 5): """# ♆ Neptune en Bélier
**En une phrase :** Tu crées avec une vision héroïque — tes œuvres et tes amours sont des rêves d'action et de courage.

## Ton moteur
Neptune en Bélier en Maison 5 te pousse vers une créativité qui inspire l'action. Tu peux créer des œuvres qui éveillent le courage des autres. En amour, tu cherches des partenaires qui partagent tes idéaux héroïques.

## Ton défi
Le piège : idéaliser les partenaires comme des héros, une créativité qui reste dans les rêves, confondre romance et illusion. La vraie joie créative sait aussi apprécier l'imparfait.

## Maison 5 en Bélier
Neptune spiritualise tes plaisirs et ta créativité. Tu peux avoir des amours inspirantes mais parfois décevantes quand la réalité diffère du rêve.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui allie rêve et réalité
- Trois respirations en appréciant la beauté de l'imparfait
- Journal : « Comment ma créativité peut-elle inspirer tout en restant ancrée ? »""",

    ('aries', 6): """# ♆ Neptune en Bélier
**En une phrase :** Tu travailles avec une vision inspirée — ton quotidien devient une mission au service de quelque chose de plus grand.

## Ton moteur
Neptune en Bélier en Maison 6 te pousse vers un travail qui a un sens héroïque. Tu ne supportes pas un travail qui ne sert aucun idéal — tu veux que ton quotidien soit une forme de mission.

## Ton défi
Le piège : un travail confus par excès d'idéalisme, te sacrifier pour ton travail, confondre mission et exploitation. Le vrai service inspiré te protège aussi.

## Maison 6 en Bélier
Neptune spiritualise ton quotidien. Tu travailles mieux quand tu sens que tu sers quelque chose de noble. Ta santé peut être sensible à ton niveau d'inspiration.

## Micro-rituel du jour (2 min)
- Relier une tâche quotidienne à un sens plus large
- Trois respirations en trouvant l'inspiration dans le service
- Journal : « Comment mon travail quotidien peut-il être une mission qui me respecte ? »""",

    ('aries', 7): """# ♆ Neptune en Bélier
**En une phrase :** Tu rêves de partenariats héroïques — tes relations sont des aventures idéalistes partagées.

## Ton moteur
Neptune en Bélier en Maison 7 crée des relations basées sur des idéaux partagés. Tu attires des partenaires avec qui tu veux changer le monde, vivre des aventures nobles.

## Ton défi
Le piège : idéaliser les partenaires, des relations confuses par manque de limites, être déçu quand la réalité diffère du rêve. Les meilleures relations acceptent aussi l'humain imparfait.

## Maison 7 en Bélier
Neptune spiritualise tes partenariats. Tu peux avoir des relations qui semblent destinées mais qui demandent un travail de réalisme.

## Micro-rituel du jour (2 min)
- Apprécier ton partenaire pour qui il est vraiment
- Trois respirations en équilibrant idéal et réalité dans la relation
- Journal : « Comment puis-je aimer mes partenaires pour leur humanité ? »""",

    ('aries', 8): """# ♆ Neptune en Bélier
**En une phrase :** Tu traverses les crises avec foi dans l'action — les transformations deviennent des renaissances héroïques.

## Ton moteur
Neptune en Bélier en Maison 8 te donne la capacité de voir les crises comme des appels à l'héroïsme. Les transformations te poussent à agir avec courage pour quelque chose de plus grand.

## Ton défi
Le piège : fuir les crises dans des rêves d'action, confondre transformation et combat, avoir du mal avec les pertes réelles. La vraie transformation héroïque inclut aussi le deuil.

## Maison 8 en Bélier
Neptune spiritualise ta relation aux crises. Tu peux trouver du sens et de l'inspiration dans les épreuves. Ta sexualité peut être idéaliste ou spiritualisée.

## Micro-rituel du jour (2 min)
- Identifier ce que tu peux faire concrètement face à une transformation
- Trois respirations en accueillant à la fois l'action et le deuil
- Journal : « Comment mes crises m'appellent-elles à l'héroïsme réaliste ? »""",

    ('aries', 9): """# ♆ Neptune en Bélier
**En une phrase :** Tu rêves d'une sagesse héroïque — ta philosophie est celle de l'action inspirée et du courage spirituel.

## Ton moteur
Neptune en Bélier en Maison 9 te pousse vers des croyances qui célèbrent le courage et l'action noble. Ta spiritualité est active, engagée, au service du bien.

## Ton défi
Le piège : des croyances qui justifient l'agressivité, confondre conviction et vérité, imposer tes idéaux aux autres. La vraie sagesse héroïque respecte aussi les autres chemins.

## Maison 9 en Bélier
Neptune spiritualise ta quête de sens. Tu peux être attiré par des spiritualités qui valorisent l'action, le courage, la défense du bien.

## Micro-rituel du jour (2 min)
- Explorer une sagesse qui célèbre le courage sans violence
- Trois respirations en équilibrant conviction et humilité
- Journal : « Quelle sagesse héroïque me guide avec sagesse ? »""",

    ('aries', 10): """# ♆ Neptune en Bélier
**En une phrase :** Tu rêves d'une carrière héroïque — ta réussite vient quand tu deviens un champion de causes inspirantes.

## Ton moteur
Neptune en Bélier en Maison 10 te pousse vers une carrière qui défend des idéaux nobles. Tu ne veux pas juste réussir — tu veux que ta réussite serve quelque chose de plus grand.

## Ton défi
Le piège : une carrière confuse par excès d'idéalisme, être exploité au nom d'une cause, confondre réputation et réalité. La vraie réussite inspirée est aussi reconnue.

## Maison 10 en Bélier
Neptune spiritualise ta carrière et ta réputation. On te reconnaît pour ton engagement et tes idéaux. Ta carrière peut sembler floue mais suivre un fil de mission.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière sert concrètement tes idéaux
- Trois respirations en alignant ambition et service
- Journal : « Comment ma carrière peut-elle être héroïque et réaliste ? »""",

    ('aries', 11): """# ♆ Neptune en Bélier
**En une phrase :** Tu rêves d'action collective héroïque — tes amitiés et tes projets sont des croisades inspirées.

## Ton moteur
Neptune en Bélier en Maison 11 te connecte à des réseaux de personnes engagées pour des causes nobles. Tes amis partagent tes rêves d'action et de changement. Les projets collectifs sont des missions.

## Ton défi
Le piège : des amitiés confuses par des idéaux partagés, te perdre dans des groupes au nom d'une cause, confondre mouvement et changement réel. Les meilleures communautés ont aussi des résultats.

## Maison 11 en Bélier
Neptune spiritualise tes réseaux et tes projets. Tu es fait pour les mouvements inspirants, les associations de défense de causes, les communautés d'idéalistes actifs.

## Micro-rituel du jour (2 min)
- Partager un rêve d'action avec un groupe
- Trois respirations en équilibrant idéal et efficacité collective
- Journal : « Comment mes réseaux peuvent-ils servir nos idéaux concrètement ? »""",

    ('aries', 12): """# ♆ Neptune en Bélier
**En une phrase :** Tu rêves d'héroïsme spirituel — ton inconscient te guide vers des actions qui servent l'invisible.

## Ton moteur
Neptune en Bélier en Maison 12 crée des connexions entre ton courage et les dimensions spirituelles. Tes rêves peuvent t'appeler à l'action inspirée. Ton inconscient est un réservoir de courage spirituel.

## Ton défi
Le piège : fuir dans des rêves d'héroïsme, confondre inspiration et illusion, avoir du mal à agir concrètement. La vraie inspiration intérieure se manifeste aussi dans le monde.

## Maison 12 en Bélier
Neptune spiritualise au maximum ta connexion à l'invisible actif. Tu peux avoir des intuitions qui t'appellent à l'action. Les retraites actives te régénèrent.

## Micro-rituel du jour (2 min)
- Méditer en accueillant l'appel à l'action qui vient de l'intérieur
- Trois respirations en ancrant l'inspiration dans le concret
- Journal : « Quel appel héroïque mon inconscient m'envoie-t-il ? »""",

    # TAURUS - 12 maisons
    ('taurus', 1): """# ♆ Neptune en Taureau
**En une phrase :** Tu incarnes une vision idéaliste de la beauté — ton identité cherche à fusionner sens et sensualité.

## Ton moteur
Neptune en Taureau en Maison 1 te donne une personnalité qui cherche la beauté dans tout ce qui est matériel. Tu veux spiritualiser les sens, trouver le sacré dans le concret.

## Ton défi
Le piège : une identité attachée aux plaisirs qui peuvent devenir des fuites, confondre confort et bonheur, avoir du mal à distinguer besoin et désir. La vraie beauté incarnée sait aussi être simple.

## Maison 1 en Taureau
Neptune adoucit et idéalise ton rapport au corps et aux sens. Tu projettes une image de douceur et de beauté. Ton apparence peut refléter ta quête de l'idéal sensuel.

## Micro-rituel du jour (2 min)
- Identifier une beauté simple et vraie dans ton environnement
- Trois respirations en appréciant le sacré dans le quotidien
- Journal : « Comment puis-je trouver le divin dans le concret ? »""",

    ('taurus', 2): """# ♆ Neptune en Taureau
**En une phrase :** Tu rêves d'une prospérité sacrée — tes ressources sont des bénédictions à partager et à honorer.

## Ton moteur
Neptune en Taureau en Maison 2 crée une relation spirituelle à l'argent et aux ressources. Tu vois l'abondance comme un don qui doit être honoré et partagé.

## Ton défi
Le piège : une relation confuse à l'argent, être trop généreux au point de t'appauvrir, confondre abondance spirituelle et matérielle. La vraie prospérité sacrée est aussi concrète.

## Maison 2 en Taureau
Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par des activités qui touchent à la beauté, à l'art, au bien-être. Tes valeurs sont liées au partage et à la gratitude.

## Micro-rituel du jour (2 min)
- Exprimer de la gratitude pour une ressource que tu as
- Trois respirations en honorant l'abondance dans ta vie
- Journal : « Comment puis-je honorer mes ressources comme des bénédictions ? »""",

    ('taurus', 3): """# ♆ Neptune en Taureau
**En une phrase :** Tu communiques avec beauté et sensibilité — tes mots touchent les sens et éveillent l'appréciation du beau.

## Ton moteur
Neptune en Taureau en Maison 3 te donne une communication qui touche par sa beauté et sa douceur. Tu sais présenter les choses de façon esthétique, éveiller l'appréciation sensorielle.

## Ton défi
Le piège : une communication trop lente ou floue, avoir du mal avec la clarté, confondre beauté et vérité. La vraie communication belle est aussi précise.

## Maison 3 en Taureau
Neptune spiritualise tes échanges de douceur et de beauté. Tu peux avoir un don pour l'écriture poétique ou sensorielle. Tes relations avec frères, sœurs et voisins peuvent être douces mais parfois confuses.

## Micro-rituel du jour (2 min)
- Communiquer quelque chose avec beauté et clarté
- Trois respirations en alignant esthétique et précision
- Journal : « Comment ma communication peut-elle être belle ET claire ? »""",

    ('taurus', 4): """# ♆ Neptune en Taureau
**En une phrase :** Tu rêves d'un foyer sacré — ta maison devient un temple de beauté et de paix sensorielle.

## Ton moteur
Neptune en Taureau en Maison 4 crée un environnement domestique idéalement beau et paisible. Ton foyer est un sanctuaire de beauté, un lieu où les sens sont nourris.

## Ton défi
Le piège : idéaliser le foyer au point d'être déçu par la réalité, fuir les problèmes domestiques dans le confort, confondre cocon et isolement. La vraie maison sacrée s'ouvre aussi au monde.

## Maison 4 en Taureau
Neptune spiritualise ta vie familiale. Tu as peut-être grandi dans un environnement qui valorisait la beauté ou tu crées le tien comme un temple. Ton foyer peut être un lieu de ressourcement profond.

## Micro-rituel du jour (2 min)
- Créer un élément de beauté sacrée chez toi
- Trois respirations en faisant de ton foyer un temple ouvert
- Journal : « Comment mon chez-moi peut-il être un sanctuaire qui accueille ? »""",

    ('taurus', 5): """# ♆ Neptune en Taureau
**En une phrase :** Tu crées avec une sensualité sacrée — tes œuvres et tes amours sont des célébrations de la beauté incarnée.

## Ton moteur
Neptune en Taureau en Maison 5 te pousse vers une créativité qui célèbre les sens et la beauté. Tu peux créer des œuvres qui touchent par leur sensualité. En amour, tu cherches des partenaires qui partagent ton appréciation du beau.

## Ton défi
Le piège : idéaliser les plaisirs au point de fuir dans eux, des amours basées sur la surface, confondre désir et amour. La vraie joie créative a aussi de la profondeur.

## Maison 5 en Taureau
Neptune spiritualise tes plaisirs et ta créativité. Tu peux avoir des amours qui célèbrent la beauté mais qui peuvent manquer de profondeur si tu n'es pas vigilant.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui allie beauté et profondeur
- Trois respirations en appréciant la beauté qui a du sens
- Journal : « Comment ma créativité peut-elle célébrer la beauté avec profondeur ? »""",

    ('taurus', 6): """# ♆ Neptune en Taureau
**En une phrase :** Tu travailles avec une vision de beauté — ton quotidien devient une pratique d'embellissement du monde.

## Ton moteur
Neptune en Taureau en Maison 6 te pousse vers un travail qui crée de la beauté. Tu ne supportes pas un environnement de travail laid — tu veux que ton quotidien soit esthétique et nourrissant.

## Ton défi
Le piège : fuir les tâches ingrates, un travail confus par excès de rêverie, négliger l'efficacité pour l'esthétique. Le vrai travail beau est aussi efficace.

## Maison 6 en Taureau
Neptune spiritualise ton quotidien. Tu travailles mieux dans des environnements beaux et paisibles. Ta santé peut bénéficier de soins qui nourrissent les sens.

## Micro-rituel du jour (2 min)
- Apporter un élément de beauté à ton espace de travail
- Trois respirations en trouvant la beauté dans l'efficacité
- Journal : « Comment mon travail peut-il être beau ET utile ? »""",

    ('taurus', 7): """# ♆ Neptune en Taureau
**En une phrase :** Tu rêves de partenariats harmonieux — tes relations sont des jardins de beauté à cultiver ensemble.

## Ton moteur
Neptune en Taureau en Maison 7 crée des relations basées sur l'harmonie et la beauté partagée. Tu attires des partenaires avec qui tu veux créer un monde de douceur.

## Ton défi
Le piège : idéaliser les partenaires pour leur beauté extérieure, des relations confuses par manque de communication claire, éviter les conflits au détriment de l'authenticité. Les meilleures relations ont aussi des conversations difficiles.

## Maison 7 en Taureau
Neptune spiritualise tes partenariats. Tu peux avoir des relations qui ressemblent à des rêves mais qui demandent du travail pour rester ancrées.

## Micro-rituel du jour (2 min)
- Avoir une conversation authentique avec un partenaire
- Trois respirations en équilibrant harmonie et vérité
- Journal : « Comment mes relations peuvent-elles être belles ET vraies ? »""",

    ('taurus', 8): """# ♆ Neptune en Taureau
**En une phrase :** Tu traverses les crises avec foi dans la beauté — les transformations deviennent des occasions de trouver un nouveau sens du sacré.

## Ton moteur
Neptune en Taureau en Maison 8 te donne la capacité de trouver de la beauté même dans les crises. Les transformations te reconnectent à ce qui est vraiment précieux.

## Ton défi
Le piège : fuir les crises dans les plaisirs, confondre confort et guérison, avoir du mal à lâcher prise sur les attachements matériels. La vraie transformation trouve la beauté au-delà des possessions.

## Maison 8 en Taureau
Neptune spiritualise ta relation aux crises. Tu peux trouver du sens et de la beauté dans les épreuves. Ta sexualité peut être idéalisée ou transcendante.

## Micro-rituel du jour (2 min)
- Identifier une beauté qui émerge d'une transformation
- Trois respirations en lâchant prise sur un attachement
- Journal : « Quelle beauté ai-je découverte dans une épreuve ? »""",

    ('taurus', 9): """# ♆ Neptune en Taureau
**En une phrase :** Tu rêves d'une sagesse incarnée — ta philosophie célèbre le sacré dans le concret et le sensuel.

## Ton moteur
Neptune en Taureau en Maison 9 te pousse vers des croyances qui honorent la matière et les sens comme sacrés. Ta spiritualité est incarnée, terrestre, célébrant la beauté du monde physique.

## Ton défi
Le piège : confondre confort et éveil, des croyances qui justifient l'attachement, avoir du mal avec l'ascèse. La vraie sagesse incarnée sait aussi se détacher.

## Maison 9 en Taureau
Neptune spiritualise ta quête de sens. Tu peux être attiré par des spiritualités qui célèbrent la nature, la beauté, les arts comme voies d'éveil.

## Micro-rituel du jour (2 min)
- Explorer une sagesse qui honore le sacré dans le concret
- Trois respirations en trouvant le divin dans le sensuel
- Journal : « Quelle sagesse incarnée me guide ? »""",

    ('taurus', 10): """# ♆ Neptune en Taureau
**En une phrase :** Tu rêves d'une carrière au service de la beauté — ta réussite vient quand tu embellis le monde.

## Ton moteur
Neptune en Taureau en Maison 10 te pousse vers une carrière qui crée de la beauté. Tu peux réussir dans l'art, le design, le bien-être, tout ce qui nourrit les sens et l'âme.

## Ton défi
Le piège : une carrière floue par excès de rêverie, confondre esthétique et succès, avoir du mal avec les aspects pratiques de la réussite. La vraie carrière belle est aussi reconnue.

## Maison 10 en Taureau
Neptune spiritualise ta carrière et ta réputation. On te reconnaît pour ta capacité à créer de la beauté. Ta carrière peut sembler suivre un chemin mystérieux.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière embellit concrètement le monde
- Trois respirations en alignant beauté et reconnaissance
- Journal : « Comment ma carrière peut-elle être belle ET reconnue ? »""",

    ('taurus', 11): """# ♆ Neptune en Taureau
**En une phrase :** Tu rêves de communautés de beauté — tes amitiés et tes projets créent des oasis de douceur.

## Ton moteur
Neptune en Taureau en Maison 11 te connecte à des réseaux de personnes qui valorisent la beauté et l'harmonie. Tes amis partagent ton appréciation du beau. Les projets collectifs embellissent le monde.

## Ton défi
Le piège : des amitiés basées sur le confort partagé, des projets qui restent au stade du rêve, confondre bien-être collectif et action. Les meilleures communautés passent aussi à l'action.

## Maison 11 en Taureau
Neptune spiritualise tes réseaux et tes projets. Tu es fait pour les collectifs artistiques, les associations écologiques, les communautés qui célèbrent la beauté.

## Micro-rituel du jour (2 min)
- Partager un moment de beauté avec un groupe
- Trois respirations en créant de la douceur collective
- Journal : « Comment mes réseaux peuvent-ils créer de la beauté ensemble ? »""",

    ('taurus', 12): """# ♆ Neptune en Taureau
**En une phrase :** Tu rêves du paradis terrestre — ton inconscient te guide vers une beauté qui transcende le visible.

## Ton moteur
Neptune en Taureau en Maison 12 crée des connexions entre ta sensibilité à la beauté et les dimensions invisibles. Tes rêves peuvent être sensoriellement riches. Ton inconscient cherche le jardin d'Eden.

## Ton défi
Le piège : fuir dans des rêveries de paradis, confondre plaisirs et éveil, avoir du mal avec la réalité imparfaite. La vraie beauté spirituelle accepte aussi l'imperfection.

## Maison 12 en Taureau
Neptune spiritualise au maximum ta connexion à la beauté invisible. Tu peux avoir des expériences de beauté transcendante. Les retraites dans la nature te régénèrent.

## Micro-rituel du jour (2 min)
- Méditer en t'ouvrant à une beauté au-delà du visible
- Trois respirations en acceptant la beauté de l'imparfait
- Journal : « Quelle beauté invisible mon inconscient perçoit-il ? »""",

    # GEMINI - 12 maisons
    ('gemini', 1): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu incarnes une vision poétique de la pensée — ton identité cherche à fusionner raison et imagination.

## Ton moteur
Neptune en Gémeaux en Maison 1 te donne une personnalité qui pense de façon imagée et intuitive. Tu ne sépares pas logique et poésie — tu vois les connexions invisibles entre les idées.

## Ton défi
Le piège : une pensée trop dispersée ou confuse, avoir du mal à distinguer réalité et imagination, confondre rêverie et réflexion. La vraie pensée poétique reste aussi claire.

## Maison 1 en Gémeaux
Neptune adoucit et spiritualise ton intelligence. Tu projettes une image de penseur rêveur. Ton apparence peut refléter ta nature changeante et imaginative.

## Micro-rituel du jour (2 min)
- Exprimer une idée de façon à la fois imagée et claire
- Trois respirations en équilibrant imagination et raison
- Journal : « Comment ma pensée peut-elle être poétique ET précise ? »""",

    ('gemini', 2): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu rêves d'une prospérité par les idées — tes ressources viennent quand tu transmets des visions inspirantes.

## Ton moteur
Neptune en Gémeaux en Maison 2 crée des revenus par la communication inspirée, l'écriture, l'enseignement créatif. Tu valorises les idées qui touchent l'âme.

## Ton défi
Le piège : une relation confuse à l'argent par excès de rêverie, des revenus instables par manque de focus, confondre idées et valeur. La vraie prospérité des idées est aussi concrète.

## Maison 2 en Gémeaux
Neptune spiritualise ta relation aux ressources intellectuelles. Tu peux gagner de l'argent par des talents de communication poétique. Tes valeurs sont liées aux idées et à l'imagination.

## Micro-rituel du jour (2 min)
- Identifier une idée inspirante que tu pourrais valoriser
- Trois respirations en connectant imagination et prospérité
- Journal : « Comment mes idées peuvent-elles créer de la valeur concrète ? »""",

    ('gemini', 3): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu communiques avec poésie — tes mots créent des ponts entre le visible et l'invisible.

## Ton moteur
Neptune en Gémeaux en Maison 3 te donne une communication intuitive et imagée. Tu sais exprimer l'inexprimable, communiquer des idées qui touchent au-delà des mots.

## Ton défi
Le piège : une communication trop floue ou confuse, avoir du mal à être compris, confondre métaphore et mensonge. La vraie communication poétique reste aussi honnête.

## Maison 3 en Gémeaux
Neptune spiritualise au maximum tes échanges. Tu peux avoir des dons pour l'écriture poétique ou intuitive. Tes relations peuvent inclure des liens psychiques ou des malentendus.

## Micro-rituel du jour (2 min)
- Communiquer quelque chose de subtil de façon claire
- Trois respirations en alignant poésie et précision
- Journal : « Comment ma communication peut-elle toucher l'âme tout en restant claire ? »""",

    ('gemini', 4): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu rêves d'un foyer de mots et d'idées — ta maison devient un lieu où l'imagination circule librement.

## Ton moteur
Neptune en Gémeaux en Maison 4 crée un environnement familial où les idées et la créativité sont valorisées. Ton foyer peut être un lieu d'échange intellectuel et poétique.

## Ton défi
Le piège : une vie familiale confuse par trop d'idées, des racines floues, confondre communication et connexion émotionnelle. La vraie maison des idées a aussi du cœur.

## Maison 4 en Gémeaux
Neptune spiritualise ta vie familiale. Tu as peut-être grandi dans un environnement intellectuellement stimulant mais émotionnellement confus. Ton foyer peut être un lieu de créativité et de rêverie.

## Micro-rituel du jour (2 min)
- Créer un moment de connexion émotionnelle au-delà des mots
- Trois respirations en ancrant les idées dans le cœur
- Journal : « Comment mon foyer peut-il nourrir à la fois l'esprit et le cœur ? »""",

    ('gemini', 5): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu crées avec l'imagination verbale — tes œuvres et tes amours sont des poèmes vivants.

## Ton moteur
Neptune en Gémeaux en Maison 5 te pousse vers une créativité littéraire et communicative. Tu peux exceller dans l'écriture, le storytelling, les arts du mot. En amour, tu cherches des partenaires qui nourrissent ton imagination.

## Ton défi
Le piège : des amours qui restent au niveau des mots, une créativité qui se perd dans les idées sans se concrétiser, confondre séduction verbale et amour. La vraie joie créative dépasse aussi les mots.

## Maison 5 en Gémeaux
Neptune spiritualise tes plaisirs intellectuels et créatifs. Tu peux avoir des amours basées sur la stimulation mentale qui peuvent manquer de profondeur émotionnelle.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui va au-delà des mots
- Trois respirations en laissant la joie être silencieuse aussi
- Journal : « Comment ma créativité peut-elle toucher au-delà du mental ? »""",

    ('gemini', 6): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu travailles avec une pensée inspirée — ton quotidien devient une exploration créative des idées.

## Ton moteur
Neptune en Gémeaux en Maison 6 te pousse vers un travail qui utilise tes talents de communication et d'imagination. Tu excelles quand tu peux écrire, enseigner, connecter les idées.

## Ton défi
Le piège : un travail confus par excès de dispersion, avoir du mal avec les tâches pratiques, fuir dans les idées. Le vrai travail inspiré est aussi concret.

## Maison 6 en Gémeaux
Neptune spiritualise ton quotidien. Tu travailles mieux quand tu peux utiliser ton imagination. Ta santé peut être sensible à la sur-stimulation mentale.

## Micro-rituel du jour (2 min)
- Accomplir une tâche pratique avec attention et présence
- Trois respirations en ancrant l'esprit dans le corps
- Journal : « Comment mon travail peut-il être imaginatif ET concret ? »""",

    ('gemini', 7): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu rêves de partenariats de l'esprit — tes relations sont des dialogues d'âmes qui dépassent les mots.

## Ton moteur
Neptune en Gémeaux en Maison 7 crée des relations basées sur la connexion intellectuelle et spirituelle. Tu attires des partenaires avec qui tu partages des conversations qui touchent l'invisible.

## Ton défi
Le piège : des relations qui restent au niveau mental, des malentendus par manque de clarté, confondre communication et connexion. Les meilleures relations incluent aussi le silence et le cœur.

## Maison 7 en Gémeaux
Neptune spiritualise tes partenariats. Tu peux avoir des relations où la communication est intense mais parfois confuse.

## Micro-rituel du jour (2 min)
- Partager un moment de silence significatif avec un partenaire
- Trois respirations en connectant au-delà des mots
- Journal : « Comment mes relations peuvent-elles communiquer au-delà du verbal ? »""",

    ('gemini', 8): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu traverses les crises par la compréhension — les transformations deviennent des révélations qui changent ta façon de penser.

## Ton moteur
Neptune en Gémeaux en Maison 8 te donne la capacité de comprendre les crises à un niveau profond. Les transformations t'apportent des insights qui changent ta vision du monde.

## Ton défi
Le piège : intellectualiser les crises au lieu de les traverser émotionnellement, fuir dans les idées, confondre compréhension et guérison. La vraie transformation inclut aussi le ressenti.

## Maison 8 en Gémeaux
Neptune spiritualise ta relation aux mystères. Tu peux avoir des intuitions fulgurantes sur les situations cachées. Ta sexualité peut être communicative ou mentale.

## Micro-rituel du jour (2 min)
- Laisser une émotion exister sans la comprendre
- Trois respirations en accueillant le mystère au-delà des mots
- Journal : « Quelle transformation m'appelle à ressentir plutôt qu'à comprendre ? »""",

    ('gemini', 9): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu rêves d'une sagesse qui connecte tout — ta philosophie est un réseau d'idées qui révèle l'unité sous la diversité.

## Ton moteur
Neptune en Gémeaux en Maison 9 te pousse vers des croyances qui connectent des savoirs divers. Tu vois les liens invisibles entre les traditions, les cultures, les idées.

## Ton défi
Le piège : une philosophie trop dispersée, confondre quantité d'informations et sagesse, avoir du mal à approfondir. La vraie sagesse connectée sait aussi se concentrer.

## Maison 9 en Gémeaux
Neptune spiritualise ta quête de sens. Tu peux être attiré par des spiritualités qui synthétisent plusieurs traditions. Tes voyages peuvent être mentaux autant que physiques.

## Micro-rituel du jour (2 min)
- Approfondir une seule idée plutôt que d'en survoler plusieurs
- Trois respirations en trouvant la profondeur dans la concentration
- Journal : « Quelle connexion profonde entre idées mérite mon attention ? »""",

    ('gemini', 10): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu rêves d'une carrière de mots et d'idées — ta réussite vient quand tu communiques des visions inspirantes.

## Ton moteur
Neptune en Gémeaux en Maison 10 te pousse vers une carrière dans la communication, l'écriture, l'enseignement inspirant. Tu réussis en transmettant des idées qui touchent les âmes.

## Ton défi
Le piège : une carrière floue par excès de dispersion, confondre réputation et réalité, avoir du mal à te positionner. La vraie réussite communicative a aussi une direction claire.

## Maison 10 en Gémeaux
Neptune spiritualise ta carrière et ta réputation. On te reconnaît pour ta capacité à communiquer des idées inspirantes. Ta carrière peut sembler suivre plusieurs chemins.

## Micro-rituel du jour (2 min)
- Clarifier une direction dans ta carrière
- Trois respirations en alignant diversité et focus
- Journal : « Comment ma carrière peut-elle avoir une direction claire tout en restant diverse ? »""",

    ('gemini', 11): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu rêves de réseaux d'idées — tes amitiés et tes projets sont des conversations collectives inspirantes.

## Ton moteur
Neptune en Gémeaux en Maison 11 te connecte à des réseaux de penseurs et de communicateurs. Tes amis partagent ta passion pour les idées. Les projets collectifs sont basés sur l'échange d'inspirations.

## Ton défi
Le piège : des amitiés superficielles par trop de dispersion, des projets qui restent au stade des idées, confondre conversation et action. Les meilleures communautés passent aussi à l'acte.

## Maison 11 en Gémeaux
Neptune spiritualise tes réseaux et tes projets. Tu es fait pour les groupes de réflexion, les communautés en ligne, les projets de diffusion d'idées.

## Micro-rituel du jour (2 min)
- Transformer une idée partagée en action concrète avec un groupe
- Trois respirations en ancrant les idées dans l'action
- Journal : « Comment mes réseaux peuvent-ils passer des idées à l'action ? »""",

    ('gemini', 12): """# ♆ Neptune en Gémeaux
**En une phrase :** Tu rêves de mots au-delà des mots — ton inconscient te guide vers une communication qui touche l'invisible.

## Ton moteur
Neptune en Gémeaux en Maison 12 crée des connexions entre ta pensée et les dimensions invisibles. Tes rêves peuvent contenir des messages, des mots, des symboles. Ton inconscient communique de façon poétique.

## Ton défi
Le piège : te perdre dans les pensées et les rêveries, confondre imagination et réalité, avoir du mal avec le silence mental. La vraie sagesse intérieure sait aussi se taire.

## Maison 12 en Gémeaux
Neptune spiritualise au maximum ta connexion à l'invisible mental. Tu peux avoir des intuitions qui viennent sous forme de mots ou d'idées. Les retraites silencieuses peuvent être difficiles mais transformatrices.

## Micro-rituel du jour (2 min)
- Méditer en observant les pensées sans s'y attacher
- Trois respirations dans le silence mental
- Journal : « Quel message silencieux mon inconscient m'envoie-t-il ? »""",

    # CANCER - 12 maisons
    ('cancer', 1): """# ♆ Neptune en Cancer
**En une phrase :** Tu incarnes une sensibilité transcendante — ton identité cherche à fusionner émotion et spiritualité.

## Ton moteur
Neptune en Cancer en Maison 1 te donne une personnalité profondément empathique et intuitive. Tu absorbes les émotions ambiantes comme une éponge. Ta sensibilité est ton don et ton défi.

## Ton défi
Le piège : une identité trop poreuse, te perdre dans les émotions des autres, confondre fusion et amour. La vraie sensibilité transcendante a aussi des limites claires.

## Maison 1 en Cancer
Neptune amplifie au maximum ta sensibilité. Tu projettes une image de douceur et de mystère émotionnel. Ton apparence peut refléter tes états d'âme changeants.

## Micro-rituel du jour (2 min)
- Identifier tes propres émotions distinctement de celles des autres
- Trois respirations en créant une limite douce mais claire
- Journal : « Quelles émotions sont vraiment les miennes aujourd'hui ? »""",

    ('cancer', 2): """# ♆ Neptune en Cancer
**En une phrase :** Tu rêves d'une sécurité émotionnelle — tes ressources sont des sources de nourriture pour l'âme.

## Ton moteur
Neptune en Cancer en Maison 2 crée une relation émotionnelle et spirituelle à l'argent. Tu vois les ressources comme des moyens de nourrir et protéger ceux que tu aimes.

## Ton défi
Le piège : confondre sécurité émotionnelle et financière, être trop généreux au point de t'appauvrir, avoir une relation floue à l'argent. La vraie sécurité nourricière a aussi des bases concrètes.

## Maison 2 en Cancer
Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par des activités qui nourrissent et protègent. Tes valeurs sont liées à la famille et aux liens du cœur.

## Micro-rituel du jour (2 min)
- Identifier ce qui te fait vraiment te sentir en sécurité au-delà de l'argent
- Trois respirations en nourrissant ta vraie sécurité
- Journal : « Comment puis-je créer une sécurité qui nourrit mon âme ET mon compte ? »""",

    ('cancer', 3): """# ♆ Neptune en Cancer
**En une phrase :** Tu communiques avec le cœur — tes mots créent des liens de tendresse et de soin.

## Ton moteur
Neptune en Cancer en Maison 3 te donne une communication intuitive et maternante. Tu perçois les besoins non exprimés, tu sais dire ce qui réconforte et guérit.

## Ton défi
Le piège : une communication trop émotionnelle, avoir du mal à être objectif, absorber les émotions des échanges. La vraie communication du cœur sait aussi être claire.

## Maison 3 en Cancer
Neptune spiritualise tes échanges d'émotion et de tendresse. Tu peux avoir des liens psychiques avec ton entourage proche. Tes relations peuvent être très nourrissantes ou très drainantes.

## Micro-rituel du jour (2 min)
- Communiquer quelque chose de difficile avec clarté ET tendresse
- Trois respirations en protégeant ton énergie dans les échanges
- Journal : « Comment ma communication peut-elle nourrir sans me vider ? »""",

    ('cancer', 4): """# ♆ Neptune en Cancer
**En une phrase :** Tu rêves du foyer idéal — ta maison devient un sanctuaire de compassion et de guérison.

## Ton moteur
Neptune en Cancer en Maison 4 amplifie au maximum ta connexion au foyer et à la famille. Ton chez-toi est un temple, ta famille est sacrée. Tu veux créer un cocon de protection totale.

## Ton défi
Le piège : idéaliser la famille au point d'être déçu, absorber les problèmes familiaux, fuir dans le cocon pour éviter le monde. La vraie maison sacrée s'ouvre aussi à l'extérieur.

## Maison 4 en Cancer
Neptune spiritualise au maximum ta vie familiale. Tu as peut-être grandi dans un environnement très émotionnel ou mystique. Ton foyer peut être un lieu de guérison profonde.

## Micro-rituel du jour (2 min)
- Créer un moment de connexion authentique avec ta famille ou ton foyer
- Trois respirations en équilibrant protection et ouverture
- Journal : « Comment mon foyer peut-il me protéger ET me connecter au monde ? »""",

    ('cancer', 5): """# ♆ Neptune en Cancer
**En une phrase :** Tu crées avec tendresse — tes œuvres et tes amours sont des expressions d'amour inconditionnel.

## Ton moteur
Neptune en Cancer en Maison 5 te pousse vers une créativité qui nourrit et guérit. Tu peux créer des œuvres qui touchent le cœur profondément. En amour, tu cherches des partenaires avec qui tu peux créer une famille d'âmes.

## Ton défi
Le piège : des amours fusionnelles qui étouffent, une créativité qui se perd dans le sentimentalisme, confondre protection et amour. La vraie joie créative laisse aussi de l'espace.

## Maison 5 en Cancer
Neptune spiritualise tes plaisirs et ta créativité de tendresse. Tu peux avoir des amours très nourrissantes ou très drainantes selon les limites que tu poses.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui te nourrit sans te vider
- Trois respirations en laissant de l'espace dans l'amour
- Journal : « Comment ma créativité peut-elle nourrir tout en me respectant ? »""",

    ('cancer', 6): """# ♆ Neptune en Cancer
**En une phrase :** Tu travailles avec le cœur — ton quotidien devient un service de compassion et de soin.

## Ton moteur
Neptune en Cancer en Maison 6 te pousse vers des métiers de soin et de guérison. Tu veux prendre soin des autres comme une mère, les nourrir, les protéger.

## Ton défi
Le piège : absorber les souffrances de ceux que tu aides, te sacrifier au travail, confondre service et épuisement. Le vrai soin durable inclut ta propre protection.

## Maison 6 en Cancer
Neptune spiritualise ton quotidien. Tu travailles mieux dans des environnements bienveillants et familiaux. Ta santé est très sensible aux émotions et à l'atmosphère.

## Micro-rituel du jour (2 min)
- Prendre soin de toi avant de prendre soin des autres
- Trois respirations en protégeant ton énergie de guérison
- Journal : « Comment puis-je servir avec compassion sans m'épuiser ? »""",

    ('cancer', 7): """# ♆ Neptune en Cancer
**En une phrase :** Tu rêves de partenariats familiaux — tes relations sont des familles d'âmes à créer et protéger.

## Ton moteur
Neptune en Cancer en Maison 7 crée des relations qui ressemblent à des familles. Tu attires des partenaires avec qui tu veux créer un foyer, un cocon de tendresse.

## Ton défi
Le piège : des relations fusionnelles qui étouffent, chercher à materner ton partenaire, confondre dépendance et amour. Les meilleures relations laissent aussi de l'espace.

## Maison 7 en Cancer
Neptune spiritualise tes partenariats de profonde tendresse. Tu peux avoir des relations très nourrissantes mais qui demandent des limites saines.

## Micro-rituel du jour (2 min)
- Créer un moment d'indépendance saine dans ta relation
- Trois respirations en équilibrant fusion et espace
- Journal : « Comment mes relations peuvent-elles être tendres ET spacieuses ? »""",

    ('cancer', 8): """# ♆ Neptune en Cancer
**En une phrase :** Tu traverses les crises avec le cœur — les transformations deviennent des occasions de guérison émotionnelle profonde.

## Ton moteur
Neptune en Cancer en Maison 8 te donne la capacité de guérir des blessures émotionnelles profondes à travers les crises. Les transformations te reconnectent à l'amour inconditionnel.

## Ton défi
Le piège : te noyer dans les émotions des crises, avoir du mal à lâcher prise sur les attachements, fuir dans le cocon. La vraie guérison émotionnelle traverse aussi la douleur.

## Maison 8 en Cancer
Neptune spiritualise ta relation aux crises émotionnelles. Tu peux avoir des capacités de guérison ou de connexion psychique. Ta sexualité peut être très émotionnelle et guérissante.

## Micro-rituel du jour (2 min)
- Accueillir une émotion difficile sans la fuir
- Trois respirations en traversant plutôt qu'éviter
- Journal : « Quelle guérison émotionnelle m'attend de l'autre côté de cette épreuve ? »""",

    ('cancer', 9): """# ♆ Neptune en Cancer
**En une phrase :** Tu rêves d'une sagesse maternelle — ta philosophie est celle de l'amour inconditionnel et de la compassion universelle.

## Ton moteur
Neptune en Cancer en Maison 9 te pousse vers des croyances qui célèbrent l'amour maternel cosmique, la tendresse divine, la compassion comme sagesse suprême.

## Ton défi
Le piège : des croyances qui confondent protection et limitation, chercher une mère cosmique plutôt que grandir, avoir du mal à quitter le cocon spirituel. La vraie sagesse maternelle encourage aussi l'autonomie.

## Maison 9 en Cancer
Neptune spiritualise ta quête de sens. Tu peux être attiré par des spiritualités qui vénèrent le féminin sacré, la Mère divine, l'amour inconditionnel.

## Micro-rituel du jour (2 min)
- Explorer une sagesse qui encourage ton autonomie spirituelle
- Trois respirations en grandissant au sein de l'amour
- Journal : « Comment la sagesse peut-elle me nourrir ET m'autonomiser ? »""",

    ('cancer', 10): """# ♆ Neptune en Cancer
**En une phrase :** Tu rêves d'une carrière maternante — ta réussite vient quand tu nourris et protèges le monde.

## Ton moteur
Neptune en Cancer en Maison 10 te pousse vers une carrière qui prend soin du monde. Tu peux réussir dans les métiers de soin, d'éducation, de protection, tout ce qui nourrit les autres.

## Ton défi
Le piège : une carrière confuse par excès de don, te sacrifier professionnellement, confondre vocation et exploitation. La vraie réussite nourrissante est aussi reconnue et rémunérée.

## Maison 10 en Cancer
Neptune spiritualise ta carrière et ta réputation. On te reconnaît pour ta capacité à prendre soin. Ta carrière peut sembler suivre un chemin maternel.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière peut nourrir tout en te rémunérant justement
- Trois respirations en alignant service et reconnaissance
- Journal : « Comment ma carrière peut-elle être nourrissante ET reconnue ? »""",

    ('cancer', 11): """# ♆ Neptune en Cancer
**En une phrase :** Tu rêves de familles d'âmes — tes amitiés et tes projets sont des cercles de tendresse et de protection mutuelle.

## Ton moteur
Neptune en Cancer en Maison 11 te connecte à des réseaux qui deviennent des familles. Tes amis sont des âmes sœurs avec qui tu partages un lien de tendresse profonde. Les projets collectifs nourrissent et protègent.

## Ton défi
Le piège : des amitiés fusionnelles qui étouffent, absorber les émotions du groupe, confondre communauté et famille. Les meilleures communautés respectent aussi l'individualité.

## Maison 11 en Cancer
Neptune spiritualise tes réseaux et tes projets de tendresse collective. Tu es fait pour les cercles de soutien, les associations de soin, les communautés qui nourrissent.

## Micro-rituel du jour (2 min)
- Créer un moment de tendresse avec ton réseau tout en gardant ton individualité
- Trois respirations en équilibrant appartenance et identité
- Journal : « Comment mes réseaux peuvent-ils me nourrir sans m'absorber ? »""",

    ('cancer', 12): """# ♆ Neptune en Cancer
**En une phrase :** Tu rêves de l'océan maternel — ton inconscient est une source de guérison émotionnelle infinie.

## Ton moteur
Neptune en Cancer en Maison 12 amplifie au maximum ta connexion aux dimensions émotionnelles invisibles. Tu peux percevoir les émotions du collectif, avoir des capacités de guérison profondes.

## Ton défi
Le piège : te perdre dans l'océan émotionnel, confondre tes émotions et celles du monde, fuir dans le cocon intérieur. La vraie guérison intérieure a aussi des frontières.

## Maison 12 en Cancer
Neptune spiritualise au maximum ta connexion à l'invisible émotionnel. Tu peux avoir des capacités psychiques ou de guérison. Les retraites dans des lieux nourrissants te régénèrent profondément.

## Micro-rituel du jour (2 min)
- Méditer en créant une bulle de protection douce autour de toi
- Trois respirations en accueillant l'invisible avec des limites
- Journal : « Comment puis-je me connecter à l'océan émotionnel sans m'y noyer ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in NEPTUNE_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'neptune',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP neptune/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='neptune',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT neptune/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
