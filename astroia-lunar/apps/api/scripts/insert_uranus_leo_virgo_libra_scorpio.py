#!/usr/bin/env python3
"""Script d'insertion des interprétations Uranus/Leo, Virgo, Libra, Scorpio en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

URANUS_INTERPRETATIONS = {
    # LEO - 12 maisons
    ('leo', 1): """# ♅ Uranus en Lion
**En une phrase :** Tu incarnes une créativité révolutionnaire — ton identité se forge en exprimant ton unicité de façon éclatante.

## Ton moteur
Uranus en Lion en Maison 1 te donne un besoin impérieux d'exprimer ta différence de façon visible et créative. Tu ne peux pas te fondre dans la masse — tu dois briller de façon originale.

## Ton défi
Le piège : un ego qui cherche l'attention par la provocation, avoir du mal à accepter l'ombre, confondre originalité et exhibition. La vraie créativité révolutionnaire inspire sans écraser.

## Maison 1 en Lion
Uranus électrise ta présence et ton expression personnelle. Tu projettes une image de créativité audacieuse. Ton apparence peut être théâtrale ou changer de façon spectaculaire.

## Micro-rituel du jour (2 min)
- Exprimer quelque chose d'unique sur toi de façon visible
- Trois respirations en assumant ta lumière originale
- Journal : « Comment ma créativité m'a-t-elle distingué récemment ? »""",

    ('leo', 2): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes ta valeur par la créativité — tes ressources viennent quand tu brilles de façon originale.

## Ton moteur
Uranus en Lion en Maison 2 crée des revenus par la créativité, l'expression personnelle, le spectacle, l'art. Tu valorises ta capacité à être unique et à inspirer les autres.

## Ton défi
Le piège : des finances qui dépendent trop de la reconnaissance, confondre valeur personnelle et succès visible, avoir des revenus instables par besoin de briller. La vraie prospérité créative est aussi stable.

## Maison 2 en Lion
Uranus secoue tes finances pour les relier à ta créativité. Tu peux gagner de l'argent par des talents artistiques ou expressifs uniques. Tes valeurs sont liées à l'authenticité et la créativité.

## Micro-rituel du jour (2 min)
- Identifier un talent créatif que tu pourrais mieux valoriser
- Trois respirations en reconnectant abondance et expression
- Journal : « Comment ma créativité peut-elle créer plus de valeur ? »""",

    ('leo', 3): """# ♅ Uranus en Lion
**En une phrase :** Tu communiques avec éclat et originalité — tes mots inspirent et illuminent de façon révolutionnaire.

## Ton moteur
Uranus en Lion en Maison 3 te donne une communication qui captive et inspire. Tu sais présenter les idées de façon spectaculaire et mémorable. L'enseignement créatif, les médias, le storytelling sont tes voies.

## Ton défi
Le piège : une communication qui cherche trop les projecteurs, avoir du mal à écouter les autres, confondre style et substance. La vraie communication inspirante a aussi de la profondeur.

## Maison 3 en Lion
Uranus électrise tes échanges pour les rendre plus créatifs. Tes relations avec frères, sœurs et voisins peuvent être théâtrales ou stimulantes artistiquement.

## Micro-rituel du jour (2 min)
- Communiquer une idée de façon créative et mémorable
- Trois respirations en laissant ta lumière s'exprimer par les mots
- Journal : « Comment puis-je mieux inspirer par ma communication ? »""",

    ('leo', 4): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes la famille par la créativité — ton foyer devient une scène d'expression et de célébration.

## Ton moteur
Uranus en Lion en Maison 4 crée un environnement familial où la créativité et l'expression individuelle sont encouragées. Ton foyer peut être un lieu de spectacle, d'art, de célébration de la vie.

## Ton défi
Le piège : un ego familial qui prend toute la place, des drames domestiques pour attirer l'attention, avoir du mal à partager la scène. La vraie famille créative célèbre chaque membre.

## Maison 4 en Lion
Uranus secoue ta vie familiale pour l'ouvrir à plus d'expression. Tu as peut-être grandi dans une famille artistique ou tu crées la tienne comme une troupe créative.

## Micro-rituel du jour (2 min)
- Créer un moment d'expression joyeuse chez toi
- Trois respirations en faisant de ton foyer une célébration
- Journal : « Comment mon chez-moi peut-il être plus créatif et vivant ? »""",

    ('leo', 5): """# ♅ Uranus en Lion
**En une phrase :** Tu crées avec une puissance révolutionnaire — tes œuvres et tes amours sont des célébrations éclatantes de la vie.

## Ton moteur
Uranus en Lion en Maison 5 amplifie au maximum ta créativité et ton besoin d'expression. Tu es né pour créer, jouer, aimer de façon spectaculaire et originale. Le théâtre, l'art, le spectacle sont tes domaines naturels.

## Ton défi
Le piège : des amours dramatiques qui épuisent, une créativité qui cherche trop la validation, avoir du mal avec la simplicité. La vraie joie créative n'a pas besoin d'audience.

## Maison 5 en Lion
Uranus électrise au maximum tes plaisirs et ta créativité. Tu peux vivre des passions intenses et originales. Tes œuvres sont audacieuses et personnelles.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif spectaculaire, même petit
- Trois respirations en laissant ta joie briller
- Journal : « Quelle création audacieuse me ferait vraiment vibrer ? »""",

    ('leo', 6): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes le travail par la créativité — ton efficacité vient quand tu peux exprimer ton unicité.

## Ton moteur
Uranus en Lion en Maison 6 te pousse à transformer le travail quotidien en expression créative. Tu ne supportes pas un travail qui ne te permet pas de briller. Les métiers artistiques ou expressifs te conviennent.

## Ton défi
Le piège : avoir du mal avec les tâches qui ne brillent pas, confondre travail et performance, négliger la routine par besoin de spectaculaire. La vraie efficacité créative inclut aussi l'ombre.

## Maison 6 en Lion
Uranus secoue ton quotidien pour l'ouvrir à plus d'expression. Tu travailles mieux quand tu peux apporter ta touche personnelle. Ta santé bénéficie de joie et de créativité.

## Micro-rituel du jour (2 min)
- Apporter une touche créative à une tâche quotidienne
- Trois respirations en trouvant la joie dans le travail ordinaire
- Journal : « Comment puis-je exprimer ma créativité dans mon travail ? »""",

    ('leo', 7): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes les relations par l'admiration mutuelle — tes partenariats sont des célébrations de deux unicités.

## Ton moteur
Uranus en Lion en Maison 7 crée des relations où chaque partenaire peut briller. Tu attires des personnes créatives, parfois dramatiques, toujours expressives. L'admiration mutuelle est essentielle.

## Ton défi
Le piège : des relations qui deviennent des compétitions d'ego, avoir du mal à partager les projecteurs, des drames relationnels pour l'attention. Les meilleures relations célèbrent deux lumières.

## Maison 7 en Lion
Uranus électrise tes partenariats de créativité et d'expression. Tu peux avoir des relations avec des artistes ou des personnes charismatiques.

## Micro-rituel du jour (2 min)
- Célébrer ce qui rend ton partenaire unique
- Trois respirations en partageant la scène avec joie
- Journal : « Comment mes relations peuvent-elles honorer deux lumières ? »""",

    ('leo', 8): """# ♅ Uranus en Lion
**En une phrase :** Tu traverses les crises comme des renaissances créatives — les transformations deviennent des occasions de briller différemment.

## Ton moteur
Uranus en Lion en Maison 8 transforme les crises en occasions de réinventer ton expression. Tu ne te contentes pas de survivre aux épreuves — tu en émerges plus créatif et plus lumineux.

## Ton défi
Le piège : dramatiser les crises pour l'attention, avoir du mal avec les transformations qui diminuent ton éclat, résister aux changements d'identité. La vraie renaissance créative sait aussi être humble.

## Maison 8 en Lion
Uranus secoue ta relation aux transformations pour les rendre créatives. Ta sexualité peut être spectaculaire et transformatrice. Les ressources partagées peuvent venir de talents créatifs.

## Micro-rituel du jour (2 min)
- Identifier comment une crise récente t'a rendu plus créatif
- Trois respirations en accueillant la transformation comme renaissance
- Journal : « Quelle nouvelle lumière émerge de mes épreuves ? »""",

    ('leo', 9): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes la sagesse par l'expression — ta philosophie est une célébration créative de la vie.

## Ton moteur
Uranus en Lion en Maison 9 te pousse vers une quête de sens qui passe par la créativité et l'expression. Ta spiritualité est joyeuse et célébratoire. Tu peux enseigner de façon spectaculaire.

## Ton défi
Le piège : une spiritualité égotique, avoir du mal avec les traditions humbles, confondre charisme et sagesse. La vraie sagesse créative inspire sans se mettre en avant.

## Maison 9 en Lion
Uranus électrise ta quête de sens de créativité. Tes voyages peuvent être des aventures artistiques. Tu peux être attiré par des philosophies qui célèbrent l'expression individuelle.

## Micro-rituel du jour (2 min)
- Explorer une sagesse qui célèbre la joie et la créativité
- Trois respirations en connectant sens et expression
- Journal : « Quelle philosophie de vie me fait vraiment vibrer ? »""",

    ('leo', 10): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes ta carrière par l'expression — ta réussite vient quand tu brilles de façon authentique et originale.

## Ton moteur
Uranus en Lion en Maison 10 te pousse vers une carrière où tu peux être toi-même de façon visible. Tu réussis en exprimant ta créativité et ton unicité. Les métiers artistiques, expressifs ou de leadership créatif te conviennent.

## Ton défi
Le piège : une ambition trop égotique, avoir du mal avec l'ombre du succès, confondre célébrité et accomplissement. La vraie réussite créative a aussi de l'humilité.

## Maison 10 en Lion
Uranus secoue ta réputation pour la rendre plus authentiquement créative. On te remarque pour ton expression originale et audacieuse. Ta carrière peut être dans les arts ou le spectacle.

## Micro-rituel du jour (2 min)
- Identifier comment tu peux exprimer plus d'originalité dans ta carrière
- Trois respirations en assumant ta lumière professionnelle
- Journal : « Comment ma carrière peut-elle mieux refléter ma créativité ? »""",

    ('leo', 11): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes l'action collective par la créativité — tes amitiés et tes projets sont des célébrations de l'unicité de chacun.

## Ton moteur
Uranus en Lion en Maison 11 te connecte à des réseaux créatifs où chaque individu brille. Tes amis sont des artistes, des créateurs, des personnes expressives. Les projets collectifs sont des célébrations.

## Ton défi
Le piège : vouloir être la star du groupe, avoir du mal avec les projets qui ne te mettent pas en avant, confondre leadership et domination. Les meilleures communautés honorent chaque lumière.

## Maison 11 en Lion
Uranus électrise tes réseaux de créativité et d'expression. Tu es fait pour les collectifs artistiques, les mouvements qui célèbrent l'individualité.

## Micro-rituel du jour (2 min)
- Célébrer la créativité unique d'un ami
- Trois respirations en honorant le collectif des lumières
- Journal : « Comment puis-je contribuer à un groupe tout en brillant ? »""",

    ('leo', 12): """# ♅ Uranus en Lion
**En une phrase :** Tu révolutionnes ta vie intérieure par la créativité — ton inconscient est une source d'inspiration artistique profonde.

## Ton moteur
Uranus en Lion en Maison 12 crée des connexions entre ta créativité et les dimensions invisibles. Ton art peut venir de sources transpersonnelles. Les rêves sont une source d'inspiration créative.

## Ton défi
Le piège : un ego spirituel qui cherche la reconnaissance, avoir du mal avec l'anonymat, confondre inspiration et exhibition. La vraie créativité spirituelle n'a pas besoin de public.

## Maison 12 en Lion
Uranus secoue ta connexion à l'invisible pour l'ouvrir à la créativité. Tu peux avoir des visions artistiques ou des inspirations profondes. Les retraites créatives te régénèrent.

## Micro-rituel du jour (2 min)
- Méditer en accueillant l'inspiration créative de l'invisible
- Trois respirations en laissant la lumière intérieure briller sans témoin
- Journal : « Quelle inspiration créative émerge de mes profondeurs ? »""",

    # VIRGO - 12 maisons
    ('virgo', 1): """# ♅ Uranus en Vierge
**En une phrase :** Tu incarnes une révolution de la perfection — ton identité se forge en innovant les méthodes et les systèmes.

## Ton moteur
Uranus en Vierge en Maison 1 te donne un esprit analytique révolutionnaire. Tu vois comment améliorer les systèmes, optimiser les processus, perfectionner ce qui existe. L'innovation pratique est ton domaine.

## Ton défi
Le piège : une critique constante qui épuise, avoir du mal avec l'imperfection, confondre perfectionnement et valeur. La vraie amélioration sait aussi accepter ce qui est.

## Maison 1 en Vierge
Uranus électrise ton sens pratique et analytique. Tu projettes une image d'efficacité originale. Ton apparence peut refléter ta précision et ton attention au détail.

## Micro-rituel du jour (2 min)
- Identifier une amélioration innovante que tu as apportée récemment
- Trois respirations en acceptant l'imperfection comme partie du processus
- Journal : « Comment mon sens de l'amélioration m'a-t-il servi ? »""",

    ('virgo', 2): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes ta prospérité par l'efficacité — tes ressources viennent quand tu améliores les systèmes.

## Ton moteur
Uranus en Vierge en Maison 2 crée des revenus par l'amélioration, l'optimisation, l'analyse. Tu peux gagner de l'argent en rendant les choses plus efficaces, en résolvant des problèmes pratiques.

## Ton défi
Le piège : sous-valoriser tes services, avoir une relation anxieuse à l'argent, confondre économie et avarice. La vraie prospérité pratique sait aussi profiter.

## Maison 2 en Vierge
Uranus secoue tes finances pour les optimiser. Tu peux avoir des revenus liés à la santé, au service, à l'amélioration. Tes valeurs sont liées à l'utilité et l'efficacité.

## Micro-rituel du jour (2 min)
- Identifier un service ou une compétence que tu pourrais mieux valoriser
- Trois respirations en reconnaissant la valeur de ton utilité
- Journal : « Comment mon sens pratique peut-il créer plus d'abondance ? »""",

    ('virgo', 3): """# ♅ Uranus en Vierge
**En une phrase :** Tu communiques avec précision révolutionnaire — tes analyses changent la façon dont on comprend les problèmes.

## Ton moteur
Uranus en Vierge en Maison 3 te donne une communication analytique et précise. Tu sais décortiquer les problèmes, présenter les solutions, optimiser l'information. L'écriture technique, l'analyse, le conseil pratique sont tes voies.

## Ton défi
Le piège : une communication trop critique, avoir du mal à voir la grande image, noyer les gens dans les détails. La vraie communication analytique sait aussi synthétiser.

## Maison 3 en Vierge
Uranus électrise tes échanges d'analyse et de précision. Tes relations avec frères, sœurs et voisins peuvent être pratiques et serviables.

## Micro-rituel du jour (2 min)
- Partager une analyse utile avec quelqu'un
- Trois respirations en trouvant l'équilibre entre détail et vision
- Journal : « Comment puis-je mieux communiquer mes analyses ? »""",

    ('virgo', 4): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes la vie domestique par l'efficacité — ton foyer devient un système optimisé de bien-être.

## Ton moteur
Uranus en Vierge en Maison 4 crée un environnement domestique organisé et innovant. Tu es attiré par les technologies domestiques, les méthodes d'organisation, les routines de santé à la maison.

## Ton défi
Le piège : un foyer trop rigide ou critique, avoir du mal avec le désordre familial, confondre organisation et chaleur. La vraie maison saine accueille aussi l'imperfection.

## Maison 4 en Vierge
Uranus secoue ta vie familiale pour l'améliorer. Tu as peut-être grandi dans une famille axée sur la santé ou l'ordre. Ton foyer peut intégrer des innovations pratiques.

## Micro-rituel du jour (2 min)
- Identifier une amélioration pratique pour ton espace de vie
- Trois respirations en acceptant le foyer comme lieu de détente aussi
- Journal : « Comment mon chez-moi peut-il être à la fois efficace et accueillant ? »""",

    ('virgo', 5): """# ♅ Uranus en Vierge
**En une phrase :** Tu crées avec précision et innovation — tes œuvres améliorent le monde de façon concrète.

## Ton moteur
Uranus en Vierge en Maison 5 te pousse vers une créativité qui sert un but pratique. Tu ne crées pas juste pour l'art mais pour améliorer, résoudre, optimiser. En amour, tu cherches des partenaires avec qui tu peux construire concrètement.

## Ton défi
Le piège : une créativité trop perfectionniste qui ne finit rien, des amours jugées sur des critères pratiques, avoir du mal avec la joie pure. La vraie joie créative sait aussi lâcher le contrôle.

## Maison 5 en Vierge
Uranus électrise tes plaisirs de façon analytique. Tu peux être attiré par des partenaires serviables et compétents. Ta créativité s'épanouit dans les projets utiles.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif sans chercher à le perfectionner
- Trois respirations en laissant la joie être imparfaite
- Journal : « Quelle création utile me fait vraiment plaisir ? »""",

    ('virgo', 6): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes le travail et la santé — ton efficacité vient d'innovations qui améliorent le quotidien.

## Ton moteur
Uranus en Vierge en Maison 6 amplifie au maximum ton talent pour améliorer les routines et les systèmes. Tu excelles dans l'optimisation du travail et les innovations de santé. Les métiers de l'amélioration continue te conviennent.

## Ton défi
Le piège : un perfectionnisme qui épuise, une obsession de la santé, avoir du mal à s'arrêter d'améliorer. La vraie efficacité sait aussi se satisfaire de ce qui fonctionne.

## Maison 6 en Vierge
Uranus secoue au maximum ton quotidien pour le perfectionner. Tu es naturellement attiré par les dernières méthodes de santé et d'efficacité. Attention à ne pas devenir obsessionnel.

## Micro-rituel du jour (2 min)
- Apprécier une routine qui fonctionne sans chercher à l'améliorer
- Trois respirations en acceptant que "assez bien" suffit parfois
- Journal : « Quelle amélioration a vraiment fait une différence dans mon quotidien ? »""",

    ('virgo', 7): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes les relations par le service mutuel — tes partenariats sont des collaborations pratiques et innovantes.

## Ton moteur
Uranus en Vierge en Maison 7 crée des relations basées sur l'entraide et l'amélioration mutuelle. Tu attires des partenaires compétents, serviables, orientés solutions.

## Ton défi
Le piège : des relations jugées sur des critères pratiques, une critique constante du partenaire, avoir du mal avec les imperfections de l'autre. Les meilleures relations acceptent aussi les failles.

## Maison 7 en Vierge
Uranus électrise tes partenariats de praticité et de service. Tu peux avoir des relations qui aident à résoudre des problèmes. Tes contrats bénéficient de précision et d'organisation.

## Micro-rituel du jour (2 min)
- Apprécier ton partenaire pour une qualité non liée à sa compétence
- Trois respirations en accueillant l'imperfection dans la relation
- Journal : « Comment mes relations peuvent-elles être utiles ET aimantes ? »""",

    ('virgo', 8): """# ♅ Uranus en Vierge
**En une phrase :** Tu traverses les crises par l'analyse — les transformations deviennent des processus à comprendre et optimiser.

## Ton moteur
Uranus en Vierge en Maison 8 te donne la capacité d'analyser les crises et de trouver des solutions pratiques. Tu ne subis pas les transformations — tu les décortiques pour mieux les traverser.

## Ton défi
Le piège : intellectualiser les crises au lieu de les vivre, avoir du mal avec l'irrationnel des transformations, contrôler au lieu de lâcher prise. La vraie transformation échappe parfois à l'analyse.

## Maison 8 en Vierge
Uranus secoue ta relation aux mystères pour les éclairer. Tu peux avoir des insights analytiques sur les situations cachées. Ta sexualité peut être liée à la santé ou à l'amélioration.

## Micro-rituel du jour (2 min)
- Identifier une transformation que tu ne peux pas analyser et l'accepter
- Trois respirations en lâchant le besoin de comprendre
- Journal : « Quel mystère suis-je prêt à accueillir sans l'analyser ? »""",

    ('virgo', 9): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes la sagesse par l'application pratique — ta philosophie améliore concrètement la vie.

## Ton moteur
Uranus en Vierge en Maison 9 te pousse vers des croyances qui ont une application pratique. Tu ne te satisfais pas des philosophies abstraites — tu veux des enseignements qui fonctionnent.

## Ton défi
Le piège : rejeter les sagesses qui ne sont pas "prouvées", avoir du mal avec le mystère, réduire la spiritualité à des techniques. La vraie sagesse pratique inclut aussi le mystère.

## Maison 9 en Vierge
Uranus électrise ta quête de sens de praticité. Tes voyages peuvent être orientés santé ou amélioration. Tu peux étudier des domaines qui ont une application directe.

## Micro-rituel du jour (2 min)
- Explorer une sagesse qui améliore concrètement ta vie
- Trois respirations en équilibrant pratique et mystère
- Journal : « Quelle philosophie m'a aidé à améliorer ma vie ? »""",

    ('virgo', 10): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes ta carrière par l'amélioration — ta réussite vient quand tu optimises les systèmes et aides concrètement.

## Ton moteur
Uranus en Vierge en Maison 10 te pousse vers une carrière qui améliore, optimise, résout. Tu réussis en rendant les choses meilleures, plus efficaces, plus saines. Les métiers de la santé, de l'organisation, de l'amélioration continue te conviennent.

## Ton défi
Le piège : une carrière perfectionniste qui n'est jamais satisfaite, avoir du mal à recevoir la reconnaissance, confondre service et invisibilité. La vraie réussite pratique mérite aussi d'être vue.

## Maison 10 en Vierge
Uranus secoue ta réputation pour la rendre utile. On te reconnaît pour ta capacité à résoudre les problèmes et améliorer les systèmes.

## Micro-rituel du jour (2 min)
- Identifier une amélioration que tu as apportée dans ta carrière et la célébrer
- Trois respirations en reconnaissant la valeur de ton service
- Journal : « Comment ma carrière améliore-t-elle concrètement le monde ? »""",

    ('virgo', 11): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes l'action collective par le service — tes amitiés et tes projets améliorent concrètement les choses.

## Ton moteur
Uranus en Vierge en Maison 11 te connecte à des réseaux de personnes pratiques et serviables. Tes amis partagent ton souci d'améliorer les choses. Les projets collectifs sont concrets et utiles.

## Ton défi
Le piège : être critique envers les groupes, avoir du mal avec les projets utopiques, confondre service et contrôle. Les meilleures communautés accueillent aussi les rêveurs.

## Maison 11 en Vierge
Uranus électrise tes réseaux de praticité et de service. Tu es fait pour les organisations qui améliorent concrètement le monde, les associations de santé ou d'environnement.

## Micro-rituel du jour (2 min)
- Participer à un projet collectif qui améliore quelque chose de concret
- Trois respirations en honorant le service collectif
- Journal : « Quel projet de groupe m'a permis de contribuer utilement ? »""",

    ('virgo', 12): """# ♅ Uranus en Vierge
**En une phrase :** Tu révolutionnes ta vie intérieure par l'analyse — ton inconscient devient une source de insights pratiques.

## Ton moteur
Uranus en Vierge en Maison 12 crée des connexions entre ton sens analytique et les dimensions invisibles. Tes rêves peuvent contenir des solutions à des problèmes pratiques. La méditation peut t'aider à organiser tes pensées.

## Ton défi
Le piège : analyser l'inconscient au lieu de l'accueillir, avoir du mal avec l'irrationnel spirituel, contrôler la vie intérieure. La vraie sagesse intérieure échappe parfois à la raison.

## Maison 12 en Vierge
Uranus secoue ta connexion à l'invisible pour la rendre pratique. Tu peux avoir des intuitions qui t'aident à résoudre des problèmes. Les retraites orientées santé te régénèrent.

## Micro-rituel du jour (2 min)
- Méditer en accueillant ce qui vient sans l'analyser
- Trois respirations en lâchant le besoin de comprendre l'invisible
- Journal : « Quel insight pratique m'est venu de mes profondeurs ? »""",

    # LIBRA - 12 maisons
    ('libra', 1): """# ♅ Uranus en Balance
**En une phrase :** Tu incarnes une révolution de l'harmonie — ton identité se forge en créant de nouvelles formes de beauté et de relation.

## Ton moteur
Uranus en Balance en Maison 1 te donne un sens esthétique révolutionnaire et une façon originale de te relier aux autres. Tu redéfinis la beauté, l'élégance, l'harmonie.

## Ton défi
Le piège : une identité trop dépendante du regard des autres, changer constamment pour plaire, confondre originalité et provocation esthétique. La vraie beauté révolutionnaire a aussi de la profondeur.

## Maison 1 en Balance
Uranus électrise ton apparence et tes relations. Tu projettes une image d'élégance originale. Ton style peut être avant-gardiste ou changer selon les rencontres.

## Micro-rituel du jour (2 min)
- Exprimer ta beauté unique d'une façon nouvelle
- Trois respirations en assumant ton esthétique personnelle
- Journal : « Comment ma vision de la beauté me distingue-t-elle ? »""",

    ('libra', 2): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes ta valeur par l'esthétique — tes ressources viennent quand tu crées de l'harmonie de façon originale.

## Ton moteur
Uranus en Balance en Maison 2 crée des revenus par l'art, le design, la beauté, les relations. Tu valorises l'harmonie et tu peux la monétiser de façon innovante.

## Ton défi
Le piège : des finances qui dépendent trop des autres, confondre valeur et apparence, avoir des revenus instables par indécision. La vraie prospérité harmonieuse est aussi indépendante.

## Maison 2 en Balance
Uranus secoue tes finances pour les relier à l'esthétique. Tu peux gagner de l'argent par des talents artistiques ou relationnels. Tes valeurs sont liées à la beauté et l'équilibre.

## Micro-rituel du jour (2 min)
- Identifier comment ta création d'harmonie peut avoir de la valeur
- Trois respirations en reliant beauté et abondance
- Journal : « Comment mon sens esthétique peut-il créer de la valeur ? »""",

    ('libra', 3): """# ♅ Uranus en Balance
**En une phrase :** Tu communiques avec diplomatie révolutionnaire — tes mots créent de nouvelles formes de dialogue et de compréhension.

## Ton moteur
Uranus en Balance en Maison 3 te donne une communication qui recherche l'équilibre et l'harmonie de façon innovante. Tu sais présenter tous les points de vue, créer des ponts entre les différences.

## Ton défi
Le piège : une communication qui évite le conflit à tout prix, avoir du mal à prendre position, plaire au détriment de la vérité. La vraie diplomatie révolutionnaire sait aussi être directe.

## Maison 3 en Balance
Uranus électrise tes échanges de beauté et d'équilibre. Tes relations avec frères, sœurs et voisins peuvent être artistiques ou axées sur l'harmonie.

## Micro-rituel du jour (2 min)
- Communiquer quelque chose de difficile avec grâce
- Trois respirations en trouvant l'équilibre entre vérité et harmonie
- Journal : « Comment puis-je créer plus de dialogue constructif ? »""",

    ('libra', 4): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes la vie familiale par l'harmonie — ton foyer devient un espace de beauté et de paix originale.

## Ton moteur
Uranus en Balance en Maison 4 crée un environnement domestique esthétique et harmonieux de façon innovante. Tu es attiré par le design d'intérieur, les espaces qui équilibrent les énergies.

## Ton défi
Le piège : éviter les conflits familiaux au détriment de l'authenticité, un foyer trop dépendant de l'apparence, avoir du mal avec le désordre. La vraie maison harmonieuse accueille aussi les émotions difficiles.

## Maison 4 en Balance
Uranus secoue ta vie familiale pour l'harmoniser. Tu as peut-être grandi dans une famille axée sur l'esthétique ou la diplomatie. Ton foyer peut être un lieu de beauté et de rencontres.

## Micro-rituel du jour (2 min)
- Créer un élément de beauté ou d'harmonie chez toi
- Trois respirations en faisant de ton foyer un espace de paix
- Journal : « Comment mon chez-moi reflète-t-il mon sens de l'harmonie ? »""",

    ('libra', 5): """# ♅ Uranus en Balance
**En une phrase :** Tu crées avec élégance révolutionnaire — tes œuvres et tes amours redéfinissent la beauté et l'amour.

## Ton moteur
Uranus en Balance en Maison 5 te pousse vers une créativité qui révolutionne l'esthétique. Tu peux exceller dans l'art, le design, la mode. En amour, tu cherches des partenaires qui partagent ton sens de la beauté et de l'équilibre.

## Ton défi
Le piège : des amours trop axées sur l'apparence, une créativité qui cherche trop à plaire, avoir du mal à créer seul. La vraie joie créative n'a pas besoin d'approbation.

## Maison 5 en Balance
Uranus électrise tes plaisirs d'élégance et de relation. Tu peux avoir des attirances pour des personnes esthétiquement raffinées. Ta créativité s'épanouit dans la collaboration.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui célèbre la beauté
- Trois respirations en laissant ta créativité être libre du jugement
- Journal : « Quelle création harmonieuse me ferait vraiment plaisir ? »""",

    ('libra', 6): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes le travail par l'harmonie — ton efficacité vient quand l'environnement est beau et équilibré.

## Ton moteur
Uranus en Balance en Maison 6 te pousse à créer des environnements de travail harmonieux et esthétiques. Tu ne travailles pas bien dans le chaos ou la laideur. Les métiers de l'art, du design, de la médiation te conviennent.

## Ton défi
Le piège : avoir du mal à travailler dans des conditions imparfaites, éviter les conflits professionnels, une indécision qui ralentit. La vraie efficacité harmonieuse s'adapte aussi.

## Maison 6 en Balance
Uranus secoue ton quotidien pour le rendre plus beau. Tu travailles mieux dans des équipes équilibrées. Ta santé bénéficie de l'harmonie et de la beauté dans ton environnement.

## Micro-rituel du jour (2 min)
- Apporter un élément d'harmonie à ton espace de travail
- Trois respirations en trouvant la beauté dans le quotidien
- Journal : « Comment mon travail peut-il être plus harmonieux ? »""",

    ('libra', 7): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes les relations — tes partenariats redéfinissent ce que signifie être ensemble.

## Ton moteur
Uranus en Balance en Maison 7 amplifie au maximum ton besoin de relations innovantes et équilibrées. Tu attires des partenaires qui partagent ta vision de l'amour comme art de vivre.

## Ton défi
Le piège : idéaliser les relations, avoir du mal avec les conflits, changer de partenaire pour trouver l'harmonie parfaite. Les meilleures relations sont aussi imparfaites.

## Maison 7 en Balance
Uranus électrise au maximum tes partenariats. Tu peux vivre des relations qui redéfinissent l'équilibre entre indépendance et union. Tes contrats bénéficient de ton sens de l'équité.

## Micro-rituel du jour (2 min)
- Créer un moment de beauté dans ta relation
- Trois respirations en célébrant l'harmonie avec l'autre
- Journal : « Comment ma relation peut-elle évoluer vers plus d'harmonie ? »""",

    ('libra', 8): """# ♅ Uranus en Balance
**En une phrase :** Tu traverses les crises en cherchant l'équilibre — les transformations deviennent des occasions de trouver une nouvelle harmonie.

## Ton moteur
Uranus en Balance en Maison 8 te pousse à trouver l'équilibre même dans les crises. Tu peux transformer les conflits en dialogues, les ruptures en nouvelles formes de relation.

## Ton défi
Le piège : éviter les transformations profondes pour maintenir l'harmonie superficielle, avoir du mal avec l'intensité, fuir les conflits nécessaires. La vraie harmonie inclut aussi la traversée des ombres.

## Maison 8 en Balance
Uranus secoue ta relation aux crises pour les équilibrer. Ta sexualité peut être liée à la recherche d'harmonie profonde. Les ressources partagées bénéficient de ton sens de l'équité.

## Micro-rituel du jour (2 min)
- Identifier comment tu peux trouver l'équilibre dans une transformation en cours
- Trois respirations en accueillant l'harmonie qui émerge des crises
- Journal : « Quelle harmonie nouvelle une crise m'a-t-elle apportée ? »""",

    ('libra', 9): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes la sagesse par la relation — ta philosophie est celle du dialogue et de la compréhension mutuelle.

## Ton moteur
Uranus en Balance en Maison 9 te pousse vers des croyances qui célèbrent la diversité et le dialogue. Ta spiritualité est relationnelle et ouverte à toutes les perspectives.

## Ton défi
Le piège : une philosophie qui évite de prendre position, relativiser au point de ne rien affirmer, confondre ouverture et indécision. La vraie sagesse relationnelle sait aussi s'engager.

## Maison 9 en Balance
Uranus électrise ta quête de sens de dialogue et d'harmonie. Tes voyages peuvent être orientés vers les rencontres culturelles. Tu peux enseigner l'art du dialogue.

## Micro-rituel du jour (2 min)
- Explorer une perspective différente de la tienne avec ouverture
- Trois respirations en trouvant l'unité dans la diversité
- Journal : « Quelle sagesse relationnelle me guide actuellement ? »""",

    ('libra', 10): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes ta carrière par la relation — ta réussite vient quand tu crées de l'harmonie et de la beauté publiquement.

## Ton moteur
Uranus en Balance en Maison 10 te pousse vers une carrière dans l'art, le design, la diplomatie, les relations publiques. Tu réussis en créant de l'harmonie visible.

## Ton défi
Le piège : une carrière trop dépendante du regard des autres, de l'indécision professionnelle, éviter les conflits au détriment de l'avancement. La vraie réussite harmonieuse sait aussi s'affirmer.

## Maison 10 en Balance
Uranus secoue ta réputation pour la rendre plus esthétique et relationnelle. On te reconnaît pour ton sens de la beauté et ta capacité à créer des ponts.

## Micro-rituel du jour (2 min)
- Identifier comment tu peux mieux créer de l'harmonie dans ta carrière
- Trois respirations en assumant ton rôle de créateur de beauté
- Journal : « Comment ma carrière peut-elle contribuer à plus d'harmonie ? »""",

    ('libra', 11): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes l'action collective par le dialogue — tes amitiés et tes projets créent des ponts entre les différences.

## Ton moteur
Uranus en Balance en Maison 11 te connecte à des réseaux harmonieux et divers. Tes amis viennent de tous horizons et tu sais les relier. Les projets collectifs sont basés sur le dialogue et la collaboration.

## Ton défi
Le piège : des amitiés superficielles par désir de plaire à tous, éviter les conflits de groupe nécessaires, perdre ta propre voix dans le collectif. Les meilleures communautés honorent aussi les désaccords.

## Maison 11 en Balance
Uranus électrise tes réseaux de beauté et de relation. Tu es fait pour les collectifs artistiques, les associations culturelles, les projets de dialogue interculturel.

## Micro-rituel du jour (2 min)
- Créer un pont entre deux personnes ou groupes différents
- Trois respirations en honorant la diversité harmonieuse
- Journal : « Comment puis-je contribuer à plus de dialogue collectif ? »""",

    ('libra', 12): """# ♅ Uranus en Balance
**En une phrase :** Tu révolutionnes ta vie intérieure par la relation — ton inconscient te guide vers une harmonie profonde avec le tout.

## Ton moteur
Uranus en Balance en Maison 12 crée des connexions entre ton sens de l'harmonie et les dimensions invisibles. Tu peux percevoir les équilibres et déséquilibres invisibles. La méditation t'aide à trouver la paix intérieure.

## Ton défi
Le piège : une vie intérieure trop dépendante des autres, projeter tes ombres sur tes relations, fuir le conflit intérieur. La vraie harmonie spirituelle inclut aussi l'ombre.

## Maison 12 en Balance
Uranus secoue ta connexion à l'invisible pour l'harmoniser. Tes rêves peuvent contenir des messages sur tes relations. Les retraites orientées vers la paix te régénèrent.

## Micro-rituel du jour (2 min)
- Méditer en cherchant l'harmonie intérieure
- Trois respirations en équilibrant toutes les parties de toi
- Journal : « Quelle harmonie intérieure ai-je besoin de cultiver ? »""",

    # SCORPIO - 12 maisons
    ('scorpio', 1): """# ♅ Uranus en Scorpion
**En une phrase :** Tu incarnes une transformation radicale — ton identité se forge en traversant les morts et renaissances.

## Ton moteur
Uranus en Scorpion en Maison 1 te donne une personnalité intense et transformatrice. Tu n'as pas peur des profondeurs, tu les recherches. Ton regard voit ce qui est caché.

## Ton défi
Le piège : une intensité qui repousse, chercher constamment la crise, confondre profondeur et destruction. La vraie transformation sait aussi préserver.

## Maison 1 en Scorpion
Uranus électrise ton intensité et ton magnétisme. Tu projettes une image de puissance et de mystère. Ton apparence peut refléter tes transformations intérieures.

## Micro-rituel du jour (2 min)
- Identifier une transformation que tu incarnes
- Trois respirations en accueillant ta puissance transformatrice
- Journal : « Comment mes transformations me définissent-elles ? »""",

    ('scorpio', 2): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes ta relation aux ressources — tes finances se transforment à travers les crises et les renaissances.

## Ton moteur
Uranus en Scorpion en Maison 2 crée des changements radicaux dans tes finances. Tu peux passer par des pertes qui mènent à une nouvelle forme de prospérité. Les ressources partagées, les investissements, la gestion de crise sont tes domaines.

## Ton défi
Le piège : des finances qui passent par des crises destructrices, une obsession du contrôle des ressources, confondre intensité et instabilité. La vraie prospérité transformée est aussi stable.

## Maison 2 en Scorpion
Uranus secoue tes finances pour les transformer. Tu peux gagner de l'argent dans des domaines intenses ou transformateurs. Tes valeurs sont liées à la profondeur et à l'authenticité.

## Micro-rituel du jour (2 min)
- Identifier ce qui doit mourir dans ta relation à l'argent pour renaître
- Trois respirations en faisant confiance à la transformation financière
- Journal : « Comment mes crises financières m'ont-elles transformé ? »""",

    ('scorpio', 3): """# ♅ Uranus en Scorpion
**En une phrase :** Tu communiques avec intensité transformatrice — tes mots vont au cœur des choses et changent les gens.

## Ton moteur
Uranus en Scorpion en Maison 3 te donne une communication qui pénètre les surfaces et touche les profondeurs. Tu dis ce que les autres n'osent pas dire, tu poses les questions que personne ne pose.

## Ton défi
Le piège : une communication qui manipule ou blesse, des échanges trop intenses, confondre profondeur et confrontation. La vraie communication transformatrice sait aussi être douce.

## Maison 3 en Scorpion
Uranus électrise tes échanges d'intensité et de profondeur. Tes relations avec frères, sœurs et voisins peuvent être transformatrices ou conflictuelles.

## Micro-rituel du jour (2 min)
- Partager une vérité profonde avec quelqu'un en toute bienveillance
- Trois respirations en utilisant tes mots pour transformer positivement
- Journal : « Comment ma communication peut-elle transformer sans blesser ? »""",

    ('scorpio', 4): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes la famille par la transformation — ton foyer est un creuset de morts et de renaissances.

## Ton moteur
Uranus en Scorpion en Maison 4 crée des transformations profondes dans ta vie familiale. Tu peux guérir des blessures familiales anciennes, transformer des patterns transgénérationnels.

## Ton défi
Le piège : des drames familiaux destructeurs, avoir du mal à créer de la légèreté chez toi, confondre intensité et amour. La vraie famille transformée connaît aussi la paix.

## Maison 4 en Scorpion
Uranus secoue tes fondations pour les transformer. Tu as peut-être grandi dans une famille intense ou secrète. Ton foyer peut être un lieu de guérison profonde.

## Micro-rituel du jour (2 min)
- Identifier un pattern familial que tu es en train de transformer
- Trois respirations en bénissant ton lignage
- Journal : « Quelle transformation familiale suis-je en train d'incarner ? »""",

    ('scorpio', 5): """# ♅ Uranus en Scorpion
**En une phrase :** Tu crées avec intensité transformatrice — tes œuvres et tes amours touchent les profondeurs et changent les vies.

## Ton moteur
Uranus en Scorpion en Maison 5 te pousse vers une créativité qui transforme. Tu ne crées pas pour divertir mais pour remuer, provoquer, guérir. En amour, tu cherches des partenaires avec qui vivre des transformations profondes.

## Ton défi
Le piège : des amours destructrices par intensité excessive, une créativité qui choque sans transformer, avoir du mal avec la joie légère. La vraie joie créative peut aussi être douce.

## Maison 5 en Scorpion
Uranus électrise tes plaisirs d'intensité et de passion. Tu peux vivre des passions transformatrices. Ta créativité s'épanouit dans les thèmes profonds.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui touche quelque chose de profond
- Trois respirations en laissant la joie être à la fois intense et légère
- Journal : « Quelle création transformatrice me fait vraiment vibrer ? »""",

    ('scorpio', 6): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes le travail par la transformation — ton efficacité vient quand tu peux aller en profondeur.

## Ton moteur
Uranus en Scorpion en Maison 6 te pousse vers des métiers qui transforment : thérapie, recherche, médecine, gestion de crise. Tu ne supportes pas le travail superficiel — tu dois aller au fond des choses.

## Ton défi
Le piège : un travail trop intense qui épuise, absorber les énergies négatives, avoir du mal avec les tâches légères. La vraie efficacité profonde inclut aussi le repos.

## Maison 6 en Scorpion
Uranus secoue ton quotidien pour le transformer. Tu travailles mieux quand tu peux avoir un impact profond. Ta santé peut bénéficier de thérapies transformatrices.

## Micro-rituel du jour (2 min)
- Identifier une transformation que tu apportes à ton travail
- Trois respirations en protégeant ton énergie
- Journal : « Comment mon travail peut-il transformer tout en préservant mon énergie ? »""",

    ('scorpio', 7): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes les relations par la transformation mutuelle — tes partenariats sont des alchimies de croissance.

## Ton moteur
Uranus en Scorpion en Maison 7 crée des relations transformatrices où les deux partenaires évoluent profondément. Tu attires des personnes intenses avec qui tu vis des morts et des renaissances.

## Ton défi
Le piège : des relations destructrices, des jeux de pouvoir, confondre passion et amour. Les meilleures relations transforment sans détruire.

## Maison 7 en Scorpion
Uranus électrise tes partenariats de passion et de profondeur. Tu peux vivre des relations qui te changent complètement. Tes contrats peuvent impliquer des enjeux de pouvoir.

## Micro-rituel du jour (2 min)
- Reconnaître comment une relation te transforme positivement
- Trois respirations en honorant la croissance mutuelle
- Journal : « Comment mes relations peuvent-elles transformer sans détruire ? »""",

    ('scorpio', 8): """# ♅ Uranus en Scorpion
**En une phrase :** Tu traverses les crises comme un maître — les transformations sont ton domaine naturel.

## Ton moteur
Uranus en Scorpion en Maison 8 amplifie au maximum ta capacité à traverser les crises et à en émerger transformé. Tu n'as pas peur de la mort symbolique — tu sais qu'elle précède la renaissance.

## Ton défi
Le piège : chercher les crises par addiction à l'intensité, avoir du mal avec la vie ordinaire, confondre destruction et transformation. La vraie maîtrise transformatrice inclut aussi la paix.

## Maison 8 en Scorpion
Uranus électrise au maximum ta relation aux mystères et aux transformations. Tu peux avoir des capacités de guérison ou des perceptions de l'invisible. Ta sexualité est transformatrice.

## Micro-rituel du jour (2 min)
- Identifier une transformation en cours et la bénir
- Trois respirations en accueillant la mort comme porte vers la vie
- Journal : « Quelle maîtrise ai-je gagnée de mes crises passées ? »""",

    ('scorpio', 9): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes la sagesse par la transformation — ta philosophie est celle de la mort et de la renaissance.

## Ton moteur
Uranus en Scorpion en Maison 9 te pousse vers des croyances qui embrassent les mystères de la transformation. Ta spiritualité est chamanique, initiatique, touchant aux grandes transitions.

## Ton défi
Le piège : une spiritualité obsédée par les ténèbres, avoir du mal avec la lumière et la joie, confondre profondeur et morbidité. La vraie sagesse transformatrice célèbre aussi la vie.

## Maison 9 en Scorpion
Uranus électrise ta quête de sens de profondeur et de mystère. Tes voyages peuvent être des initiations. Tu peux étudier les traditions qui touchent à la mort et à la renaissance.

## Micro-rituel du jour (2 min)
- Explorer une sagesse qui embrasse la transformation
- Trois respirations en célébrant le cycle mort-renaissance
- Journal : « Quelle sagesse transformatrice me guide actuellement ? »""",

    ('scorpio', 10): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes ta carrière par la transformation — ta réussite vient quand tu aides les autres à traverser leurs crises.

## Ton moteur
Uranus en Scorpion en Maison 10 te pousse vers une carrière de transformation : thérapeute, médecin, chercheur, gestionnaire de crise. Tu réussis en accompagnant les autres dans leurs traversées.

## Ton défi
Le piège : une carrière épuisante par trop d'intensité, absorber les crises des autres, confondre pouvoir et service. La vraie réussite transformatrice se protège aussi.

## Maison 10 en Scorpion
Uranus secoue ta réputation pour la rendre plus profonde. On te reconnaît pour ta capacité à traverser et accompagner les crises. Ta carrière peut impliquer des transformations majeures.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière transforme positivement
- Trois respirations en protégeant ton énergie professionnelle
- Journal : « Comment ma carrière peut-elle transformer tout en me préservant ? »""",

    ('scorpio', 11): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes l'action collective par la transformation — tes amitiés et tes projets touchent aux profondeurs.

## Ton moteur
Uranus en Scorpion en Maison 11 te connecte à des réseaux de personnes engagées dans la transformation. Tes amis sont des êtres de profondeur. Les projets collectifs touchent aux enjeux essentiels.

## Ton défi
Le piège : des amitiés trop intenses qui épuisent, des projets qui deviennent des luttes de pouvoir, confondre engagement et obsession. Les meilleures communautés transforment avec légèreté aussi.

## Maison 11 en Scorpion
Uranus électrise tes réseaux de profondeur et de transformation. Tu es fait pour les mouvements qui changent les structures en profondeur, les associations de guérison collective.

## Micro-rituel du jour (2 min)
- Partager une vision transformatrice avec un groupe
- Trois respirations en honorant la puissance du collectif conscient
- Journal : « Quel projet collectif de transformation m'inspire ? »""",

    ('scorpio', 12): """# ♅ Uranus en Scorpion
**En une phrase :** Tu révolutionnes ta vie intérieure par la transformation — ton inconscient est un réservoir de pouvoir régénérateur.

## Ton moteur
Uranus en Scorpion en Maison 12 crée des connexions puissantes avec les dimensions invisibles de transformation. Tu peux avoir des capacités de guérison spirituelle ou des expériences de mort-renaissance intérieure.

## Ton défi
Le piège : des abîmes intérieurs qui engloutissent, une fascination pour les ténèbres, avoir du mal à revenir à la lumière. La vraie transformation spirituelle inclut l'intégration.

## Maison 12 en Scorpion
Uranus secoue ta connexion à l'invisible pour la transformer. Tes rêves peuvent être intenses et révélateurs. Les retraites de guérison profonde te régénèrent.

## Micro-rituel du jour (2 min)
- Méditer en accueillant ce qui veut mourir en toi
- Trois respirations en faisant confiance à la renaissance
- Journal : « Quelle transformation intérieure est en cours ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in URANUS_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'uranus',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP uranus/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='uranus',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT uranus/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
