#!/usr/bin/env python3
"""Script d'insertion des interprétations Jupiter/Leo en base."""

import asyncio
import sys
sys.path.insert(0, '/Users/remibeaurain/astroia/astroia-lunar/apps/api')

from sqlalchemy import select
from database import AsyncSessionLocal
from models.pregenerated_natal_interpretation import PregeneratedNatalInterpretation

JUPITER_LEO = {
    ('leo', 1): """# ♃ Jupiter en Lion
**En une phrase :** Tu incarnes une présence royale et généreuse qui attire naturellement l'attention et inspire confiance.

## Ton moteur
Jupiter en Lion en Maison 1 te donne une aura de leader charismatique. Tu rayonnes, tu occupes l'espace avec assurance, tu inspires les autres par ta simple présence. Cette configuration amplifie ton besoin de reconnaissance et ta capacité à la mériter par ton authenticité.

## Ton défi
Le piège : avoir besoin d'être au centre de l'attention, confondre confiance et arrogance, te sentir blessé quand on ne te remarque pas. Le vrai charisme n'a pas besoin d'applaudissements constants.

## Maison 1 en Lion
Jupiter amplifie ta première impression : on te perçoit comme quelqu'un de solaire, de généreux, de naturellement noble. Ton corps exprime ta royauté intérieure — posture droite, gestuelle ample.

## Micro-rituel du jour (2 min)
- Offrir un compliment sincère à quelqu'un qui le mérite
- Trois respirations en visualisant un soleil qui brille dans ta poitrine
- Journal : « Comment ai-je inspiré quelqu'un aujourd'hui par mon exemple ? »""",

    ('leo', 2): """# ♃ Jupiter en Lion
**En une phrase :** Tu développes tes ressources avec panache — ta valeur personnelle se manifeste dans ta capacité à créer et à donner généreusement.

## Ton moteur
Jupiter en Lion en Maison 2 te pousse à gagner de l'argent de façon créative et visible. Tu as besoin de fierté dans ta façon de générer des revenus. Les métiers artistiques, de leadership ou de représentation te conviennent naturellement.

## Ton défi
Le piège : dépenser de façon ostentatoire pour impressionner, confondre valeur personnelle et signes extérieurs de richesse, avoir du mal à gérer quand les ressources sont limitées. La vraie noblesse sait aussi être discrète.

## Maison 2 en Lion
Jupiter amplifie ton rapport royal à l'argent. Tu préfères la qualité à la quantité, le beau au pratique. Tes valeurs sont liées à la créativité, l'authenticité, la générosité. Tu donnes volontiers quand tu en as les moyens.

## Micro-rituel du jour (2 min)
- Identifier une dépense récente qui reflète vraiment qui tu es
- Trois respirations en visualisant ta valeur intérieure rayonner vers l'extérieur
- Journal : « Comment ma façon de gagner et dépenser reflète-t-elle ma vraie nature ? »""",

    ('leo', 3): """# ♃ Jupiter en Lion
**En une phrase :** Tu communiques avec éclat et conviction — tes mots portent une chaleur qui captive et inspire ceux qui t'écoutent.

## Ton moteur
Jupiter en Lion en Maison 3 te donne une communication dramatique et expressive. Tu racontes des histoires, tu exagères parfois pour l'effet, tu sais captiver un auditoire. Cette configuration favorise les métiers créatifs liés à la parole : théâtre, présentation, enseignement.

## Ton défi
Le piège : monopoliser la parole, avoir du mal à écouter quand tu n'es pas le centre de la conversation, dramatiser les situations ordinaires. La communication véritable laisse aussi de la place aux autres.

## Maison 3 en Lion
Jupiter amplifie ta présence dans les échanges quotidiens. Tes relations avec frères, sœurs et voisins sont teintées de jeux de pouvoir ou de rivalité créative. Tu apprends mieux quand on te laisse briller.

## Micro-rituel du jour (2 min)
- Partager une histoire ou une anecdote qui inspire ou amuse quelqu'un
- Trois respirations en visualisant tes mots comme des rayons de soleil
- Journal : « Quelle conversation m'a permis d'exprimer ma vraie nature récemment ? »""",

    ('leo', 4): """# ♃ Jupiter en Lion
**En une phrase :** Ton foyer est ton royaume — tu crées un chez-toi où tu peux régner avec chaleur et générosité sur ceux que tu aimes.

## Ton moteur
Jupiter en Lion en Maison 4 te donne un besoin de fierté dans ton espace de vie. Tu aimes recevoir, montrer ta maison, créer un intérieur qui reflète ton goût et ta personnalité. La famille est ton public et ton cercle de loyauté.

## Ton défi
Le piège : vouloir être le roi ou la reine chez toi au point d'écraser les autres, transformer le foyer en théâtre permanent, avoir du mal à partager le pouvoir domestique. Le vrai royaume accueille aussi les égaux.

## Maison 4 en Lion
Jupiter amplifie ton sens dramatique de la vie familiale. Tu as peut-être grandi avec un parent charismatique ou dans une famille qui valorisait l'expression personnelle. Ton foyer doit avoir quelque chose de spécial, d'unique.

## Micro-rituel du jour (2 min)
- Ajouter un élément de beauté ou de chaleur à ton espace de vie
- Trois respirations en visualisant ton foyer comme un soleil qui rayonne
- Journal : « Comment mon chez-moi exprime-t-il qui je suis vraiment ? »""",

    ('leo', 5): """# ♃ Jupiter en Lion
**En une phrase :** Tu vis la créativité comme une vocation — tes œuvres, tes amours et tes joies sont des expressions magnifiques de ton feu intérieur.

## Ton moteur
Jupiter en Lion en Maison 5 est une position royale pour la créativité et le plaisir. Tu as un talent naturel pour briller dans l'art, le théâtre, tout ce qui te met en scène. En amour, tu es généreux, passionné, parfois exigeant en retour.

## Ton défi
Le piège : avoir besoin de louanges constantes pour créer, transformer les relations amoureuses en compétition d'ego, utiliser les enfants comme extensions de ton narcissisme. La vraie créativité se suffit parfois à elle-même.

## Maison 5 en Lion
Jupiter amplifie ton talent pour le spectacle et le plaisir. Tu attires des partenaires qui admirent ta flamme ou qui rivalisent avec elle. Avec les enfants, tu es un parent ludique et fier, parfois exigeant.

## Micro-rituel du jour (2 min)
- Créer quelque chose de beau juste pour le plaisir d'exprimer qui tu es
- Trois respirations en sentant ta flamme créative s'intensifier
- Journal : « Quelle création récente me rend le plus fier de moi ? »""",

    ('leo', 6): """# ♃ Jupiter en Lion
**En une phrase :** Tu travailles avec fierté et excellence — chaque tâche quotidienne est une occasion de montrer ta valeur et ton savoir-faire.

## Ton moteur
Jupiter en Lion en Maison 6 te pousse à exceller dans ton travail quotidien. Tu as besoin de fierté dans ce que tu fais, même les tâches modestes. Cette configuration favorise les positions de leadership dans les équipes, la gestion créative.

## Ton défi
Le piège : avoir du mal à accomplir des tâches qui ne te mettent pas en valeur, être trop fier pour demander de l'aide, négliger les détails ennuyeux. L'excellence durable passe aussi par l'humilité.

## Maison 6 en Lion
Jupiter amplifie ton besoin de reconnaissance dans le travail quotidien. Tu travailles mieux quand on apprécie tes efforts. Ta santé est liée à ta vitalité émotionnelle — le cœur et le dos demandent attention.

## Micro-rituel du jour (2 min)
- Accomplir une tâche ordinaire avec excellence et fierté aujourd'hui
- Trois respirations en visualisant ton travail comme une œuvre d'art
- Journal : « Quelle tâche quotidienne mériterait plus de fierté de ma part ? »""",

    ('leo', 7): """# ♃ Jupiter en Lion
**En une phrase :** Tes relations sont des duos de stars — tu cherches des partenaires qui brillent autant que toi et avec qui tu peux créer quelque chose de grand.

## Ton moteur
Jupiter en Lion en Maison 7 te pousse vers des partenariats où les deux brillent. Tu attires des personnes charismatiques, parfois plus visibles que toi, parfois qui te mettent en valeur. L'amour doit avoir quelque chose de royal, de spécial.

## Ton défi
Le piège : rivaliser avec ton partenaire plutôt que de collaborer, avoir besoin que la relation soit toujours extraordinaire, fuir l'ordinaire du quotidien à deux. Les meilleures relations acceptent aussi les moments simples.

## Maison 7 en Lion
Jupiter amplifie ton besoin de fierté dans tes partenariats. Tu peux t'associer avec des personnes de haut rang ou créatives. Tes contrats et mariages ont besoin de cérémonies, de reconnaissance publique.

## Micro-rituel du jour (2 min)
- Célébrer quelque chose que tu admires chez ton partenaire
- Trois respirations en visualisant votre couple comme deux soleils qui dansent
- Journal : « Comment mon partenaire me permet-il de briller ? Et inversement ? »""",

    ('leo', 8): """# ♃ Jupiter en Lion
**En une phrase :** Tu traverses les crises avec courage et dignité — les transformations deviennent des occasions de révéler ta vraie grandeur.

## Ton moteur
Jupiter en Lion en Maison 8 te donne une capacité à traverser les épreuves en gardant la tête haute. Tu refuses de te laisser abattre, tu trouves de la fierté même dans les moments difficiles. Cette configuration peut apporter des héritages liés à des personnes de pouvoir.

## Ton défi
Le piège : refuser de montrer ta vulnérabilité même quand c'est nécessaire, transformer les crises en spectacles, avoir du mal à accepter l'aide des autres. La vraie force sait aussi s'incliner.

## Maison 8 en Lion
Jupiter amplifie ta capacité à rebondir avec panache. Tu peux hériter de personnes créatives ou de positions de pouvoir. Ta sexualité est liée au jeu, à la séduction, au besoin de briller même dans l'intimité.

## Micro-rituel du jour (2 min)
- Identifier une crise passée dont tu es sorti plus fort et célébrer cette force
- Trois respirations en visualisant le phénix qui renaît de ses cendres avec éclat
- Journal : « Comment les épreuves ont-elles révélé ma vraie grandeur ? »""",

    ('leo', 9): """# ♃ Jupiter en Lion
**En une phrase :** Ta quête de sens est une aventure héroïque — tu cherches une philosophie qui te permette de vivre pleinement et d'inspirer les autres.

## Ton moteur
Jupiter en Lion en Maison 9 te donne une soif de grandes idées et de grandes expériences. Tu veux une philosophie qui enflamme, une spiritualité qui élève. Les voyages doivent être épiques, les études doivent mener à quelque chose de grand.

## Ton défi
Le piège : avoir besoin d'être le gourou plutôt que l'élève, chercher les philosophies qui te mettent au centre, confondre charisme et sagesse. La vraie connaissance sait aussi se faire humble.

## Maison 9 en Lion
Jupiter amplifie ton besoin d'aventures qui te grandissent. Tu peux enseigner, écrire, voyager de façon qui te met en lumière. Ta spiritualité est souvent liée à l'expression créative ou au développement personnel glorifiant.

## Micro-rituel du jour (2 min)
- Partager une idée ou une conviction qui t'inspire profondément avec quelqu'un
- Trois respirations en visualisant ta vision qui s'élargit comme un horizon doré
- Journal : « Quelle grande idée guide ma vie en ce moment ? »""",

    ('leo', 10): """# ♃ Jupiter en Lion
**En une phrase :** Ta carrière est une scène — tu vises les sommets avec charisme et tu inspires les autres par ton ascension brillante.

## Ton moteur
Jupiter en Lion en Maison 10 te pousse vers des positions de visibilité et de leadership. Tu as besoin d'une carrière qui te permette de briller, d'être reconnu, d'avoir un impact visible. Les métiers créatifs, de direction ou de représentation te conviennent.

## Ton défi
Le piège : mesurer ta réussite uniquement par la reconnaissance extérieure, avoir du mal avec les rôles de second plan, confondre célébrité et accomplissement. Le vrai succès n'a pas toujours besoin de projecteurs.

## Maison 10 en Lion
Jupiter amplifie ta visibilité professionnelle au maximum. On te remarque, on te confie des responsabilités prestigieuses. Ta réputation est liée à ton charisme, ta créativité, ta générosité avec ton équipe.

## Micro-rituel du jour (2 min)
- Identifier une action professionnelle qui te mettrait vraiment en valeur
- Trois respirations en visualisant ta place au sommet, rayonnante
- Journal : « Comment ma carrière exprime-t-elle ma vraie grandeur ? »""",

    ('leo', 11): """# ♃ Jupiter en Lion
**En une phrase :** Tu fédères des troupes autour de visions grandioses — tes amitiés sont des alliances entre personnes qui veulent changer le monde.

## Ton moteur
Jupiter en Lion en Maison 11 te donne un talent pour inspirer les groupes et fédérer autour de grandes causes. Tu attires des amis brillants, parfois célèbres, toujours passionnés. Tes projets collectifs ont de l'ambition.

## Ton défi
Le piège : avoir besoin d'être le leader de chaque groupe, attirer l'attention au détriment de la cause, t'entourer de courtisans plutôt que de vrais amis. Les meilleures communautés sont des cercles, pas des royaumes.

## Maison 11 en Lion
Jupiter amplifie ton influence dans les réseaux. Tu peux attirer des amis créatifs ou de haut rang. Tes projets humanitaires ont de l'envergure et visent à laisser une marque durable.

## Micro-rituel du jour (2 min)
- Proposer une vision inspirante à un groupe ou un ami aujourd'hui
- Trois respirations en visualisant ta communauté comme une constellation brillante
- Journal : « Quel projet collectif me permettrait de laisser une vraie marque ? »""",

    ('leo', 12): """# ♃ Jupiter en Lion
**En une phrase :** Tu explores l'invisible avec majesté — ta spiritualité est une quête de la lumière intérieure qui veut rayonner même dans l'ombre.

## Ton moteur
Jupiter en Lion en Maison 12 crée une tension entre ton besoin de briller et le monde caché de l'inconscient. Tu as peut-être une mission secrète, une grandeur qui ne se montre pas. Ta spiritualité cherche le divin en toi.

## Ton défi
Le piège : avoir besoin de reconnaissance même dans ta vie spirituelle, fuir l'ombre parce qu'elle ne brille pas, confondre ego et âme. La vraie lumière intérieure n'a pas besoin de public.

## Maison 12 en Lion
Jupiter amplifie ta quête d'une royauté intérieure. Tu peux avoir des talents cachés, une créativité qui s'exprime dans l'ombre, une générosité secrète. Les retraites créatives ou les pratiques qui connectent au cœur te régénèrent.

## Micro-rituel du jour (2 min)
- Faire un acte de générosité anonyme aujourd'hui
- Trois respirations en visualisant un soleil qui brille à l'intérieur, sans public
- Journal : « Quelle partie de ma grandeur reste cachée et mérite d'être honorée ? »""",
}

async def insert_interpretations():
    async with AsyncSessionLocal() as db:
        inserted = 0
        skipped = 0

        for (sign, house), content in JUPITER_LEO.items():
            result = await db.execute(
                select(PregeneratedNatalInterpretation).where(
                    PregeneratedNatalInterpretation.subject == 'jupiter',
                    PregeneratedNatalInterpretation.sign == sign,
                    PregeneratedNatalInterpretation.house == house,
                    PregeneratedNatalInterpretation.version == 2,
                    PregeneratedNatalInterpretation.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                print(f"⏭️  SKIP jupiter/{sign}/M{house}")
                skipped += 1
                continue

            interp = PregeneratedNatalInterpretation(
                subject='jupiter',
                sign=sign,
                house=house,
                version=2,
                lang='fr',
                content=content.strip(),
                length=len(content.strip())
            )
            db.add(interp)
            print(f"✅ INSERT jupiter/{sign}/M{house} ({len(content.strip())} chars)")
            inserted += 1

        await db.commit()
        print(f"\n📊 Résultat: {inserted} insérées, {skipped} ignorées")

if __name__ == '__main__':
    asyncio.run(insert_interpretations())
