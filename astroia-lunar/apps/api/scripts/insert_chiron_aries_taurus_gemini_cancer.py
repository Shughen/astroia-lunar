#!/usr/bin/env python3
"""Insert Chiron interpretations for Aries, Taurus, Gemini, Cancer (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_chiron_interp(sign_name, house, phrase, blessure, guerison, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'aries': '⚷ Chiron en Bélier',
        'taurus': '⚷ Chiron en Taureau',
        'gemini': '⚷ Chiron en Gémeaux',
        'cancer': '⚷ Chiron en Cancer',
    }
    sign_fr = {
        'aries': 'Bélier',
        'taurus': 'Taureau',
        'gemini': 'Gémeaux',
        'cancer': 'Cancer',
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
    # === ARIES (M1-M12) ===
    ('aries', 1): make_chiron_interp('aries', 1,
        "Ta blessure touche ton droit d'exister et de t'affirmer — tu deviens guérisseur de l'identité.",
        "Chiron en Bélier dans ta maison I révèle une blessure profonde autour de ton droit d'exister tel que tu es. Tu as pu te sentir illégitime dans ton affirmation, comme si tu n'avais pas le droit de prendre ta place.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à s'affirmer et à trouver leur identité. Tu deviens un catalyseur de courage pour ceux qui doutent d'eux-mêmes.",
        "Cette position en maison I rend la blessure très visible. Ta présence même peut activer cette vulnérabilité, mais aussi inspirer les autres par ton courage à être toi-même malgré la douleur.",
        "Affirme quelque chose de vrai sur toi, même si c'est inconfortable.",
        "Respire en te répétant : « J'ai le droit d'exister tel que je suis. »",
        "Quelle partie de moi ai-je du mal à affirmer par peur du rejet ? »"),

    ('aries', 2): make_chiron_interp('aries', 2,
        "Ta blessure touche ta capacité à valoriser ce que tu crées — tu deviens guérisseur de l'estime de soi.",
        "Chiron en Bélier dans ta maison II révèle une blessure autour de ta valeur personnelle et de ta capacité à générer des ressources par toi-même. Tu as pu douter de ta capacité à te débrouiller seul.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconnaître leur propre valeur et à développer leur autonomie financière et matérielle.",
        "Cette position en maison II lie la blessure identitaire aux ressources. Ton estime de toi peut fluctuer avec tes finances, mais tu apprends à valoriser qui tu es au-delà de ce que tu possèdes.",
        "Accomplis quelque chose par toi-même et reconnais ta valeur.",
        "Respire en te sentant capable et digne d'abondance.",
        "Où mon estime de moi dépend-elle trop de ce que je possède ou produis ? »"),

    ('aries', 3): make_chiron_interp('aries', 3,
        "Ta blessure touche ton droit de parler et d'avoir des idées — tu deviens guérisseur de la communication.",
        "Chiron en Bélier dans ta maison III révèle une blessure autour de ta parole et de tes idées. Tu as pu te sentir illégitime dans l'expression de tes pensées, comme si ta voix ne comptait pas.",
        "En traversant cette blessure, tu développes un don pour encourager les autres à s'exprimer et à défendre leurs idées, même face à l'opposition.",
        "Cette position en maison III peut avoir créé des difficultés avec les frères et sœurs ou dans l'apprentissage. Tu apprends que ta façon unique de penser est un cadeau.",
        "Exprime une idée que tu gardais pour toi.",
        "Respire en validant ta propre intelligence et tes propres opinions.",
        "Quelles idées n'osé-je pas exprimer par peur de ne pas être pris au sérieux ? »"),

    ('aries', 4): make_chiron_interp('aries', 4,
        "Ta blessure touche ton droit d'avoir des racines et une place — tu deviens guérisseur de l'appartenance.",
        "Chiron en Bélier dans ta maison IV révèle une blessure autour de ta place dans la famille et ton droit d'exister au sein du foyer. Tu as pu te sentir comme un intrus dans ta propre maison.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur place et à créer un foyer où ils se sentent légitimes d'exister.",
        "Cette position en maison IV lie la blessure identitaire aux racines. Tu peux aider ceux qui se sentent déracinés ou illégitimes dans leur famille à trouver leur ancrage.",
        "Crée un espace dans ton foyer qui est vraiment à toi.",
        "Respire en te sentant chez toi, exactement là où tu es.",
        "Où me suis-je senti illégitime dans ma propre famille ou mon propre foyer ? »"),

    ('aries', 5): make_chiron_interp('aries', 5,
        "Ta blessure touche ton droit de créer et d'être vu — tu deviens guérisseur de l'expression créative.",
        "Chiron en Bélier dans ta maison V révèle une blessure autour de ta créativité et ton droit de briller. Tu as pu te sentir illégitime dans tes expressions créatives ou amoureuses.",
        "En traversant cette blessure, tu développes un don pour encourager les autres à créer et à s'exprimer, même quand ils doutent de leur talent.",
        "Cette position en maison V peut avoir affecté tes amours ou ta relation aux enfants. Tu apprends que ta créativité unique mérite d'être vue.",
        "Crée quelque chose et partage-le, même imparfait.",
        "Respire en validant ton droit de créer et d'être vu.",
        "Quelles expressions créatives retiens-je par peur de ne pas être assez bon ? »"),

    ('aries', 6): make_chiron_interp('aries', 6,
        "Ta blessure touche ton droit de servir et d'être efficace — tu deviens guérisseur du travail.",
        "Chiron en Bélier dans ta maison VI révèle une blessure autour de ta capacité à travailler et à être utile. Tu as pu douter de ton efficacité ou de ta légitimité professionnelle.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur place dans le travail et à reconnaître leur contribution unique.",
        "Cette position en maison VI peut avoir créé des difficultés de santé liées au stress identitaire. Tu apprends que ta façon de servir est précieuse.",
        "Accomplis une tâche et reconnais sa valeur sans la minimiser.",
        "Respire en te sentant compétent et utile.",
        "Où me sens-je illégitime ou incompétent dans mon travail ? »"),

    ('aries', 7): make_chiron_interp('aries', 7,
        "Ta blessure touche ton droit d'exister dans les relations — tu deviens guérisseur du partenariat.",
        "Chiron en Bélier dans ta maison VII révèle une blessure autour de ton identité dans les relations. Tu as pu te perdre dans l'autre ou te sentir illégitime à affirmer tes besoins en couple.",
        "En traversant cette blessure, tu développes un don pour aider les autres à maintenir leur identité dans les relations et à s'affirmer face à leur partenaire.",
        "Cette position en maison VII peut créer des dynamiques où tu attires des partenaires qui t'aident à guérir cette blessure. Tu apprends l'équilibre entre le « je » et le « nous ».",
        "Affirme un besoin personnel dans une relation.",
        "Respire en te sentant entier, même en couple.",
        "Où me suis-je perdu dans mes relations par peur de m'affirmer ? »"),

    ('aries', 8): make_chiron_interp('aries', 8,
        "Ta blessure touche ton droit de te transformer — tu deviens guérisseur des crises.",
        "Chiron en Bélier dans ta maison VIII révèle une blessure autour de ta capacité à traverser les crises et les transformations. Tu as pu te sentir impuissant face aux épreuves.",
        "En traversant cette blessure, tu développes un don pour guider les autres à travers leurs propres crises et transformations, en leur montrant qu'ils peuvent survivre.",
        "Cette position en maison VIII peut avoir été activée par des pertes ou des traumas. Tu apprends que ta capacité à renaître est ta plus grande force.",
        "Affronte une peur profonde avec courage.",
        "Respire en sentant ta capacité à traverser les tempêtes.",
        "Quelle transformation évité-je par peur de ne pas y survivre ? »"),

    ('aries', 9): make_chiron_interp('aries', 9,
        "Ta blessure touche ton droit d'avoir une vision et des croyances — tu deviens guérisseur de la quête de sens.",
        "Chiron en Bélier dans ta maison IX révèle une blessure autour de tes croyances et ton droit d'avoir ta propre vision du monde. Tu as pu douter de ta sagesse ou de tes opinions.",
        "En traversant cette blessure, tu développes un don pour encourager les autres à trouver leur propre vérité et à oser défendre leurs croyances.",
        "Cette position en maison IX peut avoir créé des conflits avec l'autorité religieuse ou académique. Tu apprends que ta vérité compte autant que celle des autres.",
        "Affirme une croyance personnelle avec conviction.",
        "Respire en validant ta propre sagesse.",
        "Quelles croyances n'osé-je pas affirmer par peur d'être jugé ? »"),

    ('aries', 10): make_chiron_interp('aries', 10,
        "Ta blessure touche ton droit de réussir et d'avoir de l'autorité — tu deviens guérisseur de carrière.",
        "Chiron en Bélier dans ta maison X révèle une blessure autour de ta légitimité professionnelle. Tu as pu douter de ton droit d'occuper des positions de pouvoir ou de réussir.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur vocation et à assumer leur autorité, même face au syndrome de l'imposteur.",
        "Cette position en maison X peut avoir créé des difficultés avec les figures d'autorité ou les ambitions. Tu apprends que ton chemin vers le sommet est unique et valide.",
        "Assume une responsabilité ou une position d'autorité.",
        "Respire en te sentant légitime dans ta réussite.",
        "Où me sens-je illégitime dans ma carrière ou mon statut social ? »"),

    ('aries', 11): make_chiron_interp('aries', 11,
        "Ta blessure touche ton droit d'appartenir à un groupe — tu deviens guérisseur du collectif.",
        "Chiron en Bélier dans ta maison XI révèle une blessure autour de ta place dans les groupes et les amitiés. Tu as pu te sentir rejeté ou illégitime parmi les autres.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur place dans les groupes et à s'affirmer tout en appartenant.",
        "Cette position en maison XI peut avoir créé un sentiment d'être différent ou exclu. Tu apprends que ton unicité enrichit le collectif.",
        "Affirme ton unicité au sein d'un groupe.",
        "Respire en te sentant appartenir tout en étant unique.",
        "Où me suis-je senti rejeté ou en dehors des groupes ? »"),

    ('aries', 12): make_chiron_interp('aries', 12,
        "Ta blessure touche ton droit d'exister au niveau spirituel — tu deviens guérisseur de l'âme.",
        "Chiron en Bélier dans ta maison XII révèle une blessure profonde autour de ton existence même. Tu as pu porter une culpabilité ou un doute existentiel, comme si tu n'avais pas le droit d'être là.",
        "En traversant cette blessure, tu développes un don pour guider les autres vers la guérison de leurs blessures les plus profondes et les connecter à leur essence.",
        "Cette position en maison XII porte une dimension karmique. La blessure peut sembler venir de nulle part ou de très loin. Tu apprends que ton existence est un miracle.",
        "Médite sur ton droit d'exister, exactement tel que tu es.",
        "Respire en sentant ton existence comme un cadeau.",
        "Quelle culpabilité existentielle porte mon âme ? »"),

    # === TAURUS (M1-M12) ===
    ('taurus', 1): make_chiron_interp('taurus', 1,
        "Ta blessure touche ta valeur intrinsèque et ton rapport au corps — tu deviens guérisseur de l'estime de soi.",
        "Chiron en Taureau dans ta maison I révèle une blessure profonde autour de ta valeur personnelle et de ton corps. Tu as pu te sentir indigne, pas assez bien ou mal dans ta peau.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à reconnaître leur valeur intrinsèque et à habiter leur corps avec amour.",
        "Cette position en maison I rend la blessure très visible dans ton rapport à toi-même et à ton apparence. Tu apprends que ta valeur ne dépend pas de ce que tu possèdes ou de ton apparence.",
        "Regarde-toi dans un miroir avec compassion et amour.",
        "Respire en te répétant : « Je suis digne, tel que je suis. »",
        "Quelle partie de mon corps ou de moi-même ai-je du mal à accepter ? »"),

    ('taurus', 2): make_chiron_interp('taurus', 2,
        "Ta blessure touche ta capacité à avoir et à posséder — tu deviens guérisseur de l'abondance.",
        "Chiron en Taureau dans ta maison II (son domicile) révèle une blessure profonde autour des ressources et de la sécurité matérielle. Tu as pu vivre la privation ou le manque.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer l'abondance et à guérir leur relation à l'argent et aux possessions.",
        "Cette position en maison II intensifie la blessure matérielle. Tu peux avoir un rapport complexe à l'argent, oscillant entre manque et accumulation. Tu apprends la vraie sécurité.",
        "Donne ou reçois quelque chose avec gratitude.",
        "Respire en te sentant soutenu par l'univers.",
        "Quelle peur du manque porte encore mon inconscient ? »"),

    ('taurus', 3): make_chiron_interp('taurus', 3,
        "Ta blessure touche ta façon d'apprendre et de communiquer — tu deviens guérisseur de la parole.",
        "Chiron en Taureau dans ta maison III révèle une blessure autour de ta voix et de ta façon de communiquer. Tu as pu te sentir lent, bête ou incapable de t'exprimer.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur voix et à communiquer avec authenticité, sans se presser.",
        "Cette position en maison III peut avoir créé des difficultés d'apprentissage ou des comparaisons douloureuses. Tu apprends que ta façon de penser est précieuse.",
        "Exprime quelque chose à ton propre rythme, sans te presser.",
        "Respire en validant ta façon unique de communiquer.",
        "Où me suis-je senti stupide ou lent dans mon apprentissage ? »"),

    ('taurus', 4): make_chiron_interp('taurus', 4,
        "Ta blessure touche ton sentiment de sécurité au foyer — tu deviens guérisseur des racines.",
        "Chiron en Taureau dans ta maison IV révèle une blessure autour de la sécurité familiale et du foyer. Tu as pu manquer de stabilité ou te sentir en insécurité chez toi.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer un foyer sûr et à guérir leurs blessures liées au manque de sécurité.",
        "Cette position en maison IV peut avoir été marquée par l'instabilité financière familiale. Tu apprends à créer ta propre sécurité intérieure.",
        "Crée un moment de confort et de sécurité dans ton foyer.",
        "Respire en te sentant ancré et en sécurité.",
        "Quel manque de sécurité de mon enfance porte-je encore ? »"),

    ('taurus', 5): make_chiron_interp('taurus', 5,
        "Ta blessure touche ta capacité à jouir et à créer — tu deviens guérisseur du plaisir.",
        "Chiron en Taureau dans ta maison V révèle une blessure autour du plaisir et de la créativité. Tu as pu te sentir coupable de jouir ou indigne de créer de la beauté.",
        "En traversant cette blessure, tu développes un don pour aider les autres à s'autoriser le plaisir et à créer sans culpabilité.",
        "Cette position en maison V peut avoir affecté tes amours ou ta créativité par une peur de ne pas mériter le bonheur. Tu apprends que le plaisir est un droit.",
        "Offre-toi un petit plaisir sans culpabilité.",
        "Respire en t'autorisant à jouir de la vie.",
        "Quel plaisir me refuse-je par culpabilité ou sentiment d'indignité ? »"),

    ('taurus', 6): make_chiron_interp('taurus', 6,
        "Ta blessure touche ta valeur dans le travail — tu deviens guérisseur du quotidien.",
        "Chiron en Taureau dans ta maison VI révèle une blessure autour de ta valeur dans le travail quotidien. Tu as pu te sentir sous-payé, sous-estimé ou exploité.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconnaître leur valeur professionnelle et à créer un quotidien nourrissant.",
        "Cette position en maison VI peut avoir créé des problèmes de santé liés au stress du travail ou à la dévalorisation. Tu apprends à te valoriser au quotidien.",
        "Accomplis une tâche et reconnais sa vraie valeur.",
        "Respire en te sentant précieux dans ta contribution quotidienne.",
        "Où me suis-je senti sous-estimé ou exploité dans mon travail ? »"),

    ('taurus', 7): make_chiron_interp('taurus', 7,
        "Ta blessure touche ta valeur dans les relations — tu deviens guérisseur du couple.",
        "Chiron en Taureau dans ta maison VII révèle une blessure autour de ta valeur dans les partenariats. Tu as pu te sentir indigne d'amour ou rester dans des relations déséquilibrées.",
        "En traversant cette blessure, tu développes un don pour aider les couples à créer des relations où chacun est valorisé et respecté.",
        "Cette position en maison VII peut attirer des partenaires qui activent ta blessure de valeur. Tu apprends que tu mérites un amour qui te valorise.",
        "Affirme ta valeur dans une relation.",
        "Respire en te sentant digne de l'amour que tu donnes.",
        "Où ai-je accepté d'être dévalorisé dans mes relations ? »"),

    ('taurus', 8): make_chiron_interp('taurus', 8,
        "Ta blessure touche ta capacité à partager les ressources — tu deviens guérisseur des crises matérielles.",
        "Chiron en Taureau dans ta maison VIII révèle une blessure autour du partage des ressources et des pertes matérielles. Tu as pu vivre des trahisons financières ou des pertes traumatiques.",
        "En traversant cette blessure, tu développes un don pour aider les autres à traverser les crises financières et à reconstruire après les pertes.",
        "Cette position en maison VIII peut avoir créé une peur de l'intimité liée à la vulnérabilité matérielle. Tu apprends à faire confiance et à partager.",
        "Partage une ressource en faisant confiance.",
        "Respire en relâchant la peur de perdre.",
        "Quelle perte matérielle ou trahison financière n'ai-je pas encore guérie ? »"),

    ('taurus', 9): make_chiron_interp('taurus', 9,
        "Ta blessure touche ta valeur spirituelle — tu deviens guérisseur de la sagesse incarnée.",
        "Chiron en Taureau dans ta maison IX révèle une blessure autour de ta sagesse et de ta valeur philosophique. Tu as pu douter de ton droit à avoir des croyances ou à enseigner.",
        "En traversant cette blessure, tu développes un don pour aider les autres à incarner leur sagesse et à trouver une spiritualité ancrée dans le corps.",
        "Cette position en maison IX peut avoir créé un conflit entre matérialisme et spiritualité. Tu apprends que le sacré habite aussi la matière.",
        "Incarne une croyance dans un acte concret.",
        "Respire en sentant le sacré dans ton corps.",
        "Où ai-je séparé le spirituel du matériel ? »"),

    ('taurus', 10): make_chiron_interp('taurus', 10,
        "Ta blessure touche ta valeur professionnelle — tu deviens guérisseur de la reconnaissance.",
        "Chiron en Taureau dans ta maison X révèle une blessure autour de ta valeur et de ton statut. Tu as pu te sentir indigne de réussite ou mal rétribué pour ton travail.",
        "En traversant cette blessure, tu développes un don pour aider les autres à atteindre leur valeur professionnelle juste et à être reconnus à leur juste valeur.",
        "Cette position en maison X peut avoir créé des difficultés de carrière liées à la sous-estimation. Tu apprends à réclamer ce que tu vaux.",
        "Demande ce que tu vaux professionnellement.",
        "Respire en te sentant digne de réussite et de reconnaissance.",
        "Où me suis-je sous-vendu professionnellement ? »"),

    ('taurus', 11): make_chiron_interp('taurus', 11,
        "Ta blessure touche ta valeur dans les groupes — tu deviens guérisseur de l'appartenance.",
        "Chiron en Taureau dans ta maison XI révèle une blessure autour de ta valeur au sein des groupes. Tu as pu te sentir indigne d'appartenir ou rejeté pour ce que tu possèdes ou non.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur valeur dans le collectif et à contribuer de façon unique.",
        "Cette position en maison XI peut avoir créé des comparaisons douloureuses avec les autres. Tu apprends que ta contribution unique enrichit le groupe.",
        "Contribue au groupe avec ce que tu as, sans comparaison.",
        "Respire en te sentant précieux pour le collectif.",
        "Où me suis-je senti moins que les autres dans un groupe ? »"),

    ('taurus', 12): make_chiron_interp('taurus', 12,
        "Ta blessure touche ton droit d'avoir et d'être incarné — tu deviens guérisseur de l'incarnation.",
        "Chiron en Taureau dans ta maison XII révèle une blessure profonde et karmique autour du corps et de la matière. Tu peux porter une culpabilité liée aux possessions ou au plaisir.",
        "En traversant cette blessure, tu développes un don pour aider les autres à guérir leur relation au corps et à la matière, à réconcilier esprit et chair.",
        "Cette position en maison XII porte une dimension spirituelle. La blessure peut venir de vies passées ou de l'inconscient collectif. Tu apprends que l'incarnation est sacrée.",
        "Médite en honorant ton corps comme un temple.",
        "Respire en sentant le sacré dans la matière.",
        "Quelle culpabilité porte mon âme autour du corps ou des possessions ? »"),

    # === GEMINI (M1-M12) ===
    ('gemini', 1): make_chiron_interp('gemini', 1,
        "Ta blessure touche ton intelligence et ta façon de penser — tu deviens guérisseur de la communication.",
        "Chiron en Gémeaux dans ta maison I révèle une blessure profonde autour de ton intelligence et de ta façon de t'exprimer. Tu as pu te sentir incompris ou pas assez intelligent.",
        "En traversant cette blessure, tu développes un don unique pour aider les autres à communiquer et à valoriser leur propre intelligence.",
        "Cette position en maison I rend la blessure très visible dans ta façon de te présenter et de parler. Tu apprends que ta façon unique de penser est un cadeau.",
        "Exprime une idée personnelle avec confiance.",
        "Respire en validant ton intelligence unique.",
        "Quelle partie de mon intelligence ou de ma façon de penser ai-je du mal à accepter ? »"),

    ('gemini', 2): make_chiron_interp('gemini', 2,
        "Ta blessure touche ta capacité à valoriser tes idées — tu deviens guérisseur de la valeur intellectuelle.",
        "Chiron en Gémeaux dans ta maison II révèle une blessure autour de la valeur de tes idées et de ta capacité à les monétiser. Tu as pu te sentir incapable de vivre de ton intelligence.",
        "En traversant cette blessure, tu développes un don pour aider les autres à reconnaître la valeur de leurs idées et à en vivre.",
        "Cette position en maison II peut créer un sentiment que tes talents mentaux ne valent rien. Tu apprends que tes idées ont de la valeur.",
        "Valorise une de tes idées concrètement.",
        "Respire en te sentant riche de tes idées.",
        "Où ai-je dévalorisé mes capacités intellectuelles ? »"),

    ('gemini', 3): make_chiron_interp('gemini', 3,
        "Ta blessure touche ta parole et ton apprentissage — tu deviens guérisseur des mots.",
        "Chiron en Gémeaux dans ta maison III (son domicile) révèle une blessure profonde autour de la communication et de l'apprentissage. Tu as pu avoir des difficultés scolaires ou verbales.",
        "En traversant cette blessure, tu développes un don exceptionnel pour aider les autres à communiquer, apprendre et surmonter leurs blocages verbaux.",
        "Cette position en maison III intensifie la blessure de communication. Tu peux avoir vécu des moqueries ou des incompréhensions. Tu deviens expert en connexion par les mots.",
        "Communique quelque chose de vulnérable avec authenticité.",
        "Respire en honorant ta façon unique de parler et penser.",
        "Quel traumatisme de communication ou d'apprentissage n'ai-je pas guéri ? »"),

    ('gemini', 4): make_chiron_interp('gemini', 4,
        "Ta blessure touche la communication familiale — tu deviens guérisseur des dialogues familiaux.",
        "Chiron en Gémeaux dans ta maison IV révèle une blessure autour de la communication au sein de la famille. Tu as pu te sentir incompris ou pas écouté chez toi.",
        "En traversant cette blessure, tu développes un don pour aider les familles à communiquer et à créer des espaces de dialogue authentique.",
        "Cette position en maison IV peut avoir créé un sentiment d'être le « différent » de la famille. Tu apprends à créer un foyer où la parole circule.",
        "Initie une conversation authentique dans ta famille.",
        "Respire en te sentant entendu et compris.",
        "Quels non-dits familiaux portent encore ma blessure ? »"),

    ('gemini', 5): make_chiron_interp('gemini', 5,
        "Ta blessure touche ta créativité intellectuelle — tu deviens guérisseur de l'expression créative.",
        "Chiron en Gémeaux dans ta maison V révèle une blessure autour de la créativité et du jeu intellectuel. Tu as pu te sentir pas assez créatif ou brillant.",
        "En traversant cette blessure, tu développes un don pour aider les autres à exprimer leur créativité et à jouer avec les idées sans peur du jugement.",
        "Cette position en maison V peut avoir affecté tes amours par une peur de ne pas être assez intéressant. Tu apprends que ta créativité mentale brille.",
        "Crée quelque chose de ludique avec les mots ou les idées.",
        "Respire en te sentant créatif et brillant.",
        "Où ma peur de ne pas être assez intéressant a-t-elle limité ma créativité ? »"),

    ('gemini', 6): make_chiron_interp('gemini', 6,
        "Ta blessure touche ta communication au travail — tu deviens guérisseur du quotidien verbal.",
        "Chiron en Gémeaux dans ta maison VI révèle une blessure autour de la communication professionnelle. Tu as pu te sentir incompris ou mal à l'aise dans les échanges au travail.",
        "En traversant cette blessure, tu développes un don pour améliorer la communication dans les équipes et créer des environnements de travail où la parole circule.",
        "Cette position en maison VI peut créer des tensions nerveuses ou des difficultés avec les collègues. Tu apprends à communiquer avec efficacité et empathie.",
        "Améliore un échange professionnel par une communication claire.",
        "Respire en relâchant le stress de la communication au travail.",
        "Où la communication au travail est-elle source de stress pour moi ? »"),

    ('gemini', 7): make_chiron_interp('gemini', 7,
        "Ta blessure touche la communication en couple — tu deviens guérisseur du dialogue relationnel.",
        "Chiron en Gémeaux dans ta maison VII révèle une blessure autour de la communication dans les relations. Tu as pu te sentir incompris par tes partenaires ou avoir peur de parler.",
        "En traversant cette blessure, tu développes un don pour aider les couples à communiquer et à créer des ponts de compréhension.",
        "Cette position en maison VII peut attirer des partenaires avec qui la communication est difficile. Tu apprends à créer des espaces de dialogue dans l'intimité.",
        "Partage quelque chose de vulnérable avec un partenaire.",
        "Respire en te sentant capable de vraie communication intime.",
        "Quels non-dits empoisonnent ou ont empoisonné mes relations ? »"),

    ('gemini', 8): make_chiron_interp('gemini', 8,
        "Ta blessure touche la parole profonde — tu deviens guérisseur des secrets.",
        "Chiron en Gémeaux dans ta maison VIII révèle une blessure autour des communications profondes et des secrets. Tu as pu être blessé par des mots ou des révélations traumatiques.",
        "En traversant cette blessure, tu développes un don pour aider les autres à dire l'indicible et à transformer par la parole les expériences les plus sombres.",
        "Cette position en maison VIII peut avoir créé une peur de certains sujets tabous. Tu apprends le pouvoir de guérison des mots vrais.",
        "Dis une vérité que tu gardais enfouie.",
        "Respire en sentant le pouvoir libérateur de la parole vraie.",
        "Quels mots n'ai-je pas osé prononcer de peur de leurs conséquences ? »"),

    ('gemini', 9): make_chiron_interp('gemini', 9,
        "Ta blessure touche ta capacité à enseigner et partager ta vision — tu deviens guérisseur de la transmission.",
        "Chiron en Gémeaux dans ta maison IX révèle une blessure autour de l'enseignement et de la communication de tes croyances. Tu as pu douter de ta légitimité à enseigner.",
        "En traversant cette blessure, tu développes un don pour transmettre des connaissances et aider les autres à trouver leur propre façon d'enseigner.",
        "Cette position en maison IX peut avoir créé des conflits avec des enseignants ou des institutions. Tu apprends que ta voix d'enseignant est unique et précieuse.",
        "Partage un enseignement avec confiance.",
        "Respire en validant ta capacité à transmettre.",
        "Où me suis-je senti illégitime à enseigner ou partager ma vision ? »"),

    ('gemini', 10): make_chiron_interp('gemini', 10,
        "Ta blessure touche ta parole publique — tu deviens guérisseur de la communication professionnelle.",
        "Chiron en Gémeaux dans ta maison X révèle une blessure autour de ta voix publique et professionnelle. Tu as pu avoir peur de parler en public ou douter de ta crédibilité.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur voix professionnelle et à communiquer avec autorité.",
        "Cette position en maison X peut avoir créé des difficultés de carrière liées à la communication. Tu apprends à porter ta voix dans le monde.",
        "Communique professionnellement avec confiance et autorité.",
        "Respire en te sentant crédible et entendu.",
        "Où ma peur de parler en public a-t-elle limité ma carrière ? »"),

    ('gemini', 11): make_chiron_interp('gemini', 11,
        "Ta blessure touche ta communication dans les groupes — tu deviens guérisseur des conversations collectives.",
        "Chiron en Gémeaux dans ta maison XI révèle une blessure autour de ta parole dans les groupes. Tu as pu te sentir exclu des conversations ou pas entendu dans les collectifs.",
        "En traversant cette blessure, tu développes un don pour faciliter les communications de groupe et créer des espaces où chacun peut s'exprimer.",
        "Cette position en maison XI peut avoir créé un sentiment d'être le mal compris du groupe. Tu apprends à créer des connexions par les mots.",
        "Facilite une conversation de groupe inclusive.",
        "Respire en te sentant connecté aux autres par les idées.",
        "Où me suis-je senti exclu des conversations collectives ? »"),

    ('gemini', 12): make_chiron_interp('gemini', 12,
        "Ta blessure touche l'indicible et les pensées cachées — tu deviens guérisseur du mental inconscient.",
        "Chiron en Gémeaux dans ta maison XII révèle une blessure profonde autour de pensées que tu n'as jamais pu exprimer. Tu peux porter des mots non-dits qui pèsent sur ton inconscient.",
        "En traversant cette blessure, tu développes un don pour aider les autres à exprimer l'inexprimable et à guérir par la parole intérieure.",
        "Cette position en maison XII peut créer une hyperactivité mentale ou des pensées obsédantes. Tu apprends le silence qui guérit.",
        "Écris les pensées que tu n'oses pas dire à voix haute.",
        "Respire en laissant ton mental se calmer dans le silence.",
        "Quelles pensées restent enfermées dans mon inconscient ? »"),

    # === CANCER (M1-M12) ===
    ('cancer', 1): make_chiron_interp('cancer', 1,
        "Ta blessure touche ton besoin d'être aimé et nourri — tu deviens guérisseur de la maternance.",
        "Chiron en Cancer dans ta maison I révèle une blessure profonde autour de ton besoin d'être aimé et pris en charge. Tu as pu manquer de nourriture émotionnelle ou te sentir abandonné.",
        "En traversant cette blessure, tu développes un don unique pour nourrir les autres et créer des espaces de sécurité émotionnelle.",
        "Cette position en maison I rend la blessure très visible dans ta sensibilité. Tu apprends que prendre soin des autres est ta force, pas ta faiblesse.",
        "Offre du soin à quelqu'un et accepte d'en recevoir aussi.",
        "Respire en te sentant aimé et en sécurité.",
        "Quel manque d'amour ou de soin de mon enfance porte-je encore ? »"),

    ('cancer', 2): make_chiron_interp('cancer', 2,
        "Ta blessure touche ta sécurité émotionnelle et matérielle — tu deviens guérisseur de l'abondance nourricière.",
        "Chiron en Cancer dans ta maison II révèle une blessure autour de la sécurité émotionnelle liée aux ressources. Tu as pu associer l'amour à la provision matérielle.",
        "En traversant cette blessure, tu développes un don pour aider les autres à créer une sécurité qui nourrit à la fois le corps et l'âme.",
        "Cette position en maison II peut créer une peur du manque liée au manque d'amour. Tu apprends que l'abondance vraie est émotionnelle.",
        "Nourris-toi de quelque chose qui réconforte ton cœur.",
        "Respire en te sentant soutenu émotionnellement et matériellement.",
        "Comment mon rapport à l'argent reflète-t-il mon besoin d'amour ? »"),

    ('cancer', 3): make_chiron_interp('cancer', 3,
        "Ta blessure touche ta communication émotionnelle — tu deviens guérisseur du dialogue du cœur.",
        "Chiron en Cancer dans ta maison III révèle une blessure autour de l'expression de tes émotions. Tu as pu apprendre à cacher ce que tu ressens ou te sentir incompris.",
        "En traversant cette blessure, tu développes un don pour aider les autres à communiquer leurs émotions et à créer des espaces d'échange sincère.",
        "Cette position en maison III peut avoir créé des difficultés avec les frères et sœurs autour des émotions. Tu apprends à parler depuis le cœur.",
        "Exprime une émotion que tu gardais pour toi.",
        "Respire en te sentant libre d'exprimer ce que tu ressens.",
        "Quelles émotions n'ai-je jamais osé exprimer à ma famille proche ? »"),

    ('cancer', 4): make_chiron_interp('cancer', 4,
        "Ta blessure touche ta famille et ton foyer — tu deviens guérisseur des racines.",
        "Chiron en Cancer dans ta maison IV (son domicile) révèle une blessure profonde autour de la famille, de la mère et du foyer. Tu as pu manquer de présence maternelle ou de sécurité au foyer.",
        "En traversant cette blessure, tu développes un don exceptionnel pour créer des foyers guérisseurs et aider les autres à guérir leurs blessures familiales.",
        "Cette position en maison IV intensifie la blessure maternelle et familiale. Tu peux devenir le guérisseur de ta lignée, celui qui brise les schémas.",
        "Crée un moment de chaleur et de sécurité dans ton foyer.",
        "Respire en te sentant chez toi, peu importe où tu es.",
        "Quelle blessure familiale ou maternelle n'ai-je pas encore guérie ? »"),

    ('cancer', 5): make_chiron_interp('cancer', 5,
        "Ta blessure touche l'amour que tu donnes et reçois — tu deviens guérisseur de l'amour inconditionnel.",
        "Chiron en Cancer dans ta maison V révèle une blessure autour de l'amour romantique et de la création. Tu as pu te sentir indigne d'amour ou avoir peur d'aimer.",
        "En traversant cette blessure, tu développes un don pour aider les autres à aimer inconditionnellement et à créer depuis le cœur.",
        "Cette position en maison V peut affecter tes amours et ta relation aux enfants. Tu apprends que ton amour est un cadeau précieux.",
        "Aime quelqu'un ou quelque chose sans condition.",
        "Respire en te sentant digne d'amour.",
        "Où ma peur d'être blessé m'empêche-t-elle d'aimer pleinement ? »"),

    ('cancer', 6): make_chiron_interp('cancer', 6,
        "Ta blessure touche ta façon de prendre soin — tu deviens guérisseur du service nourricier.",
        "Chiron en Cancer dans ta maison VI révèle une blessure autour du soin et du service quotidien. Tu as pu te sentir obligé de prendre soin des autres ou négligé dans tes besoins.",
        "En traversant cette blessure, tu développes un don pour prendre soin des autres de façon saine et pour enseigner les limites dans le service.",
        "Cette position en maison VI peut créer des problèmes de santé liés aux émotions ou à l'épuisement du don. Tu apprends à prendre soin de toi aussi.",
        "Prends soin de toi comme tu prendrais soin d'un être aimé.",
        "Respire en te donnant la permission de recevoir du soin.",
        "Où me suis-je épuisé à prendre soin des autres en oubliant mes besoins ? »"),

    ('cancer', 7): make_chiron_interp('cancer', 7,
        "Ta blessure touche l'intimité en couple — tu deviens guérisseur des relations nourricières.",
        "Chiron en Cancer dans ta maison VII révèle une blessure autour de l'intimité et du soin dans les relations. Tu as pu te sentir pas assez nourri ou trop dépendant.",
        "En traversant cette blessure, tu développes un don pour aider les couples à créer des relations où chacun nourrit l'autre de façon équilibrée.",
        "Cette position en maison VII peut attirer des partenaires qui activent tes besoins de sécurité émotionnelle. Tu apprends l'interdépendance saine.",
        "Nourris et laisse-toi nourrir dans une relation.",
        "Respire en te sentant en sécurité dans l'intimité.",
        "Comment mes besoins émotionnels affectent-ils mes relations ? »"),

    ('cancer', 8): make_chiron_interp('cancer', 8,
        "Ta blessure touche les pertes émotionnelles — tu deviens guérisseur du deuil.",
        "Chiron en Cancer dans ta maison VIII révèle une blessure autour des pertes émotionnelles et des séparations. Tu as pu vivre des abandons traumatiques.",
        "En traversant cette blessure, tu développes un don pour accompagner les autres dans leurs deuils et leurs transformations émotionnelles.",
        "Cette position en maison VIII peut avoir été marquée par des pertes familiales importantes. Tu apprends que l'amour transcende la séparation.",
        "Honore une perte avec amour et gratitude.",
        "Respire en sentant que l'amour ne meurt jamais.",
        "Quel deuil émotionnel n'ai-je pas encore traversé complètement ? »"),

    ('cancer', 9): make_chiron_interp('cancer', 9,
        "Ta blessure touche ton sentiment d'appartenance au monde — tu deviens guérisseur de la famille cosmique.",
        "Chiron en Cancer dans ta maison IX révèle une blessure autour de ton sentiment d'appartenance à une communauté plus large. Tu as pu te sentir étranger partout.",
        "En traversant cette blessure, tu développes un don pour aider les autres à trouver leur famille spirituelle et à se sentir chez eux partout.",
        "Cette position en maison IX peut avoir créé des difficultés à s'intégrer dans d'autres cultures ou croyances. Tu apprends que la terre entière est ta maison.",
        "Trouve un sentiment de chez-toi dans un lieu nouveau.",
        "Respire en te sentant appartenir à la famille humaine.",
        "Où me suis-je senti étranger ou non-appartenant ? »"),

    ('cancer', 10): make_chiron_interp('cancer', 10,
        "Ta blessure touche le rôle parental dans ta carrière — tu deviens guérisseur de la vocation nourricière.",
        "Chiron en Cancer dans ta maison X révèle une blessure autour du rôle de « parent » dans ta carrière ou de l'équilibre travail-famille. Tu as pu sacrifier l'un pour l'autre.",
        "En traversant cette blessure, tu développes un don pour aider les autres à intégrer leur côté nourricier dans leur carrière.",
        "Cette position en maison X peut avoir créé des conflits entre ambition et famille. Tu apprends à nourrir le monde par ton travail.",
        "Intègre une qualité nourricière dans ton travail.",
        "Respire en te sentant capable de concilier carrière et cœur.",
        "Comment ai-je sacrifié ma vie familiale pour ma carrière ou inversement ? »"),

    ('cancer', 11): make_chiron_interp('cancer', 11,
        "Ta blessure touche ton appartenance aux groupes — tu deviens guérisseur de la famille choisie.",
        "Chiron en Cancer dans ta maison XI révèle une blessure autour de ton appartenance aux groupes et aux amitiés. Tu as pu te sentir pas assez nourri par tes amis ou exclu.",
        "En traversant cette blessure, tu développes un don pour créer des communautés nourricières où chacun se sent comme en famille.",
        "Cette position en maison XI peut avoir créé un sentiment que les groupes ne peuvent pas répondre à tes besoins émotionnels. Tu apprends à créer ta famille choisie.",
        "Crée un moment de connexion émotionnelle dans un groupe.",
        "Respire en te sentant appartenir à une communauté d'âmes.",
        "Où me suis-je senti émotionnellement négligé dans les groupes ? »"),

    ('cancer', 12): make_chiron_interp('cancer', 12,
        "Ta blessure touche la mère cosmique et l'amour universel — tu deviens guérisseur de l'âme collective.",
        "Chiron en Cancer dans ta maison XII révèle une blessure profonde et karmique autour de la maternance et de l'amour. Tu peux porter les blessures maternelles de ta lignée ou de l'humanité.",
        "En traversant cette blessure, tu développes un don pour guérir les blessures les plus profondes de l'âme et offrir un amour universel.",
        "Cette position en maison XII porte une dimension transpersonnelle. Tu peux ressentir les émotions collectives. Tu apprends à être le guérisseur de la grande famille humaine.",
        "Médite en envoyant de l'amour à tous les êtres.",
        "Respire en sentant l'amour universel qui te porte.",
        "Quelle blessure collective ou ancestrale porte mon âme ? »"),
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
