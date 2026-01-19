#!/usr/bin/env python3
"""Script d'insertion des interprétations Saturn/Aquarius et Pisces en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

SATURN_INTERPRETATIONS = {
    # AQUARIUS - 12 maisons
    ('aquarius', 1): """# ♄ Saturne en Verseau
**En une phrase :** Tu incarnes une vision structurée du futur — ta différence devient ta force quand tu l'ancres dans la réalité.

## Ton moteur
Saturne en Verseau en Maison 1 te demande d'incarner tes idéaux progressistes avec discipline. Tu ne peux pas juste rêver d'un monde meilleur — tu dois le construire méthodiquement. Cette configuration forge des innovateurs qui passent de l'idée à l'action.

## Ton défi
Le piège : osciller entre conformisme et rébellion, avoir du mal à intégrer ta différence, rejeter les structures tout en les recréant. La vraie liberté s'appuie sur une structure choisie.

## Maison 1 en Verseau
Saturne structure ton apparence d'innovateur. Tu projettes une image de sérieux dans ta différence, de détermination dans ton originalité. Ton corps peut refléter une tension entre convention et rupture.

## Micro-rituel du jour (2 min)
- Identifier un aspect unique de toi que tu assumes pleinement
- Trois respirations en ancrant ta vision dans le présent
- Journal : « Comment ma différence sert-elle concrètement le monde ? »""",

    ('aquarius', 2): """# ♄ Saturne en Verseau
**En une phrase :** Tu construis ta prospérité de façon innovante — l'abondance vient quand tu trouves des voies nouvelles et structurées.

## Ton moteur
Saturne en Verseau en Maison 2 te pousse à créer des revenus par l'innovation et la technologie. Tu dois structurer tes idées révolutionnaires pour qu'elles génèrent de la valeur. Les métiers du futur, de la tech, de l'innovation sociale peuvent être lucratifs mais demandent de la méthode.

## Ton défi
Le piège : avoir des idées brillantes mais pas les moyens de les monétiser, être trop détaché du concret financier, confondre innovation et instabilité. La vraie prospérité innovante est aussi durable.

## Maison 2 en Verseau
Saturne structure tes finances autour de l'innovation. Tes revenus peuvent venir de domaines de pointe ou de sources atypiques. Tes valeurs sont liées à la liberté et au collectif, mais tu apprends à les ancrer.

## Micro-rituel du jour (2 min)
- Identifier une idée innovante et structurer une façon de la valoriser
- Trois respirations en connectant innovation et stabilité
- Journal : « Quelle innovation pourrait devenir une source de revenus ? »""",

    ('aquarius', 3): """# ♄ Saturne en Verseau
**En une phrase :** Tu communiques avec une vision structurée — tes idées progressistes gagnent en impact quand elles sont clairement articulées.

## Ton moteur
Saturne en Verseau en Maison 3 te demande de discipliner ta communication innovante. Tu dois apprendre à rendre tes idées avant-gardistes accessibles, à argumenter solidement tes visions. Cette configuration favorise les métiers de la tech, de la communication de rupture, de l'enseignement innovant.

## Ton défi
Le piège : communiquer de façon trop abstraite ou futuriste, avoir du mal à être compris, rejeter les formes de communication traditionnelles. La vraie innovation sait aussi utiliser les canaux existants.

## Maison 3 en Verseau
Saturne structure tes échanges autour de l'innovation. Tes relations avec frères, sœurs et voisins peuvent être distantes mais connectées par la technologie. Tu apprends par l'expérimentation structurée.

## Micro-rituel du jour (2 min)
- Expliquer une idée innovante de façon simple et claire
- Trois respirations en rendant ta vision accessible
- Journal : « Comment puis-je mieux communiquer mes idées nouvelles ? »""",

    ('aquarius', 4): """# ♄ Saturne en Verseau
**En une phrase :** Tu construis un foyer qui incarne le futur — ta maison devient un laboratoire structuré de nouvelles façons de vivre.

## Ton moteur
Saturne en Verseau en Maison 4 te demande de créer un chez-toi qui reflète tes valeurs innovantes tout en étant stable. Tu peux expérimenter des formes de vie alternatives, mais tu as besoin d'une base solide pour le faire.

## Ton défi
Le piège : avoir du mal à créer des racines par idéalisation de la liberté, rejeter les traditions familiales sans discernement, vivre dans un foyer chaotique au nom de l'originalité. Le vrai progrès inclut aussi la stabilité.

## Maison 4 en Verseau
Saturne structure ta vie familiale autour de l'innovation. Tu as peut-être grandi dans une famille non conventionnelle ou tu crées la tienne selon des règles nouvelles mais structurées. Ton foyer peut être un lieu de rassemblement.

## Micro-rituel du jour (2 min)
- Identifier un aspect innovant de ton foyer qui te stabilise
- Trois respirations en ancrant ta liberté dans ton chez-toi
- Journal : « Comment mon foyer reflète-t-il mes valeurs tout en me stabilisant ? »""",

    ('aquarius', 5): """# ♄ Saturne en Verseau
**En une phrase :** Tu crées avec une vision structurée — tes œuvres innovantes deviennent des contributions durables au futur.

## Ton moteur
Saturne en Verseau en Maison 5 te demande de discipliner ta créativité avant-gardiste. Tu ne crées pas juste pour expérimenter mais pour construire quelque chose de durable. En amour, tu cherches des partenaires qui partagent ta vision tout en t'ancrant.

## Ton défi
Le piège : transformer la créativité en projet trop sérieux, avoir du mal avec la légèreté du jeu, choisir des partenaires uniquement sur des critères intellectuels. La vraie joie créative inclut aussi la spontanéité.

## Maison 5 en Verseau
Saturne structure tes plaisirs autour de l'innovation. Tu peux être attiré par des partenaires intellectuels ou excentriques mais stables. Ta créativité s'épanouit dans les projets technologiques ou expérimentaux mais structurés.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui allie innovation et simplicité
- Trois respirations en laissant la joie être légère même dans l'originalité
- Journal : « Quelle création innovante me procure vraiment du plaisir ? »""",

    ('aquarius', 6): """# ♄ Saturne en Verseau
**En une phrase :** Tu travailles avec méthode et innovation — ton efficacité vient de ta capacité à structurer de nouvelles façons de faire.

## Ton moteur
Saturne en Verseau en Maison 6 te pousse à réinventer le travail de façon structurée. Tu excelles dans les environnements qui combinent innovation et organisation. Cette configuration favorise les métiers de la tech, de l'innovation des processus, de l'amélioration continue.

## Ton défi
Le piège : vouloir tout révolutionner au lieu d'améliorer progressivement, avoir du mal avec les routines même nécessaires, confondre innovation et désorganisation. L'efficacité innovante est aussi fiable.

## Maison 6 en Verseau
Saturne structure ton quotidien autour de l'amélioration continue. Tu travailles mieux avec de l'autonomie et des méthodes innovantes mais claires. Ta santé peut bénéficier d'approches technologiques ou alternatives structurées.

## Micro-rituel du jour (2 min)
- Identifier une amélioration de routine qui pourrait être implémentée
- Trois respirations en acceptant que l'innovation prend du temps
- Journal : « Quelle petite innovation pourrait améliorer mon quotidien ? »""",

    ('aquarius', 7): """# ♄ Saturne en Verseau
**En une phrase :** Tu construis des partenariats sur des visions partagées — les relations durables sont celles qui allient liberté et engagement.

## Ton moteur
Saturne en Verseau en Maison 7 te demande de bâtir des relations qui respectent l'individualité de chacun tout en créant quelque chose de durable. Tu as besoin de partenaires qui comprennent ton besoin de liberté et qui partagent ta vision du futur.

## Ton défi
Le piège : fuir l'engagement par idéalisation de la liberté, choisir des partenaires uniquement sur des critères intellectuels, avoir du mal avec l'intimité traditionnelle. Les meilleures relations combinent indépendance et connexion profonde.

## Maison 7 en Verseau
Saturne structure tes partenariats autour de valeurs partagées et de respect mutuel. Tu peux avoir des mariages ou des associations non conventionnels mais stables. Tes contrats bénéficient d'une approche innovante mais fiable.

## Micro-rituel du jour (2 min)
- Exprimer à un partenaire ce que tu apprécies dans votre équilibre liberté-connexion
- Trois respirations en honorant à la fois l'indépendance et le lien
- Journal : « Comment mes partenariats allient-ils liberté et engagement ? »""",

    ('aquarius', 8): """# ♄ Saturne en Verseau
**En une phrase :** Tu traverses les crises avec une vision détachée — les transformations deviennent des occasions de réinventer les structures.

## Ton moteur
Saturne en Verseau en Maison 8 te donne une capacité à voir les crises avec recul et à en tirer des innovations. Tu ne subis pas les transformations — tu les utilises pour construire quelque chose de nouveau. Les ressources partagées peuvent venir de projets innovants.

## Ton défi
Le piège : te détacher excessivement des crises au lieu de les traverser émotionnellement, intellectualiser les transformations, avoir du mal avec l'intensité intime. La vraie résilience inclut aussi les émotions.

## Maison 8 en Verseau
Saturne structure ta relation aux transformations de façon innovante. Tu excelles dans la restructuration, la réinvention après les crises. Ta sexualité peut être liée à l'expérimentation structurée ou au détachement.

## Micro-rituel du jour (2 min)
- Identifier ce qu'une crise récente t'a permis de restructurer
- Trois respirations en accueillant les émotions dans la transformation
- Journal : « Quelle innovation est née d'une difficulté passée ? »""",

    ('aquarius', 9): """# ♄ Saturne en Verseau
**En une phrase :** Tu construis ta sagesse sur des idées progressistes — ta philosophie est une vision structurée du futur.

## Ton moteur
Saturne en Verseau en Maison 9 te pousse vers une quête de sens qui remet en question les paradigmes établis de façon rigoureuse. Tu ne te satisfais pas des sagesses traditionnelles — tu veux une philosophie qui prépare l'avenir. Les études peuvent être dans des domaines de pointe.

## Ton défi
Le piège : rejeter la tradition sans discernement, adhérer à des utopies irréalistes, confondre nouveauté et vérité. La vraie sagesse intègre passé et futur.

## Maison 9 en Verseau
Saturne structure ta quête de sens autour de l'innovation. Tu peux devenir un expert dans un domaine de pointe. Les voyages peuvent être liés à des projets innovants ou des conférences technologiques.

## Micro-rituel du jour (2 min)
- Explorer une idée progressiste avec rigueur et discernement
- Trois respirations en intégrant tradition et innovation
- Journal : « Quelle vision du futur guide ma quête de sens ? »""",

    ('aquarius', 10): """# ♄ Saturne en Verseau
**En une phrase :** Tu construis une carrière visionnaire — ta réussite vient quand tu incarnes le changement de façon structurée.

## Ton moteur
Saturne en Verseau en Maison 10 te pousse vers une carrière qui change le monde de façon concrète. Tu ne veux pas juste innover, tu veux que ton innovation ait un impact durable. Cette configuration favorise les carrières dans la tech, l'innovation sociale, le leadership progressiste.

## Ton défi
Le piège : être trop en avance sur ton temps pour être reconnu, avoir du mal avec les hiérarchies traditionnelles, confondre provocation et leadership. Le vrai impact sait aussi travailler avec le système.

## Maison 10 en Verseau
Saturne structure ta réputation autour de ta capacité à innover de façon fiable. On te reconnaît pour tes idées avant-gardistes et ta capacité à les mettre en œuvre. Ta carrière peut impliquer des responsabilités dans le changement.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière contribue à un changement positif et durable
- Trois respirations en alignant vision et action concrète
- Journal : « Quel impact innovant ai-je envie d'avoir dans mon domaine ? »""",

    ('aquarius', 11): """# ♄ Saturne en Verseau
**En une phrase :** Tu construis des réseaux visionnaires — tes amitiés et tes projets collectifs sont des structures pour le changement.

## Ton moteur
Saturne en Verseau en Maison 11 est une position puissante pour l'action collective structurée. Tu ne te contentes pas de rêver d'un monde meilleur — tu construis les réseaux et les projets qui le créent. Cette configuration favorise le leadership dans les mouvements progressistes.

## Ton défi
Le piège : être trop sélectif ou exigeant dans tes amitiés, imposer ta vision aux groupes, confondre réseau professionnel et amitié. Les meilleures communautés accueillent aussi la diversité.

## Maison 11 en Verseau
Saturne structure au maximum tes réseaux innovants. Tes amis peuvent être des experts, des innovateurs, des activistes engagés. Tes projets humanitaires sont bien organisés et visent des résultats concrets de changement.

## Micro-rituel du jour (2 min)
- Contribuer concrètement à un projet collectif qui te tient à cœur
- Trois respirations en honorant la force du groupe organisé
- Journal : « Quel projet collectif mérite mon engagement structuré ? »""",

    ('aquarius', 12): """# ♄ Saturne en Verseau
**En une phrase :** Tu explores l'invisible avec une vision progressiste — ta spiritualité est connectée à la conscience collective de l'humanité.

## Ton moteur
Saturne en Verseau en Maison 12 te demande de structurer ta connexion à l'inconscient collectif. Tu peux percevoir les courants d'évolution de l'humanité et travailler à les incarner. Cette configuration crée des visionnaires qui canalisent les besoins de l'époque.

## Ton défi
Le piège : te perdre dans des visions abstraites du futur, fuir l'intimité personnelle dans les grandes causes, avoir du mal avec les aspects non rationnels de la spiritualité. La vraie vision inclut aussi le cœur.

## Maison 12 en Verseau
Saturne structure ta vie intérieure autour d'une vision collective. Tu peux avoir des intuitions sur l'avenir de l'humanité. Les pratiques spirituelles en groupe ou connectées à une vision planétaire te conviennent.

## Micro-rituel du jour (2 min)
- Méditer sur ta connexion à l'évolution de l'humanité
- Trois respirations en t'ouvrant à l'inconscient collectif
- Journal : « Quelle vision du futur émerge de mon intériorité ? »""",

    # PISCES - 12 maisons
    ('pisces', 1): """# ♄ Saturne en Poissons
**En une phrase :** Tu apprends à incarner ta sensibilité — ta compassion devient une force quand tu lui donnes une structure.

## Ton moteur
Saturne en Poissons en Maison 1 te demande de discipliner ta nature fluide et empathique. Tu dois apprendre à incarner ta sensibilité de façon protégée, à mettre des limites tout en restant ouvert. Cette configuration forge une présence à la fois douce et solide.

## Ton défi
Le piège : te perdre dans les émotions des autres, avoir du mal à définir qui tu es, osciller entre dissolution et rigidité. La vraie compassion a aussi des frontières claires.

## Maison 1 en Poissons
Saturne structure ton apparence de personne sensible. Tu projettes une image de douceur maîtrisée, de mystère contenu. Ton corps peut refléter cette tension entre fluidité et structure.

## Micro-rituel du jour (2 min)
- Identifier une façon dont ta sensibilité t'a servi aujourd'hui
- Trois respirations en visualisant des limites douces mais fermes
- Journal : « Comment puis-je incarner ma compassion tout en me protégeant ? »""",

    ('pisces', 2): """# ♄ Saturne en Poissons
**En une phrase :** Tu construis ta prospérité sur l'intuition — l'abondance vient quand tu structures tes dons subtils.

## Ton moteur
Saturne en Poissons en Maison 2 te demande de donner une forme concrète à tes talents intuitifs et créatifs. Tu ne peux pas juste être sensible — tu dois transformer cette sensibilité en ressources. Les métiers de soin, d'art, de spiritualité peuvent être lucratifs avec de la méthode.

## Ton défi
Le piège : avoir un rapport flou à l'argent, être trop généreux au détriment de toi-même, confondre abondance spirituelle et matérielle. La vraie prospérité demande aussi de l'attention au concret.

## Maison 2 en Poissons
Saturne structure tes finances autour de tes dons intuitifs. Tes revenus peuvent fluctuer mais tu apprends à leur donner une base stable. Tes valeurs sont liées à la compassion et la créativité.

## Micro-rituel du jour (2 min)
- Identifier un don intuitif et réfléchir à comment le valoriser
- Trois respirations en connectant abondance et compassion
- Journal : « Comment puis-je structurer mes talents subtils en ressources ? »""",

    ('pisces', 3): """# ♄ Saturne en Poissons
**En une phrase :** Tu communiques avec profondeur poétique — tes mots gagnent en impact quand tu les ancres dans une forme claire.

## Ton moteur
Saturne en Poissons en Maison 3 te demande de structurer ta communication imagée et intuitive. Tu dois apprendre à être précis tout en restant poétique, à ancrer tes perceptions subtiles dans des mots accessibles. Cette configuration favorise l'écriture artistique disciplinée.

## Ton défi
Le piège : communiquer de façon trop vague ou confuse, avoir du mal à être factuel, te perdre dans les non-dits. La vraie poésie sait aussi être claire.

## Maison 3 en Poissons
Saturne structure tes échanges autour de la perception subtile. Tes relations avec frères, sœurs et voisins peuvent impliquer des non-dits à clarifier. Tu apprends par l'intuition mais tu dois lui donner une forme.

## Micro-rituel du jour (2 min)
- Exprimer une perception intuitive de façon claire et concrète
- Trois respirations en donnant forme à l'invisible
- Journal : « Comment puis-je mieux communiquer mes perceptions subtiles ? »""",

    ('pisces', 4): """# ♄ Saturne en Poissons
**En une phrase :** Tu construis un foyer qui nourrit l'âme — ta maison devient un sanctuaire structuré de paix et de ressourcement.

## Ton moteur
Saturne en Poissons en Maison 4 te demande de créer un chez-toi qui est à la fois un refuge et une base solide. Tu as besoin d'un espace de ressourcement mais aussi de structure dans ta vie familiale. Cette configuration peut impliquer un travail sur des mémoires familiales à guérir.

## Ton défi
Le piège : absorber les problèmes émotionnels de ta famille, avoir du mal à établir des limites chez toi, fuir dans le rêve pour éviter les difficultés domestiques. Le vrai sanctuaire a aussi des murs.

## Maison 4 en Poissons
Saturne structure ta vie familiale autour du ressourcement. Tu as peut-être grandi dans une famille sensible avec des non-dits à clarifier. Ton foyer peut inclure une dimension spirituelle ou artistique structurée.

## Micro-rituel du jour (2 min)
- Créer un moment de paix structurée dans ton espace de vie
- Trois respirations en ancrant le sacré dans ton quotidien
- Journal : « Comment mon foyer peut-il être à la fois refuge et base solide ? »""",

    ('pisces', 5): """# ♄ Saturne en Poissons
**En une phrase :** Tu crées avec profondeur — tes œuvres gagnent en puissance quand tu disciplines ton inspiration.

## Ton moteur
Saturne en Poissons en Maison 5 te demande de structurer ta créativité qui vient de l'au-delà du conscient. Tu dois apprendre à canaliser l'inspiration, à finir ce que tu commences, à transformer les rêves en œuvres. En amour, tu cherches des connexions profondes mais durables.

## Ton défi
Le piège : idéaliser les partenaires au point d'être déçu, commencer des œuvres sans les finir, confondre inspiration et accomplissement. La vraie créativité demande aussi de la discipline.

## Maison 5 en Poissons
Saturne structure tes plaisirs autour de la profondeur. Tu peux être attiré par des partenaires sensibles mais stables. Ta créativité s'épanouit dans les œuvres qui demandent patience et vision à long terme.

## Micro-rituel du jour (2 min)
- T'engager à travailler régulièrement sur un projet créatif inspiré
- Trois respirations en canalisant l'inspiration dans la forme
- Journal : « Quelle œuvre de mon cœur mérite ma discipline ? »""",

    ('pisces', 6): """# ♄ Saturne en Poissons
**En une phrase :** Tu travailles avec compassion structurée — ton service aux autres devient durable quand tu y inclus ta propre protection.

## Ton moteur
Saturne en Poissons en Maison 6 te demande de structurer ton travail de soin et de service. Tu dois apprendre à aider sans te vider, à servir avec des limites claires. Cette configuration favorise les métiers de santé, d'accompagnement, d'art-thérapie — avec une méthode.

## Ton défi
Le piège : absorber les souffrances de ceux que tu aides, négliger ta propre santé pour celle des autres, avoir du mal avec les structures de travail. Le vrai service durable commence par prendre soin de soi.

## Maison 6 en Poissons
Saturne structure ton quotidien autour du service compassionnel. Tu travailles mieux dans des environnements bienveillants mais organisés. Ta santé est sensible aux atmosphères et bénéficie de routines protectrices.

## Micro-rituel du jour (2 min)
- Identifier une façon de servir qui inclut ta propre protection
- Trois respirations en équilibrant donner et recevoir
- Journal : « Comment puis-je aider les autres tout en prenant soin de moi ? »""",

    ('pisces', 7): """# ♄ Saturne en Poissons
**En une phrase :** Tu construis des partenariats sur la compassion — les relations durables sont celles qui allient profondeur et limites saines.

## Ton moteur
Saturne en Poissons en Maison 7 te demande de bâtir des relations profondes et compassionnelles avec des frontières claires. Tu dois apprendre à te connecter sans te perdre, à aimer sans fusionner excessivement. Les partenaires sensibles mais stables te conviennent.

## Ton défi
Le piège : te perdre dans l'autre, attirer des partenaires qui ont besoin d'être sauvés, confondre compassion et codépendance. Les meilleures relations maintiennent deux individualités distinctes.

## Maison 7 en Poissons
Saturne structure tes partenariats autour de la compassion mutuelle. Tu peux avoir des liens profonds mais tu apprends à y mettre des limites. Tes contrats bénéficient de ta capacité à percevoir les intentions cachées tout en restant clair.

## Micro-rituel du jour (2 min)
- Exprimer à un partenaire une limite avec douceur
- Trois respirations en maintenant ton centre dans la connexion
- Journal : « Comment mes relations peuvent-elles être profondes et saines ? »""",

    ('pisces', 8): """# ♄ Saturne en Poissons
**En une phrase :** Tu traverses les crises avec foi — les transformations deviennent des initiations quand tu leur donnes une structure de sens.

## Ton moteur
Saturne en Poissons en Maison 8 te demande de structurer ta relation aux transformations profondes. Tu lâches prise plus facilement que d'autres, mais tu dois aussi apprendre à agir concrètement dans les crises. Cette configuration peut mener à une profonde sagesse sur la vie et la mort.

## Ton défi
Le piège : te dissoudre dans les crises au lieu de les traverser, fuir la réalité des pertes, avoir du mal à agir concrètement dans les moments difficiles. La vraie transformation demande aussi de l'action.

## Maison 8 en Poissons
Saturne structure ta connexion aux mystères. Tu peux avoir des perceptions psychiques que tu apprends à ancrer. Les ressources partagées peuvent venir de façon mystérieuse mais tu apprends à les gérer concrètement.

## Micro-rituel du jour (2 min)
- Identifier une transformation en cours et une action concrète pour la traverser
- Trois respirations en alliant foi et action
- Journal : « Quelle crise m'enseigne actuellement quelque chose de profond ? »""",

    ('pisces', 9): """# ♄ Saturne en Poissons
**En une phrase :** Tu construis ta sagesse sur l'expérience mystique — ta spiritualité devient ta philosophie quand tu l'ancres dans la réalité.

## Ton moteur
Saturne en Poissons en Maison 9 te pousse vers une quête de sens profondément spirituelle mais ancrée. Tu ne te satisfais pas des croyances intellectuelles — tu veux l'expérience directe du divin, mais aussi la capacité de l'intégrer dans ta vie. Cette configuration peut créer un enseignant spirituel incarné.

## Ton défi
Le piège : fuir la réalité dans des croyances floues, confondre rêverie et spiritualité, adhérer à des gourous douteux. La vraie foi s'incarne aussi dans le quotidien.

## Maison 9 en Poissons
Saturne structure ta connexion au transcendant. Tu peux avoir des expériences mystiques que tu apprends à intégrer. Les voyages spirituels ou les retraites structurées te transforment profondément.

## Micro-rituel du jour (2 min)
- Méditer sur comment incarner ta spiritualité dans ta vie quotidienne
- Trois respirations en ancrant le transcendant dans l'immanent
- Journal : « Comment ma quête spirituelle se manifeste-t-elle concrètement ? »""",

    ('pisces', 10): """# ♄ Saturne en Poissons
**En une phrase :** Tu construis une carrière au service — ta réussite vient quand tu incarnes ta compassion de façon structurée et visible.

## Ton moteur
Saturne en Poissons en Maison 10 te pousse vers une carrière qui sert quelque chose de plus grand que toi. Tu ne cherches pas la gloire personnelle mais l'impact sur les âmes. Cette configuration favorise les carrières dans le soin, l'art, la spiritualité, l'humanitaire — avec une structure professionnelle.

## Ton défi
Le piège : avoir du mal avec les aspects pratiques de la réussite, te sacrifier professionnellement sans recevoir en retour, confondre mission et exploitation. La vraie vocation mérite aussi d'être reconnue.

## Maison 10 en Poissons
Saturne structure ta réputation autour de ta compassion et ta vision. On te perçoit comme quelqu'un qui sert une mission plus grande. Ta carrière peut sembler floue mais suit un fil spirituel cohérent.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière sert quelque chose de plus grand de façon concrète
- Trois respirations en alignant service et professionnalisme
- Journal : « Comment ma vocation professionnelle peut-elle être à la fois service et réussite ? »""",

    ('pisces', 11): """# ♄ Saturne en Poissons
**En une phrase :** Tu construis des communautés d'âmes — tes amitiés et tes projets collectifs sont des espaces de compassion structurée.

## Ton moteur
Saturne en Poissons en Maison 11 te demande de créer des réseaux de soutien mutuel avec des limites saines. Tu attires des amis sensibles et tu dois apprendre à être là pour eux sans te perdre. Les projets collectifs ont une dimension de guérison ou de service.

## Ton défi
Le piège : te perdre dans les besoins du groupe, attirer des amis qui ont besoin d'être sauvés, avoir du mal avec les aspects pratiques de l'action collective. Les meilleures communautés ont aussi une structure.

## Maison 11 en Poissons
Saturne structure tes réseaux autour de la compassion mutuelle. Tes amis peuvent être des artistes, des soignants, des spirituels — des âmes sensibles. Tes projets humanitaires touchent à la guérison et à l'art.

## Micro-rituel du jour (2 min)
- Offrir un soutien à un ami tout en maintenant tes limites
- Trois respirations en honorant le cercle d'âmes qui t'entoure
- Journal : « Quelle amitié m'apporte autant qu'elle reçoit ? »""",

    ('pisces', 12): """# ♄ Saturne en Poissons
**En une phrase :** Tu habites l'invisible avec discipline — ta spiritualité est une immersion structurée dans l'océan de la conscience.

## Ton moteur
Saturne en Poissons en Maison 12 est une position de grande profondeur spirituelle. Tu as un accès naturel aux dimensions invisibles, mais tu dois apprendre à y naviguer avec discernement. Cette configuration peut mener à une maîtrise spirituelle acquise par la discipline intérieure.

## Ton défi
Le piège : te perdre dans les dimensions invisibles, confondre dissolution de l'ego et éveil, fuir la réalité dans la spiritualité. La vraie transcendance inclut aussi l'incarnation.

## Maison 12 en Poissons
Saturne structure au maximum ta connexion au mystère. Tu peux avoir des capacités psychiques développées que tu apprends à maîtriser. Les retraites spirituelles profondes et structurées te régénèrent.

## Micro-rituel du jour (2 min)
- Méditer avec discipline, en maintenant ta présence dans la dissolution
- Trois respirations en ancrant l'infini dans le fini
- Journal : « Comment puis-je naviguer l'invisible tout en restant ancré ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in SATURN_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'saturn',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP saturn/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='saturn',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT saturn/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
