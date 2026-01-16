/**
 * Root layout (Expo Router)
 */

import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { LogBox } from 'react-native';

// Ignore warning expo-notifications Android (Expo Go SDK 53+)
LogBox.ignoreLogs([
  'expo-notifications: Android Push notifications',
]);

// Initialize i18n (side effect import)
import '../i18n';

// Lunar Context Provider
import { LunarProvider } from '../contexts/LunarProvider';

export default function RootLayout() {
  // Vérifier que Stack est disponible au runtime
  if (!Stack) {
    console.error('[LAYOUT] Stack is undefined! Check expo-router installation.');
    return (
      <>
        <StatusBar style="light" />
        <React.Fragment>
          {/* Fallback si Stack n'est pas disponible */}
        </React.Fragment>
      </>
    );
  }

  return (
    <LunarProvider>
      <StatusBar style="light" />
      <Stack
        screenOptions={{
          headerShown: false,
          contentStyle: { backgroundColor: '#1a0b2e' },
        }}
      >
        <Stack.Screen name="index" />
        <Stack.Screen name="welcome" />
        <Stack.Screen name="onboarding" />
        <Stack.Screen name="login" />
        {/* Natal Chart screens - Stack routes (not tabs) for birth chart calculation and display */}
        <Stack.Screen name="natal-chart/index" />
        <Stack.Screen name="natal-chart/result" />
        <Stack.Screen name="lunar-month/[month]" />
        <Stack.Screen name="lunar/index" />
        <Stack.Screen name="lunar/report" />
        <Stack.Screen name="lunar/voc" />
        <Stack.Screen name="lunar-returns/timeline" />
        <Stack.Screen name="transits/overview" />
        <Stack.Screen name="transits/details" />
        <Stack.Screen name="calendar/month" />
        <Stack.Screen name="cycle/index" />
        <Stack.Screen name="cycle/history" />
        <Stack.Screen name="settings" />
        <Stack.Screen name="debug/selftest" />
      </Stack>
    </LunarProvider>
  );
}
