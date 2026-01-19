#!/usr/bin/env python3
"""
Insert MC (Midheaven) interpretations for Aries, Taurus, Gemini, Cancer (48 entries)
Version 2 format with consistent structure
"""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from uuid import uuid4
from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation


def make_mc_interp(sign_name: str, house: int, phrase: str, vocation: str, image: str, tips: list[str]) -> str:
    """Generate MC interpretation with consistent structure."""
    tips_formatted = "\n".join(f"- {t}" for t in tips)
    return f"""# MC en {sign_name}

**En une phrase :** {phrase}

## Ta vocation publique
{vocation}

## Ton image au sommet
{image}

## Pistes d'intégration
{tips_formatted}"""


MC_INTERPRETATIONS = {
    # ARIES MC
    ('aries', 1): make_mc_interp(
        "Bélier", 1,
        "Ta vocation est celle du pionnier — tu es appelé à diriger et à innover.",
        "Tu es fait pour être en première ligne, pour ouvrir des voies nouvelles. Ta carrière idéale te permet d'agir, de décider, de prendre des risques. Tu excelles dans les rôles de leadership, l'entrepreneuriat ou tout domaine où tu peux être indépendant et proactif.",
        "Le monde te voit comme un leader né, quelqu'un de courageux et d'entreprenant. Ta réputation est celle d'une personne qui n'a pas peur de se lancer, qui ose là où d'autres hésitent. On te respecte pour ton audace et ta capacité à initier des projets.",
        ["Assume ton rôle de pionnier dans ta carrière.", "Canalise ton énergie pour construire durablement.", "Journal : « Comment puis-je exprimer mon leadership de façon constructive ? »"]
    ),
    ('aries', 2): make_mc_interp(
        "Bélier", 2,
        "Ta vocation de pionnier s'enracine dans ta capacité à créer de la valeur — tu construis ta réputation sur tes ressources.",
        "Ta mission publique est liée à ta capacité à générer de la valeur. Tu es appelé à être un entrepreneur, un créateur de richesse, quelqu'un qui transforme l'audace en ressources concrètes. Ton approche directe te permet de saisir les opportunités financières.",
        "On te perçoit comme quelqu'un qui sait ce qu'il veut et qui a les moyens de l'obtenir. Ta réputation est celle d'un bâtisseur ambitieux qui ose investir et risquer pour créer de la valeur.",
        ["Utilise ton audace pour créer des ressources.", "Construis une réputation d'entrepreneur courageux.", "Journal : « Comment mon énergie pionnière peut-elle générer de la valeur durable ? »"]
    ),
    ('aries', 3): make_mc_interp(
        "Bélier", 3,
        "Ta vocation de pionnier s'exprime à travers la communication — tu es appelé à porter des idées nouvelles.",
        "Ta mission publique passe par les mots et les idées. Tu es fait pour être un communicateur direct, un porte-parole qui n'a pas peur de dire les choses. Tu excelles dans le journalisme d'investigation, le marketing percutant ou l'enseignement dynamique.",
        "On te perçoit comme quelqu'un de vif, d'éloquent et de franc. Ta réputation est celle d'une personne qui communique avec impact et qui n'hésite pas à défendre ses idées publiquement.",
        ["Utilise ta voix pour porter des messages importants.", "Communique avec audace et responsabilité.", "Journal : « Comment puis-je utiliser ma communication pour ouvrir des voies nouvelles ? »"]
    ),
    ('aries', 4): make_mc_interp(
        "Bélier", 4,
        "Ta vocation de pionnier est nourrie par tes racines — tu construis ta mission sur des fondations audacieuses.",
        "Ta mission publique est profondément liée à ton histoire familiale et à tes origines. Peut-être as-tu hérité d'un esprit d'entreprise ou tu cherches à créer ce que ta famille n'a pas pu. Tu bâtis ta carrière sur des convictions personnelles profondes.",
        "Le monde te voit comme quelqu'un de déterminé qui porte ses valeurs familiales ou personnelles dans le monde professionnel. Ta réputation est celle d'une personne authentique qui construit à partir de ses racines.",
        ["Honore tes racines tout en pionnier ta propre voie.", "Construis ta carrière sur des fondations solides.", "Journal : « Comment mon histoire familiale nourrit-elle ma vocation ? »"]
    ),
    ('aries', 5): make_mc_interp(
        "Bélier", 5,
        "Ta vocation de pionnier s'exprime dans la créativité — tu es appelé à briller par ton audace artistique.",
        "Ta mission publique passe par l'expression créative. Tu es fait pour être un artiste audacieux, un créateur qui n'a pas peur de choquer ou d'innover. Tu excelles dans les arts de la scène, le leadership créatif ou tout domaine où tu peux exprimer ta personnalité unique.",
        "On te perçoit comme quelqu'un de passionné, de créatif et de magnétique. Ta réputation est celle d'un artiste ou d'un leader qui inspire par son courage d'être pleinement lui-même.",
        ["Exprime ta créativité avec courage.", "Ose montrer au monde ton unicité.", "Journal : « Comment puis-je briller publiquement par ma créativité audacieuse ? »"]
    ),
    ('aries', 6): make_mc_interp(
        "Bélier", 6,
        "Ta vocation de pionnier s'applique au service — tu es appelé à révolutionner les méthodes de travail.",
        "Ta mission publique passe par l'amélioration des systèmes. Tu es fait pour être un réformateur du travail, quelqu'un qui optimise et qui n'a pas peur de bousculer les routines. Tu excelles dans la gestion de crise, la médecine d'urgence ou tout domaine qui demande action et efficacité.",
        "On te perçoit comme quelqu'un d'efficace, de déterminé et de résoluteur de problèmes. Ta réputation est celle d'une personne qui agit vite et bien quand il faut résoudre des situations.",
        ["Utilise ton énergie pour améliorer les systèmes.", "Sois le pionnier de meilleures méthodes.", "Journal : « Comment puis-je servir le monde par mon efficacité audacieuse ? »"]
    ),
    ('aries', 7): make_mc_interp(
        "Bélier", 7,
        "Ta vocation de pionnier s'accomplit dans le partenariat — tu es appelé à mener dans la collaboration.",
        "Ta mission publique passe par les alliances stratégiques. Tu es fait pour être un négociateur assertif, un partenaire qui apporte l'énergie et la direction. Tu excelles dans les relations publiques, le droit ou tout domaine où tu dois représenter et défendre.",
        "On te perçoit comme quelqu'un de charismatique dans les partenariats, capable de mener tout en collaborant. Ta réputation est celle d'un leader qui sait s'entourer et dynamiser ses équipes.",
        ["Développe des partenariats qui amplifient ton impact.", "Apprends à mener en équipe.", "Journal : « Comment puis-je accomplir ma mission à travers des collaborations audacieuses ? »"]
    ),
    ('aries', 8): make_mc_interp(
        "Bélier", 8,
        "Ta vocation de pionnier s'applique aux transformations profondes — tu es appelé à mener les changements radicaux.",
        "Ta mission publique touche aux domaines profonds : crises, finances partagées, transformations. Tu es fait pour être un gestionnaire de crise, un investisseur audacieux ou un thérapeute qui n'a pas peur d'aller en profondeur. Tu excelles à gérer ce que les autres évitent.",
        "On te perçoit comme quelqu'un de puissant, capable de naviguer les eaux troubles. Ta réputation est celle d'une personne qui transforme les situations difficiles en opportunités.",
        ["Utilise ton courage pour guider les transformations.", "Sois le pionnier du renouveau.", "Journal : « Comment puis-je aider les autres à traverser leurs crises avec audace ? »"]
    ),
    ('aries', 9): make_mc_interp(
        "Bélier", 9,
        "Ta vocation de pionnier s'étend aux horizons lointains — tu es appelé à explorer et à enseigner.",
        "Ta mission publique est liée à l'expansion des horizons. Tu es fait pour être un explorateur, un enseignant qui inspire ou un entrepreneur international. Tu excelles dans tout ce qui demande de voir grand et d'aller loin.",
        "On te perçoit comme un visionnaire, quelqu'un qui pense en grand et qui n'a pas peur de l'inconnu. Ta réputation est celle d'un aventurier intellectuel ou géographique qui ouvre des voies.",
        ["Explore de nouveaux territoires professionnels.", "Partage ta vision avec audace.", "Journal : « Comment puis-je étendre ma mission aux horizons les plus larges ? »"]
    ),
    ('aries', 10): make_mc_interp(
        "Bélier", 10,
        "Ta vocation de pionnier est au cœur de ta destinée — tu es né pour diriger et innover publiquement.",
        "Ici, le MC en Bélier est dans sa pleine puissance en maison 10. Tu es destiné à être un leader, un chef d'entreprise, un pionnier dans ton domaine. Ta carrière est ta grande aventure et tu es fait pour laisser ta marque dans le monde.",
        "Le monde te voit exactement comme tu es : un meneur, un innovateur, quelqu'un qui n'a pas peur de prendre les devants. Ta réputation publique est celle d'un leader audacieux et accompli.",
        ["Assume pleinement ton rôle de leader.", "Construis une carrière qui reflète ton courage.", "Journal : « Comment puis-je manifester ma pleine puissance de pionnier ? »"]
    ),
    ('aries', 11): make_mc_interp(
        "Bélier", 11,
        "Ta vocation de pionnier sert l'humanité — tu es appelé à mener des mouvements collectifs.",
        "Ta mission publique est liée aux causes collectives et à l'avenir. Tu es fait pour être un leader de mouvement, un innovateur social ou un entrepreneur qui change le monde. Tu excelles à rassembler des gens autour de visions audacieuses.",
        "On te perçoit comme un visionnaire collectif, quelqu'un qui mène des groupes vers de nouveaux horizons. Ta réputation est celle d'un pionnier humanitaire ou technologique.",
        ["Mets ton leadership au service du collectif.", "Inspire des mouvements audacieux.", "Journal : « Comment puis-je utiliser mon énergie pionnière pour l'humanité ? »"]
    ),
    ('aries', 12): make_mc_interp(
        "Bélier", 12,
        "Ta vocation de pionnier opère dans l'invisible — tu es appelé à initier depuis les coulisses.",
        "Ta mission publique est paradoxalement liée à l'ombre et à l'intériorité. Tu es fait pour être un pionnier spirituel, un thérapeute qui aide les gens à affronter leurs peurs ou un artiste qui explore l'inconscient. Tu agis puissamment depuis les coulisses.",
        "Le monde ne voit pas toujours ton influence, mais elle est réelle. Ta réputation se construit sur ta capacité à aider les autres à surmonter leurs obstacles invisibles.",
        ["Sois un pionnier dans les domaines invisibles.", "Aide les autres à vaincre leurs peurs.", "Journal : « Comment puis-je exercer mon leadership dans les espaces cachés ? »"]
    ),

    # TAURUS MC
    ('taurus', 1): make_mc_interp(
        "Taureau", 1,
        "Ta vocation est celle du bâtisseur — tu es appelé à créer de la valeur durable.",
        "Tu es fait pour construire quelque chose de solide et de beau. Ta carrière idéale te permet de créer, de faire croître et d'embellir. Tu excelles dans les domaines liés à la beauté, aux finances, à l'immobilier ou à tout ce qui demande patience et persévérance.",
        "Le monde te voit comme quelqu'un de fiable, de compétent et de constant. Ta réputation est celle d'une personne qui tient ses promesses et qui construit sur la durée. On te fait confiance pour les projets à long terme.",
        ["Construis ta carrière avec patience et solidité.", "Crée de la valeur qui dure.", "Journal : « Comment puis-je bâtir quelque chose de durable dans le monde ? »"]
    ),
    ('taurus', 2): make_mc_interp(
        "Taureau", 2,
        "Ta vocation de bâtisseur est au cœur des ressources — tu es un maître de la prospérité.",
        "Ta mission publique est directement liée à la création de richesse et de valeur. Tu es fait pour être un financier, un gestionnaire de patrimoine ou un entrepreneur qui bâtit des empires matériels. Tes talents naturels pour l'argent sont reconnus.",
        "On te perçoit comme quelqu'un qui sait gérer les ressources, qui fait fructifier ce qu'il touche. Ta réputation est celle d'un expert en création de valeur et en gestion financière.",
        ["Utilise tes talents financiers pour construire.", "Sois le gardien de la prospérité.", "Journal : « Comment puis-je maximiser ma capacité à créer de la valeur ? »"]
    ),
    ('taurus', 3): make_mc_interp(
        "Taureau", 3,
        "Ta vocation de bâtisseur s'exprime dans la communication — tu donnes forme aux idées.",
        "Ta mission publique passe par la communication concrète et tangible. Tu es fait pour être un auteur, un artisan des mots ou un communicant qui rend les choses claires et belles. Tu excelles à traduire les idées en formes compréhensibles.",
        "On te perçoit comme quelqu'un de clair, de fiable dans ses communications. Ta réputation est celle d'une personne qui communique avec solidité et beauté.",
        ["Communique de façon concrète et belle.", "Construis ta réputation par tes paroles fiables.", "Journal : « Comment puis-je donner forme durable aux idées ? »"]
    ),
    ('taurus', 4): make_mc_interp(
        "Taureau", 4,
        "Ta vocation de bâtisseur est nourrie par tes racines — tu construis sur des fondations solides.",
        "Ta mission publique est profondément liée à ton foyer et tes origines. Tu es peut-être destiné à hériter d'une entreprise familiale ou à bâtir quelque chose qui honore tes racines. Tu construis ta carrière sur des valeurs familiales fortes.",
        "Le monde te voit comme quelqu'un d'enraciné, de traditionnel dans le bon sens. Ta réputation est celle d'une personne qui valorise ses origines et qui construit avec intégrité.",
        ["Honore tes racines dans ta construction professionnelle.", "Bâtis sur des fondations familiales solides.", "Journal : « Comment mon héritage familial nourrit-il ma vocation ? »"]
    ),
    ('taurus', 5): make_mc_interp(
        "Taureau", 5,
        "Ta vocation de bâtisseur s'exprime dans la créativité — tu crées de la beauté durable.",
        "Ta mission publique passe par la création artistique et l'expression de la beauté. Tu es fait pour être un artiste, un designer ou un créateur qui produit des œuvres qui durent. Tu excelles à donner forme matérielle à la beauté.",
        "On te perçoit comme quelqu'un de talentueux et d'esthète. Ta réputation est celle d'un créateur qui allie beauté et durabilité.",
        ["Crée de la beauté qui traverse le temps.", "Exprime ta sensibilité artistique.", "Journal : « Comment puis-je manifester la beauté de façon durable ? »"]
    ),
    ('taurus', 6): make_mc_interp(
        "Taureau", 6,
        "Ta vocation de bâtisseur s'applique au service — tu améliores les choses concrètement.",
        "Ta mission publique passe par le travail quotidien et l'amélioration des conditions. Tu es fait pour être un artisan, un praticien de santé naturelle ou quelqu'un qui améliore concrètement la vie des gens. Tu excelles dans le travail méthodique et soigné.",
        "On te perçoit comme quelqu'un de travailleur, de fiable et de compétent. Ta réputation est celle d'un professionnel qui fait du bon travail, solidement.",
        ["Améliore les choses concrètement par ton travail.", "Sois l'artisan de la qualité.", "Journal : « Comment puis-je servir par la qualité de mon travail ? »"]
    ),
    ('taurus', 7): make_mc_interp(
        "Taureau", 7,
        "Ta vocation de bâtisseur s'accomplit dans le partenariat — tu construis des alliances durables.",
        "Ta mission publique passe par les partenariats stables et fructueux. Tu es fait pour être un médiateur, un avocat en droit des affaires ou un collaborateur qui construit des relations professionnelles solides.",
        "On te perçoit comme quelqu'un de fiable en partenariat, qui honore ses engagements. Ta réputation est celle d'un associé stable sur qui on peut compter.",
        ["Construis des partenariats solides et durables.", "Sois le pilier de tes collaborations.", "Journal : « Comment puis-je bâtir ma mission à travers des alliances stables ? »"]
    ),
    ('taurus', 8): make_mc_interp(
        "Taureau", 8,
        "Ta vocation de bâtisseur s'applique aux ressources partagées — tu gères la richesse collective.",
        "Ta mission publique touche aux finances partagées, aux héritages et aux transformations de valeur. Tu es fait pour être un gestionnaire de patrimoine, un conseiller en succession ou quelqu'un qui fait croître les ressources collectives.",
        "On te perçoit comme quelqu'un de digne de confiance avec l'argent des autres. Ta réputation est celle d'un gardien fiable de la richesse partagée.",
        ["Gère les ressources partagées avec intégrité.", "Transforme la valeur de façon durable.", "Journal : « Comment puis-je être un bon gestionnaire des ressources collectives ? »"]
    ),
    ('taurus', 9): make_mc_interp(
        "Taureau", 9,
        "Ta vocation de bâtisseur s'étend aux horizons — tu ancres la sagesse dans le concret.",
        "Ta mission publique est liée à rendre les grandes idées pratiques et tangibles. Tu es fait pour être un enseignant qui ancre la théorie dans la pratique, un éditeur ou quelqu'un qui donne forme aux visions philosophiques.",
        "On te perçoit comme quelqu'un de sage et de pratique. Ta réputation est celle d'une personne qui sait traduire les grandes idées en réalités concrètes.",
        ["Ancre les grandes visions dans le concret.", "Enseigne par l'exemple pratique.", "Journal : « Comment puis-je donner forme tangible aux grandes idées ? »"]
    ),
    ('taurus', 10): make_mc_interp(
        "Taureau", 10,
        "Ta vocation de bâtisseur est au cœur de ta destinée — tu es né pour construire ta place au sommet.",
        "Ici, le MC en Taureau est dans sa pleine puissance. Tu es destiné à construire une carrière solide, à atteindre une position de stabilité et de respect. Tu bâtis lentement mais sûrement ton empire.",
        "Le monde te voit comme quelqu'un de stable, de fiable et de compétent. Ta réputation publique est celle d'un bâtisseur qui réussit par la persévérance.",
        ["Construis ta position avec patience et détermination.", "Deviens le pilier de ton domaine.", "Journal : « Comment puis-je atteindre le sommet par ma solidité naturelle ? »"]
    ),
    ('taurus', 11): make_mc_interp(
        "Taureau", 11,
        "Ta vocation de bâtisseur sert l'humanité — tu construis pour le collectif.",
        "Ta mission publique est liée à la création de ressources collectives. Tu es fait pour construire des organisations stables, des systèmes qui perdurent ou des communautés qui prospèrent.",
        "On te perçoit comme quelqu'un qui apporte stabilité aux projets collectifs. Ta réputation est celle d'un bâtisseur communautaire.",
        ["Mets tes talents de construction au service du collectif.", "Crée des fondations durables pour les autres.", "Journal : « Comment puis-je bâtir quelque chose de durable pour l'humanité ? »"]
    ),
    ('taurus', 12): make_mc_interp(
        "Taureau", 12,
        "Ta vocation de bâtisseur opère dans l'invisible — tu ancres ce qui est éthéré.",
        "Ta mission publique est de donner forme concrète à l'invisible. Tu es fait pour être un artiste spirituel, un thérapeute qui aide à incarner ou quelqu'un qui construit des refuges pour les âmes perdues.",
        "Le monde ne voit pas toujours ce que tu construis, mais tes créations nourrissent l'âme collective. Ta réputation se fait dans les espaces subtils.",
        ["Donne forme à l'invisible.", "Construis des refuges pour l'esprit.", "Journal : « Comment puis-je ancrer le spirituel dans le matériel ? »"]
    ),

    # GEMINI MC
    ('gemini', 1): make_mc_interp(
        "Gémeaux", 1,
        "Ta vocation est celle du communicateur — tu es appelé à connecter et à informer.",
        "Tu es fait pour être un passeur d'idées, un connecteur de personnes et d'informations. Ta carrière idéale implique la communication, les échanges, l'écriture ou l'enseignement. Tu excelles dans tout ce qui demande agilité mentale et polyvalence.",
        "Le monde te voit comme quelqu'un d'intelligent, de vif et d'adaptable. Ta réputation est celle d'un expert en communication, quelqu'un qui sait parler à tous les publics et qui maîtrise l'art des mots.",
        ["Utilise tes dons de communication pour ta carrière.", "Connecte les idées et les personnes.", "Journal : « Comment puis-je servir le monde par ma capacité à communiquer ? »"]
    ),
    ('gemini', 2): make_mc_interp(
        "Gémeaux", 2,
        "Ta vocation de communicateur s'applique aux ressources — tu multiplies les sources de revenus.",
        "Ta mission publique est liée à l'utilisation intelligente de l'information pour créer de la valeur. Tu es fait pour être un entrepreneur multitâche, un trader ou quelqu'un qui transforme les idées en argent.",
        "On te perçoit comme quelqu'un de malin avec les ressources, capable de trouver des opportunités partout. Ta réputation est celle d'un professionnel polyvalent qui sait diversifier.",
        ["Multiplie intelligemment tes sources de revenus.", "Transforme tes idées en valeur.", "Journal : « Comment puis-je utiliser mon intelligence pour créer de la prospérité ? »"]
    ),
    ('gemini', 3): make_mc_interp(
        "Gémeaux", 3,
        "Ta vocation de communicateur est à son apogée — tu es né pour transmettre.",
        "Ici, le MC en Gémeaux est dans sa pleine puissance en maison 3. Tu es destiné à être un communicateur professionnel : journaliste, écrivain, enseignant, marketeur ou influenceur. Les mots et les idées sont ton domaine.",
        "Le monde te voit exactement comme tu es : brillant, éloquent et connecté. Ta réputation publique est celle d'un maître des mots et des idées.",
        ["Excelle dans l'art de la communication.", "Deviens une référence dans la transmission.", "Journal : « Comment puis-je maximiser mon don pour les mots et les idées ? »"]
    ),
    ('gemini', 4): make_mc_interp(
        "Gémeaux", 4,
        "Ta vocation de communicateur est nourrie par tes racines — tu transmets l'héritage familial.",
        "Ta mission publique est liée à la transmission de ton histoire familiale ou culturelle. Tu es peut-être destiné à écrire sur ta famille, à enseigner les traditions ou à connecter les générations par les mots.",
        "On te perçoit comme quelqu'un qui porte une histoire, qui transmet avec intelligence. Ta réputation est celle d'un passeur de mémoire.",
        ["Transmets l'héritage de tes racines.", "Utilise ta voix pour honorer ton histoire.", "Journal : « Comment puis-je communiquer ce qui vient de mes racines ? »"]
    ),
    ('gemini', 5): make_mc_interp(
        "Gémeaux", 5,
        "Ta vocation de communicateur s'exprime dans la créativité — tu divertis et tu inspires.",
        "Ta mission publique passe par la communication créative et divertissante. Tu es fait pour être un auteur de fiction, un humoriste, un créateur de contenu ou un animateur. Tu excelles à rendre les idées amusantes et engageantes.",
        "On te perçoit comme quelqu'un de brillant et de divertissant. Ta réputation est celle d'un créateur qui sait captiver son public par l'esprit et la légèreté.",
        ["Exprime ta créativité à travers les mots.", "Divertis et éduque à la fois.", "Journal : « Comment puis-je utiliser ma communication pour inspirer et divertir ? »"]
    ),
    ('gemini', 6): make_mc_interp(
        "Gémeaux", 6,
        "Ta vocation de communicateur s'applique au service — tu informes pour aider.",
        "Ta mission publique passe par la communication utile et pratique. Tu es fait pour être un conseiller, un formateur technique ou un communicateur en santé. Tu excelles à rendre l'information accessible et utile.",
        "On te perçoit comme quelqu'un de serviable et d'informatif. Ta réputation est celle d'un professionnel qui aide par le partage de connaissances pratiques.",
        ["Communique pour aider concrètement.", "Rends l'information accessible.", "Journal : « Comment puis-je servir les autres par ma capacité à informer ? »"]
    ),
    ('gemini', 7): make_mc_interp(
        "Gémeaux", 7,
        "Ta vocation de communicateur s'accomplit dans le partenariat — tu es le diplomate des mots.",
        "Ta mission publique passe par la communication dans les relations. Tu es fait pour être un médiateur, un avocat ou un conseiller en communication relationnelle. Tu excelles à faciliter le dialogue entre les parties.",
        "On te perçoit comme quelqu'un de diplomate et d'éloquent. Ta réputation est celle d'un médiateur qui sait trouver les mots justes pour rapprocher les gens.",
        ["Facilite le dialogue par tes mots.", "Sois le pont entre les personnes.", "Journal : « Comment puis-je utiliser ma communication pour créer des connexions ? »"]
    ),
    ('gemini', 8): make_mc_interp(
        "Gémeaux", 8,
        "Ta vocation de communicateur s'applique aux profondeurs — tu transmets l'invisible.",
        "Ta mission publique touche à la communication sur les sujets profonds : psychologie, sexualité, mort, transformation. Tu es fait pour être un thérapeute qui parle, un auteur sur les mystères ou un communicateur sur les tabous.",
        "On te perçoit comme quelqu'un qui ose parler de ce que les autres évitent. Ta réputation est celle d'un communicateur des profondeurs.",
        ["Parle des sujets que les autres taisent.", "Communique sur la transformation.", "Journal : « Comment puis-je utiliser mes mots pour éclairer les profondeurs ? »"]
    ),
    ('gemini', 9): make_mc_interp(
        "Gémeaux", 9,
        "Ta vocation de communicateur s'étend aux horizons — tu enseignes et tu publies.",
        "Ta mission publique est liée à la diffusion du savoir à grande échelle. Tu es fait pour être un professeur d'université, un auteur publié internationalement ou un communicateur interculturel. Tu transmets la sagesse.",
        "On te perçoit comme quelqu'un de cultivé et d'érudit. Ta réputation est celle d'un penseur qui sait communiquer les grandes idées.",
        ["Diffuse le savoir à grande échelle.", "Enseigne ce que tu as appris.", "Journal : « Comment puis-je partager ma sagesse avec le monde ? »"]
    ),
    ('gemini', 10): make_mc_interp(
        "Gémeaux", 10,
        "Ta vocation de communicateur est ta destinée publique — tu es reconnu pour tes mots.",
        "Le MC en Gémeaux en maison 10 fait de toi un communicateur public par excellence. Tu es destiné à être connu pour tes paroles, tes écrits ou ta capacité à connecter. Ta carrière tourne autour de la communication sous toutes ses formes.",
        "Le monde te voit comme l'expert en communication. Ta réputation est celle d'un maître des mots qui sait toucher tous les publics.",
        ["Deviens reconnu pour ta communication.", "Construis ta réputation sur tes mots.", "Journal : « Comment puis-je atteindre le sommet par ma maîtrise de la communication ? »"]
    ),
    ('gemini', 11): make_mc_interp(
        "Gémeaux", 11,
        "Ta vocation de communicateur sert l'humanité — tu connectes les communautés.",
        "Ta mission publique est de faciliter la communication collective. Tu es fait pour être un organisateur de réseaux, un communicateur pour des causes ou un connecteur de communautés diverses.",
        "On te perçoit comme quelqu'un qui rassemble par les mots. Ta réputation est celle d'un communicateur qui sert le collectif.",
        ["Connecte les communautés par ta communication.", "Utilise tes mots pour le bien commun.", "Journal : « Comment puis-je utiliser ma communication pour l'humanité ? »"]
    ),
    ('gemini', 12): make_mc_interp(
        "Gémeaux", 12,
        "Ta vocation de communicateur opère dans l'invisible — tu donnes voix à l'indicible.",
        "Ta mission publique est de communiquer ce qui est caché ou difficile à exprimer. Tu es fait pour être un écrivain introspectif, un thérapeute qui utilise les mots pour guérir ou un poète qui touche l'âme.",
        "Le monde ne voit pas toujours ton travail de communication, mais tes mots touchent les profondeurs. Ta réputation se fait dans l'ombre.",
        ["Donne voix à ce qui est caché.", "Communique avec l'inconscient collectif.", "Journal : « Comment puis-je exprimer l'indicible ? »"]
    ),

    # CANCER MC
    ('cancer', 1): make_mc_interp(
        "Cancer", 1,
        "Ta vocation est celle du protecteur — tu es appelé à prendre soin et à nourrir.",
        "Tu es fait pour être un gardien, quelqu'un qui prend soin des autres dans ta carrière. Ta vocation idéale implique le soin, la protection, l'alimentation ou la création de sécurité. Tu excelles dans tout ce qui demande empathie et attention aux besoins émotionnels.",
        "Le monde te voit comme quelqu'un de bienveillant, de maternel/paternel et de protecteur. Ta réputation est celle d'une personne qui crée un environnement sécurisant pour les autres.",
        ["Utilise tes dons de protection pour ta carrière.", "Crée de la sécurité pour les autres.", "Journal : « Comment puis-je nourrir le monde par ma vocation ? »"]
    ),
    ('cancer', 2): make_mc_interp(
        "Cancer", 2,
        "Ta vocation de protecteur s'applique aux ressources — tu nourris par l'abondance.",
        "Ta mission publique est liée à la création de sécurité matérielle pour toi et les autres. Tu es fait pour être dans l'alimentation, l'immobilier familial ou la gestion de patrimoine familial. Tu crées de la valeur qui nourrit.",
        "On te perçoit comme quelqu'un qui sait créer la sécurité. Ta réputation est celle d'un gardien de la prospérité familiale.",
        ["Crée des ressources qui nourrissent.", "Protège la sécurité matérielle.", "Journal : « Comment puis-je utiliser les ressources pour nourrir et protéger ? »"]
    ),
    ('cancer', 3): make_mc_interp(
        "Cancer", 3,
        "Ta vocation de protecteur s'exprime dans la communication — tu parles au cœur.",
        "Ta mission publique passe par une communication qui touche les émotions. Tu es fait pour être un auteur qui touche les cœurs, un thérapeute qui écoute ou un communicateur empathique. Tu excelles à créer la connexion émotionnelle par les mots.",
        "On te perçoit comme quelqu'un de chaleureux dans sa communication. Ta réputation est celle d'un communicateur qui sait parler à l'âme.",
        ["Communique avec ton cœur.", "Touche les autres par tes paroles bienveillantes.", "Journal : « Comment puis-je utiliser ma communication pour réconforter ? »"]
    ),
    ('cancer', 4): make_mc_interp(
        "Cancer", 4,
        "Ta vocation de protecteur est au cœur de tes racines — tu travailles avec la famille.",
        "Ici, le MC en Cancer est dans sa pleine puissance en maison 4. Tu es destiné à travailler dans un contexte familial : entreprise familiale, immobilier, généalogie ou tout domaine lié au foyer et aux racines.",
        "Le monde te voit comme quelqu'un de profondément connecté à ses racines. Ta réputation publique est celle d'un gardien des traditions familiales.",
        ["Construis ta carrière autour de la famille.", "Honore tes racines dans ta vocation.", "Journal : « Comment puis-je faire de mes racines ma mission ? »"]
    ),
    ('cancer', 5): make_mc_interp(
        "Cancer", 5,
        "Ta vocation de protecteur s'exprime dans la créativité — tu crées avec amour.",
        "Ta mission publique passe par la création nourricière. Tu es fait pour être un artiste qui touche les émotions, quelqu'un qui travaille avec les enfants ou un créateur de contenus réconfortants. Tes créations sont comme des enfants.",
        "On te perçoit comme quelqu'un de créatif et de nourricier. Ta réputation est celle d'un créateur qui met de l'amour dans tout ce qu'il fait.",
        ["Crée avec amour et émotion.", "Nourris les autres par ta créativité.", "Journal : « Comment puis-je exprimer ma créativité de façon nourricière ? »"]
    ),
    ('cancer', 6): make_mc_interp(
        "Cancer", 6,
        "Ta vocation de protecteur s'applique au service — tu soignes au quotidien.",
        "Ta mission publique passe par le soin quotidien aux autres. Tu es fait pour être dans les métiers de la santé, de l'aide à domicile ou de l'alimentation. Tu excelles à prendre soin des autres de façon pratique.",
        "On te perçoit comme quelqu'un de serviable et de bienveillant. Ta réputation est celle d'un professionnel qui prend soin avec dévouement.",
        ["Prends soin des autres dans ton travail quotidien.", "Sois le gardien du bien-être.", "Journal : « Comment puis-je servir en prenant soin ? »"]
    ),
    ('cancer', 7): make_mc_interp(
        "Cancer", 7,
        "Ta vocation de protecteur s'accomplit dans le partenariat — tu crées des liens nourriciers.",
        "Ta mission publique passe par les partenariats bienveillants. Tu es fait pour être un conseiller conjugal, un médiateur familial ou un collaborateur qui crée de la sécurité émotionnelle dans les relations professionnelles.",
        "On te perçoit comme quelqu'un de sécurisant en partenariat. Ta réputation est celle d'un associé qui prend soin de ses relations.",
        ["Crée des partenariats nourriciers.", "Prends soin de tes collaborations.", "Journal : « Comment puis-je nourrir mes partenariats professionnels ? »"]
    ),
    ('cancer', 8): make_mc_interp(
        "Cancer", 8,
        "Ta vocation de protecteur s'applique aux transformations — tu accompagnes les passages.",
        "Ta mission publique touche aux moments de transition émotionnelle. Tu es fait pour être un accompagnateur de deuil, un thérapeute qui aide à traverser les crises ou quelqu'un qui protège pendant les transformations.",
        "On te perçoit comme quelqu'un de fort dans les moments difficiles. Ta réputation est celle d'un gardien qui accompagne les passages.",
        ["Accompagne les autres dans leurs transformations.", "Protège pendant les crises.", "Journal : « Comment puis-je aider les autres à traverser leurs épreuves ? »"]
    ),
    ('cancer', 9): make_mc_interp(
        "Cancer", 9,
        "Ta vocation de protecteur s'étend aux horizons — tu nourris par la sagesse.",
        "Ta mission publique est liée à l'enseignement nourricier et à la transmission de sagesse réconfortante. Tu es fait pour être un enseignant bienveillant, un guide spirituel maternel ou un auteur de livres réconfortants.",
        "On te perçoit comme quelqu'un de sage et de bienveillant. Ta réputation est celle d'un guide qui nourrit l'âme.",
        ["Enseigne avec bienveillance.", "Nourris les autres par ta sagesse.", "Journal : « Comment puis-je transmettre une sagesse réconfortante ? »"]
    ),
    ('cancer', 10): make_mc_interp(
        "Cancer", 10,
        "Ta vocation de protecteur est ta destinée publique — tu es reconnu pour ton soin.",
        "Le MC en Cancer en maison 10 fait de toi un protecteur public. Tu es destiné à être connu pour prendre soin : médecin, thérapeute, chef cuisinier, gestionnaire de foyer. Ta carrière est centrée sur le soin.",
        "Le monde te voit comme le grand protecteur. Ta réputation est celle de quelqu'un qui met le bien-être des autres au centre.",
        ["Deviens reconnu pour ta capacité à prendre soin.", "Construis ta réputation sur ta bienveillance.", "Journal : « Comment puis-je atteindre le sommet par ma vocation de protecteur ? »"]
    ),
    ('cancer', 11): make_mc_interp(
        "Cancer", 11,
        "Ta vocation de protecteur sert l'humanité — tu crées des communautés familiales.",
        "Ta mission publique est de créer de la sécurité collective. Tu es fait pour construire des communautés qui fonctionnent comme des familles, des organisations qui prennent soin ou des mouvements qui protègent les plus vulnérables.",
        "On te perçoit comme quelqu'un qui materne le collectif. Ta réputation est celle d'un créateur de familles élargies.",
        ["Crée des communautés nourricières.", "Protège le collectif comme une famille.", "Journal : « Comment puis-je prendre soin de l'humanité ? »"]
    ),
    ('cancer', 12): make_mc_interp(
        "Cancer", 12,
        "Ta vocation de protecteur opère dans l'invisible — tu soignes l'âme du monde.",
        "Ta mission publique est de prendre soin de ce qui est caché ou oublié. Tu es fait pour être un soignant de l'âme, un protecteur des exclus ou quelqu'un qui nourrit l'inconscient collectif.",
        "Le monde ne voit pas toujours ton soin, mais tu nourris l'invisible. Ta réputation se fait dans les espaces cachés.",
        ["Prends soin de ce que le monde oublie.", "Nourris l'invisible.", "Journal : « Comment puis-je soigner l'âme du monde ? »"]
    ),
}


async def insert_interpretations():
    """Insert MC interpretations into database."""
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in MC_INTERPRETATIONS.items():
            # Check if already exists
            query = select(PregeneratedNatalInterpretation).where(
                PregeneratedNatalInterpretation.subject == "mc",
                PregeneratedNatalInterpretation.sign == sign,
                PregeneratedNatalInterpretation.house == house,
                PregeneratedNatalInterpretation.version == 2,
                PregeneratedNatalInterpretation.lang == "fr"
            )
            result = await db.execute(query)
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️ SKIP mc/{sign}/M{house} (already exists)")
                skipped += 1
                continue

            # Insert new interpretation
            interpretation = PregeneratedNatalInterpretation(
                id=uuid4(),
                subject="mc",
                sign=sign,
                house=house,
                version=2,
                lang="fr",
                content=content,
                length=len(content)
            )
            db.add(interpretation)
            print(f"✅ INSERT mc/{sign}/M{house} ({len(content)} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")


if __name__ == "__main__":
    asyncio.run(insert_interpretations())
