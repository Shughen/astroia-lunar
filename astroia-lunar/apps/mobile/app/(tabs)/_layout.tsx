/**
 * Tab Navigator Layout
 * 3 onglets: Mon Cycle, Calendrier, Profil
 */

import React from 'react';
import { Tabs } from 'expo-router';
import { View, StyleSheet, Platform } from 'react-native';
import Svg, { Path, Circle, Rect } from 'react-native-svg';
import { colors } from '../../constants/theme';

// Tab bar configuration
const TAB_BAR_HEIGHT = 70;
const ICON_SIZE = 24;

// CycleIcon - Lune simple pour "Mon Cycle"
function CycleIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE} height={ICON_SIZE} viewBox="0 0 24 24" fill="none">
      {/* Crescent moon */}
      <Path
        d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        strokeLinecap="round"
        strokeLinejoin="round"
        fill={focused ? `${color}30` : 'none'}
      />
      {/* Inner glow when focused */}
      {focused && (
        <Circle
          cx="14"
          cy="10"
          r="2"
          fill={color}
          opacity={0.4}
        />
      )}
    </Svg>
  );
}

// CalendarIcon
function CalendarIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE} height={ICON_SIZE} viewBox="0 0 24 24" fill="none">
      <Rect
        x="3"
        y="4"
        width="18"
        height="18"
        rx="2"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        fill={focused ? `${color}20` : 'none'}
      />
      <Path d="M3 10h18" stroke={color} strokeWidth={1.5} />
      <Path d="M8 2v4M16 2v4" stroke={color} strokeWidth={1.5} strokeLinecap="round" />
      {/* Moon phase dot */}
      <Circle cx="12" cy="15" r="2" fill={color} opacity={focused ? 1 : 0.6} />
    </Svg>
  );
}

// ProfileIcon
function ProfileIcon({ color, focused }: { color: string; focused: boolean }) {
  return (
    <Svg width={ICON_SIZE} height={ICON_SIZE} viewBox="0 0 24 24" fill="none">
      {/* Head */}
      <Circle
        cx="12"
        cy="8"
        r="4"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        fill={focused ? `${color}20` : 'none'}
      />
      {/* Body */}
      <Path
        d="M4 20c0-4 4-6 8-6s8 2 8 6"
        stroke={color}
        strokeWidth={focused ? 2 : 1.5}
        strokeLinecap="round"
        fill={focused ? `${color}20` : 'none'}
      />
    </Svg>
  );
}

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        headerShown: false,
        tabBarActiveTintColor: colors.gold,
        tabBarInactiveTintColor: colors.textMuted,
        tabBarStyle: styles.tabBar,
        tabBarLabelStyle: styles.tabBarLabel,
        tabBarItemStyle: styles.tabBarItem,
      }}
    >
      <Tabs.Screen
        name="home"
        options={{
          title: 'Mon Cycle',
          tabBarIcon: ({ color, focused }) => <CycleIcon color={color} focused={focused} />,
        }}
      />
      <Tabs.Screen
        name="calendar"
        options={{
          title: 'Calendrier',
          tabBarIcon: ({ color, focused }) => <CalendarIcon color={color} focused={focused} />,
        }}
      />
      <Tabs.Screen
        name="profile"
        options={{
          title: 'Profil',
          tabBarIcon: ({ color, focused }) => <ProfileIcon color={color} focused={focused} />,
        }}
      />
    </Tabs>
  );
}

const styles = StyleSheet.create({
  tabBar: {
    backgroundColor: '#1a0b2e',
    borderTopColor: 'rgba(183, 148, 246, 0.15)',
    borderTopWidth: 1,
    height: TAB_BAR_HEIGHT + (Platform.OS === 'ios' ? 20 : 0),
    paddingTop: 8,
    paddingBottom: Platform.OS === 'ios' ? 24 : 8,
  },
  tabBarLabel: {
    fontSize: 10,
    fontWeight: '500',
    marginTop: 4,
  },
  tabBarItem: {
    paddingVertical: 4,
  },
});
