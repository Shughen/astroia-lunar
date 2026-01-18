/**
 * LunarCycleIndicator Component
 * Affiche le jour du cycle lunaire actuel
 */

import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { colors, fonts, spacing } from '../constants/theme';

interface LunarCycleIndicatorProps {
  currentLunarDay: number | null;
}

export function LunarCycleIndicator({ currentLunarDay }: LunarCycleIndicatorProps) {
  // Ne rien afficher si pas de données
  if (currentLunarDay === null) {
    return null;
  }

  return (
    <View style={styles.container}>
      <Text style={styles.text}>
        Jour {currentLunarDay} du cycle lunaire
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    marginBottom: spacing.md,
  },
  text: {
    ...fonts.body,
    color: colors.textMuted,
    fontSize: 14,
  },
});

