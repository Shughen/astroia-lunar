# Lunation - Application Mobile

**Version:** 3.0
**Framework:** Expo SDK 54 + React Native 0.81 + Expo Router v6
**Etat:** En developpement actif

---

## Vision Produit

**Lunation** est une application d'astrologie lunaire personnalisee avec 2 axes principaux :

1. **Revolution Lunaire Mensuelle** - Chaque mois, un nouveau cycle lunaire demarre au moment ou la Lune revient a sa position natale. C'est le coeur de l'app.

2. **Rituel Quotidien** - Guidance quotidienne basee sur la phase lunaire, le signe traverse, et les aspects du jour.

**Fonctionnalite secondaire :**
- **Theme Natal** - Le ciel de naissance de l'utilisateur, base de tous les calculs personnalises.

---

## Architecture v3.0 (Refonte 29/01/2026)

### Navigation (3 Tabs + Stack)

```
App
├── (tabs)/                    # Tab Navigator (3 onglets)
│   ├── home.tsx               # "Mon Cycle" - Dashboard principal
│   ├── calendar.tsx           # "Calendrier" - Phases + VoC windows
│   └── profile.tsx            # "Profil" - Theme natal + parametres
│
├── lunar/                     # Stack screens lunaires
│   ├── index.tsx              # Hub Luna Pack
│   ├── report.tsx             # Rapport mensuel detaille
│   └── voc.tsx                # Void of Course
│
├── natal-chart/               # Theme natal
│   ├── index.tsx              # Formulaire de calcul
│   └── result.tsx             # Resultat du theme
│
├── transits/                  # Transits planetaires
│   ├── overview.tsx           # Vue d'ensemble
│   └── details.tsx            # Detail d'un aspect
│
├── lunar-returns/
│   └── timeline.tsx           # Timeline des 12 revolutions
│
├── onboarding/                # Parcours d'inscription
│   ├── index.tsx              # Bienvenue
│   ├── consent.tsx            # Consentement
│   ├── disclaimer.tsx         # Avertissement
│   ├── profile-setup.tsx      # Saisie date/heure/lieu
│   └── chart-preview.tsx      # Preview du theme
│
├── journal.tsx                # Journal intime lunaire
├── settings.tsx               # Parametres
├── auth.tsx                   # Authentification
└── welcome.tsx                # Ecran de bienvenue
```

### Home Screen "Mon Cycle" (Architecture Hero + Bottom Sheet)

```
Home Screen
├── Header
│   └── "Lunation - Ton rituel lunaire"
│
├── VocBanner (conditionnel)
│   └── Banniere amber si Void of Course actif
│
├── HeroLunarCard (60% ecran)
│   └── Revolution lunaire du mois
│   └── Lune en [signe] + Ascendant lunaire
│   └── Themes du mois (3 KeywordChips)
│   └── CTA gradient → /lunar/report
│
├── TodayMiniCard
│   └── Phase lunaire + signe du jour
│   └── Tap → ouvre TodayBottomSheet
│
├── NatalMiniCard
│   └── "Mon thème natal"
│   └── Tap → tab Profil
│
└── TodayBottomSheet (Modal slide-up)
    ├── Header: date + phase + signe
    ├── VoC Alert detaillee (si actif)
    ├── Guidance du jour + mots-cles
    ├── Jauges energie (Creative + Intuition)
    ├── Mansion lunaire du jour
    ├── Rituels suggeres (3 checkboxes)
    └── CTA Journal → JournalEntryModal
```

### Profil Screen (Theme Natal integre)

```
Profile Screen
├── Avatar + Nom utilisateur
│
├── Section "Mon Theme Natal"
│   ├── Big 3 (Soleil, Lune, Ascendant)
│   ├── Grille 4 planetes (Mercure, Venus, Mars, Jupiter)
│   └── CTA "Voir thème complet" → /natal-chart
│
└── Settings
    ├── Notifications
    ├── Langue
    └── Deconnexion
```

### Calendrier Screen (VoC Windows)

```
Calendar Screen
├── Calendrier mensuel
│   └── Phases lunaires par jour
│
└── Section "Fenetres VoC cette semaine"
    └── Liste des periodes VoC (date + heures)
```

---

## Composants Crees (Session 29/01/2026)

| Composant | Fichier | Role |
|-----------|---------|------|
| `VocBanner` | `components/VocBanner.tsx` | Banniere amber Void of Course |
| `HeroLunarCard` | `components/HeroLunarCard.tsx` | Hero card 60% ecran revolution lunaire |
| `TodayMiniCard` | `components/TodayMiniCard.tsx` | Mini card pour ouvrir bottom sheet |
| `NatalMiniCard` | `components/NatalMiniCard.tsx` | Raccourci vers thème natal |
| `TodayBottomSheet` | `components/TodayBottomSheet.tsx` | Modal slide-up rituel quotidien |
| `RitualCheckItem` | `components/RitualCheckItem.tsx` | Checkbox animee pour rituels |

---

## Changements Techniques v3.0

### Packages supprimes
- `@gorhom/bottom-sheet` - Conflit version avec worklets
- `react-native-reanimated` - Causait erreur Babel
- `react-native-worklets-core` - Module introuvable

### Solution adoptee
Le `TodayBottomSheet` utilise les composants natifs React Native :
- `Modal` avec `transparent` et `animationType="none"`
- `Animated.Value` + `Animated.spring` pour l'animation slide-up
- `TouchableWithoutFeedback` pour fermer au tap overlay
- `forwardRef` + `useImperativeHandle` pour exposer `snapToIndex()` et `close()`

### Theme.ts - Couleurs VoC ajoutees
```typescript
vocWarning: '#f59e0b',
vocBg: 'rgba(245, 158, 11, 0.2)',
vocBorder: 'rgba(245, 158, 11, 0.4)',
```

---

## Stack Technique

### Frontend
- **Expo SDK 54** + React Native 0.81
- **Expo Router v6** (file-based routing)
- **Zustand** (state management)
- **SWR** (data fetching + cache)
- **react-native-svg** (icones)
- **expo-linear-gradient** (backgrounds)
- **i18next** (FR/EN)

### Backend (apps/api)
- **FastAPI** + PostgreSQL (Supabase)
- **Claude Opus 4.5** pour interpretations IA
- **RapidAPI** pour calculs astrologiques

---

## Donnees Disponibles

### Revolution Lunaire (LunarReturn)
```typescript
{
  return_date: string;      // Date de la revolution
  moon_sign: string;        // Signe de la Lune (ex: "Taurus")
  lunar_ascendant: string;  // Ascendant lunaire
  interpretation?: string;  // Interpretation IA du mois
}
```

### Climat Lunaire Quotidien (LunarContext)
```typescript
{
  moon: {
    phase: string;          // "waxing_gibbous", "full_moon", etc.
    sign: string;           // Signe actuel de la Lune
    lunar_day?: number;     // Jour du cycle (1-29)
  };
  voc?: {
    active: boolean;
    end_time?: string;
  };
}
```

### Theme Natal (NatalChart)
```typescript
{
  sun_sign: string;
  moon_sign: string;
  ascendant: string;
  planets: Planet[];
  houses: House[];
  aspects: Aspect[];
}
```

---

## Commandes

```bash
# Installation
cd apps/mobile
npm install

# Lancement
npm start                  # Expo dev server
npm start --clear          # Avec cache clear
npx tsc --noEmit           # Check TypeScript

# Backend requis
cd ../api
uvicorn main:app --reload --port 8000
```

---

## Fichiers Supprimes (v3.0)

- `app/(tabs)/horoscope.tsx` - Fusionne dans TodayBottomSheet
- `app/(tabs)/rituals.tsx` - Fusionne dans TodayBottomSheet

---

## Documentation Supplementaire

- `docs/SCREENS.md` - Documentation detaillee des ecrans
- `docs/SCREENSHOTS_WORKFLOW.md` - **Guide capture et validation screenshots** 📸
- `maestro/README.md` - Tests E2E avec Maestro
- `../api/docs/ARCHITECTURE.md` - Architecture complete
- `../.claude/CLAUDE.md` - Instructions projet

---

## Capture de Screenshots pour Publication

Un workflow automatise permet de capturer et valider tous les ecrans pour publication sur Google Play Store.

### Quick Start

```bash
# Workflow complet (capture + organisation + validation IA)
npm run screenshots:full

# Etapes separees
npm run screenshots:capture     # Capture Maestro uniquement
npm run screenshots:organize    # Organisation et renommage
npm run screenshots:validate    # Validation avec Claude Opus 4.5
```

### Caracteristiques

- ✅ **22+ ecrans captures** automatiquement (auth, onboarding, tabs, stacks, modals)
- ✅ **Navigation intelligente** avec Maestro (skip sections deja completes)
- ✅ **Organisation automatique** avec convention de nommage (`01-auth.png`, `12-home.png`, etc.)
- ✅ **Validation IA** avec Claude Opus 4.5 (contenu, lisibilite, coherence design, accessibilite)
- ✅ **Rapport detaille** avec feedback et suggestions d'amelioration
- ⚡ **~10-15 minutes** par session complete
- 💰 **~$1.50** par validation complete (Claude Opus 4.5)

### Documentation Complete

Voir `docs/SCREENSHOTS_WORKFLOW.md` pour :
- Prerequis (backend, emulateur, Maestro)
- Guide d'installation
- Architecture des scripts
- Criteres de validation IA
- Troubleshooting
- FAQ

---

**Derniere mise a jour:** 2026-01-30 (Ajout workflow screenshots)
