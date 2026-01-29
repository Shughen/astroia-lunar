/**
 * VocBanner Component
 * Banniere orange pour afficher le statut Void of Course
 */

import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { colors, fonts, spacing, borderRadius } from '../constants/theme';

interface VocStatus {
  now?: {
    is_active: boolean;
    start_at?: string;
    end_at?: string;
  };
}

interface VocBannerProps {
  vocStatus: VocStatus | null;
  onInfoPress?: () => void;
}

/**
 * Formate l'heure de fin du VoC
 */
function formatVocEndTime(endAt: string | undefined): string {
  if (!endAt) return '';
  try {
    const date = new Date(endAt);
    const hours = date.getHours().toString().padStart(2, '0');
    const minutes = date.getMinutes().toString().padStart(2, '0');
    return `${hours}:${minutes}`;
  } catch {
    return '';
  }
}

export function VocBanner({ vocStatus, onInfoPress }: VocBannerProps) {
  // Ne pas afficher si VoC n'est pas actif
  if (!vocStatus?.now?.is_active) {
    return null;
  }

  const endTime = formatVocEndTime(vocStatus.now.end_at);

  return (
    <TouchableOpacity
      style={styles.container}
      onPress={onInfoPress}
      activeOpacity={onInfoPress ? 0.8 : 1}
      disabled={!onInfoPress}
    >
      <LinearGradient
        colors={['rgba(245, 158, 11, 0.15)', 'rgba(245, 158, 11, 0.08)']}
        start={{ x: 0, y: 0 }}
        end={{ x: 1, y: 0 }}
        style={styles.gradient}
      >
        <View style={styles.iconContainer}>
          <Text style={styles.icon}>!</Text>
        </View>
        <View style={styles.content}>
          <Text style={styles.title}>Void of Course</Text>
          <Text style={styles.subtitle}>
            {endTime ? `Jusqu'a ${endTime}` : 'Lune sans aspects majeurs'}
          </Text>
        </View>
        {onInfoPress && (
          <Text style={styles.infoIcon}>?</Text>
        )}
      </LinearGradient>
    </TouchableOpacity>
  );
}

const styles = StyleSheet.create({
  container: {
    marginHorizontal: spacing.md,
    marginBottom: spacing.md,
    borderRadius: borderRadius.md,
    overflow: 'hidden',
    borderWidth: 1,
    borderColor: colors.vocBorder,
  },
  gradient: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: spacing.md,
    paddingHorizontal: spacing.md,
  },
  iconContainer: {
    width: 28,
    height: 28,
    borderRadius: 14,
    backgroundColor: colors.vocWarning,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: spacing.md,
  },
  icon: {
    fontSize: 16,
    fontWeight: '700',
    color: '#1a0b2e',
  },
  content: {
    flex: 1,
  },
  title: {
    ...fonts.body,
    color: colors.vocWarning,
    fontWeight: '600',
    marginBottom: 2,
  },
  subtitle: {
    ...fonts.caption,
    color: colors.text,
    opacity: 0.8,
  },
  infoIcon: {
    fontSize: 18,
    color: colors.vocWarning,
    fontWeight: '500',
  },
});

export default VocBanner;
