/**
 * Écran de tracking du cycle menstruel
 */

import React, { useEffect, useState } from 'react';
import {
  View,
  Text,
  StyleSheet,
  ScrollView,
  TouchableOpacity,
  Alert,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { useRouter } from 'expo-router';
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

export default function CycleTrackingScreen() {
  const router = useRouter();
  const {
    currentCycle,
    correlation,
    isLoading,
    error,
    fetchCurrentCycle,
    fetchCorrelation,
    startCycle,
    endCycle,
  } = useCycleStore();

  const [showStartDialog, setShowStartDialog] = useState(false);

  useEffect(() => {
    fetchCurrentCycle();
    if (currentCycle?.cycle) {
      fetchCorrelation();
    }
  }, []);

  const handleStartCycle = () => {
    Alert.alert(
      'Début des règles',
      'Voulez-vous enregistrer le début de vos règles aujourd\'hui ?',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Confirmer',
          onPress: async () => {
            try {
              await startCycle(new Date());
              Alert.alert('Succès', 'Cycle démarré avec succès');
            } catch (err: any) {
              Alert.alert('Erreur', err.message || 'Impossible de démarrer le cycle');
            }
          },
        },
      ]
    );
  };

  const handleEndCycle = () => {
    if (!currentCycle?.cycle) return;

    Alert.alert(
      'Fin des règles',
      'Voulez-vous enregistrer la fin de vos règles aujourd\'hui ?',
      [
        { text: 'Annuler', style: 'cancel' },
        {
          text: 'Confirmer',
          onPress: async () => {
            try {
              await endCycle(currentCycle.cycle!.id, new Date());
              Alert.alert('Succès', 'Cycle terminé avec succès');
            } catch (err: any) {
              Alert.alert('Erreur', err.message || 'Impossible de terminer le cycle');
            }
          },
        },
      ]
    );
  };

  if (isLoading && !currentCycle) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <View style={styles.center}>
          <ActivityIndicator size="large" color={colors.accent} />
          <Text style={styles.loadingText}>Chargement...</Text>
        </View>
      </LinearGradient>
    );
  }

  const cycle = currentCycle?.cycle;
  const phase = currentCycle?.phase || cycle?.current_phase;
  const day = currentCycle?.day || cycle?.cycle_day;

  return (
    <LinearGradient colors={colors.darkBg} style={styles.container}>
      <ScrollView style={styles.scrollView} contentContainerStyle={styles.content}>
        {error && (
          <View style={styles.errorContainer}>
            <Text style={styles.errorText}>⚠️ {error}</Text>
          </View>
        )}

        {!cycle ? (
          <View style={styles.emptyContainer}>
            <Text style={styles.emoji}>🩸</Text>
            <Text style={styles.emptyTitle}>Aucun cycle en cours</Text>
            <Text style={styles.emptySubtitle}>
              Commencez à suivre votre cycle menstruel
            </Text>
            <TouchableOpacity style={styles.startButton} onPress={handleStartCycle}>
              <Text style={styles.startButtonText}>🩸 Début des règles</Text>
            </TouchableOpacity>
          </View>
        ) : (
          <>
            {/* Cycle actuel */}
            <View style={styles.card}>
              <Text style={styles.cardTitle}>Cycle actuel</Text>
              <View style={styles.phaseContainer}>
                <Text style={styles.phaseEmoji}>
                  {phase ? PHASE_EMOJIS[phase] || '🌙' : '🌙'}
                </Text>
                <View style={styles.phaseInfo}>
                  <Text style={styles.phaseName}>
                    {phase ? PHASE_NAMES[phase] || phase : 'Non calculé'}
                  </Text>
                  {day && <Text style={styles.cycleDay}>Jour {day}</Text>}
                </View>
              </View>
              {currentCycle?.next_period_prediction && (
                <Text style={styles.prediction}>
                  📅 Prochaines règles prévues :{' '}
                  {new Date(currentCycle.next_period_prediction).toLocaleDateString('fr-FR')}
                </Text>
              )}
              <TouchableOpacity
                style={styles.endButton}
                onPress={handleEndCycle}
              >
                <Text style={styles.endButtonText}>Terminer le cycle</Text>
              </TouchableOpacity>
            </View>

            {/* Corrélation cycle + lune */}
            {correlation && (
              <View style={styles.card}>
                <Text style={styles.cardTitle}>🌙 Corrélation Lune</Text>
                <View style={styles.energyContainer}>
                  <Text style={styles.energyLabel}>Niveau d'énergie</Text>
                  <Text style={styles.energyValue}>
                    {correlation.energy.total_energy}%
                  </Text>
                </View>
                {correlation.lunar.moon_sign && (
                  <Text style={styles.lunarInfo}>
                    Lune en {correlation.lunar.moon_sign}
                  </Text>
                )}
                {correlation.insights && correlation.insights.length > 0 && (
                  <View style={styles.insightsContainer}>
                    {correlation.insights.map((insight, idx) => (
                      <Text key={idx} style={styles.insight}>
                        {insight}
                      </Text>
                    ))}
                  </View>
                )}
              </View>
            )}

            {/* Recommandations */}
            {correlation?.recommendations && (
              <View style={styles.card}>
                <Text style={styles.cardTitle}>💡 Recommandations</Text>
                {correlation.recommendations.activities.length > 0 && (
                  <View style={styles.recommendationSection}>
                    <Text style={styles.recommendationTitle}>Activités</Text>
                    {correlation.recommendations.activities.map((act, idx) => (
                      <Text key={idx} style={styles.recommendationItem}>
                        • {act}
                      </Text>
                    ))}
                  </View>
                )}
                {correlation.recommendations.wellness.length > 0 && (
                  <View style={styles.recommendationSection}>
                    <Text style={styles.recommendationTitle}>Bien-être</Text>
                    {correlation.recommendations.wellness.map((well, idx) => (
                      <Text key={idx} style={styles.recommendationItem}>
                        • {well}
                      </Text>
                    ))}
                  </View>
                )}
              </View>
            )}

            <TouchableOpacity
              style={styles.historyButton}
              onPress={() => router.push('/cycle/history')}
            >
              <Text style={styles.historyButtonText}>📊 Voir l'historique</Text>
            </TouchableOpacity>
          </>
        )}
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
  errorContainer: {
    backgroundColor: 'rgba(255, 0, 0, 0.1)',
    padding: spacing.md,
    borderRadius: borderRadius.md,
    marginBottom: spacing.md,
  },
  errorText: {
    color: '#ff6b6b',
    fontSize: fonts.size.sm,
  },
  emptyContainer: {
    alignItems: 'center',
    paddingVertical: spacing.xl * 2,
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
    marginBottom: spacing.xl,
  },
  startButton: {
    backgroundColor: colors.accent,
    paddingHorizontal: spacing.xl,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.lg,
  },
  startButtonText: {
    color: colors.text,
    fontSize: fonts.size.md,
    fontWeight: 'bold',
  },
  card: {
    backgroundColor: colors.cardBg,
    padding: spacing.lg,
    borderRadius: borderRadius.lg,
    marginBottom: spacing.md,
  },
  cardTitle: {
    fontSize: fonts.size.lg,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.md,
  },
  phaseContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.md,
  },
  phaseEmoji: {
    fontSize: 50,
    marginRight: spacing.md,
  },
  phaseInfo: {
    flex: 1,
  },
  phaseName: {
    fontSize: fonts.size.lg,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.xs,
  },
  cycleDay: {
    fontSize: fonts.size.md,
    color: colors.textMuted,
  },
  prediction: {
    fontSize: fonts.size.sm,
    color: colors.textMuted,
    marginTop: spacing.sm,
  },
  endButton: {
    backgroundColor: 'rgba(255, 107, 107, 0.2)',
    padding: spacing.md,
    borderRadius: borderRadius.md,
    marginTop: spacing.md,
    alignItems: 'center',
  },
  endButtonText: {
    color: '#ff6b6b',
    fontSize: fonts.size.md,
    fontWeight: 'bold',
  },
  energyContainer: {
    alignItems: 'center',
    marginVertical: spacing.md,
  },
  energyLabel: {
    fontSize: fonts.size.sm,
    color: colors.textMuted,
    marginBottom: spacing.xs,
  },
  energyValue: {
    fontSize: 48,
    fontWeight: 'bold',
    color: colors.accent,
  },
  lunarInfo: {
    fontSize: fonts.size.md,
    color: colors.textMuted,
    marginTop: spacing.sm,
  },
  insightsContainer: {
    marginTop: spacing.md,
  },
  insight: {
    fontSize: fonts.size.sm,
    color: colors.text,
    marginBottom: spacing.xs,
  },
  recommendationSection: {
    marginTop: spacing.md,
  },
  recommendationTitle: {
    fontSize: fonts.size.md,
    fontWeight: 'bold',
    color: colors.text,
    marginBottom: spacing.xs,
  },
  recommendationItem: {
    fontSize: fonts.size.sm,
    color: colors.textMuted,
    marginLeft: spacing.sm,
    marginBottom: spacing.xs,
  },
  historyButton: {
    backgroundColor: colors.cardBg,
    padding: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
    marginTop: spacing.md,
  },
  historyButtonText: {
    color: colors.accent,
    fontSize: fonts.size.md,
    fontWeight: 'bold',
  },
});

