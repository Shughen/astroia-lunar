/**
 * NatalMiniCard Component
 * Card horizontale raccourci vers le theme natal
 */

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import Svg, { Circle, Line } from 'react-native-svg';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { haptics } from '../services/haptics';

interface NatalMiniCardProps {
  onPress: () => void;
}

// Icone roue astrologique simplifiee
function AstroWheelIcon() {
  return (
    <Svg width={28} height={28} viewBox="0 0 24 24" fill="none">
      <Circle
        cx="12"
        cy="12"
        r="10"
        stroke={colors.accent}
        strokeWidth={1.5}
        fill={`${colors.accent}15`}
      />
      <Circle
        cx="12"
        cy="12"
        r="6"
        stroke={colors.accent}
        strokeWidth={1}
        fill="none"
      />
      <Line x1="12" y1="2" x2="12" y2="6" stroke={colors.accent} strokeWidth={1} />
      <Line x1="12" y1="18" x2="12" y2="22" stroke={colors.accent} strokeWidth={1} />
      <Line x1="2" y1="12" x2="6" y2="12" stroke={colors.accent} strokeWidth={1} />
      <Line x1="18" y1="12" x2="22" y2="12" stroke={colors.accent} strokeWidth={1} />
      <Circle cx="12" cy="12" r="2" fill={colors.accent} />
    </Svg>
  );
}

export function NatalMiniCard({ onPress }: NatalMiniCardProps) {
  const handlePress = () => {
    haptics.light();
    onPress();
  };

  return (
    <TouchableOpacity
      testID="natal-mini-card"
      style={styles.container}
      onPress={handlePress}
      activeOpacity={0.7}
    >
      <View style={styles.iconContainer}>
        <AstroWheelIcon />
      </View>
      <View style={styles.content}>
        <Text style={styles.title}>Mon thème natal</Text>
        <Text style={styles.subtitle}>Voir mon ciel de naissance</Text>
      </View>
      <Text style={styles.chevron}>{'>'}</Text>
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
  title: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '600',
    marginBottom: 2,
  },
  subtitle: {
    ...fonts.caption,
    color: colors.textMuted,
  },
  chevron: {
    fontSize: 24,
    color: colors.accent,
    fontWeight: '300',
  },
});

export default NatalMiniCard;
