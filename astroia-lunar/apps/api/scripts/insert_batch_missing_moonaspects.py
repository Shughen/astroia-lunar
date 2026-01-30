"""
Insertion des 10 aspects manquants : Moon-Sun et Moon-Uranus (version=5)
Ces aspects n'ont jamais été insérés malgré progress.json
"""

import asyncio
import sys
from pathlib import Path

# Ajouter le répertoire parent au path
sys.path.insert(0, str(Path(__file__).parent.parent))

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from models.pregenerated_natal_aspect import PregeneratedNatalAspect
from config import settings

# Aspects Moon-Sun (5 aspects)
MOON_SUN_ASPECTS = {
    "conjunction": """# ☌ Conjonction Lune - Soleil

**En une phrase :** Tes émotions et ton identité ne font qu'un — authenticité brute ou confusion totale.

## L'énergie de cet aspect

Quand la Lune (besoins, émotions, inconscient) fusionne avec le Soleil (identité, volonté, conscience), il n'y a plus de filtre entre ce que tu ressens et ce que tu es. Cette conjonction crée une authenticité spontanée : impossible de cacher tes états d'âme. Ce que tu vis intérieurement devient immédiatement visible. C'est une force (sincérité désarmante) et un piège (difficulté à prendre du recul).

## Manifestations concrètes

- **Expression directe** : Tes émotions s'affichent sur ton visage avant même que tu en sois conscient
- **Besoin de cohérence** : Tu ne supportes pas la dissonance entre ce que tu ressens et ce que tu montres
- **Réactivité émotionnelle** : Tes réactions sont spontanées, immédiates, sans censure
- **Identité émotionnelle** : Tu te définis souvent par tes humeurs, tes besoins, ton ressenti

## Conseil pratique

Cultive des moments d'observation de tes émotions sans t'identifier à elles. Ton authenticité est précieuse, mais elle devient toxique si tu confonds "ressentir" et "être".

## Attention

Gare à croire que tes émotions définissent qui tu es. L'humeur du moment n'est pas ta vérité permanente — apprends à faire la différence.""",

    "opposition": """# ☍ Opposition Lune - Soleil

**En une phrase :** Tiraillé entre tes besoins et ton identité — la quête d'équilibre commence ici.

## L'énergie de cet aspect

L'opposition Lune-Soleil crée une tension entre ce dont tu as besoin (Lune) et ce que tu veux devenir (Soleil). Tu te sens souvent coupé en deux : une partie cherche la sécurité, l'autre veut briller et avancer. Cette polarité peut générer du stress, mais c'est aussi elle qui te pousse à grandir. Chaque pôle révèle ce que l'autre occulte.

## Manifestations concrètes

- **Double bind** : Tu veux être reconnu (Soleil) mais tu as besoin de sécurité émotionnelle (Lune)
- **Relations miroirs** : Les autres reflètent souvent un pôle que tu rejettes en toi
- **Alternance** : Tantôt dans l'action visible, tantôt dans le cocooning émotionnel
- **Lucidité forcée** : Cette tension t'empêche de t'illusionner longtemps

## Conseil pratique

Ne cherche pas à éliminer un pôle. Ton défi est l'intégration : comment honorer tes besoins tout en assumant ton identité ? Les deux sont vrais.

## Attention

Gare à projeter un des deux pôles sur les autres (ex: devenir hyper-solaire et attirer des partenaires hyper-lunaires). L'équilibre se trouve en toi, pas dans l'externe.""",

    "square": """# □ Carré Lune - Soleil

**En une phrase :** Friction interne entre émotions et volonté — ce qui te met en mouvement malgré toi.

## L'énergie de cet aspect

Le carré Lune-Soleil crée une friction constante entre tes besoins émotionnels et ton identité consciente. Ce que tu ressens ne colle pas naturellement avec ce que tu veux être. Cette tension génère une énergie puissante : l'inconfort te pousse à agir, à trouver des solutions, à évoluer. Mais elle peut aussi créer du stress chronique si tu nies l'un des deux pôles.

## Manifestations concrètes

- **Insatisfaction motrice** : Tu es rarement totalement à l'aise, ce qui te pousse à avancer
- **Décalage interne** : Ton humeur sabote parfois tes objectifs (ou inversement)
- **Résilience** : L'habitude de la friction te rend plus fort face aux obstacles
- **Autodiscipline** : Tu dois apprendre à gérer tes émotions pour accomplir tes projets

## Conseil pratique

Transforme cette friction en énergie créative. Ne cherche pas à supprimer le conflit — utilise-le comme carburant. Les plus grands accomplissements naissent souvent de cette tension.

## Attention

Gare à l'auto-sabotage : tes émotions peuvent bloquer tes projets si tu ne leur accordes pas d'espace. Et inversement, ton ambition peut écraser tes besoins légitimes. Ni l'un ni l'autre ne doit gagner — ils doivent collaborer.""",

    "trine": """# △ Trigone Lune - Soleil

**En une phrase :** Harmonie naturelle entre émotions et identité — fluidité qui peut endormir.

## L'énergie de cet aspect

Le trigone Lune-Soleil crée une harmonie facile entre tes besoins émotionnels et ton identité consciente. Ce que tu ressens et ce que tu veux être s'alignent naturellement. Cette fluidité te donne une personnalité cohérente, équilibrée, sans grandes tensions internes. Ton authenticité coule de source. Mais attention : l'excès d'harmonie peut t'endormir.

## Manifestations concrètes

- **Aisance relationnelle** : Les gens te trouvent facile à vivre, authentique, fiable
- **Cohérence interne** : Pas de grand écart entre ton ressenti et ton expression
- **Confiance en soi naturelle** : Tu ne te bats pas contre toi-même, ça libère de l'énergie
- **Risque de complaisance** : L'absence de friction peut te rendre passif

## Conseil pratique

Utilise cette harmonie comme base, pas comme but. Tu as la chance de ne pas gaspiller d'énergie en conflits internes — alors investi-la dans des défis externes. Ne te repose pas sur tes lauriers.

## Attention

Gare à la complaisance. L'harmonie facile peut te rendre frileux face aux défis. Explore aussi les ombres : intègre consciemment les parts difficiles de ton identité et de tes émotions. La facilité n'est pas toujours synonyme de profondeur.""",

    "sextile": """# ⚹ Sextile Lune - Soleil

**En une phrase :** Opportunités d'alignement entre émotions et volonté — potentiel à activer.

## L'énergie de cet aspect

Le sextile Lune-Soleil offre des opportunités d'harmonisation entre tes besoins émotionnels et ton identité. Contrairement au trigone (harmonie automatique), le sextile demande une activation consciente. Les deux énergies sont compatibles, mais c'est à toi de créer les ponts. Quand tu le fais, tu gagnes en cohérence interne et en efficacité.

## Manifestations concrètes

- **Potentiel d'équilibre** : Tu peux facilement aligner émotions et objectifs si tu t'en donnes la peine
- **Adaptabilité** : Tu sais jongler entre tes besoins et tes ambitions sans trop de friction
- **Communication fluide** : Tu exprimes tes émotions de manière constructive quand tu es conscient
- **Besoin d'initiative** : L'harmonie n'arrive pas toute seule, il faut la cultiver

## Conseil pratique

Prends des micro-décisions quotidiennes qui honorent à la fois tes besoins (Lune) et ton identité (Soleil). Rituel du matin qui nourrit ton âme + action qui affirme qui tu es. Le sextile récompense les petits efforts.

## Attention

Gare à la passivité. Le sextile est comme un jardin fertile : si tu ne plantes rien, il ne pousse rien. Ne confonds pas potentiel et réalisation — l'opportunité doit être saisie."""
}

# Aspects Moon-Uranus (5 aspects)
MOON_URANUS_ASPECTS = {
    "conjunction": """# ☌ Conjonction Lune - Uranus

**En une phrase :** Tes émotions deviennent électriques — instabilité créative ou chaos émotionnel.

## L'énergie de cet aspect

Quand la Lune (besoins, sécurité, émotions) fusionne avec Uranus (rupture, liberté, innovation), ton monde émotionnel devient imprévisible. Tu ressens les choses par flashs, tes besoins changent brutalement, et tu as une hypersensibilité aux énergies collectives. Cette conjonction crée une intelligence émotionnelle unique mais instable — tu captes des choses que les autres ne voient pas, mais tu paies le prix de cette clairvoyance erratique.

## Manifestations concrètes

- **Humeurs électriques** : Passage de l'excitation à l'anxiété en quelques minutes
- **Besoin de liberté émotionnelle** : Toute forme de routine affective te suffoqu e
- **Intuitions fulgurantes** : Des insights émotionnels qui arrivent comme l'éclair
- **Difficulté à s'ancrer** : Les habitudes rassurantes te semblent étouffantes

## Conseil pratique

Crée des structures souples : rituels quotidiens courts que tu peux modifier selon ton humeur. Note tes intuitions soudaines mais attends 24h avant d'agir dessus. L'électricité émotionnelle est juste, mais le timing peut être erratique.

## Attention

Gare à saboter tes bases émotionnelles juste parce que tu t'ennuies. L'agitation intérieure n'est pas toujours un signal de danger — parfois c'est juste Uranus qui teste la solidité de tes fondations. Apprends à distinguer l'intuition vraie du simple besoin de stimulation.""",

    "opposition": """# ☍ Opposition Lune - Uranus

**En une phrase :** Tiraillé entre sécurité et liberté — la quête d'une indépendance émotionnelle saine.

## L'énergie de cet aspect

L'opposition Lune-Uranus crée une tension entre ton besoin de sécurité émotionnelle (Lune) et ton besoin de liberté radicale (Uranus). Tu oscilles entre le cocooning et la rupture, entre l'attachement et la fuite. Les autres te renvoient souvent ce que tu rejettes : soit des gens trop envahissants, soit des électrons libres insaisissables. Cette polarité te pousse à redéfinir ce que "sécurité" veut dire pour toi.

## Manifestations concrètes

- **Ambivalence relationnelle** : Tu veux de la proximité mais tu as peur de perdre ton autonomie
- **Ruptures soudaines** : Quand la pression émotionnelle monte, tu peux couper brutalement
- **Relations miroirs** : Tu attires des gens qui incarnent soit la dépendance soit l'indépendance extrême
- **Lucidité sur les attachements** : Cette tension t'empêche de tomber dans l'illusion fusionnelle

## Conseil pratique

Apprends à créer de la sécurité dans la liberté. Intimité n'est pas synonyme de dépendance. Trouve des relations qui respectent ton besoin d'espace tout en offrant une base émotionnelle solide.

## Attention

Gare à fuir systématiquement dès que tu te sens vulnérable. La vraie liberté n'est pas l'absence de liens — c'est la capacité à choisir consciemment tes attachements. Et inversement, ne sacrifie pas ton besoin d'autonomie juste pour te sentir en sécurité.""",

    "square": """# □ Carré Lune - Uranus

**En une phrase :** Friction entre stabilité émotionnelle et besoin de changement — énergie explosive à canaliser.

## L'énergie de cet aspect

Le carré Lune-Uranus crée une friction constante entre ton besoin de sécurité et ton besoin de rupture. Tu te sens coincé dans un paradoxe : tu veux de la stabilité émotionnelle, mais dès que tu l'obtiens, tu as envie de tout faire exploser. Cette tension génère une énergie puissante mais inconfortable. Elle peut se manifester par de l'anxiété chronique ou devenir un moteur de transformation.

## Manifestations concrètes

- **Stress émotionnel chronique** : Sensation d'être sous tension, prêt à exploser
- **Réactions imprévisibles** : Tes émotions te surprennent toi-même par leur intensité soudaine
- **Sabotage inconscient** : Tu peux détruire ce qui te sécurise sans comprendre pourquoi
- **Créativité sous pression** : Tes meilleures idées naissent souvent du chaos émotionnel

## Conseil pratique

Transforme cette friction en innovation émotionnelle. Au lieu de subir le chaos, deviens l'architecte de tes propres révolutions intérieures. Fais des micro-ruptures contrôlées : change un rituel par semaine, expérimente de nouvelles façons de gérer tes émotions.

## Attention

Gare à l'auto-sabotage compulsif. Si tu détruis systématiquement ce qui te fait du bien, tu ne changes rien — tu tournes en rond. La vraie liberté émotionnelle demande parfois de la constance et de la discipline, pas juste des ruptures spectaculaires.""",

    "trine": """# △ Trigone Lune - Uranus

**En une phrase :** Harmonie entre stabilité et innovation — créativité émotionnelle fluide.

## L'énergie de cet aspect

Le trigone Lune-Uranus crée une harmonie naturelle entre ton besoin de sécurité et ton besoin de liberté. Tu as l'aisance rare de pouvoir innover émotionnellement sans te détruire. Cette fluidité te donne une intelligence émotionnelle originale : tu captes des intuitions justes, tu t'adaptes facilement aux changements, et tu crées de la nouveauté sans dramatiser.

## Manifestations concrètes

- **Intuition fiable** : Tes flashs émotionnels sont souvent justes et exploitables
- **Adaptabilité émotionnelle** : Tu gères les changements sans paniquer
- **Originalité naturelle** : Tes besoins ne sont pas conventionnels, mais tu assumes
- **Facilité avec le futur** : Tu anticipes les transformations nécessaires sans résistance

## Conseil pratique

Utilise cette aisance pour aider les autres à naviguer leurs propres chaos émotionnels. Tu as un don pour montrer qu'on peut être stable ET libre. Partage tes stratégies : comment tu crées de la sécurité dans l'imprévu, comment tu innoves sans tout casser.

## Attention

Gare à prendre ton aisance pour acquise. Si tu ne nourris pas consciemment cette harmonie, elle peut s'endormir. Cherche activement les opportunités d'innover émotionnellement — ne te repose pas sur le pilote automatique. L'harmonie facile peut devenir de la complaisance si tu ne la défies pas.""",

    "sextile": """# ⚹ Sextile Lune - Uranus

**En une phrase :** Opportunités d'innovation émotionnelle — potentiel à activer consciemment.

## L'énergie de cet aspect

Le sextile Lune-Uranus offre des opportunités d'harmonisation entre sécurité et liberté. Contrairement au trigone (harmonie automatique), le sextile demande une activation consciente. Tu as le potentiel de créer une vie émotionnelle originale et stable à la fois, mais c'est à toi de saisir les occasions. Quand tu le fais, tu gagnes en authenticité et en résilience.

## Manifestations concrètes

- **Potentiel d'innovation** : Tu peux facilement expérimenter de nouvelles façons de gérer tes émotions
- **Adaptabilité consciente** : Tu sais quand il faut changer et quand il faut tenir
- **Intuitions exploitables** : Tes flashs émotionnels sont pertinents si tu les écoutes
- **Besoin d'initiative** : L'harmonie n'arrive pas toute seule, il faut la cultiver

## Conseil pratique

Chaque mois, expérimente un nouveau rituel émotionnel. Change une habitude qui ne te sert plus, teste une approche inédite. Le sextile récompense les micro-innovations : tu n'as pas besoin de tout révolutionner d'un coup. Petits ajustements, grands effets.

## Attention

Gare à la passivité. Le sextile est comme une porte entrouverte : si tu ne la pousses pas, elle ne s'ouvre pas toute seule. Ne confonds pas potentiel et réalisation — l'opportunité doit être saisie. Si tu attends que le changement vienne de l'extérieur, tu passes à côté de ton pouvoir."""
}


async def insert_aspects():
    """Insère les 10 aspects manquants en base de données"""

    # Connexion DB
    engine = create_async_engine(
        settings.DATABASE_URL.replace('postgresql+asyncpg', 'postgresql+asyncpg'),
        echo=False
    )

    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    inserted_count = 0

    async with async_session() as session:
        # Insérer Moon-Sun (5 aspects)
        for aspect_type, content in MOON_SUN_ASPECTS.items():
            aspect = PregeneratedNatalAspect(
                planet1='moon',
                planet2='sun',
                aspect_type=aspect_type,
                version=5,
                lang='fr',
                content=content,
                length=len(content)
            )

            # Upsert: si existe déjà, update
            result = await session.execute(
                select(PregeneratedNatalAspect).where(
                    PregeneratedNatalAspect.planet1 == 'moon',
                    PregeneratedNatalAspect.planet2 == 'sun',
                    PregeneratedNatalAspect.aspect_type == aspect_type,
                    PregeneratedNatalAspect.version == 5,
                    PregeneratedNatalAspect.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                existing.content = content
                existing.length = len(content)
                print(f"✏️  Mis à jour: moon-sun {aspect_type}")
            else:
                session.add(aspect)
                inserted_count += 1
                print(f"✅ Inséré: moon-sun {aspect_type}")

        # Insérer Moon-Uranus (5 aspects)
        for aspect_type, content in MOON_URANUS_ASPECTS.items():
            aspect = PregeneratedNatalAspect(
                planet1='moon',
                planet2='uranus',
                aspect_type=aspect_type,
                version=5,
                lang='fr',
                content=content,
                length=len(content)
            )

            # Upsert
            result = await session.execute(
                select(PregeneratedNatalAspect).where(
                    PregeneratedNatalAspect.planet1 == 'moon',
                    PregeneratedNatalAspect.planet2 == 'uranus',
                    PregeneratedNatalAspect.aspect_type == aspect_type,
                    PregeneratedNatalAspect.version == 5,
                    PregeneratedNatalAspect.lang == 'fr'
                )
            )
            existing = result.scalar_one_or_none()

            if existing:
                existing.content = content
                existing.length = len(content)
                print(f"✏️  Mis à jour: moon-uranus {aspect_type}")
            else:
                session.add(aspect)
                inserted_count += 1
                print(f"✅ Inséré: moon-uranus {aspect_type}")

        await session.commit()

    print(f"\n✅ {inserted_count} aspects insérés (version=5, lang=fr)")

    # Vérification
    async with async_session() as session:
        result = await session.execute(
            select(PregeneratedNatalAspect).where(
                PregeneratedNatalAspect.version == 5
            )
        )
        total_v5 = len(result.scalars().all())
        print(f"🔍 Vérification BD : {total_v5} aspects version=5 lang=fr")


if __name__ == "__main__":
    asyncio.run(insert_aspects())
