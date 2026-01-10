/**
 * Skeleton loader component (Phase 1.6)
 * Provides visual feedback during data loading
 */

import React, { useEffect, useRef } from 'react';
import { View, StyleSheet, Animated } from 'react-native';

interface SkeletonProps {
  width?: number | string;
  height?: number;
  borderRadius?: number;
  style?: any;
}

export function Skeleton({ width = '100%', height = 20, borderRadius = 4, style }: SkeletonProps) {
  const opacity = useRef(new Animated.Value(0.3)).current;

  useEffect(() => {
    const animation = Animated.loop(
      Animated.sequence([
        Animated.timing(opacity, {
          toValue: 0.7,
          duration: 800,
          useNativeDriver: true,
        }),
        Animated.timing(opacity, {
          toValue: 0.3,
          duration: 800,
          useNativeDriver: true,
        }),
      ])
    );

    animation.start();

    return () => animation.stop();
  }, [opacity]);

  return (
    <Animated.View
      style={[
        styles.skeleton,
        {
          width,
          height,
          borderRadius,
          opacity,
        },
        style,
      ]}
    />
  );
}

export function SkeletonCard({ style }: { style?: any }) {
  return (
    <View style={[styles.card, style]}>
      <Skeleton width="60%" height={24} borderRadius={6} style={styles.mb8} />
      <Skeleton width="40%" height={16} borderRadius={4} style={styles.mb12} />
      <Skeleton width="100%" height={16} borderRadius={4} style={styles.mb8} />
      <Skeleton width="80%" height={16} borderRadius={4} />
    </View>
  );
}

export function SkeletonList({ count = 3, style }: { count?: number; style?: any }) {
  return (
    <View style={style}>
      {Array.from({ length: count }).map((_, index) => (
        <SkeletonCard key={index} style={styles.mb16} />
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  skeleton: {
    backgroundColor: 'rgba(139, 123, 247, 0.1)',
  },
  card: {
    backgroundColor: '#1A1F3E',
    borderRadius: 12,
    padding: 20,
    borderWidth: 1,
    borderColor: '#2D3561',
  },
  mb8: {
    marginBottom: 8,
  },
  mb12: {
    marginBottom: 12,
  },
  mb16: {
    marginBottom: 16,
  },
});
