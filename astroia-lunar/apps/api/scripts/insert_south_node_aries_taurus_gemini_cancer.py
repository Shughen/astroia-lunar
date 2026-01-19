#!/usr/bin/env python3
"""Insert South Node interpretations for Aries, Taurus, Gemini, Cancer (48 entries)."""
import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

def make_sn_interp(sign_name, house, phrase, moteur, defi, maison_desc, ritual_action, ritual_breath, ritual_journal):
    sign_titles = {
        'aries': '☋ Nœud Sud en Bélier',
        'taurus': '☋ Nœud Sud en Taureau',
        'gemini': '☋ Nœud Sud en Gémeaux',
        'cancer': '☋ Nœud Sud en Cancer',
    }
    sign_fr = {
        'aries': 'Bélier',
        'taurus': 'Taureau',
        'gemini': 'Gémeaux',
        'cancer': 'Cancer',
    }
    return f"""# {sign_titles[sign_name]}

**En une phrase :** {phrase}

## Ton acquis karmique
{moteur}

## Ton piège
{defi}

## Maison {house} en {sign_fr[sign_name]}
{maison_desc}

## Micro-rituel du jour (2 min)
- {ritual_action}
- {ritual_breath}
- Journal : « {ritual_journal} »"""

SOUTH_NODE_INTERPRETATIONS = {
    # === ARIES (M1-M12) ===
    ('aries', 1): make_sn_interp('aries', 1,
        "Tu arrives avec une maîtrise de l'affirmation et du courage — mais l'excès d'indépendance te freine.",
        "Le Nœud Sud en Bélier dans ta maison I indique une maîtrise karmique de l'affirmation personnelle. Tu sais te battre, prendre des initiatives et agir avec courage.",
        "L'égocentrisme et l'impatience peuvent te piéger. Ta tendance à foncer sans considérer les autres te coupe des relations qui t'aideraient à grandir.",
        "Ta présence porte la mémoire du guerrier solitaire. Tu dois maintenant apprendre à inclure les autres dans ta démarche, à créer des alliances plutôt qu'à tout faire seul.",
        "Avant une action impulsive, prends 3 secondes pour considérer l'impact sur les autres.",
        "Respire en adoucissant la tension dans tes épaules et ta mâchoire.",
        "Dans quelle situation ma tendance à agir seul me freine-t-elle ? »"),

    ('aries', 2): make_sn_interp('aries', 2,
        "Tu arrives avec une capacité à conquérir les ressources — mais l'attachement combatif te freine.",
        "Le Nœud Sud en Bélier dans ta maison II indique une maîtrise karmique de la conquête financière. Tu sais te battre pour ce que tu veux et prendre ce qui t'appartient.",
        "L'agressivité autour de l'argent peut te piéger. Ta tendance à voir les finances comme un combat te coupe du partage et de la coopération.",
        "Tes ressources portent la mémoire du conquérant. Tu dois maintenant apprendre à créer de la valeur avec les autres, pas contre eux.",
        "Partage une ressource sans attente de retour.",
        "Respire en relâchant la tension de compétition autour de l'argent.",
        "Où mon attitude combative autour de l'argent me fait-elle perdre plus qu'elle ne me rapporte ? »"),

    ('aries', 3): make_sn_interp('aries', 3,
        "Tu arrives avec une capacité à communiquer directement — mais l'agressivité verbale te freine.",
        "Le Nœud Sud en Bélier dans ta maison III indique une maîtrise karmique de la parole directe. Tu sais dire ce que tu penses sans détour et défendre tes idées.",
        "La communication agressive peut te piéger. Ta tendance à couper la parole ou à imposer tes opinions te coupe du vrai dialogue.",
        "Ta communication porte la mémoire du débatteur combatif. Tu dois maintenant apprendre à écouter et à dialoguer véritablement.",
        "Dans ta prochaine conversation, écoute jusqu'au bout avant de répondre.",
        "Respire en adoucissant le ton de ta voix intérieure.",
        "Dans quelles conversations ma communication directe devient-elle agressive ? »"),

    ('aries', 4): make_sn_interp('aries', 4,
        "Tu arrives avec une capacité à défendre ton foyer — mais les conflits familiaux te freinent.",
        "Le Nœud Sud en Bélier dans ta maison IV indique une maîtrise karmique de la protection du territoire. Tu sais défendre ta famille et ton espace avec férocité.",
        "Les luttes de pouvoir familiales peuvent te piéger. Ta tendance à voir le foyer comme une forteresse te coupe de l'intimité et de la douceur.",
        "Ton foyer porte la mémoire des batailles familiales. Tu dois maintenant apprendre à créer un espace de paix et d'harmonie, pas un champ de bataille.",
        "Initie un moment de paix et de tendresse dans ton foyer.",
        "Respire en imaginant ton foyer comme un sanctuaire, pas une forteresse.",
        "Quels conflits familiaux perpétué-je par habitude karmique ? »"),

    ('aries', 5): make_sn_interp('aries', 5,
        "Tu arrives avec une capacité à créer avec audace — mais l'égo créatif te freine.",
        "Le Nœud Sud en Bélier dans ta maison V indique une maîtrise karmique de la création audacieuse. Tu sais prendre des risques créatifs et t'exprimer avec passion.",
        "L'égo créatif et la compétition peuvent te piéger. Ta tendance à vouloir briller seul te coupe de la co-création et des amours durables.",
        "Ta créativité porte la mémoire du créateur solitaire. Tu dois maintenant apprendre à créer avec les autres et à aimer sans possessivité.",
        "Crée quelque chose en collaboration, même petite.",
        "Respire en relâchant le besoin d'être le meilleur créateur.",
        "Comment mon besoin de briller seul limite-t-il ma créativité et mes amours ? »"),

    ('aries', 6): make_sn_interp('aries', 6,
        "Tu arrives avec une capacité à travailler avec énergie — mais l'impatience au travail te freine.",
        "Le Nœud Sud en Bélier dans ta maison VI indique une maîtrise karmique du travail énergique. Tu sais foncer, prendre des initiatives et être productif.",
        "L'impatience et les conflits au travail peuvent te piéger. Ta tendance à vouloir tout faire vite et seul te coupe de la collaboration efficace.",
        "Ton travail porte la mémoire du travailleur solitaire et pressé. Tu dois maintenant apprendre la patience et le travail d'équipe.",
        "Demande de l'aide pour une tâche au lieu de la faire seul.",
        "Respire en relâchant l'urgence et la pression que tu te mets.",
        "Comment mon impatience au travail me rend-elle moins efficace ? »"),

    ('aries', 7): make_sn_interp('aries', 7,
        "Tu arrives avec une capacité à t'affirmer en relation — mais les conflits relationnels te freinent.",
        "Le Nœud Sud en Bélier dans ta maison VII indique une maîtrise karmique de l'affirmation dans les relations. Tu sais défendre ta position face à l'autre.",
        "Les luttes de pouvoir dans le couple peuvent te piéger. Ta tendance à voir le partenaire comme un adversaire te coupe de l'intimité vraie.",
        "Tes relations portent la mémoire des combats à deux. Tu dois maintenant apprendre à créer des partenariats d'harmonie et de coopération.",
        "Cède sur un point de désaccord avec un partenaire, consciemment.",
        "Respire en visualisant ton partenaire comme un allié, pas un adversaire.",
        "Où mes relations deviennent-elles des champs de bataille ? »"),

    ('aries', 8): make_sn_interp('aries', 8,
        "Tu arrives avec une capacité à traverser les crises avec courage — mais la violence transformatrice te freine.",
        "Le Nœud Sud en Bélier dans ta maison VIII indique une maîtrise karmique de la transformation combative. Tu sais affronter la mort et les crises avec bravoure.",
        "La violence des transformations peut te piéger. Ta tendance à forcer les passages te coupe de la transformation en douceur.",
        "Tes transformations portent la mémoire du guerrier qui force les portes. Tu dois maintenant apprendre à te transformer avec grâce et patience.",
        "Face à un changement, choisis la patience plutôt que la force.",
        "Respire en accueillant la transformation avec douceur plutôt qu'avec combat.",
        "Quelles transformations ai-je forcées au lieu de les laisser mûrir ? »"),

    ('aries', 9): make_sn_interp('aries', 9,
        "Tu arrives avec une capacité à défendre tes croyances — mais le fanatisme te freine.",
        "Le Nœud Sud en Bélier dans ta maison IX indique une maîtrise karmique de la quête combative de vérité. Tu sais défendre tes convictions avec passion.",
        "Le fanatisme et l'intolérance peuvent te piéger. Ta tendance à imposer tes croyances te coupe de l'ouverture aux autres perspectives.",
        "Ta spiritualité porte la mémoire du croisé. Tu dois maintenant apprendre l'humilité spirituelle et l'écoute des autres vérités.",
        "Explore une croyance différente de la tienne avec curiosité.",
        "Respire en relâchant le besoin d'avoir raison spirituellement.",
        "Quelles croyances défends-je avec trop de véhémence ? »"),

    ('aries', 10): make_sn_interp('aries', 10,
        "Tu arrives avec une capacité à conquérir le succès — mais l'ambition agressive te freine.",
        "Le Nœud Sud en Bélier dans ta maison X indique une maîtrise karmique de la carrière combative. Tu sais gravir les échelons et prendre le pouvoir.",
        "L'ambition agressive peut te piéger. Ta tendance à écraser la concurrence te coupe des alliances qui t'aideraient vraiment.",
        "Ta carrière porte la mémoire du conquérant solitaire. Tu dois maintenant apprendre à bâtir avec les autres et à servir plutôt qu'à régner.",
        "Aide un concurrent ou un collègue au lieu de le voir comme un rival.",
        "Respire en relâchant la tension de la compétition professionnelle.",
        "Comment mon ambition agressive m'isole-t-elle professionnellement ? »"),

    ('aries', 11): make_sn_interp('aries', 11,
        "Tu arrives avec une capacité à mener les groupes — mais la domination collective te freine.",
        "Le Nœud Sud en Bélier dans ta maison XI indique une maîtrise karmique du leadership de groupe. Tu sais prendre les commandes et inspirer l'action collective.",
        "Le besoin de dominer les groupes peut te piéger. Ta tendance à imposer ta direction te coupe de la vraie collaboration.",
        "Tes amitiés portent la mémoire du chef qui commande. Tu dois maintenant apprendre à être un membre égal du groupe, pas toujours le leader.",
        "Laisse quelqu'un d'autre mener dans un projet collectif.",
        "Respire en relâchant le besoin de contrôler les dynamiques de groupe.",
        "Où mon besoin de mener me coupe-t-il de vraies amitiés égalitaires ? »"),

    ('aries', 12): make_sn_interp('aries', 12,
        "Tu arrives avec une capacité à combattre l'invisible — mais les batailles intérieures te freinent.",
        "Le Nœud Sud en Bélier dans ta maison XII indique une maîtrise karmique du combat spirituel. Tu sais affronter tes démons et te battre contre l'adversité invisible.",
        "Les batailles intérieures incessantes peuvent te piéger. Ta tendance à voir l'inconscient comme un ennemi te coupe de la paix intérieure.",
        "Ton monde intérieur porte la mémoire du guerrier de l'ombre. Tu dois maintenant apprendre à faire la paix avec tes profondeurs.",
        "Au lieu de combattre une peur, accueille-la avec douceur.",
        "Respire en imaginant tes ombres comme des alliés, pas des ennemis.",
        "Quelles batailles intérieures puis-je lâcher ? »"),

    # === TAURUS (M1-M12) ===
    ('taurus', 1): make_sn_interp('taurus', 1,
        "Tu arrives avec une maîtrise de la stabilité et de la présence — mais la rigidité te freine.",
        "Le Nœud Sud en Taureau dans ta maison I indique une maîtrise karmique de l'ancrage et de la constance. Tu sais être stable, fiable et présent.",
        "La rigidité et la résistance au changement peuvent te piéger. Ta tendance à t'accrocher au connu te coupe des transformations nécessaires.",
        "Ta présence porte la mémoire de la stabilité excessive. Tu dois maintenant apprendre à embrasser le changement et la transformation.",
        "Fais quelque chose différemment aujourd'hui, juste pour expérimenter.",
        "Respire en relâchant la tension de résistance au changement.",
        "Quelle transformation évité-je par attachement au connu ? »"),

    ('taurus', 2): make_sn_interp('taurus', 2,
        "Tu arrives avec une maîtrise de la gestion des ressources — mais l'attachement matériel te freine.",
        "Le Nœud Sud en Taureau dans ta maison II (son domicile) indique une maîtrise karmique profonde de la sécurité matérielle. Tu sais accumuler et préserver les ressources.",
        "L'attachement excessif aux possessions peut te piéger. Ta tendance à t'accrocher à ce que tu as te coupe du partage et de la transformation.",
        "Tes finances portent la mémoire de l'accumulation. Tu dois maintenant apprendre à partager, à lâcher prise, à transformer ton rapport à la matière.",
        "Donne ou partage quelque chose que tu aurais gardé.",
        "Respire en relâchant la peur du manque.",
        "À quoi m'accroche-je par peur plutôt que par besoin réel ? »"),

    ('taurus', 3): make_sn_interp('taurus', 3,
        "Tu arrives avec une maîtrise de la communication posée — mais la lenteur mentale te freine.",
        "Le Nœud Sud en Taureau dans ta maison III indique une maîtrise karmique de la parole mesurée. Tu sais peser tes mots et communiquer avec constance.",
        "La lenteur excessive et l'entêtement intellectuel peuvent te piéger. Ta tendance à rester sur tes positions te coupe des nouvelles idées.",
        "Ta communication porte la mémoire de la pensée lente. Tu dois maintenant apprendre la curiosité et l'adaptabilité mentale.",
        "Explore une idée nouvelle avec ouverture, même si elle te déstabilise.",
        "Respire en laissant ton mental devenir plus léger et flexible.",
        "Quelles idées refuses-je de considérer par entêtement ? »"),

    ('taurus', 4): make_sn_interp('taurus', 4,
        "Tu arrives avec une maîtrise de la création d'un foyer stable — mais l'attachement aux racines te freine.",
        "Le Nœud Sud en Taureau dans ta maison IV indique une maîtrise karmique de l'ancrage familial. Tu sais créer un foyer solide et des racines profondes.",
        "L'attachement excessif au foyer et au passé peut te piéger. Ta tendance à rester dans le connu te coupe de la croissance professionnelle.",
        "Ton foyer porte la mémoire de l'immobilité. Tu dois maintenant apprendre à sortir de ta zone de confort pour construire ta place dans le monde.",
        "Ose quelque chose de nouveau en dehors de ton foyer confortable.",
        "Respire en relâchant l'attachement au confort familier.",
        "Comment mon attachement au foyer me retient-il de grandir ? »"),

    ('taurus', 5): make_sn_interp('taurus', 5,
        "Tu arrives avec une maîtrise de la création stable — mais l'attachement à tes œuvres te freine.",
        "Le Nœud Sud en Taureau dans ta maison V indique une maîtrise karmique de la création durable. Tu sais produire des œuvres solides et des amours constants.",
        "L'attachement excessif à tes créations peut te piéger. Ta tendance à t'accrocher à ce que tu fais te coupe de l'évolution créative.",
        "Ta créativité porte la mémoire de la possession. Tu dois maintenant apprendre à créer et laisser aller, à aimer sans posséder.",
        "Laisse partir une création ou une relation qui ne te sert plus.",
        "Respire en relâchant l'attachement à tes œuvres et tes amours.",
        "À quelles créations ou amours m'accroche-je par peur de perdre ? »"),

    ('taurus', 6): make_sn_interp('taurus', 6,
        "Tu arrives avec une maîtrise des routines stables — mais la résistance au changement te freine.",
        "Le Nœud Sud en Taureau dans ta maison VI indique une maîtrise karmique des habitudes solides. Tu sais maintenir des routines et prendre soin de ton corps.",
        "La rigidité des habitudes peut te piéger. Ta tendance à répéter les mêmes routines te coupe de l'amélioration et de l'évolution.",
        "Ton travail porte la mémoire de la répétition. Tu dois maintenant apprendre à transformer tes habitudes et à évoluer dans ton quotidien.",
        "Change une routine, même petite, pour expérimenter la flexibilité.",
        "Respire en relâchant l'attachement à la façon habituelle de faire.",
        "Quelles routines perpétué-je par habitude plutôt que par choix ? »"),

    ('taurus', 7): make_sn_interp('taurus', 7,
        "Tu arrives avec une maîtrise de la loyauté en relation — mais la possessivité te freine.",
        "Le Nœud Sud en Taureau dans ta maison VII indique une maîtrise karmique de la fidélité. Tu sais être un partenaire loyal et constant.",
        "La possessivité et la jalousie peuvent te piéger. Ta tendance à t'accrocher à l'autre te coupe de la vraie intimité basée sur la liberté.",
        "Tes relations portent la mémoire de la possession. Tu dois maintenant apprendre à aimer dans la liberté et à lâcher prise sur le contrôle.",
        "Offre plus d'espace et de liberté à un partenaire.",
        "Respire en relâchant le besoin de posséder dans tes relations.",
        "Comment ma possessivité étouffe-t-elle mes relations ? »"),

    ('taurus', 8): make_sn_interp('taurus', 8,
        "Tu arrives avec une maîtrise de la préservation des ressources — mais la peur de la perte te freine.",
        "Le Nœud Sud en Taureau dans ta maison VIII indique une maîtrise karmique de la conservation. Tu sais préserver les ressources partagées et éviter les pertes.",
        "La peur de la perte et du changement peut te piéger. Ta tendance à t'accrocher te coupe des transformations nécessaires.",
        "Tes transformations portent la mémoire de la résistance. Tu dois maintenant apprendre à lâcher prise et à embrasser les cycles de mort et renaissance.",
        "Laisse aller quelque chose que tu gardais par peur de la perte.",
        "Respire en accueillant la transformation comme un cadeau, pas une menace.",
        "Qu'est-ce que ma peur de perdre m'empêche de gagner ? »"),

    ('taurus', 9): make_sn_interp('taurus', 9,
        "Tu arrives avec une maîtrise des croyances stables — mais le dogmatisme te freine.",
        "Le Nœud Sud en Taureau dans ta maison IX indique une maîtrise karmique des convictions ancrées. Tu sais maintenir une philosophie stable et cohérente.",
        "Le dogmatisme et le refus de questionner peuvent te piéger. Ta tendance à rester sur tes croyances te coupe de l'expansion spirituelle.",
        "Ta spiritualité porte la mémoire de l'immobilité philosophique. Tu dois maintenant apprendre à questionner, à explorer, à laisser ta vision évoluer.",
        "Questionne une croyance que tu tiens pour acquise.",
        "Respire en ouvrant ton esprit à de nouvelles possibilités.",
        "Quelles croyances refuses-je de questionner par confort ? »"),

    ('taurus', 10): make_sn_interp('taurus', 10,
        "Tu arrives avec une maîtrise de la carrière stable — mais la peur du risque te freine.",
        "Le Nœud Sud en Taureau dans ta maison X indique une maîtrise karmique de la sécurité professionnelle. Tu sais maintenir une position solide et fiable.",
        "La peur du risque et du changement peut te piéger. Ta tendance à rester dans le connu te coupe de l'évolution de carrière.",
        "Ta carrière porte la mémoire de la sécurité. Tu dois maintenant apprendre à prendre des risques calculés et à évoluer professionnellement.",
        "Prends un risque professionnel que tu évitais par peur.",
        "Respire en relâchant la peur de l'échec professionnel.",
        "Quel risque de carrière évité-je par attachement à la sécurité ? »"),

    ('taurus', 11): make_sn_interp('taurus', 11,
        "Tu arrives avec une maîtrise des amitiés stables — mais l'attachement au groupe te freine.",
        "Le Nœud Sud en Taureau dans ta maison XI indique une maîtrise karmique de la loyauté amicale. Tu sais être un ami fidèle et un membre constant du groupe.",
        "L'attachement excessif au groupe peut te piéger. Ta tendance à t'accrocher aux anciennes amitiés te coupe des nouvelles connexions.",
        "Tes amitiés portent la mémoire de la fidélité excessive. Tu dois maintenant apprendre à laisser évoluer tes cercles sociaux.",
        "Connecte-toi avec quelqu'un de nouveau au lieu de rester dans ton cercle habituel.",
        "Respire en relâchant l'attachement aux anciens groupes.",
        "Quelles amitiés perpétué-je par habitude plutôt que par choix ? »"),

    ('taurus', 12): make_sn_interp('taurus', 12,
        "Tu arrives avec une maîtrise de la paix intérieure — mais la stagnation spirituelle te freine.",
        "Le Nœud Sud en Taureau dans ta maison XII indique une maîtrise karmique de la tranquillité. Tu sais trouver la paix et le calme intérieur.",
        "La stagnation et le refus de l'inconfort spirituel peuvent te piéger. Ta tendance à rester dans le confort te coupe de la croissance profonde.",
        "Ton monde intérieur porte la mémoire du repos excessif. Tu dois maintenant apprendre à embrasser l'inconfort transformateur.",
        "Explore un territoire intérieur qui te met mal à l'aise.",
        "Respire en accueillant l'inconfort comme un signe de croissance.",
        "Quel inconfort spirituel évité-je par attachement à la paix ? »"),

    # === GEMINI (M1-M12) ===
    ('gemini', 1): make_sn_interp('gemini', 1,
        "Tu arrives avec une maîtrise de la curiosité et de l'adaptabilité — mais la dispersion te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison I indique une maîtrise karmique de la versatilité. Tu sais t'adapter, communiquer et jongler avec plusieurs facettes.",
        "La dispersion et la superficialité peuvent te piéger. Ta tendance à multiplier les identités te coupe de la profondeur et de la conviction.",
        "Ta présence porte la mémoire du caméléon. Tu dois maintenant apprendre à te fixer sur une direction et à développer une vision claire.",
        "Choisis une direction et suis-la avec constance pendant une journée.",
        "Respire en ancrant ta présence dans UNE version de toi-même.",
        "Où ma dispersion m'empêche-t-elle de développer une vraie profondeur ? »"),

    ('gemini', 2): make_sn_interp('gemini', 2,
        "Tu arrives avec une maîtrise de la diversification des revenus — mais l'éparpillement te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison II indique une maîtrise karmique de la polyvalence financière. Tu sais avoir plusieurs sources de revenus et t'adapter.",
        "L'éparpillement des ressources peut te piéger. Ta tendance à diversifier sans profondeur te coupe de la vraie prospérité.",
        "Tes finances portent la mémoire de la dispersion. Tu dois maintenant apprendre à concentrer tes ressources et à approfondir un domaine.",
        "Concentre ton énergie financière sur une source principale.",
        "Respire en ancrant ta valeur dans quelque chose de profond.",
        "Comment mon éparpillement financier me coûte-t-il de la vraie richesse ? »"),

    ('gemini', 3): make_sn_interp('gemini', 3,
        "Tu arrives avec une maîtrise de la communication — mais le bavardage te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison III (son domicile) indique une maîtrise karmique profonde de l'échange verbal. Tu sais communiquer, apprendre et partager l'information.",
        "Le bavardage et la dispersion mentale peuvent te piéger. Ta tendance à parler sans aller en profondeur te coupe de la vraie sagesse.",
        "Ta communication porte la mémoire de la surface. Tu dois maintenant apprendre à aller au fond des sujets et à développer une pensée philosophique.",
        "Explore un sujet en profondeur au lieu de survoler plusieurs sujets.",
        "Respire en laissant ton mental se calmer et s'approfondir.",
        "Quand est-ce que je parle sans vraiment rien dire d'important ? »"),

    ('gemini', 4): make_sn_interp('gemini', 4,
        "Tu arrives avec une maîtrise de la mobilité familiale — mais l'instabilité des racines te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison IV indique une maîtrise karmique de l'adaptabilité familiale. Tu sais changer, déménager et t'adapter aux différentes situations.",
        "L'instabilité des racines peut te piéger. Ta tendance à changer sans cesse te coupe de l'ancrage profond dont tu as besoin.",
        "Ton foyer porte la mémoire de la mobilité. Tu dois maintenant apprendre à t'ancrer et à créer des racines profondes.",
        "Établis quelque chose de permanent dans ton foyer.",
        "Respire en visualisant des racines qui s'enfoncent profondément.",
        "Comment mon besoin de changement m'empêche-t-il de créer un vrai foyer ? »"),

    ('gemini', 5): make_sn_interp('gemini', 5,
        "Tu arrives avec une maîtrise de la créativité intellectuelle — mais la dispersion créative te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison V indique une maîtrise karmique de la créativité mentale. Tu sais créer avec les mots, les idées et jouer avec l'esprit.",
        "La dispersion créative peut te piéger. Ta tendance à commencer mille projets sans en finir aucun te coupe de la création aboutie.",
        "Ta créativité porte la mémoire de l'éparpillement. Tu dois maintenant apprendre à créer avec passion et à finir ce que tu commences.",
        "Finis un projet créatif que tu avais abandonné.",
        "Respire en ancrant ton énergie créative dans UNE direction.",
        "Combien de projets créatifs ai-je abandonnés par manque de persévérance ? »"),

    ('gemini', 6): make_sn_interp('gemini', 6,
        "Tu arrives avec une maîtrise de la polyvalence au travail — mais la dispersion quotidienne te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison VI indique une maîtrise karmique du multitâche. Tu sais jongler avec plusieurs tâches et t'adapter aux changements.",
        "Le multitâche excessif peut te piéger. Ta tendance à faire plusieurs choses à la fois te coupe de l'efficacité et de la présence.",
        "Ton travail porte la mémoire de la dispersion. Tu dois maintenant apprendre à te concentrer et à faire une chose à la fois avec présence.",
        "Fais une tâche à la fois avec ta pleine attention.",
        "Respire en ancrant ta présence dans l'action présente.",
        "Comment mon multitâche réduit-il ma qualité de travail et de vie ? »"),

    ('gemini', 7): make_sn_interp('gemini', 7,
        "Tu arrives avec une maîtrise de la communication en couple — mais la légèreté relationnelle te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison VII indique une maîtrise karmique du dialogue. Tu sais communiquer avec ton partenaire et maintenir une relation stimulante.",
        "La légèreté et l'évitement des profondeurs peuvent te piéger. Ta tendance à parler sans vraiment te connecter te coupe de l'intimité.",
        "Tes relations portent la mémoire de la surface. Tu dois maintenant apprendre à aller en profondeur émotionnelle avec ton partenaire.",
        "Partage quelque chose de profond avec un partenaire, au-delà du bavardage.",
        "Respire en ouvrant ton cœur au-delà des mots.",
        "Quand est-ce que je parle avec mon partenaire sans vraiment me connecter ? »"),

    ('gemini', 8): make_sn_interp('gemini', 8,
        "Tu arrives avec une maîtrise de l'analyse des crises — mais l'intellectualisation te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison VIII indique une maîtrise karmique de la compréhension mentale des mystères. Tu sais analyser et expliquer les processus profonds.",
        "L'intellectualisation peut te piéger. Ta tendance à penser les transformations plutôt qu'à les vivre te coupe de la vraie métamorphose.",
        "Tes transformations portent la mémoire de la tête. Tu dois maintenant apprendre à vivre les crises plutôt qu'à les analyser.",
        "Vis une émotion intense sans l'analyser.",
        "Respire en descendant de ta tête vers ton corps et tes émotions.",
        "Quand est-ce que j'intellectualise au lieu de ressentir ? »"),

    ('gemini', 9): make_sn_interp('gemini', 9,
        "Tu arrives avec une maîtrise de l'apprentissage — mais l'accumulation de savoirs te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison IX indique une maîtrise karmique de la collecte d'informations. Tu sais apprendre, collecter et partager des connaissances.",
        "L'accumulation sans intégration peut te piéger. Ta tendance à collecter sans incarner te coupe de la vraie sagesse.",
        "Ta spiritualité porte la mémoire de l'intellect. Tu dois maintenant apprendre à incarner ce que tu sais, à vivre ta philosophie.",
        "Incarne un enseignement au lieu de juste le comprendre intellectuellement.",
        "Respire en laissant la connaissance descendre de ta tête vers ton cœur.",
        "Quelle sagesse que je connais bien n'ai-je pas encore incarnée ? »"),

    ('gemini', 10): make_sn_interp('gemini', 10,
        "Tu arrives avec une maîtrise de la communication professionnelle — mais la dispersion de carrière te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison X indique une maîtrise karmique de la polyvalence professionnelle. Tu sais communiquer et t'adapter dans ta carrière.",
        "La dispersion professionnelle peut te piéger. Ta tendance à changer de direction te coupe de la construction d'une vraie expertise.",
        "Ta carrière porte la mémoire de l'éparpillement. Tu dois maintenant apprendre à construire une expertise profonde et une réputation solide.",
        "Approfondis un domaine professionnel au lieu d'en explorer plusieurs.",
        "Respire en ancrant ta vision de carrière dans une direction claire.",
        "Comment ma polyvalence professionnelle m'empêche-t-elle de devenir expert ? »"),

    ('gemini', 11): make_sn_interp('gemini', 11,
        "Tu arrives avec une maîtrise du réseau social — mais les connexions superficielles te freinent.",
        "Le Nœud Sud en Gémeaux dans ta maison XI indique une maîtrise karmique du networking. Tu sais créer des connexions et maintenir un réseau étendu.",
        "Les amitiés superficielles peuvent te piéger. Ta tendance à avoir beaucoup de contacts sans vraie profondeur te coupe de l'amitié authentique.",
        "Tes amitiés portent la mémoire de la surface. Tu dois maintenant apprendre à approfondir quelques relations plutôt qu'à en avoir mille.",
        "Approfondis une amitié existante au lieu d'en créer de nouvelles.",
        "Respire en choisissant la qualité sur la quantité dans tes relations.",
        "Combien de mes contacts sont de vraies amitiés profondes ? »"),

    ('gemini', 12): make_sn_interp('gemini', 12,
        "Tu arrives avec une maîtrise de l'analyse de l'inconscient — mais le mental envahissant te freine.",
        "Le Nœud Sud en Gémeaux dans ta maison XII indique une maîtrise karmique de la compréhension du monde invisible. Tu sais analyser tes rêves et comprendre les symboles.",
        "Le mental hyperactif peut te piéger. Ta tendance à penser sans cesse te coupe de la paix intérieure et de la connexion mystique.",
        "Ton monde intérieur porte la mémoire du bavardage mental. Tu dois maintenant apprendre le silence et la connexion au-delà des mots.",
        "Médite en silence, sans analyser ce qui se passe.",
        "Respire en laissant ton mental se calmer complètement.",
        "Comment mon mental hyperactif m'empêche-t-il de trouver la paix ? »"),

    # === CANCER (M1-M12) ===
    ('cancer', 1): make_sn_interp('cancer', 1,
        "Tu arrives avec une maîtrise de la sensibilité et du soin — mais la dépendance émotionnelle te freine.",
        "Le Nœud Sud en Cancer dans ta maison I indique une maîtrise karmique de la sensibilité et de la protection. Tu sais prendre soin et te connecter émotionnellement.",
        "La dépendance émotionnelle peut te piéger. Ta tendance à te protéger excessivement te coupe de la confiance en toi et de l'action dans le monde.",
        "Ta présence porte la mémoire de l'enfant protégé. Tu dois maintenant apprendre l'indépendance et l'action dans le monde extérieur.",
        "Fais quelque chose d'autonome sans chercher le soutien émotionnel.",
        "Respire en te sentant fort et indépendant.",
        "Où ma dépendance émotionnelle m'empêche-t-elle de m'affirmer ? »"),

    ('cancer', 2): make_sn_interp('cancer', 2,
        "Tu arrives avec une maîtrise de la sécurité émotionnelle — mais l'attachement au confort te freine.",
        "Le Nœud Sud en Cancer dans ta maison II indique une maîtrise karmique de la création d'un nid sécuritaire. Tu sais accumuler ce qui te fait sentir en sécurité.",
        "L'attachement au confort peut te piéger. Ta tendance à t'entourer de sécurité te coupe de la prise de risque nécessaire à la croissance.",
        "Tes ressources portent la mémoire de la protection. Tu dois maintenant apprendre à partager tes ressources et à sortir de ta zone de confort.",
        "Partage quelque chose de précieux même si cela te rend vulnérable.",
        "Respire en relâchant le besoin de sécurité excessive.",
        "Qu'est-ce que j'accumule par peur plutôt que par besoin réel ? »"),

    ('cancer', 3): make_sn_interp('cancer', 3,
        "Tu arrives avec une maîtrise de la communication émotionnelle — mais la subjectivité te freine.",
        "Le Nœud Sud en Cancer dans ta maison III indique une maîtrise karmique de l'expression des sentiments. Tu sais communiquer avec le cœur et créer des liens affectifs.",
        "La subjectivité excessive peut te piéger. Ta tendance à tout filtrer par tes émotions te coupe de l'objectivité et du discernement.",
        "Ta communication porte la mémoire du cœur. Tu dois maintenant apprendre à équilibrer émotion et raison dans tes échanges.",
        "Communique quelque chose de façon objective, sans te laisser emporter par les émotions.",
        "Respire en équilibrant tête et cœur.",
        "Quand mes émotions colorent-elles trop ma perception de la réalité ? »"),

    ('cancer', 4): make_sn_interp('cancer', 4,
        "Tu arrives avec une maîtrise de la vie familiale — mais l'attachement au passé te freine.",
        "Le Nœud Sud en Cancer dans ta maison IV (son domicile) indique une maîtrise karmique profonde de la création d'un foyer. Tu sais créer un nid et nourrir les liens familiaux.",
        "L'attachement au passé et à la famille peut te piéger. Ta tendance à rester dans le cocon te coupe de ta mission dans le monde.",
        "Ton foyer porte la mémoire de la régression. Tu dois maintenant apprendre à sortir du nid et à construire ta place publique.",
        "Prends une initiative professionnelle au lieu de rester dans le confort du foyer.",
        "Respire en te sentant prêt à affronter le monde extérieur.",
        "Comment mon attachement au foyer me retient-il de construire ma carrière ? »"),

    ('cancer', 5): make_sn_interp('cancer', 5,
        "Tu arrives avec une maîtrise de l'amour maternel — mais la surprotection te freine.",
        "Le Nœud Sud en Cancer dans ta maison V indique une maîtrise karmique de l'amour nourricier. Tu sais aimer avec tendresse et protéger ce que tu crées.",
        "La surprotection peut te piéger. Ta tendance à materner tes créations et tes amours te coupe de leur autonomie et de ta liberté.",
        "Ta créativité porte la mémoire de la mère. Tu dois maintenant apprendre à créer et laisser partir, à aimer sans étouffer.",
        "Laisse une création ou un être aimé voler de ses propres ailes.",
        "Respire en relâchant le besoin de contrôler ce que tu aimes.",
        "Qui ou quoi étouffe-je par trop d'amour protecteur ? »"),

    ('cancer', 6): make_sn_interp('cancer', 6,
        "Tu arrives avec une maîtrise du soin aux autres — mais le sacrifice excessif te freine.",
        "Le Nœud Sud en Cancer dans ta maison VI indique une maîtrise karmique du service nourricier. Tu sais prendre soin des autres au quotidien.",
        "Le sacrifice de soi peut te piéger. Ta tendance à donner sans limites te coupe de ton propre bien-être et de ta croissance.",
        "Ton travail porte la mémoire du sacrifice. Tu dois maintenant apprendre à poser des limites et à prendre soin de toi aussi.",
        "Dis non à une demande de soin pour préserver ton énergie.",
        "Respire en te donnant à toi-même le soin que tu donnes aux autres.",
        "Comment mon excès de service aux autres me vide-t-il ? »"),

    ('cancer', 7): make_sn_interp('cancer', 7,
        "Tu arrives avec une maîtrise de l'intimité émotionnelle — mais la fusion te freine.",
        "Le Nœud Sud en Cancer dans ta maison VII indique une maîtrise karmique du lien émotionnel en couple. Tu sais créer une intimité profonde et nourrir la relation.",
        "La fusion peut te piéger. Ta tendance à te perdre dans l'autre te coupe de ton autonomie et de ta capacité à t'affirmer.",
        "Tes relations portent la mémoire de la dépendance. Tu dois maintenant apprendre l'équilibre entre intimité et autonomie.",
        "Fais quelque chose seul(e), même si ton partenaire est disponible.",
        "Respire en ressentant ta propre identité distincte de tes relations.",
        "Où me suis-je perdu(e) dans mes relations ? »"),

    ('cancer', 8): make_sn_interp('cancer', 8,
        "Tu arrives avec une maîtrise de la connexion émotionnelle profonde — mais l'attachement aux liens te freine.",
        "Le Nœud Sud en Cancer dans ta maison VIII indique une maîtrise karmique de l'intimité fusionnelle. Tu sais te connecter profondément et partager l'émotionnel.",
        "L'attachement aux liens peut te piéger. Ta tendance à t'accrocher aux connexions te coupe des transformations nécessaires.",
        "Tes transformations portent la mémoire de la fusion. Tu dois maintenant apprendre à lâcher les liens qui ne servent plus ta croissance.",
        "Lâche un lien émotionnel qui ne te sert plus.",
        "Respire en accueillant la transformation avec détachement.",
        "À quels liens émotionnels m'accroche-je malgré leur toxicité ? »"),

    ('cancer', 9): make_sn_interp('cancer', 9,
        "Tu arrives avec une maîtrise de la spiritualité intuitive — mais le repli dans le connu te freine.",
        "Le Nœud Sud en Cancer dans ta maison IX indique une maîtrise karmique de la sagesse du cœur. Tu sais te connecter spirituellement par l'intuition et le ressenti.",
        "Le repli sur les croyances familiales peut te piéger. Ta tendance à rester dans le connu te coupe de l'exploration spirituelle.",
        "Ta spiritualité porte la mémoire de la tradition. Tu dois maintenant apprendre à explorer de nouvelles voies et à élargir ta vision.",
        "Explore une croyance ou une pratique différente de tes traditions.",
        "Respire en ouvrant ton esprit au-delà du connu.",
        "Quelles traditions spirituelles me retiennent d'explorer plus loin ? »"),

    ('cancer', 10): make_sn_interp('cancer', 10,
        "Tu arrives avec une maîtrise du soin professionnel — mais la peur de l'exposition te freine.",
        "Le Nœud Sud en Cancer dans ta maison X indique une maîtrise karmique du travail nourricier. Tu sais prendre soin des autres professionnellement.",
        "La peur de l'exposition peut te piéger. Ta tendance à rester en retrait te coupe de la reconnaissance que tu mérites.",
        "Ta carrière porte la mémoire de la protection. Tu dois maintenant apprendre à t'exposer et à assumer ta place publique.",
        "Montre-toi professionnellement au lieu de rester en retrait.",
        "Respire en te sentant prêt à être vu dans le monde.",
        "Comment ma peur d'être vulnérable me cache-t-elle professionnellement ? »"),

    ('cancer', 11): make_sn_interp('cancer', 11,
        "Tu arrives avec une maîtrise des liens amicaux profonds — mais l'attachement au groupe te freine.",
        "Le Nœud Sud en Cancer dans ta maison XI indique une maîtrise karmique de la création de famille choisie. Tu sais créer des liens émotionnels forts dans les groupes.",
        "L'attachement au groupe peut te piéger. Ta tendance à faire du groupe ta famille te coupe de ton expression individuelle.",
        "Tes amitiés portent la mémoire de la famille. Tu dois maintenant apprendre à briller individuellement tout en restant connecté.",
        "Affirme ton unicité dans un groupe au lieu de te fondre.",
        "Respire en célébrant ta différence au sein du collectif.",
        "Comment mon besoin d'appartenance m'empêche-t-il de m'exprimer vraiment ? »"),

    ('cancer', 12): make_sn_interp('cancer', 12,
        "Tu arrives avec une maîtrise de la connexion émotionnelle à l'invisible — mais la fuite dans l'émotion te freine.",
        "Le Nœud Sud en Cancer dans ta maison XII indique une maîtrise karmique de la sensibilité psychique. Tu sais te connecter aux émotions collectives et à l'invisible.",
        "La fuite dans l'émotion peut te piéger. Ta tendance à te noyer dans les sentiments te coupe de l'action dans le monde.",
        "Ton monde intérieur porte la mémoire de la mer émotionnelle. Tu dois maintenant apprendre à sortir des eaux et à agir concrètement.",
        "Agis sur quelque chose au lieu de te perdre dans les émotions.",
        "Respire en ancrant tes émotions dans l'action.",
        "Où mes émotions me servent-elles d'excuse pour ne pas agir ? »"),
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0
        for (sign, house), content in SOUTH_NODE_INTERPRETATIONS.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'south_node',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()
            if existing:
                print(f"⏭️  SKIP south_node/{sign}/M{house}")
                skipped += 1
                continue
            interp = PregeneratedNatalInterpretation(
                subject='south_node',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT south_node/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1
        await db.commit()
        print(f"📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == "__main__":
    asyncio.run(insert_interpretations())
