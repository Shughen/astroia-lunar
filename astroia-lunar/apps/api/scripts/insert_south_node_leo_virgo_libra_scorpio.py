#!/usr/bin/env python3
"""Insert South Node interpretations for Leo, Virgo, Libra, Scorpio (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_sn_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'leo': '☋ Nœud Sud en Lion',
        'virgo': '☋ Nœud Sud en Vierge',
        'libra': '☋ Nœud Sud en Balance',
        'scorpio': '☋ Nœud Sud en Scorpion',
    }
    sign_fr = {
        'leo': 'Lion',
        'virgo': 'Vierge',
        'libra': 'Balance',
        'scorpio': 'Scorpion',
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
    # === LEO (M1-M12) ===
    ('leo', 1): make_sn_interp('leo', 1,
        "Tu arrives avec une maîtrise du charisme et de l'expression de soi — mais l'égo te freine.",
        "Le Nœud Sud en Lion dans ta maison I indique une maîtrise karmique de la présence royale. Tu sais briller, attirer l'attention et exprimer ton individualité avec force.",
        "L'égo et le besoin de reconnaissance peuvent te piéger. Ta tendance à vouloir être le centre de l'attention te coupe de la vraie connexion avec les autres.",
        "Ta présence porte la mémoire du roi. Tu dois maintenant apprendre à servir un groupe, une cause plus grande que toi, plutôt qu'à briller seul.",
        "Mets quelqu'un d'autre en lumière aujourd'hui.",
        "Respire en relâchant le besoin d'être vu et admiré.",
        "Comment mon besoin de briller m'isole-t-il des autres ? »"),

    ('leo', 2): make_sn_interp('leo', 2,
        "Tu arrives avec une maîtrise de l'abondance généreuse — mais l'orgueil financier te freine.",
        "Le Nœud Sud en Lion dans ta maison II indique une maîtrise karmique de la générosité royale. Tu sais créer l'abondance et la partager avec magnificence.",
        "L'orgueil autour de l'argent peut te piéger. Ta tendance à faire de tes possessions un symbole de statut te coupe de la vraie valeur.",
        "Tes ressources portent la mémoire de la richesse ostentatoire. Tu dois maintenant apprendre à valoriser ce qui n'a pas de prix et à partager sans attente.",
        "Donne sans en faire une démonstration.",
        "Respire en te sentant riche indépendamment de ce que tu possèdes.",
        "Où mon orgueil financier masque-t-il une insécurité profonde ? »"),

    ('leo', 3): make_sn_interp('leo', 3,
        "Tu arrives avec une maîtrise de l'expression dramatique — mais le monologue te freine.",
        "Le Nœud Sud en Lion dans ta maison III indique une maîtrise karmique de la parole théâtrale. Tu sais captiver par tes mots et commander l'attention.",
        "Le monologue et le besoin d'être entendu peuvent te piéger. Ta tendance à dominer les conversations te coupe du vrai échange.",
        "Ta communication porte la mémoire du roi qui proclame. Tu dois maintenant apprendre à écouter et à dialoguer d'égal à égal.",
        "Pose des questions au lieu de raconter.",
        "Respire en créant de l'espace pour la parole de l'autre.",
        "Quand est-ce que je parle pour briller plutôt que pour communiquer ? »"),

    ('leo', 4): make_sn_interp('leo', 4,
        "Tu arrives avec une maîtrise de la création d'un foyer royal — mais le besoin de contrôle familial te freine.",
        "Le Nœud Sud en Lion dans ta maison IV indique une maîtrise karmique de la souveraineté familiale. Tu sais régner sur ton foyer et créer un espace de prestige.",
        "Le besoin de contrôle familial peut te piéger. Ta tendance à dominer ton foyer te coupe de l'intimité égalitaire.",
        "Ton foyer porte la mémoire du palais. Tu dois maintenant apprendre à partager le pouvoir et à accueillir les besoins des autres.",
        "Laisse quelqu'un d'autre décider pour le foyer.",
        "Respire en relâchant le besoin de contrôler ton territoire.",
        "Comment mon besoin de régner à la maison affecte-t-il ma famille ? »"),

    ('leo', 5): make_sn_interp('leo', 5,
        "Tu arrives avec une maîtrise de la créativité glorieuse — mais le besoin de reconnaissance te freine.",
        "Le Nœud Sud en Lion dans ta maison V (son domicile) indique une maîtrise karmique profonde de l'expression créative. Tu sais briller par tes créations et tes amours.",
        "Le besoin de reconnaissance peut te piéger. Ta tendance à créer pour la gloire te coupe de la créativité pure et des amours authentiques.",
        "Ta créativité porte la mémoire de la scène. Tu dois maintenant apprendre à créer pour le collectif, pas pour ton ego.",
        "Crée quelque chose d'anonyme, sans signature.",
        "Respire en te sentant créatif même sans applaudissements.",
        "Combien de fois créé-je pour être admiré plutôt que pour le plaisir ? »"),

    ('leo', 6): make_sn_interp('leo', 6,
        "Tu arrives avec une maîtrise du leadership au travail — mais l'orgueil professionnel te freine.",
        "Le Nœud Sud en Lion dans ta maison VI indique une maîtrise karmique de l'autorité au quotidien. Tu sais diriger et inspirer dans le travail.",
        "L'orgueil et le refus des tâches « indignes » peuvent te piéger. Ta tendance à vouloir les beaux rôles te coupe de l'humilité nécessaire.",
        "Ton travail porte la mémoire du chef. Tu dois maintenant apprendre le service humble et la valeur des tâches simples.",
        "Accomplis une tâche humble sans te sentir diminué.",
        "Respire en trouvant la dignité dans le service simple.",
        "Quelles tâches considéré-je comme en-dessous de moi ? »"),

    ('leo', 7): make_sn_interp('leo', 7,
        "Tu arrives avec une maîtrise de l'amour passionné — mais le drame relationnel te freine.",
        "Le Nœud Sud en Lion dans ta maison VII indique une maîtrise karmique de l'amour romantique. Tu sais aimer avec passion et créer des relations intenses.",
        "Le drame et le besoin d'attention dans le couple peuvent te piéger. Ta tendance à faire de la relation un spectacle te coupe de l'intimité simple.",
        "Tes relations portent la mémoire de la passion théâtrale. Tu dois maintenant apprendre l'amour calme et l'égalité dans le partenariat.",
        "Aime simplement, sans drame ni mise en scène.",
        "Respire en appréciant les moments ordinaires de la relation.",
        "Quand créé-je du drame pour me sentir vivant en amour ? »"),

    ('leo', 8): make_sn_interp('leo', 8,
        "Tu arrives avec une maîtrise de la transformation héroïque — mais le contrôle des crises te freine.",
        "Le Nœud Sud en Lion dans ta maison VIII indique une maîtrise karmique de la gestion des crises avec panache. Tu sais traverser les épreuves comme un héros.",
        "Le besoin de contrôler les transformations peut te piéger. Ta tendance à vouloir diriger les crises te coupe de la surrender nécessaire.",
        "Tes transformations portent la mémoire du héros. Tu dois maintenant apprendre à te rendre, à lâcher prise et à laisser la vie te transformer.",
        "Abandonne le contrôle face à une situation de crise.",
        "Respire en acceptant de ne pas être le héros de ta transformation.",
        "Où mon besoin de contrôle m'empêche-t-il de me transformer vraiment ? »"),

    ('leo', 9): make_sn_interp('leo', 9,
        "Tu arrives avec une maîtrise de la proclamation de vérité — mais le dogmatisme glorieux te freine.",
        "Le Nœud Sud en Lion dans ta maison IX indique une maîtrise karmique de l'enseignement charismatique. Tu sais proclamer ta vérité et inspirer par tes croyances.",
        "Le dogmatisme et le besoin d'avoir raison peuvent te piéger. Ta tendance à prêcher te coupe de l'apprentissage humble.",
        "Ta spiritualité porte la mémoire du prophète. Tu dois maintenant apprendre à questionner tes croyances et à écouter d'autres vérités.",
        "Apprends de quelqu'un au lieu d'enseigner.",
        "Respire en relâchant le besoin d'avoir raison spirituellement.",
        "Quand mes croyances deviennent-elles des proclamations égotiques ? »"),

    ('leo', 10): make_sn_interp('leo', 10,
        "Tu arrives avec une maîtrise de la carrière glorieuse — mais le besoin de statut te freine.",
        "Le Nœud Sud en Lion dans ta maison X indique une maîtrise karmique de la réussite visible. Tu sais briller professionnellement et atteindre les sommets.",
        "Le besoin de statut et de reconnaissance peut te piéger. Ta tendance à chercher la gloire te coupe de la vraie contribution.",
        "Ta carrière porte la mémoire du roi au sommet. Tu dois maintenant apprendre à servir plutôt qu'à régner, à contribuer plutôt qu'à briller.",
        "Contribue au succès collectif sans chercher la reconnaissance personnelle.",
        "Respire en te sentant accompli indépendamment des applaudissements.",
        "Comment mon besoin de gloire limite-t-il ma vraie contribution ? »"),

    ('leo', 11): make_sn_interp('leo', 11,
        "Tu arrives avec une maîtrise du leadership de groupe — mais le besoin d'être admiré te freine.",
        "Le Nœud Sud en Lion dans ta maison XI indique une maîtrise karmique de l'inspiration collective. Tu sais galvaniser les groupes et inspirer les masses.",
        "Le besoin d'être admiré par le groupe peut te piéger. Ta tendance à vouloir être la star te coupe de l'amitié égalitaire.",
        "Tes amitiés portent la mémoire de la cour royale. Tu dois maintenant apprendre à être un membre égal, pas le roi du groupe.",
        "Participe à un groupe sans chercher à en être le leader.",
        "Respire en te sentant appartenir sans avoir besoin d'être spécial.",
        "Où mon besoin d'être admiré compromet-il mes amitiés ? »"),

    ('leo', 12): make_sn_interp('leo', 12,
        "Tu arrives avec une maîtrise de la gloire intérieure — mais l'égo spirituel te freine.",
        "Le Nœud Sud en Lion dans ta maison XII indique une maîtrise karmique de la connexion divine glorieuse. Tu sais te sentir spécial aux yeux de l'univers.",
        "L'égo spirituel peut te piéger. Ta tendance à te sentir spécial spirituellement te coupe de l'humilité nécessaire à la vraie dissolution.",
        "Ton monde intérieur porte la mémoire du roi spirituel. Tu dois maintenant apprendre à te dissoudre dans le tout, à abandonner toute prétention.",
        "Médite sur ton insignifiance face à l'infini.",
        "Respire en te sentant un parmi des milliards, égal à tous.",
        "Comment mon égo spirituel me sépare-t-il de l'unité ? »"),

    # === VIRGO (M1-M12) ===
    ('virgo', 1): make_sn_interp('virgo', 1,
        "Tu arrives avec une maîtrise de l'analyse et du perfectionnisme — mais l'autocritique te freine.",
        "Le Nœud Sud en Vierge dans ta maison I indique une maîtrise karmique de l'amélioration de soi. Tu sais te perfectionner, t'analyser et te corriger.",
        "L'autocritique et le perfectionnisme peuvent te piéger. Ta tendance à chercher la perfection te coupe de l'acceptation de toi-même.",
        "Ta présence porte la mémoire de l'analyse incessante. Tu dois maintenant apprendre à te faire confiance, à accueillir l'imperfection.",
        "Accepte-toi avec un défaut aujourd'hui, sans chercher à le corriger.",
        "Respire en relâchant le besoin d'être parfait.",
        "Comment mon perfectionnisme m'empêche-t-il de me montrer au monde ? »"),

    ('virgo', 2): make_sn_interp('virgo', 2,
        "Tu arrives avec une maîtrise de la gestion minutieuse des ressources — mais l'avarice te freine.",
        "Le Nœud Sud en Vierge dans ta maison II indique une maîtrise karmique de l'économie. Tu sais gérer tes ressources avec précision et éviter le gaspillage.",
        "L'avarice et l'excès de prudence peuvent te piéger. Ta tendance à tout contrôler te coupe de l'abondance et du partage.",
        "Tes finances portent la mémoire de la restriction. Tu dois maintenant apprendre à faire confiance à la vie et à partager généreusement.",
        "Dépense pour quelque chose de non-nécessaire, juste pour le plaisir.",
        "Respire en te sentant abondant au-delà de ce que tu possèdes.",
        "Comment ma prudence excessive me prive-t-elle de la richesse de la vie ? »"),

    ('virgo', 3): make_sn_interp('virgo', 3,
        "Tu arrives avec une maîtrise de la communication précise — mais l'excès de détails te freine.",
        "Le Nœud Sud en Vierge dans ta maison III indique une maîtrise karmique de l'analyse verbale. Tu sais communiquer avec précision et attention aux détails.",
        "L'excès de détails peut te piéger. Ta tendance à tout analyser te coupe de la vision d'ensemble et de la communication intuitive.",
        "Ta communication porte la mémoire de l'analyste. Tu dois maintenant apprendre à synthétiser, à voir la forêt au-delà des arbres.",
        "Communique une idée en une phrase, sans détails.",
        "Respire en laissant ton mental s'élargir vers la vue d'ensemble.",
        "Quand mes détails empêchent-ils mon message de passer ? »"),

    ('virgo', 4): make_sn_interp('virgo', 4,
        "Tu arrives avec une maîtrise de l'organisation du foyer — mais le contrôle domestique te freine.",
        "Le Nœud Sud en Vierge dans ta maison IV indique une maîtrise karmique de l'ordre domestique. Tu sais organiser ton foyer et maintenir une maison fonctionnelle.",
        "Le contrôle excessif peut te piéger. Ta tendance à tout ordonner te coupe de la chaleur et de la spontanéité du foyer.",
        "Ton foyer porte la mémoire de la perfection domestique. Tu dois maintenant apprendre à accueillir le désordre de la vie et la chaleur émotionnelle.",
        "Laisse un peu de désordre dans ta maison sans le corriger.",
        "Respire en accueillant l'imperfection de ton espace.",
        "Comment mon contrôle domestique refroidit-il l'atmosphère de mon foyer ? »"),

    ('virgo', 5): make_sn_interp('virgo', 5,
        "Tu arrives avec une maîtrise de la création minutieuse — mais le perfectionnisme créatif te freine.",
        "Le Nœud Sud en Vierge dans ta maison V indique une maîtrise karmique de la création technique. Tu sais perfectionner tes œuvres et analyser tes amours.",
        "Le perfectionnisme créatif peut te piéger. Ta tendance à critiquer ce que tu crées te coupe du plaisir de la création spontanée.",
        "Ta créativité porte la mémoire de l'analyse. Tu dois maintenant apprendre à créer avec abandon, sans chercher la perfection.",
        "Crée quelque chose d'imparfait et laisse-le tel quel.",
        "Respire en trouvant la beauté dans l'imperfection.",
        "Combien d'œuvres ai-je abandonnées parce qu'elles n'étaient pas parfaites ? »"),

    ('virgo', 6): make_sn_interp('virgo', 6,
        "Tu arrives avec une maîtrise du travail méticuleux — mais l'obsession du détail te freine.",
        "Le Nœud Sud en Vierge dans ta maison VI (son domicile) indique une maîtrise karmique profonde du service et du travail. Tu sais être efficace et utile.",
        "L'obsession du détail peut te piéger. Ta tendance à tout perfectionner te coupe de la vue d'ensemble et de la connexion spirituelle.",
        "Ton travail porte la mémoire du service perfectionniste. Tu dois maintenant apprendre à lâcher prise, à faire confiance et à te connecter au sens.",
        "Termine une tâche sans la perfectionner.",
        "Respire en relâchant le besoin de tout contrôler.",
        "Comment mon perfectionnisme au travail m'épuise-t-il ? »"),

    ('virgo', 7): make_sn_interp('virgo', 7,
        "Tu arrives avec une maîtrise de l'analyse des relations — mais la critique du partenaire te freine.",
        "Le Nœud Sud en Vierge dans ta maison VII indique une maîtrise karmique de l'amélioration relationnelle. Tu sais analyser et optimiser tes relations.",
        "La critique du partenaire peut te piéger. Ta tendance à voir les défauts de l'autre te coupe de l'amour inconditionnel.",
        "Tes relations portent la mémoire de l'analyse. Tu dois maintenant apprendre à accepter ton partenaire tel qu'il est, avec ses imperfections.",
        "Regarde ton partenaire sans chercher à le corriger.",
        "Respire en accueillant l'imperfection de l'autre.",
        "Comment mes critiques dégradent-elles mes relations ? »"),

    ('virgo', 8): make_sn_interp('virgo', 8,
        "Tu arrives avec une maîtrise de l'analyse des crises — mais le contrôle des transformations te freine.",
        "Le Nœud Sud en Vierge dans ta maison VIII indique une maîtrise karmique de la gestion analytique des crises. Tu sais disséquer et comprendre les processus de transformation.",
        "Le contrôle analytique peut te piéger. Ta tendance à tout comprendre te coupe de l'abandon nécessaire à la vraie métamorphose.",
        "Tes transformations portent la mémoire de l'analyse. Tu dois maintenant apprendre à te transformer sans comprendre, à faire confiance au processus.",
        "Traverse une émotion intense sans l'analyser.",
        "Respire en lâchant le besoin de comprendre ta transformation.",
        "Quand mon mental m'empêche-t-il de me transformer vraiment ? »"),

    ('virgo', 9): make_sn_interp('virgo', 9,
        "Tu arrives avec une maîtrise de l'étude des traditions — mais le scepticisme te freine.",
        "Le Nœud Sud en Vierge dans ta maison IX indique une maîtrise karmique de l'analyse spirituelle. Tu sais étudier les traditions et comprendre les philosophies.",
        "Le scepticisme et l'excès d'analyse peuvent te piéger. Ta tendance à critiquer les croyances te coupe de la foi et de l'inspiration.",
        "Ta spiritualité porte la mémoire de l'analyse. Tu dois maintenant apprendre la foi, la confiance et l'ouverture à l'inconnu.",
        "Accepte une croyance sans la disséquer.",
        "Respire en ouvrant ton cœur à l'inexplicable.",
        "Comment mon scepticisme me ferme-t-il à la transcendance ? »"),

    ('virgo', 10): make_sn_interp('virgo', 10,
        "Tu arrives avec une maîtrise de la carrière technique — mais le perfectionnisme te freine.",
        "Le Nœud Sud en Vierge dans ta maison X indique une maîtrise karmique de l'excellence professionnelle. Tu sais produire un travail de qualité.",
        "Le perfectionnisme peut te piéger. Ta tendance à viser l'impossible te coupe de la satisfaction et de la vision.",
        "Ta carrière porte la mémoire du technicien parfait. Tu dois maintenant apprendre à viser l'inspiration plutôt que la perfection.",
        "Accepte un travail « suffisamment bon » au lieu de parfait.",
        "Respire en relâchant l'anxiété de performance.",
        "Comment mon perfectionnisme m'empêche-t-il de prendre des risques de carrière ? »"),

    ('virgo', 11): make_sn_interp('virgo', 11,
        "Tu arrives avec une maîtrise de l'amélioration des groupes — mais la critique des amis te freine.",
        "Le Nœud Sud en Vierge dans ta maison XI indique une maîtrise karmique du service au groupe. Tu sais être utile et améliorer les dynamiques collectives.",
        "La critique peut te piéger. Ta tendance à voir les défauts des autres et du groupe te coupe de l'amitié inconditionnelle.",
        "Tes amitiés portent la mémoire du correcteur. Tu dois maintenant apprendre à accepter tes amis et les groupes tels qu'ils sont.",
        "Apprécie un ami sans chercher à l'améliorer.",
        "Respire en voyant la beauté dans les imperfections du collectif.",
        "Comment mes critiques affectent-elles mes amitiés ? »"),

    ('virgo', 12): make_sn_interp('virgo', 12,
        "Tu arrives avec une maîtrise de l'analyse de l'inconscient — mais le mental intrusif te freine.",
        "Le Nœud Sud en Vierge dans ta maison XII indique une maîtrise karmique de l'auto-analyse. Tu sais explorer ton inconscient et comprendre tes schémas.",
        "L'analyse excessive peut te piéger. Ta tendance à tout disséquer te coupe de la paix intérieure et de la dissolution mystique.",
        "Ton monde intérieur porte la mémoire de l'analyste. Tu dois maintenant apprendre le silence, la méditation et l'abandon total.",
        "Médite sans analyser ce qui se passe.",
        "Respire en laissant ton mental se dissoudre dans le silence.",
        "Comment mon mental m'empêche-t-il de trouver la paix ? »"),

    # === LIBRA (M1-M12) ===
    ('libra', 1): make_sn_interp('libra', 1,
        "Tu arrives avec une maîtrise de l'harmonie et de la diplomatie — mais la peur du conflit te freine.",
        "Le Nœud Sud en Balance dans ta maison I indique une maîtrise karmique de l'élégance relationnelle. Tu sais créer l'harmonie et plaire aux autres.",
        "La peur du conflit peut te piéger. Ta tendance à éviter les confrontations te coupe de ta propre vérité et de ton affirmation.",
        "Ta présence porte la mémoire du diplomate. Tu dois maintenant apprendre à t'affirmer, même si cela déplaît, à oser le conflit sain.",
        "Affirme une opinion impopulaire.",
        "Respire en te sentant entier même dans le désaccord.",
        "Où évité-je le conflit au prix de ma propre vérité ? »"),

    ('libra', 2): make_sn_interp('libra', 2,
        "Tu arrives avec une maîtrise du partage des ressources — mais la dépendance financière te freine.",
        "Le Nœud Sud en Balance dans ta maison II indique une maîtrise karmique de la coopération financière. Tu sais partager et créer des partenariats de ressources.",
        "La dépendance aux autres pour les ressources peut te piéger. Ta tendance à t'appuyer sur les autres te coupe de ta propre autonomie financière.",
        "Tes finances portent la mémoire du partage. Tu dois maintenant apprendre à créer ta propre sécurité, indépendamment des autres.",
        "Gagne ou crée quelque chose par toi-même.",
        "Respire en te sentant financièrement autonome.",
        "Comment ma dépendance financière aux autres limite-t-elle ma liberté ? »"),

    ('libra', 3): make_sn_interp('libra', 3,
        "Tu arrives avec une maîtrise de la communication diplomatique — mais l'évitement de la vérité te freine.",
        "Le Nœud Sud en Balance dans ta maison III indique une maîtrise karmique de l'échange harmonieux. Tu sais communiquer avec grâce et maintenir la paix verbale.",
        "L'évitement de la vérité peut te piéger. Ta tendance à dire ce que l'autre veut entendre te coupe de l'authenticité.",
        "Ta communication porte la mémoire du diplomate. Tu dois maintenant apprendre à dire ta vérité, même si elle dérange.",
        "Dis une vérité que tu évitais pour maintenir la paix.",
        "Respire en te sentant courageux dans tes paroles.",
        "Quand est-ce que j'adoucis la vérité au point de la perdre ? »"),

    ('libra', 4): make_sn_interp('libra', 4,
        "Tu arrives avec une maîtrise de l'harmonie familiale — mais l'évitement des conflits domestiques te freine.",
        "Le Nœud Sud en Balance dans ta maison IV indique une maîtrise karmique de la paix au foyer. Tu sais créer un espace harmonieux et esthétique.",
        "L'évitement des conflits peut te piéger. Ta tendance à maintenir une fausse paix te coupe de l'authenticité familiale.",
        "Ton foyer porte la mémoire de la façade harmonieuse. Tu dois maintenant apprendre à exprimer les tensions et à bâtir une vraie paix.",
        "Exprime un désaccord familial que tu évitais.",
        "Respire en acceptant que le conflit sain renforce les liens.",
        "Quelles tensions familiales évité-je au prix de l'authenticité ? »"),

    ('libra', 5): make_sn_interp('libra', 5,
        "Tu arrives avec une maîtrise de la création esthétique — mais le besoin d'approbation te freine.",
        "Le Nœud Sud en Balance dans ta maison V indique une maîtrise karmique de l'art de plaire. Tu sais créer de la beauté et charmer dans l'amour.",
        "Le besoin d'approbation peut te piéger. Ta tendance à créer pour plaire te coupe de ton expression authentique.",
        "Ta créativité porte la mémoire de la séduction. Tu dois maintenant apprendre à créer pour toi-même, sans chercher l'approbation.",
        "Crée quelque chose qui te plaît à toi, même si ça déplaît aux autres.",
        "Respire en validant ta propre créativité.",
        "Combien de mes créations sont faites pour plaire plutôt que pour m'exprimer ? »"),

    ('libra', 6): make_sn_interp('libra', 6,
        "Tu arrives avec une maîtrise de la coopération au travail — mais l'effacement professionnel te freine.",
        "Le Nœud Sud en Balance dans ta maison VI indique une maîtrise karmique du travail en équipe. Tu sais coopérer et maintenir l'harmonie professionnelle.",
        "L'effacement peut te piéger. Ta tendance à privilégier la paix au travail te coupe de ton affirmation professionnelle.",
        "Ton travail porte la mémoire du médiateur. Tu dois maintenant apprendre à prendre position et à défendre tes idées.",
        "Défends une position au travail sans chercher à plaire à tous.",
        "Respire en te sentant légitime dans ton autorité.",
        "Où m'efface-je au travail pour maintenir la paix ? »"),

    ('libra', 7): make_sn_interp('libra', 7,
        "Tu arrives avec une maîtrise des relations harmonieuses — mais la perte de soi dans le couple te freine.",
        "Le Nœud Sud en Balance dans ta maison VII (son domicile) indique une maîtrise karmique profonde du partenariat. Tu sais créer des relations élégantes et équilibrées.",
        "La perte de soi peut te piéger. Ta tendance à te fondre dans l'autre te coupe de ta propre identité.",
        "Tes relations portent la mémoire de la fusion élégante. Tu dois maintenant apprendre à rester toi-même tout en étant en couple.",
        "Affirme un besoin personnel même s'il diffère de celui de ton partenaire.",
        "Respire en ressentant ton identité distincte de ta relation.",
        "Comment me suis-je perdu(e) dans mes relations ? »"),

    ('libra', 8): make_sn_interp('libra', 8,
        "Tu arrives avec une maîtrise de la transformation en douceur — mais l'évitement de l'intensité te freine.",
        "Le Nœud Sud en Balance dans ta maison VIII indique une maîtrise karmique de la gestion élégante des crises. Tu sais traverser les transformations avec grâce.",
        "L'évitement de l'intensité peut te piéger. Ta tendance à adoucir les crises te coupe de la transformation profonde.",
        "Tes transformations portent la mémoire de la surface. Tu dois maintenant apprendre à plonger dans l'intensité sans la fuir.",
        "Affronte une émotion intense au lieu de la polir.",
        "Respire en accueillant l'inconfort de la transformation.",
        "Quelles transformations évité-je parce qu'elles ne sont pas « élégantes » ? »"),

    ('libra', 9): make_sn_interp('libra', 9,
        "Tu arrives avec une maîtrise de l'ouverture d'esprit — mais l'indécision philosophique te freine.",
        "Le Nœud Sud en Balance dans ta maison IX indique une maîtrise karmique de la tolérance. Tu sais voir tous les points de vue et respecter toutes les croyances.",
        "L'indécision peut te piéger. Ta tendance à tout relativiser te coupe de tes propres convictions.",
        "Ta spiritualité porte la mémoire du relativisme. Tu dois maintenant apprendre à choisir ta vérité et à la défendre.",
        "Prends position sur une question philosophique importante.",
        "Respire en te sentant ancré dans tes propres croyances.",
        "Quand mon ouverture d'esprit devient-elle de l'indécision ? »"),

    ('libra', 10): make_sn_interp('libra', 10,
        "Tu arrives avec une maîtrise de la diplomatie professionnelle — mais le compromis excessif te freine.",
        "Le Nœud Sud en Balance dans ta maison X indique une maîtrise karmique de l'image publique. Tu sais plaire et maintenir de bonnes relations professionnelles.",
        "Le compromis excessif peut te piéger. Ta tendance à plaire à tous te coupe de ta vraie mission et de ton autorité.",
        "Ta carrière porte la mémoire du diplomate. Tu dois maintenant apprendre à diriger, à trancher et à assumer l'impopularité si nécessaire.",
        "Prends une décision de carrière impopulaire mais juste.",
        "Respire en assumant ton autorité même si elle déplaît.",
        "Quels compromis de carrière ai-je faits au détriment de ma vérité ? »"),

    ('libra', 11): make_sn_interp('libra', 11,
        "Tu arrives avec une maîtrise de l'harmonie de groupe — mais la perte de soi dans le collectif te freine.",
        "Le Nœud Sud en Balance dans ta maison XI indique une maîtrise karmique de la création de paix sociale. Tu sais harmoniser les groupes et créer des amitiés plaisantes.",
        "La perte de soi peut te piéger. Ta tendance à te fondre dans le groupe te coupe de ton expression individuelle.",
        "Tes amitiés portent la mémoire du caméléon social. Tu dois maintenant apprendre à briller individuellement tout en restant connecté.",
        "Affirme ton unicité dans un groupe.",
        "Respire en te sentant différent et accepté.",
        "Comment me perds-je dans les dynamiques de groupe ? »"),

    ('libra', 12): make_sn_interp('libra', 12,
        "Tu arrives avec une maîtrise de la paix intérieure — mais la fuite dans l'harmonie te freine.",
        "Le Nœud Sud en Balance dans ta maison XII indique une maîtrise karmique de l'équilibre intérieur. Tu sais trouver la paix et éviter les turbulences.",
        "La fuite dans l'harmonie peut te piéger. Ta tendance à éviter l'inconfort te coupe des transformations profondes.",
        "Ton monde intérieur porte la mémoire de la surface paisible. Tu dois maintenant apprendre à affronter les profondeurs, même inconfortables.",
        "Explore une zone d'ombre que tu évitais.",
        "Respire en acceptant l'inconfort comme chemin de croissance.",
        "Quelle turbulence intérieure évité-je au nom de la paix ? »"),

    # === SCORPIO (M1-M12) ===
    ('scorpio', 1): make_sn_interp('scorpio', 1,
        "Tu arrives avec une maîtrise de l'intensité et du pouvoir — mais la méfiance te freine.",
        "Le Nœud Sud en Scorpion dans ta maison I indique une maîtrise karmique de la survie et de la transformation. Tu sais naviguer les profondeurs et exercer un pouvoir magnétique.",
        "La méfiance et le contrôle peuvent te piéger. Ta tendance à te protéger et à manipuler te coupe de la simplicité et de la confiance.",
        "Ta présence porte la mémoire du survivant. Tu dois maintenant apprendre la légèreté, la confiance et la simplicité dans ton rapport au monde.",
        "Fais confiance à quelqu'un sans chercher ses motivations cachées.",
        "Respire en relâchant le besoin de te protéger.",
        "Où ma méfiance m'empêche-t-elle de vivre simplement ? »"),

    ('scorpio', 2): make_sn_interp('scorpio', 2,
        "Tu arrives avec une maîtrise du pouvoir financier — mais l'obsession des ressources te freine.",
        "Le Nœud Sud en Scorpion dans ta maison II indique une maîtrise karmique de la transformation des ressources. Tu sais accumuler du pouvoir à travers la matière.",
        "L'obsession et le contrôle financier peuvent te piéger. Ta tendance à tout transformer en jeu de pouvoir te coupe de la simplicité matérielle.",
        "Tes finances portent la mémoire du contrôle. Tu dois maintenant apprendre à valoriser la simplicité et à partager sans stratégie.",
        "Dépense ou donne sans calcul stratégique.",
        "Respire en relâchant le besoin de contrôler tes ressources.",
        "Comment mon obsession financière me complique-t-elle la vie ? »"),

    ('scorpio', 3): make_sn_interp('scorpio', 3,
        "Tu arrives avec une maîtrise de la communication pénétrante — mais la manipulation verbale te freine.",
        "Le Nœud Sud en Scorpion dans ta maison III indique une maîtrise karmique de la parole puissante. Tu sais toucher les points sensibles et révéler les non-dits.",
        "La manipulation et l'intensité verbale peuvent te piéger. Ta tendance à utiliser les mots comme des armes te coupe de la légèreté de l'échange.",
        "Ta communication porte la mémoire du détective. Tu dois maintenant apprendre la conversation simple, sans agenda caché.",
        "Parle de quelque chose de léger, sans profondeur.",
        "Respire en laissant ta communication devenir simple et directe.",
        "Quand est-ce que ma communication devient manipulation ? »"),

    ('scorpio', 4): make_sn_interp('scorpio', 4,
        "Tu arrives avec une maîtrise des secrets familiaux — mais les drames enfouis te freinent.",
        "Le Nœud Sud en Scorpion dans ta maison IV indique une maîtrise karmique de la gestion des ombres familiales. Tu sais naviguer les profondeurs psychologiques du foyer.",
        "Les drames et les secrets peuvent te piéger. Ta tendance à fouiller les ombres te coupe de la stabilité et de la paix domestique.",
        "Ton foyer porte la mémoire des crises. Tu dois maintenant apprendre à créer un foyer simple, stable et ouvert.",
        "Crée un moment de légèreté au foyer au lieu de profondeur.",
        "Respire en laissant ton foyer devenir un lieu de paix simple.",
        "Quels drames familiaux perpétué-je inconsciemment ? »"),

    ('scorpio', 5): make_sn_interp('scorpio', 5,
        "Tu arrives avec une maîtrise de la passion intense — mais les amours destructrices te freinent.",
        "Le Nœud Sud en Scorpion dans ta maison V indique une maîtrise karmique de la création intense. Tu sais créer et aimer avec passion et profondeur.",
        "L'intensité destructrice peut te piéger. Ta tendance aux amours obsessionnels et aux créations tourmentées te coupe de la joie simple.",
        "Ta créativité porte la mémoire de l'intensité. Tu dois maintenant apprendre à créer et aimer avec légèreté et joie.",
        "Crée ou aime quelque chose de léger et joyeux.",
        "Respire en accueillant la joie simple sans drame.",
        "Comment mon besoin d'intensité me prive-t-il de la joie ? »"),

    ('scorpio', 6): make_sn_interp('scorpio', 6,
        "Tu arrives avec une maîtrise du travail en profondeur — mais l'obsession te freine.",
        "Le Nœud Sud en Scorpion dans ta maison VI indique une maîtrise karmique du travail transformateur. Tu sais plonger dans les tâches et tout transformer.",
        "L'obsession au travail peut te piéger. Ta tendance à tout rendre intense te coupe de l'efficacité simple.",
        "Ton travail porte la mémoire de la transformation. Tu dois maintenant apprendre la routine paisible et le service simple.",
        "Accomplis une tâche de façon simple sans la transformer.",
        "Respire en laissant ton travail devenir léger.",
        "Comment mon intensité au travail m'épuise-t-elle ? »"),

    ('scorpio', 7): make_sn_interp('scorpio', 7,
        "Tu arrives avec une maîtrise des relations intenses — mais les jeux de pouvoir te freinent.",
        "Le Nœud Sud en Scorpion dans ta maison VII indique une maîtrise karmique du partenariat passionné. Tu sais créer des liens profonds et fusionnels.",
        "Les jeux de pouvoir peuvent te piéger. Ta tendance à la fusion et au contrôle te coupe du partenariat équilibré.",
        "Tes relations portent la mémoire de l'intensité. Tu dois maintenant apprendre le partenariat léger, la confiance et l'équilibre.",
        "Vis un moment simple avec un partenaire sans intensité.",
        "Respire en relâchant le besoin de contrôler la relation.",
        "Où mes jeux de pouvoir détruisent-ils mes relations ? »"),

    ('scorpio', 8): make_sn_interp('scorpio', 8,
        "Tu arrives avec une maîtrise de la transformation profonde — mais l'attachement aux crises te freine.",
        "Le Nœud Sud en Scorpion dans ta maison VIII (son domicile) indique une maîtrise karmique profonde des processus de mort et renaissance. Tu sais naviguer les abîmes.",
        "L'attachement aux crises peut te piéger. Ta tendance à créer du drame te coupe de la stabilité et de la paix.",
        "Tes transformations portent la mémoire de l'intensité. Tu dois maintenant apprendre à évoluer en douceur, sans crise.",
        "Transforme-toi doucement au lieu de forcer une crise.",
        "Respire en accueillant le changement sans drame.",
        "Quelles crises créé-je inconsciemment pour me sentir vivant ? »"),

    ('scorpio', 9): make_sn_interp('scorpio', 9,
        "Tu arrives avec une maîtrise des vérités occultes — mais le fanatisme te freine.",
        "Le Nœud Sud en Scorpion dans ta maison IX indique une maîtrise karmique de la quête des mystères. Tu sais explorer les profondeurs spirituelles et révéler ce qui est caché.",
        "Le fanatisme et l'obsession de vérité peuvent te piéger. Ta tendance à tout déconstruire te coupe de la foi simple.",
        "Ta spiritualité porte la mémoire du chercheur d'abîmes. Tu dois maintenant apprendre la sagesse pratique et la foi simple.",
        "Accepte une croyance simple sans la déconstruire.",
        "Respire en trouvant la sagesse dans la simplicité.",
        "Comment mon obsession de vérité me complique-t-elle la vie ? »"),

    ('scorpio', 10): make_sn_interp('scorpio', 10,
        "Tu arrives avec une maîtrise du pouvoir professionnel — mais les manipulations de carrière te freinent.",
        "Le Nœud Sud en Scorpion dans ta maison X indique une maîtrise karmique de la stratégie de carrière. Tu sais exercer le pouvoir et naviguer les politiques.",
        "Les manipulations peuvent te piéger. Ta tendance à jouer les jeux de pouvoir te coupe de la réussite authentique.",
        "Ta carrière porte la mémoire du stratège. Tu dois maintenant apprendre à bâtir simplement, avec intégrité et transparence.",
        "Agis professionnellement avec transparence totale.",
        "Respire en relâchant le besoin de contrôler ta carrière.",
        "Quelles manipulations de carrière me coûtent-elles plus qu'elles ne me rapportent ? »"),

    ('scorpio', 11): make_sn_interp('scorpio', 11,
        "Tu arrives avec une maîtrise des liens de groupe intenses — mais les dynamiques toxiques te freinent.",
        "Le Nœud Sud en Scorpion dans ta maison XI indique une maîtrise karmique des connexions profondes. Tu sais créer des liens puissants et transformer les groupes.",
        "Les dynamiques toxiques peuvent te piéger. Ta tendance à l'intensité groupale te coupe de l'amitié légère et saine.",
        "Tes amitiés portent la mémoire de l'intensité. Tu dois maintenant apprendre l'amitié simple, sans drame ni profondeur obligatoire.",
        "Apprécie un ami sans chercher la profondeur.",
        "Respire en laissant tes amitiés devenir légères.",
        "Quelles amitiés ai-je rendues toxiques par trop d'intensité ? »"),

    ('scorpio', 12): make_sn_interp('scorpio', 12,
        "Tu arrives avec une maîtrise des profondeurs psychiques — mais l'obsession de l'ombre te freine.",
        "Le Nœud Sud en Scorpion dans ta maison XII indique une maîtrise karmique de l'exploration des abîmes. Tu sais naviguer l'inconscient et affronter les démons.",
        "L'obsession de l'ombre peut te piéger. Ta tendance à fouiller sans cesse les profondeurs te coupe de la lumière et de la paix.",
        "Ton monde intérieur porte la mémoire des ténèbres. Tu dois maintenant apprendre à émerger vers la lumière et à servir concrètement.",
        "Passe du temps dans la lumière, au service des autres.",
        "Respire en montant vers la clarté au lieu de descendre dans l'ombre.",
        "Comment mon obsession des profondeurs me garde-t-elle dans l'obscurité ? »"),
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
