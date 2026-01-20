/**
 * DailyRitualCard Component
 * Carte "Rituel Quotidien" pour le dashboard Home
 *
 * Features:
 * - Affiche phase lunaire + signe + guidance quotidienne
 * - Badge VoC si actif
 * - Animation fade-in au premier affichage du jour
 * - Cache 24h avec fallback robuste
 * - i18n FR/EN
 */

import React, { useEffect, useState, useRef } from 'react';
import {
  View,
  Text,
  Pressable,
  StyleSheet,
  Animated,
  Easing,
  ActivityIndicator,
} from 'react-native';
import { useTranslation } from 'react-i18next';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { useLunar } from '../contexts/LunarProvider';
import { isFirstViewToday, markAsViewedToday } from '../services/ritualService';
import { getTodayDateString, translatePhaseToFrench } from '../utils/ritualHelpers';
import { translateZodiacSign } from '../utils/astrologyTranslations';
import { Skeleton } from './Skeleton';
import { JournalEntryModal } from './JournalEntryModal';
import { LunarCycleIndicator } from './LunarCycleIndicator';
import { hasJournalEntry } from '../services/journalService';
import { haptics } from '../services/haptics';
import { MoonPhaseIcon, ZodiacBadge } from './icons';

/**
 * Formate le timestamp de cache en date/heure lisible
 * Ex: "30 déc. 14h30" ou "Aujourd'hui 14h30"
 */
function formatCachedDate(timestamp: number): string {
  const date = new Date(timestamp);
  const now = new Date();

  // Vérifier si c'est aujourd'hui
  const isToday =
    date.getDate() === now.getDate() &&
    date.getMonth() === now.getMonth() &&
    date.getFullYear() === now.getFullYear();

  const hours = date.getHours();
  const minutes = date.getMinutes().toString().padStart(2, '0');
  const time = `${hours}h${minutes}`;

  if (isToday) {
    return `Aujourd'hui ${time}`;
  }

  // Sinon, afficher la date courte
  const day = date.getDate();
  const monthNames = ['jan', 'fév', 'mar', 'avr', 'mai', 'juin', 'juil', 'août', 'sep', 'oct', 'nov', 'déc'];
  const month = monthNames[date.getMonth()];

  return `${day} ${month}. ${time}`;
}

export function DailyRitualCard() {
  const { t, i18n } = useTranslation();
  const router = useRouter();

  // Lunar context (remplace fetchRitualData)
  const { current: data, status, helpers } = useLunar();

  // State
  const [isFirstView, setIsFirstView] = useState(false);
  const [journalModalVisible, setJournalModalVisible] = useState(false);
  const [hasJournalToday, setHasJournalToday] = useState(false);

  // Animations
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const translateAnim = useRef(new Animated.Value(20)).current;

  // Check first view and journal on mount
  useEffect(() => {
    checkFirstView();
    checkJournalEntry();
  }, []);

  // Refresh journal status when modal closes
  useEffect(() => {
    if (!journalModalVisible) {
      checkJournalEntry();
    }
  }, [journalModalVisible]);

  // Animate if first view
  useEffect(() => {
    if (isFirstView && data && !status.isLoading) {
      Animated.parallel([
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 600,
          useNativeDriver: true,
        }),
        Animated.timing(translateAnim, {
          toValue: 0,
          duration: 600,
          easing: Easing.out(Easing.cubic),
          useNativeDriver: true,
        }),
      ]).start();
    } else if (data && !status.isLoading) {
      // Pas d'animation, affichage direct
      fadeAnim.setValue(1);
      translateAnim.setValue(0);
    }
  }, [isFirstView, data, status.isLoading]);

  const checkFirstView = async () => {
    const isFirst = await isFirstViewToday();
    setIsFirstView(isFirst);
    if (isFirst) {
      await markAsViewedToday();
    }
  };

  const checkJournalEntry = async () => {
    const today = getTodayDateString();
    const exists = await hasJournalEntry(today);
    setHasJournalToday(exists);
  };

  const handleCtaPress = () => {
    haptics.light();
    // Navigation vers le rapport mensuel de révolution lunaire
    router.push('/lunar/report');
  };

  const handleJournalPress = () => {
    haptics.light();
    setJournalModalVisible(true);
  };

  // Render loading
  if (status.isLoading && !data) {
    return (
      <View style={styles.container}>
        <Skeleton width="100%" height={160} borderRadius={borderRadius.md} />
      </View>
    );
  }

  // Pas de données (ne devrait jamais arriver avec les fallbacks)
  if (!data) {
    return null;
  }

  // Derive display data from helpers
  const phaseEmoji = helpers.phaseEmoji;
  const phaseKey = helpers.phaseKey;
  const guidance = t(`ritualCard.guidance.${phaseKey}`, {
    defaultValue: t('ritualCard.guidance.fallback'),
  });
  const vocActive = helpers.vocActive;
  const vocEndTime = helpers.vocEndTime;
  
  // Accès défensif à cachedAt (non typé dans LunarContextStatus)
  const cachedAt = (status as any)?.cachedAt;

  // Texte phase + signe (traduit en français)
  const phaseFr = translatePhaseToFrench(data.moon.phase);
  const signFr = translateZodiacSign(data.moon.sign);
  const phaseText =
    data.moon.sign !== 'Unknown'
      ? `${phaseFr.toUpperCase()} EN ${signFr.toUpperCase()}`
      : phaseFr.toUpperCase();

  // Récupérer le jour du cycle lunaire depuis les données (fallback à null si absent)
  const currentLunarDay = (data.moon as any)?.lunar_day ?? null;

  return (
    <Animated.View
      style={[
        styles.container,
        {
          opacity: fadeAnim,
          transform: [{ translateY: translateAnim }],
        },
      ]}
    >
      <View style={styles.card}>
        {/* Header avec icône phase lunaire */}
        <View style={styles.header}>
          <View style={styles.headerContent}>
            <MoonPhaseIcon phase={data.moon.phase || 'new_moon'} size={28} />
            <Text style={styles.headerText}>
              {t('ritualCard.header')}
            </Text>
          </View>
          {data.moon.sign && data.moon.sign !== 'Unknown' && (
            <ZodiacBadge sign={data.moon.sign} size={32} />
          )}
        </View>

        {/* Phase + Sign */}
        <Text style={styles.phaseTitle}>{phaseText}</Text>

        {/* Lunar Cycle Indicator */}
        <LunarCycleIndicator currentLunarDay={currentLunarDay} />

        {/* Guidance */}
        <Text style={styles.guidance}>{guidance}</Text>

        {/* VoC Badge */}
        {vocActive && vocEndTime && (
          <View style={styles.vocBadge}>
            <Text style={styles.vocText}>
              ⚠️ {t('ritualCard.vocActive', { endTime: vocEndTime })}
            </Text>
          </View>
        )}

        {/* Cache/Offline indicator */}
        {cachedAt && status.source !== 'api' && (
          <View style={styles.cacheBadge}>
            <Text style={styles.cacheText}>
              {status.source === 'local'
                ? 'ℹ️ Connexion requise pour la mise à jour'
                : `ℹ️ Dernière mise à jour : ${formatCachedDate(cachedAt)}`
              }
            </Text>
          </View>
        )}
        {!cachedAt && status.source === 'local' && (
          <View style={styles.cacheBadge}>
            <Text style={styles.cacheText}>
              ℹ️ Calcul local (connexion requise pour données complètes)
            </Text>
          </View>
        )}

        {/* Journal CTA (text-button discret) */}
        <Pressable
          onPress={handleJournalPress}
          style={({ pressed }) => [
            styles.journalCta,
            pressed && styles.journalCtaPressed,
          ]}
        >
          <Text
            style={[
              styles.journalCtaText,
              hasJournalToday && styles.journalCtaTextEdited,
            ]}
          >
            {hasJournalToday ? '✓ ' : ''}
            {hasJournalToday
              ? t('ritualCard.journalEdited')
              : t('ritualCard.journalPrompt')}
          </Text>
        </Pressable>

        {/* CTA climat lunaire */}
        <Pressable
          onPress={handleCtaPress}
          style={({ pressed }) => [styles.cta, pressed && styles.ctaPressed]}
        >
          <Text style={styles.ctaText}>→ {t('ritualCard.cta')}</Text>
        </Pressable>
      </View>

      {/* Journal Modal */}
      {data && (
        <JournalEntryModal
          visible={journalModalVisible}
          onClose={() => setJournalModalVisible(false)}
          moonContext={data.moon}
        />
      )}
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: spacing.md,
    marginVertical: spacing.sm,
  },
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: spacing.sm,
  },
  headerContent: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: spacing.sm,
  },
  headerText: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    textTransform: 'uppercase',
    letterSpacing: 0.8,
  },
  phaseTitle: {
    ...fonts.h3,
    color: colors.text,
    marginBottom: spacing.md,
    letterSpacing: 0.5,
  },
  guidance: {
    ...fonts.body,
    color: colors.text,
    lineHeight: 24,
    marginBottom: spacing.md,
    fontStyle: 'italic',
  },
  vocBadge: {
    backgroundColor: 'rgba(251, 191, 36, 0.1)',
    borderWidth: 1,
    borderColor: colors.warning,
    borderRadius: borderRadius.sm,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    marginBottom: spacing.sm,
  },
  vocText: {
    ...fonts.bodySmall,
    color: colors.warning,
  },
  cacheBadge: {
    backgroundColor: 'rgba(160, 160, 176, 0.08)',
    borderWidth: 1,
    borderColor: 'rgba(160, 160, 176, 0.2)',
    borderRadius: borderRadius.sm,
    paddingVertical: spacing.sm,
    paddingHorizontal: spacing.md,
    marginBottom: spacing.sm,
  },
  cacheText: {
    ...fonts.caption,
    color: colors.textMuted,
    fontSize: 12,
  },
  cta: {
    paddingVertical: spacing.sm,
    marginTop: spacing.xs,
  },
  ctaPressed: {
    opacity: 0.7,
  },
  ctaText: {
    ...fonts.button,
    color: colors.accent,
    fontSize: 15,
  },
  journalCta: {
    paddingVertical: spacing.sm,
    marginBottom: spacing.xs,
  },
  journalCtaPressed: {
    opacity: 0.6,
  },
  journalCtaText: {
    ...fonts.body,
    color: colors.textMuted,
    fontSize: 14,
  },
  journalCtaTextEdited: {
    color: colors.success,
  },
});
