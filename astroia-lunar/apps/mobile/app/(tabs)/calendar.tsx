/**
 * Calendar Tab Screen
 * Monthly view with lunar phases and VoC windows
 */

import React, { useState, useMemo, useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Dimensions,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';
import { haptics } from '../../services/haptics';
import { MoonPhaseIcon } from '../../components/icons/MoonPhaseIcon';
import { getPhaseSign } from '../../data/moonPhaseSigns2026';

// Fallback si LinearGradient n'est pas disponible
const LinearGradientComponent = LinearGradient || (({ colors: bgColors, style, children, ...props }: any) => {
  return <View style={[{ backgroundColor: bgColors?.[0] || '#1a0b2e' }, style]} {...props}>{children}</View>;
});

const SCREEN_WIDTH = Dimensions.get('window').width;
const DAY_SIZE = (SCREEN_WIDTH - spacing.lg * 2 - spacing.xs * 6) / 7;

const WEEKDAYS = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim'];
const MONTH_NAMES = [
  'Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
  'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre'
];

// Dates exactes des phases principales 2025-2027 (éphémérides vérifiées)
// Format: 'YYYY-MM-DD' => phase
const EXACT_PHASES: Record<string, string> = {
  // Pleines Lunes 2025
  '2025-01-13': 'full', '2025-02-12': 'full', '2025-03-14': 'full',
  '2025-04-13': 'full', '2025-05-12': 'full', '2025-06-11': 'full',
  '2025-07-10': 'full', '2025-08-09': 'full', '2025-09-07': 'full',
  '2025-10-07': 'full', '2025-11-05': 'full', '2025-12-04': 'full',
  // Pleines Lunes 2026
  '2026-01-03': 'full', '2026-02-01': 'full', '2026-03-03': 'full',
  '2026-04-02': 'full', '2026-05-01': 'full', '2026-05-31': 'full',
  '2026-06-30': 'full', '2026-07-29': 'full', '2026-08-28': 'full',
  '2026-09-26': 'full', '2026-10-26': 'full', '2026-11-24': 'full',
  '2026-12-24': 'full',
  // Pleines Lunes 2027 (dates vérifiées)
  '2027-01-22': 'full', '2027-02-21': 'full', '2027-03-22': 'full',
  '2027-04-21': 'full', '2027-05-20': 'full', '2027-06-19': 'full',
  '2027-07-18': 'full', '2027-08-17': 'full', '2027-09-16': 'full',
  '2027-10-15': 'full', '2027-11-14': 'full', '2027-12-13': 'full',
  // Pleines Lunes 2028 (dates vérifiées - 13 pleines lunes, 2 en décembre)
  '2028-01-12': 'full', '2028-02-10': 'full', '2028-03-11': 'full',
  '2028-04-09': 'full', '2028-05-08': 'full', '2028-06-07': 'full',
  '2028-07-06': 'full', '2028-08-05': 'full', '2028-09-04': 'full',
  '2028-10-03': 'full', '2028-11-02': 'full', '2028-12-02': 'full',
  '2028-12-31': 'full',
  // Pleines Lunes 2029
  '2029-01-30': 'full', '2029-02-28': 'full', '2029-03-30': 'full',
  '2029-04-28': 'full', '2029-05-27': 'full', '2029-06-26': 'full',
  '2029-07-25': 'full', '2029-08-24': 'full', '2029-09-22': 'full',
  '2029-10-22': 'full', '2029-11-21': 'full', '2029-12-20': 'full',
  // Pleines Lunes 2030
  '2030-01-19': 'full', '2030-02-18': 'full', '2030-03-19': 'full',
  '2030-04-18': 'full', '2030-05-17': 'full', '2030-06-15': 'full',
  '2030-07-15': 'full', '2030-08-13': 'full', '2030-09-11': 'full',
  '2030-10-11': 'full', '2030-11-10': 'full', '2030-12-09': 'full',
  // Pleines Lunes 2031 (13 pleines lunes, 2 en septembre)
  '2031-01-08': 'full', '2031-02-07': 'full', '2031-03-09': 'full',
  '2031-04-07': 'full', '2031-05-07': 'full', '2031-06-05': 'full',
  '2031-07-04': 'full', '2031-08-03': 'full', '2031-09-01': 'full',
  '2031-09-30': 'full', '2031-10-30': 'full', '2031-11-29': 'full',
  '2031-12-28': 'full',
  // Pleines Lunes 2032
  '2032-01-27': 'full', '2032-02-26': 'full', '2032-03-27': 'full',
  '2032-04-25': 'full', '2032-05-25': 'full', '2032-06-23': 'full',
  '2032-07-22': 'full', '2032-08-21': 'full', '2032-09-19': 'full',
  '2032-10-18': 'full', '2032-11-17': 'full', '2032-12-16': 'full',
  // Pleines Lunes 2033
  '2033-01-15': 'full', '2033-02-14': 'full', '2033-03-16': 'full',
  '2033-04-14': 'full', '2033-05-14': 'full', '2033-06-13': 'full',
  '2033-07-12': 'full', '2033-08-10': 'full', '2033-09-09': 'full',
  '2033-10-08': 'full', '2033-11-06': 'full', '2033-12-06': 'full',
  // Pleines Lunes 2034 (13 pleines lunes, 2 en juillet)
  '2034-01-04': 'full', '2034-02-03': 'full', '2034-03-05': 'full',
  '2034-04-03': 'full', '2034-05-03': 'full', '2034-06-02': 'full',
  '2034-07-01': 'full', '2034-07-31': 'full', '2034-08-29': 'full',
  '2034-09-28': 'full', '2034-10-27': 'full', '2034-11-25': 'full',
  '2034-12-25': 'full',
  // Pleines Lunes 2035
  '2035-01-23': 'full', '2035-02-22': 'full', '2035-03-23': 'full',
  '2035-04-22': 'full', '2035-05-22': 'full', '2035-06-20': 'full',
  '2035-07-20': 'full', '2035-08-19': 'full', '2035-09-17': 'full',
  '2035-10-17': 'full', '2035-11-15': 'full', '2035-12-15': 'full',
  // Nouvelles Lunes 2025
  '2025-01-29': 'new', '2025-02-28': 'new', '2025-03-29': 'new',
  '2025-04-27': 'new', '2025-05-26': 'new', '2025-06-25': 'new',
  '2025-07-24': 'new', '2025-08-23': 'new', '2025-09-21': 'new',
  '2025-10-21': 'new', '2025-11-20': 'new', '2025-12-20': 'new',
  // Nouvelles Lunes 2026
  '2026-01-18': 'new', '2026-02-17': 'new', '2026-03-19': 'new',
  '2026-04-17': 'new', '2026-05-16': 'new', '2026-06-15': 'new',
  '2026-07-14': 'new', '2026-08-12': 'new', '2026-09-11': 'new',
  '2026-10-10': 'new', '2026-11-09': 'new', '2026-12-09': 'new',
  // Nouvelles Lunes 2027
  '2027-01-07': 'new', '2027-02-06': 'new', '2027-03-08': 'new',
  '2027-04-06': 'new', '2027-05-06': 'new', '2027-06-04': 'new',
  '2027-07-04': 'new', '2027-08-02': 'new', '2027-09-01': 'new',
  '2027-09-30': 'new', '2027-10-30': 'new', '2027-11-28': 'new',
  '2027-12-28': 'new',
  // Premiers Quartiers 2026 (dates corrigees)
  '2026-01-26': 'first_quarter', '2026-02-24': 'first_quarter',
  '2026-03-25': 'first_quarter', '2026-04-24': 'first_quarter',
  '2026-05-23': 'first_quarter', '2026-06-21': 'first_quarter',
  '2026-07-21': 'first_quarter', '2026-08-20': 'first_quarter',
  '2026-09-18': 'first_quarter', '2026-10-18': 'first_quarter',
  '2026-11-17': 'first_quarter', '2026-12-17': 'first_quarter',
  // Derniers Quartiers 2026 (dates corrigees)
  '2026-01-10': 'last_quarter', '2026-02-09': 'last_quarter',
  '2026-03-11': 'last_quarter', '2026-04-10': 'last_quarter',
  '2026-05-09': 'last_quarter', '2026-06-08': 'last_quarter',
  '2026-07-07': 'last_quarter', '2026-08-06': 'last_quarter',
  '2026-09-04': 'last_quarter', '2026-10-03': 'last_quarter',
  '2026-11-01': 'last_quarter', '2026-12-01': 'last_quarter',
  '2026-12-30': 'last_quarter',
};

// Calcul des phases lunaires avec dates exactes + fallback approximatif
function getMoonPhase(date: Date): { phase: string; emoji: string } {
  // Formater la date pour lookup
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, '0');
  const day = String(date.getDate()).padStart(2, '0');
  const dateKey = `${year}-${month}-${day}`;

  // Vérifier si c'est une date exacte connue
  const exactPhase = EXACT_PHASES[dateKey];
  if (exactPhase) {
    const emojis: Record<string, string> = {
      'new': '🌑', 'first_quarter': '🌓', 'full': '🌕', 'last_quarter': '🌗'
    };
    return { phase: exactPhase, emoji: emojis[exactPhase] || '🌙' };
  }

  // Fallback: calcul approximatif pour les phases intermédiaires
  const knownNewMoon = new Date('2024-12-30T15:48:00Z').getTime();
  const lunarCycle = 29.530588853;
  const dateAtNoon = new Date(date.getFullYear(), date.getMonth(), date.getDate(), 12, 0, 0);
  const daysSinceNew = (dateAtNoon.getTime() - knownNewMoon) / (1000 * 60 * 60 * 24);
  const currentCycleDay = ((daysSinceNew % lunarCycle) + lunarCycle) % lunarCycle;

  // Phases intermédiaires seulement (les principales sont gérées par EXACT_PHASES)
  if (currentCycleDay < 7.38) return { phase: 'waxing_crescent', emoji: '🌒' };
  if (currentCycleDay < 14.77) return { phase: 'waxing_gibbous', emoji: '🌔' };
  if (currentCycleDay < 22.15) return { phase: 'waning_gibbous', emoji: '🌖' };
  return { phase: 'waning_crescent', emoji: '🌘' };
}

interface CalendarDay {
  date: Date;
  day: number;
  isCurrentMonth: boolean;
  isToday: boolean;
  moonPhase: { phase: string; emoji: string };
}

function generateCalendarDays(year: number, month: number): CalendarDay[] {
  const days: CalendarDay[] = [];
  const today = new Date();
  today.setHours(0, 0, 0, 0);

  // First day of month
  const firstDay = new Date(year, month, 1);
  // Day of week (0 = Sunday, convert to Monday start)
  let startDay = firstDay.getDay();
  startDay = startDay === 0 ? 6 : startDay - 1;

  // Days in current month
  const daysInMonth = new Date(year, month + 1, 0).getDate();
  // Days in previous month
  const daysInPrevMonth = new Date(year, month, 0).getDate();

  // Previous month days
  for (let i = startDay - 1; i >= 0; i--) {
    const date = new Date(year, month - 1, daysInPrevMonth - i);
    days.push({
      date,
      day: daysInPrevMonth - i,
      isCurrentMonth: false,
      isToday: false,
      moonPhase: getMoonPhase(date),
    });
  }

  // Current month days
  for (let i = 1; i <= daysInMonth; i++) {
    const date = new Date(year, month, i);
    date.setHours(0, 0, 0, 0);
    days.push({
      date,
      day: i,
      isCurrentMonth: true,
      isToday: date.getTime() === today.getTime(),
      moonPhase: getMoonPhase(date),
    });
  }

  // Next month days (fill to complete weeks)
  const remainingDays = 42 - days.length; // 6 rows * 7 days
  for (let i = 1; i <= remainingDays; i++) {
    const date = new Date(year, month + 1, i);
    days.push({
      date,
      day: i,
      isCurrentMonth: false,
      isToday: false,
      moonPhase: getMoonPhase(date),
    });
  }

  return days;
}

// Key phases to highlight
const KEY_PHASES = ['new', 'full', 'first_quarter', 'last_quarter'];

// Hook to fetch VoC windows for the week
function useVocWindows() {
  const [vocWindows, setVocWindows] = useState<Array<{
    start_at: string;
    end_at: string;
  }>>([]);

  useEffect(() => {
    const fetchVocWindows = async () => {
      try {
        const apiUrl = process.env.EXPO_PUBLIC_API_URL || 'http://localhost:8000';
        const response = await fetch(`${apiUrl}/api/lunar/voc/status`);
        if (response.ok) {
          const data = await response.json();
          // Extract upcoming windows from API response
          if (data.upcoming && data.upcoming.length > 0) {
            setVocWindows(data.upcoming.slice(0, 5));
          } else if (data.next) {
            // Fallback: use next VoC window if upcoming is empty
            setVocWindows([data.next]);
          }
        }
      } catch (error) {
        console.log('[Calendar] VoC windows unavailable');
      }
    };

    fetchVocWindows();
  }, []);

  return vocWindows;
}

// Format VoC window for display
function formatVocWindow(window: { start_at: string; end_at: string }): {
  date: string;
  time: string;
  duration: string;
} {
  const start = new Date(window.start_at);
  const end = new Date(window.end_at);

  const isSameDay = start.toDateString() === end.toDateString();

  // Format date
  const startDateStr = start.toLocaleDateString('fr-FR', {
    weekday: 'short',
    day: 'numeric',
    month: 'short',
  });
  const endDateStr = end.toLocaleDateString('fr-FR', {
    weekday: 'short',
    day: 'numeric',
    month: 'short',
  });

  const dateStr = isSameDay
    ? startDateStr
    : `${startDateStr} → ${endDateStr}`;

  // Format heures
  const startTime = `${start.getHours().toString().padStart(2, '0')}:${start.getMinutes().toString().padStart(2, '0')}`;
  const endTime = `${end.getHours().toString().padStart(2, '0')}:${end.getMinutes().toString().padStart(2, '0')}`;

  // Calcul durée en heures
  const durationMs = end.getTime() - start.getTime();
  const durationHours = (durationMs / (1000 * 60 * 60)).toFixed(1);

  return {
    date: dateStr.charAt(0).toUpperCase() + dateStr.slice(1),
    time: `${startTime} - ${endTime}`,
    duration: `${durationHours}h`,
  };
}

export default function CalendarScreen() {
  const router = useRouter();
  const today = new Date();
  const [currentMonth, setCurrentMonth] = useState(today.getMonth());
  const [currentYear, setCurrentYear] = useState(today.getFullYear());
  const vocWindows = useVocWindows();

  const calendarDays = useMemo(
    () => generateCalendarDays(currentYear, currentMonth),
    [currentYear, currentMonth]
  );

  const goToPreviousMonth = () => {
    haptics.light();
    if (currentMonth === 0) {
      setCurrentMonth(11);
      setCurrentYear(currentYear - 1);
    } else {
      setCurrentMonth(currentMonth - 1);
    }
  };

  const goToNextMonth = () => {
    haptics.light();
    if (currentMonth === 11) {
      setCurrentMonth(0);
      setCurrentYear(currentYear + 1);
    } else {
      setCurrentMonth(currentMonth + 1);
    }
  };

  const goToToday = () => {
    haptics.light();
    setCurrentMonth(today.getMonth());
    setCurrentYear(today.getFullYear());
  };

  const handleDayPress = (day: CalendarDay) => {
    if (!day.isCurrentMonth) return;
    haptics.light();
    // Navigate to lunar details for that day
    const monthStr = `${day.date.getFullYear()}-${String(day.date.getMonth() + 1).padStart(2, '0')}`;
    router.push(`/lunar-month/${monthStr}`);
  };

  // Find key phase days for the legend (deduplicated by phase type)
  const keyPhaseDays = useMemo(() => {
    const seen = new Set<string>();
    return calendarDays
      .filter((d) => d.isCurrentMonth && KEY_PHASES.includes(d.moonPhase.phase))
      .filter((d) => {
        if (seen.has(d.moonPhase.phase)) return false;
        seen.add(d.moonPhase.phase);
        return true;
      })
      .sort((a, b) => a.date.getTime() - b.date.getTime());
  }, [calendarDays]);

  return (
    <LinearGradientComponent colors={colors.darkBg} style={styles.container}>
      <ScrollView contentContainerStyle={styles.scrollContent}>
        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.title}>Calendrier Lunaire</Text>
        </View>

        {/* Month Navigation */}
        <View style={styles.monthNav}>
          <TouchableOpacity onPress={goToPreviousMonth} style={styles.navButton}>
            <Text style={styles.navButtonText}>{'<'}</Text>
          </TouchableOpacity>

          <TouchableOpacity onPress={goToToday}>
            <Text style={styles.monthTitle}>
              {MONTH_NAMES[currentMonth]} {currentYear}
            </Text>
          </TouchableOpacity>

          <TouchableOpacity onPress={goToNextMonth} style={styles.navButton}>
            <Text style={styles.navButtonText}>{'>'}</Text>
          </TouchableOpacity>
        </View>

        {/* Weekday Headers */}
        <View style={styles.weekdaysRow}>
          {WEEKDAYS.map((day) => (
            <View key={day} style={styles.weekdayCell}>
              <Text style={styles.weekdayText}>{day}</Text>
            </View>
          ))}
        </View>

        {/* Calendar Grid */}
        <View style={styles.calendarGrid}>
          {calendarDays.map((day, index) => {
            const isKeyPhase = KEY_PHASES.includes(day.moonPhase.phase);
            const iconPhase = day.moonPhase.phase === 'new' ? 'new_moon'
              : day.moonPhase.phase === 'full' ? 'full_moon'
              : day.moonPhase.phase;
            return (
              <TouchableOpacity
                key={index}
                style={[
                  styles.dayCell,
                  !day.isCurrentMonth && styles.dayCellInactive,
                  day.isToday && styles.dayCellToday,
                ]}
                onPress={() => handleDayPress(day)}
                disabled={!day.isCurrentMonth}
              >
                <Text
                  style={[
                    styles.dayNumber,
                    !day.isCurrentMonth && styles.dayNumberInactive,
                    day.isToday && styles.dayNumberToday,
                  ]}
                >
                  {day.day}
                </Text>
                {day.isCurrentMonth && (
                  isKeyPhase ? (
                    <MoonPhaseIcon phase={iconPhase} size={18} />
                  ) : (
                    <Text style={styles.moonEmoji}>
                      {day.moonPhase.emoji}
                    </Text>
                  )
                )}
              </TouchableOpacity>
            );
          })}
        </View>

        {/* Key Phases Legend */}
        <View style={styles.legendCard}>
          <Text style={styles.legendTitle}>Phases principales ce mois</Text>
          <View style={styles.legendGrid}>
            {keyPhaseDays.slice(0, 4).map((day, index) => {
              // Mapper les phases du calendrier vers MoonPhaseIcon
              const iconPhase = day.moonPhase.phase === 'new' ? 'new_moon'
                : day.moonPhase.phase === 'full' ? 'full_moon'
                : day.moonPhase.phase;
              return (
                <View key={index} style={styles.legendItem}>
                  <View style={styles.legendIconContainer}>
                    <MoonPhaseIcon phase={iconPhase} size={48} />
                  </View>
                  <Text style={styles.legendDate}>
                    {day.day} {MONTH_NAMES[currentMonth].slice(0, 3)}
                  </Text>
                  <Text style={styles.legendPhase}>
                    {day.moonPhase.phase === 'new' && 'Nouvelle Lune'}
                    {day.moonPhase.phase === 'full' && 'Pleine Lune'}
                    {day.moonPhase.phase === 'first_quarter' && '1er Quartier'}
                    {day.moonPhase.phase === 'last_quarter' && 'Dernier Quartier'}
                    {' '}{getPhaseSign(`${day.date.getFullYear()}-${String(day.date.getMonth() + 1).padStart(2, '0')}-${String(day.date.getDate()).padStart(2, '0')}`)}
                  </Text>
                </View>
              );
            })}
          </View>
        </View>

        {/* Quick Access */}
        <TouchableOpacity
          style={styles.quickAccessButton}
          onPress={() => {
            haptics.light();
            const monthStr = `${currentYear}-${String(currentMonth + 1).padStart(2, '0')}`;
            router.push(`/lunar-month/${monthStr}`);
          }}
        >
          <Text style={styles.quickAccessText}>
            Voir le rapport de {MONTH_NAMES[currentMonth]}
          </Text>
        </TouchableOpacity>

        {/* VoC Windows Section */}
        {vocWindows.length > 0 && (
          <View style={styles.vocSection}>
            <Text style={styles.vocSectionTitle}>Fenêtres VoC cette semaine</Text>
            <Text style={styles.vocSectionSubtitle}>
              Périodes à éviter pour les décisions importantes
            </Text>
            {vocWindows.map((window, index) => {
              const formatted = formatVocWindow(window);
              return (
                <View key={index} style={styles.vocWindowCard}>
                  <View style={styles.vocWindowIcon}>
                    <Text style={styles.vocWindowIconText}>!</Text>
                  </View>
                  <View style={styles.vocWindowInfo}>
                    <Text style={styles.vocWindowDate}>{formatted.date}</Text>
                    <Text style={styles.vocWindowTime}>
                      {formatted.time} ({formatted.duration})
                    </Text>
                  </View>
                </View>
              );
            })}
          </View>
        )}
      </ScrollView>
    </LinearGradientComponent>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollContent: {
    paddingTop: 60,
    paddingHorizontal: spacing.lg,
    paddingBottom: 100,
  },
  header: {
    alignItems: 'center',
    marginBottom: spacing.lg,
  },
  title: {
    ...fonts.h2,
    color: colors.text,
  },
  monthNav: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.lg,
  },
  navButton: {
    padding: spacing.md,
  },
  navButtonText: {
    ...fonts.h2,
    color: colors.accent,
  },
  monthTitle: {
    ...fonts.h3,
    color: colors.text,
  },
  weekdaysRow: {
    flexDirection: 'row',
    marginBottom: spacing.sm,
  },
  weekdayCell: {
    width: DAY_SIZE,
    alignItems: 'center',
    paddingVertical: spacing.xs,
  },
  weekdayText: {
    ...fonts.caption,
    color: colors.textMuted,
    fontWeight: '600',
  },
  calendarGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.xs,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  dayCell: {
    width: DAY_SIZE,
    height: DAY_SIZE + 10,
    alignItems: 'center',
    justifyContent: 'center',
    borderRadius: borderRadius.sm,
  },
  dayCellInactive: {
    opacity: 0.3,
  },
  dayCellToday: {
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    borderWidth: 1,
    borderColor: colors.accent,
  },
  dayNumber: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '500',
  },
  dayNumberInactive: {
    color: colors.textDark,
  },
  dayNumberToday: {
    color: colors.accent,
    fontWeight: '700',
  },
  moonEmoji: {
    fontSize: 12,
    marginTop: 2,
  },
  moonEmojiMain: {
    fontSize: 16,
    opacity: 1,
  },
  legendCard: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginTop: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  legendTitle: {
    ...fonts.body,
    color: colors.gold,
    fontWeight: '600',
    marginBottom: spacing.md,
  },
  legendGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'space-between',
  },
  legendItem: {
    width: '48%',
    alignItems: 'center',
    paddingVertical: spacing.sm,
    marginBottom: spacing.sm,
  },
  legendIconContainer: {
    width: 56,
    height: 56,
    borderRadius: 28,
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    alignItems: 'center',
    justifyContent: 'center',
    marginBottom: spacing.xs,
  },
  legendDate: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
  },
  legendPhase: {
    ...fonts.caption,
    color: colors.textMuted,
  },
  quickAccessButton: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginTop: spacing.md,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: colors.accent,
  },
  quickAccessText: {
    ...fonts.body,
    color: colors.accent,
  },
  // VoC Section styles
  vocSection: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginTop: spacing.lg,
    borderWidth: 1,
    borderColor: colors.vocBorder,
  },
  vocSectionTitle: {
    ...fonts.body,
    color: colors.vocWarning,
    fontWeight: '600',
    marginBottom: spacing.xs,
  },
  vocSectionSubtitle: {
    ...fonts.caption,
    color: colors.textMuted,
    marginBottom: spacing.md,
  },
  vocWindowCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.vocBg,
    borderRadius: borderRadius.sm,
    padding: spacing.md,
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(245, 158, 11, 0.2)',
  },
  vocWindowIcon: {
    width: 24,
    height: 24,
    borderRadius: 12,
    backgroundColor: colors.vocWarning,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: spacing.md,
  },
  vocWindowIconText: {
    fontSize: 12,
    fontWeight: '700',
    color: '#1a0b2e',
  },
  vocWindowInfo: {
    flex: 1,
  },
  vocWindowDate: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '500',
    marginBottom: 2,
  },
  vocWindowTime: {
    ...fonts.caption,
    color: colors.textMuted,
  },
});
