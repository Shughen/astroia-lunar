/**
 * TodayMiniCard Component
 * Card horizontale cliquable pour ouvrir le bottom sheet du jour
 */

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { MoonPhaseIcon } from './icons/MoonPhaseIcon';
import { getZodiacSignFrench, getMoonPhaseFrench } from '../utils/horoscopeCalculations';
import { haptics } from '../services/haptics';

interface TodayMiniCardProps {
  moonPhase?: string;
  moonSign?: string;
  onPress: () => void;
}

export function TodayMiniCard({ moonPhase, moonSign, onPress }: TodayMiniCardProps) {
  const phaseFrench = getMoonPhaseFrench(moonPhase);
  const signFrench = moonSign ? getZodiacSignFrench(moonSign) : null;

  const handlePress = () => {
    haptics.light();
    onPress();
  };

  // Construire le texte principal
  const mainText = signFrench
    ? `${phaseFrench} en ${signFrench}`
    : phaseFrench;

  return (
    <TouchableOpacity
      testID="today-mini-card"
      style={styles.container}
      onPress={handlePress}
      activeOpacity={0.7}
    >
      <View style={styles.iconContainer}>
        <MoonPhaseIcon phase={moonPhase || 'new_moon'} size={32} />
      </View>
      <View style={styles.content}>
        <Text style={styles.label}>Aujourd'hui</Text>
        <Text style={styles.title} numberOfLines={1}>
          {mainText}
        </Text>
      </View>
      <View style={styles.chevronContainer}>
        <Text style={styles.chevron}>^</Text>
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: colors.cardBg,
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.lg,
    marginHorizontal: spacing.md,
    marginVertical: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
    zIndex: 10,
    elevation: 5,
  },
  iconContainer: {
    width: 48,
    height: 48,
    borderRadius: 24,
    backgroundColor: 'rgba(183, 148, 246, 0.1)',
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: spacing.md,
  },
  content: {
    flex: 1,
  },
  label: {
    ...fonts.caption,
    color: colors.textMuted,
    textTransform: 'uppercase',
    letterSpacing: 0.5,
    marginBottom: 2,
  },
  title: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
  },
  chevronContainer: {
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: 'rgba(183, 148, 246, 0.15)',
    alignItems: 'center',
    justifyContent: 'center',
  },
  chevron: {
    fontSize: 14,
    color: colors.accent,
    fontWeight: '600',
  },
});

export default TodayMiniCard;
