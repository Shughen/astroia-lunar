#!/usr/bin/env python3
"""
Insert MC (Midheaven) interpretations for Leo, Virgo, Libra, Scorpio (48 entries)
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
    # LEO MC
    ('leo', 1): make_mc_interp(
        "Lion", 1,
        "Ta vocation est celle du leader charismatique — tu es appelé à briller et à inspirer.",
        "Tu es fait pour être au centre de la scène, pour diriger avec cœur et charisme. Ta carrière idéale te permet de briller, de créer et de recevoir de la reconnaissance. Tu excelles dans les rôles de leadership créatif, les arts, le divertissement ou tout domaine où ta personnalité peut rayonner.",
        "Le monde te voit comme quelqu'un de charismatique, de confiant et de généreux. Ta réputation est celle d'un leader qui inspire par son exemple et sa présence lumineuse. On te respecte pour ton courage d'être pleinement toi-même.",
        ["Brille dans ta carrière sans te retenir.", "Utilise ton charisme pour inspirer les autres.", "Journal : « Comment puis-je exprimer pleinement ma lumière dans le monde ? »"]
    ),
    ('leo', 2): make_mc_interp(
        "Lion", 2,
        "Ta vocation de leader s'applique aux ressources — tu crées de la richesse avec panache.",
        "Ta mission publique est liée à la création de valeur avec style et générosité. Tu es fait pour être un entrepreneur de luxe, un artiste qui monétise son talent ou un créateur de marques prestigieuses. Tu transformes ta créativité en prospérité.",
        "On te perçoit comme quelqu'un qui sait vivre et qui gagne bien. Ta réputation est celle d'un professionnel qui allie succès financier et élégance.",
        ["Crée de la richesse avec générosité.", "Montre que le succès peut être généreux.", "Journal : « Comment puis-je créer de la valeur tout en restant généreux ? »"]
    ),
    ('leo', 3): make_mc_interp(
        "Lion", 3,
        "Ta vocation de leader s'exprime dans la communication — tu parles avec éclat.",
        "Ta mission publique passe par une communication charismatique et inspirante. Tu es fait pour être un orateur, un animateur, un leader d'opinion ou un créateur de contenu qui captive. Tes mots ont du poids et de l'éclat.",
        "On te perçoit comme quelqu'un de brillant quand il communique. Ta réputation est celle d'un communicateur qui inspire et qui capte l'attention.",
        ["Communique avec confiance et charisme.", "Utilise ta voix pour inspirer.", "Journal : « Comment puis-je utiliser ma communication pour rayonner ? »"]
    ),
    ('leo', 4): make_mc_interp(
        "Lion", 4,
        "Ta vocation de leader est nourrie par tes racines — tu portes un héritage royal.",
        "Ta mission publique est liée à honorer et perpétuer quelque chose de grand venant de ta famille. Tu es peut-être destiné à reprendre un flambeau familial ou à créer ta propre dynastie. Tu construis ta carrière sur la fierté de tes origines.",
        "On te perçoit comme quelqu'un de noble dans son héritage. Ta réputation est celle d'une personne qui porte dignement son histoire familiale.",
        ["Honore tes racines avec fierté.", "Construis un héritage digne.", "Journal : « Comment mon histoire familiale nourrit-elle ma grandeur ? »"]
    ),
    ('leo', 5): make_mc_interp(
        "Lion", 5,
        "Ta vocation de leader s'épanouit dans la créativité — tu es né pour créer et briller.",
        "Ici, le MC en Lion est dans sa pleine puissance créative. Tu es destiné à être un artiste, un créateur, un performer ou quelqu'un qui exprime sa créativité de façon publique. Tes créations sont une extension de toi-même.",
        "Le monde te voit comme un artiste accompli, quelqu'un de passionné et de talentueux. Ta réputation publique est celle d'un créateur qui met son cœur dans tout ce qu'il fait.",
        ["Crée sans limites.", "Exprime ta passion pleinement.", "Journal : « Comment puis-je manifester ma créativité à son maximum ? »"]
    ),
    ('leo', 6): make_mc_interp(
        "Lion", 6,
        "Ta vocation de leader s'applique au service — tu excelles avec panache.",
        "Ta mission publique passe par un travail quotidien accompli avec excellence et style. Tu es fait pour être le meilleur dans ton domaine, que ce soit la médecine, l'artisanat de luxe ou la gestion de qualité. Tu apportes de la grandeur au travail ordinaire.",
        "On te perçoit comme quelqu'un d'excellent dans ce qu'il fait. Ta réputation est celle d'un professionnel qui élève tout ce qu'il touche.",
        ["Apporte de l'excellence à ton travail quotidien.", "Sois le meilleur avec humilité.", "Journal : « Comment puis-je servir avec excellence ? »"]
    ),
    ('leo', 7): make_mc_interp(
        "Lion", 7,
        "Ta vocation de leader s'accomplit dans le partenariat — tu brilles en équipe.",
        "Ta mission publique passe par des partenariats où tu peux briller et faire briller les autres. Tu es fait pour être un leader d'équipe charismatique, un associé qui apporte l'éclat ou un collaborateur qui inspire.",
        "On te perçoit comme quelqu'un de magnétique en partenariat. Ta réputation est celle d'un collaborateur qui élève l'équipe entière.",
        ["Brille tout en faisant briller les autres.", "Sois le leader généreux.", "Journal : « Comment puis-je inspirer mes partenaires ? »"]
    ),
    ('leo', 8): make_mc_interp(
        "Lion", 8,
        "Ta vocation de leader s'applique aux transformations — tu guides avec courage dans les profondeurs.",
        "Ta mission publique touche aux transformations profondes et aux crises. Tu es fait pour être un leader qui guide à travers les épreuves, un investisseur audacieux ou un thérapeute charismatique. Tu apportes de la lumière dans l'obscurité.",
        "On te perçoit comme quelqu'un de courageux face aux défis. Ta réputation est celle d'un guide qui n'a pas peur des profondeurs.",
        ["Guide les autres à travers les transformations.", "Sois la lumière dans l'obscurité.", "Journal : « Comment puis-je aider les autres à traverser leurs crises avec dignité ? »"]
    ),
    ('leo', 9): make_mc_interp(
        "Lion", 9,
        "Ta vocation de leader s'étend aux horizons — tu enseignes avec charisme.",
        "Ta mission publique est liée à l'enseignement inspirant et à la diffusion de visions grandioses. Tu es fait pour être un professeur charismatique, un guide spirituel rayonnant ou un explorateur qui partage ses aventures avec éclat.",
        "On te perçoit comme un sage inspirant. Ta réputation est celle d'un enseignant ou d'un visionnaire qui captive et élève.",
        ["Enseigne avec passion et charisme.", "Partage ta vision avec générosité.", "Journal : « Comment puis-je inspirer par ma sagesse ? »"]
    ),
    ('leo', 10): make_mc_interp(
        "Lion", 10,
        "Ta vocation de leader est ta destinée absolue — tu es né pour régner.",
        "Le MC en Lion en maison 10 est l'accomplissement suprême de l'énergie léonine. Tu es destiné à occuper une position de pouvoir et de prestige. Que ce soit comme dirigeant, célébrité ou leader dans ton domaine, tu es fait pour être au sommet.",
        "Le monde te voit comme un roi ou une reine dans ton domaine. Ta réputation est celle d'un leader accompli qui a mérité sa place au sommet.",
        ["Assume pleinement ton leadership.", "Règne avec cœur et générosité.", "Journal : « Comment puis-je atteindre mon plein potentiel de leader ? »"]
    ),
    ('leo', 11): make_mc_interp(
        "Lion", 11,
        "Ta vocation de leader sert l'humanité — tu inspires les mouvements collectifs.",
        "Ta mission publique est de mettre ton charisme au service des causes collectives. Tu es fait pour être un leader de mouvement, un porte-parole inspirant ou un créateur qui rassemble les communautés autour de visions partagées.",
        "On te perçoit comme un leader du peuple. Ta réputation est celle d'un inspirateur collectif.",
        ["Mets ton charisme au service du collectif.", "Inspire des mouvements positifs.", "Journal : « Comment puis-je utiliser ma lumière pour l'humanité ? »"]
    ),
    ('leo', 12): make_mc_interp(
        "Lion", 12,
        "Ta vocation de leader opère dans l'invisible — tu brilles dans l'ombre.",
        "Ta mission publique est paradoxalement liée aux coulisses et à l'intériorité. Tu es fait pour être un mentor discret, un créateur qui inspire depuis l'ombre ou un guide spirituel qui illumine sans chercher la gloire.",
        "Le monde ne voit pas toujours ta lumière, mais elle touche les âmes. Ta réputation se fait dans les espaces invisibles.",
        ["Brille dans les coulisses.", "Inspire sans chercher la gloire.", "Journal : « Comment puis-je rayonner de façon discrète mais puissante ? »"]
    ),

    # VIRGO MC
    ('virgo', 1): make_mc_interp(
        "Vierge", 1,
        "Ta vocation est celle de l'expert — tu es appelé à servir avec excellence.",
        "Tu es fait pour être un maître dans ton domaine, quelqu'un dont la compétence est reconnue. Ta carrière idéale te permet d'analyser, d'améliorer et de servir avec précision. Tu excelles dans la santé, l'analyse, l'artisanat de précision ou tout domaine qui demande rigueur et service.",
        "Le monde te voit comme quelqu'un de compétent, de méthodique et de fiable. Ta réputation est celle d'un expert dont le travail est irréprochable. On te respecte pour ta maîtrise technique et ton dévouement.",
        ["Développe ton expertise avec patience.", "Sers avec excellence et humilité.", "Journal : « Comment puis-je atteindre la maîtrise dans mon domaine ? »"]
    ),
    ('virgo', 2): make_mc_interp(
        "Vierge", 2,
        "Ta vocation d'expert s'applique aux ressources — tu crées de la valeur par la qualité.",
        "Ta mission publique est liée à la création de valeur par le travail méticuleux et la qualité. Tu es fait pour être un artisan de précision, un gestionnaire financier rigoureux ou un créateur de produits de qualité supérieure.",
        "On te perçoit comme quelqu'un de prudent et d'avisé avec les ressources. Ta réputation est celle d'un professionnel qui optimise et qui ne gaspille pas.",
        ["Crée de la valeur par la qualité.", "Gère tes ressources avec sagesse.", "Journal : « Comment puis-je transformer mon expertise en prospérité ? »"]
    ),
    ('virgo', 3): make_mc_interp(
        "Vierge", 3,
        "Ta vocation d'expert s'exprime dans la communication — tu informes avec précision.",
        "Ta mission publique passe par une communication claire, précise et utile. Tu es fait pour être un analyste, un éditeur, un enseignant technique ou un communicateur qui rend les choses compréhensibles. Tes mots sont au service de la clarté.",
        "On te perçoit comme quelqu'un de clair et de précis. Ta réputation est celle d'un communicateur fiable dont on peut faire confiance aux informations.",
        ["Communique avec clarté et précision.", "Sois la source d'information fiable.", "Journal : « Comment puis-je servir par ma communication précise ? »"]
    ),
    ('virgo', 4): make_mc_interp(
        "Vierge", 4,
        "Ta vocation d'expert est nourrie par tes racines — tu perfectionnes l'héritage.",
        "Ta mission publique est liée à améliorer et perfectionner ce qui vient de ta famille ou de tes origines. Tu es peut-être destiné à optimiser une entreprise familiale ou à corriger les erreurs du passé.",
        "On te perçoit comme quelqu'un de dévoué à son héritage. Ta réputation est celle d'une personne qui améliore ce qu'on lui transmet.",
        ["Perfectionne ce que tes racines t'ont donné.", "Améliore l'héritage familial.", "Journal : « Comment puis-je améliorer ce qui vient de mon histoire ? »"]
    ),
    ('virgo', 5): make_mc_interp(
        "Vierge", 5,
        "Ta vocation d'expert s'exprime dans la créativité — tu crées avec technique.",
        "Ta mission publique passe par une créativité technique et perfectionnée. Tu es fait pour être un artisan, un designer qui maîtrise chaque détail ou un créateur dont le travail est techniquement parfait.",
        "On te perçoit comme un créateur méticuleux. Ta réputation est celle d'un artiste qui allie talent et technique.",
        ["Crée avec précision et soin.", "Perfectionne ton art.", "Journal : « Comment puis-je allier créativité et technique ? »"]
    ),
    ('virgo', 6): make_mc_interp(
        "Vierge", 6,
        "Ta vocation d'expert est à son apogée — tu es né pour servir avec excellence.",
        "Ici, le MC en Vierge est dans sa pleine puissance en maison 6. Tu es destiné à être un professionnel du service : santé, bien-être, conseil, analyse ou tout domaine où l'excellence technique au service des autres est valorisée.",
        "Le monde te voit exactement comme tu es : un expert dévoué. Ta réputation publique est celle d'un maître dans l'art du service.",
        ["Excelle dans ton service.", "Deviens la référence dans ton domaine.", "Journal : « Comment puis-je manifester ma pleine excellence dans le service ? »"]
    ),
    ('virgo', 7): make_mc_interp(
        "Vierge", 7,
        "Ta vocation d'expert s'accomplit dans le partenariat — tu améliores les collaborations.",
        "Ta mission publique passe par des partenariats où tu apportes ton sens du détail et de l'amélioration. Tu es fait pour être un consultant qui optimise les relations d'affaires ou un collaborateur qui perfectionne les processus.",
        "On te perçoit comme quelqu'un de précieux en partenariat. Ta réputation est celle d'un associé qui améliore tout ce qu'il touche.",
        ["Apporte ton expertise aux partenariats.", "Améliore les collaborations.", "Journal : « Comment puis-je optimiser mes partenariats professionnels ? »"]
    ),
    ('virgo', 8): make_mc_interp(
        "Vierge", 8,
        "Ta vocation d'expert s'applique aux transformations — tu analyses les profondeurs.",
        "Ta mission publique touche à l'analyse des processus profonds. Tu es fait pour être un analyste financier, un thérapeute méthodique ou un chercheur qui décortique les mystères avec rigueur.",
        "On te perçoit comme quelqu'un de capable d'analyser ce qui est complexe. Ta réputation est celle d'un expert des situations délicates.",
        ["Analyse les profondeurs avec rigueur.", "Apporte de la clarté dans le chaos.", "Journal : « Comment puis-je utiliser mon analyse pour aider dans les crises ? »"]
    ),
    ('virgo', 9): make_mc_interp(
        "Vierge", 9,
        "Ta vocation d'expert s'étend aux horizons — tu ancres la sagesse dans le pratique.",
        "Ta mission publique est liée à rendre la connaissance applicable et utile. Tu es fait pour être un enseignant qui rend les théories pratiques, un chercheur rigoureux ou un auteur de guides pratiques.",
        "On te perçoit comme un sage pratique. Ta réputation est celle d'un expert qui sait appliquer les grandes idées.",
        ["Rends la sagesse pratique.", "Enseigne avec rigueur et application.", "Journal : « Comment puis-je rendre les grandes idées utiles ? »"]
    ),
    ('virgo', 10): make_mc_interp(
        "Vierge", 10,
        "Ta vocation d'expert est ta destinée publique — tu es reconnu pour ta maîtrise.",
        "Le MC en Vierge en maison 10 fait de toi un expert public par excellence. Tu es destiné à être reconnu pour ta compétence et ton dévouement. Ta carrière te mène à une position de référence dans ton domaine.",
        "Le monde te voit comme le maître de ton domaine. Ta réputation est celle d'un professionnel dont l'expertise est incontestée.",
        ["Deviens la référence dans ton domaine.", "Construis ta réputation sur ton excellence.", "Journal : « Comment puis-je atteindre la reconnaissance par ma maîtrise ? »"]
    ),
    ('virgo', 11): make_mc_interp(
        "Vierge", 11,
        "Ta vocation d'expert sert l'humanité — tu améliores les systèmes collectifs.",
        "Ta mission publique est de mettre ton expertise au service de l'amélioration collective. Tu es fait pour être un réformateur de systèmes, un optimisateur de processus collectifs ou un conseiller pour des organisations.",
        "On te perçoit comme quelqu'un qui améliore le bien commun. Ta réputation est celle d'un expert au service de la communauté.",
        ["Mets ton expertise au service du collectif.", "Améliore les systèmes pour tous.", "Journal : « Comment puis-je utiliser mon expertise pour l'humanité ? »"]
    ),
    ('virgo', 12): make_mc_interp(
        "Vierge", 12,
        "Ta vocation d'expert opère dans l'invisible — tu soignes ce qui est caché.",
        "Ta mission publique est de mettre ton expertise au service de ce qui est négligé ou caché. Tu es fait pour être un thérapeute des profondeurs, un chercheur de l'inconscient ou un soignant des âmes oubliées.",
        "Le monde ne voit pas toujours ton travail, mais il guérit les profondeurs. Ta réputation se fait dans les espaces invisibles.",
        ["Soigne ce que le monde oublie.", "Analyse les profondeurs cachées.", "Journal : « Comment puis-je servir ce qui est invisible ? »"]
    ),

    # LIBRA MC
    ('libra', 1): make_mc_interp(
        "Balance", 1,
        "Ta vocation est celle du diplomate — tu es appelé à créer l'harmonie.",
        "Tu es fait pour être un créateur d'harmonie dans le monde public. Ta carrière idéale te permet de négocier, d'embellir ou de réconcilier. Tu excelles dans le droit, l'art, la diplomatie ou tout domaine où l'équilibre et la beauté sont valorisés.",
        "Le monde te voit comme quelqu'un d'élégant, de juste et de conciliant. Ta réputation est celle d'un professionnel qui sait créer l'harmonie et la beauté dans tout ce qu'il touche.",
        ["Crée de l'harmonie dans ta carrière.", "Utilise ton sens de la justice.", "Journal : « Comment puis-je apporter plus d'équilibre dans le monde ? »"]
    ),
    ('libra', 2): make_mc_interp(
        "Balance", 2,
        "Ta vocation de diplomate s'applique aux ressources — tu crées de la valeur par la beauté.",
        "Ta mission publique est liée à la création de valeur par l'esthétique et l'harmonie. Tu es fait pour être dans le luxe, l'art, le design ou tout domaine où la beauté génère de la richesse.",
        "On te perçoit comme quelqu'un qui a du goût et qui sait créer du beau. Ta réputation est celle d'un professionnel qui allie esthétique et prospérité.",
        ["Crée de la richesse par la beauté.", "Équilibre esthétique et finances.", "Journal : « Comment puis-je transformer mon sens de la beauté en prospérité ? »"]
    ),
    ('libra', 3): make_mc_interp(
        "Balance", 3,
        "Ta vocation de diplomate s'exprime dans la communication — tu parles avec grâce.",
        "Ta mission publique passe par une communication harmonieuse et équilibrée. Tu es fait pour être un négociateur, un médiateur ou un communicateur qui réconcilie les perspectives. Tes mots créent des ponts.",
        "On te perçoit comme quelqu'un de diplomate et d'agréable. Ta réputation est celle d'un communicateur qui sait dire les choses avec tact.",
        ["Communique avec grâce et équilibre.", "Sois le médiateur des mots.", "Journal : « Comment puis-je utiliser ma communication pour créer l'harmonie ? »"]
    ),
    ('libra', 4): make_mc_interp(
        "Balance", 4,
        "Ta vocation de diplomate est nourrie par tes racines — tu harmonises l'héritage.",
        "Ta mission publique est liée à créer l'harmonie dans ou à partir de ta famille. Tu es peut-être destiné à réconcilier des conflits familiaux ou à créer un foyer qui rayonne d'équilibre.",
        "On te perçoit comme quelqu'un d'équilibré dans ses racines. Ta réputation est celle d'une personne qui crée l'harmonie familiale.",
        ["Crée l'harmonie dans tes racines.", "Équilibre l'héritage familial.", "Journal : « Comment puis-je apporter l'équilibre à mon histoire familiale ? »"]
    ),
    ('libra', 5): make_mc_interp(
        "Balance", 5,
        "Ta vocation de diplomate s'exprime dans la créativité — tu crées de la beauté.",
        "Ta mission publique passe par la création artistique et l'expression de la beauté. Tu es fait pour être un artiste, un designer ou un créateur qui apporte l'harmonie visuelle au monde.",
        "On te perçoit comme un créateur esthète. Ta réputation est celle d'un artiste qui a le sens de l'équilibre et de la beauté.",
        ["Crée de la beauté pour le monde.", "Exprime l'harmonie par l'art.", "Journal : « Comment puis-je exprimer la beauté dans mes créations ? »"]
    ),
    ('libra', 6): make_mc_interp(
        "Balance", 6,
        "Ta vocation de diplomate s'applique au service — tu harmonises le quotidien.",
        "Ta mission publique passe par l'amélioration de l'équilibre dans le travail quotidien. Tu es fait pour être un conseiller en ergonomie, un designer d'espaces de travail ou un professionnel qui rend le quotidien plus harmonieux.",
        "On te perçoit comme quelqu'un qui apporte de l'équilibre au travail. Ta réputation est celle d'un professionnel qui harmonise.",
        ["Apporte de l'harmonie au travail quotidien.", "Équilibre les environnements.", "Journal : « Comment puis-je rendre le quotidien plus harmonieux ? »"]
    ),
    ('libra', 7): make_mc_interp(
        "Balance", 7,
        "Ta vocation de diplomate est à son apogée — tu es né pour le partenariat.",
        "Ici, le MC en Balance est dans sa pleine puissance en maison 7. Tu es destiné à exceller dans les partenariats : avocat, conseiller conjugal, négociateur ou tout professionnel de la relation. Les associations sont ta voie.",
        "Le monde te voit exactement comme tu es : un expert des relations. Ta réputation publique est celle d'un maître de la collaboration et de la négociation.",
        ["Excelle dans l'art du partenariat.", "Deviens la référence en collaboration.", "Journal : « Comment puis-je manifester ma pleine puissance dans les partenariats ? »"]
    ),
    ('libra', 8): make_mc_interp(
        "Balance", 8,
        "Ta vocation de diplomate s'applique aux transformations — tu réconcilies dans les profondeurs.",
        "Ta mission publique touche à la réconciliation dans les moments de crise. Tu es fait pour être un médiateur de conflits profonds, un avocat en divorce ou un conseiller en fusions-acquisitions.",
        "On te perçoit comme quelqu'un de capable de créer l'harmonie même dans le chaos. Ta réputation est celle d'un diplomate des situations difficiles.",
        ["Réconcilie dans les moments de crise.", "Apporte l'équilibre aux transformations.", "Journal : « Comment puis-je créer l'harmonie dans les profondeurs ? »"]
    ),
    ('libra', 9): make_mc_interp(
        "Balance", 9,
        "Ta vocation de diplomate s'étend aux horizons — tu réconcilies les cultures.",
        "Ta mission publique est liée à créer des ponts entre différentes cultures, philosophies ou systèmes de pensée. Tu es fait pour être un diplomate international, un philosophe de la justice ou un éducateur interculturel.",
        "On te perçoit comme un sage équilibré. Ta réputation est celle d'un pont entre les mondes.",
        ["Crée des ponts entre les cultures.", "Enseigne l'équilibre entre les perspectives.", "Journal : « Comment puis-je réconcilier les différentes visions du monde ? »"]
    ),
    ('libra', 10): make_mc_interp(
        "Balance", 10,
        "Ta vocation de diplomate est ta destinée publique — tu es reconnu pour ton équilibre.",
        "Le MC en Balance en maison 10 fait de toi un diplomate public par excellence. Tu es destiné à être reconnu pour ton sens de la justice, de l'équilibre et de la beauté. Ta carrière te mène à une position de médiateur ou d'esthète.",
        "Le monde te voit comme l'incarnation de l'équilibre. Ta réputation est celle d'un professionnel juste et élégant.",
        ["Deviens reconnu pour ton équilibre.", "Construis ta réputation sur la justice.", "Journal : « Comment puis-je atteindre le sommet par mon sens de l'harmonie ? »"]
    ),
    ('libra', 11): make_mc_interp(
        "Balance", 11,
        "Ta vocation de diplomate sert l'humanité — tu crées l'harmonie collective.",
        "Ta mission publique est de mettre ton sens de l'équilibre au service de la justice sociale. Tu es fait pour être un médiateur de conflits collectifs, un avocat des droits ou un créateur d'harmonie communautaire.",
        "On te perçoit comme un artisan de la paix collective. Ta réputation est celle d'un diplomate humanitaire.",
        ["Mets ton équilibre au service du collectif.", "Crée l'harmonie sociale.", "Journal : « Comment puis-je apporter la justice à l'humanité ? »"]
    ),
    ('libra', 12): make_mc_interp(
        "Balance", 12,
        "Ta vocation de diplomate opère dans l'invisible — tu réconcilies ce qui est caché.",
        "Ta mission publique est de créer l'harmonie dans les espaces invisibles. Tu es fait pour être un thérapeute qui réconcilie les parts d'ombre, un médiateur de l'inconscient ou un artiste qui harmonise l'indicible.",
        "Le monde ne voit pas toujours ton travail d'équilibre, mais il touche les profondeurs. Ta réputation se fait dans les espaces subtils.",
        ["Réconcilie les ombres.", "Crée l'harmonie dans l'invisible.", "Journal : « Comment puis-je apporter l'équilibre aux espaces cachés ? »"]
    ),

    # SCORPIO MC
    ('scorpio', 1): make_mc_interp(
        "Scorpion", 1,
        "Ta vocation est celle du transformateur — tu es appelé à régénérer et à révéler.",
        "Tu es fait pour être un agent de transformation dans le monde. Ta carrière idéale te permet d'enquêter, de transformer ou de guérir en profondeur. Tu excelles dans la psychologie, la recherche, la finance de crise ou tout domaine qui touche aux puissances cachées.",
        "Le monde te voit comme quelqu'un d'intense, de puissant et de capable de gérer les situations difficiles. Ta réputation est celle d'un professionnel qui n'a pas peur d'aller là où les autres n'osent pas.",
        ["Embrasse ton pouvoir de transformation.", "Utilise ton intensité pour guérir.", "Journal : « Comment puis-je transformer le monde par mon travail ? »"]
    ),
    ('scorpio', 2): make_mc_interp(
        "Scorpion", 2,
        "Ta vocation de transformateur s'applique aux ressources — tu régénères la richesse.",
        "Ta mission publique est liée à la transformation des ressources et de la valeur. Tu es fait pour être un investisseur qui redresse les situations, un gestionnaire de patrimoine en crise ou un expert en restructuration financière.",
        "On te perçoit comme quelqu'un de puissant avec l'argent. Ta réputation est celle d'un professionnel qui peut transformer les finances même les plus compromises.",
        ["Transforme et régénère les ressources.", "Sois le phénix financier.", "Journal : « Comment puis-je transformer les ressources par mon expertise ? »"]
    ),
    ('scorpio', 3): make_mc_interp(
        "Scorpion", 3,
        "Ta vocation de transformateur s'exprime dans la communication — tu révèles ce qui est caché.",
        "Ta mission publique passe par une communication qui va en profondeur. Tu es fait pour être un journaliste d'investigation, un psychanalyste ou un communicateur qui ose parler de ce que les autres taisent.",
        "On te perçoit comme quelqu'un qui dit les vérités profondes. Ta réputation est celle d'un communicateur qui n'a pas peur des sujets tabous.",
        ["Communique les vérités profondes.", "Révèle ce qui est caché.", "Journal : « Comment puis-je utiliser mes mots pour transformer ? »"]
    ),
    ('scorpio', 4): make_mc_interp(
        "Scorpion", 4,
        "Ta vocation de transformateur est nourrie par tes racines — tu guéris l'héritage.",
        "Ta mission publique est liée à la transformation et la guérison de ton histoire familiale. Tu es peut-être destiné à briser des cycles familiaux dysfonctionnels ou à transformer des héritages lourds.",
        "On te perçoit comme quelqu'un qui porte une transformation familiale. Ta réputation est celle d'une personne qui transmute son passé.",
        ["Transforme ton héritage familial.", "Guéris les blessures ancestrales.", "Journal : « Comment puis-je transformer ce qui vient de mes racines ? »"]
    ),
    ('scorpio', 5): make_mc_interp(
        "Scorpion", 5,
        "Ta vocation de transformateur s'exprime dans la créativité — tu crées du profond.",
        "Ta mission publique passe par une créativité intense et transformatrice. Tu es fait pour être un artiste qui explore les profondeurs, un créateur qui touche les tabous ou un performer qui transforme son public.",
        "On te perçoit comme un créateur intense. Ta réputation est celle d'un artiste qui n'a pas peur d'aller dans les ombres.",
        ["Crée depuis les profondeurs.", "Exprime l'intensité par l'art.", "Journal : « Comment puis-je transformer par ma créativité ? »"]
    ),
    ('scorpio', 6): make_mc_interp(
        "Scorpion", 6,
        "Ta vocation de transformateur s'applique au service — tu guéris en profondeur.",
        "Ta mission publique passe par un travail quotidien de transformation et de guérison. Tu es fait pour être un thérapeute, un médecin spécialisé dans les cas difficiles ou un professionnel qui résout les crises quotidiennes.",
        "On te perçoit comme quelqu'un qui guérit vraiment. Ta réputation est celle d'un professionnel qui va à la racine des problèmes.",
        ["Guéris en allant à la racine.", "Transforme par ton travail quotidien.", "Journal : « Comment puis-je servir en transformant vraiment ? »"]
    ),
    ('scorpio', 7): make_mc_interp(
        "Scorpion", 7,
        "Ta vocation de transformateur s'accomplit dans le partenariat — tu transformes les relations.",
        "Ta mission publique passe par des partenariats transformateurs. Tu es fait pour être un thérapeute de couple, un avocat en divorce ou un consultant qui transforme les dynamiques relationnelles.",
        "On te perçoit comme quelqu'un de puissant en partenariat. Ta réputation est celle d'un professionnel qui transforme les relations.",
        ["Transforme les partenariats.", "Guéris les dynamiques relationnelles.", "Journal : « Comment puis-je transformer les relations par mon travail ? »"]
    ),
    ('scorpio', 8): make_mc_interp(
        "Scorpion", 8,
        "Ta vocation de transformateur est à son apogée — tu es né pour les profondeurs.",
        "Ici, le MC en Scorpion est dans sa pleine puissance en maison 8. Tu es destiné à travailler avec les forces profondes : mort, renaissance, sexualité, finances partagées, crises. Tu es le phénix professionnel.",
        "Le monde te voit exactement comme tu es : un maître de la transformation. Ta réputation publique est celle d'un expert des profondeurs.",
        ["Excelle dans les transformations profondes.", "Deviens le maître de la renaissance.", "Journal : « Comment puis-je manifester ma pleine puissance transformatrice ? »"]
    ),
    ('scorpio', 9): make_mc_interp(
        "Scorpion", 9,
        "Ta vocation de transformateur s'étend aux horizons — tu transformes les croyances.",
        "Ta mission publique est liée à la transformation des systèmes de croyances et des philosophies. Tu es fait pour être un enseignant de sagesse profonde, un chercheur de vérités occultes ou un guide spirituel transformateur.",
        "On te perçoit comme un sage des profondeurs. Ta réputation est celle d'un transformateur de consciences.",
        ["Transforme les croyances limitantes.", "Enseigne la sagesse des profondeurs.", "Journal : « Comment puis-je transformer les visions du monde ? »"]
    ),
    ('scorpio', 10): make_mc_interp(
        "Scorpion", 10,
        "Ta vocation de transformateur est ta destinée publique — tu es reconnu pour ton pouvoir.",
        "Le MC en Scorpion en maison 10 fait de toi un transformateur public par excellence. Tu es destiné à être reconnu pour ton pouvoir de changement. Ta carrière te mène à une position de pouvoir transformateur.",
        "Le monde te voit comme une force de transformation. Ta réputation est celle d'un professionnel puissant qui change ce qu'il touche.",
        ["Deviens reconnu pour ton pouvoir de transformation.", "Utilise ton influence pour le bien.", "Journal : « Comment puis-je atteindre le sommet par mon pouvoir de changement ? »"]
    ),
    ('scorpio', 11): make_mc_interp(
        "Scorpion", 11,
        "Ta vocation de transformateur sert l'humanité — tu transformes les collectifs.",
        "Ta mission publique est de mettre ton pouvoir de transformation au service du changement collectif. Tu es fait pour être un réformateur social, un leader de mouvements de transformation ou un agent de changement systémique.",
        "On te perçoit comme un transformateur du collectif. Ta réputation est celle d'un agent de changement profond.",
        ["Transforme les systèmes collectifs.", "Sois l'agent du changement social.", "Journal : « Comment puis-je transformer l'humanité ? »"]
    ),
    ('scorpio', 12): make_mc_interp(
        "Scorpion", 12,
        "Ta vocation de transformateur opère dans l'invisible — tu guéris l'inconscient collectif.",
        "Ta mission publique est de transformer ce qui est caché dans l'âme collective. Tu es fait pour être un guérisseur des profondeurs, un explorateur de l'inconscient ou un thérapeute qui travaille avec les ombres.",
        "Le monde ne voit pas toujours ton travail de transformation, mais il touche les racines. Ta réputation se fait dans les espaces invisibles.",
        ["Transforme les ombres collectives.", "Guéris l'inconscient.", "Journal : « Comment puis-je transformer ce qui est caché ? »"]
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
