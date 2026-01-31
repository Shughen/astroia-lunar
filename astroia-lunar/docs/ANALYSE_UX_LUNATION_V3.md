# Analyse UX/UI — Lunation v3.0

**Date** : 30 janvier 2026  
**Version analysée** : v3.0 (affichée v2.0 dans l'app)  
**Nombre de captures** : 34  
**Objectif** : Validation pré-bêta test  

---

## Score global : 16.75/20

| Lot | Captures | Note |
|-----|----------|------|
| Lot 1 | 1-20 (Onboarding → Home → Rapport) | 17/20 |
| Lot 2 | 21-34 (Journal → Profil → Thème natal → Calendrier) | 16.5/20 |

**Verdict** : App prête pour les bêta-testeurs avec corrections mineures recommandées.

---

## Sommaire

1. [Points forts](#points-forts)
2. [Problèmes critiques](#problèmes-critiques)
3. [Problèmes importants](#problèmes-importants)
4. [Améliorations suggérées](#améliorations-suggérées)
5. [Analyse détaillée par écran](#analyse-détaillée-par-écran)
6. [Checklist pré-bêta](#checklist-pré-bêta)

---

## Points forts

### Design & Identité visuelle ✨

- **Palette cohérente** : Dégradés violet/lavande maîtrisés de bout en bout
- **Roue du thème natal** : Magnifique, lisible, professionnelle
- **Icônes et emojis** : Utilisés avec parcimonie et pertinence
- **Cards et sections** : Hiérarchie visuelle claire
- **Écran de chargement** : Animation charmante (sablier + lune + étoiles) avec transparence sur l'IA utilisée

### Cohérence des données ✅

- **Dates du cycle lunaire harmonisées** : "6 janv - 2 févr" partout
- **Thème natal cohérent** : Naissance avril 1989 → Soleil Bélier ✓
- **Big 3 aligné** : Soleil Bélier, Lune Lion, Ascendant Vierge
- **Phases lunaires sans doublons** : 4 phases distinctes affichées

### Contenu & Interprétations 📝

- **Qualité des textes IA** : Interprétations personnalisées et pertinentes
- **Structure des aspects** : Données factuelles → En bref → Pourquoi → Manifestations → Conseil → Attention
- **Disclaimer responsable** : "L'astrologie comme boussole, pas comme GPS"
- **Bloc "Attention"** : Bordure orange efficace pour les mises en garde

### UX & Navigation 🧭

- **Onboarding fluide** : 4 étapes claires avec progression visible
- **Tutoriel post-onboarding** : Explique bien les fonctionnalités clés
- **Bottom sheet quotidien** : Très riche (guidance, énergies, mansion lunaire, rituels)
- **Profil complet** : Informations de naissance + notifications + actions compte

### Fonctionnalités avancées 🔮

- **Positions planétaires exhaustives** : Toutes les planètes jusqu'à Neptune
- **12 maisons astrologiques** : Avec signe et degré
- **Aspects avec orbes** : Classification (exact, serré, moyen, large)
- **Mansions lunaires** : Touche distinctive rare dans les apps astro
- **Jauges d'énergie** : Créativité et Intuition en pourcentage

---

## Problèmes critiques

### 1. Incohérence tutoiement/vouvoiement

**Gravité** : 🔴 Critique — Casse l'immersion

L'app utilise le tutoiement partout SAUF dans certains endroits :

| Écran | Texte problématique | Correction |
|-------|---------------------|------------|
| Journal - Modal confirmation | "Votre entrée a été enregistrée avec succès" | "Ton entrée a été enregistrée avec succès" |
| Journal - Placeholder | "Comment vous sentez-vous aujourd'hui ?" | "Comment te sens-tu aujourd'hui ?" |
| Journal - Sous-titre | "Un espace pour votre rituel quotidien" | "Un espace pour ton rituel quotidien" |
| Bottom sheet - Rituel | "Remerciez pour ce qui se manifeste" | "Remercie pour ce qui se manifeste" |
| Révolution lunaire - Interprétation | "Votre sensibilité spirituelle est exacerbée, votre imaginaire foisonnant. Laissez-vous guider par vos ressentis..." | Tout passer au tutoiement |

**Cause probable** : Templates ou prompts backend différents selon les sections.

**Fichiers à vérifier** :
```
apps/mobile/app/journal/
apps/api/prompts/lunar_return_interpretation.txt
apps/api/services/ai_interpretation.py
```

---

### 2. Version affichée incorrecte

**Gravité** : 🔴 Critique — Confusion pour les testeurs

**Localisation** : Profil (bas de page)

**Actuel** : "Lunation v2.0"  
**Attendu** : "Lunation v3.0"

**Fichier à corriger** :
```typescript
// Probablement dans constants/app.ts ou app.json
export const APP_VERSION = "3.0";
```

---

### 3. État de chargement technique visible

**Gravité** : 🟠 Important

**Localisation** : Onboarding étape 2/4 (création profil)

**Problème** : Pendant le calcul, l'utilisateur voit :
- LUNE : "Calcul API..."
- ASCENDANT : "Lieu requis"

**Impact** : Impression d'app non finie.

**Correction** : Remplacer par un loader animé ou "—" ou "En attente..."

---

## Problèmes importants

### 4. Termes anglais dans les aspects de révolution lunaire

**Localisation** : Écran "Révolution Lunaire Janvier 2026"

**Problème** :
- "Soleil conjunction Vénus" → "Soleil conjonction Vénus"
- "Lune square Uranus" → "Lune carré Uranus"
- "Mercure square Neptune" → "Mercure carré Neptune"

**Note** : Dans le thème natal, les termes sont en français ("conjonction", "trigone", "carré"). Incohérence.

**Cause probable** : L'API de calcul retourne les noms d'aspects en anglais et ils ne sont pas traduits pour cet écran.

---

### 5. Espacement manquant dans le profil

**Localisation** : Profil → Informations de naissance

**Problème** : "Lieu de naissance**Livry-Gargan, Île-de-France, France**"

Le label et la valeur sont collés sans espace ni séparateur.

**Correction** :
```typescript
// Ajouter un espace ou utiliser une structure cohérente
<Text style={styles.label}>Lieu de naissance :</Text>
<Text style={styles.value}>Livry-Gargan, Île-de-France, France</Text>
```

---

### 6. Loader flottant sans contexte

**Localisation** : Home (en scroll)

**Problème** : Un cercle de chargement apparaît au milieu de la HeroCard sans explication.

**Correction** : Soit le masquer, soit ajouter un texte contextuel, soit le positionner de manière moins intrusive.

---

### 7. Section "Transits du jour" vide mais aspects existent

**Localisation** : Bottom sheet quotidien

**Problème** : Affiche "Aucun transit majeur ce mois-ci" alors que le rapport mensuel montre "5 aspects identifiés".

**Explication** : Les "aspects" du rapport sont ceux de la révolution lunaire, tandis que les "transits du jour" sont les transits planétaires temps réel. Mais la distinction n'est pas claire.

**Amélioration** : Clarifier le wording ou afficher un résumé des aspects du mois si les transits sont vides.

---

## Améliorations suggérées

### 8. Icône warning uniforme sur tous les aspects

**Localisation** : Thème natal → Aspects Majeurs

**Problème** : Tous les aspects affichent ⚠️, même les trigones (harmoniques).

**Suggestion** :
| Type d'aspect | Icône suggérée |
|---------------|----------------|
| Trigone, Sextile | ✨ ou 💚 (harmonique) |
| Carré, Opposition | ⚠️ (tendu) |
| Conjonction | 🔄 ou ⭐ (neutre/puissant) |

---

### 9. "Touchez pour interpréter" → Tutoiement

**Localisation** : Thème natal → Cards Big 3

**Actuel** : "Touchez pour interpréter"  
**Suggéré** : "Touche pour découvrir" ou "Appuie pour en savoir plus"

---

### 10. Accessibilité des couleurs

**Suggestion** : Vérifier les contrastes WCAG AA pour les textes gris clair sur fond violet foncé.

---

## Analyse détaillée par écran

### Lot 1 : Captures 1-20

| # | Écran | Note | Points positifs | Points négatifs |
|---|-------|------|-----------------|-----------------|
| 1 | Welcome | 10/10 | Design impactant, CTA clair | — |
| 2 | Profil - date | 7/10 | Picker intuitif | "Calcul API..." visible |
| 3 | Profil - complet | 10/10 | Tous les champs, info fuseau | — |
| 4 | Thème natal preview | 10/10 | Big 3 cohérent | — |
| 5 | Thème natal complet | 10/10 | Ascendant Vierge visible | — |
| 6 | Disclaimer | 10/10 | Message parfait, cœur vert | — |
| 7 | Tuto - Rituel | 10/10 | Dynamique, exemple concret | — |
| 8 | Tuto - Saisons | 10/10 | Boule de cristal, mois affiché | — |
| 9 | Tuto - VoC | 10/10 | Explication claire, statut actuel | — |
| 10 | Tuto - Journal | 10/10 | Mockup de lignes | — |
| 11 | Home | 9/10 | Dates cohérentes, thèmes du mois | — |
| 12 | Home scrollé | 7/10 | Cards bien structurées | Loader flottant |
| 13 | Rapport haut | 10/10 | Dates alignées, maison affichée | — |
| 14 | Rapport milieu | 9/10 | Sections claires | Icônes warning uniformes |
| 15 | Aspects liste | 9/10 | Orbes affichés | Idem |
| 16 | Aspect détail 1 | 10/10 | Données factuelles complètes | — |
| 17 | Aspect détail 2 | 10/10 | Conseil + bloc Attention | — |
| 18 | Bottom sheet haut | 10/10 | Guidance, jauges, mansion | — |
| 19 | Bottom sheet bas | 7/10 | Rituels cochables | Vouvoiement, transits vides |
| 20 | Journal | 8/10 | Empty state sympathique | Vouvoiement placeholder |

### Lot 2 : Captures 21-34

| # | Écran | Note | Points positifs | Points négatifs |
|---|-------|------|-----------------|-----------------|
| 21 | Journal - Modal | 7/10 | Confirmation claire | Vouvoiement |
| 22 | Profil haut | 10/10 | Avatar signe, Big 3, planètes | — |
| 23 | Profil bas | 7/10 | Infos naissance, notifications | Version v2.0, espacement |
| 24 | Thème natal roue | 10/10 | Magnifique, axes visibles | — |
| 25 | Positions planétaires | 10/10 | Complet jusqu'à Neptune | — |
| 26 | Maisons | 10/10 | 12 maisons avec degrés | — |
| 27 | Aspects nataux | 8/10 | Orbes + classification | Warning uniforme |
| 28 | Aspect détail haut | 10/10 | Structure excellente | — |
| 29 | Aspect détail bas | 10/10 | Conseil pratique + Attention | — |
| 30 | Calendrier | 9/10 | 4 phases, jour encadré | — |
| 31 | Calendrier scrollé | 10/10 | CTA rapport visible | — |
| 32 | Révolution données | 8/10 | Date précise, position lune | Termes anglais |
| 33 | Révolution interprétation | 6/10 | Contenu riche | Vouvoiement complet |
| 34 | Loading | 10/10 | Animation charmante, transparence IA | — |

---

## Checklist pré-bêta

### Corrections critiques (à faire avant envoi)

- [ ] Passer tous les textes au tutoiement (Journal, Bottom sheet rituels, Révolution lunaire)
- [ ] Mettre à jour la version affichée : v2.0 → v3.0
- [ ] Remplacer "Calcul API..." par un loader ou "—"

### Corrections importantes (fortement recommandées)

- [ ] Traduire "conjunction/square" → "conjonction/carré" dans la révolution lunaire
- [ ] Corriger l'espacement "Lieu de naissance:" dans le profil
- [ ] Investiguer et corriger le loader flottant sur Home

### Améliorations optionnelles (polish)

- [ ] Différencier visuellement aspects harmoniques vs tendus
- [ ] Clarifier la section "Transits du jour" vs "Aspects du cycle"
- [ ] Passer "Touchez pour interpréter" au tutoiement
- [ ] Vérifier les contrastes WCAG AA

---

## Fichiers probablement concernés

```
apps/mobile/
├── constants/app.ts                    # Version
├── app/journal/index.tsx               # Vouvoiement modal/placeholder
├── components/TodayBottomSheet.tsx     # Vouvoiement rituels
├── app/onboarding/profile-setup.tsx    # "Calcul API..."
├── app/(tabs)/profile.tsx              # Espacement lieu
├── locales/fr.json                     # Si i18n utilisé

apps/api/
├── prompts/lunar_return_interpretation.txt  # Vouvoiement interprétation
├── services/ai_interpretation.py            # Templates
├── utils/aspect_names.py                    # Traduction aspects
```

---

## Conclusion

Lunation v3.0 est une app de qualité avec une identité visuelle forte et un contenu riche. Les problèmes identifiés sont principalement des incohérences de ton (tutoiement/vouvoiement) et quelques détails de polish.

**Estimation des corrections** :
- Critiques : 1-2h
- Importantes : 1h
- Total : 2-3h de travail

L'app peut partir en bêta-test avec les corrections critiques uniquement. Les bêta-testeurs pourront confirmer les problèmes d'UX plus subtils.
