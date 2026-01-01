/**
 * Configuration centralisée de l'application
 */

import Constants from 'expo-constants';

// API Configuration
export const API_CONFIG = {
  BASE_URL: process.env.EXPO_PUBLIC_API_URL || 'http://127.0.0.1:8000',
  TIMEOUT: 30000, // 30 seconds
} as const;

// Feature Flags
export const FEATURES = {
  DEV_AUTH_BYPASS: process.env.EXPO_PUBLIC_DEV_AUTH_BYPASS === 'true',
  DEV_USER_ID: process.env.EXPO_PUBLIC_DEV_USER_ID || '1',
} as const;

// App Metadata
export const APP_INFO = {
  NAME: 'Lunation',
  VERSION: Constants.expoConfig?.version || '1.0.0',
  BUILD_NUMBER: Constants.expoConfig?.extra?.buildNumber || '1',
} as const;

// Storage TTL (Time To Live)
export const TTL = {
  CALENDAR: 5 * 60 * 1000, // 5 minutes
  VOC: 5 * 60 * 1000, // 5 minutes
  CYCLE: 5 * 60 * 1000, // 5 minutes
} as const;
