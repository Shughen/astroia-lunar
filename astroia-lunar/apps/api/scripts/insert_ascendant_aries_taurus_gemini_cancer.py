#!/usr/bin/env python3
"""
Insert Ascendant interpretations for Aries, Taurus, Gemini, Cancer (48 entries)
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


# Ascendant in Aries (Houses 1-12)
ASCENDANT_INTERPRETATIONS = {
    # ARIES ASCENDANT
    ('aries', 1): make_asc_interp(
        "Bélier", 1,
        "Tu te présentes au monde comme un pionnier audacieux — ton approche spontanée est celle de l'action directe.",
        "Ton masque est celui du guerrier, du premier à agir. Les gens te perçoivent comme quelqu'un d'énergique, direct et courageux. Tu dégages une aura d'indépendance et de confiance en toi qui peut intimider ou inspirer. Ta présence physique est souvent dynamique, avec des gestes rapides et décidés.",
        "Tu abordes la vie frontalement, sans détour. Face à un obstacle, ton instinct est de foncer. Cette spontanéité te rend authentique mais parfois impulsif. Tu préfères l'action à la réflexion prolongée, ce qui te permet de saisir les opportunités avant les autres.",
        ["Canalise ton énergie de pionnier avec intention.", "Respire avant de réagir pour tempérer l'impulsivité.", "Journal : « Comment mon besoin d'action immédiate me sert-il ou me dessert-il ? »"]
    ),
    ('aries', 2): make_asc_interp(
        "Bélier", 2,
        "Tu te présentes au monde avec fougue — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie de pionnier influence ta façon de gagner et de dépenser. Tu es perçu comme quelqu'un qui sait ce qu'il veut matériellement et qui n'hésite pas à aller le chercher. Ta présence énergique se manifeste dans ta détermination à construire ta sécurité financière de façon indépendante.",
        "Tu abordes les questions d'argent et de valeurs avec la même fougue que tout le reste. Tes décisions financières sont rapides, parfois impulsives. Tu préfères créer tes propres ressources plutôt que de dépendre des autres.",
        ["Utilise ton audace pour entreprendre financièrement.", "Tempère l'impulsivité dans les achats.", "Journal : « Comment mon énergie de pionnier influence-t-elle mes finances ? »"]
    ),
    ('aries', 3): make_asc_interp(
        "Bélier", 3,
        "Tu te présentes au monde avec dynamisme — ton approche spontanée s'exprime dans ta communication.",
        "Ta façon de communiquer est directe, parfois tranchante. Les gens te perçoivent comme quelqu'un qui dit ce qu'il pense sans filtre. Dans ton environnement proche, tu es celui qui initie les conversations et les projets. Tes échanges avec frères et sœurs peuvent être compétitifs.",
        "Tu apprends vite et tu t'ennuies facilement. Ton esprit va droit au but, préférant les informations pratiques aux théories complexes. Tu as tendance à interrompre ou à finir les phrases des autres par impatience.",
        ["Canalise ton énergie dans une communication assertive mais respectueuse.", "Cultive la patience dans les échanges.", "Journal : « Comment ma façon directe de communiquer affecte-t-elle mes relations proches ? »"]
    ),
    ('aries', 4): make_asc_interp(
        "Bélier", 4,
        "Tu te présentes au monde avec vigueur — ton approche spontanée touche ta sphère familiale.",
        "Ton énergie de leader se manifeste dans ta vie privée et familiale. Tu as besoin d'être le chef de ta maison, celui qui décide. Tes racines sont marquées par une énergie combative — peut-être un parent fort ou des conflits familiaux formateurs.",
        "Tu abordes ta vie privée avec la même intensité que le reste. Tu as besoin d'un chez-toi qui te permette d'être actif, pas un endroit pour te reposer passivement. Tu peux avoir tendance à créer du mouvement même là où le calme serait bienvenu.",
        ["Crée un espace qui canalise ton énergie.", "Trouve l'équilibre entre leadership et écoute à la maison.", "Journal : « Comment mon besoin d'action influence-t-il ma vie familiale ? »"]
    ),
    ('aries', 5): make_asc_interp(
        "Bélier", 5,
        "Tu te présentes au monde avec enthousiasme — ton approche spontanée brille dans ta créativité.",
        "Ton énergie de pionnier s'exprime pleinement dans tes créations et tes passions. Tu es perçu comme quelqu'un de passionné, entier dans ses plaisirs. En amour, tu fais le premier pas sans hésitation. Avec les enfants, tu es le parent qui joue et qui challenge.",
        "Tu abordes les loisirs et la romance avec intensité. Tu préfères les activités qui font monter l'adrénaline aux passe-temps tranquilles. Tes passions sont vives mais peuvent s'éteindre aussi vite qu'elles s'allument.",
        ["Canalise ta passion créative dans des projets durables.", "Savoure le processus créatif, pas seulement le résultat.", "Journal : « Comment ma fougue influence-t-elle mes passions et mes amours ? »"]
    ),
    ('aries', 6): make_asc_interp(
        "Bélier", 6,
        "Tu te présentes au monde avec énergie — ton approche spontanée s'applique à ton quotidien.",
        "Ta façon d'aborder le travail quotidien et la santé est directe et énergique. Tu es perçu comme un travailleur efficace qui va droit au but. Tu préfères les tâches qui demandent de l'action à celles qui requièrent de la patience. Ta santé dépend de ton niveau d'activité physique.",
        "Tu abordes les routines avec impatience — tu veux des résultats rapides. Tu excelles dans les situations d'urgence mais tu peux négliger les soins préventifs qui demandent de la constance. Ton corps a besoin de bouger régulièrement.",
        ["Intègre l'exercice physique dans ta routine quotidienne.", "Cultive la patience dans les tâches répétitives.", "Journal : « Comment mon énergie de pionnier influence-t-elle ma santé et mon travail ? »"]
    ),
    ('aries', 7): make_asc_interp(
        "Bélier", 7,
        "Tu te présentes au monde avec assurance — ton approche spontanée teinte tes relations.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes qui complètent ton énergie — soit aussi combatives, soit plus pacifiques pour t'équilibrer. Tu peux avoir tendance à dominer dans les relations ou à créer des conflits stimulants.",
        "Tu abordes les associations avec franchise. Tu dis ce que tu penses à ton partenaire, même si ça crée des frictions. Tu as besoin d'un partenaire qui peut tenir tête à ton énergie sans se laisser écraser.",
        ["Apprends à écouter avant de réagir dans les relations.", "Transforme la compétition en collaboration.", "Journal : « Comment ma nature directe influence-t-elle mes partenariats ? »"]
    ),
    ('aries', 8): make_asc_interp(
        "Bélier", 8,
        "Tu te présentes au monde avec intensité — ton approche spontanée s'applique aux transformations profondes.",
        "Tu abordes les crises et les transformations avec courage. Là où d'autres hésitent face à l'inconnu, tu fonces. Les questions d'intimité, d'argent partagé et de mort sont abordées frontalement. Tu as une capacité à renaître rapidement de tes cendres.",
        "Face aux épreuves, ton instinct est de combattre plutôt que de fuir. Tu peux être impulsif dans les situations qui demandent de la prudence — investissements risqués, engagements intimes précipités. Mais cette audace te permet aussi des transformations rapides.",
        ["Canalise ton courage dans les moments de crise.", "Tempère l'impulsivité dans les décisions financières partagées.", "Journal : « Comment j'aborde les transformations majeures de ma vie ? »"]
    ),
    ('aries', 9): make_asc_interp(
        "Bélier", 9,
        "Tu te présentes au monde avec audace — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances et d'aventure est pionnière. Tu es celui qui part explorer de nouveaux territoires — géographiques ou intellectuels — en premier. Tu défends tes croyances avec passion, parfois au point de devenir dogmatique.",
        "Tu abordes les études supérieures et les voyages avec enthousiasme. Tu préfères apprendre par l'expérience directe que par les livres. Tes convictions philosophiques sont fortes et tu n'hésites pas à les défendre.",
        ["Explore de nouveaux horizons avec discernement.", "Reste ouvert aux perspectives différentes des tiennes.", "Journal : « Comment ma fougue influence-t-elle ma vision du monde ? »"]
    ),
    ('aries', 10): make_asc_interp(
        "Bélier", 10,
        "Tu te présentes au monde comme un leader — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un d'ambitieux, direct et prêt à prendre les rênes. Ta réputation est celle d'un pionnier dans ton domaine. Tu excelles dans les rôles qui demandent de l'initiative et du courage. Tu préfères être ton propre patron.",
        "Tu abordes ta carrière avec la même fougue que tout — tu veux monter vite et tu n'as pas peur de prendre des risques professionnels. Tu peux avoir du mal avec l'autorité si elle freine ton élan.",
        ["Utilise ton leadership naturel avec sagesse.", "Construis une réputation d'audace et d'intégrité.", "Journal : « Comment mon énergie de pionnier façonne-t-elle ma vie professionnelle ? »"]
    ),
    ('aries', 11): make_asc_interp(
        "Bélier", 11,
        "Tu te présentes au monde avec dynamisme — ton approche spontanée anime tes projets collectifs.",
        "Dans les groupes, tu prends naturellement la tête. Tu attires des amis aussi dynamiques que toi ou qui admirent ton énergie. Tes idéaux pour l'avenir sont audacieux et tu n'hésites pas à te battre pour des causes progressistes.",
        "Tu abordes l'amitié et les projets de groupe avec enthousiasme. Tu es celui qui initie les rassemblements et qui pousse le groupe à l'action. Tu peux avoir du mal avec les processus démocratiques lents.",
        ["Canalise ton énergie au service du collectif.", "Apprends à collaborer sans dominer.", "Journal : « Comment mon leadership influence-t-il mes amitiés et mes causes ? »"]
    ),
    ('aries', 12): make_asc_interp(
        "Bélier", 12,
        "Tu te présentes au monde avec une énergie cachée — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie de guerrier opère dans l'ombre. Tu peux paraître plus doux que tu ne l'es vraiment, gardant ta combativité pour toi-même ou pour des batailles intérieures. Tu as un courage discret qui se révèle dans les moments de solitude ou de crise.",
        "Tu abordes la spiritualité et l'inconscient avec la même fougue que le reste — tu veux des résultats, même dans le domaine mystique. Tu peux avoir des ennemis cachés ou te saboter par impatience avec toi-même.",
        ["Explore ton monde intérieur avec courage et patience.", "Transforme la colère cachée en force spirituelle.", "Journal : « Comment mon énergie de pionnier s'exprime-t-elle dans ma vie intérieure ? »"]
    ),

    # TAURUS ASCENDANT
    ('taurus', 1): make_asc_interp(
        "Taureau", 1,
        "Tu te présentes au monde avec stabilité — ton approche spontanée est celle de la persévérance.",
        "Ton masque est celui du roc, de la présence solide et rassurante. Les gens te perçoivent comme quelqu'un de calme, fiable et ancré. Tu dégages une aura de sérénité qui met les autres en confiance. Ta présence physique est souvent imposante ou sensuelle, avec une démarche posée.",
        "Tu abordes la vie avec patience et détermination. Face à un obstacle, ton instinct est de persévérer plutôt que de forcer. Cette constance te rend fiable mais parfois têtu. Tu préfères la stabilité à l'aventure, ce qui te protège des risques inconsidérés.",
        ["Ancre-toi dans ta force tranquille.", "Sois ouvert au changement quand il est nécessaire.", "Journal : « Comment ma stabilité naturelle me sert-elle ou me limite-t-elle ? »"]
    ),
    ('taurus', 2): make_asc_interp(
        "Taureau", 2,
        "Tu te présentes au monde avec solidité — ton approche spontanée s'aligne parfaitement avec les ressources.",
        "Ici, ton masque et ta maison sont en harmonie. Tu incarnes naturellement les valeurs taurines de sécurité matérielle et de plaisirs sensoriels. Les gens te voient comme quelqu'un qui sait jouir de la vie et construire sa prospérité avec patience.",
        "Tu abordes les questions d'argent avec le même calme que tout le reste. Tes finances se construisent lentement mais sûrement. Tu apprécies la qualité plutôt que la quantité et tu investis dans ce qui dure.",
        ["Construis ta sécurité avec patience et sagesse.", "Partage ton sens de l'abondance.", "Journal : « Comment mon rapport naturel aux plaisirs et aux ressources s'exprime-t-il ? »"]
    ),
    ('taurus', 3): make_asc_interp(
        "Taureau", 3,
        "Tu te présentes au monde avec calme — ton approche spontanée s'exprime dans ta communication posée.",
        "Ta façon de communiquer est réfléchie, mesurée. Les gens te perçoivent comme quelqu'un qui pèse ses mots. Dans ton environnement proche, tu apportes stabilité et sens pratique. Tes échanges avec frères et sœurs sont généralement paisibles mais peuvent devenir têtus.",
        "Tu apprends à ton rythme et tu retiens ce que tu apprends. Ton esprit est concret, préférant les applications pratiques aux théories abstraites. Tu as besoin de temps pour assimiler les informations avant de répondre.",
        ["Communique avec ta sagesse tranquille.", "Sois patient avec ceux qui pensent plus vite.", "Journal : « Comment ma façon posée de communiquer enrichit-elle mes échanges ? »"]
    ),
    ('taurus', 4): make_asc_interp(
        "Taureau", 4,
        "Tu te présentes au monde avec assurance — ton approche spontanée crée un foyer stable.",
        "Ton besoin de sécurité se manifeste pleinement dans ta vie privée et familiale. Tu as besoin d'un chez-toi confortable, beau et stable. Tes racines sont marquées par une recherche de stabilité — peut-être un environnement familial prospère ou, au contraire, un manque qui t'a motivé.",
        "Tu abordes ta vie privée comme un sanctuaire à construire patiemment. Tu investis dans ton intérieur et tu crées un environnement qui nourrit les sens. La famille représente une ancre importante pour toi.",
        ["Crée un foyer qui nourrit tous tes sens.", "Partage ta stabilité avec tes proches.", "Journal : « Comment mon besoin de sécurité façonne-t-il ma vie familiale ? »"]
    ),
    ('taurus', 5): make_asc_interp(
        "Taureau", 5,
        "Tu te présentes au monde avec sensualité — ton approche spontanée s'épanouit dans les plaisirs.",
        "Ton énergie stable s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un qui sait apprécier les plaisirs de la vie. En amour, tu es patient, romantique et fidèle. Avec les enfants, tu offres sécurité et tendresse.",
        "Tu abordes les loisirs et la romance avec constance. Tu préfères les plaisirs durables aux excitations passagères. Tes passions prennent du temps à s'allumer mais elles durent longtemps.",
        ["Savoure les plaisirs de la vie avec présence.", "Exprime ta créativité à travers les sens.", "Journal : « Comment ma nature sensuelle enrichit-elle ma vie amoureuse et créative ? »"]
    ),
    ('taurus', 6): make_asc_interp(
        "Taureau", 6,
        "Tu te présentes au monde avec fiabilité — ton approche spontanée s'applique au travail constant.",
        "Ta façon d'aborder le travail quotidien et la santé est méthodique et persévérante. Tu es perçu comme un travailleur fiable qui accomplit ses tâches avec soin. Tu excelles dans les travaux qui demandent patience et constance.",
        "Tu abordes les routines avec un certain plaisir — tu aimes les habitudes bien établies. Ta santé dépend de la qualité de tes plaisirs : bonne nourriture, repos suffisant, activité physique régulière mais modérée.",
        ["Construis des routines qui nourrissent ton corps.", "Travaille avec patience et constance.", "Journal : « Comment ma fiabilité naturelle influence-t-elle ma santé et mon travail ? »"]
    ),
    ('taurus', 7): make_asc_interp(
        "Taureau", 7,
        "Tu te présentes au monde avec stabilité — ton approche spontanée recherche des relations durables.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes qui partagent tes valeurs de stabilité — ou qui t'apportent la stimulation qui te manque. Tu es un partenaire fidèle et constant qui construit sur la durée.",
        "Tu abordes les associations avec patience. Tu prends ton temps avant de t'engager mais une fois engagé, tu es loyal. Tu peux avoir du mal à quitter des relations qui ne fonctionnent plus par attachement à la stabilité.",
        ["Construis des partenariats sur des bases solides.", "Reste ouvert à l'évolution dans tes relations.", "Journal : « Comment ma nature constante influence-t-elle mes partenariats ? »"]
    ),
    ('taurus', 8): make_asc_interp(
        "Taureau", 8,
        "Tu te présentes au monde avec ancrage — ton approche spontanée s'applique aux transformations profondes.",
        "Tu abordes les crises et les transformations avec calme et résilience. Là où d'autres paniquent, tu restes ancré. Les questions d'intimité, d'argent partagé et de transformation sont abordées avec prudence et sens pratique.",
        "Face aux épreuves, ton instinct est de t'ancrer et de persévérer. Tu peux résister trop longtemps au changement nécessaire par attachement à ce qui est familier. Mais ta stabilité te permet de traverser les crises sans t'effondrer.",
        ["Utilise ton ancrage pour traverser les transformations.", "Accepte le changement quand il est inévitable.", "Journal : « Comment mon besoin de stabilité influence-t-il ma façon de gérer les crises ? »"]
    ),
    ('taurus', 9): make_asc_interp(
        "Taureau", 9,
        "Tu te présentes au monde avec pragmatisme — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances et d'aventure est tempérée par ton sens pratique. Tu préfères les philosophies terre-à-terre aux abstractions. Tu explores le monde à ton rythme, préférant approfondir que survoler.",
        "Tu abordes les études supérieures et les voyages avec méthode. Tu préfères apprendre ce qui a une application concrète. Tes convictions philosophiques sont stables et tu n'aimes pas qu'on les remette en question.",
        ["Explore de nouveaux horizons à ton rythme.", "Reste ouvert aux idées qui défient tes certitudes.", "Journal : « Comment mon pragmatisme influence-t-il ma vision du monde ? »"]
    ),
    ('taurus', 10): make_asc_interp(
        "Taureau", 10,
        "Tu te présentes au monde avec solidité — ton approche spontanée façonne une carrière stable.",
        "Tu es perçu publiquement comme quelqu'un de fiable, patient et compétent. Ta réputation est celle de quelqu'un qui construit sur la durée. Tu excelles dans les domaines qui demandent persévérance et sens pratique.",
        "Tu abordes ta carrière comme une construction progressive. Tu vises la sécurité plutôt que la gloire éphémère. Tu peux avoir du mal avec les environnements professionnels instables ou trop compétitifs.",
        ["Construis ta carrière pierre par pierre.", "Valorise ta fiabilité comme un atout professionnel.", "Journal : « Comment ma stabilité naturelle façonne-t-elle ma vie professionnelle ? »"]
    ),
    ('taurus', 11): make_asc_interp(
        "Taureau", 11,
        "Tu te présentes au monde avec constance — ton approche spontanée s'applique aux projets collectifs.",
        "Dans les groupes, tu apportes stabilité et sens pratique. Tu attires des amis fidèles qui partagent tes valeurs. Tes idéaux pour l'avenir sont réalistes et tu travailles patiemment vers des améliorations concrètes.",
        "Tu abordes l'amitié et les projets de groupe avec loyauté. Tu es l'ami sur qui on peut compter dans la durée. Tu peux avoir du mal avec les groupes trop changeants ou les causes trop radicales.",
        ["Apporte ta stabilité aux projets collectifs.", "Construis des amitiés durables basées sur des valeurs partagées.", "Journal : « Comment ma constance enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('taurus', 12): make_asc_interp(
        "Taureau", 12,
        "Tu te présentes au monde avec une force tranquille cachée — ton approche spontanée habite ton monde intérieur.",
        "Ta stabilité opère dans l'ombre. Tu peux paraître moins ancré que tu ne l'es vraiment, gardant ta force tranquille pour ta vie intérieure. Tu as une résilience secrète qui se révèle dans les moments de solitude ou de méditation.",
        "Tu abordes la spiritualité et l'inconscient avec patience. Tu préfères les pratiques spirituelles qui ancrent plutôt que celles qui déstabilisent. Tu peux avoir des attachements cachés ou te saboter par résistance au changement.",
        ["Explore ton monde intérieur avec patience.", "Transforme l'attachement caché en ancrage spirituel.", "Journal : « Comment ma stabilité s'exprime-t-elle dans ma vie intérieure ? »"]
    ),

    # GEMINI ASCENDANT
    ('gemini', 1): make_asc_interp(
        "Gémeaux", 1,
        "Tu te présentes au monde avec curiosité — ton approche spontanée est celle de la communication.",
        "Ton masque est celui du communicateur, de l'esprit vif. Les gens te perçoivent comme quelqu'un d'intelligent, adaptable et sociable. Tu dégages une aura de jeunesse et de vivacité qui attire les échanges. Ta présence physique est souvent légère, avec des gestes expressifs.",
        "Tu abordes la vie par la pensée et la parole. Face à une situation, ton instinct est d'analyser, de questionner, de communiquer. Cette agilité mentale te rend polyvalent mais parfois dispersé. Tu préfères la variété à la profondeur.",
        ["Canalise ta curiosité avec intention.", "Approfondis certains sujets plutôt que de tout survoler.", "Journal : « Comment ma vivacité mentale me sert-elle ou me disperse-t-elle ? »"]
    ),
    ('gemini', 2): make_asc_interp(
        "Gémeaux", 2,
        "Tu te présentes au monde avec légèreté — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie de communicateur influence ta façon de gagner et de dépenser. Tu es perçu comme quelqu'un de malin avec l'argent, capable de jongler avec plusieurs sources de revenus. Tu préfères la flexibilité financière à la sécurité rigide.",
        "Tu abordes les questions d'argent avec curiosité et adaptabilité. Tes finances peuvent fluctuer au gré de tes intérêts multiples. Tu dépenses facilement pour la communication, les voyages courts et les nouvelles expériences.",
        ["Utilise ton intelligence pour diversifier tes revenus.", "Évite l'éparpillement financier.", "Journal : « Comment ma nature adaptable influence-t-elle mes finances ? »"]
    ),
    ('gemini', 3): make_asc_interp(
        "Gémeaux", 3,
        "Tu te présentes au monde avec vivacité — ton approche spontanée s'exprime pleinement dans la communication.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement l'énergie gémellienne de l'échange et de la curiosité. Ta façon de communiquer est brillante, rapide, et tu excelles dans tout ce qui touche aux mots et aux idées.",
        "Tu apprends vite et tu t'intéresses à tout. Ton esprit est agile, capable de passer d'un sujet à l'autre avec aisance. Tes relations avec l'environnement proche sont stimulantes intellectuellement.",
        ["Développe tes dons de communication.", "Partage ta curiosité avec ton entourage.", "Journal : « Comment ma vivacité intellectuelle enrichit-elle mes échanges ? »"]
    ),
    ('gemini', 4): make_asc_interp(
        "Gémeaux", 4,
        "Tu te présentes au monde avec curiosité — ton approche spontanée anime ta vie familiale.",
        "Ton énergie de communicateur se manifeste dans ta vie privée. Tu as besoin d'un foyer stimulant intellectuellement, où les discussions sont animées. Tes racines sont marquées par une éducation qui valorisait la communication ou les déménagements fréquents.",
        "Tu abordes ta vie privée avec légèreté. Tu peux avoir du mal avec le côté émotionnel de la famille, préférant intellectualiser. Ton chez-toi a souvent beaucoup de livres et de moyens de communication.",
        ["Crée un foyer qui stimule ton esprit.", "Connecte-toi émotionnellement avec ta famille, pas seulement intellectuellement.", "Journal : « Comment ma curiosité influence-t-elle ma vie familiale ? »"]
    ),
    ('gemini', 5): make_asc_interp(
        "Gémeaux", 5,
        "Tu te présentes au monde avec esprit — ton approche spontanée s'exprime dans ta créativité.",
        "Ton énergie de communicateur s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de spirituel et divertissant. En amour, tu séduis par l'esprit et les mots. Avec les enfants, tu es le parent qui joue avec les idées et stimule l'intelligence.",
        "Tu abordes les loisirs et la romance avec curiosité. Tu préfères les activités qui stimulent l'esprit aux plaisirs purement physiques. Tes passions sont nombreuses et changeantes.",
        ["Exprime ta créativité à travers les mots et les idées.", "Reste engagé assez longtemps pour approfondir.", "Journal : « Comment ma vivacité influence-t-elle ma vie amoureuse et créative ? »"]
    ),
    ('gemini', 6): make_asc_interp(
        "Gémeaux", 6,
        "Tu te présentes au monde avec adaptabilité — ton approche spontanée s'applique au travail varié.",
        "Ta façon d'aborder le travail quotidien est flexible et multitâche. Tu es perçu comme quelqu'un de débrouillard qui peut gérer plusieurs choses à la fois. Tu excelles dans les environnements qui changent et qui demandent de la communication.",
        "Tu abordes les routines avec un besoin de variété. Tu peux t'ennuyer des tâches répétitives. Ta santé est liée à ton niveau de stimulation mentale — le stress mental peut affecter ton système nerveux.",
        ["Crée des routines variées qui stimulent ton esprit.", "Prends soin de ton système nerveux.", "Journal : « Comment mon besoin de variété influence-t-il ma santé et mon travail ? »"]
    ),
    ('gemini', 7): make_asc_interp(
        "Gémeaux", 7,
        "Tu te présentes au monde avec légèreté — ton approche spontanée anime tes relations.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes qui stimulent ton esprit. Tu as besoin de communication constante dans tes relations. Tu peux avoir du mal avec les partenaires trop émotionnels ou silencieux.",
        "Tu abordes les associations avec curiosité. Tu veux comprendre ton partenaire intellectuellement. Tu peux avoir tendance à rationaliser les émotions relationnelles ou à éviter les conversations profondes par légèreté.",
        ["Communique ouvertement dans tes relations.", "Écoute autant que tu parles.", "Journal : « Comment ma nature communicative influence-t-elle mes partenariats ? »"]
    ),
    ('gemini', 8): make_asc_interp(
        "Gémeaux", 8,
        "Tu te présentes au monde avec légèreté — ton approche spontanée s'applique aux questions profondes.",
        "Tu abordes les crises et les transformations avec curiosité et analyse. Tu cherches à comprendre intellectuellement ce qui se passe. Les questions d'intimité et de transformation peuvent être abordées avec une certaine distance mentale.",
        "Face aux épreuves, ton instinct est de chercher des informations, de parler, d'analyser. Tu peux avoir du mal à te laisser transformer émotionnellement, préférant intellectualiser. Mais ta curiosité te permet d'explorer des territoires que d'autres évitent.",
        ["Utilise ton intelligence pour naviguer les transformations.", "Permets-toi de ressentir, pas seulement de penser.", "Journal : « Comment j'intègre le mental et l'émotionnel dans les moments de crise ? »"]
    ),
    ('gemini', 9): make_asc_interp(
        "Gémeaux", 9,
        "Tu te présentes au monde avec ouverture — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances est vaste et variée. Tu es celui qui veut tout savoir sur tout, qui voyage pour apprendre et qui étudie par passion. Tu défends la liberté de pensée et la diversité des perspectives.",
        "Tu abordes les études supérieures et les voyages avec enthousiasme intellectuel. Tu préfères survoler plusieurs philosophies que d'en approfondir une seule. Tes convictions peuvent changer au gré de tes découvertes.",
        ["Explore de nouveaux horizons intellectuels.", "Approfondis certaines sagesses plutôt que de toutes les survoler.", "Journal : « Comment ma curiosité influence-t-elle ma vision du monde ? »"]
    ),
    ('gemini', 10): make_asc_interp(
        "Gémeaux", 10,
        "Tu te présentes au monde comme un communicateur — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un d'intelligent, adaptable et éloquent. Ta réputation est celle d'un expert en communication ou d'un touche-à-tout talentueux. Tu excelles dans les rôles qui demandent des échanges et de la polyvalence.",
        "Tu abordes ta carrière avec flexibilité — tu peux changer de direction professionnelle plusieurs fois. Tu as du mal avec les carrières trop routinières ou silencieuses.",
        ["Utilise tes talents de communication dans ta carrière.", "Construis une expertise reconnue malgré tes intérêts multiples.", "Journal : « Comment ma polyvalence façonne-t-elle ma vie professionnelle ? »"]
    ),
    ('gemini', 11): make_asc_interp(
        "Gémeaux", 11,
        "Tu te présentes au monde avec sociabilité — ton approche spontanée anime tes projets collectifs.",
        "Dans les groupes, tu es le connecteur, celui qui met les gens en relation. Tu attires des amis divers et stimulants intellectuellement. Tes idéaux pour l'avenir sont progressistes et tu défends la liberté d'expression.",
        "Tu abordes l'amitié et les projets de groupe avec légèreté et ouverture. Tu as beaucoup de connaissances mais peut-être moins d'amis intimes. Tu peux avoir du mal à t'engager profondément dans une seule cause.",
        ["Connecte les gens et les idées au service du collectif.", "Approfondis certaines amitiés plutôt que de toutes les maintenir superficiellement.", "Journal : « Comment ma sociabilité enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('gemini', 12): make_asc_interp(
        "Gémeaux", 12,
        "Tu te présentes au monde avec une curiosité cachée — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie de communicateur opère dans l'ombre. Tu peux avoir une vie mentale intérieure très riche que tu ne partages pas facilement. Tu as des pensées et des idées secrètes, peut-être un journal ou des écrits privés.",
        "Tu abordes la spiritualité et l'inconscient avec curiosité intellectuelle. Tu cherches à comprendre tes rêves et ton inconscient par l'analyse. Tu peux avoir des pensées anxieuses cachées ou te saboter par dispersion mentale.",
        ["Explore ton monde intérieur par l'écriture.", "Calme le bavardage mental par la méditation.", "Journal : « Quelles pensées je garde secrètes et pourquoi ? »"]
    ),

    # CANCER ASCENDANT
    ('cancer', 1): make_asc_interp(
        "Cancer", 1,
        "Tu te présentes au monde avec sensibilité — ton approche spontanée est celle de la protection.",
        "Ton masque est celui du protecteur, de l'être sensible et nourricier. Les gens te perçoivent comme quelqu'un de doux, empathique et maternel/paternel. Tu dégages une aura de chaleur qui met les autres à l'aise. Ta présence physique est souvent accueillante, avec un visage expressif.",
        "Tu abordes la vie par l'émotion et l'intuition. Face à une situation, ton instinct est de ressentir, de protéger, de nourrir. Cette sensibilité te rend empathique mais parfois trop vulnérable. Tu préfères la sécurité émotionnelle à l'aventure.",
        ["Honore ta sensibilité comme une force.", "Protège-toi sans te fermer complètement.", "Journal : « Comment ma sensibilité naturelle me guide-t-elle dans la vie ? »"]
    ),
    ('cancer', 2): make_asc_interp(
        "Cancer", 2,
        "Tu te présentes au monde avec douceur — ton approche spontanée colore ta relation aux ressources.",
        "Ton énergie nourricière influence ta façon de gagner et de sécuriser tes ressources. Tu es perçu comme quelqu'un qui sait prendre soin de ce qu'il possède. Tu recherches la sécurité financière pour te sentir émotionnellement stable.",
        "Tu abordes les questions d'argent avec un besoin de sécurité. Tu économises instinctivement pour les jours difficiles. Tu peux avoir un attachement émotionnel à tes possessions, surtout celles qui ont une valeur sentimentale.",
        ["Construis une sécurité financière qui nourrit ton besoin émotionnel.", "Évite de t'attacher excessivement aux possessions.", "Journal : « Comment mon besoin de sécurité influence-t-il mes finances ? »"]
    ),
    ('cancer', 3): make_asc_interp(
        "Cancer", 3,
        "Tu te présentes au monde avec empathie — ton approche spontanée s'exprime dans ta communication émotionnelle.",
        "Ta façon de communiquer est teintée d'émotion et d'intuition. Les gens te perçoivent comme quelqu'un qui écoute avec le cœur. Dans ton environnement proche, tu apportes chaleur et soutien. Tes échanges avec frères et sœurs sont souvent nourriciers.",
        "Tu apprends mieux quand tu te sens en sécurité émotionnelle. Ton esprit est intuitif, captant les non-dits et les ambiances. Tu retiens ce qui t'a touché émotionnellement.",
        ["Communique avec ton cœur autant qu'avec ta tête.", "Protège ta sensibilité dans les échanges difficiles.", "Journal : « Comment mes émotions colorent-elles ma façon de communiquer ? »"]
    ),
    ('cancer', 4): make_asc_interp(
        "Cancer", 4,
        "Tu te présentes au monde avec chaleur — ton approche spontanée s'épanouit dans ta vie familiale.",
        "Ici, ton masque et ta maison sont en harmonie parfaite. Tu incarnes naturellement les valeurs cancériennes de foyer et de famille. Tu as besoin d'un chez-toi qui soit un nid, un refuge émotionnel. Tes racines et ta famille sont au cœur de ton identité.",
        "Tu abordes ta vie privée comme un sanctuaire sacré. Tu investis énormément dans ton foyer et dans les liens familiaux. Le passé et la mémoire familiale sont importants pour toi.",
        ["Crée un foyer qui nourrit ton âme.", "Honore tes racines tout en évoluant.", "Journal : « Comment ma famille et mon foyer façonnent-ils qui je suis ? »"]
    ),
    ('cancer', 5): make_asc_interp(
        "Cancer", 5,
        "Tu te présentes au monde avec tendresse — ton approche spontanée s'exprime dans ta créativité.",
        "Ton énergie nourricière s'exprime dans tes créations et tes passions. Tu es perçu comme quelqu'un de romantique et protecteur. En amour, tu offres sécurité et dévotion. Avec les enfants, tu es le parent nourricier par excellence.",
        "Tu abordes les loisirs et la romance avec émotion. Tu crées pour exprimer tes sentiments. Tes passions sont liées à ce qui te touche au cœur et tu t'attaches profondément.",
        ["Exprime ta créativité à travers tes émotions.", "Protège ton cœur créatif sans le fermer.", "Journal : « Comment mes émotions nourrissent-elles ma créativité et mes amours ? »"]
    ),
    ('cancer', 6): make_asc_interp(
        "Cancer", 6,
        "Tu te présentes au monde avec sollicitude — ton approche spontanée s'applique au service quotidien.",
        "Ta façon d'aborder le travail quotidien et la santé est nourricière. Tu es perçu comme quelqu'un qui prend soin des autres au travail. Tu excelles dans les environnements où tu peux aider et soutenir.",
        "Tu abordes les routines avec un besoin de sécurité. Ta santé est directement liée à ton état émotionnel — le stress affecte ton système digestif. Tu as besoin de te sentir en sécurité pour bien travailler.",
        ["Crée des routines qui nourrissent ton bien-être émotionnel.", "Prends soin de toi autant que tu prends soin des autres.", "Journal : « Comment mes émotions influencent-elles ma santé et mon travail ? »"]
    ),
    ('cancer', 7): make_asc_interp(
        "Cancer", 7,
        "Tu te présentes au monde avec douceur — ton approche spontanée recherche des relations sécurisantes.",
        "Dans les partenariats, tu attires ou tu es attiré par des personnes qui offrent sécurité ou qui ont besoin de ta protection. Tu es un partenaire dévoué qui crée un nid relationnel. Tu peux avoir tendance à materner/paterner ton partenaire.",
        "Tu abordes les associations avec un besoin de sécurité émotionnelle. Tu t'investis profondément et tu peux avoir du mal avec le détachement. Tu as besoin de te sentir en sécurité pour t'ouvrir vraiment.",
        ["Crée des partenariats qui nourrissent mutuellement.", "Évite de surprotéger ou de te rendre trop dépendant.", "Journal : « Comment mon besoin de sécurité influence-t-il mes partenariats ? »"]
    ),
    ('cancer', 8): make_asc_interp(
        "Cancer", 8,
        "Tu te présentes au monde avec sensibilité — ton approche spontanée s'applique aux transformations émotionnelles.",
        "Tu abordes les crises et les transformations avec ton cœur. Tu ressens profondément les pertes et les fins. Les questions d'intimité et de vulnérabilité sont abordées avec prudence protectrice mais aussi avec une grande capacité empathique.",
        "Face aux épreuves, ton instinct est de te replier pour te protéger. Tu peux avoir du mal à lâcher prise sur ce que tu as aimé. Mais ta sensibilité te permet de traverser les transformations avec une profondeur émotionnelle que d'autres n'atteignent pas.",
        ["Utilise ta sensibilité pour naviguer les transformations.", "Permets-toi de lâcher prise quand c'est nécessaire.", "Journal : « Comment mon cœur guide-t-il ma façon de gérer les crises ? »"]
    ),
    ('cancer', 9): make_asc_interp(
        "Cancer", 9,
        "Tu te présentes au monde avec intuition — ton approche spontanée s'étend à ta quête de sens.",
        "Ta soif de connaissances et d'aventure est teintée d'émotion. Tu es attiré par les philosophies qui parlent au cœur, les traditions spirituelles qui nourrissent l'âme. Tu explores le monde en cherchant ce qui te fait te sentir chez toi.",
        "Tu abordes les études supérieures et les voyages avec ton cœur. Tu apprends mieux ce qui te touche émotionnellement. Tes convictions sont liées à tes racines et tes traditions familiales.",
        ["Explore de nouveaux horizons qui nourrissent ton âme.", "Reste ouvert aux sagesses différentes de tes traditions.", "Journal : « Comment mes émotions guident-elles ma quête de sens ? »"]
    ),
    ('cancer', 10): make_asc_interp(
        "Cancer", 10,
        "Tu te présentes au monde comme un protecteur — ton approche spontanée façonne ta carrière.",
        "Tu es perçu publiquement comme quelqu'un de fiable, nourricier et empathique. Ta réputation est celle de quelqu'un qui prend soin. Tu excelles dans les rôles qui impliquent d'aider, de protéger ou de nourrir les autres.",
        "Tu abordes ta carrière avec un besoin de sécurité. Tu peux hésiter à prendre des risques professionnels. Tu t'épanouis dans les environnements de travail qui ressemblent à une famille.",
        ["Utilise tes qualités nourricières dans ta carrière.", "Trouve une vocation qui te permet de prendre soin.", "Journal : « Comment mon besoin de protéger façonne-t-il ma vie professionnelle ? »"]
    ),
    ('cancer', 11): make_asc_interp(
        "Cancer", 11,
        "Tu te présentes au monde avec bienveillance — ton approche spontanée s'applique aux projets collectifs.",
        "Dans les groupes, tu apportes chaleur et cohésion. Tu attires des amis qui deviennent comme une famille. Tes idéaux pour l'avenir sont liés à la protection des plus vulnérables et au bien-être collectif.",
        "Tu abordes l'amitié et les projets de groupe avec dévouement. Tu es l'ami qui nourrit et qui console. Tu peux avoir du mal avec les groupes trop impersonnels ou compétitifs.",
        ["Apporte ta chaleur aux projets collectifs.", "Crée des communautés qui ressemblent à des familles.", "Journal : « Comment ma bienveillance enrichit-elle mes amitiés et mes causes ? »"]
    ),
    ('cancer', 12): make_asc_interp(
        "Cancer", 12,
        "Tu te présentes au monde avec une sensibilité cachée — ton approche spontanée habite ton monde intérieur.",
        "Ton énergie nourricière opère dans l'ombre. Tu peux avoir une vie émotionnelle intérieure très riche que tu ne montres pas facilement. Tu as des émotions et des besoins de protection secrets, peut-être liés au passé ou à la famille.",
        "Tu abordes la spiritualité et l'inconscient avec ton cœur. Tu ressens intuitivement ce qui est caché. Tu peux avoir des peurs cachées ou te saboter par excès de protection de toi-même.",
        ["Explore ton monde intérieur avec tendresse.", "Soigne les blessures émotionnelles cachées.", "Journal : « Quelles émotions je garde secrètes et pourquoi ? »"]
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
