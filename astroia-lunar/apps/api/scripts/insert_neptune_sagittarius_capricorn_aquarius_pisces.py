#!/usr/bin/env python3
"""Script d'insertion des interprétations Neptune/Sagittarius, Capricorn, Aquarius, Pisces en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_neptune_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'sagittarius': '♆ Neptune en Sagittaire', 'capricorn': '♆ Neptune en Capricorne',
        'aquarius': '♆ Neptune en Verseau', 'pisces': '♆ Neptune en Poissons'
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
    # SAGITTARIUS - 12 maisons
    ('sagittarius', 1): make_neptune_interp('sagittarius', 1,
        "Tu incarnes un rêve d'expansion — ton identité cherche à fusionner vision et spiritualité.",
        "Neptune en Sagittaire en Maison 1 te donne une personnalité qui rêve d'horizons infinis. Tu veux embrasser toutes les vérités, explorer toutes les philosophies, comprendre le sens de tout.",
        "Le piège : une identité qui se perd dans les grandes idées, fuir la réalité dans les visions, confondre enthousiasme et sagesse. La vraie expansion spirituelle s'incarne aussi.",
        "Neptune spiritualise ta soif d'expansion. Tu projettes une image de chercheur de vérité inspiré. Ton apparence peut refléter tes influences multiculturelles ou philosophiques.",
        "Ancrer une vision dans une action concrète",
        "Trois respirations en incarnant ta philosophie",
        "Comment puis-je vivre mes idéaux de façon concrète ?"),

    ('sagittarius', 2): make_neptune_interp('sagittarius', 2,
        "Tu rêves d'une prospérité de sens — tes ressources viennent quand tu partages ta vision généreusement.",
        "Neptune en Sagittaire en Maison 2 crée une relation idéaliste à l'argent. Tu veux que tes revenus viennent de l'expansion des consciences, de l'enseignement, des voyages de l'esprit.",
        "Le piège : des finances floues par excès d'idéalisme, donner sans compter, confondre abondance spirituelle et matérielle. La vraie prospérité visionnaire est aussi concrète.",
        "Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par l'enseignement, l'édition, les voyages. Tes valeurs sont liées au sens et à l'expansion.",
        "Créer une structure pour ta générosité",
        "Trois respirations en équilibrant don et stabilité",
        "Comment ma vision peut-elle créer une prospérité durable ?"),

    ('sagittarius', 3): make_neptune_interp('sagittarius', 3,
        "Tu communiques avec vision et inspiration — tes mots ouvrent des horizons et éveillent la soif de sens.",
        "Neptune en Sagittaire en Maison 3 te donne une communication qui inspire et élève. Tu sais présenter les grandes idées de façon à éveiller l'enthousiasme et la quête de sens.",
        "Le piège : une communication qui exagère, promettre plus que possible, confondre inspiration et manipulation. La vraie communication visionnaire reste aussi honnête.",
        "Neptune spiritualise tes échanges de vision et d'expansion. Tu peux avoir un don pour l'enseignement inspirant ou l'écriture philosophique.",
        "Communiquer une vision de façon mesurée",
        "Trois respirations en servant la vérité avec enthousiasme",
        "Comment ma communication peut-elle inspirer sans exagérer ?"),

    ('sagittarius', 4): make_neptune_interp('sagittarius', 4,
        "Tu rêves d'un foyer de sagesse — ta maison devient un temple où se transmettent les grandes vérités.",
        "Neptune en Sagittaire en Maison 4 crée un environnement familial philosophique et ouvert. Ton foyer peut être un lieu de transmission de sagesse, de discussions sur le sens de la vie.",
        "Le piège : fuir les responsabilités familiales dans les grandes idées, un foyer instable par excès de voyages, confondre ouverture et déracinement. La vraie maison de sagesse a aussi des racines.",
        "Neptune spiritualise ta vie familiale. Tu as peut-être grandi dans un environnement philosophique ou multiculturel. Ton foyer peut être un lieu de rassemblement d'esprits.",
        "Créer un enracinement tout en gardant l'ouverture",
        "Trois respirations en ancrant la sagesse chez toi",
        "Comment mon foyer peut-il être à la fois ancré et ouvert sur le monde ?"),

    ('sagittarius', 5): make_neptune_interp('sagittarius', 5,
        "Tu crées avec vision et enthousiasme — tes œuvres et tes amours sont des aventures de l'esprit.",
        "Neptune en Sagittaire en Maison 5 te pousse vers une créativité qui explore et enseigne. Tu veux que tes œuvres élargissent les horizons. En amour, tu cherches des partenaires qui partagent ta soif d'expansion.",
        "Le piège : idéaliser les partenaires comme des sages, une créativité qui reste dans les idées, confondre aventure et engagement. La vraie joie créative s'incarne aussi.",
        "Neptune spiritualise tes plaisirs d'exploration et de sens. Tu peux avoir des amours inspirantes mais qui peuvent manquer de profondeur si tu n'es pas vigilant.",
        "Approfondir une création plutôt qu'en commencer une nouvelle",
        "Trois respirations en trouvant la profondeur dans l'exploration",
        "Comment ma créativité peut-elle être expansive ET profonde ?"),

    ('sagittarius', 6): make_neptune_interp('sagittarius', 6,
        "Tu travailles avec vision et idéalisme — ton quotidien devient une quête de sens incarné.",
        "Neptune en Sagittaire en Maison 6 te pousse vers un travail qui a du sens large. Tu veux que ton quotidien serve une vision plus grande, que tes tâches contribuent à quelque chose de significatif.",
        "Le piège : avoir du mal avec les tâches ordinaires, un travail confus par excès de vision, négliger les détails pour les grandes idées. Le vrai travail visionnaire inclut aussi l'ordinaire.",
        "Neptune spiritualise ton quotidien. Tu travailles mieux quand tu comprends le sens de ce que tu fais. Ta santé peut être sensible à ton niveau d'inspiration.",
        "Trouver du sens dans une tâche ordinaire",
        "Trois respirations en trouvant le sacré dans le quotidien",
        "Comment mon travail quotidien peut-il servir ma vision plus large ?"),

    ('sagittarius', 7): make_neptune_interp('sagittarius', 7,
        "Tu rêves de partenariats d'expansion — tes relations sont des voyages de croissance partagée.",
        "Neptune en Sagittaire en Maison 7 crée des relations basées sur la quête de sens commune. Tu attires des partenaires avec qui tu veux explorer, grandir, comprendre le monde.",
        "Le piège : idéaliser les partenaires comme des guides, des relations qui fuient l'intimité dans les grandes idées, confondre inspiration et amour. Les meilleures relations incluent aussi l'intimité.",
        "Neptune spiritualise tes partenariats d'exploration et de croissance. Tu peux avoir des relations qui semblent destinées mais qui demandent du travail concret.",
        "Créer un moment d'intimité simple avec un partenaire",
        "Trois respirations en trouvant la profondeur dans la proximité",
        "Comment mes relations peuvent-elles être expansives ET intimes ?"),

    ('sagittarius', 8): make_neptune_interp('sagittarius', 8,
        "Tu traverses les crises avec foi — les transformations deviennent des initiations qui élargissent ta vision.",
        "Neptune en Sagittaire en Maison 8 te donne la capacité de trouver du sens dans les crises. Les transformations te poussent vers une compréhension plus large de la vie et de la mort.",
        "Le piège : philosopher sur les crises au lieu de les traverser, fuir l'intensité dans les grandes idées, confondre compréhension et guérison. La vraie transformation visionnaire inclut le ressenti.",
        "Neptune spiritualise ta relation aux crises de façon expansive. Tu peux trouver des enseignements profonds dans les épreuves. Ta sexualité peut être liée à la quête de transcendance.",
        "Laisser une émotion exister sans la philosophiser",
        "Trois respirations en accueillant le ressenti",
        "Comment puis-je traverser les crises avec foi ET présence émotionnelle ?"),

    ('sagittarius', 9): make_neptune_interp('sagittarius', 9,
        "Tu rêves de la vérité ultime — ta quête de sens est une immersion dans les mystères de l'existence.",
        "Neptune en Sagittaire en Maison 9 amplifie au maximum ta soif de comprendre le sens de tout. Tu ne te satisfais pas des réponses partielles — tu veux embrasser toutes les vérités.",
        "Le piège : une quête de sens qui s'éparpille, adhérer à des croyances floues, confondre recherche et errance. La vraie sagesse visionnaire sait aussi s'engager dans une voie.",
        "Neptune spiritualise au maximum ta quête de sens. Tu peux être attiré par toutes les spiritualités à la fois. Les voyages de l'esprit sont ta passion.",
        "S'engager dans une pratique spirituelle spécifique",
        "Trois respirations en trouvant la profondeur dans l'engagement",
        "Quelle voie spirituelle mérite mon engagement profond ?"),

    ('sagittarius', 10): make_neptune_interp('sagittarius', 10,
        "Tu rêves d'une carrière de sens — ta réussite vient quand tu inspires les autres vers des horizons plus larges.",
        "Neptune en Sagittaire en Maison 10 te pousse vers une carrière qui élargit les consciences. Tu peux réussir dans l'enseignement, l'édition, les voyages, tout ce qui ouvre des perspectives.",
        "Le piège : une carrière floue par excès de vision, promettre plus que tu ne peux tenir, confondre inspiration et accomplissement. La vraie réussite visionnaire est aussi concrète.",
        "Neptune spiritualise ta carrière et ta réputation de vision. On te reconnaît pour ta capacité à inspirer et à élargir les horizons. Ta carrière peut sembler suivre un chemin philosophique.",
        "Concrétiser une promesse professionnelle",
        "Trois respirations en alignant vision et action",
        "Comment ma carrière peut-elle être visionnaire ET concrète ?"),

    ('sagittarius', 11): make_neptune_interp('sagittarius', 11,
        "Tu rêves de communautés de chercheurs — tes amitiés et tes projets sont des explorations collectives du sens.",
        "Neptune en Sagittaire en Maison 11 te connecte à des réseaux de chercheurs de vérité. Tes amis partagent ta soif de comprendre. Les projets collectifs explorent de nouvelles visions.",
        "Le piège : des amitiés qui restent au niveau des grandes idées, des projets qui ne se concrétisent pas, confondre discussion et action. Les meilleures communautés passent aussi à l'acte.",
        "Neptune spiritualise tes réseaux et tes projets de vision collective. Tu es fait pour les cercles philosophiques, les groupes de réflexion spirituelle.",
        "Transformer une idée partagée en action concrète",
        "Trois respirations en ancrant la vision dans l'action",
        "Comment mes réseaux peuvent-ils concrétiser nos visions ?"),

    ('sagittarius', 12): make_neptune_interp('sagittarius', 12,
        "Tu rêves de l'infini — ton inconscient est une porte vers les vérités universelles.",
        "Neptune en Sagittaire en Maison 12 crée des connexions entre ta quête de sens et les dimensions invisibles. Tes rêves peuvent contenir des enseignements universels. Ton inconscient est un réservoir de sagesse.",
        "Le piège : te perdre dans des visions grandioses, fuir la réalité dans les grandes idées, confondre intuition et illusion. La vraie sagesse intérieure s'incarne aussi.",
        "Neptune spiritualise au maximum ta connexion à l'invisible expansif. Tu peux avoir des visions qui dépassent ton expérience personnelle. Les retraites de méditation profonde te transforment.",
        "Ancrer une vision intérieure dans une action concrète",
        "Trois respirations en incarnant la sagesse reçue",
        "Comment puis-je incarner les vérités que je perçois intérieurement ?"),

    # CAPRICORN - 12 maisons
    ('capricorn', 1): make_neptune_interp('capricorn', 1,
        "Tu incarnes un rêve de maîtrise — ton identité cherche à fusionner ambition et spiritualité.",
        "Neptune en Capricorne en Maison 1 te donne une personnalité qui rêve de réussite spirituelle. Tu veux accomplir quelque chose de durable qui serve le bien commun.",
        "Le piège : une identité confuse entre ambition et idéalisme, avoir du mal à définir tes objectifs, confondre pouvoir et service. La vraie maîtrise spirituelle sait ce qu'elle veut.",
        "Neptune adoucit et spiritualise ton ambition. Tu projettes une image de sérieux inspiré. Ton apparence peut refléter ta quête de respectabilité spirituelle.",
        "Clarifier un objectif concret",
        "Trois respirations en alignant ambition et service",
        "Comment mon ambition peut-elle servir quelque chose de plus grand ?"),

    ('capricorn', 2): make_neptune_interp('capricorn', 2,
        "Tu rêves d'une prospérité durable — tes ressources servent à construire quelque chose qui dure.",
        "Neptune en Capricorne en Maison 2 crée une relation responsable à l'argent. Tu veux que tes revenus construisent quelque chose de durable, qui serve les générations futures.",
        "Le piège : une relation anxieuse à l'argent, confondre sécurité et valeur, des finances floues malgré l'ambition. La vraie prospérité durable a aussi de la clarté.",
        "Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par des activités qui construisent pour l'avenir. Tes valeurs sont liées à la responsabilité et à la durabilité.",
        "Créer de la clarté dans tes finances",
        "Trois respirations en alignant sécurité et service",
        "Comment ma prospérité peut-elle servir les générations futures ?"),

    ('capricorn', 3): make_neptune_interp('capricorn', 3,
        "Tu communiques avec autorité inspirée — tes mots construisent des structures de pensée durables.",
        "Neptune en Capricorne en Maison 3 te donne une communication qui combine autorité et inspiration. Tu sais présenter des idées de façon à ce qu'elles aient un impact durable.",
        "Le piège : une communication trop rigide ou froide, avoir du mal avec l'informel, confondre sérieux et distance. La vraie communication d'autorité est aussi chaleureuse.",
        "Neptune spiritualise tes échanges d'autorité et de structure. Tu peux avoir un don pour l'écriture qui structure les idées de façon inspirante.",
        "Communiquer avec chaleur et autorité",
        "Trois respirations en servant par les mots structurés",
        "Comment ma communication peut-elle être à la fois autoritaire et chaleureuse ?"),

    ('capricorn', 4): make_neptune_interp('capricorn', 4,
        "Tu rêves d'un foyer de tradition — ta maison devient un lieu où se transmettent les valeurs durables.",
        "Neptune en Capricorne en Maison 4 crée un environnement familial qui honore les traditions tout en les spiritualisant. Ton foyer peut être un lieu de transmission de valeurs.",
        "Le piège : un foyer trop rigide ou austère, confondre tradition et limitation, fuir la chaleur dans le devoir. La vraie maison de tradition est aussi chaleureuse.",
        "Neptune spiritualise ta vie familiale. Tu as peut-être grandi dans un environnement qui valorisait les traditions ou tu crées le tien comme un lieu de transmission.",
        "Créer un moment de chaleur informelle chez toi",
        "Trois respirations en trouvant la tendresse dans la structure",
        "Comment mon foyer peut-il être traditionnel ET chaleureux ?"),

    ('capricorn', 5): make_neptune_interp('capricorn', 5,
        "Tu crées avec ambition spirituelle — tes œuvres visent à laisser une trace durable.",
        "Neptune en Capricorne en Maison 5 te pousse vers une créativité qui construit pour l'avenir. Tu veux que tes œuvres durent, qu'elles aient un impact à long terme.",
        "Le piège : une créativité trop sérieuse qui oublie la joie, des amours basées sur l'ambition, confondre accomplissement et bonheur. La vraie joie créative sait aussi être légère.",
        "Neptune spiritualise tes plaisirs d'accomplissement et de durabilité. Tu peux avoir des amours sérieuses et engagées.",
        "Créer quelque chose de léger et joyeux",
        "Trois respirations en laissant la joie être simple",
        "Comment ma créativité peut-elle être durable ET joyeuse ?"),

    ('capricorn', 6): make_neptune_interp('capricorn', 6,
        "Tu travailles avec dévotion et discipline — ton quotidien devient une pratique de construction patiente.",
        "Neptune en Capricorne en Maison 6 te pousse vers un travail qui construit quelque chose de durable. Tu veux que tes efforts quotidiens contribuent à un édifice plus grand.",
        "Le piège : un travail qui devient obsessionnel, négliger ta santé pour l'accomplissement, confondre devoir et sacrifice. Le vrai travail durable te nourrit aussi.",
        "Neptune spiritualise ton quotidien de discipline et de construction. Tu travailles mieux quand tu vois comment tes efforts servent un but plus grand. Ta santé bénéficie de discipline mais souffre de rigidité.",
        "Prendre soin de toi comme partie du travail",
        "Trois respirations en équilibrant discipline et bien-être",
        "Comment mon travail peut-il être discipliné tout en me nourrissant ?"),

    ('capricorn', 7): make_neptune_interp('capricorn', 7,
        "Tu rêves de partenariats durables — tes relations sont des constructions qui traversent le temps.",
        "Neptune en Capricorne en Maison 7 crée des relations basées sur l'engagement à long terme. Tu attires des partenaires avec qui tu veux construire quelque chose de durable.",
        "Le piège : des relations trop basées sur le devoir, confondre engagement et froideur, avoir du mal avec la spontanéité. Les meilleures relations combinent durabilité et tendresse.",
        "Neptune spiritualise tes partenariats de durabilité et d'engagement. Tu peux avoir des relations qui semblent destinées à durer mais qui demandent aussi de la chaleur.",
        "Créer un moment de spontanéité dans ta relation",
        "Trois respirations en trouvant la tendresse dans l'engagement",
        "Comment mes relations peuvent-elles être durables ET tendres ?"),

    ('capricorn', 8): make_neptune_interp('capricorn', 8,
        "Tu traverses les crises avec endurance — les transformations deviennent des occasions de reconstruire plus solidement.",
        "Neptune en Capricorne en Maison 8 te donne la capacité de traverser les crises avec résilience. Les transformations te poussent à reconstruire sur des bases plus solides.",
        "Le piège : te durcir excessivement face aux crises, avoir du mal à lâcher prise, confondre reconstruction et contrôle. La vraie résilience sait aussi s'adapter.",
        "Neptune spiritualise ta relation aux crises de façon structurante. Tu peux trouver de la force et de la structure dans les épreuves. Ta sexualité peut être liée au pouvoir ou à l'engagement.",
        "Lâcher prise sur quelque chose que tu ne peux pas contrôler",
        "Trois respirations en trouvant la force dans l'abandon",
        "Comment puis-je traverser les crises avec résilience ET flexibilité ?"),

    ('capricorn', 9): make_neptune_interp('capricorn', 9,
        "Tu rêves d'une sagesse structurée — ta philosophie construit des systèmes de pensée durables.",
        "Neptune en Capricorne en Maison 9 te pousse vers des croyances qui structurent et organisent. Tu veux une philosophie qui tient face à l'épreuve du temps, qui peut être enseignée et transmise.",
        "Le piège : des croyances trop rigides ou dogmatiques, confondre structure et vérité, avoir du mal avec le mystère. La vraie sagesse structurée inclut aussi l'incertitude.",
        "Neptune spiritualise ta quête de sens de façon structurante. Tu peux être attiré par des traditions établies ou vouloir créer ta propre structure de sens.",
        "Accueillir une incertitude sans la résoudre",
        "Trois respirations en trouvant la paix dans le mystère",
        "Comment ma sagesse peut-elle être structurée tout en accueillant le mystère ?"),

    ('capricorn', 10): make_neptune_interp('capricorn', 10,
        "Tu rêves d'une carrière de service durable — ta réussite laisse une trace positive dans le monde.",
        "Neptune en Capricorne en Maison 10 te pousse vers une carrière qui construit quelque chose de durable pour le bien commun. Tu veux que ta réussite serve les générations futures.",
        "Le piège : une carrière qui devient obsessionnelle, confondre statut et service, avoir du mal à déléguer. La vraie réussite durable sait aussi collaborer.",
        "Neptune spiritualise ta carrière et ta réputation de durabilité. On te reconnaît pour ta capacité à construire des choses qui durent. Ta carrière peut sembler suivre un chemin de responsabilité.",
        "Collaborer plutôt que tout porter seul",
        "Trois respirations en partageant la construction",
        "Comment ma carrière peut-elle laisser une trace tout en collaborant ?"),

    ('capricorn', 11): make_neptune_interp('capricorn', 11,
        "Tu rêves de communautés durables — tes amitiés et tes projets construisent des structures qui servent l'avenir.",
        "Neptune en Capricorne en Maison 11 te connecte à des réseaux de constructeurs et de bâtisseurs. Tes amis partagent ta vision du long terme. Les projets collectifs créent des institutions durables.",
        "Le piège : des amitiés trop formelles ou basées sur l'intérêt, des projets qui deviennent des institutions rigides, confondre structure et communauté. Les meilleures communautés ont aussi de la chaleur.",
        "Neptune spiritualise tes réseaux et tes projets de construction durable. Tu es fait pour les organisations qui construisent pour l'avenir.",
        "Créer un moment informel avec tes amis",
        "Trois respirations en trouvant la chaleur dans la structure",
        "Comment mes réseaux peuvent-ils être durables ET chaleureux ?"),

    ('capricorn', 12): make_neptune_interp('capricorn', 12,
        "Tu rêves d'une maîtrise intérieure — ton inconscient te guide vers une discipline spirituelle profonde.",
        "Neptune en Capricorne en Maison 12 crée des connexions entre ta discipline et les dimensions invisibles. Ta pratique spirituelle peut être structurée et mener à une maîtrise intérieure.",
        "Le piège : contrôler la vie intérieure au lieu de l'accueillir, confondre maîtrise et rigidité, avoir du mal avec l'abandon spirituel. La vraie discipline intérieure sait aussi lâcher prise.",
        "Neptune spiritualise au maximum ta connexion à l'invisible de façon structurée. Tu peux avoir une pratique méditative disciplinée qui mène à des percées profondes.",
        "Lâcher le contrôle dans ta pratique spirituelle",
        "Trois respirations en trouvant la liberté dans la discipline",
        "Comment ma discipline spirituelle peut-elle mener à l'abandon ?"),

    # AQUARIUS - 12 maisons
    ('aquarius', 1): make_neptune_interp('aquarius', 1,
        "Tu incarnes un rêve de liberté collective — ton identité cherche à fusionner originalité et compassion universelle.",
        "Neptune en Verseau en Maison 1 te donne une personnalité qui rêve d'un monde meilleur pour tous. Tu veux être unique tout en servant l'humanité.",
        "Le piège : une identité qui se perd dans les causes, confondre excentricité et authenticité, fuir l'intimité dans les grandes visions. La vraie originalité compassionnelle inclut aussi le personnel.",
        "Neptune adoucit et spiritualise ton originalité. Tu projettes une image de visionnaire humaniste. Ton apparence peut refléter ta connexion à l'avant-garde et au collectif.",
        "Créer une connexion personnelle intime",
        "Trois respirations en équilibrant universel et personnel",
        "Comment mon originalité peut-elle servir l'humanité tout en restant personnelle ?"),

    ('aquarius', 2): make_neptune_interp('aquarius', 2,
        "Tu rêves d'une prospérité collective — tes ressources servent à créer un monde meilleur pour tous.",
        "Neptune en Verseau en Maison 2 crée une relation idéaliste à l'argent orientée vers le collectif. Tu veux que tes revenus servent l'humanité, pas seulement toi.",
        "Le piège : négliger tes propres besoins pour les causes, des finances floues par excès d'idéalisme, confondre générosité et sacrifice. La vraie prospérité collective inclut aussi ta propre sécurité.",
        "Neptune spiritualise ta relation aux ressources. Tu peux gagner de l'argent par des activités qui servent le collectif. Tes valeurs sont liées à la liberté et au bien commun.",
        "Prendre soin de ta propre sécurité financière",
        "Trois respirations en incluant tes besoins dans le collectif",
        "Comment ma prospérité peut-elle servir l'humanité ET mes propres besoins ?"),

    ('aquarius', 3): make_neptune_interp('aquarius', 3,
        "Tu communiques avec une vision collective — tes mots éveillent la conscience de notre humanité partagée.",
        "Neptune en Verseau en Maison 3 te donne une communication qui touche à l'universel. Tu sais présenter des idées qui concernent l'humanité entière, qui éveillent la conscience collective.",
        "Le piège : une communication trop abstraite, avoir du mal avec les échanges personnels, confondre vision et détachement. La vraie communication collective inclut aussi le personnel.",
        "Neptune spiritualise tes échanges de vision collective. Tu peux avoir un don pour la communication qui éveille les consciences.",
        "Avoir une conversation personnelle et intime",
        "Trois respirations en trouvant l'universel dans le personnel",
        "Comment ma communication peut-elle être universelle ET personnelle ?"),

    ('aquarius', 4): make_neptune_interp('aquarius', 4,
        "Tu rêves d'un foyer ouvert sur l'humanité — ta maison devient un lieu où se rencontrent toutes les différences.",
        "Neptune en Verseau en Maison 4 crée un environnement familial ouvert et inclusif. Ton foyer peut accueillir des personnes de tous horizons, être un lieu d'expérimentation sociale.",
        "Le piège : un foyer qui manque d'intimité, fuir les liens familiaux dans les grandes causes, confondre ouverture et déracinement. La vraie maison inclusive a aussi des liens profonds.",
        "Neptune spiritualise ta vie familiale. Tu as peut-être grandi dans un environnement non conventionnel ou tu crées le tien comme un laboratoire social.",
        "Créer un moment d'intimité familiale profonde",
        "Trois respirations en ancrant l'ouverture dans l'intimité",
        "Comment mon foyer peut-il être ouvert sur le monde ET intime ?"),

    ('aquarius', 5): make_neptune_interp('aquarius', 5,
        "Tu crées avec une vision collective — tes œuvres et tes amours servent l'évolution de l'humanité.",
        "Neptune en Verseau en Maison 5 te pousse vers une créativité qui sert le collectif. Tu veux que tes œuvres éveillent les consciences. En amour, tu cherches des partenaires avec qui tu partages une vision pour l'humanité.",
        "Le piège : des amours trop détachées, une créativité qui oublie la joie personnelle, confondre mission et plaisir. La vraie joie créative collective inclut aussi le bonheur personnel.",
        "Neptune spiritualise tes plaisirs de vision et de service collectif. Tu peux avoir des amours basées sur des idéaux partagés.",
        "Créer quelque chose juste pour ton propre plaisir",
        "Trois respirations en trouvant la joie personnelle",
        "Comment ma créativité peut-elle servir l'humanité ET me rendre heureux ?"),

    ('aquarius', 6): make_neptune_interp('aquarius', 6,
        "Tu travailles avec une vision humanitaire — ton quotidien devient un service à l'évolution collective.",
        "Neptune en Verseau en Maison 6 te pousse vers un travail qui sert l'humanité. Tu veux que tes efforts quotidiens contribuent à un monde meilleur pour tous.",
        "Le piège : te sacrifier au service des causes, un travail qui néglige tes propres besoins, confondre service et martyre. Le vrai service humanitaire te nourrit aussi.",
        "Neptune spiritualise ton quotidien de service collectif. Tu travailles mieux quand tu sens que tu contribues à l'évolution de l'humanité. Ta santé peut être sensible aux énergies collectives.",
        "Prendre soin de tes propres besoins au quotidien",
        "Trois respirations en incluant ton bien-être dans le service",
        "Comment mon travail peut-il servir l'humanité tout en me nourrissant ?"),

    ('aquarius', 7): make_neptune_interp('aquarius', 7,
        "Tu rêves de partenariats d'évolution — tes relations sont des collaborations pour le bien de l'humanité.",
        "Neptune en Verseau en Maison 7 crée des relations basées sur une vision partagée de l'humanité. Tu attires des partenaires avec qui tu veux changer le monde ensemble.",
        "Le piège : des relations qui manquent d'intimité personnelle, fuir l'engagement dans les grandes causes, confondre mission commune et amour. Les meilleures relations combinent vision et intimité.",
        "Neptune spiritualise tes partenariats de vision collective. Tu peux avoir des relations avec des âmes sœurs humanitaires.",
        "Créer un moment d'intimité qui n'a rien à voir avec vos causes",
        "Trois respirations en trouvant l'amour au-delà de la mission",
        "Comment mes relations peuvent-elles avoir une vision ET une intimité ?"),

    ('aquarius', 8): make_neptune_interp('aquarius', 8,
        "Tu traverses les crises avec une vision collective — les transformations te connectent à l'évolution de l'humanité.",
        "Neptune en Verseau en Maison 8 te donne la capacité de voir les crises personnelles dans le contexte de l'évolution collective. Les transformations te reconnectent à quelque chose de plus grand.",
        "Le piège : te détacher émotionnellement des crises, fuir l'intimité des transformations, confondre détachement et éveil. La vraie transformation collective inclut aussi le personnel.",
        "Neptune spiritualise ta relation aux crises de façon collective. Tu peux avoir des insights sur les transformations de l'humanité. Ta sexualité peut être expérimentale ou détachée.",
        "Traverser une transformation de façon personnelle et intime",
        "Trois respirations en accueillant l'émotion dans la transformation",
        "Comment mes crises personnelles me connectent-elles à l'humanité ?"),

    ('aquarius', 9): make_neptune_interp('aquarius', 9,
        "Tu rêves d'une sagesse universelle — ta philosophie embrasse l'évolution de toute l'humanité.",
        "Neptune en Verseau en Maison 9 te pousse vers des croyances qui concernent l'avenir de l'humanité. Tu ne te satisfais pas des philosophies individualistes — tu veux comprendre où nous allons tous ensemble.",
        "Le piège : des croyances trop abstraites, confondre utopie et sagesse, avoir du mal avec le chemin personnel. La vraie sagesse universelle inclut aussi la voie individuelle.",
        "Neptune spiritualise ta quête de sens de façon collective. Tu peux être attiré par des philosophies du futur, des visions de l'humanité évoluée.",
        "Explorer ton propre chemin spirituel unique",
        "Trois respirations en honorant ta voie personnelle",
        "Comment ma sagesse peut-elle embrasser l'humanité tout en honorant mon chemin unique ?"),

    ('aquarius', 10): make_neptune_interp('aquarius', 10,
        "Tu rêves d'une carrière humanitaire — ta réussite sert l'évolution de l'humanité entière.",
        "Neptune en Verseau en Maison 10 te pousse vers une carrière qui change le monde. Tu veux que ta réussite serve l'humanité, contribue à un futur meilleur pour tous.",
        "Le piège : une carrière qui se perd dans les utopies, confondre vision et accomplissement, avoir du mal avec les aspects pratiques de la réussite. La vraie réussite humanitaire est aussi concrète.",
        "Neptune spiritualise ta carrière et ta réputation de vision collective. On te reconnaît pour ta capacité à voir le futur de l'humanité. Ta carrière peut être dans l'humanitaire ou l'innovation sociale.",
        "Concrétiser un aspect de ta vision humanitaire",
        "Trois respirations en incarnant ta vision",
        "Comment ma carrière peut-elle servir l'humanité de façon concrète ?"),

    ('aquarius', 11): make_neptune_interp('aquarius', 11,
        "Tu rêves de l'humanité unie — tes amitiés et tes projets créent des ponts entre tous les êtres.",
        "Neptune en Verseau en Maison 11 amplifie au maximum ta connexion aux réseaux humanitaires. Tu te sens chez toi dans les groupes qui travaillent pour l'humanité. Les projets collectifs sont ta passion.",
        "Le piège : préférer les idéaux aux personnes réelles, des amitiés superficielles par excès de réseautage, confondre mouvement et connexion. Les meilleures communautés honorent aussi les individus.",
        "Neptune spiritualise au maximum tes réseaux et tes projets collectifs. Tu es fait pour les mouvements qui changent le monde, les associations humanitaires.",
        "Créer une connexion profonde avec un ami en particulier",
        "Trois respirations en honorant l'individu dans le collectif",
        "Comment mes réseaux peuvent-ils honorer à la fois l'humanité et les individus ?"),

    ('aquarius', 12): make_neptune_interp('aquarius', 12,
        "Tu rêves de la conscience collective — ton inconscient est connecté à l'âme de l'humanité.",
        "Neptune en Verseau en Maison 12 crée des connexions profondes entre ton inconscient et la conscience collective de l'humanité. Tu peux percevoir les courants de l'évolution humaine.",
        "Le piège : te perdre dans les visions collectives, fuir l'intimité personnelle, confondre détachement et éveil. La vraie conscience collective inclut aussi le cœur personnel.",
        "Neptune spiritualise au maximum ta connexion à l'invisible collectif. Tu peux avoir des visions qui concernent l'avenir de l'humanité. Les pratiques spirituelles en groupe te conviennent.",
        "Méditer sur ton propre cœur plutôt que sur l'humanité",
        "Trois respirations en revenant à ton centre personnel",
        "Comment puis-je rester connecté à l'humanité tout en honorant mon cœur ?"),

    # PISCES - 12 maisons
    ('pisces', 1): make_neptune_interp('pisces', 1,
        "Tu incarnes l'océan de la compassion — ton identité se dissout dans l'amour universel.",
        "Neptune en Poissons en Maison 1 amplifie au maximum ta sensibilité et ta connexion au tout. Tu es une éponge émotionnelle qui absorbe tout. Ta compassion est sans limites.",
        "Le piège : une identité qui se perd complètement, absorber les émotions des autres sans protection, confondre dissolution et amour. La vraie compassion infinie a aussi des frontières.",
        "Neptune est chez lui et amplifie ta sensibilité de façon maximale. Tu projettes une image de douceur mystique. Ton apparence peut sembler éthérée ou changeante.",
        "Créer une limite protectrice autour de toi",
        "Trois respirations en établissant une frontière douce",
        "Comment puis-je être infiniment compatissant tout en me protégeant ?"),

    ('pisces', 2): make_neptune_interp('pisces', 2,
        "Tu rêves d'une abondance infinie — tes ressources viennent de sources invisibles et sans limites.",
        "Neptune en Poissons en Maison 2 crée une relation mystique à l'argent. Tu peux recevoir de façon miraculeuse, attirer l'abondance par la foi. Mais tu peux aussi tout donner.",
        "Le piège : une relation complètement floue à l'argent, donner tout sans discernement, confondre foi et irresponsabilité. La vraie abondance mystique a aussi de la structure.",
        "Neptune spiritualise au maximum ta relation aux ressources. Tu peux gagner de l'argent par des activités spirituelles, artistiques ou de guérison. Tes valeurs sont liées à l'amour universel.",
        "Créer une structure simple pour tes finances",
        "Trois respirations en ancrant l'abondance",
        "Comment puis-je avoir foi en l'abondance tout en étant responsable ?"),

    ('pisces', 3): make_neptune_interp('pisces', 3,
        "Tu communiques avec l'invisible — tes mots touchent les dimensions qui échappent aux mots.",
        "Neptune en Poissons en Maison 3 te donne une communication qui touche au-delà du verbal. Tu perçois ce qui n'est pas dit, tu exprimes l'inexprimable. La poésie et l'art sont tes langages.",
        "Le piège : une communication trop floue pour être comprise, te perdre dans les impressions, confondre intuition et confusion. La vraie communication mystique peut aussi être claire.",
        "Neptune spiritualise au maximum tes échanges. Tu peux avoir des liens psychiques avec ton entourage. L'écriture intuitive ou automatique peut être une voie.",
        "Communiquer quelque chose de façon claire et simple",
        "Trois respirations en donnant forme à l'informe",
        "Comment puis-je exprimer l'inexprimable de façon accessible ?"),

    ('pisces', 4): make_neptune_interp('pisces', 4,
        "Tu rêves du foyer divin — ta maison est un temple où l'invisible devient tangible.",
        "Neptune en Poissons en Maison 4 crée un environnement familial profondément spirituel. Ton foyer peut être un sanctuaire, un lieu où les voiles entre les mondes sont minces.",
        "Le piège : un foyer qui perd tout ancrage dans la réalité, absorber les problèmes familiaux sans limite, fuir les difficultés dans le rêve. La vraie maison sacrée a aussi des fondations.",
        "Neptune spiritualise au maximum ta vie familiale. Tu as peut-être grandi dans un environnement très sensible ou mystique. Ton foyer est un lieu de ressourcement spirituel profond.",
        "Créer une structure simple et sécurisante chez toi",
        "Trois respirations en ancrant le sacré dans le concret",
        "Comment mon foyer peut-il être un sanctuaire qui me protège aussi ?"),

    ('pisces', 5): make_neptune_interp('pisces', 5,
        "Tu crées avec l'infini — tes œuvres et tes amours sont des expériences de fusion avec le tout.",
        "Neptune en Poissons en Maison 5 te pousse vers une créativité qui touche au transcendant. Tu veux que tes œuvres soient des portes vers l'invisible. En amour, tu cherches la fusion totale.",
        "Le piège : idéaliser les partenaires au point de nier la réalité, une créativité qui reste dans les rêves, confondre fusion et amour. La vraie joie créative s'incarne aussi.",
        "Neptune spiritualise au maximum tes plaisirs et ta créativité. Tu peux avoir des amours transcendantes mais qui peuvent manquer d'ancrage.",
        "Concrétiser une création qui te tient à cœur",
        "Trois respirations en incarnant le rêve",
        "Comment ma créativité peut-elle toucher l'infini tout en s'incarnant ?"),

    ('pisces', 6): make_neptune_interp('pisces', 6,
        "Tu travailles avec dévotion totale — ton quotidien est un service à l'invisible et à la guérison.",
        "Neptune en Poissons en Maison 6 te pousse vers des métiers de guérison spirituelle. Tu veux que ton travail touche les dimensions invisibles de la souffrance, que tes soins guérissent l'âme.",
        "Le piège : absorber toutes les souffrances, te sacrifier totalement, confondre service et martyrisationn. Le vrai service de guérison te protège aussi.",
        "Neptune spiritualise au maximum ton quotidien. Tu travailles mieux dans des environnements paisibles et spirituels. Ta santé est extrêmement sensible aux énergies.",
        "Protéger fermement ton énergie dans le service",
        "Trois respirations en créant un bouclier de lumière",
        "Comment puis-je servir la guérison tout en me préservant totalement ?"),

    ('pisces', 7): make_neptune_interp('pisces', 7,
        "Tu rêves de la fusion totale — tes relations sont des unions d'âmes sans frontières.",
        "Neptune en Poissons en Maison 7 crée des relations de fusion profonde. Tu attires des partenaires avec qui tu veux ne faire qu'un, te dissoudre dans l'amour.",
        "Le piège : te perdre complètement dans l'autre, des relations sans limites qui deviennent destructrices, confondre fusion et codépendance. Les meilleures relations gardent aussi deux individus.",
        "Neptune spiritualise au maximum tes partenariats. Tu peux avoir des relations karmiques ou des connexions d'âmes profondes qui demandent beaucoup de conscience.",
        "Maintenir ton identité dans la relation",
        "Trois respirations en restant toi dans l'union",
        "Comment mes relations peuvent-elles être profondes tout en respectant mon individualité ?"),

    ('pisces', 8): make_neptune_interp('pisces', 8,
        "Tu traverses les crises comme des dissolutions — les transformations te reconnectent à l'océan de la conscience.",
        "Neptune en Poissons en Maison 8 te donne une capacité extraordinaire à lâcher prise. Les transformations sont des occasions de te fondre dans quelque chose de plus grand. La mort symbolique est une porte.",
        "Le piège : te dissoudre dans les crises au lieu de les traverser, fuir la réalité dans la transcendance, avoir du mal à agir concrètement. La vraie transformation spirituelle inclut aussi l'action.",
        "Neptune spiritualise au maximum ta relation aux mystères et aux transformations. Tu peux avoir des expériences de mort-renaissance spirituelle. Ta sexualité peut être transcendante.",
        "Prendre une action concrète face à une transformation",
        "Trois respirations en alliant transcendance et action",
        "Comment puis-je me dissoudre dans les transformations tout en agissant ?"),

    ('pisces', 9): make_neptune_interp('pisces', 9,
        "Tu rêves de l'union avec le divin — ta quête de sens est une immersion dans l'océan de la conscience.",
        "Neptune en Poissons en Maison 9 amplifie au maximum ta soif de transcendance. Tu ne veux pas comprendre le divin — tu veux te fondre en lui. La mystique est ta voie.",
        "Le piège : te perdre dans des états altérés, fuir la réalité dans la spiritualité, confondre dissolution et éveil. La vraie union mystique revient aussi à la vie ordinaire.",
        "Neptune spiritualise au maximum ta quête de sens. Tu peux avoir des expériences mystiques profondes, des visions, des états de conscience élargie.",
        "Revenir à la vie ordinaire après une expérience spirituelle",
        "Trois respirations en intégrant le transcendant dans le quotidien",
        "Comment puis-je toucher l'infini tout en restant présent à la vie ?"),

    ('pisces', 10): make_neptune_interp('pisces', 10,
        "Tu rêves d'une carrière de service divin — ta réussite est une dévotion totale au plus grand.",
        "Neptune en Poissons en Maison 10 te pousse vers une carrière qui sert quelque chose de transcendant. Tu ne cherches pas la gloire — tu cherches à être un canal pour le divin.",
        "Le piège : une carrière qui se perd dans les rêves, te sacrifier professionnellement, confondre vocation et exploitation. La vraie réussite spirituelle est aussi reconnue et rémunérée.",
        "Neptune spiritualise au maximum ta carrière et ta réputation. On te reconnaît pour ta capacité à toucher l'invisible. Ta carrière peut être dans les arts, la spiritualité, la guérison.",
        "Recevoir juste reconnaissance pour ton travail",
        "Trois respirations en acceptant d'être vu et valorisé",
        "Comment ma carrière peut-elle servir le divin tout en étant reconnue ?"),

    ('pisces', 11): make_neptune_interp('pisces', 11,
        "Tu rêves de l'humanité une — tes amitiés et tes projets dissolvent toutes les frontières entre les êtres.",
        "Neptune en Poissons en Maison 11 te connecte à des réseaux de compassion universelle. Tes amis sont des âmes sœurs avec qui tu partages l'amour inconditionnel. Les projets collectifs guérissent le monde.",
        "Le piège : te perdre dans les besoins du groupe, des amitiés sans limites qui épuisent, absorber les souffrances collectives. Les meilleures communautés protègent aussi leurs membres.",
        "Neptune spiritualise au maximum tes réseaux et tes projets. Tu es fait pour les cercles de guérison, les communautés spirituelles, les projets de compassion universelle.",
        "Protéger ton énergie dans le collectif",
        "Trois respirations en créant une limite dans l'amour",
        "Comment puis-je aimer l'humanité tout en me préservant ?"),

    ('pisces', 12): make_neptune_interp('pisces', 12,
        "Tu habites l'océan infini — ton inconscient EST l'océan de la conscience universelle.",
        "Neptune en Poissons en Maison 12 est la position de connexion maximale à l'invisible. Tu n'as pas accès à l'inconscient collectif — tu EN ES. Tu es une goutte qui sait qu'elle est l'océan.",
        "Le piège : te dissoudre complètement, avoir du mal avec la vie incarnée, confondre dissolution et éveil. La vraie transcendance inclut aussi le retour au rivage.",
        "Neptune est au maximum de sa puissance spirituelle. Tu peux avoir des expériences mystiques profondes et continues. Tu es un canal naturel pour l'invisible.",
        "Revenir au rivage après l'immersion",
        "Trois respirations en retrouvant ton corps",
        "Comment puis-je habiter l'océan tout en retrouvant le rivage ?"),
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
