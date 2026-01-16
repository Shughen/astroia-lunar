/**
 * JournalPrompt Component
 * Widget discret "As-tu écrit aujourd'hui ?" pour le dashboard Home
 *
 * Features:
 * - Badge ✅ si entrée journal aujourd'hui
 * - State local, utilise hasJournalEntry() depuis journalService.ts
 * - useFocusEffect pour refresh au retour de /journal
 */

import React, { useState, useEffect, useCallback } from 'react';
import {
  View,
  Text,
  Pressable,
  StyleSheet,
  ActivityIndicator,
} from 'react-native';
import { useRouter, useFocusEffect } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { hasJournalEntry } from '../services/journalService';
import { getTodayDateString } from '../utils/ritualHelpers';

export function JournalPrompt() {
  const router = useRouter();

  // State local
  const [journalDoneToday, setJournalDoneToday] = useState(false);
  const [loading, setLoading] = useState(true);

  // Effect mount
  useEffect(() => {
    loadJournalStatus();
  }, []);

  // Effect focus (refresh au retour de /journal)
  useFocusEffect(
    useCallback(() => {
      loadJournalStatus();
    }, [])
  );

  const loadJournalStatus = async () => {
    try {
      setLoading(true);
      const today = getTodayDateString();
      const exists = await hasJournalEntry(today);
      setJournalDoneToday(exists);
    } catch (error) {
      console.error('[JournalPrompt] Erreur:', error);
    } finally {
      setLoading(false);
    }
  };

  const handlePress = () => {
    router.push('/journal');
  };

  if (loading) {
    return (
      <View style={styles.card}>
        <ActivityIndicator size="small" color={colors.accent} />
      </View>
    );
  }

  return (
    <Pressable
      onPress={handlePress}
      style={({ pressed }) => [styles.card, pressed && styles.cardPressed]}
    >
      {/* Header avec badge conditionnel */}
      <View style={styles.header}>
        <Text style={styles.title}>📖 Journal</Text>
        {journalDoneToday && (
          <View style={styles.badge}>
            <Text style={styles.badgeText}>✅ Aujourd'hui</Text>
          </View>
        )}
      </View>

      {/* Prompt */}
      <Text style={styles.prompt}>
        {journalDoneToday
          ? "Tu as déjà écrit aujourd'hui 🌙"
          : "As-tu écrit aujourd'hui ?"}
      </Text>

      {/* CTA */}
      <Text style={styles.ctaText}>
        {journalDoneToday ? 'Relire →' : 'Écrire une note →'}
      </Text>
    </Pressable>
  );
}

const styles = StyleSheet.create({
  card: {
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    padding: spacing.lg,
    marginBottom: spacing.md,
    marginHorizontal: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  cardPressed: {
    opacity: 0.8,
  },
  header: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginBottom: spacing.sm,
  },
  title: {
    ...fonts.h3,
    color: colors.text,
    fontSize: 18,
    fontWeight: 'bold',
  },
  badge: {
    backgroundColor: 'rgba(74, 222, 128, 0.15)',
    borderWidth: 1,
    borderColor: '#4ade80',
    borderRadius: 12,
    paddingHorizontal: spacing.sm,
    paddingVertical: spacing.xs,
  },
  badgeText: {
    fontSize: 10,
    color: '#4ade80',
    fontWeight: '600',
    letterSpacing: 0.5,
  },
  prompt: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.md,
    fontSize: 15,
  },
  ctaText: {
    ...fonts.button,
    color: colors.accent,
    fontSize: 14,
    fontWeight: '600',
  },
});
