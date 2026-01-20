#!/usr/bin/env python3
"""
Script pour corriger les 36 interprétations SUN manquantes (maisons 9, 11, 12)
Format natal V2 avec: En une phrase / Ton moteur / Ton défi / Maison X / Micro-rituel
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import update
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Interprétations SUN format V2 - Maisons 9, 11, 12 pour les 12 signes
SUN_INTERPRETATIONS = {
    # ARIES
    ('aries', 9): """# ☀️ Soleil en Bélier

**En une phrase :** Tu t'affirmes à travers l'exploration, la quête de sens et l'aventure intellectuelle ou physique.

## Ton moteur
Ta vitalité s'exprime dans l'expansion de tes horizons. Tu as besoin de repousser les limites, que ce soit par les voyages, les études ou les défis philosophiques. L'action et la découverte nourrissent ton identité.

## Ton défi
Éviter de t'éparpiller dans trop de directions à la fois. Ton enthousiasme pionnier peut te faire commencer mille aventures sans en approfondir aucune.

## Maison 9 en Bélier
Tu abordes les grandes questions de la vie avec audace et spontanéité. Les voyages lointains, l'enseignement ou la philosophie sont des terrains où tu brilles naturellement, à condition de cultiver la patience.

## Micro-rituel du jour (2 min)
- Identifie une croyance que tu n'as jamais remise en question
- Respire profondément et demande-toi : "Est-ce vraiment ma conviction ?"
- Note une action concrète pour explorer une nouvelle perspective""",

    ('aries', 11): """# ☀️ Soleil en Bélier

**En une phrase :** Tu t'affirmes en prenant l'initiative au sein des groupes et en portant des projets collectifs audacieux.

## Ton moteur
Tu as besoin de te sentir leader ou pionnier dans tes cercles sociaux. Les amitiés qui te stimulent sont celles où tu peux initier, proposer, entraîner les autres vers de nouveaux horizons.

## Ton défi
Apprendre à collaborer sans toujours vouloir être en tête. Ton impatience peut froisser ceux qui ont un rythme différent du tien.

## Maison 11 en Bélier
Tes projets collectifs portent ta marque d'audace. Tu attires des amis dynamiques et tu excelles à lancer des initiatives de groupe, même si tu dois veiller à ne pas imposer ton tempo.

## Micro-rituel du jour (2 min)
- Pense à un projet collectif qui te tient à cœur
- Respire et visualise-toi écoutant vraiment les idées des autres
- Note une façon de valoriser la contribution d'un ami aujourd'hui""",

    ('aries', 12): """# ☀️ Soleil en Bélier

**En une phrase :** Tu puises ta force dans une combativité intérieure, une énergie qui se manifeste souvent en coulisses.

## Ton moteur
Ton identité se construit dans l'ombre, à travers des batailles intérieures et une quête spirituelle active. Tu as besoin de temps seul pour recharger ton feu intérieur.

## Ton défi
Éviter de réprimer ton énergie d'action ou de la retourner contre toi-même. L'isolement excessif peut éteindre ta flamme.

## Maison 12 en Bélier
Tu agis souvent dans l'ombre, portant des combats invisibles. Ta spiritualité est active, dynamique. Apprends à canaliser cette énergie sans t'épuiser dans des luttes intérieures.

## Micro-rituel du jour (2 min)
- Ferme les yeux et identifie une frustration que tu gardes pour toi
- Respire dans cette tension sans chercher à la résoudre
- Note une action symbolique pour libérer cette énergie aujourd'hui""",

    # TAURUS
    ('taurus', 9): """# ☀️ Soleil en Taureau

**En une phrase :** Tu t'affirmes en construisant une philosophie de vie concrète, ancrée dans l'expérience sensible.

## Ton moteur
Ta quête de sens passe par le tangible. Les voyages, études ou croyances qui te nourrissent sont ceux que tu peux toucher, goûter, vivre pleinement. Tu bâtis ta sagesse pierre par pierre.

## Ton défi
Éviter de t'enfermer dans des certitudes trop rigides. Ton besoin de stabilité peut freiner l'ouverture à d'autres visions du monde.

## Maison 9 en Taureau
Tu explores les grandes questions avec patience et pragmatisme. Tes voyages ou apprentissages visent une richesse durable, pas l'aventure pour l'aventure.

## Micro-rituel du jour (2 min)
- Choisis une croyance qui te sécurise
- Respire et demande-toi : "Cette certitude m'ouvre-t-elle ou me limite-t-elle ?"
- Note une petite ouverture que tu pourrais faire aujourd'hui""",

    ('taurus', 11): """# ☀️ Soleil en Taureau

**En une phrase :** Tu t'affirmes en apportant stabilité et fiabilité aux projets collectifs et à tes amitiés.

## Ton moteur
Tu as besoin d'amitiés durables et de projets de groupe qui construisent quelque chose de concret. Ta loyauté est ta signature dans les cercles sociaux.

## Ton défi
Éviter de t'accrocher à des amitiés ou des groupes qui ne te correspondent plus par simple habitude ou confort.

## Maison 11 en Taureau
Tes projets collectifs visent la pérennité. Tu attires des amis fidèles et tu apportes une énergie stabilisatrice, même si tu dois parfois accepter le changement.

## Micro-rituel du jour (2 min)
- Pense à une amitié ou un groupe qui t'apporte de la stabilité
- Respire et ressens la gratitude pour cette ancre
- Note une façon de nourrir ce lien aujourd'hui""",

    ('taurus', 12): """# ☀️ Soleil en Taureau

**En une phrase :** Tu puises ta force dans une connexion profonde avec la nature, le corps et les ressources intérieures.

## Ton moteur
Ton identité se ressource dans le silence, le contact avec la terre, les plaisirs simples vécus en solitude. Tu as besoin de ce retrait pour te sentir ancré.

## Ton défi
Éviter de t'isoler par paresse ou résistance au changement. Le confort peut devenir une prison dorée.

## Maison 12 en Taureau
Ta spiritualité est sensorielle, incarnée. Tu trouves le sacré dans la matière, le repos, la beauté simple. Veille à ne pas fuir le monde dans un cocon trop douillet.

## Micro-rituel du jour (2 min)
- Trouve un moment de silence et touche quelque chose de naturel
- Respire en ressentant la texture, la température
- Note ce que ce contact t'apprend sur toi aujourd'hui""",

    # GEMINI
    ('gemini', 9): """# ☀️ Soleil en Gémeaux

**En une phrase :** Tu t'affirmes en explorant une multitude d'idées, de cultures et de perspectives.

## Ton moteur
Ta quête de sens est intellectuelle et plurielle. Tu as besoin de voyager mentalement, de comparer les philosophies, d'apprendre plusieurs langues ou disciplines.

## Ton défi
Éviter de survoler les sujets sans jamais approfondir. Ta curiosité peut te disperser au point de ne rien maîtriser vraiment.

## Maison 9 en Gémeaux
Tu explores les grandes questions avec légèreté et curiosité. L'enseignement, l'écriture ou les échanges interculturels te permettent de briller.

## Micro-rituel du jour (2 min)
- Choisis un sujet que tu survoles depuis longtemps
- Respire et engage-toi à l'approfondir pendant 10 minutes
- Note une question précise à explorer aujourd'hui""",

    ('gemini', 11): """# ☀️ Soleil en Gémeaux

**En une phrase :** Tu t'affirmes en connectant les gens, en faisant circuler idées et informations dans tes réseaux.

## Ton moteur
Tu as besoin d'amitiés stimulantes intellectuellement et de projets collectifs où la communication est centrale. Tu es le connecteur naturel de tes cercles.

## Ton défi
Éviter les relations superficielles ou le papillonnage social. Trop d'échanges légers peuvent te laisser isolé dans la foule.

## Maison 11 en Gémeaux
Tes projets de groupe brillent par leur créativité communicative. Tu attires des amis variés et excelles à faire le lien entre différents univers.

## Micro-rituel du jour (2 min)
- Pense à deux amis qui ne se connaissent pas mais gagneraient à se rencontrer
- Respire et visualise ce pont que tu peux créer
- Note une action pour connecter ces personnes""",

    ('gemini', 12): """# ☀️ Soleil en Gémeaux

**En une phrase :** Tu puises ta force dans l'écriture intime, la réflexion solitaire et l'exploration de ton monde intérieur.

## Ton moteur
Ton identité se construit dans le dialogue avec toi-même. Journal intime, méditation active, lectures profondes nourrissent ton être caché.

## Ton défi
Éviter de te perdre dans un mental hyperactif qui tourne à vide. Le bavardage intérieur peut devenir épuisant.

## Maison 12 en Gémeaux
Ta spiritualité passe par les mots, l'écriture, la compréhension. Tu as une vie mentale secrète riche qu'il est bon de canaliser.

## Micro-rituel du jour (2 min)
- Écris trois pensées qui tournent dans ta tête en ce moment
- Respire et observe-les sans les juger
- Note celle qui mérite vraiment ton attention aujourd'hui""",

    # CANCER
    ('cancer', 9): """# ☀️ Soleil en Cancer

**En une phrase :** Tu t'affirmes en explorant tes racines, ton histoire familiale et les traditions qui te nourrissent.

## Ton moteur
Ta quête de sens est émotionnelle et mémorielle. Les voyages qui te touchent sont ceux qui te reconnectent à des origines, des ancêtres, une mémoire collective.

## Ton défi
Éviter de t'enfermer dans le passé ou dans une vision trop nostalgique du monde. L'avenir a aussi besoin de toi.

## Maison 9 en Cancer
Tu explores les grandes questions avec ton cœur. L'enseignement ou la philosophie qui te parlent sont ceux qui honorent l'émotion et la transmission.

## Micro-rituel du jour (2 min)
- Pense à une tradition familiale qui t'a marqué
- Respire et ressens ce qu'elle t'a transmis
- Note comment tu pourrais la faire vivre autrement aujourd'hui""",

    ('cancer', 11): """# ☀️ Soleil en Cancer

**En une phrase :** Tu t'affirmes en créant des communautés chaleureuses où chacun se sent accueilli comme en famille.

## Ton moteur
Tu as besoin d'amitiés profondes et de projets collectifs qui prennent soin des membres. Tu es le cœur nourricier de tes cercles sociaux.

## Ton défi
Éviter de materner excessivement tes amis ou de te replier si tu te sens rejeté. Tous n'ont pas besoin de la même chaleur.

## Maison 11 en Cancer
Tes projets de groupe ont une dimension familiale. Tu attires des amis fidèles et crées des espaces où l'émotion a sa place.

## Micro-rituel du jour (2 min)
- Pense à un ami qui pourrait avoir besoin de soutien
- Respire et envoie-lui mentalement de la chaleur
- Note un geste concret d'attention pour aujourd'hui""",

    ('cancer', 12): """# ☀️ Soleil en Cancer

**En une phrase :** Tu puises ta force dans un monde intérieur riche en émotions, souvenirs et connexions invisibles.

## Ton moteur
Ton identité se ressource dans la solitude protectrice, le contact avec tes émotions profondes, la mémoire des êtres aimés.

## Ton défi
Éviter de te noyer dans la nostalgie ou de fuir le présent dans un cocon émotionnel. Le passé ne doit pas devenir une prison.

## Maison 12 en Cancer
Ta spiritualité est celle du cœur, de l'intuition, du lien invisible avec ceux que tu aimes. Veille à ne pas t'isoler dans une mélancolie trop douce.

## Micro-rituel du jour (2 min)
- Ferme les yeux et pense à quelqu'un qui t'a aimé inconditionnellement
- Respire cet amour qui est toujours en toi
- Note comment tu peux t'offrir cette même douceur aujourd'hui""",

    # LEO
    ('leo', 9): """# ☀️ Soleil en Lion

**En une phrase :** Tu t'affirmes en partageant ta vision du monde avec générosité et en inspirant les autres par ton enthousiasme.

## Ton moteur
Ta quête de sens est créative et rayonnante. Tu as besoin d'enseigner, de transmettre, de voyager en laissant une empreinte lumineuse partout où tu passes.

## Ton défi
Éviter de transformer ta philosophie en spectacle ou de vouloir avoir raison à tout prix. Ta lumière n'a pas besoin d'écraser celle des autres.

## Maison 9 en Lion
Tu explores les grandes questions avec panache. L'enseignement, les voyages ou la spiritualité te permettent de briller et d'inspirer.

## Micro-rituel du jour (2 min)
- Pense à une conviction que tu aimerais transmettre
- Respire et demande-toi : "Comment la partager avec humilité ?"
- Note une façon d'inspirer sans imposer aujourd'hui""",

    ('leo', 11): """# ☀️ Soleil en Lion

**En une phrase :** Tu t'affirmes en étant le cœur vibrant de tes cercles sociaux, celui qui fédère et enthousiasme.

## Ton moteur
Tu as besoin de briller au sein de tes groupes, d'être reconnu pour ta générosité et ton leadership naturel. Tes amitiés doivent célébrer qui tu es.

## Ton défi
Éviter de monopoliser l'attention ou de souffrir si d'autres brillent aussi. La vraie grandeur sait partager la lumière.

## Maison 11 en Lion
Tes projets collectifs portent ta signature créative. Tu attires des amis loyaux et tu sais transformer un groupe en tribu soudée autour d'une vision.

## Micro-rituel du jour (2 min)
- Pense à un ami dont tu admires une qualité
- Respire et ressens la joie de le voir briller
- Note une façon de célébrer son talent aujourd'hui""",

    ('leo', 12): """# ☀️ Soleil en Lion

**En une phrase :** Tu puises ta force dans une créativité secrète, une lumière intérieure qui n'a pas besoin d'applaudissements.

## Ton moteur
Ton identité se ressource dans la création solitaire, la méditation sur ta propre lumière, la connexion avec une source intérieure de confiance.

## Ton défi
Éviter de cacher tes talents par fausse modestie ou de t'éteindre dans l'ombre. Ta lumière mérite aussi de rayonner à l'extérieur.

## Maison 12 en Lion
Ta spiritualité est celle du cœur créateur. Tu as une dignité intérieure qui ne dépend pas du regard des autres, à condition de ne pas t'isoler.

## Micro-rituel du jour (2 min)
- Ferme les yeux et visualise une flamme dorée au centre de ton cœur
- Respire en la laissant grandir doucement
- Note une création que tu pourrais faire juste pour toi aujourd'hui""",

    # VIRGO
    ('virgo', 9): """# ☀️ Soleil en Vierge

**En une phrase :** Tu t'affirmes en analysant les grandes questions avec rigueur et en cherchant une sagesse pratique.

## Ton moteur
Ta quête de sens est méthodique. Tu as besoin de comprendre, d'étudier en profondeur, de trouver des applications concrètes aux philosophies qui t'attirent.

## Ton défi
Éviter de réduire le sens de la vie à ce qui est mesurable ou utile. Le mystère a aussi sa place.

## Maison 9 en Vierge
Tu explores les grandes questions avec discernement. L'enseignement ou les voyages te nourrissent s'ils ont une utilité pratique.

## Micro-rituel du jour (2 min)
- Choisis une croyance abstraite que tu as du mal à saisir
- Respire et cherche un exemple concret qui l'illustre
- Note comment cette croyance pourrait s'appliquer aujourd'hui""",

    ('virgo', 11): """# ☀️ Soleil en Vierge

**En une phrase :** Tu t'affirmes en étant utile à tes amis et en apportant une contribution concrète aux projets collectifs.

## Ton moteur
Tu as besoin de te sentir utile dans tes cercles sociaux. Tes amitiés sont nourries par l'entraide pratique et les projets qui améliorent la vie quotidienne.

## Ton défi
Éviter de te cantonner au rôle de celui qui aide sans jamais recevoir, ou de critiquer excessivement les projets des autres.

## Maison 11 en Vierge
Tes projets collectifs visent l'amélioration concrète. Tu attires des amis fiables et tu apportes une rigueur précieuse aux initiatives de groupe.

## Micro-rituel du jour (2 min)
- Pense à un ami à qui tu pourrais demander de l'aide
- Respire et accepte l'idée de recevoir autant que de donner
- Note une demande simple que tu pourrais faire aujourd'hui""",

    ('virgo', 12): """# ☀️ Soleil en Vierge

**En une phrase :** Tu puises ta force dans le service discret, l'analyse de ton monde intérieur et le perfectionnement silencieux.

## Ton moteur
Ton identité se construit dans l'ombre à travers le travail sur toi-même, l'aide discrète aux autres, une quête de pureté intérieure.

## Ton défi
Éviter l'autocritique excessive ou de te perdre dans des détails insignifiants. La perfection intérieure n'existe pas.

## Maison 12 en Vierge
Ta spiritualité est celle du service humble et de l'amélioration continue. Tu as une vie intérieure ordonnée qui peut devenir rigide si tu n'y prends garde.

## Micro-rituel du jour (2 min)
- Identifie une critique intérieure récurrente
- Respire et transforme-la en encouragement bienveillant
- Note une imperfection que tu peux accepter aujourd'hui""",

    # LIBRA
    ('libra', 9): """# ☀️ Soleil en Balance

**En une phrase :** Tu t'affirmes en explorant les différentes perspectives avec équité et en cherchant une harmonie philosophique.

## Ton moteur
Ta quête de sens passe par le dialogue, la comparaison des points de vue, la recherche d'une vérité équilibrée qui intègre les opposés.

## Ton défi
Éviter de rester indécis face aux grandes questions ou de vouloir plaire à toutes les écoles de pensée.

## Maison 9 en Balance
Tu explores les grandes questions avec diplomatie. L'enseignement ou les voyages te nourrissent s'ils favorisent la rencontre et l'échange.

## Micro-rituel du jour (2 min)
- Choisis un débat où tu as du mal à trancher
- Respire et identifie ta vraie position, même imparfaite
- Note une conviction que tu assumes aujourd'hui""",

    ('libra', 11): """# ☀️ Soleil en Balance

**En une phrase :** Tu t'affirmes en créant l'harmonie dans tes cercles sociaux et en facilitant la collaboration.

## Ton moteur
Tu as besoin d'amitiés équilibrées et de projets collectifs où règne la coopération. Tu es le diplomate naturel de tes groupes.

## Ton défi
Éviter de t'oublier pour maintenir la paix ou de fuir les conflits nécessaires à l'évolution du groupe.

## Maison 11 en Balance
Tes projets collectifs visent la beauté et l'harmonie. Tu attires des amis raffinés et tu excelles à créer des espaces de dialogue.

## Micro-rituel du jour (2 min)
- Pense à un désaccord que tu évites dans un groupe
- Respire et visualise une façon de l'aborder avec tact
- Note une position que tu pourrais affirmer aujourd'hui""",

    ('libra', 12): """# ☀️ Soleil en Balance

**En une phrase :** Tu puises ta force dans une quête intérieure d'harmonie, de beauté et de paix avec toi-même.

## Ton moteur
Ton identité se ressource dans la solitude esthétique, la méditation sur l'équilibre, le dialogue intérieur entre tes différentes facettes.

## Ton défi
Éviter de te perdre dans l'indécision intérieure ou de fuir les aspects de toi-même que tu juges inélégants.

## Maison 12 en Balance
Ta spiritualité est celle de l'harmonie intérieure. Tu cherches la paix avec tes zones d'ombre, à condition de ne pas nier leur existence.

## Micro-rituel du jour (2 min)
- Ferme les yeux et identifie un aspect de toi que tu caches
- Respire et offre-lui de la douceur sans le juger
- Note une façon d'intégrer cette part de toi aujourd'hui""",

    # SCORPIO
    ('scorpio', 9): """# ☀️ Soleil en Scorpion

**En une phrase :** Tu t'affirmes en explorant les vérités cachées, les mystères de l'existence et les profondeurs philosophiques.

## Ton moteur
Ta quête de sens est intense et transformatrice. Tu as besoin de voyages initiatiques, d'études qui te bouleversent, de croyances qui touchent à la mort et à la renaissance.

## Ton défi
Éviter de t'enfermer dans une vision trop sombre du monde ou de rejeter les philosophies qui te semblent superficielles.

## Maison 9 en Scorpion
Tu explores les grandes questions avec passion et profondeur. L'enseignement ou les voyages qui te marquent sont ceux qui transforment ton regard.

## Micro-rituel du jour (2 min)
- Choisis une vérité inconfortable que tu évites
- Respire et regarde-la en face sans te laisser submerger
- Note une façon d'intégrer cette vérité aujourd'hui""",

    ('scorpio', 11): """# ☀️ Soleil en Scorpion

**En une phrase :** Tu t'affirmes en créant des liens profonds au sein de tes groupes et en portant des projets transformateurs.

## Ton moteur
Tu as besoin d'amitiés intenses et de projets collectifs qui ont un impact réel. Les relations superficielles t'ennuient ou te frustrent.

## Ton défi
Éviter de vouloir tout contrôler dans tes cercles ou de te méfier excessivement des intentions des autres.

## Maison 11 en Scorpion
Tes projets de groupe visent la transformation profonde. Tu attires des amis loyaux jusqu'à la mort et tu excelles dans les causes qui touchent aux tabous.

## Micro-rituel du jour (2 min)
- Pense à un ami en qui tu as une confiance absolue
- Respire et ressens la puissance de ce lien
- Note une façon d'approfondir cette connexion aujourd'hui""",

    ('scorpio', 12): """# ☀️ Soleil en Scorpion

**En une phrase :** Tu puises ta force dans l'exploration de tes profondeurs, la confrontation avec tes zones d'ombre.

## Ton moteur
Ton identité se forge dans les descentes intérieures, les morts et renaissances psychiques, la transformation silencieuse.

## Ton défi
Éviter de t'enliser dans tes abysses ou de cultiver une fascination morbide. La lumière existe aussi dans les profondeurs.

## Maison 12 en Scorpion
Ta spiritualité est celle de la métamorphose. Tu as accès à des puissances intérieures considérables, à condition de ne pas te perdre dans l'obscurité.

## Micro-rituel du jour (2 min)
- Ferme les yeux et descends dans ton espace intérieur le plus sombre
- Respire et cherche une lueur, aussi petite soit-elle
- Note ce que cette lueur t'enseigne aujourd'hui""",

    # SAGITTARIUS
    ('sagittarius', 9): """# ☀️ Soleil en Sagittaire

**En une phrase :** Tu t'affirmes en explorant le monde avec enthousiasme, en quête de sens et d'aventure.

## Ton moteur
Tu es dans ton élément en maison 9. Voyages, philosophie, enseignement, tout ce qui élargit tes horizons nourrit profondément ton identité.

## Ton défi
Éviter de croire que tu détiens la vérité ou de fuir dans l'ailleurs dès que le quotidien t'ennuie.

## Maison 9 en Sagittaire
Double signature sagittarienne : tu as un besoin vital d'expansion. L'enseignement, les cultures étrangères, la quête spirituelle sont ton terrain de jeu naturel.

## Micro-rituel du jour (2 min)
- Pense à une conviction qui te porte
- Respire et demande-toi : "Puis-je l'enrichir d'un autre point de vue ?"
- Note une façon d'élargir ta vision aujourd'hui""",

    ('sagittarius', 11): """# ☀️ Soleil en Sagittaire

**En une phrase :** Tu t'affirmes en inspirant tes amis et en portant des projets collectifs enthousiastes et visionnaires.

## Ton moteur
Tu as besoin d'amitiés qui partagent ta soif d'aventure et de projets de groupe qui visent haut. Tu es le motivateur naturel de tes cercles.

## Ton défi
Éviter de promettre plus que tu ne peux tenir ou de t'impatienter face à ceux qui avancent plus lentement.

## Maison 11 en Sagittaire
Tes projets collectifs sont ambitieux et optimistes. Tu attires des amis de tous horizons et tu excelles à fédérer autour de grandes visions.

## Micro-rituel du jour (2 min)
- Pense à un projet de groupe qui te fait rêver
- Respire et identifie la première étape concrète
- Note une action réaliste pour avancer aujourd'hui""",

    ('sagittarius', 12): """# ☀️ Soleil en Sagittaire

**En une phrase :** Tu puises ta force dans une quête spirituelle solitaire, une foi intérieure qui n'a pas besoin de temples.

## Ton moteur
Ton identité se ressource dans l'exploration intérieure, les voyages de l'âme, une connexion directe avec le sens de l'existence.

## Ton défi
Éviter de fuir dans des croyances qui t'éloignent de la réalité ou de t'isoler dans une tour d'ivoire spirituelle.

## Maison 12 en Sagittaire
Ta spiritualité est vaste et libre. Tu as accès à une sagesse intérieure profonde, à condition de rester ancré dans le monde.

## Micro-rituel du jour (2 min)
- Ferme les yeux et connecte-toi à ta source de foi intérieure
- Respire et laisse cette confiance t'envelopper
- Note comment cette foi peut éclairer ta journée""",

    # CAPRICORN
    ('capricorn', 9): """# ☀️ Soleil en Capricorne

**En une phrase :** Tu t'affirmes en construisant une vision du monde solide, fondée sur l'expérience et la maturité.

## Ton moteur
Ta quête de sens est pragmatique et ambitieuse. Tu cherches des philosophies qui ont fait leurs preuves, des enseignements qui mènent quelque part.

## Ton défi
Éviter de réduire la spiritualité à ce qui est utile ou de rejeter les approches qui te semblent trop légères.

## Maison 9 en Capricorne
Tu explores les grandes questions avec sérieux et persévérance. L'enseignement ou les voyages te nourrissent s'ils servent ta progression.

## Micro-rituel du jour (2 min)
- Choisis une croyance qui te semble trop idéaliste
- Respire et cherche ce qu'elle pourrait t'apporter malgré tout
- Note une façon de l'explorer sans cynisme aujourd'hui""",

    ('capricorn', 11): """# ☀️ Soleil en Capricorne

**En une phrase :** Tu t'affirmes en structurant les projets collectifs et en apportant ta rigueur aux groupes.

## Ton moteur
Tu as besoin d'amitiés matures et de projets de groupe qui construisent quelque chose de durable. Tu es le pilier fiable de tes cercles.

## Ton défi
Éviter de prendre tout sur tes épaules ou de juger ceux qui s'engagent moins que toi.

## Maison 11 en Capricorne
Tes projets collectifs visent le long terme. Tu attires des amis sérieux et tu excelles à transformer les rêves en réalités concrètes.

## Micro-rituel du jour (2 min)
- Pense à un projet de groupe où tu portes beaucoup
- Respire et identifie une responsabilité que tu pourrais déléguer
- Note une façon de faire confiance aux autres aujourd'hui""",

    ('capricorn', 12): """# ☀️ Soleil en Capricorne

**En une phrase :** Tu puises ta force dans une discipline intérieure, une ambition secrète qui se construit loin des regards.

## Ton moteur
Ton identité se forge dans la solitude productive, le travail sur toi-même, une maturation lente et profonde.

## Ton défi
Éviter de t'isoler dans une austérité excessive ou de porter seul des fardeaux invisibles.

## Maison 12 en Capricorne
Ta spiritualité est celle de la structure intérieure. Tu as une force cachée considérable, à condition de ne pas t'enfermer dans ta forteresse.

## Micro-rituel du jour (2 min)
- Ferme les yeux et identifie un fardeau que tu portes seul
- Respire et visualise-toi le déposant un instant
- Note une façon d'alléger cette charge aujourd'hui""",

    # AQUARIUS
    ('aquarius', 9): """# ☀️ Soleil en Verseau

**En une phrase :** Tu t'affirmes en explorant des idées avant-gardistes et en remettant en question les vérités établies.

## Ton moteur
Ta quête de sens est intellectuelle et révolutionnaire. Tu cherches des philosophies qui libèrent, des visions du monde qui ouvrent de nouvelles possibilités.

## Ton défi
Éviter de rejeter systématiquement la tradition ou de t'isoler dans des théories que personne ne comprend.

## Maison 9 en Verseau
Tu explores les grandes questions avec originalité. L'enseignement ou les voyages te nourrissent s'ils élargissent ta vision de l'humanité.

## Micro-rituel du jour (2 min)
- Choisis une idée conventionnelle qui t'agace
- Respire et cherche ce qu'elle contient de valable
- Note une façon d'innover sans tout rejeter aujourd'hui""",

    ('aquarius', 11): """# ☀️ Soleil en Verseau

**En une phrase :** Tu t'affirmes en étant le visionnaire de tes cercles, celui qui porte les idées nouvelles et rassemble les esprits libres.

## Ton moteur
Tu es dans ton élément en maison 11. Amitiés atypiques, projets collectifs innovants, causes humanitaires nourrissent profondément ton identité.

## Ton défi
Éviter de te sentir supérieur aux autres ou de sacrifier les liens personnels au nom de l'idéal collectif.

## Maison 11 en Verseau
Double signature verseau : tu as un besoin vital de communauté libre. Tu attires des amis originaux et tu excelles à imaginer le monde de demain.

## Micro-rituel du jour (2 min)
- Pense à un ami très différent de toi
- Respire et apprécie cette différence comme une richesse
- Note une façon de célébrer la diversité aujourd'hui""",

    ('aquarius', 12): """# ☀️ Soleil en Verseau

**En une phrase :** Tu puises ta force dans une liberté intérieure radicale, une connexion avec l'humanité qui transcende les liens personnels.

## Ton moteur
Ton identité se ressource dans la solitude créative, la méditation sur l'avenir, une connexion avec le collectif qui dépasse l'ego.

## Ton défi
Éviter de te couper des émotions personnelles au nom d'idéaux abstraits.

## Maison 12 en Verseau
Ta spiritualité est celle de la liberté intérieure et de la conscience collective. Tu as accès à des intuitions pour l'humanité, à condition de rester humain.

## Micro-rituel du jour (2 min)
- Ferme les yeux et connecte-toi à l'humanité tout entière
- Respire et ressens ta place unique dans ce grand tout
- Note une façon de servir le collectif à ta manière aujourd'hui""",

    # PISCES
    ('pisces', 9): """# ☀️ Soleil en Poissons

**En une phrase :** Tu t'affirmes en explorant les dimensions spirituelles, artistiques et mystiques de l'existence.

## Ton moteur
Ta quête de sens est intuitive et transcendante. Tu cherches des philosophies qui parlent à l'âme, des vérités qui se ressentent plus qu'elles ne s'expliquent.

## Ton défi
Éviter de te perdre dans des croyances floues ou de fuir la réalité dans des rêveries spirituelles.

## Maison 9 en Poissons
Tu explores les grandes questions avec sensibilité. L'enseignement ou les voyages te nourrissent s'ils touchent au sacré et au poétique.

## Micro-rituel du jour (2 min)
- Choisis une intuition spirituelle que tu as du mal à formuler
- Respire et laisse-la exister sans chercher à l'expliquer
- Note une façon de lui faire confiance aujourd'hui""",

    ('pisces', 11): """# ☀️ Soleil en Poissons

**En une phrase :** Tu t'affirmes en apportant compassion et inspiration à tes cercles, en connectant les âmes au-delà des apparences.

## Ton moteur
Tu as besoin d'amitiés profondes et de projets collectifs qui servent une cause plus grande. Tu es le cœur sensible de tes groupes.

## Ton défi
Éviter de te dissoudre dans les besoins des autres ou de te sacrifier pour des causes qui ne te respectent pas.

## Maison 11 en Poissons
Tes projets de groupe ont une dimension spirituelle ou humanitaire. Tu attires des amis sensibles et tu excelles à créer des espaces de communion.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu donnes beaucoup
- Respire et vérifie que tu reçois aussi ce dont tu as besoin
- Note une limite saine à poser aujourd'hui""",

    ('pisces', 12): """# ☀️ Soleil en Poissons

**En une phrase :** Tu puises ta force dans l'océan intérieur, la connexion avec le tout, la dissolution des frontières de l'ego.

## Ton moteur
Tu es dans ton élément en maison 12. Méditation, art, compassion universelle, tout ce qui te connecte à l'infini nourrit profondément ton identité.

## Ton défi
Éviter de te perdre dans la confusion ou de fuir le monde dans des paradis artificiels.

## Maison 12 en Poissons
Double signature poissons : tu as un accès naturel au transcendant. Tu as des dons mystiques ou artistiques profonds, à condition de garder un pied sur terre.

## Micro-rituel du jour (2 min)
- Ferme les yeux et laisse-toi flotter dans ton espace intérieur
- Respire et ressens la paix de n'avoir rien à prouver
- Note une façon d'ancrer cette paix dans ta journée""",
}


async def update_interpretations():
    async with AsyncSessionLocal() as db:
        updated = 0
        for (sign, house), content in SUN_INTERPRETATIONS.items():
            result = await db.execute(
                update(PregeneratedNatalInterpretation)
                .where(
                    PregeneratedNatalInterpretation.subject == 'sun',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
                .values(content=content.strip(), length=len(content.strip()))
            )
            if result.rowcount > 0:
                updated += result.rowcount

        await db.commit()
        print(f"Done: {updated} sun interpretations updated")


if __name__ == '__main__':
    asyncio.run(update_interpretations())
