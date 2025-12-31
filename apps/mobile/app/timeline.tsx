/**
 * Écran Timeline Lunaire
 * Liste scrollable de jours avec contexte lunaire et indicateurs journal
 */

import React, { useState, useEffect, useCallback } from 'react';
import {
  View,
  Text,
  StyleSheet,
  FlatList,
  ActivityIndicator,
  SafeAreaView,
} from 'react-native';
import { useTranslation } from 'react-i18next';
import { LinearGradient } from 'expo-linear-gradient';
import { Stack } from 'expo-router';

import { TimelineDay } from '../types/timeline';
import { TimelineDayCard } from '../components/TimelineDayCard';
import { JournalEntryModal } from '../components/JournalEntryModal';
import { generateTimelineV2, refreshTimelineJournalIndicators } from '../services/timelineServiceV2';
import { useLunar } from '../contexts/LunarProvider';
import { getTodayDateString } from '../utils/ritualHelpers';
import { colors, fonts, spacing } from '../constants/theme';

const ITEM_HEIGHT = 88; // Hauteur approximative d'un TimelineDayCard

export default function TimelineScreen() {
  const { t } = useTranslation();

  // Lunar context
  const { getDayData } = useLunar();

  const [timeline, setTimeline] = useState<TimelineDay[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  // Modal journal
  const [modalVisible, setModalVisible] = useState(false);
  const [selectedDay, setSelectedDay] = useState<TimelineDay | null>(null);

  /**
   * Charge la timeline au montage
   */
  useEffect(() => {
    loadTimeline();
  }, [getDayData]);

  const loadTimeline = useCallback(async () => {
    try {
      setLoading(true);
      setError(false);
      // V1 : 7 jours uniquement (3 passés + aujourd'hui + 3 futurs)
      const data = await generateTimelineV2(getDayData, { daysBefore: 3, daysAfter: 3 });
      setTimeline(data);
    } catch (err) {
      console.error('[Timeline] Error loading timeline:', err);
      setError(true);
    } finally {
      setLoading(false);
    }
  }, [getDayData]);

  /**
   * Gestion du tap sur un jour
   */
  const handleDayPress = useCallback((day: TimelineDay) => {
    const { type, date } = day;

    // Futur : lecture seule (pas d'ouverture de modal pour V1)
    if (type === 'future') {
      console.log('[Timeline] Future day tapped (read-only):', date);
      // TODO: Ouvrir écran climat ou "À venir" si route disponible
      return;
    }

    // Passé ou aujourd'hui : ouvrir modal journal
    setSelectedDay(day);
    setModalVisible(true);
  }, []);

  /**
   * Callback après sauvegarde/suppression de journal
   * Rafraîchit les indicateurs sans recharger toute la timeline
   */
  const handleModalClose = useCallback(async () => {
    setModalVisible(false);
    setSelectedDay(null);

    // Rafraîchir uniquement les indicateurs journal
    if (timeline.length > 0) {
      const refreshed = await refreshTimelineJournalIndicators(timeline);
      setTimeline(refreshed);
    }
  }, [timeline]);

  /**
   * Optimisation FlatList : keyExtractor stable
   */
  const keyExtractor = useCallback((item: TimelineDay) => item.date, []);

  /**
   * Optimisation FlatList : getItemLayout pour performances
   */
  const getItemLayout = useCallback(
    (_data: TimelineDay[] | null | undefined, index: number) => ({
      length: ITEM_HEIGHT,
      offset: ITEM_HEIGHT * index,
      index,
    }),
    []
  );

  /**
   * Render item
   */
  const renderItem = useCallback(
    ({ item }: { item: TimelineDay }) => (
      <TimelineDayCard day={item} onPress={handleDayPress} />
    ),
    [handleDayPress]
  );

  /**
   * Scroll initial sur aujourd'hui
   */
  const getInitialScrollIndex = useCallback(() => {
    const todayIndex = timeline.findIndex((day) => day.type === 'today');
    return todayIndex > 0 ? todayIndex : 0;
  }, [timeline]);

  // État de chargement
  if (loading) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: t('timeline.title'),
              headerShown: true,
            }}
          />
          <View style={styles.centerContent}>
            <ActivityIndicator size="large" color={colors.accent} />
            <Text style={styles.loadingText}>{t('timeline.loadingTimeline')}</Text>
          </View>
        </SafeAreaView>
      </LinearGradient>
    );
  }

  // État d'erreur
  if (error || timeline.length === 0) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea}>
          <Stack.Screen
            options={{
              title: t('timeline.title'),
              headerShown: true,
            }}
          />
          <View style={styles.centerContent}>
            <Text style={styles.emptyTitle}>{t('timeline.emptyState.title')}</Text>
            <Text style={styles.emptySubtitle}>{t('timeline.emptyState.subtitle')}</Text>
          </View>
        </SafeAreaView>
      </LinearGradient>
    );
  }

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <SafeAreaView style={styles.safeArea}>
        <Stack.Screen
          options={{
            title: t('timeline.title'),
            headerShown: true,
          }}
        />

        {/* Header */}
        <View style={styles.header}>
          <Text style={styles.subtitle}>{t('timeline.subtitle')}</Text>
        </View>

        {/* Timeline List */}
        <FlatList
          data={timeline}
          renderItem={renderItem}
          keyExtractor={keyExtractor}
          getItemLayout={getItemLayout}
          initialScrollIndex={getInitialScrollIndex()}
          contentContainerStyle={styles.listContent}
          showsVerticalScrollIndicator={false}
          removeClippedSubviews={true}
          maxToRenderPerBatch={10}
          updateCellsBatchingPeriod={50}
          windowSize={11}
        />

        {/* Journal Entry Modal */}
        {selectedDay && (
          <JournalEntryModal
            visible={modalVisible}
            date={selectedDay.date}
            moonContext={selectedDay.moon}
            onClose={handleModalClose}
          />
        )}
      </SafeAreaView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    paddingHorizontal: spacing.md,
    paddingTop: spacing.sm,
    paddingBottom: spacing.md,
  },
  subtitle: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    textAlign: 'center',
  },
  listContent: {
    paddingVertical: spacing.sm,
  },
  centerContent: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: spacing.lg,
  },
  loadingText: {
    ...fonts.body,
    color: colors.textMuted,
    marginTop: spacing.md,
  },
  emptyTitle: {
    ...fonts.h3,
    color: colors.text,
    textAlign: 'center',
    marginBottom: spacing.sm,
  },
  emptySubtitle: {
    ...fonts.bodySmall,
    color: colors.textMuted,
    textAlign: 'center',
  },
});
