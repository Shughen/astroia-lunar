#!/usr/bin/env python3
"""
Script pour corriger les 96 interprétations MOON manquantes (maisons 2,3,5,6,8,9,11,12)
Format natal V2 avec: En une phrase / Ton moteur / Ton défi / Maison X / Micro-rituel
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import update
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Interprétations MOON format V2 - Maisons 2,3,5,6,8,9,11,12 pour les 12 signes
MOON_INTERPRETATIONS = {
    # ARIES
    ('aries', 2): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand tu peux conquérir tes ressources par toi-même, avec énergie et indépendance.

## Ton moteur
Tes besoins émotionnels passent par l'autonomie financière et matérielle. Tu as besoin de sentir que tu peux subvenir à tes besoins par tes propres moyens, rapidement et sans dépendre de personne.

## Ton défi
Éviter les dépenses impulsives ou les décisions financières trop rapides sous le coup de l'émotion. La patience dans la gestion de tes ressources n'est pas ton fort.

## Maison 2 en Bélier
Tu abordes l'argent et les possessions avec une énergie de conquête. Tes valeurs sont directes, ton rapport aux ressources est actif. Tu préfères gagner que recevoir.

## Micro-rituel du jour (2 min)
- Identifie un achat impulsif récent
- Respire et demande-toi : "Était-ce un besoin ou une réaction ?"
- Note une façon de canaliser ton énergie financière aujourd'hui""",

    ('aries', 3): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand tu peux t'exprimer spontanément et que tes idées sont entendues immédiatement.

## Ton moteur
Tes besoins émotionnels passent par la communication directe. Tu as besoin de dire ce que tu penses, d'être stimulé intellectuellement, d'échanger avec vivacité.

## Ton défi
Éviter de couper la parole ou de t'impatienter face à ceux qui réfléchissent plus lentement. Ton mental rapide peut blesser sans le vouloir.

## Maison 3 en Bélier
Tu communiques avec fougue et spontanéité. Tes échanges avec ton entourage proche sont dynamiques, parfois vifs. L'apprentissage te passionne quand il est actif.

## Micro-rituel du jour (2 min)
- Pense à une conversation où tu as été trop direct
- Respire et visualise une façon plus douce de dire la même chose
- Note une intention d'écoute pour aujourd'hui""",

    ('aries', 5): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand tu peux créer, jouer et t'exprimer avec passion et spontanéité.

## Ton moteur
Tes besoins émotionnels passent par la créativité active et les plaisirs immédiats. Tu as besoin de t'amuser, de prendre des initiatives ludiques, de vivre intensément.

## Ton défi
Éviter de transformer les loisirs en compétition ou de t'ennuyer trop vite. La patience dans les activités créatives peut te manquer.

## Maison 5 en Bélier
Tu abordes la créativité et les plaisirs avec énergie. Tes romances sont passionnées et directes. Avec les enfants, tu es stimulant mais parfois impatient.

## Micro-rituel du jour (2 min)
- Identifie une activité créative que tu as abandonnée trop vite
- Respire et reconnecte-toi à l'enthousiasme initial
- Note une façon de t'amuser sans compétition aujourd'hui""",

    ('aries', 6): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand ton quotidien est actif, dynamique et que tu peux résoudre les problèmes rapidement.

## Ton moteur
Tes besoins émotionnels passent par l'efficacité au travail et un corps en mouvement. Tu as besoin d'action dans ta routine, de défis quotidiens à relever.

## Ton défi
Éviter l'épuisement par hyperactivité ou l'impatience face aux tâches répétitives. Ton corps réagit vite au stress.

## Maison 6 en Bélier
Tu abordes le travail et la santé avec énergie. Ta routine a besoin de mouvement et de nouveauté. Tu es efficace mais parfois brusque avec tes collègues.

## Micro-rituel du jour (2 min)
- Identifie une tension physique liée au stress
- Respire profondément et bouge cette partie du corps
- Note une façon de ralentir dans ta routine aujourd'hui""",

    ('aries', 8): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand tu peux affronter les crises directement et transformer les obstacles en victoires.

## Ton moteur
Tes besoins émotionnels passent par l'intensité et la transformation active. Tu as besoin de pouvoir agir face aux épreuves, pas de subir passivement.

## Ton défi
Éviter de provoquer des crises par impatience ou de fuir l'intimité émotionnelle profonde. La vulnérabilité te met mal à l'aise.

## Maison 8 en Bélier
Tu abordes les transformations avec courage. Les ressources partagées, l'intimité profonde sont des terrains où tu veux agir, pas attendre.

## Micro-rituel du jour (2 min)
- Identifie une peur que tu évites d'affronter
- Respire et visualise-toi la regardant en face
- Note un petit pas courageux pour aujourd'hui""",

    ('aries', 9): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand tu explores de nouveaux horizons avec audace et que tu peux défendre tes convictions.

## Ton moteur
Tes besoins émotionnels passent par l'aventure et l'expansion. Tu as besoin de voyager, d'apprendre, de te sentir libre de découvrir le monde.

## Ton défi
Éviter d'imposer tes croyances ou de t'impatienter face à d'autres visions du monde. L'écoute philosophique n'est pas ton fort.

## Maison 9 en Bélier
Tu abordes les grandes questions avec passion. Les voyages, les études supérieures sont des aventures que tu veux vivre activement.

## Micro-rituel du jour (2 min)
- Choisis une croyance que tu défends avec fougue
- Respire et demande-toi : "Puis-je l'enrichir d'un autre point de vue ?"
- Note une ouverture possible aujourd'hui""",

    ('aries', 11): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand tu peux prendre l'initiative dans tes groupes et que tes amis te suivent.

## Ton moteur
Tes besoins émotionnels passent par le leadership social. Tu as besoin d'amis dynamiques, de projets collectifs où tu peux être moteur.

## Ton défi
Éviter de vouloir toujours mener le groupe ou de t'impatienter face aux décisions collectives lentes. Tout le monde n'a pas ton rythme.

## Maison 11 en Bélier
Tu abordes les amitiés et projets collectifs avec énergie. Tu initie, tu proposes, tu entraînes. Tes amis apprécient ton dynamisme s'il ne devient pas domination.

## Micro-rituel du jour (2 min)
- Pense à un ami qui avance à son propre rythme
- Respire et accepte ce tempo différent du tien
- Note une façon de soutenir sans pousser aujourd'hui""",

    ('aries', 12): """# 🌙 Lune en Bélier

**En une phrase :** Tu te sens en sécurité quand tu peux combattre tes démons intérieurs avec courage et transformer ta colère en force.

## Ton moteur
Tes besoins émotionnels passent par l'action intérieure. Tu as besoin de te battre pour ta paix, de transformer activement tes peurs en énergie.

## Ton défi
Éviter de retourner ta combativité contre toi-même ou de réprimer une colère qui a besoin de s'exprimer sainement.

## Maison 12 en Bélier
Tu abordes le monde intérieur avec courage. Ta spiritualité est active, tes retraites sont dynamiques. Attention à ne pas fuir dans l'hyperactivité pour éviter l'introspection.

## Micro-rituel du jour (2 min)
- Identifie une frustration que tu gardes pour toi
- Respire et donne-lui une forme (couleur, image)
- Note une action physique pour libérer cette énergie""",

    # TAURUS
    ('taurus', 2): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand tes ressources sont stables et que tu peux profiter des plaisirs matériels.

## Ton moteur
Tes besoins émotionnels passent par la stabilité financière. Tu as besoin de sentir que tu as assez, que tes possessions sont durables, que ton confort est assuré.

## Ton défi
Éviter l'attachement excessif aux biens matériels ou la peur du manque qui te pousse à accumuler. La sécurité ne vient pas que de l'avoir.

## Maison 2 en Taureau
Double signature taurine : tu as un besoin profond de sécurité matérielle. Tes valeurs sont solides, ton rapport à l'argent est prudent et sensuel.

## Micro-rituel du jour (2 min)
- Touche un objet que tu possèdes et qui te rassure
- Respire et ressens la gratitude pour ce que tu as déjà
- Note une façon de te sentir riche sans acheter aujourd'hui""",

    ('taurus', 3): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand tu peux réfléchir à ton rythme et que tes idées sont accueillies avec patience.

## Ton moteur
Tes besoins émotionnels passent par une communication posée. Tu as besoin de temps pour formuler tes pensées, d'échanges calmes et concrets.

## Ton défi
Éviter de t'entêter dans tes opinions ou de refuser les idées nouvelles par confort intellectuel. Ta pensée peut devenir rigide.

## Maison 3 en Taureau
Tu communiques avec lenteur et profondeur. Tes échanges avec l'entourage sont stables mais peuvent manquer de spontanéité. Tu apprends mieux par la pratique.

## Micro-rituel du jour (2 min)
- Pense à une idée nouvelle que tu as rejetée trop vite
- Respire et donne-lui une chance d'exister
- Note une conversation à avoir sans te presser aujourd'hui""",

    ('taurus', 5): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand tu peux créer quelque chose de beau et de durable, et savourer les plaisirs simples.

## Ton moteur
Tes besoins émotionnels passent par la créativité sensorielle. Tu as besoin de toucher, de fabriquer, de profiter des plaisirs terrestres avec lenteur.

## Ton défi
Éviter de rester dans ta zone de confort créative ou de confondre plaisir et excès. La gourmandise peut devenir un refuge émotionnel.

## Maison 5 en Taureau
Tu abordes la créativité et les plaisirs avec sensualité. Tes romances sont lentes à démarrer mais profondes. Avec les enfants, tu es patient et affectueux.

## Micro-rituel du jour (2 min)
- Choisis un plaisir simple que tu pourrais savourer aujourd'hui
- Respire et engage-toi à le vivre pleinement, sans culpabilité
- Note une création à faire avec tes mains""",

    ('taurus', 6): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand ta routine est stable, prévisible et que ton corps est bien traité.

## Ton moteur
Tes besoins émotionnels passent par un quotidien régulier. Tu as besoin de rituels, de repas à heures fixes, d'un environnement de travail confortable.

## Ton défi
Éviter de t'enliser dans une routine trop rigide ou de résister aux changements nécessaires dans ton quotidien.

## Maison 6 en Taureau
Tu abordes le travail et la santé avec constance. Ta routine est ton ancre, ton corps a besoin de régularité. Tu es fiable mais parfois trop lent à t'adapter.

## Micro-rituel du jour (2 min)
- Identifie un petit changement bénéfique que tu repousses
- Respire et visualise-toi l'intégrant doucement
- Note un premier pas minuscule pour aujourd'hui""",

    ('taurus', 8): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand tu peux traverser les crises à ton rythme et que personne ne te pousse à changer trop vite.

## Ton moteur
Tes besoins émotionnels passent par la stabilité même dans les transformations. Tu as besoin de temps pour digérer les changements profonds.

## Ton défi
Éviter de résister aux transformations nécessaires par peur de perdre ta sécurité. Le lâcher-prise est ton grand apprentissage.

## Maison 8 en Taureau
Tu abordes les crises avec lenteur et obstination. Les ressources partagées te demandent confiance. L'intimité profonde se construit pierre par pierre.

## Micro-rituel du jour (2 min)
- Identifie quelque chose que tu devrais lâcher
- Respire et visualise-toi le déposant doucement
- Note un micro-lâcher-prise possible aujourd'hui""",

    ('taurus', 9): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand ta philosophie de vie est concrète et que tes croyances ont fait leurs preuves.

## Ton moteur
Tes besoins émotionnels passent par une sagesse pratique. Tu as besoin de croyances qui s'incarnent, de voyages qui nourrissent les sens.

## Ton défi
Éviter de t'enfermer dans des certitudes confortables ou de rejeter les idées qui bousculent tes convictions établies.

## Maison 9 en Taureau
Tu abordes les grandes questions avec pragmatisme. Tes voyages sont sensoriels, ta philosophie est terrestre. Tu cherches une vérité qui se touche.

## Micro-rituel du jour (2 min)
- Choisis une croyance qui te sécurise
- Respire et demande-toi : "M'ouvre-t-elle ou me limite-t-elle ?"
- Note une petite ouverture possible aujourd'hui""",

    ('taurus', 11): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand tes amitiés sont durables et que les projets collectifs avancent à un rythme stable.

## Ton moteur
Tes besoins émotionnels passent par la fidélité en amitié. Tu as besoin de liens solides, de groupes stables, de projets qui construisent dans le temps.

## Ton défi
Éviter de t'accrocher à des amitiés qui ne te correspondent plus ou de résister aux évolutions naturelles de tes cercles.

## Maison 11 en Taureau
Tu abordes les amitiés avec loyauté et constance. Tes projets de groupe visent le concret et le durable. Tu es l'ancre fiable de tes cercles.

## Micro-rituel du jour (2 min)
- Pense à une amitié ancienne qui t'apporte de la stabilité
- Respire et ressens la gratitude pour cette présence
- Note une façon de nourrir ce lien aujourd'hui""",

    ('taurus', 12): """# 🌙 Lune en Taureau

**En une phrase :** Tu te sens en sécurité quand tu peux te retirer dans un cocon sensoriel et te reconnecter à la nature.

## Ton moteur
Tes besoins émotionnels passent par la solitude confortable. Tu as besoin de temps seul dans un environnement doux, naturel, rassurant.

## Ton défi
Éviter de fuir dans le confort matériel pour éviter l'introspection profonde. Le cocon peut devenir une prison dorée.

## Maison 12 en Taureau
Tu abordes le monde intérieur avec les sens. Ta spiritualité est incarnée, ta méditation passe par le corps. Veille à ne pas t'endormir dans le confort.

## Micro-rituel du jour (2 min)
- Trouve un moment de silence et touche quelque chose de naturel
- Respire en ressentant la texture, la température
- Note ce que ce contact t'apprend sur toi""",

    # GEMINI
    ('gemini', 2): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand tu as plusieurs sources de revenus et que tes idées peuvent se monnayer.

## Ton moteur
Tes besoins émotionnels passent par la diversité financière. Tu as besoin de flexibilité dans tes ressources, de pouvoir gagner ta vie par l'intellect.

## Ton défi
Éviter l'éparpillement financier ou les décisions d'argent trop légères. Ta curiosité peut te faire changer d'avis trop souvent.

## Maison 2 en Gémeaux
Tu abordes l'argent avec légèreté et adaptabilité. Tes valeurs sont multiples, ton rapport aux possessions est peu attaché. Tu préfères la mobilité à l'accumulation.

## Micro-rituel du jour (2 min)
- Identifie une dépense légère que tu regrettes
- Respire et demande-toi ce qu'elle révèle de tes besoins
- Note une façon de valoriser tes idées aujourd'hui""",

    ('gemini', 3): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand tu peux parler, échanger, apprendre et que ton esprit est stimulé.

## Ton moteur
Tu es dans ton élément en maison 3. Communication, curiosité, échanges avec l'entourage proche nourrissent profondément tes besoins émotionnels.

## Ton défi
Éviter de te disperser dans trop de conversations ou de fuir les émotions profondes dans le bavardage. Le silence t'angoisse parfois.

## Maison 3 en Gémeaux
Double signature géminienne : tu as un besoin vital de communiquer. Ton esprit est vif, tes échanges multiples. Tu apprends en parlant.

## Micro-rituel du jour (2 min)
- Choisis un moment de silence intentionnel
- Respire et observe les pensées sans les suivre
- Note une conversation de qualité à avoir aujourd'hui""",

    ('gemini', 5): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand tu peux jouer avec les mots, les idées, et que la créativité est légère et variée.

## Ton moteur
Tes besoins émotionnels passent par la créativité intellectuelle. Tu as besoin de jeux d'esprit, de flirts légers, d'activités ludiques stimulantes.

## Ton défi
Éviter de papillonner dans les plaisirs ou de fuir l'engagement créatif profond. Ta légèreté peut manquer de profondeur.

## Maison 5 en Gémeaux
Tu abordes la créativité avec curiosité et versatilité. Tes romances sont légères et communicatives. Avec les enfants, tu es joueur et stimulant intellectuellement.

## Micro-rituel du jour (2 min)
- Choisis une activité créative que tu pourrais approfondir
- Respire et engage-toi à rester plus longtemps qu'à l'habitude
- Note un jeu d'esprit à partager aujourd'hui""",

    ('gemini', 6): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand ton quotidien est varié et que tu peux faire plusieurs choses à la fois.

## Ton moteur
Tes besoins émotionnels passent par la diversité dans la routine. Tu as besoin de tâches variées, d'un environnement de travail stimulant, de mouvement mental.

## Ton défi
Éviter la dispersion dans le travail quotidien ou le stress lié au multitasking excessif. Ton système nerveux est sensible.

## Maison 6 en Gémeaux
Tu abordes le travail avec adaptabilité et curiosité. Ta routine a besoin de variété, ta santé passe par le mental. Tu excelles dans les métiers de communication.

## Micro-rituel du jour (2 min)
- Identifie une tâche que tu repousses par ennui
- Respire et trouve une façon de la rendre plus intéressante
- Note une routine à simplifier aujourd'hui""",

    ('gemini', 8): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand tu peux comprendre et analyser les crises plutôt que de les subir émotionnellement.

## Ton moteur
Tes besoins émotionnels passent par la compréhension des transformations. Tu as besoin de mettre des mots sur l'intensité, d'intellectualiser le profond.

## Ton défi
Éviter de fuir les émotions profondes dans l'analyse ou de rester en surface face aux vrais enjeux. Le mental ne peut pas tout résoudre.

## Maison 8 en Gémeaux
Tu abordes les crises avec curiosité et verbalisation. L'intimité profonde passe par la parole. Tu as besoin de comprendre avant de ressentir.

## Micro-rituel du jour (2 min)
- Identifie une émotion profonde que tu rationalises
- Respire et laisse-la exister sans l'expliquer
- Note une façon de ressentir avant de penser aujourd'hui""",

    ('gemini', 9): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand tu peux explorer plusieurs philosophies et que ta curiosité spirituelle est nourrie.

## Ton moteur
Tes besoins émotionnels passent par l'apprentissage permanent. Tu as besoin de voyager mentalement, de comparer les idées, d'apprendre toujours.

## Ton défi
Éviter de survoler les grandes questions ou de collectionner les savoirs sans les approfondir. La sagesse demande de la persévérance.

## Maison 9 en Gémeaux
Tu abordes les grandes questions avec légèreté et curiosité. Tes voyages sont courts et multiples, ta philosophie est ouverte et changeante.

## Micro-rituel du jour (2 min)
- Choisis un sujet que tu survoles depuis longtemps
- Respire et engage-toi à l'approfondir aujourd'hui
- Note une question précise à explorer""",

    ('gemini', 11): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand tu peux connecter les gens, faire circuler les idées et avoir des amitiés stimulantes.

## Ton moteur
Tes besoins émotionnels passent par le réseau social actif. Tu as besoin d'amis variés, de conversations multiples, de projets de groupe intellectuels.

## Ton défi
Éviter les relations superficielles ou de t'éparpiller dans trop de cercles. La profondeur amicale demande du temps.

## Maison 11 en Gémeaux
Tu abordes les amitiés avec légèreté et curiosité. Tu connectes les gens, tu fais circuler l'information. Tu es le messager de tes cercles.

## Micro-rituel du jour (2 min)
- Pense à une amitié que tu pourrais approfondir
- Respire et visualise une conversation plus intime
- Note un ami à qui donner plus de ton temps aujourd'hui""",

    ('gemini', 12): """# 🌙 Lune en Gémeaux

**En une phrase :** Tu te sens en sécurité quand tu peux dialoguer avec toi-même, écrire tes pensées et explorer ton monde intérieur par les mots.

## Ton moteur
Tes besoins émotionnels passent par l'introspection verbale. Tu as besoin d'écrire, de te parler, de comprendre ton inconscient par le langage.

## Ton défi
Éviter de te perdre dans un mental hyperactif qui tourne à vide. Le bavardage intérieur peut devenir épuisant.

## Maison 12 en Gémeaux
Tu abordes le monde intérieur avec les mots. Ta spiritualité est intellectuelle, tes rêves sont narratifs. Veille à ne pas fuir le silence.

## Micro-rituel du jour (2 min)
- Écris trois pensées qui tournent dans ta tête
- Respire et observe-les sans les suivre
- Note celle qui mérite vraiment ton attention""",

    # CANCER
    ('cancer', 2): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand tes ressources te permettent de prendre soin de toi et des tiens.

## Ton moteur
Tes besoins émotionnels passent par la sécurité matérielle familiale. Tu as besoin de sentir que tu peux nourrir, protéger, créer un foyer stable.

## Ton défi
Éviter d'accumuler par peur du manque ou de lier ta valeur personnelle à ce que tu possèdes. L'attachement émotionnel aux objets peut être excessif.

## Maison 2 en Cancer
Tu abordes l'argent avec sensibilité et prudence. Tes valeurs sont liées à la famille, tes possessions ont une charge émotionnelle. Tu gardes précieusement.

## Micro-rituel du jour (2 min)
- Touche un objet qui te relie à ta famille
- Respire et ressens la sécurité qu'il t'apporte
- Note une façon de te sentir riche en liens aujourd'hui""",

    ('cancer', 3): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand tu peux communiquer avec ton cœur et que ton entourage proche te comprend émotionnellement.

## Ton moteur
Tes besoins émotionnels passent par une communication intime. Tu as besoin d'échanger sur ce que tu ressens, d'avoir des conversations nourrissantes.

## Ton défi
Éviter de te refermer si tu te sens incompris ou de communiquer uniquement quand tu es émotionnellement submergé.

## Maison 3 en Cancer
Tu communiques avec sensibilité et intuition. Tes échanges avec l'entourage proche sont émotionnels. Tu apprends mieux dans un environnement chaleureux.

## Micro-rituel du jour (2 min)
- Pense à quelqu'un à qui tu voudrais exprimer ce que tu ressens
- Respire et trouve les mots du cœur
- Note une conversation émotionnelle à avoir aujourd'hui""",

    ('cancer', 5): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand tu peux créer dans un cocon protégé et exprimer tes émotions artistiquement.

## Ton moteur
Tes besoins émotionnels passent par la créativité intime. Tu as besoin de créer pour exprimer ce que tu ressens, de plaisirs partagés en petit comité.

## Ton défi
Éviter de te replier dans ta bulle créative ou de trop protéger tes œuvres. Partager ta sensibilité est ta force.

## Maison 5 en Cancer
Tu abordes la créativité avec émotion et intimité. Tes romances sont profondes et maternantes/paternantes. Avec les enfants, tu es très protecteur.

## Micro-rituel du jour (2 min)
- Choisis une émotion que tu pourrais exprimer créativement
- Respire et visualise une forme artistique pour elle
- Note une création à faire pour quelqu'un que tu aimes""",

    ('cancer', 6): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand ton quotidien est douillet et que tu peux prendre soin des autres au travail.

## Ton moteur
Tes besoins émotionnels passent par un environnement de travail chaleureux. Tu as besoin de te sentir utile émotionnellement, de nourrir les autres au quotidien.

## Ton défi
Éviter de trop materner tes collègues ou de négliger ta santé quand tu es stressé émotionnellement.

## Maison 6 en Cancer
Tu abordes le travail avec sensibilité et soin. Ta routine a besoin de chaleur humaine, ta santé est liée à tes émotions. Tu excelles dans les métiers du care.

## Micro-rituel du jour (2 min)
- Identifie comment tu te sens dans ton corps en ce moment
- Respire et envoie de la douceur à la zone tendue
- Note une façon de prendre soin de toi au travail aujourd'hui""",

    ('cancer', 8): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand tu peux traverser les crises dans les bras de quelqu'un qui t'aime.

## Ton moteur
Tes besoins émotionnels passent par l'intimité protectrice. Tu as besoin de liens profonds qui te sécurisent dans les transformations.

## Ton défi
Éviter de t'accrocher excessivement aux autres dans les crises ou de fuir les changements qui menacent ta sécurité émotionnelle.

## Maison 8 en Cancer
Tu abordes les transformations avec sensibilité. L'intimité profonde est ton refuge, les ressources partagées sont liées à la confiance émotionnelle.

## Micro-rituel du jour (2 min)
- Pense à quelqu'un en qui tu as une confiance absolue
- Respire et ressens le soutien de ce lien
- Note une façon de t'appuyer sur cette personne aujourd'hui""",

    ('cancer', 9): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand ta philosophie de vie honore les émotions et les racines.

## Ton moteur
Tes besoins émotionnels passent par une sagesse du cœur. Tu as besoin de croyances qui nourrissent, de voyages qui te reconnectent à tes origines.

## Ton défi
Éviter de t'enfermer dans une vision trop sentimentale du monde ou de rejeter les idées qui ne touchent pas ton cœur.

## Maison 9 en Cancer
Tu abordes les grandes questions avec ton cœur. Tes voyages sont des retours aux sources, ta philosophie honore la mémoire et l'émotion.

## Micro-rituel du jour (2 min)
- Pense à une sagesse transmise par ta famille
- Respire et ressens comment elle vit en toi
- Note une façon de l'honorer aujourd'hui""",

    ('cancer', 11): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand tes amis sont comme une famille et que les projets collectifs prennent soin de chacun.

## Ton moteur
Tes besoins émotionnels passent par des amitiés profondes et familiales. Tu as besoin de cercles chaleureux, de projets qui nourrissent le cœur.

## Ton défi
Éviter de materner excessivement tes amis ou de te replier si tu ne te sens pas assez accueilli.

## Maison 11 en Cancer
Tu abordes les amitiés avec tendresse et protection. Tes projets de groupe ont une dimension familiale. Tu crées des espaces où chacun se sent chez soi.

## Micro-rituel du jour (2 min)
- Pense à un ami qui aurait besoin de soutien
- Respire et envoie-lui mentalement de la chaleur
- Note un geste d'attention pour aujourd'hui""",

    ('cancer', 12): """# 🌙 Lune en Cancer

**En une phrase :** Tu te sens en sécurité quand tu peux te retirer dans ton monde intérieur et te connecter à tes souvenirs.

## Ton moteur
Tes besoins émotionnels passent par la solitude nourrissante. Tu as besoin de temps seul pour digérer tes émotions, te reconnecter à tes racines intérieures.

## Ton défi
Éviter de te noyer dans la nostalgie ou de fuir le présent dans un passé idéalisé. La mélancolie peut devenir une prison.

## Maison 12 en Cancer
Tu abordes le monde intérieur avec sensibilité. Ta spiritualité est celle du cœur et de la mémoire. Veille à ne pas t'isoler dans une bulle trop douce.

## Micro-rituel du jour (2 min)
- Ferme les yeux et pense à un souvenir heureux
- Respire et laisse-le t'envelopper de douceur
- Note comment tu peux apporter cette chaleur dans ta journée""",

    # LEO
    ('leo', 2): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tes ressources te permettent de vivre généreusement et de briller.

## Ton moteur
Tes besoins émotionnels passent par l'abondance visible. Tu as besoin de pouvoir donner, offrir, vivre avec panache grâce à tes moyens.

## Ton défi
Éviter les dépenses ostentatoires ou de lier ta valeur personnelle à ta capacité à impressionner matériellement.

## Maison 2 en Lion
Tu abordes l'argent avec fierté et générosité. Tes valeurs sont nobles, tes possessions reflètent ton identité. Tu aimes que tes ressources brillent.

## Micro-rituel du jour (2 min)
- Identifie un achat récent motivé par l'image
- Respire et demande-toi ce qu'il cache comme besoin
- Note une façon de te sentir riche intérieurement aujourd'hui""",

    ('leo', 3): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tu peux t'exprimer avec éclat et que tes paroles sont admirées.

## Ton moteur
Tes besoins émotionnels passent par une communication expressive. Tu as besoin que tes idées soient reconnues, que ta façon de parler marque les esprits.

## Ton défi
Éviter de monopoliser la parole ou de souffrir si tes idées ne reçoivent pas l'attention espérée.

## Maison 3 en Lion
Tu communiques avec chaleur et théâtralité. Tes échanges avec l'entourage sont généreux mais tu as besoin d'être le centre. Tu apprends en étant valorisé.

## Micro-rituel du jour (2 min)
- Pense à une conversation où tu as trop parlé de toi
- Respire et visualise un échange où tu écoutes vraiment
- Note une question à poser à quelqu'un aujourd'hui""",

    ('leo', 5): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tu peux créer, jouer et recevoir de l'admiration pour ton expression personnelle.

## Ton moteur
Tu es dans ton élément en maison 5. Créativité, jeu, romance, expression personnelle nourrissent profondément tes besoins émotionnels.

## Ton défi
Éviter de transformer les loisirs en performance ou de souffrir si ton talent n'est pas reconnu. Crée aussi pour toi-même.

## Maison 5 en Lion
Double signature léonine : tu as un besoin vital de briller par ta créativité. Tes romances sont passionnées et dramatiques. Tu es un parent fier et généreux.

## Micro-rituel du jour (2 min)
- Choisis une création que personne ne verra
- Respire et fais-la juste pour le plaisir
- Note une façon de jouer sans public aujourd'hui""",

    ('leo', 6): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tu peux briller dans ton quotidien et que ton travail est valorisé.

## Ton moteur
Tes besoins émotionnels passent par la reconnaissance au travail. Tu as besoin que tes efforts quotidiens soient vus et appréciés.

## Ton défi
Éviter de vouloir être le centre au bureau ou de négliger les tâches ordinaires qui ne te font pas briller.

## Maison 6 en Lion
Tu abordes le travail avec fierté et générosité. Ta routine a besoin de moments de lumière, ta santé passe par la joie. Tu veux exceller dans ce que tu fais.

## Micro-rituel du jour (2 min)
- Identifie une tâche ordinaire que tu négliges
- Respire et trouve une façon d'y mettre ta touche personnelle
- Note une reconnaissance à offrir à un collègue""",

    ('leo', 8): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tu peux traverser les crises avec dignité et en ressortir grandi.

## Ton moteur
Tes besoins émotionnels passent par une transformation héroïque. Tu as besoin de sentir que les épreuves te rendent plus fort, pas plus petit.

## Ton défi
Éviter de dramatiser les crises ou de refuser l'aide par orgueil. La vulnérabilité n'est pas une faiblesse.

## Maison 8 en Lion
Tu abordes les transformations avec courage et fierté. L'intimité profonde te demande de montrer ta vulnérabilité, ce qui est ton défi.

## Micro-rituel du jour (2 min)
- Identifie une faiblesse que tu caches par orgueil
- Respire et accepte qu'elle fait partie de toi
- Note une façon de demander de l'aide aujourd'hui""",

    ('leo', 9): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tu peux partager ta vision du monde avec générosité et inspirer les autres.

## Ton moteur
Tes besoins émotionnels passent par le rayonnement philosophique. Tu as besoin d'enseigner, de transmettre, de voir tes croyances admirées.

## Ton défi
Éviter de transformer ta philosophie en spectacle ou de croire que ta vision est la seule valable.

## Maison 9 en Lion
Tu abordes les grandes questions avec panache. Tes voyages sont royaux, ton enseignement est généreux. Tu veux inspirer par ta sagesse.

## Micro-rituel du jour (2 min)
- Pense à une conviction que tu aimerais transmettre
- Respire et demande-toi : "Comment la partager avec humilité ?"
- Note une façon d'inspirer sans imposer aujourd'hui""",

    ('leo', 11): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tu es le cœur vibrant de tes cercles et que tes amis t'admirent.

## Ton moteur
Tes besoins émotionnels passent par le leadership social. Tu as besoin de briller parmi tes amis, de fédérer, d'être reconnu comme généreux et inspirant.

## Ton défi
Éviter de monopoliser l'attention dans les groupes ou de souffrir si d'autres brillent aussi.

## Maison 11 en Lion
Tu abordes les amitiés avec chaleur et générosité. Tes projets de groupe portent ta marque. Tu es le soleil de tes cercles, à condition de laisser les autres briller aussi.

## Micro-rituel du jour (2 min)
- Pense à un ami dont tu admires une qualité
- Respire et ressens la joie de le voir briller
- Note une façon de célébrer quelqu'un d'autre aujourd'hui""",

    ('leo', 12): """# 🌙 Lune en Lion

**En une phrase :** Tu te sens en sécurité quand tu peux cultiver une lumière intérieure qui ne dépend pas des applaudissements.

## Ton moteur
Tes besoins émotionnels passent par une dignité secrète. Tu as besoin de savoir que tu brilles même quand personne ne regarde.

## Ton défi
Éviter de cacher ta lumière par fausse modestie ou de t'éteindre dans l'ombre. Tu mérites de rayonner aussi à l'extérieur.

## Maison 12 en Lion
Tu abordes le monde intérieur avec fierté et créativité. Ta spiritualité est celle du cœur rayonnant. Veille à ne pas t'isoler dans une tour dorée.

## Micro-rituel du jour (2 min)
- Ferme les yeux et visualise une flamme au centre de ton cœur
- Respire en la laissant grandir sans public
- Note une création à faire juste pour toi aujourd'hui""",

    # VIRGO
    ('virgo', 2): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand tes finances sont en ordre et que tu gères tes ressources avec méthode.

## Ton moteur
Tes besoins émotionnels passent par la gestion rigoureuse. Tu as besoin de savoir exactement ce que tu as, de budgets clairs, d'une organisation financière impeccable.

## Ton défi
Éviter l'anxiété liée à l'argent ou de te priver excessivement par peur du manque. La perfection budgétaire n'existe pas.

## Maison 2 en Vierge
Tu abordes l'argent avec analyse et prudence. Tes valeurs sont pratiques, tes possessions sont utiles. Tu préfères la qualité à la quantité.

## Micro-rituel du jour (2 min)
- Identifie une inquiétude financière récurrente
- Respire et demande-toi si elle est réaliste
- Note une action concrète pour te rassurer aujourd'hui""",

    ('virgo', 3): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand tu peux t'exprimer avec précision et que tes idées sont utiles.

## Ton moteur
Tes besoins émotionnels passent par une communication claire et ordonnée. Tu as besoin que tes paroles servent à quelque chose, que tes analyses soient appréciées.

## Ton défi
Éviter la critique excessive dans tes échanges ou de te sentir incompris quand les autres sont moins précis que toi.

## Maison 3 en Vierge
Tu communiques avec méthode et discernement. Tes échanges avec l'entourage sont pratiques. Tu apprends en analysant.

## Micro-rituel du jour (2 min)
- Pense à une critique que tu as formulée récemment
- Respire et transforme-la en suggestion constructive
- Note une façon d'encourager quelqu'un aujourd'hui""",

    ('virgo', 5): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand ta créativité est utile et perfectionnée.

## Ton moteur
Tes besoins émotionnels passent par la création méticuleuse. Tu as besoin de peaufiner tes œuvres, que tes loisirs aient un sens pratique.

## Ton défi
Éviter de bloquer ta créativité par perfectionnisme ou de critiquer tes propres créations avant qu'elles ne soient finies.

## Maison 5 en Vierge
Tu abordes la créativité avec méthode et discernement. Tes romances sont prudentes et analytiques. Avec les enfants, tu es attentif aux détails.

## Micro-rituel du jour (2 min)
- Choisis une création imparfaite et assume-la
- Respire et laisse-la exister sans la corriger
- Note un plaisir à prendre sans le perfectionner""",

    ('virgo', 6): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand ta routine est ordonnée et que tu peux améliorer les choses au quotidien.

## Ton moteur
Tu es dans ton élément en maison 6. Organisation, service, santé, amélioration continue nourrissent profondément tes besoins émotionnels.

## Ton défi
Éviter l'obsession du contrôle dans ta routine ou l'autocritique sur ta santé et ton travail.

## Maison 6 en Vierge
Double signature virginienne : tu as un besoin vital d'ordre et d'utilité. Ta routine est méticuleuse, ta santé est surveillée. Tu excelles dans le service.

## Micro-rituel du jour (2 min)
- Identifie une imperfection que tu pourrais accepter
- Respire et laisse-la exister sans la corriger
- Note une façon de te féliciter pour ce que tu fais bien""",

    ('virgo', 8): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand tu peux analyser les crises et trouver des solutions pratiques aux transformations.

## Ton moteur
Tes besoins émotionnels passent par la compréhension des processus profonds. Tu as besoin de disséquer, d'analyser, de trouver un sens pratique aux épreuves.

## Ton défi
Éviter de rationaliser les émotions intenses ou de chercher la perfection dans les processus de transformation.

## Maison 8 en Vierge
Tu abordes les transformations avec méthode et discernement. L'intimité profonde te demande d'accepter le chaos émotionnel.

## Micro-rituel du jour (2 min)
- Identifie une émotion intense que tu essaies d'analyser
- Respire et laisse-la exister sans la comprendre
- Note une façon d'accueillir le mystère aujourd'hui""",

    ('virgo', 9): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand ta philosophie de vie est pratique et applicable au quotidien.

## Ton moteur
Tes besoins émotionnels passent par une sagesse concrète. Tu as besoin de croyances qui marchent, d'enseignements qui s'appliquent.

## Ton défi
Éviter de réduire les grandes questions à leur utilité ou de critiquer les philosophies qui ne te semblent pas pratiques.

## Maison 9 en Vierge
Tu abordes les grandes questions avec discernement. Tes voyages sont organisés, ta philosophie est terre-à-terre.

## Micro-rituel du jour (2 min)
- Choisis une croyance qui te semble trop abstraite
- Respire et cherche un fil pratique pour la saisir
- Note une sagesse à appliquer concrètement aujourd'hui""",

    ('virgo', 11): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand tu peux être utile à tes amis et contribuer concrètement aux projets collectifs.

## Ton moteur
Tes besoins émotionnels passent par le service amical. Tu as besoin d'aider tes amis de façon pratique, de projets de groupe bien organisés.

## Ton défi
Éviter de te cantonner au rôle de celui qui aide ou de critiquer l'organisation des autres.

## Maison 11 en Vierge
Tu abordes les amitiés avec discernement et service. Tes projets de groupe sont méthodiques. Tu es le détail qui fait la différence.

## Micro-rituel du jour (2 min)
- Pense à un ami à qui tu pourrais demander de l'aide
- Respire et accepte de recevoir autant que de donner
- Note une demande simple à faire aujourd'hui""",

    ('virgo', 12): """# 🌙 Lune en Vierge

**En une phrase :** Tu te sens en sécurité quand tu peux analyser ton monde intérieur et améliorer ta vie spirituelle.

## Ton moteur
Tes besoins émotionnels passent par l'introspection méthodique. Tu as besoin de comprendre tes mécanismes cachés, d'ordonner ton inconscient.

## Ton défi
Éviter l'autocritique excessive dans ton monde intérieur ou de vouloir perfectionner jusqu'à ta vie spirituelle.

## Maison 12 en Vierge
Tu abordes le monde intérieur avec analyse et discernement. Ta spiritualité est pratique, ton inconscient est scruté. Veille à accueillir aussi le mystère.

## Micro-rituel du jour (2 min)
- Identifie une zone de toi que tu essaies de perfectionner
- Respire et accepte-la telle qu'elle est
- Note une imperfection intérieure à accueillir aujourd'hui""",

    # LIBRA
    ('libra', 2): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand tes ressources te permettent de vivre dans la beauté et l'harmonie.

## Ton moteur
Tes besoins émotionnels passent par l'esthétique matérielle. Tu as besoin d'un environnement beau, de possessions élégantes, d'un équilibre financier.

## Ton défi
Éviter les dépenses excessives pour l'esthétique ou l'indécision face aux choix financiers.

## Maison 2 en Balance
Tu abordes l'argent avec goût et diplomatie. Tes valeurs sont liées à l'harmonie, tes possessions doivent être belles. Tu cherches l'équilibre dans tes ressources.

## Micro-rituel du jour (2 min)
- Identifie un achat récent motivé uniquement par l'esthétique
- Respire et demande-toi s'il t'apporte vraiment de la paix
- Note une façon de créer de la beauté sans acheter""",

    ('libra', 3): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand tu peux t'exprimer avec diplomatie et que tes échanges sont harmonieux.

## Ton moteur
Tes besoins émotionnels passent par une communication équilibrée. Tu as besoin de dialogues respectueux, d'échanges où chacun a sa place.

## Ton défi
Éviter de taire tes opinions pour maintenir la paix ou de ne jamais trancher dans tes communications.

## Maison 3 en Balance
Tu communiques avec grâce et diplomatie. Tes échanges avec l'entourage cherchent l'harmonie. Tu apprends mieux en binôme.

## Micro-rituel du jour (2 min)
- Pense à une opinion que tu n'as pas osé exprimer
- Respire et trouve une façon élégante de la dire
- Note une position à affirmer aujourd'hui""",

    ('libra', 5): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand ta créativité est élégante et que tes plaisirs sont partagés.

## Ton moteur
Tes besoins émotionnels passent par la création harmonieuse. Tu as besoin de beauté dans tes loisirs, de romances raffinées, de plaisirs esthétiques.

## Ton défi
Éviter de sacrifier ta créativité pour plaire ou de dépendre de l'autre pour t'amuser.

## Maison 5 en Balance
Tu abordes la créativité avec goût et équilibre. Tes romances sont élégantes et diplomatiques. Avec les enfants, tu cherches la paix.

## Micro-rituel du jour (2 min)
- Choisis une création qui te plaît vraiment, même si elle déplaît
- Respire et assume ton goût personnel
- Note un plaisir à prendre seul aujourd'hui""",

    ('libra', 6): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand ton quotidien est harmonieux et que les relations de travail sont équilibrées.

## Ton moteur
Tes besoins émotionnels passent par un environnement de travail agréable. Tu as besoin de collègues respectueux, d'un cadre esthétique, de routines équilibrées.

## Ton défi
Éviter de tout faire pour maintenir l'harmonie au travail ou de négliger ta santé par indécision.

## Maison 6 en Balance
Tu abordes le travail avec diplomatie et souci de l'harmonie. Ta routine a besoin de beauté, ta santé passe par l'équilibre. Tu excelles en collaboration.

## Micro-rituel du jour (2 min)
- Identifie un déséquilibre dans ta routine
- Respire et choisis une action pour le corriger
- Note une décision à prendre sans trop peser""",

    ('libra', 8): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand tu peux traverser les crises en maintenant l'harmonie relationnelle.

## Ton moteur
Tes besoins émotionnels passent par l'équilibre dans l'intensité. Tu as besoin de vivre les transformations à deux, de trouver la beauté même dans les épreuves.

## Ton défi
Éviter de fuir les conflits nécessaires ou de rester dans des relations déséquilibrées par peur de la rupture.

## Maison 8 en Balance
Tu abordes les transformations avec diplomatie. L'intimité profonde te demande de l'équilibre, les ressources partagées doivent être équitables.

## Micro-rituel du jour (2 min)
- Identifie un déséquilibre que tu tolères par peur du conflit
- Respire et visualise une façon de le nommer avec tact
- Note une limite à poser aujourd'hui""",

    ('libra', 9): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand ta philosophie de vie intègre tous les points de vue avec équité.

## Ton moteur
Tes besoins émotionnels passent par une sagesse équilibrée. Tu as besoin de comprendre toutes les perspectives, de trouver une harmonie entre les croyances.

## Ton défi
Éviter l'indécision philosophique ou de ne jamais t'engager dans une vision du monde par peur d'exclure.

## Maison 9 en Balance
Tu abordes les grandes questions avec diplomatie. Tes voyages sont esthétiques, ta philosophie cherche la beauté.

## Micro-rituel du jour (2 min)
- Choisis un débat où tu as du mal à trancher
- Respire et identifie ta vraie position
- Note une conviction à assumer aujourd'hui""",

    ('libra', 11): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand tes amitiés sont harmonieuses et que les projets collectifs sont équitables.

## Ton moteur
Tes besoins émotionnels passent par l'harmonie sociale. Tu as besoin d'amis raffinés, de cercles où règne la diplomatie, de projets équilibrés.

## Ton défi
Éviter de t'effacer pour maintenir la paix dans le groupe ou de fuir les amitiés qui demandent de trancher.

## Maison 11 en Balance
Tu abordes les amitiés avec grâce et souci de l'équité. Tes projets de groupe cherchent l'harmonie. Tu es le diplomate de tes cercles.

## Micro-rituel du jour (2 min)
- Pense à un désaccord que tu évites dans un groupe
- Respire et visualise une façon de l'aborder avec tact
- Note une position à affirmer aujourd'hui""",

    ('libra', 12): """# 🌙 Lune en Balance

**En une phrase :** Tu te sens en sécurité quand tu peux trouver la paix intérieure et l'harmonie avec tes zones d'ombre.

## Ton moteur
Tes besoins émotionnels passent par l'équilibre intérieur. Tu as besoin de faire la paix avec toi-même, de trouver la beauté dans ton inconscient.

## Ton défi
Éviter de fuir les parties de toi qui ne sont pas harmonieuses ou de chercher l'équilibre parfait.

## Maison 12 en Balance
Tu abordes le monde intérieur avec grâce et diplomatie. Ta spiritualité cherche l'harmonie, ton inconscient aspire à la paix.

## Micro-rituel du jour (2 min)
- Identifie une partie de toi que tu juges inélégante
- Respire et offre-lui de la douceur
- Note une façon de faire la paix avec cette part aujourd'hui""",

    # SCORPIO
    ('scorpio', 2): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand tu as le contrôle de tes ressources et que personne ne peut te les retirer.

## Ton moteur
Tes besoins émotionnels passent par la maîtrise financière. Tu as besoin de ressources qui te protègent, d'un pouvoir économique qui te rend invulnérable.

## Ton défi
Éviter l'obsession du contrôle financier ou la méfiance excessive concernant l'argent partagé.

## Maison 2 en Scorpion
Tu abordes l'argent avec intensité et stratégie. Tes valeurs sont profondes, tes possessions ont une charge émotionnelle forte. Tu ne partages pas facilement.

## Micro-rituel du jour (2 min)
- Identifie une peur liée à l'argent
- Respire et regarde-la en face sans la fuir
- Note une façon de lâcher un peu de contrôle""",

    ('scorpio', 3): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand tu peux communiquer en profondeur et que tes paroles ont de l'impact.

## Ton moteur
Tes besoins émotionnels passent par une communication intense. Tu as besoin d'échanges qui vont au fond des choses, de mots qui transforment.

## Ton défi
Éviter les paroles blessantes ou de garder des secrets qui finissent par peser.

## Maison 3 en Scorpion
Tu communiques avec intensité et pénétration. Tes échanges avec l'entourage sont profonds ou conflictuels. Tu apprends en enquêtant.

## Micro-rituel du jour (2 min)
- Pense à quelque chose que tu n'oses pas dire
- Respire et demande-toi si le silence te protège vraiment
- Note une vérité à exprimer avec tact aujourd'hui""",

    ('scorpio', 5): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand ta créativité touche aux profondeurs et que tes plaisirs sont intenses.

## Ton moteur
Tes besoins émotionnels passent par la création passionnée. Tu as besoin que tes œuvres remuent, que tes plaisirs soient sans demi-mesure.

## Ton défi
Éviter de dramatiser les loisirs ou de transformer chaque romance en passion destructrice.

## Maison 5 en Scorpion
Tu abordes la créativité avec intensité et profondeur. Tes romances sont passionnées et transformatrices. Avec les enfants, tu es protecteur et intense.

## Micro-rituel du jour (2 min)
- Choisis un plaisir simple que tu pourrais intensifier
- Respire et plonge dedans sans retenue
- Note une création à faire sur ce qui te passionne""",

    ('scorpio', 6): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand tu peux aller au fond des problèmes quotidiens et transformer ta routine.

## Ton moteur
Tes besoins émotionnels passent par la maîtrise du quotidien. Tu as besoin de comprendre les mécanismes cachés de ton travail, de transformer ta santé en profondeur.

## Ton défi
Éviter l'obsession du contrôle dans ta routine ou les relations de pouvoir malsaines au travail.

## Maison 6 en Scorpion
Tu abordes le travail avec intensité et stratégie. Ta routine a besoin de profondeur, ta santé est liée à tes émotions enfouies.

## Micro-rituel du jour (2 min)
- Identifie une habitude que tu devrais transformer
- Respire et engage-toi à la changer radicalement
- Note un premier pas courageux pour aujourd'hui""",

    ('scorpio', 8): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand tu peux plonger dans les profondeurs et ressortir transformé.

## Ton moteur
Tu es dans ton élément en maison 8. Transformation, intimité profonde, pouvoir et ressources partagées nourrissent profondément tes besoins émotionnels.

## Ton défi
Éviter de t'enliser dans l'intensité ou de chercher le pouvoir dans les relations intimes.

## Maison 8 en Scorpion
Double signature scorpionique : tu as un besoin vital d'intensité et de transformation. L'intimité est ton terrain, la crise est ton élément.

## Micro-rituel du jour (2 min)
- Identifie une peur profonde que tu évites
- Respire et regarde-la en face un instant
- Note un petit pas courageux vers elle""",

    ('scorpio', 9): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand ta philosophie de vie explore les mystères et les vérités cachées.

## Ton moteur
Tes besoins émotionnels passent par une quête de vérité profonde. Tu as besoin de croyances qui touchent aux tabous, de voyages initiatiques.

## Ton défi
Éviter de t'enfermer dans une vision sombre ou de rejeter les philosophies qui te semblent superficielles.

## Maison 9 en Scorpion
Tu abordes les grandes questions avec intensité. Tes voyages transforment, ta philosophie explore les ombres.

## Micro-rituel du jour (2 min)
- Choisis une vérité inconfortable que tu évites
- Respire et laisse-la exister sans la fuir
- Note ce qu'elle pourrait t'enseigner aujourd'hui""",

    ('scorpio', 11): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand tes amitiés sont loyales jusqu'à la mort et que les projets collectifs ont un impact réel.

## Ton moteur
Tes besoins émotionnels passent par des liens profonds. Tu as besoin d'amis en qui tu as une confiance absolue, de projets qui transforment.

## Ton défi
Éviter de tester excessivement la loyauté de tes amis ou de manipuler les dynamiques de groupe.

## Maison 11 en Scorpion
Tu abordes les amitiés avec intensité et engagement. Tes projets de groupe ont de l'impact. Tu es le stratège de tes cercles.

## Micro-rituel du jour (2 min)
- Pense à un ami en qui tu as une confiance absolue
- Respire et ressens la puissance de ce lien
- Note une façon d'approfondir cette connexion""",

    ('scorpio', 12): """# 🌙 Lune en Scorpion

**En une phrase :** Tu te sens en sécurité quand tu peux explorer tes profondeurs et transformer tes démons en alliés.

## Ton moteur
Tes besoins émotionnels passent par l'alchimie intérieure. Tu as besoin de descendre dans tes abysses, de transformer ta douleur en pouvoir.

## Ton défi
Éviter de t'enliser dans tes zones sombres ou de cultiver une fascination morbide.

## Maison 12 en Scorpion
Tu abordes le monde intérieur avec intensité et courage. Ta spiritualité est celle de la transformation profonde. Veille à ne pas te perdre dans l'obscurité.

## Micro-rituel du jour (2 min)
- Descends dans ton espace intérieur le plus sombre
- Respire et cherche une lueur, aussi petite soit-elle
- Note ce que cette lueur t'enseigne""",

    # SAGITTARIUS
    ('sagittarius', 2): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand tes ressources te permettent de voyager et d'élargir tes horizons.

## Ton moteur
Tes besoins émotionnels passent par la liberté financière. Tu as besoin d'argent pour l'aventure, pas pour l'accumulation.

## Ton défi
Éviter les dépenses impulsives pour les voyages ou la négligence dans la gestion de tes ressources.

## Maison 2 en Sagittaire
Tu abordes l'argent avec optimisme et générosité. Tes valeurs sont philosophiques, tes possessions te servent à explorer.

## Micro-rituel du jour (2 min)
- Identifie une dépense pour l'aventure que tu pourrais reporter
- Respire et demande-toi : "Est-ce le bon moment ?"
- Note une façon de voyager mentalement gratuitement""",

    ('sagittarius', 3): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand tu peux t'exprimer avec enthousiasme et partager ta vision du monde.

## Ton moteur
Tes besoins émotionnels passent par une communication inspirante. Tu as besoin de parler de tes rêves, d'échanger sur les grandes idées.

## Ton défi
Éviter d'exagérer ou de monopoliser la parole avec tes opinions philosophiques.

## Maison 3 en Sagittaire
Tu communiques avec enthousiasme et vision. Tes échanges avec l'entourage sont expansifs. Tu apprends en voyageant.

## Micro-rituel du jour (2 min)
- Pense à une conversation où tu as trop prêché
- Respire et visualise un échange où tu poses plus de questions
- Note une écoute curieuse à pratiquer aujourd'hui""",

    ('sagittarius', 5): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand tu peux jouer, explorer et vivre des aventures créatives.

## Ton moteur
Tes besoins émotionnels passent par l'expansion créative. Tu as besoin de plaisirs qui élargissent tes horizons, de romances aventureuses.

## Ton défi
Éviter de fuir l'engagement dans les plaisirs ou de toujours chercher mieux ailleurs.

## Maison 5 en Sagittaire
Tu abordes la créativité avec enthousiasme et vision. Tes romances sont des aventures, tes loisirs sont des explorations.

## Micro-rituel du jour (2 min)
- Choisis un plaisir simple que tu pourrais approfondir
- Respire et engage-toi à le savourer ici et maintenant
- Note une création à faire sans chercher la perfection""",

    ('sagittarius', 6): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand ton quotidien a du sens et que ton travail sert une vision plus grande.

## Ton moteur
Tes besoins émotionnels passent par un travail inspirant. Tu as besoin de routines qui élèvent, d'un quotidien qui ne t'enferme pas.

## Ton défi
Éviter de négliger les détails quotidiens ou de t'impatienter face aux tâches répétitives.

## Maison 6 en Sagittaire
Tu abordes le travail avec optimisme et vision. Ta routine a besoin de sens, ta santé passe par le mouvement et l'expansion.

## Micro-rituel du jour (2 min)
- Identifie une tâche quotidienne qui t'ennuie
- Respire et trouve-lui un sens plus grand
- Note une façon d'apporter de l'aventure dans ta routine""",

    ('sagittarius', 8): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand tu peux transformer les crises en aventures de croissance.

## Ton moteur
Tes besoins émotionnels passent par une vision positive des transformations. Tu as besoin de trouver un sens aux épreuves, de grandir à travers l'intensité.

## Ton défi
Éviter de fuir les profondeurs dans l'optimisme ou de minimiser l'intensité émotionnelle.

## Maison 8 en Sagittaire
Tu abordes les transformations avec foi et expansion. L'intimité profonde est une aventure, les crises sont des opportunités.

## Micro-rituel du jour (2 min)
- Pense à une épreuve que tu as traversée
- Respire et identifie ce qu'elle t'a appris
- Note une façon de transformer une difficulté actuelle""",

    ('sagittarius', 9): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand tu peux explorer le monde et nourrir ta soif de sens.

## Ton moteur
Tu es dans ton élément en maison 9. Voyages, philosophie, enseignement, expansion nourrissent profondément tes besoins émotionnels.

## Ton défi
Éviter la fuite dans l'ailleurs ou de croire que tu as trouvé LA vérité.

## Maison 9 en Sagittaire
Double signature sagittarienne : tu as un besoin vital d'horizons larges. Ta quête de sens est constante, ta soif d'apprendre est infinie.

## Micro-rituel du jour (2 min)
- Choisis une conviction qui te porte
- Respire et demande-toi : "Puis-je l'enrichir ?"
- Note une nouvelle perspective à explorer""",

    ('sagittarius', 11): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand tes amis partagent ta soif d'aventure et que les projets collectifs visent haut.

## Ton moteur
Tes besoins émotionnels passent par l'expansion sociale. Tu as besoin d'amis qui rêvent grand, de projets qui élargissent les horizons.

## Ton défi
Éviter de promettre plus que tu ne peux tenir ou de t'impatienter face aux rythmes plus lents.

## Maison 11 en Sagittaire
Tu abordes les amitiés avec enthousiasme et vision. Tes projets de groupe sont ambitieux. Tu es l'inspirateur de tes cercles.

## Micro-rituel du jour (2 min)
- Pense à un projet de groupe qui te fait rêver
- Respire et identifie la première étape concrète
- Note une action réaliste pour avancer""",

    ('sagittarius', 12): """# 🌙 Lune en Sagittaire

**En une phrase :** Tu te sens en sécurité quand tu peux te connecter à une foi intérieure et voyager dans ton monde invisible.

## Ton moteur
Tes besoins émotionnels passent par la spiritualité expansive. Tu as besoin de te sentir relié à quelque chose de plus grand, même dans la solitude.

## Ton défi
Éviter la fuite dans des croyances qui t'éloignent de la réalité.

## Maison 12 en Sagittaire
Tu abordes le monde intérieur avec foi et expansion. Ta spiritualité est vaste, tes retraites sont des voyages. Veille à rester ancré.

## Micro-rituel du jour (2 min)
- Ferme les yeux et connecte-toi à ta source de foi
- Respire et laisse cette confiance t'envelopper
- Note comment cette foi peut éclairer ta journée""",

    # CAPRICORN
    ('capricorn', 2): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand tes ressources sont stables et que tu as construit ta sécurité par tes efforts.

## Ton moteur
Tes besoins émotionnels passent par la solidité financière. Tu as besoin de construire ta richesse pierre par pierre, de prouver ta valeur par le travail.

## Ton défi
Éviter l'austérité excessive ou de mesurer ta valeur uniquement à tes possessions.

## Maison 2 en Capricorne
Tu abordes l'argent avec sérieux et ambition. Tes valeurs sont traditionnelles, tes possessions sont durables. Tu construis dans le temps.

## Micro-rituel du jour (2 min)
- Identifie une richesse non-matérielle que tu possèdes
- Respire et ressens sa valeur
- Note une façon de te sentir riche sans argent""",

    ('capricorn', 3): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand tu peux t'exprimer avec autorité et que tes paroles ont du poids.

## Ton moteur
Tes besoins émotionnels passent par une communication structurée. Tu as besoin que tes idées soient respectées, que tes mots comptent.

## Ton défi
Éviter la communication trop sèche ou de te fermer quand tu ne te sens pas pris au sérieux.

## Maison 3 en Capricorne
Tu communiques avec sérieux et structure. Tes échanges avec l'entourage sont pragmatiques. Tu apprends avec persévérance.

## Micro-rituel du jour (2 min)
- Pense à une idée que tu n'oses pas partager
- Respire et trouve une façon de la formuler avec autorité
- Note une communication à oser aujourd'hui""",

    ('capricorn', 5): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand ta créativité est reconnue et que tes plaisirs ont un sens.

## Ton moteur
Tes besoins émotionnels passent par la création sérieuse. Tu as besoin que tes œuvres durent, que tes loisirs aient une valeur.

## Ton défi
Éviter de transformer les plaisirs en obligations ou de bloquer ta créativité par perfectionnisme.

## Maison 5 en Capricorne
Tu abordes la créativité avec discipline et ambition. Tes romances sont sérieuses, tes loisirs sont structurés. Avec les enfants, tu es exigeant.

## Micro-rituel du jour (2 min)
- Choisis un plaisir que tu t'interdis par sérieux
- Respire et donne-toi la permission de le vivre
- Note une création à faire sans enjeu de réussite""",

    ('capricorn', 6): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand ta routine est productive et que ton travail est reconnu.

## Ton moteur
Tes besoins émotionnels passent par l'efficacité professionnelle. Tu as besoin de structures claires, de responsabilités, de résultats visibles.

## Ton défi
Éviter de te surcharger de travail ou de négliger ta santé pour la performance.

## Maison 6 en Capricorne
Tu abordes le travail avec discipline et ambition. Ta routine est structurée, ta santé est gérée avec sérieux. Tu vises l'excellence.

## Micro-rituel du jour (2 min)
- Identifie une charge que tu pourrais alléger
- Respire et donne-toi la permission de déléguer
- Note une façon de prendre soin de toi au travail""",

    ('capricorn', 8): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand tu peux traverser les crises avec dignité et contrôle.

## Ton moteur
Tes besoins émotionnels passent par la maîtrise des transformations. Tu as besoin de garder le contrôle même dans l'intensité.

## Ton défi
Éviter de réprimer les émotions profondes ou de refuser l'aide par orgueil.

## Maison 8 en Capricorne
Tu abordes les transformations avec sérieux et stratégie. L'intimité profonde te demande structure, les crises sont des défis à relever.

## Micro-rituel du jour (2 min)
- Identifie une émotion que tu contrôles trop
- Respire et laisse-la exister un instant
- Note une façon de lâcher un peu de contrôle""",

    ('capricorn', 9): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand ta philosophie de vie est solide et a fait ses preuves.

## Ton moteur
Tes besoins émotionnels passent par une sagesse pragmatique. Tu as besoin de croyances qui marchent, qui ont de l'autorité.

## Ton défi
Éviter le cynisme philosophique ou de rejeter les idées qui ne sont pas immédiatement utiles.

## Maison 9 en Capricorne
Tu abordes les grandes questions avec sérieux et pragmatisme. Tes voyages sont organisés, ta philosophie est terre-à-terre.

## Micro-rituel du jour (2 min)
- Choisis une croyance qui te semble trop idéaliste
- Respire et cherche ce qu'elle pourrait t'apporter
- Note une ouverture possible aujourd'hui""",

    ('capricorn', 11): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand tes amitiés sont fiables et que les projets collectifs sont bien structurés.

## Ton moteur
Tes besoins émotionnels passent par des liens durables. Tu as besoin d'amis sérieux, de projets de groupe qui construisent quelque chose.

## Ton défi
Éviter de choisir tes amis pour leur statut ou de prendre tout sur tes épaules dans les groupes.

## Maison 11 en Capricorne
Tu abordes les amitiés avec sérieux et engagement. Tes projets de groupe visent le long terme. Tu es le pilier fiable de tes cercles.

## Micro-rituel du jour (2 min)
- Pense à un ami que tu respectes profondément
- Respire et ressens la solidité de ce lien
- Note une responsabilité à déléguer aujourd'hui""",

    ('capricorn', 12): """# 🌙 Lune en Capricorne

**En une phrase :** Tu te sens en sécurité quand tu peux travailler sur toi en silence et construire ta force intérieure.

## Ton moteur
Tes besoins émotionnels passent par la discipline intérieure. Tu as besoin de structurer ton monde invisible, de bâtir ta solidité secrète.

## Ton défi
Éviter de t'isoler dans une austérité excessive ou de porter seul des fardeaux cachés.

## Maison 12 en Capricorne
Tu abordes le monde intérieur avec sérieux et persévérance. Ta spiritualité est structurée, ton inconscient est travaillé. Veille à ne pas t'enfermer.

## Micro-rituel du jour (2 min)
- Identifie un fardeau que tu portes seul
- Respire et visualise-toi le déposant un instant
- Note une façon d'alléger cette charge""",

    # AQUARIUS
    ('aquarius', 2): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand tes ressources te permettent d'être libre et indépendant.

## Ton moteur
Tes besoins émotionnels passent par la liberté financière non-conventionnelle. Tu as besoin de gagner ta vie à ta façon, de ne pas dépendre du système.

## Ton défi
Éviter l'instabilité financière par anticonformisme ou le détachement excessif des besoins matériels.

## Maison 2 en Verseau
Tu abordes l'argent avec originalité et détachement. Tes valeurs sont progressistes, tes possessions sont atypiques.

## Micro-rituel du jour (2 min)
- Identifie un besoin matériel que tu négliges
- Respire et accepte qu'il est légitime
- Note une façon de prendre soin de ta sécurité""",

    ('aquarius', 3): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand tu peux t'exprimer librement et que tes idées originales sont entendues.

## Ton moteur
Tes besoins émotionnels passent par une communication innovante. Tu as besoin d'échanger des idées nouvelles, de ne pas être enfermé dans les conventions.

## Ton défi
Éviter de choquer pour choquer ou de te couper des autres par trop d'originalité.

## Maison 3 en Verseau
Tu communiques avec originalité et liberté. Tes échanges avec l'entourage sont atypiques. Tu apprends en expérimentant.

## Micro-rituel du jour (2 min)
- Pense à une idée que tu retiens par peur d'être bizarre
- Respire et trouve une façon de l'exprimer
- Note une originalité à assumer aujourd'hui""",

    ('aquarius', 5): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand ta créativité est libre et que tes plaisirs sont originaux.

## Ton moteur
Tes besoins émotionnels passent par la création innovante. Tu as besoin de loisirs atypiques, de romances qui ne suivent pas les règles.

## Ton défi
Éviter de fuir l'engagement émotionnel dans les plaisirs ou de rejeter les joies simples par snobisme.

## Maison 5 en Verseau
Tu abordes la créativité avec originalité et liberté. Tes romances sont atypiques, tes loisirs sont innovants. Avec les enfants, tu es stimulant mais distant.

## Micro-rituel du jour (2 min)
- Choisis un plaisir conventionnel que tu évites
- Respire et donne-lui une chance
- Note une joie simple à vivre aujourd'hui""",

    ('aquarius', 6): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand ta routine est flexible et que ton travail est innovant.

## Ton moteur
Tes besoins émotionnels passent par la liberté au quotidien. Tu as besoin d'un travail qui sort de l'ordinaire, de routines non-conventionnelles.

## Ton défi
Éviter l'instabilité excessive dans ta routine ou le rejet de toute structure par principe.

## Maison 6 en Verseau
Tu abordes le travail avec originalité et indépendance. Ta routine a besoin de variété, ta santé passe par l'innovation.

## Micro-rituel du jour (2 min)
- Identifie une routine que tu rejettes par anticonformisme
- Respire et demande-toi si elle pourrait t'aider
- Note une structure à accepter aujourd'hui""",

    ('aquarius', 8): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand tu peux traverser les crises avec détachement et en garder ta liberté.

## Ton moteur
Tes besoins émotionnels passent par la distance face à l'intensité. Tu as besoin de comprendre les transformations plutôt que de t'y perdre.

## Ton défi
Éviter de fuir l'intimité émotionnelle dans l'intellect ou de te couper de tes profondeurs.

## Maison 8 en Verseau
Tu abordes les transformations avec détachement et originalité. L'intimité profonde te demande de ne pas tout intellectualiser.

## Micro-rituel du jour (2 min)
- Identifie une émotion intense que tu rationalises
- Respire et laisse-la exister sans l'analyser
- Note une façon de ressentir pleinement aujourd'hui""",

    ('aquarius', 9): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand ta philosophie de vie est libre et que tu peux remettre en question les dogmes.

## Ton moteur
Tes besoins émotionnels passent par la liberté de pensée. Tu as besoin de croyances qui libèrent, pas qui enferment.

## Ton défi
Éviter de rejeter toute tradition ou de t'isoler dans des théories que personne ne comprend.

## Maison 9 en Verseau
Tu abordes les grandes questions avec originalité et liberté. Tes voyages sont atypiques, ta philosophie est progressiste.

## Micro-rituel du jour (2 min)
- Choisis une tradition que tu rejettes par principe
- Respire et cherche ce qu'elle contient de valable
- Note une sagesse ancienne à reconsidérer""",

    ('aquarius', 11): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand tu fais partie de communautés libres et que tes amis respectent ton indépendance.

## Ton moteur
Tu es dans ton élément en maison 11. Amitiés atypiques, projets collectifs innovants, causes humanitaires nourrissent profondément tes besoins émotionnels.

## Ton défi
Éviter de sacrifier les liens personnels au nom de l'idéal collectif.

## Maison 11 en Verseau
Double signature verseau : tu as un besoin vital de communauté libre. Tu attires des amis originaux et tu portes des projets visionnaires.

## Micro-rituel du jour (2 min)
- Pense à un ami très différent de toi
- Respire et apprécie cette différence
- Note une façon de nourrir ce lien unique""",

    ('aquarius', 12): """# 🌙 Lune en Verseau

**En une phrase :** Tu te sens en sécurité quand tu peux te connecter à une conscience plus vaste et transcender les limites de l'ego.

## Ton moteur
Tes besoins émotionnels passent par la liberté intérieure. Tu as besoin de te sentir relié à l'humanité tout en gardant ta solitude.

## Ton défi
Éviter de te couper des émotions personnelles au nom d'idéaux abstraits.

## Maison 12 en Verseau
Tu abordes le monde intérieur avec liberté et détachement. Ta spiritualité est universelle, ton inconscient aspire au collectif.

## Micro-rituel du jour (2 min)
- Ferme les yeux et connecte-toi à l'humanité
- Respire et ressens ta place unique dans ce tout
- Note une façon de servir à ta manière""",

    # PISCES
    ('pisces', 2): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand tes ressources coulent naturellement et que l'argent n'est pas une obsession.

## Ton moteur
Tes besoins émotionnels passent par un rapport fluide à l'argent. Tu as besoin de sentir que l'univers pourvoit, que les ressources viennent quand il faut.

## Ton défi
Éviter la négligence financière ou de te faire avoir par naïveté. Les pieds sur terre sont nécessaires.

## Maison 2 en Poissons
Tu abordes l'argent avec fluidité et détachement. Tes valeurs sont spirituelles, tes possessions ont peu d'importance.

## Micro-rituel du jour (2 min)
- Identifie une question financière que tu évites
- Respire et décide de t'en occuper
- Note une action concrète pour ta sécurité""",

    ('pisces', 3): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand tu peux communiquer avec ton intuition et que les mots portent de l'émotion.

## Ton moteur
Tes besoins émotionnels passent par une communication sensible. Tu as besoin d'échanger sur ce qui se ressent, pas seulement ce qui se pense.

## Ton défi
Éviter le flou dans la communication ou de te perdre dans des rêveries au lieu d'écouter.

## Maison 3 en Poissons
Tu communiques avec sensibilité et intuition. Tes échanges avec l'entourage sont empathiques. Tu apprends par absorption.

## Micro-rituel du jour (2 min)
- Pense à quelque chose que tu ressens sans pouvoir l'exprimer
- Respire et cherche une image plutôt que des mots
- Note une façon de communiquer avec le cœur""",

    ('pisces', 5): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand ta créativité peut s'exprimer librement et que tes plaisirs nourrissent l'âme.

## Ton moteur
Tes besoins émotionnels passent par la création inspirée. Tu as besoin d'art, de musique, de beauté qui touche au sacré.

## Ton défi
Éviter de fuir dans les rêveries ou les paradis artificiels. La créativité demande aussi de la discipline.

## Maison 5 en Poissons
Tu abordes la créativité avec sensibilité et inspiration. Tes romances sont idéalisées, tes plaisirs sont poétiques.

## Micro-rituel du jour (2 min)
- Choisis une création à faire sans attendre l'inspiration parfaite
- Respire et commence même imparfaitement
- Note une façon d'ancrer ta créativité aujourd'hui""",

    ('pisces', 6): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand ton quotidien a une dimension de service et que ton travail aide les autres.

## Ton moteur
Tes besoins émotionnels passent par le service compassionnel. Tu as besoin de te sentir utile aux autres, de routines qui ont du sens.

## Ton défi
Éviter de te sacrifier excessivement ou de négliger ta santé par négligence.

## Maison 6 en Poissons
Tu abordes le travail avec compassion et fluidité. Ta routine a besoin de sens, ta santé est sensible à l'émotionnel.

## Micro-rituel du jour (2 min)
- Identifie un besoin de ton corps que tu négliges
- Respire et écoute ce qu'il te dit
- Note une façon de prendre soin de toi aujourd'hui""",

    ('pisces', 8): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand tu peux te dissoudre dans l'intensité et fusionner avec quelque chose de plus grand.

## Ton moteur
Tes besoins émotionnels passent par la transcendance dans l'intimité. Tu as besoin de te perdre pour mieux te trouver.

## Ton défi
Éviter de te noyer dans les émotions des autres ou de fuir dans des états altérés.

## Maison 8 en Poissons
Tu abordes les transformations avec fluidité et abandon. L'intimité profonde est fusion, les crises sont des dissolutions.

## Micro-rituel du jour (2 min)
- Identifie une émotion qui n'est peut-être pas la tienne
- Respire et recentre-toi sur ton propre ressenti
- Note une limite à maintenir aujourd'hui""",

    ('pisces', 9): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand ta spiritualité est vivante et que tu peux te connecter au mystère.

## Ton moteur
Tes besoins émotionnels passent par la transcendance. Tu as besoin de croyances qui touchent l'âme, de vérités qui se ressentent.

## Ton défi
Éviter de te perdre dans des croyances floues ou de fuir la réalité dans le spirituel.

## Maison 9 en Poissons
Tu abordes les grandes questions avec sensibilité et intuition. Tes voyages sont des pèlerinages, ta philosophie est mystique.

## Micro-rituel du jour (2 min)
- Choisis une intuition spirituelle que tu as du mal à formuler
- Respire et laisse-la exister sans l'expliquer
- Note une façon de lui faire confiance""",

    ('pisces', 11): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand tes amitiés sont des liens d'âme et que les projets collectifs servent une cause sacrée.

## Ton moteur
Tes besoins émotionnels passent par la communion avec les autres. Tu as besoin d'amis avec qui tu te sens connecté au-delà des mots.

## Ton défi
Éviter de te dissoudre dans les groupes ou de te sacrifier pour des causes qui ne te respectent pas.

## Maison 11 en Poissons
Tu abordes les amitiés avec compassion et idéalisme. Tes projets de groupe ont une dimension spirituelle.

## Micro-rituel du jour (2 min)
- Pense à un groupe où tu donnes beaucoup
- Respire et vérifie que tu reçois aussi
- Note une limite à poser aujourd'hui""",

    ('pisces', 12): """# 🌙 Lune en Poissons

**En une phrase :** Tu te sens en sécurité quand tu peux te retirer du monde et te connecter à l'infini.

## Ton moteur
Tu es dans ton élément en maison 12. Solitude, spiritualité, compassion universelle, dissolution des frontières nourrissent profondément tes besoins émotionnels.

## Ton défi
Éviter de fuir le monde ou de te perdre dans des états de conscience qui t'éloignent de la réalité.

## Maison 12 en Poissons
Double signature poissons : tu as un accès naturel au transcendant. Ta sensibilité à l'invisible est un don, à condition de garder un pied sur terre.

## Micro-rituel du jour (2 min)
- Ferme les yeux et laisse-toi flotter
- Respire et ressens la paix de l'infini
- Note une façon d'ancrer cette paix dans ta journée""",
}


async def update_interpretations():
    async with AsyncSessionLocal() as db:
        updated = 0
        for (sign, house), content in MOON_INTERPRETATIONS.items():
            result = await db.execute(
                update(PregeneratedNatalInterpretation)
                .where(
                    PregeneratedNatalInterpretation.subject == 'moon',
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
        print(f"Done: {updated} moon interpretations updated")


if __name__ == '__main__':
    asyncio.run(update_interpretations())
