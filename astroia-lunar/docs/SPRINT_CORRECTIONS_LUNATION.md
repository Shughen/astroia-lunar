# SPRINT CORRECTIONS CRITIQUES — Lunation v3.0

**Date** : 29 janvier 2026  
**Objectif** : Corrections pré-publication Google Play Store  
**Estimation totale** : 9h  

---

## Vue d'ensemble

| Ticket | Titre | Priorité | Estimation |
|--------|-------|----------|------------|
| T1 | Harmoniser les dates du cycle lunaire | P0 | 2h |
| T2 | Corriger les doublons de phases lunaires | P0 | 1h |
| T3 | Corriger les fautes d'orthographe | P0 | 30min |
| T4 | Dédupliquer l'autocomplétion de lieu | P1 | 1.5h |
| T5 | Ajouter les indicateurs de phase sur le calendrier | P1 | 2h |
| T6 | Implémenter la section VoC dans le calendrier | P1 | 2h |

---

## T1 — Harmoniser les dates du cycle lunaire

### Priorité : P0 — BLOQUANT

### Problème

La révolution lunaire de janvier 2026 affiche 3 plages de dates différentes selon les écrans :
- Home (ancienne capture) : "6 janv. - 4 fév."
- Home (récente capture) : "21 janv. - 19 fév."
- Rapport mensuel : "Du 21 jan. au 17 fév."

La date de révolution lunaire est unique par utilisateur (retour de la Lune à sa position natale). Elle doit être cohérente partout.

### Fichiers concernés

```
apps/mobile/
├── app/(tabs)/home.tsx
├── components/HeroLunarCard.tsx
├── app/lunar/report.tsx
├── services/api.ts
├── stores/lunarStore.ts (si existant)
```

### Tâches

#### 1. Créer un hook centralisé pour les lunar returns

Créer `hooks/useLunarReturn.ts` :

```typescript
import useSWR from 'swr';
import { fetcher } from '@/services/api';

interface LunarReturn {
  id: string;
  return_date: string;
  end_date: string;
  moon_sign: string;
  lunar_ascendant: string;
  month_name: string;
  interpretation?: string;
  themes?: string[];
}

export function useLunarReturn() {
  const { data, error, isLoading } = useSWR<LunarReturn>(
    '/api/lunar/returns/current',
    fetcher,
    {
      revalidateOnFocus: false,
      dedupingInterval: 60000,
    }
  );

  return {
    lunarReturn: data,
    isLoading,
    isError: error,
    dateRange: data ? formatDateRange(data.return_date, data.end_date) : null,
    dateRangeLong: data ? formatDateRangeLong(data.return_date, data.end_date) : null,
  };
}

function formatDateRange(start: string, end: string): string {
  const startDate = new Date(start);
  const endDate = new Date(end);
  
  const opts: Intl.DateTimeFormatOptions = { day: 'numeric', month: 'short' };
  const startStr = startDate.toLocaleDateString('fr-FR', opts).replace('.', '');
  const endStr = endDate.toLocaleDateString('fr-FR', opts).replace('.', '');
  
  return `${startStr} - ${endStr}`;
}

function formatDateRangeLong(start: string, end: string): string {
  const startDate = new Date(start);
  const endDate = new Date(end);
  
  const opts: Intl.DateTimeFormatOptions = { day: 'numeric', month: 'long' };
  const startStr = startDate.toLocaleDateString('fr-FR', opts);
  const endStr = endDate.toLocaleDateString('fr-FR', opts);
  
  return `Du ${startStr} au ${endStr}`;
}
```

#### 2. Modifier HeroLunarCard.tsx

Remplacer les appels API locaux par le hook :

```typescript
import { useLunarReturn } from '@/hooks/useLunarReturn';

export function HeroLunarCard() {
  const { lunarReturn, dateRange, isLoading } = useLunarReturn();
  
  if (isLoading) return <HeroLunarCardSkeleton />;
  
  return (
    <View style={styles.container}>
      <Text style={styles.monthName}>{lunarReturn?.month_name}</Text>
      <Text style={styles.dateRange}>{dateRange}</Text>
      {/* ... reste du composant */}
    </View>
  );
}
```

#### 3. Modifier report.tsx

Même pattern :

```typescript
import { useLunarReturn } from '@/hooks/useLunarReturn';

export default function LunarReport() {
  const { lunarReturn, dateRangeLong } = useLunarReturn();
  
  return (
    <ScrollView>
      <Text style={styles.title}>Rapport Mensuel</Text>
      <Text style={styles.subtitle}>{lunarReturn?.month_name}</Text>
      <Text style={styles.dates}>{dateRangeLong}</Text>
      {/* ... */}
    </ScrollView>
  );
}
```

### Critères d'acceptation

- [ ] Les dates sont identiques sur Home et Rapport mensuel
- [ ] Format court sur Home : "21 janv. - 19 fév."
- [ ] Format long dans le rapport : "Du 21 janvier au 19 février"
- [ ] Un seul appel API (vérifier Network tab)
- [ ] Pas de flash/rechargement lors de la navigation

---

## T2 — Corriger les doublons de phases lunaires

### Priorité : P0 — BLOQUANT

### Problème

La section "Phases principales ce mois" affiche "2 Jan - Pleine Lune" ET "3 Jan - Pleine Lune". Astronomiquement incorrect : une pleine lune est un instant précis.

### Fichiers concernés

```
apps/mobile/
├── app/(tabs)/calendar.tsx
├── components/PhasesList.tsx (si existant)
```

### Tâches

#### 1. Identifier la source du problème

```bash
# Rechercher le code de rendu des phases
grep -rn "Pleine Lune\|full_moon\|phases" apps/mobile/app/\(tabs\)/calendar.tsx
grep -rn "phases" apps/mobile/components/
```

#### 2. Implémenter la déduplication

Dans le composant qui affiche les phases (calendar.tsx ou PhasesList.tsx) :

```typescript
interface LunarPhase {
  date: string;
  phase: string;
  phase_name: string;
}

function deduplicatePhases(phases: LunarPhase[]): LunarPhase[] {
  const mainPhases = ['new_moon', 'first_quarter', 'full_moon', 'last_quarter'];
  const seen = new Set<string>();
  
  return phases
    .filter(p => mainPhases.includes(p.phase))
    .filter(p => {
      if (seen.has(p.phase)) return false;
      seen.add(p.phase);
      return true;
    })
    .sort((a, b) => new Date(a.date).getTime() - new Date(b.date).getTime());
}

// Utilisation dans le composant :
function MainPhasesSection({ phases }: { phases: LunarPhase[] }) {
  const uniquePhases = useMemo(() => deduplicatePhases(phases), [phases]);
  
  return (
    <View style={styles.phasesContainer}>
      <Text style={styles.phasesTitle}>Phases principales ce mois</Text>
      <View style={styles.phasesGrid}>
        {uniquePhases.map((phase) => (
          <PhaseItem 
            key={`${phase.phase}-${phase.date}`}
            date={phase.date}
            name={phase.phase_name}
          />
        ))}
      </View>
    </View>
  );
}
```

#### 3. Vérifier les clés de rendu

S'assurer que les clés React sont uniques et stables :

```typescript
// ❌ Mauvais
{phases.map((phase, index) => <PhaseItem key={index} ... />)}

// ✅ Bon
{phases.map((phase) => <PhaseItem key={`${phase.phase}-${phase.date}`} ... />)}
```

### Critères d'acceptation

- [ ] Une seule entrée par type de phase (1 pleine lune, 1 nouvelle lune, etc.)
- [ ] 4 phases affichées maximum par mois
- [ ] Ordre chronologique respecté
- [ ] Pas de warning React sur les clés

---

## T3 — Corriger les fautes d'orthographe

### Priorité : P0 — BLOQUANT (risque de rejet store)

### Problème

Fautes d'accent identifiées :
1. "J'accepte la politique de confidentialite" → "confidentialité"
2. "Mon theme natal" → "Mon thème natal"

### Fichiers concernés

```
apps/mobile/
├── app/onboarding/consent.tsx (ou step1.tsx)
├── components/NatalMiniCard.tsx
├── locales/fr.json (si i18n)
```

### Tâches

#### 1. Rechercher toutes les occurrences

```bash
cd apps/mobile

# Rechercher les fautes
grep -rn "confidentialite" app/ components/ locales/ 2>/dev/null
grep -rn "theme natal" app/ components/ locales/ 2>/dev/null
grep -rn '"theme"' locales/ 2>/dev/null

# Rechercher d'autres fautes potentielles
grep -rn "evenement" app/ components/ locales/ 2>/dev/null
grep -rn "securite[^é]" app/ components/ locales/ 2>/dev/null
grep -rn "generale[^é]" app/ components/ locales/ 2>/dev/null
```

#### 2. Corriger dans les fichiers i18n (si utilisé)

```json
// locales/fr.json

{
  "onboarding": {
    "consent": {
      "checkbox_label": "J'accepte la politique de confidentialité"
    }
  },
  "home": {
    "natal_card": {
      "title": "Mon thème natal",
      "subtitle": "Voir mon ciel de naissance"
    }
  },
  "profile": {
    "natal_section": {
      "title": "Mon Thème Natal"
    }
  }
}
```

#### 3. Corriger dans les composants (si texte en dur)

```typescript
// Dans le fichier concerné, remplacer :

// ❌ Avant
<Text>J'accepte la politique de confidentialite</Text>

// ✅ Après
<Text>J'accepte la politique de confidentialité</Text>
```

```typescript
// ❌ Avant
<Text>Mon theme natal</Text>

// ✅ Après
<Text>Mon thème natal</Text>
```

#### 4. Créer un script de vérification

Créer `scripts/check-french.sh` :

```bash
#!/bin/bash
echo "=== Vérification orthographe française ==="

ERRORS=0

check_pattern() {
  local pattern=$1
  local correct=$2
  local result=$(grep -rn "$pattern" apps/mobile/app apps/mobile/components apps/mobile/locales 2>/dev/null)
  if [ -n "$result" ]; then
    echo "❌ Trouvé '$pattern' (devrait être '$correct'):"
    echo "$result"
    ERRORS=$((ERRORS + 1))
  fi
}

check_pattern "confidentialite[^é]" "confidentialité"
check_pattern " theme[^è]" "thème"
check_pattern "evenement[^s]" "événement"
check_pattern "securite[^é]" "sécurité"
check_pattern "generale[^é]" "générale"
check_pattern "particuliere[^é]" "particulière"

if [ $ERRORS -eq 0 ]; then
  echo "✅ Aucune faute d'accent détectée"
else
  echo ""
  echo "⚠️  $ERRORS pattern(s) problématique(s) trouvé(s)"
  exit 1
fi
```

### Critères d'acceptation

- [ ] "confidentialité" avec accent partout
- [ ] "thème" avec accent partout
- [ ] Script de vérification passe sans erreur
- [ ] Aucune autre faute d'accent visible

---

## T4 — Dédupliquer l'autocomplétion de lieu

### Priorité : P1 — IMPORTANT

### Problème

La saisie "Paris, France" affiche 3 fois "Paris, Île-de-France, France" avec des descriptions identiques.

### Fichiers concernés

```
apps/mobile/
├── app/onboarding/profile-setup.tsx
├── components/LocationAutocomplete.tsx (si séparé)
├── services/geocoding.ts
```

### Tâches

#### 1. Identifier le composant d'autocomplétion

```bash
grep -rn "autocomplete\|location\|geocod" apps/mobile/app/onboarding/
grep -rn "TextInput" apps/mobile/app/onboarding/profile-setup.tsx
```

#### 2. Implémenter la déduplication

Créer ou modifier `services/geocoding.ts` :

```typescript
export interface GeocodingResult {
  place_id: string;
  display_name: string;
  lat: number;
  lon: number;
  type?: string;
}

export async function searchLocations(query: string): Promise<GeocodingResult[]> {
  if (query.length < 2) return [];
  
  const response = await fetch(
    `${GEOCODING_API_URL}?q=${encodeURIComponent(query)}&limit=10`
  );
  const results: GeocodingResult[] = await response.json();
  
  return deduplicateLocations(results);
}

function deduplicateLocations(results: GeocodingResult[]): GeocodingResult[] {
  const seen = new Map<string, GeocodingResult>();
  
  for (const result of results) {
    const key = normalizeLocationName(result.display_name);
    
    if (!seen.has(key)) {
      seen.set(key, result);
    } else if (result.type === 'city') {
      // Privilégier le type "city" sur les autres
      seen.set(key, result);
    }
  }
  
  return Array.from(seen.values()).slice(0, 5);
}

function normalizeLocationName(name: string): string {
  return name
    .toLowerCase()
    .normalize('NFD')
    .replace(/[\u0300-\u036f]/g, '')
    .split(',')
    .slice(0, 2)
    .join(',')
    .trim();
}
```

#### 3. Améliorer l'affichage des résultats

```typescript
// components/LocationAutocomplete.tsx

interface LocationItemProps {
  result: GeocodingResult;
  onSelect: (result: GeocodingResult) => void;
}

function LocationItem({ result, onSelect }: LocationItemProps) {
  const parts = result.display_name.split(',').map(p => p.trim());
  const primary = parts[0];
  const secondary = parts.slice(1, 3).join(', ');
  
  return (
    <TouchableOpacity 
      style={styles.locationItem}
      onPress={() => onSelect(result)}
    >
      <View style={styles.locationText}>
        <Text style={styles.locationPrimary}>{primary}</Text>
        <Text style={styles.locationSecondary}>{secondary}</Text>
      </View>
      <Ionicons name="chevron-forward" size={20} color="#666" />
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  locationItem: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingVertical: 12,
    paddingHorizontal: 16,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  locationText: {
    flex: 1,
  },
  locationPrimary: {
    fontSize: 16,
    color: '#ffffff',
    fontWeight: '500',
  },
  locationSecondary: {
    fontSize: 13,
    color: '#999999',
    marginTop: 2,
  },
});
```

### Critères d'acceptation

- [ ] Maximum 5 résultats affichés
- [ ] Pas de doublons visuels
- [ ] Affichage clair : ville en gras, région/pays en dessous
- [ ] Les coordonnées correctes sont enregistrées

---

## T5 — Ajouter les indicateurs de phase sur le calendrier

### Priorité : P1 — IMPORTANT

### Problème

Le calendrier n'affiche aucun indicateur visuel des phases lunaires sur les jours.

### Fichiers concernés

```
apps/mobile/
├── app/(tabs)/calendar.tsx
├── components/CalendarDay.tsx (à créer)
├── constants/lunarPhases.ts (à créer)
```

### Tâches

#### 1. Créer les constantes de phases

Créer `constants/lunarPhases.ts` :

```typescript
export const PHASE_ICONS: Record<string, string> = {
  new_moon: '🌑',
  waxing_crescent: '🌒',
  first_quarter: '🌓',
  waxing_gibbous: '🌔',
  full_moon: '🌕',
  waning_gibbous: '🌖',
  last_quarter: '🌗',
  waning_crescent: '🌘',
};

export const PHASE_NAMES_FR: Record<string, string> = {
  new_moon: 'Nouvelle Lune',
  waxing_crescent: 'Premier Croissant',
  first_quarter: 'Premier Quartier',
  waxing_gibbous: 'Gibbeuse Croissante',
  full_moon: 'Pleine Lune',
  waning_gibbous: 'Gibbeuse Décroissante',
  last_quarter: 'Dernier Quartier',
  waning_crescent: 'Dernier Croissant',
};

export const MAIN_PHASES = ['new_moon', 'first_quarter', 'full_moon', 'last_quarter'];
```

#### 2. Créer le composant CalendarDay

Créer `components/CalendarDay.tsx` :

```typescript
import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';
import { PHASE_ICONS, MAIN_PHASES } from '@/constants/lunarPhases';

interface CalendarDayProps {
  day: number;
  isCurrentMonth: boolean;
  isToday: boolean;
  phase?: string;
  onPress?: () => void;
}

export function CalendarDay({ 
  day, 
  isCurrentMonth, 
  isToday, 
  phase,
  onPress 
}: CalendarDayProps) {
  const isMainPhase = phase && MAIN_PHASES.includes(phase);
  
  return (
    <TouchableOpacity 
      style={[
        styles.container,
        isToday && styles.todayContainer,
        !isCurrentMonth && styles.otherMonth,
      ]}
      onPress={onPress}
      disabled={!isCurrentMonth}
      activeOpacity={0.7}
    >
      <Text style={[
        styles.dayNumber,
        isToday && styles.todayNumber,
        !isCurrentMonth && styles.otherMonthNumber,
      ]}>
        {day}
      </Text>
      
      {phase && isCurrentMonth && (
        <Text style={[
          styles.phaseIcon,
          isMainPhase && styles.mainPhaseIcon,
        ]}>
          {PHASE_ICONS[phase] || '○'}
        </Text>
      )}
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    width: 44,
    height: 58,
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: 8,
    margin: 2,
  },
  todayContainer: {
    borderWidth: 2,
    borderColor: '#a78bfa',
    backgroundColor: 'rgba(167, 139, 250, 0.1)',
  },
  otherMonth: {
    opacity: 0.3,
  },
  dayNumber: {
    fontSize: 16,
    color: '#ffffff',
    fontWeight: '500',
  },
  todayNumber: {
    fontWeight: '700',
    color: '#a78bfa',
  },
  otherMonthNumber: {
    color: '#666666',
  },
  phaseIcon: {
    fontSize: 10,
    marginTop: 2,
    opacity: 0.7,
  },
  mainPhaseIcon: {
    fontSize: 12,
    opacity: 1,
  },
});
```

#### 3. Intégrer dans calendar.tsx

```typescript
import { CalendarDay } from '@/components/CalendarDay';
import useSWR from 'swr';
import { useMemo } from 'react';

export default function CalendarScreen() {
  const [currentMonth, setCurrentMonth] = useState(new Date());
  
  const monthKey = `${currentMonth.getFullYear()}-${currentMonth.getMonth() + 1}`;
  
  const { data: phasesData } = useSWR(
    `/api/lunar/phases?month=${currentMonth.getMonth() + 1}&year=${currentMonth.getFullYear()}`,
    fetcher
  );
  
  // Map jour -> phase pour accès O(1)
  const phasesByDay = useMemo(() => {
    if (!phasesData?.phases) return {};
    
    const map: Record<number, string> = {};
    for (const phase of phasesData.phases) {
      const day = new Date(phase.date).getDate();
      map[day] = phase.phase;
    }
    return map;
  }, [phasesData]);
  
  const calendarDays = useMemo(() => 
    generateCalendarDays(currentMonth), 
    [currentMonth]
  );
  
  return (
    <View style={styles.container}>
      {/* Header avec navigation mois */}
      <CalendarHeader 
        month={currentMonth}
        onPrevious={() => setCurrentMonth(subMonths(currentMonth, 1))}
        onNext={() => setCurrentMonth(addMonths(currentMonth, 1))}
      />
      
      {/* Jours de la semaine */}
      <View style={styles.weekRow}>
        {['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'].map(d => (
          <Text key={d} style={styles.weekDay}>{d}</Text>
        ))}
      </View>
      
      {/* Grille des jours */}
      <View style={styles.daysGrid}>
        {calendarDays.map((dayInfo, index) => (
          <CalendarDay
            key={`${monthKey}-${index}`}
            day={dayInfo.day}
            isCurrentMonth={dayInfo.isCurrentMonth}
            isToday={dayInfo.isToday}
            phase={dayInfo.isCurrentMonth ? phasesByDay[dayInfo.day] : undefined}
            onPress={() => handleDayPress(dayInfo)}
          />
        ))}
      </View>
      
      {/* Section phases principales */}
      <MainPhasesSection phases={phasesData?.phases || []} />
    </View>
  );
}

// Helper pour générer les jours du calendrier
function generateCalendarDays(month: Date) {
  const year = month.getFullYear();
  const monthIndex = month.getMonth();
  
  const firstDay = new Date(year, monthIndex, 1);
  const lastDay = new Date(year, monthIndex + 1, 0);
  
  // Jour de la semaine du 1er (0=dimanche, on veut lundi=0)
  let startDayOfWeek = firstDay.getDay() - 1;
  if (startDayOfWeek < 0) startDayOfWeek = 6;
  
  const days = [];
  const today = new Date();
  
  // Jours du mois précédent
  const prevMonthLastDay = new Date(year, monthIndex, 0).getDate();
  for (let i = startDayOfWeek - 1; i >= 0; i--) {
    days.push({
      day: prevMonthLastDay - i,
      isCurrentMonth: false,
      isToday: false,
    });
  }
  
  // Jours du mois courant
  for (let d = 1; d <= lastDay.getDate(); d++) {
    const isToday = 
      d === today.getDate() && 
      monthIndex === today.getMonth() && 
      year === today.getFullYear();
    
    days.push({
      day: d,
      isCurrentMonth: true,
      isToday,
    });
  }
  
  // Jours du mois suivant pour compléter la grille
  const remaining = 42 - days.length; // 6 semaines * 7 jours
  for (let d = 1; d <= remaining; d++) {
    days.push({
      day: d,
      isCurrentMonth: false,
      isToday: false,
    });
  }
  
  return days;
}
```

### Critères d'acceptation

- [ ] Chaque jour affiche un emoji de phase lunaire
- [ ] Les 4 phases principales sont plus visibles (taille plus grande)
- [ ] Le jour actuel est encadré en violet
- [ ] Pas de lag au changement de mois
- [ ] Les jours hors mois sont grisés

---

## T6 — Implémenter la section VoC dans le calendrier

### Priorité : P1 — IMPORTANT

### Problème

La fonctionnalité Void of Course est mentionnée dans le README mais absente de l'écran calendrier.

### Fichiers concernés

```
apps/mobile/
├── app/(tabs)/calendar.tsx
├── components/VocSection.tsx (à créer)
├── constants/Theme.ts (vérifier les couleurs VoC)
```

### Tâches

#### 1. Vérifier l'endpoint API

```bash
# Tester l'endpoint
curl "http://localhost:8000/api/lunar/voc?start_date=2026-01-29&days=7"
```

Format attendu :
```json
{
  "voc_windows": [
    {
      "start_time": "2026-01-29T14:30:00Z",
      "end_time": "2026-01-29T18:45:00Z",
      "moon_sign_leaving": "Taurus",
      "moon_sign_entering": "Gemini",
      "duration_hours": 4.25
    }
  ]
}
```

#### 2. Créer le composant VocSection

Créer `components/VocSection.tsx` :

```typescript
import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

interface VocWindow {
  start_time: string;
  end_time: string;
  moon_sign_leaving: string;
  moon_sign_entering: string;
  duration_hours: number;
}

interface VocSectionProps {
  vocWindows: VocWindow[];
}

const SIGN_TRANSLATIONS: Record<string, string> = {
  Aries: 'Bélier',
  Taurus: 'Taureau',
  Gemini: 'Gémeaux',
  Cancer: 'Cancer',
  Leo: 'Lion',
  Virgo: 'Vierge',
  Libra: 'Balance',
  Scorpio: 'Scorpion',
  Sagittarius: 'Sagittaire',
  Capricorn: 'Capricorne',
  Aquarius: 'Verseau',
  Pisces: 'Poissons',
};

export function VocSection({ vocWindows }: VocSectionProps) {
  if (!vocWindows || vocWindows.length === 0) {
    return (
      <View style={styles.container}>
        <Text style={styles.title}>🌙 Fenêtres Void of Course</Text>
        <Text style={styles.emptyText}>
          Aucune fenêtre VoC prévue cette semaine
        </Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🌙 Fenêtres Void of Course</Text>
      <Text style={styles.subtitle}>
        Périodes à éviter pour les nouvelles initiatives
      </Text>
      
      {vocWindows.map((voc, index) => (
        <VocCard key={index} voc={voc} />
      ))}
    </View>
  );
}

function VocCard({ voc }: { voc: VocWindow }) {
  const start = new Date(voc.start_time);
  const end = new Date(voc.end_time);
  
  const formatDate = (d: Date) => 
    d.toLocaleDateString('fr-FR', { weekday: 'short', day: 'numeric', month: 'short' });
  
  const formatTime = (d: Date) => 
    d.toLocaleTimeString('fr-FR', { hour: '2-digit', minute: '2-digit' });
  
  const isSameDay = start.toDateString() === end.toDateString();
  const signFrom = SIGN_TRANSLATIONS[voc.moon_sign_leaving] || voc.moon_sign_leaving;
  const signTo = SIGN_TRANSLATIONS[voc.moon_sign_entering] || voc.moon_sign_entering;

  return (
    <View style={styles.card}>
      <View style={styles.cardHeader}>
        <View style={styles.dot} />
        <Text style={styles.cardDate}>
          {formatDate(start)}
          {!isSameDay && ` → ${formatDate(end)}`}
        </Text>
      </View>
      
      <View style={styles.cardBody}>
        <Text style={styles.cardTime}>
          {formatTime(start)} → {formatTime(end)}
        </Text>
        <Text style={styles.cardDuration}>
          ({voc.duration_hours.toFixed(1)}h)
        </Text>
      </View>
      
      <Text style={styles.cardTransit}>
        {signFrom} → {signTo}
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginTop: 24,
    paddingHorizontal: 20,
    paddingBottom: 40,
  },
  title: {
    fontSize: 18,
    fontWeight: '600',
    color: '#f59e0b', // Amber/warning
    marginBottom: 4,
  },
  subtitle: {
    fontSize: 13,
    color: '#9ca3af',
    marginBottom: 16,
  },
  emptyText: {
    fontSize: 14,
    color: '#6b7280',
    fontStyle: 'italic',
    marginTop: 8,
  },
  card: {
    backgroundColor: 'rgba(245, 158, 11, 0.15)',
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.3)',
    borderRadius: 12,
    padding: 14,
    marginBottom: 10,
  },
  cardHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 8,
  },
  dot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: '#f59e0b',
    marginRight: 10,
  },
  cardDate: {
    fontSize: 15,
    fontWeight: '600',
    color: '#ffffff',
  },
  cardBody: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 6,
  },
  cardTime: {
    fontSize: 14,
    color: '#e5e7eb',
  },
  cardDuration: {
    fontSize: 13,
    color: '#9ca3af',
    marginLeft: 8,
  },
  cardTransit: {
    fontSize: 13,
    color: '#9ca3af',
  },
});
```

#### 3. Intégrer dans calendar.tsx

```typescript
import { VocSection } from '@/components/VocSection';
import { format } from 'date-fns';

export default function CalendarScreen() {
  // ... code existant ...
  
  // Ajouter le fetch VoC
  const today = format(new Date(), 'yyyy-MM-dd');
  const { data: vocData } = useSWR(
    `/api/lunar/voc?start_date=${today}&days=7`,
    fetcher
  );
  
  return (
    <ScrollView style={styles.container}>
      {/* Calendrier */}
      <View style={styles.calendarContainer}>
        {/* ... header, grille ... */}
      </View>
      
      {/* Phases principales */}
      <MainPhasesSection phases={phasesData?.phases || []} />
      
      {/* Section VoC */}
      <VocSection vocWindows={vocData?.voc_windows || []} />
    </ScrollView>
  );
}
```

### Critères d'acceptation

- [ ] Section VoC visible sous les phases principales
- [ ] Affiche date, heures, durée et transit pour chaque fenêtre
- [ ] Couleur amber cohérente avec le VocBanner de Home
- [ ] Message approprié si aucune VoC cette semaine
- [ ] Traduction des signes en français

---

## Checklist finale pré-publication

Après avoir complété tous les tickets :

- [ ] `npm start` → App démarre sans erreur
- [ ] `npx tsc --noEmit` → Pas d'erreur TypeScript
- [ ] Navigation fluide entre tous les onglets
- [ ] Dates cohérentes Home ↔ Rapport mensuel
- [ ] Calendrier : pas de doublons, indicateurs visibles, section VoC
- [ ] Orthographe : "confidentialité", "thème" avec accents
- [ ] Autocomplétion lieu : pas de doublons
- [ ] Test sur émulateur Android
- [ ] Test sur appareil physique Android

---

## Notes pour Claude Code

### Commandes utiles

```bash
# Démarrer le projet
cd apps/mobile && npm start

# Vérifier TypeScript
npx tsc --noEmit

# Rechercher dans le code
grep -rn "pattern" apps/mobile/app apps/mobile/components

# Lancer le backend (nécessaire pour tester)
cd apps/api && uvicorn main:app --reload --port 8000
```

### Conventions du projet

- **State** : Zustand pour le state global, SWR pour le data fetching
- **Style** : StyleSheet.create, pas de inline styles
- **Couleurs** : Utiliser `Theme.colors.*` depuis `constants/Theme.ts`
- **i18n** : Vérifier si les textes sont dans `locales/fr.json`
- **Commits** : `feat(mobile): description` ou `fix(mobile): description`

### Ordre d'exécution recommandé

1. T3 (orthographe) — rapide, impact immédiat
2. T2 (doublons phases) — isolé, peu de risque
3. T1 (dates cycle) — plus complexe, tester après
4. T4 (autocomplétion) — amélioration UX
5. T5 (indicateurs calendrier) — nouveau composant
6. T6 (section VoC) — nouveau composant, dépend de l'API
