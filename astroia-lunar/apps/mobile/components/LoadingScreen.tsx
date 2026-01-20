/**
 * LoadingScreen - Écran de chargement réutilisable avec animation
 *
 * Utilise le MoonLoader pour un effet de chargement cohérent
 * à travers toute l'application.
 */

import React from 'react';
import { View, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { colors } from '../constants/theme';
import { MoonLoader } from './MoonLoader';

interface LoadingScreenProps {
  text?: string;
  size?: 'small' | 'medium' | 'large';
  fullScreen?: boolean;
}

export function LoadingScreen({
  text = 'Chargement...',
  size = 'large',
  fullScreen = true,
}: LoadingScreenProps) {
  const content = (
    <View style={styles.center}>
      <MoonLoader size={size} text={text} />
    </View>
  );

  if (fullScreen) {
    return (
      <LinearGradient colors={colors.darkBg} style={styles.container}>
        {content}
      </LinearGradient>
    );
  }

  return content;
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
  },
  center: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

export default LoadingScreen;
