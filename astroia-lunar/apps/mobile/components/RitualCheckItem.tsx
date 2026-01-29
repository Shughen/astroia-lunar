/**
 * RitualCheckItem Component
 * Ligne rituel avec checkbox animee
 */

import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  Animated,
} from 'react-native';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';
import { haptics } from '../services/haptics';

interface RitualCheckItemProps {
  title: string;
  description?: string;
  checked: boolean;
  onToggle: () => void;
}

export function RitualCheckItem({
  title,
  description,
  checked,
  onToggle,
}: RitualCheckItemProps) {
  const handlePress = () => {
    haptics.light();
    onToggle();
  };

  return (
    <TouchableOpacity
      style={[styles.container, checked && styles.containerChecked]}
      onPress={handlePress}
      activeOpacity={0.7}
    >
      <View style={styles.content}>
        <Text style={[styles.title, checked && styles.titleChecked]}>
          {title}
        </Text>
        {description && (
          <Text style={styles.description} numberOfLines={2}>
            {description}
          </Text>
        )}
      </View>
      <View style={[styles.checkbox, checked && styles.checkboxChecked]}>
        {checked && <Text style={styles.checkmark}>OK</Text>}
      </View>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(183, 148, 246, 0.08)',
    borderRadius: borderRadius.md,
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
    marginBottom: spacing.sm,
    borderWidth: 1,
    borderColor: 'rgba(183, 148, 246, 0.1)',
  },
  containerChecked: {
    backgroundColor: 'rgba(74, 222, 128, 0.1)',
    borderColor: 'rgba(74, 222, 128, 0.3)',
  },
  content: {
    flex: 1,
    marginRight: spacing.md,
  },
  title: {
    ...fonts.body,
    color: colors.text,
    fontWeight: '500',
    marginBottom: 2,
  },
  titleChecked: {
    color: colors.success,
    textDecorationLine: 'line-through',
  },
  description: {
    ...fonts.caption,
    color: colors.textMuted,
    lineHeight: 16,
  },
  checkbox: {
    width: 28,
    height: 28,
    borderRadius: 14,
    borderWidth: 2,
    borderColor: colors.textMuted,
    alignItems: 'center',
    justifyContent: 'center',
  },
  checkboxChecked: {
    backgroundColor: colors.success,
    borderColor: colors.success,
  },
  checkmark: {
    ...fonts.caption,
    color: colors.text,
    fontWeight: '700',
    fontSize: 10,
  },
});

export default RitualCheckItem;
