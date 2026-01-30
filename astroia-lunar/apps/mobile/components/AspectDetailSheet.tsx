/**
 * AspectDetailSheet - Composant d'affichage détaillé d'un aspect v4
 *
 * Affiche les 4 sections pédagogiques:
 * - Summary (résumé 1-2 lignes)
 * - Why (3 bullets factuels)
 * - Manifestation (2-4 phrases, tone v4 professionnel)
 * - Advice (1 bullet optionnel)
 *
 * + Métadonnées factuelles (expectedAngle, actualAngle, orb, placements)
 */

import React from 'react';
import {
  View,
  Text,
  Modal,
  ScrollView,
  TouchableOpacity,
  StyleSheet,
} from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { LinearGradient } from 'expo-linear-gradient';
import Markdown from 'react-native-markdown-display';
import { AspectV4 } from '../types/api';
import { colors } from '../constants/theme';
import { tSign, tPlanet } from '../i18n/astro.format';
import { translateAstrologyText } from '../utils/astrologyTranslations';

interface AspectDetailSheetProps {
  visible: boolean;
  onClose: () => void;
  aspect: AspectV4 | null;
}

export const AspectDetailSheet: React.FC<AspectDetailSheetProps> = ({
  visible,
  onClose,
  aspect,
}) => {
  if (!aspect) {
    return null;
  }

  // Fallback si copy absent (offline, erreur backend)
  const hasCopy = aspect.copy && aspect.copy.summary;

  // Symboles d'aspects
  const aspectSymbols: Record<string, string> = {
    conjunction: '☌',
    opposition: '☍',
    square: '□',
    trine: '△',
    sextile: '⚹',
  };

  const aspectNamesFR: Record<string, string> = {
    conjunction: 'Conjonction',
    opposition: 'Opposition',
    square: 'Carré',
    trine: 'Trigone',
    sextile: 'Sextile',
  };

  const aspectSymbol = aspectSymbols[aspect.type] || '○';
  const aspectName = aspectNamesFR[aspect.type] || aspect.type;

  // Traduction signes
  const sign1 = tSign(aspect.placements.planet1.sign);
  const sign2 = tSign(aspect.placements.planet2.sign);

  // Labels maisons
  const house1 = aspect.placements.planet1.house
    ? `Maison ${aspect.placements.planet1.house}`
    : 'Maison N/A';
  const house2 = aspect.placements.planet2.house
    ? `Maison ${aspect.placements.planet2.house}`
    : 'Maison N/A';

  return (
    <Modal
      visible={visible}
      animationType="slide"
      presentationStyle="pageSheet"
      onRequestClose={onClose}
    >
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        <SafeAreaView style={styles.safeArea} edges={['top', 'bottom']}>
          {/* Header */}
          <View style={styles.header}>
            <TouchableOpacity onPress={onClose} style={styles.closeButton}>
              <Text style={styles.closeText}>← Retour</Text>
            </TouchableOpacity>
            <View style={styles.headerTitle}>
              <Text style={styles.headerSymbol}>{aspectSymbol}</Text>
              <Text style={styles.headerText}>{aspectName}</Text>
            </View>
          </View>

          <ScrollView
            contentContainerStyle={styles.scrollContent}
            showsVerticalScrollIndicator={false}
          >
            {/* Métadonnées factuelles */}
            <View style={styles.metadataCard}>
              <Text style={styles.metadataTitle}>📐 Données factuelles</Text>

              <View style={styles.metadataRow}>
                <Text style={styles.metadataLabel}>Planètes :</Text>
                <Text style={styles.metadataValue}>
                  {tPlanet(aspect.planet1)} ({sign1}, {house1}) ↔ {tPlanet(aspect.planet2)} ({sign2}, {house2})
                </Text>
              </View>

              <View style={styles.metadataRow}>
                <Text style={styles.metadataLabel}>Angle attendu :</Text>
                <Text style={styles.metadataValue}>{aspect.expected_angle}°</Text>
              </View>

              {aspect.actual_angle !== undefined && aspect.actual_angle !== null && (
                <View style={styles.metadataRow}>
                  <Text style={styles.metadataLabel}>Angle mesuré :</Text>
                  <Text style={styles.metadataValue}>{aspect.actual_angle.toFixed(1)}°</Text>
                </View>
              )}

              {aspect.delta_to_exact !== undefined && aspect.delta_to_exact !== null && (
                <View style={styles.metadataRow}>
                  <Text style={styles.metadataLabel}>Distance à l'exact :</Text>
                  <Text style={styles.metadataValue}>
                    {aspect.delta_to_exact.toFixed(1)}° (
                    {aspect.delta_to_exact <= 1
                      ? 'exact'
                      : aspect.delta_to_exact <= 3
                      ? 'serré'
                      : aspect.delta_to_exact <= 6
                      ? 'moyen'
                      : 'large'}
                    )
                  </Text>
                </View>
              )}
            </View>

            {/* Sections pédagogiques (copy) */}
            {hasCopy && aspect.copy ? (
              <>
                {/* Section 1: Summary */}
                <View style={styles.section}>
                  <Text style={styles.sectionTitle}>✨ En bref</Text>
                  <Text style={styles.summaryText}>{translateAstrologyText(aspect.copy.summary)}</Text>
                </View>

                {/* Section 2: Why (bullets factuels) */}
                <View style={styles.section}>
                  <Text style={styles.sectionTitle}>🔍 Pourquoi cet aspect ?</Text>
                  {aspect.copy.why.map((bullet, index) => (
                    <View key={index} style={styles.bulletRow}>
                      <Text style={styles.bulletDot}>•</Text>
                      <Text style={styles.bulletText}>{translateAstrologyText(bullet)}</Text>
                    </View>
                  ))}
                </View>

                {/* Section 3: Manifestation (tone v4 professionnel) */}
                <View style={styles.section}>
                  <Text style={styles.sectionTitle}>🌟 Manifestations concrètes</Text>
                  <Markdown style={markdownStyles as any}>
                    {translateAstrologyText(aspect.copy.manifestation)}
                  </Markdown>
                </View>

                {/* Section 4: Advice (optionnel) */}
                {aspect.copy.advice && (
                  <View style={styles.section}>
                    <Text style={styles.sectionTitle}>💡 Conseil pratique</Text>
                    <Markdown style={markdownStyles as any}>
                      {translateAstrologyText(aspect.copy.advice)}
                    </Markdown>
                  </View>
                )}

                {/* Section 5: Shadow/Attention (v5 optionnel) */}
                {aspect.copy.shadow && (
                  <View style={[styles.section, styles.shadowSection]}>
                    <Text style={styles.sectionTitle}>⚠️ Attention</Text>
                    <Markdown style={markdownStyles as any}>
                      {translateAstrologyText(aspect.copy.shadow)}
                    </Markdown>
                  </View>
                )}
              </>
            ) : (
              // Fallback si copy absent
              <View style={styles.fallbackCard}>
                <Text style={styles.fallbackText}>
                  ℹ️ Explications détaillées non disponibles pour cet aspect.
                </Text>
                <Text style={styles.fallbackHint}>
                  Type: {aspectName} • Orbe: {Math.abs(aspect.orb).toFixed(1)}°
                </Text>
              </View>
            )}
          </ScrollView>
        </SafeAreaView>
      </LinearGradient>
    </Modal>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  safeArea: {
    flex: 1,
  },
  header: {
    paddingHorizontal: 20,
    paddingVertical: 15,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.1)',
  },
  closeButton: {
    marginBottom: 10,
  },
  closeText: {
    color: colors.accent,
    fontSize: 16,
    fontWeight: '600',
  },
  headerTitle: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
  },
  headerSymbol: {
    fontSize: 32,
    color: colors.text,
  },
  headerText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: colors.text,
  },
  scrollContent: {
    paddingHorizontal: 20,
    paddingVertical: 20,
    paddingBottom: 40,
  },

  // Métadonnées factuelles
  metadataCard: {
    backgroundColor: 'rgba(255,255,255,0.05)',
    borderRadius: 12,
    padding: 15,
    marginBottom: 20,
    borderWidth: 1,
    borderColor: 'rgba(255,255,255,0.1)',
  },
  metadataTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: colors.text,
    marginBottom: 12,
  },
  metadataRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginBottom: 8,
    flexWrap: 'wrap',
  },
  metadataLabel: {
    fontSize: 14,
    color: colors.textMuted,
    flex: 1,
  },
  metadataValue: {
    fontSize: 14,
    color: colors.text,
    fontWeight: '500',
    flex: 2,
    textAlign: 'right',
  },

  // Sections pédagogiques
  section: {
    marginBottom: 24,
  },
  sectionTitle: {
    fontSize: 18,
    fontWeight: '600',
    color: colors.text,
    marginBottom: 12,
  },
  summaryText: {
    fontSize: 16,
    lineHeight: 24,
    color: colors.text,
    fontStyle: 'italic',
  },
  bulletRow: {
    flexDirection: 'row',
    marginBottom: 8,
  },
  bulletDot: {
    fontSize: 16,
    color: colors.accent,
    marginRight: 8,
    marginTop: 2,
  },
  bulletText: {
    fontSize: 15,
    lineHeight: 22,
    color: colors.text,
    flex: 1,
  },
  manifestationText: {
    fontSize: 15,
    lineHeight: 24,
    color: colors.text,
  },
  adviceText: {
    fontSize: 15,
    lineHeight: 24,
    color: colors.text,
    fontWeight: '500',
  },

  // Section Shadow/Attention (v5)
  shadowSection: {
    backgroundColor: 'rgba(251, 191, 36, 0.15)', // Amber warning
    borderLeftWidth: 3,
    borderLeftColor: '#f59e0b',
    paddingLeft: 12,
  },
  shadowText: {
    fontSize: 15,
    lineHeight: 24,
    color: '#fbbf24',
    fontStyle: 'italic',
  },

  // Fallback (copy absent)
  fallbackCard: {
    backgroundColor: 'rgba(255,255,255,0.05)',
    borderRadius: 12,
    padding: 20,
    alignItems: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255,255,255,0.1)',
  },
  fallbackText: {
    fontSize: 16,
    color: colors.textMuted,
    textAlign: 'center',
    marginBottom: 10,
  },
  fallbackHint: {
    fontSize: 14,
    color: colors.textMuted,
    textAlign: 'center',
  },
});

// Styles pour le rendu Markdown
const markdownStyles = {
  body: {
    color: colors.text,
    fontSize: 15,
    lineHeight: 24,
  },
  paragraph: {
    marginTop: 0,
    marginBottom: 8,
    color: colors.text,
    fontSize: 15,
    lineHeight: 24,
  },
  strong: {
    fontWeight: '700' as const,
    color: colors.text,
  },
  bullet_list: {
    marginTop: 4,
    marginBottom: 4,
  },
  bullet_list_item: {
    flexDirection: 'row',
    marginBottom: 6,
  },
  bullet_list_icon: {
    marginRight: 8,
    color: colors.accent,
    fontSize: 15,
  },
  list_item: {
    color: colors.text,
    fontSize: 15,
    lineHeight: 24,
  },
};
