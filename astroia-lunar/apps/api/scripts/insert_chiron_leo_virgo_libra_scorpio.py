#!/usr/bin/env python3
"""Insert Chiron interpretations for Leo, Virgo, Libra, Scorpio (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_chiron_interp(sign_name, house, phrase, blessure, guerison, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'leo': '⚷ Chiron en Lion',
        'virgo': '⚷ Chiron en Vierge',
        'libra': '⚷ Chiron en Balance',
        'scorpio': '⚷ Chiron en Scorpion',
    }
    sign_fr = {
        'leo': 'Lion',
        'virgo': 'Vierge',
        'libra': 'Balance',
        'scorpio': 'Scorpion',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ta blessure originelle
{blessure}

## Ton don de guérison
{guerison}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

CHIRON_INTERPRETATIONS = {
    # === LEO (M1-M12) ===
    ('leo', 1): make_chiron_interp('leo', 1,
        "Ta blessure touche ta capacité à briller et à être vu — tu deviens guérisseur de l'expression de soi.",
        "Chiron en Lion dans ta maison I révèle une blessure profonde autour de ton droit de briller et d'être remarqué. Tu as pu te sentir invisible, humilié ou honteux de ta lumière.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à oser briller et à exprimer leur unicité sans honte.",
        "Cette position en maison I rend la blessure très visible dans ta présence. Tu apprends que ta lumière mérite d'être vue et que tu inspires en osant briller.",
        "Fais quelque chose qui te met en lumière, même modestement.",
        "Respire en te sentant digne d'être vu et admiré.",
        "Où ai-je eu honte de ma lumière ou de mon besoin d'être vu ? »"),

    ('leo', 2): make_chiron_interp('leo', 2,
        "Ta blessure touche ta valeur créative — tu deviens guérisseur de la valeur personnelle.",
        "Chiron en Lion dans ta maison II révèle une blessure autour de la valeur de tes talents créatifs. Tu as pu te sentir indigne de gagner ta vie par ta créativité.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconnaître la valeur de leur créativité et à en vivre.",
        "Cette position en maison II peut créer un sentiment que tes talents ne valent rien. Tu apprends que ta créativité est précieuse et mérite d'être rétribuée.",
        "Valorise un de tes talents créatifs concrètement.",
        "Respire en te sentant riche de ta créativité.",
        "Où ai-je dévalorisé mes talents créatifs ? »"),

    ('leo', 3): make_chiron_interp('leo', 3,
        "Ta blessure touche ta parole créative — tu deviens guérisseur de l'expression.",
        "Chiron en Lion dans ta maison III révèle une blessure autour de l'expression créative de tes idées. Tu as pu te sentir moqué ou humilié quand tu t'exprimais.",
        "En traversant cette blessure, tu développes un don pour encourager les autres à s'exprimer avec créativité et audace.",
        "Cette position en maison III peut avoir créé des blocages d'expression par peur du ridicule. Tu apprends que ta voix créative mérite d'être entendue.",
        "Exprime une idée de façon créative et audacieuse.",
        "Respire en te sentant libre de t'exprimer pleinement.",
        "Où me suis-je retenu d'exprimer ma créativité par peur du jugement ? »"),

    ('leo', 4): make_chiron_interp('leo', 4,
        "Ta blessure touche la reconnaissance familiale — tu deviens guérisseur de la lumière intérieure.",
        "Chiron en Lion dans ta maison IV révèle une blessure autour de la reconnaissance au sein de ta famille. Tu as pu te sentir invisible ou non-célébré chez toi.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur lumière intérieure, indépendamment de la reconnaissance familiale.",
        "Cette position en maison IV peut avoir créé un sentiment que ta famille ne voyait pas ta valeur. Tu apprends à être ton propre soleil.",
        "Célèbre quelque chose de toi-même, même sans public.",
        "Respire en te sentant brillant de l'intérieur.",
        "Quelle reconnaissance familiale m'a manqué ? »"),

    ('leo', 5): make_chiron_interp('leo', 5,
        "Ta blessure touche ta créativité et tes amours — tu deviens guérisseur de la joie de vivre.",
        "Chiron en Lion dans ta maison V (son domicile) révèle une blessure profonde autour de la créativité, de l'amour et de la joie. Tu as pu être humilié dans tes expressions créatives ou amoureuses.",
        "En traversant cette blessure, tu développes un don exceptionnel pour aider les autres à retrouver leur joie de vivre et leur créativité.",
        "Cette position en maison V intensifie la blessure créative et amoureuse. Tu peux avoir peur de te montrer ou d'aimer. Tu apprends que ta créativité guérit.",
        "Crée quelque chose pour la pure joie, sans attente.",
        "Respire en sentant ta joie de vivre renaître.",
        "Quelle humiliation créative ou amoureuse n'ai-je pas guérie ? »"),

    ('leo', 6): make_chiron_interp('leo', 6,
        "Ta blessure touche la reconnaissance au travail — tu deviens guérisseur de la valeur professionnelle.",
        "Chiron en Lion dans ta maison VI révèle une blessure autour de la reconnaissance de ton travail quotidien. Tu as pu te sentir invisible ou non-apprécié.",
        "En traversant cette blessure, tu développes un don pour aider les autres à être reconnus dans leur travail et à apporter leur lumière au quotidien.",
        "Cette position en maison VI peut créer des frustrations professionnelles liées au manque de reconnaissance. Tu apprends à briller même dans les tâches ordinaires.",
        "Apporte ta touche créative dans une tâche quotidienne.",
        "Respire en te sentant précieux dans ton travail.",
        "Où me suis-je senti invisible ou sous-apprécié au travail ? »"),

    ('leo', 7): make_chiron_interp('leo', 7,
        "Ta blessure touche la lumière en couple — tu deviens guérisseur des relations créatives.",
        "Chiron en Lion dans ta maison VII révèle une blessure autour de ta capacité à briller dans les relations. Tu as pu te sentir éclipsé par tes partenaires.",
        "En traversant cette blessure, tu développes un don pour aider les couples à briller ensemble et à célébrer mutuellement leur unicité.",
        "Cette position en maison VII peut attirer des partenaires qui te volent la vedette ou t'empêchent de briller. Tu apprends l'équilibre des lumières.",
        "Brille dans une relation sans éclipser l'autre.",
        "Respire en te sentant radieux au sein de tes relations.",
        "Où me suis-je éteint pour ne pas faire d'ombre à un partenaire ? »"),

    ('leo', 8): make_chiron_interp('leo', 8,
        "Ta blessure touche la lumière dans les ténèbres — tu deviens guérisseur des crises créatives.",
        "Chiron en Lion dans ta maison VIII révèle une blessure autour de ta capacité à garder ta lumière dans les moments sombres. Tu as pu perdre ta joie dans les crises.",
        "En traversant cette blessure, tu développes un don pour aider les autres à garder leur lumière même dans les transformations les plus profondes.",
        "Cette position en maison VIII peut avoir éteint ta lumière dans des expériences traumatiques. Tu apprends que ta lumière survit aux ténèbres.",
        "Trouve quelque chose de lumineux dans une situation sombre.",
        "Respire en sentant ta lumière indestructible.",
        "Comment ai-je perdu ma joie dans les épreuves ? »"),

    ('leo', 9): make_chiron_interp('leo', 9,
        "Ta blessure touche ta vision et ton enseignement — tu deviens guérisseur de l'inspiration.",
        "Chiron en Lion dans ta maison IX révèle une blessure autour de ta capacité à enseigner et à partager ta vision. Tu as pu te sentir illégitime à inspirer les autres.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur vision unique et à oser l'enseigner.",
        "Cette position en maison IX peut avoir créé des doutes sur ta capacité à être un guide ou un professeur. Tu apprends que ta vision inspire.",
        "Partage une vision ou un enseignement qui t'est cher.",
        "Respire en te sentant inspirant et visionnaire.",
        "Où me suis-je senti illégitime à enseigner ou inspirer ? »"),

    ('leo', 10): make_chiron_interp('leo', 10,
        "Ta blessure touche la gloire et le statut — tu deviens guérisseur de l'ambition créative.",
        "Chiron en Lion dans ta maison X révèle une blessure autour de ta visibilité publique et de ta réussite. Tu as pu être humilié publiquement ou avoir peur de la célébrité.",
        "En traversant cette blessure, tu développes un don pour aider les autres à assumer leur réussite et à briller sur la scène publique.",
        "Cette position en maison X peut créer une peur du succès ou de l'exposition. Tu apprends à briller publiquement avec authenticité.",
        "Assume ta réussite et ta visibilité.",
        "Respire en te sentant à l'aise avec le succès.",
        "Quelle humiliation publique ou peur du succès porte-je encore ? »"),

    ('leo', 11): make_chiron_interp('leo', 11,
        "Ta blessure touche ta lumière dans les groupes — tu deviens guérisseur de l'appartenance créative.",
        "Chiron en Lion dans ta maison XI révèle une blessure autour de ta place unique dans les groupes. Tu as pu te sentir rejeté pour ta différence ou ta lumière.",
        "En traversant cette blessure, tu développes un don pour aider chacun à briller dans le collectif et à être célébré pour son unicité.",
        "Cette position en maison XI peut avoir créé un sentiment d'être trop différent pour appartenir. Tu apprends que ton unicité enrichit le groupe.",
        "Apporte ta lumière unique à un groupe.",
        "Respire en te sentant célébré pour ta différence.",
        "Où me suis-je senti rejeté pour ma lumière ou ma différence dans un groupe ? »"),

    ('leo', 12): make_chiron_interp('leo', 12,
        "Ta blessure touche ta lumière cachée — tu deviens guérisseur de l'égo spirituel.",
        "Chiron en Lion dans ta maison XII révèle une blessure profonde autour de ton droit de briller au niveau spirituel. Tu peux avoir honte de ta lumière ou la cacher.",
        "En traversant cette blessure, tu développes un don pour aider les autres à réconcilier leur égo et leur spiritualité, à briller humblement.",
        "Cette position en maison XII porte une dimension karmique. Tu peux avoir été puni pour ta lumière dans d'autres vies. Tu apprends l'éclat humble.",
        "Médite sur ta lumière intérieure avec humilité et gratitude.",
        "Respire en laissant ta lumière rayonner doucement.",
        "Quelle culpabilité porte mon âme autour du fait de briller ? »"),

    # === VIRGO (M1-M12) ===
    ('virgo', 1): make_chiron_interp('virgo', 1,
        "Ta blessure touche ta perfection et ta santé — tu deviens guérisseur du corps et de l'esprit.",
        "Chiron en Vierge dans ta maison I révèle une blessure profonde autour de ton corps et de ton perfectionnisme. Tu as pu te sentir imparfait, critiqué ou malade.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à accepter leur imperfection et à guérir leur corps.",
        "Cette position en maison I rend la blessure très visible dans ton rapport au corps et à toi-même. Tu apprends que l'imperfection est humaine et belle.",
        "Accepte une de tes imperfections avec amour.",
        "Respire en te sentant parfait dans ton imperfection.",
        "Quelle imperfection de mon corps ou de moi-même n'ai-je pas acceptée ? »"),

    ('virgo', 2): make_chiron_interp('virgo', 2,
        "Ta blessure touche ta valeur dans le service — tu deviens guérisseur de la valeur pratique.",
        "Chiron en Vierge dans ta maison II révèle une blessure autour de la valeur de ton travail et de ta capacité à servir. Tu as pu te sentir mal payé ou sous-estimé.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconnaître la valeur de leur service et de leurs compétences pratiques.",
        "Cette position en maison II peut créer un sentiment que ton travail minutieux ne vaut rien. Tu apprends que ton service est précieux.",
        "Valorise une de tes compétences pratiques.",
        "Respire en te sentant utile et précieux.",
        "Où ai-je été sous-payé ou sous-estimé pour mon travail minutieux ? »"),

    ('virgo', 3): make_chiron_interp('virgo', 3,
        "Ta blessure touche ta communication analytique — tu deviens guérisseur de la parole précise.",
        "Chiron en Vierge dans ta maison III révèle une blessure autour de ton analyse et de ta façon de communiquer. Tu as pu te sentir critiqué ou trop critique.",
        "En traversant cette blessure, tu développes un don pour aider les autres à communiquer avec précision et discernement sans tomber dans la critique.",
        "Cette position en maison III peut avoir créé des difficultés liées à l'autocritique ou à la critique des autres. Tu apprends la parole constructive.",
        "Communique une observation utile avec bienveillance.",
        "Respire en équilibrant analyse et compassion.",
        "Comment ma tendance critique a-t-elle blessé mes communications ? »"),

    ('virgo', 4): make_chiron_interp('virgo', 4,
        "Ta blessure touche l'ordre dans le foyer — tu deviens guérisseur de la maison intérieure.",
        "Chiron en Vierge dans ta maison IV révèle une blessure autour de l'ordre et du service au sein de la famille. Tu as pu porter trop de responsabilités ou te sentir critiqué.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer un foyer fonctionnel sans perfectionnisme toxique.",
        "Cette position en maison IV peut avoir créé un environnement où tu n'étais jamais assez bien. Tu apprends à créer un foyer d'acceptation.",
        "Crée du confort chez toi sans chercher la perfection.",
        "Respire en te sentant chez toi dans l'imperfection.",
        "Quelles critiques familiales ont façonné mon perfectionnisme ? »"),

    ('virgo', 5): make_chiron_interp('virgo', 5,
        "Ta blessure touche ta créativité et le plaisir — tu deviens guérisseur de la joie imparfaite.",
        "Chiron en Vierge dans ta maison V révèle une blessure autour du plaisir et de la créativité imparfaite. Tu as pu ne pas t'autoriser à jouer ou créer « mal ».",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer et aimer sans perfectionnisme.",
        "Cette position en maison V peut avoir inhibé ta créativité et tes amours par peur de ne pas être parfait. Tu apprends la joie de l'imperfection.",
        "Crée quelque chose de délibérément imparfait avec joie.",
        "Respire en t'autorisant le plaisir sans condition.",
        "Où mon perfectionnisme a-t-il tué ma joie de créer ou d'aimer ? »"),

    ('virgo', 6): make_chiron_interp('virgo', 6,
        "Ta blessure touche le travail et la santé — tu deviens guérisseur du quotidien.",
        "Chiron en Vierge dans ta maison VI (son domicile) révèle une blessure profonde autour du travail, de la santé et du service. Tu as pu te rendre malade de perfectionnisme.",
        "En traversant cette blessure, tu développes un don exceptionnel pour la guérison et l'aide aux autres dans leur corps et leur quotidien.",
        "Cette position en maison VI intensifie le lien entre santé et perfectionnisme. Tu peux avoir des problèmes digestifs ou nerveux. Tu apprends la guérison holistique.",
        "Accomplis une tâche de façon « assez bonne » sans perfectionnisme.",
        "Respire en relâchant la tension du perfectionnisme dans ton corps.",
        "Comment mon perfectionnisme affecte-t-il ma santé ? »"),

    ('virgo', 7): make_chiron_interp('virgo', 7,
        "Ta blessure touche le perfectionnisme en couple — tu deviens guérisseur des relations imparfaites.",
        "Chiron en Vierge dans ta maison VII révèle une blessure autour de la perfection dans les relations. Tu as pu être trop critique ou critiqué dans tes partenariats.",
        "En traversant cette blessure, tu développes un don pour aider les couples à accepter leurs imperfections mutuelles et à grandir ensemble.",
        "Cette position en maison VII peut attirer des partenaires critiques ou te rendre très exigeant. Tu apprends l'amour inconditionnel de l'imperfection.",
        "Accepte une imperfection de ton partenaire avec amour.",
        "Respire en voyant la beauté dans les défauts de l'autre.",
        "Comment ma tendance critique a-t-elle affecté mes relations ? »"),

    ('virgo', 8): make_chiron_interp('virgo', 8,
        "Ta blessure touche le contrôle dans les crises — tu deviens guérisseur des transformations.",
        "Chiron en Vierge dans ta maison VIII révèle une blessure autour du contrôle dans les moments de crise. Tu as pu essayer de tout analyser pour éviter la douleur.",
        "En traversant cette blessure, tu développes un don pour aider les autres à traverser les transformations avec discernement mais sans contrôle excessif.",
        "Cette position en maison VIII peut créer une peur de l'incontrôlable. Tu apprends à analyser sans éviter et à transformer avec sagesse.",
        "Lâche le contrôle dans une situation qui te dépasse.",
        "Respire en faisant confiance au chaos transformateur.",
        "Où mon besoin de contrôle m'empêche-t-il de me transformer ? »"),

    ('virgo', 9): make_chiron_interp('virgo', 9,
        "Ta blessure touche la sagesse pratique — tu deviens guérisseur de l'intégration corps-esprit.",
        "Chiron en Vierge dans ta maison IX révèle une blessure autour de l'intellect et de la spiritualité pratique. Tu as pu douter de ta sagesse ou la juger trop terre-à-terre.",
        "En traversant cette blessure, tu développes un don pour aider les autres à incarner leur sagesse dans le quotidien.",
        "Cette position en maison IX peut avoir créé un conflit entre analyse et foi. Tu apprends que la spiritualité peut être pratique.",
        "Incarne une sagesse dans un geste pratique.",
        "Respire en intégrant l'esprit et le corps.",
        "Où ai-je séparé la sagesse de la vie pratique ? »"),

    ('virgo', 10): make_chiron_interp('virgo', 10,
        "Ta blessure touche le perfectionnisme de carrière — tu deviens guérisseur de l'excellence humaine.",
        "Chiron en Vierge dans ta maison X révèle une blessure autour de la perfection professionnelle. Tu as pu te sentir jamais assez compétent ou toujours critiqué.",
        "En traversant cette blessure, tu développes un don pour aider les autres à atteindre l'excellence sans perfectionnisme destructeur.",
        "Cette position en maison X peut créer une peur de l'imperfection publique. Tu apprends que l'excellence humaine inclut les erreurs.",
        "Accepte une erreur professionnelle avec compassion.",
        "Respire en te sentant compétent malgré tes imperfections.",
        "Comment mon perfectionnisme a-t-il limité ma carrière ? »"),

    ('virgo', 11): make_chiron_interp('virgo', 11,
        "Ta blessure touche ta place dans le service collectif — tu deviens guérisseur des communautés.",
        "Chiron en Vierge dans ta maison XI révèle une blessure autour de ton utilité dans les groupes. Tu as pu te sentir pas assez utile ou trop critique des autres.",
        "En traversant cette blessure, tu développes un don pour aider les groupes à fonctionner efficacement dans l'acceptation mutuelle.",
        "Cette position en maison XI peut avoir créé un sentiment de ne jamais en faire assez pour le collectif. Tu apprends le service joyeux.",
        "Sers un groupe sans juger son fonctionnement.",
        "Respire en te sentant utile sans épuisement.",
        "Où mon sens critique a-t-il nui à mes relations de groupe ? »"),

    ('virgo', 12): make_chiron_interp('virgo', 12,
        "Ta blessure touche le perfectionnisme spirituel — tu deviens guérisseur de l'acceptation totale.",
        "Chiron en Vierge dans ta maison XII révèle une blessure profonde autour de la perfection spirituelle. Tu peux te juger indigne spirituellement ou analyser excessivement.",
        "En traversant cette blessure, tu développes un don pour aider les autres à accepter leur imperfection humaine comme partie du divin.",
        "Cette position en maison XII porte une dimension karmique. Tu peux porter une culpabilité ancienne d'imperfection. Tu apprends la grâce de l'imperfection.",
        "Médite sur ton acceptation totale par l'univers.",
        "Respire en te sentant parfaitement imparfait.",
        "Quelle culpabilité d'imperfection porte mon âme ? »"),

    # === LIBRA (M1-M12) ===
    ('libra', 1): make_chiron_interp('libra', 1,
        "Ta blessure touche ta capacité à être aimé pour toi-même — tu deviens guérisseur des relations.",
        "Chiron en Balance dans ta maison I révèle une blessure profonde autour de l'amabilité et de l'acceptation. Tu as pu te sentir indigne d'amour ou obligé de plaire.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à s'aimer eux-mêmes et à créer des relations authentiques.",
        "Cette position en maison I rend la blessure très visible dans ton besoin d'approbation. Tu apprends à t'aimer sans condition extérieure.",
        "Fais quelque chose pour toi, même si ça ne plaît pas aux autres.",
        "Respire en te sentant digne d'amour, tel que tu es.",
        "Où me suis-je trahi pour être aimé ou accepté ? »"),

    ('libra', 2): make_chiron_interp('libra', 2,
        "Ta blessure touche la valeur dans le partage — tu deviens guérisseur de l'équité.",
        "Chiron en Balance dans ta maison II révèle une blessure autour du partage des ressources et de l'équilibre donner-recevoir. Tu as pu donner trop ou recevoir trop peu.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer des échanges équilibrés et à valoriser ce qu'ils apportent.",
        "Cette position en maison II peut créer un déséquilibre dans les échanges financiers. Tu apprends à recevoir autant que tu donnes.",
        "Reçois quelque chose avec gratitude sans te sentir redevable.",
        "Respire en te sentant digne de recevoir.",
        "Où ai-je donné plus que je ne recevais ? »"),

    ('libra', 3): make_chiron_interp('libra', 3,
        "Ta blessure touche la communication harmonieuse — tu deviens guérisseur du dialogue.",
        "Chiron en Balance dans ta maison III révèle une blessure autour de la communication et de l'harmonie verbale. Tu as pu avoir peur du conflit ou de dire ta vérité.",
        "En traversant cette blessure, tu développes un don pour aider les autres à communiquer avec authenticité tout en maintenant l'harmonie.",
        "Cette position en maison III peut avoir créé une difficulté à exprimer les désaccords. Tu apprends le conflit constructif.",
        "Exprime un désaccord avec bienveillance.",
        "Respire en te sentant capable de dire ta vérité avec grâce.",
        "Quelles vérités n'ai-je pas dites pour maintenir la paix ? »"),

    ('libra', 4): make_chiron_interp('libra', 4,
        "Ta blessure touche l'harmonie familiale — tu deviens guérisseur de la paix intérieure.",
        "Chiron en Balance dans ta maison IV révèle une blessure autour de l'harmonie au foyer. Tu as pu grandir dans un environnement conflictuel ou porter la responsabilité de la paix.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer la paix dans leur foyer et en eux-mêmes.",
        "Cette position en maison IV peut avoir fait de toi le médiateur familial. Tu apprends que la vraie paix ne vient pas du sacrifice de soi.",
        "Crée de l'harmonie chez toi sans te renier.",
        "Respire en te sentant en paix intérieurement.",
        "Quel rôle de pacificateur ai-je porté au détriment de moi-même ? »"),

    ('libra', 5): make_chiron_interp('libra', 5,
        "Ta blessure touche l'amour et la créativité — tu deviens guérisseur des amours artistiques.",
        "Chiron en Balance dans ta maison V révèle une blessure autour de l'amour romantique et de la création esthétique. Tu as pu être blessé en amour ou douter de ta beauté créative.",
        "En traversant cette blessure, tu développes un don pour aider les autres à aimer et créer de la beauté sans peur du rejet.",
        "Cette position en maison V peut avoir créé des déceptions amoureuses ou des doutes artistiques. Tu apprends l'amour de la beauté imparfaite.",
        "Crée quelque chose de beau ou aime sans peur.",
        "Respire en te sentant digne d'amour et de beauté.",
        "Quelles blessures amoureuses ou artistiques n'ai-je pas guéries ? »"),

    ('libra', 6): make_chiron_interp('libra', 6,
        "Ta blessure touche les relations au travail — tu deviens guérisseur des dynamiques professionnelles.",
        "Chiron en Balance dans ta maison VI révèle une blessure autour des relations avec les collègues et de l'équilibre au travail. Tu as pu te sentir exploité ou en conflit.",
        "En traversant cette blessure, tu développes un don pour améliorer les relations professionnelles et créer des environnements de travail harmonieux.",
        "Cette position en maison VI peut créer des difficultés relationnelles au travail. Tu apprends à maintenir l'harmonie sans te perdre.",
        "Établis une relation de travail équilibrée.",
        "Respire en te sentant respecté dans tes relations professionnelles.",
        "Où me suis-je effacé au travail pour maintenir la paix ? »"),

    ('libra', 7): make_chiron_interp('libra', 7,
        "Ta blessure touche le partenariat — tu deviens guérisseur des relations.",
        "Chiron en Balance dans ta maison VII (son domicile) révèle une blessure profonde autour des relations et du couple. Tu as pu être profondément blessé par un partenaire ou te perdre dans les relations.",
        "En traversant cette blessure, tu développes un don exceptionnel pour aider les autres à créer des partenariats sains et équilibrés.",
        "Cette position en maison VII intensifie la blessure relationnelle. Tu peux attirer des partenaires qui activent ta blessure. Tu apprends l'amour équilibré.",
        "Crée de l'équilibre dans une relation importante.",
        "Respire en te sentant entier, avec ou sans partenaire.",
        "Quelle blessure relationnelle majeure n'ai-je pas guérie ? »"),

    ('libra', 8): make_chiron_interp('libra', 8,
        "Ta blessure touche l'intimité profonde — tu deviens guérisseur des crises relationnelles.",
        "Chiron en Balance dans ta maison VIII révèle une blessure autour de l'intimité et des engagements profonds. Tu as pu être trahi ou blessé dans la vulnérabilité partagée.",
        "En traversant cette blessure, tu développes un don pour aider les autres à traverser les crises relationnelles et à reconstruire la confiance.",
        "Cette position en maison VIII peut créer une peur de l'intimité vraie. Tu apprends à te rendre vulnérable malgré les blessures passées.",
        "Partage une vulnérabilité avec quelqu'un de confiance.",
        "Respire en te sentant capable d'intimité profonde.",
        "Quelle trahison ou blessure intime n'ai-je pas guérie ? »"),

    ('libra', 9): make_chiron_interp('libra', 9,
        "Ta blessure touche tes croyances sur les relations — tu deviens guérisseur de la philosophie relationnelle.",
        "Chiron en Balance dans ta maison IX révèle une blessure autour de tes croyances sur l'amour et les relations. Tu as pu perdre foi dans le couple ou les partenariats.",
        "En traversant cette blessure, tu développes un don pour aider les autres à retrouver une vision saine des relations.",
        "Cette position en maison IX peut avoir créé un cynisme relationnel ou un idéalisme déçu. Tu apprends la sagesse de l'amour réaliste.",
        "Cultive une croyance positive sur les relations.",
        "Respire en renouvelant ta foi dans l'amour.",
        "Quelles croyances négatives sur l'amour porte-je encore ? »"),

    ('libra', 10): make_chiron_interp('libra', 10,
        "Ta blessure touche les relations professionnelles — tu deviens guérisseur des partenariats de travail.",
        "Chiron en Balance dans ta maison X révèle une blessure autour des relations dans ta carrière. Tu as pu être trahi par des associés ou avoir du mal à collaborer.",
        "En traversant cette blessure, tu développes un don pour créer des partenariats professionnels sains et aider les autres à collaborer.",
        "Cette position en maison X peut créer des difficultés dans les associations professionnelles. Tu apprends à choisir tes partenaires avec discernement.",
        "Construis une relation professionnelle équilibrée.",
        "Respire en te sentant capable de partenariats réussis.",
        "Quelles trahisons professionnelles n'ai-je pas guéries ? »"),

    ('libra', 11): make_chiron_interp('libra', 11,
        "Ta blessure touche ta place dans les groupes — tu deviens guérisseur des dynamiques collectives.",
        "Chiron en Balance dans ta maison XI révèle une blessure autour de ton appartenance aux groupes et de tes amitiés. Tu as pu te sentir exclu ou trop sacrifié au groupe.",
        "En traversant cette blessure, tu développes un don pour créer des communautés harmonieuses où chacun a sa place.",
        "Cette position en maison XI peut créer des difficultés à trouver ta place dans les groupes. Tu apprends l'équilibre individu-collectif.",
        "Trouve ta place unique dans un groupe.",
        "Respire en te sentant appartenir sans te perdre.",
        "Où me suis-je perdu ou senti exclu dans les groupes ? »"),

    ('libra', 12): make_chiron_interp('libra', 12,
        "Ta blessure touche l'amour universel — tu deviens guérisseur de l'harmonie cosmique.",
        "Chiron en Balance dans ta maison XII révèle une blessure profonde autour de l'amour et de l'harmonie au niveau de l'âme. Tu peux porter une solitude spirituelle.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver la paix intérieure et l'harmonie avec le tout.",
        "Cette position en maison XII porte une dimension karmique relationnelle. Tu peux porter des blessures d'amour de vies passées. Tu apprends l'amour divin.",
        "Médite sur l'amour universel qui t'entoure.",
        "Respire en te sentant aimé par l'univers.",
        "Quelle blessure d'amour porte mon âme depuis toujours ? »"),

    # === SCORPIO (M1-M12) ===
    ('scorpio', 1): make_chiron_interp('scorpio', 1,
        "Ta blessure touche ta survie et ton pouvoir — tu deviens guérisseur de la renaissance.",
        "Chiron en Scorpion dans ta maison I révèle une blessure profonde autour de la survie, du pouvoir et de la transformation. Tu as pu vivre des traumatismes qui ont menacé ton existence.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à traverser leurs crises et à renaître de leurs cendres.",
        "Cette position en maison I rend la blessure très visible dans ton intensité. Tu apprends que ta survie est ta plus grande force.",
        "Reconnais une crise que tu as traversée et honorée ta résilience.",
        "Respire en sentant ta capacité à renaître.",
        "Quel traumatisme ou quelle crise n'ai-je pas complètement guéri ? »"),

    ('scorpio', 2): make_chiron_interp('scorpio', 2,
        "Ta blessure touche le pouvoir et l'argent — tu deviens guérisseur de la transformation financière.",
        "Chiron en Scorpion dans ta maison II révèle une blessure autour du pouvoir lié aux ressources. Tu as pu vivre des pertes traumatiques ou des abus de pouvoir financier.",
        "En traversant cette blessure, tu développes un don pour aider les autres à transformer leur rapport au pouvoir et à l'argent.",
        "Cette position en maison II peut créer une peur de la perte ou un rapport intense à l'argent. Tu apprends que la vraie richesse est indestructible.",
        "Transforme ton rapport à une ressource avec conscience.",
        "Respire en relâchant la peur de la perte matérielle.",
        "Quelle perte financière ou trahison de pouvoir n'ai-je pas guérie ? »"),

    ('scorpio', 3): make_chiron_interp('scorpio', 3,
        "Ta blessure touche les secrets et les vérités — tu deviens guérisseur de la parole vraie.",
        "Chiron en Scorpion dans ta maison III révèle une blessure autour des secrets, des non-dits et des vérités difficiles. Tu as pu être blessé par des mots ou forcé au silence.",
        "En traversant cette blessure, tu développes un don pour aider les autres à dire l'indicible et à transformer par la parole.",
        "Cette position en maison III peut avoir créé une peur de dire ou d'entendre certaines vérités. Tu apprends le pouvoir guérisseur de la vérité.",
        "Dis une vérité que tu gardais enfouie.",
        "Respire en sentant le pouvoir libérateur de la parole vraie.",
        "Quels secrets ou non-dits empoisonnent encore ma vie ? »"),

    ('scorpio', 4): make_chiron_interp('scorpio', 4,
        "Ta blessure touche les ombres familiales — tu deviens guérisseur de la lignée.",
        "Chiron en Scorpion dans ta maison IV révèle une blessure autour des traumatismes familiaux et des secrets de lignée. Tu as pu porter des ombres qui ne t'appartiennent pas.",
        "En traversant cette blessure, tu développes un don pour aider les familles à guérir leurs traumatismes transgénérationnels.",
        "Cette position en maison IV peut avoir été marquée par des drames familiaux ou des abus. Tu deviens celui qui brise le cycle.",
        "Honore un traumatisme familial en le reconnaissant.",
        "Respire en te libérant des ombres de ta lignée.",
        "Quel traumatisme familial ou secret de lignée porte-je encore ? »"),

    ('scorpio', 5): make_chiron_interp('scorpio', 5,
        "Ta blessure touche la passion et la créativité — tu deviens guérisseur de la création intense.",
        "Chiron en Scorpion dans ta maison V révèle une blessure autour de la passion créative et amoureuse. Tu as pu vivre des amours destructrices ou une créativité bloquée par la peur.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer et aimer intensément sans se détruire.",
        "Cette position en maison V peut avoir été marquée par des passions douloureuses. Tu apprends à transformer l'intensité en création.",
        "Crée quelque chose à partir d'une émotion intense.",
        "Respire en canalisant ta passion de façon constructive.",
        "Quelles passions destructrices n'ai-je pas transformées ? »"),

    ('scorpio', 6): make_chiron_interp('scorpio', 6,
        "Ta blessure touche le pouvoir au travail — tu deviens guérisseur des dynamiques de pouvoir.",
        "Chiron en Scorpion dans ta maison VI révèle une blessure autour du pouvoir dans le travail quotidien. Tu as pu subir ou exercer un pouvoir toxique.",
        "En traversant cette blessure, tu développes un don pour aider les autres à transformer les dynamiques de pouvoir au travail.",
        "Cette position en maison VI peut avoir créé des expériences d'abus de pouvoir ou de manipulation au travail. Tu apprends le pouvoir sain.",
        "Transforme une dynamique de pouvoir toxique.",
        "Respire en exerçant ton pouvoir avec intégrité.",
        "Où ai-je subi ou exercé un pouvoir toxique au travail ? »"),

    ('scorpio', 7): make_chiron_interp('scorpio', 7,
        "Ta blessure touche l'intimité et la confiance — tu deviens guérisseur des relations profondes.",
        "Chiron en Scorpion dans ta maison VII révèle une blessure autour de l'intimité et de la confiance dans les relations. Tu as pu être trahi profondément par un partenaire.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconstruire la confiance après les trahisons.",
        "Cette position en maison VII peut attirer des partenaires qui activent tes peurs d'abandon ou de trahison. Tu apprends la vulnérabilité malgré les blessures.",
        "Fais confiance malgré ta peur de la trahison.",
        "Respire en te sentant capable d'intimité vraie.",
        "Quelle trahison relationnelle n'ai-je pas guérie ? »"),

    ('scorpio', 8): make_chiron_interp('scorpio', 8,
        "Ta blessure touche la mort et la transformation — tu deviens guérisseur chamanique.",
        "Chiron en Scorpion dans ta maison VIII (son domicile) révèle une blessure profonde autour de la mort, des pertes et des transformations. Tu as pu toucher le fond ou frôler la mort.",
        "En traversant cette blessure, tu développes un don exceptionnel pour accompagner les autres dans leurs passages et leurs morts symboliques.",
        "Cette position en maison VIII intensifie le contact avec les profondeurs. Tu es un initié aux mystères. Tu apprends à guider les autres dans les ténèbres.",
        "Accompagne quelqu'un dans une transition difficile.",
        "Respire en sentant ta connexion aux mystères de la vie et de la mort.",
        "Quelle mort ou transformation n'ai-je pas complètement traversée ? »"),

    ('scorpio', 9): make_chiron_interp('scorpio', 9,
        "Ta blessure touche les vérités profondes — tu deviens guérisseur de la sagesse occulte.",
        "Chiron en Scorpion dans ta maison IX révèle une blessure autour des croyances profondes et des vérités cachées. Tu as pu perdre ta foi ou être blessé par des dogmes.",
        "En traversant cette blessure, tu développes un don pour guider les autres vers les vérités profondes au-delà des apparences.",
        "Cette position en maison IX peut avoir créé une crise de foi ou une quête intense de vérité. Tu apprends à être un passeur de sagesse profonde.",
        "Explore une vérité profonde avec courage.",
        "Respire en sentant ta connexion à la sagesse cachée.",
        "Quelle crise de foi ou de croyance n'ai-je pas résolue ? »"),

    ('scorpio', 10): make_chiron_interp('scorpio', 10,
        "Ta blessure touche le pouvoir public — tu deviens guérisseur de la transformation sociale.",
        "Chiron en Scorpion dans ta maison X révèle une blessure autour du pouvoir et du statut. Tu as pu vivre des chutes ou des abus de pouvoir dans ta carrière.",
        "En traversant cette blessure, tu développes un don pour aider les autres à exercer le pouvoir avec intégrité et à transformer les structures.",
        "Cette position en maison X peut avoir été marquée par des expériences de pouvoir traumatiques. Tu apprends à transformer plutôt qu'à détruire.",
        "Utilise ton pouvoir pour transformer positivement.",
        "Respire en assumant ton pouvoir avec sagesse.",
        "Quel traumatisme de pouvoir ou de statut n'ai-je pas guéri ? »"),

    ('scorpio', 11): make_chiron_interp('scorpio', 11,
        "Ta blessure touche les trahisons collectives — tu deviens guérisseur des groupes.",
        "Chiron en Scorpion dans ta maison XI révèle une blessure autour des dynamiques de groupe et des trahisons collectives. Tu as pu être exclu ou trahi par un groupe.",
        "En traversant cette blessure, tu développes un don pour transformer les dynamiques de groupe toxiques et créer des communautés de confiance.",
        "Cette position en maison XI peut créer une méfiance des groupes ou des amitiés intenses et douloureuses. Tu apprends à transformer le collectif.",
        "Fais confiance à un groupe malgré tes blessures passées.",
        "Respire en te sentant capable d'appartenir sans trahison.",
        "Quelle trahison de groupe n'ai-je pas guérie ? »"),

    ('scorpio', 12): make_chiron_interp('scorpio', 12,
        "Ta blessure touche l'ombre collective — tu deviens guérisseur de l'âme du monde.",
        "Chiron en Scorpion dans ta maison XII révèle une blessure profonde et karmique autour des ténèbres de l'inconscient collectif. Tu peux porter les traumatismes de l'humanité.",
        "En traversant cette blessure, tu développes un don pour guérir les blessures les plus profondes de l'âme collective.",
        "Cette position en maison XII porte une dimension transpersonnelle intense. Tu es un guérisseur chamanique de l'ombre. Tu apprends à transmuter les ténèbres.",
        "Médite en transformant une ombre en lumière.",
        "Respire en sentant ta capacité à transmuter les ténèbres.",
        "Quelle blessure collective ou karmique porte mon âme ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in CHIRON_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'chiron',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP chiron/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='chiron',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT chiron/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
