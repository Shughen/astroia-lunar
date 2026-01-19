#!/usr/bin/env python3
"""Script d'insertion des interprétations Uranus/Aries, Taurus, Gemini, Cancer en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

URANUS_INTERPRETATIONS = {
    # ARIES - 12 maisons
    ('aries', 1): """# ♅ Uranus en Bélier
**En une phrase :** Tu incarnes le pionnier de la liberté — ton identité se forge en brisant les moules et en ouvrant de nouvelles voies.

## Ton moteur
Uranus en Bélier en Maison 1 te donne une personnalité électrique et rebelle. Tu es naturellement en avance sur ton temps, pionnier de nouvelles façons d'être. L'innovation et l'indépendance sont au cœur de ton identité.

## Ton défi
Le piège : confondre rébellion et liberté, être provocateur pour le plaisir, avoir du mal avec la patience et la continuité. La vraie révolution s'ancre aussi dans la durée.

## Maison 1 en Bélier
Uranus amplifie ton besoin d'être unique et d'agir selon tes propres règles. Tu projettes une image d'audace et d'originalité. Ton apparence peut être frappante ou changer de façon soudaine.

## Micro-rituel du jour (2 min)
- Identifier un aspect de toi qui défie les conventions et le célébrer
- Trois respirations en embrassant ton unicité
- Journal : « Comment mon originalité a-t-elle inspiré les autres récemment ? »""",

    ('aries', 2): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes ta relation à l'argent — tes ressources viennent quand tu innoves et prends des risques calculés.

## Ton moteur
Uranus en Bélier en Maison 2 crée des fluctuations dans tes finances, mais aussi des opportunités soudaines. Tu génères de l'abondance par l'innovation, les projets pionniers, les approches non conventionnelles.

## Ton défi
Le piège : avoir des revenus trop instables, prendre des risques financiers excessifs, confondre innovation et imprudence. La vraie liberté financière demande aussi de la stabilité.

## Maison 2 en Bélier
Uranus secoue tes finances pour te pousser vers de nouvelles sources de revenus. Tu valorises l'indépendance financière et tu es prêt à tout changer pour l'obtenir.

## Micro-rituel du jour (2 min)
- Identifier une opportunité financière non conventionnelle
- Trois respirations en faisant confiance à ton instinct pionnier
- Journal : « Quelle innovation pourrait transformer mes revenus ? »""",

    ('aries', 3): """# ♅ Uranus en Bélier
**En une phrase :** Tu communiques avec audace et originalité — tes idées révolutionnent la façon de penser de ton entourage.

## Ton moteur
Uranus en Bélier en Maison 3 te donne une communication directe, parfois provocatrice, toujours originale. Tu dis ce que les autres n'osent pas dire, tu penses ce que les autres n'osent pas penser.

## Ton défi
Le piège : être trop abrupt ou choquant dans ta communication, avoir du mal à écouter les idées des autres, confondre originalité et confrontation. La vraie communication innovante sait aussi créer des ponts.

## Maison 3 en Bélier
Uranus électrise tes échanges et ton entourage proche. Tes relations avec frères, sœurs et voisins peuvent être stimulantes mais imprévisibles.

## Micro-rituel du jour (2 min)
- Partager une idée audacieuse avec quelqu'un de ton entourage
- Trois respirations en ouvrant ton esprit à de nouvelles perspectives
- Journal : « Quelle idée révolutionnaire m'a traversé l'esprit aujourd'hui ? »""",

    ('aries', 4): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes ta vie familiale — ton foyer devient un lieu d'expérimentation et de liberté individuelle.

## Ton moteur
Uranus en Bélier en Maison 4 crée des changements soudains dans ta vie familiale ou ton habitat. Tu as besoin d'un chez-toi qui respecte ton indépendance, même au sein de la famille.

## Ton défi
Le piège : créer de l'instabilité familiale par besoin de changement, avoir du mal à créer des racines, fuir les responsabilités domestiques. La vraie liberté sait aussi s'ancrer.

## Maison 4 en Bélier
Uranus secoue tes fondations familiales pour te libérer des conditionnements hérités. Ton foyer peut être non conventionnel ou changer souvent.

## Micro-rituel du jour (2 min)
- Identifier un aspect libérateur de ton foyer ou ta vie familiale
- Trois respirations en équilibrant liberté et appartenance
- Journal : « Comment puis-je créer un chez-moi qui honore mon besoin d'indépendance ? »""",

    ('aries', 5): """# ♅ Uranus en Bélier
**En une phrase :** Tu crées avec audace révolutionnaire — tes œuvres et tes amours sont des actes de libération.

## Ton moteur
Uranus en Bélier en Maison 5 te pousse vers une créativité radicalement originale. Tu ne crées pas pour plaire mais pour innover, choquer parfois, libérer toujours. En amour, tu cherches des partenaires qui respectent ta liberté.

## Ton défi
Le piège : des relations amoureuses instables par peur de l'engagement, une créativité qui choque sans profondeur, confondre liberté et inconstance. La vraie joie créative sait aussi se développer dans la durée.

## Maison 5 en Bélier
Uranus électrise tes plaisirs et tes amours. Tu peux avoir des coups de foudre soudains et des ruptures tout aussi rapides. Ta créativité est avant-gardiste et audacieuse.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui brise tes habitudes
- Trois respirations en laissant ta créativité être totalement libre
- Journal : « Quelle création audacieuse ai-je envie de manifester ? »""",

    ('aries', 6): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes ta façon de travailler — ton efficacité vient quand tu innoves et travailles à ta façon.

## Ton moteur
Uranus en Bélier en Maison 6 te pousse à réinventer constamment tes méthodes de travail. Tu ne supportes pas la routine imposée, tu dois créer ta propre façon de faire. Cette configuration favorise le travail indépendant ou les environnements innovants.

## Ton défi
Le piège : avoir du mal avec toute forme de routine, changer de travail trop souvent, résister aux structures même nécessaires. La vraie efficacité innovante sait aussi maintenir une discipline.

## Maison 6 en Bélier
Uranus secoue ton quotidien pour le rendre plus libre. Tu travailles mieux avec de l'autonomie totale. Ta santé peut réagir de façon soudaine au stress — écoute les signaux.

## Micro-rituel du jour (2 min)
- Identifier une routine que tu pourrais révolutionner
- Trois respirations en trouvant la liberté dans le quotidien
- Journal : « Comment puis-je travailler de façon plus alignée avec mon besoin d'indépendance ? »""",

    ('aries', 7): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes les relations — tes partenariats sont des alliances entre individus libres, pas des fusions.

## Ton moteur
Uranus en Bélier en Maison 7 crée des relations non conventionnelles où chacun garde son indépendance. Tu attires des partenaires originaux, parfois excentriques, toujours stimulants. L'amitié au sein du couple est essentielle.

## Ton défi
Le piège : des relations instables par peur de perdre ta liberté, repousser l'engagement, attirer des partenaires peu fiables. Les meilleures relations combinent liberté et engagement.

## Maison 7 en Bélier
Uranus électrise tes partenariats. Tu peux avoir des mariages soudains ou des séparations inattendues. Tes contrats bénéficient de clauses innovantes et flexibles.

## Micro-rituel du jour (2 min)
- Exprimer à un partenaire ce que tu apprécies dans votre liberté mutuelle
- Trois respirations en équilibrant connexion et indépendance
- Journal : « Comment mes relations peuvent-elles honorer la liberté de chacun ? »""",

    ('aries', 8): """# ♅ Uranus en Bélier
**En une phrase :** Tu traverses les crises comme des éveils — les transformations sont des opportunités de te libérer radicalement.

## Ton moteur
Uranus en Bélier en Maison 8 crée des transformations soudaines et libératrices. Les crises deviennent des catalyseurs de changement radical. Tu n'as pas peur de tout lâcher pour renaître différent.

## Ton défi
Le piège : provoquer des crises par besoin de changement, avoir du mal avec les transformations lentes, confondre destruction et libération. La vraie transformation intègre aussi la continuité.

## Maison 8 en Bélier
Uranus secoue ta relation aux transformations profondes. Ta sexualité peut être expérimentale ou imprévisible. Les ressources partagées peuvent arriver ou partir de façon soudaine.

## Micro-rituel du jour (2 min)
- Identifier ce que tu es prêt à lâcher pour te libérer
- Trois respirations en accueillant le changement radical
- Journal : « Quelle transformation soudaine m'a récemment libéré ? »""",

    ('aries', 9): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes ta vision du monde — ta philosophie est pionnière, en avance sur son temps.

## Ton moteur
Uranus en Bélier en Maison 9 te pousse vers des croyances radicalement originales. Tu ne te satisfais pas des philosophies établies — tu dois forger la tienne. Les voyages peuvent être soudains et transformateurs.

## Ton défi
Le piège : rejeter toutes les traditions sans discernement, avoir des croyances trop iconoclastes pour être partagées, confondre originalité et vérité. La vraie sagesse intègre aussi le passé.

## Maison 9 en Bélier
Uranus électrise ta quête de sens. Tu peux être attiré par des philosophies révolutionnaires, des spiritualités alternatives, des études de pointe. Les voyages sont des aventures d'éveil.

## Micro-rituel du jour (2 min)
- Explorer une idée philosophique qui challenge tes croyances
- Trois respirations en ouvrant ton esprit à l'inconnu
- Journal : « Quelle vision révolutionnaire me passionne actuellement ? »""",

    ('aries', 10): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes ta carrière — ta réussite vient quand tu oses être pionnier dans ton domaine.

## Ton moteur
Uranus en Bélier en Maison 10 te pousse vers une carrière où tu peux innover et diriger à ta façon. Tu ne supportes pas les hiérarchies rigides — tu dois tracer ta propre voie professionnelle. Les changements de carrière peuvent être soudains.

## Ton défi
Le piège : une carrière trop instable, avoir du mal avec l'autorité, saboter ta réussite par rébellion. La vraie révolution professionnelle sait aussi travailler avec le système.

## Maison 10 en Bélier
Uranus secoue ta réputation et ton statut. On te remarque pour ton audace et ton originalité. Ta carrière peut connaître des retournements spectaculaires, en bien ou en mal.

## Micro-rituel du jour (2 min)
- Identifier comment tu peux innover dans ton domaine professionnel
- Trois respirations en osant être un pionnier
- Journal : « Quelle révolution ai-je envie de mener dans ma carrière ? »""",

    ('aries', 11): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes l'action collective — tes amitiés et tes projets sont des avant-gardes du changement.

## Ton moteur
Uranus en Bélier en Maison 11 te connecte à des réseaux de pionniers et d'innovateurs. Tes amis sont des originaux, des rebelles, des visionnaires. Les projets collectifs sont audacieux et révolutionnaires.

## Ton défi
Le piège : des amitiés instables par besoin d'indépendance, imposer tes visions aux groupes, confondre leadership et domination. Les meilleures communautés respectent la diversité.

## Maison 11 en Bélier
Uranus électrise tes réseaux et tes idéaux. Tu es fait pour les mouvements d'avant-garde, les causes révolutionnaires. Tes amis peuvent être imprévisibles mais toujours stimulants.

## Micro-rituel du jour (2 min)
- Partager une vision audacieuse avec un ami ou un groupe
- Trois respirations en honorant la force du collectif innovant
- Journal : « Quel projet collectif révolutionnaire m'inspire ? »""",

    ('aries', 12): """# ♅ Uranus en Bélier
**En une phrase :** Tu révolutionnes ta vie intérieure — ton inconscient est une source d'éveils soudains et de libérations profondes.

## Ton moteur
Uranus en Bélier en Maison 12 crée des éveils spirituels soudains et parfois déstabilisants. Ton inconscient est un réservoir de révolutions personnelles. Les rêves peuvent être prophétiques ou libérateurs.

## Ton défi
Le piège : des périodes d'instabilité psychique, avoir du mal à intégrer les éveils soudains, fuir dans l'irrationnel. La vraie libération intérieure s'ancre aussi dans la réalité.

## Maison 12 en Bélier
Uranus secoue ta connexion à l'invisible. Tu peux avoir des intuitions fulgurantes, des prises de conscience soudaines. Les retraites peuvent provoquer des transformations radicales.

## Micro-rituel du jour (2 min)
- Méditer en accueillant ce qui veut émerger sans contrôle
- Trois respirations en faisant confiance à ton inconscient révolutionnaire
- Journal : « Quel éveil soudain m'a récemment transformé ? »""",

    # TAURUS - 12 maisons
    ('taurus', 1): """# ♅ Uranus en Taureau
**En une phrase :** Tu incarnes une révolution ancrée — tu changes les structures matérielles avec patience et détermination.

## Ton moteur
Uranus en Taureau en Maison 1 te donne une personnalité qui allie stabilité et innovation. Tu révolutionnes de l'intérieur, progressivement mais sûrement. Ton originalité s'exprime à travers les sens et la matière.

## Ton défi
Le piège : résister au changement par attachement à la sécurité, ou au contraire subir des bouleversements qui te déstabilisent. La vraie révolution se fait aussi dans la durée.

## Maison 1 en Taureau
Uranus secoue ton rapport au corps et aux sens. Ton apparence peut évoluer de façon surprenante. Tu projettes une image de solidité avec une touche d'inattendu.

## Micro-rituel du jour (2 min)
- Identifier un changement que tu intègres progressivement dans ta vie
- Trois respirations en ancrant l'innovation dans ton corps
- Journal : « Comment mon originalité s'exprime-t-elle de façon concrète ? »""",

    ('taurus', 2): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes ta relation aux ressources — ta prospérité vient de nouvelles façons de créer de la valeur.

## Ton moteur
Uranus en Taureau en Maison 2 crée des innovations dans ta façon de gagner et gérer l'argent. Tu peux être attiré par les nouvelles économies, les technologies financières, les formes alternatives de valeur.

## Ton défi
Le piège : des finances qui fluctuent de façon déstabilisante, résister aux nouvelles façons de prospérer, confondre innovation et instabilité. La vraie prospérité innovante reste ancrée.

## Maison 2 en Taureau
Uranus secoue tes finances pour les transformer. Tu peux passer par des phases d'insécurité financière qui te poussent à trouver de nouvelles sources de revenus.

## Micro-rituel du jour (2 min)
- Explorer une nouvelle façon de créer de la valeur
- Trois respirations en faisant confiance au changement financier
- Journal : « Quelle innovation pourrait stabiliser mes finances différemment ? »""",

    ('taurus', 3): """# ♅ Uranus en Taureau
**En une phrase :** Tu communiques des idées révolutionnaires de façon concrète — tes mots changent les choses tangiblement.

## Ton moteur
Uranus en Taureau en Maison 3 te donne une communication qui allie innovation et pragmatisme. Tu sais présenter les idées nouvelles de façon accessible et pratique.

## Ton défi
Le piège : avoir du mal à communiquer tes idées révolutionnaires, être trop fixé sur tes opinions, résister aux nouvelles façons de communiquer. La vraie communication innovante reste accessible.

## Maison 3 en Taureau
Uranus secoue tes échanges pour les rendre plus authentiques. Tes relations avec frères, sœurs et voisins peuvent connaître des changements qui libèrent.

## Micro-rituel du jour (2 min)
- Partager une idée nouvelle de façon simple et concrète
- Trois respirations en ancrant l'innovation dans les mots
- Journal : « Comment puis-je communiquer mes idées de façon plus impactante ? »""",

    ('taurus', 4): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes ta vie domestique — ton foyer devient un laboratoire de nouvelles façons de vivre.

## Ton moteur
Uranus en Taureau en Maison 4 crée des changements dans ta conception du foyer et de la sécurité. Tu peux être attiré par des habitats écologiques, des technologies domestiques innovantes, de nouvelles formes de vie familiale.

## Ton défi
Le piège : des bouleversements familiaux déstabilisants, avoir du mal à créer un foyer stable, résister aux changements nécessaires. La vraie innovation domestique crée aussi de la sécurité.

## Maison 4 en Taureau
Uranus secoue tes fondations pour les reconstruire différemment. Ton foyer peut intégrer des éléments innovants tout en restant confortable.

## Micro-rituel du jour (2 min)
- Identifier une innovation qui rendrait ton foyer plus aligné avec tes valeurs
- Trois respirations en ancrant le changement dans ton chez-toi
- Journal : « Comment mon foyer pourrait-il évoluer pour mieux me correspondre ? »""",

    ('taurus', 5): """# ♅ Uranus en Taureau
**En une phrase :** Tu crées de façon révolutionnaire et sensorielle — tes œuvres transforment notre rapport au beau et au plaisir.

## Ton moteur
Uranus en Taureau en Maison 5 te pousse vers une créativité qui révolutionne les sens. Tu peux innover dans l'art, la gastronomie, le design, tout ce qui touche au plaisir et à la beauté. En amour, tu cherches des relations qui combinent sécurité et excitation.

## Ton défi
Le piège : des amours instables par peur de l'ennui, une créativité qui reste au stade de l'idée, avoir du mal avec les plaisirs simples. La vraie joie créative sait aussi apprécier la constance.

## Maison 5 en Taureau
Uranus électrise tes plaisirs et ta créativité. Tu peux avoir des attirances soudaines pour des personnes très différentes de ton type habituel.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui allie innovation et sensorialité
- Trois respirations en savourant la beauté de l'inattendu
- Journal : « Quelle création sensorielle m'inspire actuellement ? »""",

    ('taurus', 6): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes ta façon de travailler — ton efficacité vient de méthodes innovantes ancrées dans le concret.

## Ton moteur
Uranus en Taureau en Maison 6 te pousse à transformer tes routines de travail de façon pratique. Tu peux être attiré par les nouvelles technologies au service du bien-être, les méthodes de travail alternatives mais efficaces.

## Ton défi
Le piège : des routines instables, résister aux changements nécessaires dans ton travail, avoir du mal à trouver un équilibre. La vraie efficacité innovante reste régulière.

## Maison 6 en Taureau
Uranus secoue ton quotidien pour le rendre plus aligné. Ta santé peut bénéficier d'approches innovantes mais douces. Ton travail évolue vers plus d'autonomie.

## Micro-rituel du jour (2 min)
- Identifier une routine que tu pourrais améliorer avec une innovation pratique
- Trois respirations en ancrant le changement dans le quotidien
- Journal : « Quelle innovation concrète améliorerait mon bien-être au travail ? »""",

    ('taurus', 7): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes les relations de façon durable — tes partenariats allient liberté et fidélité.

## Ton moteur
Uranus en Taureau en Maison 7 crée des relations qui sortent de l'ordinaire tout en restant stables. Tu attires des partenaires qui apportent de l'excitation dans ta vie tout en étant fiables.

## Ton défi
Le piège : des relations qui vacillent entre besoin de sécurité et besoin de changement, attirer des partenaires imprévisibles, avoir du mal à t'engager. Les meilleures relations évoluent ensemble.

## Maison 7 en Taureau
Uranus secoue tes partenariats pour les rendre plus authentiques. Tu peux vivre des changements relationnels qui te libèrent tout en créant de nouvelles formes de stabilité.

## Micro-rituel du jour (2 min)
- Exprimer à un partenaire une appréciation pour votre évolution commune
- Trois respirations en accueillant le changement dans la relation
- Journal : « Comment ma relation évolue-t-elle vers plus d'authenticité ? »""",

    ('taurus', 8): """# ♅ Uranus en Taureau
**En une phrase :** Tu traverses les transformations avec ancrage — les crises deviennent des occasions de reconstruire plus solidement.

## Ton moteur
Uranus en Taureau en Maison 8 crée des transformations qui changent ta relation aux ressources partagées et à l'intimité. Tu peux vivre des renversements financiers ou émotionnels qui te poussent à reconstruire.

## Ton défi
Le piège : résister aux transformations nécessaires par peur de l'instabilité, ou au contraire subir des crises déstabilisantes. La vraie transformation sait aussi préserver ce qui est essentiel.

## Maison 8 en Taureau
Uranus secoue ta relation à l'intimité et aux ressources partagées. Ta sexualité peut être à la fois sensuelle et expérimentale. Les héritages ou investissements peuvent connaître des changements.

## Micro-rituel du jour (2 min)
- Identifier une transformation en cours et comment la traverser avec ancrage
- Trois respirations en accueillant le changement profond
- Journal : « Quelle crise m'a récemment permis de reconstruire plus solidement ? »""",

    ('taurus', 9): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes ta vision du monde de façon pratique — ta philosophie transforme le concret.

## Ton moteur
Uranus en Taureau en Maison 9 te pousse vers des croyances qui changent notre rapport à la matière, à la nature, à l'économie. Tu peux être attiré par l'écologie profonde, les nouvelles économies, les spiritualités incarnées.

## Ton défi
Le piège : avoir des croyances trop fixes ou au contraire trop changeantes, avoir du mal à intégrer l'abstrait et le concret. La vraie sagesse révolutionnaire transforme aussi le quotidien.

## Maison 9 en Taureau
Uranus secoue ta quête de sens pour l'ancrer dans la réalité. Tes voyages peuvent te reconnecter à la terre et à la nature. Tes études peuvent toucher à l'écologie ou aux ressources.

## Micro-rituel du jour (2 min)
- Explorer une idée qui change notre rapport au monde matériel
- Trois respirations en ancrant ta vision dans la terre
- Journal : « Quelle philosophie incarnée me guide actuellement ? »""",

    ('taurus', 10): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes ta carrière de façon durable — ta réussite vient quand tu innoves dans les domaines concrets.

## Ton moteur
Uranus en Taureau en Maison 10 te pousse vers une carrière qui transforme notre rapport aux ressources, à l'économie, à la terre. Tu peux réussir dans les nouvelles économies, les technologies vertes, les innovations concrètes.

## Ton défi
Le piège : une carrière instable entre tradition et innovation, avoir du mal avec le long terme, vouloir tout changer trop vite. La vraie révolution professionnelle s'ancre dans la durée.

## Maison 10 en Taureau
Uranus secoue ta réputation pour la rendre plus authentique. On te remarque pour ta capacité à innover de façon pratique. Ta carrière peut connaître des tournants qui t'ancrent différemment.

## Micro-rituel du jour (2 min)
- Identifier comment tu peux innover de façon durable dans ton domaine
- Trois respirations en alignant ambition et valeurs
- Journal : « Quelle innovation concrète pourrait transformer ma carrière ? »""",

    ('taurus', 11): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes l'action collective de façon concrète — tes projets changent la façon dont nous partageons les ressources.

## Ton moteur
Uranus en Taureau en Maison 11 te connecte à des réseaux qui transforment l'économie et notre rapport aux ressources. Tes amis partagent tes préoccupations pour l'avenir de la planète et les nouvelles formes de prospérité.

## Ton défi
Le piège : des amitiés qui fluctuent avec tes valeurs, des projets qui restent au stade de l'idée, avoir du mal à concrétiser les visions collectives. Les meilleures communautés passent à l'action.

## Maison 11 en Taureau
Uranus secoue tes réseaux pour les rendre plus alignés. Tu es fait pour les projets collectifs qui transforment concrètement le monde. Tes amis peuvent être des innovateurs pratiques.

## Micro-rituel du jour (2 min)
- Partager une vision concrète avec un groupe ou un ami
- Trois respirations en honorant le pouvoir du collectif ancré
- Journal : « Quel projet collectif concret m'inspire actuellement ? »""",

    ('taurus', 12): """# ♅ Uranus en Taureau
**En une phrase :** Tu révolutionnes ta vie intérieure de façon incarnée — ton inconscient te guide vers de nouvelles façons d'habiter ton corps et la terre.

## Ton moteur
Uranus en Taureau en Maison 12 crée des éveils qui changent ta relation au corps, à la nature, au monde matériel. Ton inconscient peut te guider vers des guérisons physiques ou des transformations de ton rapport à la terre.

## Ton défi
Le piège : ignorer les messages du corps, résister aux transformations profondes, se couper de la nature. La vraie libération intérieure s'incarne aussi physiquement.

## Maison 12 en Taureau
Uranus secoue ta connexion à l'invisible pour l'ancrer dans le corps. Tes rêves peuvent contenir des messages sur ta santé ou ta relation à la terre. Les pratiques méditatives corporelles te conviennent.

## Micro-rituel du jour (2 min)
- Méditer en portant attention aux sensations de ton corps
- Trois respirations en te connectant à la terre
- Journal : « Quel message de mon corps ai-je besoin d'entendre ? »""",

    # GEMINI - 12 maisons
    ('gemini', 1): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu incarnes la révolution de la pensée — ton identité se forge en connectant les idées de façon innovante.

## Ton moteur
Uranus en Gémeaux en Maison 1 te donne un mental brillant et une curiosité insatiable pour tout ce qui est nouveau. Tu penses plus vite que les autres, tu fais des connexions que personne ne voit.

## Ton défi
Le piège : une pensée trop dispersée, avoir du mal à te fixer sur une idée, être perçu comme superficiel ou inconstant. La vraie innovation mentale sait aussi approfondir.

## Maison 1 en Gémeaux
Uranus électrise ton intelligence et ta communication. Tu projettes une image de vivacité et d'originalité intellectuelle. Ton apparence peut refléter ta polyvalence.

## Micro-rituel du jour (2 min)
- Identifier une connexion originale entre deux idées apparemment sans rapport
- Trois respirations en célébrant l'agilité de ton esprit
- Journal : « Quelle idée innovante m'a traversé l'esprit aujourd'hui ? »""",

    ('gemini', 2): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes ta prospérité par les idées — tes ressources viennent de ta capacité à innover intellectuellement.

## Ton moteur
Uranus en Gémeaux en Maison 2 crée des revenus par la communication, les idées, la technologie de l'information. Tu peux avoir plusieurs sources de revenus liées à ta polyvalence mentale.

## Ton défi
Le piège : des revenus trop dispersés ou instables, sous-valoriser tes talents intellectuels, confondre quantité d'idées et valeur. La vraie prospérité intellectuelle sait aussi se concentrer.

## Maison 2 en Gémeaux
Uranus secoue tes finances pour les diversifier. Tu peux gagner de l'argent de façons multiples et innovantes. Tes valeurs sont liées à la liberté de penser et de communiquer.

## Micro-rituel du jour (2 min)
- Identifier une idée que tu pourrais monétiser
- Trois respirations en valorisant ton intelligence
- Journal : « Comment mes idées peuvent-elles créer de la valeur ? »""",

    ('gemini', 3): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes la communication — tes idées changent la façon dont les gens pensent et échangent.

## Ton moteur
Uranus en Gémeaux en Maison 3 te donne une communication brillante et innovante. Tu es fait pour les nouvelles technologies de communication, les médias, l'enseignement révolutionnaire.

## Ton défi
Le piège : une communication trop dispersée, avoir du mal à être compris, sauter d'une idée à l'autre trop vite. La vraie communication innovante sait aussi être claire.

## Maison 3 en Gémeaux
Uranus amplifie au maximum ton intelligence et ta curiosité. Tes échanges sont stimulants et imprévisibles. Tu peux avoir de nombreux contacts mais des relations moins profondes.

## Micro-rituel du jour (2 min)
- Partager une idée innovante de façon claire avec quelqu'un
- Trois respirations en canalisant ton flux mental
- Journal : « Comment puis-je communiquer mes idées de façon plus impactante ? »""",

    ('gemini', 4): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes ta vie familiale par la communication — ton foyer est un lieu d'échanges et de stimulation intellectuelle.

## Ton moteur
Uranus en Gémeaux en Maison 4 crée un environnement familial stimulant et changeant. Tu as besoin d'un foyer qui nourrit ta curiosité, où les idées circulent librement.

## Ton défi
Le piège : un foyer trop instable ou dispersé, avoir du mal à créer des racines émotionnelles, privilégier l'intellect sur le cœur dans la famille. La vraie maison nourrit aussi les émotions.

## Maison 4 en Gémeaux
Uranus secoue ta vie familiale pour la rendre plus libre. Ton foyer peut être un lieu de passage, connecté au monde par la technologie. Tu peux avoir plusieurs lieux que tu appelles chez toi.

## Micro-rituel du jour (2 min)
- Créer un moment d'échange intellectuel stimulant chez toi
- Trois respirations en ancrant la curiosité dans ton foyer
- Journal : « Comment mon chez-moi nourrit-il mon esprit ? »""",

    ('gemini', 5): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu crées avec l'esprit — tes œuvres et tes amours sont des aventures intellectuelles innovantes.

## Ton moteur
Uranus en Gémeaux en Maison 5 te pousse vers une créativité mentale et communicative. Tu peux exceller dans l'écriture, les médias, la création de contenu. En amour, tu cherches des partenaires qui stimulent ton esprit.

## Ton défi
Le piège : des amours trop cérébrales, une créativité qui reste au niveau des idées, avoir du mal avec l'engagement émotionnel. La vraie joie créative inclut aussi le cœur.

## Maison 5 en Gémeaux
Uranus électrise tes plaisirs intellectuels. Tu peux avoir plusieurs amours en même temps ou des relations basées sur la stimulation mentale. Ta créativité est polyvalente et rapide.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui stimule ton esprit
- Trois respirations en laissant ta créativité jouer
- Journal : « Quelle création intellectuelle me ferait vraiment plaisir ? »""",

    ('gemini', 6): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes ta façon de travailler par l'intelligence — ton efficacité vient de méthodes mentales innovantes.

## Ton moteur
Uranus en Gémeaux en Maison 6 te pousse à trouver des solutions intelligentes aux problèmes quotidiens. Tu excelles dans l'optimisation, l'automatisation, les méthodes de travail innovantes.

## Ton défi
Le piège : un quotidien trop dispersé, avoir du mal avec les tâches répétitives, changer de méthode trop souvent. La vraie efficacité intelligente sait aussi maintenir ce qui fonctionne.

## Maison 6 en Gémeaux
Uranus secoue tes routines pour les rendre plus intelligentes. Tu travailles mieux avec de la variété et de la stimulation mentale. Ta santé peut bénéficier des dernières informations.

## Micro-rituel du jour (2 min)
- Identifier une tâche répétitive que tu pourrais optimiser intelligemment
- Trois respirations en trouvant la curiosité dans le quotidien
- Journal : « Quelle solution innovante simplifierait mon travail ? »""",

    ('gemini', 7): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes les relations par la communication — tes partenariats sont des échanges intellectuels libres.

## Ton moteur
Uranus en Gémeaux en Maison 7 crée des relations basées sur la stimulation mentale et la liberté d'expression. Tu attires des partenaires intelligents, communicatifs, parfois multiples.

## Ton défi
Le piège : des relations trop superficielles ou multiples, avoir du mal avec l'engagement émotionnel profond, confondre communication et connexion. Les meilleures relations incluent aussi le cœur.

## Maison 7 en Gémeaux
Uranus électrise tes partenariats. Tu peux vivre des relations à distance ou basées sur l'échange d'idées. Tes contrats peuvent être multiples ou innovants.

## Micro-rituel du jour (2 min)
- Avoir une conversation profonde et stimulante avec un partenaire
- Trois respirations en équilibrant mental et cœur dans la relation
- Journal : « Comment mes relations peuvent-elles être à la fois stimulantes et profondes ? »""",

    ('gemini', 8): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu traverses les crises par la compréhension — les transformations deviennent des occasions d'apprendre et de communiquer.

## Ton moteur
Uranus en Gémeaux en Maison 8 te donne la capacité de comprendre intellectuellement les crises et de les traverser par la communication. Tu peux aider les autres à traverser leurs transformations par tes mots.

## Ton défi
Le piège : intellectualiser les émotions au lieu de les vivre, avoir du mal avec l'intimité profonde, fuir les transformations dans la dispersion. La vraie transformation inclut aussi le ressenti.

## Maison 8 en Gémeaux
Uranus secoue ta relation aux mystères pour les éclairer. Tu peux avoir des intuitions fulgurantes sur les situations cachées. Ta sexualité peut être expérimentale ou communicative.

## Micro-rituel du jour (2 min)
- Mettre des mots sur une transformation que tu traverses
- Trois respirations en accueillant à la fois compréhension et ressenti
- Journal : « Qu'ai-je compris récemment sur mes propres transformations ? »""",

    ('gemini', 9): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes la pensée — ta philosophie est une synthèse innovante d'idées multiples.

## Ton moteur
Uranus en Gémeaux en Maison 9 te pousse vers une quête de sens intellectuellement stimulante. Tu connectes des savoirs différents pour créer une vision nouvelle. L'enseignement et la diffusion d'idées sont tes voies.

## Ton défi
Le piège : une philosophie trop changeante ou dispersée, avoir du mal à approfondir, confondre quantité d'informations et sagesse. La vraie sagesse sait aussi se concentrer.

## Maison 9 en Gémeaux
Uranus électrise ta quête de sens. Tu peux voyager mentalement plus que physiquement, étudier de nombreux domaines, enseigner de façon innovante.

## Micro-rituel du jour (2 min)
- Connecter deux idées de domaines différents pour créer une vision nouvelle
- Trois respirations en célébrant ta synthèse mentale
- Journal : « Quelle connexion d'idées m'a récemment illuminé ? »""",

    ('gemini', 10): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes ta carrière par les idées — ta réussite vient de ta capacité à communiquer l'innovation.

## Ton moteur
Uranus en Gémeaux en Maison 10 te pousse vers une carrière dans la communication, les médias, la technologie de l'information. Tu réussis en étant le messager de l'innovation.

## Ton défi
Le piège : une carrière dispersée entre trop d'options, avoir du mal à te positionner, changer de direction trop souvent. La vraie réussite communicative sait aussi se spécialiser.

## Maison 10 en Gémeaux
Uranus secoue ta réputation pour la rendre plus dynamique. On te remarque pour ton intelligence et ta polyvalence. Ta carrière peut impliquer plusieurs activités ou évoluer rapidement.

## Micro-rituel du jour (2 min)
- Identifier comment tu peux mieux communiquer ton expertise
- Trois respirations en alignant intellect et ambition
- Journal : « Comment mes idées peuvent-elles servir ma carrière ? »""",

    ('gemini', 11): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes les réseaux par la communication — tes amitiés et tes projets sont des échanges d'idées innovantes.

## Ton moteur
Uranus en Gémeaux en Maison 11 te connecte à des réseaux de penseurs, communicateurs, innovateurs. Tes amis sont des sources d'idées nouvelles. Les projets collectifs sont basés sur l'échange d'informations.

## Ton défi
Le piège : des amitiés trop superficielles ou nombreuses, des projets qui restent au stade de l'idée, avoir du mal à approfondir les liens. Les meilleures communautés créent aussi de la profondeur.

## Maison 11 en Gémeaux
Uranus amplifie tes réseaux de communication. Tu es fait pour les communautés en ligne, les groupes de réflexion, les projets médiatiques collectifs.

## Micro-rituel du jour (2 min)
- Partager une idée stimulante avec ton réseau
- Trois respirations en honorant la force du collectif intellectuel
- Journal : « Quel échange d'idées m'a récemment inspiré ? »""",

    ('gemini', 12): """# ♅ Uranus en Gémeaux
**En une phrase :** Tu révolutionnes ta vie intérieure par la compréhension — ton inconscient est une source d'idées et d'intuitions fulgurantes.

## Ton moteur
Uranus en Gémeaux en Maison 12 crée des connexions entre ton conscient et ton inconscient sous forme d'idées et d'insights soudains. Tes rêves peuvent contenir des messages clairs. L'écriture automatique peut être une voie.

## Ton défi
Le piège : mentaliser la vie intérieure au lieu de la vivre, être submergé par le flux d'idées, avoir du mal avec le silence. La vraie sagesse intérieure sait aussi se taire.

## Maison 12 en Gémeaux
Uranus secoue ta connexion à l'invisible par des éclairs de compréhension. Tu peux avoir des intuitions sur les pensées des autres. Les retraites de méditation peuvent être difficiles mais transformatrices.

## Micro-rituel du jour (2 min)
- Méditer en observant le flux de tes pensées sans t'y attacher
- Trois respirations dans le silence mental
- Journal : « Quelle intuition fulgurante m'a récemment traversé ? »""",

    # CANCER - 12 maisons
    ('cancer', 1): """# ♅ Uranus en Cancer
**En une phrase :** Tu incarnes une révolution émotionnelle — ton identité se forge en libérant de nouvelles façons de ressentir et d'appartenir.

## Ton moteur
Uranus en Cancer en Maison 1 te donne une sensibilité hors normes et une façon originale de vivre tes émotions. Tu révolutionnes le rapport au foyer, à la famille, aux racines.

## Ton défi
Le piège : des émotions imprévisibles qui déstabilisent, avoir du mal à créer de la sécurité, osciller entre besoin d'appartenance et besoin de liberté. La vraie libération émotionnelle crée aussi de l'ancrage.

## Maison 1 en Cancer
Uranus secoue ton identité émotionnelle. Tu projettes une image de sensibilité unique. Ton apparence peut refléter tes états émotionnels changeants.

## Micro-rituel du jour (2 min)
- Identifier une émotion que tu vis de façon originale et l'honorer
- Trois respirations en accueillant ta sensibilité révolutionnaire
- Journal : « Comment mes émotions me distinguent-elles ? »""",

    ('cancer', 2): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes ta sécurité — tes ressources viennent quand tu crées de nouvelles formes de nourriture et de protection.

## Ton moteur
Uranus en Cancer en Maison 2 crée des changements dans ta façon de gagner et de valoriser. Tu peux générer des revenus par tout ce qui nourrit : alimentation, habitat, soins, famille.

## Ton défi
Le piège : une sécurité financière instable qui te déstabilise émotionnellement, confondre sécurité et argent, avoir du mal à te sentir en sécurité. La vraie prospérité nourrit aussi l'âme.

## Maison 2 en Cancer
Uranus secoue tes finances pour les relier à ta vraie sécurité. Tu peux avoir des revenus liés au foyer, à la famille, aux soins. Tes valeurs sont émotionnelles et familiales.

## Micro-rituel du jour (2 min)
- Identifier ce qui te fait vraiment te sentir en sécurité au-delà de l'argent
- Trois respirations en nourrissant ta vraie sécurité
- Journal : « Comment puis-je créer une prospérité qui nourrit mon âme ? »""",

    ('cancer', 3): """# ♅ Uranus en Cancer
**En une phrase :** Tu communiques avec le cœur — tes mots créent de nouvelles formes de connexion émotionnelle.

## Ton moteur
Uranus en Cancer en Maison 3 te donne une communication intuitive et émotionnelle. Tu perçois et exprimes des choses que les autres ne savent pas dire. Tes échanges créent des liens de cœur.

## Ton défi
Le piège : une communication trop émotionnelle ou imprévisible, avoir du mal à être objectif, laisser les émotions perturber les échanges. La vraie communication du cœur sait aussi être claire.

## Maison 3 en Cancer
Uranus secoue tes échanges pour les rendre plus authentiques émotionnellement. Tes relations avec frères, sœurs et voisins peuvent connaître des changements qui libèrent des non-dits.

## Micro-rituel du jour (2 min)
- Partager une émotion authentique avec quelqu'un de ton entourage
- Trois respirations en ouvrant ton cœur dans la communication
- Journal : « Quel non-dit émotionnel ai-je besoin d'exprimer ? »""",

    ('cancer', 4): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes la famille — ton foyer devient un laboratoire de nouvelles formes d'appartenance.

## Ton moteur
Uranus en Cancer en Maison 4 crée des transformations profondes dans ta conception de la famille et du foyer. Tu peux créer des familles choisies, des foyers non conventionnels, des nouvelles formes d'appartenance.

## Ton défi
Le piège : des bouleversements familiaux déstabilisants, avoir du mal à créer de la continuité, couper les racines par besoin de liberté. La vraie libération familiale crée aussi de nouvelles racines.

## Maison 4 en Cancer
Uranus secoue au maximum tes fondations émotionnelles. Tu peux vivre des changements familiaux majeurs qui te libèrent de conditionnements anciens. Ton foyer évolue avec toi.

## Micro-rituel du jour (2 min)
- Identifier ce que tu veux créer comme nouvelle forme de famille ou d'appartenance
- Trois respirations en honorant tes racines tout en t'en libérant
- Journal : « Quelle est ma vision d'une famille libérée ? »""",

    ('cancer', 5): """# ♅ Uranus en Cancer
**En une phrase :** Tu crées avec le cœur — tes œuvres et tes amours sont des expressions révolutionnaires de tendresse.

## Ton moteur
Uranus en Cancer en Maison 5 te pousse vers une créativité qui nourrit et protège de façon originale. En amour, tu cherches des connexions émotionnelles profondes mais libres.

## Ton défi
Le piège : des amours déstabilisantes émotionnellement, une créativité bloquée par la peur, avoir du mal avec la joie légère. La vraie joie créative sait aussi être ludique.

## Maison 5 en Cancer
Uranus électrise tes émotions dans les plaisirs et l'amour. Tu peux avoir des attirances soudaines pour des personnes qui éveillent ta tendresse. Ta créativité est intuitive et nourrissante.

## Micro-rituel du jour (2 min)
- T'offrir un plaisir créatif qui nourrit ton cœur
- Trois respirations en laissant la joie être douce et libre
- Journal : « Quelle création de cœur ai-je envie de manifester ? »""",

    ('cancer', 6): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes le soin — ton travail quotidien devient une façon de nourrir et protéger différemment.

## Ton moteur
Uranus en Cancer en Maison 6 te pousse vers des métiers de soin innovants. Tu peux transformer la façon dont on prend soin des autres, que ce soit dans la santé, l'alimentation, le bien-être.

## Ton défi
Le piège : absorber les émotions des autres dans le travail, un quotidien émotionnellement instable, confondre prendre soin et se sacrifier. Le vrai soin durable inclut ta propre protection.

## Maison 6 en Cancer
Uranus secoue tes routines pour les rendre plus nourrissantes. Tu travailles mieux dans des environnements bienveillants. Ta santé est sensible aux émotions et peut bénéficier de nouvelles approches.

## Micro-rituel du jour (2 min)
- Identifier une façon de prendre soin qui te nourrit aussi
- Trois respirations en équilibrant donner et recevoir
- Journal : « Comment puis-je révolutionner ma façon de prendre soin ? »""",

    ('cancer', 7): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes l'intimité — tes relations créent de nouvelles formes de famille et d'appartenance.

## Ton moteur
Uranus en Cancer en Maison 7 crée des partenariats qui réinventent l'intimité et la famille. Tu attires des partenaires avec qui tu crées des formes d'union non conventionnelles.

## Ton défi
Le piège : des relations émotionnellement instables, avoir du mal à trouver la sécurité dans le couple, osciller entre fusion et indépendance. Les meilleures relations créent une nouvelle sécurité.

## Maison 7 en Cancer
Uranus secoue tes partenariats pour les rendre plus authentiquement intimes. Tu peux vivre des changements relationnels qui transforment ta conception de la famille.

## Micro-rituel du jour (2 min)
- Exprimer à un partenaire ce qui crée une vraie sécurité entre vous
- Trois respirations en créant un espace d'intimité libre
- Journal : « Quelle nouvelle forme d'intimité ai-je envie de créer ? »""",

    ('cancer', 8): """# ♅ Uranus en Cancer
**En une phrase :** Tu traverses les crises avec le cœur — les transformations deviennent des occasions de guérir émotionnellement.

## Ton moteur
Uranus en Cancer en Maison 8 crée des transformations émotionnelles profondes et libératrices. Les crises touchent au cœur mais permettent de guérir des blessures anciennes.

## Ton défi
Le piège : des crises émotionnelles déstabilisantes, avoir du mal à lâcher prise sur les attachements, confondre intensité et intimité. La vraie transformation émotionnelle apporte aussi de la paix.

## Maison 8 en Cancer
Uranus secoue tes attachements pour les libérer. Ta relation à l'intimité et à la mort symbolique peut être transformée par des expériences profondes. L'héritage émotionnel familial peut être guéri.

## Micro-rituel du jour (2 min)
- Identifier un attachement émotionnel que tu es prêt à transformer
- Trois respirations en accueillant la guérison profonde
- Journal : « Quelle blessure émotionnelle est prête à guérir ? »""",

    ('cancer', 9): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes la sagesse du cœur — ta philosophie est basée sur l'amour inconditionnel et l'appartenance universelle.

## Ton moteur
Uranus en Cancer en Maison 9 te pousse vers une spiritualité du cœur qui transcende les frontières. Tu peux trouver ta famille spirituelle partout dans le monde.

## Ton défi
Le piège : des croyances émotionnellement instables, avoir du mal à élargir ton cercle d'appartenance, confondre tradition et vérité. La vraie sagesse du cœur est universelle.

## Maison 9 en Cancer
Uranus secoue ta quête de sens pour l'ancrer dans le cœur. Tes voyages peuvent créer des liens de famille avec des personnes de toutes cultures. Ta spiritualité est nourrissante.

## Micro-rituel du jour (2 min)
- Méditer sur l'appartenance universelle de tous les êtres
- Trois respirations en élargissant ton cercle de compassion
- Journal : « Où ai-je trouvé de la famille inattendue ? »""",

    ('cancer', 10): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes ta carrière par le cœur — ta réussite vient quand tu nourris et protèges le monde de façon innovante.

## Ton moteur
Uranus en Cancer en Maison 10 te pousse vers une carrière qui prend soin du monde de façon nouvelle. Tu peux réussir dans tout ce qui nourrit, protège, crée de l'appartenance.

## Ton défi
Le piège : une carrière émotionnellement instable, avoir du mal à être reconnu pour ta sensibilité, confondre profession et famille. La vraie réussite nourrissante a aussi des limites.

## Maison 10 en Cancer
Uranus secoue ta réputation pour la rendre plus authentiquement bienveillante. On te reconnaît pour ta capacité à prendre soin de façon innovante.

## Micro-rituel du jour (2 min)
- Identifier comment ta carrière peut mieux nourrir le monde
- Trois respirations en alignant ambition et cœur
- Journal : « Comment ma profession peut-elle créer plus d'appartenance ? »""",

    ('cancer', 11): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes l'action collective par le cœur — tes amitiés et tes projets créent des familles choisies.

## Ton moteur
Uranus en Cancer en Maison 11 te connecte à des réseaux qui deviennent des familles. Tes amis sont des âmes sœurs avec qui tu partages des liens profonds. Les projets collectifs nourrissent et protègent.

## Ton défi
Le piège : des amitiés émotionnellement intenses mais instables, avoir du mal avec les groupes impersonnels, confondre amitié et famille. Les meilleures communautés respectent aussi l'indépendance.

## Maison 11 en Cancer
Uranus secoue tes réseaux pour créer de vraies familles d'âmes. Tu es fait pour les communautés de soutien, les projets qui prennent soin du collectif.

## Micro-rituel du jour (2 min)
- Partager un moment de cœur avec un ami ou un groupe
- Trois respirations en honorant ta famille choisie
- Journal : « Quelle communauté me nourrit comme une famille ? »""",

    ('cancer', 12): """# ♅ Uranus en Cancer
**En une phrase :** Tu révolutionnes ta vie intérieure par le cœur — ton inconscient est une source de guérison émotionnelle profonde.

## Ton moteur
Uranus en Cancer en Maison 12 crée des connexions profondes entre ton cœur et l'inconscient collectif. Tu peux percevoir les émotions cachées des autres et de l'humanité. Les guérisons émotionnelles peuvent être soudaines.

## Ton défi
Le piège : être submergé par les émotions collectives, avoir du mal à distinguer tes émotions de celles des autres, fuir dans les rêves. La vraie guérison intérieure inclut aussi des limites.

## Maison 12 en Cancer
Uranus secoue ta connexion à l'invisible pour l'ouvrir au cœur. Tes rêves peuvent contenir des messages de guérison. Les retraites dans des lieux nourrissants te régénèrent profondément.

## Micro-rituel du jour (2 min)
- Méditer en ouvrant ton cœur à l'inconscient
- Trois respirations en accueillant la guérison qui émerge
- Journal : « Quel message de guérison mon inconscient m'envoie-t-il ? »""",
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
