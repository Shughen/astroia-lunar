/**
 * MoonLoader - Loader animé avec une lune qui pulse
 *
 * Affiche un emoji lune avec une animation de pulse/glow
 * pour les états de chargement de l'app.
 */

import React, { useEffect, useRef } from 'react';
import {
  Animated,
  View,
  Text,
  StyleSheet,
  Easing,
} from 'react-native';
import { colors, fonts, spacing } from '../constants/theme';

interface MoonLoaderProps {
  size?: 'small' | 'medium' | 'large';
  text?: string;
  showText?: boolean;
}

const SIZES = {
  small: { moon: 32, text: 12 },
  medium: { moon: 48, text: 14 },
  large: { moon: 64, text: 16 },
};

export function MoonLoader({
  size = 'medium',
  text = 'Chargement...',
  showText = true,
}: MoonLoaderProps) {
  const scaleAnim = useRef(new Animated.Value(1)).current;
  const opacityAnim = useRef(new Animated.Value(0.7)).current;
  const rotateAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    // Animation de pulse (scale + opacity)
    const pulseAnimation = Animated.loop(
      Animated.sequence([
        Animated.parallel([
          Animated.timing(scaleAnim, {
            toValue: 1.15,
            duration: 800,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
          Animated.timing(opacityAnim, {
            toValue: 1,
            duration: 800,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
        ]),
        Animated.parallel([
          Animated.timing(scaleAnim, {
            toValue: 1,
            duration: 800,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
          Animated.timing(opacityAnim, {
            toValue: 0.7,
            duration: 800,
            easing: Easing.inOut(Easing.ease),
            useNativeDriver: true,
          }),
        ]),
      ])
    );

    // Légère rotation
    const rotateAnimation = Animated.loop(
      Animated.timing(rotateAnim, {
        toValue: 1,
        duration: 8000,
        easing: Easing.linear,
        useNativeDriver: true,
      })
    );

    pulseAnimation.start();
    rotateAnimation.start();

    return () => {
      pulseAnimation.stop();
      rotateAnimation.stop();
    };
  }, [scaleAnim, opacityAnim, rotateAnim]);

  const { moon: moonSize, text: textSize } = SIZES[size];

  const rotate = rotateAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ['0deg', '360deg'],
  });

  return (
    <View style={styles.container}>
      <Animated.View
        style={[
          styles.moonContainer,
          {
            transform: [
              { scale: scaleAnim },
              { rotate },
            ],
            opacity: opacityAnim,
          },
        ]}
      >
        <Text style={[styles.moon, { fontSize: moonSize }]}>🌙</Text>
      </Animated.View>

      {showText && (
        <Animated.Text
          style={[
            styles.text,
            { fontSize: textSize, opacity: opacityAnim },
          ]}
        >
          {text}
        </Animated.Text>
      )}
    </View>
  );
}

/**
 * MoonSpinner - Version plus compacte pour inline loading
 */
export function MoonSpinner({ size = 24 }: { size?: number }) {
  const rotateAnim = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    const animation = Animated.loop(
      Animated.timing(rotateAnim, {
        toValue: 1,
        duration: 2000,
        easing: Easing.linear,
        useNativeDriver: true,
      })
    );
    animation.start();
    return () => animation.stop();
  }, [rotateAnim]);

  const rotate = rotateAnim.interpolate({
    inputRange: [0, 1],
    outputRange: ['0deg', '360deg'],
  });

  return (
    <Animated.Text style={{ fontSize: size, transform: [{ rotate }] }}>
      🌙
    </Animated.Text>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
    padding: spacing.lg,
  },
  moonContainer: {
    marginBottom: spacing.md,
  },
  moon: {
    textAlign: 'center',
  },
  text: {
    ...fonts.body,
    color: colors.textMuted,
    textAlign: 'center',
  },
});

export default MoonLoader;
