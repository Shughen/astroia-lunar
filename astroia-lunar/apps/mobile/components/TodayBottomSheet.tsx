/**
 * TodayBottomSheet Component
 * Modal animee pour le rituel quotidien (fallback sans @gorhom/bottom-sheet)
 *
 * Contenu:
 * - Header: date + phase lunaire
 * - VoC Alert (si actif)
 * - Guidance du jour + mots-cles (depuis constants/lunarGuidance.ts)
 * - Jauges energie
 * - Mansion lunaire (API ou fallback hardcode)
 * - Rituels suggerees (checkboxes)
 * - CTA Journal (navigation /journal - ecriture + historique)
 * - CTA Rapport mensuel (navigation /lunar/report)
 */

import React, { forwardRef, useImperativeHandle, useState, useCallback, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Modal,
  Animated,
  Dimensions,
  TouchableWithoutFeedback,
} from 'react-native';
import { useRouter } from 'expo-router';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { LUNAR_GUIDANCE } from '../constants/lunarGuidance';
import { useLunar } from '../contexts/LunarProvider';
import { LunarReturn } from '../services/api';
import { MoonPhaseIcon } from './icons/MoonPhaseIcon';
import { ZodiacBadge } from './icons/ZodiacIcon';
import { ProgressBar } from './ProgressBar';
import { KeywordChip } from './KeywordChip';
import { RitualCheckItem } from './RitualCheckItem';
import {
  getMoonPhaseFrench,
  getZodiacSignFrench,
  getHoroscopeMetrics,
} from '../utils/horoscopeCalculations';
import { haptics } from '../services/haptics';
import type { MansionTodayResponse } from '../hooks/useLunarData';

const { height: SCREEN_HEIGHT } = Dimensions.get('window');

// Rituels par phase
const PHASE_RITUALS: Record<string, Array<{ title: string; description: string }>> = {
  new_moon: [
    { title: 'Meditation d\'intention', description: 'Visualisez vos objectifs du cycle' },
    { title: 'Liste de souhaits', description: 'Ecrivez 3 intentions claires' },
    { title: 'Nettoyage energetique', description: 'Renouvelez l\'energie de votre espace' },
  ],
  waxing_crescent: [
    { title: 'Premier pas', description: 'Une action concrete vers votre objectif' },
    { title: 'Affirmations positives', description: 'Repetez 3 affirmations' },
    { title: 'Planification', description: 'Organisez votre semaine' },
  ],
  first_quarter: [
    { title: 'Bilan intermediaire', description: 'Evaluez vos progres' },
    { title: 'Action decisive', description: 'Prenez une decision repoussee' },
    { title: 'Perseverance', description: 'Surmontez un obstacle' },
  ],
  waxing_gibbous: [
    { title: 'Perfectionnement', description: 'Affinez vos projets' },
    { title: 'Gratitude anticipee', description: 'Remerciez pour ce qui se manifeste' },
    { title: 'Preparation', description: 'Preparez la culmination' },
  ],
  full_moon: [
    { title: 'Celebration', description: 'Reconnaissez vos accomplissements' },
    { title: 'Liberation', description: 'Laissez partir ce qui ne sert plus' },
    { title: 'Bain de lune', description: 'Meditez sous la lune' },
  ],
  waning_gibbous: [
    { title: 'Partage', description: 'Transmettez ce que vous avez appris' },
    { title: 'Gratitude', description: 'Listez 5 reconnaissances' },
    { title: 'Reflexion', description: 'Analysez ce qui a fonctionne' },
  ],
  last_quarter: [
    { title: 'Lacher-prise', description: 'Abandonnez une habitude limitante' },
    { title: 'Tri et rangement', description: 'Desencombrez un espace' },
    { title: 'Pardon', description: 'Pardonnez-vous ou quelqu\'un' },
  ],
  waning_crescent: [
    { title: 'Repos', description: 'Accordez-vous du temps' },
    { title: 'Introspection', description: 'Meditez sur les lecons du cycle' },
    { title: 'Reve lucide', description: 'Notez vos reves au reveil' },
  ],
};

// Mansions lunaires (MVP hardcode)
const LUNAR_MANSIONS = [
  { number: 1, name: 'Al-Sharatain', meaning: 'Nouveaux departs' },
  { number: 2, name: 'Al-Butain', meaning: 'Richesse et abondance' },
  { number: 3, name: 'Al-Thurayya', meaning: 'Chance et fortune' },
  { number: 4, name: 'Al-Dabaran', meaning: 'Courage et determination' },
];

function normalizePhase(phase: string | undefined): string {
  if (!phase) return 'new_moon';
  return phase.toLowerCase().replace(/\s+/g, '_');
}

interface VocStatus {
  now?: {
    is_active: boolean;
    start_at?: string;
    end_at?: string;
  };
}

interface TodayBottomSheetProps {
  vocStatus?: VocStatus | null;
  lunarReturn?: LunarReturn | null;
  mansion?: MansionTodayResponse | null;
}

export interface TodayBottomSheetRef {
  snapToIndex: (index: number) => void;
  close: () => void;
}

export const TodayBottomSheet = forwardRef<TodayBottomSheetRef, TodayBottomSheetProps>(
  ({ vocStatus, lunarReturn, mansion: mansionProp }, ref) => {
    const router = useRouter();
    const { current: lunarData } = useLunar();
    const [visible, setVisible] = useState(false);
    const [completedRituals, setCompletedRituals] = useState<Set<string>>(new Set());
    const slideAnim = useRef(new Animated.Value(SCREEN_HEIGHT)).current;

    // Expose methods to parent
    useImperativeHandle(ref, () => ({
      snapToIndex: (index: number) => {
        if (index >= 0) {
          setVisible(true);
          Animated.spring(slideAnim, {
            toValue: 0,
            useNativeDriver: true,
            tension: 65,
            friction: 11,
          }).start();
        }
      },
      close: () => {
        Animated.timing(slideAnim, {
          toValue: SCREEN_HEIGHT,
          duration: 250,
          useNativeDriver: true,
        }).start(() => setVisible(false));
      },
    }));

    const handleClose = useCallback(() => {
      haptics.light();
      Animated.timing(slideAnim, {
        toValue: SCREEN_HEIGHT,
        duration: 250,
        useNativeDriver: true,
      }).start(() => setVisible(false));
    }, [slideAnim]);

    // Derive data
    const moonPhase = lunarData?.moon?.phase || 'new_moon';
    const moonSign = lunarReturn?.moon_sign || lunarData?.moon?.sign || 'Aries';
    const normalizedPhase = normalizePhase(moonPhase);

    const phaseFrench = getMoonPhaseFrench(moonPhase);
    const signFrench = getZodiacSignFrench(moonSign);
    const lunarGuidance = LUNAR_GUIDANCE[normalizedPhase] || LUNAR_GUIDANCE.new_moon;
    const guidance = lunarGuidance.message;
    const keywords = lunarGuidance.keywords;
    const rituals = PHASE_RITUALS[normalizedPhase] || PHASE_RITUALS.new_moon;
    const metrics = getHoroscopeMetrics(moonSign, moonPhase, lunarReturn?.aspects);

    // Nom du mois courant pour le CTA rapport
    const currentMonthName = new Date().toLocaleDateString('fr-FR', { month: 'long' });

    // Mansion lunaire du jour - utilise API si disponible, sinon fallback hardcodé
    const mansion = mansionProp?.data?.mansion
      ? {
          number: mansionProp.data.mansion.number,
          name: mansionProp.data.mansion.name,
          meaning: mansionProp.data.mansion.interpretation,
        }
      : LUNAR_MANSIONS[(new Date().getDate() - 1) % LUNAR_MANSIONS.length];

    // Format date
    const today = new Date();
    const formattedDate = today.toLocaleDateString('fr-FR', {
      weekday: 'long',
      day: 'numeric',
      month: 'long',
    });

    const formatVocEndTime = (endAt?: string): string => {
      if (!endAt) return '';
      try {
        const date = new Date(endAt);
        const hours = date.getHours().toString().padStart(2, '0');
        const minutes = date.getMinutes().toString().padStart(2, '0');
        return `${hours}:${minutes}`;
      } catch {
        return '';
      }
    };

    const toggleRitual = useCallback((title: string) => {
      haptics.light();
      setCompletedRituals((prev) => {
        const newSet = new Set(prev);
        if (newSet.has(title)) {
          newSet.delete(title);
        } else {
          newSet.add(title);
        }
        return newSet;
      });
    }, []);

    const handleJournalPress = () => {
      haptics.light();
      // Fermer le sheet puis naviguer vers le journal
      Animated.timing(slideAnim, {
        toValue: SCREEN_HEIGHT,
        duration: 250,
        useNativeDriver: true,
      }).start(() => {
        setVisible(false);
        router.push('/journal');
      });
    };

    const handleReportPress = () => {
      haptics.light();
      // Fermer le sheet puis naviguer
      Animated.timing(slideAnim, {
        toValue: SCREEN_HEIGHT,
        duration: 250,
        useNativeDriver: true,
      }).start(() => {
        setVisible(false);
        router.push('/lunar/report');
      });
    };

    return (
      <>
        <Modal
          visible={visible}
          transparent
          animationType="none"
          onRequestClose={handleClose}
        >
          <TouchableWithoutFeedback onPress={handleClose}>
            <View style={styles.overlay}>
              <TouchableWithoutFeedback>
                <Animated.View
                  style={[
                    styles.sheet,
                    {
                      transform: [{ translateY: slideAnim }],
                    },
                  ]}
                >
                  {/* Handle */}
                  <View style={styles.handleContainer}>
                    <View style={styles.handle} />
                  </View>

                  <ScrollView
                    style={styles.scrollView}
                    contentContainerStyle={styles.content}
                    showsVerticalScrollIndicator={false}
                  >
                    {/* Header */}
                    <View style={styles.header}>
                      <MoonPhaseIcon phase={moonPhase} size={36} />
                      <View style={styles.headerText}>
                        <Text style={styles.dateText}>
                          {formattedDate.charAt(0).toUpperCase() + formattedDate.slice(1)}
                        </Text>
                        <Text style={styles.phaseText}>
                          {phaseFrench} en {signFrench}
                        </Text>
                      </View>
                      {moonSign && <ZodiacBadge sign={moonSign} size={40} />}
                    </View>

                    {/* VoC Alert */}
                    {vocStatus?.now?.is_active && (
                      <View style={styles.vocAlert}>
                        <View style={styles.vocIconContainer}>
                          <Text style={styles.vocIcon}>!</Text>
                        </View>
                        <View style={styles.vocContent}>
                          <Text style={styles.vocTitle}>Void of Course</Text>
                          <Text style={styles.vocSubtitle}>
                            Jusqu'a {formatVocEndTime(vocStatus.now.end_at)}
                          </Text>
                        </View>
                      </View>
                    )}

                    {/* Guidance */}
                    <View style={styles.section}>
                      <Text style={styles.sectionTitle}>Guidance du jour</Text>
                      <Text style={styles.guidanceText}>{guidance}</Text>
                      <View style={styles.keywordsRow}>
                        {keywords.map((keyword, index) => (
                          <KeywordChip
                            key={index}
                            label={keyword}
                            variant={index === 0 ? 'gold' : 'default'}
                          />
                        ))}
                      </View>
                    </View>

                    {/* Energy Gauges */}
                    <View style={styles.section}>
                      <Text style={styles.sectionTitle}>Energies du jour</Text>
                      <View style={styles.metricsRow}>
                        <View style={styles.metricItem}>
                          <ProgressBar
                            label="Energie Creative"
                            value={metrics.creativeEnergy}
                            color={colors.gold}
                          />
                        </View>
                        <View style={styles.metricItem}>
                          <ProgressBar
                            label="Intuition"
                            value={metrics.intuition}
                            color={colors.accent}
                          />
                        </View>
                      </View>
                    </View>

                    {/* Lunar Mansion */}
                    <View style={styles.section}>
                      <Text style={styles.sectionTitle}>Mansion Lunaire</Text>
                      <View style={styles.mansionCard}>
                        <Text style={styles.mansionNumber}>#{mansion.number}</Text>
                        <View style={styles.mansionInfo}>
                          <Text style={styles.mansionName}>{mansion.name}</Text>
                          <Text style={styles.mansionMeaning}>{mansion.meaning}</Text>
                        </View>
                      </View>
                    </View>

                    {/* Rituals */}
                    <View style={styles.section}>
                      <Text style={styles.sectionTitle}>Rituels suggeres</Text>
                      {rituals.map((ritual, index) => (
                        <RitualCheckItem
                          key={index}
                          title={ritual.title}
                          description={ritual.description}
                          checked={completedRituals.has(ritual.title)}
                          onToggle={() => toggleRitual(ritual.title)}
                        />
                      ))}
                    </View>

                    {/* Journal CTA */}
                    <TouchableOpacity
                      style={styles.journalButton}
                      onPress={handleJournalPress}
                      activeOpacity={0.8}
                    >
                      <Text style={styles.journalButtonText}>Mon journal</Text>
                    </TouchableOpacity>

                    {/* Report CTA */}
                    <TouchableOpacity
                      style={styles.reportButton}
                      onPress={handleReportPress}
                      activeOpacity={0.8}
                    >
                      <Text style={styles.reportButtonText}>
                        Voir le rapport de {currentMonthName} →
                      </Text>
                    </TouchableOpacity>

                    {/* Bottom padding */}
                    <View style={{ height: spacing.xxl }} />
                  </ScrollView>
                </Animated.View>
              </TouchableWithoutFeedback>
            </View>
          </TouchableWithoutFeedback>
        </Modal>
      </>
    );
  }
);

TodayBottomSheet.displayName = 'TodayBottomSheet';

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'flex-end',
  },
  sheet: {
    backgroundColor: colors.cardBg,
    borderTopLeftRadius: borderRadius.lg,
    borderTopRightRadius: borderRadius.lg,
    maxHeight: SCREEN_HEIGHT * 0.9,
    minHeight: SCREEN_HEIGHT * 0.7,
  },
  handleContainer: {
    alignItems: 'center',
    paddingVertical: spacing.md,
  },
  handle: {
    width: 40,
    height: 4,
    backgroundColor: colors.textMuted,
    borderRadius: 2,
  },
  scrollView: {
    flex: 1,
  },
  content: {
    paddingHorizontal: spacing.lg,
    paddingBottom: spacing.xl,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: spacing.lg,
    paddingBottom: spacing.md,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(183, 148, 246, 0.1)',
  },
  headerText: {
    flex: 1,
    marginLeft: spacing.md,
  },
  dateText: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
    marginBottom: 2,
  },
  phaseText: {
    ...fonts.bodySmall,
    color: colors.textMuted,
  },
  vocAlert: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.vocBg,
    borderRadius: borderRadius.md,
    padding: spacing.md,
    marginBottom: spacing.lg,
    borderWidth: 1,
    borderColor: colors.vocBorder,
  },
  vocIconContainer: {
    width: 28,
    height: 28,
    borderRadius: 14,
    backgroundColor: colors.vocWarning,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: spacing.md,
  },
  vocIcon: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1a0b2e',
  },
  vocContent: {
    flex: 1,
  },
  vocTitle: {
    ...fonts.body,
    color: colors.vocWarning,
    fontWeight: '600',
  },
  vocSubtitle: {
    ...fonts.caption,
    color: colors.text,
    opacity: 0.8,
  },
  section: {
    marginBottom: spacing.xl,
  },
  sectionTitle: {
    ...fonts.bodySmall,
    color: colors.gold,
    fontWeight: '600',
    textTransform: 'uppercase',
    letterSpacing: 0.5,
    marginBottom: spacing.md,
  },
  guidanceText: {
    ...fonts.body,
    color: colors.text,
    lineHeight: 24,
    marginBottom: spacing.md,
    fontStyle: 'italic',
  },
  keywordsRow: {
    flexDirection: 'row',
    flexWrap: 'wrap',
  },
  metricsRow: {
    flexDirection: 'row',
    gap: spacing.md,
  },
  metricItem: {
    flex: 1,
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
  },
  mansionCard: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255, 215, 0, 0.08)',
    borderRadius: borderRadius.md,
    padding: spacing.md,
    borderWidth: 1,
    borderColor: 'rgba(255, 215, 0, 0.2)',
  },
  mansionNumber: {
    fontSize: 24,
    fontWeight: '700',
    color: colors.gold,
    marginRight: spacing.md,
    minWidth: 40,
  },
  mansionInfo: {
    flex: 1,
  },
  mansionName: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
    marginBottom: 2,
  },
  mansionMeaning: {
    ...fonts.caption,
    color: colors.textMuted,
  },
  journalButton: {
    backgroundColor: colors.accent,
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    alignItems: 'center',
    marginTop: spacing.md,
  },
  journalButtonText: {
    ...fonts.button,
    color: '#000000',
    fontWeight: '600',
  },
  reportButton: {
    backgroundColor: 'transparent',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    alignItems: 'center',
    marginTop: spacing.md,
    borderWidth: 1,
    borderColor: colors.accent,
  },
  reportButtonText: {
    ...fonts.button,
    color: colors.accent,
    fontWeight: '600',
  },
});

export default TodayBottomSheet;
