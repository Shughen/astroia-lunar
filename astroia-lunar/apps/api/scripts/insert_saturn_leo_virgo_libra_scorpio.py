#!/usr/bin/env python3
"""Script d'insertion des interprétations Saturn Leo/Virgo/Libra/Scorpio."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

# Template simplifié pour accélérer - chaque interprétation ~1000 chars
def make_saturn_interp(sign_fr, sign_en, house, theme, moteur, defi, maison_desc, rituel, journal):
    return f"""# ♄ Saturne en {sign_fr}
**En une phrase :** {theme}

## Ton moteur
{moteur}

## Ton défi
Le piège : {defi}

## Maison {house} en {sign_fr}
{maison_desc}

## Micro-rituel du jour (2 min)
- {rituel}
- Trois respirations en acceptant les leçons de Saturne
- Journal : « {journal} »"""

SATURN_INTERPRETATIONS = {}

# LEO - 12 maisons
for h in range(1, 13):
    themes = {
        1: ("Tu apprends à briller avec maturité — l'égo devient force tranquille.",
            "Saturne en Lion en Maison 1 te demande de développer une confiance en toi solide et méritée. Tu peux avoir des blocages dans l'expression de ta créativité ou de ton leadership. Le travail de Saturne est d'apprendre à briller avec authenticité.",
            "retenir ton éclat par peur du jugement, confondre humilité et effacement, ou chercher la reconnaissance de façon excessive. L'équilibre se trouve dans une expression de soi mature.",
            "Saturne structure ta présence autour de l'authenticité. Tu apprends que le vrai charisme vient de la maturité. Avec le temps, ton leadership gagne en profondeur.",
            "Exprimer quelque chose de créatif ou personnel de façon authentique",
            "Comment mon expression personnelle a-t-elle gagné en maturité ?"),
        2: ("Tu construis ta valeur sur des accomplissements réels — la fierté devient méritée.",
            "Saturne en Lion en Maison 2 te demande de bâtir ta valeur personnelle sur des réalisations concrètes. Tu peux douter de ta valeur ou avoir du mal à reconnaître tes talents. Le travail de Saturne est d'apprendre à te valoriser justement.",
            "sous-estimer ta valeur, confondre richesse et reconnaissance, ou dépenser pour impressionner. L'équilibre se trouve dans une estime de soi basée sur les faits.",
            "Saturne structure ton rapport à l'argent autour de la fierté méritée. Tu apprends à te valoriser pour ce que tu accomplis vraiment. Avec le temps, tes ressources reflètent ta vraie valeur.",
            "Reconnaître un accomplissement récent et sa valeur réelle",
            "Quelle réalisation concrète renforce ma fierté personnelle ?"),
        3: ("Tu communiques avec autorité et profondeur — les mots portent le poids de l'expérience.",
            "Saturne en Lion en Maison 3 te demande de développer une communication qui fait autorité. Tu peux avoir du mal à t'exprimer avec confiance ou craindre de ne pas être pris au sérieux. Le travail de Saturne est de gagner le respect par ta parole.",
            "te retenir de parler par peur du ridicule, communiquer de façon trop dramatique, ou chercher l'approbation constante. L'équilibre se trouve dans une expression confiante mais humble.",
            "Saturne structure ta communication autour de l'autorité méritée. Tu apprends que le respect vient de la substance. Avec le temps, ta parole gagne en impact.",
            "Exprimer une idée avec confiance et simplicité",
            "Comment ma communication a-t-elle gagné en autorité ?"),
        4: ("Tu construis un foyer où tu peux régner avec sagesse — la famille devient ton royaume.",
            "Saturne en Lion en Maison 4 te demande de créer un espace familial où tu peux exprimer ton leadership avec maturité. Tu as peut-être eu des tensions avec une figure d'autorité parentale. Le travail de Saturne est de devenir un pilier familial sage.",
            "vouloir dominer ta famille, avoir des conflits d'ego avec les parents, ou chercher l'admiration constante chez toi. L'équilibre se trouve dans un leadership familial bienveillant.",
            "Saturne structure ta vie familiale autour d'une autorité méritée. Tu apprends à être respecté pour ta sagesse plutôt que craint. Avec le temps, tu deviens le cœur stable de ta famille.",
            "Exercer ton autorité familiale avec bienveillance",
            "Comment suis-je devenu un pilier plus sage pour ma famille ?"),
        5: ("Tu apprends à créer et aimer avec maturité — la passion devient œuvre durable.",
            "Saturne en Lion en Maison 5 te confronte à tes blocages dans la créativité et l'expression amoureuse. Tu peux avoir peur de te montrer vulnérable ou de ne pas être à la hauteur. Le travail de Saturne est d'apprendre que la vraie créativité vient du cœur discipliné.",
            "bloquer ta créativité par perfectionnisme, des relations amoureuses trop sérieuses, ou te priver de joie par peur du jugement. L'équilibre se trouve dans une expression créative mature mais libre.",
            "Saturne structure tes plaisirs autour de l'authenticité. Tu apprends à créer avec profondeur. Avec le temps, tes œuvres et tes amours gagnent en substance.",
            "Créer quelque chose d'authentique sans chercher l'approbation",
            "Comment ma créativité a-t-elle mûri avec le temps ?"),
        6: ("Tu travailles avec excellence et fierté — l'effort quotidien devient œuvre d'art.",
            "Saturne en Lion en Maison 6 te demande de mettre ta fierté dans un travail bien fait. Tu peux avoir du mal à trouver de la reconnaissance dans les tâches quotidiennes. Le travail de Saturne est de trouver de la noblesse dans le service.",
            "dédaigner les tâches modestes, chercher la reconnaissance constante au travail, ou négliger ta santé par orgueil. L'équilibre se trouve dans un travail qui honore ton excellence.",
            "Saturne structure ton quotidien autour de la fierté du travail bien fait. Tu apprends à briller dans les détails. Avec le temps, ton excellence devient ta signature.",
            "Accomplir une tâche ordinaire avec excellence et fierté",
            "Comment mon travail quotidien exprime-t-il mon excellence ?"),
        7: ("Tu construis des partenariats où chacun peut briller — l'amour devient partage de lumière.",
            "Saturne en Lion en Maison 7 te demande d'apprendre à partager la scène avec un partenaire. Tu peux attirer des partenaires qui testent ton ego ou des relations où la fierté est en jeu. Le travail de Saturne est d'apprendre le duo harmonieux.",
            "rivaliser avec ton partenaire, des relations où l'ego domine, ou avoir du mal à laisser briller l'autre. L'équilibre se trouve dans un partenariat qui célèbre les deux.",
            "Saturne structure tes relations autour du respect mutuel. Tu apprends à admirer et être admiré. Avec le temps, tes partenariats deviennent des duos brillants.",
            "Célébrer une qualité de ton partenaire sincèrement",
            "Comment mes relations m'apprennent-elles à partager la lumière ?"),
        8: ("Tu traverses les crises avec dignité — les transformations révèlent ta vraie grandeur.",
            "Saturne en Lion en Maison 8 te demande d'affronter les profondeurs sans perdre ta dignité. Tu peux résister aux transformations par peur de perdre ton éclat. Le travail de Saturne est d'apprendre que la vraie noblesse survit aux crises.",
            "refuser de montrer ta vulnérabilité, des crises d'ego face aux pertes, ou confondre fierté et déni. L'équilibre se trouve dans une transformation qui préserve l'essentiel.",
            "Saturne structure ton rapport aux crises autour de la dignité. Tu apprends à traverser l'ombre en gardant ta lumière. Avec le temps, les épreuves révèlent ta vraie grandeur.",
            "Faire face à une difficulté avec dignité",
            "Quelle crise m'a révélé ma vraie force intérieure ?"),
        9: ("Tu forges ta philosophie avec courage — la sagesse devient expression personnelle.",
            "Saturne en Lion en Maison 9 te demande de développer une vision du monde qui t'appartient vraiment. Tu peux avoir du mal à adhérer aux systèmes qui ne te permettent pas de briller. Le travail de Saturne est de créer ta propre sagesse.",
            "imposer tes croyances, rejeter les enseignements qui ne te mettent pas au centre, ou confondre conviction et arrogance. L'équilibre se trouve dans une sagesse qui rayonne sans écraser.",
            "Saturne structure ta quête de sens autour de l'authenticité. Tu apprends à enseigner par l'exemple. Avec le temps, ta philosophie devient inspirante.",
            "Partager une conviction personnelle avec humilité",
            "Quelle sagesse personnelle puis-je transmettre aux autres ?"),
        10: ("Tu bâtis ta carrière en leader reconnu — l'ambition devient accomplissement durable.",
            "Saturne en Lion en Maison 10 te demande de mériter ta place au sommet par l'excellence. Tu peux avoir des blocages autour de l'ambition ou la peur de ne pas être à la hauteur. Le travail de Saturne est de devenir un leader par le mérite.",
            "chercher la gloire sans la substance, des conflits d'ego avec les supérieurs, ou confondre réussite et célébrité. L'équilibre se trouve dans un succès basé sur l'excellence réelle.",
            "Saturne structure ta carrière autour du leadership mérité. Tu apprends à briller par tes accomplissements. Avec le temps, ta réputation reflète ta vraie valeur.",
            "Travailler sur un aspect de ton excellence professionnelle",
            "Comment mes accomplissements construisent-ils ma réputation ?"),
        11: ("Tu crées des cercles où chacun peut briller — les amitiés deviennent des constellations.",
            "Saturne en Lion en Maison 11 te demande d'apprendre à partager la vedette dans les groupes. Tu peux avoir des difficultés à trouver ta place sans dominer ou te sentir menacé par les talents des autres. Le travail de Saturne est de créer des communautés où tous brillent.",
            "vouloir être le leader de chaque groupe, des amitiés où l'ego interfère, ou rejeter ceux qui te font de l'ombre. L'équilibre se trouve dans un cercle qui célèbre chaque lumière.",
            "Saturne structure tes réseaux autour du respect mutuel. Tu apprends à admirer les talents des autres. Avec le temps, tu deviens un catalyseur de brillance collective.",
            "Reconnaître et célébrer le talent d'un ami",
            "Comment puis-je soutenir la lumière des autres dans mes cercles ?"),
        12: ("Tu apprivoises ton besoin de briller — l'inconscient révèle une lumière plus profonde.",
            "Saturne en Lion en Maison 12 te confronte à tes blocages cachés autour de l'expression de toi-même. Tu peux saboter ton éclat inconsciemment ou avoir peur de ta propre lumière. Le travail de Saturne est de libérer la vraie lumière intérieure.",
            "t'effacer pour éviter l'attention, des schémas d'auto-sabotage de ta créativité, ou confondre humilité et effacement. L'équilibre se trouve dans une lumière qui brille sans chercher les projecteurs.",
            "Saturne structure ton monde intérieur autour de l'authenticité profonde. Tu apprends à briller de l'intérieur. Avec le temps, ta lumière vient de l'essence plutôt que de l'apparence.",
            "Méditer sur ta lumière intérieure sans besoin de validation",
            "Quelle lumière intérieure ai-je découverte en moi ?")
    }
    t = themes[h]
    SATURN_INTERPRETATIONS[('leo', h)] = make_saturn_interp('Lion', 'leo', h, t[0], t[1], t[2], t[3], t[4], t[5])

# VIRGO - 12 maisons
for h in range(1, 13):
    themes = {
        1: ("Tu incarnes la compétence et la précision — le service devient identité.",
            "Saturne en Vierge en Maison 1 te demande de développer une excellence pratique reconnue. Tu peux être trop critique envers toi-même ou avoir peur de ne pas être assez compétent. Le travail de Saturne est de bâtir une confiance basée sur la maîtrise réelle.",
            "te critiquer sans cesse, paraître froid par excès de réserve, ou te perdre dans les détails. L'équilibre se trouve dans une compétence sereine.",
            "Saturne structure ta présence autour de l'efficacité. Tu apprends à te faire confiance. Avec le temps, ta compétence inspire le respect.",
            "Reconnaître une compétence que tu as développée avec méthode", "Quelle maîtrise ai-je construite avec patience ?"),
        2: ("Tu construis ta sécurité par la compétence — le savoir-faire devient richesse.",
            "Saturne en Vierge en Maison 2 te demande de valoriser ton expertise pratique. Tu peux sous-estimer la valeur de tes compétences ou avoir des anxiétés financières. Le travail de Saturne est de monétiser ton savoir-faire.",
            "te sous-payer par modestie excessive, anxiété autour de l'argent, ou perfectionnisme qui retarde la rémunération. L'équilibre se trouve dans une juste valorisation de ton expertise.",
            "Saturne structure tes finances autour de la compétence. Tu apprends à facturer ta valeur réelle. Avec le temps, ton expertise devient une source de revenus stable.",
            "Identifier une compétence que tu pourrais mieux valoriser", "Comment mon expertise peut-elle mieux me rémunérer ?"),
        3: ("Tu communiques avec précision et méthode — les mots servent l'utilité.",
            "Saturne en Vierge en Maison 3 amplifie le besoin de communication précise et utile. Tu peux avoir peur de mal t'exprimer ou être trop critique dans tes échanges. Le travail de Saturne est de maîtriser l'art de la communication efficace.",
            "sur-analyser avant de parler, critiquer plutôt que construire, ou des apprentissages laborieux. L'équilibre se trouve dans une précision bienveillante.",
            "Saturne intensifie ici le besoin de maîtrise verbale. Tu apprends à communiquer avec exactitude. Avec le temps, ta parole devient une référence de clarté.",
            "Communiquer une idée de façon simple et précise", "Comment ma communication est-elle devenue plus efficace ?"),
        4: ("Tu construis un foyer organisé et fonctionnel — l'ordre devient sécurité.",
            "Saturne en Vierge en Maison 4 te demande de créer un espace de vie qui fonctionne bien. Tu as peut-être grandi avec des exigences de perfection domestique. Le travail de Saturne est de trouver l'équilibre entre ordre et chaleur.",
            "un foyer trop rigide, critique envers les membres de la famille, ou anxiété domestique. L'équilibre se trouve dans un chez-toi fonctionnel mais accueillant.",
            "Saturne structure ta vie familiale autour de l'efficacité. Tu apprends à créer un foyer qui fonctionne. Avec le temps, ton organisation devient un atout familial.",
            "Améliorer un aspect de l'organisation de ton foyer", "Comment l'ordre dans ma maison soutient-il mon bien-être ?"),
        5: ("Tu crées avec méthode et attention aux détails — l'art devient artisanat maîtrisé.",
            "Saturne en Vierge en Maison 5 te confronte au perfectionnisme dans la créativité. Tu peux bloquer tes créations par excès d'autocritique ou avoir des relations amoureuses trop analytiques. Le travail de Saturne est d'apprendre à créer avec précision ET joie.",
            "bloquer ta créativité par perfectionnisme, analyser l'amour au lieu de le vivre, ou te priver de plaisirs imparfaits. L'équilibre se trouve dans une création qui accepte l'imperfection.",
            "Saturne structure tes plaisirs autour de la maîtrise. Tu apprends à créer avec soin. Avec le temps, tes œuvres gagnent en finesse.",
            "Créer quelque chose sans chercher la perfection", "Comment puis-je m'amuser tout en étant attentif aux détails ?"),
        6: ("Tu excelles dans le travail méthodique — l'efficacité devient ta marque.",
            "Saturne en Vierge en Maison 6 amplifie ton besoin de travail bien fait et de santé optimale. Tu peux être trop exigeant envers toi-même ou avoir des inquiétudes de santé. Le travail de Saturne est de trouver un équilibre entre excellence et bien-être.",
            "te surmener par perfectionnisme, hypocondrie ou anxiété de santé, ou critiquer le travail des autres. L'équilibre se trouve dans une efficacité soutenable.",
            "Saturne intensifie ici les thèmes de travail et de santé. Tu apprends à être efficace sans t'épuiser. Avec le temps, ta méthode devient exemplaire.",
            "Accomplir une tâche avec excellence et sans stress excessif", "Comment puis-je être efficace sans m'épuiser ?"),
        7: ("Tu construis des partenariats basés sur le respect mutuel des compétences.",
            "Saturne en Vierge en Maison 7 te demande d'apprendre à apprécier les partenaires pour ce qu'ils sont vraiment. Tu peux être trop critique en couple ou attirer des partenaires perfectionnistes. Le travail de Saturne est d'accepter l'imperfection relationnelle.",
            "critiquer constamment ton partenaire, des relations basées sur l'utilité, ou des attentes impossibles. L'équilibre se trouve dans un partenariat qui accepte les défauts.",
            "Saturne structure tes relations autour du réalisme. Tu apprends à aimer les gens tels qu'ils sont. Avec le temps, tes partenariats gagnent en authenticité.",
            "Apprécier ton partenaire pour ce qu'il est, sans chercher à le corriger", "Comment ai-je appris à accepter les imperfections en relation ?"),
        8: ("Tu traverses les crises avec méthode — les transformations deviennent optimisations.",
            "Saturne en Vierge en Maison 8 te demande d'affronter les profondeurs de façon pratique. Tu peux analyser les crises au lieu de les traverser ou avoir des anxiétés autour de la santé et la mort. Le travail de Saturne est de transformer avec discernement.",
            "intellectualiser les émotions profondes, anxiété de santé ou hypocondrie, ou contrôle excessif des ressources partagées. L'équilibre se trouve dans une transformation acceptée avec méthode.",
            "Saturne structure ton rapport aux crises autour de l'analyse. Tu apprends à comprendre les transformations. Avec le temps, tu développes une sagesse pratique des profondeurs.",
            "Faire face à une peur de façon méthodique", "Quelle transformation ai-je gérée avec méthode et discernement ?"),
        9: ("Tu construis ta philosophie sur des bases vérifiables — la sagesse devient pratique.",
            "Saturne en Vierge en Maison 9 te demande de développer une vision du monde basée sur l'expérience concrète. Tu peux rejeter les croyances non prouvables ou avoir des études difficiles. Le travail de Saturne est de trouver le sens dans le vérifiable.",
            "scepticisme excessif, rejet des dimensions spirituelles, ou études trop analytiques. L'équilibre se trouve dans une ouverture qui reste critique.",
            "Saturne structure ta quête de sens autour du pragmatisme. Tu apprends à vérifier avant de croire. Avec le temps, ta sagesse devient une référence de bon sens.",
            "Explorer une idée philosophique de façon pratique", "Quelle croyance a résisté à mon analyse critique ?"),
        10: ("Tu bâtis ta carrière sur la compétence pure — l'expertise devient pouvoir.",
            "Saturne en Vierge en Maison 10 te demande de développer une excellence professionnelle reconnue. Tu peux douter de tes compétences ou travailler trop dur sans reconnaissance. Le travail de Saturne est de mériter le succès par la maîtrise.",
            "travailler dans l'ombre sans reconnaissance, perfectionnisme qui retarde la promotion, ou critique des supérieurs. L'équilibre se trouve dans une excellence reconnue.",
            "Saturne structure ta carrière autour de la compétence. Tu apprends à te faire valoir par la qualité. Avec le temps, ton expertise te hisse au sommet.",
            "Identifier une compétence professionnelle à développer", "Comment mon expertise construit-elle ma carrière ?"),
        11: ("Tu crées des réseaux basés sur l'entraide pratique — les amitiés servent un but.",
            "Saturne en Vierge en Maison 11 te demande de contribuer de façon concrète aux groupes. Tu peux être critique envers les amis ou avoir du mal à accepter l'aide. Le travail de Saturne est de créer des liens basés sur le service mutuel.",
            "critiquer les groupes ou les amis, des amitiés trop utilitaires, ou difficulté à demander de l'aide. L'équilibre se trouve dans une entraide authentique.",
            "Saturne structure tes réseaux autour de l'utilité mutuelle. Tu apprends à donner et recevoir de l'aide. Avec le temps, tes amitiés deviennent des ressources précieuses.",
            "Offrir une aide concrète à un ami", "Comment mes amitiés sont-elles basées sur l'entraide ?"),
        12: ("Tu apprivoises ton perfectionnisme caché — l'inconscient révèle ses exigences.",
            "Saturne en Vierge en Maison 12 te confronte à tes auto-critiques inconscientes. Tu peux te saboter par perfectionnisme invisible ou avoir des anxiétés cachées. Le travail de Saturne est de libérer le besoin de perfection.",
            "auto-sabotage par critique intérieure, anxiétés cachées de santé, ou service excessif qui épuise. L'équilibre se trouve dans l'acceptation de l'imperfection.",
            "Saturne structure ton inconscient autour du lâcher-prise. Tu apprends à accepter tes limites. Avec le temps, tu trouves la paix avec l'imperfection.",
            "Observer ta critique intérieure avec bienveillance", "Quelle exigence cachée ai-je commencé à relâcher ?")
    }
    t = themes[h]
    SATURN_INTERPRETATIONS[('virgo', h)] = make_saturn_interp('Vierge', 'virgo', h, t[0], t[1], t[2], t[3], t[4], t[5])

# LIBRA - 12 maisons (version condensée)
for h in range(1, 13):
    themes = {
        1: ("Tu incarnes l'équilibre et la diplomatie — l'harmonie devient ta signature.",
            "Saturne en Balance en Maison 1 te demande de développer un sens de l'équilibre authentique. Tu peux avoir du mal à t'affirmer ou trop dépendre de l'approbation des autres. Le travail de Saturne est de trouver ton centre tout en restant diplomate.",
            "te perdre dans le regard des autres, indécision chronique, ou effacement pour plaire. L'équilibre se trouve dans une harmonie qui inclut ta propre voix.",
            "Saturne structure ta présence autour de l'équilibre. Tu apprends à affirmer tes positions avec grâce. Avec le temps, ta diplomatie devient une force.", "Prendre une position claire sur un sujet important", "Comment puis-je être harmonieux tout en m'affirmant ?"),
        2: ("Tu construis ta valeur par les partenariats équitables — l'échange devient richesse.", "Saturne en Balance en Maison 2 te demande de valoriser l'équité dans les échanges financiers. Tu peux avoir du mal à demander ta juste part. Le travail de Saturne est d'apprendre la valeur de la réciprocité.", "te sous-évaluer pour maintenir l'harmonie, dépendance financière dans les relations, ou difficulté à négocier. L'équilibre se trouve dans des échanges justes.", "Saturne structure tes finances autour de l'équité. Tu apprends à recevoir autant que tu donnes. Avec le temps, tes ressources reflètent un échange équilibré.", "Négocier quelque chose de façon équitable", "Comment puis-je mieux valoriser ma contribution ?"),
        3: ("Tu communiques avec diplomatie et mesure — les mots créent des ponts.", "Saturne en Balance en Maison 3 te demande de développer une communication équilibrée et constructive. Tu peux avoir du mal à dire non ou à exprimer des désaccords. Le travail de Saturne est d'apprendre à être diplomate ET authentique.", "éviter les conflits au détriment de la vérité, indécision dans la communication, ou chercher constamment l'approbation. L'équilibre se trouve dans une diplomatie honnête.", "Saturne structure ta communication autour de l'équilibre. Tu apprends à dire les vérités difficiles avec grâce. Avec le temps, ta parole devient médiatrice.", "Exprimer un désaccord de façon constructive", "Comment ma communication a-t-elle gagné en équilibre ?"),
        4: ("Tu construis un foyer harmonieux — l'équilibre domestique devient priorité.", "Saturne en Balance en Maison 4 te demande de créer un espace familial équilibré. Tu as peut-être grandi avec des conflits familiaux ou un besoin d'harmonie à tout prix. Le travail de Saturne est de créer une vraie paix familiale.", "éviter les conflits familiaux plutôt que les résoudre, un foyer trop préoccupé par les apparences, ou sacrifier tes besoins pour l'harmonie. L'équilibre se trouve dans une famille qui accepte les différences.", "Saturne structure ta vie familiale autour de l'harmonie. Tu apprends à créer un foyer où chacun a sa place. Avec le temps, ta famille devient un modèle d'équilibre.", "Initier une conversation pour résoudre un déséquilibre familial", "Comment puis-je créer plus d'harmonie authentique chez moi ?"),
        5: ("Tu crées avec élégance et équilibre — l'art devient harmonie.", "Saturne en Balance en Maison 5 te confronte à tes blocages dans l'expression créative et amoureuse. Tu peux avoir du mal à jouer ou à aimer sans chercher l'approbation. Le travail de Saturne est de créer et d'aimer avec authenticité.", "créer pour plaire plutôt que pour exprimer, des relations amoureuses trop calculées, ou difficulté à profiter sans mesure. L'équilibre se trouve dans une joie authentique.", "Saturne structure tes plaisirs autour de l'harmonie. Tu apprends à créer et aimer avec grâce. Avec le temps, tes œuvres et tes amours gagnent en raffinement.", "Créer quelque chose pour le plaisir sans chercher l'approbation", "Comment puis-je m'amuser sans calculer ?"),
        6: ("Tu travailles avec harmonie et coopération — l'efficacité devient collaborative.", "Saturne en Balance en Maison 6 te demande de développer un travail d'équipe efficace. Tu peux avoir du mal à travailler seul ou à imposer tes méthodes. Le travail de Saturne est de trouver l'équilibre entre collaboration et autonomie.", "dépendre trop des collègues, difficulté à travailler seul, ou sacrifier ton efficacité pour la paix. L'équilibre se trouve dans une collaboration qui respecte tes besoins.", "Saturne structure ton quotidien autour de la coopération. Tu apprends à travailler efficacement avec les autres. Avec le temps, tu deviens un partenaire de travail recherché.", "Contribuer à un projet d'équipe de façon équilibrée", "Comment puis-je être efficace tout en coopérant ?"),
        7: ("Tu construis des partenariats matures et durables — l'engagement devient sérieux.", "Saturne en Balance en Maison 7 amplifie les thèmes de partenariat et d'engagement. Tu peux avoir des difficultés à t'engager ou attirer des partenaires qui te testent. Le travail de Saturne est d'apprendre le vrai partenariat.", "peur de l'engagement, des relations déséquilibrées, ou des partenaires trop exigeants. L'équilibre se trouve dans un engagement mature qui respecte les deux.", "Saturne intensifie ici les défis relationnels. Tu apprends ce qu'est un vrai partenariat. Avec le temps, tes relations deviennent des modèles d'équilibre.", "Travailler sur l'équilibre dans une relation importante", "Comment mes partenariats sont-ils devenus plus matures ?"),
        8: ("Tu traverses les crises en cherchant l'équilibre — les transformations deviennent rééquilibrages.", "Saturne en Balance en Maison 8 te demande d'affronter les profondeurs tout en maintenant l'harmonie. Tu peux éviter les conflits intimes ou les crises relationnelles. Le travail de Saturne est d'accepter le déséquilibre comme part de la transformation.", "éviter les crises nécessaires, des difficultés à partager équitablement les ressources, ou fuir l'intimité vraie. L'équilibre se trouve dans une transformation qui accepte le chaos temporaire.", "Saturne structure ton rapport aux crises autour de l'équité. Tu apprends à traverser les transformations relationnelles. Avec le temps, tu trouves un nouvel équilibre après chaque crise.", "Accepter un déséquilibre temporaire comme part du changement", "Quelle crise m'a mené à un nouvel équilibre ?"),
        9: ("Tu forges ta philosophie sur l'équilibre des perspectives — la sagesse devient dialogue.", "Saturne en Balance en Maison 9 te demande de développer une vision du monde qui intègre plusieurs points de vue. Tu peux avoir du mal à te positionner ou rejeter les croyances trop tranchées. Le travail de Saturne est de trouver ta vérité dans la nuance.", "indécision philosophique, rejet des positions fermes, ou relativisme excessif. L'équilibre se trouve dans une ouverture qui sait aussi se positionner.", "Saturne structure ta quête de sens autour du dialogue. Tu apprends à forger ta philosophie par l'échange. Avec le temps, ta sagesse devient inclusive mais claire.", "Te positionner sur une question importante malgré les nuances", "Quelle conviction ai-je forgée en écoutant toutes les perspectives ?"),
        10: ("Tu bâtis ta carrière sur la diplomatie et les partenariats — le succès devient collaboration.", "Saturne en Balance en Maison 10 te demande de réussir à travers les relations et la diplomatie. Tu peux avoir du mal à t'affirmer professionnellement ou dépendre des partenariats. Le travail de Saturne est de construire une carrière qui équilibre autonomie et collaboration.", "dépendre trop des autres pour réussir, difficulté à prendre des décisions seul, ou carrière définie par les relations. L'équilibre se trouve dans un succès qui t'appartient tout en valorisant les autres.", "Saturne structure ta carrière autour des partenariats. Tu apprends à réussir avec et grâce aux autres. Avec le temps, tu deviens un leader qui fédère.", "Prendre une décision professionnelle autonome", "Comment puis-je réussir tout en valorisant les collaborations ?"),
        11: ("Tu crées des réseaux harmonieux — les amitiés deviennent des alliances équilibrées.", "Saturne en Balance en Maison 11 te demande de développer des amitiés basées sur l'équité. Tu peux avoir du mal à dire non aux amis ou attirer des groupes déséquilibrés. Le travail de Saturne est de créer des cercles où chacun contribue.", "donner plus que tu ne reçois en amitié, des groupes où les rôles sont déséquilibrés, ou difficulté à t'intégrer. L'équilibre se trouve dans des amitiés de vraie réciprocité.", "Saturne structure tes réseaux autour de l'équité. Tu apprends à créer des amitiés équilibrées. Avec le temps, tes cercles deviennent des espaces d'échange juste.", "Évaluer l'équilibre du donner-recevoir dans une amitié", "Comment mes amitiés sont-elles devenues plus équilibrées ?"),
        12: ("Tu apprivoises ton besoin d'approbation — l'inconscient révèle sa quête d'harmonie.", "Saturne en Balance en Maison 12 te confronte à tes dépendances cachées au regard des autres. Tu peux saboter ton équilibre par besoin inconscient d'approbation. Le travail de Saturne est de trouver l'harmonie intérieure.", "auto-sabotage pour plaire, peur cachée du rejet, ou sacrifice de soi inconscient. L'équilibre se trouve dans une paix intérieure qui ne dépend pas des autres.", "Saturne structure ton inconscient autour de l'autonomie émotionnelle. Tu apprends à te valider toi-même. Avec le temps, tu trouves l'harmonie en toi.", "Méditer sur ton besoin d'approbation avec bienveillance", "Quelle paix intérieure ai-je trouvée indépendamment des autres ?")
    }
    t = themes[h]
    SATURN_INTERPRETATIONS[('libra', h)] = make_saturn_interp('Balance', 'libra', h, t[0], t[1], t[2], t[3], t[4], t[5])

# SCORPIO - 12 maisons (version condensée)
for h in range(1, 13):
    themes = {
        1: ("Tu incarnes une présence intense et transformatrice — la profondeur devient force.", "Saturne en Scorpion en Maison 1 te demande de maîtriser ton intensité. Tu peux avoir des blocages autour de l'expression de ta puissance ou une peur de ta propre profondeur. Le travail de Saturne est d'apprendre à canaliser ton magnétisme.", "réprimer ton intensité, intimider les autres inconsciemment, ou avoir peur de ta propre puissance. L'équilibre se trouve dans une profondeur maîtrisée.", "Saturne structure ta présence autour de la maîtrise de soi. Tu apprends à canaliser ton intensité. Avec le temps, ta profondeur devient une force respectée.", "Exprimer ton intensité de façon constructive", "Comment ma profondeur est-elle devenue une force ?"),
        2: ("Tu construis ta sécurité sur des fondations profondes — la transformation devient richesse.", "Saturne en Scorpion en Maison 2 te demande de trouver la vraie sécurité à travers les transformations. Tu peux avoir des peurs profondes autour de la perte ou du contrôle des ressources. Le travail de Saturne est d'apprendre que la vraie richesse survit aux crises.", "contrôle excessif des ressources, peur de la perte, ou manipulation pour la sécurité. L'équilibre se trouve dans une confiance qui transcende le matériel.", "Saturne structure tes finances autour de la résilience. Tu apprends à construire une sécurité qui ne craint pas le changement. Avec le temps, ta valeur devient indestructible.", "Identifier une sécurité intérieure qui ne dépend pas des possessions", "Quelle valeur en moi survit à toutes les pertes ?"),
        3: ("Tu communiques avec profondeur et perspicacité — les mots percent les apparences.", "Saturne en Scorpion en Maison 3 te demande de maîtriser l'art de la communication profonde. Tu peux avoir du mal à parler de sujets légers ou à exprimer tes perceptions intuitives. Le travail de Saturne est d'apprendre à communiquer l'essentiel.", "garder les vérités profondes pour toi, communication intimidante, ou manipulation verbale. L'équilibre se trouve dans une profondeur qui sait aussi être accessible.", "Saturne structure ta communication autour de l'essentiel. Tu apprends à dire ce qui compte vraiment. Avec le temps, ta parole gagne en impact transformateur.", "Partager une vérité profonde de façon accessible", "Comment ma communication touche-t-elle à l'essentiel ?"),
        4: ("Tu construis un foyer qui permet la transformation — les racines deviennent régénération.", "Saturne en Scorpion en Maison 4 te demande de créer un espace familial qui accepte les profondeurs. Tu as peut-être vécu des intensités familiales ou des secrets. Le travail de Saturne est de transformer les blessures en fondations solides.", "des secrets familiaux lourds, une atmosphère domestique trop intense, ou difficulté à se sentir en sécurité chez soi. L'équilibre se trouve dans un foyer qui guérit.", "Saturne structure ta vie familiale autour de la transformation. Tu apprends à créer un espace qui permet la guérison. Avec le temps, ton foyer devient un lieu de renaissance.", "Transformer un aspect de ton héritage familial", "Quelle blessure familiale ai-je transformée en force ?"),
        5: ("Tu crées avec intensité et pouvoir transformateur — l'art devient alchimie.", "Saturne en Scorpion en Maison 5 te confronte à tes blocages dans l'expression créative et amoureuse profonde. Tu peux avoir peur de l'intensité émotionnelle ou des relations qui transforment. Le travail de Saturne est d'apprendre à créer et aimer intensément.", "bloquer ta créativité par peur de ce qui pourrait émerger, des relations amoureuses intenses mais difficiles, ou éviter les plaisirs qui engagent vraiment. L'équilibre se trouve dans une intensité qui libère plutôt qu'elle ne détruit.", "Saturne structure tes plaisirs autour de la transformation. Tu apprends à créer et aimer en profondeur. Avec le temps, tes œuvres et tes amours ont un pouvoir transformateur.", "Créer quelque chose qui exprime une vérité profonde", "Comment ma créativité touche-t-elle aux profondeurs ?"),
        6: ("Tu travailles avec intensité et transformation — le service devient guérison.", "Saturne en Scorpion en Maison 6 te demande de trouver un travail qui transforme. Tu peux être attiré par les métiers de crise ou de guérison. Le travail de Saturne est de canaliser ton intensité dans le service.", "te consumer dans le travail, attirer des environnements de travail intenses, ou des problèmes de santé liés au stress émotionnel. L'équilibre se trouve dans un travail transformateur mais soutenable.", "Saturne structure ton quotidien autour de la transformation. Tu apprends à travailler intensément sans te brûler. Avec le temps, ton travail devient une force de guérison.", "Transformer un aspect de ta routine quotidienne", "Comment mon travail a-t-il un impact transformateur ?"),
        7: ("Tu construis des partenariats profonds et transformateurs — l'amour devient alchimie.", "Saturne en Scorpion en Maison 7 te demande d'apprendre le partenariat profond. Tu peux attirer des relations intenses ou avoir des difficultés avec l'intimité vraie. Le travail de Saturne est d'apprendre à se transformer mutuellement.", "des relations de pouvoir déséquilibrées, peur de l'intimité vraie, ou manipulation dans les partenariats. L'équilibre se trouve dans une transformation mutuelle qui respecte chacun.", "Saturne structure tes partenariats autour de la profondeur. Tu apprends à créer des liens qui transforment. Avec le temps, tes relations deviennent des espaces de croissance mutuelle.", "Approfondir l'intimité dans une relation importante", "Comment mes partenariats me transforment-ils positivement ?"),
        8: ("Tu maîtrises les cycles de mort et renaissance — la transformation devient sagesse.", "Saturne en Scorpion en Maison 8 amplifie ta capacité à traverser les crises avec maîtrise. Tu peux avoir vécu des pertes importantes ou avoir un rapport intense aux ressources partagées. Le travail de Saturne est de devenir un maître de la transformation.", "résistance aux transformations nécessaires, contrôle excessif dans les domaines partagés, ou fascination morbide pour les profondeurs. L'équilibre se trouve dans une sagesse qui honore les cycles.", "Saturne intensifie ici ta connexion aux mystères de la vie. Tu apprends à naviguer les transformations avec maîtrise. Avec le temps, tu deviens un guide pour ceux qui traversent leurs propres crises.", "Honorer une transformation que tu as traversée", "Quelle sagesse ai-je tirée de mes crises les plus profondes ?"),
        9: ("Tu forges ta philosophie dans les profondeurs — la sagesse devient ésotérique.", "Saturne en Scorpion en Maison 9 te demande de développer une vision du monde qui intègre les mystères. Tu peux être attiré par les connaissances cachées ou avoir du mal avec les religions de surface. Le travail de Saturne est de trouver la vérité dans les profondeurs.", "scepticisme des philosophies superficielles, attrait pour les connaissances occultes, ou difficulté à partager ta vision. L'équilibre se trouve dans une sagesse profonde qui reste accessible.", "Saturne structure ta quête de sens autour des mystères. Tu apprends à explorer les dimensions cachées avec discernement. Avec le temps, ta sagesse touche à l'essentiel.", "Explorer une vérité ésotérique avec discernement", "Quelle sagesse profonde guide ma vie ?"),
        10: ("Tu bâtis ta carrière sur ta capacité à transformer — le pouvoir devient responsabilité.", "Saturne en Scorpion en Maison 10 te demande de mériter une position de pouvoir par ta capacité transformatrice. Tu peux être attiré par des carrières intenses ou avoir des blocages autour du pouvoir. Le travail de Saturne est d'apprendre à exercer le pouvoir avec sagesse.", "luttes de pouvoir professionnelles, attirer des environnements de travail intenses, ou résistance à prendre des responsabilités. L'équilibre se trouve dans un pouvoir qui sert.", "Saturne structure ta carrière autour de la transformation. Tu apprends à exercer une influence profonde. Avec le temps, tu deviens un leader qui transforme.", "Exercer ton influence de façon constructive", "Comment mon pouvoir professionnel sert-il un but plus grand ?"),
        11: ("Tu crées des cercles de transformation mutuelle — les amitiés deviennent initiatiques.", "Saturne en Scorpion en Maison 11 te demande de développer des amitiés profondes qui transforment. Tu peux avoir peu d'amis mais des liens intenses. Le travail de Saturne est de créer des communautés qui guérissent.", "des amitiés trop intenses, des groupes où règnent les jeux de pouvoir, ou difficulté à faire confiance. L'équilibre se trouve dans des cercles qui transforment positivement.", "Saturne structure tes réseaux autour de la profondeur. Tu apprends à créer des liens qui changent. Avec le temps, tes amitiés deviennent des espaces de transformation mutuelle.", "Approfondir une amitié vers plus d'authenticité", "Comment mes cercles permettent-ils la transformation ?"),
        12: ("Tu apprivoises tes profondeurs cachées — l'inconscient révèle ses trésors.", "Saturne en Scorpion en Maison 12 te confronte à tes peurs et désirs les plus profonds. Tu peux avoir des processus psychiques intenses ou des secrets qui pèsent. Le travail de Saturne est d'explorer l'inconscient avec courage et discernement.", "résistance à explorer l'ombre, des processus psychiques intenses, ou porter des fardeaux karmiques. L'équilibre se trouve dans une exploration bienveillante des profondeurs.", "Saturne structure ton inconscient autour de la transformation. Tu apprends à plonger dans tes abysses avec sagesse. Avec le temps, tu transformes tes ombres en lumière.", "Explorer une peur profonde avec bienveillance", "Quelle ombre ai-je transformée en force ?")
    }
    t = themes[h]
    SATURN_INTERPRETATIONS[('scorpio', h)] = make_saturn_interp('Scorpion', 'scorpio', h, t[0], t[1], t[2], t[3], t[4], t[5])

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
