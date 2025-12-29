/**
 * Modal pour afficher l'interprétation d'un placement natal
 * Version 2 - Header simplifié, affichage markdown, maison visible
 */

import React, { useState, useEffect } from 'react';
import {
  Modal,
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  ActivityIndicator,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SafeAreaView } from 'react-native-safe-area-context';
import Markdown from 'react-native-markdown-display';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { NatalSubject, ChartPayload, NatalInterpretationResponse } from '../types/natal';
import { natalInterpretations } from '../services/api';
import { getHouseLabel } from '../utils/natalChartUtils';

interface Props {
  visible: boolean;
  onClose: () => void;
  subject: NatalSubject;
  chartId: string;
  chartPayload: ChartPayload;
}

// Mapping emoji par sujet (côté mobile)
const SUBJECT_EMOJI: Record<NatalSubject, string> = {
  sun: '☀️',
  moon: '🌙',
  ascendant: '↑',
  midheaven: '⬆️',  // Milieu du Ciel (MC)
  mercury: '☿️',
  venus: '♀️',
  mars: '♂️',
  jupiter: '♃',
  saturn: '♄',
  uranus: '♅',
  neptune: '♆',
  pluto: '♇',
  chiron: '⚕️',
  north_node: '☊',
  south_node: '☋',
  lilith: '⚸'
};

export default function NatalInterpretationModal({
  visible,
  onClose,
  subject,
  chartId,
  chartPayload,
}: Props) {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [interpretation, setInterpretation] = useState<NatalInterpretationResponse | null>(null);

  // Charger l'interprétation au mount ou au changement de subject
  useEffect(() => {
    if (visible && subject && chartId) {
      loadInterpretation();
    }
  }, [visible, subject, chartId]);

  const loadInterpretation = async () => {
    setLoading(true);
    setError(null);

    try {
      const data = await natalInterpretations.generate({
        chart_id: chartId,
        subject,
        lang: 'fr',
        chart_payload: chartPayload,
        force_refresh: false,
      });

      setInterpretation(data);

      // Log dev only
      if (__DEV__) {
        console.log(`[NatalInterpretation v${data.version}] ${subject} - Cached: ${data.cached}`);
      }
    } catch (err: any) {
      console.error('[NatalInterpretation] Erreur:', err);
      setError(
        err.response?.data?.detail ||
        err.message ||
        'Impossible de générer l\'interprétation. Réessayez.'
      );
    } finally {
      setLoading(false);
    }
  };

  const handleRefresh = async () => {
    setLoading(true);
    setError(null);

    try {
      const data = await natalInterpretations.generate({
        chart_id: chartId,
        subject,
        lang: 'fr',
        chart_payload: chartPayload,
        force_refresh: true, // Forcer régénération (bypass cache)
      });

      setInterpretation(data);
    } catch (err: any) {
      setError(
        err.response?.data?.detail ||
        err.message ||
        'Impossible de régénérer l\'interprétation.'
      );
    } finally {
      setLoading(false);
    }
  };

  // Emoji pour le header
  const emoji = SUBJECT_EMOJI[subject] || '⭐';

  return (
    <Modal
      visible={visible}
      animationType="slide"
      transparent={true}
      onRequestClose={onClose}
    >
      <LinearGradient colors={colors.darkBg} style={styles.modalOverlay}>
        <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
          <View style={styles.modalContent}>
            {/* Header - Simple: Emoji + Nom */}
            <View style={styles.header}>
              <View style={styles.headerLeft}>
                <Text style={styles.title}>
                  {emoji} {chartPayload.subject_label}
                </Text>
                {chartPayload.house && (
                  <Text style={styles.houseSubtitle}>
                    Maison {chartPayload.house} ({getHouseLabel(chartPayload.house)})
                  </Text>
                )}
              </View>
              <TouchableOpacity onPress={onClose} style={styles.closeButton}>
                <Text style={styles.closeText}>✕</Text>
              </TouchableOpacity>
            </View>

            {/* Content */}
            <ScrollView
              style={styles.scrollView}
              contentContainerStyle={styles.scrollContent}
              showsVerticalScrollIndicator={false}
            >
              {loading && (
                <View style={styles.loadingContainer}>
                  <ActivityIndicator size="large" color={colors.accent} />
                  <Text style={styles.loadingText}>
                    {interpretation ? 'Régénération...' : 'Génération de l\'interprétation...'}
                  </Text>
                </View>
              )}

              {error && !loading && (
                <View style={styles.errorContainer}>
                  <Text style={styles.errorEmoji}>⚠️</Text>
                  <Text style={styles.errorText}>{error}</Text>
                  <TouchableOpacity style={styles.retryButton} onPress={loadInterpretation}>
                    <Text style={styles.retryText}>Réessayer</Text>
                  </TouchableOpacity>
                </View>
              )}

              {interpretation && !loading && !error && (
                <View style={styles.interpretationContainer}>
                  <Markdown style={markdownStyles}>{interpretation.text}</Markdown>

                  {interpretation.cached && __DEV__ && (
                    <Text style={styles.cachedBadge}>
                      ♻️ Depuis le cache (v{interpretation.version})
                    </Text>
                  )}
                </View>
              )}
            </ScrollView>

            {/* Footer */}
            <View style={styles.footer}>
              {interpretation && !loading && (
                <TouchableOpacity
                  style={styles.refreshButton}
                  onPress={handleRefresh}
                >
                  <Text style={styles.refreshText}>🔄 Régénérer</Text>
                </TouchableOpacity>
              )}
              <TouchableOpacity style={styles.primaryButton} onPress={onClose}>
                <Text style={styles.primaryButtonText}>Fermer</Text>
              </TouchableOpacity>
            </View>
          </View>
        </SafeAreaView>
      </LinearGradient>
    </Modal>
  );
}

// Styles Markdown
const markdownStyles = {
  body: {
    color: colors.text,
    fontSize: 16,
    lineHeight: 24,
  },
  heading1: {
    ...fonts.h2,
    color: colors.gold,
    marginBottom: spacing.md,
  },
  heading2: {
    ...fonts.h3,
    color: colors.accent,
    marginTop: spacing.lg,
    marginBottom: spacing.sm,
  },
  paragraph: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.md,
  },
  strong: {
    fontWeight: '600' as const,
    color: colors.gold,
  },
  bullet_list: {
    marginBottom: spacing.md,
  },
  list_item: {
    ...fonts.body,
    color: colors.text,
    marginBottom: spacing.xs,
  },
};

const styles = StyleSheet.create({
  modalOverlay: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  modalContent: {
    flex: 1,
    marginHorizontal: spacing.md,
    marginVertical: spacing.lg,
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.lg,
    overflow: 'hidden',
  },
  header: {
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'space-between',
    padding: spacing.lg,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255, 255, 255, 0.1)',
  },
  headerLeft: {
    flex: 1,
  },
  title: {
    ...fonts.h2,
    color: colors.gold,
  },
  houseSubtitle: {
    ...fonts.caption,
    color: colors.textMuted,
    marginTop: spacing.xs,
  },
  closeButton: {
    padding: spacing.sm,
    marginLeft: spacing.sm,
  },
  closeText: {
    ...fonts.h2,
    color: colors.textMuted,
  },
  scrollView: {
    flex: 1,
  },
  scrollContent: {
    padding: spacing.lg,
  },
  loadingContainer: {
    alignItems: 'center',
    paddingVertical: spacing.xl * 2,
  },
  loadingText: {
    ...fonts.body,
    color: colors.textMuted,
    marginTop: spacing.md,
  },
  errorContainer: {
    alignItems: 'center',
    paddingVertical: spacing.xl,
  },
  errorEmoji: {
    fontSize: 48,
    marginBottom: spacing.md,
  },
  errorText: {
    ...fonts.body,
    color: '#f87171',
    textAlign: 'center',
    marginBottom: spacing.lg,
  },
  retryButton: {
    backgroundColor: colors.accent,
    paddingHorizontal: spacing.lg,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
  },
  retryText: {
    ...fonts.button,
    color: colors.text,
  },
  interpretationContainer: {
    paddingBottom: spacing.lg,
  },
  cachedBadge: {
    ...fonts.caption,
    color: colors.textMuted,
    marginTop: spacing.lg,
    textAlign: 'center',
    fontStyle: 'italic',
  },
  footer: {
    flexDirection: 'row',
    padding: spacing.lg,
    borderTopWidth: 1,
    borderTopColor: 'rgba(255, 255, 255, 0.1)',
    gap: spacing.md,
  },
  refreshButton: {
    flex: 1,
    backgroundColor: 'rgba(183, 148, 246, 0.2)',
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
  },
  refreshText: {
    ...fonts.button,
    color: colors.accent,
  },
  primaryButton: {
    flex: 1,
    backgroundColor: colors.accent,
    paddingVertical: spacing.md,
    borderRadius: borderRadius.md,
    alignItems: 'center',
  },
  primaryButtonText: {
    ...fonts.button,
    color: colors.text,
  },
});
