#!/usr/bin/env python3
"""Script d'insertion des interprétations Neptune/Leo, Virgo, Libra, Scorpio en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_neptune_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'leo': '♆ Neptune en Lion', 'virgo': '♆ Neptune en Vierge',
        'libra': '♆ Neptune en Balance', 'scorpio': '♆ Neptune en Scorpion'
    }
    return f"""# {sign_titles[sign_name]}
**En une phrase :** {phrase}

## Ton moteur
{moteur}

## Ton défi
{defi}

## Maison {house} en {sign_name.capitalize()}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

NEPTUNE_INTERPRETATIONS = {
    # LEO - 12 maisons
    ('leo', 1): make_neptune_interp('leo', 1,
        "Tu incarnes un rêve de grandeur — ton identité cherche à fusionner créativité et spiritualité.",
        "Neptune en Lion en Maison 1 te donne une personnalité qui rêve de briller de façon transcendante. Tu veux que ton expression personnelle touche les âmes, pas seulement les yeux.",
        "Le piège : un ego qui rêve de gloire spirituelle, confondre charisme et éveil, chercher l'adoration au nom de l'inspiration. La vraie créativité transcendante sert plutôt qu'elle n'éblouit.",
        "Neptune adoucit et spiritualise ton besoin d'expression. Tu projettes une image de créativité mystique. Ton apparence peut refléter tes rêves de grandeur.",
        "Exprimer ta créativité au service de quelque chose de plus grand",
        "Trois respirations en alignant ego et service",
        "Comment ma créativité peut-elle toucher les âmes plutôt que chercher l'admiration ?"),

    ('leo', 2): make_neptune_interp('leo', 2,
        "Tu rêves d'une prospérité créative — tes ressources viennent quand tu partages ta lumière généreusement.",
        "Neptune en Lion en Maison 2 crée une relation généreuse à l'argent. Tu veux que tes revenus viennent de ta créativité et servent à illuminer le monde.",
        "Le piège : être trop généreux au point de t'appauvrir, confondre valeur et reconnaissance, des finances floues par excès de grandeur. La vraie prospérité créative a aussi des bases solides.",
        "Neptune spiritualise ta relation aux ressources créatives. Tu peux gagner de l'argent par des talents artistiques. Tes valeurs sont liées à la générosité et à l'expression.",
        "Identifier comment ta créativité peut créer de la valeur durable",
        "Trois respirations en équilibrant générosité et stabilité",
        "Comment ma lumière créative peut-elle générer une prospérité durable ?"),

    ('leo', 3): make_neptune_interp('leo', 3,
        "Tu communiques avec éclat et inspiration — tes mots illuminent et élèvent ceux qui t'écoutent.",
        "Neptune en Lion en Maison 3 te donne une communication qui inspire et élève. Tu sais présenter les idées de façon à toucher le cœur et l'imagination.",
        "Le piège : une communication qui exagère, vouloir briller plutôt qu'éclairer, confondre performance et partage. La vraie communication inspirante est aussi authentique.",
        "Neptune spiritualise tes échanges de créativité et de chaleur. Tes relations peuvent être théâtrales mais aussi profondément inspirantes.",
        "Communiquer pour éclairer plutôt que pour briller",
        "Trois respirations en servant par les mots",
        "Comment ma communication peut-elle illuminer sans chercher l'admiration ?"),

    ('leo', 4): make_neptune_interp('leo', 4,
        "Tu rêves d'un foyer rayonnant — ta maison devient une scène où chacun peut briller et être célébré.",
        "Neptune en Lion en Maison 4 crée un environnement familial créatif et célébratoire. Ton foyer peut être un lieu de spectacle, d'art, de joie partagée.",
        "Le piège : un foyer où l'ego domine, des drames familiaux pour l'attention, confondre célébration et exhibition. La vraie maison rayonnante honore chaque membre.",
        "Neptune spiritualise ta vie familiale de créativité et de chaleur. Tu as peut-être grandi dans un environnement artistique ou créatif.",
        "Créer un moment où chaque membre de ta famille peut briller",
        "Trois respirations en célébrant les autres autant que toi",
        "Comment mon foyer peut-il célébrer chaque personne également ?"),

    ('leo', 5): make_neptune_interp('leo', 5,
        "Tu crées avec une vision transcendante — tes œuvres et tes amours sont des célébrations de la beauté divine.",
        "Neptune en Lion en Maison 5 amplifie au maximum ta créativité spirituelle. Tu veux que tes œuvres touchent l'âme, que tes amours soient des connexions transcendantes.",
        "Le piège : idéaliser les partenaires ou les œuvres, une créativité qui rêve sans concrétiser, confondre romance et illusion. La vraie joie créative s'incarne aussi.",
        "Neptune spiritualise au maximum tes plaisirs et ta créativité. Tu peux avoir des amours très inspirantes mais qui demandent un ancrage dans la réalité.",
        "Concrétiser une création qui te tient à cœur",
        "Trois respirations en incarnant ton rêve créatif",
        "Comment ma créativité peut-elle toucher le divin tout en s'incarnant ?"),

    ('leo', 6): make_neptune_interp('leo', 6,
        "Tu travailles avec une vision créative — ton quotidien devient une expression de beauté et de service.",
        "Neptune en Lion en Maison 6 te pousse vers un travail qui allie créativité et service. Tu veux que ton quotidien soit une œuvre d'art qui sert les autres.",
        "Le piège : un travail qui cherche la reconnaissance plutôt que le service, fuir les tâches ordinaires, confondre inspiration et efficacité. Le vrai travail créatif inclut aussi l'ordinaire.",
        "Neptune spiritualise ton quotidien de créativité. Tu travailles mieux quand tu peux apporter ta touche personnelle. Ta santé peut être sensible à ton expression créative.",
        "Trouver de la beauté dans une tâche ordinaire",
        "Trois respirations en servant par la créativité",
        "Comment mon travail peut-il être créatif ET utile ?"),

    ('leo', 7): make_neptune_interp('leo', 7,
        "Tu rêves de partenariats lumineux — tes relations sont des célébrations de deux créativités qui s'unissent.",
        "Neptune en Lion en Maison 7 crée des relations basées sur l'admiration mutuelle et la créativité partagée. Tu attires des partenaires avec qui tu veux créer quelque chose de beau.",
        "Le piège : idéaliser les partenaires, des relations qui deviennent des compétitions d'ego, confondre admiration et amour. Les meilleures relations célèbrent deux lumières sans compétition.",
        "Neptune spiritualise tes partenariats de créativité et de chaleur. Tu peux avoir des relations très inspirantes mais qui demandent de l'humilité.",
        "Célébrer ton partenaire sans te comparer",
        "Trois respirations en partageant la lumière",
        "Comment mes relations peuvent-elles célébrer deux lumières sans compétition ?"),

    ('leo', 8): make_neptune_interp('leo', 8,
        "Tu traverses les crises comme des renaissances créatives — les transformations révèlent ta lumière intérieure.",
        "Neptune en Lion en Maison 8 te donne la capacité de trouver de la beauté et du sens dans les crises. Les transformations deviennent des occasions de briller différemment.",
        "Le piège : dramatiser les crises pour l'attention, avoir du mal avec les transformations qui diminuent ton éclat, fuir les profondeurs. La vraie renaissance créative traverse aussi l'ombre.",
        "Neptune spiritualise ta relation aux crises de façon créative. Tu peux avoir des transformations qui révèlent de nouveaux talents. Ta sexualité peut être très expressive.",
        "Accueillir une transformation sans la dramatiser",
        "Trois respirations en trouvant la lumière dans l'ombre",
        "Quelle lumière nouvelle émerge de mes crises ?"),

    ('leo', 9): make_neptune_interp('leo', 9,
        "Tu rêves d'une sagesse rayonnante — ta philosophie célèbre la créativité comme voie d'éveil.",
        "Neptune en Lion en Maison 9 te pousse vers des croyances qui célèbrent la créativité et l'expression comme voies spirituelles. Ta spiritualité est joyeuse et expressive.",
        "Le piège : une spiritualité égotique, confondre charisme et sagesse, imposer ta vision de façon théâtrale. La vraie sagesse rayonnante éclaire sans éblouir.",
        "Neptune spiritualise ta quête de sens de créativité et d'expression. Tu peux être attiré par des spiritualités qui valorisent l'art et l'expression personnelle.",
        "Explorer une sagesse qui célèbre sans idolâtrer",
        "Trois respirations en servant la lumière",
        "Comment ma spiritualité peut-elle rayonner sans dominer ?"),

    ('leo', 10): make_neptune_interp('leo', 10,
        "Tu rêves d'une carrière inspirante — ta réussite vient quand tu illumines les autres par ta créativité.",
        "Neptune en Lion en Maison 10 te pousse vers une carrière créative qui inspire et élève. Tu veux que ta réussite touche les âmes et laisse une trace de beauté.",
        "Le piège : une carrière qui cherche la gloire plutôt que le service, confondre réputation et impact, des ambitions floues par excès de rêve. La vraie réussite inspirante est aussi concrète.",
        "Neptune spiritualise ta carrière et ta réputation de créativité. On te reconnaît pour ta capacité à inspirer. Ta carrière peut être dans les arts ou l'inspiration.",
        "Identifier comment ta carrière peut servir plutôt que briller",
        "Trois respirations en alignant créativité et service",
        "Comment ma carrière peut-elle inspirer durablement ?"),

    ('leo', 11): make_neptune_interp('leo', 11,
        "Tu rêves de communautés créatives — tes amitiés et tes projets sont des célébrations collectives de la beauté.",
        "Neptune en Lion en Maison 11 te connecte à des réseaux de personnes créatives et inspirantes. Tes amis partagent ta passion pour l'expression et la beauté. Les projets collectifs sont des célébrations.",
        "Le piège : vouloir être la star du groupe, des projets qui célèbrent l'ego plutôt que le collectif, confondre popularité et communauté. Les meilleures communautés honorent chaque membre.",
        "Neptune spiritualise tes réseaux et tes projets de créativité collective. Tu es fait pour les collectifs artistiques, les associations culturelles.",
        "Célébrer la créativité d'un ami plutôt que la tienne",
        "Trois respirations en partageant la scène collective",
        "Comment mes réseaux peuvent-ils célébrer chaque créativité ?"),

    ('leo', 12): make_neptune_interp('leo', 12,
        "Tu rêves d'une lumière intérieure — ton inconscient est une source de créativité spirituelle profonde.",
        "Neptune en Lion en Maison 12 crée des connexions entre ta créativité et les dimensions invisibles. Tes rêves peuvent être spectaculaires et inspirants. Ton inconscient est un théâtre de l'âme.",
        "Le piège : un ego spirituel qui cherche la reconnaissance, confondre visions et illusions de grandeur, fuir dans des rêves de gloire. La vraie créativité intérieure n'a pas besoin de public.",
        "Neptune spiritualise au maximum ta connexion à la créativité invisible. Tu peux avoir des inspirations profondes qui viennent de l'intérieur.",
        "Créer quelque chose sans le montrer à personne",
        "Trois respirations en laissant la lumière briller en silence",
        "Quelle créativité intérieure n'a besoin d'aucun témoin ?"),

    # VIRGO - 12 maisons
    ('virgo', 1): make_neptune_interp('virgo', 1,
        "Tu incarnes un rêve de perfection — ton identité cherche à fusionner service et spiritualité.",
        "Neptune en Vierge en Maison 1 te donne une personnalité qui rêve de servir de façon parfaite. Tu veux améliorer le monde, guérir ce qui est brisé, purifier ce qui est pollué.",
        "Le piège : une identité perfectionniste qui n'est jamais satisfaite, se critiquer constamment, confondre amélioration et valeur. La vraie perfection accepte aussi l'imperfection.",
        "Neptune adoucit et spiritualise ton sens pratique. Tu projettes une image de service et de pureté. Ton apparence peut refléter ta quête de perfection.",
        "Accepter une imperfection en toi avec compassion",
        "Trois respirations en t'aimant tel que tu es",
        "Comment puis-je servir sans me juger ?"),

    ('virgo', 2): make_neptune_interp('virgo', 2,
        "Tu rêves d'une prospérité pure — tes ressources viennent quand tu sers avec dévouement.",
        "Neptune en Vierge en Maison 2 crée une relation éthique à l'argent. Tu veux que tes revenus soient purs, gagnés par un service authentique.",
        "Le piège : sous-valoriser tes services, avoir une relation anxieuse à l'argent, confondre sacrifice et service. La vraie prospérité du service est aussi juste pour toi.",
        "Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par des activités de soin, d'amélioration, de guérison. Tes valeurs sont liées à l'utilité et à la pureté.",
        "Identifier la juste valeur de tes services",
        "Trois respirations en honorant ton travail",
        "Comment mes services méritent-ils une juste rémunération ?"),

    ('virgo', 3): make_neptune_interp('virgo', 3,
        "Tu communiques avec précision inspirée — tes mots guérissent et clarifient de façon subtile.",
        "Neptune en Vierge en Maison 3 te donne une communication qui combine précision et intuition. Tu sais exprimer des idées complexes de façon claire et touchante.",
        "Le piège : une communication trop critique ou perfectionniste, avoir du mal à tolérer l'imprécision des autres, confondre analyse et jugement. La vraie communication guérissante est aussi bienveillante.",
        "Neptune spiritualise tes échanges de façon subtile et précise. Tu peux avoir un don pour l'écriture qui guérit ou clarifie.",
        "Communiquer une critique de façon bienveillante",
        "Trois respirations en servant par les mots",
        "Comment ma communication peut-elle guérir plutôt que critiquer ?"),

    ('virgo', 4): make_neptune_interp('virgo', 4,
        "Tu rêves d'un foyer parfait — ta maison devient un sanctuaire de pureté et de soin.",
        "Neptune en Vierge en Maison 4 crée un environnement domestique orienté vers la santé, l'ordre et le soin. Ton foyer peut être un lieu de guérison et de bien-être.",
        "Le piège : un foyer obsédé par la perfection, critiquer constamment l'environnement, confondre ordre et amour. La vraie maison de soin accepte aussi le désordre.",
        "Neptune spiritualise ta vie familiale. Tu as peut-être grandi dans un environnement axé sur la santé ou le service. Ton foyer peut être un lieu de guérison.",
        "Accepter un désordre chez toi sans anxiété",
        "Trois respirations en trouvant la paix dans l'imparfait",
        "Comment mon foyer peut-il être sain sans être parfait ?"),

    ('virgo', 5): make_neptune_interp('virgo', 5,
        "Tu crées avec précision et soin — tes œuvres et tes amours sont des expressions de service et de dévouement.",
        "Neptune en Vierge en Maison 5 te pousse vers une créativité qui sert un but utile. Tu veux que tes œuvres améliorent quelque chose. En amour, tu cherches des partenaires avec qui tu peux construire concrètement.",
        "Le piège : juger tes créations trop sévèrement, des amours basées sur des critères de perfection, avoir du mal avec la joie pure. La vraie joie créative accepte aussi l'imperfection.",
        "Neptune spiritualise tes plaisirs de façon pratique et utile. Tu peux avoir des amours qui se construisent dans le service mutuel.",
        "Créer quelque chose sans le juger",
        "Trois respirations en laissant la joie être imparfaite",
        "Comment ma créativité peut-elle être joyeuse sans être parfaite ?"),

    ('virgo', 6): make_neptune_interp('virgo', 6,
        "Tu travailles avec dévotion spirituelle — ton quotidien devient une pratique de service et de guérison.",
        "Neptune en Vierge en Maison 6 amplifie au maximum ton sens du service et de l'amélioration. Tu veux que ton travail quotidien soit une forme de guérison, une contribution au bien du monde.",
        "Le piège : un perfectionnisme qui épuise, te sacrifier au service des autres, confondre dévotion et martyre. Le vrai service spirituel te nourrit aussi.",
        "Neptune spiritualise au maximum ton quotidien. Tu excelles dans les métiers de soin, d'amélioration, de guérison. Ta santé est très sensible à ton environnement de travail.",
        "Prendre soin de toi avec le même soin que tu donnes aux autres",
        "Trois respirations en équilibrant service et soin de soi",
        "Comment puis-je servir tout en me nourrissant ?"),

    ('virgo', 7): make_neptune_interp('virgo', 7,
        "Tu rêves de partenariats de service mutuel — tes relations sont des collaborations pour améliorer le monde.",
        "Neptune en Vierge en Maison 7 crée des relations basées sur le service mutuel et l'amélioration commune. Tu attires des partenaires avec qui tu veux construire quelque chose d'utile.",
        "Le piège : critiquer constamment ton partenaire, des relations basées sur l'amélioration plutôt que l'acceptation, confondre aide et amour. Les meilleures relations acceptent aussi les imperfections.",
        "Neptune spiritualise tes partenariats de service et d'aide mutuelle. Tu peux avoir des relations très constructives mais qui demandent de l'acceptation.",
        "Apprécier ton partenaire sans chercher à l'améliorer",
        "Trois respirations en aimant ce qui est",
        "Comment mes relations peuvent-elles être aimantes sans être correctrices ?"),

    ('virgo', 8): make_neptune_interp('virgo', 8,
        "Tu traverses les crises par l'analyse guérissante — les transformations deviennent des occasions de purification.",
        "Neptune en Vierge en Maison 8 te donne la capacité d'analyser les crises de façon guérissante. Les transformations te permettent de te purifier, d'éliminer ce qui n'est plus utile.",
        "Le piège : analyser les crises au lieu de les traverser émotionnellement, vouloir tout contrôler, confondre purification et rejet. La vraie guérison accepte aussi ce qui ne peut être changé.",
        "Neptune spiritualise ta relation aux crises de façon analytique. Tu peux avoir des capacités de guérison ou de diagnostic. Ta sexualité peut être liée à la santé et à la purification.",
        "Accueillir une transformation sans chercher à la contrôler",
        "Trois respirations en lâchant le besoin d'analyser",
        "Quelle guérison m'attend de l'autre côté du lâcher-prise ?"),

    ('virgo', 9): make_neptune_interp('virgo', 9,
        "Tu rêves d'une sagesse pratique — ta philosophie améliore concrètement la vie.",
        "Neptune en Vierge en Maison 9 te pousse vers des croyances qui ont une application pratique. Tu ne te satisfais pas des philosophies abstraites — tu veux des enseignements qui fonctionnent.",
        "Le piège : rejeter les sagesses qui ne sont pas pratiques, réduire la spiritualité à des techniques, confondre utilité et vérité. La vraie sagesse pratique inclut aussi le mystère.",
        "Neptune spiritualise ta quête de sens de façon pratique. Tu peux être attiré par des spiritualités qui améliorent la vie quotidienne.",
        "Explorer une sagesse qui accepte le mystère",
        "Trois respirations en trouvant la paix au-delà de l'utile",
        "Quelle sagesse m'enseigne l'acceptation du mystère ?"),

    ('virgo', 10): make_neptune_interp('virgo', 10,
        "Tu rêves d'une carrière de service — ta réussite vient quand tu améliores et guéris le monde.",
        "Neptune en Vierge en Maison 10 te pousse vers une carrière qui améliore concrètement les choses. Tu peux réussir dans les métiers de soin, d'amélioration, de guérison.",
        "Le piège : une carrière perfectionniste qui n'est jamais satisfaite, sous-valoriser tes contributions, confondre service et invisibilité. La vraie réussite de service est aussi reconnue.",
        "Neptune spiritualise ta carrière et ta réputation de service. On te reconnaît pour ta capacité à améliorer et à guérir. Ta carrière peut sembler modeste mais a un impact profond.",
        "Reconnaître la valeur de tes contributions",
        "Trois respirations en honorant ton service",
        "Comment ma carrière peut-elle être reconnue pour son impact ?"),

    ('virgo', 11): make_neptune_interp('virgo', 11,
        "Tu rêves de communautés de service — tes amitiés et tes projets améliorent concrètement le monde.",
        "Neptune en Vierge en Maison 11 te connecte à des réseaux de personnes orientées vers le service et l'amélioration. Tes amis partagent ton souci de rendre le monde meilleur. Les projets collectifs sont utiles et concrets.",
        "Le piège : critiquer les groupes qui ne sont pas assez efficaces, des projets qui restent au stade de l'analyse, confondre critique et amélioration. Les meilleures communautés acceptent aussi l'imperfection.",
        "Neptune spiritualise tes réseaux et tes projets de service collectif. Tu es fait pour les organisations de soin, les associations d'amélioration.",
        "Participer à un projet imparfait sans le critiquer",
        "Trois respirations en acceptant l'imperfection collective",
        "Comment mes réseaux peuvent-ils agir sans tout perfectionner d'abord ?"),

    ('virgo', 12): make_neptune_interp('virgo', 12,
        "Tu rêves d'une guérison intérieure — ton inconscient est une source de purification et de service silencieux.",
        "Neptune en Vierge en Maison 12 crée des connexions entre ton sens du service et les dimensions invisibles. Tes rêves peuvent contenir des messages de guérison. Ton inconscient cherche la purification.",
        "Le piège : une autocritique intérieure constante, confondre introspection et jugement, avoir du mal à s'accepter. La vraie guérison intérieure est aussi compatissante envers soi-même.",
        "Neptune spiritualise au maximum ta connexion à la guérison invisible. Tu peux avoir des capacités de guérison spirituelle. Les retraites de santé te régénèrent.",
        "Te pardonner une imperfection avec compassion",
        "Trois respirations en t'accueillant tel que tu es",
        "Quelle guérison intérieure m'attend dans l'auto-compassion ?"),

    # LIBRA - 12 maisons
    ('libra', 1): make_neptune_interp('libra', 1,
        "Tu incarnes un rêve d'harmonie — ton identité cherche à fusionner beauté et spiritualité.",
        "Neptune en Balance en Maison 1 te donne une personnalité qui rêve de beauté et d'harmonie parfaites. Tu veux incarner l'élégance, créer de l'équilibre partout où tu vas.",
        "Le piège : une identité trop dépendante du regard des autres, perdre tes limites dans les relations, confondre plaire et être. La vraie harmonie inclut aussi l'affirmation de soi.",
        "Neptune adoucit et idéalise ta personnalité. Tu projettes une image de douceur et de beauté. Ton apparence peut refléter ta quête d'harmonie.",
        "Affirmer un aspect de toi qui ne plaît pas à tous",
        "Trois respirations en t'assumant pleinement",
        "Comment puis-je être harmonieux tout en restant authentique ?"),

    ('libra', 2): make_neptune_interp('libra', 2,
        "Tu rêves d'une prospérité harmonieuse — tes ressources viennent quand tu crées de la beauté et de l'équilibre.",
        "Neptune en Balance en Maison 2 crée une relation esthétique à l'argent. Tu veux que tes revenus viennent de la création de beauté et d'harmonie.",
        "Le piège : des finances floues par excès de générosité, confondre valeur et apparence, dépendre financièrement des autres. La vraie prospérité harmonieuse est aussi indépendante.",
        "Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par des activités artistiques ou relationnelles. Tes valeurs sont liées à la beauté et à l'équilibre.",
        "Créer de la valeur indépendamment des autres",
        "Trois respirations en trouvant ta propre abondance",
        "Comment ma prospérité peut-elle être harmonieuse ET indépendante ?"),

    ('libra', 3): make_neptune_interp('libra', 3,
        "Tu communiques avec grâce — tes mots créent des ponts et de l'harmonie entre les gens.",
        "Neptune en Balance en Maison 3 te donne une communication diplomatique et belle. Tu sais présenter les choses de façon à créer de l'entente, à adoucir les conflits.",
        "Le piège : une communication qui évite la vérité pour maintenir l'harmonie, avoir du mal à dire non, confondre diplomatie et manque de sincérité. La vraie communication harmonieuse est aussi vraie.",
        "Neptune spiritualise tes échanges de grâce et de diplomatie. Tu peux avoir un don pour la médiation ou l'écriture esthétique.",
        "Communiquer une vérité difficile avec grâce",
        "Trois respirations en équilibrant harmonie et vérité",
        "Comment ma communication peut-elle être belle ET sincère ?"),

    ('libra', 4): make_neptune_interp('libra', 4,
        "Tu rêves d'un foyer harmonieux — ta maison devient un temple de beauté et de paix.",
        "Neptune en Balance en Maison 4 crée un environnement domestique idéalement beau et paisible. Ton foyer peut être un sanctuaire d'harmonie, un lieu où règne l'équilibre.",
        "Le piège : éviter les conflits familiaux au détriment de l'authenticité, un foyer trop dépendant de l'apparence, fuir les problèmes dans l'esthétique. La vraie maison harmonieuse accueille aussi les difficultés.",
        "Neptune spiritualise ta vie familiale. Tu as peut-être grandi dans un environnement axé sur l'harmonie ou tu crées le tien comme un havre de paix.",
        "Accueillir un conflit familial sans le fuir",
        "Trois respirations en trouvant la paix au-delà de l'harmonie apparente",
        "Comment mon foyer peut-il être paisible tout en étant authentique ?"),

    ('libra', 5): make_neptune_interp('libra', 5,
        "Tu crées avec élégance spirituelle — tes œuvres et tes amours sont des célébrations de la beauté divine.",
        "Neptune en Balance en Maison 5 te pousse vers une créativité qui célèbre la beauté et l'harmonie. Tu veux que tes œuvres touchent par leur élégance. En amour, tu cherches des partenaires qui incarnent la beauté.",
        "Le piège : idéaliser les partenaires pour leur apparence, une créativité qui cherche trop à plaire, confondre surface et profondeur. La vraie joie créative a aussi de la substance.",
        "Neptune spiritualise tes plaisirs d'élégance et de beauté. Tu peux avoir des amours très esthétiques mais qui peuvent manquer de profondeur.",
        "Créer quelque chose de beau qui a aussi de la profondeur",
        "Trois respirations en trouvant la beauté dans la substance",
        "Comment ma créativité peut-elle être belle ET profonde ?"),

    ('libra', 6): make_neptune_interp('libra', 6,
        "Tu travailles avec une vision d'harmonie — ton quotidien devient une pratique d'embellissement du monde.",
        "Neptune en Balance en Maison 6 te pousse vers un travail qui crée de la beauté et de l'harmonie. Tu veux que ton environnement de travail soit esthétique et équilibré.",
        "Le piège : éviter les tâches ingrates, un travail confus par excès de rêverie, négliger l'efficacité pour l'apparence. Le vrai travail harmonieux est aussi efficace.",
        "Neptune spiritualise ton quotidien. Tu travailles mieux dans des environnements beaux et paisibles. Ta santé peut bénéficier d'harmonie dans ton environnement.",
        "Accomplir une tâche ingrate avec grâce",
        "Trois respirations en trouvant la beauté dans l'utile",
        "Comment mon travail peut-il être harmonieux ET efficace ?"),

    ('libra', 7): make_neptune_interp('libra', 7,
        "Tu rêves de partenariats parfaits — tes relations sont des unions d'âmes en quête d'harmonie absolue.",
        "Neptune en Balance en Maison 7 amplifie au maximum ton rêve de partenariats harmonieux. Tu attires des partenaires avec qui tu veux créer l'équilibre parfait.",
        "Le piège : idéaliser les partenaires, des relations qui évitent les conflits nécessaires, confondre paix et stagnation. Les meilleures relations incluent aussi les désaccords constructifs.",
        "Neptune spiritualise au maximum tes partenariats. Tu peux avoir des relations qui ressemblent à des rêves mais qui demandent un travail de réalisme.",
        "Accueillir un désaccord constructif dans ta relation",
        "Trois respirations en trouvant l'harmonie qui inclut la vérité",
        "Comment mes relations peuvent-elles être harmonieuses tout en étant vraies ?"),

    ('libra', 8): make_neptune_interp('libra', 8,
        "Tu traverses les crises en cherchant l'équilibre — les transformations deviennent des occasions de trouver une nouvelle harmonie.",
        "Neptune en Balance en Maison 8 te donne la capacité de trouver de l'équilibre même dans les crises. Les transformations te poussent vers de nouvelles formes d'harmonie.",
        "Le piège : éviter les transformations profondes pour maintenir l'harmonie superficielle, fuir les conflits nécessaires, confondre paix et déni. La vraie transformation harmonieuse traverse aussi l'ombre.",
        "Neptune spiritualise ta relation aux crises de façon équilibrante. Ta sexualité peut être liée à la recherche d'union parfaite.",
        "Traverser une transformation sans éviter l'inconfort",
        "Trois respirations en trouvant l'équilibre au-delà du confort",
        "Quelle harmonie nouvelle m'attend de l'autre côté de cette crise ?"),

    ('libra', 9): make_neptune_interp('libra', 9,
        "Tu rêves d'une sagesse d'harmonie — ta philosophie célèbre l'équilibre et la beauté comme voies d'éveil.",
        "Neptune en Balance en Maison 9 te pousse vers des croyances qui célèbrent l'harmonie, la beauté et l'équilibre comme valeurs suprêmes. Ta spiritualité cherche l'union des contraires.",
        "Le piège : une philosophie qui évite les positions tranchées, confondre relativisme et sagesse, avoir du mal à s'engager dans une voie. La vraie sagesse d'harmonie sait aussi choisir.",
        "Neptune spiritualise ta quête de sens de beauté et d'équilibre. Tu peux être attiré par des spiritualités qui unissent les polarités.",
        "Prendre position sur quelque chose d'important",
        "Trois respirations en trouvant l'équilibre dans l'engagement",
        "Comment ma sagesse peut-elle être équilibrée ET engagée ?"),

    ('libra', 10): make_neptune_interp('libra', 10,
        "Tu rêves d'une carrière d'harmonie — ta réussite vient quand tu crées de la beauté et de l'équilibre visibles.",
        "Neptune en Balance en Maison 10 te pousse vers une carrière qui crée de l'harmonie et de la beauté. Tu peux réussir dans l'art, la diplomatie, la médiation, le design.",
        "Le piège : une carrière floue par excès de rêverie, avoir du mal à te positionner, confondre réputation et réalité. La vraie réussite harmonieuse a aussi une direction claire.",
        "Neptune spiritualise ta carrière et ta réputation de beauté et d'équilibre. On te reconnaît pour ta capacité à créer de l'harmonie. Ta carrière peut sembler suivre un chemin esthétique.",
        "Clarifier une direction dans ta carrière",
        "Trois respirations en alignant beauté et détermination",
        "Comment ma carrière peut-elle être harmonieuse ET déterminée ?"),

    ('libra', 11): make_neptune_interp('libra', 11,
        "Tu rêves de communautés d'harmonie — tes amitiés et tes projets créent de la beauté collective.",
        "Neptune en Balance en Maison 11 te connecte à des réseaux de personnes qui valorisent l'harmonie et la beauté. Tes amis partagent ton sens esthétique. Les projets collectifs embellissent le monde.",
        "Le piège : des amitiés superficielles par désir de plaire à tous, éviter les conflits de groupe nécessaires, confondre consensus et unité. Les meilleures communautés honorent aussi les désaccords.",
        "Neptune spiritualise tes réseaux et tes projets d'harmonie collective. Tu es fait pour les collectifs artistiques, les associations de paix et de dialogue.",
        "Exprimer un désaccord constructif dans un groupe",
        "Trois respirations en trouvant l'unité qui inclut la diversité",
        "Comment mes réseaux peuvent-ils être harmonieux tout en accueillant les différences ?"),

    ('libra', 12): make_neptune_interp('libra', 12,
        "Tu rêves d'une harmonie intérieure — ton inconscient cherche l'équilibre parfait entre toutes les parties de toi.",
        "Neptune en Balance en Maison 12 crée des connexions entre ton sens de l'harmonie et les dimensions invisibles. Tes rêves peuvent chercher à réconcilier des opposés. Ton inconscient aspire à l'unité.",
        "Le piège : projeter tes ombres sur les autres, avoir du mal avec les conflits intérieurs, fuir dans des rêves d'harmonie. La vraie paix intérieure inclut aussi l'ombre.",
        "Neptune spiritualise au maximum ta connexion à l'harmonie invisible. Tu peux avoir des intuitions sur les équilibres et déséquilibres subtils.",
        "Accueillir une partie de toi qui semble en conflit",
        "Trois respirations en trouvant l'harmonie dans la totalité",
        "Quelle harmonie intérieure m'attend quand j'accepte toutes mes parties ?"),

    # SCORPIO - 12 maisons
    ('scorpio', 1): make_neptune_interp('scorpio', 1,
        "Tu incarnes une profondeur mystique — ton identité cherche à fusionner transformation et transcendance.",
        "Neptune en Scorpion en Maison 1 te donne une personnalité profondément intuitive et transformatrice. Tu perçois l'invisible, tu sens ce qui est caché, tu touches les mystères.",
        "Le piège : une identité obsédée par les ténèbres, confondre profondeur et morbidité, avoir du mal avec la légèreté. La vraie profondeur mystique inclut aussi la lumière.",
        "Neptune amplifie ton intensité et ta connexion aux mystères. Tu projettes une image de profondeur et de puissance subtile. Ton apparence peut refléter ton intensité intérieure.",
        "Trouver de la légèreté dans la profondeur",
        "Trois respirations en équilibrant ombre et lumière",
        "Comment puis-je être profond tout en restant léger ?"),

    ('scorpio', 2): make_neptune_interp('scorpio', 2,
        "Tu rêves d'une prospérité transformée — tes ressources viennent de sources invisibles et profondes.",
        "Neptune en Scorpion en Maison 2 crée une relation mystique à l'argent. Tu peux recevoir de façon inattendue, transformer des crises en opportunités, trouver des ressources cachées.",
        "Le piège : une relation confuse et intense à l'argent, des finances qui fluctuent avec tes crises, confondre pouvoir et valeur. La vraie prospérité transformée est aussi stable.",
        "Neptune spiritualise ta relation aux ressources profondes. Tu peux gagner de l'argent par des activités de transformation ou de guérison. Tes valeurs sont liées à la profondeur et à l'authenticité.",
        "Créer de la stabilité financière dans l'intensité",
        "Trois respirations en ancrant ta prospérité",
        "Comment mes ressources peuvent-elles être profondes ET stables ?"),

    ('scorpio', 3): make_neptune_interp('scorpio', 3,
        "Tu communiques avec une profondeur pénétrante — tes mots touchent les vérités cachées et transforment.",
        "Neptune en Scorpion en Maison 3 te donne une communication qui va au fond des choses. Tu perçois ce qui n'est pas dit, tu exprimes des vérités que d'autres n'osent pas formuler.",
        "Le piège : une communication qui manipule ou blesse, des échanges trop intenses, confondre révélation et agression. La vraie communication profonde est aussi bienveillante.",
        "Neptune spiritualise tes échanges d'intensité et de vérité. Tu peux avoir des dons pour l'écriture qui touche les profondeurs. Tes relations peuvent être intenses ou transformatrices.",
        "Communiquer une vérité profonde avec bienveillance",
        "Trois respirations en servant la vérité avec amour",
        "Comment ma communication peut-elle transformer tout en guérissant ?"),

    ('scorpio', 4): make_neptune_interp('scorpio', 4,
        "Tu rêves d'un foyer de transformation — ta maison devient un creuset où les âmes se transforment.",
        "Neptune en Scorpion en Maison 4 crée un environnement familial intense et transformateur. Ton foyer peut être un lieu de guérison profonde, de secrets révélés, de renaissance.",
        "Le piège : des drames familiaux constants, absorber les ombres familiales, confondre intensité et amour. La vraie maison de transformation connaît aussi la paix.",
        "Neptune spiritualise ta vie familiale de façon intense. Tu as peut-être grandi dans un environnement où les secrets et les transformations étaient présents.",
        "Créer un moment de paix légère chez toi",
        "Trois respirations en trouvant la sérénité dans l'intensité",
        "Comment mon foyer peut-il être transformateur ET paisible ?"),

    ('scorpio', 5): make_neptune_interp('scorpio', 5,
        "Tu crées avec une intensité transcendante — tes œuvres et tes amours touchent les profondeurs de l'âme.",
        "Neptune en Scorpion en Maison 5 te pousse vers une créativité qui transforme. Tu veux que tes œuvres touchent les gens au plus profond. En amour, tu cherches des connexions qui transforment l'âme.",
        "Le piège : des amours intenses qui deviennent destructrices, une créativité obsédée par les ténèbres, confondre passion et amour. La vraie joie créative inclut aussi la lumière.",
        "Neptune spiritualise tes plaisirs d'intensité et de profondeur. Tu peux avoir des amours transformatrices mais qui peuvent être éprouvantes.",
        "Créer quelque chose de lumineux et joyeux",
        "Trois respirations en laissant la joie être légère",
        "Comment ma créativité peut-elle transformer tout en célébrant la vie ?"),

    ('scorpio', 6): make_neptune_interp('scorpio', 6,
        "Tu travailles avec une intensité guérissante — ton quotidien devient une pratique de transformation et de guérison.",
        "Neptune en Scorpion en Maison 6 te pousse vers des métiers de guérison profonde. Tu veux que ton travail touche les causes profondes, pas seulement les symptômes.",
        "Le piège : absorber les énergies négatives des autres, un travail épuisant par trop d'intensité, confondre service et sacrifice. Le vrai travail de guérison te protège aussi.",
        "Neptune spiritualise ton quotidien de guérison et de transformation. Tu travailles mieux quand tu peux avoir un impact profond. Ta santé peut être sensible aux énergies.",
        "Protéger ton énergie dans le service",
        "Trois respirations en créant une limite de protection",
        "Comment mon travail peut-il transformer tout en me préservant ?"),

    ('scorpio', 7): make_neptune_interp('scorpio', 7,
        "Tu rêves de partenariats de transformation mutuelle — tes relations sont des alchimies d'âmes.",
        "Neptune en Scorpion en Maison 7 crée des relations de transformation mutuelle profonde. Tu attires des partenaires avec qui tu vis des morts et des renaissances ensemble.",
        "Le piège : des relations destructrices par excès d'intensité, des jeux de pouvoir, confondre passion et connexion. Les meilleures relations transforment sans détruire.",
        "Neptune spiritualise tes partenariats de profondeur et de transformation. Tu peux avoir des relations karmiques ou très intenses qui demandent de la conscience.",
        "Créer un moment de légèreté dans ta relation intense",
        "Trois respirations en équilibrant profondeur et joie",
        "Comment mes relations peuvent-elles transformer tout en restant joyeuses ?"),

    ('scorpio', 8): make_neptune_interp('scorpio', 8,
        "Tu traverses les crises comme un initié — les transformations sont des portails vers des dimensions plus profondes.",
        "Neptune en Scorpion en Maison 8 amplifie au maximum ta capacité à traverser les crises et à en émerger transformé. Tu as accès aux mystères de la vie et de la mort.",
        "Le piège : chercher les crises par fascination pour les ténèbres, avoir du mal avec la vie ordinaire, confondre initiation et destruction. La vraie maîtrise transformatrice inclut aussi la vie.",
        "Neptune spiritualise au maximum ta relation aux mystères et aux transformations. Tu peux avoir des capacités de guérison ou des perceptions de l'invisible. Ta sexualité est profondément transformatrice.",
        "Célébrer un aspect simple et joyeux de la vie",
        "Trois respirations en équilibrant profondeur et célébration",
        "Comment puis-je honorer les mystères tout en célébrant la vie ?"),

    ('scorpio', 9): make_neptune_interp('scorpio', 9,
        "Tu rêves d'une sagesse des mystères — ta philosophie embrasse la mort et la renaissance comme vérités ultimes.",
        "Neptune en Scorpion en Maison 9 te pousse vers des croyances qui touchent aux mystères ultimes. Ta spiritualité est initiatique, explorant les dimensions cachées de l'existence.",
        "Le piège : une spiritualité obsédée par les ténèbres, confondre profondeur et morbidité, imposer ta vision intense aux autres. La vraie sagesse des mystères célèbre aussi la vie.",
        "Neptune spiritualise ta quête de sens de façon initiatique. Tu peux être attiré par des traditions mystiques, chamaniques, qui touchent aux grands passages.",
        "Explorer une sagesse qui célèbre la vie autant que la mort",
        "Trois respirations en trouvant la lumière dans le mystère",
        "Comment ma sagesse peut-elle embrasser les mystères tout en célébrant la vie ?"),

    ('scorpio', 10): make_neptune_interp('scorpio', 10,
        "Tu rêves d'une carrière de transformation — ta réussite vient quand tu aides les autres à traverser leurs crises.",
        "Neptune en Scorpion en Maison 10 te pousse vers une carrière qui touche aux transformations profondes. Tu peux réussir dans la thérapie, la médecine, la gestion de crise, tout ce qui accompagne les passages.",
        "Le piège : une carrière épuisante par trop d'intensité, absorber les crises des autres, confondre pouvoir et service. La vraie réussite transformatrice te préserve aussi.",
        "Neptune spiritualise ta carrière et ta réputation de profondeur. On te reconnaît pour ta capacité à accompagner les transformations. Ta carrière peut sembler mystérieuse aux autres.",
        "Protéger ton énergie dans ta carrière",
        "Trois respirations en servant sans s'épuiser",
        "Comment ma carrière peut-elle transformer tout en me préservant ?"),

    ('scorpio', 11): make_neptune_interp('scorpio', 11,
        "Tu rêves de communautés de transformation — tes amitiés et tes projets touchent aux profondeurs collectives.",
        "Neptune en Scorpion en Maison 11 te connecte à des réseaux de personnes engagées dans la transformation. Tes amis sont des êtres de profondeur. Les projets collectifs touchent aux enjeux essentiels.",
        "Le piège : des amitiés trop intenses qui épuisent, des projets qui deviennent des luttes de pouvoir, confondre engagement et obsession. Les meilleures communautés transforment avec joie aussi.",
        "Neptune spiritualise tes réseaux et tes projets de transformation collective. Tu es fait pour les mouvements de guérison collective, les associations qui touchent aux enjeux profonds.",
        "Créer un moment de légèreté avec ton réseau",
        "Trois respirations en trouvant la joie dans l'engagement",
        "Comment mes réseaux peuvent-ils transformer tout en restant joyeux ?"),

    ('scorpio', 12): make_neptune_interp('scorpio', 12,
        "Tu rêves des abîmes de l'âme — ton inconscient est une porte vers les mystères ultimes.",
        "Neptune en Scorpion en Maison 12 amplifie au maximum ta connexion aux dimensions invisibles les plus profondes. Tu as accès aux couches les plus cachées de l'inconscient collectif.",
        "Le piège : te perdre dans les abîmes, confondre dissolution et éveil, avoir du mal avec la vie ordinaire. La vraie connexion aux mystères inclut aussi le retour à la surface.",
        "Neptune spiritualise au maximum ta connexion à l'invisible profond. Tu peux avoir des expériences spirituelles intenses et transformatrices. Les retraites de méditation profonde te conviennent.",
        "Remonter doucement à la surface après une immersion",
        "Trois respirations en ancrant les profondeurs dans le quotidien",
        "Comment puis-je explorer les abîmes tout en restant ancré dans la vie ?"),
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
