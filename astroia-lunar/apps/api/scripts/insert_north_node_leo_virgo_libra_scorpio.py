#!/usr/bin/env python3
"""Insert North Node interpretations for Leo, Virgo, Libra, Scorpio (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_nn_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'leo': '☊ Nœud Nord en Lion',
        'virgo': '☊ Nœud Nord en Vierge',
        'libra': '☊ Nœud Nord en Balance',
        'scorpio': '☊ Nœud Nord en Scorpion',
    }
    sign_fr = {
        'leo': 'Lion',
        'virgo': 'Vierge',
        'libra': 'Balance',
        'scorpio': 'Scorpion',
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

NORTH_NODE_INTERPRETATIONS = {
    # === LEO (M1-M12) ===
    ('leo', 1): make_nn_interp('leo', 1,
        "Ton chemin d'âme t'appelle à briller et à exprimer ta créativité unique.",
        "Le Nœud Nord en Lion dans ta maison I t'invite à développer ton rayonnement personnel. Tu quittes l'anonymat du Verseau pour la lumière du Lion.",
        "Oser être le centre de l'attention et montrer ta créativité. Ta tendance à te fondre dans le groupe ou à intellectualiser te freine dans ton expression personnelle.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à briller, à être fier de toi, à rayonner ta lumière unique sans te cacher.",
        "Fais quelque chose qui te met en avant, même modestement.",
        "Respire en visualisant un soleil doré qui brille dans ta poitrine.",
        "Comment puis-je briller davantage aujourd'hui ? »"),

    ('leo', 2): make_nn_interp('leo', 2,
        "Ton chemin d'âme t'appelle à valoriser ta créativité et tes talents uniques.",
        "Le Nœud Nord en Lion dans ta maison II t'invite à développer la fierté de ta valeur. Tu quittes la dépendance aux réseaux pour créer ta propre richesse par tes talents.",
        "Oser monétiser tes dons créatifs et être fier de ce que tu gagnes. Ta tendance à partager ou à minimiser ta valeur te freine dans ta prospérité.",
        "Tes finances sont le terrain de ton évolution. Tu apprends que TES talents valent de l'or, que ta créativité est ta richesse.",
        "Identifie un talent créatif et imagine comment il pourrait te rapporter.",
        "Respire en ressentant la valeur de ta lumière intérieure.",
        "Quelle richesse créative ai-je négligé de valoriser ? »"),

    ('leo', 3): make_nn_interp('leo', 3,
        "Ton chemin d'âme t'appelle à communiquer avec créativité et charisme.",
        "Le Nœud Nord en Lion dans ta maison III t'invite à développer une expression personnelle audacieuse. Tu quittes l'objectivité froide pour la communication passionnée.",
        "Oser mettre ta personnalité dans ta communication. Ta tendance à rester neutre ou à parler pour le groupe te freine dans ton expression unique.",
        "Ta communication est le terrain de ton évolution. Tu apprends à parler avec passion, à écrire avec style, à charmer par les mots.",
        "Dis quelque chose avec enthousiasme et personnalité, pas de façon neutre.",
        "Respire en sentant ta voix devenir chaude et rayonnante.",
        "Comment puis-je communiquer avec plus de créativité et de charisme ? »"),

    ('leo', 4): make_nn_interp('leo', 4,
        "Ton chemin d'âme t'appelle à créer un foyer où tu peux briller.",
        "Le Nœud Nord en Lion dans ta maison IV t'invite à développer un royaume personnel. Tu quittes l'ambition sociale pour la création d'un foyer royal.",
        "Oser être le roi ou la reine de ton propre foyer. Ta tendance à chercher la reconnaissance externe te freine dans la création de ton sanctuaire.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer un espace qui te ressemble, à être fier de ta maison, à rayonner dans ta vie privée.",
        "Décore ou améliore quelque chose dans ton foyer qui te rend fier.",
        "Respire en visualisant ton foyer comme un palais de lumière.",
        "Comment puis-je mieux exprimer ma créativité dans mon foyer ? »"),

    ('leo', 5): make_nn_interp('leo', 5,
        "Ton chemin d'âme t'appelle à créer, aimer et jouer avec passion.",
        "Le Nœud Nord en Lion dans ta maison V (son domicile naturel) t'invite à développer pleinement ta joie créatrice. Tu quittes les idéaux collectifs pour la création personnelle.",
        "Oser créer pour toi-même et aimer passionnément. Ta tendance à penser au groupe ou à l'avenir te freine dans la joie du moment présent.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'art de la création audacieuse, de l'amour dramatique, du jeu joyeux.",
        "Crée quelque chose de grandiose et audacieux, juste pour le plaisir.",
        "Respire en laissant la joie créatrice exploser dans ta poitrine.",
        "Quelle création magnifique ai-je peur de montrer au monde ? »"),

    ('leo', 6): make_nn_interp('leo', 6,
        "Ton chemin d'âme t'appelle à briller dans ton travail quotidien.",
        "Le Nœud Nord en Lion dans ta maison VI t'invite à apporter de la créativité et du charisme dans le quotidien. Tu quittes la fuite ou le sacrifice pour le leadership au travail.",
        "Oser te distinguer et prendre des initiatives au travail. Ta tendance à te sacrifier ou à te cacher te freine dans ta contribution unique.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends à être fier de ton travail, à briller dans les tâches quotidiennes, à prendre soin de toi avec dignité.",
        "Fais une tâche quotidienne avec excellence et fierté.",
        "Respire en ressentant la dignité de chaque geste quotidien.",
        "Comment puis-je briller davantage dans mon travail quotidien ? »"),

    ('leo', 7): make_nn_interp('leo', 7,
        "Ton chemin d'âme t'appelle à briller dans tes relations.",
        "Le Nœud Nord en Lion dans ta maison VII t'invite à apporter de la chaleur et de la générosité dans tes partenariats. Tu quittes l'indépendance froide pour l'amour généreux.",
        "Oser être aimant et généreux dans le couple. Ta tendance à l'autonomie ou à la distance émotionnelle te freine dans la création de liens chaleureux.",
        "Tes relations sont le terrain de ton évolution. Tu apprends à aimer généreusement, à être fier de tes partenaires, à créer du couple un espace de joie.",
        "Fais un geste généreux et chaleureux envers un partenaire.",
        "Respire en visualisant tes relations baignées de lumière dorée.",
        "Comment puis-je être plus généreux et rayonnant dans mes relations ? »"),

    ('leo', 8): make_nn_interp('leo', 8,
        "Ton chemin d'âme t'appelle à traverser les transformations avec dignité.",
        "Le Nœud Nord en Lion dans ta maison VIII t'invite à apporter la lumière dans les moments sombres. Tu quittes l'attachement aux possessions pour la noblesse face aux crises.",
        "Oser rester digne et créatif même dans les transformations profondes. Ta tendance à t'accrocher à la sécurité te freine dans la renaissance glorieuse.",
        "Les transformations sont le terrain de ton évolution. Tu apprends à mourir et renaître comme un roi phénix, avec dignité et créativité.",
        "Face à une épreuve, trouve une façon créative et digne de la traverser.",
        "Respire en visualisant un lion qui traverse le feu sans brûler.",
        "Comment puis-je transformer mes épreuves en triomphe créatif ? »"),

    ('leo', 9): make_nn_interp('leo', 9,
        "Ton chemin d'âme t'appelle à partager ta vision avec passion.",
        "Le Nœud Nord en Lion dans ta maison IX t'invite à développer une philosophie personnelle passionnée. Tu quittes l'accumulation d'informations pour l'enseignement inspirant.",
        "Oser enseigner et partager ta vérité avec charisme. Ta tendance à rester un éternel étudiant ou à garder tes idées pour toi te freine.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends à être un guide inspirant, à voyager comme un roi, à professer ta foi avec passion.",
        "Partage une sagesse personnelle avec enthousiasme et conviction.",
        "Respire en sentant la flamme de ta vérité qui demande à rayonner.",
        "Quelle sagesse ai-je à enseigner au monde ? »"),

    ('leo', 10): make_nn_interp('leo', 10,
        "Ton chemin d'âme t'appelle à devenir une figure publique rayonnante.",
        "Le Nœud Nord en Lion dans ta maison X t'invite à développer une carrière où tu peux briller. Tu quittes l'ombre familiale pour la lumière publique.",
        "Oser prendre le leadership et être reconnu pour ta créativité. Ta tendance à rester dans la sécurité du foyer te freine dans ton ascension.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à diriger avec charisme, à créer une réputation royale, à inspirer par ta présence.",
        "Prends une initiative de leadership visible dans ta carrière.",
        "Respire en visualisant une couronne sur ta tête qui symbolise ton autorité naturelle.",
        "Quel leadership créatif suis-je appelé(e) à exercer ? »"),

    ('leo', 11): make_nn_interp('leo', 11,
        "Ton chemin d'âme t'appelle à inspirer les groupes par ta créativité.",
        "Le Nœud Nord en Lion dans ta maison XI t'invite à devenir une source d'inspiration pour les autres. Tu quittes la créativité solitaire pour l'impact sur le collectif.",
        "Oser être un leader créatif dans les groupes. Ta tendance à créer seul ou à chercher l'attention personnelle te freine dans ton influence collective.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à inspirer les autres, à être une figure charismatique du groupe, à porter des causes avec passion.",
        "Partage un de tes talents créatifs avec un groupe.",
        "Respire en visualisant ta lumière qui inspire un cercle d'amis.",
        "Comment puis-je inspirer mes amis et communautés par ma créativité ? »"),

    ('leo', 12): make_nn_interp('leo', 12,
        "Ton chemin d'âme t'appelle à développer une créativité spirituelle.",
        "Le Nœud Nord en Lion dans ta maison XII t'invite à découvrir ta lumière intérieure secrète. Tu quittes l'anxiété du quotidien pour la joie de la connexion spirituelle.",
        "Oser briller intérieurement sans besoin d'audience. Ta tendance à t'inquiéter des détails ou à servir les autres te freine dans ta joie spirituelle.",
        "L'inconscient est le terrain de ton évolution. Tu apprends la joie de la méditation, la créativité de l'invisible, le rayonnement silencieux.",
        "Crée quelque chose de beau en secret, comme une offrande à ton âme.",
        "Respire en visualisant un soleil qui brille au centre de ton être, invisible mais puissant.",
        "Quelle lumière intérieure ai-je peur de reconnaître en moi ? »"),

    # === VIRGO (M1-M12) ===
    ('virgo', 1): make_nn_interp('virgo', 1,
        "Ton chemin d'âme t'appelle à développer le discernement et l'efficacité.",
        "Le Nœud Nord en Vierge dans ta maison I t'invite à développer ta présence pratique et attentive. Tu quittes la confusion des Poissons pour la clarté de la Vierge.",
        "Apprendre à être présent et précis plutôt que de fuir dans l'imaginaire. Ta tendance à la confusion, à l'évasion ou au sacrifice te freine dans ton affirmation.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être clair, précis, organisé, utile dans ta façon d'être.",
        "Fais quelque chose de très concret et précis aujourd'hui.",
        "Respire en visualisant un mental clair et un corps présent.",
        "Quel aspect de ma vie a besoin de plus de clarté et d'organisation ? »"),

    ('virgo', 2): make_nn_interp('virgo', 2,
        "Ton chemin d'âme t'appelle à construire ta valeur par le travail consciencieux.",
        "Le Nœud Nord en Vierge dans ta maison II t'invite à développer ta valeur par tes compétences. Tu quittes la dépendance aux ressources partagées pour créer ta propre valeur.",
        "Apprendre à gagner par ton travail et tes compétences pratiques. Ta tendance aux transformations dramatiques ou à la dépendance te freine dans ta prospérité.",
        "Tes finances sont le terrain de ton évolution. Tu apprends que ta valeur vient de ton travail, de tes compétences, de ton attention aux détails.",
        "Améliore une compétence pratique qui peut te rapporter de l'argent.",
        "Respire en ressentant la valeur de ton travail bien fait.",
        "Quelle compétence pratique ai-je négligé de développer ? »"),

    ('virgo', 3): make_nn_interp('virgo', 3,
        "Ton chemin d'âme t'appelle à communiquer avec précision et utilité.",
        "Le Nœud Nord en Vierge dans ta maison III t'invite à développer une communication claire et utile. Tu quittes les grandes théories pour l'information pratique.",
        "Apprendre à être précis et concret dans ta communication. Ta tendance à philosopher ou à rester dans l'abstrait te freine dans l'échange efficace.",
        "Ta communication est le terrain de ton évolution. Tu apprends l'écriture claire, l'écoute attentive, le partage d'informations utiles.",
        "Communique une information précise et utile à quelqu'un aujourd'hui.",
        "Respire en sentant tes mots devenir clairs et bien choisis.",
        "Comment puis-je communiquer plus clairement et utilement ? »"),

    ('virgo', 4): make_nn_interp('virgo', 4,
        "Ton chemin d'âme t'appelle à créer un foyer organisé et fonctionnel.",
        "Le Nœud Nord en Vierge dans ta maison IV t'invite à développer un espace de vie pratique et sain. Tu quittes le chaos ou l'ambition pour l'ordre domestique.",
        "Apprendre à organiser et entretenir ton espace de vie. Ta tendance au désordre ou à la fuite te freine dans la création d'un vrai foyer.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer un espace propre, fonctionnel, qui soutient ta santé et ton travail.",
        "Organise ou nettoie un espace de ton foyer avec attention.",
        "Respire en visualisant un foyer ordonné et apaisant.",
        "Quel espace de mon foyer a besoin de plus d'ordre et de soin ? »"),

    ('virgo', 5): make_nn_interp('virgo', 5,
        "Ton chemin d'âme t'appelle à créer avec précision et à aimer avec discernement.",
        "Le Nœud Nord en Vierge dans ta maison V t'invite à développer une créativité artisanale et des amours saines. Tu quittes le besoin d'approbation pour la qualité du travail.",
        "Apprendre à créer avec soin et à aimer avec discernement. Ta tendance à chercher l'amour du groupe ou l'idéal te freine dans la création concrète.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'artisanat soigné, l'amour qui prend soin, le jeu éducatif.",
        "Crée quelque chose avec attention aux détails et à la qualité.",
        "Respire en appréciant la beauté de la précision et du soin.",
        "Comment puis-je améliorer la qualité de ma créativité ? »"),

    ('virgo', 6): make_nn_interp('virgo', 6,
        "Ton chemin d'âme t'appelle à maîtriser le travail quotidien et la santé.",
        "Le Nœud Nord en Vierge dans ta maison VI (son domicile naturel) t'invite à développer pleinement tes capacités de service et d'amélioration.",
        "Apprendre à travailler avec efficacité et à prendre soin de ta santé. Ta tendance à fuir la réalité ou à te sacrifier te freine dans ton efficacité.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends la maîtrise des routines, l'attention au corps, le service efficace.",
        "Établis une routine de santé simple et suis-la avec discipline.",
        "Respire en visualisant un corps qui fonctionne parfaitement.",
        "Quelle amélioration concrète puis-je apporter à ma santé ou mon travail ? »"),

    ('virgo', 7): make_nn_interp('virgo', 7,
        "Ton chemin d'âme t'appelle à créer des partenariats pratiques et utiles.",
        "Le Nœud Nord en Vierge dans ta maison VII t'invite à développer des relations qui fonctionnent concrètement. Tu quittes l'idéal romantique pour le couple qui s'entraide.",
        "Apprendre à aider concrètement dans tes relations. Ta tendance aux rêves romantiques ou à l'affirmation solitaire te freine dans la création de partenariats fonctionnels.",
        "Tes relations sont le terrain de ton évolution. Tu apprends l'aide pratique entre partenaires, le service mutuel, l'amélioration ensemble.",
        "Offre une aide concrète et pratique à un partenaire.",
        "Respire en visualisant des relations où chacun améliore l'autre.",
        "Comment puis-je être plus utile dans mes relations ? »"),

    ('virgo', 8): make_nn_interp('virgo', 8,
        "Ton chemin d'âme t'appelle à analyser et comprendre les transformations.",
        "Le Nœud Nord en Vierge dans ta maison VIII t'invite à développer une approche pratique des crises. Tu quittes l'attachement aux possessions pour la gestion efficace du changement.",
        "Apprendre à gérer les crises avec discernement. Ta tendance à t'accrocher au confort te freine dans la navigation des transformations.",
        "Les transformations sont le terrain de ton évolution. Tu apprends à analyser les crises, à gérer les ressources partagées avec précision, à comprendre la psyché.",
        "Face à une difficulté, fais une liste pratique de solutions.",
        "Respire en accueillant la clarté mentale même dans les moments intenses.",
        "Comment puis-je mieux analyser et gérer les transformations de ma vie ? »"),

    ('virgo', 9): make_nn_interp('virgo', 9,
        "Ton chemin d'âme t'appelle à développer une sagesse pratique et applicable.",
        "Le Nœud Nord en Vierge dans ta maison IX t'invite à développer une philosophie utile. Tu quittes l'accumulation d'informations pour la sagesse applicable.",
        "Apprendre à vivre ta spiritualité de façon concrète. Ta tendance à collecter des savoirs sans les appliquer te freine dans ta croissance.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends la sagesse incarnée, le voyage pratique, l'enseignement qui se vérifie.",
        "Applique concrètement un enseignement spirituel dans ta journée.",
        "Respire en ancrant une vérité dans ton corps et ta vie quotidienne.",
        "Quelle sagesse dois-je incarner plus concrètement ? »"),

    ('virgo', 10): make_nn_interp('virgo', 10,
        "Ton chemin d'âme t'appelle à construire une carrière de compétence et de service.",
        "Le Nœud Nord en Vierge dans ta maison X t'invite à développer une réputation d'expert. Tu quittes la dépendance émotionnelle pour l'autorité professionnelle.",
        "Apprendre à être reconnu pour tes compétences. Ta tendance à rester dans l'ombre ou à dépendre des autres te freine dans ta carrière.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à devenir expert dans ton domaine, à être utile au monde, à être reconnu pour ton travail.",
        "Améliore une compétence professionnelle de façon visible.",
        "Respire en visualisant une carrière basée sur ton excellence.",
        "Quelle compétence professionnelle dois-je développer ou montrer ? »"),

    ('virgo', 11): make_nn_interp('virgo', 11,
        "Ton chemin d'âme t'appelle à servir les groupes par tes compétences.",
        "Le Nœud Nord en Vierge dans ta maison XI t'invite à apporter tes talents pratiques aux projets collectifs. Tu quittes le besoin d'être spécial pour être utile.",
        "Apprendre à contribuer concrètement aux groupes. Ta tendance à chercher l'attention personnelle ou la romance te freine dans le service au collectif.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à être utile à la communauté, à organiser les groupes, à servir les causes avec efficacité.",
        "Offre une compétence pratique à un groupe ou une cause.",
        "Respire en visualisant tes talents au service du bien commun.",
        "Comment puis-je être plus utile à mes communautés ? »"),

    ('virgo', 12): make_nn_interp('virgo', 12,
        "Ton chemin d'âme t'appelle à organiser ton monde intérieur.",
        "Le Nœud Nord en Vierge dans ta maison XII t'invite à apporter de l'ordre dans ton inconscient. Tu quittes l'anxiété du contrôle pour la clarté intérieure.",
        "Apprendre à observer et organiser tes patterns inconscients. Ta tendance à l'anxiété du détail ou au perfectionnisme te freine dans la paix intérieure.",
        "L'inconscient est le terrain de ton évolution. Tu apprends à méditer avec méthode, à analyser tes rêves, à nettoyer tes schémas cachés.",
        "Observe tes pensées pendant 5 minutes avec clarté et détachement.",
        "Respire en laissant le mental devenir clair et ordonné naturellement.",
        "Quel schéma inconscient ai-je besoin d'observer et de comprendre ? »"),

    # === LIBRA (M1-M12) ===
    ('libra', 1): make_nn_interp('libra', 1,
        "Ton chemin d'âme t'appelle à développer l'harmonie et la diplomatie.",
        "Le Nœud Nord en Balance dans ta maison I t'invite à développer ta grâce et ta capacité relationnelle. Tu quittes l'affirmation combative du Bélier pour l'équilibre de la Balance.",
        "Apprendre à être diplomate et à considérer les autres. Ta tendance à foncer tête baissée ou à te battre seul te freine dans tes relations.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être gracieux, équilibré, à tenir compte des autres dans qui tu es.",
        "Avant d'agir, demande-toi comment cela affecte les autres.",
        "Respire en visualisant un équilibre parfait entre toi et le monde.",
        "Comment puis-je être plus conscient de l'impact de mes actions sur les autres ? »"),

    ('libra', 2): make_nn_interp('libra', 2,
        "Ton chemin d'âme t'appelle à créer la valeur par la coopération.",
        "Le Nœud Nord en Balance dans ta maison II t'invite à développer la richesse par le partenariat. Tu quittes l'attachement aux ressources des autres pour créer ensemble.",
        "Apprendre à valoriser tes talents de médiateur et créer par la coopération. Ta tendance aux drames financiers ou à la dépendance te freine.",
        "Tes finances sont le terrain de ton évolution. Tu apprends que la valeur vient aussi de l'équité, de la beauté, de la collaboration.",
        "Identifie comment un partenariat pourrait enrichir tes projets.",
        "Respire en visualisant une prospérité basée sur l'équilibre et le partage.",
        "Comment la coopération peut-elle enrichir ma vie matérielle ? »"),

    ('libra', 3): make_nn_interp('libra', 3,
        "Ton chemin d'âme t'appelle à communiquer avec diplomatie et équilibre.",
        "Le Nœud Nord en Balance dans ta maison III t'invite à développer l'art du dialogue. Tu quittes les certitudes pour l'écoute des différentes perspectives.",
        "Apprendre à écouter autant qu'à parler. Ta tendance à prêcher ou à imposer ta vérité te freine dans la vraie communication.",
        "Ta communication est le terrain de ton évolution. Tu apprends le dialogue équilibré, l'écriture élégante, la médiation entre les points de vue.",
        "Dans ta prochaine conversation, cherche sincèrement à comprendre l'autre point de vue.",
        "Respire en laissant tes mots devenir des ponts plutôt que des flèches.",
        "Comment puis-je mieux écouter et intégrer les perspectives des autres ? »"),

    ('libra', 4): make_nn_interp('libra', 4,
        "Ton chemin d'âme t'appelle à créer un foyer harmonieux et beau.",
        "Le Nœud Nord en Balance dans ta maison IV t'invite à développer l'harmonie familiale. Tu quittes l'ambition solitaire pour la paix du foyer partagé.",
        "Apprendre à créer l'équilibre dans ta vie familiale. Ta tendance à privilégier la carrière ou le statut te freine dans la création d'un vrai foyer.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer un espace beau et harmonieux, à équilibrer les relations familiales, à faire des compromis.",
        "Embellis un espace de ton foyer ou résous un conflit familial.",
        "Respire en visualisant un foyer baigné de paix et de beauté.",
        "Quel équilibre dois-je trouver dans ma vie familiale ? »"),

    ('libra', 5): make_nn_interp('libra', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec élégance et équilibre.",
        "Le Nœud Nord en Balance dans ta maison V t'invite à développer une créativité harmonieuse et des amours équilibrées. Tu quittes le besoin du groupe pour le partenariat intime.",
        "Apprendre à créer avec beauté et à aimer en considérant l'autre. Ta tendance à te fondre dans le collectif te freine dans l'intimité créative.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'art de la création élégante, de l'amour courtois, du jeu partagé.",
        "Crée quelque chose de beau avec ou pour quelqu'un.",
        "Respire en laissant la beauté de l'harmonie inspirer ta créativité.",
        "Comment puis-je créer plus de beauté et d'harmonie dans mes amours et ma créativité ? »"),

    ('libra', 6): make_nn_interp('libra', 6,
        "Ton chemin d'âme t'appelle à travailler en harmonie avec les autres.",
        "Le Nœud Nord en Balance dans ta maison VI t'invite à développer la coopération au travail. Tu quittes la confusion ou le sacrifice pour le partenariat quotidien.",
        "Apprendre à collaborer efficacement au quotidien. Ta tendance à te sacrifier seul ou à fuir te freine dans la création de bonnes relations de travail.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends le travail d'équipe, l'équilibre entre donner et recevoir, la beauté dans le quotidien.",
        "Cherche à établir plus d'harmonie avec un collègue aujourd'hui.",
        "Respire en visualisant un équilibre parfait entre travail et bien-être.",
        "Comment puis-je créer plus d'harmonie dans mon environnement de travail ? »"),

    ('libra', 7): make_nn_interp('libra', 7,
        "Ton chemin d'âme t'appelle à maîtriser l'art du partenariat.",
        "Le Nœud Nord en Balance dans ta maison VII (son domicile naturel) t'invite à développer pleinement tes capacités relationnelles.",
        "Apprendre à être un partenaire équilibré plutôt qu'un guerrier solitaire. Ta tendance à l'indépendance ou à l'affirmation agressive te freine dans le couple.",
        "Tes relations sont le terrain de ton évolution. Tu apprends l'art du compromis, de la diplomatie amoureuse, de la création d'un « nous » harmonieux.",
        "Fais un compromis conscient et généreux avec un partenaire.",
        "Respire en visualisant des relations parfaitement équilibrées.",
        "Quel compromis suis-je appelé(e) à faire pour créer plus d'harmonie ? »"),

    ('libra', 8): make_nn_interp('libra', 8,
        "Ton chemin d'âme t'appelle à traverser les transformations avec équilibre.",
        "Le Nœud Nord en Balance dans ta maison VIII t'invite à apporter de l'harmonie dans les crises. Tu quittes l'attachement aux possessions pour le partage équitable.",
        "Apprendre à partager les ressources avec équité et à naviguer les transformations avec grâce. Ta tendance à t'accrocher au confort te freine.",
        "Les transformations sont le terrain de ton évolution. Tu apprends à partager les ressources, à traverser les crises en partenariat, à trouver l'équilibre dans l'intime.",
        "Identifie un partage que tu peux rendre plus équitable.",
        "Respire en accueillant les transformations avec grâce et équilibre.",
        "Quel partage de ressources ai-je besoin de rééquilibrer ? »"),

    ('libra', 9): make_nn_interp('libra', 9,
        "Ton chemin d'âme t'appelle à développer une philosophie d'équité et de paix.",
        "Le Nœud Nord en Balance dans ta maison IX t'invite à développer une sagesse relationnelle. Tu quittes l'accumulation d'informations pour la quête de justice.",
        "Apprendre à voir tous les côtés d'une question philosophique. Ta tendance à te disperser dans les détails te freine dans la vision d'ensemble équilibrée.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends la philosophie de la paix, le voyage avec des partenaires, l'enseignement de l'harmonie.",
        "Explore une question de plusieurs points de vue avant de conclure.",
        "Respire en visualisant une sagesse qui unit plutôt qu'elle ne divise.",
        "Quelle vérité gagne à être vue sous plusieurs angles ? »"),

    ('libra', 10): make_nn_interp('libra', 10,
        "Ton chemin d'âme t'appelle à bâtir une carrière de médiateur ou d'artiste.",
        "Le Nœud Nord en Balance dans ta maison X t'invite à développer une réputation de diplomate. Tu quittes la dépendance émotionnelle pour l'autorité harmonieuse.",
        "Apprendre à être reconnu pour tes capacités de médiation ou ton sens de la beauté. Ta tendance à rester dans l'ombre ou à dépendre des autres te freine.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à diriger avec diplomatie, à créer une réputation de justice, à apporter la beauté au monde.",
        "Cherche une opportunité de médiation ou de création de beauté dans ta carrière.",
        "Respire en visualisant une carrière basée sur l'harmonie et la justice.",
        "Comment puis-je apporter plus de diplomatie et de beauté dans ma carrière ? »"),

    ('libra', 11): make_nn_interp('libra', 11,
        "Ton chemin d'âme t'appelle à créer des communautés harmonieuses.",
        "Le Nœud Nord en Balance dans ta maison XI t'invite à développer des amitiés équilibrées. Tu quittes le besoin d'être spécial pour créer l'harmonie collective.",
        "Apprendre à médier dans les groupes et à créer l'unité. Ta tendance à chercher l'attention personnelle te freine dans la contribution au collectif.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à être un médiateur social, à créer des liens entre les gens, à servir l'harmonie collective.",
        "Aide à résoudre un conflit ou à créer l'harmonie dans un groupe.",
        "Respire en visualisant une communauté unie et harmonieuse.",
        "Comment puis-je contribuer à plus d'harmonie dans mes groupes ? »"),

    ('libra', 12): make_nn_interp('libra', 12,
        "Ton chemin d'âme t'appelle à trouver la paix intérieure.",
        "Le Nœud Nord en Balance dans ta maison XII t'invite à développer l'harmonie dans ton monde intérieur. Tu quittes l'anxiété du quotidien pour la paix de l'âme.",
        "Apprendre à équilibrer tes mondes intérieur et extérieur. Ta tendance à t'inquiéter des détails ou à servir excessivement te freine dans ta paix.",
        "L'inconscient est le terrain de ton évolution. Tu apprends la méditation de la paix, l'équilibre entre conscient et inconscient, la beauté spirituelle.",
        "Médite en cherchant l'équilibre et l'harmonie intérieure.",
        "Respire en visualisant la paix qui règne dans ton monde intérieur.",
        "Quel équilibre intérieur dois-je trouver ? »"),

    # === SCORPIO (M1-M12) ===
    ('scorpio', 1): make_nn_interp('scorpio', 1,
        "Ton chemin d'âme t'appelle à développer l'intensité et le pouvoir de transformation.",
        "Le Nœud Nord en Scorpion dans ta maison I t'invite à développer ta profondeur et ton magnétisme. Tu quittes le confort du Taureau pour l'intensité du Scorpion.",
        "Apprendre à embrasser les transformations et à développer ton pouvoir personnel. Ta tendance à t'accrocher à la sécurité te freine dans ta métamorphose.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être intense, magnétique, capable de mourir et renaître.",
        "Laisse mourir une habitude ou une façade qui ne te sert plus.",
        "Respire en visualisant ta propre capacité à te transformer complètement.",
        "Quelle transformation suis-je appelé(e) à incarner ? »"),

    ('scorpio', 2): make_nn_interp('scorpio', 2,
        "Ton chemin d'âme t'appelle à partager les ressources et à gérer le pouvoir financier.",
        "Le Nœud Nord en Scorpion dans ta maison II t'invite à développer une relation profonde avec les ressources. Tu quittes l'attachement superficiel pour la richesse transformatrice.",
        "Apprendre à partager, à gérer les ressources partagées et à transformer ton rapport à l'argent. Ta tendance à accumuler pour la sécurité te freine.",
        "Tes finances sont le terrain de ton évolution. Tu apprends que la vraie richesse vient de la transformation, du partage, de la mort de l'attachement.",
        "Partage quelque chose de précieux ou transforme ton rapport à une possession.",
        "Respire en visualisant l'abondance qui vient du lâcher-prise.",
        "Quel attachement financier suis-je prêt(e) à transformer ? »"),

    ('scorpio', 3): make_nn_interp('scorpio', 3,
        "Ton chemin d'âme t'appelle à communiquer avec profondeur et authenticité.",
        "Le Nœud Nord en Scorpion dans ta maison III t'invite à développer une parole qui va au fond des choses. Tu quittes la légèreté pour la vérité profonde.",
        "Apprendre à dire les choses difficiles et à explorer les tabous. Ta tendance à rester en surface ou à éviter les sujets sensibles te freine.",
        "Ta communication est le terrain de ton évolution. Tu apprends à parler des vérités profondes, à écrire sur les mystères, à avoir des conversations transformatrices.",
        "Engage une conversation sur un sujet que tu évites habituellement.",
        "Respire en laissant tes mots descendre dans les profondeurs.",
        "Quelle vérité profonde ai-je besoin d'exprimer ? »"),

    ('scorpio', 4): make_nn_interp('scorpio', 4,
        "Ton chemin d'âme t'appelle à transformer tes racines et ton histoire familiale.",
        "Le Nœud Nord en Scorpion dans ta maison IV t'invite à plonger dans les profondeurs de ton histoire. Tu quittes l'ambition extérieure pour la transformation intérieure.",
        "Apprendre à guérir les blessures familiales et à transformer tes racines. Ta tendance à chercher le succès extérieur te freine dans ton travail intérieur.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à transformer les schémas familiaux, à guérir les mémoires ancestrales, à créer un foyer de renaissance.",
        "Explore un secret ou une blessure familiale avec courage.",
        "Respire en visualisant tes racines qui se transforment et guérissent.",
        "Quel pattern familial suis-je appelé(e) à transformer ? »"),

    ('scorpio', 5): make_nn_interp('scorpio', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec passion transformatrice.",
        "Le Nœud Nord en Scorpion dans ta maison V t'invite à développer une créativité cathartique et des amours profondes. Tu quittes l'attachement à l'appréciation pour la création viscérale.",
        "Apprendre à créer depuis tes profondeurs et à aimer avec intensité. Ta tendance au confort ou à la superficialité te freine dans l'expression authentique.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'art de la création transformatrice, de l'amour qui change tout, du jeu qui révèle.",
        "Crée quelque chose qui exprime une vérité profonde ou taboue.",
        "Respire en laissant ta créativité naître de tes profondeurs les plus sombres.",
        "Quelle création transformatrice demande à naître de moi ? »"),

    ('scorpio', 6): make_nn_interp('scorpio', 6,
        "Ton chemin d'âme t'appelle à transformer ton rapport au travail et à la santé.",
        "Le Nœud Nord en Scorpion dans ta maison VI t'invite à développer une approche profonde du quotidien. Tu quittes la confusion pour la purification.",
        "Apprendre à transformer tes habitudes et à guérir tes patterns de santé. Ta tendance à fuir ou à te sacrifier te freine dans la régénération.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends les purifications profondes, le travail transformateur, la guérison des causes cachées.",
        "Identifie une habitude malsaine et décide de la transformer radicalement.",
        "Respire en visualisant ton corps qui se purifie et se régénère.",
        "Quelle habitude suis-je prêt(e) à laisser mourir pour ma santé ? »"),

    ('scorpio', 7): make_nn_interp('scorpio', 7,
        "Ton chemin d'âme t'appelle à créer des partenariats de transformation mutuelle.",
        "Le Nœud Nord en Scorpion dans ta maison VII t'invite à développer des relations profondes et transformatrices. Tu quittes l'indépendance pour la fusion consciente.",
        "Apprendre à t'engager profondément et à te transformer à travers l'autre. Ta tendance à rester autonome ou à fuir l'intimité te freine.",
        "Tes relations sont le terrain de ton évolution. Tu apprends l'intimité profonde, la transformation à deux, le partenariat qui fait mourir et renaître.",
        "Partage une vérité profonde avec un partenaire, même si c'est difficile.",
        "Respire en visualisant des relations qui vous transforment mutuellement.",
        "Quelle profondeur suis-je prêt(e) à explorer avec un partenaire ? »"),

    ('scorpio', 8): make_nn_interp('scorpio', 8,
        "Ton chemin d'âme t'appelle à maîtriser les mystères de la mort et de la renaissance.",
        "Le Nœud Nord en Scorpion dans ta maison VIII (son domicile naturel) t'invite à développer pleinement ton pouvoir de transformation.",
        "Apprendre à embrasser les transformations profondes et à partager les ressources. Ta tendance à t'accrocher aux possessions te freine dans la renaissance.",
        "Les transformations sont le terrain de ton évolution. Tu apprends à mourir et renaître, à partager l'intime, à accompagner les autres dans leurs métamorphoses.",
        "Médite sur ce que tu dois laisser mourir pour renaître plus puissant.",
        "Respire en accueillant la mort comme ta plus grande alliée.",
        "Quelle transformation majeure suis-je appelé(e) à traverser ? »"),

    ('scorpio', 9): make_nn_interp('scorpio', 9,
        "Ton chemin d'âme t'appelle à développer une spiritualité de transformation.",
        "Le Nœud Nord en Scorpion dans ta maison IX t'invite à développer une quête de vérité profonde. Tu quittes l'information superficielle pour la sagesse transformatrice.",
        "Apprendre à chercher les vérités qui transforment plutôt que celles qui confortent. Ta tendance à rester en surface ou à fuir la profondeur te freine.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends les mystères initiatiques, les voyages de transformation, l'enseignement qui change tout.",
        "Étudie un texte ou une tradition qui parle de mort et renaissance.",
        "Respire en accueillant les vérités qui transforment tout.",
        "Quelle vérité transformatrice ai-je peur de découvrir ? »"),

    ('scorpio', 10): make_nn_interp('scorpio', 10,
        "Ton chemin d'âme t'appelle à exercer un pouvoir de transformation dans ta carrière.",
        "Le Nœud Nord en Scorpion dans ta maison X t'invite à développer une carrière de pouvoir et de transformation. Tu quittes la dépendance émotionnelle pour l'autorité transformatrice.",
        "Apprendre à exercer une influence profonde dans le monde. Ta tendance à rester dans le confort du foyer te freine dans ton ascension.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à transformer les structures, à exercer un pouvoir éthique, à avoir un impact profond.",
        "Identifie comment ta carrière peut transformer quelque chose dans le monde.",
        "Respire en visualisant le pouvoir de transformation que tu peux exercer.",
        "Quel pouvoir de transformation ma carrière peut-elle exercer ? »"),

    ('scorpio', 11): make_nn_interp('scorpio', 11,
        "Ton chemin d'âme t'appelle à transformer les groupes et les causes.",
        "Le Nœud Nord en Scorpion dans ta maison XI t'invite à développer un engagement profond pour des causes transformatrices. Tu quittes la créativité personnelle pour l'impact collectif.",
        "Apprendre à canaliser ton intensité au service du collectif. Ta tendance à te centrer sur toi te freine dans la transformation sociale.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à créer des mouvements de transformation, à avoir des amitiés profondes, à servir des causes qui comptent.",
        "Engage-toi dans une cause qui vise une transformation profonde.",
        "Respire en visualisant ton pouvoir au service du changement collectif.",
        "Quelle transformation collective suis-je appelé(e) à soutenir ? »"),

    ('scorpio', 12): make_nn_interp('scorpio', 12,
        "Ton chemin d'âme t'appelle à plonger dans les profondeurs de l'inconscient.",
        "Le Nœud Nord en Scorpion dans ta maison XII t'invite à développer une connexion profonde avec l'invisible. Tu quittes l'anxiété du contrôle pour l'abandon transformateur.",
        "Apprendre à naviguer les profondeurs de la psyché et à guérir l'ombre. Ta tendance à rester dans le rationnel ou le quotidien te freine.",
        "L'inconscient est le terrain de ton évolution. Tu apprends à méditer dans les profondeurs, à transformer tes démons, à guérir le karma.",
        "Médite en plongeant consciemment dans les profondeurs de ton être.",
        "Respire en accueillant les ténèbres comme un territoire de transformation.",
        "Quelle ombre inconsciente suis-je appelé(e) à transformer ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in NORTH_NODE_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'north_node',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP north_node/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='north_node',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT north_node/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
