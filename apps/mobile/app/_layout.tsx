/**
 * Root layout (Expo Router)
 */

import { Stack } from 'expo-router';
import { StatusBar } from 'expo-status-bar';

export default function RootLayout() {
  return (
    <>
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
        <Stack.Screen name="natal-chart" />
        <Stack.Screen name="lunar-month/[month]" />
        <Stack.Screen name="lunar/index" />
        <Stack.Screen name="lunar/report" />
        <Stack.Screen name="lunar/voc" />
        <Stack.Screen name="lunar-returns/timeline" />
        <Stack.Screen name="transits/overview" />
        <Stack.Screen name="transits/details" />
        <Stack.Screen name="calendar/month" />
        <Stack.Screen name="settings" />
        <Stack.Screen name="debug/selftest" />
      </Stack>
    </>
  );
}

