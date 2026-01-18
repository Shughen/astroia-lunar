/**
 * ToastContainer - Affiche les toasts/snackbars en bas de l'écran
 *
 * Fonctionnalités:
 * - Animation slide-in/out
 * - Auto-dismiss après durée configurable
 * - Couleurs selon le type (info, success, warning, error)
 * - Swipe pour dismiss (optionnel)
 */

import React, { useEffect, useRef } from 'react';
import {
  View,
  Text,
  StyleSheet,
  Animated,
  TouchableOpacity,
  Dimensions,
} from 'react-native';
import { useSafeAreaInsets } from 'react-native-safe-area-context';
import { useToastStore, Toast, ToastType } from '../stores/useToastStore';

const { width: SCREEN_WIDTH } = Dimensions.get('window');

// Couleurs par type de toast
const TOAST_COLORS: Record<ToastType, { bg: string; text: string; border: string }> = {
  info: {
    bg: 'rgba(59, 130, 246, 0.95)',
    text: '#FFFFFF',
    border: '#3B82F6',
  },
  success: {
    bg: 'rgba(34, 197, 94, 0.95)',
    text: '#FFFFFF',
    border: '#22C55E',
  },
  warning: {
    bg: 'rgba(245, 158, 11, 0.95)',
    text: '#1F2937',
    border: '#F59E0B',
  },
  error: {
    bg: 'rgba(239, 68, 68, 0.95)',
    text: '#FFFFFF',
    border: '#EF4444',
  },
};

// Icônes par type
const TOAST_ICONS: Record<ToastType, string> = {
  info: 'i',
  success: '✓',
  warning: '!',
  error: '✕',
};

interface ToastItemProps {
  toast: Toast;
  onDismiss: () => void;
}

function ToastItem({ toast, onDismiss }: ToastItemProps) {
  const translateY = useRef(new Animated.Value(100)).current;
  const opacity = useRef(new Animated.Value(0)).current;

  const colors = TOAST_COLORS[toast.type];
  const icon = TOAST_ICONS[toast.type];

  useEffect(() => {
    // Animate in
    Animated.parallel([
      Animated.spring(translateY, {
        toValue: 0,
        useNativeDriver: true,
        tension: 100,
        friction: 10,
      }),
      Animated.timing(opacity, {
        toValue: 1,
        duration: 200,
        useNativeDriver: true,
      }),
    ]).start();

    // Auto-dismiss animation
    const dismissTimeout = setTimeout(() => {
      Animated.parallel([
        Animated.timing(translateY, {
          toValue: 100,
          duration: 200,
          useNativeDriver: true,
        }),
        Animated.timing(opacity, {
          toValue: 0,
          duration: 200,
          useNativeDriver: true,
        }),
      ]).start();
    }, toast.duration - 200);

    return () => clearTimeout(dismissTimeout);
  }, [toast.duration]);

  return (
    <Animated.View
      style={[
        styles.toastItem,
        {
          backgroundColor: colors.bg,
          borderLeftColor: colors.border,
          transform: [{ translateY }],
          opacity,
        },
      ]}
    >
      <View style={[styles.iconContainer, { backgroundColor: colors.border }]}>
        <Text style={styles.iconText}>{icon}</Text>
      </View>
      <Text style={[styles.message, { color: colors.text }]} numberOfLines={2}>
        {toast.message}
      </Text>
      <TouchableOpacity onPress={onDismiss} style={styles.dismissButton}>
        <Text style={[styles.dismissText, { color: colors.text }]}>✕</Text>
      </TouchableOpacity>
    </Animated.View>
  );
}

export function ToastContainer() {
  const insets = useSafeAreaInsets();
  const { toasts, hideToast } = useToastStore();

  if (toasts.length === 0) {
    return null;
  }

  return (
    <View style={[styles.container, { bottom: insets.bottom + 16 }]}>
      {toasts.map((toast) => (
        <ToastItem
          key={toast.id}
          toast={toast}
          onDismiss={() => hideToast(toast.id)}
        />
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    left: 16,
    right: 16,
    zIndex: 9999,
    elevation: 9999,
  },
  toastItem: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingVertical: 12,
    paddingHorizontal: 12,
    borderRadius: 12,
    marginBottom: 8,
    borderLeftWidth: 4,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
  iconContainer: {
    width: 24,
    height: 24,
    borderRadius: 12,
    alignItems: 'center',
    justifyContent: 'center',
    marginRight: 10,
  },
  iconText: {
    color: '#FFFFFF',
    fontSize: 14,
    fontWeight: 'bold',
  },
  message: {
    flex: 1,
    fontSize: 14,
    fontWeight: '500',
    lineHeight: 18,
  },
  dismissButton: {
    marginLeft: 8,
    padding: 4,
  },
  dismissText: {
    fontSize: 16,
    fontWeight: '600',
    opacity: 0.8,
  },
});
