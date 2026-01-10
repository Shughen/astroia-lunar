/**
 * Écran d'historique des cycles menstruels
 */

import React, { useEffect } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useCycleStore } from '../../stores/useCycleStore';
import { colors, fonts, spacing, borderRadius } from '../../constants/theme';

const PHASE_EMOJIS: Record<string, string> = {
  menstrual: '🌑',
  follicular: '🌒',
  ovulation: '🌕',
  luteal: '🌘',
};

const PHASE_NAMES: Record<string, string> = {
  menstrual: 'Menstruelle',
  follicular: 'Folliculaire',
  ovulation: 'Ovulation',
  luteal: 'Lutéale',
};

export default function CycleHistoryScreen() {
  const { cycles, isLoading, error, fetchHistory } = useCycleStore();

  useEffect(() => {
    fetchHistory();
  }, []);

  if (isLoading) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <View style={styles.center}>
          <ActivityIndicator size="large" color={colors.accent} />
          <Text style={styles.loadingText}>Chargement...</Text>
        </View>
      </LinearGradient>
    );
  }

  if (error) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <View style={styles.center}>
          <Text style={styles.errorText}>⚠️ {error}</Text>
        </View>
      </LinearGradient>
    );
  }

  if (cycles.length === 0) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <View style={styles.center}>
          <Text style={styles.emoji}>📊</Text>
          <Text style={styles.emptyTitle}>Aucun historique</Text>
          <Text style={styles.emptySubtitle}>
            Votre historique de cycles apparaîtra ici
          </Text>
        </View>
      </LinearGradient>
    );
  }

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        <Text style={styles.title}>Historique des cycles</Text>
        
        {cycles.map((cycle) => {
          const startDate = new Date(cycle.start_date);
          const endDate = cycle.end_date ? new Date(cycle.end_date) : null;
          const phase = cycle.current_phase;

          return (
            <View key={cycle.id} style={styles.cycleCard}>
              <View style={styles.cycleHeader}>
                <Text style={styles.phaseEmoji}>
                  {phase ? PHASE_EMOJIS[phase] || '🌙' : '🌙'}
                </Text>
                <View style={styles.cycleInfo}>
                  <Text style={styles.cycleDate}>
                    {startDate.toLocaleDateString('fr-FR', {
                      day: 'numeric',
                      month: 'long',
                      year: 'numeric',
                    })}
                  </Text>
                  {phase && (
                    <Text style={styles.phaseName}>
                      {PHASE_NAMES[phase] || phase}
                    </Text>
                  )}
                </View>
              </View>

              <View style={styles.cycleDetails}>
                {cycle.cycle_length && (
                  <View style={styles.detailItem}>
                    <Text style={styles.detailLabel}>Durée cycle</Text>
                    <Text style={styles.detailValue}>{cycle.cycle_length} jours</Text>
                  </View>
                )}
                {cycle.period_length && (
                  <View style={styles.detailItem}>
                    <Text style={styles.detailLabel}>Durée règles</Text>
                    <Text style={styles.detailValue}>{cycle.period_length} jours</Text>
                  </View>
                )}
                {cycle.cycle_day && (
                  <View style={styles.detailItem}>
                    <Text style={styles.detailLabel}>Jour du cycle</Text>
                    <Text style={styles.detailValue}>Jour {cycle.cycle_day}</Text>
                  </View>
                )}
              </View>

              {endDate && (
                <Text style={styles.endDate}>
                  Terminé le {endDate.toLocaleDateString('fr-FR')}
                </Text>
              )}
              {!endDate && (
                <Text style={styles.activeLabel}>Cycle en cours</Text>
              )}
            </View>
          );
        })}
      </ScrollView>
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    padding: spacing.lg,
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  loadingText: {
    marginTop: spacing.md,
    color: colors.textMuted,
    fontSize: fonts.size.md,
  },
  errorText: {
    color: '#ff6b6b',
    fontSize: fonts.size.md,
    textAlign: 'center',
  },
  emoji: {
    fontSize: 80,
    marginBottom: spacing.lg,
  },
  emptyTitle: {
    fontSize: fonts.size.xl,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.sm,
  },
  emptySubtitle: {
    fontSize: fonts.size.md,
    color: colors.textMuted,
    textAlign: 'center',
  },
  title: {
    fontSize: fonts.size.xl,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.lg,
  },
  cycleCard: {
    backgroundColor: colors.cardBg,
    padding: spacing.lg,
    borderRadius: borderRadius.lg,
    marginBottom: spacing.md,
  },
  cycleHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.md,
  },
  phaseEmoji: {
    fontSize: 40,
    marginRight: spacing.md,
  },
  cycleInfo: {
    flex: 1,
  },
  cycleDate: {
    fontSize: fonts.size.md,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.xs,
  },
  phaseName: {
    fontSize: fonts.size.sm,
    color: colors.textMuted,
  },
  cycleDetails: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    marginTop: spacing.sm,
  },
  detailItem: {
    marginRight: spacing.lg,
    marginBottom: spacing.sm,
  },
  detailLabel: {
    fontSize: fonts.size.xs,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
  detailValue: {
    fontSize: fonts.size.sm,
    color: colors.text,
    fontWeight: 'bold',
  },
  endDate: {
    fontSize: fonts.size.xs,
    color: colors.textMuted,
    marginTop: spacing.sm,
  },
  activeLabel: {
    fontSize: fonts.size.sm,
    color: colors.accent,
    marginTop: spacing.sm,
    fontWeight: 'bold',
  },
});

