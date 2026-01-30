# Lunation Mobile - Documentation des Ecrans

**Version:** 3.3 (Journal simplifie 29/01/2026)

## Architecture de Navigation

```
app/
├── index.tsx                 # Routing guards (auth, onboarding)
├── _layout.tsx               # Root Stack Navigator
├── (tabs)/                   # Tab Navigator (3 onglets)
│   ├── _layout.tsx           # Configuration tabs
│   ├── home.tsx              # "Mon Cycle" - Dashboard principal
│   ├── calendar.tsx          # "Calendrier" - Phases + VoC windows
│   └── profile.tsx           # "Profil" - Theme natal + parametres
├── auth.tsx                  # Authentification (modal)
├── welcome.tsx               # Ecran bienvenue (modal)
├── onboarding/               # Flow onboarding (modal)
├── lunar/                    # Details lunaires (stack)
├── natal-chart/              # Theme natal (stack)
└── transits/                 # Transits (stack)
```

---

## Tab Navigator

**Fichier** : `app/(tabs)/_layout.tsx`

### Configuration
- 3 onglets avec icones SVG custom
- Style : fond `#1a0b2e`, accent or `#ffd700` pour onglet actif
- Hauteur : 70px + safe area iOS

### Onglets
| Onglet | Route | Icone | Description |
|--------|-------|-------|-------------|
| Mon Cycle | `/home` | Lune croissante | Dashboard principal + bottom sheet |
| Calendrier | `/calendar` | Calendrier + point lune | Vue mensuelle + VoC windows |
| Profil | `/profile` | Silhouette | Theme natal + parametres |

---

## Ecrans Tabs

### 1. Home "Mon Cycle" (`home.tsx`)

**Role** : Dashboard principal avec Hero lunar et bottom sheet rituel quotidien

**Architecture UI** :
```
┌─────────────────────────────────────┐
│           Lunation                  │
│       Ton rituel lunaire            │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │      VocBanner (si actif)       │ │
│ │   ⚠️ Void of Course jusqu'a...  │ │
│ └─────────────────────────────────┘ │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │                                 │ │
│ │       HeroLunarCard             │ │
│ │       (60% ecran)               │ │
│ │                                 │ │
│ │   Revolution Lunaire Janvier    │ │
│ │   Lune en Taurus ☽              │ │
│ │   Ascendant: Cancer             │ │
│ │                                 │ │
│ │   [Stabilite] [Ancrage] [...]   │ │
│ │                                 │
│ │   [   Voir mon mois   ] ────────┼──► /lunar/report
│ └─────────────────────────────────┘ │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ TodayMiniCard          ▲        │ │
│ │ Lune Gibbeuse en Gemeaux        │──► TodayBottomSheet
│ └─────────────────────────────────┘ │
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ NatalMiniCard          ▶        │ │
│ │ Mon thème natal                 │──► tab Profil
│ └─────────────────────────────────┘ │
└─────────────────────────────────────┘
```

**Composants utilises** :
- `VocBanner` - Banniere amber Void of Course (conditionnelle)
- `HeroLunarCard` - Hero card 60% ecran revolution lunaire
- `TodayMiniCard` - Mini card phase du jour → ouvre bottom sheet
- `NatalMiniCard` - Raccourci vers thème natal
- `TodayBottomSheet` - Modal slide-up avec rituel complet

**Donnees** :
- `useCurrentLunarReturn()` - SWR hook pour revolution lunaire
- `useLunar()` - Context pour donnees lunaires temps reel
- `useVocStatus()` - SWR hook pour statut Void of Course (cache 5min)
- `useMansionToday()` - SWR hook pour mansion lunaire du jour (cache 10min)

**Features** :
- Pull-to-refresh
- Detection mode hors ligne (banner)
- Bottom sheet modal avec animation spring

---

### 2. TodayBottomSheet (`components/TodayBottomSheet.tsx`)

**Role** : Modal slide-up contenant le rituel quotidien complet

**Architecture UI** :
```
┌─────────────────────────────────────┐
│              ━━━━━                  │  ← Handle
│                                     │
│  🌔  Mercredi 29 janvier            │
│      Lune Gibbeuse en Gemeaux       │  [Badge]
│                                     │
│ ┌─────────────────────────────────┐ │
│ │ ⚠️ Void of Course               │ │  ← Si actif
│ │    Jusqu'a 14:30                │ │
│ └─────────────────────────────────┘ │
│                                     │
│  GUIDANCE DU JOUR                   │
│  "Periode de perfectionnement..."   │
│  [Patience] [Detail] [Focus]        │
│                                     │
│  ENERGIES DU JOUR                   │
│  ┌───────────────┐ ┌───────────────┐│
│  │Energie Creative│ │  Intuition   ││
│  │    ████░░ 72%  │ │  █████░ 85%  ││
│  └───────────────┘ └───────────────┘│
│                                     │
│  MANSION LUNAIRE                    │
│  ┌─────────────────────────────────┐│
│  │ #3  Al-Thurayya                 ││
│  │     Chance et fortune           ││
│  └─────────────────────────────────┘│
│                                     │
│  RITUELS SUGGERES                   │
│  ☑️ Perfectionnement - Affinez...   │
│  ☐ Gratitude anticipee - Remerciez..│
│  ☐ Preparation - Preparez...        │
│                                     │
│  [      Mon journal      ]          │  → /journal (ecriture + historique)
│  [ Voir le rapport de janvier → ]   │  → /lunar/report
│                                     │
└─────────────────────────────────────┘
```

**Implementation technique** :
```typescript
// Modal native React Native (pas @gorhom/bottom-sheet)
<Modal visible={visible} transparent animationType="none">
  <TouchableWithoutFeedback onPress={handleClose}>
    <View style={styles.overlay}>
      <Animated.View style={[styles.sheet, { transform: [{ translateY: slideAnim }] }]}>
        {/* Content */}
      </Animated.View>
    </View>
  </TouchableWithoutFeedback>
</Modal>

// Expose methods via forwardRef
useImperativeHandle(ref, () => ({
  snapToIndex: (index) => { /* Animated.spring */ },
  close: () => { /* Animated.timing */ },
}));
```

**Composants utilises** :
- `MoonPhaseIcon` - Icone phase lunaire
- `ZodiacBadge` - Badge signe zodiacal
- `ProgressBar` - Jauge energie animee
- `KeywordChip` - Badge mot-cle
- `RitualCheckItem` - Checkbox rituel animee

**Donnees calculees** :
| Donnee | Source |
|--------|--------|
| Phase francais | `getMoonPhaseFrench(phase)` |
| Signe francais | `getZodiacSignFrench(sign)` |
| Guidance + Mots-cles | `LUNAR_GUIDANCE[phase]` (depuis `constants/lunarGuidance.ts`) |
| Rituels | `PHASE_RITUALS[phase]` (inline dans composant) |
| Energies | `getHoroscopeMetrics(sign, phase, aspects)` |
| Mansion | `useMansionToday()` API avec fallback hardcode |

**Navigation** :
| Bouton | Destination | Description |
|--------|-------------|-------------|
| Mon journal | `/journal` | Ecran journal complet (ecriture + historique) |
| Voir le rapport | `/lunar/report` | Rapport lunaire mensuel |

---

### 3. Calendar (`calendar.tsx`)

**Role** : Vue mensuelle avec phases lunaires et fenetres VoC

**Structure UI** :
```
┌─────────────────────────────────────┐
│       ◀  Janvier 2026  ▶            │
│                                     │
│  L   M   M   J   V   S   D          │
│  🌒  🌒  🌓  🌓  🌔  🌔  🌕          │
│  6   7   8   9   10  11  12         │
│  ...                                │
│                                     │
│  LEGENDE                            │
│  🌑 Nouvelle  🌓 1er Quartier       │
│  🌕 Pleine    🌗 Dernier Quartier   │
│                                     │
│  FENETRES VOC CETTE SEMAINE         │
│  ┌─────────────────────────────────┐│
│  │ 📅 Mer 29 Jan  14:30 - 18:45   ││
│  │ 📅 Ven 31 Jan  09:15 - 11:30   ││
│  │ 📅 Dim 2 Fev   22:00 - 02:15   ││
│  └─────────────────────────────────┘│
└─────────────────────────────────────┘
```

**Composants** :
- Navigation mois (precedent/suivant)
- Grille 7x6 jours avec phases
- Legende phases principales
- Section VoC windows (nouveau v3.0)

**Hooks** :
- `useVocWindows()` - Recupere les fenetres VoC via `/api/lunar/voc/status`
  - Parse `data.upcoming` pour les fenetres a venir
  - Fallback sur `data.next` si `upcoming` vide

**Calculs locaux** :
- `getMoonPhase(date)` - Calcule la phase lunaire pour chaque jour
  - Base : cycle synodique de 29.53 jours
  - Reference : nouvelle lune du 6 janvier 2000

---

### 4. Profile (`profile.tsx`)

**Role** : Theme natal integre + parametres utilisateur

**Structure UI** :
```
┌─────────────────────────────────────┐
│           Mon Profil                │
│                                     │
│         [ZodiacBadge]               │
│         Prenom Nom                  │
│         email@example.com           │
│                                     │
│  MON THEME NATAL                    │
│  ┌─────────────────────────────────┐│
│  │  BIG 3                          ││
│  │  ☉ Soleil: Lion                 ││
│  │  ☽ Lune: Scorpion               ││
│  │  ↑ Ascendant: Verseau           ││
│  └─────────────────────────────────┘│
│                                     │
│  ┌────────┐ ┌────────┐ ┌────────┐  │
│  │Mercure │ │ Venus  │ │ Mars   │  │
│  │Vierge  │ │Balance │ │Belier  │  │
│  └────────┘ └────────┘ └────────┘  │
│  ┌────────┐                        │
│  │Jupiter │                        │
│  │Sagitt. │                        │
│  └────────┘                        │
│                                     │
│  [   Voir thème complet   ] ────────┼──► /natal-chart
│                                     │
│  PARAMETRES                         │
│  ┌─────────────────────────────────┐│
│  │ 🔔 Notifications        [ON]   ││
│  │ 🌐 Langue               FR     ││
│  └─────────────────────────────────┘│
│                                     │
│  [   Se deconnecter   ]             │
└─────────────────────────────────────┘
```

**Sections** :
1. **Carte profil** - Avatar (ZodiacBadge), nom, email
2. **Mon Theme Natal** (nouveau v3.0)
   - Big 3 : Soleil, Lune, Ascendant
   - Grille 4 planetes : Mercure, Venus, Mars, Jupiter
   - CTA vers thème complet
3. **Parametres** - Notifications, langue
4. **Actions** - Deconnexion

**Donnees** :
- `useAuthStore()` - Utilisateur authentifie
- `useNatalChart()` - Theme natal complet
- `useNotificationsStore()` - Preferences notifications

---

## Composants Nouveaux (v3.0)

### VocBanner (`components/VocBanner.tsx`)
```tsx
<VocBanner vocStatus={{
  now: { is_active: true, end_at: '2026-01-29T14:30:00' }
}} />
```
- Banniere amber avec icone alerte
- Affiche heure de fin du VoC
- Conditionnel : ne s'affiche que si VoC actif

### HeroLunarCard (`components/HeroLunarCard.tsx`)
```tsx
<HeroLunarCard
  lunarReturn={currentLunarReturn}
  loading={false}
/>
```
- Occupe 60% de l'ecran
- Elements decoratifs (blur circles)
- Themes du mois (3 KeywordChips)
- CTA gradient vers `/lunar/report`

### TodayMiniCard (`components/TodayMiniCard.tsx`)
```tsx
<TodayMiniCard
  moonPhase="waxing_gibbous"
  moonSign="Gemini"
  onPress={() => bottomSheetRef.current?.snapToIndex(1)}
/>
```
- Card horizontale compacte
- Phase + signe du jour
- Chevron up indiquant le bottom sheet

### NatalMiniCard (`components/NatalMiniCard.tsx`)
```tsx
<NatalMiniCard onPress={() => router.push('/(tabs)/profile')} />
```
- Raccourci vers thème natal
- Icone roue astrologique
- Chevron right

### RitualCheckItem (`components/RitualCheckItem.tsx`)
```tsx
<RitualCheckItem
  title="Meditation d'intention"
  description="Visualisez vos objectifs"
  checked={isCompleted}
  onToggle={() => toggleRitual(title)}
/>
```
- Checkbox avec animation scale
- Haptic feedback
- State local (non persiste)

---

## Composants Conserves

### ProgressBar (`components/ProgressBar.tsx`)
```tsx
<ProgressBar
  label="Energie Creative"
  value={86}
  color={colors.gold}
/>
```

### KeywordChip (`components/KeywordChip.tsx`)
```tsx
<KeywordChip label="Action" variant="gold" />
// variants: 'default' | 'accent' | 'gold'
```

### MoonPhaseIcon (`components/icons/MoonPhaseIcon.tsx`)
```tsx
<MoonPhaseIcon phase="full_moon" size={36} />
```

### ZodiacBadge (`components/icons/ZodiacIcon.tsx`)
```tsx
<ZodiacBadge sign="Taurus" size={40} />
```

---

## Fichiers Supprimes (v3.0)

| Fichier | Raison |
|---------|--------|
| `app/(tabs)/horoscope.tsx` | Fusionne dans TodayBottomSheet |
| `app/(tabs)/rituals.tsx` | Fusionne dans TodayBottomSheet |

Le contenu de ces ecrans est maintenant accessible via le bottom sheet sur Home.

---

## Flux de Navigation

```
App Start
    │
    ▼
index.tsx (Guards)
    │
    ├─ Non authentifie → /auth
    ├─ Welcome non vu → /welcome
    ├─ Consent non accepte → /onboarding/consent
    ├─ Profil incomplet → /onboarding/profile-setup
    ├─ Disclaimer non vu → /onboarding/disclaimer
    ├─ Onboarding non fini → /onboarding
    │
    ▼
/(tabs)/home ◄────────────────────┐
    │                             │
    ├─ TodayMiniCard → Bottom Sheet (modal)
    ├─ NatalMiniCard → Tab Profil ┤
    ├─ HeroLunarCard → /lunar/report
    │                             │
    ├─ Tab Calendrier ────────────┤
    └─ Tab Profil ────────────────┘
         │
         ├─ Theme natal → /natal-chart
         ├─ Deconnexion → /welcome
         └─ Reset donnees → /welcome
```

---

## Hooks SWR (`hooks/useLunarData.ts`)

| Hook | Endpoint | Cache | Description |
|------|----------|-------|-------------|
| `useCurrentLunarReturn()` | `/api/lunar-returns/current` | On mount | Revolution lunaire en cours |
| `useVocStatus()` | `/api/lunar/voc/status` | 5 min | Statut Void of Course + upcoming windows |
| `useMansionToday()` | `/api/lunar/mansion/today` | 10 min | Mansion lunaire du jour |
| `useMajorTransits()` | `/api/transits/overview` | On mount | Transits majeurs du mois |

**Types exportes** :
- `VocStatus` - Statut VoC avec now/next/upcoming
- `MansionTodayResponse` - Reponse API mansion avec fallback
- `MansionData` - Donnees mansion (number, name, interpretation)

---

## Points d'Attention

1. **Bottom Sheet natif** : Utilise Modal + Animated (pas @gorhom/bottom-sheet)
2. **Donnees hors ligne** : Home detecte le reseau et affiche un banner
3. **Cache SWR** : Les hooks utilisent SWR avec deduplication 60s
4. **Haptics** : Feedback tactile sur toutes les interactions
5. **Safe Area** : Tab bar ajustee pour iOS (24px bottom padding)
6. **VoC conditionnel** : Banner et section ne s'affichent que si API disponible
7. **Mansion fallback** : Si API non dispo, utilise donnees hardcodees basees sur le jour du mois

---

*Derniere mise a jour : 29 janvier 2026 (Journal simplifie v3.3)*
