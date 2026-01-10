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
  return (
    <View style={styles.container}>
      <Text style={styles.text}>
        {currentLunarDay !== null
          ? `Jour lunaire : ${currentLunarDay}`
          : 'Cycle lunaire : —'}
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

