#!/usr/bin/env python3
"""
Insert MC (Midheaven) interpretations for Sagittarius, Capricorn, Aquarius, Pisces (48 entries)
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
    # SAGITTARIUS MC
    ('sagittarius', 1): make_mc_interp(
        "Sagittaire", 1,
        "Ta vocation est celle de l'explorateur — tu es appelé à élargir les horizons.",
        "Tu es fait pour être un visionnaire, quelqu'un qui explore et qui enseigne. Ta carrière idéale te permet de voyager, d'apprendre, d'enseigner ou de publier. Tu excelles dans l'éducation supérieure, l'édition, le tourisme ou tout domaine qui élargit les perspectives.",
        "Le monde te voit comme quelqu'un d'optimiste, de sage et d'aventurier. Ta réputation est celle d'un professionnel qui voit grand et qui inspire les autres à élargir leurs horizons.",
        ["Explore de nouveaux horizons dans ta carrière.", "Enseigne ce que tu as appris.", "Journal : « Comment puis-je élargir les horizons du monde ? »"]
    ),
    ('sagittarius', 2): make_mc_interp(
        "Sagittaire", 2,
        "Ta vocation d'explorateur s'applique aux ressources — tu crées de l'abondance par l'expansion.",
        "Ta mission publique est liée à la création de richesse par l'expansion et l'optimisme. Tu es fait pour être un entrepreneur international, un éditeur prospère ou un créateur de contenus éducatifs rentables.",
        "On te perçoit comme quelqu'un de généreux et d'expansif avec les ressources. Ta réputation est celle d'un professionnel qui voit l'abondance partout.",
        ["Crée de la richesse en élargissant les horizons.", "Sois généreux dans ta prospérité.", "Journal : « Comment puis-je transformer ma vision en abondance ? »"]
    ),
    ('sagittarius', 3): make_mc_interp(
        "Sagittaire", 3,
        "Ta vocation d'explorateur s'exprime dans la communication — tu diffuses la sagesse.",
        "Ta mission publique passe par la communication de grandes idées. Tu es fait pour être un auteur, un conférencier, un podcaster ou un communicateur qui inspire par sa vision. Tes mots ouvrent des mondes.",
        "On te perçoit comme quelqu'un d'inspirant dans sa communication. Ta réputation est celle d'un communicateur visionnaire.",
        ["Communique tes grandes idées.", "Inspire par tes mots.", "Journal : « Comment puis-je diffuser la sagesse par ma communication ? »"]
    ),
    ('sagittarius', 4): make_mc_interp(
        "Sagittaire", 4,
        "Ta vocation d'explorateur est nourrie par tes racines — tu portes une sagesse ancestrale.",
        "Ta mission publique est liée à la transmission de sagesse venant de tes origines. Tu es peut-être destiné à enseigner les traditions familiales ou à porter un héritage philosophique ou culturel.",
        "On te perçoit comme quelqu'un de sage dans ses racines. Ta réputation est celle d'une personne qui transmet une sagesse héritée.",
        ["Transmets la sagesse de tes racines.", "Honore l'héritage philosophique.", "Journal : « Quelle sagesse familiale suis-je appelé à partager ? »"]
    ),
    ('sagittarius', 5): make_mc_interp(
        "Sagittaire", 5,
        "Ta vocation d'explorateur s'exprime dans la créativité — tu crées avec vision.",
        "Ta mission publique passe par une créativité qui inspire et qui élargit. Tu es fait pour être un artiste visionnaire, un créateur de contenus inspirants ou un performer qui transporte son public vers de nouveaux horizons.",
        "On te perçoit comme un créateur inspirant. Ta réputation est celle d'un artiste qui voit grand.",
        ["Crée avec une vision large.", "Inspire par ton art.", "Journal : « Comment puis-je exprimer ma créativité de façon visionnaire ? »"]
    ),
    ('sagittarius', 6): make_mc_interp(
        "Sagittaire", 6,
        "Ta vocation d'explorateur s'applique au service — tu apportes du sens au quotidien.",
        "Ta mission publique passe par un travail quotidien qui a du sens et de l'envergure. Tu es fait pour être un formateur, un conseiller en développement ou un professionnel de santé holistique. Tu apportes une vision large au travail quotidien.",
        "On te perçoit comme quelqu'un qui donne du sens. Ta réputation est celle d'un professionnel qui élève le quotidien.",
        ["Apporte du sens au travail quotidien.", "Élargis les perspectives de service.", "Journal : « Comment puis-je donner plus de sens à mon service ? »"]
    ),
    ('sagittarius', 7): make_mc_interp(
        "Sagittaire", 7,
        "Ta vocation d'explorateur s'accomplit dans le partenariat — tu crées des alliances internationales.",
        "Ta mission publique passe par des partenariats qui élargissent les horizons. Tu es fait pour être un consultant international, un avocat en droit international ou un collaborateur qui apporte une vision globale.",
        "On te perçoit comme quelqu'un d'ouvert en partenariat. Ta réputation est celle d'un collaborateur qui élargit les perspectives.",
        ["Crée des partenariats qui élargissent.", "Collabore avec une vision globale.", "Journal : « Comment puis-je élargir mes partenariats ? »"]
    ),
    ('sagittarius', 8): make_mc_interp(
        "Sagittaire", 8,
        "Ta vocation d'explorateur s'applique aux transformations — tu trouves le sens dans les crises.",
        "Ta mission publique touche à donner du sens aux transformations profondes. Tu es fait pour être un philosophe de la mort et de la renaissance, un conseiller qui aide à trouver le sens des épreuves ou un gestionnaire de crise avec vision.",
        "On te perçoit comme quelqu'un qui trouve de la sagesse dans l'adversité. Ta réputation est celle d'un guide dans les moments de transformation.",
        ["Trouve le sens dans les transformations.", "Guide avec sagesse dans les crises.", "Journal : « Comment puis-je aider les autres à trouver le sens dans leurs épreuves ? »"]
    ),
    ('sagittarius', 9): make_mc_interp(
        "Sagittaire", 9,
        "Ta vocation d'explorateur est à son apogée — tu es né pour enseigner et explorer.",
        "Ici, le MC en Sagittaire est dans sa pleine puissance en maison 9. Tu es destiné à être un enseignant, un explorateur ou un éditeur. Les voyages, la philosophie et l'éducation supérieure sont ta voie naturelle.",
        "Le monde te voit exactement comme tu es : un sage et un explorateur. Ta réputation publique est celle d'un maître de la sagesse et de l'aventure.",
        ["Excelle dans l'enseignement et l'exploration.", "Deviens la référence en sagesse.", "Journal : « Comment puis-je manifester ma pleine vocation d'explorateur ? »"]
    ),
    ('sagittarius', 10): make_mc_interp(
        "Sagittaire", 10,
        "Ta vocation d'explorateur est ta destinée publique — tu es reconnu pour ta vision.",
        "Le MC en Sagittaire en maison 10 fait de toi un visionnaire public par excellence. Tu es destiné à être reconnu pour ton optimisme et ta sagesse. Ta carrière te mène à une position d'influence philosophique ou éducative.",
        "Le monde te voit comme un sage au sommet. Ta réputation est celle d'un professionnel qui inspire par sa vision.",
        ["Deviens reconnu pour ta sagesse.", "Utilise ta position pour enseigner.", "Journal : « Comment puis-je atteindre le sommet par ma vision ? »"]
    ),
    ('sagittarius', 11): make_mc_interp(
        "Sagittaire", 11,
        "Ta vocation d'explorateur sert l'humanité — tu élargis les horizons collectifs.",
        "Ta mission publique est d'élargir les perspectives de l'humanité. Tu es fait pour être un leader de mouvements progressistes, un éducateur des masses ou un visionnaire qui pousse la société vers de nouveaux horizons.",
        "On te perçoit comme un visionnaire collectif. Ta réputation est celle d'un élargisseur d'horizons pour tous.",
        ["Élargis les horizons de l'humanité.", "Enseigne la vision collective.", "Journal : « Comment puis-je aider l'humanité à voir plus grand ? »"]
    ),
    ('sagittarius', 12): make_mc_interp(
        "Sagittaire", 12,
        "Ta vocation d'explorateur opère dans l'invisible — tu explores les dimensions spirituelles.",
        "Ta mission publique est d'explorer et d'enseigner les réalités invisibles. Tu es fait pour être un guide spirituel, un enseignant de sagesse ésotérique ou un explorateur des dimensions cachées de l'existence.",
        "Le monde ne voit pas toujours tes explorations, mais elles touchent l'âme. Ta réputation se fait dans les espaces spirituels.",
        ["Explore les dimensions invisibles.", "Enseigne la sagesse spirituelle.", "Journal : « Comment puis-je explorer les horizons invisibles ? »"]
    ),

    # CAPRICORN MC
    ('capricorn', 1): make_mc_interp(
        "Capricorne", 1,
        "Ta vocation est celle du bâtisseur d'empire — tu es appelé à construire et à diriger.",
        "Tu es fait pour atteindre le sommet de ta profession. Ta carrière idéale te permet de construire, de diriger et de laisser un héritage. Tu excelles dans la direction d'entreprise, la politique, l'administration ou tout domaine qui demande persévérance et ambition.",
        "Le monde te voit comme quelqu'un de compétent, d'ambitieux et de fiable. Ta réputation est celle d'un professionnel sérieux qui atteint ses objectifs avec détermination.",
        ["Construis ta carrière avec patience.", "Vise le sommet avec intégrité.", "Journal : « Comment puis-je construire un héritage durable ? »"]
    ),
    ('capricorn', 2): make_mc_interp(
        "Capricorne", 2,
        "Ta vocation de bâtisseur s'applique aux ressources — tu construis la richesse sur la durée.",
        "Ta mission publique est liée à la construction de richesse durable et structurée. Tu es fait pour être un gestionnaire de patrimoine, un investisseur à long terme ou un entrepreneur qui construit des actifs solides.",
        "On te perçoit comme quelqu'un de prudent et de compétent avec l'argent. Ta réputation est celle d'un professionnel qui construit la richesse de façon responsable.",
        ["Construis la richesse progressivement.", "Investis pour le long terme.", "Journal : « Comment puis-je bâtir une prospérité durable ? »"]
    ),
    ('capricorn', 3): make_mc_interp(
        "Capricorne", 3,
        "Ta vocation de bâtisseur s'exprime dans la communication — tu structures les idées.",
        "Ta mission publique passe par une communication structurée et faisant autorité. Tu es fait pour être un auteur de référence, un conférencier d'expertise ou un communicateur dont les mots ont du poids.",
        "On te perçoit comme quelqu'un d'autoritaire dans sa communication. Ta réputation est celle d'un communicateur dont on respecte les paroles.",
        ["Communique avec autorité et structure.", "Deviens une voix de référence.", "Journal : « Comment puis-je donner du poids à ma communication ? »"]
    ),
    ('capricorn', 4): make_mc_interp(
        "Capricorne", 4,
        "Ta vocation de bâtisseur est nourrie par tes racines — tu honores un héritage de responsabilité.",
        "Ta mission publique est liée à perpétuer ou à construire une tradition familiale. Tu es peut-être destiné à reprendre une entreprise familiale ou à bâtir quelque chose qui honore tes ancêtres.",
        "On te perçoit comme quelqu'un de responsable envers son héritage. Ta réputation est celle d'une personne qui construit sur des fondations solides.",
        ["Construis sur les fondations de tes ancêtres.", "Honore ton héritage avec responsabilité.", "Journal : « Comment puis-je construire sur l'héritage familial ? »"]
    ),
    ('capricorn', 5): make_mc_interp(
        "Capricorne", 5,
        "Ta vocation de bâtisseur s'exprime dans la créativité — tu crées avec discipline.",
        "Ta mission publique passe par une créativité structurée et professionnelle. Tu es fait pour être un artiste qui maîtrise son art, un créateur de contenus de qualité ou un entrepreneur créatif qui construit des marques durables.",
        "On te perçoit comme un créateur sérieux. Ta réputation est celle d'un artiste professionnel et respecté.",
        ["Crée avec discipline et professionnalisme.", "Construis une œuvre qui dure.", "Journal : « Comment puis-je professionnaliser ma créativité ? »"]
    ),
    ('capricorn', 6): make_mc_interp(
        "Capricorne", 6,
        "Ta vocation de bâtisseur s'applique au service — tu excelles par la rigueur.",
        "Ta mission publique passe par un travail quotidien accompli avec excellence et rigueur. Tu es fait pour être un expert reconnu dans ton domaine, un professionnel de santé respecté ou un gestionnaire d'exception.",
        "On te perçoit comme quelqu'un d'ultra-compétent. Ta réputation est celle d'un professionnel qui ne fait pas d'erreurs.",
        ["Excelle par ta rigueur professionnelle.", "Deviens la référence dans ton domaine.", "Journal : « Comment puis-je atteindre l'excellence dans mon service ? »"]
    ),
    ('capricorn', 7): make_mc_interp(
        "Capricorne", 7,
        "Ta vocation de bâtisseur s'accomplit dans le partenariat — tu construis des alliances stratégiques.",
        "Ta mission publique passe par des partenariats solides et stratégiques. Tu es fait pour être un associé fiable, un conseiller en fusions-acquisitions ou un professionnel qui construit des relations d'affaires durables.",
        "On te perçoit comme quelqu'un de sérieux en partenariat. Ta réputation est celle d'un collaborateur sur qui on peut compter.",
        ["Construis des partenariats stratégiques.", "Sois le pilier de tes collaborations.", "Journal : « Comment puis-je bâtir des partenariats durables ? »"]
    ),
    ('capricorn', 8): make_mc_interp(
        "Capricorne", 8,
        "Ta vocation de bâtisseur s'applique aux transformations — tu restructures ce qui est en crise.",
        "Ta mission publique touche à la restructuration et à la gestion de crise. Tu es fait pour être un redresseur d'entreprises, un gestionnaire de patrimoine en succession ou un expert qui construit à partir des ruines.",
        "On te perçoit comme quelqu'un de capable dans les situations difficiles. Ta réputation est celle d'un bâtisseur qui peut reconstruire n'importe quoi.",
        ["Restructure ce qui est en crise.", "Construis à partir des ruines.", "Journal : « Comment puis-je aider à reconstruire après les crises ? »"]
    ),
    ('capricorn', 9): make_mc_interp(
        "Capricorne", 9,
        "Ta vocation de bâtisseur s'étend aux horizons — tu structures la sagesse.",
        "Ta mission publique est liée à structurer et institutionnaliser les connaissances. Tu es fait pour être un fondateur d'institution éducative, un auteur de référence ou un expert qui donne forme aux grandes idées.",
        "On te perçoit comme un sage structuré. Ta réputation est celle d'un bâtisseur de systèmes de connaissance.",
        ["Structure la sagesse pour la transmettre.", "Construis des institutions de savoir.", "Journal : « Comment puis-je institutionnaliser la connaissance ? »"]
    ),
    ('capricorn', 10): make_mc_interp(
        "Capricorne", 10,
        "Ta vocation de bâtisseur est à son apogée — tu es né pour le sommet.",
        "Ici, le MC en Capricorne est dans sa pleine puissance en maison 10. Tu es destiné à atteindre les plus hautes positions dans ton domaine. PDG, dirigeant politique, autorité reconnue — le sommet t'attend.",
        "Le monde te voit exactement comme tu es : un leader né, un bâtisseur d'empire. Ta réputation publique est celle d'un maître dans ton domaine.",
        ["Atteins le sommet avec intégrité.", "Deviens l'autorité dans ton domaine.", "Journal : « Comment puis-je manifester ma pleine puissance de bâtisseur ? »"]
    ),
    ('capricorn', 11): make_mc_interp(
        "Capricorne", 11,
        "Ta vocation de bâtisseur sert l'humanité — tu structures les mouvements collectifs.",
        "Ta mission publique est de mettre ta capacité de construction au service du collectif. Tu es fait pour être un fondateur d'organisations, un structureur de mouvements ou un bâtisseur de systèmes qui servent l'humanité.",
        "On te perçoit comme un bâtisseur pour le bien commun. Ta réputation est celle d'un constructeur de structures collectives.",
        ["Construis des organisations pour le bien commun.", "Structure les mouvements collectifs.", "Journal : « Comment puis-je construire pour l'humanité ? »"]
    ),
    ('capricorn', 12): make_mc_interp(
        "Capricorne", 12,
        "Ta vocation de bâtisseur opère dans l'invisible — tu structures ce qui est caché.",
        "Ta mission publique est de donner structure aux espaces invisibles. Tu es fait pour être un fondateur d'institutions spirituelles, un organisateur de retraites ou un constructeur de refuges pour l'âme.",
        "Le monde ne voit pas toujours ce que tu construis, mais tes structures soutiennent l'invisible. Ta réputation se fait dans les espaces profonds.",
        ["Structure les espaces invisibles.", "Construis des fondations pour l'âme.", "Journal : « Comment puis-je bâtir dans les dimensions cachées ? »"]
    ),

    # AQUARIUS MC
    ('aquarius', 1): make_mc_interp(
        "Verseau", 1,
        "Ta vocation est celle du révolutionnaire — tu es appelé à innover et à libérer.",
        "Tu es fait pour être un innovateur, un pionnier du futur. Ta carrière idéale te permet d'innover, de révolutionner ou de libérer. Tu excelles dans la technologie, les sciences, l'humanitaire ou tout domaine qui brise les conventions.",
        "Le monde te voit comme quelqu'un d'original, de visionnaire et d'avant-gardiste. Ta réputation est celle d'un professionnel qui pense différemment et qui n'a pas peur de bousculer le statu quo.",
        ["Innove sans crainte du jugement.", "Libère par ton originalité.", "Journal : « Comment puis-je révolutionner mon domaine ? »"]
    ),
    ('aquarius', 2): make_mc_interp(
        "Verseau", 2,
        "Ta vocation de révolutionnaire s'applique aux ressources — tu crées de la valeur par l'innovation.",
        "Ta mission publique est liée à la création de valeur par des moyens non conventionnels. Tu es fait pour être un entrepreneur technologique, un investisseur en startups ou un créateur de nouveaux modèles économiques.",
        "On te perçoit comme quelqu'un d'innovant avec les ressources. Ta réputation est celle d'un professionnel qui trouve de nouvelles façons de créer de la valeur.",
        ["Innove dans ta façon de créer de la valeur.", "Révolutionne les modèles financiers.", "Journal : « Comment puis-je créer de la richesse de façon innovante ? »"]
    ),
    ('aquarius', 3): make_mc_interp(
        "Verseau", 3,
        "Ta vocation de révolutionnaire s'exprime dans la communication — tu diffuses des idées nouvelles.",
        "Ta mission publique passe par la communication d'idées révolutionnaires. Tu es fait pour être un influenceur d'idées, un communicateur technologique ou un porte-parole de visions futuristes.",
        "On te perçoit comme quelqu'un d'avant-gardiste dans sa communication. Ta réputation est celle d'un communicateur qui fait avancer la pensée.",
        ["Communique les idées du futur.", "Révolutionne par tes mots.", "Journal : « Comment puis-je diffuser des idées qui changent le monde ? »"]
    ),
    ('aquarius', 4): make_mc_interp(
        "Verseau", 4,
        "Ta vocation de révolutionnaire est nourrie par tes racines — tu libères l'héritage.",
        "Ta mission publique est liée à révolutionner ou libérer quelque chose de ton passé familial. Tu es peut-être destiné à briser des cycles familiaux ou à moderniser un héritage.",
        "On te perçoit comme quelqu'un qui réinvente ses racines. Ta réputation est celle d'une personne qui libère son héritage des contraintes du passé.",
        ["Libère ton héritage des anciennes contraintes.", "Révolutionne les traditions familiales.", "Journal : « Comment puis-je moderniser ce qui vient de mes racines ? »"]
    ),
    ('aquarius', 5): make_mc_interp(
        "Verseau", 5,
        "Ta vocation de révolutionnaire s'exprime dans la créativité — tu crées l'inattendu.",
        "Ta mission publique passe par une créativité qui brise les conventions. Tu es fait pour être un artiste d'avant-garde, un créateur de tendances ou un innovateur qui surprend par son originalité.",
        "On te perçoit comme un créateur unique. Ta réputation est celle d'un artiste qui n'entre dans aucune case.",
        ["Crée sans suivre les règles.", "Exprime ton unicité artistique.", "Journal : « Comment puis-je créer de façon véritablement originale ? »"]
    ),
    ('aquarius', 6): make_mc_interp(
        "Verseau", 6,
        "Ta vocation de révolutionnaire s'applique au service — tu optimises par l'innovation.",
        "Ta mission publique passe par la révolution des méthodes de travail et de santé. Tu es fait pour être un innovateur en bien-être, un automatiseur de processus ou un créateur de nouvelles façons de servir.",
        "On te perçoit comme quelqu'un qui modernise le travail. Ta réputation est celle d'un professionnel qui trouve des solutions nouvelles.",
        ["Révolutionne les méthodes de travail.", "Innove dans le service.", "Journal : « Comment puis-je moderniser la façon de servir ? »"]
    ),
    ('aquarius', 7): make_mc_interp(
        "Verseau", 7,
        "Ta vocation de révolutionnaire s'accomplit dans le partenariat — tu crées des collaborations non conventionnelles.",
        "Ta mission publique passe par des partenariats qui brisent les conventions. Tu es fait pour être un créateur de collaborations innovantes, un consultant en nouvelles formes d'organisation ou un partenaire qui apporte des idées fraîches.",
        "On te perçoit comme quelqu'un d'original en partenariat. Ta réputation est celle d'un collaborateur qui apporte une perspective unique.",
        ["Crée des partenariats innovants.", "Révolutionne les collaborations.", "Journal : « Comment puis-je innover dans mes partenariats ? »"]
    ),
    ('aquarius', 8): make_mc_interp(
        "Verseau", 8,
        "Ta vocation de révolutionnaire s'applique aux transformations — tu libères des crises.",
        "Ta mission publique touche à la libération des situations de crise et de transformation. Tu es fait pour être un innovateur en gestion de crise, un technologue qui aide les transformations ou un libérateur de systèmes bloqués.",
        "On te perçoit comme quelqu'un qui trouve des solutions innovantes aux crises. Ta réputation est celle d'un libérateur qui pense différemment.",
        ["Libère par l'innovation dans les crises.", "Trouve des solutions non conventionnelles.", "Journal : « Comment puis-je aider à libérer des situations bloquées ? »"]
    ),
    ('aquarius', 9): make_mc_interp(
        "Verseau", 9,
        "Ta vocation de révolutionnaire s'étend aux horizons — tu révolutionnes la pensée.",
        "Ta mission publique est liée à la révolution des systèmes de pensée et d'éducation. Tu es fait pour être un penseur révolutionnaire, un réformateur de l'éducation ou un diffuseur d'idées futuristes.",
        "On te perçoit comme un penseur avant-gardiste. Ta réputation est celle d'un révolutionnaire de la sagesse.",
        ["Révolutionne les systèmes de pensée.", "Enseigne les idées du futur.", "Journal : « Comment puis-je révolutionner la façon de penser ? »"]
    ),
    ('aquarius', 10): make_mc_interp(
        "Verseau", 10,
        "Ta vocation de révolutionnaire est ta destinée publique — tu es reconnu pour ton innovation.",
        "Le MC en Verseau en maison 10 fait de toi un innovateur public par excellence. Tu es destiné à être reconnu pour ton originalité et ton avant-gardisme. Ta carrière te mène à une position d'influence dans l'innovation.",
        "Le monde te voit comme un visionnaire. Ta réputation est celle d'un professionnel qui façonne le futur.",
        ["Deviens reconnu pour ton innovation.", "Utilise ta position pour changer le monde.", "Journal : « Comment puis-je atteindre le sommet par mon originalité ? »"]
    ),
    ('aquarius', 11): make_mc_interp(
        "Verseau", 11,
        "Ta vocation de révolutionnaire est à son apogée — tu es né pour changer l'humanité.",
        "Ici, le MC en Verseau est dans sa pleine puissance en maison 11. Tu es destiné à être un agent de changement collectif, un leader de mouvements, un créateur de nouvelles formes de communauté. Le futur de l'humanité passe par toi.",
        "Le monde te voit exactement comme tu es : un révolutionnaire humanitaire. Ta réputation publique est celle d'un changeur de monde.",
        ["Révolutionne pour l'humanité.", "Deviens le leader du changement collectif.", "Journal : « Comment puis-je manifester ma pleine puissance révolutionnaire pour le bien de tous ? »"]
    ),
    ('aquarius', 12): make_mc_interp(
        "Verseau", 12,
        "Ta vocation de révolutionnaire opère dans l'invisible — tu libères l'inconscient collectif.",
        "Ta mission publique est de révolutionner les espaces invisibles et l'inconscient. Tu es fait pour être un innovateur en spiritualité, un technologue de la conscience ou un libérateur des prisons mentales collectives.",
        "Le monde ne voit pas toujours ta révolution, mais elle libère les âmes. Ta réputation se fait dans les dimensions subtiles.",
        ["Révolutionne l'invisible.", "Libère l'inconscient collectif.", "Journal : « Comment puis-je libérer ce qui est caché dans la psyché collective ? »"]
    ),

    # PISCES MC
    ('pisces', 1): make_mc_interp(
        "Poissons", 1,
        "Ta vocation est celle du guérisseur — tu es appelé à soigner et à inspirer.",
        "Tu es fait pour être un guérisseur, un artiste ou un guide spirituel. Ta carrière idéale te permet de soigner, d'inspirer ou de créer de la beauté. Tu excelles dans les arts, la guérison, le travail humanitaire ou tout domaine qui touche l'âme.",
        "Le monde te voit comme quelqu'un de compatissant, d'inspiré et de mystérieux. Ta réputation est celle d'un professionnel qui touche les cœurs et qui apporte de la guérison au monde.",
        ["Soigne et inspire par ta vocation.", "Utilise tes dons au service de l'âme.", "Journal : « Comment puis-je guérir le monde par mon travail ? »"]
    ),
    ('pisces', 2): make_mc_interp(
        "Poissons", 2,
        "Ta vocation de guérisseur s'applique aux ressources — tu crées de la valeur par l'inspiration.",
        "Ta mission publique est liée à la création de valeur par l'art, la spiritualité ou la guérison. Tu es fait pour être un artiste qui vit de son art, un guérisseur qui prospère ou un créateur de beauté qui génère de l'abondance.",
        "On te perçoit comme quelqu'un qui transforme l'inspiration en valeur. Ta réputation est celle d'un professionnel qui crée de la richesse par la beauté.",
        ["Crée de la valeur par l'inspiration.", "Transforme tes dons en prospérité.", "Journal : « Comment puis-je vivre de mon inspiration ? »"]
    ),
    ('pisces', 3): make_mc_interp(
        "Poissons", 3,
        "Ta vocation de guérisseur s'exprime dans la communication — tu parles à l'âme.",
        "Ta mission publique passe par une communication qui touche les profondeurs. Tu es fait pour être un poète, un auteur inspiré ou un communicateur qui touche l'âme de son public.",
        "On te perçoit comme quelqu'un de poétique et d'inspiré. Ta réputation est celle d'un communicateur qui parle au cœur.",
        ["Communique avec ton âme.", "Touche les autres par tes mots inspirés.", "Journal : « Comment puis-je communiquer de façon à toucher l'âme ? »"]
    ),
    ('pisces', 4): make_mc_interp(
        "Poissons", 4,
        "Ta vocation de guérisseur est nourrie par tes racines — tu portes une sensibilité ancestrale.",
        "Ta mission publique est liée à guérir ou exprimer quelque chose de profond venant de ton histoire familiale. Tu es peut-être destiné à guérir les blessures familiales ou à exprimer une sensibilité héritée.",
        "On te perçoit comme quelqu'un de profondément sensible à ses racines. Ta réputation est celle d'une personne qui porte et guérit l'héritage émotionnel.",
        ["Guéris l'héritage émotionnel.", "Exprime la sensibilité ancestrale.", "Journal : « Comment puis-je guérir ce qui vient de mes racines ? »"]
    ),
    ('pisces', 5): make_mc_interp(
        "Poissons", 5,
        "Ta vocation de guérisseur s'exprime dans la créativité — tu crées depuis l'âme.",
        "Ta mission publique passe par une créativité qui vient des profondeurs de l'âme. Tu es fait pour être un artiste inspiré, un créateur qui canalise quelque chose de plus grand ou un performer qui transporte son public.",
        "On te perçoit comme un créateur inspiré. Ta réputation est celle d'un artiste qui crée depuis un lieu de profondeur.",
        ["Crée depuis les profondeurs de ton âme.", "Exprime ce qui vient d'au-delà.", "Journal : « Comment puis-je exprimer ma créativité la plus inspirée ? »"]
    ),
    ('pisces', 6): make_mc_interp(
        "Poissons", 6,
        "Ta vocation de guérisseur s'applique au service — tu soignes au quotidien.",
        "Ta mission publique passe par le soin quotidien aux corps et aux âmes. Tu es fait pour être un soignant, un thérapeute ou un professionnel qui apporte de la guérison dans le travail de tous les jours.",
        "On te perçoit comme quelqu'un qui soigne vraiment. Ta réputation est celle d'un professionnel qui touche l'âme de ceux qu'il aide.",
        ["Soigne corps et âme dans ton travail.", "Apporte de la guérison au quotidien.", "Journal : « Comment puis-je soigner par mon service quotidien ? »"]
    ),
    ('pisces', 7): make_mc_interp(
        "Poissons", 7,
        "Ta vocation de guérisseur s'accomplit dans le partenariat — tu crées des liens d'âme.",
        "Ta mission publique passe par des partenariats qui touchent l'âme. Tu es fait pour être un conseiller conjugal spirituel, un collaborateur empathique ou un partenaire qui crée des connexions profondes.",
        "On te perçoit comme quelqu'un de profondément connecté en partenariat. Ta réputation est celle d'un collaborateur qui crée des liens authentiques.",
        ["Crée des partenariats d'âme.", "Connecte en profondeur.", "Journal : « Comment puis-je créer des liens authentiques dans mes partenariats ? »"]
    ),
    ('pisces', 8): make_mc_interp(
        "Poissons", 8,
        "Ta vocation de guérisseur s'applique aux transformations — tu guides à travers les passages.",
        "Ta mission publique touche aux passages et aux transformations de l'âme. Tu es fait pour être un accompagnateur de fin de vie, un thérapeute des profondeurs ou un guide qui aide à traverser les morts et renaissances.",
        "On te perçoit comme quelqu'un de capable d'accompagner les passages. Ta réputation est celle d'un guide des transformations de l'âme.",
        ["Accompagne les passages de l'âme.", "Guide à travers les transformations.", "Journal : « Comment puis-je aider les autres à traverser leurs transformations ? »"]
    ),
    ('pisces', 9): make_mc_interp(
        "Poissons", 9,
        "Ta vocation de guérisseur s'étend aux horizons — tu enseignes la sagesse de l'âme.",
        "Ta mission publique est liée à l'enseignement de vérités spirituelles et à la diffusion de sagesse inspirée. Tu es fait pour être un enseignant spirituel, un guide de pèlerinage ou un auteur de sagesse mystique.",
        "On te perçoit comme un sage inspiré. Ta réputation est celle d'un transmetteur de vérités profondes.",
        ["Enseigne la sagesse de l'âme.", "Diffuse les vérités inspirées.", "Journal : « Comment puis-je transmettre la sagesse spirituelle ? »"]
    ),
    ('pisces', 10): make_mc_interp(
        "Poissons", 10,
        "Ta vocation de guérisseur est ta destinée publique — tu es reconnu pour ta compassion.",
        "Le MC en Poissons en maison 10 fait de toi un guérisseur public par excellence. Tu es destiné à être reconnu pour ta compassion, ton inspiration et ta capacité à toucher l'âme collective.",
        "Le monde te voit comme un guérisseur inspiré. Ta réputation est celle d'un professionnel qui soigne l'âme du monde.",
        ["Deviens reconnu pour ta compassion.", "Utilise ta position pour guérir.", "Journal : « Comment puis-je atteindre le sommet par ma capacité à guérir ? »"]
    ),
    ('pisces', 11): make_mc_interp(
        "Poissons", 11,
        "Ta vocation de guérisseur sert l'humanité — tu soignes le collectif.",
        "Ta mission publique est de mettre ta compassion au service de l'humanité. Tu es fait pour être un guérisseur collectif, un artiste qui inspire les masses ou un humanitaire qui touche l'âme du monde.",
        "On te perçoit comme un guérisseur de l'humanité. Ta réputation est celle d'un compatissant qui soigne le collectif.",
        ["Soigne l'âme de l'humanité.", "Inspire le collectif par ta compassion.", "Journal : « Comment puis-je guérir l'humanité ? »"]
    ),
    ('pisces', 12): make_mc_interp(
        "Poissons", 12,
        "Ta vocation de guérisseur est à son apogée — tu es né pour l'invisible.",
        "Ici, le MC en Poissons est dans sa pleine puissance en maison 12. Tu es destiné à travailler avec l'invisible : spiritualité, inconscient, dimensions cachées. Tu es le guérisseur de l'âme, le pont entre les mondes.",
        "Le monde ne voit pas toujours ton travail, mais il touche les dimensions les plus profondes. Ta réputation est celle d'un maître de l'invisible.",
        ["Travaille avec les dimensions invisibles.", "Sois le pont entre les mondes.", "Journal : « Comment puis-je manifester ma pleine vocation de guérisseur des profondeurs ? »"]
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
