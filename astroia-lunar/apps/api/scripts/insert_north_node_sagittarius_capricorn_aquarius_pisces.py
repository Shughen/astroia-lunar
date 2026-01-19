#!/usr/bin/env python3
"""Insert North Node interpretations for Sagittarius, Capricorn, Aquarius, Pisces (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_nn_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'sagittarius': '☊ Nœud Nord en Sagittaire',
        'capricorn': '☊ Nœud Nord en Capricorne',
        'aquarius': '☊ Nœud Nord en Verseau',
        'pisces': '☊ Nœud Nord en Poissons',
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

NORTH_NODE_INTERPRETATIONS = {
    # === SAGITTARIUS (M1-M12) ===
    ('sagittarius', 1): make_nn_interp('sagittarius', 1,
        "Ton chemin d'âme t'appelle à développer la foi, l'aventure et l'optimisme.",
        "Le Nœud Nord en Sagittaire dans ta maison I t'invite à développer ta vision et ton enthousiasme. Tu quittes la dispersion des Gémeaux pour la quête de sens du Sagittaire.",
        "Apprendre à avoir foi en toi-même et à voir le tableau d'ensemble. Ta tendance à trop réfléchir ou à te disperser te freine dans ton affirmation.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être optimiste, aventurier, inspirant dans ta façon d'être au monde.",
        "Affirme une croyance positive sur toi-même à voix haute.",
        "Respire en visualisant un horizon infini qui s'ouvre devant toi.",
        "Quelle vision plus grande de moi-même suis-je appelé(e) à incarner ? »"),

    ('sagittarius', 2): make_nn_interp('sagittarius', 2,
        "Ton chemin d'âme t'appelle à créer la richesse par ta vision et ta foi.",
        "Le Nœud Nord en Sagittaire dans ta maison II t'invite à développer une prospérité basée sur tes croyances. Tu quittes la dépendance aux détails pour la richesse expansive.",
        "Apprendre à faire confiance à l'abondance universelle. Ta tendance à compter chaque sou ou à douter te freine dans ta prospérité.",
        "Tes finances sont le terrain de ton évolution. Tu apprends que la foi attire l'abondance, que la vision crée la richesse.",
        "Fais un investissement basé sur ta foi en l'avenir, même petit.",
        "Respire en visualisant l'abondance qui coule vers toi sans limite.",
        "Quelle croyance limitante sur l'argent dois-je abandonner ? »"),

    ('sagittarius', 3): make_nn_interp('sagittarius', 3,
        "Ton chemin d'âme t'appelle à communiquer avec inspiration et vision.",
        "Le Nœud Nord en Sagittaire dans ta maison III t'invite à développer une parole inspirante. Tu quittes les détails pour le message d'ensemble.",
        "Apprendre à inspirer par ta communication plutôt qu'à juste informer. Ta tendance à te perdre dans les détails te freine.",
        "Ta communication est le terrain de ton évolution. Tu apprends à parler avec vision, à écrire pour inspirer, à voir le sens derrière les faits.",
        "Partage une idée inspirante avec quelqu'un, pas juste une information.",
        "Respire en laissant tes mots porter une vision plus grande.",
        "Quel message inspirant ai-je à communiquer ? »"),

    ('sagittarius', 4): make_nn_interp('sagittarius', 4,
        "Ton chemin d'âme t'appelle à créer un foyer de croissance et d'expansion.",
        "Le Nœud Nord en Sagittaire dans ta maison IV t'invite à développer une vie familiale ouverte et en expansion. Tu quittes l'ambition publique pour la sagesse du foyer.",
        "Apprendre à trouver le sens dans ta vie familiale. Ta tendance à privilégier le statut te freine dans la création d'un vrai foyer philosophique.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer un espace d'ouverture, de sagesse, d'exploration intérieure.",
        "Apporte quelque chose d'inspirant ou d'étranger dans ton foyer.",
        "Respire en visualisant ton foyer comme un temple de sagesse.",
        "Comment puis-je apporter plus de sens et d'expansion dans ma vie de famille ? »"),

    ('sagittarius', 5): make_nn_interp('sagittarius', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec foi et enthousiasme.",
        "Le Nœud Nord en Sagittaire dans ta maison V t'invite à développer une créativité visionnaire et des amours aventureuses. Tu quittes la sécurité du groupe pour la joie de l'exploration.",
        "Apprendre à créer avec foi et à aimer avec aventure. Ta tendance à te fondre dans le collectif te freine dans ton expression joyeuse.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends la création audacieuse, l'amour aventureux, le jeu expansif.",
        "Crée quelque chose d'audacieux basé sur une vision, pas sur des règles.",
        "Respire en laissant la joie de la découverte inspirer ta créativité.",
        "Quelle aventure créative ou amoureuse m'appelle ? »"),

    ('sagittarius', 6): make_nn_interp('sagittarius', 6,
        "Ton chemin d'âme t'appelle à trouver le sens dans ton travail quotidien.",
        "Le Nœud Nord en Sagittaire dans ta maison VI t'invite à développer une approche philosophique du quotidien. Tu quittes la confusion pour la quête de sens au travail.",
        "Apprendre à voir le sens plus large de tes tâches quotidiennes. Ta tendance à fuir ou à te sacrifier te freine dans le travail inspiré.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends que chaque tâche peut avoir un sens, que la santé est un voyage.",
        "Trouve le sens plus profond d'une tâche quotidienne que tu fais mécaniquement.",
        "Respire en visualisant chaque action comme partie d'un voyage plus grand.",
        "Quel sens plus grand puis-je trouver dans mon travail quotidien ? »"),

    ('sagittarius', 7): make_nn_interp('sagittarius', 7,
        "Ton chemin d'âme t'appelle à créer des partenariats basés sur la vision partagée.",
        "Le Nœud Nord en Sagittaire dans ta maison VII t'invite à développer des relations qui élargissent tes horizons. Tu quittes l'affirmation solitaire pour l'exploration à deux.",
        "Apprendre à créer des partenariats qui grandissent ensemble. Ta tendance à agir seul ou à te battre te freine dans la création de couples inspirants.",
        "Tes relations sont le terrain de ton évolution. Tu apprends le voyage à deux, le partenariat philosophique, la croissance mutuelle.",
        "Partage une vision d'avenir avec un partenaire.",
        "Respire en visualisant des relations qui vous élèvent mutuellement vers de nouveaux horizons.",
        "Quelle vision partagée puis-je créer avec mes partenaires ? »"),

    ('sagittarius', 8): make_nn_interp('sagittarius', 8,
        "Ton chemin d'âme t'appelle à trouver le sens des transformations profondes.",
        "Le Nœud Nord en Sagittaire dans ta maison VIII t'invite à développer une approche philosophique des crises. Tu quittes l'attachement aux possessions pour la sagesse du passage.",
        "Apprendre à voir les transformations comme des initiations. Ta tendance à t'accrocher à la sécurité te freine dans la croissance spirituelle par les crises.",
        "Les transformations sont le terrain de ton évolution. Tu apprends que chaque mort est une initiation, que le partage est une expansion.",
        "Vois une épreuve passée comme une initiation qui t'a fait grandir.",
        "Respire en accueillant les transformations comme des voyages initiatiques.",
        "Quel enseignement mes épreuves m'ont-elles apporté ? »"),

    ('sagittarius', 9): make_nn_interp('sagittarius', 9,
        "Ton chemin d'âme t'appelle à maîtriser la quête de sagesse et de vérité.",
        "Le Nœud Nord en Sagittaire dans ta maison IX (son domicile naturel) t'invite à développer pleinement ta spiritualité et ta philosophie.",
        "Apprendre à chercher la vérité avec passion et à partager ta sagesse. Ta tendance à rester dans les détails ou à douter te freine.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends à voyager pour grandir, à étudier pour comprendre, à enseigner pour partager.",
        "Engage-toi dans une quête de sagesse — lecture, voyage, enseignement.",
        "Respire en visualisant ta conscience qui s'élargit vers l'infini.",
        "Quelle vérité suis-je appelé(e) à découvrir et enseigner ? »"),

    ('sagittarius', 10): make_nn_interp('sagittarius', 10,
        "Ton chemin d'âme t'appelle à bâtir une carrière d'inspiration et d'enseignement.",
        "Le Nœud Nord en Sagittaire dans ta maison X t'invite à développer une réputation de visionnaire. Tu quittes la dépendance émotionnelle pour l'autorité inspirante.",
        "Apprendre à être reconnu pour ta vision et ta sagesse. Ta tendance à rester dans le confort du foyer te freine dans ton rayonnement.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à inspirer par ton travail, à enseigner par l'exemple, à voyager pour ta carrière.",
        "Partage une vision inspirante dans ton domaine professionnel.",
        "Respire en visualisant une carrière qui inspire et élève les autres.",
        "Quelle vision puis-je apporter au monde par ma carrière ? »"),

    ('sagittarius', 11): make_nn_interp('sagittarius', 11,
        "Ton chemin d'âme t'appelle à inspirer les groupes par ta vision.",
        "Le Nœud Nord en Sagittaire dans ta maison XI t'invite à développer une influence inspirante sur le collectif. Tu quittes le besoin d'être spécial pour être inspirant.",
        "Apprendre à partager ta vision avec les groupes. Ta tendance à te centrer sur toi ou à chercher l'attention te freine dans l'inspiration collective.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à inspirer les mouvements, à avoir des amitiés philosophiques, à servir des causes universelles.",
        "Partage une vision inspirante avec un groupe ou une communauté.",
        "Respire en visualisant ta vision qui inspire un cercle de personnes.",
        "Quelle vision puis-je partager pour inspirer ma communauté ? »"),

    ('sagittarius', 12): make_nn_interp('sagittarius', 12,
        "Ton chemin d'âme t'appelle à développer une foi spirituelle profonde.",
        "Le Nœud Nord en Sagittaire dans ta maison XII t'invite à développer une connexion spirituelle basée sur la foi. Tu quittes l'anxiété des détails pour la confiance universelle.",
        "Apprendre à faire confiance à l'univers et à développer ta foi. Ta tendance à l'inquiétude ou au perfectionnisme te freine dans ta paix spirituelle.",
        "L'inconscient est le terrain de ton évolution. Tu apprends la méditation expansive, la foi sans preuve, la sagesse de l'invisible.",
        "Médite en te connectant à quelque chose de plus grand que toi.",
        "Respire en laissant la foi remplacer l'inquiétude.",
        "Quelle foi suis-je appelé(e) à développer ? »"),

    # === CAPRICORN (M1-M12) ===
    ('capricorn', 1): make_nn_interp('capricorn', 1,
        "Ton chemin d'âme t'appelle à développer la discipline, l'ambition et la maturité.",
        "Le Nœud Nord en Capricorne dans ta maison I t'invite à développer ta structure et ton autorité. Tu quittes la dépendance émotionnelle du Cancer pour la maturité du Capricorne.",
        "Apprendre à prendre tes responsabilités et à bâtir ta vie avec discipline. Ta tendance à rester dans le confort émotionnel te freine dans ton développement.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être solide, fiable, capable de prendre les rênes de ta vie.",
        "Prends une responsabilité que tu évitais.",
        "Respire en visualisant une montagne solide au centre de ton être.",
        "Quelle responsabilité suis-je appelé(e) à assumer pleinement ? »"),

    ('capricorn', 2): make_nn_interp('capricorn', 2,
        "Ton chemin d'âme t'appelle à construire ta propre sécurité financière.",
        "Le Nœud Nord en Capricorne dans ta maison II t'invite à développer une prospérité basée sur le travail. Tu quittes la dépendance aux ressources partagées pour créer ta propre base.",
        "Apprendre à gagner par ton travail et ta discipline. Ta tendance à dépendre des autres ou des transformations te freine dans ta prospérité.",
        "Tes finances sont le terrain de ton évolution. Tu apprends que la vraie richesse vient du travail patient, de l'investissement à long terme.",
        "Fais un plan financier à long terme, même simple.",
        "Respire en visualisant des structures financières solides que TU bâtis.",
        "Quelle discipline financière dois-je développer ? »"),

    ('capricorn', 3): make_nn_interp('capricorn', 3,
        "Ton chemin d'âme t'appelle à communiquer avec structure et autorité.",
        "Le Nœud Nord en Capricorne dans ta maison III t'invite à développer une parole responsable et structurée. Tu quittes l'idéalisme pour la communication pratique.",
        "Apprendre à parler avec autorité et à organiser tes pensées. Ta tendance à rester dans le vague ou l'idéal te freine dans la communication efficace.",
        "Ta communication est le terrain de ton évolution. Tu apprends l'écriture structurée, la parole responsable, l'enseignement pratique.",
        "Communique quelque chose de façon structurée et responsable.",
        "Respire en organisant tes pensées comme des blocs solides.",
        "Comment puis-je communiquer avec plus de structure et d'autorité ? »"),

    ('capricorn', 4): make_nn_interp('capricorn', 4,
        "Ton chemin d'âme t'appelle à construire des fondations familiales solides.",
        "Le Nœud Nord en Capricorne dans ta maison IV t'invite à développer la structure dans ta vie privée. Tu quittes l'ambition publique pour la construction du foyer.",
        "Apprendre à prendre tes responsabilités familiales. Ta tendance à privilégier la carrière ou le statut te freine dans la création de vraies racines.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer une structure familiale solide, à être le pilier de ton foyer.",
        "Prends une responsabilité familiale que tu évitais.",
        "Respire en visualisant un foyer aussi solide qu'une forteresse.",
        "Quelle structure familiale dois-je construire ou renforcer ? »"),

    ('capricorn', 5): make_nn_interp('capricorn', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec engagement et sérieux.",
        "Le Nœud Nord en Capricorne dans ta maison V t'invite à développer une créativité disciplinée et des amours matures. Tu quittes la sécurité du groupe pour la responsabilité créative.",
        "Apprendre à t'engager dans ta créativité et tes amours. Ta tendance à rester dans le collectif ou à fuir l'engagement te freine.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'art de la création engagée, de l'amour responsable, du jeu structuré.",
        "Engage-toi dans un projet créatif à long terme.",
        "Respire en ressentant la joie d'un engagement créatif solide.",
        "Dans quelle création suis-je appelé(e) à m'engager sérieusement ? »"),

    ('capricorn', 6): make_nn_interp('capricorn', 6,
        "Ton chemin d'âme t'appelle à maîtriser le travail et les routines.",
        "Le Nœud Nord en Capricorne dans ta maison VI t'invite à développer l'excellence professionnelle et la discipline de santé. Tu quittes la confusion pour la structure.",
        "Apprendre à travailler avec méthode et à prendre soin de toi avec discipline. Ta tendance à fuir ou à te sacrifier te freine dans l'efficacité.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends la maîtrise des routines, la discipline de la santé, le travail efficace.",
        "Établis une routine disciplinée et suis-la avec constance.",
        "Respire en visualisant un corps et un travail parfaitement structurés.",
        "Quelle discipline de travail ou de santé dois-je développer ? »"),

    ('capricorn', 7): make_nn_interp('capricorn', 7,
        "Ton chemin d'âme t'appelle à construire des partenariats solides et engagés.",
        "Le Nœud Nord en Capricorne dans ta maison VII t'invite à développer des relations responsables. Tu quittes la dépendance émotionnelle pour le partenariat mature.",
        "Apprendre à t'engager et à prendre tes responsabilités dans le couple. Ta tendance à rester dépendant ou protecteur te freine dans l'égalité relationnelle.",
        "Tes relations sont le terrain de ton évolution. Tu apprends le partenariat mature, l'engagement à long terme, la construction à deux.",
        "Prends une responsabilité claire dans un partenariat.",
        "Respire en visualisant des relations bâties sur des engagements solides.",
        "Quelle responsabilité dois-je prendre dans mes relations ? »"),

    ('capricorn', 8): make_nn_interp('capricorn', 8,
        "Ton chemin d'âme t'appelle à gérer les transformations avec maturité.",
        "Le Nœud Nord en Capricorne dans ta maison VIII t'invite à développer une gestion responsable des ressources partagées et des crises. Tu quittes l'attachement pour la gestion sage.",
        "Apprendre à naviguer les transformations avec discipline. Ta tendance à t'accrocher aux possessions te freine dans la gestion mature du changement.",
        "Les transformations sont le terrain de ton évolution. Tu apprends à gérer les crises avec maturité, à partager les ressources avec équité, à mourir avec dignité.",
        "Face à un changement, adopte une approche structurée et responsable.",
        "Respire en accueillant les transformations avec la sagesse de l'expérience.",
        "Comment puis-je mieux gérer les transformations de ma vie ? »"),

    ('capricorn', 9): make_nn_interp('capricorn', 9,
        "Ton chemin d'âme t'appelle à développer une philosophie pragmatique.",
        "Le Nœud Nord en Capricorne dans ta maison IX t'invite à développer une sagesse ancrée dans la réalité. Tu quittes l'accumulation d'informations pour la sagesse applicable.",
        "Apprendre à vivre ta philosophie concrètement. Ta tendance à te disperser dans les détails te freine dans la construction d'une vision de vie.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends la sagesse incarnée, le voyage avec but, l'enseignement basé sur l'expérience.",
        "Applique un principe de sagesse concrètement dans ta vie.",
        "Respire en ancrant ta philosophie dans des actions concrètes.",
        "Quelle sagesse dois-je incarner plus concrètement ? »"),

    ('capricorn', 10): make_nn_interp('capricorn', 10,
        "Ton chemin d'âme t'appelle à maîtriser ta carrière et ton autorité.",
        "Le Nœud Nord en Capricorne dans ta maison X (son domicile naturel) t'invite à développer pleinement ta capacité de leadership et de construction.",
        "Apprendre à prendre tes responsabilités publiques et à bâtir ta réputation. Ta tendance à rester dans le confort du foyer te freine dans ton ascension.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à construire pierre par pierre, à exercer l'autorité avec sagesse, à laisser un héritage.",
        "Prends une initiative de leadership dans ta carrière.",
        "Respire en visualisant le sommet de ta montagne professionnelle.",
        "Quelle autorité suis-je appelé(e) à exercer ? »"),

    ('capricorn', 11): make_nn_interp('capricorn', 11,
        "Ton chemin d'âme t'appelle à structurer les projets collectifs.",
        "Le Nœud Nord en Capricorne dans ta maison XI t'invite à apporter structure et discipline aux groupes. Tu quittes le besoin d'attention pour la contribution structurée.",
        "Apprendre à organiser et à structurer les projets collectifs. Ta tendance à chercher la lumière personnelle te freine dans le service au groupe.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à être un pilier pour les groupes, à organiser les causes, à structurer les rêves collectifs.",
        "Apporte structure et organisation à un projet de groupe.",
        "Respire en visualisant des projets collectifs solidement construits.",
        "Comment puis-je mieux structurer les projets collectifs auxquels je participe ? »"),

    ('capricorn', 12): make_nn_interp('capricorn', 12,
        "Ton chemin d'âme t'appelle à structurer ta vie spirituelle.",
        "Le Nœud Nord en Capricorne dans ta maison XII t'invite à développer une discipline spirituelle. Tu quittes l'anxiété du quotidien pour la construction intérieure.",
        "Apprendre à méditer avec discipline et à structurer ton monde intérieur. Ta tendance à l'inquiétude ou au perfectionnisme te freine dans la paix.",
        "L'inconscient est le terrain de ton évolution. Tu apprends la méditation structurée, la discipline spirituelle, la construction intérieure solide.",
        "Établis une pratique spirituelle régulière, même de 5 minutes.",
        "Respire en visualisant une structure intérieure solide et paisible.",
        "Quelle discipline spirituelle dois-je développer ? »"),

    # === AQUARIUS (M1-M12) ===
    ('aquarius', 1): make_nn_interp('aquarius', 1,
        "Ton chemin d'âme t'appelle à développer ton originalité et ton indépendance.",
        "Le Nœud Nord en Verseau dans ta maison I t'invite à développer ton unicité et ta vision futuriste. Tu quittes le besoin d'approbation du Lion pour l'originalité du Verseau.",
        "Apprendre à être différent et à penser par toi-même. Ta tendance à chercher l'attention ou la validation te freine dans ton authenticité.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être original, indépendant, visionnaire dans qui tu es.",
        "Fais quelque chose d'original, sans chercher l'approbation.",
        "Respire en célébrant ce qui te rend unique et différent.",
        "Quelle originalité ai-je peur de montrer au monde ? »"),

    ('aquarius', 2): make_nn_interp('aquarius', 2,
        "Ton chemin d'âme t'appelle à créer de la valeur par l'innovation.",
        "Le Nœud Nord en Verseau dans ta maison II t'invite à développer une prospérité basée sur l'originalité. Tu quittes les drames financiers pour l'innovation.",
        "Apprendre à valoriser tes idées originales. Ta tendance aux crises ou à la dépendance te freine dans ta prospérité innovante.",
        "Tes finances sont le terrain de ton évolution. Tu apprends que la vraie valeur vient de l'innovation, de l'originalité, de la pensée différente.",
        "Identifie comment une idée originale pourrait créer de la valeur.",
        "Respire en visualisant une prospérité basée sur ton unicité.",
        "Quelle innovation puis-je apporter qui créerait de la valeur ? »"),

    ('aquarius', 3): make_nn_interp('aquarius', 3,
        "Ton chemin d'âme t'appelle à communiquer avec originalité et innovation.",
        "Le Nœud Nord en Verseau dans ta maison III t'invite à développer une communication visionnaire. Tu quittes les certitudes pour la pensée innovante.",
        "Apprendre à communiquer tes idées originales. Ta tendance à prêcher ou à imposer te freine dans l'échange ouvert.",
        "Ta communication est le terrain de ton évolution. Tu apprends la pensée hors du cadre, l'écriture innovante, le dialogue qui réinvente.",
        "Partage une idée originale, même si elle semble bizarre.",
        "Respire en laissant des idées nouvelles traverser ton esprit.",
        "Quelle idée innovante ai-je peur de communiquer ? »"),

    ('aquarius', 4): make_nn_interp('aquarius', 4,
        "Ton chemin d'âme t'appelle à réinventer ta notion de famille et de foyer.",
        "Le Nœud Nord en Verseau dans ta maison IV t'invite à créer un foyer non-conventionnel. Tu quittes l'ambition traditionnelle pour l'innovation domestique.",
        "Apprendre à créer des liens familiaux basés sur le choix. Ta tendance au conformisme ou au statut te freine dans la création d'un vrai foyer.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer une famille choisie, un espace original, des traditions réinventées.",
        "Introduis quelque chose de non-conventionnel dans ta vie de famille.",
        "Respire en visualisant un foyer qui reflète ton unicité.",
        "Quelle tradition familiale ai-je besoin de réinventer ? »"),

    ('aquarius', 5): make_nn_interp('aquarius', 5,
        "Ton chemin d'âme t'appelle à créer et aimer de façon originale.",
        "Le Nœud Nord en Verseau dans ta maison V t'invite à développer une créativité innovante et des amours libres. Tu quittes le besoin d'approbation pour l'expression authentique.",
        "Apprendre à créer sans chercher la validation et à aimer sans posséder. Ta tendance à chercher l'attention te freine dans l'expression originale.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends la création expérimentale, l'amour basé sur la liberté, le jeu innovant.",
        "Crée quelque chose d'expérimental et original.",
        "Respire en libérant ta créativité de toute attente de validation.",
        "Quelle création originale ai-je peur d'exprimer ? »"),

    ('aquarius', 6): make_nn_interp('aquarius', 6,
        "Ton chemin d'âme t'appelle à innover dans ton travail quotidien.",
        "Le Nœud Nord en Verseau dans ta maison VI t'invite à apporter de l'innovation dans le quotidien. Tu quittes le sacrifice pour l'efficacité créative.",
        "Apprendre à transformer ton travail par l'innovation. Ta tendance à fuir ou à te sacrifier te freine dans la contribution originale.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends les méthodes innovantes, la santé alternative, le travail qui change les choses.",
        "Essaie une nouvelle façon de faire quelque chose au quotidien.",
        "Respire en visualisant ton quotidien réinventé avec originalité.",
        "Quelle innovation puis-je apporter dans mon travail quotidien ? »"),

    ('aquarius', 7): make_nn_interp('aquarius', 7,
        "Ton chemin d'âme t'appelle à créer des partenariats basés sur la liberté.",
        "Le Nœud Nord en Verseau dans ta maison VII t'invite à développer des relations égalitaires et innovantes. Tu quittes l'affirmation solitaire pour le partenariat libre.",
        "Apprendre à créer des relations qui respectent l'individualité de chacun. Ta tendance à dominer ou à te battre seul te freine.",
        "Tes relations sont le terrain de ton évolution. Tu apprends le partenariat d'égaux, l'amitié amoureuse, la relation qui libère.",
        "Offre plus de liberté et d'espace à un partenaire.",
        "Respire en visualisant des relations où chacun est libre et connecté.",
        "Comment puis-je créer plus de liberté dans mes relations ? »"),

    ('aquarius', 8): make_nn_interp('aquarius', 8,
        "Ton chemin d'âme t'appelle à transformer de façon révolutionnaire.",
        "Le Nœud Nord en Verseau dans ta maison VIII t'invite à aborder les transformations avec innovation. Tu quittes l'attachement pour le détachement libérateur.",
        "Apprendre à traverser les crises avec détachement et vision. Ta tendance à t'accrocher au confort te freine dans la libération.",
        "Les transformations sont le terrain de ton évolution. Tu apprends le détachement conscient, la transformation qui libère, le partage innovant.",
        "Face à un changement, adopte une perspective radicalement nouvelle.",
        "Respire en accueillant les transformations comme des libérations.",
        "Quel attachement suis-je prêt(e) à libérer pour évoluer ? »"),

    ('aquarius', 9): make_nn_interp('aquarius', 9,
        "Ton chemin d'âme t'appelle à développer une philosophie révolutionnaire.",
        "Le Nœud Nord en Verseau dans ta maison IX t'invite à développer une vision du futur. Tu quittes l'accumulation de détails pour la pensée visionnaire.",
        "Apprendre à voir au-delà du présent et à développer une vision futuriste. Ta tendance au perfectionnisme te freine dans la vision d'ensemble.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends la philosophie du futur, le voyage qui change la perspective, l'enseignement innovant.",
        "Explore une idée sur le futur qui te semble radicale.",
        "Respire en visualisant un futur lumineux que tu contribues à créer.",
        "Quelle vision du futur suis-je appelé(e) à développer ? »"),

    ('aquarius', 10): make_nn_interp('aquarius', 10,
        "Ton chemin d'âme t'appelle à devenir un agent de changement dans ta carrière.",
        "Le Nœud Nord en Verseau dans ta maison X t'invite à développer une réputation d'innovateur. Tu quittes le besoin d'approbation pour l'impact révolutionnaire.",
        "Apprendre à faire une différence par ta carrière. Ta tendance à chercher la reconnaissance personnelle te freine dans le changement collectif.",
        "Ta carrière est le terrain de ton évolution. Tu apprends à innover dans ton domaine, à avoir un impact social, à changer les structures.",
        "Identifie comment ta carrière peut contribuer au changement.",
        "Respire en visualisant une carrière qui transforme le monde.",
        "Quel changement ma carrière peut-elle apporter au monde ? »"),

    ('aquarius', 11): make_nn_interp('aquarius', 11,
        "Ton chemin d'âme t'appelle à maîtriser l'innovation collective.",
        "Le Nœud Nord en Verseau dans ta maison XI (son domicile naturel) t'invite à développer pleinement ta capacité à contribuer au collectif.",
        "Apprendre à mettre ton unicité au service du groupe. Ta tendance à chercher l'attention personnelle te freine dans la contribution collective.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends à être un catalyseur de changement, à créer des mouvements, à servir l'humanité.",
        "Engage-toi dans une cause ou un mouvement qui te tient à cœur.",
        "Respire en visualisant ton unicité au service du bien commun.",
        "Comment puis-je mieux contribuer au bien collectif ? »"),

    ('aquarius', 12): make_nn_interp('aquarius', 12,
        "Ton chemin d'âme t'appelle à libérer ton inconscient des conditionnements.",
        "Le Nœud Nord en Verseau dans ta maison XII t'invite à développer une liberté intérieure radicale. Tu quittes l'anxiété du contrôle pour la libération spirituelle.",
        "Apprendre à te libérer des conditionnements inconscients. Ta tendance au perfectionnisme ou à l'inquiétude te freine dans la liberté intérieure.",
        "L'inconscient est le terrain de ton évolution. Tu apprends la méditation de libération, l'éveil hors des conditionnements, la connexion à l'humanité.",
        "Médite en observant et libérant un conditionnement inconscient.",
        "Respire en laissant aller les chaînes invisibles qui te retiennent.",
        "Quel conditionnement inconscient suis-je prêt(e) à libérer ? »"),

    # === PISCES (M1-M12) ===
    ('pisces', 1): make_nn_interp('pisces', 1,
        "Ton chemin d'âme t'appelle à développer la compassion, l'intuition et la spiritualité.",
        "Le Nœud Nord en Poissons dans ta maison I t'invite à développer ta connexion au divin. Tu quittes le perfectionnisme de la Vierge pour la fluidité des Poissons.",
        "Apprendre à lâcher prise sur le contrôle et à faire confiance à l'univers. Ta tendance au perfectionnisme ou à l'analyse te freine dans ta connexion spirituelle.",
        "Ta présence et ton identité sont le terrain de ton évolution. Tu apprends à être fluide, intuitif, connecté à quelque chose de plus grand.",
        "Laisse aller le besoin de tout contrôler aujourd'hui.",
        "Respire en visualisant ta présence qui se dissout dans l'océan de la vie.",
        "Quel contrôle suis-je appelé(e) à lâcher ? »"),

    ('pisces', 2): make_nn_interp('pisces', 2,
        "Ton chemin d'âme t'appelle à développer un rapport spirituel à la valeur.",
        "Le Nœud Nord en Poissons dans ta maison II t'invite à développer une richesse intérieure. Tu quittes l'obsession des détails pour la valeur de l'intangible.",
        "Apprendre à valoriser ce qui ne se mesure pas. Ta tendance à tout analyser ou à t'inquiéter des détails te freine dans la vraie richesse.",
        "Tes ressources sont le terrain de ton évolution. Tu apprends que la vraie valeur est spirituelle, que l'abondance vient du lâcher-prise.",
        "Offre quelque chose sans attendre de retour mesurable.",
        "Respire en visualisant une richesse intérieure infinie.",
        "Quelle valeur intangible ai-je négligé de cultiver ? »"),

    ('pisces', 3): make_nn_interp('pisces', 3,
        "Ton chemin d'âme t'appelle à communiquer avec intuition et poésie.",
        "Le Nœud Nord en Poissons dans ta maison III t'invite à développer une expression intuitive. Tu quittes la communication logique pour la parole inspirée.",
        "Apprendre à communiquer par l'intuition et l'imagination. Ta tendance à sur-analyser ou à rester dans la logique te freine dans l'expression inspirée.",
        "Ta communication est le terrain de ton évolution. Tu apprends l'écriture poétique, la parole intuitive, l'écoute qui va au-delà des mots.",
        "Communique quelque chose de façon poétique ou intuitive.",
        "Respire en laissant les mots venir de l'océan de l'inconscient.",
        "Quelle vérité intuitive ai-je besoin d'exprimer ? »"),

    ('pisces', 4): make_nn_interp('pisces', 4,
        "Ton chemin d'âme t'appelle à créer un foyer de paix et de spiritualité.",
        "Le Nœud Nord en Poissons dans ta maison IV t'invite à développer un sanctuaire intérieur. Tu quittes l'ambition extérieure pour la paix du foyer.",
        "Apprendre à créer un espace de connexion spirituelle. Ta tendance à privilégier la carrière ou le statut te freine dans la création d'un vrai refuge.",
        "Ton foyer est le terrain de ton évolution. Tu apprends à créer un sanctuaire, un espace de paix, une connexion ancestrale spirituelle.",
        "Crée un espace de paix et de méditation dans ton foyer.",
        "Respire en visualisant ton foyer comme un temple de paix.",
        "Quel espace sacré puis-je créer chez moi ? »"),

    ('pisces', 5): make_nn_interp('pisces', 5,
        "Ton chemin d'âme t'appelle à créer et aimer avec transcendance.",
        "Le Nœud Nord en Poissons dans ta maison V t'invite à développer une créativité spirituelle et des amours transcendantes. Tu quittes le besoin du groupe pour la création sacrée.",
        "Apprendre à créer depuis ton âme et à aimer inconditionnellement. Ta tendance à rationaliser ou à chercher l'approbation te freine dans l'expression spirituelle.",
        "Ta créativité et tes amours sont le terrain de ton évolution. Tu apprends l'art sacré, l'amour inconditionnel, le jeu comme méditation.",
        "Crée quelque chose qui exprime ton âme, sans but précis.",
        "Respire en laissant la créativité spirituelle couler à travers toi.",
        "Quelle création de l'âme demande à naître de moi ? »"),

    ('pisces', 6): make_nn_interp('pisces', 6,
        "Ton chemin d'âme t'appelle à servir avec compassion et à guérir.",
        "Le Nœud Nord en Poissons dans ta maison VI t'invite à développer un travail de guérison et de service. Tu quittes le chaos pour le service compassionnel.",
        "Apprendre à prendre soin avec compassion plutôt qu'avec sacrifice. Ta tendance à fuir ou à te perdre te freine dans le service incarné.",
        "Ton travail et ta santé sont le terrain de ton évolution. Tu apprends le travail de guérison, la santé holistique, le service comme méditation.",
        "Fais une tâche quotidienne comme un acte de service sacré.",
        "Respire en visualisant chaque action comme un acte de guérison.",
        "Comment puis-je servir avec plus de compassion aujourd'hui ? »"),

    ('pisces', 7): make_nn_interp('pisces', 7,
        "Ton chemin d'âme t'appelle à créer des partenariats de compassion.",
        "Le Nœud Nord en Poissons dans ta maison VII t'invite à développer des relations basées sur la compassion. Tu quittes l'affirmation pour la fusion aimante.",
        "Apprendre à aimer sans conditions et à se connecter au niveau de l'âme. Ta tendance à te battre ou à rester indépendant te freine dans la connexion profonde.",
        "Tes relations sont le terrain de ton évolution. Tu apprends l'amour compassionnel, le partenariat d'âmes, la connexion au-delà des mots.",
        "Offre de la compassion inconditionnelle à un partenaire.",
        "Respire en visualisant des relations baignées de compassion.",
        "Comment puis-je aimer avec plus de compassion et moins de conditions ? »"),

    ('pisces', 8): make_nn_interp('pisces', 8,
        "Ton chemin d'âme t'appelle à te laisser transformer par le divin.",
        "Le Nœud Nord en Poissons dans ta maison VIII t'invite à développer l'abandon dans les transformations. Tu quittes l'attachement pour le lâcher-prise total.",
        "Apprendre à traverser les crises avec confiance dans l'univers. Ta tendance à t'accrocher au confort te freine dans la dissolution libératrice.",
        "Les transformations sont le terrain de ton évolution. Tu apprends le lâcher-prise total, la mort comme retour à la source, l'intimité spirituelle.",
        "Abandonne-toi à une transformation en cours au lieu de la résister.",
        "Respire en laissant aller tout ce qui doit mourir.",
        "Qu'est-ce que l'univers me demande de lâcher ? »"),

    ('pisces', 9): make_nn_interp('pisces', 9,
        "Ton chemin d'âme t'appelle à développer une foi mystique.",
        "Le Nœud Nord en Poissons dans ta maison IX t'invite à développer une spiritualité de transcendance. Tu quittes le perfectionnisme pour la foi.",
        "Apprendre à faire confiance au mystère et à développer ta connexion au divin. Ta tendance à analyser ou à servir te freine dans la transcendance.",
        "Ta spiritualité est le terrain de ton évolution. Tu apprends la foi sans preuve, le voyage intérieur, l'enseignement mystique.",
        "Médite en te connectant à quelque chose de plus grand que toi.",
        "Respire en laissant la foi remplacer le doute.",
        "Quelle foi mystique suis-je appelé(e) à développer ? »"),

    ('pisces', 10): make_nn_interp('pisces', 10,
        "Ton chemin d'âme t'appelle à mettre ta carrière au service de quelque chose de plus grand.",
        "Le Nœud Nord en Poissons dans ta maison X t'invite à développer une réputation de compassion. Tu quittes la dépendance émotionnelle pour le service public.",
        "Apprendre à offrir ta carrière au monde comme un service. Ta tendance à rester dans le confort du foyer te freine dans ta mission.",
        "Ta carrière est le terrain de ton évolution. Tu apprends le travail qui guérit, la réputation de compassion, le service au monde.",
        "Offre les fruits de ton travail à quelque chose de plus grand.",
        "Respire en visualisant ta carrière comme un acte de service universel.",
        "Comment ma carrière peut-elle mieux servir le monde ? »"),

    ('pisces', 11): make_nn_interp('pisces', 11,
        "Ton chemin d'âme t'appelle à développer une compassion universelle.",
        "Le Nœud Nord en Poissons dans ta maison XI t'invite à développer des connexions basées sur la compassion. Tu quittes le besoin d'être spécial pour servir l'humanité.",
        "Apprendre à aimer l'humanité sans conditions. Ta tendance à chercher l'attention te freine dans le service au collectif.",
        "Tes amitiés et projets sont le terrain de ton évolution. Tu apprends l'amitié inconditionnelle, les causes humanitaires, le service sans ego.",
        "Offre de la compassion à un groupe ou une cause sans rien attendre.",
        "Respire en visualisant ta compassion qui s'étend à toute l'humanité.",
        "Comment puis-je servir l'humanité avec plus de compassion ? »"),

    ('pisces', 12): make_nn_interp('pisces', 12,
        "Ton chemin d'âme t'appelle à maîtriser la dissolution et l'unité mystique.",
        "Le Nœud Nord en Poissons dans ta maison XII (son domicile naturel) t'invite à développer pleinement ta connexion spirituelle.",
        "Apprendre à te dissoudre dans l'océan de la conscience. Ta tendance au perfectionnisme ou à l'inquiétude te freine dans l'union mystique.",
        "L'inconscient est le terrain de ton évolution. Tu apprends la méditation profonde, la connexion à tout ce qui est, la guérison par l'abandon.",
        "Médite en laissant toutes les frontières se dissoudre.",
        "Respire en te laissant fondre dans l'océan infini de la conscience.",
        "Quelle union avec le tout suis-je appelé(e) à expérimenter ? »"),
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
