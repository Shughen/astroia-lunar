/**
 * Layout pour le flow onboarding
 */

import { Stack } from 'expo-router';

export default function OnboardingLayout() {
  return (
    <Stack
      screenOptions={{
        headerShown: false,
        contentStyle: { backgroundColor: '#1a0b2e' },
      }}
    >
      <Stack.Screen name="index" />
      <Stack.Screen name="profile-setup" />
      <Stack.Screen name="consent" />
      <Stack.Screen name="disclaimer" />
      <Stack.Screen name="cycle-setup" />
    </Stack>
  );
}
