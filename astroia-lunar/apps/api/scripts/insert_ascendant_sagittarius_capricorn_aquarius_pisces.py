#!/usr/bin/env python3
"""
Insert Ascendant interpretations for Sagittarius, Capricorn, Aquarius, Pisces (48 entries)
Version 2 format with consistent structure
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from uuid import uuid4
from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation


def make_asc_interp(sign_name: str, house: int, phrase: str, masque: str, approche: str, tips: list[str]) -> str:
    """Generate Ascendant interpretation with consistent structure."""
    tips_formatted = "\n".join(f"- {t}" for t in tips)
    return f"""# ↑ Ascendant en {sign_name}

**En une phrase :** {phrase}

## Ton masque au monde
{masque}

## Ton approche spontanée
{approche}

## Pistes d'intégration
{tips_formatted}"""


ASCENDANT_INTERPRETATIONS = {
    # SAGITTARIUS ASCENDANT
    ('sagittarius', 1): make_asc_interp(
        "Sagittaire", 1,
        "Tu te présentes au monde avec optimisme — ton approche spontanée est celle de l'aventure.",
        "Ton masque est celui de l'explorateur, de l'être enthousiaste et philosophe. Les gens te perçoivent comme quelqu'un d'optimiste, aventurier et franc. Tu dégages une aura d'ouverture qui inspire la confiance. Ta présence physique est souvent grande ou expansive, avec des gestes amples.",
        "Tu abordes la vie comme une grande aventure. Face à une situation, ton instinct est d'explorer, d'élargir, de chercher le sens. Cette ouverture te rend inspirant mais parfois excessif. Tu préfères la liberté à la contrainte.",
        ["Explore la vie avec ton enthousiasme naturel.", "Canalise ton énergie pour aller en profondeur.", "Journal : « Comment mon optimisme me guide-t-il dans la vie ? »"]
    ),
    ('sagittarius', 2): make_asc_interp(
        "Sagittaire", 2,
        "Tu te présentes au monde avec générosité — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie expansive influence ta façon de gagner et de dépenser. Tu es perçu comme quelqu'un de généreux, peut-être trop. Tu vois l'argent comme un moyen pour vivre des expériences et partager. Tu crois en l'abondance.",
        "Tu abordes les questions d'argent avec optimisme. Tu peux être insouciant avec tes finances, croyant que tout s'arrangera. Tu dépenses facilement pour les voyages, l'éducation et les expériences.",
        ["Utilise tes ressources pour élargir tes horizons.", "Cultive un peu de prudence financière.", "Journal : « Comment mon optimisme influence-t-il mes finances ? »"]
    ),
    ('sagittarius', 3): make_asc_interp(
        "Sagittaire", 3,
        "Tu te présentes au monde avec enthousiasme — ton approche spontanée s'exprime dans ta communication inspirante.",
        "Ta façon de communiquer est expansive, enthousiaste et parfois excessive. Les gens te perçoivent comme quelqu'un qui a toujours quelque chose d'intéressant à dire. Dans ton environnement proche, tu es celui qui inspire et qui raconte des histoires.",
        "Tu communiques pour partager ta vision du monde. Tu as tendance à philosopher ou à prêcher. Tu peux être trop direct ou exagérer dans tes propos par enthousiasme.",
        ["Partage ta sagesse avec enthousiasme mesuré.", "Écoute autant que tu enseignes.", "Journal : « Comment mon enthousiasme colore-t-il ma communication ? »"]
    ),
    ('sagittarius', 4): make_asc_interp(
        "Sagittaire", 4,
        "Tu te présentes au monde avec ouverture — ton approche spontanée crée un foyer cosmopolite.",
        "Ton énergie d'explorateur se manifeste dans ta vie privée. Tu as besoin d'un chez-toi qui soit ouvert sur le monde — livres, souvenirs de voyage, cultures différentes. Tes racines sont marquées par l'éducation, la philosophie ou les origines étrangères.",
        "Tu abordes ta vie privée avec un besoin de liberté et d'espace. Tu peux avoir du mal à t'enraciner ou tu crées un foyer qui est un point de départ vers le monde. Ta famille est peut-être multiculturelle ou voyageuse.",
        ["Crée un foyer qui reflète ta vision du monde.", "Trouve l'équilibre entre aventure et ancrage.", "Journal : « Comment mon besoin de liberté influence-t-il ma vie familiale ? »"]
    ),
    ('sagittarius', 5): make_asc_interp(
        "Sagittaire", 5,
        "Tu te présentes au monde avec joie — ton approche spontanée s'exprime dans la créativité expansive.",
        "Ton énergie d'aventurier s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de fun et de passionnant. En amour, tu cherches l'aventure et l'expansion. Avec les enfants, tu es le parent qui ouvre le monde.",
        "Tu abordes les loisirs et la romance comme des aventures. Tu aimes les activités qui élargissent tes horizons. Tu peux t'ennuyer dans les relations ou les hobbies routiniers.",
        ["Vis tes passions comme des aventures.", "Engage-toi assez longtemps pour approfondir.", "Journal : « Comment ma soif d'aventure enrichit-elle ma créativité et mes amours ? »"]
    ),
    ('sagittarius', 6): make_asc_interp(
        "Sagittaire", 6,
        "Tu te présentes au monde avec optimisme — ton approche spontanée s'applique au travail inspiré.",
        "Ta façon d'aborder le travail quotidien et la santé est optimiste et philosophique. Tu es perçu comme quelqu'un qui apporte de l'enthousiasme au travail. Tu excelles dans les environnements qui offrent variété et sens.",
        "Tu abordes les routines avec un besoin de sens et de liberté. Tu as du mal avec les travaux répétitifs ou confinés. Ta santé dépend de ton mouvement — tu as besoin d'activité physique et de grands espaces.",
        ["Trouve du sens dans ton travail quotidien.", "Bouge ton corps régulièrement.", "Journal : « Comment mon besoin de liberté influence-t-il ma santé et mon travail ? »"]
    ),
    ('sagittarius', 7): make_asc_interp(
        "Sagittaire", 7,
        "Tu te présentes au monde avec franchise — ton approche spontanée recherche des relations expansives.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes qui élargissent tes horizons — voyageurs, philosophes, étrangers. Tu veux un partenaire qui partage ta soif d'aventure et de croissance.",
        "Tu abordes les associations avec optimisme et franchise. Tu as besoin de liberté dans tes relations. Tu peux avoir du mal avec les partenaires trop possessifs ou casaniers.",
        ["Crée des partenariats qui permettent la croissance mutuelle.", "Équilibre liberté et engagement.", "Journal : « Comment mon besoin d'expansion influence-t-il mes partenariats ? »"]
    ),
    ('sagittarius', 8): make_asc_interp(
        "Sagittaire", 8,
        "Tu te présentes au monde avec foi — ton approche spontanée s'applique aux transformations avec optimisme.",
        "Tu abordes les crises et les transformations avec foi en un sens plus grand. Tu cherches la signification derrière les épreuves. Les questions d'intimité et de transformation sont abordées avec une attitude philosophique.",
        "Face aux épreuves, ton instinct est de chercher le sens et de garder espoir. Tu peux avoir du mal à t'attarder dans la douleur, préférant voir le positif. Mais ta foi te permet de traverser les crises avec résilience.",
        ["Utilise ta foi pour naviguer les transformations.", "Permets-toi de traverser pleinement les épreuves.", "Journal : « Comment mon optimisme influence-t-il ma façon de gérer les crises ? »"]
    ),
    ('sagittarius', 9): make_asc_interp(
        "Sagittaire", 9,
        "Tu te présentes au monde comme un philosophe — ton approche spontanée s'épanouit dans la quête de sens.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie sagittarienne : expansion, sagesse, aventure. Tu es né pour explorer les horizons — géographiques et intellectuels. Tu es le grand voyageur du zodiaque.",
        "Tu abordes les études supérieures et les voyages comme ton élément naturel. Tu as une soif insatiable de comprendre le monde et son sens. Tes convictions sont généralement optimistes et expansives.",
        ["Explore tous les horizons qui t'appellent.", "Partage ta sagesse avec générosité.", "Journal : « Comment ma quête de sens s'exprime-t-elle pleinement ? »"]
    ),
    ('sagittarius', 10): make_asc_interp(
        "Sagittaire", 10,
        "Tu te présentes au monde comme un visionnaire — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un d'inspirant, visionnaire et international. Ta réputation est celle d'un sage ou d'un aventurier. Tu excelles dans les rôles qui impliquent enseignement, voyage ou expansion.",
        "Tu abordes ta carrière avec ambition et optimisme. Tu vises haut et tu veux que ton travail ait un sens plus grand. Tu as du mal avec les carrières étriquées ou sans vision.",
        ["Utilise ta vision pour inspirer.", "Construis une réputation de sagesse et d'ouverture.", "Journal : « Comment mon optimisme façonne-t-il ma vie professionnelle ? »"]
    ),
    ('sagittarius', 11): make_asc_interp(
        "Sagittaire", 11,
        "Tu te présentes au monde avec idéalisme — ton approche spontanée anime tes projets collectifs.",
        "Dans les groupes, tu apportes vision et enthousiasme. Tu attires des amis de tous horizons et tu crées des connexions internationales. Tes idéaux pour l'avenir sont généreux et universels.",
        "Tu abordes l'amitié et les projets de groupe avec ton sens de l'aventure. Tu es l'ami qui inspire et qui ouvre les portes du monde. Tu peux avoir du mal avec les groupes trop fermés ou les causes limitées.",
        ["Inspire les collectifs par ta vision.", "Travaille pour des causes universelles.", "Journal : « Comment ma vision du monde enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('sagittarius', 12): make_asc_interp(
        "Sagittaire", 12,
        "Tu te présentes au monde avec un optimisme discret — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie d'explorateur opère dans l'ombre. Tu as une vie intérieure riche en quêtes spirituelles et en visions. Tu explores les territoires invisibles avec le même enthousiasme que les visibles.",
        "Tu abordes la spiritualité et l'inconscient comme des territoires à explorer. Tu as peut-être des expériences mystiques ou des rêves significatifs. Tu peux te saboter par excès d'optimisme ou fuite dans l'idéalisme.",
        ["Explore les dimensions invisibles avec courage.", "Ancre ta spiritualité dans le quotidien.", "Journal : « Quelles vérités spirituelles je porte secrètement ? »"]
    ),

    # CAPRICORN ASCENDANT
    ('capricorn', 1): make_asc_interp(
        "Capricorne", 1,
        "Tu te présentes au monde avec sérieux — ton approche spontanée est celle de la responsabilité.",
        "Ton masque est celui du sage, de l'être mature et ambitieux. Les gens te perçoivent comme quelqu'un de sérieux, compétent et fiable. Tu dégages une aura d'autorité qui commande le respect. Ta présence physique est souvent sobre, avec une dignité naturelle.",
        "Tu abordes la vie avec détermination et réalisme. Face à une situation, ton instinct est de structurer, de planifier, d'atteindre. Cette maturité te rend accompli mais parfois trop rigide. Tu préfères la compétence à la légèreté.",
        ["Utilise ta maturité comme une force.", "Permets-toi de la légèreté parfois.", "Journal : « Comment mon sens des responsabilités me guide-t-il dans la vie ? »"]
    ),
    ('capricorn', 2): make_asc_interp(
        "Capricorne", 2,
        "Tu te présentes au monde avec solidité — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie ambitieuse influence ta façon de construire ta sécurité financière. Tu es perçu comme quelqu'un de prudent et stratégique avec l'argent. Tu construis ta richesse progressivement et durablement.",
        "Tu abordes les questions d'argent avec sérieux et vision à long terme. Tu investis dans ce qui dure, tu évites les risques inconsidérés. Tu peux être trop austère ou te priver par excès de prudence.",
        ["Construis ta sécurité avec patience et stratégie.", "Profite aussi du fruit de ton travail.", "Journal : « Comment mon ambition influence-t-elle mes finances ? »"]
    ),
    ('capricorn', 3): make_asc_interp(
        "Capricorne", 3,
        "Tu te présentes au monde avec gravité — ton approche spontanée s'exprime dans ta communication structurée.",
        "Ta façon de communiquer est mesurée, réfléchie et autoritaire. Les gens te perçoivent comme quelqu'un qui parle avec sagesse. Dans ton environnement proche, tu es celui qui structure et qui conseille. Tes échanges avec frères et sœurs peuvent être responsabilisants.",
        "Tu communiques pour informer et structurer, pas pour bavarder. Ton esprit est méthodique et stratégique. Tu peux paraître froid ou distant dans tes échanges.",
        ["Communique avec ta sagesse naturelle.", "Ajoute de la chaleur à tes échanges.", "Journal : « Comment mon sérieux colore-t-il ma communication ? »"]
    ),
    ('capricorn', 4): make_asc_interp(
        "Capricorne", 4,
        "Tu te présentes au monde avec dignité — ton approche spontanée crée un foyer structuré.",
        "Ton énergie d'accomplissement se manifeste dans ta vie privée. Tu as besoin d'un chez-toi qui soit solide, respectable et bien organisé. Tes racines sont marquées par des responsabilités précoces ou une famille traditionnelle.",
        "Tu abordes ta vie privée avec sérieux. Tu veux être le pilier de ta famille, celui sur qui on peut compter. Tu peux avoir porté des responsabilités familiales tôt ou avoir eu un parent exigeant.",
        ["Crée un foyer solide et structuré.", "Permets-toi d'être vulnérable à la maison.", "Journal : « Comment mes responsabilités façonnent-elles ma vie familiale ? »"]
    ),
    ('capricorn', 5): make_asc_interp(
        "Capricorne", 5,
        "Tu te présentes au monde avec réserve — ton approche spontanée s'exprime dans la créativité disciplinée.",
        "Ton énergie ambitieuse s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de sérieux même dans ses loisirs. En amour, tu es loyal et responsable. Avec les enfants, tu enseignes la discipline et l'accomplissement.",
        "Tu abordes les loisirs et la romance avec un certain sérieux. Tu préfères les activités qui développent tes compétences aux divertissements frivoles. Tu peux avoir du mal à simplement jouer sans but.",
        ["Exprime ta créativité avec discipline.", "Permets-toi de jouer sans objectif.", "Journal : « Comment mon sérieux influence-t-il ma créativité et mes amours ? »"]
    ),
    ('capricorn', 6): make_asc_interp(
        "Capricorne", 6,
        "Tu te présentes au monde avec professionnalisme — ton approche spontanée excelle dans le travail.",
        "Ta façon d'aborder le travail quotidien et la santé est méthodique et ambitieuse. Tu es perçu comme un travailleur acharné et compétent. Tu excelles dans les environnements structurés qui récompensent l'effort.",
        "Tu abordes les routines avec sérieux et discipline. Ta santé dépend de ta capacité à gérer le stress — tu peux te surcharger de travail. Tu as besoin de structure pour te sentir bien.",
        ["Travaille avec discipline et vision.", "Prends soin de ton corps autant que de ta carrière.", "Journal : « Comment mon ambition influence-t-elle ma santé et mon travail ? »"]
    ),
    ('capricorn', 7): make_asc_interp(
        "Capricorne", 7,
        "Tu te présentes au monde avec maturité — ton approche spontanée recherche des relations sérieuses.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes matures, ambitieuses ou stables. Tu veux un partenaire qui soit un vrai partenaire de vie, fiable et engagé. Tu prends les relations au sérieux.",
        "Tu abordes les associations avec engagement et responsabilité. Tu cherches des relations qui durent et qui construisent quelque chose. Tu peux avoir du mal avec les partenaires immatures ou instables.",
        ["Crée des partenariats solides et durables.", "Apporte aussi de la légèreté à tes relations.", "Journal : « Comment mon sens de l'engagement influence-t-il mes partenariats ? »"]
    ),
    ('capricorn', 8): make_asc_interp(
        "Capricorne", 8,
        "Tu te présentes au monde avec contrôle — ton approche spontanée s'applique aux transformations stratégiques.",
        "Tu abordes les crises et les transformations avec stratégie et contrôle. Tu essaies de gérer même l'ingérable. Les questions d'intimité et de pouvoir sont abordées avec une volonté de maîtrise.",
        "Face aux épreuves, ton instinct est de garder le contrôle et de persévérer. Tu peux avoir du mal à lâcher prise ou à montrer ta vulnérabilité. Mais ta résilience te permet de traverser les crises avec dignité.",
        ["Utilise ta force pour traverser les transformations.", "Permets-toi de perdre le contrôle parfois.", "Journal : « Comment mon besoin de contrôle influence-t-il ma façon de gérer les crises ? »"]
    ),
    ('capricorn', 9): make_asc_interp(
        "Capricorne", 9,
        "Tu te présentes au monde avec sagesse — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances est sérieuse et orientée vers l'application pratique. Tu es attiré par les philosophies qui ont fait leurs preuves au fil du temps. Tu explores le monde pour comprendre ce qui fonctionne.",
        "Tu abordes les études supérieures avec rigueur et les voyages avec un but. Tu préfères les traditions établies aux nouvelles tendances. Tes convictions sont solides et fondées sur l'expérience.",
        ["Explore de nouveaux horizons avec ta sagesse.", "Reste ouvert aux vérités qui défient les traditions.", "Journal : « Comment ma maturité influence-t-elle ma vision du monde ? »"]
    ),
    ('capricorn', 10): make_asc_interp(
        "Capricorne", 10,
        "Tu te présentes au monde comme une autorité — ton approche spontanée excelle dans la carrière.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie capricornienne : ambition, accomplissement, autorité. Tu es né pour réussir et laisser ta marque dans le monde professionnel.",
        "Tu abordes ta carrière comme ta mission de vie. Tu vises le sommet avec patience et détermination. Tu excelles dans les positions de responsabilité et d'autorité.",
        ["Réalise tes ambitions avec intégrité.", "Utilise ton pouvoir pour construire quelque chose de durable.", "Journal : « Comment mon ambition naturelle façonne-t-elle ma vie professionnelle ? »"]
    ),
    ('capricorn', 11): make_asc_interp(
        "Capricorne", 11,
        "Tu te présentes au monde avec sérieux — ton approche spontanée structure les projets collectifs.",
        "Dans les groupes, tu apportes structure et vision à long terme. Tu attires des amis ambitieux ou responsables. Tes idéaux pour l'avenir sont réalistes et tu travailles concrètement pour les atteindre.",
        "Tu abordes l'amitié et les projets de groupe avec ton sens de la responsabilité. Tu es l'ami qui tient ses promesses et qui aide à concrétiser les visions. Tu peux avoir du mal avec les groupes désorganisés.",
        ["Structure les projets collectifs avec ta vision.", "Apporte aussi de la chaleur aux amitiés.", "Journal : « Comment ma maturité enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('capricorn', 12): make_asc_interp(
        "Capricorne", 12,
        "Tu te présentes au monde avec une autorité discrète — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie d'accomplissement opère dans l'ombre. Tu as une vie intérieure très structurée et ambitieuse. Tu travailles secrètement sur tes objectifs de vie. Tu peux porter des responsabilités cachées ou des ambitions secrètes.",
        "Tu abordes la spiritualité et l'inconscient avec méthode. Tu cherches à maîtriser même les dimensions invisibles. Tu peux te saboter par excès de contrôle ou peurs cachées de l'échec.",
        ["Explore ton monde intérieur avec discipline et douceur.", "Libère les peurs cachées de ne pas être à la hauteur.", "Journal : « Quelles ambitions je porte secrètement ? »"]
    ),

    # AQUARIUS ASCENDANT
    ('aquarius', 1): make_asc_interp(
        "Verseau", 1,
        "Tu te présentes au monde avec originalité — ton approche spontanée est celle de l'innovation.",
        "Ton masque est celui du rebelle, de l'être unique et visionnaire. Les gens te perçoivent comme quelqu'un d'original, intellectuel et détaché. Tu dégages une aura d'avant-garde qui intrigue ou déstabilise. Ta présence physique est souvent distinctive, avec un style personnel unique.",
        "Tu abordes la vie en cherchant ce qui est nouveau et différent. Face à une situation, ton instinct est d'innover, de questionner, de libérer. Cette originalité te rend visionnaire mais parfois trop détaché. Tu préfères l'authenticité à la conformité.",
        ["Assume ton originalité sans crainte.", "Connecte-toi aussi émotionnellement avec les autres.", "Journal : « Comment mon besoin d'être unique me guide-t-il dans la vie ? »"]
    ),
    ('aquarius', 2): make_asc_interp(
        "Verseau", 2,
        "Tu te présentes au monde avec indépendance — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie innovante influence ta façon de gagner et de gérer tes ressources. Tu es perçu comme quelqu'un qui a des idées originales sur l'argent. Tu peux être attiré par des revenus non conventionnels ou les nouvelles technologies financières.",
        "Tu abordes les questions d'argent avec originalité et détachement. Tu n'es pas très attaché aux possessions matérielles. Tu préfères investir dans ce qui est innovant ou qui sert l'humanité.",
        ["Innove dans ta façon de créer des ressources.", "Garde un minimum de stabilité financière.", "Journal : « Comment mon originalité influence-t-elle mes finances ? »"]
    ),
    ('aquarius', 3): make_asc_interp(
        "Verseau", 3,
        "Tu te présentes au monde avec intellect — ton approche spontanée s'exprime dans ta communication innovante.",
        "Ta façon de communiquer est originale, intellectuelle et parfois provocatrice. Les gens te perçoivent comme quelqu'un qui pense différemment. Dans ton environnement proche, tu es celui qui apporte des idées nouvelles.",
        "Tu communiques pour faire réfléchir et remettre en question. Ton esprit est brillant et non conventionnel. Tu peux avoir du mal avec les conversations banales ou conventionnelles.",
        ["Partage tes idées innovantes avec le monde.", "Adapte ta communication à ton audience.", "Journal : « Comment mon originalité colore-t-elle ma communication ? »"]
    ),
    ('aquarius', 4): make_asc_interp(
        "Verseau", 4,
        "Tu te présentes au monde avec détachement — ton approche spontanée crée un foyer non conventionnel.",
        "Ton énergie d'innovateur se manifeste dans ta vie privée. Tu as besoin d'un chez-toi qui soit unique, peut-être technologique ou communautaire. Tes racines sont marquées par l'originalité ou l'anticonformisme familial.",
        "Tu abordes ta vie privée avec un besoin de liberté et d'espace personnel. Tu peux avoir une famille non traditionnelle ou des arrangements domestiques originaux. Tu as du mal avec les conventions familiales rigides.",
        ["Crée un foyer qui reflète ton originalité.", "Reste connecté émotionnellement à ta famille.", "Journal : « Comment mon besoin de liberté influence-t-il ma vie familiale ? »"]
    ),
    ('aquarius', 5): make_asc_interp(
        "Verseau", 5,
        "Tu te présentes au monde avec excentricité — ton approche spontanée s'exprime dans la créativité unique.",
        "Ton énergie innovante s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de créatif et original. En amour, tu cherches une connexion intellectuelle et la liberté. Avec les enfants, tu encourages l'individualité.",
        "Tu abordes les loisirs et la romance de façon non conventionnelle. Tu aimes les activités qui stimulent l'intellect. Tu peux avoir du mal avec les démonstrations émotionnelles traditionnelles.",
        ["Exprime ta créativité unique sans retenue.", "Connecte-toi aussi au cœur, pas seulement à l'esprit.", "Journal : « Comment mon originalité enrichit-elle ma créativité et mes amours ? »"]
    ),
    ('aquarius', 6): make_asc_interp(
        "Verseau", 6,
        "Tu te présentes au monde avec efficience — ton approche spontanée s'applique au travail innovant.",
        "Ta façon d'aborder le travail quotidien et la santé est originale et technologique. Tu es perçu comme quelqu'un qui trouve des solutions innovantes. Tu excelles dans les environnements qui valorisent la créativité et l'autonomie.",
        "Tu abordes les routines avec un besoin de les réinventer. Tu aimes utiliser la technologie pour optimiser. Ta santé peut être affectée par le stress mental ou le manque de connexion sociale.",
        ["Innove dans tes méthodes de travail.", "Prends soin de ton système nerveux.", "Journal : « Comment mon originalité influence-t-elle ma santé et mon travail ? »"]
    ),
    ('aquarius', 7): make_asc_interp(
        "Verseau", 7,
        "Tu te présentes au monde avec indépendance — ton approche spontanée recherche des relations libres.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes originales, intellectuelles ou indépendantes. Tu veux un partenaire qui respecte ta liberté et qui te stimule intellectuellement.",
        "Tu abordes les associations avec un besoin d'espace et de liberté. Tu peux avoir des arrangements relationnels non conventionnels. Tu as du mal avec les partenaires possessifs ou trop émotionnels.",
        ["Crée des partenariats basés sur la liberté mutuelle.", "Cultive aussi l'intimité émotionnelle.", "Journal : « Comment mon besoin de liberté influence-t-il mes partenariats ? »"]
    ),
    ('aquarius', 8): make_asc_interp(
        "Verseau", 8,
        "Tu te présentes au monde avec détachement — ton approche spontanée s'applique aux transformations rationnelles.",
        "Tu abordes les crises et les transformations avec une certaine distance intellectuelle. Tu essaies de comprendre rationnellement ce qui se passe. Les questions d'intimité sont abordées avec un besoin de liberté.",
        "Face aux épreuves, ton instinct est d'analyser et de rester détaché. Tu peux avoir du mal avec les émotions intenses des transformations. Mais ta perspective unique te permet de voir des solutions que d'autres ne voient pas.",
        ["Utilise ton intellect pour naviguer les transformations.", "Permets-toi de ressentir profondément.", "Journal : « Comment mon détachement influence-t-il ma façon de gérer les crises ? »"]
    ),
    ('aquarius', 9): make_asc_interp(
        "Verseau", 9,
        "Tu te présentes au monde avec vision — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances est avant-gardiste et universelle. Tu es attiré par les philosophies progressistes et les idées nouvelles. Tu explores le monde en cherchant ce qui fait avancer l'humanité.",
        "Tu abordes les études supérieures avec originalité et les voyages avec curiosité pour les différentes cultures. Tu préfères les vérités universelles aux dogmes particuliers. Tes convictions sont souvent humanitaires.",
        ["Explore de nouveaux horizons de pensée.", "Reste ouvert aux sagesses traditionnelles aussi.", "Journal : « Comment ma vision progressiste influence-t-elle ma vision du monde ? »"]
    ),
    ('aquarius', 10): make_asc_interp(
        "Verseau", 10,
        "Tu te présentes au monde comme un innovateur — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un d'original, visionnaire et humanitaire. Ta réputation est celle d'un pionnier ou d'un rebelle. Tu excelles dans les rôles qui impliquent innovation, technologie ou changement social.",
        "Tu abordes ta carrière avec un besoin d'être différent et de contribuer au progrès. Tu as du mal avec les environnements conservateurs ou hiérarchiques rigides.",
        ["Utilise ton originalité pour innover dans ta carrière.", "Construis une réputation de visionnaire.", "Journal : « Comment mon originalité façonne-t-elle ma vie professionnelle ? »"]
    ),
    ('aquarius', 11): make_asc_interp(
        "Verseau", 11,
        "Tu te présentes au monde avec humanisme — ton approche spontanée excelle dans les projets collectifs.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie verseau : communauté, innovation, humanitarisme. Tu es né pour les causes collectives et l'amitié. Tu attires des amis aussi uniques que toi.",
        "Tu abordes l'amitié et les projets de groupe comme ton élément naturel. Tu excelles à connecter des personnes différentes pour une cause commune. Tes idéaux sont progressistes et inclusifs.",
        ["Rassemble les gens autour de visions progressistes.", "Valorise aussi les amitiés individuelles profondes.", "Journal : « Comment ma nature humanitaire s'exprime-t-elle pleinement ? »"]
    ),
    ('aquarius', 12): make_asc_interp(
        "Verseau", 12,
        "Tu te présentes au monde avec une originalité cachée — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie innovante opère dans l'ombre. Tu as une vie intérieure très riche en idées et en visions. Tu peux avoir des intuitions sur l'avenir ou des connexions avec le collectif inconscient.",
        "Tu abordes la spiritualité et l'inconscient de façon originale. Tu peux avoir des expériences mystiques ou des perceptions inhabituelles. Tu peux te saboter par trop de détachement ou de fuite dans l'abstraction.",
        ["Explore les dimensions invisibles avec ton intellect.", "Ancre tes visions dans la réalité.", "Journal : « Quelles visions je porte secrètement pour l'humanité ? »"]
    ),

    # PISCES ASCENDANT
    ('pisces', 1): make_asc_interp(
        "Poissons", 1,
        "Tu te présentes au monde avec douceur — ton approche spontanée est celle de la compassion.",
        "Ton masque est celui du mystique, de l'être sensible et empathique. Les gens te perçoivent comme quelqu'un de doux, rêveur et compatissant. Tu dégages une aura de mystère qui attire ceux qui cherchent la compréhension. Ta présence physique est souvent éthérée, avec un regard qui semble voir au-delà.",
        "Tu abordes la vie par l'intuition et l'empathie. Face à une situation, ton instinct est de ressentir, d'absorber, de compatir. Cette sensibilité te rend profondément connecté mais parfois sans limites claires. Tu préfères l'harmonie au conflit.",
        ["Honore ta sensibilité comme un don.", "Protège-toi en établissant des limites claires.", "Journal : « Comment ma compassion me guide-t-elle dans la vie ? »"]
    ),
    ('pisces', 2): make_asc_interp(
        "Poissons", 2,
        "Tu te présentes au monde avec détachement — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie intuitive influence ta façon de gérer tes ressources. Tu es perçu comme quelqu'un de généreux, peut-être trop. Tu peux avoir du mal avec les aspects pratiques de l'argent, préférant donner ou partager.",
        "Tu abordes les questions d'argent avec un certain flou. Tu peux oublier les détails financiers ou être naïf dans les affaires. Tu dépenses facilement pour l'art, la spiritualité ou pour aider les autres.",
        ["Développe un rapport sain et ancré à l'argent.", "Protège tes ressources tout en restant généreux.", "Journal : « Comment ma nature spirituelle influence-t-elle mes finances ? »"]
    ),
    ('pisces', 3): make_asc_interp(
        "Poissons", 3,
        "Tu te présentes au monde avec sensibilité — ton approche spontanée s'exprime dans ta communication intuitive.",
        "Ta façon de communiquer est douce, imaginative et parfois vague. Les gens te perçoivent comme quelqu'un de poétique et d'empathique. Dans ton environnement proche, tu es celui qui comprend sans mots.",
        "Tu communiques autant par l'énergie que par les mots. Tu captes les ambiances et les non-dits. Tu peux avoir du mal à être direct ou précis, préférant les nuances et les suggestions.",
        ["Communique avec ta sensibilité poétique.", "Sois plus direct quand c'est nécessaire.", "Journal : « Comment mon intuition colore-t-elle ma communication ? »"]
    ),
    ('pisces', 4): make_asc_interp(
        "Poissons", 4,
        "Tu te présentes au monde avec douceur — ton approche spontanée crée un foyer sanctuaire.",
        "Ton énergie sensible se manifeste dans ta vie privée. Tu as besoin d'un chez-toi qui soit un sanctuaire, un refuge du monde. Tes racines sont marquées par la spiritualité, la créativité ou des secrets familiaux.",
        "Tu abordes ta vie privée comme un espace sacré. Tu as besoin de beauté et de paix dans ton environnement. Tu peux avoir des frontières floues avec ta famille ou absorber leurs émotions.",
        ["Crée un foyer qui nourrit ton âme.", "Protège ton espace intérieur.", "Journal : « Comment ma sensibilité façonne-t-elle ma vie familiale ? »"]
    ),
    ('pisces', 5): make_asc_interp(
        "Poissons", 5,
        "Tu te présentes au monde avec romantisme — ton approche spontanée s'exprime dans la créativité inspirée.",
        "Ton énergie imaginative s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de romantique et d'artistique. En amour, tu idéalises et tu te dévoues. Avec les enfants, tu nourris l'imagination et la compassion.",
        "Tu abordes les loisirs et la romance comme des expériences transcendantes. Tu crées pour exprimer l'inexprimable. Tu peux idéaliser l'amour au point d'être déçu par la réalité.",
        ["Exprime ta créativité sans limites.", "Garde les pieds sur terre dans tes amours.", "Journal : « Comment mon imagination enrichit-elle ma créativité et mes amours ? »"]
    ),
    ('pisces', 6): make_asc_interp(
        "Poissons", 6,
        "Tu te présentes au monde avec service — ton approche spontanée s'applique au soin des autres.",
        "Ta façon d'aborder le travail quotidien et la santé est intuitive et compatissante. Tu es perçu comme quelqu'un qui aide naturellement. Tu excelles dans les environnements où tu peux servir et guérir.",
        "Tu abordes les routines avec un besoin de sens spirituel. Ta santé est sensible aux énergies environnantes — tu absorbes facilement les stress des autres. Tu as besoin de temps seul pour te régénérer.",
        ["Sers avec compassion tout en te protégeant.", "Prends soin de ta santé énergétique.", "Journal : « Comment ma sensibilité influence-t-elle ma santé et mon travail ? »"]
    ),
    ('pisces', 7): make_asc_interp(
        "Poissons", 7,
        "Tu te présentes au monde avec empathie — ton approche spontanée recherche des relations fusionnelles.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes spirituelles, artistiques ou qui ont besoin d'aide. Tu es un partenaire dévoué qui peut se sacrifier pour l'autre. Tu cherches l'union des âmes.",
        "Tu abordes les associations avec ton cœur grand ouvert. Tu peux avoir du mal avec les limites dans les relations, te perdant dans l'autre. Tu idéalises peut-être tes partenaires.",
        ["Crée des partenariats basés sur la connexion profonde.", "Garde ton identité intacte dans les relations.", "Journal : « Comment ma compassion influence-t-elle mes partenariats ? »"]
    ),
    ('pisces', 8): make_asc_interp(
        "Poissons", 8,
        "Tu te présentes au monde avec profondeur — ton approche spontanée s'applique aux transformations spirituelles.",
        "Tu abordes les crises et les transformations avec une compréhension intuitive. Tu ressens ce qui se passe au-delà des apparences. Les questions d'intimité et de transformation sont abordées comme des expériences spirituelles.",
        "Face aux épreuves, ton instinct est de t'abandonner et de faire confiance au processus. Tu peux avoir des capacités psychiques ou une connexion profonde avec l'invisible. Tu comprends naturellement les mystères de la vie et de la mort.",
        ["Utilise ton intuition pour naviguer les transformations.", "Reste ancré pendant les traversées.", "Journal : « Comment ma spiritualité m'aide-t-elle à traverser les crises ? »"]
    ),
    ('pisces', 9): make_asc_interp(
        "Poissons", 9,
        "Tu te présentes au monde avec sagesse mystique — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances est spirituelle et mystique. Tu es attiré par les traditions ésotériques et les vérités qui transcendent la logique. Tu explores le monde en cherchant l'unité derrière la diversité.",
        "Tu abordes les études supérieures par l'intuition et les voyages comme des pèlerinages. Tu préfères l'expérience directe du divin aux doctrines intellectuelles. Tes convictions sont fluides et ouvertes.",
        ["Explore les dimensions spirituelles de l'existence.", "Ancre ta spiritualité dans la réalité quotidienne.", "Journal : « Comment ma quête mystique influence-t-elle ma vision du monde ? »"]
    ),
    ('pisces', 10): make_asc_interp(
        "Poissons", 10,
        "Tu te présentes au monde comme un guérisseur — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un de compatissant, artistique ou spirituel. Ta réputation est celle d'un guérisseur ou d'un artiste. Tu excelles dans les rôles qui impliquent aider, guérir ou créer de la beauté.",
        "Tu abordes ta carrière avec un besoin de servir quelque chose de plus grand. Tu peux avoir du mal avec les environnements professionnels compétitifs ou matérialistes.",
        ["Utilise tes dons au service des autres.", "Construis une réputation de compassion et d'inspiration.", "Journal : « Comment ma spiritualité façonne-t-elle ma vie professionnelle ? »"]
    ),
    ('pisces', 11): make_asc_interp(
        "Poissons", 11,
        "Tu te présentes au monde avec compassion universelle — ton approche spontanée anime tes projets collectifs.",
        "Dans les groupes, tu apportes empathie et vision spirituelle. Tu attires des amis qui partagent tes idéaux ou qui ont besoin de ta compassion. Tes idéaux pour l'avenir sont utopiques et inclusifs.",
        "Tu abordes l'amitié et les projets de groupe avec ton cœur. Tu es l'ami qui comprend et qui pardonne. Tu peux avoir du mal avec les limites dans les amitiés ou te sacrifier pour le groupe.",
        ["Porte ta compassion au service du collectif.", "Protège-toi tout en servant.", "Journal : « Comment ma compassion enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('pisces', 12): make_asc_interp(
        "Poissons", 12,
        "Tu te présentes au monde avec une spiritualité profonde — ton approche spontanée habite ton monde intérieur.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie poissons : spiritualité, mystère, compassion. Tu es né pour explorer les dimensions invisibles. Tu as une connexion naturelle avec le divin.",
        "Tu abordes la spiritualité et l'inconscient comme ton domaine naturel. Tu as probablement des capacités psychiques ou une intuition très développée. Tu comprends les mystères que d'autres ne perçoivent pas.",
        ["Explore les profondeurs de ton être.", "Utilise tes dons spirituels pour aider.", "Journal : « Comment ma connexion au divin s'exprime-t-elle pleinement ? »"]
    ),
}


async def insert_interpretations():
    """Insert Ascendant interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in ASCENDANT_INTERPRETATIONS.items():
            # Check if already exists
            query = select(PregeneratedNatalInterpretation).where(
                PregeneratedNatalInterpretation.subject == "ascendant",
                PregeneratedNatalInterpretation.sign == sign,
                PregeneratedNatalInterpretation.house == house,
                PregeneratedNatalInterpretation.version == 2,
                PregeneratedNatalInterpretation.lang == "fr"
            )
            result = await db.execute(query)
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️ SKIP ascendant/{sign}/M{house} (already exists)")
                skipped += 1
                continue

            # Insert new interpretation
            interpretation = PregeneratedNatalInterpretation(
                id=uuid4(),
                subject="ascendant",
                sign=sign,
                house=house,
                version=2,
                lang="fr",
                content=content,
                length=len(content)
            )
            db.add(interpretation)
            print(f"✅ INSERT ascendant/{sign}/M{house} ({len(content)} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == "__main__":
    asyncio.run(insert_interpretations())
