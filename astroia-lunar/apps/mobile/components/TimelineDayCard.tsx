/**
 * Composant TimelineDayCard
 * Affiche un jour dans la Timeline Lunaire
 */

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useTranslation } from 'react-i18next';
import { TimelineDay } from '../types/timeline';
import { getPhaseEmoji, getPhaseKey } from '../utils/ritualHelpers';
import { translateZodiacSign } from '../utils/astrologyTranslations';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

interface TimelineDayCardProps {
  day: TimelineDay;
  onPress: (day: TimelineDay) => void;
}

/**
 * Génère le label relatif pour une date (Aujourd'hui, Hier, Demain, etc.)
 */
function getRelativeLabel(day: TimelineDay, t: any): string {
  const { type, date } = day;

  if (type === 'today') return t('timeline.today');

  const today = new Date();
  const targetDate = new Date(date);
  const diffTime = targetDate.getTime() - today.getTime();
  const diffDays = Math.round(diffTime / (1000 * 60 * 60 * 24));

  if (type === 'past') {
    if (diffDays === -1) return t('timeline.yesterday');
    return t('timeline.daysAgo', { count: Math.abs(diffDays) });
  }

  if (type === 'future') {
    if (diffDays === 1) return t('timeline.tomorrow');
    return t('timeline.inDays', { count: diffDays });
  }

  return date;
}

/**
 * Formate la date au format court (ex: "31 déc.")
 */
function formatShortDate(dateString: string, locale: string = 'fr'): string {
  const date = new Date(dateString);
  const day = date.getDate();
  const monthIndex = date.getMonth();

  const monthsFr = ['jan', 'fév', 'mar', 'avr', 'mai', 'juin', 'juil', 'août', 'sep', 'oct', 'nov', 'déc'];
  const monthsEn = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

  const months = locale === 'fr' ? monthsFr : monthsEn;
  return `${day} ${months[monthIndex]}.`;
}

export function TimelineDayCard({ day, onPress }: TimelineDayCardProps) {
  const { t, i18n } = useTranslation();

  const relativeLabel = getRelativeLabel(day, t);
  const shortDate = formatShortDate(day.date, i18n.language);
  const phaseEmoji = getPhaseEmoji(day.moon.phase);
  const phaseKey = getPhaseKey(day.moon.phase);
  const phaseLabel = t(`phases.${phaseKey}`);

  // Couleur du badge selon le type
  const isToday = day.type === 'today';
  const isPast = day.type === 'past';
  const isFuture = day.type === 'future';

  return (
    <TouchableOpacity
      style={[styles.card, isToday && styles.cardToday]}
      onPress={() => onPress(day)}
      activeOpacity={0.7}
    >
      {/* Left: Date */}
      <View style={styles.dateSection}>
        <Text style={[styles.relativeLabel, isToday && styles.relativeLabelToday]}>
          {relativeLabel}
        </Text>
        <Text style={styles.shortDate}>{shortDate}</Text>
      </View>

      {/* Center: Moon Phase + Sign */}
      <View style={styles.moonSection}>
        <View style={styles.moonRow}>
          <Text style={styles.phaseEmoji}>{phaseEmoji}</Text>
          <View style={styles.moonText}>
            <Text style={styles.phaseLabel} numberOfLines={1}>
              {phaseLabel}
            </Text>
            <Text style={styles.signLabel} numberOfLines={1}>
              {translateZodiacSign(day.moon.sign)}
            </Text>
          </View>
        </View>
      </View>

      {/* Right: Indicators */}
      <View style={styles.indicatorsSection}>
        {/* VoC Badge */}
        {day.hasVoc && (
          <View style={styles.vocBadge}>
            <Text style={styles.vocText}>{t('timeline.vocBadge')}</Text>
          </View>
        )}

        {/* Journal Indicator */}
        {day.hasJournalEntry ? (
          <Text style={styles.journalIndicator}>✓</Text>
        ) : isPast || isToday ? (
          <View style={styles.journalEmpty} />
        ) : null}
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginHorizontal: spacing.md,
    marginBottom: spacing.sm,
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
  },
  cardToday: {
    borderWidth: 2,
    borderColor: colors.accent,
  },

  // Date Section
  dateSection: {
    flex: 1,
    minWidth: 80,
  },
  relativeLabel: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    marginBottom: 2,
  },
  relativeLabelToday: {
    color: colors.accent,
    fontWeight: '600',
  },
  shortDate: {
    ...fonts.caption,
    color: colors.textDark,
  },

  // Moon Section
  moonSection: {
    flex: 2,
    paddingHorizontal: spacing.sm,
  },
  moonRow: {
    flexDirection: 'row',
    alignItems: 'center',
  },
  phaseEmoji: {
    fontSize: 24,
    marginRight: spacing.xs,
  },
  moonText: {
    flex: 1,
  },
  phaseLabel: {
    ...fonts.bodySmall,
    color: colors.text,
    fontWeight: '500',
  },
  signLabel: {
    ...fonts.caption,
    color: colors.textMuted,
  },

  // Indicators Section
  indicatorsSection: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.xs,
  },
  vocBadge: {
    backgroundColor: colors.warning,
    borderRadius: borderRadius.sm,
    paddingHorizontal: 6,
    paddingVertical: 2,
  },
  vocText: {
    ...fonts.caption,
    color: colors.darkBg[0],
    fontWeight: '600',
    fontSize: 10,
  },
  journalIndicator: {
    fontSize: 20,
    color: colors.success,
  },
  journalEmpty: {
    width: 16,
    height: 16,
    borderRadius: borderRadius.full,
    borderWidth: 1,
    borderColor: colors.textDark,
  },
});
