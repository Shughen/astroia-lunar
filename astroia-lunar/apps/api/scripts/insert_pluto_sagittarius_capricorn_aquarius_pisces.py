#!/usr/bin/env python3
"""Insert Pluto interpretations for Sagittarius, Capricorn, Aquarius, Pisces (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_pluto_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'sagittarius': '♇ Pluton en Sagittaire',
        'capricorn': '♇ Pluton en Capricorne',
        'aquarius': '♇ Pluton en Verseau',
        'pisces': '♇ Pluton en Poissons',
    }
    sign_fr = {
        'sagittarius': 'Sagittaire',
        'capricorn': 'Capricorne',
        'aquarius': 'Verseau',
        'pisces': 'Poissons',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ton moteur
{moteur}

## Ton défi
{defi}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

PLUTO_INTERPRETATIONS = {
    # === SAGITTARIUS (M1-M12) ===
    ('sagittarius', 1): make_pluto_interp('sagittarius', 1,
        "Tu transformes ta vie par une quête expansive de vérité et de sens.",
        "Pluton en Sagittaire dans ta maison I te donne une présence enthousiaste et philosophique. Tu incarnes la recherche de vérité et l'expansion des horizons avec une intensité passionnée.",
        "Apprendre à tempérer ton zèle missionnaire. Ta conviction peut devenir dogmatisme si tu ne restes pas ouvert aux autres perspectives.",
        "Ton apparence dégage une aura d'aventurier spirituel. Les transformations personnelles passent par l'élargissement de ta vision du monde. Tu renais à travers les voyages et la quête de sens.",
        "Regarde vers l'horizon (par une fenêtre ou en imagination) et sens l'appel de l'expansion.",
        "Respire en visualisant ton champ de conscience qui s'élargit infiniment.",
        "Quelle nouvelle vérité suis-je prêt(e) à explorer et incarner ? »"),

    ('sagittarius', 2): make_pluto_interp('sagittarius', 2,
        "Tu transformes ta vie par une relation généreuse et philosophique à l'argent.",
        "Pluton en Sagittaire dans ta maison II lie ta valeur personnelle à ta capacité d'inspirer et d'enseigner. L'argent vient quand tu partages ta vision avec générosité.",
        "Éviter les dépenses excessives ou la croyance que l'argent viendra par magie. Ton défi est de valoriser tes talents visionnaires de façon pratique.",
        "Tes revenus sont liés à l'éducation, les voyages, l'édition, la spiritualité. Les possessions ont une dimension philosophique. Tu investis dans les expériences plus que dans les objets.",
        "Fais un don généreux à une cause qui élargit les horizons des autres.",
        "Respire en visualisant l'abondance qui vient de partager ta sagesse.",
        "Comment puis-je mieux valoriser ma vision unique du monde ? »"),

    ('sagittarius', 3): make_pluto_interp('sagittarius', 3,
        "Tu transformes ta vie par une communication inspirante et philosophique.",
        "Pluton en Sagittaire dans ta maison III fait de ta parole une flèche de vérité. Tu communiques avec enthousiasme et conviction, cherchant toujours le sens plus large.",
        "Éviter de prêcher au lieu de dialoguer. Le défi est de partager ta vision sans écraser les perspectives différentes de la tienne.",
        "Les relations avec frères, sœurs ou voisins sont stimulantes intellectuellement. L'apprentissage est une aventure. Tu excelles à transmettre l'enthousiasme pour les idées.",
        "Partage une idée inspirante avec quelqu'un — pas pour convaincre, pour inspirer.",
        "Respire en sentant tes mots qui portent la flamme de la vérité.",
        "Quelle vérité inspirante puis-je partager aujourd'hui ? »"),

    ('sagittarius', 4): make_pluto_interp('sagittarius', 4,
        "Tu transformes ta vie par une redéfinition expansive de la notion de foyer.",
        "Pluton en Sagittaire dans ta maison IV fait de ton foyer une base d'exploration ou un ashram. Les racines familiales portent une quête de sens transmise entre générations.",
        "Éviter de fuir la maison ou de projeter tes idéaux sur ta famille. Le défi est de créer un foyer qui permet l'expansion tout en offrant des racines solides.",
        "Ton espace de vie reflète tes voyages et ta philosophie. La relation au parent aventurier ou philosophe est transformatrice. Les traditions familiales sont questionnées et renouvelées.",
        "Ajoute un élément d'un pays ou d'une culture lointaine à ton espace de vie.",
        "Respire en visualisant ton foyer comme un temple de sagesse et d'ouverture.",
        "Comment puis-je intégrer ma quête de sens dans ma vie de famille ? »"),

    ('sagittarius', 5): make_pluto_interp('sagittarius', 5,
        "Tu transformes ta vie par une créativité visionnaire et des amours aventureuses.",
        "Pluton en Sagittaire dans ta maison V fait de ta créativité une quête de vérité. Tes œuvres portent un message, une vision. L'amour est une aventure philosophique.",
        "Éviter de transformer chaque romance en croisade ou de créer uniquement pour prouver quelque chose. Le défi est de créer et aimer avec joie, pas avec mission.",
        "Les romances sont stimulantes, aventureuses, souvent avec des étrangers ou des personnes différentes. La relation aux enfants est philosophique et ouverte. Le jeu est une exploration.",
        "Crée quelque chose qui exprime ta vision du monde avec joie et légèreté.",
        "Respire en laissant ta créativité s'inspirer de tes plus grandes aspirations.",
        "Quelle aventure créative m'appelle aujourd'hui ? »"),

    ('sagittarius', 6): make_pluto_interp('sagittarius', 6,
        "Tu transformes ta vie par un travail qui a du sens et une santé holistique.",
        "Pluton en Sagittaire dans ta maison VI fait du travail quotidien un terrain d'exploration. Ta santé dépend de ton sens de l'aventure et de ta connexion au sens plus large.",
        "Éviter de négliger les tâches pratiques au profit des grandes idées. Le défi est de trouver le sens dans les petites choses, pas seulement dans les grandes.",
        "Ton travail doit te permettre d'apprendre et de grandir. Le foie et les cuisses sont tes zones sensibles. L'exercice en extérieur, l'aventure physique te régénèrent.",
        "Fais une tâche ordinaire en y trouvant consciemment un sens plus grand.",
        "Respire en visualisant ton corps comme un véhicule d'exploration.",
        "Comment puis-je trouver plus de sens dans mon travail quotidien ? »"),

    ('sagittarius', 7): make_pluto_interp('sagittarius', 7,
        "Tu transformes ta vie par des partenariats avec des visionnaires et des explorateurs.",
        "Pluton en Sagittaire dans ta maison VII attire des partenaires qui élargissent tes horizons. Le couple est une aventure intellectuelle et spirituelle commune.",
        "Éviter de vouloir convertir ton partenaire à ta vision ou de choisir des compagnons uniquement pour leur exotisme. Le défi est de créer des partenariats qui grandissent ensemble.",
        "Tes associations ont une dimension philosophique ou internationale. Le partenaire peut être étranger ou très différent culturellement. Les contrats impliquent des questions d'éthique.",
        "Partage une vision d'avenir avec un partenaire et explore ensemble.",
        "Respire en visualisant un partenariat qui vous élève tous les deux vers de nouveaux horizons.",
        "Quelle aventure puis-je partager avec mes partenaires ? »"),

    ('sagittarius', 8): make_pluto_interp('sagittarius', 8,
        "Tu transformes ta vie par une exploration philosophique des mystères ultimes.",
        "Pluton en Sagittaire dans ta maison VIII fait de la mort et de la transformation une quête de sens. Tu cherches la vérité dans les expériences limites et les passages initiatiques.",
        "Éviter le tourisme spirituel ou la fuite des profondeurs par la philosophie. Le défi est de vraiment traverser les transformations, pas juste d'y réfléchir.",
        "La sexualité peut avoir une dimension sacrée ou initiatique. Les héritages peuvent venir de l'étranger ou de traditions spirituelles. Tu peux accompagner les autres dans leurs passages avec optimisme.",
        "Médite sur une expérience de transformation passée et trouve son enseignement.",
        "Respire en accueillant les mystères comme des portes vers une vérité plus grande.",
        "Quel enseignement se cache dans mes épreuves les plus profondes ? »"),

    ('sagittarius', 9): make_pluto_interp('sagittarius', 9,
        "Tu transformes ta vie par une quête spirituelle passionnée et des voyages initiatiques.",
        "Pluton en Sagittaire dans ta maison IX (son domicile naturel) fait de toi un chercheur de vérité puissant. Ta philosophie est vivante, évolutive, transformatrice.",
        "Éviter le dogmatisme ou la croyance que tu as trouvé LA vérité. Le défi est de rester un éternel étudiant tout en partageant ce que tu as appris.",
        "L'éducation supérieure te transforme profondément. Les voyages vers des lieux sacrés ou des cultures différentes sont initiatiques. Tu peux devenir un enseignant ou guide influent.",
        "Étudie un texte sacré ou philosophique avec une vraie soif de vérité.",
        "Respire en visualisant ta conscience qui s'élargit vers l'infini.",
        "Quelle vérité suis-je appelé(e) à découvrir et transmettre ? »"),

    ('sagittarius', 10): make_pluto_interp('sagittarius', 10,
        "Tu transformes ta vie par une carrière qui inspire et élève la conscience collective.",
        "Pluton en Sagittaire dans ta maison X te destine à une position d'influence comme visionnaire ou enseignant. Ta réputation est liée à ta capacité d'inspirer et d'élargir les horizons.",
        "Éviter l'arrogance intellectuelle ou la prétention de détenir la vérité. Le défi est d'influencer avec humilité tout en restant fidèle à ta vision.",
        "Ta carrière passe par des phases d'expansion et de remise en question. Tu peux exceller dans l'éducation, l'édition, le voyage, la spiritualité. Ton impact est souvent international.",
        "Visualise la contribution que tu veux apporter au monde à travers ta carrière.",
        "Respire en ressentant la responsabilité joyeuse d'inspirer les autres.",
        "Quel message veux-je que ma carrière transmette au monde ? »"),

    ('sagittarius', 11): make_pluto_interp('sagittarius', 11,
        "Tu transformes ta vie par des amitiés inspirantes et des projets d'expansion collective.",
        "Pluton en Sagittaire dans ta maison XI t'amène des amis visionnaires et multiculturels. Tes projets collectifs visent à élargir les horizons et élever les consciences.",
        "Éviter de considérer tes amis uniquement comme des disciples ou de rejeter ceux qui ne partagent pas ta vision. Le défi est de créer des communautés diversifiées et ouvertes.",
        "Tes réseaux sont composés de personnes de cultures et horizons différents. Les projets collectifs peuvent concerner l'éducation, le voyage, la spiritualité, la philosophie.",
        "Connecte-toi à un ami d'une culture différente et explore une nouvelle perspective.",
        "Respire en visualisant une communauté mondiale unie par la quête de vérité.",
        "Comment mes connexions peuvent-elles élargir les horizons collectifs ? »"),

    ('sagittarius', 12): make_pluto_interp('sagittarius', 12,
        "Tu transformes ta vie par une dissolution des croyances limitantes et une expansion spirituelle.",
        "Pluton en Sagittaire dans ta maison XII te confronte à l'ombre de tes croyances — dogmatisme caché, fuite dans la spiritualité, orgueil intellectuel. Ton travail est la vraie humilité spirituelle.",
        "Éviter de te perdre dans des quêtes sans fin ou de fuir la réalité par les voyages. Le défi est de trouver l'expansion dans le moment présent, pas ailleurs.",
        "L'inconscient porte des mémoires de vies passées ou de traditions ancestrales. Les retraites spirituelles dans des lieux lointains sont profondément transformatrices. Les rêves sont prophétiques.",
        "Médite en silence en laissant aller toute croyance, même les plus précieuses.",
        "Respire en visualisant ton mental qui s'ouvre au-delà de toute limite connue.",
        "Quelle croyance limitante suis-je prêt(e) à abandonner ? »"),

    # === CAPRICORN (M1-M12) ===
    ('capricorn', 1): make_pluto_interp('capricorn', 1,
        "Tu transformes ta vie par une ambition structurée et une maîtrise de toi implacable.",
        "Pluton en Capricorne dans ta maison I te donne une présence d'autorité naturelle. Tu incarnes la discipline, l'ambition et la capacité de construire des structures durables.",
        "Apprendre à ne pas te définir uniquement par tes accomplissements. Ta rigueur peut devenir dureté si elle n'est pas tempérée par la compassion.",
        "Ton apparence dégage une aura de compétence et de sérieux. Les transformations personnelles passent par des restructurations profondes. Tu renais en bâtissant sur des ruines.",
        "Regarde-toi dans un miroir et reconnais la force tranquille qui habite ton regard.",
        "Respire en visualisant une montagne solide au centre de ton être.",
        "Quelle structure intérieure suis-je en train de bâtir ? »"),

    ('capricorn', 2): make_pluto_interp('capricorn', 2,
        "Tu transformes ta vie par une construction patiente et stratégique de tes ressources.",
        "Pluton en Capricorne dans ta maison II lie ta valeur personnelle à ta capacité de bâtir la prospérité à long terme. L'argent est un outil de pouvoir à accumuler avec sagesse.",
        "Éviter l'avarice ou l'obsession du statut financier. Ton défi est de construire des richesses qui servent une vision plus grande que la simple accumulation.",
        "Tes revenus viennent de positions d'autorité ou de compétences d'expertise. Les possessions sont des investissements à long terme. Tu bâtis la prospérité génération après génération.",
        "Fais un petit investissement conscient dans ton futur — financier ou autre.",
        "Respire en visualisant des structures de prospérité qui se construisent pierre après pierre.",
        "Quelle fondation financière suis-je en train de construire pour l'avenir ? »"),

    ('capricorn', 3): make_pluto_interp('capricorn', 3,
        "Tu transformes ta vie par une communication structurée et une pensée stratégique.",
        "Pluton en Capricorne dans ta maison III fait de ta parole un outil de pouvoir. Tu communiques avec précision et autorité, visant toujours l'essentiel.",
        "Éviter la froideur dans la communication ou la manipulation par l'information. Le défi est de structurer tes pensées sans devenir rigide ou contrôlant.",
        "Les relations avec frères, sœurs ou voisins impliquent des dynamiques d'autorité. L'apprentissage est méthodique et orienté vers des résultats concrets. Tu excelles dans la stratégie.",
        "Écris un plan structuré pour atteindre un objectif qui te tient à cœur.",
        "Respire en organisant mentalement tes pensées comme des blocs bien empilés.",
        "Quelle communication stratégique puis-je faire aujourd'hui ? »"),

    ('capricorn', 4): make_pluto_interp('capricorn', 4,
        "Tu transformes ta vie par une reconstruction des fondations familiales et professionnelles.",
        "Pluton en Capricorne dans ta maison IV indique des transformations profondes dans ta structure familiale. Les racines portent des enjeux d'autorité et de responsabilité.",
        "Éviter de reproduire les structures rigides ou les schémas d'autorité excessive. Le défi est de créer des fondations solides mais flexibles pour ta vie.",
        "Ton foyer peut être austère mais solide. La relation au père ou aux figures d'autorité est transformatrice. Les mémoires familiales concernent souvent le travail, le statut, la survie.",
        "Stabilise consciemment un aspect de ta vie domestique qui en a besoin.",
        "Respire en visualisant les fondations de ta vie qui se renforcent.",
        "Quelle structure familiale ai-je besoin de transformer ou renforcer ? »"),

    ('capricorn', 5): make_pluto_interp('capricorn', 5,
        "Tu transformes ta vie par une créativité disciplinée et des amours matures.",
        "Pluton en Capricorne dans ta maison V fait de ta créativité une entreprise sérieuse. Tes œuvres sont structurées, ambitieuses, destinées à durer. L'amour se mérite et se construit.",
        "Éviter de transformer le jeu en travail ou de juger sévèrement ta créativité. Le défi est de trouver la joie dans la discipline, pas malgré elle.",
        "Les romances sont sérieuses, orientées vers l'engagement. La relation aux enfants peut être exigeante mais structurante. Le jeu a une dimension d'apprentissage et de maîtrise.",
        "Crée quelque chose avec discipline et engagement, même si c'est petit.",
        "Respire en trouvant la joie dans l'effort et la structure.",
        "Comment puis-je apporter plus de joie dans ma discipline créative ? »"),

    ('capricorn', 6): make_pluto_interp('capricorn', 6,
        "Tu transformes ta vie par un travail acharné et une santé à surveiller.",
        "Pluton en Capricorne dans ta maison VI fait du travail un terrain d'accomplissement intense. Ta santé dépend de l'équilibre entre ambition et repos.",
        "Éviter de t'épuiser au travail ou de négliger ta santé pour la carrière. Le défi est de construire des habitudes durables qui soutiennent ton ambition à long terme.",
        "Ton travail demande structure et discipline. Les os, les genoux, la peau sont tes zones sensibles. Les routines structurées sont transformatrices pour ta santé.",
        "Établis une routine de santé simple mais non négociable.",
        "Respire en visualisant ton corps comme une structure solide et bien entretenue.",
        "Quelle habitude de santé puis-je institutionnaliser dans ma vie ? »"),

    ('capricorn', 7): make_pluto_interp('capricorn', 7,
        "Tu transformes ta vie par des partenariats solides et des engagements sérieux.",
        "Pluton en Capricorne dans ta maison VII attire des partenaires ambitieux et structurés. Le couple est une institution à bâtir avec sérieux et engagement.",
        "Éviter les relations basées uniquement sur le statut ou le contrôle. Le défi est de créer des partenariats d'égal à égal, pas de hiérarchie.",
        "Tes associations ont une dimension professionnelle ou officielle. Le partenaire peut être plus âgé ou représenter l'autorité. Les contrats sont sérieux et à long terme.",
        "Évalue la solidité des fondations d'un partenariat important dans ta vie.",
        "Respire en visualisant des relations construites sur des bases solides.",
        "Quelle structure relationnelle ai-je besoin de renforcer ? »"),

    ('capricorn', 8): make_pluto_interp('capricorn', 8,
        "Tu transformes ta vie par une gestion stratégique des ressources partagées et du pouvoir.",
        "Pluton en Capricorne dans ta maison VIII te donne un sens aigu des dynamiques de pouvoir. Tu navigues les transformations avec stratégie et contrôle.",
        "Éviter l'obsession du contrôle dans les moments de crise. Le défi est d'accepter les transformations que tu ne peux pas contrôler tout en agissant sur ce que tu peux.",
        "La sexualité peut être structurée ou retenue. Les héritages impliquent souvent des entreprises ou des positions de pouvoir. Tu gères les crises avec compétence.",
        "Accepte consciemment quelque chose que tu ne peux pas contrôler.",
        "Respire en trouvant la paix dans ce qui dépasse ton pouvoir.",
        "Quel pouvoir dois-je lâcher pour avancer dans ma transformation ? »"),

    ('capricorn', 9): make_pluto_interp('capricorn', 9,
        "Tu transformes ta vie par une philosophie pragmatique et des ambitions éducatives.",
        "Pluton en Capricorne dans ta maison IX fait de ta spiritualité une discipline. Ta philosophie est pratique, orientée vers les résultats, testée par l'expérience.",
        "Éviter le cynisme ou le rejet de tout ce qui ne peut pas être prouvé. Le défi est de trouver la sagesse dans la structure sans rejeter le mystère.",
        "L'éducation supérieure est une ascension. Les voyages ont une dimension professionnelle ou d'établissement de contacts. Tu enseignes par l'exemple et l'autorité.",
        "Applique concrètement une sagesse que tu as apprise théoriquement.",
        "Respire en intégrant la sagesse dans tes structures quotidiennes.",
        "Quelle vérité puis-je incarner plus concrètement dans ma vie ? »"),

    ('capricorn', 10): make_pluto_interp('capricorn', 10,
        "Tu transformes ta vie par une carrière de pouvoir et de transformation des structures.",
        "Pluton en Capricorne dans ta maison X (son domicile naturel) te destine à une position de pouvoir et d'influence. Ta carrière est une montagne à gravir avec détermination.",
        "Éviter l'abus de pouvoir ou l'obsession du statut. Le défi est d'utiliser ton influence pour transformer les structures de façon juste et durable.",
        "Ta carrière passe par des transformations de pouvoir significatives. Tu peux devenir une figure d'autorité dans ton domaine. Le succès vient avec le temps et la persévérance.",
        "Visualise le sommet de ta carrière et les étapes pour y arriver.",
        "Respire en ressentant la patience et la détermination d'un alpiniste.",
        "Quel héritage de pouvoir responsable veux-je laisser ? »"),

    ('capricorn', 11): make_pluto_interp('capricorn', 11,
        "Tu transformes ta vie par des réseaux stratégiques et des projets institutionnels.",
        "Pluton en Capricorne dans ta maison XI t'amène des amis influents et des connexions professionnelles. Tes projets collectifs visent à transformer les structures sociales.",
        "Éviter d'utiliser les amitiés uniquement pour avancer ou de ne rejoindre que des groupes de pouvoir. Le défi est de contribuer aux structures collectives avec intégrité.",
        "Tes réseaux sont composés de personnes établies et influentes. Les projets collectifs concernent les institutions, la politique, les structures économiques.",
        "Contribue à un projet collectif qui transforme une structure existante.",
        "Respire en visualisant des réseaux de personnes engagées à améliorer le monde.",
        "Comment mes connexions peuvent-elles transformer les structures existantes ? »"),

    ('capricorn', 12): make_pluto_interp('capricorn', 12,
        "Tu transformes ta vie par une confrontation avec les structures intérieures rigides.",
        "Pluton en Capricorne dans ta maison XII te confronte à l'ombre de ton ambition — peur de l'échec, rigidité inconsciente, autorité intériorisée. Ton travail est de libérer les structures qui t'emprisonnent.",
        "Éviter de fuir la réussite ou de saboter inconsciemment tes ambitions. Le défi est de transformer les structures intérieures limitantes en fondations pour ta croissance.",
        "L'inconscient porte des voix d'autorité à identifier et à transformer. Les retraites structurées ou les thérapies à long terme sont transformatrices. Le karma professionnel se résout.",
        "Identifie une croyance rigide inconsciente et questionne-la avec douceur.",
        "Respire en visualisant les murs intérieurs qui deviennent des fenêtres.",
        "Quelle structure intérieure m'emprisonne et demande à être transformée ? »"),

    # === AQUARIUS (M1-M12) ===
    ('aquarius', 1): make_pluto_interp('aquarius', 1,
        "Tu transformes ta vie par une expression radicale de ton unicité et de ta vision révolutionnaire.",
        "Pluton en Verseau dans ta maison I te donne une présence électrique et avant-gardiste. Tu incarnes le changement et la révolution avec une intensité qui déstabilise le statu quo.",
        "Apprendre à te connecter émotionnellement tout en restant unique. Ton détachement peut devenir froid si tu oublies l'humanité dans la révolution.",
        "Ton apparence est originale, parfois provocante, toujours unique. Les transformations personnelles sont soudaines et radicales. Tu renais par les ruptures et les éveils de conscience.",
        "Regarde-toi dans un miroir et célèbre ce qui te rend absolument unique.",
        "Respire en visualisant un éclair de conscience qui illumine ta singularité.",
        "Quelle révolution personnelle suis-je appelé(e) à incarner ? »"),

    ('aquarius', 2): make_pluto_interp('aquarius', 2,
        "Tu transformes ta vie par une relation révolutionnaire à l'argent et aux valeurs.",
        "Pluton en Verseau dans ta maison II révolutionne ton rapport aux ressources. Tu peux inventer de nouvelles façons de créer de la valeur ou rejeter complètement le système.",
        "Éviter l'instabilité financière par idéalisme ou le rejet total de la sécurité. Ton défi est de créer de nouvelles formes de prospérité sans te mettre en danger.",
        "Tes revenus viennent de domaines innovants ou technologiques. Les possessions sont originales ou partagées différemment. Tu remets en question ce que signifie vraiment « avoir ».",
        "Imagine une nouvelle façon de penser la valeur et l'échange.",
        "Respire en visualisant des formes innovantes d'abondance.",
        "Quelle nouvelle relation à l'argent suis-je en train d'inventer ? »"),

    ('aquarius', 3): make_pluto_interp('aquarius', 3,
        "Tu transformes ta vie par une communication révolutionnaire et des idées avant-gardistes.",
        "Pluton en Verseau dans ta maison III fait de ta parole un vecteur de changement. Tu penses en dehors des cadres et communiques des idées qui transforment les esprits.",
        "Éviter l'arrogance intellectuelle ou le rejet systématique des idées conventionnelles. Le défi est de révolutionner la pensée tout en restant compréhensible.",
        "Les relations avec frères, sœurs ou voisins sont stimulantes et parfois électriques. L'apprentissage est non-conventionnel. Tu excelles dans les nouvelles technologies de communication.",
        "Partage une idée originale qui pourrait changer la perspective de quelqu'un.",
        "Respire en sentant l'électricité des idées nouvelles qui traversent ton esprit.",
        "Quelle idée révolutionnaire demande à être communiquée ? »"),

    ('aquarius', 4): make_pluto_interp('aquarius', 4,
        "Tu transformes ta vie par une redéfinition radicale de la famille et du foyer.",
        "Pluton en Verseau dans ta maison IV révolutionne ta notion de foyer. Les racines familiales peuvent être non-conventionnelles ou en rupture avec la tradition.",
        "Éviter de couper complètement avec tes racines ou de rejeter toute structure familiale. Le défi est de créer des liens familiaux qui honorent à la fois la liberté et l'appartenance.",
        "Ton espace de vie est original, peut-être technologique ou communautaire. La relation aux parents implique des ruptures ou des réconciliations radicales. Les traditions sont réinventées.",
        "Crée un rituel familial complètement nouveau et significatif pour toi.",
        "Respire en visualisant un foyer qui combine liberté et appartenance.",
        "Comment puis-je réinventer ma notion de famille et de foyer ? »"),

    ('aquarius', 5): make_pluto_interp('aquarius', 5,
        "Tu transformes ta vie par une créativité révolutionnaire et des amours libres.",
        "Pluton en Verseau dans ta maison V fait de ta créativité une force de changement social. Tes œuvres sont innovantes, parfois choquantes. L'amour refuse les cadres conventionnels.",
        "Éviter la froideur émotionnelle au nom de la liberté ou la création purement provocatrice. Le défi est d'innover avec cœur, pas juste avec esprit.",
        "Les romances sont non-conventionnelles, libres, parfois à distance ou virtuelles. La relation aux enfants est basée sur la liberté et le respect de leur unicité. Le jeu est expérimental.",
        "Crée quelque chose qui sort complètement de tes habitudes.",
        "Respire en libérant ta créativité de toute attente ou convention.",
        "Quelle création révolutionnaire demande à naître de moi ? »"),

    ('aquarius', 6): make_pluto_interp('aquarius', 6,
        "Tu transformes ta vie par un travail innovant et une approche révolutionnaire de la santé.",
        "Pluton en Verseau dans ta maison VI révolutionne ton rapport au travail quotidien. Ta santé bénéficie d'approches nouvelles et parfois expérimentales.",
        "Éviter de rejeter toute routine ou de tester des approches de santé dangereuses. Le défi est d'innover dans le quotidien tout en maintenant une base stable.",
        "Ton travail implique la technologie, l'innovation ou des environnements non-conventionnels. Le système nerveux et la circulation sont tes zones sensibles. Les approches de santé futuristes t'attirent.",
        "Essaie une nouvelle façon de faire une tâche quotidienne.",
        "Respire en visualisant ton corps comme un système intelligent qui s'adapte.",
        "Comment puis-je innover dans ma routine quotidienne ? »"),

    ('aquarius', 7): make_pluto_interp('aquarius', 7,
        "Tu transformes ta vie par des partenariats égalitaires et des relations non-conventionnelles.",
        "Pluton en Verseau dans ta maison VII attire des partenaires originaux et indépendants. Le couple est un espace d'expérimentation et de liberté mutuelle.",
        "Éviter le détachement émotionnel ou les relations si libres qu'elles perdent leur profondeur. Le défi est de créer des partenariats à la fois libres et intimement connectés.",
        "Tes associations sont basées sur des valeurs partagées plus que sur des conventions. Le partenaire peut être excentrique ou très indépendant. Les contrats sont réinventés.",
        "Discute avec un partenaire de comment réinventer ensemble vos règles de relation.",
        "Respire en visualisant des partenariats où liberté et intimité coexistent.",
        "Comment puis-je créer plus de liberté ET de connexion dans mes relations ? »"),

    ('aquarius', 8): make_pluto_interp('aquarius', 8,
        "Tu transformes ta vie par une exploration révolutionnaire des mystères et du pouvoir.",
        "Pluton en Verseau dans ta maison VIII révolutionne ton rapport à la transformation. Tu peux expérimenter avec les frontières de la conscience et de la mort/renaissance.",
        "Éviter les expériences extrêmes sans ancrage ou le détachement face aux crises. Le défi est de traverser les transformations avec ton cœur, pas juste ton esprit.",
        "La sexualité peut être expérimentale ou détachée. Les héritages peuvent impliquer des technologies ou des idées plutôt que des biens matériels. Tu explores les frontières de la psyché.",
        "Explore consciemment une limite de ta conscience ou de ton confort.",
        "Respire en accueillant les territoires inconnus de ton être.",
        "Quelle frontière intérieure suis-je appelé(e) à explorer ? »"),

    ('aquarius', 9): make_pluto_interp('aquarius', 9,
        "Tu transformes ta vie par une philosophie révolutionnaire et une vision du futur.",
        "Pluton en Verseau dans ta maison IX fait de ta spiritualité une vision futuriste. Ta philosophie est progressiste, orientée vers l'évolution collective et l'innovation.",
        "Éviter le rejet de toute sagesse ancienne ou la croyance aveugle dans le progrès. Le défi est d'intégrer le meilleur du passé dans ta vision du futur.",
        "L'éducation supérieure peut être alternative ou à distance. Les voyages sont vers des lieux d'innovation ou des communautés alternatives. Tu enseignes le changement.",
        "Étudie une idée ou une technologie qui pourrait changer le futur.",
        "Respire en visualisant un futur lumineux que tu contribues à créer.",
        "Quelle vision du futur suis-je appelé(e) à transmettre ? »"),

    ('aquarius', 10): make_pluto_interp('aquarius', 10,
        "Tu transformes ta vie par une carrière qui change le monde et bouscule les conventions.",
        "Pluton en Verseau dans ta maison X te destine à une réputation d'innovateur ou de révolutionnaire. Ta carrière vise à transformer les structures sociales.",
        "Éviter de sacrifier ta carrière pour l'idéalisme ou de te marginaliser par rébellion. Le défi est d'influencer le système depuis l'intérieur ou l'extérieur de façon stratégique.",
        "Ta carrière passe par des ruptures et des réinventions. Tu peux exceller dans la technologie, les causes sociales, l'innovation. Ton parcours est non-linéaire mais visionnaire.",
        "Visualise comment ta carrière peut contribuer à un monde meilleur.",
        "Respire en ressentant ton rôle unique dans l'évolution collective.",
        "Quel changement social ma carrière peut-elle catalyser ? »"),

    ('aquarius', 11): make_pluto_interp('aquarius', 11,
        "Tu transformes ta vie par des réseaux révolutionnaires et des mouvements de changement.",
        "Pluton en Verseau dans ta maison XI (son domicile naturel) fait de toi un catalyseur de changement collectif. Tes amitiés et projets visent la transformation sociale.",
        "Éviter de perdre ton individualité dans le groupe ou de devenir tyrannique pour la cause. Le défi est de contribuer au changement tout en honorant la diversité.",
        "Tes réseaux sont composés d'innovateurs, de marginaux, de visionnaires. Les projets collectifs concernent la technologie, les droits humains, l'évolution sociale.",
        "Rejoins ou soutiens un mouvement qui correspond à tes valeurs de changement.",
        "Respire en visualisant un réseau mondial d'agents de changement.",
        "Comment puis-je mieux contribuer à la révolution collective en cours ? »"),

    ('aquarius', 12): make_pluto_interp('aquarius', 12,
        "Tu transformes ta vie par une libération des conditionnements collectifs inconscients.",
        "Pluton en Verseau dans ta maison XII te confronte à l'ombre de l'humanité — conditionnements collectifs, aliénation, peur de la liberté. Ton travail est la libération des chaînes invisibles.",
        "Éviter de fuir dans l'utopie ou de te déconnecter de l'humanité par idéalisme. Le défi est de rester ancré tout en travaillant à la libération collective.",
        "L'inconscient porte des mémoires collectives de révolution et d'oppression. Les pratiques qui connectent au champ collectif sont transformatrices. Tu guéris les blessures de l'humanité.",
        "Médite en te connectant consciemment à l'humanité entière.",
        "Respire en visualisant les chaînes invisibles de l'inconscient collectif qui se dissolvent.",
        "Quel conditionnement collectif suis-je en train de libérer à travers moi ? »"),

    # === PISCES (M1-M12) ===
    ('pisces', 1): make_pluto_interp('pisces', 1,
        "Tu transformes ta vie par une dissolution des frontières de l'égo et une connexion au tout.",
        "Pluton en Poissons dans ta maison I te donne une présence mystique et insaisissable. Tu incarnes la compassion, la créativité et la connexion au divin avec une profondeur transformatrice.",
        "Apprendre à maintenir des limites claires tout en restant perméable. Ta sensibilité peut devenir fuite si tu ne l'ancres pas dans la réalité.",
        "Ton apparence est fluide, changeante, parfois insaisissable. Les transformations personnelles passent par la dissolution et la renaissance spirituelle. Tu renais par le lâcher-prise.",
        "Regarde-toi dans un miroir et vois au-delà de l'apparence physique.",
        "Respire en laissant les frontières de ton être se dissoudre dans l'infini.",
        "Quelle part de mon égo suis-je prêt(e) à laisser se dissoudre ? »"),

    ('pisces', 2): make_pluto_interp('pisces', 2,
        "Tu transformes ta vie par un rapport spirituel et détaché à l'argent.",
        "Pluton en Poissons dans ta maison II lie ta valeur personnelle à ta connexion spirituelle. L'argent vient et va comme les marées — tu apprends le détachement.",
        "Éviter la négligence financière ou la croyance que la spiritualité exclut la prospérité. Ton défi est de valoriser tes dons intuitifs tout en maintenant une base matérielle.",
        "Tes revenus peuvent venir de domaines artistiques, spirituels ou de guérison. Les possessions sont peu importantes — tu valorises l'intangible. L'argent peut avoir une dimension karmique.",
        "Donne quelque chose sans attente de retour et observe ce qui circule.",
        "Respire en visualisant l'abondance comme un océan infini disponible.",
        "Comment puis-je mieux équilibrer spiritualité et prospérité matérielle ? »"),

    ('pisces', 3): make_pluto_interp('pisces', 3,
        "Tu transformes ta vie par une communication intuitive et une pensée visionnaire.",
        "Pluton en Poissons dans ta maison III fait de ta parole une poésie transformatrice. Tu communiques par l'intuition, l'art, les symboles plus que par la logique pure.",
        "Éviter la confusion mentale ou le mensonge par omission. Le défi est de communiquer clairement tout en honorant le mystère et la nuance.",
        "Les relations avec frères, sœurs ou voisins sont empathiques et parfois télépathiques. L'apprentissage passe par l'intuition et l'imagination. Tu captes l'essence au-delà des mots.",
        "Écris quelque chose d'intuitif sans te soucier de la logique.",
        "Respire en laissant les mots émerger de l'océan de ton inconscient.",
        "Quel message intuitif demande à être communiqué ? »"),

    ('pisces', 4): make_pluto_interp('pisces', 4,
        "Tu transformes ta vie par une dissolution des frontières familiales et une compassion ancestrale.",
        "Pluton en Poissons dans ta maison IV fait de ton foyer un sanctuaire spirituel. Les racines familiales portent des dons mystiques ou des blessures à guérir par la compassion.",
        "Éviter de te perdre dans les drames familiaux ou de porter les fardeaux émotionnels des autres. Le défi est de compatir sans te noyer.",
        "Ton espace de vie est un refuge de paix et de créativité. La relation à la mère ou aux ancêtres a une dimension mystique. Les mémoires familiales remontent par vagues.",
        "Crée un espace sacré dans ton foyer, même minuscule.",
        "Respire en visualisant ton foyer comme un temple de paix et de guérison.",
        "Quelle mémoire ancestrale demande à être guérie par ma compassion ? »"),

    ('pisces', 5): make_pluto_interp('pisces', 5,
        "Tu transformes ta vie par une créativité transcendante et des amours fusionnelles.",
        "Pluton en Poissons dans ta maison V fait de ta créativité une porte vers le divin. Tes œuvres touchent l'âme et éveillent la transcendance. L'amour est une dissolution des frontières.",
        "Éviter les amours addictives ou la créativité qui sert à fuir la réalité. Le défi est de créer et aimer depuis l'amour universel, pas depuis le besoin.",
        "Les romances sont spirituelles, parfois idéalisées ou impossibles. La relation aux enfants est intuitive et créative. Le jeu est imaginatif et sans frontières.",
        "Crée quelque chose sans but, juste pour le plaisir de laisser couler l'inspiration.",
        "Respire en laissant la créativité universelle s'exprimer à travers toi.",
        "Quelle création divine demande à naître de moi ? »"),

    ('pisces', 6): make_pluto_interp('pisces', 6,
        "Tu transformes ta vie par un service compassionnel et une santé spirituelle.",
        "Pluton en Poissons dans ta maison VI fait du travail quotidien un acte de dévotion. Ta santé est intimement liée à ton état spirituel et émotionnel.",
        "Éviter de t'épuiser au service des autres ou de négliger ta santé physique pour la spiritualité. Le défi est de prendre soin de ton corps comme d'un temple sacré.",
        "Ton travail idéal implique le soin, la guérison ou l'art. Les pieds et le système lymphatique demandent attention. Les pratiques spirituelles comme la méditation sont thérapeutiques.",
        "Fais une tâche quotidienne comme un acte sacré, avec dévotion.",
        "Respire en visualisant chaque cellule de ton corps baignée de lumière divine.",
        "Comment puis-je mieux servir par mon travail quotidien ? »"),

    ('pisces', 7): make_pluto_interp('pisces', 7,
        "Tu transformes ta vie par des partenariats d'âme et des relations de fusion spirituelle.",
        "Pluton en Poissons dans ta maison VII attire des partenaires avec qui tu partages une connexion d'âme. Le couple est un espace de transcendance et de guérison mutuelle.",
        "Éviter de te perdre dans l'autre ou d'idéaliser les relations. Le défi est de créer des partenariats où chacun reste entier tout en fusionnant spirituellement.",
        "Tes associations ont une dimension karmique ou spirituelle. Le partenaire peut être artiste, guérisseur ou très sensible. Les frontières sont fluides — apprendre à les maintenir.",
        "Médite en visualisant une relation parfaitement équilibrée entre fusion et individualité.",
        "Respire en ressentant la connexion d'âme possible avec l'autre.",
        "Comment puis-je aimer profondément sans me perdre ? »"),

    ('pisces', 8): make_pluto_interp('pisces', 8,
        "Tu transformes ta vie par une exploration mystique des royaumes au-delà de la mort.",
        "Pluton en Poissons dans ta maison VIII te connecte aux mystères ultimes avec une sensibilité extrême. Tu as un accès naturel aux dimensions invisibles et aux processus de transcendance.",
        "Éviter de te perdre dans l'occulte ou de fuir la réalité par la fascination de la mort. Le défi est de traverser les voiles tout en restant ancré dans la vie.",
        "La sexualité peut être tantrique ou transcendante. Les héritages incluent des dons psychiques ou des karmas à transmuter. Tu accompagnes les mourants avec une grâce naturelle.",
        "Médite sur ce qui existe au-delà de la mort avec confiance et paix.",
        "Respire en accueillant le mystère de la mort comme une porte, pas une fin.",
        "Quel voile entre les mondes suis-je appelé(e) à traverser ? »"),

    ('pisces', 9): make_pluto_interp('pisces', 9,
        "Tu transformes ta vie par une spiritualité mystique et une sagesse universelle.",
        "Pluton en Poissons dans ta maison IX fait de ta spiritualité une voie de dissolution dans le divin. Ta philosophie est celle de l'amour universel et de l'unité de toutes choses.",
        "Éviter le fanatisme mystique ou la fuite dans des croyances qui déconnectent de la réalité. Le défi est de trouver l'unité sans perdre ton discernement.",
        "L'éducation supérieure peut être en spiritualité, art ou psychologie des profondeurs. Les voyages vers des lieux sacrés ou près de l'eau sont transformateurs. Tu enseignes l'amour.",
        "Médite en te sentant un avec l'univers entier.",
        "Respire en dissolvant toute séparation entre toi et le cosmos.",
        "Quelle sagesse universelle suis-je appelé(e) à incarner et transmettre ? »"),

    ('pisces', 10): make_pluto_interp('pisces', 10,
        "Tu transformes ta vie par une carrière de service et de compassion universelle.",
        "Pluton en Poissons dans ta maison X te destine à une réputation liée à la spiritualité, l'art ou le soin. Ta carrière est un véhicule de compassion pour le monde.",
        "Éviter de fuir les responsabilités ou de sacrifier ta carrière au nom de la spiritualité. Le défi est de réussir dans le monde tout en servant quelque chose de plus grand.",
        "Ta carrière passe par des phases de dissolution et de reconstruction. Tu peux exceller dans les arts, la guérison, les causes humanitaires. Le succès vient par le lâcher-prise.",
        "Visualise ta carrière comme un service au monde plutôt qu'une quête personnelle.",
        "Respire en offrant les fruits de ton travail à quelque chose de plus grand.",
        "Comment ma carrière peut-elle mieux servir la guérison du monde ? »"),

    ('pisces', 11): make_pluto_interp('pisces', 11,
        "Tu transformes ta vie par des amitiés spirituelles et des projets de compassion collective.",
        "Pluton en Poissons dans ta maison XI t'amène des amis d'âme et des projets humanitaires. Tes réseaux visent la guérison et l'éveil collectif.",
        "Éviter de te perdre dans des groupes ou de confondre compassion et absence de limites. Le défi est de contribuer aux causes collectives tout en préservant ton énergie.",
        "Tes réseaux sont composés de mystiques, d'artistes, de guérisseurs. Les projets collectifs concernent la spiritualité, l'art, les causes humanitaires.",
        "Connecte-toi à un groupe qui partage tes aspirations spirituelles ou humanitaires.",
        "Respire en visualisant un réseau mondial d'âmes dévouées à la guérison.",
        "Comment mes connexions peuvent-elles servir la guérison collective ? »"),

    ('pisces', 12): make_pluto_interp('pisces', 12,
        "Tu transformes ta vie par une dissolution totale dans l'océan de l'inconscient universel.",
        "Pluton en Poissons dans ta maison XII (triple domicile) te donne un accès direct aux profondeurs de l'inconscient collectif. Tu es un canal pour la guérison et la transformation spirituelle.",
        "Éviter de te dissoudre complètement ou de te perdre dans les dimensions invisibles. Le défi est de naviguer les océans intérieurs tout en maintenant ton ancrage.",
        "L'inconscient est un océan infini de sagesse et de guérison. Les retraites en silence ou près de l'eau sont profondément transformatrices. Tu guéris l'humanité par ta propre dissolution.",
        "Médite en te laissant dissoudre dans l'océan de la conscience universelle.",
        "Respire en laissant aller toute frontière entre toi et l'infini.",
        "Quelle guérison universelle passe à travers moi quand je me laisse être ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in PLUTO_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'pluto',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP pluto/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='pluto',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT pluto/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
