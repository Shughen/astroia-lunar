#!/usr/bin/env python3
"""Insert South Node interpretations for Sagittarius, Capricorn, Aquarius, Pisces (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_sn_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'sagittarius': '☋ Nœud Sud en Sagittaire',
        'capricorn': '☋ Nœud Sud en Capricorne',
        'aquarius': '☋ Nœud Sud en Verseau',
        'pisces': '☋ Nœud Sud en Poissons',
    }
    sign_fr = {
        'sagittarius': 'Sagittaire',
        'capricorn': 'Capricorne',
        'aquarius': 'Verseau',
        'pisces': 'Poissons',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ton acquis karmique
{moteur}

## Ton piège
{defi}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

SOUTH_NODE_INTERPRETATIONS = {
    # === SAGITTARIUS (M1-M12) ===
    ('sagittarius', 1): make_sn_interp('sagittarius', 1,
        "Tu arrives avec une maîtrise de l'aventure et de l'optimisme — mais l'excès de liberté te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison I indique une maîtrise karmique de l'expansion et de l'aventure. Tu sais explorer, philosopher et voir grand.",
        "L'excès de liberté et le manque de focus peuvent te piéger. Ta tendance à toujours chercher plus loin te coupe de l'ancrage et des détails importants.",
        "Ta présence porte la mémoire du voyageur éternel. Tu dois maintenant apprendre à te fixer, à approfondir un domaine et à valoriser ce qui est proche.",
        "Reste quelque part au lieu de chercher ailleurs.",
        "Respire en appréciant exactement là où tu es maintenant.",
        "Comment ma quête constante d'ailleurs m'empêche-t-elle d'être vraiment présent ici ? »"),

    ('sagittarius', 2): make_sn_interp('sagittarius', 2,
        "Tu arrives avec une maîtrise de l'abondance philosophique — mais la négligence matérielle te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison II indique une maîtrise karmique de la richesse des idées. Tu sais trouver de la valeur dans les concepts et les croyances.",
        "La négligence des détails matériels peut te piéger. Ta tendance à voir grand te coupe de la gestion pratique des ressources.",
        "Tes finances portent la mémoire de l'insouciance. Tu dois maintenant apprendre la valeur des détails et la gestion précise.",
        "Gère un aspect pratique de tes finances que tu évitais.",
        "Respire en valorisant le concret autant que l'abstrait.",
        "Comment ma vision des grandes choses me fait-elle négliger les petites ? »"),

    ('sagittarius', 3): make_sn_interp('sagittarius', 3,
        "Tu arrives avec une maîtrise de la communication inspirante — mais le prêche te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison III indique une maîtrise karmique de la parole expansive. Tu sais communiquer avec enthousiasme et partager ta vision.",
        "Le prêche et le monologue peuvent te piéger. Ta tendance à enseigner plutôt qu'échanger te coupe du vrai dialogue.",
        "Ta communication porte la mémoire du professeur. Tu dois maintenant apprendre à écouter, à poser des questions et à valoriser les détails.",
        "Écoute plus que tu ne parles dans ta prochaine conversation.",
        "Respire en créant de l'espace pour les idées des autres.",
        "Quand est-ce que j'enseigne au lieu d'échanger ? »"),

    ('sagittarius', 4): make_sn_interp('sagittarius', 4,
        "Tu arrives avec une maîtrise des racines cosmopolites — mais le déracinement te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison IV indique une maîtrise karmique de la liberté familiale. Tu sais voyager, explorer et élargir les horizons du foyer.",
        "Le déracinement peut te piéger. Ta tendance à ne pas t'attacher te coupe de la stabilité et de l'intimité familiale.",
        "Ton foyer porte la mémoire de l'errance. Tu dois maintenant apprendre à créer des racines profondes et un chez-toi stable.",
        "Investis dans quelque chose de permanent pour ton foyer.",
        "Respire en te sentant ancré là où tu es.",
        "Comment mon besoin de liberté m'empêche-t-il de créer un vrai chez-moi ? »"),

    ('sagittarius', 5): make_sn_interp('sagittarius', 5,
        "Tu arrives avec une maîtrise de la créativité expansive — mais l'excès d'enthousiasme te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison V indique une maîtrise karmique de la création joyeuse. Tu sais créer avec optimisme et aimer avec passion aventureuse.",
        "L'excès d'enthousiasme peut te piéger. Ta tendance à toujours chercher la prochaine aventure te coupe de l'approfondissement.",
        "Ta créativité porte la mémoire de la chasse. Tu dois maintenant apprendre à approfondir tes créations et tes amours.",
        "Approfondis une création ou une relation existante au lieu d'en chercher une nouvelle.",
        "Respire en trouvant la joie dans ce que tu as déjà.",
        "Combien de projets ou d'amours ai-je abandonnés pour la prochaine aventure ? »"),

    ('sagittarius', 6): make_sn_interp('sagittarius', 6,
        "Tu arrives avec une maîtrise du travail inspirant — mais le manque de méthode te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison VI indique une maîtrise karmique du travail visionnaire. Tu sais voir le sens et inspirer au quotidien.",
        "Le manque de méthode et de détails peut te piéger. Ta tendance à voir grand te coupe de l'efficacité pratique.",
        "Ton travail porte la mémoire de la vision. Tu dois maintenant apprendre la méthode, les détails et la rigueur quotidienne.",
        "Accomplis une tâche minutieusement, avec attention aux détails.",
        "Respire en appréciant la beauté du travail précis.",
        "Comment mon manque de méthode me rend-il moins efficace ? »"),

    ('sagittarius', 7): make_sn_interp('sagittarius', 7,
        "Tu arrives avec une maîtrise des relations libres — mais le manque d'engagement te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison VII indique une maîtrise karmique du partenariat aventurier. Tu sais créer des relations stimulantes et expansives.",
        "Le manque d'engagement peut te piéger. Ta tendance à garder tes options ouvertes te coupe de l'intimité profonde.",
        "Tes relations portent la mémoire de la liberté. Tu dois maintenant apprendre l'engagement, la présence et la profondeur relationnelle.",
        "Engage-toi pleinement dans une relation au lieu de garder tes distances.",
        "Respire en te sentant présent et engagé.",
        "Comment mon besoin de liberté sabote-t-il mes relations ? »"),

    ('sagittarius', 8): make_sn_interp('sagittarius', 8,
        "Tu arrives avec une maîtrise de la transformation philosophique — mais la fuite en avant te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison VIII indique une maîtrise karmique de la compréhension des crises. Tu sais trouver du sens dans les transformations.",
        "La fuite en avant peut te piéger. Ta tendance à intellectualiser les crises te coupe de leur vécu émotionnel.",
        "Tes transformations portent la mémoire de la philosophie. Tu dois maintenant apprendre à vivre les crises plutôt qu'à les comprendre.",
        "Vis une émotion intense sans la philosophiser.",
        "Respire en descendant dans l'expérience au lieu de t'élever vers le sens.",
        "Comment ma fuite vers le sens m'empêche-t-elle de vraiment transformer ? »"),

    ('sagittarius', 9): make_sn_interp('sagittarius', 9,
        "Tu arrives avec une maîtrise de l'expansion spirituelle — mais le dogmatisme te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison IX (son domicile) indique une maîtrise karmique profonde de la quête de vérité. Tu sais explorer les philosophies et enseigner.",
        "Le dogmatisme et l'excès de certitude peuvent te piéger. Ta tendance à croire avoir trouvé LA vérité te ferme aux autres perspectives.",
        "Ta spiritualité porte la mémoire du sage. Tu dois maintenant apprendre l'humilité, la curiosité et l'écoute des vérités locales.",
        "Apprends quelque chose de nouveau d'une source inattendue.",
        "Respire en relâchant le besoin d'avoir raison.",
        "Comment mes certitudes me ferment-elles à la vraie sagesse ? »"),

    ('sagittarius', 10): make_sn_interp('sagittarius', 10,
        "Tu arrives avec une maîtrise de la carrière visionnaire — mais le manque de structure te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison X indique une maîtrise karmique du leadership inspirant. Tu sais voir grand et communiquer une vision.",
        "Le manque de structure peut te piéger. Ta tendance à toujours voir plus loin te coupe de la construction méthodique.",
        "Ta carrière porte la mémoire du visionnaire. Tu dois maintenant apprendre à construire pas à pas, avec méthode et patience.",
        "Construis quelque chose de concret au lieu de planifier le prochain projet.",
        "Respire en appréciant le processus de construction.",
        "Comment mon impatience visionnaire sabote-t-elle ma carrière ? »"),

    ('sagittarius', 11): make_sn_interp('sagittarius', 11,
        "Tu arrives avec une maîtrise des groupes idéalistes — mais l'excès d'idéalisme te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison XI indique une maîtrise karmique des mouvements collectifs. Tu sais inspirer les groupes et créer des causes.",
        "L'excès d'idéalisme peut te piéger. Ta tendance à voir le potentiel plutôt que la réalité te coupe de l'amitié authentique.",
        "Tes amitiés portent la mémoire de la cause. Tu dois maintenant apprendre à voir tes amis comme ils sont, pas comme tu voudrais qu'ils soient.",
        "Apprécie un ami tel qu'il est, sans vouloir l'améliorer.",
        "Respire en accueillant la réalité de tes amitiés.",
        "Comment mon idéalisme me coupe-t-il de mes amis réels ? »"),

    ('sagittarius', 12): make_sn_interp('sagittarius', 12,
        "Tu arrives avec une maîtrise de la connexion cosmique — mais la fuite spirituelle te freine.",
        "Le Nœud Sud en Sagittaire dans ta maison XII indique une maîtrise karmique de la spiritualité expansive. Tu sais te connecter aux grandes vérités.",
        "La fuite spirituelle peut te piéger. Ta tendance à chercher l'absolu te coupe de l'action concrète dans le monde.",
        "Ton monde intérieur porte la mémoire de l'expansion. Tu dois maintenant apprendre à servir concrètement plutôt qu'à philosopher.",
        "Agis concrètement pour aider quelqu'un au lieu de méditer.",
        "Respire en ancrant ta spiritualité dans le service.",
        "Comment ma quête spirituelle me sert-elle d'excuse pour ne pas agir ? »"),

    # === CAPRICORN (M1-M12) ===
    ('capricorn', 1): make_sn_interp('capricorn', 1,
        "Tu arrives avec une maîtrise de l'autorité et de la structure — mais la rigidité te freine.",
        "Le Nœud Sud en Capricorne dans ta maison I indique une maîtrise karmique du sérieux et de la responsabilité. Tu sais te discipliner et atteindre tes objectifs.",
        "La rigidité et l'excès de contrôle peuvent te piéger. Ta tendance à tout prendre au sérieux te coupe de la spontanéité et des émotions.",
        "Ta présence porte la mémoire du patriarche. Tu dois maintenant apprendre la vulnérabilité, la tendresse et l'ouverture émotionnelle.",
        "Montre une vulnérabilité au lieu de maintenir ta façade.",
        "Respire en relâchant le besoin de contrôle.",
        "Où ma rigidité m'empêche-t-elle de vivre pleinement ? »"),

    ('capricorn', 2): make_sn_interp('capricorn', 2,
        "Tu arrives avec une maîtrise de l'accumulation méthodique — mais l'avarice te freine.",
        "Le Nœud Sud en Capricorne dans ta maison II indique une maîtrise karmique de la construction de richesse. Tu sais accumuler avec patience et discipline.",
        "L'avarice et la peur du manque peuvent te piéger. Ta tendance à contrôler tes ressources te coupe du partage et de l'abondance.",
        "Tes finances portent la mémoire de la restriction. Tu dois maintenant apprendre à partager, à faire confiance et à nourrir.",
        "Partage une ressource sans calcul stratégique.",
        "Respire en te sentant abondant et généreux.",
        "Comment ma peur du manque me prive-t-elle de la vraie richesse ? »"),

    ('capricorn', 3): make_sn_interp('capricorn', 3,
        "Tu arrives avec une maîtrise de la communication structurée — mais la froideur te freine.",
        "Le Nœud Sud en Capricorne dans ta maison III indique une maîtrise karmique de la parole efficace. Tu sais communiquer avec précision et autorité.",
        "La froideur et le manque d'émotion peuvent te piéger. Ta tendance à la communication professionnelle te coupe de l'intimité verbale.",
        "Ta communication porte la mémoire de l'autorité. Tu dois maintenant apprendre à communiquer avec le cœur, avec tendresse.",
        "Partage quelque chose de personnel et vulnérable.",
        "Respire en laissant tes mots porter de l'émotion.",
        "Quand ma communication efficace devient-elle froide et distante ? »"),

    ('capricorn', 4): make_sn_interp('capricorn', 4,
        "Tu arrives avec une maîtrise de la structure familiale — mais l'autorité excessive te freine.",
        "Le Nœud Sud en Capricorne dans ta maison IV indique une maîtrise karmique de la responsabilité familiale. Tu sais organiser et structurer le foyer.",
        "L'autorité excessive peut te piéger. Ta tendance à contrôler le foyer te coupe de l'intimité et de la chaleur émotionnelle.",
        "Ton foyer porte la mémoire de la hiérarchie. Tu dois maintenant apprendre à créer un foyer chaleureux, nourricier et émotionnel.",
        "Crée un moment de tendresse au foyer au lieu de discipline.",
        "Respire en laissant ton foyer devenir un nid chaleureux.",
        "Comment mon autorité au foyer refroidit-elle les liens familiaux ? »"),

    ('capricorn', 5): make_sn_interp('capricorn', 5,
        "Tu arrives avec une maîtrise de la création disciplinée — mais le manque de joie te freine.",
        "Le Nœud Sud en Capricorne dans ta maison V indique une maîtrise karmique de la création structurée. Tu sais produire des œuvres durables et des amours sérieux.",
        "Le manque de joie peut te piéger. Ta tendance à tout prendre au sérieux te coupe du plaisir et de la légèreté créative.",
        "Ta créativité porte la mémoire du travail. Tu dois maintenant apprendre à créer pour le plaisir, à jouer et à aimer légèrement.",
        "Crée quelque chose juste pour le plaisir, sans objectif.",
        "Respire en retrouvant l'enfant créatif en toi.",
        "Quand ai-je oublié de m'amuser dans ma créativité et mes amours ? »"),

    ('capricorn', 6): make_sn_interp('capricorn', 6,
        "Tu arrives avec une maîtrise du travail acharné — mais le surmenage te freine.",
        "Le Nœud Sud en Capricorne dans ta maison VI indique une maîtrise karmique de l'effort et de la discipline. Tu sais travailler dur et atteindre tes objectifs quotidiens.",
        "Le surmenage peut te piéger. Ta tendance à tout sacrifier au travail te coupe de ta santé et de ton bien-être.",
        "Ton travail porte la mémoire de l'esclave. Tu dois maintenant apprendre à prendre soin de toi, à nourrir ton corps et ton âme.",
        "Prends une pause non-productive juste pour toi.",
        "Respire en relâchant la pression du devoir.",
        "Comment mon acharnement au travail détruit-il ma santé ? »"),

    ('capricorn', 7): make_sn_interp('capricorn', 7,
        "Tu arrives avec une maîtrise des relations structurées — mais le manque de tendresse te freine.",
        "Le Nœud Sud en Capricorne dans ta maison VII indique une maîtrise karmique du partenariat responsable. Tu sais créer des relations stables et durables.",
        "Le manque de tendresse peut te piéger. Ta tendance à voir le partenariat comme un contrat te coupe de l'intimité émotionnelle.",
        "Tes relations portent la mémoire du devoir. Tu dois maintenant apprendre l'amour tendre, le soin et la vulnérabilité.",
        "Offre un geste de tendresse sans raison à ton partenaire.",
        "Respire en ouvrant ton cœur à l'intimité.",
        "Comment mon approche contractuelle de l'amour me prive-t-elle de tendresse ? »"),

    ('capricorn', 8): make_sn_interp('capricorn', 8,
        "Tu arrives avec une maîtrise du contrôle des crises — mais la peur de lâcher prise te freine.",
        "Le Nœud Sud en Capricorne dans ta maison VIII indique une maîtrise karmique de la gestion des transformations. Tu sais garder le contrôle même dans les crises.",
        "La peur de lâcher prise peut te piéger. Ta tendance à contrôler les processus te coupe de la vraie métamorphose.",
        "Tes transformations portent la mémoire du contrôle. Tu dois maintenant apprendre à te rendre, à accueillir et à faire confiance.",
        "Lâche le contrôle dans une situation de transformation.",
        "Respire en faisant confiance au processus.",
        "Où mon besoin de contrôle m'empêche-t-il de me transformer ? »"),

    ('capricorn', 9): make_sn_interp('capricorn', 9,
        "Tu arrives avec une maîtrise des traditions — mais le conservatisme te freine.",
        "Le Nœud Sud en Capricorne dans ta maison IX indique une maîtrise karmique des structures spirituelles. Tu sais respecter les traditions et enseigner l'autorité.",
        "Le conservatisme peut te piéger. Ta tendance à rester dans les traditions te coupe de l'exploration et de la nouveauté.",
        "Ta spiritualité porte la mémoire de l'institution. Tu dois maintenant apprendre à explorer librement, à questionner et à innover.",
        "Explore une croyance non-traditionnelle.",
        "Respire en ouvrant ton esprit au-delà des structures connues.",
        "Quelles traditions spirituelles me limitent-elles ? »"),

    ('capricorn', 10): make_sn_interp('capricorn', 10,
        "Tu arrives avec une maîtrise de l'ambition et du statut — mais l'obsession de carrière te freine.",
        "Le Nœud Sud en Capricorne dans ta maison X (son domicile) indique une maîtrise karmique profonde de la réussite. Tu sais construire une carrière et atteindre les sommets.",
        "L'obsession du statut peut te piéger. Ta tendance à tout sacrifier à la carrière te coupe de ta vie privée et de tes émotions.",
        "Ta carrière porte la mémoire du conquérant. Tu dois maintenant apprendre à nourrir ta vie personnelle, ta famille et tes émotions.",
        "Passe du temps de qualité en famille au lieu de travailler.",
        "Respire en relâchant l'ambition et en accueillant la tendresse.",
        "Qu'ai-je sacrifié à ma carrière que je regrette ? »"),

    ('capricorn', 11): make_sn_interp('capricorn', 11,
        "Tu arrives avec une maîtrise des groupes hiérarchiques — mais le besoin de contrôle te freine.",
        "Le Nœud Sud en Capricorne dans ta maison XI indique une maîtrise karmique du leadership structuré. Tu sais organiser les groupes et créer des systèmes.",
        "Le besoin de contrôle peut te piéger. Ta tendance à hiérarchiser les amitiés te coupe de l'égalité et de la spontanéité.",
        "Tes amitiés portent la mémoire de la hiérarchie. Tu dois maintenant apprendre l'amitié égalitaire, la joie et la spontanéité.",
        "Participe à un groupe sans chercher à le diriger.",
        "Respire en te sentant égal parmi tes amis.",
        "Comment mon besoin de contrôle affecte-t-il mes amitiés ? »"),

    ('capricorn', 12): make_sn_interp('capricorn', 12,
        "Tu arrives avec une maîtrise de la solitude structurée — mais l'isolement te freine.",
        "Le Nœud Sud en Capricorne dans ta maison XII indique une maîtrise karmique de la retraite disciplinée. Tu sais te retirer et travailler dans l'ombre.",
        "L'isolement peut te piéger. Ta tendance à tout faire seul te coupe de l'aide et de la connexion.",
        "Ton monde intérieur porte la mémoire de la tour d'ivoire. Tu dois maintenant apprendre à t'ouvrir, à recevoir et à te connecter.",
        "Demande de l'aide ou du soutien à quelqu'un.",
        "Respire en ouvrant ton cœur à la connexion.",
        "Comment mon isolement me prive-t-il de soutien ? »"),

    # === AQUARIUS (M1-M12) ===
    ('aquarius', 1): make_sn_interp('aquarius', 1,
        "Tu arrives avec une maîtrise de l'originalité et du détachement — mais l'excès de distance te freine.",
        "Le Nœud Sud en Verseau dans ta maison I indique une maîtrise karmique de l'indépendance et de l'originalité. Tu sais être unique et penser différemment.",
        "L'excès de détachement peut te piéger. Ta tendance à te tenir à l'écart te coupe des connexions profondes et de la chaleur.",
        "Ta présence porte la mémoire du rebelle. Tu dois maintenant apprendre à t'engager émotionnellement et à créer des liens spéciaux.",
        "Engage-toi dans une relation au lieu de rester détaché.",
        "Respire en te permettant d'être touché émotionnellement.",
        "Où mon détachement me prive-t-il de vraies connexions ? »"),

    ('aquarius', 2): make_sn_interp('aquarius', 2,
        "Tu arrives avec une maîtrise des ressources non-conventionnelles — mais l'instabilité te freine.",
        "Le Nœud Sud en Verseau dans ta maison II indique une maîtrise karmique de l'indépendance financière. Tu sais créer des revenus alternatifs et ne pas dépendre du système.",
        "L'instabilité peut te piéger. Ta tendance à rejeter les voies classiques te coupe de la sécurité matérielle.",
        "Tes finances portent la mémoire de la rébellion. Tu dois maintenant apprendre à créer de la stabilité et à apprécier la simplicité.",
        "Crée de la stabilité financière par une voie simple.",
        "Respire en appréciant la sécurité matérielle.",
        "Comment ma résistance aux voies classiques me prive-t-elle de stabilité ? »"),

    ('aquarius', 3): make_sn_interp('aquarius', 3,
        "Tu arrives avec une maîtrise de la communication innovante — mais le détachement te freine.",
        "Le Nœud Sud en Verseau dans ta maison III indique une maîtrise karmique de la pensée originale. Tu sais communiquer des idées révolutionnaires.",
        "Le détachement peut te piéger. Ta tendance à intellectualiser te coupe de la communication du cœur.",
        "Ta communication porte la mémoire de l'intellect froid. Tu dois maintenant apprendre à communiquer avec passion et chaleur.",
        "Parle de ce que tu ressens au lieu de ce que tu penses.",
        "Respire en laissant tes mots venir du cœur.",
        "Quand est-ce que ma communication intellectuelle manque de chaleur ? »"),

    ('aquarius', 4): make_sn_interp('aquarius', 4,
        "Tu arrives avec une maîtrise du foyer non-conventionnel — mais le détachement familial te freine.",
        "Le Nœud Sud en Verseau dans ta maison IV indique une maîtrise karmique de la famille choisie. Tu sais créer des structures familiales alternatives.",
        "Le détachement émotionnel peut te piéger. Ta tendance à ne pas t'attacher te coupe de l'intimité familiale.",
        "Ton foyer porte la mémoire de la distance. Tu dois maintenant apprendre à créer un nid chaleureux et à t'attacher émotionnellement.",
        "Crée un moment d'intimité émotionnelle en famille.",
        "Respire en te sentant connecté à tes racines.",
        "Comment mon détachement familial me prive-t-il de vraies racines ? »"),

    ('aquarius', 5): make_sn_interp('aquarius', 5,
        "Tu arrives avec une maîtrise de la créativité révolutionnaire — mais le détachement amoureux te freine.",
        "Le Nœud Sud en Verseau dans ta maison V indique une maîtrise karmique de la création originale. Tu sais créer de façon innovante et aimer librement.",
        "Le détachement peut te piéger. Ta tendance à ne pas t'engager émotionnellement te coupe de la passion et de la joie.",
        "Ta créativité porte la mémoire de l'expérimentation. Tu dois maintenant apprendre à créer avec le cœur et à aimer passionnément.",
        "Crée ou aime avec passion au lieu de détachement.",
        "Respire en te permettant d'être passionné.",
        "Comment mon détachement amoureux me prive-t-il de vraie intimité ? »"),

    ('aquarius', 6): make_sn_interp('aquarius', 6,
        "Tu arrives avec une maîtrise du travail innovant — mais le rejet des routines te freine.",
        "Le Nœud Sud en Verseau dans ta maison VI indique une maîtrise karmique de l'innovation au quotidien. Tu sais transformer les routines et travailler différemment.",
        "Le rejet des routines peut te piéger. Ta tendance à résister à la structure te coupe de l'efficacité et de la santé.",
        "Ton travail porte la mémoire de la révolution. Tu dois maintenant apprendre à apprécier les routines saines et le service simple.",
        "Établis et suis une routine bénéfique.",
        "Respire en appréciant la beauté de la régularité.",
        "Comment ma résistance aux routines nuit-elle à ma santé et mon efficacité ? »"),

    ('aquarius', 7): make_sn_interp('aquarius', 7,
        "Tu arrives avec une maîtrise des relations libres — mais le détachement te freine.",
        "Le Nœud Sud en Verseau dans ta maison VII indique une maîtrise karmique du partenariat égalitaire. Tu sais créer des relations basées sur la liberté et l'amitié.",
        "Le détachement émotionnel peut te piéger. Ta tendance à éviter la fusion te coupe de l'intimité profonde.",
        "Tes relations portent la mémoire de la distance. Tu dois maintenant apprendre l'engagement passionné et la spécialité de l'être aimé.",
        "Traite ton partenaire comme spécial, pas comme tout le monde.",
        "Respire en ouvrant ton cœur à l'amour exclusif.",
        "Comment mon détachement m'empêche-t-il de vraiment aimer ? »"),

    ('aquarius', 8): make_sn_interp('aquarius', 8,
        "Tu arrives avec une maîtrise de la transformation détachée — mais l'intellectualisation te freine.",
        "Le Nœud Sud en Verseau dans ta maison VIII indique une maîtrise karmique de la compréhension des processus de transformation. Tu sais observer les crises avec recul.",
        "L'intellectualisation peut te piéger. Ta tendance à analyser les transformations te coupe de leur vécu émotionnel.",
        "Tes transformations portent la mémoire de la distance. Tu dois maintenant apprendre à plonger dans l'intensité émotionnelle.",
        "Vis une émotion intense sans la décortiquer.",
        "Respire en te permettant d'être submergé par l'émotion.",
        "Quand mon détachement m'empêche-t-il de me transformer vraiment ? »"),

    ('aquarius', 9): make_sn_interp('aquarius', 9,
        "Tu arrives avec une maîtrise des idées progressistes — mais le dogmatisme inversé te freine.",
        "Le Nœud Sud en Verseau dans ta maison IX indique une maîtrise karmique de la pensée révolutionnaire. Tu sais remettre en question et innover philosophiquement.",
        "Le dogmatisme inversé peut te piéger. Ta tendance à rejeter automatiquement la tradition te coupe de la sagesse ancienne.",
        "Ta spiritualité porte la mémoire de la révolution. Tu dois maintenant apprendre à honorer aussi la tradition et la sagesse du passé.",
        "Explore une sagesse traditionnelle avec respect.",
        "Respire en accueillant l'ancien comme le nouveau.",
        "Comment mon rejet automatique de la tradition me limite-t-il ? »"),

    ('aquarius', 10): make_sn_interp('aquarius', 10,
        "Tu arrives avec une maîtrise de la carrière non-conventionnelle — mais le rejet de l'autorité te freine.",
        "Le Nœud Sud en Verseau dans ta maison X indique une maîtrise karmique de l'innovation professionnelle. Tu sais créer ta propre voie et rejeter les structures.",
        "Le rejet de l'autorité peut te piéger. Ta tendance à résister aux hiérarchies te coupe de la reconnaissance et du pouvoir légitime.",
        "Ta carrière porte la mémoire du rebelle. Tu dois maintenant apprendre à embrasser l'autorité légitime et à créer avec chaleur.",
        "Accepte une forme d'autorité ou de structure bénéfique.",
        "Respire en te sentant à l'aise avec le pouvoir.",
        "Comment ma résistance à l'autorité limite-t-elle ma carrière ? »"),

    ('aquarius', 11): make_sn_interp('aquarius', 11,
        "Tu arrives avec une maîtrise des réseaux et des causes — mais le détachement te freine.",
        "Le Nœud Sud en Verseau dans ta maison XI (son domicile) indique une maîtrise karmique profonde du collectif. Tu sais créer des mouvements et fédérer les groupes.",
        "Le détachement personnel peut te piéger. Ta tendance à voir les gens comme des idées te coupe des amitiés profondes.",
        "Tes amitiés portent la mémoire de la distance. Tu dois maintenant apprendre à voir tes amis comme des individus spéciaux, pas comme des représentants d'idées.",
        "Traite un ami comme unique et spécial.",
        "Respire en voyant la personne derrière l'idée.",
        "Comment mon détachement m'empêche-t-il de vraiment connaître mes amis ? »"),

    ('aquarius', 12): make_sn_interp('aquarius', 12,
        "Tu arrives avec une maîtrise de la transcendance intellectuelle — mais le détachement spirituel te freine.",
        "Le Nœud Sud en Verseau dans ta maison XII indique une maîtrise karmique de la compréhension cosmique. Tu sais te connecter à l'universel par la pensée.",
        "Le détachement peut te piéger. Ta tendance à intellectualiser le spirituel te coupe de l'expérience mystique directe.",
        "Ton monde intérieur porte la mémoire de la distance. Tu dois maintenant apprendre à te dissoudre dans le cœur, pas dans l'esprit.",
        "Médite avec le cœur au lieu de l'esprit.",
        "Respire en te laissant toucher par le mystère.",
        "Comment mon détachement spirituel me coupe-t-il de l'expérience directe ? »"),

    # === PISCES (M1-M12) ===
    ('pisces', 1): make_sn_interp('pisces', 1,
        "Tu arrives avec une maîtrise de la sensibilité et de l'intuition — mais la perte des limites te freine.",
        "Le Nœud Sud en Poissons dans ta maison I indique une maîtrise karmique de la connexion universelle. Tu sais te fondre, ressentir et te connecter au tout.",
        "La perte des limites peut te piéger. Ta tendance à te dissoudre te coupe de ta propre identité et de ta capacité d'action.",
        "Ta présence porte la mémoire de l'océan. Tu dois maintenant apprendre à définir qui tu es, à poser des limites et à agir concrètement.",
        "Définis clairement une limite ou une position personnelle.",
        "Respire en te sentant solide et défini.",
        "Où ma tendance à me fondre me fait-elle perdre mon identité ? »"),

    ('pisces', 2): make_sn_interp('pisces', 2,
        "Tu arrives avec une maîtrise du détachement matériel — mais le manque de structure te freine.",
        "Le Nœud Sud en Poissons dans ta maison II indique une maîtrise karmique du non-attachement. Tu sais ne pas t'accrocher aux possessions et vivre simplement.",
        "Le manque de structure peut te piéger. Ta tendance à négliger le matériel te coupe de la sécurité et de l'efficacité.",
        "Tes finances portent la mémoire de la dissolution. Tu dois maintenant apprendre à créer une structure financière claire et stable.",
        "Organise un aspect pratique de tes finances.",
        "Respire en te sentant ancré dans la matière.",
        "Comment ma négligence matérielle crée-t-elle de l'instabilité ? »"),

    ('pisces', 3): make_sn_interp('pisces', 3,
        "Tu arrives avec une maîtrise de la communication intuitive — mais la confusion te freine.",
        "Le Nœud Sud en Poissons dans ta maison III indique une maîtrise karmique de la communication empathique. Tu sais ressentir et transmettre des messages subtils.",
        "La confusion peut te piéger. Ta tendance à communiquer par impression te coupe de la clarté et de la précision.",
        "Ta communication porte la mémoire du rêve. Tu dois maintenant apprendre à communiquer clairement, avec précision et discernement.",
        "Exprime une idée de façon claire et structurée.",
        "Respire en clarifiant tes pensées avant de parler.",
        "Quand ma communication intuitive devient-elle confusion ? »"),

    ('pisces', 4): make_sn_interp('pisces', 4,
        "Tu arrives avec une maîtrise de l'amour familial inconditionnel — mais le sacrifice te freine.",
        "Le Nœud Sud en Poissons dans ta maison IV indique une maîtrise karmique de la compassion familiale. Tu sais aimer sans conditions et te sacrifier pour les tiens.",
        "Le sacrifice excessif peut te piéger. Ta tendance à te perdre pour ta famille te coupe de ton propre bien-être.",
        "Ton foyer porte la mémoire du martyr. Tu dois maintenant apprendre à créer des limites saines et à te construire une carrière.",
        "Pose une limite familiale claire et saine.",
        "Respire en te donnant la permission de prendre soin de toi.",
        "Comment mon sacrifice familial me détruit-il ? »"),

    ('pisces', 5): make_sn_interp('pisces', 5,
        "Tu arrives avec une maîtrise de la créativité inspirée — mais la fuite dans l'imaginaire te freine.",
        "Le Nœud Sud en Poissons dans ta maison V indique une maîtrise karmique de la création mystique. Tu sais créer à partir de l'invisible et aimer inconditionnellement.",
        "La fuite dans l'imaginaire peut te piéger. Ta tendance à rêver tes créations plutôt qu'à les réaliser te coupe de l'accomplissement.",
        "Ta créativité porte la mémoire du rêveur. Tu dois maintenant apprendre à ancrer ta créativité dans le réel et à finir tes projets.",
        "Termine un projet créatif au lieu d'en rêver un nouveau.",
        "Respire en ancrant ton inspiration dans l'action.",
        "Combien de créations restent-elles dans mon imagination sans jamais se réaliser ? »"),

    ('pisces', 6): make_sn_interp('pisces', 6,
        "Tu arrives avec une maîtrise du service désintéressé — mais le manque de limites te freine.",
        "Le Nœud Sud en Poissons dans ta maison VI indique une maîtrise karmique du service compassionnel. Tu sais aider sans compter et te sacrifier au quotidien.",
        "Le manque de limites peut te piéger. Ta tendance à donner sans recevoir te coupe de ta propre santé et efficacité.",
        "Ton travail porte la mémoire du sacrifice. Tu dois maintenant apprendre à poser des limites saines, à discerner et à prendre soin de toi.",
        "Dis non à une demande d'aide pour préserver ton énergie.",
        "Respire en te donnant la permission d'avoir des limites.",
        "Comment mon sacrifice au travail détruit-il ma santé ? »"),

    ('pisces', 7): make_sn_interp('pisces', 7,
        "Tu arrives avec une maîtrise de l'amour inconditionnel — mais le sacrifice en couple te freine.",
        "Le Nœud Sud en Poissons dans ta maison VII indique une maîtrise karmique de la compassion relationnelle. Tu sais aimer sans limites et pardonner infiniment.",
        "Le sacrifice peut te piéger. Ta tendance à te perdre dans l'autre te coupe de ta propre identité et de tes besoins.",
        "Tes relations portent la mémoire de la fusion sacrificielle. Tu dois maintenant apprendre à aimer avec discernement et à garder ton centre.",
        "Affirme un de tes besoins dans ta relation.",
        "Respire en te sentant entier même en couple.",
        "Comment mon sacrifice relationnel me détruit-il ? »"),

    ('pisces', 8): make_sn_interp('pisces', 8,
        "Tu arrives avec une maîtrise de la dissolution — mais la peur de la structure te freine.",
        "Le Nœud Sud en Poissons dans ta maison VIII indique une maîtrise karmique de la transcendance des limites. Tu sais te dissoudre et traverser les frontières.",
        "La peur de la structure peut te piéger. Ta tendance à tout dissoudre te coupe de la stabilité nécessaire à la vraie transformation.",
        "Tes transformations portent la mémoire de la dissolution. Tu dois maintenant apprendre à transformer avec discernement, à garder ce qui fonctionne.",
        "Transforme quelque chose tout en gardant une structure.",
        "Respire en trouvant l'équilibre entre dissolution et forme.",
        "Que dissous-je par habitude alors que cela mériterait d'être gardé ? »"),

    ('pisces', 9): make_sn_interp('pisces', 9,
        "Tu arrives avec une maîtrise de la spiritualité mystique — mais le flou te freine.",
        "Le Nœud Sud en Poissons dans ta maison IX indique une maîtrise karmique de la connexion au divin. Tu sais te fondre dans le tout et vivre l'unité.",
        "Le flou et le manque de discernement peuvent te piéger. Ta tendance à tout accepter te coupe de la sagesse discriminante.",
        "Ta spiritualité porte la mémoire de l'océan. Tu dois maintenant apprendre le discernement spirituel, l'analyse et la clarté.",
        "Analyse une croyance avec discernement au lieu de l'accepter sans question.",
        "Respire en clarifiant ta vision spirituelle.",
        "Comment mon manque de discernement spirituel me rend-il vulnérable ? »"),

    ('pisces', 10): make_sn_interp('pisces', 10,
        "Tu arrives avec une maîtrise de la vocation inspirée — mais le manque de structure te freine.",
        "Le Nœud Sud en Poissons dans ta maison X indique une maîtrise karmique de la carrière intuitive. Tu sais servir une vision et te sacrifier pour ta mission.",
        "Le manque de structure peut te piéger. Ta tendance à négliger les détails pratiques te coupe de la réussite concrète.",
        "Ta carrière porte la mémoire du rêveur. Tu dois maintenant apprendre à structurer ta vision, à planifier et à exécuter méthodiquement.",
        "Crée un plan concret pour un objectif de carrière.",
        "Respire en ancrant ta vision dans l'action structurée.",
        "Comment mon manque de structure sabote-t-il ma carrière ? »"),

    ('pisces', 11): make_sn_interp('pisces', 11,
        "Tu arrives avec une maîtrise des liens collectifs fusionnels — mais la perte de discernement te freine.",
        "Le Nœud Sud en Poissons dans ta maison XI indique une maîtrise karmique de la compassion collective. Tu sais te fondre dans les groupes et aimer l'humanité.",
        "La perte de discernement peut te piéger. Ta tendance à accepter tout le monde te coupe des amitiés vraies et saines.",
        "Tes amitiés portent la mémoire de l'océan. Tu dois maintenant apprendre à choisir tes amis avec discernement et à créer des liens spéciaux.",
        "Choisis consciemment un ami au lieu de t'ouvrir à tous.",
        "Respire en honorant ce qui rend chaque ami spécial.",
        "Comment mon amour universel me prive-t-il d'amitiés profondes ? »"),

    ('pisces', 12): make_sn_interp('pisces', 12,
        "Tu arrives avec une maîtrise de la dissolution mystique — mais la fuite te freine.",
        "Le Nœud Sud en Poissons dans ta maison XII (son domicile) indique une maîtrise karmique profonde de la transcendance. Tu sais te dissoudre dans l'infini et te connecter au tout.",
        "La fuite peut te piéger. Ta tendance à te perdre dans l'invisible te coupe de l'action dans le monde matériel.",
        "Ton monde intérieur porte la mémoire de la dissolution. Tu dois maintenant apprendre à agir concrètement, à servir visiblement, à incarner.",
        "Agis concrètement dans le monde au lieu de te retirer.",
        "Respire en ancrant ta spiritualité dans le service visible.",
        "Comment ma fuite spirituelle me coupe-t-elle de ma mission dans le monde ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in SOUTH_NODE_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'south_node',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP south_node/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='south_node',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT south_node/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
