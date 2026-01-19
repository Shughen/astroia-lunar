#!/usr/bin/env python3
"""Insert Lilith interpretations for Leo, Virgo, Libra, Scorpio (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_lilith_interp(sign_name, house, phrase, ombre, pouvoir, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'leo': '⚸ Lilith en Lion',
        'virgo': '⚸ Lilith en Vierge',
        'libra': '⚸ Lilith en Balance',
        'scorpio': '⚸ Lilith en Scorpion',
    }
    sign_fr = {
        'leo': 'Lion',
        'virgo': 'Vierge',
        'libra': 'Balance',
        'scorpio': 'Scorpion',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ton ombre
{ombre}

## Ton pouvoir brut
{pouvoir}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

LILITH_INTERPRETATIONS = {
    # === LEO (M1-M12) ===
    ('leo', 1): make_lilith_interp('leo', 1,
        "Ton ombre se loge dans l'égo et le besoin de briller — ton pouvoir est celui de la lumière sauvage.",
        "Lilith en Lion dans ta maison I place ton ombre dans ton identité et ton besoin de reconnaissance. Tu peux avoir refoulé ton désir de briller ou au contraire un égo démesuré.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de présence magnétique et de rayonnement brut. Tu brilles d'une lumière indomptée.",
        "En maison I, cette énergie est très visible. Tu peux osciller entre l'effacement et la tyrannie de l'égo. Trouve ta lumière authentique.",
        "Brille sans chercher l'approbation.",
        "Respire en sentant ta lumière intérieure.",
        "Quelle honte ou excès ai-je autour de mon besoin de briller ? »"),

    ('leo', 2): make_lilith_interp('leo', 2,
        "Ton ombre se loge dans l'orgueil de posséder — ton pouvoir est celui de la générosité royale.",
        "Lilith en Lion dans ta maison II place ton ombre dans ta relation aux possessions et à la valeur. Tu peux avoir un orgueil autour de ce que tu possèdes ou une honte de tes désirs.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de création de valeur magnifique. Tu génères de la richesse avec générosité royale.",
        "En maison II, cette énergie peut créer un rapport orgueilleux à l'argent. Apprends la générosité sans attente de reconnaissance.",
        "Donne généreusement sans attendre de louanges.",
        "Respire en te sentant riche de ta lumière.",
        "Quel orgueil ou honte autour de mes possessions ai-je refoulé ? »"),

    ('leo', 3): make_lilith_interp('leo', 3,
        "Ton ombre se loge dans la parole dramatique — ton pouvoir est celui de l'expression théâtrale.",
        "Lilith en Lion dans ta maison III place ton ombre dans ta communication. Tu peux avoir refoulé un côté dramatique ou une tendance à exagérer pour être vu.",
        "En intégrant cette Lilith, tu accèdes à une parole captivante et théâtrale. Tu peux inspirer et captiver par tes mots.",
        "En maison III, cette énergie peut créer des communications excessives ou un besoin d'être le centre de l'attention verbale. Parle pour illuminer, pas pour dominer.",
        "Exprime-toi avec théâtralité assumée.",
        "Respire en honorant ta parole créatrice.",
        "Comment mon besoin de briller affecte-t-il ma communication ? »"),

    ('leo', 4): make_lilith_interp('leo', 4,
        "Ton ombre se loge dans la fierté familiale — ton pouvoir est celui de créer un foyer royal.",
        "Lilith en Lion dans ta maison IV place ton ombre dans ta famille et ton foyer. Tu peux avoir des conflits d'orgueil familiaux ou un besoin d'être le centre de la famille.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer un foyer lumineux et créatif. Tu es le cœur rayonnant de ta famille.",
        "En maison IV, cette énergie peut créer des drames familiaux liés à l'égo. Transforme l'orgueil en générosité familiale.",
        "Crée de la joie et de la lumière dans ton foyer.",
        "Respire en étant le soleil de ta famille sans l'éclipser.",
        "Quel orgueil ou drame familial ai-je refoulé ? »"),

    ('leo', 5): make_lilith_interp('leo', 5,
        "Ton ombre se loge dans l'égo créatif et amoureux — ton pouvoir est celui de la création souveraine.",
        "Lilith en Lion dans ta maison V (son domicile) place ton ombre dans ta créativité et tes amours. Tu peux avoir un égo démesuré dans la création ou l'amour.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir créatif et amoureux exceptionnel. Tu crées et aimes avec une passion royale.",
        "En maison V, cette énergie est particulièrement puissante. Tu peux créer des drames amoureux ou de la création grandiose. Canalise ta flamme.",
        "Crée quelque chose de grandiose sans attente d'applaudissements.",
        "Respire en sentant ta puissance créatrice.",
        "Quel égo créatif ou amoureux ai-je refoulé ou excessivement développé ? »"),

    ('leo', 6): make_lilith_interp('leo', 6,
        "Ton ombre se loge dans l'orgueil au travail — ton pouvoir est celui du service inspirant.",
        "Lilith en Lion dans ta maison VI place ton ombre dans ton rapport au travail. Tu peux avoir un orgueil qui refuse les tâches humbles ou un besoin de briller au quotidien.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer le travail en création. Tu apportes de la lumière dans les tâches ordinaires.",
        "En maison VI, cette énergie peut créer des conflits au travail liés à l'égo. Apprends à servir avec noblesse sans orgueil.",
        "Accomplis une tâche humble avec dignité royale.",
        "Respire en trouvant la noblesse dans le service.",
        "Où mon orgueil m'empêche-t-il de servir humblement ? »"),

    ('leo', 7): make_lilith_interp('leo', 7,
        "Ton ombre se loge dans l'égo en relation — ton pouvoir est celui de l'amour généreux.",
        "Lilith en Lion dans ta maison VII place ton ombre dans tes relations. Tu peux avoir des luttes d'égo avec tes partenaires ou attirer des partenaires narcissiques.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer des relations généreuses et lumineuses. Tu aimes avec magnificence.",
        "En maison VII, cette énergie peut créer des drames relationnels liés à l'égo. Apprends à briller ensemble, pas l'un contre l'autre.",
        "Laisse ton partenaire briller aussi.",
        "Respire en partageant la lumière dans tes relations.",
        "Quelles luttes d'égo ai-je dans mes relations ? »"),

    ('leo', 8): make_lilith_interp('leo', 8,
        "Ton ombre se loge dans l'orgueil face à la mort — ton pouvoir est celui de la transformation lumineuse.",
        "Lilith en Lion dans ta maison VIII place ton ombre dans ta relation au pouvoir, à la sexualité et à la mort. Tu peux avoir un égo autour du contrôle ou de la puissance sexuelle.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformation qui conserve la lumière. Tu renaîs en gardant ta flamme.",
        "En maison VIII, cette énergie peut créer des luttes de pouvoir intenses. Apprends à lâcher l'égo pour mieux renaître.",
        "Lâche ton égo dans une situation de transformation.",
        "Respire en laissant ta lumière survivre aux ténèbres.",
        "Quel égo autour du pouvoir ou de la sexualité ai-je refoulé ? »"),

    ('leo', 9): make_lilith_interp('leo', 9,
        "Ton ombre se loge dans l'orgueil spirituel — ton pouvoir est celui de l'enseignant charismatique.",
        "Lilith en Lion dans ta maison IX place ton ombre dans tes croyances et ton enseignement. Tu peux avoir un égo autour de ta vision ou de ton rôle de guide.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'enseigner et d'inspirer avec charisme. Tu transmets avec passion.",
        "En maison IX, cette énergie peut créer du prosélytisme orgueilleux. Enseigne pour élever, pas pour être admiré.",
        "Partage ta vision avec passion et humilité.",
        "Respire en étant un canal lumineux sans égo.",
        "Quel orgueil spirituel ou philosophique ai-je refoulé ? »"),

    ('leo', 10): make_lilith_interp('leo', 10,
        "Ton ombre se loge dans l'ambition de gloire — ton pouvoir est celui du leader inspirant.",
        "Lilith en Lion dans ta maison X place ton ombre dans ta carrière et ton statut. Tu peux avoir une ambition de célébrité refoulée ou un besoin excessif de reconnaissance publique.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de leadership charismatique. Tu peux inspirer et guider avec ta lumière.",
        "En maison X, cette énergie peut créer une carrière de star ou des chutes d'égo. Construis ta réputation sur l'authenticité.",
        "Assume ton leadership avec charisme.",
        "Respire en brillant professionnellement sans égo excessif.",
        "Quelle ambition de gloire ou de célébrité ai-je refoulée ? »"),

    ('leo', 11): make_lilith_interp('leo', 11,
        "Ton ombre se loge dans l'égo de groupe — ton pouvoir est celui de rassembler et inspirer.",
        "Lilith en Lion dans ta maison XI place ton ombre dans tes groupes et tes idéaux. Tu peux avoir besoin d'être la star du groupe ou rejeter les groupes qui ne t'admirent pas.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de rassembler et d'inspirer les collectifs. Tu es le cœur lumineux des groupes.",
        "En maison XI, cette énergie peut créer des conflits d'égo dans les groupes. Brille pour élever le collectif, pas pour le dominer.",
        "Inspire un groupe avec ta lumière.",
        "Respire en partageant ta lumière avec le collectif.",
        "Comment mon égo affecte-t-il mes relations de groupe ? »"),

    ('leo', 12): make_lilith_interp('leo', 12,
        "Ton ombre se loge dans l'égo spirituel caché — ton pouvoir est celui de la lumière intérieure.",
        "Lilith en Lion dans ta maison XII place ton ombre dans l'inconscient et l'égo caché. Tu peux avoir un orgueil spirituel refoulé ou une lumière que tu n'oses pas montrer.",
        "En intégrant cette Lilith, tu accèdes à une lumière intérieure puissante qui n'a pas besoin d'être vue pour briller.",
        "En maison XII, cette énergie peut créer un conflit entre égo et dissolution. Apprends à briller dans l'invisible.",
        "Médite sur ta lumière intérieure sans besoin de la montrer.",
        "Respire en rayonnant de l'intérieur.",
        "Quelle lumière ai-je cachée par peur ou honte ? »"),

    # === VIRGO (M1-M12) ===
    ('virgo', 1): make_lilith_interp('virgo', 1,
        "Ton ombre se loge dans le perfectionnisme et la critique — ton pouvoir est celui de l'analyse pénétrante.",
        "Lilith en Vierge dans ta maison I place ton ombre dans ton identité et ta tendance au perfectionnisme. Tu peux avoir une autocritique féroce ou une exigence excessive.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'analyse et de discernement exceptionnels. Tu peux voir ce que personne ne voit.",
        "En maison I, cette énergie est très visible. Tu peux paraître critique ou distant. Transforme l'analyse en service.",
        "Accepte une de tes imperfections.",
        "Respire en relâchant le jugement sur toi-même.",
        "Quelle autocritique féroce habite mon ombre ? »"),

    ('virgo', 2): make_lilith_interp('virgo', 2,
        "Ton ombre se loge dans l'anxiété financière — ton pouvoir est celui de la gestion précise.",
        "Lilith en Vierge dans ta maison II place ton ombre dans ta relation à l'argent et à la valeur. Tu peux avoir une anxiété excessive autour des finances ou une critique de tes capacités.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de gestion impeccable des ressources. Tu maximises avec précision.",
        "En maison II, cette énergie peut créer une relation anxieuse à l'argent. Apprends que la suffisance est aussi une richesse.",
        "Reconnais la valeur de ce que tu as déjà.",
        "Respire en relâchant l'anxiété financière.",
        "Quelle anxiété ou critique autour de ma valeur ai-je refoulée ? »"),

    ('virgo', 3): make_lilith_interp('virgo', 3,
        "Ton ombre se loge dans la critique verbale — ton pouvoir est celui de l'analyse verbale.",
        "Lilith en Vierge dans ta maison III place ton ombre dans ta communication. Tu peux avoir une tendance à critiquer ou à analyser excessivement dans tes échanges.",
        "En intégrant cette Lilith, tu accèdes à une parole précise et discernante. Tu peux améliorer par tes mots.",
        "En maison III, cette énergie peut créer des relations tendues avec l'entourage. Transforme la critique en feedback constructif.",
        "Communique une observation utile avec bienveillance.",
        "Respire en adoucissant ton mental critique.",
        "Comment ma tendance critique affecte-t-elle mes communications ? »"),

    ('virgo', 4): make_lilith_interp('virgo', 4,
        "Ton ombre se loge dans le perfectionnisme familial — ton pouvoir est celui de l'ordre intérieur.",
        "Lilith en Vierge dans ta maison IV place ton ombre dans ta famille et ton foyer. Tu peux avoir grandi dans un environnement critique ou vouloir un foyer parfait.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer un foyer fonctionnel et sain. Tu organises avec sagesse.",
        "En maison IV, cette énergie peut créer un foyer anxieux ou trop contrôlé. Apprends à accueillir l'imperfection chez toi.",
        "Crée du confort sans chercher la perfection.",
        "Respire en acceptant l'imperfection de ton foyer.",
        "Quelles critiques familiales ou perfectionnisme ai-je hérités ? »"),

    ('virgo', 5): make_lilith_interp('virgo', 5,
        "Ton ombre se loge dans la critique créative — ton pouvoir est celui de la création raffinée.",
        "Lilith en Vierge dans ta maison V place ton ombre dans ta créativité et tes amours. Tu peux être trop critique de ce que tu crées ou de tes partenaires.",
        "En intégrant cette Lilith, tu accèdes à une créativité méticuleuse et raffinée. Tu crées avec précision et beauté.",
        "En maison V, cette énergie peut bloquer la créativité par le perfectionnisme. Apprends à créer sans juger.",
        "Crée quelque chose sans le critiquer.",
        "Respire en célébrant ta création imparfaite.",
        "Comment mon perfectionnisme a-t-il bloqué ma créativité ou mes amours ? »"),

    ('virgo', 6): make_lilith_interp('virgo', 6,
        "Ton ombre se loge dans l'obsession du travail — ton pouvoir est celui du service parfait.",
        "Lilith en Vierge dans ta maison VI (son domicile) place ton ombre dans le travail et la santé. Tu peux avoir une obsession du travail ou une hypochondrie.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de service et de travail exceptionnels. Tu excelles dans l'amélioration.",
        "En maison VI, cette énergie est particulièrement puissante. Tu peux t'épuiser à perfectionner. Apprends que suffisant est parfois parfait.",
        "Accomplis une tâche de façon « assez bonne ».",
        "Respire en relâchant l'obsession de la perfection.",
        "Quelle obsession du travail ou de la santé ai-je refoulée ? »"),

    ('virgo', 7): make_lilith_interp('virgo', 7,
        "Ton ombre se loge dans la critique du partenaire — ton pouvoir est celui de l'amélioration relationnelle.",
        "Lilith en Vierge dans ta maison VII place ton ombre dans tes relations. Tu peux être très critique de tes partenaires ou attirer des partenaires critiques.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'améliorer les relations. Tu peux aider ton partenaire à grandir.",
        "En maison VII, cette énergie peut créer des relations basées sur la critique. Transforme l'analyse en soutien bienveillant.",
        "Apprécie ton partenaire sans chercher à l'améliorer.",
        "Respire en voyant la beauté dans les imperfections de l'autre.",
        "Comment ma tendance critique affecte-t-elle mes relations ? »"),

    ('virgo', 8): make_lilith_interp('virgo', 8,
        "Ton ombre se loge dans le contrôle des crises — ton pouvoir est celui de la transformation méthodique.",
        "Lilith en Vierge dans ta maison VIII place ton ombre dans ta relation aux crises et au contrôle. Tu peux essayer de tout analyser pour éviter l'intensité émotionnelle.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformation méthodique. Tu traverses les crises avec discernement.",
        "En maison VIII, cette énergie peut créer une anxiété face à l'incontrôlable. Apprends à lâcher l'analyse pour vivre.",
        "Traverse une émotion intense sans l'analyser.",
        "Respire en acceptant ce qui ne peut être contrôlé.",
        "Où mon besoin de contrôle m'empêche-t-il de me transformer ? »"),

    ('virgo', 9): make_lilith_interp('virgo', 9,
        "Ton ombre se loge dans le scepticisme — ton pouvoir est celui de la sagesse pratique.",
        "Lilith en Vierge dans ta maison IX place ton ombre dans tes croyances. Tu peux être excessivement sceptique ou critiquer toute spiritualité qui n'est pas « logique ».",
        "En intégrant cette Lilith, tu accèdes à une sagesse ancrée et pratique. Tu incarnes ce que tu crois.",
        "En maison IX, cette énergie peut créer un conflit entre foi et raison. Apprends que le mystère fait aussi partie de la vérité.",
        "Accepte une croyance sans la disséquer.",
        "Respire en accueillant le mystère.",
        "Comment mon scepticisme me ferme-t-il à la transcendance ? »"),

    ('virgo', 10): make_lilith_interp('virgo', 10,
        "Ton ombre se loge dans le perfectionnisme de carrière — ton pouvoir est celui de l'excellence professionnelle.",
        "Lilith en Vierge dans ta maison X place ton ombre dans ta carrière. Tu peux avoir une anxiété de performance ou un perfectionnisme qui te paralyse.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'excellence professionnelle. Tu excelles dans les détails qui comptent.",
        "En maison X, cette énergie peut créer une peur de l'erreur publique. Apprends que l'excellence n'est pas la perfection.",
        "Accepte une imperfection dans ton travail public.",
        "Respire en relâchant la peur de l'erreur.",
        "Quelle anxiété de performance affecte ma carrière ? »"),

    ('virgo', 11): make_lilith_interp('virgo', 11,
        "Ton ombre se loge dans la critique des groupes — ton pouvoir est celui de l'amélioration collective.",
        "Lilith en Vierge dans ta maison XI place ton ombre dans tes groupes et tes amitiés. Tu peux être très critique des dynamiques de groupe ou t'isoler par perfectionnisme.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir d'améliorer les groupes. Tu apportes du discernement aux collectifs.",
        "En maison XI, cette énergie peut créer des tensions dans les groupes. Transforme la critique en contribution constructive.",
        "Contribue à améliorer un groupe sans le critiquer.",
        "Respire en acceptant les imperfections du collectif.",
        "Comment mon perfectionnisme affecte-t-il mes relations de groupe ? »"),

    ('virgo', 12): make_lilith_interp('virgo', 12,
        "Ton ombre se loge dans l'autocritique inconsciente — ton pouvoir est celui du service silencieux.",
        "Lilith en Vierge dans ta maison XII place ton ombre dans l'inconscient et l'autocritique. Tu peux avoir une voix intérieure qui te critique sans cesse.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de service invisible et de guérison silencieuse. Tu améliores sans être vu.",
        "En maison XII, cette énergie peut créer une anxiété inconsciente ou un perfectionnisme spirituel. Apprends la paix au-delà de l'analyse.",
        "Médite sans analyser ton expérience.",
        "Respire en faisant taire la voix critique.",
        "Quelle autocritique inconsciente porte mon âme ? »"),

    # === LIBRA (M1-M12) ===
    ('libra', 1): make_lilith_interp('libra', 1,
        "Ton ombre se loge dans la codépendance et le faux-self — ton pouvoir est celui de l'harmonie authentique.",
        "Lilith en Balance dans ta maison I place ton ombre dans ton identité et ton rapport aux autres. Tu peux avoir créé un faux-self pour plaire ou avoir refoulé ton vrai moi.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer l'harmonie tout en restant toi-même. Tu es magnétiquement équilibré.",
        "En maison I, cette énergie peut créer une personnalité trop adaptable. Apprends à plaire sans te trahir.",
        "Affirme qui tu es vraiment, même si ça déplaît.",
        "Respire en te sentant complet sans l'approbation des autres.",
        "Où me suis-je trahi pour plaire ou être aimé ? »"),

    ('libra', 2): make_lilith_interp('libra', 2,
        "Ton ombre se loge dans la dépendance financière — ton pouvoir est celui de la co-création de valeur.",
        "Lilith en Balance dans ta maison II place ton ombre dans ta relation aux ressources partagées. Tu peux avoir dépendu financièrement des autres ou partagé au détriment de tes besoins.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer de la valeur en partenariat. Tu prospères avec les autres.",
        "En maison II, cette énergie peut créer des déséquilibres financiers dans les relations. Apprends à recevoir autant que tu donnes.",
        "Crée de la valeur par toi-même.",
        "Respire en te sentant digne d'avoir tes propres ressources.",
        "Quelle dépendance financière ou déséquilibre ai-je dans mes relations ? »"),

    ('libra', 3): make_lilith_interp('libra', 3,
        "Ton ombre se loge dans l'évitement du conflit verbal — ton pouvoir est celui de la parole juste.",
        "Lilith en Balance dans ta maison III place ton ombre dans ta communication. Tu peux éviter les confrontations verbales ou dire ce que l'autre veut entendre.",
        "En intégrant cette Lilith, tu accèdes à une parole diplomatique mais vraie. Tu peux dire des vérités difficiles avec grâce.",
        "En maison III, cette énergie peut créer des non-dits par peur du conflit. Apprends que le conflit sain est une forme d'amour.",
        "Dis une vérité inconfortable avec diplomatie.",
        "Respire en trouvant ta voix authentique.",
        "Quelles vérités ai-je évitées pour maintenir la paix ? »"),

    ('libra', 4): make_lilith_interp('libra', 4,
        "Ton ombre se loge dans la fausse harmonie familiale — ton pouvoir est celui de la paix authentique.",
        "Lilith en Balance dans ta maison IV place ton ombre dans ta famille et ton foyer. Tu peux avoir maintenu une façade d'harmonie ou porté le rôle de médiateur.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer une vraie paix au foyer. Tu harmonises avec authenticité.",
        "En maison IV, cette énergie peut créer une famille en surface lisse mais en tension dessous. Apprends que la vraie paix vient de la vérité.",
        "Exprime une tension familiale au lieu de la masquer.",
        "Respire en accueillant le conflit comme chemin vers la paix.",
        "Quelle fausse harmonie ai-je maintenue dans ma famille ? »"),

    ('libra', 5): make_lilith_interp('libra', 5,
        "Ton ombre se loge dans l'amour conditionnel — ton pouvoir est celui de l'amour équilibré.",
        "Lilith en Balance dans ta maison V place ton ombre dans tes amours et ta créativité. Tu peux avoir aimé ou créé pour plaire plutôt que par passion vraie.",
        "En intégrant cette Lilith, tu accèdes à un amour et une créativité authentiquement beaux. Tu crées et aimes avec harmonie et vérité.",
        "En maison V, cette énergie peut créer des amours superficielles ou une créativité trop soucieuse du jugement. Aime et crée pour toi.",
        "Crée ou aime quelque chose de vrai, pas de beau.",
        "Respire en embrassant ta passion authentique.",
        "Où ai-je aimé ou créé pour plaire plutôt que par passion vraie ? »"),

    ('libra', 6): make_lilith_interp('libra', 6,
        "Ton ombre se loge dans le sacrifice au travail — ton pouvoir est celui du service équilibré.",
        "Lilith en Balance dans ta maison VI place ton ombre dans ton rapport au travail. Tu peux te sacrifier pour maintenir l'harmonie ou éviter les conflits professionnels.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de servir avec équilibre. Tu travailles en harmonie sans te perdre.",
        "En maison VI, cette énergie peut créer de l'épuisement à maintenir la paix au travail. Apprends que tes besoins comptent aussi.",
        "Affirme un besoin au travail sans te sentir coupable.",
        "Respire en équilibrant service et préservation de soi.",
        "Où me suis-je sacrifié au travail pour maintenir l'harmonie ? »"),

    ('libra', 7): make_lilith_interp('libra', 7,
        "Ton ombre se loge dans la perte de soi en relation — ton pouvoir est celui du partenariat équilibré.",
        "Lilith en Balance dans ta maison VII (son domicile) place ton ombre dans tes relations. Tu peux t'être complètement perdu dans l'autre ou avoir évité tout conflit.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer des partenariats profondément équilibrés. Tu es en relation sans te perdre.",
        "En maison VII, cette énergie est particulièrement puissante. Tu es destiné à maîtriser l'art de la relation authentique.",
        "Maintiens ton identité dans une relation proche.",
        "Respire en te sentant complet même en couple.",
        "Où me suis-je perdu dans mes relations ? »"),

    ('libra', 8): make_lilith_interp('libra', 8,
        "Ton ombre se loge dans l'évitement de l'intensité — ton pouvoir est celui de la transformation harmonieuse.",
        "Lilith en Balance dans ta maison VIII place ton ombre dans ta relation à l'intensité et aux crises. Tu peux éviter les confrontations profondes pour maintenir la paix.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer avec grâce. Tu traverses les crises avec équilibre.",
        "En maison VIII, cette énergie peut créer une fuite devant l'intensité émotionnelle. Apprends que la profondeur n'est pas l'ennemi de l'harmonie.",
        "Plonge dans une émotion intense au lieu de l'éviter.",
        "Respire en accueillant l'intensité avec grâce.",
        "Quelle intensité ai-je évitée pour maintenir la surface lisse ? »"),

    ('libra', 9): make_lilith_interp('libra', 9,
        "Ton ombre se loge dans l'indécision philosophique — ton pouvoir est celui de la sagesse équilibrée.",
        "Lilith en Balance dans ta maison IX place ton ombre dans tes croyances. Tu peux être tellement ouvert à toutes les perspectives que tu n'en choisis aucune.",
        "En intégrant cette Lilith, tu accèdes à une sagesse qui intègre les contraires. Tu peux voir toutes les vérités et choisir la tienne.",
        "En maison IX, cette énergie peut créer un relativisme paralysant. Apprends à choisir ta vérité tout en respectant les autres.",
        "Prends position sur une question philosophique.",
        "Respire en assumant tes propres croyances.",
        "Quelle vérité évité-je de choisir par peur de désaccord ? »"),

    ('libra', 10): make_lilith_interp('libra', 10,
        "Ton ombre se loge dans l'image publique — ton pouvoir est celui du leadership harmonieux.",
        "Lilith en Balance dans ta maison X place ton ombre dans ta carrière et ton image. Tu peux avoir façonné une image pour plaire plutôt que pour être vrai.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de leadership qui rassemble. Tu réussis en créant de l'harmonie.",
        "En maison X, cette énergie peut créer une réputation de people pleaser. Construis ta carrière sur l'authenticité.",
        "Assume une position professionnelle authentique.",
        "Respire en étant vrai dans ta vie publique.",
        "Quelle image professionnelle ai-je créée pour plaire ? »"),

    ('libra', 11): make_lilith_interp('libra', 11,
        "Ton ombre se loge dans la fusion dans les groupes — ton pouvoir est celui de l'harmonie collective.",
        "Lilith en Balance dans ta maison XI place ton ombre dans tes groupes et tes amitiés. Tu peux te fondre dans les groupes ou éviter tout conflit collectif.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer des communautés harmonieuses. Tu rassembles avec grâce.",
        "En maison XI, cette énergie peut créer une perte d'identité dans les groupes. Appartiens tout en restant unique.",
        "Affirme ton unicité dans un groupe.",
        "Respire en appartenant sans te perdre.",
        "Où me suis-je perdu dans les dynamiques de groupe ? »"),

    ('libra', 12): make_lilith_interp('libra', 12,
        "Ton ombre se loge dans la codépendance karmique — ton pouvoir est celui de l'harmonie cosmique.",
        "Lilith en Balance dans ta maison XII place ton ombre dans l'inconscient et les relations karmiques. Tu peux porter des schémas relationnels de vies passées.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de créer l'harmonie au niveau de l'âme. Tu équilibres les karmas relationnels.",
        "En maison XII, cette énergie porte une dimension spirituelle. Tu es destiné à guérir les déséquilibres relationnels profonds.",
        "Médite sur l'équilibre dans tes relations karmiques.",
        "Respire en sentant l'harmonie cosmique.",
        "Quels schémas relationnels karmiques porte mon âme ? »"),

    # === SCORPIO (M1-M12) ===
    ('scorpio', 1): make_lilith_interp('scorpio', 1,
        "Ton ombre se loge dans le pouvoir et l'intensité — tu accèdes au pouvoir brut de la transformation.",
        "Lilith en Scorpion dans ta maison I place ton ombre dans ton identité et ton intensité. Tu peux avoir refoulé un pouvoir immense ou des désirs tabous.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir magnétique et transformateur. Tu es capable de renaître et de faire renaître.",
        "En maison I, cette énergie est très visible. Tu dégages une intensité qui peut attirer ou effrayer. Assume ton pouvoir.",
        "Embrasse ton pouvoir sans en avoir peur.",
        "Respire en sentant ta puissance de transformation.",
        "Quel pouvoir ou désir tabou ai-je refoulé ? »"),

    ('scorpio', 2): make_lilith_interp('scorpio', 2,
        "Ton ombre se loge dans l'obsession de contrôle des ressources — ton pouvoir est celui de la transformation matérielle.",
        "Lilith en Scorpion dans ta maison II place ton ombre dans ta relation à l'argent et au pouvoir matériel. Tu peux avoir une obsession de contrôle ou des peurs de perte intenses.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer les ressources. Tu peux renaître matériellement de n'importe quelle perte.",
        "En maison II, cette énergie peut créer des cycles de gain et de perte intenses. Apprends que tu peux tout reconstruire.",
        "Lâche le contrôle sur une ressource.",
        "Respire en faisant confiance à ta capacité de renaissance.",
        "Quelle obsession ou peur autour des ressources ai-je refoulée ? »"),

    ('scorpio', 3): make_lilith_interp('scorpio', 3,
        "Ton ombre se loge dans les secrets et les paroles qui tuent — ton pouvoir est celui de la parole transformatrice.",
        "Lilith en Scorpion dans ta maison III place ton ombre dans ta communication et les secrets. Tu peux détenir des informations puissantes ou avoir le pouvoir de blesser par les mots.",
        "En intégrant cette Lilith, tu accèdes à une parole qui transforme. Tu peux nommer l'indicible et guérir par les mots.",
        "En maison III, cette énergie peut créer des communications intenses ou manipulatrices. Utilise ton pouvoir verbal pour guérir.",
        "Parle d'un sujet tabou avec l'intention de guérir.",
        "Respire en honorant le pouvoir de tes mots.",
        "Quels secrets ou paroles destructrices ai-je retenus ? »"),

    ('scorpio', 4): make_lilith_interp('scorpio', 4,
        "Ton ombre se loge dans les traumatismes familiaux — ton pouvoir est celui de transformer la lignée.",
        "Lilith en Scorpion dans ta maison IV place ton ombre dans ta famille et les secrets de lignée. Tu peux porter des traumatismes familiaux lourds ou des secrets toxiques.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer ta lignée. Tu es l'alchimiste qui brise les cycles.",
        "En maison IV, cette énergie est particulièrement intense. Tu es destiné à faire remonter les secrets et à les transmuter.",
        "Expose et transforme un secret ou traumatisme familial.",
        "Respire en sentant ta capacité à guérir ta lignée.",
        "Quels traumatismes ou secrets familiaux porte mon inconscient ? »"),

    ('scorpio', 5): make_lilith_interp('scorpio', 5,
        "Ton ombre se loge dans la passion destructrice — ton pouvoir est celui de la création intense.",
        "Lilith en Scorpion dans ta maison V place ton ombre dans ta créativité et tes amours. Tu peux avoir des passions destructrices ou une créativité obsessionnelle.",
        "En intégrant cette Lilith, tu accèdes à une créativité et un amour intenses et transformateurs. Tu crées et aimes avec toute ton âme.",
        "En maison V, cette énergie peut créer des drames amoureux ou une créativité sombre. Canalise l'intensité en création.",
        "Crée quelque chose d'intense et transformateur.",
        "Respire en embrassant ta passion créatrice.",
        "Quelles passions destructrices ou obsessions créatives ai-je refoulées ? »"),

    ('scorpio', 6): make_lilith_interp('scorpio', 6,
        "Ton ombre se loge dans le pouvoir au travail — ton pouvoir est celui de la transformation quotidienne.",
        "Lilith en Scorpion dans ta maison VI place ton ombre dans ton rapport au travail et au pouvoir quotidien. Tu peux avoir vécu des jeux de pouvoir toxiques au travail.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer les environnements de travail. Tu peux assainir ce qui est toxique.",
        "En maison VI, cette énergie peut créer des conflits de pouvoir au travail ou des problèmes de santé liés au stress. Apprends à utiliser ton pouvoir sainement.",
        "Transforme une dynamique toxique au travail.",
        "Respire en utilisant ton pouvoir pour guérir.",
        "Quels jeux de pouvoir toxiques ai-je vécus ou exercés au travail ? »"),

    ('scorpio', 7): make_lilith_interp('scorpio', 7,
        "Ton ombre se loge dans les relations de pouvoir — tu accèdes au pouvoir de l'intimité transformatrice.",
        "Lilith en Scorpion dans ta maison VII place ton ombre dans tes relations et les jeux de pouvoir en couple. Tu peux avoir vécu des trahisons ou exercé du contrôle.",
        "En intégrant cette Lilith, tu accèdes à des relations profondément transformatrices. Tu peux créer une intimité qui guérit.",
        "En maison VII, cette énergie peut créer des relations intenses et parfois destructrices. Apprends le pouvoir de l'amour sans manipulation.",
        "Crée de l'intimité sans jeux de pouvoir.",
        "Respire en faisant confiance à l'autre.",
        "Quels jeux de pouvoir ou trahisons ai-je vécus en relation ? »"),

    ('scorpio', 8): make_lilith_interp('scorpio', 8,
        "Ton ombre se loge dans les profondeurs — tu accèdes au pouvoir ultime de transformation.",
        "Lilith en Scorpion dans ta maison VIII (son domicile) place ton ombre dans les profondeurs absolues. Tu as accès aux mystères de la mort, de la sexualité et du pouvoir.",
        "En intégrant cette Lilith, tu accèdes au pouvoir ultime de transformation. Tu es un initié aux mystères les plus profonds.",
        "En maison VIII, cette énergie est à son maximum. Tu es destiné à être un alchimiste, un guérisseur des profondeurs.",
        "Plonge dans ta profondeur sans peur.",
        "Respire en embrassant les mystères de la vie et de la mort.",
        "Quelles profondeurs de mon être n'ai-je pas encore explorées ? »"),

    ('scorpio', 9): make_lilith_interp('scorpio', 9,
        "Ton ombre se loge dans les vérités occultes — ton pouvoir est celui de la sagesse des mystères.",
        "Lilith en Scorpion dans ta maison IX place ton ombre dans ta quête de vérité et les connaissances occultes. Tu peux être attiré par les vérités interdites ou cachées.",
        "En intégrant cette Lilith, tu accèdes à une sagesse des profondeurs. Tu peux enseigner ce que d'autres n'osent pas dire.",
        "En maison IX, cette énergie peut créer un attrait pour l'occulte ou une quête de vérité obsessionnelle. Enseigne avec sagesse.",
        "Explore une vérité cachée ou tabou.",
        "Respire en honorant ta quête des mystères.",
        "Quelles vérités cachées ou occultes m'attirent ? »"),

    ('scorpio', 10): make_lilith_interp('scorpio', 10,
        "Ton ombre se loge dans le pouvoir public — tu accèdes au pouvoir de la transformation sociale.",
        "Lilith en Scorpion dans ta maison X place ton ombre dans ta carrière et ton pouvoir public. Tu peux avoir vécu des abus de pouvoir ou avoir une ambition intense.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer les structures. Tu peux exercer une influence profonde.",
        "En maison X, cette énergie peut créer une carrière intense avec des hauts et des bas dramatiques. Utilise ton pouvoir pour transformer.",
        "Utilise ton influence pour transformer positivement.",
        "Respire en assumant ton pouvoir public.",
        "Quel pouvoir ou abus de pouvoir ai-je vécu dans ma carrière ? »"),

    ('scorpio', 11): make_lilith_interp('scorpio', 11,
        "Ton ombre se loge dans les dynamiques de groupe intenses — ton pouvoir est celui de transformer les collectifs.",
        "Lilith en Scorpion dans ta maison XI place ton ombre dans les groupes et les dynamiques collectives. Tu peux avoir vécu des trahisons de groupe ou exercé un pouvoir dans les collectifs.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformer les groupes. Tu peux assainir les dynamiques toxiques.",
        "En maison XI, cette énergie peut créer des expériences de groupe intenses. Tu es destiné à transformer les collectifs.",
        "Transforme une dynamique de groupe toxique.",
        "Respire en utilisant ton pouvoir pour le bien collectif.",
        "Quelles trahisons ou jeux de pouvoir ai-je vécus dans les groupes ? »"),

    ('scorpio', 12): make_lilith_interp('scorpio', 12,
        "Ton ombre se loge dans l'inconscient collectif — ton pouvoir est celui de transformer l'âme du monde.",
        "Lilith en Scorpion dans ta maison XII place ton ombre dans les profondeurs de l'inconscient et du karma. Tu portes peut-être les ombres de l'humanité.",
        "En intégrant cette Lilith, tu accèdes à un pouvoir de transformation transpersonnel. Tu peux guérir les blessures collectives.",
        "En maison XII, cette énergie est la plus intense. Tu es un guérisseur des profondeurs invisibles, un alchimiste de l'âme collective.",
        "Médite en transformant une ombre collective.",
        "Respire en sentant ta connexion aux mystères de l'univers.",
        "Quelle ombre collective ou karmique porte mon âme ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in LILITH_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'lilith',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP lilith/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='lilith',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT lilith/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
