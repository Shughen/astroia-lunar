/**
 * AnimatedCard - Carte avec animation fade-in au montage
 *
 * Utilise l'API Animated native de React Native pour un effet
 * de fade-in + légère translation vers le haut lors de l'apparition.
 */

import React, { useEffect, useRef } from 'react';
import {
  Animated,
  ViewStyle,
  StyleProp,
} from 'react-native';

interface AnimatedCardProps {
  children: React.ReactNode;
  style?: StyleProp<ViewStyle>;
  delay?: number; // Délai avant le début de l'animation (ms)
  duration?: number; // Durée de l'animation (ms)
  slideDistance?: number; // Distance de translation (px)
}

export function AnimatedCard({
  children,
  style,
  delay = 0,
  duration = 400,
  slideDistance = 20,
}: AnimatedCardProps) {
  const fadeAnim = useRef(new Animated.Value(0)).current;
  const translateAnim = useRef(new Animated.Value(slideDistance)).current;

  useEffect(() => {
    const timeout = setTimeout(() => {
      Animated.parallel([
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration,
          useNativeDriver: true,
        }),
        Animated.timing(translateAnim, {
          toValue: 0,
          duration,
          useNativeDriver: true,
        }),
      ]).start();
    }, delay);

    return () => clearTimeout(timeout);
  }, [delay, duration, fadeAnim, translateAnim]);

  return (
    <Animated.View
      style={[
        style,
        {
          opacity: fadeAnim,
          transform: [{ translateY: translateAnim }],
        },
      ]}
    >
      {children}
    </Animated.View>
  );
}

/**
 * Hook pour créer une animation de fade-in réutilisable
 */
export function useFadeIn(delay = 0, duration = 400) {
  const opacity = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    const timeout = setTimeout(() => {
      Animated.timing(opacity, {
        toValue: 1,
        duration,
        useNativeDriver: true,
      }).start();
    }, delay);

    return () => clearTimeout(timeout);
  }, [delay, duration, opacity]);

  return opacity;
}

/**
 * Hook pour créer une animation de scale (zoom-in)
 */
export function useScaleIn(delay = 0, duration = 500) {
  const scale = useRef(new Animated.Value(0.8)).current;
  const opacity = useRef(new Animated.Value(0)).current;

  useEffect(() => {
    const timeout = setTimeout(() => {
      Animated.parallel([
        Animated.spring(scale, {
          toValue: 1,
          friction: 8,
          tension: 40,
          useNativeDriver: true,
        }),
        Animated.timing(opacity, {
          toValue: 1,
          duration: duration * 0.6,
          useNativeDriver: true,
        }),
      ]).start();
    }, delay);

    return () => clearTimeout(timeout);
  }, [delay, duration, scale, opacity]);

  return { scale, opacity };
}

export default AnimatedCard;
