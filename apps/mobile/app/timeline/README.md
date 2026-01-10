# Timeline Lunaire

Vision continue du temps lunaire pour Lunation.

## Objectif

Donner une vision continue du temps lunaire en reliant :
- **Passé** : journal écrit
- **Présent** : rituel quotidien
- **Futur** : climat lunaire à venir

Créer un attachement long terme sans gamification (pas de streaks, pas de score).

## Fonctionnalités V1

### Liste scrollable de jours
- **±14 jours** autour d'aujourd'hui (configurable)
- Scroll initial centré sur aujourd'hui
- FlatList optimisée avec `getItemLayout` pour performances

### Affichage par jour
Chaque carte affiche :
- **Date relative** : Aujourd'hui / Hier / Demain / Il y a X jours / Dans X jours
- **Date courte** : 31 déc.
- **Phase lunaire** : Emoji + nom traduit
- **Signe lunaire** : Aquarius, Taurus, etc.
- **Badge VoC** : Si Void of Course actif (V1 = désactivé)
- **Indicateur journal** : ✓ si écrit, ○ si vide (passé/aujourd'hui uniquement)

### Interactions

**Tap sur un jour passé ou aujourd'hui :**
- Ouvre `JournalEntryModal`
- Si entrée existe → lecture + modification
- Sinon → écriture nouvelle entrée

**Tap sur un jour futur :**
- Lecture seule (V1)
- TODO : ouvrir écran climat ou message "À venir"

### États

- **Loading** : ActivityIndicator + message traduit
- **Empty** : Message si aucune donnée disponible
- **Offline** : Calcul local automatique (fallback sur API)

## Architecture

### Types
`/types/timeline.ts` :
```typescript
interface TimelineDay {
  date: string; // YYYY-MM-DD
  type: 'past' | 'today' | 'future';
  moon: { phase: MoonPhase; sign: string };
  hasVoc: boolean;
  hasJournalEntry: boolean;
  relativeLabel?: string;
}
```

### Service
`/services/timelineService.ts` :
- `generateTimeline()` : Génère ±14 jours avec contexte lunaire
- `refreshTimelineJournalIndicators()` : Rafraîchit les indicateurs après save/delete
- Optimisation : API uniquement pour aujourd'hui, calcul local pour le reste

### Composants
- `TimelineDayCard` : Carte individuelle pour un jour
- `JournalEntryModal` : Modal existant (réutilisé)

### Écran
`/app/timeline.tsx` :
- FlatList avec optimisations :
  - `keyExtractor` stable
  - `getItemLayout` pour scroll performant
  - `removeClippedSubviews={true}`
  - `windowSize={11}`
- Gestion états : loading, error, empty
- Rafraîchissement indicateurs sans reload complet

## i18n

Clés ajoutées dans `/i18n/fr.json` et `/i18n/en.json` :
```json
{
  "timeline": {
    "title": "Timeline Lunaire",
    "subtitle": "Vision continue du temps lunaire",
    "today": "Aujourd'hui",
    "yesterday": "Hier",
    "tomorrow": "Demain",
    "daysAgo": "Il y a {{count}} jours",
    "inDays": "Dans {{count}} jours",
    "vocBadge": "VoC",
    "hasJournal": "Entrée écrite",
    "noJournal": "Aucune note",
    "loadingTimeline": "Chargement de la timeline...",
    "emptyState": { ... },
    "offline": { ... }
  }
}
```

## Contraintes respectées

✅ **0 nouvelle dépendance**
- Réutilise `expo-router`, `react-i18next`, `@react-native-async-storage/async-storage`

✅ **Lune : API si dispo, sinon fallback local**
- `getMoonDataForDate()` : API pour aujourd'hui, calcul local pour le reste
- Pas de nouvelle lib astro/ephemeris

✅ **Futur = lecture seule**
- Pas d'écriture journal sur dates futures
- Tap ouvre rien pour V1 (TODO: écran climat)

✅ **Performance : FlatList optimisée**
- `keyExtractor` stable
- `getItemLayout` pour scroll constant
- `removeClippedSubviews`, `windowSize`, `maxToRenderPerBatch`

## Tests

- TypeScript : ✅ `npm run typecheck` (0 erreur)
- Jest : ✅ Tous les tests passent (78/78)

## Navigation

Pour accéder à la Timeline depuis l'app :
```tsx
import { useRouter } from 'expo-router';

const router = useRouter();
router.push('/timeline');
```

## Améliorations futures (hors V1)

- [ ] Intégrer VoC réel via API
- [ ] Tap sur futur → ouvrir écran climat
- [ ] Pull to refresh
- [ ] Cache AsyncStorage pour offline complet
- [ ] Animations scroll (highlight aujourd'hui)
- [ ] Filtres (jours avec journal uniquement)
